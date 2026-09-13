#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve o PISO da secao 25.2 em todo registro publicavel do banco da Robometria.

    python3 ferramentas/gerar-busca-de-produto.py            # mostra o que mudaria
    python3 ferramentas/gerar-busca-de-produto.py --gravar   # grava

POR QUE ISTO EXISTE
-------------------
A secao 25.2 do ARQUIPELAGO.md decidiu, com a palavra do dono citada — "deve ser
100% automatico sem eu tocar" —, que o PISO de todo item publicavel e o link de
BUSCA, e que "nada, nunca, fica na fila esperando o Raphael". A corrente tem dois
elos e so um deles depende de alguem:

  1. ESCOLHER A PALAVRA-CHAVE .. nao depende de sessao nenhuma. E este arquivo.
  2. ENCURTAR a busca num link de afiliado .. exige a sessao logada do painel da
     Shopee, que mora no navegador do Raphael. Remedido desta nuvem em 13/09/2026
     as 19h17Z: affiliate.shopee.com.br/offer/custom_link responde 200 e serve
     casca de JavaScript com ZERO ocorrencia de `custom_link`.

O que este arquivo faz, entao, e tirar a ESCOLHA da fila de espera. No dia em que
houver sessao, os 62 itens publicaveis ja sabem por qual frase serao buscados, e o
que falta e colar. NENHUMA LINHA DE CODIGO MUDA naquele dia.

O QUE ELE NUNCA FAZ
-------------------
Nao inventa palavra. A chave e composta de campos que ja estao no banco, mais duas
coisas que moram no ESQUEMA e nao aqui dentro:

  . `nome_de_busca` da marca, em dados/marcas.json — porque nem o id nem o nome de
    tela servem para buscar (o id de duas das cinco marcas e palavra comum do
    portugues, e o nome de duas carrega parenteses ou tres tokens);
  . o TERMO DE CONTEXTO da entidade, em dados/esquema-banco.json.

A lista de termos mora no esquema pelo mesmo motivo que a lista de tipos saiu de
dentro da regua da funcao em 13/09/2026: lista dentro da regua envelhece calada, e
entidade nova entraria sem termo nenhum com o banco verde. Aqui, entidade sem termo
declarado e ERRO e este arquivo PARA — nunca compoe busca so por marca, que e a
armadilha que a 25.3 nomeia.

A ASSIMETRIA ENTRE AS DUAS ENTIDADES E DE PROPOSITO
---------------------------------------------------
MODELO leva o codigo (Electrolux ERB60 robo aspirador) porque o codigo do modelo E
o nome comercial do produto: ninguem vende "Electrolux robo aspirador". PECA nao
leva (WAP escova lateral robo aspirador) porque o codigo de peca e SKU interno de
fabricante e o vendedor de marketplace nao o digita no titulo. Chave com token que
o vendedor nao usa traz ZERO resultado, e busca com zero resultado e o beco sem
saida que o piso existe para impedir. O raciocinio inteiro, com a medicao que falta
e com quem vai poder fazer ela um dia, esta em
esquema-banco.json > afiliado > escada_de_compra > por_que_a_peca_nao_leva_o_codigo.
"""
import json
import os
import sys
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# entidade do esquema -> arquivo do banco. A chave e a MESMA string que o esquema
# usa em termo_de_contexto_por_entidade, para que entidade nova nao possa entrar
# aqui sem entrar la.
ARQUIVOS = {
    "modelo_robo": "dados/modelos-robo.json",
    "peca": "dados/pecas.json",
}

# A ordem canonica do campo afiliado. Ela existe para o diff de amanha ser legivel:
# dicionario de JSON nao tem ordem obrigatoria, mas arquivo de repositorio tem
# historia, e campo que pula de lugar a cada passada faz o git mostrar dez linhas
# onde uma mudou.
ORDEM_AFILIADO = [
    "url", "url_produto", "motivo_sem_url_produto", "degrau",
    "url_busca", "url_busca_produto", "motivo_sem_url_busca",
    "plataforma", "coletado_em", "sub_id_1",
]

MOTIVO_SEM_URL_BUSCA = (
    "falta o ENCURTAMENTO, nao a escolha: gerar o link de afiliado da busca exige a "
    "sessao logada do painel da Shopee (25.6). A palavra-chave ja esta escrita em "
    "url_busca_produto, e no dia da sessao e colar."
)


def caminho(rel):
    return os.path.join(RAIZ, rel)


def carregar(rel):
    with open(caminho(rel), encoding="utf-8") as fh:
        return json.load(fh)


def indentacao_do_arquivo(rel):
    """Quantos espacos o arquivo ja usa. Os dois bancos desta ilha NAO concordam —
    modelos-robo.json nasceu com 2 e pecas.json com 1 — e regravar com a indentacao
    errada reescreveria o arquivo inteiro num diff de milhares de linhas, escondendo
    as poucas que este bloco de fato mudou."""
    with open(caminho(rel), encoding="utf-8") as fh:
        fh.readline()
        segunda = fh.readline()
    return len(segunda) - len(segunda.lstrip(" "))


def gravar(rel, dados, indent):
    with open(caminho(rel), "w", encoding="utf-8") as fh:
        json.dump(dados, fh, ensure_ascii=False, indent=indent)
        fh.write("\n")


def palavra_chave(registro, entidade, nome_de_busca, termo):
    """marca + (codigo, so no modelo) + (tipo, so na peca) + contexto.

    A ordem e a de quem digita na loja: a marca primeiro porque e o filtro mais
    forte, o que distingue o item depois, e o contexto por ultimo porque e
    desempate, nao busca.
    """
    partes = [nome_de_busca]
    if entidade == "modelo_robo":
        partes.append(str(registro.get("codigo_fabricante") or "").strip())
    else:
        partes.append(str(registro.get("tipo") or "").strip())
    partes.append(termo)
    return " ".join(p for p in (x.strip() for x in partes) if p)


def afiliado_normalizado(atual):
    """O campo com as dez chaves da versao 5 do esquema, na ordem canonica, sem
    perder o que ja estava escrito."""
    atual = dict(atual or {})
    novo = {}
    for chave in ORDEM_AFILIADO:
        if chave in atual:
            novo[chave] = atual.pop(chave)
        elif chave in ("url", "url_busca", "url_busca_produto"):
            novo[chave] = ""
        elif chave == "sub_id_1":
            novo[chave] = "robometria"
        else:
            novo[chave] = None
    # Chave que nao esta na forma do esquema NAO some em silencio: ela volta para o
    # dicionario e o validador reprova. Sumir com dado que alguem escreveu e pior do
    # que reprovar alto — foi essa a regra que fez o sub_id_2 ser REPROVADO em vez de
    # apagado em 12/09/2026.
    novo.update(atual)
    return novo


def main():
    gravando = "--gravar" in sys.argv
    esquema = carregar("dados/esquema-banco.json")
    marcas = carregar("dados/marcas.json")

    escada = esquema["tipos_compostos"]["afiliado"]["escada_de_compra"]
    base = escada["base_da_busca"]
    termos = escada["termo_de_contexto_por_entidade"]

    nomes_de_busca = {}
    erros = []
    for m in marcas["registros"]:
        nome = (m.get("nome_de_busca") or "").strip()
        if not nome:
            erros.append("marcas.json/%s: sem nome_de_busca. Marca muda faria a chave "
                         "sair sem marca, e busca sem marca nao e busca de produto"
                         % m["id"])
        nomes_de_busca[m["id"]] = nome

    mudou = igual = total = 0
    for entidade, rel in ARQUIVOS.items():
        termo = (termos.get(entidade) or "").strip()
        if not termo:
            # A trava que faz a regra valer: entidade nova sem termo PARA aqui, em
            # vez de gerar uma busca so por marca (25.3).
            erros.append("esquema-banco.json: entidade %r sem termo de contexto em "
                         "escada_de_compra.termo_de_contexto_por_entidade" % entidade)
            continue

        indent = indentacao_do_arquivo(rel)
        arquivo = carregar(rel)
        for reg in arquivo["registros"]:
            total += 1
            afil = afiliado_normalizado(reg.get("afiliado"))

            if reg.get("status") != "publicavel":
                # Registro nao publicavel nao tem pagina, entao nao tem piso a
                # cumprir — e escrever "robo aspirador" na busca de um aspirador
                # vertical seria afirmacao falsa dentro do banco.
                nova_busca, novo_motivo = "", None
            else:
                nome = nomes_de_busca.get(reg.get("marca"), "")
                if not nome:
                    erros.append("%s/%s: marca %r sem nome_de_busca"
                                 % (rel, reg.get("id"), reg.get("marca")))
                    continue
                chave = palavra_chave(reg, entidade, nome, termo)
                nova_busca = base + quote(chave)
                novo_motivo = None if afil.get("url_busca") else MOTIVO_SEM_URL_BUSCA

            antes = (afil.get("url_busca_produto"), afil.get("motivo_sem_url_busca"),
                     reg.get("afiliado"))
            afil["url_busca_produto"] = nova_busca
            afil["motivo_sem_url_busca"] = novo_motivo
            depois = (nova_busca, novo_motivo, afil)

            if antes[0] == depois[0] and antes[1] == depois[1] and antes[2] == afil:
                igual += 1
            else:
                mudou += 1
                if reg.get("status") == "publicavel":
                    print("  %-52s %s" % (reg.get("id"),
                                          palavra_chave(reg, entidade,
                                                        nomes_de_busca[reg["marca"]],
                                                        termo)))
            reg["afiliado"] = afil

        if gravando and not erros:
            gravar(rel, arquivo, indent)

    print("\n%d registro(s): %d ja estava(m) com o piso escrito, %d %s"
          % (total, igual, mudou,
             "gravado(s)" if (gravando and not erros) else "a gravar (rode com --gravar)"))
    for e in erros:
        print("  ERRO %s" % e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

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

O QUE O DESPACHO DO RAPHAEL DE 14/09/2026 ACRESCENTOU AQUI
-----------------------------------------------------------
Ate 14/09 este arquivo escrevia a PALAVRA-CHAVE e parava. O degrau ficava `null` em
65 de 65 registros publicaveis, e `null` no degrau quer dizer "ninguem decidiu" —
quando a verdade era o contrario: a decisao estava tomada havia um dia inteiro e so
nao estava escrita. Degrau em branco num item que TEM piso e a mesma familia do
numero de tela digitado: parece pendencia e e dado que ninguem gravou.

Agora o degrau sai CONTADO do proprio campo, nunca digitado:

  . tem `url` (ficha de produto) .... o degrau e 1, 2 ou 3 e quem o escolheu foi
    quem escolheu a ficha. Este arquivo NAO o toca: ele nao sabe se a URL e loja
    oficial, catalogo do Mercado Livre ou anuncio de vendedor, e adivinhar isso
    pelo formato do link e exatamente o que o esquema proibe em `degrau`.
  . nao tem ficha e tem piso ....... degrau 4, com `conferido_em` do dia. E a
    leitura honesta da escada da 25.1: ela parou na busca.

E o campo `intestavel` da 25.4-b nasce junto, pelo item 3 daquele despacho. Ele e
DERIVADO, nunca opinado: ha link encurtado (`url`) e nao ha a URL crua do produto
(`url_produto`) que a ronda precisaria abrir. Hoje ele e `false` em 65 de 65, porque
nenhum item tem link encurtado — e e por isso que a mutacao que o mede PRODUZ o
mundo em vez de esperar por ele (secao 8 do ARQUIPELAGO.md).
"""
import json
import os
import sys
from datetime import date
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
    "url", "url_produto", "motivo_sem_url_produto", "intestavel", "degrau",
    "conferido_em", "url_busca", "url_busca_produto", "motivo_sem_url_busca",
    "plataforma", "coletado_em", "sub_id_1",
]

# O degrau do PISO, com o nome que a 25.1 lhe deu. Escrito aqui a mao de proposito:
# quem confere escreve a propria regua, e teste-escada-compra.py compara este numero
# com o do esquema por outro caminho.
DEGRAU_DO_PISO = 4

# Onde mora a medicao da palavra-chave (16/09/2026). Ver carregar_medicao().
MEDICAO = "dados/palavras-chave-medidas.json"

HOJE = date.today().isoformat()

# ESTE MOTIVO FICOU RARO EM 16/09/2026, e a frase mudou junto. Ate aquele dia ele
# era a verdade de 65 registros: a escolha estava feita e o ENCURTAMENTO esperava
# a sessao logada do painel da Shopee. A Open API da 25.6 tem generateShortLink,
# aceita sub-id, e fecha o elo — entao o motivo deixou de descrever a fabrica e
# passou a descrever a falha: registro que chega aqui sem link curto e registro
# que a medicao nao alcancou.
MOTIVO_SEM_URL_BUSCA = (
    "sem link curto: a medicao de palavra-chave (dados/palavras-chave-medidas.json) "
    "nao cobre este registro. Rode ferramentas/medir-palavras-chave.py --gravar "
    "--encurtar com a credencial da Open API no ambiente."
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


def carregar_medicao():
    """A chave MEDIDA de cada registro, quando existir.

    `ferramentas/medir-palavras-chave.py` chama a Open API da Shopee e desce uma
    escada ate achar a chave que serve o leitor; o resultado, com a data e com o
    que a API devolveu, mora em `dados/palavras-chave-medidas.json`. Este arquivo
    continua sendo quem GRAVA, e continua sendo deterministico e conferivel sem
    rede — ele nao chama ninguem, so le o que ja foi medido.

    Arquivo ausente nao e erro: a ilha nasceu sem ele e a composicao de sempre
    continua valendo. O que seria erro e o contrario — gravar uma chave que
    ninguem chamou, que foi como tres buscas de ZERO resultado ficaram um dia
    inteiro no ar com o botao de compra em cima delas (item 1 do despacho da
    Sentinela de 16/09/2026).
    """
    try:
        doc = carregar(MEDICAO)
    except FileNotFoundError:
        return {}, None
    por_id = {}
    for reg in doc.get("registros", []):
        escolhido = reg.get("escolhido") or {}
        if escolhido.get("chave"):
            por_id[reg["id"]] = escolhido
    return por_id, doc.get("gerado_em")


def palavra_chave(registro, entidade, nome_de_busca, termo, medida=None):
    """marca + (codigo, so no modelo) + (tipo, so na peca) + contexto — ou a
    chave MEDIDA, quando a medicao provou que a composicao de sempre nao serve.

    A ordem e a de quem digita na loja: a marca primeiro porque e o filtro mais
    forte, o que distingue o item depois, e o contexto por ultimo porque e
    desempate, nao busca.
    """
    if medida and medida.get("chave"):
        return medida["chave"]
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
        elif chave == "intestavel":
            novo[chave] = False
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
    medidas, medido_em = carregar_medicao()
    if medidas:
        print("chave medida disponivel para %d registro(s), medicao de %s"
              % (len(medidas), medido_em))

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
                medida = medidas.get(reg.get("id"))
                chave = palavra_chave(reg, entidade, nome, termo, medida)
                nova_busca = base + quote(chave)
                # O LINK CURTO VEM DA MEDICAO, e so dela. Ele e o segundo elo do
                # piso da 25.2, e ate 16/09/2026 era o elo que esperava alguem.
                # Nunca se escreve link curto para uma chave que nao foi a
                # medida: link curto e chave sao um par, e trocar um sem o outro
                # e mandar o leitor para a busca de ontem com o carimbo de hoje.
                if medida and medida.get("url_busca") and medida.get("url_busca_produto") == nova_busca:
                    afil["url_busca"] = medida["url_busca"]
                elif afil.get("url_busca") and afil.get("url_busca_produto") != nova_busca:
                    # A CHAVE MUDOU E O LINK CURTO NAO ACOMPANHOU: ELE CAI.
                    #
                    # O paragrafo acima dizia, desde 16/09/2026, que "link curto e
                    # chave sao um par, e trocar um sem o outro e mandar o leitor
                    # para a busca de ontem com o carimbo de hoje" — e o codigo so
                    # cumpria METADE disso: recusava escrever link curto de chave
                    # alheia, e MANTINHA calado o link curto que ja estava no
                    # registro quando a chave debaixo dele mudava. Enquanto a unica
                    # forma de trocar chave foi a propria medicao (que devolve as
                    # duas coisas juntas), o buraco nunca abriu. Ele abriu em
                    # 20/09/2026, quando o despacho do Raphael trocou 28 chaves
                    # medidas NO NAVEGADOR sem que a Open API estivesse ao alcance
                    # para reencurtar: os 28 registros teriam servido o botao de
                    # ontem sobre a palavra de hoje, que e exatamente o defeito que
                    # o despacho mandou consertar.
                    afil["url_busca"] = ""
                novo_motivo = None if afil.get("url_busca") else MOTIVO_SEM_URL_BUSCA
                # O MOTIVO SAI DA MEDICAO QUANDO A MEDICAO O ESCREVEU. O texto
                # padrao deste arquivo diz "a medicao nao cobre este registro", e
                # isso seria FALSO num registro que a medicao cobre e que so nao
                # tem link curto porque a credencial da Open API faltou no ambiente
                # do dia. Motivo errado e pior que motivo generico: a proxima
                # execucao le "rode a ferramenta" e a ferramenta nao e o conserto.
                if novo_motivo and medida and medida.get("motivo_sem_url_busca") \
                        and medida.get("url_busca_produto") == nova_busca:
                    novo_motivo = medida["motivo_sem_url_busca"]

            antes = (afil.get("url_busca_produto"), afil.get("motivo_sem_url_busca"),
                     reg.get("afiliado"))
            afil["url_busca_produto"] = nova_busca
            afil["motivo_sem_url_busca"] = novo_motivo

            # O DEGRAU E O `intestavel` SAO DERIVADOS DO PROPRIO CAMPO, nunca
            # digitados — item 2 e item 3 do despacho do Raphael de 14/09/2026.
            tem_ficha = bool((afil.get("url") or "").strip())
            afil["intestavel"] = bool(tem_ficha and not (afil.get("url_produto") or ""))
            if tem_ficha:
                # Ficha e degrau 1, 2 ou 3, e quem sabe qual e quem a escolheu. Ler o
                # degrau pelo formato do link curto e o que o esquema proibe: o mesmo
                # encurtador serve loja oficial e anuncio de vendedor com a mesma cara.
                pass
            elif nova_busca:
                # `conferido_em` e o dia em que ESTE degrau foi decidido, e por isso
                # so e escrito quando ele muda. Carimbar a data de hoje a cada passada
                # faria o campo dizer "conferido hoje" sem que nada tivesse sido
                # conferido — numero de tela digitado com outro nome — e encheria o
                # diff de 65 linhas por execucao.
                if afil.get("degrau") != DEGRAU_DO_PISO or not afil.get("conferido_em"):
                    afil["conferido_em"] = HOJE
                afil["degrau"] = DEGRAU_DO_PISO
            else:
                # Sem pagina nao ha piso a cumprir, entao nao ha degrau a declarar.
                afil["degrau"] = None
                afil["conferido_em"] = None

            depois = (nova_busca, novo_motivo, afil)

            if antes[0] == depois[0] and antes[1] == depois[1] and antes[2] == afil:
                igual += 1
            else:
                mudou += 1
                if reg.get("status") == "publicavel":
                    print("  %-52s %s" % (reg.get("id"),
                                          palavra_chave(reg, entidade,
                                                        nomes_de_busca[reg["marca"]],
                                                        termo,
                                                        medidas.get(reg.get("id")))))
            reg["afiliado"] = afil

        # A CONTAGEM DE DIVIDA DO CABECALHO ANDA JUNTO COM O CAMPO QUE ELA CONTA.
        # `itens_com_piso_nao_rastreavel` conta quem tem busca crua e nao tem link
        # curto — exatamente o que este arquivo acabou de mexer. Ate 16/09/2026 o
        # numero era escrito a mao e so o `validar-banco.py` o conferia: encher os
        # cinco modelos de link curto deixou o cabecalho dizendo 5 com o arquivo em
        # 0, e a gravacao passou no gerador e reprovou no validador. Contar aqui
        # nao afrouxa portao nenhum — o validador continua recontando por outro
        # caminho, e a mutacao que mente no numero continua reprovando.
        publicaveis = [r for r in arquivo["registros"] if r.get("status") == "publicavel"]
        contagem = arquivo.get("contagem")
        if isinstance(contagem, dict) and "itens_com_piso_nao_rastreavel" in contagem:
            contagem["itens_com_piso_nao_rastreavel"] = sum(
                1 for r in publicaveis
                if not (r["afiliado"].get("url") or "")
                and not (r["afiliado"].get("url_busca") or "")
                and (r["afiliado"].get("url_busca_produto") or ""))

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

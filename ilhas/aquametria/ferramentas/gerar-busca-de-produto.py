#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve `afiliado.url_busca_produto` em todo produto do banco da Aquametria.

POR QUE ISTO EXISTE. A secao 25.2 do ARQUIPELAGO.md decidiu que o PISO de todo
item e o link de busca, e que "o piso nunca depende de ninguem". A corrente
inteira tem dois elos: escolher a PALAVRA-CHAVE e ENCURTAR a busca num link de
afiliado. O segundo elo exige a sessao logada do painel da Shopee, que mora no
navegador do Raphael — medido desta nuvem em 13/09/2026, em duas passadas:
affiliate.shopee.com.br/offer/custom_link responde 200 e serve uma casca de
JavaScript com ZERO ocorrencia de `custom_link`, de `sub_id` e de `input`. O
primeiro elo nao depende de sessao nenhuma, e e este arquivo.

O que ele faz, entao, e tirar a ESCOLHA da fila de espera: no dia em que houver
sessao, os 78 itens ja sabem por qual frase serao buscados, e o que falta e
colar. Nenhuma linha de codigo muda naquele dia.

O QUE ELE NUNCA FAZ. Nao inventa palavra: a frase e composta de campos que ja
estao no banco (marca e modelo) mais o termo de contexto da ENTIDADE, que mora
em dados/esquema-produtos.json e nao aqui dentro. A 25.3 e explicita — "nunca
filtre o feed so por marca", porque JBL e caixa de som e e aquario, Aquario e
roteador e e peixe, Betta e peixe e e movel. E a lista de termos mora no esquema
pelo mesmo motivo que a Robometria tirou a lista de tipos de dentro da regua em
13/09/2026: lista dentro da regua envelhece calada, e uma entidade nova entraria
sem termo nenhum com o banco verde. Aqui, entidade sem termo declarado e ERRO.

Rodar sem argumento mostra o que mudaria; com --gravar, grava.
"""
import json
import os
import sys
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
ARQUIVOS = {
    "filtro": "dados/produtos-filtro.json",
    "aquecedor": "dados/produtos-aquecedor.json",
    "iluminacao": "dados/produtos-iluminacao.json",
    "midia": "dados/produtos-midia.json",
}


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return json.load(f)


def gravar(caminho, dados):
    with open(os.path.join(RAIZ, caminho), "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        f.write("\n")


def palavra_chave(produto, termo):
    """marca + modelo + contexto, nesta ordem, sem campo vazio e sem espaco duplo.

    A ordem importa e e a ordem de quem digita na loja: a marca primeiro porque
    e o filtro mais forte, o modelo depois porque e o que distingue a variante,
    e o contexto por ultimo porque e desempate, nao busca.
    """
    partes = [str(produto.get("marca") or "").strip(),
              str(produto.get("modelo") or "").strip(),
              termo.strip()]
    return " ".join(p for p in partes if p)


def url_da_busca(base, chave):
    return base + quote(chave)


def main():
    gravando = "--gravar" in sys.argv
    esquema = carregar(os.path.relpath(ESQUEMA, RAIZ))
    escada = esquema["afiliado"]["escada_de_compra"]
    base = escada["base_da_busca"]
    termos = escada["termo_de_contexto_por_entidade"]

    erros = []
    mudou = 0
    igual = 0
    total = 0

    for entidade, caminho in ARQUIVOS.items():
        termo = termos.get(entidade)
        if not termo:
            # A trava que faz a V27 valer alguma coisa: entidade nova sem termo
            # declarado PARA aqui, em vez de gerar uma busca so por marca.
            erros.append("entidade '%s' sem termo de contexto no esquema" % entidade)
            continue

        arquivo = carregar(caminho)
        for produto in arquivo.get("produtos", []):
            total += 1
            afil = produto.setdefault("afiliado", {})
            chave = palavra_chave(produto, termo)
            nova = url_da_busca(base, chave)
            atual = afil.get("url_busca_produto")
            if atual == nova:
                igual += 1
                continue
            mudou += 1
            print("  %-28s %s" % (produto.get("id"), chave))
            afil["url_busca_produto"] = nova

        if gravando:
            gravar(caminho, arquivo)

    print("\n%d produto(s): %d ja estava(m) com a busca escrita, %d %s"
          % (total, igual, mudou, "gravado(s)" if gravando else "a gravar (rode com --gravar)"))
    for e in erros:
        print("  ERRO %s" % e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

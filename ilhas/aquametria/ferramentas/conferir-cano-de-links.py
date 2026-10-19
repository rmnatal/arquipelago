#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — este confere o REPOSITORIO, nao o site.

O CANO DE LINKS DESTA ILHA ESTA CONTADO E DECLARADO, ITEM POR ITEM?

    python3 ferramentas/conferir-cano-de-links.py
    python3 ferramentas/conferir-cano-de-links.py --gravar

POR QUE ELE EXISTE, e a data e 19/10/2026
-----------------------------------------
O cano de links e o caminho do dinheiro desta ilha: `url_busca` e o PISO da
25.2 ("nunca depende de ninguem"), `url_produto` e a ficha que paga comissao,
e o `degrau` diz em que altura da escada da 25.1 cada registro parou. Esses
numeros eram contados por `contar-cano-de-links.py`, que escreve um relatorio
DATADO — e so isso. Duas consequencias, as duas escritas no repositorio antes
desta passada:

  * A `bancada.py` denunciava o contador desde 14/10/2026 — "SEM CONVENCAO,
    ninguem roda". A denuncia estava certa: a contagem do cano nao era
    exercitada por portao nenhum e nao tinha teste.
  * A ronda da Sentinela de 14/10/2026 RECONTOU os quatro bancos a mao para
    conferir o relatorio. Recontagem a mao e a assinatura de instrumento sem
    portao — quando existe portao, ninguem reconta.

E o aviso que a 25.2-b do ARQUIPELAGO.md deixou escrito, medido na Robometria
em 18/09/2026 e valido para toda ilha: em 16/09 aquele banco tinha 73
publicaveis e ZERO sem piso rastreavel; em 18/09 tinha 95 e 22 sem. "Ninguem
quebrou nada — a ilha cresceu mais rapido que os proprios acabamentos, e cada
leva nova entrou pela porta de tras. Isso nao e defeito de codigo, e defeito de
PORTAO, e portao que nao existe deixa passar sempre."

O QUE ELE AFIRMA
----------------
  1. A contagem leu TODOS os bancos que existem na pasta `dados/`, e leu
     registro. Esta e a primeira de proposito: "0 sem piso" sobre zero banco
     lido e VERDE VAZIO, e verde vazio e a unica forma de este portao mentir
     sem ninguem editar uma linha.
  2. O cano medido e o DECLARADO sao o mesmo, item por item: nenhum registro
     novo sem declaracao, nenhum registro sumido, e nenhum registro que mudou
     de degrau, de piso, de ficha ou de bandeira `intestavel` em silencio.
  3. Os totais da declaracao saem das frases de estado dela e nao de um numero
     digitado ao lado — declaracao cujo total nao fecha com os proprios itens
     nao e declaracao, e a mesma familia do `total_de_linhas` da serie da
     deriva.

E O QUE ELE NAO FAZ, de proposito
---------------------------------
Nao julga registro, um por um: quem reprova registro publicavel sem piso e a
regra V26 do `validar-produtos.py`, e quem confere a coerencia da bandeira
`intestavel` e a V25. Reescrever essas regras aqui seria a terceira regua da
mesma coisa — a cicatriz que esta pasta mediu em 16/10/2026 ("agora a regua e
uma so" era falso no dia em que foi escrito: ela era QUATRO). Este portao
pergunta outra coisa, que nenhuma das duas pergunta: **o cano de hoje e o cano
que alguem declarou?**

Nao abre rede e nao testa link: teste de vida e o portao da 25.4.

QUANDO ELE FICA VERMELHO, O CONSERTO E UM COMANDO
--------------------------------------------------
Entrou leva nova no banco, um registro ganhou ficha, um link morreu e desceu de
degrau? `--gravar` escreve a secao nova da serie, com a data, e o portao volta
a verde — e a serie passa a mostrar, por data, como o cano desta ilha andou. O
que ele recusa e o silencio: cano que mudou e ninguem contou nem declarou.
"""
import importlib.util
import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
SERIE = os.path.join(RAIZ, "dados", "cano-de-links.md")

GRAVAR = "--gravar" in sys.argv[1:]


def carregar_regua():
    caminho = os.path.join(FERRAMENTAS, "regua-cano-de-links.py")
    spec = importlib.util.spec_from_file_location("regua_cano_de_links", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()

falhas = []


def ok(rotulo, condicao, detalhe=""):
    if condicao:
        print("  ok   %s" % rotulo)
    else:
        print("  FALHA %s%s" % (rotulo, (" — " + detalhe) if detalhe else ""))
        falhas.append(rotulo)


def cabecalho_da_serie():
    return (
        "# Serie do CANO DE LINKS — Aquametria\n"
        "\n"
        "Em que degrau da escada de compra (secao 25.1 do `ARQUIPELAGO.md`) cada\n"
        "registro dos `dados/produtos-*.json` parou. Escreve aqui o\n"
        "`ferramentas/conferir-cano-de-links.py --gravar`; quem confere e o mesmo\n"
        "arquivo sem a opcao, e ele compara ITEM POR ITEM, nao pelo total.\n"
        "\n"
        "**Secao nova vai no TOPO** (a serie cresce por cima, como `dados/posicoes.md`\n"
        "e `dados/deriva-do-catalogo.md`) e secao antiga NUNCA e sobrescrita: a serie so\n"
        "vale porque cresce. O bloco `json` de cada secao e a declaracao que o portao\n"
        "le — o primeiro do arquivo e o que manda.\n"
        "\n"
        "A frase de estado de cada item se le assim: `piso` e ter `afiliado.url_busca`\n"
        "(o piso da 25.2, que nunca depende de ninguem), `ficha` e ter `url_produto` (o\n"
        "degrau que paga comissao e o unico que o teste de vida da 25.4 alcanca),\n"
        "`anuncio` e ter `url`, `degrau` e o degrau declarado (`-` e nulo) e\n"
        "`intestavel` e a bandeira da 25.4-b.\n"
        "\n"
        "Cano que muda **nao e defeito**: coleta nova, link que morreu e ficha que\n"
        "chegou movem estes numeros por desenho. O que e defeito e cano que mudou e\n"
        "ninguem contou — e era o que acontecia antes de 19/10/2026, quando a contagem\n"
        "saia em relatorio datado que nada comparava com o do dia anterior.\n"
    )


def gravar(contagem, agora):
    dados = {
        "medido_em": agora,
        "bancos": contagem["bancos"],
        "totais": contagem["totais"],
        "degraus": contagem["degraus"],
        "itens": contagem["itens"],
    }
    t = contagem["totais"]
    secao = ["## %s" % agora, ""]
    secao.append("**%d registro(s)** em %d banco(s) de produto." % (t["registros"], len(contagem["bancos"])))
    secao.append("")
    secao.append("| o que | quantos |")
    secao.append("|---|---|")
    secao.append("| sem `afiliado.url_busca` — o piso da 25.2 | **%d** |" % t["sem_url_busca"])
    secao.append("| sem `afiliado.url_produto` — a ficha que paga comissao | **%d** |" % t["sem_url_produto"])
    secao.append("| com `url` e **sem** `url_produto` — a divida da 25.4-b | **%d** |" % t["url_sem_url_produto"])
    secao.append("| com `intestavel: true` | **%d** |" % t["intestaveis"])
    secao.append("")
    secao.append("**Por `degrau`:** %s" % ", ".join(
        "%s = %d" % ("nulo" if d == "-" else d, contagem["degraus"][d])
        for d in sorted(contagem["degraus"], key=lambda x: (x == "-", x))))
    secao += ["", "```json", json.dumps(dados, ensure_ascii=False, indent=2, sort_keys=True), "```", ""]
    novo = "\n".join(secao) + "\n"

    if os.path.exists(SERIE):
        antigo = regua.ler(SERIE)
        corte = antigo.find("\n## ")
        if corte == -1:
            texto = antigo.rstrip("\n") + "\n\n" + novo
        else:
            texto = antigo[:corte + 1] + "\n" + novo + antigo[corte + 1:]
    else:
        texto = cabecalho_da_serie() + "\n" + novo
    with open(SERIE, "w", encoding="utf-8") as f:
        f.write(texto)
    print("serie gravada: %s" % os.path.relpath(SERIE, RAIZ))


def main():
    agora = time.strftime("%Y-%m-%d %H:%MZ", time.gmtime())
    print("CANO DE LINKS — contado dos bancos do repositorio, %s" % agora)
    print("")

    contagem = regua.contar(RAIZ)
    t = contagem["totais"]

    existentes = [os.path.basename(c) for c in regua.bancos(RAIZ)]
    ok("a contagem leu todos os bancos de produto da pasta dados/ (%d)" % len(existentes),
       contagem["bancos"] == existentes and len(existentes) > 0,
       "lidos %s, existentes %s" % (contagem["bancos"], existentes))
    ok("a contagem achou registro (verde vazio nao passa por aprovado)",
       t["registros"] > 0,
       "%d registro(s)" % t["registros"])

    print("")
    print("CANO MEDIDO: %d registro(s) — sem piso %d, sem ficha %d, url sem ficha %d, intestavel %d"
          % (t["registros"], t["sem_url_busca"], t["sem_url_produto"],
             t["url_sem_url_produto"], t["intestaveis"]))
    print("  por degrau: %s" % ", ".join(
        "%s = %d" % ("nulo" if d == "-" else d, contagem["degraus"][d])
        for d in sorted(contagem["degraus"], key=lambda x: (x == "-", x))))
    for banco, linha in sorted(contagem["por_banco"].items()):
        print("  %-26s %3d registro(s), %d sem piso, %d sem ficha"
              % (banco, linha["n"], linha["sem_busca"], linha["sem_produto"]))
    print("")

    if GRAVAR:
        gravar(contagem, agora)
        return 0 if not falhas else 1

    declarado = regua.declaracao(SERIE)
    ok("a serie do cano tem declaracao", declarado is not None,
       "escreva a primeira com --gravar")
    novos, sumidos, mudados = regua.comparar_com_declaracao(contagem["itens"], declarado)
    ok("o cano medido e o declarado sao o mesmo, item por item",
       not novos and not sumidos and not mudados,
       "novos: %s | sumidos: %s | mudados: %s" % (novos[:3], sumidos[:3], mudados[:3]))
    if declarado is not None:
        declarados = declarado.get("itens", {})
        ok("os totais declarados saem dos itens declarados, e nao de um numero ao lado",
           declarado.get("totais") == regua.totais(declarados)
           and declarado.get("degraus") == regua.degraus(declarados),
           "totais %s contra %s" % (declarado.get("totais"), regua.totais(declarados)))

    print("")
    if falhas:
        print("REPROVADO: %d afirmacao(oes)" % len(falhas))
        for f in falhas:
            print("  - %s" % f)
        print("")
        print("Se o cano mudou de proposito (coleta nova, ficha que chegou, link que morreu),")
        print("grave a secao nova da serie: conferir-cano-de-links.py --gravar")
        return 1
    print("APROVADO: cano de %d registro(s), contado dos bancos e declarado item por item."
          % t["registros"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

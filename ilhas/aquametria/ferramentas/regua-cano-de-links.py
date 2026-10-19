#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: conta o CANO DE LINKS desta ilha a partir dos
`dados/produtos-*.json` de uma RAIZ — a de verdade ou uma de sombra.

Nao afirma nada sozinha. Quem afirma e `conferir-cano-de-links.py` (bancada,
sem rede); quem a exercita contra bancos encenados e `teste-cano-de-links.py`;
e quem a usa para escrever o relatorio datado do despacho de 07/10/2026 e
`contar-cano-de-links.py`. Ela mora num arquivo so porque, antes de hoje, a
contagem morava DENTRO do contador — e contagem que mora dentro de quem
imprime o relatorio nao pode ser rodada contra um banco encenado, portanto nao
pode ser testada por nada.

POR QUE ESTE ARQUIVO EXISTE, e a data e 19/10/2026
--------------------------------------------------
Dois sinais, os dois escritos no repositorio antes desta passada:

  1. A `bancada.py` denuncia `contar-cano-de-links.py` desde 14/10/2026 —
     "SEM CONVENCAO, ninguem roda" — e a denuncia estava certa: o arquivo que
     produz os quatro numeros do cano de links desta ilha nao era rodado por
     portao nenhum, e a contagem dele nao tinha teste.

  2. A ronda da Sentinela de 14/10/2026 RECONTOU os quatro bancos a mao para
     conferir o relatorio ("a ronda recontou os quatro `dados/produtos-*.json`
     do `main` por conta propria: 78 registros, 0 sem `url_busca`, 43 sem
     `url_produto`..."). Recontagem a mao e a assinatura de instrumento sem
     portao: quando existe portao, ninguem reconta.

A RAIZ PARAMETRIZADA E O PONTO
------------------------------
Toda funcao daqui recebe a raiz. Com isso o portao conta a ilha de verdade e o
teste conta bancos de mentira, com a MESMA conta — e nao existe segunda copia
da aritmetica para divergir depois. E e por isso que a armadilha do VERDE VAZIO
pode ser afirmada: `bancos(raiz)` devolve quais arquivos foram lidos, e portao
que conta zero banco acha zero defeito.

O QUE ELA CONTA, cada numero com o nome do campo que o sustenta
---------------------------------------------------------------
  * total de registros nos bancos de produto;
  * sem `afiliado.url_busca` — o PISO da escada de compra (secao 25.2 do
    ARQUIPELAGO.md), o degrau que nunca depende de ninguem;
  * sem `afiliado.url_produto` — a ficha, o degrau que paga comissao e o unico
    que o teste de vida da 25.4 consegue testar;
  * com `afiliado.url` e sem `url_produto` — a divida da 25.4-b;
  * com `afiliado.intestavel: true`;
  * a distribuicao por `afiliado.degrau`.

ELA NAO ABRE REDE E NAO TESTA LINK. Teste de vida e outro portao (25.4), e
misturar as duas coisas faria esta contagem depender do egresso.

E ELA NAO REESCREVE A REGRA DE NINGUEM. Quem reprova registro publicavel sem
piso, um por um, e a regra V26 do `validar-produtos.py`; esta regua CONTA e nao
julga registro. Duas reguas afirmando a mesma regra e como se perde a conta de
qual manda — a cicatriz de 16/10/2026 desta pasta.
"""
import glob
import io
import json
import os
import re

MARCA = re.compile(r"^```json\s*$")


def bancos(raiz):
    """Os arquivos de banco de produto desta raiz, em ordem estavel.

    Devolve a lista, e nao so os registros, porque o portao afirma QUANTOS
    bancos foram lidos: "0 sem piso" sobre zero banco lido e verde vazio, e
    verde vazio e a unica forma de este portao mentir sem ninguem editar nada.
    """
    return sorted(glob.glob(os.path.join(raiz, "dados", "produtos-*.json")))


def registros(raiz):
    """(arquivo, registro) de todo registro dos bancos de produto da raiz."""
    for caminho in bancos(raiz):
        with io.open(caminho, encoding="utf-8") as fh:
            dados = json.load(fh)
        for item in dados.get("produtos", []):
            yield os.path.basename(caminho), item


def identidade(banco, item):
    """`filtro/eheim-classic-250-2213` — o banco sem o enfeite, mais o id."""
    curto = banco.replace("produtos-", "").replace(".json", "")
    return "%s/%s" % (curto, item.get("id"))


def estado(item):
    """O estado de um registro no cano, em uma frase comparavel.

    E uma FRASE e nao um numero de proposito: ela e a unidade da declaracao, e
    o portao compara item por item. Declaracao por total diz "42" e fica verde
    quando os 42 viram 42 OUTROS — a licao que a serie da deriva aprendeu em
    16/10/2026, um andar abaixo.
    """
    af = item.get("afiliado") or {}
    degrau = af.get("degrau")
    return "piso:%d ficha:%d anuncio:%d degrau:%s intestavel:%d" % (
        1 if af.get("url_busca") else 0,
        1 if af.get("url_produto") else 0,
        1 if af.get("url") else 0,
        "-" if degrau is None else degrau,
        1 if af.get("intestavel") else 0,
    )


def contar(raiz):
    """A contagem inteira do cano, derivada de `estado()` e de mais nada."""
    itens = {}
    por_banco = {}
    for banco, item in registros(raiz):
        ident = identidade(banco, item)
        itens[ident] = estado(item)
        linha = por_banco.setdefault(banco, {"n": 0, "sem_busca": 0, "sem_produto": 0})
        linha["n"] += 1
        af = item.get("afiliado") or {}
        if not af.get("url_busca"):
            linha["sem_busca"] += 1
        if not af.get("url_produto"):
            linha["sem_produto"] += 1

    return {
        "bancos": [os.path.basename(c) for c in bancos(raiz)],
        "itens": itens,
        "por_banco": por_banco,
        "totais": totais(itens),
        "degraus": degraus(itens),
        "sem_busca": sorted(i for i, e in itens.items() if campo(e, "piso") == "0"),
        "sem_produto": sorted(i for i, e in itens.items() if campo(e, "ficha") == "0"),
        "url_sem_produto": sorted(i for i, e in itens.items()
                                  if campo(e, "anuncio") == "1" and campo(e, "ficha") == "0"),
        "intestaveis": sorted(i for i, e in itens.items() if campo(e, "intestavel") == "1"),
    }


def campo(frase, nome):
    """Le um campo da frase de estado. Devolve string, sempre."""
    for parte in frase.split():
        chave, _, valor = parte.partition(":")
        if chave == nome:
            return valor
    return ""


def totais(itens):
    """Os totais SAEM das frases de estado, nunca de uma segunda contagem."""
    return {
        "registros": len(itens),
        "sem_url_busca": sum(1 for e in itens.values() if campo(e, "piso") == "0"),
        "sem_url_produto": sum(1 for e in itens.values() if campo(e, "ficha") == "0"),
        "url_sem_url_produto": sum(1 for e in itens.values()
                                   if campo(e, "anuncio") == "1" and campo(e, "ficha") == "0"),
        "intestaveis": sum(1 for e in itens.values() if campo(e, "intestavel") == "1"),
    }


def degraus(itens):
    """{degrau (str): quantos}. O nulo viaja como '-', para o JSON ter chave."""
    conta = {}
    for frase in itens.values():
        d = campo(frase, "degrau")
        conta[d] = conta.get(d, 0) + 1
    return conta


def ler(caminho):
    with io.open(caminho, encoding="utf-8") as fh:
        return fh.read()


def declaracao(caminho):
    """Le a declaracao mais NOVA da serie: o 1o bloco ```json do arquivo.

    A serie cresce por cima (secao nova no topo), como o `dados/posicoes.md` e
    o `dados/deriva-do-catalogo.md` desta ilha. Arquivo ausente devolve None,
    que o portao trata como "cano nao declarado" — e nunca como zero.
    """
    if not os.path.exists(caminho):
        return None
    dentro, buf = False, []
    for linha in ler(caminho).split("\n"):
        if not dentro and MARCA.match(linha):
            dentro = True
            continue
        if dentro:
            if linha.strip() == "```":
                break
            buf.append(linha)
    if not buf:
        return None
    return json.loads("\n".join(buf))


def comparar_com_declaracao(itens, declarado):
    """O que a medicao tem e a declaracao nao, e o contrario. Item por item.

    Tres listas, porque as tres falhas sao diferentes e o conserto de cada uma
    e outro: registro NOVO no banco, registro que SAIU, e registro que mudou de
    degrau no cano sem ninguem declarar.
    """
    if declarado is None:
        return (["a serie nao tem declaracao nenhuma"], [], [])
    esperado = declarado.get("itens", {})
    novos = sorted(set(itens) - set(esperado))
    sumidos = sorted(set(esperado) - set(itens))
    mudados = sorted(
        "%s: medido '%s' contra declarado '%s'" % (i, itens[i], esperado[i])
        for i in (set(itens) & set(esperado)) if itens[i] != esperado[i]
    )
    return (novos, sumidos, mudados)

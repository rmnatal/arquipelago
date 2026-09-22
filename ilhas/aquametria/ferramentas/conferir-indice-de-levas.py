#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — este confere o REPOSITORIO, nao o site.

TODA PAGINA DO EIXO /peixes/ ESTA NO INDICE DE LEVAS DO dados/indexacao.md?

    python3 ferramentas/conferir-indice-de-levas.py

POR QUE ELE EXISTE, e a data e 22/09/2026
------------------------------------------
A secao 14.9 manda cada pagina nascer com duas promessas escritas — a consulta
que ela mira e por que ela consegue chegar as dez primeiras — e as duas moram no
registro do snippet que serve a pagina. A tabela "Levas publicadas" do
`dados/indexacao.md` e o INDICE delas, e existe para a leitura semanal da
Sentinela nao precisar abrir codigo.

Indice escrito a mao envelhece calado. Em 22/09/2026 a leva 7 achou essa tabela
com QUATRO linhas para SEIS levas: as levas 5 e 6 sairam em 14/09 e ninguem
escreveu a linha delas, entao por oito dias a leitura semanal leu um eixo de 20
URLs como se fosse de 12. No MESMO dia, a mesma doenca foi achada no portao da
voz, que media 36 das 40 paginas do site — e la ela ja virou portao.

Este arquivo e a outra metade: ele pergunta ao snippet quais paginas o eixo
publica e exige que cada uma apareca no indice, pelo ENDERECO (`/peixes/<slug>/`)
ou pela CONSULTA-ALVO exata que o proprio registro declara. Nao julga o texto da
linha, nao reclassifica SERP e nao escreve nada: so recusa o silencio.

E ele NAO le o banco de especies: le o registro do snippet, que e quem publica.
Se lesse o banco, as duas metades errariam juntas — a cicatriz do
`teste-peixes.py`, que so parou de digitar a contagem de categorias quando
passou a LER o `ARVORE.md` em vez de repetir o numero.
"""
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDICE = os.path.join(RAIZ, "dados", "indexacao.md")
TITULO_SECAO = "## Levas publicadas"

falhas = []


def ok(nome, cond, extra=""):
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def registro_do_eixo():
    """Pergunta ao snippet, por PHP, quais paginas ele registra."""
    saida = subprocess.run(
        ["php", os.path.join("ferramentas", "listar-paginas-do-eixo.php"), "."],
        cwd=RAIZ, capture_output=True, text=True)
    if saida.returncode != 0:
        print("  FALHA listar-paginas-do-eixo.php nao rodou: %s" % saida.stderr.strip()[:200])
        sys.exit(1)
    return json.loads(saida.stdout)


def consultas_do_eixo():
    """A consulta-alvo declarada por pagina. Sai do MESMO registro, por PHP."""
    php = (
        '$GLOBALS["__raiz_ilha"]="."; $GLOBALS["__slug_pagina"]="peixes"; $GLOBALS["__paginas"]=array();'
        'require "ferramentas/render-para-teste.php"; aquametria_teste_carregar(".");'
        '$s=array(); foreach (aquametria_peixes_registro() as $slug=>$def)'
        ' { $s[$slug] = isset($def["consulta"]) ? $def["consulta"] : ""; }'
        'echo json_encode($s, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);'
    )
    saida = subprocess.run(["php", "-r", php], cwd=RAIZ, capture_output=True, text=True)
    if saida.returncode != 0 or not saida.stdout.strip():
        print("  FALHA nao consegui ler as consultas-alvo do registro do eixo")
        sys.exit(1)
    return json.loads(saida.stdout)


def secao_do_indice(texto):
    """So o trecho da tabela de levas: o resto do arquivo e a serie semanal."""
    i = texto.find(TITULO_SECAO)
    if i < 0:
        return ""
    j = texto.find("\n## ", i + len(TITULO_SECAO))
    return texto[i:j if j > 0 else len(texto)]


def main():
    print("INDICE DE LEVAS — toda pagina do eixo aparece em dados/indexacao.md?")
    texto = open(INDICE, encoding="utf-8").read()
    secao = secao_do_indice(texto)
    ok("a seção 'Levas publicadas' existe no dados/indexacao.md", bool(secao))
    if not secao:
        print("\n1 FALHA(S)")
        return 1

    # A TABELA E UMA SO. Linha de tabela separada do cabecalho por linha em
    # branco vira, em Markdown, outra tabela — e sem cabecalho ela sai da tela
    # como texto solto. Foi o estado em que esta tabela ficou de 14 a 22/09/2026.
    linhas = [l.rstrip() for l in secao.split("\n")]
    blocos, atual = [], []
    for l in linhas:
        if l.startswith("|"):
            atual.append(l)
        elif atual:
            blocos.append(atual)
            atual = []
    if atual:
        blocos.append(atual)
    ok("as linhas de tabela formam UM bloco só, com cabeçalho",
       len(blocos) == 1, "achei %d blocos de tabela" % len(blocos))
    corpo = [l for bloco in blocos for l in bloco]
    separadores = [l for l in corpo if re.match(r"^\|[\s:|-]+\|$", l)]
    ok("a tabela tem exatamente uma linha de separação de cabeçalho",
       len(separadores) == 1, "achei %d" % len(separadores))
    linhas_de_leva = [l for l in corpo if l.startswith("|") and l not in separadores][1:]
    ok("a tabela tem linha de leva", len(linhas_de_leva) > 0, "%d linha(s)" % len(linhas_de_leva))

    registro = registro_do_eixo()
    consultas = consultas_do_eixo()
    alvo = {slug: d for slug, d in registro.items() if d["nivel"] >= 2}
    ok("o eixo declarou páginas de nível 2 ou 3", len(alvo) > 0, "%d página(s)" % len(alvo))

    faltando = []
    for slug in alvo:
        endereco = "/peixes/%s/" % slug
        consulta = (consultas.get(slug) or "").strip()
        if endereco not in secao and (not consulta or consulta not in secao):
            faltando.append(slug)
    ok("toda página do eixo aparece no índice, pelo endereço ou pela consulta-alvo",
       not faltando, ", ".join(faltando))

    # Cada categoria (nivel 2) e uma leva, e a leva se anuncia pelo ENDERECO da
    # mae: e por ele que a leitura semanal acha a linha dela.
    sem_endereco = [slug for slug, d in alvo.items()
                    if d["nivel"] == 2 and ("/peixes/%s/" % slug) not in secao]
    ok("toda categoria do eixo aparece no índice pelo endereço da mãe",
       not sem_endereco, ", ".join(sem_endereco))

    print("\n%s" % ("TUDO OK" if not falhas else "%d FALHA(S)" % len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conta o CANO DE LINKS desta ilha lendo os dados/produtos-*.json commitados.

    python3 ferramentas/contar-cano-de-links.py            # grava dados/cano-de-links-<hoje>.md
    python3 ferramentas/contar-cano-de-links.py --conferir  # so imprime, nao grava

NASCE DO ITEM 3 DO DESPACHO DA SENTINELA DE 07/10/2026, e o item nasceu de um
defeito de CONTAGEM, nao de cano: aquela leitura escreveu, com a data a vista,
que a contagem NAO foi feita e que nao seria estimada — "o ultimo numero medido e
do Pente Fino de 05/10/2026" e "a ronda de 02/10 mediu 12 de 78". Dois numeros de
dois e cinco dias antes, repetidos em relatorio novo, viram numero de hoje sem
que ninguem minta: basta parar de escrever a data do lado. O criterio de pronto
que o despacho declarou e justamente um ARQUIVO DATADO.

POR QUE UM SCRIPT, E NAO UMA CONTAGEM A MAO NO RELATORIO. Contagem a mao nao se
repete: a proxima execucao conta de novo, de outro jeito, e a serie nao existe.
Com o script, "quantos itens sem url_produto" passa a ser um comando, e a
diferenca entre duas datas passa a ser legivel.

O QUE ELE CONTA, e cada numero com o nome do campo que o sustenta:
  * total de registros nos quatro bancos de produto — e o que esta ilha chama de
    PUBLICAVEL: todo registro do banco e sugerivel por alguma calculadora, e o
    que decide se ele SAI na tela e a regua de cada uma, nao este arquivo;
  * sem `afiliado.url_busca` — o PISO da escada de compra (secao 25.2 do
    ARQUIPELAGO.md), o degrau que nunca depende de ninguem;
  * sem `afiliado.url_produto` — a FICHA, o degrau que paga comissao;
  * a distribuicao por `afiliado.degrau`;
  * e duas colunas que o Pente Fino de 05/10 mediu e que o despacho nao pediu,
    porque elas sao o que explica as outras: quantos tem `url` (link de anuncio)
    sem `url_produto`, e quantos declaram `intestavel`.

ELE NAO ABRE REDE E NAO TESTA LINK. Teste de vida e outro portao (secao 25.4), e
misturar as duas coisas faria esta contagem depender do egresso.
"""
from __future__ import print_function

import collections
import datetime
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def registros():
    """(arquivo, item) de todo registro dos bancos de produto."""
    for caminho in sorted(glob.glob(os.path.join(RAIZ, 'dados', 'produtos-*.json'))):
        with io.open(caminho, encoding='utf-8') as fh:
            dados = json.load(fh)
        for item in dados.get('produtos', []):
            yield os.path.basename(caminho), item


def contar():
    por_banco = collections.OrderedDict()
    degraus = collections.Counter()
    total = 0
    sem_busca = []
    sem_produto = []
    url_sem_produto = []
    intestaveis = []

    for banco, item in registros():
        total += 1
        linha = por_banco.setdefault(banco, {'n': 0, 'sem_busca': 0, 'sem_produto': 0})
        linha['n'] += 1
        af = item.get('afiliado') or {}
        ident = '%s/%s' % (banco.replace('produtos-', '').replace('.json', ''), item.get('id'))
        if not af.get('url_busca'):
            sem_busca.append(ident)
            linha['sem_busca'] += 1
        if not af.get('url_produto'):
            sem_produto.append(ident)
            linha['sem_produto'] += 1
        if af.get('url') and not af.get('url_produto'):
            url_sem_produto.append(ident)
        if af.get('intestavel'):
            intestaveis.append(ident)
        degraus[af.get('degrau')] += 1

    return {
        'total': total,
        'por_banco': por_banco,
        'degraus': degraus,
        'sem_busca': sem_busca,
        'sem_produto': sem_produto,
        'url_sem_produto': url_sem_produto,
        'intestaveis': intestaveis,
    }


def relatorio(c, hoje):
    l = []
    l.append('# Cano de links — contagem de %s' % hoje)
    l.append('')
    l.append('Contado por `ferramentas/contar-cano-de-links.py` sobre os quatro '
             '`dados/produtos-*.json` deste repositório. **Nenhuma rede foi aberta e '
             'nenhum link foi testado** — teste de vida é outro portão (seção 25.4 do '
             '`ARQUIPELAGO.md`). Fecha o item 3 do despacho da Sentinela de 07/10/2026, '
             'que pedia um arquivo datado com quatro números contados em vez dos números '
             'de 02 e 05/10 repetidos.')
    l.append('')
    l.append('## Os quatro números que o despacho pediu')
    l.append('')
    l.append('| o que | quantos |')
    l.append('|---|---|')
    l.append('| registros nos quatro bancos de produto (o que esta ilha chama de publicável) | **%d** |' % c['total'])
    l.append('| sem `afiliado.url_busca` — o piso da 25.2, que nunca depende de ninguém | **%d** |'
             % len(c['sem_busca']))
    l.append('| sem `afiliado.url_produto` — a ficha, o degrau que paga comissão | **%d** |'
             % len(c['sem_produto']))
    l.append('')
    l.append('**Distribuição por `afiliado.degrau`:**')
    l.append('')
    l.append('| degrau | quantos |')
    l.append('|---|---|')
    for degrau in sorted(c['degraus'], key=lambda d: (d is None, d)):
        nome = 'ausente (campo `degrau` nulo)' if degrau is None else str(degrau)
        l.append('| %s | %d |' % (nome, c['degraus'][degrau]))
    l.append('')
    l.append('## As duas colunas que o despacho não pediu, e que explicam as de cima')
    l.append('')
    l.append('| o que | quantos |')
    l.append('|---|---|')
    l.append('| com `afiliado.url` (link de anúncio) e **sem** `url_produto` | **%d** |'
             % len(c['url_sem_produto']))
    l.append('| com `afiliado.intestavel: true` | **%d** |' % len(c['intestaveis']))
    l.append('')
    l.append('## Por banco')
    l.append('')
    l.append('| banco | registros | sem `url_busca` | sem `url_produto` |')
    l.append('|---|---|---|---|')
    for banco, linha in c['por_banco'].items():
        l.append('| `%s` | %d | %d | %d |' % (banco, linha['n'], linha['sem_busca'], linha['sem_produto']))
    l.append('')
    if c['sem_busca']:
        l.append('**Os sem `url_busca`, um por um:** %s' % ', '.join('`%s`' % i for i in c['sem_busca']))
        l.append('')
    if c['sem_produto']:
        l.append('**Os sem `url_produto`, um por um:** %s' % ', '.join('`%s`' % i for i in c['sem_produto']))
        l.append('')
    return '\n'.join(l) + '\n'


def main():
    hoje = datetime.date.today().isoformat()
    c = contar()
    texto = relatorio(c, hoje)
    print(texto)
    if '--conferir' in sys.argv:
        return 0
    alvo = os.path.join(RAIZ, 'dados', 'cano-de-links-%s.md' % hoje)
    with io.open(alvo, 'w', encoding='utf-8') as fh:
        fh.write(texto)
    print('gravado: %s' % alvo)
    return 0


if __name__ == '__main__':
    sys.exit(main())

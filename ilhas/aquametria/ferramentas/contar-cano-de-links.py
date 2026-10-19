#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve o RELATORIO DATADO do cano de links desta ilha.

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

ELE NAO CONTA NADA POR CONTA PROPRIA, E ISSO MUDOU EM 19/10/2026. A aritmetica
morava aqui dentro, e por isso nao podia ser rodada contra banco encenado nem
exercitada por portao nenhum — a `bancada.py` denunciava este arquivo desde
14/10/2026 ("SEM CONVENCAO, ninguem roda") e a ronda da Sentinela de 14/10
RECONTOU os quatro bancos a mao para conferir o que ele imprimiu. Agora a
contagem mora em `ferramentas/regua-cano-de-links.py`, que recebe a RAIZ: o
portao `conferir-cano-de-links.py` conta a ilha de verdade com ela, o
`teste-cano-de-links.py` conta bancos de mentira com a MESMA conta, e este
arquivo so imprime. Ele e producao, nao portao — quem afirma e o portao.

O QUE ELE IMPRIME e o que cada numero sustenta esta escrito na regua. Ele NAO
abre rede e NAO testa link: teste de vida e outro portao (secao 25.4).
"""
from __future__ import print_function

import datetime
import importlib.util
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def carregar_regua():
    caminho = os.path.join(RAIZ, 'ferramentas', 'regua-cano-de-links.py')
    spec = importlib.util.spec_from_file_location('regua_cano_de_links', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()


def relatorio(c, hoje):
    t = c['totais']
    l = []
    l.append('# Cano de links — contagem de %s' % hoje)
    l.append('')
    l.append('Contado por `ferramentas/contar-cano-de-links.py` sobre os '
             '`dados/produtos-*.json` deste repositório, com a régua compartilhada '
             '`ferramentas/regua-cano-de-links.py` — a mesma que o portão '
             '`ferramentas/conferir-cano-de-links.py` usa, para o relatório e o portão '
             'não poderem divergir. **Nenhuma rede foi aberta e nenhum link foi '
             'testado** — teste de vida é outro portão (seção 25.4 do `ARQUIPELAGO.md`). '
             'Fecha o item 3 do despacho da Sentinela de 07/10/2026, que pedia um '
             'arquivo datado com quatro números contados em vez dos números de 02 e '
             '05/10 repetidos.')
    l.append('')
    l.append('O estado de hoje, item por item, está declarado em `dados/cano-de-links.md`, '
             'que é a série que o portão confere.')
    l.append('')
    l.append('## Os quatro números que o despacho pediu')
    l.append('')
    l.append('| o que | quantos |')
    l.append('|---|---|')
    l.append('| registros nos bancos de produto (o que esta ilha chama de publicável) | **%d** |'
             % t['registros'])
    l.append('| sem `afiliado.url_busca` — o piso da 25.2, que nunca depende de ninguém | **%d** |'
             % t['sem_url_busca'])
    l.append('| sem `afiliado.url_produto` — a ficha, o degrau que paga comissão | **%d** |'
             % t['sem_url_produto'])
    l.append('')
    l.append('**Distribuição por `afiliado.degrau`:**')
    l.append('')
    l.append('| degrau | quantos |')
    l.append('|---|---|')
    for degrau in sorted(c['degraus'], key=lambda d: (d == '-', d)):
        nome = 'ausente (campo `degrau` nulo)' if degrau == '-' else degrau
        l.append('| %s | %d |' % (nome, c['degraus'][degrau]))
    l.append('')
    l.append('## As duas colunas que o despacho não pediu, e que explicam as de cima')
    l.append('')
    l.append('| o que | quantos |')
    l.append('|---|---|')
    l.append('| com `afiliado.url` (link de anúncio) e **sem** `url_produto` | **%d** |'
             % t['url_sem_url_produto'])
    l.append('| com `afiliado.intestavel: true` | **%d** |' % t['intestaveis'])
    l.append('')
    l.append('## Por banco')
    l.append('')
    l.append('| banco | registros | sem `url_busca` | sem `url_produto` |')
    l.append('|---|---|---|---|')
    for banco, linha in sorted(c['por_banco'].items()):
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
    c = regua.contar(RAIZ)
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

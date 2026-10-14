#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao SEM REDE das duas funcoes que o item 2 do despacho de 07/10/2026 criou
em ferramentas/search-console.py: `totais()` e `por_pagina()`.

    python3 ferramentas/teste-search-console.py

POR QUE ELE EXISTE, e por que ele mede SO as funcoes puras. O defeito que o item
2 nomeia nao estava na chamada da API: estava na CONTA que o script fazia depois
dela. O script somava as linhas da dimensao `query` e chamava aquilo de
impressoes da ilha; o Google anonimiza a consulta de quase toda impressao de
cauda longa, e na aquametria, na janela de 07/10/2026, 370 das 371 impressoes
sairam anonimizadas. Resultado emitido: "1 impressao, 0 clique" para uma
propriedade que a Search Console mostrava com 371 e 3.

Uma conta errada nao precisa de rede para ser medida, e NAO HAVIA CREDENCIAL
NESTE AMBIENTE quando este portao foi escrito (GOOGLE_SA_B64, GOOGLE_SA_JSON e
GOOGLE_SA_FILE ausentes, conferidos em 14/10/2026). Entao o que este arquivo
mede e a conta, com a resposta da API ENCENADA a partir dos numeros que a
leitura de 07/10 registrou. O que ele NAO mede, e esta escrito para ninguem ler
verde aqui como entrega: que a chamada nova devolve o que se espera dela. Isso
so a passada com credencial diz, e e o que falta do item 2.

O CASO 1 E O MUNDO MEDIDO EM 07/10/2026, em pessoa: 371 impressoes e 3 cliques
na propriedade, contra 1 e 0 na soma da dimensao `query`.
"""
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# O modulo tem hifen no nome e importa google-auth no topo, com um bootstrap de
# venv no except. Carregar por spec e ler o fonte sem executar o topo seria
# complicado; mais simples e honesto: injetamos um stub dos dois nomes que o
# topo importa, para a importacao nao sair comprando dependencia nenhuma.
for nome, atributos in (
    ('google', ()),
    ('google.oauth2', ('service_account',)),
    ('google.auth', ()),
    ('google.auth.transport', ()),
    ('google.auth.transport.requests', ('AuthorizedSession',)),
):
    if nome in sys.modules:
        continue
    modulo = type(sys)(nome)
    for atributo in atributos:
        setattr(modulo, atributo, object())
    sys.modules[nome] = modulo
sys.modules['google.oauth2'].service_account = object()
sys.modules['google.auth.transport.requests'].AuthorizedSession = object()

spec = importlib.util.spec_from_file_location(
    'search_console', os.path.join(RAIZ, 'ferramentas', 'search-console.py'))
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)

contadas = [0]
falhas = []


def ok(nome, cond, extra=''):
    contadas[0] += 1
    print('  %s %s%s' % ('ok   ' if cond else 'FALHA', nome, (' — ' + extra) if extra else ''))
    if not cond:
        falhas.append(nome)


# ---------------------------------------------------------------- totais()
print('totais() — a consulta SEM dimensao')

# CASO 1: o mundo medido em 07/10/2026 na aquametria.
resposta = {'rows': [{'clicks': 3, 'impressions': 371, 'ctr': 0.0080862, 'position': 6.7}]}
t = sc.totais(resposta)
ok('caso 1: 371 impressoes, e nao as 1 que a dimensao query somava',
   t['impressoes'] == 371, str(t['impressoes']))
ok('caso 1: 3 cliques', t['cliques'] == 3, str(t['cliques']))
ok('caso 1: posicao media 6,7', abs(t['posicao'] - 6.7) < 0.001, str(t['posicao']))
ok('caso 1: declara que foi medido', t['medido'] is True)

# CASO 2: a API nao devolve linha. "Nao medido" NAO e "zero" — e a distincao que
# a leitura de 07/10 cobrou com estas palavras sobre o clique de afiliado:
# "nao e zero: e nao medido".
t = sc.totais({'rows': []})
ok('caso 2: resposta vazia devolve medido=False', t['medido'] is False)
ok('caso 2: resposta vazia devolve zeros, e nao None',
   (t['impressoes'], t['cliques']) == (0, 0), repr((t['impressoes'], t['cliques'])))
ok('caso 3: resposta ausente nao estoura', sc.totais(None)['medido'] is False)

# CASO 4: a API omite o ctr. O quociente manda, e nao um campo faltando.
t = sc.totais({'rows': [{'clicks': 1, 'impressions': 4, 'position': 8.1}]})
ok('caso 4: ctr recalculado quando a API nao o manda', abs(t['ctr'] - 0.25) < 1e-9, str(t['ctr']))
t = sc.totais({'rows': [{'clicks': 0, 'impressions': 0, 'position': 0}]})
ok('caso 5: zero impressao nao divide por zero', t['ctr'] == 0.0)

# -------------------------------------------------------------- por_pagina()
print('\npor_pagina() — a dimensao `page`, que o Google NAO anonimiza')

resposta = {'rows': [
    {'keys': ['https://aquametria.com.br/calculadora-de-litragem/'],
     'clicks': 0, 'impressions': 27, 'position': 9.1},
    {'keys': ['https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/'],
     'clicks': 1, 'impressions': 125, 'position': 8.1},
    {'keys': ['https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-bandeira/'],
     'clicks': 1, 'impressions': 23, 'position': 5.3},
]}
linhas = sc.por_pagina(resposta, 'aquametria.com.br')
ok('tres paginas entram', len(linhas) == 3, str(len(linhas)))
ok('a ordem e por impressao decrescente — a de 125 vem primeiro',
   linhas[0]['pagina'] == '/peixes/bettas/quantos-litros-para-betta/', linhas[0]['pagina'])
ok('o dominio sai do caminho', all(not x['pagina'].startswith('http') for x in linhas),
   linhas[1]['pagina'])
ok('a banda da pagina do betta e 4-10 (posicao 8,1)', linhas[0]['banda'] == '4-10', linhas[0]['banda'])
ok('a banda da acara-bandeira e 4-10 (posicao 5,3)',
   [x for x in linhas if x['posicao'] == 5.3][0]['banda'] == '4-10')
ok('pagina sem impressao sai com banda "sem impressão"',
   sc.por_pagina({'rows': [{'keys': ['https://x/y/'], 'clicks': 0, 'impressions': 0,
                            'position': 0}]}, 'x')[0]['banda'] == 'sem impressão')
ok('resposta vazia devolve lista vazia, e nao estoura', sc.por_pagina({'rows': []}, 'x') == [])
ok('resposta ausente devolve lista vazia', sc.por_pagina(None, 'x') == [])
ok('linha sem `keys` e descartada em vez de estourar',
   sc.por_pagina({'rows': [{'clicks': 0, 'impressions': 1, 'position': 2}]}, 'x') == [])

# A AFIRMACAO QUE AMARRA AS DUAS: a soma da dimensao `page` tem de poder bater com
# o total da propriedade, que e justamente o que a soma da dimensao `query` nao
# conseguia fazer.
soma_paginas = sum(x['impressoes'] for x in linhas)
ok('a soma da dimensao `page` deste caso da 175 — comparavel ao total, ao contrario da soma de `query`',
   soma_paginas == 175, str(soma_paginas))

print('\n' + '=' * 70)
print('%d afirmacoes, %d falha(s).' % (contadas[0], len(falhas)))
for f in falhas:
    print('  FALHA  ' + f)
sys.exit(1 if falhas else 0)

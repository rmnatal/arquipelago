#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA DA TRAVA DO BATISMO — 29/09/2026.

    python3 ferramentas/teste-batismo.py

Mede `ferramentas/batismo-do-fabricante.py` contra os registros REAIS deste
banco e contra as bordas que o banco de hoje nao exercita. Quem a ataca e
`ferramentas/mutacoes-batismo.py`.

**As afirmacoes sobre o defeito rodam sobre uma COPIA do registro**, nunca sobre
o banco em disco: bancada que escreve no banco para se provar e bancada que
estraga o que mede.
"""

import copy
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_s = importlib.util.spec_from_file_location(
    'batismo', os.path.join(RAIZ, 'ferramentas', 'batismo-do-fabricante.py'))
bat = importlib.util.module_from_spec(_s)
_s.loader.exec_module(bat)

ESQUEMA = json.load(open(os.path.join(RAIZ, 'dados', 'esquema-banco.json'), encoding='utf-8'))

falhas = []
contadas = [0]


def ok(condicao, titulo, visto=''):
    contadas[0] += 1
    if condicao:
        print('  ok   %-72s %s' % (titulo, visto))
    else:
        print('  FALHA %-71s %s' % (titulo, visto))
        falhas.append(titulo)


def banco():
    fora = {}
    dados = os.path.join(RAIZ, 'dados')
    for nome in sorted(os.listdir(dados)):
        if nome.startswith('materiais-') and nome.endswith('.json'):
            for m in json.load(open(os.path.join(dados, nome), encoding='utf-8'))['materiais']:
                fora[m['id']] = m
    return fora


REG = banco()


def reg(ident):
    return copy.deepcopy(REG[ident])


print('A TRAVA DO BATISMO, contra os registros reais deste banco:')

em_escopo, aprovados, fora_de_escopo = [], [], []
for ident, m in sorted(REG.items()):
    certo, laudo = bat.conferir(m, ESQUEMA)
    if laudo['em_escopo']:
        em_escopo.append(ident)
        if certo:
            aprovados.append(ident)
    else:
        fora_de_escopo.append(ident)
        ok(bool(laudo.get('motivo')),
           'fora de escopo com motivo escrito, nunca aprovado em silencio: %s' % ident,
           laudo.get('motivo', '')[:44])

ok(len(em_escopo) == 7, 'sete registros citam PDF de fabricante e entram em escopo',
   '%d em escopo' % len(em_escopo))
ok(len(aprovados) == len(em_escopo),
   'o banco de hoje passa inteiro na trava', '%d de %d' % (len(aprovados), len(em_escopo)))
ok(len(fora_de_escopo) == len(REG) - 7, 'os outros ficam fora com motivo, nao aprovados',
   '%d fora' % len(fora_de_escopo))

print('\nO DEFEITO QUE A TRAVA NASCEU PARA PEGAR, refeito sobre uma copia:')

m = reg('quartzolit-borracha-liquida-elastica')
ok(bat.conferir(m, ESQUEMA)[0], 'o registro corrigido passa', m['nome_comercial'])

m['nome_comercial'] = 'impermeabilizante borracha liquida elastica quartzolit'
certo, laudo = bat.conferir(m, ESQUEMA)
ok(not certo, 'o nome antigo REPROVA', laudo['motivo'][:44])
ok(laudo['ausentes'] == ['impermeabilizante'],
   'e a trava nomeia a palavra, nao reprova em bloco', str(laudo['ausentes']))

# O CORACAO DA TRAVA: `impermeabilizante` ESTA na URL da pagina de produto (no
# caminho: /impermeabilizantes-quartzolit/...). Quem comparasse contra a URL
# inteira aprovaria o defeito. A trava compara contra o NOME DO ARQUIVO da
# fonte que BATIZA, e prateleira nao batiza.
url_pagina = REG['quartzolit-borracha-liquida-elastica']['fontes'][
    'pagina-produto-borracha-liquida-elastica']['url']
ok('impermeabilizante' in url_pagina.lower(),
   'a palavra reprovada ESTA na URL da pagina de produto (a prateleira)', 'sim')
ok(not certo,
   'e mesmo assim reprova: o que batiza e o arquivo do boletim, nao o caminho', 'reprovado')

print('\nO SERVIDOR DO FABRICANTE MUTILA O NOME DO ARQUIVO, e a trava sabe disso:')

m = reg('quartzolit-rejunte-epoxi')
certo, laudo = bat.conferir(m, ESQUEMA)
ok(certo, 'letra acentuada APAGADA pelo servidor: `Epoxi` vale `Epxi`', laudo['arquivo'])
ok('epxi' in laudo['arquivo'].lower(), 'e o arquivo e mesmo o mutilado', laudo['arquivo'])

m = reg('quartzolit-rejunte-porcelanatos-e-ceramicas')
certo, laudo = bat.conferir(m, ESQUEMA)
ok(certo, 'palavras COLADAS no nome do arquivo continuam legiveis', laudo['arquivo'])
ok('quartzolit' not in laudo['arquivo'].lower(),
   'e a marca nao esta nesse arquivo — por isso ela nao e cobrada', laudo['arquivo'])

m = reg('quartzolit-rejunte-ceramicas')
ok(bat.conferir(m, ESQUEMA)[0], 'so o acento de diferenca passa (Ceramicas)',
   m['nome_comercial'])

m = reg('quartzolit-verniz-protetor-para-pisos')
certo, laudo = bat.conferir(m, ESQUEMA)
ok(certo, 'palavra vazia no meio do batismo nao e cobrada (`para`)', m['nome_comercial'])

print('\nAS BORDAS QUE O BANCO DE HOJE NAO EXERCITA, fabricadas:')

m = reg('quartzolit-rejunte-epoxi')
m['nome_comercial'] = 'Rejunte Epóxi Quartzolit Premium Ultra'
certo, laudo = bat.conferir(m, ESQUEMA)
ok(not certo, 'palavra inventada no fim do batismo reprova', str(laudo['ausentes']))
ok(laudo['ausentes'] == ['Premium', 'Ultra'], 'e as duas sao nomeadas', str(laudo['ausentes']))

m = reg('quartzolit-rejunte-epoxi')
m['marca'] = 'Epóxi'
m['nome_comercial'] = 'Epóxi Inexistente'
certo, laudo = bat.conferir(m, ESQUEMA)
ok(laudo['ausentes'] == ['Inexistente'],
   'a MARCA nao e cobrada nem quando e a palavra do produto', str(laudo['ausentes']))

# Duas fontes que batizam e discordam: vence o nivel MENOR, que e a regra que
# `escada_de_fontes` ja declarava para qualquer conflito.
m = reg('quartzolit-rejunte-epoxi')
fraca = dict(list(m['fontes'].values())[0])
fraca['url'] = 'https://www.quartzolit.weber/files/br/2024-01/BT_Argamassa_Outra_Coisa.pdf'
fraca['nivel'] = 4
m['fontes'] = {'a-fraca': fraca, 'a-forte': list(reg('quartzolit-rejunte-epoxi')['fontes'].values())[0]}
chave, fonte = bat.fonte_que_batiza(m, set(ESQUEMA['batismo_do_fabricante']['origens_que_batizam']))
ok(chave == 'a-forte' and fonte['nivel'] == 2,
   'entre duas que batizam, vence a de MENOR nivel', '%s (nivel %s)' % (chave, fonte['nivel']))

m2 = reg('quartzolit-rejunte-epoxi')
m2['fontes'] = {'a-fraca': fraca}
certo, laudo = bat.conferir(m2, ESQUEMA)
ok(not certo, 'e com so a fraca em cena o batismo deixa de ser legivel', str(laudo['ausentes']))

print('\nAS DUAS BORDAS QUE A BATERIA OBRIGOU A FABRICAR, e nenhuma existe no banco de hoje:')

# A BATERIA ACHOU AS DUAS (29/09/2026): `mutacoes-batismo.py` m09 e m10 passaram
# com a bancada verde, e mutacao que passa e trava que ninguem mede. As duas
# travas sao reais — elas so nao tinham, no banco de hoje, um registro que as
# exercitasse. Bancada que so mede o banco de hoje envelhece junto com ele.

# BORDA 1 — a palavra vazia. Cobrar `de` num batismo cujo arquivo nao o traz
# reprovaria um nome CERTO. No banco de hoje isso nunca aparece porque o
# casamento e por SUBSTRING e palavra de duas letras casa em quase tudo: o
# `para` de "Verniz Protetor para Pisos" esta escrito no proprio arquivo.
m = reg('quartzolit-rejunte-piscinas')
unica = dict(list(m['fontes'].values())[0])
unica['url'] = 'https://www.quartzolit.weber/files/br/2024-03/rejunte_piscinas_quartzolit.pdf'
unica['nivel'] = 2
m['fontes'] = {'bt-fabricado': unica}
m['nome_comercial'] = 'Rejunte de Piscinas Quartzolit'
certo, laudo = bat.conferir(m, ESQUEMA)
ok('de' not in bat.nome_do_arquivo(unica['url']).lower(),
   'BORDA: o arquivo do fabricante nao traz a palavra vazia `de`', unica['url'].split('/')[-1])
ok(certo, 'e por isso mesmo ela nao pode ser cobrada — o batismo passa',
   m['nome_comercial'])

# BORDA 2 — o separador. O fabricante parte no arquivo o que o batismo escreve
# junto (`AC2` virando `AC_2`). Comparar sem achatar os dois lados reprovaria
# este nome certo; no banco de hoje nenhum arquivo parte uma palavra do batismo.
m = reg('quartzolit-rejunte-piscinas')
unica = dict(list(m['fontes'].values())[0])
unica['url'] = 'https://www.quartzolit.weber/files/br/2024-03/BT_Rejunte_AC_2_Quartzolit.pdf'
unica['nivel'] = 2
m['fontes'] = {'bt-fabricado': unica}
m['nome_comercial'] = 'Rejunte AC2 Quartzolit'
certo, laudo = bat.conferir(m, ESQUEMA)
ok('ac2' not in bat.nome_do_arquivo(unica['url']).lower(),
   'BORDA: o arquivo parte `AC2` em `AC_2`', unica['url'].split('/')[-1])
ok(certo, 'e o separador nao conta de nenhum dos dois lados — o batismo passa',
   m['nome_comercial'])

print('\nA LISTA MORA NO ESQUEMA, E A TRAVA REPROVA QUANDO ELA SOME (26.2):')

for descricao, esquema_quebrado in (
        ('o esquema perde a chave inteira', {}),
        ('`origens_que_batizam` vira lista vazia',
         {'batismo_do_fabricante': {'origens_que_batizam': []}}),
        ('`origens_que_batizam` deixa de ser lista',
         {'batismo_do_fabricante': {'origens_que_batizam': 'documento-pdf-do-fabricante'}}),
        ('`batismo_do_fabricante` deixa de ser objeto',
         {'batismo_do_fabricante': True})):
    try:
        bat.conferir(reg('quartzolit-rejunte-epoxi'), esquema_quebrado)
        ok(False, descricao, 'aprovou em silencio')
    except bat.EsquemaSemBatismo as erro:
        ok(True, descricao, str(erro)[:44])

origens_hoje = ESQUEMA['batismo_do_fabricante']['origens_que_batizam']
ok(origens_hoje == ['documento-pdf-do-fabricante'],
   'e a lista de hoje e so o PDF do fabricante', str(origens_hoje))

print('\n%s: %d afirmacoes, %d falha(s).'
      % ('REPROVADO' if falhas else 'APROVADO', contadas[0], len(falhas)))
sys.exit(1 if falhas else 0)

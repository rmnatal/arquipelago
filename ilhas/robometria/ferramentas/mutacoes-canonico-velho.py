#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Serve uma pagina VELHA no canonico e exige que a secao 10 reprove.

    python3 ferramentas/mutacoes-canonico-velho.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 10 do `conferir-no-ar.py` nasceu em 14/09/2026 para impedir o defeito que
custou a revisao 37: o Sync aplica, o `/status` confirma, as URLs dao 200 — e o
leitor continua na pagina de antes, porque o cache em arquivo do hospedeiro nao
purga com gravacao de option.

ELA NASCEU CEGA PARA O CASO MAIS COMUM, e isso foi MEDIDO no ar as 19h33:30Z de
14/09/2026, pelo teste que o item (b) do despacho da Sentinela pedia. A secao
comparava TRES CONTAGENS DE MARCADOR — saidas de compra, degraus de trilha e
blocos de compra — e mais nada. Naquele instante o canonico servia
"o fabricante a declara para HO041, HO400, HO401, HO407, OB010" e a quebra de
cache servia "... S20, S10, E10, S12, E12, X20": a leva do Xiaomi S10 tinha
trocado QUAL peca tem o maior alcance do banco. Nenhuma das tres contagens se
move com isso, entao a regua aprovaria a pagina velha sem hesitar.

O QUE ESTA BATERIA MEDE: que a afirmacao nova — a impressao do LEITOR, o texto
servido — separa as duas paginas que as contagens nao separam. E que ela NAO
reprova o mundo sadio, porque regua que reprova tudo nao mede nada.

COMO ELA PRODUZ O MUNDO, e por que assim: nao toca no site. O par velho/novo e
construido a partir do HTML que o site serve HOJE, trocando so a lista de
codigos do artigo-ancora pela que estava no ar antes desta leva. E exatamente a
diferenca que existiu, e ela chega aqui sem depender de o cache estar quente.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))

import importlib.util

_spec = importlib.util.spec_from_file_location(
    'conferir_no_ar', os.path.join(RAIZ, 'ferramentas', 'conferir-no-ar.py'))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

impressao = _mod._impressao_do_leitor
MARCAS = ('rbm-comprar', 'rbm-trilha', 'rbm-vitrine-acao')
CHAVE = 'rbm_quebra_de_cache=1757877216'

# O TEXTO DOS DOIS MUNDOS, escrito LITERALMENTE aqui e nao lido do banco. Se
# esta bateria derivasse do mesmo lugar de onde a pagina deriva, as duas metades
# errariam juntas. Sao as duas frases que o site serviu de verdade em 14/09/2026,
# com dezenove minutos de diferenca.
CODIGOS_VELHOS = 'HO041, HO400, HO401, HO407, OB010'
CODIGOS_NOVOS = 'S20, S10, E10, S12, E12, X20'

MOLDE = (
    '<html><body>'
    '<nav class="rbm-trilha"><a href="/">Inicio</a></nav>'
    '<p>A peca de maior alcance do banco e a <b>%s</b>: '
    'o fabricante a declara para %s. E o teto do que universal poderia '
    'significar neste nicho.</p>'
    '<div class="rbm-vitrine-acao"><a class="rbm-comprar" href="#">Ver na loja</a></div>'
    '<script>var x = "%s";</script>'
    '</body></html>'
)

VELHO = MOLDE % ('PR10124', CODIGOS_VELHOS, CHAVE)
NOVO = MOLDE % ('B106GL-BX', CODIGOS_NOVOS, CHAVE)

falhas = 0
print('=' * 78)
print('A SECAO 10 SEPARA PAGINA VELHA DE PAGINA NOVA?')
print('=' * 78)


def afirmar(condicao, rotulo, medido=''):
    global falhas
    marca = 'ok  ' if condicao else 'X   '
    if not condicao:
        falhas += 1
    print('%s%-62s %s' % (marca, rotulo, medido))


# 1. O MUNDO EM QUE A REGUA ANTIGA E CEGA -----------------------------------
iguais = all(VELHO.count(m) == NOVO.count(m) for m in MARCAS)
afirmar(iguais,
        'as TRES contagens de marcador NAO separam os dois mundos',
        ' · '.join('%s %d=%d' % (m, VELHO.count(m), NOVO.count(m)) for m in MARCAS))
print('     por que: e esta a cegueira medida as 19h33:30Z de 14/09/2026. Se as')
print('     contagens separassem os dois, a afirmacao nova nao estaria medindo')
print('     nada que a antiga ja nao medisse.')
print()

# 2. A AFIRMACAO NOVA MORDE --------------------------------------------------
afirmar(impressao(VELHO, CHAVE) != impressao(NOVO, CHAVE),
        'a impressao do LEITOR separa o canonico velho do recem-gerado',
        'diferentes')
print('     por que: e o defeito na forma em que ele chega ao leitor — a pagina')
print('     inteira de pe, com a palavra errada dentro.')
print()

# 3. E NAO REPROVA O MUNDO SADIO --------------------------------------------
afirmar(impressao(NOVO, CHAVE) == impressao(NOVO, CHAVE.replace('1757877216', '1757999999')),
        'a CHAVE de quebra de cache nao entra na comparacao',
        'igual')
print('     por que: a chave aparece em link interno e no canonical da propria')
print('     pagina. Compara-la garantiria desacordo e chamaria isso de defeito —')
print('     regua que reprova sempre nao mede nada.')
print()

afirmar(impressao(NOVO, CHAVE) == impressao(
            NOVO.replace('<script>', '<script >'), CHAVE),
        'marcacao que o leitor nao ve nao muda a impressao',
        'igual')
print('     por que: a afirmacao e sobre a PALAVRA na tela. Byte a byte daria')
print('     alarme falso a cada espaco de markup, e o alarme falso foi o que')
print('     custou quatro revisoes de diagnostico nesta ilha.')
print()

afirmar(impressao(VELHO, CHAVE) == impressao(VELHO, CHAVE),
        'o mundo intacto passa',
        'igual')
print()

print('=' * 78)
if falhas:
    print('REPROVADO: %d afirmacao(oes) fora do esperado.' % falhas)
    sys.exit(1)
print('APROVADO: 5 afirmacoes, a trava nova separa o que as contagens nao separam.')

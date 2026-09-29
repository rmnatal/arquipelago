#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA DA REGRA DE CASAMENTO — `ferramentas/casar-anuncio.py`.

    python3 ferramentas/teste-casamento.py

Nao fala com a rede. Os titulos desta bancada sao TODOS REAIS: foram devolvidos
pela Open API da Shopee em **29/09/2026**, nas chamadas que abriram este bloco, e
estao copiados aqui byte a byte — com acento, com caixa errada, com espaco duplo
e com `\\n` no meio de um deles, que e como o vendedor escreveu. Titulo inventado
mede a regra contra a imaginacao de quem a escreveu; titulo medido mede a regra
contra a Shopee.

O banco tambem e o real: a bancada LE `dados/materiais-*.json`. Ela nunca cobra o
NUMERO de registros nem a contagem por degrau — esses mudam no proximo bloco — e
so cobra o comportamento da regra sobre os registros que existem.

A GRADE INCLUI A BORDA (regra 2 da secao 8 do contrato): alem dos titulos que
casam, entram os que NAO podem casar, um por trava, com o motivo esperado. Regua
que so mede o acerto aprova o desastre calada.
"""

import glob
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    'casar_anuncio', os.path.join(RAIZ, 'ferramentas', 'casar-anuncio.py'))
casar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(casar)

afirmacoes = 0
falhas = []


def af(condicao, texto):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(texto)


REGISTROS = []
for caminho in sorted(glob.glob(os.path.join(RAIZ, 'dados', 'materiais-*.json'))):
    for item in json.load(open(caminho, encoding='utf-8'))['materiais']:
        REGISTROS.append(item)


def irmaos_de(reg):
    marca = (reg.get('marca') or '').lower()
    return [x for x in REGISTROS
            if (x.get('marca') or '').lower() == marca and x['id'] != reg['id']]


def quem(titulo):
    escolhido, _ = casar.casar(titulo, REGISTROS, irmaos_de)
    return escolhido['id'] if escolhido else None


def porque(titulo, ident):
    for linha in casar.casar(titulo, REGISTROS, irmaos_de)[1]:
        if linha['id'] == ident:
            return linha['motivo'] or ''
    return ''


# --------------------------------------------------------------- OS QUE CASAM
# Um anuncio medido hoje para cada registro que subiu de degrau neste bloco.
CASAM = [
    ('Verniz Acrílico Brilhante Transparente Acrilex 250ml Artesanato Tela Pintura',
     'acrilex-verniz-acrilico-brilhante'),
    ('Verniz Acrílico Fosco 250ml Acrilex Transparente Artesanato',
     'acrilex-verniz-acrilico-fosco'),
    ('Verniz Acrilfix Brilhante Acrilex 300 ml - 10672',
     'acrilex-verniz-acrilfix-brilhante'),
    ('Verniz Protetor de Piso 1L Quartzolit ',
     'quartzolit-verniz-protetor-para-pisos'),
    ('Torquês Para Mosaico Com Roldanas de Metal Duro - 61341 Cortag',
     'cortag-torques-mosaico-roldanas'),
    ('Torquês  Alicate Azulejista Corte Reto Cortag - 8 polegadas',
     'cortag-torques-azulejista-corte-reto'),
    ('Cortador de cerâmicas e azulejos manual, 51 cm, VDEC\n51, VONDER',
     'vonder-vdec-51'),
    ('Cortador de cerâmicas e azulejos manual, 51 cm, VDEC 51, VONDER 6851050000',
     'vonder-vdec-51'),
    ('Adesivo Silicone Acético Maxx Transparente 280g Tekbond',
     'tekbond-silicone-acetico-maxx'),
]
for titulo, esperado in CASAM:
    af(quem(titulo) == esperado,
       'deveria casar com %s e casou com %r: %s' % (esperado, quem(titulo), titulo[:60]))

# O `\n` no meio do titulo da Vonder e real e nao pode mudar o resultado: a
# quebra em tokens ignora tudo que nao e letra nem digito.
af(quem('Cortador de cerâmicas e azulejos manual, 51 cm, VDEC\n51, VONDER')
   == quem('Cortador de cerâmicas e azulejos manual, 51 cm, VDEC 51, VONDER'),
   'a quebra de linha dentro do titulo mudou o casamento')

# ------------------------------------------------- TRAVA 3 e 4: OS IRMAOS
# Medidos hoje: o anuncio que vende a ESCOLHA entre dois registros nao
# identifica nenhum dos dois. Sao os titulos que fizeram a trava 4 existir.
ESCOLHA = [
    'Verniz para Couro Acrilex 100ml Fosco Semibrilho Brilhante Base Água E Tinta',
    'Verniz Acrílico Acrilex 100ml / 250ml / 500ml (Fosco ou Brilhante)',
    'Verniz Acrilex Acrilfix Fosco, SemiBrilho ou Brilhante Spray 300 ml',
]
for titulo in ESCOLHA:
    af(quem(titulo) is None, 'anuncio de escolha entre irmaos casou: %s' % titulo[:60])
af('vendendo a escolha' in porque(ESCOLHA[1], 'acrilex-verniz-acrilico-brilhante'),
   'o motivo do anuncio de escolha nao nomeia a escolha')

# O 51 e o 75 e o 90 sao irmaos e o numero e o que os separa.
af(quem('Cortador de cerâmicas e azulejos manual, 75 cm, VDEC 75, VONDER') == 'vonder-vdec-75',
   'o 75 nao casou com o proprio anuncio')
af(quem('Cortador de cerâmicas e azulejos manual, VDEC, VONDER') is None,
   'anuncio sem o numero casou com um dos tres cortadores')

# ------------------------------------------------- TRAVA 1: A MARCA
af(quem('Verniz Acrílico Brilhante Transparente 250ml Artesanato Tela') is None,
   'titulo sem marca nenhuma casou')
af('marca' in porque('Verniz Acrílico Brilhante Transparente 250ml',
                     'acrilex-verniz-acrilico-brilhante'),
   'o motivo de titulo sem marca nao fala em marca')

# ------------------------------------- TRAVA 2: A CABECA DO TITULO E O PRODUTO
af(quem('Pincel Trincha para aplicar Verniz Acrílico Brilhante Acrilex 250ml') is None,
   'o acessorio com o produto no meio do titulo casou (armadilha 1 da 25.7)')
af('cabeca' in porque('Pincel Trincha para aplicar Verniz Acrílico Brilhante Acrilex 250ml',
                      'acrilex-verniz-acrilico-brilhante'),
   'o motivo do acessorio nao fala na cabeca do titulo')

# ------------------------------------------------- TRAVA 5a: AS ARMADILHAS
# Medidos hoje na chave `Cascola PL500`: o mesmo vendedor anuncia o mesmo
# produto em KIT de 2, 4, 6 e 8. Kit nao e quantidade quando o registro nao e
# um kit (armadilha 2 da 25.7).
af(quem('KIT 4 COLA CASCOLA MONTA&FIXA PL500 360g BRANCO INTERIOR HENKEL') is None,
   'o anuncio de KIT casou')
af(quem('Torquês Para Mosaico Com Roldanas de Metal Duro - 61341 Cortag usado') is None,
   'o anuncio de produto usado casou')
# `manual` NAO e armadilha: tres registros deste banco a trazem no nome.
af(quem('Cortador de cerâmicas e azulejos manual, 90 cm, VDEC 90, VONDER') == 'vonder-vdec-90',
   'a palavra `manual` foi tratada como armadilha e derrubou um casamento certo')

# ------------------------------- TRAVA 5b: O TITULO TRAZ O NOME COMERCIAL INTEIRO
# A trava que nasceu do ensaio: `selador quartzolit` devolve PU40, PU30 e Primer
# Flex, e NENHUM deles e o `fundo selador` do banco. Todos os quatro titulos
# abaixo sao reais, de 29/09/2026.
SELADOR = [
    'Selante PU40 Quartzolit Branco 360g Vedação Flexível.',
    'Selador PU30 Cinza Quartzolit 600g p/ Cimento,Dry Wall,Cerâm',
    'Primer Flex Base Selador Quartzolit 3,6l Piso Vinilico',
    'Silicone Acético Quartzolit 50g – Vedação Profissional!',
]
for titulo in SELADOR:
    af(quem(titulo) != 'quartzolit-fundo-selador',
       'um selante que nao e o fundo selador casou: %s' % titulo[:58])
af('nome comercial' in porque(SELADOR[1], 'quartzolit-fundo-selador'),
   'o motivo do PU30 nao nomeia o nome comercial')

# ------------------------------------------------- AS DUAS BORDAS FABRICADAS
# As duas travas abaixo nao mordem em NENHUM registro que o banco tem hoje, e
# por isso a primeira versao desta bancada nao as media: `mutacoes-casamento.py`
# derrubou as duas e a bancada continuou verde. Bateria que so mede o banco de
# hoje envelhece junto com ele — entao a bancada FABRICA o mundo em que elas
# mordem (regra 2 da secao 8 do contrato: a grade inclui a borda).

# BORDA 1 — A METADE POSITIVA DA TRAVA 3.
# Ela so e a unica a salvar quando o nome comercial de X esta INTEIRO dentro do
# nome comercial do irmao, e o unico separador dos dois e o codigo. Hoje isso
# nao existe neste banco; existe no dia em que um fabricante lancar a versao
# "Spray" do que ja vende. Sem a trava 3, o titulo do produto simples casaria
# com ele mesmo E o portao teria aprovado um registro que o titulo nao
# identifica sozinho.
PAR_CONTIDO = [
    {'id': 'fab-verniz-simples', 'marca': 'Fabrica', 'tipo': 'verniz',
     'nome_comercial': 'Verniz Fixador', 'codigo_fabricante': 'FX100'},
    {'id': 'fab-verniz-spray', 'marca': 'Fabrica', 'tipo': 'verniz',
     'nome_comercial': 'Verniz Fixador Spray', 'codigo_fabricante': 'FX200'},
]


def _irmaos_fabricados(reg):
    return [x for x in PAR_CONTIDO if x['id'] != reg['id']]


escolhido, _ = casar.casar('Verniz Fixador Fabrica 200ml', PAR_CONTIDO, _irmaos_fabricados)
af(escolhido is None,
   'o titulo sem codigo casou com o registro cujo nome cabe inteiro no do irmao')
escolhido, _ = casar.casar('Verniz Fixador Fabrica FX100 200ml', PAR_CONTIDO, _irmaos_fabricados)
af(escolhido is not None and escolhido['id'] == 'fab-verniz-simples',
   'o codigo no titulo deveria separar os dois e nao separou')

# Dois registros com o MESMO nome e o mesmo codigo nunca se identificam, e a
# regra tem de dizer isso em vez de escolher um.
GEMEOS = [
    {'id': 'gemeo-a', 'marca': 'Fabrica', 'tipo': 'verniz',
     'nome_comercial': 'Verniz Fixador', 'codigo_fabricante': None},
    {'id': 'gemeo-b', 'marca': 'Fabrica', 'tipo': 'verniz',
     'nome_comercial': 'Verniz Fixador', 'codigo_fabricante': None},
]
escolhido, laudo = casar.casar('Verniz Fixador Fabrica 200ml', GEMEOS,
                               lambda r: [x for x in GEMEOS if x['id'] != r['id']])
af(escolhido is None, 'dois registros gemeos e um deles foi escolhido')
af(any('mesmo nome' in (l['motivo'] or '') for l in laudo),
   'o laudo dos gemeos nao diz que nenhum token os separa')

# BORDA 2 — A UNICIDADE.
# A trava 4 ja derruba o anuncio que vende a escolha entre dois IRMAOS (mesma
# marca e mesmo tipo). O que ela nao alcanca e o LOTE de marcas diferentes: ali
# os dois registros nao sao irmaos um do outro, entao as travas 3 e 4 nao se
# olham, e so a unicidade os derruba.
#
# E O LOTE TEM DE COMECAR PELA PALAVRA QUE OS DOIS DIVIDEM, senao nem chega la:
# a primeira versao deste titulo juntava a torques da Cortag com o cortador da
# Vonder, e a trava 2 sozinha ja derrubava a Vonder — a cabeca do titulo era a
# torques. Dois VERNIZES de marcas diferentes e o caso real: a cabeca serve aos
# dois, e o anuncio de lote e comum em loja de material de arte.
LOTE = ('Verniz Acrílico Brilhante Acrilex 250ml + '
        'Verniz Protetor de Piso 1L Quartzolit')
escolhido, laudo = casar.casar(LOTE, REGISTROS, irmaos_de)
af(escolhido is None, 'o anuncio de LOTE com dois produtos casou com um deles')
af(any('armadilha 5' in (l['motivo'] or '') for l in laudo),
   'o laudo do lote nao nomeia a armadilha 5 da 25.7')

# ------------------------------------------------- O LAUDO NUNCA VEM VAZIO
_, laudo = casar.casar('Verniz Acrílico Brilhante Acrilex 100ml', REGISTROS, irmaos_de)
af(len(laudo) == len(REGISTROS), 'o laudo nao tem uma linha por registro')
af(all(l['passou'] or l['motivo'] for l in laudo),
   'ha registro reprovado sem motivo escrito')

# ------------------------------------------------- A QUEBRA EM TOKENS
af(casar.tokens('VDEC-51') == casar.tokens('VDEC 51'),
   'o hifen mudou a quebra em tokens')
af('51' in casar.tokens('VDEC 51') and '510' not in casar.tokens('VDEC 51'),
   'o token 51 virou prefixo de 510 (armadilha 4 da 25.7)')
af('510' in casar.tokens('VDEC 510') and '51' not in casar.tokens('VDEC 510'),
   'o sufixo do modelo foi lido como o modelo')
af(casar.normalizar('Acrílico') == casar.normalizar('acrilico'),
   'o acento mudou a palavra')
af(casar.normalizar('pisos') == casar.normalizar('piso'),
   'o plural de cinco letras ou mais nao cai')
af(casar.normalizar('mais') != casar.normalizar('mai'),
   'o corte do plural comeu palavra curta')

print('teste-casamento: %d afirmacoes, %d falha(s)' % (afirmacoes, len(falhas)))
for f in falhas:
    print('  FALHA: %s' % f)
sys.exit(1 if falhas else 0)

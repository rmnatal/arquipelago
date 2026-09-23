#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao do casamento da coleta da Shopee — SEM REDE.

    python3 ferramentas/teste-coleta-shopee.py

Mede `ferramentas/coletar-shopee.py` contra titulos de anuncio REAIS e contra
titulos construidos para serem a armadilha exata que a secao 25.7 do contrato
nomeia. Nenhuma chamada de rede: o que entra aqui e um titulo, e o que sai e o
veredito do portao.

POR QUE ESTE PORTAO EXISTE, e por que ele nasce junto com a ferramenta: um
casamento errado no banco e pior que casamento nenhum, porque **parece dado**.
Quem le a C5 nao tem como saber que o botao de 25 W abre o anuncio de 300 W —
a pagina fica com a cara de certa. O portao e o unico lugar em que esse erro
consegue aparecer antes de chegar ao leitor.

E TRES DAS AFIRMACOES ABAIXO NAO SAO HIPOTESE: sao defeitos que o portao pegou
em mim enquanto eu o escrevia, em 23/09/2026, e cada um esta comentado no lugar
onde mora a regra que o conserta.
"""

import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_spec = importlib.util.spec_from_file_location(
    'coletor', os.path.join(RAIZ, 'ferramentas', 'coletar-shopee.py'))
coletor = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(coletor)

afirmacoes = 0
falhas = []


def ok(titulo, condicao, detalhe=''):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append('%s — %s' % (titulo, detalhe))


def carregar_banco():
    banco = {}
    for nome in ('aquecedor', 'filtro', 'iluminacao', 'midia'):
        caminho = os.path.join(RAIZ, 'dados', 'produtos-%s.json' % nome)
        with open(caminho, encoding='utf-8') as f:
            banco[nome] = json.load(f).get('produtos') or []
    return banco


BANCO = carregar_banco()


def registro(ident):
    for irmaos in BANCO.values():
        for p in irmaos:
            if p.get('id') == ident:
                return p, irmaos
    raise SystemExit('o teste cita um id que nao existe no banco: %s' % ident)


# ---------------------------------------------------------------------------
# OS CASOS. Cada linha e (id do registro, titulo do anuncio, casa?).
# ---------------------------------------------------------------------------
CASOS = [
    # --- titulos REAIS, devolvidos pela API em 23/09/2026 ---
    ('roxin-ht-1300-q3-25w',
     'Termostato Com Aquecedor Roxin Ht-1300 25w Para Aquário', True),
    ('roxin-ht-1300-q3-200w',
     'Termostato Com Aquecedor Roxin Ht-1300 200w Aquário', True),

    # A ARMADILHA DA VARIANTE, que e a desta ilha. O titulo traz a marca certa
    # e a linha certa, e a potencia do VIZINHO. Sem este portao, a C5 promete
    # 25 W e a pessoa recebe 200 W.
    ('roxin-ht-1300-q3-25w',
     'Termostato Com Aquecedor Roxin Ht-1300 200w Aquário', False),
    ('roxin-ht-1300-q3-25w',
     'Termostato Aquecedor Roxin 50w Aquário até 50 litros HT-1300/Q3', False),

    # A MEDIDA CALADA. O anuncio nao mente: ele so nao diz qual das cinco
    # potencias e. Numa linha em que a potencia e o que separa um irmao do
    # outro, "nao diz" e o mesmo que "nao da para provar".
    ('roxin-ht-1300-q3-25w', 'Aquecedor Roxin HT-1300 aquario', False),

    # O SEPARADOR E DE QUEM ESCREVE O ANUNCIO. "HT1300" e "HT-1300" sao o
    # mesmo aquecedor em duas lojas.
    ('roxin-ht-1300-q3-25w', 'Aquecedor Roxin HT1300 25 W aquario', True),

    # ARMADILHA 1 DA 25.7, virada do avesso: la a peca era o produto, aqui a
    # peca e o ruido. Loja de reposicao escreve o codigo do aparelho no titulo
    # da tampa dele.
    ('roxin-ht-1300-q3-25w', 'Tampa Do Aquecedor Roxin HT-1300 25w', False),
    ('atman-at-3338', 'Rotor Impelidor Para Filtro Atman AT-3338', False),

    # ARMADILHA 2 DA 25.7: "kit" quando o registro nao e kit.
    ('roxin-ht-1300-q3-25w',
     'Kit Aquecedor Roxin HT-1300 25w com termometro', False),

    # ARMADILHA 4 DA 25.7: o sufixo faz outro aparelho. Os dois moram neste
    # banco e diferem por uma letra — o B tem UV de 9 W.
    ('sunsun-hw-303b', 'Filtro Canister SunSun HW-303B 1400L/H com UV', True),
    ('sunsun-hw-303b', 'Filtro Canister SunSun HW-303 1400L/H', False),
    ('sunsun-hw-303b', 'Filtro Canister SunSun HW-603B', False),
    ('atman-at-3338', 'Filtro Canister Atman AT-3338 1350L/H', True),
    ('atman-at-3338', 'Filtro Canister Atman AT-3338S 1350L/H', False),

    # O PORTAO DA MEDIDA NAO PODE SER LIGADO EM TODO MUNDO. O varejo de
    # aquarismo anuncia canister pela VAZAO, nunca pelo consumo em watts —
    # exigir "35 W" no titulo do HW-303B reprovaria o anuncio certo. E ele nao
    # precisa da medida: o codigo dele ja e unico no banco. Esta foi a primeira
    # coisa que o portao pegou em mim.
    ('sunsun-hw-303b', 'Filtro Canister SunSun HW-303B com UV 9w 110v', True),

    # A LUMINARIA, que e o caso que esta ilha ja pagou no ar em 07/09/2026.
    ('ista-i-401-45', 'Luminaria Ista I-401 45cm LED aquario plantado', True),
    ('ista-i-401-45', 'Luminaria Ista I-401 60cm LED aquario plantado', False),

    # O CODIGO BASE TEM DE SOBREVIVER AO "cm" COLADO. Exigir "WRGB II Pro 60"
    # como um token so reprova o anuncio certo, porque "60cm" nao tem fronteira
    # depois do 60. Segunda coisa que o portao pegou em mim.
    ('chihiros-wrgb-ii-pro-60', 'Luminaria Chihiros WRGB II Pro 60cm', True),
    ('chihiros-wrgb-ii-pro-60', 'Luminaria Chihiros WRGB II Pro 90cm', False),
    ('chihiros-wrgb-ii-pro-60',
     'Luminaria Chihiros WRGB II Pro para aquario plantado', False),
    # Pro, Slim e a WRGB II pelada sao TRES linhas no mesmo banco.
    ('chihiros-wrgb-ii-pro-60', 'Luminaria Chihiros WRGB II Slim 60cm', False),

    # O NUMERO QUE E CODIGO NAO E VARIANTE. "classic 250 (2213)": o 2213 e o
    # codigo do filtro e nao o tamanho dele, e uma regra que jogasse fora todo
    # numero final comeria justamente o que identifica o produto. Terceira
    # coisa que o portao pegou em mim.
    ('eheim-classic-250-2213',
     'Filtro Canister Eheim Classic 250 2213 220v', True),
    ('eheim-classic-250-2213', 'Filtro Canister Eheim Classic 600 2217', False),

    # A MIDIA E CONSUMIVEL, entao "refil" no titulo dela e o produto — nao uma
    # peca de outro aparelho.
    ('seachem-matrix-1l', 'Seachem Matrix 1L midia biologica refil', True),
    ('seachem-matrix-1l', 'Seachem Matrix 2L midia biologica', False),
    ('seachem-matrix-1l', 'Seachem Matrix 1000ml midia biologica', True),

    # O SUFIXO QUE VEM DO BANCO, e este e o caso mais perigoso da ilha: a
    # Chihiros tem TRES linhas aqui — WRGB II, WRGB II Pro e WRGB II Slim — e o
    # codigo da primeira esta inteiro dentro do titulo das outras duas. A WRGB
    # II 90 e a WRGB II Pro 90 sao as DUAS de 90 cm, entao nem o portao da
    # medida as separa: so o sufixo. Sem isso a C15 prometeria 100 W e abriria
    # o anuncio de 110 W.
    ('chihiros-wrgb-ii-90', 'Luminaria Chihiros WRGB II 90cm aquario plantado', True),
    ('chihiros-wrgb-ii-90', 'Luminaria Chihiros WRGB II Pro 90cm', False),
    ('chihiros-wrgb-ii-90', 'Luminaria Chihiros WRGB II Slim 90cm', False),

    # A MARCA E NECESSARIA E NUNCA SUFICIENTE (25.3). Sem ela, "Matrix" sozinho
    # casa com qualquer coisa.
    ('seachem-matrix-1l', 'Matrix 1L midia biologica para aquario', False),
    ('roxin-ht-1300-q3-25w', 'Aquecedor Atman HT-1300 25w', False),
]

for ident, titulo, esperado in CASOS:
    reg, irmaos = registro(ident)
    obtido, motivo = coletor.casa({'titulo': titulo}, reg, irmaos)
    ok('%s %s: %s' % (ident, 'CASA' if esperado else 'NAO casa', titulo[:64]),
       obtido == esperado,
       'obtido=%s motivo=%s' % (obtido, motivo))

# ---------------------------------------------------------------------------
# O PORTAO DA MEDIDA SAI DO BANCO, e e isso que faz irmao novo liga-lo sozinho
# ---------------------------------------------------------------------------
ESPERADO_GATE = {
    # linha em que varios irmaos dividem o mesmo codigo: so a medida separa
    'roxin-ht-1300-q3-25w': True,
    'eheim-jager-50w': True,
    'chihiros-wrgb-ii-pro-60': True,
    # codigo ja unico no banco: a medida nao precisa estar no titulo
    'sunsun-hw-303b': False,
    'atman-at-3338': False,
    'seachem-matrix-1l': False,
    'ista-i-401-45': False,
}
for ident, esperado in ESPERADO_GATE.items():
    reg, irmaos = registro(ident)
    ok('%s: portao da medida %s' % (ident, 'LIGADO' if esperado else 'desligado'),
       coletor.medida_discrimina(reg, irmaos) == esperado,
       'base=%r' % coletor.codigo_base(reg))

# OS SUFIXOS QUE O BANCO DECLARA. Sao eles que separam a WRGB II da WRGB II
# Pro, e eles nascem da comparacao entre irmaos — nao de lista escrita a mao.
ESPERADO_SUFIXOS = {
    'chihiros-wrgb-ii-90': {'pro', 'slim'},
    'chihiros-wrgb-ii-pro-60': set(),
    'roxin-ht-1300-q3-25w': set(),
}
for ident, esperado in ESPERADO_SUFIXOS.items():
    reg, irmaos = registro(ident)
    ok('%s: sufixos de irmao = %s' % (ident, sorted(esperado) or 'nenhum'),
       coletor.sufixos_irmaos(reg, irmaos) == esperado,
       'obtido=%r' % sorted(coletor.sufixos_irmaos(reg, irmaos)))

# A LISTA DE IRMAOS CHEGA MESMO ATE O PORTAO. As duas regras acima leem o
# banco, e as duas viram letra morta se `main` chamar `casa` sem os irmaos —
# defeito que nao aparece em teste nenhum que chame `casa` direto, porque o
# teste passa os irmaos na mao. Entao afirma-se a FIACAO.
import inspect
fonte_main = inspect.getsource(coletor.main)
ok('main() passa a lista de irmaos para casa()',
   'casa(o, r, irmaos)' in fonte_main,
   'a chamada de casa() dentro de main() nao carrega irmaos')
ok('main() monta os registros com os irmaos do mesmo banco',
   'for caminho, r, irmaos in registros' in fonte_main,
   'o laco de main() nao carrega irmaos')

# O CODIGO BASE, afirmado valor a valor. E ele que decide as duas coisas acima.
ESPERADO_BASE = {
    'roxin-ht-1300-q3-25w': 'ht-1300',
    'sunsun-hw-303b': 'hw-303b',
    'chihiros-wrgb-ii-pro-60': 'wrgb ii pro',
    'seachem-matrix-1l': 'matrix',
    'ista-i-401-45': 'i-401',
    'eheim-classic-250-2213': 'classic 250 2213',
}
for ident, esperado in ESPERADO_BASE.items():
    reg, _ = registro(ident)
    ok('%s: codigo base e %r' % (ident, esperado),
       coletor.codigo_base(reg) == esperado,
       'obtido=%r' % coletor.codigo_base(reg))

# ---------------------------------------------------------------------------
# NENHUM REGISTRO DO BANCO PODE FICAR SEM IDENTIDADE. Registro cujo codigo base
# sai vazio passaria pelo portao do codigo sem ser conferido — e sairia casando
# com qualquer anuncio da marca.
# ---------------------------------------------------------------------------
for nome, irmaos in BANCO.items():
    for p in irmaos:
        ok('%s: tem codigo base ou linha' % p.get('id'),
           bool(coletor.codigo_base(p) or p.get('linha')),
           'modelo=%r linha=%r' % (p.get('modelo'), p.get('linha')))

# REGISTRO SEM MARCA NAO RECEBE FICHA, e isso se afirma em vez de se supor. O
# banco aceita `marca: null` de propósito (importado revendido com o nome da
# loja) e chama esse caso de "o pior caso do banco". Sem marca a condicao
# necessaria da 25.3 nao existe, entao o portao TEM de recusar — qualquer
# anuncio da categoria casaria. Sao dois registros hoje; a afirmacao vale para
# quantos vierem.
sem_marca = [p for irmaos in BANCO.values() for p in irmaos if not p.get('marca')]
ok('o banco tem registro sem marca (se deixar de ter, esta afirmacao avisa)',
   bool(sem_marca), 'nenhum registro sem marca')
for p in sem_marca:
    irmaos = next(v for v in BANCO.values() if p in v)
    obtido, motivo = coletor.casa(
        {'titulo': '%s original pronta entrega' % (p.get('modelo') or '')}, p, irmaos)
    ok('%s: sem marca, NAO recebe ficha' % p.get('id'), obtido is False,
       'o portao aprovou um anuncio para um registro sem marca')
    # E O MOTIVO TEM DE DIZER QUE E O REGISTRO QUE NAO DECLARA, nao que o
    # titulo nao traz. Sem esta distincao a recusa continua acontecendo por
    # acidente — `token_no_titulo(None, ...)` tambem devolve falso — e o dia em
    # que alguem mexer naquela funcao a protecao some sem ninguem ver.
    ok('%s: e o motivo diz que o REGISTRO nao declara marca' % p.get('id'),
       'nao declara marca' in (motivo or ''), 'motivo=%r' % motivo)

print('\n%d afirmacoes, %d falha(s)' % (afirmacoes, len(falhas)))
if falhas:
    for f in falhas:
        print('  FALHOU: %s' % f)
sys.exit(1 if falhas else 0)

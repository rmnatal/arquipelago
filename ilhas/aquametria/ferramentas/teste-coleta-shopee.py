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

    # ---------------------------------------------------------------------
    # O CODIGO DE CATALOGO GANHOU CAMPO PROPRIO (14/10/2026, esquema 13), E
    # ESTES SEIS CASOS SAO A DIVIDA QUE ELE PAGOU. O anuncio da primeira linha e
    # REAL, esta guardado em `afiliado.anuncio_shopee` deste registro desde
    # 07/09/2026, e foi RECUSADO por doze dias com o motivo "o titulo nao traz o
    # codigo (classic 250 2213)": o campo `modelo` empacotava o nome da linha e
    # o codigo do fabricante num campo so, o portao os exigia CONTIGUOS, e o
    # varejo brasileiro escreve os dois separados com a vazao e a marca no meio.
    # Era a UNICA divida de ficha desta ilha que era nossa (as outras 11 sao
    # mercado, medidas em dados/divida-25-4-b-2026-10-14.md).
    ('eheim-classic-250-2213',
     'Filtro Canister Classic 250 440lh Eheim - 2213', True),
    # O TITULO QUE CALA O CODIGO NAO BARRA, e e esta metade que faz o campo ser
    # confirmacao OPCIONAL em vez de exigencia nova. Se esta afirmacao cair, o
    # conserto virou outro jeito de escrever o mesmo defeito.
    ('eheim-classic-250-2213', 'Filtro Canister Eheim Classic 250 440 L/h', True),
    # E A OUTRA METADE, que e o que paga o afrouxamento: o codigo de um IRMAO no
    # titulo barra sempre. "Classic 250 ... 2217" nao e um anuncio incompleto do
    # 2213, e um anuncio do 2217 — e essa protecao nao existia antes de o campo
    # existir, porque antes nenhum registro declarava codigo nenhum.
    ('eheim-classic-250-2213',
     'Filtro Canister Eheim Classic 250 - 2217 1000l/h', False),
    # A GRAFIA DA MARCA CONTINUA BARRANDO. Este titulo tambem e real, foi o
    # segundo candidato do ensaio de hoje, e foi recusado com razao: o vendedor
    # escreveu "Ehein".
    ('eheim-classic-250-2213',
     'Filtro Canister Ehein Classic 250 - 440 L/h ( 2213 ) 110v', False),
    # OS DOIS CLASSIC 600 JA CASAVAM EM 24/09/2026 E TEM DE CONTINUAR CASANDO:
    # o conserto de hoje encurta o codigo base deles de "classic 600 2217" para
    # "classic 600", e um conserto que quebra o que estava verde nao e conserto.
    ('eheim-classic-600-2217-220v',
     'Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w 220v', True),
    # E A VOLTAGEM CONTINUA SEPARANDO OS GEMEOS com o codigo base mais curto:
    # os dois 2217 dividem o mesmo codigo, entao quem os separa e a medida.
    ('eheim-classic-600-2217-127v',
     'Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w 220v', False),

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

    # ---------------------------------------------------------------------
    # OS SEIS QUE O ENSAIO DE 23/09/2026 ACHOU NO AR. Todos sao titulos REAIS
    # devolvidos pela API, e todos tinham CASADO antes destas regras existirem.
    # E a prova de que conferir a amostra com os olhos (25.3) nao e cerimonia:
    # nenhum deles seria pego por teste escrito de cabeca.
    # ---------------------------------------------------------------------

    # A VOLTAGEM DO ANUNCIO E MEDIDA. Sete registros Maxxi existem separados
    # por ela — o M-200 aparece duas vezes, uma por anuncio. Sem le-la, os dois
    # gemeos casaram com o MESMO anuncio de 110 V.
    ('maxxi-m-200-anuncio-220v',
     'Aquecedor Termostato Maxxi M-200 200w Para Aquários 110v', False),
    ('maxxi-m-200-anuncio-110v',
     'Aquecedor Termostato Maxxi M-200 200w Para Aquários 110v', True),
    # O ANUNCIO CALADO SOBRE O DISCRIMINADOR NAO CASA. Os dois M-200 tem a
    # MESMA potencia e existem separados so pela voltagem: um titulo que diz
    # "200W" e nao diz volt nenhum nao prova qual dos dois e. Exigir "alguma
    # medida" aceitava esse anuncio pelo 200 W, que e igual nos gemeos.
    ('maxxi-m-200-anuncio-220v', 'Maxxi Termostato M-200 200W', False),
    ('maxxi-m-200-anuncio-220v', 'Maxxi Termostato M-200 200W 220v', True),
    # E onde o codigo ja e unico no banco, a voltagem nao e cobrada: o M-100
    # nao tem gemeo, entao o anuncio calado sobre volt continua valendo.
    ('maxxi-m-100-anuncio-127v', 'Maxxi Termostato M-100 100W', True),

    ('maxxi-m-050-anuncio-220v',
     'Maxxi Termostato M-050 50W 127V - Termostato para Aquários', False),
    # 110 e 127 sao a mesma tomada, e o varejo usa os dois nomes.
    ('maxxi-m-100-anuncio-127v', 'Maxxi Termostato M-100 100W 110v', True),
    ('sunsun-hw-702a-anuncio-110v',
     'Filtro Canister Sunsun Hw -702a Aquario 300 Litros 220v', False),

    # A LAMPADA UV DO CANISTER NAO E O CANISTER.
    ('sunsun-hw-303b',
     'Lâmpada Filtro Canister Hw 303b / 304b Uv 9w Sunsun Aquario', False),

    # O BALDE E PECA, E A PALAVRA QUE O DENUNCIA VEM NO FIM DO TITULO — fora
    # dos 40 primeiros caracteres em que o portao olhava.
    ('atman-at-3338',
     'Balde Para Filtro Canister Atman AT-3335 AT-3336 AT-3337 AT-3338 '
     'Peça de Reposição', False),

    # E A DENUNCIA TEM DE VALER NO TITULO INTEIRO, nao so na cabeca: aqui a
    # cabeca e o aparelho, certinha, e o que denuncia vem no fim. Sem esta
    # afirmacao a regra do titulo inteiro nao e medida por nada.
    ('atman-at-3338',
     'Filtro Canister Atman AT-3338 1350l/h Original - Peça de Reposição', False),

    # O REFIL DE UM FILTRO E PECA; o de uma midia e o produto.
    ('atman-hf-0400', 'Refil Filtro Atman HF-0400', False),
    ('seachem-matrix-1l', 'Refil Midia Biologica Seachem Matrix 1L', True),

    # ARMADILHA 5: o anuncio nomeia DOIS registros do banco.
    ('atman-hf-0800', 'Filtro Externo Atman HF-0600 HF-0800', False),

    # MATRIX E MATRIXCARBON SAO PRODUTOS DIFERENTES, e os dois estao no banco:
    # um e colonia de bacteria, o outro adsorve. O anuncio do carvao casou com
    # a midia biologica.
    ('seachem-matrix-1l',
     'Carvão Ativado Matrix Carbon 1 L Seachem Filtragem Aquário', False),
    ('seachem-matrixcarbon-250ml',
     'Carvão Ativado Seachem MatrixCarbon 250ml', True),

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
ESPERADO_UNIDADES = {
    'maxxi-m-200-anuncio-220v': {'v'},     # mesma potencia, so a volt separa
    'roxin-ht-1300-q3-25w': {'w'},         # mesma linha, so a potencia separa
    'chihiros-wrgb-ii-pro-60': {'cm', 'w'},
    'maxxi-m-100-anuncio-127v': set(),     # sem gemeo de mesmo codigo
    'sunsun-hw-303b': set(),
}
for ident, esperado in ESPERADO_UNIDADES.items():
    reg, irmaos = registro(ident)
    ok('%s: unidade que discrimina = %s' % (ident, sorted(esperado) or 'nenhuma'),
       coletor.unidades_discriminantes(reg, irmaos) == esperado,
       'obtido=%r' % sorted(coletor.unidades_discriminantes(reg, irmaos)))

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

# ---------------------------------------------------------------------------
# O CODIGO DE CATALOGO DO FABRICANTE (14/10/2026, esquema 13)
# ---------------------------------------------------------------------------
# O campo existe porque `modelo` empacotava dois identificadores num campo so, e
# o portao exige as partes do codigo contiguas no titulo. Ele e lido em dois
# lugares de sentido oposto, e as duas direcoes sao afirmadas aqui:
#   `codigo_base()`   TIRA o codigo do que o portao exige  -> afrouxa
#   `codigo_catalogo_conflitante()` barra o codigo do irmao -> aperta
# Medir so a primeira deixaria um afrouxamento verde.
CATALOGO_ESPERADO = {
    'eheim-classic-250-2213': '2213',
    'eheim-classic-600-2217-220v': '2217',
    'eheim-classic-600-2217-127v': '2217',
}
for ident, esperado in CATALOGO_ESPERADO.items():
    reg, _ = registro(ident)
    ok('%s: codigo de catalogo declarado = %r' % (ident, esperado),
       reg.get('codigo_catalogo') == esperado,
       'obtido=%r' % reg.get('codigo_catalogo'))

# A CHAVE EXISTE EM TODO REGISTRO, e null e a declaracao de que o fabricante nao
# publica codigo separado do nome do modelo. Chave ausente nao declara nada — e
# a mesma razao do `afiliado.intestavel`: divida escrita em observacao nao se
# conta. E a regra executavel disto e a V28 do validador; aqui ela e afirmada de
# novo porque a coleta LE este campo, e campo que a coleta le e portao da coleta.
for nome, irmaos in BANCO.items():
    for p in irmaos:
        ok('%s: declara a chave codigo_catalogo' % p.get('id'),
           'codigo_catalogo' in p, 'chave ausente no banco de %s' % nome)
        # E O CODIGO DECLARADO E UM RECORTE DO MODELO, nunca identidade nova.
        # Esta e a metade que impede o afrouxamento pela porta do DADO: um
        # codigo que nao esta no modelo tiraria do codigo base um pedaco que
        # ninguem escreveu, e o portao ficaria folgado sem uma linha de regua
        # mudar.
        codigo = p.get('codigo_catalogo')
        if codigo:
            ok('%s: o codigo de catalogo esta dentro do modelo' % p.get('id'),
               coletor.token_no_titulo(codigo, p.get('modelo') or ''),
               'codigo=%r modelo=%r' % (codigo, p.get('modelo')))
            ok('%s: e o codigo de catalogo nao e o modelo inteiro' % p.get('id'),
               bool(coletor.codigo_base(p)),
               'o registro ficaria sem codigo base')

# O BANCO TEM DE TER O CASO (se deixar de ter, esta afirmacao avisa). Sem um
# registro que declare codigo de catalogo, as duas regras acima ficam verdes
# sem exercer nada — e o campo vira decoracao no esquema.
com_codigo = [p for irmaos in BANCO.values() for p in irmaos if p.get('codigo_catalogo')]
ok('o banco tem registro com codigo de catalogo declarado',
   bool(com_codigo), 'nenhum registro declara codigo de catalogo')

# A FUNCAO DO CONFLITO, afirmada nos tres mundos dela. O do meio e o que torna
# o campo opcional, e e o unico que, se virar False->True, desfaz o conserto.
_reg_250, _irmaos_f = registro('eheim-classic-250-2213')
ok('codigo proprio no titulo: confirmacao positiva, nenhum irmao e conferido',
   coletor.codigo_catalogo_conflitante(
       _reg_250, _irmaos_f, 'Filtro Canister Classic 250 440lh Eheim - 2213') is None,
   'o portao achou conflito num titulo que declara o codigo DESTE registro')
ok('codigo calado no titulo: nao ha conflito',
   coletor.codigo_catalogo_conflitante(
       _reg_250, _irmaos_f, 'Filtro Canister Eheim Classic 250 440 L/h') is None,
   'o portao inventou conflito num titulo que nao declara codigo nenhum')
ok('codigo do irmao no titulo: o portao devolve o codigo do irmao',
   coletor.codigo_catalogo_conflitante(
       _reg_250, _irmaos_f, 'Filtro Canister Eheim Classic 250 - 2217') == '2217',
   'obtido=%r' % coletor.codigo_catalogo_conflitante(
       _reg_250, _irmaos_f, 'Filtro Canister Eheim Classic 250 - 2217'))
# SO IRMAO DA MESMA MARCA: digito igual em outra marca e coincidencia, nao
# conflito, e barrar por isso seria inventar defeito onde ha so um numero.
#
# ESTE CASO E CONSTRUIDO, E A CONSTRUCAO E O PONTO: hoje os TRES registros que
# declaram codigo de catalogo sao Eheim e moram no mesmo banco, entao a regra da
# marca nao e exercida por dado nenhum — uma afirmacao tirada do banco de hoje
# ficaria verde sem medir nada, que e o que esta ilha chama de INERTE. O mundo
# abaixo e o de amanha: o dia em que outra marca declarar codigo. Quem apagar a
# regra da marca ve esta linha cair; quem a mantiver, nao.
_outra_marca = {'id': 'marca-vizinha-fingida', 'marca': 'Atman',
                'modelo': 'AT-9999', 'codigo_catalogo': '9999'}
ok('o conflito nao atravessa a marca',
   coletor.codigo_catalogo_conflitante(
       _reg_250, list(_irmaos_f) + [_outra_marca],
       'Filtro Canister Eheim Classic 250 440 L/h 9999') is None,
   'o portao barrou o Eheim pelo codigo de catalogo de uma Atman')
# E A DIRECAO OPOSTA, para a afirmacao de cima nao passar por acidente: o mesmo
# codigo, na mesma marca, BARRA.
ok('o conflito acontece dentro da marca',
   coletor.codigo_catalogo_conflitante(
       _reg_250, list(_irmaos_f) + [dict(_outra_marca, marca='Eheim')],
       'Filtro Canister Eheim Classic 250 440 L/h 9999') == '9999',
   'o portao nao barrou com o codigo de um irmao da mesma marca no titulo')

# A FIACAO: o portao do conflito tem de ser CHAMADO por `casa()`. Sem esta
# afirmacao a funcao pode ficar escrita, testada e nunca executada — que e a
# mesma armadilha do `main() passa a lista de irmaos` logo acima.
fonte_casa = inspect.getsource(coletor.casa)
ok('casa() chama o portao do codigo de catalogo',
   'codigo_catalogo_conflitante(registro, irmaos, titulo)' in fonte_casa,
   'o portao do codigo de catalogo nao e chamado dentro de casa()')
# E ELE RODA FORA DO `if base:`, senao registro sem codigo base perde a trava.
ok('o portao do codigo de catalogo nao depende de haver codigo base',
   coletor.casa({'titulo': 'Filtro Canister Eheim Classic 250 - 2217'},
                dict(_reg_250, modelo='', linha=None), _irmaos_f)[0] is False,
   'um registro sem codigo base passou com o codigo do irmao no titulo')

# O CODIGO BASE, afirmado valor a valor. E ele que decide as duas coisas acima.
ESPERADO_BASE = {
    'roxin-ht-1300-q3-25w': 'ht-1300',
    'sunsun-hw-303b': 'hw-303b',
    'chihiros-wrgb-ii-pro-60': 'wrgb ii pro',
    'seachem-matrix-1l': 'matrix',
    'ista-i-401-45': 'i-401',
    # ERA 'classic 250 2213' ATE 14/10/2026, e o valor antigo e o defeito em
    # pessoa: ele exigia no titulo um codigo que o varejo brasileiro nunca
    # escreve contiguo. O `2213` saiu daqui para o campo `codigo_catalogo` e
    # voltou como confirmacao opcional — ver o bloco do codigo de catalogo logo
    # abaixo e o cabecalho de `codigo_base()`.
    'eheim-classic-250-2213': 'classic 250',
    'eheim-classic-600-2217-220v': 'classic 600',
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


# ---------------------------------------------------------------------------
# A DECISAO DE PRESERVAR OU REESCOLHER A FICHA (25.4-b.1 e 25.4-b.2)
# ---------------------------------------------------------------------------
# Item 2 do despacho da Sentinela de 23/09/2026. Ate aquele dia esta decisao era
# um `if` dentro do `main()` e portao nenhum a alcancava — a bancada media o
# CASAMENTO e nao media a escolha entre manter um link e troca-lo, que e a mais
# cara desta ferramenta. As tres afirmacoes abaixo sao os tres mundos que o
# banco produz, e o do meio e o que estava errado: 39 registros com `url` e sem
# `url_produto` eram protegidos por uma trava que existia para proteger
# atribuicao, e ficavam `intestavel: true` para sempre.

preserva, motivo = coletor.preserva_ficha_existente(
    {'url': 'https://s.shopee.com.br/ABC', 'url_produto': 'https://shopee.com.br/x.i.1.2'})
ok('par completo: a ficha do banco e PRESERVADA', preserva is True, 'motivo=%r' % motivo)
ok('  e o motivo fala do PAR, nao do link', 'PAR' in motivo, 'motivo=%r' % motivo)

preserva, motivo = coletor.preserva_ficha_existente({'url': 'https://s.shopee.com.br/ABC'})
ok('url sem url_produto: a ficha NAO e preservada, o par se reescolhe inteiro',
   preserva is False, 'motivo=%r' % motivo)
ok('  e o motivo diz que o par nao e demonstravel',
   'nao e demonstravel' in motivo or 'nao e\ndemonstravel' in motivo, 'motivo=%r' % motivo)

preserva, motivo = coletor.preserva_ficha_existente({})
ok('registro sem ficha nenhuma: nao ha o que preservar', preserva is False,
   'motivo=%r' % motivo)

# A DIRECAO QUE NENHUMA DAS TRES ACIMA PEGA SOZINHA: a funcao nao pode olhar o
# `url_produto` isolado. Um registro com url_produto e SEM url nao tem ficha de
# afiliado para preservar — preservar ali seria barrar a gravacao de um link que
# o banco nunca teve.
preserva, _ = coletor.preserva_ficha_existente({'url_produto': 'https://shopee.com.br/x.i.1.2'})
ok('url_produto sozinho nao preserva nada', preserva is False)


# ---------------------------------------------------------------------------
# O PARENTESE E SEPARADOR, E A PALAVRA NAO E (24/09/2026)
# ---------------------------------------------------------------------------
# Escrito no mutirao do despacho do Raphael de 24/09, depois que o ensaio da
# coleta mostrou TRES registros recusando o anuncio CERTO, que aparecia na
# primeira pagina da busca:
#
#     "Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w 220v"
#         recusado por "o titulo nao traz o codigo (classic 600 2217)"
#
# A causa e uma regra aplicada de um lado so da comparacao: `codigo_base()`
# troca `(` e `)` por espaco NO MODELO desde que nasceu, mas a classe de
# separadores do `token_no_titulo()` nunca teve parentese, entao o TITULO
# chegava com ele no meio. Regua que devolve zero para sempre por mais certo que
# esteja o anuncio — a mesma familia do falso positivo do `noindex` de aspa
# simples, medido nesta mesma ilha quatro horas antes.
#
# AS AFIRMACOES VEM EM PAR, e o par e o ponto: afrouxar o separador e a metade
# barata, e a metade que importa e a que continua FECHADA. Pontuacao entre as
# partes do codigo passa; PALAVRA entre elas nao passa, porque codigo espalhado
# pelo titulo identificaria tambem o anuncio de kit que cita dois filtros da
# linha.

PASSAM = [
    ('classic 600 2217', 'Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w 220v',
     'o parentese em volta do codigo do filtro'),
    ('classic 600 2217', 'Eheim Classic 600 [2217] bivolt',
     'o colchete, pelo mesmo motivo do parentese'),
    ('classic 600 2217', 'Eheim Classic 600, 2217, 1000 l/h',
     'a virgula separando as partes'),
    ('ht-1300', 'Termostato Com Aquecedor Roxin HT-1300 - Q3 - 300w - 220v',
     'o hifen, que ja passava antes e tem de continuar passando'),
    ('hw-303b', 'Filtro Canister SunSun HW-303B 1400 l/h',
     'o codigo colado, que ja passava antes'),
]
for codigo, titulo, porque in PASSAM:
    ok('passa: %s (%s)' % (porque, codigo),
       coletor.token_no_titulo(codigo, titulo) is True,
       'codigo=%r titulo=%r' % (codigo, titulo))

NAO_PASSAM = [
    ('classic 250 2213', 'Filtro Canister Classic 250 440lh Eheim - 2213',
     'PALAVRA entre as partes do codigo nao e separador'),
    ('classic 250 2213', 'Filtro Canister Ehein Classic 250 - 440 L/h ( 2213 ) 110v',
     'palavra entre as partes, mesmo com parentese em volta da ultima'),
    ('classic 250 2213', 'Kit Eheim Classic 250 e Classic 600 com midia 2213 e 2217',
     'o kit que cita dois filtros da linha — o caso que o afrouxamento criaria'),
    ('classic 600 2217', 'Filtro Canister Eheim Classic 250 (2213) 440l/h',
     'o IRMAO da mesma linha, com parentese: separador solto nao pode confundir irmao'),
    ('hw-303b', 'Filtro Canister SunSun HW-603B',
     'o vizinho de codigo, que a fronteira de token barra'),
    ('ht-1300', 'Aquecedor Roxin HT 13000',
     'o codigo como PEDACO de um numero maior'),
]
for codigo, titulo, porque in NAO_PASSAM:
    ok('NAO passa: %s (%s)' % (porque, codigo),
       coletor.token_no_titulo(codigo, titulo) is False,
       'codigo=%r titulo=%r' % (codigo, titulo))

# O QUE ESTA BANCADA DESCOBRIU E **NAO** CONSERTOU, escrito porque divida
# medida e calada e a que volta:
#
#     token_no_titulo('classic 600 2217', 'Eheim Classic 6002217 bivolt') -> True
#
# As partes GRUDADAS casam, porque o separador e opcional (`*`) — e isso e de
# proposito e anterior a 24/09/2026: e o mesmo mecanismo que faz "HT1300" casar
# com o codigo `HT-1300`, que e como metade do varejo escreve, e que faz `a 301`
# casar com "A301". Nao da para exigir separador entre duas partes sem perder as
# duas colagens legitimas, e nao da para exigi-lo so entre digitos sem perder
# codigos como `2 213`. **Fica afirmado como esta**, e nao como se gostaria, para
# que uma mudanca futura no `*` apareca aqui em vez de passar calada.
ok('partes grudadas casam, e isso e o mecanismo do "HT1300" (nao e defeito novo)',
   coletor.token_no_titulo('classic 600 2217', 'Eheim Classic 6002217 bivolt') is True)
ok('e e o mesmo mecanismo que faz o varejo escrever HT1300',
   coletor.token_no_titulo('ht-1300', 'Aquecedor Roxin HT1300 300w') is True)

# E A CLASSE DE SEPARADORES NAO PODE ENGOLIR LETRA NEM DIGITO. Esta afirmacao
# nao olha exemplo nenhum: olha a propria classe. Um dia alguem acrescenta um
# caractere a ela para destravar um anuncio, e se aquele caractere for `\w` o
# codigo passa a casar com qualquer coisa — e nenhum dos exemplos acima
# reprovaria, porque eles nao usam letra como separador.
import re as _re
for _proibido in 'abz09':
    ok('o separador nao aceita %r' % _proibido,
       _re.fullmatch(coletor.SEPARADOR, _proibido) is None,
       'SEPARADOR=%r aceita %r' % (coletor.SEPARADOR, _proibido))

print('\n%d afirmacoes, %d falha(s)' % (afirmacoes, len(falhas)))
if falhas:
    for f in falhas:
        print('  FALHOU: %s' % f)
sys.exit(1 if falhas else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA QUE DECIDE SE UM ANUNCIO SERVE A UMA CONSULTA DE PRODUTO (secao 30.2).

    python3 ferramentas/relevancia-do-anuncio.py --autoteste

POR QUE ELA EXISTE SEPARADA DO CASAMENTO DE OFERTA
--------------------------------------------------
Esta ilha ja tem `coletar-oferta.py`, que parte de um REGISTRO do banco e
procura o anuncio DAQUELE produto — marca e modelo batendo, as seis travas da
25.7. A pergunta dele e "onde se compra o Honeywhale M2 MAX".

Esta regua responde outra: "o que aparece quando a pessoa digita `patinete
eletrico`, e qual daquilo e o produto que esta pagina promete". Ela nao sabe de
marca nenhuma. As duas convivem porque a 30.2 abriu um portao que a 25.1 nao
abria: dado COMERCIAL de anuncio (titulo, preco, foto) vale para a pagina de
consulta de produto, e ali o anuncio nao precisa casar com registro nenhum.

O ACHADO QUE ESTA REGUA EXISTE PARA NAO DEIXAR PASSAR (29/10/2026)
------------------------------------------------------------------
Medido na Open API nas seis cabecas do dossie, 20 ofertas cada: a consulta
`patinete eletrico` devolve, nas 20 primeiras, ZERO patinete de adulto. O que
ela serve e `Patinete Eletrico Infantil 150W Rodas 6 Polegadas UNITOYS` e
`Moto Eletrica Infantil 6V`. `moto eletrica` devolve 20 de 20 entre brinquedo
infantil e peca de caminhao. `bicicleta eletrica` e `bike eletrica` devolvem
camara de ar, pneu, compressor e moto infantil.

**A palavra que a pessoa digita no Google e a palavra que acha o produto na
loja NAO sao a mesma, e neste nicho elas divergem por um qualificador:
`adulto`.** Com ele, `patinete eletrico adulto` devolve 12 patinetes de adulto
entre R$ 1.297 e R$ 3.399, e `bicicleta eletrica adulto` devolve 5 e-bikes, tres
delas com 74, 28 e 25 vendas.

Por isso a exigencia desta ilha e POSITIVA e nao negativa: o anuncio tem de
DECLARAR `adulto` no titulo. A secao 8 do contrato chama de adivinhacao
perdoar por presenca de palavra ("perdoar por presenca de palavra e adivinhar"),
e o avesso vale igual — recusar por presenca de `infantil` deixaria passar
`Patinete Eletrico 800W Pico 1000W Off-Road`, que nao diz nem uma coisa nem
outra, e barraria `Patinete Eletrico Dobravel 350W Adulto | infantil`, que e
produto de adulto anunciado tambem para filho. **Exigir a declaracao erra para
o lado de nao publicar, que e o lado barato da assimetria da 30.8.**

COMO SE LE O VEREDITO
---------------------
`serve=True` exige, nesta ordem e todas:
  1. toda palavra de `exige_todas` presente no titulo (a familia do produto e a
     palavra `eletric`, que separa o patinete eletrico do patinete de empurrar);
  2. ao menos uma palavra de `exige_alguma` presente (o qualificador `adulto`);
  3. nenhuma recusa disparada.

`recusado_por` nomeia a recusa com o NOME dela — `brinquedo`, `acessorio`,
`outro_veiculo`, `kit_multiplo`, `fora_da_familia`, `sem_qualificador` — e
`exigencia_que_faltou` guarda a palavra exata. A 30.2 manda a pagina dizer o que
o anuncio nao declara em vez de preencher coluna com palavra tirada do titulo, e
e com estes dois campos que ela diz.

AS LISTAS NASCERAM DE TITULOS REAIS DESTA COLETA, e cada grupo traz, no
comentario, o titulo que o fez existir. Lista escrita de cabeca envelhece
calada; lista com o titulo ao lado se audita.
"""
import argparse
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# AS RECUSAS. Cada grupo traz o titulo REAL que o fez nascer, medido em
# 29/10/2026 na Open API de afiliados da Shopee.
# ---------------------------------------------------------------------------
RECUSAS = (
    ('outro_veiculo', (
        'quadriciclo', 'triciclo', 'hoverboard', 'kart', 'skate', 'patins',
        'cadeira de rodas', 'drift', 'carrinho', 'caminhao', 'scania',
    )),
    # "Capacete Coquinho Couro Moto Eletrica Scooter Patinete Eletrico Chopper"
    # "Capa de Chuva Longa Adulto Impermeavel para Scooter Eletrico e Bicicleta"
    # "Camara De Ar Fat Bike Aro 20x4.00 Valvula Americana 40mm Bike Eletrica"
    # "Assento De Plastico Para Kart Hoverboard Acessorio Adultos Criancas Scooter"
    #
    # ESTE GRUPO E O UNICO QUE SE MEDE POR POSICAO (ver `POR_POSICAO` abaixo), e
    # a razao e uma medicao: na primeira passada com rede, em 29/10/2026, ele
    # recusou QUATRO patinetes de adulto certos — `Patinete Eletrico 800W Pico
    # 1000W ... Pneu 10" Off-Road` (por `pneu`), `Patinete Eletrico Dobravel
    # Adulto com Assento Controle Bluetooth` (por `assento`), `VYRON Patinete
    # Eletrico Adulto Dobravel Pro Premium ... Amortecedor` (por `amortecedor`) e
    # outro por `pneu`. **O titulo de um veiculo nomeia as pecas DELE.** E o
    # absurdo que fechou a conta: `Bicicleta Eletrica Dobravel Adulto com Pneus A
    # Vacuo` PASSOU, porque `pneus` no plural nao casa com `pneu` entre bordas —
    # duas paginas certas, uma recusada e uma aprovada, pela letra `s`.
    ('acessorio', (
        'capacete', 'capa de chuva', 'pelicula', 'buzina', 'apoio', 'pedaleira',
        'pedal pes', 'assento', 'banco com encosto', 'camara de ar', 'camara',
        'pneu', 'pneus', 'aro 20', 'aro 4', 'garfo', 'quadro p/', 'corrente',
        'compressor', 'bomba', 'calibrador', 'abracadeira', 'carregador',
        'espelho', 'alarme', 'cadeado', 'esteque', 'laco para', 'viseira',
        'soquete', 'rele', 'amortecedor', 'haste frontal', 'descanso',
        'protetores de ouvido', 'chifre', 'suporte',
    )),
    ('kit_multiplo', (
        'kit 2', 'kit com 2', '2 unidades', 'par de', 'kit 5',
    )),
    # "Mini Moto Eletrica Esportiva Vermelha Alta Performance Criancas Adultos"
    # — este titulo declara `Adultos` e e brinquedo, e e por ele que este grupo
    # existe: ele e a UNICA recusa de publico que a exigencia positiva de
    # `adulto` nao resolve sozinha.
    #
    # A PALAVRA `infantil` SOZINHA NAO ESTA AQUI, e isto e decisao medida. O
    # titulo real `Patinete Eletrico Dobravel 350W Adulto | infantil Ate 30km/h
    # Suspensao Reforcada` e produto de ADULTO que o vendedor tambem oferece
    # para filho — recusa-lo custa um produto certo. Todo brinquedo das 180
    # ofertas medidas em 29/10/2026 carrega outro marcador deste grupo (`6v`,
    # `unitoys`, `mini moto`, `empurrador`, `passeio`) ou simplesmente nao
    # declara `adulto`, e cai na exigencia positiva, que e a trava barata.
    ('brinquedo', (
        'crianca', 'criancas', 'kids', 'bebe', 'motoca', 'unitoys',
        'un toys', 'unotoys', 'empurrador', 'passeio', 'brinquedo', '6v',
        '3 anos', 'coordenacao motora', 'mini moto', 'mini quadriciclo',
    )),
)

# ---------------------------------------------------------------------------
# O QUALIFICADOR DE ADULTO. Mora aqui, numa constante, porque ele e a lição da
# medicao de 29/10 e porque a declaracao de cada consulta o cita por nome em
# vez de repetir a lista.
# ---------------------------------------------------------------------------
QUALIFICADOR_ADULTO = ('adulto', 'adultos')

# ---------------------------------------------------------------------------
# A REGRA DA POSICAO: QUEM NOMEIA PRIMEIRO E O PRODUTO
#
# O anuncio de marketplace nomeia o produto no COMECO do titulo e descreve o
# resto depois. Entao `capa de chuva` em `Capa de Chuva Longa Adulto para
# Scooter Eletrico` esta ANTES do substantivo da familia e e o produto; `pneu`
# em `Patinete Eletrico 800W ... Pneu 10" Off-Road` esta DEPOIS e e uma peca do
# veiculo que esta a venda.
#
# A medida e a posicao do termo contra a posicao do SUBSTANTIVO DO PRODUTO, que
# a familia declara por nome em `substantivo` (`patinete`, `bicicleta`, `moto`,
# `scooter`). Ele e um campo e nao a primeira posicao de uma lista de proposito:
# regra que depende da ORDEM de uma lista se desliga em silencio no dia em que
# alguem reordena a lista por estetica. Quando o substantivo nao e declarado, o
# primeiro de `exige_todas` vale como ele; quando ele nao e achado no titulo, a
# regra da posicao NAO se aplica e o grupo volta a valer por presenca — que e o
# lado barato da assimetria da 30.8.
#
# Ela vale SO para `acessorio`. As outras tres sao por presenca, porque errar
# para o lado de nao publicar e o lado barato da assimetria da 30.8 e porque
# nenhuma delas recusou produto certo na medicao.
POR_POSICAO = ('acessorio',)


def normalizar(texto):
    """Sem acento e em minuscula. Titulo de anuncio vem dos dois jeitos."""
    t = unicodedata.normalize('NFD', (texto or '').lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', t)


# A BUSCA E POR PALAVRA INTEIRA, NUNCA POR PEDACO DE PALAVRA — e isto nao e
# capricho: a primeira versao desta regua recusou
# `Patinete Eletrico Adulto 350W 36V | Dobravel 30km/h` com a causa `infantil`,
# porque a lista do brinquedo tem `6v` (a bateria de 6 volts do brinquedo) e
# `36V` TERMINA em `6v` (a recusa chamava-se `infantil` quando isso aconteceu;
# hoje o grupo se chama `brinquedo`). Recusa por pedaco de palavra e a mesma
# familia do `grep` que atravessa YAML quebrado: ela responde, e a resposta e
# errada.
#
# PREFIXOS DECLARADOS: termo que vale como comeco de palavra, e nao como palavra
# inteira. Sao poucos e estao nomeados um por um, porque prefixo implicito e
# justamente o defeito que a nota acima conta. `eletric` cobre eletrico,
# eletrica, eletricos e eletricas sem precisar das quatro, e `bicicleta` cobre o
# plural do titulo real `Kit 2 Bicicletas Eletricas`.
#
# `moto` NAO e prefixo, e a razao e medida: como prefixo ele casaria com
# `motocicleta`, `motorizado` e `motoca` — tres palavras que aparecem em titulo
# de acessorio e de brinquedo desta coleta. A consulta `motos eletricas para
# adultos` nao tem pagina (ver `dados/consultas-de-produto.json`), entao o
# plural de `moto` nao e cobrado por ninguem hoje; quem for abrir aquela pagina
# declara o plural na propria familia em vez de alargar este prefixo.
PREFIXOS = ('eletric', 'adulto', 'bicicleta', 'patinete')

_CACHE = {}


def _padrao(termo):
    p = _CACHE.get(termo)
    if p is None:
        t = normalizar(termo)
        esq = r'\b' if t[:1].isalnum() else ''
        dir_ = '' if t in PREFIXOS else (r'\b' if t[-1:].isalnum() else '')
        p = _CACHE[termo] = re.compile(esq + re.escape(t) + dir_)

    return p


def _onde(texto_normalizado, termo):
    """Posicao da primeira ocorrencia, ou -1. E a mesma busca do `_contem`."""
    m = _padrao(termo).search(texto_normalizado)

    return m.start() if m else -1


def _contem(texto_normalizado, termo):
    return _onde(texto_normalizado, termo) >= 0


def julgar(titulo, exige_todas, exige_alguma=(), recusas_desligadas=(),
           substantivo=None):
    """Devolve (serve, recusado_por, exigencia_que_faltou, exigencias_atendidas).

    `recusas_desligadas` existe para a consulta cujo produto E o que outra
    recusa: uma pagina de PECA desta ilha vai querer `acessorio` desligada. Ela
    e DECLARADA na consulta, nunca decidida aqui — regua que escolhe sozinha
    qual trava vale e a regua que mede a si mesma.
    """
    t = normalizar(titulo)
    atendidas = []

    for palavra in exige_todas:
        if not _contem(t, palavra):
            return (False, 'fora_da_familia', palavra, atendidas)
        atendidas.append(palavra)

    if exige_alguma:
        achou = next((p for p in exige_alguma if _contem(t, p)), None)
        if not achou:
            return (False, 'sem_qualificador', ' ou '.join(exige_alguma), atendidas)
        atendidas.append(achou)

    onde_o_produto = _onde(t, substantivo or exige_todas[0])

    for nome, palavras in RECUSAS:
        if nome in recusas_desligadas:
            continue
        for palavra in palavras:
            onde = _onde(t, palavra)
            if onde < 0:
                continue
            if nome in POR_POSICAO and 0 <= onde_o_produto < onde:
                continue              # e peca DO veiculo, nao o produto a venda
            return (False, nome, palavra, atendidas)

    return (True, None, None, atendidas)


# ---------------------------------------------------------------------------
# A CONTAGEM DO ROTULO DE POTENCIA — o numero proprio desta ilha
#
# O `VOZ.md` escreve a tese em uma linha: "O numero grande no anuncio as vezes e
# o pico do motor. O que conta para a regra e a potencia nominal". Esta funcao
# conta, nos titulos colhidos, quantos declaram watt e quantos dizem qual dos
# dois watts e aquele. E a mesma distincao que o banco desta ilha guarda em
# `potencia_declarada_sem_rotulo_w`, agora medida na vitrine.
#
# Ela NAO atribui o watt a `potencia_nominal_w` de ninguem: a 10 do contrato e o
# `niveis_minimos_por_campo` do esquema exigem nivel 5 ou melhor nesse campo, e
# titulo de anuncio e nivel 6. O que sai daqui e uma CONTAGEM sobre titulos,
# nunca um dado tecnico atribuido a um veiculo.
# ---------------------------------------------------------------------------
PADRAO_WATT = re.compile(r'(\d{2,5})\s*w\b')
PADRAO_NOMINAL = re.compile(r'\bnominal\b')
PADRAO_PICO = re.compile(r'\bpico\b')


def rotulo_de_potencia(titulo):
    """'sem_watt' | 'watt_sem_rotulo' | 'nominal' | 'pico' | 'os_dois'."""
    t = normalizar(titulo)
    if not PADRAO_WATT.search(t):
        return 'sem_watt'
    nominal = bool(PADRAO_NOMINAL.search(t))
    pico = bool(PADRAO_PICO.search(t))
    if nominal and pico:
        return 'os_dois'
    if nominal:
        return 'nominal'
    if pico:
        return 'pico'
    return 'watt_sem_rotulo'


# ---------------------------------------------------------------------------
# AUTOTESTE — e os casos sao titulos REAIS da medicao de 29/10/2026
# ---------------------------------------------------------------------------
PATINETE = dict(exige_todas=('patinete', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
                substantivo='patinete')
BICICLETA = dict(exige_todas=('bicicleta', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
                 substantivo='bicicleta')
# A familia da `moto eletrica`, que ainda nao tem pagina: ela entra no autoteste
# porque os dois casos de brinquedo que declaram `Adultos` sao motos.
MOTO = dict(exige_todas=('moto', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
            substantivo='moto')

CASOS = (
    # (titulo, familia, serve_esperado, recusa_esperada)
    ('Patinete Elétrico Adulto 350W 36V | Dobrável 30km/h com Bluetooth, LED Alta Potência',
     PATINETE, True, None),
    ('Patinete Elétrico Adulto Dobrável Turbo 550W - 40km/h, 40km Autonomia Portátil',
     PATINETE, True, None),
    # O caso que a prosa do topo cita: adulto E infantil no mesmo titulo. A
    # exigencia POSITIVA o aprova; recusar por presenca de `infantil` o barraria.
    ('Patinete Elétrico Dobrável 350W Adulto | infantil Até 30km/h Suspensão Reforçada',
     PATINETE, True, None),
    # E o avesso dele, tambem real: declara `Adultos` e e brinquedo. Sem o grupo
    # `brinquedo` este passaria, e e a unica razao pela qual o grupo existe.
    ('Mini Moto Elétrica Esportiva Vermelha Alta Performance Crianças Adultos Presente',
     MOTO, False, 'brinquedo'),
    # Brinquedo: nao declara adulto, e a recusa que dispara primeiro e a do
    # qualificador, porque ela e a de ordem 2 e as recusas sao a de ordem 3.
    ('Patinete Elétrico Infantil Laranja Rodas PU 6 Polegadas 150W Dobrável UNITOYS',
     PATINETE, False, 'sem_qualificador'),
    # Patinete de EMPURRAR anunciado para adulto: sem `eletric` no titulo, cai
    # na familia. E a trava que separa o veiculo do brinquedo de rua.
    ('Patinete Scooter Dobrável Capacidade 70kg Jovens Adultos',
     PATINETE, False, 'fora_da_familia'),
    # Acessorio que declara adulto — a recusa de acessorio tem de vencer.
    ('Capa de Chuva Longa Adulto Impermeável para Scooter Elétrico e Bicicleta',
     BICICLETA, False, 'acessorio'),
    ('Capacete Coquinho Couro Moto Elétrica Scooter Patinete Elétrico Chopper Custom',
     PATINETE, False, 'sem_qualificador'),
    # Kit de dois veiculos que declara adulto. Na familia da bicicleta ele cai
    # antes, na familia, porque o titulo nao diz `bicicleta` — e e assim no ar.
    ('Kit 2 Triciclos Elétricos Drift 350W Adulto Infantil 3 Velocidades Motorizado',
     BICICLETA, False, 'fora_da_familia'),
    # E o kit DENTRO da familia, FABRICADO para a trava `kit_multiplo` poder
    # falhar: nenhuma oferta real das 180 medidas em 29/10/2026 era um kit de
    # dois veiculos da mesma familia, e trava que nunca viu o mundo dela nasce
    # errada sem poder falhar (secao 8 do ARQUIPELAGO.md).
    ('Kit 2 Bicicletas Elétricas Dobráveis Adulto Bateria de Lítio',
     BICICLETA, False, 'kit_multiplo'),
    ('Bicicleta elétrica dobrável NIUDA para adultos, ideal para viagens e deslocamento',
     BICICLETA, True, None),
    ('Bicicleta Elétrica Ebike M2 800w Litio 48v 43kmh Scooter eletrica Trabalho adulto',
     BICICLETA, True, None),
    # ESTE CASO E A RAZAO DE `bike` NAO ESTAR EM `exige_todas` DA BICICLETA: o
    # titulo diz `Bike` e nao `Bicicleta`, e quem aceitasse `bike` como
    # substantivo da familia estaria aceitando o vocabulario do acessorio.
    ('Câmara De Ar Fat Bike Aro 20x4.00 Válvula Americana 40mm Bike Elétrica',
     BICICLETA, False, 'fora_da_familia'),
    # OS QUATRO QUE A REGRA DA POSICAO EXISTE PARA NAO RECUSAR. Os quatro sao
    # titulos reais da primeira passada com rede, em 29/10/2026, e os quatro
    # eram patinete ou bicicleta de adulto a venda com a peca DELES no titulo.
    ('Patinete Elétrico 800W Pico 1000W 40km/h Bateria 36V 15Ah Pneu 10” Off-Road '
     'LCD Scooter Dobrável Adulto', PATINETE, True, None),
    ('Patinete Elétrico Dobrável Adulto com Assento Controle Bluetooth Suspensão LED',
     PATINETE, True, None),
    ('VYRON Patinete Elétrico Adulto Dobrável Pro Premium 36V 350W 3 Velocidades Amortecedor',
     PATINETE, True, None),
    ('Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo e Bateria de Lítio',
     BICICLETA, True, None),
    # E O AVESSO, que e o que a regra da posicao NAO pode deixar passar: o
    # acessorio nomeado ANTES do substantivo da familia.
    ('Capacete De Bicicleta Seguro E Confortável Adulto Leve Com Óculos Para '
     'Motocicleta Veículo Elétrico Mountain Bike', BICICLETA, False, 'acessorio'),
    # Este cai em `outro_veiculo` (`kart`) antes de cair em `acessorio`
    # (`assento`), porque aquele grupo vem primeiro e nao e medido por posicao.
    # As duas leituras estao certas e a ordem decide qual a pagina imprime.
    ('Assento De Plástico Para Kart Hoverboard Acessório Adultos Crianças Scooter '
     'Elétrico Auto Balanceamento',
     dict(exige_todas=('scooter', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
          substantivo='scooter'), False, 'outro_veiculo'),
)

CASOS_DE_ROTULO = (
    ('Patinete Elétrico Adulto 350W 36V | Dobrável 30km/h', 'watt_sem_rotulo'),
    ('Patinete Elétrico 800W Pico 1000W 40km/h Bateria 36V 15Ah Pneu 10" Off-Road', 'pico'),
    ('Patinete Elétrico Adulto Dobrável 30km/h Original Premium', 'sem_watt'),
    ('Scooter com 500 W nominal e 1000 W de pico', 'os_dois'),
    ('Motor de 500 W nominal declarado pela ficha', 'nominal'),
)


def autoteste():
    falhas = []
    for titulo, familia, esperado, recusa in CASOS:
        serve, por, _, _ = julgar(titulo, **familia)
        if serve is not esperado or por != recusa:
            falhas.append('FALHOU: %r -> serve=%s recusado_por=%s (esperava %s/%s)'
                          % (titulo[:60], serve, por, esperado, recusa))
    for titulo, esperado in CASOS_DE_ROTULO:
        obtido = rotulo_de_potencia(titulo)
        if obtido != esperado:
            falhas.append('FALHOU rotulo: %r -> %s (esperava %s)'
                          % (titulo[:60], obtido, esperado))

    # A trava da propria trava: recusa DESLIGADA tem de deixar passar.
    serve, por, _, _ = julgar(
        'Pneu Bike Bicicleta Elétrica Scooter 14x2.50 para adulto',
        exige_todas=('pneu', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
        substantivo='pneu', recusas_desligadas=('acessorio',))
    if not serve:
        falhas.append('FALHOU: recusa desligada nao deixou passar (recusado_por=%s)' % por)

    for f in falhas:
        print(f)
    total = len(CASOS) + len(CASOS_DE_ROTULO) + 1
    print('\n%d caso(s), %d falha(s).' % (total, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--autoteste', action='store_true')
    a = p.parse_args()
    if not a.autoteste:
        p.error('esta regua e uma biblioteca: rode --autoteste')
    sys.exit(autoteste())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA QUE DECIDE SE UM ANUNCIO SERVE A UMA CONSULTA DE PRODUTO (secao 30.2).

    python3 ferramentas/teste-relevancia-do-anuncio.py

O NOME COMECA COM `teste-` E ISSO NAO E ENFEITE: `bancada.py` desta ilha varre
`ferramentas/` e classifica pela convencao do nome, e arquivo que nao casa com
nenhuma e DENUNCIADO. Esta regua nasceu chamada `relevancia-do-anuncio.py` e a
bancada a denunciou na primeira passada, com a frase certa: "ou ele e portao e
precisa do prefixo, ou nao e e precisa estar fora de ferramentas/ — silencio
aqui e portao que nunca roda". Ela e as duas coisas — biblioteca que o coletor
importa e bateria que se mede sozinha —, entao ela entra na bancada pelo nome e
roda a bateria quando chamada sem argumento.

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
    # `1 peca` ENTROU EM 03/11/2026, E ELE E A SEGUNDA METADE DO MESMO TITULO
    # REAL QUE TROUXE A BORDA DA DIREITA (ver a nota em `_borda_direita`):
    #
    #   "1 Peca Certificado 3C ... Bicicleta Eletrica Motocicleta Meio Capacete1"
    #
    # Consertada a borda, este titulo AINDA passava — e por um segundo buraco,
    # independente: `capacete1` esta no FIM, DEPOIS de `bicicleta`, e a regra de
    # POSICAO abaixo le isso como "e peca DO veiculo" e pula a recusa. A regra de
    # posicao esta certa para o titulo que ela nasceu medindo (o veiculo que
    # nomeia as pecas DELE: `Patinete Eletrico 800W ... Pneu 10" Off-Road`) e
    # cega para a forma INVERSA, que e a forma mais comum de titulo de acessorio:
    # listar primeiro os veiculos COMPATIVEIS e nomear o produto por ultimo.
    #
    # `1 peca` fura os dois porque esta na POSICAO 0 — antes do substantivo da
    # familia —, e porque a afirmacao que ele carrega e verdadeira no nicho e
    # facil de conferir: **ninguem vende bicicleta, patinete ou moto eletrica
    # como "1 Peca".** Quem anuncia "1 Peca" esta vendendo uma peca. E a irma
    # singular do grupo `kit_multiplo` (`2 unidades`, `par de`), e mora aqui e
    # nao la porque o que ela decide nao e quantidade: e O QUE o anuncio e.
    ('acessorio', (
        '1 peca',
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

# A BORDA DA DIREITA NAO E A MESMA DA ESQUERDA, E A ASSIMETRIA E MEDIDA
# (03/11/2026)
# ---------------------------------------------------------------------------
# Medido na coleta das 16h5xZ de 03/11/2026, na consulta `bicicleta eletrica`:
# o titulo real
#
#   "1 Peca Certificado 3C Masculino E Feminino Adulto Desenho Animado
#    Bicicleta Eletrica Motocicleta Meio Capacete1"
#
# PASSOU a regua, e com R$ 113,34 ele seria o PISO da faixa de preco da pagina
# `/veiculos/bicicleta-eletrica/` — o numero PROPRIO da ilha, servido na
# primeira tela sob a frase "Preco mediano hoje". Um capacete publicado como
# bicicleta, com botao de afiliado ao lado.
#
# A CAUSA: a recusa `capacete` nao casou porque o vendedor escreveu
# `Capacete1`, com o digito COLADO. `\b` e borda entre caractere de palavra e
# nao-palavra, e `1` E caractere de palavra — entao nao ha borda, e a regua
# recusou DEZ capacetes pela palavra e deixou passar o DECIMO PRIMEIRO pelo
# digito. Mesma familia do `git log` raso da 1.1 e do numero de tela digitado:
# o instrumento responde, e a resposta sai curta com cara de completa.
#
# E A CORRECAO NAO PODE SER "casar por pedaco de palavra", porque a nota de cima
# conta o que isso custou (`36V` recusado por `6v`). Entao as duas bordas deixam
# de ser a mesma coisa, cada uma pelo que ela PROTEGE:
#
#   - a da ESQUERDA segue `\b`, estrita. E ela que impede `6v` de casar `36V`:
#     o digito ANTES do termo e justamente o caso medido, e afrouxa-la aqui
#     reabriria o defeito de 29/10 pelo qual esta regua tem bordas.
#   - a da DIREITA, para termo que termina em LETRA, passa a ser "nao seguido de
#     LETRA" (`(?![a-z])`). Digito colado no fim nao faz outra palavra —
#     `capacete1` e `capacete` com a enumeracao do vendedor —, mas letra colada
#     FAZ, e e por isso que `moto` continua nao casando `motocicleta` e
#     `pneu` continua nao casando `pneus` (os dois estao na lista, pelo motivo
#     escrito la).
#   - a da DIREITA, para termo que termina em DIGITO, segue `\b`: `aro 20` nao
#     pode casar `aro 200`, e ali o digito seguinte MUDA a medida.
#
# `normalizar` tira acento e baixa a caixa antes disto, entao `[a-z]` alcanca o
# alfabeto inteiro que chega aqui.
_CACHE = {}


def _borda_direita(t):
    if t in PREFIXOS:
        return ''
    if t[-1:].isdigit():
        return r'\b'              # `aro 20` nao casa `aro 200`
    if t[-1:].isalpha():
        return r'(?![a-z])'       # `capacete` casa `capacete1`, nao casa `capacetear`

    return ''


def _padrao(termo):
    p = _CACHE.get(termo)
    if p is None:
        t = normalizar(termo)
        esq = r'\b' if t[:1].isalnum() else ''
        p = _CACHE[termo] = re.compile(esq + re.escape(t) + _borda_direita(t))

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
# A CARGA QUE O ANUNCIO DECLARA — o terceiro numero da ilha, lido do titulo
#
# O `PROMPT.md` desta ilha diz que o nicho e "acertar os TRES numeros antes de
# comprar": potencia e velocidade (a F1), bateria (a F2) e CARGA MAXIMA (a F3).
# A F3 nao vai ao ar: `carga_max_kg` esta declarado em TRES registros do banco e
# os tres sao `rascunho` — a escada de compra inteira devolveu zero oferta nos
# tres, remedido em 03/11/2026. Entao a pergunta "aguenta o meu peso?" nao tinha
# NENHUMA resposta no site, e tinha dado para responder: o titulo do anuncio.
#
# O DEFEITO MEDIDO QUE FEZ ESTA FUNCAO NASCER (03/11/2026, no ar):
# `/veiculos/patinete-eletrico/` servia, na dobra "Qual escolher", a frase
# declarada *"a carga maxima declarada e o primeiro filtro, e ela QUASE NUNCA
# ESTA NO TITULO"* — e naquele instante SEIS dos DEZESSEIS anuncios publicados
# naquela pagina a declaravam no titulo, de 60 a 150 kg. Prosa escrita a mao
# afirmando o estado do catalogo: a cicatriz que o `REGISTRO.md` de 29/10 ja
# tinha nomeado nesta ilha com estas palavras — **prosa que afirma o estado do
# banco e numero digitado em outro traje**. A frase saiu e virou contagem.
#
# ELA NAO ATRIBUI `carga_max_kg` A NINGUEM, pelo mesmo motivo que
# `rotulo_de_potencia` nao atribui watt: titulo de anuncio e nivel 6 e o
# `niveis_minimos_por_campo` do esquema exige melhor nesse campo. O que sai daqui
# e uma CONTAGEM sobre titulos e uma FAIXA do que os vendedores declaram.
#
# A LIGACAO E OBRIGATORIA, E ISSO E A REGRA INTEIRA. `kg` solto no titulo e
# AMBIGUO entre a carga que o veiculo aguenta e o peso do PROPRIO veiculo — e as
# duas aparecem em titulo de patinete ("dobravel 12kg" e "ate 120kg"). Ler kg
# solto como carga maxima publicaria o peso do aparelho como se fosse o limite
# de quem sobe nele, numa pagina que diz "passar da carga maxima deixa a solda do
# guidao mais perto de ceder". Entao o numero so e lido quando uma palavra de
# CAPACIDADE o liga: `capacidade`, `suporta`, `suporte`, `aguenta`, `carga`,
# `peso maximo`, `maximo`, `max`, `ate`.
# O CASO REAL QUE A REGRA DEIXA DE FORA DE PROPOSITO, e ele estava na coleta de
# hoje: `patinete eletrico 350w 10ah 120kg autonomia 30km dobravel` — `120kg`
# solto, entre a amperagem e a autonomia. Quase certamente e carga, e "quase
# certamente" nao e procedencia (secao 8). Ele entra na contagem como NAO
# DECLARADO, e a pagina nao perde nada: ele continua nomeado na tabela.
#
# AS BORDAS SAO ASSIMETRICAS, CADA UMA PELO QUE PROTEGE — a licao de 03/11 desta
# mesma regua, onde `\b` depois de LETRA deixou passar `Capacete1`:
#   - a da ESQUERDA, na palavra que liga, e `\b` estrita: `ate` nao pode casar
#     dentro de outra palavra.
#   - a da DIREITA, depois de `kg`, e `(?![a-z])`, e NAO `(?![a-z0-9])`: ela
#     barra `90kgf` (kgf e forca, nao massa) e DEIXA PASSAR `150kg1`, a
#     enumeracao do vendedor. A primeira versao desta linha escreveu
#     `(?![a-z0-9])` e o caso do `150kg1` do autoteste a REPROVOU na primeira
#     passada — o mesmo buraco que o `Capacete1` abriu hoje nesta regua, do
#     outro lado. A diferenca com `aro 20`/`aro 200` da regua de recusa e que
#     la o digito vem DENTRO da medida e a MUDA; aqui ele vem depois da UNIDADE
#     e nao pode mudar nada.
# ---------------------------------------------------------------------------
PALAVRAS_DE_CAPACIDADE = ('capacidade', 'suporta', 'suporte', 'aguenta',
                          'carga', 'peso maximo', 'maximo', 'max', 'ate')

# Entre a palavra que liga e o numero cabe pouco: `suporta ate 150kg` tem 4
# caracteres no meio, `capacidade de carga 120kg` tem 10. O teto de 14 e o que
# separa a ligacao de uma coincidencia a meia frase de distancia, e ele esta
# medido contra os titulos reais da coleta nos casos do autoteste.
PADRAO_CARGA = re.compile(
    r'\b(?:' + '|'.join(p.replace(' ', r'\s+') for p in PALAVRAS_DE_CAPACIDADE)
    + r')[^0-9]{0,14}(\d{2,3})\s*(?:kg|quilos?)(?![a-z])')

PADRAO_KG_SOLTO = re.compile(r'(\d{2,3})\s*(?:kg|quilos?)(?![a-z])')


def carga_declarada(titulo):
    """(valor_kg, declarado_como) ou (None, motivo). Nunca atribui campo tecnico.

    `declarado_como` e o PEDACO DO TITULO que sustenta o numero, nao uma frase
    nossa: procedencia que se confere abrindo o anuncio.
    """
    t = normalizar(titulo)
    m = PADRAO_CARGA.search(t)
    if m:
        return (int(m.group(1)), m.group(0).strip())
    solto = PADRAO_KG_SOLTO.search(t)
    if solto:
        return (None, 'tem %r no titulo e nenhuma palavra de capacidade o liga: '
                      'kg solto e ambiguo entre a carga que o veiculo aguenta e o '
                      'peso do proprio veiculo' % solto.group(0).strip())

    return (None, 'o titulo nao declara nenhum kg')


# ---------------------------------------------------------------------------
# O PIVO DA F1 LIDO DO TITULO — e a leitura mais ASSIMETRICA desta ilha
#
# Nasceu de um defeito MEDIDO NO AR em 04/11/2026: a camada declarada de
# `/veiculos/bicicleta-eletrica/` servia, escrito a mao, *"quase toda a faixa de
# baixo e dobravel, de PEDAL ASSISTIDO (...); o topo da faixa e a que tem
# ACELERADOR e motor forte"*. Naquele instante, dos SEIS anuncios que aquela
# pagina publica, ZERO declarava acelerador e ZERO declarava nao ter um.
#
# E ISTO NAO E "numero velho na prosa": e a prosa afirmando o PIVO. A seção 3 da
# `dados/especificacao-calculadoras.md` e literal — *"o enum de `acelerador` e
# pivo da F1, entao ele NAO aceita nulo silencioso: ficha sem a informacao grava
# `nao_declarado` (...) e NUNCA cai no lado 'so pedal assistido' por omissao"*. A
# camada declarada fazia em PROSA exatamente o que o esquema proibe no BANCO, e
# na metade que decide se a pessoa precisa de habilitacao.
#
# A REGRA, e ela e assimetrica DE PROPOSITO, cada lado pelo que ele afirma:
#
#   - `manual` (TEM acelerador): a palavra no titulo basta. Quem escreve
#     "acelerador" esta vendendo o acelerador; ninguem o anuncia por engano.
#   - `so_pedal_assistido`: a palavra "pedal assistido" NAO basta, e e aqui que
#     esta o buraco que ninguem via. Ter pedal nao exclui ter acelerador — a
#     maioria das bicicletas eletricas tem os dois. So declara este lado o
#     titulo que NEGA o acelerador ("sem acelerador", "somente pedal assistido",
#     "apenas pedal assistido"). E a regra do esquema aplicada a camada do
#     titulo: nunca por omissao.
#   - `pedal tripulado`, que esta em DOIS titulos reais desta coleta, nao declara
#     nada: e traducao de maquina de "pedal assisted", e atribuir sentido a uma
#     frase truncada e a familia do `kg` solto — "quase certamente" nao e
#     procedencia.
#
# O que sai daqui e CONTAGEM, nunca campo tecnico: titulo e nivel 6, e
# `niveis_minimos_por_campo` exige melhor para `acelerador`.
# ---------------------------------------------------------------------------
NEGA_O_ACELERADOR = ('sem acelerador', 'somente pedal assistido',
                     'apenas pedal assistido', 'so pedal assistido',
                     'sem manopla de aceleracao')

TEM_ACELERADOR = ('acelerador', 'aceleracao', 'throttle')


def declaracao_do_pivo(titulo):
    """(lado, pedaco_do_titulo) ou (None, motivo). Nunca atribui `acelerador`.

    `lado` e 'manual' ou 'so_pedal_assistido'. O pedaco do titulo e a
    procedencia — se confere abrindo o anuncio, e nao e uma frase nossa.
    """
    t = normalizar(titulo)
    # A NEGACAO VEM PRIMEIRO: "somente pedal assistido, sem acelerador" tem a
    # palavra `acelerador` dentro dela, e ler a ordem inversa classificaria como
    # `manual` o titulo que diz o contrario.
    for termo in NEGA_O_ACELERADOR:
        i = _onde(t, termo)
        if i >= 0:
            return ('so_pedal_assistido', t[i:i + len(normalizar(termo))])
    for termo in TEM_ACELERADOR:
        i = _onde(t, termo)
        if i >= 0:
            return ('manual', t[i:i + len(normalizar(termo))])
    if _contem(t, 'pedal assistido') or _contem(t, 'pedal tripulado'):
        return (None, 'fala de pedal e nao diz se tem acelerador: ter pedal nao '
                      'exclui ter acelerador, e e o acelerador que decide a categoria')

    return (None, 'o titulo nao diz se tem acelerador')


def contagem_do_pivo(anuncios_que_servem):
    """(declaram, com_acelerador, so_pedal) sobre os titulos que a pagina publica."""
    com, so = 0, 0
    for a in anuncios_que_servem:
        lado = declaracao_do_pivo(a['titulo'])[0]
        if lado == 'manual':
            com += 1
        elif lado == 'so_pedal_assistido':
            so += 1

    return (com + so, com, so)


# ---------------------------------------------------------------------------
# O DOBRAVEL, e ele esta aqui porque a frase falsa de 04/11 tinha DUAS metades:
# a do pivo (acima, grave) e a do dobravel (contavel e nao contada). A palavra
# esta no titulo ou nao esta — e esta e a leitura mais simples desta regua, com
# a MESMA borda assimetrica das outras: `dobravel` casa `dobravel1` e nao casa
# `dobravelmente`.
# ---------------------------------------------------------------------------
DOBRAVEL = ('dobravel', 'dobraveis', 'plegable')


def declara_dobravel(titulo):
    t = normalizar(titulo)
    for termo in DOBRAVEL:
        i = _onde(t, termo)
        if i >= 0:
            return (True, t[i:i + len(termo)])

    return (False, 'o titulo nao diz dobravel')


def contagem_do_dobravel(anuncios_que_servem):
    return sum(1 for a in anuncios_que_servem if declara_dobravel(a['titulo'])[0])


# ---------------------------------------------------------------------------
# O PAR DE ENTRADA DA F2 — TENSAO E AMPERAGEM, LIDOS DO TITULO (04/11/2026)
#
# POR QUE ESTA REGUA NASCEU, e a causa esta no AR: a camada declarada de
# `/veiculos/bicicleta-eletrica/` mandava a pessoa "olhar a tensao e a
# amperagem" e emendava, escrito a mao, que bateria pequena em cidade de ladeira
# "e a RECLAMACAO MAIS COMUM de quem compra sem fazer essa conta". Esta ilha
# nunca mediu reclamacao nenhuma: a frase era um RANQUEAMENTO inventado, servido
# o dia inteiro ao lado de uma instrucao correta.
#
# E O NUMERO QUE ELA DEVIA DIZER ESTAVA A UM `grep` DE DISTANCIA: dos 22
# anuncios que esta ilha publica, ZERO declara os dois no titulo — 1 de 6 e 1 de
# 16 declaram so a TENSAO, e nenhum declara a amperagem. A pagina manda usar uma
# calculadora cujas duas entradas a propria vitrine nao entrega, e e a tese da
# ilha outra vez: "todos falam, ninguem calcula".
#
# A LEITURA E DE UNIDADE E NUNCA DE NUMERO SOLTO: `48v` e tensao, `10ah` e
# amperagem, e `350W 36V` tem as duas unidades no mesmo titulo sem uma vir da
# outra. A borda e a mesma assimetria das outras reguas deste arquivo: digito
# colado a esquerda DERROTA (`1048v` nao e tensao), letra colada a direita
# DERROTA (`48va` nao e), e digito colado a direita idem.
TENSAO = re.compile(r'(?<![0-9a-z])(\d{2,3})\s?v(?![0-9a-z])')
AMPERAGEM = re.compile(r'(?<![0-9a-z])(\d{1,3}(?:[.,]\d)?)\s?ah(?![0-9a-z])')


def declaracao_do_par_da_f2(titulo):
    """(tem_tensao, tem_amperagem, pedaco_ou_motivo) sobre o TITULO.

    O pedaco e a procedencia: confere abrindo o anuncio, e nao e frase nossa.
    """
    t = normalizar(titulo)
    mv, ma = TENSAO.search(t), AMPERAGEM.search(t)
    if mv and ma:
        return (True, True, '%s + %s' % (mv.group(0).strip(), ma.group(0).strip()))
    if mv:
        return (True, False, mv.group(0).strip() + ' (sem amperagem)')
    if ma:
        return (False, True, ma.group(0).strip() + ' (sem tensao)')

    return (False, False, 'o titulo nao declara tensao nem amperagem')


def contagem_do_par_da_f2(anuncios_que_servem):
    """(os_dois, so_tensao, so_amperagem) sobre os titulos que a pagina publica."""
    dois = so_v = so_ah = 0
    for a in anuncios_que_servem:
        v, ah, _ = declaracao_do_par_da_f2(a['titulo'])
        if v and ah:
            dois += 1
        elif v:
            so_v += 1
        elif ah:
            so_ah += 1

    return (dois, so_v, so_ah)


def faixa_de_carga(anuncios_que_servem):
    """(quantos_declaram, menor, maior) sobre os titulos que a pagina publica."""
    valores = sorted(v for v in (carga_declarada(a['titulo'])[0]
                                 for a in anuncios_que_servem)
                     if v is not None)
    if not valores:
        return (0, None, None)

    return (len(valores), valores[0], valores[-1])


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
    # O TITULO REAL DE 03/11/2026, medido na Open API na consulta
    # `bicicleta eletrica adulto`, a R$ 113,34 e com `serve: True` na regua de
    # ontem. Ele e UM caso e DOIS defeitos somados, e por isso esta aqui inteiro:
    # o digito colado em `Capacete1` furou a borda da direita, e a posicao do
    # `capacete` DEPOIS de `bicicleta` furou a regra de POSICAO. A recusa que
    # vence hoje e `1 peca`, que esta na posicao 0.
    ('1 Peça Certificado 3C Masculino E Feminino Adulto Desenho Animado '
     'Bicicleta Elétrica Motocicleta Meio Capacete1',
     BICICLETA, False, 'acessorio'),
    # E A METADE DA BORDA, SOZINHA, EM MUNDO FABRICADO — porque o titulo real
    # acima e recusado por `1 peca` e NAO exerce a borda da direita: com ela
    # quebrada ele continuaria sendo recusado, e a correcao da borda passaria
    # por conferida sem nunca ter sido medida. Aqui o `Capacete1` esta ANTES do
    # substantivo da familia (logo a regra de posicao nao o pula) e nao ha
    # `1 peca` para salvar o veredito: se `(?![a-z])` voltar a ser `\b`, este
    # caso PASSA e a bateria reprova. E a regra da secao 8 — trava que nunca viu
    # o mundo dela nasce errada sem poder falhar.
    ('Capacete1 Meio Casco Adulto para Bicicleta Elétrica e Motocicleta',
     BICICLETA, False, 'acessorio'),
    # O avesso dela, para a borda nao virar pedaco de palavra: `capacetear` nao
    # e capacete, e letra colada tem de continuar barrando a recusa.
    ('Bicicleta Elétrica Dobrável Adulto Capaceteria Lítio 350W',
     BICICLETA, True, None),
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


# OS CASOS DA CARGA SAO TITULOS REAIS DA COLETA DE 03/11/2026, e os tres que
# NAO declaram estao aqui pelo mesmo motivo que os que declaram: a regra que
# nunca viu o mundo em que ela tem de se calar nasce errada sem poder falhar.
CASOS_DE_CARGA = (
    ('Patinete Elétrico Scooter 350W 10" com Amortecedor e App GPS Dobrável Super '
     'Autonomia Para Adultos Até 150kg', 150),
    ('Patinete Elétrico Scooter Adulto 150w Dobrável Até 60kg Preto', 60),
    ('Patinete Scooter Dobrável Capacidade 70kg Jovens Adultos', 70),
    ('Patinete Elétrico Dobrável 350W Adulto | infantil Até 30km/h Suspensão '
     'Reforçada Suporta 100kg', 100),
    ('Patinete Elétrico Adulto,potência 500w Até 140kg Dobrável E Patinete', 140),
    # KG SOLTO: a carga quase certamente e esta, e "quase certamente" nao e
    # procedencia. Este titulo e real e esta na coleta de hoje.
    ('Patinete Elétrico 350w 10ah 120kg Autonomia 30km Dobravel Preto', None),
    # O PESO DO PROPRIO APARELHO, que e a razao de a ligacao ser obrigatoria.
    ('Patinete Elétrico Adulto Dobrável Leve 12kg Para Levar no Ônibus', None),
    ('Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo e Bateria de Lítio', None),
    # A BORDA DA DIREITA, pela licao do `Capacete1` desta mesma regua: digito
    # colado no fim nao pode derrotar a leitura, e `kgf` nao e `kg`.
    ('Patinete Elétrico Adulto Suporta 150kg1 Dobrável', 150),
    ('Patinete Elétrico Adulto Torque Máximo 90kgf Dobrável', None),
    # A BORDA DA ESQUERDA: `ate` dentro de outra palavra nao liga nada. Sem o
    # `\\b`, o `ate` de `Matelado` ligaria os 95kg do estofamento.
    ('Patinete Elétrico Adulto Assento Matelado 95kg de Espuma', None),
)


# OS CASOS DO PIVO. Os quatro primeiros sao titulos REAIS da coleta de
# 03-04/11/2026 e os quatro devolvem None — que e o achado, nao a lacuna: as 22
# ofertas que esta ilha publica nao declaram o pivo da F1 em nenhum titulo. Os
# fabricados estao aqui porque regra que nunca viu o mundo dela nasce errada sem
# poder falhar (secao 8), e o terceiro fabricado e o que separa esta regua de uma
# regua ingenua: "pedal assistido" NAO declara o lado do pedal.
CASOS_DO_PIVO = (
    ('Bicicleta elétrica dobrável para adultos, pedal tripulado, compras ao ar livre', None),
    ('Bicicleta Elétrica Ebike M2 800w Litio 48v 43kmh Scooter eletrica adulto', None),
    ('Patinete Elétrico Adulto 350W 36V | Dobrável 30km/h com Bluetooth', None),
    ('Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo e Bateria de Lítio', None),
    ('Bicicleta Elétrica Adulto com Acelerador e Pedal Assistido 500W', 'manual'),
    ('Bicicleta Elétrica Adulto Somente Pedal Assistido, Sem Acelerador, 350W',
     'so_pedal_assistido'),
    # O CASO QUE A REGUA INGENUA ERRA: pedal declarado e acelerador CALADO. Ter
    # pedal nao exclui ter acelerador, e por omissao nunca se cai neste lado.
    ('Bicicleta Elétrica Adulto com Pedal Assistido 350W Dobrável', None),
    # A ORDEM DA LEITURA: a negacao TEM a palavra `acelerador` dentro dela, e ler
    # `TEM_ACELERADOR` primeiro classificaria como `manual` o titulo que nega.
    ('Bike Elétrica Adulto Sem Acelerador 250W Dobrável', 'so_pedal_assistido'),
    # A BORDA DA DIREITA, pela licao do `Capacete1`: digito colado nao derrota.
    ('Bicicleta Elétrica Adulto com Acelerador1 500W', 'manual'),
    # E A BORDA QUE PROTEGE: `aceleradormente` nao existe, mas `acelerado` sim,
    # e ele nao e `acelerador`.
    ('Bicicleta Elétrica Adulto Carregamento Acelerado 350W', None),
)

# OS CASOS DO DOBRAVEL — os tres primeiros reais, o quarto o mundo que se cala.
CASOS_DO_DOBRAVEL = (
    ('Bicicleta elétrica dobrável NIUDA para adultos, viagens diárias', True),
    ('Patinete Elétrico Scooter Adulto 150w Dobrável Até 60kg Preto', True),
    ('Patinete Elétrico 350w 10ah 120kg Autonomia 30km Dobravel Preto', True),
    ('Bicicleta Elétrica Ebike M2 800w Litio 48v 43kmh Scooter eletrica adulto', False),
    ('Patinete Elétrico Adulto Dobrável1 350W', True),
)


# OS CASOS DO PAR DA F2 — os quatro primeiros sao titulos REAIS desta vitrine
# (medidos em 04/11/2026), e os fabricados existem porque regra que nunca viu o
# mundo dela nasce errada sem poder falhar (secao 8): o mundo "os dois
# declarados" NAO EXISTE em anuncio nenhum que esta ilha publica.
CASOS_DO_PAR_DA_F2 = (
    # (titulo, (tem_tensao, tem_amperagem))
    ('Bicicleta Elétrica Ebike M2 800w Litio 48v 43kmh Scooter eletrica adulto', (True, False)),
    ('Patinete Elétrico Adulto 350W 36V | Dobrável 30km/h com Bluetooth', (True, False)),
    ('Patinete Elétrico 350w 10ah 120kg Autonomia 30km Dobravel Preto', (False, True)),
    ('Bicicleta elétrica dobrável NIUDA para adultos, viagens diárias', (False, False)),
    # O MUNDO QUE A VITRINE NAO TEM: os dois no mesmo titulo.
    ('Scooter Elétrica Adulto 60V 20Ah 1000W Autonomia 60km', (True, True)),
    # A BORDA DA ESQUERDA: digito colado derrota, senao `1048v` viraria 48 V.
    ('Patinete Elétrico Adulto Código 1048v Dobrável', (False, False)),
    # A BORDA DA DIREITA, nas duas unidades.
    ('Bicicleta Elétrica Adulto 48va 350W', (False, False)),
    ('Patinete Elétrico Adulto 10aho 350W', (False, False)),
    # 43kmh NAO e tensao, e `10km` nao e amperagem: a unidade e que manda.
    ('Bicicleta Elétrica Adulto 43kmh 10km Dobrável', (False, False)),
    # Amperagem com decimal, que a Shopee escreve com virgula e com ponto.
    ('Patinete Elétrico Adulto 36V 7,8Ah Dobrável', (True, True)),
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

    for titulo, esperado in CASOS_DE_CARGA:
        valor, porque = carga_declarada(titulo)
        if valor != esperado:
            falhas.append('FALHOU carga: %r -> %s (esperava %s) [%s]'
                          % (titulo[:60], valor, esperado, porque))

    # A FAIXA E CONTADA, NUNCA DIGITADA, e o mundo VAZIO tem de devolver zero
    # sem inventar extremo: e o mundo da pagina da bicicleta eletrica, medido em
    # 03/11/2026 — 0 dos 6 anuncios dela declara kg no titulo.
    quantos, menor, maior = faixa_de_carga(
        [{'titulo': t} for t, _ in CASOS_DE_CARGA])
    if (quantos, menor, maior) != (6, 60, 150):
        falhas.append('FALHOU faixa: (%s, %s, %s), esperava (6, 60, 150)'
                      % (quantos, menor, maior))
    if faixa_de_carga([{'titulo': 'Bicicleta Elétrica Dobrável Adulto'}]) != (0, None, None):
        falhas.append('FALHOU faixa: mundo sem nenhuma carga nao devolveu (0, None, None)')

    for titulo, esperado in CASOS_DO_PIVO:
        lado, porque = declaracao_do_pivo(titulo)
        if lado != esperado:
            falhas.append('FALHOU pivo: %r -> %s (esperava %s) [%s]'
                          % (titulo[:60], lado, esperado, porque))

    for titulo, esperado in CASOS_DO_DOBRAVEL:
        obtido = declara_dobravel(titulo)[0]
        if obtido is not esperado:
            falhas.append('FALHOU dobravel: %r -> %s (esperava %s)'
                          % (titulo[:60], obtido, esperado))

    # A CONTAGEM E CONTADA. O mundo dos casos acima tem 2 `manual` e 2 `so_pedal`;
    # o mundo REAL desta ilha tem (0, 0, 0) nas duas paginas, e so a bateria
    # fabricada prova que a contagem sabe somar.
    obtido = contagem_do_pivo([{'titulo': t} for t, _ in CASOS_DO_PIVO])
    if obtido != (4, 2, 2):
        falhas.append('FALHOU contagem do pivo: %s, esperava (4, 2, 2)' % (obtido,))
    if contagem_do_pivo([{'titulo': 'Bicicleta Elétrica Dobrável Adulto'}]) != (0, 0, 0):
        falhas.append('FALHOU contagem do pivo: mundo calado nao devolveu (0, 0, 0)')
    if contagem_do_dobravel([{'titulo': t} for t, _ in CASOS_DO_DOBRAVEL]) != 4:
        falhas.append('FALHOU contagem do dobravel: esperava 4')

    for titulo, esperado in CASOS_DO_PAR_DA_F2:
        v, ah, porque = declaracao_do_par_da_f2(titulo)
        if (v, ah) != esperado:
            falhas.append('FALHOU par da F2: %r -> (%s, %s) (esperava %s) [%s]'
                          % (titulo[:60], v, ah, esperado, porque))

    # A CONTAGEM E CONTADA. No mundo dos casos acima: 2 com os DOIS, 2 so
    # tensao, 1 so amperagem. O mundo REAL desta ilha e (0, 1, 0) em cada uma
    # das duas paginas, e so a bateria fabricada prova que a contagem soma.
    obtido = contagem_do_par_da_f2([{'titulo': t} for t, _ in CASOS_DO_PAR_DA_F2])
    if obtido != (2, 2, 1):
        falhas.append('FALHOU contagem do par da F2: %s, esperava (2, 2, 1)' % (obtido,))
    if contagem_do_par_da_f2([{'titulo': 'Bicicleta Elétrica Dobrável Adulto'}]) != (0, 0, 0):
        falhas.append('FALHOU contagem do par da F2: mundo calado nao devolveu (0, 0, 0)')

    # A trava da propria trava: recusa DESLIGADA tem de deixar passar.
    serve, por, _, _ = julgar(
        'Pneu Bike Bicicleta Elétrica Scooter 14x2.50 para adulto',
        exige_todas=('pneu', 'eletric'), exige_alguma=QUALIFICADOR_ADULTO,
        substantivo='pneu', recusas_desligadas=('acessorio',))
    if not serve:
        falhas.append('FALHOU: recusa desligada nao deixou passar (recusado_por=%s)' % por)

    for f in falhas:
        print(f)
    total = (len(CASOS) + len(CASOS_DE_ROTULO) + len(CASOS_DE_CARGA)
             + len(CASOS_DO_PIVO) + len(CASOS_DO_DOBRAVEL)
             + len(CASOS_DO_PAR_DA_F2) + 8)
    print('\n%d caso(s), %d falha(s).' % (total, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--autoteste', action='store_true',
                   help='o padrao; fica por compatibilidade com quem o chamava assim')
    p.parse_args()
    sys.exit(autoteste())

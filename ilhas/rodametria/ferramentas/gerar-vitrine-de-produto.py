#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve `dados/vitrine-de-produto.json`, que e o que a TELA das paginas da 30 serve.

    python3 ferramentas/gerar-vitrine-de-produto.py            # mostra o que mudaria
    python3 ferramentas/gerar-vitrine-de-produto.py --gravar
    python3 ferramentas/gerar-vitrine-de-produto.py --conferir  # SEM REDE

AS DUAS METADES, E POR QUE ELAS MORAM EM ARQUIVOS SEPARADOS
-----------------------------------------------------------
`dados/paginas-de-produto.json` e DECLARADO e escrito a mao: titulo,
`description`, a resposta em duas frases, o "qual escolher" e as perguntas. E a
voz do `VOZ.md`, e nela NENHUM numero e digitado — a prosa traz moldes
(`{DE}`, `{ATE}`, `{MEDIANA}`, `{N}`, `{DECLARAM_WATT}`, `{DIZEM_QUAL_WATT}`,
`{DATA}`) e quem os preenche e o PHP, com o numero que sai deste arquivo.

`dados/vitrine-de-produto.json` e GERADO daqui: o cartao de compra, a tabela e
os numeros, RECONTADOS de `dados/anuncios-por-consulta.json`. Preco escrito a
mao na frase e preco que mente na coleta seguinte, calado.

A ORDEM DA VITRINE, E ELA E A DA SECAO 7
----------------------------------------
A secao 7 manda: (1) elegibilidade tecnica completa; (2) adequacao tecnica entre
os elegiveis; (3) e so como DESEMPATE entre itens equivalentes, quem tem link de
loja aparece antes. Nesta pagina NAO existe criterio tecnico que separe os
anuncios: o dado tecnico de anuncio e nivel 6 e o esquema desta ilha exige nivel
5 ou melhor em watt, velocidade, acelerador e carga maxima — nenhum deles entra.
Logo os anuncios sao, para a regra, EQUIVALENTES, e o passo 3 e o unico que
vale. A ordem e por `vendas` (medidas na propria API, com data) e depois por
preco crescente, e a pagina DIZ isso no "como sabemos" em vez de ordenar em
silencio.

`vendas` ordena e NAO vai para a tela. A secao 7 proibe "selo de mais vendido" e
"avaliacao que a ilha nao mediu"; esta ilha mediu as vendas, mas publicar a
contagem ao lado do produto e prova social, e prova social nao e o que esta
pagina vende. O que vai para a tela e o que o anuncio DECLARA e o que ele NAO
declara.

O CARROSSEL LEVA DE 3 A 5, A TABELA LEVA TODOS
----------------------------------------------
A 32.1 (item 5) pede "carrossel horizontal de 3 a 5 cartoes" e a 30.3 pede
"tabela comparando os produtos". Sao duas coisas: o carrossel e a primeira tela
e tem teto, a tabela e a prestacao de contas e nao tem. A 32.5-b mede o primeiro
botao de compra antes de 1.400 px, e carrossel de dezesseis cartoes nao muda esse
numero (ele rola na horizontal) — mas a secao 7 manda nomear TODO item uma vez
em cada resposta, e e a tabela que faz isso.
"""
import argparse
import importlib.util
import json
import json as _json
import os
import re as _re
import unicodedata as _unicodedata
import statistics
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANUNCIOS = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')
EDITORIAL = os.path.join(RAIZ, 'dados', 'paginas-de-produto.json')
VITRINE = os.path.join(RAIZ, 'dados', 'vitrine-de-produto.json')

PISO_DA_30_2 = 3
TETO_DO_CARROSSEL = 5

FERRAMENTAS = os.path.dirname(os.path.abspath(__file__))


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# A REGUA MORA NUM LUGAR SO. O coletor a carrega do mesmo jeito, e e por isso
# que este gerador LE a carga do titulo em vez de a herdar de um campo gravado:
# os anuncios colhidos antes de 03/11/2026 nao tem o campo, e campo ausente lido
# como "nao declara" seria o portao aprovando o que nao mediu. O titulo esta
# gravado; a leitura dele e refeita aqui e refeita no `--conferir`.
rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'teste-relevancia-do-anuncio.py'))


def _textos(valor):
    """Toda string dentro de um valor da camada declarada, em qualquer profundidade.

    Ela e recursiva de proposito: a primeira versao olhava so string e lista de
    string, e as perguntas frequentes sao uma lista de DICIONARIOS — a trava
    passaria por cima de toda pergunta e resposta sem dizer que nao as leu, que
    e a cara do portao que aprova em silencio o que nao mediu (32.5-b).
    """
    if isinstance(valor, str):
        yield valor
    elif isinstance(valor, dict):
        for v in valor.values():
            for t in _textos(v):
                yield t
    elif isinstance(valor, (list, tuple)):
        for v in valor:
            for t in _textos(v):
                yield t


def _sem_acento(texto):
    """Minuscula e sem acento. A trava de quantificador compara assim porque a
    camada declarada escreve `pratica` e `prática` no mesmo arquivo."""
    t = _unicodedata.normalize('NFD', (texto or '').lower())

    return ''.join(c for c in t if _unicodedata.category(c) != 'Mn')


def ler(caminho):
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)


def real(valor):
    """R$ 1.297,13 — o separador do Brasil, feito aqui e nunca no PHP."""
    inteiro, centavos = ('%.2f' % float(valor)).split('.')
    partes = []
    while len(inteiro) > 3:
        partes.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    partes.insert(0, inteiro)

    return 'R$ ' + '.'.join(partes) + ',' + centavos


def data_br(iso):
    a, m, d = (iso or '').split('-')

    return '%s/%s/%s' % (d, m, a)


def o_que_o_anuncio_declara(a):
    """A frase da coluna "o que o anuncio diz", e ela nunca afirma dado tecnico.

    O watt do titulo NAO e atribuido a `potencia_nominal_w` de ninguem: o que a
    pagina diz e que o anuncio declara aquele numero e se ele diz QUAL watt e.
    E a tese do `VOZ.md` em forma de coluna.
    """
    rotulo = a['rotulo_de_potencia']
    if rotulo == 'sem_watt':
        return 'o anúncio não declara potência'
    if rotulo == 'watt_sem_rotulo':
        return 'declara watt, sem dizer se é nominal ou de pico'
    if rotulo == 'pico':
        return 'declara o watt de pico — o nominal, que é o que vale para a regra, não aparece'
    if rotulo == 'nominal':
        return 'declara a potência nominal'

    return 'declara os dois watts, nominal e de pico'


# ---------------------------------------------------------------------------
# A FRASE DO ROTULO DE POTENCIA — contada, nunca digitada
#
# Esta funcao existe por uma cicatriz desta ilha, de HOJE: o `REGISTRO.md` de
# 29/10/2026 as 16h2xZ escreve que a frase de abertura do bloco de compra da F2
# era digitada, dizia "Nenhum destes entrou pela conta de Wh", e teria virado
# mentira calada no dia em que o banco mudasse. A licao esta la com estas
# palavras: **prosa que afirma o estado do banco e numero digitado em outro
# traje.**
#
# A camada declarada NAO pode escrever esta frase, porque ela muda de FORMA e
# nao so de numero: com zero watt declarado, com todos declarados, e com nenhum
# rotulado, as tres pedem frases diferentes, e um molde `{DIZEM_QUAL_WATT}` solto
# produz "sem dizer, em 0 deles, se e o nominal" — portugues que so aparece no
# dia em que a contagem chega em zero.
#
# As cinco formas sao conferidas sobre MUNDOS FABRICADOS em `--conferir`, porque
# o banco de hoje produz uma delas so e regua que nunca viu o mundo dela nasce
# errada sem poder falhar (secao 8).
def frase_do_rotulo(n, declaram_watt, dizem_qual_watt):
    if declaram_watt == 0:
        return ('Nenhum dos %d anúncios declara potência, e é a potência nominal que '
                'decide se precisa de habilitação.' % n)
    if dizem_qual_watt == 0 and declaram_watt == n:
        return ('Todos os %d declaram um watt, e nenhum diz se aquele número é o nominal '
                'ou o de pico — e é o nominal que decide a categoria.' % n)
    if dizem_qual_watt == 0:
        return ('%d dos %d declaram um watt, e nenhum diz se aquele número é o nominal ou '
                'o de pico — e é o nominal que decide a categoria.' % (declaram_watt, n))
    if dizem_qual_watt == declaram_watt:
        return ('Os %d que declaram watt dizem todos qual watt é aquele, o que nesta '
                'família é raro.' % declaram_watt)

    return ('%d dos %d declaram um watt e só %d dizem qual watt é aquele — e é o nominal '
            'que decide a categoria.' % (declaram_watt, n, dizem_qual_watt))


MUNDOS_DO_ROTULO = (
    # (n, declaram, dizem_qual, pedaco que a frase tem de conter)
    (5, 0, 0, 'Nenhum dos 5'),
    (5, 5, 0, 'Todos os 5'),
    (5, 1, 0, '1 dos 5'),
    (5, 3, 3, 'Os 3 que declaram'),
    (16, 15, 1, 'só 1 dizem'),
)


# ---------------------------------------------------------------------------
# A FRASE DA CARGA DECLARADA — contada, nunca digitada, pela MESMA cicatriz
#
# Esta funcao nasceu de um defeito MEDIDO NO AR em 03/11/2026: a dobra "Qual
# escolher" de `/veiculos/patinete-eletrico/` servia, escrito a mao,
# *"a carga maxima declarada e o primeiro filtro, e ela QUASE NUNCA ESTA NO
# TITULO"* — e naquele instante SEIS dos DEZESSEIS anuncios publicados naquela
# pagina a declaravam no titulo. A prosa afirmava o estado do catalogo e estava
# errada; a contagem nao pode estar.
#
# E A FORMA MUDA, nao so o numero — por isso a camada declarada nao pode
# escrever esta frase. Com zero declarando (o mundo da pagina da bicicleta
# eletrica, medido no mesmo dia: 0 de 6), com um so, com todos declarando o
# MESMO valor e com uma faixa de verdade, as quatro pedem portugues diferente, e
# um molde `{CARGA_DE}`/`{CARGA_ATE}` solto produziria "de 60 a 60 kg".
def frase_da_carga(n, declaram, menor, maior):
    if declaram == 0:
        return ('Nenhum dos %d anúncios declara no título a carga máxima que aguenta '
                '— e é ela que decide se o veículo aguenta você.' % n)
    if menor == maior:
        if declaram == 1:
            return ('Um dos %d anúncios declara no título a carga máxima: %d kg. '
                    'Nos outros, o limite não está no título.' % (n, menor))
        return ('%d dos %d anúncios declaram no título a carga máxima, e os %d dizem '
                'o mesmo número: %d kg.' % (declaram, n, declaram, menor))
    if declaram == n:
        return ('Todos os %d declaram no título a carga máxima, e ela vai de %d a %d kg '
                '— a diferença entre os dois extremos é maior que o peso de uma pessoa.'
                % (n, menor, maior))

    return ('%d dos %d anúncios declaram no título a carga máxima, e entre eles ela vai '
            'de %d a %d kg. Nos outros, o limite não está no título.'
            % (declaram, n, menor, maior))


MUNDOS_DA_CARGA = (
    # (n, declaram, menor, maior, pedaco que a frase tem de conter)
    (6, 0, None, None, 'Nenhum dos 6'),
    (16, 1, 150, 150, 'Um dos 16'),
    (16, 3, 100, 100, 'dizem o mesmo número: 100 kg'),
    (16, 16, 60, 150, 'Todos os 16'),
    (16, 6, 60, 150, 'de 60 a 150 kg'),
)


# ---------------------------------------------------------------------------
# A FRASE DO PIVO DA F1 — a contagem que mais vale nesta ilha, e ela nasceu de
# uma prosa que afirmava o PIVO sem um anuncio declarando (04/11/2026)
#
# A camada declarada de `/veiculos/bicicleta-eletrica/` servia, escrito a mao:
# *"quase toda a faixa de baixo e dobravel, de PEDAL ASSISTIDO (...); o topo da
# faixa e a que tem ACELERADOR e motor forte — e e justamente ela que pode sair
# da categoria de bicicleta e entrar na de ciclomotor."*
#
# Medido no mesmo instante, nos seis anuncios que aquela pagina publica: ZERO
# declara acelerador e ZERO declara nao ter um. A frase punha os seis em dois
# lados do pivo da F1 — o que decide se a pessoa precisa de habilitacao — por
# PRECO, que nao e fonte de nada.
#
# E A ESPECIFICACAO DESTA ILHA JA PROIBIA ISSO NO BANCO, com estas palavras:
# "o enum de `acelerador` e pivo da F1, entao ele nao aceita nulo silencioso
# (...) e NUNCA cai no lado 'so pedal assistido' por omissao". A camada declarada
# fazia em prosa o que o esquema proibe no registro — e nenhuma regua desta ilha
# olhava para a prosa.
#
# O QUE A FRASE PODE DIZER E A CONTAGEM, e com zero declarando ela e a tese da
# ilha medida na propria vitrine: "todos falam, ninguem calcula".
def frase_do_pivo(n, declaram, com_acelerador, so_pedal):
    if declaram == 0:
        return ('Nenhum dos %d anúncios diz se o veículo tem acelerador, e é o '
                'acelerador que decide se ele é bicicleta elétrica ou ciclomotor '
                '— a diferença entre andar sem habilitação e precisar de uma.' % n)
    if com_acelerador and not so_pedal:
        return ('%d dos %d anúncios declaram acelerador no título; os outros não '
                'dizem se têm um, e é o acelerador que separa bicicleta elétrica '
                'de ciclomotor.' % (com_acelerador, n))
    if so_pedal and not com_acelerador:
        return ('%d dos %d anúncios declaram no título que não têm acelerador; os '
                'outros não dizem, e é o acelerador que separa bicicleta elétrica '
                'de ciclomotor.' % (so_pedal, n))

    return ('Dos %d anúncios, %d declaram acelerador no título e %d declaram não '
            'ter um; o resto não diz, e é o acelerador que separa bicicleta '
            'elétrica de ciclomotor.' % (n, com_acelerador, so_pedal))


MUNDOS_DO_PIVO = (
    # (n, declaram, com, so, pedaco que a frase tem de conter)
    (6, 0, 0, 0, 'Nenhum dos 6'),
    (16, 0, 0, 0, 'Nenhum dos 16'),
    (6, 2, 2, 0, '2 dos 6 anúncios declaram acelerador'),
    (6, 1, 0, 1, '1 dos 6 anúncios declaram no título que não têm'),
    (6, 5, 3, 2, 'Dos 6 anúncios, 3 declaram acelerador no título e 2'),
)


# A FRASE DO DOBRAVEL — a outra metade da mesma prosa falsa, e esta era apenas
# NAO CONTADA em vez de errada: `dobravel` esta no titulo ou nao esta.
def frase_do_dobravel(n, quantos):
    if quantos == 0:
        return 'Nenhum dos %d anúncios diz dobrável no título.' % n
    if quantos == n:
        return 'Os %d anúncios dizem dobrável no título.' % n
    if quantos == 1:
        return 'Um dos %d anúncios diz dobrável no título.' % n

    return '%d dos %d anúncios dizem dobrável no título.' % (quantos, n)


MUNDOS_DO_DOBRAVEL = (
    (6, 0, 'Nenhum dos 6'),
    (6, 6, 'Os 6 anúncios dizem'),
    (6, 1, 'Um dos 6'),
    (6, 5, '5 dos 6'),
)


# A FRASE DO PAR DE ENTRADA DA F2 — TENSAO E AMPERAGEM (04/11/2026)
#
# ELA NASCEU DE UMA FRASE QUE ESTAVA NO AR E NAO TINHA FONTE NENHUMA. A camada
# declarada da pagina da bicicleta mandava "olhar a tensao e a amperagem, e
# passar os dois na calculadora de autonomia" — instrucao CORRETA — e emendava,
# escrito a mao: *"bateria pequena em cidade de ladeira e a RECLAMACAO MAIS
# COMUM de quem compra sem fazer essa conta"*. Esta ilha nunca mediu reclamacao
# de ninguem: era um RANQUEAMENTO inventado, e a lista de quantificadores dos
# portoes de ar nao o via porque ele nao e um quantificador — e um SUPERLATIVO.
#
# E O NUMERO QUE A FRASE DEVIA DIZER E O MELHOR DESTA PAGINA: dos anuncios que
# ela publica, ZERO declara os DOIS no titulo. A pagina manda usar uma
# calculadora cujas duas entradas a propria vitrine nao entrega — a tese da ilha
# medida na vitrine, como a do pivo.
def frase_do_par_da_f2(n, os_dois, so_tensao, so_amperagem):
    if os_dois == 0 and so_tensao == 0 and so_amperagem == 0:
        return ('Nenhum dos %d anúncios declara a tensão e a amperagem no título '
                '— e são esses dois números que a calculadora de autonomia pede.' % n)
    if os_dois == 0:
        partes = []
        if so_tensao:
            partes.append('%d declara%s só a tensão'
                          % (so_tensao, '' if so_tensao == 1 else 'm'))
        if so_amperagem:
            partes.append('%d declara%s só a amperagem'
                          % (so_amperagem, '' if so_amperagem == 1 else 'm'))
        return ('Nenhum dos %d anúncios declara a tensão E a amperagem no mesmo '
                'título (%s) — e a calculadora de autonomia pede os dois.'
                % (n, ' e '.join(partes)))
    if os_dois == n:
        return ('Os %d anúncios declaram a tensão e a amperagem no título, que é '
                'o par que a calculadora de autonomia pede.' % n)
    if os_dois == 1:
        return ('Um dos %d anúncios declara a tensão e a amperagem no título; nos '
                'outros, o par que a calculadora de autonomia pede está na ficha.' % n)

    return ('%d dos %d anúncios declaram a tensão e a amperagem no título; nos '
            'outros, o par que a calculadora de autonomia pede está na ficha.'
            % (os_dois, n))


MUNDOS_DO_PAR_DA_F2 = (
    # (n, os_dois, so_tensao, so_amperagem, pedaco que a frase tem de conter)
    # O MUNDO REAL DAS DUAS PAGINAS em 04/11/2026: so a tensao, num anuncio so.
    (6, 0, 1, 0, 'Nenhum dos 6 anúncios declara a tensão E a amperagem'),
    (16, 0, 1, 0, '1 declara só a tensão'),
    (16, 0, 0, 0, 'Nenhum dos 16 anúncios declara a tensão e a amperagem no título'),
    (6, 6, 0, 0, 'Os 6 anúncios declaram'),
    (6, 1, 2, 0, 'Um dos 6 anúncios declara'),
    (16, 4, 3, 1, '4 dos 16 anúncios declaram'),
    (6, 0, 2, 1, '2 declaram só a tensão e 1 declara só a amperagem'),
)


def o_que_o_anuncio_declara_de_carga(a):
    """A celula da coluna de carga. Diz o numero, ou diz que o titulo se cala."""
    valor, porque = rel.carga_declarada(a['titulo'])
    if valor is None:
        return ('o título não declara', porque)

    return ('até %d kg' % valor, porque)


def ordenar(servem):
    """Secao 7, passo 3: desempate entre equivalentes. Ver o cabecalho."""
    return sorted(servem, key=lambda a: (-(a.get('vendas') or 0), a.get('preco') or 0))


def montar(bloco, editorial_da_pagina):
    # O piso de compra desta consulta, colhido por coletar-piso-da-vitrine.py.
    # Este gerador roda na bancada SEM REDE, entao ele LE o piso e nunca o gera.
    piso = bloco.get('piso_da_busca') or {}
    servem = ordenar([a for a in bloco['anuncios']
                      if a['serve'] and a.get('url_afiliado') and a.get('preco') is not None])
    if len(servem) < PISO_DA_30_2:
        return None, ('menos de %d anuncios que servem COM link e preco: %d'
                      % (PISO_DA_30_2, len(servem)))

    precos = sorted(a['preco'] for a in servem)
    rotulos = {}
    for a in servem:
        rotulos[a['rotulo_de_potencia']] = rotulos.get(a['rotulo_de_potencia'], 0) + 1
    declaram_watt = sum(v for k, v in rotulos.items() if k != 'sem_watt')
    dizem_qual = sum(v for k, v in rotulos.items() if k in ('nominal', 'pico', 'os_dois'))
    declaram_carga, carga_menor, carga_maior = rel.faixa_de_carga(servem)
    # O PIVO DA F1 E O DOBRAVEL, CONTADOS DO TITULO. Os dois entraram em
    # 04/11/2026, quando a camada declarada da pagina da bicicleta foi medida
    # afirmando os DOIS lados do pivo com ZERO anuncio declarando um deles.
    declaram_pivo, com_acelerador, so_pedal = rel.contagem_do_pivo(servem)
    dobraveis = rel.contagem_do_dobravel(servem)
    # O PAR DE ENTRADA DA F2, CONTADO DO TITULO (04/11/2026): entrou quando a
    # camada declarada da pagina da bicicleta foi medida afirmando um
    # RANQUEAMENTO de reclamacao que esta ilha nunca mediu.
    par_dois, par_so_v, par_so_ah = rel.contagem_do_par_da_f2(servem)

    cartoes, linhas = [], []
    for i, a in enumerate(servem):
        item = {
            'nome': a['titulo'],
            'preco': real(a['preco']),
            'preco_numero': a['preco'],
            'preco_nota': '(preço de %s)' % data_br(a['coletado_em']),
            'especificacao': o_que_o_anuncio_declara(a),
            # A CARGA QUE O TITULO DECLARA, e `carga_porque` e o PEDACO DO
            # TITULO que a sustenta — procedencia que se confere abrindo o
            # anuncio, nunca uma frase nossa (secao 24).
            'carga': o_que_o_anuncio_declara_de_carga(a)[0],
            'carga_porque': o_que_o_anuncio_declara_de_carga(a)[1],
            'url': a['url_afiliado'],
            'programa': 'shopee',
            # DOIS "DEGRAUS" DIFERENTES, E JUNTA-LOS SERIA DEFEITO SILENCIOSO.
            # `degrau_da_escada` do anuncio e o degrau da escada de CHAVES (que
            # palavra achou o produto na loja). O `degrau` que o cartao da casca
            # le e o da escada de COMPRA da 25.1, e e ele que decide o rotulo do
            # botao: ficha de produto diz "Ver na Shopee", busca diz "Ver ofertas
            # na Shopee". Estes links sao `url_produto` encurtado, ou seja FICHA,
            # entao o degrau de compra e 1 — e vai declarado, nao herdado.
            'degrau': 1,
            'degrau_da_escada_de_chaves': a['degrau_da_escada'],
            'imagem': a.get('imagem'),
            'loja': a['loja'],
            # ITEM 4 DO DESPACHO DE 30/10/2026 — O PAR DA 25.4-b E O PISO DA 25.2.
            # As 21 ofertas desta vitrine iam para a tela com SO `url`, o
            # encurtado da ficha: INTESTAVEIS pela 25.4-b (sem `url_produto` nao
            # ha como conferir se o anuncio vive) e SEM PISO pela 25.2 (no dia em
            # que o anuncio esgotar, o cartao fica sem saida de compra).
            # OS TRES PRIMEIROS NAO FORAM COLHIDOS AGORA: vinham da MESMA chamada
            # da API que devolveu `url_afiliado`, e e por isso que a 25.4-b.1
            # esta atendida sem remendo — os dois lados do par sao da mesma
            # oferta, da mesma leitura. Eles so nao chegavam ate aqui.
            'url_produto': a.get('url_produto'),
            'shop_id': a.get('shop_id'),
            'item_id': a.get('item_id'),
            'par_colhido_em': a.get('coletado_em'),
            # O PISO E DA CONSULTA, nao do anuncio, e a causa esta escrita em
            # coletar-piso-da-vitrine.py: a chave que achou TODOS os anuncios
            # desta pagina e uma so, e e ela que a 25.2 pode oferecer como saida
            # honesta. Ele nunca e montado aqui — vem colhido, com data.
            'url_busca': (piso or {}).get('url_busca'),
            'url_busca_produto': (piso or {}).get('url_busca_produto'),
            'piso_medido_em': (piso or {}).get('medido_em'),
        }
        linhas.append(item)
        if i < TETO_DO_CARROSSEL:
            cartoes.append(item)

    # AS RECUSAS VAO PARA A TELA, porque a secao 7 manda a pagina dizer o que
    # deve ao leitor sobre quem NAO entrou — e aqui o que nao entrou e, na
    # maioria, acessorio e brinquedo que a loja devolve na mesma busca.
    recusas = {}
    for a in bloco['anuncios']:
        if not a['serve']:
            recusas[a['recusado_por']] = recusas.get(a['recusado_por'], 0) + 1

    return {
        'id': bloco['id'],
        'consulta': bloco['consulta'],
        'slug': bloco['slug'],
        'chave_da_loja': bloco['chave_escolhida'],
        'degrau_da_escada': bloco['degrau_escolhido'],
        'colhido_em': bloco['colhido_em'],
        'colhido_em_br': data_br(bloco['colhido_em']),
        'numeros': {
            'n': len(servem),
            'de': real(precos[0]),
            'ate': real(precos[-1]),
            'mediana': real(statistics.median(precos)),
            'de_numero': precos[0],
            'ate_numero': precos[-1],
            'declaram_watt': declaram_watt,
            'dizem_qual_watt': dizem_qual,
            'sem_watt': rotulos.get('sem_watt', 0),
            'frase_do_rotulo': frase_do_rotulo(len(servem), declaram_watt, dizem_qual),
            'declaram_carga': declaram_carga,
            'carga_de': carga_menor,
            'carga_ate': carga_maior,
            'frase_da_carga': frase_da_carga(len(servem), declaram_carga,
                                             carga_menor, carga_maior),
            'declaram_pivo': declaram_pivo,
            'com_acelerador': com_acelerador,
            'so_pedal_assistido': so_pedal,
            'frase_do_pivo': frase_do_pivo(len(servem), declaram_pivo,
                                           com_acelerador, so_pedal),
            'dobraveis': dobraveis,
            'frase_do_dobravel': frase_do_dobravel(len(servem), dobraveis),
            'par_da_f2_os_dois': par_dois,
            'par_da_f2_so_tensao': par_so_v,
            'par_da_f2_so_amperagem': par_so_ah,
            'frase_do_par_da_f2': frase_do_par_da_f2(len(servem), par_dois,
                                                     par_so_v, par_so_ah),
            'lidas': bloco['resumo']['ofertas_lidas'],
            'recusadas': bloco['resumo']['ofertas_recusadas'],
            'recusas_por_causa': recusas,
        },
        'cartoes': cartoes,
        'linhas': linhas,
        'ordem': 'vendas medidas na API (decrescente), depois preço crescente — '
                 'o desempate entre equivalentes da seção 7',
    }, None


def gerar():
    anuncios = ler(ANUNCIOS)
    editorial = ler(EDITORIAL)
    decl = {p['id']: p for p in editorial['paginas']}

    paginas, recusadas = [], []
    for bloco in anuncios['consultas']:
        if not bloco.get('publicar_declarado'):
            recusadas.append({'id': bloco['id'],
                              'causa': 'nao declarada para publicar em consultas-de-produto.json'})
            continue
        if bloco['id'] not in decl:
            recusadas.append({'id': bloco['id'],
                              'causa': 'colhida e sem camada editorial em paginas-de-produto.json'})
            continue
        v, causa = montar(bloco, decl[bloco['id']])
        if v is None:
            recusadas.append({'id': bloco['id'], 'causa': causa})
            continue
        paginas.append(v)

    return {
        'id': 'vitrine-de-produto',
        'ilha': 'rodametria',
        'bloco': '5b',
        'gerado_em': anuncios['gerado_em'],
        'gerado_por': 'ferramentas/gerar-vitrine-de-produto.py',
        'o_que_este_arquivo_e': (
            'O que a TELA das paginas da secao 30 serve: cartoes do carrossel, linhas da '
            'tabela e os numeros, todos RECONTADOS de dados/anuncios-por-consulta.json. '
            'Nenhum numero desta ilha e digitado em prosa: a camada declarada traz moldes e '
            'quem os preenche e o PHP com o numero daqui.'),
        'vendas_ordenam_e_nao_vao_para_a_tela': (
            'A ordem e o desempate entre equivalentes da secao 7, e `vendas` e o unico '
            'desempate honesto porque comissao nunca ordena. Mas a contagem de vendas NAO '
            'e publicada: a secao 7 proibe selo de mais vendido, e prova social nao e o que '
            'esta pagina vende.'),
        'piso_da_30_2': PISO_DA_30_2,
        'teto_do_carrossel': TETO_DO_CARROSSEL,
        'paginas': paginas,
        'nao_nasceram': recusadas,
    }


def conferir():
    if not os.path.exists(VITRINE):
        print('REPROVADO: %s nao existe' % os.path.basename(VITRINE))
        return 1
    gravado = ler(VITRINE)
    calculado = gerar()

    falhas, afirmacoes = [], 0

    afirmacoes += 1
    if [p['id'] for p in gravado['paginas']] != [p['id'] for p in calculado['paginas']]:
        falhas.append('a lista de paginas gravada discorda da calculada')
    afirmacoes += 1
    if gravado.get('nao_nasceram') != calculado.get('nao_nasceram'):
        falhas.append('a lista de `nao_nasceram` gravada discorda da calculada')

    for g, c in zip(gravado['paginas'], calculado['paginas']):
        for campo in ('numeros', 'cartoes', 'linhas', 'chave_da_loja', 'degrau_da_escada',
                      'colhido_em', 'colhido_em_br', 'consulta', 'slug', 'ordem'):
            afirmacoes += 1
            if g.get(campo) != c.get(campo):
                falhas.append('%s: campo %r gravado nao refaz' % (g['id'], campo))
        afirmacoes += 1
        if len(g['cartoes']) > calculado['teto_do_carrossel']:
            falhas.append('%s: carrossel com %d cartoes, teto %d'
                          % (g['id'], len(g['cartoes']), calculado['teto_do_carrossel']))
        afirmacoes += 1
        if len(g['linhas']) < calculado['piso_da_30_2']:
            falhas.append('%s: tabela com %d linhas, piso da 30.2 e %d'
                          % (g['id'], len(g['linhas']), calculado['piso_da_30_2']))
        # Link de compra sem `url` nao e saida de compra, e a secao 7 proibe
        # bloco de compra com item sem saida.
        for item in g['linhas']:
            afirmacoes += 1
            if not (item.get('url') or '').startswith('https://'):
                falhas.append('%s: linha sem url de afiliado' % g['id'])
            afirmacoes += 1
            if 'preço de' not in (item.get('preco_nota') or ''):
                falhas.append('%s: preco sem a data da coleta ao lado (secao 7)' % g['id'])

    # OS CINCO MUNDOS DA FRASE DO ROTULO, e quatro deles o banco de hoje nao
    # produz. Trava que nunca viu o mundo dela nasce errada sem poder falhar.
    for n, decl_w, dizem, pedaco in MUNDOS_DO_ROTULO:
        afirmacoes += 1
        frase = frase_do_rotulo(n, decl_w, dizem)
        if pedaco not in frase:
            falhas.append('frase_do_rotulo(%d,%d,%d) nao traz %r: %r'
                          % (n, decl_w, dizem, pedaco, frase))
        afirmacoes += 1
        if ', 0 ' in frase or frase.endswith(' 0.'):
            falhas.append('frase_do_rotulo(%d,%d,%d) imprime zero no meio da frase: %r'
                          % (n, decl_w, dizem, frase))

    # OS CINCO MUNDOS DA FRASE DA CARGA, e o banco de hoje produz DOIS deles (o
    # vazio na bicicleta e a faixa no patinete). Os outros tres sao fabricados
    # pelo mesmo motivo dos do rotulo.
    for n, decl_c, menor, maior, pedaco in MUNDOS_DA_CARGA:
        afirmacoes += 1
        frase = frase_da_carga(n, decl_c, menor, maior)
        if pedaco not in frase:
            falhas.append('frase_da_carga(%s,%s,%s,%s) nao traz %r: %r'
                          % (n, decl_c, menor, maior, pedaco, frase))
        afirmacoes += 1
        # O PORTUGUES QUE SO APARECE NO MUNDO QUE O BANCO NAO TEM: faixa de um
        # valor so nao pode sair como "de X a X", e um anuncio so nao pode sair
        # com verbo no plural.
        if menor is not None and menor == maior and ' a %d kg' % maior in frase:
            falhas.append('frase_da_carga(%s,%s,%s,%s) imprime faixa de valor unico: %r'
                          % (n, decl_c, menor, maior, frase))
        afirmacoes += 1
        if decl_c == 1 and 'declaram' in frase:
            falhas.append('frase_da_carga com UM anuncio usa verbo no plural: %r' % frase)

    # TODA LINHA TEM A CELULA DA CARGA, E ELA TEM PROCEDENCIA. A celula pode
    # dizer que o titulo se cala — o que ela nao pode e nascer vazia, porque
    # coluna vazia na tabela e a pagina deixando o leitor sem saber se ninguem
    # declarou ou se ninguem leu.
    for g in calculado['paginas']:
        for item in g['linhas']:
            afirmacoes += 1
            if not (item.get('carga') or '').strip():
                falhas.append('%s: linha sem a celula de carga' % g['id'])
            afirmacoes += 1
            if not (item.get('carga_porque') or '').strip():
                falhas.append('%s: celula de carga sem procedencia' % g['id'])
            afirmacoes += 1
            # A CELULA TEM DE REFAZER DA REGUA, nunca de campo herdado.
            valor = rel.carga_declarada(item['nome'])[0]
            esperado = 'o título não declara' if valor is None else 'até %d kg' % valor
            if item['carga'] != esperado:
                falhas.append('%s: celula de carga %r nao refaz da regua: %r'
                              % (g['id'], item['carga'], esperado))

    # OS MUNDOS FABRICADOS DAS DUAS FRASES NOVAS (04/11/2026). O dado de hoje
    # produz UM dos cinco mundos do pivo — zero declarando nas duas paginas — e
    # dois dos quatro do dobravel. Mundo que o banco nao tem e mundo que so a
    # bateria fabricada ve: a frase do pivo com acelerador declarado NUNCA rodou
    # contra dado de verdade, e e por isso que ela esta aqui.
    for n, decl, com, so, pedaco in MUNDOS_DO_PIVO:
        frase = frase_do_pivo(n, decl, com, so)
        afirmacoes += 1
        if pedaco not in frase:
            falhas.append('frase_do_pivo(%d,%d,%d,%d) nao traz %r: %r'
                          % (n, decl, com, so, pedaco, frase))
        afirmacoes += 1
        # IMPRIMIR ZERO NO MEIO DA FRASE e falha nomeada nas irmas desta funcao:
        # "0 dos 6 anuncios declaram acelerador" e portugues de maquina, e o
        # ramo do zero existe justamente para nao sair.
        if ' 0 ' in frase:
            falhas.append('frase_do_pivo(%d,%d,%d,%d) imprime zero no meio da frase: %r'
                          % (n, decl, com, so, frase))
        afirmacoes += 1
        if decl == 1 and 'anúncios declaram' in frase and 'os outros' not in frase:
            falhas.append('frase_do_pivo com UM declarando perde a ressalva dos outros')

    for n, quantos, pedaco in MUNDOS_DO_DOBRAVEL:
        frase = frase_do_dobravel(n, quantos)
        afirmacoes += 1
        if pedaco not in frase:
            falhas.append('frase_do_dobravel(%d,%d) nao traz %r: %r'
                          % (n, quantos, pedaco, frase))
        afirmacoes += 1
        if ' 0 ' in frase:
            falhas.append('frase_do_dobravel(%d,%d) imprime zero no meio: %r'
                          % (n, quantos, frase))

    # OS MUNDOS FABRICADOS DA FRASE DO PAR DA F2 (04/11/2026). O dado de hoje
    # produz UM dos sete — zero com os dois e UM so com a tensao, nas duas
    # paginas. O mundo "os dois declarados" nao existe em anuncio nenhum desta
    # vitrine, e e exatamente por isso que ele esta fabricado aqui.
    for n, dois, so_v, so_ah, pedaco in MUNDOS_DO_PAR_DA_F2:
        frase = frase_do_par_da_f2(n, dois, so_v, so_ah)
        afirmacoes += 1
        if pedaco not in frase:
            falhas.append('frase_do_par_da_f2(%d,%d,%d,%d) nao traz %r: %r'
                          % (n, dois, so_v, so_ah, pedaco, frase))
        afirmacoes += 1
        if ' 0 ' in frase:
            falhas.append('frase_do_par_da_f2(%d,%d,%d,%d) imprime zero no meio: %r'
                          % (n, dois, so_v, so_ah, frase))
        afirmacoes += 1
        # A FRASE NUNCA PODE AFIRMAR RANQUEAMENTO, que e o defeito que ela
        # substituiu: superlativo de frequencia sobre o mercado nao tem fonte
        # nesta ilha.
        for proibida in ('mais comum', 'mais comuns', 'vende mais', 'mais vendid'):
            if proibida in frase.lower():
                falhas.append('frase_do_par_da_f2 afirma ranqueamento (%r): %r'
                              % (proibida, frase))

    for g in calculado['paginas']:
        ad = [{'titulo': item['nome']} for item in g['linhas']]
        afirmacoes += 1
        esperado_par = rel.contagem_do_par_da_f2(ad)
        obtido_par = (g['numeros']['par_da_f2_os_dois'],
                      g['numeros']['par_da_f2_so_tensao'],
                      g['numeros']['par_da_f2_so_amperagem'])
        if obtido_par != esperado_par:
            falhas.append('%s: a contagem do par da F2 %s nao refaz da regua: %s'
                          % (g['id'], obtido_par, esperado_par))
        afirmacoes += 1
        if g['numeros']['frase_do_par_da_f2'] != frase_do_par_da_f2(len(ad), *esperado_par):
            falhas.append('%s: a frase do par da F2 no arquivo nao e a que a funcao produz'
                          % g['id'])

    # E OS DOIS NUMEROS NOVOS REFAZEM DA REGUA, nunca de campo herdado — a mesma
    # cobranca que a celula da carga ja tinha. Campo gravado que ninguem recontra
    # e numero digitado com data de validade.
    for g in calculado['paginas']:
        ad = [{'titulo': item['nome']} for item in g['linhas']]
        afirmacoes += 1
        esperado = rel.contagem_do_pivo(ad)
        obtido = (g['numeros']['declaram_pivo'], g['numeros']['com_acelerador'],
                  g['numeros']['so_pedal_assistido'])
        if obtido != esperado:
            falhas.append('%s: a contagem do pivo %s nao refaz da regua: %s'
                          % (g['id'], obtido, esperado))
        afirmacoes += 1
        if g['numeros']['dobraveis'] != rel.contagem_do_dobravel(ad):
            falhas.append('%s: a contagem do dobravel nao refaz da regua' % g['id'])
        afirmacoes += 1
        if g['numeros']['frase_do_pivo'] != frase_do_pivo(len(ad), *esperado):
            falhas.append('%s: a frase do pivo no arquivo nao e a que a funcao produz'
                          % g['id'])

    # A CAMADA DECLARADA NAO PODE TRAZER NUMERO DIGITADO. Esta e a trava que a
    # cicatriz do `REGISTRO.md` desta ilha de 29/10 (16h2xZ) deixou escrita:
    # "prosa que afirma o estado do banco e numero digitado em outro traje".
    editorial = ler(EDITORIAL)
    permitidos = tuple(n['texto'] for n in editorial.get('numeros_declarados_permitidos', []))
    # QUALQUER DIGITO, e nao "grupo de dois ou mais": a primeira versao desta
    # trava cobrava `\d{2,}` e a mutacao `Sao 2 familias com pagina hoje` na
    # prosa da mae SOBREVIVEU — justamente a contagem de um digito, que e a
    # contagem que esta ilha tem. Numero pequeno digitado e o que envelhece
    # primeiro: a prosa que diz `2 familias` mente no dia em que a terceira
    # nascer, e nada acusa.
    #
    # O que escapa e so o que esta NOMEADO em `numeros_declarados_permitidos`,
    # com o motivo ao lado — o numero da Resolucao Contran e nome proprio de
    # documento, nao numero de tela. Numero que a prosa precisa dizer e nao e
    # contagem (oito quilometros, cem quilos) se escreve por extenso.
    proibido = _re.compile(r'\d')
    # O MOLDE NAO E NUMERO DIGITADO — ELE E O OPOSTO, E A TRAVA NAO SABIA DISSO
    # (04/11/2026). Todo molde desta ilha nasceu sem digito no nome
    # (`{FRASE_DA_CARGA}`, `{DECLARAM_WATT}`), entao a trava nunca encontrou um
    # e o buraco ficou invisivel. O molde do par de entrada da F2 e o primeiro
    # nomeado pela FERRAMENTA desta ilha, e as tres ferramentas se chamam F1, F2
    # e F3: o nome carrega um digito, e a trava reprovou a frase CERTA — aquela
    # que SUBSTITUIU uma afirmacao inventada por uma contagem.
    #
    # Renomear o molde para fugir da trava seria o conserto errado: o proximo
    # `{FRASE_DA_F1}` pagaria de novo, e e a 32.5-c outra vez. A trava passa a
    # tirar os MOLDES antes de procurar digito, e a forma do molde e estreita de
    # proposito — `{` + MAIUSCULA/digito/sublinhado + `}` —, porque e a forma que
    # o PHP substitui. Minuscula dentro das chaves NAO e molde e continua
    # reprovando: molde que o PHP nao reconhece vai para a tela como esta.
    molde = _re.compile(r'\{[A-Z][A-Z0-9_]*\}')
    for pag in editorial['paginas'] + [editorial['mae']]:
        for campo, valor in sorted(pag.items()):
            for texto in _textos(valor):
                limpo = molde.sub(' ', texto)
                for ok in permitidos:
                    limpo = limpo.replace(ok, '')
                afirmacoes += 1
                achado = proibido.search(limpo)
                if achado:
                    falhas.append('%s: a camada declarada traz numero digitado em %r (%r): %r'
                                  % (pag.get('id', pag.get('slug')), campo,
                                     achado.group(0), texto[:70]))

    # A CAMADA DECLARADA NAO PODE TRAZER QUANTIFICADOR POR EXTENSO, E ESTA TRAVA
    # E IRMA DA DE CIMA — ela existe porque a de cima esta CERTA e nao bastava.
    #
    # Medido em 03/11 e outra vez em 04/11/2026, duas frases diferentes, o mesmo
    # buraco. A trava de digito reprova QUALQUER digito na camada declarada, ate
    # um so. As duas frases que foram ao ar afirmando o estado do catalogo
    # passaram por ela SEM ESFORCO, porque nenhuma das duas tem um digito:
    #
    #   "a carga maxima (...) QUASE NUNCA ESTA NO TITULO"  -> 6 de 16 declaravam
    #   "QUASE TODA a faixa de baixo e dobravel, de PEDAL ASSISTIDO"  -> 0 de 6
    #                                                      declarava o pivo
    #
    # Proporcao por extenso e contagem com outro traje: ela afirma o estado do
    # banco com a mesma validade de prazo que um numero, e envelhece do mesmo
    # jeito — calada. Esta trava e a 32.5-d uma familia acima: a regua que nunca
    # viu o mundo dela aprova o mundo que existia.
    #
    # E ELA NAO JULGA PROSA, DE PROPOSITO. Regua que tentasse decidir se um
    # "quase nunca" fala do mundo ou do catalogo reprovaria voz legitima, que e o
    # caminho mais curto para alguem a ignorar (20.5). Ela DENUNCIA a ocorrencia
    # e exige que alguem a tenha olhado: o que escapa e so o que esta NOMEADO em
    # `quantificadores_declarados_permitidos`, com o campo e o motivo ao lado —
    # exatamente a forma de `numeros_declarados_permitidos`, que esta ilha ja
    # usa. Quem acrescentar prosa nova com quantificador tem de responder, por
    # escrito e no arquivo, se aquilo e voz ou contagem.
    quantificadores = (
        'quase nunca', 'quase sempre', 'quase todo', 'quase toda', 'quase todos',
        'quase todas', 'quase ninguem', 'quase nenhum', 'quase nenhuma',
        'a maioria', 'maioria', 'a minoria', 'minoria', 'raramente', 'costuma',
        'costumam', 'na maior parte', 'a maior parte', 'maior parte', 'boa parte',
        'grande parte', 'geralmente', 'normalmente', 'em geral', 'de modo geral',
        'via de regra', 'tipicamente', 'frequentemente', 'na pratica',
        'a maior parte das', 'poucos', 'poucas', 'muitos', 'muitas',
    )
    liberados = {}
    for q in editorial.get('quantificadores_declarados_permitidos', []):
        liberados.setdefault(q['termo'], []).append(q)
        afirmacoes += 1
        if not (q.get('porque') or '').strip():
            falhas.append('quantificador liberado %r sem motivo escrito' % q['termo'])
        afirmacoes += 1
        if not (q.get('campo') or '').strip():
            falhas.append('quantificador liberado %r sem o campo onde ele mora' % q['termo'])
        afirmacoes += 1
        if not (q.get('ancora_no_ar') or '').strip():
            falhas.append('quantificador liberado %r sem ancora_no_ar: o portao de ar nao '
                          'teria como saber dentro de que texto ele vale' % q['termo'])

    # OS CAMPOS DE DOCUMENTACAO DA RAIZ ficam fora: eles nao vao para a tela e
    # falam justamente desta trava. Varrer o que explica a regra e a familia do
    # portao que reprova a pagina certa.
    usados = set()
    for pag in editorial['paginas'] + [editorial['mae']]:
        quem = pag.get('id', pag.get('slug'))
        for campo, valor in sorted(pag.items()):
            for texto in _textos(valor):
                t = _sem_acento(texto)
                for q in quantificadores:
                    i = t.find(q)
                    if i < 0:
                        continue
                    # BORDA A DIREITA pela licao do `Capacete1` desta ilha:
                    # `poucos` nao pode casar dentro de `poucossimos`, e `muitas`
                    # nao pode casar `muitassimas`. A esquerda tem de ser inicio
                    # ou nao-letra, senao `maioria` casaria dentro de outra.
                    antes = t[i - 1] if i else ' '
                    depois = t[i + len(q):i + len(q) + 1] or ' '
                    if antes.isalpha() or depois.isalpha():
                        continue
                    afirmacoes += 1
                    ok = [x for x in liberados.get(q, []) if x['campo'] == campo]
                    if not ok:
                        falhas.append(
                            '%s: a camada declarada afirma uma PROPORCAO por extenso em %r '
                            '(%r) e ela nao esta em quantificadores_declarados_permitidos: '
                            '%r' % (quem, campo, q, texto[:90]))
                    else:
                        usados.add((q, campo))
                        # A ANCORA TEM DE EXISTIR NO PROPRIO TEXTO, e ela tem de
                        # CONTER o termo. Ancora solta (ou que nao cerca o termo)
                        # faz o portao de ar apagar um pedaco qualquer da pagina e
                        # aprovar o resto: liberacao de uma frase viraria anistia.
                        for x in ok:
                            anc = _sem_acento(x.get('ancora_no_ar') or '')
                            afirmacoes += 1
                            if anc and anc not in t:
                                falhas.append(
                                    '%s: a ancora %r do quantificador liberado %r nao '
                                    'existe no texto declarado de %r'
                                    % (quem, x['ancora_no_ar'], q, campo))
                            afirmacoes += 1
                            if anc and q not in anc:
                                falhas.append(
                                    'a ancora %r do quantificador liberado %r nao contem o '
                                    'proprio termo' % (x['ancora_no_ar'], q))

    # LIBERACAO QUE NAO LIBERA NADA E LIXO, e lixo nesta lista e pior que em
    # outra: ela e a lista de quem JA FOI OLHADO. Entrada morta faz a proxima
    # execucao pensar que alguem conferiu uma frase que nao existe mais.
    for termo, itens in sorted(liberados.items()):
        for q in itens:
            afirmacoes += 1
            if (termo, q['campo']) not in usados:
                falhas.append('quantificador liberado %r em %r nao existe mais na camada '
                              'declarada: liberacao morta' % (termo, q['campo']))

    # A PROVA DE QUE A TRAVA DO QUANTIFICADOR MORDE — trava que nunca falhou nao
    # e trava, e a `bancada.py` desta ilha cobra as duas metades do veredito.
    #
    # OS MUNDOS SAO FABRICADOS A PARTIR DA CAMADA DECLARADA REAL, mexendo UMA
    # coisa de cada vez, e o primeiro deles e a FRASE DE VERDADE que esteve no ar
    # — nao um exemplo inventado.
    def _varre(pag, liberados_de_teste):
        achados = []
        for campo, valor in sorted(pag.items()):
            for texto in _textos(valor):
                tt = _sem_acento(texto)
                for q in quantificadores:
                    i = tt.find(q)
                    while i >= 0:
                        antes = tt[i - 1] if i else ' '
                        depois = tt[i + len(q):i + len(q) + 1] or ' '
                        if not (antes.isalpha() or depois.isalpha()):
                            if not [x for x in liberados_de_teste.get(q, [])
                                    if x['campo'] == campo]:
                                achados.append((campo, q))
                            break
                        i = tt.find(q, i + 1)
        return achados

    base = _json.loads(_json.dumps(editorial['mae']))
    afirmacoes += 1
    if _varre(base, liberados):
        falhas.append('o mundo REAL da mae nao passa na trava do quantificador: a prova de '
                      'que ela morde mede nada se o mundo sadio ja reprova')

    # (a) A FRASE REAL DE 03/11, que viveu um dia inteiro nesta pagina.
    real = _json.loads(_json.dumps(editorial['mae']))
    real['o_que_decide'][2]['porque'] = (
        'é o filtro que quase ninguém olha e que quase nunca está no título.')
    afirmacoes += 1
    if not _varre(real, liberados):
        falhas.append('a frase REAL que esteve no ar ("quase nunca esta no titulo") NAO e '
                      'achada pela trava do quantificador')

    # (b) OUTRA FORMA, porque a trava nao pode pegar so o "quase nunca" que
    #     alguem ja imaginou — a leitura pelo avesso e o defeito da 20.8.
    outra = _json.loads(_json.dumps(editorial['mae']))
    outra['resposta'].append('A maioria das famílias desta seção não declara a bateria.')
    afirmacoes += 1
    if not _varre(outra, liberados):
        falhas.append('outra forma de proporcao ("a maioria") NAO e achada pela trava')

    # (c) A LIBERACAO VALE PARA O CAMPO DELA E NAO PARA OUTRO. Sem esta, a lista
    #     de quem foi olhado viraria anistia por palavra.
    afirmacoes += 1
    if not _varre(real, {'quase nunca': [{'campo': 'outro_campo'}]}):
        falhas.append('a liberacao de um quantificador em OUTRO campo liberou este: a lista '
                      'de quem foi olhado virou anistia por palavra')

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')

    return 1 if falhas else 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group()
    g.add_argument('--gravar', action='store_true')
    g.add_argument('--conferir', action='store_true')
    a = p.parse_args()

    if a.conferir:
        return conferir()

    saida = gerar()
    for pg in saida['paginas']:
        n = pg['numeros']
        print('%s: %d anuncios · %s a %s (mediana %s) · declaram watt %d, dizem qual %d'
              % (pg['id'], n['n'], n['de'], n['ate'], n['mediana'],
                 n['declaram_watt'], n['dizem_qual_watt']))
        print('   carga declarada em %d de %d · faixa %s a %s kg'
              % (n['declaram_carga'], n['n'], n['carga_de'], n['carga_ate']))
        print('   %s' % n['frase_da_carga'])
        print('   carrossel %d cartao(oes) · recusadas %d %s'
              % (len(pg['cartoes']), n['recusadas'], n['recusas_por_causa']))
    for r in saida['nao_nasceram']:
        print('NAO NASCEU %s: %s' % (r['id'], r['causa']))

    if not a.gravar:
        print('\nsem --gravar: nada foi escrito.')
        return 0

    with open(VITRINE, 'w', encoding='utf-8') as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('\ngravado: %s' % os.path.basename(VITRINE))

    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Colhe o dado COMERCIAL das consultas de produto da secao 30, consulta por consulta.

    python3 ferramentas/coletar-por-consulta.py --ensaio  [--so <id>]
    python3 ferramentas/coletar-por-consulta.py --gravar  [--so <id>] [--sem-link]
    python3 ferramentas/coletar-por-consulta.py --conferir   # SEM REDE

`--ensaio` nao toca no banco: escreve o laudo na tela e para (25.3).
`--conferir` nao chama a rede: recarrega `dados/anuncios-por-consulta.json`,
REAPLICA a regua de relevancia sobre os titulos gravados e reprova se algum
veredito gravado discordar do calculado, ou se algum numero do resumo nao
refizer. `--sem-link` grava sem chamar o encurtador, para medir a coleta sem
gastar chamada de geracao de link.

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE (25.6). Esta
ferramenta nunca as imprime e nunca as grava.

---------------------------------------------------------------------------
A DIFERENCA ENTRE ESTA FERRAMENTA E AS DUAS QUE JA EXISTEM NESTA ILHA
---------------------------------------------------------------------------
`coletar-piso-de-compra.py` parte de um REGISTRO do banco e grava a BUSCA
encurtada daquele produto: o degrau 4 da escada da 25.1.
`coletar-oferta.py` parte do mesmo registro e procura a FICHA daquele produto:
os degraus 1 a 3, com as seis travas do casamento da 25.7.

Esta parte da CONSULTA. A pergunta nao e "onde se compra o Honeywhale M2 MAX",
e "o que a loja tem para quem digita `patinete eletrico`" — e quem decide e
`relevancia-do-anuncio.py`, que nao sabe de marca nenhuma. A 30.2 abriu esse
portao com todas as letras: anuncio de Shopee e de Mercado Livre e fonte valida
de dado COMERCIAL (titulo, preco, foto, medida e quantidade declaradas), com
fonte e data, e ali o anuncio nao precisa casar com registro do banco.

**Dado TECNICO continua fora.** O watt, a velocidade, o acelerador e a carga
maxima tem piso de nivel 5 no `niveis_minimos_por_campo` do esquema desta ilha,
e titulo de anuncio e nivel 6. Nada que sai daqui entra em campo tecnico de
registro nenhum: o que sai e anuncio, com o que ele declara e o que ele NAO
declara escritos lado a lado.

---------------------------------------------------------------------------
A ESCADA DE CHAVES, E POR QUE ELA EXISTE AQUI E NAO NA `coletar-por-consulta`
DAS OUTRAS ILHAS
---------------------------------------------------------------------------
No Clube do Mosaico a chave da loja E a consulta: quem digita `torques para
mosaico` no Google acha torques na Shopee com a mesma palavra. Aqui elas
divergem, e a divergencia foi medida em 29/10/2026 nas seis cabecas do dossie:
`patinete eletrico` devolve ZERO patinete de adulto nas 20 primeiras ofertas, e
`patinete eletrico adulto` devolve doze. A consulta e a palavra da PESSOA; a
chave e a palavra da LOJA. Por isso cada consulta declara uma escada, do degrau
mais especifico para o mais largo, a escada PARA no primeiro degrau que alcanca
o piso de tres, e o degrau que casou fica gravado em cada anuncio.

E o degrau NAO e escolhido por quem escreve: e medido. Chave que devolve menos
de tres anuncios que servem nao vira a chave da pagina — a escada desce, e os
degraus medidos ficam gravados em `escada_medida`, que e procedencia e e o que a
ronda compara para ver uma palavra-chave morrer sem ninguem avisar.
"""
import argparse
import datetime
import importlib.util
import json
import os
import re
import statistics
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')
DECLARACAO = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')

SUB_ID_1 = 'rodametria'      # a Shopee recusa sub-id com hifen ou sublinhado
QUANTOS = 20
PAUSA = 0.5
PISO_DA_30_2 = 3
# O RECUO COM QUE ESTE ARQUIVO E GRAVADO, declarado UMA vez. Ele estava escrito
# so dentro do `--gravar` daqui, e a ferramenta que aplicou a repeticao da loja
# em 16/11/2026 gravou com outro — o diff saiu com o arquivo INTEIRO reformatado,
# 2.199 linhas trocadas para marcar um anuncio. Formato de arquivo gerado e fato
# do dono dele: quem grava le daqui.
RECUO_DO_BANCO = 1
HOJE = datetime.date.today().isoformat()


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'teste-relevancia-do-anuncio.py'))

# A DIMENSAO DA FOTO E LIDA DE UM LUGAR SO, e o lugar e `coletar-oferta.py`.
# A secao 8 do contrato separa as duas metades com todas as letras: DECISAO se
# escreve duas vezes e se confere; FATO EXTERNO se le de um lugar so, porque
# "ninguem redescobre fato externo de forma independente, entao a segunda
# escrita dele nao confere nada e so cria duas verdades". Largura e altura de um
# arquivo na CDN sao fato externo. Quem decide se a foto ENTRA e desta
# ferramenta; quem le os bytes e aquela.
oferta_mod = _modulo('coletar_oferta', os.path.join(FERRAMENTAS, 'coletar-oferta.py'))
medir_foto = oferta_mod.medir_foto


def shopee():
    """A API so e carregada quando a rede vai ser usada: `--conferir` nao a quer."""
    return _modulo('shopee_api', os.path.abspath(
        os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))


def declaracao():
    with open(DECLARACAO, encoding='utf-8') as f:
        return json.load(f)


def sub_id_2_de(id_da_consulta):
    """So letras e digitos: a Shopee recusa o resto, e o ML tem teto de 30.

    Derivado do `id` da consulta e nunca digitado, pelo mesmo motivo que o ID de
    medicao do GA4 mora numa constante.
    """
    return re.sub(r'[^0-9a-z]', '', (id_da_consulta or '').lower())[:24]


# ---------------------------------------------------------------------------
# O NUMERO PROPRIO
#
# A 30.2 pede UM numero proprio por pagina, e a declaracao de cada consulta diz
# qual. Hoje ha uma forma, e ela nao e estimada: `faixa_de_preco`, o menor e o
# maior preco entre os anuncios que SERVEM, com a mediana ao lado e a contagem de
# sobre quantas ofertas ela foi feita.
#
# A CONTAGEM DO ROTULO DE POTENCIA viaja junto, e ela e o numero que e a TESE
# desta ilha: de quantos anuncios declaram watt, quantos dizem se o watt e
# nominal ou de pico. Ela nao e o numero proprio declarado — e a prestacao de
# contas da secao 7 em forma de contagem, e e o que separa esta pagina de uma
# lista de precos.
#
# Os dois sao RECALCULADOS por `--conferir` e comparados com o gravado: numero
# que a ilha publica sobre si mesma nasce contado, e continua contado na passada
# seguinte (secao 8).
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# A MESMA LOJA ANUNCIANDO A MESMA OFERTA DUAS VEZES — 16/11/2026
#
# MEDIDO NO AR em `/veiculos/moto-eletrica/`, a pagina que nasceu na manha do
# mesmo dia, e o estrago era de TRES ordens diferentes ao mesmo tempo:
#
#   cartao 1  "11.11 Moto Eletrica Adulto Panda A4 ... 150kg"   R$ 1.096,38
#   cartao 2  "Moto Eletrica Adulto Panda A4 ... 150kg"         R$ 1.522,76
#
# os dois da loja `francyellenoliveira`, shop_id 277054573, item 58273014613 e
# 58273026115 — o mesmo veiculo, nos DOIS cartoes mais caros da tela.
#
#   (1) O LEITOR PAGA PELO CARTAO ERRADO. Clicar no segundo custa R$ 426,38 mais
#       (38,9%) pelo MESMO produto da MESMA loja. Nao e escolha a oferecer: e a
#       pagina cobrando do leitor por existir.
#   (2) A MEDIANA PUBLICADA ESTAVA ERRADA. Com o repetido dentro, a pagina
#       publicava mediana de R$ 5.011,38 sobre 4 ofertas; sobre as 3 ofertas
#       DISTINTAS ela e R$ 8.500,00. A diferenca e de R$ 3.488,62, e e a
#       cicatriz do item 3 do despacho de 04/11/2026 num traje novo — lá a
#       mediana virou o MINIMO porque cinco anuncios tinham o mesmo preco, e o
#       conserto daquele dia alcancou o CARROSSEL e nao a CONTA.
#   (3) TODA FRASE "X DOS 4" CONTAVA O MESMO ANUNCIO DUAS VEZES: "2 dos 4
#       declaram a carga maxima, e os 2 dizem o mesmo numero: 150 kg" — os 2
#       eram um.
#
# POR QUE O `escolher_carrossel` DO GERADOR NAO PEGAVA, e ele nao esta errado: a
# regra dele e de PRECO ("enquanto houver preco que o carrossel ainda nao mostra,
# a vaga e dele") e os dois precos sao DISTINTOS. Ela recusa deduplicar por
# produto com a razao certa — *"deduplicar oferta equivalente exigiria afirmar
# que dois anuncios de duas lojas SAO o mesmo produto, e esta ilha nao mede
# isso"*. Esta passada nao fura aquela recusa: ela e de UMA LOJA SO, e quem
# afirma a identidade e o VENDEDOR, que escreveu os dois titulos (ver
# `chave_de_oferta_da_loja` na regua).
#
# E ELA NAO E UMA RECUSA DE RELEVANCIA, E `serve` NAO E TOCADO. O anuncio
# repetido E o produto da pagina — ele e exatamente igual ao que ficou. Escrever
# `serve: False` nele seria o item 3 do despacho de 16/11 acontecendo outra vez:
# duas perguntas diferentes num campo so. `serve` responde "e o produto desta
# pagina?"; `repetido_por` responde "esta oferta ja esta nesta pagina, mais
# barata?". Quem le a pagina usa `entra_na_pagina`, que e as duas.
#
# E ELA NAO E QUARENTENA, e isto e deliberado: a quarentena da 25.11 e para
# anuncio que MORREU e ela atravessa a coleta seguinte de proposito. Aqui o
# repetido esta VIVO, e no dia em que o mais barato sair do ar o mais caro passa
# a ser a unica oferta daquele veiculo — e tem de voltar sozinho. Por isso esta
# marca e DERIVADA, recalculada do zero em toda passada (`a.pop`), como o
# `energia_wh` do `derivar-banco.py`. Marca derivada que se grava uma vez e
# nunca se refaz e a divida que a 25.11 pagou do outro lado.
#
# QUEM FICA E O MAIS BARATO, e o desempate e o `item_id` menor: precos iguais
# com o mesmo nome na mesma loja sao a mesma oferta duplicada, e escolher pelo
# `item_id` e escolher o anuncio mais antigo da loja em vez de deixar a ordem do
# dicionario decidir.
# ---------------------------------------------------------------------------
CAUSA_DA_REPETICAO = 'mesma_oferta_repetida_pela_loja'


def entra_na_pagina(a):
    """O anuncio entra na tela e nas CONTAS da pagina?

    Duas perguntas, e as duas no mesmo lugar porque toda conta desta pagina quer
    as duas: `serve` (e o produto desta pagina) e `repetido_por` (esta oferta ja
    esta aqui, mais barata). Ela existe para nao haver um segundo filtro escrito
    a mao em cada conta — era `a['serve']` em quatro lugares, e trava nova
    entraria em tres deles (20.7).
    """
    return bool(a.get('serve')) and not a.get('repetido_por')


def marcar_repeticao_da_loja(bloco, dizer=False):
    """Marca como repetida a oferta que a MESMA loja anuncia duas vezes.

    Devolve a lista dos anuncios marcados. Recalcula do zero: a marca de ontem
    e apagada antes, porque ela e derivada do preco de HOJE (ver o comentario
    acima). `dizer=True` imprime cada marca — a secao 8 nao admite que uma
    passada deixe oferta de fora em silencio.
    """
    for a in bloco.get('anuncios') or []:
        a.pop('repetido_por', None)

    grupos = {}
    for a in bloco.get('anuncios') or []:
        # SO QUEM TEM PRECO E JULGADO: sem preco nao ha "mais barato" a medir, e
        # anuncio sem preco ja nao entra na faixa nem no carrossel. Inventar um
        # criterio de desempate para ele seria escolher no escuro.
        if not a.get('serve') or a.get('preco') is None:
            continue
        chave = (a.get('shop_id'), rel.chave_de_oferta_da_loja(a.get('titulo')))
        if not chave[1]:
            continue
        grupos.setdefault(chave, []).append(a)

    marcados = []
    for (shop_id, _), grupo in sorted(grupos.items(), key=lambda kv: str(kv[0])):
        if len(grupo) < 2:
            continue
        grupo = sorted(grupo, key=lambda a: (a['preco'], int(a.get('item_id') or 0)))
        fica = grupo[0]
        for a in grupo[1:]:
            diferenca = round(a['preco'] - fica['preco'], 2)
            a['repetido_por'] = {
                'causa': CAUSA_DA_REPETICAO,
                'mesmo_que': fica.get('item_id'),
                'mais_caro_em_brl': diferenca,
                # COMO FOI MEDIDO, EM PALAVRAS, NO PROPRIO REGISTRO: e a
                # exigencia que a 25.10 poe no degrau de compra, e ela vale
                # igual aqui — marca que ninguem consegue reauditar e marca que
                # ninguem vai desfazer no dia em que estiver errada.
                'como_foi_medido': (
                    'a loja %s (shop_id %s) anuncia os itens %s e %s com o MESMO nome '
                    'depois de tirada a cabeca de campanha do titulo, e quem declarou '
                    'que a cabeca nao e nome foi ela mesma, publicando as duas formas. '
                    'Ficou o mais barato (R$ %s contra R$ %s). A identidade e de UMA '
                    'loja so: titulo parecido entre lojas NAO e prova, e esta ilha nao '
                    'a usa (25.9).'
                    % (a.get('loja'), shop_id, fica.get('item_id'), a.get('item_id'),
                       ('%.2f' % fica['preco']).replace('.', ','),
                       ('%.2f' % a['preco']).replace('.', ','))),
            }
            marcados.append(a)
            if dizer:
                print('  REPETIDA: a loja %s anuncia o item %s pelo mesmo nome do item '
                      '%s e R$ %s mais caro; fica o mais barato.'
                      % (a.get('loja'), a.get('item_id'), fica.get('item_id'),
                         ('%.2f' % diferenca).replace('.', ',')))

    return marcados


def numero_proprio(pedido, anuncios):
    servem = [a for a in anuncios if entra_na_pagina(a) and a.get('preco') is not None]
    if pedido != 'faixa_de_preco':
        return (None, 'forma de numero proprio nao implementada: %r' % pedido)
    if len(servem) < PISO_DA_30_2:
        return (None, 'menos de %d anuncios com preco' % PISO_DA_30_2)
    precos = sorted(a['preco'] for a in servem)

    return ({
        'de': precos[0],
        'ate': precos[-1],
        'mediana': round(statistics.median(precos), 2),
        'sobre_quantas_ofertas': len(precos),
    }, None)


def contagem_de_rotulo(anuncios):
    """Quantos titulos declaram watt, e quantos dizem QUAL watt e."""
    conta = {'sem_watt': 0, 'watt_sem_rotulo': 0, 'nominal': 0, 'pico': 0, 'os_dois': 0}
    for a in anuncios:
        if entra_na_pagina(a):
            conta[a['rotulo_de_potencia']] = conta.get(a['rotulo_de_potencia'], 0) + 1
    conta['declaram_watt'] = (conta['watt_sem_rotulo'] + conta['nominal']
                              + conta['pico'] + conta['os_dois'])
    conta['dizem_qual_watt'] = conta['nominal'] + conta['pico'] + conta['os_dois']

    return conta


# ---------------------------------------------------------------------------
# A COLETA
# ---------------------------------------------------------------------------
# A Open API devolve `priceMin` como TEXTO ("1399.90"), nao como numero. Quem
# nao converter soma preco com `+` e concatena, ou chama `round()` num str e
# morre — foi o que esta ferramenta fez na primeira passada. A conversao e
# estrita de proposito: preco que nao vira numero vira `None` com o motivo, e o
# anuncio deixa de contar para a faixa em vez de entrar com zero.
# ---------------------------------------------------------------------------
# A QUARENTENA DO ANUNCIO APOSENTADO — e ela mora AQUI, e nao na ferramenta que
# aposenta, por um motivo so: e ESTE arquivo que reescreve o bloco inteiro a
# partir da API. Sem a quarentena no caminho do `--gravar`, o anuncio esgotado
# VOLTA na proxima coleta, com o mesmo id, como oferta viva — e o conserto de
# 11/11/2026 se desfaria calado na primeira coleta seguinte.
#
# O ID DO APOSENTADO NAO VIVE EM CAMPO NENHUM, por desenho (item 1 do despacho
# de 11/11/2026: "zero ocorrencia em campo vivo do banco"). Ele vive DENTRO da
# prosa da quarentena, num formato fechado, e e de la que esta funcao o le.
# Prosa que e tambem a lista de quarentena nao envelhece separada da historia.
# O FORMATO FECHADO DA LINHA DE QUARENTENA (25.11), E ELE GANHOU O ROTULO CURTO
# DA CAUSA EM 16/11/2026. A linha ja guardava a causa em PROSA, e prosa nao se
# conta: a frase de leitor que a 25.11 exige — *"outra saiu da lista depois dessa
# leitura: a loja mostrava o produto como esgotado"* — era servida IGUAL para as
# duas causas, e desde 13/11 ela publicava `esgotado` para um anuncio cuja ficha
# devolve "O produto nao existe". A 25.11 pede a causa EM PALAVRAS na tela, e
# tela que diz a causa errada e pior que tela calada. O rotulo e o que a contagem
# le; a prosa continua sendo a historia.
CAUSAS_DE_APOSENTADORIA = {
    'esgotado': 'a loja mostrava o produto como esgotado',
    'produto-nao-existe': 'a pagina do produto ja nao existia na loja',
}

PADRAO_APOSENTADO = re.compile(
    r'^APOSENTADO EM (?P<em>\d{4}-\d{2}-\d{2}) — item (?P<item>\d+) '
    r'da loja (?P<loja>\d+) — .*CAUSA \((?P<causa>[a-z][a-z-]*)\): .+ '
    r'\|\| ULTIMA MEDICAO: .+$', re.S)


def aposentados_de(bloco):
    return list(bloco.get('anuncios_aposentados') or [])


def causas_em_quarentena(bloco):
    """{rotulo_da_causa: quantos} lido da prosa da quarentena deste bloco.

    E daqui que sai a contagem que a tela usa para dizer a causa EM PALAVRAS
    (25.11). Ela mora no dono do arquivo e e USADA por quem precisa, nunca
    copiada (20.7).
    """
    contagem = {}
    for linha in aposentados_de(bloco):
        m = PADRAO_APOSENTADO.match((linha or '').strip())
        if m:
            causa = m.group('causa')
            contagem[causa] = contagem.get(causa, 0) + 1
    return contagem


def ids_em_quarentena(bloco):
    """Os `item_id` aposentados deste bloco, lidos da prosa da quarentena."""
    ids = set()
    for linha in aposentados_de(bloco):
        m = PADRAO_APOSENTADO.match((linha or '').strip())
        if m:
            ids.add(int(m.group('item')))
    return ids


def recontar_resumo(bloco):
    """Reconta o `resumo` sobre os anuncios que SOBRARAM no bloco.

    `ofertas_lidas` e `ofertas_recusadas` NAO entram: sao fato da coleta do dia
    em que ela aconteceu. O que esta funcao reconta e o que serve HOJE — e e por
    isso que ela e uma funcao, chamada pelo `--gravar` daqui e pela ferramenta
    que aposenta anuncio: duas contas do mesmo numero comecam iguais e so uma
    sobe (20.7).
    """
    r = bloco['resumo']
    # A MARCA DA REPETICAO E REFEITA AQUI, ANTES DE QUALQUER CONTA, e nao na
    # ferramenta que a aplica: e esta funcao que todo caminho de escrita chama
    # (o `--gravar` daqui, a ferramenta que aposenta anuncio e a que reaplica a
    # regua), e marca derivada que depende de alguem se lembrar de a refazer nao
    # se refaz. A ordem importa: a repeticao se mede sobre quem SERVE e as
    # contas se fazem sobre quem ENTRA.
    repetidos = marcar_repeticao_da_loja(bloco)
    servem = [x for x in bloco['anuncios'] if entra_na_pagina(x)]
    com_link = [x for x in servem if x.get('url_afiliado')]
    num, motivo = numero_proprio(r.get('numero_proprio_pedido'), bloco['anuncios'])
    r['ofertas_que_servem'] = len(servem)
    r['ofertas_com_link_de_afiliado'] = len(com_link)
    r['ofertas_aposentadas'] = len(aposentados_de(bloco))
    # QUANTAS FICARAM DE FORA POR REPETICAO DA PROPRIA LOJA. Vai para a tela
    # porque sem ela a conta do leitor (lidas menos recusadas menos aposentadas)
    # NAO FECHA com o tamanho da tabela — a mesma razao pela qual
    # `ofertas_aposentadas` existe, e conta que nao fecha na tela e pior que
    # conta ausente.
    r['ofertas_repetidas_pela_loja'] = len(repetidos)
    r['numero_proprio'] = num
    r['motivo_sem_numero_proprio'] = motivo
    r['contagem_de_rotulo_de_potencia'] = contagem_de_rotulo(bloco['anuncios'])
    r['abre_o_portao_da_30_2'] = len(com_link) >= PISO_DA_30_2 and num is not None
    return r


def aplicar_quarentena(novo_bloco, bloco_antigo):
    """Carrega a quarentena do bloco antigo e RECUSA o anuncio que ela nomeia.

    Devolve quantos anuncios foram recusados. Imprime cada recusa (secao 8): o
    que uma coleta deixa de fora em silencio e o que a passada seguinte
    redescobre do zero.
    """
    quarentena = ids_em_quarentena(bloco_antigo or {})
    if not quarentena:
        return 0
    novo_bloco['anuncios_aposentados'] = aposentados_de(bloco_antigo)
    fora = [a for a in novo_bloco['anuncios'] if int(a.get('item_id') or 0) in quarentena]
    for a in fora:
        print('  QUARENTENA: a loja devolveu de novo o item %s (%s) e ele esta APOSENTADO; '
              'nao entra.' % (a.get('item_id'), (a.get('titulo') or '')[:60]))
    if fora:
        novo_bloco['anuncios'] = [a for a in novo_bloco['anuncios']
                                  if int(a.get('item_id') or 0) not in quarentena]
    recontar_resumo(novo_bloco)
    return len(fora)


def preco_numero(bruto):
    try:
        return round(float(str(bruto).replace(',', '.')), 2)
    except (TypeError, ValueError):
        return None


def julgar_oferta(oferta, familia, chave, degrau):
    titulo = oferta.get('titulo') or ''
    # A TRADUCAO DE `familia` PARA ARGUMENTOS MORA NA REGUA, numa funcao so, e
    # nao aqui — ela estava escrita duas vezes neste arquivo (aqui e no
    # `conferir()`), e a trava nova de 16/11 entraria em uma delas e deixaria o
    # portao conferindo com a regua velha, ou seja aprovando (20.7).
    serve, por, faltou, atendidas = rel.julgar_declaracao(titulo, familia)

    return {
        'item_id': oferta.get('item_id'),
        'shop_id': oferta.get('shop_id'),
        'titulo': titulo,
        'preco': preco_numero(oferta.get('preco_min')),
        'moeda': 'BRL',
        'loja': oferta.get('loja'),
        'nota': oferta.get('nota'),
        'vendas': oferta.get('vendas'),
        'tipo_de_loja': oferta.get('tipo_de_loja'),
        'url_bruto_da_imagem': oferta.get('imagem_url'),
        'imagem': None,
        'motivo_sem_imagem': 'foto nao medida nesta passada',
        'url_produto': oferta.get('url_produto'),
        'url_afiliado': None,
        'motivo_sem_link': 'encurtamento nao tentado nesta passada',
        'sub_id_1': SUB_ID_1,
        'sub_id_2': None,
        'fonte': 'anuncio-shopee',
        'coletado_em': HOJE,
        'chave_que_achou': chave,
        'degrau_da_escada': degrau,
        'serve': serve,
        'recusado_por': por,
        'exigencia_que_faltou': faltou,
        'exigencias_atendidas': atendidas,
        'rotulo_de_potencia': rel.rotulo_de_potencia(titulo),
    }


def colher_consulta(c, api, com_link):
    """Sobe a escada de chaves e para no primeiro degrau que alcanca o piso."""
    escada_medida = []
    escolhido = None

    for passo in c['escada_de_chaves']:
        chave, degrau = passo['chave'], passo['degrau']
        ofertas = api.buscar(chave, quantos=QUANTOS)
        julgadas = [julgar_oferta(o, c['familia'], chave, degrau) for o in ofertas]
        servem = sum(1 for a in julgadas if a['serve'])
        escada_medida.append({
            'degrau': degrau,
            'chave': chave,
            'ofertas_lidas': len(ofertas),
            'ofertas_que_servem': servem,
            'alcancou_o_piso': servem >= PISO_DA_30_2,
            'medido_em': HOJE,
        })
        if servem >= PISO_DA_30_2 and escolhido is None:
            escolhido = (chave, degrau, julgadas)
            break
        time.sleep(PAUSA)

    if escolhido is None:
        return {'escada_medida': escada_medida, 'anuncios': [], 'chave_escolhida': None}

    chave, degrau, julgadas = escolhido

    # A FOTO E MEDIDA SO PARA QUEM SERVE. A 32.1 pede foto no cartao e a secao 6
    # manda que produto sem foto apareca com espaco reservado neutro, nunca que
    # ele suma — e a 32.5-d, escrita nesta ilha HOJE, mostra por que a dimensao
    # nao pode ser digitada: reservado e foto sao CSS diferente, e a medicao de
    # pixel feita sobre o reservado nao vale para a foto.
    for a in julgadas:
        if not a['serve']:
            a['imagem'] = None
            a['motivo_sem_imagem'] = 'anuncio recusado: foto nao e medida para quem nao serve'
            continue
        dim, erro = medir_foto(a.get('url_bruto_da_imagem'))
        if dim:
            a['imagem'] = {
                'url': a['url_bruto_da_imagem'],
                'largura': dim[0],
                'altura': dim[1],
                # SEM A CABECA DE CAMPANHA (16/11/2026): o `alt` e texto de
                # pagina, e `11.11` nao e nome de veiculo. O titulo cru da loja
                # segue ao lado, no campo `titulo`, que e a procedencia.
                'alt': rel.nome_do_anuncio(a['titulo'])[:120],
                'fonte': 'anuncio-shopee',
                'coletado_em': HOJE,
                'como_a_dimensao_foi_medida': 'cabecalho do arquivo na CDN, nunca digitada',
            }
            a['motivo_sem_imagem'] = None
        else:
            a['imagem'] = None
            a['motivo_sem_imagem'] = erro
        a.pop('url_bruto_da_imagem', None)
        time.sleep(PAUSA / 2)
    for a in julgadas:
        a.pop('url_bruto_da_imagem', None)

    if com_link:
        sub2 = sub_id_2_de(c['id'])
        for a in julgadas:
            if not a['serve'] or not a['url_produto']:
                a['motivo_sem_link'] = ('anuncio recusado: link nao e gerado para quem nao serve'
                                        if not a['serve'] else 'anuncio sem url de produto')
                continue
            try:
                curto = api.encurtar(a['url_produto'], SUB_ID_1, sub2)
                a['url_afiliado'] = curto
                a['sub_id_2'] = sub2
                a['url_afiliado_gerada_em'] = HOJE
                a['motivo_sem_link'] = None
            except Exception as e:                         # noqa: BLE001
                a['motivo_sem_link'] = 'encurtamento falhou: %s' % type(e).__name__
            time.sleep(PAUSA)

    return {'escada_medida': escada_medida, 'anuncios': julgadas,
            'chave_escolhida': chave, 'degrau_escolhido': degrau}


def montar(c, colhido):
    anuncios = colhido['anuncios']
    servem = [a for a in anuncios if a['serve']]
    # A 25.2-b: publicavel exige piso de compra TENTADO. Aqui o piso e o proprio
    # anuncio, e `com_link` sem link gerado nao abre o portao.
    com_link = [a for a in servem if a.get('url_afiliado')]
    num, motivo = numero_proprio(c.get('numero_proprio_pedido'), anuncios)
    recusas = {}
    for a in anuncios:
        if not a['serve']:
            recusas[a['recusado_por']] = recusas.get(a['recusado_por'], 0) + 1

    return {
        'id': c['id'],
        'consulta': c['consulta'],
        'slug': c['slug'],
        'publicar_declarado': bool(c.get('publicar_declarado')),
        'colhido_em': HOJE,
        'canal': 'API de afiliado da Shopee (productOfferV2), credencial no ambiente',
        'chave_escolhida': colhido['chave_escolhida'],
        'degrau_escolhido': colhido.get('degrau_escolhido'),
        'escada_medida': colhido['escada_medida'],
        'resumo': {
            'ofertas_lidas': len(anuncios),
            'ofertas_que_servem': len(servem),
            'ofertas_recusadas': len(anuncios) - len(servem),
            'recusas_por_causa': recusas,
            'ofertas_com_link_de_afiliado': len(com_link),
            'abre_o_portao_da_30_2': len(com_link) >= PISO_DA_30_2 and num is not None,
            'numero_proprio_pedido': c.get('numero_proprio_pedido'),
            'numero_proprio': num,
            'motivo_sem_numero_proprio': motivo,
            'contagem_de_rotulo_de_potencia': contagem_de_rotulo(anuncios),
        },
        'anuncios': anuncios,
    }


# ---------------------------------------------------------------------------
# `--conferir`: sem rede, reaplica a regua e refaz as contas
# ---------------------------------------------------------------------------
def conferir():
    if not os.path.exists(BANCO):
        print('REPROVADO: %s nao existe' % os.path.basename(BANCO))
        return 1
    with open(BANCO, encoding='utf-8') as f:
        banco = json.load(f)
    decl = {c['id']: c for c in declaracao()['consultas']}

    falhas, afirmacoes = [], 0
    for bloco in banco['consultas']:
        c = decl.get(bloco['id'])
        afirmacoes += 1
        if not c:
            falhas.append('%s: colhido e nao declarado em consultas-de-produto.json' % bloco['id'])
            continue
        if not c.get('familia'):
            falhas.append('%s: colhido e a declaracao nao tem `familia`' % bloco['id'])
            continue

        for a in bloco['anuncios']:
            afirmacoes += 1
            serve, por, faltou, _ = rel.julgar_declaracao(a['titulo'], c['familia'])
            if serve != a['serve'] or por != a['recusado_por'] or faltou != a['exigencia_que_faltou']:
                # A MENSAGEM IMPRIME AS TRES COISAS QUE A COMPARACAO LE, e isto
                # foi consertado em 03/11/2026 porque ela imprimia DUAS: a
                # comparacao sempre leu `exigencia_que_faltou`, e quando era so
                # ela que divergia a linha saia dizendo
                # `gravado (False/acessorio) discorda do calculado
                # (False/acessorio)` — o portao acusando a divergencia certa e
                # escondendo QUAL campo divergiu, com os dois lados impressos
                # identicos. Aconteceu na mesma passada que trocou a ordem da
                # lista de `acessorio`: a palavra que recusa mudou, o nome do
                # grupo nao. Portao que nao imprime o campo que ele compara faz
                # quem o le duvidar do portao em vez do dado (20.5).
                falhas.append('%s / %s: veredito gravado (%s/%s/%s) discorda do calculado (%s/%s/%s)'
                              % (bloco['id'], a['item_id'],
                                 a['serve'], a['recusado_por'], a['exigencia_que_faltou'],
                                 serve, por, faltou))
            afirmacoes += 1
            if rel.rotulo_de_potencia(a['titulo']) != a['rotulo_de_potencia']:
                falhas.append('%s / %s: rotulo de potencia gravado discorda do calculado'
                              % (bloco['id'], a['item_id']))

        # A CHAVE GRAVADA TEM DE SER UMA DAS DECLARADAS, e todo anuncio tem de
        # ter sido achado por ELA. Sem isto o degrau viaja como enfeite: a
        # 25.6(a) manda registrar em qual degrau a escada parou porque e
        # procedencia, e procedencia que ninguem confere e prosa.
        declaradas = [p['chave'] for p in (c.get('escada_de_chaves') or [])]
        afirmacoes += 1
        if bloco['chave_escolhida'] not in declaradas:
            falhas.append('%s: chave escolhida %r nao esta na escada declarada %r'
                          % (bloco['id'], bloco['chave_escolhida'], declaradas))
        for a in bloco['anuncios']:
            afirmacoes += 1
            if a['chave_que_achou'] != bloco['chave_escolhida']:
                falhas.append('%s / %s: achado por %r e a chave do bloco e %r'
                              % (bloco['id'], a['item_id'], a['chave_que_achou'],
                                 bloco['chave_escolhida']))

        r = bloco['resumo']
        num, motivo = numero_proprio(r.get('numero_proprio_pedido'), bloco['anuncios'])
        afirmacoes += 1
        if num != r.get('numero_proprio'):
            falhas.append('%s: numero proprio gravado %r nao refaz: %r'
                          % (bloco['id'], r.get('numero_proprio'), num))
        afirmacoes += 1
        if motivo != r.get('motivo_sem_numero_proprio'):
            falhas.append('%s: motivo_sem_numero_proprio gravado %r nao refaz: %r'
                          % (bloco['id'], r.get('motivo_sem_numero_proprio'), motivo))
        afirmacoes += 1
        if contagem_de_rotulo(bloco['anuncios']) != r.get('contagem_de_rotulo_de_potencia'):
            falhas.append('%s: contagem de rotulo de potencia nao refaz' % bloco['id'])

        # A MARCA DA REPETICAO GRAVADA TEM DE SER A QUE A REGRA REFAZ. Este
        # portao le o arquivo como ele esta no disco, entao sem esta afirmacao
        # um banco editado a mao — marca apagada, marca posta no anuncio errado
        # — passaria verde: as contas abaixo concordariam com o resumo porque as
        # duas leriam a MESMA marca errada. A regra nao e repetida aqui; ela e
        # chamada, e o que se confere e o arquivo contra ela.
        marcados_no_disco = sorted(int(a.get('item_id') or 0) for a in bloco['anuncios']
                                   if a.get('repetido_por'))
        marcados_pela_regra = sorted(int(a.get('item_id') or 0)
                                     for a in marcar_repeticao_da_loja(
                                         json.loads(json.dumps(bloco))))
        afirmacoes += 1
        if marcados_no_disco != marcados_pela_regra:
            falhas.append('%s: a repeticao da loja gravada e %s e a regra refaz %s'
                          % (bloco['id'], marcados_no_disco, marcados_pela_regra))

        # QUEM ENTRA NA PAGINA, E NAO QUEM SERVE: a conta e refeita aqui por um
        # caminho proprio (a terceira conta que a secao 8 pede), mas a PERGUNTA
        # e a mesma que o resumo responde. Contar `serve` aqui mediria uma coisa
        # e o resumo outra, e o portao reprovaria a pagina certa.
        servem = [a for a in bloco['anuncios'] if entra_na_pagina(a)]
        com_link = [a for a in servem if a.get('url_afiliado')]
        afirmacoes += 1
        if len(servem) != r['ofertas_que_servem']:
            falhas.append('%s: ofertas_que_servem gravado %d, contado %d'
                          % (bloco['id'], r['ofertas_que_servem'], len(servem)))
        afirmacoes += 1
        if len(com_link) != r['ofertas_com_link_de_afiliado']:
            falhas.append('%s: ofertas_com_link_de_afiliado gravado %d, contado %d'
                          % (bloco['id'], r['ofertas_com_link_de_afiliado'], len(com_link)))
        afirmacoes += 1
        abre = len(com_link) >= PISO_DA_30_2 and num is not None
        if abre != r['abre_o_portao_da_30_2']:
            falhas.append('%s: abre_o_portao_da_30_2 gravado %s, calculado %s'
                          % (bloco['id'], r['abre_o_portao_da_30_2'], abre))
        # O link de afiliado e `sponsored` e vai para o visitante: ele nunca pode
        # sair sem o sub-id da ilha, senao a venda chega sem dono (secao 7).
        for a in com_link:
            afirmacoes += 1
            if a.get('sub_id_1') != SUB_ID_1 or not a.get('sub_id_2'):
                falhas.append('%s / %s: link de afiliado sem sub-id completo'
                              % (bloco['id'], a['item_id']))
        # A 32.5-d, escrita nesta ilha em 29/10/2026: dimensao de foto DIGITADA
        # e da familia do numero de tela digitado. Ou ela foi medida no cabecalho
        # do arquivo, ou a foto nao entra e a causa esta escrita.
        for a in servem:
            afirmacoes += 1
            img = a.get('imagem')
            if img:
                if not (isinstance(img.get('largura'), int) and img['largura'] > 0
                        and isinstance(img.get('altura'), int) and img['altura'] > 0):
                    falhas.append('%s / %s: imagem sem largura e altura MEDIDAS'
                                  % (bloco['id'], a['item_id']))
            elif not (a.get('motivo_sem_imagem') or '').strip():
                falhas.append('%s / %s: sem imagem e sem causa escrita'
                              % (bloco['id'], a['item_id']))

    # A declaracao nao pode prometer pagina para consulta que nao foi colhida.
    colhidas = {b['id'] for b in banco['consultas']}
    for c in declaracao()['consultas']:
        afirmacoes += 1
        if c.get('publicar_declarado') and c['id'] not in colhidas:
            falhas.append('%s: `publicar_declarado` e nao foi colhida' % c['id'])
        afirmacoes += 1
        if not c.get('publicar_declarado') and not (c.get('motivo_para_nao_publicar_agora') or '').strip():
            falhas.append('%s: nao publica e nao diz por que' % c['id'])

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')

    return 1 if falhas else 0


# ---------------------------------------------------------------------------
def laudo(bloco):
    r = bloco['resumo']
    print('\n=== %s (%s)' % (bloco['consulta'], bloco['id']))
    for e in bloco['escada_medida']:
        print('  degrau %d  %-34s lidas=%2d servem=%2d piso=%s'
              % (e['degrau'], e['chave'], e['ofertas_lidas'], e['ofertas_que_servem'],
                 'SIM' if e['alcancou_o_piso'] else 'nao'))
    print('  chave escolhida: %r (degrau %s)' % (bloco['chave_escolhida'], bloco['degrau_escolhido']))
    print('  servem %d · recusadas %d %s' % (r['ofertas_que_servem'], r['ofertas_recusadas'],
                                             r['recusas_por_causa']))
    print('  com link de afiliado: %d · abre o portao da 30.2: %s'
          % (r['ofertas_com_link_de_afiliado'], r['abre_o_portao_da_30_2']))
    print('  numero proprio: %s %s' % (r['numero_proprio'], r['motivo_sem_numero_proprio'] or ''))
    print('  rotulo de potencia: %s' % r['contagem_de_rotulo_de_potencia'])
    for a in bloco['anuncios']:
        print('   %s %-9s v=%-4s %s' % ('ok ' if a['serve'] else 'X  ',
                                        a['preco'], a['vendas'], a['titulo'][:76]))
        if not a['serve']:
            print('        recusado_por=%s (%s)' % (a['recusado_por'], a['exigencia_que_faltou']))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--ensaio', action='store_true')
    g.add_argument('--gravar', action='store_true')
    g.add_argument('--conferir', action='store_true')
    p.add_argument('--so', help='colhe so esta consulta, pelo id')
    p.add_argument('--sem-link', action='store_true',
                   help='nao chama o encurtador')
    a = p.parse_args()

    if a.conferir:
        return conferir()

    d = declaracao()
    alvos = [c for c in d['consultas']
             if c.get('publicar_declarado') and c.get('familia') and c.get('escada_de_chaves')]
    if a.so:
        alvos = [c for c in alvos if c['id'] == a.so]
        if not alvos:
            print('nada a colher com --so %r' % a.so)
            return 1

    api = shopee()
    blocos = []
    for c in alvos:
        colhido = colher_consulta(c, api, com_link=not a.sem_link)
        bloco = montar(c, colhido)
        blocos.append(bloco)
        laudo(bloco)

    if a.ensaio:
        print('\n--ensaio: nada foi gravado.')
        return 0

    antigo = {}
    if os.path.exists(BANCO):
        with open(BANCO, encoding='utf-8') as f:
            antigo = {b['id']: b for b in json.load(f).get('consultas', [])}
    for b in blocos:
        # A QUARENTENA ATRAVESSA A COLETA. Ver `aplicar_quarentena`.
        aplicar_quarentena(b, antigo.get(b['id']))
        antigo[b['id']] = b

    saida = {
        'id': 'anuncios-por-consulta',
        'ilha': 'rodametria',
        'bloco': '5b',
        'gerado_em': HOJE,
        'gerado_por': 'ferramentas/coletar-por-consulta.py',
        'o_que_este_arquivo_e': (
            'O dado COMERCIAL das consultas de produto da secao 30: os anuncios lidos na '
            'Open API de afiliados da Shopee, com o veredito da regua de relevancia por '
            'anuncio, a escada de chaves medida, o numero proprio contado e a contagem do '
            'rotulo de potencia. Dado TECNICO nao entra aqui: titulo de anuncio e nivel 6 e '
            'o `niveis_minimos_por_campo` do esquema exige nivel 5 ou melhor em watt, '
            'velocidade, acelerador e carga maxima.'),
        'abre_o_portao_NAO_e_o_mesmo_que_publica': (
            '`abre_o_portao_da_30_2` diz que a consulta tem tres anuncios que servem COM link '
            'de afiliado e um numero proprio contado. Quem decide se a pagina nasce e a '
            'declaracao (`publicar_declarado`) mais este portao, os dois.'),
        'o_que_decide_o_veredito': 'ferramentas/teste-relevancia-do-anuncio.py',
        'consultas': [antigo[k] for k in sorted(antigo)],
    }
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(saida, f, ensure_ascii=False, indent=RECUO_DO_BANCO)
        f.write('\n')
    print('\ngravado: %s (%d consulta(s))' % (os.path.basename(BANCO), len(saida['consultas'])))

    return 0


if __name__ == '__main__':
    sys.exit(main())

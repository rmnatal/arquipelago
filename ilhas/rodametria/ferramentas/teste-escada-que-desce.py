#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A ESCADA DESCE PELA REGUA QUE PUBLICA, E NAO PELA MAIS FROUXA (18/11/2026).

    python3 ferramentas/teste-escada-que-desce.py

O DEFEITO QUE ELE EXISTE PARA IMPEDIR FOI MEDIDO NO AR, e nao suposto. As
10h2xZ de 18/11/2026, na recoleta de `/veiculos/moto-eletrica/` — a cabeca de
823 mil buscas/mes, nascida dois dias antes:

  * o degrau 1 (`moto eletrica adulto`) devolveu 20 ofertas e TRES passaram na
    regua de relevancia, entao `alcancou_o_piso` saiu `True` e a escada PAROU;
  * uma das tres era o item 23598774355, APOSENTADO em 16/11 pela 25.11 — a
    ficha dele serve "O produto nao existe" —, e `atravessar_a_coleta`, que roda
    DEPOIS, o recusou;
  * o bloco fechou com DOIS anuncios, abaixo do piso de tres da 30.2, e a pagina
    caiu para o estado degradado de `rdm_produto_pagina_html()`;
  * e o degrau 2 da escada declarada (`moto eletrica`, a consulta crua) NUNCA FOI
    CONSULTADO, porque a escada ja havia parado no de cima.

A pagina de maior volume do nicho degradou com um degrau inteiro por medir, e a
causa nao era a loja: era a aritmetica. A 20.7 em traje de escada — **duas
contas do mesmo numero comecando diferentes, e a que decidia era a mais
frouxa.** `colher_consulta()` contava `a['serve']`; quem publica conta
`entra_na_pagina()` mais a quarentena.

POR QUE ELE E PYTHON E NAO PHP: a decisao e tomada em Python, dentro de
`coletar-por-consulta.py`, e esta regua CHAMA a funcao que decide
(`quantos_entram_no_degrau`) em vez de reescrever o critério. Regua que refaz a
conta a mao mede a copia e nunca a decisao.

AS SEIS METADES:
  1. O MUNDO DO DIA (18/11): 3 que servem, 1 aposentado -> 2 entram -> a escada
     DESCE e consulta o degrau 2.
  2. O MUNDO DA DEDUPE (25.9): 3 que servem, 2 da mesma loja com o mesmo nome ->
     2 entram -> desce. Causa diferente, mesma aritmetica.
  3. O MUNDO QUE PASSA: 3 que entram de verdade -> PARA no degrau 1. Sem ele
     este portao aprovaria uma trava que barra tudo, que nao e conserto.
  4. O MUNDO DO ZERO, que e o comportamento de antes e nao pode ter sido
     quebrado: degrau sem nenhuma oferta que serve -> desce.
  5. A ESCADA ESGOTADA: nenhum degrau alcanca -> `chave_escolhida` None, sem
     excecao e sem bloco meio montado.
  6. O MUNDO DA DISCORDANCIA (20.8): a regua VELHA e refeita aqui e OBRIGADA a
     discordar da nova nos mundos 1 e 2, e a concordar nos mundos 3 e 4.
     Autoteste em que as duas concordam sempre nao mede conserto nenhum.
"""

import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


col = _modulo('coletor', os.path.join(AQUI, 'coletar-por-consulta.py'))

FALHAS = []
AFIRMACOES = [0]


def afirmar(condicao, frase):
    AFIRMACOES[0] += 1
    if not condicao:
        FALHAS.append(frase)


# ---------------------------------------------------------------------------
# O MUNDO DE MENTIRA — a familia e a escada sao as REAIS da moto, lidas da
# declaracao, para o portao nao medir uma familia que nao existe.
# ---------------------------------------------------------------------------

def familia_da_moto():
    for c in col.declaracao()['consultas']:
        if c['id'] == 'moto-eletrica':
            return c['familia'], c['escada_de_chaves']
    raise SystemExit('a consulta moto-eletrica saiu da declaracao')


# O ID E A LINHA DE QUARENTENA SAO OS REAIS do bloco no banco, lidos e nunca
# digitados: no dia em que a quarentena desta consulta mudar, estas afirmacoes
# mudam com ela, e e o que se quer.
def quarentena_real():
    for c in col.declaracao.__globals__['json'].load(
            open(col.BANCO, encoding='utf-8'))['consultas']:
        if c['id'] == 'moto-eletrica':
            return c
    raise SystemExit('o bloco moto-eletrica saiu do banco')


class ApiDeMentira(object):
    """Devolve, por chave, as ofertas que o mundo daquele teste declara."""

    def __init__(self, por_chave):
        self.por_chave = por_chave
        self.chaves_pedidas = []

    def buscar(self, chave, quantos=20):
        self.chaves_pedidas.append(chave)
        return list(self.por_chave.get(chave, []))


def oferta(item_id, titulo, preco, shop_id=1):
    """Uma oferta no formato que `julgar_oferta` recebe da Open API.

    O CAMPO DO PRECO E `preco_min`, E ESTE PORTAO JA ERROU ISSO: a primeira
    versao o chamou de `preco`, `julgar_oferta` leu `None` e o mundo 2 passou a
    nao medir a dedupe — que pula, de proposito, quem nao tem preco. Mundo de
    mentira com campo errado aprova em silencio, e foi a propria bateria que o
    acusou, porque o mundo 3 continuou certo e o 2 nao.
    """
    return {
        'item_id': item_id,
        'shop_id': shop_id,
        'titulo': titulo,
        'preco_min': '%.2f' % preco,   # a Open API devolve TEXTO, nunca numero
        'loja': 'loja %s' % shop_id,
        'nota': '0',
        'vendas': 0,
        'tipo_de_loja': [],
        'imagem_url': None,
        'url_produto': 'https://shopee.com.br/product/%s/%s' % (shop_id, item_id),
    }


# Tres titulos que PASSAM na familia da moto (`moto` + `eletric` + `adulto`), e
# um quarto para o degrau de baixo. Sao da forma dos titulos reais medidos.
T1 = 'Moto Elétrica Adulto Alfa 1000W 60V 20Ah Velocidade Max 32km h'
T2 = 'Moto Elétrica Adulto Beta 2000W 72V 30Ah Off Road Trilha'
T3 = 'Moto Elétrica Adulto Gama 1500W 60V 24Ah Freio a Disco'
T4 = 'Moto Elétrica Adulto Delta 800W 48V 12Ah Urbana'


def rodar(por_chave, bloco_antigo, com_link=False):
    familia, escada = familia_da_moto()
    c = {'id': 'moto-eletrica', 'familia': familia, 'escada_de_chaves': escada}
    api = ApiDeMentira(por_chave)
    # `time.sleep` da PAUSA nao serve a um portao sem rede: zero aqui e o que
    # faz a bateria caber em segundos.
    pausa = col.PAUSA
    col.PAUSA = 0
    try:
        colhido = col.colher_consulta(c, api, com_link=com_link,
                                      bloco_antigo=bloco_antigo)
    finally:
        col.PAUSA = pausa
    return colhido, api


def regua_velha(por_chave, escada):
    """A REGUA DE ANTES DE 18/11/2026, refeita aqui para poder DISCORDAR (20.8).

    Ela conta `a['serve']` e nada mais — nem quarentena, nem dedupe. Nao chama o
    coletor: se chamasse, herdaria o conserto e concordaria sempre, que e
    exatamente o autoteste que nao mede nada.
    """
    familia, _ = familia_da_moto()
    for passo in escada:
        julgadas = [col.julgar_oferta(o, familia, passo['chave'], passo['degrau'])
                    for o in por_chave.get(passo['chave'], [])]
        if sum(1 for a in julgadas if a['serve']) >= col.PISO_DA_30_2:
            return passo['degrau']
    return None


def main():
    familia, escada = familia_da_moto()
    d1 = escada[0]['chave']
    d2 = escada[1]['chave'] if len(escada) > 1 else None

    afirmar(len(escada) >= 2,
            'a escada declarada da moto tem menos de 2 degraus: o portao nao tem '
            'para onde descer e o mundo do defeito nao e reproduzivel')
    afirmar(col.PISO_DA_30_2 == 3,
            'o piso da 30.2 deixou de ser 3 (%r): as afirmacoes deste portao '
            'contam com ele' % col.PISO_DA_30_2)

    bloco = quarentena_real()
    aposentado = sorted(col.ids_em_quarentena(bloco))
    afirmar(len(aposentado) >= 1,
            'o bloco moto-eletrica do banco nao tem nenhum item em quarentena: o '
            'mundo 1 deste portao nasceu de um que tinha (23598774355, 16/11/2026)')
    ap = aposentado[0] if aposentado else 999

    # -----------------------------------------------------------------------
    # MUNDO 1 — O DIA 18/11: tres servem, uma esta APOSENTADA.
    # -----------------------------------------------------------------------
    m1 = {
        d1: [oferta(101, T1, 1000.0, shop_id=11),
             oferta(102, T2, 2000.0, shop_id=12),
             oferta(ap, T3, 15000.0, shop_id=13)],
        d2: [oferta(201, T1, 1100.0, shop_id=21),
             oferta(202, T2, 2100.0, shop_id=22),
             oferta(203, T3, 3100.0, shop_id=23),
             oferta(204, T4, 4100.0, shop_id=24)],
    }
    colhido, api = rodar(m1, bloco)
    e1 = colhido['escada_medida'][0]
    afirmar(e1['ofertas_que_servem'] == 3,
            'mundo 1: a regua de relevancia devia achar 3 que servem, achou %r'
            % e1['ofertas_que_servem'])
    afirmar(e1['ofertas_que_entram'] == 2,
            'mundo 1: com o aposentado %s fora, 2 entram; o degrau diz %r'
            % (ap, e1.get('ofertas_que_entram')))
    afirmar(e1['alcancou_o_piso'] is False,
            'mundo 1: o degrau 1 NAO alcanca o piso com 2 que entram, e ele diz '
            'que alcanca — e o defeito de 18/11/2026 de volta')
    afirmar(colhido['degrau_escolhido'] == 2,
            'mundo 1: a escada tinha de DESCER para o degrau 2, parou em %r'
            % colhido.get('degrau_escolhido'))
    afirmar(d2 in api.chaves_pedidas,
            'mundo 1: o degrau de baixo (%r) nunca foi consultado — e o custo '
            'exato medido na moto em 18/11' % d2)
    afirmar(len(colhido['escada_medida']) == 2,
            'mundo 1: a procedencia tem de guardar os DOIS degraus medidos, '
            'guardou %r' % len(colhido['escada_medida']))

    # -----------------------------------------------------------------------
    # MUNDO 2 — A DEDUPE DA 25.9: tres servem, duas da MESMA loja com o MESMO
    # nome. Causa diferente da do mundo 1, aritmetica identica.
    # -----------------------------------------------------------------------
    m2 = {
        d1: [oferta(301, T1, 1000.0, shop_id=31),
             oferta(302, T2, 2000.0, shop_id=32),
             oferta(303, T2, 2500.0, shop_id=32)],
        d2: [oferta(401, T1, 1100.0, shop_id=41),
             oferta(402, T2, 2100.0, shop_id=42),
             oferta(403, T3, 3100.0, shop_id=43)],
    }
    colhido2, api2 = rodar(m2, {})
    e2 = colhido2['escada_medida'][0]
    afirmar(e2['ofertas_que_servem'] == 3,
            'mundo 2: 3 passam na relevancia, a regua diz %r' % e2['ofertas_que_servem'])
    afirmar(e2['ofertas_que_entram'] == 2,
            'mundo 2: a mesma loja anuncia o mesmo nome duas vezes, logo 2 entram; '
            'o degrau diz %r' % e2.get('ofertas_que_entram'))
    afirmar(colhido2['degrau_escolhido'] == 2,
            'mundo 2: a escada tinha de descer pela dedupe da 25.9, parou em %r'
            % colhido2.get('degrau_escolhido'))

    # -----------------------------------------------------------------------
    # MUNDO 3 — O QUE PASSA: tres que entram de verdade. A escada PARA em cima.
    # -----------------------------------------------------------------------
    m3 = {
        d1: [oferta(501, T1, 1000.0, shop_id=51),
             oferta(502, T2, 2000.0, shop_id=52),
             oferta(503, T3, 3000.0, shop_id=53)],
        d2: [oferta(601, T4, 4000.0, shop_id=61)],
    }
    colhido3, api3 = rodar(m3, {})
    e3 = colhido3['escada_medida'][0]
    afirmar(e3['ofertas_que_entram'] == 3 and e3['alcancou_o_piso'] is True,
            'mundo 3: tres que entram tem de alcancar o piso (entram=%r, piso=%r)'
            % (e3.get('ofertas_que_entram'), e3['alcancou_o_piso']))
    afirmar(colhido3['degrau_escolhido'] == 1,
            'mundo 3: a escada tinha de PARAR no degrau 1, foi para %r'
            % colhido3.get('degrau_escolhido'))
    afirmar(d2 not in api3.chaves_pedidas,
            'mundo 3: o degrau de baixo foi consultado sem precisar — o conserto '
            'virou uma chamada de rede a mais por consulta')
    afirmar(len(colhido3['escada_medida']) == 1,
            'mundo 3: so o degrau 1 devia estar medido, estao %r'
            % len(colhido3['escada_medida']))

    # -----------------------------------------------------------------------
    # MUNDO 4 — O ZERO, que e o comportamento de antes do conserto.
    # -----------------------------------------------------------------------
    m4 = {
        d1: [oferta(701, 'Capacete de moto elétrica para adultos RGN', 102.09, shop_id=71)],
        d2: [oferta(801, T1, 1000.0, shop_id=81),
             oferta(802, T2, 2000.0, shop_id=82),
             oferta(803, T3, 3000.0, shop_id=83)],
    }
    colhido4, _ = rodar(m4, {})
    e4 = colhido4['escada_medida'][0]
    afirmar(e4['ofertas_que_servem'] == 0 and e4['ofertas_que_entram'] == 0,
            'mundo 4: capacete nao serve e nao entra (servem=%r, entram=%r)'
            % (e4['ofertas_que_servem'], e4.get('ofertas_que_entram')))
    afirmar(colhido4['degrau_escolhido'] == 2,
            'mundo 4: o degrau de zero sempre desceu, e tem de continuar descendo; '
            'parou em %r' % colhido4.get('degrau_escolhido'))

    # -----------------------------------------------------------------------
    # MUNDO 5 — A ESCADA ESGOTADA COM DADO NA MAO: nenhum degrau alcanca o piso,
    # mas um deles entrega 2. E o mundo REAL da moto em 18/11/2026, e antes
    # daquele dia este caminho devolvia VAZIO — jogando fora os dois anuncios
    # que a consulta tem. Vazio nao e mais honesto que dois: a pagina degrada
    # igual nos dois casos, e so um deles sabe dizer de quanto ela esta longe.
    # -----------------------------------------------------------------------
    m5 = {
        d1: [oferta(901, T1, 1000.0, shop_id=91),
             oferta(902, T2, 2000.0, shop_id=92)],
        d2: [oferta(903, T3, 3000.0, shop_id=93)],
    }
    colhido5, _ = rodar(m5, {})
    afirmar(colhido5['chave_escolhida'] == d1,
            'mundo 5: sem degrau que alcance, fica o que mais ENTREGA (%r), e a '
            'escada devolveu %r' % (d1, colhido5['chave_escolhida']))
    afirmar(len(colhido5['anuncios']) == 2,
            'mundo 5: os 2 anuncios lidos tem de sobreviver a escada esgotada, '
            'sobraram %r' % len(colhido5['anuncios']))
    afirmar(len(colhido5['escada_medida']) == 2,
            'mundo 5: os dois degraus medidos ficam gravados como procedencia '
            'mesmo sem nenhum alcancar; estao %r' % len(colhido5['escada_medida']))
    afirmar(all(not e['alcancou_o_piso'] for e in colhido5['escada_medida']),
            'mundo 5: nenhum degrau alcancou o piso, e a procedencia tem de '
            'dizer isso em todos — guardar o melhor NAO e alcancar')

    # A TRAVA DE SEGURANCA DO MUNDO 5, E ELA E A AFIRMACAO MAIS IMPORTANTE DESTE
    # PORTAO: guardar o melhor degrau NAO PODE abrir o portao da 30.2. Se
    # abrisse, o conserto de 18/11 teria trocado "perder a leitura do dia" por
    # "publicar uma pagina de compra com dois anuncios", que e infinitamente
    # pior — e seria um defeito no ar, na cabeca de 823 mil buscas/mes.
    bloco5 = col.montar({'id': 'moto-eletrica', 'consulta': 'moto elétrica',
                         'slug': 'veiculos/moto-eletrica',
                         'numero_proprio_pedido': 'faixa_de_preco',
                         'familia': familia, 'escada_de_chaves': escada},
                        colhido5)
    afirmar(bloco5['resumo']['abre_o_portao_da_30_2'] is False,
            'TRAVA: com 2 anuncios guardados o portao da 30.2 tem de ficar '
            'FECHADO, e ele diz %r — isto publicaria pagina de compra abaixo do '
            'piso' % bloco5['resumo']['abre_o_portao_da_30_2'])
    afirmar(bloco5['resumo']['numero_proprio'] is None,
            'TRAVA: sem o piso de tres nao se publica faixa de preco, e o resumo '
            'traz %r' % (bloco5['resumo']['numero_proprio'],))
    afirmar(bloco5['resumo']['ofertas_que_servem'] == 2,
            'TRAVA: o resumo tem de CONTAR os dois que sobraram — e o numero que '
            'diz de quanto a consulta esta longe —, e diz %r'
            % bloco5['resumo']['ofertas_que_servem'])

    # MUNDO 5-b — O EMPATE: dois degraus entregando o mesmo numero. Fica o mais
    # ESPECIFICO, que e o de cima: a escada foi escrita do mais estreito para o
    # mais largo, e desempatar pelo largo inverteria a ordem declarada.
    m5b = {
        d1: [oferta(911, T1, 1000.0, shop_id=11)],
        d2: [oferta(912, T2, 2000.0, shop_id=12)],
    }
    colhido5b, _ = rodar(m5b, {})
    afirmar(colhido5b['degrau_escolhido'] == 1,
            'mundo 5-b: no empate em 1 e 1, fica o degrau mais especifico (1), '
            'e ficou %r' % colhido5b.get('degrau_escolhido'))

    # MUNDO 5-c — O VAZIO DE VERDADE: nenhum degrau entrega NADA. Aqui a lista
    # vazia e a resposta certa, e continua sendo.
    m5c = {
        d1: [oferta(921, 'Capacete de moto elétrica para adultos RGN', 102.09, shop_id=21)],
        d2: [oferta(922, 'Buzina De Bicicleta Elétrica Anti-Roubo', 63.92, shop_id=22)],
    }
    colhido5c, _ = rodar(m5c, {})
    afirmar(colhido5c['chave_escolhida'] is None,
            'mundo 5-c: sem NENHUMA oferta que entre, chave_escolhida tem de ser '
            'None, e deu %r' % colhido5c['chave_escolhida'])
    afirmar(colhido5c['anuncios'] == [],
            'mundo 5-c: sem nada que entre nao se monta anuncio, montou %r'
            % len(colhido5c['anuncios']))

    # -----------------------------------------------------------------------
    # MUNDO 5-d — O LAUDO DIZ O QUE FOI GRAVADO, e nao o que era verdade antes
    # da quarentena. Medido em 18/11/2026: a tela imprimiu `servem 3 · abre o
    # portao da 30.2: True · numero proprio de 8500 ate 15000` e o arquivo
    # recebeu `2 · False · None` no mesmo segundo, porque `laudo()` rodava antes
    # de `atravessar_a_coleta()`. Quem le a tela para decidir o que fazer com a
    # pagina decidia sobre um momento que nao existe.
    # -----------------------------------------------------------------------
    c_moto = {'id': 'moto-eletrica', 'consulta': 'moto elétrica',
              'slug': 'veiculos/moto-eletrica',
              'numero_proprio_pedido': 'faixa_de_preco',
              'familia': familia, 'escada_de_chaves': escada}
    # O MUNDO DAQUI E O REAL DA MOTO EM 18/11, e nao o m1: para a quarentena
    # mudar o veredito, o aposentado tem de estar no degrau ESCOLHIDO. No m1 a
    # escada desce para um degrau limpo e a quarentena nao morde mais nada —
    # exatamente o que a primeira versao deste mundo nao viu.
    m5d = {
        d1: [oferta(1001, T1, 1000.0, shop_id=101),
             oferta(1002, T2, 2000.0, shop_id=102),
             oferta(ap, T3, 15000.0, shop_id=103)],
        d2: [oferta(1003, 'Capacete de moto elétrica para adultos RGN', 102.09,
                    shop_id=104)],
    }
    colhido_d, _ = rodar(m5d, bloco)
    afirmar(colhido_d['degrau_escolhido'] == 1,
            'mundo 5-d: a escada tinha de esgotar e guardar o degrau 1 (o melhor '
            'medido), e ficou em %r' % colhido_d.get('degrau_escolhido'))
    bloco_d = col.montar(c_moto, colhido_d)
    antes = dict(bloco_d['resumo'])
    guardado_stdout = sys.stdout

    class Mudo(object):
        def __init__(self):
            self.texto = []

        def write(self, t):
            self.texto.append(t)

        def flush(self):
            pass

    # `atravessar_a_coleta` imprime a linha da quarentena, e ela e saida DELE e
    # nao do laudo: silenciada aqui para a tela do portao nao virar ruido e para
    # a captura abaixo medir SO o laudo.
    sys.stdout = Mudo()
    try:
        col.atravessar_a_coleta(bloco_d, bloco)
    finally:
        sys.stdout = guardado_stdout
    mudo = Mudo()
    sys.stdout = mudo
    try:
        col.laudo(bloco_d)
    finally:
        sys.stdout = guardado_stdout
    tela = ''.join(mudo.texto)
    depois = bloco_d['resumo']

    # A MUDANCA SE MEDE NOS NUMEROS QUE O LAUDO IMPRIME E QUE NAO DEPENDEM DE
    # REDE. O veredito do portao da 30.2 tambem exige link de afiliado
    # (`ofertas_com_link >= 3`), e este portao roda sem rede e nao encurta nada:
    # nele o portao e False nos dois lados por falta de link, nao por causa da
    # quarentena, e afirmar sobre ele aqui mediria a ausencia do encurtador.
    # `ofertas_que_servem` e `numero_proprio` sao as duas linhas que a tela de
    # 18/11/2026 imprimiu erradas, e as duas se medem em memoria.
    afirmar(antes['ofertas_que_servem'] == 3 and depois['ofertas_que_servem'] == 2,
            'mundo 5-d: a quarentena tinha de levar `ofertas_que_servem` de 3 '
            'para 2 (antes %r, depois %r) — sem essa mudanca o mundo nao '
            'reproduz o defeito' % (antes['ofertas_que_servem'],
                                    depois['ofertas_que_servem']))
    afirmar(antes['numero_proprio'] is not None and depois['numero_proprio'] is None,
            'mundo 5-d: antes da quarentena havia faixa de preco e depois dela '
            'nao ha (antes %r, depois %r) — e a faixa que a tela anunciou'
            % (antes['numero_proprio'], depois['numero_proprio']))
    afirmar('servem %d ' % depois['ofertas_que_servem'] in tela,
            'mundo 5-d: a tela tinha de imprimir `servem %d` (o numero gravado) '
            'e imprimiu: %r' % (depois['ofertas_que_servem'],
                                [l for l in tela.splitlines() if 'servem' in l]))
    afirmar('abre o portao da 30.2: %s' % depois['abre_o_portao_da_30_2'] in tela,
            'mundo 5-d: a tela tinha de imprimir o portao como %r e imprimiu: %r'
            % (depois['abre_o_portao_da_30_2'],
               [l for l in tela.splitlines() if 'portao' in l]))
    afirmar('8500' not in tela or depois['numero_proprio'] is not None,
            'mundo 5-d: a tela anunciou a faixa de preco que o arquivo nao '
            'recebeu (numero_proprio gravado: %r) — e exatamente a mentira de '
            '18/11/2026' % (depois['numero_proprio'],))

    # -----------------------------------------------------------------------
    # MUNDO 6 — A DISCORDANCIA (20.8). Sem ela este portao nao prova conserto.
    # -----------------------------------------------------------------------
    pares = (
        ('mundo 1 (aposentado)', m1, bloco, 2),
        ('mundo 2 (dedupe)', m2, {}, 2),
    )
    for nome, mundo, antigo, esperado in pares:
        novo = rodar(mundo, antigo)[0]['degrau_escolhido']
        velho = regua_velha(mundo, escada)
        afirmar(novo == esperado,
                '%s: a regua nova devia parar no degrau %r, parou em %r'
                % (nome, esperado, novo))
        afirmar(velho == 1,
                '%s: a regua VELHA devia parar no degrau 1 (e por isso o defeito '
                'existia), parou em %r' % (nome, velho))
        afirmar(novo != velho,
                '%s: as duas reguas CONCORDAM, e se concordam aqui o conserto nao '
                'esta medido (20.8)' % nome)

    for nome, mundo in (('mundo 3 (passa)', m3), ('mundo 4 (zero)', m4)):
        novo = rodar(mundo, {})[0]['degrau_escolhido']
        velho = regua_velha(mundo, escada)
        afirmar(novo == velho,
                '%s: aqui as duas reguas TEM de concordar — o conserto nao pode '
                'mudar o que ja estava certo (nova=%r, velha=%r)'
                % (nome, novo, velho))

    # -----------------------------------------------------------------------
    # AUTOTESTE DA BATERIA: ela morde?
    # -----------------------------------------------------------------------
    guardado = col.quantos_entram_no_degrau
    try:
        col.quantos_entram_no_degrau = (
            lambda julgadas, quarentena: sum(1 for a in julgadas if a.get('serve')))
        voltou = rodar(m1, bloco)[0]['degrau_escolhido']
    finally:
        col.quantos_entram_no_degrau = guardado
    afirmar(voltou == 1,
            'AUTOTESTE: com a regua velha de volta no lugar da nova, o mundo 1 '
            'tinha de parar no degrau 1 (o defeito) e parou em %r — se nao para, '
            'esta bateria nao esta medindo a funcao que decide' % voltou)

    confere = rodar(m1, bloco)[0]['degrau_escolhido']
    afirmar(confere == 2,
            'AUTOTESTE: depois de repor a funcao, o mundo 1 tinha de voltar a '
            'descer, e deu %r — a bateria deixou o modulo sujo' % confere)

    print('%d afirmacao(oes).' % AFIRMACOES[0])
    if FALHAS:
        print('\nREPROVADO — %d falha(s):' % len(FALHAS))
        for f in FALHAS:
            print('  - %s' % f)
        return 1
    print('APROVADO')
    return 0


if __name__ == '__main__':
    sys.exit(main())

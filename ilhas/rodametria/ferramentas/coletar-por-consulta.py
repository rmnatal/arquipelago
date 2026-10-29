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
HOJE = datetime.date.today().isoformat()


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'relevancia-do-anuncio.py'))

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
def numero_proprio(pedido, anuncios):
    servem = [a for a in anuncios if a['serve'] and a.get('preco') is not None]
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
        if a['serve']:
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
def preco_numero(bruto):
    try:
        return round(float(str(bruto).replace(',', '.')), 2)
    except (TypeError, ValueError):
        return None


def julgar_oferta(oferta, familia, chave, degrau):
    titulo = oferta.get('titulo') or ''
    serve, por, faltou, atendidas = rel.julgar(
        titulo,
        exige_todas=tuple(familia['exige_todas']),
        exige_alguma=tuple(familia.get('exige_alguma') or ()),
        recusas_desligadas=tuple(familia.get('recusas_desligadas') or ()))

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
                'alt': a['titulo'][:120],
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
            serve, por, faltou, _ = rel.julgar(
                a['titulo'],
                exige_todas=tuple(c['familia']['exige_todas']),
                exige_alguma=tuple(c['familia'].get('exige_alguma') or ()),
                recusas_desligadas=tuple(c['familia'].get('recusas_desligadas') or ()))
            if serve != a['serve'] or por != a['recusado_por'] or faltou != a['exigencia_que_faltou']:
                falhas.append('%s / %s: veredito gravado (%s/%s) discorda do calculado (%s/%s)'
                              % (bloco['id'], a['item_id'], a['serve'], a['recusado_por'], serve, por))
            afirmacoes += 1
            if rel.rotulo_de_potencia(a['titulo']) != a['rotulo_de_potencia']:
                falhas.append('%s / %s: rotulo de potencia gravado discorda do calculado'
                              % (bloco['id'], a['item_id']))

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

        servem = [a for a in bloco['anuncios'] if a['serve']]
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
        'o_que_decide_o_veredito': 'ferramentas/relevancia-do-anuncio.py',
        'consultas': [antigo[k] for k in sorted(antigo)],
    }
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('\ngravado: %s (%d consulta(s))' % (os.path.basename(BANCO), len(saida['consultas'])))

    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APLICA, SOBRE O BANCO JA COLHIDO, O VEREDITO DE UMA FOTO QUE A ORIGEM RECUSOU —
ITEM 2 DO DESPACHO DA RONDA DE 18/11/2026.

    python3 ferramentas/aplicar-foto-quebrada.py --conferir
    python3 ferramentas/aplicar-foto-quebrada.py --item 22899142088 \
        --em 2026-11-18 --medicao "..."          # mostra o que mudaria
    ... mais --gravar                            # grava

O DEFEITO QUE ELA EXISTE PARA FECHAR, medido NO CHROME DO RAPHAEL em 18/11/2026,
que e onde o visitante esta: duas fotos de cartao estao quebradas para quem abre
a pagina, e uma delas e o PRIMEIRO cartao de `/veiculos/patinete-eletrico/`, o
espaco mais caro da pagina. `fetch` das duas, TRES passadas cada, `cache:
no-store`: 503 nas seis; na mesma passada uma terceira foto da MESMA CDN
devolveu 200 `image/jpeg`, que e o controle verde — nao e intermitencia (20.2) e
nao e a CDN inteira. No DOM, forcando `loading="eager"` e esperando 6 s:
`naturalWidth: 0` com `complete: true` nas duas, contra 800/1024 nas outras
cinco.

POR QUE UMA FERRAMENTA, E POR QUE ELA SO APLICA O QUE JA FOI MEDIDO. O coletor
mede a foto na coleta e grava `motivo_sem_imagem` quando a CDN nao responde —
ele ja tem a frase certa, e dois registros do banco de hoje a carregam. O que
nao da e RECOLHER para consertar: `cf.shopee.com.br` responde `CONNECT tunnel
failed, response 403` ao egresso desta nuvem, entao uma passada de coleta daqui
marcaria TODAS as fotos como ausentes — trocar duas fotos quebradas por vinte e
uma e o conserto pior que o defeito. Quem mede a foto e a ronda, no navegador do
Raphael; esta ferramenta aplica o veredito dela, e por isso EXIGE a prosa da
medicao na linha de comando em vez de inventar uma (a mesma escolha da
`aplicar-aposentadoria-de-anuncio.py`).

A ESCOLHA DE DESENHO, ENTRE AS TRES QUE O DESPACHO POS NA MESA. "Recolher na
coleta seguinte" deixa a foto quebrada no ar ate la; "ir a segunda fonte da
25.3" (imagem do fabricante) e trabalho que esta nuvem nao alcanca, pelo mesmo
egresso. Fica a terceira: a foto CAI PARA O ESPACO RESERVADO NEUTRO da secao 6,
que a casca ja serve — um `<span class="rdm-molde-cartao-sem-foto">`, nao um
`<img>` —, com `imagem: null` e `motivo_sem_imagem` carregando a medicao inteira.
Cartao sem foto e pior que cartao com foto; cartao com foto QUEBRADA e pior que
os dois, porque promete uma imagem e entrega o icone de imagem rota do
navegador no lugar mais caro da pagina.

E A FOTO VOLTA SOZINHA NO DIA EM QUE A CDN VOLTAR: a coleta remede a foto de
todo anuncio que serve, entao a URL que a loja ainda publicar e lida de novo na
passada seguinte. Isto NAO e quarentena — nada aqui entra em lista de bloqueio,
porque o anuncio continua vivo e vendendo; o que saiu e a foto.
"""

import argparse
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')

# A FRASE E A DO COLETOR, E ELA NAO E DIGITADA AQUI: ver `motivo()`.
PREFIXO_DA_CAUSA = 'a CDN nao respondeu'


def ler():
    with open(BANCO, encoding='utf-8') as f:
        return json.load(f)


def gravar(d):
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write('\n')


def motivo(em, medicao):
    """A prosa de `motivo_sem_imagem`, no formato `CAUSA || ULTIMA MEDICAO` da
    25.4-b.3 — o mesmo separador da quarentena, pelo mesmo motivo: a causa nao
    muda nunca e a medicao e reescrita a cada passada que tentar de novo."""
    return ('%s (HTTP 503: Service Unavailable), medido em %s FORA desta nuvem — '
            'a foto cai para o espaco reservado da secao 6 e volta sozinha na coleta '
            'em que a CDN responder || ULTIMA MEDICAO: %s'
            % (PREFIXO_DA_CAUSA, em, medicao.strip()))


def achar(d, item_id):
    for b in d['consultas']:
        for a in b['anuncios']:
            if int(a.get('item_id') or 0) == item_id:
                return b, a
    return None, None


def conferir():
    """O PORTAO, SEM REDE. Ele NAO confere foto nenhuma — isso nao e tarefa
    desta nuvem. Ele confere a INVARIANTE que esta ferramenta pode quebrar:
    anuncio que serve tem foto OU tem motivo, nunca os dois e nunca nenhum."""
    d = ler()
    falhas, afirmacoes = [], 0

    col = importlib.util.spec_from_file_location(
        'col', os.path.join(RAIZ, 'ferramentas', 'coletar-por-consulta.py'))
    coletor = importlib.util.module_from_spec(col)
    col.loader.exec_module(coletor)

    for b in d['consultas']:
        for a in b['anuncios']:
            if not coletor.entra_na_pagina(a):
                continue
            tem_foto = bool((a.get('imagem') or {}).get('url'))
            tem_motivo = bool((a.get('motivo_sem_imagem') or '').strip())
            afirmacoes += 1
            if tem_foto and tem_motivo:
                falhas.append('%s item %s: tem foto E tem motivo de nao ter foto — '
                              'duas declaracoes do mesmo fato, e so uma sobe (20.7)'
                              % (b['id'], a.get('item_id')))
            afirmacoes += 1
            if not tem_foto and not tem_motivo:
                falhas.append('%s item %s: sem foto e SEM motivo — cartao cai para o '
                              'espaco reservado e a pagina nao sabe dizer por que'
                              % (b['id'], a.get('item_id')))
            # A PROSA DO MOTIVO NAO PODE SER SO UM ROTULO: quem ler o banco
            # amanha precisa saber de que medicao ele saiu.
            # A METADE DA MEDICAO SO E COBRADA DE QUEM ESTA FERRAMENTA ESCREVEU.
            # O coletor grava um motivo CURTO, na passada em que mediu a foto, e
            # cobrar dele o formato da 25.4-b.3 seria reprovar banco certo — o
            # erro que a invariante da ferramenta irma cometeu em 17/11. A
            # assinatura desta ferramenta e `FORA desta nuvem`: o veredito dela
            # vem de medicao que esta nuvem nao fez, e por isso ela TEM de dizer
            # de onde veio.
            if tem_motivo and 'FORA desta nuvem' in a['motivo_sem_imagem']:
                afirmacoes += 1
                if 'ULTIMA MEDICAO:' not in a['motivo_sem_imagem']:
                    falhas.append('%s item %s: veredito de fora da nuvem sem a metade '
                                  'da medicao (25.4-b.3): %r'
                                  % (b['id'], a.get('item_id'),
                                     a['motivo_sem_imagem'][:90]))
            # E O 403 NAO PODE NOMEAR A CDN: esta nuvem nao o alcanca, e
            # atribui-lo a origem e afirmar o que ela nao sabe (item 2 do
            # despacho de 18/11). Quem grava a prosa e
            # `coletar-oferta.causa_de_foto_nao_medida`.
            if tem_motivo and '403' in a['motivo_sem_imagem']:
                afirmacoes += 1
                if PREFIXO_DA_CAUSA in a['motivo_sem_imagem']:
                    falhas.append('%s item %s: motivo com 403 nomeando a CDN — 403 tem '
                                  'dois pais e esta nuvem nao sabe qual: %r'
                                  % (b['id'], a.get('item_id'),
                                     a['motivo_sem_imagem'][:90]))

    # A FUNCAO E CHAMADA, nunca uma copia dela — a licao que a ferramenta irma
    # pagou hoje com um `TypeError` que o autoteste nao via.
    afirmacoes += 1
    linha = motivo('2026-11-18', 'mundo da areia')
    if 'ULTIMA MEDICAO:' not in linha or PREFIXO_DA_CAUSA not in linha:
        falhas.append('motivo() nao monta a prosa fechada: %r' % linha)

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')

    return 1 if falhas else 0


def aplicar(args):
    d = ler()
    bloco, a = achar(d, args.item)
    if a is None:
        print('REPROVADO: item %d nao esta no banco' % args.item)
        return 1
    if not (a.get('imagem') or {}).get('url'):
        print('nada a fazer: o item %d ja esta sem foto (motivo: %r)'
              % (args.item, a.get('motivo_sem_imagem')))
        return 0

    url = a['imagem']['url']
    novo = motivo(args.em, args.medicao)

    print('FOTO FORA, item %d da consulta %s (%s, R$ %s):'
          % (args.item, bloco['id'], a.get('loja'), a.get('preco')))
    print('  - sai a foto: %s' % url)
    print('  - o cartao passa a servir o espaco reservado da secao 6 (<span>, nao <img>)')
    print('  + motivo_sem_imagem: %s' % novo)

    if not args.gravar:
        print('\nnada gravado (rode outra vez com --gravar).')
        return 0

    a['imagem'] = None
    a['motivo_sem_imagem'] = novo
    gravar(d)
    print('\ngravado em dados/anuncios-por-consulta.json')
    print('AGORA RODE: python3 ferramentas/gerar-vitrine-de-produto.py --gravar')

    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--conferir', action='store_true', help='portao, sem rede')
    p.add_argument('--item', type=int)
    p.add_argument('--em', help='data da medicao, aaaa-mm-dd')
    p.add_argument('--medicao', help='o que a medicao FORA desta nuvem viu')
    p.add_argument('--gravar', action='store_true')
    args = p.parse_args()

    if args.conferir:
        return conferir()
    if not (args.item and args.em and args.medicao):
        p.error('--item, --em e --medicao sao obrigatorios (a medicao nao se inventa)')

    return aplicar(args)


if __name__ == '__main__':
    sys.exit(main())

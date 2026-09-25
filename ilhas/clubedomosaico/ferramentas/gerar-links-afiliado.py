#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera (e REGERA) os links de afiliado da Shopee do banco desta ilha, com os
`sub_id` nas casas certas da secao 7 do ARQUIPELAGO.md.

POR QUE ESTA FERRAMENTA EXISTE — o defeito que ela conserta, medido
-------------------------------------------------------------------
Os dezesseis links de Shopee desta ilha nasceram em 13/09/2026 pelo painel
`affiliate.shopee.com.br/offer/custom_link`, com os cinco campos de sub-id
preenchidos a mao. Eles sairam DESLOCADOS UMA CASA: o unico clique da ilha na
janela 16->22/09 chegou ao Relatorio de cliques como

    -clubedomosaico-F2--

isto e, `sub_id_1` VAZIO, `sub_id_2` = clubedomosaico, `sub_id_3` = F2. A
secao 7 manda `sub_id_1` = nome da ilha e `sub_id_2` = codigo da ferramenta, e
o painel nao consegue responder "qual ilha vendeu" enquanto o campo 1 estiver
vazio. Mao humana em cinco caixas de texto nao tem portao; chamada de API tem.

O CAMINHO, e ele nao depende de sessao de ninguem
-------------------------------------------------
A Open API entrou em 16/09/2026 (secao 25.6) e `generateShortLink` aceita os
cinco sub-ids como LISTA POSICIONAL. `ferramentas/shopee-api.py` ja monta essa
lista na ordem certa — `[sub_id_1, sub_id_2, '', '', '']` — entao esta
ferramenta nao reimplementa nada: ela decide QUAIS registros regerar e grava.

O `motivo_sem_url_busca` dos quinze sem piso dizia, desde 13/09, que o
encurtamento "exige a sessao logada". Era verdade naquele dia e deixou de ser
tres dias depois. E a 25.4-b.3 em acao: motivo velho manda a execucao seguinte
nem tentar.

O PAR PERDIDO SE REESCOLHE INTEIRO (25.4-b.1)
---------------------------------------------
Dez registros tinham `url_busca` encurtado e NAO tinham `url_busca_produto` —
a busca crua se perdeu no painel. Nao da para grampear uma palavra-chave nova
ao lado do link velho e chamar aquilo de par: ninguem mediu que os dois apontam
para a mesma busca. Entao a palavra-chave e REESCRITA aqui, em `CHAVES_DE_BUSCA`,
e o link encurtado e gerado DELA, na mesma passada. O link velho e descartado,
nao remendado.

`url` (a ficha de produto) so e regerado quando `url_produto` existe e e da
Shopee: os dois campos saem da mesma URL crua conhecida, e o par continua
demonstravel. Link do Mercado Livre (`meli.la`) nao e tocado — e outro
programa, com `etiqueta_ml` propria, e o gerador dele tem reCAPTCHA (25.6).

A PROVA DE QUE AS CASAS ESTAO CERTAS NAO CUSTA CLIQUE DA ILHA
--------------------------------------------------------------
Ver `ferramentas/conferir-sub-id.py`, na raiz do repositorio: ele gera um link
de BANCADA, com sub-id de bancada, e le o `utm_content` do 301. Conferir os
links da ilha um a um por esse caminho registraria dezesseis cliques com o
sub-id da ilha no Relatorio — justo na semana em que a leitura de 30/09 vai
procurar o PRIMEIRO clique organico (PROPOSTA 3 do despacho de 23/09). O
mecanismo se prova uma vez, na bancada; os links da ilha saem certos por
construcao, pela mesma chamada.

Uso:
    SHOPEE_APP_ID=... SHOPEE_SECRET=... \\
        python3 ilhas/clubedomosaico/ferramentas/gerar-links-afiliado.py [--escrever]

Sem `--escrever` ela so mostra o que faria. A credencial vem do ambiente do
processo e de lugar nenhum mais (secao 25.6).
"""

import argparse
import io
import json
import os
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))

import importlib.util
_spec = importlib.util.spec_from_file_location(
    'shopee_api', os.path.join(RAIZ, 'ferramentas', 'shopee-api.py'))
shopee = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(shopee)

ARQUIVOS = ['materiais-colas', 'materiais-pastilhas', 'materiais-rejuntes']

# A PALAVRA-CHAVE DOS DEZ QUE PERDERAM A BUSCA CRUA (25.4-b.1).
#
# Escrita aqui, a mao, a partir de `marca` + `nome_comercial` do proprio
# registro — nunca deduzida do link encurtado, de onde nao se chega sem clicar.
# Cada uma foi conferida contra a API antes de virar link: a busca tem de
# devolver pelo menos uma oferta, senao a palavra-chave e piso que nao sustenta
# ninguem (25.4-b: "palavra-chave que deixou de trazer resultado e defeito
# silencioso").
CHAVES_DE_BUSCA = {
    # --- OS DEZ QUE PERDERAM A BUSCA CRUA (25.4-b.1) ---
    # Escritas a mao a partir de `marca` + `nome_comercial` do proprio registro,
    # nunca deduzidas do link encurtado, de onde nao se chega sem clicar.
    'tekbond-silicone-acetico-construcao': (
        'silicone acetico construcao tekbond', 'marca + linha + uso'),
    'tekbond-silicone-neutro': (
        'silicone neutro tekbond', 'marca + linha'),
    'cascola-cascorez-extra': (
        'cascorez extra cola branca pva cascola', 'marca + linha + tipo'),
    'quartzolit-cimentcola-externo-acii': (
        'argamassa cimentcola externo quartzolit',
        'a chave com `ac-ii` devolvia ZERO em 25/09/2026: a Shopee anuncia '
        'AC-2/AC-3 e quase nunca escreve a numeracao romana. Um degrau abaixo '
        'na escada da 25.6 — marca + linha + uso'),
    'loctite-durepoxi': ('durepoxi loctite', 'marca + linha'),
    'quartzolit-rejunte-ceramicas': (
        'rejunte ceramicas quartzolit', 'marca + linha'),
    'quartzolit-rejunte-porcelanatos-e-ceramicas': (
        'rejunte porcelanatos e ceramicas quartzolit', 'marca + linha'),
    'quartzolit-rejunte-acrilico': (
        'rejunte acrilico quartzolit', 'marca + linha'),
    'quartzolit-rejunte-epoxi': ('rejunte epoxi quartzolit', 'marca + linha'),
    'quartzolit-rejunte-piscinas': (
        'rejunte para piscinas quartzolit', 'marca + linha'),

    # --- AS TREZE PASTILHAS: A CHAVE DE 13/09 DEVOLVIA ZERO, MEDIDO EM 25/09 ---
    #
    # `Glass Mosaic <codigo> pastilha de vidro <medida>` devolveu ZERO oferta nas
    # treze. A marca nao e anunciada por nome na Shopee e o codigo de catalogo
    # nao aparece em titulo de anuncio. Piso que leva a busca vazia e exatamente
    # o beco sem saida que o degrau 4 da 25.1 existe para impedir.
    #
    # A DESCIDA PAROU NO PRIMEIRO DEGRAU UTIL, e o codigo sozinho esta BARRADO
    # pela armadilha 3 da 25.7: `K2501` sozinho devolve grade traseira de
    # aspirador Karcher. `pastilha de vidro` pelado tambem esta barrado — devolve
    # pastilha de FREIO. O que sustenta a busca e a MEDIDA junto do substantivo.
    #
    # O que se perde na descida esta dito: a busca deixa de prometer AQUELE
    # codigo e passa a prometer a familia (medida e acabamento). Isso e o que um
    # piso e — "ver outras ofertas", nunca "este produto". Nenhuma ficha, nenhum
    # preco e nenhuma foto sai daqui; casamento de item continua proibido pela
    # 25.7.
    'glassmosaic-k2501': ('pastilha de vidro cristal 2,5', 'familia: linha + medida'),
    'glassmosaic-k2502': ('pastilha de vidro cristal 2,5', 'familia: linha + medida'),
    'glassmosaic-mix2510': ('pastilha de vidro cristal 2,5', 'familia: linha + medida'),
    'glassmosaic-102': ('pastilha de vidro cristal 2,5', 'familia: linha + medida'),
    'glassmosaic-k117': ('pastilha de vidro 3x3', 'familia: medida'),
    'glassmosaic-k77': ('pastilha de vidro 3x3', 'familia: medida'),
    'glassmosaic-k66': ('pastilha de vidro 3x3', 'familia: medida'),
    'glassmosaic-a11': ('pastilha de vidro 2x2', 'familia: medida'),
    'glassmosaic-a61': ('pastilha de vidro 2x2', 'familia: medida'),
    'glassmosaic-a37': ('pastilha de vidro 2x2', 'familia: medida'),
    'glassmosaic-ic02': ('pastilha de vidro 2,3', 'familia: medida'),
    'pastilhart-af1500': ('pastilha de vidro 1,5x1,5', 'familia: medida'),
    'glassmosaic-st5102': (
        'pastilha de vidro placa 30x30',
        'strip de 1,2 cm: `strip`, `retangular strip` e `1,2` devolveram zero ou '
        'resultado de outro objeto em 25/09/2026. Parou no degrau da placa'),
}

HOJE = '2026-09-25'


def url_de_busca(chave):
    return 'https://shopee.com.br/search?keyword=' + urllib.parse.quote(chave)


def e_da_shopee(url):
    return bool(url) and 'shopee.com.br' in url


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--escrever', action='store_true')
    p.add_argument('--conferir-chaves', action='store_true',
                   help='so mede se cada palavra-chave nova devolve oferta')
    args = p.parse_args()

    if args.conferir_chaves:
        falhas = 0
        for ident, (chave, _motivo) in sorted(CHAVES_DE_BUSCA.items()):
            try:
                achados = shopee.buscar(chave, quantos=3)
            except shopee.ErroDaShopee as erro:
                print('  ERRO  %-45s %s' % (ident, erro))
                falhas += 1
                continue
            marca = 'ok  ' if achados else 'ZERO'
            if not achados:
                falhas += 1
            print('  %s  %-45s %-46s %d oferta(s)' % (marca, ident, chave, len(achados)))
        print('\npalavras-chave sem oferta: %d' % falhas)
        return 1 if falhas else 0

    resumo = {'url_regerado': 0, 'busca_regerada': 0, 'busca_nova': 0,
              'ml_intocado': 0, 'sem_chave': []}

    for nome in ARQUIVOS:
        caminho = os.path.join(RAIZ, 'ilhas', 'clubedomosaico', 'dados', nome + '.json')
        with io.open(caminho, encoding='utf-8') as f:
            arq = json.load(f)

        for m in arq.get('materiais', []):
            af = m.get('afiliado') or {}
            if not af:
                continue
            ident = m['id']
            s1 = af.get('sub_id_1')
            s2 = af.get('sub_id_2')
            if s1 != 'clubedomosaico' or not s2:
                print('  PULADO %s: sub_id_1=%r sub_id_2=%r' % (ident, s1, s2))
                continue

            # 1. A BUSCA CRUA, que e o piso da 25.2 e o par da 25.4-b.
            #
            # A CHAVE DA TABELA MANDA SEMPRE QUE EXISTIR, inclusive por cima de
            # uma `url_busca_produto` ja gravada: as treze chaves das pastilhas
            # estavam escritas desde 13/09 e devolviam ZERO oferta, e chave que
            # nao traz resultado e o defeito silencioso da 25.4-b, nao um dado a
            # preservar. Quem nao esta na tabela mantem a chave que tem.
            par = CHAVES_DE_BUSCA.get(ident)
            if par:
                chave, motivo = par
                crua = url_de_busca(chave)
                novo_par = not af.get('url_busca_produto')
            elif af.get('url_busca_produto'):
                crua, motivo, novo_par = af['url_busca_produto'], None, False
            else:
                resumo['sem_chave'].append(ident)
                continue

            tinha_busca = bool(af.get('url_busca'))
            curto = shopee.encurtar(crua, s1, s2) if args.escrever else '(seco)'
            if args.escrever:
                af['url_busca_produto'] = crua
                af['url_busca'] = curto
                af.pop('motivo_sem_url_busca', None)
                af['url_busca_gerada_em'] = HOJE
                if motivo:
                    af['motivo_da_chave'] = motivo
                if not af.get('programa'):
                    af['programa'] = 'shopee'
            resumo['busca_regerada' if tinha_busca else 'busca_nova'] += 1
            print('  busca %-45s %s%s' % (ident, curto,
                                          '  [par reescolhido]' if novo_par else ''))

            # 2. A FICHA, so quando o par cru existe e e da Shopee.
            prod = af.get('url_produto')
            if af.get('url') and e_da_shopee(prod):
                curto_u = shopee.encurtar(prod, s1, s2) if args.escrever else '(seco)'
                if args.escrever:
                    af['url'] = curto_u
                    af['gerado_em'] = HOJE
                resumo['url_regerado'] += 1
                print('  ficha %-45s %s' % (ident, curto_u))
            elif af.get('url'):
                resumo['ml_intocado'] += 1

        if args.escrever:
            # os numeros de cabecalho sao recontados aqui; quem os deixa para
            # depois e como a divida de 13/09 ficou invisivel por onze dias
            mats = arq.get('materiais', [])
            afh = arq.setdefault('afiliado', {})
            afh['itens_esperando_link'] = sum(
                1 for x in mats if (x.get('afiliado') or {}).get('url') == '')
            afh['itens_sem_saida_de_compra'] = sum(
                1 for x in mats
                if not ((x.get('afiliado') or {}).get('url')
                        or (x.get('afiliado') or {}).get('url_busca')
                        or (x.get('afiliado') or {}).get('url_busca_produto')))
            afh['itens_com_piso_nao_rastreavel'] = sum(
                1 for x in mats
                if (x.get('afiliado') or {}).get('url_busca_produto')
                and not (x.get('afiliado') or {}).get('url_busca'))
            with io.open(caminho, 'w', encoding='utf-8') as f:
                json.dump(arq, f, ensure_ascii=False, indent=2)
                f.write('\n')

    print('\nficha regerada: %d | busca regerada: %d | busca nova: %d | '
          'Mercado Livre intocado: %d' % (resumo['url_regerado'],
                                          resumo['busca_regerada'],
                                          resumo['busca_nova'],
                                          resumo['ml_intocado']))
    if resumo['sem_chave']:
        print('SEM PALAVRA-CHAVE (nao gerados): %s' % ', '.join(resumo['sem_chave']))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

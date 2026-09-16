#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open API de Afiliados da Shopee — Projeto Arquipélago.

Uso:
    python3 ferramentas/shopee-api.py busca "<palavra-chave>" [--quantos 10] [--sub-id <ilha>]
    python3 ferramentas/shopee-api.py item <itemId> [--shop-id <shopId>] [--sub-id <ilha>]
    python3 ferramentas/shopee-api.py link <url> --sub-id <ilha>

Saída: JSON normalizado em stdout, uma lista de ofertas, cada uma com
`item_id`, `shop_id`, `titulo`, `imagem_url`, `url_produto`, `url_afiliado`,
`preco_min`, `preco_max`, `loja` e `nota`.

CREDENCIAL — A REGRA QUE NÃO SE NEGOCIA (seção 25.6 do ARQUIPELAGO.md)
---------------------------------------------------------------------
`SHOPEE_APP_ID` e `SHOPEE_SECRET` são lidos **do ambiente do processo**, e de
lugar nenhum mais. Eles moram num documento privado do Google Drive do Raphael
chamado `arquipelago-credenciais`; quem chama esta ferramenta lê o documento
pelo conector e passa os dois adiante em memória.

Esta ferramenta **nunca** grava credencial em disco, **nunca** a imprime — nem
em mensagem de erro, nem em modo de depuração — e **nunca** a manda para o
repositório, que é público: o que entra lá fica no histórico do git para
sempre. A mensagem de falta de credencial diz o NOME do campo e nada do valor.

A ASSINATURA, medida em 16/09/2026
----------------------------------
GraphQL puro em `https://open-api.affiliate.shopee.com.br/graphql`. POST com o
corpo `{"query": "..."}` e o cabeçalho:

    Authorization: SHA256 Credential=<AppId>, Timestamp=<unix em segundos>,
                   Signature=<sha256(AppId + Timestamp + Payload + Secret)>

onde `Payload` é **o corpo JSON exato que vai no POST**, byte a byte. Se o
corpo for serializado duas vezes — uma para assinar e outra para enviar — a
assinatura vale para um texto que não foi o enviado e a Shopee devolve
`Invalid Signature`. Por isso o corpo é serializado UMA vez, numa variável, e
essa mesma variável é assinada e enviada.

Credencial errada devolve `error [10020]: Invalid Credential`, com HTTP 200 —
o que é, ele mesmo, a prova de que a chamada chegou ao servidor da Shopee.
Erro de GraphQL não é erro de HTTP, então quem lê só o código de status
conclui sucesso sobre uma resposta vazia.

O EGRESSO — e isto não é passo de rotina
----------------------------------------
`open-api.affiliate.shopee.com.br` precisa estar na lista de domínios
permitidos da conta. Antes de 16/09/2026 o proxy devolvia
`CONNECT tunnel failed, response 403`. Nenhuma rotina mexe nessa lista: é passo
do Raphael (seção 25.6). Quando o egresso estiver fechado, esta ferramenta
falha alto dizendo isso, para ninguém confundir rede fechada com API morta.

O SUB-ID, e por que ele é obrigatório aqui
------------------------------------------
`offerLink` volta **sem** sub-id, e link sem sub-id não sabe dizer de onde
veio: a ilha perde a atribuição do que ela mesma rendeu. Então
`--sub-id <ilha>` faz esta ferramenta pedir o link por `generateShortLink`, que
aceita sub-id, e devolver ESSE link em `url_afiliado`. Sem `--sub-id` ela
devolve `url_afiliado: null` e escreve o motivo — nunca o `offerLink` pelado,
porque link bonito sem atribuição é pior que link feio com atribuição.
"""

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

ENDERECO = 'https://open-api.affiliate.shopee.com.br/graphql'
TEMPO_LIMITE = 45

# A consulta pede só o que o banco das ilhas grava. Campo a mais é byte a mais
# no ar e uma chance a mais de a consulta inteira ser recusada por um campo que
# a conta não tem permissão de ler.
CONSULTA_BUSCA = '''
query($palavra: String, $pagina: Int, $quantos: Int) {
  productOfferV2(keyword: $palavra, page: $pagina, limit: $quantos) {
    nodes {
      itemId
      shopId
      productName
      imageUrl
      productLink
      offerLink
      priceMin
      priceMax
      shopName
      ratingStar
    }
    pageInfo { page limit hasNextPage }
  }
}
'''

CONSULTA_ITEM = '''
query($itemId: Int64, $shopId: Int64) {
  productOfferV2(itemId: $itemId, shopId: $shopId) {
    nodes {
      itemId
      shopId
      productName
      imageUrl
      productLink
      offerLink
      priceMin
      priceMax
      shopName
      ratingStar
    }
    pageInfo { page limit hasNextPage }
  }
}
'''

CONSULTA_LINK = '''
mutation($entrada: ShortLinkInput!) {
  generateShortLink(input: $entrada) { shortLink }
}
'''


class ErroDaShopee(Exception):
    """Falha que veio da Shopee ou da rede. Nunca carrega valor de credencial."""


def _credenciais():
    """Os dois campos, do AMBIENTE e de lugar nenhum mais.

    A mensagem de erro nomeia o campo que falta e não repete o valor de nada —
    inclusive porque o valor que falta é, por definição, o que não existe, e o
    que existe é o que não pode aparecer.
    """
    app_id = (os.environ.get('SHOPEE_APP_ID') or '').strip()
    segredo = (os.environ.get('SHOPEE_SECRET') or '').strip()

    faltando = [nome for nome, valor in (('SHOPEE_APP_ID', app_id),
                                         ('SHOPEE_SECRET', segredo)) if not valor]
    if faltando:
        raise ErroDaShopee(
            'credencial ausente no ambiente: %s. Ela mora no documento privado '
            '`arquipelago-credenciais` do Google Drive do Raphael (seção 25.6 do '
            'ARQUIPELAGO.md) e entra neste processo APENAS como variável de '
            'ambiente, em memória.' % ', '.join(faltando))

    # COLE_AQUI é o marcador do documento: campo não preenchido. Tratá-lo como
    # credencial faria a chamada voltar `Invalid Credential` e alguém concluiria
    # que a API caiu. O despacho manda parar antes da coleta e dizer isso.
    for nome, valor in (('SHOPEE_APP_ID', app_id), ('SHOPEE_SECRET', segredo)):
        if valor.startswith('COLE_AQUI'):
            raise ErroDaShopee(
                '%s ainda está com o marcador de não preenchido no documento de '
                'credenciais. Não é falha da API: a credencial não foi cadastrada.'
                % nome)

    return app_id, segredo


def _chamar(corpo_dict):
    """Uma chamada GraphQL assinada. Devolve o `data` já desembrulhado.

    O CORPO É SERIALIZADO UMA VEZ SÓ, de propósito: a assinatura vale sobre o
    texto exato do POST. Serializar duas vezes produz assinatura de um corpo
    que não foi enviado — e a Shopee recusa sem dizer por quê.
    """
    app_id, segredo = _credenciais()

    corpo = json.dumps(corpo_dict, ensure_ascii=False, separators=(',', ':'))
    agora = str(int(time.time()))
    assinatura = hashlib.sha256(
        (app_id + agora + corpo + segredo).encode('utf-8')).hexdigest()

    pedido = urllib.request.Request(
        ENDERECO,
        data=corpo.encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'SHA256 Credential=%s, Timestamp=%s, Signature=%s'
                             % (app_id, agora, assinatura),
        },
        method='POST')

    try:
        with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE) as resposta:
            bruto = resposta.read().decode('utf-8')
    except urllib.error.HTTPError as erro:
        raise ErroDaShopee('a Shopee devolveu HTTP %s' % erro.code)
    except urllib.error.URLError as erro:
        # Egresso fechado tem cara de erro de rede comum. Dizer o nome do
        # domínio aqui é o que separa "a API caiu" de "a lista de domínios
        # permitidos da conta não tem este endereço" — que é passo do Raphael.
        raise ErroDaShopee(
            'não foi possível alcançar %s (%s). Confira se o domínio '
            '`open-api.affiliate.shopee.com.br` está na lista de domínios '
            'permitidos da conta — seção 25.6 do ARQUIPELAGO.md.'
            % (ENDERECO, erro.reason))

    try:
        resposta = json.loads(bruto)
    except ValueError:
        raise ErroDaShopee('a Shopee devolveu algo que não é JSON (%d bytes)' % len(bruto))

    # ERRO DE GRAPHQL CHEGA COM HTTP 200. Quem lê só o status conclui sucesso
    # sobre uma resposta vazia — e foi assim que a chamada com credencial falsa
    # de 16/09/2026 provou que o caminho de rede estava aberto.
    if resposta.get('errors'):
        primeiro = resposta['errors'][0]
        raise ErroDaShopee('erro da API: %s' % (primeiro.get('message') or primeiro))
    if resposta.get('error'):
        raise ErroDaShopee('erro da API: [%s] %s'
                           % (resposta.get('error'), resposta.get('message') or ''))

    return resposta.get('data') or {}


def _normalizar(no):
    """Um nó da Shopee na forma que o banco das ilhas grava.

    `url_afiliado` sai VAZIO aqui de propósito: quem o preenche é
    `_encurtar_com_sub_id`, e só quando há sub-id. Ver o cabeçalho.
    """
    return {
        'item_id': no.get('itemId'),
        'shop_id': no.get('shopId'),
        'titulo': no.get('productName'),
        'imagem_url': no.get('imageUrl'),
        'url_produto': no.get('productLink'),
        'url_afiliado': None,
        'url_afiliado_sem_sub_id': no.get('offerLink'),
        'preco_min': no.get('priceMin'),
        'preco_max': no.get('priceMax'),
        'loja': no.get('shopName'),
        'nota': no.get('ratingStar'),
    }


def buscar(palavra, quantos=10, pagina=1):
    dados = _chamar({'query': CONSULTA_BUSCA,
                     'variables': {'palavra': palavra, 'pagina': pagina,
                                   'quantos': quantos}})
    oferta = (dados.get('productOfferV2') or {})
    return [_normalizar(n) for n in (oferta.get('nodes') or [])]


def por_item(item_id, shop_id=None):
    variaveis = {'itemId': int(item_id)}
    if shop_id is not None:
        variaveis['shopId'] = int(shop_id)
    dados = _chamar({'query': CONSULTA_ITEM, 'variables': variaveis})
    oferta = (dados.get('productOfferV2') or {})
    return [_normalizar(n) for n in (oferta.get('nodes') or [])]


def encurtar(url, sub_id):
    """O link COM sub-id, que é o único que entra no banco.

    Sem sub-id a ilha não consegue separar o que ela rendeu do que veio de
    qualquer outro lugar — e o banco já carrega `afiliado.sub_id_1` em todo
    registro justamente para isso.
    """
    if not sub_id:
        raise ErroDaShopee('encurtar sem sub-id é o que esta ferramenta existe para impedir')
    dados = _chamar({'query': CONSULTA_LINK,
                     'variables': {'entrada': {'originUrl': url,
                                               'subIds': [sub_id, '', '', '', '']}}})
    curto = ((dados.get('generateShortLink') or {}).get('shortLink'))
    if not curto:
        raise ErroDaShopee('generateShortLink não devolveu link para %s' % url)
    return curto


def _com_sub_id(ofertas, sub_id):
    """Preenche `url_afiliado` com o link que carrega o sub-id da ilha.

    Falha de uma oferta não derruba as outras: o motivo fica escrito NO item,
    porque item sem link com motivo em branco é o mesmo que item sem link
    inventado — ninguém sabe se faltou dado ou faltou tentativa.
    """
    for oferta in ofertas:
        origem = oferta.get('url_produto') or oferta.get('url_afiliado_sem_sub_id')
        if not origem:
            oferta['motivo_sem_link'] = 'a Shopee não devolveu endereço de produto'
            continue
        try:
            oferta['url_afiliado'] = encurtar(origem, sub_id)
            oferta['sub_id_1'] = sub_id
        except ErroDaShopee as erro:
            oferta['motivo_sem_link'] = str(erro)
    return ofertas


def main():
    p = argparse.ArgumentParser(description='Open API de Afiliados da Shopee')
    sub = p.add_subparsers(dest='acao', required=True)

    b = sub.add_parser('busca', help='buscar ofertas por palavra-chave')
    b.add_argument('palavra')
    b.add_argument('--quantos', type=int, default=10)
    b.add_argument('--pagina', type=int, default=1)
    b.add_argument('--sub-id', default=None)

    i = sub.add_parser('item', help='buscar uma oferta por itemId')
    i.add_argument('item_id')
    i.add_argument('--shop-id', default=None)
    i.add_argument('--sub-id', default=None)

    l = sub.add_parser('link', help='encurtar uma URL com o sub-id da ilha')
    l.add_argument('url')
    l.add_argument('--sub-id', required=True)

    args = p.parse_args()

    try:
        if args.acao == 'busca':
            ofertas = buscar(args.palavra, args.quantos, args.pagina)
        elif args.acao == 'item':
            ofertas = por_item(args.item_id, args.shop_id)
        else:
            print(json.dumps({'url': args.url, 'sub_id_1': args.sub_id,
                              'url_afiliado': encurtar(args.url, args.sub_id)},
                             ensure_ascii=False, indent=1))
            return 0

        if args.sub_id:
            ofertas = _com_sub_id(ofertas, args.sub_id)

        # ZERO RESULTADO NÃO É ERRO (seção 25.6). Palavra-chave longa devolve
        # vazio, e quem trata vazio como falha desiste da escada no primeiro
        # degrau.
        print(json.dumps(ofertas, ensure_ascii=False, indent=1))
        return 0
    except ErroDaShopee as erro:
        sys.stderr.write('shopee-api: %s\n' % erro)
        return 1


if __name__ == '__main__':
    sys.exit(main())

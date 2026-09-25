#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portao do `sub_id`: prova em que CASA a Shopee grava cada sub-id, sem gastar um
clique da ilha nenhuma. Vale para todo o Arquipelago.

O DEFEITO QUE ELE EXISTE PARA IMPEDIR, medido na clubedomosaico
-----------------------------------------------------------------
Os dezesseis links de Shopee daquela ilha nasceram em 13/09/2026 pelo painel
`offer/custom_link`, com os cinco campos preenchidos a mao. Sairam deslocados
uma casa, e o unico clique da janela 16->22/09 chegou ao Relatorio como

    -clubedomosaico-F2--

`sub_id_1` VAZIO. A secao 7 manda `sub_id_1` = nome da ilha e `sub_id_2` =
codigo da ferramenta, e sem o campo 1 o painel nao responde "qual ilha vendeu".
Ficou onze dias no ar e ninguem viu, porque nenhum portao media a CASA — so o
conteudo do banco, que estava certo o tempo todo.

COMO A CASA SE LE SEM CLICAR NO LINK DA ILHA
---------------------------------------------
`s.shopee.com.br/XXXX` responde **301** e o `Location` traz os cinco sub-ids
juntos em `utm_content`, com hifen de separador — exatamente o texto que o
Relatorio de cliques mostra. Entao a casa se le do CABECALHO, sem seguir o
redirecionamento e sem abrir pagina nenhuma.

**E por isso o link conferido aqui e um link de BANCADA, nunca um da ilha.** O
salto do encurtador e o ponto onde a Shopee conta o clique: conferir os
dezesseis links da clubedomosaico por este caminho gravaria dezesseis cliques
com o sub-id dela no Relatorio, justo na semana em que a leitura semanal
procura o PRIMEIRO clique organico da ilha. O mecanismo se prova UMA vez, com
sub-id de bancada; os links das ilhas saem certos por construcao, pela mesma
funcao `encurtar()`, e o que este portao mede e justamente essa funcao.

Uso:
    SHOPEE_APP_ID=... SHOPEE_SECRET=... python3 ferramentas/conferir-sub-id.py

Sai 0 quando as casas batem, 1 quando nao batem. A credencial vem do ambiente
do processo e de lugar nenhum mais (secao 25.6).
"""

import importlib.util
import os
import sys
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    'shopee_api', os.path.join(RAIZ, 'ferramentas', 'shopee-api.py'))
shopee = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(shopee)

# Hifen e sublinhado sao recusados DENTRO de um sub-id (25.7), entao os dois
# valores de bancada sao alfanumericos puros — e nao se parecem com o nome de
# ilha nenhuma, para ninguem confundir um clique de bancada com trafego real.
BANCADA_1 = 'bancada'
BANCADA_2 = 't0'
ESPERADO = '%s-%s---' % (BANCADA_1, BANCADA_2)

# Uma busca qualquer: pagina de busca nao esgota e nao some, e o que esta sendo
# medido e o encurtador, nao o produto.
URL_DE_PROVA = 'https://shopee.com.br/search?keyword=teste'


def sub_id_do_link(curto):
    """Le `utm_content` do 301 do encurtador. NAO segue o redirecionamento."""
    class NaoSiga(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    abridor = urllib.request.build_opener(NaoSiga)
    pedido = urllib.request.Request(curto, method='GET')
    try:
        with abridor.open(pedido, timeout=30) as r:
            destino = r.headers.get('Location')
            codigo = r.status
    except urllib.error.HTTPError as erro:
        destino = erro.headers.get('Location')
        codigo = erro.code
    if not destino:
        raise SystemExit('o encurtador respondeu %s e nao mandou Location' % codigo)
    campos = urllib.parse.parse_qs(urllib.parse.urlparse(destino).query)
    return codigo, campos.get('utm_content', [''])[0]


def main():
    curto = shopee.encurtar(URL_DE_PROVA, BANCADA_1, BANCADA_2)
    codigo, lido = sub_id_do_link(curto)

    print('link de bancada ..... %s' % curto)
    print('resposta ............ HTTP %s' % codigo)
    print('utm_content lido .... %r' % lido)
    print('esperado ............ %r' % ESPERADO)

    if lido != ESPERADO:
        campos = lido.split('-')
        print('\nFALHOU: os cinco campos chegaram como %r.' % (campos,))
        print('Campo 1 tem de ser o nome da ilha e campo 2 o codigo da '
              'ferramenta (secao 7). Campo 1 vazio e o defeito de 13/09/2026.')
        return 1

    print('\nOK: campo 1 = %r, campo 2 = %r, campos 3 a 5 vazios. '
          'A ordem de `encurtar()` e a ordem da secao 7.' % (BANCADA_1, BANCADA_2))
    return 0


if __name__ == '__main__':
    sys.exit(main())

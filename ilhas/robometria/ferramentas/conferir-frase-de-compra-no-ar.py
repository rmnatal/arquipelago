#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere NO AR o criterio de pronto do item 3 do despacho da Sentinela de
18/09/2026: nenhuma frase pode negar link de loja numa resposta que serve botao
de compra.

    python3 ferramentas/conferir-frase-de-compra-no-ar.py

POR QUE ELE EXISTE SEPARADO DA BANCADA
--------------------------------------
`ferramentas/teste-r1.php` ja tem a afirmacao equivalente, e ela e a que o
despacho pediu com estas palavras. Mas a bancada mede o HTML que o RENDER DE
BANCADA produz, e a secao 8 do ARQUIPELAGO.md cobra desta casa, com cicatriz
propria, a diferenca entre isso e o que o site SERVE — cache do hospedeiro,
snippet desatualizado no ar, revisao presa. As duas entradas abaixo sao as duas
que o despacho citou nominalmente, com os parametros dele, e e sobre elas que a
18.4 manda afirmar antes de apagar o despacho.

O QUE ELE MEDE, E POR QUE NAS DUAS DIRECOES
-------------------------------------------
1. Serve botao E nega link de loja .... REPROVA. E o defeito de 18/09: a pagina
   negando um botao que ela mesma mostra, que e pior que a promessa "link de
   loja em breve" da secao 7, porque aquela ao menos nao se contradizia na
   mesma tela.
2. Botao cru (sem `sponsored`) ........ AVISA e nao reprova. Pela 25.2-b o link
   cru continua legitimo quando a API nao devolve anuncio para o item — o que
   ele nunca pode e ser o padrao. Reprovar aqui empurraria a ilha a esconder
   peca que nao da comissao, que e o oposto do que a secao decidiu.
3. Sem botao nenhum e SEM a frase ..... REPROVA. Regua que so proibisse a frase
   seria satisfeita por uma pagina que cala sobre um item sem saida de compra, e
   calar e o que a 25.2 e a secao 7 proibiram juntas.
"""
import re
import sys
import urllib.request

URLS = [
    'https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/'
    '?modelo=electrolux-erb60&peca=filtro',
    'https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/'
    '?piso=tapete&pelo=sim&m2=80',
]

# A REGUA E O TEXTO QUE O LEITOR LE, nao um contador do codigo. Contador se
# reescreve amanha; a frase servida e o que o despacho mediu.
NEGA = re.compile(
    r'(n[ãa]o t[ê e]m link de loja|Nenhum[a]? dest[ae]s?[^<.]{0,40}link de loja'
    r'|link de loja em breve)', re.I)

BLOCO = re.compile(r'<div class="rbm-secao rbm-compra">(.*?)</div>', re.S)


def baixar(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'robometria-conferencia/1.0', 'Cache-Control': 'no-cache'})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')


def main():
    falhas = []
    afirmacoes = 0
    print('Robometria — a frase de compra, no ar (item 3 do despacho de 18/09/2026)\n')
    for url in URLS:
        html = baixar(url)
        bloco = BLOCO.search(html)
        trecho = bloco.group(1) if bloco else html
        botoes = len(re.findall(r'class="[^"]*rbm-comprar', html))
        crus = len(re.findall(r'rbm-comprar-cru', html))
        nega = NEGA.search(trecho)
        print('  %s' % url)
        print('    botoes=%d  crus=%d  nega link de loja: %s'
              % (botoes, crus, nega.group(0) if nega else 'nao'))

        afirmacoes += 1
        if botoes and nega:
            falhas.append('%s: serve %d botao(oes) de compra E imprime %r'
                          % (url, botoes, nega.group(0)))
        afirmacoes += 1
        if not botoes and not nega:
            falhas.append('%s: nenhum botao de compra e nenhuma frase dizendo isso. '
                          'Calar sobre a falta e o que a 25.2 e a secao 7 proibiram'
                          % url)
        if crus:
            print('    AVISO: %d botao(oes) cru(s) — clique que nao paga comissao '
                  '(25.2-b). Legitimo so quando a API nao devolve anuncio.' % crus)

    print('\n  afirmacoes ... %d' % afirmacoes)
    if falhas:
        print('\nREPROVADO NO AR — %d:' % len(falhas))
        for f in falhas:
            print('  x %s' % f)
        return 1
    print('APROVADO NO AR: nenhuma entrada nega link de loja servindo botao.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

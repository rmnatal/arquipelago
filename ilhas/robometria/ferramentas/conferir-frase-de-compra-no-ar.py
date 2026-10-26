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
snippet desatualizado no ar, revisao presa. As duas entradas PARAMETRIZADAS
abaixo sao as duas que o despacho de 18/09 citou nominalmente, com os parametros
dele, e e sobre elas que a 18.4 mandava afirmar antes de apagar aquele despacho.

ELE DEIXOU DE TER LISTA EM 26/10/2026, E O MOTIVO E UM DEFEITO QUE ELE NAO VIU
-----------------------------------------------------------------------------
Ate hoje este arquivo visitava DUAS URLs, as duas da R1 e da R2, e o proprio
texto acima justificava a lista dizendo que eram as que o despacho citara. O
defeito do item 1 do despacho de 26/10/2026 morava em
`/quantos-m2-o-robo-aspirador-limpa-por-carga/` — uma pagina que esta regua NAO
ABRIA — e era exatamente o defeito que ela existe para pegar: a pagina negando
link de loja para um modelo cujo botao ela mesma serve, tres linhas acima. A
regua ficou VERDE o tempo todo, e ficou verde com razao: ela nao estava la.

E a cicatriz que o despacho de 23/10 desta mesma ilha ja tinha escrito numa
frase — *"regua que nao varre todas certifica a pagina que o autor abriu"* — e
que a lesson 2 do `teste-escada-compra.py` chama pelo nome: lista dentro da
regua envelhece calada, e o que ela esquece nao aparece em lugar nenhum, porque
o verde das outras ocupa o espaco do que faltou. Pagina nova desta ilha entrava
sem portao nenhum com o ar verde.

Agora ele DESCOBRE as paginas no `wp-sitemap.xml` no ar, como o
`conferir-32-5-no-navegador.mjs` desta ilha ja fazia, e julga toda pagina que
SERVE bloco de compra. As duas entradas parametrizadas continuam, somadas as
descobertas: parametro nao esta no sitemap e a R1 e a R2 so servem botao com
consulta. Pagina sem bloco de compra e LISTADA como tal, nunca aprovada em
silencio.

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
import time
import urllib.request

SITE = 'https://robometria.com.br'

# AS DUAS ENTRADAS QUE O SITEMAP NAO PODE TRAZER, e e por isso que elas ficam a
# mao: as ferramentas so servem botao de compra COM consulta, e consulta nao
# mora em sitemap. Sao as duas que o despacho de 18/09/2026 citou nominalmente,
# com os parametros dele.
COM_PARAMETRO = [
    SITE + '/qual-peca-serve-no-meu-robo-aspirador/'
    '?modelo=electrolux-erb60&peca=filtro',
    SITE + '/quantos-pa-o-robo-aspirador-precisa/'
    '?piso=tapete&pelo=sim&m2=80',
]

# A REGUA E O TEXTO QUE O LEITOR LE, nao um contador do codigo. Contador se
# reescreve amanha; a frase servida e o que o despacho mediu.
NEGA = re.compile(
    r'(n[ãa]o t[ê e]m link de loja|Nenhum[a]? dest[ae]s?[^<.]{0,40}link de loja'
    r'|link de loja em breve)', re.I)

# O BLOCO DE COMPRA GANHOU id EM 21/10/2026 (a 32.1 manda a barra do celular
# apontar para ele). O padrao lia a abertura da <div> pela classe EXATA: com o
# atributo novo ele deixava de casar, esta regua passava a medir NADA e o ar
# ficava sem o portao que denuncia a frase proibida dentro do bloco de compra.
# Agora aceita atributo depois da classe, e a classe continua sendo cobrada.
BLOCO = re.compile(r'<div class="rbm-secao rbm-compra"[^>]*>(.*?)</div>', re.S)


def baixar(url):
    # QUEBRA DE CACHE NA URL, e nao so no cabecalho: o cache de borda do
    # hospedeiro desta ilha ignora `Cache-Control` do cliente — e medir o cache
    # em vez do site e a cicatriz que a secao 8 cobra desta casa.
    sep = '&' if '?' in url else '?'
    alvo = url + sep + 'cb=' + str(int(time.time()))
    req = urllib.request.Request(alvo, headers={
        'User-Agent': 'robometria-conferencia/1.0', 'Cache-Control': 'no-cache'})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')


def do_sitemap():
    """As paginas da ilha, lidas do `wp-sitemap.xml` no ar.

    Nao e lista: e o que o site declara que publica. Pagina nova entra no dia em
    que e publicada, sem ninguem lembrar de acrescenta-la aqui — que e
    exatamente o que ninguem lembrou de fazer com os dois artigos.
    """
    indice = baixar(SITE + '/wp-sitemap.xml')
    urls = set()
    for sub in re.findall(r'<loc>([^<]+)</loc>', indice):
        if 'wp-sitemap' not in sub:
            continue
        for u in re.findall(r'<loc>([^<]+)</loc>', baixar(sub)):
            if u.startswith(SITE) and 'wp-sitemap' not in u:
                urls.add(u)
    if not urls:
        raise SystemExit(
            'PARADA: o wp-sitemap.xml nao devolveu nenhuma URL desta ilha. Sem '
            'as paginas nao ha o que conferir, e aprovar aqui seria aprovar o '
            'vazio — o defeito que esta regua acabou de pagar por ter lista.')
    return sorted(urls)


def main():
    falhas = []
    afirmacoes = 0
    com_compra = 0
    sem_compra = []
    print('Robometria — a frase de compra, no ar (item 3 do despacho de 18/09/2026,\n'
          'e o item 1 do de 26/10/2026, que foi o que lhe tirou a lista)\n')
    alvos = COM_PARAMETRO + do_sitemap()
    for url in alvos:
        html = baixar(url)
        bloco = BLOCO.search(html)
        botoes = len(re.findall(r'class="[^"]*rbm-comprar', html))

        # PAGINA SEM BLOCO DE COMPRA NAO E JULGADA, E E LISTADA. A home, a
        # metodologia, o sobre e a divulgacao de afiliados nao vendem nada e nao
        # devem nenhuma frase sobre link de loja — cobrar delas a afirmacao 2
        # faria esta regua reprovar paginas sadias, que e o jeito mais rapido de
        # ensinar a proxima execucao a ignora-la. Mas o silencio sobre elas e
        # declarado, nunca omitido: e so assim que se ve a pagina de compra que
        # deixou de ter bloco.
        if not bloco and not botoes:
            sem_compra.append(url)
            continue

        com_compra += 1
        trecho = bloco.group(1) if bloco else html
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

    print('\n  paginas com bloco de compra ... %d de %d abertas' % (com_compra, len(alvos)))
    print('  sem bloco de compra .......... %d: %s'
          % (len(sem_compra), ' '.join(u.replace(SITE, '') or '/' for u in sem_compra)))
    # A REGUA TEM DE TER ACHADO ALGO. Sitemap vazio, classe renomeada ou bloco
    # que sumiu deixariam este arquivo imprimir "APROVADO" sobre zero medicao —
    # o verde mais caro que existe, porque ele parece conferido.
    afirmacoes += 1
    if com_compra < 3:
        falhas.append('so %d pagina(s) com bloco de compra em %d abertas. As duas '
                      'ferramentas e os dois artigos servem bloco de compra desde '
                      '14/09/2026: menos que isso e classe renomeada ou bloco que '
                      'sumiu, nao ilha que vende menos' % (com_compra, len(alvos)))

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

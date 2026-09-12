#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere NO AR a entrada que a transcricao dos kits mudou (12/09/2026).

    python3 ferramentas/conferir-kits-no-ar.py

POR QUE ESTE ARQUIVO EXISTE, e por que o conferir-no-ar.py nao bastava
---------------------------------------------------------------------
O `conferir-no-ar.py` mede as nove URLs da ilha no caso-ANCORA — a pagina sem
consulta. A R1 e ferramenta de entrada variavel: ela serve uma pagina por
consulta, e o bloco de 12/09/2026 mudou exatamente as paginas que so existem
QUANDO ALGUEM ESCOLHE UM MODELO. Sem este arquivo, o desembarque seria dado por
entregue com 149 afirmacoes verdes que nao tocaram uma linha do que mudou — a
cicatriz "VARRER A ENTRADA INTEIRA, NAO O CASO-ANCORA" da secao 8 do
ARQUIPELAGO.md, escrita nesta mesma ilha.

A REGUA E ESCRITA AQUI, LITERALMENTE. Nao e lida de pecas.json nem de
r1-respostas.json de proposito: se esta conferencia derivasse do mesmo lugar de
onde a pagina deriva, as duas metades errariam juntas e o verde nao mediria nada.
O preco e que ela envelhece quando o banco mudar — e esse e o desenho: ela
REPROVA, e alguem le o que mudou, em vez de acompanhar calada.

A MEDICAO E NO CORPO, nunca no HTML inteiro (secao 8). E o localizador do corpo e
<main ...>, com atributo: no ar o WordPress serve classes na tag, e um padrao
que so casa a tag nua devolve vazio e aprova tudo por ausencia.
"""

import re
import subprocess
import sys
import time
import unicodedata

BASE = 'https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/'

falhas = 0
feitos = 0


def ok(condicao, rotulo, medido=''):
    global falhas, feitos
    feitos += 1
    print('  %s %-58s %s' % ('ok   ' if condicao else 'FALHA', rotulo, medido))
    if not condicao:
        falhas += 1
    return condicao


def buscar(url, tentativas=3):
    """Uma falha de rede so vira bloqueio depois de repetir (secao 20.2)."""
    for _ in range(tentativas):
        r = subprocess.run(['curl', '-s', '-w', '\\n%{http_code}', '--max-time', '40', url],
                           capture_output=True, text=True)
        corpo = r.stdout
        codigo = corpo.rsplit('\n', 1)[-1].strip()
        if codigo and codigo != '000':
            return corpo.rsplit('\n', 1)[0], codigo
        time.sleep(4)
    return '', '000'


def corpo_da_pagina(servido):
    m = re.search(r'<main\b[^>]*>(.*?)</main>', servido, re.S | re.I)
    return m.group(1) if m else ''


def bloco_da_resposta(corpo):
    """SO o bloco que responde a consulta, nunca a pagina inteira.

    A primeira versao desta conferencia procurava "nao localizamos" no corpo e
    reprovou os cinco estados que RESPONDEM — porque a frase existe duas vezes na
    pagina por motivo legitimo: na promessa do topo ("nos outros, a resposta e
    'nao localizamos declaracao do fabricante'") e na secao que lista os 12
    modelos em que a ferramenta ainda nao responde. Medir no corpo inteiro e a
    mesma heuristica por vizinhanca que a secao 8 do ARQUIPELAGO.md proibe: quem
    decide e a ESTRUTURA.

    O bloco vai de id="resultado" ate a tabela pre-renderizada (rbm-quadro), que
    e o primeiro irmao depois dele em todos os estados. Se a fronteira nao for
    encontrada, devolve vazio E quem chama REPROVA — localizador que nao casa
    tem de gritar, nunca aprovar por ausencia (foi o <body> da Aquametria).
    """
    i = corpo.find('id="resultado"')
    if i < 0:
        return ''
    fim = corpo.find('rbm-quadro', i)
    if fim < 0:
        return ''
    return corpo[i:fim]


def texto(bloco):
    """So o texto que um leitor ve: sem marcacao e sem acento.

    Sem acento porque a comparacao e de conteudo, nao de transcricao — o acento
    ja tem portao proprio (teste-acentuacao.php), e cobrar as duas coisas na
    mesma afirmacao faz uma esconder a outra."""
    limpo = re.sub(r'<script\b.*?</script>', ' ', bloco, flags=re.S | re.I)
    limpo = re.sub(r'<[^>]+>', ' ', limpo)
    limpo = limpo.replace('&nbsp;', ' ')
    limpo = unicodedata.normalize('NFKD', limpo)
    limpo = ''.join(c for c in limpo if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', limpo).lower()


# ---------------------------------------------------------------- A REGUA
#
# O que a pagina TEM que dizer depois da transcricao de 12/09/2026, por estado.
# Cada linha e: (modelo, tipo consultado, tem que responder?, por que).
#
# ERB30: a composicao do Kit Performance dele foi transcrita com quantidades, e
# ele era o unico modelo da ilha que so tinha kit fechado — nao respondia nada.
# ERB44: a composicao veio pela metade (a pagina declara os tipos e nao as
# quantidades, e chama a escova de "escovas" sem dizer qual), entao filtro e mop
# respondem e as DUAS escovas nao — e nao responder aqui e o acerto, nao a falta.
ESTADOS = [
    ('electrolux-erb30', 'filtro',           True,
     'o kit do ERB30 declara 01 filtro HEPA'),
    ('electrolux-erb30', 'mop',              True,
     'o kit do ERB30 declara 01 pano de microfibra'),
    ('electrolux-erb30', 'escova lateral',   True,
     'o kit do ERB30 declara 02 escovas de varredura de cantos'),
    ('electrolux-erb30', 'escova principal', False,
     'o kit nao declara escova central, e supor seria inventar'),
    ('electrolux-erb30', 'bateria',          False,
     'o kit nao traz bateria'),
    ('electrolux-erb44', 'mop',              True,
     'o kit do ERB44 declara pano de microfibra'),
    ('electrolux-erb44', 'filtro',           True,
     'o ERB44 ja tinha filtro avulso declarado, e o kit tambem traz filtro'),
    ('electrolux-erb44', 'escova lateral',   False,
     'a pagina do kit diz "escovas" sem dizer qual — o item entrou com tipo null'),
    ('electrolux-erb44', 'escova principal', False,
     'mesma razao: tipo nao declarado pela fonte'),
]

# Como a pagina diz que NAO tem o que responder. Escrito aqui, e nao lido do
# snippet, pelo mesmo motivo que o resto da regua.
MARCA_DE_RECUSA = 'nao localizamos'

# A composicao do ERB30, literal. Ela nao precisa aparecer na tela — a R1 fala de
# tipo, nao de quantidade —, mas se um dia aparecer, tem que ser esta.
COMPOSICAO_ERB30 = ('01 filtro hepa', '01 pano de microfibra', '02 escovas')


def url(modelo, tipo):
    from urllib.parse import quote
    return '%s?modelo=%s&peca=%s&v=%s' % (BASE, quote(modelo), quote(tipo),
                                          time.strftime('%H%M%S'))


def main():
    print('Robometria — a entrada que a transcricao dos kits mudou, medida NO AR\n')
    print('  (regua escrita dentro deste arquivo; medicao no CORPO, nunca no HTML inteiro)\n')

    corpos = {}
    for modelo, tipo, _, _ in ESTADOS:
        chave = (modelo, tipo)
        if chave in corpos:
            continue
        servido, codigo = buscar(url(modelo, tipo))
        c = corpo_da_pagina(servido)
        bloco = bloco_da_resposta(c)
        corpos[chave] = bloco
        ok(codigo == '200', 'HTTP 200 em %s x %s' % (modelo.split('-')[-1], tipo), codigo)
        ok(len(c) > 1500, '  o corpo tem tamanho de pagina de verdade',
           '%d caracteres' % len(c))
        ok(len(bloco) > 200, '  o bloco de resposta foi LOCALIZADO, nao presumido',
           '%d caracteres' % len(bloco))

    print('\nO que a pagina responde em cada estado\n')
    for modelo, tipo, deve_responder, porque in ESTADOS:
        t = texto(corpos[(modelo, tipo)])
        recusou = MARCA_DE_RECUSA in t
        rotulo = '%s x %s' % (modelo.split('-')[-1], tipo)
        if deve_responder:
            ok(not recusou, '%-34s RESPONDE' % rotulo, porque)
        else:
            ok(recusou, '%-34s recusa, e a recusa e o acerto' % rotulo, porque)

    print('\nO ERB30 deixou de ser o modelo que nao respondia nada\n')
    t_filtro = texto(corpos[('electrolux-erb30', 'filtro')])
    ok('kit performance' in t_filtro,
       'a resposta do ERB30 nomeia o kit que a serve')
    ok(MARCA_DE_RECUSA not in t_filtro,
       'e nao diz mais que nao localizou declaracao do fabricante')

    # A porta de compra tem que existir onde a pagina recomenda (secao 7 do
    # ARQUIPELAGO.md): o bloco nasce mesmo sem link, reservando o lugar.
    ok('link de loja em breve' in t_filtro or 'onde comprar' in t_filtro,
       'a porta de compra existe no estado que passou a recomendar',
       'o dado abriu a porta, e ela nao ficou so na procedencia')

    # E onde ela recusa, o bloco NAO pode existir — botao embaixo de uma recusa
    # e recomendar assim mesmo (decisao da R2, 12/09/2026).
    t_bateria = texto(corpos[('electrolux-erb30', 'bateria')])
    ok('onde comprar' not in t_bateria,
       'onde a pagina recusa, a porta de compra nao aparece')

    print('\nSe a quantidade chegar a tela, ela e a que a fonte declara\n')
    achadas = [q for q in COMPOSICAO_ERB30 if q in t_filtro]
    ok(all(q in COMPOSICAO_ERB30 for q in achadas),
       'nenhuma quantidade estranha a fonte na tela',
       'encontradas: %s' % (', '.join(achadas) if achadas else 'nenhuma (a R1 fala de tipo)'))

    print('\n' + '=' * 78)
    if falhas:
        print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0


if __name__ == '__main__':
    sys.exit(main())

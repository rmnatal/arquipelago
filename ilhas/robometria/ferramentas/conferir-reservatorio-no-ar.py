#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere NO AR o que o bloco do reservatorio mudou (13/09/2026).

    python3 ferramentas/conferir-reservatorio-no-ar.py

POR QUE ESTE ARQUIVO EXISTE, e por que os tres que ja havia nao bastavam
-----------------------------------------------------------------------
`conferir-no-ar.py` mede as nove URLs no caso-ANCORA, `conferir-kits-no-ar.py`
mede a entrada que a transcricao dos kits mudou e `conferir-atribuicao-no-ar.py`
mede a funcao das escovas. Os tres passaram VERDES depois do desembarque da
revisao 31 sem tocar uma linha do que este bloco mudou: nenhum deles sabe o que e
um reservatorio. Dar o desembarque por entregue com 331 afirmacoes verdes que nao
medem a mudanca e a cicatriz "VARRER A ENTRADA INTEIRA, NAO O CASO-ANCORA" da
secao 8 do ARQUIPELAGO.md — escrita nesta ilha, e por isto ela nao se repete.

O QUE MUDOU E O QUE ESTA REGUA MEDE
-----------------------------------
O tipo "reservatorio" existia no vocabulario do banco com ZERO pecas, e por isso
estava FORA do seletor da R1 desde 10/09 — a pagina dizia isso em voz alta, numa
frase que terminava com uma PROMESSA: "o tipo volta ao seletor no dia em que a
primeira peca dele entrar". As duas primeiras entraram. Esta regua cobra a
promessa cumprida, nos dois sentidos: o tipo oferecido E a frase da ausencia
sumida.

A REGUA E ESCRITA AQUI, LITERALMENTE, como a dos kits. Nao le pecas.json nem
r1-respostas.json de proposito: conferencia que deriva do mesmo lugar de onde a
pagina deriva erra junto com ela e o verde nao mede nada. O preco e que ela
envelhece quando o banco mudar — e esse e o desenho: ela REPROVA, e alguem le o
que mudou, em vez de acompanhar calada.

AS DUAS DIRECOES, porque so a primeira tem porta dos fundos (secao 8)
--------------------------------------------------------------------
Cobrar apenas "o W300 responde reservatorio" aprovaria uma pagina que
respondesse QUALQUER COISA a QUALQUER consulta. Por isso entra o estado NEGATIVO:
um modelo que nao tem reservatorio declarado TEM de recusar. E entra a trava do
codigo que nao existe: o recipiente do WSMART tem codigo de fabricante e o do
W300 nao tem, entao a resposta do W300 nao pode carregar codigo nenhum — a
maneira mais barata de esta ilha mentir seria emprestar o codigo da peca vizinha.

A MEDICAO E NO CORPO, nunca no HTML inteiro, e o localizador e <main ...> com
atributo: no ar o WordPress serve classes na tag, e padrao que so casa a tag nua
devolve vazio e aprova tudo por ausencia.
"""

import os
import re
import subprocess
import sys
import time
import unicodedata
from urllib.parse import quote

BASE = 'https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/'

# MODO BANCADA — como esta regua foi vista REPROVANDO (13/09/2026).
#
# Conferencia no ar nao pode ser mutada: o site e um so e a mutacao teria de ir ao
# AR para ser medida, o que e exatamente o que nenhum portao pode exigir. Sem
# saida, uma regua de ar nasce e vive sem nunca ter sido vista falhar — e o
# contrato chama isso de regua nao medida.
#
# A saida e separar o que ela AFIRMA do lugar de onde ela LE. Com RBM_BANCADA
# apontando para um diretorio, cada estado vem de um arquivo renderizado em vez da
# rede, e as MESMAS afirmacoes correm sobre uma ilha mutada:
# ferramentas/mutacoes-reservatorio.py fabrica o defeito e exige a reprovacao.
# No ar, o modo bancada nao existe — a variavel nao esta no ambiente.
BANCADA = os.environ.get('RBM_BANCADA') or ''

falhas = 0
feitos = 0


def ok(condicao, rotulo, medido=''):
    global falhas, feitos
    feitos += 1
    print('  %s %-62s %s' % ('ok   ' if condicao else 'FALHA', rotulo, medido))
    if not condicao:
        falhas += 1
    return condicao


def buscar(url, tentativas=3):
    """Uma falha de rede so vira bloqueio depois de repetir (secao 20.2)."""
    for _ in range(tentativas):
        # 'Accept-Encoding: identity' entrou em 14/09/2026, pelo item 1 do despacho
        # da Sentinela: `curl` sem cabecalho nenhum recebe uma copia de 11/09 presa
        # no cache, e esta ferramenta vinha conferindo uma pagina que nao existe mais.
        # Quem MEDE o defeito e conferir-no-ar.py, que reprova enquanto ele estiver de
        # pe; aqui o cabecalho existe so para a conferencia ler o que o leitor le.
        r = subprocess.run(['curl', '-s', '-H', 'Accept-Encoding: identity',
                            '-w', '\\n%{http_code}', '--max-time', '40', url],
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
    """SO o bloco que responde a consulta — mesma fronteira do conferir-kits.

    Vai de id="resultado" ate a tabela pre-renderizada (id rbm-exemplos). Fronteira
    nao encontrada devolve vazio E quem chama REPROVA: localizador que nao casa
    tem de gritar, nunca aprovar por ausencia.
    """
    i = corpo.find('id="resultado"')
    if i < 0:
        return ''
    # A FRONTEIRA E UM MARCADOR DECLARADO, e nao "a primeira coisa parecida com
    # uma tabela": `rbm-quadro` e a classe de qualquer quadro, inclusive o de
    # DIVERGENCIAS, que fica dentro da resposta. Ate 13/09/2026 o bloco medido
    # terminava nele, e a tabela de divergencias ficava publicada sem regua.
    fim = corpo.find('id="rbm-exemplos"', i)
    if fim < 0:
        return ''
    return corpo[i:fim]


def texto(bloco):
    """So o texto que um leitor ve: sem marcacao e sem acento."""
    limpo = re.sub(r'<script\b.*?</script>', ' ', bloco, flags=re.S | re.I)
    limpo = re.sub(r'<[^>]+>', ' ', limpo)
    limpo = limpo.replace('&nbsp;', ' ')
    limpo = unicodedata.normalize('NFKD', limpo)
    limpo = ''.join(c for c in limpo if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', limpo).lower()


def sem_acento(s):
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()


def consulta(modelo, tipo):
    return '%s?modelo=%s&peca=%s&v=%s' % (BASE, quote(modelo), quote(tipo),
                                          int(time.time()))


# Cada estado tem NOME, e e pelo nome que o modo bancada acha o arquivo. Estado
# sem arquivo no diretorio REPROVA com 000, nunca aprova por ausencia.
ESTADOS = {
    'ancora': None,
    'w300': ('wap-w300', 'reservatorio'),
    'wsmart': ('wap-wsmart', 'reservatorio'),
    'erb60': ('electrolux-erb60', 'reservatorio'),
    'w100': ('wap-w100', 'reservatorio'),
    'w90': ('wap-w90', 'reservatorio'),
}


def obter(estado):
    """O HTML de um estado: da rede no ar, do disco na bancada."""
    if BANCADA:
        caminho = os.path.join(BANCADA, 'rbm-r1-%s.html' % estado)
        if not os.path.exists(caminho):
            return '', '000'
        with open(caminho, encoding='utf-8') as fh:
            return fh.read(), '200'
    alvo = ESTADOS[estado]
    url = BASE + '?v=%d' % int(time.time()) if alvo is None else consulta(*alvo)
    return buscar(url)


# ------------------------------------------------------------------ A REGUA
#
# Os seis tipos que o vocabulario do banco conhece e que a R1 consulta. A lista
# esta ESCRITA, e nao lida de cobertura-r1.json, pelo motivo do cabecalho: no dia
# em que um tipo novo nascer, esta regua reprova e alguem decide o que a pagina
# deve dizer — em vez de passar a medir sozinha um mundo que ninguem leu.
TIPOS_NO_SELETOR = [
    ('filtro', 'filtro'),
    ('escova lateral', 'escova lateral'),
    ('escova principal', 'escova principal'),
    ('mop', 'mop'),
    ('bateria', 'bateria'),
    ('reservatorio', 'reservatorio'),
]

# Os dois recipientes deste bloco, transcritos do que a loja oficial da WAP
# publica. TITULO e CODIGO ficam separados de proposito: o do WSMART tem codigo e
# o do W300 nao, e essa assimetria e o que a trava de baixo cobra.
RECIPIENTE_W300 = 'Recipiente de Pó Para Robô Aspirador de Pó WAP Robot W300'
RECIPIENTE_WSMART_CODIGO = 'FW008024'

# A TERCEIRA PECA, de 13/09/2026, e a primeira declarada para DOIS modelos. O
# titulo e o codigo sao transcritos do que a loja oficial publica — escritos aqui,
# nao lidos do banco, para as duas metades nao errarem juntas.
RECIPIENTE_W100_W90_CODIGO = 'FW008543'
RECIPIENTE_W100_W90_TITULO = ('Kit Recipiente de Pó Para Robôs Aspiradores de Pó '
                              'WAP Robot W100 e WAP Robot W90')

# OS MODELOS QUE OS REVENDEDORES ANUNCIAM E O FABRICANTE NAO DECLARA. O W100C e o
# unico deles que existe no banco desta ilha, e ele esta no vazio da R1: se a
# extensao por vizinhanca entrasse um dia, e aqui que ela apareceria.
MODELOS_SO_DO_VAREJO = ('W95', 'W96', 'W100C')

# O estado NEGATIVO: um modelo sem reservatorio declarado. O ERB60 e da marca com
# mais pecas do banco — se a recusa falhar em algum, falha aqui.
MODELO_SEM_RESERVATORIO = 'electrolux-erb60'

print('CONFERENCIA NO AR — o tipo reservatorio voltou ao seletor da R1')
print('=' * 78)

# ---------------------------------------------------------- 1. A PAGINA ANCORA
print('\n1. A pagina ancora: o seletor e a promessa que estava escrita nela')
servido, codigo = obter('ancora')
ok(codigo == '200', 'a R1 responde HTTP 200', codigo)
corpo = corpo_da_pagina(servido)
ok(bool(corpo), 'o corpo <main> foi localizado', '%d bytes' % len(corpo))

opcoes = re.findall(r'<option\b[^>]*value="([^"]*)"', corpo)
for valor, rotulo in TIPOS_NO_SELETOR:
    ok(valor in opcoes, "o seletor oferece o tipo '%s'" % rotulo,
       '' if valor in opcoes else 'ausente das %d opcoes servidas' % len(opcoes))

# A PROMESSA CUMPRIDA. A frase da ausencia so pode existir quando ha tipo sem
# peca; com os seis oferecidos ela nao tem o que nomear, e ficar no ar seria a
# pagina afirmando o contrario do proprio seletor, tres linhas acima.
corpo_txt = texto(corpo)
ok('o seletor acima nao oferece' not in corpo_txt,
   'a frase do tipo ausente sumiu da pagina (a promessa era essa)',
   'presente' if 'o seletor acima nao oferece' in corpo_txt else 'ausente')

# ------------------------------------------------------- 2. OS DOIS ESTADOS QUE RESPONDEM
print('\n2. Os dois estados que este bloco criou')

servido, codigo = obter('w300')
ok(codigo == '200', 'W300 + reservatorio responde HTTP 200', codigo)
bloco = bloco_da_resposta(corpo_da_pagina(servido))
ok(bool(bloco), 'o bloco da resposta do W300 foi localizado', '%d bytes' % len(bloco))
w300 = texto(bloco)
ok(sem_acento(RECIPIENTE_W300) in w300,
   'a resposta do W300 cita o titulo publicado pela loja oficial',
   'presente' if sem_acento(RECIPIENTE_W300) in w300 else 'AUSENTE')
ok('nao localizamos' not in w300, 'a resposta do W300 nao recusa',
   'recusou' if 'nao localizamos' in w300 else 'respondeu')
# A TRAVA DO CODIGO EMPRESTADO: este recipiente nao tem codigo de fabricante, e a
# maneira mais barata de mentir aqui seria carregar o da peca vizinha.
codigos_no_w300 = re.findall(r'fw\d{6}', w300)
ok(not codigos_no_w300,
   'a resposta do W300 nao inventa codigo de fabricante (ele nao tem)',
   ', '.join(codigos_no_w300) if codigos_no_w300 else 'nenhum codigo citado')

servido, codigo = obter('wsmart')
ok(codigo == '200', 'WSMART + reservatorio responde HTTP 200', codigo)
bloco = bloco_da_resposta(corpo_da_pagina(servido))
ok(bool(bloco), 'o bloco da resposta do WSMART foi localizado', '%d bytes' % len(bloco))
wsmart = texto(bloco)
ok(RECIPIENTE_WSMART_CODIGO.lower() in wsmart,
   'a resposta do WSMART cita o codigo de fabricante',
   RECIPIENTE_WSMART_CODIGO if RECIPIENTE_WSMART_CODIGO.lower() in wsmart else 'AUSENTE')
ok('nao localizamos' not in wsmart, 'a resposta do WSMART nao recusa',
   'recusou' if 'nao localizamos' in wsmart else 'respondeu')

# ---------------------------------------------------------- 3. A OUTRA DIRECAO
print('\n3. A outra direcao — sem ela as de cima tem porta dos fundos')
servido, codigo = obter('erb60')
ok(codigo == '200', 'ERB60 + reservatorio responde HTTP 200', codigo)
bloco = bloco_da_resposta(corpo_da_pagina(servido))
ok(bool(bloco), 'o bloco da resposta do ERB60 foi localizado', '%d bytes' % len(bloco))
erb60 = texto(bloco)
ok('nao localizamos' in erb60,
   'modelo sem reservatorio declarado RECUSA, e nao responde qualquer coisa',
   'recusou' if 'nao localizamos' in erb60 else 'RESPONDEU ALGO')
ok(sem_acento(RECIPIENTE_W300) not in erb60,
   'a recusa do ERB60 nao vaza o recipiente do W300',
   'limpo' if sem_acento(RECIPIENTE_W300) not in erb60 else 'VAZOU')
ok(RECIPIENTE_WSMART_CODIGO.lower() not in erb60,
   'a recusa do ERB60 nao vaza o codigo do WSMART',
   'limpo' if RECIPIENTE_WSMART_CODIGO.lower() not in erb60 else 'VAZOU')

# ---------------------------------------- 4. A PECA DE FAMILIA E QUEM DIVERGE
print('\n4. A terceira peca: um registro, DOIS modelos, e tres canais que divergem')

# POR QUE ESTES DOIS ESTADOS PRECISAM DOS DOIS: a peca e UMA e os modelos sao
# DOIS. Medir so o W100 deixaria o W90 com porta dos fundos — bastaria a
# compatibilidade do segundo par sumir do banco para a bancada seguir verde.
for estado, rotulo in (('w100', 'W100'), ('w90', 'W90')):
    servido, codigo = obter(estado)
    ok(codigo == '200', '%s + reservatorio responde HTTP 200' % rotulo, codigo)
    bloco = bloco_da_resposta(corpo_da_pagina(servido))
    ok(bool(bloco), 'o bloco da resposta do %s foi localizado' % rotulo,
       '%d bytes' % len(bloco))
    txt = texto(bloco)
    ok('nao localizamos' not in txt, 'a resposta do %s nao recusa' % rotulo,
       'recusou' if 'nao localizamos' in txt else 'respondeu')
    ok(RECIPIENTE_W100_W90_CODIGO.lower() in txt,
       'a resposta do %s cita o codigo de fabricante' % rotulo,
       RECIPIENTE_W100_W90_CODIGO if RECIPIENTE_W100_W90_CODIGO.lower() in txt else 'AUSENTE')
    ok(sem_acento(RECIPIENTE_W100_W90_TITULO).lower() in txt,
       'a resposta do %s cita o titulo publicado pela loja oficial' % rotulo)

    # A ATRIBUICAO. Tres anuncios de revendedor divergem desta peca, e ate
    # 13/09/2026 a pagina os chamava de "canais do FABRICANTE" — na cauda da
    # frase E no titulo do bloco. Sao as duas superficies medidas aqui.
    ok('canais de fora do fabricante declaram' in txt,
       'a pagina do %s diz que quem diverge esta FORA do fabricante' % rotulo)
    ok('canais do fabricante discordam' not in txt
       and 'canais do fabricante declaram' not in txt,
       'e NAO empresta ao fabricante a declaracao de quem revende (%s)' % rotulo,
       'limpo' if 'canais do fabricante' not in txt else 'ATRIBUIU AO FABRICANTE')
    # O NUMERO SAI CONTADO: sao tres canais divergentes, e a frase diz tres.
    ok('tres canais de fora do fabricante' in txt,
       'o numero de canais divergentes sai contado na frase (%s)' % rotulo)

    # A DIVERGENCIA E PUBLICADA, e ela e conteudo: sem ver o que foi descartado,
    # a regra do conjunto mais estreito nao e verificavel por quem le.
    for modelo_do_varejo in MODELOS_SO_DO_VAREJO:
        ok(modelo_do_varejo.lower() in txt,
           'o quadro de divergencia do %s publica o %s que so o varejo declara'
           % (rotulo, modelo_do_varejo))

# E A OUTRA METADE, sem a qual a de cima aprovaria uma pagina que RECOMENDA o
# W100C: o modelo que so o revendedor declara nao pode virar recomendacao. A
# consulta dele nao esta nos estados porque ele continua no vazio da R1 — e e
# justamente isso que esta afirmacao cobra, no estado do W100.
servido, _ = obter('w100')
bloco_w100 = texto(bloco_da_resposta(corpo_da_pagina(servido)))
antes_da_divergencia = bloco_w100.split('canais de fora do fabricante')[0]
ok('w100c' not in antes_da_divergencia,
   'o W100C aparece SO no quadro de divergencia, nunca na recomendacao',
   'limpo' if 'w100c' not in antes_da_divergencia else 'VAZOU PARA A RECOMENDACAO')

# ------------------------------------------------------------- 5. A RECEITA DITA
print('\n5. A receita, dita como ela e (secao 7 e escada da 25)')
# AS DUAS AFIRMACOES FORAM INVERTIDAS EM 14/09/2026. Elas cobravam a PRESENCA de
# "link de loja em breve", que era o estado aceitavel de ontem e virou defeito hoje:
# a secao 7 do contrato proibiu a frase, e o despacho do Raphael mandou o bloco de
# compra servir o piso da 25.2 sempre. Reservar o lugar com uma promessa e a versao
# educada do beco sem saida — quem decidia comprar nao tinha para onde ir.
for _rot, _pag in (('W300', w300), ('WSMART', wsmart)):
    ok('em breve' not in _pag.lower(),
       'o recipiente do %s nao serve a frase proibida pela secao 7' % _rot,
       'ausente' if 'em breve' not in _pag.lower() else 'AINDA NO AR')
    ok('rbm-comprar' in _pag,
       'o recipiente do %s tem saida de compra que clica (25.2)' % _rot,
       'presente' if 'rbm-comprar' in _pag else 'AUSENTE')

print('\n' + '=' * 78)
if falhas:
    print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
    sys.exit(1)
print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)

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
    """SO o bloco que responde a consulta — mesma fronteira do conferir-kits.

    Vai de id="resultado" ate a tabela pre-renderizada (rbm-quadro). Fronteira
    nao encontrada devolve vazio E quem chama REPROVA: localizador que nao casa
    tem de gritar, nunca aprovar por ausencia.
    """
    i = corpo.find('id="resultado"')
    if i < 0:
        return ''
    fim = corpo.find('rbm-quadro', i)
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

# ------------------------------------------------------------- 4. A RECEITA DITA
print('\n4. A receita, dita como ela e (secao 7 e escada da 25)')
ok('link de loja em breve' in w300,
   'o recipiente do W300 reserva o lugar do botao, sem prometer link',
   'presente' if 'link de loja em breve' in w300 else 'AUSENTE')
ok('link de loja em breve' in wsmart,
   'o recipiente do WSMART reserva o lugar do botao, sem prometer link',
   'presente' if 'link de loja em breve' in wsmart else 'AUSENTE')

print('\n' + '=' * 78)
if falhas:
    print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
    sys.exit(1)
print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)

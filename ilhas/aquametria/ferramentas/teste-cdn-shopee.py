#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DE BANCADA DA REGUA DO ESPELHO — sem rede, sem banco.

    python3 ferramentas/teste-cdn-shopee.py

Mede `ferramentas/regua-cdn-shopee.py`: a montagem do endereco espelho e a
leitura de dimensao dos bytes. O irmao no ar e `conferir-espelho-cdn.py`, que
remede o grupo de controle no CDN de verdade.

A DIVISAO ENTRE OS DOIS NAO E CERIMONIA. O que este arquivo afirma e sobre a
NOSSA regra e vale sempre; o que o irmao afirma e sobre a infraestrutura da
Shopee e pode deixar de ser verdade sem aviso. Somar os dois num arquivo so
faria a bancada inteira depender de rede, e regra que so se mede com rede e
regra que ninguem roda quando o tunel cai.
"""

import importlib.util
import os
import struct
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    'regua_cdn', os.path.join(RAIZ, 'ferramentas', 'regua-cdn-shopee.py'))
regua = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(regua)

afirmacoes = 0
falhas = []


def ok(titulo, condicao, detalhe=''):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append('%s%s' % (titulo, (' — ' + detalhe) if detalhe else ''))


def levanta(titulo, funcao, *args):
    global afirmacoes
    afirmacoes += 1
    try:
        funcao(*args)
    except regua.UrlForaDoCdn:
        return
    except Exception as e:                                        # noqa: BLE001
        falhas.append('%s — levantou %s em vez de UrlForaDoCdn' % (titulo, type(e).__name__))
        return
    falhas.append('%s — nao levantou nada' % titulo)


# ---------------------------------------------------------------------------
# O IDENTIFICADOR DO ARQUIVO — o que e o mesmo nos dois hosts
# ---------------------------------------------------------------------------
CASOS_ID = [
    ('https://down-bs-br.img.susercontent.com/sg-11134201-8259h-mge5jlcqmbyhc4.webp',
     'sg-11134201-8259h-mge5jlcqmbyhc4'),
    ('https://cf.shopee.com.br/file/sg-11134201-8259h-mge5jlcqmbyhc4',
     'sg-11134201-8259h-mge5jlcqmbyhc4'),
    ('https://down-bs-br.img.susercontent.com/br-11134207-7r98o-m8eusegtvu9dea.webp',
     'br-11134207-7r98o-m8eusegtvu9dea'),
    # O id SEM prefixo de regiao existe no banco desta ilha (duas midias), e e
    # so um hash. Se a regua supusesse o prefixo `sg-`/`br-`, essas duas fotos
    # ficariam sem espelho e ninguem descobriria — elas ja tem dimensao.
    ('https://cf.shopee.com.br/file/a70f5cb3c45076a03c27e0f7c2f86552',
     'a70f5cb3c45076a03c27e0f7c2f86552'),
    ('https://down-bs-br.img.susercontent.com/2bb44a02215e58113eb2e28a852f5552.webp',
     '2bb44a02215e58113eb2e28a852f5552'),
    # Parametro de consulta nao faz parte do id.
    ('https://cf.shopee.com.br/file/sg-11134201-8259h-mge5jlcqmbyhc4?x=1',
     'sg-11134201-8259h-mge5jlcqmbyhc4'),
]
for url, esperado in CASOS_ID:
    ok('id de %s' % url[-45:], regua.id_do_arquivo(url) == esperado,
       'obtido=%r' % regua.id_do_arquivo(url))


# ---------------------------------------------------------------------------
# A REPRESENTACAO E PRESERVADA — e e ela que decide os bytes
# ---------------------------------------------------------------------------
# `cf.shopee.com.br/file/<id>` devolve JPEG e `.../file/<id>.webp` devolve WebP.
# Medido em 24/09/2026 no mesmo id: 33.317 bytes de JPEG contra 21.150 de WebP.
# A dimensao que vai para o banco descreve a URL que o VISITANTE recebe, entao
# espelho de `.webp` tem de ser `.webp` — medir o JPEG e escrever a medida do
# WebP seria medir uma coisa e declarar outra.
ok('webp espelha para webp',
   regua.espelho('https://down-bs-br.img.susercontent.com/sg-1-x.webp')
   == 'https://cf.shopee.com.br/file/sg-1-x.webp')
ok('sem extensao espelha sem extensao',
   regua.espelho('https://down-bs-br.img.susercontent.com/sg-1-x')
   == 'https://cf.shopee.com.br/file/sg-1-x')
ok('jpg espelha para jpg',
   regua.espelho('https://down-bs-br.img.susercontent.com/sg-1-x.jpg')
   == 'https://cf.shopee.com.br/file/sg-1-x.jpg')
ok('a extensao em MAIUSCULA nao vira id',
   regua.id_do_arquivo('https://down-bs-br.img.susercontent.com/sg-1-x.WEBP') == 'sg-1-x')

# URL QUE JA ESTA NO HOST ALCANCAVEL VOLTA IDENTICA. Espelhar o espelho montaria
# `/file/file/<id>`, que responde 404 — e a regua pareceria quebrada justamente
# nas 8 fotos que vieram da API e nao precisam dela.
ja = 'https://cf.shopee.com.br/file/sg-11134201-8258f-mt5nna6b8a2vc7'
ok('URL ja alcancavel volta identica', regua.espelho(ja) == ja)
ok('e ela NAO precisa de espelho', regua.precisa_de_espelho(ja) is False)
ok('a do host bloqueado PRECISA',
   regua.precisa_de_espelho('https://down-bs-br.img.susercontent.com/x.webp') is True)


# ---------------------------------------------------------------------------
# HOST DESCONHECIDO NAO TEM ESPELHO — a recusa e o coracao da regua
# ---------------------------------------------------------------------------
# Sem esta recusa, `https://loja-qualquer.com/foto.webp` viraria
# `cf.shopee.com.br/file/foto.webp`, que pode responder 200 servindo OUTRA
# imagem. Regua prestativa demais inventa endereco, e endereco inventado que
# responde 200 e pior que erro.
for ruim in ['https://exemplo.com/sg-1-x.webp',
             'https://aquametria.com.br/foto.webp',
             'https://cf.shopee.com.br.exemplo.com/file/x',
             'http://down-bs-br.img.susercontent.com/x.webp',
             'down-bs-br.img.susercontent.com/x.webp',
             'https://down-bs-br.img.susercontent.com/',
             'https://down-bs-br.img.susercontent.com',
             '', None, 42]:
    levanta('espelho recusa %r' % (ruim,), regua.espelho, ruim)


# ---------------------------------------------------------------------------
# A LEITURA DE DIMENSAO — cabecalho de verdade, montado byte a byte
# ---------------------------------------------------------------------------
def jpeg(largura, altura):
    return (b'\xff\xd8'
            + b'\xff\xe0' + struct.pack('>H', 16) + b'JFIF\x00' + b'\x00' * 9
            + b'\xff\xc0' + struct.pack('>H', 17) + b'\x08'
            + struct.pack('>HH', altura, largura) + b'\x03' + b'\x00' * 9)


def png(largura, altura):
    return (b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR'
            + struct.pack('>II', largura, altura) + b'\x08\x06\x00\x00\x00')


def webp_vp8(largura, altura):
    corpo = (b'VP8 ' + struct.pack('<I', 20) + b'\x00' * 3 + b'\x9d\x01\x2a'
             + struct.pack('<H', largura) + struct.pack('<H', altura) + b'\x00' * 6)
    return b'RIFF' + struct.pack('<I', 4 + len(corpo)) + b'WEBP' + corpo


def webp_vp8x(largura, altura):
    corpo = (b'VP8X' + struct.pack('<I', 10) + b'\x00' * 4
             + (largura - 1).to_bytes(3, 'little') + (altura - 1).to_bytes(3, 'little'))
    return b'RIFF' + struct.pack('<I', 4 + len(corpo)) + b'WEBP' + corpo


def webp_vp8l(largura, altura):
    v = (largura - 1) | ((altura - 1) << 14)
    corpo = b'VP8L' + struct.pack('<I', 5) + b'\x2f' + struct.pack('<I', v)
    return b'RIFF' + struct.pack('<I', 4 + len(corpo)) + b'WEBP' + corpo


# OS NUMEROS NAO SAO REDONDOS DE PROPOSITO. 800x800 e 1024x1024 passariam por
# qualquer leitor que devolvesse um valor plausivel, inclusive um que trocasse
# largura por altura. 265, 692, 726 e 1001 sao as dimensoes REAIS de quatro
# fotos desta ilha, e 265x300 separa os dois lados.
for nome, monta in [('JPEG', jpeg), ('PNG', png), ('WebP VP8', webp_vp8),
                    ('WebP VP8X', webp_vp8x), ('WebP VP8L', webp_vp8l)]:
    for L, A in [(265, 265), (1001, 1001), (726, 692), (265, 300)]:
        ok('%s %dx%d' % (nome, L, A),
           regua.dimensao_dos_bytes(monta(L, A)) == (L, A),
           'obtido=%r' % (regua.dimensao_dos_bytes(monta(L, A)),))

# LARGURA E ALTURA NAO PODEM SER TROCADAS, e isto nao e redundante com o acima:
# o JPEG guarda ALTURA primeiro e todos os outros guardam LARGURA primeiro, que
# e o erro mais facil de cometer e o mais dificil de ver em foto quadrada — e
# esta ilha so tem foto quadrada no banco.
ok('JPEG nao troca os lados (altura vem primeiro no arquivo)',
   regua.dimensao_dos_bytes(jpeg(300, 200)) == (300, 200),
   'obtido=%r' % (regua.dimensao_dos_bytes(jpeg(300, 200)),))
ok('PNG nao troca os lados (largura vem primeiro no arquivo)',
   regua.dimensao_dos_bytes(png(300, 200)) == (300, 200),
   'obtido=%r' % (regua.dimensao_dos_bytes(png(300, 200)),))

# O QUE NAO E IMAGEM NAO DEVOLVE NUMERO. Um 404 em HTML, uma pagina de erro do
# proxy ou um arquivo cortado tem de virar None — nunca um par plausivel. E o
# None e o que faz o registro manter `motivo_sem_medida` em vez de publicar uma
# caixa reservada errada.
for lixo in [b'', b'<!DOCTYPE html><html>404</html>', b'\xff\xd8', b'RIFF????WEBP',
             b'RIFFxxxxWEBPVP8 ', b'\x89PNG\r\n\x1a\n', None,
             b'RIFF' + struct.pack('<I', 20) + b'WEBPVP8L' + struct.pack('<I', 5) + b'\x00\x00\x00\x00\x00']:
    ok('lixo nao vira dimensao: %r' % (lixo[:24] if lixo else lixo,),
       regua.dimensao_dos_bytes(lixo) is None,
       'obtido=%r' % (regua.dimensao_dos_bytes(lixo),))

# E ZERO NAO E DIMENSAO. WebP guarda largura-1, entao um arquivo corrompido que
# leia 0 devolveria 1 — nao da para pegar ali. Mas o par (0,0) sai do JPEG e do
# PNG sem esforco, e o V19 do validar-produtos.py recusa `<= 0`. A afirmacao
# existe para que a regua e o validador digam a mesma coisa.
ok('JPEG 0x0 e lido como 0x0 e nao mascarado',
   regua.dimensao_dos_bytes(jpeg(0, 0)) == (0, 0))



# ---------------------------------------------------------------------------
# OS TRES BURACOS QUE AS MUTACOES ACHARAM (24/09/2026)
# ---------------------------------------------------------------------------
# As 54 afirmacoes acima deixaram TRES mutacoes vivas na primeira passada de
# `mutacoes-cdn-shopee.py`. Nenhuma das tres era um caso exotico: as tres eram
# lados da regua que os exemplos escolhidos nao tocavam. Ficam escritas aqui com
# o motivo, porque exemplo bem escolhido e o que separa bancada de cerimonia.

# BURACO 1 — A MASCARA DE 14 BITS DO WEBP VP8 (mutacao 6).
# O campo de largura do VP8 tem 16 bits: os 14 de baixo sao a dimensao e os 2 de
# cima sao a ESCALA. Todas as dimensoes que eu tinha escolhido (265, 692, 726,
# 1001) cabem em 14 bits com os dois bits altos em zero — entao apagar a mascara
# nao mudava resultado nenhum e o portao ficava verde com a regua errada.
# Arquivo real com escala e raro, e e exatamente por isso que so a mutacao o
# acha: o defeito dormiria ate a primeira foto que o tivesse.
def webp_vp8_com_escala(largura, altura, escala_h, escala_v):
    campo_l = (largura & 0x3FFF) | (escala_h << 14)
    campo_a = (altura & 0x3FFF) | (escala_v << 14)
    corpo = (b'VP8 ' + struct.pack('<I', 20) + b'\x00' * 3 + b'\x9d\x01\x2a'
             + struct.pack('<H', campo_l) + struct.pack('<H', campo_a) + b'\x00' * 6)
    return b'RIFF' + struct.pack('<I', 4 + len(corpo)) + b'WEBP' + corpo

for escala_h, escala_v in [(1, 0), (0, 1), (3, 2)]:
    bytes_ = webp_vp8_com_escala(726, 692, escala_h, escala_v)
    ok('WebP VP8 726x692 com escala %d/%d: a escala NAO entra na dimensao'
       % (escala_h, escala_v),
       regua.dimensao_dos_bytes(bytes_) == (726, 692),
       'obtido=%r' % (regua.dimensao_dos_bytes(bytes_),))

# BURACO 2 — O ESPELHO DO ESPELHO (mutacao 9).
# `espelho()` devolve a URL identica quando ela ja esta no host alcancavel. Eu
# afirmava isso com `.../file/<id>`, que e a forma canonica — e remontar a forma
# canonica da a forma canonica, entao a afirmacao passava com e sem o atalho. O
# caso que SEPARA os dois e a URL com parametro de consulta: o atalho a devolve
# inteira, a remontagem joga o parametro fora.
com_query = 'https://cf.shopee.com.br/file/sg-11134201-8258f-mt5nna6b8a2vc7?x=1'
ok('URL ja alcancavel volta INTEIRA, com o parametro de consulta',
   regua.espelho(com_query) == com_query,
   'obtido=%r' % regua.espelho(com_query))

# BURACO 3 — AS TRES TENTATIVAS DA SECAO 20.2 (mutacao 11).
# `medir_no_espelho()` e a unica funcao da regua que toca a rede, e por isso
# nenhuma das 54 afirmacoes a exercia — a bancada inteira roda sem rede de
# proposito. Mas a REPETICAO nao precisa de rede para ser medida: precisa de um
# `urlopen` de mentira que falhe duas vezes e acerte na terceira. Sem esta
# afirmacao, uma intermitencia do tunel viraria `motivo_sem_medida` escrito como
# se fosse diagnostico — que e o defeito de 11/09/2026 na clubedomosaico em
# pessoa, e a razao de a 20.2 existir.
class _Resposta:
    def __init__(self, dados):
        self._dados = dados

    def read(self, _n=None):
        return self._dados

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


_verdadeiro_urlopen = regua.urllib.request.urlopen


def _com_falhas(quantas, dados):
    estado = {'n': 0}

    def falso(_pedido, timeout=None):
        estado['n'] += 1
        if estado['n'] <= quantas:
            raise OSError('tunel caiu na tentativa %d' % estado['n'])
        return _Resposta(dados)
    return falso, estado


try:
    # duas falhas e um acerto: a medida sai, e sai na terceira.
    falso, estado = _com_falhas(2, webp_vp8(726, 692))
    regua.urllib.request.urlopen = falso
    L, A, alvo_url, erro = regua.medir_no_espelho(
        'https://down-bs-br.img.susercontent.com/sg-1-x.webp')
    ok('duas falhas de rede nao impedem a medida', (L, A) == (726, 692),
       'obtido=%r erro=%r' % ((L, A), erro))
    ok('  e foram precisas as tres tentativas', estado['n'] == 3,
       'tentativas=%d' % estado['n'])
    ok('  e o alvo medido e o espelho, nao a URL original',
       alvo_url == 'https://cf.shopee.com.br/file/sg-1-x.webp', 'alvo=%r' % alvo_url)

    # tres falhas: NAO inventa numero, devolve o erro.
    falso, estado = _com_falhas(9, b'')
    regua.urllib.request.urlopen = falso
    L, A, _, erro = regua.medir_no_espelho(
        'https://down-bs-br.img.susercontent.com/sg-1-x.webp')
    ok('tres falhas nao viram dimensao', L is None and A is None,
       'obtido=%r' % ((L, A),))
    ok('  e o erro e dito, nao engolido', bool(erro), 'erro=%r' % erro)
    ok('  e foram exatamente tres tentativas, nao mais', estado['n'] == 3,
       'tentativas=%d' % estado['n'])

    # resposta 200 que NAO e imagem (pagina de erro do proxy): sem numero.
    falso, _ = _com_falhas(0, b'<!DOCTYPE html><html>403</html>')
    regua.urllib.request.urlopen = falso
    L, A, _, erro = regua.medir_no_espelho(
        'https://down-bs-br.img.susercontent.com/sg-1-x.webp')
    ok('200 que nao e imagem nao vira dimensao', L is None and A is None,
       'obtido=%r' % ((L, A),))
    ok('  e o erro diz que o cabecalho nao decodificou',
       'cabecalho' in (erro or ''), 'erro=%r' % erro)
finally:
    regua.urllib.request.urlopen = _verdadeiro_urlopen


print('\n%d afirmacoes, %d falha(s)' % (afirmacoes, len(falhas)))
for f in falhas:
    print('  FALHOU: %s' % f)
sys.exit(1 if falhas else 0)

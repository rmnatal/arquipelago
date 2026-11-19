#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A ESCADA DE JANELAS DO `medir_foto`, PROVADA COM JPEG FABRICADO E UM SERVIDOR DE
LOOPBACK QUE CONTA OS PEDIDOS (19/11/2026).

    python3 ferramentas/teste-janela-da-foto.py

O DEFEITO QUE ESTE PORTAO EXISTE PARA IMPEDIR DE VOLTAR, e ele foi medido numa
foto de verdade desta ilha. `medir_foto` lia os primeiros 32.768 bytes e, se a
dimensao nao saisse dali, respondia:

    os primeiros 32768 bytes nao traziam cabecalho de JPEG, PNG nem WebP

Essa frase e FALSA sobre a foto `sg-11134201-825b4-mu4ds42j0q9x25`, do anuncio
58270189618 (`/veiculos/moto-eletrica/`): ela e um JPEG 1024x1024 que o
navegador pinta, e os primeiros bytes dela TRAZEM o cabecalho de JPEG. Em JPEG a
dimensao mora no segmento **SOF**, que vem depois de todo metadado, e metadado
nao tem teto — naquele arquivo ha Exif de 14.033 bytes, um segundo Exif de 4.487
e um bloco 0xED de 16.114, e o SOF cai no byte **34.780**, a 2 KB da janela.
Faltou JANELA, nunca cabecalho. O custo foi um cartao de produto servindo o
espaco reservado na pagina da consulta de **823 mil buscas/mes**, com a causa
escrita no banco afirmando algo que o arquivo desmente.

POR QUE UM SERVIDOR DE LOOPBACK E NAO UM `medir_foto` COM BYTES NA MAO: o que
este portao precisa provar nao e a leitura do cabecalho — isso o
`dimensao_dos_bytes` faz sozinho e ja tem afirmacao. E a ESCADA: quantos pedidos
saem, de que tamanho, e quando ela se recusa a subir. Isso so se mede do lado de
quem RESPONDE. O servidor nao sai da maquina (127.0.0.1) e nao depende de
egresso nenhum, entao este portao e dos que rodam SEM rede, como o nome dele diz.
"""

import importlib.util
import os
import struct
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

AQUI = os.path.dirname(os.path.abspath(__file__))


def _modulo(nome, caminho):
    espec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(mod)
    return mod


OFERTA = _modulo('coletar_oferta', os.path.join(AQUI, 'coletar-oferta.py'))


# --------------------------------------------------------- arquivos fabricados
def jpeg(largura, altura, bytes_de_metadado=0):
    """Um JPEG valido com `bytes_de_metadado` de lixo ANTES do SOF.

    O metadado vai em segmentos APP1 de 65.533 bytes no maximo, que e o teto de
    um segmento JPEG: e assim que a Shopee empurra o SOF de uma foto de produto
    para depois de 34 KB, e e assim que este portao reproduz o caso.
    """
    corpo = b'\xff\xd8'
    restante = bytes_de_metadado
    while restante > 0:
        tamanho = min(restante, 65533)
        if tamanho < 3:
            break
        corpo += b'\xff\xe1' + struct.pack('>H', tamanho) + b'\x00' * (tamanho - 2)
        restante -= tamanho + 2
    corpo += b'\xff\xc0' + struct.pack('>H', 17) + b'\x08' + struct.pack('>HH', altura, largura)
    corpo += b'\x00' * 10
    corpo += b'\xff\xda' + struct.pack('>H', 12) + b'\x00' * 10
    corpo += b'\x00' * 2048                      # os dados da imagem, que ninguem le aqui
    corpo += b'\xff\xd9'
    return corpo


def png(largura, altura):
    return (b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR'
            + struct.pack('>II', largura, altura) + b'\x08\x06\x00\x00\x00'
            + b'\x00' * 64)


def nao_e_imagem(tamanho):
    return b'%PDF-1.7\n' + b'x' * tamanho


# --------------------------------------------------------- o servidor que conta
class Servidor(ThreadingHTTPServer):
    daemon_threads = True
    arquivos = {}
    pedidos = []


class Mao(BaseHTTPRequestHandler):
    def log_message(self, *_a):            # silencio: o laudo e do portao
        pass

    def do_GET(self):                      # noqa: N802
        conteudo = self.server.arquivos.get(self.path)
        if conteudo is None:
            self.send_response(404)
            self.end_headers()
            return
        faixa = self.headers.get('Range') or ''
        fim = len(conteudo) - 1
        if faixa.startswith('bytes=0-'):
            pedido = int(faixa.split('-', 1)[1])
            fim = min(pedido, len(conteudo) - 1)
        pedaco = conteudo[:fim + 1]
        self.server.pedidos.append({'caminho': self.path, 'faixa': faixa,
                                    'devolvido': len(pedaco)})
        self.send_response(206 if faixa else 200)
        self.send_header('Content-Type', 'image/jpeg')
        self.send_header('Content-Length', str(len(pedaco)))
        if faixa:
            self.send_header('Content-Range', 'bytes 0-%d/%d' % (fim, len(conteudo)))
        self.end_headers()
        self.wfile.write(pedaco)


# --------------------------------------------------------- o portao
def main():
    afirmacoes = 0
    falhas = []

    def exigir(cond, texto):
        nonlocal afirmacoes
        afirmacoes += 1
        if not cond:
            falhas.append(texto)

    # --- a regua pura: o formato se reconhece pelo COMECO e so por ele
    exigir(OFERTA.formato_conhecido(jpeg(8, 8)) == 'JPEG', 'JPEG nao foi reconhecido pelo comeco')
    exigir(OFERTA.formato_conhecido(png(8, 8)) == 'PNG', 'PNG nao foi reconhecido pelo comeco')
    exigir(OFERTA.formato_conhecido(nao_e_imagem(100)) is None,
           'um PDF foi reconhecido como imagem')
    exigir(OFERTA.formato_conhecido(b'') is None, 'bytes vazios foram reconhecidos como imagem')

    # --- a escada declarada, e ela e FECHADA
    exigir(OFERTA.ESCADA_DE_JANELAS[0] == 32768,
           'a primeira janela da escada deixou de ser 32768: o custo de rede da coleta mudou '
           'e isto tem de ser decisao escrita, nao efeito colateral')
    exigir(len(OFERTA.ESCADA_DE_JANELAS) >= 2,
           'a escada com um degrau so E a regua velha: sem segundo degrau nada sobe')
    exigir(list(OFERTA.ESCADA_DE_JANELAS) == sorted(OFERTA.ESCADA_DE_JANELAS),
           'a escada tem de subir: janela menor depois de maior nunca le nada novo')

    # --- quem sobe e quem nao sobe, contado do lado de quem RESPONDE
    srv = Servidor(('127.0.0.1', 0), Mao)
    srv.arquivos = {
        # O CASO MEDIDO: 1024x1024 com o SOF a 34 KB, como a foto de verdade.
        '/sof-depois-da-janela.jpg': jpeg(1024, 1024, bytes_de_metadado=34000),
        # O caso comum: SOF logo no comeco.
        '/sof-na-primeira-janela.jpg': jpeg(800, 800),
        '/png.png': png(300, 200),
        '/pdf.bin': nao_e_imagem(50000),
        # Metadado alem do TETO da escada: isto nao e foto de produto, e o
        # instrumento tem de DIZER isso em vez de subir para sempre.
        '/metadado-sem-fim.jpg': jpeg(640, 480, bytes_de_metadado=600000),
    }
    srv.pedidos = []
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = 'http://127.0.0.1:%d' % srv.server_address[1]

    def medir(caminho):
        srv.pedidos = []
        return OFERTA.medir_foto(base + caminho)

    dim, erro = medir('/sof-na-primeira-janela.jpg')
    exigir(dim == (800, 800), 'SOF na primeira janela: esperava (800, 800), deu %r (%s)' % (dim, erro))
    exigir(len(srv.pedidos) == 1,
           'SOF na primeira janela pediu %d vez(es): a escada subiu sem precisar, e isso e rede '
           'gasta em toda coleta' % len(srv.pedidos))

    dim, erro = medir('/sof-depois-da-janela.jpg')
    exigir(dim == (1024, 1024),
           'O CASO MEDIDO EM 19/11: SOF a 34 KB tem de sair (1024, 1024), deu %r (%s)' % (dim, erro))
    exigir(len(srv.pedidos) == 2,
           'SOF depois da janela pediu %d vez(es): esperava 2 — a primeira janela e o degrau '
           'seguinte, nunca mais' % len(srv.pedidos))

    dim, erro = medir('/png.png')
    exigir(dim == (300, 200), 'PNG: esperava (300, 200), deu %r (%s)' % (dim, erro))
    exigir(len(srv.pedidos) == 1,
           'PNG pediu %d vez(es): em PNG a dimensao esta nos primeiros 24 bytes, entao subir a '
           'escada aqui e baixar arquivo atras de dado que nao esta mais longe' % len(srv.pedidos))

    dim, erro = medir('/pdf.bin')
    exigir(dim is None, 'um PDF devolveu dimensao: %r' % (dim,))
    exigir('nao comecam como JPEG, PNG nem WebP' in (erro or ''),
           'a frase do que NAO e imagem mudou e nao diz mais o que mediu: %r' % erro)
    exigir(len(srv.pedidos) == 1,
           'o PDF pediu %d vez(es): a escada SUBIU atras de dimensao dentro de arquivo que nao '
           'e imagem, e ai ela baixa qualquer coisa inteira' % len(srv.pedidos))

    dim, erro = medir('/metadado-sem-fim.jpg')
    exigir(dim is None, 'metadado de 600 KB antes do SOF devolveu dimensao sem teto: %r' % (dim,))
    exigir('teto da escada' in (erro or ''),
           'o erro do teto nao diz que e teto: %r' % erro)
    exigir(len(srv.pedidos) == len(OFERTA.ESCADA_DE_JANELAS),
           'o teto pediu %d vez(es) para uma escada de %d degraus: ou ela parou antes, ou nao '
           'parou' % (len(srv.pedidos), len(OFERTA.ESCADA_DE_JANELAS)))

    # --- A MUTACAO COBRADA: a regua VELHA, de uma janela so, tem de REPROVAR o
    #     caso medido. Sem isto, as afirmacoes acima passariam numa regua que
    #     nunca sobe, e o portao estaria verde sobre o defeito que o criou.
    srv.pedidos = []
    dim_velha, erro_velha = OFERTA.medir_foto(base + '/sof-depois-da-janela.jpg',
                                              escada=(32768,))
    exigir(dim_velha is None,
           'A REGUA VELHA (uma janela so) NAO REPROVOU o caso medido: ela devolveu %r, logo as '
           'afirmacoes deste portao nao separam a regua nova da velha' % (dim_velha,))
    exigir('teto da escada' in (erro_velha or '') or 'nao apareceu' in (erro_velha or ''),
           'a regua velha reprovou pelo motivo errado: %r' % erro_velha)
    # E ELA NAO PODE REPROVAR AFIRMANDO O QUE O ARQUIVO DESMENTE: a frase antiga
    # dizia que os bytes `nao traziam cabecalho de JPEG, PNG nem WebP`, e eles
    # traziam. Nenhum caminho desta funcao pode voltar a dizer isso de um JPEG.
    exigir('nao traziam cabecalho de JPEG' not in (erro_velha or ''),
           'a frase que afirma coisa errada sobre um JPEG de verdade voltou: %r' % erro_velha)

    srv.shutdown()

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())

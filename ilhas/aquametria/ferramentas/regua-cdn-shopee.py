#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA DO ESPELHO DO CDN DA SHOPEE — medir de um host o arquivo que outro serve.

REGUA COMPARTILHADA, nao portao: nao afirma nada sozinha. Quem afirma sao
`teste-cdn-shopee.py` (bancada, sem rede) e `conferir-espelho-cdn.py` (no ar).

---------------------------------------------------------------------------
POR QUE ELA NASCEU (24/09/2026, mutirao do despacho do Raphael)
---------------------------------------------------------------------------
Esta ilha carregava, desde 09/09/2026, **24 fotos de produto sem largura e sem
altura**. A causa estava medida e certa: o egresso desta nuvem barra
`down-bs-br.img.susercontent.com`, que e o CDN de onde o painel de afiliados
copia a URL da foto. Quem nao alcanca o arquivo nao le o cabecalho, e quem nao
le o cabecalho nao tem dimensao — entao a divida ficou escrita com o motivo, o
que e o certo, e esperando a Sentinela medir uma a uma no Chrome do Raphael.

**O que ninguem tinha perguntado e se o MESMO arquivo respondia em outro
endereco.** Responde. O identificador do arquivo (`sg-11134201-8259h-...`) e o
mesmo nos dois hosts, e `cf.shopee.com.br/file/<id>` — o host que a Open API da
Shopee devolve, e que esta nuvem ALCANCA — serve aquele mesmo arquivo.

---------------------------------------------------------------------------
E A PROVA NAO E O RACIOCINIO ACIMA. E UM GRUPO DE CONTROLE.
---------------------------------------------------------------------------
"Mesmo id, logo mesmo arquivo" e uma hipotese sobre a infraestrutura de outra
empresa, e hipotese sobre infra alheia envelhece calada — que e a doenca que a
secao 4 do contrato paga mais caro. Ela so vira dado porque esta ilha tinha, por
acaso, o grupo de controle perfeito guardado no banco:

**oito fotos hospedadas no host BLOQUEADO cuja dimensao ja estava medida** — e
medida por OUTRO INSTRUMENTO (`naturalWidth` x `naturalHeight` lidos no Chrome
do Raphael pela ronda da Sentinela de 13/09/2026), do outro lado do bloqueio.

Medidas pelo espelho em 24/09/2026: **8 de 8 batem**. E batem em 265, 692, 726 e
1001, que sao justamente os numeros que um redimensionamento nao sobreviveria —
espelho que servisse miniatura padronizada devolveria 800x800 ou 1024x1024 para
todos, e o controle ficaria vermelho na primeira foto torta.

**Por isso o `conferir-espelho-cdn.py` NAO mede so as fotos sem dimensao: ele
remede o grupo de controle a cada passada.** A premissa desta regua e uma
afirmacao sobre um CDN que nao e nosso e pode mudar sem avisar; quando mudar,
quem descobre e o controle ficando vermelho, e nao um cartao com a caixa errada
na tela de alguem.

---------------------------------------------------------------------------
TRES RECUSAS QUE SAO O CORACAO DESTA REGUA
---------------------------------------------------------------------------
1. **O ESPELHO PRESERVA A REPRESENTACAO, e isso nao e detalhe.**
   `cf.shopee.com.br/file/<id>` devolve **JPEG**; `cf.shopee.com.br/file/<id>.webp`
   devolve **WebP**. Sao dois fluxos de bytes diferentes do mesmo arquivo. A
   dimensao que vai para o banco descreve a URL que o VISITANTE recebe, entao o
   espelho de uma URL `.webp` tem de ser `.webp`. Medir o JPEG e declarar a
   medida do WebP seria medir uma coisa e escrever outra — que e a familia
   inteira de defeitos da secao 4.

2. **HOST DESCONHECIDO NAO TEM ESPELHO.** So os hosts de imagem da Shopee
   entram. Uma URL de qualquer outro dominio levanta excecao em vez de virar
   `cf.shopee.com.br/file/<o-que-vier-depois-da-ultima-barra>` — que e como uma
   regua prestativa demais inventa um endereco que responde 200 servindo outra
   coisa.

3. **A URL SERVIDA NAO MUDA.** Esta regua MEDE pelo espelho; ela nao reescreve o
   banco para apontar para o espelho. As oito do controle provam que o host
   bloqueado entrega o arquivo a quem tem navegador — ou seja, ele funciona para
   o visitante, e quem nao alcanca e esta nuvem. Trocar o que o visitante recebe
   para contornar um limite da maquina que constroi o site seria o rabo abanando
   o cachorro. E por isso `verificado_em` continua `null` nas 24: ninguem abriu a
   URL servida e viu a imagem carregar. Tres datas, tres vidas — `coletado_em`,
   `verificado_em` e `medida_em` sao atos diferentes, e agora o terceiro existe.
"""

import struct
import urllib.request

# Os hosts que a Shopee usa para o mesmo servico de imagem. `cf.shopee.com.br` e
# o que a Open API devolve e o unico que esta nuvem alcanca (medido em 24/09/2026:
# os outros tres em 000 nas tres passadas, este em 200 nas tres).
HOSTS_DE_IMAGEM = (
    'down-bs-br.img.susercontent.com',
    'down-br.img.susercontent.com',
    'deo.shopeemobile.com',
    'cf.shopee.com.br',
)

HOST_ALCANCAVEL = 'cf.shopee.com.br'

# As extensoes que a Shopee serve. A lista existe para o espelho preservar a
# representacao — nao para adivinhar uma quando a URL nao traz nenhuma.
EXTENSOES = ('.webp', '.jpg', '.jpeg', '.png')


class UrlForaDoCdn(ValueError):
    """URL que nao e de host de imagem da Shopee. Nao tem espelho, e ponto."""


def _partes(url):
    if not isinstance(url, str) or not url.startswith('https://'):
        raise UrlForaDoCdn('URL sem https: %r' % (url,))
    resto = url[len('https://'):]
    if '/' not in resto:
        raise UrlForaDoCdn('URL sem caminho: %r' % (url,))
    host, caminho = resto.split('/', 1)
    if host not in HOSTS_DE_IMAGEM:
        raise UrlForaDoCdn('host %r nao e CDN de imagem da Shopee' % (host,))
    caminho = caminho.split('?', 1)[0].split('#', 1)[0]
    if not caminho:
        raise UrlForaDoCdn('URL sem arquivo: %r' % (url,))
    return host, caminho


def id_do_arquivo(url):
    """O identificador do arquivo, sem extensao e sem o prefixo /file/.

    E ele que e o mesmo nos dois hosts, e e por ele que o espelho e montado.
    """
    _, caminho = _partes(url)
    nome = caminho.rsplit('/', 1)[-1]
    if not nome:
        raise UrlForaDoCdn('URL terminada em barra: %r' % (url,))
    baixo = nome.lower()
    for ext in EXTENSOES:
        if baixo.endswith(ext):
            return nome[:-len(ext)]
    return nome


def extensao(url):
    """A extensao da URL, em minusculas, ou '' quando ela nao traz nenhuma.

    O espelho a preserva: e o que decide se o CDN devolve WebP ou JPEG, e os
    dois sao bytes diferentes do mesmo arquivo.
    """
    _, caminho = _partes(url)
    baixo = caminho.rsplit('/', 1)[-1].lower()
    for ext in EXTENSOES:
        if baixo.endswith(ext):
            return ext
    return ''


def espelho(url):
    """A URL do MESMO arquivo, na MESMA representacao, no host que esta nuvem alcanca.

    URL que ja esta no host alcancavel volta identica: espelhar o espelho seria
    montar `/file/file/<id>`, que responde 404 e faria a regua parecer quebrada
    onde ela nao tem nada a fazer.
    """
    host, _ = _partes(url)
    if host == HOST_ALCANCAVEL:
        return url
    return 'https://%s/file/%s%s' % (HOST_ALCANCAVEL, id_do_arquivo(url), extensao(url))


def precisa_de_espelho(url):
    """True quando a URL esta num host que esta nuvem nao alcanca."""
    host, _ = _partes(url)
    return host != HOST_ALCANCAVEL


def dimensao_dos_bytes(dados):
    """(largura, altura) lidas do CABECALHO do arquivo, ou None.

    JPEG, PNG e WebP (VP8, VP8L e VP8X) cobrem o que a Shopee serve. Le so o
    comeco: a dimensao mora no cabecalho, e baixar 300 KB por foto para ler 4
    bytes seria gastar rede por nada.

    E a mesma leitura de `coletar-shopee.py:dimensao_da_imagem()`, com VP8L a
    mais — o formato sem perdas, que aquela funcao nao cobria porque nenhuma das
    fotos da API veio nele. Numero deduzido do formato do anuncio nao e medida
    (25.7): ou sai do cabecalho, ou nao sai.
    """
    if not dados:
        return None

    if dados[:2] == b'\xff\xd8':                                  # JPEG
        i = 2
        while i < len(dados) - 9:
            if dados[i] != 0xFF:
                i += 1
                continue
            marcador = dados[i + 1]
            if marcador in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                altura, largura = struct.unpack('>HH', dados[i + 5:i + 9])
                return largura, altura
            if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7:
                i += 2
                continue
            if i + 4 > len(dados):
                return None
            tamanho = struct.unpack('>H', dados[i + 2:i + 4])[0]
            i += 2 + tamanho
        return None

    if dados[:8] == b'\x89PNG\r\n\x1a\n':                         # PNG
        if len(dados) < 24:
            return None
        largura, altura = struct.unpack('>II', dados[16:24])
        return largura, altura

    if dados[:4] == b'RIFF' and dados[8:12] == b'WEBP':           # WebP
        formato = dados[12:16]
        if formato == b'VP8X' and len(dados) >= 30:
            return (int.from_bytes(dados[24:27], 'little') + 1,
                    int.from_bytes(dados[27:30], 'little') + 1)
        if formato == b'VP8 ' and len(dados) >= 30:
            return (struct.unpack('<H', dados[26:28])[0] & 0x3FFF,
                    struct.unpack('<H', dados[28:30])[0] & 0x3FFF)
        if formato == b'VP8L' and len(dados) >= 25:
            if dados[20] != 0x2F:
                return None
            v = int.from_bytes(dados[21:25], 'little')
            return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)
    return None


def medir_no_espelho(url, timeout=30, tentativas=3):
    """(largura, altura, url_medida, erro). Baixa o cabecalho do espelho e le.

    Tres tentativas porque a secao 20.2 manda repetir antes de chamar de
    bloqueio: uma falha isolada e o tunel, tres seguidas sao rede. Sem isso uma
    intermitencia viraria `motivo_sem_medida` escrito como se fosse diagnostico
    — que foi exatamente o que aconteceu em 11/09/2026 com a clubedomosaico.
    """
    alvo = espelho(url)
    ultimo = None
    for _ in range(tentativas):
        try:
            pedido = urllib.request.Request(alvo, headers={'User-Agent': 'aquametria/1.0'})
            with urllib.request.urlopen(pedido, timeout=timeout) as r:
                dados = r.read(262144)
            par = dimensao_dos_bytes(dados)
            if par is None:
                return None, None, alvo, 'cabecalho nao decodificou (%d bytes lidos)' % len(dados)
            return par[0], par[1], alvo, None
        except Exception as e:                                    # noqa: BLE001
            ultimo = '%s: %s' % (type(e).__name__, e)
    return None, None, alvo, ultimo

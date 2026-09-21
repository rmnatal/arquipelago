#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COLHER A FOTO DO FABRICANTE — o braco de coleta do despacho do Raphael de
19/09/2026, que so pode existir com a rede aberta.

A regua `medir-portas-do-fabricante.py` ja diz QUAL pagina abrir para cada
registro sem foto, e diz porque: a porta nao se inventa por busca, ela e a
pagina de onde o dado daquele registro ja foi lido uma vez (`fontes{}.url` e
`canal_brasileiro.valor`). Esta ferramenta abre essa pagina e traz de volta os
CANDIDATOS a foto — nunca grava nada no banco.

**POR QUE ELA NAO GRAVA, e isto nao e timidez.** A secao 25.3 do contrato manda
abrir cada imagem COM OS OLHOS antes de gravar, e olho nao se automatiza. O que
esta ferramenta entrega e uma lista de candidatos com a PROVA de procedencia ao
lado, para o julgamento humano ser feito sobre dado medido em vez de sobre
palpite. Quem grava e `aplicar-fotos-do-fabricante.py`, depois do olho.

AS TRES ESTRATEGIAS, e cada uma existe porque um fabricante desta ilha usa uma:

  vtex     loja.electrolux.com.br, www.multilaser.com.br, loja.wap.ind.br,
           www.positivocasainteligente.com.br, loja.meupositivo.com.br.
           O HTML e renderizado por JavaScript e nao carrega a foto; o catalogo
           publico (`/api/catalog_system/pub/products/search/<slug>/p`) carrega,
           e carrega junto o `productReference` — que E o codigo do fabricante.
           **Isso transforma a amarra da 25.3 em medicao:** "a pagina nomeia o
           codigo" deixa de ser leitura de texto e vira igualdade de campo.

  shopify  us.roborock.com. `<url>.json` devolve titulo, imagens e as DIMENSOES
           reais de cada uma, que o banco pede e que de outro jeito sairiam de
           um download so para medir.

  html     o resto. og:image e JSON-LD, com o texto da pagina varrido atras do
           codigo. E a estrategia mais fraca das tres e ela se declara assim no
           relatorio, em vez de passar por medicao.

  python3 ferramentas/coletar-foto-do-fabricante.py
  python3 ferramentas/coletar-foto-do-fabricante.py --so xiaomi,roborock
  python3 ferramentas/coletar-foto-do-fabricante.py --saida dados/candidatos.json

Prefixo `coletar-` = ferramenta de producao, fora da bancada (ver bancada.py).
"""

import argparse
import html as htmllib
import importlib.util
import json
import os
import re
import subprocess
import sys
from urllib.parse import urlparse, unquote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# A data da colheita NAO se digita: colheita e medicao, e medicao carrega o dia
# em que foi feita. Ate 21/09/2026 este nome e o `gerado_em` estavam fixos em
# '2026-09-20' — entao a passada de hoje sobrescreveria a de ontem carimbada com
# a data de ontem, e o relatorio diria 20/09 sobre numero colhido em 21/09.
HOJE = __import__('datetime').date.today().isoformat()
SAIDA_PADRAO = 'dados/candidatos-de-foto-%s.json' % HOJE
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'

# Hosts cujo HTML nao carrega a foto porque a loja e VTEX. Nao e lista de
# fabricante — e lista de TECNOLOGIA, e por isso mora aqui e nao em marcas.json.
VTEX = (
    'loja.electrolux.com.br',
    'www.multilaser.com.br',
    'loja.wap.ind.br',
    'www.positivocasainteligente.com.br',
    'loja.meupositivo.com.br',
    'www.multilaserempresas.com.br',
)
SHOPIFY = ('us.roborock.com', 'br.roborock.com')

# Ruido que toda loja serve e que nunca e foto de produto: bandeira de cartao,
# selo, banner de campanha, logo. Sem este filtro o primeiro candidato de uma
# pagina VTEX e quase sempre um icone de bandeira.
LIXO = re.compile(
    r'(file-manager|vtex\.file|/assets/|logo|banner|selo|bandeira|icon|sprite|'
    r'favicon|placeholder|loading|gif$)', re.I)


# O OLHO TAMBEM DEIXA RASTRO. A 25.3 manda abrir cada imagem com os olhos antes
# de gravar, e ate hoje o resultado desse olhar nao morava em lugar nenhum: a
# foto aprovada virava campo no banco e a REPROVADA sumia, entao a execucao
# seguinte reabria o mesmo arquivo para chegar a mesma conclusao. Aqui ficam as
# reprovadas, com a data e o motivo — e o relatorio as tira de "pode gravar
# hoje", que e onde elas estariam sem este dicionario.
REPROVADAS_PELO_OLHO = {
    'wap-wsmart': (
        '2026-09-20: a unica imagem que ABRE desta nuvem em toda a colheita, e ela '
        'nao serve. E o banner de lancamento do blog da WAP (1516x907), com '
        '"LANCAMENTO" num selo azul e o nome do produto em letra de cartaz ocupando '
        'metade do quadro. Procedencia passa — e do fabricante e nomeia o WSMART —, '
        'mas nao e foto de produto: no espaco quadrado do cartao ela entra como '
        'peca de campanha de 2020, com texto promocional que a ilha nao escreveu e '
        'nao pode datar. Foto e ganho e nunca requisito (25.3); espaco reservado '
        'neutro e melhor que cartaz velho.'),
}

def _medir():
    """Importa a regua de portas. O nome tem hifen, entao nao ha import direto."""
    caminho = os.path.join(RAIZ, 'ferramentas', 'medir-portas-do-fabricante.py')
    spec = importlib.util.spec_from_file_location('medir_portas', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def baixar(url, tempo=40):
    """curl porque e o mesmo canal que a regua de portas mede. Devolve (codigo, corpo)."""
    try:
        r = subprocess.run(
            ['curl', '-sL', '--compressed', '-A', UA, '--max-time', str(tempo),
             '-w', '\n__HTTP__%{http_code}', url],
            capture_output=True, text=True, timeout=tempo + 15)
    except (subprocess.SubprocessError, OSError) as erro:
        return '000', 'erro: %s' % erro
    corpo = r.stdout or ''
    marca = corpo.rfind('\n__HTTP__')
    if marca < 0:
        return '000', corpo
    return corpo[marca + 9:].strip(), corpo[:marca]


def slug_vtex(url):
    partes = [p for p in urlparse(url).path.split('/') if p]
    if len(partes) >= 2 and partes[-1] == 'p':
        return unquote(partes[-2])
    return None


def colher_vtex(porta):
    host = urlparse(porta).netloc
    slug = slug_vtex(porta)
    if not slug:
        return {'estrategia': 'vtex', 'falha': 'a URL nao tem a forma /<slug>/p'}
    codigo, corpo = baixar('https://%s/api/catalog_system/pub/products/search/%s/p' % (host, slug))
    if codigo != '200':
        return {'estrategia': 'vtex', 'falha': 'catalogo devolveu %s' % codigo}
    try:
        dados = json.loads(corpo)
    except ValueError:
        return {'estrategia': 'vtex', 'falha': 'catalogo nao devolveu JSON'}
    if not dados:
        return {'estrategia': 'vtex', 'falha': 'catalogo devolveu lista vazia'}
    p = dados[0]
    fotos = []
    for item in p.get('items') or []:
        for im in item.get('images') or []:
            u = im.get('imageUrl')
            if u and not LIXO.search(u):
                fotos.append({'url': u, 'alt': im.get('imageLabel') or im.get('imageText') or None})
    return {
        'estrategia': 'vtex',
        'nome_na_pagina': p.get('productName'),
        'referencia_na_pagina': p.get('productReference'),
        'skus': [i.get('itemId') for i in (p.get('items') or [])][:4],
        'texto': ' '.join(str(x) for x in [
            p.get('productName'), p.get('productReference'), p.get('description'),
            ' '.join(i.get('name') or '' for i in (p.get('items') or [])),
            ' '.join((i.get('referenceId') or [{}])[0].get('Value') or ''
                     for i in (p.get('items') or []) if i.get('referenceId')),
        ] if x),
        'fotos': fotos[:8],
    }


def colher_shopify(porta):
    base = porta.split('?')[0].rstrip('/')
    codigo, corpo = baixar(base + '.json')
    if codigo != '200':
        return {'estrategia': 'shopify', 'falha': 'produto .json devolveu %s' % codigo}
    try:
        p = json.loads(corpo)['product']
    except (ValueError, KeyError):
        return {'estrategia': 'shopify', 'falha': 'resposta nao e produto'}
    fotos = [{'url': i['src'].split('?')[0] + ('?' + i['src'].split('?')[1] if '?' in i['src'] else ''),
              'largura': i.get('width'), 'altura': i.get('height'), 'alt': i.get('alt')}
             for i in (p.get('images') or []) if not LIXO.search(i.get('src', ''))]
    return {
        'estrategia': 'shopify',
        'nome_na_pagina': p.get('title'),
        'referencia_na_pagina': (p.get('variants') or [{}])[0].get('sku') or None,
        'texto': ' '.join(str(x) for x in [p.get('title'), p.get('body_html'),
                                           ' '.join(v.get('title') or '' for v in (p.get('variants') or []))] if x),
        'fotos': fotos[:8],
    }


TAG = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
SEM_TAG = re.compile(r'<[^>]+>')


def colher_html(porta):
    codigo, corpo = baixar(porta)
    if codigo != '200':
        return {'estrategia': 'html', 'falha': 'pagina devolveu %s' % codigo}
    fotos = []
    for m in re.finditer(r'<meta[^>]+property=["\']og:image["\'][^>]*>', corpo, re.I):
        c = re.search(r'content=["\']([^"\']+)["\']', m.group(0))
        if c and not LIXO.search(c.group(1)):
            fotos.append({'url': htmllib.unescape(c.group(1)), 'alt': None})
    for m in re.finditer(r'"image"\s*:\s*("(?:[^"\\]|\\.)*"|\[[^\]]*\])', corpo):
        for u in re.findall(r'https?://[^"\\\s]+', m.group(1)):
            if not LIXO.search(u):
                fotos.append({'url': htmllib.unescape(u), 'alt': None})
    texto = SEM_TAG.sub(' ', TAG.sub(' ', corpo))
    texto = htmllib.unescape(re.sub(r'\s+', ' ', texto))[:20000]
    vistas, unicas = set(), []
    for f in fotos:
        if f['url'] not in vistas:
            vistas.add(f['url'])
            unicas.append(f)
    return {'estrategia': 'html', 'nome_na_pagina': None,
            'referencia_na_pagina': None, 'texto': texto, 'fotos': unicas[:8]}


def colher(porta):
    host = urlparse(porta).netloc.lower()
    if host in VTEX:
        r = colher_vtex(porta)
        if r.get('fotos'):
            return r
        alt = colher_html(porta)
        alt['aviso'] = 'catalogo VTEX nao serviu: %s' % r.get('falha', 'sem foto')
        return alt
    if host in SHOPIFY:
        r = colher_shopify(porta)
        if r.get('fotos'):
            return r
        alt = colher_html(porta)
        alt['aviso'] = 'produto .json nao serviu: %s' % r.get('falha', 'sem foto')
        return alt
    return colher_html(porta)


def nomeia(colheita, reg):
    """A amarra da 25.3, medida: a pagina nomeia o codigo ou o modelo EXATO?

    Devolve (veredito, prova). Ha tres forcas de prova, e elas estao em ordem:

      `referencia`  o campo que a loja usa para o codigo do fabricante bate com
                    `codigo_fabricante`. E a mais forte que existe: igualdade de
                    campo nao e coincidencia de texto.
      `texto`       o codigo aparece escrito na pagina.
      `tokens`      o registro NAO TEM codigo de fabricante (as pecas da WAP e
                    da Roborock nao tem), entao a prova e o par nome-do-modelo +
                    tipo-da-peca aparecendo os DOIS na pagina. Cada palavra e
                    procurada por conta propria, porque "escova direita w300"
                    nunca sai nessa ordem no titulo de uma loja. A prova impressa
                    traz o trecho de cada palavra, para o olho conferir que nao
                    casou por acaso.

    Token de uma letra ou dois digitos nao entra: casaria em qualquer pagina.
    """
    codigo = (reg.get('codigo') or '').strip()
    texto = (colheita.get('texto') or '')
    ref = (colheita.get('referencia_na_pagina') or '').strip()
    if codigo:
        se = re.escape(codigo).replace(r'\ ', r'[\s-]*')
        if ref and re.search(se, ref, re.I):
            return 'referencia', '%s == %s' % (ref, codigo)
        m = re.search(r'.{0,60}' + se + r'.{0,60}', texto, re.I)
        if m:
            return 'texto', m.group(0).strip()
        return 'NAO', ''
    # Sem codigo de fabricante: o par modelo + tipo tem que aparecer inteiro.
    sufixo = reg['id'].split('-', 1)[-1]
    tokens = [t for t in re.split(r'[-\s]+', sufixo) if len(t) > 2]
    if not tokens:
        return 'NAO', ''
    provas = []
    for t in tokens:
        m = re.search(r'.{0,40}' + re.escape(t) + r'.{0,40}', texto, re.I)
        if not m:
            return 'NAO', 'faltou a palavra "%s"' % t
        provas.append('%s -> ...%s...' % (t, m.group(0).strip()))
    return 'tokens', ' | '.join(provas)


# ---------------------------------------------------------------------------
# O RELATORIO — e ele mede uma coisa que a coleta nao mede
# ---------------------------------------------------------------------------
# A pagina do fabricante e a FOTO nao moram no mesmo host, e foi so ao tentar
# baixar as 37 fotos de 20/09/2026 que isso apareceu: as paginas abriram e as
# imagens nao. Loja VTEX serve o HTML em `loja.marca.com.br` e o arquivo em
# `marca.vteximg.com.br`; a Roborock serve em `cdn.shopify.com`; a Xiaomi em
# `i0N.appmifile.com`. Liberar o dominio da pagina nao libera a foto, e a 25.3
# manda ABRIR a imagem com os olhos antes de gravar — entao host de imagem
# fechado e o mesmo bloqueio de antes, um andar adiante.
#
# Por isso o relatorio mede os DOIS hosts por registro, separados: o da porta
# (que a regua de portas ja media) e o do ARQUIVO da foto (que ninguem media).

def medir_host_de_imagem(url):
    import socket as _s
    u = 'https:' + url if url.startswith('//') else url
    host = urlparse(u).netloc.lower()
    try:
        _s.getaddrinfo(host, 443)
        dns = 'resolve'
    except _s.gaierror:
        return host, 'NAO_RESOLVE', None
    try:
        r = subprocess.run(['curl', '-sLo', os.devnull, '--compressed', '-A', UA,
                            '--max-time', '25', '-w', '%{http_code}', u],
                           capture_output=True, text=True, timeout=45)
        codigo = (r.stdout or '').strip()
    except (subprocess.SubprocessError, OSError):
        codigo = '000'
    return host, dns, codigo


def relatorio(caminho_json, caminho_md):
    with open(os.path.join(RAIZ, caminho_json), encoding='utf-8') as fp:
        dados = json.load(fp)
    medidos, hosts = {}, {}
    for r in dados['registros']:
        c = r.get('colheita')
        if not c or not c.get('fotos') or c['veredito_nome'] == 'NAO':
            continue
        u = c['fotos'][0]['url']
        host = urlparse('https:' + u if u.startswith('//') else u).netloc.lower()
        if host not in hosts:
            hosts[host] = medir_host_de_imagem(u)
        medidos[r['id']] = (u, host)

    pronto, preso, sem, olho = [], [], [], []
    for r in dados['registros']:
        c = r.get('colheita')
        if not c or not c.get('fotos') or c['veredito_nome'] == 'NAO':
            sem.append(r)
            continue
        u, host = medidos[r['id']]
        if r['id'] in REPROVADAS_PELO_OLHO:
            olho.append((r, u, host))
        elif (hosts[host][2] or '').startswith('2'):
            pronto.append((r, u, host))
        else:
            preso.append((r, u, host))

    L = []
    L.append('# A FOTO DO FABRICANTE — colheita de %s' % dados.get('gerado_em', '?'))
    L.append('')
    L.append('Gerada por `ferramentas/coletar-foto-do-fabricante.py --relatorio`, para o')
    L.append('**despacho do Raphael de 19/09/2026**. **Nenhum numero foi digitado:** os')
    L.append('registros saem dos dois arquivos de banco, as portas saem de `fontes{}.url` e')
    L.append('`canal_brasileiro.valor`, os candidatos saem do catalogo publico de cada loja')
    L.append('e o estado de cada host de imagem sai de uma consulta de DNS mais um `curl`.')
    L.append('')
    L.append('## O placar')
    L.append('')
    L.append('| | |')
    L.append('|---|---|')
    L.append('| publicaveis sem foto (o alvo do despacho) | **%d** |' % len(dados['registros']))
    L.append('| com candidato E com o nome medido na pagina | **%d** |'
             % (len(pronto) + len(preso) + len(olho)))
    L.append('| ... cujo ARQUIVO da foto abre daqui (pode gravar hoje) | **%d** |' % len(pronto))
    L.append('| ... cujo arquivo esta em host de imagem fechado | **%d** |' % len(preso))
    L.append('| ... reprovado pelo OLHO, com o motivo escrito | **%d** |' % len(olho))
    L.append('| sem candidato (causa registro a registro, abaixo) | **%d** |' % len(sem))
    L.append('')
    L.append('## Os hosts de IMAGEM, um a um')
    L.append('')
    L.append('Nenhum deles e o host da pagina. Esta e a metade que o pedido de 20/09 nao')
    L.append('cobria, porque ninguem tinha tentado baixar o arquivo.')
    L.append('')
    L.append('| host da imagem | DNS | HTTP | registros |')
    L.append('|---|---|---|---|')
    conta = {}
    for _r, _u, h in pronto + preso + olho:
        conta[h] = conta.get(h, 0) + 1
    for h, n in sorted(conta.items(), key=lambda x: -x[1]):
        _, dns, codigo = hosts[h]
        L.append('| `%s` | %s | %s | %d |' % (h, dns, codigo, n))
    L.append('')
    L.append('## Pode gravar hoje')
    L.append('')
    if pronto:
        L.append('| registro | prova do nome | foto |')
        L.append('|---|---|---|')
        for r, u, _h in sorted(pronto, key=lambda x: x[0]['id']):
            L.append('| `%s` | %s | %s |' % (r['id'], r['colheita']['veredito_nome'], u))
    else:
        L.append('Nenhum. Todos os candidatos medidos estao em host de imagem fechado.')
    L.append('')
    L.append('## Reprovado pelo olho (25.3), com o motivo')
    L.append('')
    if olho:
        L.append('| registro | foto que foi aberta | por que nao entra |')
        L.append('|---|---|---|')
        for r, u, _h in sorted(olho, key=lambda x: x[0]['id']):
            L.append('| `%s` | %s | %s |' % (r['id'], u, REPROVADAS_PELO_OLHO[r['id']]))
    else:
        L.append('Nenhuma imagem chegou a ser aberta nesta passada.')
    L.append('')
    L.append('## Tem candidato e o arquivo nao abre daqui')
    L.append('')
    L.append('Estes **nao** sao duvida de procedencia: o nome do registro foi medido na')
    L.append('pagina do fabricante, e a URL exata da foto esta escrita aqui. Falta so o')
    L.append('host da imagem na lista de dominios permitidos.')
    L.append('')
    L.append('| registro | marca | tipo | prova do nome | foto |')
    L.append('|---|---|---|---|---|')
    for r, u, _h in sorted(preso, key=lambda x: x[0]['id']):
        L.append('| `%s` | %s | %s | %s | %s |'
                 % (r['id'], r['marca'], r['tipo'], r['colheita']['veredito_nome'], u))
    L.append('')
    L.append('## Sem candidato, por causa')
    L.append('')
    L.append('| registro | porta | causa medida |')
    L.append('|---|---|---|')
    for r in sorted(sem, key=lambda x: x['id']):
        c = r.get('colheita')
        if not c:
            causa = r.get('motivo') or 'sem porta de fabricante aberta'
            porta = ''
        else:
            porta = c.get('porta') or ''
            if c.get('falha'):
                causa = c['falha']
            elif not c.get('fotos'):
                causa = 'a pagina abre e nao serve foto de produto no HTML (%s)' % c['estrategia']
            else:
                causa = 'a pagina nao nomeia este registro: %s' % (c.get('prova_nome') or 'sem prova')
        L.append('| `%s` | %s | %s |' % (r['id'], porta, causa.replace('|', '/')))
    L.append('')
    with open(os.path.join(RAIZ, caminho_md), 'w', encoding='utf-8') as fp:
        fp.write('\n'.join(L) + '\n')
    print('%d pode(m) gravar hoje, %d preso(s) em host de imagem, %d reprovado(s) pelo '
          'olho, %d sem candidato -> %s'
          % (len(pronto), len(preso), len(olho), len(sem), caminho_md))
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--so', default='')
    ap.add_argument('--saida', default=SAIDA_PADRAO)
    ap.add_argument('--relatorio', default='',
                    help='le o JSON ja colhido e escreve o relatorio em markdown')
    args = ap.parse_args(argv)
    marcas = {m.strip() for m in args.so.split(',') if m.strip()}
    if args.relatorio:
        return relatorio(args.saida, args.relatorio)

    medir = _medir()
    registros, hosts = medir.medir(com_rede=True)
    abertos = {h for h, d in hosts.items() if d and d['veredito'] == 'aberto'}

    saida = []
    for reg in registros:
        if marcas and reg['marca'] not in marcas:
            continue
        portas = [p for p in reg['portas'] if p['especie'] == 'fabricante' and p['host'] in abertos]
        if not portas:
            saida.append(dict(reg, portas=[p['url'] for p in reg['portas']],
                              colheita=None, motivo='sem porta de fabricante aberta'))
            continue
        melhor = None
        for porta in portas:
            c = colher(porta['url'])
            c['porta'] = porta['url']
            c['veredito_nome'], c['prova_nome'] = nomeia(c, reg)
            c.pop('texto', None)
            if c.get('fotos') and c['veredito_nome'] != 'NAO':
                melhor = c
                break
            melhor = melhor or c
        saida.append({'id': reg['id'], 'marca': reg['marca'], 'arquivo': reg['arquivo'],
                      'entidade': reg['entidade'], 'codigo': reg['codigo'],
                      'tipo': reg['tipo'], 'colheita': melhor})
        pronto = melhor and melhor.get('fotos') and melhor['veredito_nome'] != 'NAO'
        print('%-42s %-8s %s' % (reg['id'], reg['marca'],
                                 'CANDIDATO' if pronto else 'sem candidato'), flush=True)

    caminho = os.path.join(RAIZ, args.saida)
    with open(caminho, 'w', encoding='utf-8') as fp:
        json.dump({'gerado_em': HOJE, 'alvo': len(saida), 'registros': saida},
                  fp, ensure_ascii=False, indent=1)
        fp.write('\n')
    com = sum(1 for r in saida if r.get('colheita') and r['colheita'].get('fotos')
              and r['colheita']['veredito_nome'] != 'NAO')
    print('\n%d de %d com candidato e com o nome medido na pagina. -> %s'
          % (com, len(saida), args.saida))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

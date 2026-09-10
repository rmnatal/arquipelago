#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escreve o mapa de meta description dentro de snippets/aquametria-seo-tecnico.php.

    python3 ferramentas/gerar-metas-descricao.py .            # grava
    python3 ferramentas/gerar-metas-descricao.py . --conferir  # so confere

Nasce do despacho da Sentinela de 10/09/2026, item 1: nenhuma das 13 URLs do
sitemap servia <meta name="description">, e nenhuma pagina tinha tag og:.

POR QUE GERADO, E NAO ESCRITO A MAO. O texto de cada pagina de conteudo ja mora
no front matter dela (campo `meta_descricao`), que e o lugar natural: quem edita
a pagina edita a descricao junto, na mesma tela. As quatro paginas da casca nao
tem arquivo em conteudo/ — elas nascem do snippet — entao a descricao delas mora
em dados/metas-seo.json. Sao dois lugares porque sao dois tipos de pagina, mas
NENHUMA pagina aparece nos dois. Descricao mantida em dois lugares diverge em
silencio, que e exatamente o defeito que o favicon evitou sendo gerado tambem
(ver o cabecalho da secao 2b da casca).

O QUE ELE RECUSA GERAR, e por que cada recusa existe:
  - texto fora de 120 a 160 caracteres — e a faixa que o proprio despacho cobra,
    e o que o Google costuma exibir sem cortar no meio da frase;
  - texto repetido em duas paginas — description igual em duas URLs devolve ao
    Google o sinal de duplicata, que e pior do que nao ter description;
  - slug do sitemap sem descricao, ou descricao para slug que nao existe — as 13
    URLs sao conferidas contra a lista abaixo, para o mapa nao envelhecer em
    silencio quando uma pagina nascer ou morrer.
"""

from __future__ import print_function

import io
import json
import os
import re
import sys

# As 13 URLs do sitemap, medidas pela Sentinela em 10/09/2026. Pagina nova entra
# aqui no mesmo commit em que entra no site — a recusa e o alarme.
SLUGS_ESPERADOS = [
    'inicio',
    'calculadoras',
    'metodologia',
    'sobre',
    'calculadora-de-litragem',
    'calculadora-de-vazao-do-filtro',
    'calculadora-de-potencia-do-aquecedor',
    'calculadora-de-midia-filtrante',
    'calculadora-de-iluminacao',
    'divulgacao-de-afiliados',
    'quantos-watts-de-aquecedor-para-aquario',
    'quanta-midia-biologica-o-aquario-precisa',
    'quantos-lumens-por-litro-aquario-plantado',
]

MIN_CARACTERES = 120
MAX_CARACTERES = 160

INICIO = '/* METAS-INICIO — gerado por ferramentas/gerar-metas-descricao.py, nao edite a mao */'
FIM = '/* METAS-FIM */'


def ler_front_matter(caminho):
    """Le so os campos de uma linha que interessam. Nao e um parser de YAML."""
    with io.open(caminho, encoding='utf-8') as fh:
        texto = fh.read()
    if not texto.lstrip('﻿').startswith('---'):
        return None
    corpo = texto.lstrip('﻿')
    fim = corpo.find('\n---', 3)
    if fim < 0:
        return None
    campos = {}
    for linha in corpo[3:fim].splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', linha)
        if not m:
            continue
        valor = m.group(2).strip()
        if valor.startswith('"') and valor.endswith('"') and len(valor) > 1:
            valor = valor[1:-1].replace('\\"', '"')
        campos[m.group(1)] = valor
    return campos


def coletar(raiz):
    """Devolve {slug: {'titulo':..., 'descricao':..., 'origem':...}} e a lista de erros."""
    metas = {}
    erros = []

    caminho_json = os.path.join(raiz, 'dados', 'metas-seo.json')
    with io.open(caminho_json, encoding='utf-8') as fh:
        dados = json.load(fh)
    for slug, item in dados.get('paginas_da_casca', {}).items():
        metas[slug] = {
            'titulo': item.get('titulo', ''),
            'descricao': item.get('meta_descricao', ''),
            'origem': 'dados/metas-seo.json',
        }

    pasta = os.path.join(raiz, 'conteudo')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.md') or nome == 'README.md':
            continue
        campos = ler_front_matter(os.path.join(pasta, nome))
        if campos is None:
            continue
        slug = campos.get('slug', '')
        if not slug:
            continue
        if campos.get('publicar', 'true') == 'false':
            continue
        if slug in metas:
            erros.append('slug "%s" aparece no JSON da casca E em conteudo/%s' % (slug, nome))
            continue
        metas[slug] = {
            'titulo': campos.get('titulo', ''),
            'descricao': campos.get('meta_descricao', ''),
            'origem': 'conteudo/' + nome,
        }

    return metas, erros


def conferir(metas, erros):
    vistos = {}
    for slug in sorted(metas):
        item = metas[slug]
        texto = item['descricao']
        if not texto:
            erros.append('%s: sem meta_descricao (%s)' % (slug, item['origem']))
            continue
        n = len(texto)
        if n < MIN_CARACTERES or n > MAX_CARACTERES:
            erros.append('%s: %d caracteres, fora da faixa %d a %d (%s)'
                         % (slug, n, MIN_CARACTERES, MAX_CARACTERES, item['origem']))
        chave = texto.strip().lower()
        if chave in vistos:
            erros.append('%s: descricao identica a de %s' % (slug, vistos[chave]))
        else:
            vistos[chave] = slug
        if not item['titulo']:
            erros.append('%s: sem titulo (%s)' % (slug, item['origem']))

    for slug in SLUGS_ESPERADOS:
        if slug not in metas:
            erros.append('slug do sitemap sem descricao: %s' % slug)
    for slug in sorted(metas):
        if slug not in SLUGS_ESPERADOS:
            erros.append('descricao para slug que nao esta na lista do sitemap: %s' % slug)
    return erros


def php_texto(valor):
    return "'" + valor.replace('\\', '\\\\').replace("'", "\\'") + "'"


def montar_php(metas):
    linhas = [
        INICIO,
        "if ( ! function_exists( 'aquametria_seo_metas_por_slug' ) ) {",
        'function aquametria_seo_metas_por_slug() {',
        '\treturn array(',
    ]
    for slug in SLUGS_ESPERADOS:
        item = metas[slug]
        linhas.append('\t\t%s => array(' % php_texto(slug))
        linhas.append("\t\t\t'titulo'    => %s," % php_texto(item['titulo']))
        linhas.append("\t\t\t'descricao' => %s," % php_texto(item['descricao']))
        linhas.append('\t\t),')
    linhas += ['\t);', '}', '}', FIM]
    return '\n'.join(linhas)


def main():
    raiz = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else '.'
    so_conferir = '--conferir' in sys.argv

    metas, erros = coletar(raiz)
    erros = conferir(metas, erros)
    if erros:
        for e in erros:
            print('FALHA  ' + e)
        print('%d problema(s). Nada foi gravado.' % len(erros))
        return 1

    for slug in SLUGS_ESPERADOS:
        print('ok  %3d  %-42s %s' % (len(metas[slug]['descricao']), slug, metas[slug]['origem']))

    alvo = os.path.join(raiz, 'snippets', 'aquametria-seo-tecnico.php')
    with io.open(alvo, encoding='utf-8') as fh:
        src = fh.read()
    if INICIO not in src or FIM not in src:
        print('FALHA  marcadores METAS-INICIO/METAS-FIM ausentes em %s' % alvo)
        return 1

    novo_bloco = montar_php(metas)
    antes = src[:src.index(INICIO)]
    depois = src[src.index(FIM) + len(FIM):]
    resultado = antes + novo_bloco + depois

    if so_conferir:
        if resultado != src:
            print('FALHA  o snippet esta desatualizado; rode sem --conferir.')
            return 1
        print('snippet em dia com as %d descricoes.' % len(SLUGS_ESPERADOS))
        return 0

    if resultado == src:
        print('snippet ja estava em dia; nada mudou.')
        return 0
    with io.open(alvo, 'w', encoding='utf-8') as fh:
        fh.write(resultado)
    print('gravado: %s' % alvo)
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Confere que TODO endereço publicado existe, em quatro lugares que precisam
concordar entre si:

  1. o slug do front matter de cada arquivo de conteudo/  — a página de verdade;
  2. o slug do item correspondente no manifest.json       — o que o Sync grava;
  3. a constante AQUAMETRIA_C*_SLUG de cada snippet        — o que a calculadora
     anuncia ao hub;
  4. todo link /alguma-coisa/ escrito nos snippets e no conteudo.

Existe por causa do defeito 2 de 08/09/2026: o hub publicava
/calculadora-de-aquecedor/ para a C5, cuja página é
/calculadora-de-potencia-do-aquecedor/, e o clique dava 404. Link que o site
publica e que devolve 404 é defeito, mesmo quando cada arquivo, sozinho, está
certo.

    python3 ferramentas/conferir-slugs.py
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Endereços que existem no site sem vir de conteudo/: a casca os cria sozinha.
DA_CASCA = {'inicio', 'calculadoras', 'metodologia', 'sobre'}

# Endereços externos ao site ou ainda não publicados aparecem aqui com o motivo.
CONHECIDOS_AUSENTES = {}


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as fh:
        return fh.read()


def slugs_do_conteudo():
    achados = {}
    pasta = os.path.join(RAIZ, 'conteudo')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.md') or nome == 'README.md':
            continue
        texto = ler('conteudo/' + nome)
        m = re.search(r'^slug:\s*(\S+)\s*$', texto, re.M)
        if m:
            achados[m.group(1)] = 'conteudo/' + nome
    return achados


def main():
    falhas = []
    conteudo = slugs_do_conteudo()
    manifesto = json.loads(ler('manifest.json'))

    # 1. front matter x manifest
    do_manifest = {}
    for item in manifesto.get('conteudo', []):
        if item.get('slug'):
            do_manifest[item['slug']] = item['arquivo']
    for slug, arquivo in conteudo.items():
        if slug not in do_manifest:
            falhas.append('slug "%s" (%s) não tem item no manifest' % (slug, arquivo))
    for slug, arquivo in do_manifest.items():
        if slug not in conteudo:
            falhas.append('manifest publica o slug "%s" (%s) que nenhum front matter declara' % (slug, arquivo))

    # 2. constantes de slug dos snippets
    pasta = os.path.join(RAIZ, 'snippets')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.php'):
            continue
        texto = ler('snippets/' + nome)
        for const, slug in re.findall(r"define\(\s*'(AQUAMETRIA_C\w*_SLUG)',\s*'([^']+)'\s*\)", texto):
            if slug not in conteudo:
                falhas.append('%s vale "%s" em snippets/%s, e nenhuma página de conteudo/ tem esse slug'
                              % (const, slug, nome))

    # 3. o hub da casca x a constante de cada calculadora
    #
    # A casca traz um slug de partida para as oito calculadoras e a calculadora
    # publicada sobrescreve o seu por filtro. Quando os dois discordam, basta a
    # calculadora não ter carregado para o hub publicar o endereço errado — foi
    # o defeito 2 de 08/09/2026.
    casca = ler('snippets/aquametria-casca.php')
    do_hub = dict(re.findall(
        r"'codigo'\s*=>\s*'(C\d+)',.*?'slug'\s*=>\s*'([a-z0-9-]+)'", casca, re.S))
    constantes = {}
    pasta = os.path.join(RAIZ, 'snippets')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.php'):
            continue
        for const, slug in re.findall(
                r"define\(\s*'AQUAMETRIA_(C\d+)_SLUG',\s*'([^']+)'\s*\)", ler('snippets/' + nome)):
            constantes[const] = slug
    for codigo, slug in constantes.items():
        if codigo in do_hub and do_hub[codigo] != slug:
            falhas.append('a casca publica /%s/ para a %s, cuja página é /%s/'
                          % (do_hub[codigo], codigo, slug))

    # 4. todo link absoluto de raiz escrito em snippet ou conteudo
    conhecidos = set(conteudo) | DA_CASCA | set(CONHECIDOS_AUSENTES)
    for sub in ('snippets', 'conteudo'):
        pasta = os.path.join(RAIZ, sub)
        for nome in sorted(os.listdir(pasta)):
            if nome.startswith('README'):
                continue
            texto = ler(sub + '/' + nome)
            for linha_n, linha in enumerate(texto.splitlines(), 1):
                if linha.lstrip().startswith('*') or linha.lstrip().startswith('//'):
                    continue  # comentário: pode citar o endereço errado de propósito
                # So endereco DESTE site: URL absoluta de aquametria.com.br, href de
                # raiz ou link de Markdown de raiz. O caminho de URL de fabricante
                # e de loja nao e pagina nossa e nao entra na conferencia.
                achados = (re.findall(r'https://aquametria\.com\.br/([a-z0-9][a-z0-9-]{3,})/', linha)
                           + re.findall(r'href="/([a-z0-9][a-z0-9-]{3,})/', linha)
                           + re.findall(r'\]\(/([a-z0-9][a-z0-9-]{3,})/', linha))
                for slug in achados:
                    if slug in conhecidos:
                        continue
                    if slug in ('wp-json', 'wp-content', 'wp-admin', 'feed'):
                        continue
                    falhas.append('%s/%s:%d publica /%s/ e nenhuma página tem esse slug'
                                  % (sub, nome, linha_n, slug))

    for f in sorted(set(falhas)):
        print('  FALHA', f)
    if falhas:
        print('\n%d divergência(s) de endereço.' % len(set(falhas)))
        return 1
    print('  ok    %d slugs de conteudo/, manifest e snippets concordam' % len(conteudo))
    print('  ok    nenhum link publicado aponta para página inexistente')
    return 0


if __name__ == '__main__':
    sys.exit(main())

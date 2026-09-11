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


def titulos_do_conteudo():
    """slug -> titulo declarado no front matter, ja desescapado.

    O `titulo` do manifest e o que o Sync grava em post_title; o front matter e
    o que a pessoa edita. Se os dois divergirem, o site publica o titulo VELHO e
    nenhum teste que renderize do repositorio pode ver — foi o que aconteceu em
    11/09/2026, quando os nove titulos foram reescritos, a bancada ficou verde e
    o ar continuou com os de antes por um desembarque inteiro."""
    achados = {}
    pasta = os.path.join(RAIZ, 'conteudo')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.md') or nome == 'README.md':
            continue
        texto = ler('conteudo/' + nome)
        slug = re.search(r'^slug:\s*(\S+)\s*$', texto, re.M)
        tit = re.search(r'^titulo:\s*"(.*)"\s*$', texto, re.M)
        if not tit:
            tit = re.search(r'^titulo:\s*(.+?)\s*$', texto, re.M)
            valor = tit.group(1) if tit else None
        else:
            valor = tit.group(1).replace('\\"', '"').replace('\\\\', '\\')
        if slug and valor:
            achados[slug.group(1)] = valor
    return achados


def tipos_do_conteudo():
    """slug -> 'pagina' ou 'artigo'.

    Importa porque os dois moram em endereços de formato diferente: página fica
    na raiz (/calculadora-de-litragem/) e artigo é `post`, com o prefixo de data
    da estrutura de permalink (/2026/09/08/quantos-watts-.../). Publicar um
    artigo pelo endereço de página NÃO dá 404 — dá 301, que é pior de achar: a
    página abre, ninguém reclama, e cada visita do robô gasta dois acessos do
    orçamento de rastreamento em vez de um. Foi o item 3 do despacho da Sentinela
    de 10/09/2026, e é para ele não voltar que a conferência abaixo existe.
    """
    tipos = {}
    pasta = os.path.join(RAIZ, 'conteudo')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.md') or nome == 'README.md':
            continue
        texto = ler('conteudo/' + nome)
        slug = re.search(r'^slug:\s*(\S+)\s*$', texto, re.M)
        tipo = re.search(r'^tipo:\s*(\S+)\s*$', texto, re.M)
        if slug:
            tipos[slug.group(1)] = tipo.group(1) if tipo else 'pagina'
    return tipos


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

    # 1b. front matter x manifest, no TITULO
    titulos = titulos_do_conteudo()
    do_manifest_titulo = {}
    for item in manifesto.get('conteudo', []):
        if item.get('slug'):
            do_manifest_titulo[item['slug']] = item.get('titulo')
    for slug, titulo in titulos.items():
        no_manifest = do_manifest_titulo.get(slug)
        if no_manifest is None:
            continue
        if no_manifest != titulo:
            falhas.append(
                'o titulo de "%s" diverge: front matter diz %r e o manifest diz %r. '
                'Quem publica e o manifest — rode ferramentas/atualizar-manifest.py.'
                % (slug, titulo, no_manifest))

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
    #
    # Duas perguntas, não uma: o endereço existe, E ele é o CANÔNICO daquele
    # conteúdo. Um artigo linkado sem o prefixo de data existe e responde — com
    # 301 para a URL com data. Ver tipos_do_conteudo().
    tipos = tipos_do_conteudo()
    artigos = {s for s, t in tipos.items() if t == 'artigo'}
    conhecidos = set(conteudo) | DA_CASCA | set(CONHECIDOS_AUSENTES)
    # O prefixo de data não é escolha do repositório: quem o forma é a data de
    # publicação no WordPress. Por isso a conferência aceita QUALQUER data bem
    # formada e cobra só a presença dela — cravar 2026/09/08 aqui faria este
    # portão reprovar sozinho no dia em que nascesse o quarto artigo.
    com_data = re.compile(r'(?:https://aquametria\.com\.br|href="|\]\()/\d{4}/\d{2}/\d{2}/([a-z0-9][a-z0-9-]{3,})/')
    for sub in ('snippets', 'conteudo'):
        pasta = os.path.join(RAIZ, sub)
        for nome in sorted(os.listdir(pasta)):
            if nome.startswith('README'):
                continue
            texto = ler(sub + '/' + nome)
            for linha_n, linha in enumerate(texto.splitlines(), 1):
                if linha.lstrip().startswith('*') or linha.lstrip().startswith('//'):
                    continue  # comentário: pode citar o endereço errado de propósito

                # 4a. endereço com prefixo de data: só artigo pode usá-lo.
                datados = com_data.findall(linha)
                for slug in datados:
                    if slug in artigos:
                        continue
                    if slug in conhecidos:
                        falhas.append('%s/%s:%d linka a página /%s/ com prefixo de data, '
                                      'e página não tem data no endereço'
                                      % (sub, nome, linha_n, slug))
                    else:
                        falhas.append('%s/%s:%d publica /AAAA/MM/DD/%s/ e nenhum artigo tem esse slug'
                                      % (sub, nome, linha_n, slug))
                # O endereço com data já foi julgado acima, e o casamento de 4b
                # veria o "2026" dele como slug. Ele sai da linha, mas a LINHA
                # continua sendo conferida: uma linha que carrega um link datado
                # e um link cru do mesmo artigo é exatamente o caso que um
                # `continue` aqui deixaria passar.
                linha = com_data.sub('', linha)

                # 4b. So endereco DESTE site: URL absoluta de aquametria.com.br, href de
                # raiz ou link de Markdown de raiz. O caminho de URL de fabricante
                # e de loja nao e pagina nossa e nao entra na conferencia.
                achados = (re.findall(r'https://aquametria\.com\.br/([a-z0-9][a-z0-9-]{3,})/', linha)
                           + re.findall(r'href="/([a-z0-9][a-z0-9-]{3,})/', linha)
                           + re.findall(r'\]\(/([a-z0-9][a-z0-9-]{3,})/', linha))
                for slug in achados:
                    if slug in artigos:
                        falhas.append('%s/%s:%d linka o artigo /%s/ sem o prefixo de data — '
                                      'esse endereço responde 301 para a URL com data'
                                      % (sub, nome, linha_n, slug))
                        continue
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
    print('  ok    %d titulos de conteudo/ e do manifest concordam' % len(titulos))
    print('  ok    nenhum link publicado aponta para página inexistente')
    return 0


if __name__ == '__main__':
    sys.exit(main())

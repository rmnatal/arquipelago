#!/usr/bin/env python3
"""Quebra o portao do no `WebSite` da home DE PROPOSITO, uma quebra por vez.

    python3 ferramentas/mutacoes-site-jsonld.py

O portao nasceu em 23/09/2026 para fechar o item 1 do despacho da Sentinela, e
portao recem-nascido e justamente o que ninguem viu ficar vermelho. A secao 8
do ARQUIPELAGO.md e feita de cicatrizes dessa familia.

AS DUAS MUTACOES QUE MAIS IMPORTAM NESTA LISTA NAO APAGAM NADA — elas consertam
o defeito PELO CAMINHO ERRADO, que e o jeito plausivel de o item 1 ser fechado
por quem le so o titulo dele:

  * a 3 faz a TRILHA deixar de devolver vazio na home. A medicao crua que o
    despacho escreveu ("a home serve ld+json") fica verde na hora — e a ilha
    passa a publicar um breadcrumb de um degrau so na unica pagina que a 16.3
    diz nao ter degrau nenhum.
  * a 4 tira a guarda `is_front_page()` e espalha o no de identidade pelas 48
    URLs. A home continua verde; o que quebra e a afirmacao de que o no e DELA.

E a 8 e a porta dos fundos que nao se ve olhando a tela: o JSON sai, a tag
existe, e o corpo nao parseia. Quem medir por `strpos` ve verde.

Cada mutacao roda num repositorio COPIADO, entao o repositorio de verdade nunca
e tocado.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CASCA = 'snippets/aquametria-casca.php'


def troca(arquivo, velho, novo, vezes=1):
    """Mutacao por substituicao literal. Falha alto se o alvo nao existir mais."""
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit(f'ALVO SUMIU em {arquivo}: {velho[:70]!r}\n'
                             'A mutacao nao pode ser aplicada, entao ela nao prova nada. '
                             'Atualize esta lista junto com o codigo.')
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


def regex(arquivo, padrao, novo):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        s2, n = re.subn(padrao, novo, s, count=1)
        if n == 0:
            raise SystemExit(f'ALVO SUMIU (regex) em {arquivo}: {padrao[:70]!r}')
        p.write_text(s2, encoding='utf-8')
    return aplicar


MUTACOES = [
    (
        'o no some da home (o mundo de antes do conserto volta)',
        regex(CASCA,
              r"\techo '<script type=\"application/ld\+json\" id=\"aquametria-site-jsonld\">'[^;]*;",
              "\treturn;"),
    ),
    (
        'a guarda inverte e o no sai em TODA pagina menos na home',
        troca(CASCA, "\tif ( ! is_front_page() ) {\n\t\treturn;\n\t}",
                     "\tif ( is_front_page() ) {\n\t\treturn;\n\t}"),
    ),
    (
        'o conserto pelo caminho errado: a home ganha um BreadcrumbList de um degrau so',
        troca(CASCA,
              "\t$dados = aquametria_casca_trilha_jsonld( aquametria_casca_slug_atual() );\n"
              "\tif ( ! $dados ) {\n\t\treturn;\n\t}",
              "\t$dados = aquametria_casca_trilha_jsonld( aquametria_casca_slug_atual() );\n"
              "\tif ( ! $dados ) {\n"
              "\t\t$dados = array( '@context' => 'https://schema.org', '@type' => 'BreadcrumbList',\n"
              "\t\t\t'itemListElement' => array( array( '@type' => 'ListItem', 'position' => 1,\n"
              "\t\t\t\t'name' => 'Início', 'item' => home_url( '/' ) ) ) );\n\t}"),
    ),
    (
        'a guarda de is_front_page() some e o no de identidade vira ruido nas 48 URLs',
        troca(CASCA, "\tif ( ! is_front_page() ) {\n\t\treturn;\n\t}\n\techo '<script type=\"application/ld+json\" id=\"aquametria-site-jsonld\">'",
                     "\techo '<script type=\"application/ld+json\" id=\"aquametria-site-jsonld\">'"),
    ),
    (
        'o @type deixa de ser WebSite e vira WebPage',
        troca(CASCA, "\t\t'@type'       => 'WebSite',", "\t\t'@type'       => 'WebPage',"),
    ),
    (
        'a url do no aponta para outra ilha',
        troca(CASCA, "\t\t'url'         => home_url( '/' ),",
                     "\t\t'url'         => 'https://robometria.com.br/',"),
    ),
    (
        'o publisher deixa de ser Organization e vira uma string solta',
        troca(CASCA, "\t\t'publisher'   => $editora,", "\t\t'publisher'   => 'Aquametria',"),
    ),
    (
        'a tag existe e o corpo nao parseia: um JSON cortado no meio',
        troca(CASCA, ". wp_json_encode( aquametria_casca_site_jsonld() ) . \"\\n\" . '</script>'",
                     ". substr( wp_json_encode( aquametria_casca_site_jsonld() ), 0, 40 ) . \"\\n\" . '</script>'"),
    ),
    (
        'o @context some e o no deixa de ser schema.org',
        troca(CASCA, "\t\t'@context'    => 'https://schema.org',\n\t\t'@type'       => 'WebSite',",
                     "\t\t'@type'       => 'WebSite',"),
    ),
    (
        'nasce um potentialAction de busca que a ilha nao serve',
        troca(CASCA, "\t\t'publisher'   => $editora,",
                     "\t\t'publisher'   => $editora,\n\t\t'potentialAction' => array(\n"
                     "\t\t\t'@type'       => 'SearchAction',\n"
                     "\t\t\t'target'      => home_url( '/?s={q}' ),\n"
                     "\t\t\t'query-input' => 'required name=q',\n\t\t),"),
    ),
    (
        'a description vira uma terceira frase, escrita so para o robo ler',
        troca(CASCA, "\t\t'description' => AQUAMETRIA_CASCA_TAGLINE_CURTA,",
                     "\t\t'description' => 'Calculadoras e dados tecnicos para dimensionar o seu aquario',"),
    ),
    (
        'o name do no vira o nome interno do projeto',
        troca(CASCA, "\t\t'@type'       => 'WebSite',\n\t\t'name'        => 'Aquametria',",
                     "\t\t'@type'       => 'WebSite',\n\t\t'name'        => 'Ilha Aquametria do Arquipelago',"),
    ),
    (
        'o inLanguage declara ingles',
        troca(CASCA, "\t\t'inLanguage'  => 'pt-BR',", "\t\t'inLanguage'  => 'en-US',"),
    ),
    (
        'o no passa a depender do contexto e muda de conteudo fora da home',
        troca(CASCA, "\t\t'name'        => 'Aquametria',\n\t\t'url'         => home_url( '/' ),",
                     "\t\t'name'        => is_front_page() ? 'Aquametria' : 'Aquametria (interna)',\n"
                     "\t\t'url'         => home_url( '/' ),"),
    ),
]


def rodar_portao(base: Path):
    r = subprocess.run(['php', str(base / 'ferramentas/teste-site-jsonld.php'), str(base)],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    codigo, saida = rodar_portao(RAIZ)
    if codigo != 0:
        print('O portao ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.')
        print(saida[-2000:])
        return 1
    print('repositorio limpo: portao verde\n')

    reprovou = 0
    for i, (nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            shutil.copytree(RAIZ, base, ignore=shutil.ignore_patterns('node_modules', '.git'))
            aplicar(base)
            codigo, saida = rodar_portao(base)
            falhas = [l.strip() for l in saida.splitlines() if l.strip().startswith('FALHA')]
            if codigo != 0:
                reprovou += 1
                print(f'  {i:2d}. REPROVOU (certo) — {nome}')
                for l in falhas[:3]:
                    print(f'        {l}')
            else:
                print(f'  {i:2d}. PASSOU (ERRADO) — {nome}')
                print('        o portao nao viu este defeito. Ele nao protege contra ele.')

    print(f'\n{reprovou} de {len(MUTACOES)} mutacoes reprovadas pelo portao')
    return 0 if reprovou == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

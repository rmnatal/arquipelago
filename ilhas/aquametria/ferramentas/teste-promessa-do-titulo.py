#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — a PROMESSA NUMERICA do <title>, as tres travas dela, e a
pagina de controle que tem de continuar SEM promessa.

    python3 ferramentas/teste-promessa-do-titulo.py

O QUE E A PROMESSA. Decidido na Proposta 1 e na Proposta 2 da leitura semanal de
07/10/2026: as cinco calculadoras somavam 116 impressoes na banda 4 a 10 com ZERO
clique, e a ficha do betta 125 impressoes com 1 clique na posicao 8,1. O problema
dessas paginas deixou de ser indexacao e passou a ser CTR, e a alavanca que a
secao 12.1 do ARQUIPELAGO.md nomeia para a banda 4 a 10 e "titulo que promete o
numero, meta que promete a faixa e a fonte". Entao os 13 caracteres de
" - Aquametria" cedem o lugar a um numero que sai do banco — o mesmo desenho que
a Robometria estreou em 17/09/2026 e que esta escrito na secao 2c do
snippets/aquametria-seo-tecnico.php.

POR QUE ESTE PORTAO EXISTE, e a frase e da ilha irma: as travas da promessa sao
SILENCIOSAS POR DESENHO. Se o numero nao couber no teto de 65, ou se a funcao do
banco nao responder, o titulo volta a ser nome + marca — que e sempre valido, e
por isso ninguem ve a promessa desaparecer. Trava silenciosa sem quem a conte e
como a promessa some sem ninguem notar.

AS AFIRMACOES, e cada uma existe por um defeito possivel:

  1. as cinco paginas que DECLARARAM promessa servem uma promessa nao vazia;
  2. cada promessa tem digito — promessa sem numero nao e promessa, e e
     exatamente o que uma funcao de banco devolvendo null produz;
  3. nome + separador + promessa cabe em 65 — o teto e o que o Google mostra
     antes de cortar e o mesmo do teste-titulos-das-duas-fontes.py;
  4. nome + " - Aquametria" TAMBEM cabe em 65 — porque esse e o titulo de volta
     quando a trava 3 fecha, e fallback estourado e pior que promessa nenhuma;
  5. TODO numero da promessa aparece, escrito igual, na meta description da
     mesma pagina. E esta a afirmacao que amarra a meta ao banco: o texto da
     meta e escrito a mao (ele e voz, e a voz e da ilha), mas o NUMERO dentro
     dele nao pode divergir do que o snippet resolve do banco;
  6. a /calculadora-de-litragem/ continua SEM promessa. Ela ficou parada de
     proposito na Proposta 2 — "sem nada parado a leitura de 14/10 nao atribui
     nada" —, e uma promessa acidental nela apaga o unico controle da medicao;
  7. nenhuma OUTRA pagina da ilha serve promessa. As direcoes 1 e 7 juntas sao
     o que faz a lista abaixo ser um alarme em vez de um comentario: promessa
     que sai reprova, promessa que entra sem decisao reprova.

O TITULO E LIDO NA FONTE AUTORITATIVA, nao no mapa gerado — front matter para a
pagina de conteudo/, registro do snippet para a pagina do eixo /peixes/ — e
depois comparado com o que o mapa gerado diz. Mapa gerado desatualizado reprova
aqui, e nao no ar.
"""
import importlib.util
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# AS TRES CONSTANTES DO TITULO SAO PERGUNTADAS AO SNIPPET, NAO DIGITADAS AQUI
# (19/10/2026, achado 11 do fecho das 13h27Z desta ilha). Elas moram num lugar
# so — AQUAMETRIA_TITULO_TETO, _SEPARADOR e _MARCA do aquametria-seo-tecnico.php
# — e redigita-las faz este portao ficar VERDE no dia em que o snippet mudar,
# com a promessa caindo do ar em silencio. Quem le e a regua-teto-do-titulo.py.
def carregar_regua_do_teto():
    caminho = os.path.join(RAIZ, 'ferramentas', 'regua-teto-do-titulo.py')
    spec = importlib.util.spec_from_file_location('regua_teto_do_titulo', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_teto = carregar_regua_do_teto()
_c = _teto.perguntar(RAIZ)
TETO = _c['teto']
SEPARADOR = _c['separador']
MARCA = _c['marca']

# AS PAGINAS QUE DECLARARAM PROMESSA, por decisao escrita, e a pagina que ficou
# parada para servir de controle. Lista digitada, e cobrada nas DUAS direcoes
# (afirmacoes 1 e 7): quem tirar uma promessa reprova aqui, e quem puser uma
# promessa nova sem decisao reprova aqui tambem.
COM_PROMESSA = [
    'calculadora-de-vazao-do-filtro',
    'calculadora-de-potencia-do-aquecedor',
    'calculadora-de-midia-filtrante',
    'calculadora-de-iluminacao',
    'quantos-litros-para-betta',
]
CONTROLE = 'calculadora-de-litragem'

contadas = [0]
falhas = []


def ok(nome, cond, extra=''):
    contadas[0] += 1
    print('  %s %s%s' % ('ok   ' if cond else 'FALHA', nome, (' — ' + extra) if extra else ''))
    if not cond:
        falhas.append(nome)


def promessas_do_snippet():
    """{slug: {'titulo':..., 'promessa':...}} perguntado ao proprio snippet."""
    script = os.path.join(RAIZ, 'ferramentas', 'listar-promessas.php')
    if not os.path.exists(script):
        raise SystemExit('FALHA  %s nao existe' % script)
    saida = subprocess.run(['php', script, RAIZ], capture_output=True, text=True)
    if saida.returncode != 0:
        raise SystemExit('FALHA  listar-promessas.php devolveu %d:\n%s'
                         % (saida.returncode, saida.stderr.strip()))
    return json.loads(saida.stdout)


def front_matter(caminho):
    """Os campos de uma linha do front matter. Nao e um parser de YAML."""
    with io.open(caminho, encoding='utf-8') as fh:
        texto = fh.read().lstrip('\ufeff')
    if not texto.startswith('---'):
        return {}
    fim = texto.find('\n---', 3)
    if fim < 0:
        return {}
    campos = {}
    for linha in texto[3:fim].splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', linha)
        if not m:
            continue
        valor = m.group(2).strip()
        if valor.startswith('"') and valor.endswith('"') and len(valor) > 1:
            valor = valor[1:-1].replace('\\"', '"')
        campos[m.group(1)] = valor
    return campos


def fontes_autoritativas():
    """{slug: {'titulo':..., 'descricao':..., 'origem':...}} lido na fonte de cada tipo."""
    fontes = {}

    pasta = os.path.join(RAIZ, 'conteudo')
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith('.md') or nome == 'README.md':
            continue
        campos = front_matter(os.path.join(pasta, nome))
        slug = campos.get('slug', '')
        if slug:
            fontes[slug] = {
                'titulo': campos.get('titulo', ''),
                'descricao': campos.get('meta_descricao', ''),
                'origem': 'conteudo/' + nome,
            }

    caminho = os.path.join(RAIZ, 'dados', 'metas-seo.json')
    with io.open(caminho, encoding='utf-8') as fh:
        dados = json.load(fh)
    for secao in ('paginas_da_casca', 'paginas_do_eixo_peixes'):
        for slug, item in dados.get(secao, {}).items():
            fontes.setdefault(slug, {
                'titulo': item.get('titulo', ''),
                'descricao': item.get('meta_descricao', ''),
                'origem': 'dados/metas-seo.json (%s)' % secao,
            })

    # O titulo da pagina do eixo que vale para o <title> e o do REGISTRO do
    # snippet, que e de onde sai o post_title. Ele sobrescreve o do JSON de
    # proposito: os dois tem de concordar, e quem cobra a concordancia e o
    # teste-titulos-das-duas-fontes.py. Aqui o que importa e o que o site serve.
    for slug, titulo in titulos_do_registro().items():
        if slug in fontes:
            fontes[slug]['titulo'] = titulo
            fontes[slug]['origem'] += ' + registro do eixo'
    return fontes


def titulos_do_registro():
    """{slug: titulo} lido do TEXTO de snippets/aquametria-peixes.php."""
    caminho = os.path.join(RAIZ, 'snippets', 'aquametria-peixes.php')
    with io.open(caminho, encoding='utf-8') as fh:
        src = fh.read()
    corte = src.index('function aquametria_peixes_registro()')
    corpo = src[corte:]
    entradas = [(m.start(), m.group(1))
                for m in re.finditer(r"^\t\t'([a-z0-9\-]+)' => array\(", corpo, re.M)]
    out = {}
    for i, (pos, slug) in enumerate(entradas):
        fim = entradas[i + 1][0] if i + 1 < len(entradas) else len(corpo)
        m = re.search(r"'titulo'\s*=>\s*'((?:[^'\\]|\\.)*)'", corpo[pos:fim])
        if m:
            out[slug] = m.group(1).replace("\\'", "'").replace('\\\\', '\\')
    return out


def numeros(texto):
    """Os numeros como ELES ESTAO ESCRITOS, sem normalizar virgula nem ponto.

    Normalizar aqui seria aceitar "1.76" numa meta cuja promessa diz "1,76" — e
    o que o leitor compara na tela e a grafia, nao o valor.
    """
    return re.findall(r'\d+(?:[.,]\d+)?', texto)


def main():
    print('PROMESSA DO TITULO — bancada, sem rede')
    print('=' * 70)

    do_snippet = promessas_do_snippet()
    fontes = fontes_autoritativas()

    for slug in COM_PROMESSA:
        print('\n%s' % slug)
        if slug not in do_snippet:
            ok('%s: o mapa de SEO conhece a pagina' % slug, False,
               'ausente de aquametria_seo_metas_por_slug()')
            continue
        if slug not in fontes:
            ok('%s: a fonte autoritativa existe' % slug, False, 'nao achei titulo nem descricao')
            continue

        promessa = do_snippet[slug]['promessa']
        titulo = fontes[slug]['titulo']
        descricao = fontes[slug]['descricao']

        ok('%s: serve promessa' % slug, promessa != '', repr(promessa))
        ok('%s: a promessa tem numero' % slug, bool(numeros(promessa)), repr(promessa))
        ok('%s: titulo do mapa gerado = titulo da fonte' % slug,
           do_snippet[slug]['titulo'] == titulo,
           'mapa=%r fonte=%r (%s)' % (do_snippet[slug]['titulo'], titulo, fontes[slug]['origem']))

        com_promessa = titulo + SEPARADOR + promessa
        ok('%s: nome + promessa cabe em %d' % (slug, TETO),
           len(com_promessa) <= TETO, '%d — %s' % (len(com_promessa), com_promessa))

        com_marca = titulo + SEPARADOR + MARCA
        ok('%s: o titulo de volta (nome + marca) cabe em %d' % (slug, TETO),
           len(com_marca) <= TETO, '%d — %s' % (len(com_marca), com_marca))

        faltando = [n for n in numeros(promessa) if n not in descricao]
        ok('%s: todo numero da promessa aparece na meta description' % slug,
           not faltando and descricao != '',
           ('faltam %s na meta' % ', '.join(faltando)) if faltando else '%d numeros' % len(numeros(promessa)))

    print('\ncontrole e as outras paginas')
    ok('%s: continua SEM promessa (controle da medicao de 14/10)' % CONTROLE,
       do_snippet.get(CONTROLE, {}).get('promessa', '') == '',
       repr(do_snippet.get(CONTROLE, {}).get('promessa', '')))

    intrusas = sorted(s for s, d in do_snippet.items()
                      if d['promessa'] != '' and s not in COM_PROMESSA)
    ok('nenhuma outra pagina da ilha serve promessa', not intrusas,
       ', '.join(intrusas) if intrusas else '%d paginas no mapa' % len(do_snippet))

    print('\n' + '=' * 70)
    print('%d afirmacoes, %d falha(s).' % (contadas[0], len(falhas)))
    for f in falhas:
        print('  FALHA  ' + f)
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())

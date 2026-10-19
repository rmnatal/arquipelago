#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: le o `<title>` e a `<meta name="description">` que um
HTML SERVE, e compara o conjunto medido com o DECLARADO na serie — pagina por
pagina, nunca pelo total.

Nao afirma nada sozinha e nao abre rede. Quem afirma e
`conferir-titulo-no-ar.py` (abre o site); quem a exercita contra HTML encenado
e `teste-titulo-no-ar.py` (bancada, sem rede); e quem a mutila e
`mutacoes-titulo-no-ar.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 19/10/2026
--------------------------------------------------
Tres linhas escritas no repositorio antes desta passada, e as tres pedem a
MESMA medicao, que nao existia:

  1. `dados/posicoes.md`, linha de 14/10/2026: *"NAO COPIEI os `<title>`
     servidos para esta serie, e digo por que em vez de deixar em branco (...)
     A leitura de 21/10 e a primeira em que copiar o titulo servido significa
     alguma coisa — e ai e OBRIGATORIO."* Obrigatorio em dois dias, e sem
     instrumento: copiar a mao e a recontagem a mao que esta pasta mediu em
     19/10 um andar abaixo, no cano de links.

  2. O despacho da leitura semanal de 14/10, item 2: o critERIO de pronto da
     Proposta 1 e da Proposta 2 e *"a leitura de 21/10 registrar os dois
     criterios acima COM o `<title>` servido no dia copiado para
     `dados/posicoes.md`"*. A unica alavanca de CTR desta ilha esta puxada e
     a medicao dela depende de um texto copiado de uma aba de navegador.

  3. O cabecalho do `conferir-datas-e-voz-no-ar.py`, que nomeia a cicatriz de
     11/09/2026: *"293 afirmacoes verdes, o Sync dizendo '18 aplicado(s)', e
     os nove titulos no ar continuando os de antes"*. O portao da promessa
     desta ilha — `teste-promessa-do-titulo.py` — e BANCADA, mede o
     repositorio, e por desenho nao ve o ar. As tres travas da promessa sao
     SILENCIOSAS: quando uma fecha, o titulo volta a nome + marca, que e
     sempre valido. **Promessa que nao desembarca nao reprova nada hoje.**

O QUE ELA LE, e cada campo existe por um defeito possivel
---------------------------------------------------------
  * `titulo` — o `<title>` servido, com as entidades DECODIFICADAS. Decodificar
    nao e enfeite: a ronda da Sentinela mede o teto "depois de decodificar as
    entidades" porque `&#8211;` sao 7 caracteres na fonte e 1 na tela, e o teto
    de 65 e da tela.
  * `n` — quantos caracteres tem o titulo decodificado.
  * `descricao` e `descricao_n` — a meta description servida e o tamanho dela.
  * `digito` — se o titulo tem algarismo. E o que separa promessa de nome: a
    promessa desta ilha E um numero, e a pagina de CONTROLE
    (`/calculadora-de-litragem/`) tem de continuar sem nenhum.

O TITULO VIAJA COMO TEXTO E NAO COMO CONTAGEM, e isto e o ponto
---------------------------------------------------------------
A serie da deriva e a do cano declaram FRASES de estado porque o que importa
nelas e o estado. Aqui o que a leitura de 21/10 tem de copiar e o TEXTO do
titulo servido, entao o texto e o dado — e a comparacao item por item e sobre
ele. "40 paginas com titulo" fica verde no dia em que 40 titulos virarem 40
OUTROS titulos: e a licao que a serie da deriva aprendeu em 16/10/2026 e que a
do cano reaprendeu em 19/10.

ELA NAO REESCREVE A MONTAGEM DO TITULO, DE PROPOSITO
----------------------------------------------------
Quem monta `nome + separador + promessa`, com as tres travas e o teto, e o
`aquametria_seo_titulo_do_documento()` do `snippets/aquametria-seo-tecnico.php`,
e quem cobra essa montagem no repositorio e o `teste-promessa-do-titulo.py`.
Esta regua nao tem o separador, nao tem a marca e nao sabe montar titulo
nenhum: ela le o que o ar serve e pergunta se a PROMESSA — a string que o
proprio snippet resolve, perguntada a ele por `listar-promessas.php` — chegou
la dentro. Terceira copia da mesma regra e a cicatriz de 16/10/2026 desta pasta
(*"agora a regua e uma so" era falso no dia em que foi escrito: ela era
QUATRO*).
"""
import html as _html
import io
import json
import os
import re

MARCA_JSON = re.compile(r"^```json\s*$")
RE_TITULO = re.compile(r"<title[^>]*>([\s\S]*?)</title>", re.I)
RE_DESCRICAO = re.compile(
    r"<meta\s+name=[\"']description[\"']\s+content=[\"']([\s\S]*?)[\"']\s*/?>", re.I)
RE_LOC = re.compile(r"<loc>([^<]+)</loc>")


def texto(bruto):
    """Decodifica entidades e normaliza espaco. O teto de 65 e da TELA."""
    return re.sub(r"\s+", " ", _html.unescape(bruto or "")).strip()


def titulo(html):
    """O `<title>` servido, decodificado. String vazia quando nao ha nenhum."""
    achado = RE_TITULO.search(html or "")
    return texto(achado.group(1)) if achado else ""


def descricao(html):
    """A `<meta name="description">` servida, decodificada."""
    achado = RE_DESCRICAO.search(html or "")
    return texto(achado.group(1)) if achado else ""


def locs(xml):
    """As URLs de um sitemap ou do indice dele, sem a quebra de cache."""
    return [u.split("?")[0] for u in RE_LOC.findall(xml or "")]


def slug_da_url(url):
    """O ultimo degrau do caminho — que e o `post_name`, e o `post_name` e o
    slug que o `aquametria_seo_slug_atual()` devolve. A raiz nao tem degrau e
    devolve string vazia: quem precisa do slug da home o descobre casando a
    promessa, nunca digitando `inicio` aqui."""
    caminho = re.sub(r"^https?://[^/]+", "", (url or "").split("?")[0])
    partes = [p for p in caminho.split("/") if p]
    return partes[-1] if partes else ""


def estado(html):
    """O estado servido de UMA pagina. O titulo e o dado, nao a contagem."""
    t = titulo(html)
    d = descricao(html)
    return {
        "titulo": t,
        "n": len(t),
        "descricao": d,
        "descricao_n": len(d),
        "digito": any(c.isdigit() for c in t),
    }


def medir(paginas):
    """{url: estado} a partir de {url: html}. Nao abre rede: recebe o HTML."""
    return dict((url, estado(html)) for url, html in paginas.items())


def promessas(mapa):
    """{slug: promessa} so das paginas que DECLARARAM promessa.

    Recebe o JSON do `listar-promessas.php` como DADO, e nao o chama: e isso
    que deixa o teste encenar uma ilha com outras promessas sem subir PHP.
    Promessa vazia nao entra — ela e o resultado da pagina de controle, e quem
    a cobra e a afirmacao do controle, pela ausencia de digito.
    """
    saida = {}
    for slug, linha in (mapa or {}).items():
        p = (linha or {}).get("promessa") or ""
        if p.strip():
            saida[slug] = p.strip()
    return saida


def promessa_chegou(estado_servido, promessa):
    """A promessa que o snippet resolve esta DENTRO do titulo servido?

    `in` e nao igualdade: a igualdade exigiria montar `nome + separador +
    promessa` aqui, que e a montagem que esta regua se proibe de copiar.
    """
    return promessa in (estado_servido or {}).get("titulo", "")


def sem_promessa(estado_servido):
    """Titulo sem algarismo nenhum — o estado da pagina de CONTROLE."""
    return not (estado_servido or {}).get("digito", False)


def acima_do_teto(medido, teto):
    """As URLs cujo titulo decodificado passa do teto. Lista, nao contagem."""
    return sorted(u for u, e in (medido or {}).items() if e["n"] > teto)


def sem_titulo(medido):
    """As URLs que servem titulo vazio — ou nenhum."""
    return sorted(u for u, e in (medido or {}).items() if not e["titulo"])


def sem_descricao(medido):
    """As URLs que servem meta description vazia — ou nenhuma."""
    return sorted(u for u, e in (medido or {}).items() if not e["descricao"])


def totais(medido):
    """Os totais SAEM dos estados, nunca de uma segunda contagem."""
    itens = medido or {}
    return {
        "paginas": len(itens),
        "com_digito": sum(1 for e in itens.values() if e["digito"]),
        "sem_titulo": sum(1 for e in itens.values() if not e["titulo"]),
        "sem_descricao": sum(1 for e in itens.values() if not e["descricao"]),
        "titulo_mais_longo": max([e["n"] for e in itens.values()] or [0]),
    }


def ler(caminho):
    with io.open(caminho, encoding="utf-8") as fh:
        return fh.read()


def declaracao(caminho):
    """A declaracao mais NOVA da serie: o 1o bloco ```json do arquivo.

    A serie cresce por cima, como `dados/posicoes.md`, `dados/cano-de-links.md`
    e `dados/deriva-do-catalogo.md`. Arquivo ausente devolve None, que o portao
    trata como "titulo nao declarado" — e nunca como zero.
    """
    if not os.path.exists(caminho):
        return None
    dentro, buf = False, []
    for linha in ler(caminho).split("\n"):
        if not dentro and MARCA_JSON.match(linha):
            dentro = True
            continue
        if dentro:
            if linha.strip() == "```":
                break
            buf.append(linha)
    if not buf:
        return None
    return json.loads("\n".join(buf))


def comparar_com_declaracao(medido, declarado):
    """O que o ar serve e a declaracao nao, e o contrario. Pagina por pagina.

    Tres listas, porque as tres falhas pedem conserto diferente: URL NOVA no
    ar sem declaracao, URL que SAIU do ar, e URL cujo titulo ou descricao
    mudou sem ninguem declarar — que e o caso que a leitura de 21/10 nao pode
    descobrir pela aba do navegador.
    """
    if declarado is None:
        return (["a serie nao tem declaracao nenhuma"], [], [])
    esperado = declarado.get("paginas", {})
    novas = sorted(set(medido) - set(esperado))
    sumidas = sorted(set(esperado) - set(medido))
    mudadas = []
    for url in sorted(set(medido) & set(esperado)):
        if medido[url] == esperado[url]:
            continue
        mudadas.append("%s: %s" % (url, quais_campos(medido[url], esperado[url])))
    return (novas, sumidas, mudadas)


def quais_campos(servido, declarado):
    """Nomeia QUAL campo divergiu, e nao so que houve divergencia.

    A primeira escrita desta regua, em 19/10/2026, montava a frase sempre com o
    `titulo` dos dois lados — e o proprio `teste-titulo-no-ar.py` a pegou: na
    metade (E), com o titulo igual e a DESCRICAO trocada, a frase saia dizendo
    *"servido 'Titulo de A' contra declarado 'Titulo de A'"*. Reprovar e uma
    coisa; reprovar dizendo o que mudou e outra, e sem a segunda quem le a falha
    vai procurar defeito no titulo que esta certo. E a mesma licao de 15/10
    desta pasta, um andar acima: *"reprovar nao e a mesma coisa que reprovar
    PELO MOTIVO CERTO"*.
    """
    servido, declarado = servido or {}, declarado or {}
    partes = []
    for campo in ("titulo", "descricao", "n", "descricao_n", "digito"):
        a, b = servido.get(campo), declarado.get(campo)
        if a != b:
            partes.append("%s servido %r contra declarado %r" % (campo, a, b))
    return "; ".join(partes) if partes else "divergiu sem campo nomeado"

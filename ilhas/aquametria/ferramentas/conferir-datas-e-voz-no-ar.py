#!/usr/bin/env python3
"""CONFERE NO AR o que o despacho da Sentinela de 13/09/2026 pediu, nas quatro
frentes dele — e as quatro sao a mesma pergunta vista de lados diferentes: o que
a pagina declara sobre si mesma.

    python3 ferramentas/conferir-datas-e-voz-no-ar.py .

Por que existe ao lado dos portoes de bancada: bancada e imitacao. Esta ilha
pagou o preco de confiar na imitacao em 11/09/2026 — 293 afirmacoes verdes, o
Sync dizendo "18 aplicado(s)", e os nove titulos no ar continuando os de antes.
E, no caso das datas, a bancada NAO PODE medir o criterio de pronto: ele compara
o JSON-LD com o `lastmod` que o `wp-sitemap` declara, e sitemap so existe no ar.

O QUE ELA MEDE, e de onde sai cada regua:

  1. dateModified DO SCHEMA = lastmod DO SITEMAP, url por url. E o criterio de
     pronto do item 1, escrito pela Sentinela. A comparacao e de STRING: as duas
     saem da mesma leitura de `post_modified_gmt` formatada em W3C, entao
     qualquer diferenca — de formato, de fuso, de fonte — e defeito.

  2. AS ONZE FICHAS DECLARAM datePublished, dateModified, author e publisher
     (item 2), com a mesma editora que os tres artigos declaram. A editora e
     comparada entre as duas familias de pagina, nao com um texto digitado aqui:
     "a mesma que os artigos ja declaram" foi o que o despacho pediu.

  3. AS OITO FOTOS DAS QUATRO CALCULADORAS SERVEM width e height iguais aos do
     BANCO (item 3). A regua le `dados/produtos-*.json`, nunca o catalogo
     embutido no snippet — que e a copia que pode divergir.

  4. A ABERTURA DAS ONZE NAO CITA QUEM DECLAROU (item 4), medida no <title>, no
     H1 e no primeiro paragrafo do corpo servido, com a mesma regra de estrutura
     do `teste-voz.mjs`: "conforme" e "segundo" so contam como atribuicao quando
     o que vem depois NOMEIA alguem. A lista esta escrita AQUI, a mao, porque
     quem confere escreve a propria regua.

DUAS ESCOLHAS HERDADAS do `conferir-peixes-no-ar.py`, pelos mesmos motivos: a
lista de URLs vem do SITEMAP no ar, nunca digitada; e toda requisicao leva
`?v=<hora>`, porque o cache duplo da secao 4 do contrato faz a medicao ler o site
de ontem e chamar isso de conferencia.
"""

import glob
import json
import os
import re
import sys
import time
import unicodedata
import urllib.request

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
BASE = "https://aquametria.com.br"

# As quatro paginas que mostram foto de produto, e o mapa esta aqui a mao.
PAGINAS_COM_FOTO = [
    "/calculadora-de-vazao-do-filtro/",
    "/calculadora-de-potencia-do-aquecedor/",
    "/calculadora-de-midia-filtrante/",
    "/calculadora-de-iluminacao/",
]

ATRIBUICAO_SEMPRE = [
    "a fonte declara", "as fontes declaram", "declarado por",
    "declarada por", "declarados por",
]
ATRIBUICAO_SE_NOMEIA = ["conforme", "segundo", "de acordo com"]
ATRIBUIDOS = [
    "a fonte", "as fontes", "o fabricante", "os fabricantes",
    "o compendio", "o manual", "a ficha do", "o boletim",
    "eheim", "seachem", "jbl", "ocean tech", "atman", "chihiros", "ista",
    "sunsun", "sicce", "hopar", "roxin", "soma", "maxxi", "wfish", "aquaverso",
    "reefflow", "casa da ada", "ehow", "fishbase", "seriously fish",
]

falhas = []
contadas = [0]


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def buscar(url):
    sep = "&" if "?" in url else "?"
    pedido = urllib.request.Request(
        url + sep + "v=" + time.strftime("%H%M%S"),
        headers={"User-Agent": "Aquametria/conferir-datas-e-voz-no-ar (Arquipelago)"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn").lower()


def texto(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = re.sub(r"&[a-z]+;|&#\d+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def achar_atribuicao(t):
    plano = sem_acento(t)
    achados = [x for x in ATRIBUICAO_SEMPRE if x in plano]
    for termo in ATRIBUICAO_SE_NOMEIA:
        i = plano.find(termo)
        while i != -1:
            depois = plano[i + len(termo):i + len(termo) + 40]
            nome = next((n for n in ATRIBUIDOS if n in depois), None)
            if nome:
                achados.append("%s + %s" % (termo, nome))
                break
            i = plano.find(termo, i + 1)
    return achados


def nos_jsonld(html):
    achados = []
    for bloco in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
                            html, re.S):
        try:
            d = json.loads(bloco)
        except ValueError:
            achados.append({"@type": "JSON-LD INVALIDO"})
            continue
        if isinstance(d, dict) and "@graph" in d:
            achados.extend(d["@graph"])
        elif isinstance(d, list):
            achados.extend(d)
        else:
            achados.append(d)
    return achados


def lastmods():
    """loc -> lastmod, de todos os sitemaps que o indice do nucleo lista."""
    _, indice = buscar(BASE + "/wp-sitemap.xml")
    mapa = {}
    for sm in re.findall(r"<loc>(.*?)</loc>", indice):
        _, xml = buscar(sm)
        for url in re.findall(r"<url>(.*?)</url>", xml, re.S):
            loc = re.search(r"<loc>(.*?)</loc>", url)
            mod = re.search(r"<lastmod>(.*?)</lastmod>", url)
            if loc:
                mapa[loc.group(1)] = mod.group(1) if mod else None
    return mapa


def banco_por_url():
    por_url = {}
    for arquivo in sorted(glob.glob(os.path.join(RAIZ, "dados", "produtos-*.json"))):
        d = json.load(open(arquivo, encoding="utf-8"))
        for p in d.get("produtos", []):
            img = p.get("imagem")
            if img and img.get("url"):
                por_url.setdefault(img["url"], (p.get("id"),
                                                (img.get("largura"), img.get("altura"))))
    return por_url


def corpo_de(html):
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
    if m:
        return m.group(1)
    # O tema pode nao usar <main>; cair no <body> e melhor do que medir o <head>.
    m = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    return m.group(1) if m else html


def main():
    print("\n== o sitemap no ar ==")
    mapa = lastmods()
    ok("o indice do sitemap lista URLs com lastmod", len(mapa) > 0, "%d URLs" % len(mapa))
    sem_lastmod = [u for u, m in mapa.items() if not m]
    ok("toda URL do sitemap declara lastmod", not sem_lastmod,
       "sem lastmod: %s" % ", ".join(sem_lastmod[:3]))

    artigos = sorted(u for u in mapa if re.search(r"/20\d\d/\d\d/\d\d/", u))
    fichas = sorted(u for u in mapa if "/peixes/" in u and "quantos-litros-para-" in u)
    ok("achei os tres artigos-ancora no sitemap", len(artigos) == 3, str(len(artigos)))
    ok("achei as onze fichas de peixe no sitemap", len(fichas) == 11, str(len(fichas)))

    # ------------------------------------------------------------------
    # 1 e 2. AS DATAS DO SCHEMA
    # ------------------------------------------------------------------
    editoras = {}
    print("\n== item 1: dateModified do schema = lastmod do sitemap ==")
    for url in artigos + fichas:
        status, html = buscar(url)
        ok("%s responde 200" % url.replace(BASE, ""), status == 200, str(status))
        nos = [n for n in nos_jsonld(html) if n.get("@type") == "Article"]
        ok("%s serve exatamente um no Article" % url.replace(BASE, ""), len(nos) == 1,
           "%d nos" % len(nos))
        if len(nos) != 1:
            continue
        no = nos[0]
        editoras[url] = (json.dumps(no.get("author"), sort_keys=True),
                         json.dumps(no.get("publisher"), sort_keys=True))
        ok("%s: dateModified do schema e o lastmod do sitemap" % url.replace(BASE, ""),
           no.get("dateModified") == mapa[url],
           "schema=%r sitemap=%r" % (no.get("dateModified"), mapa[url]))

        if url in fichas:
            for campo in ("datePublished", "dateModified", "author", "publisher"):
                ok("%s: o Article declara %s" % (url.replace(BASE, ""), campo),
                   no.get(campo) not in (None, "", {}), repr(no.get(campo))[:60])

    print("\n== item 2: a editora das fichas e a MESMA dos artigos ==")
    dos_artigos = {editoras[u] for u in artigos if u in editoras}
    ok("os tres artigos declaram uma editora so", len(dos_artigos) == 1, str(dos_artigos))
    for url in fichas:
        if url in editoras:
            ok("%s: author e publisher iguais aos dos artigos" % url.replace(BASE, ""),
               editoras[url] in dos_artigos, str(editoras[url])[:120])

    # ------------------------------------------------------------------
    # 4. A VOZ DA ABERTURA
    # ------------------------------------------------------------------
    print("\n== item 4: a abertura das onze nao cita quem declarou ==")
    for url in fichas:
        _, html = buscar(url)
        corpo = corpo_de(html)
        aba = texto((re.search(r"<title>(.*?)</title>", html, re.S) or [None, ""])[1]
                    if re.search(r"<title>(.*?)</title>", html, re.S) else "")
        h1 = texto((re.search(r"<h1\b[^>]*>(.*?)</h1>", corpo, re.S) or [None, ""])[1]
                   if re.search(r"<h1\b[^>]*>(.*?)</h1>", corpo, re.S) else "")
        p1 = texto((re.search(r"<p\b[^>]*>(.*?)</p>", corpo, re.S) or [None, ""])[1]
                   if re.search(r"<p\b[^>]*>(.*?)</p>", corpo, re.S) else "")
        nome = url.replace(BASE, "")
        for onde, t in (("<title>", aba), ("H1", h1), ("1o paragrafo", p1)):
            achados = achar_atribuicao(t)
            ok("%s %s sem atribuicao" % (nome, onde), not achados,
               "%s em %r" % (", ".join(achados), t[:80]))
        plano = sem_acento(p1)
        ok("%s: a abertura responde com a frente em cm" % nome,
           bool(re.search(r"\d+(,\d+)? cm de frente", plano)), p1[:80])
        com_base = " cm de fundo" in plano and "base" in plano
        sem_base = "fica em aberto" in plano and "comprimento" in plano
        ok("%s: declara a BASE ou o COMPRIMENTO, e exatamente um" % nome,
           com_base != sem_base, "base=%s comprimento=%s" % (com_base, sem_base))

    # ------------------------------------------------------------------
    # 3. AS OITO FOTOS
    # ------------------------------------------------------------------
    print("\n== item 3: as fotos servem width e height do banco ==")
    urls_banco = banco_por_url()
    servidas = 0
    com_par = 0
    for caminho in PAGINAS_COM_FOTO:
        _, html = buscar(BASE + caminho)
        achadas = 0
        for tag in re.findall(r"<img\b[^>]*>", html):
            src = re.search(r'src="([^"]+)"', tag)
            if not src:
                continue
            u = src.group(1).replace("&#038;", "&").replace("&amp;", "&")
            if u not in urls_banco:
                continue
            achadas += 1
            servidas += 1
            pid, (bl, ba) = urls_banco[u]
            l = re.search(r'\bwidth="(\d+)"', tag)
            a = re.search(r'\bheight="(\d+)"', tag)
            tl = int(l.group(1)) if l else None
            ta = int(a.group(1)) if a else None
            if bl is not None and ba is not None:
                com_par += 1
                ok("%s / %s serve %sx%s" % (caminho, pid, bl, ba), (tl, ta) == (bl, ba),
                   "tela=%r banco=%r" % ((tl, ta), (bl, ba)))
            else:
                ok("%s / %s sem medida no banco: nao inventa atributo" % (caminho, pid),
                   (tl, ta) == (None, None), "tela=%r" % ((tl, ta),))
        ok("%s serve foto de produto" % caminho, achadas > 0, "%d fotos" % achadas)

    print("\n%d fotos servidas, %d com o par" % (servidas, com_par))
    ok("toda foto servida no ar carrega o par", servidas == com_par,
       "%d de %d" % (com_par, servidas))

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

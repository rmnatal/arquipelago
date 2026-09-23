#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O no `WebSite` da home, medido NO AR — criterio de pronto do item 1 do
despacho da Sentinela de 23/09/2026, escrito por ele e nao por mim.

    python3 ferramentas/conferir-site-jsonld-no-ar.py

O despacho declarou o criterio com todas as letras, e as DUAS direcoes sao
dele:

    "pronto quando: curl -s -H 'Accept-Encoding: identity'
     'https://aquametria.com.br/?v=<agora>' servir pelo menos um bloco
     <script type="application/ld+json"> que parseie como JSON valido e
     contenha um objeto de @type WebSite com name e url da ilha; e o mesmo
     curl na home CONTINUAR SEM BreadcrumbList, porque a 16.3 nao mudou.
     Medir nas duas direcoes: sem o WebSite reprova, e com BreadcrumbList na
     home tambem reprova."

POR QUE ESTE PORTAO EXISTE SE `teste-site-jsonld.php` JA MEDE A MESMA COISA.
Porque eles nao medem a mesma coisa: aquele mede o REPOSITORIO e este mede o
AR, e a distancia entre os dois e um Sync que pode nao ter desembarcado. E a
secao 4 do ARQUIPELAGO.md inteira — commit sem Sync nao e entrega, e o portao
de bancada fica verde do mesmo jeito enquanto o site serve a casca velha.

A TERCEIRA AFIRMACAO NAO ESTA NO DESPACHO E E MINHA: as outras URLs continuam
SEM o `WebSite`. O no de identidade e da home; se ele aparecer nas 48, a ronda
de amanha mede "toda pagina tem ld+json" e fica verde sobre ruido. Mede-se numa
amostra do sitemap, nao nas 48, porque este portao roda junto de outros cinco e
o custo de 48 requisicoes extras nao compra nada que a amostra nao compre.
"""

import json
import re
import sys
import time
import urllib.request

BASE = "https://aquametria.com.br"
AMOSTRA = 6          # URLs internas medidas na direcao contraria

contadas = [0]
falhas = []


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def buscar(url):
    """A QUEBRA DE CACHE E O `identity` SAO OS DOIS DO DESPACHO, e nenhum dos
    dois e cerimonia: sem o parametro novo, o cache do hospedeiro serve a
    pagina de antes do Sync e o portao aprova o mundo velho."""
    sep = "&" if "?" in url else "?"
    pedido = urllib.request.Request(
        url + sep + "v=" + time.strftime("%H%M%S"),
        headers={"User-Agent": "Aquametria/conferir-site-jsonld-no-ar (Arquipelago)",
                 "Accept-Encoding": "identity"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def nos(html):
    """Os blocos ld+json ja decodificados. Bloco que nao parseia volta como
    None de proposito: a tag presente com corpo quebrado deixa verde qualquer
    medicao que so procure a string `ld+json`, e e o pior dos tres mundos."""
    fora = []
    for corpo in re.findall(
            r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
        try:
            fora.append(json.loads(corpo.strip()))
        except ValueError:
            fora.append(None)
    return fora


def tipos(lista):
    fora = []
    for no in lista:
        if isinstance(no, dict) and no.get("@type"):
            fora.append(no["@type"])
        elif isinstance(no, list):
            for item in no:
                if isinstance(item, dict) and item.get("@type"):
                    fora.append(item["@type"])
    return fora


def urls_do_sitemap():
    _, indice = buscar(BASE + "/wp-sitemap.xml")
    fora = []
    for sm in re.findall(r"<loc>(.*?)</loc>", indice):
        _, xml = buscar(sm)
        fora += re.findall(r"<loc>(.*?)</loc>", xml)
    return sorted(set(fora))


def main():
    print("\n== direcao 1: a home SERVE o no WebSite ==")
    status, home = buscar(BASE + "/")
    ok("a home responde 200", status == 200, str(status))
    ok("a home serve ao menos um bloco ld+json", "application/ld+json" in home)
    ok("a home cita schema.org", "schema.org" in home)

    blocos = nos(home)
    ok("a home tem bloco ld+json extraivel", len(blocos) >= 1, "%d bloco(s)" % len(blocos))
    ok("todo bloco ld+json da home parseia como JSON valido",
       all(b is not None for b in blocos),
       "%d nao parseiam" % len([b for b in blocos if b is None]))

    site = None
    for b in blocos:
        if isinstance(b, dict) and b.get("@type") == "WebSite":
            site = b
    ok("a home tem um objeto de @type WebSite", site is not None,
       "tipos servidos: %s" % ", ".join(tipos(blocos)) or "nenhum")

    if site:
        ok("o WebSite declara name da ilha", site.get("name") == "Aquametria",
           repr(site.get("name")))
        ok("o WebSite declara url da ilha",
           str(site.get("url") or "").rstrip("/") == BASE, repr(site.get("url")))
        ok("o WebSite declara @context schema.org",
           site.get("@context") == "https://schema.org", repr(site.get("@context")))
        editora = site.get("publisher") or {}
        ok("o publisher e uma Organization com nome e url",
           editora.get("@type") == "Organization" and editora.get("name") == "Aquametria"
           and str(editora.get("url") or "").rstrip("/") == BASE, json.dumps(editora))
        ok("o WebSite NAO promete busca que a ilha nao serve",
           "potentialAction" not in site)

    print("\n== direcao 2: a home CONTINUA SEM BreadcrumbList (16.3) ==")
    ok("nenhum no da home e BreadcrumbList",
       "BreadcrumbList" not in tipos(blocos), ", ".join(tipos(blocos)))
    ok("a home nem imprime a tag da trilha",
       "aquametria-trilha-jsonld" not in home)

    print("\n== direcao 3: o no de identidade e da home e de mais ninguem ==")
    urls = [u for u in urls_do_sitemap() if u.rstrip("/") != BASE]
    ok("o sitemap lista URLs internas", len(urls) > 0, "%d URLs" % len(urls))
    amostra = urls[:AMOSTRA]
    com_site, sem_trilha = [], []
    for u in amostra:
        _, html = buscar(u)
        t = tipos(nos(html))
        if "WebSite" in t:
            com_site.append(u)
        if "BreadcrumbList" not in t:
            sem_trilha.append(u)
    ok("nenhuma das %d internas da amostra serve WebSite" % len(amostra),
       not com_site, ", ".join(com_site[:3]))
    # Sem esta, a de cima passaria por vacuidade se as internas parassem de
    # servir JSON-LD nenhum — que e o defeito do item 1 espalhado, nao a cura.
    ok("as %d internas da amostra servem BreadcrumbList" % len(amostra),
       not sem_trilha, "sem trilha: %s" % ", ".join(sem_trilha[:3]))

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

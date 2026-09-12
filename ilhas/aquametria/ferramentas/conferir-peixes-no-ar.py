#!/usr/bin/env python3
"""CONFERE A LEVA 1 DO EIXO /peixes/ NO HTML SERVIDO, nao no repositorio.

    python3 ferramentas/conferir-peixes-no-ar.py .

Por que existe ao lado do `teste-peixes.py`: aquele mede a BANCADA, e bancada e
uma imitacao do site. Esta ilha ja pagou o preco de confiar na imitacao — em
11/09/2026 a bancada deu 293 afirmacoes verdes, o Sync disse "18 aplicado(s)" e
os nove titulos no ar continuaram os de antes, porque a bancada lia o `.md` e o
Sync lia o manifest. A regua aqui e a MESMA (importada do teste, um lugar so para
a aritmetica); o que muda e o sujeito: o que o servidor devolve.

DUAS ESCOLHAS QUE VALEM PARA A PROXIMA LEVA:

  1. A LISTA DE URLS VEM DO SITEMAP NO AR, nunca digitada aqui. Pagina nova entra
     na medicao sozinha, e lista escrita a mao vira, com o tempo, afirmacao sobre
     um site que nao existe mais.

  2. `?v=<hora e minuto>` em toda requisicao, por causa do cache duplo da secao 4
     do contrato: sem isso a medicao pode estar lendo o site de ontem e chamar
     isso de conferencia.

E O QUE ELA MEDE E QUE A BANCADA NAO PODE MEDIR: que a pagina de nivel 2 da
trilha RESOLVE — o degrau intermediario desta ilha nunca foi link, e afirmacao
sobre o caso que nao existe nao mede nada; que nenhuma das cinco e orfa, contando
as ligacoes internas nas 18 paginas servidas (16.4f); e que a tag de medicao
continua no ar depois de a casca mudar de versao.
"""

import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.request

# O nome do arquivo do portao tem hifen, e nome com hifen nao e importavel por
# nome. Carrego pelo caminho, de proposito: a ARITMETICA mora num lugar so. Se
# esta conferencia recomputasse a regua por conta propria, o dia em que uma das
# duas mudasse a outra ficaria verde sobre a conta antiga — e e a mesma armadilha
# de manter documento e codigo a mao em dois lugares. O que este arquivo NAO
# importa e o site: o sujeito da medicao aqui e o HTML que o servidor devolve.
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "teste_peixes", os.path.join(os.path.dirname(os.path.abspath(__file__)), "teste-peixes.py"))
TP = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(TP)

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
SITE = "https://aquametria.com.br"
SITEMAP_INDICE = SITE + "/wp-sitemap.xml"

falhas = []
contadas = [0]


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def buscar(url):
    """GET com quebra-cache e cabecalho honesto."""
    sep = "&" if "?" in url else "?"
    pedido = urllib.request.Request(
        url + sep + "v=" + time.strftime("%H%M%S"),
        headers={"User-Agent": "Aquametria/conferir-peixes-no-ar (Arquipelago)"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main():
    banco = TP.carregar_banco()
    TP.banco_global[0] = banco

    print("CONFERENCIA NO AR — o eixo /peixes/ inteiro\n")

    # O INDICE, e nao um provedor so: as cinco paginas novas moram no provedor de
    # `page` e os tres artigos-ancora no de `post`. Medir um provedor e chamar o
    # numero de "as URLs da ilha" foi o primeiro erro desta conferencia — ela
    # cobrou 18 de um provedor que tem 15, e as outras 3 estavam ao lado.
    status, indice = buscar(SITEMAP_INDICE)
    ok("o indice do sitemap responde 200", status == 200)
    provedores = [u for u in re.findall(r"<loc>([^<]+)</loc>", indice)]
    ok("o indice lista os dois provedores (page e post)", len(provedores) == 2, str(provedores))

    urls = []
    for prov in provedores:
        s2, xml = buscar(prov)
        ok("o provedor %s responde 200" % prov.rsplit("/", 1)[-1], s2 == 200)
        urls += [u.split("?")[0] for u in re.findall(r"<loc>([^<]+)</loc>", xml)]
    # O TOTAL SE CONTA, NUNCA SE DIGITA — e este arquivo tinha o 18 escrito.
    #
    # A leva 2 publicou quatro URLs e a afirmacao reprovou sozinha, o que e o
    # comportamento certo de um alarme; o que estava errado era o alarme dizer a
    # coisa errada ("a ilha publica 18 URLs" e uma afirmacao sobre o passado).
    # O que importa medir e que o sitemap cobre o que a ilha publica: as 13
    # antigas MAIS o eixo inteiro, e nada a menos.
    URLS_ANTES_DO_EIXO = 13
    # secao + uma pagina por categoria + as fichas
    esperado = URLS_ANTES_DO_EIXO + 1 + len(TP.CATEGORIAS) + len(TP.FICHAS)
    ok("o sitemap publica as %d URLs da ilha (13 antigas + o eixo /peixes/)" % esperado,
       len(urls) == esperado, "%d URLs" % len(urls))

    # O CAMINHO DE CADA FICHA SAI DA MAE DELA, e ate a leva 2 saia de "tetras"
    # escrito no meio da linha. Enquanto houve uma categoria so, a URL montada e
    # a URL certa eram a mesma coisa; a leva 3 as separou. Do jeito antigo esta
    # conferencia teria procurado /peixes/tetras/quantos-litros-para-coridora-panda/
    # no sitemap, nao teria achado, e o alarme apontaria para o lugar errado —
    # acusaria o desembarque de nao ter acontecido quando o que estava errado era
    # a regua. E a mesma familia do "18 URLs" digitado que a leva 2 consertou
    # nesta mesma funcao, dois paragrafos acima: numero e caminho, os dois nascem
    # derivados ou os dois envelhecem.
    esperadas = {"peixes": SITE + "/peixes/"}
    for cat in TP.CATEGORIAS:
        esperadas[cat] = SITE + "/peixes/" + cat + "/"
    for slug in TP.FICHAS:
        esperadas[slug] = SITE + "/peixes/" + TP.CATEGORIA_DA_FICHA[slug] + "/" + slug + "/"
    for slug, url in esperadas.items():
        ok("o sitemap lista /%s/" % slug.replace(SITE, ""), url in urls, url)

    servidas = {}
    for slug, url in esperadas.items():
        status, html = buscar(url)
        servidas[slug] = html
        ok("%s responde 200" % slug, status == 200, str(status))
        ok("%s: zero &#038; dentro de <script>" % slug,
           all("&#038;" not in b for b in re.findall(r"<script[^>]*>(.*?)</script>", html, re.S)))
        ok("%s: a tag de medicao continua no ar" % slug,
           "G-8Y26XFZF39" in html)

        # A META DESCRIPTION, MEDIDA NO AR — o defeito que a leva 2 achou.
        #
        # As cinco URLs da leva 1 estavam no ar servindo ZERO description e zero
        # tag og:, enquanto as 13 antigas serviam a delas. A bancada nao podia
        # ver: o que estava errado era a LISTA do gerador, e a lista estava certa
        # para as 13 que ela conhecia. Entao a afirmacao mora aqui, onde o
        # sujeito e o que o servidor devolve, e cobra o texto inteiro e nao a
        # presenca da tag: tag vazia passaria por um `in html`.
        desc = re.search(r'<meta name="description" content="([^"]*)"', html)
        ok("%s: serve meta description de 120 a 160 caracteres" % slug,
           desc is not None and 120 <= len(desc.group(1)) <= 160,
           "%d caracteres" % (len(desc.group(1)) if desc else 0))
        ok("%s: serve og:description" % slug, "og:description" in html)
        ok("%s: o corpo nao comeca por metadado YAML" % slug,
           not TP.texto(TP.corpo(html)).startswith("---"))

    # --- a trilha de quatro degraus, e o degrau do meio RESOLVENDO
    for slug in TP.FICHAS:
        passos = TP.trilha(servidas[slug])
        ok("%s: a trilha servida tem quatro degraus" % slug, len(passos) == 4,
           " › ".join(p[0] for p in passos))
        ok("%s: os tres primeiros degraus da trilha servida sao link" % slug,
           len(passos) == 4 and all(p[1] for p in passos[:3]))

        nos = TP.jsonlds(servidas[slug])
        trilhas = [n for n in nos if n.get("@type") == "BreadcrumbList"]
        ok("%s: serve BreadcrumbList" % slug, len(trilhas) == 1)
        if trilhas:
            itens = trilhas[0]["itemListElement"]
            ok("%s: o BreadcrumbList tem quatro degraus, todos com endereco" % slug,
               len(itens) == 4 and all(i.get("item") for i in itens),
               "%d itens" % len(itens))
            for i in itens[:3]:
                s2, _ = buscar(i["item"])
                ok("%s: o degrau %r do schema responde 200" % (slug, i["name"][:28]), s2 == 200, str(s2))

        tipos = {n.get("@type") for n in nos}
        ok("%s: serve Article e FAQPage" % slug, "Article" in tipos and "FAQPage" in tipos, str(sorted(tipos)))
        ok("%s: NAO serve Product" % slug, "Product" not in tipos)

    # --- a aritmetica, celula por celula, no que o SERVIDOR devolveu
    for slug, ident in TP.FICHAS.items():
        e = banco[ident]
        c = TP.corpo(servidas[slug])
        t = TP.texto(c)
        frente = TP.faixa_do_campo(e, "comprimento_minimo_aquario_cm")
        porte = TP.faixa_do_campo(e, "porte_adulto_cm")
        largura = (e.get("base_minima_cm") or {}).get("largura")

        ok("%s: a resposta servida traz a frente minima de %s cm" % (slug, TP.numero_br(frente[1])),
           ("%s cm de frente" % TP.numero_br(frente[1])) in t)

        tab = TP.tabela_com(c, "pelas duas réguas brasileiras")
        ok("%s: serve a tabela de lotacao" % slug, tab is not None)
        if tab:
            for n, linha in zip(TP.degraus(e), tab["linhas"]):
                soma = n * porte[1]
                esperado = [
                    "%s cm" % TP.numero_br(soma),
                    "%s L" % TP.numero_br(soma * TP.CLASSICA),
                    "%s L" % TP.numero_br(soma * TP.MEIO),
                    "%s L" % TP.numero_br(soma * TP.CONSERVADORA),
                ]
                ok("%s: no ar, %d exemplares dao %s" % (slug, n, " | ".join(esperado)),
                   linha[1:] == esperado, " | ".join(linha[1:]))

        if largura:
            tab = TP.tabela_com(c, "em três alturas de aquário")
            ok("%s: serve a tabela das tres alturas" % slug, tab is not None)
            if tab:
                for a, linha in zip(TP.ALTURAS, tab["linhas"]):
                    v = frente[1] * float(largura) * a / 1000.0
                    esperado = [
                        "%s cm" % TP.numero_br(a),
                        "%s L" % TP.numero_br(v),
                        str(int(math.floor((v / TP.CLASSICA) / porte[1]))),
                        str(int(math.floor((v / TP.MEIO) / porte[1]))),
                        str(int(math.floor((v / TP.CONSERVADORA) / porte[1]))),
                    ]
                    ok("%s: no ar, %d cm de altura da %s" % (slug, a, " | ".join(esperado)),
                       linha == esperado, " | ".join(linha))

        if e.get("comportamento") == "agressivo":
            ok("%s: no ar, especie agressiva sem tabela de companheiro" % slug,
               "Quem divide a mesma faixa de temperatura" not in t)
        ok("%s: no ar, nenhum link de loja" % slug, 'rel="sponsored"' not in servidas[slug])

    # --- NENHUMA DAS CINCO E ORFA: 16.4(f), contado nas 18 paginas servidas.
    #     A casca e o rodape estao em todas, entao o que se conta e a ligacao que
    #     o CORPO de outra pagina faz — e a mae tem de ser uma delas.
    print("\nNENHUMA PAGINA ORFA — ligacoes internas contadas no corpo de cada URL servida")
    corpos = {}
    for url in urls:
        if url in servidas.values():
            for slug, u in esperadas.items():
                if u == url:
                    corpos[url] = servidas[slug]
        else:
            _, html = buscar(url)
            corpos[url] = html

    for slug, url in esperadas.items():
        caminho = url[len(SITE):]
        quantos = 0
        de_onde = []
        for outra, html in corpos.items():
            if outra == url:
                continue
            miolo = TP.corpo(html)
            # o menu e o rodape saem fora: eles estao em todas as paginas e
            # contariam ligacao que nao e editorial
            miolo = re.sub(r'<div class="aqm-nav-caixa">.*?</div>\s*</div>', "", miolo, flags=re.S)
            miolo = re.sub(r'<nav class="aqm-trilha".*?</nav>', "", miolo, flags=re.S)
            if ('href="' + url) in miolo or ('href="' + caminho) in miolo:
                quantos += 1
                de_onde.append(outra[len(SITE):])
        ok("%s: 2 ou mais corpos a citam" % caminho, quantos >= 2, "%d: %s" % (quantos, ", ".join(de_onde)))

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()

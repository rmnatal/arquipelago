#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le as URLs desta ilha COMO O VISITANTE LE — sem quebra de cache.

    python3 ferramentas/leitura-do-visitante.py .
    python3 ferramentas/leitura-do-visitante.py . --autoteste

EXISTE POR UM ACHADO ESCRITO NESTE REPOSITORIO EM 25/09/2026, no BLOCO C do
despacho do Raphael de 24/09, e que ficou quatro dias sem instrumento:

    "conferir-no-ar.py gruda `?v=<agora>` em toda URL — e esta certo, porque
    nasceu para provar que o Sync aplicou a revisao nova. O preco e que ELE
    NUNCA VE O QUE O VISITANTE VE. Cache servindo pagina velha para gente de
    verdade passa por baixo das 504 afirmacoes dele sem encostar em nenhuma."

E o mesmo bloco mediu a outra metade: o rastreador NUNCA RECEBE
REDIRECIONAMENTO, porque o Googlebot nao manda quebra de cache e o cache de
pagina responde 200 antes do WordPress. Em 36 das 71 URLs daquela varredura as
duas leituras discordam. Ou seja: a leitura SEM quebra nao e um detalhe de
conforto — e a unica que se parece com a do Google.

O QUE ISSO CUSTOU A ESTA ILHA, para ninguem achar que e zelo teorico: ela passou
NOVE DIAS com 16 das 17 URLs servindo a pagina de estacionamento da HostGator,
com o `/status` verde e a bancada verde, e ninguem viu. E a causa da decisao de
28/09/2026 no ARQUIPELAGO.md que mandou a ronda tecnica rodar em toda ilha.

O QUE ESTA REGUA REPROVA, e so isto: o visitante NAO receber a ilha. Codigo
diferente de 200, pagina do hospedeiro, pagina sem titulo, casca ausente, e o
404 servido com 200 (o soft 404, que tira pagina do indice sem mudar uma cor na
tela).

O QUE ELA RELATA SEM REPROVAR: titulo ou canonica do visitante diferentes dos da
ORIGEM. Isso e JANELA DE CACHE, e a politica ja estava decidida nesta ilha desde
14/09/2026, escrita no `conferir-no-ar.py`: "fazer o canonico reprovar
transformaria toda entrega em duas horas de portao vermelho que ninguem
consegue fechar — e portao assim se aprende a ignorar, que e pior do que nao ter
portao". Pagina velha no cache continua sendo uma pagina DESTA ilha, com titulo
e com casca; quem cai no ramo de cima e outra coisa.
"""

import importlib.util
import os
import re
import subprocess
import sys
import time

BASE = "https://clubedomosaico.com.br"

# As assinaturas do hospedeiro, escritas literais aqui e nao lidas de lugar
# nenhum: e o texto que ESTA ilha recebeu de 15 a 24/09/2026.
DO_HOSPEDEIRO = ("cgi-sys/defaultwebpage.cgi", "HostGator", "Future home of something quite cool")
# A casca desta ilha no HTML servido. Se ela sumir, o visitante nao esta
# recebendo a ilha, seja la o que ele esteja recebendo.
DA_CASCA = "cdm-marca-logo"
# A classe que o WordPress poe no <body> da pagina de 404 desta ilha.
DO_404 = "error404"

RE_TITULO = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
RE_CANON = re.compile(r"<link[^>]*rel=[\"']canonical[\"'][^>]*href=[\"']([^\"']+)[\"']", re.I)


def titulo_de(html):
    m = RE_TITULO.search(html or "")
    return m.group(1).strip() if m else ""


def canonica_de(html):
    m = RE_CANON.search(html or "")
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# A REGUA, e ela nao toca na rede: e funcao pura das duas leituras, para o
# autoteste poder exercer cada ramo com caso fabricado.
def classificar(codigo, html, titulo_origem="", canonica_origem=""):
    """(veredito, motivo) para uma URL lida SEM quebra de cache.

    veredito: 'defeito' | 'janela' | 'esperado'
    """
    if codigo != "200":
        return ("defeito", "o visitante recebe HTTP %s" % codigo)
    for marca in DO_HOSPEDEIRO:
        if marca in html:
            return ("defeito", "o visitante recebe a pagina do hospedeiro (%s)" % marca)
    if DA_CASCA not in html:
        return ("defeito", "o visitante recebe uma pagina sem a casca desta ilha")
    titulo = titulo_de(html)
    if not titulo:
        return ("defeito", "o visitante recebe pagina sem <title>")
    if DO_404 in html:
        return ("defeito", "o visitante recebe o 404 desta ilha COM codigo 200 (soft 404)")
    if titulo_origem and titulo != titulo_origem:
        return ("janela", "o cache serve titulo anterior: %r contra %r da origem" % (titulo, titulo_origem))
    if canonica_origem and canonica_de(html) != canonica_origem:
        return ("janela", "o cache serve canonica anterior: %r contra %r da origem"
                % (canonica_de(html), canonica_origem))
    return ("esperado", "o visitante recebe a mesma pagina que a origem serve")


# ---------------------------------------------------------------------------
# O AUTOTESTE. Em 29/09/2026 a varredura fechou em 17 esperado e ZERO defeito —
# e a propria ilha ja escreveu, em 25/09, que "passada limpa em portao que nunca
# acusou nada nao prova nada". Cada ramo abaixo e exercido com caso fabricado, e
# nenhum deles chama a rede.
def autoteste():
    BOA = ('<html><head><title>Loja &#8211; Clube do Mosaico</title>'
           '<link rel="canonical" href="https://clubedomosaico.com.br/loja/" />'
           '</head><body class="page"><img class="cdm-marca-logo" /></body></html>')
    casos = [
        ("visitante recebe 500",
         dict(codigo="500", html=BOA), "defeito"),
        ("visitante recebe 404",
         dict(codigo="404", html=BOA), "defeito"),
        ("visitante recebe 000 (nao respondeu)",
         dict(codigo="000", html=""), "defeito"),
        ("visitante recebe a pagina de estacionamento do hospedeiro",
         dict(codigo="200", html='<html><body>Future home of something quite cool</body></html>'), "defeito"),
        ("visitante recebe pagina 200 SEM a casca da ilha",
         dict(codigo="200", html='<html><head><title>x</title></head><body>oi</body></html>'), "defeito"),
        ("visitante recebe pagina com casca e SEM titulo",
         dict(codigo="200", html='<html><head></head><body><img class="cdm-marca-logo" /></body></html>'), "defeito"),
        ("visitante recebe o 404 da ilha com codigo 200 (soft 404)",
         dict(codigo="200",
              html='<html><head><title>Pagina nao encontrada</title></head>'
                   '<body class="error404"><img class="cdm-marca-logo" /></body></html>'), "defeito"),
        ("o cache serve o titulo anterior",
         dict(codigo="200", html=BOA, titulo_origem="Loja nova &#8211; Clube do Mosaico"), "janela"),
        ("o cache serve a canonica anterior",
         dict(codigo="200", html=BOA, titulo_origem="Loja &#8211; Clube do Mosaico",
              canonica_origem="https://clubedomosaico.com.br/loja-nova/"), "janela"),
        ("o caso de hoje: visitante e origem servem a mesma pagina",
         dict(codigo="200", html=BOA, titulo_origem="Loja &#8211; Clube do Mosaico",
              canonica_origem="https://clubedomosaico.com.br/loja/"), "esperado"),
        ("sem leitura de origem para comparar, a pagina sa continua sa",
         dict(codigo="200", html=BOA), "esperado"),
    ]
    falhas = 0
    for rotulo, kw, esperado in casos:
        veredito = classificar(**kw)[0]
        bom = veredito == esperado
        falhas += 0 if bom else 1
        print(("  ok   " if bom else "  FALHA ") + rotulo.ljust(62) + " " + veredito)
    print("\n%s: %d casos de regua, %d falha(s)." %
          ("APROVADO" if not falhas else "REPROVADO", len(casos), falhas))
    return falhas


if "--autoteste" in sys.argv:
    sys.exit(1 if autoteste() else 0)


# ---------------------------------------------------------------------------
# A REDE. Duas leituras por URL: a do VISITANTE (sem nenhum parametro) e a da
# ORIGEM (com quebra de cache), nesta ordem — a do visitante vem primeiro de
# proposito, para a quebra nao aquecer o cache antes de ele ser medido.
def ler(url, quebrar_cache=False):
    if quebrar_cache:
        url = url + ("&" if "?" in url else "?") + "v=" + str(int(time.time()))
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    partes = r.stdout.rsplit("\n", 1)
    return partes[0], (partes[1] if len(partes) > 1 else "000")


def cabecalhos(url):
    r = subprocess.run(["curl", "-s", "-D", "-", "-o", "/dev/null", "--max-time", "40", url],
                       capture_output=True, text=True)
    fora = {}
    for linha in r.stdout.splitlines():
        if ":" in linha:
            chave, _, valor = linha.partition(":")
            fora[chave.strip().lower()] = valor.strip()
    return fora


def urls_do_sitemap():
    """As URLs do sitemap, lidas do sitemap NO AR e nunca digitadas aqui."""
    indice, _ = ler(BASE + "/wp-sitemap.xml", quebrar_cache=True)
    urls = []
    for sub in re.findall(r"<loc>([^<]+)</loc>", indice):
        corpo, _ = ler(sub, quebrar_cache=True)
        urls += re.findall(r"<loc>([^<]+)</loc>", corpo)
    return urls


def varrer():
    urls = urls_do_sitemap()
    print("A LEITURA DO VISITANTE — %d URL(s) do sitemap, SEM quebra de cache\n" % len(urls))
    defeitos, janelas = [], []
    for url in urls:
        html_v, cod_v = ler(url)
        html_o, _cod_o = ler(url, quebrar_cache=True)
        veredito, motivo = classificar(cod_v, html_v, titulo_de(html_o), canonica_de(html_o))
        caminho = url.replace(BASE, "") or "/"
        if veredito == "defeito":
            defeitos.append((caminho, motivo))
            print("  DEFEITO " + caminho.ljust(50) + " " + motivo)
        elif veredito == "janela":
            cab = cabecalhos(url)
            detalhe = "%s | proxy %s | entrada de %s" % (
                motivo, cab.get("x-proxy-cache", "-"), cab.get("last-modified", "-"))
            janelas.append((caminho, detalhe))
            print("  janela  " + caminho.ljust(50) + " " + detalhe)
        else:
            print("  ok      " + caminho.ljust(50) + " " + cod_v)

    # A porta de entrada (secao 29), lida tambem como o visitante le. No
    # `conferir-no-ar.py` o CODIGO destas tres ja e medido sem quebra, mas o
    # CORPO do sitemap so e lido com quebra — e o corpo e o que distingue "o
    # sitemap responde" de "o sitemap responde a pagina do hospedeiro".
    print("\nA porta de entrada, lida sem quebra de cache:")
    sitemap, cod = ler(BASE + "/wp-sitemap.xml")
    sitemap_bom = cod == "200" and ("<sitemap>" in sitemap or "<url>" in sitemap)
    print(("  ok      " if sitemap_bom else "  DEFEITO ")
          + "/wp-sitemap.xml".ljust(50) + " " + cod + " " + sitemap[:40].replace("\n", " "))
    if not sitemap_bom:
        defeitos.append(("/wp-sitemap.xml", "o visitante nao recebe XML de sitemap"))

    # -----------------------------------------------------------------
    # O 404 PELA BORDA, e foi esta sonda que achou o defeito de 29/09/2026.
    #
    # O `conferir-no-ar.py` ja cobra "caminho inexistente responde 404" — mas
    # cobra COM quebra de cache, isto e, da ORIGEM. Pela borda a resposta e
    # outra, e a medicao esta escrita no REGISTRO.md de 29/09:
    #
    #   1a leitura de uma URL inexistente: 404 (a origem, `no-cache, no-store`)
    #   2a leitura em diante:              200, `x-proxy-cache: HIT`,
    #                                      `max-age=7200`, corpo = o 404 da ilha
    #
    # Isso e SOFT 404, e ele e sistematico: basta alguem — ou o Googlebot — ler
    # uma URL morta duas vezes em duas horas. O Google conta pagina assim como
    # existente, e o orcamento de rastreamento desta ilha e o recurso escasso
    # da secao 14.1, com 15 URLs ainda nao indexadas.
    #
    # A URL DA SONDA LEVA UM SUFIXO NOVO A CADA PASSADA, de proposito: ler uma
    # URL fixa mediria a entrada que a passada ANTERIOR criou no cache, e a
    # sonda acusaria a si mesma para sempre. Com sufixo novo, a primeira leitura
    # e sempre virgem e o que se mede e a SEGUNDA.
    print("\nO 404 pela borda (a sonda que achou o defeito de 29/09):")
    sonda = BASE + "/sonda-de-404-%d/" % int(time.time())
    _, primeira = ler(sonda)
    _, segunda = ler(sonda)
    bom = primeira == "404" and segunda == "404"
    print(("  ok      " if bom else "  DEFEITO ") + "caminho inexistente".ljust(50)
          + " 1a leitura %s, 2a leitura %s" % (primeira, segunda))
    if not bom:
        defeitos.append(("sonda de 404",
                         "a borda serve %s na 2a leitura de uma URL que a origem da como %s — soft 404"
                         % (segunda, primeira)))

    print("\n%s: %d URL(s) lidas, %d defeito(s), %d em janela de cache." %
          ("APROVADO" if not defeitos else "REPROVADO", len(urls) + 1, len(defeitos), len(janelas)))
    return len(defeitos)


if __name__ == "__main__":
    sys.exit(1 if varrer() else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONFERE NO AR AS QUATRO PAGINAS DO BLOCO 5d — e as afirmacoes que a de
privacidade faz sobre TODA pagina desta ilha.

    python3 ferramentas/conferir-institucional-no-ar.py

Ele existe porque a pagina de privacidade desta ilha nao promete: ela AFIRMA,
com estas palavras, que este site nao escreve cookie, que nao carrega medidor
de audiencia e que os unicos enderecos de fora que carregam junto com a pagina
sao os dois que ela nomeia. Afirmacao de pagina que nada mede e a familia do
numero de tela digitado — parece conferida.

POR QUE ELE DESCOBRE AS URLs EM VEZ DE AS LISTAR, e isto e a licao da 32.5-b na
frase dela: "regua que nao varre todas certifica a pagina que o autor abriu".
As tres afirmacoes acima sao sobre a ILHA e nao sobre quatro paginas, entao o
portao as cobra em TODA URL do `wp-sitemap.xml` lido no ar. No dia em que
alguem puser um medidor de audiencia numa pagina so, e esta passada que acusa —
e a pagina de privacidade tem de mudar ANTES do codigo, nunca depois.

E A TERCEIRA CONTA (secao 8): os numeros que estas paginas publicam sobre si
mesmas sao RECONTADOS aqui, em Python, direto dos arquivos de dados, por um
caminho diferente do que o PHP usa — e comparados com o que foi ao ar. Duas
metades que contam a mesma coisa ficam verdes quando erram juntas; a terceira
conta e o que separa "o numero bate" de "as duas copias concordam".
"""
import html as html_lib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
DOMINIO = "https://rodametria.com.br"

AS_QUATRO = ("sobre", "contato", "divulgacao-de-afiliados", "privacidade")

# Agulhas de medidor de audiencia e de pixel. A pagina de privacidade afirma a
# AUSENCIA das duas familias, e e isto que torna a afirmacao mensuravel.
MEDIDORES = (
    "googletagmanager.com", "google-analytics.com", "gtag(", "gtag/js",
    "connect.facebook.net", "fbq(", "static.hotjar.com", "clarity.ms",
    "plausible.io", "matomo", "segment.com", "mixpanel",
)

falhas = []
registros = []
afirmacoes = 0


def afirma(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)
    return bool(cond)


def registro(msg):
    registros.append(msg)


def buscar(caminho):
    """Devolve (codigo, cabecalhos, corpo). Quebra de cache sempre: as
    afirmacoes daqui sao sobre a ORIGEM."""
    url = DOMINIO + caminho
    url += ("&" if "?" in caminho else "?") + "v=" + str(int(time.time() * 1000))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.headers, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, {}, "ERRO: %s" % e


def corpo_da_pagina(html):
    """So o CORPO (secao 8): afirmacao sobre o que a pagina DIZ nunca se mede no
    HTML completo, senao ela se acha dentro do proprio JSON-LD."""
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)
    return corpo


def texto_do_corpo(html):
    """O texto que a PESSOA le, com as entidades ja desfeitas.

    O `unescape` nao e detalhe: `esc_html()` do WordPress transforma a aspa reta
    em `&quot;`, e sem desfazer isso a comparacao com o texto declarado REPROVA
    a pagina certa — foi o que a primeira passada desta regua fez, em dois itens
    do bloco de recusa de `/sobre/` que estavam no ar, corretos, escritos com
    aspas. Portao que reprova pagina certa e o caminho mais curto para alguem
    passar a ignora-lo (20.5 e 32.5-b).
    """
    t = re.sub(r"<[^>]+>", " ", corpo_da_pagina(html))
    return re.sub(r"\s+", " ", html_lib.unescape(t)).strip()


def hosts_que_carregam(html):
    """Os enderecos de fora que o navegador busca SEM a pessoa clicar.

    A diferenca entre CARREGAR e LINKAR e a afirmacao inteira da pagina de
    privacidade: `src` e `<link rel=stylesheet|preconnect|preload>` fazem o
    navegador falar com o outro lado; `href` de `<a>` nao faz nada ate o
    clique. Juntar os dois chamaria de rastreador o link de uma fonte citada.
    """
    hosts = set()
    for m in re.finditer(r'\b(?:src|srcset)="(https?://[^"]+)"', html):
        hosts.add(m.group(1).split("/")[2])
    for m in re.finditer(r"<link[^>]*>", html, re.I):
        tag = m.group(0)
        if not re.search(r'rel="(stylesheet|preconnect|preload|modulepreload)"', tag, re.I):
            continue
        u = re.search(r'href="(https?://[^"]+)"', tag)
        if u:
            hosts.add(u.group(1).split("/")[2])
    return {h for h in hosts if not h.endswith("rodametria.com.br")}


# ---------------------------------------------------------------------------
# A TERCEIRA CONTA — recontada em Python, dos arquivos, por outro caminho
# ---------------------------------------------------------------------------

def recontar(urls_do_sitemap=None):
    """Os numeros que estas paginas publicam sobre si mesmas.

    Deliberadamente escrito SEM olhar o PHP: a conta sai dos mesmos arquivos de
    dado, por iteracao propria. Se as duas discordarem, a discordancia e a
    informacao — e e por isso que ela e uma DECISAO e se escreve duas vezes
    (secao 8, a fronteira entre decisao e fato externo).
    """
    f2 = json.load(open(os.path.join(ILHA, "dados", "f2-respostas.json"), encoding="utf-8"))
    vit = json.load(open(os.path.join(ILHA, "dados", "vitrine-de-produto.json"), encoding="utf-8"))

    compra = f2["compra"]
    veiculos_total = int(compra["total_registros_veiculos"])

    def tem_saida(i):
        return bool(i.get("url_afiliado_da_ficha")) or bool(i.get("url_busca"))

    veiculos_link = len([i for i in compra.get("vitrine", []) if tem_saida(i)])
    pecas_link = len([i for i in compra.get("pecas_publicaveis", []) if tem_saida(i)])

    com_saida = [i for i in list(compra.get("vitrine", [])) + list(compra.get("pecas_publicaveis", []))
                 if tem_saida(i)]
    com_ficha = len([i for i in com_saida if 1 <= int(i.get("degrau") or 0) <= 3])
    com_busca = len(com_saida) - com_ficha

    lidas = recusadas = publicados = 0
    for p in vit.get("paginas", []):
        n = p.get("numeros") or {}
        lidas += int(n.get("lidas") or 0)
        recusadas += int(n.get("recusadas") or 0)
        publicados += int(n.get("n") or 0)

    contas = {
        "VEICULOS_NO_BANCO": veiculos_total,
        "VEICULOS_COM_LINK": veiculos_link,
        "VEICULOS_SEM_LINK": max(0, veiculos_total - veiculos_link),
        "PECAS_COM_LINK": pecas_link,
        "ITENS_COM_LINK": veiculos_link + pecas_link,
        "ITENS_COM_FICHA": com_ficha,
        "ITENS_COM_BUSCA": com_busca,
        "ANUNCIOS_LIDOS": lidas,
        "ANUNCIOS_RECUSADOS": recusadas,
        "ANUNCIOS_PUBLICADOS": publicados,
        "PAGINAS_DE_PRODUTO": len(vit.get("paginas", [])),
    }

    # PAGINAS NO AR, POR UM CAMINHO QUE NAO E O DO PHP. O PHP conta o MAPA de
    # paginas da casca (entrada com URL nao vazia); aqui a conta sai do
    # `wp-sitemap.xml` servido. Quando as duas divergirem, a divergencia e
    # INFORMACAO e nao ruido: URL no sitemap que o mapa nao conhece e pagina
    # orfa da arvore da 16, e pagina no mapa que o sitemap nao lista nao esta
    # indexavel. E por isso que esta conta mora aqui e nao e lida do PHP.
    if urls_do_sitemap is not None:
        contas["PAGINAS_NO_AR"] = len(urls_do_sitemap)

    return contas


def main():
    declarado = json.load(open(os.path.join(ILHA, "dados", "paginas-institucionais.json"),
                               encoding="utf-8"))
    terceiros_declarados = set()
    for t in declarado.get("terceiros_que_carregam", []):
        for campo in ("endereco", "endereco_irmao"):
            if t.get(campo):
                terceiros_declarados.add(t[campo])
    registro("terceiros declarados na pagina: %s" % ", ".join(sorted(terceiros_declarados)))

    # -------------------------------------------------------------------
    # 1. AS URLs, DESCOBERTAS NO SITEMAP — nunca listadas aqui
    # -------------------------------------------------------------------
    cod, _, mapa = buscar("/wp-sitemap.xml")
    if not afirma(cod == 200, "wp-sitemap.xml respondeu %s" % cod):
        return encerrar()

    todas = []
    for sub in re.findall(r"<loc>([^<]+)</loc>", mapa):
        if sub.endswith(".xml"):
            c2, _, filho = buscar(sub.replace(DOMINIO, ""))
            if c2 == 200:
                todas += [u for u in re.findall(r"<loc>([^<]+)</loc>", filho)]
        else:
            todas.append(sub)
    todas = sorted(set(todas))
    afirma(len(todas) >= 1, "o sitemap nao publica nenhuma URL")
    registro("sitemap: %d URL(s)" % len(todas))

    caminhos = [u.replace(DOMINIO, "") or "/" for u in todas]

    # As quatro ESTAO no sitemap? Esta e a unica afirmacao do portao que nomeia
    # as paginas — e ela e sobre o bloco 5d ter acontecido, nao sobre conteudo.
    for slug in AS_QUATRO:
        afirma("/%s/" % slug in caminhos,
               "/%s/ nao esta no sitemap — a 16.1 nomeia esta pagina e a ilha serve "
               "link de afiliado" % slug)

    # -------------------------------------------------------------------
    # 2. AS TRES AFIRMACOES DA PRIVACIDADE, COBRADAS EM TODA URL
    # -------------------------------------------------------------------
    for caminho in caminhos:
        cod, cab, html = buscar(caminho)
        if not afirma(cod == 200, "%s respondeu %s" % (caminho, cod)):
            continue

        # (a) nenhum cookie — e o cabecalho e quem decide, nao o nosso codigo
        cookies = []
        try:
            cookies = cab.get_all("Set-Cookie") or []
        except AttributeError:
            c = cab.get("Set-Cookie") if hasattr(cab, "get") else None
            cookies = [c] if c else []
        afirma(not cookies,
               "%s devolveu Set-Cookie (%s) e a pagina de privacidade afirma que este site "
               "nao escreve cookie nenhum — a pagina tem de mudar ANTES do codigo"
               % (caminho, "; ".join(x[:60] for x in cookies)))

        # (b) nenhum medidor de audiencia, nenhum pixel
        for agulha in MEDIDORES:
            afirma(agulha not in html,
                   "%s carrega %r e a pagina de privacidade afirma que nao ha medidor de "
                   "audiencia nem pixel — a pagina tem de mudar ANTES do codigo"
                   % (caminho, agulha))

        # (c) os enderecos de fora que CARREGAM sao os declarados, e so eles
        fora = hosts_que_carregam(html)
        nao_declarados = sorted(fora - terceiros_declarados)
        afirma(not nao_declarados,
               "%s carrega de fora %s, que a pagina de privacidade nao nomeia — ela diz "
               "quais sao, e endereco novo a torna falsa" % (caminho, nao_declarados))
        if fora:
            registro("%s carrega de fora: %s" % (caminho, ", ".join(sorted(fora))))

    # -------------------------------------------------------------------
    # 3. AS QUATRO PAGINAS, UMA POR UMA
    # -------------------------------------------------------------------
    contas = recontar(caminhos)
    registro("terceira conta: " + ", ".join("%s=%s" % (k, v) for k, v in sorted(contas.items())))

    por_slug = {p["slug"]: p for p in declarado["paginas"]}

    for slug in AS_QUATRO:
        caminho = "/%s/" % slug
        if caminho not in caminhos:
            continue
        cod, _, html = buscar(caminho)
        if not afirma(cod == 200, "%s respondeu %s" % (caminho, cod)):
            continue
        corpo = corpo_da_pagina(html)
        texto = texto_do_corpo(html)
        pg = por_slug[slug]

        # O piso de corpo da secao 8, MEDIDO NO AR — e nao pela conta de antes
        # do desembarque, que e o erro que a mae /veiculos/ quase pagou (daria
        # 1.253 e a pagina no ar passou).
        afirma(len(texto) >= 1500,
               "%s: o corpo tem %d caracteres e o piso e 1.500" % (caminho, len(texto)))
        registro("%s: %d caracteres de corpo no ar" % (caminho, len(texto)))

        # ZERO molde cru na tela. Molde que escapa e a prosa falando em codigo.
        crus = re.findall(r"\{[A-Z_]{3,}\}", corpo)
        afirma(not crus, "%s: molde cru na tela: %s" % (caminho, sorted(set(crus))))

        # O H1 e o declarado, e ha um so (a casca cobra o resto).
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
        afirma(len(h1) == 1, "%s: tem %d <h1>" % (caminho, len(h1)))
        if h1:
            afirma(pg["h1"] in re.sub(r"<[^>]+>", "", h1[0]),
                   "%s: o <h1> no ar nao e o declarado" % caminho)

        # O BLOCO DE RECUSA existe na tela e esta MARCADO — e e a marcacao que
        # faz a regua de escassez poder retirar o bloco em vez de adivinhar
        # pela vizinhanca das palavras (secao 8, cicatriz de 11/09/2026).
        afirma("rdm-inst-recusa" in corpo,
               "%s: o bloco de recusa nao esta marcado no markup" % caminho)
        for item in pg["recusa"]["itens"]:
            afirma(item.split(":")[0][:40] in texto,
                   "%s: um item do bloco de recusa nao esta no ar: %r"
                   % (caminho, item[:50]))

        # SEM bloco de compra: a 32.2 so o manda onde ha o que comprar, e aqui
        # nao ha. Bloco de compra numa pagina de privacidade seria obsceno.
        afirma("rdm-molde-compra" not in corpo,
               "%s: tem bloco de compra, e esta familia de pagina nasce sem ele" % caminho)
        afirma("s.shopee.com.br" not in corpo,
               "%s: tem link de loja no corpo, e esta familia de pagina nao vende nada"
               % caminho)

        # A MALHA da 16.4: a pagina linka as irmas pelo nome delas.
        for alvo in pg.get("veja_tambem", []):
            afirma(("/%s/" % alvo) in html,
                   "%s: nao linka /%s/, que o declarado manda" % (caminho, alvo))

        # A TERCEIRA CONTA contra o que foi ao ar: o numero da caixa.
        molde = re.fullmatch(r"\{([A-Z_]+)\}", pg["caixa"]["numero"].strip())
        if molde and molde.group(1) in contas:
            chave = molde.group(1)
            esperado = str(contas[chave])
            caixa = re.search(r'class="rdm-molde-caixa-numero"[^>]*>\s*<span class="rdm-num">'
                              r'([^<]+)</span>', corpo)
            if afirma(bool(caixa), "%s: nao achei o numero da caixa no ar" % caminho):
                afirma(caixa.group(1).strip() == esperado,
                       "%s: a caixa serve %r e a conta independente de %s da %r"
                       % (caminho, caixa.group(1).strip(), chave, esperado))
                registro("%s: caixa %s = %s, e a terceira conta concorda"
                         % (caminho, chave, esperado))

    # -------------------------------------------------------------------
    # 4. O QUE ESTE PORTAO NAO MEDIU, dito em vez de aprovado em silencio
    # -------------------------------------------------------------------
    registro("NAO MEDIDO AQUI: pixel. A 32.5 pede 390 px num navegador de verdade, e quem "
             "faz isso e conferir-32-5-no-navegador.mjs.")
    registro("NAO MEDIDO AQUI: a borda do hospedeiro. Quem le sem quebra de cache e outro "
             "portao; as afirmacoes daqui sao sobre a ORIGEM.")

    return encerrar()


def encerrar():
    for r in registros:
        print("  . %s" % r)
    print("")
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d afirmacao(oes), %d falha(s)." % (afirmacoes, len(falhas)))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

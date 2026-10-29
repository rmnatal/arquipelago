#!/usr/bin/env python3
"""
CONFERE A ILHA NO AR — o portao que a secao 8 do ARQUIPELAGO.md exige por escrito.

    "Depois de publicar, busque a URL no ar e confira com numero medido:
     (1) HTTP 200; (2) zero entidades &#038; DENTRO de <script>; (3) o corpo
     comeca pelo texto e nao por metadado; (4) o script vem do rodape e a tabela
     de exemplos aparece no HTML servido; (5) a revisao aplicada bate com a do
     manifest."

Mais o que as outras secoes cobram e que esta ilha tinha de herdar pronto:
  - a PORTA DE ENTRADA da 29.2 (robots.txt em text/plain, wp-sitemap.xml em
    application/xml, wp-json em application/json, e caminho virgem em 404);
  - o PORTAO DO DESEMBARQUE da 20.4: o log do /status e lido LINHA POR LINHA e
    nenhuma linha da revisao corrente pode deixar de dizer `ok`. Resumo verde
    nao e entrega;
  - a 20.5: revisao atrasada com log de AGORA e cache do GitHub, nao defeito —
    e o portao diz qual dos dois e, em vez de reprovar os dois igual;
  - a 32.4: zero palavra de bastidor da fabrica no texto servido;
  - a 32.5 pede medicao a 390 px num navegador de verdade, e ISSO NAO E AQUI:
    quem faz e `conferir-32-5-no-navegador.mjs` (a copiar do modelo da
    clubedomosaico quando esta ilha tiver molde em mais de uma pagina). Este
    portao mede o que se mede no HTML servido, e DIZ que nao mediu pixel —
    aprovar em silencio o que nao se mediu e o defeito que a 32.5-b nomeou.

TODA URL E PEDIDA COM QUEBRA DE CACHE: as afirmacoes aqui sao sobre a ORIGEM.
Quem le como o Google le, sem quebra de cache, e outro portao.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
DOMINIO = "https://rodametria.com.br"

falhas = []
registros = []
afirmacoes = 0


def afirma(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)


def registro(msg):
    registros.append(msg)


def buscar(caminho, v=True):
    url = DOMINIO + caminho
    if v:
        url += ("&" if "?" in caminho else "?") + "v=" + str(int(__import__("time").time()))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", ""), e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, "", "ERRO: %s" % e


def corpo_da_pagina(html):
    """So o CORPO, nunca o HTML completo.

    A secao 8: "afirmacao sobre o que a pagina diz se mede no CORPO, nunca no
    HTML completo" — a trava que achava o texto dentro do proprio JSON-LD e
    passava ate com resposta inventada.
    """
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)

    return corpo


def main():
    manifest = json.load(open(os.path.join(ILHA, "manifest.json"), encoding="utf-8"))
    revisao_esperada = int(manifest["revisao"])

    # -------------------------------------------------------------------
    # 1. A PORTA DE ENTRADA (29.2). Ela cai sozinha, sem nenhum portao
    #    acusar, e foi assim que o Clube do Mosaico passou nove dias fora.
    # -------------------------------------------------------------------
    porta = (
        ("/robots.txt", "text/plain"),
        ("/wp-sitemap.xml", "xml"),
        ("/wp-json/", "application/json"),
    )
    for caminho, tipo in porta:
        cod, ct, _ = buscar(caminho)
        afirma(cod == 200, "29.2: %s respondeu %s, nao 200" % (caminho, cod))
        afirma(tipo in ct, "29.2: %s veio como %r e tinha de ser %r" % (caminho, ct, tipo))

    virgem = "/caminho-que-nunca-existiu-%d/" % int(__import__("time").time())
    cod, _, _ = buscar(virgem, v=False)
    afirma(cod == 404, "29.2: caminho virgem respondeu %s e tinha de ser 404" % cod)

    # -------------------------------------------------------------------
    # 2. O /status E O PORTAO DO DESEMBARQUE (20.4 e 20.5)
    # -------------------------------------------------------------------
    cod, _, bruto = buscar("/wp-json/rodametria/v1/status")
    afirma(cod == 200, "/status respondeu %s" % cod)
    if cod != 200:
        return encerrar()

    st = json.loads(bruto)
    revisao_no_ar = int(st.get("revisao", -1))
    log = st.get("log", [])
    ultimo = str(st.get("ultimo", ""))

    if revisao_no_ar < revisao_esperada:
        # 20.5: cache do GitHub, ou Sync que nao rodou? Quem decide e o log.
        afirma(False,
               "o manifest esta na revisao %d e o /status esta na %d. O ultimo log e de %s — "
               "pela 20.5, log recente aqui significa CACHE do GitHub (reacione de dois em dois) "
               "e log antigo significa que o Sync NAO RODOU."
               % (revisao_esperada, revisao_no_ar, ultimo))
        return encerrar()

    afirma(revisao_no_ar == revisao_esperada,
           "o /status esta na revisao %d e o manifest na %d" % (revisao_no_ar, revisao_esperada))

    # O LOG LINHA POR LINHA, E SO AS LINHAS DA REVISAO CORRENTE.
    #
    # A 20.4 e literal: "a execucao le as linhas da REVISAO CORRENTE no log do
    # /status, e nenhuma pode deixar de dizer `ok`". A primeira versao desta
    # regua lia a JANELA INTEIRA e reprovou a entrega de 29/10 por causa de
    # quatro linhas `FALHA manifest: HTTP 404` de 28/10 — de antes de o
    # manifest.json existir no repositorio, ou seja a historia de um defeito ja
    # consertado. Regua que reprova entrega certa e o caminho mais curto para
    # alguem passar a ignora-la (20.5), e a janela do log e append-only: ela
    # SEMPRE vai carregar o passado.
    #
    # O corte: o log vem do mais novo para o mais velho, e cada revisao comeca
    # com a linha "revisao N:". As linhas desta entrega sao as que vao do topo
    # ate essa linha, inclusive.
    linhas_da_revisao = []
    for l in log:
        linhas_da_revisao.append(l)
        if re.search(r"revis\w*\s+%d\s*:" % revisao_no_ar, l):
            break
    afirma(any(re.search(r"revis\w*\s+%d\s*:" % revisao_no_ar, l) for l in linhas_da_revisao),
           "20.4: o log do /status nao tem a linha de fecho da revisao %d — a janela pode "
           "ter rolado, e entrega sem linha de fecho nao foi conferida" % revisao_no_ar)
    falhas_no_log = [l for l in linhas_da_revisao
                     if "FALHA" in l or "NÃO" in l or "NAO" in l or "erro" in l.lower()]
    afirma(not falhas_no_log,
           "20.4: o log do /status tem linha da revisao %d que nao diz ok: %s"
           % (revisao_no_ar, falhas_no_log))
    antigas = [l for l in log if l not in linhas_da_revisao
               and ("FALHA" in l or "erro" in l.lower())]
    if antigas:
        registro("20.4: a janela do log carrega %d linha(s) de FALHA de revisoes "
                 "ANTERIORES, e elas nao sao desta entrega: %s"
                 % (len(antigas), antigas[:2]))
    registro("20.4: log lido linha por linha — %d linha(s) na janela, %d da revisao %d, "
             "0 linha de falha nesta entrega"
             % (len(log), len(linhas_da_revisao), revisao_no_ar))
    if len(log) >= 15:
        registro("20.4: a janela do log tem %d linhas e esta CHEIA — item que rolou para fora "
                 "dela NAO foi conferido. Registro, nao aprovacao." % len(log))

    # -------------------------------------------------------------------
    # 3. A CASCA INSTALOU AS PAGINAS QUE DIZ TER INSTALADO
    # -------------------------------------------------------------------
    cod, _, bruto = buscar("/wp-json/rodametria/v1/casca")
    afirma(cod == 200, "/casca respondeu %s — a casca nao esta ativa no ar" % cod)
    urls = {}
    if cod == 200:
        c = json.loads(bruto)
        registro("casca %s instalada em %s"
                 % (c.get("versao_casca"), (c.get("instalado") or {}).get("em")))
        for linha in ((c.get("instalado") or {}).get("relato") or []):
            afirma("ERRO" not in linha and "ATENCAO" not in linha,
                   "a instalacao da casca relatou: %s" % linha)
            registro("instalacao: %s" % linha)
        for slug, p in (c.get("paginas") or {}).items():
            afirma(bool(p.get("url")),
                   "a pagina %r esta no mapa da casca e nao tem URL no ar — link interno "
                   "para 404 e o defeito de 08/09/2026" % slug)
            if p.get("url"):
                urls[slug] = p["url"]

    # -------------------------------------------------------------------
    # 4. O SITEMAP, E TODA URL DELE EM 200
    # -------------------------------------------------------------------
    cod, _, mapa = buscar("/wp-sitemap.xml")
    sub = re.findall(r"<loc>([^<]+)</loc>", mapa)
    todas = []
    for s in sub:
        c2, _, x = buscar(s.replace(DOMINIO, ""), v=True)
        afirma(c2 == 200, "sub-sitemap %s respondeu %s" % (s, c2))
        todas.extend(re.findall(r"<loc>([^<]+)</loc>", x))
    todas = sorted(set(todas))
    registro("sitemap: %d URL(s) publicada(s)" % len(todas))
    afirma(len(todas) >= 1, "o sitemap nao publica nenhuma URL")

    # O SITEMAP E CURADORIA, NAO INVENTARIO (14.1). Medido em 29/10/2026: quatro
    # das seis URLs eram lixo de fabrica do WordPress, num dominio de dois dias.
    lixo = ("hello-world", "sample-page", "/author/", "/category/", "ola-mundo",
            "pagina-exemplo", "/tag/", "?p=")
    for u in todas:
        for termo in lixo:
            afirma(termo not in u,
                   "14.1: o sitemap publica %s, que e URL fraca de dominio novo — sitemap e "
                   "curadoria, nao inventario" % u)
    for s in sub:
        afirma("users" not in s and "taxonomies" not in s,
               "14.1: o sitemap ainda tem o sub-sitemap %s — arquivo de autor e de "
               "categoria nao e pagina de verdade nesta ilha" % s)

    # -------------------------------------------------------------------
    # 5. CADA PAGINA, UMA POR UMA
    # -------------------------------------------------------------------
    bastidor = ["egresso", "SERP classificada", "snippet", "wp-sitemap", "manifest.json",
                "ARQUIPELAGO", "Rodametria Sync", "bancada", "dados/", "ferramentas/",
                "regras/", "publicavel", "sha256", "revisao"]

    for u in todas:
        caminho = u.replace(DOMINIO, "")
        cod, ct, html = buscar(caminho)
        afirma(cod == 200, "%s respondeu %s" % (caminho, cod))
        if cod != 200:
            continue

        # (2) zero &#038; DENTRO de <script> — contado SO nos blocos script.
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.S | re.I)
        dentro = sum(s.count("&#038;") for s in scripts)
        afirma(dentro == 0,
               "%s: ha %d entidade(s) &#038; dentro de <script> — e o defeito que derrubou "
               "cinco calculadoras da Aquametria" % (caminho, dentro))

        corpo = corpo_da_pagina(html)
        texto = re.sub(r"<[^>]+>", " ", corpo)
        texto = re.sub(r"\s+", " ", texto).strip()

        # (3) o corpo comeca pelo texto, e nao por metadado YAML.
        afirma(not texto.startswith("---"),
               "%s: o corpo comeca por metadado e nao por texto" % caminho)

        # Pagina fina nao entra no indice de dominio novo (secao 8).
        afirma(len(texto) >= 1500,
               "%s: o corpo tem %d caracteres e o piso e 1.500 — pagina fina gasta orcamento "
               "de rastreamento de dominio novo" % (caminho, len(texto)))
        registro("%s: %d caracteres de corpo" % (caminho, len(texto)))

        # <title>, H1, description e JSON-LD (32.3: nenhum deles muda com o molde).
        afirma(bool(re.search(r"<title>[^<]{10,}</title>", html)),
               "%s: sem <title>" % caminho)
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
        afirma(len(h1) == 1, "%s: tem %d <h1> e tinha de ter 1" % (caminho, len(h1)))
        desc = re.search(r'<meta name="description" content="([^"]{20,})"', html)
        afirma(bool(desc), "%s: sem meta description" % caminho)
        if desc:
            afirma(len(desc.group(1)) <= 200,
                   "%s: description com %d caracteres" % (caminho, len(desc.group(1))))
        jsonld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        afirma(len(jsonld) >= 1, "%s: sem JSON-LD" % caminho)
        for j in jsonld:
            try:
                json.loads(j)
            except Exception as e:
                afirma(False, "%s: JSON-LD invalido (%s)" % (caminho, e))
        if caminho not in ("/", ""):
            afirma(any("BreadcrumbList" in j for j in jsonld),
                   "%s: sem BreadcrumbList, e a 16.4 o exige em toda pagina que nao e a home"
                   % caminho)
            afirma("rdm-trilha" in html, "%s: sem trilha na tela" % caminho)

        # Menu acessivel (secao 6), favicon proprio e marca.
        afirma('aria-expanded' in html and 'aria-controls' in html,
               "%s: o botao do menu esta sem aria-expanded/aria-controls" % caminho)
        afirma('rel="icon"' in html and "image/svg+xml" in html,
               "%s: sem favicon proprio — icone padrao do WordPress na aba e bloco reprovado"
               % caminho)
        afirma("rdm-marca" in html, "%s: a casca nao pintou a marca" % caminho)
        afirma(html.count("rdm-rodape") >= 1, "%s: sem rodape da casca" % caminho)
        afirma(len(re.findall(r'class="rdm-rodape"', html)) <= 1,
               "%s: DOIS rodapes empilhados" % caminho)

        # Imagem com width/height e alt (secao 6 e 32.3).
        for img in re.findall(r"<img[^>]*>", corpo):
            afirma("alt=" in img, "%s: <img> sem alt: %s" % (caminho, img[:80]))
            afirma("width=" in img and "height=" in img,
                   "%s: <img> sem width/height: %s" % (caminho, img[:80]))

        # 32.4: zero palavra de bastidor no texto SERVIDO.
        for termo in bastidor:
            afirma(termo.lower() not in texto.lower(),
                   "32.4: a palavra de bastidor %r aparece no texto servido de %s"
                   % (termo, caminho))

        # Shortcode cru na tela e desembarque que nao aconteceu.
        afirma("[rodametria_" not in texto,
               "%s: shortcode cru servido na tela — o snippet nao esta ativo" % caminho)

    # -------------------------------------------------------------------
    # 6. A F2, AFIRMACAO POR AFIRMACAO CONTRA O BANCO
    # -------------------------------------------------------------------
    d = json.load(open(os.path.join(ILHA, "dados", "f2-respostas.json"), encoding="utf-8"))
    alvo = None
    for u in todas:
        if "autonomia" in u:
            alvo = u.replace(DOMINIO, "")
    afirma(alvo is not None, "a F2 nao esta no sitemap")
    if alvo:
        cod, _, html = buscar(alvo)
        corpo = corpo_da_pagina(html)
        texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo))

        # (4) o script vem do RODAPE e a tabela aparece no HTML servido.
        pos_script = html.find('id="rodametria-f2-js"')
        pos_corpo = html.find("rdm-tabela")
        afirma(pos_script > pos_corpo > 0,
               "a F2 serve o script antes da tabela — o JS tinha de vir do rodape")
        afirma("rdm-tabela" in html, "a F2 nao serve a tabela pre-renderizada")

        # A CAIXA DE RESULTADO ESTA PRE-RENDERIZADA: o numero do exemplo tem de
        # estar no HTML servido, sem ninguem clicar em nada. E a 32.1 item 4 e a
        # secao 5 (visibilidade em IA) na mesma afirmacao.
        r = d["resposta_exemplo"]
        afirma(r["piso_km_tela"] in corpo,
               "a F2 nao serve o piso de km do exemplo (%s) no HTML" % r["piso_km_tela"])
        afirma(r["teto_km_tela"] in corpo,
               "a F2 nao serve o teto de km do exemplo (%s) no HTML" % r["teto_km_tela"])
        for f in r["frases_km"] + r["frases_peso"]:
            limpo = re.sub(r"\s+", " ", f)
            afirma(limpo[:60] in texto,
                   "a F2 nao serve a frase do banco: %r" % limpo[:70])

        # A RESSALVA DO PESO ESTA DEPOIS DO BLOCO DE COMPRA, e nao dentro da
        # caixa: e o que mantem o primeiro botao de compra acima do teto de
        # 1.400 px da 32.5 no telefone de 390 px.
        pos_compra = corpo.find("rdm-molde-compra")
        pos_ressalva = corpo.find("rdm-f2-ressalva")
        afirma(0 < pos_compra < pos_ressalva,
               "a ressalva do peso nao esta depois do bloco de compra (compra em %d, "
               "ressalva em %d)" % (pos_compra, pos_ressalva))

        # TODA linha da tabela do banco esta no ar, com o Wh que o banco diz.
        for l in d["tabela"]["do_banco"] + d["tabela"]["externas"]:
            afirma(l["rotulo"] in corpo,
                   "a linha %r da tabela nao esta no ar" % l["rotulo"])
            afirma(l["wh"] in corpo,
                   "o Wh %r da linha %r nao esta no ar" % (l["wh"], l["rotulo"]))

        # O BLOCO DE COMPRA: conta CARTAO contra BLOCO, nunca a classe de um
        # degrau (secao 8 — sete reguas quebraram por procurar o rotulo do
        # degrau). O degrau viaja como registro, nunca como criterio.
        cartoes = re.findall(r'class="rdm-molde-cartao"', corpo)
        afirma(len(cartoes) == len(d["compra"]["vitrine"]),
               "o bloco de compra serve %d cartao(oes) e a vitrine do banco tem %d"
               % (len(cartoes), len(d["compra"]["vitrine"])))
        afirma(len(cartoes) >= 1,
               "o bloco de compra esta VAZIO, e a secao 7 proibe: o piso e o link de busca")
        for f in d["compra"]["vitrine"]:
            afirma(f["url_busca"] in corpo,
                   "a saida de compra de %s nao esta no ar" % f["id"])
            afirma(f["nome"] in corpo, "o nome de %s nao esta no ar" % f["id"])
        for a in re.findall(r"<a[^>]*s\.shopee\.com\.br[^>]*>", corpo):
            afirma('rel="sponsored noopener"' in a,
                   "link de afiliado sem rel sponsored: %s" % a[:90])
            afirma('target="_blank"' in a,
                   "link de afiliado sem target _blank: %s" % a[:90])
        registro("bloco de compra: %d cartao(oes), degrau(s) %s"
                 % (len(cartoes), sorted({f["degrau"] for f in d["compra"]["vitrine"]})))

        # A PRESTACAO DE CONTAS FECHA NO AR, e o numero e lido da TELA.
        total = d["compra"]["total_registros_veiculos"]
        soma = sum(len(v) for v in d["compra"]["grupos"].values())
        afirma(soma == total, "a prestacao de contas do banco nao fecha: %d de %d" % (soma, total))
        m = re.search(r"São (\d+) veículos nomeados de (\d+) no banco", texto)
        afirma(bool(m), "a F2 nao serve a frase que fecha a prestacao de contas")
        if m:
            afirma(int(m.group(1)) == int(m.group(2)) == total,
                   "a tela diz %s nomeados de %s e o banco tem %d"
                   % (m.group(1), m.group(2), total))

        # Toda dobra e <details> de verdade: o texto continua no HTML servido.
        dobras = re.findall(r"<details[^>]*class=\"rdm-molde-dobra\"", corpo)
        afirma(len(dobras) >= 3,
               "a F2 tem %d dobra(s) e a 32.1 item 7 pede o texto recolhivel em secoes" % len(dobras))

        # O aviso de comissao existe e esta visivel (secao 7).
        afirma("comiss" in texto.lower(), "a F2 nao serve o aviso de comissao")

    # -------------------------------------------------------------------
    # 7. O QUE ESTE PORTAO NAO MEDIU — dito, nunca aprovado em silencio
    # -------------------------------------------------------------------
    # Esta linha dizia "que esta ilha ainda nao tem", e envelheceu em UMA HORA:
    # o portao nasceu na mesma execucao. Frase sobre o estado da fabrica dentro
    # de um portao e a mesma divida do numero de tela digitado — ela nao fala
    # com o que descreve. Agora ela CONFERE que o arquivo existe.
    tem_portao_de_pixel = os.path.exists(
        os.path.join(AQUI, "conferir-32-5-no-navegador.mjs"))
    registro("NAO MEDIDO AQUI: a 32.5 (formulario antes de 700 px, primeiro botao de compra "
             "antes de 1.400 px) se mede a 390 px num navegador de verdade. O portao de "
             "pixel %s — rode `node ferramentas/conferir-32-5-no-navegador.mjs`."
             % ("EXISTE nesta ilha e NAO foi rodado por este portao"
                if tem_portao_de_pixel else
                "NAO EXISTE nesta ilha, e a 32.5 segue sem ser medida em pixel"))
    registro("NAO MEDIDO AQUI: a leitura SEM quebra de cache (como o Google le). Toda URL acima "
             "foi pedida com ?v=<agora>, entao estas afirmacoes sao sobre a ORIGEM.")

    return encerrar()


def encerrar():
    print("conferir-no-ar: %d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
    for r in registros:
        print("  registro: %s" % r)
    for f in falhas:
        print("  REPROVADO: %s" % f)
    print("APROVADO" if not falhas else "REPROVADO")

    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

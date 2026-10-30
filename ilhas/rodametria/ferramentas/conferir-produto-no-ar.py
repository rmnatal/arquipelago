#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONFERE NO AR AS PAGINAS DE VITRINE (secao 30) — A ESCADA DA 25.2 NA TELA.

    python3 ferramentas/conferir-produto-no-ar.py

POR QUE ELE NASCEU EM 30/10/2026, e a causa e uma LACUNA e nao um defeito:
`conferir-no-ar.py` confere a casca e a F2, e `conferir-institucional-no-ar.py`
confere as quatro paginas do bloco 5d. As paginas de VITRINE — `/veiculos/` e as
filhas — nao tinham portao de ar NENHUM desde que nasceram em 29/10. O que as
media era `conferir-32-5-no-navegador.mjs`, que julga PIXEL, e `mutacoes-produto.py`,
que roda sem rede sobre o gerador. **Entre os dois faltava quem lesse o HTML
servido.** E foi justamente ali que a escada da 25.2 tinha TRES lugares lendo a
`url` crua do dado.

O QUE ELE COBRA, e cada item e uma coisa que o dado de hoje NAO exercita:
  1. ZERO `href=""` no HTML servido. Era o estado em que a celula "Comprar" da
     tabela cairia no dia em que uma ficha morresse — e `href=""` nao e botao
     morto: e um botao que RECARREGA A PROPRIA PAGINA, com o rotulo "Ver na
     Shopee" do lado.
  2. A LINHA DISCRETA DO PISO da 25.2, UMA vez por pagina. Uma, e nao uma por
     linha, porque o piso e da CONSULTA e nao do anuncio — ha UMA `url_busca`
     distinta por pagina, e repeti-la seria o mesmo link dezesseis vezes.
  3. TODO anuncio da vitrine NOMEADO na tabela (secao 7) e com saida de compra.
  4. `rel="sponsored noopener"` e `target="_blank"` em TODO link de afiliado.
  5. O JSON-LD: nenhuma `Offer` com `url` vazia, e `availability` so onde ha
     ficha — afirmar estoque sobre um resultado de busca e afirmar o que ninguem
     mediu.

ELE DESCOBRE AS URLs NO `wp-sitemap.xml` LIDO NO AR, nunca de uma lista, pela
frase da 32.5-b: "regua que nao varre todas certifica a pagina que o autor
abriu". Pagina de vitrine nova entra no dia em que desembarca.
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
    """Quebra de cache sempre: as afirmacoes daqui sao sobre a ORIGEM."""
    url = DOMINIO + caminho
    url += ("&" if "?" in caminho else "?") + "v=" + str(int(time.time() * 1000))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, "ERRO: %s" % e


def corpo_da_pagina(html):
    """So o CORPO: `<script>` fora, senao a afirmacao sobre o que a pagina DIZ
    se acha dentro do proprio JSON-LD."""
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)
    return corpo


def urls_do_sitemap():
    """TODA URL do sitemap, lida no ar. O sitemap do WordPress e um indice."""
    cod, xml = buscar("/wp-sitemap.xml")
    if cod != 200:
        return cod, []
    urls = []
    for sub in re.findall(r"<loc>([^<]+)</loc>", xml):
        if "wp-sitemap" in sub:
            c2, x2 = buscar(sub.replace(DOMINIO, ""))
            if c2 == 200:
                urls += re.findall(r"<loc>([^<]+)</loc>", x2)
        else:
            urls.append(sub)
    return cod, sorted(set(urls))


def vitrine_do_repositorio():
    """A FONTE, lida do repositorio: o que a tela DEVIA servir."""
    with open(os.path.join(ILHA, "dados", "vitrine-de-produto.json"), encoding="utf-8") as f:
        d = json.load(f)
    return {p["slug"]: p for p in d.get("paginas", []) if p.get("slug")}


def normalizar(t):
    """O NOME COMO ELE E COMPARAVEL, e as tres normalizacoes sao CICATRIZ.

    (1) `unescape`, porque `esc_html()` troca a aspa reta por `&quot;` e um
        titulo desta vitrine tem `10"`.
    (2) espaco colapsado, porque dois titulos trazem ESPACO DUPLO da loja.
    (3) TRAVESSAO VIRA HIFEN, e esta e a que vale registro: o WordPress roda os
        filtros do `the_content` sobre o retorno do shortcode, e o `wptexturize`
        troca o hifen CERCADO DE ESPACOS por EN DASH. Medido em 30/10/2026 no
        `patinete-eletrico`: o dado diz `550W - 40km/h` e o corpo serve
        `550W &#8211; 40km/h`. O JSON-LD, que sai no `wp_head` e NAO passa por
        aquele filtro, serve o hifen cru — entao o MESMO nome sai de duas formas
        na MESMA pagina. Nao e defeito a consertar: e tipografia do WordPress, e
        brigar com ela custa mais do que vale. E a mesma pedra que esta ilha ja
        tem escrita no topo da casca ("o WordPress troca && por &#038;&#038; no
        retorno do shortcode"), num traje novo — e quem nao a souber escreve uma
        regua que reprova a pagina certa.
    """
    t = html_lib.unescape(str(t or ""))
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", t).strip()


def texto_do_corpo(html):
    """O texto que a PESSOA le, com as entidades JA DESFEITAS.

    O `unescape` nao e detalhe, e esta regua o aprendeu reprovando a pagina
    CERTA na primeira passada: `esc_html()` transforma a aspa reta em `&quot;`,
    e o anuncio `Patinete Eletrico Scooter 350W 10" com App` nunca casaria com o
    nome do dado. E a mesma pedra em que `conferir-institucional-no-ar.py`
    bateu, e o comentario dele diz por que ela importa: portao que reprova
    pagina certa e o caminho mais curto para alguem passar a ignora-lo.
    """
    return normalizar(re.sub(r"<[^>]+>", " ", corpo_da_pagina(html)))


ROTULO_DO_PISO = "Veja todos disponíveis aqui"

# A LINHA DO PISO DA TABELA SE CONTA PELA CLASSE, NUNCA PELA FRASE, e a primeira
# versao desta regua contou pela frase e reprovou a pagina certa: a MESMA frase e
# a linha discreta de cada CARTAO do carrossel (25.2), entao ela aparece 5 vezes
# numa pagina sa antes de a tabela existir. Contar a frase e medir duas coisas
# diferentes com a mesma regua — a familia das sete reguas desta fabrica que
# quebraram por procurar o rotulo de UM degrau.
CLASSE_DO_PISO_DA_TABELA = 'class="rdm-tabela-piso"'


def main():
    cod, urls = urls_do_sitemap()
    if not afirma(cod == 200, "o wp-sitemap.xml nao respondeu 200 (deu %s)" % cod):
        return encerrar()

    fonte = vitrine_do_repositorio()
    afirma(bool(fonte), "dados/vitrine-de-produto.json nao tem pagina nenhuma")

    # AS PAGINAS DE VITRINE SE DESCOBREM PELO CASAMENTO entre o sitemap no ar e
    # os slugs da fonte — nunca por uma lista digitada aqui.
    # O `slug` da fonte e o CAMINHO INTEIRO (`veiculos/patinete-eletrico`), nao a
    # ultima parte — e a primeira versao desta regua comparou a ultima parte e
    # achou ZERO pagina, denunciando-se com "este portao ficou cego" em vez de
    # aprovar em silencio. E o que a 32.5-b pede: regua que nao varre todas diz
    # que nao varreu.
    alvos = []
    for u in urls:
        caminho = u.replace(DOMINIO, "")
        slug = caminho.strip("/")
        if slug in fonte:
            alvos.append((caminho, slug))

    if not afirma(alvos, "nenhuma pagina de vitrine achada no sitemap: este portao ficou cego"):
        return encerrar()
    registro("paginas de vitrine descobertas no sitemap: %d (%s)"
             % (len(alvos), ", ".join(s for _, s in alvos)))

    for caminho, slug in alvos:
        pg = fonte[slug]
        linhas = pg.get("linhas", [])
        cod, html = buscar(caminho)
        if not afirma(cod == 200, "%s nao respondeu 200 (deu %s)" % (caminho, cod)):
            continue
        corpo = corpo_da_pagina(html)

        # (1) O href VAZIO, e ele e medido no HTML INTEIRO e nao so no corpo.
        vazios = len(re.findall(r'href=""', html)) + len(re.findall(r"href=''", html))
        afirma(vazios == 0,
               "%s serve %d href vazio: botao que recarrega a propria pagina" % (caminho, vazios))

        # (2) A LINHA DISCRETA DO PISO, uma vez.
        buscas = {str(l.get("url_busca") or "").strip() for l in linhas}
        buscas.discard("")
        quantos = corpo.count(CLASSE_DO_PISO_DA_TABELA)
        nos_cartoes = corpo.count(ROTULO_DO_PISO) - quantos
        if len(buscas) == 1:
            afirma(quantos == 1,
                   "%s serve a linha do piso da TABELA %d vez(es) e devia servir UMA: o piso e da "
                   "consulta, nao do anuncio" % (caminho, quantos))
            afirma(list(buscas)[0] in corpo,
                   "%s nao serve o piso da 25.2 (%s)" % (caminho, list(buscas)[0]))
        else:
            afirma(quantos == 0,
                   "%s tem %d buscas distintas na fonte e ainda serve a linha unica do piso da "
                   "tabela: 'a primeira' e arbitraria" % (caminho, len(buscas)))

        # (3) TODO anuncio NOMEADO, e TODO anuncio com saida de compra.
        texto = texto_do_corpo(html)
        for l in linhas:
            # OS DOIS LADOS PASSAM PELA MESMA NORMALIZACAO, nunca um so: regua
            # que normaliza metade reprova a pagina certa (ver `normalizar`).
            nome = normalizar(l.get("nome"))
            afirma(nome in texto,
                   "%s nao nomeia o anuncio %r: a secao 7 manda nomear todo item uma vez"
                   % (caminho, nome[:40]))
            saida = str(l.get("url") or "").strip() or str(l.get("url_busca") or "").strip()
            afirma(saida != "",
                   "%s: o anuncio %r nao tem saida de compra NENHUMA no dado — defeito da 19.1 "
                   "pela 25.2" % (caminho, nome[:40]))
            if saida:
                afirma(saida in corpo,
                       "%s: a saida de compra do anuncio %r nao esta no ar" % (caminho, nome[:40]))
        afirma("rdm-tabela" in corpo, "%s nao serve a tabela pre-renderizada (32.1 item 6)" % caminho)
        afirma("sem link de compra hoje" not in corpo,
               "%s serve celula 'sem link de compra hoje': ha anuncio sem saida no ar" % caminho)

        # (4) rel e target em TODO link de afiliado.
        for a in re.findall(r"<a[^>]*s\.shopee\.com\.br[^>]*>", corpo):
            afirma('rel="sponsored noopener"' in a,
                   "%s: link de afiliado sem rel sponsored: %s" % (caminho, a[:90]))
            afirma('target="_blank"' in a,
                   "%s: link de afiliado sem target _blank: %s" % (caminho, a[:90]))

        # (5) O JSON-LD, que e o lugar mais silencioso dos tres: `"url": ""` numa
        #     `Offer` e dado estruturado invalido que olho humano nao ve.
        ofertas = 0
        com_disponibilidade = 0
        for bloco in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                dado = json.loads(bloco)
            except Exception:
                afirma(False, "%s serve JSON-LD que nao parseia" % caminho)
                continue
            if not isinstance(dado, dict) or dado.get("@type") != "ItemList":
                continue
            itens = dado.get("itemListElement") or []
            afirma(len(itens) == len(linhas),
                   "%s: o ItemList tem %d itens e a vitrine tem %d linhas"
                   % (caminho, len(itens), len(linhas)))
            for it in itens:
                of = ((it or {}).get("item") or {}).get("offers") or {}
                if not of:
                    continue
                ofertas += 1
                afirma(str(of.get("url") or "").strip() != "",
                       "%s: uma Offer do JSON-LD esta com url vazia" % caminho)
                if of.get("availability"):
                    com_disponibilidade += 1
        afirma(ofertas == len(linhas),
               "%s: o JSON-LD serve %d Offer(s) e a vitrine tem %d linhas"
               % (caminho, ofertas, len(linhas)))
        # HOJE TODA LINHA TEM FICHA, entao toda Offer declara estoque. No dia em
        # que uma ficha morrer, este numero cai — e esta linha e quem o mostra,
        # em vez de o portao aprovar em silencio.
        com_ficha = sum(1 for l in linhas if str(l.get("url") or "").strip())
        afirma(com_disponibilidade == com_ficha,
               "%s: %d Offer(s) declaram availability e %d linha(s) tem ficha — estoque de "
               "resultado de busca e afirmacao sem medicao"
               % (caminho, com_disponibilidade, com_ficha))

        registro("%s: %d linha(s), %d com ficha, %d href vazio, piso da tabela %dx, a MESMA frase "
                 "%dx nos cartoes do carrossel, %d Offer(s) (%d com availability)"
                 % (caminho, len(linhas), com_ficha, vazios, quantos, nos_cartoes, ofertas,
                    com_disponibilidade))

    registro("NAO MEDIDO AQUI: pixel. A 32.5 e trabalho de "
             "conferir-32-5-no-navegador.mjs, que abre a pagina a 390 px num navegador.")
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

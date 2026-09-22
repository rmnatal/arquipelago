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
    # O que importa medir e que o sitemap cobre o que a ilha publica: o que esta
    # fora do eixo MAIS o eixo inteiro, e nada a menos.
    #
    # O "13 ANTIGAS" ERA A METADE DIGITADA QUE SOBRAVA AQUI, e ela envelheceu em
    # 13/09/2026, no dia em que /politica-de-privacidade/ nasceu: o alarme
    # reprovou dizendo "o sitemap publica as 27 URLs da ilha" quando o certo era
    # 28, e a frase estava errada nas duas metades — no numero e no que ela
    # afirmava. Trocar 13 por 14 so reagendaria o defeito para a proxima pagina
    # institucional, que e exatamente o que a secao 8 do contrato proibe fazer
    # com literal ("trocar o literal por outro literal so reagenda"). Entao o
    # numero passa a ser DERIVADO das duas fontes que criam pagina nesta ilha:
    #
    #   * a casca, pelo `$base` de aquametria_casca_definicao_paginas() — quatro
    #     hoje, e o dia em que uma quinta entrar ali o numero anda sozinho;
    #   * o manifest, pelos itens de conteudo/ com publicar=true — e o Sync que
    #     cria pagina a partir deles, entao o manifest e a fonte de quem publica,
    #     nao o diretorio.
    #
    # O eixo continua vindo do proprio portao (TP), como ja vinha.
    with open(os.path.join(RAIZ, "snippets", "aquametria-casca.php"),
              encoding="utf-8") as fh:
        fonte_casca = fh.read()
    bloco = re.search(r"\$base\s*=\s*array\((.*?)\n\t\);", fonte_casca, re.S)
    ok("achei o bloco $base da casca, de onde saem as paginas dela", bloco is not None)
    paginas_da_casca = len(re.findall(r"^\s*'[a-z0-9-]+'\s*=>\s*array\(",
                                      bloco.group(1), re.M)) if bloco else 0
    manifest = json.load(open(os.path.join(RAIZ, "manifest.json"), encoding="utf-8"))
    paginas_de_conteudo = sum(1 for it in manifest["conteudo"] if it.get("publicar"))
    urls_antes_do_eixo = paginas_da_casca + paginas_de_conteudo
    ok("as paginas fora do eixo sao contadas, nunca digitadas",
       paginas_da_casca > 0 and paginas_de_conteudo > 0,
       "%d da casca + %d de conteudo/ = %d" %
       (paginas_da_casca, paginas_de_conteudo, urls_antes_do_eixo))
    # secao + uma pagina por categoria + as fichas
    esperado = urls_antes_do_eixo + 1 + len(TP.CATEGORIAS) + len(TP.FICHAS)
    ok("o sitemap publica as %d URLs da ilha (%d fora do eixo + o eixo /peixes/)"
       % (esperado, urls_antes_do_eixo),
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
        # A LARGURA QUE A PAGINA PUBLICA, e nao a que o banco tem (22/09/2026).
        # `chao_declarado_para` (esquema versao 5) diz para QUAL populacao a base
        # foi declarada, e a ficha cujo chao foi declarado para outra gente nao
        # serve o fundo — logo nao serve nenhuma das duas tabelas que dependem
        # dele. Sem esta linha a regua cobraria no ar, da agassizii, a frase que
        # a correcao de hoje tirou de la de proposito.
        chao = (e.get("chao_declarado_para") or {}).get("arranjos") or []
        niveis = {"juvenis": 0, "um-exemplar": 1, "casal": 2, "grupo": 3}
        populacao = {"solitario": "um-exemplar", "casal": "casal", "cardume": "grupo",
                     "grupo": "grupo", "harem": "grupo"}.get(e.get("convivencia"))
        fundo_de_outro = bool(
            chao and "nao-declarado" not in chao and populacao
            and niveis[populacao] > max(niveis[a] for a in chao if a in niveis)
        )
        largura = None if fundo_de_outro else (e.get("base_minima_cm") or {}).get("largura")
        if fundo_de_outro:
            ok("%s: no ar, nao promete a esta populacao o chao declarado para outra" % slug,
               "a largura declarada é para outra quantidade de peixe" in t
               and "em três alturas de aquário" not in t,
               t[max(0, t.find("cm de frente")):][:140])
            ok("%s: no ar, publica o fundo dizendo para quem ele foi declarado" % slug,
               "foi declarada para" in t and "que é outra quantidade de peixe" in t)

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

        # --- AS DUAS FRASES QUE A LEVA 5 CONSERTOU, medidas NO AR (14/09/2026).
        #
        # As duas estavam servidas e erradas antes deste bloco, e as duas so
        # erram quando a contagem e UM — por isso atravessaram quatorze fichas
        # sem ninguem ver. A bancada mede as duas desde hoje; elas moram TAMBEM
        # aqui porque o corpo da ficha e um shortcode, entao a mudanca que vem do
        # snippet nao move `post_modified` e nao aparece em log de desembarque
        # nenhum: a unica prova de que o conserto chegou e o HTML servido.
        # A REGUA DAS DUAS ERA `in`, E `in` NAO SABE ONDE O NUMERO COMECA
        # (medido em 14/09/2026, na preparacao da leva 6). As duas linhas abaixo
        # nasceram como teste de substring — "1 estão na tabela" not in t — e
        # isso REPROVA a ficha do peixe-espada no dia em que a contagem dela
        # chega a 21, porque "21 estão na tabela" contem "1 estão na tabela".
        # Foi exatamente o que aconteceu: duas especies novas no banco levaram a
        # tabela de vizinhos de temperatura de 20 para 21 e a conferencia no ar
        # acusou um defeito que a pagina nao tinha. E a mesma familia do numero
        # de tela digitado que esta ilha persegue, do lado do portao: regua que
        # falha ERRADO custa tanto quanto regua que nao falha.
        #
        # O `(?<![\d.,])` e o conserto inteiro: so casa o 1 que comeca o numero.
        # A intencao nao mudou — pegar a concordancia agramatical com UM.
        if e.get("comportamento") != "agressivo":
            um_ficaram = re.search(r"(?<![\d.,])1 ficaram fora", t)
            ok("%s: no ar, a prestacao de contas nunca diz '1 ficaram'" % slug,
               um_ficaram is None,
               t[max(0, um_ficaram.start() - 90):][:180] if um_ficaram else "")
            ok("%s: no ar, a prestacao de contas nunca diz '1 estao'" % slug,
               re.search(r"(?<![\d.,])1 estão na tabela", t) is None)
        if largura and e.get("convivencia") not in TP.ARRANJO_FIXO:
            v_meio = frente[1] * float(largura) * TP.ALTURAS[1] / 1000.0
            classica = int(math.floor((v_meio / TP.CLASSICA) / porte[1]))
            conserv = int(math.floor((v_meio / TP.CONSERVADORA) / porte[1]))
            ok("%s: no ar, 'cabe'/'cabem' concorda com o numero" % slug,
               ("%s %d " % ("cabe" if conserv == 1 else "cabem", conserv)) in t,
               t[max(0, t.find("de altura cab")):][:120])
            if conserv >= 1:
                # A RAZAO E A DOS DOIS NUMEROS IMPRESSOS, nunca a das constantes:
                # ate 14/09 a pagina anunciava 4 vezes em toda ficha, e o
                # arredondamento para baixo fazia disso mentira em dez das
                # quatorze no ar — 6 vezes na sterbai, 7 no peixe-espada.
                ok("%s: no ar, a razao publicada e a dos dois numeros da tela" % slug,
                   ("A diferença entre os dois é de %s vezes"
                    % TP.numero_br(classica / conserv)) in t,
                   t[max(0, t.find("A diferença entre os dois")):][:110])

    # --- A PRESTACAO DE CONTAS DE QUEM NAO ESTA NA TABELA, no HTML servido.
    #
    # Mora aqui e nao so na bancada porque o corpo da secao e um SHORTCODE: a
    # mudanca que vem do snippet nao move `post_modified` e nao aparece em log de
    # desembarque nenhum — o Sync pode dizer "0 aplicado(s)" e a tela ter mudado,
    # ou nao ter mudado. A unica prova de que o bloco chegou ao ar e ler o HTML
    # que o servidor devolve, e e a mesma cicatriz dos nove titulos de 11/09.
    print("\nOS AUSENTES DO CATALOGO, no HTML servido pela secao")
    c_secao = TP.corpo(servidas["peixes"])
    t_secao = TP.texto(c_secao)
    esperados = TP.barrados_do_banco(banco)
    lista = re.search(r'<ul class="aqm-px-barrados">(.*?)</ul>', c_secao, re.S)
    ok("no ar, a secao serve a lista de ausentes", lista is not None)
    ok("no ar, a frase conta os %d registros do banco" % len(banco),
       ("guarda %d registros de espécie" % len(banco)) in t_secao)
    ok("no ar, a frase conta os %d que ficaram de fora" % len(esperados),
       ("Os outros %d estão aqui pelo nome" % len(esperados)) in t_secao)
    ok("no ar, nenhum nome de campo do banco vaza para o corpo",
       not [cod for cod in TP.CAMPOS_DO_PORTAO if cod in t_secao])
    ok("no ar, nenhum motivo caiu no ramo sem traducao",
       "ainda não tem nome nesta tela" not in t_secao)
    if lista is not None:
        itens = [TP.texto(x) for x in re.findall(r"<li>(.*?)</li>", lista.group(1), re.S)]
        ok("no ar, um item por ausente (%d)" % len(esperados), len(itens) == len(esperados),
           "%d itens" % len(itens))
        for ident, codigos in esperados.items():
            nome = banco[ident]["nome_cientifico"]
            achados = [x for x in itens if nome in x]
            ok("no ar, %s aparece uma vez so" % ident, len(achados) == 1, "%d" % len(achados))
            if achados:
                ok("no ar, a causa de %s esta em lingua de gente" % ident,
                   all(TP.traducao_do_motivo(cod) and TP.traducao_do_motivo(cod) in achados[0]
                       for cod in codigos), achados[0])

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

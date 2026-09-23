#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao da ESCADA DA SECAO 25 dentro do banco da Aquametria.

    python3 ferramentas/teste-escada-compra.py [raiz]

Ele mede tres coisas que o validador sozinho nao mede:

1. **Os numeros do relatorio sao CONTADOS, nao digitados.** Este portao recomputa
   as cinco contagens da escada lendo os arquivos de produto com regua propria e
   exige que batam com as que `validar-produtos.py` imprime. Sem isto, "78 de 78
   sem piso" seria uma frase, e frase envelhece calada — que e exatamente o
   defeito que a secao 4 do contrato paga mais caro.

2. **A escada declarada no esquema e a da 25.1 inteira.** Os quatro degraus, com
   os nomes deles, e um termo de contexto para CADA arquivo de produto. Entidade
   nova sem termo nao pode entrar em silencio: ela geraria busca so por marca, e
   a 25.3 mostra o que isso traz — a JBL de caixa de som e a "Aquario" de
   roteador.

3. **O gerador da busca e IDEMPOTENTE.** Rodar duas vezes nao pode mover nada.
   Gerador que muda a palavra-chave a cada passada moveria o piso de 78 itens
   sem ninguem decidir.

4. **O PISO CHEGA NA TELA** (14/09/2026). As tres acima medem o repositorio e
   nenhuma encosta no que o leitor ve — e era exatamente ali que a divida vivia:
   os 78 itens tinham a palavra-chave escrita desde 13/09 e nenhum snippet a
   lia, entao 39 produtos chegavam na pagina com "link de loja em breve" no
   lugar do botao. Esta secao renderiza as quatro calculadoras e confere, no
   CORPO servido, que todo cartao e ancora e que o href dela sai do banco.

Uma afirmacao por linha, e o codigo de saida e 1 na primeira falha contada.
"""
import json
import os
import re
import subprocess
import sys
from urllib.parse import unquote

RAIZ = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVOS = {
    "filtro": "dados/produtos-filtro.json",
    "aquecedor": "dados/produtos-aquecedor.json",
    "iluminacao": "dados/produtos-iluminacao.json",
    "midia": "dados/produtos-midia.json",
}
DEGRAUS_DA_251 = {
    1: "loja-oficial-shopee",
    2: "catalogo-mercadolivre",
    3: "anuncio-vendedor-shopee",
    4: "busca",
}

falhas = []
afirmacoes = [0]


def confere(condicao, texto):
    afirmacoes[0] += 1
    if not condicao:
        falhas.append(texto)
        print("  FALHA %s" % texto)


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return json.load(f)


def preenchido(v):
    return v is not None and v != "" and v != []


# ---------------------------------------------------------------------------
# 4. O PISO CHEGA NA TELA — 14/09/2026, item 4 do despacho do Raphael
#
# As tres secoes acima medem o BANCO. Nenhuma delas encosta no que o leitor ve, e
# era exatamente ali que a divida vivia: os 78 itens tinham a palavra-chave da
# busca escrita desde 13/09 e NENHUM snippet a lia, entao 39 produtos chegavam na
# pagina com "link de loja em breve" no lugar do botao — a frase que a secao 7
# passou a proibir. Portao que mede so o repositorio deixa passar exatamente o
# defeito que a secao 4 do contrato paga mais caro: o que esta commitado e nao
# esta no ar, ou o contrario.
#
# A regua e PROPRIA e mede no CORPO, nunca no HTML inteiro: ela renderiza cada
# calculadora com render-para-teste.php, arranca <style> e <script>, e confere o
# href de cada cartao contra o BANCO — nao contra o catalogo embutido no snippet,
# que e copia do banco e erraria junto com ele. E ela nao chama nenhuma funcao da
# pagina: a escada da 25.1 esta reescrita aqui em quinze linhas, porque quem
# confere escreve a propria regua (secao 8 do ARQUIPELAGO.md).
# ---------------------------------------------------------------------------
CALCULADORAS = {
    "c3": ("aquametria_calculadora_vazao", "filtro"),
    "c5": ("aquametria_calculadora_aquecedor", "aquecedor"),
    "c12": ("aquametria_calculadora_midia", "midia"),
    "c15": ("aquametria_calculadora_iluminacao", "iluminacao"),
}
PROIBIDA = "link de loja em breve"


def corpo_servido(shortcode):
    r = subprocess.run(["php", os.path.join(RAIZ, "ferramentas/render-para-teste.php"),
                        RAIZ, shortcode], capture_output=True, text=True, cwd=RAIZ)
    if r.returncode != 0:
        return None, (r.stderr or r.stdout)[-400:]
    html = r.stdout
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S)
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S)
    return html, None


def saidas_do_banco():
    """Toda URL de compra que o banco autoriza a aparecer numa pagina.

    TRES listas, e ate 23/09/2026 eram duas. A versao antiga somava o
    `url_busca` ENCURTADO ao conjunto das fichas, com o argumento escrito no
    proprio docblock: *"a FICHA paga comissao e a busca CRUA nao"*. Naquele
    mundo isso era verdade por acidente — o unico link que pagava era a ficha,
    porque encurtar a busca exigia o Raphael abrir o painel, e nenhum registro
    tinha `url_busca`.

    **A Open API (25.6) desfez a coincidencia no dia em que os 78 pisos foram
    encurtados**: a busca passou a pagar comissao e continuou sendo a busca. A
    regua, lida ao pe da letra, passou a exigir "a linha discreta do piso
    embaixo" de cartoes cujo botao JA E o piso — sete cartoes reprovados, todos
    certos. E a mesma familia das duas reguas que a leva 8 consertou em 22/09:
    regra que so funcionava porque duas coisas andavam juntas para de medir no
    dia em que elas se separam.

    Sao dois eixos independentes, e agora eles se cruzam:
      - **o que o link E** — ficha de produto ou busca. So a ficha leva a linha
        discreta do piso embaixo (25.2), porque so ela pode apodrecer.
      - **se o link PAGA** — `sponsored` contra `nofollow`. Isso decide a
        marcacao e o selo, e nada mais.
    """
    fichas, pisos_pagos, pisos_crus = set(), set(), set()
    for caminho in ARQUIVOS.values():
        for p in carregar(caminho).get("produtos", []):
            a = p.get("afiliado") or {}
            if preenchido(a.get("url")):
                fichas.add(a["url"])
            if preenchido(a.get("url_busca")):
                pisos_pagos.add(a["url_busca"])
            elif preenchido(a.get("url_busca_produto")):
                pisos_crus.add(a["url_busca_produto"])
    return fichas, pisos_pagos, pisos_crus


def mede_o_piso_na_tela():
    print("\n== o piso da 25.2 chega na tela, e nenhuma pagina fica sem saida de compra ==")
    fichas, pisos_pagos, pisos_crus = saidas_do_banco()

    for prefixo, (shortcode, _entidade) in sorted(CALCULADORAS.items()):
        corpo, erro = corpo_servido(shortcode)
        if corpo is None:
            confere(False, "%s: o render falhou (%s)" % (prefixo, erro))
            continue

        confere(PROIBIDA not in corpo,
                "%s: o corpo servido ainda escreve %r, proibido pela secao 7 desde 14/09/2026"
                % (prefixo, PROIBIDA))

        itens = re.findall(r'<li class="aqm-%s-vt-item[^"]*">(.*?)</li>' % prefixo, corpo, flags=re.S)
        confere(len(itens) > 0, "%s: a vitrine servida nao tem cartao nenhum para medir" % prefixo)

        for i, item in enumerate(itens, 1):
            cartao = re.search(r'<(a|div) class="aqm-%s-vt-cartao[^"]*"([^>]*)>' % prefixo, item)
            confere(cartao is not None, "%s cartao %d: nao achei o cartao" % (prefixo, i))
            if cartao is None:
                continue

            confere(cartao.group(1) == "a",
                    "%s cartao %d: saiu como <%s> em vez de ancora — cartao sem saida de compra"
                    % (prefixo, i, cartao.group(1)))
            if cartao.group(1) != "a":
                continue

            atributos = cartao.group(2)
            href = re.search(r'href="([^"]+)"', atributos)
            rel = re.search(r'rel="([^"]+)"', atributos)
            href = href.group(1).replace("&amp;", "&") if href else ""
            rel = rel.group(1) if rel else ""

            e_ficha = href in fichas
            e_piso_pago = href in pisos_pagos
            e_piso_cru = href in pisos_crus
            e_piso = e_piso_pago or e_piso_cru
            confere(e_ficha or e_piso,
                    "%s cartao %d: aponta para %r, que nao e ficha nem piso de nenhum item do banco"
                    % (prefixo, i, href[:80]))

            # A marcacao do link tem de dizer o que ele E. `sponsored` e do que
            # paga; a busca crua nao paga, e marca-la como paga seria declarar em
            # formato de maquina o contrario do que a pagina diz em texto.
            # A AFIRMACAO E DE IGUALDADE, E ISSO NAO E ESTILO. Escrita como dois
            # ramos (`if paga: exige sponsored / elif cru: exige nofollow`), ela
            # deixa de medir o cartao que nao cai em ramo nenhum — e foi assim
            # que a mutacao "o piso encurtado deixa de exigir sponsored"
            # sobreviveu em 23/09/2026: tirado o `e_piso_pago` do primeiro ramo,
            # os cartoes do piso simplesmente pararam de ser conferidos, em
            # silencio. Com `==`, tirar um termo nao cala a regua: faz a regua
            # discordar da tela.
            paga = e_ficha or e_piso_pago
            confere(("sponsored" in rel) == paga,
                    "%s cartao %d: rel=%r, e este link %s comissao"
                    % (prefixo, i, rel, "PAGA" if paga else "NAO paga"))
            confere(("nofollow" in rel) == (not paga),
                    "%s cartao %d: rel=%r, e este link %s comissao"
                    % (prefixo, i, rel, "PAGA" if paga else "NAO paga"))

            confere('target="_blank"' in atributos and "noopener" in rel,
                    "%s cartao %d: link de loja sem aba nova ou sem noopener" % (prefixo, i))

            # A linha discreta do piso so existe no cartao que TEM ficha (25.2),
            # e ela fica FORA da ancora: ancora dentro de ancora nao e valido.
            piso_do_item = re.search(r'<a class="aqm-%s-vt-piso" href="([^"]+)"' % prefixo, item)
            if e_ficha:
                confere(piso_do_item is not None,
                        "%s cartao %d: tem ficha e nao carrega o piso embaixo (25.2)" % (prefixo, i))
                # E O ENDERECO DELA TAMBEM E CONFERIDO. Ate 23/09/2026 a regua
                # so perguntava se a linha EXISTIA, e nunca para onde ela
                # levava: uma URL inventada ali passava batida, enquanto a
                # mesma URL inventada no botao do cartao era pega. Metade do
                # piso media, metade nao.
                if piso_do_item is not None:
                    destino = piso_do_item.group(1).replace("&amp;", "&")
                    confere(destino in pisos_pagos or destino in pisos_crus,
                            "%s cartao %d: a linha do piso aponta para %r, que nao e piso "
                            "de nenhum item do banco" % (prefixo, i, destino[:80]))
            else:
                confere(piso_do_item is None,
                        "%s cartao %d: ja E o piso e ainda repete a linha do piso" % (prefixo, i))

        # ------------------------------------------------------------------
        # A TABELA PRE-RENDERIZADA, que e o que chega a quem nao tem JavaScript
        # (portao 22.8) e ao robo de busca. Ate 23/09/2026 esta regua media SO
        # os cartoes da vitrine, e a tabela — que sai da MESMA
        # `aquametria_cN_compra()` — nao era olhada por ninguem. O buraco so
        # apareceu quando a coleta pela Open API deu ficha aos itens do topo:
        # a mutacao "A URL INVENTADA" deixou de acertar um cartao e passou a
        # acertar so a tabela, e a bateria ficou verde com uma URL inventada
        # servida na pagina. Meia regua nao e regua.
        # ------------------------------------------------------------------
        for destino in re.findall(r'<a class="aqm-%s-prod" href="([^"]+)"' % prefixo, corpo):
            destino = destino.replace("&amp;", "&")
            confere(destino in fichas or destino in pisos_pagos or destino in pisos_crus,
                    "%s: a tabela servida aponta para %r, que nao e ficha nem piso de "
                    "nenhum item do banco" % (prefixo, destino[:80]))


def main():
    esquema = carregar("dados/esquema-produtos.json")
    escada = esquema["afiliado"].get("escada_de_compra")

    print("== a escada da 25.1 esta declarada no esquema ==")
    confere(escada is not None, "o esquema nao declara 'escada_de_compra'")
    if escada is None:
        print("\n%d afirmacao(oes), %d falha(s)" % (afirmacoes[0], len(falhas)))
        return 1

    declarados = {d["degrau"]: d.get("nome") for d in escada.get("degraus", [])}
    for degrau, nome in DEGRAUS_DA_251.items():
        confere(declarados.get(degrau) == nome,
                "degrau %d deveria se chamar '%s' e veio %r" % (degrau, nome, declarados.get(degrau)))
    confere(len(declarados) == 4, "a escada tem %d degraus; a 25.1 tem 4" % len(declarados))
    confere(str(escada.get("base_da_busca", "")).startswith("https://shopee.com.br/search?keyword="),
            "base_da_busca nao e a pagina de busca da Shopee: %r" % escada.get("base_da_busca"))

    termos = escada.get("termo_de_contexto_por_entidade", {})
    for entidade in ARQUIVOS:
        termo = termos.get(entidade)
        confere(preenchido(termo),
                "entidade '%s' sem termo de contexto: a busca dela sairia so por marca" % entidade)

    print("\n== toda busca carrega marca E contexto (25.3) ==")
    base = escada["base_da_busca"]
    conta = {"com_ficha": 0, "com_piso": 0, "sem_piso": 0, "sem_degrau": 0, "sem_url_produto": 0}
    for entidade, caminho in ARQUIVOS.items():
        termo = (termos.get(entidade) or "").lower()
        for p in carregar(caminho).get("produtos", []):
            a = p.get("afiliado") or {}
            pid = p.get("id")

            busca = a.get("url_busca_produto")
            confere(preenchido(busca), "%s sem url_busca_produto: a 25.2 nao deixa item sem piso "
                                       "escolhido" % pid)
            if preenchido(busca):
                confere(str(busca).startswith(base), "%s: a busca nao sai da base declarada" % pid)
                chave = unquote(str(busca)[len(base):]).lower()
                # A MARCA SO E COBRADA DE QUEM TEM MARCA, e isto foi medido e
                # nao suposto: a primeira versao desta regua reprovou DOIS
                # registros CERTOS — rs-50-50w e aquarios-do-rio-led-60cm, os
                # dois com marca null porque sao produto sem marca declarada. A
                # 25.3 fala de CONTEXTO, nao de marca: o que ela proibe e buscar
                # so por marca, e produto sem marca nenhuma nao cai nessa
                # armadilha. O contexto, esse, e cobrado de todos.
                marca = str(p.get("marca") or "").strip().lower()
                if marca:
                    confere(marca in chave, "%s: a busca nao carrega a marca declarada" % pid)
                confere(termo and any(t in chave for t in termo.split()),
                        "%s: a busca nao carrega o contexto da entidade" % pid)
                confere(len(chave.replace(termo, "").strip()) >= 3,
                        "%s: fora o contexto, a busca nao identifica nada" % pid)

            # O par da 25.4-b, medido nos dois sentidos.
            if preenchido(a.get("url")):
                conta["com_ficha"] += 1
                confere(preenchido(a.get("url_produto")) or preenchido(a.get("motivo_sem_url_produto")),
                        "%s: link de afiliado sem url crua e sem o motivo de nao ter" % pid)
                if a.get("degrau") is None:
                    conta["sem_degrau"] += 1
                if not preenchido(a.get("url_produto")):
                    conta["sem_url_produto"] += 1
            if preenchido(a.get("url_busca")):
                conta["com_piso"] += 1
                confere(preenchido(a.get("url_busca_produto")),
                        "%s: tem piso e nao guarda a busca crua (25.4-b)" % pid)
            else:
                conta["sem_piso"] += 1
                confere(preenchido(a.get("motivo_sem_url_busca")),
                        "%s: sem piso e sem dizer o que trava o piso" % pid)

    print("\n== os numeros do relatorio sao contados, nao digitados ==")
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "ferramentas/validar-produtos.py")],
                       capture_output=True, text=True, cwd=RAIZ)
    saida = r.stdout + r.stderr
    lidos = {}
    for rotulo, chave in (("com ficha \\(url\\)", "com_ficha"), ("com piso \\(url_busca\\)", "com_piso"),
                          ("itens_sem_piso", "sem_piso"), ("links_sem_degrau", "sem_degrau"),
                          ("links sem url crua", "sem_url_produto")):
        m = re.search(rotulo + r"\s+(\d+) de \d+", saida)
        lidos[chave] = int(m.group(1)) if m else None
    for chave, esperado in sorted(conta.items()):
        confere(lidos.get(chave) == esperado,
                "o relatorio diz %r em '%s' e a contagem propria da %d"
                % (lidos.get(chave), chave, esperado))

    mede_o_piso_na_tela()

    print("\n== o gerador da busca e idempotente ==")
    g = subprocess.run([sys.executable, os.path.join(RAIZ, "ferramentas/gerar-busca-de-produto.py")],
                       capture_output=True, text=True, cwd=RAIZ)
    m = re.search(r"(\d+) a gravar", g.stdout)
    confere(m is not None and m.group(1) == "0",
            "rodar o gerador de novo mexeria em %s item(ns)" % (m.group(1) if m else "?"))

    print("\n%d afirmacao(oes), %d falha(s)" % (afirmacoes[0], len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

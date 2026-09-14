#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere NO AR que nenhuma pagina da Aquametria fica sem saida de compra.

    python3 ferramentas/conferir-escada-no-ar.py

POR QUE ELE EXISTE, ao lado de ferramentas/teste-escada-compra.py. Aquele portao
mede o que o render de bancada produz; este mede o que o SITE serve. A secao 4 do
ARQUIPELAGO.md existe inteira por causa da distancia entre as duas coisas — o
repositorio na revisao 17 e o site na 11, tres blocos commitados e fora do ar,
sem ninguem perceber porque a verificacao olhava o repositorio. Bancada verde nao
e entrega; entrega e a pagina no ar.

O QUE ELE MEDE, e sao quatro afirmacoes por calculadora:

  1. a pagina responde 200;
  2. o CORPO servido nao contem "link de loja em breve", a frase que a secao 7
     passou a proibir em 14/09/2026;
  3. todo cartao da vitrine servida e uma ANCORA — nenhum produto que chega ao
     leitor fica sem saida de compra (25.2);
  4. o href de cada cartao sai do BANCO deste repositorio: ou e a ficha de
     afiliado de um item, ou e a busca crua dele. URL que nao esta em nenhuma
     das duas listas foi inventada pelo snippet.

E a marcacao acompanha o que o link E: `sponsored` para a ficha, que paga
comissao, e `nofollow` para a busca crua, que nao paga. Marcar a busca como paga
seria declarar em formato de maquina o contrario do que a pagina diz em texto.

MEDIDO NO CORPO, NUNCA NO HTML INTEIRO. A casca do tema carrega <style> e
<script> com dezenas de ocorrencias legitimas de texto e de classe, e procurar
uma frase na pagina inteira e o mesmo erro de contar &#038; fora do <script>
(secao 8). Aqui o <style> e o <script> saem antes de qualquer conta.

CACHE: a secao 4 avisa que o raw guarda ~5 min e o WebFetch 15 min por URL. Por
isso toda URL leva um ?v= com hora e minuto.
"""
import datetime
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOMINIO = "https://aquametria.com.br"
PAGINAS = {
    "c3": "calculadora-de-vazao-do-filtro",
    "c5": "calculadora-de-potencia-do-aquecedor",
    "c12": "calculadora-de-midia-filtrante",
    "c15": "calculadora-de-iluminacao",
}
ARQUIVOS = (
    "dados/produtos-filtro.json",
    "dados/produtos-aquecedor.json",
    "dados/produtos-iluminacao.json",
    "dados/produtos-midia.json",
)
PROIBIDA = "link de loja em breve"

falhas = []
afirmacoes = [0]


def confere(condicao, texto):
    afirmacoes[0] += 1
    if not condicao:
        falhas.append(texto)
        print("  FALHA %s" % texto)


def preenchido(v):
    return v is not None and v != "" and v != []


def saidas_do_banco():
    """As duas listas de URL que o banco autoriza a aparecer numa pagina.

    Elas nao se misturam de proposito: a FICHA paga comissao e a busca CRUA nao,
    e e essa diferenca que decide o `rel` e o selo do cartao.
    """
    fichas, pisos = set(), set()
    for caminho in ARQUIVOS:
        with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
            for p in json.load(f).get("produtos", []):
                a = p.get("afiliado") or {}
                if preenchido(a.get("url")):
                    fichas.add(a["url"])
                if preenchido(a.get("url_busca")):
                    fichas.add(a["url_busca"])
                elif preenchido(a.get("url_busca_produto")):
                    pisos.add(a["url_busca_produto"])
    return fichas, pisos


def baixar(url):
    r = subprocess.run(["curl", "-sS", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None, None
    partes = r.stdout.rsplit("\n", 1)
    if len(partes) != 2:
        return None, None
    return partes[0], partes[1].strip()


def corpo(html):
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S)
    return re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S)


def main():
    fichas, pisos = saidas_do_banco()
    versao = datetime.datetime.utcnow().strftime("%H%M")
    print("banco: %d ficha(s) de afiliado e %d busca(s) crua(s) autorizadas na tela"
          % (len(fichas), len(pisos)))

    for prefixo, slug in sorted(PAGINAS.items()):
        url = "%s/%s/?v=%s" % (DOMINIO, slug, versao)
        print("\n== %s — %s ==" % (prefixo, slug))
        html, codigo = baixar(url)
        confere(codigo == "200", "%s: a pagina respondeu %r em vez de 200" % (prefixo, codigo))
        if html is None or codigo != "200":
            continue

        c = corpo(html)
        confere(PROIBIDA not in c,
                "%s: o corpo NO AR ainda escreve %r, proibido pela secao 7" % (prefixo, PROIBIDA))

        itens = re.findall(r'<li class="aqm-%s-vt-item[^"]*">(.*?)</li>' % prefixo, c, flags=re.S)
        confere(len(itens) > 0, "%s: a vitrine servida no ar nao tem cartao nenhum" % prefixo)

        pela_ficha = 0
        pelo_piso = 0
        for i, item in enumerate(itens, 1):
            cartao = re.search(r'<(a|div) class="aqm-%s-vt-cartao[^"]*"([^>]*)>' % prefixo, item)
            confere(cartao is not None, "%s cartao %d: nao achei o cartao no ar" % (prefixo, i))
            if cartao is None:
                continue
            confere(cartao.group(1) == "a",
                    "%s cartao %d: NO AR saiu como <%s> — cartao sem saida de compra"
                    % (prefixo, i, cartao.group(1)))
            if cartao.group(1) != "a":
                continue

            atributos = cartao.group(2)
            href = re.search(r'href="([^"]+)"', atributos)
            rel = re.search(r'rel="([^"]+)"', atributos)
            href = href.group(1).replace("&amp;", "&").replace("&#038;", "&") if href else ""
            rel = rel.group(1) if rel else ""

            e_ficha = href in fichas
            e_piso = href in pisos
            confere(e_ficha or e_piso,
                    "%s cartao %d: aponta para %r, que nao e ficha nem piso de item nenhum do banco"
                    % (prefixo, i, href[:90]))
            if e_ficha:
                pela_ficha += 1
                confere("sponsored" in rel,
                        "%s cartao %d: ficha de afiliado sem 'sponsored' (%r)" % (prefixo, i, rel))
            elif e_piso:
                pelo_piso += 1
                confere("nofollow" in rel and "sponsored" not in rel,
                        "%s cartao %d: busca CRUA marcada como paga (%r)" % (prefixo, i, rel))
            confere('target="_blank"' in atributos and "noopener" in rel,
                    "%s cartao %d: sem aba nova ou sem noopener" % (prefixo, i))

        print("  %d cartao(oes): %d pela ficha, %d pelo piso da 25.2, 0 sem saida"
              % (len(itens), pela_ficha, pelo_piso))

    print("\n%d afirmacao(oes), %d falha(s)" % (afirmacoes[0], len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

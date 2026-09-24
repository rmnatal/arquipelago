#!/usr/bin/env python3
"""BANCADA: sem rede — o titulo de cada pagina do eixo /peixes/ mora em DOIS
arquivos, e este portao cobra que os dois digam a mesma coisa.

    python3 ferramentas/teste-titulos-das-duas-fontes.py

AS DUAS COPIAS, e cada uma serve uma superficie diferente da MESMA pagina:

  * `snippets/aquametria-peixes.php`, no `aquametria_peixes_registro()` — e daqui
    que sai o `post_title`, logo o `<h1>` e a primeira metade do `<title>`.
  * `dados/metas-seo.json`, em `paginas_do_eixo_peixes` — e daqui que sai o
    `og:title` e o `twitter:title`, pelo mapa gerado dentro do seo-tecnico.

NINGUEM MEDIA ISSO. Medido em 24/09/2026, antes de escrever este arquivo: as 38
paginas do eixo concordavam nas duas fontes — nenhuma divergencia, ainda. O
portao nasce no dia em que a primeira mudanca de titulo do eixo foi feita (a
Proposta 1 da leitura semanal de 23/09, em `/peixes/ciclideos-anoes/`), porque e
exatamente esse o momento em que a segunda copia fica para tras: quem muda o
`titulo` para consertar a posicao na busca esta pensando no `<title>`, e o
`og:title` mora noutro arquivo, noutra pasta, sem nada que avise.

E A TERCEIRA VEZ QUE ESTA ILHA PAGA A MESMA DOENCA, e as duas primeiras ja tem
portao: o favicon mantido em dois lugares (casca, secao 2b) e a meta description
(seo-tecnico, que por isso e GERADA e nao escrita). "Texto mantido em dois
lugares diverge em silencio" e frase do cabecalho daquele snippet.

O REGISTRO E LIDO EM TEXTO, NAO PERGUNTANDO A FUNCAO DO SNIPPET — a mesma escolha
que `teste-peixes.py` declara e pelo mesmo motivo: a afirmacao e que os dois
ARQUIVOS concordam, e carregar o PHP para perguntar faria as duas metades errarem
juntas se o erro estivesse na leitura.

O TETO DE 65 TAMBEM E COBRADO AQUI, e ele tinha regua so no `teste-voz.mjs`, que
precisa de Chromium e de site no ar. O `<title>` servido e o titulo mais os 13
caracteres de ` – Aquametria` que o WordPress acrescenta; 65 e o que o Google
mostra antes de cortar. Cobrar isto na bancada, sem rede, e o que impede um
titulo estourado de sair do repositorio.
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAUDA = " – Aquametria"   # o que o WordPress acrescenta: 13 caracteres
TETO = 65                 # o mesmo TITULO_MAXIMO do teste-voz.mjs

contadas = [0]
falhas = []


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def titulos_do_registro():
    """{slug: titulo} lido do TEXTO do snippet, entrada por entrada.

    Cada entrada do registro abre com dois tabs e `'slug' => array(`. O `titulo`
    de uma entrada e o primeiro que aparece antes da entrada seguinte — o que
    evita depender da indentacao dos arrays internos, que muda de campo para
    campo.
    """
    caminho = os.path.join(RAIZ, "snippets", "aquametria-peixes.php")
    src = open(caminho, encoding="utf-8").read()
    corte = src.index("function aquametria_peixes_registro()")
    corpo = src[corte:]
    abre = [(m.start(), m.group(1))
            for m in re.finditer(r"\n\t\t'([a-z0-9-]+)' => array\(", corpo)]
    fora = {}
    for i, (pos, slug) in enumerate(abre):
        fim = abre[i + 1][0] if i + 1 < len(abre) else len(corpo)
        m = re.search(r"'titulo'\s*=>\s*'((?:[^'\\]|\\.)*)'", corpo[pos:fim])
        if m:
            fora[slug] = m.group(1).replace("\\'", "'").replace("\\\\", "\\")
    return fora


def titulos_do_json():
    caminho = os.path.join(RAIZ, "dados", "metas-seo.json")
    j = json.load(open(caminho, encoding="utf-8"))
    return {s: d["titulo"] for s, d in j["paginas_do_eixo_peixes"].items()}


def main():
    reg = titulos_do_registro()
    js = titulos_do_json()

    print("A LEITURA ACHOU AS DUAS FONTES")
    # Sem isto o portao inteiro passaria por vacuidade se a leitura em texto
    # parasse de casar — dois dicionarios vazios concordam.
    ok("o registro do snippet tem titulo para mais de 30 paginas", len(reg) > 30,
       "%d" % len(reg))
    ok("o metas-seo.json tem titulo para mais de 30 paginas do eixo", len(js) > 30,
       "%d" % len(js))
    ok("as duas fontes tem o MESMO numero de paginas", len(reg) == len(js),
       "registro %d, json %d" % (len(reg), len(js)))

    print("\nAS DUAS DIRECOES DA CONCORDANCIA")
    for slug in sorted(reg):
        ok("%s esta nas duas fontes" % slug, slug in js,
           "falta no metas-seo.json" if slug not in js else "")
    for slug in sorted(js):
        ok("%s do json existe no registro" % slug, slug in reg,
           "falta no registro do snippet" if slug not in reg else "")

    print("\nO TITULO E O MESMO NAS DUAS")
    for slug in sorted(set(reg) & set(js)):
        ok("%s: registro e json dizem o mesmo titulo" % slug, reg[slug] == js[slug],
           "registro %r vs json %r" % (reg[slug], js[slug]) if reg[slug] != js[slug] else "")

    print("\nO <title> SERVIDO CABE EM %d CARACTERES" % TETO)
    for slug in sorted(reg):
        servido = reg[slug] + CAUDA
        ok("%s: %d caracteres" % (slug, len(servido)), len(servido) <= TETO,
           servido if len(servido) > TETO else "")

    print("\nA PROPOSTA 1 DA LEITURA SEMANAL DE 23/09, cobrada por nome")
    # O criterio de pronto que a Sentinela escreveu: as duas formas, singular e
    # plural, no titulo E na descricao da categoria. Fica aqui, e nao numa
    # medicao solta, porque criterio de despacho que ninguem transforma em
    # portao volta a ser esquecido na leva seguinte.
    alvo = "ciclideos-anoes"
    if alvo not in reg:
        ok("a categoria %s existe no registro" % alvo, False)
    else:
        t = reg[alvo].lower()
        ok("o titulo de %s traz a forma SINGULAR 'ciclídeo anão'" % alvo,
           "ciclídeo anão" in t, reg[alvo])
        ok("o titulo de %s traz a forma PLURAL 'ciclídeos anões'" % alvo,
           "ciclídeos anões" in t, reg[alvo])
        caminho = os.path.join(RAIZ, "dados", "metas-seo.json")
        d = json.load(open(caminho, encoding="utf-8"))
        desc = d["paginas_do_eixo_peixes"][alvo]["meta_descricao"]
        ok("a meta description de %s traz a forma SINGULAR" % alvo,
           "ciclídeo anão" in desc.lower(), desc)
        ok("a meta description de %s traz a forma PLURAL" % alvo,
           "ciclídeos anões" in desc.lower(), desc)
        # A consulta declarada e o que a pagina diz que persegue. Ter a consulta
        # DENTRO do titulo e o que faltava, e faltou nove dias sem ninguem ver.
        src = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"),
                   encoding="utf-8").read()
        bloco = src[src.index("'%s' => array(" % alvo):]
        consulta = re.search(r"'consulta'\s*=>\s*'((?:[^'\\]|\\.)*)'", bloco)
        ok("o titulo de %s contem a consulta que o registro declara" % alvo,
           consulta is not None and consulta.group(1).lower() in t,
           "consulta: %r" % (consulta.group(1) if consulta else None))

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

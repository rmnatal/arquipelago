#!/usr/bin/env python3
"""O PORTAO DO EIXO /peixes/ — mede o que as NOVE paginas SERVEM.

    python3 ferramentas/teste-peixes.py .

COMO ESTE ARQUIVO FOI ESCRITO, e as cicatrizes da secao 8 do ARQUIPELAGO.md que
decidiram cada escolha:

  1. QUEM CONFERE ESCREVE A PROPRIA REGUA. Toda aritmetica aqui e recomputada do
     `dados/especies-agua-doce.json`, do zero. Nada e importado do snippet nem do
     catalogo gerado: se as duas metades chamassem a mesma funcao, trocar 1,5 por
     1,6 faria as duas errarem juntas e o teste continuaria verde.

  2. O MAPA PAGINA -> ESPECIE ESTA ESCRITO AQUI, a mao. Ler o mapa do snippet e
     perguntar ao snippet qual e a resposta certa — e o unico erro que isso nunca
     pegaria e o que vai acontecer de verdade, porque a proxima leva vai copiar
     este registro: a ficha que ficasse apontando para a especie anterior iria
     AO AR funcionando, com a conta certa da especie errada.

  3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. O <head>, o JSON-LD e
     o rodape saem fora antes de qualquer contagem de texto, senao o numero e
     "encontrado" dentro do proprio schema — foi assim que a Robometria passou um
     teste com resposta inventada.

  4. UMA PAGINA POR PROCESSO. `render-pagina-completa.php` explica por que: o
     `static` da marca, do estilo e da trilha sai na primeira e some nas
     seguintes, e a bancada mede a metade de tudo depois da primeira pagina.

  5. A GRADE PISA NA BORDA. O degrau do cardume minimo, o menor e o maior degrau
     da tabela, as tres alturas, a especie com conflito nos DOIS campos que
     entram em conta (mato-grosso) e a especie agressiva estao todos medidos —
     varredura que so passa pelo caso do meio e amostra com nome de varredura.
"""

import decimal
import html
import json
import math
import os
import re
import subprocess
import sys

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
RENDER = os.path.join(RAIZ, "ferramentas", "render-pagina-completa.php")

# A regua das duas fontes brasileiras de lotacao, escrita AQUI (constante 2 e 3
# de dados/constantes-calculadoras.json, colhidas em 04/09/2026).
CLASSICA = 1.0
MEIO = 1.5
CONSERVADORA = 4.0
ALTURAS = (30, 35, 40)
DEGRAUS_EXTRA = (6, 8, 10, 12, 15, 20)

# Decisao 2 do cabecalho: o mapa esta aqui, nao no snippet.
FICHAS = {
    "quantos-litros-para-tetra-neon": "paracheirodon-innesi",
    "quantos-litros-para-tetra-cardinal": "paracheirodon-axelrodi",
    "quantos-litros-para-mato-grosso": "hyphessobrycon-eques",
    # leva 2, 12/09/2026 — as quatro que fecham a categoria
    "quantos-litros-para-tetra-ember": "hyphessobrycon-amandae",
    "quantos-litros-para-tetra-brilhante": "hemigrammus-erythrozonus",
    "quantos-litros-para-rodostomo": "hemigrammus-rhodostomus",
    "quantos-litros-para-tetra-negro": "gymnocorymbus-ternetzi",
}

# As especies do catalogo que NAO declaram o fundo do aquario: a fonte publica o
# comprimento minimo e para ai. Escrito aqui a mao pelo mesmo motivo do mapa de
# cima — se o teste perguntasse ao banco quem tem base nula, ele mediria o banco
# contra ele mesmo e a afirmacao "a pagina diz COMPRIMENTO quando nao ha fundo"
# passaria verde com o banco inteiro nulo.
SEM_FUNDO_DECLARADO = {"hemigrammus-rhodostomus"}
CATEGORIA = "tetras"
SECAO = "peixes"
PAGINAS = [SECAO, CATEGORIA] + list(FICHAS)

# Os tetras que a categoria tem de listar, escritos aqui pelo mesmo motivo.
TETRAS = [
    "paracheirodon-innesi",
    "paracheirodon-axelrodi",
    "hyphessobrycon-amandae",
    "hyphessobrycon-eques",
    "hemigrammus-erythrozonus",
    "hemigrammus-rhodostomus",
    "gymnocorymbus-ternetzi",
]

CORPO_MINIMO = 1500      # secao 8: pagina fina e reprovacao
MAX_PROVA = 2            # blocos aqm-prova por corpo (regra do portao da voz)

falhas = []
contadas = [0]


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


# ---------------------------------------------------------------------------
# A regua: recomputada do banco, do zero
# ---------------------------------------------------------------------------

def carregar_banco():
    with open(BANCO, encoding="utf-8") as f:
        return {e["id"]: e for e in json.load(f)["especies"]}


def faixa_do_campo(e, campo):
    """[min, max] do campo, juntando o valor e os extremos do conflito declarado."""
    valores = [float(e[campo])] if e.get(campo) is not None else []
    for c in e.get("conflitos", []):
        if c.get("campo") != campo:
            continue
        for v in c.get("valores", []):
            if isinstance(v.get("valor"), (int, float)):
                valores.append(float(v["valor"]))
    return [min(valores), max(valores)] if valores else [None, None]


def degraus(e):
    minimo = int(e["cardume_minimo"]) if e.get("cardume_minimo") else 1
    return sorted({minimo} | {n for n in DEGRAUS_EXTRA if n > minimo})


def meio_para_cima(v, casas):
    """Arredonda com o 5 subindo, que e o que o leitor brasileiro espera.

    POR QUE ISTO E UMA FUNCAO E NAO UM '%.1f' (achado da leva 2, 12/09/2026).
    O Python e o C arredondam o meio para o PAR — '%.1f' % 47.25 devolve '47,2'
    —, e o number_format do PHP arredonda o meio para CIMA, devolvendo '47,3'.
    Durante a leva 1 as duas reguas concordaram em 295 afirmacoes, e concordaram
    por sorte: nenhum numero daquelas tres fichas caiu exatamente no meio. A
    leva 2 pos tres deles na tela de uma vez — 45 x 30 x 35 / 1000 = 47,25 L no
    tetra ember, 15 x 3,3 x 1,5 = 74,25 L no tetra-brilhante e 5 x 7,5 x 1,5 =
    56,25 L no tetra-negro. E a cicatriz da secao 8 do ARQUIPELAGO.md em estado
    puro: grade que nao pisa na borda nao separa uma regra da outra.

    QUEM ESTA CERTO E A PAGINA, e isso e decisao, nao empate desfeito para o
    teste ficar verde: "arredonda para cima no 5" e o que se ensina na escola
    brasileira, e o meio-para-o-par e um artefato do C que ninguem escolheu.
    """
    d = decimal.Decimal(repr(float(v)))
    passo = decimal.Decimal(1).scaleb(-casas)
    return float(d.quantize(passo, rounding=decimal.ROUND_HALF_UP))


def numero_br(v, casas=1):
    """O mesmo formato que a pagina serve: virgula decimal, sem zero inutil."""
    if v is None:
        return "—"
    v = float(v)
    inteiro = meio_para_cima(v, 0)
    if abs(v - inteiro) < 0.05:
        return "{:,.0f}".format(inteiro).replace(",", ".")
    return ("%.*f" % (casas, meio_para_cima(v, casas))).replace(".", ",")


# ---------------------------------------------------------------------------
# A bancada
# ---------------------------------------------------------------------------

def servir(slug):
    saida = subprocess.run(
        ["php", RENDER, RAIZ, slug],
        capture_output=True, text=True, check=True,
    ).stdout
    if "PHP Parse error" in saida or "PHP Fatal error" in saida:
        raise SystemExit("ERRO: o render de %s falhou:\n%s" % (slug, saida[:800]))
    return saida


def cabeca(pagina):
    m = re.search(r"<head[^>]*>(.*?)</head>", pagina, re.S)
    return m.group(1) if m else ""


def corpo(pagina):
    """O corpo SEM head, sem script, sem style e sem rodape — decisao 3.

    `<body[^>]*>` e nao `<body>`: a bancada serve a tag pelada e o WordPress
    serve `<body class="wp-singular page page-child ...">`. Localizador que
    exigia o fecho logo depois do nome achava o corpo na bancada e devolvia
    VAZIO no ar — e corpo vazio faz toda afirmacao sobre o texto reprovar de
    uma vez, que foi como esta conferencia abriu em 12/09/2026.
    """
    m = re.search(r"<body[^>]*>(.*)</body>", pagina, re.S)
    b = m.group(1) if m else ""
    b = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", b, flags=re.S)
    b = re.sub(r'<footer class="aqm-rodape".*?</footer>', "", b, flags=re.S)
    return b


def texto(h):
    t = re.sub(r"<[^>]+>", " ", h)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def jsonlds(pagina):
    nos = []
    # O atributo nao e opcional no localizador: a trilha da casca imprime o
    # script COM id, e um regex que exigisse ">" logo depois do tipo deixaria o
    # BreadcrumbList de fora e a pagina pareceria sem trilha em schema.
    for bruto in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', pagina, re.S):
        nos.append(json.loads(bruto))
    return nos


def tabelas(c):
    """As tabelas do corpo: legenda, cabecalho e as celulas de cada linha.

    POR QUE CELULA, E NAO "o numero esta na pagina": duas mutacoes deliberadas
    PASSARAM na primeira rodada deste portao, e as duas pela mesma razao — o
    numero errado que elas produziam era um numero que a pagina servia em OUTRO
    lugar. Trocar floor por ceil na conta de quantos peixes cabem devolvia 29
    onde cabem 28, e o teste achou o "28" dentro de "20 a 28 °C", na tabela de
    temperatura. E a mesma familia do "conte &#038; dentro do <script>, nunca na
    pagina inteira": afirmacao sobre um numero se mede na CELULA em que ele mora.
    """
    achadas = []
    for bruto in re.findall(r"<table[^>]*>(.*?)</table>", c, re.S):
        legenda = re.search(r"<caption[^>]*>(.*?)</caption>", bruto, re.S)
        cabecalho = [texto(x) for x in re.findall(r"<th[^>]*scope=\"col\"[^>]*>(.*?)</th>", bruto, re.S)]
        corpo_tabela = re.search(r"<tbody>(.*?)</tbody>", bruto, re.S)
        linhas = []
        if corpo_tabela:
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", corpo_tabela.group(1), re.S):
                linhas.append([texto(x) for x in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)])
        achadas.append({
            "legenda": texto(legenda.group(1)) if legenda else "",
            "cabecalho": cabecalho,
            "linhas": linhas,
        })
    return achadas


def tabela_com(c, pedaco):
    for t_ in tabelas(c):
        if pedaco in t_["legenda"]:
            return t_
    return None


def trilha(pagina):
    """Os degraus da trilha visivel: (rotulo, tem_link)."""
    m = re.search(r'<nav class="aqm-trilha".*?</nav>', pagina, re.S)
    if not m:
        return []
    degraus_html = re.findall(r"<li>(.*?)</li>", m.group(0), re.S)
    return [(texto(d), "<a href=" in d) for d in degraus_html]


# ---------------------------------------------------------------------------
# As afirmacoes
# ---------------------------------------------------------------------------

def medir_ficha(slug, ident, banco):
    e = banco[ident]
    pagina = servir(slug)
    c = corpo(pagina)
    t = texto(c)

    print("\n### ficha %s (%s)" % (slug, ident))

    ok("%s: corpo tem tamanho de pagina" % slug, len(t) >= CORPO_MINIMO, "%d caracteres" % len(t))
    ok("%s: nenhuma entidade &#038; dentro de <script>" % slug,
       all("&#038;" not in b for b in re.findall(r"<script[^>]*>(.*?)</script>", pagina, re.S)))
    ok("%s: no maximo %d blocos de prova no corpo" % (slug, MAX_PROVA),
       c.count('class="aqm-prova"') <= MAX_PROVA, "%d blocos" % c.count('class="aqm-prova"'))

    # --- o nome popular da especie certa, e nunca o de outra ficha
    nome = e["nomes_populares_br"][0]
    ok("%s: serve o nome popular do banco (%s)" % (slug, nome), nome in t)
    for outro_slug, outro_id in FICHAS.items():
        if outro_slug == slug:
            continue
        outro_nome = banco[outro_id]["nomes_populares_br"][0]
        if outro_nome in nome or nome in outro_nome:
            continue
        # o nome da irma pode aparecer no cluster e na tabela de vizinhos, mas
        # NUNCA na resposta direta: e ali que a ficha copiada erraria a especie
        direta = re.search(r'<div class="aqm-px-direta">(.*?)</div>', c, re.S)
        ok("%s: a resposta direta nao fala do %s" % (slug, outro_nome),
           direta is not None and outro_nome not in texto(direta.group(1)))

    # --- a frente minima: o EXTREMO MAIOR do conflito, sempre
    frente = faixa_do_campo(e, "comprimento_minimo_aquario_cm")
    ok("%s: a resposta direta traz a frente minima de %s cm" % (slug, numero_br(frente[1])),
       ("%s cm de frente" % numero_br(frente[1])) in t)
    if frente[0] != frente[1]:
        ok("%s: o extremo menor (%s cm) tambem esta publicado" % (slug, numero_br(frente[0])),
           numero_br(frente[0]) in t)

    # --- a tabela de lotacao, CELULA POR CELULA, com a borda do cardume minimo
    porte = faixa_do_campo(e, "porte_adulto_cm")
    if porte[0] != porte[1]:
        ok("%s: os dois extremos do porte (%s e %s cm) estao publicados"
           % (slug, numero_br(porte[0]), numero_br(porte[1])),
           ("%s a %s cm" % (numero_br(porte[0]), numero_br(porte[1]))) in t)
    tab = tabela_com(c, "pelas duas réguas brasileiras")
    ok("%s: serve a tabela de lotacao pre-renderizada" % slug, tab is not None)
    if tab:
        ok("%s: a tabela de lotacao tem as cinco colunas" % slug, len(tab["cabecalho"]) == 5,
           str(tab["cabecalho"]))
        ok("%s: a tabela de lotacao tem %d linhas" % (slug, len(degraus(e))),
           len(tab["linhas"]) == len(degraus(e)), "%d linhas" % len(tab["linhas"]))
        for n, linha in zip(degraus(e), tab["linhas"]):
            soma = n * porte[1]
            esperado = [
                "%s cm" % numero_br(soma),
                "%s L" % numero_br(soma * CLASSICA),
                "%s L" % numero_br(soma * MEIO),
                "%s L" % numero_br(soma * CONSERVADORA),
            ]
            ok("%s: a linha de %d exemplares diz %s" % (slug, n, " | ".join(esperado)),
               linha[1:] == esperado, " | ".join(linha[1:]))
            ok("%s: a linha de %d exemplares e rotulada pelo numero" % (slug, n),
               linha[0].startswith(str(n)), linha[0])

    # --- BASE nao e FRENTE: a frase tem o escopo do que a fonte declarou
    #
    # A regua do lado do teste e o conjunto SEM_FUNDO_DECLARADO, escrito a mao no
    # topo deste arquivo. Perguntar ao banco quem tem base nula faria as duas
    # metades errarem juntas: com o banco inteiro nulo a afirmacao passaria.
    sem_fundo = ident in SEM_FUNDO_DECLARADO
    ok("%s: o banco concorda com a lista escrita a mao (fundo declarado: %s)"
       % (slug, "nao" if sem_fundo else "sim"),
       sem_fundo == ((e.get("base_minima_cm") or {}).get("largura") in (None, "")))
    if sem_fundo:
        ok("%s: a frase mestra diz COMPRIMENTO, nunca BASE" % slug,
           "declara o COMPRIMENTO do aquário" in t and "declara a BASE" not in t)
        ok("%s: declara a ausencia do fundo em vez de encolher calada" % slug,
           'class="aqm-px-sem-fundo"' in c and "não há largura declarada por ninguém" in t)
        ok("%s: e diz quais tabelas nao saem por causa disso" % slug,
           "não sai a tabela de litros por altura" in t)
        ok("%s: a fonte e atribuida ao comprimento, nao a base" % slug,
           "Quem declara esse comprimento é o" in t and "Quem declara essa base é o" not in t)
    else:
        ok("%s: a frase mestra diz BASE, porque a fonte declarou os dois lados" % slug,
           "declara a BASE" in t and "declara o COMPRIMENTO do aquário" not in t)
        ok("%s: nao declara ausencia de fundo que nao existe" % slug,
           'class="aqm-px-sem-fundo"' not in c)

    # --- o volume por altura, e o inverso (quantos cabem)
    largura = (e.get("base_minima_cm") or {}).get("largura")
    if largura:
        tab = tabela_com(c, "em três alturas de aquário")
        ok("%s: serve a tabela do aquario minimo em tres alturas" % slug, tab is not None)
        if tab:
            ok("%s: a tabela de alturas tem %d linhas" % (slug, len(ALTURAS)),
               len(tab["linhas"]) == len(ALTURAS), "%d linhas" % len(tab["linhas"]))
            for a, linha in zip(ALTURAS, tab["linhas"]):
                v = frente[1] * float(largura) * a / 1000.0
                esperado = [
                    "%s cm" % numero_br(a),
                    "%s L" % numero_br(v),
                    str(int(math.floor((v / CLASSICA) / porte[1]))),
                    str(int(math.floor((v / MEIO) / porte[1]))),
                    str(int(math.floor((v / CONSERVADORA) / porte[1]))),
                ]
                ok("%s: a linha de %d cm de altura diz %s" % (slug, a, " | ".join(esperado)),
                   linha == esperado, " | ".join(linha))

    # --- O DERIVADO PER CAPITA NAO SE MULTIPLICA. A tabela de lotacao nao tem
    #     coluna de centimetro por exemplar, e a pagina diz por escrito que
    #     multiplicar nao tem fonte. Sem esta afirmacao, a proxima versao do
    #     snippet poderia publicar "dez neons: 120 cm" sem nada reprovar.
    if e.get("cardume_minimo"):
        por_individuo = frente[1] / float(e["cardume_minimo"])
        ok("%s: publica os %s cm por exemplar como leitura" % (slug, numero_br(por_individuo)),
           ("%s cm de frente por exemplar" % numero_br(por_individuo)) in t)
        ok("%s: diz que multiplicar nao tem fonte" % slug,
           "o que nenhuma fonte sustenta" in t)
        ok("%s: a tabela de lotacao nao tem coluna de frente" % slug,
           "frente" not in texto(re.search(r"<thead>.*?</thead>", c, re.S).group(0)).lower())

    # --- procedencia na propria frase: corpo da fonte e data
    corpos = set()
    for f in e.get("fontes", []):
        ref = f.get("referencia") or ""
        nome_corpo = re.split(r"(?:\s+[—–-]\s+|:\s|,\s)", ref, maxsplit=1)[0].strip(" .:,")
        if nome_corpo and not re.search(r"\d", nome_corpo):
            corpos.add(nome_corpo)
    ok("%s: nomeia pelo menos um corpo de fonte na tela" % slug,
       any(x in t for x in corpos), ", ".join(sorted(corpos)))
    datas = {f["verificado_em"] for f in e.get("fontes", []) if f.get("verificado_em")}
    br = {"%s/%s/%s" % tuple(reversed(d.split("-"))) for d in datas}
    ok("%s: leva a data em que a fonte foi colhida" % slug, any(x in t for x in br), ", ".join(sorted(br)))

    # --- nome de campo de esquema NUNCA chega a tela
    for campo in ("comprimento_minimo_aquario_cm", "porte_adulto_cm", "cardume_minimo",
                  "base_minima_cm", "temperatura_C", "status_registro", "nomes_populares_br"):
        ok("%s: o campo %s nao aparece cru no corpo" % (slug, campo), campo not in t)
    for origem in ("base-cientifica-via-busca", "compendio-via-busca", "via-busca"):
        ok("%s: o codigo de origem %s nao aparece no corpo" % (slug, origem), origem not in t)

    # --- a divergencia sai com os dois extremos e os dois nomes
    if e.get("conflitos"):
        ok("%s: publica o bloco de divergencia" % slug, "Onde as fontes discordam" in t)
        for c_ in e["conflitos"]:
            valores = [v.get("valor") for v in c_["valores"]]
            numeros = [v for v in valores if isinstance(v, (int, float))]
            for v in numeros:
                ok("%s: o extremo %s do campo %s esta na tela" % (slug, numero_br(v), c_["campo"]),
                   numero_br(v) in t)
    else:
        ok("%s: sem conflito no banco, sem bloco de divergencia" % slug,
           "Onde as fontes discordam" not in t)

    # --- O PORTAO DE DADO DA SECAO 13: 3 itens de banco reais por pagina.
    #     Contado nomeando os registros do banco que aparecem no corpo, nunca
    #     digitado — e sem contar a propria especie duas vezes.
    citados = {i for i, outro in banco.items()
               if outro["nomes_populares_br"][0] in t or outro["nome_cientifico"] in t}
    ok("%s: cita 3 ou mais registros reais do banco" % slug, len(citados) >= 3,
       "%d registros" % len(citados))

    # --- ESPECIE AGRESSIVA NAO GANHA LISTA DE COMPANHEIRO
    if e.get("comportamento") == "agressivo":
        ok("%s: especie agressiva nao publica tabela de companheiro" % slug,
           "Quem divide a mesma faixa de temperatura" not in t)
        ok("%s: especie agressiva diz que nao publica lista, e por que" % slug,
           "não publica lista de companheiro" in t and "agressivo" in t)
    else:
        ok("%s: publica a tabela de quem divide a faixa" % slug,
           "Quem divide a mesma faixa de temperatura" in t)
        ok("%s: declara o criterio antes da lista" % slug,
           "interseção das faixas de temperatura declaradas" in t)
        # o companheiro agressivo fica fora, e nomeado
        agressivos = [i for i, o in banco.items()
                      if o.get("comportamento") == "agressivo" and i in citados]
        for i in agressivos:
            tabela = re.search(r"Quem divide a mesma faixa.*?</table>", c, re.S)
            ok("%s: %s (agressivo) nao esta na tabela de companheiro" % (slug, i),
               tabela is None or banco[i]["nomes_populares_br"][0] not in texto(tabela.group(0)))

    # --- a trilha: quatro degraus, os tres primeiros com link
    passos = trilha(pagina)
    ok("%s: a trilha tem quatro degraus" % slug, len(passos) == 4, str([p[0] for p in passos]))
    if len(passos) == 4:
        ok("%s: os tres primeiros degraus da trilha sao link" % slug,
           all(p[1] for p in passos[:3]))
        ok("%s: o ultimo degrau nao e link e e o H1" % slug, not passos[3][1])
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", pagina, re.S)
        ok("%s: o degrau atual diz o mesmo que o H1" % slug,
           h1 is not None and texto(h1.group(1)) == passos[3][0],
           "%r vs %r" % (texto(h1.group(1)) if h1 else None, passos[3][0]))

    # --- o JSON-LD: Article + FAQPage + BreadcrumbList, e nunca Product
    tipos = {no.get("@type") for no in jsonlds(pagina)}
    ok("%s: JSON-LD tem Article" % slug, "Article" in tipos, str(sorted(tipos)))
    ok("%s: JSON-LD tem FAQPage" % slug, "FAQPage" in tipos)
    ok("%s: JSON-LD tem BreadcrumbList" % slug, "BreadcrumbList" in tipos)
    ok("%s: JSON-LD NAO declara Product (especie nao e produto)" % slug, "Product" not in tipos)

    # --- a resposta do FAQ cita numero que a pagina SERVE. FAQPage que promete o
    #     que a pagina nao mostra e lixo, e lixo detectavel.
    for no in jsonlds(pagina):
        if no.get("@type") != "FAQPage":
            continue
        for q in no["mainEntity"]:
            resposta = q["acceptedAnswer"]["text"]
            for numero in re.findall(r"\d+(?:,\d+)?", resposta):
                ok("%s: o numero %s da resposta do FAQ existe no corpo" % (slug, numero),
                   numero in t, q["name"][:50])

    # --- o cluster e a mae
    ok("%s: linka a mae numa frase do corpo" % slug, 'class="aqm-px-mae"' in c)
    ok("%s: o bloco Veja tambem tem as irmas" % slug, 'class="aqm-veja"' in c)

    # A REGRA E A DO 16.4(c) — DE 2 A 4 IRMAS —, e nao "todas as irmas".
    #
    # Ate a leva 1 esta afirmacao cobrava que o cluster apontasse para TODAS as
    # outras fichas, e passava: com tres fichas, cada uma tinha duas irmas e o
    # teto de quatro nunca era tocado. A leva 2 fechou a categoria em sete, cada
    # ficha passou a ter seis irmas candidatas, e a afirmacao antiga reprovou as
    # sete paginas de uma vez — acusando de defeito exatamente o comportamento
    # que a regra manda ter. Era a afirmacao que estava errada, nao a pagina.
    #
    # E o outro lado da mesma cicatriz do arredondamento, duas telas acima:
    # enquanto o mundo nao produz a borda, "todas" e "ate quatro" sao a mesma
    # frase, e o portao fica verde nas duas versoes do codigo.
    irmas_candidatas = [o for o in FICHAS if o != slug]
    irmas_no_bloco = sorted({o for o in irmas_candidatas if ('/%s/' % o) in c})
    ok("%s: o cluster aponta para 2 a 4 irmas (16.4c), e sao %d" % (slug, len(irmas_no_bloco)),
       2 <= len(irmas_no_bloco) <= 4, ", ".join(irmas_no_bloco))
    ok("%s: nenhuma irma do cluster e estranha ao registro" % slug,
       all(o in FICHAS for o in irmas_no_bloco))
    ok("%s: a propria pagina nao aparece como irma" % slug,
       ('/%s/' % slug) not in c.split('aqm-veja', 1)[-1] if 'aqm-veja' in c else False)

    # --- espécie não é produto: nenhum link de afiliado, e a pagina diz por que
    ok("%s: nenhum link de loja (especie nao e produto)" % slug,
       'rel="sponsored"' not in pagina)
    ok("%s: explica a ausencia do link em vez de calar" % slug,
       "não tem link de loja" in t)

    # --- a consulta-alvo e a classificacao da SERP, no corpo
    ok("%s: publica a consulta-alvo" % slug, 'class="aqm-px-consulta"' in c)
    ok("%s: diz a data em que a SERP foi classificada" % slug, "12/09/2026" in t)


def medir_categoria(banco):
    slug = CATEGORIA
    pagina = servir(slug)
    c = corpo(pagina)
    t = texto(c)
    print("\n### categoria %s" % slug)

    ok("%s: corpo tem tamanho de pagina" % slug, len(t) >= CORPO_MINIMO, "%d caracteres" % len(t))
    ok("%s: nenhuma entidade &#038; dentro de <script>" % slug,
       all("&#038;" not in b for b in re.findall(r"<script[^>]*>(.*?)</script>", pagina, re.S)))

    # --- a listagem tem as sete especies e o numero CONTADO
    for ident in TETRAS:
        ok("%s: lista %s" % (slug, ident), banco[ident]["nome_cientifico"] in t)
    ok("%s: a contagem da abertura e %d" % (slug, len(TETRAS)),
       ("São %d tetras" % len(TETRAS)) in t)
    # A prestação de contas tem DUAS formas, e a segunda so existe desde a leva
    # 2: com a fila vazia, "0 estão na fila, e a próxima leva sai depois" e uma
    # promessa sobre uma leva que nao existe. O teste cobra a forma certa para o
    # estado de hoje e cobra que a OUTRA nao apareca — senao a pagina poderia
    # servir as duas frases e passar.
    na_fila = len(TETRAS) - len(FICHAS)
    if na_fila > 0:
        ok("%s: diz quantas ja tem ficha (%d) e quantas faltam (%d)" % (slug, len(FICHAS), na_fila),
           ("%d já têm a conta inteira" % len(FICHAS)) in t and ("%d estão na fila" % na_fila) in t)
        ok("%s: nao diz que a lista esta fechada" % slug, "esta lista está fechada" not in t)
    else:
        ok("%s: a categoria esta fechada e a pagina diz isso" % slug,
           ("As %d espécies da tabela têm a conta inteira" % len(TETRAS)) in t
           and "esta lista está fechada" in t)
        ok("%s: nao promete leva nenhuma com a fila vazia" % slug, "estão na fila" not in t)

    # --- o criterio da listagem, na frente dela (14.4)
    ok("%s: publica o criterio da lista" % slug, "O critério desta lista" in t)

    # --- a ordem: frente minima crescente
    linhas = re.findall(r"<tbody>(.*?)</tbody>", c, re.S)
    ok("%s: serve uma tabela" % slug, len(linhas) >= 1)
    if linhas:
        ordem = []
        for tr in re.findall(r"<tr>(.*?)</tr>", linhas[0], re.S):
            for ident in TETRAS:
                if banco[ident]["nome_cientifico"] in texto(tr):
                    ordem.append(ident)
        frentes = [faixa_do_campo(banco[i], "comprimento_minimo_aquario_cm")[1] for i in ordem]
        ok("%s: a tabela sai da menor frente para a maior" % slug,
           frentes == sorted(frentes), str(list(zip(ordem, frentes))))
        ok("%s: a tabela tem as sete linhas" % slug, len(ordem) == len(TETRAS), str(ordem))

    # --- a ancora de cada filha e o titulo dela, nunca "clique aqui"
    ancoras = re.findall(r"<a [^>]*>(.*?)</a>", c, re.S)
    ancoras = [texto(a) for a in ancoras]
    for proibida in ("clique aqui", "saiba mais", "veja mais", "leia mais"):
        ok("%s: nenhuma ancora diz %r" % (slug, proibida),
           not any(proibida in a.lower() for a in ancoras))
    for outro in FICHAS:
        ok("%s: aponta para a ficha %s" % (slug, outro), outro in c)

    # --- a trilha: tres degraus
    passos = trilha(pagina)
    ok("%s: a trilha tem tres degraus" % slug, len(passos) == 3, str([p[0] for p in passos]))
    if len(passos) == 3:
        ok("%s: os dois primeiros degraus sao link" % slug, all(p[1] for p in passos[:2]))

    tipos = {no.get("@type") for no in jsonlds(pagina)}
    ok("%s: JSON-LD tem CollectionPage" % slug, "CollectionPage" in tipos, str(sorted(tipos)))
    ok("%s: JSON-LD tem ItemList" % slug, "ItemList" in tipos)
    for no in jsonlds(pagina):
        if no.get("@type") == "ItemList":
            ok("%s: o ItemList tem %d itens, todos com endereco" % (slug, len(FICHAS)),
               no["numberOfItems"] == len(FICHAS) and all(x.get("item") for x in no["itemListElement"]))
    ok("%s: linka a mae numa frase do corpo" % slug, 'class="aqm-px-mae"' in c)


def medir_secao(banco):
    slug = SECAO
    pagina = servir(slug)
    c = corpo(pagina)
    t = texto(c)
    print("\n### secao %s" % slug)

    ok("%s: corpo tem tamanho de pagina" % slug, len(t) >= CORPO_MINIMO, "%d caracteres" % len(t))

    # --- o numero de especies do banco que passam no portao de pagina, CONTADO
    #     aqui pela regua propria: sete campos e dois corpos de fonte.
    def passa(e):
        if e.get("status_registro") in ("rascunho", "revalidar"):
            return False
        for campo in ("nome_cientifico", "nomes_populares_br", "porte_adulto_cm", "porte_medida",
                      "comprimento_minimo_aquario_cm", "convivencia"):
            if not e.get(campo):
                return False
        temp = e.get("temperatura_C") or {}
        if temp.get("min") is None or temp.get("max") is None:
            return False
        corpos = set()
        for f in e.get("fontes", []):
            ref = f.get("referencia") or ""
            nome = re.split(r"(?:\s+[—–-]\s+|:\s|,\s)", ref, maxsplit=1)[0].strip(" .:,")
            corpos.add(nome if nome and not re.search(r"\d", nome) else f.get("origem"))
        return len(corpos) >= 2

    elegiveis = [i for i, e in banco.items() if passa(e)]
    ok("%s: a abertura diz %d especies" % (slug, len(elegiveis)),
       ("São %d espécies" % len(elegiveis)) in t, "%d elegiveis" % len(elegiveis))
    ok("%s: diz quantas fichas estao no ar (%d)" % (slug, len(FICHAS)),
       ("%d espécies têm ficha própria no ar hoje" % len(FICHAS)) in t)

    # --- 16.5: categoria sem as filhas nao e link e nao mostra contagem
    cartoes = re.findall(r'<li class="aqm-px-cat">(.*?)</li>', c, re.S)
    ok("%s: serve seis cartoes de categoria" % slug, len(cartoes) == 6, "%d cartoes" % len(cartoes))
    com_link = [x for x in cartoes if "<a href=" in x]
    ok("%s: so a categoria com filhas e link" % slug, len(com_link) == 1, "%d com link" % len(com_link))
    for cartao in cartoes:
        if "<a href=" in cartao:
            continue
        ok("%s: cartao sem filha diz Em breve e nao mostra contagem" % slug,
           "Em breve" in texto(cartao) and not re.search(r"\d+ espécies", texto(cartao)))

    passos = trilha(pagina)
    ok("%s: a trilha tem dois degraus" % slug, len(passos) == 2, str([p[0] for p in passos]))
    tipos = {no.get("@type") for no in jsonlds(pagina)}
    ok("%s: JSON-LD tem CollectionPage" % slug, "CollectionPage" in tipos, str(sorted(tipos)))
    ok("%s: aponta para a categoria que existe" % slug, CATEGORIA in c)


banco_global = [None]


def medir_o_conjunto_contra_o_registro(banco):
    """As tres coisas que a leva 1 deixou passar, e que nao sao de uma pagina.

    Todas as tres tem a mesma forma: uma lista que devia crescer junto com o
    eixo e nao cresceu, porque ninguem cobrava. Aqui a lista de referencia e o
    REGISTRO do snippet — ele e o unico lugar que nao tem como ficar para tras,
    porque e ele que cria a pagina.
    """
    print("\n### o conjunto contra o registro do eixo")

    do_eixo = json.loads(subprocess.run(
        ["php", os.path.join(RAIZ, "ferramentas", "listar-paginas-do-eixo.php"), RAIZ],
        capture_output=True, text=True, check=True).stdout)

    # 1. O registro e o mapa escrito a mao neste arquivo dizem a mesma coisa. Se
    #    a proxima leva acrescentar pagina la e esquecer aqui, o teste mediria um
    #    eixo menor do que o que vai ao ar — e passaria verde.
    ok("o registro do snippet tem exatamente as %d paginas deste teste" % len(PAGINAS),
       sorted(do_eixo) == sorted(PAGINAS),
       "no snippet e nao aqui: %s" % sorted(set(do_eixo) - set(PAGINAS)))
    for slug, ident in FICHAS.items():
        ok("%s: o registro aponta para a especie que este teste conta (%s)" % (slug, ident),
           do_eixo.get(slug, {}).get("especie") == ident,
           str(do_eixo.get(slug, {}).get("especie")))

    # 2. TODA pagina do eixo serve meta description. As cinco da leva 1 foram ao
    #    ar sem nenhuma porque a lista do gerador era digitada; agora ela e
    #    perguntada ao registro, e esta afirmacao mede o resultado no <head>.
    for slug in do_eixo:
        cab = cabeca(servir(slug))
        ok("%s: serve <meta name=\"description\">" % slug,
           re.search(r'<meta name="description" content="[^"]{80,}"', cab) is not None)
        ok("%s: serve og:description" % slug, "og:description" in cab)

    # 2b. NENHUMA PAGINA DO EIXO E ORFA — o 16.4(f) medido NA BANCADA.
    #
    # Ate a leva 2 esta contagem so existia no `conferir-peixes-no-ar.py`, e por
    # isso o defeito foi descoberto depois do desembarque: com sete filhas e um
    # teto de quatro irmas, a casca escolhia sempre as quatro primeiras do mapa e
    # as duas ultimas da categoria nao eram irmas de ninguem. No ar elas ficaram
    # com UM link apontando para elas — o da mae — contra os sete da primeira.
    #
    # A conta e a mesma do ar: quantos CORPOS citam cada URL. Medir na bancada
    # significa que a proxima leva reprova antes de publicar, e nao depois.
    corpos = {slug: corpo(servir(slug)) for slug in do_eixo}
    for alvo in do_eixo:
        citam = sorted(s for s, c in corpos.items() if s != alvo and ('/%s/' % alvo) in c)
        ok("%s: 2 ou mais irmas do eixo a citam (16.4f)" % alvo, len(citam) >= 2,
           "%d: %s" % (len(citam), ", ".join(citam)))

    # A REPARTICAO, que e a razao de a roda existir: com teto de quatro e ordem
    # fixa, a cauda da categoria fica sem ninguem. Esta afirmacao mede a
    # diferenca entre a mais citada e a menos citada entre as FICHAS — se ela
    # abrir, o teto voltou a concentrar.
    citacoes = {a: sum(1 for s, c in corpos.items() if s != a and ('/%s/' % a) in c)
                for a in FICHAS}
    ok("as citacoes entre irmas sao repartidas (max - min <= 2)",
       max(citacoes.values()) - min(citacoes.values()) <= 2,
       "max=%d min=%d" % (max(citacoes.values()), min(citacoes.values())))

    # 3. O portao de PAGINA do esquema e o do snippet dizem a mesma frase, e
    #    nenhuma ficha registrada aponta para especie que nao passa nele.
    esquema = json.load(open(os.path.join(RAIZ, "dados", "esquema-especies.json"), encoding="utf-8"))
    regra = "cardume_minimo OU convivencia igual a solitario/casal/harem"
    ok("o esquema declara o portao de pagina separado do de catalogo",
       regra in esquema["minimo_para_sugerir"]["pagina-especie"]
       and regra not in esquema["minimo_para_sugerir"]["catalogo-de-especies"])
    snippet = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"), encoding="utf-8").read()
    ok("o snippet tem a regua da ficha escrita nele (pode_virar_ficha)",
       "function aquametria_peixes_pode_virar_ficha" in snippet)

    # A varredura e sobre o REGISTRO, nao sobre o mapa escrito a mao: a pergunta
    # e "alguma pagina que o snippet CRIA aponta para especie que nao pode ter
    # pagina?", e uma ficha registrada e esquecida aqui e exatamente o caso que
    # precisa ser pego. Varrer FICHAS responderia a pergunta mais facil.
    for slug, def_ in do_eixo.items():
        ident = def_.get("especie")
        if not ident:
            continue
        e = banco.get(ident)
        ok("%s: a especie registrada existe no banco (%s)" % (slug, ident), e is not None)
        if not e:
            continue
        passa = bool(e.get("cardume_minimo")) or e.get("convivencia") in ("solitario", "casal", "harem")
        ok("%s: a especie passa no portao de pagina do esquema" % slug, passa,
           "cardume=%s convivencia=%s" % (e.get("cardume_minimo"), e.get("convivencia")))


def medir_o_que_vale_para_todas():
    """Duas afirmacoes que nao sao de uma pagina, e sim do conjunto."""
    print("\n### o conjunto")

    # --- SLUG REPETIDO: `aquametria_casca_url_se_existir()` acha a pagina pelo
    #     post_name, que e o ULTIMO pedaco da URL. Duas paginas com o mesmo
    #     post_name em maes diferentes fariam o link do hub apontar para a
    #     errada — e /calculadoras/peixes/ esta no ARVORE.md como categoria
    #     futura, com o mesmo slug da secao que esta leva publica. Esta
    #     afirmacao e o alarme que vai tocar no dia em que alguem criar a outra.
    casca = open(os.path.join(RAIZ, "snippets", "aquametria-casca.php"), encoding="utf-8").read()
    categorias_calc = re.search(r"function aquametria_casca_categorias\(\).*?return array\((.*?)\);", casca, re.S)
    slugs_calc = re.findall(r"'([a-z0-9-]+)'\s*=>", categorias_calc.group(1)) if categorias_calc else []
    ok("nenhuma categoria de calculadora usa o slug de uma pagina do eixo",
       not (set(slugs_calc) & set(PAGINAS)),
       "colisao: %s" % sorted(set(slugs_calc) & set(PAGINAS)))

    # --- 16.5: CATEGORIA SO NASCE COM 3 FILHAS DE DADO REAL, e isto se mede no
    #     REGISTRO, nao na tela. Medir so a tela nao pega o defeito: o cartao de
    #     uma categoria sem filha ja sai sem link porque a pagina dela nao
    #     existe, e o dia em que alguem registrar a pagina o cartao viraria link
    #     sozinho — o erro estaria no registro, uma leva antes de aparecer.
    snippet = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"), encoding="utf-8").read()
    registradas = re.findall(r"'([a-z0-9-]+)' => array\(\s*\n\s*'nivel'\s*=> 2,", snippet)
    ok("so uma categoria de nivel 2 esta registrada como pagina",
       registradas == [CATEGORIA], str(registradas))
    for cat in registradas:
        bloco = re.search(r"'%s' => array\(\s*\n\s*'rotulo'.*?'especies' => array\((.*?)\),"
                          % re.escape(cat), snippet, re.S)
        filhas = re.findall(r"'([a-z0-9-]+)'", bloco.group(1)) if bloco else []
        ok("a categoria %s registrada como pagina tem 3 filhas ou mais no banco" % cat,
           len([f for f in filhas if f in banco_global[0]]) >= 3, "%d filhas" % len(filhas))

    # --- as duas promessas da secao 14.9, escritas no arquivo da pagina
    for slug in PAGINAS:
        bloco = re.search(r"'%s' => array\((.*?)\n\t\t\),\n" % re.escape(slug), snippet, re.S)
        ok("%s: o registro declara a consulta-alvo e o porque da primeira pagina" % slug,
           bloco is not None and "'consulta'" in bloco.group(1) and "'porque'" in bloco.group(1))


def main():
    banco = carregar_banco()
    banco_global[0] = banco
    medir_secao(banco)
    medir_categoria(banco)
    for slug, ident in FICHAS.items():
        medir_ficha(slug, ident, banco)
    medir_o_que_vale_para_todas()
    medir_o_conjunto_contra_o_registro(banco)

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()

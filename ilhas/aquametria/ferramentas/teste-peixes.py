#!/usr/bin/env python3
"""O PORTAO DO EIXO /peixes/ — mede o que as paginas do eixo SERVEM.

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
import shutil
import subprocess
import sys
import tempfile

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
    # leva 3, 12/09/2026 — a categoria corydoras inteira
    "quantos-litros-para-coridora-bronze": "corydoras-aeneus",
    "quantos-litros-para-coridora-pimenta": "corydoras-paleatus",
    "quantos-litros-para-coridora-panda": "corydoras-panda",
    "quantos-litros-para-coridora-sterbai": "corydoras-sterbai",
}

# As especies do catalogo que NAO declaram o fundo do aquario: a fonte publica o
# comprimento minimo e para ai. Escrito aqui a mao pelo mesmo motivo do mapa de
# cima — se o teste perguntasse ao banco quem tem base nula, ele mediria o banco
# contra ele mesmo e a afirmacao "a pagina diz COMPRIMENTO quando nao ha fundo"
# passaria verde com o banco inteiro nulo.
SEM_FUNDO_DECLARADO = {"hemigrammus-rhodostomus"}
SECAO = "peixes"

# A DATA DA CLASSIFICACAO DE SERP (14.9), com a regua propria deste arquivo.
#
# Ate 13/09/2026 esta afirmacao era `"12/09/2026" in t` — uma data digitada, e
# ela reprovaria uma pagina CERTA no dia em que uma leva nascesse classificada
# em outro dia. E a mesma familia da regua que morre quando o banco melhora: a
# afirmacao dependia de TODAS as paginas terem a mesma data, que e um caso do
# banco de hoje e nao uma propriedade do codigo.
#
# A regua agora e a regra, escrita aqui a mao pela decisao 1 do cabecalho: a
# pagina que declara `serp_em` no registro serve a data DELA; quem nao declara
# herda o padrao. O teste le o registro do snippet em texto e NAO chama
# `aquametria_peixes_serp_em()` — se chamasse, um erro na funcao faria os dois
# lados errarem juntos e o portao ficaria verde.
SERP_PADRAO = "12/09/2026"


def serp_declarada_no_registro(slug):
    """O `serp_em` que o registro do snippet declara para este slug, ou None."""
    snippet = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"),
                   encoding="utf-8").read()
    bloco = re.search(r"'%s' => array\((.*?)\n\t\t\),\n" % re.escape(slug), snippet, re.S)
    if bloco is None:
        return None
    achado = re.search(r"'serp_em'\s*=>\s*'([^']*)'", bloco.group(1))
    if achado is None or achado.group(1) == "":
        return None
    return achado.group(1)


def serp_esperada(slug):
    declarada = serp_declarada_no_registro(slug)
    return declarada if declarada is not None else SERP_PADRAO

# As categorias de nivel 2 QUE JA SAO PAGINA, e as especies que cada uma tem de
# listar — escritas aqui a mao pelo mesmo motivo do mapa de cima.
#
# Ate a leva 2 isto era `CATEGORIA = "tetras"`, uma string, e o teste afirmava
# `registradas == [CATEGORIA]`: a regua nao dizia "as categorias registradas sao
# estas", dizia "so existe UMA". Passou tres blocos porque so havia uma mesmo, e
# teria reprovado a segunda categoria da ilha sem apontar defeito nenhum — o
# oposto do que um portao serve para fazer. E a mesma familia das tres listas
# digitadas que a leva 2 converteu, numa forma mais discreta: nao um numero
# velho, e um mundo de um elemento so escrito como se fosse o mundo inteiro.
#
# O rotulo entra aqui junto porque a frase de abertura da categoria o usa, e
# tirar "tetras"/"coridoras" do slug por heuristica seria adivinhar por
# vizinhanca (secao 8) onde o certo e declarar.
# `barradas` e a OUTRA METADE da lista declarada: as especies que a categoria
# declara e o portao de catalogo recusa. Ela nasceu vazia nas duas categorias no
# ar, e nasceu declarada mesmo assim porque o que ela mede nao e o banco de
# hoje: e que a lista do snippet e a lista deste arquivo digam a mesma coisa.
# Sem ela, acrescentar uma especie barrada a uma categoria mudaria a pagina e
# nao mudaria uma afirmacao sequer — a tabela continuaria com o mesmo numero de
# linhas, que e exatamente como uma mudanca de lista passa despercebida.
CATEGORIAS = {
    "tetras": {
        "rotulo": "tetras",
        "barradas": [],
        "especies": [
            "paracheirodon-innesi",
            "paracheirodon-axelrodi",
            "hyphessobrycon-amandae",
            "hyphessobrycon-eques",
            "hemigrammus-erythrozonus",
            "hemigrammus-rhodostomus",
            "gymnocorymbus-ternetzi",
        ],
    },
    # leva 3, 12/09/2026
    "corydoras": {
        "rotulo": "coridoras",
        "barradas": [],
        "especies": [
            "corydoras-aeneus",
            "corydoras-paleatus",
            "corydoras-panda",
            "corydoras-sterbai",
        ],
    },
}
PAGINAS = [SECAO] + list(CATEGORIAS) + list(FICHAS)

# A qual categoria cada ficha pertence, derivado da regua acima e nao do
# snippet: e o que permite cobrar que a ficha aponte para a MAE dela, e nao
# para uma categoria qualquer que por acaso exista.
CATEGORIA_DA_FICHA = {
    slug: cat
    for cat, dados in CATEGORIAS.items()
    for slug, ident in FICHAS.items()
    if ident in dados["especies"]
}

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
    # A FRASE MUDOU EM 13/09/2026 (item 4 do despacho da Sentinela) e a DISTINCAO
    # NAO: a abertura nao cita mais quem declarou — "a fonte declara a BASE" virou
    # "O que manda é a BASE do aquário" —, porque a 15.2 proibe procedencia no
    # primeiro paragrafo. A regua continua sendo a mesma pergunta: a ficha com
    # fundo declarado fala de BASE e mostra o fundo; a ficha sem fundo fala de
    # COMPRIMENTO e diz que o fundo FICA EM ABERTO. Esta e a SEGUNDA regua desta
    # invariante, independente da do teste-voz.mjs, e as duas foram escritas em
    # arquivos diferentes de proposito.
    if sem_fundo:
        ok("%s: a frase mestra diz COMPRIMENTO, nunca BASE" % slug,
           "O que manda é o COMPRIMENTO do aquário" in t
           and "o fundo fica em aberto" in t
           and "é a BASE do aquário" not in t)
        ok("%s: declara a ausencia do fundo em vez de encolher calada" % slug,
           'class="aqm-px-sem-fundo"' in c and "não há largura declarada por ninguém" in t)
        ok("%s: e diz quais tabelas nao saem por causa disso" % slug,
           "não sai a tabela de litros por altura" in t)
        ok("%s: a fonte e atribuida ao comprimento, nao a base" % slug,
           "Quem declara esse comprimento é o" in t and "Quem declara essa base é o" not in t)
    else:
        ok("%s: a frase mestra diz BASE, porque a fonte declarou os dois lados" % slug,
           "O que manda é a BASE do aquário" in t
           and "O que manda é o COMPRIMENTO do aquário" not in t
           and "o fundo fica em aberto" not in t)
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
    # E A MAE E A DELA, nao uma mae qualquer (leva 3, 12/09/2026). Enquanto o
    # eixo teve uma categoria so, "linka a mae" e "linka a mae certa" eram a
    # mesma afirmacao, e a primeira bastava. Com a segunda categoria no ar elas
    # se separam, e o erro que a folga deixaria passar e mudo: uma ficha de
    # coridora registrada com 'pai' => 'tetras' iria AO AR funcionando, com a
    # trilha, o breadcrumb e a frase de mae inteiros, apontando para a categoria
    # errada. E a decisao 2 do cabecalho aplicada ao parentesco.
    mae = CATEGORIA_DA_FICHA[slug]
    frase_mae = re.search(r'<[^>]*class="aqm-px-mae".*?</\w+>', c, re.S)
    ok("%s: a mae da frase e a categoria %s" % (slug, mae),
       frase_mae is not None and ('/%s/' % mae) in frase_mae.group(0),
       frase_mae.group(0)[:160] if frase_mae else "sem frase de mae")
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
    ok("%s: diz a data em que a SERP DESTA pagina foi classificada" % slug,
       serp_esperada(slug) in t, serp_esperada(slug))


def medir_categoria(slug, banco):
    ESPECIES = CATEGORIAS[slug]["especies"]
    ROTULO = CATEGORIAS[slug]["rotulo"]
    pagina = servir(slug)
    c = corpo(pagina)
    t = texto(c)
    print("\n### categoria %s" % slug)

    ok("%s: corpo tem tamanho de pagina" % slug, len(t) >= CORPO_MINIMO, "%d caracteres" % len(t))
    ok("%s: nenhuma entidade &#038; dentro de <script>" % slug,
       all("&#038;" not in b for b in re.findall(r"<script[^>]*>(.*?)</script>", pagina, re.S)))

    # --- a listagem tem as sete especies e o numero CONTADO
    for ident in ESPECIES:
        ok("%s: lista %s" % (slug, ident), banco[ident]["nome_cientifico"] in t)
    ok("%s: a contagem da abertura e %d" % (slug, len(ESPECIES)),
       ("São %d %s" % (len(ESPECIES), ROTULO)) in t)
    # A prestação de contas tem DUAS formas, e a segunda so existe desde a leva
    # 2: com a fila vazia, "0 estão na fila, e a próxima leva sai depois" e uma
    # promessa sobre uma leva que nao existe. O teste cobra a forma certa para o
    # estado de hoje e cobra que a OUTRA nao apareca — senao a pagina poderia
    # servir as duas frases e passar.
    com_ficha = [i for i in ESPECIES if i in FICHAS.values()]
    na_fila = len(ESPECIES) - len(com_ficha)
    if na_fila > 0:
        ok("%s: diz quantas ja tem ficha (%d) e quantas faltam (%d)" % (slug, len(FICHAS), na_fila),
           ("%d já têm a conta inteira" % len(com_ficha)) in t and ("%d estão na fila" % na_fila) in t)
        ok("%s: nao diz que a lista esta fechada" % slug, "esta lista está fechada" not in t)
    else:
        ok("%s: a categoria esta fechada e a pagina diz isso" % slug,
           ("As %d espécies da tabela têm a conta inteira" % len(ESPECIES)) in t
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
            for ident in ESPECIES:
                if banco[ident]["nome_cientifico"] in texto(tr):
                    ordem.append(ident)
        frentes = [faixa_do_campo(banco[i], "comprimento_minimo_aquario_cm")[1] for i in ordem]
        ok("%s: a tabela sai da menor frente para a maior" % slug,
           frentes == sorted(frentes), str(list(zip(ordem, frentes))))
        ok("%s: a tabela tem uma linha por especie da categoria" % slug, len(ordem) == len(ESPECIES), str(ordem))

    # --- a ancora de cada filha e o titulo dela, nunca "clique aqui"
    ancoras = re.findall(r"<a [^>]*>(.*?)</a>", c, re.S)
    ancoras = [texto(a) for a in ancoras]
    for proibida in ("clique aqui", "saiba mais", "veja mais", "leia mais"):
        ok("%s: nenhuma ancora diz %r" % (slug, proibida),
           not any(proibida in a.lower() for a in ancoras))
    # AS FICHAS DESTA CATEGORIA, nao as do eixo inteiro (leva 3, 12/09/2026).
    # Ate a leva 2 as duas listas eram a mesma, porque so havia uma categoria, e
    # esta afirmacao varria `FICHAS`. Com a segunda no ar ela passou a cobrar
    # que /peixes/tetras/ apontasse para as coridoras — pedindo justamente o
    # cluster ralo que o 16.6 proibe. A regua estava errada, nao a pagina.
    minhas = [sl for sl, cat in CATEGORIA_DA_FICHA.items() if cat == slug]
    for outro in minhas:
        ok("%s: aponta para a ficha %s" % (slug, outro), outro in c)
    de_outra = [sl for sl, cat in CATEGORIA_DA_FICHA.items() if cat != slug]
    vazadas = [sl for sl in de_outra if sl in c]
    ok("%s: nao aponta para ficha de outra categoria" % slug, not vazadas, str(vazadas))

    # --- a trilha: tres degraus
    passos = trilha(pagina)
    ok("%s: a trilha tem tres degraus" % slug, len(passos) == 3, str([p[0] for p in passos]))
    if len(passos) == 3:
        ok("%s: os dois primeiros degraus sao link" % slug, all(p[1] for p in passos[:2]))

    # --- a prestacao de contas de quem a categoria DECLARA e a tabela nao mostra
    medir_barradas_da_categoria(slug, c, t, banco)

    tipos = {no.get("@type") for no in jsonlds(pagina)}
    ok("%s: JSON-LD tem CollectionPage" % slug, "CollectionPage" in tipos, str(sorted(tipos)))
    ok("%s: JSON-LD tem ItemList" % slug, "ItemList" in tipos)
    for no in jsonlds(pagina):
        if no.get("@type") == "ItemList":
            ok("%s: o ItemList tem %d itens, todos com endereco" % (slug, len(minhas)),
               no["numberOfItems"] == len(minhas) and all(x.get("item") for x in no["itemListElement"]))
    ok("%s: linka a mae numa frase do corpo" % slug, 'class="aqm-px-mae"' in c)


# ---------------------------------------------------------------------------
# A REGUA DO PORTAO DE CATALOGO, E O MOTIVO DE CADA RECUSA — escrita aqui
#
# Ate 13/09/2026 a unica regua deste arquivo sobre o portao era a `passa()` de
# dentro da `medir_secao`, que devolvia sim ou nao. O snippet passou a carregar
# tambem QUEM NAO PASSA, com o motivo, e "quem confere escreve a propria regua"
# vale igual para a lista dos ausentes: se este arquivo importasse os motivos do
# gerador, a tela e o portao errariam juntos e a lista de barrados poderia
# publicar a causa errada com toda a cara de conferida.
#
# A implementacao aqui NAO e a do gerador — e a mesma regra escrita de outro
# jeito, de proposito. O que as duas tem de concordar e o resultado.
# ---------------------------------------------------------------------------

CAMPOS_DO_PORTAO = (
    "nome_cientifico", "nomes_populares_br", "porte_adulto_cm", "porte_medida",
    "comprimento_minimo_aquario_cm", "convivencia", "temperatura_C",
)


def corpo_da_referencia(ref):
    """O nome do corpo de fonte que uma referencia deixa ler, ou ''.

    A regra: corta no primeiro separador (travessao, dois-pontos ou virgula
    seguidos de espaco), recusa o que tiver digito e o que passar de 40
    caracteres. Nome de corpo de fonte nao tem numero dentro — e o que separa
    "FishBase" de "FishBase: pH 5,0 a 7,8".
    """
    pedaco = re.split(r"(?:\s+[—–-]\s+|:\s|,\s)", str(ref or ""), maxsplit=1)[0].strip(" .:,")
    if not pedaco or len(pedaco) > 40 or any(d.isdigit() for d in pedaco):
        return ""
    return pedaco


def dominio(url):
    achado = re.match(r"https?://([^/]+)", str(url or ""))
    return achado.group(1).lower().replace("www.", "") if achado else ""


def corpos_por_dominio(banco):
    """dominio -> nome do corpo, aprendido das referencias do proprio banco."""
    mapa = {}
    for e in banco.values():
        for f in e.get("fontes", []):
            nome = corpo_da_referencia(f.get("referencia"))
            d = dominio(f.get("url"))
            if nome and d:
                mapa.setdefault(d, nome)
    return mapa


def motivos_do_portao(e, mapa_dominio):
    """Os codigos do vocabulario fechado que barram esta especie, na ordem."""
    codigos = []
    for campo in CAMPOS_DO_PORTAO:
        if campo == "temperatura_C":
            faixa = e.get(campo) or {}
            if faixa.get("min") is None or faixa.get("max") is None:
                codigos.append(campo)
        elif not e.get(campo):
            codigos.append(campo)
    corpos = set()
    for f in e.get("fontes", []):
        corpos.add(corpo_da_referencia(f.get("referencia")) or f.get("origem") or "")
    if len(corpos) < 2:
        codigos.append("duas fontes distintas")
    if e.get("status_registro") in ("rascunho", "revalidar"):
        codigos.append("status_registro " + str(e.get("status_registro")))
    if codigos:
        return codigos
    # So quem passou nos campos chega aqui: o gerador so procura fonte sem nome
    # depois de o registro estar completo, e a ordem importa porque um registro
    # pode falhar nas duas coisas.
    for f in e.get("fontes", []):
        if not (corpo_da_referencia(f.get("referencia")) or mapa_dominio.get(dominio(f.get("url")))):
            return ["fonte sem nome de corpo"]
    for c in e.get("conflitos", []):
        for v in c.get("valores", []):
            if not (corpo_da_referencia(v.get("referencia")) or mapa_dominio.get(dominio(v.get("url")))):
                return ["fonte sem nome de corpo"]
    return []


def barrados_do_banco(banco):
    """id -> codigos, para todo registro que o portao de catalogo recusa."""
    mapa = corpos_por_dominio(banco)
    fora = {}
    for ident, e in banco.items():
        codigos = motivos_do_portao(e, mapa)
        if codigos:
            fora[ident] = codigos
    return fora


def barrados_do_snippet():
    """O que o bloco BARRADOS do snippet carrega: id -> (cientifico, codigos).

    Lido em TEXTO, e na ordem em que esta escrito — a ordem e uma afirmacao da
    pagina ("de quem esta mais perto de entrar para quem esta mais longe") e
    ler por dicionario a perderia.
    """
    php = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"), encoding="utf-8").read()
    bloco = php.split("BARRADOS-INICIO")[1].split("BARRADOS-FIM")[0]
    achados = []
    for m in re.finditer(r"\n\t\t'([a-z0-9-]+)' => array\((.*?)\n\t\t\),", bloco, re.S):
        ident, corpo_reg = m.group(1), m.group(2)
        cientifico = re.search(r"'cientifico' => '([^']*)'", corpo_reg)
        faltando = re.search(r"'faltando' => array\((.*?)\n\t\t\t\)", corpo_reg, re.S)
        codigos = re.findall(r"'([^']+)',", faltando.group(1)) if faltando else []
        achados.append((ident, cientifico.group(1) if cientifico else "", codigos))
    return achados


def medir_barrados(banco):
    """A PRESTACAO DE CONTAS DA SECAO 7 ALCANCA QUEM NAO ESTA NA TABELA.

    A pagina dizia "sao 29 especies" e nao tinha como dizer que o banco tem 37:
    os barrados nao existiam no snippet. Estas afirmacoes cobram as duas metades
    — que o snippet carregue exatamente quem a regua daqui barra, e que a tela
    nomeie cada um com a causa em lingua de gente.
    """
    print("\n### os barrados: quem o banco tem e o portao nao deixa entrar")

    esperados = barrados_do_banco(banco)
    do_snippet = barrados_do_snippet()
    ids_snippet = [x[0] for x in do_snippet]

    ok("o snippet carrega os %d barrados do banco" % len(esperados),
       sorted(ids_snippet) == sorted(esperados),
       "snippet=%s banco=%s" % (sorted(ids_snippet), sorted(esperados)))
    ok("nenhum barrado esta tambem no catalogo",
       not (set(ids_snippet) & set(catalogo_do_snippet())),
       str(sorted(set(ids_snippet) & set(catalogo_do_snippet()))))
    ok("catalogo mais barrados fecham os %d registros do banco" % len(banco),
       len(catalogo_do_snippet()) + len(ids_snippet) == len(banco),
       "%d + %d" % (len(catalogo_do_snippet()), len(ids_snippet)))

    for ident, cientifico, codigos in do_snippet:
        if ident not in esperados:
            continue
        ok("%s: o motivo gravado e o que a regua daqui calcula" % ident,
           codigos == esperados[ident], "snippet=%s regua=%s" % (codigos, esperados[ident]))
        ok("%s: viaja com o nome cientifico do banco" % ident,
           cientifico == banco[ident]["nome_cientifico"], cientifico)

    # A ORDEM E UMA AFIRMACAO DA PAGINA: de quem falta menos para quem falta
    # mais. Recomputada aqui, nunca lida do gerador.
    quantos = [len(c) for _, _, c in do_snippet]
    ok("os barrados vao de quem esta mais perto de entrar para quem esta mais longe",
       quantos == sorted(quantos), str(list(zip(ids_snippet, quantos))))

    # --- a tela da secao
    c = corpo(servir(SECAO))
    t = texto(c)
    lista = re.search(r'<ul class="aqm-px-barrados">(.*?)</ul>', c, re.S)
    ok("%s: serve a lista de barrados" % SECAO, lista is not None)
    if lista is None:
        return
    itens = [texto(x) for x in re.findall(r"<li>(.*?)</li>", lista.group(1), re.S)]
    ok("%s: um item por barrado (%d)" % (SECAO, len(esperados)), len(itens) == len(esperados),
       "%d itens" % len(itens))

    total = len(banco)
    ok("%s: a frase conta os %d registros do banco" % (SECAO, total),
       ("guarda %d registros de espécie" % total) in t)
    ok("%s: a frase conta os %d que a tabela exige" % (SECAO, len(banco) - len(esperados)),
       ("e %d deles têm o mínimo declarado" % (len(banco) - len(esperados))) in t)
    ok("%s: a frase conta os %d que ficaram de fora" % (SECAO, len(esperados)),
       ("Os outros %d estão aqui pelo nome" % len(esperados)) in t)

    for ident in esperados:
        nome = banco[ident]["nome_cientifico"]
        achados = [x for x in itens if nome in x]
        ok("%s: nomeia %s uma vez so" % (SECAO, ident), len(achados) == 1, "%d vezes" % len(achados))
        if achados:
            ok("%s: a causa de %s esta em lingua de gente, e a traducao e a do codigo"
               % (SECAO, ident),
               all(traducao_do_motivo(cod) and traducao_do_motivo(cod) in achados[0]
                   for cod in esperados[ident]),
               achados[0])

    # NENHUMA DO CATALOGO NA LISTA DOS AUSENTES. A contradicao que a secao 7
    # nomeia — negar e afirmar o mesmo fato na mesma pagina — e o unico jeito de
    # este bloco ficar pior do que nao existir.
    vazadas = [i for i in catalogo_do_snippet() if banco[i]["nome_cientifico"] in texto(lista.group(1))]
    ok("%s: nenhuma espécie da contagem publicada aparece entre os ausentes" % SECAO,
       not vazadas, str(vazadas))

    # CODIGO DE BANCO NUNCA CHEGA A TELA (secao 5 e 15.1).
    crus = [cod for cod in CAMPOS_DO_PORTAO if cod in t]
    ok("%s: nenhum nome de campo do banco aparece no corpo" % SECAO, not crus, str(crus))
    ok("%s: nenhum motivo caiu no ramo sem tradução" % SECAO,
       "ainda não tem nome nesta tela" not in t)


def catalogo_do_snippet():
    """Os ids que o bloco CATALOGO do snippet carrega."""
    php = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"), encoding="utf-8").read()
    bloco = php.split("CATALOGO-INICIO")[1].split("CATALOGO-FIM")[0]
    return re.findall(r"\n\t\t'([a-z0-9-]+)' => array\(", bloco)


def traducao_do_motivo(codigo):
    """A frase que o snippet publica para um codigo, lida do mapa do PHP.

    LER O MAPA NAO E CHAMAR A REGUA DE QUEM PRODUZ O DADO: o que se mede aqui e
    que a tela nao serve codigo cru, e para isso e preciso saber qual frase
    corresponde a qual codigo. A afirmacao que importa — que o codigo esteja
    certo — e feita acima, contra o banco, sem passar por aqui.
    """
    php = open(os.path.join(RAIZ, "snippets", "aquametria-peixes.php"), encoding="utf-8").read()
    bloco = php.split("function aquametria_peixes_motivo_na_tela")[1].split("return isset")[0]
    achado = re.search(r"'%s'\s*=> '([^']*)'" % re.escape(codigo), bloco)
    return achado.group(1) if achado else ""


def categorias_declaradas_no_snippet():
    """O que o snippet declara por categoria, via a ferramenta que pergunta ao eixo."""
    return json.loads(subprocess.run(
        ["php", os.path.join(RAIZ, "ferramentas", "listar-categorias-do-eixo.php"), RAIZ],
        capture_output=True, text=True, check=True).stdout)


def medir_barradas_da_categoria(slug, c, t, banco):
    """QUEM A CATEGORIA DECLARA E A TABELA NAO MOSTRA.

    Ate 13/09/2026 o snippet descartava em silencio o id declarado que nao
    estivesse no catalogo: a lista podia crescer e a pagina nao dizia nada. As
    afirmacoes daqui cobram as tres coisas que aquele silencio escondia — que
    nenhum id declarado seja desconhecido do banco (erro de digitacao encolhe a
    tabela sem aviso), que a lista do snippet e a deste arquivo coincidam, e que
    a pagina nomeie cada barrada com a causa.

    O CONJUNTO ESTA VAZIO NAS DUAS CATEGORIAS NO AR, e por isso o ramo cheio e
    provado por mutacao que PRODUZ O MUNDO (secao 8 do ARQUIPELAGO.md): caso que
    o codigo permite e o banco ainda nao tem e caso que a regua trata hoje.
    """
    declaradas = categorias_declaradas_no_snippet()[slug]["especies"]
    esperadas = CATEGORIAS[slug]["especies"] + CATEGORIAS[slug]["barradas"]
    ok("%s: a lista declarada no snippet e a deste arquivo dizem o mesmo" % slug,
       sorted(declaradas) == sorted(esperadas),
       "snippet=%s aqui=%s" % (sorted(declaradas), sorted(esperadas)))

    desconhecidas = [i for i in declaradas if i not in banco]
    ok("%s: nenhum id declarado esta fora do banco" % slug, not desconhecidas, str(desconhecidas))

    barradas = CATEGORIAS[slug]["barradas"]
    lista = re.search(r'<ul class="aqm-px-barrados">(.*?)</ul>', c, re.S)
    if not barradas:
        ok("%s: sem barrada declarada, a pagina nao serve bloco de ausentes" % slug,
           lista is None)
        ok("%s: e a lista continua podendo se dizer fechada" % slug,
           "NÃO está fechada" not in t)
        return

    ok("%s: serve o bloco de ausentes" % slug, lista is not None)
    ok("%s: a contagem de ausentes e %d de %d declaradas" % (slug, len(barradas), len(declaradas)),
       ("%d de %d" % (len(barradas), len(declaradas))) in t)
    ok("%s: nao se diz fechada com %d esperando do lado de fora" % (slug, len(barradas)),
       "esta lista está fechada" not in t)
    if lista is None:
        return
    itens = [texto(x) for x in re.findall(r"<li>(.*?)</li>", lista.group(1), re.S)]
    ok("%s: um item por barrada declarada (%d)" % (slug, len(barradas)), len(itens) == len(barradas),
       "%d itens" % len(itens))
    esperados = barrados_do_banco(banco)
    for ident in barradas:
        if ident not in banco:
            continue  # ja reprovou em `desconhecidas`; perguntar ao banco aqui so quebraria
        nome = banco[ident]["nome_cientifico"]
        achados = [x for x in itens if nome in x]
        ok("%s: nomeia a ausente %s uma vez so" % (slug, ident), len(achados) == 1,
           "%d vezes" % len(achados))
        if achados:
            ok("%s: a causa de %s esta em lingua de gente" % (slug, ident),
               all(traducao_do_motivo(cod) and traducao_do_motivo(cod) in achados[0]
                   for cod in esperados.get(ident, [])),
               achados[0])


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
    ok("%s: so as categorias com filhas sao link (%d)" % (slug, len(CATEGORIAS)),
       len(com_link) == len(CATEGORIAS), "%d com link" % len(com_link))

    # A REGRA QUE O CARTAO IMPLEMENTA, dita como regra e nao como numero. Ate
    # 13/09/2026 o cartao virava link quando a categoria DECLARAVA especie; com
    # os barrados dentro do snippet, declarar deixou de significar entrar na
    # tabela, e categoria que declarasse so barradas viraria link para uma
    # pagina de tabela vazia — a pagina fina que o 16.5 nao deixa entrar no
    # indice. O que decide e a contagem de quem esta no catalogo, e e isso que
    # esta afirmacao cobra, recomputado do banco pela regua deste arquivo.
    no_catalogo = set(catalogo_do_snippet())
    for slug_cat, declarada in categorias_declaradas_no_snippet().items():
        cabem = [i for i in declarada["especies"] if i in no_catalogo]
        rotulo = declarada["rotulo"]
        tem_link = any(("<a href=" in x and rotulo in texto(x)) or
                       ("<a href=" in x and ("/%s/" % slug_cat) in x) for x in cartoes)
        if not cabem:
            ok("%s: o cartao de %s nao e link, porque nenhuma declarada entra na tabela"
               % (slug, slug_cat), not tem_link)
    for cartao in cartoes:
        if "<a href=" in cartao:
            continue
        ok("%s: cartao sem filha diz Em breve e nao mostra contagem" % slug,
           "Em breve" in texto(cartao) and not re.search(r"\d+ espécies", texto(cartao)))

    passos = trilha(pagina)
    ok("%s: a trilha tem dois degraus" % slug, len(passos) == 2, str([p[0] for p in passos]))
    tipos = {no.get("@type") for no in jsonlds(pagina)}
    ok("%s: JSON-LD tem CollectionPage" % slug, "CollectionPage" in tipos, str(sorted(tipos)))
    for cat in CATEGORIAS:
        ok("%s: aponta para a categoria %s, que existe" % (slug, cat), ("/%s/" % cat) in c)


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
    ok("as categorias de nivel 2 registradas sao exatamente as da regua",
       registradas == list(CATEGORIAS), "registro=%s regua=%s" % (registradas, list(CATEGORIAS)))
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

    # --- CATEGORIA COM ESPECIE TEM DE DECLARAR O CRITERIO DE QUEM ENTRA NELA.
    #
    #     A regra e sobre quem TEM especies, e nao sobre quem esta registrada
    #     como pagina, e a diferenca e a que importa: em 13/09/2026 a `bettas`
    #     ganhou o criterio escrito com a lista de especies ainda VAZIA, porque
    #     o criterio e o que a leva 4 precisa ter decidido ANTES de escrever uma
    #     linha (14.9 e 14.4). Cobrar o criterio so das registradas deixaria a
    #     leva seguinte encher a lista e publicar a categoria com o campo vazio
    #     — o defeito entraria no ar uma leva depois de ser cometido.
    #
    #     O bloco se procura dentro de `aquametria_peixes_categorias()` e nao no
    #     arquivo inteiro: o registro das paginas usa a MESMA forma `'slug' =>
    #     array(` e vem antes no arquivo, entao a busca solta achava o bloco
    #     errado e reprovava duas categorias que declaram o criterio ha tres
    #     blocos. Regua que mede o pedaco errado do arquivo reprova codigo certo.
    corpo_cats = re.search(
        r"function aquametria_peixes_categorias\(\) \{(.*?)\n\}\n\}", snippet, re.S)
    ok("o corpo de aquametria_peixes_categorias() foi localizado", corpo_cats is not None)
    if corpo_cats:
        for cat in re.findall(r"\t\t'([a-z0-9-]+)' => array\(", corpo_cats.group(1)):
            bloco = re.search(r"'%s' => array\((.*?)\n\t\t\),\n" % re.escape(cat),
                              corpo_cats.group(1), re.S)
            if bloco is None:
                continue
            especies = re.search(r"'especies' => array\((.*?)\),", bloco.group(1), re.S)
            tem_especie = bool(especies and re.search(r"'[a-z0-9-]+'", especies.group(1)))
            crit = re.search(r"'criterio'\s*=>\s*'(.*?)',\n", bloco.group(1), re.S)
            texto_crit = crit.group(1).strip() if crit else ""
            if tem_especie:
                ok("a categoria %s tem especie e declara o criterio de quem entra nela" % cat,
                   len(texto_crit) >= 80, "%d caracteres" % len(texto_crit))
            else:
                ok("a categoria %s ainda nao tem especie — criterio escrito e preparo, nao defeito"
                   % cat, True, "criterio com %d caracteres" % len(texto_crit))


def medir_serp_em_produzido():
    """O CAMINHO DA DATA PROPRIA, medido num mundo PRODUZIDO de proposito.

    Em 13/09/2026 nenhuma das doze paginas no ar declara `serp_em`: as doze
    herdam o padrao. Uma afirmacao sobre o caminho da data propria, medida no
    banco de hoje, mediria o caminho do PADRAO e ficaria verde com a funcao
    quebrada — e o dia em que ela importasse seria justamente o dia da leva 4,
    que nasce classificada em outra data. Entao o mundo se produz: uma copia da
    ilha em que UMA ficha declara data propria.

    As tres afirmacoes sao uma so ideia partida em tres, e cada uma pega um
    defeito diferente:
      (a) a pagina com data propria serve a data DELA — pega a funcao que
          ignora o campo e devolve a constante sempre;
      (b) essa mesma pagina NAO serve mais o padrao — pega a funcao que
          imprime os dois, que passaria em (a) sem consertar nada;
      (c) a pagina vizinha, que nao declara nada, CONTINUA no padrao — pega a
          funcao que devolve a data declarada para todo mundo, que e o erro
          mais provavel de quem escreve isto com pressa e o unico que (a) e (b)
          aprovariam juntas.
    """
    print("\n### o caminho da data propria da SERP (mundo produzido)")
    alvo, vizinho = "quantos-litros-para-tetra-neon", "quantos-litros-para-tetra-cardinal"
    propria = "01/01/2027"

    base = tempfile.mkdtemp(prefix="serp-em-")
    try:
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia)
        caminho = os.path.join(copia, "snippets", "aquametria-peixes.php")
        fonte = open(caminho, encoding="utf-8").read()
        marca = "\t\t'%s' => array(\n\t\t\t'nivel'    => 3," % alvo
        if fonte.count(marca) != 1:
            ok("o mundo produzido consegue injetar a data propria", False,
               "a marca do registro de %s mudou de forma" % alvo)
            return
        open(caminho, "w", encoding="utf-8").write(
            fonte.replace(marca, marca + "\n\t\t\t'serp_em'  => '%s'," % propria, 1))

        def servir_na_copia(slug):
            return subprocess.run(
                ["php", os.path.join(copia, "ferramentas", "render-pagina-completa.php"),
                 copia, slug],
                capture_output=True, text=True, check=True).stdout

        t_alvo = texto(corpo(servir_na_copia(alvo)))
        t_vizinho = texto(corpo(servir_na_copia(vizinho)))

        ok("(a) a pagina que declara serp_em serve a data DELA", propria in t_alvo)
        ok("(b) e deixa de servir o padrao", SERP_PADRAO not in t_alvo)
        ok("(c) a vizinha que nao declara nada segue no padrao",
           SERP_PADRAO in t_vizinho and propria not in t_vizinho)
    finally:
        shutil.rmtree(base, ignore_errors=True)


# Qual familia cada CRITERIO de categoria preparada declara como sendo o
# criterio dela. Escrito AQUI a mao, e de proposito: e a afirmacao central
# daqueles textos, e perguntar ao snippet qual familia ele usa seria pedir a
# resposta a quem produziu o dado (cicatriz 1 do cabecalho deste arquivo). Se
# uma categoria trocar de familia sem trocar esta linha, a afirmacao reprova.
FAMILIA_DO_CRITERIO = {
    "bettas": "Osphronemidae",
    "vivaparos": "Poeciliidae",
}

# O que o criterio dos vivaparos AFIRMA sobre o banco, em numero: que plati e
# espada, do mesmo genero, pedem frentes que diferem em duas vezes. Publicar a
# razao na tela e digitar um numero de banco numa frase — entao ela e cobrada
# aqui, e no dia em que o banco mudar a frase e reescrita em vez de envelhecer
# calada.
RAZAO_DE_FRENTE_DOS_VIVAPAROS = 2.0


def medir_categoria_preparada(banco):
    """A PRIMEIRA VIDA DE UMA CATEGORIA — declarada, e ainda sem URL.

    A `bettas` ganhou `criterio` e `linha_mestra` em 13/09/2026 e nada conferia
    que eles estavam la, nem que a familia declarada por aquele texto tem no
    banco as tres filhas do 16.5. Preparacao de leva conferida a olho e a mesma
    familia de defeito que o numero de tela digitado: parece conferida.

    A regua e propria: a pertinencia a categoria e recomputada do banco pela
    FAMILIA que o criterio declara (mapa acima, escrito a mao), e o portao de
    pagina e reescrito aqui pela frase do esquema — nunca importado do snippet.
    """
    print("\n### a categoria preparada, antes de existir URL")

    cats = json.loads(subprocess.run(
        ["php", os.path.join(RAIZ, "ferramentas", "listar-categorias-do-eixo.php"), RAIZ],
        capture_output=True, text=True, check=True).stdout)
    do_eixo = json.loads(subprocess.run(
        ["php", os.path.join(RAIZ, "ferramentas", "listar-paginas-do-eixo.php"), RAIZ],
        capture_output=True, text=True, check=True).stdout)

    def passa_no_portao_de_pagina(e):
        campos = ("nome_cientifico", "nomes_populares_br", "porte_adulto_cm",
                  "porte_medida", "comprimento_minimo_aquario_cm", "convivencia",
                  "temperatura_C")
        if any(not e.get(c) for c in campos):
            return False
        corpos = {f["origem"].replace("-via-busca", "") for f in e.get("fontes", [])}
        if len(corpos) < 2:
            return False
        return bool(e.get("cardume_minimo")) or e.get("convivencia") in ("solitario", "casal", "harem")

    # 1. PREPARACAO INTEIRA OU NENHUMA. Categoria com criterio e sem linha
    #    mestra (ou o contrario) e meia preparacao, e meia preparacao vai ao ar
    #    como pagina sem a primeira linha que explica por que ela junta o que
    #    junta — foi o que a `bettas` teve de escrever na mao em 1.3.0.
    for slug, c in cats.items():
        tem_crit = c["criterio"].strip() != ""
        tem_linha = c["linha_mestra"].strip() != ""
        ok("%s: criterio e linha_mestra declarados juntos, ou nenhum dos dois" % slug,
           tem_crit == tem_linha, "criterio=%s linha_mestra=%s" % (tem_crit, tem_linha))

    # 2. CATEGORIA SEM CRITERIO NAO NASCE (14.4: listagem tem texto proprio
    #    explicando o critério). Medido contra o REGISTRO, que e quem cria a
    #    pagina: se um dia alguem registrar a pagina antes de escrever o texto,
    #    isto reprova antes do desembarque.
    for slug, c in cats.items():
        if c["criterio"].strip() == "":
            ok("%s: sem criterio escrito, nao esta no registro do eixo" % slug,
               slug not in do_eixo)

    # 3. LISTA DE ESPECIES E DA LEVA, NAO DA PREPARACAO. Categoria declarada e
    #    nao nascida tem `especies` vazio; categoria nascida tem cheio. As duas
    #    direcoes, porque preencher a lista antes da leva faria a mae publicar
    #    contagem de uma categoria que o 16.5 ainda nao deixou nascer.
    for slug, c in cats.items():
        if slug in do_eixo:
            ok("%s: nascida, e a lista de especies dela esta cheia" % slug,
               len(c["especies"]) > 0)
        else:
            ok("%s: nao nascida, e a lista de especies dela esta vazia" % slug,
               len(c["especies"]) == 0, "%d" % len(c["especies"]))

    # 4. O 16.5 MEDIDO NA PREPARACAO: a familia que o criterio declara tem tres
    #    ou mais especies do banco que passam no portao de PAGINA. Tres e o
    #    minimo exato, e uma categoria preparada que caia abaixo disso nao pode
    #    receber leva — e melhor descobrir aqui que na hora de publicar.
    for slug, familia in FAMILIA_DO_CRITERIO.items():
        ok("%s: esta declarada no snippet" % slug, slug in cats)
        if slug not in cats:
            continue
        ok("%s: o criterio declarado nomeia a familia %s" % (slug, familia),
           familia in cats[slug]["criterio"] or familia.lower() in cats[slug]["criterio"].lower())
        da_familia = [e for e in banco.values() if e.get("familia") == familia]
        aptas = [e for e in da_familia if passa_no_portao_de_pagina(e)]
        ok("%s: a familia %s tem 3 ou mais especies aptas no banco (16.5)" % (slug, familia),
           len(aptas) >= 3, "%d de %d no banco: %s" % (
               len(aptas), len(da_familia), ", ".join(sorted(e["id"] for e in aptas))))

    # 5. A AFIRMACAO QUE O CRITERIO DOS VIVAPAROS PUBLICA, em numero. Ele diz
    #    que duas especies do mesmo genero pedem frentes que diferem em duas
    #    vezes; a razao e recomputada do banco entre as aptas da familia.
    aptas_viv = [e for e in banco.values()
                 if e.get("familia") == FAMILIA_DO_CRITERIO["vivaparos"]
                 and passa_no_portao_de_pagina(e)]
    frentes = [float(e["comprimento_minimo_aquario_cm"]) for e in aptas_viv]
    if frentes:
        razao = max(frentes) / min(frentes)
        ok("vivaparos: a razao entre a maior e a menor frente e %.1f, como o criterio afirma"
           % RAZAO_DE_FRENTE_DOS_VIVAPAROS,
           abs(razao - RAZAO_DE_FRENTE_DOS_VIVAPAROS) < 1e-9,
           "razao=%.3f frentes=%s" % (razao, sorted(frentes)))

    # 6. A PROMESSA DO CRITERIO E CUMPRIVEL, e isso se mede numa categoria que
    #    JA EXISTE. O texto novo termina dizendo que a contagem de quantas estao
    #    dentro e quantas esperam fica abaixo da tabela, nunca escrita no
    #    criterio — promessa sobre outra parte da pagina. Quem prova que aquela
    #    parte existe e o corpo de uma categoria no ar.
    nascida = next((s for s in CATEGORIAS if s in do_eixo), None)
    ok("existe categoria nascida para medir a promessa do criterio", nascida is not None)
    if nascida:
        c_nascida = corpo(servir(nascida))
        ok("%s: serve o bloco de contagem abaixo da tabela (aqm-px-fora)" % nascida,
           "aqm-px-fora" in c_nascida)
        ok("vivaparos: o criterio NAO escreve a contagem, e remete a ela",
           "contado logo abaixo da tabela" in cats["vivaparos"]["criterio"])


def main():
    banco = carregar_banco()
    banco_global[0] = banco
    medir_secao(banco)
    medir_barrados(banco)
    medir_categoria_preparada(banco)
    for cat in CATEGORIAS:
        medir_categoria(cat, banco)
    for slug, ident in FICHAS.items():
        medir_ficha(slug, ident, banco)
    medir_o_que_vale_para_todas()
    medir_o_conjunto_contra_o_registro(banco)
    medir_serp_em_produzido()

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()

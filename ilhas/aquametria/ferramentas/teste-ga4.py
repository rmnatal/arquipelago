#!/usr/bin/env python3
"""
PORTAO DA TAG DE MEDICAO (GA4) — Aquametria.

    python3 ferramentas/teste-ga4.py

Nasceu do despacho de prioridade alta de 12/09/2026 (dados/despachos.md), que poe
o gtag na casca das tres ilhas. Mede o que o despacho declara como criterio, e
nada que ele nao declare.

REGUA PROPRIA, e essa e a parte que importa (secao 8 do ARQUIPELAGO.md). O ID de
medicao esperado NAO e lido do snippet: e lido do PROMPT.md da ilha, que e onde a
ilha registra os endpoints e a propriedade dela. Um teste que pergunta ao snippet
qual e o ID certo aprova qualquer ID — inclusive o da ilha vizinha, que e o erro
caro de verdade aqui, porque uma tag com o ID errado MEDE, nao da erro nenhum, e
manda a audiencia desta ilha para o relatorio de outra. Por isso a afirmacao
central deste arquivo e "duas fontes dizem a mesma coisa", a cicatriz de
11/09/2026 do titulo que vivia no manifest e era medido no .md.

UM PROCESSO POR PAGINA, como manda a secao 8: o `static` da marca, do estilo e da
trilha sai na primeira pagina e some nas seguintes se as treze forem montadas no
mesmo processo.

O QUE ESTE PORTAO NAO CONSEGUE MEDIR, declarado em vez de silenciado:
  - a bancada NAO serve <meta name="description"> na home (o shim nao tem o
    contexto de is_front_page() que o snippet de SEO usa), entao a afirmacao de
    ordem contra a meta descricao e feita nas paginas que a servem, e a home e
    medida no HTML SERVIDO por ferramentas/conferir-ga4-no-ar.py;
  - se o GA4 recebeu o evento, ninguem mede daqui: www.googletagmanager.com
    responde 000 por politica de egresso (remedido em 12/09/2026) e a credencial
    da conta de servico nao existe neste ambiente. Isso e leitura do GA4, e o
    relatorio da execucao diz isso com essas palavras.

A ORDEM NO wp_head E AFIRMADA DE DOIS JEITOS, de proposito. Por pagina, comparando
a posicao em bytes no HTML montado (afirmacoes 8 a 10); e ESTRUTURALMENTE, lendo a
prioridade de todo add_action('wp_head') dos snippets da ilha e cobrando que a do
gtag seja a maior (afirmacao global 3). A segunda existe porque a primeira so
cobre a pagina que a bancada consegue montar hoje: no dia em que uma calculadora
nova registrar JSON-LD numa prioridade acima de 23, a afirmacao estrutural reprova
antes de alguem publicar a pagina.
"""
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

falhas = []
total = 0


def afirmar(ok, texto):
    global total
    total += 1
    if ok:
        print("  ok   " + texto)
    else:
        print("  FALHA " + texto)
        falhas.append(texto)


# ---------------------------------------------------------------------------
# A regua: o ID esperado vem do PROMPT.md, nunca do snippet.
# ---------------------------------------------------------------------------

def id_do_prompt():
    """Le a linha de GA4 do PROMPT.md da ilha. Sem essa linha nao ha teste: o
    portao para, em vez de aprovar por ausencia de regua."""
    caminho = os.path.join(RAIZ, "PROMPT.md")
    texto = open(caminho, encoding="utf-8").read()
    achados = re.findall(r"ID de medi[cç][aã]o\s*\*{0,2}\s*(G-[A-Z0-9]+)", texto)
    if not achados:
        sys.exit("PROMPT.md nao declara 'ID de medicao G-...' — sem regua nao ha portao.")
    if len(set(achados)) != 1:
        sys.exit("PROMPT.md declara mais de um ID de medicao: " + ", ".join(sorted(set(achados))))
    return achados[0]


def paginas():
    """A lista de paginas vem do MAPA DO PROPRIO RENDERIZADOR, nao digitada aqui:
    pagina nova entra na medicao sozinha, e lista digitada a mao envelhece calada
    (secao 8, o numero de tela que nasce contado)."""
    caminho = os.path.join(RAIZ, "ferramentas", "render-pagina-completa.php")
    texto = open(caminho, encoding="utf-8").read()
    bloco = re.search(r"\$GLOBALS\['__paginas'\]\s*=\s*array\((.*?)\n\);", texto, re.S)
    if not bloco:
        sys.exit("nao achei o mapa __paginas no render-pagina-completa.php")
    slugs = re.findall(r"'([a-z0-9-]+)'\s*=>\s*true", bloco.group(1))
    if len(slugs) < 5:
        sys.exit("mapa __paginas com %d paginas — regua suspeita, parando" % len(slugs))
    return slugs


def renderizar(slug):
    return subprocess.run(
        ["php", os.path.join(RAIZ, "ferramentas", "render-pagina-completa.php"), RAIZ, slug],
        capture_output=True, text=True, check=True,
    ).stdout


def blocos_script(html):
    return re.findall(r"<script\b[^>]*>.*?</script>", html, re.S)


ID = id_do_prompt()
SLUGS = paginas()

print("PORTAO DA TAG DE MEDICAO — Aquametria")
print("ID esperado, lido do PROMPT.md: " + ID)
print("%d paginas, um processo cada" % len(SLUGS))

# ---------------------------------------------------------------------------
# Afirmacoes globais — as que valem para a ilha, nao para uma pagina.
# ---------------------------------------------------------------------------

print("\n[global] as fontes do ID dizem a mesma coisa")

casca = open(os.path.join(RAIZ, "snippets", "aquametria-casca.php"), encoding="utf-8").read()

m = re.search(r"define\(\s*'AQUAMETRIA_CASCA_GA4_ID'\s*,\s*'([^']*)'\s*\)", casca)
afirmar(m is not None, "a casca define AQUAMETRIA_CASCA_GA4_ID como constante")
afirmar(bool(m) and m.group(1) == ID,
        "a constante da casca e o ID do PROMPT.md sao o mesmo valor (%s)" % (m.group(1) if m else "ausente"))

# A constante tem de estar no TOPO, junto das outras — a exigencia literal do
# despacho. "Topo" aqui e mecanico: antes da primeira add_action do arquivo.
pos_const = casca.find("AQUAMETRIA_CASCA_GA4_ID")
pos_1a_acao = casca.find("add_action(")
afirmar(0 <= pos_const < pos_1a_acao,
        "a constante nasce no topo do arquivo, antes do primeiro add_action")

# Terceira testemunha: o despacho que pediu a tag nomeia o ID de cada ilha.
desp = os.path.join(os.path.dirname(os.path.dirname(RAIZ)), "dados", "despachos.md")
if os.path.exists(desp):
    t = open(desp, encoding="utf-8").read()
    linha = re.search(r"aquametria\s*(?:→|->)\s*`?(G-[A-Z0-9]+)`?", t)
    if linha:
        afirmar(linha.group(1) == ID,
                "dados/despachos.md nomeia o mesmo ID para a aquametria (%s)" % linha.group(1))

# O numero de tela que nasce contado: a versao do manifest e a constante da casca.
manifest = json.load(open(os.path.join(RAIZ, "manifest.json"), encoding="utf-8"))
item = next((s for s in manifest["snippets"] if s["id"] == "aquametria-casca"), None)
mv = re.search(r"define\(\s*'AQUAMETRIA_CASCA_VERSAO'\s*,\s*'([^']*)'\s*\)", casca)
afirmar(item is not None and mv is not None and item.get("versao") == mv.group(1),
        "manifest e constante da casca declaram a mesma versao (%s / %s)"
        % (item.get("versao") if item else "?", mv.group(1) if mv else "?"))

print("\n[global] a prioridade do gtag no wp_head e a maior da ilha")

prioridades = {}
for arq in sorted(os.listdir(os.path.join(RAIZ, "snippets"))):
    if not arq.endswith(".php"):
        continue
    txt = open(os.path.join(RAIZ, "snippets", arq), encoding="utf-8").read()
    for corpo, prio in re.findall(
            r"add_action\(\s*'wp_head'\s*,\s*(.*?)\s*,\s*(\d+)\s*\)\s*;", txt, re.S):
        prioridades.setdefault(int(prio), []).append(arq)

prio_gtag = None
# A prioridade do gtag e a do bloco de wp_head que contem googletagmanager, achada
# no texto do snippet — nao digitada aqui, senao o teste guardaria a resposta.
m_prio = re.search(
    r"add_action\(\s*'wp_head'\s*,\s*function\s*\(\s*\)\s*\{(?:(?!add_action).)*?googletagmanager"
    r".*?\}\s*,\s*(\d+)\s*\)\s*;", casca, re.S)
afirmar(m_prio is not None, "o gtag entra por add_action('wp_head', ..., N) com prioridade explicita")
if m_prio:
    prio_gtag = int(m_prio.group(1))
    outras = sorted(p for p in prioridades if p != prio_gtag)
    afirmar(bool(outras) and prio_gtag > max(outras),
            "prioridade %d e maior que todas as outras do wp_head da ilha (%s)"
            % (prio_gtag, ", ".join(str(p) for p in outras)))

print("\n[global] a ESTRUTURA do bloco que imprime a tag")

# Estas duas afirmacoes nasceram de duas mutacoes que PASSARAM na primeira rodada,
# e as duas sao a mesma licao da C15 de 12/09/2026: quando o que a mutacao ameaca
# e a estrutura e nao um valor, o resultado servido fica identico e nenhuma
# medicao de RESULTADO pode ver. Entao o portao mede a estrutura.
bloco = m_prio.group(0) if m_prio else ""

# (1) Devolver o ID literal para dentro da funcao nao muda um byte do que o site
# serve — e e exatamente o que o despacho proibe, e o defeito do podeRegular() da
# C15, que guardava uma segunda copia da lista do esquema.
afirmar(bool(bloco) and re.search(r"G-[A-Z0-9]{6,}", bloco) is None,
        "o bloco que imprime a tag NAO guarda ID literal — le a constante")
afirmar("AQUAMETRIA_CASCA_GA4_ID" in bloco,
        "o bloco le AQUAMETRIA_CASCA_GA4_ID como fonte unica do ID")

# (2) A guarda da constante ausente. Ela protege um mundo real: o bloco de
# constantes do topo esta todo dentro de if ( ! defined( 'AQUAMETRIA_CASCA_VERSAO' ) ),
# entao uma copia antiga da casca ja carregada define a VERSAO, o bloco e pulado, e
# o GA4_ID nunca nasce. Sem a guarda, o PHP 8 morre com Error de constante
# indefinida e a pagina inteira cai — por uma tag de medicao.
afirmar(re.search(
    r"if\s*\(\s*!\s*defined\(\s*'AQUAMETRIA_CASCA_GA4_ID'\s*\).*?\)\s*\{\s*return;", bloco, re.S)
    is not None,
    "o bloco abre com a guarda de constante ausente, e ela devolve sem imprimir")

# ---------------------------------------------------------------------------
# Por pagina.
# ---------------------------------------------------------------------------

for slug in SLUGS:
    print("\n[/%s]" % ("" if slug == "inicio" else slug + "/"))
    html = renderizar(slug)
    cabeca = html.split("</head>")[0]

    carregadores = re.findall(r"<script\b[^>]*googletagmanager[^>]*>\s*</script>", html)
    afirmar(len(carregadores) == 1,
            "exatamente um carregador do gtag na pagina (achei %d)" % len(carregadores))

    if len(carregadores) == 1:
        tag = carregadores[0]
        afirmar(re.search(r"<script\b[^>]*\basync\b", tag) is not None,
                "o carregador vai com async")
        src = re.search(r'src="([^"]+)"', tag)
        afirmar(src is not None, "o carregador tem src")
        if src:
            url = src.group(1)
            consulta = url.split("?", 1)[1] if "?" in url else ""
            afirmar("&" not in consulta and "&#038;" not in consulta,
                    "a URL do carregador tem UM parametro so — nada de E-comercial para escapar")
            afirmar(re.fullmatch(r"id=" + re.escape(ID), consulta) is not None,
                    "o parametro e id=%s, o ID do PROMPT.md (servido: %s)" % (ID, consulta))

    inline = re.findall(r'<script\b[^>]*id="aquametria-ga4"[^>]*>(.*?)</script>', html, re.S)
    afirmar(len(inline) == 1,
            "exatamente um bloco de configuracao do gtag (achei %d)" % len(inline))

    if len(inline) == 1:
        js = inline[0]
        afirmar(ID in js, "o bloco de configuracao usa o mesmo ID (%s)" % ID)
        outros = re.findall(r"G-[A-Z0-9]+", js + (carregadores[0] if carregadores else ""))
        afirmar(set(outros) == {ID},
                "nenhum outro ID de medicao viaja na pagina (achei %s)" % ", ".join(sorted(set(outros))))
        # Sem banner e sem porta de consentimento: a configuracao e incondicional.
        afirmar("consent" not in js.lower(), "o bloco nao tem porta de consentimento")
        afirmar("if(" not in js.replace(" ", "") and "addEventListener" not in js
                and "setTimeout" not in js,
                "a configuracao e incondicional — nada espera clique, evento nem temporizador")

    afirmar("googletagmanager" in cabeca,
            "a tag esta DENTRO do <head>, nao no corpo")

    # Ordem: o gtag depois do titulo, da meta descricao e de todo JSON-LD.
    p_gtag = cabeca.find("googletagmanager")
    p_titulo = cabeca.find("<title")
    afirmar(p_titulo >= 0 and p_gtag > p_titulo, "o gtag vem depois do <title>")

    p_desc = cabeca.rfind('<meta name="description"')
    if p_desc >= 0:
        afirmar(p_gtag > p_desc, "o gtag vem depois da meta descricao")
    else:
        print("  --   esta pagina nao serve meta descricao na bancada; medida no ar")

    ld = [m.start() for m in re.finditer(r"application/ld\+json", cabeca)]
    if ld:
        afirmar(p_gtag > max(ld),
                "o gtag vem depois dos %d blocos de JSON-LD do <head>" % len(ld))
    else:
        print("  --   esta pagina nao tem JSON-LD no <head>")

    # A tag do Google e o UNICO script de terceiro da pagina publica (secao 22.4).
    hosts = set()
    for tag in re.findall(r'<script\b[^>]*src="(https?://[^"]+)"', html):
        hosts.add(re.sub(r"^https?://([^/]+).*$", r"\1", tag))
    afirmar(hosts <= {"www.googletagmanager.com"},
            "o unico script de terceiro e o do Google (achei: %s)"
            % (", ".join(sorted(hosts)) if hosts else "nenhum"))

    # A cicatriz de 08/09/2026: contada DENTRO dos <script>, nunca na pagina toda.
    dentro = sum(b.count("&#038;") for b in blocos_script(html))
    afirmar(dentro == 0, "zero &#038; dentro de <script> (achei %d)" % dentro)

print("\n%d afirmacoes, %d falha(s)" % (total, len(falhas)))
if falhas:
    for f in falhas:
        print("  - " + f)
    sys.exit(1)

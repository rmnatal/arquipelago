#!/usr/bin/env python3
"""
CONFERE A TAG DE MEDICAO NO HTML SERVIDO — Aquametria.

    python3 ferramentas/conferir-ga4-no-ar.py

Secao 4 do ARQUIPELAGO.md: commit sem Sync e sem verificacao no ar NAO e entrega,
e "aplicado com sucesso" no log do Sync nao e evidencia de nada. Este arquivo mede
o que o servidor devolve, nao o que o repositorio contem.

A LISTA DE URLS VEM DO SITEMAP NO AR, nunca digitada aqui. Duas razoes: pagina
nova entra na medicao sozinha, e uma lista escrita a mao vira, com o tempo, uma
afirmacao sobre um site que nao existe mais — que e a familia do numero de tela
digitado da secao 8.

O ID ESPERADO VEM DO PROMPT.md, como no portao de bancada: perguntar ao snippet
qual e o ID certo aprovaria o ID da ilha vizinha, e uma tag com ID errado MEDE em
silencio em vez de dar erro.

CACHE: a secao 4 manda acrescentar ?v=<hora e minuto> em toda conferencia, porque
o raw.githubusercontent guarda ~5 min e a borda da hospedagem guarda o seu
tanto. Esta ferramenta faz isso sozinha.

O QUE ELA ACHOU NA PRIMEIRA RODADA, antes de existir tag da casca, e vale ler
antes de mexer nas afirmacoes: o site JA servia um `gtag/js?id=GT-PL9DD7KW`, posto
pelo plugin Google Site Kit nas treze paginas — o despacho foi escrito acreditando
que nenhuma ilha tinha tag no ar. Duas consequencias de desenho, e as duas estao
no codigo abaixo: toda afirmacao localiza a NOSSA tag pelo ID da ilha, nunca pela
palavra "googletagmanager" (senao ela fica verde falando da tag alheia — foi o que
tres afirmacoes de ordem fizeram na primeira medicao); e o ID estrangeiro e
RELATADO com nome, em vez de reprovar ou de ser calado, porque quem o serve e um
plugin e nao a casca.

O QUE ELA NAO MEDE, e esta escrito para ninguem confundir entrega com medicao:
se o GA4 RECEBEU o evento. www.googletagmanager.com responde 000 por politica de
egresso deste ambiente (remedido em 12/09/2026, duas vezes) e a credencial da
conta de servico do Arquipelago nao existe aqui, entao nem a tag carrega daqui nem
o relatorio do GA4 pode ser lido. Isso e leitura de GA4 — do Raphael, no
navegador, ou de uma execucao com GOOGLE_SA_B64 no ambiente.
"""
import os
import re
import subprocess
import sys
import time
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://aquametria.com.br"
SITEMAPS = DOMINIO + "/wp-sitemap.xml"

falhas = []
total = 0


def afirmar(ok, texto):
    global total
    total += 1
    print(("  ok   " if ok else "  FALHA ") + texto)
    if not ok:
        falhas.append(texto)


def buscar(url, tentativas=3):
    """curl, com a regra de rede da secao 20.2: uma falha isolada e o tunel, e so
    vira bloqueio depois de repetir NA MESMA execucao."""
    selo = time.strftime("%H%M", time.gmtime())
    sep = "&" if "?" in url else "?"
    alvo = url + sep + "v=" + selo
    for i in range(tentativas):
        r = subprocess.run(["curl", "-sS", "--max-time", "30", "-w", "\n%{http_code}", alvo],
                           capture_output=True, text=True)
        corpo, _, codigo = r.stdout.rpartition("\n")
        if codigo.strip() == "200":
            return corpo
        print("      tentativa %d em %s: HTTP %s" % (i + 1, url, codigo.strip() or "000"))
    return None


def id_do_prompt():
    texto = open(os.path.join(RAIZ, "PROMPT.md"), encoding="utf-8").read()
    achados = sorted(set(re.findall(r"ID de medi[cç][aã]o\s*\*{0,2}\s*(G-[A-Z0-9]+)", texto)))
    if len(achados) != 1:
        sys.exit("PROMPT.md tem de declarar exatamente um 'ID de medicao G-...' (achei %d)"
                 % len(achados))
    return achados[0]


def urls_do_sitemap():
    indice = buscar(SITEMAPS)
    if indice is None:
        sys.exit("o sitemap nao respondeu 200 em 3 tentativas — sem lista de URLs nao ha medicao")
    urls = []
    for filho in re.findall(r"<loc>([^<]+)</loc>", indice):
        pagina = buscar(filho)
        if pagina is None:
            sys.exit("o sitemap filho %s nao respondeu 200 em 3 tentativas" % filho)
        urls.extend(re.findall(r"<loc>([^<]+)</loc>", pagina))
    # A home nunca esta no sitemap de posts nem no de pages como "/" — ela e a
    # pagina inicial, e e justamente a pagina que o despacho cita no criterio de
    # pronto. Entra sempre.
    if DOMINIO + "/" not in urls:
        urls.insert(0, DOMINIO + "/")
    return urls


def blocos_script(html):
    return re.findall(r"<script\b[^>]*>.*?</script>", html, re.S)


ID = id_do_prompt()
URLS = urls_do_sitemap()

print("TAG DE MEDICAO NO HTML SERVIDO — Aquametria")
print("ID esperado, lido do PROMPT.md: " + ID)
print("%d URLs, vindas do sitemap no ar\n" % len(URLS))

sem_descricao = []
sem_jsonld = []
alheios = {}
plugins_js = {}

for url in URLS:
    caminho = urllib.parse.urlparse(url).path or "/"
    print("[%s]" % caminho)
    html = buscar(url)
    if html is None:
        afirmar(False, "%s responde 200" % caminho)
        continue
    afirmar(True, "%s responde 200 (%d KB)" % (caminho, len(html) // 1024))

    cabeca = html.split("</head>")[0]

    # A afirmacao e sobre O NOSSO carregador, achado pelo ID da ilha — e nao sobre
    # "algum carregador do Google na pagina". A diferenca apareceu medindo: o
    # Site Kit ja servia um `gtag/js?id=GT-...` aqui, e um portao que contasse
    # carregadores daria verde com a tag ERRADA e a nossa ausente.
    nossos = [t for t in re.findall(r"<script\b[^>]*googletagmanager[^>]*>\s*</script>", html)
              if ID in t]
    afirmar(len(nossos) == 1,
            "um carregador com o ID da ilha, e um so (achei %d)" % len(nossos))
    if nossos:
        afirmar(re.search(r"\basync\b", nossos[0]) is not None, "carregador com async")
        src = re.search(r'src="([^"]+)"', nossos[0])
        consulta = src.group(1).split("?", 1)[1] if src and "?" in src.group(1) else ""
        afirmar(consulta == "id=" + ID,
                "a URL do carregador e id=%s e nada mais (servido: %s)" % (ID, consulta))

    inline = re.findall(r'<script\b[^>]*id="aquametria-ga4"[^>]*>(.*?)</script>', html, re.S)
    afirmar(len(inline) == 1, "um bloco de configuracao da casca (achei %d)" % len(inline))
    if inline:
        afirmar(ID in inline[0], "a configuracao da casca usa o ID da ilha")
    afirmar(len(re.findall(r"gtag\(\s*[\"']config[\"']\s*,\s*[\"']%s[\"']" % ID, html)) == 1,
            "o ID da ilha e configurado exatamente uma vez — dois config para o mesmo"
            " destino dobrariam a pagina vista")

    afirmar(("googletagmanager" in cabeca) and (ID in cabeca),
            "a tag da ilha esta dentro do <head>")

    # MEDICAO ESTRANGEIRA: nao e falha desta tag, e nao pode ser silencio. Um
    # segundo Google Tag na pagina e um numero que ninguem desta fabrica controla,
    # e se ele rotear para a MESMA propriedade a serie da secao 5 nasce dobrada.
    estrangeiros = sorted({i for i in re.findall(r"G[T]?-[A-Z0-9]{6,}", html) if i != ID})
    if estrangeiros:
        alheios.setdefault(caminho, estrangeiros)
        print("  !!   OUTRO ID de medicao servido nesta pagina: %s (ver relatorio)"
              % ", ".join(estrangeiros))

    # A POSICAO MEDIDA E A DA NOSSA TAG, achada pelo ID da ilha. Procurar
    # "googletagmanager" daria a posicao da tag do Site Kit, que esta na pagina
    # desde antes deste bloco — e a afirmacao ficaria verde falando de uma tag que
    # nao e nossa. Foi o que a primeira versao desta linha fez, medindo o site
    # ANTES do desembarque: tres afirmacoes de ordem deram ok com a nossa tag
    # ausente. E a cicatriz da secao 8 na hora de escolher o localizador.
    p_gtag = cabeca.find("gtag/js?id=" + ID)
    if p_gtag < 0:
        p_gtag = cabeca.find(ID)
    p_titulo = cabeca.find("<title")
    afirmar(p_titulo >= 0 and p_gtag > p_titulo,
            "a tag da ilha vem depois do <title>")

    p_desc = cabeca.rfind('<meta name="description"')
    if p_desc >= 0:
        afirmar(p_gtag > p_desc, "a tag da ilha vem depois da meta descricao")
    else:
        sem_descricao.append(caminho)
        afirmar(False, "a pagina serve <meta name=\"description\"> (despacho de 10/09, item 1)")

    ld = [m.start() for m in re.finditer(r"application/ld\+json", cabeca)]
    if ld:
        afirmar(p_gtag > max(ld),
                "a tag da ilha vem depois dos %d JSON-LD do <head>" % len(ld))
    else:
        sem_jsonld.append(caminho)
        print("  --   sem JSON-LD no <head> desta pagina")

    # Script de TERCEIRO e o que sai de outro dominio. O que vem de
    # aquametria.com.br e primeira parte (o nucleo do WordPress, e o que os
    # plugins hospedam) e nao entra nesta conta — contar o proprio dominio como
    # terceiro foi a primeira versao desta linha, e ela reprovava o site por ele
    # servir o proprio JavaScript.
    fora = sorted({re.sub(r"^https?://([^/]+).*$", r"\1", s)
                   for s in re.findall(r'<script\b[^>]*src="(https?://[^"]+)"', html)
                   if "aquametria.com.br" not in s})
    afirmar(fora in ([], ["www.googletagmanager.com"]),
            "o unico script de OUTRO dominio e o do Google (achei: %s)"
            % (", ".join(fora) if fora else "nenhum"))

    # Plugin que imprime JavaScript na pagina publica: seção 11.7 reserva a pagina
    # publica para a casca. Registrado, nao calado — e nao e falha desta tag.
    plugins = sorted({re.sub(r"^.*/plugins/([^/]+)/.*$", r"\1", s)
                      for s in re.findall(r'<script\b[^>]*src="([^"]+/plugins/[^"]+)"', html)})
    if plugins:
        plugins_js.setdefault(caminho, plugins)
        print("  !!   plugin com JavaScript na pagina publica: %s (secao 11.7)"
              % ", ".join(plugins))

    dentro = sum(b.count("&#038;") for b in blocos_script(html))
    afirmar(dentro == 0, "zero &#038; dentro de <script> (achei %d)" % dentro)
    print()

print("%d afirmacoes, %d falha(s)" % (total, len(falhas)))
if sem_jsonld:
    print("sem JSON-LD no <head> (nao e defeito desta tag): " + ", ".join(sem_jsonld))
if alheios:
    ids = sorted({i for v in alheios.values() for i in v})
    print("\nOUTRO ID DE MEDICAO NO AR, em %d das %d paginas: %s"
          % (len(alheios), len(URLS), ", ".join(ids)))
    print("  Nao e falha desta tag e nao foi tocado por esta execucao: quem o serve e")
    print("  um plugin, nao a casca. PRECISA DE RESPOSTA HUMANA, porque muda numero:")
    print("  se esse Google Tag rotear para a MESMA propriedade da ilha, a pagina vista")
    print("  chega duas vezes e a serie da secao 5 nasce dobrada. Quem le isso em um")
    print("  clique e o Raphael, no painel do Google Tag ou no proprio plugin.")
if plugins_js:
    print("\nPLUGIN COM JAVASCRIPT NA PAGINA PUBLICA (secao 11.7), em %d pagina(s): %s"
          % (len(plugins_js), ", ".join(sorted({p for v in plugins_js.values() for p in v}))))
if falhas:
    for f in falhas:
        print("  - " + f)
    sys.exit(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede o que o SITE serve, e nao o que o repositorio guarda.

    python3 ferramentas/conferir-no-ar.py

Existe porque "aplicado com sucesso" no log do Sync nao e evidencia de nada
(secao 8 do ARQUIPELAGO.md) e porque commit sem verificacao no ar nao e entrega
(secoes 4 e 18.4). A bancada mede o HTML que a bancada monta; isto abre as onze
URLs com curl e afirma sobre o HTML SERVIDO.

A regua e deste arquivo, nao do snippet: a URL do logo e a medida 78x52 estao
escritas literais aqui, copiadas do despacho do Raphael de 11/09. Se alguem
trocar a constante da casca por outra imagem, as duas metades nao erram juntas.

O `?v=` em toda URL nao e enfeite: o raw.githubusercontent guarda ~5 min e o
cache de borda guarda mais, e sem ele se conclui que nada mudou (secao 4).
"""

import json
import os
import re, subprocess, sys, time

BASE = "https://clubedomosaico.com.br"
LOGO = "https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png"
# O ID de medicao DESTA ilha, copiado a mao do PROMPT.md (despacho de 12/09/2026).
# Escrito aqui literal de proposito: ler CDM_CASCA_GA4_ID seria conferir a casca
# com a propria casca, e o defeito que este numero pega — o ID de outra ilha
# viajando numa copia da casca — nao tem sintoma nenhum na tela.
GA4 = "G-0K5PY39HV7"
PAGS = ["/", "/loja/", "/materiais/", "/materiais/como-sabemos/", "/como-fazer/",
        "/sobre/", "/contato/", "/divulgacao-de-afiliados/", "/privacidade/",
        "/materiais/qual-cola-usar-no-mosaico/", "/materiais/quantas-pastilhas-para-mosaico/"]

# A F2, medida no ar com regua propria: os pares abaixo sao (consulta, o que a
# pagina TEM que dizer) e estao escritos LITERAIS aqui, lidos da ficha do
# fabricante, nunca da constante do snippet nem do esquema. Se a regra mudar de
# um lado so, as duas metades nao erram juntas.
F2 = "/materiais/qual-cola-usar-no-mosaico/"
F2_CASOS = [
    ("base=espelho&onde=interno_seco", "Silicone Neutro", "Silicone Acético Construção"),
    ("base=cimento_concreto&onde=externo_exposto", "Silicone Neutro", "Silicone Acético Construção"),
    ("base=mdf_madeira&onde=interno_seco", "Cascorez", "Silicone Acético Construção"),
    ("base=vidro_laminado&onde=interno_seco", "Silicone Neutro", "Silicone Acético Construção"),
]

falhas = 0
feitos = 0
def ok(cond, rotulo, medida=""):
    global falhas, feitos
    feitos += 1
    print(("  ok   " if cond else "  FALHA ") + rotulo.ljust(60) + " " + str(medida))
    if not cond:
        falhas += 1

def buscar(url):
    v = str(int(time.time()))
    sep = "&" if "?" in url else "?"
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-w", "\n%{http_code}", url + sep + "v=" + v],
                       capture_output=True, text=True)
    partes = r.stdout.rsplit("\n", 1)
    return partes[0], partes[1] if len(partes) > 1 else "000"

print("NO AR — o logo do Raphael no cabecalho das onze paginas\n")
for p in PAGS:
    html, codigo = buscar(BASE + p)
    ok("200" == codigo, f"[{p}] HTTP 200", codigo)
    m = re.search(r'<a class="cdm-marca".*?</a>', html, re.S)
    marca = m.group(0) if m else ""
    ok(marca != "", f"[{p}] a marca sai no HTML servido")
    img = re.search(r'<img[^>]*class="cdm-marca-logo"[^>]*>', marca)
    img = img.group(0) if img else ""
    ok(f'src="{LOGO}"' in img, f"[{p}] o src e o arquivo que ele subiu")
    texto = re.sub(r"<[^>]+>", "", marca).strip()
    ok(texto == "", f"[{p}] nenhum texto ao lado do logo", repr(texto))
    ok('alt="Clube do Mosaico"' in img, f"[{p}] alt com o nome da marca")
    ok('width="78" height="52"' in img, f"[{p}] medida declarada 78x52")
    ok(html.count('class="cdm-marca-logo"') == 1, f"[{p}] o logo sai uma vez so",
       html.count('class="cdm-marca-logo"'))
    ok("cdm-marca-nome" not in html, f"[{p}] o wordmark em texto de 1.2.0 saiu da pagina")
    # zero &#038; DENTRO de <script> (secao 8)
    scripts = "".join(re.findall(r"<script[^>]*>.*?</script>", html, re.S))
    ok(scripts.count("&#038;") == 0, f"[{p}] zero &#038; dentro de <script>", scripts.count("&#038;"))
    # a folha da casca e a regra dos 52 px
    css = re.search(r'<style id="cdm-casca">(.*?)</style>', html, re.S)
    css = css.group(1) if css else ""
    ok(re.search(r"\.cdm-marca-logo\{[^{}]*height:52px", css) is not None,
       f"[{p}] a folha servida manda 52 px de altura")
    ok(re.search(r"header[^{}]*\{[^{}]*background:var\(--cdm-papel\)", css) is not None,
       f"[{p}] o cabecalho onde o logo vive continua claro")

    # ---- A TAG DO GA4 (despacho de 12/09/2026, secao 5 do ARQUIPELAGO.md).
    # Medida no <head> SERVIDO, porque a bancada prova que o codigo esta certo e
    # so isto prova que ele esta no ar — e porque nesta ilha existe um segundo
    # candidato a dono da tag (o Site Kit) que a bancada nao tem como ver.
    cabeca = re.search(r"<head\b[^>]*>(.*?)</head>", html, re.S)
    cabeca = cabeca.group(1) if cabeca else ""
    ok(cabeca.count("www.googletagmanager.com/gtag/js") == 1,
       f"[{p}] a tag do GA4 sai UMA vez no <head> servido",
       cabeca.count("www.googletagmanager.com/gtag/js"))
    ok(f"id={GA4}" in cabeca, f"[{p}] o ID servido e o desta ilha")
    ok(re.search(r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=' + re.escape(GA4) + r'">',
                 cabeca) is not None, f"[{p}] o script de terceiro vai com async")
    ok(f"gtag('config','{GA4}')" in cabeca, f"[{p}] o config nomeia o mesmo ID do src")
    # A ORDEM, medida no que o servidor serve — e nao no que a bancada monta.
    pos_gtag = html.find("www.googletagmanager.com/gtag/js")
    pos_title = html.find("<title>")
    pos_org = html.find('id="cdm-casca-jsonld"')
    pos_fonte = html.find("fonts.googleapis.com/css2")
    ok(-1 < pos_title < pos_gtag, f"[{p}] a tag nao entra antes do <title>")
    ok(-1 < pos_org < pos_gtag, f"[{p}] a tag nao entra antes do JSON-LD")
    ok(-1 < pos_gtag < pos_fonte, f"[{p}] mas entra antes da folha de fontes")
    # O UNICO SCRIPT DE TERCEIRO. Aqui esta afirmacao vale mais do que na
    # bancada: no site existem plugin e tema, e e o site que decide de verdade
    # quem imprime script na pagina publica.
    externos = [s for s in re.findall(r'<script[^>]+src="(https?://[^"]+)"', html)
                if "clubedomosaico.com.br" not in s]
    ok(len(externos) == 1 and "googletagmanager.com" in externos[0],
       f"[{p}] o gtag e o UNICO script de terceiro servido",
       "; ".join(externos) if externos else "nenhum")
    # A TAG SO PODE TER UM DONO. O Site Kit esta instalado nesta ilha (medido em
    # 12/09/2026: meta generator presente, gtag ausente). No dia em que alguem o
    # conectar pelo wp-admin, a sessao passa a ser contada duas vezes e nada na
    # tela muda — entao quem acusa e esta linha.
    ok(html.count("gtag('js',new Date())") == 1,
       f"[{p}] existe UM inicializador de gtag, e nao dois (Site Kit)",
       html.count("gtag('js',new Date())"))

print("\nA pagina de Privacidade no ar — a promessa que venceu hoje:")
html_pr, _ = buscar(BASE + "/privacidade/")
corpo_pr = re.search(r"<main.*?</main>", html_pr, re.S)
corpo_pr = corpo_pr.group(0) if corpo_pr else html_pr
ok("Google Analytics 4" in corpo_pr, "[privacidade] a pagina diz que o site mede audiencia com GA4")
ok("12 de setembro de 2026" in corpo_pr, "[privacidade] com a data em que a medicao comecou")
# A AFIRMACAO QUE MEDE A AUSENCIA, e e ela que importa: a pagina prometia por
# escrito ser atualizada ANTES de a medicao ser ligada. Conferir so que a frase
# nova chegou aprovaria uma pagina servindo a promessa e o fato lado a lado.
ok("Se um dia houver" not in corpo_pr,
   "[privacidade] a promessa antiga SAIU do HTML servido")
ok("remarketing" in corpo_pr, "[privacidade] e o que continua nao acontecendo continua escrito")

# ---------------------------------------------------------------------------
# O LUGAR DO LINK DE LOJA — a regua que envelheceu em 12/09/2026
#
# Ela era `"Link de loja em breve" in corpo`, e media o banco daquele dia: zero
# item com link de afiliado. Na noite em que as dez colas e rejuntes ganharam
# link, as duas afirmacoes reprovaram NO AR sem defeito nenhum embaixo — a ilha
# tinha melhorado e a regua chamou isso de erro. E a mesma familia que a
# Aquametria nomeou: regua que depende de um caso raro do banco morre no dia em
# que o banco melhora.
#
# O que se mede agora e o COMPORTAMENTO, e ele tem dois lados que o banco
# escolhe: item sem link reserva o lugar e diz "em breve" (nunca some do
# cartao); item com link serve o botao marcado como patrocinado. A regra vale
# com 0, com 10 ou com 500 links, e o banco do repositorio e quem diz qual dos
# dois lados tem de estar na tela.
_DADOS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dados")


def _conta_links(categorias):
    """(com link, sem link) somados nas categorias pedidas, lidos do repositorio."""
    com = sem = 0
    for nome in sorted(os.listdir(_DADOS_DIR)):
        if not (nome.startswith("materiais-") and nome.endswith(".json")):
            continue
        with open(os.path.join(_DADOS_DIR, nome), encoding="utf-8") as fh:
            banco = json.load(fh)
        if banco.get("categoria") not in categorias:
            continue
        for item in banco.get("materiais", []):
            if (item.get("afiliado") or {}).get("url"):
                com += 1
            else:
                sem += 1
    return com, sem


def _reserva_ou_entrega(corpo, categorias):
    com, sem = _conta_links(categorias)
    reserva = "Link de loja em breve" in corpo
    entrega = 'rel="sponsored' in corpo
    if sem > 0 and not reserva:
        return False          # ha item esperando e a pagina escondeu o cartao
    if com > 0 and not entrega:
        return False          # ha link no banco e a pagina nao o serve
    if sem == 0 and reserva:
        return False          # promete "em breve" sem ninguem esperando
    return com > 0 or sem > 0


def _diagnostico_do_link(corpo, categorias):
    com, sem = _conta_links(categorias)
    botoes = corpo.count('rel="sponsored')
    breves = corpo.count("Link de loja em breve")
    return "banco: %d com link, %d sem | tela: %d botoes, %d 'em breve'" % (com, sem, botoes, breves)


# ---------------------------------------------------------------------------
# A ESCADA DA SECAO 25 NO HTML SERVIDO (13/09/2026, f2 1.2.0)
#
# A bancada ja mede os tres degraus em mundos produzidos (`teste-f2.php`, secao
# 7b). O que SO se mede aqui e se o site esta servindo a versao que os conhece:
# `url_busca` estava no banco desde 13/09 e o site serviu semanas de cartao sem
# ele, porque a tela nao lia o campo. A diferenca entre "o manifest diz que
# subiu" e "o site esta servindo" e a marca do codigo novo no corpo servido —
# aqui, a classe `cdm-f2-busca`, que so existe a partir da 1.2.0.
#
# A regua conta do BANCO quantos itens da pagina tem ficha e piso, e cobra a
# tela pelo mesmo numero. Numero digitado envelheceria calado no dia em que um
# link fosse gerado ou morresse.
def _conta_escada(categorias):
    """(com ficha e piso, so piso, sem nada) lidos do repositorio."""
    ficha_e_piso = so_piso = sem_nada = 0
    for nome in sorted(os.listdir(_DADOS_DIR)):
        if not (nome.startswith("materiais-") and nome.endswith(".json")):
            continue
        with open(os.path.join(_DADOS_DIR, nome), encoding="utf-8") as fh:
            banco = json.load(fh)
        if banco.get("categoria") not in categorias:
            continue
        for item in banco.get("materiais", []):
            af = item.get("afiliado") or {}
            if af.get("url") and af.get("url_busca"):
                ficha_e_piso += 1
            elif af.get("url_busca"):
                so_piso += 1
            elif not af.get("url"):
                sem_nada += 1
    return ficha_e_piso, so_piso, sem_nada


def _escada_na_tela(corpo, categorias, rotulo):
    """A escada e medida CARTAO A CARTAO, nunca contra o tamanho do banco.

    A primeira versao desta regua comparou `cdm-f2-busca` no corpo com o numero
    de itens do banco que tem ficha e piso, e reprovou a pagina certa: a ancora
    da F2 serve SEIS cartoes e o banco tem DEZ itens, porque a pagina publica um
    caso de referencia e nao o catalogo inteiro. A regua media a pagina com a
    regua do banco. O que a escada afirma e sobre CADA cartao servido — todo
    cartao que tem botao de ficha tem tambem a linha discreta —, e essa
    afirmacao vale com 6, com 10 ou com 500 cartoes na tela.

    O banco continua entrando na medicao, mas no papel certo: ele diz o que a
    tela NAO pode ter (cartao a mais do que o banco sustenta) e se a etiqueta
    "em breve" tem direito de existir.
    """
    ficha_e_piso, so_piso, sem_nada = _conta_escada(categorias)
    cartoes = re.findall(r'<li class="cdm-f2-cartao[^"]*">.*?</li>', corpo, re.S)
    ok(len(cartoes) > 0, "[%s] a varredura acha os cartoes servidos" % rotulo, len(cartoes))

    com_ficha = [c for c in cartoes if 'class="cdm-f2-botao" href' in c]
    sem_segunda = [c for c in com_ficha if 'class="cdm-f2-busca"' not in c]
    ok(not sem_segunda,
       "[%s] 25.2: todo cartao com ficha serve TAMBEM a busca, na linha discreta" % rotulo,
       "%d cartoes com ficha, %d sem a segunda porta" % (len(com_ficha), len(sem_segunda)))

    so_busca = [c for c in cartoes if "cdm-f2-botao cdm-f2-botao-busca" in c]
    ok(not (set(so_busca) & set(com_ficha)),
       "[%s] 25.2: nenhum cartao serve a busca COMO BOTAO tendo ficha" % rotulo,
       "%d cartoes com a busca no botao" % len(so_busca))

    sem_compra = [c for c in cartoes if "cdm-f2-sem-loja" in c]
    ok(not sem_compra or sem_nada > 0,
       "[%s] 25.2: 'em breve' na tela exige item sem piso nenhum no banco" % rotulo,
       "banco: %d sem piso | tela: %d cartoes 'em breve'" % (sem_nada, len(sem_compra)))
    ok(len(cartoes) <= ficha_e_piso + so_piso + sem_nada,
       "[%s] a tela nao serve mais cartao do que o banco sustenta" % rotulo,
       "%d na tela, %d no banco" % (len(cartoes), ficha_e_piso + so_piso + sem_nada))

    # A MARCA DO CODIGO NOVO NO CORPO SERVIDO. E a diferenca entre "o manifest
    # diz que subiu" e "o site esta servindo": `cdm-f2-busca` so existe a partir
    # da f2 1.2.0, e foi exatamente este campo que passou semanas no banco sem
    # nenhuma linha de codigo para le-lo.
    if com_ficha or so_busca:
        ok('class="cdm-f2-busca"' in corpo or "cdm-f2-botao-busca" in corpo,
           "[%s] o site esta servindo a f2 1.2.0 — a marca do codigo novo esta no corpo" % rotulo)


print("\nA F2 no ar — a ferramenta responde, e nunca recomenda o que ela diz que nao serve:")
html_f2, codigo_f2 = buscar(BASE + F2)
ok("200" == codigo_f2, "[F2] a pagina-ancora responde 200", codigo_f2)
corpo_f2 = re.search(r"<main.*?</main>", html_f2, re.S)
corpo_f2 = corpo_f2.group(0) if corpo_f2 else html_f2
ok(len(re.sub(r"<[^>]+>", " ", corpo_f2)) > 4000, "[F2] o corpo tem tamanho de pagina",
   len(re.sub(r"<[^>]+>", " ", corpo_f2)))
ok(corpo_f2.count("<table class=\"cdm-f2-tabela\">") == 2,
   "[F2] as duas tabelas pre-renderizadas estao no HTML servido")
ok('rel="canonical" href="' + BASE + F2 + '"' in html_f2, "[F2] canonical aponta para a ancora")
ok('name="robots"' not in html_f2, "[F2] a ancora nao sai com noindex")
ok('"@type":"WebApplication"' in html_f2.replace(" ", ""), "[F2] JSON-LD WebApplication servido")
ok('"@type":"FAQPage"' in html_f2.replace(" ", ""), "[F2] JSON-LD FAQPage servido")
ok(_reserva_ou_entrega(corpo_f2, ("cola", "rejunte")),
   "[F2] o bloco de compra reserva o lugar do link OU serve o link, conforme o banco",
   _diagnostico_do_link(corpo_f2, ("cola", "rejunte")))
_escada_na_tela(corpo_f2, ("cola", "rejunte"), "F2")

for consulta, tem_que_recomendar, nao_pode_recomendar in F2_CASOS:
    html_c, codigo_c = buscar(BASE + F2 + "?" + consulta)
    ok("200" == codigo_c, f"[F2 {consulta}] responde 200", codigo_c)
    ok('content="noindex, follow"' in html_c, f"[F2 {consulta}] estado com parametro sai com noindex")
    # O bloco onde a RECOMENDACAO mora: a frase da resposta mais a vitrine de
    # compra. A secao do que nao usar fica FORA desta medida de proposito — o
    # nome do produto proibido aparece la, e contar na pagina inteira acharia os
    # dois. E o mesmo erro de contar &#038; na pagina toda.
    frase = re.search(r'<p class="cdm-f2-frase">(.*?)</p>', html_c, re.S)
    vitrine = re.search(r'<h2>Onde comprar</h2>.*?<ul class="cdm-f2-vitrine">(.*?)</ul>', html_c, re.S)
    bloco = (frase.group(1) if frase else "") + (vitrine.group(1) if vitrine else "")
    ok(bloco != "", f"[F2 {consulta}] a resposta e a vitrine saem no HTML servido")
    ok(tem_que_recomendar in bloco, f"[F2 {consulta}] recomenda {tem_que_recomendar}")
    ok(nao_pode_recomendar not in bloco,
       f"[F2 {consulta}] NAO recomenda {nao_pode_recomendar} (coerencia, secao 12)")
    fora = re.search(r'<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>', html_c, re.S)
    ok(fora is not None and nao_pode_recomendar in fora.group(1),
       f"[F2 {consulta}] o proibido aparece na secao do que nao usar")

# A F1, medida no ar com regua ARITMETICA escrita aqui. Os pares sao (consulta,
# area em cm2, pastilhas, gramas) e foram calculados A MAO no bloco da F1 — sao
# as mesmas contas que dados/pecas-tipicas.json guarda por extenso. Nenhum deles
# e lido do snippet nem do banco: se a formula mudar de um lado so, as duas
# metades nao erram juntas.
F1 = "/materiais/quantas-pastilhas-para-mosaico/"
F1_CASOS = [
    ("forma=cilindro&d=15&h=20&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=cimenticio", "942", "720", "264"),
    ("forma=disco&d=60&pastilha=p20&junta=3&sobra=10&esp=4&rejunte=cimenticio", "2.827", "588", "594"),
    ("forma=esfera&d=20&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=cimenticio", "1.257", "960", "352"),
    ("forma=moldura&l=40&a=60&vl=30&va=50&pastilha=p20&junta=3&sobra=10&esp=4&rejunte=cimenticio", "900", "188", "189"),
]

print("\nA F1 no ar — a conta que a pagina serve e a conta que a gente fez na mao:")
html_f1, codigo_f1 = buscar(BASE + F1)
ok("200" == codigo_f1, "[F1] a pagina-ancora responde 200", codigo_f1)
corpo_f1 = re.search(r"<main.*?</main>", html_f1, re.S)
corpo_f1 = corpo_f1.group(0) if corpo_f1 else html_f1
texto_f1 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo_f1))
ok(len(texto_f1) > 4000, "[F1] o corpo tem tamanho de pagina", len(texto_f1))
ok(corpo_f1.count('<table class="cdm-f1-tabela">') == 3,
   "[F1] as tres tabelas pre-renderizadas estao no HTML servido",
   corpo_f1.count('<table class="cdm-f1-tabela">'))
ok('rel="canonical" href="' + BASE + F1 + '"' in html_f1, "[F1] canonical aponta para a ancora")
ok('name="robots"' not in html_f1, "[F1] a ancora nao sai com noindex")
ok('"@type":"WebApplication"' in html_f1.replace(" ", ""), "[F1] JSON-LD WebApplication servido")
ok('"@type":"FAQPage"' in html_f1.replace(" ", ""), "[F1] JSON-LD FAQPage servido")
ok(_reserva_ou_entrega(corpo_f1, ("rejunte",)),
   "[F1] o bloco de compra reserva o lugar do link OU serve o link, conforme o banco",
   _diagnostico_do_link(corpo_f1, ("rejunte",)))
_escada_na_tela(corpo_f1, ("rejunte",), "F1")
ok("Ainda não temos as pastilhas no nosso banco" not in texto_f1,
   "[F1] a frase 'ainda nao temos as pastilhas' saiu do ar (era falsa desde 12/09)")

# ---------------------------------------------------------------------------
# A VITRINE DE PASTILHA NO AR (f1 1.2.0). A regua e deste arquivo: os treze
# codigos estao escritos LITERAIS abaixo, copiados do banco a mao, e os tres
# elegiveis de 2 cm tambem. Ler o banco daqui seria conferir o site com a mesma
# fonte que o site le (secao 8).
# ---------------------------------------------------------------------------
PASTILHAS_NO_BANCO = ["K2501", "K2502", "MIX2510", "K117", "K77", "K66", "A11", "A61",
                      "A37", "ST5102", "AF1500", "102", "IC02"]
DE_2CM = ["A11", "A61", "A37"]

print("\nA vitrine de pastilha no ar (f1 1.2.0):")
tabela_p = re.search(r'<table class="cdm-f1-tabela cdm-f1-tabela-pastilhas">.*?<tbody>(.*?)</tbody>',
                     corpo_f1, re.S)
tabela_p = tabela_p.group(1) if tabela_p else ""
ok(tabela_p != "", "[F1] a tabela pre-renderizada do banco de pastilhas esta no HTML SERVIDO")
ok(tabela_p.count("<tr>") == len(PASTILHAS_NO_BANCO),
   "[F1] a tabela serve uma linha por item do banco",
   f"{tabela_p.count('<tr>')} de {len(PASTILHAS_NO_BANCO)}")
texto_tab = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", tabela_p))
faltam = [c for c in PASTILHAS_NO_BANCO if not re.search(r"\b" + re.escape(c) + r"\b", texto_tab)]
ok(not faltam, "[F1] os treze codigos do banco estao na tabela servida",
   "todos" if not faltam else ", ".join(faltam))
# O ESTADO-ANCORA E 1 cm E 1 cm TEM ZERO: a pagina explica a causa que mediu.
ok("não tem nenhuma pastilha de 1 cm no banco" in texto_f1,
   "[F1] no ancora a pagina diz que nao tem 1 cm, com a causa medida")
ok("não aparece em catálogo de fabricante" in texto_f1,
   "[F1] e diz POR QUE: 1 cm nao existe em catalogo de fabricante")

# O estado de 2 cm: tres cartoes, e cada um com o lugar do link reservado.
html_p20, codigo_p20 = buscar(BASE + F1 + "?forma=cilindro&d=15&h=20&pastilha=p20&junta=2&sobra=10&esp=4&rejunte=cimenticio")
ok("200" == codigo_p20, "[F1 2 cm] responde 200", codigo_p20)
bloco_p20 = re.search(r"<h2>E onde comprar a pastilha</h2>(.*?)</div>\s*<div class=\"cdm-f1-secao\">",
                      html_p20, re.S)
bloco_p20 = bloco_p20.group(1) if bloco_p20 else ""
ok(bloco_p20 != "", "[F1 2 cm] o bloco da pastilha sai no HTML servido")
cartoes_p20 = bloco_p20.count('<li class="cdm-f2-cartao"')
ok(cartoes_p20 == len(DE_2CM),
   "[F1 2 cm] a vitrine serve um cartao por elegivel de 2 cm",
   "%d de %d" % (cartoes_p20, len(DE_2CM)))
# AS ETIQUETAS VIRAM ESPACO, e nao desaparecem: `strip_tags` cola "Mosaic" com
# "A11" e a busca por palavra isolada nao casa com nada. Foi assim que a bancada
# acusou quatro estados de nao nomear os elegiveis que eles nomeiam.
texto_p20 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloco_p20))
ok(all(re.search(r"\b" + re.escape(c) + r"\b", texto_p20) for c in DE_2CM),
   "[F1 2 cm] os tres de 2 cm estao nomeados no bloco", ", ".join(DE_2CM))
ok(bloco_p20.count('class="cdm-f2-compra"') == len(DE_2CM),
   "[F1 2 cm] todo cartao de pastilha tem bloco de compra, cheio ou reservado")
ok(bloco_p20.count("Link de loja em breve") == len(DE_2CM),
   "[F1 2 cm] os treze estao sem piso, e o cartao RESERVA o lugar em vez de sumir")
# A PORTA DO CAQUINHO IRREGULAR, que e a decisao desta versao sobre os cinco
# itens cujo lado o seletor nao lista.
ok("caquinho irregular" in re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloco_p20)),
   "[F1 2 cm] a pagina manda ao caquinho irregular quem quer o lado que o seletor nao lista")
html_ir, codigo_ir = buscar(BASE + F1 + "?forma=cilindro&d=15&h=20&pastilha=irregular&ladoeq=3&junta=2&sobra=10&esp=4&rejunte=cimenticio")
bloco_ir = re.search(r"<h2>E onde comprar a pastilha</h2>(.*?)</div>\s*<div class=\"cdm-f1-secao\">",
                     html_ir, re.S)
bloco_ir = bloco_ir.group(1) if bloco_ir else ""
ok("200" == codigo_ir, "[F1 irregular 3 cm] responde 200", codigo_ir)
ok(bloco_ir.count('<li class="cdm-f2-cartao"') == 3,
   "[F1 irregular 3 cm] o caquinho irregular ALCANCA os tres K de 3 cm, que o seletor nao lista",
   bloco_ir.count('<li class="cdm-f2-cartao"'))
# A TRILHA E O CLUSTER, que so existem porque a pagina tem mae e agora tem irmas
ok('Veja também' in corpo_f1, "[F1] o bloco Veja tambem saiu (duas irmas no ar)")
ok(BASE + "/materiais/qual-cola-usar-no-mosaico/" in corpo_f1,
   "[F1] a pagina linka a irma (a F2)")

for consulta, area, pastilhas, gramas in F1_CASOS:
    html_c, codigo_c = buscar(BASE + F1 + "?" + consulta)
    ok("200" == codigo_c, f"[F1 {consulta[:28]}] responde 200", codigo_c)
    ok('content="noindex, follow"' in html_c, f"[F1 {consulta[:28]}] estado com parametro sai com noindex")
    # SO o bloco de resposta: a tabela das doze pecas traz outros numeros, e
    # procurar na pagina inteira acharia qualquer um deles. Mesmo erro de contar
    # &#038; na pagina toda.
    bloco = re.search(r'<div class="cdm-f1-resposta"[^>]*>(.*?)</div>\s*<div', html_c, re.S)
    bloco = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloco.group(1))) if bloco else ""
    ok(bloco != "", f"[F1 {consulta[:28]}] a resposta sai no HTML servido")
    ok(area + " cm²" in bloco, f"[F1 {consulta[:28]}] area {area} cm2")
    ok(pastilhas + " pastilhas" in bloco, f"[F1 {consulta[:28]}] {pastilhas} pastilhas")
    ok(gramas + " g" in bloco, f"[F1 {consulta[:28]}] {gramas} g de rejunte")

# A RECUSA DO BLOCO 3c, medida no ar: rejunte que nao e po nao ganha numero.
html_e, codigo_e = buscar(BASE + F1 + "?forma=cilindro&d=15&h=20&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=epoxi")
bloco_e = re.search(r'<div class="cdm-f1-resposta"[^>]*>(.*?)</div>\s*<div', html_e, re.S)
bloco_e = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloco_e.group(1))) if bloco_e else ""
ok("200" == codigo_e, "[F1 epoxi] responde 200", codigo_e)
ok(re.search(r"\d[\d\.,]* g\b", bloco_e) is None,
   "[F1 epoxi] NENHUM numero de rejunte na resposta (correcao do bloco 3c)", bloco_e[-90:])
ok("não calcula" in re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_e)),
   "[F1 epoxi] a pagina diz POR QUE nao calcula")

# ---------------------------------------------------------------------------
# O DESPACHO DA SENTINELA DE 12/09/2026, medido no HTML SERVIDO — e nas palavras
# do proprio despacho, nao nas minhas. A secao 18.4 do contrato e explicita: o
# despacho morre quando e VERIFICADO no ar, e o criterio e o que ele declara.
#
# A bancada varre 720 estados; aqui vao os que o despacho nomeia um a um, mais a
# soma que ele exige. Regua propria: os 5 nomes comerciais estao escritos
# LITERAIS abaixo, copiados do banco a mao, para o site e o teste nao lerem a
# mesma fonte (secao 8).
# ---------------------------------------------------------------------------
print("\nO despacho da Sentinela de 12/09, medido no ar:")

REJUNTES = ["Rejunte Cerâmicas Quartzolit", "Rejunte Porcelanatos e Cerâmicas Quartzolit",
            "Rejunte Acrílico Quartzolit", "Rejunte Epóxi Quartzolit", "Rejunte Piscinas Quartzolit"]


def so_prosa(html, abre, fecha):
    """O bloco pedido, SEM os cartoes da vitrine: a prestacao de contas e prosa,
    e o nome dentro do cartao e a vitrine fazendo o trabalho dela."""
    m = re.search(abre + r"(.*?)(?=" + fecha + r"|</main>)", html, re.S)
    if not m:
        return ""
    corpo = re.sub(r"<li\b.*?</li>", " ", m.group(1), flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo))


def conta(texto, nome):
    """Nome de produto e substring de outro; desconta o nome maior."""
    n = texto.count(nome)
    for outro in REJUNTES:
        if outro != nome and nome in outro:
            n -= texto.count(outro)
    return max(0, n)


# ITEM 1 — a F1 nao culpa mais a folga quando quem exclui e o lugar.
BASE_F1 = "forma=disco&d=50&pastilha=p20&esp=6&sobra=15&rejunte=cimenticio"
for onde, rotulo in [("externo_exposto", "no sol e na chuva"), ("contato_permanente_agua", "dentro da água")]:
    for junta in (2, 4, 10):
        html_d, codigo_d = buscar(f"{BASE}{F1}?{BASE_F1}&onde={onde}&junta={junta}")
        bloco = so_prosa(html_d, r"<h2>Qual rejunte cabe nessa folga</h2>", r'<p class="cdm-f1-aviso"')
        marca = f"[item 1 {onde[:9]} {junta}mm]"
        ok("200" == codigo_d, f"{marca} responde 200", codigo_d)
        ok("Nenhum rejunte do nosso banco declara folga de" not in bloco,
           f"{marca} a frase do defeito sumiu da pagina")
        ok("é o LUGAR, não a folga" in bloco,
           f"{marca} a pagina diz que a exclusao e do lugar")
        ok(rotulo in bloco, f"{marca} e nomeia o lugar", rotulo)
        # A contradicao do despacho: negar a folga e, no mesmo bloco, listar
        # produto "dentro dessa folga".
        ok(not ("do nosso banco cobre folga de" in bloco and "dentro dessa folga" in bloco),
           f"{marca} nao nega e afirma o mesmo fato no mesmo bloco")

# ITEM 2 — a prestacao de contas da F2 fecha o banco, e a vitrine serve o que a
# frase nomeia. O caso-ancora e o que a Sentinela mediu, com os 5 nomes.
for consulta in ["base=ceramica_esmaltada_porcelana&caco=pastilha_ceramica&onde=interno_seco&junta=2",
                 "base=ceramica_esmaltada_porcelana&caco=pastilha_ceramica&onde=externo_exposto&junta=2",
                 "base=vidro&caco=pastilha_vidro&onde=interno_molhado&junta=4"]:
    html_d, codigo_d = buscar(f"{BASE}{F2}?{consulta}")
    bloco = so_prosa(html_d, r"<h2>E o rejunte, que vai entre os caquinhos</h2>", r'<div class="cdm-f2-secao[ "]')
    marca = "[item 2 " + consulta.split("onde=")[1][:22] + "]"
    ok("200" == codigo_d, f"{marca} responde 200", codigo_d)
    faltando = [n for n in REJUNTES if conta(bloco, n) != 1]
    ok(not faltando, f"{marca} os 5 rejuntes do banco nomeados 1 vez cada",
       "todos" if not faltando else "; ".join(faltando))

# A tabela pre-renderizada, que e a metade que a IA le: cada linha soma o banco.
html_t, _ = buscar(BASE + F2)
tabela = re.search(r"<h2>O mesmo, para o rejunte</h2>(.*?)</table>", html_t, re.S)
linhas_ruins = []
if tabela:
    for i, tr in enumerate(re.findall(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>",
                                      tabela.group(1), re.S)):
        serve = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", tr[2]))
        fora_c = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", tr[3]))
        n_serve = sum(conta(serve, n) for n in REJUNTES)
        n_fora = sum(int(x) for x in re.findall(r"(\d+)\s+(?:por|porque)", fora_c))
        if n_serve + n_fora != len(REJUNTES):
            linhas_ruins.append(f"linha {i}: {n_serve}+{n_fora}")
ok(tabela is not None and not linhas_ruins,
   "[item 2] toda linha da tabela pre-renderizada soma os 5 do banco",
   "9 linhas" if not linhas_ruins else "; ".join(linhas_ruins))

# ---------------------------------------------------------------------------
# A PRESTACAO DE CONTAS DO BANCO, no HTML servido (bloco 3d, 12/09/2026).
#
# A frase do "Como sabemos" publica um total e a reparticao dele por categoria.
# Ela ja esteve errada nesta ilha ("hoje 10 dos 5 itens esperam link": dois
# numeros certos numa frase impossivel), e agora ela tem TRES parcelas em vez de
# duas. Duas coisas podem se separar sem ninguem ver: a soma pode deixar de bater
# com as parcelas, e uma categoria que ganhou arquivo de banco pode nao entrar na
# frase — item que a soma conta e a frase nao nomeia e prestacao de contas pela
# metade, que e o defeito que o despacho de 12/09 fechou nas ferramentas.
#
# A regua nao le a frase do snippet: le os ARQUIVOS de banco do repositorio,
# um a um, e cobra que a tela diga o que eles dizem.
print("\nA prestacao de contas do banco, no ar:")

_dados = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dados")
_por_categoria = {}
for _nome in sorted(os.listdir(_dados)):
    if _nome.startswith("materiais-") and _nome.endswith(".json"):
        with open(os.path.join(_dados, _nome), encoding="utf-8") as _fh:
            _b = json.load(_fh)
        _por_categoria[_b["categoria"]] = len(_b["materiais"])
_total_banco = sum(_por_categoria.values())

html_m, _ = buscar(BASE + "/materiais/")
_frase = re.search(r"Hoje o banco tem (.{0,240}?)esperam link de loja", re.sub(r"<[^>]+>", "", html_m), re.S)
_texto = re.sub(r"\s+", " ", _frase.group(1)) if _frase else ""
_nums = [int(x.replace(".", "")) for x in re.findall(r"(\d[\d.]*)", _texto)]

ok(_frase is not None, "a frase do total do banco esta na pagina servida", _texto[:80])
ok(bool(_nums) and _nums[0] == _total_banco,
   "o total servido e a soma dos arquivos de banco do repositorio",
   f"tela {_nums[0] if _nums else '-'} / repositorio {_total_banco}")
# Esta afirmacao NAO repete a de cima: ali a tela e comparada com o repositorio,
# aqui a frase e comparada CONSIGO MESMA. Uma frase pode estar internamente certa
# e desatualizada, e pode estar atualizada no total e errada na reparticao — sao
# dois defeitos diferentes, e foi o segundo que pos no ar "hoje 10 dos 5 itens".
ok(len(_nums) >= 3 and sum(_nums[1:-1]) == _nums[0],
   "as parcelas nomeadas na frase somam o total que a propria frase publica",
   f"{' + '.join(str(n) for n in _nums[1:-1])} = {_nums[0] if _nums else '-'}")
_faltando = [c for c in _por_categoria if c not in _texto and c + "s" not in _texto]
ok(not _faltando,
   "toda categoria com arquivo de banco e NOMEADA na frase",
   "nenhuma faltando" if not _faltando else "faltou: " + ", ".join(_faltando))
ok(len(_nums) >= 2 and _nums[-1] == sum(
       json.load(open(os.path.join(_dados, n), encoding="utf-8"))["afiliado"]["itens_esperando_link"]
       for n in sorted(os.listdir(_dados)) if n.startswith("materiais-") and n.endswith(".json")),
   "o numero de itens esperando link servido bate com os cabecalhos do banco",
   f"tela {_nums[-1] if _nums else '-'}")

print("\nA imagem, no ar:")
for rot, url in [("original (src)", LOGO),
                 ("-300x200 (srcset)", LOGO.replace(".png", "-300x200.png")),
                 ("-768x512 (srcset)", LOGO.replace(".png", "-768x512.png"))]:
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{size_download} %{content_type}",
                        "--max-time", "40", url], capture_output=True, text=True)
    codigo, tam, tipo = r.stdout.split(" ")
    ok(codigo == "200" and tipo.startswith("image/png"),
       f"{rot} responde PNG", f"{codigo} · {int(tam)//1024} KB · {tipo}")

print(f"\n{'APROVADO' if falhas == 0 else 'REPROVADO'}: {feitos} afirmacoes medidas no HTML servido, {falhas} falha(s).")
sys.exit(1 if falhas else 0)

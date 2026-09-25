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

# A ETIQUETA DE ROBO SE MEDE PELA DIRETIVA E PELA CONTAGEM, NUNCA PELA ASPA.
# Ate 25/09/2026 quatro afirmacoes deste arquivo procuravam a frase literal com
# ASPAS DUPLAS — as do `echo` que os snippets faziam. Duas delas (as do estado
# com parametro) reprovaram codigo CERTO no dia em que quem imprime virou o
# `wp_robots()` do nucleo, que usa aspas simples; as outras duas (as das
# ancoras) passavam A VAZIO, porque `'name="robots"' not in html` e verdade em
# toda pagina que use aspas simples — inclusive numa que saisse com `noindex`
# por engano. Regua de pontuacao reprova o conserto e aprova o desastre.
RE_ROBOTS = re.compile(r"<meta[^>]*name=[\"']robots[\"'][^>]*>", re.I)


def robots_de(html):
    """As etiquetas de robo do HTML servido, na ordem em que aparecem."""
    return RE_ROBOTS.findall(html)


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
    """(com ficha, sem ficha) somados nas categorias pedidas, lidos do repositorio."""
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
    """A PERGUNTA MUDOU EM 14/09/2026, e a antiga exigia o que a secao 7 proibiu.

    Ela pedia a etiqueta "link de loja em breve" na tela sempre que houvesse item
    sem ficha no banco — era a forma certa de medir enquanto reservar o lugar com
    uma promessa era o comportamento correto. A secao 7 do contrato proibiu a
    frase em 14/09, e a ilha passou a servir a busca crua no lugar dela. Entao o
    que se mede agora e o que a regra sempre quis dizer: quem chega no cartao tem
    para onde ir, e a pagina nao promete nada.
    """
    com, sem = _conta_links(categorias)
    if "Link de loja em breve" in corpo or "cdm-f2-sem-loja" in corpo:
        return False          # a frase proibida esta na tela
    if com > 0 and 'rel="sponsored' not in corpo:
        return False          # ha ficha no banco e a pagina nao a serve
    if sem > 0 and "cdm-f2-botao-busca-crua" not in corpo and 'rel="sponsored' not in corpo:
        return False          # ha item sem ficha e nenhuma saida de compra na tela
    return com > 0 or sem > 0


def _diagnostico_do_link(corpo, categorias):
    com, sem = _conta_links(categorias)
    botoes = corpo.count('rel="sponsored')
    cruas = corpo.count("cdm-f2-botao-busca-crua")
    breves = corpo.count("Link de loja em breve")
    return "banco: %d com ficha, %d sem | tela: %d patrocinados, %d buscas cruas, %d 'em breve'" % (
        com, sem, botoes, cruas, breves)


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
    """(com ficha e piso, so piso, so busca crua, sem nada) lidos do repositorio.

    O QUARTO NUMERO NASCEU EM 14/09/2026 e o quarto degrau com ele: `sem_nada`
    contava, junto, quem nao tinha NADA e quem tinha a busca CRUA. Enquanto a
    tela nao lia `url_busca_produto` os dois eram a mesma coisa na pratica — os
    dois viam a etiqueta proibida. Deixados juntos depois da f2 1.5.0, a regua
    aprovaria uma pagina sem saida de compra por engano.
    """
    ficha_e_piso = so_piso = so_crua = sem_nada = 0
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
            elif af.get("url_busca_produto") and not af.get("url"):
                so_crua += 1
            elif not af.get("url"):
                sem_nada += 1
    return ficha_e_piso, so_piso, so_crua, sem_nada


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
    ficha_e_piso, so_piso, so_crua, sem_nada = _conta_escada(categorias)
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

    # A SECAO 7 PROIBIU A FRASE EM 14/09/2026, e a afirmacao virou absoluta: ela
    # nao pode existir com banco nenhum, em pagina nenhuma. O que sobrou da
    # pergunta antiga — todo cartao tem para onde mandar quem quer comprar? — se
    # mede contando LINKS dentro do bloco de compra, nunca promessas.
    ok("Link de loja em breve" not in corpo and "cdm-f2-sem-loja" not in corpo,
       "[%s] secao 7: a frase 'link de loja em breve' NAO esta na tela" % rotulo)
    sem_saida_na_tela = []
    for c in cartoes:
        bloco = re.search(r'<span class="cdm-f2-compra">(.*?)</span>\s*<span class="cdm-f2-fonte"', c, re.S)
        if not bloco or not re.search(r"<a\b", bloco.group(1)):
            sem_saida_na_tela.append(c[:80])
    ok(not sem_saida_na_tela,
       "[%s] secao 7: TODO cartao servido tem uma saida de compra clicavel" % rotulo,
       "%d cartoes, %d sem saida" % (len(cartoes), len(sem_saida_na_tela)))
    ok(sem_nada == 0,
       "[%s] o banco desta pagina nao tem item sem NENHUMA saida de compra" % rotulo,
       "%d sem saida no banco" % sem_nada)
    # O REL SAI DO QUE O LINK E: a busca crua nao rende comissao, entao ela e
    # nofollow e nunca sponsored. Medido no HTML servido, nao no codigo.
    cruas = re.findall(r'<a\b[^>]*cdm-f2-botao-busca-crua[^>]*>', corpo)
    erradas = [t for t in cruas if 'rel="nofollow' not in t or "sponsored" in t]
    ok(not erradas,
       "[%s] a busca CRUA servida sai nofollow e nunca sponsored" % rotulo,
       "%d cruas na tela, %d erradas" % (len(cruas), len(erradas)))
    ok(len(cartoes) <= ficha_e_piso + so_piso + so_crua + sem_nada,
       "[%s] a tela nao serve mais cartao do que o banco sustenta" % rotulo,
       "%d na tela, %d no banco" % (len(cartoes), ficha_e_piso + so_piso + so_crua + sem_nada))

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
_r_f2 = robots_de(html_f2)
ok(len(_r_f2) == 1, "[F2] a ancora serve UMA etiqueta de robo", f"{len(_r_f2)}")
ok(len(_r_f2) == 1 and "noindex" not in _r_f2[0].lower(),
   "[F2] a ancora nao sai com noindex", " | ".join(_r_f2)[:60])
ok('"@type":"WebApplication"' in html_f2.replace(" ", ""), "[F2] JSON-LD WebApplication servido")
ok('"@type":"FAQPage"' in html_f2.replace(" ", ""), "[F2] JSON-LD FAQPage servido")
ok(_reserva_ou_entrega(corpo_f2, ("cola", "rejunte")),
   "[F2] o bloco de compra reserva o lugar do link OU serve o link, conforme o banco",
   _diagnostico_do_link(corpo_f2, ("cola", "rejunte")))
_escada_na_tela(corpo_f2, ("cola", "rejunte"), "F2")

for consulta, tem_que_recomendar, nao_pode_recomendar in F2_CASOS:
    html_c, codigo_c = buscar(BASE + F2 + "?" + consulta)
    ok("200" == codigo_c, f"[F2 {consulta}] responde 200", codigo_c)
    _rc = robots_de(html_c)
    ok(len(_rc) == 1, f"[F2 {consulta}] serve UMA etiqueta de robo", f"{len(_rc)}")
    ok(len(_rc) == 1 and "noindex" in _rc[0].lower(),
       f"[F2 {consulta}] estado com parametro sai com noindex", " | ".join(_rc)[:60])
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

# ---------------------------------------------------------------------------
# A FAIXA DESCOBERTA NO AR — 13/09/2026, e ela nasce porque as 390 afirmacoes
# desta ferramenta passaram VERDES depois do desembarque sem tocar uma linha do
# que mudou. E a cicatriz da robometria de 13/09 ("331 afirmacoes verdes que nao
# medem a mudanca") acontecendo aqui: nenhum dos F2_CASOS acima e uma celula SEM
# recomendacao, entao nenhum deles nunca leu a frase que este bloco consertou.
#
# A REGUA E DESTE ARQUIVO. O nome do produto e o tipo do documento estao
# escritos LITERAIS abaixo, copiados da fonte do Loctite Durepoxi — ler o banco
# aqui seria conferir a pagina com o mesmo arquivo que a monta.
#
# OS QUATRO ESTADOS, e por que sao quatro e nao um: as tres primeiras linhas sao
# as bases em que o epoxi declara a base E a imersao (procedencia), e a quarta e
# o estado NEGATIVO, sem o qual as outras tres tem porta dos fundos — em espelho
# dentro da agua ninguem declarou nada, e ali a pagina TEM de dizer que ninguem
# declarou. Sem o negativo, uma pagina que servisse a frase da procedencia em
# TODA faixa descoberta passaria nas tres primeiras.
DUREPOXI = "Loctite Durepoxi"
DOC_DUREPOXI = "material de imprensa do fabricante (2018)"
NEGA_A_DECLARACAO = "Nenhum dos adesivos do nosso banco é declarado"
NEGA_NA_VITRINE = "nenhum produto do nosso banco passa no que o fabricante declara"
POR_PROCEDENCIA = "o motivo não é falta de declaração"

F2_DESCOBERTAS = [
    ("base=vidro&onde=contato_permanente_agua&caco=pastilha_vidro", "procedencia"),
    ("base=metal&onde=contato_permanente_agua&caco=pastilha_vidro", "procedencia"),
    ("base=alvenaria_tijolo&onde=contato_permanente_agua&caco=pastilha_vidro", "procedencia"),
    ("base=espelho&onde=contato_permanente_agua&caco=pastilha_vidro", "silencio"),
]

print("\nA faixa descoberta no ar — a pagina nomeia QUAL causa a segura:")
for consulta, causa in F2_DESCOBERTAS:
    html_d, codigo_d = buscar(BASE + F2 + "?" + consulta)
    ok("200" == codigo_d, f"[F2 {consulta}] responde 200", codigo_d)
    corpo_d = re.search(r"<main.*?</main>", html_d, re.S)
    corpo_d = corpo_d.group(0) if corpo_d else html_d
    texto_d = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo_d))
    ok("Não temos cola para indicar" in texto_d,
       f"[F2 {consulta}] a faixa descoberta e declarada, nunca deixada em branco")
    if causa == "procedencia":
        ok(NEGA_A_DECLARACAO not in texto_d,
           f"[F2 {consulta}] a resposta NAO nega a declaracao que a propria pagina cita")
        ok(NEGA_NA_VITRINE not in texto_d,
           f"[F2 {consulta}] a vitrine vazia tambem NAO nega essa declaracao")
        ok(POR_PROCEDENCIA in texto_d,
           f"[F2 {consulta}] a recusa nomeia a causa medida: procedencia, nao silencio")
        ok(DUREPOXI in texto_d, f"[F2 {consulta}] a recusa nomeia o produto que declarou")
        ok(DOC_DUREPOXI in texto_d,
           f"[F2 {consulta}] e cita o documento que a sustenta, com o ano")
    else:
        ok(NEGA_A_DECLARACAO in texto_d,
           f"[F2 {consulta}] silencio de verdade: a pagina diz que ninguem declara")
        ok(POR_PROCEDENCIA not in texto_d,
           f"[F2 {consulta}] e NAO usa a frase da procedencia, que aqui seria falsa")

# A tabela pre-renderizada da cola serve a grade INTEIRA de base x lugar. O 45
# nao e digitado: e o produto dos dois vocabularios, contado do esquema em disco.
_esq = json.load(open(os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "dados", "esquema-banco.json"), encoding="utf-8"))
_grade_inteira = len(_esq["vocabularios"]["base"]) * len(_esq["vocabularios"]["ambiente"])
_tab_cola = re.search(r'<table class="cdm-f2-tabela">(.*?)</table>', corpo_f2, re.S)
_linhas_cola = len(re.findall(r"<tr>", _tab_cola.group(1))) - 1 if _tab_cola else 0
ok(_linhas_cola == _grade_inteira,
   f"[F2] a tabela pre-renderizada serve a grade inteira de base x lugar ({_grade_inteira} linhas)",
   f"{_linhas_cola} linhas no HTML servido")

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
_r_f1 = robots_de(html_f1)
ok(len(_r_f1) == 1, "[F1] a ancora serve UMA etiqueta de robo", f"{len(_r_f1)}")
ok(len(_r_f1) == 1 and "noindex" not in _r_f1[0].lower(),
   "[F1] a ancora nao sai com noindex", " | ".join(_r_f1)[:60])
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
bloco_p20 = re.search(r"<div class=\"cdm-f1-secao cdm-f1-vitrine-pastilha\">(.*?)(?=<div class=\"cdm-f1-secao|</main>)",
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
   "[F1 2 cm] todo cartao de pastilha tem bloco de compra")
# ESTA LINHA JA MUDOU DE OBJETO DUAS VEZES, e as tres versoes contam o MESMO
# numero medindo coisas diferentes — por isso ela fica, com a historia junto:
#
#  - ate 14/09/2026 contava etiquetas "Link de loja em breve", uma por
#    elegivel, e estava certa: os treze itens de pastilha nao tinham saida
#    nenhuma;
#  - de 14/09 a 25/09 contava BOTOES DE BUSCA CRUA — a promessa proibida pela
#    secao 7 trocada pela saida de compra que ela exige, mas uma saida que nao
#    rende comissao;
#  - desde 25/09/2026 conta o botao da busca ENCURTADA, com `rel="sponsored"`,
#    que e o mesmo piso rendendo. Os treze links nasceram nesse dia, pela Open
#    API (25.6), e o que os segurava era um motivo de 13/09 dizendo que o
#    encurtamento exigia sessao do painel — verdade naquele dia, falsa desde
#    16/09 (25.4-b.3).
#
# E O BOTAO CRU TEM DE TER SUMIDO, nao so o encurtado aparecido: enquanto os
# dois puderem conviver na mesma tela, um item com piso nao rastreavel passa
# escondido atras do vizinho que tem.
ok(bloco_p20.count('cdm-f2-botao-busca"') == len(DE_2CM)
   and bloco_p20.count("cdm-f2-botao-busca-crua") == 0
   and "Link de loja em breve" not in bloco_p20,
   "[F1 2 cm] cada cartao de pastilha serve a busca ENCURTADA como botao, zero crua, nenhum promete",
   "%d encurtadas e %d cruas para %d elegiveis"
   % (bloco_p20.count('cdm-f2-botao-busca"'),
      bloco_p20.count("cdm-f2-botao-busca-crua"), len(DE_2CM)))
# 25.2-b: o botao que rende comissao e um link patrocinado, e isso e exigencia
# de divulgacao, nao detalhe de markup.
ok(bloco_p20.count('rel="sponsored') >= len(DE_2CM),
   "[F1 2 cm] todo botao de compra da vitrine sai como link patrocinado",
   "%d rel=sponsored para %d elegiveis" % (bloco_p20.count('rel="sponsored'), len(DE_2CM)))
# A PORTA DO CAQUINHO IRREGULAR, que e a decisao desta versao sobre os cinco
# itens cujo lado o seletor nao lista.
ok("caquinho irregular" in re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloco_p20)),
   "[F1 2 cm] a pagina manda ao caquinho irregular quem quer o lado que o seletor nao lista")
html_ir, codigo_ir = buscar(BASE + F1 + "?forma=cilindro&d=15&h=20&pastilha=irregular&ladoeq=3&junta=2&sobra=10&esp=4&rejunte=cimenticio")
bloco_ir = re.search(r"<div class=\"cdm-f1-secao cdm-f1-vitrine-pastilha\">(.*?)(?=<div class=\"cdm-f1-secao|</main>)",
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

# A ORDEM DAS DUAS VITRINES NO HTML SERVIDO (f1 1.3.0).
#
# A bancada mede isto em quinze estados; aqui a medicao e outra e nao substitui
# aquela: o que ela prova e que a ORDEM sobreviveu ao caminho — o Sync, o
# the_content e o cache de borda —, no HTML que a pessoa e o modelo de linguagem
# recebem. Foi por nao medir o HTML servido que esta ilha publicou um '</p>'
# orfao na galeria em 14/09/2026 com o portao verde.
#
# O marcador e a fronteira, e nao o titulo: o titulo do rejunte muda no estado
# degradado, e regua presa a texto de titulo morre calada no dia em que ele muda.
for consulta_o, rotulo_o in [("", "ancora"),
                             ("?pastilha=p20", "2 cm"),
                             ("?rejunte=epoxi", "epoxi (a pagina recusa o grama)")]:
    html_o, codigo_o = buscar(BASE + F1 + consulta_o)
    corpo_o = re.search(r"<main.*?</main>", html_o, re.S)
    corpo_o = corpo_o.group(0) if corpo_o else html_o
    marca_o = f"[F1 ordem {rotulo_o}]"
    ok("200" == codigo_o, f"{marca_o} responde 200", codigo_o)
    n_past_o = corpo_o.count("cdm-f1-vitrine-pastilha")
    n_rej_o = corpo_o.count("cdm-f1-vitrine-rejunte")
    ok(n_past_o == 1 and n_rej_o == 1,
       f"{marca_o} as duas vitrines declaram o marcador, uma vez cada",
       f"pastilha {n_past_o}, rejunte {n_rej_o}")
    if n_past_o == 1 and n_rej_o == 1:
        p_past_o = corpo_o.index("cdm-f1-vitrine-pastilha")
        p_rej_o = corpo_o.index("cdm-f1-vitrine-rejunte")
        p_resp_o = corpo_o.find("cdm-f1-resposta")
        p_prova_o = corpo_o.find("cdm-prova")
        ok(p_past_o < p_rej_o,
           f"{marca_o} a vitrine de PASTILHA vem antes da de rejunte no HTML servido")
        ok(-1 < p_resp_o < p_past_o,
           f"{marca_o} 22.2: a resposta continua antes das duas vitrines")
        ok(p_prova_o > p_rej_o,
           f"{marca_o} secao 7: as DUAS vitrines vem antes da camada de prova")
    # O TITULO NAO DEPENDE DA POSICAO: o "E" de "E onde comprar a pastilha" era
    # conector, e conector num titulo e uma frase que mente quando a ordem muda.
    ok("<h2>Onde comprar a pastilha</h2>" in corpo_o,
       f"{marca_o} o titulo da pastilha e autossuficiente, sem o conector")
    ok("<h2>E onde comprar a pastilha</h2>" not in corpo_o,
       f"{marca_o} e o titulo antigo, que dependia de vir em segundo lugar, sumiu do ar")

for consulta, area, pastilhas, gramas in F1_CASOS:
    html_c, codigo_c = buscar(BASE + F1 + "?" + consulta)
    ok("200" == codigo_c, f"[F1 {consulta[:28]}] responde 200", codigo_c)
    _rc = robots_de(html_c)
    ok(len(_rc) == 1, f"[F1 {consulta[:28]}] serve UMA etiqueta de robo", f"{len(_rc)}")
    ok(len(_rc) == 1 and "noindex" in _rc[0].lower(),
       f"[F1 {consulta[:28]}] estado com parametro sai com noindex", " | ".join(_rc)[:60])
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

# ---------------------------------------------------------------------------
# A REGRA 6 NO AR — bloco 3e, 13/09/2026.
#
# A regua e deste arquivo. Os ids dos dois produtos e as duas listas de
# porosidade estao escritos LITERAIS abaixo, copiados das declaracoes lidas na
# coleta, e NAO sao lidos do esquema: ler o esquema aqui seria conferir a regra
# com a propria regra, e a secao 8 do contrato ja cobrou essa conta tres vezes
# nesta fabrica. O unico numero que este bloco le do repositorio e o tamanho do
# banco, e ele o CONTA do arquivo.
# ---------------------------------------------------------------------------

print("\nA regra 6 (condicao de superficie), no ar:")

MAXX = "Tekbond Silicone Acético Maxx"
PL500 = "Cascola Adesivo de Montagem PL500 Interior"

# (base, caquinho, ambiente) -> o que a pagina TEM que dizer, e o que NAO pode.
REGRA6_CASOS = [
    # A faixa do plastico, os dois lados dela. As duas telas seriam identicas
    # byte a byte se a regra 6 nao existisse: e o par que prova que ela morde.
    ("plastico", "pastilha_ceramica", "interno_seco",
     [PL500, "somos nós, não ela"],
     ["Não temos cola para indicar"]),
    ("plastico", "pastilha_vidro", "interno_seco",
     ["o motivo não é falta de declaração", "voltaria a servir"],
     ["Nenhum dos adesivos do nosso banco é declarado"]),
    # A faixa da agua, e o limite dela dito no mesmo folego: aberta em ceramica,
    # fechada em vidro, porque 'ceramicas vitrificadas' e a unica superficie que
    # o fabricante do Maxx nomeia.
    ("ceramica_esmaltada_porcelana", "pastilha_vidro", "contato_permanente_agua",
     [MAXX],
     ["Não temos cola para indicar"]),
    ("vidro", "pastilha_vidro", "contato_permanente_agua",
     ["Não temos cola para indicar"],
     [MAXX, PL500]),
]

for base, caco, onde, precisa, proibido in REGRA6_CASOS:
    html_r, codigo_r = buscar(f"{BASE}{F2}?base={base}&caco={caco}&onde={onde}&junta=2")
    corpo_r = re.search(r"<main[^>]*>(.*?)</main>", html_r, re.S)
    texto_r = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo_r.group(1))) if corpo_r else ""
    # A LISTA DO "NAO SERVE" MEDE A REGIAO DA RECOMENDACAO, NUNCA O CORPO.
    # A primeira versao disto media o corpo e reprovou a pagina CERTA: em vidro
    # dentro da agua, o Maxx e o PL500 aparecem — na prestacao de contas, que e
    # onde a secao 7 EXIGE que eles apareçam, cada um com o motivo de nao estar
    # ali. Presenca do nome nao e recomendacao; quem decide e a regiao, e a
    # regiao e marcada no markup. Mesmo erro de contar &#038; na pagina inteira.
    reg = re.search(r'<div class="cdm-f2-resposta">(.*?)<div class="cdm-f2-secao cdm-f2-fora"', html_r, re.S)
    if reg is None:
        reg = re.search(r'<div class="cdm-f2-resposta">(.*?)<div class="cdm-f2-secao"', html_r, re.S)
    bruto_rec = reg.group(1) if reg else ""
    # o bloco de recusa mora dentro da resposta e nomeia produto para dizer que
    # ele NAO foi indicado: sai daqui, pelo mesmo motivo e pela mesma marcacao.
    bruto_rec = re.sub(r'<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>', " ", bruto_rec, flags=re.S)
    texto_rec = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bruto_rec))
    marca = f"[regra 6 {base[:9]}/{caco[:9]}/{onde[:9]}]"
    ok("200" == codigo_r, f"{marca} responde 200", codigo_r)
    ok(texto_rec.strip() != "", f"{marca} a regiao da recomendacao foi encontrada para medir")
    for frase in precisa:
        ok(frase in texto_r, f"{marca} serve: {frase[:44]}")
    for frase in proibido:
        alvo = texto_rec if frase not in ("Não temos cola para indicar",) else texto_r
        ok(frase not in alvo, f"{marca} NAO recomenda: {frase[:40]}")

# A contagem do que falta, recontada aqui pelo tamanho do vocabulario — que e
# aritmetica e nao depende de elegibilidade nenhuma. Se a pagina publicar um
# total menor, ela esta falando de um recorte da entrada com cara de entrada
# inteira, que e a afirmacao com escopo maior do que o medido ao contrario.
_esq = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                   "dados", "esquema-banco.json"), encoding="utf-8"))
_total_esperado = (len(_esq["vocabularios"]["base"]) * len(_esq["vocabularios"]["ambiente"])
                   * len(_esq["vocabularios"]["material_tessela"]))
html_a, codigo_a = buscar(f"{BASE}{F2}")
_m = re.search(r"O que a gente ainda não responde</h2>(.*?)</div>", html_a, re.S)
_txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", _m.group(1))) if _m else ""
ok(_txt != "", "a pagina no ar serve a secao do que ela ainda nao responde")
ok(f"{_total_esperado} combinações" in _txt,
   "o total publicado bate com o vocabulario contado do repositorio",
   f"{_total_esperado} esperado")
_sem = re.search(r"Em ([\d.]+) delas", _txt)
ok(_sem is not None and 0 < int(_sem.group(1).replace(".", "")) < _total_esperado,
   "o numero de faixas sem resposta e publicado e nao e vacuidade",
   (_sem.group(1) if _sem else "-") + f" de {_total_esperado}")

# A tabela pre-renderizada e a metade que um modelo de linguagem le sem
# preencher formulario. A coluna da condicao tem de estar LA, servida no HTML.
ok("Com que condição" in html_a,
   "a tabela pre-renderizada publica a coluna da condicao no HTML servido")
ok("ao menos uma das superfícies deve ser porosa" in html_a,
   "e a condicao literal do fabricante aparece servida, nao resumida")

# O banco cresceu e a tela tem de dizer o numero CONTADO do arquivo.
_colas = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                     "dados", "materiais-colas.json"), encoding="utf-8"))
_n_colas = len([m for m in _colas["materiais"] if m.get("status") == "ativo"])
ok(f">{_n_colas}<" in html_a or f" {_n_colas} colas" in re.sub(r"<[^>]+>", " ", html_a),
   "o numero de colas servido bate com o banco contado do arquivo", f"{_n_colas} colas")

# ---------------------------------------------------------------------------
# O CACHE DO HOSPEDEIRO — e o que esta ilha MEDIU em 14/09/2026, que nao e o que
# o despacho supunha.
#
# O despacho de prioridade ALTA da Fundacao, aberto na Robometria, manda quem
# pegar esta ilha por o endereco canonico contra o mesmo endereco com quebra de
# cache antes de dar bloco por entregue. Feito, e o resultado tem duas metades:
#
#   1. A ENTREGA ESTA CERTA. Com quebra de cache — que e o que a ORIGEM serve —
#      as marcas do bloco aparecem inteiras.
#   2. A PURGA SO VALE A PARTIR DO SEGUNDO SYNC, e esta e a medicao que vale
#      para TODA ilha. A casca que contem a purga faz parte da carga que esta
#      sendo entregue: no Sync que a instala, o PHP ja carregado e o ANTERIOR, e
#      por isso nenhuma purga roda. Medido aqui, minuto a minuto, em 14/09/2026:
#      18h29 o Sync da revisao 32 aplicou com a casca 1.9.2 na memoria e o
#      canonico continuou servindo entradas de 17h36Z (e a home, uma de 13h53Z,
#      do bloco ANTERIOR — velha havia cinco horas sem ninguem ver); 18h34 um
#      SEGUNDO Sync, ja com a 1.10.0 carregada; poucos minutos depois o canonico
#      passou a servir o bloco novo em todas as paginas, com `x-proxy-cache`
#      voltando a HIT sobre a copia NOVA e zero ocorrencia da frase proibida nas
#      onze URLs. As duas camadas existem e foram medidas pelos cabecalhos:
#      `x-server-cache: true` e `x-proxy-cache`, nginx, `max-age=7200`.
#
# POR ISSO A AFIRMACAO REPROVA PELA ORIGEM E RELATA O CANONICO. Fazer o canonico
# reprovar transformaria toda entrega em duas horas de portao vermelho que
# ninguem consegue fechar — e portao assim se aprende a ignorar, que e pior do
# que nao ter portao. O que e defeito de verdade e a ORIGEM nao servir o bloco;
# o canonico velho e janela de cache, e ela e relatada com a hora da entrada e a
# da expiracao, para a proxima execucao saber se esta vendo a janela ou uma
# entrega perdida.
#
# E O METODO IMPORTA, porque foi ele que enganou a execucao que abriu o despacho:
# comparar cabecalho de HEAD com corpo de GET, em requisicoes diferentes,
# condenou uma purga que funcionava. Aqui as duas leituras sao GET do CORPO e o
# que se compara sao MARCADORES do bloco — nunca o md5 da pagina, que difere por
# ruido legitimo (o proprio parametro de quebra ecoa no `action` do formulario).
# ---------------------------------------------------------------------------
print("\nO cache do hospedeiro — a origem contra o canonico (despacho de 14/09):")

_QUEBRA = str(int(time.time()))
# Os marcadores deste bloco: o que a revisao 32 mudou e que so existe depois dela.
_MARCADORES = {
    "/materiais/quantas-pastilhas-para-mosaico/?forma=disco&d=50&pastilha=p20&esp=6&sobra=15&rejunte=cimenticio":
        # O MARCADOR TROCOU EM 25/09/2026 com o bloco que ele mede: a vitrine
        # deixou de servir o botao CRU e passou a servir o ENCURTADO. O par
        # classe+dominio e o marcador estavel — o codigo do encurtador muda a
        # cada regeracao e viraria uma regua que apodrece sozinha.
        ['cdm-f2-botao-busca" href="https://s.shopee.com.br/'],
    "/divulgacao-de-afiliados/": ["Nem todo link daqui rende comiss"],
}


def _cabecalhos(url):
    r = subprocess.run(["curl", "-s", "-D", "-", "-o", "/dev/null", "--max-time", "40", url],
                       capture_output=True, text=True)
    fora = {}
    for linha in r.stdout.splitlines():
        if ":" in linha:
            chave, _, valor = linha.partition(":")
            fora[chave.strip().lower()] = valor.strip()
    return fora


for caminho, marcas in _MARCADORES.items():
    junta = "&" if "?" in caminho else "?"
    origem, cod_o = buscar(BASE + caminho + junta + "v=" + _QUEBRA)
    canonico, cod_c = buscar(BASE + caminho)
    ok(cod_o == "200" and cod_c == "200",
       "[cache] as duas leituras de %s respondem 200" % caminho.split("?")[0],
       "origem %s e canonico %s" % (cod_o, cod_c))
    for marca in marcas:
        ok(marca in origem,
           "[cache] a ORIGEM serve o marcador deste bloco: %s" % marca[:44])
        if marca not in canonico:
            cab = _cabecalhos(BASE + caminho)
            ok(True,
               "[cache] o canonico ainda serve a copia anterior — JANELA, nao entrega perdida",
               "%s | proxy %s | entrada de %s | expira %s" % (
                   caminho.split("?")[0], cab.get("x-proxy-cache", "-"),
                   cab.get("last-modified", "-"), cab.get("expires", "-")))
        else:
            ok(True, "[cache] o canonico ja serve o bloco novo", caminho.split("?")[0])

# A CAMADA QUE ESTA NA FRENTE, medida e registrada em vez de suposta: saber QUAL
# ela e o que separa "purgamos" de "achamos que purgamos". A assinatura do
# Endurance no HTML e o `x-proxy-cache` do nginx sao duas leituras da mesma
# entrega, e as duas mudaram juntas depois do segundo Sync.
_cab_home = _cabecalhos(BASE + "/")
_home, _ = buscar(BASE + "/")
ok(True, "[cache] as camadas na frente da home (registro, nunca portao)",
   "EPC no HTML: %s | x-proxy-cache: %s | x-server-cache: %s | entrada de %s" % (
       "sim" if "Endurance Page Cache" in _home else "nao",
       _cab_home.get("x-proxy-cache", "-"), _cab_home.get("x-server-cache", "-"),
       _cab_home.get("last-modified", "-")))

print("\nA imagem, no ar:")
for rot, url in [("original (src)", LOGO),
                 ("-300x200 (srcset)", LOGO.replace(".png", "-300x200.png")),
                 ("-768x512 (srcset)", LOGO.replace(".png", "-768x512.png"))]:
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{size_download} %{content_type}",
                        "--max-time", "40", url], capture_output=True, text=True)
    codigo, tam, tipo = r.stdout.split(" ")
    ok(codigo == "200" and tipo.startswith("image/png"),
       f"{rot} responde PNG", f"{codigo} · {int(tam)//1024} KB · {tipo}")

# ---------------------------------------------------------------------------
# A PORTA DE ENTRADA DO SITE. Acrescentado em 24/09/2026, no dia em que 16 das
# 17 URLs desta ilha serviam a pagina de estacionamento da HostGator com 404 e
# nenhum portao do repositorio acusou nada por nove dias.
#
# Este arquivo TERIA acusado, e vale dizer por que: `buscar()` gruda uma quebra
# de cache em toda URL, entao toda leitura dele e uma URL com query — que era
# exatamente a forma que morria. O que faltava nao era sensibilidade, era
# alguem rodar: a ilha passou de 15/09 a 24/09 sem bloco.
#
# O QUE ELE NAO COBRIA, e e o que entra aqui: as tres URLs que o Google usa e
# que nenhuma pagina desta ilha linka — `wp-sitemap.xml`, `robots.txt` e a raiz
# do REST. Elas nao sao pagina, nao tem marca, nao tem canonico, e por isso
# ficaram de fora de todas as afirmacoes acima. Sao tambem as PRIMEIRAS a cair
# quando o roteamento de permalink some, porque nao existem como arquivo em
# disco — sao rota virtual do WordPress e dependem inteiramente da reescrita.
#
# O 404 QUE TEM DE SER 404 esta aqui de proposito: um portao que so cobra 200
# aprova um servidor que responde 200 para tudo, e "tudo responde" e um jeito
# conhecido de uma ilha inteira sair do indice sem ninguem ver.
print("\nA porta de entrada (roteamento de permalink):")

for caminho, tipo_esperado, rotulo in [
    ("/wp-sitemap.xml", "xml", "o sitemap responde"),
    ("/robots.txt", "text/plain", "o robots.txt responde"),
    ("/wp-json/", "json", "a raiz do REST responde"),
]:
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{content_type}",
                        "--max-time", "40", BASE + caminho], capture_output=True, text=True)
    partes = r.stdout.split(" ", 1)
    codigo = partes[0]
    tipo = partes[1] if len(partes) > 1 else ""
    ok(codigo == "200" and tipo_esperado in tipo,
       "[rota] " + rotulo, codigo + " " + tipo)

_sm, _cod_sm = buscar(BASE + "/wp-sitemap.xml")
ok("<sitemap>" in _sm or "<url>" in _sm,
   "[rota] o sitemap traz XML de sitemap, nao pagina do hospedeiro",
   _sm[:60].replace("\n", " "))

_lixo, _cod_lixo = buscar(BASE + "/caminho-que-esta-ilha-nunca-teve/")
ok(_cod_lixo == "404", "[rota] caminho inexistente responde 404", _cod_lixo)
ok("clubedomosaico" in _lixo.lower() or "Clube do Mosaico" in _lixo,
   "[rota] o 404 e a pagina DESTA ilha, nao a do hospedeiro",
   "HostGator" if "HostGator" in _lixo else "propria")

# ---------------------------------------------------------------------------
# O LINK DE AFILIADO SERVIDO E O DO BANCO. Acrescentado em 25/09/2026, no dia
# em que os 31 links de Shopee desta ilha foram REGERADOS porque os antigos
# tinham os `sub_id` deslocados uma casa (`-clubedomosaico-F2--`, campo 1
# vazio).
#
# O QUE ESTA AFIRMACAO PEGA, e e uma familia inteira: encurtador servido que o
# banco nao conhece. Depois de uma regeracao, o link velho so some da tela se o
# Sync tiver aplicado o dado novo — e "12 aplicado(s)" no log do Sync nao e
# evidencia de nada (secao 8). O link velho continua VIVO na Shopee, entao nada
# quebra e nada responde 404: a unica coisa que acontece e a ilha perder a
# atribuicao da venda, calada, que foi exatamente o defeito de 13/09 a 24/09.
#
# O QUE ELA NAO PEGA, dito para ninguem confiar de mais: a CASA do sub-id
# dentro do link. Isso nao se le do HTML — so do `utm_content` do 301 do
# encurtador, e esse salto e onde a Shopee conta o clique. Conferir os links
# desta ilha por ali gravaria um clique com o sub-id dela por link, justo na
# semana em que a leitura semanal procura o PRIMEIRO clique organico. Quem mede
# a casa e `ferramentas/conferir-sub-id.py`, na raiz do repositorio, com um
# link de BANCADA e sub-id de bancada. Aqui se mede a OUTRA metade: que o link
# na tela e o que o banco mandou.
print("\nO link de afiliado servido (25.6, sub_id na casa certa):")

_do_banco = set()
for _nome in sorted(os.listdir(_DADOS_DIR)):
    if not (_nome.startswith("materiais-") and _nome.endswith(".json")):
        continue
    with open(os.path.join(_DADOS_DIR, _nome), encoding="utf-8") as _fh:
        _banco = json.load(_fh)
    for _item in _banco.get("materiais", []):
        _af = _item.get("afiliado") or {}
        for _campo in ("url", "url_busca"):
            _u = _af.get(_campo) or ""
            if "s.shopee.com.br" in _u:
                _do_banco.add(_u)

_sm_indice, _ = buscar(BASE + "/wp-sitemap.xml")
_paginas = []
for _sub in re.findall(r"<loc>([^<]+)</loc>", _sm_indice):
    _corpo_sm, _ = buscar(_sub)
    _paginas += re.findall(r"<loc>([^<]+)</loc>", _corpo_sm)

_servidos = set()
for _pag in _paginas:
    _corpo, _cod = buscar(_pag)
    _servidos |= set(re.findall(r"https://s\.shopee\.com\.br/[A-Za-z0-9]+", _corpo))

_estranhos = sorted(_servidos - _do_banco)
ok(not _estranhos,
   "[afiliado] todo encurtador de Shopee servido esta no banco",
   "%d servido(s), %d estranho(s)%s" % (len(_servidos), len(_estranhos),
                                        (": " + ", ".join(_estranhos[:3])) if _estranhos else ""))
# Portao que nao encontra nada aprova por vacuidade, e e assim que um portao
# morre sem ninguem notar: se a tela parar de servir link, esta afirmacao cai.
ok(len(_servidos) > 0,
   "[afiliado] as paginas do sitemap servem pelo menos um encurtador",
   "%d" % len(_servidos))

# ---------------------------------------------------------------------------
# UMA ETIQUETA DE ROBO, E SO UMA. Acrescentado em 25/09/2026 pelo BLOCO B do
# despacho do Raphael de 24/09, que trouxe a licao da Aquametria com todas as
# letras: "NAO adicionar uma segunda meta robots (...) o caminho e o filtro,
# nunca uma tag em paralelo".
#
# O DEFEITO QUE ESTE PORTAO EXISTE PARA PEGAR JA ESTAVA NO AR quando ele
# nasceu, e nenhum portao daqui o via: `/materiais/como-sabemos/` servia DUAS
# <meta name="robots"> — a do nucleo (`max-image-preview:large`, aspas simples)
# e a da casca (`noindex, follow`, aspas duplas), injetada por um `wp_head`
# proprio. Todo portao anterior media SE a frase `noindex` aparecia; nenhum
# media QUANTAS etiquetas apareciam. Duas etiquetas com o mesmo nome sao um
# pedido ambiguo, e nada na tela muda de cor por causa disso.
#
# A REGUA E DAQUI, nao da casca: a contagem e por expressao regular sobre o
# HTML servido, e o veredito de cada URL esta escrito literal nesta lista. Se
# alguem declarar outra pagina `noindex` na casca, esta lista discorda — que e
# o ponto: as duas metades nao erram juntas.
#
# AS DUAS DIRECOES, porque so uma aprova o desastre: `noindex` indevido tira do
# indice a pagina que rankeia, e esta ilha tem TRES paginas na primeira pagina
# do Google. Entao o portao cobra a etiqueta onde ela tem de estar E a ausencia
# dela em toda URL do sitemap, lida do sitemap no ar e nao digitada aqui.
print("\nA etiqueta de robo (uma so, e nas paginas certas):")

def _robots_de(url):
    html, codigo = buscar(url)
    return codigo, robots_de(html)

# 1. As que TEM de sair do indice. `/author/` e o achado da Sentinela de 23/09:
#    200, sem etiqueta, fora do sitemap, sem link de lugar nenhum — e indexada,
#    servida na posicao 1,0. A busca interna e o mesmo buraco sem sintoma.
for _caminho, _rotulo in [
    ("/author/mosaico_gestor/", "o arquivo de autor"),
    ("/materiais/como-sabemos/", "a pagina de prova"),
    ("/?s=mosaico", "a busca interna"),
]:
    _cod, _achadas = _robots_de(BASE + _caminho)
    _conteudo = " | ".join(_achadas)
    ok(len(_achadas) == 1, f"[robots] {_rotulo} serve UMA etiqueta", f"{len(_achadas)} · {_conteudo[:70]}")
    ok(len(_achadas) == 1 and "noindex" in _achadas[0].lower(),
       f"[robots] {_rotulo} sai do indice", _conteudo[:70])
    ok(len(_achadas) == 1 and "follow" in _achadas[0].lower().replace("nofollow", ""),
       f"[robots] {_rotulo} mantem follow (a malha nao se corta)", _conteudo[:70])

# 1b. OS ESTADOS COM PARAMETRO DAS DUAS FERRAMENTAS. Sao eles que serviam DUAS
#     etiquetas ate 25/09/2026 — a do nucleo e a que o proprio snippet imprimia
#     num `wp_head` paralelo — e o estado com parametro de
#     `/materiais/qual-cola-usar-no-mosaico/` e da MELHOR pagina desta ilha.
#     Quem entra no indice e a ancora; o estado com parametro sai, e sai numa
#     etiqueta so.
for _caminho, _rotulo in [
    (F2 + "?base=espelho&onde=interno_seco", "o estado com parametro da F2"),
    ("/materiais/quantas-pastilhas-para-mosaico/?forma=vaso&caquinho=medio", "o estado com parametro da F1"),
]:
    _cod, _achadas = _robots_de(BASE + _caminho)
    ok(len(_achadas) == 1, f"[robots] {_rotulo} serve UMA etiqueta",
       f"{len(_achadas)} · {' | '.join(_achadas)[:60]}")
    ok(len(_achadas) == 1 and "noindex" in _achadas[0].lower(),
       f"[robots] {_rotulo} sai do indice", " | ".join(_achadas)[:60])

# As DUAS ancoras continuam NO indice — o lado caro da borda: `noindex` indevido
# tiraria do ar as paginas que rankeiam.
for _caminho, _rotulo in [
    (F2, "a ancora da F2 (posicao 7,8)"),
    ("/materiais/quantas-pastilhas-para-mosaico/", "a ancora da F1 (posicao 9,1)"),
]:
    _cod, _achadas = _robots_de(BASE + _caminho)
    ok(len(_achadas) == 1 and "noindex" not in _achadas[0].lower(),
       f"[robots] {_rotulo} CONTINUA no indice", " | ".join(_achadas)[:60])

# 2. O OUTRO LADO: toda URL do sitemap continua NO indice, e com uma etiqueta so.
#    A lista vem do sitemap servido — quem confere nao digita o inventario.
_sm_idx, _ = buscar(BASE + "/wp-sitemap.xml")
_urls_sitemap = []
for _sub in re.findall(r"<loc>([^<]+)</loc>", _sm_idx):
    _corpo, _ = buscar(_sub)
    _urls_sitemap += re.findall(r"<loc>([^<]+)</loc>", _corpo)

ok(len(_urls_sitemap) > 0, "[robots] o sitemap entregou a lista de URLs", f"{len(_urls_sitemap)} URLs")

_com_noindex, _duplicadas = [], []
for _u in _urls_sitemap:
    _cod, _achadas = _robots_de(_u)
    if len(_achadas) > 1:
        _duplicadas.append(_u)
    if _achadas and "noindex" in _achadas[0].lower():
        _com_noindex.append(_u)

ok(not _duplicadas, "[robots] nenhuma URL do sitemap serve DUAS etiquetas",
   f"{len(_urls_sitemap)} conferidas" + ((": " + ", ".join(_duplicadas[:2])) if _duplicadas else ""))
ok(not _com_noindex, "[robots] nenhuma URL do sitemap saiu do indice",
   f"{len(_urls_sitemap)} conferidas" + ((": " + ", ".join(_com_noindex[:2])) if _com_noindex else ""))

# 3. E o arquivo de autor continua FORA do sitemap — tirar do sitemap e tirar do
#    indice sao duas coisas, e esta ilha precisa das duas.
ok(not [_u for _u in _urls_sitemap if "/author/" in _u],
   "[robots] o arquivo de autor continua fora do sitemap", f"{len(_urls_sitemap)} URLs")

print(f"\n{'APROVADO' if falhas == 0 else 'REPROVADO'}: {feitos} afirmacoes medidas no HTML servido, {falhas} falha(s).")
sys.exit(1 if falhas else 0)

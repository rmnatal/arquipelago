#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede o que o SITE serve, e nao o que o repositorio guarda.

    python3 ferramentas/conferir-no-ar.py

Existe porque "aplicado com sucesso" no log do Sync nao e evidencia de nada
(secao 8 do ARQUIPELAGO.md) e porque commit sem verificacao no ar nao e entrega
(secoes 4 e 18.4). A bancada mede o HTML que a bancada monta; isto abre as nove
URLs com curl e afirma sobre o HTML SERVIDO.

A regua e deste arquivo, nao do snippet: a URL do logo e a medida 78x52 estao
escritas literais aqui, copiadas do despacho do Raphael de 11/09. Se alguem
trocar a constante da casca por outra imagem, as duas metades nao erram juntas.

O `?v=` em toda URL nao e enfeite: o raw.githubusercontent guarda ~5 min e o
cache de borda guarda mais, e sem ele se conclui que nada mudou (secao 4).
"""

import re, subprocess, sys, time

BASE = "https://clubedomosaico.com.br"
LOGO = "https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png"
PAGS = ["/", "/loja/", "/materiais/", "/materiais/como-sabemos/", "/como-fazer/",
        "/sobre/", "/contato/", "/divulgacao-de-afiliados/", "/privacidade/",
        "/materiais/qual-cola-usar-no-mosaico/"]

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

print("NO AR — o logo do Raphael no cabecalho das nove paginas\n")
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
ok("Link de loja em breve" in corpo_f2, "[F2] o bloco de compra reserva o lugar do link")

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

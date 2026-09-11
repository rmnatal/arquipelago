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
        "/sobre/", "/contato/", "/divulgacao-de-afiliados/", "/privacidade/"]

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

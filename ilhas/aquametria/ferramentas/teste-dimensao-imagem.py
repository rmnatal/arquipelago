#!/usr/bin/env python3
"""O PORTAO DA DIMENSAO DA IMAGEM — mede o par width/height no HTML SERVIDO das
quatro paginas que mostram foto de produto.

    python3 ferramentas/teste-dimensao-imagem.py .

POR QUE ELE NASCEU (item 3 do despacho da Sentinela de 13/09/2026): oito imagens
de produto saiam sem `width` e sem `height`. O renderizador estava certo — ele so
emite o par quando o registro tem os dois campos —, e o que faltava era DADO. A
Sentinela mediu as oito no Chrome (`naturalWidth` x `naturalHeight`), porque o
egresso desta nuvem barra `down-bs-br.img.susercontent.com` e continua barrando,
reconferido por curl em 13/09/2026.

O QUE ESTE PORTAO DECIDE, e que o despacho mandou decidir: o que acontece quando
o campo falta. A imagem CONTINUA sendo servida, sem o par, e isso nao e desleixo
— a caixa da foto e reservada pelo CSS (`aspect-ratio:1/1;width:100%`), entao a
pagina nao salta com ou sem os atributos, e este portao MEDE essa regra de CSS no
que e servido. Tirar a foto de um produto tecnicamente certo por falta de uma
medida seria trocar o certo pelo bonito ao contrario. O que fica proibido e o
SILENCIO: registro com imagem sem dimensao declara `motivo_sem_medida`, e
registro com dimensao declara `medida_em` e `medida_como` — as duas regras moram
no `validar-produtos.py` (V19), e este portao mede a outra ponta, o HTML.

COMO ELE FOI ESCRITO, e as cicatrizes da secao 8 que decidiram cada escolha:

  1. A REGUA LE O BANCO, e o banco e `dados/produtos-*.json`. Nada e importado do
     catalogo embutido no snippet — que e justamente a copia que pode divergir —
     nem do gerador que a produz. Comparar o snippet com o snippet ficaria verde
     com as duas metades erradas juntas.

  2. NENHUM NUMERO ESPERADO ESTA DIGITADO AQUI. Nem as oito medidas, nem "oito".
     Uma regua com o numero dentro reprovaria pagina certa na leva seguinte, que
     e o defeito que esta ilha cometeu com a data da SERP em 13/09/2026.

  3. A AFIRMACAO TEM AS DUAS DIRECOES. Imagem cujo registro tem o par serve o
     par com os numeros do banco; imagem cujo registro NAO tem o par nao serve
     atributo nenhum. So a primeira direcao deixaria passar dimensao inventada
     dentro do snippet — que e exatamente o erro que "800x800 porque foto de
     e-commerce costuma ser quadrada" cometeria, e nenhum validador de valor
     pegaria.

  4. O PORTAO PRODUZ O MUNDO que o banco nao tem mais: ele COPIA a ilha, apaga a
     dimensao de um registro medido, roda o gerador do catalogo e mede a pagina
     resultante. Sem isso, "a foto continua aparecendo sem o par" seria uma
     afirmacao sobre um caso que hoje nao existe em nenhuma das quatro paginas —
     verde sem poder falhar, e o dia em que importasse seria o dia da imagem
     nova.

  5. UMA PAGINA POR PROCESSO (ver render-pagina-completa.php).
"""

import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."

# Pagina -> gerador que reescreve o catalogo embutido dela. O mapa esta aqui, a
# mao, porque o mundo produzido (decisao 4) precisa rodar o gerador certo.
PAGINAS = {
    "calculadora-de-vazao-do-filtro": "gerar-catalogo-filtros.py",
    "calculadora-de-potencia-do-aquecedor": "gerar-catalogo-aquecedores.py",
    "calculadora-de-midia-filtrante": "gerar-catalogo-midias.py",
    "calculadora-de-iluminacao": "gerar-catalogo-iluminacao.py",
}

falhas = []
afirmacoes = 0


def ok(nome, condicao, detalhe=""):
    global afirmacoes
    afirmacoes += 1
    if condicao:
        print("  ok %s" % nome)
    else:
        falhas.append(nome)
        print("FALHA %s %s" % (nome, detalhe))


def banco_por_url(raiz):
    """url da imagem -> (id, largura, altura), lido do BANCO (decisao 1).

    Uma URL pode servir mais de um registro — dois anuncios da mesma linha
    reaproveitam o arquivo —, e nesse caso os registros precisam concordar sobre a
    dimensao, senao a pagina nao tem o que servir. O portao mede isso: e um
    conflito de banco que sairia como atributo errado na tela.
    """
    por_url = {}
    for arquivo in sorted(glob.glob(os.path.join(raiz, "dados", "produtos-*.json"))):
        d = json.load(open(arquivo, encoding="utf-8"))
        for p in d.get("produtos", []):
            img = p.get("imagem")
            if not img or not img.get("url"):
                continue
            par = (img.get("largura"), img.get("altura"))
            anterior = por_url.get(img["url"])
            if anterior and anterior[1] != par:
                ok("banco: a URL %s...%s tem dimensao unica entre os registros que a usam"
                   % (img["url"][:44], img["url"][-12:]),
                   False, "%s=%r contra %s=%r" % (anterior[0], anterior[1], p.get("id"), par))
            por_url.setdefault(img["url"], (p.get("id"), par))
    return por_url


def servir(raiz, slug):
    r = subprocess.run(
        ["php", os.path.join(raiz, "ferramentas", "render-pagina-completa.php"), raiz, slug],
        capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("render falhou em %s: %s" % (slug, r.stderr[-600:]))
    return r.stdout


def imgs_de_produto(pagina, urls):
    """Toda <img> servida cuja URL o banco conhece. Casar pela URL do banco, e
    nao por classe de CSS, e o que faz o portao nao depender do nome da classe
    que o desenho pode trocar."""
    achadas = []
    for tag in re.findall(r"<img\b[^>]*>", pagina):
        m = re.search(r'src="([^"]+)"', tag)
        if not m:
            continue
        url = m.group(1).replace("&#038;", "&").replace("&amp;", "&")
        if url in urls:
            achadas.append((url, tag))
    return achadas


def par_do_tag(tag):
    l = re.search(r'\bwidth="(\d+)"', tag)
    a = re.search(r'\bheight="(\d+)"', tag)
    return (int(l.group(1)) if l else None, int(a.group(1)) if a else None)


# ---------------------------------------------------------------------------
# 1. O MUNDO DE HOJE — as quatro paginas, nas duas direcoes (decisao 3)
# ---------------------------------------------------------------------------
URLS = banco_por_url(RAIZ)
print("\n== banco: %d URLs de imagem, %d com dimensao medida ==" % (
    len(URLS), sum(1 for _, par in URLS.values() if par[0] is not None)))

servidas = 0
com_par = 0
for slug in PAGINAS:
    pagina = servir(RAIZ, slug)
    achadas = imgs_de_produto(pagina, URLS)
    ok("%s: serve pelo menos uma foto de produto" % slug, bool(achadas),
       "nenhuma <img> do banco na pagina — o portao nao mediria nada")

    # A CAIXA E RESERVADA PELO CSS, e e isso que faz a imagem sem dimensao nao
    # saltar o layout. Medido no que a pagina SERVE, nao no repositorio.
    estilo = "".join(re.findall(r"<style[^>]*>(.*?)</style>", pagina, re.S))
    regra = re.search(r"\.aqm-c\d+-vt-foto\{([^}]*)\}", estilo)
    ok("%s: a caixa da foto reserva espaco no CSS servido" % slug,
       bool(regra) and "aspect-ratio:1/1" in regra.group(1)
       and "width:100%" in regra.group(1),
       "regra=%r" % (regra.group(1)[:120] if regra else None))

    for url, tag in achadas:
        pid, (bl, ba) = URLS[url]
        servidas += 1
        tl, ta = par_do_tag(tag)
        if bl is not None and ba is not None:
            com_par += 1
            ok("%s / %s: serve width e height iguais aos do banco" % (slug, pid),
               (tl, ta) == (bl, ba), "tela=%r banco=%r" % ((tl, ta), (bl, ba)))
        else:
            # A OUTRA DIRECAO: sem medida no banco, nao existe atributo na tela.
            ok("%s / %s: sem dimensao no banco, nao inventa atributo na tela" % (slug, pid),
               (tl, ta) == (None, None), "tela=%r" % ((tl, ta),))
        ok("%s / %s: a foto tem alt descritivo" % (slug, pid),
           bool(re.search(r'alt="[^"]{20,}"', tag)), "tag=%s" % tag[:140])

print("\n%d fotos de produto servidas nas quatro paginas, %d com o par" % (servidas, com_par))
ok("toda foto servida hoje carrega o par (nenhuma esperando medida nas quatro paginas)",
   servidas == com_par, "%d de %d" % (com_par, servidas))

# ---------------------------------------------------------------------------
# 2. O SCRIPT QUE PINTA OS OUTROS CARTOES — o par nunca sai pela metade
#
# A vitrine servida e so a metade que o crawler recebe; o comprador que mexe no
# formulario ve cartoes montados pelo script. As duas metades leem o MESMO
# catalogo, entao o valor ja esta medido acima; o que so aqui pode ser medido e a
# forma da atribuicao — `width` sozinho da ao navegador uma proporcao errada, que
# e pior do que nenhuma. Medido no script SERVIDO, nao no repositorio.
# ---------------------------------------------------------------------------
print("\n== o script servido nunca atribui metade do par ==")
for slug in PAGINAS:
    pagina = servir(RAIZ, slug)
    script = "".join(re.findall(r"<script\b[^>]*>(.*?)</script>", pagina, re.S))
    # A REGUA MEDE A INVARIANTE, NAO A FORMA DE ESCREVER. A primeira versao
    # procurava `img.width =` e a guarda com o nome de variavel `p`, e reprovou
    # duas paginas CERTAS: a C3 e a C5 montam o cartao por propriedade de DOM, a
    # C12 e a C15 por string de HTML, e a C12 chama o item de `m` em vez de `p`.
    # Regua colada numa implementacao reprova a outra implementacao correta — e
    # no dia em que a terceira forma aparecer, reprovaria ela tambem.
    usos_l = len(re.findall(r"\.imagem\.largura\b", script))
    usos_a = len(re.findall(r"\.imagem\.altura\b", script))
    ok("%s: o script cita largura e altura o mesmo numero de vezes" % slug,
       usos_l == usos_a and usos_l > 0, "largura=%d altura=%d" % (usos_l, usos_a))
    juntas = len(re.findall(r"\.imagem\.largura\s*&&\s*\w+\.imagem\.altura", script))
    ok("%s: e as duas so entram JUNTAS, sob a mesma condicao" % slug, juntas > 0,
       "nenhuma conjuncao largura && altura no script servido")

# ---------------------------------------------------------------------------
# 3. O MUNDO PRODUZIDO — a imagem que ninguem mediu ainda (decisao 4)
# ---------------------------------------------------------------------------
print("\n== mundo produzido: um registro medido volta a nao ter dimensao ==")
ALVO_PAGINA = "calculadora-de-vazao-do-filtro"
with tempfile.TemporaryDirectory() as tmp:
    base = os.path.join(tmp, "ilha")
    shutil.copytree(RAIZ, base, ignore=shutil.ignore_patterns("node_modules", ".git"))

    caminho = os.path.join(base, "dados", "produtos-filtro.json")
    d = json.load(open(caminho, encoding="utf-8"))
    alvo = None
    for p in d["produtos"]:
        img = p.get("imagem")
        if img and img.get("largura") is not None:
            img["largura"] = None
            img["altura"] = None
            img["medida_em"] = None
            img["medida_como"] = None
            img["motivo_sem_medida"] = "mundo produzido pelo teste-dimensao-imagem.py"
            alvo = (p["id"], img["url"])
            break
    if alvo is None:
        raise SystemExit("nenhum registro de filtro com dimensao: o mundo produzido nao prova nada")
    open(caminho, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    r = subprocess.run(["python3", os.path.join(base, "ferramentas", PAGINAS[ALVO_PAGINA])],
                       capture_output=True, text=True, cwd=base)
    if r.returncode != 0:
        raise SystemExit("o gerador falhou no mundo produzido: %s" % r.stderr[-600:])

    pagina = servir(base, ALVO_PAGINA)
    urls = banco_por_url(base)
    achadas = dict(imgs_de_produto(pagina, urls))
    pid, url = alvo
    ok("%s sem medida: a FOTO CONTINUA SERVIDA (produto nao se perde por falta de medida)" % pid,
       url in achadas, "a <img> sumiu da pagina")
    if url in achadas:
        ok("%s sem medida: e sai sem width e sem height" % pid,
           par_do_tag(achadas[url]) == (None, None),
           "tela=%r" % (par_do_tag(achadas[url]),))
    outras = [u for u in achadas if u != url]
    ok("%s sem medida: as VIZINHAS medidas continuam servindo o par delas" % pid,
       bool(outras) and all(par_do_tag(achadas[u]) == urls[u][1] for u in outras),
       "vizinhas=%d" % len(outras))

print("\n%d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
if falhas:
    for f in falhas:
        print("  FALHOU: %s" % f)
sys.exit(1 if falhas else 0)

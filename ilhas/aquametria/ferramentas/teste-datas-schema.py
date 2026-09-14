#!/usr/bin/env python3
"""O PORTAO DAS DATAS DO SCHEMA — mede se a pagina declara a data que o
WordPress tem, no formato em que o sitemap a declara.

    python3 ferramentas/teste-datas-schema.py .

POR QUE ELE NASCEU (itens 1 e 2 do despacho da Sentinela de 13/09/2026):

  - os tres artigos serviam `'dateModified' => '2026-09-10'`, um literal digitado
    dentro do snippet, enquanto o `wp-sitemap-posts-post-1.xml` declarava
    `2026-09-13T13:38:10+00:00` para as MESMAS tres URLs. Duas datas da mesma
    pagina, e a do schema envelhecia sozinha a cada Sync;
  - as onze fichas de peixe serviam `Article` SEM data, SEM autor e SEM
    publicador, enquanto o `Article` dos artigos trazia os quatro campos.

COMO ESTE ARQUIVO FOI ESCRITO, e qual cicatriz da secao 8 decidiu cada escolha:

  1. A REGUA E RECOMPUTADA AQUI, do valor que este portao INJETOU no post. Nada
     e importado do snippet e nada e comparado com uma data digitada. Uma regua
     com data digitada dentro reprovaria pagina certa no dia em que a data
     mudasse — foi o defeito que a regua da SERP cometeu nesta mesma ilha, em
     13/09/2026, e ela e da mesma familia desta.

  2. O PORTAO PRODUZ O MUNDO. Data ausente e o caso em que a regra manda o campo
     NAO SAIR, e o banco de hoje nao tem nenhuma pagina assim: medido so no
     mundo normal, "omite quando nao sabe" ficaria verde com a funcao quebrada, e
     o dia em que importasse seria o dia em que um post voltasse sem data. As
     duas datas tambem sao injetadas DIFERENTES uma da outra, senao uma funcao
     que trocasse os dois campos passaria.

  3. AS DUAS DATAS SAO MEDIDAS NO JSON-LD SERVIDO, pagina por pagina, UM PROCESSO
     POR PAGINA — o `static` da marca, do estilo e da trilha sai na primeira e
     some nas seguintes (ver render-pagina-completa.php).

  4. A ASSIMETRIA DOS ARTIGOS E MEDIDA COMO ASSIMETRIA, nao tolerada: o
     `datePublished` dos tres artigos e data editorial declarada no registro
     ('2026-09-08', que o proprio endereco carrega), e NAO a data do post. Quem
     "consertar" isso por simetria muda a data de publicacao de tres URLs
     indexadas, e o portao reprova nomeando o porque.

  5. A CONSTANTE NAO PODE RENASCER NA PAGINA VIZINHA. Uma afirmacao le o codigo
     dos snippets e proibe literal de data em campo de schema. Sem ela, o proximo
     no de schema nasceria com a data escrita a mao e este portao ficaria verde,
     porque ele mede os catorze nos que existem hoje, nao os que virao.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
RENDER = os.path.join(RAIZ, "ferramentas", "render-pagina-completa.php")

# O mapa esta AQUI, a mao, pela decisao 2 do cabecalho de teste-peixes.py: ler o
# mapa do snippet e perguntar ao snippet o que ele publica.
ARTIGOS = [
    "quantos-watts-de-aquecedor-para-aquario",
    "quanta-midia-biologica-o-aquario-precisa",
    "quantos-lumens-por-litro-aquario-plantado",
]

FICHAS = [
    "quantos-litros-para-tetra-neon",
    "quantos-litros-para-tetra-cardinal",
    "quantos-litros-para-mato-grosso",
    "quantos-litros-para-tetra-ember",
    "quantos-litros-para-tetra-brilhante",
    "quantos-litros-para-rodostomo",
    "quantos-litros-para-tetra-negro",
    "quantos-litros-para-coridora-bronze",
    "quantos-litros-para-coridora-pimenta",
    "quantos-litros-para-coridora-panda",
    "quantos-litros-para-coridora-sterbai",
    # leva 4, 14/09/2026
    "quantos-litros-para-betta",
    "quantos-litros-para-colisa-anao",
    "quantos-litros-para-gurami-mel",
]

# A data editorial que os tres artigos declaram no registro, e que o endereco
# /2026/09/08/ carrega. Escrita aqui porque a afirmacao 4 do cabecalho e
# justamente que ela NAO vem do post.
PUBLICADO_EDITORIAL = "2026-09-08"

# Os dois mundos, com valores que NAO sao os padroes da bancada — mundo medido
# com o valor padrao nao distingue "a funcao leu o post" de "a funcao devolveu o
# que estava escrito no render".
MUNDO = {"publicado": "2026-09-05 08:01:02", "modificado": "2026-09-13 19:44:55"}
MUNDO_SEM_MODIFICADO = {"publicado": "2026-09-05 08:01:02", "modificado": "0000-00-00 00:00:00"}
MUNDO_SEM_NENHUMA = {"publicado": "", "modificado": ""}
# O TERCEIRO MUNDO E O QUE O BANCO NAO TEM E O ESQUEMA PERMITE: o campo do post e
# uma STRING, e a funcao da casca tem um ramo para o texto que nao se le como
# data. O WordPress nunca grava isto, e por isso esse ramo era codigo que nenhuma
# afirmacao podia alcancar — a primeira rodada de mutacoes provou: "sem data, a
# casca devolve a data de HOJE" PASSOU, porque as duas guardas de cima
# interceptavam os dois mundos que eu produzia e o ramo nunca rodava. Ramo
# defensivo nao medido e ramo que pode mentir a vontade.
MUNDO_ILEGIVEL = {"publicado": "sem data", "modificado": "13 de setembro"}

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


def w3c(cru):
    """A REGUA PROPRIA: 'Y-m-d H:i:s' em UTC -> W3C, do jeito que o sitemap do
    nucleo escreve. Recomputada aqui com a biblioteca do Python, sem PHP e sem
    chamar a funcao da casca."""
    d = datetime.strptime(cru, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    return d.isoformat()


def servir(slug, mundo):
    amb = dict(os.environ)
    amb["AQM_TESTE_DATA_PUBLICADO"] = mundo["publicado"]
    amb["AQM_TESTE_DATA_MODIFICADO"] = mundo["modificado"]
    r = subprocess.run(["php", RENDER, RAIZ, slug], capture_output=True, text=True, env=amb)
    if r.returncode != 0:
        raise SystemExit("render falhou em %s: %s" % (slug, r.stderr[-600:]))
    return r.stdout


def nos_de(pagina):
    """Todo no de JSON-LD servido no <head>, com o @graph desdobrado."""
    achados = []
    for bloco in re.findall(
        r'<script type="application/ld\+json"[^>]*>(.*?)</script>', pagina, re.S
    ):
        try:
            d = json.loads(bloco)
        except ValueError:
            achados.append({"@type": "JSON-LD INVALIDO"})
            continue
        if isinstance(d, dict) and "@graph" in d:
            achados.extend(d["@graph"])
        elif isinstance(d, list):
            achados.extend(d)
        else:
            achados.append(d)
    return achados


def artigo_de(pagina, slug):
    artigos = [n for n in nos_de(pagina) if n.get("@type") == "Article"]
    if len(artigos) != 1:
        raise SystemExit(
            "%s serviu %d nos Article; o portao mede um por pagina" % (slug, len(artigos))
        )
    return artigos[0]


def editora_ok(no, campo):
    v = no.get(campo)
    return (
        isinstance(v, dict)
        and v.get("@type") == "Organization"
        and v.get("name") == "Aquametria"
        and isinstance(v.get("url"), str)
        and v["url"].startswith("https://aquametria.com.br")
    )


# ---------------------------------------------------------------------------
# 1. MUNDO NORMAL — as catorze paginas com Article servem as datas do post
# ---------------------------------------------------------------------------
print("\n== mundo normal: post modificado em %s, publicado em %s ==" % (
    MUNDO["modificado"], MUNDO["publicado"]))

esperado_mod = w3c(MUNDO["modificado"])
esperado_pub = w3c(MUNDO["publicado"])
ok("a regua injeta duas datas DIFERENTES (senao trocar os campos passaria)",
   esperado_mod != esperado_pub, "%s == %s" % (esperado_mod, esperado_pub))

for slug in ARTIGOS:
    pagina = servir(slug, MUNDO)
    no = artigo_de(pagina, slug)
    ok("artigo %s: dateModified = a data do post, em W3C" % slug,
       no.get("dateModified") == esperado_mod,
       "servido=%r esperado=%r" % (no.get("dateModified"), esperado_mod))
    # Decisao 4 do cabecalho: a assimetria e deliberada e e medida.
    ok("artigo %s: datePublished continua a data EDITORIAL, nao a do post" % slug,
       no.get("datePublished") == PUBLICADO_EDITORIAL,
       "servido=%r editorial=%r post=%r" % (
           no.get("datePublished"), PUBLICADO_EDITORIAL, esperado_pub))
    ok("artigo %s: author e publisher sao a editora Aquametria" % slug,
       editora_ok(no, "author") and editora_ok(no, "publisher"),
       "author=%r publisher=%r" % (no.get("author"), no.get("publisher")))

for slug in FICHAS:
    pagina = servir(slug, MUNDO)
    no = artigo_de(pagina, slug)
    ok("ficha %s: dateModified = a data do post, em W3C" % slug,
       no.get("dateModified") == esperado_mod,
       "servido=%r esperado=%r" % (no.get("dateModified"), esperado_mod))
    ok("ficha %s: datePublished = a data de PUBLICACAO do post, em W3C" % slug,
       no.get("datePublished") == esperado_pub,
       "servido=%r esperado=%r" % (no.get("datePublished"), esperado_pub))
    ok("ficha %s: author e publisher sao a editora Aquametria" % slug,
       editora_ok(no, "author") and editora_ok(no, "publisher"),
       "author=%r publisher=%r" % (no.get("author"), no.get("publisher")))
    ok("ficha %s: o Article continua trazendo headline e about" % slug,
       isinstance(no.get("headline"), str) and no["headline"].strip() != ""
       and isinstance(no.get("about"), dict),
       "headline=%r" % no.get("headline"))

# ---------------------------------------------------------------------------
# 2. MUNDO PRODUZIDO — o WordPress nao sabe quando a pagina mudou
#
# Decisao 2 do cabecalho. Duas amostras (um artigo e uma ficha) por mundo: a
# regra mora numa funcao so, e medir as catorze aqui triplicaria o tempo do
# portao sem medir um caminho novo de codigo.
# ---------------------------------------------------------------------------
print("\n== mundo produzido: post_modified_gmt = 0000-00-00 ==")
for tipo, slug in (("artigo", ARTIGOS[0]), ("ficha", FICHAS[0])):
    no = artigo_de(servir(slug, MUNDO_SEM_MODIFICADO), slug)
    ok("%s %s: sem data de modificacao, dateModified NAO SAI" % (tipo, slug),
       "dateModified" not in no, "servido=%r" % no.get("dateModified"))
    ok("%s %s: e nenhuma data de HOJE entra no lugar dela" % (tipo, slug),
       datetime.now(timezone.utc).strftime("%Y-%m-%d") not in json.dumps(no),
       "no=%s" % json.dumps(no, ensure_ascii=False)[:300])
    ok("%s %s: a pagina continua servindo o Article inteiro" % (tipo, slug),
       isinstance(no.get("headline"), str) and editora_ok(no, "publisher"),
       "no=%s" % json.dumps(no, ensure_ascii=False)[:200])

print("\n== mundo produzido: as duas datas vazias ==")
no = artigo_de(servir(FICHAS[0], MUNDO_SEM_NENHUMA), FICHAS[0])
ok("ficha sem nenhuma das duas datas: nem dateModified nem datePublished saem",
   "dateModified" not in no and "datePublished" not in no,
   "no=%s" % json.dumps(no, ensure_ascii=False)[:300])

print("\n== mundo produzido: o campo do post tem texto que nao se le como data ==")
for tipo, slug in (("artigo", ARTIGOS[1]), ("ficha", FICHAS[2])):
    no = artigo_de(servir(slug, MUNDO_ILEGIVEL), slug)
    # O artigo continua declarando a data EDITORIAL, que nao vem do post: aqui
    # so o dateModified pode desaparecer. Cobrar as duas ausencias reprovaria o
    # artigo por servir o campo certo, que e o avesso do que este mundo mede.
    ok("%s %s: data ilegivel nao vira dateModified" % (tipo, slug),
       "dateModified" not in no, "servido=%r" % no.get("dateModified"))
    if tipo == "ficha":
        ok("%s %s: data ilegivel nao vira datePublished" % (tipo, slug),
           "datePublished" not in no, "servido=%r" % no.get("datePublished"))
    ok("%s %s: e nem a data de HOJE entra no lugar dela" % (tipo, slug),
       datetime.now(timezone.utc).strftime("%Y-%m-%d") not in json.dumps(no),
       "no=%s" % json.dumps(no, ensure_ascii=False)[:300])

print("\n== mundo produzido: so a data de publicacao existe ==")
no = artigo_de(servir(FICHAS[1], MUNDO_SEM_MODIFICADO), FICHAS[1])
ok("ficha: datePublished sai sozinho, sem dateModified para acompanhar",
   no.get("datePublished") == esperado_pub and "dateModified" not in no,
   "pub=%r mod=%r" % (no.get("datePublished"), no.get("dateModified")))

# ---------------------------------------------------------------------------
# 3. A CONSTANTE NAO RENASCE — decisao 5 do cabecalho
# ---------------------------------------------------------------------------
print("\n== o codigo nao volta a digitar data de schema ==")
CAMPOS = ("dateModified", "datePublished", "lastmod")
for arquivo in sorted(os.listdir(os.path.join(RAIZ, "snippets"))):
    if not arquivo.endswith(".php"):
        continue
    fonte = open(os.path.join(RAIZ, "snippets", arquivo), encoding="utf-8").read()
    # OS COMENTARIOS DE BLOCO SAEM ANTES DA CONTAGEM, e a primeira versao desta
    # regua nao os tirava: ela reprovou o cabecalho que acabara de EXPLICAR o
    # conserto, que cita `'dateModified' => '2026-09-10'` como o defeito de onde
    # o item 1 partiu. Regua que proibe a palavra em vez do codigo torna a
    # cicatriz impossivel de escrever, e a cicatriz e o que impede o defeito de
    # voltar. Fica de fora so o comentario de bloco (`/* */`, que e onde esta
    # ilha escreve prosa); `//` continua contando, porque codigo comentado com
    # `//` e codigo esperando voltar.
    fonte = re.sub(r"/\*.*?\*/", "", fonte, flags=re.S)
    digitadas = []
    for campo in CAMPOS:
        # `'campo' => '2026-...'` ou `"campo": "2026-..."`, em qualquer ordem de
        # aspas. O alvo e o LITERAL de data, nunca a mencao ao campo: o
        # cabecalho deste portao e os comentarios dos snippets citam as duas
        # coisas, e proibir a palavra reprovaria a explicacao do conserto.
        digitadas += re.findall(
            r"""['"]%s['"]\s*(?:=>|:)\s*['"](\d{4}-\d{2}-\d{2}[^'"]*)['"]""" % campo, fonte
        )
    # A data editorial dos artigos e a unica excecao, e ela e NOMEADA: nao e data
    # de modificacao, e o endereco /2026/09/08/ a carrega.
    digitadas = [d for d in digitadas if d != PUBLICADO_EDITORIAL]
    ok("%s: nenhum campo de data de schema com literal digitado" % arquivo,
       not digitadas, "literais=%r" % digitadas)

print("\n%d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
if falhas:
    for f in falhas:
        print("  FALHOU: %s" % f)
sys.exit(1 if falhas else 0)

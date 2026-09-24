#!/usr/bin/env python3
"""CONFERE NO AR quem manda indexar e quem nao manda — as DUAS direcoes.

    python3 ferramentas/conferir-robots-no-ar.py .

E o criterio de pronto do item 1 do despacho da leitura semanal de 23/09/2026,
escrito como portao em vez de como um `grep` digitado uma vez. O item dizia que
`/author/aquametria_gestor/` estava no ar sem `noindex`; NAO ESTAVA, e o
cabecalho de `ferramentas/regua-robots.py` conta por que a medicao errou (aspa
simples do nucleo do WordPress contra aspa dupla das ilhas irmas). O que o item
achou de verdade e mais util do que o defeito que ele descreveu: NADA nesta ilha
media, no ar, a diretiva que decide o que entra no indice do Google. A regra
existia em `aquametria_seo_deve_noindex()` e `teste-seo-tecnico.php` a media
FORA do WordPress — entao a distancia entre a regra e a tela era exatamente a
que a secao 4 do ARQUIPELAGO.md paga mais caro, e ela ficou 14 dias sem regua.

O ITEM DECLAROU AS DUAS DIRECOES, E E POR ISSO QUE ELE VALE MAIS QUE UM `grep`:
"acrescentar `noindex` demais e o defeito oposto e igualmente grave". As duas
metades estao aqui, e a de baixo e a caro:

  1. OS QUATRO CONTEXTOS DE ARQUIVO servem `noindex`: autor, busca, arquivo por
     data e a categoria `metodos` (que nasce fora do sitemap de proposito, T2).
     Nenhum deles e pagina desta ilha; todos respondem 200 e gastam orcamento de
     rastreamento de um dominio novo.
  2. NENHUMA URL DO SITEMAP serve `noindex`. A lista vem do sitemap NO AR, nunca
     digitada aqui — a leva seguinte publica pagina e esta regua cresce sozinha.
  3. CADA UMA SERVE EXATAMENTE UMA meta `robots`. Duas e defeito: o Google
     resolve meta duplicada pelo lado restritivo, e a maneira plausivel de
     "consertar" o item 1 era imprimir uma segunda tag na mao, ao lado da que o
     nucleo ja imprimia. Este portao reprovaria esse conserto.

DUAS ESCOLHAS HERDADAS dos outros `conferir-*` desta pasta, pelos mesmos motivos:
a lista de URLs sai do sitemap, e toda requisicao leva `?v=<hora>`, porque o
cache duplo da secao 4 faz a medicao ler o site de ontem e chamar isso de
conferencia.
"""
import importlib.util
import os
import re
import sys
import time
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://aquametria.com.br"

# Os contextos de ARQUIVO que o WordPress serve e que nao sao pagina da ilha.
# A lista e curta e explicita porque cada linha e uma URL que alguem pode abrir
# e conferir a mao; `aquametria_seo_deve_noindex()` cobre outras (anexo, tag,
# 404) e essas nao tem endereco estavel para medir daqui.
ARQUIVOS = [
    ("/author/aquametria_gestor/", "arquivo de AUTOR"),
    ("/?s=aquario", "pagina de BUSCA"),
    ("/2026/09/", "arquivo por DATA"),
    ("/category/metodos/", "categoria METODOS, fora do sitemap pelo T2"),
]


def carregar(nome):
    caminho = os.path.join(RAIZ, "ferramentas", nome)
    spec = importlib.util.spec_from_file_location(nome.replace("-", "_")[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar("regua-robots.py")

contadas = [0]
falhas = []


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def buscar(url):
    sep = "&" if "?" in url else "?"
    pedido = urllib.request.Request(
        url + sep + "v=" + time.strftime("%H%M%S"),
        headers={"User-Agent": "Aquametria/conferir-robots-no-ar (Arquipelago)",
                 # `identity` pelo mesmo motivo da conferencia do JSON-LD: o
                 # corpo comprimido chegava truncado em algumas passadas, e
                 # medicao de ausencia sobre corpo truncado acha ausencia.
                 "Accept-Encoding": "identity"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def urls_do_sitemap():
    """Toda URL interna que o indice de sitemaps do nucleo lista."""
    _, indice = buscar(BASE + "/wp-sitemap.xml")
    fora = []
    for sm in re.findall(r"<loc>(.*?)</loc>", indice):
        _, xml = buscar(sm)
        for loc in re.findall(r"<loc>(.*?)</loc>", xml):
            if loc.startswith(BASE) and loc not in fora:
                fora.append(loc)
    return fora


def main():
    print("1. OS CONTEXTOS DE ARQUIVO MANDAM NAO INDEXAR")
    for caminho, rotulo in ARQUIVOS:
        url = BASE + caminho
        try:
            status, html = buscar(url)
        except Exception as e:                                   # noqa: BLE001
            ok("%s responde" % rotulo, False, "%s: %s" % (url, e))
            continue
        metas = regua.metas_de_robots(html)
        ok("%s manda noindex" % rotulo, regua.tem_noindex(html),
           "%s -> %s" % (url, metas if metas else "NENHUMA meta robots"))
        ok("%s serve UMA meta robots" % rotulo, 1 == len(metas),
           "%d servida(s)" % len(metas))

    print("\n2. NENHUMA URL DO SITEMAP MANDA NAO INDEXAR")
    urls = urls_do_sitemap()
    ok("o sitemap lista URLs desta ilha", len(urls) > 0, "%d URLs" % len(urls))
    com_noindex, sem_meta, duplicadas = [], [], []
    for u in urls:
        try:
            _, html = buscar(u)
        except Exception as e:                                   # noqa: BLE001
            com_noindex.append("%s (nao abriu: %s)" % (u, e))
            continue
        n = regua.quantas_metas_de_robots(html)
        if regua.tem_noindex(html):
            com_noindex.append(u)
        if n == 0:
            sem_meta.append(u)
        elif n > 1:
            duplicadas.append("%s (%d)" % (u, n))
    ok("as %d URLs do sitemap NAO mandam noindex" % len(urls),
       not com_noindex, ", ".join(com_noindex[:5]))
    # Sem esta, a de cima passaria por vacuidade se a ilha parasse de servir a
    # tag: "nenhuma manda noindex" fica verde numa pagina sem meta nenhuma.
    ok("as %d servem a meta robots (a de cima nao passa por ausencia)" % len(urls),
       not sem_meta, ", ".join(sem_meta[:5]))
    ok("nenhuma das %d serve meta robots DUPLICADA" % len(urls),
       not duplicadas, ", ".join(duplicadas[:5]))

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

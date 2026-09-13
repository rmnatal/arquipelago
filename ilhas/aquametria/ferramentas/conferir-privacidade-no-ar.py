#!/usr/bin/env python3
"""CONFERE NO AR a pagina de privacidade — e o que ela afirma NAO e sobre o
codigo desta ilha, e sim sobre o que o navegador de quem le vai buscar fora
daqui. Afirmacao sobre o ar so se mede no ar.

    python3 ferramentas/conferir-privacidade-no-ar.py .

POR QUE ESTE PORTAO EXISTE, e a familia da cicatriz e conhecida. A secao 8 do
contrato ja registra duas vezes o mesmo defeito com roupas diferentes: "numero de
tela nasce contado, nunca digitado" (Clube do Mosaico, 11/09) e "afirmacao da
pagina sobre o proprio banco se conta, nunca se digita" (Robometria, 12/09). Uma
lista de terceiros escrita a mao numa pagina de privacidade e exatamente isso: ela
nasce certa no dia em que e escrita e envelhece CALADA no dia em que alguem
acrescentar um script, um plugin ou uma fonte nova — e o leitor nunca descobre,
porque a pagina continua com cara de conferida. O que este arquivo faz e obrigar
as DUAS METADES a dizerem a mesma coisa, nas duas direcoes.

AS REGUAS, e de onde cada uma sai:

  1. NENHUMA URL DO SITEMAP DEVOLVE Set-Cookie. E a frase mais forte da pagina
     ("o servidor deste site nao grava cookie nenhum"), e e a unica que a ilha
     pode afirmar sozinha, porque o servidor e dela. Medida no CABECALHO da
     resposta, url por url.

  2. TODO ENDERECO EXTERNO QUE O AR SERVE ESTA NOMEADO NA PAGINA. Recolhido do
     HTML SERVIDO de cada URL, separando o que o navegador busca sozinho
     (src/href de script, link, img, iframe, source, video) do que ele so
     contata se a pessoa clicar (href de <a>) — porque a pagina afirma coisas
     diferentes sobre os dois, e misturar os dois seria publicar que a ilha
     entrega o IP de quem le a um endereco que ela so linka.

  3. TODO ENDERECO NOMEADO NA PAGINA EXISTE NO AR. E a direcao que quase sempre
     falta, e sem ela a regra 2 tem porta dos fundos: bastaria a pagina listar
     meia internet para nunca mais reprovar. Os nomes sao extraidos do CORPO
     SERVIDO da propria pagina, nao do arquivo `.md` — quem publica e o Sync, e
     ja aconteceu nesta ilha do corpo trocar no ar e o titulo nao (11/09/2026).

  4. A PAGINA ESTA NO SITEMAP, RESPONDE 200 e NAO E PAGINA FINA. O piso de ~1.500
     caracteres de corpo e o da secao 8: pagina magra em dominio novo gasta
     orcamento de rastreamento.

  5. O RODAPE DE TODA URL LINKA A PAGINA. E o que tira do 16.4(f) uma pagina que
     nao tem mae e nao tem irma: ela nao entra em cluster nenhum, entao o que a
     impede de ser orfa e o rodape, e isso se conta.

QUEM CONFERE ESCREVE A PROPRIA REGUA (secao 8): a lista de enderecos desta ilha
NAO esta escrita aqui e NAO e importada de nenhum arquivo que a pagina tambem
leia. Ela e recolhida do ar a cada execucao. Uma lista digitada neste arquivo
faria as duas metades errarem juntas, que e a definicao de teste verde que nao
mede nada.

E O CACHE DUPLO DA SECAO 4: toda requisicao leva `?v=<hora>`, senao a medicao le
o site de ontem e chama isso de conferencia.
"""

import re
import sys
import time
import urllib.parse
import urllib.request

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
BASE = "https://aquametria.com.br"
CAMINHO_PAGINA = "/politica-de-privacidade/"

# O dominio da propria ilha nunca e terceiro. Tudo o mais e.
CASA = "aquametria.com.br"

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
        headers={"User-Agent": "Aquametria/conferir-privacidade-no-ar (Arquipelago)"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, dict(r.getheaders()), r.read().decode("utf-8", "replace")


def urls_do_sitemap():
    _, _, indice = buscar(BASE + "/wp-sitemap.xml")
    fora = []
    for sm in re.findall(r"<loc>(.*?)</loc>", indice):
        _, _, xml = buscar(sm)
        fora += re.findall(r"<loc>(.*?)</loc>", xml)
    return sorted(set(fora))


def corpo_de(html):
    """O CORPO, nunca a pagina inteira — a cicatriz da secao 8 e literal: quem
    afirma sobre o que a pagina DIZ mede no corpo, senao acha a propria frase
    dentro do JSON-LD do <head> e passa ate com resposta inventada."""
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
    if m:
        return m.group(1)
    m = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    return m.group(1) if m else html


def texto(html):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;|&#\d+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def hospedeiro(valor):
    """Devolve o dominio de um endereco absoluto, ou '' se ele nao for externo."""
    if valor.startswith("//"):
        valor = "https:" + valor
    if not valor.lower().startswith("http"):
        return ""
    ho = urllib.parse.urlparse(valor).netloc.lower().split("@")[-1].split(":")[0]
    if ho == CASA or ho.endswith("." + CASA):
        return ""
    return ho


def enderecos_servidos(html):
    """(carrega sozinho, so se clicar) — dois conjuntos de dominios.

    A separacao e por TAG, que e estrutura, e nao por vizinhanca de palavra: o
    que decide se o navegador liga sozinho para um endereco e o elemento em que
    ele esta, nao o que a pagina escreve em volta dele.
    """
    auto, clique = set(), set()
    for tag, atributos in re.findall(
            r"<(script|link|img|iframe|source|video|audio|embed|a)\b([^>]*)>", html, re.I):
        for _, valor in re.findall(r"\b(src|href|data-src|srcset)\s*=\s*[\"']([^\"']+)[\"']",
                                   atributos, re.I):
            ho = hospedeiro(valor.split()[0] if valor.strip() else valor)
            if not ho:
                continue
            (clique if tag.lower() == "a" else auto).add(ho)
    return auto, clique


# Um dominio dito em prosa: pelo menos dois rotulos, terminando em rotulo de
# letras. Nao casa "1,25" nem "R$ 12,50"; casa "fonts.gstatic.com" e
# "s.shopee.com.br". A regua e propria e vive aqui.
RE_DOMINIO_NA_PROSA = re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.){1,4}[a-z]{2,}\b")


def dominios_citados(corpo_texto):
    achados = set()
    for m in RE_DOMINIO_NA_PROSA.findall(corpo_texto.lower()):
        if m == CASA or m.endswith("." + CASA):
            continue
        # Um dominio de verdade termina em TLD conhecido desta medicao. Sem esta
        # guarda, "etc.com" de uma frase qualquer viraria endereco.
        if re.search(r"\.(com|br|net|org|io|dev)$", m):
            achados.add(m)
    return achados


def main():
    print("\n== as URLs do ar ==")
    urls = urls_do_sitemap()
    ok("o sitemap lista URLs", len(urls) > 0, "%d URLs" % len(urls))

    alvo = BASE + CAMINHO_PAGINA
    ok("a pagina de privacidade esta no sitemap", alvo in urls,
       "procurei %s" % CAMINHO_PAGINA)

    print("\n== regra 1: nenhuma URL devolve Set-Cookie ==")
    print("== regra 2: o que o ar serve, e a regra 5: o rodape linka a pagina ==")
    auto_total, clique_total = set(), set()
    com_cookie = []
    sem_link_rodape = []
    fora_de_200 = []
    paginas = {}
    for u in urls:
        st, cab, html = buscar(u)
        paginas[u] = html
        if st != 200:
            fora_de_200.append("%s (%s)" % (u, st))
        if any(k.lower() == "set-cookie" for k in cab):
            com_cookie.append(u)
        a, c = enderecos_servidos(html)
        auto_total |= a
        clique_total |= c
        if CAMINHO_PAGINA not in html:
            sem_link_rodape.append(u)

    ok("toda URL do sitemap responde 200", not fora_de_200,
       ", ".join(fora_de_200[:3]))
    ok("nenhuma das %d URLs devolve Set-Cookie" % len(urls), not com_cookie,
       ", ".join(com_cookie[:3]))
    ok("toda URL linka a pagina de privacidade", not sem_link_rodape,
       "sem link: %s" % ", ".join(sem_link_rodape[:3]))

    so_clique = clique_total - auto_total
    print("\n  carrega sozinho: %s" % (", ".join(sorted(auto_total)) or "nenhum"))
    print("  so se clicar   : %s" % (", ".join(sorted(so_clique)) or "nenhum"))

    print("\n== a pagina, no ar ==")
    st, _, html = buscar(alvo)
    ok("a pagina de privacidade responde 200", st == 200, str(st))
    corpo = corpo_de(html)
    corpo_texto = texto(corpo)
    ok("a pagina nao e fina (corpo com 1.500 caracteres ou mais)",
       len(corpo_texto) >= 1500, "%d caracteres" % len(corpo_texto))
    ok("o corpo nao comeca por metadado YAML",
       not corpo_texto.lstrip().startswith("---"), corpo_texto[:40])

    citados = dominios_citados(corpo_texto)
    print("\n  nomeados na pagina: %s" % (", ".join(sorted(citados)) or "nenhum"))

    print("\n== regra 2: todo endereco do ar esta nomeado na pagina ==")
    for ho in sorted(auto_total):
        ok("a pagina nomeia %s, que carrega sozinho" % ho, ho in citados)
    for ho in sorted(so_clique):
        ok("a pagina nomeia %s, que so e contatado no clique" % ho, ho in citados)

    print("\n== regra 3: todo endereco nomeado existe no ar ==")
    servidos = auto_total | clique_total
    for ho in sorted(citados):
        ok("%s, que a pagina nomeia, aparece no HTML servido" % ho, ho in servidos,
           "se nao aparece mais, a frase envelheceu")

    ok("a pagina nomeia ao menos um endereco externo", len(citados) > 0,
       "pagina que nao nomeia nada nunca reprova pela regra 2")

    print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

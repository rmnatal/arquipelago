#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABRE O SITE — este confere o AR, nao o repositorio.

O `<title>` QUE O SITE SERVE HOJE E O QUE ALGUEM DECLAROU, PAGINA POR PAGINA?
E A PROMESSA NUMERICA DA BANDA 4 A 10 CHEGOU LA?

    python3 ferramentas/conferir-titulo-no-ar.py
    python3 ferramentas/conferir-titulo-no-ar.py --gravar

POR QUE ELE EXISTE, e a data e 19/10/2026
-----------------------------------------
Esta ilha nao tem problema de indexacao: 50 de 52 URLs indexadas, 580
impressoes em 7 dias e as 40 paginas com impressao entre a posicao 2,0 e 10,0.
Tem problema de CTR — 4 cliques — e a leitura semanal de 14/10/2026 escreveu,
com todas as letras, que **a unica alavanca e titulo e meta**, que ela ja foi
puxada em 14/10, e que a semana de 14 a 21/10 tem um trabalho so: *"deixar
quieto e medir"*.

Medir o que, exatamente, esta escrito em duas linhas do proprio repositorio:

  * `dados/posicoes.md`, 14/10: *"NAO COPIEI os `<title>` servidos para esta
    serie (...) A leitura de 21/10 e a primeira em que copiar o titulo servido
    significa alguma coisa — e ai e OBRIGATORIO."*
  * o despacho da leitura semanal, item 2: o critERIO de pronto das duas
    propostas e a leitura de 21/10 *"com o `<title>` servido no dia copiado
    para `dados/posicoes.md`"*.

**Obrigatorio em dois dias, e o instrumento era uma aba de navegador.** Copiar
texto da tela para a serie e a recontagem a mao que esta pasta mediu em 19/10
um andar abaixo, no cano de links: *"recontagem a mao e a assinatura de
instrumento sem portao — quando existe portao, ninguem reconta"*.

E O PORTAO DA PROMESSA NAO VE O AR, POR DESENHO
-----------------------------------------------
`ferramentas/teste-promessa-do-titulo.py` e BANCADA e mede o REPOSITORIO: ele
reprova a pagina que declarou promessa e nao serve digito, reprova a pagina de
controle que ganhar promessa, e cobra o teto de 65. Nada disso alcanca o ar — e
a cicatriz de 11/09/2026 desta ilha, citada no cabecalho do
`conferir-datas-e-voz-no-ar.py`, e exatamente esta: *"293 afirmacoes verdes, o
Sync dizendo '18 aplicado(s)', e os nove titulos no ar continuando os de
antes"*. Pior: **as tres travas da promessa sao silenciosas por desenho** — se
o numero nao couber em 65 ou se a funcao do banco nao responder, o titulo volta
a nome + marca, que e sempre valido. Promessa que nao desembarca nao reprova
nada hoje, e a leitura de 21/10 creditaria as promessas um resultado que elas
nao produziram, ou as reprovaria por nunca terem chegado.

O QUE ELE AFIRMA
----------------
  1. O sitemap respondeu e trouxe URL, e TODA URL dele foi aberta. Esta e a
     primeira de proposito: "0 titulo acima do teto" sobre zero pagina lida e
     VERDE VAZIO, e verde vazio e a unica forma de este portao mentir sem
     ninguem editar uma linha dele.
  2. Toda URL serve `<title>` e serve `<meta name="description">`.
  3. Nenhum `<title>` servido passa do teto de 65 caracteres, medido DEPOIS de
     decodificar as entidades — que e como a tela conta.
  4. **As paginas que DECLARAM promessa servem a promessa.** A string vem do
     proprio snippet, perguntada a ele pelo `listar-promessas.php`; este portao
     nao monta titulo nenhum e nao sabe o separador.
  5. **A pagina de CONTROLE continua sem promessa.** Ela e descoberta — e a
     que o mapa de promessas devolve vazia entre as calculadoras —, nao
     digitada aqui, e o teste e a ausencia de algarismo no titulo servido.
     A leitura de 14/10 escreveu por que ela importa: a
     `/calculadora-de-litragem/` foi de 27 para 82 impressoes SEM SER TOCADA, e
     *"sem este controle, a leitura de 21/10 creditaria as promessas um ganho
     que elas nao produziram"*.

     **E A AFIRMACAO NAO E "NENHUMA PAGINA SEM PROMESSA TEM ALGARISMO", porque
     isso foi MEDIDO e e falso.** Na passada de 19/10/2026 as 13h3xZ, SEIS dos
     52 titulos servidos tem algarismo: as cinco promessas e o artigo
     `/2026/09/08/quantos-watts-de-aquecedor-para-aquario/`, cujo titulo e
     *"Por que o 1 W por litro erra para o mesmo lado"* — o algarismo esta no
     NOME da pagina, nao numa promessa. Por isso a ausencia de algarismo e
     cobrada so na calculadora que o mapa devolve com promessa vazia, que e o
     controle. Regra mais larga do que a medicao sustenta reprova pagina boa no
     primeiro titulo com numero no nome.
  6. O titulo e a descricao servidos sao os DECLARADOS na serie, pagina por
     pagina. E esta afirmacao que faz a leitura de 21/10 copiar um numero
     MEDIDO em vez de digitar um texto lido na aba.

E O QUE ELE NAO FAZ, de proposito
---------------------------------
Nao cobra a montagem do titulo (quem a cobra e o `teste-promessa-do-titulo.py`,
no repositorio), nao cobra as duas fontes do titulo do eixo (quem cobra e o
`teste-titulos-das-duas-fontes.py`), nao cobra voz nem termo proibido (quem
cobra e o `teste-voz.mjs`) e nao cobra o teto da meta description. Terceira
regua da mesma regra e a cicatriz de 16/10/2026 desta pasta. Ele pergunta o que
nenhum deles pergunta: **o titulo de hoje, no ar, e o titulo que alguem
declarou?**

QUANDO ELE FICA VERMELHO, O CONSERTO DEPENDE DO LADO
----------------------------------------------------
Titulo trocado DE PROPOSITO (leva nova, promessa nova, pagina nova): `--gravar`
escreve a secao nova da serie, com a data, e o portao volta a verde. Titulo que
mudou no ar SEM ninguem trocar — ou promessa que sumiu — e desembarque que
quebrou, e o conserto e a secao 20.4/20.5: ler o log da revisao no `/status`
linha por linha e reacionar o Sync.

**ATENCAO DE CALENDARIO, escrita aqui para ninguem se enganar:** entre hoje e
21/10/2026 a leitura semanal PROIBE mexer em titulo e meta desta ilha — mexer
destroi a medicao de CTR em curso. Este portao MEDE e nao conserta superficie:
vermelho aqui antes de 21/10 significa desembarque quebrado, nunca autorizacao
para reescrever titulo.
"""
import importlib.util
import json
import os
import subprocess
import sys
import time
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
SERIE = os.path.join(RAIZ, "dados", "titulos-no-ar.md")

SITE = "https://aquametria.com.br"
SITEMAP = SITE + "/wp-sitemap.xml"

# O teto do que o Google mostra antes de cortar. E o mesmo numero do
# `teste-promessa-do-titulo.py`, do `teste-titulos-das-duas-fontes.py` e do
# `teste-voz.mjs` — e nao e uma quarta regua: aqueles tres medem a frase do
# REPOSITORIO e este mede a frase do AR, que e outra medicao do mesmo teto.
TETO = 65

GRAVAR = "--gravar" in sys.argv[1:]


def carregar_regua():
    caminho = os.path.join(FERRAMENTAS, "regua-titulo-no-ar.py")
    spec = importlib.util.spec_from_file_location("regua_titulo_no_ar", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()

falhas = []


def ok(rotulo, condicao, detalhe=""):
    if condicao:
        print("  ok   %s" % rotulo)
    else:
        print("  FALHA %s%s" % (rotulo, (" — " + detalhe) if detalhe else ""))
        falhas.append(rotulo)


def buscar(url):
    """GET com quebra-cache e cabecalho honesto, como as irmas desta pasta."""
    sep = "&" if "?" in url else "?"
    pedido = urllib.request.Request(
        url + sep + "v=" + time.strftime("%H%M%S"),
        headers={"User-Agent": "Aquametria/conferir-titulo-no-ar (Arquipelago)"})
    with urllib.request.urlopen(pedido, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def urls_do_sitemap():
    """Toda URL que a ilha PUBLICA, lida do indice e dos sub-sitemaps.

    A lista sai do ar e nao de um arquivo do repositorio de proposito: o que
    este portao mede e o que o site serve, e uma lista digitada aqui ficaria
    para tras na primeira leva — a doenca que a `bancada.py` desta pasta nasceu
    para matar em 22/09/2026.
    """
    status, xml = buscar(SITEMAP)
    if status != 200:
        return status, []
    urls = []
    for sub in regua.locs(xml):
        _, pedaco = buscar(sub)
        urls += regua.locs(pedaco)
    return status, sorted(set(urls))


def mapa_de_promessas():
    """{slug: {titulo, promessa}} perguntado ao PROPRIO snippet.

    Nao reimplemento a promessa: o `listar-promessas.php` chama o provedor de
    cada calculadora e da ficha do betta e devolve a frase resolvida. Se ele
    falhar, o portao reprova em vez de seguir sem a afirmacao 4 — portao que
    perde uma afirmacao em silencio e verde vazio com outro nome.
    """
    script = os.path.join(FERRAMENTAS, "listar-promessas.php")
    p = subprocess.Popen(["php", script, RAIZ],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = p.communicate()
    if p.returncode != 0:
        return None, erro.decode("utf-8", "replace")
    return json.loads(saida.decode("utf-8")), ""


def url_do_slug(urls, slug):
    """A URL do sitemap cujo ultimo degrau e este slug. None se nao houver.

    Devolve None em vez de montar endereco: promessa declarada para pagina que
    o sitemap nao publica e defeito, e o portao tem de dizer isso em vez de
    abrir uma URL inventada e receber 404.
    """
    for u in urls:
        if regua.slug_da_url(u) == slug:
            return u
    return None


def cabecalho_da_serie():
    return (
        "# Serie do TITULO SERVIDO NO AR — Aquametria\n"
        "\n"
        "O `<title>` e a `<meta name=\"description\">` que cada URL do\n"
        "`wp-sitemap.xml` desta ilha SERVE, com as entidades decodificadas — que e\n"
        "como a tela conta. Escreve aqui o\n"
        "`ferramentas/conferir-titulo-no-ar.py --gravar`; quem confere e o mesmo\n"
        "arquivo sem a opcao, e ele compara PAGINA POR PAGINA, nao pelo total.\n"
        "\n"
        "**Secao nova vai no TOPO** (a serie cresce por cima, como\n"
        "`dados/posicoes.md`, `dados/cano-de-links.md` e\n"
        "`dados/deriva-do-catalogo.md`) e secao antiga NUNCA e sobrescrita: a serie\n"
        "so vale porque cresce. O bloco `json` de cada secao e a declaracao que o\n"
        "portao le — o primeiro do arquivo e o que manda.\n"
        "\n"
        "**POR QUE ELA NASCEU EM 19/10/2026, dois dias antes de ser cobrada.** A\n"
        "linha de 14/10 do `dados/posicoes.md` diz: *\"NAO COPIEI os `<title>`\n"
        "servidos para esta serie (...) A leitura de 21/10 e a primeira em que\n"
        "copiar o titulo servido significa alguma coisa — e ai e OBRIGATORIO.\"* O\n"
        "critErio de pronto da Proposta 1 e da Proposta 2 da leitura de 07/10 pede\n"
        "o titulo servido no dia da medicao. Esta serie e esse titulo, **medido e\n"
        "nao copiado da aba** — a leitura de 21/10 cita a secao desta data em vez\n"
        "de transcrever 52 frases a mao.\n"
        "\n"
        "Titulo que muda **nao e defeito**: leva nova, promessa nova e pagina nova\n"
        "movem estas frases por desenho. O que e defeito e titulo que mudou no ar e\n"
        "ninguem declarou — que e a cicatriz de 11/09/2026 desta ilha, quando 293\n"
        "afirmacoes de bancada ficaram verdes com os nove titulos do ar sendo os de\n"
        "antes.\n"
    )


def gravar(medido, promessa_por_url, agora, revisao):
    dados = {
        "medido_em": agora,
        "revisao_do_status": revisao,
        "site": SITE,
        "teto": TETO,
        "totais": regua.totais(medido),
        "promessas": promessa_por_url,
        "paginas": medido,
    }
    t = dados["totais"]
    secao = ["## %s" % agora, ""]
    secao.append("**%d URL(s)** do `wp-sitemap.xml`, abertas uma a uma com quebra de cache. "
                 "Revisao do `/status` na medicao: **%s**." % (t["paginas"], revisao))
    secao.append("")
    secao.append("| o que | quanto |")
    secao.append("|---|---|")
    secao.append("| URLs sem `<title>` | **%d** |" % t["sem_titulo"])
    secao.append("| URLs sem `<meta name=\"description\">` | **%d** |" % t["sem_descricao"])
    secao.append("| `<title>` com algarismo (a promessa da banda 4 a 10) | **%d** |" % t["com_digito"])
    secao.append("| o `<title>` mais longo, decodificado (teto %d) | **%d** |" % (TETO, t["titulo_mais_longo"]))
    secao.append("")
    if promessa_por_url:
        secao.append("**AS PROMESSAS QUE CHEGARAM AO AR**, com o `<title>` servido inteiro "
                     "— e esta tabela e a que a leitura semanal cita:")
        secao.append("")
        secao.append("| URL | promessa que o snippet resolve | `<title>` servido | n |")
        secao.append("|---|---|---|---|")
        for url in sorted(promessa_por_url):
            e = medido.get(url, {})
            secao.append("| `%s` | %s | %s | %d |"
                         % (url, promessa_por_url[url], e.get("titulo", ""), e.get("n", 0)))
        secao.append("")
    secao += ["```json", json.dumps(dados, ensure_ascii=False, indent=2, sort_keys=True), "```", ""]
    novo = "\n".join(secao) + "\n"

    if os.path.exists(SERIE):
        antigo = regua.ler(SERIE)
        corte = antigo.find("\n## ")
        if corte == -1:
            texto = antigo.rstrip("\n") + "\n\n" + novo
        else:
            texto = antigo[:corte + 1] + "\n" + novo + antigo[corte + 1:]
    else:
        texto = cabecalho_da_serie() + "\n" + novo
    with open(SERIE, "w", encoding="utf-8") as f:
        f.write(texto)
    print("serie gravada: %s" % os.path.relpath(SERIE, RAIZ))


def revisao_do_status():
    """A revisao que o `/status` declara, para a secao da serie dizer CONTRA
    QUE DESEMBARQUE ela foi medida. Nao e afirmacao: quem afirma revisao e o
    `conferir-desembarque.py`, pela 20.4. Aqui ela e procedencia."""
    try:
        _, corpo = buscar(SITE + "/wp-json/aquametria/v1/status")
        return str(json.loads(corpo).get("revisao", "?"))
    except Exception as erro:          # noqa: BLE001 — procedencia, nao portao
        return "nao lida (%s)" % type(erro).__name__


def main():
    agora = time.strftime("%Y-%m-%d %H:%MZ", time.gmtime())
    print("TITULO SERVIDO NO AR — %s, %s" % (SITE, agora))
    print("")

    status, urls = urls_do_sitemap()
    ok("o indice do sitemap responde 200", status == 200, "respondeu %s" % status)
    ok("o sitemap trouxe URL (verde vazio nao passa por aprovado)",
       len(urls) > 0, "%d URL(s)" % len(urls))
    if not urls:
        print("")
        print("REPROVADO: sem URL nenhuma nao ha o que medir.")
        return 1

    paginas, quebradas = {}, []
    for u in urls:
        try:
            st, html = buscar(u)
        except Exception as erro:      # noqa: BLE001
            quebradas.append("%s (%s)" % (u, type(erro).__name__))
            continue
        if st != 200:
            quebradas.append("%s (HTTP %s)" % (u, st))
            continue
        paginas[u] = html

    ok("as %d URLs do sitemap foram abertas" % len(urls),
       not quebradas and len(paginas) == len(urls),
       "nao abriram: %s" % quebradas[:3])

    medido = regua.medir(paginas)
    t = regua.totais(medido)
    print("")
    print("MEDIDO: %d pagina(s), %d com algarismo no titulo, mais longo %d de %d"
          % (t["paginas"], t["com_digito"], t["titulo_mais_longo"], TETO))
    print("")

    ok("toda URL serve <title>", not regua.sem_titulo(medido),
       "sem titulo: %s" % regua.sem_titulo(medido)[:3])
    ok("toda URL serve <meta name=\"description\">", not regua.sem_descricao(medido),
       "sem descricao: %s" % regua.sem_descricao(medido)[:3])
    ok("nenhum <title> servido passa de %d caracteres decodificados" % TETO,
       not regua.acima_do_teto(medido, TETO),
       "acima do teto: %s" % regua.acima_do_teto(medido, TETO)[:3])

    mapa, erro = mapa_de_promessas()
    ok("o listar-promessas.php respondeu (sem ele a afirmacao da promessa nao existe)",
       mapa is not None, erro.strip()[:200])

    promessa_por_url = {}
    if mapa is not None:
        declaradas = regua.promessas(mapa)
        ok("o snippet declara promessa em alguma pagina", len(declaradas) > 0,
           "nenhuma promessa resolvida")
        for slug in sorted(declaradas):
            url = url_do_slug(urls, slug)
            ok("a pagina que promete '%s' esta no sitemap" % slug, url is not None)
            if url is None:
                continue
            promessa_por_url[url] = declaradas[slug]
            ok("%s serve a promessa %r" % (slug, declaradas[slug]),
               regua.promessa_chegou(medido.get(url, {}), declaradas[slug]),
               "servido %r" % medido.get(url, {}).get("titulo", ""))

        # A pagina de CONTROLE nao e digitada aqui: ela e a calculadora que o
        # proprio mapa devolve com promessa VAZIA. Decidida na Proposta 2 da
        # leitura de 07/10 e protegida pela de 14/10 — "quem der promessa a ela
        # antes de 21/10 destroi o unico controle do arquipelago".
        controles = sorted(s for s, l in mapa.items()
                           if s.startswith("calculadora-") and not (l.get("promessa") or "").strip())
        ok("existe calculadora de controle, sem promessa declarada", len(controles) > 0,
           "nenhuma — o controle da medicao de CTR desapareceu")
        for slug in controles:
            url = url_do_slug(urls, slug)
            if url is None:
                continue
            ok("o controle %s continua sem promessa no ar (nenhum algarismo no titulo)" % slug,
               regua.sem_promessa(medido.get(url, {})),
               "servido %r" % medido.get(url, {}).get("titulo", ""))

    if GRAVAR:
        print("")
        gravar(medido, promessa_por_url, agora, revisao_do_status())
        return 0 if not falhas else 1

    print("")
    declarado = regua.declaracao(SERIE)
    ok("a serie do titulo no ar tem declaracao", declarado is not None,
       "escreva a primeira com --gravar")
    novas, sumidas, mudadas = regua.comparar_com_declaracao(medido, declarado)
    ok("o titulo servido e o declarado sao o mesmo, pagina por pagina",
       not novas and not sumidas and not mudadas,
       "novas: %s | sumidas: %s | mudadas: %s" % (novas[:2], sumidas[:2], mudadas[:2]))
    if declarado is not None:
        ok("os totais declarados saem das paginas declaradas, e nao de um numero ao lado",
           declarado.get("totais") == regua.totais(declarado.get("paginas", {})),
           "totais %s contra %s" % (declarado.get("totais"),
                                    regua.totais(declarado.get("paginas", {}))))

    print("")
    if falhas:
        print("REPROVADO: %d afirmacao(oes)" % len(falhas))
        for f in falhas:
            print("  - %s" % f)
        print("")
        print("Titulo trocado de proposito? grave a secao nova da serie:")
        print("  python3 ferramentas/conferir-titulo-no-ar.py --gravar")
        print("Titulo que mudou no ar sem ninguem trocar e desembarque quebrado:")
        print("  secao 20.4/20.5 do ARQUIPELAGO.md — ler o log do /status e reacionar o Sync.")
        return 1
    print("APROVADO: %d pagina(s) no ar, titulo e descricao declarados pagina por pagina,"
          % t["paginas"])
    print("          %d promessa(s) chegando ao ar e o controle sem nenhuma." % len(promessa_por_url))
    return 0


if __name__ == "__main__":
    sys.exit(main())

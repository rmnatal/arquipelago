#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-titulo-no-ar.py` contra HTML ENCENADO
e o portao inteiro contra uma ILHA DE SOMBRA.

    python3 ferramentas/teste-titulo-no-ar.py

POR QUE ELE EXISTE, e nao e para repetir o que o portao ja diz
--------------------------------------------------------------
O `conferir-titulo-no-ar.py` abre o site: ele prova que o mundo de HOJE passa, e
nao prova que a regua MORDE. Esta bancada roda a mesma leitura contra HTML que
eu escrevo, inclusive HTML quebrado de proposito — e contra uma ilha de sombra,
onde o portao inteiro roda com a rede trocada por paginas de mentira.

AS SEIS METADES, e cada uma existe por um defeito possivel
----------------------------------------------------------
  (A) A LEITURA. `<title>` com entidade, com quebra de linha no meio, com
      atributo na tag, ausente, vazio; meta description nas duas grafias de
      aspas e ausente. **A decodificacao e o ponto:** `&#8211;` e 1 caractere na
      tela e 7 na fonte, e o teto de 65 e da tela — regua que mede a fonte
      aprova titulo que o Google corta.

  (B) A PROMESSA. Promessa que chegou, promessa que NAO chegou (o titulo voltou
      a nome + marca, que e o desembarque silencioso da cicatriz de 11/09/2026),
      promessa vazia que nao e promessa, e o mapa do `listar-promessas.php` lido
      como DADO — e por isso encenavel sem subir PHP.

  (C) O CONTROLE. Titulo sem algarismo e o controle intacto; titulo com
      algarismo e o controle perdido. A leitura de 14/10 escreveu o preco: sem o
      controle, a leitura de 21/10 credita as promessas um ganho que elas nao
      produziram.

  (D) O VERDE VAZIO. Zero pagina lida nao acha defeito nenhum: `acima_do_teto`,
      `sem_titulo` e `sem_descricao` devolvem lista vazia sobre nada, e os
      totais dizem `paginas: 0`. E a unica forma de este portao mentir sem
      ninguem editar uma linha dele, e por isso o portao afirma que o sitemap
      trouxe URL.

  (E) A COMPARACAO PAGINA POR PAGINA, e e a metade que mais importa. **Duas
      paginas TROCANDO de titulo entre si deixam todos os totais identicos** —
      numero de paginas, de digitos, de sem-titulo e o titulo mais longo — e a
      comparacao item por item acusa as duas. E a licao que a serie da deriva
      aprendeu em 16/10/2026 (*"74 linhas podem virar 74 OUTRAS linhas sem o
      total mudar"*) e que a do cano reaprendeu em 19/10.

  (F) O PORTAO INTEIRO NUMA ILHA DE SOMBRA: verde com a serie, vermelho sem
      ela, vermelho na troca de titulo com total intacto, vermelho com pagina
      nova, vermelho com declaracao cujo total nao fecha com as proprias
      paginas, e verde de novo depois do `--gravar`. A rede e trocada por um
      mapa de paginas: o portao nao sabe que nao esta no ar.
"""
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
# TETO_ENCENADO ENCENADO, E O NOME E O CONSERTO (19/10/2026)
# -------------------------------------------------
# Este numero NAO e o teto da ilha e nao se le do snippet: e dado de teste. A
# `regua-titulo-no-ar.py` recebe o teto como ARGUMENTO (`acima_do_teto(medido,
# teto)`), e as afirmacoes daqui montam titulos de exatamente este tamanho e de
# um a mais para medir a borda da regua. Ler o snippet aqui desligaria a propria
# medicao: no dia em que o teto mudasse, as cadeias de "a" continuariam do
# tamanho antigo e a borda deixaria de ser borda.
# O que estava errado era o NOME. Ele se chamava `TETO`, com o numero digitado ao
# lado, identico ao dos portoes que afirmam sobre a ILHA, e nenhum leitor
# distinguia encenacao de divida — foi
# por isso que o achado 11 do fecho das 13h27Z contou QUATRO arquivos quando a
# varredura desta passada achou CINCO. A `regua-teto-do-titulo.py` denuncia o nome
# `TETO` com numero digitado ao lado, e deixa este passar pelo nome: encenacao
# que se declara
# encenacao nao e divida, e encenacao disfarcada de decisao e.
TETO_ENCENADO = 65

contadas = [0]
falhas = []


def ultima(saida):
    """A ULTIMA linha util da saida do portao. O detalhe do `ok()` sai sempre, e
    despejar a saida inteira do portao aqui afoga a bancada em texto que nao e
    afirmacao de ninguem."""
    linhas = [l for l in (saida or "").strip().split("\n") if l.strip()]
    return linhas[-1].strip()[:110] if linhas else "(sem saida)"


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


def carregar_regua(caminho=None):
    caminho = caminho or os.path.join(FERRAMENTAS, "regua-titulo-no-ar.py")
    spec = importlib.util.spec_from_file_location("regua_titulo_no_ar_t", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()


def pagina(titulo="Um titulo", descricao="Uma descricao", aspas='"'):
    """HTML minimo e crivel: as duas tags que esta regua le, e nada mais."""
    partes = ["<!DOCTYPE html><html><head>"]
    if titulo is not None:
        partes.append("<title>%s</title>" % titulo)
    if descricao is not None:
        partes.append("<meta name=%sdescription%s content=%s%s%s />"
                      % (aspas, aspas, aspas, descricao, aspas))
    partes.append("</head><body><h1>oi</h1></body></html>")
    return "".join(partes)


# ---------------------------------------------------------------- (A) leitura
def metade_a():
    print("(A) A LEITURA DO QUE O AR SERVE\n")

    ok("le o <title> simples", regua.titulo(pagina(titulo="Oi")) == "Oi")
    ok("le o <title> com atributo na tag",
       regua.titulo('<title lang="pt">Oi</title>') == "Oi")
    ok("<title> ausente devolve string vazia, nao erro",
       regua.titulo(pagina(titulo=None)) == "")
    ok("<title> vazio devolve string vazia", regua.titulo("<title></title>") == "")

    # A decodificacao e o motivo desta regua existir separada do olho humano.
    bruto = "Quanta luz? &#8211; de 10 a 60 lm"
    lido = regua.titulo("<title>%s</title>" % bruto)
    ok("DECODIFICA a entidade: &#8211; vira um caractere so",
       lido == "Quanta luz? – de 10 a 60 lm", repr(lido))
    # A afirmacao e a RELACAO, nao dois numeros digitados: `&#8211;` sao 7
    # caracteres na fonte e 1 na tela, logo a tela conta exatamente 6 menos.
    # Numero digitado aqui envelheceria no dia em que eu mudasse a frase de
    # exemplo — e foi o que aconteceu na primeira escrita deste arquivo.
    ok("e o tamanho medido e o da TELA, nao o da fonte (%d contra %d)"
       % (len(lido), len(bruto)), len(lido) == len(bruto) - 6,
       "%d contra %d" % (len(lido), len(bruto)))
    ok("decodifica &amp; e &#038;, que e o que o wptexturize desta ilha produz",
       regua.titulo("<title>a &amp; b &#038; c</title>") == "a & b & c")
    ok("quebra de linha dentro do <title> nao duplica espaco",
       regua.titulo("<title>Oi\n   mundo</title>") == "Oi mundo")

    ok("le a meta description com aspas duplas",
       regua.descricao(pagina(descricao="Uma frase")) == "Uma frase")
    ok("le a meta description com aspas simples",
       regua.descricao(pagina(descricao="Uma frase", aspas="'")) == "Uma frase")
    ok("meta description ausente devolve string vazia",
       regua.descricao(pagina(descricao=None)) == "")

    ok("o slug e o ultimo degrau do caminho",
       regua.slug_da_url("https://x.com.br/peixes/bettas/quantos-litros-para-betta/")
       == "quantos-litros-para-betta")
    ok("a raiz nao tem degrau e devolve string vazia",
       regua.slug_da_url("https://x.com.br/") == "")
    ok("a quebra de cache nao entra no slug",
       regua.slug_da_url("https://x.com.br/calculadora-de-litragem/?v=1234")
       == "calculadora-de-litragem")
    ok("locs() tira a quebra de cache das URLs do sitemap",
       regua.locs("<loc>https://x.com.br/a/?v=1</loc><loc>https://x.com.br/b/</loc>")
       == ["https://x.com.br/a/", "https://x.com.br/b/"])
    print("")


# --------------------------------------------------------------- (B) promessa
def mapa_encenado():
    """O que o `listar-promessas.php` devolve, encenado. Ele e DADO aqui."""
    return {
        "inicio": {"titulo": "As contas", "promessa": ""},
        "calculadora-de-litragem": {"titulo": "Quantos litros tem?", "promessa": ""},
        "calculadora-de-iluminacao": {"titulo": "Quanta luz?", "promessa": "de 10 a 60 lm por litro"},
        "calculadora-de-midia-filtrante": {"titulo": "Quanta midia?", "promessa": "de 1,25 a 12,5 mL/L"},
        "quantos-litros-para-betta": {"titulo": "Quantos litros para um betta?", "promessa": "de 40,5 a 54 litros"},
    }


def metade_b():
    print("(B) A PROMESSA QUE O SNIPPET RESOLVE CHEGOU AO AR?\n")

    declaradas = regua.promessas(mapa_encenado())
    ok("so as paginas com promessa nao vazia entram", sorted(declaradas) ==
       ["calculadora-de-iluminacao", "calculadora-de-midia-filtrante",
        "quantos-litros-para-betta"], str(sorted(declaradas)))
    ok("promessa vazia NAO entra — ela e o estado do controle",
       "calculadora-de-litragem" not in declaradas)
    ok("mapa vazio devolve nenhuma promessa, sem erro", regua.promessas({}) == {})
    ok("mapa None devolve nenhuma promessa, sem erro", regua.promessas(None) == {})
    ok("promessa so de espaco nao conta como promessa",
       regua.promessas({"x": {"promessa": "   "}}) == {})

    chegou = regua.estado(pagina(titulo="Quanta luz? &#8211; de 10 a 60 lm por litro"))
    ok("a promessa chegou ao ar",
       regua.promessa_chegou(chegou, "de 10 a 60 lm por litro"))

    # O desembarque silencioso: as tres travas da promessa fecham e o titulo
    # volta a nome + marca, que e sempre valido. E a cicatriz de 11/09/2026.
    caiu = regua.estado(pagina(titulo="Quanta luz? &#8211; Aquametria"))
    ok("promessa que NAO chegou e pega: o titulo voltou a nome + marca",
       not regua.promessa_chegou(caiu, "de 10 a 60 lm por litro"))
    ok("e o titulo do fallback continua VALIDO — e isso que o faz silencioso",
       caiu["titulo"] and caiu["n"] <= TETO_ENCENADO and not caiu["digito"])

    # Promessa que chega PELA METADE e promessa que nao chegou: 'de 10 a 60' nao
    # e 'de 10 a 60 lm por litro', e o `in` separa os dois.
    metade = regua.estado(pagina(titulo="Quanta luz? – de 10 a 60"))
    ok("promessa truncada nao passa por chegada",
       not regua.promessa_chegou(metade, "de 10 a 60 lm por litro"))
    ok("promessa_chegou sobre estado vazio nao explode",
       not regua.promessa_chegou({}, "x") and not regua.promessa_chegou(None, "x"))
    print("")


# --------------------------------------------------------------- (C) controle
def metade_c():
    print("(C) O CONTROLE DA MEDICAO DE CTR CONTINUA SEM PROMESSA?\n")

    intacto = regua.estado(pagina(titulo="Quantos litros tem o seu aquário? &#8211; Aquametria"))
    ok("controle intacto: nenhum algarismo no titulo servido", regua.sem_promessa(intacto))
    ok("e `digito` diz o mesmo pelo outro lado", not intacto["digito"])

    perdido = regua.estado(pagina(titulo="Quantos litros tem? &#8211; de 1 a 1.000 litros"))
    ok("controle PERDIDO e pego: o titulo ganhou algarismo",
       not regua.sem_promessa(perdido))
    ok("sem_promessa sobre estado vazio nao explode",
       regua.sem_promessa({}) and regua.sem_promessa(None))
    print("")


# ------------------------------------------------------------ (D) verde vazio
def metade_d():
    print("(D) O VERDE VAZIO — zero pagina lida nao acha defeito nenhum\n")

    vazio = regua.medir({})
    ok("medir({}) devolve nada", vazio == {})
    ok("acima_do_teto sobre nada: lista vazia", regua.acima_do_teto(vazio, TETO_ENCENADO) == [])
    ok("sem_titulo sobre nada: lista vazia", regua.sem_titulo(vazio) == [])
    ok("sem_descricao sobre nada: lista vazia", regua.sem_descricao(vazio) == [])
    # O try/except nao e zelo: `max([])` explode, e excecao aqui derruba a
    # bancada ANTES de ela dizer o que mediu — reprovar por traceback e
    # reprovar sem afirmacao. A mutacao 12 e exatamente este caso.
    try:
        t = regua.totais(vazio)
        explodiu = ""
    except Exception as erro:          # noqa: BLE001
        t, explodiu = {}, type(erro).__name__
    ok("e os totais dizem paginas: 0, em vez de calar",
       not explodiu and t.get("paginas") == 0, explodiu or str(t))
    ok("titulo_mais_longo sobre nada e 0, nao erro de max()",
       not explodiu and t.get("titulo_mais_longo") == 0, explodiu)
    try:
        ok("os totais sobre None tambem nao explodem", regua.totais(None)["paginas"] == 0)
    except Exception as erro:          # noqa: BLE001
        ok("os totais sobre None tambem nao explodem", False, type(erro).__name__)

    # O teto morde: 66 reprova, 65 passa. A fronteira medida nos dois lados.
    sessenta_e_cinco = regua.medir({"u": pagina(titulo="a" * 65)})
    sessenta_e_seis = regua.medir({"u": pagina(titulo="a" * 66)})
    ok("titulo de 65 nao esta acima do teto", regua.acima_do_teto(sessenta_e_cinco, TETO_ENCENADO) == [])
    ok("titulo de 66 esta acima do teto", regua.acima_do_teto(sessenta_e_seis, TETO_ENCENADO) == ["u"])
    ok("e a entidade e decodificada ANTES de medir o teto: 65 na tela passa",
       regua.acima_do_teto(regua.medir({"u": pagina(titulo="a" * 64 + "&#8211;")}), TETO_ENCENADO) == [])

    ok("sem_titulo acha a pagina sem <title>",
       regua.sem_titulo(regua.medir({"u": pagina(titulo=None)})) == ["u"])
    ok("sem_descricao acha a pagina sem meta description",
       regua.sem_descricao(regua.medir({"u": pagina(descricao=None)})) == ["u"])
    print("")


# ------------------------------------- (E) a comparacao, e a troca de titulos
def metade_e():
    print("(E) PAGINA POR PAGINA — a troca de titulos com total INTACTO\n")

    antes = regua.medir({
        "https://x/a/": pagina(titulo="Titulo de A", descricao="Descricao de A"),
        "https://x/b/": pagina(titulo="Titulo de B", descricao="Descricao de B"),
    })
    declarado = {"totais": regua.totais(antes), "paginas": antes}

    novas, sumidas, mudadas = regua.comparar_com_declaracao(antes, declarado)
    ok("mundo igual ao declarado: nenhuma divergencia",
       not novas and not sumidas and not mudadas, str((novas, sumidas, mudadas)))

    # A TROCA: A passa a servir o titulo de B e B o de A. Todos os totais ficam
    # identicos, e a comparacao por total ficaria VERDE sobre duas paginas
    # erradas.
    depois = regua.medir({
        "https://x/a/": pagina(titulo="Titulo de B", descricao="Descricao de B"),
        "https://x/b/": pagina(titulo="Titulo de A", descricao="Descricao de A"),
    })
    ok("a troca deixa TODOS os totais identicos — e por isso total nao serve",
       regua.totais(depois) == regua.totais(antes), str(regua.totais(depois)))
    novas, sumidas, mudadas = regua.comparar_com_declaracao(depois, declarado)
    ok("e a comparacao pagina por pagina acusa AS DUAS", len(mudadas) == 2, str(mudadas))
    ok("a frase da divergencia nomeia o servido e o declarado",
       all("servido" in m and "declarado" in m for m in mudadas), str(mudadas))
    ok("e nomeia QUAL campo divergiu — aqui o titulo",
       all("titulo servido" in m for m in mudadas), str(mudadas))

    nova = dict(antes)
    nova["https://x/c/"] = regua.estado(pagina(titulo="Titulo de C"))
    novas, sumidas, mudadas = regua.comparar_com_declaracao(nova, declarado)
    ok("pagina NOVA no ar sem declaracao e acusada", novas == ["https://x/c/"], str(novas))

    menos = {"https://x/a/": antes["https://x/a/"]}
    novas, sumidas, mudadas = regua.comparar_com_declaracao(menos, declarado)
    ok("pagina que SAIU do ar e acusada", sumidas == ["https://x/b/"], str(sumidas))

    # A descricao tambem e comparada: titulo igual e descricao trocada e
    # divergencia, porque a meta e a outra metade da alavanca de CTR.
    so_descricao = regua.medir({
        "https://x/a/": pagina(titulo="Titulo de A", descricao="OUTRA"),
        "https://x/b/": pagina(titulo="Titulo de B", descricao="Descricao de B"),
    })
    novas, sumidas, mudadas = regua.comparar_com_declaracao(so_descricao, declarado)
    ok("descricao trocada com titulo igual TAMBEM e divergencia", len(mudadas) == 1, str(mudadas))
    # E aqui a frase tem de falar de DESCRICAO, nao de titulo: com o titulo
    # igual nos dois lados, uma frase que cite o titulo manda quem le procurar
    # defeito no campo que esta certo.
    ok("e a frase nomeia a DESCRICAO, nao o titulo que esta igual",
       mudadas and "descricao servido" in mudadas[0] and "titulo servido" not in mudadas[0],
       str(mudadas))

    ok("declaracao ausente nao e tratada como zero: e acusada como ausente",
       regua.comparar_com_declaracao(antes, None)[0] == ["a serie nao tem declaracao nenhuma"])
    print("")


# ------------------------------------------- (F) o portao numa ilha de sombra
SONDA = '''
# --- ENCENACAO DA REDE PELO teste-titulo-no-ar.py: sem isto o portao abriria o site.
import json as _j, io as _io, os as _os
_MUNDO = _j.load(_io.open(_os.path.join(RAIZ, "mundo-encenado.json"), encoding="utf-8"))


def buscar(url):
    limpa = url.split("?")[0]
    if limpa.endswith("/wp-sitemap.xml"):
        return 200, "".join("<loc>%s</loc>" % u for u in ["%s/sub.xml" % SITE])
    if limpa.endswith("/sub.xml"):
        return 200, "".join("<loc>%s</loc>" % u for u in sorted(_MUNDO["paginas"]))
    if limpa.endswith("/status"):
        return 200, _j.dumps({"revisao": _MUNDO.get("revisao", 0)})
    if limpa in _MUNDO["paginas"]:
        return 200, _MUNDO["paginas"][limpa]
    return 404, ""


def mapa_de_promessas():
    if _MUNDO.get("promessas_falham"):
        return None, "o listar-promessas.php falhou de proposito"
    return _MUNDO["mapa"], ""
'''


# O TETO DA ILHA DE SOMBRA, E ELE NAO E 65 DE PROPOSITO (19/10/2026)
# ------------------------------------------------------------------
# Desde 19/10 o `conferir-titulo-no-ar.py` nao digita mais o teto: ele pergunta
# a `regua-teto-do-titulo.py`, que pergunta ao snippet da ilha (achado 11 do
# fecho das 13h27Z). A ilha de sombra nao tinha snippet nenhum, e por isso o
# portao parou de subir aqui na primeira passada deste conserto.
#
# A SAIDA NAO FOI COPIAR A ILHA DE VERDADE PARA DENTRO DA SOMBRA. Sombra que
# precisa da ilha inteira deixa de ser encenacao. A saida foi dar a sombra um
# snippet SEU, com as tres constantes, e com o teto num numero DIFERENTE do da
# ilha — e isso vira a prova que o conserto precisava: se o portao da sombra
# relatar 60, o numero viajou do snippet daquela ilha ate a medicao, e nao
# estava escrito em lugar nenhum do portao. Teto igual a 65 provaria nada,
# porque e o numero que o codigo teria se continuasse redigitado.
#
# 60 cabe na banda crivel da regua e e maior que o titulo mais longo de qualquer
# mundo encenado aqui (37 caracteres), entao nenhuma afirmacao antiga muda de
# cor por causa dele. O que muda de cor se o conserto for desfeito e a
# afirmacao nova da metade (F).
TETO_DA_SOMBRA = 60

# SEM `<?php` DE PROPOSITO, e e convencao desta ilha e nao descuido: os snippets
# de `snippets/` sao o que o Code Snippets guarda, ou seja PHP CRU, e o
# `render-para-teste.php` os carrega com `eval()` — que recusa a tag de abertura
# com erro de sintaxe. A primeira versao deste texto tinha a tag e o portao da
# sombra reprovou com "PHP Parse error".
SNIPPET_DE_SOMBRA = """/* Snippet de sombra escrito pelo teste-titulo-no-ar.py: so as tres constantes
   do titulo, com o teto de proposito DIFERENTE do da ilha de verdade. */
if ( ! defined( 'AQUAMETRIA_TITULO_TETO' ) ) {
	define( 'AQUAMETRIA_TITULO_TETO', %d );
}
if ( ! defined( 'AQUAMETRIA_TITULO_SEPARADOR' ) ) {
	define( 'AQUAMETRIA_TITULO_SEPARADOR', ' – ' );
}
if ( ! defined( 'AQUAMETRIA_TITULO_MARCA' ) ) {
	define( 'AQUAMETRIA_TITULO_MARCA', 'Aquametria' );
}
"""


def ilha_de_sombra(mundo, teto=None):
    tmp = tempfile.mkdtemp(prefix="aqm-teste-titulo-ar-")
    os.makedirs(os.path.join(tmp, "ferramentas"))
    os.makedirs(os.path.join(tmp, "dados"))
    os.makedirs(os.path.join(tmp, "snippets"))
    for nome in ("regua-titulo-no-ar.py", "conferir-titulo-no-ar.py",
                 "regua-teto-do-titulo.py", "listar-teto-do-titulo.php",
                 "render-para-teste.php"):
        shutil.copy(os.path.join(FERRAMENTAS, nome), os.path.join(tmp, "ferramentas", nome))
    with io.open(os.path.join(tmp, "snippets", "aquametria-teto-de-sombra.php"),
                 "w", encoding="utf-8") as f:
        f.write(SNIPPET_DE_SOMBRA % (TETO_DA_SOMBRA if teto is None else teto))
    # A sonda entra NO FIM do portao, depois das definicoes: em Python a ultima
    # definicao do nome e a que vale, e e assim que a rede sai sem eu editar o
    # corpo do portao — que e o que o teste existe para medir intacto.
    caminho = os.path.join(tmp, "ferramentas", "conferir-titulo-no-ar.py")
    texto = io.open(caminho, encoding="utf-8").read()
    marca = 'if __name__ == "__main__":'
    texto = texto.replace(marca, SONDA + "\n\n" + marca, 1)
    with io.open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)
    with io.open(os.path.join(tmp, "mundo-encenado.json"), "w", encoding="utf-8") as f:
        json.dump(mundo, f, ensure_ascii=False)
    return tmp


def rodar_portao(ilha, *args):
    p = subprocess.Popen(
        [sys.executable, os.path.join(ilha, "ferramentas", "conferir-titulo-no-ar.py")] + list(args),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def mundo_bom():
    base = "https://aquametria.com.br"
    return {
        "revisao": 122,
        "mapa": {
            "calculadora-de-litragem": {"titulo": "Quantos litros tem?", "promessa": ""},
            "calculadora-de-iluminacao": {"titulo": "Quanta luz?",
                                          "promessa": "de 10 a 60 lm por litro"},
        },
        "paginas": {
            base + "/": pagina(titulo="As contas do seu aquário &#8211; Aquametria"),
            base + "/calculadora-de-litragem/":
                pagina(titulo="Quantos litros tem? &#8211; Aquametria"),
            base + "/calculadora-de-iluminacao/":
                pagina(titulo="Quanta luz? &#8211; de 10 a 60 lm por litro"),
        },
    }


def metade_f():
    print("(F) O PORTAO INTEIRO, NUMA ILHA DE SOMBRA\n")

    ilha = ilha_de_sombra(mundo_bom())
    try:
        codigo, saida = rodar_portao(ilha)
        ok("sem serie o portao REPROVA, e nomeia a declaracao ausente",
           codigo == 1 and "a serie do titulo no ar tem declaracao" in saida, ultima(saida))

        codigo, saida = rodar_portao(ilha, "--gravar")
        ok("--gravar escreve a serie e sai 0", codigo == 0, ultima(saida))
        serie = os.path.join(ilha, "dados", "titulos-no-ar.md")
        ok("a serie existe no disco", os.path.exists(serie))
        corpo = io.open(serie, encoding="utf-8").read()
        ok("a serie traz o titulo servido DECODIFICADO, para a leitura semanal copiar",
           "Quanta luz? – de 10 a 60 lm por litro" in corpo)
        ok("a serie traz a revisao do /status como procedencia", "122" in corpo)
        ok("a serie traz a tabela das promessas que chegaram",
           "AS PROMESSAS QUE CHEGARAM AO AR" in corpo)

        codigo, saida = rodar_portao(ilha)
        ok("com a serie gravada o portao APROVA", codigo == 0, ultima(saida))

        # A PROVA DE QUE O TETO E LIDO E NAO REDIGITADO (19/10/2026)
        # ---------------------------------------------------------
        # Esta e a afirmacao que fecha o achado 11, e ela nao olha o codigo do
        # portao: olha o NUMERO que ele relata. O snippet desta ilha de sombra
        # declara 60, a ilha de verdade declara 65, e nenhum dos dois numeros
        # esta escrito no `conferir-titulo-no-ar.py`. Se alguem redigitar o teto
        # ali dentro, o portao da sombra volta a relatar 65 e esta linha fica
        # vermelha no mesmo dia — que e exactamente o aviso que nao existia
        # quando o teto morava a mao em cinco arquivos.
        # O numero e LIDO da linha do relatorio, nunca procurado como substring:
        # a pagina encenada serve "de 10 a 60 lm por litro", entao um `in saida`
        # com "60" poderia ficar verde pelo texto do titulo e nao pelo teto. A
        # primeira versao desta afirmacao tinha esse furo.
        relatado = re.search(r"mais longo \d+ de (\d+)", saida)
        ok("o portao da sombra relata o teto DO SNIPPET DELA, nao um numero escrito nele",
           bool(relatado) and int(relatado.group(1)) == TETO_DA_SOMBRA,
           "relatou %s, esperado %d" % (relatado.group(1) if relatado else "(nada)", TETO_DA_SOMBRA))
        ok("e o teto da sombra nao e o da ilha de verdade — senao a prova acima nao prova nada",
           TETO_DA_SOMBRA != 65, "sombra=%d" % TETO_DA_SOMBRA)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # E A OUTRA DIRECAO: TETO FORA DA BANDA CRIVEL NAO PASSA PELO PORTAO.
    # Ilha de sombra com teto de 5 — numero que o PHP aceita e que a regua
    # recusa, porque reprovaria TODO titulo e uma bancada inteira vermelha por
    # numero fora de faixa e indistinguivel de ilha quebrada.
    ilha = ilha_de_sombra(mundo_bom(), teto=5)
    try:
        codigo, saida = rodar_portao(ilha, "--gravar")
        ok("teto fora da banda crivel REPROVA o portao em vez de medir contra ele",
           codigo != 0 and "banda crivel" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # A troca de titulos entre duas paginas, com os totais intactos.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")
        mundo = mundo_bom()
        base = "https://aquametria.com.br"
        a, b = base + "/calculadora-de-litragem/", base + "/"
        mundo["paginas"][a], mundo["paginas"][b] = mundo["paginas"][b], mundo["paginas"][a]
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo, f, ensure_ascii=False)
        codigo, saida = rodar_portao(ilha)
        ok("titulo TROCADO entre duas paginas reprova, com os totais intactos",
           codigo == 1 and "pagina por pagina" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # A promessa que nao desembarcou: o titulo volta a nome + marca.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")
        mundo = mundo_bom()
        mundo["paginas"]["https://aquametria.com.br/calculadora-de-iluminacao/"] = \
            pagina(titulo="Quanta luz? &#8211; Aquametria")
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo, f, ensure_ascii=False)
        codigo, saida = rodar_portao(ilha)
        ok("PROMESSA QUE NAO DESEMBARCOU reprova, e nomeia a promessa",
           codigo == 1 and "serve a promessa" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # O controle que ganhou promessa.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")
        mundo = mundo_bom()
        mundo["paginas"]["https://aquametria.com.br/calculadora-de-litragem/"] = \
            pagina(titulo="Quantos litros tem? &#8211; de 1 a 1.000 litros")
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo, f, ensure_ascii=False)
        codigo, saida = rodar_portao(ilha)
        ok("CONTROLE QUE GANHOU PROMESSA reprova, e nomeia o controle",
           codigo == 1 and "continua sem promessa no ar" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # Pagina nova no ar sem declaracao.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")
        mundo = mundo_bom()
        mundo["paginas"]["https://aquametria.com.br/peixes/novos/"] = pagina(titulo="Nova")
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo, f, ensure_ascii=False)
        codigo, saida = rodar_portao(ilha)
        ok("PAGINA NOVA no ar sem declaracao reprova", codigo == 1, ultima(saida))
        codigo, saida = rodar_portao(ilha, "--gravar")
        ok("e --gravar fecha a serie em verde de novo", codigo == 0, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # Declaracao cujo total nao fecha com as proprias paginas.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")
        serie = os.path.join(ilha, "dados", "titulos-no-ar.md")
        corpo = io.open(serie, encoding="utf-8").read()
        corpo = corpo.replace('"paginas": 3', '"paginas": 9', 1)
        with io.open(serie, "w", encoding="utf-8") as f:
            f.write(corpo)
        codigo, saida = rodar_portao(ilha)
        ok("declaracao cujo total nao fecha com as paginas dela reprova",
           codigo == 1 and "saem das paginas declaradas" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # A SERIE CRESCE POR CIMA, e o portao le a secao DO TOPO. Sem este caso a
    # serie de sombra tem uma secao so, o primeiro bloco json e tambem o
    # ultimo, e uma leitura que pegasse o ULTIMO ficaria verde — foi assim que
    # a mutacao 19 sobreviveu na primeira bateria.
    ilha = ilha_de_sombra(mundo_bom())
    try:
        rodar_portao(ilha, "--gravar")           # secao 1: o mundo bom
        mundo = mundo_bom()
        base = "https://aquametria.com.br"
        mundo["paginas"][base + "/"] = pagina(titulo="Outro titulo da home")
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo, f, ensure_ascii=False)
        rodar_portao(ilha, "--gravar")           # secao 2, no TOPO: o mundo novo
        corpo = io.open(os.path.join(ilha, "dados", "titulos-no-ar.md"), encoding="utf-8").read()
        ok("a serie tem DUAS secoes, a nova por cima da antiga",
           corpo.count("```json") == 2 and
           corpo.index("Outro titulo da home") < corpo.rindex("As contas do seu"),
           "%d secao(oes)" % corpo.count("```json"))
        codigo, saida = rodar_portao(ilha)
        ok("com duas secoes o portao APROVA contra a do TOPO", codigo == 0, ultima(saida))

        # E agora o mundo volta a ser o da secao ANTIGA: quem le o topo reprova,
        # quem le o ultimo bloco fica verde sobre uma declaracao vencida.
        with io.open(os.path.join(ilha, "mundo-encenado.json"), "w", encoding="utf-8") as f:
            json.dump(mundo_bom(), f, ensure_ascii=False)
        codigo, saida = rodar_portao(ilha)
        ok("e voltar ao mundo da secao ANTIGA REPROVA: a declaracao que manda e a do topo",
           codigo == 1 and "pagina por pagina" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # O mapa de promessas que NAO responde: sem ele a afirmacao da promessa
    # simplesmente nao existe, e portao que perde afirmacao em silencio e verde
    # vazio com outro nome. Foi assim que a mutacao 21 sobreviveu.
    mundo = mundo_bom()
    mundo["promessas_falham"] = True
    ilha = ilha_de_sombra(mundo)
    try:
        codigo, saida = rodar_portao(ilha, "--gravar")
        ok("listar-promessas.php que NAO responde REPROVA, mesmo no --gravar",
           codigo == 1 and "FALHA o listar-promessas.php respondeu" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # O verde vazio no portao inteiro: sitemap sem URL nenhuma.
    ilha = ilha_de_sombra({"revisao": 1, "mapa": {}, "paginas": {}})
    try:
        codigo, saida = rodar_portao(ilha)
        # A frase procurada tem de ser a da FALHA e nao a da afirmacao: o
        # rotulo "verde vazio nao passa por aprovado" aparece tambem na linha
        # `ok`, e foi assim que a mutacao 14 sobreviveu na primeira bateria.
        ok("sitemap sem URL nenhuma REPROVA em vez de aprovar vazio",
           codigo == 1 and "FALHA o sitemap trouxe URL" in saida, ultima(saida))
    finally:
        shutil.rmtree(ilha, ignore_errors=True)
    print("")


def main():
    print("TITULO SERVIDO NO AR — bancada sem rede, HTML encenado\n")
    metade_a()
    metade_b()
    metade_c()
    metade_d()
    metade_e()
    metade_f()
    print("%d afirmacao(oes), %d falha(s)" % (contadas[0], len(falhas)))
    if falhas:
        for f in falhas:
            print("  - %s" % f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

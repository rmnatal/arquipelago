#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-teto-do-titulo.py` contra respostas
ENCENADAS e contra ilhas de sombra com o `define()` trocado.

    python3 ferramentas/teste-teto-do-titulo.py

POR QUE ESTE PORTAO EXISTE, e a data e 19/10/2026
-------------------------------------------------
O achado 11 do fecho das 13h27Z desta ilha: *"o teto de 65 esta digitado A MAO
em QUATRO arquivos desta pasta (...) No dia em que o Google mudar o corte, tres
arquivos vao continuar dizendo 65 e ninguem vai ser avisado. Quem consertar LE o
teto do snippet, nao o redigita."*

O conserto trocou cinco numeros digitados por uma pergunta — e um conserto desse
tipo tem um modo de falhar que e pior que o defeito: a regua que PARECE
perguntar e na verdade devolve um padrao quando a pergunta falha. Um `except`
com `return 65` dentro dela deixaria toda a bancada desta ilha verde para
sempre, agora com a aparencia de estar lendo a fonte. E por isso que a metade
(A) deste arquivo e quase toda sobre respostas RUINS: o que se mede aqui nao e
se a regua le o mundo bom, e se ela se RECUSA a inventar um numero no mundo
ruim.

AS DUAS LEITURAS DO MESMO NUMERO, na metade (C)
-----------------------------------------------
O teto e lido de duas formas que nao se cruzam: pelo PHP, que RESOLVE a
constante como o site a resolve, e pela expressao regular sobre o TEXTO do
`define()`. As duas tem de dar no mesmo numero. Se divergirem, alguem definiu a
constante em outro lugar antes do snippet — que e justamente o caso em que ler o
texto do arquivo mentiria, e o motivo escrito no `listar-teto-do-titulo.php`
para a pergunta ir ao PHP e nao a um `grep`.

A METADE (D) E A QUE FECHA O ACHADO: ilha de sombra com o `define()` em outro
numero. Se a regua devolver aquele numero, ele viajou; se devolver 65, ela o tem
escrito dentro de si e o conserto e cenario.
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
SNIPPET = os.path.join(RAIZ, "snippets", "aquametria-seo-tecnico.php")

contadas = [0]
falhas = []


def ok(rotulo, condicao, detalhe=""):
    contadas[0] += 1
    if condicao:
        print("  ok    %s%s" % (rotulo, (" — %s" % detalhe) if detalhe else ""))
    else:
        falhas.append(rotulo)
        print("  FALHA %s%s" % (rotulo, (" — %s" % detalhe) if detalhe else ""))


def carregar_regua(caminho=None):
    caminho = caminho or os.path.join(FERRAMENTAS, "regua-teto-do-titulo.py")
    spec = importlib.util.spec_from_file_location("regua_teto_do_titulo_t", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()


def resposta(teto=65, separador=" – ", marca="Aquametria", **extra):
    """Resposta crivel, para as metades mordidas mudarem UM campo cada."""
    d = {"teto": teto, "separador": separador, "marca": marca}
    d.update(extra)
    return json.dumps(d, ensure_ascii=False)


def recusa(rotulo, texto, pedaco=None):
    """A regua tem de LEVANTAR, e a mensagem tem de dizer o que estava errado.

    Mensagem generica e meio defeito: quem a ler vai procurar no lugar errado,
    que e a licao de 15/10 desta pasta — reprovar nao e a mesma coisa que
    reprovar PELO MOTIVO CERTO.
    """
    try:
        regua.ler_resposta(texto)
    except regua.RespostaInvalida as e:
        if pedaco is None:
            ok(rotulo, True, str(e)[:80])
        else:
            ok(rotulo, pedaco in str(e), str(e)[:90])
        return
    except Exception as e:  # noqa: BLE001 — qualquer outra e defeito de desenho
        ok(rotulo, False, "levantou %s e nao RespostaInvalida: %s" % (type(e).__name__, e))
        return
    ok(rotulo, False, "NAO levantou nada — devolveu um numero para uma resposta ruim")


# ------------------------------------------------- (A) a resposta, como DADO
def metade_a():
    print("(A) A RESPOSTA E LIDA COMO DADO, E RESPOSTA RUIM NAO VIRA PADRAO\n")

    c = regua.ler_resposta(resposta())
    ok("a resposta boa devolve os tres campos", sorted(c) == ["marca", "separador", "teto"])
    ok("o teto volta como inteiro", c["teto"] == 65 and isinstance(c["teto"], int))
    ok("o separador volta com os espacos dos dois lados", c["separador"] == " – ")
    ok("a marca volta inteira", c["marca"] == "Aquametria")

    recusa("resposta vazia e recusada", "", "nao devolveu nada")
    recusa("resposta so com espaco e recusada", "   \n  ", "nao devolveu nada")
    recusa("resposta que nao e JSON e recusada", "teto=65", "nao e JSON")
    recusa("JSON truncado e recusado", '{"teto": 65, "separa', "nao e JSON")
    recusa("JSON que e lista e recusado", "[65]", "nao e um objeto")
    recusa("JSON que e so um numero e recusado", "65", "nao e um objeto")

    for campo in ("teto", "separador", "marca"):
        d = json.loads(resposta())
        del d[campo]
        recusa("resposta sem o campo %s e recusada" % campo,
               json.dumps(d), "sem o campo %s" % campo)

    recusa("teto em texto e recusado", resposta(teto="65"), "nao e inteiro")
    recusa("teto fracionario e recusado", resposta(teto=65.0), "nao e inteiro")
    recusa("teto booleano e recusado — True nao e 1 aqui", resposta(teto=True), "nao e inteiro")
    recusa("teto nulo e recusado", resposta(teto=None), "nao e inteiro")

    # O ZERO E O NEGATIVO SAO O CASO QUE PARECE INOFENSIVO E NAO E: eles nao
    # afrouxam o portao, eles o fecham. Toda afirmacao de teto da ilha ficaria
    # vermelha de uma vez, e bancada inteira vermelha por um numero fora de
    # faixa e indistinguivel de ilha quebrada.
    recusa("teto zero e recusado", resposta(teto=0), "banda crivel")
    recusa("teto negativo e recusado", resposta(teto=-65), "banda crivel")
    recusa("teto abaixo da banda e recusado", resposta(teto=regua.TETO_MINIMO_CRIVEL - 1),
           "banda crivel")
    recusa("teto acima da banda e recusado — e esta e a direcao que ALARGA o portao",
           resposta(teto=regua.TETO_MAXIMO_CRIVEL + 1), "banda crivel")
    ok("a borda de baixo da banda PASSA",
       regua.ler_resposta(resposta(teto=regua.TETO_MINIMO_CRIVEL))["teto"]
       == regua.TETO_MINIMO_CRIVEL)
    ok("a borda de cima da banda PASSA",
       regua.ler_resposta(resposta(teto=regua.TETO_MAXIMO_CRIVEL))["teto"]
       == regua.TETO_MAXIMO_CRIVEL)

    recusa("separador vazio e recusado", resposta(separador=""), "separador")
    recusa("separador so com espaco e recusado", resposta(separador="   "), "separador")
    recusa("separador que nao e texto e recusado", resposta(separador=1), "separador")
    recusa("marca vazia e recusada", resposta(marca=""), "marca")
    recusa("marca que nao e texto e recusada", resposta(marca=[]), "marca")

    # Campo a mais nao e defeito: o perguntador pode crescer sem derrubar quem o le.
    ok("campo a mais na resposta nao reprova",
       regua.ler_resposta(resposta(versao="2"))["teto"] == 65)


# --------------------------------------------- (B) a cauda e DERIVADA
def metade_b():
    print("\n(B) A CAUDA E DERIVADA DAS DUAS CONSTANTES, NUNCA DIGITADA\n")

    c = regua.ler_resposta(resposta())
    ok("a cauda e separador + marca", regua.cauda(c) == " – Aquametria", repr(regua.cauda(c)))
    ok("trocar o separador muda a cauda",
       regua.cauda(regua.ler_resposta(resposta(separador=" | "))) == " | Aquametria")
    ok("trocar a marca muda a cauda",
       regua.cauda(regua.ler_resposta(resposta(marca="Outra"))) == " – Outra")
    # Se a cauda fosse digitada, as duas linhas acima ficariam verdes com a
    # cauda antiga — e era exatamente o estado do `CAUDA = " – Aquametria"` do
    # teste-titulos-das-duas-fontes.py antes desta passada.


# ------------------------- (C) o mundo de verdade, lido de duas formas
def metade_c():
    print("\n(C) A ILHA DE VERDADE, LIDA PELAS DUAS FORMAS QUE NAO SE CRUZAM\n")

    c = regua.perguntar(RAIZ)
    ok("o PHP responde e a resposta presta", isinstance(c["teto"], int), "teto=%d" % c["teto"])

    texto = io.open(SNIPPET, encoding="utf-8").read()
    m = re.search(r"define\(\s*'AQUAMETRIA_TITULO_TETO'\s*,\s*(\d+)\s*\)", texto)
    ok("o snippet tem o define do teto", bool(m))
    ok("o teto RESOLVIDO pelo PHP e o mesmo do texto do define",
       bool(m) and int(m.group(1)) == c["teto"],
       "php=%s texto=%s" % (c["teto"], m.group(1) if m else "(nada)"))

    ms = re.search(r"define\(\s*'AQUAMETRIA_TITULO_SEPARADOR'\s*,\s*'([^']*)'\s*\)", texto)
    ok("o separador resolvido e o mesmo do texto do define",
       bool(ms) and ms.group(1) == c["separador"],
       "php=%r texto=%r" % (c["separador"], ms.group(1) if ms else None))
    mm = re.search(r"define\(\s*'AQUAMETRIA_TITULO_MARCA'\s*,\s*'([^']*)'\s*\)", texto)
    ok("a marca resolvida e a mesma do texto do define",
       bool(mm) and mm.group(1) == c["marca"],
       "php=%r texto=%r" % (c["marca"], mm.group(1) if mm else None))

    # Perguntador ausente e ausencia de resposta, nao um padrao.
    vazio = tempfile.mkdtemp(prefix="aqm-teto-vazio-")
    try:
        os.makedirs(os.path.join(vazio, "ferramentas"))
        try:
            regua.perguntar(vazio)
            ok("ilha sem o perguntador e recusada", False, "NAO levantou")
        except regua.RespostaInvalida as e:
            ok("ilha sem o perguntador e recusada", "perguntador ausente" in str(e), str(e)[:70])
    finally:
        shutil.rmtree(vazio, ignore_errors=True)


# ------------------- (D) a prova do achado: o define trocado viaja
SOMBRA = """/* so as tres constantes do titulo — sem `<?php`, porque o
   render-para-teste.php carrega os snippets com eval(). */
if ( ! defined( 'AQUAMETRIA_TITULO_TETO' ) ) {
\tdefine( 'AQUAMETRIA_TITULO_TETO', %s );
}
if ( ! defined( 'AQUAMETRIA_TITULO_SEPARADOR' ) ) {
\tdefine( 'AQUAMETRIA_TITULO_SEPARADOR', '%s' );
}
if ( ! defined( 'AQUAMETRIA_TITULO_MARCA' ) ) {
\tdefine( 'AQUAMETRIA_TITULO_MARCA', '%s' );
}
"""


def ilha_de_sombra(teto, separador=" – ", marca="Aquametria"):
    tmp = tempfile.mkdtemp(prefix="aqm-teto-sombra-")
    os.makedirs(os.path.join(tmp, "ferramentas"))
    os.makedirs(os.path.join(tmp, "snippets"))
    for nome in ("regua-teto-do-titulo.py", "listar-teto-do-titulo.php",
                 "render-para-teste.php"):
        shutil.copy(os.path.join(FERRAMENTAS, nome), os.path.join(tmp, "ferramentas", nome))
    with io.open(os.path.join(tmp, "snippets", "aquametria-teto.php"), "w", encoding="utf-8") as f:
        f.write(SOMBRA % (teto, separador, marca))
    return tmp


def metade_d():
    print("\n(D) O DEFINE TROCADO VIAJA — E ESTA E A METADE QUE FECHA O ACHADO 11\n")

    # Tres numeros, nenhum deles 65: um numero so poderia coincidir com um
    # padrao escondido, e tres seguidos nao coincidem com padrao nenhum.
    for n in (41, 58, 119):
        ilha = ilha_de_sombra(n)
        try:
            c = regua.perguntar(ilha)
            ok("define com %d devolve %d, e nao 65" % (n, n), c["teto"] == n, "devolveu %s" % c["teto"])
        finally:
            shutil.rmtree(ilha, ignore_errors=True)

    ilha = ilha_de_sombra(50, separador=" :: ", marca="Sombrametria")
    try:
        c = regua.perguntar(ilha)
        ok("separador trocado no define tambem viaja", c["separador"] == " :: ", repr(c["separador"]))
        ok("marca trocada no define tambem viaja", c["marca"] == "Sombrametria", repr(c["marca"]))
        ok("e a cauda da sombra se deriva das duas", regua.cauda(c) == " :: Sombrametria")
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # Teto fora da banda no PROPRIO define: o PHP aceita e a regua recusa. E o
    # unico caminho pelo qual o snippet poderia alargar os portoes em silencio.
    ilha = ilha_de_sombra(400)
    try:
        try:
            regua.perguntar(ilha)
            ok("define fora da banda e recusado, nao obedecido", False, "NAO levantou")
        except regua.RespostaInvalida as e:
            ok("define fora da banda e recusado, nao obedecido", "banda crivel" in str(e), str(e)[:85])
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # PHP QUE IMPRIME JSON BOM E SAI 1 — o furo que as mutacoes acharam em mim.
    # Nenhuma afirmacao cobrava o CODIGO DE SAIDA: com a resposta vazia, a regua
    # recusava pela leitura e a mutacao que apagava a checagem sobrevivia. Aqui a
    # saida e impecavel e o codigo e 1, entao so o codigo pode reprovar. Um php
    # que falha no meio e imprime o que ja tinha montado e exatamente este caso.
    ilha = tempfile.mkdtemp(prefix="aqm-teto-sai1-")
    try:
        os.makedirs(os.path.join(ilha, "ferramentas"))
        shutil.copy(os.path.join(FERRAMENTAS, "regua-teto-do-titulo.py"),
                    os.path.join(ilha, "ferramentas", "regua-teto-do-titulo.py"))
        with io.open(os.path.join(ilha, "ferramentas", "listar-teto-do-titulo.php"),
                     "w", encoding="utf-8") as f:
            f.write("<?php\n"
                    "fwrite( STDERR, \"morri no meio\\n\" );\n"
                    "echo json_encode( array( 'teto' => 65, 'separador' => ' - ',"
                    " 'marca' => 'Aquametria' ) ), \"\\n\";\n"
                    "exit( 1 );\n")
        try:
            regua.perguntar(ilha)
            ok("php que sai 1 e recusado mesmo imprimindo JSON perfeito", False, "NAO levantou")
        except regua.RespostaInvalida as e:
            ok("php que sai 1 e recusado mesmo imprimindo JSON perfeito",
               "devolveu 1" in str(e), str(e)[:85])
            ok("e a recusa carrega o que o php escreveu no stderr",
               "morri no meio" in str(e), str(e)[:85])
    finally:
        shutil.rmtree(ilha, ignore_errors=True)

    # Snippet SEM o define: o perguntador tem de sair 1 e dizer qual constante
    # falta — e nao imprimir um JSON com um valor de consolo.
    ilha = tempfile.mkdtemp(prefix="aqm-teto-sem-")
    try:
        os.makedirs(os.path.join(ilha, "ferramentas"))
        os.makedirs(os.path.join(ilha, "snippets"))
        for nome in ("regua-teto-do-titulo.py", "listar-teto-do-titulo.php",
                     "render-para-teste.php"):
            shutil.copy(os.path.join(FERRAMENTAS, nome), os.path.join(ilha, "ferramentas", nome))
        with io.open(os.path.join(ilha, "snippets", "vazio.php"), "w", encoding="utf-8") as f:
            f.write("/* snippet sem constante nenhuma */\n")
        p = subprocess.run(["php", os.path.join(ilha, "ferramentas", "listar-teto-do-titulo.php"), ilha],
                           capture_output=True, text=True)
        ok("perguntador sem o define sai diferente de zero", p.returncode != 0, "saida=%d" % p.returncode)
        ok("e nomeia a constante que falta",
           "AQUAMETRIA_TITULO_TETO" in (p.stderr or ""), (p.stderr or "").strip()[:80])
        ok("e nao imprime JSON nenhum no lugar", "teto" not in (p.stdout or ""), (p.stdout or "")[:60])
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


# --------------------------------- (E) a varredura de quem redigitou
def metade_e():
    print("\n(E) A VARREDURA — QUEM REDIGITOU, E A PROSA QUE NAO E DIVIDA\n")

    teto = regua.perguntar(RAIZ)["teto"]

    denuncias, avisos = regua.redigitados(regua.ler_pasta(), teto)
    ok("HOJE a pasta ferramentas/ nao tem NENHUMA denuncia",
       denuncias == [], "; ".join("%s:%d" % (d[0], d[1]) for d in denuncias[:4]))
    print("        (%d aviso(s) de prosa, que nao reprovam: %s)"
          % (len(avisos), ", ".join("%s:%d" % (a[0], a[1]) for a in avisos[:4])))

    def varrer(texto, nome="portao-de-mentira.py"):
        return regua.redigitados({nome: texto}, teto)

    # O QUE TEM DE SER DENUNCIADO
    d, a = varrer("TETO = 65\n")
    ok("`TETO` atribuido a numero e denunciado", len(d) == 1 and d[0][3] == "teto digitado a mao")
    d, a = varrer("TETO=65\n")
    ok("sem espaco em volta do igual tambem e denunciado", len(d) == 1)
    d, a = varrer("    self.TETO  =  65\n")
    ok("indentado e com espaco a mais tambem e denunciado", len(d) == 1)
    d, a = varrer("const TITULO_MAXIMO = 65;\n")
    ok("`TITULO_MAXIMO` do .mjs e denunciado", len(d) == 1)
    d, a = varrer("SEPARADOR = ' - '\n")
    ok("`SEPARADOR` em texto e denunciado", len(d) == 1
       and d[0][3] == "separador ou marca digitados a mao")
    d, a = varrer('MARCA = "Aquametria"\n')
    ok("`MARCA` em texto e denunciada", len(d) == 1)
    d, a = varrer('CAUDA = " - Aquametria"\n')
    ok("`CAUDA` em texto e denunciada", len(d) == 1)
    # OS MUNDOS ENCENADOS DE COMPARACAO SE MONTAM COM O TETO LIDO, NAO COM 65.
    # As mutacoes acharam este furo em mim: com `65` digitado aqui, trocar o
    # define do snippet para 58 fazia a bancada REPROVAR O MUNDO BOM — porque a
    # afirmacao media a comparacao contra um numero que a ilha ja nao usava. Era
    # o defeito do achado 11 dentro do portao que existe para fecha-lo.
    d, a = varrer("  ok('<title> cabe', aba.length <= %d);\n" % teto)
    ok("comparacao contra o teto literal, em linha que fala de titulo, e denunciada",
       len(d) == 1 and d[0][3] == "comparacao contra o teto literal")
    d, a = varrer("    if len(titulo) > %d:\n" % teto)
    ok("a comparacao e pega nos dois sentidos", len(d) == 1)

    # O QUE NAO PODE SER DENUNCIADO, e cada linha e um falso positivo possivel
    d, a = varrer("TPA_TETO = 50\n")
    ok("`TPA_TETO` do snippet da midia NAO e denunciado: outro teto, outra regra",
       d == [] and a == [])
    d, a = varrer("TETO_ENCENADO = 65\n")
    ok("`TETO_ENCENADO` NAO e denunciado: encenacao declarada nao e divida",
       d == [] and a == [])
    d, a = varrer("TETO = outra_coisa\n")
    ok("`TETO` lido de outro lugar NAO e denunciado — e exatamente o conserto",
       d == [] and a == [])
    d, a = varrer('TETO = carregar()["teto"]\n')
    ok("`TETO` vindo da regua NAO e denunciado", d == [] and a == [])
    d, a = varrer("    if len(litros) > %d:\n" % teto)
    ok("comparacao com o teto em linha que NAO fala de titulo nao e denunciada",
       d == [] and a == [], "%s" % (d[:1],))
    d, a = varrer("  ok('<title> cabe', aba.length <= %d);\n" % (teto - 1))
    ok("comparacao com numero que NAO e o teto nao e denunciada", d == [] and a == [])

    # A PROSA: aviso, nunca denuncia
    d, a = varrer("# o teto era `TETO = 65` escrito a mao\n")
    ok("comentario que cita o numero e AVISO, nao denuncia", d == [] and len(a) == 1)
    d, a = varrer("   * antes isto era CAUDA = \" - Aquametria\"\n")
    ok("linha de comentario de bloco tambem e aviso", d == [] and len(a) == 1)
    d, a = varrer("codigo_de_verdade(); # e antes era `TETO = 65`\n")
    ok("o numero entre acentos graves e aviso mesmo com codigo na linha",
       d == [] and len(a) == 1, "%s" % (d[:1],))
    d, a = varrer("sobre o teto de 65 caracteres\n")
    ok("prosa sem atribuicao e sem comparacao nao produz nada", d == [] and a == [])

    # OS DOIS ARQUIVOS DE FORA, e eles sao de fora por motivos diferentes
    for nome in regua.FORA_DA_VARREDURA:
        d, a = varrer("TETO = 65\n", nome=nome)
        ok("%s fica fora da varredura" % nome, d == [] and a == [])

    # A CORRENTE EXISTE: quem afirma sobre o teto tem de CHAMAR a regua. Se
    # alguem tirar a chamada e voltar a digitar, a varredura acima pega; se
    # tirar a chamada e nao medir mais nada, so esta afirmacao pega.
    # A PERGUNTA TEM DE SER UMA CHAMADA, E AS MUTACOES ACHARAM ESTE FURO EM MIM
    # TRES VEZES, cada uma mais estreita que a anterior:
    #   1. "o nome aparece no arquivo" — satisfeito pelo comentario que explica a
    #      chamada;
    #   2. "o nome aparece em linha que nao comeca por marcador de comentario" —
    #      satisfeito pelas linhas de CONTINUACAO do comentario de BLOCO do
    #      teste-voz.mjs, que nao comecam por marcador nenhum;
    #   3. "o nome aparece entre aspas" — satisfeito pela MENSAGEM DE ERRO do
    #      proprio teste-voz.mjs, que cita o nome da regua numa frase.
    # A diferenca que sobrevive as tres: numa chamada a string E o caminho; numa
    # mensagem ela e uma frase que CONTEM o nome. Entao a afirmacao compara a
    # string inteira, e nao procura o nome dentro dela.
    def chama(texto, alvo):
        achadas = []
        for linha in texto.split("\n"):
            nua = linha.strip()
            if nua.startswith(regua.MARCADORES_DE_PROSA):
                continue
            for aspa in regua.ASPAS:
                for pedaco in nua.split(aspa)[1::2]:
                    if pedaco == alvo or pedaco.endswith("/" + alvo):
                        achadas.append(nua)
        return achadas

    for nome in ("teste-promessa-do-titulo.py", "teste-titulos-das-duas-fontes.py",
                 "conferir-titulo-no-ar.py", "teste-voz.mjs"):
        texto = io.open(os.path.join(FERRAMENTAS, nome), encoding="utf-8").read()
        achadas = chama(texto, "regua-teto-do-titulo.py")
        ok("%s tem uma string que E o caminho da regua, ou seja CHAMA" % nome,
           len(achadas) >= 1, (achadas[0][:80] if achadas else "so prosa e mensagem"))


def main():
    print("PORTAO DO TETO DO TITULO — a constante e lida, nao digitada\n")
    metade_a()
    metade_b()
    metade_c()
    metade_d()
    metade_e()
    print("\n%d afirmacao(oes), %d falha(s)" % (contadas[0], len(falhas)))
    for f in falhas:
        print("  - %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

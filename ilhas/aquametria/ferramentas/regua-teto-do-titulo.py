#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: devolve as TRES CONSTANTES que montam o `<title>` desta
ilha — teto, separador e marca — PERGUNTANDO ao snippet que as define, e varre a
pasta `ferramentas/` procurando quem as redigitou.

Nao afirma nada sozinha e nao abre rede. Quem afirma sobre o repositorio sao o
`teste-promessa-do-titulo.py` e o `teste-titulos-das-duas-fontes.py`; quem
afirma sobre o ar e o `conferir-titulo-no-ar.py`; quem exercita esta regua
contra respostas ENCENADAS e o `teste-teto-do-titulo.py`; e quem a mutila e o
`mutacoes-teto-do-titulo.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 19/10/2026
--------------------------------------------------
O achado 11 do fecho das 13h27Z desta ilha, deixado sem conserto de proposito
pela 19.2: *"o teto de 65 esta digitado A MAO em QUATRO arquivos desta pasta
(...) o teto e definido num lugar so, o AQUAMETRIA_TITULO_TETO do snippet. No
dia em que o Google mudar o corte, tres arquivos vao continuar dizendo 65 e
ninguem vai ser avisado. Quem consertar LE o teto do snippet, nao o redigita."*

O DEFEITO NAO E O NUMERO REPETIDO: E A DIRECAO EM QUE ELE FALHA
---------------------------------------------------------------
Teto redigitado nao faz portao nenhum ficar vermelho. Ele faz o contrario, que
e pior: no dia em que o snippet baixar o teto para 60, o site passa a devolver
nome + marca nos titulos que nao couberem mais — porque as tres travas da
promessa sao SILENCIOSAS por desenho, e nome + marca e SEMPRE valido — e os
portoes continuam medindo contra 65, continuam verdes, e a promessa desaparece
do ar com a bancada APROVADO. E a mesma familia da cicatriz de 11/09/2026 desta
pasta (293 afirmacoes verdes e os nove titulos do ar sendo os de antes): o
numero que a medicao usa tem de vir de onde o site o usa.

O QUE ELA LE, e cada campo existe por um defeito possivel
---------------------------------------------------------
  * `teto` — `AQUAMETRIA_TITULO_TETO`, o corte que o Google mostra. Inteiro
    positivo; qualquer outra coisa e resposta invalida e nao um valor baixo.
  * `separador` — `AQUAMETRIA_TITULO_SEPARADOR`, o travessao com espaco dos dois
    lados. Ele ENTRA na conta do teto, entao digita-lo errado por um espaco
    muda o numero de caracteres que a ilha acha que cabe.
  * `marca` — `AQUAMETRIA_TITULO_MARCA`. O titulo de volta e nome + separador +
    marca, e e ele que tem de caber no teto quando a promessa nao couber.

A RESPOSTA VIAJA COMO TEXTO, e isto e o ponto
---------------------------------------------
`perguntar()` abre um processo e devolve dado; `ler_resposta()` recebe o TEXTO
da resposta e e quem decide se ela presta. Separados, a bancada encena resposta
vazia, resposta truncada, teto zero, teto negativo e teto que nao e numero sem
precisar de um snippet quebrado no disco — e o desenho e o mesmo da
`regua-titulo-no-ar.py`, que recebe HTML como texto e o mapa de promessas como
dado. Regua que so sabe medir o mundo bom nao prova que morde.

NENHUM CAMINHO DEVOLVE UM PADRAO, E E A REGRA CENTRAL DESTE ARQUIVO
-------------------------------------------------------------------
Resposta que falta, resposta ilegivel e teto fora de faixa levantam
`RespostaInvalida`. Um `except` com `return 65` aqui dentro reproduziria
exatamente o defeito que o achado 11 descreve, com a agravante de o esconder
atras de uma regua que parece ser a cura.

ELA NAO REESCREVE A MONTAGEM DO TITULO, DE PROPOSITO
----------------------------------------------------
Quem monta nome + separador + promessa, com as tres travas e o teto, e o
`aquametria_seo_titulo_do_documento()` do snippet. Esta regua entrega as pecas e
a `cauda()`, que e a unica derivacao que ela faz — separador + marca, o que o
WordPress acrescenta — porque esse par estava redigitado como uma terceira
constante (`CAUDA = " – Aquametria"`) e derivar e o contrario de redigitar.
"""

import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERGUNTADOR = "listar-teto-do-titulo.php"

CAMPOS = ("teto", "separador", "marca")

# A BANDA E A REGUA QUE ESTE ARQUIVO ESCREVE PARA SI, E ELA EXISTE POR CAUSA DE
# UMA OBJECAO ESCRITA NESTA PASTA (19/10/2026)
# ---------------------------------------------------------------------------
# O cabecalho do `teste-voz.mjs` declara o principio contrario a este arquivo,
# com todas as letras: *"QUEM CONFERE ESCREVE A PROPRIA REGUA. A lista de termos
# esta AQUI (...) Ela nao e importada do snippet (...) se as duas metades lessem
# a mesma lista, apagar um termo dela faria as duas errarem juntas e o teste
# continuaria verde."* Ele esta certo, e o achado 11 tambem — eles falam de duas
# coisas diferentes, e a diferenca decide o desenho:
#
#   * A lista de termos proibidos e o que o portao EXISTE PARA POLICIAR, e a
#     autoridade dela e o `VOZ.md`, que e documento e nao codigo. Le-la do
#     snippet deixaria o policiado escolher a lei.
#   * O teto nao e o policiado: e a DECISAO, tomada num lugar so. Portao que
#     mede contra um teto redigitado mede contra uma decisao que ninguem mais
#     sustenta, e e isso que o achado 11 nomeia.
#
# MAS A OBJECAO VALE NUMA DIRECAO, E ELA FICA COBERTA AQUI: perguntar sozinho
# deixaria o snippet ALARGAR o portao em silencio — subir o teto para 200 faria
# todas as afirmacoes de teto desta ilha passarem a aceitar titulo de 200
# caracteres, sem ninguem ser avisado, que e exatamente o "errar juntas" do
# `teste-voz.mjs`. Entao o numero e LIDO e a FAIXA e DECLARADA aqui.
#
# OS DOIS NUMEROS DA BANDA NAO SAO MEDICAO DO GOOGLE, e dizer o que eles sao
# importa mais que o valor deles: sao o limite fora do qual um teto de `<title>`
# deixa de ser credivel e passa a ser erro de digitacao ou alargamento de
# portao. Quem precisar de um teto fora da banda muda ESTA linha, no claro, em
# vez de muda-lo de lado no snippet e colher o portao ja alargado.
TETO_MINIMO_CRIVEL = 40
TETO_MAXIMO_CRIVEL = 120


class RespostaInvalida(Exception):
    """A resposta do snippet nao presta. Levantada em vez de um padrao."""


def ler_resposta(texto):
    """Recebe o TEXTO da resposta e devolve {teto, separador, marca}.

    Levanta `RespostaInvalida` em tudo que nao for uma resposta boa — e o teto
    tem de ser inteiro POSITIVO, porque teto zero ou negativo nao reprova
    titulo nenhum: ele reprova TODOS, e uma bancada inteira vermelha por um
    numero fora de faixa e indistinguivel de uma ilha quebrada.
    """
    cru = (texto or "").strip()
    if not cru:
        raise RespostaInvalida("o perguntador nao devolveu nada")
    try:
        dado = json.loads(cru)
    except ValueError as e:
        raise RespostaInvalida("resposta nao e JSON: %s — %r" % (e, cru[:120]))
    if not isinstance(dado, dict):
        raise RespostaInvalida("resposta nao e um objeto: %r" % (cru[:120],))

    faltando = [c for c in CAMPOS if c not in dado]
    if faltando:
        raise RespostaInvalida("resposta sem o campo %s" % ", ".join(faltando))

    teto = dado["teto"]
    if isinstance(teto, bool) or not isinstance(teto, int):
        raise RespostaInvalida("teto nao e inteiro: %r" % (teto,))
    if not TETO_MINIMO_CRIVEL <= teto <= TETO_MAXIMO_CRIVEL:
        raise RespostaInvalida(
            "teto fora da banda crivel de %d a %d: %r — se a mudanca e de verdade, "
            "mude a banda da regua-teto-do-titulo.py no claro"
            % (TETO_MINIMO_CRIVEL, TETO_MAXIMO_CRIVEL, teto)
        )

    for c in ("separador", "marca"):
        if not isinstance(dado[c], str) or not dado[c].strip():
            raise RespostaInvalida("%s vazio ou nao e texto: %r" % (c, dado[c]))

    return {"teto": teto, "separador": dado["separador"], "marca": dado["marca"]}


def perguntar(raiz=None):
    """Pergunta ao snippet, pelo PHP, e devolve as tres constantes.

    A raiz e argumento para a bancada poder perguntar a uma COPIA da ilha com o
    `define()` trocado — que e a unica forma de provar que o numero e lido e
    nao redigitado.
    """
    raiz = raiz or RAIZ
    script = os.path.join(raiz, "ferramentas", PERGUNTADOR)
    if not os.path.exists(script):
        raise RespostaInvalida("perguntador ausente: %s" % script)
    try:
        saida = subprocess.run(["php", script, raiz], capture_output=True, text=True)
    except OSError as e:
        raise RespostaInvalida("nao deu para rodar o php: %s" % e)
    if saida.returncode != 0:
        raise RespostaInvalida(
            "%s devolveu %d: %s" % (PERGUNTADOR, saida.returncode, (saida.stderr or "").strip()[:200])
        )
    return ler_resposta(saida.stdout)


def cauda(c):
    """O que o WordPress acrescenta ao nome quando a promessa nao cabe: o
    separador e a marca. DERIVADO das duas constantes, nunca digitado."""
    return c["separador"] + c["marca"]


# ---------------------------------------------------------------------------
# A VARREDURA — quem redigitou as constantes
#
# Ela e a metade que impede o conserto de hoje de ser desfeito amanha. Portao
# novo que digite `TETO = 65` nasce denunciado no mesmo dia, pelo mesmo desenho
# da `bancada.py` desta pasta: a pergunta e feita aos ARQUIVOS, nunca a uma
# lista aqui dentro.
#
# O QUE ELA ACUSA E POSICAO DE CODIGO, NUNCA PROSA. O cabecalho de meio portao
# desta pasta explica o teto em portugues ("o teto de 65 e da tela"), e proibir
# a prosa seria apagar a explicacao para salvar o numero. O que ela acusa e o
# numero ENTRANDO NA MEDICAO: atribuicao a um nome de constante do titulo, ou
# comparacao contra um literal numa linha que fala de titulo.
#
# E O NOME `TETO_ENCENADO` ESCAPA POR DESENHO, NAO POR BURACO. O
# `teste-titulo-no-ar.py` passa um teto como ARGUMENTO para a
# `regua-titulo-no-ar.py` e monta titulos de exatamente aquele tamanho para
# medir a borda; ali o numero e dado de teste e nao afirmacao sobre a ilha, e a
# regua que o recebe e parametrizada — nao ha o que ler do snippet. O que estava
# errado era o NOME: `TETO = 65`, igual ao dos tres portoes que afirmam sobre a
# ilha, de forma que nenhum leitor distinguia os dois. Encenacao que se declara
# encenacao nao e divida.
# ---------------------------------------------------------------------------

NOMES_DO_TETO = r"(?:TETO|TITULO_MAXIMO)"
NOMES_DO_TEXTO = r"(?:SEPARADOR|MARCA|CAUDA)"

# O GRUPO 1 E O TRECHO QUE IMPORTA, SEM O CARACTERE DA FRENTE. A primeira
# versao usava o casamento inteiro, que carregava o caractere anterior ao nome —
# uma acento grave, uma aspa — e por isso a classificacao abaixo nunca achava o
# trecho dentro do proprio trecho citado. O portao pegou isto em mim.
RE_TETO_DIGITADO = re.compile(r"(?:^|[^0-9A-Za-z_])(" + NOMES_DO_TETO + r"\s*=\s*[0-9]+)")
RE_TEXTO_DIGITADO = re.compile(r"(?:^|[^0-9A-Za-z_])(" + NOMES_DO_TEXTO + r"\s*=\s*['\"])")
RE_FALA_DE_TITULO = re.compile(r"title|titulo|título|\baba\b", re.I)
RE_COMPARACAO = re.compile(r"(?:<=|>=|<|>)\s*([0-9]+)\b")

# O proprio perguntador e a propria regua estao FORA da varredura, e os dois por
# motivos diferentes: o perguntador e a porta por onde o numero sai do snippet,
# e esta regua e quem faz a pergunta. Nenhum dos dois digita o numero.
FORA_DA_VARREDURA = (PERGUNTADOR, "regua-teto-do-titulo.py")


# PROSA NAO E MEDICAO, E A SEPARACAO NASCEU DE UM ACERTO CONTRA MIM MESMA
# ---------------------------------------------------------------------------
# A primeira versao desta varredura denunciou os COMENTARIOS que esta passada
# escreveu para explicar o conserto — linhas que citam o nome da constante
# entre acentos graves para dizer que ele era o defeito. Elas estavam certas e
# a varredura tambem: ela nao distingue comentario de codigo.
#
# Afrouxar o padrao para ele nao morder mais a prosa seria trocar a regua pelo
# resultado. A separacao certa e outra, e e a pergunta que importa: a linha
# EXECUTA? Comentario nao mede nada, entao numero redigitado nele nao alarga
# portao nenhum — mas envelhece calado e manda o proximo leitor para o numero
# errado, que e metade do defeito do achado 11. Ou seja: nao e erro e nao e
# nada. E AVISO, pelo mesmo desenho do E21 e do E25 do esquema desta ilha — o
# dado esta certo e quem tem de obedecer e outra camada.
#
# O que conta como prosa, e o criterio e deliberadamente ESTREITO: linha que
# comeca por marcador de comentario, ou numero que aparece dentro de acentos
# graves. Qualquer outra posicao continua sendo denuncia, porque o lado seguro
# do erro e denunciar codigo demais e nao prosa de menos.
MARCADORES_DE_PROSA = ("#", "//", "/*", "*", '''"""''', "'''")

ACENTO_GRAVE = ("`",)
ASPAS = ('"', "'")


# DELIMITADOR ESCAPADO NAO ABRE NEM FECHA NADA, e esta linha nasceu de um
# acerto contra este arquivo em 19/10/2026
# ---------------------------------------------------------------------------
# A `regua-constantes-de-snippet.py`, que IMPORTA a `onde()` daqui, foi apontada
# para a propria bancada dela e DENUNCIOU uma linha que era encenacao:
#
#     d, a = varrer("d, saida = varrer(\"NIVEL = 'alta'\\n\")\n")
#
# O `split` por `"` conta os escapados como se abrissem e fechassem, os pares
# saem trocados, e o trecho que esta DENTRO da string cai em indice par — ou
# seja, e lido como codigo. O defeito e desta funcao e nao daquela regua, e e
# da mesma familia do que as duas existem para pegar: a medicao estava certa no
# mundo bom e errada no mundo com uma aspa a mais.
RE_ESCAPADO = re.compile(r"\\.")


def entre(nua, trecho, delimitadores):
    """O trecho esta dentro de um par de algum destes delimitadores?

    Os pedacos de indice IMPAR de um `split` pelo delimitador sao os de dentro.
    E barato, nao e um analisador de sintaxe, e o limite esta escrito na `onde()`.

    O que e ESCAPADO sai da conta antes do `split`, porque `\\"` nao abre nem
    fecha string nenhuma. Sai como dois caracteres neutros e nao como nada, para
    o trecho procurado continuar inteiro no pedaco em que ele estava.
    """
    limpa = RE_ESCAPADO.sub("\x00\x00", nua)
    for d in delimitadores:
        for i, pedaco in enumerate(limpa.split(d)):
            if i % 2 == 0:
                continue
            # O pedaco vem da linha LIMPA; o trecho procurado vem da linha crua,
            # entao a comparacao se faz na mesma moeda.
            if RE_ESCAPADO.sub("\x00\x00", trecho) in pedaco:
                return True
    return False


def onde(linha, trecho):
    """Em que posicao o trecho esta: `codigo`, `prosa` ou `dado`.

    A pergunta que decide e UMA: a linha MEDE alguma coisa ali?

      * `codigo` — mede. E a unica que reprova.
      * `prosa` — comentario, ou nome citado entre ACENTOS GRAVES. Nao mede
        nada, mas envelhece calado e manda o proximo leitor ao numero errado,
        que e metade do defeito do achado 11. Vira AVISO, pelo desenho do E21 e
        do E25 do esquema desta ilha. O acento grave entra aqui porque neste
        repositorio ele e convencao de documentacao — e assim que todo
        cabecalho desta pasta cita um nome de arquivo ou de constante.
      * `dado` — o trecho esta dentro de ASPAS, ou seja e TEXTO que o arquivo
        manipula, nao uma atribuicao. E o caso do `teste-teto-do-titulo.py`, que
        encena mundos redigitados para provar que esta varredura morde: o
        padrao TEM de aparecer no texto dele. Silencioso, porque nao e defeito
        nem informacao para leitor nenhum.

    O LIMITE, escrito em vez de descoberto depois: isto nao e um analisador de
    sintaxe. Uma linha que montasse a medicao dentro de uma string — um `exec`,
    um `eval` — seria lida como `dado` e passaria. Nao e por distracao: e o
    preco de uma regua de uma pagina que roda em .py, .mjs e .php com o mesmo
    criterio, e redigitar o teto dentro de um `exec` nao e o jeito como alguem
    redigita um teto por descuido.
    """
    nua = linha.strip()
    if nua.startswith(MARCADORES_DE_PROSA):
        return "prosa"
    if entre(nua, trecho, ACENTO_GRAVE):
        return "prosa"
    if entre(nua, trecho, ASPAS):
        return "dado"
    return "codigo"


def redigitados(arquivos, teto):
    """Recebe {nome: texto} como DADO e devolve (denuncias, avisos).

    Cada achado e (nome, linha, texto_da_linha, motivo). `denuncias` vazia e o
    unico resultado que o portao aceita; `avisos` ele imprime e nao reprova.
    """
    denuncias = []
    avisos = []
    for nome in sorted(arquivos):
        if nome in FORA_DA_VARREDURA:
            continue
        for n, linha in enumerate((arquivos[nome] or "").split("\n"), 1):
            achado = None
            for regra, motivo in (
                (RE_TETO_DIGITADO, "teto digitado a mao"),
                (RE_TEXTO_DIGITADO, "separador ou marca digitados a mao"),
            ):
                m = regra.search(linha)
                if m:
                    achado = (m.group(1).strip(), motivo)
                    break
            if achado is None and RE_FALA_DE_TITULO.search(linha):
                for m in RE_COMPARACAO.finditer(linha):
                    if int(m.group(1)) == teto:
                        achado = (m.group(0).strip(), "comparacao contra o teto literal")
                        break
            if achado is None:
                continue
            trecho, motivo = achado
            posicao = onde(linha, trecho)
            if posicao == "dado":
                continue
            alvo = avisos if posicao == "prosa" else denuncias
            alvo.append((nome, n, linha.strip()[:110], motivo))
    return denuncias, avisos


def ler_pasta(pasta=None):
    """{nome: texto} de todo .py, .mjs e .php de `ferramentas/`. Le o disco; a
    decisao e da `redigitados()`, que recebe dado."""
    pasta = pasta or os.path.join(RAIZ, "ferramentas")
    saida = {}
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith((".py", ".mjs", ".php")):
            continue
        # `errors="replace"` ACRESCENTADO EM 20/10/2026 as 19h4xZ, e nao e enfeite:
        # sem ele um unico byte que nao e UTF-8 em QUALQUER arquivo desta pasta
        # mata esta regua de `UnicodeDecodeError` — que e `ValueError` e NAO
        # `OSError`, entao o `except` abaixo nao o pega. Medido pela
        # `regua-exercitadores.py` no dia em que ela contou as copias desta funcao:
        # ha CINCO `ler_pasta()` nesta pasta, em DUAS versoes, e as tres que ja
        # tinham o `errors` sobreviviam ao mesmo mundo em que estas duas morriam.
        # Quem cobra a propriedade e a metade 3 do `teste-exercitadores.py`, que
        # DESCOBRE as copias pelo nome em vez de as listar.
        try:
            with open(os.path.join(pasta, nome), encoding="utf-8", errors="replace") as f:
                saida[nome] = f.read()
        except OSError:
            continue
    return saida


if __name__ == "__main__":
    # `--teto` imprime SO o inteiro, e existe para o `teste-voz.mjs`. Ele poderia
    # chamar o PHP direto — ja chama php para renderizar —, e nao chama de
    # proposito: a banda crivel acima e a regua do portao, e perguntar ao PHP por
    # cima dela seria recriar em JavaScript o alargamento que ela impede. Uma
    # autoridade para o numero, uma para a banda.
    if "--teto" in sys.argv[1:]:
        print(perguntar()["teto"])
        raise SystemExit(0)

    c = perguntar()
    print("teto=%d  separador=%r  marca=%r  cauda=%r" % (c["teto"], c["separador"], c["marca"], cauda(c)))
    denuncias, avisos = redigitados(ler_pasta(), c["teto"])
    for d in denuncias:
        print("DENUNCIA  %s:%d  %s  — %s" % (d[0], d[1], d[2], d[3]))
    for a in avisos:
        print("aviso     %s:%d  %s  — %s (prosa, nao mede nada)" % (a[0], a[1], a[2], a[3]))

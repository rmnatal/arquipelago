#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTAO da `regua-constantes-de-snippet.py`. Sem rede.

Exercita a regua contra respostas e contra pastas ENCENADAS, e no fim roda a
regua DE VERDADE, como processo, contra uma ilha de sombra — porque conta certa
com fiacao errada foi exatamente como o defeito que ela persegue nasceu nesta
pasta (achado 11 do fecho das 17h04Z de 19/10/2026).

  python3 ferramentas/teste-constantes-de-snippet.py .

O QUE ELE AFIRMA, em seis metades
---------------------------------
  1. `ler_resposta()` — resposta que falta ou nao presta levanta
     `RespostaInvalida`, e NUNCA devolve lista de consolo.
  2. `nomes_locais()` — o grau de prova do nome: inteiro e sem prefixo sao
     fortes, cauda de dois segmentos e forte, cauda de um e fraca.
  3. `mesmo_valor()` — numero compara como numero (`40`, `40.0`, `40.00`),
     texto compara como texto e o espaco do separador E o valor.
  4. `varrer()` — os tres vereditos e as tres posicoes, e a regra de que prova
     fraca com valor diferente nao vira achado nenhum.
  5. A EXENCAO — o marcador cala a denuncia, e cala apenas a linha dele.
CUIDADO AO ESCREVER NESTE ARQUIVO: A BANCADA CLASSIFICA PELO TEXTO, PROSA
INCLUIDA (medido em 19/10/2026)
----------------------------------------------------------------------------
A `bancada.py` decide a classe de cada portao procurando uma marca no TEXTO do
arquivo (ver a `MARCA_NAVEGADOR` dela). Quem CITA o nome de um portao de
Chromium, ainda que num comentario ou dentro de uma string de encenacao, e
mandado para a classe de Chromium — que roda so com `--navegador`, leva dezenas
de minutos e quase nunca roda.

Aconteceu duas vezes com este arquivo na mesma passada: primeiro pelo NOME do
portao encenado da metade 6 (renomeado para `portao-encenado-que-redigita.mjs`,
porque encenacao nao se chama como a coisa encenada — a mesma licao do
`TETO_ENCENADO` do fecho das 17h04Z), e depois por um comentario que explicava a
primeira vez CITANDO os nomes. Por isso esta secao nao escreve nenhum deles.

Portao que nao roda na passada padrao fica vermelho sem ninguem ver, e nao e
hipotese: foi assim que este bloco encontrou o portao da vitrine da C15 — ver o
achado registrado no fecho desta passada. **O defeito nao e deste arquivo e nao
foi consertado aqui:** a classificacao da bancada deveria perguntar se a linha
MEDE alguma coisa, que e o que a `onde()` da `regua-teto-do-titulo.py` sabe
responder, em vez de procurar a marca na pasta inteira do texto. Generalizar
isso pede medir antes quantos portoes estao hoje na classe errada, e isso e
bloco — nao um remendo de passagem (19.2).

  6. PONTA A PONTA — a regua, rodada como processo contra uma ilha de sombra,
     DENUNCIA um portao encenado que redigita uma constante, sai 1, e volta a
     sair 0 quando a mesma linha ganha o marcador. E a sombra tem o `define()`
     TROCADO, que e a unica forma de provar que o valor e lido e nao redigitado:
     com teto igual ao da ilha, um portao que redigitasse passaria igual.
"""

import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, "ferramentas")

_spec = importlib.util.spec_from_file_location(
    "regua_constantes_de_snippet", os.path.join(PASTA, "regua-constantes-de-snippet.py")
)
regua = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(regua)

falhas = 0
afirmacoes = 0


def ok(nome, condicao, medida=""):
    global falhas, afirmacoes
    afirmacoes += 1
    if condicao:
        print("  ok    %s%s" % (nome, (" — %s" % medida) if medida else ""))
    else:
        falhas += 1
        print("  FALHOU %s%s" % (nome, (" — %s" % medida) if medida else ""))


def levanta(nome, texto):
    try:
        regua.ler_resposta(texto)
    except regua.RespostaInvalida as e:
        ok(nome, True, str(e)[:60])
        return
    except Exception as e:  # noqa: BLE001
        ok(nome, False, "levantou %s e nao RespostaInvalida" % type(e).__name__)
        return
    ok(nome, False, "nao levantou nada")


# ---------------------------------------------------------------------------
print("1. ler_resposta() — nenhum caminho devolve padrao")

levanta("resposta vazia e invalida", "")
levanta("resposta de espaco em branco e invalida", "   \n  ")
levanta("resposta ilegivel e invalida", "{isto nao e json")
levanta("resposta truncada e invalida", '{"constantes": {"AQUAMETRIA_X": {"valor": 1,')
levanta("lista no lugar de objeto e invalida", '["AQUAMETRIA_X"]')
levanta("objeto sem constantes e invalido", '{"constantes": {}, "snippets_pulados": []}')
levanta("constantes que nao e objeto e invalido", '{"constantes": 65, "snippets_pulados": []}')
levanta(
    "constante sem o campo valor e invalida",
    '{"constantes": {"AQUAMETRIA_X": {"tipo": "numero"}}, "snippets_pulados": []}',
)
levanta(
    "constante sem o campo tipo e invalida",
    '{"constantes": {"AQUAMETRIA_X": {"valor": 65}}, "snippets_pulados": []}',
)
levanta(
    "constante fora do prefixo da ilha e invalida",
    '{"constantes": {"OUTRA_COISA": {"valor": 65, "tipo": "numero"}}, "snippets_pulados": []}',
)
levanta(
    "resposta sem a lista de snippets pulados e invalida",
    '{"constantes": {"AQUAMETRIA_X": {"valor": 65, "tipo": "numero"}}}',
)

boa = (
    '{"constantes": {"AQUAMETRIA_TITULO_TETO": {"valor": 65, "tipo": "numero"}},'
    ' "snippets_lidos": ["a.php"], "snippets_pulados": ["b.php"]}'
)
lida = regua.ler_resposta(boa)
ok("resposta boa devolve a constante", lida["constantes"]["AQUAMETRIA_TITULO_TETO"]["valor"] == 65)
ok("resposta boa devolve o tipo", lida["constantes"]["AQUAMETRIA_TITULO_TETO"]["tipo"] == "numero")
ok("resposta boa devolve os pulados", lida["snippets_pulados"] == ["b.php"])

# ---------------------------------------------------------------------------
print("\n2. nomes_locais() — o grau de prova do nome")

n = regua.nomes_locais("AQUAMETRIA_C15_VITRINE_LARGURA_CM")
ok("o nome inteiro e prova forte", n.get("AQUAMETRIA_C15_VITRINE_LARGURA_CM") == "forte")
ok("o nome sem o prefixo da ilha e prova forte", n.get("C15_VITRINE_LARGURA_CM") == "forte")
ok("cauda de tres segmentos e prova forte", n.get("VITRINE_LARGURA_CM") == "forte")
ok("cauda de dois segmentos e prova forte", n.get("LARGURA_CM") == "forte")
ok("cauda de um segmento e prova FRACA", n.get("CM") is None, "curta demais, nem entra")

n2 = regua.nomes_locais("AQUAMETRIA_SEO_NOME_DO_SITE")
ok("SITE e cauda de um segmento e portanto prova FRACA", n2.get("SITE") == "fraca")
ok("NOME_DO_SITE e prova forte", n2.get("NOME_DO_SITE") == "forte")

n3 = regua.nomes_locais("AQUAMETRIA_TITULO_TETO")
ok("TETO e prova fraca pelo nome, e vai depender do valor", n3.get("TETO") == "fraca")

mapa = regua.mapa_de_nomes({"AQUAMETRIA_C1_VERSAO": {}, "AQUAMETRIA_SEO_VERSAO": {}})
ok("um nome local pode apontar para DUAS constantes", len(mapa.get("VERSAO", [])) == 2, "VERSAO")

# ---------------------------------------------------------------------------
print("\n3. mesmo_valor() — numero compara como numero, texto como texto")

ok("40 e 40 e o mesmo valor", regua.mesmo_valor("40", 40, "numero"))
ok("40.0 e 40 e o mesmo valor", regua.mesmo_valor("40.0", 40, "numero"))
ok("40.00 e 40 e o mesmo valor", regua.mesmo_valor("40.00", 40, "numero"))
ok("45 NAO e 40", not regua.mesmo_valor("45", 40, "numero"))
ok("texto no lugar de numero nao casa", not regua.mesmo_valor("quarenta", 40, "numero"))
ok("None nunca casa", not regua.mesmo_valor(None, 40, "numero"))
ok("'alta' e 'alta' e o mesmo valor", regua.mesmo_valor("alta", "alta", "string"))
ok("'Alta' NAO e 'alta'", not regua.mesmo_valor("Alta", "alta", "string"))
# O ESPACO DO SEPARADOR E O VALOR, e esta afirmacao existe porque apara-lo faria
# a regua dizer que ' – ' e '–' sao a mesma coisa — e a diferenca muda a conta
# do teto do `<title>`.
ok("o separador com espaco dos dois lados casa", regua.mesmo_valor(" – ", " – ", "string"))
ok("o separador SEM os espacos nao casa", not regua.mesmo_valor("–", " – ", "string"))

# ---------------------------------------------------------------------------
print("\n4. varrer() — os tres vereditos e as tres posicoes")

CONSTANTES = {
    "AQUAMETRIA_C15_VITRINE_NIVEL": {"valor": "alta", "tipo": "string"},
    "AQUAMETRIA_C15_VITRINE_LARGURA_CM": {"valor": 45, "tipo": "numero"},
    "AQUAMETRIA_TITULO_TETO": {"valor": 65, "tipo": "numero"},
    "AQUAMETRIA_SEO_NOME_DO_SITE": {"valor": "Aquametria", "tipo": "string"},
}


def varrer(texto, nome="portao-encenado.py"):
    return regua.varrer({nome: texto}, CONSTANTES, fora=())


d, a = varrer("NIVEL = 'alta'\n")
ok("nome casa e valor casa, em codigo: DENUNCIA", len(d) == 1 and not a, "%d/%d" % (len(d), len(a)))
ok("a denuncia nomeia a constante", d and d[0]["constante"] == "AQUAMETRIA_C15_VITRINE_NIVEL")
ok("a denuncia traz o veredito REDIGITADO", d and d[0]["veredito"] == "REDIGITADO")

d, a = varrer('NIVEL = "alta"\n')
ok("aspa dupla conta igual a simples", len(d) == 1)

d, a = varrer("LARGURA_CM = 45\n")
ok("cauda de dois segmentos com valor igual: DENUNCIA", len(d) == 1 and not a)

d, a = varrer("LARGURA_CM = 45.0\n")
ok("o mesmo valor escrito como decimal: DENUNCIA", len(d) == 1 and not a)

d, a = varrer("TETO = 65\n")
ok("cauda FRACA com valor igual: DENUNCIA, porque sao duas provas", len(d) == 1 and not a)

d, a = varrer("LARGURA_CM = 40\n")
ok("nome forte e valor diferente: AVISO de homonimo, nao denuncia", not d and len(a) == 1)
ok("o aviso diz homonimo", a and a[0]["veredito"] == "HOMONIMO")
ok("o aviso traz o valor do snippet para quem le decidir", a and a[0]["valor"] == 45)
ok("o aviso traz o literal escrito no portao", a and a[0]["literal"] == "40")

d, a = varrer('SITE = "https://aquametria.com.br"\n')
ok("nome FRACO e valor diferente: nao e achado nenhum", not d and not a, "silencioso")

d, a = varrer("# NIVEL = 'alta' era digitado aqui\n")
ok("redigito em PROSA nao denuncia", not d and len(a) == 1)
ok("o aviso de prosa diz que e prosa", a and a[0]["posicao"] == "prosa")

d, a = varrer("  * `NIVEL = 'alta'` no portao da vitrine\n")
ok("nome entre acentos graves e prosa", not d and len(a) == 1)

d, a = varrer("d, saida = varrer(\"NIVEL = 'alta'\\n\")\n")
ok("mundo ENCENADO dentro de aspas e silencioso", not d and not a, "e o caso deste proprio arquivo")

d, a = varrer("SUBNIVEL = 'alta'\n")
ok("o nome nao casa no MEIO de outro nome", not d and not a, "SUBNIVEL nao e NIVEL")

d, a = varrer("NIVELZINHO = 'alta'\n")
ok("o nome nao casa no COMECO de outro nome", not d and not a)

# ESTA AFIRMACAO FOI ESCRITA PELA MUTACAO 14, e e o caso que importa: um nome
# TODO EM MAIUSCULA que contem o outro (`SUBNIVEL`) e consumido inteiro pelo
# proprio padrao, entao ele passaria mesmo sem a guarda da frente. Quem so
# depende da guarda e o nome com prefixo MINUSCULO, e sem ele a mutacao que
# arranca a guarda sobrevive — foi o que ela fez na primeira rodada.
d, a = varrer("meuNIVEL = 'alta'\n")
ok("prefixo minusculo nao faz o nome casar", not d and not a, "meuNIVEL nao e NIVEL")
d, a = varrer("$NIVEL = 'alta'\n")
ok("sigilo de variavel de PHP nao faz o nome casar", not d and not a)

d, a = varrer("nivel = 'alta'\n")
ok("nome em minuscula nao e constante local", not d and not a)

d, a = varrer("NIVEL = outra_coisa()\n")
ok("atribuicao que nao e literal nao e redigito", not d and not a)

d, a = varrer("VERSAO = '1.2.0'\n")
ok("nome que nao esta nas constantes nao da achado", not d and not a)

d, a = varrer("NIVEL = 'alta'\nLARGURA_CM = 45\nTETO = 65\n")
ok("tres redigitos em tres linhas: tres denuncias", len(d) == 3)
ok("cada denuncia traz a sua linha", sorted(x["linha"] for x in d) == [1, 2, 3])

d, a = varrer("const LARGURA_CM = 45, NIVEL = 'alta';\n")
ok("duas atribuicoes na MESMA linha: duas denuncias", len(d) == 2, "%d" % len(d))

d, a = regua.varrer({"regua-constantes-de-snippet.py": "NIVEL = 'alta'\n"}, CONSTANTES)
ok("a propria regua esta fora da varredura", not d and not a)
d, a = regua.varrer({"regua-teto-do-titulo.py": "TETO = 65\n"}, CONSTANTES)
ok("a regua do teto esta fora da varredura", not d and not a)
d, a = regua.varrer({"listar-constantes-do-snippet.php": "NIVEL = 'alta'\n"}, CONSTANTES)
ok("o perguntador esta fora da varredura", not d and not a)

# ---------------------------------------------------------------------------
print("\n5. a exencao mora na linha, e cala so a linha dela")

d, a = varrer("NIVEL = 'alta'   # REGUA PROPRIA: e a entrada do teste\n")
ok("o marcador cala a denuncia", not d and not a)

d, a = varrer("const NIVEL = 'alta';   // REGUA PROPRIA: entrada do teste\n")
ok("o marcador vale em .mjs tambem", not d and not a)

d, a = varrer("LARGURA_CM = 40   # REGUA PROPRIA: secao da varredura\n")
ok("o marcador cala o aviso de homonimo tambem", not d and not a)

d, a = varrer("NIVEL = 'alta'   # REGUA PROPRIA\nTETO = 65\n")
ok("o marcador NAO cala a linha seguinte", len(d) == 1 and d[0]["linha"] == 2, "linha %s" % (d[0]["linha"] if d else "—"))

d, a = varrer("# a linha abaixo era REGUA PROPRIA e deixou de ser\nTETO = 65\n")
ok("marcador na linha de CIMA nao cala nada", len(d) == 1, "a declaracao fica ao lado do numero")

# ---------------------------------------------------------------------------
print("\n6. ponta a ponta — a regua de verdade, contra uma ilha de SOMBRA")

sombra = tempfile.mkdtemp(prefix="aqm-constantes-")
try:
    for pasta in ("snippets", "ferramentas", "dados"):
        shutil.copytree(os.path.join(RAIZ, pasta), os.path.join(sombra, pasta))

    # O `define()` DA SOMBRA E OUTRO, e e isto que prova que o valor e lido: com
    # 90 nos dois lados, um portao que redigitasse 90 passaria por engano.
    alvo = os.path.join(sombra, "snippets", "aquametria-calculadora-iluminacao.php")
    with io.open(alvo, encoding="utf-8") as f:
        php = f.read()
    trocado = php.replace("define( 'AQUAMETRIA_C15_VITRINE_CM', 90 )", "define( 'AQUAMETRIA_C15_VITRINE_CM', 118 )")
    ok("a sombra teve o define trocado", trocado != php, "90 -> 118")
    with io.open(alvo, "w", encoding="utf-8") as f:
        f.write(trocado)

    def rodar(args=()):
        return subprocess.run(
            ["python3", os.path.join(sombra, "ferramentas", "regua-constantes-de-snippet.py")] + list(args),
            capture_output=True,
            text=True,
            cwd=sombra,
        )

    r = rodar(["--constante", "AQUAMETRIA_C15_VITRINE_CM"])
    ok("a regua da sombra LE o define trocado", r.stdout.strip() == "118", r.stdout.strip() or r.stderr.strip()[:60])
    ok("e sai 0 ao responder", r.returncode == 0)

    r = rodar(["--constante", "AQUAMETRIA_NAO_EXISTE"])
    ok("constante inexistente sai 1 e nao imprime valor", r.returncode == 1 and not r.stdout.strip())

    r = rodar(["--constante", "AQUAMETRIA_SYNC_VERSAO"])
    ok(
        "constante de snippet PULADO sai 1 em vez de inventar",
        r.returncode == 1 and "nao sao perguntaveis" in r.stderr,
    )

    # A sombra, como esta, tem de passar: ela e a ilha de hoje com um numero
    # trocado, e nenhum portao dela redigita esse numero.
    r = rodar()
    ok("a sombra intocada passa", r.returncode == 0, "%d denuncia(s) na saida" % r.stdout.count("DENUNCIA"))
    ok("a saida diz quantas constantes foram perguntadas", "constantes perguntadas ao PHP" in r.stdout)
    ok(
        "a saida diz NAO MEDIDAS, e nao zero, para os snippets pulados",
        "NAO MEDIDAS (nao zero)" in r.stdout and "AQUAMETRIA_SYNC_VERSAO" in r.stdout,
    )

    # Agora um portao encenado que redigita o numero NOVO da sombra.
    encenado = os.path.join(sombra, "ferramentas", "portao-encenado-que-redigita.mjs")
    with io.open(encenado, "w", encoding="utf-8") as f:
        f.write("const VITRINE_CM = 118;\n")
    r = rodar()
    ok("portao que redigita a constante e DENUNCIADO", r.returncode == 1, "saida %d" % r.returncode)
    ok("a denuncia nomeia o arquivo", "portao-encenado-que-redigita.mjs" in r.stdout)
    ok("a denuncia nomeia a constante", "AQUAMETRIA_C15_VITRINE_CM" in r.stdout)

    # E a mesma linha, com o marcador, volta a passar.
    with io.open(encenado, "w", encoding="utf-8") as f:
        f.write("const VITRINE_CM = 118;   // REGUA PROPRIA: encenacao do portao\n")
    r = rodar()
    ok("a mesma linha com o marcador volta a passar", r.returncode == 0, "saida %d" % r.returncode)

    # E o redigito do valor ANTIGO nao e denunciado, porque nao e mais o valor
    # do snippet — vira homonimo, que avisa e nao reprova.
    with io.open(encenado, "w", encoding="utf-8") as f:
        f.write("const VITRINE_CM = 90;\n")
    r = rodar()
    ok("o valor VELHO nao denuncia: ele virou homonimo", r.returncode == 0 and "aviso" in r.stdout)
finally:
    shutil.rmtree(sombra, ignore_errors=True)

# ---------------------------------------------------------------------------
print("\n%d afirmacoes, %d falha(s)" % (afirmacoes, falhas))
raise SystemExit(1 if falhas else 0)

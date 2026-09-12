#!/usr/bin/env python3
"""
MUTACOES DELIBERADAS CONTRA O PORTAO DA TAG DE MEDICAO — Aquametria.

    python3 ferramentas/mutacoes-ga4.py

Cada mutacao quebra o gtag de um jeito que ja aconteceu ou que aconteceria, numa
COPIA da ilha, e roda o ferramentas/teste-ga4.py nela. Mutacao que PASSA e o
portao nao medindo nada — e o defeito que a secao 8 do ARQUIPELAGO.md persegue
desde 10/09/2026, quando tres travas novas da Robometria aprovaram codigo
quebrado.

O CUIDADO QUE ESTE ARQUIVO TEM DE TER, e que custou rodadas nas outras ilhas:
mutacao que nao MORDE e verde honesto com cara de portao. Uma mutacao aqui muda o
que o SITE serve (o snippet) ou o que a REGUA le (o PROMPT.md) — e quando o alvo e
a regua, ela tem de produzir o mundo do defeito nas duas metades, ou reprova por
motivo errado.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = "snippets/aquametria-casca.php"
PROMPT = "PROMPT.md"


def troca(arquivo, de, para, vezes=1):
    """Substituicao exata, que RECUSA operar se o alvo nao estiver la — a trava
    contra a mutacao inerte: alvo que nao existe mais nao quebra nada, e o teste
    passa por engano."""
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        texto = open(caminho, encoding="utf-8").read()
        if texto.count(de) != vezes:
            raise SystemExit(
                "MUTACAO INERTE: %r aparece %d vez(es) em %s, esperava %d"
                % (de, texto.count(de), arquivo, vezes))
        open(caminho, "w", encoding="utf-8").write(texto.replace(de, para, vezes))
    return aplicar


MUTACOES = [
    ("o ID da ilha vizinha na constante — a tag mede, e manda a audiencia para outra ilha",
     troca(CASCA, "'AQUAMETRIA_CASCA_GA4_ID', 'G-8Y26XFZF39'",
           "'AQUAMETRIA_CASCA_GA4_ID', 'G-RM7KS75QP2'")),

    ("uma letra trocada no ID — o erro que ninguem le conferindo de olho",
     troca(CASCA, "'AQUAMETRIA_CASCA_GA4_ID', 'G-8Y26XFZF39'",
           "'AQUAMETRIA_CASCA_GA4_ID', 'G-8Y26XFZF38'")),

    ("o carregador perde o async e passa a bloquear a pintura",
     troca(CASCA, "echo '<script async src=\"'", "echo '<script src=\"'")),

    ("o ID volta a ser digitado no meio da funcao, longe da constante",
     troca(CASCA, "$id = AQUAMETRIA_CASCA_GA4_ID;", "$id = 'G-8Y26XFZF39';")),

    ("a prioridade desce para 2 — a tag entra ANTES da meta descricao e do JSON-LD",
     troca(CASCA, "'</script>' . \"\\n\";\n}, 23 );", "'</script>' . \"\\n\";\n}, 2 );")),

    ("a prioridade sobe para 21, que ainda e antes do BreadcrumbList da prioridade 22",
     troca(CASCA, "'</script>' . \"\\n\";\n}, 23 );", "'</script>' . \"\\n\";\n}, 21 );")),

    ("um segundo parametro na URL do carregador, e o E-comercial volta a ser escapado",
     troca(CASCA, "'https://www.googletagmanager.com/gtag/js?id=' . $id",
           "'https://www.googletagmanager.com/gtag/js?l=dataLayer&id=' . $id")),

    ("porta de consentimento: a configuracao passa a esperar um clique",
     troca(CASCA, "\"gtag('config',\" . wp_json_encode( $id ) . ');'",
           "\"document.addEventListener('aqm-consent',function(){gtag('config',\""
           " . wp_json_encode( $id ) . ');});'")),

    ("a tag sai do wp_head e vai para o wp_footer, onde nao mede pagina vista cedo",
     troca(CASCA, "add_action( 'wp_head', function () {\n\t/* Esta guarda",
           "add_action( 'wp_footer', function () {\n\t/* Esta guarda")),

    ("a guarda da constante ausente cai, e o site serviria o nome da constante crua",
     troca(CASCA,
           "if ( ! defined( 'AQUAMETRIA_CASCA_GA4_ID' ) || '' === AQUAMETRIA_CASCA_GA4_ID ) {\n\t\treturn;\n\t}",
           "if ( false ) {\n\t\treturn;\n\t}")),

    # A versao viaja nesta mutacao, e por isso ela e a primeira a virar INERTE
    # quando a casca sobe de numero. Reapontada em 12/09/2026 (1.6.0 -> 1.7.0):
    # mutacao que nao morde e teste verde com outro nome.
    ("a versao da casca fica atras da do manifest — o conserto commitado e invisivel",
     troca(CASCA, "'AQUAMETRIA_CASCA_VERSAO', '1.7.0'", "'AQUAMETRIA_CASCA_VERSAO', '1.6.9'")),

    # As duas ultimas atacam a REGUA, nao o site. Se o portao lesse o ID do
    # snippet, elas passariam — e e exatamente por isso que elas existem.
    ("a regua perde a fonte: o PROMPT.md deixa de declarar o ID de medicao",
     troca(PROMPT, "ID de medição **G-8Y26XFZF39**", "ID de medicao nao declarado")),

    ("o PROMPT.md passa a declarar um ID e o snippet serve outro — as duas fontes divergem",
     troca(PROMPT, "ID de medição **G-8Y26XFZF39**", "ID de medição **G-0K5PY39HV7**")),
]


def rodar(aplicar):
    base = tempfile.mkdtemp(prefix="mut-ga4-")
    copia = os.path.join(base, "ilha")
    shutil.copytree(RAIZ, copia)
    try:
        aplicar(copia)
        r = subprocess.run([sys.executable, os.path.join(copia, "ferramentas", "teste-ga4.py")],
                           capture_output=True, text=True)
        return r.returncode, (r.stdout + r.stderr)
    finally:
        shutil.rmtree(base, ignore_errors=True)


print("MUTACOES CONTRA O PORTAO DA TAG DE MEDICAO — %d deliberadas" % len(MUTACOES))
print("A copia limpa tem de PASSAR; toda mutacao tem de REPROVAR.\n")

codigo, saida = rodar(lambda base: None)
if codigo != 0:
    print("A COPIA LIMPA JA REPROVA — conserte o portao antes de mutar:")
    print(saida[-2500:])
    sys.exit(1)
print("copia limpa: passa (%s)\n" % re.search(r"\d+ afirmacoes", saida).group(0))

passaram = []
for i, (nome, aplicar) in enumerate(MUTACOES, 1):
    codigo, saida = rodar(aplicar)
    if codigo == 0:
        print("%2d. PASSOU (portao cego) — %s" % (i, nome))
        passaram.append(nome)
    else:
        motivo = [l.strip() for l in saida.splitlines() if l.strip().startswith("- ")]
        print("%2d. reprovou — %s" % (i, nome))
        for m in motivo[:2]:
            print("      %s" % m)

print("\n%d de %d reprovadas" % (len(MUTACOES) - len(passaram), len(MUTACOES)))
if passaram:
    print("\nMUTACOES QUE O PORTAO NAO VIU — cada uma e uma trava que falta:")
    for n in passaram:
        print("  - " + n)
    sys.exit(1)

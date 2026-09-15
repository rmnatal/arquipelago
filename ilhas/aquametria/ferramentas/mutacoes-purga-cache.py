#!/usr/bin/env python3
"""AS MUTACOES DA PURGA — e cada uma declara a FRASE que espera ouvir de volta.

    python3 ferramentas/mutacoes-purga-cache.py .

`teste-purga-cache.php` afirma que a funcao que apaga arquivo PARA quando a
levam para fora da pasta dela. Afirmacao assim e a mais facil de escrever verde
por acidente: basta a funcao nao apagar nada, ou basta a armadilha nao ser uma
armadilha. Esta bateria quebra a casca de proposito, de um jeito por vez, e
cobra que o portao REPROVE — e que reprove PELA AFIRMACAO CERTA.

POR QUE A FRASE ESPERADA IMPORTA, e nao so o codigo de saida: reprovar nao e a
mesma coisa que reprovar pelo motivo certo. Uma mutacao que derruba a funcao
inteira faria o teste falhar em tudo, e a bateria ficaria verde sem nunca ter
medido a guarda que ela dizia estar medindo. Cada caso abaixo nomeia um pedaco
da afirmacao que TEM de aparecer na saida.

E O MUNDO INTACTO TEM DE PASSAR. Sem ele a bateria estaria so dizendo nao: um
teste que reprova sempre reprova todas as mutacoes e nao mede nada.

ONDE ISSO ACONTECE: numa copia da ilha em pasta temporaria. A mutacao nunca
toca o repositorio, e o proprio teste so apaga arquivo dentro do /tmp dele.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ".")
CASCA = os.path.join("snippets", "aquametria-casca.php")
TESTE = os.path.join("ferramentas", "teste-purga-cache.php")

with open(os.path.join(RAIZ, CASCA), encoding="utf-8") as f:
    ORIGINAL = f.read()

# Cada mutacao: (nome, funcao que devolve a casca quebrada, pedaco da afirmacao
# que tem de aparecer reprovada). O pedaco e curto de proposito — texto longo
# quebraria a bateria quando alguem reescrever o rotulo, e o que se esta medindo
# e QUAL guarda caiu, nao como ela foi redigida.
A_GUARDA_DO_VAZIO = (
    "\tif ( ! is_string( $pasta ) || ! is_string( $raiz ) "
    "|| '' === $pasta || '' === $raiz ) {\n\t\treturn;\n\t}\n\n"
)


def sem_guarda_do_vazio(src):
    """O ACIDENTE DE 15/09/2026. `realpath('')` devolve o diretorio de trabalho
    atual, nao false — entao sem esta linha a funcao esvazia de onde o processo
    esta rodando. Foi assim que este teste apagou a pasta da ilha."""
    assert A_GUARDA_DO_VAZIO in src
    return src.replace(A_GUARDA_DO_VAZIO, "", 1)


def sem_contencao(src):
    """A guarda que a recursao usa a cada nivel: o caminho real tem de comecar
    pelo caminho real da raiz. Sem ela, qualquer pasta do disco e alvo."""
    alvo = ("\tif ( ! $real_raiz || ! $real || 0 !== strpos( $real . DIRECTORY_SEPARATOR,\n"
            "\t\trtrim( $real_raiz, DIRECTORY_SEPARATOR ) . DIRECTORY_SEPARATOR ) ) {\n"
            "\t\treturn;\n\t}\n")
    assert alvo in src
    return src.replace(alvo, "\tif ( ! $real_raiz || ! $real ) {\n\t\treturn;\n\t}\n", 1)


def contencao_por_prefixo_de_texto(src):
    """A PORTA DOS FUNDOS MAIS PLAUSIVEL, porque parece a mesma coisa: comparar
    sem a barra no fim faz `/cachedeoutro` comecar com `/cache` e virar alvo.
    E o erro que alguem comete ao 'simplificar' a linha acima."""
    alvo = ("0 !== strpos( $real . DIRECTORY_SEPARATOR,\n"
            "\t\trtrim( $real_raiz, DIRECTORY_SEPARATOR ) . DIRECTORY_SEPARATOR )")
    assert alvo in src
    return src.replace(alvo, "0 !== strpos( $real, $real_raiz )", 1)


def segue_link_simbolico(src):
    """Apagar o link e seguro; seguir o link e sair da pasta sem perceber."""
    alvo = ("\t\tif ( is_link( $caminho ) ) {\n")
    assert alvo in src
    return src.replace(alvo, "\t\tif ( false ) {\n", 1)


def gatilho_sem_prefixo(src):
    """Sem o prefixo, a purga dispara na gravacao de option de QUALQUER plugin —
    uma varredura de pasta em cada `update_option` do site."""
    alvo = "\tif ( 0 === strpos( (string) $opcao, 'aquametria_' ) ) {"
    assert alvo in src
    return src.replace(alvo, "\tif ( true ) {", 1)


def purga_mais_de_uma_vez(src):
    """Sem a trava de uma vez por requisicao, uma revisao que grava vinte
    options faz vinte varreduras na mesma requisicao do Sync."""
    alvo = ("function aquametria_casca_purgar_cache() {\n"
            "\tstatic $ja = false;\n\tif ( $ja ) {\n\t\treturn;\n\t}\n\t$ja = true;\n")
    assert alvo in src
    return src.replace(alvo, "function aquametria_casca_purgar_cache() {\n", 1)


def raiz_sem_pasta(src):
    """A raiz do cache nao pode ser apagada, so esvaziada: o plugin a recria, e
    sumir com ela nao e direito da ilha. Esta mutacao a remove no fim."""
    alvo = ("\t\t\taquametria_casca_esvaziar_pasta( $caminho, $real_raiz );\n"
            "\t\t\t@rmdir( $caminho );\n")
    assert alvo in src
    return src.replace(alvo, "\t\t\taquametria_casca_esvaziar_pasta( $caminho, $real_raiz );\n", 1)


MUTACOES = [
    ("sem a guarda do caminho vazio", sem_guarda_do_vazio,
     "caminho vazio"),
    ("sem a contencao dentro da raiz", sem_contencao,
     "pasta irmã não é esvaziada"),
    ("contencao comparando prefixo de TEXTO", contencao_por_prefixo_de_texto,
     "COMEÇA pelo da raiz"),
    # O ALVO DO LINK E PROTEGIDO PELA CONTENCAO, NAO PELO `is_link` — medido
    # nesta bateria e nao suposto. Com a mutacao, a recursao entra no atalho,
    # `realpath()` o resolve para fora da raiz e a contencao para ali; o que
    # sobra quebrado e o proprio link, que fica no disco servindo cache velho.
    # Por isso a afirmacao esperada e a do link, e nao a do alvo: e a unica que
    # esta mutacao move.
    ("seguindo link simbolico", segue_link_simbolico,
     "o link em si foi apagado"),
    ("gatilho sem o prefixo da ilha", gatilho_sem_prefixo,
     "terceiro"),
    ("purga sem a trava de uma vez por requisicao", purga_mais_de_uma_vez,
     "UMA vez por requisição"),
    ("subpasta esvaziada mas nao removida", raiz_sem_pasta,
     "subpasta foi apagada"),
]


def rodar(casca_fonte):
    """Monta uma copia da ilha com a casca dada e roda o portao nela."""
    tmp = tempfile.mkdtemp(prefix="aqm-mut-")
    try:
        os.makedirs(os.path.join(tmp, "snippets"))
        os.makedirs(os.path.join(tmp, "ferramentas"))
        with open(os.path.join(tmp, CASCA), "w", encoding="utf-8") as f:
            f.write(casca_fonte)
        shutil.copy(os.path.join(RAIZ, TESTE), os.path.join(tmp, TESTE))
        r = subprocess.run(["php", os.path.join(tmp, TESTE), tmp],
                           capture_output=True, text=True, cwd=tmp)
        return r.returncode, r.stdout + r.stderr
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


feitas = 0
falhas = []

print("MUNDO INTACTO — esta TEM de passar")
codigo, saida = rodar(ORIGINAL)
feitas += 1
if codigo == 0:
    print("  ok    o portao aprova a casca de verdade")
else:
    falhas.append("mundo intacto")
    print("  FALHA o portao reprova a casca de verdade:\n" + saida)

print("\nMUTACOES — cada uma TEM de reprovar, e pela afirmacao declarada")
for nome, quebrar, esperado in MUTACOES:
    feitas += 1
    try:
        quebrada = quebrar(ORIGINAL)
    except AssertionError:
        falhas.append(nome + " (INERTE: o alvo nao existe mais na casca)")
        print("  FALHA %s — INERTE, o alvo sumiu do arquivo" % nome)
        continue
    if quebrada == ORIGINAL:
        falhas.append(nome + " (INERTE: nao mudou nada)")
        print("  FALHA %s — INERTE, a mutacao nao mudou o arquivo" % nome)
        continue

    codigo, saida = rodar(quebrada)
    reprovou = codigo != 0
    linhas_falha = [l for l in saida.splitlines() if "FALHA" in l]
    pelo_motivo = any(esperado in l for l in linhas_falha)
    if reprovou and pelo_motivo:
        print("  ok    %s — reprova em: %s" % (nome, esperado))
    elif reprovou:
        falhas.append(nome + " (reprovou pelo motivo ERRADO)")
        print("  FALHA %s — reprovou, mas nao pela afirmacao '%s'. Falhas vistas:\n    %s"
              % (nome, esperado, "\n    ".join(linhas_falha) or "(nenhuma)"))
    else:
        falhas.append(nome + " (passou)")
        print("  FALHA %s — o portao APROVOU a casca quebrada" % nome)

print("\n" + "=" * 70)
if falhas:
    print("REPROVADO: %d baterias, %d errada(s):" % (feitas, len(falhas)))
    for f in falhas:
        print("  - " + f)
    sys.exit(1)
print("APROVADO: %d baterias, todas decidindo certo, ZERO inertes." % feitas)

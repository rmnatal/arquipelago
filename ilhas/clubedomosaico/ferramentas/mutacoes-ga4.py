#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a tag do GA4 de proposito, uma mutacao por vez, e exige que
`teste-casca.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-ga4.py

Por que este arquivo existe: os portoes do GA4 nasceram VERDES na primeira
rodada, e teste verde que nunca foi visto reprovar nao mediu nada (secao 8 do
ARQUIPELAGO.md). Pior neste caso especifico do que no geral: a tag e a unica
coisa desta ilha cujo defeito NAO APARECE NA TELA. Uma tag no lugar errado, com
o ID de outra ilha ou impressa duas vezes serve uma pagina identica a esta, e o
sintoma so chega semanas depois, como um numero errado num relatorio que ninguem
tem como conferir de memoria. Portao de coisa invisivel e o que mais precisa
ser visto reprovando.

O QUE ESTAS MUTACOES PROCURAM, em tres familias:
  1. A TAG SOME ou sai pela metade — o caso facil, e o unico que alguem notaria.
  2. A TAG FICA, MAS ERRADA: ID de outra ilha, ID digitado no meio do codigo,
     config discordando do src. Sao os que servem uma pagina perfeita.
  3. A TAG FICA CERTA E NO LUGAR ERRADO: sem `async`, antes do JSON-LD, antes do
     <title>, ou depois da folha de fontes. O despacho de 12/09/2026 escreveu
     cada uma dessas linhas, e linha de despacho que nenhuma medicao defende e
     linha que a proxima versao apaga sem ninguem ver.

Cada uma roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")


def editar(raiz, arquivo, velho, novo, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    if texto.count(velho) < vezes:
        raise AssertionError(
            "mutacao INERTE: %r aparece %d vez(es) em %s, esperava %d"
            % (velho[:60], texto.count(velho), arquivo, vezes))
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, vezes))


# --------------------------------------------- 1. a tag some ou sai pela metade

def m_tag_nao_sai(raiz):
    """O caso trivial: ninguem imprime a tag. Se esta passar, nenhuma das
    outras vale nada."""
    editar(raiz, CASCA,
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex",
           "\t// echo cdm_casca_ga4_html();")


def m_so_o_carregador(raiz):
    """Meia tag: o script do Google carrega e ninguem chama `config`. E o
    defeito que mais parece funcionar — a requisicao sai, a aba da rede mostra
    200, e a propriedade nao recebe UMA sessao."""
    editar(raiz, CASCA,
           "\t\t. \"gtag('config','\" . $id . \"');\"\n",
           "")


def m_guarda_recusa_tudo(raiz):
    """A guarda de formato passa a recusar o ID de verdade. A funcao continua
    existindo, o site continua de pe, e a ilha volta a medir zero em silencio —
    que e o estado de onde este bloco partiu."""
    editar(raiz, CASCA,
           "\tif ( ! preg_match( '/^G-[A-Z0-9]{6,}$/', $id ) ) {",
           "\tif ( ! preg_match( '/^GA4-[A-Z0-9]{6,}$/', $id ) ) {")


def m_guarda_aceita_tudo(raiz):
    """O outro lado: a guarda some. Nao quebra a pagina de hoje — quebra a
    borda, e e por isso que a borda esta medida."""
    editar(raiz, CASCA,
           "\tif ( ! preg_match( '/^G-[A-Z0-9]{6,}$/', $id ) ) {\n\t\treturn '';\n\t}",
           "\tif ( '' === $id ) {\n\t\treturn '';\n\t}")


# ------------------------------------------- 2. a tag fica, mas errada

def m_id_de_outra_ilha(raiz):
    """O ID da Robometria no lugar do desta ilha. E o defeito que a copia desta
    casca para a ilha 4 vai produzir, e ele nao tem sintoma nenhum no site: as
    duas ilhas passam a somar visita na mesma propriedade."""
    editar(raiz, CASCA,
           "\tdefine( 'CDM_CASCA_GA4_ID', 'G-0K5PY39HV7' );",
           "\tdefine( 'CDM_CASCA_GA4_ID', 'G-RM7KS75QP2' );")


def m_id_digitado_no_meio(raiz):
    """A constante fica de pe e o `config` passa a ter o ID digitado. Duas
    fontes para o mesmo fato, que e a familia de defeito que este repositorio
    ja encontrou em quatro lugares diferentes."""
    editar(raiz, CASCA,
           "\t\t. \"gtag('config','\" . $id . \"');\"",
           "\t\t. \"gtag('config','G-0K5PY39HV7');\"")


def m_config_discorda_do_src(raiz):
    """O `src` carrega uma propriedade e o `config` nomeia outra. O navegador
    nao reclama; a sessao vai para o lugar errado."""
    editar(raiz, CASCA,
           "\t\t. \"gtag('config','\" . $id . \"');\"",
           "\t\t. \"gtag('config','G-0K5PY39HV7X');\"")


def m_tag_duas_vezes(raiz):
    """A mesma tag impressa duas vezes — o que acontece de verdade no dia em que
    alguem conectar o Site Kit (que ESTA instalado nesta ilha) sem tirar esta
    daqui. Toda sessao passa a ser contada duas vezes."""
    editar(raiz, CASCA,
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex",
           "\techo cdm_casca_ga4_html(); echo cdm_casca_ga4_html();")


# ------------------------------------- 3. a tag certa, no lugar errado

def m_sem_async(raiz):
    """Sem `async` o script de terceiro vira bloqueante e entra na frente da
    folha de fontes — o unico jeito de esta mudanca piorar o LCP da ilha."""
    editar(raiz, CASCA,
           "\treturn '<script async src=\"' . esc_url( $src ) . '\"></script>' . \"\\n\"",
           "\treturn '<script src=\"' . esc_url( $src ) . '\"></script>' . \"\\n\"")


def m_antes_do_jsonld(raiz):
    """Prioridade 3: a tag passa na frente do Organization e do BreadcrumbList.
    A pagina fica identica para quem olha; o que muda e a ordem em que o
    rastreador le, e o despacho escreveu essa linha de proposito."""
    editar(raiz, CASCA,
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex\n}, 8 );",
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex\n}, 3 );")


def m_depois_das_fontes(raiz):
    """O outro extremo: prioridade 30, depois da folha de fontes. Nao quebra
    nada e nao mede nada de errado — so atrasa a medicao para depois do recurso
    mais lento da pagina, que e o contrario de "o mais cedo possivel"."""
    editar(raiz, CASCA,
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex\n}, 8 );",
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex\n}, 30 );")


def m_segundo_script_de_terceiro(raiz):
    """Um segundo script de fora entra na pagina publica. O despacho diz que o
    gtag e o UNICO permitido, e sem esta mutacao essa frase seria so uma frase."""
    editar(raiz, CASCA,
           "\techo cdm_casca_ga4_html(); // markup fixo + constante conferida por regex",
           "\techo cdm_casca_ga4_html();\n\techo '<script src=\"https://cdn.exemplo.com/a.js\"></script>';")


# ------------------------------------- 4. a promessa da pagina de privacidade

def m_privacidade_volta_a_prometer(raiz):
    """A pagina de Privacidade volta a dizer "se um dia houver medicao" com a
    medicao ligada — e SEM tirar a frase nova, que e como isso acontece de
    verdade: alguem acrescenta um paragrafo e nao le o que ja estava ali. A
    pagina passa a afirmar as duas coisas ao mesmo tempo, e e por isso que o
    portao mede a AUSENCIA da frase velha, e nao so a presenca da nova.

    A primeira versao desta mutacao trocava a frase nova PELA velha, e com isso
    reprovava pelo portao errado — o da frase nova, que qualquer coisa derruba.
    Mutacao que morde a trava vizinha deixa a trava que interessa sem medida."""
    editar(raiz, CASCA,
           "\t$html .= '<p>Não há remarketing, não há pixel de rede social",
           "\t$html .= '<p>Se um dia houver medição de audiência, esta página será atualizada <em>antes</em> de ela ser ligada, com a data da mudança.</p>';\n"
           "\t$html .= '<p>Não há remarketing, não há pixel de rede social")


def m_privacidade_sem_data(raiz):
    """A frase fica e a data sai. O despacho pede a data porque e ela que
    separa "sempre mediu" de "comecou em tal dia" — e a secao 21 vai precisar
    desse marco para saber a partir de quando o zero e dado."""
    editar(raiz, CASCA,
           "<strong>Desde 12 de setembro de 2026, o site usa o Google Analytics 4 para medir audiência</strong>",
           "<strong>O site usa o Google Analytics 4 para medir audiência</strong>")


MUTACOES = [
    ("a tag simplesmente nao sai", m_tag_nao_sai),
    ("so o carregador, sem o config (meia tag)", m_so_o_carregador),
    ("a guarda de formato recusa o ID de verdade", m_guarda_recusa_tudo),
    ("a guarda de formato aceita qualquer coisa", m_guarda_aceita_tudo),
    ("o ID de outra ilha na constante", m_id_de_outra_ilha),
    ("o ID digitado no meio do codigo, ao lado da constante", m_id_digitado_no_meio),
    ("o config nomeia um ID diferente do src", m_config_discorda_do_src),
    ("a tag impressa duas vezes (o caso Site Kit)", m_tag_duas_vezes),
    ("o script de terceiro perde o async", m_sem_async),
    ("a tag entra ANTES do JSON-LD (prioridade 3)", m_antes_do_jsonld),
    ("a tag entra DEPOIS da folha de fontes (prioridade 30)", m_depois_das_fontes),
    ("um segundo script de terceiro na pagina publica", m_segundo_script_de_terceiro),
    ("a privacidade volta a prometer o que ja aconteceu", m_privacidade_volta_a_prometer),
    ("a frase da privacidade perde a data", m_privacidade_sem_data),
]


def rodar_teste(raiz):
    r = subprocess.run([sys.executable and "php", "ferramentas/teste-casca.php", "."],
                       cwd=raiz, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A casca de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("Casca intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-ga4-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [" + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if "FALHA" in linha:
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-56s | %s" % (nome, primeira[:78]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

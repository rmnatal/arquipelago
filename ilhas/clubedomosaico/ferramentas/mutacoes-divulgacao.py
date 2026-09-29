#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a pagina de divulgacao de afiliados de proposito, uma mutacao por vez,
e exige que `teste-casca.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-divulgacao.py

POR QUE ESTE ARQUIVO EXISTE, e a causa tem data e esteve no ar quatro dias.
A secao "Nem todo link daqui rende comissao" foi escrita em 14/09/2026, quando a
busca CRUA era o botao de 15 itens e a frase "essa busca nao e link de afiliado:
ninguem nos paga por aquele clique" era verdadeira. Em 16/09 a Open API de
afiliados entrou (25.6 do ARQUIPELAGO.md) e em 25/09 os 38 itens do banco
ganharam busca ENCURTADA, que E link de afiliado. A pagina continuou servindo a
frase do mundo anterior — e servindo-a sobre 28 botoes que saem com
`rel="sponsored"`. A ilha declarava a relacao paga ao buscador e a negava a quem
le, na unica pagina cujo produto inteiro e a divulgacao.

NENHUM PORTAO VIA, e o motivo e estrutural: o texto mora na casca, o `rel` mora
na F2, e nenhuma regua comparava os dois. Verde na primeira execucao e prova
nenhuma (secao 8), entao as mutacoes abaixo sao as que reescrevem exatamente o
defeito que aconteceu, e nao as obvias:

  * A FRASE DE 14/09 VOLTANDO — o proprio acontecimento, palavra por palavra.
  * O `rel` MUDANDO SEM O TEXTO MUDAR, e o contrario tambem: e o par que falha,
    nunca um lado so, e e por isso que a regua pergunta ao codigo em vez de
    guardar a resposta.
  * A PARCELA DO MEIO SUMINDO DA CONTA — o segundo defeito do mesmo dia. A
    pagina publicava 10 com ficha e 0 sem rastreio, de 38, e nenhum digito
    estava visivelmente errado: o que faltava era uma classificacao inteira.
  * A CONTA VOLTANDO A SAIR DO INSTANTANEO, que ainda traz `piso_nao_rastreavel`
    em 15 — disclosure velho nao envelhece, mente.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")
F2 = os.path.join("snippets", "clubedomosaico-f2.php")


def ler(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, rel, texto):
    with open(os.path.join(raiz, rel), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, rel, antigo, novo, vezes=1):
    texto = ler(raiz, rel)
    if antigo not in texto:
        raise AssertionError("mutacao nao achou o alvo em %s: %r" % (rel, antigo[:70]))
    gravar(raiz, rel, texto.replace(antigo, novo, vezes))


# ------------------------------------------------------------------ mutacoes

def m_frase_de_14_09_volta(raiz):
    """O acontecimento, palavra por palavra: a busca encurtada volta a ser
    anunciada como link que nao rende."""
    trocar(raiz, CASCA,
           "<strong>Também é link de afiliado</strong> e também pode render comissão.",
           "essa busca <strong>não é link de afiliado</strong>: ninguém nos paga por aquele clique.")


def m_texto_cala_sobre_a_busca(raiz):
    """A forma silenciosa do mesmo defeito: o <li> da busca encurtada deixa de
    dizer que e afiliado, sem afirmar o contrario. Omitir tambem e enganar."""
    trocar(raiz, CASCA,
           "<strong>Também é link de afiliado</strong> e também pode render comissão. Ela existe",
           "Ela existe")


def m_rel_da_busca_cai_para_nofollow(raiz):
    """O outro lado do par: o codigo para de declarar a relacao paga e o texto
    continua prometendo comissao. A pagina passa a prometer o que o site nao faz."""
    trocar(raiz, F2,
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca\" href=\"' . esc_url( $busca ) . '\"'\n\t\t\t. ' rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';",
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca\" href=\"' . esc_url( $busca ) . '\"'\n\t\t\t. ' rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';")


def m_rel_da_busca_crua_vira_patrocinado(raiz):
    """A mentira na direcao oposta, que e a que os programas punem: chamar de
    patrocinado o clique que nao paga."""
    trocar(raiz, F2,
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua\" href=\"' . esc_url( $crua ) . '\"'\n\t\t\t. ' rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';",
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua\" href=\"' . esc_url( $crua ) . '\"'\n\t\t\t. ' rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';")


def m_parcela_do_meio_some_da_conta(raiz):
    """O defeito de 25/09 na conta: duas parcelas de tres, sem nenhum digito
    visivelmente errado."""
    trocar(raiz, CASCA,
           "' o botão é a ficha do produto e em ' . cdm_casca_num( $com_busca ) . ' é a busca na loja: esses ' . cdm_casca_num( $rendem ) . ' são link de afiliado e podem render comissão.",
           "' o botão é a ficha do produto, que é link de afiliado e pode render comissão.")


def m_soma_deixa_de_fechar(raiz):
    """A soma passa a contar so a ficha — parcela certa, total errado."""
    trocar(raiz, CASCA,
           "$rendem       = $com_ficha + $com_busca;",
           "$rendem       = $com_ficha;")


def m_parcela_da_busca_troca_de_fonte(raiz):
    """A parcela do meio passa a ser o total de quem espera link, sem descontar
    quem nao tem rastreio. Hoje os dois numeros sao iguais porque o sem-rastreio
    e zero: a mutacao so aparece quando ele deixar de ser, que e exatamente
    quando ela custa caro."""
    trocar(raiz, CASCA,
           "$com_busca    = (int) $n['esperando_link'] - (int) $n['piso_nao_rastreavel'];",
           "$com_busca    = (int) $n['esperando_link'];")


def m_conta_volta_a_sair_do_instantaneo(raiz):
    """A trava da via viva cai e a conta passa a poder sair do instantaneo de
    14/09, que ainda declara 15 buscas sem rastreio num banco que tem zero."""
    trocar(raiz, CASCA,
           "if ( ! empty( $n['numeros_vivos'] ) ) {",
           "if ( true ) {")
    trocar(raiz, CASCA,
           "\t\t$n['numeros_vivos']        = true;\n", "")


MUTACOES = [
    ("a frase de 14/09 volta ao ar", m_frase_de_14_09_volta),
    ("o texto cala sobre a busca encurtada", m_texto_cala_sobre_a_busca),
    ("o `rel` da busca encurtada cai para nofollow", m_rel_da_busca_cai_para_nofollow),
    ("a busca crua passa a se dizer patrocinada", m_rel_da_busca_crua_vira_patrocinado),
    ("a parcela do meio some da conta", m_parcela_do_meio_some_da_conta),
    ("a soma do que rende deixa de fechar", m_soma_deixa_de_fechar),
    ("a parcela da busca troca de fonte", m_parcela_da_busca_troca_de_fonte),
    ("a conta volta a poder sair do instantaneo", m_conta_volta_a_sair_do_instantaneo),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-casca.php"), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A casca de verdade ja esta reprovada — conserte antes de mutar.")
        print(base_saida[-2000:])
        return 1
    print("casca intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-div-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if linha.strip().startswith("FALHA"):
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-52s | %s" % (nome, primeira[:92]))
        except AssertionError as erro:
            passaram.append("%s (a mutacao nao conseguiu ser escrita: %s)" % (nome, erro))
            print("  MUTACAO INVALIDA: %s — %s" % (nome, erro))
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

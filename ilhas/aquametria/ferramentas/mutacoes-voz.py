#!/usr/bin/env python3
"""Quebra o portao da voz DE PROPOSITO, uma quebra por vez, e exige que ele reprove.

    python3 ferramentas/mutacoes-voz.py

Por que existe: um teste verde so vale alguma coisa depois de alguem ter visto
ele ficar vermelho. A secao 8 do ARQUIPELAGO.md tem tres cicatrizes da mesma
familia — teste que chama a regua de quem produziu o dado, grade que nao pisa na
borda, e afirmacao medida no HTML inteiro em vez do corpo — e as tres passaram
verdes ate alguem quebrar o codigo para ver.

Cada mutacao abaixo e um defeito PLAUSIVEL, do tipo que entra num commit sem
ninguem notar. A mutacao que mais importa e a numero 3: ela nao escreve nada de
errado na tela, so embrulha a pagina inteira na classe que declara "isto aqui e
camada de prova". E a porta dos fundos da regra estrutural, e se ela passasse, a
marca `aqm-prova` valeria zero.

Cada mutacao roda num repositorio COPIADO, entao o repositorio de verdade nunca
e tocado.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CASCA = 'snippets/aquametria-casca.php'
ARTIGOS = 'snippets/aquametria-artigos.php'


def troca(arquivo, velho, novo, vezes=1):
    """Mutacao por substituicao literal. Falha alto se o alvo nao existir mais."""
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit(f'ALVO SUMIU em {arquivo}: {velho[:70]!r}\n'
                             'A mutacao nao pode ser aplicada, entao ela nao prova nada. '
                             'Atualize esta lista junto com o codigo.')
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


def regex(arquivo, padrao, novo):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        s2, n = re.subn(padrao, novo, s, count=1)
        if n == 0:
            raise SystemExit(f'ALVO SUMIU (regex) em {arquivo}: {padrao[:70]!r}')
        p.write_text(s2, encoding='utf-8')
    return aplicar


MUTACOES = [
    (
        'o termo proibido volta para o primeiro paragrafo da home',
        troca(CASCA,
              'Pega a fita métrica e anota comprimento, largura e altura em centímetros.',
              'Esta consulta paramétrica aceita comprimento, largura e altura em centímetros.'),
    ),
    (
        'um cartao volta a se chamar pelo nome interno da ferramenta',
        troca(CASCA,
              "'titulo'  => 'Qual filtro dá conta do seu aquário?',",
              "'titulo'  => 'Calculadora de vazão do filtro e turnover',"),
    ),
    (
        'a PORTA DOS FUNDOS: a home inteira se declara camada de prova',
        troca(CASCA,
              "$html  = '<div class=\"aqm-bloco\">';\n\n\t/* 1. A pergunta mais frequente da ilha, com as três medidas. */",
              "$html  = '<div class=\"aqm-bloco aqm-prova\">';\n\n\t/* 1. A pergunta mais frequente da ilha, com as três medidas. */"),
    ),
    (
        'a contagem de calculadoras no ar passa a ser digitada',
        regex(CASCA,
              r"\$html \.= '<p>' \. esc_html\( \$publicadas \) \. ' de ' \. esc_html\( \$total \) \. ' já estão no ar\.",
              r"$html .= '<p>7 de 8 já estão no ar."),
    ),
    (
        'a abertura da home perde uma das tres medidas',
        troca(CASCA,
              'anota comprimento, largura e altura em centímetros',
              'anota comprimento e largura em centímetros'),
    ),
    (
        'a camada de prova sobe para antes das contas',
        regex(CASCA,
              r"\t/\* 2\. As outras contas\.",
              "\t$html .= '<div class=\"aqm-secao aqm-prova\"><h2>Antes de tudo</h2><p>Prova subindo.</p></div>';\n\n\t/* 2. As outras contas."),
    ),
    (
        'o guia deixa de ser link e vira texto morto',
        troca(CASCA,
              "$html .= '<h3><a href=\"' . esc_url( $url ) . '\">' . esc_html( $g['manchete'] ) . '</a></h3>';",
              "$html .= '<h3>' . esc_html( $g['manchete'] ) . '</h3>';"),
    ),
    (
        'o menu volta a falar a lingua do painel',
        troca(CASCA,
              "'metodologia'  => 'Como a gente calcula',",
              "'metodologia'  => 'Metodologia',"),
    ),
    (
        'a pagina Sobre emagrece abaixo do piso de corpo',
        regex(CASCA,
              r"add_shortcode\( 'aquametria_sobre', function \(\) \{\n\t\$html  = '<div class=\"aqm-bloco\">';",
              "add_shortcode( 'aquametria_sobre', function () {\n\treturn '<div class=\"aqm-bloco\"><p class=\"aqm-linha-mestra\">A gente faz as contas do seu aquário.</p></div>';\n\t$html  = '<div class=\"aqm-bloco\">';"),
    ),
    (
        'a tagline do WordPress volta a ser a descricao interna do produto',
        troca(CASCA,
              "define( 'AQUAMETRIA_CASCA_TAGLINE_CURTA', 'as contas do seu aquário' );",
              "define( 'AQUAMETRIA_CASCA_TAGLINE_CURTA', 'Calculadoras e dados técnicos para dimensionar o seu aquário conforme a ficha técnica' );"),
    ),
    (
        'a prateleira de guias some porque ninguem mais se anuncia',
        troca(ARTIGOS,
              "add_filter( 'aquametria_guias', 'aquametria_artigos_registrar_guias' );",
              "/* mutacao: sem anuncio */"),
    ),
]


def rodar_portao(base: Path):
    r = subprocess.run(['node', str(base / 'ferramentas/teste-voz.mjs'), str(base)],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    codigo, saida = rodar_portao(RAIZ)
    if codigo != 0:
        print('O portao ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.')
        print(saida[-2000:])
        return 1
    print(f'repositorio limpo: portao verde ({saida.count("  ok ")} afirmacoes)\n')

    reprovou = 0
    for i, (nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            shutil.copytree(RAIZ, base, ignore=shutil.ignore_patterns('node_modules', '.git'))
            aplicar(base)
            codigo, saida = rodar_portao(base)
            falhas = [l.strip() for l in saida.splitlines() if l.strip().startswith('FALHA')]
            if codigo != 0:
                reprovou += 1
                print(f'  {i:2d}. REPROVOU (certo) — {nome}')
                for l in falhas[:3]:
                    print(f'        {l}')
            else:
                print(f'  {i:2d}. PASSOU (ERRADO) — {nome}')
                print('        o portao nao viu este defeito. Ele nao protege contra ele.')

    print(f'\n{reprovou} de {len(MUTACOES)} mutacoes reprovadas pelo portao')
    return 0 if reprovou == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

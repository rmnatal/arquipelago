#!/usr/bin/env python3
"""Quebra o portao da arvore DE PROPOSITO, uma quebra por vez, e exige que ele reprove.

    python3 ferramentas/mutacoes-arvore.py

Um teste verde so vale alguma coisa depois de alguem ter visto ele ficar
vermelho. A secao 8 do ARQUIPELAGO.md junta seis cicatrizes da mesma familia, e
tres delas passaram verdes ate alguem quebrar o codigo para ver.

AS DUAS MUTACOES QUE MAIS VALEM AQUI, e por que:

  - A numero 4 e a PORTA DOS FUNDOS do schema. Ela nao escreve nada errado na
    tela: so acrescenta ao BreadcrumbList o degrau de categoria que ainda nao
    tem endereco. Fica parecendo um breadcrumb mais completo, e e o contrario —
    ListItem do meio sem `item` invalida a lista inteira no Google, e lista
    invalida e lista ignorada. O schema publicaria MENOS do que publica hoje,
    com cara de publicar mais.
  - A numero 8 e a cicatriz do numero de tela digitado, feita do jeito que um
    editor de verdade a faria: ela troca a contagem por um 5 cravado — que e
    EXATO hoje — E tira uma calculadora do ar na mesma passada. As duas metades
    passam a errar juntas. Quem ve e a regua independente: o teste conta os
    cartoes com link no HUB, nao pergunta ao snippet quantos existem.

UM LIMITE DECLARADO, porque fingir que ele nao existe seria pior: se alguem
mudar a categoria da C5 no snippet E no ARVORE.md na mesma passada, este portao
NAO ve — as duas metades passam a dizer a mesma coisa nova e nao ha terceira
fonte no repositorio que diga de que categoria uma calculadora e. Categoria e
decisao editorial, e a unica trava contra ela e a leitura humana. As mutacoes 1
e 2 cobrem o caso de UMA das metades mudar, que e o que acontece por descuido.

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
ARVORE = 'ARVORE.md'
RENDER = 'ferramentas/render-pagina-completa.php'


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


def varias(*aplicadores):
    """Uma mutacao que mexe em duas metades, como um editor de verdade mexeria."""
    def aplicar(base: Path):
        for a in aplicadores:
            a(base)
    return aplicar


MUTACOES = [
    (
        'a C5 muda de categoria SO no snippet (o documento fica para tras)',
        regex(CASCA,
              r"'codigo'  => 'C5',\n\t\t\t'categoria' => 'aquecimento-e-luz',",
              "'codigo'  => 'C5',\n\t\t\t'categoria' => 'filtragem',"),
    ),
    (
        'a C5 muda de categoria SO no ARVORE.md (o codigo fica para tras)',
        troca(ARVORE,
              '| `/calculadoras/aquecimento-e-luz/` | C5 aquecedor',
              '| `/calculadoras/aquecimento-e-luz/` | C55 aquecedor'),
    ),
    (
        'o ultimo degrau da trilha vira link para si mesmo',
        troca(CASCA,
              "$html .= '<span aria-current=\"page\">' . esc_html( $d['rotulo'] ) . '</span>';",
              "$html .= '<a href=\"' . esc_url( home_url( '/' ) ) . '\">' . esc_html( $d['rotulo'] ) . '</a>';"),
    ),
    (
        'A PORTA DOS FUNDOS: o schema ganha o degrau de categoria SEM endereco',
        troca(CASCA,
              "\t\tif ( '' === $d['url'] ) {\n\t\t\tcontinue;\n\t\t}\n\t\t$pos++;",
              "\t\t$pos++;"),
    ),
    (
        'o teto de irmas sobe de 4 para 5 — so a borda FABRICADA ve isto',
        troca(CASCA,
              'return array_slice( $irmas, 0, 4 );',
              'return array_slice( $irmas, 0, 5 );'),
    ),
    (
        'a pagina entra na propria lista de irmas',
        troca(CASCA,
              "\t\t\tif ( empty( $c['slug'] ) || $c['slug'] === $slug ) {\n\t\t\t\tcontinue;\n\t\t\t}",
              "\t\t\tif ( empty( $c['slug'] ) ) {\n\t\t\t\tcontinue;\n\t\t\t}"),
    ),
    (
        'a calculadora passa a receber GUIA como irma (categoria herdando regua alheia)',
        troca(CASCA,
              "\t\t$irmas = array_merge( $perto, $longe );\n\t\treturn array_slice( $irmas, 0, 4 );",
              "\t\tforeach ( aquametria_casca_guias() as $g ) {\n"
              "\t\t\tarray_unshift( $perto, array( 'slug' => $g['slug'], 'rotulo' => $g['manchete'] ) );\n\t\t}\n"
              "\t\t$irmas = array_merge( $perto, $longe );\n\t\treturn array_slice( $irmas, 0, 4 );"),
    ),
    (
        'AS DUAS METADES JUNTAS: a contagem vira 5 cravado E uma calculadora sai do ar',
        varias(
            troca(CASCA,
                  "$quantas = aquametria_casca_conta_no_ar();",
                  "$quantas = 5;"),
            troca(RENDER,
                  "\t'calculadora-de-iluminacao'                 => true,",
                  "\t/* mutacao: a C15 saiu do ar */"),
        ),
    ),
    (
        'a rede de seguranca perde a trava e a trilha sai DUAS vezes',
        troca(CASCA,
              "\tif ( is_admin() || ! is_singular() || aquametria_casca_trilha_impressa() ) {\n\t\treturn $html;\n\t}",
              "\tif ( is_admin() || ! is_singular() ) {\n\t\treturn $html;\n\t}"),
    ),
    (
        'a trilha passa a sair tambem na home',
        varias(
            troca(CASCA,
                  "\tif ( is_front_page() || ! is_singular() ) {\n\t\treturn '';\n\t}",
                  "\tif ( ! is_singular() ) {\n\t\treturn '';\n\t}"),
            troca(CASCA,
                  "\t\t'calculadoras'            => 'Calculadoras',",
                  "\t\t'inicio'                  => 'Início',\n\t\t'calculadoras'            => 'Calculadoras',"),
        ),
    ),
    (
        'O CONSERTO TENTADOR: a categoria vira link para a pagina que nao existe',
        troca(CASCA,
              "\t\t\t$html .= '<span class=\"aqm-trilha-espera\">' . esc_html( $d['rotulo'] ) . '</span>';",
              "\t\t\t$html .= '<a href=\"' . esc_url( home_url( '/calculadoras/aquecimento-e-luz/' ) ) . '\">' . esc_html( $d['rotulo'] ) . '</a>';"),
    ),
    (
        'a trilha desce para depois do H1',
        troca(CASCA,
              "\treturn $trilha . $conteudo;\n}, 10, 2 );",
              "\treturn $conteudo . $trilha;\n}, 10, 2 );"),
    ),
    (
        'a ancora das irmas vira "Saiba mais"',
        troca(CASCA,
              "$html .= '<li><a href=\"' . esc_url( $url ) . '\">' . esc_html( $irma['rotulo'] ) . '</a></li>';",
              "$html .= '<li><a href=\"' . esc_url( $url ) . '\">Saiba mais</a></li>';"),
    ),
    (
        'o guia ganha frase de mae apontando para /guias/, que nao existe',
        troca(CASCA,
              "\tif ( '' !== $url_mae && 'calculadoras' === $n1_slug ) {",
              "\tif ( 'guias' === $n1_slug ) {\n"
              "\t\t$html .= '<p class=\"aqm-veja-mae\">Este e um dos <a href=\"' . esc_url( home_url( '/guias/' ) ) . '\">3 guias</a> da ilha.</p>';\n"
              "\t}\n\tif ( '' !== $url_mae && 'calculadoras' === $n1_slug ) {"),
    ),
]


def rodar_portao(base: Path):
    r = subprocess.run(['node', str(base / 'ferramentas/teste-arvore.mjs'), str(base)],
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

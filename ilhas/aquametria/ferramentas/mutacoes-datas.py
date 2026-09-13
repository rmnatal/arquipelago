#!/usr/bin/env python3
"""Quebra o portao das datas DE PROPOSITO, uma quebra por vez, e exige que ele
reprove.

    python3 ferramentas/mutacoes-datas.py

Um teste verde so vale depois de alguem ter visto ele ficar vermelho. Cada
mutacao aqui e um defeito PLAUSIVEL — do tipo que entra num commit sem ninguem
notar — e as duas primeiras sao os dois defeitos do despacho da Sentinela de
13/09/2026 escritos de volta: o literal de data digitado no snippet dos artigos
e a ficha de peixe sem autor nem publicador.

AS DUAS MUTACOES QUE MAIS IMPORTAM sao a 5 e a 6, e nenhuma das duas escreve
nada de errado na tela: elas fazem a funcao INVENTAR data quando o WordPress nao
tem nenhuma. `strtotime(' UTC')` devolve AGORA e
`strtotime('0000-00-00 00:00:00 UTC')` devolve o ano zero — as duas guardas da
casca sao carregadas, e sem elas uma pagina que o WordPress diz nao saber quando
mudou passaria a jurar que mudou hoje. E o mundo em que isso acontece nao existe
no banco de hoje: ele e PRODUZIDO pelo portao.

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
PEIXES = 'snippets/aquametria-peixes.php'


def troca(arquivo, velho, novo, vezes=1):
    """Mutacao por substituicao literal. Falha alto se o alvo nao existir mais.

    ALVO SUMIDO NAO E MUTACAO FRACA, E MUTACAO INERTE — e inerte conta como
    passou. Foi o que aconteceu duas vezes nesta ilha, com alvo que dependia da
    vizinhanca do codigo."""
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
        'O DEFEITO DE 13/09 DE VOLTA: dateModified vira literal digitado no snippet',
        troca(ARTIGOS,
              "\t$modificado = function_exists( 'aquametria_casca_data_da_pagina' )\n"
              "\t\t? aquametria_casca_data_da_pagina( 'modificado' )\n"
              "\t\t: '';",
              "\t$modificado = '2026-09-10';"),
    ),
    (
        'O OUTRO DEFEITO DE 13/09: a ficha de peixe volta a servir Article sem editora',
        troca(PEIXES,
              "\t\t\t'author'        => $editora,\n\t\t\t'publisher'     => $editora,\n",
              ""),
    ),
    (
        'a ficha perde so o publisher, e fica com metade da editora',
        troca(PEIXES,
              "\t\t\t'publisher'     => $editora,\n",
              ""),
    ),
    (
        'a ficha para de declarar dateModified, e so ela',
        troca(PEIXES,
              "\t\tif ( '' !== $modificado ) {\n\t\t\t$artigo['dateModified'] = $modificado;\n\t\t}",
              "\t\tif ( false ) {\n\t\t\t$artigo['dateModified'] = $modificado;\n\t\t}"),
    ),
    (
        'A INVENCAO 1: sem data, a casca devolve a data de HOJE em vez de vazio',
        troca(CASCA,
              "\t$momento = strtotime( $cru . ' UTC' );\n\tif ( ! $momento ) {\n\t\treturn '';\n\t}",
              "\t$momento = strtotime( $cru . ' UTC' );\n\tif ( ! $momento ) {\n\t\treturn gmdate( DATE_W3C );\n\t}"),
    ),
    (
        'A INVENCAO 2: a guarda de data vazia cai, e strtotime(" UTC") devolve AGORA',
        troca(CASCA,
              "\tif ( '' === $cru || 0 === strpos( $cru, '0000-00-00' ) ) {",
              "\tif ( 0 === strpos( $cru, '0000-00-00' ) ) {"),
    ),
    (
        'A INVENCAO 3: a guarda do 0000-00-00 cai, e a pagina jura ter mudado no ano zero',
        troca(CASCA,
              "\tif ( '' === $cru || 0 === strpos( $cru, '0000-00-00' ) ) {",
              "\tif ( '' === $cru ) {"),
    ),
    (
        'a casca serve so a parte da data, e nunca mais bate com o lastmod do sitemap',
        troca(CASCA,
              "\treturn gmdate( DATE_W3C, $momento );",
              "\treturn gmdate( 'Y-m-d', $momento );"),
    ),
    (
        'a casca troca os dois campos por dentro: modificado passa a ler post_date',
        troca(CASCA,
              "\t$campo = ( 'publicado' === $qual ) ? 'post_date_gmt' : 'post_modified_gmt';",
              "\t$campo = ( 'publicado' === $qual ) ? 'post_modified_gmt' : 'post_date_gmt';"),
    ),
    (
        'a ficha troca os dois campos por fora: datePublished recebe a data de modificacao',
        troca(PEIXES,
              "\t\t$publicado = function_exists( 'aquametria_casca_data_da_pagina' )\n"
              "\t\t\t? aquametria_casca_data_da_pagina( 'publicado' )\n"
              "\t\t\t: '';",
              "\t\t$publicado = function_exists( 'aquametria_casca_data_da_pagina' )\n"
              "\t\t\t? aquametria_casca_data_da_pagina( 'modificado' )\n"
              "\t\t\t: '';"),
    ),
    (
        'A SIMETRIA FALSA: o artigo passa a publicar a data do post e MOVE tres datas indexadas',
        troca(ARTIGOS,
              "\t\t'datePublished'      => $a['publicado'],",
              "\t\t'datePublished'      => aquametria_casca_data_da_pagina( 'publicado' ),"),
    ),
    (
        'a ficha imprime o campo mesmo vazio, e serve dateModified em branco',
        troca(PEIXES,
              "\t\tif ( '' !== $modificado ) {\n\t\t\t$artigo['dateModified'] = $modificado;\n\t\t}",
              "\t\t$artigo['dateModified'] = $modificado;"),
    ),
]


def rodar_portao(base: Path):
    r = subprocess.run(['python3', str(base / 'ferramentas/teste-datas-schema.py'), str(base)],
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
                for l in falhas[:2]:
                    print(f'        {l[:160]}')
            else:
                print(f'  {i:2d}. PASSOU (ERRADO) — {nome}')
                print('        o portao nao viu este defeito. Ele nao protege contra ele.')

    print(f'\n{reprovou} de {len(MUTACOES)} mutacoes reprovadas pelo portao')
    return 0 if reprovou == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

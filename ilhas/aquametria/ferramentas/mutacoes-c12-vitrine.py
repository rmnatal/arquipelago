#!/usr/bin/env python3
"""Quebra o portao da vitrine da C12 DE PROPOSITO, uma quebra por vez.

    python3 ferramentas/mutacoes-c12-vitrine.py

Por que existe: um teste verde so vale alguma coisa depois de alguem ter visto
ele ficar vermelho. A secao 8 do ARQUIPELAGO.md tem uma familia inteira de
cicatrizes dessa forma — teste que chama a regua de quem produziu o dado, grade
que nao pisa na borda, afirmacao medida no HTML inteiro em vez do corpo, e
mutacao que acha o alvo e mesmo assim nao muda nada na tela.

Cada mutacao abaixo e um defeito PLAUSIVEL, do tipo que entra num commit sem
ninguem notar. Duas delas sao o proprio defeito que este bloco achou no ar: a
numero 3 devolve o rendimento da embalagem para o denominador da dose, e a
numero 4 devolve a ficha ao texto que chamava os 200 L de "uma embalagem
atende" — que e verdade para o JBL e quatro vezes menos que a verdade para o
Seachem Matrix.

COMO A MUTACAO E APLICADA: o repositorio e copiado, a copia e mutada, a pagina
e renderizada DA COPIA, e quem julga e o portao do repositorio LIMPO. O portao
nunca e copiado junto — se ele fosse, uma mutacao poderia, sem querer, afrouxar
a regua que deveria reprova-la.
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SNIPPET = 'snippets/aquametria-calculadora-midia.php'
BANCO = 'dados/produtos-midia.json'


def troca(arquivo, velho, novo, vezes=1):
    """Mutacao por substituicao literal. Falha alto se o alvo nao existir mais."""
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit('ALVO SUMIU em %s: %r\n'
                             'A mutacao nao pode ser aplicada, entao ela nao prova nada. '
                             'Atualize esta lista junto com o codigo.' % (arquivo, velho[:80]))
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


MUTACOES = [
    (
        'a vitrine pintada poe quem tem link de loja na frente',
        troca(SNIPPET,
              "\t\tvar comLink = 0;\n\t\tsequencia.forEach(function (item) {",
              "\t\tvar comLink = 0;\n\t\tsequencia = sequencia.slice().sort(function (a, b) "
              "{ return (b.m.link ? 1 : 0) - (a.m.link ? 1 : 0); });\n\t\tsequencia.forEach(function (item) {"),
    ),
    (
        'a vitrine servida ordena pelo preco, do mais barato para o mais caro',
        troca(SNIPPET,
              "\t$h .= '<ul class=\"aqm-c12-vt-trilho\">';\n\tforeach ( $seq as $item ) {",
              "\t$h .= '<ul class=\"aqm-c12-vt-trilho\">';\n\tusort( $seq, function ( $a, $b ) {\n"
              "\t\treturn ( $a['m']['preco'] ? $a['m']['preco']['min'] : 1e9 ) <=> ( $b['m']['preco'] ? $b['m']['preco']['min'] : 1e9 );\n"
              "\t} );\n\tforeach ( $seq as $item ) {"),
    ),
    (
        'O DEFEITO ORIGINAL: o rendimento da embalagem volta a ser o volume da DOSE',
        troca(SNIPPET,
              "\t\t. aquametria_c12_litros( $m['rende_L'] ) . ' L nessa dosagem';",
              "\t\t. aquametria_c12_litros( $m['volume_max_L'] ) . ' L nessa dosagem';"),
    ),
    (
        'O DEFEITO ORIGINAL, a outra metade: a ficha volta a chamar a dose de "uma embalagem"',
        troca(SNIPPET,
              "\t\t\tlinhas.push('O fabricante declara que <b>' + esc(m.dose_texto) + '</b> atendem <b>até '\n"
              "\t\t\t\t+ litros(m.volume_max_L) + ' L</b> de água');",
              "\t\t\tlinhas.push('Uma embalagem atende, pela declaração do fabricante: <b>até '\n"
              "\t\t\t\t+ litros(m.volume_max_L) + ' L</b> de aquário');"),
    ),
    (
        'o cartao perde a marca de grupo no DOM',
        troca(SNIPPET,
              "\t$h = '<li class=\"aqm-c12-vt-item aqm-c12-vt-grupo-' . esc_attr( $grupo ) . '\">';",
              "\t$h = '<li class=\"aqm-c12-vt-item\">';"),
    ),
    (
        'a midia sem foto some da vitrine servida',
        troca(SNIPPET,
              "\tforeach ( $seq as $item ) {\n\t\t$h .= aquametria_c12_vitrine_cartao_html( $item['m'], $v, $item['grupo'] );",
              "\tforeach ( $seq as $item ) {\n\t\tif ( empty( $item['m']['imagem'] ) ) {\n\t\t\tcontinue;\n\t\t}\n"
              "\t\t$h .= aquametria_c12_vitrine_cartao_html( $item['m'], $v, $item['grupo'] );"),
    ),
    (
        'o numero de embalagens arredonda em vez de subir para a proxima inteira',
        troca(SNIPPET,
              "\t\tvar embalagens = Math.ceil((m.dose_mL_por_L * r.V) / (m.embalagem_L * 1000));",
              "\t\tvar embalagens = Math.round((m.dose_mL_por_L * r.V) / (m.embalagem_L * 1000));"),
    ),
    (
        'a vitrine servida desce para DEPOIS da procedencia (contrato 7)',
        troca(SNIPPET,
              "\t$h .= aquametria_c12_vitrine_servida_html();\n\t$h .= aquametria_c12_tenho_html();\n\t$h .= aquametria_c12_fontes_html();",
              "\t$h .= aquametria_c12_tenho_html();\n\t$h .= aquametria_c12_fontes_html();\n\t$h .= aquametria_c12_vitrine_servida_html();"),
    ),
    (
        'o preco perde a data da coleta e vira preco de hoje',
        troca(SNIPPET,
              "\treturn $valor . $onde . ', cotado em ' . aquametria_c12_data_br( $pr['coletado_em'] );",
              "\treturn $valor . $onde;"),
    ),
    (
        'o cartao sem link vira ancora que nao leva a lugar nenhum',
        troca(SNIPPET,
              "\t\t$h .= '<div class=\"' . esc_attr( $classe ) . '\">';",
              "\t\t$h .= '<a class=\"' . esc_attr( $classe ) . '\" href=\"#\">';"),
    ),
]


# A decima primeira mutacao nao e do portao da vitrine: e do validador, e ela
# prova que a regra V21 morde. Alguem "conserta" o banco pelo rendimento da
# embalagem — 800 L em vez dos 200 L da dose — que e exatamente a confusao que
# a regra existe para pegar.
MUTACAO_V21 = (
    'V21: o volume atendido do Matrix vira o rendimento da embalagem',
    lambda base: _mutar_banco(base),
)


def _mutar_banco(base: Path):
    p = base / BANCO
    d = json.loads(p.read_text(encoding='utf-8'))
    for produto in d['produtos']:
        if produto['id'] == 'seachem-matrix-1l':
            produto['volume_atendido_declarado_L']['max'] = 800
            break
    else:
        raise SystemExit('ALVO SUMIU: seachem-matrix-1l nao esta mais no banco')
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def rodar_portao(base: Path):
    """Renderiza a pagina DA COPIA e julga com o portao do repositorio limpo.

    O HTML sai num arquivo TEMPORARIO e nunca dentro da pasta renderizada: a
    primeira versao escrevia `pagina-c12.html` ao lado do snippet, e na rodada
    do repositorio limpo isso sujava o repositorio de verdade — um arquivo de
    bancada entrando no commit sem ninguem pedir.
    """
    render = subprocess.run(
        ['php', str(RAIZ / 'ferramentas/render-para-teste.php'), str(base), 'aquametria_calculadora_midia'],
        capture_output=True, text=True)
    if render.returncode != 0:
        return render.returncode, 'FALHA no render: ' + render.stderr[-800:]

    with tempfile.NamedTemporaryFile('w', suffix='.html', encoding='utf-8', delete=False) as f:
        f.write(render.stdout)
        html = Path(f.name)
    try:
        r = subprocess.run(['node', str(RAIZ / 'ferramentas/teste-navegador-c12-vitrine.mjs'), str(html)],
                           capture_output=True, text=True, cwd=str(RAIZ))
        return r.returncode, r.stdout + r.stderr
    finally:
        html.unlink(missing_ok=True)


def rodar_validador(base: Path):
    r = subprocess.run([sys.executable, str(base / 'ferramentas/validar-produtos.py')],
                       capture_output=True, text=True, cwd=str(base))
    return r.returncode, r.stdout + r.stderr


def copia(destino):
    shutil.copytree(RAIZ, destino, ignore=shutil.ignore_patterns('node_modules', '.git'))


def main():
    codigo, saida = rodar_portao(RAIZ)
    if codigo != 0:
        print('O portao ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.')
        print(saida[-2000:])
        return 1
    print('repositorio limpo: portao verde (%d afirmacoes)\n' % saida.count('  ok '))

    reprovou = 0
    for i, (nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            copia(base)
            aplicar(base)
            codigo, saida = rodar_portao(base)
            falhas = [l.strip() for l in saida.splitlines() if l.strip().startswith('FALHOU')]
            if codigo != 0:
                reprovou += 1
                print('  %2d. REPROVOU (certo) — %s' % (i, nome))
                for l in falhas[:2]:
                    print('        ' + l[:150])
            else:
                print('  %2d. PASSOU (ERRADO) — %s' % (i, nome))
                print('        o portao nao viu este defeito. Ele nao protege contra ele.')

    # O validador, com a sua propria mutacao.
    nome, aplicar = MUTACAO_V21
    total = len(MUTACOES) + 1
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / 'ilha'
        copia(base)
        aplicar(base)
        codigo, saida = rodar_validador(base)
        if codigo != 0 and 'V21' in saida:
            reprovou += 1
            print('  %2d. REPROVOU (certo) — %s' % (total, nome))
            linha = [l.strip() for l in saida.splitlines() if 'V21' in l]
            if linha:
                print('        ' + linha[0][:150])
        else:
            print('  %2d. PASSOU (ERRADO) — %s' % (total, nome))

    print('\n%d de %d mutacoes reprovadas' % (reprovou, total))
    return 0 if reprovou == total else 1


if __name__ == '__main__':
    sys.exit(main())

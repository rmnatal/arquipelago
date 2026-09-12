#!/usr/bin/env python3
"""Quebra o portao da REGULAGEM da C15 DE PROPOSITO, uma quebra por vez.

    python3 ferramentas/mutacoes-c15-regulagem.py

Por que existe: um teste verde so vale alguma coisa depois de alguem ter visto
ele ficar vermelho. E este bloco tem uma razao a mais para insistir nisso — o
defeito que ele consertou passou por TRES portoes verdes. O validador nao lia a
chave 'vocabulario' do esquema; o teste de navegador media a lista "dentro da
faixa", onde o defeito nao aparece; e o ramo dos reguláveis, que era justamente
o ramo quebrado, nunca executava, entao nao havia o que reprovar. Ramo que nunca
roda e codigo que nenhum teste protege, por mais afirmacoes que o teste tenha.

As mutacoes 1 e 2 sao o proprio defeito que estava no ar em 12/09/2026: a grafia
divergente no banco e a terceira copia da lista dentro do podeRegular().

COMO A MUTACAO E APLICADA: o repositorio e copiado, a copia e mutada, a pagina e
renderizada DA COPIA, e quem julga e o portao do repositorio LIMPO. O portao
nunca e copiado junto — se fosse, uma mutacao poderia afrouxar sem querer a
regua que deveria reprova-la.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SNIPPET = 'snippets/aquametria-calculadora-iluminacao.php'
BANCO = 'dados/produtos-iluminacao.json'
ESQUEMA = 'dados/esquema-produtos.json'
GERADOR = 'ferramentas/gerar-catalogo-iluminacao.py'


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


def _regrava_banco(base: Path, mudar):
    p = base / BANCO
    d = json.loads(p.read_text(encoding='utf-8'))
    if not mudar(d):
        raise SystemExit('ALVO SUMIU no banco de iluminacao')
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def _regrava_esquema(base: Path, mudar):
    p = base / ESQUEMA
    d = json.loads(p.read_text(encoding='utf-8'))
    campo = next((c for c in d['entidades']['iluminacao']['campos'] if c.get('campo') == 'regulagem'), None)
    if campo is None or not mudar(campo):
        raise SystemExit('ALVO SUMIU: a declaracao de regulagem no esquema')
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def _grafia_divergente(base: Path):
    def mudar(d):
        for p in d['produtos']:
            if p.get('regulagem') == 'app' and p['id'] != 'chihiros-wrgb-ii-pro-60':
                p['regulagem'] = 'aplicativo'
                return True
        return False
    _regrava_banco(base, mudar)


def _regulagem_inventada(base: Path):
    """A luminaria que nao declara regulagem ganha uma, sem fonte que a sustente."""
    def mudar(d):
        for p in d['produtos']:
            if p.get('regulagem') in (None, ''):
                p['regulagem'] = 'dimmer'
                return True
        return False
    _regrava_banco(base, mudar)


# ---------------------------------------------------------------- as mutacoes

# Julgadas pelo portao de navegador: o defeito aparece na TELA.
MUTACOES_TELA = [
    (
        # ESTA MUTACAO SAIU INERTE NA PRIMEIRA RODADA, e o motivo virou regra.
        # Devolver a lista para dentro do podeRegular() com os MESMOS valores nao
        # muda um byte na tela: as duas copias concordam no dia em que nascem, e
        # a divergencia chega depois, quando alguem mexe numa e esquece a outra —
        # que foi exatamente a historia deste bloco. Nenhuma medicao de RESULTADO
        # pode pegar isso, porque o resultado e identico. Tentar fazer a mutacao
        # morder mudando tambem o esquema nao resolve: quem julga e o portao do
        # repositorio LIMPO, entao a regua continua lendo o esquema limpo e as
        # duas metades voltam a concordar.
        # A saida nao e uma mutacao mais esperta, e uma afirmacao de outra
        # natureza: o portao mede a ESTRUTURA do podeRegular() servido — que ele
        # le AQM_C15_REGULA e que nao guarda valor de vocabulario digitado. E a
        # mesma licao da secao 8 sobre perdoar por presenca de palavra: quando o
        # certo e o errado produzem o mesmo texto, quem decide e a estrutura.
        'O DEFEITO ORIGINAL: o podeRegular() volta a ter a lista digitada dentro dele',
        troca(SNIPPET,
              "\t\treturn !!p.regulagem && AQM_C15_REGULA.indexOf(p.regulagem) !== -1;",
              "\t\treturn p.regulagem === 'dimmer' || p.regulagem === 'app' || p.regulagem === 'controlador';"),
    ),
    (
        'a terceira copia volta E envelhece: o podeRegular() testa a grafia velha',
        troca(SNIPPET,
              "\t\treturn !!p.regulagem && AQM_C15_REGULA.indexOf(p.regulagem) !== -1;",
              "\t\treturn p.regulagem === 'dimmer' || p.regulagem === 'aplicativo' || p.regulagem === 'controlador';"),
    ),
    (
        'A FRASE COLAPSADA VOLTA: o silencio da ilha vira silencio do fabricante',
        troca(SNIPPET,
              "\t\t\treturn 'e a Aquametria não colheu se ela tem regulagem de intensidade — '\n"
              "\t\t\t\t+ 'não estamos dizendo que o fabricante não oferece, estamos dizendo que não conferimos';",
              "\t\t\treturn 'e não declara regulagem de intensidade';"),
    ),
    (
        'o temporizador passa a contar como quem abaixa o brilho',
        troca(SNIPPET,
              "\t\treturn !!p.regulagem && AQM_C15_REGULA.indexOf(p.regulagem) !== -1;",
              "\t\treturn !!p.regulagem && p.regulagem !== 'nenhuma';"),
    ),
    (
        'o grupo regulável perde a marca no DOM e some da conferencia',
        troca(SNIPPET,
              "\t\t\t+ (viaRegulagem ? ' aqm-c15-produto-regulavel' : '');",
              "\t\t\t+ '';"),
    ),
    (
        'a lista de reguláveis passa de 2 para 3 cartoes',
        troca(SNIPPET,
              "\t\tr.regulaveis = regulaveis.slice(0, 2);",
              "\t\tr.regulaveis = regulaveis.slice(0, 3);"),
    ),
    (
        'quem regula entra na lista principal, misturado com quem cabe na faixa',
        troca(SNIPPET,
              "\t\t\tif (p.fluxo_lm > r.max && podeRegular(p)) {\n\t\t\t\tregulaveis.push(p);",
              "\t\t\tif (p.fluxo_lm > r.max && podeRegular(p)) {\n\t\t\t\tdentro.push(p);"),
    ),
    (
        # Tambem saiu inerte na primeira versao, por outro motivo: mutar o
        # GERADOR nao muda nada enquanto ninguem o roda, e o catalogo ja estava
        # escrito dentro do snippet. Por isso esta entrada pede `regerar`.
        'o gerador para de levar a regulagem para dentro do snippet',
        troca(GERADOR,
              '        item["regulagem"] = p.get("regulagem")',
              '        item["regulagem"] = None'),
        True,
    ),
    (
        'a ficha volta a chamar o campo vazio de "não declarada" pelo fabricante',
        troca(SNIPPET,
              "'Regulagem: <b>' + (p.regulagem ? esc(p.regulagem) : 'não colhemos este campo') + '</b>'",
              "'Regulagem: <b>' + (p.regulagem ? esc(p.regulagem) : 'não declarada') + '</b>'"),
    ),
]

# Julgadas pelo VALIDADOR: o defeito esta no dado ou na declaracao, e tem de
# morrer antes de chegar a tela.
MUTACOES_VALIDADOR = [
    ('V23: a grafia divergente volta ao banco ("aplicativo" onde o vocabulario diz "app")',
     _grafia_divergente, 'V23'),
    ('V23b: regula_intensidade lista um comando que nao existe no vocabulario',
     lambda base: _regrava_esquema(base, lambda c: c.__setitem__('regula_intensidade',
                                                                 c['regula_intensidade'] + ['bluetooth']) or True),
     'V23'),
    ('V2: a luminaria ganha regulagem que nenhuma fonte do registro sustenta',
     _regulagem_inventada, 'V2'),
]

# Julgada pelo GERADOR: sem a declaracao do esquema ele nao pode escrever nada,
# porque lista vazia faria a C15 recusar toda regulagem EM SILENCIO — o mesmo
# defeito com o sinal trocado.
MUTACAO_GERADOR = (
    'o esquema perde a chave regula_intensidade e o gerador escreve lista vazia',
    lambda base: _regrava_esquema(base, lambda c: c.pop('regula_intensidade', None) is not None),
)


def rodar_portao(base: Path):
    render = subprocess.run(
        ['php', str(RAIZ / 'ferramentas/render-para-teste.php'), str(base), 'aquametria_calculadora_iluminacao'],
        capture_output=True, text=True)
    if render.returncode != 0:
        return render.returncode, 'FALHA no render: ' + render.stderr[-800:]
    with tempfile.NamedTemporaryFile('w', suffix='.html', encoding='utf-8', delete=False) as f:
        f.write(render.stdout)
        html = Path(f.name)
    try:
        r = subprocess.run(['node', str(RAIZ / 'ferramentas/teste-navegador-c15-regulagem.mjs'), str(html)],
                           capture_output=True, text=True, cwd=str(RAIZ))
        return r.returncode, r.stdout + r.stderr
    finally:
        html.unlink(missing_ok=True)


def rodar_validador(base: Path):
    r = subprocess.run([sys.executable, str(base / 'ferramentas/validar-produtos.py')],
                       capture_output=True, text=True, cwd=str(base))
    return r.returncode, r.stdout + r.stderr


def rodar_gerador(base: Path):
    r = subprocess.run([sys.executable, str(base / GERADOR)],
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
    print('repositorio limpo: portao verde\n  ' + saida.strip().splitlines()[-1] + '\n')

    reprovou = 0
    total = len(MUTACOES_TELA) + len(MUTACOES_VALIDADOR) + 1
    n = 0

    for entrada in MUTACOES_TELA:
        nome, aplicar = entrada[0], entrada[1]
        regerar = entrada[2] if len(entrada) > 2 else False
        n += 1
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            copia(base)
            for passo in (aplicar if isinstance(aplicar, list) else [aplicar]):
                passo(base)
            if regerar:
                # O gerador da COPIA, para a mutacao chegar ao catalogo embutido.
                r = subprocess.run([sys.executable, str(base / GERADOR)],
                                   capture_output=True, text=True, cwd=str(base))
                if r.returncode != 0:
                    print('  %2d. REPROVOU (certo, no gerador) — %s' % (n, nome))
                    reprovou += 1
                    continue
            codigo, saida = rodar_portao(base)
            if codigo != 0:
                reprovou += 1
                print('  %2d. REPROVOU (certo) — %s' % (n, nome))
                for l in [x.strip() for x in saida.splitlines() if x.strip().startswith('FALHA')][:1]:
                    print('        ' + l[:150])
            else:
                print('  %2d. PASSOU (ERRADO) — %s' % (n, nome))
                print('        o portao nao viu este defeito. Ele nao protege contra ele.')

    for nome, aplicar, regra in MUTACOES_VALIDADOR:
        n += 1
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            copia(base)
            aplicar(base)
            codigo, saida = rodar_validador(base)
            if codigo != 0 and regra in saida:
                reprovou += 1
                print('  %2d. REPROVOU (certo) — %s' % (n, nome))
                linha = [l.strip() for l in saida.splitlines() if regra in l and 'ERRO' in l]
                if linha:
                    print('        ' + linha[0][:150])
            else:
                print('  %2d. PASSOU (ERRADO) — %s' % (n, nome))

    n += 1
    nome, aplicar = MUTACAO_GERADOR
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / 'ilha'
        copia(base)
        aplicar(base)
        codigo, saida = rodar_gerador(base)
        if codigo != 0 and 'regula_intensidade' in saida:
            reprovou += 1
            print('  %2d. REPROVOU (certo) — %s' % (n, nome))
            linha = [l.strip() for l in saida.splitlines() if 'regula_intensidade' in l]
            if linha:
                print('        ' + linha[0][:150])
        else:
            print('  %2d. PASSOU (ERRADO) — %s' % (n, nome))

    print('\n%d de %d mutacoes reprovadas' % (reprovou, total))
    return 0 if reprovou == total else 1


if __name__ == '__main__':
    sys.exit(main())

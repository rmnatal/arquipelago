#!/usr/bin/env python3
"""Quebra DE PROPOSITO o portao da promessa do titulo, uma quebra por vez.

    python3 ferramentas/mutacoes-promessa-do-titulo.py

O portao (`teste-promessa-do-titulo.py`) nasceu em 14/10/2026, no mesmo bloco que
a promessa, e portao recem-nascido e justamente o que ninguem viu ficar vermelho.
A secao 8 do ARQUIPELAGO.md e feita de cicatrizes dessa familia, e a ilha irma
escreveu a frase que explica por que este arquivo existe: as travas da promessa
sao SILENCIOSAS POR DESENHO — quando uma fecha, o titulo volta a ser nome mais
marca, que e sempre valido, e por isso ninguem ve nada quebrar.

A MUTACAO QUE MAIS IMPORTA E A 5, a porta dos fundos: ela erra UMA letra no nome
do gancho, as cinco promessas desaparecem do site inteiro e TODA pagina continua
servindo um <title> valido. Nenhuma ronda de HTTP, nenhum olho na tela e nenhum
dos outros 41 portoes desta bancada veria isso. As afirmacoes 1 e 2 do portao
existem para que ela fique vermelha.

A 3 E A SEGUNDA MAIS IMPORTANTE, e e a razao de a afirmacao 5 do portao existir:
ela muda o BANCO e nao o texto. A promessa acompanha — porque ela sai do banco —
e a meta description, que e escrita a mao, fica para tras dizendo o numero velho.
Titulo e meta prometendo numeros diferentes na MESMA linha de resultado e pior do
que nenhum dos dois prometer nada.

Cada mutacao roda num repositorio COPIADO, entao o repositorio de verdade nunca
e tocado.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SEO = 'snippets/aquametria-seo-tecnico.php'
VAZAO = 'snippets/aquametria-calculadora-vazao.php'
ILUM = 'snippets/aquametria-calculadora-iluminacao.php'
PEIXES = 'snippets/aquametria-peixes.php'
PORTAO = 'ferramentas/teste-promessa-do-titulo.py'


def troca(arquivo, velho, novo, vezes=1):
    """Mutacao por substituicao literal. Falha alto se o alvo nao existir mais.

    Falhar alto e deliberado: `.replace()` cru de alvo sumido NAO falha, e
    mutacao que nao foi aplicada passa pelo portao e e contada como se o portao
    tivesse protegido alguma coisa. Foi assim que quatro mutacoes do
    `mutacoes-escada.py` morreram caladas em 23/09/2026.
    """
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit(f'ALVO SUMIU em {arquivo}: {velho[:70]!r}\n'
                             'A mutacao nao pode ser aplicada, entao ela nao prova nada. '
                             'Atualize esta lista junto com o codigo.')
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


MUTACOES = [
    ('1. a promessa do betta sai da lista do eixo — a pagina de maior trafego da '
     'ilha volta a servir " – Aquametria" e nada mais quebra',
     troca(PEIXES,
           "\t\t'quantos-litros-para-betta' => 'litros-da-base',\n",
           '')),

    ('2. a pagina de CONTROLE ganha promessa por acidente — a /calculadora-de-litragem/ '
     'ficou parada de proposito, e sem ela a leitura de 14/10 nao atribui nada',
     troca(ILUM,
           '\tif ( AQUAMETRIA_C15_SLUG !== $slug ) {',
           "\tif ( ! in_array( $slug, array( AQUAMETRIA_C15_SLUG, 'calculadora-de-litragem' ), true ) ) {")),

    ('3. O BANCO MUDA E A META FICA PARA TRAS: a banda de bolso vai de 5–10 para '
     '5–9 x/h, a promessa acompanha sozinha e a meta description continua dizendo 10',
     troca(VAZAO,
           "'faixa'  => array( 5, 10 ),",
           "'faixa'  => array( 5, 9 ),")),

    ('4. a promessa estoura o teto de 65 — "renovações/h" viram "renovações por hora", '
     'o titulo volta a ser nome + marca em silencio e a promessa desaparece do ar',
     troca(VAZAO,
           "' renovações/h';",
           "' renovações por hora';")),

    ('5. A PORTA DOS FUNDOS: uma letra errada no nome do gancho e as CINCO promessas '
     'somem do site inteiro, com todo <title> continuando valido',
     troca(SEO,
           "apply_filters( 'aquametria_promessa_do_titulo', '', $slug )",
           "apply_filters( 'aquametria_promessa_do_titulos', '', $slug )")),

    ('6. a GRAFIA do numero divergir: o formatador perde a virgula decimal, a promessa '
     'passa a dizer 1.76 e a meta continua dizendo 1,76 na mesma linha de resultado',
     troca(SEO,
           '$texto = number_format_i18n( $v, $casas );',
           '$texto = number_format( $v, $casas );')),
]


def rodar_portao(base: Path):
    r = subprocess.run(['python3', str(base / PORTAO)], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    codigo, saida = rodar_portao(RAIZ)
    if codigo != 0:
        print('O portao ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.')
        print(saida[-2000:])
        return 1
    print('repositorio limpo: portao verde\n')

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

#!/usr/bin/env python3
"""Quebra DE PROPOSITO os dois portoes da dimensao de imagem e exige que eles
reprovem.

    python3 ferramentas/mutacoes-dimensao.py

Sao dois portoes, porque a regra tem duas pontas e cada ponta falha sozinha:

  - `teste-dimensao-imagem.py` mede o HTML SERVIDO das quatro paginas;
  - `validar-produtos.py` mede o BANCO (V19).

Cada mutacao declara qual dos dois deveria pega-la, e a lista so passa quando o
portao NOMEADO reprova — um defeito de dado pego "por sorte" pelo portao do HTML
nao prova que a regra do banco existe. Isso tambem impede a mutacao inerte de se
disfarcar de sucesso.

A MUTACAO QUE MAIS IMPORTA e a numero 4, e ela e o conserto TENTADOR: quando
falta dimensao, deixar de servir a foto parece rigor e e perda de produto certo.
O mundo em que ela aparece nao existe no banco de hoje — as oito fotos servidas
estao todas medidas —, e por isso o portao o PRODUZ: copia a ilha, apaga a
medida de um registro e roda o gerador.

Cada mutacao roda num repositorio COPIADO.
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VAZAO = 'snippets/aquametria-calculadora-vazao.php'
MIDIA = 'snippets/aquametria-calculadora-midia.php'
FILTROS = 'dados/produtos-filtro.json'

HTML = 'ferramentas/teste-dimensao-imagem.py'
BANCO = 'ferramentas/validar-produtos.py'


def troca(arquivo, velho, novo, vezes=1):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit(f'ALVO SUMIU em {arquivo}: {velho[:70]!r}\n'
                             'Mutacao inerte nao prova nada. Atualize a lista junto com o codigo.')
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


def mexer_no_banco(id_produto, mudanca):
    """Edita UM registro do banco de filtros SEM rodar o gerador.

    E o defeito mais realista desta familia: quem mexe no banco e esquece o
    gerador deixa as duas copias divergindo, e a tela continua servindo o numero
    antigo. Foi assim que o Clube do Mosaico deixou dez links fora do ar em
    12/09/2026 — banco editado, manifest intocado."""
    def aplicar(base: Path):
        caminho = base / FILTROS
        d = json.loads(caminho.read_text(encoding='utf-8'))
        for p in d['produtos']:
            if p.get('id') == id_produto:
                mudanca(p['imagem'])
                break
        else:
            raise SystemExit(f'ALVO SUMIU: nenhum produto {id_produto!r} no banco de filtros')
        caminho.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return aplicar


def regerar(base: Path):
    r = subprocess.run(['python3', str(base / 'ferramentas/gerar-catalogo-filtros.py')],
                       capture_output=True, text=True, cwd=str(base))
    if r.returncode != 0:
        raise SystemExit('o gerador falhou na mutacao: ' + r.stderr[-500:])


def ambas(*aplicadores):
    def aplicar(base):
        for a in aplicadores:
            a(base)
    return aplicar


def sem_medida(img):
    img['largura'] = None
    img['altura'] = None
    img['medida_em'] = None
    img['medida_como'] = None
    img['motivo_sem_medida'] = 'mutacao'


MUTACOES = [
    (
        HTML,
        'o banco e corrigido e NINGUEM roda o gerador: a tela serve o numero velho',
        mexer_no_banco('eheim-classic-250-2213',
                       lambda img: img.update({'largura': 800, 'altura': 800})),
    ),
    (
        HTML,
        'a tela serve dimensao que o banco NAO TEM (o catalogo embutido sobrevive ao banco)',
        # Sem regerar de proposito: o banco passa a dizer "ninguem mediu" e o
        # snippet continua servindo 726x726. E a direcao que a primeira versao
        # deste portao nao tinha, e sem ela um numero plausivel digitado dentro
        # do catalogo passaria para sempre.
        mexer_no_banco('eheim-classic-250-2213', sem_medida),
    ),
    (
        HTML,
        'o renderizador para de emitir o par, e volta ao defeito do despacho de 13/09',
        troca(VAZAO,
              "\t\tif ( ! empty( $p['imagem']['largura'] ) && ! empty( $p['imagem']['altura'] ) ) {",
              "\t\tif ( false ) {"),
    ),
    (
        HTML,
        'O CONSERTO TENTADOR: sem dimensao, o produto perde a foto em vez de sair sem o par',
        ambas(
            mexer_no_banco('eheim-classic-250-2213', sem_medida),
            regerar,
            troca(VAZAO,
                  "\tif ( ! empty( $p['imagem'] ) && ! empty( $p['imagem']['url'] ) ) {",
                  "\tif ( ! empty( $p['imagem'] ) && ! empty( $p['imagem']['url'] )\n\t\t&& ! empty( $p['imagem']['largura'] ) && ! empty( $p['imagem']['altura'] ) ) {"),
        ),
    ),
    (
        HTML,
        'o renderizador serve width sozinho, e da ao navegador uma proporcao errada',
        troca(VAZAO,
              "\t\t\t$img .= ' width=\"' . esc_attr( $p['imagem']['largura'] ) . '\" height=\"' . esc_attr( $p['imagem']['altura'] ) . '\"';",
              "\t\t\t$img .= ' width=\"' . esc_attr( $p['imagem']['largura'] ) . '\"';"),
    ),
    (
        HTML,
        'o CSS deixa de reservar a caixa, e ai a foto sem par passa a saltar o layout',
        troca(VAZAO, 'aspect-ratio:1/1;width:100%;max-width:100%;background:var(--c3-papel)',
              'width:100%;max-width:100%;background:var(--c3-papel)'),
    ),
    (
        HTML,
        'o script passa a atribuir width sem height',
        troca(VAZAO, "\t\t\t\timg.height = p.imagem.altura;", "\t\t\t\t/* mutacao */"),
    ),
    (
        HTML,
        'o script atribui o par SEM exigir os dois campos do catalogo',
        troca(VAZAO, "if (p.imagem.largura && p.imagem.altura) {", "if (p.imagem.largura) {"),
    ),
    (
        HTML,
        'duas fichas usam o MESMO arquivo com dimensoes diferentes',
        mexer_no_banco('eheim-classic-600-2217-127v',
                       lambda img: img.update({
                           'url': 'https://down-bs-br.img.susercontent.com/'
                                  'sg-11134201-7rd58-m7bniamcy29b62.webp',
                           'largura': 512, 'altura': 512})),
    ),
    (
        BANCO,
        'O BURACO DO V19 DE VOLTA: o banco grava largura e esquece altura',
        mexer_no_banco('seachem-tidal-55', lambda img: img.update({'altura': None})),
    ),
    (
        BANCO,
        'o banco grava dimensao sem dizer quando ela foi lida',
        mexer_no_banco('seachem-tidal-55', lambda img: img.update({'medida_em': None})),
    ),
    (
        BANCO,
        'o banco grava dimensao sem dizer como ela foi lida',
        mexer_no_banco('seachem-tidal-55', lambda img: img.update({'medida_como': None})),
    ),
    (
        BANCO,
        'o banco fica com dimensao E com o motivo de nao ter dimensao',
        mexer_no_banco('seachem-tidal-55',
                       lambda img: img.update({'motivo_sem_medida': 'sobrou do tempo sem medida'})),
    ),
    (
        BANCO,
        'a imagem nova chega sem dimensao e sem dizer por que — o silencio que a regra proibe',
        mexer_no_banco('eheim-classic-250-2213',
                       lambda img: img.update({'largura': None, 'altura': None,
                                               'medida_em': None, 'medida_como': None,
                                               'motivo_sem_medida': None})),
    ),
]


def rodar(base: Path, portao: str):
    r = subprocess.run(['python3', str(base / portao), str(base)],
                       capture_output=True, text=True, cwd=str(base))
    return r.returncode, r.stdout + r.stderr


def main():
    for portao in (HTML, BANCO):
        codigo, saida = rodar(RAIZ, portao)
        if codigo != 0:
            print(f'O portao {portao} ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.')
            print(saida[-2000:])
            return 1
        print(f'repositorio limpo: {portao} verde')
    print()

    reprovou = 0
    for i, (portao, nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            shutil.copytree(RAIZ, base, ignore=shutil.ignore_patterns('node_modules', '.git'))
            aplicar(base)
            codigo, saida = rodar(base, portao)
            marca = Path(portao).name
            if codigo != 0:
                reprovou += 1
                print(f'  {i:2d}. REPROVOU (certo, por {marca}) — {nome}')
                for l in [x.strip() for x in saida.splitlines()
                          if x.strip().startswith(('FALHA', 'erro ['))][:2]:
                    print(f'        {l[:150]}')
            else:
                print(f'  {i:2d}. PASSOU (ERRADO, {marca} nao viu) — {nome}')

    print(f'\n{reprovou} de {len(MUTACOES)} mutacoes reprovadas pelo portao que as nomeia')
    return 0 if reprovou == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

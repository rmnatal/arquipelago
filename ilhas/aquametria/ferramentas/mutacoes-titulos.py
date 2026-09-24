#!/usr/bin/env python3
"""Quebra DE PROPOSITO o portao das duas fontes de titulo, uma quebra por vez.

    python3 ferramentas/mutacoes-titulos.py

O portao (`teste-titulos-das-duas-fontes.py`) nasceu em 24/09/2026 e portao
recem-nascido e justamente o que ninguem viu ficar vermelho. A secao 8 do
ARQUIPELAGO.md e feita de cicatrizes dessa familia.

A MUTACAO QUE MAIS IMPORTA AQUI E A 1, porque ela nao apaga nada e nao quebra
pagina nenhuma: ela muda o titulo em UM dos dois arquivos, que e exatamente o
acidente que o portao existe para pegar. O site continua respondendo 200, o
`<h1>` continua certo, e so o `og:title` passa a dizer outra coisa — o tipo de
defeito que nenhuma ronda de HTTP e nenhum olho na tela encontra.

E A 5 E A PORTA DOS FUNDOS DESTE PORTAO EM PARTICULAR: ele le o registro do
snippet em TEXTO, por expressao regular. Se a leitura parar de casar, os dois
dicionarios ficam vazios — e dois dicionarios vazios CONCORDAM. As tres primeiras
afirmacoes do portao existem so para que a 5 fique vermelha, e esta mutacao e a
prova de que elas funcionam.

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
PEIXES = 'snippets/aquametria-peixes.php'
JSON = 'dados/metas-seo.json'
PORTAO = 'ferramentas/teste-titulos-das-duas-fontes.py'


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


def regex(arquivo, padrao, novo, flags=0):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        s2, n = re.subn(padrao, novo, s, count=1, flags=flags)
        if n == 0:
            raise SystemExit(f'ALVO SUMIU (regex) em {arquivo}: {padrao[:70]!r}')
        p.write_text(s2, encoding='utf-8')
    return aplicar


MUTACOES = [
    ('1. o titulo muda SO no metas-seo.json — <h1> certo, og:title errado, '
     'site verde em qualquer medicao de HTTP',
     troca(JSON,
           '"titulo": "Ciclídeos anões: quantos litros para ciclídeo anão"',
           '"titulo": "Ciclídeos anões: quantos litros, do casal ao grupo"')),

    ('2. o titulo muda SO no registro do snippet — o defeito espelhado, e o mais '
     'provavel dos dois, porque quem conserta posicao de busca mexe no <title>',
     troca(PEIXES,
           "'titulo'   => 'Ciclídeos anões: quantos litros para ciclídeo anão',",
           "'titulo'   => 'Ciclídeos anões: quantos litros, do casal ao grupo',")),

    ('3. o titulo estoura o teto de 65 por UM caractere, nas duas fontes juntas — '
     'a divergencia fica verde e o Google corta o titulo',
     lambda base: (
         troca(PEIXES,
               "'titulo'   => 'Ciclídeos anões: quantos litros para ciclídeo anão',",
               "'titulo'   => 'Ciclídeos anões: quantos litros para um ciclídeo anão',")(base),
         troca(JSON,
               '"titulo": "Ciclídeos anões: quantos litros para ciclídeo anão"',
               '"titulo": "Ciclídeos anões: quantos litros para um ciclídeo anão"')(base),
     )),

    ('4. o conserto pela METADE: o titulo ganha o singular e a meta description '
     'fica so no plural — o criterio da Proposta 1 pede as duas nas duas',
     troca(JSON,
           '"meta_descricao": "Quantos litros para ciclídeo anão? Os ciclídeos anões pedem',
           '"meta_descricao": "Os ciclídeos anões pedem')),

    ('5. a PORTA DOS FUNDOS: o registro deixa de ser lido em texto (a entrada abre '
     'com tres tabs em vez de dois) e os dois lados ficam vazios, portanto '
     'concordes',
     regex(PEIXES,
           r"\n\t\t'ciclideos-anoes' => array\(",
           "\n\t\t\t'ciclideos-anoes' => array(")),

    ('6. uma pagina do eixo sai do metas-seo.json — nenhum titulo diverge, e uma '
     'pagina passa a servir og:title nenhum',
     regex(JSON,
           r'\n    "tetras": \{.*?\n    \},',
           '',
           re.S)),
]


def rodar_portao(base: Path):
    r = subprocess.run(['python3', str(base / PORTAO)],
                       capture_output=True, text=True)
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra DE PROPOSITO o portao do casamento da Shopee e exige que ele reprove.

    python3 ferramentas/mutacoes-coleta-shopee.py

O portao e `ferramentas/teste-coleta-shopee.py`; o codigo medido e
`ferramentas/coletar-shopee.py`. Cada mutacao roda num repositorio COPIADO, e a
lista so passa quando TODAS reprovam.

POR QUE MUTACAO E NAO SO TESTE: um teste que so olha titulo bom prova que o
portao deixa passar, nunca que ele barra. E barrar e o trabalho inteiro deste
portao — o dano que ele existe para impedir (a C5 prometer 25 W e abrir o
anuncio de 300 W) so acontece quando ele deixa passar o que deveria recusar.

AS PORTAS DOS FUNDOS ESTAO NOMEADAS. Nao basta apagar a regra: a mutacao 5 a
mantem e desliga a lista de irmaos, que e de onde ela tira a resposta; a 7
mantem o portao do sufixo e corta so os sufixos que vem do banco; a 8 mantem
tudo e troca a fronteira de token por `in`, que e o jeito mais natural de
escrever a mesma coisa errada. Regra que so reprova a versao ingenua do defeito
nao protege ninguem.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
COLETOR = 'ferramentas/coletar-shopee.py'
PORTAO = 'ferramentas/teste-coleta-shopee.py'


def troca(arquivo, velho, novo, vezes=1):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit(
                'ALVO SUMIU em %s: %r\nMutacao inerte nao prova nada. '
                'Atualize a lista junto com o codigo.' % (arquivo, velho[:80]))
        p.write_text(s.replace(velho, novo, vezes), encoding='utf-8')
    return aplicar


MUTACOES = [
    # 1. A MEDIDA DEIXA DE BARRAR O CONFLITO. E o defeito de maior dano do
    #    banco inteiro: o titulo diz 300 W, o registro e de 25 W, e o botao da
    #    C5 abre o aquecedor errado na casa de quem leu.
    ('o conflito de medida deixa de barrar',
     troca(COLETOR,
           "            if medida_conflitante(unidade, valores, titulo):",
           "            if False and medida_conflitante(unidade, valores, titulo):")),

    # 2. A MEDIDA CALADA PASSA A SER ACEITA. Mais sutil que a 1: o anuncio nao
    #    mente, so nao diz qual dos cinco irmaos e — e aceitar isso e escolher
    #    um irmao no sorteio.
    ('a medida ausente deixa de barrar',
     troca(COLETOR,
           "        if medida_discrimina(registro, irmaos):",
           "        if False and medida_discrimina(registro, irmaos):")),

    # 3. A MARCA DEIXA DE SER EXIGIDA no titulo (condicao necessaria da 25.3).
    ('a marca deixa de ser exigida no titulo',
     troca(COLETOR,
           "    if not token_no_titulo(marca, titulo):",
           "    if False and not token_no_titulo(marca, titulo):")),

    # 4. REGISTRO SEM MARCA VOLTA A RECEBER FICHA. Os dois registros sem marca
    #    do banco casariam com qualquer anuncio da categoria.
    ('registro sem marca volta a receber ficha',
     troca(COLETOR, "    if not marca:\n        return False,",
           "    if False:\n        return False,")),

    # 5. PORTA DOS FUNDOS DA 2: a regra da medida fica de pe e a LISTA DE
    #    IRMAOS chega vazia. O portao continua escrito e passa a responder
    #    "nao discrimina" para todo mundo — que e o mesmo estrago com o codigo
    #    intacto, e e como uma refatoracao distraida o causaria.
    ('a lista de irmaos chega vazia e os portoes que leem o banco se desligam',
     troca(COLETOR, "                    ok, motivo = casa(o, r, irmaos)",
           "                    ok, motivo = casa(o, r, ())")),

    # 6. O SUFIXO DEIXA DE FAZER OUTRO APARELHO. Quem paga e a Chihiros WRGB
    #    II 90, que casaria com a Pro 90 e com a Slim 90 — as tres de 90 cm.
    ('o sufixo de variante deixa de barrar',
     troca(COLETOR, "        if variante_depois_do_codigo(base, titulo, extras):",
           "        if False and variante_depois_do_codigo(base, titulo, extras):")),

    # 7. PORTA DOS FUNDOS DO SUFIXO: a funcao fica de pe e os sufixos do BANCO
    #     param de chegar. Sobra a lista estatica, que nao conhece "slim" — e a
    #     WRGB II Slim 90 volta a casar com a WRGB II 90.
    ('os sufixos vindos do banco param de chegar ao portao',
     troca(COLETOR, "        extras = sufixos_irmaos(registro, irmaos)",
           "        extras = ()")),

    # 8. PORTA DOS FUNDOS DO CODIGO: a fronteira de token vira `in`, que e
    #    como qualquer pessoa escreveria a mesma intencao. Com `in`, "HW-303"
    #    esta dentro de "HW-303B" e o filtro vizinho passa.
    ('a fronteira de token vira substring',
     troca(COLETOR,
           "    return re.search(r'(?<![a-z0-9])%s(?![a-z0-9+])' % padrao,\n"
           "                     sem_acento(titulo)) is not None",
           "    return re.search(padrao, sem_acento(titulo)) is not None")),

    # 9. A PECA VOLTA A PASSAR POR APARELHO (armadilha 1 da 25.7).
    ('a peca do aparelho volta a passar por aparelho',
     troca(COLETOR, "    if e_peca_e_nao_aparelho(titulo, entidade):",
           "    if False and e_peca_e_nao_aparelho(titulo, entidade):")),

    # 10. O KIT VOLTA A PASSAR (armadilha 2 da 25.7).
    ('o kit indevido volta a passar',
     troca(COLETOR, "    if kit_indevido(titulo, registro):",
           "    if False and kit_indevido(titulo, registro):")),

    # 11. PORTA DOS FUNDOS DO CODIGO BASE: ele volta a comer TODO numero final,
    #     que foi a primeira versao que escrevi. Come o `2213` do Eheim classic,
    #     que e o codigo do filtro e nao o tamanho dele.
    ('o codigo base volta a comer todo numero final',
     troca(COLETOR,
           "            if any(abs(n - v) <= max(0.01 * v, 0.001) for v in valores):\n"
           "                continue",
           "            continue")),

    # 12. PORTA DOS FUNDOS DA MARCA: a `linha` volta a valer como identidade
    #     alternativa. "HW" esta no titulo do HW-303, do HW-603B e do HW-702A.
    ('a linha volta a valer como codigo',
     troca(COLETOR, "    base = codigo_base(registro) or linha",
           "    base = linha or codigo_base(registro)")),
]


# A COPIA TEM DE REPRODUZIR O LAYOUT DO REPOSITORIO, E ISSO NAO E DETALHE.
# `coletar-shopee.py` carrega `../../ferramentas/shopee-api.py`, que mora na
# RAIZ do repositorio e nao na ilha. Na primeira versao deste arquivo a copia
# ia para `<tmp>/ilha`, e dali o caminho relativo apontava para
# `/tmp/ferramentas/shopee-api.py`, que nao existe: o portao morria com
# FileNotFoundError ANTES de medir qualquer coisa, e o `returncode != 0` era
# lido como "mutacao reprovada". **As onze passaram verdes sem que uma unica
# regra tivesse sido exercida** — a lista inteira era inerte, que e o defeito
# que este arquivo existe para impedir nos outros. Pego pelo controle positivo
# ter rodado na arvore real enquanto as mutacoes rodavam na copia quebrada.
def preparar(tmp: str) -> Path:
    """Monta `<tmp>/repo/ilhas/aquametria` + `<tmp>/repo/ferramentas`."""
    repo = Path(tmp) / 'repo'
    ilha = repo / 'ilhas' / 'aquametria'
    ilha.parent.mkdir(parents=True)
    shutil.copytree(RAIZ, ilha, symlinks=True)
    shutil.copytree(RAIZ.parent.parent / 'ferramentas', repo / 'ferramentas',
                    symlinks=True)
    return ilha


def rodar(base: Path):
    return subprocess.run(['python3', str(base / PORTAO)],
                          capture_output=True, text=True, cwd=str(base))


def main():
    # CONTROLE POSITIVO: sem mutacao nenhuma o portao tem de APROVAR. Sem isto,
    # um portao quebrado reprovaria as onze e a lista sairia verde mentindo.
    limpo = rodar(RAIZ)
    if limpo.returncode != 0:
        print('CONTROLE NEGATIVO FALHOU: o portao ja reprova o codigo intacto.')
        print(limpo.stdout[-1500:])
        return 1
    print('controle: o portao aprova o codigo intacto (%s)'
          % limpo.stdout.strip().splitlines()[-1])

    sobreviventes = []
    for i, (nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            copia = preparar(tmp)
            # A COPIA TEM DE APROVAR ANTES DE SER MUTADA. Sem esta conferencia
            # uma copia quebrada devolve `returncode != 0` para tudo e a lista
            # inteira sai verde sem medir nada — que foi exatamente o que
            # aconteceu aqui em 23/09/2026.
            antes = rodar(copia)
            if antes.returncode != 0:
                print('  %2d. COPIA QUEBRADA (a mutacao nao chegou a ser medida)' % i)
                print((antes.stderr or antes.stdout)[-600:])
                sobreviventes.append((i, nome + ' [copia quebrada]'))
                continue
            aplicar(copia)
            r = rodar(copia)
            if r.returncode == 0:
                sobreviventes.append((i, nome))
                print('  %2d. SOBREVIVEU  %s' % (i, nome))
            else:
                print('  %2d. reprovada   %s' % (i, nome))

    print('\n%d mutacoes, %d reprovadas, %d sobreviventes'
          % (len(MUTACOES), len(MUTACOES) - len(sobreviventes), len(sobreviventes)))
    if sobreviventes:
        print('\nMUTACAO QUE SOBREVIVE E REGRA QUE NAO EXISTE:')
        for i, nome in sobreviventes:
            print('  %d. %s' % (i, nome))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

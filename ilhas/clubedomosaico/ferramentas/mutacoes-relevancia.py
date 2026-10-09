#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DA REGRA DE RELEVANCIA — 09/10/2026.

    python3 ferramentas/mutacoes-relevancia.py

Cada mutacao estraga uma trava de `ferramentas/relevancia-do-anuncio.py` (ou da
leitura de quantidade de `coletar-por-consulta.py`) e roda
`ferramentas/teste-relevancia.py` em cima da arvore mutada. **Toda mutacao tem
de REPROVAR.** Mutacao que passa e uma trava que a bancada nao mede — e trava
que ninguem mede e trava que nao existe, por mais bem escrita que esteja no
cabecalho.

ESTA BATERIA TRABALHA EM `mkdtemp`, E ISSO NAO E DETALHE DE ARRUMACAO. O aviso
no topo do `PROMPT.md` desta ilha e de hoje: a `mutacoes-par.py` foi morta por
sinal no meio de uma passada e deixou `snippets/clubedomosaico-f2.php` MUTADO no
repositorio, com a regra 8 devolvendo a causa errada — e quem nomeou o arquivo
foi o `git status`, nao a bancada. Bateria que copia a ilha para um diretorio
temporario nao tem como sujar nada, nem morta por SIGKILL, que nao se captura.

POR QUE ESTA REGRA MERECE BATERIA: ela decide o que entra na vitrine de uma
pagina que promete ao visitante *o que comprar*. Quando ela erra nao aparece
tela vermelha nenhuma — aparece uma lista de anuncios plausiveis, com preco e
foto, do produto ERRADO. O ensaio de 09/10 mediu os dois erros ao mesmo tempo na
mesma consulta: os CINCO kits de pastilha de verdade recusados e DUAS ofertas de
obra e de adesivo aceitas, tudo por causa de um `s` de plural. **Dessas duas, a
que custa mais caro e a segunda, e nenhum portao desta ilha a veria.**

AS MUTACOES QUE ANDAM PARA O OUTRO LADO, de proposito (m08 e m09): elas APERTAM
a regra em vez de afrouxar. Uma regua que recusa o certo custa tanto quanto uma
que aceita o errado — e so uma bancada com os dois lados pega as duas. A m08 e
a prova de que o corte de plural precisa valer nas DUAS pontas da comparacao, e
nao so no titulo.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ILHA = RAIZ
REGRA = os.path.join('ferramentas', 'relevancia-do-anuncio.py')
COLETA = os.path.join('ferramentas', 'coletar-por-consulta.py')
BANCADA = os.path.join('ferramentas', 'teste-relevancia.py')


def _troca(copia, arquivo, antigo, novo):
    caminho = os.path.join(copia, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if antigo not in texto:
        raise SystemExit('mutacao invalida: o alvo nao existe mais em %s\n  %r'
                         % (arquivo, antigo[:70]))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antigo, novo, 1))


def m01(c):
    """a recusa para de vencer: ela deixa de ser medida antes da exigencia"""
    _troca(c, REGRA,
           "    for termo in (declaracao.get('recusa') or []):",
           "    for termo in []:")


def m02(c):
    """o corte de plural cai: `pastilha` volta a nao casar com `Pastilhas`"""
    _troca(c, REGRA,
           "    if len(p) >= 5 and p.endswith('s'):\n        p = p[:-1]",
           "    if False:\n        p = p[:-1]")


def m03(c):
    """a exigencia passa a bastar UM grupo, em vez de todos"""
    _troca(c, REGRA,
           "        if casou is None:",
           "        if False:")


def m04(c):
    """a falha fechada abre: declaracao sem exigencia passa a aceitar o mundo"""
    _troca(c, REGRA,
           "    if not atendidas:",
           "    if False:")


def m05(c):
    """grupo de exigencia VAZIO passa a ser ignorado em vez de recusar"""
    _troca(c, REGRA,
           "        if not termos:",
           "        if False:")


def m06(c):
    """a palavra inteira cai: o termo volta a casar pedaco de palavra"""
    _troca(c, REGRA,
           "    return (' %s ' % alvo) in titulo_comparavel",
           "    return alvo in titulo_comparavel")


def m07(c):
    """o motivo da recusa deixa de ser o termo que a causou"""
    _troca(c, REGRA,
           "                'recusado_por': termo,",
           "                'recusado_por': 'recusado',")


def m08(c):
    """APERTA: o plural e cortado so no titulo, nunca no termo declarado

    E a mutacao mais sutil da bateria, e a que prova por que `palavra()` tem de
    rodar nos DOIS lados. Com o corte so no titulo, `recusa: adesivos` para de
    casar com `Adesivos` — o termo fica com o `s` e o titulo perde o dele.
    """
    _troca(c, REGRA,
           "    alvo = ' '.join(\n        palavra(p) for p in re.split",
           "    alvo = ' '.join(\n        p for p in re.split")


def m09(c):
    """APERTA: a ambiguidade de quantidade passa a escolher em vez de recusar

    `Kit 5 Plaquinhas ... 245pcs` tem duas leituras defensaveis, e escolher a
    primeira da lista erra o preco por peca por um fator de 49.
    """
    _troca(c, COLETA,
           "    if len(distintos) > 1:",
           "    if False:")


def m10(c):
    """a quantidade passa a ser estimada quando o titulo nao a declara"""
    _troca(c, COLETA,
           "    if not achados:\n        return None, 'o titulo nao declara quantidade de pecas'",
           "    if not achados:\n        return 1, 'estimada'")


MUTACOES = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10]


def main():
    passaram = []
    for mutar in MUTACOES:
        nome = '%s — %s' % (mutar.__name__, (mutar.__doc__ or '').strip().splitlines()[0])
        tmp = tempfile.mkdtemp(prefix='mut-rel-')
        copia = os.path.join(tmp, 'ilha')
        try:
            shutil.copytree(ILHA, copia)
            mutar(copia)
            r = subprocess.run([sys.executable, os.path.join(copia, BANCADA)],
                               capture_output=True, text=True)
            if r.returncode == 0:
                passaram.append(nome)
                print('  PASSOU (a trava NAO viu): %s' % nome)
            else:
                primeiro = next((l.strip()[8:] for l in r.stdout.splitlines()
                                 if l.strip().startswith('DEFEITO')), '')
                print('  reprovou como devia: %-62s | %s' % (nome[:62], primeiro[:70]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print('\n%d mutacoes, %d reprovadas, %d passaram'
          % (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print('\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:')
        for nome in passaram:
            print('  - %s' % nome)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

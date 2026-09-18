#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troca a escova de propósito e exige REPROVACAO.

    python3 ferramentas/mutacoes-qual-escova.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

A trava nasceu em 18/09/2026, na segunda passada de fotos, e nasceu de um
casamento errado que NENHUMA regua desta ilha pegou — pegou o olho, pela 25.3.
O registro `positivo-11206519` e a escova PRINCIPAL (o rolo). Ele casou com
*"Escova E Filtro Hepa Para Robo Aspirador Positivo Pra800"*: o codigo PRA800
esta no titulo e `escova` esta na cabeca dele, entao as duas metades da regra
antiga passavam. **A foto do anuncio, aberta com os olhos, traz um filtro e uma
escova LATERAL de tres bracos — nenhum rolo.**

A CAUSA, e ela estava escrita como verdade ha dois dias
--------------------------------------------------------
`palavras_estritas_do_tipo` nasceu em 16/09/2026 dentro de
`medir-palavras-chave.py`, com este comentario: o substantivo pelado basta
*"para a coleta: la o codigo do registro ou do modelo ja amarrou o anuncio, e
`escova` so confirma que o objeto e uma escova"*.

A frase junta dois casos que sao opostos. Quando quem amarra e o codigo da
PECA, ele identifica a peca e `escova` de fato so confirma. Quando quem amarra
e o codigo do MODELO, o anuncio esta preso ao APARELHO — e o aparelho tem
escova lateral E escova principal, as duas no banco, as duas compativeis com o
mesmo modelo. Ali `escova` nao confirma nada: escolhe por sorteio.

E a mesma familia da regra dos dois registros no mesmo anuncio, que esta ilha ja
tinha: **casamento que nao identifica UM registro nao identifica nenhum.** A
diferenca e onde mora a ambiguidade — la no anuncio, aqui na palavra.

O QUE AS SETE MUTACOES GUARDAM
------------------------------
As quatro primeiras sao o defeito e as suas vizinhas; a quinta e a sexta provam
que a trava distingue as duas escovas em vez de barrar as duas; a setima prova
que a aparagem NAO morde tipo de uma palavra so — se mordesse, `filtro` ficaria
sem nenhuma palavra e toda peca de tipo simples perderia a foto, que e uma
trava reprovando o mundo sadio.

O MUNDO SADIO TEM DE PASSAR, e ele e a mutacao 1: o titulo que diz QUAL escova
continua casando, e foi ele que entrou no banco nesta mesma passada.
"""

import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _modulo(caminho, nome):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


COLETA = _modulo(os.path.join(RAIZ, 'ferramentas', 'coletar-shopee.py'),
                 'coletar_shopee')


def banco(rel):
    with open(os.path.join(RAIZ, rel), encoding='utf-8') as fh:
        return json.load(fh)


PECAS = {r['id']: r for r in banco('dados/pecas.json')['registros']}
MODELOS = {r['id']: r for r in banco('dados/modelos-robo.json')['registros']}

# OS REGISTROS SAO OS DE VERDADE, NAO INVENTADOS. Mutacao que constroi o proprio
# mundo prova o que o autor imaginou; esta le o banco commitado, entao o dia em
# que a escova lateral da Positivo sair do banco esta bancada reclama — e e isso
# que se quer, porque nesse dia a ambiguidade tambem muda.
ESCOVA_PRINCIPAL = 'positivo-11206519'   # o rolo
ESCOVA_LATERAL = 'positivo-11206518'     # a de tres bracos
FILTRO = 'multi-pr10205'                 # tipo de UMA palavra

# (nome, id do registro, titulo do anuncio, casa?)
MUTACOES = [
    ('MUNDO SADIO — o titulo diz QUAL escova, e ela e esta',
     'wap-escova-central-wsmart',
     'Escova Central Aspirador Robô Wap Robot WSMART Original', True),

    ('O DEFEITO MEDIDO EM 18/09 — "Escova" pelada com o codigo do MODELO',
     ESCOVA_PRINCIPAL,
     'Escova E Filtro Hepa Para Robô Aspirador Positivo Pra800', False),

    ('A IRMA CAI PELO MESMO MOTIVO — a palavra pelada nao escolhe entre as duas',
     ESCOVA_LATERAL,
     'Escova E Filtro Hepa Para Robô Aspirador Positivo Pra800', False),

    ('O CODIGO DA PECA CONTINUA MANDANDO — ele identifica sozinho, sem o tipo',
     ESCOVA_PRINCIPAL,
     'Escova 11206519 Para Robô Aspirador Positivo Pra800', True),

    ('O QUALIFICADOR CERTO PASSA — "Lateral" e a lateral',
     ESCOVA_LATERAL,
     'Escova Lateral Para Robô Aspirador Positivo Pra800', True),

    ('O QUALIFICADOR ERRADO REPROVA — "Lateral" nao e o rolo',
     ESCOVA_PRINCIPAL,
     'Escova Lateral Para Robô Aspirador Positivo Pra800', False),

    ('TIPO DE UMA PALAVRA NAO E APARADO — senao `filtro` fica sem palavra nenhuma',
     FILTRO,
     'Filtro Para Robô Aspirador Multilaser Ho041', True),
]


def main():
    falhas = 0
    for nome, ident, titulo, esperado in MUTACOES:
        peca = PECAS.get(ident)
        if not peca:
            sys.stderr.write('!! %s: registro %s nao esta no banco\n' % (nome, ident))
            falhas += 1
            continue
        porque = COLETA.casa_peca({'titulo': titulo}, peca, MODELOS)
        casou = porque is not None
        ok = (casou == esperado)
        falhas += 0 if ok else 1
        sys.stdout.write('%s  %s\n' % ('  ok  ' if ok else '  FALHA', nome))
        sys.stdout.write('        %-24s tipo %-18s casou=%s esperado=%s%s\n'
                         % (ident, peca.get('tipo'), casou, esperado,
                            ('  (%s)' % porque) if porque else ''))

    total = len(MUTACOES)
    sys.stdout.write('\n%d de %d no resultado esperado\n' % (total - falhas, total))
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())

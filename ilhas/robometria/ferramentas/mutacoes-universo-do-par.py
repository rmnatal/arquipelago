#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito do item 2 do despacho da Sentinela de 16/09/2026 e
exige REPROVACAO.

    python3 ferramentas/mutacoes-universo-do-par.py

O DEFEITO, medido no ar as 14h50Z de 16/09/2026. A R1 servia, na MESMA frase:

    "Hoje sao 71 pares peca x modelo declarados, em 5 marcas, cobrindo 30 dos 38
     modelos do banco."

Os dois numeros estao certos e saem de universos diferentes. O 71 conta um par
para `multi-ho401`, que tem `status: nao_publicavel`; os 38 o excluem. Esse par
nao esta no seletor, nao tem celula na tabela e nenhum leitor chega nele — a
promessa anunciava uma cobertura que a ferramenta nao entrega, e o erro era de
UM, que e o tamanho em que ninguem olha.

E a mesma familia dos dois 63 que o item 2 do despacho de 14/09 desmontou, um
nivel adiante: la eram dois numeros certos com o MESMO nome, aqui e um numero
certo no universo errado. A regua criada naquele dia recomputava as quatro contas
e nunca perguntava DE QUE UNIVERSO cada uma sai — por isso ela aprovou o 71
durante dois dias.

O "PRONTO QUANDO" DO DESPACHO EXIGE ESTE ARQUIVO, com todas as letras: *"a regua
tem de reprovar o mundo de hoje antes de aprovar o de amanha"*. Sem ele, a unica
prova de que a trava nova funciona seria ela estar verde num banco ja consertado
— que e o mesmo que nao ter prova.

AS TRES MUTACOES:

  1. o gerador volta a ler a contagem do banco inteiro (o defeito original);
  2. o numero publicado volta a ser 71, direto no arquivo de dados;
  3. o resumo mente no numero de pares que ficam de fora.

A (1) e a que importa: ela quebra o GERADOR, e a trava so pega porque o
`teste-r1.php` reconta os dois universos por conta propria, sem ler `contagem`.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GERADOR = 'ferramentas/gerar-r1.py'
TESTE = 'ferramentas/teste-r1.php'
RESPOSTAS = 'dados/r1-respostas.json'

CERTO = '"pares_declarados": _pares_entre_publicaveis(),'
DEFEITO = ('"pares_declarados": ref.doc_pecas["contagem"].get('
           '"pares_peca_x_modelo_declarados"),')


def _regerar(base):
    saida = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-r1.py falhou depois da mutacao: %s'
                             % saida.stderr[-300:])


def _ler(base):
    with open(os.path.join(base, RESPOSTAS), encoding='utf-8') as f:
        return json.load(f)


def _gravar(base, d):
    with open(os.path.join(base, RESPOSTAS), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _exigir_divergencia(base):
    """A bateria so mede alguma coisa se existir par para modelo nao publicavel.

    Sem ele os dois universos dao o mesmo numero e TODA mutacao daqui fica
    inerte — a morte por melhora que a `mutacoes-par-sem-modelo.py` ja pagou
    uma vez nesta ilha, em 16/09/2026, e que esta escrita la em prosa longa.
    Aqui a bateria PARA e diz, em vez de imprimir verde.
    """
    d = _ler(base)
    fora = d['resumo'].get('pares_para_modelo_nao_publicavel')
    if not fora:
        raise AssertionError(
            'nenhum par aponta para modelo nao publicavel hoje: as mutacoes deste '
            'arquivo seriam inertes. Quando isso for verdade de propria vontade — e '
            'sera, no dia em que o multi-ho401 entrar no banco ou sair dele —, PLANTE '
            'o par aqui, como a mutacoes-par-sem-modelo.py passou a plantar o null.')


def m1_gerador_volta_ao_banco_inteiro(base):
    caminho = os.path.join(base, GERADOR)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(CERTO) != 1:
        raise AssertionError('esperava 1 ocorrencia da linha certa em %s, achei %d'
                             % (GERADOR, texto.count(CERTO)))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(CERTO, DEFEITO))
    _regerar(base)


def m2_numero_publicado_volta_a_71(base):
    d = _ler(base)
    r = d['resumo']
    r['pares_declarados'] = r['pares_declarados_no_banco']
    _gravar(base, d)


def m3_resumo_mente_nos_que_ficam_de_fora(base):
    d = _ler(base)
    d['resumo']['pares_para_modelo_nao_publicavel'] = 0
    _gravar(base, d)


MUTACOES = [
    ('o gerador volta a ler a contagem do banco inteiro',
     'o numero da promessa passa a contar par que o seletor nao oferece',
     m1_gerador_volta_ao_banco_inteiro),
    ('o numero publicado volta a ser o do banco inteiro',
     'a frase serve 71 ao lado de "30 dos 38" — dois universos, uma frase',
     m2_numero_publicado_volta_a_71),
    ('o resumo jura que nenhum par fica de fora',
     'divida contada em zero e divida que ninguem paga',
     m3_resumo_mente_nos_que_ficam_de_fora),
]


def main():
    _exigir_divergencia(RAIZ)
    print('Robometria — o universo do par (despacho da Sentinela de 16/09, item 2)\n')
    reprovadas = 0
    for titulo, porque, mutar in MUTACOES:
        base = tempfile.mkdtemp(prefix='rbm-universo-')
        alvo = os.path.join(base, 'ilha')
        shutil.copytree(RAIZ, alvo)
        try:
            mutar(alvo)
        except AssertionError as e:
            print('  INERTE %-58s %s' % (titulo[:58], e))
            shutil.rmtree(base, ignore_errors=True)
            continue
        saida = subprocess.run(['php', os.path.join(alvo, TESTE), alvo],
                               capture_output=True, text=True, cwd=alvo)
        falhou = saida.returncode != 0
        marca = 'ok    ' if falhou else 'PASSOU'
        quantas = saida.stdout.count('  FALHA')
        print('  %s %-58s %s' % (marca, titulo[:58],
                                 ('%d falha(s) em %s' % (quantas, TESTE)) if falhou
                                 else 'a trava NAO pegou'))
        if not falhou:
            print('         %s' % porque)
        reprovadas += 1 if falhou else 0
        shutil.rmtree(base, ignore_errors=True)

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    return 0 if reprovadas == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

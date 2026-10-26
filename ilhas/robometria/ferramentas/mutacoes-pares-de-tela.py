#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito do item 1 do despacho da Sentinela de 02/10/2026
e exige REPROVACAO.

    python3 ferramentas/mutacoes-pares-de-tela.py

O DEFEITO, medido no ar em 02/10/2026 as 14h51Z e remedido em 16/10 e em 23/10 —
24 dias aberto. A ilha publicava DOIS numeros para a mesma frase:

    /sobre/                                  "91 pares peca x modelo"
    /qual-peca-serve-no-meu-robo-aspirador/  "91 pares peca x modelo"
    /pecas/                                  "91 pares peca x modelo"
    /filtro-universal-de-robo-aspirador/     "92 pares peca x modelo"

Os dois estavam certos sob definicoes diferentes — 91 e o par com as DUAS pontas
publicaveis, 92 e o par declarado contado do lado da peca — e NENHUMA das quatro
paginas dizia qual delas estava dizendo. A diferenca e de UM par,
`multi-pr10124` x `multi-ho401`, que e o tamanho em que ninguem olha.

POR QUE ESTA BATERIA EXISTE. O conserto de 26/10 tem duas metades: o numero da
tela passa a ser sempre o das duas pontas, com a definicao escrita na frase, e
`ferramentas/validar-pares.py` passa a ser o unico lugar onde as copias se
encontram. A segunda metade e uma trava NOVA num banco JA CONSERTADO — e trava
verde em banco consertado nao e prova de nada. Aqui o mundo de 02/10 e escrito
de volta, uma mutacao por vez, e a trava tem de morder em todas.

AS MUTACOES, e cada uma e um jeito real pelo qual o defeito volta:

  1. o derivado do A1 volta a publicar o numero do lado da peca (o defeito tal
     e qual ele estava no ar);
  2. o GERADOR do A1 volta a somar codigos_declarados (a causa, e nao o
     sintoma: a mutacao regera o arquivo);
  3. a casca discorda do A1 em um par (o jeito pelo qual os dois nasceram);
  4. o banco mente na contagem das duas pontas;
  5. a lista que NOMEIA os pares sem destino e esvaziada (a conta fecha e a
     divida desaparece);
  6. a R1 jura que nenhum par fica de fora (a conta deixa de fechar);
  7. a constante da definicao sai da casca (o numero volta a ser servido sem
     dizer qual conta ele e);
  8. uma pagina para de ler a constante (tres dizem a definicao e uma nao);
  9. uma copia NOVA nasce calada num dados/*.json (foi assim que o 92 viveu);
 10. e, contra o teste-a1.php: a pagina serve o numero certo e emudece sobre o
     par que fica de fora.
"""

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORTAO = 'ferramentas/validar-pares.py'
TESTE_A1 = 'ferramentas/teste-a1.php'

GERADOR_A1 = 'ferramentas/gerar-a1.py'
CERTO_A1 = '    pares = _pares_entre_publicaveis()'
DEFEITO_A1 = '    pares = sum(l["codigos_declarados"] for l in alcance)'


def _ler(base, nome):
    with io.open(os.path.join(base, 'dados', nome), encoding='utf-8') as f:
        return json.load(f)


def _gravar(base, nome, d):
    with io.open(os.path.join(base, 'dados', nome), 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')


def _exigir_divergencia():
    """Sem par sem destino, metade destas mutacoes seria inerte.

    Quando os dois universos derem o mesmo numero — e darao, no dia em que o
    multi-ho401 entrar no banco como publicavel ou sair dele —, mutacao que
    troca um pelo outro nao muda nada e imprime verde sem medir. A bateria PARA
    e diz, em vez de aprovar. E a morte por melhora que a
    `mutacoes-par-sem-modelo.py` desta mesma ilha ja pagou uma vez.
    """
    c = _ler(RAIZ, 'pecas.json')['contagem']
    if not c.get('pares_para_modelo_nao_publicavel'):
        raise SystemExit(
            'PARADA: nenhum par aponta para modelo nao publicavel hoje, entao as '
            'mutacoes 1, 3, 4, 5, 6 e 10 seriam inertes. PLANTE o par aqui antes '
            'de confiar nesta bateria.')


def m1_a1_volta_ao_lado_da_peca(base):
    d = _ler(base, 'a1-fatos.json')
    d['resumo']['pares_declarados'] = d['resumo']['pares_declarados_no_banco']
    _gravar(base, 'a1-fatos.json', d)


def m2_gerador_do_a1_volta_a_somar_codigos(base):
    caminho = os.path.join(base, GERADOR_A1)
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(CERTO_A1) != 1:
        raise AssertionError('esperava 1 ocorrencia de %r em %s, achei %d'
                             % (CERTO_A1, GERADOR_A1, texto.count(CERTO_A1)))
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(CERTO_A1, DEFEITO_A1))
    saida = subprocess.run(['python3', os.path.join(base, GERADOR_A1), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-a1.py falhou depois da mutacao: %s'
                             % saida.stderr[-300:])


def m3_casca_discorda_do_a1(base):
    d = _ler(base, 'casca-fatos.json')
    d['medicao']['pares_declarados'] += 1
    _gravar(base, 'casca-fatos.json', d)


def m4_banco_mente_nas_duas_pontas(base):
    d = _ler(base, 'pecas.json')
    d['contagem']['pares_peca_x_modelo_publicaveis_nas_duas_pontas'] = (
        d['contagem']['pares_peca_x_modelo_declarados'])
    _gravar(base, 'pecas.json', d)


def m5_lista_dos_sem_destino_e_esvaziada(base):
    d = _ler(base, 'pecas.json')
    d['contagem']['pares_para_modelo_nao_publicavel_quais'] = []
    _gravar(base, 'pecas.json', d)


def m6_r1_jura_que_nenhum_fica_de_fora(base):
    d = _ler(base, 'r1-respostas.json')
    d['resumo']['pares_para_modelo_nao_publicavel'] = 0
    _gravar(base, 'r1-respostas.json', d)


def m7_constante_da_definicao_sai_da_casca(base):
    caminho = os.path.join(base, 'snippets/robometria-casca.php')
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    alvo = "\tdefine( 'ROBOMETRIA_PARES_DEFINICAO', 'contando só os pares em que a peça e o modelo estão os dois publicados aqui' );"
    if alvo not in texto:
        raise AssertionError('nao achei a constante da definicao na casca')
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(
            alvo,
            "\tdefine( 'ROBOMETRIA_PARES_DEFINICAO', 'pares peça × modelo' );"))


def m8_uma_pagina_para_de_ler_a_constante(base):
    caminho = os.path.join(base, 'snippets/robometria-malha.php')
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    alvo = "'declarados pelo fabricante, ' . ROBOMETRIA_PARES_DEFINICAO . '.',"
    if alvo not in texto:
        raise AssertionError('nao achei a leitura da constante na malha')
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(alvo, "'declarados pelo fabricante.',"))


def m9_copia_nova_nasce_calada(base):
    caminho = os.path.join(base, 'dados', 'cobertura-r1.json')
    with io.open(caminho, encoding='utf-8') as f:
        d = json.load(f)
    d['pares_peca_x_modelo_de_hoje'] = 92
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')


def m10_pagina_emudece_sobre_o_par_de_fora(base):
    """Esta mutacao e contra o teste-a1.php, nao contra o validar-pares.py.

    O numero da tela fica CERTO e o paragrafo que nomeia o par sem destino sai.
    E o conserto pela metade mais provavel de todos: trocar 92 por 91 e nao
    dizer por que o numero caiu."""
    caminho = os.path.join(base, 'snippets/robometria-a1.php')
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    alvo = "\tif ( $fora > 0 ) {"
    if alvo not in texto:
        raise AssertionError('nao achei o bloco do par sem destino no A1')
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(alvo, "\tif ( false ) {", 1))


MUTACOES = [
    ('o derivado do A1 volta a publicar o numero do lado da peca',
     'e o defeito tal e qual estava no ar: 92 numa pagina, 91 nas outras tres',
     m1_a1_volta_ao_lado_da_peca, PORTAO),
    ('o GERADOR do A1 volta a somar codigos_declarados',
     'a causa e nao o sintoma — o arquivo e regerado com o defeito dentro',
     m2_gerador_do_a1_volta_a_somar_codigos, PORTAO),
    ('a casca discorda do A1 em um par',
     'e o jeito pelo qual os dois numeros nasceram: duas contas sem testemunha',
     m3_casca_discorda_do_a1, PORTAO),
    ('o banco mente na contagem das duas pontas',
     'cabecalho de banco e numero de tela: contado, nunca digitado',
     m4_banco_mente_nas_duas_pontas, PORTAO),
    ('a lista que NOMEIA os pares sem destino e esvaziada',
     'a conta fecha e a divida desaparece: foi assim que o par ficou invisivel',
     m5_lista_dos_sem_destino_e_esvaziada, PORTAO),
    ('a R1 jura que nenhum par fica de fora',
     'divida contada em zero e divida que ninguem paga',
     m6_r1_jura_que_nenhum_fica_de_fora, PORTAO),
    ('a constante da definicao sai da casca',
     'o numero volta a ser servido sem dizer qual das duas contas ele e',
     m7_constante_da_definicao_sai_da_casca, PORTAO),
    ('uma pagina para de ler a constante da definicao',
     'tres paginas dizem a definicao e uma nao: o defeito de 02/10 num andar acima',
     m8_uma_pagina_para_de_ler_a_constante, PORTAO),
    ('uma copia NOVA nasce calada num dados/*.json',
     'copia que nenhuma lista conhece e exatamente como o 92 viveu 24 dias',
     m9_copia_nova_nasce_calada, PORTAO),
    ('a pagina serve o numero certo e emudece sobre o par de fora',
     'o conserto pela metade: o numero cai de 92 para 91 e o leitor nao sabe por que',
     m10_pagina_emudece_sobre_o_par_de_fora, TESTE_A1),
]


def main():
    _exigir_divergencia()
    print('Robometria — as copias do par peca x modelo (despacho de 02/10, item 1)\n')
    reprovadas = 0
    for titulo, porque, mutar, portao in MUTACOES:
        base = tempfile.mkdtemp(prefix='rbm-pares-')
        alvo = os.path.join(base, 'ilha')
        shutil.copytree(RAIZ, alvo)
        try:
            mutar(alvo)
        except AssertionError as e:
            print('  INERTE %-56s %s' % (titulo[:56], e))
            shutil.rmtree(base, ignore_errors=True)
            continue
        if portao.endswith('.php'):
            cmd = ['php', os.path.join(alvo, portao), alvo]
        else:
            cmd = ['python3', os.path.join(alvo, portao)]
        saida = subprocess.run(cmd, capture_output=True, text=True, cwd=alvo)
        falhou = saida.returncode != 0
        quantas = saida.stdout.count('  FALHA')
        print('  %s %-56s %s' % ('ok    ' if falhou else 'PASSOU', titulo[:56],
                                 ('%d falha(s) em %s' % (quantas, os.path.basename(portao)))
                                 if falhou else 'a trava NAO pegou'))
        if not falhou:
            print('         %s' % porque)
        reprovadas += 1 if falhou else 0
        shutil.rmtree(base, ignore_errors=True)

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    return 0 if reprovadas == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())

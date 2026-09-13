#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito do PISO DIGITADO da varredura e exige REPROVACAO.

    python3 ferramentas/mutacoes-varredura-por-modelo.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, achado em 13/09/2026 na leva WAP. O `teste-acentuacao.php` e o portao
que garante que a ilha nao serve portugues sem acento, e ele mede o CORPO de todo
estado de pagina — inclusive um estado de R1 por modelo, porque palavra vinda do
banco so aparece quando alguem escolhe aquele modelo. Duas afirmacoes seguravam
essa cobertura, e as duas traziam o numero DIGITADO:

    rbm_ok( count( $estados ) >= 70, 'a varredura monta 70 estados ou mais', ... );
    rbm_ok( $com_r1 >= 28, 'a R1 e medida em pelo menos 28 estados — um por modelo
            do banco', ... );

Os dois numeros eram exatos no dia em que foram escritos. A leva WAP levou o banco
de 28 para 33 modelos publicaveis e a regua continuou aprovando 28: cinco modelos
inteiros podiam sumir da varredura sem uma unica falha — e junto com eles sumiria
a unica medicao que ve as strings daqueles registros chegando a tela. A frase "um
por modelo do banco" estava escrita ao lado de um numero que nao era mais o do
banco, o que e pior que nao ter a frase: ela afirma a cobertura que a regua parou
de cobrar.

E a cicatriz do "numero de tela nasce contado, nunca digitado" (secao 8), agora
dentro da bancada e nao na pagina. A regua passou a LER `dados/modelos-robo.json`
e a cobrar, por id, um estado para cada modelo publicavel.

O QUE CADA MUTACAO TEM DE FAZER: reprovar. A (3) e a que nao existia antes desta
leva — ela nao mexe na varredura, mexe no BANCO, e mede a deriva entre o que o
banco tem e o que a ilha serve.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VARREDOR = 'ferramentas/varrer-corpo.php'
TESTES = ('ferramentas/teste-acentuacao.php',)

LOOP_CERTO = "\tforeach ( $r1['modelos'] as $m ) {"
LOOP_SEM_O_ULTIMO = "\tforeach ( array_slice( $r1['modelos'], 0, -1 ) as $m ) {"
LOOP_ATE_28 = "\tforeach ( array_slice( $r1['modelos'], 0, 28 ) as $m ) {"


def _troca(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(antes) != quantas:
        raise AssertionError('%s: esperava %d ocorrencia(s) de %r, achei %d — a mutacao '
                             'seria inerte' % (arquivo, quantas, antes[:48], texto.count(antes)))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def _um_modelo_fora_da_varredura(base):
    """O defeito na sua forma minima: UM modelo deixa de ser montado. Com a regua
    antiga, 32 estados de R1 continuavam acima do piso de 28 e nada reprovava."""
    _troca(base, VARREDOR, LOOP_CERTO, LOOP_SEM_O_ULTIMO)


def _varredura_cortada_no_piso_antigo(base):
    """O defeito exatamente como ele estava vivo em 13/09/2026: a varredura para
    nos 28 primeiros modelos, que era o numero digitado na regua. Cinco modelos
    ficam de fora — os cinco ultimos da ordem do banco, quaisquer que sejam — e o
    portao antigo aprova, porque 28 estados de R1 e exatamente o piso dele."""
    _troca(base, VARREDOR, LOOP_CERTO, LOOP_ATE_28)


def _modelo_novo_no_banco_sem_regerar(base):
    """PRODUZ O MUNDO, e pelo DADO em vez de pelo codigo. Um modelo entra no banco
    e ninguem roda `gerar-r1.py --gravar`: `dados/r1-respostas.json` continua o de
    ontem, a varredura monta os estados de ontem, e o modelo novo nunca chega a
    tela de medicao nenhuma. Nenhuma linha de codigo esta errada — a deriva e entre
    dois arquivos. E o caso que a regua antiga NAO podia pegar nem em principio,
    porque ela comparava a varredura com um numero, e nunca com o banco."""
    caminho = os.path.join(base, 'dados/modelos-robo.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    molde = None
    for r in banco['registros']:
        if r['status'] == 'publicavel':
            molde = r
            break
    if molde is None:
        raise AssertionError('o banco nao tem modelo publicavel — a mutacao seria inerte')
    novo = json.loads(json.dumps(molde))
    novo['id'] = 'wap-modelo-que-nao-foi-servido'
    novo['codigo_fabricante'] = 'W-MUTACAO'
    banco['registros'].append(novo)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=2)
        f.write('\n')


MUTACOES = [
    (
        'um modelo some da varredura',
        'a forma minima: com o piso digitado de 28, 32 estados de R1 passavam sem uma falha',
        _um_modelo_fora_da_varredura,
    ),
    (
        'a varredura para nos 28 primeiros modelos',
        'o defeito como ele estava vivo: cinco modelos fora da unica medicao que le o corpo deles',
        _varredura_cortada_no_piso_antigo,
    ),
    (
        'modelo novo no banco e r1-respostas.json de ontem',
        'PRODUZ O MUNDO pelo dado: nenhuma linha de codigo errada, e o modelo novo nao chega a tela de medicao nenhuma',
        _modelo_novo_no_banco_sem_regerar,
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na varredura por modelo — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in TESTES:
                cmd = ['php', os.path.join(base, teste), base]
                saida = subprocess.run(cmd, capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'ERRO', 'x '))]

            if not pegou_em:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-62s %d falha(s) em %s'
                  % (nome, len(falhas), ', '.join(pegou_em)))
            for l in falhas[:2]:
                print('         %s' % l[:120])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for n in passaram:
            print('  - %s' % n)
        sys.exit(1)


if __name__ == '__main__':
    main()

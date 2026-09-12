#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito a comparacao R1 x referencia e exige REPROVACAO.

    python3 ferramentas/mutacoes-chaves-da-r1.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
As travas que ele mede nasceram em 12/09/2026, DEPOIS do defeito — entao elas
passarem nao prova coisa nenhuma.

O DEFEITO, e ele estava verde havia blocos. A secao 3 do ferramentas/teste-r1.php
compara cada frase do snippet com a da implementacao de referencia, e e o bloco
que justifica o arquivo existir. Todos os seus lacos eram assim:

    foreach ( $esperado[ $grupo ] as $k => $ref ) {
        $item = $obtido[ $grupo ][ $k ];

Ele varre a lista da REFERENCIA e indexa a do PHP pela chave dela. Duas coisas
somem por causa disso, e as duas sao da familia que esta ilha ja pagou tres
vezes:

  (a) ITEM A MAIS NO LADO DO PHP NUNCA E COMPARADO COM NADA. Se o snippet
      passasse a recomendar uma peca que a referencia nao tem, o laco nao teria
      chave por onde encontra-la — e a R1 recomendaria, na tela, uma peca que a
      regra da ilha nao declarou. Numa ilha cujo produto e compatibilidade, esse
      e o defeito mais caro que existe.

  (b) GRUPO VAZIO RODA ZERO VEZES E CONTINUA VERDE. Foi o que aconteceu de
      verdade: ao transcrever a composicao dos kits do ERB30 e do ERB44 em
      12/09/2026, 'kits_sem_composicao' zerou em TODOS os modelos, e a
      comparacao daquele grupo deixou de medir o que foi escrita para medir —
      sem uma linha de aviso. E a mesma "mutacao inerte" do registro de 11/09,
      agora do lado do teste. Ao escrever a contagem por grupo apareceu um
      segundo grupo que ninguem sabia estar vazio: 'terceiro', que nunca mediu
      nada desde que o arquivo existe.

O QUE ESTE ARQUIVO EXIGE DE CADA MUTACAO. Que ela reprove pela trava NOVA, e nao
de raspao por outra. Por isso cada mutacao aqui e escolhida para passar pelo
portao ANTIGO: a de chave a mais mantem o numero de frases comparadas acima do
piso de 100, e a de grupo vazio deixa 141 frases comparadas — as duas passariam
verdes na bancada de ontem.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GABARITO = 'dados/r1-referencia.json'
OBTIDO = 'dados/r1-respostas.json'
TESTE = ('ferramentas/teste-r1.php',)


def _primeiro_modelo_com(doc, grupo):
    """O primeiro modelo cujo grupo tem item. Escolhido por varredura e nunca
    digitado: modelo cravado no teste envelhece calado quando o banco muda."""
    for mid, resp in doc['respostas'].items():
        if resp.get(grupo):
            return mid
    raise AssertionError('nenhum modelo tem item em %s — a mutacao seria inerte' % grupo)


def _peca_a_mais_no_php(base):
    """O PHP passa a servir uma peca que a referencia nao tem.

    E o defeito (a) inteiro: a R1 recomendando na tela um item que a regra da
    ilha nunca declarou. Com o laco antigo, a chave extra nao existe do lado do
    gabarito, entao NADA a compara — e as 191 frases legitimas continuam batendo.
    """
    caminho = os.path.join(base, OBTIDO)
    with open(caminho, encoding='utf-8') as f:
        doc = json.load(f)
    mid = _primeiro_modelo_com(doc, 'fabricante')
    clone = json.loads(json.dumps(doc['respostas'][mid]['fabricante'][0]))
    doc['respostas'][mid]['fabricante'].append(clone)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')


def _peca_a_menos_no_php(base):
    """O lado contrario: o PHP deixa de servir uma peca que a referencia tem.

    Aqui o laco antigo indexaria uma chave inexistente. Em PHP isso e um aviso,
    nao um erro — e a frase comparada vira vazio contra vazio em alguns estados.
    A trava de chaves diz o que aconteceu, com nome do modelo e do grupo.
    """
    caminho = os.path.join(base, OBTIDO)
    with open(caminho, encoding='utf-8') as f:
        doc = json.load(f)
    mid = _primeiro_modelo_com(doc, 'fabricante')
    doc['respostas'][mid]['fabricante'].pop()
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')


def _grupo_principal_esvaziado_no_gabarito(base):
    """O grupo que SEMPRE tem caso fica vazio na referencia, e o teste para de
    medir a R1 inteira sem reprovar.

    Escolhida para passar pelo portao antigo de proposito: sobram as 140 frases
    de recusa e 1 de variante, ou seja 141 — acima do piso de 100 que o
    'a comparacao cobriu o banco inteiro' cobra. Na bancada de ontem esta
    mutacao apagava a medicao central do arquivo e dava VERDE.
    """
    caminho = os.path.join(base, GABARITO)
    with open(caminho, encoding='utf-8') as f:
        doc = json.load(f)
    for resp in doc['respostas'].values():
        resp['fabricante'] = []
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')


def _kit_fechado_so_do_lado_do_php(base):
    """Um kit volta a ficar sem composicao SO no lado do PHP.

    E a mutacao que amarra este arquivo ao bloco que o gerou. Ela nao toca no
    banco: reproduz o mundo em que a option do site envelheceu e o site continua
    dizendo "ha um kit e nao sabemos o que vem dentro" para um modelo cuja
    composicao ja foi transcrita. Como o grupo esta vazio nos dois lados hoje, o
    laco de frase nao roda nem depois da mutacao — quem pega e a trava de chaves.
    """
    caminho = os.path.join(base, OBTIDO)
    with open(caminho, encoding='utf-8') as f:
        doc = json.load(f)
    alvo = None
    for mid, resp in doc['respostas'].items():
        if resp.get('fabricante'):
            alvo = (mid, resp)
            break
    if alvo is None:
        raise AssertionError('nenhum modelo com item de fabricante')
    mid, resp = alvo
    resp['kits_sem_composicao'] = {'kit-fantasma': resp['fabricante'][0]}
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')


MUTACOES = [
    (
        'o PHP serve uma peca a MAIS que a referencia',
        'a R1 recomendaria na tela um item que a regra da ilha nunca declarou, e o laco antigo nao teria por onde ve-lo',
        _peca_a_mais_no_php,
    ),
    (
        'o PHP serve uma peca a MENOS que a referencia',
        'o lado contrario da mesma assimetria: a chave some e o laco antigo indexa o vazio',
        _peca_a_menos_no_php,
    ),
    (
        'o grupo principal fica vazio na referencia',
        'restam 141 frases comparadas, acima do piso de 100 — na bancada de ontem isto apagava a medicao central e dava verde',
        _grupo_principal_esvaziado_no_gabarito,
    ),
    (
        'um kit volta a ficar sem composicao so do lado do PHP',
        'o site diria "ha um kit e nao sabemos o que vem dentro" para um modelo cuja composicao ja foi transcrita',
        _kit_fechado_so_do_lado_do_php,
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na comparacao R1 x referencia — cada uma TEM que reprovar\n')

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
            for teste in TESTE:
                cmd = ['php', os.path.join(base, teste), base]
                saida = subprocess.run(cmd, capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'ERRO'))]

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
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

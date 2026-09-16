#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A TERCEIRA CONTA do portao do canal brasileiro.

    python3 ferramentas/conferir-canal-na-resposta.py [raiz]

POR QUE ESTE ARQUIVO EXISTE, E POR QUE ELE NAO PODE MORAR DENTRO DA R2
---------------------------------------------------------------------
O portao nasceu em 16/09/2026 dentro de `cobertura-r2.py`: `classificar_modelos`
pula o modelo sem canal brasileiro antes de olhar o Pa. So que a R2 desta ilha e
uma dupla — a referencia em Python decide e `gerar-r2.py` grava a decisao em
`dados/r2-respostas.json`, que e o que o site serve. As duas metades saem SEMPRE
de acordo, porque a segunda copia a primeira. Entao uma regua escrita dentro da
referencia nao e regua: e a propria decisao se conferindo, e ela fica verde no
dia em que a decisao estiver errada.

E o defeito que esta ilha ja pagou tres vezes com nomes diferentes: a funcao
`atende()` que so o teste chamava, os dois 63 da R1 que davam o mesmo numero por
acidente do banco, e a dispersao do A1 em que gerador e teste erravam juntos. A
forma dele e sempre a mesma — duas metades que concordam por construcao, e
nenhuma terceira voz.

ENTAO ESTA CONTA LE O ARTEFATO PUBLICADO E NAO O CODIGO QUE O PRODUZIU. Ela abre
`dados/r2-respostas.json` — o arquivo que o Sync leva para a option que a pagina
le —, junta TODO id de modelo que aparece em lista de recomendacao, e cobra do
banco que cada um tenha canal brasileiro. Se alguem tirar o portao da referencia
e regerar, as duas metades continuam de acordo entre si e esta conta discorda das
duas.

O QUE ELA COBRA, e sao tres coisas separadas:

  1. Nenhum modelo em `elegiveis` ou `no_limiar` pode estar sem canal brasileiro.
     E a afirmacao que importa: e essa lista que vira cartao com porta de compra.
  2. Os modelos que a resposta carrega em `modelos[]` (a vitrine) tambem nao.
  3. As somas de cada situacao tem que fechar com o total de publicaveis do
     banco. Sem isto, um modelo poderia sumir de todos os grupos em silencio —
     que e como um portao mal escrito esconde o que ele barra em vez de declarar.
"""

import json
import os
import sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


def carregar(nome):
    with open(os.path.join(RAIZ, 'dados', nome), encoding='utf-8') as f:
        return json.load(f)


def main():
    respostas = carregar('r2-respostas.json')
    banco = carregar('modelos-robo.json')

    canal = {r['id']: (r.get('canal_brasileiro') or {}).get('valor')
             for r in banco['registros']}
    publicaveis = {r['id'] for r in banco['registros'] if r['status'] == 'publicavel'}

    falhas = []
    afirmacoes = 0

    # ---------------------------------------------------- 1. as listas de recomendacao
    for situacao, grupos in sorted(respostas['classificacao'].items()):
        for nome_grupo in ('elegiveis', 'no_limiar'):
            for mid in grupos.get(nome_grupo, []):
                afirmacoes += 1
                if mid not in canal:
                    falhas.append('FALHA %s/%s: o id %r nao existe em modelos-robo.json'
                                  % (situacao, nome_grupo, mid))
                elif canal[mid] is None:
                    falhas.append(
                        'FALHA %s/%s: %s esta na lista de recomendacao e NAO tem canal '
                        'brasileiro. A pagina estaria mandando o leitor comprar um '
                        'aparelho que o fabricante nao publica no Brasil'
                        % (situacao, nome_grupo, mid))

    # ------------------------------------------------------------ 2. a vitrine servida
    for m in respostas.get('modelos', []):
        afirmacoes += 1
        mid = m['id']
        if canal.get(mid) is None:
            falhas.append(
                'FALHA modelos[]: %s vai para a vitrine da resposta sem canal brasileiro'
                % mid)

    # ------------------------------------------------- 3. as somas fecham com o banco
    #
    # O portao BARRA, e barrar em silencio e o que faz um numero encolher sem que
    # nada discorde. Se os grupos de uma situacao nao somam os publicaveis do
    # banco, algum modelo saiu da conta sem ser declarado em grupo nenhum.
    for situacao, grupos in sorted(respostas['classificacao'].items()):
        afirmacoes += 1
        soma = (len(grupos.get('elegiveis', []))
                + len(grupos.get('no_limiar', []))
                + int(grupos.get('nao_atendem', 0))
                + int(grupos.get('sem_pa_declarado', 0))
                + int(grupos.get('sem_canal_brasileiro', 0)))
        if soma != len(publicaveis):
            falhas.append(
                'FALHA %s: os grupos somam %d e o banco tem %d publicaveis — %d modelo(s) '
                'sairam da classificacao sem ser declarados em grupo nenhum'
                % (situacao, soma, len(publicaveis), len(publicaveis) - soma))

    barrados = sorted(mid for mid in publicaveis if canal[mid] is None)
    print('Conferencia do canal brasileiro na resposta servida')
    print('  modelos publicaveis no banco ....... %d' % len(publicaveis))
    print('  com canal brasileiro ............... %d' % (len(publicaveis) - len(barrados)))
    print('  barrados pelo portao ............... %d%s'
          % (len(barrados), ('  ' + ', '.join(barrados)) if barrados else ''))
    print('  afirmacoes ......................... %d' % afirmacoes)

    if falhas:
        print('\nREPROVADO — %d falha(s):' % len(falhas))
        for f in falhas:
            print('  x %s' % f)
        sys.exit(1)
    print('\nAPROVADO: nenhum modelo sem canal brasileiro na resposta servida.')


if __name__ == '__main__':
    main()

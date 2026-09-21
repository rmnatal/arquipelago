#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutacoes deliberadas contra ferramentas/validar-derivados.py.

    python3 ferramentas/mutacoes-derivados.py

POR QUE ESTA BATERIA EXISTE: o portao que ela ataca nasceu em 21/09/2026 e,
no minuto em que os derivados foram regravados, ele ficou VERDE. Trava que
nasce sem mudar nada e trava que ninguem sabe se existe — a mesma frase que
`mutacoes-canal-brasileiro.py` carrega, pelo mesmo motivo. Aqui ela pesa o
dobro, porque o defeito que o portao existe para pegar ficou um dia no ar com
38 portoes verdes ao lado.

CADA MUTACAO FABRICA UM MUNDO E EXIGE UM VEREDITO. A (1) e a reconstituicao
LITERAL do defeito de 20/09: o `as_duas` do cobertura-r1.json volta para 15
com o banco medindo 11. A (5) e a que mais importa para o futuro: ela fabrica
um derivado NOVO, que ninguem declarou, e exige que o portao o denuncie em vez
de ignora-lo — e a regra que impede este arquivo de envelhecer como envelheceu
o que ele conserta.

A (6) NAO e mutacao de defeito: e a prova do mundo sadio. Sem ela, uma trava
que reprovasse TUDO passaria nesta bateria com nota maxima, e verde por
reprovar sempre e a outra metade do verde barato.

AS DUAS METADES DO VEREDITO SAO COBRADAS: codigo de saida E palavra impressa.
Portao que imprime REPROVADO saindo com 0 e INERTE, e a bancada desta ilha
nomeia isso — aqui a bateria nomeia primeiro.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _ler(base, rel):
    with open(os.path.join(base, rel), encoding='utf-8') as fh:
        return json.load(fh)


def _gravar(base, rel, doc):
    with open(os.path.join(base, rel), 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write('\n')


def _cobertura_volta_a_dizer_15(base):
    """O defeito de 20/09/2026, refeito byte a byte: o portao do canal
    brasileiro tirou quatro Roborock da interseccao e o arquivo derivado
    continuou afirmando o numero de antes."""
    doc = _ler(base, 'dados/cobertura-r1.json')
    cruz = doc['cruzamento_com_a_r2']
    cruz['contagem']['as_duas'] = 15
    cruz['as_duas_respondem'] = cruz['as_duas_respondem'] + [
        'roborock-q8-max', 'roborock-qrevo-curv',
        'roborock-qrevo-master', 'roborock-s8-maxv-ultra']
    _gravar(base, 'dados/cobertura-r1.json', doc)


def _casca_fatos_com_numero_de_ontem(base):
    """A ponta da corrente que CHEGA A TELA. O cobertura-r1.json fica certo e
    so o casca-fatos envelhece — que e o caso em que a option servida mente
    sem nenhum arquivo intermediario a acusar."""
    doc = _ler(base, 'dados/casca-fatos.json')
    doc['medicao']['as_duas'] = 15
    _gravar(base, 'dados/casca-fatos.json', doc)


def _r1_respostas_com_peca_a_mais(base):
    """Derivado da R1 mexido a mao. E o mundo em que alguem 'corrige' o
    combustivel da pagina sem passar pelo gerador."""
    doc = _ler(base, 'dados/r1-respostas.json')
    doc['resumo']['pecas_publicaveis'] = doc['resumo']['pecas_publicaveis'] + 1
    _gravar(base, 'dados/r1-respostas.json', doc)


def _tabela_de_exemplos_editada(base):
    """O derivado que NAO e JSON. O cabecalho dele diz 'Nao edite a mao' — e
    ate 21/09/2026 nada media se alguem editou."""
    rel = os.path.join(base, 'dados/tabela-exemplos-r1.md')
    with open(rel, encoding='utf-8') as fh:
        texto = fh.read()
    with open(rel, 'w', encoding='utf-8') as fh:
        fh.write(texto.replace('| ', '| ~', 1))


def _derivado_novo_nao_declarado(base):
    """Um derivado que ninguem cobriu nem declarou. O portao TEM que
    denuncia-lo: e o unico jeito de ele nao envelhecer sozinho, do jeito que
    envelheceu a lista de bancadas escrita de cabeca."""
    _gravar(base, 'dados/cobertura-r3.json', {
        'id': 'cobertura-r3',
        'gerado_por': 'ferramentas/cobertura-r3.py',
        'resumo': {'inventado_para_a_mutacao': True},
    })


def _mundo_sadio(base):
    """Nada muda. Tem que APROVAR — se reprovar, o portao reprova sempre e
    esta bateria inteira valeria zero."""
    return


MUTACOES = [
    ('cobertura-r1.json volta a afirmar as_duas=15',
     'e o defeito real de 20/09, com o banco medindo 11', _cobertura_volta_a_dizer_15, 'reprovar'),
    ('casca-fatos.json guarda o numero de ontem',
     'e a ponta que chega a tela, sem intermediario para acusar', _casca_fatos_com_numero_de_ontem, 'reprovar'),
    ('r1-respostas.json editado a mao',
     'combustivel da pagina mexido sem passar pelo gerador', _r1_respostas_com_peca_a_mais, 'reprovar'),
    ('tabela-exemplos-r1.md editada a mao',
     'o derivado que nao e JSON, e o cabecalho dele proibe a mao', _tabela_de_exemplos_editada, 'reprovar'),
    ('derivado novo que ninguem declarou',
     'a regra que impede o proprio portao de envelhecer calado', _derivado_novo_nao_declarado, 'reprovar'),
    ('o mundo sadio, sem nenhuma mutacao',
     'sem esta, um portao que reprova tudo passaria com nota maxima', _mundo_sadio, 'aprovar'),
]


def _rodar(base):
    return subprocess.run(
        ['python3', os.path.join(base, 'ferramentas/validar-derivados.py')],
        cwd=base, capture_output=True, text=True, timeout=900)


def main():
    print('Mutacoes deliberadas em validar-derivados.py — cada uma com o '
          'veredito que ela exige\n')

    certas = 0
    erradas = []

    for nome, porque, aplicar, esperado in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            aplicar(base)
            saida = _rodar(base)

            reprovou_pelo_codigo = saida.returncode != 0
            reprovou_pela_palavra = 'REPROVADO' in saida.stdout
            aprovou_pela_palavra = saida.stdout.strip().splitlines() and any(
                l.startswith('APROVADO') for l in saida.stdout.splitlines())

            if reprovou_pelo_codigo != reprovou_pela_palavra:
                print('  INERTE %-52s codigo=%d, palavra=%s'
                      % (nome, saida.returncode,
                         'REPROVADO' if reprovou_pela_palavra else 'sem REPROVADO'))
                erradas.append(nome)
                continue

            if esperado == 'reprovar' and reprovou_pelo_codigo:
                linha = [l.strip() for l in saida.stdout.splitlines()
                         if l.strip().startswith(('REPROVADO', 'NAO JULGADO'))]
                print('  ok     %-52s reprovou' % nome)
                if linha:
                    print('         %s' % linha[0][:110])
                certas += 1
            elif esperado == 'aprovar' and not reprovou_pelo_codigo and aprovou_pela_palavra:
                print('  ok     %-52s aprovou o mundo sadio' % nome)
                certas += 1
            else:
                print('  ERRADO %-52s esperava %s e o portao %s'
                      % (nome, esperado,
                         'reprovou' if reprovou_pelo_codigo else 'aprovou'))
                print('         (%s)' % porque)
                erradas.append(nome)

    print('\n%d de %d mutacoes no veredito esperado.' % (certas, len(MUTACOES)))
    if erradas:
        print('REPROVADO: mutacao com veredito errado:')
        for nome in erradas:
            print('  - %s' % nome)
        return 1
    print('APROVADO: a trava dos derivados reprova o que promete e deixa passar '
          'o mundo sadio.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

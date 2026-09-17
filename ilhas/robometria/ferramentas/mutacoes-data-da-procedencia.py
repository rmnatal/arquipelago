#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de propósito a linha de procedência do cartão da R2 e exige REPROVACAO.

    python3 ferramentas/mutacoes-data-da-procedencia.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Em 17/09/2026 a regua do `conferir-no-ar.py` foi AFROUXADA, e afrouxar trava sem
plantar o mundo em que ela morde e o mesmo que nao ter trava (secao 8 do
ARQUIPELAGO.md). O que ela exigia era o literal

    'Como sabemos — página do fabricante, verificado em 09/09/2026'

dentro de TODO cartao da vitrine da R2. Ficou verde seis dias, e nao porque a
pagina garantisse aquela data: porque os cinco modelos servidos tinham sido
coletados no mesmo dia. VERDADE POR COINCIDENCIA DA COLETA — a mesma frase que
esta ilha ja usou para descrever a elegibilidade da R2 antes de o portao do canal
brasileiro existir. Cada cartao carrega o `verificado_em` da fonte DELE, e no dia
em que entrou um modelo coletado em outra data (o Roborock Q8 Max, 17/09) a regua
acusou defeito num cartao que estava certo.

A regua passou a exigir a FRASE mais UMA DATA no formato da tela, e continua
digitada: nada aqui e lido do banco, que e o que faz a conferencia no ar medir
alguma coisa em vez de conferir o arquivo consigo mesmo.

O QUE CADA MUTACAO TEM DE FAZER: as quatro primeiras reprovam, e a quinta —
DUAS DATAS DIFERENTES NO MESMO MUNDO — tem de PASSAR. E ela que separa o conserto
do afrouxamento: era exatamente esse mundo que a constante antiga reprovava, e e
o unico mundo desta lista que o banco de hoje produz de verdade.
"""

import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_spec = importlib.util.spec_from_file_location(
    'conferir_no_ar', os.path.join(RAIZ, 'ferramentas', 'conferir-no-ar.py'))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)   # nao dispara rede: o arquivo tem guarda __main__

REGRA = _mod.R2_PROCEDENCIA_DATA
FRASE = _mod.R2_PROCEDENCIA

LINHA_BOA = FRASE + '09/09/2026 · '
LINHA_NOVA = FRASE + '17/09/2026 · '


def cartao(linha):
    return ('<li class="rbm-vitrine-item"><h3>Modelo</h3>'
            '<p class="rbm-procedencia">%s</p></li>' % linha)


MUTACOES = [
    ('o cartao perde a linha de procedencia inteira',
     'e o defeito original que a trava existe para pegar: numero de Pa na tela sem '
     'dizer de onde veio',
     cartao('<span>5.500 Pa</span>'), False),
    ('a frase fica e a DATA some',
     'procedencia sem data e procedencia que nao envelhece — o leitor nao consegue '
     'saber se a leitura e de ontem ou de marco',
     cartao(FRASE + ' · '), False),
    ('a data vem em formato de banco, nao de tela',
     'aaaa-mm-dd e o formato do `verificado_em` do JSON; se a regua aceitasse os '
     'dois, ela deixaria de medir qual dos dois chegou a tela',
     cartao(FRASE + '2026-09-17 · '), False),
    ('a frase muda de palavra e a data continua certa',
     'a metade FIXA da linha continua digitada aqui de proposito: mudar o texto no '
     'repositorio TEM que quebrar esta conferencia, senao ela nao mede nada',
     cartao('Como sabemos — loja parceira, verificado em 17/09/2026 · '), False),
    ('DOIS cartoes com datas DIFERENTES, os dois validos',
     'o mundo que a constante antiga reprovava e que o banco de hoje produz: um '
     'modelo coletado em 09/09 ao lado de um coletado em 17/09',
     cartao(LINHA_BOA) + cartao(LINHA_NOVA), True),
]


def main():
    print('Mutacoes na linha de procedencia do cartao da R2 — quatro reprovam, uma passa\n')
    erradas = 0
    for nome, porque, mundo, deve_passar in MUTACOES:
        import re
        cartoes = re.findall(r'<li class="rbm-vitrine-item">(.*?)</li>', mundo, re.S)
        if not cartoes:
            print('  ERRO   %-58s mundo sem cartao — a mutacao seria inerte' % nome)
            erradas += 1
            continue
        passou = all(REGRA.search(c) for c in cartoes)
        certo = (passou == deve_passar)
        print('  %-6s %-58s esperado: %s | medido: %s'
              % ('ok' if certo else 'ERRO', nome,
                 'PASSAR' if deve_passar else 'REPROVAR',
                 'passou' if passou else 'reprovou'))
        if not certo:
            print('         (%s)' % porque)
            erradas += 1

    print()
    if erradas:
        print('REPROVADO: %d de %d mutacoes com resultado inesperado.' % (erradas, len(MUTACOES)))
        return 1
    print('APROVADO: %d de %d mutacoes com o resultado esperado, 0 inertes.'
          % (len(MUTACOES), len(MUTACOES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())

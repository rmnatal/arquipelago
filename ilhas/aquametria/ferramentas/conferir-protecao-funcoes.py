# -*- coding: utf-8 -*-
"""Confere que toda declaracao de funcao no comeco de linha do snippet vem
logo depois do guarda if ( ! function_exists( 'mesmo-nome' ) ) {."""
import io, re, sys

falhou = False
for arq in sys.argv[1:]:
    linhas = io.open(arq, encoding='utf-8').read().split('\n')
    nomes, ruins = [], []
    for i, l in enumerate(linhas):
        m = re.match(r'function ([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', l)
        if not m:
            continue
        nome = m.group(1)
        nomes.append(nome)
        # olha para tras pulando docblock e comentario ate achar o guarda
        j, anterior = i - 1, ''
        while j >= 0:
            t = linhas[j].strip()
            if t == '' or t.startswith('*') or t.startswith('/*') or t.startswith('//'):
                j -= 1
                continue
            anterior = t
            break
        if anterior != "if ( ! function_exists( '%s' ) ) {" % nome:
            ruins.append((i + 1, nome, anterior[:70]))
    if ruins:
        falhou = True
        print('DESPROTEGIDAS em %s:' % arq)
        for ln, nome, ant in ruins:
            print('   linha %d  %s  (anterior: %s)' % (ln, nome, ant))
    else:
        print('ok %s — %d funcoes, todas dentro de function_exists' % (arq, len(nomes)))

sys.exit(1 if falhou else 0)

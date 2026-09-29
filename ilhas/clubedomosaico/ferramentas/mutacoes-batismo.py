#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DA TRAVA DO BATISMO — 29/09/2026.

    python3 ferramentas/mutacoes-batismo.py

Cada mutacao mexe numa trava de `ferramentas/batismo-do-fabricante.py` e roda
`ferramentas/teste-batismo.py`. **Toda mutacao tem de REPROVAR.** Mutacao que
passa e uma trava que a bancada nao mede — e trava que ninguem mede e trava que
nao existe, por mais bem escrita que esteja no cabecalho.

DUAS MUTACOES ANDAM PARA O OUTRO LADO, de proposito (m07 e m08): elas APERTAM a
regua em vez de afrouxa-la. A tolerancia ao nome de arquivo mutilado pelo
servidor do fabricante e uma FOLGA deliberada, e folga deliberada que ninguem
mede vira, na leitura seguinte, folga que alguem aperta por zelo — reprovando
`Rejunte Epóxi Quartzolit`, que e um batismo certo. Regua que reprova o certo
custa tanto quanto regua que aprova o errado.

A SEGUNDA METADE ATACA O ESQUEMA E O BANCO, nao a regra: e o outro lado do
mesmo portao. Ela roda o `validar-banco.py`, e inclui a mutacao que a 26.2
exige por escrito — apagar a chave do esquema. Trava que le a propria lista de
um arquivo de dados aprova tudo, em silencio, no dia em que o arquivo perder a
chave, e o banco de hoje continua verde.
"""

import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGRA = os.path.join(RAIZ, 'ferramentas', 'batismo-do-fabricante.py')
BANCADA = os.path.join(RAIZ, 'ferramentas', 'teste-batismo.py')
VALIDADOR = os.path.join(RAIZ, 'ferramentas', 'validar-banco.py')
ESQUEMA = os.path.join(RAIZ, 'dados', 'esquema-banco.json')
BANCO_ACABAMENTO = os.path.join(RAIZ, 'dados', 'materiais-acabamento.json')


def troca(texto, antigo, novo):
    if antigo not in texto:
        raise SystemExit('mutacao invalida: o alvo nao existe mais em '
                         'batismo-do-fabricante.py\n  %r' % antigo[:70])
    return texto.replace(antigo, novo, 1)


def m01(t):
    """a trava para de cobrar: nenhuma palavra e exigida"""
    return troca(t, "        fora.append((bruto, formas))", "        pass")


def m02(t):
    """a marca deixa de ser exceçao e passa a esvaziar a cobranca inteira"""
    return troca(t, "        if not formas or (formas & marca):",
                    "        if True:")


def m03(t):
    """o batismo passa a ser comparado com a URL INTEIRA, nao com o arquivo"""
    return troca(t,
                 "    caminho = urllib.parse.urlparse(url or '').path\n"
                 "    return urllib.parse.unquote(os.path.basename(caminho))",
                 "    return urllib.parse.unquote(url or '')")


def m04(t):
    """entre as fontes que batizam passa a vencer a de MAIOR nivel"""
    return troca(t, "    candidatas.sort(key=lambda c: (c[0], c[1]))",
                    "    candidatas.sort(key=lambda c: (-c[0], c[1]))")


def m05(t):
    """o esquema sem a lista deixa de reprovar e passa a aprovar em silencio"""
    return troca(t,
                 "        raise EsquemaSemBatismo(\n"
                 "            'o esquema nao tem `batismo_do_fabricante`: sem a lista de fontes que '\n"
                 "            'batizam, esta trava nao mede nada e nao pode aprovar (26.2)')",
                 "        return True, {'em_escopo': False, 'motivo': 'sem lista no esquema'}")


def m06(t):
    """a lista vazia no esquema deixa de reprovar"""
    return troca(t,
                 "        raise EsquemaSemBatismo(\n"
                 "            '`batismo_do_fabricante.origens_que_batizam` esta vazia ou nao e lista: '\n"
                 "            'trava sem lista aprova tudo em silencio (26.2)')",
                 "        return True, {'em_escopo': False, 'motivo': 'lista vazia no esquema'}")


def m07(t):
    """APERTA: a letra acentuada deixa de poder sumir (o servidor do fabricante some com ela)"""
    return troca(t, "        if len(decomposto) > 1 and unicodedata.category(decomposto[1]) == 'Mn':\n"
                    "            continue",
                    "        pass")


def m08(t):
    """APERTA: a palavra passa a ter de casar inteira, e nome de arquivo colado deixa de valer"""
    return troca(t, "        if not any(any(f in alvo for alvo in formas_arquivo) for f in formas):",
                    "        if not any(any(f == alvo for alvo in formas_arquivo) for f in formas):")


def m09(t):
    """o separador volta a contar de um lado so, e arquivo colado deixa de casar"""
    return troca(t, "    return re.sub(r'[^0-9a-z]+', '', _sem_acento(texto or '').lower())",
                    "    return _sem_acento(texto or '').lower()")


def m10(t):
    """a palavra vazia deixa de ser vazia e a trava cobra `para`, `de`, `e`"""
    return troca(t, "        if _achatar(bruto) in VAZIAS:\n            continue",
                    "        if False:\n            continue")


MUTACOES = [
    ('a trava para de cobrar palavra nenhuma', m01),
    ('a excecao da marca esvazia a cobranca inteira', m02),
    ('compara com a URL inteira em vez do nome do arquivo', m03),
    ('entre as fontes passa a vencer a de MAIOR nivel', m04),
    ('esquema sem a chave deixa de reprovar (26.2)', m05),
    ('lista vazia no esquema deixa de reprovar (26.2)', m06),
    ('APERTA: a letra acentuada nao pode mais sumir', m07),
    ('APERTA: a palavra tem de casar inteira', m08),
    ('o separador volta a contar', m09),
    ('a palavra vazia passa a ser cobrada', m10),
]


# ---------------------------------------------------------------------------
# A SEGUNDA METADE: o ESQUEMA e o BANCO, nao a regra
# ---------------------------------------------------------------------------

def d01(esquema, bancos):
    """o batismo volta a ser a descricao da ilha"""
    for m in bancos[BANCO_ACABAMENTO]['materiais']:
        if m['id'] == 'quartzolit-borracha-liquida-elastica':
            m['nome_comercial'] = 'impermeabilizante borracha liquida elastica quartzolit'
            return
    raise SystemExit('mutacao invalida: o registro nao existe mais')


def d02(esquema, bancos):
    """a chave inteira some do esquema (a mutacao que a 26.2 exige)"""
    if 'batismo_do_fabricante' not in esquema:
        raise SystemExit('mutacao invalida: a chave ja nao existe')
    del esquema['batismo_do_fabricante']


def d03(esquema, bancos):
    """`origens_que_batizam` esvazia"""
    esquema['batismo_do_fabricante']['origens_que_batizam'] = []


def d04(esquema, bancos):
    """a origem que batiza vira uma que nenhum registro cita"""
    esquema['batismo_do_fabricante']['origens_que_batizam'] = ['nada-disso']
    # Com nenhum registro em escopo a bancada tem de acusar, senao a trava
    # pode ser desligada do esquema sem ninguem ver.


MUTACOES_DO_BANCO = [
    ('o batismo volta a ser a descricao da ilha', d01, VALIDADOR),
    ('a chave `batismo_do_fabricante` some do esquema (26.2)', d02, VALIDADOR),
    ('`origens_que_batizam` esvazia', d03, VALIDADOR),
    ('a origem que batiza vira uma que ninguem cita', d04, BANCADA),
]


def roda(alvo):
    r = subprocess.run([sys.executable, alvo], capture_output=True, text=True, cwd=RAIZ)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def main():
    original = io.open(REGRA, encoding='utf-8').read()

    codigo, saida = roda(BANCADA)
    if codigo != 0:
        print('a bancada JA esta vermelha sem mutacao nenhuma — conserte antes:')
        print(saida)
        return 1
    print('bancada limpa antes de mutar: %s' % saida.strip().splitlines()[-1])

    reprovadas = passaram = invalidas = 0
    try:
        for nome, funcao in MUTACOES:
            try:
                mutado = funcao(original)
            except SystemExit as erro:
                invalidas += 1
                print('  INVALIDA   %-56s %s' % (nome, erro))
                continue
            if mutado == original:
                invalidas += 1
                print('  INVALIDA   %-56s nao mudou uma linha' % nome)
                continue
            io.open(REGRA, 'w', encoding='utf-8').write(mutado)
            codigo, _ = roda(BANCADA)
            if codigo != 0:
                reprovadas += 1
                print('  reprovada  %s' % nome)
            else:
                passaram += 1
                print('  PASSOU !!  %-56s a bancada nao mede esta trava' % nome)
    finally:
        io.open(REGRA, 'w', encoding='utf-8').write(original)

    print('\n%d de %d reprovadas na REGRA | %d passaram | %d invalidas'
          % (reprovadas, len(MUTACOES), passaram, invalidas))
    codigo, saida = roda(BANCADA)
    print('regra restaurada: %s' % saida.strip().splitlines()[-1])
    if passaram or invalidas or codigo:
        return 1

    # ---- o esquema e o banco
    print('\nO OUTRO LADO DO PORTAO: o esquema e o banco')
    esquema_original = io.open(ESQUEMA, encoding='utf-8').read()
    banco_original = io.open(BANCO_ACABAMENTO, encoding='utf-8').read()

    codigo, saida = roda(VALIDADOR)
    if codigo != 0:
        print('o validador JA esta vermelho sem mutacao nenhuma — conserte antes:')
        print(saida)
        return 1

    reprovadas_b = passaram_b = invalidas_b = 0
    try:
        for nome, funcao, alvo in MUTACOES_DO_BANCO:
            esquema = json.loads(esquema_original)
            bancos = {BANCO_ACABAMENTO: json.loads(banco_original)}
            try:
                funcao(esquema, bancos)
            except SystemExit as erro:
                invalidas_b += 1
                print('  INVALIDA   %-56s %s' % (nome, erro))
                continue
            io.open(ESQUEMA, 'w', encoding='utf-8').write(
                json.dumps(esquema, ensure_ascii=False, indent=2))
            io.open(BANCO_ACABAMENTO, 'w', encoding='utf-8').write(
                json.dumps(bancos[BANCO_ACABAMENTO], ensure_ascii=False, indent=2))
            codigo, _ = roda(alvo)
            if codigo != 0:
                reprovadas_b += 1
                print('  reprovada  %-56s (%s)' % (nome, os.path.basename(alvo)))
            else:
                passaram_b += 1
                print('  PASSOU !!  %-56s %s nao mede isto'
                      % (nome, os.path.basename(alvo)))
    finally:
        io.open(ESQUEMA, 'w', encoding='utf-8').write(esquema_original)
        io.open(BANCO_ACABAMENTO, 'w', encoding='utf-8').write(banco_original)

    print('\n%d de %d reprovadas no ESQUEMA/BANCO | %d passaram | %d invalidas'
          % (reprovadas_b, len(MUTACOES_DO_BANCO), passaram_b, invalidas_b))
    codigo, saida = roda(VALIDADOR)
    print('esquema e banco restaurados: %s' % saida.strip().splitlines()[-1])
    if passaram_b or invalidas_b or codigo:
        return 1

    total = len(MUTACOES) + len(MUTACOES_DO_BANCO)
    print('\n%d de %d reprovadas, nenhuma passou.' % (reprovadas + reprovadas_b, total))
    return 0


if __name__ == '__main__':
    sys.exit(main())

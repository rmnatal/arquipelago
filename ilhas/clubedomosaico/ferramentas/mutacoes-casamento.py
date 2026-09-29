#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DA REGRA DE CASAMENTO — 29/09/2026.

    python3 ferramentas/mutacoes-casamento.py

Cada mutacao AFROUXA uma trava de `ferramentas/casar-anuncio.py` e roda
`ferramentas/teste-casamento.py`. **Toda mutacao tem de REPROVAR.** Mutacao que
passa e uma trava que a bancada nao mede — e trava que ninguem mede e trava que
nao existe, por mais bem escrita que esteja no cabecalho.

POR QUE ESTA BATERIA VALE MAIS QUE AS OUTRAS DESTA ILHA: a regra de casamento e
o unico portao entre o banco e um `url` errado. Ela nao devolve tela vermelha
quando erra — devolve um link que parece certo, apontando para o produto errado,
na pagina que a ilha usa para dizer o que comprar. **Casamento errado no banco e
pior que casamento nenhum, porque parece dado** (25.7), e o que separa os dois e
esta bateria.

UMA DAS MUTACOES ANDA PARA O OUTRO LADO, de proposito (a m06): ela APERTA a
regra em vez de afrouxar, pondo `manual` na lista de armadilhas. Tres registros
deste banco sao *"Cortador de ceramicas e azulejos MANUAL"* — uma regua que
reprova o certo custa tanto quanto uma que aprova o errado, e so uma bancada com
os dois lados pega as duas.
"""

import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGRA = os.path.join(RAIZ, 'ferramentas', 'casar-anuncio.py')
BANCADA = os.path.join(RAIZ, 'ferramentas', 'teste-casamento.py')


def troca(texto, antigo, novo):
    if antigo not in texto:
        raise SystemExit('mutacao invalida: o alvo nao existe mais em casar-anuncio.py\n  %r'
                         % antigo[:70])
    return texto.replace(antigo, novo, 1)


def m01(t):
    """a trava da marca cai"""
    return troca(t, "    if marca and not marca <= t:",
                    "    if False:")


def m02(t):
    """a cabeca do titulo deixa de ser o produto"""
    return troca(t, "    if not (_sem_a_marca(meu, reg) & cabeca):",
                    "    if False:")


def m03(t):
    """a metade positiva cai: o titulo nao precisa mais separar X do irmao"""
    return troca(t, "        if so_meu and not (so_meu & t):",
                    "        if False:")


def m04(t):
    """a metade negativa cai: o anuncio pode vender a escolha entre dois irmaos"""
    return troca(t, "            if invasores:",
                    "            if False:")


def m05(t):
    """a lista de armadilhas esvazia"""
    return troca(t, "ARMADILHAS = [", "ARMADILHAS = [] and [")


def m06(t):
    """`manual` entra nas armadilhas — a mutacao que APERTA"""
    return troca(t, "    'kit', 'combo',", "    'manual', 'kit', 'combo',")


def m07(t):
    """a trava do nome comercial inteiro cai"""
    return troca(t, "    if faltando:", "    if False:")


def m08(t):
    """a unicidade cai: o primeiro que passar leva"""
    return troca(t, "    if len(passaram) == 1:", "    if len(passaram) >= 1:")


def m09(t):
    """a cabeca do titulo vira o titulo inteiro"""
    return troca(t, "CABECA = 4", "CABECA = 40")


def m10(t):
    """o plural deixa de cair"""
    return troca(t, "    if len(p) >= 5 and p.endswith('s'):",
                    "    if False:")


def m11(t):
    """o corte do plural perde o piso de tamanho e come palavra curta"""
    return troca(t, "    if len(p) >= 5 and p.endswith('s'):",
                    "    if len(p) >= 2 and p.endswith('s'):")


def m12(t):
    """a quebra em tokens passa a aceitar prefixo: 510 vira 51"""
    return troca(
        t,
        "            fora.append(p)",
        "            fora.append(p)\n            if len(p) > 2:\n                fora.append(p[:-1])")


# ---------------------------------------------------------------------------
# A SEGUNDA METADE DA BATERIA: O BANCO, e nao a regra
# ---------------------------------------------------------------------------
# As doze mutacoes de cima atacam a REGRA. Elas nao alcancam o outro lado do
# mesmo portao: a prova GRAVADA em `afiliado.casamento` de cada um dos dez
# registros que subiram de degrau. Titulo gravado e procedencia, e procedencia
# que ninguem reconfere e decoracao — entao `validar-banco.py` passa o titulo
# gravado pela regra VIVA e exige que ela continue identificando aquele registro.
#
# Estas cinco mutacoes fabricam o dia em que essa prova caduca: por troca de
# titulo, por sumico da ficha, por campo de procedencia faltando e — a que mais
# importa — por mudanca no PROPRIO BANCO, que e como a prova caduca sem ninguem
# tocar no campo. Todas tem de reprovar o validador.

BANCOS = [os.path.join(RAIZ, 'dados', n)
          for n in ('materiais-acabamento.json', 'materiais-alicates.json',
                    'materiais-colas.json')]
VALIDADOR = os.path.join(RAIZ, 'ferramentas', 'validar-banco.py')


def _achar(bancos, ident):
    for conteudo in bancos.values():
        for item in conteudo['materiais']:
            if item['id'] == ident:
                return item
    raise SystemExit('mutacao invalida: o registro %s nao existe mais' % ident)


def d01(b):
    """o titulo gravado vira o do irmao"""
    _achar(b, 'acrilex-verniz-acrilico-brilhante')['afiliado']['casamento'][
        'titulo_do_anuncio'] = 'Verniz Acrílico Fosco 250ml Acrilex Transparente'


def d02(b):
    """o titulo gravado fica vazio"""
    _achar(b, 'vonder-vdec-51')['afiliado']['casamento']['titulo_do_anuncio'] = ''


def d03(b):
    """o casamento fica e a ficha some"""
    _achar(b, 'cortag-torques-mosaico-roldanas')['afiliado']['url'] = ''


def d04(b):
    """um campo de procedencia do casamento some"""
    del _achar(b, 'vonder-vdec-75')['afiliado']['casamento']['loja']


def d05(b):
    """o BANCO muda e a prova caduca sem ninguem tocar no campo"""
    _achar(b, 'vonder-vdec-90')['nome_comercial'] = (
        'Cortador de ceramicas e azulejos manual, 90 cm, VDEC 90 Profissional')


DO_BANCO = [
    ('o titulo gravado vira o do irmao', d01),
    ('o titulo gravado fica vazio', d02),
    ('o casamento fica e a ficha some', d03),
    ('um campo de procedencia do casamento some', d04),
    ('o BANCO muda e a prova caduca sozinha', d05),
]


MUTACOES = [
    ('a trava da marca cai', m01),
    ('a cabeca do titulo deixa de ser o produto', m02),
    ('o titulo nao precisa mais separar X do irmao', m03),
    ('o anuncio pode vender a escolha entre dois irmaos', m04),
    ('a lista de armadilhas esvazia', m05),
    ('APERTA: `manual` entra nas armadilhas', m06),
    ('a trava do nome comercial inteiro cai', m07),
    ('a unicidade cai: o primeiro que passar leva', m08),
    ('a cabeca do titulo vira o titulo inteiro', m09),
    ('o plural deixa de cair', m10),
    ('o corte do plural come palavra curta', m11),
    ('a quebra em tokens passa a aceitar prefixo', m12),
]


def roda_validador():
    r = subprocess.run([sys.executable, VALIDADOR], capture_output=True, text=True,
                       cwd=RAIZ)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def roda_bancada():
    r = subprocess.run([sys.executable, BANCADA], capture_output=True, text=True)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def main():
    original = io.open(REGRA, encoding='utf-8').read()

    codigo, saida = roda_bancada()
    if codigo != 0:
        print('a bancada JA esta vermelha sem mutacao nenhuma — conserte antes:')
        print(saida)
        return 1
    print('bancada limpa antes de mutar: %s' % saida.strip().splitlines()[0])

    reprovadas = passaram = invalidas = 0
    try:
        for nome, funcao in MUTACOES:
            try:
                mutado = funcao(original)
            except SystemExit as erro:
                invalidas += 1
                print('  INVALIDA   %-52s %s' % (nome, erro))
                continue
            if mutado == original:
                invalidas += 1
                print('  INVALIDA   %-52s nao mudou uma linha' % nome)
                continue
            io.open(REGRA, 'w', encoding='utf-8').write(mutado)
            codigo, _ = roda_bancada()
            if codigo != 0:
                reprovadas += 1
                print('  reprovada  %s' % nome)
            else:
                passaram += 1
                print('  PASSOU !!  %-52s a bancada nao mede esta trava' % nome)
    finally:
        io.open(REGRA, 'w', encoding='utf-8').write(original)

    print('\n%d de %d reprovadas na REGRA | %d passaram | %d invalidas'
          % (reprovadas, len(MUTACOES), passaram, invalidas))
    codigo, saida = roda_bancada()
    print('regra restaurada: %s' % saida.strip().splitlines()[0])
    if passaram or invalidas or codigo:
        return 1

    # ---- a segunda metade: o banco
    originais = {caminho: io.open(caminho, encoding='utf-8').read() for caminho in BANCOS}
    codigo, _ = roda_validador()
    if codigo != 0:
        print('o validador JA esta vermelho sem mutacao nenhuma — conserte antes')
        return 1
    print('\nvalidador limpo antes de mutar o banco.')

    r_banco = p_banco = 0
    try:
        for nome, funcao in DO_BANCO:
            bancos = {c: json.loads(t) for c, t in originais.items()}
            funcao(bancos)
            for caminho, conteudo in bancos.items():
                with io.open(caminho, 'w', encoding='utf-8') as saida_arq:
                    json.dump(conteudo, saida_arq, ensure_ascii=False, indent=2)
                    saida_arq.write('\n')
            codigo, texto = roda_validador()
            so_o_novo = 'casamento' in texto.lower()
            if codigo != 0:
                r_banco += 1
                print('  reprovada  %-46s %s' % (
                    nome, 'pelo portao do casamento' if so_o_novo else 'por outro portao'))
            else:
                p_banco += 1
                print('  PASSOU !!  %-46s o validador nao mede isto' % nome)
    finally:
        for caminho, texto in originais.items():
            io.open(caminho, 'w', encoding='utf-8').write(texto)

    print('\n%d de %d reprovadas no BANCO | %d passaram' % (r_banco, len(DO_BANCO), p_banco))
    codigo, _ = roda_validador()
    print('banco restaurado: validador %s' % ('verde' if codigo == 0 else 'VERMELHO'))
    return 0 if (p_banco == 0 and codigo == 0) else 1


if __name__ == '__main__':
    sys.exit(main())

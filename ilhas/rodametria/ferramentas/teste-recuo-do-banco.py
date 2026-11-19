#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NENHUM ESCRITOR DO BANCO DIGITA O RECUO: TODOS O LEEM DA CONSTANTE (19/11/2026).

    python3 ferramentas/teste-recuo-do-banco.py

O DEFEITO MEDIDO, e ele nao estragou nenhum dado — estragou a LEITURA do que
mudou. `RECUO_DO_BANCO` mora em `coletar-por-consulta.py` e vale **1**. Em
18/11/2026 quem escreveu `dados/anuncios-por-consulta.json` foi a
`aplicar-foto-quebrada.py`, com `indent=2` digitado na linha dela — e o arquivo
ficou em disco com recuo 2. Na passada de 19/11, a primeira gravacao por outro
caminho devolveu o recuo para 1 e o diff saiu com **2.339 linhas inseridas e
2.111 removidas** para uma mudanca de **dez fotos**. A mudanca de verdade ficou
invisivel dentro do recuo.

Era CINCO declaracoes do mesmo numero: uma constante e quatro literais. A 20.7
ja tinha escrito a regra com outro assunto — *"duas declaracoes do mesmo fato
comecam iguais e so uma sobe"* — e o custo aqui e o mesmo do resumo verde: o
diff e onde uma pessoa LE o que a passada fez, e diff que afoga a mudanca em
recuo e portao que aprova sem medir.

A REGUA, E ELA VARRE EM VEZ DE LISTAR: todo arquivo de `ferramentas/` que grava
JSON com `json.dump(..., indent=...)` tem de passar um `indent` que venha da
constante — `RECUO_DO_BANCO`, `col.RECUO_DO_BANCO`, `coletor.RECUO_DO_BANCO` ou
`_recuo_do_banco()`. Literal numerico ali e DENUNCIADO. Varredura e nao lista,
pelo mesmo motivo que a `bancada.py` desta ilha descobre os portoes: lista
escrita a mao esquece o escritor de amanha, e o que ela esquece nao aparece em
lugar nenhum.
"""

import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

# A FONTE DO NUMERO, e ela e uma so.
FONTE = 'coletar-por-consulta.py'

# AS FORMAS ACEITAS DE LER A CONSTANTE. Nao e uma lista de excecao: e a lista do
# que CONTA como ler a fonte, e qualquer forma nova de a ler entra aqui numa
# linha — ao contrario de um literal, que entra sem pedir licenca a ninguem.
LEITURAS_DA_CONSTANTE = re.compile(r'(?:\w+\.)?RECUO_DO_BANCO|_recuo_do_banco\(\)')

# A EXPRESSAO ACEITA CHAMADA DE FUNCAO, e esta linha nasceu vermelha: a
# primeira versao parava no `(` de `_recuo_do_banco()` e capturava
# `_recuo_do_banco(`, entao a regua REPROVAVA a leitura certa da constante —
# o defeito que a propria 20.5 nomeia como o caminho mais curto para alguem
# passar a ignorar um portao.
DUMP = re.compile(r'json\.dump\s*\(.*?indent\s*=\s*([A-Za-z0-9_.]+(?:\(\))?)', re.S)


def main():
    afirmacoes = 0
    falhas = []

    def exigir(cond, texto):
        nonlocal afirmacoes
        afirmacoes += 1
        if not cond:
            falhas.append(texto)

    # --- a fonte existe e tem um valor so
    fonte = open(os.path.join(AQUI, FONTE), encoding='utf-8').read()
    declaracoes = re.findall(r'^RECUO_DO_BANCO\s*=\s*(\d+)', fonte, re.M)
    exigir(len(declaracoes) == 1,
           '`RECUO_DO_BANCO` aparece %d vez(es) em %s: zero ou mais de uma e espelho que '
           'adivinha a fonte' % (len(declaracoes), FONTE))

    # --- ninguem digita o numero
    escritores = 0
    for nome in sorted(os.listdir(AQUI)):
        if not nome.endswith('.py') or nome == os.path.basename(__file__):
            continue
        texto = open(os.path.join(AQUI, nome), encoding='utf-8').read()
        for bruto in DUMP.findall(texto):
            valor = bruto.strip()
            escritores += 1
            exigir(bool(LEITURAS_DA_CONSTANTE.search(valor)),
                   '%s grava JSON com `indent=%s`: o recuo tem de sair de `RECUO_DO_BANCO`, '
                   'senao o proximo diff afoga a mudanca em recuo' % (nome, valor))

    exigir(escritores >= 5,
           'a varredura achou %d gravacao(oes) de JSON em ferramentas/: eram 8 em 19/11/2026, '
           'e menos que 5 quer dizer que a expressao parou de casar — portao que nao acha nada '
           'passa verde sobre tudo' % escritores)

    # --- A MUTACAO COBRADA: a regua tem de REPROVAR o literal, e este e o
    #     literal exato que estava em `aplicar-foto-quebrada.py` em 18/11.
    afirmacoes += 1
    mundo_velho = 'json.dump(d, f, ensure_ascii=False, indent=2)'
    achado = DUMP.findall(mundo_velho)
    if not (achado and not LEITURAS_DA_CONSTANTE.search(achado[0])):
        falhas.append('a regua NAO reprova `indent=2` digitado: ela nao esta medindo nada')
    afirmacoes += 1
    mundo_novo = 'json.dump(d, f, ensure_ascii=False, indent=_recuo_do_banco())'
    achado = DUMP.findall(mundo_novo)
    if not (achado and LEITURAS_DA_CONSTANTE.search(achado[0])):
        falhas.append('a regua reprova a leitura CERTA da constante: regua que reprova o certo '
                      'e o caminho mais curto para alguem a ignorar')

    # --- e o arquivo em disco esta no recuo da constante, que e o fato que o
    #     defeito de 18/11 quebrou calado
    banco = os.path.join(os.path.dirname(AQUI), 'dados', 'anuncios-por-consulta.json')
    with open(banco, encoding='utf-8') as f:
        f.readline()
        segunda = f.readline()
    recuo = len(segunda) - len(segunda.lstrip(' '))
    exigir(recuo == int(declaracoes[0]) if declaracoes else False,
           'o banco em disco esta com recuo %d e a constante diz %s: a proxima gravacao vai '
           'reescrever o arquivo inteiro' % (recuo, declaracoes[0] if declaracoes else '?'))

    print('%d escritor(es) de JSON varrido(s) em ferramentas/.' % escritores)
    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO da lista de consultas de produto, sobre o arquivo de verdade.

Sem rede. Le `dados/consultas-de-produto.json`, roda a regua inteira sobre ele e
confere que `dados/consultas-de-produto.md` e EXATAMENTE o que a regua gera a
partir do JSON — `.md` editado a mao fica vermelho.

    python3 ferramentas/validar-consultas-de-produto.py

Codigo de saida 0 = verde. Qualquer outra coisa e reprovacao com o motivo escrito.
"""
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
JSON = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')
MD = os.path.join(RAIZ, 'dados', 'consultas-de-produto.md')
DADOS = os.path.join(RAIZ, 'dados')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    regua = carregar('regua-consultas-de-produto.py')
    falhas = []

    if not os.path.exists(JSON):
        print('REPROVADO: %s nao existe' % JSON)
        return 1
    with open(JSON, encoding='utf-8') as f:
        dados = json.load(f)

    # O `.md` e derivado. Se ele divergir do que a regua gera, alguem editou a
    # mao — e a lista passa a ter duas fontes que vao envelhecer em direcoes
    # diferentes, que e a doenca que esta ilha mais paga. A comparacao mora na
    # regua, em `erros_do_arquivo`, junto com todo o resto: aqui so se le o
    # disco, para as `mutacoes-...py` medirem o MESMO codigo que este portao.
    if not os.path.exists(MD):
        falhas.append('dados/consultas-de-produto.md nao existe; rode o gerador')
        falhas += regua.erros_do_arquivo(dados, None, DADOS)
    else:
        with open(MD, encoding='utf-8') as f:
            falhas += regua.erros_do_arquivo(dados, f.read(), DADOS)

    if falhas:
        print('REPROVADO — %d afirmacao(oes) quebrada(s):' % len(falhas))
        for f_ in falhas:
            print('  - %s' % f_)
        return 1

    consultas = dados['consultas']
    tomadas = sum(1 for c in consultas if regua.veredito(c) == 'tomada')
    nascem = sum(1 for c in consultas if regua.nasce_agora(c)[0])
    ocupantes = sum(len(c['ocupantes']) for c in consultas)
    fora = sum(1 for c in consultas for o in c['ocupantes'] if o['classe'] == regua.CLASSE_FORA)
    print('APROVADO: %d consultas, %d com veredito `tomada` afirmado, %d nao medidas, '
          '%d nascem agora, %d ocupantes com URL (%d fora do Brasil), e o `.md` bate com o JSON.' % (
              len(consultas), tomadas, len(consultas) - tomadas, nascem, ocupantes, fora))
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve `dados/prospeccao-widget.md` a partir de `dados/prospeccao-widget.json`.

Producao, nao portao. A regua e o texto moram em `ferramentas/regua-prospeccao.py`
— aqui so tem leitura, escrita e a contagem que vai para a tela. Duas fontes para
o mesmo fato divergem; entao o `.md` nao se escreve a mao, e o
`validar-prospeccao.py` regera este mesmo texto e compara.

    python3 ferramentas/gerar-prospeccao.py
"""
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
JSON = os.path.join(RAIZ, 'dados', 'prospeccao-widget.json')
MD = os.path.join(RAIZ, 'dados', 'prospeccao-widget.md')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    regua = carregar('regua-prospeccao.py')
    with open(JSON, encoding='utf-8') as f:
        dados = json.load(f)
    texto = regua.render_md(dados)
    with open(MD, 'w', encoding='utf-8') as f:
        f.write(texto)
    porniv = {}
    for c in dados['candidatos']:
        porniv[c['prioridade']] = porniv.get(c['prioridade'], 0) + 1
    print('dados/prospeccao-widget.md escrito: %d candidatos (P1 %d, P2 %d, P3 %d), %d ocupantes da SERP.' % (
        len(dados['candidatos']), porniv.get(1, 0), porniv.get(2, 0), porniv.get(3, 0),
        len(dados['ocupantes_da_serp_de_calculadora'])))
    return 0


if __name__ == '__main__':
    sys.exit(main())

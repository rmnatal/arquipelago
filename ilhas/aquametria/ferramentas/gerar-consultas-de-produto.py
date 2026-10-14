#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve `dados/consultas-de-produto.md` a partir de `dados/consultas-de-produto.json`.

Producao, nao portao. A regua e o texto moram em
`ferramentas/regua-consultas-de-produto.py` — aqui so tem leitura, escrita e a
contagem que vai para a tela. Duas fontes para o mesmo fato divergem; entao o
`.md` nao se escreve a mao, e o `validar-consultas-de-produto.py` regera este
mesmo texto e compara.

    python3 ferramentas/gerar-consultas-de-produto.py
"""
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
JSON = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')
MD = os.path.join(RAIZ, 'dados', 'consultas-de-produto.md')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    regua = carregar('regua-consultas-de-produto.py')
    with open(JSON, encoding='utf-8') as f:
        dados = json.load(f)
    texto = regua.render_md(dados)
    with open(MD, 'w', encoding='utf-8') as f:
        f.write(texto)
    consultas = dados['consultas']
    tomadas = [c for c in consultas if regua.veredito(c) == 'tomada']
    nascem = [c for c in consultas if regua.nasce_agora(c)[0]]
    ocupantes = sum(len(c.get('ocupantes', [])) for c in consultas)
    fora = sum(1 for c in consultas for o in c.get('ocupantes', [])
               if o.get('classe') == regua.CLASSE_FORA)
    print('dados/consultas-de-produto.md escrito: %d consultas (%d tomada, %d nao medida), '
          '%d nascem agora, %d ocupantes de SERP (%d fora do Brasil).' % (
              len(consultas), len(tomadas), len(consultas) - len(tomadas),
              len(nascem), ocupantes, fora))
    return 0


if __name__ == '__main__':
    sys.exit(main())

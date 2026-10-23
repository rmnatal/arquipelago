#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/prospeccao-widget.md a partir da referencia do bloco 6.

    python3 ferramentas/gerar-prospeccao.py           # grava
    python3 ferramentas/gerar-prospeccao.py --conferir # so diz se o arquivo esta igual

O arquivo de leitura e GERADO e nunca editado a mao: quem edita a mao escreve
uma verdade que o banco nao sustenta, e no dia seguinte as duas discordam sem
ninguem notar. O portao `validar-prospeccao.py` regera e compara byte a byte.
Mesmo desenho dos gerar-f1/f2/f3 e do gerar-artigos desta ilha.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "prospeccao_referencia",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "prospeccao-referencia.py"),
)
ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ref)

DESTINO = os.path.join(ref.RAIZ, "dados", "prospeccao-widget.md")


def gerar():
    banco, experiencias = ref.carregar()
    return ref.texto(banco, ref.estado_do_banco(experiencias))


def main(argv):
    novo = gerar()
    if "--conferir" in argv:
        if not os.path.exists(DESTINO):
            print("FALTA: %s nao existe" % DESTINO)
            return 1
        with open(DESTINO, encoding="utf-8") as f:
            atual = f.read()
        if atual != novo:
            print("DIFERENTE: %s nao e o que a referencia gera agora" % DESTINO)
            return 1
        print("IGUAL: %s esta identico ao que a referencia gera" % DESTINO)
        return 0

    with open(DESTINO, "w", encoding="utf-8") as f:
        f.write(novo)
    print("gravado: %s (%d linhas)" % (DESTINO, novo.count("\n")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

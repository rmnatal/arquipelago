#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ESCREVE `dados/prospeccao-widget.md` a partir de `dados/prospeccao-widget.json`.

    python3 ferramentas/gerar-prospeccao.py              # escreve
    python3 ferramentas/gerar-prospeccao.py --conferir   # nao escreve; so diz se bate

A REGUA NAO MORA AQUI. Ela mora em `validar-prospeccao.py` e e importada — uma
fonte so. Regua escrita duas vezes erra em um dos lados, e o lado errado fica
verde; esta ilha pagou isso em 30/10/2026, quando `gerar-f2.py --conferir`
reprovava a pagina CERTA porque o selo `gerado_em` saia do relogio da execucao.
Por isso este gerador NAO tem data propria: tudo o que ele imprime sai do JSON.
"""

import importlib.util
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent

# O nome do portao tem hifen, entao nao da `import` direto.
_spec = importlib.util.spec_from_file_location("regua", AQUI / "validar-prospeccao.py")
_regua = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_regua)

ARQUIVO_JSON = RAIZ / "dados" / "prospeccao-widget.json"
ARQUIVO_MD = RAIZ / "dados" / "prospeccao-widget.md"


def main(argv):
    if not ARQUIVO_JSON.exists():
        print("FALHA: %s nao existe" % ARQUIVO_JSON)
        print("REPROVADO")
        return 1
    dados = json.loads(ARQUIVO_JSON.read_text(encoding="utf-8"))
    novo = _regua.render_md(dados)

    if "--conferir" in argv:
        # O veredito sai em portugues e com a palavra que a `bancada.py` desta
        # ilha procura: portao que nao diz APROVADO/REPROVADO ela chama de
        # INERTE, e esta de proposito — portao cujo texto discorda do codigo
        # de saida e pior que portao nenhum.
        if not ARQUIVO_MD.exists():
            print("FALHA: %s nao existe" % ARQUIVO_MD.name)
            print("REPROVADO")
            return 1
        velho = ARQUIVO_MD.read_text(encoding="utf-8")
        if velho != novo:
            print("FALHA: %s nao bate com o que o JSON gera" % ARQUIVO_MD.name)
            print("  no arquivo: %d caracteres · gerado agora: %d" % (len(velho), len(novo)))
            print("REPROVADO")
            return 1
        print("%s bate com o JSON (%d caracteres)" % (ARQUIVO_MD.name, len(novo)))
        print("APROVADO")
        return 0

    antes = ARQUIVO_MD.read_text(encoding="utf-8") if ARQUIVO_MD.exists() else None
    ARQUIVO_MD.write_text(novo, encoding="utf-8")
    if antes is None:
        print("escrito %s (%d caracteres, do zero)" % (ARQUIVO_MD.name, len(novo)))
    elif antes == novo:
        print("%s inalterado (%d caracteres)" % (ARQUIVO_MD.name, len(novo)))
    else:
        print("reescrito %s: %d -> %d caracteres" % (ARQUIVO_MD.name, len(antes), len(novo)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

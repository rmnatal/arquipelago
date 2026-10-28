#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A bancada desta ilha — um comando so, e ela DESCOBRE os portoes em vez de os listar.

    python3 ferramentas/bancada.py            # os portoes que rodam sem rede
    python3 ferramentas/bancada.py --no-ar    # mais os que abrem o site
    python3 ferramentas/bancada.py --lista    # so imprime o que rodaria

NAO TEM LISTA. Ela varre ferramentas/ e classifica pela convencao de nome, entao portao novo
entra na bancada no DIA em que e escrito, sem ninguem se lembrar dele:

    validar-*   mutacoes-*  teste-*  testar-*   -> sem rede
    conferir-*  medir-*                         -> so com --no-ar
    derivar-*  gerar-*  coletar-*  aplicar-*    -> ESCREVEM, nao sao portao; rodam com --conferir
                                                   quando aceitam, e sao DENUNCIADOS quando nao

Arquivo que nao casa com convencao nenhuma e DENUNCIADO em vez de ignorado, e portao cujo texto
discorda do codigo de saida e chamado de INERTE (imprime REPROVADO e sai 0, ou o contrario).
Esta ilha nasceu com a bancada porque a licao mais cara da Robometria nao foi uma regua errada:
foi uma regua certa que nunca rodou — "a regua existia desde 14/09 e nao tinha falhado: nao
tinha rodado". Lista de bancada escrita de cabeca esquece, e o que ela esquece nao aparece em
lugar nenhum, porque o verde das outras ocupa o espaco do que faltou.
"""
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent

SEM_REDE = ("validar-", "mutacoes-", "teste-", "testar-")
COM_REDE = ("conferir-", "medir-")
ESCREVEM = ("derivar-", "gerar-", "coletar-", "aplicar-", "atualizar-")
NAO_E_PORTAO = {"bancada.py"}


def classificar():
    sem, com, escrevem, denunciados = [], [], [], []
    for f in sorted(AQUI.iterdir()):
        if not f.is_file() or f.name.startswith(".") or f.name in NAO_E_PORTAO:
            continue
        if f.suffix not in (".py", ".mjs", ".php"):
            denunciados.append((f.name, "extensao %r nao e de portao desta bancada" % f.suffix))
            continue
        if f.name.startswith(SEM_REDE):
            sem.append(f)
        elif f.name.startswith(COM_REDE):
            com.append(f)
        elif f.name.startswith(ESCREVEM):
            escrevem.append(f)
        else:
            denunciados.append((f.name, "nao casa com convencao nenhuma de nome. Ou ele e portao e "
                                        "precisa do prefixo, ou nao e e precisa estar fora de "
                                        "ferramentas/ — silencio aqui e portao que nunca roda"))
    return sem, com, escrevem, denunciados


def rodar(caminho, args=()):
    if caminho.suffix == ".py":
        cmd = [sys.executable, str(caminho)] + list(args)
    elif caminho.suffix == ".mjs":
        cmd = ["node", str(caminho)] + list(args)
    else:
        cmd = ["php", str(caminho)] + list(args)
    r = subprocess.run(cmd, cwd=str(RAIZ), capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def veredito_do_texto(saida):
    """O que o portao DIZ. None quando ele nao diz nada de que esta bancada entenda."""
    if re.search(r"\bREPROVADO\b", saida):
        return False
    if re.search(r"\bAPROVADO\b", saida):
        return True
    m = re.search(r"(\d+)\s+falha\(s\)", saida)
    if m:
        return int(m.group(1)) == 0
    return None


def main():
    no_ar = "--no-ar" in sys.argv
    sem, com, escrevem, denunciados = classificar()
    fila = [(f, ()) for f in sem]
    if no_ar:
        fila += [(f, ()) for f in com]
    fila += [(f, ("--conferir",)) for f in escrevem]

    if "--lista" in sys.argv:
        for f, args in fila:
            print("  %s %s" % (f.name, " ".join(args)))
        for nome, por_que in denunciados:
            print("  DENUNCIADO %s — %s" % (nome, por_que))
        print("")
        print("%d portao(oes) na fila%s, %d denunciado(s)."
              % (len(fila), "" if no_ar else " (sem os de rede; use --no-ar)", len(denunciados)))
        return 0

    problemas = []
    for nome, por_que in denunciados:
        problemas.append("DENUNCIADO %s — %s" % (nome, por_que))

    for f, args in fila:
        codigo, saida = rodar(f, args)
        diz = veredito_do_texto(saida)
        rotulo = "%s %s" % (f.name, " ".join(args))
        if diz is None:
            problemas.append("INERTE %s — nao imprime APROVADO, REPROVADO nem 'N falha(s)'. "
                             "Portao que nao diz o veredito em portugues nao e lido por ninguem."
                             % rotulo)
            continue
        if diz != (codigo == 0):
            problemas.append("INERTE %s — o texto diz %s e o codigo de saida diz %s. As duas metades "
                             "do veredito tem de concordar."
                             % (rotulo, "APROVADO" if diz else "REPROVADO",
                                "APROVADO" if codigo == 0 else "REPROVADO"))
            continue
        print("%-7s %s" % ("ok" if codigo == 0 else "FALHOU", rotulo))
        if codigo != 0:
            problemas.append("FALHOU %s" % rotulo)
            for linha in saida.strip().splitlines()[-12:]:
                print("        %s" % linha)

    print("")
    for p in problemas:
        print(p)
    print("")
    print("%d portao(oes) rodado(s)%s." % (len(fila), "" if no_ar else " sem rede"))
    print("%d falha(s)." % len(problemas))
    print("APROVADO" if not problemas else "REPROVADO")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())

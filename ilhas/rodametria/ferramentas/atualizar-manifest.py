#!/usr/bin/env python3
"""
ATUALIZA O manifest.json DESTA ILHA — e IMPRIME CADA TROCA QUE FAZ.

Por que imprimir: a secao 8 do ARQUIPELAGO.md registra a cicatriz da Aquametria
de 11/09/2026, em que "a ferramenta que atualiza o manifest so recalculava
sha256: o `titulo` NUNCA era reespelhado", e o resultado foi o corpo de nove
paginas trocando no ar e os nove titulos nao. A regra que saiu de la e literal:
"a ferramenta que espelha um campo de uma fonte para outra imprime cada troca
que fez, senao o espelho envelhece calado".

A REVISAO SOBE SOZINHA quando algum sha256 muda, e nunca e digitada: revisao
digitada e a familia do numero de tela digitado.

    python3 ferramentas/atualizar-manifest.py            # escreve
    python3 ferramentas/atualizar-manifest.py --conferir  # nao escreve; falha se divergir
"""

import hashlib
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
MANIFEST = os.path.join(ILHA, "manifest.json")


def sha(rel):
    with open(os.path.join(ILHA, rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    conferir = "--conferir" in sys.argv
    m = json.load(open(MANIFEST, encoding="utf-8"))
    trocas = []
    revisao_antiga = int(m.get("revisao", 0))

    for grupo in ("snippets", "conteudo", "dados"):
        for item in m.get(grupo, []):
            rel = item["arquivo"]
            caminho = os.path.join(ILHA, rel)
            if not os.path.exists(caminho):
                trocas.append("AUSENTE  %s:%s -> %s nao existe no repositorio"
                              % (grupo, item["id"], rel))
                continue
            novo = sha(rel)
            if item.get("sha256") != novo:
                trocas.append("sha256   %s:%s  %s -> %s"
                              % (grupo, item["id"],
                                 (item.get("sha256") or "(vazio)")[:12], novo[:12]))
                item["sha256"] = novo

    if trocas:
        m["revisao"] = revisao_antiga + 1
        trocas.append("revisao  %d -> %d" % (revisao_antiga, m["revisao"]))

    ausentes = [t for t in trocas if t.startswith("AUSENTE")]
    texto = json.dumps(m, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        atual = open(MANIFEST, encoding="utf-8").read()
        if trocas or atual != texto:
            print("REPROVADO: o manifest nao bate com os arquivos do repositorio.")
            for t in trocas:
                print("  " + t)
            return 1
        print("APROVADO: manifest em dia, revisao %d." % m["revisao"])
        return 0

    if not trocas:
        print("nada a trocar; revisao %d." % m["revisao"])
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write(texto)
    print("manifest atualizado:")
    for t in trocas:
        print("  " + t)

    return 1 if ausentes else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preenche os campos DERIVADOS do banco da Rodametria. Hoje e um so: `energia_wh`.

    python3 ferramentas/derivar-banco.py            # escreve
    python3 ferramentas/derivar-banco.py --conferir # nao escreve; sai 1 se houver o que escrever

Por que isto e um programa e nao uma coluna digitada: `energia_wh` e IDENTIDADE (Wh = V x Ah,
constante `energia-wh-tensao-vezes-amperagem`), e numero de identidade digitado a mao e numero
que vai divergir da conta um dia, sem ninguem ver. Quem escreve o campo e este arquivo; quem
confere e ferramentas/validar-banco.py, que recalcula e reprova divergencia. Sao duas metades
e elas nao se falam por acaso: a segunda existe para discordar da primeira.

O FATOR NUNCA VEM DAQUI. A relacao sai de dados/constantes.json, pelo id da constante, e o
programa PARA se a constante nao estiver `publicavel` — literal numerico de conversao dentro
deste arquivo seria a mesma doenca que a 1.3 da especificacao proibe na F1.
"""
import json
import sys
from pathlib import Path

ID_CONSTANTE = "energia-wh-tensao-vezes-amperagem"
RAIZ = Path(__file__).resolve().parent.parent


def constante_publicavel():
    const = json.loads((RAIZ / "dados/constantes.json").read_text(encoding="utf-8"))
    for c in const.get("constantes", []):
        if c.get("id") == ID_CONSTANTE:
            return c
    return None


def main():
    conferir = "--conferir" in sys.argv
    c = constante_publicavel()
    if c is None:
        print("PAROU: a constante `%s` nao existe em dados/constantes.json. Este programa nao "
              "carrega a relacao Wh = V x Ah dentro de si de proposito." % ID_CONSTANTE)
        return 1
    if c.get("status") != "publicavel":
        print("PAROU: a constante `%s` esta em %r. A secao 10 do ARQUIPELAGO.md proibe constante "
              "`pendente` dentro de formula publicada." % (ID_CONSTANTE, c.get("status")))
        return 1

    alvo = RAIZ / "dados/veiculos.json"
    d = json.loads(alvo.read_text(encoding="utf-8"))
    mudou, zerados = [], []
    for v in d.get("registros", []):
        tv = (v.get("tensao_v") or {}).get("valor")
        ah = (v.get("amperagem_ah") or {}).get("valor")
        atual = (v.get("energia_wh") or {}).get("valor")
        if tv is None or ah is None:
            if atual is not None:
                v["energia_wh"] = {
                    "valor": None,
                    "motivo": "nao derivavel: falta tensao_v ou amperagem_ah. Wh copiado de anuncio e "
                              "proibido pelo esquema — o declarado vai para divergencias[].",
                }
                zerados.append(v["id"])
            continue
        novo = round(tv * ah)
        if atual != novo or not (v.get("energia_wh") or {}).get("derivado_de"):
            v["energia_wh"] = {
                "valor": novo,
                "unidade": "Wh",
                "derivado": True,
                "derivado_de": "tensao_v x amperagem_ah",
                "constante": ID_CONSTANTE,
                "conta": "%s V x %s Ah = %s Wh" % (tv, ah, novo),
                "fonte": None,
                "motivo_sem_fonte": "identidade matematica: vale por definicao de unidade e nao depende "
                                    "de fonte. As fontes sao as dos dois lados da conta (tensao_v e "
                                    "amperagem_ah), cada uma com a sua.",
            }
            mudou.append("%s -> %s Wh" % (v["id"], novo))

    if conferir:
        if mudou or zerados:
            print("REPROVADO: %d derivado(s) a escrever e %d a zerar." % (len(mudou), len(zerados)))
            for m in mudou:
                print("  a escrever: %s" % m)
            for z in zerados:
                print("  a zerar:    %s" % z)
            return 1
        print("0 falha(s).")
        print("APROVADO: todo `energia_wh` do banco bate com V x Ah.")
        return 0

    if mudou or zerados:
        alvo.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    for m in mudou:
        print("escrito: %s" % m)
    for z in zerados:
        print("zerado:  %s" % z)
    print("%d derivado(s) escrito(s), %d zerado(s)." % (len(mudou), len(zerados)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

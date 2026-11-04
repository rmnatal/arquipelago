#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preenche os campos DERIVADOS do banco da Rodametria: `energia_wh` e `afiliado.intestavel`.

    python3 ferramentas/derivar-banco.py            # escreve
    python3 ferramentas/derivar-banco.py --conferir # nao escreve; sai 1 se houver o que escrever

Por que isto e um programa e nao uma coluna digitada: `energia_wh` e IDENTIDADE (Wh = V x Ah,
constante `energia-wh-tensao-vezes-amperagem`), e numero de identidade digitado a mao e numero
que vai divergir da conta um dia, sem ninguem ver. Quem escreve o campo e este arquivo; quem
confere e ferramentas/validar-banco.py, que recalcula e reprova divergencia. Sao duas metades
e elas nao se falam por acaso: a segunda existe para discordar da primeira.

O SEGUNDO DERIVADO NASCEU EM 04/11/2026, pelo item 4 do despacho da ronda daquele
dia: `afiliado.intestavel` estava AUSENTE nos 17 registros de `veiculos.json` e nos
3 de `pecas.json`. A 25.9 (item 2) diz, com todas as letras, que campo declarado em
todo registro existe "pela mesma razao do `intestavel`" — e nesta ilha o `intestavel`
era justamente o que nao estava declarado em lugar nenhum. O validador o RECALCULAVA
de cabeca numa variavel local (`bool(url) and not url_produto`), entao a ronda que
media "0 intestavel" nesta ilha estava medindo a AUSENCIA DA CHAVE, nao a saude dos
itens. Hoje nao esconde nada — os 20 derivam `false` —, e e por isso que entra agora:
campo ausente que se comporta como o valor certo espera o dia em que o valor certo
muda, e nesse dia nenhum portao acusa.

O QUE ELE SIGNIFICA, e e a 25.4-b literal: item com link de ficha (`url`) e sem o par
cru (`url_produto`) e "um link cuja saude e desconhecida e PERMANECERA desconhecida",
porque a 25.4 proibe clicar no proprio link de afiliado para conferir. Item de degrau
4, que nao tem ficha nenhuma e vive do piso de busca, nao e intestavel: nao ha ficha
para testar, e a busca nao esgota.

E POR QUE DUAS DECLARACOES DO MESMO FATO, se a 20.7 avisa que "duas declaracoes do
mesmo fato comecam iguais e so uma sobe": porque aqui elas NAO sao duas declaracoes,
sao um espelho e um portao. Esta ferramenta escreve; `validar-banco.py` RECALCULA e
reprova divergencia — exatamente como ja faz com `energia_wh`. Espelho sem portao
envelhece calado; portao sem espelho obriga toda ronda a refazer a conta de cabeca.

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
    intestaveis = []
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

    # `afiliado.intestavel` — nos DOIS bancos que tem a chave `afiliado`.
    bancos = [(alvo, d)]
    pecas_caminho = RAIZ / "dados/pecas.json"
    pecas = json.loads(pecas_caminho.read_text(encoding="utf-8"))
    bancos.append((pecas_caminho, pecas))
    for caminho, banco in bancos:
        for r in banco.get("registros", []):
            af = r.get("afiliado")
            if not isinstance(af, dict):
                continue
            novo = bool(af.get("url")) and not af.get("url_produto")
            if af.get("intestavel") != novo or "intestavel" not in af:
                af["intestavel"] = novo
                intestaveis.append("%s:%s -> %s"
                                   % (caminho.name, r.get("id"), "true" if novo else "false"))
            else:
                af["intestavel"] = novo

    if conferir:
        if mudou or zerados or intestaveis:
            print("REPROVADO: %d derivado(s) a escrever, %d a zerar e %d `intestavel` a espelhar."
                  % (len(mudou), len(zerados), len(intestaveis)))
            for m in mudou:
                print("  a escrever: %s" % m)
            for z in zerados:
                print("  a zerar:    %s" % z)
            for i in intestaveis:
                print("  intestavel: %s" % i)
            return 1
        print("0 falha(s).")
        print("APROVADO: todo `energia_wh` bate com V x Ah e todo `afiliado.intestavel` bate "
              "com a regra da 25.4-b.")
        return 0

    if mudou or zerados or intestaveis:
        # A NOVA-LINHA FINAL E PARTE DO ARQUIVO: sem ela, todo commit desta
        # ferramenta carrega um "\ No newline at end of file" que nao e dela.
        alvo.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        if any(c.name == "pecas.json" for c, _ in bancos):
            pecas_caminho.write_text(json.dumps(pecas, ensure_ascii=False, indent=1) + "\n",
                                     encoding="utf-8")
    for m in mudou:
        print("escrito: %s" % m)
    for z in zerados:
        print("zerado:  %s" % z)
    for i in intestaveis:
        print("espelhado: %s" % i)
    print("%d derivado(s) escrito(s), %d zerado(s), %d `intestavel` espelhado(s)."
          % (len(mudou), len(zerados), len(intestaveis)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

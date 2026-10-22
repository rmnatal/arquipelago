#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/f3-respostas.json: o dominio de resposta da F3.

    python3 ferramentas/gerar-f3.py             # relatorio na tela
    python3 ferramentas/gerar-f3.py --gravar    # grava o arquivo

O que o arquivo e: a TABELA PRE-RENDERIZADA da F3 -- os casos resolvidos que uma
superficie de IA le sem preencher formulario nenhum -- mais TODAS as bordas, que
sao as recusas duras. Cada frase ja sai acentuada, do jeito que o visitante le.

`publicar: false` HOJE, e o motivo nao e qualidade do arquivo: esta ilha nao tem
WordPress, nao tem Sync e nao tem /status, e o dominio dela nao esta na lista de
dominios liberados deste ambiente. Nao existe "no ar" para onde publicar, e dizer
que publiquei seria inventar.

E O ARQUIVO JA REGISTRA O QUE A F3 AINDA NAO PODE RESPONDER. Com ZERO passes e
ZERO coberturas no banco, TODO estado valido fecha com a recusa `sem_passe_lido`:
a F3 publica a soma dos avulsos, que e metade da pergunta, e diz que a outra
metade nao foi lida. A contagem `recusas_por_codigo` deste arquivo e o que mostra
o progresso sem ninguem precisar acreditar em mim -- o dia em que o primeiro passe
for carregado, essa linha cai.

POR QUE O ARQUIVO NAO TRAZ TODO O DOMINIO: a mesma decisao da F2, por um motivo
que aqui e mais forte. O dominio da F3 cresce em 2^n - 1 com o numero de atracoes
LIDAS numa cidade: hoje sao 4 cidades com 1 atracao cada e 1.038 estados; com 8
atracoes numa cidade so, seriam 255 subconjuntos x 252 combinacoes de dias e
pessoas, so nela. A prova da grade inteira mora no portao, que a varre em cada
passada com a aritmetica refeita a mao; o arquivo carrega o que a pagina le.
"""

import importlib.util
import io
import json
import os
import sys
from decimal import Decimal

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
SAIDA = os.path.join(BASE, "dados", "f3-respostas.json")


def _referencia():
    """Carrega a referencia PELO CAMINHO, nunca uma copia."""
    caminho = os.path.join(AQUI, "f3-referencia.py")
    spec = importlib.util.spec_from_file_location("f3_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _json_seguro(no):
    """Decimal vira TEXTO exato, nunca float.

    Virar float aqui perderia o centavo exato que a ferramenta inteira existe para
    nao perder, e seria uma perda que nenhum portao veria: float de dinheiro quase
    sempre imprime igual.
    """
    if isinstance(no, Decimal):
        return str(no)
    if isinstance(no, dict):
        return {k: _json_seguro(v) for k, v in no.items()}
    if isinstance(no, (list, tuple)):
        return [_json_seguro(v) for v in no]
    return no


def montar(f3, banco=None, esquema=None, constantes=None, hoje=None):
    """O documento inteiro. Aceita banco/esquema/constantes EM MEMORIA porque e assim
    que a bateria de mutacoes gera o dominio de um mundo mutado sem gravar nada em
    disco."""
    banco = banco if banco is not None else f3.carregar_banco()
    esquema = esquema if esquema is not None else f3.carregar_esquema()
    constantes = constantes if constantes is not None else f3.carregar_constantes()

    todas = f3.todas_as_respostas(banco, esquema, constantes, hoje)
    tabela = f3.tabela_pre_renderizada(banco, esquema, constantes, hoje)

    com_conta = [r for r in todas if r["recusa_dura"] is None]
    recusadas = [r for r in todas if r["recusa_dura"] is not None]

    # O QUE ENTRA NO ARQUIVO: a grade da tabela e TODAS as bordas. As bordas entram
    # inteiras de proposito — grade que nao pisa na borda e amostra com nome de grade,
    # e as recusas duras sao justamente onde a conta NAO acontece.
    da_tabela = set()
    for cidade in (banco.get("cidades") or []):
        atracoes = [e.get("id") for e in f3.atracoes_da_cidade(banco, cidade.get("id"))]
        if not atracoes:
            continue
        for escolha in f3.subconjuntos(atracoes[:f3.ATRACOES_MAXIMO]):
            for dias in f3.DIAS_DA_TABELA:
                for pessoas in f3.PESSOAS_DA_TABELA:
                    da_tabela.add((cidade.get("id"), escolha, dias, pessoas))
    respostas = []
    for r in todas:
        e = r["estado"]
        chave = (e["cidade"], tuple(e["atracoes"]), e["dias"], e["pessoas"])
        if r["recusa_dura"] is not None or chave in da_tabela:
            respostas.append(r)

    # Toda contagem sai do que foi gerado, nunca digitada.
    recusas_por_codigo = {}
    for r in com_conta:
        for rec in r["recusas"]:
            recusas_por_codigo[rec["codigo"]] = recusas_por_codigo.get(rec["codigo"], 0) + 1
    duras_por_codigo = {}
    for r in recusadas:
        c = r["recusa_dura"]["codigo"]
        duras_por_codigo[c] = duras_por_codigo.get(c, 0) + 1
    vereditos = {}
    for r in com_conta:
        for bloco in r["passes"]:
            for versao in bloco["versoes"]:
                chave = versao["veredito"] or "sem_veredito"
                vereditos[chave] = vereditos.get(chave, 0) + 1

    passes_no_banco = sum(1 for e in (banco.get("experiencias") or [])
                          if e.get("categoria") == f3.f2.CATEGORIA_DE_PASSE)

    doc = {
        "ilha": "jornadafly",
        "ferramenta": "F3",
        "bloco": 5,
        "versao": 1,
        "publicar": False,
        "motivo_publicar_false": (
            "Esta ilha nao tem WordPress, nao tem Sync e nao tem /status, e o dominio nao "
            "esta na lista de dominios liberados deste ambiente (remedido em 22/10/2026: "
            "recusa do tunel em seis medicoes, com as duas ilhas de controle em 200). Nao "
            "existe 'no ar' para onde publicar, e dizer que publiquei seria inventar."),
        "cumpre": "dados/especificacao-calculadoras.md, secao 4 (F3)",
        "le_de": ["dados/experiencias.json", "dados/esquema-banco.json",
                  "dados/constantes.json"],
        "gerado_por": "ferramentas/gerar-f3.py, a partir de ferramentas/f3-referencia.py",
        "uma_procedencia_so_e_tres_leituras": (
            "Diferente da F2, nao ha numero de terceiro NENHUM nesta ferramenta: o preco "
            "de cada atracao, o preco de cada passe e a cobertura de cada passe foram "
            "lidos na fonte de quem opera ou de quem fixa a tarifa. O que a tela separa "
            "sao TRES LEITURAS que envelhecem em velocidades diferentes, e a cobertura e a "
            "que envelhece primeiro: e ela que muda quando um passe troca a regra de "
            "reserva, e foi isso que o bloco 1 mediu em 14/09/2026 na fonte de topo do "
            "Roma Pass."),
        "as_tres_regras_da_cobertura": (
            (esquema.get("regra_da_cobertura_do_passe") or {}).get("as_tres_regras")),
        "acentuacao": (
            "Toda frase deste arquivo e destinada a TELA e por isso sai ACENTUADA, e a "
            "concordancia tambem: a primeira versao desta ferramenta publicou «1 atracao "
            "em Veneza CUSTAM» e «dentro das 1 atracao», e foi a leitura da frase que viu "
            "— a terceira vez que esta pasta paga a concordancia."),
        "por_que_o_arquivo_nao_traz_todos_os_estados": (
            "A F3 serve %d estados e este arquivo grava %d: a grade da tabela "
            "pre-renderizada mais TODAS as bordas. Os %d estados sao varridos em cada "
            "passada do portao (ferramentas/teste-f3.py), com a aritmetica refeita a mao "
            "em Fraction, e e la que a grade inteira e provada — nao aqui. O dominio desta "
            "ferramenta cresce em 2^n - 1 com o numero de atracoes lidas numa cidade, "
            "entao gravar tudo seria pagar peso de repositorio por uma prova que nao esta "
            "no arquivo." % (len(todas), len(respostas), len(todas))),
        "resumo": {
            "cidades": len(banco.get("cidades") or []),
            "passes_no_banco": passes_no_banco,
            "coberturas_no_banco": len(banco.get("coberturas_de_passe") or []),
            "estados": len(todas),
            "estados_gravados": len(respostas),
            "estados_com_conta": len(com_conta),
            "estados_recusados_na_borda": len(recusadas),
            "estados_com_soma_de_avulsos": sum(1 for r in com_conta
                                               if r["avulsos"] is not None),
            "estados_com_passe_lido": sum(1 for r in com_conta if r["passes"]),
            "estados_com_veredito": sum(
                1 for r in com_conta
                if any(v["veredito"] for b in r["passes"] for v in b["versoes"])),
            "linhas_da_tabela": len(tabela),
            "vereditos_por_codigo": vereditos,
            "recusas_por_codigo": recusas_por_codigo,
            "recusas_duras_por_codigo": duras_por_codigo,
        },
        "tabela_pre_renderizada": tabela,
        "respostas": respostas,
    }
    return _json_seguro(doc)


def main():
    f3 = _referencia()
    doc = montar(f3)
    r = doc["resumo"]
    print("F3 da JornadaFly — dominio de resposta")
    for chave, valor in r.items():
        if isinstance(valor, dict):
            print("  %s:" % chave.replace("_", " "))
            for k in sorted(valor):
                print("     %-42s %d" % (k, valor[k]))
        else:
            print("  %-36s %s" % (chave.replace("_", " "), valor))

    if "--gravar" in sys.argv[1:]:
        with io.open(SAIDA, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("\ngravado: %s (%d bytes)" % (SAIDA, os.path.getsize(SAIDA)))
    else:
        print("\n(nada gravado — rode com --gravar)")


if __name__ == "__main__":
    main()

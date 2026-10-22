#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/f1-respostas.json: o dominio de resposta INTEIRO da F1.

    python3 ferramentas/gerar-f1.py             # relatorio na tela
    python3 ferramentas/gerar-f1.py --gravar    # grava o arquivo

O que o arquivo e: as respostas da F1 para todo estado que ela serve -- cada versao
de cada experiencia do banco x cada numero de pessoas de 1 a 12, mais as DUAS
BORDAS (0 e 13), que sao as recusas duras --, cada uma ja em frase acentuada, mais a
TABELA PRE-RENDERIZADA da secao 5 do ARQUIPELAGO.md: os casos resolvidos que um
modelo de linguagem le sem preencher formulario nenhum.

`publicar: false` HOJE, e o motivo nao e qualidade do arquivo. Esta ilha nao tem
WordPress: nao ha `manifest.json`, nao ha Sync e nao ha `/status`, e o dominio nao
esta na lista de Dominios permitidos deste ambiente. Quando a casca nascer (bloco
3b, trabalho de navegador do Raphael), este arquivo entra no manifest e o snippet
PHP monta a pagina a partir dele -- e ate la dizer que ele esta no ar seria
inventar.

AS BORDAS ENTRAM NO ARQUIVO DE PROPOSITO. Grade que nao pisa na borda e amostra com
nome de grade (secao 8 do ARQUIPELAGO.md), e as duas recusas duras desta ferramenta
-- grupo de 0 e grupo de 13 -- sao justamente onde a conta NAO acontece. Um arquivo
que so trouxesse 1 a 12 deixaria a parte que recusa sem nenhum caso gravado.
"""

import importlib.util
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
SAIDA = os.path.join(BASE, "dados", "f1-respostas.json")


def _referencia():
    """Carrega a referencia PELO CAMINHO, nunca uma copia.

    O nome tem hifen (convencao das ilhas) e por isso nao e importavel por
    `import`. Carregar pelo caminho e o que garante que o arquivo gravado sai da
    MESMA regra que a bancada mede.
    """
    caminho = os.path.join(AQUI, "f1-referencia.py")
    spec = importlib.util.spec_from_file_location("f1_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def montar(f1, banco=None, esquema=None, constantes=None):
    """O documento inteiro. Aceita banco/esquema/constantes EM MEMORIA porque e assim
    que ferramentas/mutacoes-f1.py gera o dominio de um mundo mutado sem gravar nada
    em disco -- e sem gerar o dominio junto, toda mutacao reprovaria tambem na secao
    do portao que confere o arquivo gravado, e nenhuma provaria reprovar pela
    afirmacao que diz medir."""
    banco = banco if banco is not None else f1.carregar_banco()
    esquema = esquema if esquema is not None else f1.carregar_esquema()
    constantes = constantes if constantes is not None else f1.carregar_constantes()

    respostas = f1.todas_as_respostas(banco, esquema, constantes)
    tabela = f1.tabela_pre_renderizada(banco, esquema, constantes)

    com_conta = [r for r in respostas if r["recusa_dura"] is None]
    recusadas = [r for r in respostas if r["recusa_dura"] is not None]

    # Toda contagem sai do que foi gerado, nunca digitada (secao 8).
    recusas_por_codigo = {}
    for r in com_conta:
        for rec in r["recusas"]:
            recusas_por_codigo[rec["codigo"]] = recusas_por_codigo.get(rec["codigo"], 0) + 1
    duras_por_codigo = {}
    for r in recusadas:
        c = r["recusa_dura"]["codigo"]
        duras_por_codigo[c] = duras_por_codigo.get(c, 0) + 1

    escada_aplicavel = sum(1 for r in com_conta if r["escada"]["aplicavel"])

    return {
        "ilha": "jornadafly",
        "ferramenta": "F1",
        "bloco": 4,
        "versao": 1,
        "publicar": False,
        "motivo_publicar_false": (
            "Esta ilha nao tem WordPress, nao tem Sync e nao tem /status, e o dominio "
            "nao esta na lista de Dominios permitidos deste ambiente (remedido em "
            "22/10/2026: CONNECT tunnel failed, response 403). Nao existe 'no ar' para "
            "onde publicar, e dizer que publiquei seria inventar."),
        "cumpre": "dados/especificacao-calculadoras.md, secao 2 (F1)",
        "le_de": ["dados/experiencias.json", "dados/esquema-banco.json",
                  "dados/constantes.json"],
        "gerado_por": "ferramentas/gerar-f1.py, a partir de ferramentas/f1-referencia.py",
        "acentuacao": (
            "Toda frase deste arquivo e destinada a TELA e por isso sai ACENTUADA. E a "
            "cicatriz da Robometria, que publicou portugues sem acento, e ela foi "
            "cometida DENTRO desta ferramenta na primeira versao dela, em 22/10/2026: a "
            "F1 montava o rotulo da unidade com replace('_', ' ') e publicava 'por "
            "veiculo'. O portao ferramentas/teste-f1.py passou a medir acento em toda "
            "frase de todo estado, e e por isso que ele existe."),
        "resumo": {
            "experiencias": len(banco.get("experiencias") or []),
            "versoes": sum(len(e.get("versoes") or [])
                           for e in (banco.get("experiencias") or [])),
            "estados": len(respostas),
            "estados_com_conta": len(com_conta),
            "estados_recusados_na_borda": len(recusadas),
            "linhas_da_tabela": len(tabela),
            "estados_com_escada_aplicavel": escada_aplicavel,
            "recusas_por_codigo": recusas_por_codigo,
            "recusas_duras_por_codigo": duras_por_codigo,
        },
        "tabela_pre_renderizada": tabela,
        "respostas": respostas,
    }


def main():
    f1 = _referencia()
    doc = montar(f1)
    r = doc["resumo"]
    print("F1 da JornadaFly — dominio de resposta")
    for chave in ("experiencias", "versoes", "estados", "estados_com_conta",
                  "estados_recusados_na_borda", "linhas_da_tabela",
                  "estados_com_escada_aplicavel"):
        print("  %-30s %s" % (chave.replace("_", " "), r[chave]))
    print("  recusas por codigo:")
    for codigo in sorted(r["recusas_por_codigo"]):
        print("     %-38s %d" % (codigo, r["recusas_por_codigo"][codigo]))
    print("  recusas duras por codigo:")
    for codigo in sorted(r["recusas_duras_por_codigo"]):
        print("     %-38s %d" % (codigo, r["recusas_duras_por_codigo"][codigo]))

    if "--gravar" in sys.argv[1:]:
        with io.open(SAIDA, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("\ngravado: %s (%d bytes)" % (SAIDA, os.path.getsize(SAIDA)))
    else:
        print("\n(nada gravado — rode com --gravar)")


if __name__ == "__main__":
    main()

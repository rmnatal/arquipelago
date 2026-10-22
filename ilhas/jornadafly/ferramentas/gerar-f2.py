#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/f2-respostas.json: o dominio de resposta INTEIRO da F2.

    python3 ferramentas/gerar-f2.py             # relatorio na tela
    python3 ferramentas/gerar-f2.py --gravar    # grava o arquivo

O que o arquivo e: as respostas da F2 para todo estado que ela serve -- cada cidade
do banco x cada padrao x 1 a 21 dias x 1 a 12 pessoas, mais as bordas de fora, que
sao as recusas duras --, cada uma ja em frase acentuada, mais a TABELA
PRE-RENDERIZADA: os casos resolvidos que uma superficie de IA le sem preencher
formulario nenhum.

`publicar: false` HOJE, e o motivo nao e qualidade do arquivo: esta ilha nao tem
WordPress, nao tem Sync e nao tem /status, e o dominio dela nao esta na lista de
dominios liberados deste ambiente. Nao existe "no ar" para onde publicar, e dizer
que publiquei seria inventar.

E O ARQUIVO JA REGISTRA O QUE A F2 AINDA NAO PODE RESPONDER. Com zero faixas
diarias no banco, TRES das quatro linhas de toda resposta sao recusa -- e a recusa
entra no arquivo com o mesmo peso do numero, porque linha que nao sai e nao e
explicada e espaco em branco com cara de zero. O dia em que a primeira faixa for
carregada, a contagem `recusas_por_codigo` deste arquivo cai, e e ela que mostra o
progresso sem ninguem precisar acreditar em mim.
"""

import importlib.util
import io
import json
import os
import sys
from decimal import Decimal

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
SAIDA = os.path.join(BASE, "dados", "f2-respostas.json")


def _referencia():
    """Carrega a referencia PELO CAMINHO, nunca uma copia."""
    caminho = os.path.join(AQUI, "f2-referencia.py")
    spec = importlib.util.spec_from_file_location("f2_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _json_seguro(no):
    """Decimal vira TEXTO exato, nunca float.

    A referencia devolve Decimal porque e com ele que ela faz a conta; o arquivo
    guarda o texto. Virar float aqui perderia o centavo exato que a ferramenta
    inteira existe para nao perder, e seria uma perda que nenhum portao veria,
    porque float de dinheiro quase sempre imprime igual.
    """
    if isinstance(no, Decimal):
        return str(no)
    if isinstance(no, dict):
        return {k: _json_seguro(v) for k, v in no.items()}
    if isinstance(no, (list, tuple)):
        return [_json_seguro(v) for v in no]
    return no


def montar(f2, banco=None, esquema=None, constantes=None):
    """O documento inteiro. Aceita banco/esquema/constantes EM MEMORIA porque e assim
    que a bateria de mutacoes gera o dominio de um mundo mutado sem gravar nada em
    disco."""
    banco = banco if banco is not None else f2.carregar_banco()
    esquema = esquema if esquema is not None else f2.carregar_esquema()
    constantes = constantes if constantes is not None else f2.carregar_constantes()

    # O DOMINIO INTEIRO e varrido para CONTAR, e so uma parte dele e GRAVADA. A
    # diferenca entre as duas coisas e decisao de 22/10/2026, com o numero na mesa: o
    # arquivo com os 3.077 estados deu 13 MB, contra 858 KB do arquivo da F1, e ele
    # seria regravado inteiro a cada bloco que mexesse numa regra ou no banco. O que a
    # pagina de fato le e a TABELA PRE-RENDERIZADA (a que fica visivel e que as
    # superficies de IA citam) mais a resposta do estado que o visitante pediu; o resto
    # o tradutor calcula da mesma referencia, que o portao varre inteira em cada
    # passada. Gravar 13 MB por causa de uma grade que ja e medida pelo portao seria
    # pagar peso de repositorio por uma prova que nao esta no arquivo.
    todas = f2.todas_as_respostas(banco, esquema, constantes)
    tabela = f2.tabela_pre_renderizada(banco, esquema, constantes)

    com_conta = [r for r in todas if r["recusa_dura"] is None]
    recusadas = [r for r in todas if r["recusa_dura"] is not None]

    # O QUE ENTRA NO ARQUIVO: a grade da tabela e TODAS as bordas. As bordas entram
    # inteiras de proposito — grade que nao pisa na borda e amostra com nome de grade,
    # e as recusas duras sao justamente onde a conta NAO acontece.
    da_tabela = set()
    for cidade in (banco.get("cidades") or []):
        for padrao in f2.padroes(esquema):
            for dias in f2.DIAS_DA_TABELA:
                for pessoas in f2.PESSOAS_DA_TABELA:
                    da_tabela.add((cidade.get("id"), dias, pessoas, padrao))
    respostas = []
    for r in todas:
        e = r["estado"]
        chave = (e["cidade"], e["dias"], e["pessoas"], e["padrao"])
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

    linhas_por_categoria = {}
    for r in com_conta:
        for linha in r["linhas"]:
            linhas_por_categoria[linha["categoria"]] = \
                linhas_por_categoria.get(linha["categoria"], 0) + 1

    doc = {
        "ilha": "jornadafly",
        "ferramenta": "F2",
        "bloco": 4,
        "versao": 1,
        "publicar": False,
        "motivo_publicar_false": (
            "Esta ilha nao tem WordPress, nao tem Sync e nao tem /status, e o dominio nao "
            "esta na lista de dominios liberados deste ambiente (remedido em 22/10/2026: "
            "recusa do tunel em seis medicoes, com as duas ilhas de controle em 200). Nao "
            "existe 'no ar' para onde publicar, e dizer que publiquei seria inventar."),
        "cumpre": "dados/especificacao-calculadoras.md, secao 3 (F2)",
        "le_de": ["dados/experiencias.json", "dados/esquema-banco.json",
                  "dados/constantes.json"],
        "gerado_por": "ferramentas/gerar-f2.py, a partir de ferramentas/f2-referencia.py",
        "as_duas_procedencias": (
            "Toda resposta deste arquivo separa a linha de EXPERIENCIAS, cujo preco foi "
            "colhido no site de quem opera com data de leitura, das linhas de HOSPEDAGEM, "
            "ALIMENTACAO e TRANSPORTE LOCAL, que sao faixa publicada por terceiros. As duas "
            "nunca entram na mesma linha, e a linha de terceiro so existe com o nome de quem "
            "publicou e a frase com que ele disse o que o numero significa."),
        "acentuacao": (
            "Toda frase deste arquivo e destinada a TELA e por isso sai ACENTUADA, e a "
            "concordancia tambem: a primeira versao desta ferramenta publicou «as 1 "
            "experiencias que esta ilha leu», e foi o portao que viu."),
        "por_que_o_arquivo_nao_traz_todos_os_estados": (
            "A F2 serve %d estados e este arquivo grava %d: a grade da tabela "
            "pre-renderizada mais TODAS as bordas. Os %d estados sao varridos em cada "
            "passada do portao (ferramentas/teste-f2.py), com a aritmetica refeita a mao, "
            "e e la que a grade inteira e provada — nao aqui. Gravar todos deu 13 MB "
            "contra 858 KB do arquivo da F1, e seria regravado inteiro a cada mudanca de "
            "regra ou de banco. A prova mora no portao; o arquivo carrega o que a pagina "
            "le." % (len(todas), len(respostas), len(todas))),
        "resumo": {
            "cidades": len(banco.get("cidades") or []),
            "faixas_diarias": len(banco.get("faixas_diarias") or []),
            "estados": len(todas),
            "estados_gravados": len(respostas),
            "estados_com_conta": len(com_conta),
            "estados_recusados_na_borda": len(recusadas),
            # DOIS numeros e nao um, e a diferenca importa: o primeiro conta o dominio
            # INTEIRO, o segundo conta o que este arquivo guarda. Eram um so ate a
            # bateria de mutacoes achar, em 22/10/2026, que o portao comparava a
            # contagem do dominio com o conteudo do arquivo recortado. Com zero faixas
            # no banco os dois valem 0 e o defeito era invisivel: so o mundo de
            # bancada com as tres faixas carregadas o fez aparecer (252 contra 12).
            "estados_com_total": sum(1 for r in com_conta if r["total"] is not None),
            "estados_gravados_com_total": sum(1 for r in respostas
                                              if r["recusa_dura"] is None
                                              and r["total"] is not None),
            "linhas_da_tabela": len(tabela),
            "linhas_publicadas_por_categoria": linhas_por_categoria,
            "recusas_por_codigo": recusas_por_codigo,
            "recusas_duras_por_codigo": duras_por_codigo,
        },
        "tabela_pre_renderizada": tabela,
        "respostas": respostas,
    }
    return _json_seguro(doc)


def main():
    f2 = _referencia()
    doc = montar(f2)
    r = doc["resumo"]
    print("F2 da JornadaFly — dominio de resposta")
    for chave in ("cidades", "faixas_diarias", "estados", "estados_gravados",
                  "estados_com_conta", "estados_recusados_na_borda", "estados_com_total",
                  "estados_gravados_com_total", "linhas_da_tabela"):
        print("  %-32s %s" % (chave.replace("_", " "), r[chave]))
    print("  linhas publicadas por categoria:")
    for categoria in sorted(r["linhas_publicadas_por_categoria"]):
        print("     %-38s %d" % (categoria, r["linhas_publicadas_por_categoria"][categoria]))
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA CATEGORIA PASTILHA — bloco 3d, 12/09/2026.

Cada mutacao e um defeito ESCRITO DE VOLTA no banco. Se um portao nao reprovar, o
portao nao vale o arquivo que ocupa. Duas regras herdadas de blocos anteriores
valem aqui:

  (a) Mutacao que qualquer portao ANTIGO ja pegava nao justifica portao novo. Por
      isso cada mutacao roda os DOIS — `validar-banco.py` (o esquema) e
      `validar-pastilhas.py` (a regua desta categoria) — e a saida marca as que
      SO a regua nova viu.

  (b) Alvo que nao e unico no arquivo edita a coisa errada e passa verde. A troca
      e feita por caminho de campo no JSON, nao por texto, e as que mexem em
      codigo conferem que a string aparece EXATAMENTE uma vez.

Uso:  python3 ferramentas/mutacoes-pastilhas.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
BANCO = os.path.join(ILHA, "dados", "materiais-pastilhas.json")
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")
VALIDAR_PASTILHAS = os.path.join(AQUI, "validar-pastilhas.py")


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


# --------------------------------------------------------------- as mutacoes
# (nome, o que o defeito seria no mundo real, funcao que o escreve)

def m01(b):
    """O numero que a SERP inteira publica: 30 / 2,5 = 12, logo 144 por placa."""
    g = item(b, "glassmosaic-k2501")["geometria"]
    g["pastilhas_por_placa"] = 144
    g["motivo_pastilhas_por_placa"] = None


def m02(b):
    """Passo declarado sem nada que o sustente — o numero aparece do nada."""
    g = item(b, "glassmosaic-a11")["geometria"]
    g["passo_de_fabrica_cm"] = 2.0
    g["motivo_passo"] = None


def m03(b):
    """Junta negativa: passo menor que a propria pastilha."""
    g = item(b, "glassmosaic-k117")["geometria"]
    g["pastilhas_por_placa"] = 121
    g["motivo_pastilhas_por_placa"] = None
    g["passo_de_fabrica_cm"] = 2.65
    g["motivo_passo"] = None


def m04(b):
    """Peso da caixa virando peso de peca — o atalho mais tentador do arquivo."""
    g = item(b, "glassmosaic-k2501")["geometria"]
    g["peso_unitario_g"] = 1.6
    g["motivo"] = None


def m05(b):
    """Metragem da caixa que nao fecha nem cortando nem arredondando."""
    item(b, "glassmosaic-k77")["propriedades"]["m2_por_caixa"]["valor"] = 0.9


def m06(b):
    """A divergencia do teto fisico apagada, com o peso intacto: o caso em que a
    ficha se contradiz e ninguem escreveu isso."""
    it = item(b, "glassmosaic-st5102")
    it["divergencias"] = []
    it["resolucao"] = None


def m07(b):
    """O distribuidor promovido a fabricante. E a mutacao que PRODUZ O MUNDO: sem
    mexer em mais nada ela faz 1,5 cm passar de zero para um elegivel, e e por isso
    que a cobertura por tamanho tem de ser recomputada do nivel e nunca digitada."""
    it = item(b, "pastilhart-af1500")
    for f in it["fontes"].values():
        f["nivel"] = 3


def m08(b):
    """O defeito original da regua escrito no dado: o lado da PLACA preenchido com
    o lado da pastilha. Antes do bloco 3d isto passava, porque o campo nem existia."""
    g = item(b, "glassmosaic-a61")["geometria"]
    g["placa_lado_a_cm"] = 2.0
    g["placa_lado_b_cm"] = 2.0


def m09(b):
    """O motivo apagado: o campo continua null, mas o silencio deixa de ser dito."""
    item(b, "glassmosaic-k66")["geometria"]["motivo_pastilhas_por_placa"] = None


def m10(b):
    """O cabecalho conta um item a menos do que o arquivo tem esperando link."""
    b["afiliado"]["itens_esperando_link"] = 9


def m11(b):
    """Passo em placa que nao e quadrada: a formula L/raiz(N) nem se aplica."""
    g = item(b, "glassmosaic-st5102")["geometria"]
    g["pastilhas_por_placa"] = 576
    g["motivo_pastilhas_por_placa"] = None
    g["passo_de_fabrica_cm"] = 1.19
    g["motivo_passo"] = None


def m12(b):
    """Fonte de nivel 7 (blog/SERP) sustentando campo tecnico."""
    item(b, "glassmosaic-k2502")["fontes"]["pagina-produto-k2502"]["nivel"] = 7


MUTACOES = [
    ("01 pecas por placa pela divisao ingenua", m01),
    ("02 passo declarado sem N que o sustente", m02),
    ("03 junta negativa (passo < pastilha)", m03),
    ("04 peso da caixa virando peso de peca", m04),
    ("05 metragem da caixa que nao fecha", m05),
    ("06 divergencia do teto fisico apagada", m06),
    ("07 distribuidor promovido a fabricante", m07),
    ("08 lado da placa preenchido com o lado da pastilha", m08),
    ("09 motivo do campo null apagado", m09),
    ("10 cabecalho contando um item a menos", m10),
    ("11 passo em placa que nao e quadrada", m11),
    ("12 fonte de nivel 7 sustentando campo tecnico", m12),
]


def roda(script, cwd):
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, cwd=cwd)
    return r.returncode != 0


def main():
    original = json.load(open(BANCO, encoding="utf-8"))

    # o mundo sem mutacao tem de estar verde, senao nada abaixo significa coisa alguma
    base_banco = roda(VALIDAR_BANCO, ILHA)
    base_past = roda(VALIDAR_PASTILHAS, ILHA)
    if base_banco or base_past:
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao "
              "(validar-banco=%s, validar-pastilhas=%s)" % (base_banco, base_past))
        return 1

    print("Mutacoes da categoria PASTILHA — %d escritas" % len(MUTACOES))
    print("")
    reprovadas = 0
    so_a_regua_nova = 0
    for nome, funcao in MUTACOES:
        mutado = copy.deepcopy(original)
        funcao(mutado)
        if mutado == original:
            print("  INERTE  %s — a mutacao nao mudou nada" % nome)
            continue
        backup = BANCO + ".original"
        shutil.copy2(BANCO, backup)
        try:
            with open(BANCO, "w", encoding="utf-8") as fh:
                json.dump(mutado, fh, ensure_ascii=False, indent=2)
            pegou_banco = roda(VALIDAR_BANCO, ILHA)
            pegou_past = roda(VALIDAR_PASTILHAS, ILHA)
        finally:
            shutil.move(backup, BANCO)

        if pegou_banco or pegou_past:
            reprovadas += 1
            quem = []
            if pegou_banco:
                quem.append("esquema")
            if pegou_past:
                quem.append("regua nova")
            if pegou_past and not pegou_banco:
                so_a_regua_nova += 1
            print("  REPROVOU  %-52s (%s)" % (nome, " + ".join(quem)))
        else:
            print("  PASSOU    %-52s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so a regua nova viu ............ %d" % so_a_regua_nova)
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_a_regua_nova == 0:
        print("\nREPROVADO: se o esquema antigo pega tudo, a regua nova nao se justifica.")
        return 1
    print("\nOK: as %d mutacoes reprovaram." % len(MUTACOES))
    return 0


if __name__ == "__main__":
    sys.exit(main())

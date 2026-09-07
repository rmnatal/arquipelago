#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida o banco de produtos da ilha Aquametria contra dados/esquema-produtos.json.

Uso (a partir de ilhas/aquametria/):  python3 ferramentas/validar-produtos.py

As regras V1 a V14 estao descritas em dados/esquema-produtos.json e em
dados/modelo-banco-produtos.md. Este arquivo e a versao executavel delas: regra
que nao roda vira decoracao, e banco de produto sem validacao apodrece em silencio.

Codigo de saida: 0 se nao houver erro (avisos nao reprovam), 1 se houver.
"""

import json
import math
import os
import re
import sys
from datetime import date, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
ARQUIVOS = {
    "filtro": "dados/produtos-filtro.json",
    "aquecedor": "dados/produtos-aquecedor.json",
    "iluminacao": "dados/produtos-iluminacao.json",
    "midia": "dados/produtos-midia.json",
}
COTACOES = "dados/produtos-cotacoes.json"

ID_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CAMPOS_META = {
    "id", "entidade", "marca", "linha", "modelo", "variante", "nomes_alternativos",
    "gtin", "disponibilidade_br", "fontes", "conflitos", "verificado_em",
    "status_registro", "observacao",
}
LIMITE_DIAS_REVALIDAR = 180
LIMITE_EFICIENCIA_FILTRO = 120.0   # L/h por W
LIMITE_LARGURA_FAIXA = 3.0         # x

erros = []
avisos = []


def erro(regra, produto, texto):
    erros.append((regra, produto, texto))


def aviso(regra, produto, texto):
    avisos.append((regra, produto, texto))


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as fp:
        return json.load(fp)


def preenchido(valor):
    if valor is None:
        return False
    if isinstance(valor, (list, dict)) and len(valor) == 0:
        return False
    if isinstance(valor, dict):
        return any(v is not None for v in valor.values())
    return True


def obrigatorios_da_entidade(esquema, entidade):
    obrig = []
    for campo in esquema["campos_comuns"]:
        if not campo.get("obrigatorio"):
            continue
        alvo = campo.get("obrigatorio_em")
        if alvo and entidade not in alvo:
            continue
        obrig.append(campo["campo"])
    for campo in esquema["entidades"][entidade]["campos"]:
        if campo.get("obrigatorio"):
            obrig.append(campo["campo"])
    return obrig


def campos_tecnicos_da_entidade(esquema, entidade):
    """Campos que exigem fonte. Campo de origem 'editorial' e classificacao da
    Aquametria (nao dado de terceiro) e por isso fica de fora."""
    tecnicos = {c["campo"] for c in esquema["entidades"][entidade]["campos"]
                if "editorial" not in (c.get("origem") or "")}
    tecnicos.update({"volume_atendido_declarado_L", "voltagem"})
    return tecnicos


def derivados_da_entidade(esquema, entidade):
    return {d["campo"] for d in esquema["entidades"][entidade].get("derivados", [])}


def atende(produto, requisitos):
    """Um requisito pode ser 'campo' ou 'campo_a OU campo_b'."""
    faltando = []
    for req in requisitos:
        alternativas = [p.strip() for p in req.split(" OU ")]
        if not any(preenchido(produto.get(alt)) for alt in alternativas):
            faltando.append(req)
    return faltando


def valida_produto(esquema, entidade, produto, vistos):
    pid = produto.get("id", "<sem id>")

    # V1 - id unico, kebab-case, sem acento
    if not ID_VALIDO.match(pid):
        erro("V1", pid, "id fora do padrao kebab-case sem acento")
    if pid in vistos:
        erro("V1", pid, "id repetido (ja usado em %s)" % vistos[pid])
    else:
        vistos[pid] = entidade

    if produto.get("entidade") != entidade:
        erro("V1", pid, "campo entidade ('%s') nao bate com o arquivo (%s)"
             % (produto.get("entidade"), entidade))

    tecnicos = campos_tecnicos_da_entidade(esquema, entidade)
    derivados = derivados_da_entidade(esquema, entidade)
    fontes = produto.get("fontes") or []

    # V2 - todo campo tecnico preenchido tem fonte que o sustente
    sustentados = set()
    for fonte in fontes:
        sustentados.update(fonte.get("campos") or [])
    for campo in tecnicos:
        if preenchido(produto.get(campo)) and campo not in sustentados:
            erro("V2", pid, "campo '%s' preenchido sem fonte que o sustente" % campo)

    # V2b - fonte citando campo que o produto nao tem
    for campo in sustentados:
        if campo not in tecnicos and campo not in CAMPOS_META:
            aviso("V2", pid, "fonte cita campo desconhecido '%s'" % campo)

    if not fontes:
        erro("V2", pid, "produto sem nenhuma fonte")

    # V3 - sanidade numerica
    vol = produto.get("volume_atendido_declarado_L")
    if isinstance(vol, dict):
        vmin, vmax = vol.get("min"), vol.get("max")
        if vmin is not None and vmax is not None and vmin > vmax:
            erro("V3", pid, "volume_atendido_declarado_L com min > max")
    for campo in ("vazao_nominal_lh", "potencia_w", "fluxo_lm", "volume_embalagem_L",
                  "coluna_maxima_m", "area_superficial_m2_por_L"):
        valor = produto.get(campo)
        if valor is not None and valor <= 0:
            erro("V3", pid, "%s deve ser maior que zero" % campo)
    faixa = produto.get("faixa_ajuste_C")
    if isinstance(faixa, dict) and faixa.get("min") is not None and faixa.get("max") is not None:
        if faixa["min"] >= faixa["max"]:
            erro("V3", pid, "faixa_ajuste_C com min >= max")

    # V4 - derivado gravado a mao
    for campo in derivados:
        if campo in produto:
            erro("V4", pid, "campo derivado '%s' gravado no arquivo de produto" % campo)

    # V5 - PPFD so em par
    if entidade == "iluminacao":
        tem_ppfd = preenchido(produto.get("ppfd_declarado"))
        tem_dist = preenchido(produto.get("ppfd_distancia_cm"))
        if tem_ppfd != tem_dist:
            erro("V5", pid, "ppfd_declarado e ppfd_distancia_cm precisam vir juntos")

    # V6 - marketplace nao sustenta campo tecnico
    for fonte in fontes:
        if fonte.get("origem") == "marketplace-anuncio":
            proibidos = [c for c in (fonte.get("campos") or [])
                         if c in tecnicos]
            if proibidos:
                erro("V6", pid, "fonte de marketplace sustentando campo tecnico: %s"
                     % ", ".join(sorted(proibidos)))

    # V7 - preco nao mora aqui
    for campo in produto:
        if "preco" in campo or "price" in campo:
            erro("V7", pid, "campo de preco ('%s') dentro do arquivo de produtos" % campo)

    # V8 / V14 - completude x status declarado
    obrig = obrigatorios_da_entidade(esquema, entidade)
    faltando = [c for c in obrig if not preenchido(produto.get(c))]
    status = produto.get("status_registro")
    if status == "completo" and faltando:
        erro("V8", pid, "status 'completo' mas faltam obrigatorios: %s" % ", ".join(faltando))
    if status == "parcial" and not faltando:
        aviso("V14", pid, "status 'parcial' sem obrigatorio faltante - use 'completo' ou "
                          "explique o motivo na observacao")

    # V9 - data de verificacao
    try:
        verificado = datetime.strptime(produto.get("verificado_em", ""), "%Y-%m-%d").date()
    except ValueError:
        erro("V9", pid, "verificado_em ausente ou fora do formato AAAA-MM-DD")
    else:
        hoje = date.today()
        if verificado > hoje:
            erro("V9", pid, "verificado_em no futuro")
        elif (hoje - verificado).days > LIMITE_DIAS_REVALIDAR and status != "revalidar":
            aviso("V9", pid, "verificado ha mais de %d dias e nao esta como 'revalidar'"
                  % LIMITE_DIAS_REVALIDAR)

    # V12 - conflito declarado exige status conflito
    if produto.get("conflitos") and status != "conflito":
        erro("V12", pid, "tem conflitos[] mas status_registro e '%s'" % status)

    # V13 - iluminacao com lumen precisa de comprimento
    if entidade == "iluminacao" and preenchido(produto.get("fluxo_lm")):
        if not (preenchido(produto.get("comprimento_luminaria_cm"))
                or preenchido(produto.get("comprimento_aquario_cm"))):
            aviso("V13", pid, "fluxo_lm sem comprimento: a C15 nao consegue sugerir este produto")

    return faltando


def derivar(entidade, produto):
    """Calcula os derivados do esquema. Nunca sao gravados: existem so aqui e na tela."""
    out = {}
    vol = produto.get("volume_atendido_declarado_L") or {}
    vmin, vmax = vol.get("min"), vol.get("max")

    if entidade == "filtro":
        vazao, pot = produto.get("vazao_nominal_lh"), produto.get("potencia_w")
        if vazao and vmax:
            out["turnover_min_xh"] = round(vazao / vmax, 2)
        if vazao and vmin:
            out["turnover_max_xh"] = round(vazao / vmin, 2)
        if vazao and pot:
            out["eficiencia_lh_por_w"] = round(vazao / pot, 1)
            if out["eficiencia_lh_por_w"] > LIMITE_EFICIENCIA_FILTRO:
                aviso("V10", produto["id"], "eficiencia de %.1f L/h por W e implausivel; "
                      "reconferir no manual" % out["eficiencia_lh_por_w"])

    if entidade == "aquecedor":
        pot = produto.get("potencia_w")
        if pot and vmax:
            out["w_por_L_min"] = round(pot / vmax, 2)
        if pot and vmin:
            out["w_por_L_max"] = round(pot / vmin, 2)
        if vmin and vmax:
            out["largura_faixa_x"] = round(vmax / vmin, 1)
            if out["largura_faixa_x"] > LIMITE_LARGURA_FAIXA:
                aviso("V11", produto["id"], "faixa declarada de %.1fx: a declaracao do "
                      "fabricante nao dimensiona, e a tela precisa dizer isso"
                      % out["largura_faixa_x"])

    if entidade == "iluminacao":
        lm, pot = produto.get("fluxo_lm"), produto.get("potencia_w")
        if lm and pot:
            out["eficacia_lm_por_w"] = round(lm / pot, 1)

    if entidade == "midia":
        dose = produto.get("dosagem_declarada")
        if isinstance(dose, dict) and dose.get("por_volume_agua_L"):
            out["dosagem_mL_por_L"] = round(
                dose["volume_midia_mL"] / dose["por_volume_agua_L"], 2)
        if produto.get("peso_g") and produto.get("volume_embalagem_L"):
            out["densidade_aparente_g_por_L"] = round(
                produto["peso_g"] / produto["volume_embalagem_L"], 1)
    return out


def main():
    esquema = carregar(os.path.relpath(ESQUEMA, RAIZ))
    vistos = {}
    total = 0
    sugeribilidade = {}

    for entidade, caminho in ARQUIVOS.items():
        arquivo = carregar(caminho)
        produtos = arquivo.get("produtos", [])
        minimos = esquema["entidades"][entidade]["minimo_para_sugerir"]
        for calc in minimos:
            sugeribilidade.setdefault(calc, {"aptos": [], "barrados": []})

        print("\n== %s (%d registros) ==" % (entidade, len(produtos)))
        for produto in produtos:
            total += 1
            valida_produto(esquema, entidade, produto, vistos)
            derivados = derivar(entidade, produto)
            desc = ", ".join("%s=%s" % (k, v) for k, v in sorted(derivados.items()))
            print("  %-28s %-10s %s" % (produto.get("id"),
                                        produto.get("status_registro"),
                                        desc or "(sem derivado calculavel)"))
            for calc, requisitos in minimos.items():
                faltando = atende(produto, requisitos)
                bloqueado = produto.get("status_registro") in ("rascunho", "revalidar")
                if faltando or bloqueado:
                    motivo = ", ".join(faltando) if faltando else "status " + produto["status_registro"]
                    sugeribilidade[calc]["barrados"].append((produto["id"], motivo))
                else:
                    sugeribilidade[calc]["aptos"].append(produto["id"])

    # V7 - cotacoes referenciam produtos existentes
    cot = carregar(COTACOES)
    for c in cot.get("cotacoes", []):
        if c.get("produto_id") not in vistos:
            erro("V7", c.get("produto_id", "<sem id>"),
                 "cotacao aponta para produto que nao existe no banco")

    print("\n== quem cada calculadora consegue sugerir hoje ==")
    for calc in sorted(sugeribilidade):
        dados = sugeribilidade[calc]
        print("  %-22s %d apto(s), %d barrado(s)"
              % (calc, len(dados["aptos"]), len(dados["barrados"])))
        for pid, motivo in dados["barrados"]:
            print("      - %-28s falta: %s" % (pid, motivo))

    print("\n== resultado ==")
    print("  %d produtos, %d cotacoes, %d erro(s), %d aviso(s)"
          % (total, len(cot.get("cotacoes", [])), len(erros), len(avisos)))
    for regra, pid, texto in erros:
        print("  ERRO  [%s] %s: %s" % (regra, pid, texto))
    for regra, pid, texto in avisos:
        print("  aviso [%s] %s: %s" % (regra, pid, texto))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

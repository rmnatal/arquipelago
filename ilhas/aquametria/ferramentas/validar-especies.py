#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida o banco de especies da ilha Aquametria contra dados/esquema-especies.json.

Uso (a partir de ilhas/aquametria/):  python3 ferramentas/validar-especies.py [arquivo]

As regras E1 a E15 estao descritas em dados/esquema-especies.json. Este arquivo e a
versao executavel delas, pelo mesmo motivo do validador de produtos: regra que nao
roda vira decoracao. Imprime tambem quem passa no minimo_para_sugerir de cada
consumidor, que e a resposta pratica para "esta especie ja pode virar pagina?".

Codigo de saida: 0 se nao houver erro (avisos nao reprovam), 1 se houver.
"""

import json
import os
import re
import sys
from datetime import date, datetime
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-especies.json")
# Aceita um caminho no argv para que ferramentas/testar-validador-especies.py possa
# rodar as regras contra bancos deliberadamente corrompidos sem tocar no arquivo real.
ARQUIVO = sys.argv[1] if len(sys.argv) > 1 else "dados/especies-agua-doce.json"

ID_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LIMITE_DIAS_REVALIDAR = 365
AMPLITUDE_QUE_E_TOLERANCIA = 20.0

erros = []
avisos = []


def erro(regra, alvo, texto):
    erros.append((regra, alvo, texto))


def aviso(regra, alvo, texto):
    avisos.append((regra, alvo, texto))


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as fp:
        return json.load(fp)


def preenchido(valor):
    if valor is None:
        return False
    if isinstance(valor, (list, dict)) and not valor:
        return False
    if isinstance(valor, dict):
        return any(v is not None for v in valor.values())
    return True


def intervalo(valor):
    return isinstance(valor, dict) and "min" in valor and "max" in valor


# Espelhos do MESMO corpo de conhecimento. Regra E15: url diferente nao e fonte
# diferente quando as duas leem a mesma base. fishbase.se e fishbase.org sao a
# mesma FishBase; sem esta tabela, acrescentar o espelho faria um registro de
# fonte unica passar por conferido.
ESPELHOS = {
    "fishbase.se": "fishbase",
    "fishbase.org": "fishbase",
    "seriouslyfish.com": "seriouslyfish",
}


def corpo_da_fonte(url):
    """Corpo de conhecimento por tras da url, com espelhos colapsados."""
    host = (urlparse(url or "").netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    if host in ESPELHOS:
        return ESPELHOS[host]
    partes = host.split(".")
    return ".".join(partes[-2:]) if len(partes) > 1 else host


def corpos_de(registro):
    return {corpo_da_fonte(f.get("url")) for f in registro.get("fontes", []) if f.get("url")}


def main():
    esquema = json.load(open(ESQUEMA, encoding="utf-8"))
    campos_esq = {c["campo"]: c for c in esquema["campos"]}
    obrigatorios = [c["campo"] for c in esquema["campos"] if c.get("obrigatorio")]
    isentos = set(esquema["campos_sem_fonte_exigida"]["lista"])
    origens = {n["origem"] for n in esquema["escada_de_fontes"]["niveis"]}
    status_por_origem = {n["origem"]: n["status"] for n in esquema["escada_de_fontes"]["niveis"]}
    dominio = esquema["dominio_por_campo"]
    campos_manutencao = set(dominio["manutencao"]["campos"])
    campos_bem_estar = {"cardume_minimo", "comprimento_minimo_aquario_cm", "base_minima_cm",
                        "altura_minima_cm"}

    banco = carregar(ARQUIVO)
    registros = banco["especies"]
    hoje = date.today()
    vistos = set()

    for r in registros:
        rid = r.get("id", "<sem id>")

        # E1 - id
        if not ID_VALIDO.match(rid):
            erro("E1", rid, "id fora do kebab-case")
        if rid in vistos:
            erro("E1", rid, "id repetido no arquivo")
        vistos.add(rid)
        esperado = r.get("nome_cientifico", "").lower().replace(" ", "-")
        if esperado and esperado != rid:
            erro("E1", rid, "id nao corresponde ao nome cientifico (%s)" % esperado)

        # E2 - obrigatorios
        faltando = [c for c in obrigatorios if not preenchido(r.get(c))]
        if faltando:
            if r.get("status_registro") != "parcial":
                erro("E2", rid, "falta campo obrigatorio (%s) e o status nao e parcial"
                     % ", ".join(faltando))
            elif not r.get("observacao"):
                erro("E2", rid, "registro parcial sem observacao dizendo o que falta")

        # E14 / E15 - completo exige duas fontes de CORPOS distintos, nao so de urls distintas
        urls_fonte = {f.get("url") for f in r.get("fontes", []) if f.get("url")}
        corpos = corpos_de(r)
        if r.get("status_registro") == "completo" and len(corpos) < 2:
            erro("E14", rid, "status completo com %d corpo(s) de fonte distinto(s)" % len(corpos))
        if len(urls_fonte) >= 2 and len(corpos) < 2:
            aviso("E15", rid, "tem %d urls mas um corpo de fonte so (%s): espelho nao confere "
                              "espelho" % (len(urls_fonte), ", ".join(sorted(corpos))))

        # E4 - fontes bem formadas, e o indice campo -> origens
        sustentado = {}
        for f in r.get("fontes", []):
            ref = f.get("referencia", "<sem referencia>")[:40]
            if f.get("origem") not in origens:
                erro("E4", rid, "fonte com origem fora da escada: %s" % f.get("origem"))
            elif f.get("status") != status_por_origem[f["origem"]]:
                erro("E4", rid, "fonte '%s' com status incoerente com a origem" % ref)
            if not f.get("url"):
                erro("E4", rid, "fonte '%s' sem url" % ref)
            if not f.get("verificado_em"):
                erro("E4", rid, "fonte '%s' sem verificado_em" % ref)
            for campo in f.get("campos", []):
                sustentado.setdefault(campo, []).append(f.get("origem"))

        # E3 - todo campo preenchido tem fonte
        for campo, spec in campos_esq.items():
            if campo in isentos:
                continue
            if preenchido(r.get(campo)) and campo not in sustentado:
                erro("E3", rid, "campo '%s' preenchido sem nenhuma fonte que o sustente" % campo)

        # E5 - varejo nao sustenta manutencao
        for campo, ors in sustentado.items():
            if campo in campos_manutencao and set(ors) == {"varejo"}:
                erro("E5", rid, "campo de manutencao '%s' sustentado so por varejo" % campo)

        # E6 - porte exige medida
        if preenchido(r.get("porte_adulto_cm")) and not r.get("porte_medida"):
            erro("E6", rid, "porte_adulto_cm sem porte_medida (SL ou TL)")

        # E7 - litro derivado gravado a mao
        vol = r.get("volume_minimo_declarado_L")
        if preenchido(vol):
            if "volume_minimo_declarado_L" not in sustentado:
                erro("E7", rid, "volume_minimo_declarado_L sem fonte que declare litro")
            base = r.get("base_minima_cm") or {}
            comp, larg = base.get("comprimento"), base.get("largura")
            if comp and larg:
                for altura in range(25, 61, 5):
                    if abs(comp * larg * altura / 1000.0 - vol) < 0.5:
                        erro("E7", rid, "volume_minimo_declarado_L bate com a base x %d cm: "
                                        "e derivado gravado a mao" % altura)
                        break

        # E8 - intervalos
        for campo in ("temperatura_C", "ph", "dureza_dgh"):
            v = r.get(campo)
            if intervalo(v) and v["min"] is not None and v["max"] is not None:
                if v["min"] > v["max"]:
                    erro("E8", rid, "%s com min maior que max" % campo)
                elif v["min"] == v["max"]:
                    aviso("E8", rid, "%s com min igual a max" % campo)

        # E9 / E10 - conflitos
        confs = r.get("conflitos") or []
        for c in confs:
            if c.get("tratamento") not in ("publicar-os-dois", "nivel-mais-alto-vence",
                                           "campo-vira-null", "intersecao-conservadora"):
                erro("E9", rid, "conflito em '%s' com tratamento invalido" % c.get("campo"))
            if c.get("campo") in campos_bem_estar:
                brutos = [v.get("valor") for v in c.get("valores", [])]
                numeros = [v for v in brutos if isinstance(v, (int, float))]
                if numeros and c.get("valor_conservador") != max(numeros):
                    erro("E9", rid, "conflito de bem-estar em '%s': o conservador tem de ser o maior (%s)"
                         % (c["campo"], max(numeros)))
        # E10: 'parcial' tambem vale quando o registro tem campo obrigatorio faltando.
        # Completude e divergencia sao fatos ortogonais e status_registro carrega um campo so:
        # nesse caso vale o mais restritivo, e 'parcial' e mais restritivo que 'conflito'
        # porque barra a pagina.
        aceitos_com_conflito = ["conflito", "revalidar"] + (["parcial"] if faltando else [])
        if confs and r.get("status_registro") not in aceitos_com_conflito:
            erro("E10", rid, "tem conflitos mas o status nao e conflito, revalidar nem parcial "
                             "com campo obrigatorio faltando")
        if r.get("status_registro") == "conflito" and not confs:
            erro("E10", rid, "status conflito sem nenhum conflito declarado")

        # E11 - idade do registro
        try:
            visto = datetime.strptime(r["verificado_em"], "%Y-%m-%d").date()
            if (hoje - visto).days > LIMITE_DIAS_REVALIDAR:
                aviso("E11", rid, "verificado ha mais de %d dias" % LIMITE_DIAS_REVALIDAR)
        except (KeyError, ValueError):
            erro("E11", rid, "verificado_em ausente ou fora do formato ISO")

        # E12 - cardume x convivencia
        card, conv = r.get("cardume_minimo"), r.get("convivencia")
        if preenchido(card) and card > 1 and conv not in ("cardume", "grupo"):
            erro("E12", rid, "cardume_minimo %s com convivencia '%s'" % (card, conv))
        if conv == "solitario" and preenchido(card):
            erro("E12", rid, "convivencia solitario com cardume_minimo preenchido")

        # E13 - tolerancia disfarcada de recomendacao
        t = r.get("temperatura_C")
        if intervalo(t) and t["min"] is not None and t["max"] is not None:
            if (t["max"] - t["min"]) > AMPLITUDE_QUE_E_TOLERANCIA and not r.get("temperatura_e_tolerancia"):
                erro("E13", rid, "temperatura com amplitude de %.0f C sem temperatura_e_tolerancia"
                     % (t["max"] - t["min"]))

    # quem ja pode virar pagina, e quem alimenta cada calculadora
    print("== quem passa no minimo_para_sugerir ==")
    for consumidor, requisitos in esquema["minimo_para_sugerir"].items():
        if consumidor == "regra":
            continue
        aptos, barrados = [], []
        for r in registros:
            falta = []
            for req in requisitos:
                if req == "duas fontes distintas":
                    if len(corpos_de(r)) < 2:
                        falta.append("duas fontes de corpos distintos")
                elif req.startswith("cardume_minimo OU"):
                    if not preenchido(r.get("cardume_minimo")) and \
                       r.get("convivencia") not in ("solitario", "casal", "harem"):
                        falta.append("cardume_minimo ou convivencia solitario/casal/harem")
                elif req.startswith("temperatura_C com"):
                    if not preenchido(r.get("temperatura_C")) or r.get("temperatura_e_tolerancia"):
                        falta.append("temperatura de manutencao (a faixa e de tolerancia)")
                elif not preenchido(r.get(req)):
                    falta.append(req)
            if r.get("status_registro") in ("rascunho", "revalidar"):
                falta.append("status " + r["status_registro"])
            (barrados if falta else aptos).append((r["id"], ", ".join(falta)))
        print("  %-16s %d apto(s), %d barrado(s)" % (consumidor, len(aptos), len(barrados)))
        for rid, motivo in barrados:
            print("      - %-28s falta: %s" % (rid, motivo))

    print("\n== faixa de porte coberta ==")
    portes = sorted((r["porte_adulto_cm"], r["id"]) for r in registros
                    if preenchido(r.get("porte_adulto_cm")))
    if portes:
        print("  de %.1f cm (%s) a %.1f cm (%s)"
              % (portes[0][0], portes[0][1], portes[-1][0], portes[-1][1]))
    frentes = sorted({r["comprimento_minimo_aquario_cm"] for r in registros
                      if preenchido(r.get("comprimento_minimo_aquario_cm"))})
    print("  frentes minimas declaradas: %s cm" % ", ".join(str(f) for f in frentes))

    print("\n== resultado ==")
    print("  %d especies, %d erro(s), %d aviso(s)" % (len(registros), len(erros), len(avisos)))
    for regra, rid, texto in erros:
        print("  ERRO  [%s] %s: %s" % (regra, rid, texto))
    for regra, rid, texto in avisos:
        print("  aviso [%s] %s: %s" % (regra, rid, texto))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

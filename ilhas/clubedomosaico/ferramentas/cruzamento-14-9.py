#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O CRUZAMENTO DA 14.9 — o portao de DADO e o de SERP saindo no MESMO veredito.

    python3 ferramentas/cruzamento-14-9.py              # escreve dados/cruzamento-14-9.md
    python3 ferramentas/cruzamento-14-9.py --conferir   # nao escreve; falha se o arquivo estiver velho
    python3 ferramentas/cruzamento-14-9.py --autoteste  # entradas fabricadas, para a regua poder morder

POR QUE ESTE ARQUIVO EXISTE. A secao 14.9 do ARQUIPELAGO.md manda cruzar DUAS coisas e diz
isso com estas palavras: "A prioridade e o cruzamento de duas coisas, nunca de uma so:
intencao de compra x chance real de primeira pagina. Volume alto sem chance e pagina
desperdicada; chance alta sem intencao e visita que nao vira dinheiro."

As duas metades existiam desde 30/09/2026 e NUNCA SE ENCONTRARAM num veredito:

  - o portao de DADO (secao 9: 3 itens reais e um numero calculado) e DERIVADO do banco e
    mora em `dados/filhas-do-guia.json`, escrito por `filhas-do-guia.py`, que diz de si
    mesmo, no proprio cabecalho: "ele nao escreve pagina, nao escolhe endereco e NAO
    CLASSIFICA SERP";
  - o portao de SERP era PROSA, numa secao de `dados/filhas-do-guia.md` que aquele gerador
    preservava sem ler.

E prosa nao cruza com numero. O custo foi medido: entre 30/09 e 02/10 a pergunta "o 4c pode
nascer?" exigia abrir dois arquivos e fazer a conta na cabeca, e o `ESTADO.md` de 02/10 as
13h17Z teve de escrever a mao o aviso "o portao de DADO abriu, o de SERP e outro" para a
execucao seguinte nao ler passe livre. Aviso a mao e o que este arquivo substitui.

O VEREDITO E CALCULADO, NUNCA ESCRITO. Cada recorte recebe UM veredito do cruzamento, e ele
sai de duas entradas que vem de arquivos diferentes e de coletas diferentes:

  pode_nascer                     — dado `passa` E serp `ABERTA`
  pode_nascer_sem_demanda_medida  — dado `passa` E serp `ABERTA_SEM_INTENCAO_NA_SERP`:
                                    chance alta, intencao NAO provada. E a metade "chance
                                    alta sem intencao" que a 14.9 nomeia, e por isso ela
                                    nao se confunde com a de cima
  espera_autoridade               — dado `passa` E serp `TOMADA`. Vai para a lista de
                                    "quando houver autoridade", que e o que a 14.9 manda
  espera_dado                     — serp `ABERTA` E dado nao passa. O buraco existe e o
                                    banco nao alcanca; aqui o trabalho e COLETA
  espera_serp                     — dado `passa` E nenhuma consulta medida, ou so medicao
                                    `NAO_MEDIDA`. Nao e aberta e nao e tomada: e ignorada
  nunca                           — serp `ARMADILHA`. Termo negativo
  sem_nenhum_dos_dois             — dado nao passa e SERP nao medida. Nao ha o que decidir

A PRECEDENCIA TEM UM MOTIVO E ELE E O DA 14.9. Quando um recorte tem varias consultas
medidas, vale a MELHOR classificacao de SERP — porque a 14.9 pergunta se existe UM caminho
para a primeira pagina, nao se todos os caminhos servem. Mas `ARMADILHA` vence tudo, porque
armadilha nao e um caminho pior: e outra intencao, e construir nela e erro mesmo com dado.

O QUE ESTE ARQUIVO NAO FAZ: nao escolhe o endereco da pagina (a 16.5 manda a mae esperar 3
filhas e quem publica escolhe o slug), nao afirma POSICAO de ninguem (o canal desta nuvem nao
da ordem; posicao nesta ilha vem do Search Console) e NAO ESTIMA FAIXA DE VOLUME. Onde a
faixa falta, ele deriva o PEDIDO ao Raphael — consulta por consulta, com o recorte que a
exige — em vez de escrever um numero que ninguem mediu.
"""

import io
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

ENTRADA_DADO = os.path.join(DADOS, "filhas-do-guia.json")
ENTRADA_SERP = os.path.join(DADOS, "serp-das-filhas.json")
SAIDA_MD = os.path.join(DADOS, "cruzamento-14-9.md")

# A ordem e de MELHOR para PIOR chance, e e ela que a precedencia usa. `ARMADILHA` esta
# fora desta escada de proposito: ela nao e chance pior, e outra intencao.
ESCADA_DA_SERP = ["ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP", "TOMADA", "NAO_MEDIDA"]

VEREDITOS_QUE_AUTORIZAM = ("pode_nascer", "pode_nascer_sem_demanda_medida")


# ------------------------------------------------------------------ as duas reguas

def serp_do_recorte(medicoes):
    """A classificacao que vale para o recorte, entre todas as consultas medidas nele.

    Vale a MELHOR, porque a 14.9 pergunta se existe UM caminho para a primeira pagina.
    `ARMADILHA` vence tudo: construir em consulta de outra intencao e erro mesmo com dado.
    """
    classes = [m["classificacao"] for m in medicoes]
    if not classes:
        return "SEM_MEDICAO"
    if "ARMADILHA" in classes:
        return "ARMADILHA"
    for c in ESCADA_DA_SERP:
        if c in classes:
            return c
    return "SEM_MEDICAO"


def cruzar(veredito_de_dado, classe_de_serp):
    """O veredito unico. Duas entradas de arquivos diferentes, uma saida."""
    passa = veredito_de_dado == "passa"
    if classe_de_serp == "ARMADILHA":
        return "nunca"
    if passa and classe_de_serp == "ABERTA":
        return "pode_nascer"
    if passa and classe_de_serp == "ABERTA_SEM_INTENCAO_NA_SERP":
        return "pode_nascer_sem_demanda_medida"
    if passa and classe_de_serp == "TOMADA":
        return "espera_autoridade"
    if passa:
        # `NAO_MEDIDA` e `SEM_MEDICAO` caem aqui, e e o caso que mais custou nesta ilha:
        # dado verde com SERP nunca olhada parece passe livre e nao e.
        return "espera_serp"
    if classe_de_serp in ("ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP"):
        return "espera_dado"
    if classe_de_serp == "TOMADA":
        return "sem_nenhum_dos_dois"
    return "sem_nenhum_dos_dois"


def falta_no_dado(recorte_dado):
    """O que falta do lado do BANCO, derivado da distancia que o portao de dado ja mediu.

    Esta funcao existe separada porque a mesma frase e devida em DOIS vereditos
    (`espera_dado` e `sem_nenhum_dos_dois`), e a primeira versao desta ferramenta cravou
    "nem 3 itens de banco" no segundo — o que era FALSO em `alicate/torques` e
    `rejunte/cimenticio`, que tem 3 itens e param por lastro. Achado na leitura do proprio
    documento gerado, em 02/10/2026, antes de qualquer commit.
    """
    d = recorte_dado["a_que_distancia_esta"]
    if d["itens_que_faltam_para_3"]:
        return "%d item(ns) de banco neste recorte" % d["itens_que_faltam_para_3"]
    if d["itens_com_lastro_que_faltam_para_3"]:
        return ("%d item(ns) com fonte que sustente recomendacao primaria"
                % d["itens_com_lastro_que_faltam_para_3"])
    return ("um numero que a pagina calcule sobre 3 itens do mesmo recorte (a propriedade "
            "mais perto e `%s`)" % (d["propriedade_mais_perto_de_ser_numero"] or "nenhuma"))


def o_que_falta(veredito, recorte_dado, medicoes):
    """A frase do que falta, derivada — nunca digitada por recorte."""
    if veredito == "pode_nascer":
        return "nada: os dois portoes abriram"
    if veredito == "pode_nascer_sem_demanda_medida":
        return ("a faixa de volume das consultas abertas — a chance esta medida e a intencao "
                "nao. Pedido ao Raphael, derivado abaixo")
    if veredito == "espera_autoridade":
        return "autoridade de dominio: quem ocupa a SERP e marketplace, loja ou fabricante"
    if veredito == "espera_dado":
        return falta_no_dado(recorte_dado)
    if veredito == "espera_serp":
        if medicoes:
            return ("uma consulta MEDIDA: as %d tentativas deste recorte falharam por "
                    "instrumento, nao por concorrente" % len(medicoes))
        return "olhar a SERP: o dado passa e ninguem classificou quem ocupa o top 10"
    if veredito == "nunca":
        return "nada — e outra intencao, e entra como termo negativo"
    # `sem_nenhum_dos_dois`: os DOIS lados, e o do dado sai derivado — nunca cravado.
    lado_da_serp = ("%d consulta(s) medida(s) e nenhuma aberta" % len(medicoes)) if medicoes \
        else "a SERP nunca foi olhada"
    return "os dois: %s, e %s" % (falta_no_dado(recorte_dado), lado_da_serp)


def montar(dado, serp):
    por_recorte = {r["recorte"]: r for r in dado["recortes"]}
    medicoes_por_recorte = {}
    for m in serp["medicoes"]:
        medicoes_por_recorte.setdefault(m["recorte"], []).append(m)

    # Toda medicao de SERP tem de cair num recorte que o portao de dado conhece. Medicao de
    # recorte inexistente e consulta orfa — e orfa passa despercebida justamente no arquivo
    # que decide o que nasce.
    orfas = sorted(set(medicoes_por_recorte) - set(por_recorte))

    linhas = []
    for nome in sorted(por_recorte):
        r = por_recorte[nome]
        medicoes = medicoes_por_recorte.get(nome, [])
        classe = serp_do_recorte(medicoes)
        veredito = cruzar(r["veredito"], classe)
        sem_faixa = [m["consulta"] for m in medicoes
                     if m["classificacao"] in ("ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP")
                     and not m.get("faixa_de_volume")]
        linhas.append({
            "recorte": nome,
            "veredito_de_dado": r["veredito"],
            "itens_no_banco": r["itens_no_banco"],
            "classe_de_serp": classe,
            "consultas_medidas": len(medicoes),
            "veredito": veredito,
            "o_que_falta": o_que_falta(veredito, r, medicoes),
            "consultas_abertas_sem_faixa": sem_faixa,
            "numeros_que_a_serp_nao_publica": [m["numero_que_a_serp_nao_publica"] for m in medicoes
                                               if m.get("numero_que_a_serp_nao_publica")],
        })

    # O PEDIDO AO RAPHAEL, derivado: so consulta ABERTA (ou aberta sem intencao) e sem faixa
    # entra. Consulta TOMADA sem faixa nao vira pedido — faixa de consulta que nao vai nascer
    # e numero que ninguem usa, e pedido inflado e pedido atendido pela metade.
    pedido = []
    for l in linhas:
        for c in l["consultas_abertas_sem_faixa"]:
            pedido.append({"consulta": c, "exigida_por": l["recorte"], "veredito": l["veredito"]})

    contagem = {}
    for l in linhas:
        contagem[l["veredito"]] = contagem.get(l["veredito"], 0) + 1

    return {
        "id": "cruzamento-14-9",
        "ilha": dado["ilha"],
        "gerado_por": "ferramentas/cruzamento-14-9.py",
        "derivado_de": ["dados/filhas-do-guia.json", "dados/serp-das-filhas.json"],
        "recortes": linhas,
        "medicoes_de_serp_orfas": orfas,
        "resumo": {
            "vereditos": contagem,
            "podem_nascer": [l["recorte"] for l in linhas if l["veredito"] == "pode_nascer"],
            "podem_nascer_sem_demanda_medida": [l["recorte"] for l in linhas
                                                if l["veredito"] == "pode_nascer_sem_demanda_medida"],
            "quando_houver_autoridade": [l["recorte"] for l in linhas
                                         if l["veredito"] == "espera_autoridade"],
            "dado_verde_e_serp_nunca_olhada": [l["recorte"] for l in linhas
                                               if l["veredito"] == "espera_serp"],
            "pedido_de_faixa_ao_raphael": pedido,
        },
    }


# ------------------------------------------------------------------ a 16.5, que e da mae

def mae_pode_nascer(c, categorias_do_dado):
    """A 16.5 pede 3 filhas de nivel 3 para a mae de nivel 2 nascer. E o cruzamento muda a
    pergunta: 3 filhas que PASSAM NO DADO nao sao 3 filhas que podem nascer.

    Devolve, por categoria: quantas filhas o dado autoriza, quantas o CRUZAMENTO autoriza, e
    se a mae pode nascer. A diferenca entre os dois numeros e o que nenhum dos dois arquivos
    de entrada mostra sozinho.
    """
    por_recorte = {l["recorte"]: l for l in c["recortes"]}
    saida = {}
    for cat, info in sorted(categorias_do_dado.items()):
        filhas_no_dado = info["tipos_que_passam_quais"]
        filhas_no_cruzamento = [f for f in filhas_no_dado
                                if por_recorte.get(f, {}).get("veredito") in VEREDITOS_QUE_AUTORIZAM]
        mae = por_recorte.get(cat, {})
        saida[cat] = {
            "filhas_que_o_dado_autoriza": len(filhas_no_dado),
            "filhas_que_o_cruzamento_autoriza": len(filhas_no_cruzamento),
            "quais_o_cruzamento_autoriza": filhas_no_cruzamento,
            "veredito_da_mae": mae.get("veredito", "sem_nenhum_dos_dois"),
            "a_mae_pode_nascer": (len(filhas_no_cruzamento) >= 3
                                  and mae.get("veredito") in VEREDITOS_QUE_AUTORIZAM),
        }
    return saida


# ------------------------------------------------------------------ o documento

def gerar_md(c, maes):
    L = []
    A = L.append
    A("# O cruzamento da 14.9 — os dois portoes no mesmo veredito")
    A("")
    A("**GERADO por `ferramentas/cruzamento-14-9.py`. Nao edite a mao: `--conferir` regera e")
    A("compara.** As entradas sao `dados/filhas-do-guia.json` (o portao de DADO da secao 9,")
    A("derivado do banco) e `dados/serp-das-filhas.json` (o portao de SERP da 14.9, coletado por")
    A("busca). A 14.9 manda cruzar os dois — *\"nunca de uma so\"* — e ate 02/10/2026 ninguem")
    A("cruzava: uma metade era numero e a outra era prosa.")
    A("")
    A("## O numero que manda")
    A("")
    A("| veredito | recortes |")
    A("|---|---|")
    for v, n in sorted(c["resumo"]["vereditos"].items(), key=lambda kv: -kv[1]):
        A("| `%s` | %d |" % (v, n))
    A("")
    A("**Podem nascer hoje, pelos DOIS portoes:** %s"
      % (", ".join("`%s`" % x for x in c["resumo"]["podem_nascer"]) or "nenhum"))
    A("")
    A("**Podem nascer, mas sem demanda medida:** %s"
      % (", ".join("`%s`" % x for x in c["resumo"]["podem_nascer_sem_demanda_medida"]) or "nenhum"))
    A("")
    A("**Quando houver autoridade:** %s"
      % (", ".join("`%s`" % x for x in c["resumo"]["quando_houver_autoridade"]) or "nenhum"))
    A("")
    A("**Dado verde e SERP nunca olhada** — o caso que mais custou nesta ilha, porque parece")
    A("passe livre: %s"
      % (", ".join("`%s`" % x for x in c["resumo"]["dado_verde_e_serp_nunca_olhada"]) or "nenhum"))
    A("")
    A("## A 16.5 — a mae de nivel 2 so nasce com 3 filhas, e filha nao e filha no dado: e no cruzamento")
    A("")
    A("| categoria | filhas que o DADO autoriza | filhas que o CRUZAMENTO autoriza | veredito da mae | a mae pode nascer |")
    A("|---|---|---|---|---|")
    for cat, m in maes.items():
        A("| `%s` | %d | %d | `%s` | %s |"
          % (cat, m["filhas_que_o_dado_autoriza"], m["filhas_que_o_cruzamento_autoriza"],
             m["veredito_da_mae"], "**SIM**" if m["a_mae_pode_nascer"] else "nao"))
    A("")
    A("## Recorte por recorte")
    A("")
    A("| recorte | dado | itens | SERP | consultas medidas | veredito | o que falta |")
    A("|---|---|---|---|---|---|---|")
    for l in c["recortes"]:
        A("| `%s` | `%s` | %d | `%s` | %d | **`%s`** | %s |"
          % (l["recorte"], l["veredito_de_dado"], l["itens_no_banco"], l["classe_de_serp"],
             l["consultas_medidas"], l["veredito"], l["o_que_falta"]))
    A("")
    A("## O pedido de faixa de volume, derivado — nao digitado")
    A("")
    A("A 14.9 cruza intencao com chance. A chance esta medida na SERP; a **intencao** se mede")
    A("por faixa de volume, e o Planejador de palavras-chave esta na conta do Raphael, no")
    A("navegador dele. Onde a faixa falta, esta ferramenta nao estima: ela deriva o pedido. **So")
    A("consulta ABERTA entra** — faixa de consulta que nao vai nascer e numero que ninguem usa.")
    A("")
    pedido = c["resumo"]["pedido_de_faixa_ao_raphael"]
    if pedido:
        A("| consulta | exigida pelo recorte | veredito do recorte |")
        A("|---|---|---|")
        for p in pedido:
            A("| `%s` | `%s` | `%s` |" % (p["consulta"], p["exigida_por"], p["veredito"]))
    else:
        A("Nenhuma: toda consulta aberta deste arquivo tem faixa medida.")
    A("")
    A("## Os numeros que a SERP nao publica e o banco desta ilha publica")
    A("")
    A("E a resposta da 14.9 a pergunta *\"por que ela consegue chegar as 10 primeiras\"*, recorte")
    A("por recorte, com o numero na mao em vez do adjetivo.")
    A("")
    for l in c["recortes"]:
        for n in l["numeros_que_a_serp_nao_publica"]:
            A("- **`%s`** — %s" % (l["recorte"], n))
    A("")
    if c["medicoes_de_serp_orfas"]:
        A("## MEDICOES DE SERP ORFAS — consulta medida em recorte que o portao de dado nao conhece")
        A("")
        for o in c["medicoes_de_serp_orfas"]:
            A("- `%s`" % o)
        A("")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ autoteste

def _recorte(nome, veredito, itens=3, faltam=0, lastro=0, prop=None):
    return {"recorte": nome, "veredito": veredito, "itens_no_banco": itens,
            "a_que_distancia_esta": {"itens_que_faltam_para_3": faltam,
                                     "itens_com_lastro_que_faltam_para_3": lastro,
                                     "propriedade_mais_perto_de_ser_numero": prop}}


def _medicao(recorte, classe, faixa=None, numero=None, consulta="c"):
    return {"recorte": recorte, "consulta": consulta, "classificacao": classe,
            "faixa_de_volume": faixa, "numero_que_a_serp_nao_publica": numero}


def autoteste():
    """Entradas fabricadas. Passada limpa em portao que nunca acusou nada nao prova nada."""
    falhas = 0
    print("A REGUA DO CRUZAMENTO — as 4 x 5 combinacoes que importam, e nenhuma delas e opiniao:")
    casos = [
        ("passa", "ABERTA", "pode_nascer"),
        ("passa", "ABERTA_SEM_INTENCAO_NA_SERP", "pode_nascer_sem_demanda_medida"),
        ("passa", "TOMADA", "espera_autoridade"),
        ("passa", "NAO_MEDIDA", "espera_serp"),
        ("passa", "SEM_MEDICAO", "espera_serp"),
        ("passa", "ARMADILHA", "nunca"),
        ("passa_na_contagem_sem_lastro", "ABERTA", "espera_dado"),
        ("passa_na_contagem_sem_lastro", "ABERTA_SEM_INTENCAO_NA_SERP", "espera_dado"),
        ("passa_na_contagem_sem_lastro", "TOMADA", "sem_nenhum_dos_dois"),
        ("passa_na_contagem_sem_lastro", "ARMADILHA", "nunca"),
        ("nao_passa", "ABERTA", "espera_dado"),
        ("nao_passa", "TOMADA", "sem_nenhum_dos_dois"),
        ("nao_passa", "NAO_MEDIDA", "sem_nenhum_dos_dois"),
        ("nao_passa", "SEM_MEDICAO", "sem_nenhum_dos_dois"),
        ("nao_passa", "ARMADILHA", "nunca"),
    ]
    for i, (dado, serp, esperado) in enumerate(casos, 1):
        obtido = cruzar(dado, serp)
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s caso %2d  dado=%-28s serp=%-28s -> %-30s (esperado %s)"
              % ("ok  " if ok else "FALHA", i, dado, serp, obtido, esperado))

    print("")
    print("A PRECEDENCIA ENTRE CONSULTAS DO MESMO RECORTE — vale a MELHOR, e a ARMADILHA vence tudo:")
    prec = [
        ([], "SEM_MEDICAO"),
        (["NAO_MEDIDA"], "NAO_MEDIDA"),
        (["NAO_MEDIDA", "ABERTA"], "ABERTA"),
        (["TOMADA", "ABERTA"], "ABERTA"),
        (["TOMADA", "ABERTA_SEM_INTENCAO_NA_SERP"], "ABERTA_SEM_INTENCAO_NA_SERP"),
        (["ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP"], "ABERTA"),
        (["ABERTA", "ARMADILHA"], "ARMADILHA"),
        (["TOMADA", "NAO_MEDIDA", "ARMADILHA"], "ARMADILHA"),
        (["TOMADA", "TOMADA"], "TOMADA"),
    ]
    for i, (classes, esperado) in enumerate(prec, 1):
        obtido = serp_do_recorte([_medicao("x", c) for c in classes])
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s prec %2d  %-55s -> %-28s (esperado %s)"
              % ("ok  " if ok else "FALHA", i, str(classes), obtido, esperado))

    print("")
    print("A 16.5 — e o caso que o portao de dado sozinho nao ve: 3 filhas verdes no dado e 2 no cruzamento:")
    dado = {"ilha": "x", "recortes": [
        _recorte("acab", "passa"),
        _recorte("acab/a", "passa"), _recorte("acab/b", "passa"), _recorte("acab/c", "passa"),
    ]}
    serp = {"medicoes": [
        _medicao("acab", "ABERTA"), _medicao("acab/a", "ABERTA"),
        _medicao("acab/b", "ABERTA"), _medicao("acab/c", "TOMADA"),
    ]}
    cats = {"acab": {"tipos_que_passam_quais": ["acab/a", "acab/b", "acab/c"]}}
    m = mae_pode_nascer(montar(dado, serp), cats)["acab"]
    for rotulo, obtido, esperado in (
            ("filhas que o DADO autoriza", m["filhas_que_o_dado_autoriza"], 3),
            ("filhas que o CRUZAMENTO autoriza", m["filhas_que_o_cruzamento_autoriza"], 2),
            ("a mae pode nascer", m["a_mae_pode_nascer"], False)):
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s %-34s -> %-6s (esperado %s)"
              % ("ok  " if ok else "FALHA", rotulo, obtido, esperado))

    serp["medicoes"][3] = _medicao("acab/c", "ABERTA_SEM_INTENCAO_NA_SERP")
    m = mae_pode_nascer(montar(dado, serp), cats)["acab"]
    for rotulo, obtido, esperado in (
            ("com a 3a filha sem demanda medida", m["filhas_que_o_cruzamento_autoriza"], 3),
            ("a mae pode nascer", m["a_mae_pode_nascer"], True)):
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s %-34s -> %-6s (esperado %s)"
              % ("ok  " if ok else "FALHA", rotulo, obtido, esperado))

    # E A MAE TOMADA COM TRES FILHAS ABERTAS: a 16.5 conta filha, o cruzamento conta a mae
    # tambem, e sem isso a mae nasceria para uma SERP de marketplace.
    serp["medicoes"][0] = _medicao("acab", "TOMADA")
    m = mae_pode_nascer(montar(dado, serp), cats)["acab"]
    ok = m["a_mae_pode_nascer"] is False and m["filhas_que_o_cruzamento_autoriza"] == 3
    falhas += 0 if ok else 1
    print("  %s mae TOMADA com 3 filhas abertas    -> %-6s (esperado False)"
          % ("ok  " if ok else "FALHA", m["a_mae_pode_nascer"]))

    print("")
    print("O PEDIDO DE FAIXA — derivado, e so de consulta ABERTA:")
    dado2 = {"ilha": "x", "recortes": [_recorte("a", "passa"), _recorte("b", "passa"),
                                       _recorte("c", "nao_passa", itens=0, faltam=3)]}
    serp2 = {"medicoes": [
        _medicao("a", "ABERTA", consulta="aberta sem faixa"),
        _medicao("a", "ABERTA", faixa="100-1.000", consulta="aberta com faixa"),
        _medicao("b", "TOMADA", consulta="tomada sem faixa"),
        _medicao("c", "ABERTA_SEM_INTENCAO_NA_SERP", consulta="sem intencao e sem faixa"),
    ]}
    p = montar(dado2, serp2)["resumo"]["pedido_de_faixa_ao_raphael"]
    obtido = sorted(x["consulta"] for x in p)
    esperado = ["aberta sem faixa", "sem intencao e sem faixa"]
    ok = obtido == esperado
    falhas += 0 if ok else 1
    print("  %s pedido -> %s" % ("ok  " if ok else "FALHA", obtido))
    print("       (esperado %s — `tomada sem faixa` e `aberta com faixa` ficam fora)" % esperado)

    print("")
    print("A MEDICAO ORFA — consulta num recorte que o portao de dado nao conhece:")
    orfas = montar({"ilha": "x", "recortes": [_recorte("a", "passa")]},
                   {"medicoes": [_medicao("a", "ABERTA"), _medicao("inventado/x", "ABERTA")]})
    obtido = orfas["medicoes_de_serp_orfas"]
    ok = obtido == ["inventado/x"]
    falhas += 0 if ok else 1
    print("  %s orfas -> %s (esperado ['inventado/x'])" % ("ok  " if ok else "FALHA", obtido))

    total = len(casos) + len(prec) + 3 + 2 + 1 + 1 + 1
    print("")
    if falhas:
        print("REPROVADO: %d de %d casos falharam." % (falhas, total))
        return 1
    print("APROVADO: %d casos fabricados, 0 falha." % total)
    return 0


# ------------------------------------------------------------------ main

def main(argv):
    if "--autoteste" in argv:
        return autoteste()

    with io.open(ENTRADA_DADO, encoding="utf-8") as f:
        dado = json.load(f)
    with io.open(ENTRADA_SERP, encoding="utf-8") as f:
        serp = json.load(f)

    c = montar(dado, serp)
    maes = mae_pode_nascer(c, dado["resumo"]["por_categoria_do_guia"])
    md = gerar_md(c, maes)

    if "--conferir" in argv:
        falhas = []
        if not os.path.exists(SAIDA_MD):
            falhas.append("dados/cruzamento-14-9.md nao existe")
        else:
            with io.open(SAIDA_MD, encoding="utf-8") as f:
                if f.read() != md:
                    falhas.append("dados/cruzamento-14-9.md nao fecha com a propria derivacao")
        if c["medicoes_de_serp_orfas"]:
            falhas.append("dados/serp-das-filhas.json mede recorte que o portao de dado nao conhece: %s"
                          % ", ".join(c["medicoes_de_serp_orfas"]))
        for f_ in falhas:
            print("  FALHA %s" % f_)
        if falhas:
            print("")
            print("REPROVADO: %d falha(s). Rode sem --conferir para regerar." % len(falhas))
            return 1
        print("  ok   dados/cruzamento-14-9.md fecha com as duas entradas de hoje")
        print("  ok   nenhuma medicao de SERP em recorte que o portao de dado nao conhece")
        print("")
        print("APROVADO: o cruzamento fecha com a derivacao.")
        return 0

    with io.open(SAIDA_MD, "w", encoding="utf-8") as f:
        f.write(md)

    print("Recortes cruzados: %d" % len(c["recortes"]))
    for v, n in sorted(c["resumo"]["vereditos"].items(), key=lambda kv: -kv[1]):
        print("  %-32s %d" % (v, n))
    print("")
    print("Podem nascer pelos DOIS portoes: %s"
          % (", ".join(c["resumo"]["podem_nascer"]) or "nenhum"))
    print("Podem nascer sem demanda medida: %s"
          % (", ".join(c["resumo"]["podem_nascer_sem_demanda_medida"]) or "nenhum"))
    print("Dado verde e SERP nunca olhada:  %s"
          % (", ".join(c["resumo"]["dado_verde_e_serp_nunca_olhada"]) or "nenhum"))
    print("")
    for cat, m in maes.items():
        print("  16.5  %-12s dado %d filha(s), cruzamento %d -> mae %s"
              % (cat, m["filhas_que_o_dado_autoriza"], m["filhas_que_o_cruzamento_autoriza"],
                 "PODE NASCER" if m["a_mae_pode_nascer"] else "espera"))
    print("")
    print("Pedido de faixa ao Raphael: %d consulta(s) aberta(s) sem faixa medida"
          % len(c["resumo"]["pedido_de_faixa_ao_raphael"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROSPECCAO DO WIDGET -- implementacao de REFERENCIA do bloco 6 da jornadafly.

A secao 14.7 do ARQUIPELAGO.md diz que a prospeccao do widget em lojas e a UNICA
alavanca de link do projeto. Este arquivo e o cerebro dessa lista nesta ilha:
dado o banco de candidatos (dados/prospeccao-widget.json) e o BANCO DE
EXPERIENCIAS (dados/experiencias.json), ele devolve, para cada dominio, a
PRIORIDADE e as FERRAMENTAS OFERTAVEIS -- e a prosa inteira do arquivo de leitura,
ja em frase acentuada.

    python3 ferramentas/prospeccao-referencia.py            # o resumo da lista
    python3 ferramentas/prospeccao-referencia.py --contar    # as contagens
    python3 ferramentas/prospeccao-referencia.py <dominio>   # uma linha inteira
    python3 ferramentas/prospeccao-referencia.py --texto     # o .md inteiro na tela

POR QUE A PRIORIDADE NAO E CAMPO DO JSON, e isto e a decisao desta ferramenta:
prioridade escrita a mao e opiniao com cara de dado, e ela envelhece calada --
no dia em que alguem medir uma pagina em pt-BR de um candidato, a prioridade
dele muda e ninguem reescreve a mao. Aqui ela e DERIVADA dos fatos medidos, e o
portao `validar-prospeccao.py` REPROVA se encontrar `prioridade` dentro de uma
linha do banco. E a mesma troca da versao 5 do experiencias.json, um andar
acima: o que sai da prosa para o campo nao e o numero, e O QUE DECIDE o numero.

AS DUAS REGUAS QUE ATRAVESSAM ESTE ARQUIVO
------------------------------------------
1. A ESCADA DA PRIORIDADE. Ela comeca pelo BARRAMENTO, e o barramento sai de uma
   decisao que esta ilha ja tinha escrito no bloco 1: de seis clusters medidos,
   a ilha declarou que NAO disputa um -- o A2, «quanto custa <experiencia>» --,
   porque «disputar 'quanto custa o ingresso X' contra o operador e perder, e
   nao e preciso». Quem ocupa consulta de cluster DISPUTADO nao hospeda a
   ferramenta que o disputa: e barrado, com a consulta nomeada. E o mesmo
   raciocinio da lista da aquametria («loja que ja construiu a propria
   calculadora nao instala a de ninguem»), com uma diferenca que importa: la o
   impedimento era um produto concorrente, aqui e uma CONSULTA concorrente.

2. A REGUA DA OFERTA, e ela le o BANCO em vez de acreditar nesta lista. Nenhuma
   ferramenta e oferecida se a ilha nao souber servi-la hoje:
     - F1 so vai a quem vende A MESMA versao que o banco preca. Quem vende versao
       que INCLUI a do banco (tour guiado com o ingresso dentro) receberia da F1
       um numero que compete com o proprio preco, e ferramenta que mina o
       anfitriao nao se oferece ao anfitriao;
     - F2 so existe se o banco tiver FAIXA_DIARIA. Tem zero;
     - F3 so existe se o banco tiver passe E cobertura, e NUNCA vai a quem vende
       passe de cidade, porque o veredito dela pode ser «nao vale».
   As contagens sao LIDAS do experiencias.json em toda passada. Nenhuma delas e
   escrita aqui nem no banco de candidatos: duas metades que contam a mesma
   coisa sem nunca se falarem e o defeito que esta ilha mais paga.

O QUE ESTE ARQUIVO NAO FAZ, de proposito:
  - NAO escreve abordagem, e-mail nem texto de contato. Nenhum site foi aberto
    (egresso recusa todos os candidatos, medido as 13h28:28Z de 23/10/2026), e
    abordagem escrita sobre site nao lido e invencao com cara de trabalho;
  - NAO afirma ausencia. Campo de fato aceita `true` ou `null`, nunca `false`;
  - NAO publica nada. `publicar: false` no banco, e esta ilha nao tem site.
"""

import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tipos que podem HOSPEDAR a ferramenta. Fora desta lista, o candidato nao sobe
# da prioridade 3 -- e o motivo e diferente em cada familia, por isso a prosa.
TIPOS_QUE_HOSPEDAM = (
    "operador_da_experiencia",
    "receptivo",
    "concessionaria_de_bem_publico",
    "guia_autorizado",
    "pousada",
)

# Tipos que NUNCA hospedam, com a razao de cada um escrita uma vez.
POR_QUE_NAO_HOSPEDA = {
    "plataforma": "plataforma nao instala ferramenta de afiliado: ela e o destino do link, nao a casa dele",
    "revendedor_de_ingresso": "revendedor vive do spread entre a tarifa oficial e o que cobra, e esta ferramenta publica a tarifa oficial com data de leitura",
    "revendedor_de_passe": "revendedor de passe vive de vender o passe, e a F3 pode responder que ele nao compensa",
    "portal_de_conteudo": "portal de conteudo nao vende experiencia: o widget nao lhe traz receita, e ele costuma disputar a mesma consulta",
    "imprensa_de_trade": "imprensa de trade nao e alvo de widget; ela e o instrumento que acha o candidato que a SERP de consumidor esconde",
}

TIPOS_VALIDOS = tuple(sorted(set(TIPOS_QUE_HOSPEDAM) | set(POR_QUE_NAO_HOSPEDA)))

CAMPOS_DE_FATO = (
    "brasileiro",
    "fala_pt_br",
    "site_proprio",
    "vende_experiencia",
    "mais_de_uma_versao_vendida",
    "publica_conteudo_proprio",
    "vende_passe_de_cidade",
)

RELACOES_VALIDAS = (
    "vende_a_mesma_versao",
    "vende_versao_que_inclui_a_do_banco",
    "nao_medido",
    "nao_se_aplica",
)

# Campos DERIVADOS. Se aparecerem gravados no banco, o portao reprova.
CAMPOS_PROIBIDOS_NO_BANCO = ("prioridade", "ferramentas_ofertaveis", "veredito", "classe")


def carregar(raiz=RAIZ):
    """Devolve (banco de candidatos, banco de experiencias)."""
    with open(os.path.join(raiz, "dados", "prospeccao-widget.json"), encoding="utf-8") as f:
        banco = json.load(f)
    with open(os.path.join(raiz, "dados", "experiencias.json"), encoding="utf-8") as f:
        experiencias = json.load(f)
    return banco, experiencias


# ---------------------------------------------------------------- o banco lido

def estado_do_banco(experiencias):
    """O que o BANCO DE EXPERIENCIAS tem hoje -- contado, nunca afirmado."""
    exp = experiencias.get("experiencias", []) or []
    return {
        "ids": [e.get("id") for e in exp],
        "experiencias": len(exp),
        "versoes": sum(len(e.get("versoes", []) or []) for e in exp),
        "faixas_diarias": len(experiencias.get("faixas_diarias", []) or []),
        "coberturas_de_passe": len(experiencias.get("coberturas_de_passe", []) or []),
        "passes_de_cidade": len([e for e in exp if e.get("categoria") == "passe_de_cidade"]),
        "operadores_de_poder_publico": len(
            [e for e in exp if (e.get("operador") or {}).get("tipo") == "poder_publico"]
        ),
    }


# ------------------------------------------------------------- a escada da 1a

def cluster_da_consulta(banco, consulta):
    """Em que cluster do corpus esta consulta foi medida. None = nao esta no corpus."""
    for cluster, consultas in banco["consultas_do_corpus_por_cluster"].items():
        if consulta in consultas:
            return cluster
    return None


def clusters_disputados_do_candidato(banco, candidato):
    """Os clusters DISPUTADOS que este candidato ocupa, com a consulta de cada um."""
    disputados = banco["a_regra_que_ordena_esta_lista"]["clusters_disputados"]
    achados = []
    for consulta in candidato.get("consultas_do_corpus", []) or []:
        cluster = cluster_da_consulta(banco, consulta)
        if cluster in disputados:
            achados.append((cluster, consulta))
    return achados


def prioridade(banco, candidato):
    """A escada da prioridade. Devolve (classe, motivo acentuado).

    A ORDEM IMPORTA e e a razao desta funcao ser uma escada e nao uma soma de
    pontos: o barramento ganha de qualquer qualificacao. O caso que obriga a
    ordem esta medido no banco -- o romapravoce.com e operador E concorrente ao
    mesmo tempo, e tratar os dois lados como pesos somaveis o deixaria passar.
    """
    barrados = clusters_disputados_do_candidato(banco, candidato)
    if barrados:
        nomes = "; ".join("%s («%s»)" % (c, q) for c, q in barrados)
        return "barrado", (
            "Ocupa consulta de cluster que esta ilha DISPUTA — %s. Quem ocupa a consulta "
            "não hospeda a ferramenta que a disputa." % nomes
        )

    tipo = candidato.get("tipo")
    if tipo is None:
        return "3", (
            "Tipo não medido. O corpus não o rotulou e nenhuma busca desta passada o "
            "rotulou — e o nome do domínio não é evidência de tipo."
        )
    if tipo in POR_QUE_NAO_HOSPEDA:
        return "3", "Tipo `%s`: %s." % (tipo, POR_QUE_NAO_HOSPEDA[tipo])
    if candidato.get("site_proprio") is not True:
        return "3", (
            "Site próprio não medido. A fila do bloco 6 pede «com site próprio», e sem "
            "essa medição não há onde instalar nada."
        )

    if candidato.get("brasileiro") is True:
        if candidato.get("vende_experiencia") is True and candidato.get("mais_de_uma_versao_vendida") is True:
            return "1", (
                "Fecha as cinco condições: brasileiro, tipo que hospeda, site próprio, vende "
                "experiência e mais de uma versão da mesma experiência à venda — que é o eixo "
                "da F1 (dias × pessoas × padrão). E não ocupa consulta disputada."
            )
        falta = []
        if candidato.get("vende_experiencia") is not True:
            falta.append("se vende experiência")
        if candidato.get("mais_de_uma_versao_vendida") is not True:
            falta.append("mais de uma versão vendida")
        return "2", (
            "Brasileiro com site próprio e tipo que hospeda, medido pela metade: falta %s. "
            "Uma medição o move." % " e ".join(falta)
        )

    if candidato.get("fala_pt_br") is True:
        return "2", (
            "Não é brasileiro, e sobe à 2 porque tem página em pt-BR MEDIDA: quem mantém "
            "árvore em português atende o público desta ilha."
        )
    return "3", (
        "Não é brasileiro e página em pt-BR não foi medida. A fila do bloco 6 pede "
        "brasileiros; afirmar que ele tem página em português seria adivinhar, e afirmar "
        "que não tem seria pior, porque busca não sabe afirmar ausência."
    )


# ------------------------------------------------------------ a regua da 2a

def ferramentas_ofertaveis(banco, estado, candidato):
    """Para cada ferramenta, se ela pode ser oferecida a este candidato e por que.

    Devolve lista de dicts na ordem F1, F2, F3. `ofertavel` e sempre bool; o
    `por_que` nomeia a UNICA razao que falta, quando falta uma so, porque e ela
    que diz o que destrava a linha.
    """
    classe, _ = prioridade(banco, candidato)
    saida = []

    atendidas = [i for i in (candidato.get("experiencias_do_banco_atendidas") or []) if i in estado["ids"]]
    relacao = candidato.get("relacao_com_a_versao_do_banco")

    # ---- F1
    if classe in ("barrado", "3"):
        f1 = (False, "Prioridade %s: a ferramenta não é oferecida a quem a escada não qualifica." % classe)
    elif estado["experiencias"] == 0:
        f1 = (False, "O banco não tem nenhuma experiência gravada.")
    elif not atendidas:
        f1 = (False, "Atende experiência que O BANCO NÃO TEM — sem registro no banco a F1 não responde nada na página dele.")
    elif relacao == "vende_versao_que_inclui_a_do_banco":
        f1 = (False, "Vende versão que INCLUI a do banco: a F1 serviria, ao visitante dele, o preço da versão barata que o produto dele embute.")
    elif relacao != "vende_a_mesma_versao":
        f1 = (False, "Relação com a versão do banco não medida (`%s`): sem isso não se sabe se a conta ajuda ou compete com ele." % relacao)
    else:
        f1 = (True, "Vende a mesma versão que o banco preça (%s), e a F1 responde o que ele não responde: qual versão sai melhor para este grupo." % ", ".join(atendidas))
    saida.append({"ferramenta": "F1", "ofertavel": f1[0], "por_que": f1[1]})

    # ---- F2
    if estado["faixas_diarias"] == 0:
        f2 = (False, "O banco tem ZERO FAIXA_DIARIA: a F2 publica uma linha de quatro e recusa as outras três pelo nome.")
    elif classe in ("barrado", "3"):
        f2 = (False, "Prioridade %s." % classe)
    else:
        f2 = (True, "O banco tem %d faixa(s) diária(s) e a escada o qualifica." % estado["faixas_diarias"])
    saida.append({"ferramenta": "F2", "ofertavel": f2[0], "por_que": f2[1]})

    # ---- F3
    if candidato.get("vende_passe_de_cidade") is True:
        f3 = (False, "VENDE PASSE DE CIDADE: a F3 pode responder «não vale», e esse é o produto do anfitrião. Nunca.")
    elif estado["passes_de_cidade"] == 0 or estado["coberturas_de_passe"] == 0:
        f3 = (False, "O banco tem %d passe(s) e %d cobertura(s): a F3 não tem o que somar." % (estado["passes_de_cidade"], estado["coberturas_de_passe"]))
    elif classe in ("barrado", "3"):
        f3 = (False, "Prioridade %s." % classe)
    else:
        f3 = (True, "O banco tem passe e cobertura, e a escada o qualifica.")
    saida.append({"ferramenta": "F3", "ofertavel": f3[0], "por_que": f3[1]})

    return saida


def linha(banco, estado, candidato):
    """A linha inteira de um candidato, com o que e fato e o que e derivado."""
    classe, motivo = prioridade(banco, candidato)
    return {
        "dominio": candidato["dominio"],
        "nome": candidato["nome"],
        "tipo": candidato.get("tipo"),
        "pais": candidato.get("pais"),
        "origem": candidato["origem"],
        "prioridade": classe,
        "motivo_da_prioridade": motivo,
        "ferramentas": ferramentas_ofertaveis(banco, estado, candidato),
        "consultas_do_corpus": candidato.get("consultas_do_corpus", []),
        "motivos": candidato.get("motivos", []),
        "evidencias": candidato.get("evidencias", []),
        "fatos": {c: candidato.get(c) for c in CAMPOS_DE_FATO},
    }


def todas_as_linhas(banco, estado):
    return [linha(banco, estado, c) for c in banco["candidatos"]]


def contagens(banco, estado):
    linhas = todas_as_linhas(banco, estado)
    por_classe = {}
    for l in linhas:
        por_classe[l["prioridade"]] = por_classe.get(l["prioridade"], 0) + 1
    ofertaveis = {}
    for f in ("F1", "F2", "F3"):
        ofertaveis[f] = len([l for l in linhas if any(x["ferramenta"] == f and x["ofertavel"] for x in l["ferramentas"])])
    return {
        "candidatos": len(linhas),
        "por_prioridade": por_classe,
        "com_ferramenta_ofertavel": ofertaveis,
        "banco_de_experiencias": estado,
    }


# ------------------------------------------------------------------- o texto

def _tabela(linhas):
    cab = "| domínio | tipo | país | prioridade | F1 | F2 | F3 |\n|---|---|---|---|---|---|---|\n"
    corpo = ""
    for l in linhas:
        marca = {True: "sim", False: "não"}
        f = {x["ferramenta"]: marca[x["ofertavel"]] for x in l["ferramentas"]}
        corpo += "| `%s` | %s | %s | %s | %s | %s | %s |\n" % (
            l["dominio"],
            l["tipo"] or "não medido",
            l["pais"] or "não medido",
            l["prioridade"],
            f["F1"], f["F2"], f["F3"],
        )
    return cab + corpo


def texto(banco, estado):
    """O arquivo de leitura inteiro. E este texto que o gerador grava e o portao confere."""
    linhas = todas_as_linhas(banco, estado)
    c = contagens(banco, estado)
    achado = banco["o_achado_desta_passada"]
    regra = banco["a_regra_que_ordena_esta_lista"]

    p = []
    w = p.append
    w("# PROSPECÇÃO DO WIDGET — bloco 6 da JornadaFly, seção 14.7 do contrato\n")
    w("> **ARQUIVO GERADO por `ferramentas/prospeccao-referencia.py`, escrito por**")
    w("> **`ferramentas/gerar-prospeccao.py` a partir de `dados/prospeccao-widget.json`**")
    w("> **e de `dados/experiencias.json`. Não edite à mão:** o portão")
    w("> `validar-prospeccao.py` regera este texto e compara, e edição à mão fica vermelha.")
    w("> Mude o JSON e rode o gerador.\n")
    w("Gerado em **%s**. Nada aqui vai para o ar (`publicar: false`), e esta ilha" % banco["gerado_em"])
    w("não tem site para onde ir.\n")

    w("## O QUE MEDIU ISTO, E O QUE ELE NÃO ALCANÇA\n")
    w(banco["o_que_mediu_isto_e_o_que_ele_nao_alcanca"] + "\n")
    w(banco["presenca_nunca_ausencia"] + "\n")

    w("## A RÉGUA, E ELA NÃO É OPINIÃO\n")
    w("**A prioridade e as ferramentas ofertáveis não são campos do banco: são")
    w("derivadas.** Prioridade escrita à mão é opinião com cara de dado, e envelhece")
    w("calada — no dia em que alguém medir uma página em pt-BR de um candidato, a")
    w("prioridade dele muda e ninguém reescreve à mão. O portão reprova se achar")
    w("`prioridade` dentro de uma linha do banco.\n")
    w("**O barramento vem primeiro, e ele sai de uma decisão que esta ilha já tinha**")
    w("**escrito no bloco 1.** " + regra["resumo"] + "\n")
    w("- Clusters que a ilha **disputa**: %s." % ", ".join(regra["clusters_disputados"]))
    w("- Cluster que a ilha **declarou não disputar**: %s." % ", ".join(regra["clusters_nao_disputados"]))
    w("- De onde isso sai: %s\n" % regra["de_onde_ela_sai"])
    w(regra["por_que_so_o_A2"] + "\n")
    w("**A régua da oferta lê o BANCO, não esta lista.** " + banco["a_regra_da_oferta"]["resumo"])
    w("Hoje o banco tem **%d experiências** e **%d versões**, com **%d operador(es) de poder"
      % (estado["experiencias"], estado["versoes"], estado["operadores_de_poder_publico"]))
    w("público**, **%d faixa(s) diária(s)**, **%d passe(s) de cidade** e **%d cobertura(s) de passe**.\n"
      % (estado["faixas_diarias"], estado["passes_de_cidade"], estado["coberturas_de_passe"]))

    w("## O ACHADO DESTA PASSADA\n")
    w("**%s**\n" % achado["titulo"])
    for i, passo in enumerate(achado["a_cadeia"], 1):
        w("%d. %s" % (i, passo))
    w("")
    w("**O que isso custa:** " + achado["o_que_isso_custa"] + "\n")
    w("**O que destrava, e é barato:** " + achado["o_que_destrava_e_e_barato"] + "\n")
    w("**O que isso NÃO é:** " + achado["o_que_isso_nao_e"] + "\n")

    w("## A LISTA INTEIRA, EM UMA TABELA\n")
    w("%d candidatos: %s." % (
        c["candidatos"],
        ", ".join("%s em %s" % (c["por_prioridade"][k], "prioridade " + k if k != "barrado" else "barrado")
                  for k in sorted(c["por_prioridade"]))))
    w("Com ferramenta ofertável hoje: **F1 %d · F2 %d · F3 %d**.\n"
      % (c["com_ferramenta_ofertavel"]["F1"], c["com_ferramenta_ofertavel"]["F2"], c["com_ferramenta_ofertavel"]["F3"]))
    w(_tabela(linhas))

    titulos = [
        ("1", "PRIORIDADE 1 — as cinco condições medidas"),
        ("2", "PRIORIDADE 2 — medido pela metade, e uma medição move"),
        ("3", "PRIORIDADE 3 — não hospeda, ou não foi medido o suficiente para subir"),
        ("barrado", "BARRADOS — ocupam consulta que esta ilha disputa"),
    ]
    for classe, titulo in titulos:
        grupo = [l for l in linhas if l["prioridade"] == classe]
        w("## %s\n" % titulo)
        if not grupo:
            w("Nenhum candidato nesta faixa nesta passada.\n")
            continue
        for l in grupo:
            w("### %s — `%s`\n" % (l["nome"], l["dominio"]))
            w("**Por que nesta faixa:** %s\n" % l["motivo_da_prioridade"])
            for m in l["motivos"]:
                w("- %s" % m)
            w("")
            w("**Ferramenta ofertável hoje:**")
            for f in l["ferramentas"]:
                w("- **%s — %s.** %s" % (f["ferramenta"], "SIM" if f["ofertavel"] else "não", f["por_que"]))
            w("")
            w("**Evidência, uma por afirmação:**")
            for e in l["evidencias"]:
                w("- sustenta `%s` — %s, em %s, lido em %s: «%s»"
                  % ("`, `".join(e["afirma"]), e["como"], e["onde"], e["data_leitura"], e["diz"]))
            w("")

    nc = banco["dominios_do_corpus_nao_classificados"]
    w("## O QUE NÃO FOI CLASSIFICADO, dito como é\n")
    w(nc["por_que_existem"] + "\n")
    w(nc["o_que_a_maioria_deles_e"] + "\n")
    w("**" + nc["nao_e_lista_de_descarte"] + "**\n")
    w("## O PRÓXIMO PASSO DESTA LISTA NÃO É DA FUNDAÇÃO\n")
    w("Abrir cada domínio num navegador, confirmar canal de contato e plataforma, e só")
    w("então escrever a abordagem. Nenhum dos %d candidatos é alcançável desta nuvem," % c["candidatos"])
    w("e isso foi medido nesta execução, não herdado.")
    return "\n".join(p) + "\n"


# --------------------------------------------------------------------- linha de comando

def main(argv):
    banco, experiencias = carregar()
    estado = estado_do_banco(experiencias)

    if "--texto" in argv:
        sys.stdout.write(texto(banco, estado))
        return 0

    if "--contar" in argv:
        print(json.dumps(contagens(banco, estado), ensure_ascii=False, indent=2))
        return 0

    alvo = [a for a in argv[1:] if not a.startswith("--")]
    if alvo:
        for c in banco["candidatos"]:
            if c["dominio"] == alvo[0]:
                print(json.dumps(linha(banco, estado, c), ensure_ascii=False, indent=2))
                return 0
        print("dominio nao esta no banco: %s" % alvo[0])
        return 1

    c = contagens(banco, estado)
    print("PROSPECCAO DO WIDGET -- jornadafly, bloco 6")
    print("candidatos: %d" % c["candidatos"])
    for k in sorted(c["por_prioridade"]):
        print("  %-8s %d" % (k, c["por_prioridade"][k]))
    print("com ferramenta ofertavel hoje: F1 %d | F2 %d | F3 %d"
          % (c["com_ferramenta_ofertavel"]["F1"], c["com_ferramenta_ofertavel"]["F2"], c["com_ferramenta_ofertavel"]["F3"]))
    print("banco de experiencias: %d experiencias, %d versoes, %d faixas_diarias, %d passes, %d coberturas"
          % (estado["experiencias"], estado["versoes"], estado["faixas_diarias"],
             estado["passes_de_cidade"], estado["coberturas_de_passe"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

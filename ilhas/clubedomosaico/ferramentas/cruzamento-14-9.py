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


def tentativas_que_falharam(medicoes_proprias):
    """As consultas que ALGUEM JA TENTOU medir para esta candidata e que falharam por INSTRUMENTO.

    ACRESCENTADA EM 09/10/2026, e a causa tem data, nome e custo. A fila da 16.5 abaixo decidia o
    custo da proxima filha por UMA pergunta — "esta candidata tem consulta aberta propria?" — e,
    quando a resposta era nao, imprimia que `medir uma consulta nova para ela e a coisa mais barata
    que existe nesta categoria`. No dia em que essa frase nasceu, a `alicate` tinha CINCO medicoes
    `NAO_MEDIDA` de consulta propria guardadas em `serp-das-filhas.json`, com o motivo escrito em
    cada uma — quatro do `cortador_de_azulejo` (30/09 e 07/10) e uma da pergunta da espessura. A
    fila LIA esse arquivo e nao contava essas cinco: `NAO_MEDIDA` custava zero.

    E o arquivo ja dizia POR QUE elas falham. O `limite_5_consulta_que_pede_a_medida`, escrito em
    07/10, fecha assim: "a consulta-alvo de uma filha NUNCA pede o numero". A pergunta desta
    categoria carrega como ASSUNTO exatamente o numero (`espessura_maxima_de_corte_mm`), e as
    tentativas dela pedem o milimetro na frase. Em 09/10 tres passadas novas desviaram do mesmo
    jeito — a oitava, a nona e a decima desta categoria — e uma delas achou um limite que nao
    existia (`pastilha` + `corte` e o inserto de usinagem, no mesmo idioma).

    E a MESMA familia do defeito de 08/10, uma camada acima: custo infinito escrito em PROSA entra
    numa lista ordenada por custo como se fosse zero. Ali a prosa era a pendencia de canal do
    banco; aqui e o motivo de uma medicao falhada. A diferenca boa e que aqui nao se digita nada:
    a tentativa falhada JA e dado, com data e motivo, no arquivo que esta regua le.
    """
    saida = []
    for m in medicoes_proprias:
        if m["classificacao"] != "NAO_MEDIDA":
            continue
        saida.append({"consulta": m["consulta"],
                      "medida_em": m.get("medida_em", ""),
                      "motivo": (m.get("motivo") or "").strip()})
    return sorted(saida, key=lambda t: (t["medida_em"], t["consulta"]))


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


# ------------------------------------------------ as filhas em forma de PERGUNTA (07/10/2026)
#
# O `filhas-do-guia.py` passou a medir, pela mesma regua, as filhas em forma de PERGUNTA
# declaradas em `dados/perguntas-do-guia.json`. Elas chegam aqui no mesmo arquivo de entrada, na
# chave `perguntas`, e precisam do mesmo cruzamento — com uma diferenca que e a razao desta secao
# existir: a pergunta se liga a SERP pela CONSULTA, nao pelo nome do recorte. Uma consulta medida
# pode estar arquivada sob um recorte de tipo e ser a consulta-alvo de uma pergunta, e foi
# exatamente isso que esta ilha achou em 07/10/2026 — `como cortar pastilha de vidro para mosaico
# qual ferramenta` esta arquivada em `alicate/cortador_de_azulejo` desde 30/09 e e a consulta da
# pergunta da espessura.

def serp_da_pergunta(pergunta, medicoes):
    """A classificacao que vale para uma pergunta: a melhor entre as medicoes DA CONSULTA dela.

    Entram duas coisas: medicao arquivada sob o id da pergunta, e medicao de QUALQUER recorte cuja
    `consulta` seja a consulta-alvo dela. A segunda e a que importa e a que nenhuma versao anterior
    deste arquivo alcancava: consulta e consulta, e onde ela foi arquivada e acidente de quem
    mediu primeiro.
    """
    minhas = [m for m in medicoes
              if m.get("recorte") == pergunta["pergunta"]
              or m.get("consulta") == pergunta["consulta_alvo"]]
    return serp_do_recorte(minhas), minhas


def cruzar_perguntas(perguntas, medicoes):
    linhas = []
    for p in perguntas:
        classe, minhas = serp_da_pergunta(p, medicoes)
        veredito = cruzar(p["veredito"], classe)
        # Onde a consulta-alvo dela foi arquivada. Nao e enfeite: e o que o passo da 16.5 usa para
        # nao contar duas filhas onde existe uma consulta.
        creditada_a = sorted(set(m["recorte"] for m in minhas
                                 if m.get("consulta") == p["consulta_alvo"]
                                 and m.get("recorte") != p["pergunta"]))
        sem_faixa = [m["consulta"] for m in minhas
                     if m["classificacao"] in ("ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP")
                     and not m.get("faixa_de_volume")]
        linhas.append({
            "pergunta": p["pergunta"],
            "categoria": p["categoria"],
            "consulta_alvo": p["consulta_alvo"],
            "veredito_de_dado": p["veredito"],
            "itens_que_declaram_o_numero": p["itens_que_declaram_o_numero"],
            "classe_de_serp": classe,
            "consultas_medidas": len(minhas),
            "consulta_alvo_creditada_a": creditada_a,
            "coincide_com_o_recorte_de_tipo": p["coincide_com_o_recorte_de_tipo"],
            "tentativas_de_consulta_que_falharam": tentativas_que_falharam(
                [m for m in minhas if m.get("recorte") == p["pergunta"]]),
            "veredito": veredito,
            "o_que_falta": o_que_falta_na_pergunta(veredito, p, minhas),
            "consultas_abertas_sem_faixa": sem_faixa,
            "numeros_que_a_serp_nao_publica": [m["numero_que_a_serp_nao_publica"] for m in minhas
                                               if m.get("numero_que_a_serp_nao_publica")],
        })
    return linhas


def o_que_falta_na_pergunta(veredito, p, medicoes):
    """O mesmo texto dos recortes, menos o que nao se aplica: pergunta nao tem `passa_na_contagem
    _sem_lastro`, porque o recorte dela JA e o conjunto dos itens com lastro."""
    if veredito in ("pode_nascer", "pode_nascer_sem_demanda_medida", "espera_autoridade", "nunca"):
        return o_que_falta(veredito, None, medicoes)
    if veredito == "espera_dado":
        return ("%d item(ns) declarando `%s` com fonte que sustente recomendacao primaria"
                % (3 - p["itens_que_declaram_o_numero"], p["propriedade_que_carrega_o_numero"]))
    if veredito == "espera_serp":
        if medicoes:
            return ("uma consulta MEDIDA: as %d tentativas desta pergunta falharam por instrumento,"
                    " nao por concorrente" % len(medicoes))
        return "olhar a SERP da consulta-alvo: o dado passa e ninguem classificou quem ocupa"
    return ("os dois: %d item(ns) declarando `%s`, e %s"
            % (3 - p["itens_que_declaram_o_numero"], p["propriedade_que_carrega_o_numero"],
               ("%d consulta(s) medida(s) e nenhuma aberta" % len(medicoes)) if medicoes
               else "a SERP da consulta-alvo nunca foi olhada"))


def montar(dado, serp):
    por_recorte = {r["recorte"]: r for r in dado["recortes"]}
    perguntas = dado.get("perguntas", [])
    medicoes_por_recorte = {}
    for m in serp["medicoes"]:
        medicoes_por_recorte.setdefault(m["recorte"], []).append(m)

    # Toda medicao de SERP tem de cair num recorte que o portao de dado conhece. Medicao de
    # recorte inexistente e consulta orfa — e orfa passa despercebida justamente no arquivo
    # que decide o que nasce. Desde 07/10/2026 o id de uma PERGUNTA tambem e um lugar valido:
    # sem esta linha, a primeira medicao de consulta de pergunta sairia como orfa.
    conhecidos = set(por_recorte) | set(p["pergunta"] for p in perguntas)
    orfas = sorted(set(medicoes_por_recorte) - conhecidos)

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
            "consulta_que_autoriza": consulta_que_autoriza(medicoes),
            "tentativas_de_consulta_que_falharam": tentativas_que_falharam(medicoes),
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

    linhas_de_pergunta = cruzar_perguntas(perguntas, serp["medicoes"])
    for l in linhas_de_pergunta:
        for c in l["consultas_abertas_sem_faixa"]:
            pedido.append({"consulta": c, "exigida_por": l["pergunta"], "veredito": l["veredito"]})

    contagem = {}
    for l in linhas:
        contagem[l["veredito"]] = contagem.get(l["veredito"], 0) + 1

    return {
        "id": "cruzamento-14-9",
        "ilha": dado["ilha"],
        "gerado_por": "ferramentas/cruzamento-14-9.py",
        "derivado_de": ["dados/filhas-do-guia.json", "dados/serp-das-filhas.json"],
        "recortes": linhas,
        "perguntas": linhas_de_pergunta,
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
            "perguntas_que_podem_nascer": [l["pergunta"] for l in linhas_de_pergunta
                                           if l["veredito"] in VEREDITOS_QUE_AUTORIZAM],
        },
    }


# ------------------------------------------------------------------ a 16.5, que e da mae

def consulta_que_autoriza(medicoes):
    """A consulta ABERTA que faz este recorte poder nascer, entre as medidas nele. '' quando nenhuma.

    A 16.5 pede 3 filhas, e por sete dias esta ilha contou RECORTES. Recorte nao e o que escasseia:
    o que escasseia e a CONSULTA aberta. Duas paginas que miram a mesma consulta nao sao duas
    filhas — sao a mesma pagina duas vezes, disputando a propria consulta.
    """
    abertas = [m for m in medicoes
               if m["classificacao"] in ("ABERTA", "ABERTA_SEM_INTENCAO_NA_SERP")]
    if not abertas:
        return ""
    # A melhor primeiro, pela mesma escada do recorte, e depois em ordem alfabetica para a
    # derivacao nao depender da ordem em que alguem gravou as medicoes.
    abertas.sort(key=lambda m: (ESCADA_DA_SERP.index(m["classificacao"]), m["consulta"]))
    return abertas[0]["consulta"]


def mae_pode_nascer(c, categorias_do_dado):
    """A 16.5 pede 3 filhas de nivel 3 para a mae de nivel 2 nascer. E o cruzamento muda a
    pergunta DUAS vezes.

    A primeira, de 02/10/2026: 3 filhas que PASSAM NO DADO nao sao 3 filhas que podem nascer.

    A segunda, de 07/10/2026, e a que esta versao acrescenta: filha nao se conta por RECORTE, e por
    CONSULTA ABERTA. As filhas em forma de pergunta entram na conta — era isso que faltava, e o
    `filhas-do-guia.py` avisava desde 30/09 que o recorte de tipo e so o piso — e, na mesma conta,
    pergunta e tipo que miram a MESMA consulta valem UMA filha. O caso que forcou isto esta medido
    nesta ilha: `alicate/cortador_de_azulejo` esta em `pode_nascer` e a `pergunta:alicate-espessura-
    de-corte` tambem, e as duas miram `como cortar pastilha de vidro para mosaico qual ferramenta`.
    Contadas por recorte, a `alicate` teria 2 filhas; contadas por consulta, tem 1 — e a fila da
    ilha prometia 3, somando o tipo que a SERP recusa.

    A consulta da MAE nao conta: ela e a pagina de nivel 2, nao filha dela mesma.
    """
    por_recorte = {l["recorte"]: l for l in c["recortes"]}
    perguntas_por_categoria = {}
    for l in c.get("perguntas", []):
        perguntas_por_categoria.setdefault(l["categoria"], []).append(l)

    # Quantas vezes JA se tentou medir uma consulta propria para cada candidata, e falhou por
    # instrumento. E derivado, nao declarado: sai das medicoes `NAO_MEDIDA` do proprio
    # `serp-das-filhas.json`. Ver `tentativas_que_falharam()` para a causa e o custo.
    falhas_por_candidata = {}
    for l in c["recortes"]:
        falhas_por_candidata[l["recorte"]] = l.get("tentativas_de_consulta_que_falharam", [])
    for l in c.get("perguntas", []):
        falhas_por_candidata[l["pergunta"]] = l.get("tentativas_de_consulta_que_falharam", [])

    saida = {}
    for cat, info in sorted(categorias_do_dado.items()):
        filhas_no_dado = info["tipos_que_passam_quais"]
        filhas_no_cruzamento = [f for f in filhas_no_dado
                                if por_recorte.get(f, {}).get("veredito") in VEREDITOS_QUE_AUTORIZAM]
        mae = por_recorte.get(cat, {})
        consulta_da_mae = mae.get("consulta_que_autoriza", "")

        # As candidatas, com a consulta de cada uma: tipos autorizados + perguntas autorizadas.
        candidatas = []
        for f in filhas_no_cruzamento:
            candidatas.append((f, por_recorte[f].get("consulta_que_autoriza", "")))
        perguntas_autorizadas = [l for l in perguntas_por_categoria.get(cat, [])
                                 if l["veredito"] in VEREDITOS_QUE_AUTORIZAM]
        for l in perguntas_autorizadas:
            candidatas.append((l["pergunta"], l["consulta_alvo"]))

        # A conta: consultas DISTINTAS, fora a da mae. Candidata sem consulta aberta nao conta —
        # ela esta autorizada por uma medicao que nao e dela, e isso e o que o `espera_serp` existe
        # para dizer.
        consultas = {}
        for nome, consulta in candidatas:
            if not consulta or consulta == consulta_da_mae:
                continue
            consultas.setdefault(consulta, []).append(nome)

        # QUANTO FALTA, E O QUE A PROXIMA FILHA CUSTA (09/10/2026).
        #
        # Este bloco existe porque a pergunta "qual e o proximo bloco" nao tinha resposta honesta
        # em arquivo nenhum. O `filhas-do-guia.json` respondia por TIPO COM DADO VERDE — e em
        # 08/10/2026 a execucao do dia leu dali que a `alicate` estava a UMA filha com TRES itens
        # a coletar, o menor numero do arquipelago, e escolheu esse bloco. Os dois numeros estavam
        # errados: a filha que faltava era 2, nao 1 (por consulta a `alicate` tem uma, porque o
        # `torques` esta em `espera_autoridade` e a pergunta disputa a consulta do cortador), e os
        # tres itens eram de `alicate/martelinho`, que a propria ilha fechara no dia anterior como
        # nao coletavel neste canal. **A conta da 16.5 mora aqui, entao o custo da proxima filha
        # tem de morar aqui tambem.**
        #
        # E o custo nao e um numero so, de proposito: filha que falta pode custar UMA CONSULTA
        # MEDIDA (quando ja existe candidata com dado verde esperando SERP, ou presa a uma
        # consulta disputada) ou ITEM DE BANCO (quando nao existe candidata nenhuma). As duas sao
        # trabalho de tamanho muito diferente, e chamar as duas de "falta uma filha" foi o que
        # mandou uma execucao coletar o impossivel.
        faltam = max(0, 3 - len(consultas))
        candidatas_sem_consulta_propria = sorted(
            nome for nome, consulta in candidatas
            if not consulta or consulta == consulta_da_mae
            or len(consultas.get(consulta, [])) > 1)
        # E O TERCEIRO ANDAR DESTA CONTA, DE 09/10/2026: "candidata sem consulta propria" NAO e
        # o mesmo que "consulta propria barata de medir". A candidata cuja consulta propria JA foi
        # medida e falhou por instrumento nao e caminho barato — e caminho MEDIDO E FECHADO neste
        # canal, e prometer medi-la de novo e mandar a proxima execucao repetir o que falhou. A
        # divisao abaixo e por isso, e ela e derivada de `tentativas_de_consulta_que_falharam`.
        ja_tentadas = [x for x in candidatas_sem_consulta_propria if falhas_por_candidata.get(x)]
        nunca_tentadas = [x for x in candidatas_sem_consulta_propria
                          if not falhas_por_candidata.get(x)]
        quantas_tentativas = sum(len(falhas_por_candidata.get(x, [])) for x in ja_tentadas)

        if faltam == 0:
            custo = "nada: a 16.5 esta fechada por consulta"
        elif nunca_tentadas:
            custo = ("CONSULTA MEDIDA, nao item de banco: %s ja tem dado verde e nao tem consulta"
                     " aberta propria, e NENHUMA tentativa de consulta propria falhada. Medir uma"
                     " consulta nova para %s e a coisa mais barata que existe nesta categoria."
                     % (", ".join("`%s`" % x for x in nunca_tentadas),
                        "ela" if len(nunca_tentadas) == 1 else "uma delas"))
            if ja_tentadas:
                custo += (" E NAO TENTE %s: a consulta propria dela(s) ja foi medida e falhou por"
                          " instrumento %d vez(es), com o motivo escrito em"
                          " `serp-das-filhas.json`."
                          % (", ".join("`%s`" % x for x in ja_tentadas), quantas_tentativas))
        elif ja_tentadas:
            custo = ("MEDIR SERP NAO E CAMINHO AQUI, e isto e medido e nao suposto: a(s) unica(s)"
                     " candidata(s) com dado verde e sem consulta propria — %s — ja teve(ram) %d"
                     " tentativa(s) de consulta propria medida(s) e falhada(s) por instrumento,"
                     " com o motivo de cada uma em `serp-das-filhas.json`. A %d filha(s) que"
                     " falta(m) custa(m) ITEM DE BANCO ou PERGUNTA NOVA, e antes de escrever"
                     " consulta nova leia `o_canal_e_os_limites_dele` naquele arquivo — a consulta"
                     " de uma filha nunca pede o numero (limite 5)."
                     % (", ".join("`%s`" % x for x in ja_tentadas), quantas_tentativas, faltam))
        else:
            custo = ("ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria"
                     " ja tem consulta aberta propria, entao a %d filha(s) que falta(m) nao sai(em)"
                     " de medir SERP. Qual tipo ainda e coletavel esta em"
                     " `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria —"
                     " tipo fechado por canal NAO e caminho." % faltam)

        saida[cat] = {
            "filhas_que_faltam_por_consulta": faltam,
            "o_que_a_proxima_filha_custa": custo,
            "candidatas_com_dado_verde_e_sem_consulta_propria": candidatas_sem_consulta_propria,
            "candidatas_cuja_consulta_propria_ja_foi_medida_e_falhou": {
                x: falhas_por_candidata.get(x, []) for x in ja_tentadas},
            "tentativas_de_consulta_propria_falhadas_nesta_categoria": quantas_tentativas,
            "filhas_que_o_dado_autoriza": len(filhas_no_dado),
            "filhas_que_o_cruzamento_autoriza": len(filhas_no_cruzamento),
            "quais_o_cruzamento_autoriza": filhas_no_cruzamento,
            "perguntas_que_o_cruzamento_autoriza": [l["pergunta"] for l in perguntas_autorizadas],
            "consultas_abertas_de_filha": sorted(consultas),
            "filhas_contadas_por_consulta": len(consultas),
            "consultas_disputadas_por_mais_de_uma_candidata": {
                k: sorted(v) for k, v in sorted(consultas.items()) if len(v) > 1},
            "consulta_da_mae": consulta_da_mae,
            "veredito_da_mae": mae.get("veredito", "sem_nenhum_dos_dois"),
            "a_mae_pode_nascer": (len(consultas) >= 3
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
    A("## A 16.5 — a mae de nivel 2 so nasce com 3 filhas, e filha se conta por CONSULTA")
    A("")
    A("Duas correcoes de leitura, nesta ordem. **02/10/2026:** 3 filhas que passam no DADO nao sao 3")
    A("filhas que podem nascer — por isso a coluna do cruzamento. **07/10/2026:** filha nao se conta")
    A("por RECORTE, e por **consulta aberta**. As filhas em forma de PERGUNTA entram na conta, e na")
    A("mesma conta pergunta e tipo que miram a MESMA consulta valem **uma** filha: duas paginas na")
    A("mesma consulta nao sao duas filhas, sao a mesma pagina duas vezes. A consulta da mae nao")
    A("conta — ela e a pagina de nivel 2, nao filha de si mesma.")
    A("")
    A("| categoria | filhas no DADO | filhas no CRUZAMENTO (tipos) | perguntas | **filhas por CONSULTA** | veredito da mae | a mae pode nascer |")
    A("|---|---|---|---|---|---|---|")
    for cat, m in maes.items():
        A("| `%s` | %d | %d | %d | **%d** | `%s` | %s |"
          % (cat, m["filhas_que_o_dado_autoriza"], m["filhas_que_o_cruzamento_autoriza"],
             len(m["perguntas_que_o_cruzamento_autoriza"]), m["filhas_contadas_por_consulta"],
             m["veredito_da_mae"], "**SIM**" if m["a_mae_pode_nascer"] else "nao"))
    A("")
    A("### A FILA DAS MAES, ordenada por quanto FALTA e nao por quantos tipos tem dado verde")
    A("")
    A("Esta tabela nasceu em 09/10/2026, e a causa dela tem data e custo. Ate 08/10 a pergunta")
    A("\"qual e o proximo bloco\" era respondida pelo `caminho_mais_barato_para_as_3_filhas` de")
    A("`filhas-do-guia.json`, que conta **tipo com dado verde**. A execucao de 08/10 leu dali que a")
    A("`alicate` estava a UMA filha com TRES itens a coletar e escolheu o bloco por isso. Pela conta")
    A("que decide a 16.5 — a desta pagina — a `alicate` estava a **duas**, e os tres itens eram de um")
    A("tipo que a propria ilha havia fechado no dia anterior como **nao coletavel neste canal**. A")
    A("conta da 16.5 mora aqui; a fila dela passa a morar aqui tambem.")
    A("")
    fila = sorted(maes.items(), key=lambda kv: (kv[1]["filhas_que_faltam_por_consulta"], kv[0]))
    A("| categoria | filhas por CONSULTA | faltam | o que a proxima filha custa |")
    A("|---|---|---|---|")
    for cat, m in fila:
        A("| `%s` | %d | **%d** | %s |"
          % (cat, m["filhas_contadas_por_consulta"], m["filhas_que_faltam_por_consulta"],
             m["o_que_a_proxima_filha_custa"]))
    A("")
    proximas = [(cat, m) for cat, m in fila if m["filhas_que_faltam_por_consulta"] > 0]
    if proximas:
        cat, m = proximas[0]
        A("**A proxima mae do Guia e a `%s`**, a %d filha(s) por consulta. %s"
          % (cat, m["filhas_que_faltam_por_consulta"], m["o_que_a_proxima_filha_custa"]))
    else:
        A("**Toda categoria do Guia fechou as 3 filhas por consulta.**")
    A("")
    # AS TENTATIVAS FALHADAS, NO .md E NAO SO NO JSON (09/10/2026). A licao e a mesma do
    # `o_que_este_caminho_NAO_decide` de ontem: ressalva que mora so no JSON nao viaja com o
    # numero, e quem escolhe bloco le o .md. Aqui vale mais ainda, porque o que estas linhas
    # dizem e justamente "nao tente de novo".
    tentadas = [(cat, m) for cat, m in maes.items()
                if m["candidatas_cuja_consulta_propria_ja_foi_medida_e_falhou"]]
    if tentadas:
        A("### O QUE JA FOI MEDIDO E FALHOU — nao repita a consulta")
        A("")
        A("Tentativa de consulta propria classificada `NAO_MEDIDA` em `serp-das-filhas.json`, por")
        A("candidata. Ate 09/10/2026 a fila acima nao as contava, e por isso prometia `a coisa mais")
        A("barata que existe nesta categoria` para candidata cuja consulta propria ja havia falhado")
        A("cinco vezes. Antes de escrever consulta nova, leia `o_canal_e_os_limites_dele` naquele")
        A("arquivo: a consulta-alvo de uma filha **nunca pede o numero** (limite 5).")
        A("")
        A("| categoria | candidata | tentativas | consultas que falharam |")
        A("|---|---|---|---|")
        for cat, m in tentadas:
            for cand, falhas in sorted(m["candidatas_cuja_consulta_propria_ja_foi_medida_e_falhou"].items()):
                A("| `%s` | `%s` | **%d** | %s |"
                  % (cat, cand, len(falhas),
                     " · ".join("%s (%s)" % (t["consulta"], t["medida_em"] or "sem data")
                                for t in falhas)))
        A("")

    disputa = [(cat, m) for cat, m in maes.items()
               if m["consultas_disputadas_por_mais_de_uma_candidata"]]
    if disputa:
        A("**Consultas disputadas por mais de uma candidata** — cada uma delas vale UMA filha, e e")
        A("aqui que a conta por recorte inflava:")
        A("")
        for cat, m in disputa:
            for consulta, quem in m["consultas_disputadas_por_mais_de_uma_candidata"].items():
                A("- `%s` — *%s* e disputada por %s"
                  % (cat, consulta, ", ".join("`%s`" % q for q in quem)))
        A("")
    A("## As filhas em forma de PERGUNTA, cruzadas")
    A("")
    A("Elas vem medidas no portao de DADO por `filhas-do-guia.py`, pela mesma regua dos recortes de")
    A("tipo, e se ligam a SERP pela **consulta**, nao pelo nome do recorte — consulta e consulta, e")
    A("onde ela foi arquivada e acidente de quem mediu primeiro.")
    A("")
    if not c.get("perguntas"):
        A("Nenhuma pergunta declarada em `dados/perguntas-do-guia.json`.")
    else:
        A("| pergunta | categoria | itens | SERP | veredito | consulta-alvo tambem creditada a | o que falta |")
        A("|---|---|---|---|---|---|---|")
        for l in c["perguntas"]:
            A("| `%s` | `%s` | %d | `%s` | **`%s`** | %s | %s |"
              % (l["pergunta"], l["categoria"], l["itens_que_declaram_o_numero"],
                 l["classe_de_serp"], l["veredito"],
                 ", ".join("`%s`" % x for x in l["consulta_alvo_creditada_a"]) or "—",
                 l["o_que_falta"]))
        A("")
        for l in c["perguntas"]:
            A("- **`%s`** — consulta-alvo: *%s*" % (l["pergunta"], l["consulta_alvo"]))
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
    for l in c.get("perguntas", []):
        for n in l["numeros_que_a_serp_nao_publica"]:
            A("- **`%s`** — %s" % (l["pergunta"], n))
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


def _medicao(recorte, classe, faixa=None, numero=None, consulta="c", motivo=None):
    """O `motivo` entrou em 09/10/2026 junto com a fila que LE tentativa falhada. Fixture sem o
    campo que o real tem foi o defeito que a bancada de ontem achou nos tres .md: mundo fabricado
    tem de ter a mesma FORMA do mundo medido, senao o portao verde nao diz nada sobre o disco."""
    return {"recorte": recorte, "consulta": consulta, "classificacao": classe,
            "faixa_de_volume": faixa, "numero_que_a_serp_nao_publica": numero,
            "medida_em": "2026-01-01",
            "motivo": motivo if motivo is not None
                      else ("desvio de pais medido" if classe == "NAO_MEDIDA" else "")}


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
    # CADA MEDICAO COM A CONSULTA DELA, e isto nao e detalhe de fixture desde 07/10/2026: a 16.5
    # passou a contar CONSULTA DISTINTA, e o fixture antigo deixava as quatro com a consulta "c" do
    # valor padrao do `_medicao`. Com a conta nova ele devolvia zero filha para uma mae que o caso
    # declara publicavel — a regua mordendo o proprio fixture, que e o que se espera dela.
    dado = {"ilha": "x", "recortes": [
        _recorte("acab", "passa"),
        _recorte("acab/a", "passa"), _recorte("acab/b", "passa"), _recorte("acab/c", "passa"),
    ]}
    serp = {"medicoes": [
        _medicao("acab", "ABERTA", consulta="a mae"), _medicao("acab/a", "ABERTA", consulta="ca"),
        _medicao("acab/b", "ABERTA", consulta="cb"), _medicao("acab/c", "TOMADA", consulta="cc"),
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

    serp["medicoes"][3] = _medicao("acab/c", "ABERTA_SEM_INTENCAO_NA_SERP", consulta="cc")
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
    serp["medicoes"][0] = _medicao("acab", "TOMADA", consulta="a mae")
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
    print("")
    print("A FILHA EM FORMA DE PERGUNTA, e a trava que a 16.5 ganhou em 07/10/2026 — ela conta CONSULTA:")

    def _pergunta(id_, categoria, veredito="passa", itens=4, consulta="cp",
                  coincide=None, prop="p"):
        return {"pergunta": id_, "categoria": categoria, "veredito": veredito,
                "itens_que_declaram_o_numero": itens, "consulta_alvo": consulta,
                "propriedade_que_carrega_o_numero": prop,
                "coincide_com_o_recorte_de_tipo": coincide}

    # (1) A PERGUNTA ACRESCENTA FILHA quando a consulta dela e PROPRIA: dois tipos autorizados mais
    # a pergunta, tres consultas distintas, mae nasce. E o caso que a fila da ilha supunha.
    dado3 = {"ilha": "x",
             "recortes": [_recorte("rej", "passa"), _recorte("rej/a", "passa"),
                          _recorte("rej/b", "passa")],
             "perguntas": [_pergunta("pergunta:junta", "rej", consulta="a junta")],
             "resumo": {"por_categoria_do_guia": {}}}
    serp3 = {"medicoes": [
        _medicao("rej", "ABERTA", consulta="a mae"),
        _medicao("rej/a", "ABERTA", consulta="ca"),
        _medicao("rej/b", "ABERTA", consulta="cb"),
        _medicao("pergunta:junta", "ABERTA", consulta="a junta"),
    ]}
    cats3 = {"rej": {"tipos_que_passam_quais": ["rej/a", "rej/b"]}}
    m3 = mae_pode_nascer(montar(dado3, serp3), cats3)["rej"]
    for rotulo, obtido, esperado in (
            ("filhas por RECORTE (tipos so)", m3["filhas_que_o_cruzamento_autoriza"], 2),
            ("filhas por CONSULTA (com a pergunta)", m3["filhas_contadas_por_consulta"], 3),
            ("a mae pode nascer", m3["a_mae_pode_nascer"], True)):
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s %-38s -> %-6s (esperado %s)"
              % ("ok  " if ok else "FALHA", rotulo, obtido, esperado))

    # (2) A TRAVA: a pergunta mira a consulta que JA e creditada a um tipo autorizado. Duas
    # candidatas, UMA consulta, UMA filha. E o caso medido na `alicate` em 07/10/2026, e e ele que
    # desmente a frase da fila que prometia a mae com tres filhas.
    dado4 = {"ilha": "x",
             "recortes": [_recorte("ali", "passa"), _recorte("ali/cortador", "passa")],
             "perguntas": [_pergunta("pergunta:esp", "ali", consulta="como cortar")],
             "resumo": {"por_categoria_do_guia": {}}}
    serp4 = {"medicoes": [
        _medicao("ali", "ABERTA", consulta="a mae"),
        _medicao("ali/cortador", "ABERTA", consulta="como cortar"),
    ]}
    cats4 = {"ali": {"tipos_que_passam_quais": ["ali/cortador"]}}
    c4 = montar(dado4, serp4)
    m4 = mae_pode_nascer(c4, cats4)["ali"]
    for rotulo, obtido, esperado in (
            ("a pergunta herda a SERP da consulta", c4["perguntas"][0]["classe_de_serp"], "ABERTA"),
            ("e ela diz a quem a consulta e creditada",
             c4["perguntas"][0]["consulta_alvo_creditada_a"], ["ali/cortador"]),
            ("candidatas autorizadas", 1 + len(m4["perguntas_que_o_cruzamento_autoriza"]), 2),
            ("filhas por CONSULTA", m4["filhas_contadas_por_consulta"], 1),
            ("a consulta sai marcada como disputada",
             sorted(m4["consultas_disputadas_por_mais_de_uma_candidata"]), ["como cortar"]),
            ("a mae pode nascer", m4["a_mae_pode_nascer"], False)):
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %s %-38s -> %-28s (esperado %s)"
              % ("ok  " if ok else "FALHA", rotulo, obtido, esperado))

    # (3) A CONSULTA DA MAE NAO CONTA COMO FILHA. Sem esta linha, uma categoria com a mae aberta e
    # duas filhas na mesma consulta da mae contaria tres, e a mae nasceria sendo filha de si mesma.
    dado5 = {"ilha": "x",
             "recortes": [_recorte("rej", "passa"), _recorte("rej/a", "passa")],
             "perguntas": [_pergunta("pergunta:x", "rej", consulta="a mae")],
             "resumo": {"por_categoria_do_guia": {}}}
    serp5 = {"medicoes": [
        _medicao("rej", "ABERTA", consulta="a mae"),
        _medicao("rej/a", "ABERTA", consulta="a mae"),
    ]}
    m5 = mae_pode_nascer(montar(dado5, serp5), {"rej": {"tipos_que_passam_quais": ["rej/a"]}})["rej"]
    ok = m5["filhas_contadas_por_consulta"] == 0 and m5["a_mae_pode_nascer"] is False
    falhas += 0 if ok else 1
    print("  %s %-38s -> %-6s (esperado 0)"
          % ("ok  " if ok else "FALHA", "consulta da MAE nao conta como filha",
             m5["filhas_contadas_por_consulta"]))

    # (4) PERGUNTA COM DADO VERMELHO nao vira filha, por aberta que a consulta esteja.
    dado6 = {"ilha": "x", "recortes": [_recorte("rej", "passa")],
             "perguntas": [_pergunta("pergunta:y", "rej", veredito="nao_passa", itens=2,
                                     consulta="minha")],
             "resumo": {"por_categoria_do_guia": {}}}
    serp6 = {"medicoes": [_medicao("rej", "ABERTA", consulta="a mae"),
                          _medicao("pergunta:y", "ABERTA", consulta="minha")]}
    c6 = montar(dado6, serp6)
    m6 = mae_pode_nascer(c6, {"rej": {"tipos_que_passam_quais": []}})["rej"]
    ok = (c6["perguntas"][0]["veredito"] == "espera_dado"
          and "1 item" in c6["perguntas"][0]["o_que_falta"]
          and m6["filhas_contadas_por_consulta"] == 0)
    falhas += 0 if ok else 1
    print("  %s %-38s -> %-28s (esperado espera_dado)"
          % ("ok  " if ok else "FALHA", "pergunta com dado vermelho nao conta",
             c6["perguntas"][0]["veredito"]))

    # (5) PERGUNTA SEM CONSULTA MEDIDA: dado verde e SERP nunca olhada, que e o caso que esta ilha
    # chama de passe livre falso. E a mae nao ganha filha por ela.
    dado7 = {"ilha": "x", "recortes": [_recorte("rej", "passa")],
             "perguntas": [_pergunta("pergunta:z", "rej", consulta="ninguem mediu")],
             "resumo": {"por_categoria_do_guia": {}}}
    serp7 = {"medicoes": [_medicao("rej", "ABERTA", consulta="a mae")]}
    c7 = montar(dado7, serp7)
    m7 = mae_pode_nascer(c7, {"rej": {"tipos_que_passam_quais": []}})["rej"]
    ok = (c7["perguntas"][0]["veredito"] == "espera_serp"
          and m7["filhas_contadas_por_consulta"] == 0
          and not c7["medicoes_de_serp_orfas"])
    falhas += 0 if ok else 1
    print("  %s %-38s -> %-28s (esperado espera_serp)"
          % ("ok  " if ok else "FALHA", "pergunta sem consulta medida",
             c7["perguntas"][0]["veredito"]))

    # (6) MEDICAO ARQUIVADA SOB O ID DA PERGUNTA NAO E ORFA. Sem a linha de `conhecidos` no montar,
    # a primeira medicao de consulta de pergunta sairia como orfa e o --conferir reprovaria o
    # repositorio inteiro.
    ok = not montar(dado7, {"medicoes": [_medicao("pergunta:z", "ABERTA", consulta="x")]})[
        "medicoes_de_serp_orfas"]
    falhas += 0 if ok else 1
    print("  %s %-38s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "medicao sob id de pergunta nao e orfa", ok))

    # (7) ARQUIVO SEM A CHAVE `perguntas` continua funcionando: a ferramenta e de 02/10 e o
    # `filhas-do-guia.json` de ontem nao tem a chave. Entrada velha nao pode explodir a derivacao.
    dado8 = {"ilha": "x", "recortes": [_recorte("rej", "passa")],
             "resumo": {"por_categoria_do_guia": {}}}
    c8 = montar(dado8, {"medicoes": [_medicao("rej", "ABERTA", consulta="a mae")]})
    ok = c8["perguntas"] == [] and not c8["medicoes_de_serp_orfas"]
    falhas += 0 if ok else 1
    print("  %s %-38s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "entrada SEM a chave perguntas nao explode", ok))

    print("")
    print("O CUSTO DA PROXIMA FILHA — a frase que ESCOLHE o bloco, e que nada media ate hoje:")

    # O mundo base das quatro: uma mae com dado verde, UM tipo autorizado e UMA pergunta
    # autorizada, as duas presas a MESMA consulta. E o retrato da `alicate` real: 1 filha por
    # consulta, faltam 2, e as duas candidatas sem consulta propria.
    def _mundo_do_custo(medicoes):
        dado = {"ilha": "x",
                "recortes": [_recorte("ali", "passa"), _recorte("ali/cortador", "passa")],
                "perguntas": [_pergunta("pergunta:espessura", "ali", consulta="como cortar")],
                "resumo": {"por_categoria_do_guia": {}}}
        c = montar(dado, {"medicoes": medicoes})
        return mae_pode_nascer(c, {"ali": {"tipos_que_passam_quais": ["ali/cortador"]}})["ali"]

    compartilhada = [_medicao("ali", "ABERTA", consulta="a mae"),
                     _medicao("ali/cortador", "ABERTA", consulta="como cortar")]

    # (1) O MUNDO SEM TENTATIVA FALHADA — o controle do experimento. Aqui a frase antiga e a
    # CERTA, e se ela desaparecesse o conserto teria virado uma trava sobre tudo.
    m = _mundo_do_custo(compartilhada)
    ok = ("coisa mais barata" in m["o_que_a_proxima_filha_custa"]
          and m["tentativas_de_consulta_propria_falhadas_nesta_categoria"] == 0
          and m["filhas_que_faltam_por_consulta"] == 2)
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "sem tentativa falhada, a promessa barata FICA", ok))

    # (2) UMA DAS DUAS JA FALHOU: a promessa continua, para a OUTRA, e a que falhou sai nomeada
    # com um "nao tente". Meio-mundo e o caso que mais engana, porque a frase antiga estava
    # metade certa.
    m = _mundo_do_custo(compartilhada + [
        _medicao("ali/cortador", "NAO_MEDIDA", consulta="quantos mm o cortador corta")])
    texto = m["o_que_a_proxima_filha_custa"]
    ok = ("coisa mais barata" in texto and "`pergunta:espessura`" in texto
          and "NAO TENTE" in texto and "`ali/cortador`" in texto
          and m["tentativas_de_consulta_propria_falhadas_nesta_categoria"] == 1)
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "uma falhou: promete a outra e nomeia a fechada", ok))

    # (3) AS DUAS JA FALHARAM — e e o retrato da `alicate` de 09/10/2026. A frase NAO pode mais
    # dizer "a coisa mais barata que existe nesta categoria": foi exatamente isso que ela disse
    # com CINCO tentativas falhadas no mesmo arquivo que ela le.
    m = _mundo_do_custo(compartilhada + [
        _medicao("ali/cortador", "NAO_MEDIDA", consulta="quantos mm o cortador corta"),
        _medicao("pergunta:espessura", "NAO_MEDIDA", consulta="espessura em mm do alicate")])
    texto = m["o_que_a_proxima_filha_custa"]
    ok = ("coisa mais barata" not in texto
          and "MEDIR SERP NAO E CAMINHO AQUI" in texto
          and "ITEM DE BANCO ou PERGUNTA NOVA" in texto
          and "limite 5" in texto
          and m["tentativas_de_consulta_propria_falhadas_nesta_categoria"] == 2
          and sorted(m["candidatas_cuja_consulta_propria_ja_foi_medida_e_falhou"])
              == ["ali/cortador", "pergunta:espessura"])
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "as duas falharam: a promessa barata MORRE", ok))

    # (4) E A TENTATIVA DO VIZINHO NAO E TENTATIVA DELA. A pergunta herda a CLASSE da consulta
    # compartilhada, e ela nao pode herdar a FALHA de uma consulta que nao e dela — senao o
    # conserto fecharia caminho por contagio e o erro teria trocado de lado.
    m = _mundo_do_custo(compartilhada + [
        _medicao("ali/cortador", "NAO_MEDIDA", consulta="quantos mm o cortador corta")])
    ok = sorted(m["candidatas_cuja_consulta_propria_ja_foi_medida_e_falhou"]) == ["ali/cortador"]
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "falha do vizinho NAO conta como da pergunta", ok))

    # (5) E A 16.5 FECHADA CONTINUA DIZENDO "nada", com ou sem tentativa falhada no meio: o
    # conserto mexe no CUSTO do que falta, nunca no veredito de quem nao tem o que fazer.
    dado = {"ilha": "x", "recortes": [_recorte("ac", "passa")] +
            [_recorte("ac/%s" % t, "passa") for t in ("a", "b", "c")],
            "perguntas": [], "resumo": {"por_categoria_do_guia": {}}}
    c = montar(dado, {"medicoes": [_medicao("ac", "ABERTA", consulta="mae")] +
                      [_medicao("ac/%s" % t, "ABERTA", consulta=t) for t in ("a", "b", "c")] +
                      [_medicao("ac/a", "NAO_MEDIDA", consulta="uma que falhou")]})
    m = mae_pode_nascer(c, {"ac": {"tipos_que_passam_quais": ["ac/a", "ac/b", "ac/c"]}})["ac"]
    ok = (m["o_que_a_proxima_filha_custa"] == "nada: a 16.5 esta fechada por consulta"
          and m["a_mae_pode_nascer"] is True)
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "16.5 fechada ignora tentativa falhada", ok))

    # (6) A DERIVACAO E ORDENADA E CARREGA O MOTIVO — porque a linha do .md que diz "nao repita"
    # vale pelo motivo, nao pela contagem.
    t = tentativas_que_falharam([
        _medicao("x", "NAO_MEDIDA", consulta="segunda", motivo="limite 5"),
        _medicao("x", "ABERTA", consulta="aberta"),
        _medicao("x", "NAO_MEDIDA", consulta="primeira", motivo="limite 6")])
    ok = ([i["consulta"] for i in t] == ["primeira", "segunda"]
          and [i["motivo"] for i in t] == ["limite 6", "limite 5"])
    falhas += 0 if ok else 1
    print("  %s %-44s -> %-6s (esperado True)"
          % ("ok  " if ok else "FALHA", "so NAO_MEDIDA entra, ordenada, com motivo", ok))

    print("")
    print("A MEDICAO ORFA — consulta num recorte que o portao de dado nao conhece:")
    orfas = montar({"ilha": "x", "recortes": [_recorte("a", "passa")]},
                   {"medicoes": [_medicao("a", "ABERTA"), _medicao("inventado/x", "ABERTA")]})
    obtido = orfas["medicoes_de_serp_orfas"]
    ok = obtido == ["inventado/x"]
    falhas += 0 if ok else 1
    print("  %s orfas -> %s (esperado ['inventado/x'])" % ("ok  " if ok else "FALHA", obtido))

    # A conta e a mao e por isso ela erra calada: a bancada das PERGUNTAS entrou em
    # 07/10/2026 com 14 afirmacoes e o total continuou em 32 na primeira passada, dizendo
    # verde sobre menos do que media. 3+2+1 = a 16.5; 1 = pedido de faixa; 1 = orfa;
    # 3+6+1+1+1+1+1 = as sete pecas da bancada das perguntas, na ordem em que saem.
    # Os SEIS de 09/10/2026 sao os da fila do custo, e a conta continua a mao de proposito.
    total = len(casos) + len(prec) + 3 + 2 + 1 + 1 + 1 + (3 + 6 + 1 + 1 + 1 + 1 + 1) + 6
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
        # FALHA-FECHADA DE 09/10/2026: `NAO_MEDIDA` sem motivo escrito seria tentativa falhada
        # que nao ensina nada — e desde hoje ela e o que FECHA um caminho na fila da 16.5. Fechar
        # caminho sem dizer por que e pior que nao fechar: a execucao seguinte nao tem como saber
        # se a consulta era ruim ou se o canal nao alcanca.
        sem_motivo = sorted("%s / %s" % (m["recorte"], m["consulta"])
                            for m in serp["medicoes"]
                            if m["classificacao"] == "NAO_MEDIDA"
                            and not (m.get("motivo") or "").strip())
        if sem_motivo:
            falhas.append("medicao NAO_MEDIDA sem motivo escrito, e ela fecha caminho na fila "
                          "da 16.5: %s" % ", ".join(sem_motivo))
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
        print("  ok   toda medicao NAO_MEDIDA diz por que falhou (%d medida(s))"
              % sum(1 for m in serp["medicoes"] if m["classificacao"] == "NAO_MEDIDA"))
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
        print("  16.5  %-12s dado %d, cruzamento %d, por consulta %d -> mae %s"
              % (cat, m["filhas_que_o_dado_autoriza"], m["filhas_que_o_cruzamento_autoriza"],
                 m["filhas_contadas_por_consulta"],
                 "PODE NASCER" if m["a_mae_pode_nascer"] else "espera"))
    print("")
    print("Pedido de faixa ao Raphael: %d consulta(s) aberta(s) sem faixa medida"
          % len(c["resumo"]["pedido_de_faixa_ao_raphael"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

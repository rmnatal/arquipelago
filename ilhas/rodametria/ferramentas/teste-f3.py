#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DA F3 — "aguenta o meu peso?". Roda SEM rede.

Ele julga `regras/f3.py`, `dados/f3-respostas.json` e `snippets/rodametria-f3.php`.

O QUE ELE COBRA, e a ordem e da mais forte para a mais barata:

  (A) A ARITMETICA, REESCRITA A MAO EM `Fraction`, varrendo a grade inteira de
      pesos e cargas. Ela nao chama a referencia para saber a resposta: ela a
      calcula por um caminho proprio e exige que os dois cheguem no mesmo
      numero. Duas metades contando a mesma coisa sem nunca se falarem e o
      defeito que a secao 8 mais paga; duas metades que se falam por um numero
      e o que a pega.

  (B) AS FRONTEIRAS, uma afirmacao por fronteira. A 3.2 da especificacao usa
      `>=` na margem e `<=` no teto, e e EXATAMENTE nelas que a mutacao de `<`
      para `<=` muda o veredito. A cicatriz e da F1, de hoje de manha: a grade
      de teste dela usava valores que NENHUM caia num limiar, e a mutacao de
      fronteira passava sem morder. Aqui a grade e DERIVADA dos limiares.

  (C) O ARREDONDAMENTO ANDA PARA O LADO SEGURO, e isso e regra e nao estilo. A
      carga minima arredondada para BAIXO publica um numero MENOR do que a
      margem pede — com 108 kg e 10%, publicaria 118 onde a regra diz 118,8, e
      aprovaria um veiculo de 118 kg que a propria regra recusa. O erro caro
      desta ferramenta e o permissivo (3.3).

  (D) A PRESTACAO DE CONTAS FECHA, e cada registro aparece em EXATAMENTE um
      grupo. A soma e afirmada aqui por fora, alem do `assert` que mora na
      referencia.

  (E) A LISTA VAZIA NOMEIA A CAUSA CERTA, e esta e a afirmacao que nasceu de um
      defeito MEDIDO nesta propria passada. A primeira versao da F3 tinha UM
      molde de lista vazia e ele dizia que "nenhum dos 3 veiculos que declaram
      carga maxima aguenta os seus 108 kg com folga" — e os tres declaram 120
      kg, que cobre com folga os 119 que a regra pede. O eixo que esvaziava a
      vitrine era a falta de OFERTA, nao a carga. A regua agora exige que a
      frase mude com a CAUSA, e fabrica os dois mundos.

  (F) O MUNDO QUE O BANCO NAO TEM. Nenhum registro de hoje declara carga E tem
      oferta aberta, entao a vitrine da F3 nunca foi exercitada por dado real.
      A bateria PRODUZ esse mundo — e sem ele a metade da ferramenta que vende
      iria ao ar sem nunca ter rodado.

  (G) 32.4: nenhuma palavra de bastidor em texto de tela; e todo texto de tela
      acentuado, porque ASCII sem acento na tela e a cicatriz da F2 em 29/10.

  (H) O JS NAO TEM FRASE PROPRIA: todo molde que ele usa existe no arquivo
      publicado, e nao ha prosa literal dentro do `<script>`. Duas metades
      escrevendo a propria frase dizem duas coisas para a mesma entrada.
"""
import json
import os
import re
import sys
import importlib.util
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)

_spec = importlib.util.spec_from_file_location("f3ref", os.path.join(ILHA, "regras", "f3.py"))
f3ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(f3ref)

RESPOSTAS = os.path.join(ILHA, "dados", "f3-respostas.json")
PHP = os.path.join(ILHA, "snippets", "rodametria-f3.php")

falhas = []
notas = []
contador = [0]


def afirma(condicao, mensagem):
    contador[0] += 1
    if not condicao:
        falhas.append(mensagem)


def nota(texto):
    notas.append(texto)


# ---------------------------------------------------------------------------
# (A) A ARITMETICA ESCRITA A MAO, por um caminho que nao e o da referencia.
# ---------------------------------------------------------------------------

def minimo_a_mao(peso, carga, pct):
    """`(peso + carga) * (100 + pct) / 100`, e o arredondamento e para CIMA.

    A referencia faz `total * (1 + pct/100)`. Esta faz a conta com o
    denominador 100 explicito, para as duas poderem DISCORDAR se uma delas
    errar a conversao de por cento — que e exatamente o erro que a F1 cometeu
    hoje de manha nos tres lugares que convertiam milimetro para centimetro.
    """
    total = Fraction(str(peso)) + Fraction(str(carga or 0))
    bruto = total * (100 + Fraction(str(pct))) / 100
    inteiro = int(bruto)
    return total, (inteiro if Fraction(inteiro) == bruto else inteiro + 1)


def grupo_a_mao(carga_max, total, pct):
    """A arvore da 3.2, reescrita. `>=` na margem e `<=` no teto."""
    cm = Fraction(str(carga_max))
    t = Fraction(str(total))
    precisa = t * (100 + Fraction(str(pct))) / 100
    if cm >= precisa:
        return "folga"
    if t <= cm:
        return "no_limite"
    return "nao_aguenta"


def main():
    if not os.path.exists(RESPOSTAS):
        print("REPROVADO — %s nao existe. Rode gerar-f3.py." % RESPOSTAS)
        return 1
    if not os.path.exists(PHP):
        print("REPROVADO — %s nao existe." % PHP)
        return 1

    d = json.loads(open(RESPOSTAS, encoding="utf-8").read())
    php = open(PHP, encoding="utf-8").read()
    constantes = f3ref.carregar_constantes()
    margem_fr, pct = f3ref.margem(constantes)
    veiculos = json.loads(open(os.path.join(ILHA, "dados", "veiculos.json"),
                               encoding="utf-8").read())["registros"]

    afirma(pct is not None,
           "a constante da margem nao esta publicavel: sem ela a F3 nao tem "
           "resposta a dar, e a pagina tem de dizer isso em vez de escolher um numero")
    afirma(d["margem_pct"] == pct,
           "o arquivo publicado diz margem %r e a constante diz %r — fato externo "
           "em dois lugares, e eles divergiram" % (d["margem_pct"], pct))

    # ---- (A) a varredura: 141 pesos x 41 cargas, pelos dois caminhos ----
    divergencias = 0
    varridos = 0
    for peso in range(f3ref.PESO_MINIMO_KG if False else 40, 181):
        for carga in range(0, 41, 4):
            varridos += 1
            total_mao, min_mao = minimo_a_mao(peso, carga, pct)
            r = f3ref.responder(peso, carga, constantes=constantes)
            if r["peso_total"] != total_mao:
                divergencias += 1
                continue
            if r["carga_minima_tela"] != "{:,}".format(min_mao).replace(",", "."):
                divergencias += 1
    afirma(divergencias == 0,
           "a referencia e a aritmetica reescrita a mao divergiram em %d de %d "
           "mundos varridos" % (divergencias, varridos))
    nota("varredura: %d mundos (peso 40 a 180, carga 0 a 40), %d divergencia(s) "
         "entre a referencia e a conta reescrita a mao" % (varridos, divergencias))

    # ---- (B) AS FRONTEIRAS, e a grade e DERIVADA do limiar, nunca redonda ----
    # Para um peso total T, a carga que esta EXATAMENTE na margem e T*(1+pct/100).
    fronteiras = 0
    for total in (100, 108, 109, 110, 120):
        t = Fraction(total)
        exata = t * (100 + Fraction(str(pct))) / 100
        casos = [
            (exata, "folga", "EXATAMENTE na margem entra em folga (o >= da 3.2)"),
            (exata - Fraction(1, 1000), "no_limite",
             "um milesimo ABAIXO da margem sai de folga"),
            (t, "no_limite", "carga EXATAMENTE igual ao peso entra em no_limite (o <= da 3.2)"),
            (t - Fraction(1, 1000), "nao_aguenta",
             "um milesimo abaixo do peso ja e nao_aguenta"),
        ]
        for carga, esperado, porque in casos:
            fronteiras += 1
            visto = f3ref.grupo_do_veiculo(carga, t, margem_fr)
            mao = grupo_a_mao(carga, t, pct)
            afirma(visto == esperado,
                   "fronteira em %s kg: carga %s deu %r e o esperado e %r (%s)"
                   % (total, carga, visto, esperado, porque))
            afirma(visto == mao,
                   "fronteira em %s kg: a referencia disse %r e a arvore reescrita "
                   "a mao disse %r" % (total, visto, mao))
    nota("fronteiras: %d caso(s), todos derivados do limiar e nenhum redondo" % fronteiras)

    # ---- (C) o arredondamento anda para o lado SEGURO ----
    # 108 kg com 10% pede 118,8. Para baixo seria 118, e 118 < 118,8.
    _, m108 = minimo_a_mao(108, 0, pct)
    afirma(m108 == 119,
           "108 kg com %s%% pede 118,8 kg e o publicado tem de ser 119 (para CIMA); "
           "saiu %s" % (pct, m108))
    r108 = f3ref.responder(100, 8, constantes=constantes)
    afirma(r108["carga_minima_tela"] == "119",
           "o caso do VOZ.md (100 + 8) tem de pedir 119 kg; a referencia disse %r"
           % r108["carga_minima_tela"])
    # E O NUMERO PUBLICADO NUNCA APROVA UM VEICULO QUE A REGRA RECUSA: o teto
    # arredondado tem de ser >= a conta exata, sempre, em toda a varredura.
    arredondou_para_baixo = 0
    for peso in range(40, 181, 7):
        total = Fraction(peso)
        exata = total * (100 + Fraction(str(pct))) / 100
        _, publicado = minimo_a_mao(peso, 0, pct)
        if Fraction(publicado) < exata:
            arredondou_para_baixo += 1
    afirma(arredondou_para_baixo == 0,
           "em %d peso(s) o numero publicado ficou ABAIXO da conta exata: o "
           "arredondamento andou para o lado permissivo" % arredondou_para_baixo)

    # ---- (D) a prestacao de contas fecha ----
    c = d["compra"]["contagem"]
    soma = sum(c.values())
    afirma(soma == d["compra"]["total_registros_veiculos"],
           "a prestacao de contas soma %d e o banco tem %d registros"
           % (soma, d["compra"]["total_registros_veiculos"]))
    afirma(soma == len(veiculos),
           "o arquivo publicado diz %d registros e dados/veiculos.json tem %d"
           % (soma, len(veiculos)))
    nota("prestacao de contas: %s, soma %d = %d registros do banco"
         % (c, soma, len(veiculos)))

    # Nenhum registro aparece em DOIS grupos.
    vistos = {}
    for nome_grupo, lista in d["compra"]["grupos"].items():
        for item in lista:
            afirma(item["id"] not in vistos,
                   "o registro %s aparece em %r e tambem em %r"
                   % (item["id"], vistos.get(item["id"]), nome_grupo))
            vistos[item["id"]] = nome_grupo
    afirma(len(vistos) == len(veiculos),
           "os grupos nomeiam %d registros e o banco tem %d" % (len(vistos), len(veiculos)))

    # ---- (E) A LISTA VAZIA NOMEIA A CAUSA CERTA, e os DOIS mundos sao fabricados ----
    # MUNDO 1: declaram carga, aguentariam, e NAO tem oferta. (E o banco de hoje.)
    sem_oferta = [{"id": "fab-1", "marca": "Fabricada", "modelo": "A",
                   "status": "rascunho", "carga_max_kg": {"valor": 150}}]
    r1 = f3ref.responder(100, 8, constantes=constantes, registros=sem_oferta)
    afirma(len(r1["frases_vazio"]) == 1, "o mundo sem oferta tem de dar UMA frase de vazio")
    afirma("aguentariam" in r1["frases_vazio"][0],
           "com carga que SERVE e sem link, a frase tem de dizer que aguentariam; "
           "saiu: %r" % r1["frases_vazio"][0][:120])
    afirma("oferta aberta" in r1["frases_vazio"][0],
           "a frase do mundo sem oferta tem de nomear a falta de oferta")

    # MUNDO 2: declaram carga, NAO aguentam, e nao tem oferta.
    r2 = f3ref.responder(200, 0, constantes=constantes, registros=sem_oferta)
    afirma("aguenta os seus" in r2["frases_vazio"][0],
           "com carga que NAO serve, a frase tem de dizer que nenhum aguenta; "
           "saiu: %r" % r2["frases_vazio"][0][:120])
    afirma(r1["frases_vazio"][0] != r2["frases_vazio"][0],
           "A CAUSA MUDOU E A FRASE NAO: os dois mundos (aguentariam-sem-link e "
           "nao-aguentam) produziram a MESMA frase de lista vazia. Foi exatamente "
           "este defeito que a primeira versao da F3 cometeu, em 06/11/2026.")

    # MUNDO 3: ninguem declara carga.
    r3 = f3ref.responder(100, 8, constantes=constantes,
                         registros=[{"id": "fab-2", "status": "rascunho"}])
    afirma("declara carga m" in r3["frases_vazio"][0],
           "sem nenhuma carga declarada, a frase tem de dizer isso; saiu: %r"
           % r3["frases_vazio"][0][:120])
    afirma(len({r1["frases_vazio"][0], r2["frases_vazio"][0], r3["frases_vazio"][0]}) == 3,
           "as TRES causas de lista vazia tem de produzir TRES frases diferentes")

    # ---- (F) O MUNDO QUE O BANCO NAO TEM: carga declarada E oferta aberta ----
    com_oferta = [
        {"id": "fab-folga", "marca": "Fab", "modelo": "Folga", "status": "publicavel",
         "carga_max_kg": {"valor": 150},
         "afiliado": {"url_busca": "https://exemplo/busca"}},
        {"id": "fab-limite", "marca": "Fab", "modelo": "Limite", "status": "publicavel",
         "carga_max_kg": {"valor": 110},
         "afiliado": {"url_busca": "https://exemplo/busca"}},
        {"id": "fab-nao", "marca": "Fab", "modelo": "Nao", "status": "publicavel",
         "carga_max_kg": {"valor": 90},
         "afiliado": {"url_busca": "https://exemplo/busca"}},
    ]
    r4 = f3ref.responder(100, 8, constantes=constantes, registros=com_oferta)
    afirma([len(r4["linhas"][k]) for k in f3ref.GRUPOS_EM_ORDEM] == [1, 1, 1],
           "o mundo fabricado com um veiculo em cada grupo deu %r"
           % [len(r4["linhas"][k]) for k in f3ref.GRUPOS_EM_ORDEM])
    afirma(not r4["frases_vazio"],
           "com a vitrine cheia nao pode sair frase de lista vazia")
    afirma(bool(r4["frases_ressalva"]),
           "com um veiculo no grupo do meio, a ressalva SOURCED da 3.4 tem de nascer")
    # A ressalva do meio NAO nasce quando o grupo do meio esta vazio.
    so_folga = [com_oferta[0]]
    r5 = f3ref.responder(100, 8, constantes=constantes, registros=so_folga)
    afirma(not r5["frases_ressalva"],
           "sem ninguem no grupo do meio, a ressalva dele nao pode nascer — seria a "
           "pagina avisando sobre um grupo que ela nao mostra")
    # E AS LINHAS DIZEM O NUMERO CERTO: sobra, falta e o total.
    linha_folga = r4["linhas"]["folga"][0]["frase"]
    afirma("31 kg acima" in linha_folga,
           "o veiculo de 150 kg com minimo 119 tem de sobrar 31 kg; saiu: %r" % linha_folga)
    linha_nao = r4["linhas"]["nao_aguenta"][0]["frase"]
    afirma("faltam 18 kg" in linha_nao,
           "o veiculo de 90 kg com peso 108 tem de faltar 18 kg; saiu: %r" % linha_nao)
    nota("mundos fabricados: 5, incluindo o que o banco NAO tem (carga declarada "
         "E oferta aberta, nos tres grupos)")

    # ---- a grade da tabela publicada bate com a referencia, linha por linha ----
    for l in d["tabela"]["linhas"]:
        _, mao = minimo_a_mao(l["peso_total_kg"], 0, pct)
        afirma(l["carga_minima_kg"] == mao,
               "a linha de %s kg publica %s kg e a conta a mao da %s"
               % (l["peso_total_kg"], l["carga_minima_kg"], mao))
        quantos, _ = f3ref.quantos_serviriam_sem_a_oferta(
            veiculos, Fraction(str(l["peso_total_kg"])), margem_fr)
        afirma(l["quantos_do_banco_aguentariam"] == quantos,
               "a linha de %s kg diz que %s aguentariam e a contagem do banco da %s"
               % (l["peso_total_kg"], l["quantos_do_banco_aguentariam"], quantos))
    # A VIRADA DA TABELA E A TESE DA ILHA, e ela tem de estar visivel nela:
    # 109 kg e o ultimo que o teto de 120 acolhe com folga; 110 ja nao.
    por_peso = {l["peso_total_kg"]: l for l in d["tabela"]["linhas"]}
    afirma(109 in por_peso and 110 in por_peso,
           "a tabela tem de trazer 109 e 110 kg: e nesses dois que a virada acontece, "
           "e tabela sem a virada nao mostra a tese desta ferramenta")
    if 109 in por_peso and 110 in por_peso:
        afirma(por_peso[109]["quantos_do_banco_aguentariam"] > 0
               and por_peso[110]["quantos_do_banco_aguentariam"] == 0,
               "a virada da tabela nao esta entre 109 e 110 kg: saiu %s e %s"
               % (por_peso[109]["quantos_do_banco_aguentariam"],
                  por_peso[110]["quantos_do_banco_aguentariam"]))
    nota("tabela: %d linhas conferidas, com a virada entre 109 e 110 kg"
         % len(d["tabela"]["linhas"]))

    # ---- (G) 32.4 e o acento na tela ----
    proibidas = ["egresso", "SERP", "snippet", "wp-sitemap", "manifest",
                 "ARQUIPELAGO", "Sync", "bancada", "dados/", "ferramentas/",
                 "regras/", ".py", ".mjs"]
    textos_de_tela = []
    for k, v in d["frases_molde"].items():
        textos_de_tela.append(("frases_molde/%s" % k, v))
    for k in ("frase_precisa", "frase_margem", "frase_convite_f2"):
        textos_de_tela.append(("resposta_exemplo/%s" % k, d["resposta_exemplo"][k]))
    for grupo in ("frases_vazio", "frases_ressalva", "frases_mercado"):
        for i, v in enumerate(d["resposta_exemplo"][grupo]):
            textos_de_tela.append(("resposta_exemplo/%s[%d]" % (grupo, i), v))
    for l in d["tabela"]["linhas"]:
        textos_de_tela.append(("tabela/%s/por_que" % l["peso_total_kg"], l["por_que"]))
    # A `fonte` DE CADA CONSTANTE ENTRA AQUI, porque a dobra "Como sabemos" a
    # IMPRIME — e foi exatamente por ela que a palavra "egresso" chegou a tela da
    # F2 em 29/10/2026, por DADO e nao por codigo. Esta ferramenta nasceu
    # publicando o `fonte` cru ("Decisao desta ilha. NAO e dado de terceiro..." —
    # ASCII sem acento — e "painel da Shopee do dossie, lido pelo Raphael", que e
    # bastidor da fabrica e o nome do dono na pagina publica). O gerador agora
    # troca pela frase de LEITOR de `FONTE_NA_TELA`, e esta linha e a segunda
    # metade: o gerador decide, o portao confere o que foi publicado.
    for cid, c in d["constantes_usadas"].items():
        textos_de_tela.append(("constantes_usadas/%s/fonte" % cid, c.get("fonte") or ""))

    for onde, texto in textos_de_tela:
        for termo in proibidas:
            afirma(termo not in texto,
                   "32.4: a palavra de bastidor %r aparece em texto de tela (%s): %s"
                   % (termo, onde, texto[:90]))

    # ACENTO — E ESTA REGUA NASCEU ERRADA E FOI TROCADA NA MESMA PASSADA.
    #
    # A cicatriz e da F2 em 29/10/2026: texto ASCII SEM ACENTO chegou a tela, no
    # mesmo campo que servia a pagina. A primeira versao desta regua media isso
    # por AUSENCIA DE ACENTO em texto com mais de 40 caracteres — e reprovou
    # frase CERTA: "peso igual ao teto declarado que mais se repete no varejo
    # brasileiro" nao tem um acento e esta perfeita. Portao que reprova o texto
    # certo e o caminho mais curto para alguem passar a ignora-lo (20.5), e
    # contorcer a copia para agradar a regua e pior: e a regua passar a decidir
    # o que a pagina diz.
    #
    # A REGUA CERTA PROCURA A PALAVRA ESCRITA SEM O ACENTO QUE ELA EXIGE, que e
    # o defeito de verdade. A lista e das palavras que esta fabrica escreve sem
    # acento nos arquivos de registro — e e de onde o vazamento vem, porque o
    # texto de tela e montado perto delas. Lista curta e explicita: palavra nova
    # entra quando alguem a vazar, e lista que tenta cobrir o portugues inteiro
    # produz falso positivo, que e o defeito que esta troca existe para desfazer.
    SEM_O_ACENTO = (
        "maxima", "minima", "media", "nao", "voce", "ultimo", "ultima", "proprio",
        "propria", "pagina", "numero", "criterio", "potencia", "medicao", "tambem",
        "porem", "apos", "ja ", "so ", "veiculo", "ficha tecnica", "autonomia maxima",
        "porcentagem", "tres", "varios", "voces",
        "decisao", "razao", "condicao", "varredura", "ja", "so",
    )
    # A BUSCA E POR PALAVRA INTEIRA, e isto nao e detalhe: a primeira versao
    # procurava a substring e `'so '` casou dentro de "nosso" e de "isso",
    # reprovando CINCO frases certas. Regua que casa pedaco de palavra reprova a
    # pagina certa, e foi o segundo falso positivo desta mesma regua em dois
    # minutos — o primeiro foi medir por ausencia de acento.
    vazou = []
    for onde, texto in textos_de_tela:
        baixo = texto.lower()
        for palavra in SEM_O_ACENTO:
            if re.search(r"(?<![0-9A-Za-z\u00c0-\u00ff])%s(?![0-9A-Za-z\u00c0-\u00ff])"
                         % re.escape(palavra), baixo):
                vazou.append("%s: %r" % (onde, palavra))
    afirma(not vazou,
           "palavra escrita SEM o acento que ela exige, em texto de tela: %s. E a "
           "cicatriz da F2 em 29/10/2026 — texto ASCII de arquivo de registro "
           "chegando a tela." % "; ".join(vazou[:5]))

    # E A TRAVA DESTA REGUA, porque regua de lista fica verde medindo nada: ela
    # tem de MORDER num texto fabricado com o defeito.
    # A TRAVA, e ela e por mundo FABRICADO e nao por `in`: o mundo tem o defeito
    # e a regua tem de morder nele; e o mundo CERTO tem de passar, senao a regua
    # volta a ser a que reprovava "nosso" por conter "so".
    def _vazou_em(txt):
        baixo = txt.lower()
        return [p for p in SEM_O_ACENTO
                if re.search(r"(?<![0-9A-Za-z\u00c0-\u00ff])%s(?![0-9A-Za-z\u00c0-\u00ff])"
                             % re.escape(p), baixo)]

    afirma(_vazou_em("a carga maxima da ficha nao declara") == ["maxima", "nao"]
           or set(_vazou_em("a carga maxima da ficha nao declara")) >= {"maxima", "nao"},
           "a regua de acento nao morde no mundo fabricado com o defeito: ela ficou inerte")
    afirma(not _vazou_em("isso e nosso, e o osso da questao j\u00e1 foi s\u00f3 um"),
           "a regua de acento voltou a casar PEDACO de palavra: 'isso', 'nosso' e "
           "'osso' contem 'so', e 'loja' contem 'ja'")
    afirma(not _vazou_em("a carga m\u00e1xima da ficha n\u00e3o declara"),
           "a regua de acento reprovou o texto CERTO, com os acentos no lugar")
    # E a pagina, no conjunto, TEM acento: se nenhum dos 32 textos tiver, ou a
    # pagina virou telegrama ou o arquivo perdeu a codificacao.
    com_acento = sum(1 for _, t in textos_de_tela
                     if re.search(r"[à-ÿÀ-Ý]", t))
    afirma(com_acento >= len(textos_de_tela) // 2,
           "so %d de %d textos de tela tem acento: ou a pagina virou telegrama, ou "
           "o arquivo perdeu a codificacao" % (com_acento, len(textos_de_tela)))
    nota("32.4 e acento: %d texto(s) de tela conferidos, 0 palavra de bastidor, "
         "0 palavra sem o acento que exige, %d com acento" % (len(textos_de_tela), com_acento))

    # A `fonte` das constantes vai para a dobra "Como sabemos" — e foi por um
    # campo `fonte` que a palavra "egresso" chegou a tela da F2 em 29/10.
    for cid, c in d["constantes_usadas"].items():
        for termo in proibidas:
            afirma(termo not in (c.get("fonte") or ""),
                   "32.4: a palavra %r esta na `fonte` da constante %s, e a dobra "
                   "'Como sabemos' a imprime" % (termo, cid))

    # ---- (H) o JS nao tem frase propria ----
    bloco = php.split('<script id="rodametria-f3-js">')
    afirma(len(bloco) == 2, "nao achei o bloco <script> da F3 no snippet")
    if len(bloco) == 2:
        js = bloco[1].split("</script>")[0]
        js = re.sub(r"<\?php.*?\?>", "", js, flags=re.S)
        usados = set(re.findall(r"moldes\.([a-z_0-9]+)", js))
        for m in sorted(usados):
            afirma(m in d["frases_molde"],
                   "o JS usa o molde %r e ele nao existe no arquivo publicado" % m)
        prosa = []
        for lit in re.findall(r"'([^'\n]{4,})'", js) + re.findall(r'"([^"\n]{4,})"', js):
            if "<" in lit or ">" in lit:
                continue
            acentuado = bool(re.search(r"[à-ÿÀ-Ý]", lit))
            palavras = [w for w in re.split(r"\s+", lit) if re.match(r"^[A-Za-z]{2,}$", w)]
            if acentuado or len(palavras) >= 3:
                prosa.append(lit)
        afirma(not prosa,
               "o JS da F3 tem prosa literal dentro dele, e por isso a pagina pode "
               "dizer duas coisas para a mesma entrada: %s" % prosa[:3])
        afirma(len(usados) >= 4,
               "o JS cita so %d molde(s): ou ele parou de usar o arquivo publicado, "
               "ou esta regua deixou de alcancar o bloco" % len(usados))

        # O JS LE AS DUAS LISTAS, E ESTA AFIRMACAO FECHA UMA 32.5-d ANTES DE ELA
        # ACONTECER. A primeira versao do JS reclassificava so
        # `serviriam_sem_oferta` — os que aguentam e NAO tem link. No banco de
        # hoje isso nao mente, porque a vitrine e vazia e as duas listas nao se
        # cruzam. **O dia em que um registro ganhasse link seria o dia em que a
        # recomputacao o deixaria CAIR DA TELA**, servindo MENOS do que o
        # servidor acabou de servir — e sem nenhum portao vermelho, porque o
        # HTML pre-renderizado continuaria certo. E a 32.5-d da F1,
        # pre-registrada hoje de manha, e aqui ela esta FECHADA.
        afirma("D.vitrine" in js and "D.servem" in js,
               "o JS da F3 tem de reclassificar as DUAS listas — `vitrine` (carga "
               "declarada E oferta aberta) e `servem` (aguenta e nao tem link). Lendo "
               "so uma, a recomputacao no navegador serve MENOS do que o servidor "
               "serviu, e nenhum portao fica vermelho porque o HTML pre-renderizado "
               "continua certo (32.5-d)")
        afirma("com_oferta" in json.dumps(d["compra"]),
               "o arquivo publicado tem de carregar `com_oferta`, senao o JS nao tem "
               "a vitrine de verdade para reclassificar")

        # E O MUNDO EM QUE AS DUAS LISTAS SE CRUZAM E FABRICADO AQUI, porque o
        # banco de hoje nao o tem: com um registro em cada lista, a frase de
        # vazio NAO pode nascer (a vitrine tem item) e o nome do sem-link tem de
        # continuar aparecendo.
        misto = [
            {"id": "fab-com", "marca": "Fab", "modelo": "Com", "status": "publicavel",
             "carga_max_kg": {"valor": 150},
             "afiliado": {"url_busca": "https://exemplo/busca"}},
            {"id": "fab-sem", "marca": "Fab", "modelo": "Sem", "status": "rascunho",
             "carga_max_kg": {"valor": 160}},
        ]
        r6 = f3ref.responder(100, 8, constantes=constantes, registros=misto)
        afirma(not r6["frases_vazio"],
               "com a vitrine cheia e um sem-link ao lado, nao pode sair frase de vazio")
        afirma(r6["quantos_serviriam_sem_oferta"] == 2,
               "a contagem de quem serviria conta os DOIS (o com link e o sem), porque "
               "ela e sobre CARGA e nao sobre link; saiu %d"
               % r6["quantos_serviriam_sem_oferta"])
        afirma(len(r6["linhas"]["folga"]) == 1,
               "a vitrine tem de ter exatamente o registro COM link; saiu %d"
               % len(r6["linhas"]["folga"]))
        nota("o JS pede %d molde(s) e todos existem no arquivo publicado; 0 prosa literal"
             % len(usados))

    # ---- o PHP nao digita numero de tela, e a ordem da 32.1 e respeitada ----
    afirma('name="rdm_peso"' in php and 'name="rdm_carga"' in php,
           "32.1-b: os campos da F3 tem de levar o prefixo da ilha (`rdm_peso`, `rdm_carga`)")
    afirma("rodametria_casca_noscript(" in php,
           "32.1-b: a F3 tem de servir o aviso de JavaScript desligado, pelo componente "
           "da casca")
    ordem = []
    for marca, rotulo in (("rodametria_f3_formulario_html", "formulario"),
                          ("rodametria_f3_noscript_html", "noscript"),
                          ("rodametria_f3_resultado_html", "resultado"),
                          ("rodametria_casca_bloco_de_compra", "compra"),
                          ("rodametria_f3_tabela_html", "tabela")):
        corpo = php.split("function rodametria_f3_pagina_html")[-1]
        pos = corpo.find(marca + "(")
        afirma(pos > 0, "a pagina da F3 nao chama %s()" % marca)
        ordem.append((pos, rotulo))
    afirma(ordem == sorted(ordem),
           "32.1: a ordem da pagina da F3 saiu %s e tem de ser formulario, noscript, "
           "resultado, compra, tabela" % [r for _, r in ordem])

    # -----------------------------------------------------------------------
    # A PRESTACAO DE CONTAS TEM DE FECHAR NA TELA, E NAO SO NO DADO — medido no
    # ar em 09/11/2026 em /peso-maximo-patinete-eletrico/.
    #
    # O paragrafo de abertura daquele bloco anuncia *"Dos 17 veiculos que o
    # nosso banco tem, 3 declaram a carga maxima na ficha. OS OUTROS nao entram
    # nesta conta, e A RAZAO ESTA DITA ABAIXO"* — e a razao estava dita para 11
    # dos 14 outros. Os tres `excluido_do_banco` nao apareciam em grupo nenhum.
    #
    # O DADO ESTAVA CERTO E COMPLETO: `contagem` e `grupos` do JSON servido
    # trazem `fora_do_banco: 3` desde o primeiro dia. O que faltava era UMA
    # CHAVE no `$rotulos` do snippet, e grupo sem rotulo nao e renderizado — o
    # dado ia ao ar invisivel. Por isso este portao le o PHP e nao o JSON: um
    # portao sobre o dado teria ficado VERDE sobre este defeito, que e
    # exatamente o que aconteceu durante tres dias.
    php_rot = php.split("$rotulos = array(")
    afirma(len(php_rot) == 2,
           "nao achei o `$rotulos = array(` da prestacao de contas no snippet da F3")
    if len(php_rot) == 2:
        bloco = php_rot[1].split(");")[0]
        chaves_php = set(re.findall(r"'([a-z_]+)'\s*=>", bloco))
        moldes_php = set(re.findall(r"\$m\['([a-z_]+)'\]", bloco))

        contagem = d["compra"]["contagem"]
        # Os grupos da RESPOSTA saem no outro bloco (GRUPOS_EM_ORDEM); todo o
        # resto e da prestacao de contas e precisa de rotulo.
        de_contas = [k for k in contagem if k not in f3ref.GRUPOS_EM_ORDEM]
        for k in de_contas:
            afirma(k in chaves_php,
                   "o grupo %r da prestacao de contas (%d registro(s) no dado) NAO tem "
                   "rotulo no `$rotulos` do snippet, e grupo sem rotulo nao e "
                   "renderizado: o dado vai ao ar INVISIVEL e a conta nao fecha"
                   % (k, contagem[k]))

        for m in moldes_php:
            afirma(m in f3ref.MOLDES,
                   "o `$rotulos` do snippet pede o molde %r e ele nao existe em "
                   "regras/f3.py — a pagina serviria rotulo vazio" % m)

        # E A CONTA FECHA: a soma de TODOS os grupos e o total anunciado no
        # paragrafo. Se um dia ela nao fechar, o texto esta prometendo uma conta
        # que os grupos nao entregam, com ou sem rotulo.
        soma = sum(contagem.values())
        total = d["compra"]["total_registros_veiculos"]
        afirma(soma == total,
               "a prestacao de contas da F3 anuncia %d registro(s) e os grupos somam "
               "%d: %r" % (total, soma, contagem))
        nota("prestacao de contas da F3: %d grupo(s) de contas, todos com rotulo no "
             "snippet, e a soma fecha os %d registros" % (len(de_contas), total))

    for n in notas:
        print("  . %s" % n)
    print("")
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("teste-f3: %d afirmacoes, %d falha(s)." % (contador[0], len(falhas)))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

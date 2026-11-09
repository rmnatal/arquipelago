#!/usr/bin/env python3
"""
GERADOR DA F3 — escreve dados/f3-respostas.json, que e o que o site le.

Por que existe um arquivo entre a referencia e o snippet: pela secao 8 do
ARQUIPELAGO.md, "para cada campo publicado, aponte quem e a fonte e faca a
bancada ler DELA". Quem publica a tabela pre-renderizada e o texto da resposta
e o snippet PHP, e o snippet le a option que o Sync grava de
dados/f3-respostas.json. Entao e ESTE arquivo a fonte de todo numero e de toda
frase que a F3 serve — a referencia em Python o escreve, a bancada o confere
contra a referencia, e o PHP nunca digita numero nenhum.

A TABELA PRE-RENDERIZADA DESTA FERRAMENTA E DIFERENTE DAS DUAS IRMAS, e a
diferenca vale ser dita: na F2 as linhas sao COMBINACOES DE BATERIA e saem do
banco; na F1 elas sao as CATEGORIAS da resolucao. Aqui a linha e UM PESO — e
peso nao vem de banco nenhum, vem da pessoa. Entao a grade e declarada aqui,
com o motivo de cada faixa, e NAO e contada do banco: contar do banco seria
publicar uma tabela de pesos derivada de fichas de patinete, que nao e sobre
pessoas. O que CONTINUA saindo do banco e a coluna do que o banco oferece
naquele peso, e ela e contada registro a registro.

    python3 ferramentas/gerar-f3.py            # escreve
    python3 ferramentas/gerar-f3.py --conferir # nao escreve; falha se divergir
"""

import importlib.util
import json
import os
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)

# A regra mora em regras/, fora de ferramentas/, porque a bancada desta ilha
# denuncia arquivo em ferramentas/ que nao e portao — ver regras/LEIA.md.
import importlib.util
_spec = importlib.util.spec_from_file_location("f3ref", os.path.join(ILHA, "regras", "f3.py"))
f3ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(f3ref)

SAIDA = os.path.join(ILHA, "dados", "f3-respostas.json")


def _irma():
    """A maquinaria de TEXTO DE TELA vem da irma, NAO e reescrita aqui.

    `gerar-f2.py` guarda tres coisas que valem para as tres ferramentas: a lista
    de PALAVRAS_DE_BASTIDOR da 32.4, a regua de ACENTO NA TELA (a cicatriz de
    29/10/2026, quando a palavra "egresso" chegou a tela POR DADO, de dentro do
    campo `fonte` de uma constante) e o dicionario FONTE_NA_TELA, que da a frase
    de LEITOR de cada constante cujo texto interno e de registro.

    `gerar-f1.py` ja importava as duas primeiras assim, em 06/11/2026 pela
    manha. ESTE GERADOR NASCEU SEM NENHUMA DAS TRES e publicou o `fonte` cru na
    dobra "Como sabemos": "Decisao desta ilha. NAO e dado de terceiro, e a
    pagina nunca a atribui a ninguem" — ASCII sem acento —, e, pior, "painel da
    Shopee do DOSSIE, lido pelo RAPHAEL em 27/10/2026", que e bastidor da
    fabrica e nome do dono na pagina publica. A 32.5-c outra vez, e a quinta
    desta passada.

    E A IRMA JA TINHA A FRASE DE DUAS DAS TRES CONSTANTES DESTA FERRAMENTA
    (`teto-de-carga-do-mercado-brasileiro` e `margem-de-carga-f3`), escritas em
    28/10 antecipando a F3. Faltava a da ressalva da 3.4, e ela foi escrita LA,
    onde as outras moram, e nao aqui.
    """
    caminho = os.path.join(AQUI, "gerar-f2.py")
    spec = importlib.util.spec_from_file_location("gerar_f2", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


IRMA = _irma()
conferir_acento_na_tela = IRMA.conferir_acento_na_tela
PALAVRAS_DE_BASTIDOR = IRMA.PALAVRAS_DE_BASTIDOR
FONTE_NA_TELA = IRMA.FONTE_NA_TELA


def fonte_na_tela(cid, registro):
    """O que a tela diz sobre a procedencia desta regua — e nada mais."""
    texto = FONTE_NA_TELA.get(cid) or (registro.get("fonte") or "")
    for palavra in PALAVRAS_DE_BASTIDOR:
        assert palavra.lower() not in texto.lower(), (
            "32.4: a frase de procedencia de %r carrega a palavra de bastidor %r e ela "
            "iria para a tela: %r. Declare a frase de leitor em FONTE_NA_TELA, dentro "
            "de gerar-f2.py, onde as outras moram." % (cid, palavra, texto[:120]))
    # O NOME DO DONO NAO VAI PARA A PAGINA PUBLICA. Nao esta na lista da 32.4
    # porque a 32.4 fala de vocabulario de fabrica, e este e um caso proprio:
    # "painel da Shopee do dossie, lido pelo Raphael" era o `fonte` cru de uma
    # das tres constantes desta ferramenta.
    for proibido in ("Raphael", "dossie", "dossiê"):
        assert proibido.lower() not in texto.lower(), (
            "32.4: a frase de procedencia de %r carrega %r, que e bastidor da fabrica "
            "na pagina publica: %r" % (cid, proibido, texto[:120]))

    return texto

# O CASO DE EXEMPLO. A 32.1 manda vir JA PREENCHIDO no formulario e JA
# PRE-RENDERIZADO na caixa, e a 3.1 da especificacao diz qual e: a pessoa do
# `VOZ.md` desta ilha — "O patinete aguenta 100 kg. Voce e a mochila dao 108."
# A especificacao e explicita sobre por que ele e esse e nao um folgado: "o caso
# de exemplo da casca e um caso QUE DA 'no limite', nao um que passa folgado —
# e a 32.1 item 4 servindo a pergunta real da ilha".
EXEMPLO = {"peso_piloto_kg": 100, "carga_kg": 8}

# A GRADE DO FORMULARIO. Faixa de gente, nao de produto.
# O piso de 40 kg e o teto de 180 kg existem para o campo recusar numero que nao
# e peso de pessoa adulta; eles NAO sao afirmacao sobre quem anda de patinete.
PESO_MINIMO_KG = 40
PESO_MAXIMO_KG = 180
CARGA_MAXIMA_KG = 40

# AS LINHAS DA TABELA PRE-RENDERIZADA. Cada uma com o motivo de estar ali, em
# vez de uma grade redonda escolhida por estetica. A 32.1 item 6 manda a tabela
# ser VISIVEL e nunca recolhida: e o que as IAs citam.
GRADE_DE_PESOS = [
    {"peso_total_kg": 70,
     "por_que": "faixa em que praticamente toda ficha brasileira já serve"},
    {"peso_total_kg": 80,
     "por_que": "faixa em que praticamente toda ficha brasileira já serve"},
    {"peso_total_kg": 90,
     "por_que": "último peso que ainda cabe com folga nos 100 kg declarados"},
    {"peso_total_kg": 100,
     "por_que": "o valor que mais aparece como carga máxima nas fichas de entrada"},
    {"peso_total_kg": 108,
     "por_que": "a pessoa da nossa página: 100 kg de gente mais 8 kg de mochila"},
    {"peso_total_kg": 109,
     "por_que": "o ÚLTIMO peso que os 120 kg do teto de varejo acolhem com a "
                "nossa folga — um quilo acima, já não acolhem"},
    {"peso_total_kg": 110,
     "por_que": "um quilo acima da linha anterior, para a tabela mostrar a virada"},
    {"peso_total_kg": 120,
     "por_que": "peso igual ao teto declarado que mais se repete no varejo brasileiro"},
    {"peso_total_kg": 130,
     "por_que": "faixa que só o modelo de 140 kg do painel da loja acolheria"},
]


def montar(constantes, veiculos):
    registros = veiculos["registros"]

    # A RESPOSTA DO EXEMPLO, pela referencia. Nenhuma frase e escrita aqui.
    r = f3ref.responder(EXEMPLO["peso_piloto_kg"], EXEMPLO["carga_kg"],
                        constantes=constantes, registros=registros)

    margem_fr, margem_pct = f3ref.margem(constantes)

    # A TABELA. Cada linha e recomputada pela referencia, com o banco na mao,
    # para a coluna "o que o nosso banco tem" ser CONTADA e nunca digitada.
    linhas = []
    for base in GRADE_DE_PESOS:
        total = Fraction(str(base["peso_total_kg"]))
        resposta = f3ref.responder(total, 0, constantes=constantes, registros=registros)
        quantos_serviriam, _ = f3ref.quantos_serviriam_sem_a_oferta(
            registros, total, margem_fr)
        linhas.append({
            "peso_total_kg": base["peso_total_kg"],
            "por_que": base["por_que"],
            "carga_minima_kg": int(resposta["carga_minima_tela"].replace(".", "")),
            "carga_minima_tela": resposta["carga_minima_tela"],
            # DUAS CONTAGENS, E ELAS SAO FATOS DIFERENTES: quantos do banco
            # aguentariam este peso com folga, e quantos deles poderiam ser
            # oferecidos. Hoje a segunda e ZERO em toda linha, e a tabela diz
            # isso em vez de omitir a coluna.
            "quantos_do_banco_aguentariam": quantos_serviriam,
            "quantos_com_oferta_aberta": len(resposta["linhas"].get("folga", [])),
        })

    constantes_usadas = {}
    for cid in (f3ref.CONSTANTE_DA_MARGEM, f3ref.CONSTANTE_DA_RESSALVA,
                f3ref.CONSTANTE_DO_TETO_DE_MERCADO):
        c = constantes[cid]
        constantes_usadas[cid] = {
            "valor": c.get("valor"),
            "unidade": c.get("unidade"),
            "tipo": c.get("tipo"),
            "status": c.get("status"),
            # A 32.4 PROIBE TEXTO DE BASTIDOR NA TELA, e a `fonte` destas
            # constantes vai para a dobra "Como sabemos". A da margem diz
            # "Decisao desta ilha" e a da ressalva nomeia os tres publicadores
            # — as duas servem. A cicatriz da F2 em 29/10 foi a palavra
            # "egresso" chegar a tela POR DADO e nao por codigo, de dentro do
            # campo `fonte` de uma constante; por isso o portao desta
            # ferramenta varre estes textos tambem.
            # A FRASE DE LEITOR, nunca o `fonte` cru: ver `fonte_na_tela` acima.
            "fonte": fonte_na_tela(cid, c),
            "verificado_em": c.get("verificado_em"),
        }

    # A REGUA DE ACENTO DA IRMA, sobre TODO texto que esta pagina serve.
    conferir_acento_na_tela(
        [("constantes_usadas/%s/fonte" % k, v["fonte"])
         for k, v in constantes_usadas.items()]
        + [("frases_molde/%s" % k, v) for k, v in f3ref.MOLDES.items()]
        + [("tabela/%s/por_que" % b["peso_total_kg"], b["por_que"])
           for b in GRADE_DE_PESOS])

    teto_banco, quantos_declaram = f3ref.maior_teto_do_banco(registros)
    quantos_serviriam, serviriam = f3ref.quantos_serviriam_sem_a_oferta(
        registros, r["peso_total"], margem_fr)

    contagem = dict(r["contagem"])

    return {
        "id": "f3-respostas",
        "ilha": "rodametria",
        "ferramenta": "F3",
        "bloco": "4c",
        "gerado_em": __import__("datetime").date.today().isoformat(),
        "gerado_por": "ferramentas/gerar-f3.py",
        "referencia": "regras/f3.py",
        "especificacao": "dados/especificacao-calculadoras.md (secao 3)",
        "publicar": True,
        "nota": (
            "A RESPOSTA PRINCIPAL DESTA FERRAMENTA NAO DEPENDE DO BANCO: dado o peso de "
            "quem pilota e o que ele carrega, a carga maxima a procurar sai de "
            "`total x (1 + margem)`, e a margem e uma constante desta ilha. E por isso "
            "que a F3 pode ir ao ar com a vitrine vazia sem deixar de responder. A "
            "camada do banco e a segunda, e hoje ela esta vazia por um motivo que a "
            "pagina NOMEIA: os tres registros que declaram carga maxima (120 kg, os "
            "tres, lidos em ficha de varejo grande) nao tem oferta aberta, e pela 25.2 "
            "item sem piso de compra nao entra em vitrine."
        ),
        "campos": {
            "peso_minimo_kg": PESO_MINIMO_KG,
            "peso_maximo_kg": PESO_MAXIMO_KG,
            "carga_maxima_kg": CARGA_MAXIMA_KG,
            "exemplo": EXEMPLO,
        },
        "constantes_usadas": constantes_usadas,
        "frases_molde": dict(f3ref.MOLDES),
        "margem_pct": margem_pct,
        "grupos_em_ordem": list(f3ref.GRUPOS_EM_ORDEM),
        "resposta_exemplo": {
            "entrada": r["entrada"],
            "peso_total_tela": r["peso_total_tela"],
            "carga_minima_tela": r["carga_minima_tela"],
            "frase_precisa": r["frase_precisa"],
            "frase_margem": r["frase_margem"],
            "frase_convite_f2": r["frase_convite_f2"],
            "frases_vazio": r["frases_vazio"],
            # A MESMA CAUSA, PARA A CAMADA QUE NAO TEM VIZINHO (09/11/2026).
            # Item por item igual a lista de cima, com a remissao locativa
            # ("os nomes estao logo abaixo") trocada pelos NOMES. Quem serve
            # JSON-LD le esta; o defeito que isto conserta foi medido no ar em
            # `/peso-maximo-patinete-eletrico/` as 13h4xZ de 09/11/2026.
            "frases_vazio_autocontidas": r["frases_vazio_autocontidas"],
            "frases_ressalva": r["frases_ressalva"],
            "frases_mercado": r["frases_mercado"],
            "linhas": {k: v for k, v in r["linhas"].items()},
        },
        "tabela": {
            "linhas": linhas,
            "total_de_linhas": len(linhas),
        },
        "compra": {
            # A VITRINE E O QUE TEM PISO DE COMPRA, e hoje ela e vazia. A frase
            # que a pagina serve no lugar sai da referencia (`frases_vazio`), que
            # distingue as DUAS causas — "ninguem aguenta" e "aguentam e nao tem
            # link" — porque os consertos sao diferentes e porque um molde unico
            # MENTIU na primeira versao desta ferramenta.
            "vitrine": [],
            "grupos": {k: [{"id": x.get("id"), "nome": f3ref.nome_do_registro(x)}
                           for x in (r["grupos"] or {}).get(k, [])]
                       for k in ("folga", "no_limite", "nao_aguenta",
                                 "nao_declaram_carga", "sem_saida_de_compra",
                                 "fora_do_banco")},
            "contagem": contagem,
            "total_registros_veiculos": len(registros),
            "teto_do_banco_kg": (None if teto_banco is None else float(teto_banco)),
            "quantos_declaram_carga": quantos_declaram,
            "quantos_serviriam_sem_oferta": quantos_serviriam,
            "serviriam_sem_oferta": serviriam,
            # OS REGISTROS COM CARGA DECLARADA **E** OFERTA ABERTA — a vitrine
            # de verdade, e hoje a lista e VAZIA. Ela existe no pacote porque e
            # dela que o navegador reclassifica os grupos quando a pessoa troca
            # o peso: sem ela, o dia em que um registro ganhasse link seria o
            # dia em que a recomputacao o deixaria CAIR DA TELA, servindo menos
            # do que o servidor serviu. E a familia da 32.5-d — a metade do
            # servidor e a do navegador discordando sobre o mesmo dado — e aqui
            # ela esta FECHADA em vez de pre-registrada.
            "com_oferta": [
                {"id": r.get("id"), "nome": f3ref.nome_do_registro(r),
                 "carga_max_kg": float(f3ref._valor(r.get("carga_max_kg")))}
                for r in registros
                if r.get("status") != "excluido_do_banco"
                and f3ref._valor(r.get("carga_max_kg")) is not None
                and f3ref._tem_saida_de_compra(r)
            ],
        },
    }


def main():
    conferir = "--conferir" in sys.argv
    constantes = f3ref.carregar_constantes()
    with open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
        veiculos = json.load(f)

    novo = montar(constantes, veiculos)
    texto = json.dumps(novo, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            print("REPROVADO: %s nao existe. Rode sem --conferir." % SAIDA)
            return 1
        atual = open(SAIDA, encoding="utf-8").read()

        # O SELO `gerado_em` SAI DA COMPARACAO, e isto NAO e frouxidao: e a
        # licao de 30/10/2026 herdada pronta da irma. Ele e o RELOGIO DA
        # EXECUCAO, nao um dado derivado das entradas — a F3 nao usa a data
        # para nada que calcula. Comparando-o, este portao reprovaria a pagina
        # CERTA todo dia seguinte ao que ela foi gerada, que e exatamente o
        # perigo que a 20.5 nomeia. Todo o resto do arquivo continua cobrado.
        def sem_selo(bruto, rotulo):
            try:
                d = json.loads(bruto)
            except ValueError as e:
                print("REPROVADO: %s nao e JSON legivel (%s): %s" % (rotulo, SAIDA, e))
                return None
            d["gerado_em"] = "<selo-fora-da-comparacao>"
            return json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True)

        a, b = sem_selo(atual, "o arquivo gravado"), sem_selo(texto, "a referencia")
        if a is None:
            return 1
        if a != b:
            print("REPROVADO: dados/f3-respostas.json esta diferente do que a "
                  "referencia produz agora, FORA do selo `gerado_em`. Rode "
                  "`python3 ferramentas/gerar-f3.py`.")
            return 1
        print("APROVADO: dados/f3-respostas.json bate com a referencia "
              "(o selo `gerado_em` fica fora da comparacao, de proposito).")
        return 0

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    c = novo["compra"]
    print("gravado %s" % SAIDA)
    print("  tabela: %d linhas de peso, cada uma com a carga minima recomputada"
          % novo["tabela"]["total_de_linhas"])
    print("  vitrine: %d item(ns) — %d registro(s) declaram carga, %d aguentariam o "
          "caso de exemplo, %d com oferta aberta"
          % (len(c["vitrine"]), c["quantos_declaram_carga"],
             c["quantos_serviriam_sem_oferta"], len(c["grupos"]["folga"])))
    print("  prestacao de contas (soma fecha %d registros): %s"
          % (c["total_registros_veiculos"], c["contagem"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

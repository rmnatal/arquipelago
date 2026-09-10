#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implementacao de REFERENCIA da R2 e varredura da entrada dela de ponta a ponta.

Roda sem dependencia e sem rede:

    python3 ferramentas/cobertura-r2.py            # relatorio na tela
    python3 ferramentas/cobertura-r2.py --gravar   # grava dados/cobertura-r2.json
                                                   # e dados/tabela-exemplos-r2.md

Este arquivo NUNCA e publicado no site: e ferramenta de bancada, como o
validar-banco.py e o cobertura-r1.py.

POR QUE ELE EXISTE, e por que a regra da R2 nasce aqui e nao em PHP.

A R1 fixou cinco decisoes de desenho (PROMPT.md da ilha, bloco 4) e a segunda
delas e esta: a regra mora na implementacao de referencia, e o snippet nao a
reescreve. Escrever pela primeira vez, direto num snippet que so roda com o site
no ar, quais fontes se aplicam a qual situacao, qual limiar vale, quem passa na
elegibilidade e quantos ciclos uma metragem exige seria escrever a regra onde ela
nao pode ser conferida. Aqui ela roda contra o banco commitado e a resposta
aparece frase a frase; ferramentas/teste-r2.php compara as duas implementacoes.

O QUE A R2 TEM DE DIFERENTE DA R1, e muda a forma da prova: a entrada da R1 e
uma lista fechada de 28 modelos, entao o gerador consegue pre-calcular TODA
resposta possivel. A da R2 tem uma metragem continua de 10 a 400 m2. Logo o PHP
faz aritmetica, e a prova de que ele faz a mesma conta que a referencia e uma
GRADE declarada: as 9 situacoes inteiras, mais a metragem varrida de 10 em 10 m2
contra cada modelo de referencia. A grade esta em dados/r2-referencia.json e o
teste percorre a grade inteira, nao uma amostra.

AS TRES HONESTIDADES DA ESPECIFICACAO (secao 2.2 de especificacao-calculadoras.md)
estao implementadas como medicao, nao como aviso decorativo:

  1. area_informada e area LIVRE de piso. Nenhum coeficiente de obstrucao — seria
     dado inventado.
  2. Conta de mais de um ciclo so vale se o modelo retomar de onde parou. Sem
     retoma_apos_recarga declarado, o numero NAO e publicado.
  3. Cobertura por carga so entra se o fabricante declarar. Nao se converte
     minuto em metro quadrado: a constante taxa-cobertura-m2-por-min esta
     PROIBIDA em formula publicada (secao 10 do ARQUIPELAGO.md).

O ACHADO DESTA EXECUCAO, que a varredura mede e a pagina publica: o
"TEMPO REAL ATE TERMINAR" da especificacao precisa de TRES numeros declarados
pelo fabricante — cobertura por carga, autonomia e tempo de recarga — e NENHUM
modelo do banco tem os tres. Quem declara cobertura (Electrolux) nao declara
recarga; quem declara recarga (Xiaomi S20, Positivo PRA2000) nao declara
cobertura. Entao a R2 publica os CICLOS e o tempo de limpeza somado, e diz com
todas as letras que o tempo total depende de um numero que o fabricante nao
publica. Isso nao e uma pendencia envergonhada: e a diferenca entre esta pagina e
um site que promete "termina em 2 horas" sem ter a conta.
"""

import json
import math
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

# ------------------------------------------------------------------ ENTRADA
# A faixa e a da especificacao (secao 2.4). O passo da varredura e de 10 m2:
# e o que da uma grade densa o bastante para pegar todo salto de ciclo dos
# modelos do banco (o menor deles cobre 162 m2) sem inflar o gabarito.
AREA_MINIMA = 10
AREA_MAXIMA = 400
PASSO_DA_VARREDURA = 10

PISOS = ["liso", "tapete fino", "carpete"]
PELOS = ["nao", "curto", "longo"]

# As metragens que o CORPUS desta ilha nomeia, com a linha que as nomeia. Nao sao
# um chute de "casa tipica": sao as metragens que aparecem escritas em
# dados/corpus-buscas.md, cluster B2/B3. A ancora sai daqui por regra.
METRAGENS_DO_CORPUS = [
    (60, "apartamento 60-80 m2, minimo aceitavel 90 minutos de autonomia (forum)"),
    (80, "robo aspirador para 80 m2 apartamento pequeno (busca web direta)"),
    (100, "faixa 'intermediario 100-150 m2' (Mundo Conectado)"),
    (150, "faixa 'premium 150-200+ m2' (Mundo Conectado)"),
    (200, "robo aspirador que passa pano em casa de 200 m2 (Canaltech)"),
]

# A tabela de exemplos pre-renderizada da secao 2.7 exige 40, 60, 80, 120 e 200
# m2 no minimo. As metragens do corpus entram junto, porque sao as que alguem
# realmente digita.
METRAGENS_DA_TABELA = sorted(
    {40, 60, 80, 120, 200} | {m for m, _ in METRAGENS_DO_CORPUS}
)


# ------------------------------------------------------- QUAL FONTE VALE ONDE
#
# Cada regra abaixo diz TRES coisas: qual constante, em que situacao ela vale, e
# QUE PALAVRAS da propria fonte justificam aplica-la ali. A terceira e a que
# impede a tabela de virar gosto de quem grava: se a fonte nao nomeia a situacao,
# nao ha regra, e a R2 diz que nao ha (veja PONTE, abaixo).
#
# `papel`:
#   limiar — entra na conta do maior e do menor limiar citado
#   teto   — NAO entra. E o numero acima do qual a propria fonte diz que mais
#            succao deixa de comprar melhora percebida. Serve contra o nicho:
#            e o que impede a R2 de virar corrida de Pa.
REGRAS_DE_LIMIAR = [
    {
        "constante": "pa-piso-liso-sujeira-leve",
        "papel": "limiar",
        "comparacao": "suficiente",   # "ate 1.500 Pa basta" -> pa >= valor atende
        "pisos": ["liso"],
        "pelos": ["nao"],
        "palavras_da_fonte": "piso liso, sujeira leve",
    },
    {
        "constante": "pa-apartamento-piso-liso",
        "papel": "limiar",
        "comparacao": "recomendado",  # pa >= valor
        "pisos": ["liso"],
        "pelos": ["nao"],
        "palavras_da_fonte": "apartamento com piso liso e pouca circulacao",
    },
    {
        "constante": "pa-apartamento-pequeno-sem-pet",
        "papel": "limiar",
        "comparacao": "recomendado",
        "pisos": ["liso"],
        "pelos": ["nao"],
        "palavras_da_fonte": "apartamento pequeno sem animais, uso do dia a dia",
    },
    {
        "constante": "pa-limiar-pet-canaltech",
        "papel": "limiar",
        "comparacao": "acima_de",     # pa > valor. "acima de" e exclusivo, e isso
                                      # muda quem entra na lista (veja no_limiar)
        "pisos": ["liso", "tapete fino", "carpete"],
        "pelos": ["curto", "longo"],
        "tambem_quando": {"pisos": ["carpete"], "pelos": ["nao", "curto", "longo"]},
        "palavras_da_fonte": "ideal para pelo de pet e carpete",
    },
    {
        "constante": "pa-limiar-pet-mundoconectado",
        "papel": "limiar",
        "comparacao": "recomendado",  # o consenso citado e "acima de 3.000"; o
                                      # campo do banco e valor_minimo, e a fonte
                                      # o apresenta como piso do consenso
        "campo_do_valor": "valor_minimo",
        "pisos": ["liso", "tapete fino", "carpete"],
        "pelos": ["curto", "longo"],
        "palavras_da_fonte": "casa com pet: consenso acima de 3.000 Pa, faixa confortavel entre 4.000 e 6.000 Pa",
    },
    {
        "constante": "pa-limite-pratico-percebido",
        "papel": "teto",
        "comparacao": "acima_de",
        "pisos": ["liso", "tapete fino"],
        "pelos": ["nao", "curto", "longo"],
        "palavras_da_fonte": "piso liso com tapete pontual: acima disto o resultado fica proximo do limite pratico percebido",
    },
]

# A PONTE: a unica situacao que nenhuma fonte deste banco nomeia.
#
# "tapete fino sem animal" fica entre duas situacoes que as fontes nomeiam — piso
# liso sem animal (Mundo Conectado) e carpete (Canaltech) — e nenhuma das duas a
# cita. A R2 nao inventa um limiar para ela: publica as duas vizinhas com nome e
# data, e resolve para a de CIMA, porque a assimetria de custo manda (secao 10 do
# ARQUIPELAGO.md). Errar para baixo aqui faz alguem comprar um robo que nao da
# conta do tapete — a compra inteira se perde. Errar para cima faz gastar a mais
# num robo que limpa, e o teto de utilidade limita esse excesso.
#
# A ponte fica DECLARADA, com bandeira propria no resultado, para a pagina poder
# dizer ao leitor que ali ela esta estendendo uma fonte em vez de citando uma.
SITUACOES_SEM_FONTE_DIRETA = [("tapete fino", "nao")]

# As duas situacoes vizinhas que a ponte cita, nesta ordem: a de baixo e a de
# cima. Ficam declaradas em vez de deduzidas para a frase publicada nao depender
# de uma busca no meio da lista de regras.
VIZINHAS_DA_PONTE = {("tapete fino", "nao"): (("liso", "nao"), ("carpete", "nao"))}

# O ARTIGO de cada publicador citado, porque a frase publicada leva o nome dentro
# de uma oracao ("a Canaltech recomenda", "o Mundo Conectado trata").
#
# Fica declarado, e nao adivinhado, pelo mesmo motivo que ROTULOS_DE_ORIGEM em
# gerar-r1.py: publicador novo sem artigo declarado sairia na tela com o artigo
# errado, em silencio, no meio de uma frase que a pagina afirma. Melhor parar.
ARTIGO_DO_PUBLICADOR = {
    "Canaltech": "a",
    "Mundo Conectado": "o",
}


def carregar(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return json.load(fh)


def formatar_data(iso):
    """2026-09-09 -> 09/09/2026. A frase publicada leva data em portugues."""
    if not iso or len(iso) != 10:
        return iso or "sem data"
    a, m, d = iso.split("-")
    return "%s/%s/%s" % (d, m, a)


def numero_br(n):
    """1500 -> 1.500. O separador de milhar do texto publicado e o ponto."""
    return "{:,}".format(int(n)).replace(",", ".")


# --------------------------------------------------------------- CARGA
esquema = carregar("esquema-banco.json")
marcas = {m["id"]: m for m in carregar("marcas.json")["registros"]}
doc_modelos = carregar("modelos-robo.json")
doc_constantes = carregar("constantes.json")

modelos = doc_modelos["registros"]
constantes = {c["id"]: c for c in doc_constantes["constantes"]}

VOC_PISO = esquema["vocabularios"].get("tipo_de_piso")
VOC_PELO = esquema["vocabularios"].get("pelo_de_pet")


def _conferir_vocabulario():
    """O esquema e quem manda no vocabulario da entrada.

    Se um dia o esquema ganhar um tipo de piso que esta lista nao tem, a
    ferramenta estaria oferecendo uma faixa menor do que o banco consegue
    produzir — e ninguem perceberia, porque a tela continuaria bonita. Melhor
    parar aqui.
    """
    for nome, voc, usados in (("tipo_de_piso", VOC_PISO, PISOS),
                              ("pelo_de_pet", VOC_PELO, PELOS)):
        if not voc:
            continue
        for v in usados:
            if v not in voc:
                sys.stderr.write(
                    "ERRO: %r nao existe no vocabulario %s do esquema.\n" % (v, nome)
                )
                sys.exit(1)


_conferir_vocabulario()


def valor(campo):
    """Campo do banco que pode ser {'valor': x, ...} ou o proprio x."""
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def publicaveis():
    return [m for m in modelos if m.get("status") == "publicavel"]


def rotulo_do_modelo(m):
    return "%s %s" % (marcas[m["marca"]]["nome"], m["codigo_fabricante"])


# ------------------------------------------------- A REGRA DA R2, EM UM LUGAR SO
def regra_vale(regra, piso, pelo):
    if piso in regra["pisos"] and pelo in regra["pelos"]:
        return True
    tambem = regra.get("tambem_quando")
    if tambem and piso in tambem["pisos"] and pelo in tambem["pelos"]:
        return True
    return False


def limiar_da_regra(regra):
    """A regra, virada em numero + procedencia, lida da constante.

    O valor nunca e digitado aqui: sai de dados/constantes.json. Uma constante
    que mudar de numero muda a resposta da ferramenta no mesmo commit, sem
    ninguem lembrar de atualizar duas listas.
    """
    c = constantes[regra["constante"]]
    if c.get("status") not in ("publicavel",):
        return None
    campo = regra.get("campo_do_valor", "valor")
    v = c.get(campo)
    if v is None:
        return None
    return {
        "constante": c["id"],
        "papel": regra["papel"],
        "valor": int(v),
        "comparacao": regra["comparacao"],
        "publicador": c["fonte"].split(" — ")[0],
        "fonte": c["fonte"],
        "url": c.get("url"),
        "verificado_em": c.get("verificado_em"),
        "palavras_da_fonte": regra["palavras_da_fonte"],
        "faixa_confortavel": c.get("faixa_confortavel"),
    }


def atende(pa, limiar):
    """Um Pa declarado atende a este limiar?

    A distincao entre 'acima_de' e o resto NAO e preciosismo: a Canaltech escreve
    "acima de 4.000 Pa", e um modelo de exatamente 4.000 Pa nao esta acima de
    4.000. Tratar os dois como iguais colocaria em primeiro lugar, numa lista de
    recomendacao, um modelo que a propria fonte citada nao cobre — que e a
    familia de defeito que a secao 7 do ARQUIPELAGO.md chama de grave. O modelo
    que fica exatamente no valor nao some: vai para um grupo proprio, rotulado.
    """
    if pa is None:
        return False
    if limiar["comparacao"] == "acima_de":
        return pa > limiar["valor"]
    return pa >= limiar["valor"]


def esta_no_limiar(pa, limiar):
    return pa is not None and limiar["comparacao"] == "acima_de" and pa == limiar["valor"]


def piso_efetivo(limiar):
    """Chave de ordenacao entre limiares: valor, e o exclusivo vale mais."""
    return (limiar["valor"], 1 if limiar["comparacao"] == "acima_de" else 0)


def limiares_da_situacao(piso, pelo):
    """As fontes que nomeiam esta situacao, ja como numero e procedencia.

    Devolve (limiares, teto, por_ponte). `por_ponte` e verdadeiro quando nenhuma
    fonte nomeia a situacao e a R2 esta estendendo as vizinhas — e nesse caso a
    pagina diz isso, em vez de fingir que citou alguem.
    """
    diretos = []
    teto = None
    for regra in REGRAS_DE_LIMIAR:
        if not regra_vale(regra, piso, pelo):
            continue
        l = limiar_da_regra(regra)
        if l is None:
            continue
        if l["papel"] == "teto":
            if teto is None or piso_efetivo(l) < piso_efetivo(teto):
                teto = l
        else:
            diretos.append(l)

    if diretos:
        return sorted(diretos, key=piso_efetivo), teto, False

    if (piso, pelo) not in SITUACOES_SEM_FONTE_DIRETA:
        # Situacao sem fonte e sem ponte declarada seria a ferramenta respondendo
        # do nada. Nao acontece com o banco de hoje, e se acontecer e defeito.
        return [], teto, False

    # A PONTE: as duas vizinhas nomeadas, e de cada uma o limiar que ELA
    # publicaria — nunca o menor numero que aparece na vizinha de baixo. A
    # vizinha de baixo responde "3.000 Pa" a quem pergunta por ela; citar dela o
    # "1.500 Pa basta" seria montar uma faixa mais larga do que qualquer fonte
    # sustenta, justo na situacao em que ja estamos estendendo.
    de_baixo, de_cima = VIZINHAS_DA_PONTE[(piso, pelo)]
    vizinhas = []
    for p, q in (de_baixo, de_cima):
        diretos_da_vizinha = []
        for regra in REGRAS_DE_LIMIAR:
            if regra["papel"] != "limiar" or not regra_vale(regra, p, q):
                continue
            l = limiar_da_regra(regra)
            if l is not None:
                diretos_da_vizinha.append(l)
        if diretos_da_vizinha:
            vizinhas.append(sorted(diretos_da_vizinha, key=piso_efetivo)[-1])
    return sorted(vizinhas, key=piso_efetivo), teto, True


def situacao(piso, pelo):
    """A resposta de Pa para uma situacao — sem metragem, que aqui nao entra."""
    limiares, teto, por_ponte = limiares_da_situacao(piso, pelo)
    if not limiares:
        return None

    seguro = limiares[-1]
    minimo = limiares[0]

    faixa = None
    for l in limiares:
        if l.get("faixa_confortavel"):
            faixa = {
                "de": int(l["faixa_confortavel"][0]),
                "ate": int(l["faixa_confortavel"][1]),
                "publicador": l["publicador"],
                "url": l["url"],
                "verificado_em": l["verificado_em"],
            }
            break

    return {
        "piso": piso,
        "pelo": pelo,
        "limiares": limiares,
        "limiar_seguro": seguro,
        "limiar_minimo": minimo,
        "ha_divergencia": piso_efetivo(seguro) != piso_efetivo(minimo),
        "faixa_confortavel": faixa,
        "teto": teto,
        "por_ponte": por_ponte,
    }


# ----------------------------------------------------------- ELEGIBILIDADE
def classificar_modelos(sit):
    """Quem entra na lista de recomendados desta situacao, e em que grupo.

    A ordem e a da secao 7 do ARQUIPELAGO.md, e as tres camadas ficam separadas
    de proposito:

      1. ELEGIBILIDADE TECNICA COMPLETA. Aqui e a condicao (1) da secao 2.6 da
         especificacao: pa_declarado atende ao MAIOR limiar citado. As condicoes
         (2) e (3) nao sao ignoradas — sao MEDIDAS e, hoje, nao se aplicam a
         nenhum elegivel: nenhum modelo com Pa declarado tem cobertura por carga
         declarada, e nenhum modelo publicavel declara voltagem. O que a
         ferramenta nao sabe, ela diz no cartao; nao promove a silencio.

      2. ADEQUACAO TECNICA entre os elegiveis. Nao e "mais Pa e melhor": dentro
         da faixa util (do limiar seguro ate o teto de utilidade) a folga compra
         resultado, e acima do teto a propria fonte diz que deixa de comprar
         melhora percebida. Entao ordena-se pela faixa util primeiro, com mais
         folga na frente, e o excesso depois, do menor excesso para o maior.

      3. DESEMPATE por link de loja, e so como desempate entre equivalentes.
         Nunca comparar comissao, nunca promover produto pior porque paga mais.
    """
    seguro = sit["limiar_seguro"]
    teto = sit["teto"]

    elegiveis, no_limiar, nao_atendem, sem_pa = [], [], [], []

    for m in publicaveis():
        pa = valor(m.get("pa_declarado"))
        if pa is None:
            sem_pa.append(m)
            continue
        if atende(pa, seguro):
            elegiveis.append(m)
        elif esta_no_limiar(pa, seguro):
            no_limiar.append(m)
        else:
            nao_atendem.append(m)

    def chave(m):
        pa = valor(m.get("pa_declarado"))
        acima_do_teto = 1 if (teto and pa > teto["valor"]) else 0
        tem_link = 0 if (m.get("afiliado") or {}).get("url") else 1
        # dentro da faixa util: mais folga primeiro (-pa). acima do teto: menos
        # excesso primeiro (+pa).
        return (acima_do_teto, pa if acima_do_teto else -pa, tem_link, m["id"])

    elegiveis.sort(key=chave)
    no_limiar.sort(key=lambda m: m["id"])

    return {
        "elegiveis": elegiveis,
        "no_limiar": no_limiar,
        "nao_atendem": nao_atendem,
        "sem_pa_declarado": sem_pa,
    }


def ressalvas_do_modelo(m, sit, area=None):
    """O que a ferramenta NAO sabe sobre este modelo, dito no proprio cartao.

    Existe porque a condicao (2) da elegibilidade — se a metragem passa da
    cobertura por carga, o modelo precisa retomar depois de recarregar — e hoje
    INVERIFICAVEL para todo modelo que declara Pa: nenhum deles declara cobertura.
    Calar isso deixaria a lista com cara de completa. Dizer transforma a lacuna
    em informacao, que e o que separa esta pagina de um comparativo de anuncio.
    """
    saida = []
    cob = valor(m.get("cobertura_m2_declarada"))
    if cob is None:
        saida.append("cobertura_nao_declarada")
    elif area is not None and area > cob:
        if valor(m.get("retoma_apos_recarga")) is not True:
            saida.append("passa_da_carga_e_nao_declara_retomada")
        else:
            saida.append("passa_da_carga_mas_retoma")
    pa = valor(m.get("pa_declarado"))
    if sit["teto"] and pa is not None and pa > sit["teto"]["valor"]:
        saida.append("acima_do_teto_de_utilidade")
    return saida


# --------------------------------------------------- CICLOS E TEMPO REAL
def modelos_de_referencia():
    """So quem declara cobertura por carga entra no seletor de referencia.

    Mesma regra do seletor de tipo de peca da R1 (secao 1.2 da especificacao):
    oferecer uma escolha que sempre devolve recusa contraria a promessa antes do
    formulario e ensina o visitante que a ferramenta nao sabe responder.
    """
    lista = [m for m in publicaveis() if valor(m.get("cobertura_m2_declarada")) is not None]
    lista.sort(key=lambda m: (0 if valor(m.get("retoma_apos_recarga")) is True else 1,
                              -valor(m.get("cobertura_m2_declarada")),
                              m["id"]))
    return lista


def areas_da_grade(m):
    """A metragem varrida contra um modelo de referencia.

    O passo regular de 10 m2 NAO basta, e isso nao e opiniao: ficou medido em
    10/09/2026 quebrando o codigo de proposito. Trocar o `ceil` da divisao por
    `floor + 1` nao muda resposta nenhuma numa grade de 10 em 10, porque as
    coberturas declaradas do banco (162 e 166 m2) nao tem multiplo terminado em
    zero. As duas contas so divergem EXATAMENTE em cima do multiplo — que e onde
    erro de arredondamento mora, e era o unico lugar onde a grade regular nao
    pisava. Uma grade que nao cobre a borda e uma amostra com nome de grade.

    Entao a varredura leva, alem do passo: cada multiplo da cobertura declarada,
    e o vizinho de cada lado dele.
    """
    cob = valor(m.get("cobertura_m2_declarada"))
    areas = set(range(AREA_MINIMA, AREA_MAXIMA + 1, PASSO_DA_VARREDURA))
    if cob:
        k = 1
        while cob * k <= AREA_MAXIMA:
            for a in (cob * k - 1, cob * k, cob * k + 1):
                if AREA_MINIMA <= a <= AREA_MAXIMA:
                    areas.add(a)
            k += 1
    return sorted(areas)


def ciclos(area, m):
    """CICLOS = teto( area / cobertura_declarada_por_carga ).

    E a primeira formula da secao 2.2 da especificacao, e a unica das duas que o
    banco de hoje sustenta inteira.
    """
    cob = valor(m.get("cobertura_m2_declarada"))
    if cob is None or not cob:
        return None
    return int(math.ceil(float(area) / float(cob)))


def tempo(area, m):
    """A conta de tempo, com o que falta dito em vez de preenchido.

    TEMPO REAL ATE TERMINAR = ciclos x autonomia + (ciclos-1) x recarga.

    O terceiro numero — a recarga — nao existe declarado para NENHUM modelo que
    declara cobertura. Entao esta funcao devolve o que da para sustentar (os
    ciclos e o tempo de limpeza somado) e nomeia o que falta. Preencher a recarga
    com media de mercado seria exatamente o que as fazendas fazem, e o que a
    secao 10 do contrato proibe.
    """
    n = ciclos(area, m)
    if n is None:
        return None

    aut = valor(m.get("autonomia_min_declarada"))
    rec = valor(m.get("recarga_min_declarada"))
    retoma = valor(m.get("retoma_apos_recarga"))

    # Honestidade 2 da especificacao: sem retomada declarada, a conta de mais de
    # um ciclo perde sentido e NAO e publicada.
    multiciclo_valido = (n == 1) or (retoma is True)

    saida = {
        "ciclos": n,
        "cobertura_m2": valor(m.get("cobertura_m2_declarada")),
        "autonomia_min": aut,
        "recarga_min": rec,
        "retoma_apos_recarga": retoma,
        "multiciclo_valido": multiciclo_valido,
        "tempo_de_limpeza_min": (aut * n) if (aut is not None and multiciclo_valido) else None,
        "tempo_total_min": None,
        "falta_para_o_total": None,
    }

    if multiciclo_valido and aut is not None:
        if n == 1:
            saida["tempo_total_min"] = aut
        elif rec is not None:
            saida["tempo_total_min"] = aut * n + rec * (n - 1)
        else:
            saida["falta_para_o_total"] = "recarga_min_declarada"

    return saida


# ------------------------------------------------------------------- FRASES
#
# As frases desta secao sao o GABARITO: saem em ASCII, como todo o banco desta
# ilha, e o snippet escreve as mesmas em portugues acentuado. ferramentas/
# teste-r2.php compara as duas ignorando acento. Cada molde e escolhido por
# MEDICAO — quantas fontes nomeiam a situacao, quantos ciclos a metragem exige,
# se o fabricante declara a retomada — e nunca por um "se" escrito a mao na tela.
NOME_DO_PISO = {
    "liso": "piso liso",
    "tapete fino": "tapete fino",
    "carpete": "carpete",
}

NOME_DO_PELO = {
    "nao": "sem animal que solta pelo",
    "curto": "com animal de pelo curto",
    "longo": "com animal de pelo longo",
}


def escrever_limiar(l):
    if l["comparacao"] == "acima_de":
        return "acima de %s Pa" % numero_br(l["valor"])
    if l["comparacao"] == "suficiente":
        return "ate %s Pa ja basta" % numero_br(l["valor"])
    return "%s Pa" % numero_br(l["valor"])


def com_artigo(publicador):
    """"a Canaltech", "o Mundo Conectado" — o artigo vem da tabela declarada."""
    if publicador not in ARTIGO_DO_PUBLICADOR:
        sys.stderr.write(
            "ERRO: o publicador %r nao tem artigo declarado em "
            "ARTIGO_DO_PUBLICADOR. Declare antes de publicar a frase.\n" % publicador
        )
        sys.exit(1)
    return "%s %s" % (ARTIGO_DO_PUBLICADOR[publicador], publicador)


def plural(n, singular, plural_):
    return "%d %s" % (n, singular if n == 1 else plural_)


def frase_da_situacao(sit):
    """A resposta de Pa, em uma frase autossuficiente (secao 2.8).

    TRES moldes, escolhidos pela contagem de fontes que nomeiam a situacao:
    duas ou mais e divergencia publicada; uma e recomendacao unica declarada como
    unica; nenhuma e a ponte, dita como ponte.
    """
    piso = NOME_DO_PISO[sit["piso"]]
    pelo = NOME_DO_PELO[sit["pelo"]]
    seguro = sit["limiar_seguro"]
    minimo = sit["limiar_minimo"]

    if sit["por_ponte"]:
        return (
            "Para %s %s, nenhuma das fontes brasileiras deste banco nomeia a "
            "situacao. As duas vizinhas que elas nomeiam sao %s (%s) e %s (%s), "
            "e esta pagina resolve para a de cima — errar para baixo aqui faz "
            "comprar um robo que nao da conta, e a compra inteira se perde."
            % (piso, pelo,
               escrever_limiar(minimo), com_artigo(minimo["publicador"]),
               escrever_limiar(seguro), com_artigo(seguro["publicador"]))
        )

    if sit["ha_divergencia"]:
        return (
            "Para %s %s, as fontes brasileiras divergem: %s recomenda %s e %s trata "
            "%s como o piso do consenso (verificado em %s). Esta pagina trabalha com "
            "o MAIOR limiar citado, porque errar para baixo custa a compra inteira."
            % (piso, pelo,
               com_artigo(seguro["publicador"]), escrever_limiar(seguro),
               com_artigo(minimo["publicador"]), escrever_limiar(minimo),
               formatar_data(seguro["verificado_em"]))
        )

    return (
        "Para %s %s, a unica recomendacao brasileira deste banco e a de %s: %s "
        "(verificado em %s)."
        % (piso, pelo, com_artigo(seguro["publicador"]), escrever_limiar(seguro),
           formatar_data(seguro["verificado_em"]))
    )


def frase_do_teto(sit):
    if not sit["teto"]:
        return None
    t = sit["teto"]
    return (
        "Acima de %s Pa, %s escreve que o resultado ja fica proximo do limite "
        "pratico percebido — dai para cima, mais succao deixa de comprar melhora "
        "que alguem note (verificado em %s)."
        % (numero_br(t["valor"]), com_artigo(t["publicador"]),
           formatar_data(t["verificado_em"]))
    )


def frase_da_classe_de_fonte():
    """O aviso da secao 2.5, que e regra e nao rodape.

    Fabricante declara o Pa do aparelho; quanto Pa uma casa precisa e opiniao
    publicada, e opiniao publicada tem autor. Confundir os dois seria vender
    editorial como dado tecnico.
    """
    return (
        "Os limiares de Pa desta pagina NAO sao especificacao de fabricante: sao "
        "recomendacao publicada por veiculo brasileiro, e cada uma sai com o nome "
        "de quem a recomenda. O Pa de cada robo, esse sim, e declarado pelo "
        "fabricante."
    )


def frase_do_ciclo(area, m, t):
    """A conta que ninguem publica — e o que falta para completa-la.

    QUATRO moldes, escolhidos por medicao: um ciclo; mais de um ciclo com
    retomada declarada; mais de um ciclo sem retomada declarada; e o caso em que
    o fabricante nao declara cobertura, que nem chega aqui porque o modelo nao
    entra no seletor de referencia.
    """
    rotulo = rotulo_do_modelo(m)
    cob = t["cobertura_m2"]
    aut = t["autonomia_min"]
    n = t["ciclos"]

    if n == 1:
        return (
            "Um %s, que o fabricante declara cobrir ate %s m2 por carga, faz %s m2 "
            "em um ciclo so — %s minutos de limpeza, dentro da autonomia declarada."
            % (rotulo, numero_br(cob), numero_br(area), numero_br(aut))
        )

    if not t["multiciclo_valido"]:
        return (
            "Um %s cobre ate %s m2 por carga, e %s m2 passam disso. O fabricante "
            "nao declara se este modelo retoma de onde parou depois de recarregar "
            "— sem esse dado a conta de mais de um ciclo nao se sustenta, e esta "
            "pagina nao a publica."
            % (rotulo, numero_br(cob), numero_br(area))
        )

    if t["tempo_total_min"] is not None:
        return (
            "Um %s cobre ate %s m2 por carga, entao %s m2 exigem %d ciclos: %s "
            "minutos de limpeza mais %s, e a casa fica pronta em %s minutos. O "
            "fabricante declara que este modelo retoma de onde parou."
            % (rotulo, numero_br(cob), numero_br(area), n,
               numero_br(t["tempo_de_limpeza_min"]),
               plural(n - 1, "recarga", "recargas"),
               numero_br(t["tempo_total_min"]))
        )

    return (
        "Um %s cobre ate %s m2 por carga, entao %s m2 exigem %d ciclos: %s minutos "
        "de limpeza somados, mais %s. O fabricante declara que este modelo retoma "
        "de onde parou, mas NAO declara quanto tempo a recarga leva — por isso "
        "publicamos os ciclos e nao o tempo total."
        % (rotulo, numero_br(cob), numero_br(area), n,
           numero_br(t["tempo_de_limpeza_min"]),
           plural(n - 1, "recarga", "recargas"))
    )


def frase_da_recusa_de_conversao():
    """Por que a R2 nao converte minuto em metro quadrado — com numeros do banco.

    A frase nao e digitada: os dois pares declarados e a contagem de marcas que
    nao declaram saem da varredura. No dia em que uma marca passar a declarar,
    esta frase muda sozinha.
    """
    pares = [m for m in publicaveis()
             if valor(m.get("cobertura_m2_declarada")) is not None
             and valor(m.get("autonomia_min_declarada")) is not None]
    marcas_que_declaram = sorted({m["marca"] for m in pares})
    marcas_todas = sorted({m["marca"] for m in publicaveis()})
    marcas_mudas = [b for b in marcas_todas if b not in marcas_que_declaram]

    taxas = sorted({
        round(valor(m["cobertura_m2_declarada"]) / float(valor(m["autonomia_min_declarada"])), 2)
        for m in pares
    })

    dispersao = ""
    if len(taxas) >= 2:
        dispersao = (
            " Entre os pares declarados a taxa vai de %s a %s m2 por minuto — %d%% "
            "de diferenca dentro do MESMO fabricante." % (
                ("%.2f" % taxas[0]).replace(".", ","),
                ("%.2f" % taxas[-1]).replace(".", ","),
                int(round((taxas[-1] / taxas[0] - 1) * 100)),
            )
        )

    return (
        "Esta ferramenta nao converte minutos em metros quadrados. Das %d marcas "
        "publicaveis do banco, %d nao declaram area coberta por carga em canal "
        "nenhum (%s) — declaram minutos, e algumas nem isso.%s Uma taxa geral de "
        "m2 por minuto nao existe publicada, e inventa-la seria dar ao leitor um "
        "numero que nenhum fabricante sustenta."
        % (len(marcas_todas), len(marcas_mudas),
           ", ".join(marcas[b]["nome"] for b in marcas_mudas), dispersao)
    )


def frase_do_funil_partido():
    """Quem o banco tem e a R2 nao consegue recomendar, e por que.

    Nao e desculpa: e a medida da emenda entre as duas ferramentas da ilha, e ela
    ja esta escrita na fila do 3c como a urgencia numero 1. A pagina publica o
    numero para o leitor saber que a lista curta e do mercado, nao de preguica.
    """
    sem_pa = [m for m in publicaveis() if valor(m.get("pa_declarado")) is None]
    marcas_sem = sorted({m["marca"] for m in sem_pa})
    marcas_com = {m["marca"] for m in publicaveis()
                  if valor(m.get("pa_declarado")) is not None}
    # Marca MUDA e a que nao declara Pa em modelo nenhum; marca PARCIAL declara em
    # alguns e cala em outros. Somar as duas numa frase so diria "a WAP nao publica
    # pascal" quando a WAP publica — para um dos modelos dela. E o tipo de
    # generalizacao que a pagina cobra dos outros.
    mudas = [b for b in marcas_sem if b not in marcas_com]
    parciais = [b for b in marcas_sem if b in marcas_com]
    trecho = "%s nao declaram succao em pascal em modelo nenhum" % (
        ", ".join(marcas[b]["nome"] for b in mudas))
    if parciais:
        trecho += "; %s declara em parte da linha e cala no resto" % (
            ", ".join(marcas[b]["nome"] for b in parciais))
    return (
        "%d dos %d modelos publicaveis do banco nao entram em lista nenhuma desta "
        "ferramenta: %s. Sao, em boa parte, exatamente os modelos que a outra "
        "ferramenta desta ilha responde melhor — quem publica codigo de peca "
        "costuma nao publicar pascal, e vice-versa."
        % (len(sem_pa), len(publicaveis()), trecho)
    )


def frase_do_cartao(m, sit, ressalvas):
    """A especificacao que fez o produto entrar (secao 6 do ARQUIPELAGO.md).

    O cartao nunca diz so "recomendado": diz o numero que o fabricante declarou,
    contra qual limiar e de quem e o limiar. E, quando a ferramenta nao sabe algo
    que importa para a decisao, o cartao diz isso tambem.
    """
    pa = valor(m.get("pa_declarado"))
    seguro = sit["limiar_seguro"]
    base = (
        "%s: %s Pa declarados pelo fabricante, %s do limiar de %s Pa que %s "
        "recomenda para a sua situacao."
        % (rotulo_do_modelo(m), numero_br(pa),
           "acima" if pa > seguro["valor"] else "no minimo",
           numero_br(seguro["valor"]), com_artigo(seguro["publicador"]))
    )
    extras = []
    if "acima_do_teto_de_utilidade" in ressalvas:
        extras.append(
            "esta acima dos %s Pa em que %s ve o limite pratico percebido"
            % (numero_br(sit["teto"]["valor"]), com_artigo(sit["teto"]["publicador"]))
        )
    if "cobertura_nao_declarada" in ressalvas:
        extras.append(
            "o fabricante nao declara area coberta por carga para este modelo, "
            "entao nao da para dizer se ele termina a sua metragem numa carga"
        )
    if "passa_da_carga_e_nao_declara_retomada" in ressalvas:
        extras.append(
            "a sua metragem passa da area declarada por carga e o fabricante nao "
            "declara se ele retoma de onde parou"
        )
    if extras:
        return base + " Ressalva: " + "; ".join(extras) + "."
    return base


def frase_do_no_limiar(m, sit):
    pa = valor(m.get("pa_declarado"))
    seguro = sit["limiar_seguro"]
    return (
        "%s declara exatamente %s Pa, e %s escreve \"acima de %s Pa\". Fica "
        "nesta secao separada porque estar no numero nao e estar acima dele."
        % (rotulo_do_modelo(m), numero_br(pa), com_artigo(seguro["publicador"]),
           numero_br(seguro["valor"]))
    )


def frase_de_lista_vazia(sit):
    return (
        "Nenhum modelo do banco atende ao limiar de %s Pa que %s recomenda para "
        "%s %s. Isto e o banco desta ilha, nao o mercado inteiro — e a lista de "
        "compras da proxima coleta comeca por aqui."
        % (numero_br(sit["limiar_seguro"]["valor"]),
           com_artigo(sit["limiar_seguro"]["publicador"]),
           NOME_DO_PISO[sit["piso"]], NOME_DO_PELO[sit["pelo"]])
    )


# --------------------------------------------------------------- A RESPOSTA
def responder_r2(area, piso, pelo, modelo_ref=None):
    """A resposta inteira de uma consulta. E o que o snippet tem que reproduzir.

    A frase de lista vazia e escrita DEPOIS de montar o resultado inteiro, nunca
    durante — e a licao que a R1 registrou em 10/09/2026, quando a pagina afirmou
    "a Electrolux nao vende o filtro avulso para este modelo" olhando uma peca de
    cada vez. Afirmacao sobre o conjunto so o conjunto sustenta.
    """
    sit = situacao(piso, pelo)
    if sit is None:
        return None

    grupos = classificar_modelos(sit)

    elegiveis = []
    for m in grupos["elegiveis"]:
        r = ressalvas_do_modelo(m, sit, area)
        elegiveis.append({
            "modelo": m["id"],
            "rotulo": rotulo_do_modelo(m),
            "pa": valor(m.get("pa_declarado")),
            "ressalvas": r,
            "frase": frase_do_cartao(m, sit, r),
        })

    no_limiar = [{
        "modelo": m["id"],
        "rotulo": rotulo_do_modelo(m),
        "pa": valor(m.get("pa_declarado")),
        "frase": frase_do_no_limiar(m, sit),
    } for m in grupos["no_limiar"]]

    ref = None
    if modelo_ref:
        m = next((x for x in modelos_de_referencia() if x["id"] == modelo_ref), None)
        if m is not None:
            t = tempo(area, m)
            ref = dict(t)
            ref["modelo"] = m["id"]
            ref["rotulo"] = rotulo_do_modelo(m)
            ref["frase"] = frase_do_ciclo(area, m, t)

    return {
        "area": area,
        "piso": piso,
        "pelo": pelo,
        "situacao": sit,
        "frase": frase_da_situacao(sit),
        "frase_do_teto": frase_do_teto(sit),
        "elegiveis": elegiveis,
        "no_limiar": no_limiar,
        # Escrita sobre o conjunto, e so depois de o conjunto existir.
        "frase_vazia": frase_de_lista_vazia(sit) if not elegiveis else None,
        "referencia": ref,
    }


# ------------------------------------------------------------------ ANCORA
def modelo_de_referencia_ancora():
    """O modelo de referencia da ancora, escolhido por REGRA.

    Preferencia por quem declara a retomada apos recarga, porque e o unico caso
    em que a conta de mais de um ciclo — a razao de a R2 existir — pode ser
    publicada. Depois, maior cobertura declarada; depois, ordem alfabetica.
    """
    lista = modelos_de_referencia()
    return lista[0] if lista else None


def situacao_ancora():
    """A situacao-ancora, por regra e nunca a dedo.

    Criterio, nesta ordem: (1) mais PUBLICADORES distintos nomeando a situacao —
    e a situacao sobre a qual mais gente se deu ao trabalho de escrever, e onde a
    divergencia publicada vale mais; (2) maior limiar seguro, que e onde a
    recomendacao e mais dificil e a resposta mais util; (3) ordem declarada de
    piso; (4) ordem declarada de pelo. Situacao por ponte nunca vira ancora: a
    resposta que a pagina serve sem clique nenhum precisa ser uma fonte citada,
    nao uma extensao nossa.
    """
    candidatas = []
    for piso in PISOS:
        for pelo in PELOS:
            sit = situacao(piso, pelo)
            if sit is None or sit["por_ponte"]:
                continue
            grupos = classificar_modelos(sit)
            if len(grupos["elegiveis"]) < 3:   # portao da secao 9 do contrato
                continue
            publicadores = {l["publicador"] for l in sit["limiares"]}
            candidatas.append((
                -len(publicadores),
                -piso_efetivo(sit["limiar_seguro"])[0],
                PISOS.index(piso),
                PELOS.index(pelo),
                piso, pelo,
            ))
    if not candidatas:
        return None
    c = sorted(candidatas)[0]
    return (c[4], c[5])


def area_ancora(m_ref):
    """A metragem da ancora: a menor do CORPUS que o modelo de referencia NAO
    termina numa carga.

    Duas razoes. A metragem sai do corpus, entao e uma que alguem digita de
    verdade — nao um numero redondo escolhido por quem escreve. E o criterio de
    mais de um ciclo faz a resposta servida sem clique nenhum ser justamente o
    numero que ninguem publica: quantos ciclos, e por que o tempo total depende de
    um dado que o fabricante nao declara. Ancora que sai em um ciclo mostraria a
    ferramenta no caso em que ela nao acrescenta nada.
    """
    if m_ref is None:
        return METRAGENS_DO_CORPUS[0][0]
    for area, _ in METRAGENS_DO_CORPUS:
        n = ciclos(area, m_ref)
        if n is not None and n > 1:
            return area
    return METRAGENS_DO_CORPUS[-1][0]


# --------------------------------------------------------------- VARREDURA
def varrer():
    """A entrada da R2 de ponta a ponta (secao 14.3 do ARQUIPELAGO.md).

    Duas dimensoes, e as duas de ponta a ponta: as 9 situacoes de piso x pelo, e
    a metragem de 10 a 400 m2 contra cada modelo de referencia. Contar itens do
    banco nao diria em quantas situacoes a ferramenta consegue recomendar 3
    modelos — so a varredura separa "acrescentei um item" de "tirei uma faixa do
    vazio".
    """
    faixas = []
    for piso in PISOS:
        for pelo in PELOS:
            sit = situacao(piso, pelo)
            if sit is None:
                faixas.append({
                    "piso": piso, "pelo": pelo, "sem_fonte": True,
                    "elegiveis": 0, "portao_3_itens": "SEM FONTE",
                })
                continue
            g = classificar_modelos(sit)
            marcas_eleg = sorted({m["marca"] for m in g["elegiveis"]})
            faixas.append({
                "piso": piso,
                "pelo": pelo,
                "por_ponte": sit["por_ponte"],
                "limiar_seguro": sit["limiar_seguro"]["valor"],
                "comparacao": sit["limiar_seguro"]["comparacao"],
                "publicador_seguro": sit["limiar_seguro"]["publicador"],
                "limiar_minimo": sit["limiar_minimo"]["valor"],
                "publicador_minimo": sit["limiar_minimo"]["publicador"],
                "elegiveis": len(g["elegiveis"]),
                "no_limiar": len(g["no_limiar"]),
                "marcas": [marcas[b]["nome"] for b in marcas_eleg],
                "portao_3_itens": "OK" if len(g["elegiveis"]) >= 3 else "FAIXA DESCOBERTA",
                "concentracao_de_marca": (
                    "ATENCAO: %d de %d elegiveis sao da mesma marca (%s)"
                    % (len(g["elegiveis"]), len(g["elegiveis"]),
                       marcas[marcas_eleg[0]]["nome"])
                    if len(marcas_eleg) == 1 and g["elegiveis"]
                    else "distribuida entre marcas" if g["elegiveis"] else "sem elegivel"
                ),
            })

    # A segunda dimensao: a metragem contra cada modelo de referencia.
    refs = []
    for m in modelos_de_referencia():
        saltos = []
        anterior = None
        for area in areas_da_grade(m):
            n = ciclos(area, m)
            if anterior is not None and n != anterior:
                saltos.append({"em_m2": area, "ciclos": n})
            anterior = n
        t_max = tempo(AREA_MAXIMA, m)
        refs.append({
            "modelo": m["id"],
            "rotulo": rotulo_do_modelo(m),
            "cobertura_m2": valor(m.get("cobertura_m2_declarada")),
            "autonomia_min": valor(m.get("autonomia_min_declarada")),
            "recarga_min": valor(m.get("recarga_min_declarada")),
            "retoma_apos_recarga": valor(m.get("retoma_apos_recarga")),
            "publica_multiciclo": t_max["multiciclo_valido"],
            "ciclos_em_400_m2": t_max["ciclos"],
            "saltos_de_ciclo": saltos,
        })

    # A conta que a especificacao pede inteira, e o que falta para ela fechar.
    com_cobertura = [m for m in publicaveis()
                     if valor(m.get("cobertura_m2_declarada")) is not None]
    com_recarga = [m for m in publicaveis()
                   if valor(m.get("recarga_min_declarada")) is not None]
    com_os_tres = [m for m in com_cobertura
                   if valor(m.get("recarga_min_declarada")) is not None
                   and valor(m.get("autonomia_min_declarada")) is not None]

    com_pa = [m for m in publicaveis() if valor(m.get("pa_declarado")) is not None]

    return {
        "faixas": faixas,
        "referencias": refs,
        "tempo_total": {
            "modelos_com_cobertura_declarada": [m["id"] for m in com_cobertura],
            "modelos_com_recarga_declarada": [m["id"] for m in com_recarga],
            "modelos_com_os_tres_numeros": [m["id"] for m in com_os_tres],
            "leitura": (
                "TEMPO REAL ATE TERMINAR = ciclos x autonomia + (ciclos-1) x recarga "
                "precisa de TRES numeros declarados, e nenhum modelo do banco tem os "
                "tres. Quem declara cobertura por carga (Electrolux) nao declara "
                "recarga; quem declara recarga (Xiaomi S20, Positivo PRA2000) nao "
                "declara cobertura. A R2 publica os ciclos e o tempo de limpeza "
                "somado, e diz que o total depende de um numero que o fabricante nao "
                "publica. Coletar recarga_min_declarada dos modelos Electrolux que ja "
                "declaram cobertura e o trabalho de MENOR custo e MAIOR retorno que "
                "esta varredura encontrou."
            ),
        },
        "contagem": {
            "modelos_publicaveis": len(publicaveis()),
            "com_pa_declarado": len(com_pa),
            "sem_pa_declarado": len(publicaveis()) - len(com_pa),
            "modelos_de_referencia": len(modelos_de_referencia()),
            "situacoes": len(PISOS) * len(PELOS),
            "situacoes_com_fonte_direta": sum(
                1 for f in faixas if not f.get("sem_fonte") and not f.get("por_ponte")),
            "situacoes_por_ponte": sum(1 for f in faixas if f.get("por_ponte")),
            "situacoes_no_portao": sum(1 for f in faixas if f.get("portao_3_itens") == "OK"),
            "modelos_esperando_link": sum(
                1 for m in publicaveis() if not (m.get("afiliado") or {}).get("url")),
        },
    }


# ------------------------------------------------- ORDEM DA TABELA DE EXEMPLOS
def ordem_dos_exemplos():
    """As linhas da tabela pre-renderizada, na ordem em que saem na tela.

    Metragem por fora, situacao por dentro, na ordem declarada dos vocabularios.
    A ordem e previsivel de proposito: aqui a coluna que muda dentro de uma
    metragem e o limiar de Pa, e a que muda entre metragens e o numero de ciclos
    — quem le a tabela de cima a baixo ve as duas variacoes separadas, em vez de
    misturadas.
    """
    linhas = []
    for area in METRAGENS_DA_TABELA:
        for piso in PISOS:
            for pelo in PELOS:
                if situacao(piso, pelo) is None:
                    continue
                linhas.append((area, piso, pelo))
    return linhas


def markdown_da_tabela(m_ref):
    linhas = ["| Metragem | Piso | Animal | Limiar seguro (quem) | Menor limiar citado (quem) | Modelos do banco que atendem | Ciclos no %s |"
              % (rotulo_do_modelo(m_ref) if m_ref else "modelo de referencia"),
              "|---|---|---|---|---|---|---|"]
    for area, piso, pelo in ordem_dos_exemplos():
        r = responder_r2(area, piso, pelo, m_ref["id"] if m_ref else None)
        sit = r["situacao"]
        ref = r["referencia"]
        if ref is None:
            ciclo_txt = "sem modelo de referencia"
        elif not ref["multiciclo_valido"]:
            ciclo_txt = "%d (nao publicado: retomada nao declarada)" % ref["ciclos"]
        else:
            ciclo_txt = "%d ciclo(s) · %s min de limpeza" % (
                ref["ciclos"], numero_br(ref["tempo_de_limpeza_min"]))
        linhas.append("| %s m2 | %s | %s | %s (%s)%s | %s (%s) | %d | %s |" % (
            numero_br(area), NOME_DO_PISO[piso], NOME_DO_PELO[pelo],
            escrever_limiar(sit["limiar_seguro"]), sit["limiar_seguro"]["publicador"],
            " — por ponte" if sit["por_ponte"] else "",
            escrever_limiar(sit["limiar_minimo"]), sit["limiar_minimo"]["publicador"],
            len(r["elegiveis"]), ciclo_txt,
        ))
    return "\n".join(linhas)


# ------------------------------------------------------------------ RELATORIO
def main():
    v = varrer()
    c = v["contagem"]
    m_ref = modelo_de_referencia_ancora()
    anc = situacao_ancora()

    print("Robometria — varredura da entrada da R2")
    print("")
    print("  modelos publicaveis ............. %d" % c["modelos_publicaveis"])
    print("  com Pa declarado ................ %d" % c["com_pa_declarado"])
    print("  sem Pa declarado ................ %d  <- nao entram em lista nenhuma" % c["sem_pa_declarado"])
    print("  modelos de referencia ........... %d  <- declaram cobertura por carga" % c["modelos_de_referencia"])
    print("  situacoes (piso x pelo) ......... %d" % c["situacoes"])
    print("    com fonte direta .............. %d" % c["situacoes_com_fonte_direta"])
    print("    por ponte ..................... %d" % c["situacoes_por_ponte"])
    print("    passam no portao de 3 itens ... %d" % c["situacoes_no_portao"])
    print("  esperando link de loja .......... %d  <- trabalho pendente (secao 7)"
          % c["modelos_esperando_link"])
    print("")

    print("  FAIXAS")
    for f in v["faixas"]:
        print("   %-12s %-28s limiar %5s  elegiveis %2d  %s%s" % (
            f["piso"], NOME_DO_PELO[f["pelo"]],
            numero_br(f.get("limiar_seguro", 0)), f["elegiveis"],
            f["portao_3_itens"], "  (por ponte)" if f.get("por_ponte") else ""))
    print("")

    print("  TEMPO TOTAL — o que falta para a formula fechar")
    print("   com cobertura declarada ....... %d" % len(v["tempo_total"]["modelos_com_cobertura_declarada"]))
    print("   com recarga declarada ......... %d" % len(v["tempo_total"]["modelos_com_recarga_declarada"]))
    print("   com os TRES numeros ........... %d" % len(v["tempo_total"]["modelos_com_os_tres_numeros"]))
    print("")

    if anc:
        r = responder_r2(area_ancora(m_ref), anc[0], anc[1],
                         m_ref["id"] if m_ref else None)
        print("  ANCORA: %s m2, %s, %s" % (numero_br(r["area"]), anc[0], anc[1]))
        print("   %s" % r["frase"])
        if r["referencia"]:
            print("   %s" % r["referencia"]["frase"])
        print("   elegiveis: %d | no limiar: %d" % (len(r["elegiveis"]), len(r["no_limiar"])))
        print("")

    if "--gravar" not in sys.argv:
        print("  (rode com --gravar para escrever dados/cobertura-r2.json e "
              "dados/tabela-exemplos-r2.md)")
        return 0

    doc = {
        "id": "cobertura-r2",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/cobertura-r2.py",
        "banco_gerado_em": doc_modelos["gerado_em"],
        "o_que_e": (
            "Varredura da entrada da R2 de ponta a ponta, exigida pela secao 14.3 do "
            "ARQUIPELAGO.md: as 9 situacoes de piso x pelo, e a metragem de %d a %d m2 "
            "contra cada modelo de referencia. O criterio nao e numero redondo de itens "
            "— e que nenhuma situacao que a ferramenta consegue produzir saia com menos "
            "de 3 elegiveis." % (AREA_MINIMA, AREA_MAXIMA)
        ),
        "nota_sobre_a_medicao_anterior": (
            "cobertura_de_faixa_r2, dentro de dados/modelos-robo.json, mediu a mesma "
            "faixa em 09/09/2026 e chegou a numeros MAIORES nas situacoes de pet. A "
            "diferenca nao e erro de nenhum dos dois: aquela varredura tratou o limiar "
            "da Canaltech como >=, e esta trata como >, porque a fonte escreve 'acima de "
            "4.000 Pa' e um modelo de exatamente 4.000 Pa nao esta acima de 4.000. Os "
            "modelos que ficam no valor exato nao somem — vao para um grupo proprio, "
            "rotulado. Esta varredura passa a ser a que a ferramenta consulta."
        ),
        "medido_em": doc_modelos["gerado_em"],
        "entrada": {
            "area_m2": {"minimo": AREA_MINIMA, "maximo": AREA_MAXIMA,
                        "passo_da_varredura": PASSO_DA_VARREDURA},
            "tipo_de_piso": PISOS,
            "pelo_de_pet": PELOS,
            "metragens_do_corpus": [{"m2": a, "onde": o} for a, o in METRAGENS_DO_CORPUS],
        },
        "ancora": {
            "situacao": {"piso": anc[0], "pelo": anc[1]} if anc else None,
            "area_m2": area_ancora(m_ref),
            "modelo_de_referencia": m_ref["id"] if m_ref else None,
        },
        "regras_de_limiar": [
            {"constante": r["constante"], "papel": r["papel"],
             "comparacao": r["comparacao"], "pisos": r["pisos"], "pelos": r["pelos"],
             "palavras_da_fonte": r["palavras_da_fonte"]}
            for r in REGRAS_DE_LIMIAR
        ],
        "situacoes_sem_fonte_direta": [
            {"piso": p, "pelo": q} for p, q in SITUACOES_SEM_FONTE_DIRETA
        ],
    }
    doc.update(v)

    with open(os.path.join(DADOS, "cobertura-r2.json"), "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("  gravado: dados/cobertura-r2.json")

    with open(os.path.join(DADOS, "tabela-exemplos-r2.md"), "w", encoding="utf-8") as fh:
        fh.write("---\n")
        fh.write("titulo: Tabela de exemplos pre-renderizada da R2\n")
        fh.write("gerado_por: ferramentas/cobertura-r2.py\n")
        fh.write("publicar: false\n")
        fh.write("---\n\n")
        fh.write("# Tabela de exemplos da R2\n\n")
        fh.write("GERADA, nunca digitada (secao 1.7 da especificacao, que vale para as\n")
        fh.write("duas ferramentas): tabela digitada a mao discorda do banco em silencio\n")
        fh.write("no dia em que o banco muda. O Bloco 4 serve estas linhas em HTML.\n\n")
        fh.write(markdown_da_tabela(m_ref))
        fh.write("\n")
    print("  gravado: dados/tabela-exemplos-r2.md (%d linhas)" % len(ordem_dos_exemplos()))

    return 0


if __name__ == "__main__":
    sys.exit(main())

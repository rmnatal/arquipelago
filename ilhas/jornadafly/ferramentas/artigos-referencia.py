#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Os ARTIGOS-ANCORA desta ilha (bloco 5), como REGRA e nao como texto digitado.

    python3 ferramentas/artigos-referencia.py            # relatorio na tela
    python3 ferramentas/artigos-referencia.py <id>       # um artigo inteiro

POR QUE ESTE ARQUIVO EXISTE, e por que o artigo nao e um .md escrito a mao. O
produto desta ilha e preco colhido na fonte de quem opera COM A DATA DA LEITURA.
Artigo escrito a mao carrega numero digitado, e numero digitado envelhece calado:
no dia em que o banco for recarregado, a ferramenta publica o preco novo e o
artigo continua publicando o velho, com a mesma cara de verdade. Entao aqui o
artigo e MONTADO a partir do banco e das tres referencias -- cada frase de preco
sai de `f1-referencia.py`, nao daqui -- e o que este arquivo guarda e o que
NENHUMA ferramenta sabe: qual consulta o artigo ataca, quem ocupa a SERP dela,
qual e a mae na arvore, quais sao as irmas e para onde vai o link de compra.

O MESMO DESENHO DA F1, DA F2 E DA F3: a regra mora aqui, o arquivo gravado sai de
`gerar-artigos.py`, e o PHP -- quando a casca nascer -- e tradutor desta regra,
frase a frase, nunca uma segunda regra.

NADA DESTE ARQUIVO ESTA NO AR. Esta ilha nao tem WordPress, nao tem Sync e nao
tem /status, e o dominio nao esta na lista de Dominios permitidos deste ambiente.
`publicar` sai `false` em todo artigo, com o motivo escrito dentro dele.

AS FRASES DE TELA SAEM ACENTUADAS. E a cicatriz da Robometria, que publicou
portugues sem acento, e a regra ja esta escrita no banco e nas tres referencias.
"""

import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)

PESSOAS_DA_TABELA = (1, 2, 4, 6)   # especificacao 2.8: o 6 e obrigatorio
NIVEL_1 = {"nome": "Guias", "url": "/guias/"}
NIVEL_2 = {"nome": "Quanto custa", "url": "/guias/quanto-custa/"}


class ArtigoReprovado(Exception):
    """Defeito no artigo. A mensagem nomeia o artigo, a regra e o que ela viu."""


class VozIlegivel(Exception):
    """O VOZ.md nao entregou a lista de frases proibidas."""


# ---------------------------------------------------------------------------
# AS REFERENCIAS, CARREGADAS PELO CAMINHO
# ---------------------------------------------------------------------------

def _referencia(nome):
    """Carrega uma referencia PELO CAMINHO, nunca uma copia.

    O nome tem hifen (convencao das ilhas) e por isso nao e importavel por
    `import`. Carregar pelo caminho e o que garante que o artigo sai da MESMA
    regra que a bancada mede -- se a F1 mudar de resposta, o artigo muda com ela
    na mesma passada, e nao no dia em que alguem se lembrar.
    """
    caminho = os.path.join(AQUI, "%s-referencia.py" % nome)
    spec = importlib.util.spec_from_file_location(nome.replace("-", "_"), caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def carregar_f1():
    return _referencia("f1")


# ---------------------------------------------------------------------------
# A VOZ, LIDA DO VOZ.md E NAO DIGITADA AQUI
# ---------------------------------------------------------------------------

def frases_proibidas(caminho=None):
    """As frases que o VOZ.md proibe, VARRIDAS do VOZ.md.

    Esta funcao e a licao de 22/10/2026 aplicada um andar acima. Naquele dia o
    `validar-banco.py` desta pasta foi pego conferindo o vocabulario contra SETE
    nomes digitados quando o esquema tinha NOVE -- dois nunca foram conferidos
    por ninguem, em silencio, por mais de um mes. Lista digitada que repete uma
    fonte e sempre a fonte menos a parte que alguem esqueceu de copiar.

    Entao a lista nao mora aqui: mora no `VOZ.md`, que e quem manda no tom
    (secao 15 do ARQUIPELAGO.md), e esta funcao a LE. Se a secao sumir ou
    encolher, ela ESTOURA em vez de aprovar com a lista curta.
    """
    caminho = caminho or os.path.join(BASE, "VOZ.md")
    with io.open(caminho, encoding="utf-8") as f:
        texto = f.read()

    partes = re.split(r"(?m)^##\s+Proibidas\s*$", texto)
    if len(partes) != 2:
        raise VozIlegivel(
            "VOZ.md sem a secao `## Proibidas` (achei %d marcas, esperava 1). "
            "Ela e quem diz o que nao pode ir para a tela; sem ela este portao "
            "aprovaria qualquer frase." % (len(partes) - 1))
    corpo = re.split(r"(?m)^##\s+", partes[1])[0]

    frases = [f.strip() for f in re.findall(r'"([^"]+)"', corpo)]
    frases = [f for f in frases if len(f) >= 4]
    if len(frases) < 8:
        raise VozIlegivel(
            "a secao `## Proibidas` do VOZ.md entregou so %d frases entre aspas. "
            "Em 23/10/2026 ela tinha 12. Menos que isso e a secao encolhendo sem "
            "ninguem ver, e nao uma voz que ficou mais permissiva." % len(frases))
    return frases


# Copiada da secao 32.4 do ARQUIPELAGO.md em 23/10/2026, com a data porque copia
# tem dono e tem dia. O que a 32.4 proibe e TEXTO DE BASTIDOR DA FABRICA na
# pagina publica: frase sobre como a fabrica trabalha, nome de secao do contrato
# e nome de rotina. As cinco literais sao as que ela nomeia; o resto e cobrado
# pela regra de forma logo abaixo, que nao depende de ninguem copiar nada.
BASTIDOR_LITERAL = (
    "egresso da nuvem", "SERP classificada", "snippet",
    "lista de reconferência da ilha", "busca restrita ao domínio",
)
# Nome de rotina e de camada da fabrica. Nenhum deles e palavra de leitor.
BASTIDOR_NOMES = (
    "Fundação", "Sentinela", "Bússola", "Arquipélago", "arquipélago",
    "despacho", "bancada", "portão", "desembarque", "Pente Fino",
)
# Referencia a secao de contrato, em qualquer das formas que a fabrica escreve.
BASTIDOR_FORMA = (
    re.compile(r"(?i)\bse[cç][aã]o\s+\d"),
    re.compile(r"(?i)\bbloco\s+\d"),
    re.compile(r"ARQUIPELAGO\.md|VOZ\.md|ESTADO\.md|PROMPT\.md|REGISTRO\.md"),
)


# ---------------------------------------------------------------------------
# O MAPA: o que NENHUMA ferramenta sabe
# ---------------------------------------------------------------------------
#
# A ordem desta lista e a ordem do mapa da secao 16.9(a), e e ela que faz a
# janela de irmas ROTACIONAR. Quem inserir um artigo no meio muda as irmas de
# todos -- e isso e desejado: o grafo continua circulante e o grau de ENTRADA de
# toda pagina continua igual ao de saida, com quatro filhas ou com quarenta.
#
# DOIS CAMPOS PARA A MESMA CONSULTA, e a diferenca entre eles e uma regra. O
# `consulta_alvo` e a consulta como ela foi MEDIDA, do jeito que a pessoa digita
# -- e gente digita sem acento. O `titulo_na_tela` e a mesma pergunta em
# portugues correto, e e ele que vai para o <title>, o H1, a trilha e a ancora
# das irmas. Publicar a consulta crua na tela seria publicar portugues sem
# acento, que e a cicatriz da Robometria; esconder a consulta crua seria perder
# a correspondencia exata que faz a pagina ser achada. Os dois existem porque
# cada um serve um leitor diferente.
#
# `serp_medida` nao e opiniao: cada linha e o que o corpus do bloco 1 registrou
# em 14 e 15/09/2026, com os dominios nomeados. E o que sustenta o item (b) do
# portao de tema da secao 17.2.

MAPA = [
    {
        "id": "gondola-veneza",
        "titulo_na_tela": "Quanto custa o passeio de gôndola em Veneza",
        "slug": "passeio-de-gondola-em-veneza",
        "experiencia": "veneza-passeio-de-gondola",
        "consulta_alvo": "quanto custa passeio de gôndola em veneza",
        "consultas_irmas": [
            "passeio de gôndola veneza preço",
            "vale a pena o passeio de gôndola em veneza",
            "o preço da gôndola é por pessoa",
        ],
        "serp_medida": {
            "data": "2026-09-14",
            "ocupantes": [
                "turismo.eurodicas.com.br", "maladeaventuras.com",
                "viajandoparaitalia.com.br", "queroviajarmais.com",
                "dicasdaitalia.com.br", "viveromundo.org", "lavidaesmara.com",
            ],
            "o_que_falta_no_ar": (
                "quatro dos sete publicam números que se contradizem sobre uma "
                "tarifa fixada por deliberação da prefeitura, e nenhum dos sete "
                "diz em que dia leu o preço"),
        },
        "momento": "fim",
        "promessa": (
            "O que você coloca: quantas pessoas vão na gôndola. O que sai: o "
            "preço do passeio para o grupo inteiro, com a data em que lemos a "
            "tarifa."),
        "perguntas": [
            ("O preço do passeio de gôndola é por pessoa ou pela gôndola?", "caixa"),
            ("O que está incluso no passeio?", "inclui"),
            ("Quanto custa cada versão vendida pelo operador?", "prestacao"),
        ],
    },
    {
        "id": "torre-eiffel",
        "titulo_na_tela": "Quanto custa subir na Torre Eiffel",
        "slug": "subir-na-torre-eiffel",
        "experiencia": "paris-torre-eiffel",
        "consulta_alvo": "quanto custa subir na torre eiffel",
        "consultas_irmas": [
            "quanto custa entrada torre eiffel",
            "ingresso torre eiffel preço",
            "vale a pena subir na torre eiffel",
        ],
        "serp_medida": {
            "data": "2026-09-14",
            "ocupantes": [
                "toureiffel.paris", "maladeaventuras.com", "queroviajarmais.com",
                "dicaparis.com", "encantosdeparis.com.br",
            ],
            "o_que_falta_no_ar": (
                "o operador do monumento publica a tabela dos quatro bilhetes e "
                "não fecha a conta do grupo; os outros quatro fecham a conta de "
                "um bilhete só e não dizem em que dia leram o preço"),
        },
        "momento": "fim",
        "promessa": (
            "O que você coloca: qual dos quatro bilhetes e quantas pessoas. O "
            "que sai: o total do grupo, o valor por pessoa e o que cada bilhete "
            "dá, com a data da leitura."),
        "perguntas": [
            ("Quanto custa o bilhete mais barato para subir na Torre Eiffel?", "caixa"),
            ("Quanto custa cada um dos quatro bilhetes?", "prestacao"),
            ("O que está incluso no bilhete?", "inclui"),
            ("Criança paga para subir na Torre Eiffel?", "faixa_etaria"),
        ],
    },
    {
        "id": "coliseu-roma",
        "titulo_na_tela": "Quanto custa o ingresso do Coliseu de Roma",
        "slug": "ingresso-do-coliseu-de-roma",
        "experiencia": "roma-coliseu-ingresso",
        "consulta_alvo": "quanto custa ingresso coliseu roma",
        "consultas_irmas": [
            "ingresso coliseu preço",
            "quanto custa entrar no coliseu",
            "vale a pena a experiência completa do coliseu",
        ],
        "serp_medida": {
            "data": "2026-09-14",
            "ocupantes": [
                "eurodicas.com.br", "maladeaventuras.com", "viajaquepassa.com.br",
                "grupodicas.com", "thebettervacation.com",
            ],
            "o_que_falta_no_ar": (
                "os cinco publicam o preço do ingresso comum e nenhum separa, "
                "com os dois números lado a lado, o que a versão mais cara dá a "
                "mais — nem diz em que dia leu cada um"),
        },
        "momento": "fim",
        "promessa": (
            "O que você coloca: qual ingresso e quantas pessoas. O que sai: o "
            "total do grupo e o que a versão mais cara dá a mais, com a data da "
            "leitura."),
        "perguntas": [
            ("Quanto custa o ingresso comum do Coliseu?", "caixa"),
            ("Quanto custa cada versão do ingresso, uma por uma?", "prestacao"),
            ("O que está incluso no ingresso?", "inclui"),
        ],
    },
    {
        "id": "angkor-pass",
        "titulo_na_tela": "Angkor Pass: quantos dias valem a pena",
        "slug": "angkor-pass-de-1-3-ou-7-dias",
        "experiencia": "siem-reap-angkor-pass",
        "consulta_alvo": "angkor pass quantos dias valem a pena",
        "consultas_irmas": [
            "quanto custa o angkor pass",
            "angkor pass 1 dia ou 3 dias",
            "ingresso angkor wat preço",
        ],
        "serp_medida": {
            "data": "2026-09-14",
            "ocupantes": [],
            "o_que_falta_no_ar": (
                "esta consulta não foi medida no levantamento de 14/09/2026 — o "
                "corpus mediu o julgamento de passe em Roma e em Lisboa, não em "
                "Angkor. A página nasce, então, sem a leitura de quem ocupa as "
                "dez primeiras: é o que há, e inventar a leitura seria pior"),
        },
        "momento": "fim",
        "promessa": (
            "O que você coloca: quantos dias você vai visitar o parque e quantas "
            "pessoas vão. O que sai: a partir de quantos dias o ingresso mais "
            "longo passa a custar menos que comprar o de um dia de novo."),
        "perguntas": [
            ("Quanto custa o Angkor Pass de 1 dia?", "caixa"),
            ("A partir de quantos dias de visita o passe mais longo paga?", "escada"),
            ("Quanto custa cada passe vendido pelo operador?", "prestacao"),
            ("Criança paga o Angkor Pass?", "faixa_etaria"),
        ],
    },
]

MAPA_POR_ID = {a["id"]: a for a in MAPA}


# ---------------------------------------------------------------------------
# OS ARTIGOS QUE NAO FORAM ESCRITOS, E O QUE DESTRAVA CADA UM
# ---------------------------------------------------------------------------
#
# A secao 18.3 do ARQUIPELAGO.md manda, quando um item nao couber, resolver os
# que couberem e deixar escrito o que falta COM O MOTIVO. O bloco 5 pede artigo
# pareado com CADA ferramenta, e dois nao foram escritos -- nao por tempo, e sim
# porque a ferramenta pareada nao tem resposta para publicar. Artigo cujo titulo
# promete um numero que a pagina nao entrega e exatamente o defeito que o corpus
# do bloco 1 mediu nos concorrentes.

def pre_registrados(banco=None):
    f1 = carregar_f1()
    banco = banco if banco is not None else f1.carregar_banco()
    faixas = len(banco.get("faixas_diarias") or [])
    coberturas = len(banco.get("coberturas_de_passe") or [])
    passes = sum(1 for e in (banco.get("experiencias") or [])
                 if e.get("categoria") == "passe_de_cidade")
    roma = sum(1 for e in (banco.get("experiencias") or [])
               if e.get("cidade") == "roma")

    return [
        {
            "ferramenta_pareada": "F2",
            "consulta_alvo": "quanto custa um dia em veneza para 2 pessoas",
            "por_que_a_SERP_vale": (
                "medida em 14/09/2026: oito ocupantes e NENHUM responde «para 2 "
                "pessoas». Todos respondem «viajar para Veneza» genérico."),
            "nao_foi_escrito_porque": (
                "a F2 soma quatro linhas — experiências, hospedagem, alimentação "
                "e transporte local — e hoje publica UMA. As faixas de diária "
                "contadas no banco são %d: a entidade existe desde 22/10/2026 e "
                "o dado não. Um artigo com este título e só a linha de "
                "experiências prometeria o dia inteiro e entregaria o passeio, "
                "que é o defeito medido nos oito ocupantes." % faixas),
            "destrava_quando": (
                "houver ao menos uma faixa de diária para Veneza em cada uma das "
                "três naturezas (hospedagem, alimentação e transporte local), "
                "cada uma com quem publicou nomeado, URL e data de leitura — os "
                "três obrigatórios do esquema. A coleta é de navegador: "
                "numbeo.com, booking.com e civitatis.com.br foram recusados no "
                "egresso deste ambiente em 22/10/2026 e remedidos em 000 em "
                "23/10/2026."),
            "o_que_ja_esta_pronto": (
                "a regra inteira. A F2 serve 3.077 estados e a tabela "
                "pré-renderizada tem 144 linhas; o artigo é montagem, não "
                "pesquisa, no dia em que o dado entrar."),
        },
        {
            "ferramenta_pareada": "F3",
            "consulta_alvo": "roma pass vale a pena",
            "por_que_a_SERP_vale": (
                "medida em 14/09/2026: o primeiro colocado promete «fiz as "
                "contas pra você» no próprio título, e o terceiro é um blog que "
                "virou operador e vende o próprio tour. O que nenhum publica é "
                "DE QUANTAS atrações aquele número saiu."),
            "nao_foi_escrito_porque": (
                "passes contados no banco: %d. Coberturas de passe contadas: %d. "
                "A F3 responde «a soma dos avulsos» e fecha com «sem passe "
                "lido» em todos os estados válidos, então o veredito que o "
                "título promete não existe. E falta a outra metade: Roma tem %d "
                "experiência no banco, e um julgamento de passe sobre uma "
                "atração só não é um julgamento de passe."
                % (passes, coberturas, roma)),
            "destrava_quando": (
                "houver o Roma Pass no banco, com preço e data de leitura "
                "próprios, MAIS a cobertura par por par entre ele e cada "
                "atração de Roma, cada par com fonte e data de leitura próprias "
                "— porque o preço do passe pode estar certo e a cobertura errada "
                "no mesmo dia. A coleta é de navegador: romapass.it, "
                "turismoroma.it, lisboacard.org, visitlisboa.com e "
                "civitatis.com.br foram recusados no egresso em 22/10/2026 e "
                "jornadafly.com.br segue recusado em 23/10/2026."),
            "o_que_ja_esta_pronto": (
                "a regra inteira, com as três honestidades que o julgamento "
                "exige: não lida não é coberta, o equilíbrio é sobre o que foi "
                "lido, e «até 50%» não é 50%."),
        },
    ]


# ---------------------------------------------------------------------------
# A MONTAGEM DE UM ARTIGO
# ---------------------------------------------------------------------------

def _versoes(experiencia):
    return [v for v in (experiencia.get("versoes") or []) if v.get("preco") is not None]


def _respostas_da_tabela(f1, experiencia, banco, esquema, constantes):
    """A grade do artigo: cada versao x 1, 2, 4 e 6 pessoas.

    Sai da F1, resposta por resposta. O 6 esta na grade porque e onde o degrau
    de capacidade aparece -- uma grade que para em 4 esconde exatamente o que
    esta ilha tem de diferente, e isso ja estava escrito na especificacao 2.8.
    """
    linhas = []
    for v in _versoes(experiencia):
        for n in PESSOAS_DA_TABELA:
            r = f1.responder(experiencia["id"], v["id"], n,
                             banco=banco, esquema=esquema, constantes=constantes)
            if r["recusa_dura"] is not None:
                raise ArtigoReprovado(
                    "a grade do artigo caiu numa recusa dura em %s/%s para %d "
                    "pessoas: %s. A grade tem de ser toda de estados que a "
                    "ferramenta responde."
                    % (experiencia["id"], v["id"], n, r["recusa_dura"]["codigo"]))
            linhas.append({
                "versao": v["id"],
                "rotulo": v["rotulo"],
                "pessoas": n,
                "total": r["contas"]["total_escrito"],
                "por_pessoa": r["contas"]["por_pessoa_escrito"],
                "unidade_de_preco": r["contas"]["unidade_de_preco"],
                "unidades_necessarias": r["contas"]["unidades_necessarias"],
                "com_iof": r["contas"]["total_com_iof_escrito"],
                "lido_em": f1.data_em_portugues(r["contas"]["data_leitura"]),
            })
    return linhas


def _monte_o_que_a_resposta_pede(f1, mapa, experiencia, cidade, compra, respostas):
    """O bloco da secao 32.2: 2 a 4 itens, cada um com os DOIS botoes.

    «Calcular» leva a ferramenta desta ilha com o parametro da pagina ja na URL;
    «Ver produtos» leva ao bloco de compra. Um item por versao vendida pelo
    operador -- e o item e sempre EQUIPAMENTO ou BILHETE, nunca o item vivo: a
    32.2 proibe link de compra em item vivo, e nenhuma das quatro experiencias
    desta pasta e um ser vivo, o que fica dito em vez de suposto.
    """
    itens = []
    for v in _versoes(experiencia):
        r = respostas[v["id"]]
        itens.append({
            "rotulo": v["rotulo"],
            "o_que_e": r["frase_resposta"],
            "calcular": {
                "texto": "Calcular para o meu grupo",
                "url": "/calculadoras/quanto-custa-a-experiencia/?experiencia=%s&versao=%s"
                       % (experiencia["id"], v["id"]),
                "o_que_leva": "experiência e versão desta página, já preenchidas",
            },
            "ver_produtos": {
                "texto": "Ver na plataforma",
                "url": compra["url"],
                "rel": compra["rel"],
                "o_que_e": compra["o_que_e"],
                "aviso": compra["aviso"],
            },
        })
    if not 2 <= len(itens) <= 4:
        raise ArtigoReprovado(
            "o bloco «Monte / Compre o que esta resposta pede» saiu com %d itens "
            "em %s, e a regra do molde pede de 2 a 4." % (len(itens), mapa["id"]))
    return itens


def irmas_de(indice, mapa=None):
    """A janela ROTACIONA (secao 16.9(a)).

    Cada pagina leva as ate-quatro irmas que vem DEPOIS dela na ordem do mapa,
    dando a volta no fim. Janela fixa deixa a quinta e a sexta filha sem link de
    irma nenhuma, e o grau de entrada de uma pagina nao aparece em leitura de
    HTTP: ela responde 200 com um link de entrada so.
    """
    mapa = mapa if mapa is not None else MAPA
    quantas = min(4, len(mapa) - 1)
    return [mapa[(indice + 1 + k) % len(mapa)] for k in range(quantas)]


def artigo(artigo_id, banco=None, esquema=None, constantes=None, f1=None):
    """Um artigo-ancora inteiro, montado do banco. Nenhum numero digitado aqui."""
    f1 = f1 or carregar_f1()
    banco = banco if banco is not None else f1.carregar_banco()
    esquema = esquema if esquema is not None else f1.carregar_esquema()
    constantes = constantes if constantes is not None else f1.carregar_constantes()

    if artigo_id not in MAPA_POR_ID:
        raise ArtigoReprovado("não existe artigo %r no mapa." % artigo_id)
    mapa = MAPA_POR_ID[artigo_id]
    indice = [a["id"] for a in MAPA].index(artigo_id)

    cidades, fontes, experiencias = f1.indexar(banco)
    experiencia = experiencias.get(mapa["experiencia"])
    if experiencia is None:
        raise ArtigoReprovado(
            "o artigo %s aponta para a experiência %r, que não está no banco."
            % (artigo_id, mapa["experiencia"]))
    cidade = cidades.get(experiencia.get("cidade")) or {}

    versoes = _versoes(experiencia)
    if not versoes:
        raise ArtigoReprovado(
            "a experiência %r não tem versão com preço: não há resposta para o "
            "artigo publicar." % experiencia["id"])

    # A resposta de referencia do artigo e a de UMA pessoa na versao mais barata:
    # e o numero que a pessoa busca quando digita a consulta crua, sem parametro.
    base = min(versoes, key=lambda v: v["preco"])
    respostas = {}
    for v in versoes:
        respostas[v["id"]] = f1.responder(
            experiencia["id"], v["id"], 1,
            banco=banco, esquema=esquema, constantes=constantes)
    r_base = respostas[base["id"]]

    compra = f1.bloco_de_compra(esquema, experiencia, cidade)
    tabela = _respostas_da_tabela(f1, experiencia, banco, esquema, constantes)
    pendente = experiencia.get("status") == "pendente_de_releitura"

    # A CAIXA DE RESPOSTA (molde 32.2: no topo, o numero e a condicao numa frase).
    caixa = {
        "frase": r_base["frase_resposta"],
        "cartao_brasileiro": r_base["cartao_brasileiro"],
        "promessa": mapa["promessa"],
    }
    if pendente:
        caixa["reconferir"] = next(
            (rec["frase"] for rec in r_base["recusas"]
             if rec["codigo"] == "registro_pendente_de_releitura"), None)
        if not caixa["reconferir"]:
            raise ArtigoReprovado(
                "%s: a experiência está `pendente_de_releitura` e a F1 não "
                "devolveu a frase que diz isso ao leitor. Publicar o preço sem "
                "ela seria cravá-lo como atual." % artigo_id)

    # AS DOBRAS (molde 32.2: o resto do texto recolhivel, e nada sai do HTML).
    dobras = []
    corpo_mae = (
        "Esta página é uma das respostas de preço da JornadaFly: todas elas "
        "estão em %s, e cada uma traz a data em que lemos o preço."
        % NIVEL_2["url"])
    dobras.append({
        "titulo": "Como chegamos nesse número",
        "paragrafos": [
            caixa["frase"],
            r_base["cartao_brasileiro"],
            corpo_mae,
            "Para outro tamanho de grupo, a conta fechada está na calculadora: "
            "/calculadoras/quanto-custa-a-experiencia/",
        ],
    })

    # A DOBRA DO «INCLUSO» NASCE SEMPRE, inclusive quando o operador nao declara
    # nada -- e nesse caso ela diz isso, com essas palavras. A F1 devolve a frase
    # da recusa junto com a da lista, e foi deliberado: «o operador nao declara o
    # que esta incluso» e resposta, e e a resposta que os ocupantes da SERP nao
    # dao. Pagina que simplesmente OMITE a secao deixa quem pergunta sem saber se
    # ninguem perguntou ou se a resposta nao existe.
    dobras.append({
        "titulo": "O que está incluso e o que não está",
        "paragrafos": [p for p in (r_base["inclui"]["frase"],
                                   r_base["nao_inclui"]["frase"]) if p],
    })

    escada = r_base["escada"]
    if escada["aplicavel"]:
        dobras.append({
            "titulo": "A partir de quando a versão mais longa paga",
            "paragrafos": [l["frase"] for l in escada["linhas"]],
        })
    elif escada["motivo"]:
        dobras.append({
            "titulo": "Por que as versões não se comparam por quantidade",
            "paragrafos": [escada["motivo"]],
        })

    faixa = r_base["faixa_etaria"]
    if faixa["tem_faixa"] and faixa["frases"]:
        dobras.append({"titulo": "Crianças e jovens",
                       "paragrafos": list(faixa["frases"])})

    dobras.append({
        "titulo": "Cada versão vendida pelo operador, uma por uma",
        "paragrafos": [l["frase"] for l in r_base["prestacao_de_contas"]["linhas"]],
    })

    if r_base["recusas"]:
        dobras.append({
            "titulo": "O que esta página não responde",
            "paragrafos": [rec["frase"] for rec in r_base["recusas"]],
        })

    # COMO SABEMOS (a camada de prova: fonte nomeada + data).
    cs = r_base["como_sabemos"]
    prova = ["Operador: %s." % cs["operador"]]
    if cs.get("url_operador"):
        prova.append("Endereço do operador: %s" % cs["url_operador"])
    if cs.get("documento"):
        prova.append("Documento: %s." % cs["documento"])
    prova.append("Preço lido em %s, por %s."
                 % (f1.data_em_portugues(cs["data_leitura"]),
                    "leitura na fonte de quem opera"))
    if cs.get("declarado_como"):
        prova.append("O que a fonte diz, na palavra dela: %s" % cs["declarado_como"])
    # AS DIVERGENCIAS SAO O DIFERENCIAL DESTA ILHA, nao um rodape: quatro dos
    # sete ocupantes da SERP da gondola publicam numeros que se contradizem sobre
    # uma tarifa de ato oficial, e nenhum diz quando leu. Dizer QUEM publicou O
    # QUE, com a data, e a unica coisa que nenhum deles faz -- e e por isso que a
    # frase de divergencia carrega um valor que NAO e o nosso. O portao deixa
    # esse valor passar so dentro de uma frase que nomeia quem o publicou.
    divergencias = []
    for d in (cs.get("divergentes") or []):
        if not isinstance(d, dict) or not d.get("frase") or not d.get("publicador"):
            raise ArtigoReprovado(
                "%s: divergência sem publicador nomeado ou sem frase: %r. "
                "Declaração sem publicador nomeado não vai para a tela."
                % (artigo_id, d))
        divergencias.append(d)
        prova.append(d["frase"])
    dobras.append({"titulo": "Como sabemos", "paragrafos": prova})

    # FAQ: so entra pergunta que a propria pagina responde, E a resposta e a
    # frase que responde AQUELA pergunta.
    #
    # A primeira versao disto emparelhava a pergunta declarada do artigo com a
    # frase da caixa de resposta, qualquer que fosse a pergunta -- e publicava,
    # em tres dos quatro artigos, um par que nao se fecha: «A partir de quantos
    # dias de visita o Angkor Pass de 3 dias paga?» respondido por «o de 1 dia
    # custa US$ 37». Cada pergunta diz agora DE ONDE sai a resposta dela, e o
    # portao reprova pergunta cuja fonte nao existe nesta experiencia em vez de
    # deixa-la cair fora em silencio.
    fontes_de_resposta = {
        "caixa": caixa["frase"],
        "inclui": r_base["inclui"]["frase"],
        "nao_inclui": r_base["nao_inclui"]["frase"],
        "escada": (" ".join(l["frase"] for l in escada["linhas"])
                   if escada["aplicavel"] and escada["linhas"] else None),
        "prestacao": " ".join(l["frase"]
                              for l in r_base["prestacao_de_contas"]["linhas"]),
        "faixa_etaria": (" ".join(faixa["frases"])
                         if faixa["tem_faixa"] and faixa["frases"] else None),
    }
    faq = []
    for pergunta, de_onde in mapa["perguntas"]:
        if de_onde not in fontes_de_resposta:
            raise ArtigoReprovado(
                "%s: a pergunta «%s» diz sair de %r, que não é fonte de resposta."
                % (artigo_id, pergunta, de_onde))
        resposta = fontes_de_resposta[de_onde]
        if not resposta:
            raise ArtigoReprovado(
                "%s: a pergunta «%s» sai de %r e esta experiência não tem essa "
                "frase. Pergunta sem resposta não entra no FAQ, e deixá-la cair "
                "fora em silêncio esconde um mapa errado."
                % (artigo_id, pergunta, de_onde))
        faq.append({"pergunta": pergunta, "resposta": resposta,
                    "resposta_sai_de": de_onde})

    titulo = "%s — preço com a data da leitura" % _titulo_da_consulta(mapa)
    url = NIVEL_2["url"] + mapa["slug"] + "/"
    irmas = irmas_de(indice)

    doc = {
        "id": artigo_id,
        "publicar": False,
        "motivo_publicar_false": (
            "Esta ilha não tem WordPress, não tem Sync e não tem /status, e o "
            "domínio não está na lista de Domínios permitidos deste ambiente "
            "(remedido em 23/10/2026: 000 em quatro medições, com aquametria e "
            "robometria em 200 nas quatro de controle). Não existe «no ar» para "
            "onde publicar, e dizer que publiquei seria inventar."),
        "ferramenta_pareada": "F1",
        "experiencia": experiencia["id"],
        "cidade": cidade.get("nome"),
        "pais": cidade.get("pais"),
        "consulta_alvo": mapa["consulta_alvo"],
        "consultas_irmas": list(mapa["consultas_irmas"]),
        "serp_medida": mapa["serp_medida"],
        "momento": mapa["momento"],
        "link_do_momento": "experiência",
        "titulo": titulo,
        "h1": _titulo_da_consulta(mapa),
        "description": _description(mapa, r_base, pendente),
        "url_planejada": url,
        "mae_planejada": NIVEL_2["url"],
        "nivel": 3,
        "trilha": [
            {"nome": "Início", "url": "/"},
            {"nome": NIVEL_1["nome"], "url": NIVEL_1["url"]},
            {"nome": NIVEL_2["nome"], "url": NIVEL_2["url"]},
            {"nome": _titulo_da_consulta(mapa), "url": None},
        ],
        "caixa_de_resposta": caixa,
        "monte_o_que_a_resposta_pede": _monte_o_que_a_resposta_pede(
            f1, mapa, experiencia, cidade, compra, respostas),
        "tabela_resumo": tabela,
        "tabela_recolhida": False,
        "dobras": dobras,
        "ferramenta_no_corpo": "/calculadoras/quanto-custa-a-experiencia/",
        "mae_no_corpo": corpo_mae,
        "veja_tambem": [
            {"ancora": i["titulo_na_tela"],
             "url": NIVEL_2["url"] + i["slug"] + "/"} for i in irmas],
        "faq": faq,
        "bloco_de_compra": compra,
        "status_do_registro": experiencia.get("status"),
        "divergencias": divergencias,
    }
    doc["json_ld"] = _json_ld(doc)
    return doc


def _titulo_da_consulta(mapa):
    """O H1 e a pergunta da pessoa em portugues correto, nunca uma frase nova.

    A secao 17.4 manda o titulo ser a consulta ou a resposta dela. Reescrever a
    consulta em «linguagem de marca» e como se perde a correspondencia exata que
    faz a pagina ser achada -- entao o que muda da consulta medida para aqui e
    so a acentuacao e a maiuscula de nome proprio, e o portao abaixo cobra que
    seja so isso.
    """
    titulo = mapa["titulo_na_tela"]
    palavras_do_titulo = _palavras(titulo)
    faltando = [p for p in _palavras(mapa["consulta_alvo"])
                if p not in palavras_do_titulo]
    if faltando:
        raise ArtigoReprovado(
            "o título na tela de %s perdeu palavra da consulta-alvo: %r. Palavra "
            "que sai do título é correspondência que a página deixa de ter."
            % (mapa["id"], faltando))
    extras = [p for p in palavras_do_titulo
              if p not in _palavras(mapa["consulta_alvo"])
              and p not in PALAVRAS_DE_LIGACAO]
    if extras:
        raise ArtigoReprovado(
            "o título na tela de %s ganhou palavra que não é de ligação: %r. O "
            "título acentua e capitaliza a pergunta da pessoa; não a reescreve."
            % (mapa["id"], extras))
    return titulo


def _description(mapa, r_base, pendente):
    """A description cita a resposta, e NUNCA cita preco de registro pendente.

    O preco de um registro `pendente_de_releitura` vai para a tela com a ressalva
    ao lado, porque a tela tem espaco para a ressalva. A description nao tem: ela
    e lida fora de contexto, no resultado de busca, e ali o numero apareceria
    sozinho, cravado como atual. E o defeito mais grave possivel nesta ilha.
    """
    if pendente:
        return ("%s Trazemos o preço de cada versão vendida pelo operador, a "
                "data em que lemos cada um e a conta fechada para o tamanho do "
                "seu grupo." % mapa["promessa"])
    return "%s %s" % (r_base["frase_resposta"], mapa["promessa"])


def _json_ld(doc):
    blocos = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": doc["h1"],
            "description": doc["description"],
            "about": doc["consulta_alvo"],
            "isPartOf": doc["mae_planejada"],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n["nome"],
                 "item": n["url"]}
                for i, n in enumerate(doc["trilha"]) if n["url"]
            ],
        },
    ]
    if doc["faq"]:
        blocos.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q["pergunta"],
                 "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}}
                for q in doc["faq"]
            ],
        })
    return blocos


# ---------------------------------------------------------------------------
# O QUE CONFERE CADA ARTIGO ANTES DE ELE EXISTIR
# ---------------------------------------------------------------------------

MOEDA = re.compile(r"(?:€|US\$|R\$)\s?\d[\d\.]*(?:,\d+)?")
# Artigo e preposicao, o que o portugues correto exige e a caixa de busca nao.
PALAVRAS_DE_LIGACAO = frozenset(
    ("o", "a", "os", "as", "um", "uma", "de", "do", "da", "dos", "das",
     "em", "no", "na", "nos", "nas", "e"))
ACENTOS = {"á": "a", "à": "a", "â": "a", "ã": "a", "é": "e", "ê": "e",
           "í": "i", "ó": "o", "ô": "o", "õ": "o", "ú": "u", "ü": "u",
           "ç": "c"}


def _sem_acento(texto):
    baixo = texto.lower()
    for com, sem in ACENTOS.items():
        baixo = baixo.replace(com, sem)
    return baixo


def _palavras(texto):
    """As palavras de uma frase, sem acento e sem pontuacao, para comparar."""
    return [p for p in re.split(r"[^0-9a-zà-ÿ]+", _sem_acento(texto)) if p]
DATA_NA_FRASE = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
PARAMETRO_DA_FERRAMENTA = re.compile(r"(?i)para\s+\d+\s+pessoas?|para\s+o\s+seu\s+grupo")


def _textos_de_tela(doc):
    """Toda frase que o leitor le, com o lugar dela, para o portao poder dizer ONDE.

    A varredura NAO pode dar `continue` em borda nenhuma: foi assim que as
    recusas duras da F3 passaram meses ecoando identificador de registro na tela
    sem nenhum portao ver -- as frases de borda nunca chegavam a regua. Entao
    aqui tudo entra, inclusive o que parece inofensivo.
    """
    saida = [("titulo", doc["titulo"]), ("h1", doc["h1"]),
             ("description", doc["description"])]
    c = doc["caixa_de_resposta"]
    for k in ("frase", "cartao_brasileiro", "promessa", "reconferir"):
        if c.get(k):
            saida.append(("caixa_de_resposta.%s" % k, c[k]))
    for i, item in enumerate(doc["monte_o_que_a_resposta_pede"]):
        saida.append(("monte[%d].rotulo" % i, item["rotulo"]))
        saida.append(("monte[%d].o_que_e" % i, item["o_que_e"]))
        saida.append(("monte[%d].calcular" % i, item["calcular"]["texto"]))
        saida.append(("monte[%d].ver_produtos" % i, item["ver_produtos"]["texto"]))
        saida.append(("monte[%d].aviso" % i, item["ver_produtos"]["aviso"]))
    for d in doc["dobras"]:
        saida.append(("dobra:%s" % d["titulo"], d["titulo"]))
        for j, p in enumerate(d["paragrafos"]):
            saida.append(("dobra:%s[%d]" % (d["titulo"], j), p))
    for q in doc["faq"]:
        saida.append(("faq.pergunta", q["pergunta"]))
        saida.append(("faq.resposta", q["resposta"]))
    for t in doc["veja_tambem"]:
        saida.append(("veja_tambem", t["ancora"]))
    for l in doc["tabela_resumo"]:
        saida.append(("tabela.rotulo", l["rotulo"]))
    saida.append(("mae_no_corpo", doc["mae_no_corpo"]))
    saida.append(("bloco_de_compra.aviso", doc["bloco_de_compra"]["aviso"]))
    return [(onde, txt) for onde, txt in saida if isinstance(txt, str) and txt]


def _dinheiro_permitido(doc, f1, banco, esquema, constantes):
    """O conjunto de valores que o BANCO autoriza esta pagina a publicar.

    Todo valor que aparece na tela tem de estar aqui. Hoje isso e quase uma
    tautologia, porque as frases sao copiadas da F1 -- e e DE PROPOSITO: o dia em
    que alguem escrever um preco a mao dentro do MAPA, ou ajustar uma frase «so
    para ler melhor», e o dia em que esta afirmacao para de ser tautologia e
    passa a ser a unica coisa entre o leitor e um numero sem dono.
    """
    permitido = set()
    experiencia = f1.indexar(banco)[2][doc["experiencia"]]
    for v in _versoes(experiencia):
        for n in list(PESSOAS_DA_TABELA) + [1]:
            r = f1.responder(experiencia["id"], v["id"], n, banco=banco,
                             esquema=esquema, constantes=constantes)
            if r["recusa_dura"] is not None:
                continue
            for frase in ([r["frase_resposta"], r["cartao_brasileiro"]]
                          + [l["frase"] for l in r["prestacao_de_contas"]["linhas"]]
                          + list(r["faixa_etaria"]["frases"])
                          + [l["frase"] for l in r["escada"]["linhas"]]
                          + [rec["frase"] for rec in r["recusas"]]):
                if frase:
                    permitido.update(m.group(0) for m in MOEDA.finditer(frase))
            for k in ("total_escrito", "por_pessoa_escrito",
                      "total_com_iof_escrito", "por_pessoa_com_iof_escrito"):
                if r["contas"].get(k):
                    permitido.add(r["contas"][k])
    return permitido


def conferir(doc, f1=None, banco=None, esquema=None, constantes=None):
    """Reprova o artigo, nomeando a regra. NUNCA morre em vez de relatar.

    A ordem aqui e deliberada e e a licao de 22/10/2026: AFIRMAR PRIMEIRO, e so
    entao ler o que a afirmacao garantiu. Naquele dia cinco quebras foram
    classificadas «morre» em vez de «reprova» porque o portao pegava o defeito e
    depois estourava lendo a lista que a propria afirmacao acabara de dizer
    vazia.
    """
    f1 = f1 or carregar_f1()
    banco = banco if banco is not None else f1.carregar_banco()
    esquema = esquema if esquema is not None else f1.carregar_esquema()
    constantes = constantes if constantes is not None else f1.carregar_constantes()

    falhas = []

    def reprova(regra, visto):
        falhas.append({"artigo": doc["id"], "regra": regra, "visto": visto})

    textos = _textos_de_tela(doc)
    proibidas = frases_proibidas()

    # (1) A VOZ. Frase proibida se mede pela FRASE inteira, nunca pela palavra
    # solta -- e a jurisprudencia que a Robometria deixou escrita em 02/10/2026.
    for onde, txt in textos:
        baixo = txt.lower()
        for frase in proibidas:
            if frase.lower() in baixo:
                reprova("voz: frase proibida pelo VOZ.md", "%s: «%s»" % (onde, frase))

    # (2) BASTIDOR DA FABRICA (molde de conversão, item 4).
    for onde, txt in textos:
        baixo = txt.lower()
        for frase in BASTIDOR_LITERAL:
            if frase.lower() in baixo:
                reprova("bastidor: frase da fábrica na página pública",
                        "%s: «%s»" % (onde, frase))
        for nome in BASTIDOR_NOMES:
            if nome.lower() in baixo:
                reprova("bastidor: nome de rotina ou de camada da fábrica",
                        "%s: «%s»" % (onde, nome))
        for padrao in BASTIDOR_FORMA:
            achado = padrao.search(txt)
            if achado:
                reprova("bastidor: referência a documento interno",
                        "%s: «%s»" % (onde, achado.group(0)))

    # (3) NENHUMA PROMESSA DE VOO. O nome tem «fly», o produto nao.
    for onde in ("titulo", "h1", "description"):
        if re.search(r"(?i)\bvo(?:o|os|ar|e)\b|\basa\b|passagem a[eé]rea", doc[onde]):
            reprova("o título não promete voo", "%s: «%s»" % (onde, doc[onde]))

    # (4) O TITULO DO GUIA NAO TOMA A CONSULTA DA FERRAMENTA.
    # A consulta parametrica («para N pessoas», «para o seu grupo») e da
    # calculadora; a crua e do guia. Duas paginas na mesma consulta e
    # canibalizacao, e e a propria ilha disputando consigo.
    for onde in ("titulo", "h1"):
        achado = PARAMETRO_DA_FERRAMENTA.search(doc[onde])
        if achado:
            reprova("o guia não disputa a consulta paramétrica da calculadora",
                    "%s: «%s»" % (onde, achado.group(0)))

    # (5) PRECO SEMPRE COM A DATA DA LEITURA, na propria caixa de resposta.
    frase = doc["caixa_de_resposta"]["frase"]
    if MOEDA.search(frase) and not DATA_NA_FRASE.search(frase):
        reprova("preço cravado como atual, sem a data da coleta",
                "caixa_de_resposta.frase: «%s»" % frase)

    # (6) REGISTRO PENDENTE DE RELEITURA: ressalva na caixa, e preco fora da
    # description, que e lida sozinha no resultado de busca.
    if doc["status_do_registro"] == "pendente_de_releitura":
        if not doc["caixa_de_resposta"].get("reconferir"):
            reprova("registro pendente sem a ressalva na caixa de resposta",
                    "caixa_de_resposta sem `reconferir`")
        if MOEDA.search(doc["description"]):
            reprova("preço de registro pendente dentro da description",
                    "description: «%s»" % doc["description"])

    # (7) NENHUM NUMERO DIGITADO. Todo valor da tela sai do banco -- e o valor
    # de terceiro so passa dentro da frase que nomeia quem o publicou e quando
    # foi lido. Esta foi a primeira coisa que este portao pegou, em 23/10/2026:
    # a regra escrita sem a excecao reprovava a prestacao de contas da gondola,
    # que e justamente o diferencial da ilha.
    permitido = _dinheiro_permitido(doc, f1, banco, esquema, constantes)
    frases_de_divergencia = {d["frase"]: d["publicador"]
                             for d in doc.get("divergencias") or []}
    for onde, txt in textos:
        publicador = frases_de_divergencia.get(txt)
        if publicador is not None:
            if publicador not in txt:
                reprova("valor de terceiro sem o publicador dentro da frase",
                        "%s: «%s»" % (onde, txt))
            if not DATA_NA_FRASE.search(txt):
                reprova("valor de terceiro sem a data em que foi lido",
                        "%s: «%s»" % (onde, txt))
            continue
        for m in MOEDA.finditer(txt):
            if m.group(0) not in permitido:
                reprova("valor na tela que o banco não autoriza",
                        "%s: «%s»" % (onde, m.group(0)))

    # (8) ACENTUACAO. A cicatriz da Robometria e portugues sem acento no ar, e
    # esta ilha TENTOU TRES REGUAS para ela em 23/10/2026. As tres estao escritas
    # aqui, com o que cada uma reprovou, porque a proxima execucao ia tentar as
    # mesmas tres e gastar a mesma hora.
    #
    # (i) «todo titulo tem de ter um acento» — reprovou tres paginas certas:
    #     «quanto custa subir na torre eiffel» nao tem uma letra acentuada e
    #     esta escrito corretamente.
    # (ii) «palavra acentuada num lugar nao aparece crua noutro» — 25
    #     reprovacoes em texto impecavel, porque em portugues o par sem acento
    #     costuma ser OUTRA PALAVRA: «e» e «é», «esta» e «está», «da» e «dá».
    # (iii) «paragrafo com 12 palavras ou mais tem de ter um acento» — reprovou
    #     «A partir de quantos dias de visita o Angkor Pass de 3 dias paga?» e
    #     «GetYourGuide, citada por terceiros publicou €34 (a partir de €34 por
    #     pessoa), lido em 14/09/2026». Catorze palavras, nenhum acento, as duas
    #     corretas. Subir o corte reduz o falso positivo e nao o elimina.
    #
    # O QUE ISSO DECIDE, e e informacao e nao desistencia: acentuacao correta
    # nao e verificavel localmente — e julgamento sobre cada palavra, e portao
    # que reprova texto certo e pior que portao nenhum, porque ensina a ignorar
    # o vermelho. O que SOBRA e verificavel e esta aqui: mojibake, que e
    # mecanico e inequivoco; e a procedencia de todo valor da tela, que a
    # afirmacao (7) ja cobra. A acentuacao das frases que a ferramenta gera e
    # garantida na fonte, pelas tres referencias, que nascem com a regra.
    for onde, txt in textos:
        if any(marca in txt for marca in ("\u00c3\u00a9", "\u00c3\u00a7",
                                          "\u00c3\u00a3", "\u00c3\u00b5",
                                          "\u00c2\u00a0")):
            reprova("texto de tela com acentuação corrompida", onde)

    # (9) A ARVORE: tres niveis mais o atual, mae linkada na trilha E no corpo.
    if len(doc["trilha"]) != 4:
        reprova("a trilha tem de ter Início, nível 1, nível 2 e a página atual",
                "trilha com %d níveis" % len(doc["trilha"]))
    else:
        if doc["trilha"][-1]["url"] is not None:
            reprova("o último nível da trilha não é link", "trilha")
        if doc["trilha"][2]["url"] != doc["mae_planejada"]:
            reprova("a trilha não aponta para a mãe declarada",
                    "trilha[2]=%s, mãe=%s" % (doc["trilha"][2]["url"],
                                              doc["mae_planejada"]))
    if doc["mae_planejada"] not in doc["mae_no_corpo"]:
        reprova("a mãe tem de ser linkada também numa frase do corpo",
                "mae_no_corpo: «%s»" % doc["mae_no_corpo"])
    if doc["nivel"] != 3:
        reprova("guia é nível 3 da árvore", "nivel=%r" % doc["nivel"])
    if not doc["url_planejada"].startswith(doc["mae_planejada"]):
        reprova("a URL do guia tem de nascer dentro da mãe",
                doc["url_planejada"])
    if DATA_NA_FRASE.search(doc["url_planejada"]) or re.search(
            r"20\d\d", doc["url_planejada"]):
        reprova("slug com data", doc["url_planejada"])

    # (10) IRMAS: de 2 a 4, todas da mesma mae, ancora igual a consulta delas.
    irmas = doc["veja_tambem"]
    if not 2 <= len(irmas) <= 4:
        reprova("«Veja também» tem de levar de 2 a 4 irmãs",
                "%d irmãs" % len(irmas))
    for t in irmas:
        if not t["url"].startswith(doc["mae_planejada"]):
            reprova("irmã de outra mãe no «Veja também»", t["url"])
        if t["url"] == doc["url_planejada"]:
            reprova("a página se lista como irmã de si mesma", t["url"])
        if t["ancora"].lower() in ("clique aqui", "saiba mais", "veja aqui"):
            reprova("âncora que não é a consulta da irmã", t["ancora"])

    # (11) O DESTINO COMERCIAL (portão de tema, item c) e o par guia/ferramenta.
    if doc["ferramenta_no_corpo"] not in json.dumps(doc, ensure_ascii=False):
        reprova("o guia não linka a ferramenta que ele explica",
                doc["ferramenta_no_corpo"])
    for i, item in enumerate(doc["monte_o_que_a_resposta_pede"]):
        if not item["calcular"]["url"].startswith(doc["ferramenta_no_corpo"]):
            reprova("o botão «Calcular» não leva à ferramenta desta ilha",
                    "monte[%d]: %s" % (i, item["calcular"]["url"]))
        if "experiencia=%s" % doc["experiencia"] not in item["calcular"]["url"]:
            reprova("o botão «Calcular» não leva o parâmetro da página",
                    "monte[%d]: %s" % (i, item["calcular"]["url"]))
        if not item["ver_produtos"]["url"]:
            reprova("item sem saída de compra", "monte[%d]" % i)

    # (12) O LINK DO MOMENTO. Pagina de fim de funil leva link de experiencia; o
    # cookie curto da plataforma obriga a mirar quem esta com o cartao na mao, e
    # link de experiencia em pagina de inicio de funil vence antes da compra.
    if doc["momento"] == "fim" and doc["link_do_momento"] != "experiência":
        reprova("página de fim de funil sem link de experiência",
                doc["link_do_momento"])
    if doc["momento"] == "inicio" and doc["link_do_momento"] == "experiência":
        reprova("página de início de funil com link de experiência: o cookie "
                "vence antes da compra", doc["link_do_momento"])

    # (13) O LINK CRU SAI SEM `sponsored`: ninguem esta pagando por aquele clique.
    compra = doc["bloco_de_compra"]
    if compra.get("programa") is None and "sponsored" in (compra.get("rel") or ""):
        reprova("link que não rende comissão marcado como patrocinado",
                compra["rel"])
    if "em breve" in (compra.get("aviso") or "").lower():
        reprova("promessa de link no lugar de uma saída de compra",
                compra["aviso"])

    # (14) A TABELA PRE-RENDERIZADA, visivel, cobrindo a faixa real de uso.
    if doc["tabela_recolhida"]:
        reprova("a tabela de casos resolvidos nunca é recolhida", "tabela_recolhida")
    pessoas_na_tabela = sorted({l["pessoas"] for l in doc["tabela_resumo"]})
    if pessoas_na_tabela != sorted(PESSOAS_DA_TABELA):
        reprova("a tabela não cobre 1, 2, 4 e 6 pessoas",
                "pessoas=%r" % (pessoas_na_tabela,))
    for l in doc["tabela_resumo"]:
        if not l.get("lido_em"):
            reprova("linha de tabela com preço e sem data de leitura",
                    "%s/%s" % (l["versao"], l["pessoas"]))

    # (15) JSON-LD: Article e BreadcrumbList sempre; FAQPage so com pergunta
    # que a propria pagina responde.
    tipos = [b["@type"] for b in doc["json_ld"]]
    for obrigatorio in ("Article", "BreadcrumbList"):
        if obrigatorio not in tipos:
            reprova("JSON-LD sem %s" % obrigatorio, "tipos=%r" % (tipos,))
    if "FAQPage" in tipos and not doc["faq"]:
        reprova("FAQPage sem pergunta respondida", "faq vazio")
    # DUAS PERGUNTAS RESPONDIDAS PELA MESMA FRASE e o rastro de um FAQ montado
    # por preguica, e foi o defeito desta propria passada: a primeira versao
    # emparelhava TODA pergunta declarada com a frase da caixa de resposta, e
    # publicava em tres dos quatro artigos um par que nao se fecha — «a partir de
    # quantos dias o passe mais longo paga?» respondido por «o de 1 dia custa
    # US$ 37». Se a pergunta e outra, a frase que a responde tem de ser outra.
    de_onde_vistas = {}
    for q in doc["faq"]:
        if not q["resposta"].strip():
            reprova("pergunta no FAQ sem resposta", q["pergunta"])
        de_onde = q.get("resposta_sai_de")
        if not de_onde:
            reprova("pergunta no FAQ sem dizer de onde sai a resposta",
                    q["pergunta"])
            continue
        if de_onde in de_onde_vistas:
            reprova("duas perguntas do FAQ respondidas pela mesma frase",
                    "«%s» e «%s» saem as duas de %r"
                    % (de_onde_vistas[de_onde], q["pergunta"], de_onde))
        de_onde_vistas[de_onde] = q["pergunta"]

    # (16) NADA NO AR.
    if doc["publicar"] is not False:
        reprova("artigo marcado para publicar sem site para publicar",
                "publicar=%r" % doc["publicar"])

    return falhas


def conferir_o_conjunto(docs):
    """O que nenhum artigo sozinho pode afirmar.

    A 16.4(f) e uma afirmacao sobre QUEM APONTA, e portao que conta so o que sai
    fica verde nos dois mundos. Aqui a conta e refeita na direcao de ENTRADA: com
    a janela rotacionando, o grau de entrada de toda filha tem de ser igual ao de
    saida. Se um dia a janela voltar a ser fixa, e esta afirmacao -- e nao a de
    cima -- que acusa.
    """
    falhas = []
    urls = {d["url_planejada"] for d in docs}
    entrada = {u: 0 for u in urls}
    for d in docs:
        for t in d["veja_tambem"]:
            if t["url"] in entrada:
                entrada[t["url"]] += 1
            else:
                falhas.append({"artigo": d["id"],
                               "regra": "irmã que não existe no conjunto",
                               "visto": t["url"]})
    esperado = min(4, len(docs) - 1) if len(docs) > 1 else 0
    for d in docs:
        saida = len(d["veja_tambem"])
        entra = entrada[d["url_planejada"]]
        if entra != saida or saida != esperado:
            falhas.append({
                "artigo": d["id"],
                "regra": "a janela de irmãs tem de rotacionar: entrada igual à saída",
                "visto": "entram %d, saem %d, esperado %d" % (entra, saida, esperado),
            })
    # Duas paginas na mesma consulta e a ilha disputando consigo.
    vistas = {}
    for d in docs:
        c = d["consulta_alvo"].lower()
        if c in vistas:
            falhas.append({"artigo": d["id"],
                           "regra": "duas páginas na mesma consulta-alvo",
                           "visto": "%s já é de %s" % (c, vistas[c])})
        vistas[c] = d["id"]
    slugs = {}
    for d in docs:
        u = d["url_planejada"]
        if u in slugs:
            falhas.append({"artigo": d["id"], "regra": "duas páginas na mesma URL",
                           "visto": u})
        slugs[u] = d["id"]
    return falhas


def todos(banco=None, esquema=None, constantes=None):
    f1 = carregar_f1()
    banco = banco if banco is not None else f1.carregar_banco()
    esquema = esquema if esquema is not None else f1.carregar_esquema()
    constantes = constantes if constantes is not None else f1.carregar_constantes()
    docs = [artigo(a["id"], banco=banco, esquema=esquema, constantes=constantes,
                   f1=f1) for a in MAPA]
    falhas = []
    for d in docs:
        falhas.extend(conferir(d, f1=f1, banco=banco, esquema=esquema,
                               constantes=constantes))
    falhas.extend(conferir_o_conjunto(docs))
    return docs, falhas


def main():
    if len(sys.argv) > 1:
        d = artigo(sys.argv[1])
        print(json.dumps(d, ensure_ascii=False, indent=1))
        falhas = conferir(d)
        print("\nfalhas: %d" % len(falhas))
        for f in falhas:
            print("  - [%s] %s :: %s" % (f["artigo"], f["regra"], f["visto"]))
        return 1 if falhas else 0

    docs, falhas = todos()
    print("ARTIGOS-ANCORA — %d escritos, %d pre-registrados" % (
        len(docs), len(pre_registrados())))
    for d in docs:
        print("\n  %s  ->  %s" % (d["id"], d["url_planejada"]))
        print("     consulta: %s" % d["consulta_alvo"])
        print("     titulo:   %s" % d["titulo"])
        print("     resposta: %s" % d["caixa_de_resposta"]["frase"])
        print("     irmas:    %s" % ", ".join(t["ancora"] for t in d["veja_tambem"]))
        print("     tabela:   %d linhas | dobras: %d | faq: %d" % (
            len(d["tabela_resumo"]), len(d["dobras"]), len(d["faq"])))
    for p in pre_registrados():
        print("\n  [NAO ESCRITO] pareado com a %s: %s" % (
            p["ferramenta_pareada"], p["consulta_alvo"]))
        print("     %s" % p["nao_foi_escrito_porque"])
    print("\nfalhas: %d" % len(falhas))
    for f in falhas:
        print("  - [%s] %s :: %s" % (f["artigo"], f["regra"], f["visto"]))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

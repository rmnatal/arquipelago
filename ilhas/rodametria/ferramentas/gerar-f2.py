#!/usr/bin/env python3
"""
GERADOR DA F2 — escreve dados/f2-respostas.json, que e o que o site le.

Por que existe um arquivo entre a referencia e o snippet: pela secao 8 do
ARQUIPELAGO.md, "para cada campo publicado, aponte quem e a fonte e faca a
bancada ler DELA". Quem publica a tabela pre-renderizada e o texto da resposta
e o snippet PHP, e o snippet le a option que o Sync grava de
dados/f2-respostas.json. Entao e ESTE arquivo a fonte de todo numero e de toda
frase que a F2 serve — a referencia em Python o escreve, a bancada o confere
contra a referencia, e o PHP nunca digita numero nenhum.

AS LINHAS DA TABELA SAO CONTADAS DO BANCO, NUNCA DIGITADAS (secao 8). As
combinacoes de V x Ah saem de dados/veiculos.json, uma por registro que declara
os dois campos; as duas combinacoes EXTERNAS (a tese da UPS Quito e o blog do
Mercado Livre) entram declaradas como externas, com fonte e data dentro da
propria linha, e nunca se misturam com as do banco.

    python3 ferramentas/gerar-f2.py            # escreve
    python3 ferramentas/gerar-f2.py --conferir # nao escreve; falha se divergir
"""

import json
import os
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)

# A regra mora em regras/, fora de ferramentas/, porque a bancada desta ilha
# denuncia arquivo em ferramentas/ que nao e portao — ver regras/LEIA.md.
import importlib.util
_spec = importlib.util.spec_from_file_location("f2ref", os.path.join(ILHA, "regras", "f2.py"))
f2ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(f2ref)

SAIDA = os.path.join(ILHA, "dados", "f2-respostas.json")

# O caso de exemplo que a 32.1 manda vir JA PREENCHIDO no formulario e JA
# PRE-RENDERIZADO na caixa de resultado. Os valores sao os da tabela 2.1 da
# especificacao, nao escolhidos aqui.
EXEMPLO = {"tensao_v": 48, "amperagem_ah": 20, "peso_piloto_kg": 90,
           "relevo": "misto", "autonomia_declarada_km": 60}

# Opcoes dos campos de escolha. V e Ah saem das faixas que as fichas colhidas
# declaram (bloco 1 e banco); a lista existe para o formulario nao aceitar
# combinacao que nenhuma ficha publica e para a resposta do navegador ser
# consulta e nao aritmetica livre.
TENSOES = [24, 36, 48, 60, 72]
AMPERAGENS = [7.8, 10.4, 12, 15, 20, 26, 30]

# As duas combinacoes que NAO saem do banco. Ficam aqui, separadas, com a
# procedencia dentro da linha — e o gerador as marca `externa: true` para a
# tela nunca as apresentar como ficha de produto a venda.
EXTERNAS = [
    {
        "rotulo": "Moto elétrica da medição de Quito",
        "tensao_v": 60, "amperagem_ah": 30, "autonomia_declarada_km": 60,
        "fonte": "Limaico Quinteros, R. D. — Universidade Politécnica Salesiana, "
                 "sede Quito, 2025 (mestrado em Engenharia Automotiva)",
        "data_leitura": "2026-10-28",
        "nota": "É MOTO, não patinete. Entra aqui porque é a única medição real de "
                "autonomia que a ilha tem com a ficha ao lado: 29,8 km medidos em "
                "condição mista contra 60 km de ficha.",
    },
    {
        "rotulo": "Modelo urbano de 36 V",
        "tensao_v": 36, "amperagem_ah": 10.4, "autonomia_declarada_km": 30,
        "fonte": "blog do Mercado Livre (mercadolivre.com.br/blog)",
        "data_leitura": "2026-10-28",
        "nota": "Declaração de publicador de marketplace, não de fabricante: o texto "
                "diz \"até 30 km\" para 36 V e 10,4 Ah.",
    },
]


# ---------------------------------------------------------------------------
# A 32.4 SE COBRA ONDE O TEXTO ENTRA NA PAGINA, E NAO ONDE ELE E IMPRESSO.
#
# Medido no ar as 11h1xZ de 29/10/2026, pelo conferir-no-ar.py: a palavra
# "egresso" — que a 32.4 lista por nome entre as proibidas na pagina publica —
# apareceu no texto servido da F2. NAO VEIO DO PHP: a regua de fonte do
# teste-f2.py varre o snippet e estava verde. Veio do `fonte` da constante
# `energia-wh-tensao-vezes-amperagem`, que diz "Nao depende de fonte nem de
# egresso" — frase CERTA no arquivo de constantes, que e registro interno, e
# proibida na tela, que e onde a dobra "As reguas que a conta usa" a imprime.
#
# E a familia do numero de tela digitado com o sinal invertido: ali o defeito
# era texto escrito a mao numa metade que nao fala com o banco; aqui e texto do
# banco indo para a tela sem ninguem o ler como texto de tela.
#
# O conserto e estrutural e tem duas metades:
#   (a) a constante que precisa de frase de leitor ganha uma AQUI, declarada,
#       com o texto interno preservado no arquivo de constantes;
#   (b) o gerador RECUSA publicar qualquer frase que carregue palavra de
#       bastidor. Ele falha em vez de publicar — portao no ponto em que o dado
#       vira texto, nao no ponto em que o texto e impresso.
# ---------------------------------------------------------------------------

PALAVRAS_DE_BASTIDOR = (
    "egresso", "SERP", "snippet", "wp-sitemap", "manifest", "ARQUIPELAGO",
    "bancada", "dados/", "ferramentas/", "regras/", "publicavel", "sha256",
    "nuvem", "getaddrinfo", "ENOTFOUND", "repositorio", "commit",
)

# Frase de leitor para a constante cujo texto interno carrega bastidor. A chave
# e o id; o valor e o que a tela diz. Constante que nao esta aqui publica o
# proprio `fonte`, e se ele carregar bastidor o gerador PARA.
FONTE_NA_TELA = {
    "energia-wh-tensao-vezes-amperagem":
        "Identidade de unidades: volt × ampère-hora dá watt-hora. Não é dado de "
        "ninguém e não tem fonte a citar — é a definição das unidades.",
    "consumo-absoluto-wh-por-km-patinete":
        "Não publicamos nenhum valor. A medição mais forte que achamos está em "
        "periódico que não conseguimos abrir, e as outras três candidatas foram "
        "recusadas: uma é de bicicleta e de fabricante de kit, uma é conta "
        "circular (divide a autonomia declarada pela energia, assumindo o número "
        "do fabricante) e uma é de moto, não de patinete.",
    "teto-de-carga-do-mercado-brasileiro":
        "Fichas de varejo lidas em extra.com.br, casasbahia.com.br e "
        "magazineluiza.com.br, mais o painel de afiliado da Shopee, em 27 e "
        "28/10/2026. A faixa observada foi de 115 a 140 kg, com 120 kg repetido.",
    "margem-de-carga-f3":
        "Decisão da Rodametria, e a página nunca a atribui a ninguém.",
    "fator-relevo-ladeira-contra-plano":
        "Limaico Quinteros, Rodrigo David. “Análisis de la eficiencia energética de "
        "la batería de ion litio en una moto eléctrica para el uso de micro "
        "movilidad”. Mestrado em Engenharia Automotiva, Universidade Politécnica "
        "Salesiana, sede Quito, 2025. Bateria de 60 V e 30 Ah numa moto elétrica, em "
        "rota de 25,8 km: 41,29 Wh/km no plano e 97,74 Wh/km em subida de 12%.",
    "fator-relevo-misto":
        "Decisão da Rodametria, não medição. O estudo de Quito também mediu uma "
        "condição mista, mas a mista dele é a rota dele, com a proporção de subida "
        "dele — usar aquele número aqui seria emprestar a geografia de Quito ao seu "
        "trajeto. O nosso é o meio-caminho geométrico entre os dois extremos "
        "medidos, e a página diz que é nosso.",
    "calibracao-autonomia-declarada-contra-medida":
        "Mesma medição de Quito, de 2025: a mesma moto elétrica de 60 V e 30 Ah, na "
        "mesma rota de 25,8 km, entregou 29,8 km contra os 60 km que a ficha "
        "declarava.",
}

# PALAVRA PORTUGUESA SEM ACENTO NA TELA E DEFEITO, E ELA CHEGA DE ARQUIVO.
#
# A secao 8 manda: "texto na tela sai acentuado". Os arquivos de dado desta ilha
# sao escritos em ASCII — e o `fonte` de duas constantes ia para a dobra dizendo
# "Decisao desta ilha, nao medicao". Nenhuma regua de PHP veria: o texto nao
# mora no PHP. E a mesma familia do achado da 32.4 acima, no mesmo campo.
#
# A regua nao adivinha: ela tem a lista das formas que esta ilha de fato produz,
# e cresce quando alguem achar outra. Heuristica sobre acento reprova nome
# proprio estrangeiro (o titulo em espanhol da tese, por exemplo).
SEM_ACENTO_NA_TELA = (
    "decisao", "medicao", "proposito", "numero", "nao ", "tambem", "voce",
    "veiculo", "eletric", "reguas", "procedencia", "amperagem-hora",
    "pagina", "secao", "ultima", "proximo", "orcamento", "duvida",
)


def conferir_acento_na_tela(textos):
    """Toda frase que a tela serve tem de estar acentuada (secao 8)."""
    for onde, texto in textos:
        baixo = texto.lower()
        for forma in SEM_ACENTO_NA_TELA:
            assert forma not in baixo, (
                "texto de tela sem acento em %s: a forma %r aparece em %r. Texto de "
                "arquivo ASCII nao vai para a tela cru." % (onde, forma, texto[:120]))


def fonte_na_tela(cid, registro):
    """O que a tela diz sobre a procedencia desta regua — e nada mais."""
    texto = FONTE_NA_TELA.get(cid) or (registro.get("fonte") or "")
    for palavra in PALAVRAS_DE_BASTIDOR:
        assert palavra.lower() not in texto.lower(), (
            "32.4: a frase de procedencia de %r carrega a palavra de bastidor %r e ela "
            "iria para a tela: %r. Declare a frase de leitor em FONTE_NA_TELA."
            % (cid, palavra, texto[:120]))

    return texto


def _valor(campo):
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def frase_do_bloco_de_compra(quantos, cabem_no_wh):
    """A frase de abertura do bloco de compra, DERIVADA da contagem da vitrine.

    POR QUE ELA NASCEU AQUI EM 29/10/2026: ela era uma string digitada dentro do
    PHP — "Nenhum destes entrou pela conta de Wh: a ficha deles não declara
    tensão nem amperagem" — e portanto uma afirmacao sobre o ESTADO DO BANCO que
    nenhum portao conferia. Hoje ela e verdadeira; no dia em que um registro
    declarar V e Ah com oferta aberta, o cartao entra em `cabem_no_wh` e o
    paragrafo acima dele continua dizendo que nenhum entrou. E a mesma familia
    da 32.5-d: regra escrita para o mundo que existia, sa por falta de dado que
    a contradiga. Agora o numero e contado e a frase sai dele.

    E ela DEIXOU DE NOMEAR A CAUSA de proposito. Nomeando, o bloco dizia a mesma
    coisa tres vezes na mesma tela: o paragrafo, a linha `bateria não declarada`
    do cartao e o rotulo do grupo do cartao. A causa e por cartao — cada um pode
    estar aqui por motivo diferente — e e o cartao que a diz.
    """
    if quantos <= 0:
        return ""
    if cabem_no_wh == 0:
        if quantos == 1:
            return ("O único com oferta aberta hoje não entrou pela conta de Wh, e o "
                    "cartão dele diz por quê. Vem com o watt do anúncio e o preço com "
                    "a data da leitura.")
        return ("Nenhum dos %d com oferta aberta hoje entrou pela conta de Wh, e cada "
                "cartão diz por quê. Vêm com o watt do anúncio e o preço com a data "
                "da leitura." % quantos)
    if cabem_no_wh == quantos:
        if quantos == 1:
            return ("O único com oferta aberta hoje cabe no Wh que você pediu. Vem com "
                    "o watt do anúncio e o preço com a data da leitura.")
        return ("Os %d com oferta aberta hoje cabem no Wh que você pediu. Vêm com o "
                "watt do anúncio e o preço com a data da leitura." % quantos)
    return ("%d dos %d com oferta aberta hoje cabem no Wh que você pediu e vêm "
            "primeiro; o que cada um dos outros é está escrito no cartão dele."
            % (cabem_no_wh, quantos))


def quem_declara(registro, campo, escada):
    """A atribuicao que a tela imprime ao lado de um numero colhido.

    A frase NUNCA e digitada aqui: ela sai de `escada_de_fontes.niveis[].na_tela
    .quem_declara` do esquema, alcancada pelo caminho que o proprio banco grava
    — o campo diz qual `fonte` o sustenta, a fonte do registro diz o `nivel`, e
    o nivel diz como se atribui na tela. Entao o dia em que a escada mudar a
    palavra, o cartao muda com ela, e nao ha segunda copia para envelhecer.

    Devolve None quando o campo nao foi colhido: ai nao ha o que atribuir.
    """
    c = registro.get(campo)
    if not isinstance(c, dict) or c.get("valor") is None:
        return None
    fonte = (registro.get("fontes") or {}).get(c.get("fonte")) or {}
    nivel = fonte.get("nivel")
    for n in escada["niveis"]:
        if n["nivel"] == nivel:
            return (n.get("na_tela") or {}).get("quem_declara")
    return None


def linhas_do_banco(veiculos):
    """Uma linha por registro do banco que declara V E Ah. Contado, nunca digitado."""
    linhas = []
    for r in veiculos["registros"]:
        if r.get("status") == "excluido_do_banco":
            continue
        v = _valor(r.get("tensao_v"))
        a = _valor(r.get("amperagem_ah"))
        if v is None or a is None:
            continue
        aut = _valor(r.get("autonomia_declarada_km"))
        fonte_campo = (r.get("tensao_v") or {}).get("fonte") if isinstance(r.get("tensao_v"), dict) else None
        fonte = (r.get("fontes") or {}).get(fonte_campo) or {}
        nome = " ".join(x for x in (r.get("marca"), r.get("modelo")) if x) or r.get("id")
        linhas.append({
            "rotulo": nome,
            "id_registro": r["id"],
            "tensao_v": v,
            "amperagem_ah": a,
            "autonomia_declarada_km": aut,
            "fonte": fonte.get("tipo") or "não declarada",
            "fonte_nivel": fonte.get("nivel"),
            "data_leitura": fonte.get("data_leitura"),
            "externa": False,
            "nota": None,
        })
    return linhas


def montar_linha(base, constantes):
    """Monta a linha da tabela com Wh e a faixa degradada nos tres relevos."""
    wh = f2ref.energia_wh(base["tensao_v"], base["amperagem_ah"])
    faixas = {}
    for relevo in f2ref.RELEVOS:
        fator, _cid = f2ref.fator_do_relevo(constantes, relevo)
        f = f2ref.faixa_de_km(base.get("autonomia_declarada_km"), fator)
        if f["tem_km"]:
            faixas[relevo] = {
                "piso_km": f2ref._n(f["piso_km"]),
                "teto_km": f2ref._n(f["teto_km"]),
                "degenerada": f["faixa_degenerada"],
            }
        else:
            faixas[relevo] = {"piso_km": None, "teto_km": None, "causa": f["causa"]}
    saida = dict(base)
    saida["wh"] = f2ref._n(wh)
    saida["wh_bruto"] = int(wh) if wh == int(wh) else float(wh)
    saida["faixas"] = faixas
    saida["externa"] = bool(base.get("externa", False))
    return saida


def conferir_moldes(constantes):
    """O MOLDE PREENCHIDO TEM DE SER, LETRA POR LETRA, A FRASE DA REFERENCIA.

    Esta afirmacao e a unica coisa que impede o arquivo publicado de carregar um
    molde que ninguem usa — o caso em que o navegador preenche um texto e o PHP
    serve outro. Ela varre os quatro mundos da `faixa_de_km`, inclusive os dois
    que o banco de hoje nao produz (plano com faixa degenerada, e o mundo em que
    o degrau 3 existe), porque e a regra do "produza o mundo" da secao 8.
    """
    from fractions import Fraction as F
    casos = [
        (48, 20, 90, "misto", 60),
        (60, 20, 90, "ladeira", 70),
        (36, 10.4, 70, "plano", 25),
        (48, 20, 90, "misto", None),
        (72, 30, 130, "ladeira", 100),
    ]
    for c in casos:
        r = f2ref.responder(*c, constantes=constantes)
        v, ah, peso, relevo, aut = c
        esperado = f2ref.MOLDES["wh"].format(
            v=f2ref._n(F(str(v))), ah=f2ref._n(F(str(ah)), 1), wh=f2ref._n(r["wh"]))
        assert r["frase_wh"] == esperado, (r["frase_wh"], esperado)

        f = r["faixa"]
        if not f["tem_km"]:
            assert r["frases_km"][0] == f2ref.MOLDES["km_recusa"]
        elif f["faixa_degenerada"] and f["degrau"] == 2:
            assert r["frases_km"][0] == f2ref.MOLDES["km_plano"].format(
                teto=f2ref._n(f["teto_km"]))
        elif f["degrau"] == 2:
            assert r["frases_km"][0] == f2ref.MOLDES["km_degradado"].format(
                relevo_frase=f2ref.RELEVO_FRASE[relevo],
                piso=f2ref._n(f["piso_km"]), teto=f2ref._n(f["teto_km"]))
        assert r["frases_peso"][0] == f2ref.MOLDES["peso"].format(
            peso=f2ref._n(F(str(peso))))

    # O mundo que o banco nao tem: o degrau 3 publicavel.
    fator, _ = f2ref.fator_do_relevo(constantes, "misto")
    f3 = f2ref.faixa_de_km(None, fator, consumo_wh_por_km=20, wh=960)
    assert f3["tem_km"] and f3["degrau"] == 3, f3
    assert f2ref.MOLDES["km_absoluto"].format(
        wh="960", piso=f2ref._n(f3["piso_km"])).startswith("Com 960 Wh")


def montar(constantes, veiculos, pecas, escada):
    conferir_moldes(constantes)
    CONSTANTES_NA_TELA = (
        "energia-wh-tensao-vezes-amperagem",
        "fator-relevo-ladeira-contra-plano",
        "fator-relevo-misto",
        "calibracao-autonomia-declarada-contra-medida",
        "consumo-absoluto-wh-por-km-patinete",
        "teto-de-carga-do-mercado-brasileiro",
    )
    conferir_acento_na_tela(
        [("fonte de " + cid, fonte_na_tela(cid, constantes[cid]))
         for cid in CONSTANTES_NA_TELA]
        + [("molde " + k, v) for k, v in f2ref.MOLDES.items()]
        + [("externa " + e["rotulo"], e["fonte"] + " " + (e.get("nota") or ""))
           for e in EXTERNAS])
    exemplo = f2ref.responder(constantes=constantes, **EXEMPLO)

    linhas = [montar_linha(l, constantes) for l in linhas_do_banco(veiculos)]
    linhas_externas = [montar_linha(dict(e, externa=True), constantes) for e in EXTERNAS]

    # Prestacao de contas da secao 7, contada sobre o banco inteiro.
    wh_exemplo = f2ref.energia_wh(EXEMPLO["tensao_v"], EXEMPLO["amperagem_ah"])
    grupos = f2ref.grupos_de_compra(veiculos["registros"], wh_exemplo)

    def ficha(r):
        af = r.get("afiliado") or {}
        cot = (r.get("cotacoes") or [{}])[0] if r.get("cotacoes") else {}
        nome = " ".join(x for x in (r.get("marca"), r.get("modelo")) if x) or r["id"]
        return {
            "id": r["id"],
            "nome": nome,
            "tipo_comercial": r.get("tipo_comercial"),
            "status": r.get("status"),
            "watt_sem_rotulo": _valor(r.get("potencia_declarada_sem_rotulo_w")),
            "tensao_v": _valor(r.get("tensao_v")),
            "amperagem_ah": _valor(r.get("amperagem_ah")),
            "carga_max_kg": _valor(r.get("carga_max_kg")),
            # A AUTONOMIA DECLARADA NO CARTAO, e ela nao e enfeite: esta pagina
            # RESPONDE autonomia, e o cartao dela vinha calado sobre o unico
            # numero de autonomia que a oferta linkada publica. A atribuicao vem
            # junta e sai da escada (nivel 6 = "pelo vendedor"), porque numero de
            # nivel 6 na tela sem dizer de quem e promessa da ilha.
            "autonomia_declarada_km": _valor(r.get("autonomia_declarada_km")),
            "autonomia_quem_declara": quem_declara(r, "autonomia_declarada_km", escada),
            "preco_brl": cot.get("valor_brl"),
            "preco_loja": cot.get("loja"),
            "preco_data": cot.get("data_leitura"),
            "url_busca": af.get("url_busca"),
            # A FICHA, quando o casamento do bloco 3d a achou. Pela 25.2 ela
            # vira o BOTAO e a busca desce para a linha discreta — e e a tela
            # que faz essa troca, nao o banco: o banco guarda as duas, porque
            # ficha morre e busca nao.
            "url_afiliado_da_ficha": af.get("url"),
            "url_produto": af.get("url_produto"),
            "programa": af.get("programa"),
            "degrau": af.get("degrau"),
            "imagem": r.get("imagem"),
        }

    grupos_tela = {k: [ficha(r) for r in v] for k, v in grupos.items()}

    # A VITRINE: todo item PUBLICAVEL e com saida de compra (25.2), NA ORDEM DA
    # SECAO 7 — elegibilidade tecnica completa primeiro, e quem falha numa
    # condicao nunca vem antes de quem passa em todas.
    #
    # A PRIMEIRA VERSAO DESTA FUNCAO ESTAVA ERRADA, e quem a pegou foi a mutacao
    # que PRODUZ O MUNDO (secao 8), rodada em 29/10/2026: ela lia SO o grupo
    # `nao_declaram_v_ou_ah`, porque e o unico que o banco de hoje enche. Com um
    # registro fabricado declarando V, Ah E oferta aberta, o item caia em
    # `de_outro_wh` e DESAPARECIA da vitrine — item publicavel com piso fora do
    # bloco de compra, que e o avesso da 25.2. A regua nasceu para um mundo que
    # nunca aconteceu e nao podia falhar ate o mundo existir.
    ORDEM_DOS_GRUPOS = (
        ("cabem_no_wh", "cabe no Wh que você pediu"),
        ("de_outro_wh", "bateria de outra faixa de energia"),
        ("nao_declaram_v_ou_ah", "a ficha não declara a bateria"),
    )
    vitrine = []
    quantos_por_grupo = {}
    for chave, rotulo in ORDEM_DOS_GRUPOS:
        parte = [dict(f, rotulo_do_grupo=rotulo) for f in grupos_tela[chave]
                 if f["status"] == "publicavel" and f["url_busca"]]
        parte.sort(key=lambda f: (f["tipo_comercial"] != "patinete",
                                  -(f["watt_sem_rotulo"] or 0)))
        quantos_por_grupo[chave] = len(parte)
        vitrine.extend(parte)

    frase_de_abertura = frase_do_bloco_de_compra(len(vitrine),
                                                 quantos_por_grupo["cabem_no_wh"])
    # AS CINCO FRASES SAO CONFERIDAS, NAO SO A QUE O BANCO DE HOJE ACENDE. E o
    # proprio defeito que esta funcao veio consertar: texto que so e lido no
    # mundo que existe envelhece sao. Os mundos sao fabricados aqui — vitrine
    # de 1 e de 4, com 0, com todos e com parte cabendo no Wh.
    conferir_acento_na_tela(
        [("frase do bloco de compra %r" % (c,), frase_do_bloco_de_compra(*c))
         for c in ((1, 0), (4, 0), (1, 1), (4, 4), (4, 1))]
        + [("frase do bloco de compra, vitrine vazia", frase_do_bloco_de_compra(0, 0))])

    pecas_pub = [ficha(r) for r in pecas["registros"]
                 if r.get("status") == "publicavel" and (r.get("afiliado") or {}).get("url_busca")]

    return {
        "id": "f2-respostas",
        "ilha": "rodametria",
        "ferramenta": "F2",
        "bloco": "3b",
        "gerado_em": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%d"),
        "gerado_por": "ferramentas/gerar-f2.py",
        "referencia": "ferramentas/f2-referencia.py",
        "especificacao": "dados/especificacao-calculadoras.md, secao 2",
        "publicar": True,
        "nota": "Tudo que a F2 serve na tela sai daqui: nenhum numero e nenhuma frase "
                "da F2 e digitado dentro do snippet PHP. As linhas do banco sao "
                "CONTADAS de dados/veiculos.json; as duas externas estao marcadas "
                "`externa: true` com fonte e data dentro da linha.",
        "campos": {
            "tensoes_v": TENSOES,
            "amperagens_ah": AMPERAGENS,
            "relevos": list(f2ref.RELEVOS),
            "exemplo": EXEMPLO,
        },
        "constantes_usadas": {
            cid: {
                "valor": constantes[cid].get("valor"),
                "status": constantes[cid].get("status"),
                "tipo": constantes[cid].get("tipo"),
                "fonte": fonte_na_tela(cid, constantes[cid]),
                "url": constantes[cid].get("url"),
                "verificado_em": constantes[cid].get("verificado_em"),
            }
            for cid in ("energia-wh-tensao-vezes-amperagem",
                        "fator-relevo-ladeira-contra-plano",
                        "fator-relevo-misto",
                        "calibracao-autonomia-declarada-contra-medida",
                        "consumo-absoluto-wh-por-km-patinete",
                        "teto-de-carga-do-mercado-brasileiro")
        },
        # Os moldes de frase viajam INTEIROS, de um lugar so: e deles que o
        # navegador monta a resposta quando a pessoa troca um campo, e e deles
        # que o PHP monta a resposta pre-renderizada. Duas metades lendo o
        # mesmo molde nao podem dizer coisas diferentes para a mesma entrada.
        "frases_molde": dict(f2ref.MOLDES),
        "relevo_frase": dict(f2ref.RELEVO_FRASE),
        "fatores_de_relevo": {
            relevo: str(f2ref.fator_do_relevo(constantes, relevo)[0])
            for relevo in f2ref.RELEVOS
        },
        "fatores_de_relevo_tela": {
            relevo: f2ref._n(f2ref.fator_do_relevo(constantes, relevo)[0], 2)
            for relevo in f2ref.RELEVOS
        },
        "degrau_3_disponivel": f2ref.constante_publicavel(
            constantes, "consumo-absoluto-wh-por-km-patinete") is not None,
        "resposta_exemplo": {
            "entrada": exemplo["entrada"],
            "wh_tela": exemplo["wh_tela"],
            "piso_km_tela": exemplo["piso_km_tela"],
            "teto_km_tela": exemplo["teto_km_tela"],
            "frase_wh": exemplo["frase_wh"],
            "frases_km": exemplo["frases_km"],
            "frases_peso": exemplo["frases_peso"],
            "frases_calibracao": exemplo["frases_calibracao"],
        },
        "tabela": {
            "do_banco": linhas,
            "externas": linhas_externas,
            "total_do_banco": len(linhas),
            "total_externas": len(linhas_externas),
        },
        "compra": {
            "vitrine": vitrine,
            "frase_de_abertura": frase_de_abertura,
            "grupos": grupos_tela,
            "contagem": {k: len(v) for k, v in grupos_tela.items()},
            "total_registros_veiculos": len(veiculos["registros"]),
            "pecas_publicaveis": pecas_pub,
            "pecas_que_a_resposta_pede": ["bateria por V/Ah", "carregador pela tensão"],
        },
    }


def main():
    conferir = "--conferir" in sys.argv
    constantes = f2ref.carregar_constantes()
    with open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
        veiculos = json.load(f)
    with open(os.path.join(ILHA, "dados", "pecas.json"), encoding="utf-8") as f:
        pecas = json.load(f)
    with open(os.path.join(ILHA, "dados", "esquema-banco.json"), encoding="utf-8") as f:
        escada = json.load(f)["escada_de_fontes"]

    novo = montar(constantes, veiculos, pecas, escada)
    texto = json.dumps(novo, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            print("REPROVADO: %s nao existe. Rode sem --conferir." % SAIDA)
            return 1
        atual = open(SAIDA, encoding="utf-8").read()
        # O SELO `gerado_em` SAI DA COMPARACAO, E ISSO E CONSERTO MEDIDO, NAO
        # FROUXIDAO (30/10/2026). Ele e o RELOGIO DA EXECUCAO (ver `montar`),
        # nao um dado derivado das entradas: a F2 nao depende da data para
        # nada que ela calcula. Comparando-o, este portao reprovava a pagina
        # CERTA todo dia seguinte ao que ela foi gerada — medido as 10h3xZ de
        # 30/10/2026, com a bancada acusando `REPROVADO` e a unica diferenca
        # entre o arquivo no ar e o recem-gerado sendo `2026-10-29` ->
        # `2026-10-30`. E o perigo que a 20.5 e a 32.5-b nomeiam com todas as
        # letras: portao que reprova pagina certa e o caminho mais curto para
        # alguem passar a ignora-lo. A irma `gerar-vitrine-de-produto.py` ja
        # fazia certo (`'gerado_em': anuncios['gerado_em']`, herdada do dado),
        # e os `coletar-*` selam a data da MEDICAO, que e procedencia e tem de
        # entrar. O que o portao continua cobrando e TODO o resto do arquivo.
        def sem_selo(bruto, rotulo):
            try:
                d = json.loads(bruto)
            except ValueError as e:
                print("REPROVADO: %s nao e JSON legivel (%s): %s"
                      % (rotulo, SAIDA, e))
                return None
            d["gerado_em"] = "<selo-fora-da-comparacao>"
            return json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True)

        a, b = sem_selo(atual, "o arquivo gravado"), sem_selo(texto, "a referencia")
        if a is None:
            return 1
        if a != b:
            print("REPROVADO: dados/f2-respostas.json esta diferente do que a "
                  "referencia produz agora, FORA do selo `gerado_em`. Rode "
                  "`python3 ferramentas/gerar-f2.py`.")
            return 1
        print("APROVADO: dados/f2-respostas.json bate com a referencia "
              "(o selo `gerado_em` fica fora da comparacao, de proposito: "
              "ele e o relogio da execucao e nao entra em nada que a F2 calcula).")
        return 0

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    c = novo["compra"]["contagem"]
    print("gravado %s" % SAIDA)
    print("  tabela: %d linhas do banco + %d externas"
          % (novo["tabela"]["total_do_banco"], novo["tabela"]["total_externas"]))
    print("  vitrine: %d item(ns) publicavel(eis) com piso de compra"
          % len(novo["compra"]["vitrine"]))
    print("  prestacao de contas (soma fecha %d registros): %s"
          % (novo["compra"]["total_registros_veiculos"], c))
    return 0


if __name__ == "__main__":
    sys.exit(main())

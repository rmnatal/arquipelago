#!/usr/bin/env python3
"""
PORTAO DA F1 — sem rede, e ele NAO afirma 1.000 nem 32.

A 1.6 da especificacao e literal: *"o portao usa limiares FICTICIOS, declarados
como ficticios no proprio caso (por exemplo LIMIAR_AUTOPROP_W = 777), e afirma
a ARVORE, nao os numeros do mundo. Portao que afirma 1.000 W antes de o texto
oficial chegar e o numero de tela digitado com outra roupa."* O texto oficial
chegou em 05/11/2026 — e a regra continua valendo, por um motivo que ficou MAIS
forte e nao menos: portao que grava os numeros de hoje aprova a arvore errada no
dia em que a resolucao mudar, e aprova em silencio.

ENTAO ESTE PORTAO TEM DUAS METADES QUE NAO SE MISTURAM:

  (A) A ARVORE, com limiares FICTICIOS, conferida contra uma arvore escrita
      AQUI, a mao, sem importar nada de regras/f1.py. E a regra da secao 8:
      *"quem confere escreve a propria regua, nunca chama a de quem produziu o
      dado"*.

  (B) OS NUMEROS DO MUNDO, conferidos contra dados/constantes.json — e a
      afirmacao e `o que a referencia usa e o que a constante diz`, nunca `o
      que a referencia usa e 1.000`. Se alguem trocar o valor na constante, esta
      metade continua verde e DEVE continuar: a constante e a fonte.

  (C) A TERCEIRA METADE, que e sobre a FRONTEIRA entre o codigo e o dado: nenhum
      literal de limiar pode aparecer em regras/f1.py. Isso se mede lendo o
      arquivo, nao confiando nele.

O AUTOTESTE RODA SEMPRE, e nao atras de um `--autoteste`. A bancada desta ilha
so descobre `--autoteste` nos portoes de REDE, e este e dos sem rede: *"portao
que depende de alguem lembrar nao roda"*. Entre os mundos fabricados esta o que
a 20.8 exige — um em que a regua VELHA (a arvore de TRES saidas da 1.3) e a NOVA
(quatro saidas) DISCORDAM. Autoteste em que as duas concordam nao mede conserto
nenhum.
"""

import io
import json
import os
import re
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(ILHA, "regras"))

import f1 as f1ref  # noqa: E402

CONSTANTES = os.path.join(ILHA, "dados", "constantes.json")
RESPOSTAS = os.path.join(ILHA, "dados", "f1-respostas.json")
FONTE_DA_REFERENCIA = os.path.join(ILHA, "regras", "f1.py")

GERADOR = os.path.join(AQUI, "gerar-f1.py")

FALHAS = []
AFIRMACOES = [0]


def _carregar_gerador():
    """O gerador tem HIFEN no nome, entao entra por importlib e nao por import.

    Ele e carregado porque a metade (I) mede uma frase que mora NELE e nao nos
    moldes da referencia — e foi justamente por nao ser molde que ela foi ao ar
    falsa em 06/11/2026 e ficou tres dias sem nenhum portao olhando.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("gerar_f1_para_teste", GERADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ok(condicao, frase):
    AFIRMACOES[0] += 1
    if not condicao:
        FALHAS.append(frase)


# ---------------------------------------------------------------------------
# LIMIARES FICTICIOS, DECLARADOS FICTICIOS. Nenhum deles e um numero da
# resolucao, e os valores foram escolhidos para serem reconheciveis a olho: se
# um 777 vazar para a tela, qualquer leitor ve que e de teste.
# ---------------------------------------------------------------------------
FICTICIOS = {
    "LIMIAR_BIKE_W": Fraction(555),
    "LIMIAR_BIKE_KMH": Fraction(11),
    "LIMIAR_AUTOPROP_W": Fraction(777),
    "LIMIAR_AUTOPROP_KMH": Fraction(22),
    "LIMIAR_AUTOPROP_LARGURA_MM": Fraction(333),
    "LIMIAR_AUTOPROP_ENTRE_EIXOS_MM": Fraction(888),
    "LIMIAR_CICLOMOTOR_W": Fraction(999),
    "LIMIAR_CICLOMOTOR_KMH": Fraction(44),
}


def arvore_a_mao(w, kmh, acel, lim):
    """A MINHA arvore, escrita aqui, sem olhar para regras/f1.py.

    Devolve a categoria ou a string da causa precedida de `recusa:`. A ordem das
    recusas e a que a 1.1 e a 1.4(a) mandam, reescrita do texto da
    especificacao e nao copiada do codigo.
    """
    if lim is None:
        return "recusa:limiar_legal_pendente"
    if acel is None or acel == "nao_declarado":
        return "recusa:acelerador_nao_declarado"
    if w is None:
        return "recusa:potencia_nominal_ausente"
    if kmh is None:
        return "recusa:velocidade_max_ausente"
    if Fraction(str(w)) <= 0 or Fraction(str(kmh)) <= 0:
        return "recusa:entrada_nao_positiva"

    pot = Fraction(str(w))
    vel = Fraction(str(kmh))
    bike = (acel == "so_pedal_assistido"
            and not (pot > lim["LIMIAR_BIKE_W"])
            and not (vel > lim["LIMIAR_BIKE_KMH"]))
    if bike:
        return "bicicleta_eletrica"
    autoprop = (not (pot > lim["LIMIAR_AUTOPROP_W"])
                and not (vel > lim["LIMIAR_AUTOPROP_KMH"]))
    if autoprop:
        return "autopropelido"
    ciclo = (not (pot > lim["LIMIAR_CICLOMOTOR_W"])
             and not (vel > lim["LIMIAR_CICLOMOTOR_KMH"]))
    if ciclo:
        return "ciclomotor"
    return "acima_do_ciclomotor"


def arvore_VELHA_de_tres_saidas(w, kmh, acel, lim):
    """A arvore como a 1.3 a escreveu em 28/10, com TRES saidas.

    Ela existe aqui para UM proposito: provar que o conserto de 06/11 MORDE. A
    20.8 cobra que o autoteste tenha um mundo em que a regua velha e a nova
    discordam — sem isso o conserto e afirmacao. Nao e a regra da ilha e nunca
    foi usada em producao: ela termina em `senao -> ciclomotor`, e e isso que
    esta errado.
    """
    if lim is None:
        return "recusa:limiar_legal_pendente"
    if acel is None or acel == "nao_declarado":
        return "recusa:acelerador_nao_declarado"
    if w is None:
        return "recusa:potencia_nominal_ausente"
    if kmh is None:
        return "recusa:velocidade_max_ausente"
    pot, vel = Fraction(str(w)), Fraction(str(kmh))
    if pot <= 0 or vel <= 0:
        return "recusa:entrada_nao_positiva"
    if (acel == "so_pedal_assistido" and pot <= lim["LIMIAR_BIKE_W"]
            and vel <= lim["LIMIAR_BIKE_KMH"]):
        return "bicicleta_eletrica"
    if pot <= lim["LIMIAR_AUTOPROP_W"] and vel <= lim["LIMIAR_AUTOPROP_KMH"]:
        return "autopropelido"
    return "ciclomotor"


def _veredito(r):
    return r["categoria"] if r["classifica"] else ("recusa:" + r["causa_da_recusa"])


# ---------------------------------------------------------------------------
# (A) A ARVORE, varrida com limiares FICTICIOS.
# ---------------------------------------------------------------------------
def metade_a():
    ws = [None, 0, 1, 554, 555, 556, 776, 777, 778, 998, 999, 1000, 5000]
    kmhs = [None, 0, 1, 10, 11, 12, 21, 22, 23, 43, 44, 45, 120]
    acels = [None, "manual", "so_pedal_assistido", "nao_declarado"]

    divergentes = 0
    total = 0
    for w in ws:
        for kmh in kmhs:
            for acel in acels:
                total += 1
                meu = arvore_a_mao(w, kmh, acel, FICTICIOS)
                dela = _veredito(f1ref.responder(
                    w, kmh, acel, "", constantes=_constantes_ficticias(),
                    municipios=[]))
                ok(meu == dela,
                   "a arvore discorda em (W=%r, km/h=%r, acel=%r): a minha diz %r e a "
                   "referencia diz %r" % (w, kmh, acel, meu, dela))
                velha = arvore_VELHA_de_tres_saidas(w, kmh, acel, FICTICIOS)
                if velha != meu:
                    divergentes += 1

    # A 20.8: a regua velha e a nova TEM de discordar em algum mundo, senao o
    # conserto de 06/11 nao conserta nada.
    ok(divergentes > 0,
       "a arvore de TRES saidas da 1.3 e a de QUATRO concordam em todos os %d mundos "
       "varridos — entao o conserto de 06/11 nao morde, e um dos dois esta errado"
       % total)
    print("  varredura da arvore: %d mundos, e a regua VELHA (tres saidas) discorda "
          "da NOVA em %d deles" % (total, divergentes))

    # A trava do PIVO, afirmada sozinha: `nao_declarado` NUNCA cai no lado
    # permissivo por omissao. Com W e km/h dentro do limite da bicicleta, a
    # resposta tem de ser RECUSA e nunca `bicicleta_eletrica`.
    r = f1ref.responder(100, 5, "nao_declarado", "",
                        constantes=_constantes_ficticias(), municipios=[])
    ok(not r["classifica"] and r["causa_da_recusa"] == "acelerador_nao_declarado",
       "acelerador `nao_declarado` com potencia e velocidade dentro do limite da "
       "bicicleta classificou em vez de recusar — e o erro permissivo que a ilha "
       "existe para nao cometer: devolveu %r" % (_veredito(r),))

    # E o pivo decide SOZINHO a fronteira bike/autopropelido: mesmos numeros,
    # acelerador diferente, categoria diferente.
    a = f1ref.responder(100, 5, "so_pedal_assistido", "",
                        constantes=_constantes_ficticias(), municipios=[])
    b = f1ref.responder(100, 5, "manual", "",
                        constantes=_constantes_ficticias(), municipios=[])
    ok(a["categoria"] == "bicicleta_eletrica" and b["categoria"] == "autopropelido",
       "o pivo da 1.1 nao esta decidindo: com os mesmos numeros, `so_pedal_assistido` "
       "deu %r e `manual` deu %r" % (a["categoria"], b["categoria"]))

    # A QUARTA SAIDA EXISTE e nao e `ciclomotor`.
    c = f1ref.responder(5000, 120, "manual", "",
                        constantes=_constantes_ficticias(), municipios=[])
    ok(c["categoria"] == "acima_do_ciclomotor",
       "veiculo acima do teto do ciclomotor foi chamado de %r. Os paragrafos 6o e 7o "
       "do art. 2o nao autorizam isso" % (c["categoria"],))

    # A FRASE DO ESTOURO NAO AFIRMA AS DUAS METADES quando so uma estourou — o
    # defeito que o smoke test de regras/f1.py pegou em 06/11/2026.
    so_vel = f1ref.responder(500, 30, "manual", "",
                             constantes=_constantes_ficticias(), municipios=[])
    ok(so_vel["categoria"] == "ciclomotor", "mundo do estouro so por velocidade mudou")
    frase = so_vel["frases_categoria"][0]
    ok("500 W" not in frase,
       "a frase do ciclomotor cita a potencia num mundo em que ela NAO estourou: %r"
       % frase[:140])


def _constantes_ficticias():
    """O arquivo de constantes FABRICADO, com os limiares ficticios.

    Fabricar o mundo e a regra do "produza o mundo" da secao 8: este portao nao
    depende do que dados/constantes.json diz hoje para afirmar a arvore.
    """
    return {
        f1ref.ID_LIMIARES: {
            "status": "publicavel",
            "valor": {k: int(v) for k, v in FICTICIOS.items()},
        },
        f1ref.ID_CONSEQUENCIAS: {
            "status": "publicavel",
            "valor": {
                c: {"registro_licenciamento_emplacamento": exig,
                    "capacete": "nao_consta", "artigo": "art. fictício"}
                for c, exig in (("bicicleta_eletrica", "nao_sujeito"),
                                ("autopropelido", "nao_sujeito"),
                                ("ciclomotor", "exigido"),
                                ("acima_do_ciclomotor", "nao_decidido_por_esta_resolucao"))
            },
        },
        f1ref.ID_HABILITACAO: {"status": "pendente", "valor": None},
    }


# ---------------------------------------------------------------------------
# (B) OS NUMEROS DO MUNDO: a referencia usa o que a CONSTANTE diz.
# ---------------------------------------------------------------------------
def metade_b():
    bruto = json.load(io.open(CONSTANTES, encoding="utf-8"))
    cs = {c["id"]: c for c in bruto["constantes"]}

    c = cs.get(f1ref.ID_LIMIARES)
    ok(c is not None, "a constante dos limiares desapareceu de constantes.json")
    if c is None:
        return

    lim = f1ref.limiares_publicaveis({k: v for k, v in cs.items()})
    if c.get("status") != "publicavel":
        ok(lim is None,
           "a constante esta %r e a referencia devolveu limiares. Constante pendente "
           "dentro de formula publicada e proibida pela secao 10" % c.get("status"))
        print("  a constante dos limiares esta %r: a F1 NAO vai ao ar, e este portao "
              "afirma exatamente isso" % c.get("status"))
        return

    ok(lim is not None, "a constante esta publicavel e a referencia nao devolveu limiares")
    for nome in f1ref.NOMES_DOS_LIMIARES:
        ok(nome in (c.get("valor") or {}),
           "a constante publicavel nao traz o limiar %r, e a arvore o referencia por "
           "nome" % nome)
        if lim and nome in (c.get("valor") or {}):
            ok(lim[nome] == Fraction(str(c["valor"][nome])),
               "a referencia usa %r para %s e a constante diz %r"
               % (lim[nome], nome, c["valor"][nome]))

    # A constante publicavel tem de trazer procedencia: sem url e data, ela e um
    # numero de portal com outro rotulo.
    ok(bool(c.get("url")), "a constante dos limiares esta publicavel SEM `url`")
    ok(bool(c.get("verificado_em")),
       "a constante dos limiares esta publicavel SEM `verificado_em`")
    ok(c.get("tipo") == "oficial",
       "a constante dos limiares esta publicavel com tipo %r. Limiar legal publicavel "
       "so pode ser `oficial`" % c.get("tipo"))

    # A COERENCIA INTERNA DOS LIMIARES, e ela nao e sobre os valores: e sobre a
    # ORDEM. Teto de ciclomotor abaixo do teto de autopropelido faria a terceira
    # perna da arvore ser inalcancavel, e nenhum valor de constante pode fazer
    # isso sem alguem reclamar.
    if lim:
        ok(lim["LIMIAR_CICLOMOTOR_W"] >= lim["LIMIAR_AUTOPROP_W"],
           "o teto de potencia do ciclomotor (%s) ficou ABAIXO do do autopropelido "
           "(%s): a perna do ciclomotor fica inalcancavel"
           % (lim["LIMIAR_CICLOMOTOR_W"], lim["LIMIAR_AUTOPROP_W"]))
        ok(lim["LIMIAR_CICLOMOTOR_KMH"] >= lim["LIMIAR_AUTOPROP_KMH"],
           "o teto de velocidade do ciclomotor (%s) ficou ABAIXO do do autopropelido "
           "(%s)" % (lim["LIMIAR_CICLOMOTOR_KMH"], lim["LIMIAR_AUTOPROP_KMH"]))
        ok(lim["LIMIAR_BIKE_W"] <= lim["LIMIAR_AUTOPROP_W"],
           "o teto da bicicleta (%s) passou do do autopropelido (%s)"
           % (lim["LIMIAR_BIKE_W"], lim["LIMIAR_AUTOPROP_W"]))

    # A HABILITACAO: enquanto a constante for pendente, a pagina CALA — e as
    # duas frases proibidas nao aparecem em texto gerado nenhum.
    hab = cs.get(f1ref.ID_HABILITACAO)
    ok(hab is not None,
       "a constante %r nao existe. Ela e o nome do silencio da F1 sobre CNH; sem ela "
       "o silencio volta a ser lacuna" % f1ref.ID_HABILITACAO)
    if hab is not None and hab.get("status") != "publicavel":
        textos = []
        for k in ("frases_molde",):
            textos += list(json.load(io.open(RESPOSTAS, encoding="utf-8"))[k].values())
        resp = json.load(io.open(RESPOSTAS, encoding="utf-8"))
        ex = resp["resposta_exemplo"]
        textos += ex["frases_categoria"] + ex["frases_municipal"] + ex["frases_ressalva"]
        for linha in (resp.get("tabela_regra") or []):
            textos += [v for v in linha.values() if isinstance(v, str)]
        for t in textos:
            baixo = t.lower()
            ok("dispensa cnh" not in baixo,
               "a frase `dispensa CNH` esta em texto de tela com a constante de "
               "habilitacao em %r: %r" % (hab.get("status"), t[:120]))
            ok("precisa de habilita" not in baixo and "exige habilita" not in baixo,
               "uma frase que AFIRMA habilitacao esta em texto de tela com a constante "
               "em %r: %r" % (hab.get("status"), t[:120]))
        ok(resp["habilitacao_respondida"] is False,
           "o arquivo de respostas declara `habilitacao_respondida: true` com a "
           "constante em %r" % hab.get("status"))
        print("  habilitacao em %r: as frases `dispensa CNH` e `exige habilitacao` "
              "estao PROIBIDAS e ausentes de todo texto de tela" % hab.get("status"))


# ---------------------------------------------------------------------------
# (C) A FRONTEIRA: nenhum literal de limiar dentro de regras/f1.py.
# ---------------------------------------------------------------------------
def metade_c():
    fonte = io.open(FONTE_DA_REFERENCIA, encoding="utf-8").read()

    # Os valores de HOJE, lidos da constante. A afirmacao e sobre o ARQUIVO DE
    # CODIGO, e os numeros proibidos nele sao os que a constante traz — entao
    # esta regua continua certa no dia em que a resolucao trocar os numeros.
    bruto = json.load(io.open(CONSTANTES, encoding="utf-8"))
    cs = {c["id"]: c for c in bruto["constantes"]}
    valores = (cs.get(f1ref.ID_LIMIARES) or {}).get("valor") or {}

    # So o CODIGO entra na regua: o docstring e os comentarios CITAM os numeros
    # de proposito (e onde a leitura oficial esta registrada). A regra da 1.3 e
    # sobre literal numerico dentro da logica.
    codigo = _so_codigo(fonte)

    for nome, v in sorted(valores.items()):
        achados = re.findall(r"(?<![\d.])%d(?![\d.])" % int(v), codigo)
        ok(not achados,
           "regras/f1.py tem o literal %d (valor de %s) dentro do CODIGO. A 1.3 "
           "proibe literal numerico de limiar na logica: ele mora na constante e e "
           "referenciado por nome" % (int(v), nome))

    # E a outra ponta da mesma regra: os moldes de frase nao trazem DIGITO.
    resp = json.load(io.open(RESPOSTAS, encoding="utf-8"))
    for k, molde in resp["frases_molde"].items():
        ok(not re.search(r"\d", molde),
           "o molde %r traz digito: %r. Numero entra por `{}`, do limiar lido ou da "
           "entrada da pessoa — molde com digito e o numero de tela digitado com "
           "outra roupa" % (k, molde[:120]))

    print("  fronteira: %d limiar(es) conferido(s) contra o codigo da referencia e "
          "%d molde(s) sem digito" % (len(valores), len(resp["frases_molde"])))


def _so_codigo(fonte):
    """Tira docstrings e comentarios, deixando o codigo.

    A regua da 1.3 e sobre LOGICA. O cabecalho deste arquivo e o de regras/f1.py
    citam os numeros da resolucao de proposito — e o dia em que citar o numero no
    comentario for proibido e o dia em que ninguem mais consegue registrar o que
    leu. Entao a regua le o codigo e nao o arquivo.
    """
    sem_doc = re.sub(r'""".*?"""', "", fonte, flags=re.S)
    sem_doc = re.sub(r"'''.*?'''", "", sem_doc, flags=re.S)
    linhas = []
    for linha in sem_doc.split("\n"):
        # Comentario de linha inteira sai; comentario no fim de linha de codigo
        # tambem, e o `#` dentro de string nao existe neste arquivo (conferido
        # pela propria varredura: se existisse, o corte faria a regua ficar mais
        # ESTRITA e nao mais frouxa, porque cortaria codigo).
        linhas.append(linha.split("#")[0])
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# (D) A PRESTACAO DE CONTAS DA 1.7, sobre banco FABRICADO.
# ---------------------------------------------------------------------------
def metade_d():
    def reg(id_, **kw):
        base = {"id": id_, "status": "rascunho", "marca": "M", "modelo": id_,
                "potencia_nominal_w": {"valor": None}, "velocidade_max_kmh": {"valor": None},
                "acelerador": {"valor": "nao_declarado"}, "afiliado": {}}
        base.update(kw)
        return base

    # O MUNDO QUE O BANCO DE HOJE NAO TEM: um registro que DECLARA os tres
    # campos e portanto classifica. Sem fabricar este mundo, a vitrine da F1
    # nunca seria exercitada — e a 1.7 inteira passaria por cima de uma lista
    # vazia, que e o teste que mede a si mesmo.
    banco = [
        reg("classifica-na-categoria",
            potencia_nominal_w={"valor": 100}, velocidade_max_kmh={"valor": 5},
            acelerador={"valor": "manual"},
            afiliado={"url_busca": "https://exemplo/x"}),
        reg("classifica-noutra",
            potencia_nominal_w={"valor": 900}, velocidade_max_kmh={"valor": 40},
            acelerador={"valor": "manual"},
            afiliado={"url_busca": "https://exemplo/y"}),
        reg("classifica-sem-link",
            potencia_nominal_w={"valor": 100}, velocidade_max_kmh={"valor": 5},
            acelerador={"valor": "manual"}),
        reg("sem-nominal"),
        reg("excluido", status="excluido_do_banco"),
    ]

    g = f1ref.grupos_de_compra(banco, "autopropelido", FICTICIOS)
    ok([r["id"] for r in g["cabem_na_categoria"]] == ["classifica-na-categoria"],
       "o grupo `cabem_na_categoria` saiu %r" % [r["id"] for r in g["cabem_na_categoria"]])
    ok([r["id"] for r in g["de_outra_categoria"]] == ["classifica-noutra"],
       "o grupo `de_outra_categoria` saiu %r" % [r["id"] for r in g["de_outra_categoria"]])
    ok([r["id"] for r in g["sem_saida_de_compra"]] == ["classifica-sem-link"],
       "o grupo `sem_saida_de_compra` saiu %r" % [r["id"] for r in g["sem_saida_de_compra"]])
    ok([r["id"] for r in g["nao_declaram_nominal"]] == ["sem-nominal"],
       "o grupo `nao_declaram_nominal` saiu %r" % [r["id"] for r in g["nao_declaram_nominal"]])
    ok([r["id"] for r in g["fora_do_banco"]] == ["excluido"],
       "o grupo `fora_do_banco` saiu %r" % [r["id"] for r in g["fora_do_banco"]])
    ok(sum(len(v) for v in g.values()) == len(banco),
       "a prestacao de contas nao fecha o banco fabricado")

    # A ORDEM DAS CAUSAS IMPORTA, e ela e medida: registro que classifica MAS nao
    # tem link cai em `sem_saida_de_compra` e nao em `cabem_na_categoria` — senao
    # a vitrine serviria cartao sem saida de compra, que e o que a 25.2 proibe.
    ok(g["cabem_na_categoria"] and g["cabem_na_categoria"][0].get("afiliado"),
       "um registro sem saida de compra entrou na vitrine")

    # E O NUMERO DO BANCO DE VERDADE, afirmado como e: a soma fecha e a vitrine
    # esta vazia pela causa que o arquivo de respostas declara.
    resp = json.load(io.open(RESPOSTAS, encoding="utf-8"))
    cont = resp["compra"]["contagem"]
    ok(sum(cont.values()) == resp["compra"]["total_registros_veiculos"],
       "a prestacao de contas do arquivo de respostas nao fecha: %s somam %d de %d"
       % (cont, sum(cont.values()), resp["compra"]["total_registros_veiculos"]))
    ok(len(resp["compra"]["vitrine"]) == cont["cabem_na_categoria"],
       "a vitrine tem %d cartoes e o grupo diz %d"
       % (len(resp["compra"]["vitrine"]), cont["cabem_na_categoria"]))
    print("  prestacao de contas do banco de verdade: %s, soma %d de %d registros"
          % (cont, sum(cont.values()), resp["compra"]["total_registros_veiculos"]))

    # A TABELA DO BANCO: nenhuma linha pode trazer categoria sem trazer o watt
    # NOMINAL. Esta e a trava contra a tese da ilha ser desfeita por descuido —
    # o watt sem rotulo virando classificacao.
    for linha in resp["tabela_banco"]["linhas"]:
        if linha["categoria"] is not None:
            ok(linha["watt_nominal"] is not None,
               "a linha %r da tabela tem categoria %r e NAO tem watt nominal: o "
               "numero do anuncio escreveu a regra"
               % (linha["id"], linha["categoria"]))
        else:
            ok(linha["causa_da_recusa"] is not None,
               "a linha %r nao tem categoria e nao diz a causa" % linha["id"])


# ---------------------------------------------------------------------------
# (E) A CAMADA MUNICIPAL: tres estados, tres frases, e ela SEMPRE sai.
# ---------------------------------------------------------------------------
def metade_e():
    # O terceiro estado nao existe no banco de hoje (os quatro municipios sao
    # `pendente`), entao ele e FABRICADO. Sem isso, a unica frase que o banco de
    # hoje exercita e a generica, e o ramo do municipio LIDO iria ao ar sem
    # nunca ter sido medido.
    municipios = [
        {"id": "campinas", "nome": "Campinas", "status": "pendente",
         "limite_velocidade_kmh": 20},
        {"id": "cidade-lida", "nome": "Cidade Lida", "status": "publicavel",
         "limite_velocidade_kmh": 25},
    ]
    cs = _constantes_ficticias()

    casos = [
        ("", "municipal_generica"),
        ("Campinas", "municipal_conhecido_pendente"),
        ("Cidade Lida", "municipal_conhecido"),
        ("Osasco", "municipal_desconhecido"),
    ]
    for entrada, esperado in casos:
        r = f1ref.responder(100, 5, "manual", entrada, constantes=cs, municipios=municipios)
        ok(r["estado_municipal"] == esperado,
           "municipio %r deu o estado %r e devia dar %r"
           % (entrada, r["estado_municipal"], esperado))
        ok(len(r["frases_municipal"]) == 1 and r["frases_municipal"][0].strip(),
           "a camada 2 saiu vazia para o municipio %r — e a 1.2 manda que ela seja "
           "SEMPRE impressa" % entrada)

    # As quatro frases sao DIFERENTES: estado que o codigo separa, o texto separa.
    frases = set()
    for entrada, _ in casos:
        r = f1ref.responder(100, 5, "manual", entrada, constantes=cs, municipios=municipios)
        frases.add(r["frases_municipal"][0])
    ok(len(frases) == len(casos),
       "os %d estados da camada 2 produziram so %d frase(s) distinta(s): causa que o "
       "codigo separa e o texto funde" % (len(casos), len(frases)))

    # E A CAMADA 2 SAI TAMBEM NA RECUSA. Uma F1 que recusa classificar e cala
    # sobre a rua devolve menos do que pode: a rua nao depende da categoria.
    r = f1ref.responder(None, None, "nao_declarado", "Osasco",
                        constantes=cs, municipios=municipios)
    ok(r["frases_municipal"] and r["frases_municipal"][0].strip(),
       "a camada 2 nao saiu numa resposta de RECUSA")
    print("  camada municipal: %d estados, %d frases distintas, e ela sai tambem na "
          "recusa" % (len(casos), len(frases)))


# ---------------------------------------------------------------------------
# (F) AS MUTACOES: o portao tem de MORDER.
# ---------------------------------------------------------------------------
def metade_f():
    """Refaz a arvore ESTRAGADA de quatro jeitos e exige que a metade (A) pegue.

    Sem esta metade, as afirmacoes acima sao verdadeiras e nao sao medicao: um
    portao que nunca viu vermelho nao prova que ficaria vermelho.
    """
    # A GRADE DESTA VARREDURA PASSA PELOS LIMIARES EXATOS, E ISSO FOI ACHADO
    # PELO PROPRIO PORTAO EM 06/11/2026. A primeira versao dela usava
    # (100, 556, 778, 1000, 5000) x (5, 12, 23, 45, 120) — nenhum desses valores
    # e IGUAL a um limiar, e a mutacao de fronteira (`<` no lugar de `<=`) so
    # muda o veredito do veiculo que esta EXATAMENTE no limite. Resultado: a
    # mutacao passava, e o portao dizia que a bateria mordia quando ela nao
    # morde. Mutacao que nunca foi exercitada no mundo em que ela importa e
    # afirmacao sobre o portao, nao medicao dele.
    #
    # Os valores sao DERIVADOS dos limiares ficticios, nunca digitados: o dia em
    # que alguem trocar os ficticios, a grade acompanha sozinha.
    _LIM_W = sorted({int(FICTICIOS[k]) for k in FICTICIOS if k.endswith("_W")})
    _LIM_KMH = sorted({int(FICTICIOS[k]) for k in FICTICIOS if k.endswith("_KMH")})
    GRADE_W = [None, 0] + sorted({v + d for v in _LIM_W for d in (-1, 0, 1)}) + [99999]
    GRADE_KMH = [None, 0] + sorted({v + d for v in _LIM_KMH for d in (-1, 0, 1)}) + [999]

    def varre(arvore):
        """Roda a varredura da metade (A) contra uma arvore de mentira."""
        for w in GRADE_W:
            for kmh in GRADE_KMH:
                for acel in (None, "manual", "so_pedal_assistido", "nao_declarado"):
                    if arvore(w, kmh, acel, FICTICIOS) != arvore_a_mao(
                            w, kmh, acel, FICTICIOS):
                        return True
        return False

    def sem_pivo(w, kmh, acel, lim):
        """MUTACAO 1: o acelerador deixa de decidir (o erro permissivo)."""
        if lim is None:
            return "recusa:limiar_legal_pendente"
        if w is None:
            return "recusa:potencia_nominal_ausente"
        if kmh is None:
            return "recusa:velocidade_max_ausente"
        if Fraction(str(w)) <= 0 or Fraction(str(kmh)) <= 0:
            return "recusa:entrada_nao_positiva"
        if (Fraction(str(w)) <= lim["LIMIAR_BIKE_W"]
                and Fraction(str(kmh)) <= lim["LIMIAR_BIKE_KMH"]):
            return "bicicleta_eletrica"
        return "autopropelido"

    def fronteira_estrita(w, kmh, acel, lim):
        """MUTACAO 2: `<` no lugar de `<=` — o veiculo EXATAMENTE no limite."""
        if lim is None or acel in (None, "nao_declarado"):
            return arvore_a_mao(w, kmh, acel, lim)
        if w is None or kmh is None:
            return arvore_a_mao(w, kmh, acel, lim)
        pot, vel = Fraction(str(w)), Fraction(str(kmh))
        if pot <= 0 or vel <= 0:
            return "recusa:entrada_nao_positiva"
        if (acel == "so_pedal_assistido" and pot < lim["LIMIAR_BIKE_W"]
                and vel < lim["LIMIAR_BIKE_KMH"]):
            return "bicicleta_eletrica"
        if pot < lim["LIMIAR_AUTOPROP_W"] and vel < lim["LIMIAR_AUTOPROP_KMH"]:
            return "autopropelido"
        if pot < lim["LIMIAR_CICLOMOTOR_W"] and vel < lim["LIMIAR_CICLOMOTOR_KMH"]:
            return "ciclomotor"
        return "acima_do_ciclomotor"

    def nominal_por_pico(w, kmh, acel, lim):
        """MUTACAO 3: potencia ausente deixa de recusar e vira zero."""
        if w is None:
            return arvore_a_mao(0.0001, kmh, acel, lim)
        return arvore_a_mao(w, kmh, acel, lim)

    def ordem_trocada(w, kmh, acel, lim):
        """MUTACAO 4: a potencia e cobrada ANTES do pivo (muda a causa)."""
        if lim is None:
            return "recusa:limiar_legal_pendente"
        if w is None:
            return "recusa:potencia_nominal_ausente"
        if acel is None or acel == "nao_declarado":
            return "recusa:acelerador_nao_declarado"
        return arvore_a_mao(w, kmh, acel, lim)

    mutacoes = (("o acelerador deixa de ser pivo", sem_pivo),
                ("`<` no lugar de `<=` na fronteira", fronteira_estrita),
                ("potencia ausente vira zero em vez de recusar", nominal_por_pico),
                ("a ordem das recusas troca", ordem_trocada),
                ("a arvore VELHA, de tres saidas", arvore_VELHA_de_tres_saidas))
    for nome, m in mutacoes:
        ok(varre(m),
           "a mutacao %r NAO foi pega pela varredura: o portao nao morde nela" % nome)
    print("  mutacoes: %d, e a varredura pegou todas" % len(mutacoes))


# ---------------------------------------------------------------------------
# (G) AS DUAS CONTAS QUE O PORTAO NAO TINHA E QUE FORAM AO AR ERRADAS.
#
# As duas nasceram em 06/11/2026, depois de o texto gerado ser LIDO. Nenhuma
# delas quebrava nada, e e exatamente por isso que elas chegaram ao ar: codigo
# que converte errado roda, e frase com plural errado imprime.
# ---------------------------------------------------------------------------
def metade_g():
    # (1) MILIMETRO PARA CENTIMETRO, e a regua esta escrita DO OUTRO LADO: em vez
    # de repetir a divisao da referencia (o que aprovaria o erro dela), o portao
    # multiplica de volta e exige fechar. A primeira versao da referencia dividia
    # por CEM nos TRES lugares que convertem, e a pagina foi ao ar dizendo "7 cm
    # de largura" onde a resolucao diz 70.
    bruto = json.load(io.open(CONSTANTES, encoding="utf-8"))
    cs = {c["id"]: c for c in bruto["constantes"]}
    valor = (cs.get(f1ref.ID_LIMIARES) or {}).get("valor") or {}
    for nome in ("LIMIAR_AUTOPROP_LARGURA_MM", "LIMIAR_AUTOPROP_ENTRE_EIXOS_MM"):
        if nome not in valor:
            continue
        mm = Fraction(str(valor[nome]))
        cm_tela = f1ref._mm_para_cm(mm)
        # desfaz a formatacao de tela e multiplica de volta
        cm = Fraction(cm_tela.replace(".", "").replace(",", "."))
        ok(cm * 10 == mm,
           "a conversao de %s esta errada: %s mm viraram %s cm na tela, e %s cm sao "
           "%s mm. A pagina publica centimetro e a constante guarda milimetro"
           % (nome, mm, cm_tela, cm_tela, cm * 10))

    # (2) O PLURAL DA CONTAGEM, nos DOIS mundos, e o do ZERO e o de hoje. Um molde
    # so servia "e 0 declaram o nominal" — o plural que mente, a cicatriz que a
    # clubedomosaico pagou em 12/10/2026. O mundo com nominal e FABRICADO: o banco
    # de hoje nao o tem, e sem fabrica-lo o molde dele iria ao ar nao medido.
    cs_f = _constantes_ficticias()
    cs_f[f1ref.ID_WATT_SEM_ROTULO] = {"status": "publicavel", "valor": "Titulo de teste"}
    frases = {}
    for rotulo, com_nominal in (("zero", 0), ("algum", 3)):
        r = f1ref.responder(100, 5, "manual", "", constantes=cs_f, municipios=[],
                            contagem_de_fichas={"colhidos": 14, "sem_rotulo": 13,
                                                "com_nominal": com_nominal})
        pico = [f for f in r["frases_ressalva"] if "NOMINAL" in f]
        ok(len(pico) == 1,
           "o mundo %r produziu %d ressalva(s) do pico e tinha de produzir 1"
           % (rotulo, len(pico)))
        frases[rotulo] = pico[0] if pico else ""

    ok(frases["zero"] != frases["algum"],
       "os dois mundos da contagem produziram a MESMA frase: causa que o codigo "
       "separa e o texto funde")
    ok("NENHUM declara" in frases["zero"],
       "o mundo de ZERO nominal nao diz `NENHUM declara`: %r" % frases["zero"][:160])
    ok(" 0 declaram" not in frases["zero"] and " 0 deles" not in frases["zero"],
       "o mundo de ZERO nominal serve o plural que mente: %r" % frases["zero"][:160])
    ok("3 declaram o nominal" in frases["algum"],
       "o mundo COM nominal nao traz a contagem: %r" % frases["algum"][:160])

    # (3) SEM CONTAGEM A RESSALVA NAO SAI. Frase que cita uma contagem sem a
    # contagem e o numero de tela digitado esperando a vez.
    r = f1ref.responder(100, 5, "manual", "", constantes=cs_f, municipios=[],
                        contagem_de_fichas=None)
    ok(not [f for f in r["frases_ressalva"] if "NOMINAL" in f],
       "a ressalva do pico saiu SEM a contagem")

    # (4) E NENHUM MOLDE PODE TRAZER QUANTIFICADOR POR EXTENSO. A classe que esta
    # ilha paga desde 03/11/2026, e o portao de ar a achou na primeira versao do
    # molde do pico (`costuma`) no minuto em que a pagina subiu. Aqui ela e barrada
    # ANTES do ar.
    resp = json.load(io.open(RESPOSTAS, encoding="utf-8"))
    proibidos = ("costuma", "geralmente", "normalmente", "a maioria", "quase sempre",
                 "quase nunca", "na maior parte", "o mais comum", "mais comum",
                 "em geral", "tipicamente", "raramente")
    for k, molde in resp["frases_molde"].items():
        baixo = molde.lower()
        for t in proibidos:
            ok(t not in baixo,
               "o molde %r traz o quantificador por extenso %r, e ele vai para a tela "
               "sem camada de liberacao nenhuma: %r" % (k, t, molde[:140]))
    print("  as duas contas que foram ao ar erradas: conversao mm->cm conferida do "
          "outro lado, e os dois mundos do plural fabricados")


# ---------------------------------------------------------------------------
# (H) A PRESTACAO DE CONTAS E RENDERIZADA NO SERVIDOR E O VEREDITO RECOMPUTA NO
#     NAVEGADOR — E HOJE ISSO NAO SE CONTRADIZ PORQUE O BANCO ESTA VAZIO.
#
# Esta e a 32.5-d em forma nova, e ela e PRE-REGISTRADA e nao achada: *"a regra
# que nunca rodou contra o dado de verdade esta quebrada e parece sa, e o espaco
# reservado e quem a esconde"*. Lá o reservado escondia a disputa de
# especificidade; aqui o que esconde e o banco com ZERO registro classificavel.
#
# O MECANISMO: a secao "Quem entrou, quem nao entrou, e por que" sai do PHP,
# calculada para a categoria da RESPOSTA DE EXEMPLO. Quando a pessoa troca os
# campos, o JS reescreve a caixa, a camada 2 e as ressalvas — e NAO reescreve a
# prestacao de contas. Hoje isso nao mente, porque NENHUM dos 14 registros
# classifica e portanto os grupos saem IDENTICOS para as quatro categorias. **No
# dia em que um registro declarar os tres campos, a secao passa a falar da
# categoria do exemplo enquanto a caixa fala da categoria da pessoa.**
#
# A AFIRMACAO E O INVARIANTE, e nao a promessa: enquanto a secao for do servidor
# e a caixa for do navegador, os grupos TEM de ser independentes da categoria. O
# dia em que esta afirmacao ficar VERMELHA e exatamente o dia em que o JS precisa
# passar a recomputar a secao — o portao nao avisa que vai quebrar, ele quebra
# junto com o mundo.
# ---------------------------------------------------------------------------
def metade_h():
    bruto = json.load(io.open(CONSTANTES, encoding="utf-8"))
    cs = {c["id"]: c for c in bruto["constantes"]}
    lim = f1ref.limiares_publicaveis(cs)
    with io.open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
        regs = json.load(f)["registros"]

    por_categoria = {}
    for cat in f1ref.CATEGORIAS:
        g = f1ref.grupos_de_compra(regs, cat, lim)
        por_categoria[cat] = {k: sorted(r.get("id") for r in v) for k, v in g.items()}

    primeiro = por_categoria[f1ref.CATEGORIAS[0]]
    iguais = all(por_categoria[c] == primeiro for c in f1ref.CATEGORIAS)
    ok(iguais,
       "OS GRUPOS DA PRESTACAO DE CONTAS JA DEPENDEM DA CATEGORIA, e a secao que os "
       "publica e renderizada no SERVIDOR para a categoria do EXEMPLO enquanto a caixa "
       "de resposta recomputa no NAVEGADOR. A partir de agora a pagina diz, na mesma "
       "tela, a prestacao de contas de uma categoria e o veredito de outra. O conserto "
       "e o JS passar a reescrever a secao, pelos mesmos grupos. Contagens por "
       "categoria: %s"
       % {c: {k: len(v) for k, v in d.items()} for c, d in por_categoria.items()})

    if iguais:
        print("  prestacao de contas INDEPENDENTE da categoria em %d de %d categorias — "
              "e e por isso que a secao pode ser do servidor enquanto a caixa e do "
              "navegador. Quando esta linha ficar vermelha, o JS tem de recomputa-la"
              % (len(f1ref.CATEGORIAS), len(f1ref.CATEGORIAS)))


# ---------------------------------------------------------------------------
# (I) A FRASE DE ABERTURA DA VITRINE CITAVA UMA CONTAGEM COM UM QUANTIFICADOR, E
#     ELA FOI AO AR FALSA — medido na home em 09/11/2026, pela lente do defeito
#     de 06/11 (prosa que promete uma conta e nao a fecha).
#
# O QUE ESTAVA NO AR: *"nenhum dos 14 anuncios que a gente colheu declara a
# potencia NOMINAL. TODOS declaram um watt sem dizer se e nominal ou de pico"*.
# A primeira metade era verdadeira; a segunda era FALSA — dos 14, treze
# declaravam watt e UM (a ficha PLAYBIK) nao declarava watt nenhum. E a pagina
# se contradizia duas vezes na MESMA tela: a ressalva do pico dizia `13`,
# contada do banco pelo gerador, e a TABELA imprimia "nao declara" na linha do
# PLAYBIK. Quem lesse a pagina inteira via tres respostas para uma contagem.
#
# POR QUE NENHUM PORTAO VIU, e e a licao de metodo: a regua de quantificador por
# extenso da metade (G) le `frases_molde`, e esta frase nasce INLINE no
# `gerar-f1.py`, fora daquela lista. `todos` tambem nao estava entre os
# proibidos. Portao que mede uma lista de moldes nao alcanca a frase que nao e
# molde — e a frase que nao e molde e justamente a que ninguem reconferiu.
#
# ESTA METADE MEDE AS DUAS PONTAS: fabrica os tres mundos da frase (nenhum deles
# e o de hoje por acidente) e exige que a frase SERVIDA seja refabricavel do
# banco, byte por byte.
def _grupos_fabricados(wattless, com_watt):
    """Grupos com `nao_declaram_nominal` montado a dedo, para fabricar mundo."""
    g = {"cabem_na_categoria": [], "de_outra_categoria": [],
         "nao_declaram_nominal": [], "sem_saida_de_compra": [], "fora_do_banco": []}
    for i in range(com_watt):
        g["nao_declaram_nominal"].append(
            {"id": "com-watt-%d" % i,
             "potencia_declarada_sem_rotulo_w": {"valor": 500}})
    for i in range(wattless):
        g["nao_declaram_nominal"].append(
            {"id": "sem-watt-%d" % i,
             "potencia_declarada_sem_rotulo_w": {"valor": None}})
    return g


def metade_i():
    gen = _carregar_gerador()
    frase = gen.frase_do_bloco_de_compra

    # OS TRES MUNDOS, e nenhum deles e escolhido pela intencao: a contagem
    # escolhe. O mundo do meio e o de hoje (13 com watt, 1 sem).
    mundos = {
        "todos com watt": (0, 14),
        "misto": (1, 13),
        "nenhum com watt": (14, 0),
    }
    saiu = {}
    for rotulo, (wattless, com_watt) in mundos.items():
        saiu[rotulo] = frase(_grupos_fabricados(wattless, com_watt), "autopropelido")

    ok(len(set(saiu.values())) == 3,
       "os tres mundos da frase de abertura nao produziram tres frases distintas: "
       "causa que a contagem separa e o texto funde — %r" % saiu)

    ok("Os 14 declaram um watt" in saiu["todos com watt"]
       and "watt nenhum" not in saiu["todos com watt"],
       "o mundo em que TODOS declaram watt sem rotulo nao traz a contagem, ou "
       "inventa um resto que nao existe: %r" % saiu["todos com watt"][:200])

    ok("13 declaram um watt" in saiu["misto"]
       and "o outro não declara watt nenhum" in saiu["misto"],
       "o mundo MISTO — o de hoje — nao nomeia as duas contagens: %r"
       % saiu["misto"][:220])

    ok("watt nenhum" in saiu["nenhum com watt"]
       and " 0 declara" not in saiu["nenhum com watt"],
       "o mundo em que NENHUM declara watt serve o plural que mente (a cicatriz "
       "da clubedomosaico de 12/10/2026): %r" % saiu["nenhum com watt"][:200])

    # E NENHUM DOS TRES PODE TRAZER QUANTIFICADOR POR EXTENSO. A classe que esta
    # ilha paga desde 03/11/2026, com `todos` acrescentado em 09/11 porque foi
    # ele que foi ao ar falso. Esta lista e mais larga que a da metade (G) de
    # proposito: aqui a frase fala de uma contagem que a pagina TEM medida, e
    # entao quantificador nenhum tem desculpa.
    proibidos = ("todos", "todas", "costuma", "geralmente", "normalmente",
                 "a maioria", "quase sempre", "quase nunca", "na maior parte",
                 "o mais comum", "mais comum", "em geral", "tipicamente",
                 "raramente", "varios", "vários", "alguns", "muitos")
    for rotulo, f in saiu.items():
        baixo = f.lower()
        for t in proibidos:
            ok(t not in baixo,
               "a frase de abertura do mundo %r traz o quantificador por extenso "
               "%r onde a pagina TEM a contagem medida: %r" % (rotulo, t, f[:180]))

    # E A PONTA QUE PROVA: a frase SERVIDA e refabricavel do banco. Sem isto os
    # tres mundos acima poderiam estar certos com o JSON no ar trazendo outra
    # coisa — que e exatamente o que aconteceu em 06/11 e 09/11.
    bruto = json.load(io.open(CONSTANTES, encoding="utf-8"))
    cs = {c["id"]: c for c in bruto["constantes"]}
    lim = f1ref.limiares_publicaveis(cs)
    with io.open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as fh:
        regs = json.load(fh)["registros"]
    servido = json.load(io.open(RESPOSTAS, encoding="utf-8"))
    cat = (servido.get("resposta_exemplo") or {}).get("categoria")
    refeita = frase(f1ref.grupos_de_compra(regs, cat, lim), cat)
    no_ar = (servido.get("compra") or {}).get("frase_de_abertura")
    ok(no_ar == refeita,
       "a frase de abertura SERVIDA nao e refabricavel do banco — servida %r, "
       "refeita do banco %r" % ((no_ar or "")[:170], refeita[:170]))

    print("  frase de abertura da vitrine: 3 mundos fabricados, %d quantificador(es) "
          "barrado(s) por mundo, e a frase servida refeita do banco" % len(proibidos))


def main():
    print("PORTAO DA F1 — RODAMETRIA (limiares FICTICIOS na arvore, pela 1.6)")
    metade_a()
    metade_b()
    metade_c()
    metade_d()
    metade_e()
    metade_f()
    metade_g()
    metade_h()
    metade_i()

    print()
    print("teste-f1: %d afirmacoes, %d falha(s)" % (AFIRMACOES[0], len(FALHAS)))
    for f in FALHAS[:40]:
        print("  FALHA", f)
    if len(FALHAS) > 40:
        print("  ... e mais %d" % (len(FALHAS) - 40))
    print("REPROVADO" if FALHAS else "APROVADO")
    return 1 if FALHAS else 0


if __name__ == "__main__":
    sys.exit(main())

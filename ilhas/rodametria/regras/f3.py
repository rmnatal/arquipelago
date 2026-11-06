#!/usr/bin/env python3
"""
F3 — "AGUENTA O MEU PESO?" — A REFERENCIA.

Este arquivo e o CEREBRO da F3: entrada -> resposta inteira, ja em frase
acentuada. O snippet PHP que vai ao ar e TRADUTOR dele, frase a frase, como a
Robometria faz entre cobertura-r1.py e robometria-r1.php e como a F1 e a F2
desta ilha fazem. O motivo esta na secao 8 do ARQUIPELAGO.md: quem confere
escreve a propria regua, e a regua da DECISAO se escreve duas vezes de
proposito — e o que e FATO EXTERNO (os valores das constantes) mora num lugar
so, que aqui e dados/constantes.json, lido e nunca digitado.

A COISA MAIS IMPORTANTE DESTA FERRAMENTA, E ELA SEPARA A F3 DAS DUAS IRMAS: A
RESPOSTA PRINCIPAL NAO DEPENDE DO BANCO. Dado o peso de quem pilota e o que ele
carrega, a F3 devolve QUANTOS KG DE CARGA MAXIMA A PESSOA PRECISA PROCURAR —
`peso_total x (1 + margem)` —, e isso e aritmetica sobre a entrada da pessoa
mais UMA constante. Nenhum registro do banco participa. A vitrine e a prestacao
de contas vem depois, e sao a segunda camada.

ISSO NAO E DETALHE DE ENGENHARIA: e a razao de esta ferramenta poder ir ao ar
hoje. Em 06/11/2026 o banco desta ilha tem 14 veiculos nao excluidos e TRES
declaram `carga_max_kg` — os tres em 120 kg, os tres lidos em ficha de varejo
grande (nivel 5, que e o piso que a 3.5 da especificacao exige para este
campo) — e NENHUM dos tres tem saida de compra. A F1 foi ao ar hoje de manha
com a vitrine VAZIA e a pagina dizendo por que, com os nomes contados; a F3
nasce com a vitrine vazia pelo MESMO desenho e com a resposta principal
INTEIRA, porque a pergunta "de quanto eu preciso" nao espera o mercado.

O QUE ESTA REFERENCIA SE RECUSA A FAZER, e esta e a metade que a 3.5 da
especificacao escreve com todas as letras:

  - NAO estima carga maxima de veiculo que nao a declara. Sem `carga_max_kg`, o
    veiculo vai para um grupo com nome proprio — "nao declara carga maxima" — e
    nao entra na vitrine. Estimar por aro, por potencia ou por "parece
    reforcado" e inventar dado.
  - NAO fala de garupa, carona nem bagageiro: o bloco 1 nao mediu nada disso.
  - NAO devolve lista vazia em silencio. Lista vazia imprime A CAUSA QUE A
    PAGINA MEDIU — e o numero dela e CONTADO do banco (`maior_teto_do_banco`),
    nunca lido da constante de mercado. A propria constante
    `teto-de-carga-do-mercado-brasileiro` diz isso de si mesma: "NAO entra em
    formula... existe para a tela ... com X CONTADO no banco, e nao digitado".
  - NAO atribui a margem a ninguem. Ela e `decisao_da_ilha`, e a constante
    carrega a busca limpa que NEGOU a fonte de terceiro que o bloco 1 supunha.

E A DECISAO MORA EM FUNCAO PURA, fora do laco que varre o banco: `grupo_do_veiculo()`
recebe a carga maxima, o peso total e a margem, e devolve o grupo. A bancada a
chama direto — com o veiculo exatamente no limite, exatamente na margem, um
grama acima e um grama abaixo — e nenhum desses mundos depende do banco de hoje.
E o "produza o mundo" da secao 8, e nesta ilha ele e obrigatorio: o mundo em que
um veiculo tem carga declarada E oferta aberta NAO EXISTE no banco de hoje, e so
a mutacao que o PRODUZ consegue enxergar a vitrine funcionando.
"""

import json
import os
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)   # regras/ fica na raiz da ilha; ver regras/LEIA.md

# Os tres grupos da 3.2, na ORDEM EM QUE A PAGINA OS SERVE. A ordem e regra e
# nao arrumacao: a 3.2 e literal — o grupo do meio "nunca aparece em primeiro
# lugar", porque a secao 7 chama de defeito GRAVE recomendar em primeiro lugar
# um produto que a propria pagina diz nao servir.
GRUPOS_EM_ORDEM = ("folga", "no_limite", "nao_aguenta")

# Nome da constante de cada fato externo. O NUMERO NUNCA aparece neste arquivo.
CONSTANTE_DA_MARGEM = "margem-de-carga-f3"
CONSTANTE_DA_RESSALVA = "ressalva-desempenho-perto-do-teto-de-carga"
CONSTANTE_DO_TETO_DE_MERCADO = "teto-de-carga-do-mercado-brasileiro"


# --------------------------------------------------------------------------
# OS MOLDES DE FRASE, NUM LUGAR SO.
#
# A pagina responde em DOIS lugares: o HTML pre-renderizado (que o PHP serve e
# que a IA le sem preencher formulario) e a recomputacao no navegador quando a
# pessoa troca um campo. Se cada um escrevesse a propria frase, a pagina diria
# duas coisas diferentes para a mesma entrada, e nenhum portao veria.
#
# Entao o molde e FATO EXTERNO as duas metades: mora aqui, viaja inteiro para
# dados/f3-respostas.json, e o navegador o preenche. O que continua escrito
# duas vezes de proposito e a DECISAO — qual molde vale em cada mundo.
# --------------------------------------------------------------------------

MOLDES = {
    # A RESPOSTA PRINCIPAL, e ela nao depende do banco.
    "precisa": (
        "Você e o que carrega dão {total} kg. Procure um que declare pelo menos "
        "{minimo} kg de carga máxima."
    ),
    "precisa_sem_carga": (
        "Com {piloto} kg, procure um que declare pelo menos {minimo} kg de carga "
        "máxima."
    ),
    # A margem, dita como escolha desta ilha e nunca atribuida a terceiro (3.3).
    "margem": (
        "Os {minimo} kg são os seus {total} kg mais uma folga de {pct}% — "
        "critério nosso, não de norma: quem compra um que não aguenta o peso "
        "perde o veículo e pode se machucar, e quem compra com folga paga um "
        "pouco mais."
    ),
    "rotulo_precisa": "A carga máxima que você precisa",
    # Os tres grupos da 3.2.
    "titulo_folga": "Aguentam com folga",
    "titulo_no_limite": "Passam, mas no limite",
    "titulo_nao_aguenta": "Não aguentam o seu peso",
    "titulo_sem_carga": "Não declaram carga máxima",
    "titulo_sem_compra": "Declaram a carga e não têm oferta aberta",
    # DOIS ROTULOS PARA OS MESMOS NOMES, e eles sao dois porque os dois blocos
    # os mostram por motivos diferentes: na RESPOSTA, a carga que cada um
    # declara; na PRESTACAO DE CONTAS, a conta que fecha os 17 registros. Dois
    # blocos com o MESMO titulo leem como a pagina se repetindo, e isso foi
    # medido no ar em 06/11/2026 LENDO A PAGINA, junto com a duplicata do
    # paragrafo de causa que saia nos dois lugares.
    "titulo_aguentam_sem_link": "Aguentam o seu peso, e ainda não têm link de loja",
    # A ressalva SOURCED do grupo do meio (3.4), com o publicador nomeado.
    "ressalva_no_limite": (
        "Quem fica perto do teto declarado costuma não alcançar a velocidade e a "
        "aceleração máximas que o fabricante anuncia — é o que dizem a "
        "espanhola RACE e o brasileiro my-best, que fala em evitar sobrecarga no "
        "motor. Perto do limite, o peso não derruba só a carga: derruba os km."
    ),
    # Cada veiculo, na linha dele.
    "linha_folga": "{nome} declara {carga} kg — {sobra} kg acima do que você precisa.",
    "linha_no_limite": (
        "{nome} declara {carga} kg: até aguenta os seus {total} kg, mas sem a folga "
        "de {pct}% que a gente pede."
    ),
    "linha_nao_aguenta": (
        "{nome} declara {carga} kg — faltam {faltam} kg só para alcançar o seu peso."
    ),
    # A LISTA VAZIA NOMEIA A CAUSA QUE A PAGINA MEDIU (3.5), com o numero CONTADO.
    #
    # E SAO TRES CAUSAS E NAO UMA, porque os consertos sao diferentes e porque a
    # primeira versao desta frase MENTIU. Ela dizia, com um molde so, que
    # "nenhum dos 3 veiculos que declaram carga maxima aguenta os seus 108 kg
    # com folga" — e os tres declaram 120 kg, que cobre com folga os 119 que a
    # regra pede para 108. O que esvaziava a vitrine nao era a CARGA: era a
    # falta de oferta aberta, que e outro eixo. Afirmacao sobre o estado do
    # banco escrita num molde unico e a familia do numero de tela digitado, e
    # foi achada do mesmo jeito que a conversao de milimetro da F1 em 06/11 —
    # LENDO A FRASE QUE SAIU, nao o codigo que a escreve.
    "vazio_por_carga": (
        "Nenhum dos {quantos} veículos com carga declarada e oferta aberta no nosso "
        "banco aguenta os seus {total} kg com folga: o maior teto que temos declarado "
        "é de {teto} kg. Não estimamos a carga de quem não a declara, então aqui a "
        "gente prefere dizer que não tem do que apontar um que talvez não sirva."
    ),
    "vazio_por_falta_de_oferta": (
        "{quantos_servem} dos {quantos} veículos que declaram carga máxima no nosso "
        "banco aguentariam os seus {total} kg com folga — e nenhum deles tem oferta "
        "aberta hoje. Não montamos vitrine com item sem link de loja, porque o botão "
        "que não leva a lugar nenhum é pior que a ausência dele. Os nomes estão "
        "logo abaixo, com a carga de cada um."
    ),
    "vazio_sem_nenhum": (
        "Nenhum veículo do nosso banco declara carga máxima hoje, então não há o "
        "que comparar com os seus {total} kg. O campo exige ficha de varejo grande "
        "para entrar aqui, e estimar carga por tamanho de roda ou por potência "
        "seria inventar o número que esta página existe para dar."
    ),
    # O convite para a F2, com o peso ja passado na URL (3.4 e 32.2).
    "convite_f2": (
        "Perto do limite o peso também come os km: a conta de autonomia aceita o "
        "seu peso e devolve a faixa do seu trajeto."
    ),
    # A frase do teto de mercado, dita como observacao datada e nunca como limite.
    "teto_de_mercado": (
        "Para calibrar a expectativa: na faixa que vimos no varejo brasileiro em "
        "outubro de 2026, a carga máxima declarada ia de 115 a 140 kg, com {teto} kg "
        "sendo o valor que mais se repetia. É o que observamos numa data, não um "
        "limite do mercado — e por isso a conta acima compara o seu peso com a "
        "ficha de cada veículo, nunca com esse número."
    ),
}


def carregar_constantes(caminho=None):
    """Le dados/constantes.json e devolve {id: registro}."""
    caminho = caminho or os.path.join(ILHA, "dados", "constantes.json")
    with open(caminho, encoding="utf-8") as f:
        bruto = json.load(f)
    return {c["id"]: c for c in bruto["constantes"]}


def constante_publicavel(constantes, cid):
    """Devolve o valor SO se a constante estiver publicavel; senao None.

    O status e LIDO do arquivo. Nenhuma lista de pendencias e escrita dentro
    deste codigo, porque lista escrita a mao envelhece calada no dia em que a
    constante destrava — foi exatamente assim que a F1 destravou em 06/11/2026,
    editando um objeto JSON e sem uma linha de logica mudar.
    """
    c = constantes.get(cid)
    if not c or c.get("status") != "publicavel":
        return None
    return c.get("valor")


def margem(constantes):
    """A folga, em FRACAO (0,10 e nao 10). Devolve (fracao, pct_inteiro) ou (None, None).

    A constante guarda o numero em POR CENTO (`valor: 10`, `unidade: "por cento
    acima do peso total"`), e e por isso que esta funcao converte num lugar so:
    dividir por cem espalhado pelo codigo e a familia da conversao de milimetro
    para centimetro que a F1 errou nos tres lugares que convertiam, em 06/11.
    """
    pct = constante_publicavel(constantes, CONSTANTE_DA_MARGEM)
    if pct is None:
        return None, None
    fr = Fraction(str(pct)) / 100
    return fr, pct


# --------------------------------------------------------------------------
# A CONTA. Duas funcoes puras, e as duas sao fabricaveis sem tocar no banco.
# --------------------------------------------------------------------------

def peso_total(peso_piloto_kg, carga_kg=0):
    """Soma, em Fraction, para a bancada poder discordar sem erro de float."""
    p = Fraction(str(peso_piloto_kg))
    c = Fraction(str(carga_kg or 0))
    if p <= 0:
        raise ValueError("peso_piloto_kg tem de ser positivo")
    if c < 0:
        raise ValueError("carga_kg nao pode ser negativa")
    return p + c


def carga_minima_com_folga(total, margem_fr):
    """A RESPOSTA PRINCIPAL DA F3, e ela nao toca o banco.

    `total x (1 + margem)`. Quem arredonda e a tela, uma vez, no fim — e o
    arredondamento da tela e para CIMA, por `_teto()`, porque arredondar para
    baixo uma carga minima recomendada devolve um numero MENOR do que a regra
    pede, e o erro caro desta ferramenta e o permissivo.
    """
    if margem_fr is None:
        raise ValueError("a margem nao esta publicavel; a conta nao sai")
    return Fraction(str(total)) * (1 + margem_fr)


def grupo_do_veiculo(carga_max_kg, total, margem_fr):
    """A DECISAO, em funcao pura. Devolve um dos tres nomes de GRUPOS_EM_ORDEM.

    A 3.2 da especificacao, literal:
      folga       -> carga_max >= total x (1 + margem)
      no_limite   -> total <= carga_max, e abaixo da margem
      nao_aguenta -> total > carga_max

    O veiculo EXATAMENTE na margem entra em `folga` (o `>=` e da propria
    especificacao) e o EXATAMENTE no teto entra em `no_limite` (o `<=` tambem).
    As duas fronteiras tem mundo proprio na bancada, porque e nelas que a
    mutacao de `<` para `<=` muda o veredito — e a cicatriz da F1 em 06/11 foi
    uma grade de teste cujos valores nao caiam em limiar nenhum, o que deixava a
    mutacao de fronteira passar sem morder.
    """
    if carga_max_kg is None:
        raise ValueError("grupo_do_veiculo nao decide sobre veiculo sem carga declarada: "
                         "esse caso tem grupo PROPRIO, pela 3.5")
    cm = Fraction(str(carga_max_kg))
    t = Fraction(str(total))
    if cm >= carga_minima_com_folga(t, margem_fr):
        return "folga"
    if t <= cm:
        return "no_limite"
    return "nao_aguenta"


# --------------------------------------------------------------------------
# A PRESTACAO DE CONTAS DA SECAO 7, EM FUNCAO PURA SOBRE O BANCO JA LIDO.
# --------------------------------------------------------------------------

def _valor(campo):
    """Campo do banco: ou {'valor': x, ...} ou o valor cru."""
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def _tem_saida_de_compra(r):
    af = r.get("afiliado") or {}
    return bool(af.get("url_busca") or af.get("url_produto"))


def grupos_de_carga(registros, total, margem_fr):
    """Agrupa TODO registro por CAUSA, cada um em EXATAMENTE um grupo.

    Os grupos, e a ordem das perguntas e regra:
      fora_do_banco       -> `excluido_do_banco`, antes de tudo
      nao_declaram_carga  -> sem `carga_max_kg`. VEM ANTES de "sem oferta",
                             porque o registro pode ter link e continuar sem
                             declarar a carga, e a causa que importa para ESTA
                             ferramenta e a da carga. (Na F2 a ordem e a mesma
                             pelo mesmo motivo, com V e Ah no lugar.)
      folga/no_limite/nao_aguenta -> declaram a carga E tem oferta aberta
      sem_saida_de_compra -> declaram a carga e NAO tem oferta aberta. Nao e
                             defeito nem acidente: pela 25.2 nenhum item e
                             publicavel sem piso de compra, entao estes nao
                             entram na vitrine — e a pagina os NOMEIA em vez de
                             os sumir, que e a secao 7.

    A soma dos grupos fecha o total recebido, e isso e AFIRMADO aqui dentro:
    numero de tela nasce contado, nunca digitado.
    """
    g = {
        "folga": [],
        "no_limite": [],
        "nao_aguenta": [],
        "nao_declaram_carga": [],
        "sem_saida_de_compra": [],
        "fora_do_banco": [],
    }
    for r in registros:
        if r.get("status") == "excluido_do_banco":
            g["fora_do_banco"].append(r)
            continue
        carga = _valor(r.get("carga_max_kg"))
        if carga is None:
            g["nao_declaram_carga"].append(r)
            continue
        if not _tem_saida_de_compra(r):
            g["sem_saida_de_compra"].append(r)
            continue
        g[grupo_do_veiculo(carga, total, margem_fr)].append(r)

    soma = sum(len(v) for v in g.values())
    assert soma == len(registros), (
        "prestacao de contas furada: %d agrupados de %d recebidos" % (soma, len(registros)))
    return g


def quantos_serviriam_sem_a_oferta(registros, total, margem_fr):
    """Quantos registros com carga declarada CABERIAM no grupo de folga se a
    oferta aberta nao fosse exigida — e o que a vitrine perde por falta de link.

    Esta funcao existe porque a frase de lista vazia precisa saber QUAL dos dois
    eixos esvaziou a vitrine: a CARGA (ninguem aguenta o peso) ou a COMPRA
    (aguentam e nao ha link). Sem ela, um molde unico afirmava o primeiro em
    todo mundo que o segundo produzia — e isso foi medido como falso no banco
    de 06/11/2026, onde os tres registros com carga declarada declaram 120 kg e
    cobrem com folga o caso do `VOZ.md` (108 kg, que pede 119).

    Devolve (quantos_serviriam, lista_de_nomes). A lista sai em ordem de carga
    declarada, da maior para a menor, porque e assim que a pagina os serve.
    """
    servem = []
    for r in registros:
        if r.get("status") == "excluido_do_banco":
            continue
        carga = _valor(r.get("carga_max_kg"))
        if carga is None:
            continue
        if grupo_do_veiculo(carga, total, margem_fr) == "folga":
            servem.append((Fraction(str(carga)), nome_do_registro(r), r.get("id")))
    servem.sort(key=lambda x: (-x[0], x[1]))
    return len(servem), [{"id": i, "nome": n, "carga_max_kg": float(c)}
                         for c, n, i in servem]


def maior_teto_do_banco(registros):
    """O maior `carga_max_kg` declarado no banco, e QUANTOS o declaram.

    Devolve (teto, quantos) com teto None quando ninguem declara. Este numero e
    o que a frase de lista vazia da 3.5 publica, e ele e CONTADO daqui — nunca
    lido da constante `teto-de-carga-do-mercado-brasileiro`, que fala do
    MERCADO e diz de si mesma que nao entra em formula. Sao dois fatos
    diferentes, e confundi-los publicaria o numero do mercado com a cara de
    numero do banco.
    """
    valores = []
    for r in registros:
        if r.get("status") == "excluido_do_banco":
            continue
        v = _valor(r.get("carga_max_kg"))
        if v is not None:
            valores.append(Fraction(str(v)))
    if not valores:
        return None, 0
    return max(valores), len(valores)


def _n(fr, casas=0):
    """Numero em portugues: milhar com ponto, decimal com virgula."""
    if casas == 0:
        inteiro = int(fr + Fraction(1, 2)) if fr >= 0 else -int(-fr + Fraction(1, 2))
        return "{:,}".format(inteiro).replace(",", ".")
    q = Fraction(10) ** casas
    arred = int(fr * q + Fraction(1, 2)) / float(q)
    s = ("{:,.%df}" % casas).format(arred)
    return s.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def _teto(fr):
    """Arredonda para CIMA, em inteiro. A direcao e regra, nao estilo.

    A carga minima recomendada arredondada para BAIXO devolve um numero menor
    do que a margem pede, e com 108 kg e 10% isso seria publicar 118 onde a
    regra diz 118,8 — ou seja, aprovar um veiculo de 118 kg que a propria regra
    recusa. O erro caro desta ferramenta e o permissivo (3.3), entao o
    arredondamento anda para o lado seguro.
    """
    inteiro = int(fr)
    return inteiro if Fraction(inteiro) == fr else inteiro + 1


def nome_do_registro(r):
    """O nome que a tela usa, e ele sai do banco, nunca do `id`.

    Marca + modelo quando os dois existem; o que houver quando falta um. Sem
    marca nem modelo, o `titulo_colhido` — que e a palavra do VENDEDOR e nao
    da ilha (secao 26). Sem nada disso, o `id`, que e o ultimo recurso e nunca
    o primeiro.
    """
    marca = (r.get("marca") or "").strip()
    modelo = (r.get("modelo") or "").strip()
    if marca and modelo:
        return "%s %s" % (marca, modelo)
    if marca or modelo:
        return marca or modelo
    titulo = (r.get("titulo_colhido") or "").strip()
    return titulo or r.get("id", "")


def responder(peso_piloto_kg, carga_kg=0, constantes=None, registros=None):
    """A resposta inteira da F3, ja em frases acentuadas.

    `registros` e OPCIONAL de proposito: a resposta principal — de quanta carga
    maxima a pessoa precisa — nao depende do banco, e passar None devolve a
    resposta sem a camada de vitrine. E o que torna esta ferramenta publicavel
    com o banco de hoje, e e o mundo que a bancada fabrica primeiro.
    """
    constantes = constantes if constantes is not None else carregar_constantes()

    total = peso_total(peso_piloto_kg, carga_kg)
    margem_fr, margem_pct = margem(constantes)
    if margem_fr is None:
        raise ValueError(
            "a constante %s nao esta publicavel: a F3 nao tem resposta a dar, e a "
            "pagina deve dizer isso em vez de escolher um numero" % CONSTANTE_DA_MARGEM)

    minimo = carga_minima_com_folga(total, margem_fr)
    minimo_tela = _n(Fraction(_teto(minimo)))

    tem_carga_informada = Fraction(str(carga_kg or 0)) > 0
    if tem_carga_informada:
        frase_precisa = MOLDES["precisa"].format(total=_n(total), minimo=minimo_tela)
    else:
        frase_precisa = MOLDES["precisa_sem_carga"].format(
            piloto=_n(Fraction(str(peso_piloto_kg))), minimo=minimo_tela)

    frase_margem = MOLDES["margem"].format(
        minimo=minimo_tela, total=_n(total), pct=_n(Fraction(str(margem_pct))))

    # ---- a camada do banco. Opcional, e a pagina diz quando ela esta vazia. ----
    grupos = None
    linhas = {}
    contagem = {}
    frases_vazio = []
    teto_do_banco = None
    quantos_declaram = 0
    quantos_serviriam = 0
    serviriam = []

    if registros is not None:
        grupos = grupos_de_carga(registros, total, margem_fr)
        contagem = {k: len(v) for k, v in grupos.items()}
        teto_do_banco, quantos_declaram = maior_teto_do_banco(registros)

        for nome_grupo in GRUPOS_EM_ORDEM:
            linhas[nome_grupo] = []
            for r in grupos[nome_grupo]:
                carga = Fraction(str(_valor(r.get("carga_max_kg"))))
                if nome_grupo == "folga":
                    texto = MOLDES["linha_folga"].format(
                        nome=nome_do_registro(r), carga=_n(carga),
                        sobra=_n(carga - Fraction(_teto(minimo))))
                elif nome_grupo == "no_limite":
                    texto = MOLDES["linha_no_limite"].format(
                        nome=nome_do_registro(r), carga=_n(carga), total=_n(total),
                        pct=_n(Fraction(str(margem_pct))))
                else:
                    texto = MOLDES["linha_nao_aguenta"].format(
                        nome=nome_do_registro(r), carga=_n(carga),
                        faltam=_n(total - carga))
                linhas[nome_grupo].append({"id": r.get("id"),
                                           "nome": nome_do_registro(r),
                                           "carga_max_kg": float(carga),
                                           "frase": texto})

        # A LISTA VAZIA NOMEIA A CAUSA QUE A PAGINA MEDIU, e sao TRES causas com
        # consertos diferentes (3.5). A ordem das perguntas e a da causa mais
        # funda para a mais rasa: sem banco, sem link, sem carga que sirva.
        quantos_serviriam, serviriam = quantos_serviriam_sem_a_oferta(
            registros, total, margem_fr)
        if not linhas["folga"]:
            if teto_do_banco is None:
                frases_vazio.append(MOLDES["vazio_sem_nenhum"].format(total=_n(total)))
            elif quantos_serviriam > 0:
                # Aguentam e nao ha link: o eixo que esvaziou e o da COMPRA.
                frases_vazio.append(MOLDES["vazio_por_falta_de_oferta"].format(
                    quantos_servem=_n(Fraction(quantos_serviriam)),
                    quantos=_n(Fraction(quantos_declaram)), total=_n(total)))
            else:
                # Ninguem aguenta: o eixo que esvaziou e o da CARGA.
                frases_vazio.append(MOLDES["vazio_por_carga"].format(
                    quantos=_n(Fraction(quantos_declaram)), total=_n(total),
                    teto=_n(teto_do_banco)))

    # ---- a ressalva SOURCED do grupo do meio, e ela so nasce onde ha grupo ----
    frases_ressalva = []
    if constante_publicavel(constantes, CONSTANTE_DA_RESSALVA) is not None:
        if grupos is None or linhas.get("no_limite"):
            frases_ressalva.append(MOLDES["ressalva_no_limite"])

    # ---- a observacao de mercado, datada, e NUNCA limite ----
    frases_mercado = []
    teto_mercado = constante_publicavel(constantes, CONSTANTE_DO_TETO_DE_MERCADO)
    if teto_mercado is not None:
        frases_mercado.append(MOLDES["teto_de_mercado"].format(
            teto=_n(Fraction(str(teto_mercado)))))

    return {
        "entrada": {
            "peso_piloto_kg": float(peso_piloto_kg),
            "carga_kg": float(carga_kg or 0),
        },
        "peso_total": total,
        "peso_total_tela": _n(total),
        "carga_minima_kg": minimo,
        "carga_minima_tela": minimo_tela,
        "margem_pct": margem_pct,
        "frase_precisa": frase_precisa,
        "frase_margem": frase_margem,
        "frase_convite_f2": MOLDES["convite_f2"],
        "grupos": grupos,
        "contagem": contagem,
        "linhas": linhas,
        "frases_vazio": frases_vazio,
        "frases_ressalva": frases_ressalva,
        "frases_mercado": frases_mercado,
        "teto_do_banco_kg": (None if teto_do_banco is None else float(teto_do_banco)),
        "quantos_declaram_carga": quantos_declaram,
        # OS NOMES DE QUEM SERVIRIA E NAO TEM LINK. A pagina os NOMEIA em vez
        # de os sumir (secao 7), e a frase de lista vazia acima aponta para
        # eles: "os nomes estao logo abaixo, com a carga de cada um".
        "quantos_serviriam_sem_oferta": quantos_serviriam,
        "serviriam_sem_oferta": serviriam,
    }


if __name__ == "__main__":
    import sys
    cs = carregar_constantes()
    with open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
        regs = json.load(f)["registros"]
    for caso in ((100, 8), (110, 0), (70, 5), (130, 10)):
        r = responder(caso[0], caso[1], constantes=cs, registros=regs)
        print("--", caso)
        print("  ", r["frase_precisa"])
        for f_ in r["frases_vazio"]:
            print("  ", f_)
    sys.exit(0)

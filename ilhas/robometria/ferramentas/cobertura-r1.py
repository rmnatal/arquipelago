#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implementacao de REFERENCIA da R1 e varredura da entrada dela de ponta a ponta.

Roda sem dependencia e sem rede:

    python3 ferramentas/cobertura-r1.py            # relatorio na tela
    python3 ferramentas/cobertura-r1.py --gravar   # grava dados/cobertura-r1.json
                                                   # e dados/tabela-exemplos-r1.md

Este arquivo NUNCA e publicado no site: e ferramenta de bancada, como o
validar-banco.py.

POR QUE ELE EXISTE — duas razoes, e as duas sao da secao 14.3 do ARQUIPELAGO.md.

1. A secao 14.3 manda medir a cobertura VARRENDO A FAIXA DE ENTRADA DE CADA
   FERRAMENTA de ponta a ponta. A segunda leva do Bloco 3c fez isso para a R2 e o
   resultado esta em cobertura_de_faixa_r2, dentro de modelos-robo.json — foi assim
   que a faixa descoberta acima de 6.000 Pa e a concentracao de marca apareceram.
   A entrada da R1 nunca foi varrida. Contar "33 pares declarados" no cabecalho nao
   diz em quantos modelos a ferramenta responde alguma coisa: um par a mais no
   HO041, que ja respondia, nao tira nenhum modelo do vazio. So a varredura separa
   as duas coisas.

2. A R1 e regra, nao consulta. Os tres selos, o conjunto mais estreito, o aviso de
   variante de hardware e o kit que responde por uma peca que o fabricante nao vende
   avulsa sao decisoes escritas na especificacao (secoes 1.3, 1.4 e o principio do
   kit no esquema). Escrever isso pela primeira vez direto em PHP, dentro de um
   snippet que so da para testar com o site no ar, e escrever a regra onde ela nao
   pode ser conferida. Aqui a regra roda contra o banco de verdade e a resposta
   aparece frase a frase. Quando o Bloco 4 escrever a R1 em PHP, a saida dele tem que
   BATER com a daqui, e a tabela de exemplos pre-renderizada da secao 1.7 sai gerada
   deste arquivo em vez de digitada a mao.

O QUE ELE NAO E: nao e verificador de contrato. Quem reprova banco fora do esquema e
o validar-banco.py. Este aqui mede e responde; ele so sai com codigo 1 quando a
propria varredura nao consegue ser feita.
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

# Vocabulario de tipo_de_peca do esquema, menos 'kit': kit nao e uma pergunta que a
# pessoa faz. Ninguem busca "kit para o meu ERB10" — busca "filtro para o meu ERB10"
# e descobre, na resposta, que o fabricante so vende dentro do kit. Por isso o kit
# entra na varredura como CAMINHO ate um tipo, nunca como tipo consultavel.
TIPOS_CONSULTAVEIS = [
    "filtro",
    "escova lateral",
    "escova principal",
    "mop",
    "bateria",
    "reservatorio",
]

# Os tres estados possiveis de uma celula (modelo x tipo) da varredura.
DECLARADA = "declarada"
KIT_SEM_COMPOSICAO = "kit_sem_composicao"
VAZIA = "vazia"


def carregar(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return json.load(fh)


def formatar_data(iso):
    """2026-09-09 -> 09/09/2026. A frase publicada leva data em portugues."""
    if not iso or len(iso) != 10:
        return iso or "sem data"
    a, m, d = iso.split("-")
    return "%s/%s/%s" % (d, m, a)


# --------------------------------------------------------------- CARGA
esquema = carregar("esquema-banco.json")
marcas = {m["id"]: m for m in carregar("marcas.json")["registros"]}
doc_modelos = carregar("modelos-robo.json")
doc_pecas = carregar("pecas.json")

modelos = {m["id"]: m for m in doc_modelos["registros"]}
pecas = doc_pecas["registros"]

VOC_TIPO = esquema["vocabularios"]["tipo_de_peca"]
for t in TIPOS_CONSULTAVEIS:
    if t not in VOC_TIPO:
        sys.stderr.write(
            "ERRO: o tipo %r nao existe no vocabulario do esquema. A varredura "
            "mediria uma faixa que a ferramenta nao consegue produzir.\n" % t
        )
        sys.exit(1)


# ------------------------------------------------- A REGRA DA R1, EM UM LUGAR SO
def tipos_que_a_peca_responde(peca):
    """Quais tipos consultaveis esta peca responde.

    Peca comum responde o proprio tipo. KIT responde os tipos que ele declara em
    composicao[] — e e por isso que o tipo 'kit' existe no esquema: a Electrolux nao
    vende filtro de robo avulso, vende o Kit Performance, e sem isto a R1 nao
    responderia 'qual filtro serve no meu ERB10', que e literalmente a consulta-alvo.

    Devolve (tipos_confirmados, kit_de_composicao_nao_transcrita).
    """
    if peca["tipo"] != "kit":
        return ({peca["tipo"]}, False)

    confirmados = set()
    tem_item_sem_tipo = False
    for item in peca.get("composicao", []):
        if item.get("tipo"):
            confirmados.add(item["tipo"])
        else:
            # Item sem tipo e item que a coleta nao transcreveu, ou item para o qual
            # nao ha tipo no vocabulario. Nos dois casos a R1 sabe que o kit serve e
            # NAO sabe dizer o que vem dentro — e dizer que vem seria supor.
            tem_item_sem_tipo = True
    return (confirmados, tem_item_sem_tipo and not confirmados)


def pares_do_modelo(peca, modelo_id):
    return [c for c in peca.get("compatibilidade", []) if c.get("modelo") == modelo_id]


# Genero e artigo de cada tipo consultavel. Existe porque a frase da R1 vai para a
# tela como resposta principal da pagina, e "nao vende escova lateral avulso" e um
# defeito visivel numa ilha cujo unico ativo e a confianca.
GENERO_DO_TIPO = {
    "filtro": ("o", "avulso"),
    "escova lateral": ("a", "avulsa"),
    "escova principal": ("a", "avulsa"),
    "mop": ("o", "avulso"),
    "bateria": ("a", "avulsa"),
    "reservatorio": ("o", "avulso"),
}


# --------------------------------------------- QUEM NOMEIA A FUNCAO DA PECA
# Secao 26 do ARQUIPELAGO.md. O vocabulario desta ilha classifica pela FUNCAO
# ('escova lateral' x 'escova principal'); o fabricante batiza pela POSICAO
# ('Direita', 'Central', 'Frontal'). Quando a funcao NAO saiu do titulo, dizer
# "a WAP declara a escova lateral X" empresta ao fabricante uma palavra que ele
# nunca usou — e a unica coisa que esta ilha vende e a declaracao dele.
#
# A LISTA DE TIPOS MORA NO ESQUEMA (26.2), nunca aqui dentro: tipo novo que sofra
# do mesmo mal entra numa linha do esquema e a frase passa a tratar o caso sem
# uma linha de codigo. Por isso ela e lida, e por isso a leitura FALHA ALTO
# quando a chave some — regua que cai para "nada a cobrar" no dia em que o dado
# falta e regua que aprova tudo em silencio.
if "tipos_que_exigem_funcao_declarada" not in esquema:
    sys.stderr.write(
        "ERRO: o esquema nao tem 'tipos_que_exigem_funcao_declarada'. Sem essa "
        "lista a R1 nao sabe de quais tipos ela precisa declarar QUEM nomeou a "
        "funcao, e escreveria a atribuicao ao fabricante para todos.\n"
    )
    sys.exit(1)

TIPOS_COM_FUNCAO_DECLARADA = esquema["tipos_que_exigem_funcao_declarada"]["tipos"]
FUNCAO_DECLARADA_POR = esquema["vocabularios"]["funcao_declarada_por"]

# A ressalva de cada origem de funcao, no mesmo lugar das outras caudas da frase
# (sem codigo publicado, divergencia entre canais, variante de hardware). Formato:
# um %s, que recebe o nome do tipo. 'titulo' nao tem ressalva — ali o fabricante
# escreveu a palavra, e a frase pode atribui-la a ele.
#
# E A RESSALVA DIZ SO O QUE VALE PARA TODOS OS CASOS QUE ELA COBRE. A primeira
# versao dizia "o titulo dela nomeia a posicao, nao a funcao" — verdade na WAP
# ("Escova Direita") e FALSA na Xiaomi, cujo titulo e so "Brush" e nao nomeia
# posicao nenhuma. Afirmacao em bloco tem o escopo do que foi medido (secao 8 do
# ARQUIPELAGO.md), e o que vale nos dois e mais curto: o titulo nao nomeia a
# funcao. O detalhe de cada caso esta em funcao.declarado_como, no banco.
RESSALVA_DA_FUNCAO = {
    "contraste-no-catalogo": (
        "Quem chama esta peca de %s e a Robometria, pelo contraste do catalogo do "
        "proprio fabricante: o titulo dela nao nomeia a funcao."
    ),
    "canal-de-manutencao": (
        "Quem chama esta peca de %s e o proprio fabricante, no canal de manutencao "
        "dele: o titulo da peca nao nomeia a funcao."
    ),
}


# QUEM DIVERGE MUDA A FRASE, E A FRASE NAO PODE DIGITAR NEM O NUMERO NEM A
# NATUREZA (13/09/2026). Ate esta data a cauda de divergencia era uma frase fixa:
# "Dois canais do fabricante discordam". Ela era verdadeira por acidente do banco —
# as sete divergencias de peca existentes vinham todas de canal de fabricante. O
# primeiro registro cujos canais divergentes eram marketplace e varejista (o
# recipiente FW008543 da WAP) fez a frase emprestar a autoridade do FABRICANTE a
# quem so revende, que e o defeito exato que esta ilha existe para nao cometer. E
# "Dois" e a cicatriz do numero de tela digitado, ja paga duas vezes nesta ilha.
#
# A fronteira entre "fala pela marca" e "fala sobre a marca" mora no ESQUEMA, no
# proprio degrau da escada (fala_pela_marca), pelo mesmo motivo que a lista de
# tipos saiu de dentro da regua da funcao: lista dentro da regua envelhece calada.
FALA_PELA_MARCA = {n["origem"]: n["fala_pela_marca"]
                   for n in esquema["escada_de_fontes"]["niveis"]}

POR_EXTENSO = {1: "Um", 2: "Dois", 3: "Tres", 4: "Quatro", 5: "Cinco",
               6: "Seis", 7: "Sete", 8: "Oito", 9: "Nove", 10: "Dez"}


def numeral(n):
    """O numero da frase sai CONTADO e por extenso; acima de dez, em algarismo."""
    return POR_EXTENSO.get(n, str(n))


def lado_da_divergencia(divergencias):
    """'fabricante', 'terceiro' ou 'misto' — lido do degrau de cada canal."""
    lados = set()
    for d in divergencias:
        if d["origem"] not in FALA_PELA_MARCA:
            raise SystemExit(
                "PARE: divergencia com origem %r fora da escada_de_fontes. A frase "
                "da tela nao tem como saber se quem diverge fala pela marca."
                % d["origem"])
        lados.add("fabricante" if FALA_PELA_MARCA[d["origem"]] else "terceiro")
    return lados.pop() if len(lados) == 1 else "misto"


def frase_da_divergencia(divergencias):
    """A cauda de divergencia, com o numero contado e a natureza lida do degrau.

    As duas metades sao afirmacoes diferentes e nao podem sair com as mesmas
    palavras: o fabricante que discorda de si mesmo e uma coisa, e um terceiro que
    afirma alem do que o fabricante declarou e outra. So a primeira justifica dizer
    'canais do fabricante'."""
    n = len(divergencias)
    lado = lado_da_divergencia(divergencias)
    # +1: a declaracao desta pagina tambem esta publicada e datada.
    total = numeral(n + 1).lower()
    canal = "canal" if n == 1 else "canais"
    declara = "declara" if n == 1 else "declaram"
    if lado == "fabricante":
        return (
            "%s %s do fabricante %s alcance diferente para esta peca: vale o "
            "conjunto MAIS ESTREITO, e as %s declaracoes estao publicadas com as "
            "suas datas."
            % (numeral(n), canal, declara, total)
        )
    if lado == "terceiro":
        return (
            "%s %s de fora do fabricante %s para esta peca um alcance que o "
            "fabricante nao declara: quem decide aqui e o fabricante, e as %s "
            "declaracoes estao publicadas com o nome de cada canal e a sua data."
            % (numeral(n), canal, declara, total)
        )
    return (
        "%s canais declaram alcances diferentes para esta peca, e parte deles esta "
        "fora do fabricante: vale o conjunto MAIS ESTREITO, e as %s declaracoes "
        "estao publicadas com o nome de cada canal e a sua data."
        % (numeral(n), total)
    )


def atribuicao_da_funcao(peca):
    """Quem nomeou a funcao desta peca: 'titulo', 'contraste-no-catalogo' ou
    'canal-de-manutencao'. None quando o tipo nao exige a declaracao (filtro, mop,
    bateria e reservatorio: o titulo do fabricante nomeia o que a peca E)."""
    if peca["tipo"] not in TIPOS_COM_FUNCAO_DECLARADA:
        return None
    return (peca.get("funcao") or {}).get("declarada_por")


# A FRASE PRECISA SABER A QUEM ATRIBUIR A FUNCAO ANTES DE SER ESCRITA. O
# validar-banco.py ja cobra o campo; esta trava e da FRASE, e ela existe porque as
# duas perguntas sao diferentes: la e "o registro esta completo", aqui e "eu sei
# como escrever esta linha sem mentir". Peca publicavel que chegasse aqui sem o
# campo sairia com a atribuicao ao fabricante por omissao, que e exatamente o
# defeito de 13/09.
for _peca in pecas:
    if _peca["tipo"] not in TIPOS_COM_FUNCAO_DECLARADA:
        continue
    _declarada_por = atribuicao_da_funcao(_peca)
    if _declarada_por not in FUNCAO_DECLARADA_POR:
        sys.stderr.write(
            "ERRO: a peca %r e do tipo %r e nao declara funcao.declarada_por "
            "dentro do vocabulario (leu %r). A R1 nao tem como saber se a funcao "
            "e palavra do fabricante ou leitura nossa, e escreveria a frase "
            "atribuindo a ele.\n" % (_peca["id"], _peca["tipo"], _declarada_por)
        )
        sys.exit(1)
    if _declarada_por != "titulo" and _declarada_por not in RESSALVA_DA_FUNCAO:
        sys.stderr.write(
            "ERRO: a peca %r declara a funcao por %r, que esta no vocabulario e "
            "nao tem ressalva escrita em RESSALVA_DA_FUNCAO. Origem nova de "
            "funcao entra com a frase que a explica ao leitor, nunca calada.\n"
            % (_peca["id"], _declarada_por)
        )
        sys.exit(1)


def identificar_peca(peca):
    """Como a peca e chamada na frase publicada.

    Nem todo fabricante publica codigo (a Electrolux identifica varias pecas so pelo
    titulo; a Xiaomi identifica pelo nome do acessorio). Nesse caso a frase cita o
    TITULO DA FONTE e diz que o fabricante nao publica codigo — que e a mesma regra
    do null com motivo que vale para os numeros do banco. Escrever "sem codigo
    publicado" no lugar onde o leitor espera um codigo produz frase sem sentido
    ("vem dentro do sem codigo publicado"), e foi assim que este defeito apareceu:
    rodando a regra contra o banco antes de ela virar PHP.
    """
    codigo = peca.get("codigo_fabricante")
    if codigo:
        return (codigo, False)
    return ('"%s"' % peca["nome_na_fonte"], True)


def atribuicao_do_item(peca, par, modelo, dentro_do_kit=None, existe_avulso=False):
    """A ORACAO EM QUE ESTE ITEM ATRIBUI A COMPATIBILIDADE (14/09/2026).

    Ela sempre esteve aqui, como o comeco de frase_declarada(); o que nao existia
    era um NOME para ela. Sem nome, uma regua que quisesse medir "a quem este item
    atribui" so podia medir a frase inteira — e a frase inteira carrega a cauda da
    divergencia, que fala do fabricante com toda a razao ("Um canal do fabricante
    declara alcance diferente"). Medir as duas juntas da falso positivo, e foi
    exatamente o que aconteceu ao escrever a secao 17 do teste-r1.php: a regua
    reprovou a cauda certa. Fronteira de teste e marcador escrito, nunca "a
    primeira coisa parecida com" — a cicatriz que a tabela de exemplos da R1
    deixou em 13/09/2026.

    O resto da documentacao desta frase esta em frase_declarada(), logo abaixo,
    que a chama e acrescenta as caudas.
    """
    fonte = peca["fontes"][par["fonte"]]
    publicador = fonte.get("publicador") or marcas[peca["marca"]]["nome"]
    codigos = [c.get("codigo_declarado") for c in peca.get("compatibilidade", [])
               if c.get("codigo_declarado")]
    lista = ", ".join(codigos[:-1]) + " e " + codigos[-1] if len(codigos) > 1 else codigos[0]
    identificacao, sem_codigo = identificar_peca(peca)
    data = formatar_data(fonte.get("verificado_em"))

    if dentro_do_kit and existe_avulso:
        artigo, _avulso = GENERO_DO_TIPO.get(dentro_do_kit, ("o", "avulso"))
        frase = (
            "%s %s tambem vem dentro do kit %s, que a %s declara compativel com %s "
            "(%s, verificado em %s)."
            % (artigo.capitalize(), dentro_do_kit, identificacao, publicador, lista,
               fonte.get("origem"), data)
        )
    elif dentro_do_kit:
        artigo, avulso = GENERO_DO_TIPO.get(dentro_do_kit, ("o", "avulso"))
        pronome = "ele" if artigo == "o" else "ela"
        frase = (
            "A %s nao vende %s %s %s para este modelo: %s vem dentro do kit %s, que a %s "
            "declara compativel com %s (%s, verificado em %s)."
            % (publicador, artigo, dentro_do_kit, avulso, pronome, identificacao,
               publicador, lista, fonte.get("origem"), data)
        )
    elif atribuicao_da_funcao(peca) in (None, "titulo"):
        # O fabricante escreveu a palavra do eixo no titulo ("Escova Lateral",
        # "Side Brush", "Escova Central"), ou o tipo nem depende disso (filtro,
        # mop, bateria, reservatorio). So aqui a frase pode dizer que ele
        # DECLARA o tipo: e o que ele fez.
        artigo, _ = GENERO_DO_TIPO.get(peca["tipo"], ("o", "avulso"))
        frase = (
            "A %s declara %s %s %s compativel com %s (%s, verificado em %s)."
            % (publicador, artigo, peca["tipo"], identificacao, lista,
               fonte.get("origem"), data)
        )
    else:
        # A FUNCAO NAO VEIO DO TITULO (secao 26.3). O fabricante declarou duas
        # coisas — o nome da peca e a compatibilidade dela — e a frase diz
        # exatamente essas duas. O tipo abre a frase, para o leitor continuar
        # sabendo de que peca se fala na primeira oracao, mas fora do escopo do
        # verbo 'declara'. Quem nomeou a funcao vai na ressalva, logo abaixo.
        frase = (
            "%s: %s, que a %s declara compativel com %s (%s, verificado em %s)."
            % (peca["tipo"][0].upper() + peca["tipo"][1:], identificacao, publicador,
               lista, fonte.get("origem"), data)
        )

    return frase


def frase_declarada(peca, par, modelo, dentro_do_kit=None, existe_avulso=False):
    """A frase que vai para a tela, com procedencia DENTRO dela (secao 5 do contrato).

    Nunca parafraseia: cita o publicador, o codigo (ou o titulo, quando o fabricante
    nao publica codigo), o conjunto que o fabricante declarou e a data da verificacao.

    `existe_avulso` conserta uma CONTRADICAO que so apareceu quando a resposta foi
    lida como um leitor le, e nao conferida por regra objetiva. A frase do kit
    dizia "a Electrolux nao vende o filtro avulso para este modelo" no mesmo
    resultado em que a frase anterior dizia "a Electrolux declara o filtro
    [HEPA com espuma] compativel com o ERB60" — o filtro avulso existe, e a
    pagina o mostrava e o negava na mesma tela. "Nao vende avulso" e uma
    afirmacao sobre o CATALOGO INTEIRO daquele modelo, entao ela so pode ser
    escrita quando nenhuma peca avulsa daquele tipo responde por ele. Quando
    existe avulso, o kit e um caminho A MAIS, e a frase diz isso.

    E A FRASE DO CAMINHO A MAIS NOMEIA O TIPO, NUNCA UM PRONOME (12/09/2026).
    Ela nasceu como "Ele tambem vem dentro do kit ...", e isso so lia certo
    porque, no unico caso que existia, a peca avulsa do mesmo tipo vinha logo
    antes no banco — o "Ele" apontava para a frase anterior por SORTE DE ORDEM.
    Ao entrar o pano de microfibra ERB60/61/62/80, o mop passou a ter avulso E
    kit, e a frase do kit foi emitida na posicao do KIT: ela caiu depois da
    escova lateral e antes de o mop ser nomeado, virando um pronome sem
    antecedente em tres paginas ja no ar. A saida nao e reordenar a lista — e
    parar de depender da vizinhanca, que e a mesma regra da secao 8 do
    ARQUIPELAGO.md ("quem decide e a estrutura, nunca a vizinhanca") e da 5.2
    ("frase autossuficiente que sobrevive a ser citada fora de contexto").
    Toda frase de resposta da R1 nomeia o tipo de peca de que fala, e
    ferramentas/teste-r1.php cobra isso em TODA frase, com regua propria.

    E A FRASE SO ATRIBUI AO FABRICANTE A FUNCAO QUE ELE ESCREVEU (13/09/2026,
    secao 26.3 do ARQUIPELAGO.md). "A WAP declara a escova lateral 'Escova
    Direita ...'" estava no ar e a WAP nunca usou a palavra "lateral": ela batiza
    pela POSICAO, e quem leu a funcao no contraste do catalogo dela foi esta
    ilha. Onde a funcao nao veio do titulo, o verbo 'declara' passa a recair
    sobre o que o fabricante de fato declarou — o nome da peca e a lista de
    modelos — e a atribuicao da funcao vai para uma ressalva propria. O campo
    funcao{declarada_por} da secao 26.1 e o que tornou essa diferenca
    mensuravel; antes dele, a frase nao tinha como saber.

    E QUEM DECLARA E O PUBLICADOR, NAS QUATRO FRASES (14/09/2026). Tres destes
    quatro moldes ja citavam o publicador; o do kit sem avulso escrevia "que o
    fabricante declara", DIGITADO, e a mesma frase abria com "A Electrolux (loja
    oficial) nao vende..." — o publicador correto na primeira oracao e a
    autoridade do fabricante emprestada na segunda, dentro de UMA frase, em 18
    itens que ja estavam no ar. A escada de fontes ja separava as duas coisas: o
    degrau 4 FALA PELA MARCA (por isso o item fica do lado do fabricante na
    pagina) e ao mesmo tempo declara quem_declara "pela loja oficial da marca",
    "porque quem transcreveu foi a loja". Falar pela marca nao e ser a marca, e a
    atribuicao de UM item nunca sai do rotulo do lado: sai de quem publicou.
    """
    frase = atribuicao_do_item(peca, par, modelo, dentro_do_kit, existe_avulso)
    _identificacao, sem_codigo = identificar_peca(peca)

    # A RESSALVA VEM ANTES DAS OUTRAS CAUDAS porque ela qualifica a afirmacao
    # principal — quem leu a funcao —, enquanto as de baixo qualificam detalhes
    # do registro (sem codigo publicado, canais que discordam, variante).
    _atribuicao = atribuicao_da_funcao(peca)
    if _atribuicao and _atribuicao != "titulo":
        frase += " " + RESSALVA_DA_FUNCAO[_atribuicao] % peca["tipo"]

    if sem_codigo:
        frase += (
            " Este fabricante nao publica codigo de peca nesta pagina: identifique o "
            "item pelo titulo e pela lista de modelos."
        )

    if peca.get("divergencias"):
        frase += " " + frase_da_divergencia(peca["divergencias"])
    if par.get("variante_de_hardware"):
        frase += " Vale para a versao %s deste modelo." % par["variante_de_hardware"]
    return frase


def frase_de_recusa(tipo):
    """Secao 1.3, selo nao_declarada. O texto e explicito de proposito: silencio
    parece defeito (secao 7 do contrato), e supor e o defeito que esta ilha existe
    para nao cometer."""
    return (
        "Nao localizamos declaracao do fabricante de %s para este modelo; nao vamos "
        "supor." % tipo
    )


def aviso_de_variante(modelo):
    """Secao 1.3 da especificacao e o principio VARIANTE DE HARDWARE do esquema:
    quando o mesmo codigo de modelo tem revisoes com pecas diferentes, devolver uma
    peca so seria adivinhar."""
    variantes = modelo.get("variantes_de_hardware") or []
    if len(variantes) < 2:
        return None
    rotulos = " e ".join(str(v.get("rotulo")) for v in variantes)
    o_que_muda = "; ".join(
        str(v.get("o_que_muda")) for v in variantes if v.get("o_que_muda")
    )
    # Dois pontos, e nao ponto final, antes do que o fabricante escreveu: o
    # texto do banco comeca em minuscula ("bateria — o fabricante vende..."), e
    # depois de ponto final ele saia como frase comecando em minuscula. O ponto
    # que faltava antes de "Confira" tambem entra aqui. Defeito de leitura, nao
    # de regra — apareceu lendo o aviso como um leitor le, nao conferindo campo.
    return (
        "Este modelo tem mais de uma versao de hardware conhecida (%s), e a peca "
        "certa depende da sua: %s. Confira a etiqueta do aparelho antes de comprar."
        % (rotulos, o_que_muda.rstrip("."))
    )


def responder_r1(modelo_id, tipo=None):
    """A R1 inteira. Entrada: um modelo do banco e, opcionalmente, um tipo de peca.

    Devolve a resposta ja separada pelos tres selos da secao 1.3, com as frases
    prontas. Selo declarada_terceiro sai em lista PROPRIA — a secao 7 do contrato
    proibe misturar, e proibe por em primeiro lugar.
    """
    modelo = modelos[modelo_id]
    tipos_pedidos = [tipo] if tipo else list(TIPOS_CONSULTAVEIS)

    do_fabricante = []
    de_terceiro = []
    caixas_fechadas = []

    # Quais tipos este modelo tem resolvidos por peca AVULSA (nao-kit). Precisa
    # ser sabido ANTES de escrever qualquer frase, porque "a marca nao vende o
    # filtro avulso" e uma afirmacao sobre o catalogo inteiro do modelo — e uma
    # frase que so o resultado inteiro pode sustentar nao pode ser escrita
    # olhando uma peca de cada vez.
    tipos_com_avulso = set()
    for peca in pecas:
        if peca["status"] != "publicavel" or peca["tipo"] == "kit":
            continue
        if not pares_do_modelo(peca, modelo_id):
            continue
        tipos_com_avulso.add(peca["tipo"])

    for peca in pecas:
        if peca["status"] != "publicavel":
            continue
        pares = pares_do_modelo(peca, modelo_id)
        if not pares:
            continue

        responde, caixa_fechada = tipos_que_a_peca_responde(peca)

        if caixa_fechada:
            # Kit que serve o modelo e nao diz o que tem dentro. Nao responde tipo
            # nenhum, e esconder isso seria pior: a R1 mostra o kit e diz o que
            # ainda nao sabe.
            for par in pares:
                fonte = peca["fontes"][par["fonte"]]
                caixas_fechadas.append({
                    "peca": peca["id"],
                    "codigo": peca.get("codigo_fabricante"),
                    "nome_na_fonte": peca["nome_na_fonte"],
                    "frase": (
                        "A %s declara o %s compativel com este modelo (%s, verificado "
                        "em %s), mas nao transcrevemos ainda a lista do que vem dentro "
                        "— entao nao afirmamos qual peca o kit cobre."
                        % (fonte.get("publicador") or marcas[peca["marca"]]["nome"],
                           peca["nome_na_fonte"],
                           fonte.get("origem"),
                           formatar_data(fonte.get("verificado_em")))
                    ),
                })
            continue

        atendidos = [t for t in tipos_pedidos if t in responde]
        if not atendidos:
            continue

        for par in pares:
            for t in atendidos:
                existe_avulso = (peca["tipo"] == "kit" and t in tipos_com_avulso)
                item = {
                    "tipo_respondido": t,
                    "peca": peca["id"],
                    "codigo": peca.get("codigo_fabricante"),
                    "motivo_sem_codigo": peca.get("motivo_sem_codigo"),
                    "nome_na_fonte": peca["nome_na_fonte"],
                    "dentro_de_kit": peca["tipo"] == "kit",
                    "existe_avulso": existe_avulso,
                    "selo": par["selo"],
                    "divergencia_registrada": bool(peca.get("divergencias")),
                    "vida_util_declarada": peca.get("vida_util_declarada", {}).get("valor"),
                    "afiliado_esperando_link": not (peca.get("afiliado", {}) or {}).get("url"),
                    "frase": frase_declarada(
                        peca, par, modelo,
                        dentro_do_kit=t if peca["tipo"] == "kit" else None,
                        existe_avulso=existe_avulso,
                    ),
                }
                if par["selo"] == "declarada_fabricante":
                    do_fabricante.append(item)
                else:
                    de_terceiro.append(item)

    tipos_respondidos = {i["tipo_respondido"] for i in do_fabricante}
    sem_resposta = [t for t in tipos_pedidos if t not in tipos_respondidos]

    return {
        "modelo": modelo_id,
        "marca": modelo["marca"],
        "codigo_fabricante": modelo["codigo_fabricante"],
        "aviso_de_variante": aviso_de_variante(modelo),
        "declarada_fabricante": do_fabricante,
        "declarada_terceiro": de_terceiro,
        "kits_de_composicao_nao_transcrita": caixas_fechadas,
        "sem_declaracao": [{"tipo": t, "frase": frase_de_recusa(t)} for t in sem_resposta],
    }


# -------------------------------------- O CRUZAMENTO COM A R2, QUE E O ACHADO
def cruzar_com_a_r2(por_modelo):
    """Quais modelos cada uma das duas ferramentas da ilha consegue atender.

    A R2 so tem o que dizer sobre um modelo quando ele tem pa_declarado; a R1 so tem
    o que dizer quando ele tem peca declarada. Medir as duas coberturas separadas nao
    mostra o que este cruzamento mostra — e o cruzamento e barato, entao ele fica
    aqui e nao numa frase escrita a mao que envelhece sozinha.
    """
    r1 = {l["modelo"]: l["resultado"] == "responde" for l in por_modelo}
    r2 = {
        mid: (modelos[mid].get("pa_declarado") or {}).get("valor") is not None
        for mid in r1
    }
    balde = {"as_duas": [], "so_a_r2": [], "so_a_r1": [], "nenhuma": []}
    for mid in sorted(r1):
        if r1[mid] and r2[mid]:
            balde["as_duas"].append(mid)
        elif r2[mid]:
            balde["so_a_r2"].append(mid)
        elif r1[mid]:
            balde["so_a_r1"].append(mid)
        else:
            balde["nenhuma"].append(mid)

    def marcas_de(ids):
        return sorted({modelos[i]["marca"] for i in ids})

    return {
        "o_que_e": (
            "Quais modelos publicaveis cada ferramenta da ilha consegue atender, e a "
            "intersecao entre as duas."
        ),
        "as_duas_respondem": balde["as_duas"],
        "so_a_r2_responde": balde["so_a_r2"],
        "so_a_r1_responde": balde["so_a_r1"],
        "nenhuma_das_duas_responde": balde["nenhuma"],
        "marcas_que_so_a_r2_atende": marcas_de(balde["so_a_r2"]),
        "marcas_que_so_a_r1_atende": marcas_de(balde["so_a_r1"]),
        "contagem": {k: len(v) for k, v in balde.items()},
    }


# ------------------------------------------------------------- A VARREDURA
def varrer():
    publicaveis = [m for m in doc_modelos["registros"] if m["status"] == "publicavel"]
    publicaveis.sort(key=lambda m: (m["marca"], m["codigo_fabricante"]))

    celulas = {DECLARADA: 0, KIT_SEM_COMPOSICAO: 0, VAZIA: 0}
    por_modelo = []
    por_tipo = {t: {DECLARADA: 0, KIT_SEM_COMPOSICAO: 0, VAZIA: 0} for t in TIPOS_CONSULTAVEIS}
    entrada_vazia = []
    so_caixa_fechada = []

    for m in publicaveis:
        r = responder_r1(m["id"])
        cobertos = {i["tipo_respondido"] for i in r["declarada_fabricante"]}
        tem_caixa = bool(r["kits_de_composicao_nao_transcrita"])

        estado_por_tipo = {}
        for t in TIPOS_CONSULTAVEIS:
            if t in cobertos:
                estado = DECLARADA
            elif tem_caixa:
                estado = KIT_SEM_COMPOSICAO
            else:
                estado = VAZIA
            estado_por_tipo[t] = estado
            celulas[estado] += 1
            por_tipo[t][estado] += 1

        if cobertos:
            resultado = "responde"
        elif tem_caixa:
            resultado = "so_kit_de_composicao_nao_transcrita"
            so_caixa_fechada.append(m["id"])
        else:
            resultado = "entrada_vazia"
            entrada_vazia.append(m["id"])

        por_modelo.append({
            "modelo": m["id"],
            "marca": m["marca"],
            "codigo_fabricante": m["codigo_fabricante"],
            "resultado": resultado,
            "tipos_cobertos": sorted(cobertos),
            "tipos_vazios": [t for t, e in estado_por_tipo.items() if e == VAZIA],
            "pecas_do_fabricante": len({i["peca"] for i in r["declarada_fabricante"]}),
            "tem_aviso_de_variante": bool(r["aviso_de_variante"]),
        })

    # Peca publicavel cujo par aponta so para modelo que nao e publicavel: existe no
    # banco e nao chega a resposta nenhuma. Nao e defeito de contrato, e catalogo
    # parado — e a varredura e o unico lugar onde isso aparece.
    alcancadas = set()
    for linha in por_modelo:
        for i in responder_r1(linha["modelo"])["declarada_fabricante"]:
            alcancadas.add(i["peca"])
    pecas_sem_alcance = [
        p["id"] for p in pecas
        if p["status"] == "publicavel" and p["id"] not in alcancadas
    ]

    por_marca = {}
    for linha in por_modelo:
        b = por_marca.setdefault(linha["marca"], {"modelos": 0, "respondem": 0})
        b["modelos"] += 1
        if linha["resultado"] == "responde":
            b["respondem"] += 1

    return {
        "publicaveis": publicaveis,
        "cruzamento": cruzar_com_a_r2(por_modelo),
        "por_modelo": por_modelo,
        "por_tipo": por_tipo,
        "por_marca": por_marca,
        "celulas": celulas,
        "entrada_vazia": entrada_vazia,
        "so_caixa_fechada": so_caixa_fechada,
        "pecas_sem_alcance": pecas_sem_alcance,
    }


# ---------------------------------------- TABELA DE EXEMPLOS PRE-RENDERIZADA (1.7)
def ordem_dos_exemplos(v):
    """A ORDEM da tabela de exemplos, em (linha_do_modelo, item de resposta).

    Separada da montagem da linha porque a ordem e uma decisao editorial — nunca
    alfabetica, sempre alternando marcas — e ela vale para toda forma que a
    tabela tome: o markdown do repositorio e os campos que o Bloco 4 serve em
    HTML. Duas ordens seriam duas tabelas, e duas tabelas divergem em silencio.

    Ordem: primeiro os modelos que cobrem mais tipos (linha que mostra a
    ferramenta fazendo o que promete), e sempre com marcas diferentes antes de
    repetir marca, porque a promessa desta ilha e comparacao CROSS-MARCA — se a
    ordem fosse alfabetica, as nove primeiras linhas seriam todas Electrolux.
    """
    ordenados = sorted(
        [l for l in v["por_modelo"] if l["resultado"] == "responde"],
        key=lambda l: (-len(l["tipos_cobertos"]), l["marca"], l["codigo_fabricante"]),
    )

    fila = []
    restante = list(ordenados)
    while restante:
        # uma passada por marca de cada vez, para nenhuma marca dominar o topo
        vistas = set()
        for l in list(restante):
            if l["marca"] in vistas:
                continue
            vistas.add(l["marca"])
            fila.append(l)
            restante.remove(l)

    pares = []
    for l in fila:
        for item in responder_r1(l["modelo"])["declarada_fabricante"]:
            pares.append((l, item))
    return pares


def tabela_de_exemplos(v):
    """Gera as linhas da tabela obrigatoria da secao 5 do contrato.

    Ela nao e enfeite: sem ela a R1 mostra a um modelo de linguagem um formulario
    vazio. Gerar em vez de digitar a mao garante que cada linha existe no banco, com
    o codigo, o selo e a data que o banco tem — e que ela nunca fica velha em
    silencio quando o banco muda.

    Entra TUDO que a R1 responde hoje, nao uma amostra: o minimo de 8 linhas da
    secao 1.7 e piso, e cada par declarado a mais e uma consulta a mais que a pagina
    responde no HTML servido.

    A ordem vem de ordem_dos_exemplos(), que e a mesma que o Bloco 4 serve em HTML.
    """
    linhas = []
    for l, item in ordem_dos_exemplos(v):
        fonte_peca = next(p for p in pecas if p["id"] == item["peca"])
        par = pares_do_modelo(fonte_peca, l["modelo"])[0]
        fonte = fonte_peca["fontes"][par["fonte"]]
        selo = item["selo"]
        if item["divergencia_registrada"]:
            selo += " (divergencia registrada)"
        if item["dentro_de_kit"]:
            selo += " — dentro de kit"
        linhas.append({
            "modelo": "%s %s" % (marcas[l["marca"]]["nome"], l["codigo_fabricante"]),
            "peca": item["tipo_respondido"],
            "codigo": item["codigo"] or "o fabricante nao publica codigo",
            "selo": selo,
            "fonte": "%s · %s" % (fonte.get("origem"),
                                  formatar_data(fonte.get("verificado_em"))),
        })
    return linhas


def markdown_da_tabela(linhas):
    out = [
        "# Tabela de exemplos pre-renderizada da R1",
        "",
        "GERADO por `ferramentas/cobertura-r1.py --gravar`. **Nao edite a mao:** cada",
        "linha sai do banco, com o codigo, o selo e a data que o banco tem. Editar aqui",
        "faria a tabela discordar do banco em silencio, que e exatamente o defeito que a",
        "secao 5 do `ARQUIPELAGO.md` existe para impedir.",
        "",
        "Esta tabela e o corpo da pagina da R1 para um modelo de linguagem. Sem ela a",
        "ferramenta e um formulario vazio: o robo e o modelo de IA leem o HTML servido, e",
        "no HTML servido nao existe nenhum resultado de JavaScript. O Bloco 4 serve estas",
        "linhas em HTML, sem depender de script.",
        "",
        "| Modelo | Peca | Codigo do fabricante | Selo | Fonte / data |",
        "|---|---|---|---|---|",
    ]
    for l in linhas:
        out.append("| %s | %s | %s | %s | %s |" % (
            l["modelo"], l["peca"], l["codigo"], l["selo"], l["fonte"]))
    out.append("")
    out.append("Linhas: **%d** — o minimo da secao 1.7 da especificacao e 8." % len(linhas))
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------- A LEITURA DA VARREDURA
def leitura(v):
    """A leitura da medicao, montada com os numeros da propria medicao.

    Escrita aqui, e nao a mao no JSON, pelo mesmo motivo que a tabela de exemplos e
    gerada: numero copiado a mao para dentro de prosa e numero que a proxima
    execucao vai acreditar sem conferir, muito depois de ele ter deixado de ser
    verdade.
    """
    c = v["cruzamento"]
    total = len(v["publicaveis"])
    respondem = sum(1 for l in v["por_modelo"] if l["resultado"] == "responde")
    vazias = v["celulas"][VAZIA]
    tipos_zerados = [t for t in TIPOS_CONSULTAVEIS if v["por_tipo"][t][DECLARADA] == 0]

    partes = []
    partes.append(
        "A R1 responde alguma peca em %d dos %d modelos publicaveis, e sai VAZIA em "
        "%d. Contar os 33 pares declarados do cabecalho escondia isso: par novo num "
        "modelo que ja respondia nao tira modelo nenhum do vazio, e so a varredura "
        "separa as duas coisas."
        % (respondem, total, len(v["entrada_vazia"]))
    )
    partes.append(
        "O ACHADO, e ele so aparece cruzando as duas ferramentas: das %d entradas "
        "publicaveis, apenas %d sao atendidas pelas DUAS. A R2 atende %d modelos que "
        "a R1 nao atende (%s) e a R1 atende %d que a R2 nao atende (%s). A cobertura "
        "das duas ferramentas da ilha e quase disjunta, e a causa e a mesma nos dois "
        "sentidos: Electrolux e Multi publicam peca com compatibilidade declarada e "
        "NAO publicam Pa; Xiaomi e WAP publicam Pa e NAO publicam peca com codigo."
        % (total, len(c["as_duas_respondem"]),
           len(c["so_a_r2_responde"]), ", ".join(c["marcas_que_so_a_r2_atende"]),
           len(c["so_a_r1_responde"]), ", ".join(c["marcas_que_so_a_r1_atende"]))
    )
    partes.append(
        "POR QUE ISSO CUSTA DINHEIRO: a ilha ganha a visita pela R2 ('quantos Pa para "
        "pelo de cachorro'), que hoje so consegue recomendar Xiaomi na faixa alta. "
        "Quem compra volta meses depois procurando o filtro daquele robo — a consulta "
        "de maior intencao de compra do nicho, e a razao de a R1 existir — e recebe "
        "'nao localizamos declaracao do fabricante'. As duas ferramentas nao se "
        "entregam a visita uma para a outra. O funil esta partido na emenda, e nenhuma "
        "das duas medicoes isoladas mostrava a emenda."
    )
    partes.append(
        "O QUE ISSO MUDA NA ORDEM DA FILA: a leva anterior deixou 'pecas da Xiaomi e "
        "da WAP com codigo' em ULTIMO lugar entre os alvos de coleta. A varredura diz "
        "que ele e o primeiro entre os coletaveis, por dois motivos medidos. Primeiro: "
        "e o unico alvo que fecha a emenda pelo lado que da para colher — a lacuna "
        "simetrica (Pa da Electrolux e da Multi) ja foi medida como inexistente no "
        "mercado, essas marcas nao publicam Pa em canal nenhum, entao insistir nela e "
        "trabalho sem fim. Segundo: sao exatamente os %d modelos que a R2 ja "
        "recomenda, ou seja, o retorno chega na visita que a ilha ja sabe atrair, nao "
        "numa visita hipotetica."
        % len(c["so_a_r2_responde"])
    )
    if tipos_zerados:
        partes.append(
            "DECISAO DE INTERFACE que a varredura obriga: o tipo %s nao tem NENHUMA "
            "peca declarada no banco inteiro. Deixar esse tipo no seletor da R1 e "
            "oferecer uma escolha que sempre devolve recusa — pela secao 6 do "
            "ARQUIPELAGO.md a promessa vem antes do formulario, entao o seletor da R1 "
            "so oferece tipo que o banco consegue responder em pelo menos um modelo, e "
            "o tipo volta ao seletor no dia em que a primeira peca dele entrar."
            % ", ".join("'%s'" % t for t in tipos_zerados)
        )
    partes.append(
        "O QUE A VARREDURA NAO E: ela nao aplica o portao de 3 itens da secao 9. Na "
        "R2 a faixa produz uma lista de produtos concorrentes e tres e o minimo "
        "honesto; na R1 a resposta certa costuma ser UMA peca, a que o fabricante "
        "declarou, e exigir tres levaria a ilha a inventar concorrente onde o "
        "fabricante tem uma peca so. O criterio aqui e binario e mais duro: das %d "
        "celulas (modelo x tipo), %d nao tem o que responder."
        % (sum(v["celulas"].values()), vazias)
    )
    return partes


# ------------------------------------------------------------------ RELATORIO
def relatorio(v):
    total_modelos = len(v["publicaveis"])
    respondem = sum(1 for l in v["por_modelo"] if l["resultado"] == "responde")
    total_celulas = sum(v["celulas"].values())

    print("Robometria — varredura da entrada da R1 (secao 14.3 do ARQUIPELAGO.md)")
    print("")
    print("  modelos publicaveis .............. %d" % total_modelos)
    print("  respondem alguma peca ........... %d" % respondem)
    print("  so kit de composicao nao transcrita %d" % len(v["so_caixa_fechada"]))
    print("  ENTRADA VAZIA ................... %d" % len(v["entrada_vazia"]))
    print("")
    print("  celulas modelo x tipo ........... %d (%d modelos x %d tipos)"
          % (total_celulas, total_modelos, len(TIPOS_CONSULTAVEIS)))
    print("    declarada ..................... %d" % v["celulas"][DECLARADA])
    print("    kit sem composicao ............ %d" % v["celulas"][KIT_SEM_COMPOSICAO])
    print("    vazia ......................... %d" % v["celulas"][VAZIA])
    print("")
    print("  por tipo consultavel:")
    for t in TIPOS_CONSULTAVEIS:
        b = v["por_tipo"][t]
        print("    %-18s declarada %2d · kit fechado %2d · vazia %2d"
              % (t, b[DECLARADA], b[KIT_SEM_COMPOSICAO], b[VAZIA]))
    print("")
    print("  por marca (modelos que respondem / publicaveis):")
    for marca in sorted(v["por_marca"]):
        b = v["por_marca"][marca]
        print("    %-12s %d/%d" % (marca, b["respondem"], b["modelos"]))
    print("")
    if v["entrada_vazia"]:
        print("  ENTRADA VAZIA — a R1 nao responde nada nestes modelos:")
        for mid in v["entrada_vazia"]:
            print("    . %s" % mid)
        print("")
    if v["pecas_sem_alcance"]:
        print("  pecas publicaveis que nao chegam a resposta nenhuma:")
        for pid in v["pecas_sem_alcance"]:
            print("    . %s" % pid)
        print("")

    c = v["cruzamento"]
    print("  cruzamento com a R2 (a R2 responde quando o modelo tem pa_declarado):")
    print("    as duas respondem ......... %d  %s"
          % (len(c["as_duas_respondem"]), c["as_duas_respondem"]))
    print("    so a R2 ................... %d  marcas: %s"
          % (len(c["so_a_r2_responde"]), ", ".join(c["marcas_que_so_a_r2_atende"])))
    print("    so a R1 ................... %d  marcas: %s"
          % (len(c["so_a_r1_responde"]), ", ".join(c["marcas_que_so_a_r1_atende"])))
    print("    nenhuma das duas .......... %d" % len(c["nenhuma_das_duas_responde"]))
    print("")
    for p in leitura(v):
        print("  " + p)
        print("")


def main():
    v = varrer()
    relatorio(v)
    linhas = tabela_de_exemplos(v)

    if "--gravar" not in sys.argv:
        print("  (rode com --gravar para escrever dados/cobertura-r1.json e "
              "dados/tabela-exemplos-r1.md)")
        return 0

    total_modelos = len(v["publicaveis"])
    respondem = sum(1 for l in v["por_modelo"] if l["resultado"] == "responde")

    doc = {
        "id": "cobertura-r1",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/cobertura-r1.py",
        "gerado_em": doc_pecas["gerado_em"],
        "o_que_e": (
            "Varredura da faixa de entrada da R1 de ponta a ponta, exigida pela secao "
            "14.3 do ARQUIPELAGO.md — o mesmo que cobertura_de_faixa_r2 faz para a R2. "
            "A entrada da R1 e o par (modelo publicavel, tipo de peca consultavel), "
            "entao a varredura passa por todas as celulas e registra, celula a celula, "
            "se a ferramenta tem o que responder. O criterio da R1 NAO e o de 3 itens "
            "da secao 9: ali a faixa produz uma lista de produtos concorrentes, aqui a "
            "resposta certa costuma ser UMA peca — a que o fabricante declarou. Exigir "
            "tres levaria a ilha a inventar concorrente onde o fabricante tem uma peca "
            "so. O criterio aqui e binario e mais duro: a celula responde ou nao "
            "responde, e celula que nao responde e a lista de compras."
        ),
        "criterio": {
            "declarada": "existe peca com selo declarada_fabricante para o par (modelo, tipo)",
            "kit_sem_composicao": (
                "um kit serve o modelo, mas a composicao nao foi transcrita — a R1 sabe "
                "QUE o kit serve e nao sabe dizer O QUE vem dentro. Nao conta como "
                "coberta: afirmar que o filtro esta dentro sem a lista seria supor"
            ),
            "vazia": "nada declarado — a R1 recusa com todas as letras e para ali",
        },
        "resumo": {
            "modelos_publicaveis": total_modelos,
            "modelos_que_respondem": respondem,
            "modelos_so_com_kit_de_composicao_nao_transcrita": len(v["so_caixa_fechada"]),
            "modelos_com_entrada_vazia": len(v["entrada_vazia"]),
            "tipos_consultaveis": TIPOS_CONSULTAVEIS,
            "celulas": v["celulas"],
            "celulas_total": sum(v["celulas"].values()),
        },
        "cruzamento_com_a_r2": v["cruzamento"],
        "leitura": leitura(v),
        "por_tipo": v["por_tipo"],
        "por_marca": v["por_marca"],
        "entrada_vazia": v["entrada_vazia"],
        "so_kit_de_composicao_nao_transcrita": v["so_caixa_fechada"],
        "pecas_publicaveis_que_nao_alcancam_resposta": v["pecas_sem_alcance"],
        "por_modelo": v["por_modelo"],
    }

    caminho_json = os.path.join(DADOS, "cobertura-r1.json")
    with open(caminho_json, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    caminho_md = os.path.join(DADOS, "tabela-exemplos-r1.md")
    with open(caminho_md, "w", encoding="utf-8") as fh:
        fh.write(markdown_da_tabela(linhas))

    print("  gravado: dados/cobertura-r1.json")
    print("  gravado: dados/tabela-exemplos-r1.md (%d linhas)" % len(linhas))
    return 0


if __name__ == "__main__":
    sys.exit(main())

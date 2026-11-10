#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A REGUA DAS DUAS AFIRMACOES QUE ESTA ILHA NAO PODE FAZER — e ela e UMA SO, usada
em DUAS superficies.

    python3 ferramentas/teste-afirmacao-de-tela.py              # o REPOSITORIO
    python3 ferramentas/teste-afirmacao-de-tela.py --autoteste   # os mundos fabricados

As duas afirmacoes, e as duas nasceram de defeito MEDIDO NO AR, nao de palpite:

  (A) HABILITACAO. Esta ilha decidiu, por fonte, que NAO responde sobre CNH: a
      Resolucao Contran 996/2023 decide a CATEGORIA e nao tem artigo sobre
      habilitacao, e o Codigo de Transito nao foi lido na fonte oficial (a parede
      do `.gov.br`). A home diz isso com todas as letras. E, na MESMA revisao 60,
      `/veiculos/` servia *"o par que decide se o veiculo dispensa habilitacao e
      placa"*, as duas paginas de familia serviam *"a diferenca entre andar sem
      habilitacao e precisar de uma"*, e o `FAQPage` da bicicleta respondia
      "precisa de CNH?" com **nao**.

  (B) O PESO NA AUTONOMIA. A F2 nao faz conta com o peso de quem pilota — a
      constante de consumo por quilo esta `pendente` e pela secao 10 nao entra em
      formula. A propria F2 diz isso na tela. E quatro outros textos prometiam o
      contrario, dois deles DENTRO do `FAQPage`, que e a metade que o Google e as
      ferramentas de IA citam sem abrir formulario nenhum.

POR QUE A REGUA E UMA E O PORTAO SAO DOIS: a 32.5-c nomeia a familia —
"regua escrita para uma familia de pagina NAO reprova a outra; so a ignora". O
portao mais severo desta ilha (`teste-f1.py`) cobrava a ausencia de `dispensa
CNH` em "todo texto de tela", e "todo texto de tela" ali queria dizer as telas
DA F1: 1 das 10 URLs. Entao a regra mora aqui, uma vez, e quem a aplica e:

  - este portao, sobre o REPOSITORIO (sem rede), que e onde o defeito nasce;
  - `ferramentas/conferir-no-ar.py`, sobre o HTML SERVIDO das URLs do
    `wp-sitemap.xml` **e sobre os blocos `application/ld+json`**, que e onde o
    defeito custa.

Duas copias da mesma regra seriam a "segunda declaracao do mesmo fato" que a 20.7
proibe nesta ilha. Por isso o outro portao IMPORTA daqui em vez de reescrever.

A AFIRMACAO E POSITIVA, pela licao da 20.8: nao se procura a frase ruim que
alguem ja imaginou. Toda frase que fala de habilitacao tem de estar numa das
formas PERMITIDAS, e o que nao esta na lista REPROVA. Redacao nova reprova — e
esse e o lado seguro do erro: falso positivo custa uma linha de texto, falso
negativo manda alguem para a rua sem habilitacao.
"""

import importlib.util
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)


def _reguas_de_tela():
    """As reguas de TEXTO DE TELA vivem em `gerar-f2.py` e sao IMPORTADAS daqui.

    Este arquivo ja diz, no proprio cabecalho, por que a regra mora num lugar so
    e os portoes a aplicam: *"Duas copias da mesma regra seriam a segunda
    declaracao do mesmo fato que a 20.7 proibe nesta ilha"*. As reguas de acento,
    de bastidor, de nome do dono e de vocabulario de maquina moram la porque e la
    que o dado vira texto; aqui elas correm sobre o repositorio COMO ELE ESTA,
    que e o que pega a frase que entrou por edicao a mao do JSON.
    """
    caminho = os.path.join(AQUI, "gerar-f2.py")
    spec = importlib.util.spec_from_file_location("gerar_f2_reguas", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    return mod


REGUAS = _reguas_de_tela()


# ---------------------------------------------------------------------------
# UTILIDADES DE TEXTO
# ---------------------------------------------------------------------------

def sem_acento(t):
    """Minuscula e sem acento. A tela e acentuada; a regua nao pode depender disso."""
    base = unicodedata.normalize("NFD", t)
    return "".join(c for c in base if unicodedata.category(c) != "Mn").lower()


def frases(texto):
    """Corta um elemento de texto em frases.

    O corte e por `.`, `!` e `?` seguidos de espaco, e o `?` e PRESERVADO na
    frase, porque pergunta e uma das formas permitidas.

    O `;` FICOU DE FORA, e isto foi MEDIDO: a primeira versao cortava nele e
    partia ao meio a oracao de recusa desta ilha — *"a resolucao que decide a
    categoria nao tem artigo nenhum sobre CNH; quem decide habilitacao e o Codigo
    de Transito, e esse a gente ainda nao leu na fonte oficial"* —, reprovando a
    segunda metade de um texto CERTO e empurrando quem o escrevesse a repetir o
    marcador em cada clausula. Ponto-e-virgula junta clausula; ponto separa
    afirmacao. Portao que reprova o certo e o caminho mais curto para alguem
    passar a ignora-lo (20.5).
    """
    partes = re.split(r"(?<=[.!?])\s+", texto)
    out = []
    for p in partes:
        p = p.strip()
        if p:
            out.append(p)
    return out


# ---------------------------------------------------------------------------
# (A) HABILITACAO
# ---------------------------------------------------------------------------

# O que faz uma frase FALAR de habilitacao. `habilitad` pega "habilitado".
TOKENS_DE_HABILITACAO = ("cnh", "habilitac", "habilitad")

# AS ORACOES PERMITIDAS, uma por uma, escritas como esta ilha as serve. Esta e
# uma lista de PERMISSAO e nao de proibicao: e o que a 20.8 chama de afirmacao
# positiva. Quem escrever redacao nova sobre habilitacao reprova aqui e tem de
# vir acrescentar a oracao nova A ESTA LISTA, de propria mao — que e o pedagio
# que faz alguem reler a decisao de fonte antes de publicar.
RECUSAS_DE_HABILITACAO = (
    "nao responde sobre cnh",
    "sobre habilitacao esta pagina nao responde",
    "esta pagina nao diz",
    "esta pagina nao responde",
    "esta casa nao afirma",
    "este site ainda nao responde",
    "este site nao responde",
    "habilitacao esta em outra lei",
    "artigo nenhum sobre cnh",
    "nao fala de habilitacao",
    "nao diz que voce pode andar sem cnh",
    # A ORACAO DE CUSTO, e ela nao e sobre o veiculo: e sobre o ERRO da ilha.
    # "errar para o lado permissivo manda alguem para a rua sem habilitacao" e a
    # frase que esta ilha usa para explicar POR QUE nao responde.
    "para a rua sem habilitacao",
)


def _so_dentro_de_citacao(frase, token):
    """O token aparece SO dentro de titulo de anuncio citado?

    A home cita, letra por letra, um titulo de anuncio que diz "sem CNH" — e
    citar o anuncio e justamente a tese desta ilha ("o numero do anuncio nao e o
    que a regra le"). Reprovar a citacao seria reprovar a pagina certa, e a 20.5
    ja disse qual e o preco disso: portao que reprova o certo e o caminho mais
    curto para alguem passar a ignora-lo.

    A citacao e reconhecida pelas aspas CURVAS ou retas; o que esta fora delas
    continua medido.
    """
    fora = re.sub(r"[“”\"][^“”\"]*[“”\"]", " ", frase)

    return token not in sem_acento(fora)


def problemas_de_habilitacao(onde, elementos):
    """Devolve a lista de frases que AFIRMAM algo sobre habilitacao sem licenca.

    `elementos` e uma sequencia de textos de elemento (paragrafo, item de lista,
    titulo, resposta de FAQ). O corte em frase e por elemento: marcador de recusa
    numa frase NAO absolve a frase vizinha. Foi um marcador solto que quase deixou
    passar *"isso o titulo nao diz, e e o que decide se precisa de habilitacao"* —
    o "nao diz" ali e do ANUNCIO, nao da ilha.
    """
    maus = []
    for texto in elementos:
        for f in frases(texto):
            s = sem_acento(f)
            toca = [t for t in TOKENS_DE_HABILITACAO if t in s]
            if not toca:
                continue
            if all(_so_dentro_de_citacao(f, t) for t in toca):
                continue
            if "?" in f:
                continue
            # "pergunta"/"perguntas" NOMEIA a pergunta em vez de responde-la:
            # "Tres perguntas (...): precisa de CNH e placa, quantos km (...)",
            # "A pergunta da CNH e a mais procurada", "Perguntas frequentes".
            if "pergunta" in s:
                continue
            if any(m in s for m in RECUSAS_DE_HABILITACAO):
                continue
            maus.append("%s: %s" % (onde, f.strip()))

    return maus


def problemas_do_faq_de_habilitacao(onde, pares):
    """A pergunta de FAQ que fala de habilitacao exige RECUSA na resposta.

    `pares` e uma sequencia de (pergunta, resposta).

    Esta regua existe porque a de cima NAO alcanca o defeito do item 4 do despacho
    de 06/11/2026: a resposta do `FAQPage` da bicicleta era *"A de pedal assistido,
    dentro dos limites da resolucao, nao. A que anda no acelerador pode ser
    ciclomotor, e ai precisa."* — ela responde "nao" a uma pergunta de CNH **sem
    dizer a palavra**. Nenhuma busca por palavra a pegaria; o que a pega e o PAR.
    """
    maus = []
    for pergunta, resposta in pares:
        if not any(t in sem_acento(pergunta) for t in TOKENS_DE_HABILITACAO):
            continue
        if any(m in sem_acento(resposta) for m in RECUSAS_DE_HABILITACAO):
            continue
        maus.append("%s: a pergunta %r fala de habilitacao e a resposta nao traz "
                    "nenhuma das oracoes de recusa desta ilha: %r"
                    % (onde, pergunta.strip()[:90], resposta.strip()[:160]))

    return maus


# ---------------------------------------------------------------------------
# (B) O PESO DE QUEM PILOTA NA CONTA DE AUTONOMIA
# ---------------------------------------------------------------------------

# O peso DA PESSOA, nunca a carga maxima do veiculo. "seus 90 kg" e a forma que a
# propria F2 usa na resposta.
GATILHOS_DE_PESO = (
    "seu peso",
    "desconto de peso",
    "peso de quem pilota",
    "quilo de quem pilota",
)
GATILHO_DE_PESO_EM_KG = re.compile(r"\bseus\s+\d+(?:[.,]\d+)?\s*kg\b")

# O CONTEXTO E A AUTONOMIA, e `faixa` NAO entra nele. Medido: a frase do teto de
# mercado da F3 diz *"na faixa que vimos no varejo brasileiro (...) a carga maxima
# declarada ia de 115 a 140 kg (...) a conta acima compara o seu peso com a ficha
# de cada veiculo"* — `seu peso` + `faixa` numa frase que esta CERTA e nao fala de
# km nenhum. `\bkm\b` nao casa com `kg`, e foi isso que separou as duas.
CONTEXTO_DE_AUTONOMIA = ("autonomia", "watt-hora")
CONTEXTO_DE_AUTONOMIA_RE = re.compile(r"\b(?:km|wh)\b")

# A UNICA LICENCA: a oracao que NEGA que o peso entre na conta. E ela e a da
# propria F2, que e honesta na tela desde que nasceu.
RECUSAS_DE_PESO = (
    "nao entram na conta",
    "nao entra na conta",
    "nao conta na nossa conta",
    "nao entram no calculo",
    "nao entra no calculo",
    "nenhuma regua de quanto cada quilo",
    "nenhuma regua de quantos watt-hora por km cada quilo",
    "nao faz conta com o peso",
)


def problemas_de_peso(onde, elementos):
    """Devolve os elementos que prometem o peso de quem pilota na autonomia.

    AQUI O CORTE E POR ELEMENTO E NAO POR FRASE, e a diferenca e deliberada: a
    resposta honesta da F2 gasta DUAS frases — uma nega ("Os seus 90 kg nao
    entram na conta") e a outra diz onde o peso entra de verdade ("Eles entram
    aqui, no que esperar da faixa"). Cortar em frase reprovaria a segunda metade
    da unica oracao que esta ilha quer ter.
    """
    maus = []
    for texto in elementos:
        s = sem_acento(texto)
        # PERGUNTA NAO E AFIRMACAO, e a F2 faz uma: *"O peso de quem pilota muda a
        # autonomia?"* é o titulo da recusa dela, nao a promessa. So vale como
        # pergunta o elemento que TERMINA em `?` — paragrafo longo que traz um `?`
        # no meio continua medido inteiro.
        if texto.strip().endswith("?"):
            continue
        if not (any(g in s for g in GATILHOS_DE_PESO) or GATILHO_DE_PESO_EM_KG.search(s)):
            continue
        if not (any(c in s for c in CONTEXTO_DE_AUTONOMIA)
                or CONTEXTO_DE_AUTONOMIA_RE.search(s)):
            continue
        if any(m in s for m in RECUSAS_DE_PESO):
            continue
        maus.append("%s: %s" % (onde, re.sub(r"\s+", " ", texto).strip()[:220]))

    return maus


# ---------------------------------------------------------------------------
# A TERCEIRA CLASSE: O MESMO ATO DE COLHER, CONTADO COM DOIS NUMEROS NA MESMA
# PAGINA (09/11/2026, item 4 do despacho da ronda de hoje).
#
# O DEFEITO MEDIDO no HTML servido da home: *"Hoje o banco tem 17 VEICULOS
# COLHIDOS"* e, duas dobras abaixo, *"Dos 14 anuncios que a gente COLHEU"* e
# *"De 14 anuncios COLHIDOS"*. Os numeros estavam todos CERTOS — 17 registros no
# arquivo, 14 nao excluidos — e as PALAVRAS nao: quem le a pagina de cima a baixo
# recebe duas respostas para "quantos vocês colheram".
#
# POR QUE A REGUA SE ANCORA NO VERBO E NAO NO SUBSTANTIVO: os substantivos eram
# DIFERENTES (`veiculos` e `anuncios`), entao uma regua que cruzasse substantivos
# nao veria nada. O que colide e a AFIRMACAO — "colhemos N" —, e ela se escreve
# com o participio ou com a oracao `que a gente colheu`. E a mesma licao do corte
# de frase da regua de habilitacao, de 06/11: o que se mede e a afirmacao, nao a
# forma em que alguem imaginou que ela apareceria.
#
# E A AFIRMACAO E POSITIVA, pela 20.8: nao procuro o par (17, 14) que eu ja vi.
# Recolho TODA contagem de colheita da pagina e exijo que haja no maximo UMA.
# Redacao nova, numero novo, substantivo novo — tudo cai na mesma conta, e par
# novo REPROVA sem ninguem ter imaginado.

#: "N <coisa> colhido(s)/colhida(s)" e "N <coisa> que a gente colheu/colhemos".
#: O miolo entre o numero e o verbo e limitado para a regua nao atravessar frase.
CONTAGEM_DE_COLHEITA = re.compile(
    r"(\d[\d.]*)\s+([^.;:!?]{0,60}?)\b(colhid[oa]s?|que a gente colheu|que colhemos)\b",
    re.I)


def contagens_de_colheita(texto):
    """As contagens de colheita de um texto, como [(numero, trecho)].

    O numero volta NORMALIZADO (ponto de milhar fora), porque "1.000 colhidos" e
    "1000 colhidos" sao a mesma afirmacao e um par delas nao e contradicao.
    """
    saida = []
    for m in CONTAGEM_DE_COLHEITA.finditer(sem_acento(texto)):
        bruto = m.group(1)
        numero = bruto.replace(".", "")
        if not numero.isdigit():
            continue
        saida.append((int(numero), re.sub(r"\s+", " ", m.group(0)).strip()))
    return saida


def problemas_de_colheita(onde, elementos):
    """Reprova quando a MESMA pagina declara duas colheitas de tamanhos diferentes.

    O corte e por PAGINA e nao por elemento, e e a unica forma de ver esta
    classe: cada frase, sozinha, esta certa. Foi assim que o defeito sobreviveu
    — a 20.4 desta ilha ja escreveu a familia com todas as letras sobre o log do
    `/status`, e aqui ela reaparece em prosa.
    """
    vistos = {}
    for texto in elementos:
        for numero, trecho in contagens_de_colheita(texto):
            vistos.setdefault(numero, trecho)

    if len(vistos) < 2:
        return []

    pares = ", ".join("%d em %r" % (n, vistos[n]) for n in sorted(vistos))
    return ["%s: a pagina declara %d colheitas de tamanhos DIFERENTES (%s). Os numeros podem "
            "estar todos certos e ainda assim a pagina responde duas coisas a \"quantos voces "
            "colheram\". Um numero, um substantivo: nesta ilha o total do arquivo e "
            "`registros` e o que o banco conta e `anuncios colhidos`, e a soma fecha com o "
            "grupo `fora do banco` da prestacao de contas"
            % (onde, len(vistos), pares)]


# ---------------------------------------------------------------------------
# A SUPERFICIE DO REPOSITORIO
# ---------------------------------------------------------------------------

# Os arquivos de dados que o Sync leva ao site. `publicar: false` fica fora: ele e
# bancada e nenhuma linha dele vai para a tela.
def arquivos_publicaveis():
    out = []
    pasta = os.path.join(ILHA, "dados")
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith(".json"):
            continue
        caminho = os.path.join(pasta, nome)
        try:
            with open(caminho, encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and d.get("publicar") is False:
            continue
        out.append((nome, d))

    return out


# As chaves que NAO sao texto de tela: elas existem para quem le o repositorio, e
# e nelas que a prosa de metodo mora. Medi-las reprovaria a explicacao de POR QUE
# a ilha nao responde sobre habilitacao — que e o oposto do que esta regua quer.
CHAVES_DE_BASTIDOR = {
    "o_que_este_arquivo_e", "por_que", "porque_assim", "observacao", "nota",
    "motivo_sem_url_produto", "divergencias", "comentario", "licao",
    "por_que_sem_bloco_de_compra", "nenhum_numero_e_digitado_aqui",
    "o_que_decide_rotulo", "fonte", "descricao", "o_que_falta",
    "proibicao_explicita", "por_que_a_trava_mudou_de_forma_em_06_11_2026",
    "valor",
}

# O TITULO DO ANUNCIO, COLHIDO. Ele VAI para a tela — e vai como CITACAO, que e a
# tese desta ilha: *"o numero do anuncio nao e o que a regra le"*. Um dos titulos
# do banco se chama, letra por letra, "Bicicleta eletrica Siena 1000W adulto sem
# CNH scooter". Medir o titulo do anuncio como se fosse afirmacao DA ILHA
# reprovaria a pagina mais honesta que ela tem.
CHAVES_DE_CITACAO = {
    "titulo_colhido", "titulo_do_anuncio", "titulo_da_oferta",
}


def textos_de_tela_do_dado(nome, d):
    """Toda string de tela de um arquivo de dado, com o caminho dela como `onde`."""
    out = []

    def anda(x, trilha):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in CHAVES_DE_BASTIDOR or k in CHAVES_DE_CITACAO:
                    continue
                anda(v, trilha + "/" + str(k))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                anda(v, "%s[%d]" % (trilha, i))
        elif isinstance(x, str) and len(x.strip()) >= 12 and " " in x.strip():
            # SEM ESPACO = IDENTIFICADOR, nunca frase. `siena-1000w-sem-cnh` e a
            # chave de um registro do banco, e reprova-la seria reprovar o nome
            # que o proprio anuncio deu ao produto.
            out.append(("%s%s" % (nome, trilha), x))

    anda(d, "")

    return out


# A CHAVE `fonte` E BASTIDOR EM `constantes.json` E E TELA EM `f1-respostas.json`
# — E A LISTA ACIMA EXCLUI POR NOME (10/11/2026).
#
# ESTA E A CAUSA, pela 19.4(b), DE O DEFEITO TER PASSADO POR ESTE PORTAO. Em
# `dados/constantes.json` o `fonte` e prosa de registro, escrita para quem le o
# repositorio, e medi-la reprovaria a explicacao de metodo — por isso `fonte`
# esta em CHAVES_DE_BASTIDOR, e esta certo. Mas o gerador PROMOVE esse campo a
# texto de tela quando o copia para `constantes_usadas` de um `*-respostas.json`,
# e o snippet da F1 o imprime EM NEGRITO na dobra "De onde sairam os limites".
# Mesmo nome, papel oposto — e a exclusao, sendo por nome, pulou exatamente o
# campo que acabara de virar tela.
#
# A regra: `fonte` sob `constantes_usadas` E TELA e se mede. Em qualquer outro
# lugar segue sendo registro.
# E O MESMO DEFEITO VOLTOU UM DEGRAU ABAIXO NO DIA SEGUINTE (10/11/2026), NO
# CAMPO AO LADO — por isso esta colheita deixou de ser sobre UMA chave.
#
# O comentario acima diz, sobre `fonte`: "a exclusao, sendo por nome, pulou
# exatamente o campo que acabara de virar tela". O campo `tipo` do mesmo
# `constantes_usadas` tambem virava tela — o PHP da F2 o traduzia por um mapa de
# quatro entradas e caia na PROPRIA CHAVE quando o tipo nao estava nele —, e a F2
# servia `Tipo: observacao_de_mercado` em texto visivel.
#
# E AQUI A EXCLUSAO NAO FOI POR NOME: FOI POR FORMA. `textos_de_tela_do_dado`
# pula toda cadeia sem espaco, com a frase "SEM ESPACO = IDENTIFICADOR, nunca
# frase" escrita ao lado. Ela esta CERTA sobre o dado e FALSA sobre a tela,
# porque era o PHP que promovia o identificador a frase. Mesma cadeia, papel
# oposto: a 20.7 outra vez, e nenhuma lista de nomes a pegaria.
#
# O CONSERTO NAO FOI RELAXAR A EXCLUSAO, e isto importa: relaxar reprovaria os
# slugs legitimos do banco (`siena-1000w-sem-cnh` e o nome que o proprio anuncio
# deu ao produto). O que esta escrito agora e QUAIS CAMPOS a tela recebe prontos,
# e eles sao medidos SEM pergunta de forma — chave de maquina em campo promovido
# e defeito justamente por ter a forma de chave.
CHAVES_PROMOVIDAS_A_TELA = ("fonte", "tipo_na_tela")


def frases_de_procedencia_do_dado(nome, d):
    """Os textos que a tela recebe PRONTOS de `constantes_usadas/<id>/<campo>`."""
    out = []
    usadas = d.get("constantes_usadas") if isinstance(d, dict) else None
    if not isinstance(usadas, dict):
        return out
    for cid, reg in sorted(usadas.items()):
        if not isinstance(reg, dict):
            continue
        for campo in CHAVES_PROMOVIDAS_A_TELA:
            texto = reg.get(campo)
            if isinstance(texto, str) and texto.strip():
                out.append(("%s constantes_usadas/%s/%s" % (nome, cid, campo), texto))

    return out


def problemas_de_procedencia(onde, texto):
    """As quatro reguas de tela sobre uma frase de procedencia, como FALHA.

    As reguas moram em `gerar-f2.py` e la elas levantam `AssertionError`, porque
    la o certo e PARAR antes de gravar. Aqui a mesma regua tem de devolver falha
    para o portao somar e imprimir todas de uma vez.
    """
    falhas = []
    baixo = texto.lower()
    for palavra in REGUAS.PALAVRAS_DE_BASTIDOR:
        if palavra.lower() in baixo:
            falhas.append("%s: palavra de bastidor %r na tela (32.4): %r"
                          % (onde, palavra, texto[:120]))
    for proibido in REGUAS.NUNCA_NA_PAGINA_PUBLICA:
        if proibido.lower() in baixo:
            falhas.append("%s: %r e bastidor da fabrica na pagina publica (32.4): %r"
                          % (onde, proibido, texto[:120]))
    for forma in REGUAS.SEM_ACENTO_NA_TELA:
        if forma in baixo:
            falhas.append("%s: forma sem acento %r na tela (secao 8): %r"
                          % (onde, forma, texto[:120]))
    for forma in REGUAS.SEM_ACENTO_PALAVRA_INTEIRA:
        if re.search(r"\b%s\b" % re.escape(forma), baixo):
            falhas.append("%s: palavra sem acento %r na tela (secao 8): %r"
                          % (onde, forma, texto[:120]))
    # A LACUNA `{ASSIM}` sai antes das reguas de FORMATO: ela e slot, nao frase.
    # Ver `sem_lacuna_de_molde` em `gerar-f2.py` — a regua do sublinhado reprovou
    # `{lim_w}` no minuto em que nasceu, e `lim_w` e o nome da lacuna.
    alvo = REGUAS.sem_lacuna_de_molde(texto)
    for padrao, porque in REGUAS.VOCABULARIO_DE_MAQUINA:
        achado = re.search(padrao, alvo)
        if achado is not None:
            falhas.append("%s: serve %r, que e %s (32.4): %r"
                          % (onde, achado.group(0), porque, texto[:120]))
    # A QUINTA REGUA (10/11/2026): o texto INTEIRO sendo uma chave de maquina.
    # Ela mora em `gerar-f2.py` com as outras quatro e e importada daqui.
    limpo = texto.strip().rstrip(".")
    if REGUAS.CHAVE_DE_MAQUINA.match(limpo):
        falhas.append("%s: serve %r, que e chave de maquina e nao frase de leitor "
                      "(32.4)" % (onde, limpo[:120]))

    return falhas


def pares_de_faq_do_dado(d):
    """Os pares (pergunta, resposta) que esta ilha publica em FAQPage.

    O formato do dado desta ilha e `perguntas: [{pergunta, resposta}]`, e tambem
    aparece `[{titulo, paragrafos}]` nas dobras — so o primeiro e FAQ.
    """
    out = []

    def anda(x):
        if isinstance(x, dict):
            if "pergunta" in x and "resposta" in x:
                if isinstance(x["pergunta"], str) and isinstance(x["resposta"], str):
                    out.append((x["pergunta"], x["resposta"]))
            for v in x.values():
                anda(v)
        elif isinstance(x, list):
            for v in x:
                anda(v)

    anda(d)

    return out


# O TEXTO LITERAL QUE MORA DENTRO DO PHP, E A UNIDADE E A INSTRUCAO, NAO O
# LITERAL. A trava 3 da secao 12 proibe a Sentinela de tocar em snippet, e por
# isso o defeito do item 1 e do item 2 do despacho de 06/11 ficou para a
# Fundacao — mas a REGUA alcanca o snippet sem toca-lo.
#
# POR QUE JUNTAR OS LITERAIS DA MESMA INSTRUCAO, e isto foi medido na primeira
# passada desta regua: o PHP desta ilha escreve paragrafo em cadeia
# (`$faq .= '<p>...' . '...' . '...';`), e cada pedaco sozinho e meia frase.
# Medindo pedaco, a recusa honesta da F2 — *"Conta na vida real, e nao conta na
# nossa conta"* — ficava num literal e o *"O seu peso entra aqui"* noutro, e a
# regua REPROVAVA a unica oracao que esta ilha quer ter. A instrucao inteira e a
# unidade certa, e o `;` e o que a delimita.
#
# O QUE ESTA SUPERFICIE PROMETE, E E MENOS DO QUE A DO AR: juntar por instrucao
# gruda tambem vizinhos que a pagina serve separados — o mapa dos cartoes da home
# e UMA instrucao com os tres cartoes dentro. Entao aqui ela e aviso BARATO e
# ANTECIPADO, e a medicao de verdade e a do HTML servido, elemento por elemento,
# em `conferir-no-ar.py`. Dizer isto e a regra da 32.5-b: aprovar em silencio o
# que nao se mediu e o defeito.
LITERAL_PHP = re.compile(r"'((?:[^'\\]|\\.)*)'")


def textos_de_tela_do_php():
    out = []
    pasta = os.path.join(ILHA, "snippets")
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith(".php"):
            continue
        with open(os.path.join(pasta, nome), encoding="utf-8") as f:
            fonte = f.read()
        # Comentario de bloco e de linha FORA: ali mora a prosa de metodo desta
        # fabrica, e ela fala de habilitacao para explicar a decisao de fonte.
        fonte = re.sub(r"/\*.*?\*/", " ", fonte, flags=re.S)
        fonte = re.sub(r"^\s*//.*$", " ", fonte, flags=re.M)
        for n, instrucao in enumerate(fonte.split(";")):
            pedacos = []
            for m in LITERAL_PHP.finditer(instrucao):
                t = m.group(1).replace("\\'", "'")
                t = re.sub(r"<[^>]*>", " ", t)
                t = re.sub(r"\s+", " ", t).strip()
                # Sem espaco = identificador, chave, classe de CSS ou slug.
                if " " in t:
                    pedacos.append(t)
            if not pedacos:
                continue
            texto = re.sub(r"\s+", " ", " ".join(pedacos)).strip()
            if len(texto) >= 20:
                out.append(("%s (instrucao %d)" % (nome, n + 1), texto))

    return out


def medir_repositorio():
    falhas = []
    afirmacoes = 0

    # A COLHEITA SE MEDE POR ARQUIVO AQUI, E A MEDICAO QUE MANDA E A DO AR.
    # A unidade desta classe e a PAGINA — cada frase, sozinha, esta certa —, e o
    # repositorio nao sabe de pagina: um `dados/*.json` pode alimentar varias e
    # a prosa de um snippet pode sair em nenhuma. Entao aqui ela e aviso BARATO
    # E ANTECIPADO, agrupado por arquivo, e o veredito e o de
    # `conferir-no-ar.py`, que agrupa por URL do `wp-sitemap.xml`. Esta distincao
    # esta escrita pelo mesmo motivo que a de 06/11 sobre o PHP lido por
    # instrucao: regua que promete mais do que alcanca ensina a desconfiar dela.
    por_arquivo = {}

    for nome, d in arquivos_publicaveis():
        textos = textos_de_tela_do_dado(nome, d)
        for onde, t in textos:
            afirmacoes += 2
            falhas += problemas_de_habilitacao(onde, [t])
            falhas += problemas_de_peso(onde, [t])
            por_arquivo.setdefault(nome, []).append(t)
        pares = pares_de_faq_do_dado(d)
        afirmacoes += len(pares)
        falhas += problemas_do_faq_de_habilitacao(nome, pares)
        for onde, t in frases_de_procedencia_do_dado(nome, d):
            afirmacoes += 1
            falhas += problemas_de_procedencia(onde, t)
            por_arquivo.setdefault(nome, []).append(t)

    for nome, t in textos_de_tela_do_php():
        afirmacoes += 2
        falhas += problemas_de_habilitacao(nome, [t])
        falhas += problemas_de_peso(nome, [t])
        # O nome vem como "arquivo.php (instrucao N)"; o agrupamento e por ARQUIVO.
        por_arquivo.setdefault(nome.split(" (instrucao")[0], []).append(t)

    for nome, textos in sorted(por_arquivo.items()):
        afirmacoes += 1
        falhas += problemas_de_colheita(nome, textos)

    # NOVE CONTRA NOVE (10/11/2026): todo tipo declarado em
    # `dados/constantes.json` tem de ter frase de leitor em `TIPO_NA_TELA`, e
    # vice-versa. E a licao da 20.10 — numero contra numero, escrito pelas duas
    # fontes, sem depender de ninguem ler prosa. O gerador ja PARA nisso; aqui a
    # mesma conta roda sobre o repositorio COMO ELE ESTA, que e o que pega o tipo
    # acrescentado ao JSON a mao sem regerar nada.
    afirmacoes += 1
    try:
        quantos = REGUAS.conferir_tipos_na_tela_completos()
    except AssertionError as e:
        falhas.append("dados/constantes.json x TIPO_NA_TELA: %s" % e)
    else:
        print("  tipos de constante com frase de leitor: %d de %d" % (quantos, quantos))

    return afirmacoes, falhas


# ---------------------------------------------------------------------------
# OS MUNDOS FABRICADOS — e o primeiro deles e o AR DA REVISAO 60
# ---------------------------------------------------------------------------

# Copiados letra por letra do HTML servido as 16h2xZ de 06/11/2026, revisao 60,
# pela execucao que fechou o despacho. Mundo fabricado de cabeca prova a regua
# contra a imaginacao de quem a escreveu; estes provam contra o defeito.
AR_60_MAUS_HABILITACAO = (
    "Potência nominal e velocidade máxima é o par que decide se o veículo "
    "dispensa habilitação e placa, ou se é ciclomotor e precisa dos dois.",
    "Nenhum dos 6 anúncios diz se o veículo tem acelerador, e é o acelerador que "
    "decide se ele é bicicleta elétrica ou ciclomotor — a diferença entre andar "
    "sem habilitação e precisar de uma.",
    "Para quem quer saber se precisa de habilitação o que decide é a potência "
    "nominal e a velocidade máxima.",
    "E muda para pior, porque aí entra habilitação e placa.",
    "Isso o título não diz, e é o que decide se precisa de habilitação.",
)

AR_60_BOAS_HABILITACAO = (
    "Sobre habilitação esta página não responde, e o motivo é um só: a resolução "
    "que decide a categoria não tem artigo nenhum sobre CNH.",
    "Esse elétrico precisa de CNH?",
    "Por que esta página não responde sobre CNH",
    "A habilitação está em outra lei, e a gente só vai publicar o que ela diz "
    "depois de ler nela.",
    "Publicar o limite por notícia de segunda mão seria o pior erro possível "
    "aqui — errar para baixo manda alguém para a rua sem habilitação.",
    "Errar aqui manda a pessoa para a rua sem habilitação, então esta casa não "
    "afirma categoria de nenhum modelo cuja ficha não tenha sido lida.",
    "Um deles se chama, letra por letra, “Bicicleta elétrica Siena 1000W adulto "
    "sem CNH scooter”: são quatro coisas que a regra separa, num título só.",
    "A pergunta da CNH é a mais procurada do assunto e é a que este site ainda "
    "não responde.",
    "Três perguntas sobre o seu elétrico, e só elas: precisa de CNH e placa, "
    "quantos km ele faz de verdade no seu relevo, e se ele aguenta você.",
    "Perguntas frequentes",
    "Patinete elétrico precisa de CNH?",
)

AR_60_MAUS_PESO = (
    "Perto do limite o peso também come os km: a conta de autonomia aceita o seu "
    "peso e devolve a faixa do seu trajeto.",
    "Menos do que o anúncio promete, e o quanto menos depende do seu peso e da "
    "ladeira. A nossa calculadora de autonomia desconta a ladeira a partir da "
    "tensão e da amperagem da bateria, mostra o número do anúncio ao lado para "
    "você comparar, e diz em que ponta da faixa o seu peso deixa você.",
    "Depende da bateria, do seu peso e do relevo, e muito menos do que o anúncio "
    "diz. A nossa calculadora de autonomia desconta o relevo a partir da tensão "
    "e da amperagem, mostra o número do anúncio ao lado, e diz em que ponta da "
    "faixa o seu peso deixa você.",
    "O número do anúncio é o de quem pesa menos que você, num trajeto plano: com "
    "ladeira e com o seu peso, conte bem menos. A nossa calculadora de autonomia "
    "desconta o relevo, com a fonte do fator citada na própria página, e diz "
    "onde o seu peso põe você dentro da faixa.",
    "Três perguntas sobre veículo elétrico e só elas: precisa de CNH, quantos km "
    "faz com o seu peso e se aguenta você. Todo número com fonte e data.",
    "O fator de relevo e o desconto de peso da conta de autonomia saem de "
    "medição publicada, com autor e ano nomeados no fim da página da calculadora.",
)

AR_60_BOAS_PESO = (
    "Os seus 90 kg não entram na conta: não achamos, em fonte que alcance, "
    "nenhuma régua de quanto cada quilo de quem pilota custa em Wh por km. Eles "
    "entram aqui, no que esperar da faixa.",
    "Conta na vida real, e não conta na nossa conta — e isso está dito na "
    "resposta em vez de disfarçado. A gente não achou, em fonte que alcance, "
    "nenhuma régua de quantos watt-hora por km cada quilo de quem pilota custa. "
    "O seu peso entra aqui escolhendo o que esperar da faixa, e numa pergunta "
    "mais dura: se o modelo aguenta você.",
    "Para calibrar a expectativa: na faixa que vimos no varejo brasileiro em "
    "outubro de 2026, a carga máxima declarada ia de 115 a 140 kg, com 120 kg "
    "sendo o valor que mais se repetia. É o que observamos numa data, não um "
    "limite do mercado — e por isso a conta acima compara o seu peso com a ficha "
    "de cada veículo, nunca com esse número.",
    "Diga o seu peso e o que você leva: sai a carga máxima que a ficha precisa "
    "declarar, com a folga que a gente exige e o motivo dela.",
    "3 dos 14 veículos que declaram carga máxima no nosso banco aguentariam os "
    "seus 108 kg com folga — e nenhum deles tem oferta aberta hoje.",
    "O que o nosso banco tem para o seu peso",
)

# A REGUA VELHA, REFEITA AO LADO DA NOVA. Autoteste em que as duas concordam nao
# mede conserto nenhum (20.8): a velha e a do `teste-f1.py`, que procura DUAS
# frases imaginadas e so nas telas da F1.
def regua_velha_reprova(texto):
    s = sem_acento(texto)

    return "dispensa cnh" in s or "exige habilitacao" in s


def autoteste():
    ok = []
    mal = []

    def diz(cond, msg):
        (ok if cond else mal).append(msg)

    # MUNDO 1 — AS CINCO FRASES DE HABILITACAO QUE ESTAVAM NO AR NA REVISAO 60.
    for t in AR_60_MAUS_HABILITACAO:
        diz(len(problemas_de_habilitacao("ar60", [t])) == 1,
            "1. reprova a frase do ar da revisao 60: %r" % t[:60])

    # MUNDO 2 — AS ONZE QUE ESTAVAM CERTAS E TEM DE PASSAR. Portao que reprova a
    # pagina certa e o caminho mais curto para alguem ignora-lo (20.5).
    for t in AR_60_BOAS_HABILITACAO:
        p = problemas_de_habilitacao("ar60", [t])
        diz(not p, "2. aprova a frase CERTA do ar: %r%s"
                   % (t[:60], "" if not p else "  <-- reprovou: %s" % p[0][:120]))

    # MUNDO 3 — AS DUAS REGUAS TEM DE DISCORDAR, senao o conserto nao existe.
    # A velha so ve `dispensa CNH`/`exige habilitacao`; nenhuma das cinco frases
    # do ar diz isso, e e exatamente por isso que elas chegaram ao ar.
    discordam = [t for t in AR_60_MAUS_HABILITACAO
                 if problemas_de_habilitacao("x", [t]) and not regua_velha_reprova(t)]
    diz(len(discordam) == 5,
        "3. a regua VELHA deixa passar as 5 frases do ar e a nova reprova as 5 "
        "(discordaram em %d)" % len(discordam))

    # MUNDO 4 — O PAR DE FAQ DO ITEM 4: a resposta diz "nao" sem dizer a palavra.
    faq_mau = [("Bicicleta elétrica precisa de CNH?",
                "A de pedal assistido, dentro dos limites da resolução, não. A que anda "
                "no acelerador pode ser ciclomotor, e aí precisa.")]
    diz(len(problemas_do_faq_de_habilitacao("ld", faq_mau)) == 1,
        "4. o par de FAQ da bicicleta (revisao 60) e REPROVADO pelo PAR")
    diz(not problemas_de_habilitacao("ld", [faq_mau[0][1]]),
        "4. e a regua de FRASE NAO o pega — e por isso a do par existe")
    faq_bom = [("Bicicleta elétrica precisa de CNH?",
                "Esta página não diz. O que a resolução decide é a categoria, e sobre "
                "habilitação ela não tem artigo nenhum.")]
    diz(not problemas_do_faq_de_habilitacao("ld", faq_bom),
        "4. o par com a oracao de recusa na resposta PASSA")

    # MUNDO 5 — O PESO: as seis do ar reprovam, as seis certas passam.
    for t in AR_60_MAUS_PESO:
        diz(len(problemas_de_peso("ar60", [t])) == 1,
            "5. reprova a promessa de peso do ar: %r" % t[:60])
    for t in AR_60_BOAS_PESO:
        p = problemas_de_peso("ar60", [t])
        diz(not p, "5. aprova o texto CERTO de peso: %r%s"
                   % (t[:60], "" if not p else "  <-- reprovou: %s" % p[0][:120]))

    # MUNDO 6 — O CORTE. A regua de habilitacao corta em FRASE e a de peso corta
    # em ELEMENTO, e as duas coisas tem de ser verdade:
    #   (a) marcador de recusa numa frase nao absolve a frase vizinha;
    #   (b) a recusa da F2 gasta duas frases e NAO pode ser cortada ao meio.
    vizinhas = ("Esta página não diz nada sobre CNH. É o acelerador que decide se "
                "precisa de habilitação.")
    diz(len(problemas_de_habilitacao("x", [vizinhas])) == 1,
        "6a. a frase ruim ao lado de uma recusa continua sendo pega")
    # A FORMA DA RECUSA DA F2: a negativa numa frase, o lugar onde o peso entra
    # de verdade na seguinte. Medida nos dois cortes, para a escolha ser medicao
    # e nao gosto.
    recusa_em_duas_frases = ("Os seus 90 kg não entram na conta de autonomia. O seu peso "
                             "muda os km que você faz de verdade, e é por isso que a gente "
                             "põe o número do anúncio ao lado.")
    diz(not problemas_de_peso("x", [recusa_em_duas_frases]),
        "6b. a recusa que gasta DUAS frases passa inteira, no corte por elemento")
    por_frase = [p for f in frases(recusa_em_duas_frases) for p in problemas_de_peso("x", [f])]
    diz(len(por_frase) == 1,
        "6b. e o corte por FRASE reprovaria a segunda metade dela — as duas reguas "
        "discordam, que e o que torna a escolha do corte uma medicao")

    # MUNDO 7 — A CITACAO DE TITULO DE ANUNCIO. Dentro das aspas, passa; a mesma
    # palavra fora delas, reprova.
    diz(not problemas_de_habilitacao("x", ['O título diz “patinete 1000W sem CNH” e isso não decide nada.']),
        "7. `sem CNH` dentro de aspas de citacao passa")
    diz(len(problemas_de_habilitacao("x", ["O título diz que o patinete é sem CNH e isso decide a categoria."])) == 1,
        "7. a mesma expressao FORA das aspas reprova")

    # MUNDO 7-b — O PONTO-E-VIRGULA, e este mundo e o que TORNA O CORTE UMA
    # MEDICAO em vez de gosto. A oracao de recusa desta ilha, servida em
    # `/sobre/` e nas duas paginas de familia, junta duas clausulas por `;` e so
    # a primeira traz o marcador. Com o corte no `;` a segunda metade de um texto
    # CERTO reprovava.
    com_ponto_e_virgula = ("A Resolução Contran nº 996/2023 decide a categoria do veículo e "
                           "não tem artigo nenhum sobre CNH; quem decide habilitação é o "
                           "Código de Trânsito, e a gente ainda não o leu na fonte oficial.")
    diz(not problemas_de_habilitacao("x", [com_ponto_e_virgula]),
        "7b. a oracao de recusa com `;` passa inteira")
    por_clausula = [q for f in re.split(r"(?<=[;])\s+", com_ponto_e_virgula)
                    for q in problemas_de_habilitacao("x", [f])]
    diz(len(por_clausula) == 1,
        "7b. e o corte que inclui o `;` reprovaria a segunda clausula dela — as duas "
        "reguas discordam, e e essa discordancia que vale o corte escolhido")

    # MUNDO 8 — `kg` NAO E `km`. Foi essa letra que separou a frase do teto de
    # mercado (certa) das promessas de autonomia (erradas).
    diz(not problemas_de_peso("x", ["O seu peso contra os 120 kg declarados na ficha."]),
        "8. `seu peso` com `kg` e sem `km` nao dispara a regua da autonomia")
    diz(len(problemas_de_peso("x", ["O seu peso muda os km que a conta devolve."])) == 1,
        "8. `seu peso` com `km` dispara")

    # ======================================================================
    # MUNDO 9 — A COLHEITA CONTADA DUAS VEZES (item 4 do despacho de 09/11/2026).
    #
    # O PRIMEIRO MUNDO E O AR DA REVISAO 70, copiado letra por letra do HTML
    # servido da home as 16h2xZ de 09/11/2026 pela execucao que fechou o
    # despacho. Mundo fabricado de cabeca prova a regua contra a imaginacao de
    # quem a escreveu; este prova contra o defeito.
    # ======================================================================
    AR_70_HOME_MA = (
        "A Rodametria não copia número de anúncio: cada campo entra no nosso banco com a "
        "ficha de onde saiu e a data da leitura, e campo que a ficha não declara fica vazio "
        "em vez de ser preenchido por estimativa. Hoje o banco tem 17 veículos colhidos, "
        "4 deles com oferta aberta e rastreável, e 4 combinações de bateria já calculadas "
        "na conta de autonomia.",
        "O número grande do anúncio não é o que a regra lê: ela lê a potência NOMINAL, que "
        "fica na ficha. Dos 14 anúncios que a gente colheu, 13 declaram um watt sem dizer "
        "se é nominal ou de pico, e NENHUM declara o nominal.",
        "De 14 anúncios colhidos, nenhum declara a potência nominal e nenhum dá para "
        "classificar.",
        "A soma fecha os 17 registros do banco, contada e nunca digitada.",
    )
    p9 = problemas_de_colheita("ar70/home", list(AR_70_HOME_MA))
    diz(len(p9) == 1, "9. o AR DA REVISAO 70 da home REPROVA: 17 colhidos e 14 colhidos na "
                      "mesma pagina%s" % ("" if len(p9) == 1 else "  <-- %d achado(s)" % len(p9)))
    if p9:
        diz("17" in p9[0] and "14" in p9[0],
            "9. e a frase do defeito NOMEIA os dois numeros, para quem a ler saber onde olhar")

    # O MESMO MUNDO COM O CONSERTO: so o 17 muda de substantivo, e a pagina passa.
    AR_70_HOME_BOA = tuple(
        t.replace("17 veículos colhidos", "17 registros") for t in AR_70_HOME_MA)
    diz(not problemas_de_colheita("ar70/home-consertada", list(AR_70_HOME_BOA)),
        "9. e a MESMA pagina com `17 registros` em vez de `17 veículos colhidos` passa")

    # A DISCORDANCIA QUE TORNA ISTO MEDICAO (20.8): a regua VELHA — a que
    # cruzaria SUBSTANTIVOS — nao ve este defeito, porque os substantivos eram
    # diferentes (`veículos` e `anúncios`). Se as duas concordassem, a ancora no
    # verbo nao valeria nada.
    def velha_cruza_substantivo(elementos):
        achados = {}
        for t in elementos:
            for m in re.finditer(r"(\d[\d.]*)\s+(veiculos?|anuncios?|registros?)",
                                 sem_acento(t), re.I):
                achados.setdefault(m.group(2).rstrip("s"), set()).add(m.group(1))
        return [k for k, v in achados.items() if len(v) > 1]

    diz(not velha_cruza_substantivo(list(AR_70_HOME_MA)),
        "9. a regua VELHA (cruzando substantivos) NAO ve o defeito — os substantivos eram "
        "diferentes, e e por isso que a nova se ancora no VERBO. As duas discordam")

    # MUNDO 9-b — O QUE A REGUA NAO PODE REPROVAR.
    diz(not problemas_de_colheita("x", ["Dos 14 anúncios que a gente colheu, 13 declaram "
                                        "um watt.", "De 14 anúncios colhidos, nenhum "
                                        "declara o nominal."]),
        "9b. duas frases com a MESMA contagem (14 e 14) passam — repeticao nao e contradicao")
    diz(not problemas_de_colheita("x", ["Hoje o banco tem 17 registros, 4 deles com oferta "
                                        "aberta, e 4 combinações de bateria."]),
        "9b. numeros SEM verbo de colher nao entram na conta")
    diz(not problemas_de_colheita("x", ["De 1.000 anúncios colhidos, 1000 foram lidos na "
                                        "ficha e 1.000 colhidos tinham watt."]),
        "9b. `1.000` e `1000` sao a MESMA afirmacao: ponto de milhar nao e contradicao")
    diz(len(problemas_de_colheita("x", ["Colhemos tudo. 9 anúncios colhidos hoje.",
                                        "E 11 veículos que colhemos ontem."])) == 1,
        "9b. redacao NOVA (`que colhemos`) com numero diferente REPROVA sem ninguem "
        "ter imaginado o par")
    # O MIOLO E LIMITADO: a regua nao atravessa frase para casar um numero de uma
    # com o verbo de outra. Sem esse teto, "17 registros. Os anúncios colhidos..."
    # viraria um par falso.
    # O PONTO SEPARA AFIRMACAO: o `17` de uma frase nao pode casar com o verbo da
    # seguinte. (Escrito depois de este bloco ter nascido com um `or True`
    # pendurado nesta linha — afirmacao que passa sempre e portao INERTE, que e
    # o que o proprio `bancada.py` desta ilha denuncia por nome.)
    diz(not problemas_de_colheita("x", ["Hoje o banco tem 17 registros. Os 14 anúncios "
                                        "colhidos estão na tabela."]),
        "9b. o PONTO separa afirmacao: o 17 de uma frase nao casa com o verbo da seguinte")
    diz(not contagens_de_colheita("Hoje o banco tem 17 registros. " + ("x " * 40)
                                  + "anúncios colhidos."),
        "9b. a regua NAO atravessa 60 caracteres entre o numero e o verbo — par a "
        "distancia e par inventado")

    # MUNDO 10 — A FRASE QUE A HOME SERVIA EM NEGRITO ATE 10/11/2026, LITERAL.
    # Medida no HTML servido de https://rodametria.com.br/ as 10h2xZ de
    # 10/11/2026, na dobra "De onde sairam os limites". Ela e o mundo real e nao
    # um mundo imaginado, e esta aqui inteira porque cada defeito dela e de uma
    # CLASSE diferente — contar so o total esconderia qual regua morde o que.
    AR_10_11_PROCEDENCIA_CRUA = (
        "Resolucao CONTRAN no 996, de 15/06/2023, publicada no DOU de 22/06/2023 "
        "(Ed. 117, Secao 1, p. 327), texto ORIGINAL, em vigor desde 03/07/2023 pelo "
        "art. 22. LIDA NO PDF OFICIAL do Ministerio dos Transportes em 2026-11-05 "
        "~23h3x de Brasilia (2026-11-06 ~02h3xZ), no Chrome do Raphael."
    )
    p10 = problemas_de_procedencia("ar10/11", AR_10_11_PROCEDENCIA_CRUA)
    for classe, agulha in (
            ("nome do dono", "'Raphael'"),
            ("navegador", "'Chrome'"),
            ("acento", "'resolucao'"),
            ("acento", "'ministerio'"),
            ("acento", "'brasilia'"),
            ("data em AAAA-MM-DD", "'2026-11-05'"),
            # O `02h3xZ` DESTA FRASE NAO SAI PELA REGUA DE ZULU, e isso e desenho
            # e nao lacuna: cada regua reporta a PRIMEIRA ocorrencia dela, e o
            # `~23h3x` ja tinha reclamado a classe do marcador — que casa dentro
            # de `02h3xZ` tambem. A regua de Zulu sozinha e medida no mundo 10e.
            ("marcador de minuto", "'23h3x'"),
    ):
        diz(any(agulha in f for f in p10),
            "10. reprova %s (%s) na frase que a home servia em 10/11/2026"
            % (classe, agulha))
    # `Secao 1` e pego pelo radical `secao`, que ja estava na lista de substring.
    diz(any("'secao'" in f for f in p10),
        "10. reprova o `Secao 1` da mesma frase pelo radical que ja existia")

    # MUNDO 10b — A FRASE DE LEITOR QUE A SUBSTITUIU TEM DE PASSAR. Portao que
    # reprova a pagina certa e o caminho mais curto para alguem ignora-lo (20.5).
    boa = REGUAS.FONTE_NA_TELA["limiares-categoria-contran-996-2023"]
    pb = problemas_de_procedencia("x", boa)
    diz(not pb, "10b. aprova a frase de leitor que foi ao ar%s"
                % ("" if not pb else "  <-- reprovou: %s" % pb[0][:160]))
    # E ELA NAO PERDEU O QUE O LEITOR PRECISA: o ato, a data, o DOU, a vigencia
    # com o artigo, o texto original, o orgao e a data da leitura.
    for pedaco in ("996", "15/06/2023", "22/06/2023", "117", "327",
                   "03/07/2023", "art. 22", "original", "Transportes", "05/11/2026"):
        diz(pedaco in boa,
            "10b. a frase de leitor preserva %r, que a crua tambem dizia" % pedaco)

    # MUNDO 10c — AS DUAS REGUAS TEM DE DISCORDAR, senao o conserto nao existe
    # (20.8). A VELHA e a deste proprio portao antes de hoje: ela colhe texto de
    # tela por `textos_de_tela_do_dado`, que exclui a chave `fonte` POR NOME —
    # entao sobre um `*-respostas.json` ela colhe ZERO frase de procedencia e nao
    # tem o que reprovar, por mais defeituosa que a frase seja.
    mundo = {"id": "f1-respostas", "constantes_usadas": {
        "limiares-categoria-contran-996-2023": {
            "valor": {"LIMIAR_BIKE_W": 1000},
            "fonte": AR_10_11_PROCEDENCIA_CRUA,
        }}}
    velha = [t for _, t in textos_de_tela_do_dado("f1-respostas.json", mundo)]
    nova = frases_de_procedencia_do_dado("f1-respostas.json", mundo)
    diz(AR_10_11_PROCEDENCIA_CRUA not in velha,
        "10c. a regua VELHA nao colhe a frase de procedencia (exclui `fonte` por nome)")
    diz(len(nova) == 1 and nova[0][1] == AR_10_11_PROCEDENCIA_CRUA,
        "10c. a regua NOVA colhe a frase de procedencia do `*-respostas.json`")
    diz(len(problemas_de_procedencia(*nova[0])) >= 8,
        "10c. e a reprova em 8 classes ou mais, onde a velha reprovava em zero")

    # MUNDO 10e — A REGUA DE HORA ZULU, MEDIDA SOZINHA. Ela nao aparece no mundo
    # 10 porque la o marcador `x` reclama a classe primeiro, e regua que so e
    # exercitada por tabela de outra regua e regua que pode estar INERTE — o
    # defeito que o proprio `bancada.py` desta ilha denuncia por nome.
    pz = problemas_de_procedencia("x", "Lido no painel em 05/11/2026, às 19h17Z.")
    diz(any("19h17Z" in f for f in pz),
        "10e. a regua de hora Zulu morde `19h17Z` sozinha")
    diz(not problemas_de_procedencia("x", "Lido no painel em 05/11/2026, às 19h17."),
        "10e. e a MESMA frase sem o `Z` passa — o defeito e o fuso de servidor, "
        "nao a hora")

    # MUNDO 10d — `fonte` CONTINUA SENDO REGISTRO FORA DE `constantes_usadas`.
    # Se a colheita nova alcancasse `constantes.json`, ela reprovaria a prosa de
    # metodo do repositorio, que e o oposto do que este arquivo quer.
    diz(not frases_de_procedencia_do_dado("constantes.json", {
            "constantes": {"x": {"fonte": AR_10_11_PROCEDENCIA_CRUA}}}),
        "10d. `fonte` fora de `constantes_usadas` segue sendo registro e nao e medido")

    # ---------------------------------------------------------------------
    # MUNDO 11 — O AR DE 10/11/2026 AS 13h2xZ: A CHAVE DO TIPO COMO FRASE
    # ---------------------------------------------------------------------
    #
    # A F2 servia, em texto visivel: "Maior carga maxima que vimos no varejo —
    # 120. Tipo: observacao_de_mercado." O mundo abaixo e aquele registro.
    mundo_tipo = {"id": "f2-respostas", "constantes_usadas": {
        "teto-de-carga-do-mercado-brasileiro": {
            "valor": 120,
            "tipo": "observacao_de_mercado",
        }}}

    # AS DUAS REGUAS TEM DE DISCORDAR, senao o conserto nao existe (20.8).
    # A VELHA e a deste portao antes de hoje, e ela falha por DOIS motivos
    # independentes: `textos_de_tela_do_dado` pula cadeia SEM ESPACO (a chave nao
    # tem nenhum) e tambem cadeia com menos de 12 caracteres uteis; e a colheita
    # de campo promovido so conhecia `fonte`.
    velha_t = [t for _, t in textos_de_tela_do_dado("f2-respostas.json", mundo_tipo)]
    diz("observacao_de_mercado" not in velha_t,
        "11. a regua VELHA nao colhe a chave do tipo (ela pula cadeia sem espaco)")

    # E A NOVA TAMBEM NAO A COLHE DAQUI — e isto e o desenho, nao uma falha:
    # o conserto nao foi passar a MEDIR a chave de maquina no dado, foi parar de
    # PROMOVE-LA a tela. O `tipo` segue sendo chave de maquina no arquivo, que e
    # o papel dele; quem vai a tela e `tipo_na_tela`, e e esse que se mede.
    nova_t = frases_de_procedencia_do_dado("f2-respostas.json", mundo_tipo)
    diz(not nova_t,
        "11. e a chave `tipo` crua nao e campo promovido: o dado pode guarda-la")

    # O QUE A REGUA NOVA PEGA E A CHAVE PROMOVIDA — o mundo em que alguem
    # escreve a chave no campo que a tela imprime. ESTE e o defeito de hoje em
    # forma de dado, e a regua velha reprovava em ZERO.
    mundo_promovido = {"id": "f2-respostas", "constantes_usadas": {
        "teto-de-carga-do-mercado-brasileiro": {
            "tipo": "observacao_de_mercado",
            "tipo_na_tela": "observacao_de_mercado",
        }}}
    velha_p = [t for _, t in textos_de_tela_do_dado("f2-respostas.json", mundo_promovido)]
    nova_p = frases_de_procedencia_do_dado("f2-respostas.json", mundo_promovido)
    diz("observacao_de_mercado" not in velha_p,
        "11b. a regua VELHA segue cega a chave promovida (sem espaco)")
    diz(len(nova_p) == 1 and nova_p[0][1] == "observacao_de_mercado",
        "11b. a regua NOVA colhe o campo `tipo_na_tela`")
    diz(any("chave de maquina" in f for f in problemas_de_procedencia(*nova_p[0])),
        "11b. e o reprova por ser chave de maquina, onde a velha reprovava em zero")

    # MUNDO 11c — A REGUA NAO MORDE A FRASE CERTA. Contorcer o texto para
    # agradar regua errada e pior que a regua errada: as NOVE frases de verdade
    # passam, uma por uma.
    for tipo, frase in sorted(REGUAS.TIPO_NA_TELA.items()):
        diz(not problemas_de_procedencia("tipo %s" % tipo, frase),
            "11c. a frase de leitor do tipo %r passa limpa nas cinco reguas" % tipo)

    # MUNDO 11d — AS DUAS REGUAS DE CHAVE SAO SEPARADAS, E ESTE MUNDO EXISTE
    # PARA DIZER QUAL PEGA O QUE. Ele foi REESCRITO na propria passada que o
    # escreveu: a primeira versao afirmava que chave DENTRO de uma frase nao
    # reprova — verdade sobre `conferir_nao_e_chave_de_maquina`, que e do texto
    # INTEIRO, e falsa depois de a regua do SUBLINHADO nascer, dez minutos
    # depois, justamente para alcancar a chave no meio da frase, que e onde o
    # defeito do ar estava. O portao reprovou quem o escreveu, como o de 09/11.
    dentro = "O tipo desta régua, no arquivo, é observacao_de_mercado."
    f11d = problemas_de_procedencia("x", dentro)
    diz(any("sublinhado" in f for f in f11d),
        "11d. chave com SUBLINHADO dentro de uma frase reprova pela regua de "
        "formato — e e ali que o defeito do ar estava")
    diz(not any("chave de maquina" in f for f in f11d),
        "11d. e NAO pela regua do texto inteiro, que de fato nao a alcanca: as "
        "duas sao separadas porque o conserto de cada uma e diferente (20.5)")
    diz(any("chave de maquina" in f
            for f in problemas_de_procedencia("x", "observacao-de-mercado")),
        "11d. o slug com HIFEN, sendo o texto inteiro, reprova pela do texto inteiro")
    # E O HIFEN DENTRO DE UMA FRASE NAO REPROVA, de proposito e medido: o
    # portugues tem palavra composta, e a propria F2 serve "meio-caminho
    # geometrico" e "watt-hora". Cobrar hifen por substring reprovaria texto
    # certo — o erro do `so` dentro de "nosso", pela terceira vez.
    diz(not problemas_de_procedencia(
            "x", "O nosso é o meio-caminho geométrico entre os dois watt-hora."),
        "11d. palavra composta com hifen dentro da frase NAO reprova")

    # MUNDO 11e — A COMPLETUDE, NAS DUAS DIRECOES, sobre listas FABRICADAS.
    # O numero real sai do passe do repositorio; aqui se mede a REGUA.
    reais = set(REGUAS.TIPO_NA_TELA.keys())
    diz(REGUAS.conferir_tipos_na_tela_completos(reais) == len(reais),
        "11e. a regua aprova quando as duas listas sao a mesma, e devolve %d"
        % len(reais))
    try:
        REGUAS.conferir_tipos_na_tela_completos(reais | {"tipo_que_ninguem_traduziu"})
        diz(False, "11e. tipo declarado SEM frase de leitor tem de reprovar")
    except AssertionError as e:
        diz("tipo_que_ninguem_traduziu" in str(e),
            "11e. tipo declarado SEM frase de leitor reprova, e a mensagem o nomeia")
    try:
        REGUAS.conferir_tipos_na_tela_completos(reais - {"pendente"})
        diz(False, "11e. frase que sobrou depois de o tipo sair do JSON tem de reprovar")
    except AssertionError as e:
        diz("pendente" in str(e),
            "11e. frase sem dono no JSON reprova, e a mensagem a nomeia")
    try:
        REGUAS.conferir_tipos_na_tela_completos(set())
        diz(False, "11e. lista vazia tem de reprovar, nunca aprovar por vacuidade")
    except AssertionError:
        diz(True, "11e. lista vazia REPROVA — portao inerte nao aprova (20.8)")

    # MUNDO 11f — A LACUNA DE MOLDE PASSA, E O DEFEITO AO LADO DELA NAO.
    # O primeiro texto e o molde REAL da F1 que reprovou a regua do sublinhado no
    # minuto em que ela nasceu; o segundo e o mesmo molde com uma chave de
    # verdade solta na prosa, e ele TEM de reprovar — senao o desconto da lacuna
    # teria aberto um buraco em vez de fechar um falso positivo.
    molde_real = ("É bicicleta elétrica: {lim_w} W de potência nominal e {lim_kmh} "
                  "km/h, só com pedal assistido.")
    diz(not problemas_de_procedencia("molde da F1", molde_real),
        "11f. a lacuna `{lim_w}` do molde real da F1 NAO reprova: slot nao e frase")
    diz(any("sublinhado" in f for f in problemas_de_procedencia(
            "x", molde_real + " Tipo: observacao_de_mercado.")),
        "11f. e a chave de verdade ao lado da lacuna REPROVA — o desconto remove a "
        "lacuna, nunca a regua")

    print("")
    print("  AUTOTESTE — %d mundo(s) medido(s), %d falha(s)" % (len(ok) + len(mal), len(mal)))
    for m in mal:
        print("    FALHA  %s" % m)
    if not mal:
        print("  APROVADO")
    else:
        print("  REPROVADO")

    return 0 if not mal else 1


def main():
    if "--autoteste" in sys.argv:
        return autoteste()

    afirmacoes, falhas = medir_repositorio()
    print("")
    print("  AFIRMACAO DE TELA — %d afirmacao(oes) no repositorio, %d falha(s)"
          % (afirmacoes, len(falhas)))
    for f in falhas:
        print("    FALHA  %s" % f)
    print("")
    if falhas:
        print("  REPROVADO")
        return 1
    print("  APROVADO")

    return 0


if __name__ == "__main__":
    sys.exit(main())

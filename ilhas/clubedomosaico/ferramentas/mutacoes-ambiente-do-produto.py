#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO BALDE DO AMBIENTE DO PRODUTO — 07/10/2026, esquema v15, REGRA 3.

O BURACO QUE ESTA BATERIA FECHA e o mais silencioso que esta ilha ja mediu, e a
forma dele e nova: a regra 3 sempre eliminou CERTO. Ela existe desde o bloco 3,
nenhuma celula da matriz jamais discordou dela, e por 27 dias ela mandou quem
eliminava para o balde do SILENCIO — que serve, na tela, "O fabricante
simplesmente nao fala desta superficie". Os fabricantes falam: a base esta em
`indicado_para` e a regra 2, que roda ANTES da 3, ja a deixou passar.

ENTAO O DEFEITO NAO ESTAVA NA ELEGIBILIDADE, E E POR ISSO QUE NADA O VIU. Toda
regua desta ilha — a matriz de 45 celulas, o censo de 270 estados, as oito
bancadas PHP, as 26 baterias de mutacao — media CONCORDANCIA entre o que o banco
calcula e o que a pagina serve. As duas concordavam. As duas diziam a mesma coisa
errada, em 29 entradas de 24 celulas, desde 10/09/2026.

A LICAO QUE ESTA BATERIA EXISTE PARA GUARDAR: regra que troca de BALDE nao muda
nenhum numero. Portao que compara listas de elegiveis nunca a vai pegar — so
portao que compara FRASES pega, e frase se mede no HTML servido. Por isso a
metade de tela aqui e maior que a de forma, ao contrario das irmas.

AS TRES REGRAS HERDADAS das baterias irmas, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao de forma roda o validador duas vezes, desligando as travas novas
      com CDM_SEM_PORTAO_AMBIENTE_DO_PRODUTO=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco nao tem. Sao
      tres, todas no registro: m14 da `ambientes_declarados` ao Silicone Neutro e
      cria o QUARTO delimitador, que hoje nao existe; m15 apaga a delimitacao do
      PL500 e devolve as 24 celulas dele a recomendacao, que e o mundo de antes da
      regra 3; m16 alarga a delimitacao dele para incluir area molhada e externa,
      e so UMA celula sai do balde — o mundo em que a regra morde menos.
      E UMA QUARTA FOI ESCRITA, PASSOU, E VIROU FALSO POSITIVO: a primeira versao
      da m14 acrescentava ao MAPA um termo de ambiente novo, dizendo ser a metade
      de cima do quarto delimitador. Nao era defeito — termo que registro nenhum
      cita nao delimita nada — e esta na fp5. Mutacao que passa com razao nao se
      conserta para reprovar: ela muda de lado.

  (c) ESTA BATERIA MEDE O FALSO POSITIVO. Cinco estados legitimos tem de passar,
      entre eles o que mais se parece com defeito: o produto que NAO delimita
      ambiente nenhum, que e o estado de 4 das 7 colas do banco.

E A MUTACAO MAIS IMPORTANTE DE TODAS E A t01, que e o defeito exato que este
bloco consertou: um `return` trocado, de `ambiente_do_produto` para `silencio`.
Ela nao muda uma lista, nao muda um numero, nao muda a matriz — muda a frase que
o leitor recebe, e e a frase que esta pagina vende. Se um dia alguem a desfizer
por engano, e a t01 que acusa.

Uso:  python3 ferramentas/mutacoes-ambiente-do-produto.py
"""

import copy
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")
TESTE_F2 = os.path.join(AQUI, "teste-f2.php")
SNIPPET = os.path.join(ILHA, "snippets", "clubedomosaico-f2.php")
RENDER = os.path.join(AQUI, "render-para-teste.php")

ARQUIVOS = {
    "esquema": os.path.join(ILHA, "dados", "esquema-banco.json"),
    "colas":   os.path.join(ILHA, "dados", "materiais-colas.json"),
}

PL = "cascola-pl500-adesivo-de-montagem"
CZ = "cascola-cascorez-extra"
AC = "quartzolit-cimentcola-externo-acii"
NE = "tekbond-silicone-neutro"
BLOCO = "regras_do_balde_do_ambiente_do_produto"
BALDE = "eliminados_por_ambiente_do_produto"

L_PL = "uso interno"
L_CZ = "ambientes internos"
L_AC = "área interna e externa"

# OS ESTADOS SERVIDOS QUE ESTA BATERIA LE, com o caquinho que a AC-II nao proibe.
# E_CAI e E_PASSA sao a MESMA base trocando so o lugar: e a forma com que esta ilha
# mede regra de ambiente desde a regra 6, e a unica que separa "a regra morde" de "a
# regra morde sempre".
E_CAI = "base=mdf_madeira&onde=externo_abrigado&caco=caco_azulejo"
E_PASSA = "base=mdf_madeira&onde=interno_seco&caco=caco_azulejo"
# e a celula onde a REGRA 8 morde e a 3 nao escreve nada: a prova de que os dois
# baldes de ambiente sao dois
E_REGRA_8 = "base=alvenaria_tijolo&onde=externo_abrigado&caco=caco_azulejo"

FRASE_NOVA = "delimitou o produto inteiro a outros lugares"
FRASE_DO_SILENCIO = "O fabricante simplesmente não fala desta superfície"
FRASE_DA_REGRA_8 = "declara esta superfície, e declara com o lugar dentro da frase"


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


def linha(esq, produto):
    for l in esq[BLOCO]["produtos_que_delimitam_ambiente_hoje"]:
        if l["produto"] == produto:
            return l
    raise SystemExit("mutacao aponta para linha inexistente: %s" % produto)


def celula(esq, base, ambiente):
    for c in esq["matriz_esperada_da_F2"]["celulas"]:
        if c["base"] == base and c["ambiente"] == ambiente:
            return c
    raise SystemExit("mutacao aponta para celula inexistente: %s x %s" % (base, ambiente))


# ------------------------------------------------- mutacoes de FORMA (validador)

def m01(e):
    """O BLOCO DE REGRAS DESAPARECE e os produtos que delimitam ficam. E a direcao
    perigosa escrita como mutacao, e ela e ao contrario da da regra 8: aqui perder o
    bloco nao muda elegibilidade nenhuma — muda so quem escreveu PARA ONDE o produto
    vai e O QUE a tela diz. Sem a trava, a proxima execucao o devolve ao silencio sem
    nada ficar vermelho."""
    del e[BLOCO]


def m02(e):
    """A REGRA 3 VOLTA A SER PROSA SOLTA em `regras_de_elegibilidade`. Era assim que
    ela vivia ate 07/10/2026: uma frase descrevendo o que a regua faz, sem nomear
    balde nenhum. Forma sem a regra e campo que ninguem le."""
    e["regras_de_elegibilidade"]["3_ambiente_declarado_DELIMITA"] = \
        e["regras_de_elegibilidade"]["3_ambiente_declarado_DELIMITA"]["regra"]


def m03(e):
    """A REGRA 3 NOMEIA O BALDE ERRADO: ela passa a dizer que manda o produto para
    `eliminados_por_silencio`, que e o balde de onde ele saiu. Regra que descreve
    outro balde aprova o balde errado — e este e o balde exato do defeito."""
    e["regras_de_elegibilidade"]["3_ambiente_declarado_DELIMITA"]["o_balde"] = \
        "eliminados_por_silencio"


def m04(e):
    """A REGRA 3 PERDE A LINHA QUE A SEPARA DA REGRA 8. Os dois baldes sao vizinhos,
    falam os dois de ambiente, e sem a frase que diz por que sao dois a proxima
    execucao os junta — que e a mistura de causas que a secao 7 do contrato proibe."""
    del e["regras_de_elegibilidade"]["3_ambiente_declarado_DELIMITA"][
        "e_ela_NAO_SE_JUNTA_a_regra_8"]


def m05(e):
    """O BLOCO PERDE A `regra_da_direcao`. Lista sem direcao escrita e lista que a
    proxima execucao preenche pelo lado errado."""
    del e[BLOCO]["regra_da_direcao"]


def m06(e):
    """O BLOCO PERDE A FRASE `cita_o_literal`. A regra nasceu por causa da FRASE, e
    um bloco que nao escreve a frase e a regra sem a metade dela — a 26.3 e a razao
    de o balde existir, nao um detalhe de apresentacao."""
    del e[BLOCO]["o_que_a_tela_tem_de_dizer"]["cita_o_literal"]


def m07(e):
    """A TABELA ESCONDE UM PRODUTO QUE DELIMITA: a linha do PL500 sai. Tabela que nao
    lista o delimitador existente e tabela que aprova o produto novo entrando mudo —
    e o PL500 e o maior dos tres, com 24 das 29 entradas."""
    e[BLOCO]["produtos_que_delimitam_ambiente_hoje"] = [
        l for l in e[BLOCO]["produtos_que_delimitam_ambiente_hoje"] if l["produto"] != PL]


def m08(e):
    """A TABELA CITA UMA FRASE QUE O REGISTRO NAO TEM. E a forma mais limpa de a regua
    medir ficcao: a tela cita `ambientes_declarados` e a tabela diria que ele escreveu
    uma coisa que ele nao escreveu."""
    linha(e, PL)["literais"] = ["Para uso em qualquer ambiente."]


def m09(e):
    """A CONTAGEM MENTE: `entradas_no_balde` do PL500 passa de 24 para 29. E o erro
    exato do registro de 06/10/2026, que escreveu `29 celulas` onde sao 29 ENTRADAS em
    24 celulas — duas contagens verdadeiras sobre coisas diferentes. A regua recomputa
    as duas e e por isso que a confusao nao sobrevive a este commit."""
    linha(e, PL)["entradas_no_balde"] = 29


def m10(e):
    """O TOTAL DE CELULAS MENTE: 24 passa a 29, que e o numero que o registro de 06/10
    escreveu. A direcao e a mesma da m09 e o campo e o outro — os dois numeros tem de
    ser cobrados separados, senao trocar um pelo outro fica verde."""
    e[BLOCO]["total_de_celulas_tocadas_hoje"] = 29


def m11(e):
    """A ANCORA ANTI-FUSAO PERDE O `eliminados_por_silencio`. Sem ela, a tabela nao
    distingue o balde novo cheio POR DIREITO do balde novo cheio ROUBANDO do silencio
    — e roubar do silencio e o defeito mais provavel desta regra, porque a
    implementacao errada e mais curta que a certa."""
    for a in e[BLOCO]["ancoras_ponta_a_ponta"]:
        a.pop("eliminados_por_silencio", None)


def m12(e):
    """TODAS AS ANCORAS PASSAM A MORDER: a que PASSA (madeira dentro de casa) ganha os
    dois Cascola no balde. Tabela de um lado so nao mede regra nenhuma, e deste lado
    ela aprovaria uma regra 3 que tira o produto do ambiente que o fabricante
    DECLARA."""
    for a in e[BLOCO]["ancoras_ponta_a_ponta"]:
        if a["base"] == "mdf_madeira" and a["ambiente"] == "interno_seco":
            a[BALDE] = [CZ, PL]


def m13(e):
    """A MATRIZ DEVOLVE UMA ENTRADA AO SILENCIO: na celula de madeira ao ar livre, o
    PL500 volta para `eliminados_por_silencio`. E o defeito de 10/09 a 06/10 escrito
    numa celula so — e a matriz de hoje tem de reprovar, porque ela e a prova de que a
    causa esta separada."""
    c = celula(e, "mdf_madeira", "externo_abrigado")
    c[BALDE].remove(PL)
    c["eliminados_por_silencio"] = sorted(c["eliminados_por_silencio"] + [PL])


def m14(c):
    """PRODUZ O MUNDO QUE O BANCO NAO TEM: NASCE O QUARTO DELIMITADOR. O Silicone Neutro
    ganha `ambientes_declarados`, com um literal que o mapa JA traduz (o do Cascorez), e
    com ele a regra 3 passa a morder em celulas novas — o neutro sai de `cimento_concreto`
    e de `alvenaria_tijolo` em quatro ambientes cada. Qualquer frase da tabela ou da regua
    escrita sobre TRES produtos quebra aqui.

    A PRIMEIRA VERSAO DESTA MUTACAO ERA DUAS, E A PRIMEIRA DELAS NAO ERA DEFEITO: ela
    acrescentava ao mapa um termo novo com `ambiente`, dizendo que ele era a metade de
    cima do quarto delimitador. Ela PASSOU, e passou com razao — termo que registro nenhum
    cita nao e delimitador de nada, do mesmo jeito que o termo com qualificador que
    ninguem cita e falso positivo na `mutacoes-par.py`. Virou a fp5 aqui embaixo. O que
    produz o mundo e esta metade, a do REGISTRO, e ela nao precisa da outra: o literal
    `ambientes internos` ja esta no mapa desde que o Cascorez entrou."""
    item(c, NE)["declaracoes"]["ambientes_declarados"] = ["ambientes internos"]


def m15(c):
    """NO BANCO: a delimitacao do PL500 DESAPARECE. Sem `ambientes_declarados` ele deixa
    de cair pela regra 3 e volta a ser recomendado em madeira ao ar livre, em cozinha e
    em area molhada — 24 celulas em que o fabricante escreveu `uso interno`. E a direcao
    que publica MAIS do que ele disse, e a matriz escrita a mao e quem acusa."""
    item(c, PL)["declaracoes"]["ambientes_declarados"] = []


def m16(c):
    """NO BANCO: a delimitacao do PL500 ALARGA para incluir area molhada. O literal
    continua sendo `uso interno` e o mapa e que mudaria de leitura — aqui a mutacao e no
    registro, trocando a frase por uma que o mapa traduz largo. Uma celula sai do balde
    e a matriz acusa."""
    item(c, PL)["declaracoes"]["ambientes_declarados"] = ["área interna e externa"]


MUTACOES_FORMA = [
    ("m01 o bloco de regras desaparece e os delimitadores ficam", "esquema", m01),
    ("m02 a regra 3 volta a ser prosa solta",                     "esquema", m02),
    ("m03 a regra 3 nomeia o balde do SILENCIO",                  "esquema", m03),
    ("m04 a regra 3 perde a linha que a separa da 8",             "esquema", m04),
    ("m05 o bloco perde a regra_da_direcao",                      "esquema", m05),
    ("m06 o bloco perde a frase `cita_o_literal`",                "esquema", m06),
    ("m07 a tabela esconde o PL500 (24 das 29 entradas)",         "esquema", m07),
    ("m08 a tabela cita frase que o registro nao tem",            "esquema", m08),
    ("m09 a contagem de entradas do PL500 mente (24 -> 29)",      "esquema", m09),
    ("m10 o total de CELULAS mente (24 -> 29)",                   "esquema", m10),
    ("m11 a ancora anti-fusao perde o silencio ao lado",          "esquema", m11),
    ("m12 TODAS as ancoras passam a morder",                      "esquema", m12),
    ("m13 a matriz devolve uma entrada ao silencio",              "esquema", m13),
    ("m14 PRODUZ: nasce o QUARTO delimitador no banco",           "colas",   m14),
    ("m15 no banco: a delimitacao do PL500 desaparece (publica MAIS)", "colas", m15),
    ("m16 no banco: a delimitacao do PL500 alarga",               "colas",   m16),
]


# ------------------------------------------------------- mutacoes de TELA (F2)

def t01(snippet):
    """O DEFEITO EXATO QUE ESTE BLOCO CONSERTOU, e e um `return` so: a regra 3 volta a
    devolver `silencio`. Nenhuma lista muda, nenhum numero muda, a matriz continuaria
    batendo se ela fosse escrita com o balde antigo — e a pagina volta a dizer que o
    fabricante nao fala de uma superficie que ele declara em `indicado_para`. Esta e a
    mutacao que justifica a bateria inteira."""
    velho = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}"""
    novo = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}"""
    assert velho in snippet, "a ancora do return da regra 3 nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t02(snippet):
    """A ORDEM TROCA: a regra 3 passa a rodar ANTES da 2. Com ela antes, o produto que
    NAO declara a base e que delimita ambiente cai no balde novo, e a pagina passa a
    dizer `ela declara esta superficie` sobre uma superficie que ele nunca nomeou — o
    defeito consertado virado do avesso. A elegibilidade e a MESMA nas duas ordens."""
    velho = """	/* 2 — base sem declaração não é recomendação. Silêncio não vira "pode". */
	if ( ! isset( $p['bases_indicadas'][ $base ] )
		&& ! isset( $p['bases_indicadas_so_em'][ $base ] ) ) {
		return array( 'silencio', 0 );
	}"""
    assert velho in snippet, "a ancora da regra 2 nao esta no snippet"
    alvo = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}"""
    assert alvo in snippet, "a ancora do return da regra 3 nao esta no snippet"
    s = snippet.replace(alvo, "", 1)
    return s.replace(velho, alvo + "\n" + velho, 1)


def t03(snippet):
    """A TELA PARA DE CITAR A FRASE DO FABRICANTE e passa a dizer o nosso vocabulario.
    E a 26.3 ao contrario: quem traduziu `uso interno` para `interno_seco` fomos nos, e
    por a nossa leitura na boca dele e o defeito que esta ilha paga com mais
    frequencia."""
    velho = """			if ( $lits ) {
				$html .= ': ela escreve <em>' . esc_html( cdm_f2_lista_humana( $lits ) ) . '</em>';
			}"""
    novo = """			if ( $lits ) {
				$html .= ': ela escreve <em>ambiente interno seco</em>';
			}"""
    assert velho in snippet, "a ancora da citacao do balde novo nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t04(snippet):
    """A TELA CITA O LITERAL ERRADO: em vez de `ambientes_declarados`, ela passa a citar
    os literais de COBERTURA, que misturam `indicado_para` e `resistencias_declaradas`.
    Era assim que o perfil guardava a informacao antes deste bloco — num campo so — e a
    frase sairia com o nome do substrato no lugar do lugar."""
    velho = "			$lits = $p['literais_delimitacao'];"
    novo = """			$lits = array();
			foreach ( $p['literais_cobertura'] as $alvo => $ls ) {
				foreach ( $ls as $l ) { $lits[] = $l; }
			}
			$lits = array_values( array_unique( $lits ) );"""
    assert velho in snippet, "a ancora dos literais da delimitacao nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t05(snippet):
    """OS DOIS BALDES VIRAM UM. O paragrafo da regra 3 passa a usar a frase da regra 8,
    palavra por palavra. A elegibilidade nao muda, as listas nao mudam, e a pagina
    passa a dizer que o lugar vem colado dentro da frase do substrato quando ele e
    campo do produto inteiro — a mistura de causas que a secao 7 proibe."""
    velho = """				. '</strong> — a ' . esc_html( $m['fabricante'] ) . ' declara esta superfície, e '
				. 'delimitou o produto inteiro a outros lugares';"""
    novo = """				. '</strong> — a ' . esc_html( $m['fabricante'] ) . ' declara esta superfície, e declara '
				. 'com o lugar dentro da frase';"""
    assert velho in snippet, "a ancora da frase do balde novo nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t06(snippet):
    """O PARAGRAFO DESAPARECE DA TELA e a celula perde a causa inteira: o produto sai da
    pagina sem uma palavra, nem recomendado, nem proibido, nem em silencio. E o estado
    que o `return ''` precoce de `cdm_f2_fora_html` produziria se ele nao soubesse do
    balde novo — e e o mesmo buraco que a grade das tecnicas e o censo tinham para a
    regra 8 ate hoje."""
    velho = "	if ( $celula['eliminados_por_ambiente_do_produto'] ) {\n		foreach"
    novo = "	if ( false && $celula['eliminados_por_ambiente_do_produto'] ) {\n		foreach"
    assert velho in snippet, "a ancora do paragrafo do balde novo nao esta no snippet"
    return snippet.replace(velho, novo, 1)


MUTACOES_TELA = [
    {
        "nome": "t01 O DEFEITO: a regra 3 volta a devolver `silencio`",
        "funcao": t01, "estado": E_CAI,
        "sai": [FRASE_NOVA],
        "entra": [FRASE_DO_SILENCIO],
        "por_que": "um `return` so, nenhuma lista muda, e a pagina volta a dizer que ele nao fala",
    },
    {
        "nome": "t02 a ordem troca: a regra 3 roda ANTES da 2",
        "funcao": t02, "estado": "base=espelho&onde=externo_abrigado&caco=caco_azulejo",
        "sai": [],
        "entra": [FRASE_NOVA],
        "por_que": "em espelho, que nenhum dos tres declara, a frase passa a afirmar que ele declara",
    },
    {
        "nome": "t03 a tela troca a citacao pelo nosso vocabulario",
        "funcao": t03, "estado": E_CAI,
        # O MARCADOR NAO PODE SER `uso interno` SOZINHO, e isto foi MEDIDO: a primeira
        # versao desta linha procurava o literal cru e a mutacao PASSOU. A frase
        # `o produto e declarado para uso interno` esta no FAQ desta mesma pagina, duas
        # vezes (no JSON-LD e no <dd>), e continua la depois da mutacao. Marcador que
        # existe nos DOIS lados da mutacao nao mede nada — e e a mesma cicatriz que a t04
        # da `mutacoes-par.py` ja tinha escrito, um dia antes, com outro literal. O que
        # so existe no paragrafo do balde e a citacao INTEIRA, com a tag dentro.
        "sai": ["ela escreve <em>" + L_PL + "</em>"],
        "entra": ["ela escreve <em>ambiente interno seco</em>"],
        "por_que": "26.3: a frase e dele, a traducao e nossa, e a tela nao pode trocar uma pela outra",
    },
    {
        "nome": "t04 a tela cita os literais de COBERTURA em vez da delimitacao",
        "funcao": t04, "estado": E_CAI,
        # O MARCADOR E A CITACAO INTEIRA, pelo mesmo motivo medido na t03: `madeira` existe
        # nos dois lados da mutacao (e o proprio rotulo da base nesta pagina). Medido na
        # tela mutada, a frase passa a trazer os literais do SUBSTRATO colados no do lugar
        # — `uso interno, metal, porcelana, plasticos, madeira, concreto e vidro` —, que e
        # exatamente o campo so que este bloco separou em dois.
        "sai": ["ela escreve <em>" + L_PL + "</em>"],
        "entra": ["ela escreve <em>" + L_PL + ", metal, porcelana"],
        "por_que": "o literal do substrato entra no lugar do literal do lugar — campo so, frase errada",
    },
    {
        "nome": "t05 os dois baldes de ambiente viram UM (a frase da 8 na 3)",
        "funcao": t05, "estado": E_CAI,
        "sai": [FRASE_NOVA],
        "entra": [FRASE_DA_REGRA_8],
        "por_que": "mistura de causas: o lugar do produto descrito como lugar colado no substrato",
    },
    {
        "nome": "t06 o paragrafo do balde novo desaparece da tela",
        "funcao": t06, "estado": E_CAI,
        "sai": [FRASE_NOVA],
        "entra": [],
        "por_que": "o produto sai da pagina sem uma palavra — nem recomendado, nem fora, nem em silencio",
    },
]


# ----------------------------------------- a trava do falso positivo (regra c)

def fp1(e):
    """O ESTADO DE 4 DAS 7 COLAS DO BANCO: produto sem `ambientes_declarados`. E o mais
    comum e o que mais se parece com campo esquecido — e e justamente o estado que faz a
    regra 3 nao morder, porque nao ha o que delimitar."""
    e[BLOCO]["observacao_da_bateria"] = "4 das 7 colas nao delimitam ambiente nenhum"


def fp2(e):
    """A ORDEM DAS LINHAS DA TABELA MUDA. A lista de delimitadores e um conjunto, nao
    uma sequencia: a regua a compara ordenada, e um portao sensivel a ordem reprovaria
    diff de arrumacao."""
    e[BLOCO]["produtos_que_delimitam_ambiente_hoje"].reverse()


def fp3(e):
    """A ORDEM DAS ANCORAS MUDA, pelo mesmo motivo da fp2 e num campo diferente: a
    tabela de ancoras tambem e conjunto, e a trava dos dois lados conta quantas mordem,
    nunca em que posicao elas estao."""
    e[BLOCO]["ancoras_ponta_a_ponta"].reverse()


def fp4(c):
    """NO BANCO: a frase de `ambientes_declarados` do Cascorez e reescrita com acento e
    caixa diferentes — `Ambientes Internos`. O mapa normaliza antes de comparar (minusculas,
    sem acento, espacos colapsados), entao a traducao e a MESMA e a regra morde igual.

    E A METADE QUE ESTA FIXTURE MEDE DE VERDADE, porque ela quase nao passou: a tela cita
    o LITERAL, e o literal mudou de forma. A tabela do esquema guarda o literal exato do
    registro e o validador os compara — entao a tabela acompanha a mutacao. Se ela nao
    acompanhasse, isto nao seria falso positivo: seria a tabela citando uma frase que o
    registro nao tem, que e exatamente a m08."""
    item(c, CZ)["declaracoes"]["ambientes_declarados"] = ["Ambientes Internos"]


def fp4_esquema(e):
    """A metade de esquema da fp4: a tabela acompanha o literal reescrito."""
    linha(e, CZ)["literais"] = ["Ambientes Internos"]


def fp5(e):
    """UM TERMO NOVO DE AMBIENTE, e registro nenhum o cita. Termo que ninguem usa nao
    delimita nada, entao a tabela dos delimitadores nao o lista e a regua nao pode
    cobra-lo: a lista e dos produtos que o BANCO tem, nunca dos que o mapa poderia
    produzir.

    ESTA FIXTURE NASCEU DE UMA MUTACAO QUE PASSOU, e e por isso que ela esta aqui em vez
    de uma linha a mais na forma: escrita como m14, ela afirmava ser a metade de cima do
    quarto delimitador e esperava reprovacao. Ninguem a pegou — porque nao havia o que
    pegar. Irma exata da fp3 da `mutacoes-par.py`, achada pelo mesmo caminho."""
    e["mapa_de_termos_do_fabricante"]["termos"].append({
        "literal": "para uso em interiores",
        "base": [],
        "ambiente": ["interno_seco"],
    })


FALSOS_POSITIVOS = [
    ("produto sem `ambientes_declarados` (4 das 7 colas)", [("esquema", fp1)]),
    ("termo de ambiente que registro nenhum cita",         [("esquema", fp5)]),
    ("a ordem das linhas da tabela muda",                  [("esquema", fp2)]),
    ("a ordem das ancoras muda",                           [("esquema", fp3)]),
    ("o literal muda de acento e caixa (o mapa normaliza)",
     [("colas", fp4), ("esquema", fp4_esquema)]),
]


def roda_validador(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_AMBIENTE_DO_PRODUTO"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def roda_bancada():
    r = subprocess.run(["php", TESTE_F2, "."], capture_output=True, text=True, cwd=ILHA)
    return r.returncode != 0


def serve(estado):
    r = subprocess.run(["php", RENDER, ".", "cdm_f2", "hoje", estado],
                       capture_output=True, text=True, cwd=ILHA)
    return r.stdout


# O RETRATO E DE BYTES, NUNCA DE CONTEUDO. Cicatriz medida em 06/10/2026 nas
# `mutacoes-apoio.py` e `mutacoes-base.py`: elas restauravam re-serializando o objeto
# guardado em memoria, e os arquivos que tocavam nao terminavam em quebra de linha.
# Passada verde, conteudo identico, `sha256` TROCADO — e o manifest guarda esse sha.
def retrato(caminhos):
    return {c: open(c, "rb").read() for c in caminhos}


def restaura(bytes_de):
    for caminho, b in bytes_de.items():
        with open(caminho, "wb") as fh:
            fh.write(b)


def main():
    todos = list(ARQUIVOS.values()) + [SNIPPET]
    bytes_originais = retrato(todos)
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in ARQUIVOS.items()}
    snippet_original = open(SNIPPET, encoding="utf-8").read()
    reprovadas = so_o_portao_novo = telas = fp_ok = 0

    try:
        if roda_validador():
            print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
            return 1
        if roda_validador(sem_portao_novo=True):
            print("FALHA: o banco ja esta reprovado com as travas do balde desligadas")
            return 1
        if roda_bancada():
            print("FALHA: a bancada da F2 ja esta vermelha ANTES de qualquer mutacao")
            return 1

        print("Mutacoes do balde do ambiente do produto (esquema v15, REGRA 3) — "
              "%d de forma + %d de tela" % (len(MUTACOES_FORMA), len(MUTACOES_TELA)))
        print("")
        print("  A FORMA E A CONTAGEM — quem pega e o validar-banco.py:")
        for nome, qual, funcao in MUTACOES_FORMA:
            mutado = copy.deepcopy(originais[qual])
            funcao(mutado)
            if mutado == originais[qual]:
                print("    INERTE  %s — a mutacao nao mudou nada" % nome)
                return 1
            with open(ARQUIVOS[qual], "w", encoding="utf-8") as fh:
                json.dump(mutado, fh, ensure_ascii=False, indent=2)
            try:
                pegou = roda_validador()
                pegou_sem = roda_validador(sem_portao_novo=True)
            finally:
                restaura({ARQUIVOS[qual]: bytes_originais[ARQUIVOS[qual]]})
            if not pegou:
                print("    PASSOU  %s — NINGUEM a pegou" % nome)
                return 1
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
            print("    %s  %s" % ("so o portao novo" if not pegou_sem else "ja pegava     ", nome))

        print("")
        print("  A TELA E A FRASE — quem pega e o render da F2 e o teste-f2.php:")
        for mut in MUTACOES_TELA:
            open(SNIPPET, "w", encoding="utf-8").write(mut["funcao"](snippet_original))
            try:
                html = serve(mut["estado"])
                bancada_verde = not roda_bancada()
            finally:
                restaura(bytes_originais)
            problemas = []
            if bancada_verde:
                problemas.append("a bancada da F2 ficou VERDE")
            for frase in mut["sai"]:
                if frase in html:
                    problemas.append("a frase que tinha de SAIR continua na tela: %r" % frase[:40])
            for frase in mut["entra"]:
                if frase not in html:
                    problemas.append("a frase que tinha de ENTRAR nao entrou: %r" % frase[:40])
            if problemas:
                print("    PASSOU  %s — %s" % (mut["nome"], "; ".join(problemas)))
                return 1
            telas += 1
            print("    reprovada  %s" % mut["nome"])

        print("")
        print("  O FALSO POSITIVO — estes TEM de passar:")
        for nome, partes in FALSOS_POSITIVOS:
            mutados = {}
            for qual, funcao in partes:
                mutado = mutados.get(qual) or copy.deepcopy(originais[qual])
                funcao(mutado)
                mutados[qual] = mutado
            for qual, mutado in mutados.items():
                if mutado == originais[qual]:
                    print("    INERTE  %s — a fixture nao mudou nada em %s" % (nome, qual))
                    return 1
                with open(ARQUIVOS[qual], "w", encoding="utf-8") as fh:
                    json.dump(mutado, fh, ensure_ascii=False, indent=2)
            try:
                pegou = roda_validador()
            finally:
                restaura(bytes_originais)
            if pegou:
                print("    REPROVOU  %s — e isto e FALSO POSITIVO" % nome)
                return 1
            fp_ok += 1
            print("    passou    %s" % nome)
    finally:
        restaura(bytes_originais)
        # e a arvore tem de voltar limpa, BYTE A BYTE
        for caminho, b in bytes_originais.items():
            if open(caminho, "rb").read() != b:
                print("FALHA: %s nao voltou byte a byte" % os.path.basename(caminho))
                return 1

    print("")
    print("%d de %d mutacoes de forma reprovadas, %d so pelo portao novo; "
          "%d de %d de tela; %d de %d falsos positivos passaram"
          % (reprovadas, len(MUTACOES_FORMA), so_o_portao_novo,
             telas, len(MUTACOES_TELA), fp_ok, len(FALSOS_POSITIVOS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

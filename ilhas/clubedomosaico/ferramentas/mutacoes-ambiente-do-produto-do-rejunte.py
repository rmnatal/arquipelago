#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO BALDE DO AMBIENTE DO PRODUTO DO REJUNTE — 07/10/2026, esquema v16.

O MESMO DEFEITO UM ANDAR ABAIXO DA COLA, e a forma dele e identica: a regra 3 do
rejunte sempre eliminou CERTO. Nenhuma celula da matriz jamais discordou dela, e
por 27 dias ela mandou quem eliminava para o balde `eliminados_por_ambiente` —
que era TAMBEM o da regra 2 e serve, na tela, "Fora porque o fabricante nao
declara este lugar". O fabricante declara: o `quartzolit-rejunte-acrilico`
escreve `areas internas e externas` em `ambientes_declarados`, e e justamente
essa frase que o fecha.

OS NUMEROS, varridos nos 60 estados (12 folgas x 5 lugares) em 07/10/2026:

    regra 3 (delimitacao)     8 entradas em  8 estados   a frase estava ERRADA
    regra 2 (critico)        59 entradas em 28 estados   a frase estava certa
    os dois no mesmo estado                 7 estados

E DUAS COISAS QUE ESTA BATERIA GUARDA E A DA COLA NAO TINHA:

  (1) SAO DUAS TELAS. A celula do rejunte e lida pela F2 e pela F1, e as duas
      serviam a frase errada com palavras diferentes — a F1 dizia "o que ele nao
      declara e peca <lugar>". Conserto que chegasse so a uma delas trocaria uma
      tela mentindo por duas telas discordando. A t06 e dela.

  (2) A FUSAO MAIS PROVAVEL AQUI NAO E COM O SILENCIO, E COM A FAIXA DE JUNTA.
      A regra 1 roda ANTES da 3, e de 5 mm para cima o acrilico sai por folga, nao
      por lugar. Quem implementar "produto que delimita ambiente e nao cobre o
      lugar vai para o balde novo" poe no balde quem nem cabe na folga, e a
      elegibilidade continua identica. A t05 e dela.

AS TRES REGRAS HERDADAS das baterias irmas, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao de forma roda o validador duas vezes, desligando as travas novas
      com CDM_SEM_PORTAO_AMBIENTE_DO_PRODUTO_REJUNTE=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco nao tem. Sao
      tres, todas no registro: m17 da `ambientes_declarados` ao epoxi e cria o
      SEGUNDO delimitador, que hoje nao existe — e e ele que separa as duas
      contagens que hoje coincidem por acidente de haver um produto so; m18 apaga
      a delimitacao do acrilico e devolve as 8 entradas, que e o mundo de antes da
      regra 3; m19 alarga a delimitacao dele para alcancar o sol e a chuva, e
      metade das entradas sai do balde.

  (c) ESTA BATERIA MEDE O FALSO POSITIVO. Cinco estados legitimos tem de passar,
      entre eles o que mais se parece com defeito: o rejunte que NAO delimita
      ambiente nenhum, que e o estado de 4 dos 5 rejuntes do banco.

E A MUTACAO MAIS IMPORTANTE DE TODAS E A t01, que e o defeito exato que este
bloco consertou: um `return` trocado, de `ambiente_do_produto` para
`ambiente_critico`. Ela nao muda uma lista, nao muda um numero, nao muda a
matriz — muda a frase que o leitor recebe nas duas telas.

Uso:  python3 ferramentas/mutacoes-ambiente-do-produto-do-rejunte.py
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
PRESTACAO = os.path.join(AQUI, "teste-prestacao-rejunte.php")
SNIPPET_F2 = os.path.join(ILHA, "snippets", "clubedomosaico-f2.php")
SNIPPET_F1 = os.path.join(ILHA, "snippets", "clubedomosaico-f1.php")
RENDER = os.path.join(AQUI, "render-para-teste.php")

ARQUIVOS = {
    "esquema":  os.path.join(ILHA, "dados", "esquema-banco.json"),
    "rejuntes": os.path.join(ILHA, "dados", "materiais-rejuntes.json"),
}

AC = "quartzolit-rejunte-acrilico"
EP = "quartzolit-rejunte-epoxi"
BLOCO = "regras_do_balde_do_ambiente_do_produto_do_rejunte"
BALDE = "eliminados_por_ambiente_do_produto"
BALDE_2 = "eliminados_por_ambiente_critico"
L_AC = "áreas internas e externas"

# OS ESTADOS SERVIDOS QUE ESTA BATERIA LE. E_CAI e E_PASSA trocam so o LUGAR, e
# E_FOLGA troca so a FOLGA: as tres juntas separam "a regra morde" de "a regra
# morde sempre" de "a regra 1 roda antes dela".
E_CAI = "base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua&junta=1"
E_PASSA = "base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=2"
E_FOLGA = "base=ceramica_esmaltada_porcelana&onde=externo_exposto&junta=5"
# e o estado com as DUAS causas, onde a troca de frase se esconde atras da certa
E_AMBAS = "base=ceramica_esmaltada_porcelana&onde=externo_exposto&junta=2"

E_CAI_F1 = "rejunte=acrilico&onde=contato_permanente_agua&junta=1"
E_FOLGA_F1 = "rejunte=acrilico&onde=externo_exposto&junta=5"

FRASE_NOVA = "fechou o produto inteiro em outros lugares"
FRASE_DA_REGRA_2 = "Fora porque o fabricante não declara este lugar"
FRASE_NOVA_F1 = "ele declarou onde o produto pode ir"
FRASE_DA_REGRA_2_F1 = "o que ele não declara é peça"


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


def ancora(esq, junta, ambiente):
    for a in esq[BLOCO]["ancoras_ponta_a_ponta"]:
        if a["junta_mm"] == junta and a["ambiente"] == ambiente:
            return a
    raise SystemExit("mutacao aponta para ancora inexistente: %s mm x %s" % (junta, ambiente))


def celula(esq, junta, ambiente):
    for c in esq["matriz_esperada_do_rejunte"]["celulas"]:
        if c["junta_mm"] == junta and c["ambiente"] == ambiente:
            return c
    raise SystemExit("mutacao aponta para celula inexistente: %s mm x %s" % (junta, ambiente))


def perfil_esperado(esq, ident):
    for p in esq["perfis_esperados_do_rejunte"]["perfis"]:
        if p["id"] == ident:
            return p
    raise SystemExit("mutacao aponta para perfil inexistente: %s" % ident)


# ------------------------------------------------- mutacoes de FORMA (validador)

def m01(e):
    """O BLOCO DE REGRAS DESAPARECE e o rejunte que delimita fica. E a direcao
    perigosa escrita como mutacao: perder o bloco nao muda elegibilidade nenhuma —
    muda so quem escreveu PARA ONDE o produto vai e O QUE as duas telas dizem.
    A trava dele mora DENTRO do `if rejuntes`, de proposito: a m01 da bateria da
    cola achou, um dia antes, que a trava irma tinha ficado orfa num `if` sem
    ninguem do outro lado por estar escrita onde `materiais` ainda nao existe."""
    del e[BLOCO]


def m02(e):
    """A REGRA 3 DO REJUNTE VOLTA A SER PROSA SOLTA. Era assim que ela vivia ate
    07/10/2026: uma frase de uma linha dizendo "igual a regra 3 da cola", sem nomear
    balde nenhum. Forma sem a regra e campo que ninguem le."""
    e["regras_de_elegibilidade_do_rejunte"]["3_ambiente_declarado_DELIMITA"] = \
        e["regras_de_elegibilidade_do_rejunte"]["3_ambiente_declarado_DELIMITA"]["regra"]


def m03(e):
    """A REGRA 3 NOMEIA O BALDE DA REGRA 2: ela passa a dizer que manda o produto
    para `eliminados_por_ambiente_critico`, que e o balde de onde ele saiu. Regra que
    descreve outro balde aprova o balde errado — e este e o balde exato do defeito."""
    e["regras_de_elegibilidade_do_rejunte"]["3_ambiente_declarado_DELIMITA"]["o_balde"] = BALDE_2


def m04(e):
    """A REGRA 3 PERDE A LINHA QUE A SEPARA DA REGRA 2. Aqui os dois baldes falam os
    dois de AMBIENTE — mais vizinhos que na cola, onde o da regra 2 se chama
    `eliminados_por_silencio`. Sem a frase que diz por que sao dois, a proxima
    execucao os junta, que e a mistura de causas que a secao 7 do contrato proibe."""
    del e["regras_de_elegibilidade_do_rejunte"]["3_ambiente_declarado_DELIMITA"][
        "e_ela_NAO_SE_JUNTA_a_regra_2"]


def m05(e):
    """A REGRA 2 PERDE O NOME DO BALDE DELA. Com dois baldes de ambiente, a regra que
    nao nomeia o seu deixa a proxima leitura adivinhar qual e qual — e o nome velho,
    `eliminados_por_ambiente`, descrevia os dois."""
    del e["regras_de_elegibilidade_do_rejunte"][
        "2_ambiente_critico_exige_declaracao_EXPLICITA"]["o_balde"]


def m06(e):
    """O BLOCO PERDE A `regra_da_direcao`. Lista sem direcao escrita e lista que a
    proxima execucao preenche pelo lado errado — e aqui a direcao e contraintuitiva:
    perder a regra 3 ALARGA o acrilico para os cinco ambientes."""
    del e[BLOCO]["regra_da_direcao"]


def m07(e):
    """O BLOCO PERDE `sao_DUAS_telas_e_nao_uma`. E a linha propria desta regra: a
    celula do rejunte e lida pela F2 E pela F1, e quem consertar so uma das duas
    deixa a outra mentindo. A bateria da cola nao tinha esta trava porque la a celula
    tem uma tela so."""
    del e[BLOCO]["o_que_as_TELAS_tem_de_dizer"]["sao_DUAS_telas_e_nao_uma"]


def m08(e):
    """O BLOCO PERDE `secao_propria_na_F1`. Mesma familia da m07 e um grau mais
    concreto: sem esta linha, o bloco escreve o que a F2 tem de dizer e cala sobre a
    F1 — que e exatamente a metade do defeito que ninguem tinha visto."""
    del e[BLOCO]["o_que_as_TELAS_tem_de_dizer"]["secao_propria_na_F1"]


def m09(e):
    """A TABELA ESCONDE O UNICO PRODUTO QUE DELIMITA. Tabela que nao lista o
    delimitador existente e tabela que aprova o produto novo entrando mudo — e aqui
    ela fica VAZIA, que e o caso mais facil de ler como "nao se aplica"."""
    e[BLOCO]["produtos_que_delimitam_ambiente_hoje"] = []


def m10(e):
    """A TABELA CITA UMA FRASE QUE O REGISTRO NAO TEM. E a forma mais limpa de a
    regua medir ficcao: as duas telas citam `ambientes_declarados` e a tabela diria
    que ele escreveu uma coisa que ele nao escreveu."""
    linha(e, AC)["literais"] = ["Pode ser usado em qualquer lugar."]


def m11(e):
    """A CONTAGEM MENTE: `entradas_no_balde` do acrilico passa de 8 para 9."""
    linha(e, AC)["entradas_no_balde"] = 9


def m12(e):
    """O TOTAL DE ESTADOS MENTE: 8 passa a 7, que e o numero dos estados com as DUAS
    causas. Os dois numeros sao vizinhos nesta regra e trocar um pelo outro e o erro
    que o registro da cola cometeu em 06/10 com entradas e celulas."""
    e[BLOCO]["total_de_estados_tocados_hoje"] = 7


def m13(e):
    """A ANCORA SEM A OUTRA CAUSA SAI. E a ancora propria desta regra: em 7 dos 8
    estados a regra 2 tambem morde, e so em `1 mm x contato_permanente_agua` o balde
    dela esta vazio. Sem essa ancora, a tabela mede a regra 3 apenas onde a frase
    errada tem onde se esconder atras da certa."""
    e[BLOCO]["ancoras_ponta_a_ponta"] = [
        a for a in e[BLOCO]["ancoras_ponta_a_ponta"]
        if not (a["junta_mm"] == 1 and a["ambiente"] == "contato_permanente_agua")]


def m14(e):
    """A ANCORA ANTI-FUSAO SAI — a de 5 mm, em que o acrilico delimita ambiente, nao
    cobre o lugar, e NAO vai para o balde novo porque a regra 1 o tirou antes pela
    folga. Sem ela, a regua nao distingue a regra 3 da regra 1 rodando antes dela,
    que e a fusao mais provavel desta regra."""
    e[BLOCO]["ancoras_ponta_a_ponta"] = [
        a for a in e[BLOCO]["ancoras_ponta_a_ponta"]
        if not (a["junta_mm"] == 5 and a["ambiente"] == "externo_exposto")]


def m15(e):
    """A ANCORA QUE PASSA SAI — a de 2 mm x interno_molhado, o unico lugar das cinco
    em que o acrilico esta no TOPO. Com as quatro restantes, uma regra 3 que tirasse
    o acrilico de TODO ambiente, inclusive dos tres que o fabricante declara, ficaria
    verde."""
    e[BLOCO]["ancoras_ponta_a_ponta"] = [
        a for a in e[BLOCO]["ancoras_ponta_a_ponta"]
        if not (a["junta_mm"] == 2 and a["ambiente"] == "interno_molhado")]


def m16(e):
    """A MATRIZ VOLTA AO MUNDO DE ANTES: na celula de 2 mm x externo_exposto o
    acrilico volta para o balde da regra 2. E o estado escrito do defeito, e ele e
    uma das DUAS celulas da grade que a regra 3 toca."""
    c = celula(e, 2, "externo_exposto")
    c[BALDE_2] = sorted(c[BALDE_2] + c[BALDE])
    c[BALDE] = []


def m17(e):
    """O MUNDO QUE O BANCO NAO TEM: o epoxi ganha `ambientes_declarados` com um
    literal que O MAPA CONHECE e passa a ser o SEGUNDO delimitador. E a mutacao mais
    valiosa desta bateria, porque hoje `total_de_entradas_hoje` e
    `total_de_estados_tocados_hoje` coincidem em 8 por haver UM produto so — e com
    dois eles se separam. Coincidencia que ninguem mede vira regra na leitura
    seguinte.

    A PRIMEIRA VERSAO DELA USAVA `areas internas` E PASSOU, e foi assim que a m21
    nasceu: o literal nao esta no mapa do rejunte, entao a delimitacao ficava
    ILEGIVEL, a regra 3 nao se aplicava, e o unico efeito era um `aviso`. Mutacao
    inerte de EFEITO parece mutacao que o portao nao pegou, e as duas se separam
    olhando o que a regra fez, nao o que o arquivo mudou."""
    item(e, EP)["declaracoes"]["ambientes_declarados"] = ["piscinas"]


def m21(e):
    """A DELIMITACAO ILEGIVEL, achada pela primeira versao da m17 e virada regra: o
    acrilico troca `areas internas e externas` por uma frase que o mapa nao conhece.
    `ambientes_delimitados` esvazia, a regra 3 PARA DE SE APLICAR, e o produto volta
    a ser elegivel nos cinco ambientes — com uma delimitacao escrita no registro que
    ninguem le. Nos outros dois campos de declaracao, termo ilegivel ENCOLHE o
    produto e aviso basta; neste ele ALARGA."""
    item(e, AC)["declaracoes"]["ambientes_declarados"] = ["para uso em ambientes protegidos"]


def m18(e):
    """O MUNDO DE ANTES DA REGRA 3: a delimitacao do acrilico desaparece do registro.
    O balde novo esvazia, as 8 entradas voltam a ser recomendacao, e a F2 passa a
    indicar rejunte acrilico para peca em contato permanente com agua — que e
    piscina. E a direcao que a `regra_da_direcao` escreve, medida."""
    item(e, AC)["declaracoes"]["ambientes_declarados"] = []


def m19(e):
    """A DELIMITACAO SE ALARGA: o acrilico passa a declarar tambem o sol e a chuva, e
    metade das 8 entradas sai do balde. E o mundo em que a regra morde MENOS — a
    contagem tem de acusar, senao ela aprova qualquer delimitacao."""
    item(e, AC)["declaracoes"]["ambientes_declarados"] = [L_AC, "áreas sujeitas à chuva e ao sol"]


def m20(e):
    """O PERFIL ESCRITO A MAO PERDE O LITERAL. `literais_delimitacao` do acrilico vai
    a vazio enquanto `ambientes_delimitados` fica cheio: contradicao dentro do mesmo
    perfil, e e o unico lugar escrito a mao onde a citacao da tela pode ser conferida
    sem chamar a funcao que a produz."""
    perfil_esperado(e, AC)["literais_delimitacao"] = []


MUTACOES_FORMA = [
    ("m01 o bloco de regras do balde desaparece",        "esquema",  m01),
    ("m02 a regra 3 do rejunte volta a ser prosa solta", "esquema",  m02),
    ("m03 a regra 3 nomeia o balde da regra 2",          "esquema",  m03),
    ("m04 a regra 3 perde a linha que a separa da 2",    "esquema",  m04),
    ("m05 a regra 2 perde o nome do balde dela",         "esquema",  m05),
    ("m06 o bloco perde a regra_da_direcao",             "esquema",  m06),
    ("m07 o bloco cala que sao DUAS telas",              "esquema",  m07),
    ("m08 o bloco cala a secao propria na F1",           "esquema",  m08),
    ("m09 a tabela esconde o unico delimitador",         "esquema",  m09),
    ("m10 a tabela cita frase que o registro nao tem",   "esquema",  m10),
    ("m11 entradas_no_balde mente (8 -> 9)",             "esquema",  m11),
    ("m12 total_de_estados mente (8 -> 7)",              "esquema",  m12),
    ("m13 a ancora SEM a outra causa sai",               "esquema",  m13),
    ("m14 a ancora anti-fusao da folga sai",             "esquema",  m14),
    ("m15 a ancora que PASSA sai",                       "esquema",  m15),
    ("m16 a matriz devolve o acrilico ao balde da 2",    "esquema",  m16),
    ("m17 o epoxi ganha delimitacao: 2o delimitador",    "rejuntes", m17),
    ("m18 o acrilico perde a delimitacao",               "rejuntes", m18),
    ("m19 a delimitacao do acrilico se alarga",          "rejuntes", m19),
    ("m20 o perfil a mao perde o literal da citacao",    "esquema",  m20),
    ("m21 a delimitacao vira literal que o mapa nao le", "rejuntes", m21),
]


# -------------------------------------------------- mutacoes de TELA (snippets)
# Cada uma troca UM pedaco do snippet servido e mede o HTML. A metade de tela e
# maior em peso que a de forma nesta familia de regra, ao contrario das irmas, e a
# razao e a mesma da bateria da cola: regra que troca de BALDE nao muda numero
# nenhum, e frase so se mede no HTML.

def t01(f2):
    """O DEFEITO: a regra 3 volta a devolver `ambiente_critico`. Um `return` so,
    nenhuma lista muda, a matriz nao discorda — e as duas telas voltam a dizer que o
    fabricante nao declara um lugar que ele declara."""
    # O MARCADOR TEM DE SER A REGUA DO REJUNTE, NAO A LINHA. Medido: a primeira versao
    # desta mutacao procurava `return array( 'ambiente_do_produto', 0 );` sozinho, e essa
    # linha existe DUAS vezes no arquivo — a regra 3 da COLA roda antes e a troca caiu
    # nela. A bancada ficou vermelha pelo motivo errado e a frase do rejunte continuou na
    # tela. Marcador que existe nas duas reguas nao mede nenhuma das duas; o que so existe
    # na do rejunte e o bloco inteiro, com a comparacao de `ambientes_delimitados` e o
    # comentario da ordem dentro.
    velho = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}
	/* 2 — ambiente crítico exige declaração explícita. */"""
    novo = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_critico', 0 );
	}
	/* 2 — ambiente crítico exige declaração explícita. */"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


def t02(f2):
    """A ORDEM TROCA: a regra 2 passa a rodar ANTES da 3. Em `externo_exposto` o
    acrilico nao tem o lugar em `ambientes_cobertos`, entao a 2 o morde primeiro e ele
    cai no balde dela — a elegibilidade fica IDENTICA e so a frase muda. E o estado
    E_AMBAS e justamente onde a troca se esconde atras da causa certa dos outros
    quatro produtos."""
    velho = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}
	/* 2 — ambiente crítico exige declaração explícita. */
	$criticos = cdm_f2_criticos_rejunte();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'ambiente_critico', 0 );
	}"""
    novo = """	$criticos = cdm_f2_criticos_rejunte();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'ambiente_critico', 0 );
	}
	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


def t03(f2):
    """A TELA TROCA A CITACAO PELO NOSSO VOCABULARIO. 26.3: a frase e dele, a
    traducao e nossa, e a tela nao pode trocar uma pela outra. O MARCADOR E A CITACAO
    INTEIRA, com a tag dentro, pela cicatriz medida na t03 da bateria da cola e na t04
    da `mutacoes-par.py`: o literal cru `areas internas e externas` aparece TAMBEM no
    cartao do acrilico desta mesma pagina ("O fabricante declara areas internas e
    externas"), entao procura-lo sozinho mede um marcador que existe nos dois lados."""
    # O MARCADOR TEM DE SER A TELA DO REJUNTE, pelo mesmo motivo medido na t01: a linha
    # `$lits = $p['literais_delimitacao'];` existe DUAS vezes no arquivo — a tela da regra
    # 3 da COLA a tem igual, palavra por palavra, e vem antes. A primeira versao desta
    # mutacao caiu nela e a frase do rejunte continuou na tela. O que so existe aqui e o
    # bloco com `cdm_f2_perfil_rejunte` dentro.
    velho = """			$p    = cdm_f2_perfil_rejunte( $m );
			$lits = $p['literais_delimitacao'];"""
    novo = """			$p    = cdm_f2_perfil_rejunte( $m );
			$lits = array_keys( $p['ambientes_delimitados'] );"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


def t04(f2):
    """O RESUMO DA PRESTACAO DE CONTAS DEIXA DE CONTAR O BALDE NOVO. A soma do resumo
    fecha o banco inteiro em toda combinacao de folga x lugar, e e essa soma que o
    portao cobra: sem o grupo novo ela falta 1 nos 8 estados da regra 3, e a prestacao
    de contas acusa o CONSERTO como se fosse o defeito."""
    velho = """		if ( $celula['eliminados_por_ambiente_do_produto'] ) {
			$fora[] = count( $celula['eliminados_por_ambiente_do_produto'] ) . ' porque o fabricante fechou o produto em outros lugares';
		}"""
    assert f2.count(velho) == 1
    return f2.replace(velho, "", 1)


def t05(f2):
    """A FUSAO COM A REGRA 1, e e a fusao mais provavel desta regra: a regra 3 passa a
    rodar ANTES da regra da folga. Em 5 mm o acrilico nao cabe na faixa de 1 a 4 que o
    fabricante publica, e passa a sair do balde da FOLGA para o balde do LUGAR — duas
    causas certas trocadas uma pela outra, que e este bloco virado ao contrario. A
    elegibilidade continua identica nos 60 estados."""
    velho = """	if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	if ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}"""
    novo = """	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'ambiente_do_produto', 0 );
	}
	if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	if ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


def t06(f2):
    """A F1 NAO RECEBE O BALDE NOVO: ela volta a ler so o da regra 2. E a metade do
    defeito que ninguem tinha visto — a celula do rejunte tem DUAS telas, e a F1 dizia
    "o que ele nao declara e peca <lugar>" sobre quem declara. Esta mutacao e o
    conserto chegando a uma tela so, que troca uma tela mentindo por duas telas
    discordando. Ela mexe no OUTRO snippet, e por isso tem o campo `qual`."""
    velho = """	$fora_lugar_produto = array();
	foreach ( $celula['eliminados_por_ambiente_do_produto'] as $id ) {"""
    novo = """	$fora_lugar_produto = array();
	foreach ( array() as $id ) {"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


def t07(f2):
    """A TROCA DE FRASE COM A CLASSE CERTA, e ela e a licao da t05 da bateria da cola:
    o paragrafo continua existindo, com a classe `cdm-f2-rejunte-ambiente-do-produto`
    e o nome do produto dentro, servindo a frase da REGRA 2 palavra por palavra.
    Regua que mede PRESENCA de classe, de nome ou de marcador aprova isto — foi
    exatamente o que aconteceu um dia antes, com a bancada VERDE. E por isso que a
    varredura dos 60 estados em `teste-f2.php` cobra a frase nas duas direcoes e
    proibe a palavra do silencio dentro deste paragrafo."""
    velho = """				. ' fechou o produto inteiro em outros lugares';"""
    novo = """				. ' não declara este lugar';"""
    assert f2.count(velho) == 1
    return f2.replace(velho, novo, 1)


MUTACOES_TELA = [
    {"nome": "t01 O DEFEITO: a regra 3 volta a devolver `ambiente_critico`",
     "qual": "f2", "funcao": t01, "estado": E_CAI, "tela": "cdm_f2",
     "sai": [FRASE_NOVA], "entra": [FRASE_DA_REGRA_2],
     "por_que": "um `return` so, nenhuma lista muda, e as duas telas voltam a mentir"},
    {"nome": "t02 a ordem troca: a regra 2 roda ANTES da 3",
     "qual": "f2", "funcao": t02, "estado": E_AMBAS, "tela": "cdm_f2",
     "sai": [FRASE_NOVA], "entra": [],
     "por_que": "no estado com as duas causas a troca se esconde atras da causa certa"},
    {"nome": "t03 a tela cita o NOSSO vocabulario em vez do literal",
     "qual": "f2", "funcao": t03, "estado": E_CAI, "tela": "cdm_f2",
     "sai": ["ela escreve <em>" + L_AC + "</em>"],
     "entra": ["ela escreve <em>interno_seco"],
     "por_que": "26.3: a frase e dele, a traducao e nossa"},
    {"nome": "t04 o resumo deixa de contar o balde novo",
     "qual": "f2", "funcao": t04, "estado": E_CAI, "tela": "cdm_f2",
     "sai": ["porque o fabricante fechou o produto em outros lugares"], "entra": [],
     "por_que": "a soma da prestacao de contas falta 1 nos 8 estados da regra 3"},
    {"nome": "t05 a FUSAO COM A REGRA 1: a 3 roda antes da folga",
     "qual": "f2", "funcao": t05, "estado": E_FOLGA, "tela": "cdm_f2",
     "sai": ["Fora por causa da folga"], "entra": [FRASE_NOVA],
     "por_que": "em 5 mm ele nem cabe na faixa, e a tela diria que o lugar o exclui"},
    {"nome": "t06 a F1 nao recebe o balde novo",
     "qual": "f1", "funcao": t06, "estado": E_CAI_F1, "tela": "cdm_f1",
     "sai": [FRASE_NOVA_F1], "entra": [],
     "por_que": "sao DUAS telas, e conserto em uma so troca mentira por discordancia"},
    {"nome": "t07 a frase do balde da 3 e trocada pela da 2, com a classe certa",
     "qual": "f2", "funcao": t07, "estado": E_CAI, "tela": "cdm_f2",
     "sai": [FRASE_NOVA], "entra": ["não declara este lugar"],
     "por_que": "presenca de classe e de nome nao mede troca de frase — a licao da t05 da cola"},
]


# ------------------------------------------------------ O FALSO POSITIVO
# Estes TEM de passar. Sem eles a bateria mediria apenas severidade: um validador
# que reprovasse tudo tiraria 20 de 20 nas mutacoes acima e seria inutil.

def fp1(e):
    """O REJUNTE QUE NAO DELIMITA AMBIENTE NENHUM muda de declaracao e continua sem
    delimitar. E o estado de 4 dos 5 rejuntes do banco, e o que mais se parece com
    defeito aos olhos de uma regua apressada: `ambientes_declarados` vazio nao e
    campo faltando, e a regra 3 simplesmente nao se aplica a ele."""
    item(e, "quartzolit-rejunte-ceramicas")["declaracoes"]["resistencias_declaradas"] = \
        item(e, "quartzolit-rejunte-ceramicas")["declaracoes"].get(
            "resistencias_declaradas", []) + ["liberação para tráfego de pedestres em 72 horas"]


def fp2(e):
    """A PROSA DO BLOCO CRESCE. Campo de prosa nao e portao: acrescentar explicacao a
    `por_que_ela_ganhou_balde_em_07_10_2026` nao pode reprovar nada, senao ninguem
    escreve o motivo na proxima vez."""
    r3 = e["regras_de_elegibilidade_do_rejunte"]["3_ambiente_declarado_DELIMITA"]
    r3["por_que_ela_ganhou_balde_em_07_10_2026"] += (
        " || Nota de bancada: a mesma varredura mediu que 7 dos 8 estados carregam as duas "
        "causas no mesmo paragrafo.")


def fp3(e):
    """UMA ANCORA NOVA ENTRA, escrita certa. A tabela tem de aceitar ancora a mais —
    `3 mm x externo_exposto` e um dos 8 estados da regra 3 e nao estava entre as
    cinco. Regua que reprova ancora nova e regua que trava a propria regua."""
    e[BLOCO]["ancoras_ponta_a_ponta"].append({
        "junta_mm": 3,
        "ambiente": "externo_exposto",
        BALDE: [AC],
        BALDE_2: ["quartzolit-rejunte-ceramicas", "quartzolit-rejunte-epoxi",
                  "quartzolit-rejunte-piscinas", "quartzolit-rejunte-porcelanatos-e-ceramicas"],
        "eliminados_por_faixa_de_junta": [],
        "recomendados_topo": [],
        "por_que": "ancora acrescentada pela fp3 da bateria: um sexto estado da regra 3.",
    })


def fp4(e):
    """O PRODUTO QUE DELIMITA APRENDE UMA DECLARACAO QUE CONFIRMA O QUE ELE JA COBRE.
    O acrilico ganha, em `resistencias_declaradas`, uma frase que traduz para
    `interno_molhado` — ambiente que `areas internas e externas` ja alcanca. O
    registro muda, a delimitacao nao, a citacao nao, e nenhum balde se move. E coleta
    legitima, e uma regua apressada poderia reprovar QUALQUER mexida nas declaracoes
    de um produto que delimita ambiente.

    A PRIMEIRA VERSAO DELA SAIU INERTE e fica escrito: ela reescrevia
    `ambientes_declarados` com o MESMO valor que ja estava la, para provar que
    reescrever o literal identico nao reprova. Fixture que nao muda o arquivo nao
    prova nada — e a bateria a chamou de INERTE antes do commit, que e exatamente o
    que o canario de inercia existe para fazer. E a versao obvia do conserto —
    acrescentar um SEGUNDO literal de ambiente ao registro — nao serve como falso
    positivo: ela TEM de reprovar, porque o perfil escrito a mao no esquema carrega
    `literais_delimitacao` e literal novo no registro pede literal novo no perfil."""
    d = item(e, AC)["declaracoes"]
    d["resistencias_declaradas"] = (d.get("resistencias_declaradas") or []) + [
        "liberação para contato com área molhada em 24 horas"]


def fp5(e):
    """UM TERMO DE AMBIENTE NOVO ENTRA NO MAPA e registro nenhum o cita. Veio da fp5
    da bateria da cola, que nasceu como mutacao, PASSOU, e trocou de lado ao ser
    lida: termo que registro nenhum cita nao delimita nada, entao nao muda balde
    nenhum nem contagem nenhuma. Mutacao que passa com razao nao se conserta para
    reprovar — ela muda de lado."""
    e["mapa_de_termos_do_rejunte"]["termos"].append({
        "literal": "ambientes cobertos e descobertos",
        "ambiente": ["interno_seco", "externo_abrigado", "externo_exposto"],
        "de_onde_vem": "acrescentado pela fp5 da bateria; registro nenhum do banco cita.",
    })


FALSOS_POSITIVOS = [
    ("fp1 o rejunte que nao delimita ambiente nenhum",   [("rejuntes", fp1)]),
    ("fp2 a prosa do bloco cresce",                      [("esquema", fp2)]),
    ("fp3 uma ancora NOVA entra, escrita certa",         [("esquema", fp3)]),
    ("fp4 o delimitador aprende declaracao que confirma", [("rejuntes", fp4)]),
    ("fp5 termo de ambiente novo que registro nenhum cita", [("esquema", fp5)]),
]


# ------------------------------------------------------------------ o motor

def roda_validador(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_AMBIENTE_DO_PRODUTO_REJUNTE"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def roda_bancada():
    """AS DUAS BANCADAS, e as duas sao necessarias: a `teste-f2.php` varre os 60
    estados cobrando a frase nas duas direcoes, e a `teste-prestacao-rejunte.php` e a
    QUARTA implementacao das regras do rejunte, independente, e e a unica que mede a
    F1. Mutacao de tela que uma delas engolisse em silencio ficaria verde."""
    for cmd in (["php", TESTE_F2, "."], ["php", PRESTACAO, ".", "--rapido"]):
        if subprocess.run(cmd, capture_output=True, text=True, cwd=ILHA).returncode != 0:
            return True
    return False


def serve(tela, estado):
    r = subprocess.run(["php", RENDER, ".", tela, "hoje", estado],
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


SNIPPETS = {"f2": SNIPPET_F2, "f1": SNIPPET_F1}


# A REDE DE SINAL — `ferramentas/rede-de-sinal.py`, uma copia para as catorze
# baterias que trabalham EM CIMA da arvore do git. O `finally` desta bateria nao
# roda quando ela morre por sinal, e foi assim que a `mutacoes-par.py` deixou um
# snippet mutado no repositorio em 09/10/2026. Nome com hifen nao se importa
# direto; renomear a ferramenta por conveniencia de sintaxe seria romper a
# convencao de nome desta pasta.
def _rede_de_sinal():
    import importlib.util
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "rede-de-sinal.py")
    spec = importlib.util.spec_from_file_location("cdm_rede_de_sinal", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    # A rede de sinal ANTES da primeira mutacao: a janela entre o retrato e o
    # handler e a unica que fica descoberta, e aqui ela tem zero linha.
    _rede_de_sinal().arma(list(ARQUIVOS.values()) + list(SNIPPETS.values()))
    todos = list(ARQUIVOS.values()) + list(SNIPPETS.values())
    bytes_originais = retrato(todos)
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in ARQUIVOS.items()}
    fonte = {k: open(v, encoding="utf-8").read() for k, v in SNIPPETS.items()}
    reprovadas = so_o_portao_novo = telas = fp_ok = 0

    try:
        if roda_validador():
            print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
            return 1
        if roda_validador(sem_portao_novo=True):
            print("FALHA: o banco ja esta reprovado com as travas do balde desligadas")
            return 1
        if roda_bancada():
            print("FALHA: uma das bancadas ja esta vermelha ANTES de qualquer mutacao")
            return 1

        print("Mutacoes do balde do ambiente do produto DO REJUNTE (esquema v16) — "
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
        print("  A TELA E A FRASE — quem pega e o render e as duas bancadas:")
        for mut in MUTACOES_TELA:
            qual = mut["qual"]
            open(SNIPPETS[qual], "w", encoding="utf-8").write(mut["funcao"](fonte[qual]))
            try:
                html = serve(mut["tela"], mut["estado"])
                bancada_verde = not roda_bancada()
            finally:
                restaura(bytes_originais)
            problemas = []
            if bancada_verde:
                problemas.append("as duas bancadas ficaram VERDES")
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

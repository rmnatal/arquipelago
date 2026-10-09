#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO PAR SUBSTRATO x AMBIENTE — 06/10/2026, esquema v14, REGRA 8.

O BURACO QUE ESTA BATERIA FECHA tem uma forma que nenhuma das irmas tinha: nao e
campo errado (a m01 da sobra), nao e campo invisivel (a propria sobra) e nao e
lista que envelhece calada (a regra 7). E um campo cujos DOIS erros possiveis
apontam para lados OPOSTOS, e so um deles e caro:

  - IGNORAR o qualificador publica MAIS do que o fabricante declarou. A
    Cimentcola Externo AC-II passaria a ser recomendacao primaria em
    `alvenaria_tijolo` + `externo_abrigado`, que nesta ilha e muro de mosaico ao
    ar livre — e para esse caso o boletim dela nao declara nada.
  - INTERSECTAR os qualificadores publica MENOS. A mesma argamassa sairia de
    `cimento_concreto` em todo ambiente, apesar de `Paredes de concreto curado ha
    180 dias` declarar aquela base sem qualificador nenhum.

As duas direcoes tem mutacao propria aqui (m07 e m08), e e por isso que esta
bateria existe em vez de duas afirmacoes a mais no `teste-f2.php`: uma regra
cujos erros se cancelam em metade dos casos nao se mede por uma amostra.

AS TRES REGRAS HERDADAS das baterias irmas, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao de forma roda o validador duas vezes, desligando as travas novas
      com CDM_SEM_PORTAO_PAR=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco nao tem. Sao
      tres: m09 da qualificador a uma base que HOJE e declarada larga (o avesso
      do mundo real), m10 cria o segundo produto com frase qualificada, e m11
      qualifica uma frase de PROIBICAO, que e o lado em que a leitura tem de ser
      ampliativa e nao estreita.

  (c) ESTA BATERIA MEDE O FALSO POSITIVO. Quatro estados legitimos tem de passar,
      entre eles os dois que mais se parecem com defeito: um qualificador com
      DOIS ambientes, que exerce a UNIAO entre duas frases qualificadas do mesmo
      produto, e o estado de 51 dos 53 termos do mapa, que e nao ter
      qualificador nenhum. A primeira versao do segundo falso positivo alargava
      o qualificador para os CINCO ambientes e foi REPROVADA com razao: nesse
      mundo a regra 8 nunca morde, e a trava dos dois lados da matriz do par
      existe justamente para impedir uma tabela que nao mede regra nenhuma.
      Fixture que neutraliza a propria regua e chama a reprovacao de falso
      positivo e o jeito mais limpo de desligar um portao sem apagar uma linha.

E A METADE DE TELA MEDE A FRASE, nao a elegibilidade. A regra 8 e a 2 tiram o
MESMO produto do MESMO estado em metade dos casos; o que elas nunca podem ter
igual e a frase que o leitor recebe. A mutacao t03 troca a ordem das duas regras
e a bancada da F2 tem de reprovar — nao porque a lista mudou, mas porque a causa
mudou de nome.

Uso:  python3 ferramentas/mutacoes-par.py
"""

import copy
import json
import os
import shutil
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

AC = "quartzolit-cimentcola-externo-acii"
NE = "tekbond-silicone-neutro"
CAMPO = "ambiente_que_qualifica_a_base"

F_INTERNAS = ("Emboço, alvenaria e contrapiso em áreas internas, curados há pelo menos "
              "14 dias, conforme NBR 13.754.")
F_PAREDES = "Paredes de concreto curado há 180 dias."
F_BLOCOS = ("Alvenarias de blocos vazados de concreto, de blocos silicocalcários e de "
            "blocos de concreto celular em paredes internas, conforme a Norma Técnica "
            "NBR 13.754.")

# os estados servidos que esta bateria le, com o caquinho que a AC-II NAO proibe
E_DENTRO = "base=alvenaria_tijolo&onde=interno_seco&caco=caco_azulejo"
E_FORA = "base=alvenaria_tijolo&onde=externo_abrigado&caco=caco_azulejo"
E_CIMENTO = "base=cimento_concreto&onde=externo_abrigado&caco=caco_azulejo"


def termo(esq, literal):
    for t in esq["mapa_de_termos_do_fabricante"]["termos"]:
        if t["literal"] == literal:
            return t
    raise SystemExit("mutacao aponta para termo inexistente: %s" % literal[:40])


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


# ------------------------------------------------- mutacoes de FORMA (validador)

def m01(e):
    """O QUALIFICADOR APONTA PARA AMBIENTE QUE NAO EXISTE no vocabulario. E o erro
    de digitacao que passaria calado: `interno` em vez de `interno_seco` nao casa
    com nada, e sem a trava a frase viraria declaracao que nunca vale em lugar
    nenhum — produto removido de TODA a base, em silencio."""
    termo(e, F_INTERNAS)[CAMPO] = ["interno"]


def m02(e):
    """QUALIFICADOR SEM `base`. Qualificador nao qualifica nada sozinho: ele
    estreita uma indicacao de substrato, e sem substrato ele e uma delimitacao
    solta que a regua le e descarta."""
    t = termo(e, F_INTERNAS)
    t["base"] = []


def m03(e):
    """`ambiente` E `ambiente_que_qualifica_a_base` NA MESMA LINHA. Os dois tem
    direcoes opostas — um COBRE o produto (satisfaz a regra 4 e soma score) e o
    outro DELIMITA o substrato. Uma linha com os dois e lida de um jeito pela
    regua e de outro por quem a escreveu."""
    termo(e, F_INTERNAS)["ambiente"] = ["interno_seco"]


def m04(e):
    """O QUALIFICADOR PERDE O `por_que`. A traducao de `em areas internas` para o
    vocabulario desta ilha e NOSSA (26.3), e classificacao nossa sem motivo
    escrito e palpite com cara de regra — a mesma trava que o `por_que_cada_uma`
    da regra 7 cobra caquinho por caquinho."""
    t = termo(e, F_INTERNAS)
    for k in [k for k in list(t) if k.startswith("por_que")]:
        del t[k]


def m05(e):
    """A REGRA DESAPARECE DO ESQUEMA e os termos qualificados ficam. E a direcao
    perigosa escrita como mutacao: sem `regras_do_par_substrato_ambiente`, a
    proxima execucao le a frase qualificada como indicacao larga, que e o lado
    que publica MAIS do que o fabricante disse."""
    del e["regras_do_par_substrato_ambiente"]


def m06(e):
    """A MATRIZ DO PAR DESAPARECE. Regra sem regua escrita a mao e duas metades
    que erram juntas — a mesma trava que a regra 6 e a 7 tem."""
    del e["matriz_esperada_do_par_substrato_ambiente"]


def m07(e):
    """A MATRIZ MENTE PARA O LADO QUE PUBLICA MAIS: a linha do par qualificado
    sai da tabela. Uma tabela que nao lista o par existente e uma tabela que
    aprova o produto novo entrando mudo."""
    e["matriz_esperada_do_par_substrato_ambiente"]["pares_qualificados_hoje"] = []


def m08(e):
    """A MATRIZ MENTE PARA O OUTRO LADO: a tabela passa a dizer que o
    qualificador vale nos CINCO ambientes, o que faria a regra 8 nunca morder.
    Escrita e computada tem de divergir."""
    e["matriz_esperada_do_par_substrato_ambiente"]["pares_qualificados_hoje"][0]["vale_so_em"] = [
        "interno_seco", "interno_molhado", "externo_abrigado", "externo_exposto",
        "contato_permanente_agua",
    ]


def m09(e):
    """A TABELA CITA UMA FRASE QUE O REGISTRO NAO TEM. E a forma mais limpa de a
    regua medir ficcao: o par computado seria comparado com um par escrito a
    partir de uma declaracao inexistente."""
    e["matriz_esperada_do_par_substrato_ambiente"]["pares_qualificados_hoje"][0][
        "literais_que_a_declaram"] = ["Alvenaria de qualquer tipo, em qualquer lugar."]


def m10(e):
    """PRODUZ O MUNDO QUE O BANCO NAO TEM: a frase das PAREDES DE CONCRETO,
    hoje larga, ganha qualificador. Com ela qualificada, `cimento_concreto` passa
    a ser declarada SO por frases estreitas e a argamassa sai de tres das cinco
    celulas de cimento. A matriz escrita a mao tem de reprovar — este e o unico
    jeito de medir a regra da UNIAO pelo lado de dentro."""
    termo(e, F_PAREDES)[CAMPO] = ["interno_seco"]
    termo(e, F_PAREDES)["por_que_o_qualificador"] = "mutacao"


def m11(e):
    """PRODUZ: NASCE O SEGUNDO PRODUTO COM FRASE QUALIFICADA. O `concreto` solto
    do Silicone Neutro ganha qualificador, e com ele o neutro sai de
    `cimento_concreto` em quatro ambientes. Qualquer frase da tabela ou da regua
    escrita no singular quebra aqui."""
    termo(e, "concreto")[CAMPO] = ["interno_seco"]
    termo(e, "concreto")["por_que_o_qualificador"] = "mutacao"


def m12(e):
    """PRODUZ: UMA FRASE DE PROIBICAO GANHA QUALIFICADOR. `cimento` esta na lista
    do que o Silicone Acetico Construcao NAO deve tocar. Do lado da proibicao a
    leitura tem de ser AMPLIATIVA — base proibida vale em todo ambiente —, e uma
    implementacao que lesse o qualificador ali ESTREITARIA a proibicao, devolvendo
    o acetico aos recomendados em quatro ambientes de cimento. A matriz escrita a
    mao e quem acusa."""
    termo(e, "cimento")[CAMPO] = ["contato_permanente_agua"]
    termo(e, "cimento")["por_que_o_qualificador"] = "mutacao"


def m13(e):
    """A REGRA 8 SAI DE `regras_de_elegibilidade` e a forma fica. Regra que mora
    em dois lugares do esquema tem de ser cobrada nos dois: forma sem regra e
    campo que ninguem le."""
    del e["regras_de_elegibilidade"]["8_substrato_declarado_SO_EM_CERTO_AMBIENTE"]


def m14(e):
    """O BLOCO DE REGRAS PERDE A `regra_da_direcao`. Lista sem direcao escrita e
    lista que a proxima execucao preenche pelo lado errado — e aqui os dois lados
    erram para lugares opostos."""
    del e["regras_do_par_substrato_ambiente"]["regra_da_direcao"]


def m15(e):
    """A FORMA DESCREVE OUTRO CAMPO. `a_forma.campo` passa a nomear
    `ambiente`, e a regra inteira passa a descrever um campo que a regua nao le —
    aprovacao de forma sobre o campo errado."""
    e["regras_do_par_substrato_ambiente"]["a_forma"]["campo"] = "ambiente"


def m16(c):
    """NO BANCO: a frase das paredes de concreto DESAPARECE de `indicado_para`.
    Com ela fora, `cimento_concreto` passa a ser declarada so por frase
    qualificada e a argamassa sai de tres celulas — e a matriz escrita a mao
    acusa. E tambem o estado real de 10/09 a 06/10, meio passo dele."""
    d = item(c, AC)["declaracoes"]["indicado_para"]
    d.remove(F_PAREDES)


def m17(c):
    """NO BANCO: as TRES frases desaparecem. E o estado exato de 10/09 a
    06/10/2026 — a argamassa eliminada por silencio nas 45 celulas, com a cura de
    180 dias gravada e invisivel. A matriz de hoje tem de reprovar: ela e a
    prova de que o substrato esta gravado."""
    d = item(c, AC)["declaracoes"]["indicado_para"]
    for f in (F_INTERNAS, F_PAREDES, F_BLOCOS):
        d.remove(f)


MUTACOES_FORMA = [
    ("m01 o qualificador aponta para ambiente inexistente",      "esquema", m01),
    ("m02 qualificador sem `base`",                              "esquema", m02),
    ("m03 `ambiente` e o qualificador na MESMA linha",            "esquema", m03),
    ("m04 o qualificador perde o `por_que`",                      "esquema", m04),
    ("m05 a regra desaparece do esquema e os termos ficam",       "esquema", m05),
    ("m06 a matriz do par desaparece",                            "esquema", m06),
    ("m07 a matriz esconde o par que existe",                     "esquema", m07),
    ("m08 a matriz alarga o qualificador para os cinco",          "esquema", m08),
    ("m09 a matriz cita frase que o registro nao tem",            "esquema", m09),
    ("m10 PRODUZ: a frase LARGA ganha qualificador (uniao)",      "esquema", m10),
    ("m11 PRODUZ: nasce o SEGUNDO produto com frase qualificada", "esquema", m11),
    ("m12 PRODUZ: frase de PROIBICAO ganha qualificador",         "esquema", m12),
    ("m13 a regra 8 sai de regras_de_elegibilidade",              "esquema", m13),
    ("m14 o bloco de regras perde a regra_da_direcao",            "esquema", m14),
    ("m15 a forma passa a descrever o campo `ambiente`",          "esquema", m15),
    ("m16 no banco: a frase das paredes de concreto desaparece",  "colas",   m16),
    ("m17 no banco: as TRES frases desaparecem (estado de 05/10)", "colas",  m17),
]


# ------------------------------------------------------- mutacoes de TELA (F2)

def t01(e):
    """O QUALIFICADOR SOME DO MAPA. A frase volta a ser indicacao larga: a
    argamassa passa a ser recomendada em alvenaria ao ar livre, e o paragrafo da
    regra 8 desaparece da pagina. E a direcao que publica MAIS."""
    del termo(e, F_INTERNAS)[CAMPO]
    del termo(e, F_BLOCOS)[CAMPO]


def t02(e):
    """O QUALIFICADOR TROCA DE LUGAR: vale so em `externo_exposto`. O estado que
    hoje PASSA (alvenaria dentro de casa) passa a cair, e o que cai passa. Tela
    que repetisse texto fixo ficaria identica nos dois."""
    termo(e, F_INTERNAS)[CAMPO] = ["externo_exposto"]
    termo(e, F_BLOCOS)[CAMPO] = ["externo_exposto"]


def t03(snippet):
    """A ORDEM TROCA: a regra 8 passa a rodar DEPOIS da 2. Com ela depois, a base
    declarada so em outro lugar cai no balde do SILENCIO, e a pagina passa a
    dizer `o fabricante nao fala desta superficie` sobre uma superficie que ele
    declara, com numero de norma dentro. A elegibilidade nao muda; a frase que o
    leitor recebe muda inteira, e e a frase que esta pagina vende."""
    velho = """	if ( isset( $p['bases_indicadas_so_em'][ $base ] )
		&& ! isset( $p['bases_indicadas_so_em'][ $base ][ $ambiente ] ) ) {
		return array( 'ambiente_do_substrato', 0 );
	}
	/* 2 — base sem declaração não é recomendação. Silêncio não vira "pode". */
	if ( ! isset( $p['bases_indicadas'][ $base ] )
		&& ! isset( $p['bases_indicadas_so_em'][ $base ] ) ) {
		return array( 'silencio', 0 );
	}"""
    novo = """	/* 2 — base sem declaração não é recomendação. Silêncio não vira "pode". */
	if ( ! isset( $p['bases_indicadas'][ $base ] )
		&& ! isset( $p['bases_indicadas_so_em'][ $base ] ) ) {
		return array( 'silencio', 0 );
	}
	if ( isset( $p['bases_indicadas_so_em'][ $base ] )
		&& ! isset( $p['bases_indicadas_so_em'][ $base ][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}"""
    assert velho in snippet, "a ancora da ordem nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t04(snippet):
    """A UNIAO VIRA INTERSECAO. O `if` que livra a base declarada tambem sem
    qualificador e invertido: `cimento_concreto` passa a ser tratada como
    estreita, e a argamassa sai de tres celulas de cimento — publicando MENOS do
    que o fabricante escreveu, que e o outro dos dois erros possiveis."""
    velho = """	foreach ( $ind['par'] as $b => $ambs ) {
		if ( ! isset( $ind['base'][ $b ] ) ) {
			$so_em[ $b ] = $ambs;
		}
	}"""
    novo = """	foreach ( $ind['par'] as $b => $ambs ) {
		$so_em[ $b ] = $ambs;
	}"""
    assert velho in snippet, "a ancora da uniao nao esta no snippet"
    return snippet.replace(velho, novo, 1)


def t05(snippet):
    """A TELA PARA DE CITAR A FRASE DO FABRICANTE e passa a dizer o nosso
    vocabulario. E a 26.3 ao contrario: quem traduziu `em areas internas` para
    `interno_seco` fomos nos, e por a nossa leitura na boca dele e o defeito que
    esta ilha paga com mais frequencia."""
    velho = """			if ( $lits ) {
				$html .= ': <em>' . esc_html( cdm_f2_lista_humana( $lits ) ) . '</em>';
			}"""
    novo = """			if ( $lits ) {
				$html .= ': <em>ambiente interno seco</em>';
			}"""
    assert velho in snippet, "a ancora da citacao nao esta no snippet"
    return snippet.replace(velho, novo, 1)


MUTACOES_TELA = [
    {
        "nome": "t01 o qualificador some do mapa (publica MAIS)",
        "qual": "esquema", "funcao": t01, "estado": E_FORA,
        "sai": ["declara esta superfície, e declara com o lugar dentro da frase"],
        "entra": ["Argamassa Cimentcola Externo AC-II Quartzolit"],
        "por_que": "sem o qualificador a argamassa e recomendada em alvenaria ao ar livre, "
                   "e o paragrafo da causa desaparece",
    },
    {
        "nome": "t02 o qualificador vira `externo_exposto`",
        "qual": "esquema", "funcao": t02, "estado": E_DENTRO,
        "sai": ["Paredes de concreto curado há 180 dias"],
        "entra": ["declara esta superfície, e declara com o lugar dentro da frase"],
        "por_que": "o estado que hoje passa passa a cair; tela com texto fixo ficaria identica",
    },
    {
        "nome": "t03 a ordem troca: a regra 8 roda DEPOIS da 2",
        "qual": "snippet", "funcao": t03, "estado": E_FORA,
        "sai": ["declara esta superfície, e declara com o lugar dentro da frase"],
        "entra": ["O fabricante simplesmente não fala desta superfície"],
        "por_que": "a lista e a mesma e a CAUSA muda de nome — e a causa e o que a pagina vende",
    },
    {
        "nome": "t04 a uniao vira intersecao (publica MENOS)",
        "qual": "snippet", "funcao": t04, "estado": E_CIMENTO,
        # O MARCADOR DE SAIDA NAO PODE SER A CURA, e isto foi medido: a primeira
        # versao desta linha procurava `Paredes de concreto curado ha 180 dias` e
        # a mutacao PASSOU — a frase continuava na tela, agora dentro do
        # paragrafo da REGRA 8, que cita justamente os literais da indicacao.
        # Marcador que existe nos DOIS lados da mutacao nao mede nada. O que so
        # existe no bloco de preparo e a frase do fim do recorte.
        "sai": ["Impermeabilize bases que tenham problemas de umidade"],
        "entra": ["declara esta superfície, e declara com o lugar dentro da frase"],
        "por_que": "a base declarada tambem sem qualificador sai de tres celulas de cimento",
    },
    {
        "nome": "t05 a tela troca a citacao pelo nosso vocabulario",
        "qual": "snippet", "funcao": t05, "estado": E_FORA,
        "sai": ["em paredes internas"],
        "entra": ["ambiente interno seco"],
        "por_que": "26.3: a frase e dele, a traducao e nossa, e a tela nao pode trocar uma pela outra",
    },
]


# ----------------------------------------- a trava do falso positivo (regra c)

def fp1(e):
    """O ESTADO DE 51 DOS 53 TERMOS DO MAPA: termo sem qualificador nenhum. E o
    mais comum e o que mais se parece com campo esquecido."""
    termo(e, "ceramica")["observacao"] = "linha sem qualificador, como 51 das 53"


def fp2(e):
    """QUALIFICADOR COM DOIS AMBIENTES, e ele prova a UNIAO entre duas frases
    qualificadas do mesmo produto: a dos blocos passa a valer tambem em area
    molhada, a de emboco continua so no seco, e `alvenaria_tijolo` fica declarada
    nos DOIS. Tem de passar — o que muda e o mundo, nao a forma.

    A PRIMEIRA VERSAO DESTE FALSO POSITIVO ESTAVA ERRADA, e vale escrito: ela
    alargava o qualificador para os CINCO ambientes, dizendo que isso "e o mesmo
    que nao ter qualificador". E, so que nesse mundo a REGRA 8 nunca morde, e a
    trava dos dois lados da matriz do par reprova com razao — tabela de ancoras
    que nunca morde nao mede regra nenhuma. Nao era falso positivo: era uma
    fixture que neutralizava a propria regua e chamava a reprovacao de defeito.
    Com DOIS ambientes a regra continua mordendo em tres celulas e a forma e
    exercida de verdade."""
    termo(e, F_BLOCOS)[CAMPO] = ["interno_seco", "interno_molhado"]
    # a tabela do par acompanha, porque ela e escrita a mao
    e["matriz_esperada_do_par_substrato_ambiente"]["pares_qualificados_hoje"][0][
        "vale_so_em"] = ["interno_molhado", "interno_seco"]
    # e a ancora que muda de lado: com area molhada declarada, a AC-II passa pela
    # regra 8 ali e quem a tira passa a ser a regra 7, pelo caquinho
    for a in e["matriz_esperada_do_par_substrato_ambiente"]["ancoras_ponta_a_ponta"]:
        if a["base"] == "alvenaria_tijolo" and a["ambiente"] == "interno_molhado":
            a["eliminados_por_ambiente_do_substrato"] = []
    # e a celula de alvenaria em area molhada: a argamassa assume o topo
    for c in e["matriz_esperada_da_F2"]["celulas"]:
        if c["base"] == "alvenaria_tijolo" and c["ambiente"] == "interno_molhado":
            c.pop("eliminados_por_ambiente_do_substrato", None)
            c["recomendados_topo"] = [AC]
            c["elegiveis_abaixo_do_topo"] = [NE]


def fp3(e):
    """UM TERMO NOVO COM QUALIFICADOR, e ele nao e citado por registro nenhum.
    Termo que ninguem usa nao e par, entao a tabela nao o lista e a regua nao
    pode cobra-lo: a lista e dos pares que o BANCO tem, nunca dos que o mapa
    poderia produzir."""
    e["mapa_de_termos_do_fabricante"]["termos"].append({
        "literal": "Pisos de concreto polido em areas de servico internas.",
        "base": ["cimento_concreto"],
        CAMPO: ["interno_seco"],
        "por_que_o_qualificador": "termo que nenhum registro cita ainda",
    })


def fp4(c):
    """A FRASE DAS PAREDES DE CONCRETO MUDA DE POSICAO na lista do registro. A
    ordem de `indicado_para` nao e dado: a regua le o conjunto, nao a sequencia,
    e um portao sensivel a ordem reprovaria diff de arrumacao."""
    d = item(c, AC)["declaracoes"]["indicado_para"]
    d.remove(F_PAREDES)
    d.insert(0, F_PAREDES)


FALSOS_POSITIVOS = [
    ("termo sem qualificador (51 dos 53 do mapa)",        "esquema", fp1),
    ("qualificador com DOIS ambientes (a uniao entre frases)", "esquema", fp2),
    ("termo com qualificador que registro nenhum cita",   "esquema", fp3),
    ("a frase muda de POSICAO em indicado_para",          "colas",   fp4),
]


def roda_validador(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_PAR"] = "1"
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


# A REDE DE SINAL E O RETRATO DE BYTES MORAM EM `ferramentas/rede-de-sinal.py`.
# Estas tres funcoes nasceram AQUI em 09/10/2026, no dia em que esta bateria foi
# morta por sinal e deixou `snippets/clubedomosaico-f2.php` mutado no
# repositorio. No dia seguinte as outras treze baterias que trabalham em cima da
# arvore precisaram da mesma rede, e a escolha foi entre catorze copias de seis
# linhas e um modulo. Copia que divirja e pior que modulo que exija `importlib`:
# a primeira copia que aprendesse algo novo — e a sobra de `<arquivo>.original`
# foi exatamente isso — ensinaria so a si mesma. O historico das duas cicatrizes
# (bytes e nao objeto; sinal e nao `finally`) esta inteiro no modulo, e o portao
# que mata as catorze de proposito e `ferramentas/teste-rede-de-sinal.py`.
def _rede_de_sinal():
    import importlib.util
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "rede-de-sinal.py")
    spec = importlib.util.spec_from_file_location("cdm_rede_de_sinal", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_REDE = _rede_de_sinal()
retrato = _REDE.retrato
restaura = _REDE.restaura
restaura_em_sinal = _REDE.restaura_em_sinal



def main():
    todos = list(ARQUIVOS.values()) + [SNIPPET]
    bytes_originais = retrato(todos)
    restaura_em_sinal(bytes_originais)
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in ARQUIVOS.items()}
    snippet_original = open(SNIPPET, encoding="utf-8").read()

    try:
        if roda_validador():
            print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
            return 1
        if roda_validador(sem_portao_novo=True):
            print("FALHA: o banco ja esta reprovado com as travas do par desligadas")
            return 1
        if roda_bancada():
            print("FALHA: a bancada da F2 ja esta vermelha ANTES de qualquer mutacao")
            return 1

        print("Mutacoes do par substrato x ambiente (esquema v14, REGRA 8) — "
              "%d de forma + %d de tela" % (len(MUTACOES_FORMA), len(MUTACOES_TELA)))
        print("")
        print("  A FORMA E A UNIAO — quem pega e o validar-banco.py:")
        reprovadas = 0
        so_o_portao_novo = 0
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
        telas = 0
        for mut in MUTACOES_TELA:
            if "snippet" == mut["qual"]:
                open(SNIPPET, "w", encoding="utf-8").write(mut["funcao"](snippet_original))
            else:
                mutado = copy.deepcopy(originais[mut["qual"]])
                mut["funcao"](mutado)
                if mutado == originais[mut["qual"]]:
                    print("    INERTE  %s" % mut["nome"])
                    return 1
                with open(ARQUIVOS[mut["qual"]], "w", encoding="utf-8") as fh:
                    json.dump(mutado, fh, ensure_ascii=False, indent=2)
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
        fp_ok = 0
        for nome, qual, funcao in FALSOS_POSITIVOS:
            mutado = copy.deepcopy(originais[qual])
            funcao(mutado)
            with open(ARQUIVOS[qual], "w", encoding="utf-8") as fh:
                json.dump(mutado, fh, ensure_ascii=False, indent=2)
            try:
                pegou = roda_validador()
            finally:
                restaura({ARQUIVOS[qual]: bytes_originais[ARQUIVOS[qual]]})
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F1 de proposito, uma mutacao por vez, e exige que `teste-f1.php`
REPROVE cada uma.

    python3 ferramentas/mutacoes-f1.py

Por que este arquivo existe: teste verde que nunca foi visto reprovar nao mediu
nada (secao 8 do ARQUIPELAGO.md). O teste da F1 ficou verde depois de quatro
correcoes reais, o que e bom sinal e prova nenhuma.

A F1 e uma calculadora, e calculadora erra de um jeito proprio: o numero
continua saindo, bonito e formatado, so que errado. Nenhuma das mutacoes abaixo
quebra a pagina — todas elas deixam a ferramenta respondendo. E por isso que a
regua tem que ser aritmetica e escrita fora do snippet.

A ARMADILHA QUE JA CUSTOU CARO EM TRES ILHAS: mutacao que nao acha o alvo e
verde sem medir nada. Por isso `editar` explode quando nao troca nada. E a
outra, mais fina, que o Clube do Mosaico pagou no bloco 4: mutacao que ACHA o
alvo e mesmo assim nao muda o que o site serve. Contra ela nao ha automacao —
so escolher alvos que mudam numero na tela, e conferir quando uma reprovar por
um motivo que nao e o dela.

Cada uma roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET = os.path.join("snippets", "clubedomosaico-f1.php")
PECAS = os.path.join("dados", "pecas-tipicas.json")


def editar(raiz, arquivo, velho, novo, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    if texto.count(velho) < vezes:
        raise AssertionError(
            "mutacao INERTE: %r aparece %d vez(es) em %s, esperava %d"
            % (velho, texto.count(velho), arquivo, vezes))
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, vezes))


# ------------------------------------------------------- a geometria, errada

def m_cilindro_usa_raio(raiz):
    """A lateral do vaso vira pi x R x H em vez de pi x D x H: a area cai pela
    metade e a pessoa compra METADE da pastilha que precisa. E o erro classico
    de quem escreve a formula de cabeca."""
    editar(raiz, SNIPPET,
           "return ( $d > 0 && $h > 0 ) ? M_PI * $d * $h : null;",
           "return ( $d > 0 && $h > 0 ) ? M_PI * ( $d / 2 ) * $h : null;")


def m_conico_usa_altura_em_vez_da_geratriz(raiz):
    """O tronco de cone passa a usar a ALTURA no lugar da geratriz. Num cachepot
    de 18 para 12 a diferenca e de 2% — e num vaso bojudo passa de 10%, sempre
    para menos. E a mutacao que mais parece certa lendo o codigo."""
    editar(raiz, SNIPPET,
           "$geratriz = sqrt( pow( ( $d - $d2 ) / 2, 2 ) + pow( $h, 2 ) );",
           "$geratriz = $h;")


def m_esfera_vira_meia_esfera(raiz):
    """pi x D^2 vira pi x D^2 / 2. A esfera de 20 cm cai de 960 para 480
    pastilhas, e continua parecendo um numero perfeitamente razoavel."""
    editar(raiz, SNIPPET,
           "case 'esfera':\n\t\t\treturn ( $d > 0 ) ? M_PI * pow( $d, 2 ) : null;",
           "case 'esfera':\n\t\t\treturn ( $d > 0 ) ? M_PI * pow( $d, 2 ) / 2 : null;")


def m_moldura_esquece_o_vao(raiz):
    """A moldura passa a contar o vao como area a revestir: 900 cm2 viram 2.400.
    Quem revestir um espelho compra duas vezes e meia o que precisa."""
    editar(raiz, SNIPPET,
           "return ( $l * $a ) - ( $vl * $va );",
           "return ( $l * $a );")


def m_vao_maior_que_a_moldura_passa(raiz):
    """A guarda cai e a area fica NEGATIVA. O numero de pastilhas vira zero ou
    negativo e a pagina responde isso com cara de resposta."""
    editar(raiz, SNIPPET,
           "\t\t\tif ( $vl >= $l || $va >= $a ) {\n\t\t\t\treturn null;",
           "\t\t\tif ( false ) {\n\t\t\t\treturn null;")


# ------------------------------------------------- a contagem de pastilhas

def m_passo_ignora_a_junta(raiz):
    """O passo passa a ser o lado da pastilha, sem a folga. E o erro que a
    primeira pagina do Google comete: 100 pastilhas de 1 cm cobrindo 100 cm2 em
    vez de 144. Para menos em todo lugar, sempre."""
    editar(raiz, SNIPPET,
           "\t$passo_mm = $lado_mm + $junta_mm;\n\t$area_m2  = $area_cm2 / 10000;",
           "\t$passo_mm = $lado_mm;\n\t$area_m2  = $area_cm2 / 10000;")


def m_arredonda_para_baixo(raiz):
    """ceil vira floor. Erra por uma pastilha quase sempre — e uma pastilha que
    falta no fim da peca custa um lote novo, de cor diferente."""
    editar(raiz, SNIPPET,
           "\treturn (int) ceil( $area_m2 * $por_m2 * ( 1 + ( $sobra_pct / 100 ) ) );",
           "\treturn (int) floor( $area_m2 * $por_m2 * ( 1 + ( $sobra_pct / 100 ) ) );")


def m_sobra_nao_entra(raiz):
    """A sobra some da conta em silencio: o seletor continua na tela, muda a URL
    e nao muda o numero. E a mutacao que um teste do caso-ancora nao ve."""
    editar(raiz, SNIPPET,
           "* ( 1 + ( $sobra_pct / 100 ) ) );",
           "* 1 );")


def m_sobra_vaza_para_o_rejunte(raiz):
    """A sobra passa a inflar tambem os gramas de rejunte. Parece consistente e
    esta errado: o saco de rejunte nao muda de cor entre lotes, e 10% a mais de
    rejunte e dinheiro jogado fora todo mes."""
    editar(raiz, SNIPPET,
           "\treturn ( $area_cm2 / 10000 ) * $consumo_kg_m2 * 1000;",
           "\treturn ( $area_cm2 / 10000 ) * $consumo_kg_m2 * 1000 * 1.1;")


def m_lado_do_caquinho_irregular_ignorado(raiz):
    """O lado medido pela pessoa deixa de valer e o irregular vira 1 cm fixo."""
    editar(raiz, SNIPPET,
           "\t$lado_mm = ( 'irregular' === $tamanho ) ? $lado_eq * 10 : $tam[ $tamanho ]['lado_mm'];",
           "\t$lado_mm = ( 'irregular' === $tamanho ) ? 10 : $tam[ $tamanho ]['lado_mm'];")


# ------------------------------------------------------------- o rejunte

def m_cr_digitado_no_snippet(raiz):
    """O coeficiente deixa de vir do banco e vira numero digitado — com o valor
    CERTO. A pagina continua servindo 264 g e passa a mentir na camada de prova,
    que diz que o numero foi lido do registro do produto. E a mutacao que so
    morde porque a bancada mede a pagina SEM o banco."""
    editar(raiz, SNIPPET,
           "\t\t$valor = isset( $m['propriedades']['CR']['valor'] ) ? $m['propriedades']['CR']['valor'] : null;",
           "\t\t$valor = 1.75;")


def m_cr_trocado_no_banco(raiz):
    """O 1,75 do banco vira 1,57 — dois digitos trocados de lugar, o erro de
    digitacao mais comum que existe. Todo grama da pagina muda 10%."""
    caminho = os.path.join(raiz, "dados", "materiais-rejuntes.json")
    with open(caminho, encoding="utf-8") as fh:
        banco = json.load(fh)
    trocou = False
    for m in banco["materiais"]:
        cr = m.get("propriedades", {}).get("CR", {})
        if cr.get("valor") == 1.75:
            cr["valor"] = 1.57
            trocou = True
    if not trocou:
        raise AssertionError("mutacao INERTE: nenhum CR 1,75 no banco")
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(banco, fh, ensure_ascii=False, indent=2)


def m_formula_de_consumo_sem_a_espessura(raiz):
    """A espessura sai da formula de consumo. O numero continua saindo, e o
    seletor de espessura vira enfeite: pastilha de 2 e de 10 mm passam a comer o
    mesmo rejunte."""
    editar(raiz, SNIPPET,
           "\treturn ( ( $lado_mm + $lado_mm ) * $espessura_mm * $junta_mm * $cr ) / ( $lado_mm * $lado_mm );",
           "\treturn ( ( $lado_mm + $lado_mm ) * 4 * $junta_mm * $cr ) / ( $lado_mm * $lado_mm );")


def m_epoxi_ganha_o_CR_do_cimenticio(raiz):
    """A correcao do bloco 3c cai: o acrilico e o epoxi passam a receber o
    coeficiente do po. E a mutacao mais tentadora do arquivo, porque ela
    PREENCHE um buraco da pagina — e preenche com uma suposicao."""
    editar(raiz, SNIPPET,
           "\tif ( 'cimenticio' !== $tipo_rejunte ) {",
           "\tif ( false ) {")


def m_dois_CR_diferentes_e_a_pagina_escolhe_um(raiz):
    """O banco passa a ter dois coeficientes diferentes e a pagina escolhe o
    primeiro em silencio, em vez de recusar. E a forma educada de inventar."""
    editar(raiz, SNIPPET,
           "\tif ( 1 !== count( $valores ) ) {",
           "\tif ( 0 === count( $valores ) ) {")
    caminho = os.path.join(raiz, "dados", "materiais-rejuntes.json")
    with open(caminho, encoding="utf-8") as fh:
        banco = json.load(fh)
    for m in banco["materiais"]:
        if m["tipo"] == "cimenticio" and m.get("propriedades", {}).get("CR", {}).get("valor") is None:
            m["propriedades"]["CR"]["valor"] = 2.4
            break
    else:
        raise AssertionError("mutacao INERTE: nenhum cimenticio com CR vazio")
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(banco, fh, ensure_ascii=False, indent=2)


def m_gramas_arredonda_tudo_para_inteiro(raiz):
    """A casa decimal abaixo de 10 g some: o pingente de 3,5 g vira 4 g, 14% de
    erro numa peca pequena — e ninguem olha duas vezes para um numero inteiro."""
    editar(raiz, SNIPPET,
           "\tif ( $g < 10 ) {",
           "\tif ( false ) {")


# ------------------------------------------------ a regua do rejunte e a tela

def m_vitrine_ignora_a_faixa_de_junta(raiz):
    """A F1 para de usar a regua da F2 e mostra TODO rejunte do banco. A folga
    de 11 mm, que nenhum fabricante cobre, passa a devolver cinco produtos."""
    editar(raiz, SNIPPET,
           "\t$celula = cdm_f2_celula_rejunte( $e['junta'], $e['ambiente'] );",
           "\t$celula = array( 'recomendados_topo' => array_keys( cdm_f2_banco()['materiais'] ), 'elegiveis_abaixo_do_topo' => array() );")


def m_vitrine_ignora_o_tipo_escolhido(raiz):
    """O filtro por tipo cai: quem pede epoxi recebe cartao de cimenticio no
    lugar de recomendacao. A conta continua certa; a compra e que sai errada."""
    editar(raiz, SNIPPET,
           "\t\tif ( $e['rejunte'] === ( isset( $por_id[ $id ]['tipo'] ) ? $por_id[ $id ]['tipo'] : '' ) ) {",
           "\t\tif ( true ) {")


def m_tabela_das_doze_some_do_html(raiz):
    """A tabela pre-renderizada deixa de ser servida. A pagina continua inteira
    para quem tem navegador, e passa a mostrar uma tela vazia a um modelo de
    linguagem — o defeito que a secao 5 do contrato existe para impedir."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f1_tabela_pecas_html();",
           "\t$html .= '';")


def m_estado_com_parametro_entra_no_indice(raiz):
    """O noindex do estado com parametro cai: as centenas de combinacoes viram
    paginas indexaveis e o orcamento de rastreamento de um dominio recem-nascido
    se gasta em duplicata (secoes 14.1 e 14.4)."""
    editar(raiz, SNIPPET,
           "\tif ( $e['escolheu'] ) {\n\t\techo '<meta name=\"robots\" content=\"noindex, follow\">' . \"\\n\";",
           "\tif ( false ) {\n\t\techo '<meta name=\"robots\" content=\"noindex, follow\">' . \"\\n\";")


def m_script_volta_para_dentro_do_shortcode(raiz):
    """O <script> volta para dentro do retorno do shortcode. Foi o que derrubou
    cinco calculadoras da Aquametria em 08/09/2026: o filtro de conteudo do
    WordPress converte o E-comercial duplo e mata o script inteiro."""
    editar(raiz, SNIPPET,
           "\t$html .= '</div>';\n\n\treturn $html;\n} );",
           "\t$html .= '</div><script>var a = 1 && 2;</script>';\n\n\treturn $html;\n} );")


def m_pagina_perde_a_mae(raiz):
    """A pagina nasce na raiz, sem mae: a trilha perde o degrau do Guia e a
    arvore da secao 16 deixa de existir para ela."""
    editar(raiz, SNIPPET,
           "\t\t'pai'      => 'materiais',",
           "\t\t'pai'      => '',")


def m_nome_diverge_entre_trilha_e_titulo(raiz):
    """O cartao do Guia passa a chamar a pagina por outro nome. Dois nomes para
    a mesma pagina a uma dobra de distancia — a cicatriz que a Aquametria pagou
    em oito paginas e a Robometria em seis."""
    editar(raiz, SNIPPET,
           "\t\t\t$lista[ $i ]['titulo'] = CDM_F1_TITULO;",
           "\t\t\t$lista[ $i ]['titulo'] = 'Calculadora de pastilhas';")


def m_faq_promete_o_que_a_pagina_nao_diz(raiz):
    """Uma pergunta entra so no schema. FAQPage que promete o que a pagina nao
    mostra e a definicao de schema-spam, e custa a pagina inteira."""
    editar(raiz, SNIPPET,
           "\tforeach ( cdm_f1_perguntas() as $p ) {\n\t\t$html .= '<dt>'",
           "\tforeach ( array_slice( cdm_f1_perguntas(), 0, 2 ) as $p ) {\n\t\t$html .= '<dt>'")


def m_coluna_de_cola_some_em_vez_de_declarar(raiz):
    """A linha de gramas de cola some da tela. Sumir faz parecer que a cola nao
    entra na conta; o que acontece e que a ilha nao tem o numero (secao 10)."""
    editar(raiz, SNIPPET,
           "\t$html .= '<li><span class=\"cdm-f1-rotulo\">Gramas de cola</span>",
           "\t$html .= '' . ( false ? '<li><span class=\"cdm-f1-rotulo\">Gramas de cola</span>")


def m_tabela_a_mao_diverge_do_calculo(raiz):
    """Uma linha da tabela escrita A MAO muda: 720 pastilhas viram 700. O
    snippet continua certo, e e a regua que passa a estar errada. Prova que a
    comparacao das tres escritas mede nos DOIS sentidos."""
    caminho = os.path.join(raiz, PECAS)
    with open(caminho, encoding="utf-8") as fh:
        dados = json.load(fh)
    dados["pecas"][0]["esperado"]["pastilhas"] = 700
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(dados, fh, ensure_ascii=False, indent=2)


def m_bloco_de_compra_depois_da_procedencia(raiz):
    """O cartao passa a servir a fonte antes do link de loja — a cicatriz da
    Robometria de 10/09/2026, em que o unico clique de compra levava para onde a
    ilha nao ganha nada. Mora no cartao da F2, que e o que esta pagina usa.

    ALVO ATUALIZADO EM 13/09/2026: a f2 1.2.0 tirou a abertura do `<span
    class="cdm-f2-compra">` de dentro do cartao e a pos em `cdm_f2_compra_html()`.
    O alvo antigo deixou de existir, a mutacao virou INERTE e foi contada como
    PASSOU — inerte nao mede nada. O alvo novo e a CHAMADA da funcao, que e o que
    governa a ordem no cartao de hoje."""
    editar(raiz, os.path.join("snippets", "clubedomosaico-f2.php"),
           "\t$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );",
           "\tif ( $fonte && ! empty( $fonte['url'] ) ) {\n"
           "\t\t$html .= '<span class=\"cdm-f2-fonte\">fonte</span>';\n"
           "\t}\n"
           "\t$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );")



# ---------------------------------------------- a vitrine de pastilha (1.2.0)
#
# As travas desta vitrine sao TRES e a ordem delas e o que faz cada frase de
# recusa poder ser verdadeira. Com o banco de hoje — um item por balde — quase
# toda troca de ordem produz a MESMA tela, e e por isso que tres das mutacoes
# abaixo so reprovam num mundo produzido pelo `render-para-teste.php`.

def m_pastilha_ignora_o_lado(raiz):
    """A vitrine para de filtrar pelo lado: os treze itens viram elegiveis em
    qualquer estado. E o defeito mais caro dos possiveis aqui — a pessoa pede
    caquinho de 1 cm e a pagina recomenda placa de 3 cm com a conta de 1 cm."""
    editar(raiz, SNIPPET,
           "		if ( null === $lado || abs( $lado - (float) $lado_mm ) > 0.001 ) {\n			$saida['outro_lado'][] = $m;\n			continue;\n		}",
           "		if ( null === $lado ) {\n			$saida['outro_lado'][] = $m;\n			continue;\n		}")


def m_pastilha_ignora_o_formato(raiz):
    """O strip retangular de 1,2 cm passa a ser recomendado como se fosse
    quadradinho: a conta de area da pagina e de peca quadrada, e a contagem sai
    errada para quem comprar aquilo."""
    editar(raiz, SNIPPET,
           "		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) ) {\n			$saida['outro_formato'][] = $m;\n			continue;\n		}",
           "")


def m_pastilha_ignora_a_fonte(raiz):
    """A escada de fontes deixa de valer para a pastilha: o item sustentado por
    DISTRIBUIDOR entra em recomendacao primaria, que e exatamente o que o
    nivel <= 3 do esquema existe para impedir."""
    editar(raiz, SNIPPET,
           "		if ( cdm_f1_nivel_da_pastilha( $m ) > $teto ) {\n			$saida['fonte_fraca'][] = $m;\n			continue;\n		}",
           "")


def m_pastilha_inverte_formato_e_fonte(raiz):
    """A ordem das duas ultimas travas troca: a fonte passa a decidir antes do
    formato. COM O BANCO DE HOJE A TELA NAO MUDA — nenhum item cai pelas duas —,
    e quem pega isto e o mundo `strip_fraco=1`, que rebaixa a fonte do strip
    para nivel 5 e exige que a pagina culpe o FORMATO."""
    editar(raiz, SNIPPET,
           "		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) ) {\n			$saida['outro_formato'][] = $m;\n			continue;\n		}\n		if ( cdm_f1_nivel_da_pastilha( $m ) > $teto ) {\n			$saida['fonte_fraca'][] = $m;\n			continue;\n		}",
           "		if ( cdm_f1_nivel_da_pastilha( $m ) > $teto ) {\n			$saida['fonte_fraca'][] = $m;\n			continue;\n		}\n		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) ) {\n			$saida['outro_formato'][] = $m;\n			continue;\n		}")


def m_pastilha_reimplementa_a_escada(raiz):
    """O cartao de pastilha para de chamar `cdm_f2_compra_html()` e escreve a
    etiqueta de "em breve" na mao. HOJE A TELA E IDENTICA, byte a byte: os treze
    itens estao sem ficha e sem piso, entao a escada cai no terceiro degrau de
    qualquer jeito. Quem pega isto e o mundo `com_piso=1`, e esta mutacao e a
    razao de aquele mundo existir — a copia da escada so mentiria no dia em que
    o Raphael colasse os links, com um portao verde ao lado."""
    editar(raiz, SNIPPET,
           "	$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );\n\n	if ( $fonte && ! empty( $fonte['url'] ) ) {",
           "	$html .= '<span class=\"cdm-f2-compra\"><span class=\"cdm-f2-sem-loja\">Link de loja em breve</span></span>';\n\n	if ( $fonte && ! empty( $fonte['url'] ) ) {")


def m_pastilha_sem_bloco_de_compra(raiz):
    """O cartao de pastilha perde o bloco de compra: sem link, o lugar SOME em
    vez de ficar reservado. E o "em breve com outro nome" que a secao 7 proibe."""
    editar(raiz, SNIPPET,
           "	$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );\n\n	if ( $fonte && ! empty( $fonte['url'] ) ) {",
           "	if ( $fonte && ! empty( $fonte['url'] ) ) {")


def m_placas_arredonda_para_baixo(raiz):
    """As placas arredondam para BAIXO: a pessoa compra menos placa do que a
    peca pede e descobre no meio do trabalho, com o lote seguinte de outra cor."""
    editar(raiz, SNIPPET,
           "	return (int) ceil( ( $area_cm2 * ( 1 + $sobra_pct / 100 ) ) / ( $a * $b ) );",
           "	return (int) floor( ( $area_cm2 * ( 1 + $sobra_pct / 100 ) ) / ( $a * $b ) );")


def m_placas_esquecem_a_sobra(raiz):
    """A sobra que a pessoa escolheu sai da conta das placas — e ela continua
    dentro da conta das pecas, logo acima, o que faz as duas discordarem em
    silencio na mesma tela."""
    editar(raiz, SNIPPET,
           "	return (int) ceil( ( $area_cm2 * ( 1 + $sobra_pct / 100 ) ) / ( $a * $b ) );",
           "	return (int) ceil( $area_cm2 / ( $a * $b ) );")


def m_contagem_da_vitrine_digitada(raiz):
    """O numero da frase vira literal com o valor CERTO do estado de 2 cm. A tela
    de 2 cm nao muda; a de 2,5 cm passa a anunciar tres pastilhas servindo
    quatro cartoes. E a familia do zero digitado no cartao do Guia, que esta
    ilha ja pagou em 11/09/2026."""
    editar(raiz, SNIPPET,
           "				. cdm_casca_num( $quantas ) . '</strong> pastilhas do nosso banco",
           "				. cdm_casca_num( 3 ) . '</strong> pastilhas do nosso banco")


def m_frase_do_1cm_vira_incondicional(raiz):
    """A frase "1 cm nao aparece em catalogo de fabricante nenhum" sai de dentro
    do `if` da contagem e passa a sair sempre. Ela e VERDADEIRA hoje, e e isso
    que a torna perigosa: no dia em que um 1 cm de fabricante entrar no banco, a
    pagina segue afirmando o contrario do que ela mesma serve no cartao."""
    editar(raiz, SNIPPET,
           "		if ( 10 === (int) $e['lado_mm'] ) {",
           "		if ( true ) {")


def m_tabela_do_banco_some(raiz):
    """A tabela pre-renderizada do banco desaparece do HTML servido: a unica
    pagina indexada desta ferramenta e a de 1 cm, que tem zero elegivel, e sem a
    tabela ela deixa de citar um unico produto do catalogo (secao 5)."""
    editar(raiz, SNIPPET,
           "	$html .= cdm_f1_tabela_pastilhas_html();",
           "")


def m_tabela_do_banco_pula_os_nao_quadrados(raiz):
    """A tabela passa a listar so as pastilhas quadradas. O item que ficou de
    fora e justamente o que a vitrine tambem recusa — entao ele deixa de ser
    nomeado em QUALQUER superficie da pagina, que e o defeito da prestacao de
    contas da secao 7 na sua forma original."""
    editar(raiz, SNIPPET,
           "	foreach ( $itens as $m ) {\n		$g     = isset( $m['geometria'] ) ? $m['geometria'] : array();\n		$props = isset( $m['propriedades'] ) ? $m['propriedades'] : array();",
           "	foreach ( $itens as $m ) {\n		$g     = isset( $m['geometria'] ) ? $m['geometria'] : array();\n		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) ) { continue; }\n		$props = isset( $m['propriedades'] ) ? $m['propriedades'] : array();")


def m_coluna_do_seletor_diz_sempre_sim(raiz):
    """A coluna "esta no formulario?" passa a dizer sim para todo item. A
    cobertura da secao 14.3 sai publicada dizendo que a ferramenta cobre cinco
    lados que ela nao cobre — e e essa coluna que manda a pessoa para o caquinho
    irregular."""
    editar(raiz, SNIPPET,
           "		$html .= '<td>' . ( $tem ? 'sim' : '<span class=\"cdm-f1-vazio\">não</span>' ) . '</td>';",
           "		$html .= '<td>sim</td>';")


MUTACOES = [
    ("cilindro usa o raio no lugar do diametro", m_cilindro_usa_raio),
    ("cone usa a altura no lugar da geratriz", m_conico_usa_altura_em_vez_da_geratriz),
    ("esfera vira meia esfera", m_esfera_vira_meia_esfera),
    ("moldura esquece o vao", m_moldura_esquece_o_vao),
    ("vao maior que a moldura passa e a area fica negativa", m_vao_maior_que_a_moldura_passa),
    ("o passo ignora a folga entre as pastilhas", m_passo_ignora_a_junta),
    ("a contagem arredonda para baixo", m_arredonda_para_baixo),
    ("a sobra deixa de entrar na conta", m_sobra_nao_entra),
    ("a sobra vaza para o rejunte", m_sobra_vaza_para_o_rejunte),
    ("o lado do caquinho irregular e ignorado", m_lado_do_caquinho_irregular_ignorado),
    ("o CR passa a ser digitado no snippet, com o valor certo", m_cr_digitado_no_snippet),
    ("o CR do banco vira 1,57 (dois digitos trocados)", m_cr_trocado_no_banco),
    ("a espessura sai da formula de consumo", m_formula_de_consumo_sem_a_espessura),
    ("acrilico e epoxi ganham o coeficiente do po", m_epoxi_ganha_o_CR_do_cimenticio),
    ("dois CR diferentes e a pagina escolhe um", m_dois_CR_diferentes_e_a_pagina_escolhe_um),
    ("os gramas perdem a casa decimal abaixo de 10 g", m_gramas_arredonda_tudo_para_inteiro),
    ("a vitrine ignora a faixa de junta da regua da F2", m_vitrine_ignora_a_faixa_de_junta),
    ("a vitrine ignora o tipo de rejunte escolhido", m_vitrine_ignora_o_tipo_escolhido),
    ("a tabela das doze some do HTML servido", m_tabela_das_doze_some_do_html),
    ("estado com parametro entra no indice", m_estado_com_parametro_entra_no_indice),
    ("<script> volta para dentro do shortcode", m_script_volta_para_dentro_do_shortcode),
    ("a pagina perde a mae e nasce na raiz", m_pagina_perde_a_mae),
    ("o nome diverge entre o cartao e o titulo", m_nome_diverge_entre_trilha_e_titulo),
    ("o FAQPage promete pergunta que a pagina nao mostra", m_faq_promete_o_que_a_pagina_nao_diz),
    ("a coluna de cola some em vez de declarar o vazio", m_coluna_de_cola_some_em_vez_de_declarar),
    ("a tabela escrita a mao diverge do calculo", m_tabela_a_mao_diverge_do_calculo),
    ("o bloco de compra vai para depois da procedencia", m_bloco_de_compra_depois_da_procedencia),
    ("a vitrine de pastilha ignora o lado pedido", m_pastilha_ignora_o_lado),
    ("a vitrine de pastilha ignora o formato (o strip vira quadradinho)", m_pastilha_ignora_o_formato),
    ("a vitrine de pastilha ignora a escada de fontes", m_pastilha_ignora_a_fonte),
    ("a ordem das travas troca: fonte antes de formato", m_pastilha_inverte_formato_e_fonte),
    ("o cartao de pastilha reimplementa a escada em vez de chamar a da F2", m_pastilha_reimplementa_a_escada),
    ("o cartao de pastilha sem link perde o bloco de compra", m_pastilha_sem_bloco_de_compra),
    ("as placas arredondam para baixo", m_placas_arredonda_para_baixo),
    ("as placas esquecem a sobra que a pessoa escolheu", m_placas_esquecem_a_sobra),
    ("a contagem da vitrine vira numero digitado, com o valor certo de 2 cm", m_contagem_da_vitrine_digitada),
    ("a frase do 1 cm passa a sair sempre, em vez de seguir a contagem", m_frase_do_1cm_vira_incondicional),
    ("a tabela do banco de pastilhas some do HTML servido", m_tabela_do_banco_some),
    ("a tabela do banco pula os itens nao quadrados", m_tabela_do_banco_pula_os_nao_quadrados),
    ("a coluna 'esta no formulario?' diz sempre sim", m_coluna_do_seletor_diz_sempre_sim),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-f1.php"), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A F1 de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("F1 intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-f1-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [" + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if "FALHA" in linha:
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-58s | %s" % (nome, primeira[:78]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

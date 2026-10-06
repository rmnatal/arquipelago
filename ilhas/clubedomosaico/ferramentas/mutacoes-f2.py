#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F2 de proposito, uma mutacao por vez, e exige que `teste-f2.php`
REPROVE cada uma.

    python3 ferramentas/mutacoes-f2.py

Por que este arquivo existe: teste verde que nunca foi visto reprovar nao mediu
nada (secao 8 do ARQUIPELAGO.md). O teste da F2 ficou verde na primeira rodada,
o que e bom sinal e prova nenhuma. Cada mutacao abaixo e uma forma PLAUSIVEL de
esta ferramenta ficar errada em silencio — a maioria e um caractere trocado, do
tipo que passa numa revisao de codigo.

A ARMADILHA QUE JA CUSTOU CARO EM TRES ILHAS: mutacao que nao acha o alvo no
arquivo e verde sem medir nada. Por isso toda mutacao que edita texto CONFERE
que trocou alguma coisa e explode se nao trocou. Mutacao que nao morde nao e
mutacao.

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
SNIPPET = os.path.join("snippets", "clubedomosaico-f2.php")


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


def carregar(raiz, nome):
    with open(os.path.join(raiz, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


def gravar(raiz, nome, dado):
    with open(os.path.join(raiz, "dados", nome), "w", encoding="utf-8") as fh:
        json.dump(dado, fh, ensure_ascii=False, indent=2)


# --------------------------------------------------------------- as mutacoes

def m_proibicao_deixa_de_vencer(raiz):
    """A regra 1 cai: o produto proibido pelo fabricante volta a ser candidato.

    E a mutacao mais cara do arquivo. Ela poe o silicone acetico de volta em
    espelho e em cimento — que e exatamente o que a SERP faz e a razao de esta
    pagina existir."""
    editar(raiz, SNIPPET,
           "\tif ( isset( $p['bases_proibidas'][ $base ] ) || isset( $p['ambientes_proibidos'][ $ambiente ] ) ) {\n\t\treturn array( 'proibido', 0 );",
           "\tif ( false ) {\n\t\treturn array( 'proibido', 0 );")


def m_silencio_vira_pode(raiz):
    """A regra 2 cai: base sem declaracao passa a valer como indicada.

    O defeito de blog, escrito em PHP: silencio do fabricante virando 'pode'."""
    editar(raiz, SNIPPET,
           "\tif ( ! isset( $p['bases_indicadas'][ $base ] ) ) {\n\t\treturn array( 'silencio', 0 );",
           "\tif ( false ) {\n\t\treturn array( 'silencio', 0 );")


def m_ambiente_critico_aceita_silencio(raiz):
    """A regra 4 cai so no ambiente critico — sol, chuva e imersao passam a
    aceitar silencio. E a mutacao sutil: a grande maioria das celulas continua
    certa, e so as de sol, chuva e agua parada mudam (eram 2 das 18 ate
    12/09/2026; com a matriz em 45 sao 18 das 45, porque dois dos cinco
    ambientes do vocabulario sao criticos)."""
    editar(raiz, SNIPPET,
           "\tif ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {\n\t\treturn array( 'silencio', 0 );",
           "\tif ( false && isset( $criticos[ $ambiente ] ) ) {\n\t\treturn array( 'silencio', 0 );")


def m_nivel_de_fonte_deixa_de_limitar(raiz):
    """A regra 5 cai: o Loctite Durepoxi, sustentado por material de imprensa,
    sobe de 'mencao com ressalva' para recomendacao."""
    editar(raiz, SNIPPET,
           "\tif ( $p['nivel'] > cdm_f2_nivel_maximo() ) {\n\t\treturn array( 'ressalva', $score );\n\t}\n\n\treturn array( 'recomendado', $score );",
           "\treturn array( 'recomendado', $score );")


def m_junta_abre_um_milimetro(raiz):
    """`<` vira `<=` na ponta de baixo da faixa de junta: um rejunte passa a
    servir uma folga que o fabricante nao declara. Um caractere."""
    editar(raiz, SNIPPET,
           "\tif ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {",
           "\tif ( $junta_mm < $p['junta_min'] - 1 || $junta_mm > $p['junta_max'] ) {")


def m_faixa_pela_metade_vira_sem_limite(raiz):
    """A leitura errada mais tentadora do banco: faixa com uma ponta null tratada
    como 'sem limite'. Poe no ar o unico produto declarado para pastilha de vidro
    submersa — que e justamente o que a ilha NAO pode recomendar."""
    # A PRIMEIRA VERSAO DESTA MUTACAO FOI INERTE, e o motivo vale mais que ela:
    # ela trocava o `||` por `&&` e completava as pontas que faltavam. So que o
    # unico produto do banco sem faixa tem as DUAS pontas null, entao a guarda
    # trocada continuava pegando nele e nada mudava na tela. Mutacao que acha o
    # alvo e mesmo assim nao muda o que o site serve e verde sem medir nada — a
    # mesma familia do alvo que nao existe, e mais dificil de ver. Esta versao
    # desliga a guarda e completa as duas pontas, que e o erro plausivel de
    # verdade: ler faixa DESCONHECIDA como faixa ABERTA.
    editar(raiz, SNIPPET,
           "\tif ( null === $p['junta_min'] || null === $p['junta_max'] ) {\n\t\treturn array( 'fora_da_junta', 0 );\n\t}",
           "\tif ( null === $p['junta_min'] ) { $p['junta_min'] = 0; }\n\tif ( null === $p['junta_max'] ) { $p['junta_max'] = 99; }")


def m_categoria_some_da_pergunta(raiz):
    """A matriz da cola volta a varrer o banco inteiro, sem olhar categoria.

    E o defeito que o bloco 3c encontrou no validador: os cinco rejuntes voltam
    a aparecer como 'eliminados por silencio' numa decisao de COLAGEM, frase que
    nem sentido faz."""
    editar(raiz, SNIPPET,
           "\t\tif ( 'cola' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {\n\t\t\tcontinue;\n\t\t}",
           "\t\tif ( false ) {\n\t\t\tcontinue;\n\t\t}")


def m_secao_do_que_nao_usar_some(raiz):
    """A secao que da razao de ser a pagina desaparece. A recomendacao continua
    certa — e e por isso que a mutacao vale: um teste que so olhasse o topo da
    lista aprovaria."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_fora_html( $e['base'], $e['ambiente'], $e['tessela'] );",
           "\t$html .= '';")


def m_tabela_pre_renderizada_some(raiz):
    """As tabelas saem do HTML servido e a ferramenta vira formulario vazio para
    um modelo de linguagem (secao 5 do contrato). A tela continua funcionando
    para quem tem navegador — que e o que faz o defeito ser invisivel."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_tabela_cola_html();\n\t$html .= cdm_f2_tabela_rejunte_html();",
           "\t$html .= '';")


def m_compra_depois_da_procedencia(raiz):
    """A cicatriz da Robometria de 10/09/2026, refeita: a procedencia vira a
    primeira porta do cartao e o link de compra desce para baixo dela.

    O ALVO MUDOU EM 13/09/2026, e a razao e a mesma que matou a mutacao 24 desta
    ilha em 12/09: o alvo desta mutacao era a linha que ABRIA o `<span
    class="cdm-f2-compra">` dentro do cartao, e a f2 1.2.0 mudou o vizinho — a
    abertura desceu para `cdm_f2_compra_html()` e o cartao passou a chamar a
    funcao. A mutacao virou INERTE, achou zero ocorrencia e foi contada como
    PASSOU, que e o certo: mutacao que nao morde nao mede nada. O alvo novo e a
    CHAMADA, que e o que o cartao tem hoje e e o que de fato governa a ordem."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );",
           "\t$fonte_antes = $fonte && ! empty( $fonte['url'] )\n"
           "\t\t? '<span class=\"cdm-f2-fonte\"><a href=\"' . esc_url( $fonte['url'] ) . '\" rel=\"nofollow noopener\">fonte</a></span>'\n"
           "\t\t: '';\n"
           "\t$html .= $fonte_antes;\n"
           "\t$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );")


def m_estado_com_parametro_entra_no_indice(raiz):
    """O `noindex` do estado com parametro cai, e as 45 combinacoes viram URL
    indexavel num dominio recem-nascido (secoes 14.1 e 14.4)."""
    # O ALVO MUDOU EM 25/09/2026, com a casca 1.13.0: ate entao este snippet
    # imprimia a propria etiqueta num `wp_head` paralelo, e a pagina servida
    # ficava com DUAS — medido no ar naquele dia. Agora ele DECLARA a condicao
    # pelo filtro `cdm_fora_do_indice` e quem imprime e a casca, uma vez. Sem
    # retarget a mutacao vira INERTE, que e o pior dos dois estados: a bateria
    # continua verde dizendo que mediu.
    # O ALVO MUDOU DE NOVO EM 28/09/2026: a condicao deixou de ser `escolheu` e
    # passou a ser a PRESENCA do parametro (`cdm_f2_tem_parametro()`). Sem este
    # retarget a mutacao voltaria a ser INERTE, que e o pior dos dois estados.
    editar(raiz, SNIPPET,
           "\treturn $fora || cdm_f2_tem_parametro();",
           "\treturn $fora;")


def m_noindex_volta_a_depender_do_valor(raiz):
    """A REGRESSAO QUE ESTE BLOCO CONSERTOU, escrita de volta: o `noindex` volta a
    sair do `escolheu`, que pergunta se o VALOR esta no vocabulario.

    E o defeito que a ronda da Sentinela mediu no ar em 28/09/2026 —
    `?base=ceramica&onde=externo`, `?base=mdf` e
    `?base=ceramica&caco=louca&junta=fina&onde=interno` servindo UMA etiqueta de
    robo sem `noindex`, porque nenhum daqueles valores existe no vocabulario. Os
    nomes dos quatro parametros eram todos reais; os valores, nenhum.

    Mutacao que reproduz defeito MEDIDO vale mais que mutacao inventada: se esta
    passar, a regua que fechou o item 2 do despacho parou de medir."""
    editar(raiz, SNIPPET,
           "\treturn $fora || cdm_f2_tem_parametro();",
           "\t$e = cdm_f2_entrada();\n\n\treturn $fora || ! empty( $e['escolheu'] );")


def m_faq_do_schema_promete_o_que_a_pagina_nao_diz(raiz):
    """Uma pergunta a mais no FAQPage que nao esta escrita na tela. E o jeito
    classico de FAQPage virar spam, e o jeito classico de ninguem notar."""
    editar(raiz, SNIPPET,
           "\tforeach ( cdm_f2_perguntas() as $p ) {\n\t\t$perguntas[] = array(",
           "\t$extra = cdm_f2_perguntas();\n\t$extra[] = array( 'pergunta' => 'Qual a melhor cola para mosaico?', 'resposta' => 'A melhor de todas.' );\n\tforeach ( $extra as $p ) {\n\t\t$perguntas[] = array(")


def m_script_volta_para_dentro_do_shortcode(raiz):
    """O defeito que derrubou cinco calculadoras da Aquametria em 08/09/2026: o
    <script> volta para dentro do retorno do shortcode e o filtro do conteudo o
    mata convertendo o E-comercial."""
    editar(raiz, SNIPPET,
           "\t$html .= '</div>';\n\n\treturn $html;\n} );",
           "\t$html .= '<script>var a = 1 && 2;</script>';\n\t$html .= '</div>';\n\n\treturn $html;\n} );")


def m_pagina_perde_a_mae(raiz):
    """A pagina nasce solta na raiz: sem `pai`, a URL deixa de mostrar a arvore
    (16.1) e a trilha perde o degrau do meio."""
    editar(raiz, SNIPPET,
           "\t\t'pai'      => 'materiais',",
           "")


def m_nome_diverge_entre_trilha_e_titulo(raiz):
    """A cicatriz da Aquametria de 11/09/2026: o degrau da trilha e o H1 passam a
    dizer nomes diferentes a uma linha de distancia um do outro."""
    editar(raiz, SNIPPET,
           "\t\t\t$lista[ $i ]['titulo'] = CDM_F2_TITULO;",
           "\t\t\t$lista[ $i ]['titulo'] = 'Seletor de cola e rejunte';")


def m_marca_em_dobro_no_nome(raiz):
    """A marca volta a ser colada em todo nome, e os rejuntes viram 'Quartzolit
    Rejunte Ceramicas Quartzolit' na tela."""
    editar(raiz, SNIPPET,
           "\tif ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {\n\t\treturn trim( $nome );\n\t}",
           "\tif ( '' === $marca ) {\n\t\treturn trim( $nome );\n\t}")


def m_acento_volta_a_sumir_no_banco(raiz):
    """O banco volta a servir portugues sem acento — o defeito que este bloco
    encontrou no ar da bancada. Uma string so, num produto so: o teste varre os
    45 estados justamente porque ela pode aparecer em um deles."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-construcao":
            m["nome_comercial"] = "Silicone Acetico Construcao"
    gravar(raiz, "materiais-colas.json", b)


def m_faixa_descoberta_fica_em_branco(raiz):
    """A frase que declara a faixa descoberta some, e a celula sem resposta passa
    a nao dizer nada. Silencio parece defeito; o contrato manda dizer por que."""
    editar(raiz, SNIPPET,
           "Não temos cola para indicar em <strong>",
           "Veja as opções para <strong>")


def m_rotulo_de_base_some(raiz):
    """Uma base do vocabulario fica sem rotulo na tela. Ela sai do formulario e a
    combinacao correspondente deixa de ser respondida — sem erro nenhum."""
    editar(raiz, SNIPPET,
           "\t\t\t'metal'                        => 'Metal (lata, bandeja, moldura de metal)',\n",
           "")


def m_junta_para_em_dez(raiz):
    """O campo volta a parar em 10 mm, e quem tem folga de 11 cai calado no
    padrao de 2 mm — recebendo uma resposta que nao e a dele. Foi assim que este
    estado nasceu, e foi a varredura que o achou."""
    editar(raiz, SNIPPET, "$jun <= 12 ) ? $jun : 2,", "$jun <= 10 ) ? $jun : 2,")
    editar(raiz, SNIPPET, "for ( $i = 1; $i <= 12; $i++ ) {", "for ( $i = 1; $i <= 10; $i++ ) {")


def m_busca_some_quando_ha_ficha(raiz):
    """A segunda porta da 25.2 desaparece: o cartao com ficha volta a ter so o
    botao. E o defeito MENOS visivel dos cinco, porque a pagina continua com
    link de compra em todo cartao — o que se perde e a saida de quem chegou num
    anuncio esgotado, que e exatamente o caso que quebrou quatro links em doze
    horas em 13/09."""
    editar(raiz, SNIPPET,
           "\t\tif ( '' !== $busca ) {\n"
           "\t\t\t$html .= '<a class=\"cdm-f2-busca\" href=\"' . esc_url( $busca ) . '\"'\n"
           "\t\t\t\t. ' rel=\"sponsored noopener\" target=\"_blank\">Veja todos disponíveis aqui</a>';\n"
           "\t\t}\n",
           "")


def m_busca_atropela_a_ficha(raiz):
    """O `elseif` vira `if` independente e a busca passa a ser botao TAMBEM onde
    existe ficha: dois botoes no mesmo cartao, e o leitor nao sabe qual e a
    recomendacao. E o erro de quem troca a escada por 'servir tudo que tiver'."""
    editar(raiz, SNIPPET,
           "\t} elseif ( '' !== $busca ) {",
           "\t}\n\tif ( '' === $ficha && '' !== $busca ) {\n\t\t/* nada */\n\t}\n\tif ( '' !== $busca ) {")


def m_sem_ficha_volta_o_em_breve(raiz):
    """O DEFEITO QUE ESTE BLOCO VEIO CONSERTAR, escrito de volta: sem ficha, o
    cartao volta a dizer "Link de loja em breve" com o piso da 25.2 parado no
    banco. E a forma exata do estado da ilha antes da f2 1.2.0 — a escada existia
    no dado e nao na tela."""
    editar(raiz, SNIPPET,
           "\t} elseif ( '' !== $busca ) {\n"
           "\t\t$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca\" href=\"' . esc_url( $busca ) . '\"'\n"
           "\t\t\t. ' rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';\n",
           "\t} elseif ( false ) {\n")


def m_botao_de_busca_promete_ficha(raiz):
    """O botao da busca passa a dizer "Ver na loja", igual ao da ficha. Nenhuma
    regua de existencia pega isto — o link esta la, marcado, vivo — e mesmo
    assim a pagina promete a ficha do produto recomendado e entrega uma lista de
    busca. E a familia do "faixa aberta mente em silencio" da C15 da Aquametria:
    o filtro esta certo e a FRASE e que afirma o que nao pode."""
    editar(raiz, SNIPPET,
           "target=\"_blank\">Ver as opções na loja</a>';",
           "target=\"_blank\">Ver na loja</a>';")


def m_busca_sem_sponsored(raiz):
    """O link de busca perde o `rel=\"sponsored\"` e a relacao comercial deixa de
    ser declarada em metade dos links da pagina. A afirmacao antiga do portao
    ficava verde aqui, porque olhava a pagina inteira e achava o OUTRO link
    marcado."""
    editar(raiz, SNIPPET,
           "$html .= '<a class=\"cdm-f2-busca\" href=\"' . esc_url( $busca ) . '\"'\n"
           "\t\t\t\t. ' rel=\"sponsored noopener\"",
           "$html .= '<a class=\"cdm-f2-busca\" href=\"' . esc_url( $busca ) . '\"'\n"
           "\t\t\t\t. ' rel=\"noopener\"")


def m_cartao_sem_compra_some(raiz):
    """Sem nenhum degrau, o cartao inteiro desaparece em vez de reservar o lugar:
    a recomendacao passa a depender do link de afiliado existir. E a inversao que
    a secao 7 do contrato proibe — o que a pagina recomenda nao pode ser decidido
    pelo que da para monetizar."""
    # A CONDICAO FOI REESCRITA EM 14/09/2026 PORQUE A MUTACAO TINHA FICADO INERTE.
    # Ela procurava `cdm-f2-sem-loja`, a classe da etiqueta proibida, que deixou de
    # ser emitida na f2 1.5.0 — entao ela editava o snippet, o `if` nunca era
    # verdadeiro, nenhum cartao sumia e a bateria ficava VERDE sem medir nada. E o
    # mesmo defeito que a Robometria nomeou em 14/09 com duas mutacoes suas: a
    # mutacao que deixa de achar o alvo edita NADA e passa. O estado sem nenhuma
    # saida hoje produz bloco de compra VAZIO, e e isso que ela passa a procurar.
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );",
           "\t$bloco_compra = cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );\n"
           "\tif ( '<span class=\"cdm-f2-compra\"></span>' === $bloco_compra ) {\n\t\treturn '';\n\t}\n"
           "\t$html .= $bloco_compra;")


def m_busca_crua_com_sponsored(raiz):
    """A busca CRUA passa a declarar `rel=sponsored`. E a mentira mais barata de
    escrever e a mais dificil de ver: o link continua funcionando, leva a mesma
    loja, e a pagina passa a dizer ao leitor que ganha comissao por um clique que
    nao paga nada. O atributo declara a relacao PAGA, nao o formato do destino."""
    editar(raiz, SNIPPET,
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua\" href=\"' . esc_url( $crua ) . '\"'\n"
           "\t\t\t. ' rel=\"nofollow noopener\"",
           "$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua\" href=\"' . esc_url( $crua ) . '\"'\n"
           "\t\t\t. ' rel=\"sponsored noopener\"")


def m_busca_crua_deixa_de_ser_lida(raiz):
    """O degrau 4 some e a tela volta a nao ler `url_busca_produto` — que e
    exatamente o estado em que esta ilha estava ate 14/09/2026, com o dado no
    banco e nenhuma linha de codigo o lendo. Os quinze itens voltam a ficar sem
    saida de compra, sem nenhuma promessa no lugar."""
    editar(raiz, SNIPPET,
           "\t$crua  = ( is_array( $afiliado ) && ! empty( $afiliado['url_busca_produto'] ) ) ? $afiliado['url_busca_produto'] : '';",
           "\t$crua  = '';")


def m_busca_crua_passa_na_frente_da_ficha(raiz):
    """A busca crua sobe para antes da ficha na escada. O leitor que tinha o
    endereco do produto recomendado passa a cair numa lista de busca — e a ilha
    troca um clique que paga por um que nao paga."""
    editar(raiz, SNIPPET,
           "\tif ( '' !== $ficha ) {",
           "\tif ( '' !== $crua ) {\n\t\t$html .= '<a class=\"cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua\" href=\"' . esc_url( $crua ) . '\"'\n"
           "\t\t\t. ' rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';\n\t} elseif ( '' !== $ficha ) {")



# ------------------------------------------------- A REGRA 6, bloco 3e (13/09/2026)
#
# Estas quinze nascem com a regra e com os dois produtos que a obrigaram. Duas
# coisas as separam das anteriores, e as duas sao exigencia da secao 8 do
# contrato:
#
#   - CADA UMA DECLARA QUAL PORTAO TEM DE REPROVA-LA. Defeito pego pela regra
#     vizinha prova que ALGUMA trava existe, nao que ESTA existe — e metade
#     destas mutacoes fala com o validador do banco, nao com o teste da tela.
#   - VARIAS PRODUZEM O MUNDO. O banco tem UM produto com condicao de
#     superficie; regua escrita sobre um mundo de um elemento so nao e medicao,
#     e sim ausencia de contraexemplo confundida com prova.


def m_condicao_ignorada(raiz):
    """A regra 6 cai: o produto com condicao volta a ser recomendado sempre.

    E a mutacao central do bloco. Sem ela, a pagina manda colar pastilha de
    vidro em vaso de plastico com um adesivo que seca por evaporacao de agua e
    nao tem por onde secar."""
    editar(raiz, SNIPPET,
           "\t\t\t&& cdm_f2_exige_porosa( $m )\n\t\t\t&& ! cdm_f2_condicao_cumprida( $base, $tessela ) ) {",
           "\t\t\t&& cdm_f2_exige_porosa( $m )\n\t\t\t&& false ) {")


def m_condicao_sempre_falha(raiz):
    """O avesso: a condicao passa a reprovar SEMPRE, e o produto some de toda
    combinacao. Erro plausivel de quem inverte o sinal — e ele encolhe a
    resposta em silencio, que e o modo de falhar mais dificil de ver."""
    editar(raiz, SNIPPET,
           "\treturn isset( $p['bases'][ $base ] ) || isset( $p['tesselas'][ $tessela ] );",
           "\treturn false;")


def m_condicao_so_olha_a_base(raiz):
    """A condicao esquece o caquinho. Passa a valer em MDF e cimento e a
    reprovar em plastico mesmo com pastilha de ceramica — ou seja, fecha de
    novo a faixa que este bloco abriu, sem que nenhuma frase da pagina mude."""
    editar(raiz, SNIPPET,
           "\treturn isset( $p['bases'][ $base ] ) || isset( $p['tesselas'][ $tessela ] );",
           "\treturn isset( $p['bases'][ $base ] );")


def m_condicao_manda_para_o_silencio(raiz):
    """A causa nova e jogada no balde do silencio. A elegibilidade fica IGUAL,
    entao a unica coisa que muda e a frase que o leitor recebe: passa a ler que
    o fabricante nao fala daquela superficie quando ele fala. E a mistura de
    causas que a secao 7 proibe desde 12/09/2026, nesta mesma ilha."""
    editar(raiz, SNIPPET,
           "\t\t\t$condicao[] = $id;\n\t\t\tcontinue;",
           "\t\t\t$silencio[] = $id;\n\t\t\tcontinue;")


def m_condicao_antes_das_cinco(raiz):
    """A regra 6 passa a rodar sobre QUEM FOI PROIBIDO tambem, e um produto
    proibido pelo fabricante reaparece no grupo da condicao — que e uma forma
    de ressuscitar proibicao com outro nome."""
    editar(raiz, SNIPPET,
           "\t\t\t&& ( 'recomendado' === $situacao || 'ressalva' === $situacao )",
           "\t\t\t&& true")


def m_recusa_volta_a_negar_a_declaracao(raiz):
    """A frase de recusa volta a dizer que ninguem declara, num estado em que a
    propria pagina cita a declaracao duas secoes abaixo. Foi o defeito que o
    portao pegou nesta execucao, escrito de volta."""
    editar(raiz, SNIPPET,
           "\t} elseif ( $celula['eliminados_por_condicao'] ) {",
           "\t} elseif ( false ) {")


def m_atribuicao_vira_do_fabricante(raiz):
    """A pagina passa a dizer que quem classificou a porosidade foi o
    fabricante. A frase fica mais forte e mais vendavel, e e emprestimo de
    autoridade: secao 26.3 do ARQUIPELAGO.md."""
    editar(raiz, SNIPPET,
           "'somos nós, não ela.';",
           "'foi o próprio fabricante.';")


def m_contagem_do_que_falta_vira_digitada(raiz):
    """O numero da secao "o que a gente ainda nao responde" volta a ser
    digitado. E a forma exata do defeito que esta secao veio consertar: o
    numero nasce certo e envelhece calado."""
    editar(raiz, SNIPPET,
           "\t\t. 'Em <strong>' . cdm_casca_num( $descobertos ) . '</strong> delas a gente ainda não tem cola para indicar, '",
           "\t\t. 'Em <strong>' . cdm_casca_num( 2 ) . '</strong> delas a gente ainda não tem cola para indicar, '")


def m_contagem_esquece_o_caquinho(raiz):
    """A varredura da secao do que falta perde a dimensao do caquinho e passa a
    publicar 45 combinacoes em vez de 270 — afirmacao com escopo menor do que a
    ferramenta responde."""
    editar(raiz, SNIPPET,
           "\t$tess  = array_keys( $rot['tessela'] );",
           "\t$tess  = array( 'pastilha_vidro' );")


def m_tabela_perde_a_coluna_da_condicao(raiz):
    """A tabela pre-renderizada volta a servir "use Cascola PL500" em plastico
    sem dizer a condicao. E a metade que um modelo de linguagem le sem preencher
    formulario, e e onde a afirmacao sem escopo custa mais caro."""
    editar(raiz, SNIPPET,
           "\t\t\tif ( cdm_f2_exige_porosa( $m ) ) {",
           "\t\t\tif ( false ) {")


def m_esquema_perde_a_lista_de_porosas(raiz):
    """A chave `superficies_porosas` some do esquema. E a mutacao que a secao
    26.2 prescreve por escrito: regua que le a propria lista de um arquivo de
    dados aprova tudo, em silencio, no dia em que o arquivo perder a chave. Ela
    nao estraga registro nenhum."""
    esquema = carregar(raiz, "esquema-banco.json")
    del esquema["superficies_porosas"]
    gravar(raiz, "esquema-banco.json", esquema)


def m_base_nova_sem_classificacao(raiz):
    """Uma base sai da classificacao de porosidade sem sair do vocabulario —
    que e o que acontece no dia em que alguem acrescentar uma base e esquecer
    esta lista. Sem a trava das duas direcoes, ela seria tratada como nao
    porosa por omissao, decidindo por silencio."""
    esquema = carregar(raiz, "esquema-banco.json")
    esquema["superficies_porosas"]["bases_nao_porosas"].remove("metal")
    gravar(raiz, "esquema-banco.json", esquema)


def m_porosidade_em_duas_listas(raiz):
    """A mesma base fica porosa E nao porosa. O codigo nao quebra: ele le a
    lista das porosas e ignora a outra, entao a contradicao passaria calada."""
    esquema = carregar(raiz, "esquema-banco.json")
    esquema["superficies_porosas"]["bases_porosas"].append("plastico")
    gravar(raiz, "esquema-banco.json", esquema)


def m_ficha_nao_lida_volta_para_fontes(raiz):
    """PRODUZ O MUNDO: a ficha localizada e nao lida volta para `fontes`, com o
    nivel 2 dela. O produto inteiro sobe de nivel 3 para 2 e a linha de prova da
    tela passa a atribuir a declaracao a um documento que ninguem abriu. Foi o
    que esta execucao quase commitou."""
    colas = carregar(raiz, "materiais-colas.json")
    for m in colas["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-maxx":
            m["fontes"]["ficha-brsa005"] = m.pop("fonte_localizada_nao_lida")
    gravar(raiz, "materiais-colas.json", colas)


def m_condicao_sem_dizer_quem_classifica(raiz):
    """O campo que separa a condicao (do fabricante) da classificacao (nossa)
    some do banco. Sem ele a tela nao tem como escolher a atribuicao certa, e a
    26.3 vira intencao em vez de regra."""
    colas = carregar(raiz, "materiais-colas.json")
    for m in colas["materiais"]:
        c = (m.get("condicoes") or {}).get("exige_superficie_porosa")
        if c:
            del c["quem_classifica_a_porosidade"]
    gravar(raiz, "materiais-colas.json", colas)


def m_segundo_produto_com_condicao(raiz):
    """PRODUZ O MUNDO: um SEGUNDO produto ganha a condicao de superficie, e o
    esquema nao e atualizado. O banco de hoje tem um so, entao a afirmacao que
    cobra a lista `produtos_que_carregam_a_condicao_hoje` nunca foi exercitada
    por um mundo com dois — e produto novo entrando mudo e exatamente o modo de
    falhar que ela existe para impedir."""
    colas = carregar(raiz, "materiais-colas.json")
    for m in colas["materiais"]:
        if m["id"] == "cascola-cascorez-extra":
            m["condicoes"] = {
                "exige_superficie_porosa": {
                    "valor": True,
                    "literal": "seca por evaporacao da agua",
                    "fonte_id": list(m["fontes"].keys())[0],
                    "quem_classifica_a_porosidade": "a ilha",
                }
            }
    gravar(raiz, "materiais-colas.json", colas)


def m_validador_condicao_antes_das_cinco(raiz):
    """A GEMEA DA ANTERIOR, do lado do Python. A de cima edita o snippet e e
    pega pela tela; esta edita o validador e e pega pela afirmacao que ele ja
    tinha e que nunca tinha sido exercitada — "a condicao moveu quem nao estava
    elegivel antes". Duas implementacoes da mesma regra precisam das duas
    mutacoes: quem so muta uma delas mede metade."""
    caminho = os.path.join(raiz, "ferramentas", "validar-banco.py")
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    velho = '        if situacao in ("recomendado", "ressalva") and exige_porosa(m) \\\n                and not condicao_cumprida(base, tessela):'
    novo = '        if exige_porosa(m) \\\n                and not condicao_cumprida(base, tessela):'
    if velho not in texto:
        raise AssertionError("mutacao INERTE: nao achei a guarda da regra 6 no validador")
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, 1))


def m_proibido_com_condicao_cai_no_bloco_errado(raiz):
    """PRODUZ O MUNDO, e sem ele a trava mais nova do portao NAO PODE FALHAR.

    A afirmacao "produto proibido sai no bloco da proibicao, nunca no da
    condicao" nasceu verde e sem poder errar: o banco tem UM produto com
    condicao de superficie e ele nao e proibido em base nenhuma, entao o estado
    que ela mede nao existe. E a cicatriz que a secao 8 do ARQUIPELAGO.md
    descreve com todas as letras — regua escrita para um mundo que nunca
    aconteceu, verde desde sempre.

    Esta mutacao cria o mundo em duas metades: (1) o fabricante do PL500 passa a
    proibir espelho, e (2) a regra 6 passa a rodar tambem sobre quem foi
    proibido. Com as duas, o produto proibido sai da pagina acusado de falta de
    porosidade — a pagina troca a frase mais forte que ela tem ("o fabricante
    escreve espelhos na lista do que este produto nao deve tocar") por uma
    frase sobre outra coisa. A elegibilidade nao muda; so o que o leitor le.
    """
    colas = carregar(raiz, "materiais-colas.json")
    for m in colas["materiais"]:
        if m["id"] == "cascola-pl500-adesivo-de-montagem":
            m["declaracoes"]["nao_usar_em"] = ["espelhos"]
            m["declaracoes"]["indicado_para"].append("espelhos")
    gravar(raiz, "materiais-colas.json", colas)
    editar(raiz, SNIPPET,
           "\t\t\t&& ( 'recomendado' === $situacao || 'ressalva' === $situacao )",
           "\t\t\t&& true")


def m_faixa_descoberta_nega_a_declaracao(raiz):
    """A faixa descoberta volta a dizer que ninguem declarou, e o defeito estava
    NO AR ate 13/09/2026 em quatro estados.

    E a mutacao que mede o conserto deste bloco. Em vidro, madeira, alvenaria e
    metal dentro da agua, o Loctite Durepoxi E declarado pelo proprio fabricante
    para a base E para uso submerso; quem o segura e a regua de PROCEDENCIA da
    ilha, que e nossa. A pagina dizia "nenhum dos adesivos do nosso banco e
    declarado pelo proprio fabricante para esse caso" e duas secoes abaixo
    imprimia "existe mencao a Loctite Durepoxi" — uma frase negando o que a
    outra afirma, dentro da mesma pagina.

    Ninguem tinha visto porque as 18 celulas escritas a mao de ontem TODAS
    tinham recomendacao: a regua independente nunca tinha pisado numa faixa
    descoberta, e o portao so cobrava a PRESENCA da frase, nunca qual causa ela
    nomeia."""
    editar(raiz, SNIPPET,
           "\t} elseif ( $celula['mencionados_com_ressalva'] ) {\n"
           "\t\t/* A QUINTA CAUSA",
           "\t} elseif ( false ) {\n"
           "\t\t/* A QUINTA CAUSA")


def m_vitrine_vazia_nega_a_declaracao(raiz):
    """A metade do mesmo defeito que mora uma secao abaixo da resposta.

    Consertar so a frase-resposta deixaria a vitrine vazia repetindo "nenhum
    produto do nosso banco passa no que o fabricante declara" — e ele passa: o
    que ele nao passa e a nossa regua de fonte. Defeito pego pela regra VIZINHA
    prova que ALGUMA trava existe, nunca que ESTA existe, entao ela tem mutacao
    propria."""
    editar(raiz, SNIPPET,
           "\t\t} elseif ( $celula['mencionados_com_ressalva'] ) {\n"
           "\t\t\t$html .= '<p>Não há o que listar aqui. Não é que ninguém declare",
           "\t\t} elseif ( false ) {\n"
           "\t\t\t$html .= '<p>Não há o que listar aqui. Não é que ninguém declare")


def m_mapa_perde_a_pedra_do_epoxi(raiz):
    """A UNICA MUTACAO DESTE ARQUIVO QUE AS 18 CELULAS DE ONTEM NAO PEGAVAM, e
    ela existe para medir o que o bloco de 13/09/2026 comprou.

    O mapa perde os termos 'pedra' e 'marmore' — e SO esses dois, escolhidos a
    dedo: sao os que o Loctite Durepoxi usa para alvenaria e que o Silicone
    Neutro NAO usa (ele diz 'pedras' e 'alvenaria'). Assim o neutro continua
    respondendo por alvenaria e o unico efeito visivel do defeito e o Durepoxi
    cair de mencao com ressalva para silencio nas QUATRO celulas de alvenaria
    que nasceram neste bloco.

    MEDIDO NOS DOIS MUNDOS, antes de esta funcao ser escrita: com a matriz de 45
    o validador acusa 8 erros; com as 18 celulas de ontem ele fecha em OK e o
    teste-f2 fecha em 107 afirmacoes e 0 falha — o defeito passava inteiro,
    deixando so um AVISO de termo sem traducao, que nao reprova nada. E o que
    justifica a matriz ter ido a 45: cobertura que nao existe nao e cobertura
    que esta verde, e uma regua com buraco fica verde exatamente dentro do
    buraco."""
    esquema = carregar(raiz, "esquema-banco.json")
    termos = esquema["mapa_de_termos_do_fabricante"]["termos"]
    ficam = [t for t in termos if t["literal"] not in ("pedra", "marmore")]
    if len(ficam) != len(termos) - 2:
        raise AssertionError(
            "mutacao INERTE: esperava remover 2 termos do mapa, removeu %d"
            % (len(termos) - len(ficam)))
    esquema["mapa_de_termos_do_fabricante"]["termos"] = ficam
    gravar(raiz, "esquema-banco.json", esquema)


# --------------------------------------------------- a REGRA 7 (06/10/2026)
#
# Ela entrou consertando um defeito que ESTAVA NO AR, e isso muda o que estas
# mutacoes tem de provar: nao basta a regra existir, ela tem de morder na celula
# certa e so nela. A ancora da regra 6 escrita a mao em 13/09 declarava o
# acetico no topo de `vidro` + `caco de espelho`, e as duas metades do portao
# concordavam — o que uma regua independente nao pega e a lacuna que as duas tem.

def m_regra7_ignorada(raiz):
    """A regra 7 cai: quem o fabricante proibe no caquinho volta a ser
    recomendado. E a mutacao central do bloco, e o estado que ela restaura e o
    que estava servido ate hoje — o acetico no topo para quem cola caco de
    espelho, com a Tekbond escrevendo `espelhos` na lista do que ele nao toca."""
    editar(raiz, SNIPPET,
           "\t\t\t&& cdm_f2_peca_proibida( $m, $tessela ) ) {",
           "\t\t\t&& false ) {")


def m_regra7_morde_todo_caquinho(raiz):
    """O avesso: a proibicao passa a valer para TODO caquinho, e o produto some
    de toda combinacao. Erro plausivel de quem esquece de cruzar a lista — e ele
    encolhe a resposta em silencio, o modo de falhar mais dificil de ver. Quem
    pega e a CELULA DE CONTROLE, que roda o mesmo estado com caquinho livre."""
    editar(raiz, SNIPPET,
           "\t\tif ( ! isset( $mapa['grupos'][ $g ] ) || isset( $mapa['grupos'][ $g ]['tesselas'][ $tessela ] ) ) {",
           "\t\tif ( true ) {")


def m_regra7_manda_para_o_silencio(raiz):
    """A causa nova e jogada no balde do silencio. A elegibilidade fica IGUAL,
    entao a unica coisa que muda e a frase que o leitor recebe: passa a ler que
    o fabricante nao fala daquela superficie quando ele escreveu para nao usar
    nela. Mistura de causas, secao 7, a mesma de 12/09/2026."""
    editar(raiz, SNIPPET,
           "\t\t\t$peca[] = $id;\n\t\t\tcontinue;",
           "\t\t\t$silencio[] = $id;\n\t\t\tcontinue;")


def m_regra7_antes_das_cinco(raiz):
    """A regra 7 passa a rodar sobre QUEM FOI PROIBIDO tambem, e um produto
    proibido pela base ou pelo ambiente reaparece no grupo da peca — que e
    ressuscitar proibicao com outro nome e trocar a frase do leitor inteira.
    E a ancora `ceramica x contato permanente com agua x caco de espelho` que
    existe para medir isto."""
    editar(raiz, SNIPPET,
           "\t\t\t&& ( 'recomendado' === $situacao || 'ressalva' === $situacao )\n"
           "\t\t\t&& cdm_f2_peca_proibida( $m, $tessela ) ) {",
           "\t\t\t&& true\n\t\t\t&& cdm_f2_peca_proibida( $m, $tessela ) ) {")


def m_regra7_recusa_volta_a_negar_a_declaracao(raiz):
    """PRODUZ O MUNDO: a frase de recusa da regra 7 some, e a celula que ela
    esvazia volta a dizer outra causa — a declaracao de nivel 4 do Durepoxi, que
    nao e o que tirou ninguem dali.

    ESTA MUTACAO PASSOU NA PRIMEIRA RODADA, e e por isso que ela produz o mundo.
    Apagar o ramo nao reprovava nada: nas seis celulas em que a regra 7 morde
    HOJE sempre sobra alguem recomendado, entao o ramo nunca e alcancado — e
    codigo que o portao nao ve e a mesma familia do `else` morto da regra 6, que
    ficou no ar dizendo a frase errada em quatro estados ate 13/09/2026.

    O mundo e o minimo que torna o ramo alcancavel: em `ceramica` + `caco de
    espelho` + `externo abrigado` os TRES elegiveis sao o acetico, o Maxx e o
    neutro; dando `espelho` aos dois que ainda nao o tem, a celula esvazia. Nao
    e mundo arbitrario — e exatamente o mundo que a pendencia nomeada do Maxx
    diz que pode chegar com um documento."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] in ("tekbond-silicone-acetico-maxx", "tekbond-silicone-neutro"):
            # NAO mexe em `declaracoes`: por um instante esta mutacao escrevia
            # `nao_usar_em: ["espelhos"]` nos dois, e isso tirava o neutro da BASE
            # `espelho` pela regra 1 — a reprovacao passava a vir da trava VIZINHA
            # (a matriz escrita a mao das 45 celulas), nao do ramo apagado.
            m["condicoes"] = {"proibe_grupos_de_tessela": {
                "valor": ["espelho"],
                "literais": {"espelho": "espelhos"},
                "onde_o_fabricante_escreve": "declaracoes.nao_usar_em",
                "fonte_id": sorted((m.get("fontes") or {}))[0],
                "quem_classifica_o_grupo": "a ilha",
            }}
    gravar(raiz, "materiais-colas.json", b)
    editar(raiz, SNIPPET,
           "\t} elseif ( $celula['eliminados_por_proibicao_da_peca'] ) {",
           "\t} elseif ( false ) {")


def m_regra7_atribuicao_vira_do_fabricante(raiz):
    """A pagina passa a dizer que quem classificou o caquinho dentro da palavra
    do fabricante foi ele. A frase fica mais forte e e emprestimo de autoridade
    — secao 26.3, e aqui a tentacao e maior que na regra 6, porque a nossa
    leitura (caco de espelho e espelho) parece obvia."""
    editar(raiz, SNIPPET,
           "\t\t\t\t. 'nessa frase somos nós, não ela.",
           "\t\t\t\t. 'nessa frase é a própria fabricante.")


def m_regra7_bloco_sem_a_frase_do_fabricante(raiz):
    """O bloco deixa de citar a frase do fabricante e passa a afirmar a
    proibicao com as nossas palavras. E a metade que a secao 15.2 cobra: sem o
    literal, a pagina diz `o fabricante proibe` sem mostrar onde."""
    editar(raiz, SNIPPET,
           "\t\t\t\t. esc_html( cdm_f2_lista_humana( $literais ) ) . '</em>, e quem diz que <em>'",
           "\t\t\t\t. esc_html( 'uma restrição de uso' ) . '</em>, e quem diz que <em>'")


def m_regra7_saida_vira_digitada(raiz):
    """A unica frase da pagina que diz a pessoa o que FAZER para a peca nao
    descolar volta a ser digitada. Digitada, ela erra calada no dia em que um
    caquinho novo entrar no vocabulario — e erra do jeito caro, mandando colar.
    Mesma familia de `m_contagem_do_que_falta_vira_digitada`."""
    editar(raiz, SNIPPET,
           "\t\t\t$sobram = cdm_f2_caquinhos_fora_dos_grupos( $grupos );",
           "\t\t\t$sobram = 'pastilha de vidro';")


def m_tabela_perde_a_coluna_da_peca(raiz):
    """A tabela pre-renderizada volta a servir "ceramica, no sol e na chuva: use
    Tekbond Silicone Acetico Construcao" sem dizer com que caquinho nao serve. E
    a metade que um modelo de linguagem le sem preencher formulario, e e onde a
    afirmacao sem escopo custa mais caro."""
    editar(raiz, SNIPPET,
           "\t\t\tif ( $grupos_do_m ) {",
           "\t\t\tif ( false ) {")


def m_esquema_perde_os_grupos_de_peca(raiz):
    """A chave `grupos_de_tessela_proibidos` some do esquema. Secao 26.2 por
    escrito: regua que le a propria lista de um arquivo de dados aprova tudo, em
    silencio, no dia em que o arquivo perder a chave. Nenhum registro e tocado."""
    esquema = carregar(raiz, "esquema-banco.json")
    del esquema["grupos_de_tessela_proibidos"]
    gravar(raiz, "esquema-banco.json", esquema)


def m_caquinho_sem_classificacao_de_grupo(raiz):
    """Um caquinho sai da classificacao de um grupo sem sair do vocabulario — o
    que acontece no dia em que alguem acrescentar uma tessela e esquecer esta
    lista. Sem a trava das duas direcoes ele seria tratado como FORA do grupo
    por omissao, e aqui a omissao deixa passar: e a direcao caro."""
    esquema = carregar(raiz, "esquema-banco.json")
    esquema["grupos_de_tessela_proibidos"]["grupos"]["espelho"]["tesselas_fora_do_grupo"].remove("pedra")
    gravar(raiz, "esquema-banco.json", esquema)


def m_caquinho_em_duas_listas_do_grupo(raiz):
    """O mesmo caquinho fica dentro E fora do grupo. O codigo nao quebra: ele le
    a lista de dentro e ignora a outra, entao a contradicao passaria calada."""
    esquema = carregar(raiz, "esquema-banco.json")
    esquema["grupos_de_tessela_proibidos"]["grupos"]["espelho"]["tesselas_no_grupo"].append("pedra")
    gravar(raiz, "esquema-banco.json", esquema)


def m_grupo_sem_por_que_de_um_caquinho(raiz):
    """A classificacao de um caquinho perde o motivo escrito. A lista e NOSSA, e
    sem motivo por caquinho a proxima execucao nao sabe se `pastilha_ceramica`
    entrou medida ou por descuido — e foi por isso que a regra_da_direcao
    existe."""
    esquema = carregar(raiz, "esquema-banco.json")
    del esquema["grupos_de_tessela_proibidos"]["grupos"]["revestimento_especial"]["por_que_cada_uma"]["pastilha_ceramica"]
    gravar(raiz, "esquema-banco.json", esquema)


def m_proibicao_sem_dizer_quem_classifica(raiz):
    """O registro para de dizer quem classifica o grupo. A tela continua
    imprimindo a frase dividida, mas o banco deixa de sustentar a divisao — e o
    portao da 26.3 tem de medir no banco tambem, nao so na tela."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-construcao":
            del m["condicoes"]["proibe_grupos_de_tessela"]["quem_classifica_o_grupo"]
    gravar(raiz, "materiais-colas.json", b)


def m_literal_do_registro_nao_esta_na_declaracao(raiz):
    """A citacao da regra 7 deixa de voltar a declaracao do fabricante: o
    literal gravado passa a ser uma frase que ele nunca escreveu neste registro.
    E a forma mais barata de a pagina citar uma proibicao inventada, porque a
    frase continua com cara de declaracao."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-construcao":
            m["condicoes"]["proibe_grupos_de_tessela"]["literais"]["espelho"] = \
                "nao use em espelhos nem em superficies espelhadas"
    gravar(raiz, "materiais-colas.json", b)


def m_grupo_declarado_que_nao_existe_no_esquema(raiz):
    """O registro declara um grupo que a lista do esquema nao tem. Sem a trava,
    `peca_proibida` nao acha o grupo e o produto passa — proibicao declarada que
    nao elimina ninguem, com o campo preenchido para quem olhar."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-construcao":
            m["condicoes"]["proibe_grupos_de_tessela"]["valor"] = ["espelho_e_vidro"]
            m["condicoes"]["proibe_grupos_de_tessela"]["literais"] = {"espelho_e_vidro": "espelhos"}
    gravar(raiz, "materiais-colas.json", b)


def m_segundo_produto_com_proibicao_de_peca(raiz):
    """PRODUZ O MUNDO: um segundo produto ganha proibicao de peca e entra MUDO,
    sem passar pela matriz escrita a mao. E o caminho pelo qual um registro novo
    muda a resposta de dezenas de celulas sem ninguem escrever uma linha —
    irma da mutacao da regra 6."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-neutro":
            m["condicoes"] = {"proibe_grupos_de_tessela": {
                "valor": ["espelho"],
                "literais": {"espelho": "espelhos"},
                "onde_o_fabricante_escreve": "declaracoes.indicado_para",
                "fonte_id": sorted((m.get("fontes") or {}))[0],
                "quem_classifica_o_grupo": "a ilha",
            }}
    gravar(raiz, "materiais-colas.json", b)


def m_grupo_que_ninguem_declara(raiz):
    """Um grupo fica no esquema sem nenhum produto que o declare — lista que
    cresce por previsao, o mesmo defeito que a varredura de apoio ja mede em
    `material_de_contato_do_apoio`. Grupo sem dono nao reprova nada e da a
    impressao de que a ilha mede mais do que mede."""
    esquema = carregar(raiz, "esquema-banco.json")
    g = esquema["grupos_de_tessela_proibidos"]["grupos"]
    g["pedra_natural"] = {
        "literal_que_o_origina": "pedras naturais",
        "quem_declara": "ninguem",
        "onde_o_fabricante_escreve": "declaracoes.nao_usar_em",
        "tesselas_no_grupo": ["pedra"],
        "tesselas_fora_do_grupo": [t for t in esquema["vocabularios"]["material_tessela"]
                                   if t != "pedra"],
        "por_que_cada_uma": {t: "inventado pela mutacao"
                             for t in esquema["vocabularios"]["material_tessela"]},
    }
    esquema["matriz_esperada_da_proibicao_sobre_a_peca"]["caquinhos_em_que_cada_grupo_MORDE"]["pedra_natural"] = ["pedra"]
    esquema["matriz_esperada_da_proibicao_sobre_a_peca"]["total_de_pares"] = \
        len(g) * len(esquema["vocabularios"]["material_tessela"])
    gravar(raiz, "esquema-banco.json", esquema)


def m_validador_regra7_antes_das_cinco(raiz):
    """A mesma inversao da ordem, agora no VALIDADOR. Ele tem a propria copia da
    regra por desenho (secao 8), entao a trava tem de existir duas vezes — e uma
    das duas podia estar certa sozinha sem ninguem notar."""
    editar(raiz, "ferramentas/validar-banco.py",
           '        if situacao in ("recomendado", "ressalva") and peca_proibida(m, tessela):',
           '        if peca_proibida(m, tessela):')


def m_ordem_das_duas_regras_novas_invertida(raiz):
    """PRODUZ O MUNDO E INVERTE A ORDEM: o PL500 ganha a proibicao de `espelho`,
    e passa a cair nas DUAS regras na mesma celula (`vidro` + `caco de
    espelho`), porque nem vidro nem espelho absorvem agua. O mundo e escrito
    inteiro — matriz, os dois pares de ancoras — como quem o produzisse de
    verdade escreveria; so depois a ordem e invertida no validador. Sem isto a
    frase `a regra 7 roda antes da 6` seria uma intencao escrita no esquema e
    nunca medida, porque HOJE nenhum produto do banco cai nas duas."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "cascola-pl500-adesivo-de-montagem":
            m["condicoes"]["proibe_grupos_de_tessela"] = {
                "valor": ["espelho"],
                "literais": {"espelho": "espelhos"},
                "onde_o_fabricante_escreve": "declaracoes.nao_usar_em",
                "fonte_id": "pagina-produto-pl500",
                "quem_classifica_o_grupo": "a ilha",
            }
            m["declaracoes"]["nao_usar_em"] = ["espelhos"]
    gravar(raiz, "materiais-colas.json", b)

    esquema = carregar(raiz, "esquema-banco.json")
    mp = esquema["matriz_esperada_da_proibicao_sobre_a_peca"]
    mp["produtos_que_carregam_a_proibicao_hoje"]["cascola-pl500-adesivo-de-montagem"] = ["espelho"]
    for a in mp["ancoras_ponta_a_ponta"]:
        if (a["base"], a["ambiente"], a["tessela"]) == ("vidro", "interno_seco", "caco_espelho"):
            a["eliminados_por_proibicao_da_peca"] = ["cascola-pl500-adesivo-de-montagem",
                                                     "tekbond-silicone-acetico-construcao"]
            a["eliminados_por_condicao"] = []
    for a in esquema["matriz_esperada_da_condicao_de_superficie"]["ancoras_ponta_a_ponta"]:
        if (a["base"], a["ambiente"], a["tessela"]) == ("vidro", "interno_seco", "caco_espelho"):
            a["eliminados_por_condicao"] = []
    gravar(raiz, "esquema-banco.json", esquema)

    v = "ferramentas/validar-banco.py"
    editar(raiz, v,
           '        if situacao in ("recomendado", "ressalva") and peca_proibida(m, tessela):\n'
           '            peca.append(ident)\n'
           '            continue\n'
           '        if situacao in ("recomendado", "ressalva") and exige_porosa(m) \\\n'
           '                and not condicao_cumprida(base, tessela):\n'
           '            condicao.append(ident)\n'
           '            continue',
           '        if situacao in ("recomendado", "ressalva") and exige_porosa(m) \\\n'
           '                and not condicao_cumprida(base, tessela):\n'
           '            condicao.append(ident)\n'
           '            continue\n'
           '        if situacao in ("recomendado", "ressalva") and peca_proibida(m, tessela):\n'
           '            peca.append(ident)\n'
           '            continue')


MUTACOES = [
    ("proibicao do fabricante deixa de vencer", m_proibicao_deixa_de_vencer),
    ("silencio do fabricante vira 'pode'", m_silencio_vira_pode),
    ("ambiente critico passa a aceitar silencio", m_ambiente_critico_aceita_silencio),
    ("nivel de fonte deixa de limitar a recomendacao", m_nivel_de_fonte_deixa_de_limitar),
    ("faixa de junta abre 1 mm para baixo", m_junta_abre_um_milimetro),
    ("faixa de junta pela metade vira sem limite", m_faixa_pela_metade_vira_sem_limite),
    ("a categoria some da pergunta (rejunte na matriz da cola)", m_categoria_some_da_pergunta),
    ("a secao do que nao usar desaparece", m_secao_do_que_nao_usar_some),
    ("as tabelas pre-renderizadas saem do HTML servido", m_tabela_pre_renderizada_some),
    ("compra depois da procedencia no cartao", m_compra_depois_da_procedencia),
    ("estado com parametro entra no indice", m_estado_com_parametro_entra_no_indice),
    ("o noindex volta a depender do VALOR (regressao de 28/09)", m_noindex_volta_a_depender_do_valor),
    ("FAQPage promete pergunta que a pagina nao mostra", m_faq_do_schema_promete_o_que_a_pagina_nao_diz),
    ("<script> volta para dentro do shortcode", m_script_volta_para_dentro_do_shortcode),
    ("a pagina perde a mae e nasce na raiz", m_pagina_perde_a_mae),
    ("o nome diverge entre a trilha e o titulo", m_nome_diverge_entre_trilha_e_titulo),
    ("a marca sai em dobro no nome do produto", m_marca_em_dobro_no_nome),
    ("o acento volta a sumir numa string do banco", m_acento_volta_a_sumir_no_banco),
    ("a faixa descoberta deixa de ser declarada", m_faixa_descoberta_fica_em_branco),
    ("uma base do vocabulario fica sem rotulo", m_rotulo_de_base_some),
    ("o campo de junta volta a parar em 10 mm", m_junta_para_em_dez),
    # A escada da secao 25 na tela (f2 1.2.0, 13/09/2026)
    ("a busca some do cartao que tem ficha", m_busca_some_quando_ha_ficha),
    ("a busca vira botao POR CIMA da ficha", m_busca_atropela_a_ficha),
    ("sem ficha, volta o 'em breve' com piso no banco", m_sem_ficha_volta_o_em_breve),
    ("o botao de busca promete a ficha do produto", m_botao_de_busca_promete_ficha),
    ("o link de busca perde o rel=sponsored", m_busca_sem_sponsored),
    ("cartao sem nenhum degrau some em vez de reservar o lugar", m_cartao_sem_compra_some),
    ("a busca CRUA declara sponsored — comissao que nao existe", m_busca_crua_com_sponsored),
    ("a tela volta a NAO ler url_busca_produto (o estado ate 14/09)", m_busca_crua_deixa_de_ser_lida),
    ("a busca crua passa na frente da ficha na escada", m_busca_crua_passa_na_frente_da_ficha),
    # --- regra 6, bloco 3e. A terceira coluna diz QUAL portao tem de reprovar:
    #     "tela" = ferramentas/teste-f2.php; "banco" = ferramentas/validar-banco.py.
    #     Sem ela, uma mutacao reprovada pela trava VIZINHA passaria por prova de
    #     que a trava NOVA existe.
    ("a regra 6 e ignorada: quem tem condicao e recomendado sempre", m_condicao_ignorada, "tela"),
    ("a condicao reprova SEMPRE e o produto some de tudo", m_condicao_sempre_falha, "tela"),
    ("a condicao esquece o caquinho e so olha a base", m_condicao_so_olha_a_base, "tela"),
    ("a condicao manda o produto para o balde do silencio", m_condicao_manda_para_o_silencio, "tela"),
    ("a condicao roda antes das cinco e ressuscita proibido", m_condicao_antes_das_cinco, "tela"),
    ("a recusa volta a negar a declaracao que a pagina cita", m_recusa_volta_a_negar_a_declaracao, "tela"),
    ("a classificacao de porosidade vira declaracao do fabricante", m_atribuicao_vira_do_fabricante, "tela"),
    ("o numero do que falta volta a ser digitado", m_contagem_do_que_falta_vira_digitada, "tela"),
    ("a contagem do que falta esquece o caquinho", m_contagem_esquece_o_caquinho, "tela"),
    ("a tabela pre-renderizada perde a coluna da condicao", m_tabela_perde_a_coluna_da_condicao, "tela"),
    ("o esquema perde a lista de superficies porosas", m_esquema_perde_a_lista_de_porosas, "banco"),
    ("uma base fica sem classificacao de porosidade", m_base_nova_sem_classificacao, "banco"),
    ("a mesma base fica porosa E nao porosa", m_porosidade_em_duas_listas, "banco"),
    ("PRODUZ O MUNDO: a ficha nao lida volta para fontes", m_ficha_nao_lida_volta_para_fontes, "banco"),
    ("a condicao para de dizer quem classifica a porosidade", m_condicao_sem_dizer_quem_classifica, "banco"),
    ("PRODUZ O MUNDO: um segundo produto ganha a condicao, mudo", m_segundo_produto_com_condicao, "banco"),
    ("no VALIDADOR, a condicao roda antes das cinco", m_validador_condicao_antes_das_cinco, "banco"),
    ("PRODUZ O MUNDO: proibido COM condicao sai no bloco errado", m_proibido_com_condicao_cai_no_bloco_errado, "tela"),
    # --- a matriz escrita a mao de 18 para 45 celulas (13/09/2026)
    ("a faixa descoberta volta a negar a declaracao que a pagina cita", m_faixa_descoberta_nega_a_declaracao, "tela"),
    ("a vitrine vazia volta a negar a mesma declaracao", m_vitrine_vazia_nega_a_declaracao, "tela"),
    ("SO AS 27 CELULAS NOVAS PEGAM: o mapa perde a pedra do epoxi", m_mapa_perde_a_pedra_do_epoxi, "banco"),
    # --- regra 7, 06/10/2026. Mesma terceira coluna: qual portao tem de reprovar.
    ("a regra 7 e ignorada: quem o fabricante proibe no caquinho volta ao topo", m_regra7_ignorada, "tela"),
    ("a proibicao de peca morde TODO caquinho", m_regra7_morde_todo_caquinho, "tela"),
    ("a proibicao de peca vai para o balde do silencio", m_regra7_manda_para_o_silencio, "tela"),
    ("a regra 7 roda antes das cinco e ressuscita proibido", m_regra7_antes_das_cinco, "tela"),
    ("PRODUZ O MUNDO: a recusa da regra 7 some na celula que ela esvazia", m_regra7_recusa_volta_a_negar_a_declaracao, "tela"),
    ("a classificacao do caquinho vira declaracao do fabricante", m_regra7_atribuicao_vira_do_fabricante, "tela"),
    ("o bloco da peca para de citar a frase do fabricante", m_regra7_bloco_sem_a_frase_do_fabricante, "tela"),
    ("a saida 'troque o caquinho' volta a ser digitada", m_regra7_saida_vira_digitada, "tela"),
    ("a tabela pre-renderizada perde a coluna da proibicao de peca", m_tabela_perde_a_coluna_da_peca, "tela"),
    ("o esquema perde a lista de grupos de peca", m_esquema_perde_os_grupos_de_peca, "banco"),
    ("um caquinho fica sem classificacao de grupo", m_caquinho_sem_classificacao_de_grupo, "banco"),
    ("o mesmo caquinho fica dentro E fora do grupo", m_caquinho_em_duas_listas_do_grupo, "banco"),
    ("a classificacao de um caquinho perde o motivo escrito", m_grupo_sem_por_que_de_um_caquinho, "banco"),
    ("a proibicao de peca para de dizer quem classifica o grupo", m_proibicao_sem_dizer_quem_classifica, "banco"),
    ("a citacao da regra 7 nao volta mais a declaracao do fabricante", m_literal_do_registro_nao_esta_na_declaracao, "banco"),
    ("o registro declara grupo que o esquema nao tem", m_grupo_declarado_que_nao_existe_no_esquema, "banco"),
    ("PRODUZ O MUNDO: um segundo produto ganha proibicao de peca, mudo", m_segundo_produto_com_proibicao_de_peca, "banco"),
    ("um grupo fica no esquema sem nenhum produto que o declare", m_grupo_que_ninguem_declara, "banco"),
    ("no VALIDADOR, a regra 7 roda antes das cinco", m_validador_regra7_antes_das_cinco, "banco"),
    ("PRODUZ O MUNDO: as regras 6 e 7 trocam de ordem na mesma celula", m_ordem_das_duas_regras_novas_invertida, "banco"),
]


def rodar_teste(raiz, portao="tela"):
    """Roda o portao que a mutacao declarou.

    Uma mutacao pode ser reprovada pela trava VIZINHA e nao pela que ela mira —
    e ai o verde prova que ALGUMA trava existe, nunca que ESTA existe. Por isso
    cada mutacao da regra 6 nomeia o portao, e e so ele que decide.
    """
    if portao == "banco":
        r = subprocess.run([sys.executable, os.path.join(raiz, "ferramentas", "validar-banco.py")],
                           capture_output=True, text=True, cwd=raiz)
    else:
        r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-f2.php"), raiz],
                           capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A F2 de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("F2 intacta: APROVADA (como tem que estar antes de comecar)\n")

    base_rc_banco, base_saida_banco = rodar_teste(ILHA, "banco")
    if base_rc_banco != 0:
        print("O banco de verdade ja esta reprovado — conserte antes de mutar.")
        print("\n".join(l for l in base_saida_banco.splitlines() if "ERRO" in l or "-" == l[:1]))
        return 1
    print("Banco intacto: APROVADO\n")

    passaram = []
    for entrada in MUTACOES:
        nome, mutar = entrada[0], entrada[1]
        portao = entrada[2] if len(entrada) > 2 else "tela"
        tmp = tempfile.mkdtemp(prefix="mut-f2-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [" + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = rodar_teste(copia, portao)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if "FALHA" in linha or linha.strip().startswith("- "):
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia [%s]: %-48s | %s" % (portao, nome, primeira[:70]))
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

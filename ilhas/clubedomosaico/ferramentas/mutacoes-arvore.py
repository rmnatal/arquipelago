#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a arvore da casca 1.3.0 de proposito, uma mutacao por vez, e exige que
`teste-casca.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-arvore.py

Por que este arquivo existe: as travas da secao 16 ficaram verdes na primeira
execucao, e verde na primeira execucao e prova nenhuma (secao 8 do
ARQUIPELAGO.md). Trava que ninguem viu reprovar nao mediu nada.

AS MUTACOES QUE MAIS VALEM AQUI NAO SAO AS OBVIAS. Sao quatro:

  * O DEGRAU DO MEIO SEM `item` NO SCHEMA. E a mutacao que um schema "mais
    completo" faria de boa fe: pondo no BreadcrumbList tambem o degrau que ainda
    nao tem pagina. Ela invalida a lista inteira para o Google, e lista invalida
    e lista ignorada — o schema publicaria MENOS parecendo publicar mais. Hoje
    nenhum degrau desta ilha esta sem endereco, entao a mutacao precisa PRIMEIRO
    fabricar o degrau sem pagina para a trava ter o que ver;

  * O TETO DE 4 DO 16.4(c) TROCADO POR 5. Com tres secoes no ar, nenhuma pagina
    chega a ter cinco irmas candidatas — a mutacao nao mudaria uma linha do que o
    site serve e o portao ficaria verde nas duas versoes. So a borda FABRICADA
    pela bancada (modo `todas`) da ao teto o que cortar. E o mesmo defeito da
    grade que nao pisa na borda, com a borda faltando no mundo e nao no teste;

  * A BANCADA VOLTAR A MEDIR FORA DE ORDEM. Rodar `the_content` antes do bloco de
    titulo faz a trilha cair DENTRO do corpo, abaixo do H1 — e foi exatamente
    isso que a primeira versao desta bancada fez, reprovando oito paginas por um
    defeito que so existia nela. A mutacao prova que a trava enxerga a ORDEM e
    nao so a presenca;

  * O DOCUMENTO E O CODIGO SE SEPARANDO EM SILENCIO. Mudar a mae no ARVORE.md e
    deixar o codigo como esta e o jeito normal de as duas metades divergirem:
    ninguem le os dois no mesmo dia.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")
RENDER = os.path.join("ferramentas", "render-para-teste.php")
ARVORE = "ARVORE.md"
LOJA = os.path.join("snippets", "clubedomosaico-loja.php")
PECAS = os.path.join("dados", "pecas.json")
VOZ = "VOZ.md"


def ler(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, rel, texto):
    with open(os.path.join(raiz, rel), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, rel, antigo, novo, vezes=1):
    texto = ler(raiz, rel)
    if antigo not in texto:
        raise AssertionError("mutacao nao achou o alvo em %s: %r" % (rel, antigo[:70]))
    gravar(raiz, rel, texto.replace(antigo, novo, vezes))


# ------------------------------------------------------------------ mutacoes

def m_home_ganha_trilha(raiz):
    """16.3 diz que a home nao tem trilha. Aqui ela ganha uma."""
    trocar(raiz, CASCA,
           "\tif ( function_exists( 'is_front_page' ) && is_front_page() ) {\n\t\treturn '';\n\t}",
           "\tif ( false ) {\n\t\treturn '';\n\t}")
    trocar(raiz, CASCA,
           "'materiais/como-sabemos'  => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),",
           "'materiais/como-sabemos'  => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),\n\t\t'inicio' => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Início' ),")


def m_trilha_depois_do_h1(raiz):
    """A trilha sai, mas abaixo do titulo — deixa de ser 'abaixo do header'."""
    trocar(raiz, CASCA,
           "\treturn $trilha . $conteudo;\n}, 10, 2 );",
           "\treturn $conteudo . $trilha;\n}, 10, 2 );")


def m_bancada_mede_fora_de_ordem(raiz):
    """A bancada volta a rodar the_content ANTES do bloco de titulo.

    E o defeito que a primeira versao desta bancada teve: o cinto de seguranca de
    prioridade 9 dispara, a trilha vai para dentro do corpo e o render passa a
    servir uma pagina que o site nao serve.
    """
    texto = ler(raiz, RENDER)
    alvo_h1 = "\t$h1 = '' !== $h1\n\t\t? apply_filters('render_block', $h1, array('blockName'=>'core/post-title')) . \"\\n\"\n\t\t: '';\n"
    alvo_corpo = "\t$corpo = apply_filters('the_content', $corpo_cru);\n"
    if alvo_h1 not in texto or alvo_corpo not in texto:
        raise AssertionError("mutacao nao achou a ordem do render")
    texto = texto.replace(alvo_h1, "").replace(alvo_corpo, alvo_corpo + alvo_h1)
    gravar(raiz, RENDER, texto)


def m_degrau_morto_na_trilha(raiz):
    """A trilha passa a linkar o degrau que ainda nao tem pagina — 404 no ar."""
    trocar(raiz, CASCA,
           "\t\t} else {\n\t\t\t$html .= '<span class=\"cdm-trilha-espera\">' . esc_html( $d['rotulo'] ) . '</span>';",
           "\t\t} else {\n\t\t\t$html .= '<a href=\"' . esc_url( home_url( '/' . $d['rotulo'] . '/' ) ) . '\">' . esc_html( $d['rotulo'] ) . '</a>';")


def m_schema_leva_degrau_sem_endereco(raiz):
    """O schema 'mais completo' que publica MENOS.

    Fabrica primeiro o degrau sem pagina — uma categoria de nivel 2 entre
    /materiais/ e a pagina de bastidor — e so entao tira do JSON-LD a linha que
    pula o degrau sem endereco. Sem fabricar o degrau, a mutacao seria inerte:
    hoje todos os degraus desta ilha tem pagina.
    """
    trocar(raiz, CASCA,
           "'materiais/como-sabemos'  => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),",
           "'materiais/bastidor'      => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Bastidor' ),\n\t\t'materiais/como-sabemos'  => array( 'nivel' => 3, 'mae' => 'materiais/bastidor', 'rotulo' => 'Como sabemos' ),")
    trocar(raiz, CASCA,
           "\tforeach ( $degraus as $d ) {\n\t\tif ( '' === $d['url'] ) {\n\t\t\tcontinue;\n\t\t}\n\t\t$pos++;",
           "\tforeach ( $degraus as $d ) {\n\t\t$pos++;")


def m_teto_de_irmas_vira_cinco(raiz):
    """O teto do 16.4(c) sobe de 4 para 5.

    Inerte no site de hoje — so a borda fabricada pelo modo `todas` da bancada
    tem candidatas suficientes para o teto cortar.
    """
    trocar(raiz, CASCA,
           "\treturn array_slice( $irmas, 0, 4 );",
           "\treturn array_slice( $irmas, 0, 5 );")


def m_cluster_com_uma_irma_so(raiz):
    """Bloco 'Veja tambem' com uma irma so — deixa de ser cluster e vira enfeite."""
    trocar(raiz, CASCA,
           "\t$irmas = cdm_casca_irmas( $slug );\n\tif ( count( $irmas ) < 2 ) {\n\t\treturn '';\n\t}",
           "\t$irmas = cdm_casca_irmas( $slug );\n\tif ( count( $irmas ) < 1 ) {\n\t\treturn '';\n\t}")


def m_irma_de_outra_mae(raiz):
    """Irma escolhida por qualquer mae — cluster ralo, que nao passa autoridade."""
    trocar(raiz, CASCA,
           "\t\tif ( $caminho === $slug || $def['mae'] !== $minha || 0 === (int) $def['nivel'] ) {",
           "\t\tif ( $caminho === $slug || 0 === (int) $def['nivel'] ) {")


def m_pagina_se_lista_como_irma(raiz):
    """A pagina entra na propria lista de irmas."""
    trocar(raiz, CASCA,
           "\t\tif ( $caminho === $slug || $def['mae'] !== $minha || 0 === (int) $def['nivel'] ) {",
           "\t\tif ( $def['mae'] !== $minha || 0 === (int) $def['nivel'] ) {")


def m_mae_diverge_do_documento(raiz):
    """O ARVORE.md muda de mae e o codigo fica como esta — divergencia em silencio."""
    trocar(raiz, ARVORE,
           "| `/materiais/como-sabemos/` | 2 | `/materiais/` | Início › Materiais › Como sabemos |",
           "| `/materiais/como-sabemos/` | 2 | `/loja/` | Início › Loja › Como sabemos |")


def m_nivel_diverge_do_documento(raiz):
    """O documento promove /loja/ a nivel 2 e o codigo continua achando que e 1."""
    trocar(raiz, ARVORE,
           "| `/loja/` | 1 | home | Início › Loja |",
           "| `/loja/` | 2 | home | Início › Loja |")


def m_slug_de_categoria_foge_da_voz(raiz):
    """O registro do Guia volta ao slug que o VOZ.md nao nomeia.

    E a divergencia REAL que este bloco achou: 'materiais/colas' de um lado,
    'colas-e-adesivos' do outro, e nada cobrando os dois juntos.
    """
    trocar(raiz, CASCA,
           "'slug'     => 'materiais/colas-e-adesivos',",
           "'slug'     => 'materiais/colas',")
    # A CONTAGEM DE ITENS NAO ENTRA NA BUSCA, e isto e conserto de 14/09/2026 as
    # 23h: a linha estava escrita inteira aqui, com "5 itens", e o banco cresceu
    # para 7 — entao a mutacao parou de achar o alvo e esta trava ficou INERTE,
    # sem reprovar nada e sem acusar nada. Mutacao amarrada a um numero que o
    # banco move envelhece calada, que e a mesma familia da bateria do publicador
    # da Robometria. Agora o alvo e so o endereco.
    texto = ler(raiz, ARVORE)
    alvo = [l for l in texto.splitlines() if "`/materiais/colas-e-adesivos/`" in l and l.startswith("|")]
    if not alvo:
        raise AssertionError("mutacao nao achou a linha da categoria colas no ARVORE.md")
    trocar(raiz, ARVORE, alvo[0], alvo[0].replace("/materiais/colas-e-adesivos/", "/materiais/colas/"))


def m_pagina_publicada_sem_lugar_na_arvore(raiz):
    """Uma pagina sai do mapa: continua publicada e passa a nao ter trilha."""
    trocar(raiz, CASCA,
           "\t\t'contato'                 => array( 'nivel' => 0, 'mae' => '', 'rotulo' => 'Contato' ),\n",
           "")


def m_quarto_nivel(raiz):
    """A 16.1 para no nivel 3. Aqui nasce um quarto."""
    trocar(raiz, CASCA,
           "'materiais/como-sabemos'  => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),",
           "'materiais/como-sabemos'  => array( 'nivel' => 4, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),")


def m_mae_em_circulo(raiz):
    """/materiais/ passa a ser filha da propria filha."""
    trocar(raiz, CASCA,
           "'materiais'               => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Materiais' ),",
           "'materiais'               => array( 'nivel' => 1, 'mae' => 'materiais/como-sabemos', 'rotulo' => 'Materiais' ),")


def m_cartao_volta_a_contar_o_banco(raiz):
    """O cartao 'em breve' volta a publicar a contagem — o que a 16.5 proibe."""
    trocar(raiz, CASCA,
           "\t\t\t$html .= '<span class=\"cdm-tag\">Em breve</span>';",
           "\t\t\t$html .= '<span class=\"cdm-tag\">' . esc_html( $c['no_banco'] . ' no banco, ficha em construção' ) . '</span>';")


def m_cartao_de_categoria_vira_link(raiz):
    """O cartao vira link para a categoria que ainda nao existe (16.5)."""
    trocar(raiz, CASCA,
           "\t\t$url = cdm_casca_url_se_existir( $c['slug'] );\n\t\tif ( '' !== $url ) {\n\t\t\t$html .= '<a href=\"' . esc_url( $url ) . '\">Abrir a ficha</a>';",
           "\t\t$url = cdm_casca_url_se_existir( $c['slug'] );\n\t\tif ( true ) {\n\t\t\t$html .= '<a href=\"' . esc_url( home_url( '/' . $c['slug'] . '/' ) ) . '\">Abrir a ficha</a>';")


def m_dois_slugs_com_o_mesmo_ultimo_nivel(raiz):
    """Duas paginas terminando no mesmo slug — o caminho remontado vira loteria.

    ESTA MUTACAO FICOU INERTE E O ACHADO E DO MESMO DIA (28/09/2026). Ela casava
    com a entrada `'sobre'` escrita em UMA linha, e a casca 1.16.0 — de algumas
    horas antes, quando a `description` ganhou dono — quebrou a entrada em
    varias linhas. A mutacao parou de achar o alvo e passou a se declarar
    INVALIDA, que a bancada ja conta como "passou": a trava dos slugs repetidos
    ficou sem ninguem a vendo, e e justamente a trava que sustenta a premissa do
    caminho remontado. E a mesma cicatriz que o comentario de
    `m_pagina_de_prova_deixa_de_ser_citada` registra logo abaixo, e ela voltou.

    Agora o alvo e a ABERTURA da entrada, que nao depende de quantos campos ela
    tem: a pagina nova entra antes dela.
    """
    texto = ler(raiz, CASCA)
    alvo = [l for l in texto.splitlines()
            if l.strip().startswith("'sobre'") and l.rstrip().endswith("=> array(")]
    if not alvo:
        raise AssertionError("a entrada 'sobre' da definicao de paginas mudou de forma")
    nova = ("\t\t'materiais/sobre'         => array( 'titulo' => 'Sobre os materiais', "
            "'conteudo' => '[cdm_sobre]', 'pai' => 'materiais' ),\n")
    trocar(raiz, CASCA, alvo[0] + "\n", nova + alvo[0] + "\n")


def m_pagina_de_prova_deixa_de_ser_citada(raiz):
    """A pagina fora do sitemap perde a unica citacao que tinha.

    'Fora do sitemap' nao pode virar porta dos fundos para publicar pagina que
    ninguem linka — por isso a trava cobra a citacao dela tambem.
    """
    # A MUTACAO PRECISOU SER REESCRITA EM 12/09/2026, e o motivo e o resultado:
    # ela trocava a citacao SO NA CASCA, e parou de morder no dia em que as duas
    # ferramentas passaram a citar a mesma pagina na camada de prova delas. A
    # afirmacao continuava certa (a pagina seguia citada, por outras duas), e era
    # a mutacao que tinha envelhecido. Agora ela apaga a citacao das TRES fontes,
    # que e o estado que a trava existe para impedir: pagina fora do sitemap sem
    # nenhum link interno some do site sem ninguem perceber.
    apagou = 0
    for arquivo in (CASCA,
                    os.path.join("snippets", "clubedomosaico-f2.php"),
                    os.path.join("snippets", "clubedomosaico-f1.php")):
        caminho = os.path.join(raiz, arquivo)
        with open(caminho, encoding="utf-8") as fh:
            texto = fh.read()
        alvo = "cdm_casca_link_html( 'materiais/como-sabemos', 'Como sabemos' )"
        if alvo not in texto:
            continue
        apagou += texto.count(alvo)
        with open(caminho, "w", encoding="utf-8") as fh:
            fh.write(texto.replace(alvo, "esc_html( 'Como sabemos' )"))
    if apagou < 3:
        raise AssertionError(
            "mutacao INERTE: achei %d citacoes de Como sabemos, esperava 3 ou mais" % apagou)


def m_chave_de_remontagem_volta_a_ser_a_versao(raiz):
    """A chave de remontagem da estrutura volta a ser a VERSAO da casca.

    E o defeito de 12/09/2026, escrito de volta: com ele, pagina nova entra na
    definicao, a versao da casca continua a mesma e a pagina nunca nasce no
    site. A F1 respondeu 404 no ar depois de um Sync que disse revisao 10 e
    aplicou seis itens com sucesso. Mutacao barata de escrever e cara de
    descobrir — nenhuma pagina do site muda, e o defeito so aparece no dia em
    que a proxima ferramenta nascer.
    """
    trocar(raiz, CASCA,
           "	return CDM_CASCA_VERSAO . ':' . md5( (string) wp_json_encode( $mapa ) );",
           "	return CDM_CASCA_VERSAO;")


def m_provedor_de_autor_volta_ao_sitemap(raiz):
    """O provedor `users` volta ao sitemap.

    Defeito MEDIDO no ar em 14/09/2026, e ele nasceu sozinho: o provedor so lista
    autor que TEM conteudo publicado, e ate 13/09 esta ilha nao tinha peca nenhuma.
    No minuto em que a artesa publicou a primeira, /author/artesa/ entrou no
    wp-sitemap.xml — pagina fina que repete a /loja/, e um endereco que confirma o
    login dela. Nenhuma linha de codigo mudou para isso acontecer, e e por isso que
    so uma regua pega.
    """
    trocar(raiz, CASCA,
           "\treturn ( 'users' === $nome ) ? false : $provedor;",
           "\treturn $provedor;")


def m_peca_volta_a_ser_chaveada_pelo_slug_nu(raiz):
    """O defeito de origem, de volta: o filtro da Loja escreve o slug nu.

    E a mutacao que mais vale desta leva, porque e exatamente o estado em que a
    ilha ficou quatorze dias sem nenhum portao acusar: NA TELA A TRILHA SAI
    IGUAL, porque quem pede passa o mesmo slug nu. So separando as duas pontas
    o portao ve.
    """
    trocar(raiz, LOJA,
           "\treturn ( '' === $slug ) ? '' : CDM_LOJA_BASE . '/' . $slug;",
           "\treturn $slug;")


def m_so_a_chave_vira_caminho(raiz):
    """Uma ponta so muda de formato e a outra nao — a trilha da peca SOME.

    Este e o desfecho que a funcao unica existe para impedir, e ele nao tem cor
    na tela: a peca simplesmente deixa de ter trilha.
    """
    trocar(raiz, LOJA,
           "\tif ( '' !== (string) $caminho ) {\n\t\treturn $caminho; // outro dono já respondeu; o primeiro a falar manda\n\t}\n\t$peca = cdm_loja_e_peca();",
           "\tif ( '' !== (string) $caminho ) {\n\t\treturn $caminho;\n\t}\n\treturn $caminho;\n\t$peca = cdm_loja_e_peca();")


def m_o_filtro_fala_depois_do_laco(raiz):
    """A ordem invertida na casca — e a colisao volta, so ela.

    A primeira escrita do conserto de 28/09 errou exatamente aqui: com o filtro
    depois do laco das paginas, a peca chamada `sobre` casa com a pagina /sobre/
    e nunca chega a declarar o caminho dela. O caso comum continua verde, e por
    isso a mutacao precisa existir.
    """
    texto = ler(raiz, CASCA)
    declara = ("\t$declarado = trim( (string) apply_filters( 'cdm_caminho_atual', '', $post ), '/' );\n"
               "\tif ( '' !== $declarado ) {\n\t\treturn $declarado;\n\t}\n\n")
    laco = ("\tforeach ( cdm_casca_definicao_paginas() as $caminho => $def ) {\n"
            "\t\tif ( cdm_casca_slug_final( $caminho ) === $nome ) {\n"
            "\t\t\treturn $caminho;\n\t\t}\n\t}\n")
    if declara not in texto or laco not in texto:
        raise AssertionError("a ordem do filtro e do laco mudou de forma")
    texto = texto.replace(declara, "").replace(laco, laco + "\n" + declara)
    gravar(raiz, CASCA, texto)


def m_tabela_nomeia_peca_que_nao_existe(raiz):
    """A linha da peca troca por um slug que nao esta na copia da secao 24.

    Sem a perna documento -> realidade o portao passaria: a bancada fabrica a
    peca com o slug que a tabela pedir, entao qualquer nome inventado casaria
    com o codigo.
    """
    trocar(raiz, ARVORE,
           "| `/loja/quadro-flores-do-campo/` | 2 | `/loja/` |",
           "| `/loja/vaso-que-nunca-existiu/` | 2 | `/loja/` |")


def m_peca_muda_de_mae_no_documento(raiz):
    """O documento pendura a peca em /materiais/ e o codigo continua em /loja/."""
    trocar(raiz, ARVORE,
           "| `/loja/quadro-flores-do-campo/` | 2 | `/loja/` | Início › Loja › Quadro flores do campo |",
           "| `/loja/quadro-flores-do-campo/` | 2 | `/materiais/` | Início › Materiais › Quadro flores do campo |")


def m_peca_some_da_tabela(raiz):
    """A linha da peca sai do ARVORE.md — o estado de antes de 28/09/2026.

    Ela reprova pelo portao que a propria linha trouxe: a unica pagina desta
    ilha publicada por uma pessoa volta a nao ter documento nenhum cobrando o
    codigo dela.
    """
    texto = ler(raiz, ARVORE)
    alvo = [l for l in texto.splitlines() if l.startswith("| `/loja/quadro-flores-do-campo/`")]
    if not alvo:
        raise AssertionError("a linha da peca nao esta na tabela")
    gravar(raiz, ARVORE, texto.replace(alvo[0] + "\n", ""))


def m_todas_as_pecas_entram_sempre(raiz):
    """O filtro declara a peca fora da requisicao dela.

    E o conserto preguicoso que encheria a lista de irmas de /loja/ de peca —
    outra decisao, e nao a que o snippet declara.
    """
    trocar(raiz, LOJA,
           "\t$peca = cdm_loja_e_peca();\n\tif ( ! $peca || ! is_array( $mapa ) ) {\n\t\treturn $mapa;\n\t}\n\t$caminho = cdm_loja_caminho_da_peca( $peca );",
           "\t$peca = cdm_loja_e_peca();\n\tif ( ! is_array( $mapa ) ) {\n\t\treturn $mapa;\n\t}\n\tif ( ! $peca ) {\n\t\t$peca = (object) array( 'post_name' => 'quadro-flores-do-campo', 'post_title' => 'Quadro flores do campo' );\n\t}\n\t$caminho = cdm_loja_caminho_da_peca( $peca );")


def m_uma_peca_da_copia_fica_de_fora(raiz):
    """O codigo passa a atender so a peca que a tabela nomeia.

    A perna realidade -> codigo e a que ve: sem ela, a tabela com uma linha
    seria alibi para as outras quatro.
    """
    trocar(raiz, LOJA,
           "\t$caminho = cdm_loja_caminho_da_peca( $peca );\n\tif ( '' === $caminho || isset( $mapa[ $caminho ] ) ) {",
           "\t$caminho = cdm_loja_caminho_da_peca( $peca );\n\tif ( 'quadro-flores-do-campo' !== (string) $peca->post_name ) {\n\t\treturn $mapa;\n\t}\n\tif ( '' === $caminho || isset( $mapa[ $caminho ] ) ) {")


MUTACOES = [
    ("a chave de remontagem volta a ser so a versao da casca", m_chave_de_remontagem_volta_a_ser_a_versao),
    ("a home ganha trilha (16.3)", m_home_ganha_trilha),
    ("a trilha sai ABAIXO do H1", m_trilha_depois_do_h1),
    ("a bancada volta a medir fora de ordem", m_bancada_mede_fora_de_ordem),
    ("degrau de trilha vira link morto", m_degrau_morto_na_trilha),
    ("schema 'mais completo' com degrau sem endereco", m_schema_leva_degrau_sem_endereco),
    ("teto de irmas sobe de 4 para 5", m_teto_de_irmas_vira_cinco),
    ("cluster publicado com uma irma so", m_cluster_com_uma_irma_so),
    ("irma escolhida fora da mae", m_irma_de_outra_mae),
    ("a pagina se lista como irma de si mesma", m_pagina_se_lista_como_irma),
    ("ARVORE.md e codigo divergem na mae", m_mae_diverge_do_documento),
    ("ARVORE.md e codigo divergem no nivel", m_nivel_diverge_do_documento),
    ("slug de categoria foge do VOZ.md", m_slug_de_categoria_foge_da_voz),
    ("pagina publicada sem lugar na arvore", m_pagina_publicada_sem_lugar_na_arvore),
    ("nasce um quarto nivel (16.1)", m_quarto_nivel),
    ("mae em circulo", m_mae_em_circulo),
    ("cartao 'em breve' volta a contar o banco (16.5)", m_cartao_volta_a_contar_o_banco),
    ("cartao vira link para categoria inexistente", m_cartao_de_categoria_vira_link),
    ("dois slugs com o mesmo ultimo nivel", m_dois_slugs_com_o_mesmo_ultimo_nivel),
    ("a pagina fora do sitemap perde a citacao", m_pagina_de_prova_deixa_de_ser_citada),
    ("o provedor de autor volta ao sitemap (/author/)", m_provedor_de_autor_volta_ao_sitemap),
    ("a peca volta a ser chaveada pelo slug nu", m_peca_volta_a_ser_chaveada_pelo_slug_nu),
    ("so a chave vira caminho e a outra ponta nao", m_so_a_chave_vira_caminho),
    ("o filtro do caminho fala DEPOIS do laco das paginas", m_o_filtro_fala_depois_do_laco),
    ("a tabela nomeia peca que nao esta na copia", m_tabela_nomeia_peca_que_nao_existe),
    ("ARVORE.md e codigo divergem na mae DA PECA", m_peca_muda_de_mae_no_documento),
    ("a linha da peca some da tabela", m_peca_some_da_tabela),
    ("toda peca entra no mapa, servida ou nao", m_todas_as_pecas_entram_sempre),
    ("so a peca da tabela e atendida; as outras quatro ficam de fora", m_uma_peca_da_copia_fica_de_fora),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-casca.php"), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A casca de verdade ja esta reprovada — conserte antes de mutar.")
        print(base_saida[-2000:])
        return 1
    print("casca intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-arv-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if linha.strip().startswith("FALHA"):
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-52s | %s" % (nome, primeira[:92]))
        except AssertionError as erro:
            passaram.append("%s (a mutacao nao conseguiu ser escrita: %s)" % (nome, erro))
            print("  MUTACAO INVALIDA: %s — %s" % (nome, erro))
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

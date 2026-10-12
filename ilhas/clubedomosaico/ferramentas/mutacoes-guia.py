#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra as paginas do GUIA de proposito, uma mutacao por vez, e exige que a
bancada reprove — ou, em tres casos, que ela APROVE um mundo que o banco de
hoje nao tem.

    python3 ferramentas/mutacoes-guia.py

POR QUE ESTE ARQUIVO EXISTE. `teste-guia.php` nasceu junto com as quatro
paginas, e regua que nasce junto com o codigo que ela mede e a situacao em que
ninguem ainda viu a regua FALHAR. Verde de primeira nao e elogio: e o estado em
que tanto faz se o portao mede alguma coisa (secao 8 do ARQUIPELAGO.md). Cada
mutacao abaixo e uma forma plausivel de uma destas paginas ficar errada em
silencio.

AS MUTACOES DE ESTRUTURA (08/10/2026, snippet 1.2.0). O Guia deixou de ser de
uma categoria so, e com isso nasceram formas novas de ele ficar errado em
silencio: a categoria que publica sem regua, o banco de uma categoria apontando
para o arquivo de outra, e a regua com um papel faltando. As tres estao abaixo,
e a terceira nao reprova — ela tem de ficar HONESTA, que e a falha fechada que
a 1.2.0 existe para garantir.

E UMA DELAS NAO QUEBRA NADA, de proposito: o `banco` da categoria e renomeado
junto com o arquivo e o id do manifest, e a pagina tem de sair IDENTICA, byte a
byte. E a prova de que o nome `materiais-acabamento` nao esta escrito em lugar
nenhum fora da declaracao — sem ela, "a categoria agora e declarada" seria uma
frase sobre o codigo e nao uma medicao dele.

OS TRES CASOS QUE NAO SAO "REPROVA":

  1. COM O BANCO DE ACABAMENTO FORA DO AR, a pagina TEM de dizer que nao mediu
     e NAO pode servir ficha de produto nenhuma. O teste sozinho nao mede isso
     — a bancada carrega as options na entrada do processo, entao a ausencia e
     outro MUNDO e nao outra afirmacao.

  2. SEM O SNIPPET DA F2, a pagina sai INTEIRA e diz que a lista de onde
     comprar esta fora do ar. O bloco de compra desta pagina e da F2 por
     decisao (uma escada de quatro degraus, um dono), e saida degradada que
     nunca foi produzida nasce errada sem poder falhar — foi exatamente isso
     que a F1 descobriu em 29/09/2026 nas duas vitrines dela.

  3. COM UM FABRICANTE NOMEANDO VIDRO, a frase da lacuna TEM de parar de dizer
     que ninguem nomeia vidro, e a pagina continua passando. Este e o ramo que
     o banco de hoje nao pisa: nenhum dos dez acabamentos nomeia vidro, entao a
     frase sai sempre igual e ninguem sabe se ela e derivada ou cravada. O
     mundo e fabricado aqui.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SNIPPET = "snippets/clubedomosaico-guia.php"

# A pagina usada para medir o HTML nos casos que nao passam pelo teste. O id
# esta escrito aqui de proposito — ler o registro do snippet faria a mutacao
# que mexe no registro medir a si mesma.
TAG_DA_MAE = "cdm_guia_acabamento"
TAG_DE_UMA_FILHA = "cdm_guia_impermeabilizante"


def ler(raiz, caminho):
    with open(os.path.join(raiz, caminho), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, caminho, texto):
    with open(os.path.join(raiz, caminho), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, caminho, velho, novo):
    texto = ler(raiz, caminho)
    if velho not in texto:
        raise AssertionError("mutacao nao achou o trecho em %s: %r" % (caminho, velho[:60]))
    gravar(raiz, caminho, texto.replace(velho, novo, 1))


def banco(raiz):
    return json.load(open(os.path.join(raiz, "dados", "materiais-acabamento.json"), encoding="utf-8"))


def gravar_banco(raiz, b):
    json.dump(b, open(os.path.join(raiz, "dados", "materiais-acabamento.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


# ------------------------------------------------------------------ mutacoes

def m_cobertura_cravada(raiz):
    """O numero da cobertura deixa de ser contado e passa a ser escrito. E a
    forma mais barata de a pagina mentir: ela continua com cara de medida, o
    denominador continua certo, e o numerador e uma lembranca de ontem."""
    trocar(raiz, SNIPPET,
           "\t\t'nomeadas'              => $nomeadas,",
           "\t\t'nomeadas'              => 13,")


def m_denominador_digitado(raiz):
    """As 15 superficies deixam de sair do vocabulario e viram um numero no
    codigo. No dia em que o esquema ganhar um valor, a pagina publica uma
    fracao com o denominador do mundo anterior — e ninguem ve, porque 15 e um
    numero plausivel."""
    trocar(raiz, SNIPPET,
           "\t$n_sup      = count( $sup['base'] ) + count( $sup['tessela'] );",
           "\t$n_sup      = 15;")
    e = json.load(open(os.path.join(raiz, "dados", "esquema-banco.json"), encoding="utf-8"))
    e["vocabularios"]["base"].append("ceramica_crua")
    json.dump(e, open(os.path.join(raiz, "dados", "esquema-banco.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


def m_relogio_empresta_o_intervalo(raiz):
    """O relogio passa a somar mesmo sem o intervalo entre demaos declarado,
    chutando 4 horas. E o erro que o proprio banco nomeia dentro do
    `quartzolit-fundo-selador`: emprestar demao de um produto a outro."""
    trocar(raiz, SNIPPET,
           "\tif ( ! is_numeric( $intervalo ) ) {\n\t\treturn null;\n\t}",
           "\tif ( ! is_numeric( $intervalo ) ) {\n\t\t$intervalo = 240;\n\t}")


def m_relogio_sem_a_linha_que_recusa(raiz):
    """O produto sem as tres parcelas deixa de receber a linha que diz por que
    nao ha conta. A pagina nao mente — ela fica MUDA, e silencio em tabela
    comparativa le-se como 'nao se aplica'."""
    trocar(raiz, SNIPPET,
           "\t} else {\n\t\t$html .= '<p class=\"cdm-guia-relogio cdm-guia-sem-conta\">O fabricante não declara as três partes da espera",
           "\t} elseif ( false ) {\n\t\t$html .= '<p class=\"cdm-guia-relogio cdm-guia-sem-conta\">O fabricante não declara as três partes da espera")


def m_um_produto_some_da_mae(raiz):
    """A mae deixa de mostrar um dos dez. A prestacao de contas da secao 7 diz
    que cada item da categoria consultada aparece exatamente uma vez — ou na
    frase que o recomenda, ou numa linha que diz por que ele nao esta."""
    trocar(raiz, SNIPPET,
           "\t\t\tforeach ( $cf['itens'] as $chave ) {\n\t\t\t\t$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ], $cat );",
           "\t\t\tforeach ( array_slice( $cf['itens'], 1 ) as $chave ) {\n\t\t\t\t$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ], $cat );")


def m_ancora_vira_saiba_mais(raiz):
    """A mae passa a linkar as filhas com o nome curto em vez da consulta-alvo.
    A 16.4(a) proibe isso com todas as letras — o texto-ancora e o que diz ao
    buscador do que a filha trata, e 'Selador' nao e o que ninguem digita."""
    trocar(raiz, SNIPPET,
           "\t\t\t$html .= '<li><h3>' . cdm_casca_link_html( $f['slug'], $f['consulta'] ) . '</h3>'",
           "\t\t\t$html .= '<li><h3>' . cdm_casca_link_html( $f['slug'], $f['curto'] ) . '</h3>'")


def m_filha_perde_a_frase_que_linka_a_mae(raiz):
    """A filha fica so com a trilha apontando para a mae. A 16.4(b) pede as
    duas — e a trilha sozinha passaria numa regua desatenta, que e justamente
    por que a afirmacao do teste apaga os `<nav>` antes de procurar."""
    trocar(raiz, SNIPPET,
           "\t\t$html .= '<p>Esta é uma das três etapas do '\n\t\t\t. cdm_casca_link_html( $mae['slug'], 'acabamento da peça de mosaico' )",
           "\t\t$html .= '<p>Esta é uma das três etapas do '\n\t\t\t. esc_html( 'acabamento da peça de mosaico' )")


def m_frase_da_lacuna_cravada(raiz):
    """A frase que diz o que falta deixa de ser derivada e passa a ser uma
    lista escrita. Ela continua CERTA hoje — e e esse o ponto: ela so fica
    errada no dia em que um fabricante novo nomear vidro, e nesse dia ninguem
    vai estar olhando para esta linha."""
    trocar(raiz, SNIPPET,
           "\tforeach ( array( 'vidro', 'espelho' ) as $chave ) {\n\t\tif ( in_array( $chave, $lac['base'], true ) ) {\n\t\t\t$nomes[] = cdm_guia_rotulo( 'base', $chave );\n\t\t}\n\t}",
           "\t$nomes[] = 'vidro comum';")
    # e o mundo em que ela fica errada: um fabricante passa a nomear vidro.
    b = banco(raiz)
    for m in b["materiais"]:
        if m["id"] == "coral-resina-acrilica":
            m["protecao"]["bases_do_vocabulario_que_a_frase_nomeia"].append("vidro")
            m["protecao"]["bases_do_vocabulario_que_a_frase_NAO_nomeia"].remove("vidro")
    gravar_banco(raiz, b)


def m_busca_crua_vira_patrocinada(raiz):
    """O link que NAO rende comissao passa a se declarar patrocinado. Nao e
    detalhe de atributo: e mentir ao leitor sobre a unica coisa que ele tem o
    direito de saber sobre nos. A trava mora na F2, que e a dona da escada, e
    esta mutacao prova que ela alcanca a ficha do Guia tambem."""
    b = banco(raiz)
    for m in b["materiais"]:
        m["afiliado"]["url"] = ""
        m["afiliado"]["url_busca"] = ""
    gravar_banco(raiz, b)
    trocar(raiz, "snippets/clubedomosaico-f2.php",
           "rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';",
           "rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';")


def m_uma_pagina_a_mais_sem_autorizacao(raiz):
    """Nasce uma quinta pagina, de um recorte que o cruzamento da 14.9 NAO
    autoriza. E a forma mais provavel de esta familia crescer errado: o banco
    tem itens, o recorte parece pronto, e ninguem abre o veredito."""
    trocar(raiz, SNIPPET,
           "\t\t'selador' => array(\n\t\t\t'papel'    => 'filha',",
           "\t\t'pastilha_vidro' => array(\n"
           "\t\t\t'papel'    => 'filha',\n"
           "\t\t\t'tipo'     => 'pastilha_vidro',\n"
           "\t\t\t'propriedade' => null,\n"
           "\t\t\t'recorte'  => 'acabamento/pastilha_vidro',\n"
           # A CATEGORIA ENTRA CERTA DE PROPOSITO: sem ela a pagina reprovaria
           # pelo portao da declaracao (1-b) e nao pelo do cruzamento, que e o
           # que esta mutacao quer medir. Mutacao que reprova pelo motivo errado
           # mede a regua errada e ninguem percebe.
           "\t\t\t'categoria' => 'acabamento',\n"
           "\t\t\t'slug'     => 'materiais/acabamento/pastilhas-de-vidro',\n"
           "\t\t\t'titulo'   => 'Pastilhas de vidro para mosaico',\n"
           "\t\t\t'curto'    => 'Pastilhas',\n"
           "\t\t\t'consulta' => 'pastilhas de vidro para mosaico',\n"
           "\t\t\t'resumo'   => 'As pastilhas de vidro do banco.',\n"
           "\t\t\t'linha_mestra' => 'As pastilhas de vidro do banco desta ilha.',\n"
           "\t\t\t'description'  => 'Pastilhas de vidro para mosaico: o que cada fabricante declara sobre o produto, com a frase dele e a data da leitura aqui.',\n"
           "\t\t\t'o_que_e'  => 'Pastilha de vidro e a tessela mais comum do mosaico.',\n"
           "\t\t\t'o_que_nao_e' => 'O que ela nao e: caco de espelho.',\n"
           "\t\t\t'faq_propria' => array(),\n"
           "\t\t),\n"
           "\t\t'selador' => array(\n\t\t\t'papel'    => 'filha',")


def m_pergunta_se_declara_mae(raiz):
    """A filha em forma de PERGUNTA passa a se declarar `mae`. E o defeito que o
    campo `papel` existe para impedir, e ele nao da erro de PHP nenhum: a pagina
    vira a segunda mae do `acabamento`, pendura em /materiais/ em vez da mae,
    sai da arvore de nivel 3 e passa a listar as irmas como se fosse indice de
    categoria. Ate 12/10/2026 a resposta de `e mae?` era `tipo === null`, e por
    ela esta pagina JA era mae."""
    trocar(raiz, SNIPPET,
           "\t\t'demaos' => array(\n\t\t\t'papel'    => 'filha',",
           "\t\t'demaos' => array(\n\t\t\t'papel'    => 'mae',")


def m_pergunta_recorta_a_categoria_inteira(raiz):
    """A pergunta perde a `propriedade` e passa a recortar a categoria inteira —
    os dez produtos em vez dos cinco que declaram demao. E a pagina publicando
    uma faixa de demaos sobre um conjunto em que metade nao declara demao
    nenhuma, que e a invencao mais barata desta familia."""
    trocar(raiz, SNIPPET,
           "\t\t\t'propriedade' => 'demaos_minimas',",
           "\t\t\t'propriedade' => null,")


def m_recorte_da_pergunta_ignora_a_fonte(raiz):
    """O recorte da pergunta passa a aceitar valor SEM `fonte_id`. O numero vai a
    tela sem procedencia e as duas metades divergem calado: o portao de dado em
    Python conta `propriedades_com_lastro` e o PHP contaria so `valor`."""
    trocar(raiz, SNIPPET,
           "\t\tif ( null !== $prop && null === cdm_guia_valor( $m, $prop ) ) {",
           "\t\tif ( null !== $prop && ! isset( $m['propriedades'][ $prop ] ) ) {")


def m_a_mae_agrupa_a_pergunta_junto(raiz):
    """A prestacao de contas da mae volta a agrupar TODAS as filhas, pergunta
    inclusive — e os cinco produtos que declaram demao aparecem duas vezes na
    mesma pagina. E o estado anterior a 12/10/2026, quando `cdm_guia_filhas()`
    era a unica lista que existia."""
    trocar(raiz, SNIPPET,
           "\t\tforeach ( cdm_guia_filhas_de_tipo( $cat ) as $fid => $f ) {",
           "\t\tforeach ( cdm_guia_filhas( $cat ) as $fid => $f ) {")


def m_minimo_acima_de_uma_volta_a_ser_somado(raiz):
    """`demaos_min_acima_de_uma` volta a ser `minimo + 1`, que foi a primeira
    versao desta regua em 12/10/2026. Ela ACERTA no banco de hoje, porque existe
    um produto de uma demao — e e exatamente por isso que a mutacao importa: ela
    produz o mundo em que a conta erra, apagando a demao unica do banco, e mede
    se a bancada o enxerga."""
    trocar(raiz, SNIPPET,
           "\t\t'demaos_min_acima_de_uma' => $mais_de_uma ? min( $mais_de_uma ) : null,",
           "\t\t'demaos_min_acima_de_uma' => $demaos ? min( $demaos ) + 1 : null,")
    # E O MUNDO QUE FAZ A CONTA ERRAR: sem nenhum produto de UMA demao, o
    # `minimo + 1` passa a mentir. Com o banco de hoje as duas formulas
    # coincidem, e mutacao que nao muda resultado nao mede nada.
    banco = "dados/materiais-acabamento.json"
    import json as _json
    d = _json.loads(ler(raiz, banco))
    for m in d["materiais"]:
        p = (m.get("propriedades") or {}).get("demaos_minimas")
        if p and p.get("valor") == 1:
            p["valor"] = 2
            p["declarado_como"] = "2 demaos"
    gravar(raiz, banco, _json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def m_uma_filha_some_do_registro(raiz):
    """Uma filha autorizada pelo cruzamento deixa de ter pagina. E o estado em
    que esta ilha passou quatro execucoes com o 4c: o recorte estava pronto e
    ninguem publicou. A trava e a SEGUNDA direcao da afirmacao do cruzamento,
    e e ela que faz a familia nao parar calada."""
    texto = ler(raiz, SNIPPET)
    ini = texto.index("\t\t'verniz' => array(")
    fim = texto.index("\t\t'impermeabilizante' => array(")
    gravar(raiz, SNIPPET, texto[:ini] + texto[fim:])


def m_categoria_nova_sem_regua(raiz):
    """Uma segunda categoria e DECLARADA e nao tem regua. E o caminho mais curto
    para a segunda mae do Guia: alguem aponta o banco do rejunte e espera que o
    resto saia por conta. Sem portao, a declaracao sozinha nao quebra nada hoje
    — e no dia em que a primeira pagina dela nascer, ela sai servindo numero
    nenhum ou o numero da vizinha."""
    trocar(raiz, SNIPPET,
           "\t\t'acabamento' => array(\n\t\t\t'banco' => 'materiais-acabamento',\n\t\t\t'regua' => 'acabamento',\n\t\t),",
           "\t\t'acabamento' => array(\n\t\t\t'banco' => 'materiais-acabamento',\n\t\t\t'regua' => 'acabamento',\n\t\t),\n"
           "\t\t'rejunte' => array(\n\t\t\t'banco' => 'materiais-rejuntes',\n\t\t\t'regua' => 'rejunte',\n\t\t),")


def m_banco_da_categoria_trocado(raiz):
    """A categoria `acabamento` passa a declarar o banco do REJUNTE. E a troca
    que as duas metades leriam juntas: a pagina e a bancada pegam o id da mesma
    declaracao, contam o mesmo arquivo errado e concordam. Quem acusa e a lista
    de itens do cruzamento, que varre os `materiais-*.json` e rotula pela
    categoria do esquema — um terceiro caminho."""
    trocar(raiz, SNIPPET,
           "\t\t\t'banco' => 'materiais-acabamento',",
           "\t\t\t'banco' => 'materiais-rejuntes',")


def m_regua_sem_um_papel(raiz):
    """A regua perde UM dos seis papeis — o `achado`, que e o bloco do que
    nenhum fabricante diz.

    ESTA NAO REPROVA POR REPROVAR: o que se exige e a pagina HONESTA. Meia regua
    serviria a pagina com um buraco no meio, e buraco em pagina de tabela le-se
    como "nao se aplica". A pagina tem de dizer que nao mediu e nao servir ficha
    nenhuma, igual ao banco fora do ar — um nivel acima, porque la falta o dado
    e aqui falta quem saiba conta-lo."""
    trocar(raiz, SNIPPET,
           "\t\t\t'achado'   => 'cdm_guia_achado_do_acabamento',\n",
           "")


def m_banco_renomeado(raiz):
    """O arquivo do banco, o id do manifest e a declaracao da categoria mudam de
    nome JUNTOS, de `materiais-acabamento` para `materiais-protecao`.

    NADA PODE MUDAR NA TELA. E a unica mutacao deste arquivo que mede uma
    afirmacao sobre o CODIGO e nao sobre o dado: se o nome antigo estiver escrito
    em qualquer lugar fora da declaracao — na option, nas contas, na bancada —
    a pagina sai diferente ou vazia, e a comparacao byte a byte acusa."""
    velho = os.path.join(raiz, "dados", "materiais-acabamento.json")
    novo = os.path.join(raiz, "dados", "materiais-protecao.json")
    shutil.move(velho, novo)

    p = os.path.join(raiz, "manifest.json")
    m = json.load(open(p, encoding="utf-8"))
    for d in m["dados"]:
        if d["id"] == "materiais-acabamento":
            d["id"] = "materiais-protecao"
            d["arquivo"] = "dados/materiais-protecao.json"
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    trocar(raiz, SNIPPET,
           "\t\t\t'banco' => 'materiais-acabamento',",
           "\t\t\t'banco' => 'materiais-protecao',")


def m_banco_fora_do_ar(raiz):
    """O item do manifest volta a `publicar: false` e a option some do site.

    ESTA NAO REPROVA POR REPROVAR: o que se exige e a pagina HONESTA. Ela tem
    de dizer que nao mediu e NAO pode servir ficha de produto — inventar aqui
    seria publicar recomendacao de acabamento sem banco.
    """
    p = os.path.join(raiz, "manifest.json")
    m = json.load(open(p, encoding="utf-8"))
    for d in m["dados"]:
        if d["id"] == "materiais-acabamento":
            d["publicar"] = False
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def m_sem_o_snippet_da_f2(raiz):
    """A F2 sai do ar. A pagina tem de sair INTEIRA, com os produtos e os
    numeros, dizendo que a lista de onde comprar e que esta fora."""
    os.remove(os.path.join(raiz, "snippets", "clubedomosaico-f2.php"))


def m_um_fabricante_passa_a_nomear_vidro(raiz):
    """O mundo em que a lacuna encolhe. A pagina tem de PASSAR e a frase tem de
    parar de dizer que ninguem nomeia vidro comum."""
    b = banco(raiz)
    for m in b["materiais"]:
        if m["id"] == "coral-resina-acrilica":
            m["protecao"]["bases_do_vocabulario_que_a_frase_nomeia"].append("vidro")
            m["protecao"]["bases_do_vocabulario_que_a_frase_NAO_nomeia"].remove("vidro")
    gravar_banco(raiz, b)


# AS QUATRO DO MECANISMO PLURAL (12/10/2026, snippet 1.4.0). A 1.3.0 saiu de
# manha com UMA filha-pergunta, e nela "a pergunta" e "a pergunta das demaos"
# eram a mesma coisa: a resposta e a ponte decidiam por `'pergunta' === $forma`.
# Com a SEGUNDA pergunta na mesma categoria aquele ramo passou a estar errado de
# quatro jeitos diferentes, e cada um deles tem mutacao aqui. Nenhuma delas e
# hipotetica: as quatro sao erros que a execucao de 12/10 cometeu ou quase
# cometeu antes de a bancada acusar.

def m_a_resposta_da_pergunta_volta_a_ser_singular(raiz):
    """O despacho por propriedade sai da resposta, e TODA pagina-pergunta volta
    a responder demaos. E literalmente o estado da 1.3.0, e e o defeito que a
    bancada pegou primeiro nesta execucao: a pagina da diluicao servia a frase
    das demaos, com os numeros das demaos, sob um titulo que pergunta de
    diluicao."""
    trocar(raiz, SNIPPET,
           "\t} elseif ( 'pergunta' === $forma && 'diluicao' === $c['recorte_propriedade'] ) {",
           "\t} elseif ( false ) {")


def m_a_ponte_crava_as_tres_etapas(raiz):
    """A ponte volta a dizer "as tres etapas" com a palavra digitada, que era o
    texto da 1.3.0. A pergunta da diluicao atravessa DUAS (verniz e selador), e
    a frase cravada afirma na tela uma cobertura que o recorte nao tem — a
    familia do "denominador digitado" que a primeira mutacao deste arquivo ja
    mede num outro lugar."""
    trocar(raiz, SNIPPET,
           "\t\t$quantas = ( 3 === $n_tipos ) ? 'as três etapas' : ( ( 2 === $n_tipos ) ? 'duas das três etapas' : 'as etapas' );",
           "\t\t$quantas = 'as três etapas';")


def m_a_resposta_classifica_o_solvente(raiz):
    """A frase de resposta passa a dizer QUAL e agua e QUAL e thinner. A 26.3
    proibe a tela dizer que o fabricante classificou, e aqui quem classificaria
    e a gente: as tres frases do banco nao dizem "base de agua" nem "base de
    solvente", dizem o que dizem. E a mutacao mais importante das quatro, porque
    o texto sairia plausivel e util — e trocar agua por thinner estraga a peca."""
    trocar(raiz, SNIPPET,
           "\t\t\t. 'um manda aplicar como vem, e os outros mandam diluir em coisas distintas. '",
           "\t\t\t. 'um manda aplicar como vem, um e base de água e o outro pede thinner. '")


def m_o_denominador_da_diluicao_mede_o_recorte(raiz):
    """`fora_do_recorte` volta a ser `com_diluicao` contra o proprio recorte, que
    e o defeito que esta execucao escreveu e corrigiu antes de rodar: na pagina
    da diluicao o recorte E quem declara, entao "os outros N nao dizem nada" sai
    com N igual a ZERO. Ele passa em qualquer portao de tipo — zero e um inteiro
    valido — e so a LEITURA e falsa, o que o torna a familia de defeito mais
    barata de escrever e mais cara de achar."""
    trocar(raiz, SNIPPET,
           "\t\t\t. 'Os outros <strong>' . (int) $c['fora_do_recorte'] . '</strong> produtos desta etapa não dizem nada, '",
           "\t\t\t. 'Os outros <strong>' . ( (int) $c['n_itens'] - (int) $c['com_diluicao'] ) . '</strong> produtos desta etapa não dizem nada, '")


def m_a_resposta_do_pigmentado_cai_no_ramo_vizinho(raiz):
    """O despacho da TERCEIRA pergunta sai, e a pagina do pigmentado cai no ramo
    das demaos — que e o ramo final de `'pergunta' === $forma`. E o mesmo defeito
    que a 1.4.0 consertou para a segunda pergunta, agora no andar da terceira: a
    pagina serviria a frase das demaos, com os numeros das demaos, sob um titulo
    que pergunta se o produto deixa a peca esbranquicada. Esta mutacao existe
    porque o conserto da 1.4.0 e por GRANDEZA: ele protege a diluicao
    explicitamente e nao protege sozinho a que vier depois."""
    trocar(raiz, SNIPPET,
           "\t} elseif ( 'pergunta' === $forma && 'pigmentado' === $c['recorte_propriedade'] ) {",
           "\t} elseif ( false ) {")


def m_o_pigmentado_conta_o_complemento(raiz):
    """`pigmentados` passa a ser a SUBTRACAO, e a tela ganha a frase "nao
    pigmentados". E a mutacao mais importante das quatro, e ela nao muda NENHUM
    numero neste banco: com tres declaracoes e duas em `'sim'`, a subtracao da 1
    e a contagem estrita tambem daria 1 para o complemento. O que ela muda e o
    que a pagina AFIRMA — ela passa a chamar de nao pigmentado o produto que so
    nao disse `'sim'`. Num banco com um `parcialmente` ou um `pigmentavel` ela
    publicaria o contrario do que o fabricante declarou, e passaria em qualquer
    portao de numero, porque um inteiro valido sai dos dois lados."""
    trocar(raiz, SNIPPET,
           "\t\t\t. 'Saem <strong>' . (int) $c['pigmentos_distintos'] . ' respostas diferentes</strong> no total, '",
           "\t\t\t. 'e os outros <strong>' . ( (int) $c['com_pigmento'] - (int) $c['pigmentados'] ) . '</strong> não pigmentados, '")


def m_o_pigmentado_promete_transparencia_de_quem_nao_declarou(raiz):
    """A frase que diz "nao dizer nada nao e dizer que e transparente" vira o
    contrario: os que nao declaram passam a ser servidos como transparentes.
    E a leitura que a SERP inteira faz e que esta pagina existe para desfazer —
    sete dos dez produtos desta etapa nao dizem nada, e servi-los como
    transparentes manda a artesa passar por cima de caquinho de vidro um produto
    sobre o qual ninguem afirmou nada."""
    trocar(raiz, SNIPPET,
           "\t\t\t. 'não dizem nada — e não dizer nada não é dizer que é transparente. ';",
           "\t\t\t. 'não dizem nada, então são transparentes. ';")


def m_o_denominador_do_pigmentado_mede_o_recorte(raiz):
    """`fora_do_recorte` vira a conta contra o proprio recorte, que na
    pagina-pergunta da ZERO. A mesma familia da mutacao da diluicao, repetida
    aqui de proposito: a trava e por PAGINA, nao por mecanismo, enquanto cada
    ramo escrever a sua frase."""
    trocar(raiz, SNIPPET,
           "\t\t\t. 'Os outros <strong>' . (int) $c['fora_do_recorte'] . '</strong> produtos desta etapa '",
           "\t\t\t. 'Os outros <strong>' . ( (int) $c['n_itens'] - (int) $c['com_pigmento'] ) . '</strong> produtos desta etapa '")


MUTACOES = [
    ("o numero da cobertura e cravado no codigo", m_cobertura_cravada, "reprova"),
    ("o denominador (15 superficies) e digitado", m_denominador_digitado, "reprova"),
    ("o relogio empresta o intervalo que falta", m_relogio_empresta_o_intervalo, "reprova"),
    ("o produto sem conta fica MUDO em vez de recusar", m_relogio_sem_a_linha_que_recusa, "reprova"),
    ("um dos dez produtos some da mae", m_um_produto_some_da_mae, "reprova"),
    ("a mae linka a filha com o nome curto, nao com a consulta", m_ancora_vira_saiba_mais, "reprova"),
    ("a filha perde a frase do corpo que linka a mae", m_filha_perde_a_frase_que_linka_a_mae, "reprova"),
    ("a frase da lacuna vira lista escrita a mao", m_frase_da_lacuna_cravada, "reprova"),
    ("a busca CRUA passa a se declarar patrocinada", m_busca_crua_vira_patrocinada, "reprova"),
    ("nasce uma pagina que o cruzamento NAO autoriza", m_uma_pagina_a_mais_sem_autorizacao, "reprova"),
    ("uma filha autorizada some do registro", m_uma_filha_some_do_registro, "reprova"),
    # AS CINCO DO MECANISMO DA FILHA EM FORMA DE PERGUNTA (12/10/2026). As
    # quatro primeiras matam o campo `papel` e o recorte por propriedade; a
    # quinta fabrica o mundo em que a conta `minimo + 1` erra.
    ("a pergunta se declara mae", m_pergunta_se_declara_mae, "reprova"),
    ("a pergunta recorta a categoria inteira", m_pergunta_recorta_a_categoria_inteira, "reprova"),
    ("o recorte da pergunta ignora a fonte do valor", m_recorte_da_pergunta_ignora_a_fonte, "reprova"),
    ("a mae agrupa a pergunta junto e repete cinco produtos", m_a_mae_agrupa_a_pergunta_junto, "reprova"),
    ("o minimo acima de uma demao volta a ser somado na frase", m_minimo_acima_de_uma_volta_a_ser_somado, "reprova"),
    ("uma segunda categoria e declarada sem regua", m_categoria_nova_sem_regua, "reprova"),
    ("o banco da categoria aponta para o arquivo de outra", m_banco_da_categoria_trocado, "reprova"),
    ("a regua perde um dos seis papeis", m_regua_sem_um_papel, "pagina-honesta"),
    ("o banco e renomeado junto com a declaracao", m_banco_renomeado, "mundo-identico"),
    ("o banco de acabamento sai do ar", m_banco_fora_do_ar, "pagina-honesta"),
    ("o snippet da F2 sai do ar", m_sem_o_snippet_da_f2, "pagina-sem-loja"),
    ("um fabricante passa a nomear vidro", m_um_fabricante_passa_a_nomear_vidro, "mundo-que-passa"),
    ("a resposta da pergunta volta a ser singular", m_a_resposta_da_pergunta_volta_a_ser_singular, "reprova"),
    ("a ponte crava as tres etapas onde sao duas", m_a_ponte_crava_as_tres_etapas, "reprova"),
    ("a resposta classifica o solvente pelo fabricante", m_a_resposta_classifica_o_solvente, "reprova"),
    ("o denominador da diluicao mede o recorte e da zero", m_o_denominador_da_diluicao_mede_o_recorte, "reprova"),
    # AS QUATRO DA TERCEIRA PERGUNTA (12/10/2026, 17h2xZ). A trava do ramo
    # vizinho e a do denominador sao irmas das da diluicao, e estao aqui
    # repetidas de proposito: enquanto cada grandeza escrever a sua frase, a
    # protecao e por PAGINA e nao por mecanismo. A do complemento e nova e e a
    # que mais vale: ela nao muda numero nenhum neste banco.
    ("a resposta do pigmentado cai no ramo vizinho", m_a_resposta_do_pigmentado_cai_no_ramo_vizinho, "reprova"),
    ("o pigmentado conta o complemento e chama de nao pigmentado", m_o_pigmentado_conta_o_complemento, "reprova"),
    ("o pigmentado promete transparencia de quem nao declarou", m_o_pigmentado_promete_transparencia_de_quem_nao_declarou, "reprova"),
    ("o denominador do pigmentado mede o recorte e da zero", m_o_denominador_do_pigmentado_mede_o_recorte, "reprova"),
]


def rodar(raiz, teste):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", teste), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def corpo_da_pagina(raiz, tag):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "render-para-teste.php"),
                        raiz, tag], capture_output=True, text=True)
    if r.returncode != 0:
        return ""
    m = re.search(r"<main\b[^>]*>(.*?)</main>", r.stdout, re.S)
    return m.group(1) if m else r.stdout


def main():
    rc, saida = rodar(ILHA, "teste-guia.php")
    if rc != 0:
        print("As paginas de verdade ja estao reprovadas — conserte antes de mutar.")
        print(saida[-2000:])
        return 1
    print("paginas intactas: APROVADAS (como tem que estar antes de comecar)\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-guia-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)

            if esperado == "pagina-honesta":
                corpo = corpo_da_pagina(copia, TAG_DA_MAE)
                honesta = "ainda não chegou ao site" in corpo
                sem_ficha = "cdm-guia-cartao" not in corpo
                if honesta and sem_ficha:
                    print("  ficou honesta como devia: %-50s | diz que nao mediu e NAO serve ficha" % nome)
                else:
                    erradas.append(nome + " (a pagina %s)" % (
                        "serviu ficha sem banco" if not sem_ficha else "nao disse que ficou sem medicao"))
                    print("  INVENTOU (a trava NAO viu): %s" % nome)
                continue

            if esperado == "pagina-sem-loja":
                corpo = corpo_da_pagina(copia, TAG_DE_UMA_FILHA)
                inteira = "cdm-guia-cartao" in corpo and "combinações de produto e superfície" in corpo
                avisa = "lista de onde comprar está fora do ar" in corpo
                sem_botao = "cdm-f2-compra" not in corpo
                if inteira and avisa and sem_botao:
                    print("  degradou como devia:      %-50s | pagina inteira, sem botao, com o aviso" % nome)
                else:
                    erradas.append(nome + " (inteira=%s avisa=%s sem_botao=%s)" % (inteira, avisa, sem_botao))
                    print("  DEGRADOU ERRADO: %s" % nome)
                continue

            if esperado == "mundo-identico":
                rc, saida = rodar(copia, "teste-guia.php")
                iguais = []
                for tag in (TAG_DA_MAE, TAG_DE_UMA_FILHA):
                    iguais.append(corpo_da_pagina(ILHA, tag) == corpo_da_pagina(copia, tag))
                if 0 == rc and all(iguais) and corpo_da_pagina(copia, TAG_DA_MAE):
                    print("  ficou identica como devia: %-47s | a bancada passa e o corpo e byte a byte o mesmo" % nome)
                else:
                    erradas.append(nome + " (rc=%d, corpos iguais=%s)" % (rc, iguais))
                    print("  MUDOU A TELA (o nome estava escrito fora da declaracao): %s" % nome)
                continue

            if esperado == "mundo-que-passa":
                rc, saida = rodar(copia, "teste-guia.php")
                corpo = corpo_da_pagina(copia, TAG_DE_UMA_FILHA)
                # SO A FRASE DA LACUNA. "vidro comum" aparece tambem na ficha do
                # produto que passou a nomear vidro — procurar no corpo inteiro
                # mediria o oposto do que esta mutacao quer saber.
                m = re.search(r"Entre o que ningu.m deste grupo nomeia est.(.*?)</p>", corpo, re.S)
                fala_de_vidro = bool(m) and "vidro comum" in m.group(1)
                if 0 == rc and not fala_de_vidro:
                    print("  passou como devia:        %-50s | a lacuna do vidro sumiu sozinha" % nome)
                else:
                    erradas.append(nome + " (rc=%d, ainda fala de vidro comum=%s)" % (rc, fala_de_vidro))
                    print("  NAO PASSOU (a frase da lacuna nao e derivada): %s" % nome)
                continue

            rc, saida = rodar(copia, "teste-guia.php")
            primeira = ""
            for linha in saida.splitlines():
                if linha.strip().startswith("FALHA"):
                    primeira = linha.strip()[5:].strip()
                    break
            if rc != 0:
                print("  reprovou como devia:      %-50s | %s" % (nome, primeira[:66]))
            else:
                erradas.append(nome + " (PASSOU e devia reprovar)")
                print("  PASSOU (a trava NAO viu): %s" % nome)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d decididas certo, %d erradas" %
          (len(MUTACOES), len(MUTACOES) - len(erradas), len(erradas)))
    if erradas:
        print("\nAS ERRADAS SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in erradas:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

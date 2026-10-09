#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra as paginas de consulta de produto de proposito, uma mutacao por vez, e
exige que `teste-produto.php` (ou o portao nomeado) REPROVE cada uma.

    python3 ferramentas/mutacoes-produto.py

Por que este arquivo existe: teste verde que nunca foi visto reprovar nao mediu
nada (secao 8 do ARQUIPELAGO.md). O `teste-produto.php` fechou com 288
afirmacoes e ZERO falha na primeira rodada inteira — o que e bom sinal e prova
nenhuma. Cada mutacao abaixo e uma forma PLAUSIVEL desta familia ficar errada em
silencio, e a maioria e um caractere trocado, do tipo que passa numa revisao.

A ARMADILHA QUE JA CUSTOU CARO EM TRES ILHAS: mutacao que nao acha o alvo no
arquivo e verde sem medir nada. Por isso `editar()` CONFERE que trocou alguma
coisa e explode se nao trocou. Mutacao que nao morde nao e mutacao.

ESTA BATERIA RODA EM `mkdtemp` E NAO PODE SUJAR A ARVORE — e isso nao e detalhe
de arrumacao. Em 09/10/2026 a `mutacoes-par.py`, que trabalha EM CIMA do
repositorio, foi morta por sinal no estagio do snippet e deixou
`clubedomosaico-f2.php` com a regra 8 movida para depois da regra 2, devolvendo
a frase errada; quem nomeou o arquivo foi o `git status`. Aqui a copia e inteira
e o original nunca e aberto para escrita.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET = os.path.join("snippets", "clubedomosaico-produto.php")
VITRINE = "vitrine-de-produto.json"
EDITORIAL = "paginas-de-produto.json"


def editar(raiz, arquivo, velho, novo, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    if texto.count(velho) < vezes:
        raise AssertionError(
            "mutacao INERTE: %r aparece %d vez(es) em %s, esperava %d"
            % (velho[:60], texto.count(velho), arquivo, vezes))
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, vezes))


def carregar(raiz, nome):
    with open(os.path.join(raiz, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


def gravar(raiz, nome, dado):
    with open(os.path.join(raiz, "dados", nome), "w", encoding="utf-8") as fh:
        json.dump(dado, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def pagina(dado, pid):
    """A pagina pelo ID, NOMEADA — nunca escolhida por posicao.

    Molde por posicao troca de pagina quando a ordem do arquivo muda, e o portao
    passa a medir outra coisa sem avisar.
    """
    for i, p in enumerate(dado["paginas"]):
        if p["id"] == pid:
            return i
    raise AssertionError("mutacao INERTE: nao achei a pagina %s" % pid)


# --------------------------------------------------------------- as mutacoes

def m01_numero_proprio_mentido(raiz):
    """A faixa publicada deixa de ser a das ofertas que a pagina serve.

    E a mutacao mais perigosa da familia: a tela fica bonita, o preco de cada
    oferta continua certo, e so o NUMERO QUE A PAGINA PUBLICA SOBRE SI MESMA
    esta errado. Quem a pega e a reconta do JSON cru.
    """
    d = carregar(raiz, VITRINE)
    i = pagina(d, "torques-para-mosaico")
    d["paginas"][i]["numero_proprio"]["ate"] = 999.0
    gravar(raiz, VITRINE, d)


def m02_piso_da_30_2_cai(raiz):
    """O piso de tres ofertas vira dois: a pagina de duas ofertas vai ao ar."""
    editar(raiz, SNIPPET, "function cdm_produto_piso() {\n\treturn 3;",
           "function cdm_produto_piso() {\n\treturn 2;")


def m03_oferta_recusada_entra(raiz):
    """Uma oferta que a regra RECUSOU entra na vitrine como se servisse.

    E a enxurrada desta familia voltando: na consulta do torques, catorze de
    vinte eram roda de reposicao. Se o gerador deixar passar, a pagina vende
    peca de reposicao a quem nao tem a ferramenta.
    """
    d = carregar(raiz, VITRINE)
    i = pagina(d, "torques-para-mosaico")
    molde = dict(d["paginas"][i]["ofertas"][0])
    molde["titulo"] = "Carboneto de Para Alicate de Telha 22 * 6 * 2mm Mosaico Substituir Corte"
    molde["item_id"] = 1
    d["paginas"][i]["ofertas"].append(molde)
    d["paginas"][i]["n_ofertas"] = len(d["paginas"][i]["ofertas"])
    gravar(raiz, VITRINE, d)


def m04_link_perde_o_sponsored(raiz):
    """O link de afiliado sai sem `rel="sponsored"` — secao 7 do contrato."""
    editar(raiz, SNIPPET, "rel=\"sponsored noopener\" target=\"_blank\">Ver na loja</a>",
           "rel=\"noopener\" target=\"_blank\">Ver na loja</a>")


def m05_resposta_depois_da_explicacao(raiz):
    """A resposta em duas frases desce para depois do "o que e, e o que nao e".

    O item 1 do despacho e a ORDEM: a pessoa recebe o que comprar e quanto custa
    antes de qualquer explicacao. Trocar a ordem nao quebra nada no PHP.
    """
    editar(raiz, SNIPPET,
           "\t$html .= '<div class=\"cdm-produto-resposta\">';",
           "\t$html .= '<div class=\"cdm-secao\"><h2>O que é, e o que não é</h2>'\n"
           "\t\t. '<p>' . cdm_produto_preencher( $p['o_que_e'], $p ) . '</p></div>';\n"
           "\t$html .= '<div class=\"cdm-produto-resposta\">';")


def m06_compra_depois_da_procedencia(raiz):
    """O bloco de compra desce para depois da procedencia.

    A secao 7 e o despacho pedem o contrario, com essas palavras: o link de
    compra vem ANTES da parte que mostra de onde veio a informacao.
    """
    editar(raiz, SNIPPET,
           "\t$html .= cdm_produto_malha_html( $id );",
           "\t$html .= cdm_produto_malha_html( $id );\n\t$GLOBALS['__desce_compra'] = 1;")
    editar(raiz, SNIPPET,
           "\t$html .= '<div class=\"cdm-secao cdm-prova cdm-produto-procedencia\"><h2>Como a gente sabe</h2>';",
           "\t$html = str_replace( '<td class=\"cdm-produto-compra\">', '<td class=\"cdm-produto-sem\">', $html );\n"
           "\t$html .= '<div class=\"cdm-secao cdm-prova cdm-produto-procedencia\"><h2>Como a gente sabe</h2>';\n"
           "\t$html .= '<a class=\"cdm-produto-botao\" href=\"https://s.shopee.com.br/x\" rel=\"sponsored noopener\">Ver na loja</a>';")


def m07_quantidade_adivinhada(raiz):
    """Oferta sem quantidade declarada passa a mostrar um numero.

    E o jeito barato de errar em dado comercial: o titulo diz "kit" e alguem
    chuta 100. A pagina tem de dizer "nao declara".
    """
    editar(raiz, SNIPPET,
           "\t\t$html .= '<span class=\"cdm-produto-nao-declara\">não declara</span>';",
           "\t\t$html .= '100';")


def m08_molde_nao_preenchido(raiz):
    """Um molde da prosa deixa de ser trocado e vai ao ar como `{MIN}`."""
    editar(raiz, SNIPPET, "'{MIN}'     => cdm_produto_moeda( $np['de'], $modo ),",
           "'{MIN}zzz'  => cdm_produto_moeda( $np['de'], $modo ),")


def m09_nbsp_no_json_ld(raiz):
    """O JSON-LD volta a receber o texto da TELA, com `&nbsp;` dentro.

    A maquina de busca leria "R$&nbsp;68,99" como o texto da resposta, e na tela
    as duas versoes saem identicas — nenhuma revisao humana ve a diferenca.
    """
    editar(raiz, SNIPPET,
           "'resposta'      => cdm_produto_preencher( $q['resposta'], $p, 'texto' ),",
           "'resposta'      => cdm_produto_preencher( $q['resposta'], $p, 'html' ),")


def m10_itemlist_perde_uma_oferta(raiz):
    """O ItemList publica menos ofertas do que a tela serve."""
    editar(raiz, SNIPPET, "\tforeach ( $p['ofertas'] as $i => $o ) {\n\t\t$itens[] = array(",
           "\tforeach ( array_slice( $p['ofertas'], 1 ) as $i => $o ) {\n\t\t$itens[] = array(")


def m11_preco_do_schema_divergente(raiz):
    """O preco do ItemList deixa de ser o da tela — dois precos, um endereco."""
    editar(raiz, SNIPPET, "'price'         => number_format( (float) $o['preco'], 2, '.', '' ),",
           "'price'         => number_format( (float) $o['preco'] * 0.9, 2, '.', '' ),")


def m12_url_do_schema_sem_rastreio(raiz):
    """O ItemList aponta para a ficha CRUA, e nao para o link que a pessoa clica."""
    editar(raiz, SNIPPET, "'url'           => $o['url_afiliado'],",
           "'url'           => 'https://shopee.com.br/product/1/2',")


def m13_nota_volta_para_a_tela(raiz):
    """A nota do vendedor volta a ser publicada, com `0` em mais da metade."""
    editar(raiz, SNIPPET,
           "\t\t$html .= '<span class=\"cdm-produto-loja\">' . esc_html( $o['loja'] ) . '</span>';",
           "\t\t$html .= '<span class=\"cdm-produto-loja\">' . esc_html( $o['loja'] )\n"
           "\t\t\t. ' · nota ' . esc_html( isset( $o['nota'] ) ? $o['nota'] : '0' ) . '</span>';")


def m14_mae_deixa_de_listar(raiz):
    """A mae para de listar as filhas: as oito viram orfas pela 16.4(f)."""
    editar(raiz, SNIPPET, "add_filter( 'cdm_materiais_secoes', function ( $html ) {",
           "add_filter( 'cdm_materiais_secoes', function ( $html ) {\n\treturn $html;")


def m15_irmas_somem(raiz):
    """O bloco das irmas desaparece: a malha entre as oito deixa de existir."""
    editar(raiz, SNIPPET, "\tif ( $irmas ) {", "\tif ( false ) {")


def m16_preco_digitado_na_prosa(raiz):
    """Um preco e DIGITADO na camada declarada, em vez de vir por molde.

    E o defeito mais silencioso possivel: hoje a frase esta certa, e na proxima
    coleta ela mente sozinha, sem ninguem editar nada.
    """
    d = carregar(raiz, EDITORIAL)
    i = pagina(d, "torques-para-mosaico")
    d["paginas"][i]["faq"][1]["resposta"] = "Hoje sai de R$ 68,99 a R$ 248,25 na Shopee."
    gravar(raiz, EDITORIAL, d)


def m17_sem_data_na_pagina(raiz):
    """O molde {DATA} deixa de ser preenchido: a resposta perde a data da coleta.

    A primeira versao desta mutacao PASSOU, e o motivo era uma lacuna de portao
    e nao dela: a bancada procurava a data em QUALQUER lugar do texto, e a
    procedencia imprime a data por fora do molde — entao a resposta podia perder
    a sua e o verde continuava. O portao passou a cobrar a data DENTRO da
    resposta, que e onde o despacho a pede ("o que comprar e quanto custa").
    """
    editar(raiz, SNIPPET, "'{DATA}'    => ( 'texto' === $modo ) ? $data : esc_html( $data ),",
           "'{DATA}'    => '',")


def m18_vitrine_editada_a_mao(raiz):
    """A vitrine e editada a mao e deixa de bater com o gerador.

    O arquivo e GERADO; quem o edita a mao perde a edicao na proxima coleta, e a
    pagina serve dado que nenhuma fonte sustenta.
    """
    d = carregar(raiz, VITRINE)
    i = pagina(d, "rejunte-para-mosaico")
    d["paginas"][i]["ofertas"][0]["titulo"] = "Rejunte bonito que eu inventei"
    gravar(raiz, VITRINE, d)


def m19_duas_paginas_a_mesma(raiz):
    """Duas paginas passam a servir a mesma `description`.

    Malha que nasce de um molde produz pagina fina sem ninguem decidir por isso.
    """
    d = carregar(raiz, EDITORIAL)
    i = pagina(d, "espelho-para-mosaico")
    j = pagina(d, "rejunte-para-mosaico")
    d["paginas"][i]["description"] = d["paginas"][j]["description"]
    gravar(raiz, EDITORIAL, d)


def m20_fonte_deixa_de_ser_dita(raiz):
    """A procedencia para de dizer de que loja o dado veio.

    AS TRES MENCOES CAEM JUNTAS, e as duas primeiras versoes desta mutacao
    PASSARAM por derrubar so uma e so duas: enquanto UMA sobrava, a pagina
    continuava nomeando a fonte e o verde estava certo. Mutacao tem de produzir
    o defeito inteiro que ela diz produzir, senao ela mede o portao errado — e
    "passou" viraria uma acusacao falsa contra uma trava que estava funcionando.
    """
    editar(raiz, SNIPPET, "<strong>Shopee</strong>", "<strong>a loja</strong>")
    editar(raiz, SNIPPET, "o catálogo inteiro da Shopee", "o catálogo inteiro da loja")
    editar(raiz, SNIPPET, "página diz Shopee, é Shopee", "página diz a loja, é a loja")


def m21_tres_frases_na_resposta(raiz):
    """A resposta ganha uma terceira frase: deixa de ser a resposta em DUAS."""
    d = carregar(raiz, EDITORIAL)
    i = pagina(d, "espelho-para-mosaico")
    d["paginas"][i]["resposta"].append("E tem mais uma coisa que a gente quer contar aqui.")
    gravar(raiz, EDITORIAL, d)


def m22_ordem_da_api_em_vez_do_preco(raiz):
    """As ofertas voltam a sair na ordem em que a API respondeu.

    A API devolve conjuntos diferentes entre chamadas — esta escrito no proprio
    arquivo de coleta. Ordem que muda sozinha faz a pagina mudar sem ninguem
    editar, e o leitor nao consegue comparar duas visitas.
    """
    editar(raiz, "ferramentas/gerar-vitrine-de-produto.py",
           "        ofertas.sort(key=lambda o: (float(o['preco']), int(o['item_id'])))",
           "        ofertas.reverse()")
    subprocess.run([sys.executable, os.path.join(raiz, "ferramentas/gerar-vitrine-de-produto.py"), raiz],
                   capture_output=True)


def m23_dado_fino_depois_da_tabela(raiz):
    """O aviso do rejunte desce para depois da tabela — aviso perdido.

    A pagina do rejunte DIZ "vale ler o aviso abaixo antes de olhar o preco". Se
    o aviso desce, a frase vira promessa quebrada no mesmo paragrafo.
    """
    editar(raiz, SNIPPET,
           "\tif ( ! empty( $p['dado_fino'] ) ) {\n\t\t$html .= '<p class=\"cdm-produto-fino\">",
           "\tif ( false ) {\n\t\t$html .= '<p class=\"cdm-produto-fino\">")


def m24_ancora_da_pinca_some(raiz):
    """A secao da pinca perde a ancora: a 30.4 deixa de ser cumprida."""
    editar(raiz, SNIPPET,
           "'<div class=\"cdm-secao\" id=\"' . esc_attr( $s['id'] ) . '\">'",
           "'<div class=\"cdm-secao\">'")


def m25_oferta_sem_link_vai_ao_ar(raiz):
    """Uma oferta sem link de afiliado entra na vitrine.

    A pagina publicaria um produto que ninguem consegue comprar por ela, e a
    comissao da ilha some junto.
    """
    d = carregar(raiz, VITRINE)
    i = pagina(d, "espelho-para-mosaico")
    d["paginas"][i]["ofertas"][0]["url_afiliado"] = ""
    gravar(raiz, VITRINE, d)


MUTACOES = [
    ("01 numero proprio mentido na tela", m01_numero_proprio_mentido),
    ("02 o piso de tres ofertas da 30.2 cai", m02_piso_da_30_2_cai),
    ("03 oferta RECUSADA pela regra entra na vitrine", m03_oferta_recusada_entra),
    ("04 link de afiliado sem rel=sponsored", m04_link_perde_o_sponsored),
    ("05 a resposta desce para depois da explicacao", m05_resposta_depois_da_explicacao),
    ("06 o bloco de compra desce para depois da procedencia", m06_compra_depois_da_procedencia),
    ("07 quantidade ADIVINHADA onde o anuncio nao declara", m07_quantidade_adivinhada),
    ("08 molde da prosa vai ao ar sem preencher", m08_molde_nao_preenchido),
    ("09 &nbsp; dentro do texto do JSON-LD", m09_nbsp_no_json_ld),
    ("10 o ItemList publica menos ofertas que a tela", m10_itemlist_perde_uma_oferta),
    ("11 o preco do schema diverge do da tela", m11_preco_do_schema_divergente),
    ("12 o schema aponta para a ficha crua, sem rastreio", m12_url_do_schema_sem_rastreio),
    ("13 a nota do vendedor volta para a tela", m13_nota_volta_para_a_tela),
    ("14 a mae deixa de listar as filhas (orfas pela 16.4f)", m14_mae_deixa_de_listar),
    ("15 o bloco das irmas desaparece", m15_irmas_somem),
    ("16 preco DIGITADO na camada declarada", m16_preco_digitado_na_prosa),
    ("17 a data da coleta sai da tela", m17_sem_data_na_pagina),
    ("18 a vitrine gerada e editada a mao", m18_vitrine_editada_a_mao),
    ("19 duas paginas com a MESMA description", m19_duas_paginas_a_mesma, "casca"),
    ("20 a pagina para de dizer que a fonte e a Shopee", m20_fonte_deixa_de_ser_dita),
    ("21 a resposta ganha uma TERCEIRA frase", m21_tres_frases_na_resposta),
    ("22 as ofertas saem na ordem da API, nao do preco", m22_ordem_da_api_em_vez_do_preco),
    ("23 o dado FINO desce para depois da tabela", m23_dado_fino_depois_da_tabela),
    ("24 a ancora da pinca some (30.4)", m24_ancora_da_pinca_some),
    ("25 oferta SEM link de afiliado vai ao ar", m25_oferta_sem_link_vai_ao_ar),
]


def rodar_teste(raiz, portao="produto"):
    arquivo = {
        "produto": "ferramentas/teste-produto.php",
        "casca": "ferramentas/teste-casca.php",
    }[portao]
    r = subprocess.run(["php", os.path.join(raiz, arquivo), raiz],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A familia de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("Familia intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for entrada in MUTACOES:
        nome, mutar = entrada[0], entrada[1]
        portao = entrada[2] if len(entrada) > 2 else "produto"
        tmp = tempfile.mkdtemp(prefix="mut-produto-")
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
                    if "FALHA" in linha:
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia [%s]: %-52s | %s" % (portao, nome, primeira[:66]))
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

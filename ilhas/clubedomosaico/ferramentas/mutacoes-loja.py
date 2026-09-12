#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA LOJA — bloco 4d, 12/09/2026.

Cada mutacao e um defeito ESCRITO DE VOLTA no snippet da Loja. Portao que nao
reprova nao vale o arquivo que ocupa.

TRES REGRAS HERDADAS, e uma nova deste bloco:

  (a) ALVO QUE NAO E UNICO EDITA A COISA ERRADA E PASSA VERDE. Toda troca confere
      que a string aparece EXATAMENTE uma vez no arquivo; quando nao aparece, a
      mutacao e marcada INERTE — e mutacao inerte e teste verde com outro nome.

  (b) MUTACAO QUE UM PORTAO ANTIGO JA PEGAVA NAO JUSTIFICA PORTAO NOVO. Por isso
      cada mutacao roda os DOIS portoes que podem ver o defeito — `teste-loja.php`
      (novo) e `teste-casca.php` (antigo) — e a saida marca as que SO o novo viu.

  (c) A MUTACAO QUE PRODUZ O MUNDO. Algumas travas sao inertes no estado de hoje e
      so significam algo num mundo que ainda nao existe. A m14 e uma dessas: para
      medir que a peca sem preco nao publica oferta, ela tem de produzir a peca sem
      preco, senao passa sem medir nada.

  (d) NOVA AQUI: as mutacoes deste bloco mexem em CODIGO, nao em banco, e codigo
      quebrado de um jeito errado nao reprova — ele nem carrega. A saida separa
      "reprovou" de "nao compila", porque as duas coisas parecem iguais no codigo
      de retorno e so a primeira e evidencia de que a trava funciona.

Uso:  python3 ferramentas/mutacoes-loja.py
"""

import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
SNIPPET = os.path.join("snippets", "clubedomosaico-loja.php")


def trocar(raiz, arquivo, antes, depois, vezes=1):
    """Troca `antes` por `depois`, exigindo que `antes` apareca exatamente `vezes`."""
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()
    achou = texto.count(antes)
    assert achou == vezes, "alvo aparece %d vez(es), esperava %d: %s" % (achou, vezes, antes[:60])
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(antes, depois))


# --------------------------------------------------------------- as mutacoes

def m01(r):
    """O tipo `peca` volta a aparecer no wp-admin. E o requisito escrito do
    Raphael em 10/09 ("eu nao quero que ela entre numa area wp-admin") virando
    falso com a troca de uma palavra."""
    trocar(r, SNIPPET, "'show_ui'             => false,", "'show_ui'             => true,")


def m02(r):
    """O CPT ganha arquivo proprio em /loja/ e passa a disputar a URL com a pagina
    que tem o texto editorial. O vencedor dependeria da ordem das regras de
    reescrita — a decisao 1 do snippet existe para isso nunca acontecer."""
    trocar(r, SNIPPET, "'has_archive'         => false,", "'has_archive'         => true,")


def m03(r):
    """A peca sai de baixo de /loja/ e vira URL de raiz: a arvore da secao 16
    deixa de aparecer no endereco, e a trilha perde a mae."""
    trocar(r, SNIPPET, "define( 'CDM_LOJA_BASE', 'loja' );", "define( 'CDM_LOJA_BASE', 'peca' );")


def m04(r):
    """`map_meta_cap` desligado: o nucleo para de resolver edit_post pelo AUTOR, e
    a artesa passa a poder mexer na peca de qualquer pessoa."""
    trocar(r, SNIPPET, "'map_meta_cap'        => true,", "'map_meta_cap'        => false,")


def m05(r):
    """A taxonomia `colecao` fica publica: nasce com arquivo, entra no
    wp-sitemap.xml, e um dominio de dois dias passa a pedir rastreamento para
    cinco URLs finas (secao 14.1)."""
    trocar(r, SNIPPET, """	register_taxonomy( 'colecao', array( 'peca' ), array(
		'label'              => 'Coleções',
		'hierarchical'       => true,
		'public'             => false,""",
        """	register_taxonomy( 'colecao', array( 'peca' ), array(
		'label'              => 'Coleções',
		'hierarchical'       => true,
		'public'             => true,""")


def m06(r):
    """A regra de qualidade do despacho de 10/09 apagada: peca sem foto publica.
    Uma pagina de produto sem foto e a pior pagina que esta ilha pode servir."""
    trocar(r, SNIPPET, """	if ( ! cdm_loja_galeria( $id ) ) {
		$motivos[] = 'Falta pelo menos uma foto.';
	}
""", "")


def m07(r):
    """Peca sem preco publica. E o outro lado da mesma regra do despacho."""
    trocar(r, SNIPPET, """	if ( '' === $preco || (float) $preco <= 0 ) {
		$motivos[] = 'Falta o preço.';
	}
""", "")


def m08(r):
    """Encomenda sem prazo publica: a ficha diz "sob encomenda" e nao diz quando,
    que e exatamente a informacao pela qual alguem escreve para o ateliê."""
    trocar(r, SNIPPET, """		if ( '' === $prazo || (int) $prazo <= 0 ) {
			$motivos[] = 'Peça sob encomenda precisa do prazo em dias.';
		}
""", "")


def m09(r):
    """A colecao deixa de ser obrigatoria: a peca publica sem se ligar a nada, e a
    malha automatica do despacho de 10/09 vira promessa."""
    trocar(r, SNIPPET, """	if ( ! cdm_loja_termo_da_peca( $id, 'colecao' ) ) {
		$motivos[] = 'Escolha uma coleção.';
	}
""", "")


def m10(r):
    """O preco perde o espaco inquebravel e passa a poder quebrar a linha entre o
    "R$" e o numero — no cartao da Loja, que e a primeira coisa que alguem ve."""
    trocar(r, SNIPPET, "return 'R$&nbsp;' . number_format_i18n", "return 'R$ ' . number_format_i18n")


def m11(r):
    """A disponibilidade mente: sob encomenda passa a sair como pronta entrega no
    JSON-LD, o que e declaracao falsa de estoque para o Google."""
    trocar(r, SNIPPET, """			'availability'  => 'sob_encomenda' === $disp
				? 'https://schema.org/PreOrder'
				: 'https://schema.org/InStock',""",
        """			'availability'  => 'https://schema.org/InStock',""")


def m12(r):
    """O preco do Offer sai em formato brasileiro, com virgula. Schema com preco
    invalido e schema ignorado: a peca perde o dado estruturado inteiro."""
    trocar(r, SNIPPET, "'price'         => number_format( (float) $preco, 2, '.', '' ),",
           "'price'         => number_format( (float) $preco, 2, ',', '.' ),")


def m13(r):
    """A foto perde width e height: a pagina salta quando a imagem carrega, e salto
    na foto de um produto e a primeira coisa que faz o site parecer amador (22.4)."""
    trocar(r, SNIPPET, """	if ( ! empty( $src[1] ) && ! empty( $src[2] ) ) {
		$html .= ' width="' . (int) $src[1] . '" height="' . (int) $src[2] . '"';
	}
	$html .= ' alt="' . esc_attr( $alt ) . '"';""",
        """	$html .= ' alt="' . esc_attr( $alt ) . '"';""")


def m14(r):
    """PRODUZ O MUNDO: o `Offer` passa a sair mesmo sem preco. Sem uma peca sem
    preco no mundo, a trava que proibe isso nunca mede nada — e a peca sem preco e
    o estado normal de um rascunho que ela publicou correndo."""
    trocar(r, SNIPPET, "	if ( '' !== $preco && (float) $preco > 0 ) {\n\t\t$produto['offers'] = array(",
           "	if ( true ) {\n\t\t$produto['offers'] = array(")


def m15(r):
    """A regra de reescrita para de nascer sozinha. E a cicatriz literal da F1, que
    nasceu 404 em 12/09 — e agora seria pior, porque quem teria de salvar os
    permalinks no wp-admin e justamente quem nunca entra la."""
    trocar(r, SNIPPET, "	flush_rewrite_rules( false );\n\tupdate_option( 'cdm_loja_reescrita', $chave, false );",
           "	update_option( 'cdm_loja_reescrita', $chave, false );")


def m16(r):
    """A galeria para de descartar id que nao e mais anexo: foto apagada na
    biblioteca de midia vira `<img>` quebrada na pagina de um produto."""
    trocar(r, SNIPPET, """		if ( function_exists( 'wp_attachment_is_image' ) && ! wp_attachment_is_image( $i ) ) {
			continue;
		}
""", "")


def m17(r):
    """O endpoint de copia da secao 24 fica PUBLICO. As pecas dela, com metadados e
    URLs de foto, passam a sair para qualquer um que souber a rota."""
    trocar(r, SNIPPET, """		'permission_callback' => function ( $pedido ) {
			$esperado = cdm_loja_token_esperado();
			if ( '' === $esperado ) {
				return false;
			}
			$vindo = (string) $pedido->get_param( 'token' );

			return '' !== $vindo && hash_equals( $esperado, $vindo );
		},""",
        """		'permission_callback' => '__return_true',""")


def m18(r):
    """A comparacao do token volta a ser `===`, vulneravel a ataque de tempo.

    UNICA MUTACAO DESTE ARQUIVO QUE NENHUM TESTE DE COMPORTAMENTO PODE PEGAR, e
    isso esta escrito aqui para nao ser confundido com portao fraco: `===` e
    `hash_equals()` devolvem O MESMO resultado para toda entrada. O que muda e o
    TEMPO, e tempo nao e observavel numa bancada. Por isso a trava correspondente
    em `teste-loja.php` le o FONTE — a unica afirmacao daquele arquivo que faz
    isso, e a razao e a natureza da propriedade, nao conveniencia."""
    trocar(r, SNIPPET, "return '' !== $vindo && hash_equals( $esperado, $vindo );",
           "return '' !== $vindo && $esperado === $vindo;")


def m19(r):
    """A peca perde a mae na arvore: a trilha cai de tres degraus para dois e o
    BreadcrumbList deixa de mostrar a Loja."""
    trocar(r, SNIPPET, "		'mae'    => CDM_LOJA_BASE,\n\t\t'rotulo' => $peca->post_title,",
           "		'mae'    => '',\n\t\t'rotulo' => $peca->post_title,")


def m20(r):
    """A folha volta para dentro do retorno do filtro. E a cicatriz de 08/09/2026
    que derrubou cinco calculadoras da Aquametria: os filtros do conteudo trocam o
    E-comercial por entidade e matam o bloco."""
    trocar(r, SNIPPET, "	$html .= '</div>';\n\n\treturn $html;\n}\n}\n\n/* A FICHA ENTRA PELO `the_content`",
           "	$html .= '</div>';\n\t$html .= '<style>.cdm-peca{max-width:60rem;}</style>';\n\n\treturn $html;\n}\n}\n\n/* A FICHA ENTRA PELO `the_content`")


def m21(r):
    """A description perde o teto de 160: a SERP corta no meio e a unica linha da
    peca que aparece na busca fica pela metade."""
    trocar(r, SNIPPET, "if ( mb_strlen( $texto, 'UTF-8' ) <= 160 ) {",
           "if ( mb_strlen( $texto, 'UTF-8' ) <= 100000 ) {")


def m22(r):
    """O telefone aceita numero curto: o botao da peca passa a apontar para um
    WhatsApp que nao existe, e a cliente vai para o vazio."""
    trocar(r, SNIPPET, "	if ( strlen( $so ) < 12 || strlen( $so ) > 13 ) {\n\t\treturn '';\n\t}", "")


def m24(r):
    """Toda foto vira prioritaria: a pagina passa a baixar as oito de uma vez e o
    orcamento de desempenho da 22.4 vai embora no celular dela."""
    trocar(r, SNIPPET, "	$html .= $capa ? ' fetchpriority=\"high\" decoding=\"async\"' : ' loading=\"lazy\" decoding=\"async\"';",
           "	$html .= ' fetchpriority=\"high\" decoding=\"async\"';")


MUTACOES = [
    ("01 o tipo peca volta a aparecer no wp-admin", m01),
    ("02 o CPT disputa /loja/ com a pagina", m02),
    ("03 a peca sai de baixo de /loja/", m03),
    ("04 map_meta_cap desligado (ela edita peca de outra pessoa)", m04),
    ("05 taxonomia publica enche o sitemap de URL fina", m05),
    ("06 peca sem foto publica", m06),
    ("07 peca sem preco publica", m07),
    ("08 encomenda sem prazo publica", m08),
    ("09 a colecao deixa de ser obrigatoria", m09),
    ("10 o preco perde o espaco inquebravel", m10),
    ("11 sob encomenda mente InStock no JSON-LD", m11),
    ("12 o preco do Offer sai com virgula", m12),
    ("13 a foto perde width e height", m13),
    ("14 PRODUZ O MUNDO: Offer sem preco", m14),
    ("15 a regra de reescrita para de nascer (peca 404)", m15),
    ("16 anexo apagado continua na galeria", m16),
    ("17 o endpoint de copia fica publico", m17),
    ("18 o token volta a ser comparado com ===", m18),
    ("19 a peca perde a mae na arvore", m19),
    ("20 a folha volta para dentro do retorno", m20),
    ("21 a description perde o teto de 160", m21),
    ("22 o telefone aceita numero curto", m22),
    ("24 toda foto vira prioritaria", m24),
]


def rodar(raiz, portao):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", portao), raiz],
                       capture_output=True, text=True)
    saida = r.stdout + r.stderr
    nao_compila = ("Parse error" in saida) or ("Fatal error" in saida)
    return r.returncode, saida, nao_compila


def primeira_falha(saida):
    for linha in saida.splitlines():
        if "FALHA" in linha:
            return " ".join(linha.split())[6:]
    return ""


def main():
    for portao in ("teste-loja.php", "teste-casca.php"):
        rc, saida, _ = rodar(ILHA, portao)
        if rc != 0:
            print("O portao %s ja esta reprovado — conserte antes de mutar." % portao)
            print(primeira_falha(saida))
            return 1
    print("Os dois portoes intactos: APROVADOS (como tem que estar antes de comecar)\n")

    passaram = []
    so_o_novo = []
    quebradas = []

    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-loja-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [INERTE: " + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue

            rc_novo, saida_novo, quebrou_novo = rodar(copia, "teste-loja.php")
            rc_velho, saida_velho, quebrou_velho = rodar(copia, "teste-casca.php")

            if quebrou_novo or quebrou_velho:
                quebradas.append(nome)
                print("  NAO COMPILA (nao e evidencia de trava): %s" % nome)
                continue

            if rc_novo == 0 and rc_velho == 0:
                passaram.append(nome)
                print("  PASSOU (nenhuma trava viu): %s" % nome)
                continue

            marca = ""
            if rc_novo != 0 and rc_velho == 0:
                so_o_novo.append(nome)
                marca = "  <-- SO o portao NOVO viu"
            qual = saida_novo if rc_novo != 0 else saida_velho
            print("  reprovou como devia: %-52s | %s%s" % (nome, primeira_falha(qual)[:58], marca))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram, %d nao compilaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram) - len(quebradas), len(passaram), len(quebradas)))
    if so_o_novo:
        print("\nAS QUE SO O PORTAO NOVO PEGOU (%d) — e o que justifica ele existir:" % len(so_o_novo))
        for nome in so_o_novo:
            print("  - %s" % nome)
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    if quebradas:
        print("\nAS QUE NAO COMPILARAM precisam ser reescritas: codigo que nem carrega")
        print("nao prova que a trava funciona.")
        for nome in quebradas:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

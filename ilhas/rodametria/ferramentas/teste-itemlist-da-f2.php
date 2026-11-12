<?php
/**
 * TESTE DO `ItemList` DA F2 — A CAMADA DA MAQUINA DEIXA DE ESTAR CALADA ONDE A
 * TELA SERVE QUATRO PRECOS (12/11/2026).
 *
 * O DEFEITO, MEDIDO NO AR ANTES DE SER CONSERTADO, as 19h2xZ de 12/11/2026 nas
 * 10 URLs do `wp-sitemap.xml`: `/autonomia-patinete-eletrico/` serve bloco de
 * compra com QUATRO cartoes — nome, especificacao, preco com a data da leitura
 * e botao de afiliado — e **ZERO `Product` no JSON-LD**. Das TRES paginas desta
 * ilha que servem `id="comprar"`, as outras duas (`/` e
 * `/peso-maximo-patinete-eletrico/`) o servem VAZIO, e nelas a ausencia e
 * legitima. Esta era a unica com cartao e sem declaracao nenhuma.
 *
 * E A REGRA QUE ESTA BATERIA COBRA NAO E "DECLARE TUDO", E E A METADE QUE
 * IMPORTA: a lista declara `Offer` **so onde o preco e a saida sao da MESMA
 * loja**. O banco de hoje tem, nos 4 cartoes, DOIS com preco lido no Mercado
 * Livre e saida de busca da Shopee — a tela diz as duas coisas numa frase desde
 * 30/10 ("lido no Mercado Livre em 27/10/2026 — o botao abre a Shopee"), e uma
 * `Offer` nao pode: ela e um par preco-URL, e serviria um preco que ninguem
 * mediu naquele destino. O quarto cartao nao tem preco nenhum.
 *
 * ESTE PORTAO E PHP pelo motivo que o `teste-nota-de-preco.php` escreveu
 * primeiro: a lista e decidida em PHP, entao a regua CHAMA a funcao. Regua em
 * Python sobre o texto do snippet conferiria a FORMA do arquivo.
 *
 * E ELE SE PROVA ANTES DE JULGAR (mundo M1): com a loja do preco igualada a da
 * saida, a oferta TEM de aparecer. Portao que nao reprova o mundo que o fez
 * nascer e portao inerte, e a bancada desta ilha usa essa palavra.
 */

foreach ( array( 'add_filter', 'add_action', 'add_shortcode', 'register_activation_hook' ) as $f ) {
	if ( ! function_exists( $f ) ) { eval( "function $f(){ return true; }" ); }
}
if ( ! function_exists( 'esc_html' ) ) {
	function esc_html( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_url( $s ) { return (string) $s; }
	function wp_json_encode( $v, $o = 0 ) { return json_encode( $v, JSON_UNESCAPED_UNICODE ); }
	function date_i18n( $fmt, $ts ) { return date( $fmt, $ts ); }
	function get_option( $k, $d = false ) { return $d; }
}

$RAIZ    = dirname( __DIR__ );
$MUTACAO = getenv( 'RDM_ITEMLIST_MUTACAO' ) ? getenv( 'RDM_ITEMLIST_MUTACAO' ) : '';

if ( ! defined( 'RODAMETRIA_F2_SLUG' ) ) {
	define( 'RODAMETRIA_F2_SLUG', 'autonomia-patinete-eletrico' );
}

/** Carrega UMA funcao de um snippet, equilibrando chaves — o mesmo mecanismo
 *  dos outros portoes PHP desta pasta. */
function carregar_funcao( $src, $nome ) {
	$i = strpos( $src, "function $nome(" );
	if ( false === $i ) { return false; }
	$j = strpos( $src, '{', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '{' === $src[ $k ] ) { $n++; }
		elseif ( '}' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	eval( substr( $src, $i, $k - $i + 1 ) );
	return true;
}

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

$src_f2      = file_get_contents( $RAIZ . '/snippets/rodametria-f2.php' );
$src_casca   = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );
$src_produto = file_get_contents( $RAIZ . '/snippets/rodametria-produto.php' );

foreach ( array(
	array( $src_casca, 'rodametria_casca_escada_de_compra' ),
	array( $src_casca, 'rodametria_casca_nome_da_loja' ),
	array( $src_casca, 'rodametria_casca_na_loja' ),
	array( $src_casca, 'rodametria_casca_a_loja' ),
	array( $src_casca, 'rodametria_casca_artigo_da_loja' ),
	array( $src_f2, 'rodametria_f2_numero' ),
	array( $src_f2, 'rodametria_f2_data' ),
	array( $src_f2, 'rodametria_f2_nota_de_preco' ),
	array( $src_f2, 'rodametria_f2_itens_da_vitrine' ),
	array( $src_f2, 'rodametria_f2_h1' ),
	array( $src_f2, 'rodametria_f2_itemlist' ),
	array( $src_produto, 'rdm_produto_oferta_de_linha' ),
) as $par ) {
	if ( ! carregar_funcao( $par[0], $par[1] ) ) {
		echo "FALHA DE CARGA: a funcao {$par[1]} nao foi achada no snippet\n";
		exit( 1 );
	}
}

/* A DESCRICAO VEM DO MAPA DA CASCA, e o que esta bateria julga e que a funcao
 * a LE de lá em vez de a digitar. O mapa de verdade se monta por filtro do
 * WordPress (a F2 registra a propria pagina nele), entao aqui ele e servido com
 * uma frase CONHECIDA: se a funcao passar a digitar a description, a afirmacao
 * D2 abaixo fica vermelha. Quem compara a frase REAL com a `<meta>` servida e o
 * portao de ar, letra por letra. */
$DESCRICAO_DO_MAPA = 'A description que mora no mapa da casca, e nao no ItemList.';
function rodametria_casca_paginas() {
	global $DESCRICAO_DO_MAPA;

	return array(
		RODAMETRIA_F2_SLUG => array(
			'nome'        => 'Autonomia',
			'titulo'      => 'Quantos km o patinete elétrico faz de verdade — a conta por Wh',
			'description' => $DESCRICAO_DO_MAPA,
		),
	);
}

$banco = json_decode( file_get_contents( $RAIZ . '/dados/f2-respostas.json' ), true );
if ( empty( $banco['compra']['vitrine'] ) ) {
	echo "FALHA: dados/f2-respostas.json nao tem vitrine de compra\n";
	exit( 1 );
}

/* ===========================================================================
 * AS MUTACOES. Cada uma produz um mundo que o banco de hoje NAO tem, e a
 * bateria declara, na propria afirmacao, a frase que espera ouvir dele.
 * ======================================================================== */
$d = $banco;
switch ( $MUTACAO ) {
	case 'mesma-loja':
		/* M1 — o preco do X13 passa a ter sido lido na loja da saida. */
		foreach ( $d['compra']['vitrine'] as $i => $f ) {
			if ( 'x13-chopper-1000w' === $f['id'] ) {
				$d['compra']['vitrine'][ $i ]['preco_programa'] = $f['programa'];
			}
		}
		break;
	case 'sem-data':
		/* M2 — o preco da Shopee perde a data da coleta. */
		foreach ( $d['compra']['vitrine'] as $i => $f ) {
			if ( 'honeywhale-m2-max' === $f['id'] ) {
				$d['compra']['vitrine'][ $i ]['preco_data'] = '';
			}
		}
		break;
	case 'preco-zero':
		/* M3 — o preco existe e e zero. */
		foreach ( $d['compra']['vitrine'] as $i => $f ) {
			if ( 'honeywhale-m2-max' === $f['id'] ) {
				$d['compra']['vitrine'][ $i ]['preco_brl'] = 0;
			}
		}
		break;
	case 'vitrine-vazia':
		/* M4 — nenhum cartao. A lista nao pode nascer vazia. */
		$d['compra']['vitrine'] = array();
		break;
	case 'um-cartao':
		/* M5 — um cartao so, e as posicoes continuam 1..N. */
		$d['compra']['vitrine'] = array( $d['compra']['vitrine'][0] );
		break;
	case 'sem-description':
		/* M6 — o mapa da casca sem description: a chave nao sai. */
		$DESCRICAO_DO_MAPA = '';
		break;
}

$lista = rodametria_f2_itemlist( $d );
$itens = isset( $lista['itemListElement'] ) ? $lista['itemListElement'] : array();
$ofertas = 0;
foreach ( $itens as $el ) {
	if ( ! empty( $el['item']['offers'] ) ) { $ofertas++; }
}

if ( 'vitrine-vazia' === $MUTACAO ) {
	afirma( array() === $lista,
		'M4: com a vitrine vazia a funcao devolve array() e NENHUM ItemList sai — '
		. 'lista de zero item ocupa a camada da IA sem declarar nada' );
	echo "teste-itemlist-da-f2 [M4 vitrine-vazia]: $afirmacoes afirmacao(oes), "
		. count( $falhas ) . " falha(s)\n";
	foreach ( $falhas as $f ) { echo "  FALHA $f\n"; }
	echo count( $falhas ) ? "REPROVADO\n" : "APROVADO\n";
	exit( count( $falhas ) ? 1 : 0 );
}

/* ---------------------------------------------------------------------------
 * (A) O ENVELOPE
 * ------------------------------------------------------------------------ */
afirma( 'ItemList' === $lista['@type'], 'A1: o @type e ItemList' );
afirma( 'https://schema.org' === $lista['@context'], 'A2: o @context e schema.org' );
afirma( rodametria_f2_h1() === $lista['name'],
	'A3: o `name` e o H1 da pagina, pela MESMA funcao que o renderiza — e nao o '
	. '`nome` da trilha nem o `titulo` de busca (a cicatriz do og:title de 11/11)' );
afirma( 'Quantos km o patinete elétrico faz de verdade' === $lista['name'],
	'A4: e a frase e a que a pagina serve no <h1>' );
afirma( count( $itens ) === $lista['numberOfItems'],
	'A5: o `numberOfItems` e a contagem servida' );

$posicoes = array();
foreach ( $itens as $el ) { $posicoes[] = $el['position']; }
afirma( $posicoes === range( 1, count( $itens ) ),
	'A6: as posicoes sao 1..N na ordem servida — e e o pareamento por indice que '
	. 'o portao do envelope cobra no ar' );
foreach ( $itens as $i => $el ) {
	afirma( 'ListItem' === $el['@type'], 'A7: o degrau ' . ( $i + 1 ) . ' e ListItem' );
	afirma( 'Product' === $el['item']['@type'],
		'A8: o item do degrau ' . ( $i + 1 ) . ' e Product' );
	afirma( '' !== trim( (string) $el['item']['name'] ),
		'A9: o item do degrau ' . ( $i + 1 ) . ' tem nome' );
}

/* ---------------------------------------------------------------------------
 * (B) A LISTA E A MESMA EXPRESSAO QUE O BLOCO DE COMPRA RECEBE
 * ------------------------------------------------------------------------ */
$do_bloco = rodametria_f2_itens_da_vitrine( $d );
afirma( count( $do_bloco ) === count( $itens ),
	'B1: a lista tem o mesmo numero de itens que o bloco de compra recebe — a '
	. 'fonte e a MESMA expressao, nao o banco cru (20.7)' );
foreach ( $do_bloco as $i => $item ) {
	afirma( isset( $itens[ $i ] ) && $item['nome'] === $itens[ $i ]['item']['name'],
		'B2: o degrau ' . ( $i + 1 ) . ' nomeia o mesmo anuncio que o cartao ' . ( $i + 1 ) );
}

/* ---------------------------------------------------------------------------
 * (C) A OFERTA SO ONDE O PRECO E A SAIDA SAO DA MESMA LOJA
 * ------------------------------------------------------------------------ */
$esperadas = 0;
foreach ( $d['compra']['vitrine'] as $f ) {
	if ( ! empty( $f['preco_brl'] ) && ! empty( $f['preco_data'] )
		&& ! empty( $f['preco_programa'] )
		&& (string) $f['preco_programa'] === (string) $f['programa'] ) {
		$esperadas++;
	}
}
afirma( $ofertas === $esperadas,
	"C1: $ofertas oferta(s) declarada(s) e $esperadas elegivel(is) pela regra da "
	. 'mesma loja — contadas do banco, nunca escritas aqui' );

foreach ( $itens as $i => $el ) {
	$nome = $el['item']['name'];
	$tem  = ! empty( $el['item']['offers'] );
	$f    = null;
	foreach ( $d['compra']['vitrine'] as $cand ) {
		if ( $cand['nome'] === $nome ) { $f = $cand; break; }
	}
	if ( null === $f ) { continue; }
	$mesma = ( ! empty( $f['preco_brl'] ) && ! empty( $f['preco_data'] )
		&& ! empty( $f['preco_programa'] )
		&& (string) $f['preco_programa'] === (string) $f['programa'] );
	afirma( $tem === $mesma,
		"C2: $nome " . ( $mesma ? 'tem' : 'NAO tem' ) . ' preco e saida na mesma loja, '
		. 'e a oferta dele ' . ( $tem ? 'existe' : 'nao existe' ) );
	if ( ! $tem ) { continue; }
	$of = $el['item']['offers'];
	afirma( 'Offer' === $of['@type'], "C3: a oferta de $nome e Offer" );
	afirma( 'BRL' === $of['priceCurrency'], "C4: a oferta de $nome e em BRL" );
	afirma( ! isset( $of['availability'] ),
		"C5: a oferta de $nome NAO declara availability (a regra da secao 7-b, "
		. 'herdada por chamar a MESMA funcao da vitrine)' );
	afirma( ! isset( $of['priceValidUntil'] ),
		"C6: a oferta de $nome NAO declara priceValidUntil" );
	afirma( isset( $of['priceSpecification']['validFrom'] )
		&& (string) $f['preco_data'] === $of['priceSpecification']['validFrom'],
		"C7: a oferta de $nome diz quando o preco foi lido ({$f['preco_data']})" );
	afirma( isset( $of['url'] ) && '' !== $of['url'],
		"C8: a oferta de $nome tem url de saida" );
	$escada = rodametria_casca_escada_de_compra( array(
		'url'       => isset( $f['url_afiliado_da_ficha'] ) ? $f['url_afiliado_da_ficha'] : '',
		'url_busca' => isset( $f['url_busca'] ) ? $f['url_busca'] : '',
		'degrau'    => $f['degrau'],
	) );
	afirma( $escada['url'] === $of['url'],
		"C9: a url da oferta de $nome e a que a escada da 25.2 escolhe, nao a crua" );
}

/* ---------------------------------------------------------------------------
 * (D) A DESCRICAO VEM DO MAPA DA CASCA, NAO DAQUI
 * ------------------------------------------------------------------------ */
if ( 'sem-description' === $MUTACAO ) {
	afirma( ! isset( $lista['description'] ),
		'D1: sem description no mapa, a chave NAO sai da lista — chave vazia '
		. 'declara menos que chave ausente (25.9)' );
} else {
	afirma( isset( $lista['description'] ) && $DESCRICAO_DO_MAPA === $lista['description'],
		'D2: a `description` e a do MAPA DA CASCA, que e a mesma fonte da '
		. '`<meta name=description>` e do `og:description` — uma fonte, tres '
		. 'leituras, e o portao de ar as compara letra por letra' );
}

/* ---------------------------------------------------------------------------
 * (E) O QUE CADA MUTACAO TEM DE PROVAR
 * ------------------------------------------------------------------------ */
switch ( $MUTACAO ) {
	case 'mesma-loja':
		afirma( 2 === $ofertas,
			'M1: igualando a loja do preco a da saida no X13, as ofertas sobem de '
			. '1 para 2 — e esta e a prova de que a regra da mesma loja esta VIVA '
			. 'e nao e um acidente do dado de hoje' );
		break;
	case 'sem-data':
		afirma( 0 === $ofertas,
			'M2: sem a data da coleta, a oferta da Shopee NAO sai — preco sem data '
			. 'nesta ilha e preco que ninguem sabe de quando e' );
		break;
	case 'preco-zero':
		afirma( 0 === $ofertas,
			'M3: com preco ZERO a oferta NAO sai — `price: 0.00` declararia que o '
			. 'patinete e de graca' );
		break;
	case 'um-cartao':
		afirma( 1 === count( $itens ) && array( 1 ) === $posicoes,
			'M5: com um cartao so, a lista tem UM degrau na posicao 1' );
		break;
}

/* ---------------------------------------------------------------------------
 * (F) A BATERIA SE RODA INTEIRA NUMA CHAMADA — senao a bancada ve so o banco de
 * hoje, e e justamente o banco de hoje que nao tem os mundos que importam.
 *
 * ATENCAO A DIFERENCA COM O `teste-oferta-datada.php`: la as mutacoes trocam o
 * CODIGO e tem de REPROVAR. Aqui elas trocam o DADO e cada uma AFIRMA o mundo
 * que fabrica, entao tem de APROVAR — mutacao que reprova aqui e a regra que
 * mudou de comportamento sem ninguem notar.
 * ------------------------------------------------------------------------ */
$MUTACOES = array(
	'mesma-loja'      => 'igualar a loja do preco a da saida faz a oferta APARECER',
	'sem-data'        => 'preco sem data da coleta nao vira oferta',
	'preco-zero'      => 'preco zero nao vira oferta',
	'vitrine-vazia'   => 'sem cartao nao nasce ItemList nenhum',
	'um-cartao'       => 'com um cartao a posicao e 1',
	'sem-description' => 'sem description no mapa a chave nao sai',
);
if ( '' === $MUTACAO ) {
	foreach ( $MUTACOES as $mut => $oque ) {
		$saida  = array();
		$codigo = 0;
		exec( 'RDM_ITEMLIST_MUTACAO=' . $mut . ' php ' . escapeshellarg( __FILE__ ) . ' 2>&1',
			$saida, $codigo );
		if ( 0 !== $codigo ) {
			$falhas[] = "mutacao $mut REPROVOU, e ela devia aprovar — $oque. Saida: "
				. implode( ' | ', array_slice( $saida, -2 ) );
		}
	}
}

$rotulo = '' === $MUTACAO ? 'BANCO DE HOJE' : "M:$MUTACAO";
echo "teste-itemlist-da-f2 [$rotulo]: $afirmacoes afirmacao(oes), "
	. count( $itens ) . ' degrau(s), ' . $ofertas . ' oferta(s), '
	. ( '' === $MUTACAO ? count( $MUTACOES ) : 0 ) . " mutacao(oes) cobrada(s), "
	. count( $falhas ) . " falha(s)\n";
foreach ( $falhas as $f ) { echo "  FALHA $f\n"; }
echo count( $falhas ) ? "REPROVADO\n" : "APROVADO\n";
exit( count( $falhas ) ? 1 : 0 );

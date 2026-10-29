<?php
/**
 * RODAMETRIA — CASCA (bloco 3b da fila do PROMPT.md)
 *
 * Identidade, estrutura e o MOLDE DE CONVERSAO da secao 32 do ARQUIPELAGO.md,
 * em um lugar so. Esta e a PRIMEIRA revisao desta ilha que publica alguma
 * coisa: a revisao 1 do manifest existia de proposito com os tres grupos
 * vazios, para provar o canal sem nada em risco.
 *
 * O QUE ESTA CASCA DECIDE, E POR QUE AQUI E NAO EM CADA SNIPPET (32.6-b):
 * "o que se repete entre paginas (ordem dos blocos, carrossel de compra, barra
 * fixa do rodape, <details>) vira componente da CASCA, reaproveitado por todas
 * as ferramentas, em vez de ser reescrito em cada snippet". Entao a caixa de
 * resultado, a dobra, o cartao de compra, o carrossel e a barra fixa do
 * telefone moram aqui, e a 32.5-c cobra que as regras de telefone do molde
 * alcancem toda familia de pagina POR SELETOR — por isso as classes do molde
 * sao `rdm-molde-*` e nenhuma folha de ferramenta redecora a caixa do molde.
 *
 * TRES REGRAS DA SECAO 8 QUE ESTE ARQUIVO OBEDECE DE PROPOSITO:
 *   1. Toda funcao de nivel superior dentro de if ( ! function_exists() ).
 *   2. NADA de <script> dentro do que um shortcode devolve: o WordPress roda os
 *      filtros do the_content sobre o retorno e troca && por &#038;&#038;,
 *      matando o script inteiro. Todo JS desta ilha sai no wp_footer.
 *   3. Texto de tela sai acentuado, e caminho de arquivo do repositorio nunca
 *      aparece na pagina (32.4: texto de bastidor da fabrica e proibido).
 *
 * Tokens: ilhas/rodametria/DESIGN.md e a lei (secao 22.6). Nenhuma cor, fonte
 * ou escala nasce aqui sem estar la.
 */

if ( ! defined( 'RODAMETRIA_CASCA_VERSAO' ) ) {
	define( 'RODAMETRIA_CASCA_VERSAO', '1.1.1' );
}

/**
 * O ID DO ITEM DE DADOS, EXATAMENTE COMO ELE ESTA NO manifest.json.
 *
 * Quem grava a option e o Sync, e a chave dele e `rodametria_dados_` mais
 * `sanitize_key( $item['id'] )` — e sanitize_key PRESERVA hifen. Entao o nome
 * da option e FATO EXTERNO a este arquivo: ele sai do id do manifest, nunca de
 * um nome digitado aqui.
 *
 * A PRIMEIRA VERSAO DESTA CASCA DIGITOU `f2_respostas`, com sublinhado, e o
 * conferir-no-ar.py a pegou na primeira passada, as 10h4xZ de 29/10/2026: o
 * Sync gravou `rodametria_dados_f2-respostas`, a casca pediu
 * `rodametria_dados_f2_respostas`, get_option devolveu false e a pagina caiu no
 * estado degradado honesto — sem erro de PHP, sem linha vermelha no log do Sync
 * e com as tres linhas da revisao 2 dizendo `ok`. E a familia do "resumo verde
 * nao e entrega" da 20.4, num andar abaixo: aqui o desembarque ACONTECEU e o
 * que falhou foi a leitura dele.
 */
if ( ! defined( 'RODAMETRIA_ID_DADOS_F2' ) ) {
	define( 'RODAMETRIA_ID_DADOS_F2', 'f2-respostas' );
}

/* ===========================================================================
 * 1. O MAPA DAS PAGINAS
 *
 * Uma entrada por pagina da ilha, e e deste mapa que saem o menu, a trilha, o
 * <title>, a description e o BreadcrumbList. Pagina nova entra pelo filtro
 * 'rodametria_paginas', de dentro do proprio snippet dela — e foi assim que a
 * F2 entrou, sem esta casca saber o nome dela.
 *
 * `description` diz O QUE A PAGINA RESPONDE, na voz do VOZ.md, e NUNCA carrega
 * numero digitado: numero de tela nasce contado (secao 8). Quando a pagina quer
 * numero na description, ela o passa pelo filtro com o numero ja derivado.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_paginas' ) ) {
function rodametria_casca_paginas() {
	$mapa = array(
		'inicio' => array(
			'nome'        => 'Início',
			'titulo'      => 'Rodametria — os três números antes de comprar um elétrico',
			'tipo'        => 'website',
			'no_menu'     => false,
			'pai'         => null,
			'description' => 'Antes de comprar patinete, scooter, moto ou bike elétrica: '
				. 'veja se precisa de CNH, quantos km a bateria faz de verdade com o seu '
				. 'peso e se o modelo aguenta você.',
		),
	);

	/**
	 * Cada ferramenta e cada guia acrescenta a propria entrada aqui, de dentro
	 * do snippet dela. A casca nao conhece o nome de nenhuma por antecipacao —
	 * e por isso que ela nao precisa ser editada quando a ilha cresce.
	 */
	$mapa = apply_filters( 'rodametria_paginas', $mapa );

	return is_array( $mapa ) ? $mapa : array();
}
}

if ( ! function_exists( 'rodametria_casca_slug_atual' ) ) {
function rodametria_casca_slug_atual() {
	if ( is_front_page() ) {
		return 'inicio';
	}
	$id = get_queried_object_id();
	if ( ! $id ) {
		return '';
	}
	$slug = get_post_field( 'post_name', $id );

	return is_string( $slug ) ? $slug : '';
}
}

if ( ! function_exists( 'rodametria_casca_url_do_slug' ) ) {
function rodametria_casca_url_do_slug( $slug ) {
	if ( 'inicio' === $slug ) {
		return home_url( '/' );
	}
	$p = get_page_by_path( $slug, OBJECT, 'page' );
	if ( $p && 'publish' === $p->post_status ) {
		return get_permalink( $p );
	}

	return '';
}
}

/**
 * Link so sai se a pagina EXISTIR e estiver publicada. O motivo esta na secao
 * 16: link interno para URL que da 404 custa mais do que link que falta, e a
 * cicatriz de "o hub apontando para uma pagina que nao existe" e de 08/09/2026
 * na Robometria. Quem nao existe ainda simplesmente nao aparece no menu.
 */
if ( ! function_exists( 'rodametria_casca_link' ) ) {
function rodametria_casca_link( $slug, $rotulo = '' ) {
	$url = rodametria_casca_url_do_slug( $slug );
	if ( '' === $url ) {
		return '';
	}
	$mapa   = rodametria_casca_paginas();
	$rotulo = '' !== $rotulo ? $rotulo : ( isset( $mapa[ $slug ]['nome'] ) ? $mapa[ $slug ]['nome'] : $slug );

	return '<a href="' . esc_url( $url ) . '">' . esc_html( $rotulo ) . '</a>';
}
}

/* ===========================================================================
 * 2. A MARCA — simbolo V9 e assinatura H1, aprovados em 27/10/2026
 *
 * O DESIGN.md manda: "o simbolo nunca perde detalhe. Em qualquer tamanho do
 * cabecalho vai o desenho completo (raios, manetes, garfo, risquinhos da
 * roda)". Entao o SVG do cabecalho e o mesmo logo.svg da pasta da ilha, inteiro
 * — so o favicon (<= 32 px) simplifica.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_simbolo_svg' ) ) {
function rodametria_casca_simbolo_svg( $altura = 44, $negativo = false ) {
	$tinta  = $negativo ? '#FFFFFF' : '#13212B';
	$verde  = $negativo ? '#3FC08E' : '#0A6B4C';
	$miolo  = $negativo ? '#13212B' : '#FFFFFF';
	$largura = (int) round( $altura );

	$svg  = '<svg class="rdm-simbolo" viewBox="0 0 120 120" width="' . (int) $largura . '" height="' . (int) $altura . '"'
		. ' role="img" aria-label="Rodametria" focusable="false" xmlns="http://www.w3.org/2000/svg">';
	/* asas em pena, tres de cada lado */
	for ( $i = 0; $i < 3; $i++ ) {
		$y  = 34 + ( $i * 11 );
		$cx = 22 - ( $i * 3 );
		$svg .= '<path d="M' . $cx . ' ' . $y . ' q14 -7 26 0 q-13 5 -26 0 z" fill="' . esc_attr( $tinta ) . '" opacity="0.9"/>';
		$svg .= '<path d="M' . ( 120 - $cx ) . ' ' . $y . ' q-14 -7 -26 0 q13 5 26 0 z" fill="' . esc_attr( $tinta ) . '" opacity="0.9"/>';
	}
	/* raios verdes saindo do farol — onze, como o DESIGN.md manda */
	for ( $i = 0; $i < 11; $i++ ) {
		$ang = -90 + ( ( $i - 5 ) * 13 );
		$r1  = 23;
		$r2  = 32;
		$x1  = 60 + $r1 * cos( deg2rad( $ang ) );
		$y1  = 40 + $r1 * sin( deg2rad( $ang ) );
		$x2  = 60 + $r2 * cos( deg2rad( $ang ) );
		$y2  = 40 + $r2 * sin( deg2rad( $ang ) );
		$svg .= '<line x1="' . round( $x1, 1 ) . '" y1="' . round( $y1, 1 ) . '" x2="' . round( $x2, 1 )
			. '" y2="' . round( $y2, 1 ) . '" stroke="' . esc_attr( $verde ) . '" stroke-width="2.4" stroke-linecap="round"/>';
	}
	/* guidao com manoplas e manetes */
	$svg .= '<path d="M30 48 h60" stroke="' . esc_attr( $tinta ) . '" stroke-width="5" stroke-linecap="round" fill="none"/>';
	$svg .= '<path d="M28 48 h6 M86 48 h6" stroke="' . esc_attr( $tinta ) . '" stroke-width="9" stroke-linecap="round"/>';
	$svg .= '<path d="M36 52 l-6 5 M84 52 l6 5" stroke="' . esc_attr( $tinta ) . '" stroke-width="3" stroke-linecap="round"/>';
	/* painel com tela verde */
	$svg .= '<rect x="50" y="38" width="20" height="13" rx="2.5" fill="' . esc_attr( $tinta ) . '"/>';
	$svg .= '<rect x="53" y="41" width="14" height="7" rx="1" fill="' . esc_attr( $verde ) . '"/>';
	/* coluna e garfo */
	$svg .= '<path d="M60 51 v30" stroke="' . esc_attr( $tinta ) . '" stroke-width="6" stroke-linecap="round"/>';
	$svg .= '<path d="M60 81 l-9 10 M60 81 l9 10" stroke="' . esc_attr( $tinta ) . '" stroke-width="4" stroke-linecap="round"/>';
	/* para-lama */
	$svg .= '<path d="M46 92 q14 -10 28 0" stroke="' . esc_attr( $tinta ) . '" stroke-width="3.4" fill="none" stroke-linecap="round"/>';
	/* roda com tres risquinhos */
	$svg .= '<circle cx="60" cy="100" r="13" fill="none" stroke="' . esc_attr( $tinta ) . '" stroke-width="5"/>';
	$svg .= '<path d="M60 92 v6 M53 104 l5 -3 M67 104 l-5 -3" stroke="' . esc_attr( $tinta ) . '" stroke-width="2" stroke-linecap="round"/>';
	/* farol com centro verde */
	$svg .= '<circle cx="60" cy="40" r="7.5" fill="' . esc_attr( $tinta ) . '"/>';
	$svg .= '<circle cx="60" cy="40" r="3.6" fill="' . esc_attr( $verde ) . '"/>';
	$svg .= '<circle cx="60" cy="40" r="1.4" fill="' . esc_attr( $miolo ) . '"/>';
	$svg .= '</svg>';

	return $svg;
}
}

if ( ! function_exists( 'rodametria_casca_assinatura_html' ) ) {
function rodametria_casca_assinatura_html( $negativo = false ) {
	$na_home = is_front_page();
	$dentro  = rodametria_casca_simbolo_svg( 44, $negativo )
		. '<span class="rdm-marca-texto">'
		. '<span class="rdm-marca-nome">RODAMETRIA</span>'
		. '<span class="rdm-marca-linha">MOBILIDADE ELÉTRICA</span>'
		. '</span>';

	$classe = 'rdm-marca' . ( $negativo ? ' rdm-marca-negativa' : '' );

	if ( $na_home && ! $negativo ) {
		return '<span class="' . esc_attr( $classe ) . '">' . $dentro . '</span>';
	}

	return '<a class="' . esc_attr( $classe ) . '" href="' . esc_url( home_url( '/' ) ) . '">' . $dentro . '</a>';
}
}

/* ===========================================================================
 * 3. CABECALHO, MENU E RODAPE
 *
 * Menu hamburguer no celular e padrao fixo do Arquipelago (secao 6): os links
 * existem no HTML servido, sao <a href> de verdade dentro de <nav>, o botao e
 * <button> com aria-expanded e aria-controls, e o teclado funciona. O JS que
 * abre e fecha sai no wp_footer, nunca aqui.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_nav_html' ) ) {
function rodametria_casca_nav_html() {
	$mapa  = rodametria_casca_paginas();
	$itens = array();
	foreach ( $mapa as $slug => $p ) {
		if ( 'inicio' === $slug || ! empty( $p['no_menu'] ) ) {
			continue;
		}
		$url = rodametria_casca_url_do_slug( $slug );
		if ( '' === $url ) {
			continue;
		}
		$atual  = ( $slug === rodametria_casca_slug_atual() );
		$itens[] = '<li><a href="' . esc_url( $url ) . '"'
			. ( $atual ? ' aria-current="page"' : '' ) . '>'
			. esc_html( isset( $p['nome'] ) ? $p['nome'] : $slug ) . '</a></li>';
	}

	$html  = '<nav class="rdm-nav" aria-label="Navegação principal">';
	$html .= '<button class="rdm-nav-botao" type="button" aria-expanded="false" aria-controls="rdm-nav-lista">';
	$html .= '<span class="rdm-nav-barras" aria-hidden="true"></span><span>Menu</span></button>';
	$html .= '<ul class="rdm-nav-lista" id="rdm-nav-lista">' . implode( '', $itens ) . '</ul>';
	$html .= '</nav>';

	return $html;
}
}

if ( ! function_exists( 'rodametria_casca_cabecalho_html' ) ) {
function rodametria_casca_cabecalho_html() {
	return '<header class="rdm-cabecalho"><div class="rdm-faixa">'
		. rodametria_casca_assinatura_html()
		. rodametria_casca_nav_html()
		. '</div></header>';
}
}

if ( ! function_exists( 'rodametria_casca_rodape_html' ) ) {
function rodametria_casca_rodape_html() {
	$ano   = (int) current_time( 'Y' );
	$links = array();
	foreach ( rodametria_casca_paginas() as $slug => $p ) {
		if ( 'inicio' === $slug ) {
			continue;
		}
		$l = rodametria_casca_link( $slug );
		if ( '' !== $l ) {
			$links[] = '<li>' . $l . '</li>';
		}
	}

	$html  = '<footer class="rdm-rodape"><div class="rdm-faixa">';
	$html .= '<div class="rdm-rodape-marca">' . rodametria_casca_assinatura_html( true ) . '</div>';
	if ( $links ) {
		$html .= '<ul class="rdm-rodape-links">' . implode( '', $links ) . '</ul>';
	}
	$html .= '<p class="rdm-rodape-aviso">A Rodametria participa de programas de afiliados: '
		. 'quando você compra pelos links desta página, a gente recebe uma comissão da loja, '
		. 'sem mudar o preço para você. Isso nunca muda a ordem das recomendações — quem decide '
		. 'a ordem é o que o fabricante declara.</p>';
	$html .= '<p class="rdm-rodape-creditos">© ' . $ano . ' Rodametria · Os números desta página vêm '
		. 'das fichas e das medições citadas em “Como sabemos”, com a data de cada leitura.</p>';
	$html .= '</div></footer>';

	return $html;
}
}

/**
 * Em tema de blocos o rodape e uma template part renderizada DENTRO do fluxo do
 * conteudo. Trocar a saida dela aqui e o que impede os dois rodapes empilhados —
 * a cicatriz esta escrita na casca da Robometria.
 */
if ( ! function_exists( 'rodametria_casca_rodape_impresso' ) ) {
function rodametria_casca_rodape_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}

	return $impresso;
}
}

add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	$nome = isset( $bloco['blockName'] ) ? $bloco['blockName'] : '';

	if ( 'core/site-title' === $nome || 'core/site-logo' === $nome ) {
		return rodametria_casca_assinatura_html();
	}
	if ( 'core/navigation' === $nome ) {
		return rodametria_casca_nav_html();
	}
	/* A tagline padrao do WordPress e residuo do tema. */
	if ( 'core/site-tagline' === $nome ) {
		return '';
	}
	/* DOIS <h1> POR PAGINA, medido no ar as 10h5xZ de 29/10/2026 na primeira
	   passada do portao: o tema de blocos imprime o post_title como <h1> e o
	   shortcode da pagina imprime o H1 dela. Quem sai e o do TEMA, porque o da
	   pagina e o que a 32.1 poe na ordem certa (depois da trilha, antes da
	   promessa) e o que a 32.3 protege como SEO que nao muda. H1 duplicado nao
	   da erro em lugar nenhum: so uma afirmacao que CONTA o ve. */
	if ( 'core/post-title' === $nome ) {
		return '';
	}
	if ( 'core/template-part' === $nome ) {
		$parte = isset( $bloco['attrs']['slug'] ) ? $bloco['attrs']['slug'] : '';
		if ( 'footer' === $parte || 'rodape' === $parte ) {
			rodametria_casca_rodape_impresso( true );

			return rodametria_casca_rodape_html();
		}
		if ( 'header' === $parte || 'cabecalho' === $parte ) {
			return rodametria_casca_cabecalho_html();
		}
	}

	return $conteudo;
}, 10, 2 );

add_action( 'wp_footer', function () {
	if ( rodametria_casca_rodape_impresso() ) {
		return;
	}
	rodametria_casca_rodape_impresso( true );
	echo rodametria_casca_rodape_html(); // markup proprio, escapado campo a campo
}, 20 );

/* ===========================================================================
 * 4. TRILHA (breadcrumb) E JSON-LD
 *
 * A 32.3 e explicita: trilha, BreadcrumbList, JSON-LD, title, H1 e URL NAO
 * mudam com o molde de conversao — sao SEO e ficam iguais. Entao os dois moram
 * aqui, numa funcao so, e toda pagina os recebe de graca.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_cadeia_da_trilha' ) ) {
function rodametria_casca_cadeia_da_trilha( $slug ) {
	$mapa   = rodametria_casca_paginas();
	$cadeia = array();
	$visto  = array();
	while ( '' !== $slug && isset( $mapa[ $slug ] ) && ! isset( $visto[ $slug ] ) ) {
		$visto[ $slug ] = true;
		array_unshift( $cadeia, $slug );
		$slug = isset( $mapa[ $slug ]['pai'] ) && $mapa[ $slug ]['pai'] ? $mapa[ $slug ]['pai'] : '';
	}
	if ( ! $cadeia || 'inicio' !== $cadeia[0] ) {
		array_unshift( $cadeia, 'inicio' );
	}

	return $cadeia;
}
}

if ( ! function_exists( 'rodametria_casca_trilha_html' ) ) {
function rodametria_casca_trilha_html() {
	$slug = rodametria_casca_slug_atual();
	if ( '' === $slug || 'inicio' === $slug ) {
		return '';
	}
	$mapa   = rodametria_casca_paginas();
	$cadeia = rodametria_casca_cadeia_da_trilha( $slug );
	$partes = array();
	$ultimo = count( $cadeia ) - 1;
	foreach ( $cadeia as $i => $s ) {
		$nome = isset( $mapa[ $s ]['nome'] ) ? $mapa[ $s ]['nome'] : $s;
		if ( $i === $ultimo ) {
			$partes[] = '<li><span aria-current="page">' . esc_html( $nome ) . '</span></li>';
			continue;
		}
		$url      = rodametria_casca_url_do_slug( $s );
		$partes[] = '<li>' . ( '' === $url
			? esc_html( $nome )
			: '<a href="' . esc_url( $url ) . '">' . esc_html( $nome ) . '</a>' ) . '</li>';
	}

	return '<nav class="rdm-trilha" aria-label="Trilha"><ol>' . implode( '', $partes ) . '</ol></nav>';
}
}

add_action( 'wp_head', function () {
	$slug = rodametria_casca_slug_atual();
	$mapa = rodametria_casca_paginas();
	if ( '' === $slug || ! isset( $mapa[ $slug ] ) ) {
		return;
	}
	$p = $mapa[ $slug ];

	if ( ! empty( $p['description'] ) ) {
		echo '<meta name="description" content="' . esc_attr( $p['description'] ) . '">' . "\n";
		echo '<meta property="og:description" content="' . esc_attr( $p['description'] ) . '">' . "\n";
	}
	echo '<meta property="og:title" content="' . esc_attr( isset( $p['nome'] ) ? $p['nome'] : '' ) . '">' . "\n";
	echo '<meta property="og:type" content="website">' . "\n";
	echo '<meta property="og:site_name" content="Rodametria">' . "\n";
	echo '<meta property="og:locale" content="pt_BR">' . "\n";
	echo '<meta property="og:url" content="' . esc_url( rodametria_casca_url_do_slug( $slug ) ) . '">' . "\n";

	/* WebSite + Organization, uma ocorrencia so, na home. */
	if ( 'inicio' === $slug ) {
		$site = array(
			'@context'    => 'https://schema.org',
			'@type'       => 'WebSite',
			'name'        => 'Rodametria',
			'url'         => home_url( '/' ),
			'inLanguage'  => 'pt-BR',
			'description' => $p['description'],
			'publisher'   => array(
				'@type' => 'Organization',
				'name'  => 'Rodametria',
				'url'   => home_url( '/' ),
			),
		);
		echo '<script type="application/ld+json">'
			. wp_json_encode( $site, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
			. '</script>' . "\n";
	}

	/* BreadcrumbList em toda pagina que nao e a home (16.4). */
	$cadeia = rodametria_casca_cadeia_da_trilha( $slug );
	if ( count( $cadeia ) > 1 ) {
		$itens = array();
		foreach ( $cadeia as $i => $s ) {
			$itens[] = array(
				'@type'    => 'ListItem',
				'position' => $i + 1,
				'name'     => isset( $mapa[ $s ]['nome'] ) ? $mapa[ $s ]['nome'] : $s,
				'item'     => rodametria_casca_url_do_slug( $s ),
			);
		}
		echo '<script type="application/ld+json">'
			. wp_json_encode( array(
				'@context'        => 'https://schema.org',
				'@type'           => 'BreadcrumbList',
				'itemListElement' => $itens,
			), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
			. '</script>' . "\n";
	}
}, 6 );

/* O <title> do documento sai do mapa, nao do tema: titulo e campo publicado e
 * precisa ter uma fonte so (secao 8). */
add_filter( 'pre_get_document_title', function ( $titulo ) {
	$slug = rodametria_casca_slug_atual();
	$mapa = rodametria_casca_paginas();
	if ( '' !== $slug && ! empty( $mapa[ $slug ]['titulo'] ) ) {
		return $mapa[ $slug ]['titulo'];
	}

	return $titulo;
}, 10, 1 );

/* ===========================================================================
 * 5. FAVICON — simbolo proprio desde o dia 1 (secao 6)
 *
 * Icone padrao do WordPress na aba = bloco reprovado. Aqui o <= 32 px pode
 * simplificar, e e a UNICA excecao que o DESIGN.md abre ao "nunca perde
 * detalhe": roda, coluna, guidao e farol verde.
 * ======================================================================== */

remove_action( 'wp_head', 'wp_site_icon', 99 );

if ( ! defined( 'RODAMETRIA_CASCA_ICONE_SVG' ) ) {
	define( 'RODAMETRIA_CASCA_ICONE_SVG',
		'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
		. '<rect width="32" height="32" rx="6" fill="#13212B"/>'
		. '<path d="M9 11 h14" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
		. '<path d="M16 12 v10" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
		. '<circle cx="16" cy="25" r="4.2" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>'
		. '<circle cx="16" cy="11" r="3.2" fill="#3FC08E"/></svg>' );
}

add_action( 'wp_head', function () {
	echo '<link rel="icon" type="image/svg+xml" href="'
		. esc_attr( 'data:image/svg+xml,' . rawurlencode( RODAMETRIA_CASCA_ICONE_SVG ) ) . '">' . "\n";
	echo '<meta name="theme-color" content="#13212B">' . "\n";
}, 5 );

/* ===========================================================================
 * 6. OS COMPONENTES DO MOLDE DA SECAO 32
 *
 * Todos aqui, nenhum reescrito em snippet de ferramenta — e a 32.6-b. Cada um
 * devolve markup JA ESCAPADO campo a campo.
 * ======================================================================== */

/**
 * A CAIXA DE RESULTADO (32.1, item 4). Numero em Mono, frase de leitura
 * embaixo. O `tom` decide a cor da borda: 'verde' para o veredito que libera,
 * 'alerta' para o que trava, 'neutro' para numero sem veredito. O DESIGN.md
 * manda: um uso forte do verde por tela, fora da marca.
 */
if ( ! function_exists( 'rodametria_casca_caixa' ) ) {
function rodametria_casca_caixa( $rotulo, $numero, $unidade, $frases, $tom = 'neutro', $atributos = '' ) {
	$tons  = array( 'verde', 'alerta', 'neutro' );
	$tom   = in_array( $tom, $tons, true ) ? $tom : 'neutro';
	$html  = '<div class="rdm-molde-caixa rdm-molde-caixa-' . esc_attr( $tom ) . '"' . $atributos . '>';
	$html .= '<p class="rdm-molde-caixa-rotulo">' . esc_html( $rotulo ) . '</p>';
	$html .= '<p class="rdm-molde-caixa-numero"><span class="rdm-num">' . esc_html( $numero ) . '</span>';
	if ( '' !== (string) $unidade ) {
		$html .= ' <span class="rdm-molde-caixa-unidade">' . esc_html( $unidade ) . '</span>';
	}
	$html .= '</p>';
	foreach ( (array) $frases as $f ) {
		$html .= '<p class="rdm-molde-caixa-frase">' . esc_html( $f ) . '</p>';
	}
	$html .= '</div>';

	return $html;
}
}

/**
 * A DOBRA (32.1, item 7). <details>/<summary> de verdade: pela 32.3 e pela
 * 22.8 o texto continua no HTML servido e legivel com o JavaScript desligado.
 */
if ( ! function_exists( 'rodametria_casca_dobra' ) ) {
function rodametria_casca_dobra( $titulo, $corpo, $aberta = false ) {
	return '<details class="rdm-molde-dobra"' . ( $aberta ? ' open' : '' ) . '>'
		. '<summary><span>' . esc_html( $titulo ) . '</span></summary>'
		. '<div class="rdm-molde-dobra-corpo">' . $corpo . '</div></details>';
}
}

/**
 * ROTULO DO BOTAO DE LOJA, E ELE DEPENDE DO DEGRAU DA ESCADA DA 25.1.
 *
 * A secao 8 registra sete reguas que quebraram por procurar o rotulo de UM
 * degrau; entao o rotulo mora aqui, numa funcao so, e o degrau viaja ao lado
 * como informacao — nunca como critério de regua.
 */
if ( ! function_exists( 'rodametria_casca_rotulo_da_loja' ) ) {
function rodametria_casca_rotulo_da_loja( $programa, $degrau ) {
	$loja = ( 'mercado_livre' === $programa || 'mercadolivre' === $programa )
		? 'Mercado Livre' : 'Shopee';

	return ( (int) $degrau >= 4 ) ? 'Ver ofertas na ' . $loja : 'Ver na ' . $loja;
}
}

/**
 * O CARTAO DE COMPRA (32.1, item 5). Foto, marca e modelo, a especificacao que
 * fez o produto entrar, preco com data da coleta, botao de loja.
 *
 * Produto SEM imagem nao some do resultado: aparece com espaco reservado neutro
 * (secao 6 — "perder a recomendacao tecnica certa por falta de foto e trocar o
 * certo pelo bonito"). Hoje nenhum registro desta ilha tem foto, e e por isso
 * que o espaco reservado nasce junto com o cartao, em vez de depois.
 *
 * Preco NUNCA e cravado como atual (secao 7): ou nao sai, ou sai com a data da
 * coleta ao lado.
 */
if ( ! function_exists( 'rodametria_casca_cartao_de_compra' ) ) {
function rodametria_casca_cartao_de_compra( $item ) {
	$url = isset( $item['url'] ) ? $item['url'] : '';
	if ( '' === $url ) {
		return '';
	}
	$rotulo = rodametria_casca_rotulo_da_loja(
		isset( $item['programa'] ) ? $item['programa'] : '',
		isset( $item['degrau'] ) ? $item['degrau'] : 0 );

	$html = '<li class="rdm-molde-cartao">';

	if ( ! empty( $item['imagem']['url'] ) ) {
		$img = $item['imagem'];
		$html .= '<img class="rdm-molde-cartao-foto" src="' . esc_url( $img['url'] ) . '"'
			. ' width="' . (int) ( isset( $img['largura'] ) ? $img['largura'] : 320 ) . '"'
			. ' height="' . (int) ( isset( $img['altura'] ) ? $img['altura'] : 320 ) . '"'
			. ' loading="lazy" decoding="async"'
			. ' alt="' . esc_attr( isset( $img['alt'] ) ? $img['alt'] : $item['nome'] ) . '">';
	} else {
		$html .= '<span class="rdm-molde-cartao-sem-foto" aria-hidden="true"></span>';
	}

	$html .= '<p class="rdm-molde-cartao-nome">' . esc_html( $item['nome'] ) . '</p>';

	if ( ! empty( $item['especificacao'] ) ) {
		$html .= '<p class="rdm-molde-cartao-spec">' . esc_html( $item['especificacao'] ) . '</p>';
	}
	if ( ! empty( $item['preco'] ) ) {
		$html .= '<p class="rdm-molde-cartao-preco"><span class="rdm-num">'
			. esc_html( $item['preco'] ) . '</span>'
			. ( empty( $item['preco_nota'] ) ? '' :
				' <span class="rdm-molde-cartao-preco-nota">' . esc_html( $item['preco_nota'] ) . '</span>' )
			. '</p>';
	}

	$html .= '<a class="rdm-molde-cartao-botao" href="' . esc_url( $url ) . '"'
		. ' rel="sponsored noopener" target="_blank">' . esc_html( $rotulo ) . '</a>';
	$html .= '</li>';

	return $html;
}
}

/**
 * O BLOCO DE COMPRA inteiro (32.1, item 5): carrossel horizontal de cartoes com
 * scroll-snap em CSS puro, mais o aviso de comissao em uma linha.
 *
 * A 32.5 mede o PRIMEIRO BOTAO DE COMPRA antes de 1.400 px, e a secao 7 proibe
 * bloco vazio: "nenhum item fica sem saida de compra". Quando a lista chega
 * vazia este componente NAO imprime silencio — imprime a causa que a pagina
 * mediu, que e a outra metade da mesma secao 7.
 */
if ( ! function_exists( 'rodametria_casca_bloco_de_compra' ) ) {
function rodametria_casca_bloco_de_compra( $titulo, $itens, $frase_de_escopo, $causa_se_vazio = '' ) {
	$html = '<section class="rdm-molde-compra" id="comprar">';
	$html .= '<h2 class="rdm-molde-compra-titulo">' . esc_html( $titulo ) . '</h2>';
	$html .= '<p class="rdm-molde-compra-escopo">' . esc_html( $frase_de_escopo ) . '</p>';

	$cartoes = '';
	foreach ( (array) $itens as $item ) {
		$cartoes .= rodametria_casca_cartao_de_compra( $item );
	}

	if ( '' === $cartoes ) {
		$html .= '<p class="rdm-molde-compra-vazio">' . esc_html( $causa_se_vazio ) . '</p>';
	} else {
		$html .= '<ul class="rdm-molde-carrossel">' . $cartoes . '</ul>';
		$html .= '<p class="rdm-molde-compra-comissao">Link de afiliado: a gente recebe '
			. 'comissão da loja se você comprar, e o preço para você é o mesmo.</p>';
	}

	$html .= '</section>';

	return $html;
}
}

/**
 * A BARRA FIXA DO RODAPE NO CELULAR (32.1, ultima linha): numero do resultado e
 * botao para o bloco de compra, aparecendo quando o bloco de compra esta fora
 * da tela. Quem a mostra e a esconde e o JS do wp_footer; ela nasce escondida
 * para quem esta sem JavaScript nao receber barra que nao fecha.
 */
if ( ! function_exists( 'rodametria_casca_barra_fixa' ) ) {
function rodametria_casca_barra_fixa( $rotulo, $numero, $unidade ) {
	return '<div class="rdm-molde-barra" data-rdm-barra hidden>'
		. '<span class="rdm-molde-barra-num"><span class="rdm-molde-barra-rotulo">'
		. esc_html( $rotulo ) . '</span> <span class="rdm-num" data-rdm-barra-numero>'
		. esc_html( $numero ) . '</span> <span>' . esc_html( $unidade ) . '</span></span>'
		. '<a class="rdm-molde-barra-botao" href="#comprar">Ver produtos</a></div>';
}
}

/* ===========================================================================
 * 7. A FOLHA — tokens do DESIGN.md e o molde
 *
 * Sai no wp_head porque e folha de estilo, nao script, e porque folha no rodape
 * pisca a pagina crua antes de pintar. O que a secao 8 proibe no rodape e JS e
 * CSS DENTRO do retorno do shortcode — isto nao esta dentro de shortcode
 * nenhum.
 * ======================================================================== */

add_action( 'wp_head', function () {
	?>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Barlow:wght@400;600&family=Barlow+Semi+Condensed:wght@700&family=JetBrains+Mono:wght@500&display=swap">
<style id="rodametria-casca">
:root{
  --rdm-tinta:#13212B; --rdm-verde:#0A6B4C; --rdm-verde-claro:#3FC08E;
  --rdm-alerta:#8F4A00; --rdm-legenda:#4A5A66; --rdm-piso:#F6F8F7;
  --rdm-superficie:#FFFFFF; --rdm-traco:#D3DAD7;
  --rdm-verde-fundo:#E8F3EE; --rdm-alerta-fundo:#FBF1E6;
  --rdm-e1:4px; --rdm-e2:8px; --rdm-e3:12px; --rdm-e4:16px;
  --rdm-e5:24px; --rdm-e6:32px; --rdm-e7:48px; --rdm-e8:64px;
}
html{-webkit-text-size-adjust:100%}
body.rdm{margin:0;background:var(--rdm-piso);color:var(--rdm-tinta);
  font-family:Barlow,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:1.0625rem;line-height:1.6}
body.rdm *{box-sizing:border-box}
body.rdm img{max-width:100%;height:auto}
.rdm-faixa{max-width:960px;margin:0 auto;padding:0 16px}
body.rdm h1,body.rdm h2,body.rdm h3{font-family:"Barlow Semi Condensed",Barlow,sans-serif;
  font-weight:700;line-height:1.18;margin:0 0 var(--rdm-e3)}
body.rdm h1{font-size:2.25rem}
body.rdm h2{font-size:1.75rem;margin-top:var(--rdm-e6)}
body.rdm h3{font-size:1.25rem;margin-top:var(--rdm-e5)}
body.rdm p{margin:0 0 var(--rdm-e4);max-width:68ch}
.rdm-num,body.rdm .rdm-num{font-family:"JetBrains Mono",ui-monospace,monospace;
  font-weight:500;font-variant-numeric:tabular-nums}
body.rdm a{color:var(--rdm-verde);text-underline-offset:2px}
body.rdm a:focus-visible,body.rdm button:focus-visible,body.rdm summary:focus-visible,
body.rdm select:focus-visible,body.rdm input:focus-visible{outline:2px solid var(--rdm-verde);outline-offset:2px}

/* cabecalho e marca */
.rdm-cabecalho{background:var(--rdm-superficie);border-bottom:1px solid var(--rdm-traco)}
.rdm-cabecalho .rdm-faixa{display:flex;align-items:center;justify-content:space-between;
  gap:var(--rdm-e4);min-height:72px}
.rdm-marca{display:inline-flex;align-items:center;gap:var(--rdm-e3);text-decoration:none;color:inherit}
.rdm-marca .rdm-simbolo{display:block;flex:0 0 auto}
.rdm-marca-texto{display:flex;flex-direction:column;gap:2px}
.rdm-marca-nome{font-family:"Alfa Slab One",Georgia,serif;font-size:1.25rem;letter-spacing:.01em;line-height:1}
.rdm-marca-linha{font-family:Barlow,sans-serif;font-weight:600;font-size:.6875rem;
  text-transform:uppercase;letter-spacing:.32em;color:var(--rdm-legenda);
  border-top:2px solid var(--rdm-traco);border-bottom:2px solid var(--rdm-traco);padding:2px 0}
.rdm-marca-negativa{color:#FFF}
.rdm-marca-negativa .rdm-marca-linha{color:#FFF;border-color:rgba(255,255,255,.45)}

/* menu */
.rdm-nav-botao{display:none;align-items:center;gap:var(--rdm-e2);background:none;
  border:1px solid var(--rdm-traco);border-radius:var(--rdm-e1);padding:8px 12px;
  font:600 .9375rem Barlow,sans-serif;color:var(--rdm-tinta);cursor:pointer}
.rdm-nav-barras{display:inline-block;width:16px;height:2px;background:var(--rdm-tinta);
  box-shadow:0 5px 0 var(--rdm-tinta),0 -5px 0 var(--rdm-tinta)}
.rdm-nav-lista{display:flex;gap:var(--rdm-e5);list-style:none;margin:0;padding:0}
.rdm-nav-lista a{font-weight:600;font-size:.9375rem;color:var(--rdm-tinta);text-decoration:none}
.rdm-nav-lista a:hover,.rdm-nav-lista a[aria-current=page]{text-decoration:underline;
  text-decoration-color:var(--rdm-verde);text-decoration-thickness:2px}

/* trilha */
.rdm-trilha{margin:var(--rdm-e4) 0 var(--rdm-e3)}
.rdm-trilha ol{display:flex;flex-wrap:wrap;gap:var(--rdm-e2);list-style:none;margin:0;padding:0;
  font-size:.8125rem;color:var(--rdm-legenda)}
.rdm-trilha li+li::before{content:"›";margin-right:var(--rdm-e2);color:var(--rdm-traco)}
.rdm-trilha a{color:var(--rdm-legenda)}

/* conteudo */
.rdm-pagina{padding:var(--rdm-e2) 0 var(--rdm-e8)}
.rdm-promessa{font-size:1.125rem;color:var(--rdm-legenda);margin-bottom:var(--rdm-e5)}

/* formulario de ferramenta */
.rdm-f-formulario{background:var(--rdm-superficie);border:1px solid var(--rdm-traco);
  border-radius:var(--rdm-e2);padding:var(--rdm-e4);margin:0 0 var(--rdm-e4)}
.rdm-f-campos{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:var(--rdm-e3)}
.rdm-f-campo{display:flex;flex-direction:column;gap:var(--rdm-e1)}
.rdm-f-campo label{font-weight:600;font-size:.875rem}
.rdm-f-campo select,.rdm-f-campo input{font:500 1rem "JetBrains Mono",ui-monospace,monospace;
  padding:9px 10px;border:1px solid var(--rdm-traco);border-radius:var(--rdm-e1);
  background:var(--rdm-superficie);color:var(--rdm-tinta);width:100%}
.rdm-f-campo .rdm-f-dica{font-family:Barlow,sans-serif;font-size:.75rem;color:var(--rdm-legenda)}
.rdm-f-acao{margin-top:var(--rdm-e3)}
.rdm-f-botao{background:var(--rdm-tinta);color:#FFF;border:0;border-radius:var(--rdm-e1);
  padding:12px 20px;font:600 1rem Barlow,sans-serif;cursor:pointer}

/* MOLDE: caixa de resultado */
.rdm-molde-caixa{background:var(--rdm-superficie);border:2px solid var(--rdm-traco);
  border-radius:var(--rdm-e2);padding:var(--rdm-e4);margin:0 0 var(--rdm-e4)}
.rdm-molde-caixa-verde{border-color:var(--rdm-verde);background:var(--rdm-verde-fundo)}
.rdm-molde-caixa-alerta{border-color:var(--rdm-alerta);background:var(--rdm-alerta-fundo)}
.rdm-molde-caixa-rotulo{font-size:.8125rem;text-transform:uppercase;letter-spacing:.08em;
  color:var(--rdm-legenda);margin:0 0 var(--rdm-e1)}
.rdm-molde-caixa-numero{font-size:2.25rem;line-height:1.1;margin:0 0 var(--rdm-e3)}
.rdm-molde-caixa-unidade{font-size:1.25rem;color:var(--rdm-legenda)}
.rdm-molde-caixa-frase{margin:0 0 var(--rdm-e2)}
.rdm-molde-caixa-frase:last-child{margin-bottom:0}

/* MOLDE: bloco de compra e carrossel */
.rdm-molde-compra{margin:0 0 var(--rdm-e5)}
.rdm-molde-compra-titulo{font-size:1.25rem;margin:0 0 var(--rdm-e2)}
.rdm-molde-compra-escopo{color:var(--rdm-legenda);font-size:.9375rem;margin:0 0 var(--rdm-e3)}
.rdm-molde-compra-vazio{color:var(--rdm-legenda);font-size:.9375rem;border-left:3px solid var(--rdm-traco);
  padding-left:var(--rdm-e3);margin:0}
.rdm-molde-compra-comissao{font-size:.8125rem;color:var(--rdm-legenda);margin:var(--rdm-e3) 0 0}
.rdm-molde-carrossel{display:flex;gap:var(--rdm-e3);list-style:none;margin:0;padding:0 0 var(--rdm-e2);
  overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}
.rdm-molde-cartao{flex:0 0 232px;scroll-snap-align:start;background:var(--rdm-superficie);
  border:1px solid var(--rdm-traco);border-radius:var(--rdm-e2);padding:var(--rdm-e3);
  display:flex;flex-direction:column;gap:var(--rdm-e2)}
.rdm-molde-cartao-foto,.rdm-molde-cartao-sem-foto{display:block;width:100%;height:120px;
  object-fit:contain;background:var(--rdm-piso);border-radius:var(--rdm-e1)}
.rdm-molde-cartao-nome{font-weight:600;font-size:.9375rem;margin:0;line-height:1.3}
.rdm-molde-cartao-spec{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.75rem;
  color:var(--rdm-legenda);margin:0}
.rdm-molde-cartao-preco{font-size:1rem;margin:0}
.rdm-molde-cartao-preco-nota{font-family:Barlow,sans-serif;font-size:.6875rem;color:var(--rdm-legenda)}
.rdm-molde-cartao-botao{margin-top:auto;display:block;text-align:center;background:var(--rdm-tinta);
  color:#FFF;text-decoration:none;border-radius:var(--rdm-e1);padding:10px 12px;
  font-weight:600;font-size:.9375rem}

/* MOLDE: tabela pre-renderizada, visivel e nunca recolhida (32.1 item 6) */
.rdm-tabela-rolagem{overflow-x:auto;margin:0 0 var(--rdm-e4)}
.rdm-tabela{border-collapse:collapse;width:100%;background:var(--rdm-superficie);font-size:.9375rem}
.rdm-tabela caption{text-align:left;font-size:.8125rem;color:var(--rdm-legenda);padding:0 0 var(--rdm-e2)}
.rdm-tabela th,.rdm-tabela td{border:1px solid var(--rdm-traco);padding:8px 10px;text-align:left;
  vertical-align:top}
.rdm-tabela thead th{font-family:"Barlow Semi Condensed",sans-serif;font-size:.875rem;
  background:var(--rdm-piso)}
.rdm-tabela td.rdm-num,.rdm-tabela th.rdm-num{text-align:right;white-space:nowrap}

/* MOLDE: dobra */
.rdm-molde-dobra{background:var(--rdm-superficie);border:1px solid var(--rdm-traco);
  border-radius:var(--rdm-e2);margin:0 0 var(--rdm-e3)}
.rdm-molde-dobra>summary{cursor:pointer;padding:var(--rdm-e3) var(--rdm-e4);
  font-family:"Barlow Semi Condensed",sans-serif;font-weight:700;font-size:1.125rem;
  list-style:none;display:flex;align-items:center;gap:var(--rdm-e2)}
.rdm-molde-dobra>summary::-webkit-details-marker{display:none}
.rdm-molde-dobra>summary::before{content:"+";font-family:"JetBrains Mono",monospace;
  color:var(--rdm-verde);font-size:1.125rem}
.rdm-molde-dobra[open]>summary::before{content:"–"}
.rdm-molde-dobra-corpo{padding:0 var(--rdm-e4) var(--rdm-e4)}
.rdm-molde-dobra-corpo>:last-child{margin-bottom:0}

/* MOLDE: barra fixa do celular */
.rdm-molde-barra{display:none}

/* grupos de prestacao de contas (secao 7) */
.rdm-contas{list-style:none;margin:0 0 var(--rdm-e4);padding:0}
.rdm-contas>li{border-left:3px solid var(--rdm-traco);padding:0 0 0 var(--rdm-e3);
  margin:0 0 var(--rdm-e3)}
.rdm-contas b{font-family:"Barlow Semi Condensed",sans-serif}
.rdm-fonte{font-size:.8125rem;color:var(--rdm-legenda)}
.rdm-fonte a{color:var(--rdm-legenda)}

/* cartoes da home */
.rdm-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));
  gap:var(--rdm-e3);list-style:none;margin:0 0 var(--rdm-e5);padding:0}
.rdm-cartoes>li{background:var(--rdm-superficie);border:1px solid var(--rdm-traco);
  border-radius:var(--rdm-e2);padding:var(--rdm-e4)}
.rdm-cartoes h3{margin:0 0 var(--rdm-e2);font-size:1.125rem}
.rdm-cartoes p{font-size:.9375rem;margin:0 0 var(--rdm-e3)}
.rdm-cartao-estado{font-size:.8125rem;color:var(--rdm-legenda);margin:0}

/* rodape */
.rdm-rodape{background:var(--rdm-tinta);color:#FFF;margin-top:var(--rdm-e8);
  padding:var(--rdm-e6) 0 var(--rdm-e5)}
.rdm-rodape-links{display:flex;flex-wrap:wrap;gap:var(--rdm-e4);list-style:none;
  margin:var(--rdm-e4) 0;padding:0;font-size:.9375rem}
.rdm-rodape a{color:var(--rdm-verde-claro)}
.rdm-rodape-aviso,.rdm-rodape-creditos{color:rgba(255,255,255,.82);font-size:.8125rem;max-width:68ch}

@media (max-width:719px){
  body.rdm{font-size:1.0625rem}
  body.rdm h1{font-size:1.75rem}
  body.rdm h2{font-size:1.375rem;margin-top:var(--rdm-e5)}
  .rdm-cabecalho .rdm-faixa{min-height:60px;flex-wrap:wrap}
  .rdm-marca-linha{display:none}
  .rdm-marca-nome{font-size:1.0625rem}
  .rdm-nav-botao{display:inline-flex}
  .rdm-nav-lista{display:none;flex-direction:column;gap:0;width:100%;
    border-top:1px solid var(--rdm-traco);margin:0 0 var(--rdm-e2)}
  .rdm-nav-lista>li{border-bottom:1px solid var(--rdm-traco)}
  .rdm-nav-lista a{display:block;padding:12px 0}
  .rdm-nav[data-aberto="1"] .rdm-nav-lista{display:flex}
  .rdm-f-campos{grid-template-columns:1fr 1fr}
  .rdm-molde-caixa-numero{font-size:1.75rem}
  /* 32.5-c: a regra de telefone do molde alcanca TODA familia de cartao por
     seletor, e por isso ela mira a classe do MOLDE e nunca a de uma
     ferramenta. Cartao de 232 px no telefone de 390 px deixa a borda do
     seguinte visivel, que e o que convida a arrastar. */
  .rdm-molde-cartao{flex-basis:200px}
  .rdm-molde-cartao-foto,.rdm-molde-cartao-sem-foto{height:96px}
  .rdm-molde-barra{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:40;
    align-items:center;justify-content:space-between;gap:var(--rdm-e3);
    background:var(--rdm-superficie);border-top:1px solid var(--rdm-traco);
    padding:10px 16px;box-shadow:0 -2px 8px rgba(19,33,43,.08)}
  .rdm-molde-barra[hidden]{display:none}
  .rdm-molde-barra-num{font-size:1.125rem}
  .rdm-molde-barra-rotulo{font-family:Barlow,sans-serif;font-size:.75rem;
    color:var(--rdm-legenda);display:block}
  .rdm-molde-barra-botao{background:var(--rdm-tinta);color:#FFF;text-decoration:none;
    border-radius:var(--rdm-e1);padding:10px 14px;font-weight:600;font-size:.9375rem;
    white-space:nowrap}
  body.rdm.rdm-com-barra{padding-bottom:72px}
}
@media (prefers-reduced-motion:reduce){body.rdm *{scroll-behavior:auto!important}}
</style>
	<?php
}, 8 );

add_filter( 'body_class', function ( $c ) {
	$c[] = 'rdm';

	return $c;
} );

/* ===========================================================================
 * 8. O JS DA CASCA — menu e barra fixa. NO RODAPE, SEMPRE.
 *
 * A secao 8 do contrato: "JS e CSS NUNCA vao dentro do que o shortcode
 * retorna — vao no wp_footer. O WordPress roda os filtros do the_content sobre
 * o retorno e converte o E-comercial duplo em entidade HTML, matando o script
 * inteiro. Foi o defeito que derrubou 5 calculadoras da Aquametria em
 * 08/09/2026."
 * ======================================================================== */

add_action( 'wp_footer', function () {
	?>
<script id="rodametria-casca-js">
(function(){
  var nav = document.querySelector('.rdm-nav');
  if (nav) {
    var botao = nav.querySelector('.rdm-nav-botao');
    if (botao) {
      botao.addEventListener('click', function(){
        var aberto = nav.getAttribute('data-aberto') === '1';
        nav.setAttribute('data-aberto', aberto ? '0' : '1');
        botao.setAttribute('aria-expanded', aberto ? 'false' : 'true');
      });
    }
  }

  var barra = document.querySelector('[data-rdm-barra]');
  var compra = document.getElementById('comprar');
  if (barra && compra) {
    document.body.classList.add('rdm-com-barra');
    var mostrar = function(visivel){
      if (visivel) { barra.removeAttribute('hidden'); }
      else { barra.setAttribute('hidden',''); }
    };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function(entradas){
        entradas.forEach(function(e){ mostrar(!e.isIntersecting); });
      }, {threshold: 0.05}).observe(compra);
    } else {
      mostrar(true);
    }
  }
})();
</script>
	<?php
}, 30 );

/* ===========================================================================
 * 9. HIGIENE DO TEMA
 *
 * O que sai: emoji (requisicao extra e nenhum emoji nesta ilha), o bloco de
 * comentario do tema nas paginas, e o feed de comentarios. Nada aqui mexe em
 * robots, sitemap ou canonica — a porta de entrada da secao 29 e do WordPress e
 * continua sendo dele.
 * ======================================================================== */

remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
add_filter( 'comments_open', function ( $aberto, $id ) {
	return is_page() ? false : $aberto;
}, 10, 2 );

/* ===========================================================================
 * 9-b. O SITEMAP E CURADORIA, NAO INVENTARIO (14.1)
 *
 * Medido no ar as 10h5xZ de 29/10/2026, na primeira passada do portao de ar:
 * o wp-sitemap.xml desta ilha publicava SEIS URLs e QUATRO delas eram lixo de
 * fabrica do WordPress — /2026/10/27/hello-world/, /sample-page/,
 * /category/uncategorized/ e /author/rodametria_gestor/ — contra as duas que a
 * ilha tem de verdade. A 14.1 e literal: "dominio novo tem orcamento de
 * rastreamento minusculo. Cada URL fraca gasta orcamento que uma pagina boa
 * precisaria, e ainda ensina ao Google que este site produz coisa que nao vale
 * voltar para buscar. O sitemap e curadoria, nao inventario".
 *
 * Duas coisas, e as duas sao conservadoras:
 *   (a) "Hello world!" e "Sample Page" vao para a LIXEIRA, nunca apagados —
 *       e a mesma decisao da casca da Robometria, e por isso o mesmo metodo:
 *       casa por slug E por titulo, nas duas linguas, e pula qualquer pagina
 *       que seja a home ou que a propria casca tenha criado.
 *   (b) os provedores de sitemap de AUTOR e de TAXONOMIA saem. Arquivo de autor
 *       e de categoria numa ilha de ferramenta nao e pagina de verdade: lista
 *       o que ja esta listado e nasce fina, que e o que a 14.4 recusa. Quando
 *       esta ilha tiver artigo (bloco 5 da fila), quem volta e o provedor de
 *       POST — nunca o de autor.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_limpar_padrao' ) ) {
function rodametria_casca_limpar_padrao() {
	$relato = array();
	$slugs   = array( 'hello-world', 'ola-mundo', 'sample-page',
		'pagina-exemplo', 'pagina-de-exemplo' );
	$titulos = array( 'Hello world!', 'Olá, mundo!', 'Ola, mundo!', 'Sample Page',
		'Página de exemplo', 'Pagina de exemplo' );

	$candidatos = get_posts( array(
		'post_type'        => array( 'post', 'page' ),
		'post_status'      => array( 'publish', 'draft', 'pending', 'private', 'future' ),
		'numberposts'      => 40,
		'orderby'          => 'ID',
		'order'            => 'ASC',
		'suppress_filters' => true,
	) );

	foreach ( $candidatos as $p ) {
		if ( get_post_meta( $p->ID, '_rodametria_id', true ) ) {
			continue;
		}
		if ( (int) get_option( 'page_on_front' ) === (int) $p->ID ) {
			continue;
		}
		if ( ! in_array( $p->post_name, $slugs, true )
			&& ! in_array( trim( $p->post_title ), $titulos, true ) ) {
			continue;
		}
		wp_trash_post( $p->ID );
		$relato[] = 'lixeira: ' . $p->post_type . ' #' . $p->ID . ' (' . $p->post_name . ')';
	}

	return $relato;
}
}

add_filter( 'wp_sitemaps_add_provider', function ( $provedor, $nome ) {
	if ( in_array( $nome, array( 'users', 'taxonomies' ), true ) ) {
		return false;
	}

	return $provedor;
}, 10, 2 );

/* ===========================================================================
 * 10. A HOME
 *
 * O VOZ.md manda: "Sem manifesto, sem 'bem-vindo', sem parágrafo explicando o
 * que é o site". E manda que a ferramenta principal seja a F1 ("Esse elétrico
 * precisa de CNH?").
 *
 * E A DIVERGENCIA DESTE BLOCO, escrita aqui porque e decisao e nao esquecimento:
 * a F1 NAO PODE IR AO AR. O limiar legal dela (`limiares-categoria-contran-996
 * -2023`) esta `pendente`, porque o texto oficial da resolucao nao abre nesta
 * nuvem — cinco dominios oficiais medidos em 403 de egresso em 28/10 e
 * remedidos em 29/10. Pela secao 10 do contrato a ilha nunca inventa dado, e
 * uma home que FAZ a pergunta do titulo e nao a responde seria pior do que
 * nenhuma home. Entao a home nasce HUB: a caixa de resposta no topo diz o que a
 * ilha mede, os cartoes levam para a pergunta que JA tem resposta, e a que
 * ainda nao tem diz com uma linha o que falta, sem prometer data.
 *
 * No dia em que a resolucao for lida, a F1 toma a primeira tela da home e os
 * cartoes descem — e NENHUMA URL muda, que e o que a 32.3 protege.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_home_html' ) ) {
function rodametria_casca_home_html() {
	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= '<h1>Os três números antes de comprar um elétrico</h1>';
	$html .= '<p class="rdm-promessa">Precisa de CNH? Faz quantos km de verdade com o seu peso? '
		. 'Aguenta você e a mochila? O anúncio não responde nenhuma das três direito. Aqui a gente '
		. 'responde com a conta na mesa e a ficha citada.</p>';

	/* Caixa de resposta no topo (32.2), e o numero dela e CONTADO do banco,
	   nunca digitado — a regra do numero de tela da secao 8. */
	$dados = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );
	$n_tabela = 0;
	$n_vitrine = 0;
	if ( $dados ) {
		$n_tabela  = (int) $dados['tabela']['total_do_banco'] + (int) $dados['tabela']['total_externas'];
		$n_vitrine = count( $dados['compra']['vitrine'] );
	}

	$html .= rodametria_casca_caixa(
		'Pronto para usar agora',
		'1',
		'de 3 ferramentas',
		array(
			'A conta de autonomia está no ar: você diz a tensão e a amperagem da bateria e ela '
				. 'devolve os watt-hora e a faixa de km que dá para esperar no seu relevo.',
			'As outras duas — a de CNH e a de carga máxima — estão esperando dado, e cada cartão '
				. 'abaixo diz exatamente o quê.',
		),
		'neutro' );

	/* Os cartoes, na linguagem de quem pilota (VOZ.md). Pagina que nao existe
	   nao ganha link: o cartao diz o que falta, e nao promete data. */
	$f2 = rodametria_casca_url_do_slug( 'autonomia-patinete-eletrico' );

	$html .= '<h2>As três perguntas</h2>';
	$html .= '<ul class="rdm-cartoes">';

	$html .= '<li><h3>Quantos km ele faz com o seu peso?</h3>'
		. '<p>Tensão e amperagem da bateria entram, watt-hora e a faixa de km saem — com o relevo '
		. 'do seu trajeto descontando o que tem de descontar.</p>'
		. ( '' === $f2
			? '<p class="rdm-cartao-estado">Está sendo publicada agora.</p>'
			: '<p><a class="rdm-molde-cartao-botao" href="' . esc_url( $f2 ) . '">Calcular a autonomia</a></p>' )
		. '</li>';

	$html .= '<li><h3>Esse elétrico precisa de CNH?</h3>'
		. '<p>Potência, velocidade máxima e se tem acelerador decidem se o veículo é bicicleta '
		. 'elétrica, autopropelido ou ciclomotor — e só o último exige habilitação e placa.</p>'
		. '<p class="rdm-cartao-estado">Ainda não está no ar, e o motivo é um só: o texto oficial '
		. 'da resolução que fixa os limites não abre pelo nosso canal de leitura. A gente não vai '
		. 'publicar limite de potência tirado de notícia — errar para o lado permissivo manda '
		. 'alguém para a rua sem habilitação.</p></li>';

	$html .= '<li><h3>Aguenta você e a mochila?</h3>'
		. '<p>Peso de quem pilota mais a carga, contra a carga máxima que o fabricante declara, '
		. 'com folga — e os que ficam de fora dizem por quê.</p>'
		. '<p class="rdm-cartao-estado">Ainda não está no ar: das fichas que colhemos, só três '
		. 'declaram carga máxima, e nenhuma dessas três tem oferta aberta. Sem ficha que declare o '
		. 'limite, a conta não teria o que comparar.</p></li>';

	$html .= '</ul>';

	if ( $dados ) {
		$html .= '<h2>O que a gente já mediu</h2>';
		$html .= '<p>A Rodametria não copia número de anúncio: cada campo entra no nosso banco com a '
			. 'ficha de onde saiu e a data da leitura, e campo que a ficha não declara fica vazio em '
			. 'vez de ser preenchido por estimativa. Hoje o banco tem '
			. '<span class="rdm-num">' . (int) $dados['compra']['total_registros_veiculos'] . '</span> '
			. 'veículos colhidos, <span class="rdm-num">' . (int) $n_vitrine . '</span> deles com oferta '
			. 'aberta e rastreável, e <span class="rdm-num">' . (int) $n_tabela . '</span> combinações de '
			. 'bateria já calculadas na conta de autonomia.</p>';
		$html .= '<p>O que ainda falta está dito em cada página, com a causa: é assim que a gente '
			. 'separa “não sabemos” de “não existe”.</p>';
	}

	$html .= '</div>';

	return $html;
}
}

/**
 * Leitura do banco que o Sync gravou. UM lugar so le a option, e o nome dela
 * segue o padrao do Sync desta ilha (rodametria_dados_<id com _>).
 *
 * Quando a option nao existe a funcao devolve null, e quem a chama imprime
 * pagina DEGRADADA e honesta em vez de pagina com molde cru. A cicatriz esta na
 * secao 8: "nao carregava nas options o que o Sync carrega, entao cada pagina
 * caia no aviso de 'estamos sem o banco' — que e uma pagina valida".
 */
if ( ! function_exists( 'rodametria_casca_banco' ) ) {
function rodametria_casca_banco( $id ) {
	$valor = get_option( 'rodametria_dados_' . sanitize_key( $id ) );
	if ( ! is_array( $valor ) ) {
		return null;
	}

	return $valor;
}
}

add_shortcode( 'rodametria_home', 'rodametria_casca_home_html' );

/* ===========================================================================
 * 11. CRIACAO DAS PAGINAS DA CASCA
 *
 * A home e a UNICA pagina que esta casca cria. Cada ferramenta cria a propria,
 * de dentro do snippet dela, pelo mesmo metodo — e o motivo e o da 32.6-b: a
 * casca nao cresce quando a ilha cresce.
 *
 * O WordPress NAO garante o slug pedido: se outra pagina ja ocupa o post_name
 * ele acrescenta "-2" sem avisar. Por isso a funcao devolve o slug REAL e quem
 * a chama compara. Foi assim que o hub da Robometria passou a apontar para uma
 * URL que dava 404, em 08/09/2026.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_garantir_pagina' ) ) {
function rodametria_casca_garantir_pagina( $slug, $titulo, $conteudo ) {
	$existente = get_posts( array(
		'post_type'   => 'page',
		'post_status' => array( 'publish', 'draft', 'pending', 'private' ),
		'meta_key'    => '_rodametria_id',
		'meta_value'  => $slug,
		'numberposts' => 1,
	) );

	$dados = array(
		'post_type'    => 'page',
		'post_title'   => $titulo,
		'post_name'    => $slug,
		'post_content' => $conteudo,
		'post_status'  => 'publish',
	);

	if ( $existente ) {
		$dados['ID'] = $existente[0]->ID;
		$pid         = wp_update_post( wp_slash( $dados ), true );
	} else {
		$pid = wp_insert_post( wp_slash( $dados ), true );
	}
	if ( is_wp_error( $pid ) ) {
		return array( 'id' => 0, 'erro' => $pid->get_error_message(), 'slug' => '' );
	}
	update_post_meta( $pid, '_rodametria_id', $slug );

	$slug_real = get_post_field( 'post_name', $pid );

	return array(
		'id'        => (int) $pid,
		'slug'      => $slug_real,
		'slug_ok'   => ( $slug_real === $slug ),
		'permalink' => get_permalink( $pid ),
		'novo'      => empty( $existente ),
	);
}
}

if ( ! function_exists( 'rodametria_casca_instalar' ) ) {
function rodametria_casca_instalar() {
	$relato = array();

	$home = rodametria_casca_garantir_pagina(
		'inicio',
		'Os três números antes de comprar um elétrico',
		'[rodametria_home]' );

	if ( empty( $home['id'] ) ) {
		$relato[] = 'home: ERRO — ' . ( isset( $home['erro'] ) ? $home['erro'] : 'sem id' );

		return $relato;
	}
	$relato[] = 'home: #' . $home['id'] . ' (' . $home['slug'] . ')'
		. ( empty( $home['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );

	if ( 'page' !== get_option( 'show_on_front' ) ) {
		update_option( 'show_on_front', 'page' );
		$relato[] = 'show_on_front: page';
	}
	if ( (int) get_option( 'page_on_front' ) !== (int) $home['id'] ) {
		update_option( 'page_on_front', (int) $home['id'] );
		$relato[] = 'page_on_front: #' . (int) $home['id'];
	}

	/* Cada ferramenta instala a propria pagina aqui, pelo mesmo gancho. */
	$relato = apply_filters( 'rodametria_instalar', $relato );

	/* E so DEPOIS a limpeza, porque ela pula a pagina inicial e precisa que a
	   home ja exista e ja esteja fixada para nao mandar a home para a lixeira. */
	foreach ( rodametria_casca_limpar_padrao() as $linha ) {
		$relato[] = $linha;
	}

	update_option( 'rodametria_casca_instalado', array(
		'versao' => RODAMETRIA_CASCA_VERSAO,
		'em'     => current_time( 'mysql', true ),
		'relato' => $relato,
	), 'no' );

	return $relato;
}
}

/**
 * A instalacao roda uma vez por versao da casca, no `init`, e nao em toda
 * requisicao: wp_insert_post em toda visita e caro e sujo. Trocar
 * RODAMETRIA_CASCA_VERSAO reinstala.
 */
add_action( 'init', function () {
	$feito = get_option( 'rodametria_casca_instalado' );
	if ( is_array( $feito ) && isset( $feito['versao'] ) && RODAMETRIA_CASCA_VERSAO === $feito['versao'] ) {
		return;
	}
	rodametria_casca_instalar();
}, 20 );

/* O /status da ilha ganha a linha da casca, para a verificacao da secao 8 poder
 * ler o que foi instalado sem ninguem precisar entrar no painel. */
add_action( 'rest_api_init', function () {
	register_rest_route( 'rodametria/v1', '/casca', array(
		'methods'             => 'GET',
		'permission_callback' => '__return_true',
		'callback'            => function () {
			$feito = get_option( 'rodametria_casca_instalado' );
			$mapa  = array();
			foreach ( rodametria_casca_paginas() as $slug => $p ) {
				$mapa[ $slug ] = array(
					'nome' => isset( $p['nome'] ) ? $p['nome'] : $slug,
					'url'  => rodametria_casca_url_do_slug( $slug ),
				);
			}

			return array(
				'versao_casca' => RODAMETRIA_CASCA_VERSAO,
				'instalado'    => $feito ? $feito : null,
				'paginas'      => $mapa,
			);
		},
	) );
} );

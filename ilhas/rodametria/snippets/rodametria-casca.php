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

/* 1.9.0 (04/11/2026) — DUAS COISAS, e as duas sao de item de despacho da ronda
   de 04/11.

   (1) A SEGUNDA METADE DA 32.5-d: 24 regras do molde passaram a carregar
   `body.rdm` no seletor. Elas DECLARAVAM margem, respiro e corpo e perdiam, em
   silencio, para `body.rdm p` e `body.rdm h2` — inclusive o bloco de telefone
   inteiro, escrito em 29/10 para comprar pixel e que nunca valeu um pixel.
   Medido: 48 px dentro do cartao, logo acima do botao que a 32.5 mede. O
   comentario longo esta junto das regras, e a trava nasceu na mesma passada
   dentro de `conferir-32-5-no-navegador.mjs`.

   (2) O `dateModified`: a casca passou a servir um no `WebPage` com a data que a
   propria pagina publica, pendurada por FILTRO (`rodametria_data_da_pagina`).
   Antes disto a ilha cujo produto e "o preco de hoje" tinha ZERO ocorrencia de
   `dateModified` e de `datePublished` em todo o JSON-LD das 9 URLs. */
if ( ! defined( 'RODAMETRIA_CASCA_VERSAO' ) ) {
	define( 'RODAMETRIA_CASCA_VERSAO', '1.12.0' );
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
			/* ITENS 5 E 2 DO DESPACHO DE 30/10/2026, NA MESMA FRASE.
			   O 5: tinha 161 caracteres no HTML servido, um acima do teto de 160.
			   O 2: o "com o seu peso" saiu da pergunta de KM, porque a F2 nao faz
			   essa conta. O peso ficou onde ele e de verdade — no "se aguenta
			   voce", que e a F3 e compara carga maxima. 149 agora, contados. */
			/* TROCADA EM 06/11/2026, NO DESEMBARQUE DA F1, E O MOTIVO E DE
			   HONESTIDADE E NAO DE SEO. A frase anterior prometia, em primeiro
			   lugar, *"se precisa de CNH"* — e a F1, que agora OCUPA a primeira
			   tela desta pagina, e literal sobre nao responder isso: a Resolucao
			   996/2023 nao tem artigo nenhum sobre habilitacao, e a pagina diz
			   com todas as letras que nao vai afirmar nem que dispensa nem que
			   exige. Descricao que promete o que a primeira tela recusa e a
			   pagina se desdizendo na propria aba do navegador, e e a mesma
			   familia do item 2 do despacho de 30/10 (*"o peso saiu da promessa
			   porque a F2 nao faz essa conta"*).
			   O que ela promete agora e o que a ferramenta entrega: a CATEGORIA
			   e a PLACA, as duas saindo do texto lido. 147 caracteres, contra o
			   teto de 160 que o portao de ar cobra. */
			'description' => 'Potência, velocidade e acelerador decidem se o seu elétrico é '
				. 'bicicleta, autopropelido ou ciclomotor — e a categoria é o que diz se ele '
				. 'pede placa.',
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

/**
 * A URL de um slug do mapa.
 *
 * A BUSCA E PELA META `_rodametria_id`, E NAO POR CAMINHO. `get_page_by_path()`
 * casa o caminho INTEIRO, entao no dia em que a arvore da 16.1 ganhou um nivel
 * — `/veiculos/patinete-eletrico/` — ele passou a devolver nulo para o slug da
 * filha, e `rodametria_casca_link()` faz link vazio virar texto sem reclamar:
 * a pagina ficaria no ar, orfa, com a mae apontando para texto morto e nenhum
 * portao vermelho. A meta e gravada por `garantir_pagina()` em toda pagina
 * desta ilha e nao muda quando a pagina ganha pai.
 */
if ( ! function_exists( 'rodametria_casca_url_do_slug' ) ) {
function rodametria_casca_url_do_slug( $slug ) {
	if ( 'inicio' === $slug ) {
		return home_url( '/' );
	}
	$achadas = get_posts( array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'meta_key'    => '_rodametria_id',
		'meta_value'  => $slug,
		'numberposts' => 1,
	) );
	if ( $achadas ) {
		return get_permalink( $achadas[0] );
	}
	/* Pagina que exista sem a meta (criada a mao) continua achavel pelo caminho. */
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

/* ---------------------------------------------------------------------------
 * A DATA QUE A PAGINA PUBLICA, PARA A CAMADA QUE O GOOGLE E AS IAs LEEM
 * (item 2 do despacho da ronda de 04/11/2026)
 *
 * O DEFEITO MEDIDO: ZERO ocorrencia de `dateModified` e ZERO de `datePublished`
 * em todo o JSON-LD das 9 URLs desta ilha — numa ilha cujo produto E "o preco
 * de hoje". As paginas diziam a data em PROSA ("os 16 anuncios que a gente
 * conferiu em 04/11/2026") e a camada estruturada nao dizia nada. E a familia da
 * 25.9: **chave ausente nao declara nada**, e aqui a chave ausente era o sinal
 * de frescor da ilha que recoleta preco.
 *
 * POR QUE FILTRO E NAO UM CAMPO DA CASCA: a casca nao sabe, e nao pode saber, de
 * que dado cada pagina e feita. Quem sabe e o snippet que a renderiza — a F2 sai
 * de `f2-respostas.json`, as duas de produto saem da vitrine, as quatro da 16.1
 * saem de `paginas-institucionais.json`. Entao cada snippet PENDURA a sua data
 * neste filtro, pelo proprio slug, como a 20.7 ja faz com a versao do snippet
 * carregado. A casca NAO inventa data: sem ninguem pendurando, o no nao sai, e o
 * portao de ar REPROVA a pagina — o contrario (cair no `date()` do servidor)
 * publicaria "modificada hoje" em pagina que nao muda desde 30/10, que e
 * exatamente a mentira que um sinal de frescor pode contar.
 *
 * E A DATA VEM DO MESMO CAMPO QUE A PROSA USA, nunca de uma segunda declaracao:
 * a licao da 20.7 e literal — "duas declaracoes do mesmo fato comecam iguais e
 * so uma sobe". A pagina da bicicleta diz `colhido_em_br` na tela e serve
 * `colhido_em` no JSON-LD: o mesmo campo, dois formatos.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_casca_data_da_pagina' ) ) {
function rodametria_casca_data_da_pagina( $slug = null ) {
	$slug = ( null === $slug ) ? rodametria_casca_slug_atual() : $slug;
	if ( '' === $slug ) {
		return '';
	}
	$data = apply_filters( 'rodametria_data_da_pagina', '', $slug );
	$data = is_string( $data ) ? trim( $data ) : '';

	/* AAAA-MM-DD ou nada. Data mal formada e pior que data ausente: ela entra no
	   dado estruturado e o buscador a le como quiser. */
	return preg_match( '/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/', $data ) ? $data : '';
}
}

/* A HOME SAI DO MESMO BANCO QUE ELA IMPRIME, e isto esta aqui e nao no snippet
   da F2 porque quem renderiza a home e esta casca: os tres numeros dela — 17
   veiculos colhidos, 5 com oferta aberta, 24 combinacoes de bateria — sao
   contados de `f2-respostas.json`, entao a data da home E a data daquele banco. */
add_filter( 'rodametria_data_da_pagina', function ( $data, $slug ) {
	if ( 'inicio' !== $slug || '' !== $data ) {
		return $data;
	}
	$banco = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );

	return ( $banco && ! empty( $banco['gerado_em'] ) ) ? (string) $banco['gerado_em'] : $data;
}, 10, 2 );

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

	/* O NO DA PAGINA, com a data que ela mesma publica. Sem data declarada ele
	   nao sai: `WebPage` sem `dateModified` nao acrescenta nada ao que o
	   BreadcrumbList e o ItemList ja dizem, e no vazio e ruido. */
	$data = rodametria_casca_data_da_pagina( $slug );
	if ( '' !== $data ) {
		$pagina_ld = array(
			'@context'     => 'https://schema.org',
			'@type'        => 'WebPage',
			'@id'          => rodametria_casca_url_do_slug( $slug ),
			'url'          => rodametria_casca_url_do_slug( $slug ),
			'name'         => isset( $p['nome'] ) ? $p['nome'] : '',
			'inLanguage'   => 'pt-BR',
			'dateModified' => $data,
			'isPartOf'     => array(
				'@type' => 'WebSite',
				'name'  => 'Rodametria',
				'url'   => home_url( '/' ),
			),
		);
		if ( ! empty( $p['description'] ) ) {
			$pagina_ld['description'] = $p['description'];
		}
		echo '<script type="application/ld+json">'
			. wp_json_encode( $pagina_ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
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
if ( ! function_exists( 'rodametria_casca_nome_da_loja' ) ) {
/**
 * O NOME DA LOJA DE UM PROGRAMA, E ELE MORA NUMA FUNCAO SO.
 *
 * Extraido de rodametria_casca_rotulo_da_loja() pelo item 3 do despacho de
 * 30/10/2026: a partir dele o nome da loja e perguntado em DOIS lugares — o
 * rotulo do botao e a nota do preco, que precisa saber se a loja do preco e a
 * mesma do botao. Mapeamento escrito duas vezes e mapeamento que envelhece pela
 * metade no dia em que entrar o terceiro programa.
 */
function rodametria_casca_nome_da_loja( $programa ) {
	return ( 'mercado_livre' === $programa || 'mercadolivre' === $programa )
		? 'Mercado Livre' : 'Shopee';
}
}

if ( ! function_exists( 'rodametria_casca_rotulo_da_loja' ) ) {
function rodametria_casca_rotulo_da_loja( $programa, $degrau ) {
	$loja = rodametria_casca_nome_da_loja( $programa );

	return ( (int) $degrau >= 4 ) ? 'Ver ofertas na ' . $loja : 'Ver na ' . $loja;
}
}

/**
 * O ROTULO DA LINHA DISCRETA DO PISO, numa funcao so pelo mesmo motivo que o
 * rotulo da loja: a frase aparece no CARTAO e, desde 30/10/2026, tambem embaixo
 * da TABELA da vitrine. Duas copias de uma frase sao iguais so no dia em que se
 * escrevem.
 */
if ( ! function_exists( 'rodametria_casca_rotulo_do_piso' ) ) {
function rodametria_casca_rotulo_do_piso() {
	return 'Veja todos disponíveis aqui';
}
}

/**
 * A ESCADA DA 25.2 NA TELA, E ELA MORA AQUI PORQUE E A MESMA NAS DUAS FAMILIAS
 * DE PAGINA DESTA ILHA (a ferramenta e a vitrine de produto).
 *
 * A 25.2 e literal nas duas pontas: a ficha de produto e BONUS e "quando
 * existir e estiver viva, ela vira o botao e a busca desce para a linha
 * discreta"; e "quando nao existir, ou quando a ronda marcar como morta, A
 * BUSCA SOBE E VIRA O BOTAO — sem esperar decisao humana, sem pagina ficar com
 * 'link de loja em breve'".
 *
 * ATE 30/10/2026 SO A PRIMEIRA PONTA ESTAVA NA TELA, e a segunda vivia no
 * CHAMADOR: o gerador da F2 resolvia a escada antes de montar o item, e o
 * cartao desta casca devolvia STRING VAZIA quando a `url` chegava vazia. Para a
 * F2 nunca houve defeito, porque ela nunca entrega item sem resolver; para a
 * VITRINE de produto, que passa `url` crua do dado, o cartao SUMIA da pagina no
 * dia em que a ficha morresse — com o piso da 25.2 gravado no dado, ao lado,
 * sem ninguem para o promover. E a 32.5-c outra vez, e tambem a 32.5-d: a regra
 * alcancava a segunda familia e nunca havia rodado contra o dado que a acionaria,
 * porque os 21 anuncios da vitrine tinham ficha — 21 de 21.
 *
 * ENTAO A REGRA PASSA A SER MECANISMO DO MOLDE, nunca intencao de quem chama:
 * todo chamador entrega os DOIS links crus e esta funcao decide qual sobe.
 *
 * E O DEGRAU SOBE COM A BUSCA, que e a metade que mente se ficar para tras: o
 * rotulo do botao sai de `rodametria_casca_rotulo_da_loja()`, que diz "Ver na
 * Shopee" para ficha e "Ver ofertas na Shopee" para busca. Botao que abre uma
 * PAGINA DE BUSCA dizendo "Ver na Shopee" promete uma ficha que nao existe mais.
 */
if ( ! function_exists( 'rodametria_casca_escada_de_compra' ) ) {
function rodametria_casca_escada_de_compra( $item ) {
	$ficha = isset( $item['url'] ) ? trim( (string) $item['url'] ) : '';
	$busca = isset( $item['url_busca'] ) ? trim( (string) $item['url_busca'] ) : '';

	if ( '' !== $ficha ) {
		/* A ficha vive: ela e o botao, e a busca DESCE — nunca sai. */
		return array(
			'url'        => $ficha,
			'url_busca'  => $busca,
			'degrau'     => isset( $item['degrau'] ) ? (int) $item['degrau'] : 0,
			'piso_subiu' => false,
			'tem_saida'  => true,
		);
	}

	if ( '' !== $busca ) {
		/* A ficha nao existe ou morreu: A BUSCA SOBE E VIRA O BOTAO, e o degrau
		   sobe com ela para 4, que e o degrau do link de busca na 25.1. A linha
		   discreta sai: com a busca NO botao, repeti-la abaixo seria o mesmo
		   link duas vezes no mesmo cartao. */
		return array(
			'url'        => $busca,
			'url_busca'  => '',
			'degrau'     => 4,
			'piso_subiu' => true,
			'tem_saida'  => true,
		);
	}

	/* NEM FICHA NEM BUSCA. Este e o UNICO mundo em que o cartao nao tem saida de
	   compra, e ele e defeito da 19.1 pela 25.2 ("item sem `url_busca` e defeito
	   da 19.1, sempre, em qualquer degrau") — nao um estado que a tela conserta.
	   Quem decide o que fazer com ele e quem chama: o cartao nao se imprime, e a
	   tabela nomeia o anuncio com a celula dizendo que falta a saida, porque a
	   secao 7 manda TODO item do banco ser nomeado uma vez em cada resposta. */
	return array(
		'url'        => '',
		'url_busca'  => '',
		'degrau'     => 0,
		'piso_subiu' => false,
		'tem_saida'  => false,
	);
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
	/* A ESCADA DA 25.2 DECIDE, E ELA ESTA NUMA FUNCAO SO (ver acima). Este
	   cartao NAO escolhe mais o link: ele recebe os dois crus e pergunta.
	   So nao se imprime quando NAO HA SAIDA NENHUMA — nem ficha nem busca —,
	   que pela 25.2 e defeito de banco e nao estado de tela. */
	$escada = rodametria_casca_escada_de_compra( $item );
	if ( ! $escada['tem_saida'] ) {
		return '';
	}
	$url    = $escada['url'];
	$rotulo = rodametria_casca_rotulo_da_loja(
		isset( $item['programa'] ) ? $item['programa'] : '',
		$escada['degrau'] );

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

	/* A OUTRA METADE DA 25.2, e ela e literal: "quando existir e estiver viva,
	   ela vira o botao e a busca desce para a linha discreta `Veja todos
	   disponiveis aqui` logo abaixo". Ficha de produto apodrece — foi assim que
	   quatro dos nove links da clubedomosaico morreram em doze horas — e a busca
	   nao esgota e nao some. Enquanto a ficha vive, ela converte melhor; no dia
	   em que morrer, esta linha e a saida que a pessoa ja tinha na tela.

	   Ela so sai quando ha ficha: com a busca NO botao, repeti-la aqui seria o
	   mesmo link duas vezes no mesmo cartao — e quem decide isso agora e a
	   escada, que zera `url_busca` justamente no mundo em que o piso subiu. */
	if ( '' !== $escada['url_busca'] ) {
		$html .= '<a class="rdm-molde-cartao-todos" href="' . esc_url( $escada['url_busca'] ) . '"'
			. ' rel="sponsored noopener" target="_blank">'
			. esc_html( rodametria_casca_rotulo_do_piso() ) . '</a>';
	}

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

/* ===========================================================================
 * 7-a. A FOLHA SAI SEM OS PROPRIOS COMENTARIOS — UM LUGAR SO, PARA AS TRES
 * FOLHAS DESTA ILHA (bloco 7, 04/11/2026)
 *
 * O DEFEITO, medido no ar as 19h2xZ de 04/11/2026 nas 9 URLs do sitemap: as
 * folhas DESTA ilha serviam 23 comentarios de CSS e 7.486 bytes na home e na
 * F2, 24 e 7.866 nas tres de produto, 24 e 7.827 nas quatro institucionais.
 * Na pagina da F2 isso e 10,6% do CSS que esta ilha escreve e 85,6% de TODOS
 * os bytes de comentario que a pagina serve — os outros 17 sao one-liners do
 * proprio WordPress, de 41 a 103 bytes, que nao sao desta ilha e nao saem
 * daqui. E tres desses comentarios nomeiam uma rotina desta pasta
 * (`conferir-32-5-no-navegador.mjs`), um deles diz `bancada`, e varios trazem
 * numero de secao do contrato e prosa de bastidor — tudo o que a 32.4 proibe.
 *
 * POR QUE NENHUM PORTAO VIA: a regua de bastidor desta ilha e a da ronda leem
 * o TEXTO VISIVEL, e `corpo_da_pagina()` tira `<script>` e `<style>` antes de
 * medir — com razao, porque ali mora CSS e nao prosa. So que a 32.4 nao e
 * sobre o que o leitor VE: e sobre o que a pagina SERVE, e e o fonte que a
 * visao geral de IA ingere.
 *
 * O COMENTARIO FICA NO REPOSITORIO, que e o lugar dele (secao 3) — foi ele que
 * pagou a 32.5-d duas vezes nesta ilha. O que muda e que ele nao sai na folha
 * impressa. E muda EM UM LUGAR, para as tres folhas, porque a 32.5-c e
 * literal: regra que nasce na folha de um snippet e nao viaja para as irmas e
 * a doenca que esta ilha ja pagou.
 *
 * COMO NAO SE QUEBRA CSS TIRANDO COMENTARIO, e isto e a parte dificil: `/*`
 * pode aparecer DENTRO de string (`content:"/* "`) e dentro de `url(...)` sem
 * quote, e um removedor ingenuo corta a declaracao no meio. Entao as strings e
 * as `url()` cruas sao consumidas INTEIRAS pela mesma varredura, antes de
 * qualquer `/*` dentro delas ser visto. As duas travas estao medidas em
 * `ferramentas/teste-folha-sem-comentario.php`, com os mundos FABRICADOS.
 * ======================================================================== */

if ( ! function_exists( 'rodametria_casca_css_sem_comentario' ) ) {
/**
 * Tira os comentarios de uma folha de estilo, sem tocar em mais nada.
 *
 * SAO DUAS PASSADAS, e a primeira existe por um motivo de CSS e nao de gosto:
 * comentario COLADO entre dois caracteres de palavra (`a/*c* /b`) separa dois
 * tokens, e tira-lo como nada colaria os dois num terceiro que ninguem
 * escreveu. Essa passada o troca por UM espaco. A segunda tira todo o resto
 * como nada. Nenhuma folha desta ilha tem o caso colado hoje — a passada
 * existe para o dia em que tiver, e o portao do chao a prova num mundo
 * fabricado.
 *
 * AS DUAS PASSADAS RODAM O MESMO PADRAO, e nele a ordem e o que protege o CSS:
 * string entre aspas e `url(...)` sem quote entram como alternativas e sao
 * devolvidas INTACTAS. E so por consumi-las INTEIRAS que um `/*` dentro delas
 * nunca e lido como comentario — a varredura nunca COMECA dentro de uma
 * string, porque a string ja casou como um pedaco so. `content:"/*"` e
 * `url(data:image/svg+xml;...)` sobrevivem, e as duas estao medidas em
 * `ferramentas/teste-folha-sem-comentario.php`.
 *
 * COMENTARIO SEM FECHAR come o resto da folha, que e exatamente o que o
 * navegador faz. Nao se inventa um fechamento que o autor nao escreveu; o
 * portao do chao reprova folha desta ilha que tenha um.
 */
function rodametria_casca_css_sem_comentario( $css ) {
	$cauda = '|"(?:\\\\.|[^"\\\\])*"'
		. "|'(?:\\\\.|[^'\\\\])*'"
		. '|url\(\s*[^)"\']*\)';

	/* Passada 1: so o comentario COLADO entre dois caracteres de palavra. Os
	   vizinhos entram por lookbehind e lookahead, que nao os consomem — se
	   fossem consumidos, o caractere seguinte sairia da varredura. */
	$css = preg_replace_callback(
		'~(?<=[A-Za-z0-9_-])/\*.*?\*/(?=[A-Za-z0-9_-])' . $cauda . '~s',
		function ( $m ) {
			return ( '/*' === substr( $m[0], 0, 2 ) ) ? ' ' : $m[0];
		},
		(string) $css
	);

	/* Passada 2: todo o resto, inclusive o comentario sem fechar. */
	$css = preg_replace_callback(
		'~/\*.*?\*/|/\*.*$' . $cauda . '~s',
		function ( $m ) {
			return ( '/*' === substr( $m[0], 0, 2 ) ) ? '' : $m[0];
		},
		$css
	);

	/* Linha que ficou vazia, e espaco no fim de linha, sao rastro do
	   comentario e nao CSS. A quebra de linha fica, entao nada se cola. */
	$css = preg_replace( '~[ \t]+$~m', '', $css );
	$css = preg_replace( '~\n[ \t]*(?:\n[ \t]*)+~', "\n", $css );

	return trim( $css, "\n" );
}
}

if ( ! function_exists( 'rodametria_casca_abrir_folha' ) ) {
/**
 * Abre a captura da folha.
 *
 * O CSS continua escrito como HTML cru dentro do snippet — nenhum byte dele
 * muda de lugar no repositorio, e era isso que importava: a folha da casca tem
 * 600 linhas e reescreve-las para trocar QUEM as imprime seria mexer na
 * variavel errada. A captura entrega o texto a funcao acima, e a tag `<style>`
 * passa a ser escrita por ela, em um lugar so, para as tres folhas.
 */
function rodametria_casca_abrir_folha() {
	ob_start();
}
}

if ( ! function_exists( 'rodametria_casca_fechar_folha' ) ) {
/** Fecha a captura e imprime a folha, sem um comentario.
 *
 * CADA FUNCAO EM SEU PROPRIO `if ( ! function_exists() )`, e isto nao e estilo:
 * o `teste-f2.py` mede, no fonte, que toda funcao de nivel superior da casca
 * esta atras de uma guarda — e ele REPROVOU a primeira versao deste bloco, que
 * punha as duas sob a mesma. Guarda compartilhada mente no dia em que uma das
 * duas existir e a outra nao.
 */
function rodametria_casca_fechar_folha( $id ) {
	$css = ob_get_clean();
	echo "\n" . '<style id="' . esc_attr( $id ) . '">' . "\n"
		. rodametria_casca_css_sem_comentario( $css ) . "\n</style>\n";
}
}

add_action( 'wp_head', function () {
	?>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Barlow:wght@400;600&family=Barlow+Semi+Condensed:wght@700&family=JetBrains+Mono:wght@500&display=swap">
<?php rodametria_casca_abrir_folha(); ?>
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
body.rdm .rdm-promessa{font-size:1.125rem;color:var(--rdm-legenda);margin-bottom:var(--rdm-e5)}

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
body.rdm .rdm-f-acao{margin-top:var(--rdm-e3)}
.rdm-f-botao{background:var(--rdm-tinta);color:#FFF;border:0;border-radius:var(--rdm-e1);
  padding:12px 20px;font:600 1rem Barlow,sans-serif;cursor:pointer}

/* O PIVO DA F1 — um par de radios no MESMO NIVEL VISUAL dos dois numeros.
   A 1.1 da especificacao e literal: "nunca um checkbox abaixo do botao de
   calcular". `fieldset` cru tem borda e recuo do navegador, que neste molde
   apareceriam como uma caixa dentro da caixa: os dois sao zerados e o campo
   passa a se parecer com os irmaos dele na grade. `legend` vira o rotulo, com o
   mesmo peso e tamanho do `label` dos outros campos.
   O radio recebe `accent-color` da tinta da marca, que e a unica forma de
   colorir controle nativo sem reconstrui-lo — e reconstruir controle nativo
   custa teclado e leitor de tela, que e o que a 22.8 protege. */
.rdm-f-campo-pivo{border:0;padding:0;margin:0;min-width:0}
.rdm-f-campo-pivo>legend{font-weight:600;font-size:.875rem;padding:0;margin:0 0 var(--rdm-e1)}
.rdm-f-radio{display:flex;align-items:center;gap:var(--rdm-e2);
  font:500 .9375rem Barlow,sans-serif;padding:7px 10px;margin:0 0 var(--rdm-e1);
  border:1px solid var(--rdm-traco);border-radius:var(--rdm-e1);
  background:var(--rdm-superficie);cursor:pointer}
.rdm-f-radio:last-of-type{margin-bottom:var(--rdm-e1)}
.rdm-f-radio input{width:auto;margin:0;accent-color:var(--rdm-tinta);flex:0 0 auto}
.rdm-f-radio:has(input:checked){border-color:var(--rdm-tinta);
  box-shadow:inset 0 0 0 1px var(--rdm-tinta)}

/* A PERGUNTA DA FERRAMENTA NA HOME, e ela e H2 e nao H1: o H1 da home e a
   identidade da ilha e esta indexado. */
body.rdm .rdm-f1-pergunta{margin:0 0 var(--rdm-e3)}

/* A CAMADA 2 DA F1 — bloco SEPARADO com titulo proprio (1.2 da especificacao:
   "fundi-las numa frase e o defeito que a secao 7 nomeia"). O titulo e menor que
   um H2 de secao de propósito: ele rotula um bloco dentro da resposta, nao uma
   secao da pagina. */
.rdm-f1-municipal{border-left:3px solid var(--rdm-traco);padding:0 0 0 var(--rdm-e3);
  margin:0 0 var(--rdm-e4)}
body.rdm .rdm-f1-municipal-titulo{font-size:1rem;margin:0 0 var(--rdm-e1)}
body.rdm .rdm-f1-municipal p:last-child{margin-bottom:0}

/* AS RESSALVAS DA 1.4 — abaixo do bloco de compra, e elas NAO sao rodape. */
.rdm-f1-ressalva{margin:0 0 var(--rdm-e5)}

/* O AVISO DE QUEM ESTA SEM JAVASCRIPT. Legenda, nao alerta: a pagina continua
   respondendo, so nao responde ao que a pessoa escolheu. */
body.rdm .rdm-f1-noscript{font-size:.9375rem;color:var(--rdm-legenda);
  background:var(--rdm-piso);border:1px dashed var(--rdm-traco);
  border-radius:var(--rdm-e1);padding:var(--rdm-e3);margin:0 0 var(--rdm-e4)}

/* MOLDE: caixa de resultado */
.rdm-molde-caixa{background:var(--rdm-superficie);border:2px solid var(--rdm-traco);
  border-radius:var(--rdm-e2);padding:var(--rdm-e4);margin:0 0 var(--rdm-e4)}
.rdm-molde-caixa-verde{border-color:var(--rdm-verde);background:var(--rdm-verde-fundo)}
.rdm-molde-caixa-alerta{border-color:var(--rdm-alerta);background:var(--rdm-alerta-fundo)}
body.rdm .rdm-molde-caixa-rotulo{font-size:.8125rem;text-transform:uppercase;letter-spacing:.08em;
  color:var(--rdm-legenda);margin:0 0 var(--rdm-e1)}
body.rdm .rdm-molde-caixa-numero{font-size:2.25rem;line-height:1.1;margin:0 0 var(--rdm-e3)}
.rdm-molde-caixa-unidade{font-size:1.25rem;color:var(--rdm-legenda)}
body.rdm .rdm-molde-caixa-frase{margin:0 0 var(--rdm-e2)}
body.rdm .rdm-molde-caixa-frase:last-child{margin-bottom:0}

/* ---------------------------------------------------------------------------
 * POR QUE TODA REGRA DO MOLDE DAQUI PARA BAIXO CARREGA `body.rdm`, e nao e
 * estilo: e a SEGUNDA METADE DA 32.5-d, medida em 04/11/2026 as 16h3xZ.
 *
 * Em 29/10 a 32.5-d achou que `body.rdm img{max-width:100%;height:auto}` vale
 * (0,1,2) e vence `.rdm-molde-cartao-foto`, que vale (0,1,0) — e o conserto
 * daquele dia pos `body.rdm` NO SELETOR DA FOTO. **So no da foto.** As outras
 * declaracoes do molde ficaram em (0,1,0), e `body.rdm p{margin:0 0 16px}`,
 * duas telas acima nesta mesma folha, vence TODAS elas pela mesma aritmetica.
 *
 * O QUE ISSO CUSTAVA, medido no navegador a 390 px nas 9 URLs do sitemap, com
 * a regua nova deste dia (`conferir-32-5-no-navegador.mjs --disputa`): 21
 * declaracoes do molde PERDIDAS so na pagina da F2, e tres delas dentro do
 * cartao, logo acima do botao que a 32.5 mede — `cartao-nome`, `cartao-spec` e
 * `cartao-preco` declaram `margin:0` e serviam 16 px cada uma. 48 px.
 *
 * E A IRONIA E EXATA: o bloco de telefone desta folha foi escrito em 29/10 para
 * COMPRAR PIXEL (`.rdm-molde-compra-escopo{margin-bottom:8px}`,
 * `.rdm-molde-compra-titulo{margin-bottom:4px;font-size:1.125rem}`), e nenhuma
 * dessas linhas nunca valeu um pixel: media query NAO acrescenta
 * especificidade, entao elas tambem perdiam para `body.rdm p` e `body.rdm h2`.
 * A pagina servia 16 px onde a folha pedia 8, 12 onde pedia 4, e corpo 22 px
 * onde pedia 18. E a familia da linha `height:44px` morta que a propria 32.5-d
 * achou tres telas abaixo — com uma diferenca que importa: aquela perdia para
 * uma IRMA, escrita depois com a mesma especificidade, e estas perdem para uma
 * regra GENERICA da casca, que ninguem le quando mexe no molde.
 *
 * O conserto e de ESPECIFICIDADE e nunca `!important`, pela 32.5-d item 2:
 * `body.rdm .rdm-molde-cartao-nome` vale (0,2,0) e vence `body.rdm p` (0,1,1).
 * As 24 regras foram prefixadas DE UMA VEZ, incluindo as das media queries, para
 * a ordem relativa entre elas nao mudar — prefixar metade seria trocar um
 * defeito calado por outro.
 *
 * E A TRAVA NASCEU NA MESMA PASSADA, porque esta classe ja voltou duas vezes:
 * `conferir-32-5-no-navegador.mjs` passou a comparar, em TODA pagina do molde,
 * a declaracao do molde com a regra generica que a disputa, e REPROVA quando a
 * generica vence E o valor servido discorda do declarado. Disputa que a
 * generica vence com o MESMO valor ele chama de LATENTE e imprime, em vez de
 * aprovar em silencio: foi exatamente assim que estas 48 px esperaram cinco
 * dias dentro de uma folha que parecia conferida.
 * ------------------------------------------------------------------------- */
/* MOLDE: bloco de compra e carrossel */
.rdm-molde-compra{margin:0 0 var(--rdm-e5)}
body.rdm .rdm-molde-compra-titulo{font-size:1.25rem;margin:0 0 var(--rdm-e2)}
body.rdm .rdm-molde-compra-escopo{color:var(--rdm-legenda);font-size:.9375rem;margin:0 0 var(--rdm-e3)}
body.rdm .rdm-molde-compra-vazio{color:var(--rdm-legenda);font-size:.9375rem;border-left:3px solid var(--rdm-traco);
  padding-left:var(--rdm-e3);margin:0}
body.rdm .rdm-molde-compra-comissao{font-size:.8125rem;color:var(--rdm-legenda);margin:var(--rdm-e3) 0 0}
.rdm-molde-carrossel{display:flex;gap:var(--rdm-e3);list-style:none;margin:0;padding:0 0 var(--rdm-e2);
  overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}
.rdm-molde-cartao{flex:0 0 232px;scroll-snap-align:start;background:var(--rdm-superficie);
  border:1px solid var(--rdm-traco);border-radius:var(--rdm-e2);padding:var(--rdm-e3);
  display:flex;flex-direction:column;gap:var(--rdm-e2)}
/* A FOTO E O RESERVADO TEM DE TER A MESMA ALTURA, E ISSO E REQUISITO DA 32.5 E
   NAO estetica: o reservado existe para a pagina nao PULAR quando a foto entra.
   Enquanto nenhum registro desta ilha tinha foto, esta regra nunca rodou contra
   uma foto de verdade — e ela estava QUEBRADA. Medido no ar a 390 px em
   29/10/2026, na primeira foto que a ilha teve: reservado 96 px, foto 182 px, e
   o primeiro botao de compra foi de 1.385 para 1.471 px, 71 acima do teto da
   32.5. A causa e de SELETOR, e e a familia da 32.5-c: `body.rdm img` vale
   (0,1,2) e vence `.rdm-molde-cartao-foto`, que vale (0,1,0), entao o
   `height:auto` daquela linha mandava na foto e a altura do molde era ignorada.
   Por isso o seletor da foto carrega `body.rdm` — para VENCER por especificidade,
   sem `!important`, que esconderia a disputa em vez de resolve-la. */
body.rdm .rdm-molde-cartao-foto,.rdm-molde-cartao-sem-foto{display:block;width:100%;height:120px;
  object-fit:contain;background:var(--rdm-piso);border-radius:var(--rdm-e1)}
body.rdm .rdm-molde-cartao-nome{font-weight:600;font-size:.9375rem;margin:0;line-height:1.3}
body.rdm .rdm-molde-cartao-spec{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.75rem;
  color:var(--rdm-legenda);margin:0}
body.rdm .rdm-molde-cartao-preco{font-size:1rem;margin:0}
.rdm-molde-cartao-preco-nota{font-family:Barlow,sans-serif;font-size:.6875rem;color:var(--rdm-legenda)}
.rdm-molde-cartao-botao{margin-top:auto;display:block;text-align:center;background:var(--rdm-tinta);
  color:#FFF;text-decoration:none;border-radius:var(--rdm-e1);padding:10px 12px;
  font-weight:600;font-size:.9375rem}
/* a linha discreta da 25.2, que so existe quando ha ficha. Ela vem DEPOIS do
   botao de proposito: a 32.5 mede o primeiro botao de compra, e saida secundaria
   acima da principal gastaria primeira tela com o elo mais fraco. O `margin-top`
   e zero porque o botao acima dele ja carrega o `margin-top:auto` do cartao. */
.rdm-molde-cartao-todos{display:block;text-align:center;font-size:.75rem;
  color:var(--rdm-legenda);text-decoration:underline;margin:0}

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
body.rdm .rdm-cartoes p{font-size:.9375rem;margin:0 0 var(--rdm-e3)}
.rdm-cartao-estado{font-size:.8125rem;color:var(--rdm-legenda);margin:0}

/* rodape */
.rdm-rodape{background:var(--rdm-tinta);color:#FFF;margin-top:var(--rdm-e8);
  padding:var(--rdm-e6) 0 var(--rdm-e5)}
.rdm-rodape-links{display:flex;flex-wrap:wrap;gap:var(--rdm-e4);list-style:none;
  margin:var(--rdm-e4) 0;padding:0;font-size:.9375rem}
.rdm-rodape a{color:var(--rdm-verde-claro)}
.rdm-rodape-aviso,.rdm-rodape-creditos{color:rgba(255,255,255,.82);font-size:.8125rem;max-width:68ch}

/* ---------------------------------------------------------------------------
   AS REGRAS DE TELEFONE DO MOLDE, E CADA NUMERO AQUI SAI DE UMA MEDICAO A 390 px
   NUM NAVEGADOR DE VERDADE, NUNCA DE PALPITE.

   Medido as 11h2xZ de 29/10/2026 pelo conferir-32-5-no-navegador.mjs: o primeiro
   botao de compra da F2 estava a 1.730 px contra o teto de 1.400 da 32.5. A
   medicao dos blocos, um por um, disse onde estavam os pixels — e nao estavam
   onde a intuicao punha:

     84 px   de respiro do TEMA entre o cabecalho e a trilha, que nao e nosso
    144 px   a frase de promessa, em QUATRO linhas
    521 px   o formulario, com cinco campos de 100 px cada
    144 px   a frase de escopo do bloco de compra, em QUATRO linhas
     96 px   o espaco reservado da foto, por cartao, ANTES do botao
     77 px   a especificacao do cartao, em TRES linhas

   O corte foi feito nesses seis lugares e em nenhum outro: nenhuma palavra saiu
   da pagina (32.3), nenhum bloco mudou de ordem (32.1) e nenhuma afirmacao da
   bancada mudou. O que mudou foi densidade no telefone.
   --------------------------------------------------------------------------- */
@media (max-width:719px){
  body.rdm{font-size:1.0625rem}
  /* o respiro do tema acima da trilha: 84 px de espaco que nao e nosso */
  body.rdm .wp-site-blocks>*:first-child,
  body.rdm .wp-block-group.has-global-padding,
  body.rdm main{padding-top:0;margin-top:0}
  .rdm-pagina{padding-top:0}
  .rdm-trilha{margin-top:var(--rdm-e3)}
  /* o formulario: label, campo e dica mais juntos, e a dica menor */
  .rdm-f-formulario{padding:var(--rdm-e3)}
  .rdm-f-campos{gap:var(--rdm-e2) var(--rdm-e3)}
  .rdm-f-campo{gap:1px}
  .rdm-f-campo label{font-size:.8125rem;line-height:1.25}
  .rdm-f-campo select,.rdm-f-campo input{padding:7px 8px;font-size:.9375rem}
  .rdm-f-campo .rdm-f-dica{font-size:.6875rem;line-height:1.25}
  body.rdm .rdm-f-acao{margin-top:var(--rdm-e2)}
  .rdm-f-botao{padding:10px 16px;width:100%}
  /* a promessa e a frase de escopo: mesmo texto, linha mais densa */
  body.rdm .rdm-promessa{font-size:1rem;line-height:1.45;margin-bottom:var(--rdm-e4)}
  body.rdm .rdm-molde-compra-escopo{font-size:.875rem;line-height:1.4;margin-bottom:var(--rdm-e2)}
  /* o cartao: a 32.5 mede o BOTAO, e o espaco reservado da foto vinha antes
     dele. A secao 6 manda que produto sem foto apareca com espaco reservado
     neutro, e ele continua existindo.

     A LINHA `.rdm-molde-cartao-sem-foto{height:44px}` MORAVA AQUI E ESTAVA
     MORTA, e o comentario dela afirmava um numero que a pagina nunca serviu.
     Ela foi escrita em 29/10/2026 as 11h4xZ dizendo "44 px em vez de 96, porque
     no telefone esses 52 px sao do espaco mais caro da pagina" — e a regra de 96
     px, mais abaixo neste mesmo bloco de telefone, vem DEPOIS dela com a mesma
     especificidade e por isso vencia. MEDIDO no navegador a 390 px as 14h0xZ de
     29/10: o reservado serve **96 px**. Os 52 px nunca foram economizados, e a
     medicao de 1.385 px daquela manha foi feita COM 96. Afirmacao em comentario
     nao e medicao, e esta e da familia do numero de tela digitado: ela parece
     conferida. A linha saiu em vez de ser consertada porque o teto da 32.5 ja
     passa com 96, e trocar a altura agora mexeria no numero que o portao acabou
     de aprovar. */
  .rdm-molde-cartao{padding:var(--rdm-e2);gap:var(--rdm-e1)}
  body.rdm .rdm-molde-cartao-spec{font-size:.6875rem;line-height:1.3}
  body.rdm .rdm-molde-cartao-preco{font-size:.9375rem}
  .rdm-molde-cartao-botao{padding:9px 10px}
  /* SEGUNDA PASSADA, 29/10 as 11h4xZ: a primeira levou o botao de 1.730 para
     1.409 px — NOVE px acima do teto de 1.400. Nove px nao se resolve com
     palpite, entao a medicao foi refeita e o corte foi nos quatro blocos que
     ainda tinham folga, com margem para a pagina crescer um pouco sem voltar a
     reprovar: a caixa de resultado, o titulo e o respiro do bloco de compra, e
     a linha de preco do cartao, que gastava duas linhas para dizer o preco e a
     data. Nenhuma palavra saiu da pagina. */
  .rdm-molde-caixa{padding:var(--rdm-e3);margin-bottom:var(--rdm-e3)}
  body.rdm .rdm-molde-caixa-numero{margin-bottom:var(--rdm-e2)}
  body.rdm .rdm-molde-compra-titulo{font-size:1.125rem;margin-bottom:var(--rdm-e1)}
  .rdm-molde-carrossel{gap:var(--rdm-e2);padding-bottom:var(--rdm-e1)}
  body.rdm .rdm-molde-cartao-preco{line-height:1.25}
  body.rdm .rdm-molde-cartao-nome{font-size:.875rem}
  .rdm-f-formulario{margin-bottom:var(--rdm-e3)}
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
  body.rdm .rdm-molde-caixa-numero{font-size:1.75rem}
  /* 32.5-c: a regra de telefone do molde alcanca TODA familia de cartao por
     seletor, e por isso ela mira a classe do MOLDE e nunca a de uma
     ferramenta. Cartao de 232 px no telefone de 390 px deixa a borda do
     seguinte visivel, que e o que convida a arrastar. */
  .rdm-molde-cartao{flex-basis:200px}
  body.rdm .rdm-molde-cartao-foto,.rdm-molde-cartao-sem-foto{height:96px}
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
<?php rodametria_casca_fechar_folha( 'rodametria-casca' ); ?>
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
	/* ITEM 2 DO DESPACHO DE 30/10/2026 — O PESO SAIU DA PERGUNTA DE KM.
	   Ela dizia "Faz quantos km de verdade com o seu peso?" e a F2 nao faz essa
	   conta: a constante de consumo por quilo de quem pilota esta `pendente` e
	   pela secao 10 nao pode entrar em formula. O RELEVO entra de verdade — e o
	   fator medido no estudo de Quito —, entao a pergunta passa a prometer o que
	   a ferramenta entrega. A TERCEIRA pergunta CONTINUA sendo de peso, e esta
	   certa: "Aguenta voce e a mochila?" e a F3, e carga maxima e peso de
	   verdade, comparado contra o `carga_max_kg` de cada veiculo. */
	$html .= '<p class="rdm-promessa">Precisa de CNH? Faz quantos km de verdade na sua ladeira? '
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

	/* ---------------------------------------------------------------------
	 * 1.11.0 (06/11/2026) — A PRIMEIRA TELA DA HOME E FILTRAVEL, E A PROMESSA
	 * DE 29/10 FOI CUMPRIDA.
	 *
	 * O comentario acima diz, desde 29/10, que *"no dia em que a resolucao for
	 * lida, a F1 toma a primeira tela da home e os cartoes descem — e NENHUMA
	 * URL muda"*. Esse dia foi 05/11/2026, ~23h3x de Brasilia, no Chrome do
	 * Raphael. A ferramenta se pendura AQUI, de dentro do snippet dela, pela
	 * 32.6-b: a casca nao cresce quando a ilha cresce, e a ferramenta nao edita
	 * a casca para aparecer.
	 *
	 * FILTRO VAZIO = A HOME HUB DE 29/10, BYTE POR BYTE. E isso que acontece se
	 * o banco da F1 nao chegar ao site ou se o limiar legal voltar a `pendente`
	 * — a home volta a ser HUB sozinha, sem ninguem editar PHP. A caixa abaixo
	 * continua sendo a verdade do dia em que ela aparece.
	 * ------------------------------------------------------------------- */
	$ferramenta = (string) apply_filters( 'rodametria_home_ferramenta', '' );

	if ( '' !== $ferramenta ) {
		$html .= $ferramenta;
	} else {
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
	}

	/* Os cartoes, na linguagem de quem pilota (VOZ.md). Pagina que nao existe
	   nao ganha link: o cartao diz o que falta, e nao promete data.
	 *
	 * ELES SAO UM MAPA COM CHAVE, E NAO HTML CORRIDO, desde 1.11.0: a
	 * ferramenta que ocupa a primeira tela TIRA o proprio cartao da lista pelo
	 * filtro `rodametria_home_cartoes`, porque cartao que aponta para a pagina
	 * em que ele esta e ruido — e o `VOZ.md` e literal, *"a ferramenta
	 * principal em cima; as OUTRAS ferramentas entram como cartoes"*. A chave e
	 * o que permite remover por NOME e nao por posicao: lista que depende da
	 * ordem de hoje quebra calada no dia em que a F3 entrar. */
	$f2 = rodametria_casca_url_do_slug( 'autonomia-patinete-eletrico' );

	$cartoes = array(
		'f2' => '<li><h3>Quantos km ele faz no seu relevo?</h3>'
			. '<p>Tensão e amperagem da bateria entram, watt-hora e a faixa de km saem — com o relevo '
			. 'do seu trajeto descontando o que tem de descontar.</p>'
			. ( '' === $f2
				? '<p class="rdm-cartao-estado">Está sendo publicada agora.</p>'
				: '<p><a class="rdm-molde-cartao-botao" href="' . esc_url( $f2 ) . '">Calcular a autonomia</a></p>' )
			. '</li>',

		'f1' => '<li><h3>Esse elétrico precisa de CNH?</h3>'
			. '<p>Potência, velocidade máxima e se tem acelerador decidem se o veículo é bicicleta '
			. 'elétrica, autopropelido ou ciclomotor — e a categoria é o que decide placa e '
			. 'registro.</p>'
			. '<p class="rdm-cartao-estado">Ainda não está no ar, e o motivo é um só: o texto oficial '
			. 'da resolução que fixa os limites não abre pelo nosso canal de leitura. A gente não vai '
			. 'publicar limite de potência tirado de notícia — errar para o lado permissivo manda '
			. 'alguém para a rua sem o documento que precisa.</p></li>',

		'f3' => '<li><h3>Aguenta você e a mochila?</h3>'
			. '<p>Peso de quem pilota mais a carga, contra a carga máxima que o fabricante declara, '
			. 'com folga — e os que ficam de fora dizem por quê.</p>'
			. '<p class="rdm-cartao-estado">Ainda não está no ar: das fichas que colhemos, só três '
			. 'declaram carga máxima, e nenhuma dessas três tem oferta aberta. Sem ficha que declare o '
			. 'limite, a conta não teria o que comparar.</p></li>',
	);

	$cartoes = (array) apply_filters( 'rodametria_home_cartoes', $cartoes );

	if ( $cartoes ) {
		/* O TITULO CONTA OS CARTOES QUE SOBRARAM, e nao diz "tres" de cabeca: a
		   lista encolhe quando uma ferramenta sobe para a primeira tela, e
		   titulo que afirma um numero que a lista nao tem e o numero de tela
		   digitado — a cicatriz mais cobrada desta ilha. Tres cartoes = a home
		   HUB, e o titulo e o de 29/10. */
		$quantos = count( $cartoes );
		if ( 3 === $quantos ) {
			$titulo_cartoes = 'As três perguntas';
		} elseif ( 1 === $quantos ) {
			$titulo_cartoes = 'A outra pergunta';
		} else {
			$titulo_cartoes = 'As outras perguntas';
		}
		$html .= '<h2>' . esc_html( $titulo_cartoes ) . '</h2>';
		$html .= '<ul class="rdm-cartoes">' . implode( '', $cartoes ) . '</ul>';
	}

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
function rodametria_casca_garantir_pagina( $slug, $titulo, $conteudo, $pai = 0 ) {
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
	/* O PAI, pela 16.2: "toda pagina nova nasce com pai; pagina sem pai e defeito
	   e nao publica". Ele e opcional porque as cinco paginas da raiz que a 16.1
	   nomeia (home, sobre, contato, divulgacao de afiliados, privacidade) nao tem
	   pai — e so elas. */
	if ( (int) $pai > 0 ) {
		$dados['post_parent'] = (int) $pai;
	}

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
		'versao'    => RODAMETRIA_CASCA_VERSAO,
		'assinatura' => rodametria_casca_assinatura_do_mapa(),
		'em'        => current_time( 'mysql', true ),
		'relato'    => $relato,
	), 'no' );

	return $relato;
}
}

/**
 * A ASSINATURA DO MAPA: os slugs que o mapa tem, em ordem, num texto so.
 *
 * Ela existe por um defeito medido em 29/10/2026 as 19h48Z, e ele e da familia
 * do "commit sem Sync nao e entrega". A instalacao rodava uma vez por VERSAO DA
 * CASCA, e a revisao 13 subiu casca nova e snippet de pagina nova na MESMA
 * passada do Sync: quando o `init` chamou a instalacao, o snippet novo ainda
 * nao estava carregado naquela requisicao — entao o filtro `rodametria_instalar`
 * dele nao existia, as tres paginas nao foram criadas, e a casca gravou
 * "instalado: 1.3.0". Com a versao ja marcada, a instalacao nunca mais rodaria.
 *
 * O sintoma era exatamente o que a secao 4 do contrato descreve: o `/status` em
 * 13, as cinco linhas do log dizendo `ok`, o mapa de paginas JA mostrando as
 * tres novas — e `wp-sitemap.xml` com duas URLs. **Verde em todo lugar e a
 * pagina nao existia.**
 *
 * Com a assinatura, pagina nova instala no dia em que o snippet dela entra, sem
 * ninguem tocar na versao da casca — que e o que o comentario do mapa, no topo
 * deste arquivo, promete desde a revisao 3: "a casca nao e editada quando a ilha
 * cresce".
 */
if ( ! function_exists( 'rodametria_casca_assinatura_do_mapa' ) ) {
function rodametria_casca_assinatura_do_mapa() {
	$slugs = array_keys( rodametria_casca_paginas() );
	sort( $slugs );

	return implode( ',', $slugs );
}
}

/**
 * A instalacao roda no `init`, e nao em toda requisicao: wp_insert_post em toda
 * visita e caro e sujo. Ela roda de novo quando a VERSAO DA CASCA muda OU
 * quando a ASSINATURA DO MAPA muda — e a segunda metade e a que faz pagina nova
 * nascer sem a casca ser editada. Ver a nota da assinatura acima.
 */
add_action( 'init', function () {
	$feito = get_option( 'rodametria_casca_instalado' );
	if ( is_array( $feito )
		&& isset( $feito['versao'] ) && RODAMETRIA_CASCA_VERSAO === $feito['versao']
		&& isset( $feito['assinatura'] )
		&& rodametria_casca_assinatura_do_mapa() === $feito['assinatura'] ) {
		return;
	}
	rodametria_casca_instalar();
}, 20 );

/**
 * AS VERSOES DOS SNIPPETS CARREGADOS, E A AUSENCIA E O SINAL (02/11/2026)
 * =======================================================================
 *
 * Cada snippet desta ilha define a propria constante `*_VERSAO`, e o
 * `manifest.json` passou a espelhar essa constante no campo `versao` de cada
 * item (ver o cabecalho de `ferramentas/atualizar-manifest.py`). O espelho do
 * manifest prova o que esta NO REPOSITORIO. Esta funcao prova o que esta
 * CARREGADO NO WORDPRESS, que nao e a mesma coisa e e a metade que faltava.
 *
 * POR QUE ISSO E PORTAO E NAO ENFEITE — a cicatriz e a da 20.4, e ela custou
 * SETE PAGINAS na clubedomosaico, DUAS VEZES em tres dias: o Sync grava o
 * snippet INATIVO de proposito e ATIVA depois, e quando a ativacao falha ele
 * escreve `gravado (#13) mas NAO ativado` numa linha do log e SEGUE EM FRENTE,
 * subindo a revisao. O sha256 do manifest nao pega isso, porque ele e sobre o
 * byte do repositorio, nao sobre o codigo que a requisicao carregou.
 *
 * E o mecanismo e a AUSENCIA, nao um valor errado: snippet que nao esta ativo
 * **nao roda**, logo nao chega a pendurar nada neste filtro, logo o `id` dele
 * NAO APARECE aqui. Quem confere no ar compara esta lista com os itens
 * `publicar: true` do manifest, e `id` que falta e snippet que nao carregou.
 *
 * AS CHAVES SAO OS `id` DO MANIFEST, nunca o nome da constante: e o manifest
 * que o portao tem na mao, e casar por nome de constante obrigaria o portao a
 * saber que `rodametria-institucional` se chama `RODAMETRIA_INST_VERSAO` —
 * exatamente a derivacao de cabeca que o espelho do manifest se proibe de fazer.
 */
if ( ! function_exists( 'rodametria_casca_versoes' ) ) {
function rodametria_casca_versoes() {
	$v = apply_filters( 'rodametria_versoes',
		array( 'rodametria-casca' => RODAMETRIA_CASCA_VERSAO ) );

	if ( ! is_array( $v ) ) {
		return array( 'rodametria-casca' => RODAMETRIA_CASCA_VERSAO );
	}

	$limpo = array();
	foreach ( $v as $id => $versao ) {
		if ( is_string( $id ) && '' !== $id && is_scalar( $versao ) ) {
			$limpo[ $id ] = (string) $versao;
		}
	}
	ksort( $limpo );

	return $limpo;
}
}

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
				'versoes'      => rodametria_casca_versoes(),
				'instalado'    => $feito ? $feito : null,
				'paginas'      => $mapa,
				/* A MESMA PERGUNTA QUE O RETRATO DA 29.3 RESPONDE, AQUI SEM
				   TOKEN (03/11/2026). O retrato da rota `/rotas` exige o token
				   do Sync, que não está no repositório e não deve estar — então
				   o "pronto quando" do despacho da purga não era conferível
				   desta nuvem, e portão que não roda não é portão. Isto é um
				   booleano sobre a existência de uma função desta ilha: não é
				   segredo do servidor, que é o que a 29.3 manda não vazar. */
				'tem_purga_de_cache' => function_exists( 'rodametria_casca_purgar_cache' ),
			);
		},
	) );
} );

/* =========================================================================
 * 12. A PORTA DE ENTRADA DO SITE, MEDIDA POR DENTRO — seção 29.3 do
 *     ARQUIPELAGO.md (03/11/2026)
 *
 * ESTA SEÇÃO É UMA DÍVIDA DE NASCIMENTO, E O PREÇO DELA FOI PAGO NA ILHA
 * IRMÃ. A 29.3 diz, desde 24/09/2026, que "a casca de TODA ilha serve
 * ?rest_route=/<ilha>/v1/rotas". Esta casca nasceu em 29/10/2026 sem ela, e a
 * varredura do despacho de 02/11/2026 em `dados/despachos.md` listou esta ilha
 * com `NÃO` nessa coluna, ao lado da aquametria.
 *
 * O CUSTO NÃO É HIPÓTESE — é a conta de uma queda que acabou de acontecer, e
 * numa ilha do MESMO plano de cPanel que este domínio (`/home3/rapha921/`):
 * em 30/10/2026 a ronda achou a robometria com 13 de 14 URLs em 404 e a home
 * em 200, e o despacho daquele dia escreveu "não é consertável pelo
 * repositório" — porque a rota que o consertaria não existia lá. A ilha passou
 * 30/10, 31/10, 01/11 e 02/11 fora do ar. A rota nasceu lá em 02/11 e o
 * defeito que ficou quatro dias de pé caiu em dois minutos depois disso.
 * A porta desta conta já caiu QUATRO vezes com a mesma assinatura.
 *
 * É a 29.1 na forma mais cara: todo portão desta ilha entra pela porta que
 * continua aberta. O Sync é `/?rodametria_sync=`, uma query na raiz. O
 * `/status` e o `/casca` são rotas REST, alcançáveis por `?rest_route=`. A
 * bancada roda sem rede. Os quatro estariam verdes com o site morto — e os
 * quatro continuariam certos, e continuariam irrelevantes.
 *
 *   ?rest_route=/rodametria/v1/rotas&token=<token do Sync>
 *   ?rest_route=/rodametria/v1/rotas&token=<token do Sync>&reparar=1
 *
 * O reparo é `flush_rewrite_rules( true )` — o mesmo caminho do botão Salvar
 * de Configurações > Links permanentes, que é o conserto que a documentação do
 * WordPress manda fazer para este defeito. A diferença é que daqui ele é
 * MEDIDO: a resposta traz o retrato de antes e o de depois, e quem lê compara
 * os dois em vez de acreditar.
 *
 * O `flush_rewrite_rules( false )` que já existe nesta casca (página criada) e
 * nos três snippets de página NÃO conserta isto e nunca consertou: o `false` é
 * a purga mole, que regrava a option `rewrite_rules` no banco e não encosta no
 * `.htaccess`. Era a escolha certa para o que ele faz — remontar a estrutura
 * de páginas não é motivo para reescrever a porta do site — e é por isso que o
 * reparo daqui é outra função, com outro portão, e não uma troca de argumento
 * lá dentro.
 *
 * NÃO HÁ GANCHO AUTOMÁTICO, e isso é a 29.4 e não preguiça: porta de entrada
 * que se conserta calada a cada carregamento é a que ninguém consegue desfazer
 * no dia em que estiver errada. O reparo é pedido, com token, e devolve o
 * antes e o depois para quem pediu comparar.
 *
 * O QUE ESTA SEÇÃO NÃO ALCANÇA, escrito para ninguém procurar aqui depois: se
 * o hospedeiro tiver desligado o `AllowOverride`, o `.htaccess` volta a ser
 * escrito e o Apache continua ignorando. Nesse caso o diagnóstico mostra o
 * arquivo gravado e correto E as URLs continuam em 404 — e aí é chamado na
 * HostGator, não é código desta ilha. O diagnóstico existe justamente para
 * separar os dois mundos com número em vez de palpite.
 *
 * AS DUAS COISAS EM QUE ESTA ILHA DIVERGE DO MODELO, ditas aqui porque
 * divergência calada é a que a próxima execução lê como descuido:
 *
 *   (a) ~~ESTA ILHA NÃO TEM FUNÇÃO DE PURGA DE CACHE.~~ **FECHADA EM
 *       03/11/2026, na casca 1.8.0:** a purga existe, mora na seção 13 deste
 *       arquivo e entrou COM os dois portões que o despacho exigia
 *       (`teste-purga-cache.php` e `mutacoes-purga-cache.py`). A chamada
 *       abaixo continua guardada por `function_exists` de propósito — ela é o
 *       contrato entre as duas seções, não uma suposição sobre esta ilha —, e
 *       `tem_purga_de_cache` continua saindo no retrato, agora dizendo `true`.
 *       O texto anterior desta alínea dizia que a chamada era no-op e que a
 *       primeira leitura depois de um reparo podia medir a cópia velha do
 *       hospedeiro: era verdade entre 03/11 às 10h4xZ e 03/11 às 13hxxZ, e
 *       deixou de ser. Quem reparar daqui continua lendo com quebra de cache,
 *       porque purga do hospedeiro não é promessa de cache de borda.
 *
 *   (b) O SNIPPET DO SYNC DESTA ILHA NÃO ESTÁ NO REPOSITÓRIO — as outras três
 *       têm o seu. Então o nome da função que guarda o token NÃO pôde ser
 *       conferido no chão, só herdado do padrão das irmãs
 *       (`<ilha>_sync_token()` e a option de mesmo nome). Herdar nome sem
 *       conferir é exatamente a derivação de cabeça que a 20.7 proíbe, e aqui
 *       ela erraria CALADA: `token_esperado()` devolveria vazio, a permissão
 *       negaria TODO pedido — inclusive o certo — e a rota seria um portão
 *       morto com cara de portão. É por isso que a negativa desta rota diz
 *       QUAL das três coisas faltou, em código de erro distinto, e os três
 *       códigos são legíveis SEM o token (ver a nota do `permission_callback`).
 *       A ausência passou a falar: é o mecanismo da 20.7 noutro traje.
 * ========================================================================= */

if ( ! function_exists( 'rodametria_casca_token_esperado' ) ) {
/**
 * O token do Sync, lido de onde o Sync o guarda.
 *
 * A função do Sync é preferida porque ela CRIA o token quando ele ainda não
 * existe; a option é o caminho de quem só lê. Um segundo segredo para esta
 * ilha seria um segredo a mais para perder.
 */
function rodametria_casca_token_esperado() {
	if ( function_exists( 'rodametria_sync_token' ) ) {
		$t = rodametria_sync_token();
		if ( is_string( $t ) && '' !== $t ) {
			return $t;
		}
	}
	$guardado = get_option( 'rodametria_sync_token', '' );

	return is_string( $guardado ) ? $guardado : '';
}
}

if ( ! function_exists( 'rodametria_casca_fonte_do_token' ) ) {
/**
 * DE ONDE o token veio, para quem tem o token poder ler.
 *
 * Existe por causa da divergência (b) do cabeçalho desta seção: o Sync desta
 * ilha não está no repositório, então o nome da função é herdado e não
 * conferido. Este campo é o que transforma "a rota nega tudo" em
 * "a rota nega tudo PORQUE o nome da fonte está errado".
 */
function rodametria_casca_fonte_do_token() {
	if ( function_exists( 'rodametria_sync_token' ) ) {
		$t = rodametria_sync_token();
		if ( is_string( $t ) && '' !== $t ) {
			return 'funcao:rodametria_sync_token';
		}
	}
	$guardado = get_option( 'rodametria_sync_token', '' );
	if ( is_string( $guardado ) && '' !== $guardado ) {
		return 'option:rodametria_sync_token';
	}

	return null;
}
}

if ( ! function_exists( 'rodametria_casca_carregar_ferramentas_de_admin' ) ) {
/**
 * Traz `get_home_path()`, `got_mod_rewrite()` e `save_mod_rewrite_rules()`.
 *
 * As três moram em `wp-admin/includes/` e não existem numa requisição comum.
 * Sem elas o `flush_rewrite_rules( true )` vira o `false`: o `flush_rules()`
 * do WordPress só chama `save_mod_rewrite_rules()`
 * `if ( function_exists(...) )`, e num carregamento sem admin essa condição é
 * falsa — o reparo pareceria rodar e não encostaria no arquivo. É a família do
 * "portão que nunca rodou é função morta", e aqui seria pior: um verde dizendo
 * que a porta foi consertada.
 */
function rodametria_casca_carregar_ferramentas_de_admin() {
	if ( ! defined( 'ABSPATH' ) ) {
		return false;
	}
	foreach ( array( 'file.php', 'misc.php' ) as $arquivo ) {
		$caminho = ABSPATH . 'wp-admin/includes/' . $arquivo;
		if ( is_readable( $caminho ) ) {
			require_once $caminho;
		}
	}

	return function_exists( 'get_home_path' )
		&& function_exists( 'got_mod_rewrite' )
		&& function_exists( 'save_mod_rewrite_rules' );
}
}

if ( ! function_exists( 'rodametria_casca_diagnostico_rotas' ) ) {
/**
 * O retrato do roteamento, medido de dentro do servidor.
 *
 * Só número e fato: o que o arquivo é, não o que deveria ser. Quem decide se
 * está certo é quem lê a resposta contra as URLs no ar — este lado não opina.
 */
function rodametria_casca_diagnostico_rotas() {
	$tem_admin = rodametria_casca_carregar_ferramentas_de_admin();
	$raiz      = function_exists( 'get_home_path' ) ? get_home_path() : ABSPATH;
	$arquivo   = rtrim( (string) $raiz, '/\\' ) . DIRECTORY_SEPARATOR . '.htaccess';

	/* AS FUNCOES DE `stat` DO PHP SAO CACHEADAS DENTRO DA REQUISICAO, e sem esta
	   linha o retrato de DEPOIS do reparo e o retrato de ANTES.
	   `file_exists()`, `filesize()`, `filemtime()`, `is_readable()` e
	   `is_writable()` leem o cache de stat; `file_get_contents()` nao. Entao o
	   reparo que acabou de criar o arquivo sairia com `existe: false` e
	   `bytes: 0` — e `reparado` e calculado SOBRE `existe`, logo a resposta
	   diria que a porta NAO foi consertada depois de conserta-la.
	   REPROVACAO FALSA, que e pior que nenhuma: a 20.5 escreve com todas as
	   letras que "portao que reprova pagina certa e o caminho mais curto para
	   alguem ignora-lo".
	   NAO E TEORIA — foi medido no chao em 03/11/2026, antes de esta rota ir ao
	   ar, pelo `ferramentas/teste-rotas.php`: a afirmacao que exige
	   `antes.bytes < depois.bytes` reprovou na primeira passada, com o reparo
	   tendo escrito o bloco do WordPress de verdade no arquivo fabricado.
	   O MODELO DA 29.3 NAO TEM ESTA LINHA, e as duas ilhas que servem a rota
	   (clubedomosaico desde 24/09 e robometria desde 02/11) estao sem ela —
	   virou despacho em `dados/despachos.md`, porque a secao 3 proibe editar
	   ilha que esta execucao nao reservou. */
	clearstatcache( true, $arquivo );

	$regras = get_option( 'rewrite_rules' );

	$retrato = array(
		'versao_casca'         => RODAMETRIA_CASCA_VERSAO,
		'permalink_structure'  => (string) get_option( 'permalink_structure', '' ),
		'regras_no_banco'      => is_array( $regras ) ? count( $regras ) : 0,
		'ferramentas_de_admin' => $tem_admin,
		'mod_rewrite'          => function_exists( 'got_mod_rewrite' ) ? (bool) got_mod_rewrite() : null,
		'home_url'             => home_url( '/' ),
		'site_url'             => site_url( '/' ),
		'raiz_gravavel'        => is_writable( (string) $raiz ),
		'fonte_do_token'       => rodametria_casca_fonte_do_token(),
		'tem_purga_de_cache'   => function_exists( 'rodametria_casca_purgar_cache' ),
		'htaccess'             => array(
			'caminho'  => $arquivo,
			'existe'   => file_exists( $arquivo ),
			'legivel'  => is_readable( $arquivo ),
			'gravavel' => is_writable( $arquivo ),
			'bytes'    => file_exists( $arquivo ) ? (int) filesize( $arquivo ) : 0,
			/* O `mtime` entra como FATO e nunca como sinal, e isto está medido:
			   em 05/10/2026, na segunda queda da clubedomosaico, três leituras
			   espaçadas por ~20 segundos devolveram 10:23:49, 10:24:10 e
			   10:24:31 — o arquivo é reescrito A CADA REQUISIÇÃO e acompanha o
			   relógio de quem lê. Vigiar esta data é o portão que qualquer um
			   escreveria primeiro e que não mede nada: o arquivo parece
			   recém-salvo todos os dias, inclusive nos dias em que está errado.
			   Quem for vigiar a porta vigia `blocos` e `tem_wordpress`. */
			'mtime'    => file_exists( $arquivo ) ? gmdate( 'Y-m-d H:i:s', (int) filemtime( $arquivo ) ) . 'Z' : null,
		),
	);

	/* O conteúdo do arquivo entra pelos MARCADORES e pela contagem de regras de
	   reescrita, nunca inteiro (29.3): `.htaccess` de hospedeiro compartilhado
	   carrega bloco de segurança de terceiro, e despejar isso numa resposta
	   HTTP é entregar a configuração do servidor a quem tiver o token. O que a
	   Fundação precisa saber é se o bloco do WordPress está lá — e isso são
	   duas linhas. */
	if ( $retrato['htaccess']['legivel'] ) {
		$texto = (string) @file_get_contents( $arquivo );
		preg_match_all( '/^#\s*BEGIN\s+(.+)$/mi', $texto, $achados );
		$retrato['htaccess']['blocos']         = array_map( 'trim', $achados[1] );
		$retrato['htaccess']['tem_wordpress']  = (bool) preg_match( '/^#\s*BEGIN\s+WordPress\s*$/mi', $texto );
		$retrato['htaccess']['linhas_rewrite'] = preg_match_all( '/^\s*Rewrite(Rule|Cond|Engine|Base)/mi', $texto );
	}

	return $retrato;
}
}

if ( ! function_exists( 'rodametria_casca_reparar_rotas' ) ) {
/**
 * Reescreve as regras de reescrita, e devolve o antes e o depois.
 *
 * `flush_rewrite_rules( true )` é o mesmo caminho do botão Salvar dos Links
 * permanentes. A purga de cache vai junto porque o defeito que trouxe esta
 * função foi lido, por dias, através de página servida de cache: sem ela, a
 * primeira medição depois do reparo mediria a cópia velha e diria que não
 * funcionou. Desde a casca 1.8.0 (03/11/2026) a função existe nesta ilha, na
 * seção 13; a chamada segue guardada por `function_exists` porque é assim que
 * as duas seções se falam, e `tem_purga_de_cache` no retrato continua dizendo
 * qual dos dois mundos está no ar, em vez de esconder.
 */
function rodametria_casca_reparar_rotas() {
	$antes = rodametria_casca_diagnostico_rotas();

	if ( ! $antes['ferramentas_de_admin'] ) {
		return array(
			'reparado' => false,
			'motivo'   => 'as funcoes de wp-admin/includes nao carregaram; sem elas o flush nao escreve o .htaccess',
			'antes'    => $antes,
			'depois'   => $antes,
		);
	}

	flush_rewrite_rules( true );

	if ( function_exists( 'rodametria_casca_purgar_cache' ) ) {
		rodametria_casca_purgar_cache();
	}

	$depois = rodametria_casca_diagnostico_rotas();

	return array(
		'reparado' => ( $depois['htaccess']['existe'] && ! empty( $depois['htaccess']['tem_wordpress'] ) ),
		'motivo'   => null,
		'antes'    => $antes,
		'depois'   => $depois,
	);
}
}

add_action( 'rest_api_init', function () {
	if ( ! function_exists( 'register_rest_route' ) ) {
		return;
	}
	register_rest_route( 'rodametria/v1', '/rotas', array(
		'methods'             => 'GET',
		'callback'            => function ( $pedido ) {
			if ( '1' === (string) $pedido->get_param( 'reparar' ) ) {
				return rodametria_casca_reparar_rotas();
			}

			return rodametria_casca_diagnostico_rotas();
		},
		/* A NEGATIVA DIZ QUAL DAS TRES COISAS FALTOU, e os tres codigos sao
		   legiveis SEM o token. O modelo das irmas devolve `false`, que o
		   WordPress traduz num 401 generico — e um 401 generico junta dois
		   mundos que o conserto separa: "o pedido trouxe o token errado"
		   (a rota esta viva e a parede funciona) e "esta casca nao achou de
		   onde ler o token" (a rota esta MORTA e nega tudo, inclusive o
		   pedido certo). Esta ilha precisa da distincao porque o Sync dela
		   nao esta no repositorio e o nome da fonte do token e herdado e nao
		   conferido — ver a divergencia (b) no cabecalho desta secao.
		   O `status` vai EXPLICITO em cada WP_Error: `WP_REST_Server` usa o
		   `data['status']` do erro e cai em 500 quando ele falta, e 500 numa
		   parede de permissao e exatamente o tipo de verde errado que a 20.5
		   nomeia. */
		'permission_callback' => function ( $pedido ) {
			$esperado = rodametria_casca_token_esperado();
			if ( '' === $esperado ) {
				return new WP_Error(
					'rodametria_rotas_sem_fonte_de_token',
					'esta casca nao achou de onde ler o token do Sync; a rota nega TODO pedido ate isso ser consertado',
					array( 'status' => 401 )
				);
			}
			$vindo = (string) $pedido->get_param( 'token' );
			if ( '' === $vindo ) {
				return new WP_Error(
					'rodametria_rotas_token_ausente',
					'falta o parametro token',
					array( 'status' => 401 )
				);
			}
			if ( ! hash_equals( $esperado, $vindo ) ) {
				return new WP_Error(
					'rodametria_rotas_token_invalido',
					'token invalido',
					array( 'status' => 401 )
				);
			}

			return true;
		},
	) );
} );

/* =========================================================================
 * 13. A PURGA DE CACHE DO HOSPEDEIRO — a divergência (a) da seção 12,
 *     fechada em 03/11/2026
 *
 * POR QUE ESTA SEÇÃO NASCEU DEPOIS DA 12, E NÃO JUNTO COM ELA. A seção 12
 * entrou em 03/11/2026 com a chamada da purga já escrita e GUARDADA por
 * `function_exists`, no-op, e com o cabeçalho dizendo com todas as letras que
 * esta ilha era a única no ar sem a função. Não foi esquecimento: purga que
 * apaga arquivo em disco é exatamente a função que entrou no Arquipélago com a
 * armadilha do `realpath('')` — e portar isso de carona, no fim de um bloco que
 * já havia mexido na porta de entrada do site, é como o defeito nasce. Virou
 * despacho NORMAL em `dados/despachos.md`, e este é o bloco que o fecha, com os
 * DOIS portões da aquametria do lado (`ferramentas/teste-purga-cache.php` e
 * `ferramentas/mutacoes-purga-cache.py`), que é a condição que o despacho
 * escreveu.
 *
 * ONDE ISSO CUSTA, e é medido nas irmãs e não suposto aqui: o reparo da 29.3
 * chama a purga DEPOIS do `flush_rewrite_rules( true )`, porque o defeito que
 * trouxe esta função foi lido, por dias, através de página servida de cache —
 * sem a purga, a primeira medição depois do reparo mede a cópia velha e diz que
 * não funcionou. É reprovação falsa, a mesma família que a 20.5 chama de "o
 * caminho mais curto para alguém passar a ignorar um portão", e no uso real é
 * pior: quem lê isso numa ilha caída conclui, pela 29.4, que o `AllowOverride`
 * está desligado e abre chamado na HostGator por um defeito que o reparo já
 * desfez.
 *
 * A LISTA DE GANCHOS É DEFENSIVA DE PROPÓSITO. A ilha não escolhe o hospedeiro
 * e não pode medir daqui qual cache estará instalado amanhã; cada entrada é um
 * `if` sobre algo que pode não existir, e nenhuma é obrigatória. O que NÃO é
 * defensivo são as guardas da função que apaga arquivo, e quem as mede é
 * `ferramentas/teste-purga-cache.php`, com `ferramentas/mutacoes-purga-cache.py`
 * cobrando que o portão reprove — e reprove PELA AFIRMAÇÃO CERTA — quando cada
 * guarda é retirada uma por vez.
 *
 * E A FALTA DESTA FUNÇÃO ERA DITA EM VEZ DE ESCONDIDA, que é o mecanismo da
 * 20.7 noutro traje: `tem_purga_de_cache` sai no retrato da rota da 29.3 desde
 * que a rota nasceu, e a partir desta revisão sai TAMBÉM no `/casca`, que é
 * público. A diferença importa e está escrita no `REGISTRO.md`: o retrato da
 * rota exige o token do Sync, que não está no repositório, então o "pronto
 * quando" do despacho não era conferível desta nuvem. No `/casca` ele é — e
 * booleano sobre a existência de uma função não é segredo do servidor (29.3).
 * ========================================================================= */

if ( ! function_exists( 'rodametria_casca_purgar_cache' ) ) {
/**
 * Esvazia o cache do hospedeiro, UMA vez por requisição.
 *
 * O `static` existe porque uma revisão do Sync grava muitas options, e o
 * gatilho desta função é a gravação de option: sem ele, uma revisão que grava
 * vinte options faria vinte varreduras de pasta na mesma requisição.
 */
function rodametria_casca_purgar_cache() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;

	/* Endurance Page Cache — é o que o `x-server-cache` desta hospedagem
	   anuncia. As duas formas: a ação que as versões novas escutam e o método
	   da classe, para as antigas. */
	do_action( 'epc_purge' );
	do_action( 'epc_purge_request' );
	if ( class_exists( 'Endurance_Page_Cache' ) ) {
		$epc = new Endurance_Page_Cache();
		if ( method_exists( $epc, 'purge_all' ) ) {
			$epc->purge_all();
		}
	}

	/* A PURGA QUE NÃO DEPENDE DO NOME DO GANCHO: esvaziar
	   `wp-content/endurance-page-cache/`, que é o que o `purge_all()` do próprio
	   plugin faz. Ela existe porque o gancho pode ter mudado de nome entre
	   versões, e gancho que ninguém escuta falha em silêncio.

	   AS GUARDAS, e nenhuma é decoração — este é o único código desta ilha que
	   apaga arquivo: o caminho é montado a partir de WP_CONTENT_DIR e nunca de
	   entrada de requisição; o caminho real é conferido contra a raiz a cada
	   nível da recursão; link simbólico não é seguido; e caminho VAZIO é
	   recusado antes de tudo. */
	$pasta = defined( 'WP_CONTENT_DIR' ) ? WP_CONTENT_DIR . '/endurance-page-cache' : '';
	if ( '' !== $pasta && is_dir( $pasta ) && ! is_link( $pasta ) ) {
		rodametria_casca_esvaziar_pasta( $pasta, $pasta );
	}

	/* Os outros, cada um só se estiver lá. Nenhum é esperado neste host. */
	if ( function_exists( 'wp_cache_clear_cache' ) ) {   // WP Super Cache
		wp_cache_clear_cache();
	}
	if ( function_exists( 'rocket_clean_domain' ) ) {    // WP Rocket
		rocket_clean_domain();
	}
	if ( function_exists( 'w3tc_flush_all' ) ) {         // W3 Total Cache
		w3tc_flush_all();
	}
	do_action( 'litespeed_purge_all' );                  // LiteSpeed Cache
}
}

/**
 * Apaga o conteúdo de uma pasta de cache, e NUNCA sai dela.
 *
 * `$raiz` viaja em toda chamada e é conferida a cada nível: antes de apagar
 * qualquer coisa, o caminho real tem de começar pelo caminho real da raiz, COM
 * a barra separadora no fim. É o que impede um link simbólico, um `..`, uma
 * pasta montada — ou uma pasta vizinha cujo nome apenas COMEÇA pelo da raiz —
 * de virarem uma exclusão em outro lugar do disco. A pasta raiz em si não é
 * removida, só esvaziada: o plugin a recria, e sumir com ela não é direito
 * desta ilha.
 *
 * A PRIMEIRA LINHA DESTA FUNÇÃO FOI ESCRITA, NA AQUAMETRIA, DEPOIS DE ELA
 * APAGAR A ILHA INTEIRA, em 15/09/2026, e o registro é copiado para cá porque a
 * causa é uma armadilha da linguagem que nenhuma leitura do código revelaria.
 * **`realpath('')` não devolve `false` em PHP: devolve o DIRETÓRIO DE TRABALHO
 * ATUAL.** Então, chamada com caminho e raiz vazios, a guarda de contenção
 * comparava o diretório atual consigo mesmo, aprovava, e a recursão esvaziava o
 * diretório de trabalho — que na bancada é a pasta da ilha. Foram 117 arquivos
 * apagados, recuperados na hora com `git checkout` porque o repositório é o
 * lugar do trabalho (seção 3); num servidor não haveria de onde recuperar.
 *
 * O QUE ISSO DIZ SOBRE A GUARDA, e é maior do que o caso: ela era escrita como
 * "o caminho real tem de estar DENTRO da raiz real", que é a pergunta certa — e
 * `realpath()` respondeu por um caminho que nunca foi pedido. Guarda que confia
 * numa função de biblioteca para dizer "isto não existe" herda todos os valores
 * que essa função devolve quando a entrada é degenerada. A primeira linha não
 * substitui a guarda: ela recusa o vazio ANTES, para que a comparação nunca
 * chegue a acontecer sobre um caminho inventado pela linguagem. O caso 5 do
 * portão é o que impede essa linha de ser retirada por parecer redundante.
 *
 * NO SITE NADA DISSO ACONTECE: o único chamador monta o caminho a partir de
 * `WP_CONTENT_DIR` e já exige `'' !== $pasta && is_dir( $pasta )`. O defeito era
 * da FUNÇÃO, não do caminho de produção — e é exatamente o tipo de defeito que
 * só aparece quando alguém escreve o portão, que é o motivo de o portão existir.
 */
if ( ! function_exists( 'rodametria_casca_esvaziar_pasta' ) ) {
function rodametria_casca_esvaziar_pasta( $pasta, $raiz ) {
	if ( ! is_string( $pasta ) || ! is_string( $raiz ) || '' === $pasta || '' === $raiz ) {
		return;
	}

	$real_raiz = realpath( $raiz );
	$real      = realpath( $pasta );
	if ( ! $real_raiz || ! $real || 0 !== strpos( $real . DIRECTORY_SEPARATOR,
		rtrim( $real_raiz, DIRECTORY_SEPARATOR ) . DIRECTORY_SEPARATOR ) ) {
		return;
	}

	$itens = @scandir( $real );
	if ( ! is_array( $itens ) ) {
		return;
	}
	foreach ( $itens as $item ) {
		if ( '.' === $item || '..' === $item ) {
			continue;
		}
		$caminho = $real . DIRECTORY_SEPARATOR . $item;
		if ( is_link( $caminho ) ) {
			/* Link simbólico não é seguido: apagar o link é seguro, apagar o que
			   ele aponta seria sair da pasta sem perceber. */
			@unlink( $caminho );
		} elseif ( is_dir( $caminho ) ) {
			rodametria_casca_esvaziar_pasta( $caminho, $real_raiz );
			@rmdir( $caminho );
		} else {
			@unlink( $caminho );
		}
	}
}
}

/**
 * O GATILHO: a ilha acabou de gravar dado no site.
 *
 * O Sync escreve `rodametria_dados_*` e `rodametria_sync_estado` a cada
 * aplicação, e a casca escreve `rodametria_casca_instalado` quando remonta a
 * estrutura, então uma revisão que muda QUALQUER coisa passa por aqui. O
 * prefixo é conferido para a purga não disparar em gravação de option de
 * terceiro — uma varredura de pasta em cada `update_option` do site inteiro —, e
 * o `static` da função acima faz a purga acontecer UMA vez por requisição.
 */
if ( ! function_exists( 'rodametria_casca_purgar_ao_gravar' ) ) {
function rodametria_casca_purgar_ao_gravar( $opcao ) {
	if ( 0 === strpos( (string) $opcao, 'rodametria_' ) ) {
		rodametria_casca_purgar_cache();
	}
}
}
add_action( 'updated_option', 'rodametria_casca_purgar_ao_gravar', 10, 1 );
add_action( 'added_option', 'rodametria_casca_purgar_ao_gravar', 10, 1 );

<?php
/**
 * Monta QUALQUER UMA das treze paginas no ar — casca ou conteudo/ — inteira, do
 * jeito que o site a serve, para medir antes de publicar.
 *
 *   php ferramentas/render-pagina-completa.php . calculadora-de-potencia-do-aquecedor
 *   php ferramentas/render-pagina-completa.php . inicio
 *
 * POR QUE ELE EXISTE, ao lado dos tres renderizadores que ja havia:
 *
 *   - render-casca-pagina.php monta so as QUATRO paginas da casca;
 *   - render-para-teste.php monta o shortcode de uma calculadora SEM cabecalho,
 *     sem H1 e sem rodape;
 *   - render-artigo-para-teste.php monta o artigo, tambem sem cabecalho nem H1.
 *
 * Nenhum dos tres serve a pagina inteira das nove paginas de conteudo/, e a
 * partir da casca 1.5.0 e justamente ali — entre o cabecalho e o H1, e no fim do
 * the_content — que nascem a trilha e o cluster. Medir a arvore em qualquer um
 * dos tres seria medir metade do que o site serve, que e a cicatriz que a
 * Robometria pagou tres vezes (secao 8 do ARQUIPELAGO.md).
 *
 * O QUE ELE IMITA DE PROPOSITO, e sem o que nao mediria nada:
 *
 *   1. O CAMINHO DA TRILHA. No site ela entra pelo filtro render_block, no lugar
 *      do bloco core/post-title. Aqui o H1 passa pelo MESMO filtro, com o mesmo
 *      nome de bloco — nao e um "monta a trilha e cola em cima".
 *   2. O the_content DE VERDADE. O cluster "Veja tambem" entra por ele, na
 *      prioridade 20. Por isso o corpo aqui atravessa apply_filters('the_content'),
 *      depois do escape de "&" — que e a ordem do site: o filtro 20 roda DEPOIS
 *      do do_shortcode, entao o que ele acrescenta nunca e escapado. Bancada que
 *      escapasse o cluster mediria um defeito que nao existe.
 *   3. O Markdown pelo conversor do PROPRIO Sync, para as nove paginas de
 *      conteudo/ — o mesmo motivo do render-artigo-para-teste.php.
 *
 * E UMA QUE ELE NAO IMITA, declarada: UMA pagina por processo. Quem quiser as
 * treze chama treze vezes. O `static` da marca, do estilo, do id do menu e da
 * propria trilha sai na primeira e some nas seguintes — foi assim que a
 * Robometria mediu 915 KB do que no ar tem 960 KB, sem erro nenhum aparecer.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$alvo = isset( $argv[2] ) ? $argv[2] : 'inicio';

/* O slug PRECISA estar no global antes de carregar os snippets: o snippet dos
   artigos e a trilha da casca se reconhecem por post_name, nao por shortcode. */
$GLOBALS['__slug_pagina']    = $alvo;
$GLOBALS['__pagina_inicial'] = ( 'inicio' === $alvo );

require __DIR__ . '/render-para-teste.php';

/* O que "existe publicado" neste site de teste — as quatro paginas da casca, as
   cinco calculadoras, os tres artigos-ancora e a pagina de afiliados. Sem o
   mapa a casca serve <span> no lugar de <a>, de proposito, e o teste estaria
   medindo o caso errado.

   NAO ESTAO AQUI, e e o ponto: /guias/ e as categorias de nivel 2
   (/calculadoras/aquecimento-e-luz/ e irmas). Elas nao existem no site, e e
   assim que a bancada exercita o degrau em TEXTO da trilha. */
$GLOBALS['__paginas'] = array(
	'inicio'                                    => true,
	'calculadoras'                              => true,
	'metodologia'                               => true,
	'sobre'                                     => true,
	'divulgacao-de-afiliados'                   => true,
	'calculadora-de-litragem'                   => true,
	'calculadora-de-vazao-do-filtro'            => true,
	'calculadora-de-potencia-do-aquecedor'      => true,
	'calculadora-de-midia-filtrante'            => true,
	'calculadora-de-iluminacao'                 => true,
	'quantos-watts-de-aquecedor-para-aquario'   => true,
	'quanta-midia-biologica-o-aquario-precisa'  => true,
	'quantos-lumens-por-litro-aquario-plantado' => true,
	/* A leva 1 da malha do eixo /peixes/ (T4, 12/09/2026). Nivel 1, nivel 2 e
	   as tres fichas: sao as cinco primeiras paginas desta ilha que nascem com
	   MAE, e por isso tambem as primeiras em que a trilha tem quatro degraus de
	   verdade, todos com endereco. Ate aqui o degrau de nivel 2 desta ilha
	   nunca era link, e afirmacao sobre o caso que nao existe e afirmacao que
	   nao mede nada. */
	'peixes'                                    => true,
	'tetras'                                    => true,
	'quantos-litros-para-tetra-neon'            => true,
	'quantos-litros-para-tetra-cardinal'        => true,
	'quantos-litros-para-mato-grosso'           => true,
);

aquametria_teste_carregar( $raiz );

/* ---------------------------------------------------------------------------
 * MODO BORDA — `... <slug> todas`
 *
 * Poe no ar as tres calculadoras que hoje estao em construcao (C2, C7, C8).
 * Existe por um motivo so, e ele e o da secao 8 do ARQUIPELAGO.md: com cinco
 * calculadoras no ar, nenhuma pagina chega a ter cinco irmas CANDIDATAS, entao
 * o teto de quatro do 16.4(c) nunca e exercitado — trocar o 4 por 5 no snippet
 * nao muda uma virgula do que o site serve, e o portao fica verde nas duas
 * versoes. Isso e grade que nao pisa na borda: quem mede so o mundo de hoje nao
 * separa "corta em 4" de "nunca chegou a 5".
 *
 * Entao a bancada FABRICA a borda em vez de esperar o mundo produzi-la. Este
 * modo nao existe no site e nao muda nada do modo normal — o filtro so e
 * registrado quando alguem pede, e e registrado DEPOIS dos snippets, para ser o
 * ultimo a falar sobre o hub.
 * ------------------------------------------------------------------------- */
if ( isset( $argv[3] ) && 'todas' === $argv[3] ) {
	$GLOBALS['__paginas']['calculadora-de-peso-e-carga']       = true;
	$GLOBALS['__paginas']['calculadora-de-consumo-de-energia'] = true;
	$GLOBALS['__paginas']['calculadora-de-lotacao']            = true;

	add_filter( 'aquametria_calculadoras', function ( $lista ) {
		foreach ( $lista as $i => $c ) {
			$lista[ $i ]['estado'] = 'publicada';
		}
		return $lista;
	} );
}

/* O conversor de Markdown vem do Sync, que o carregador pula de proposito (ele
   fala com o WordPress de verdade). As unicas coisas que o arquivo registra sao
   init, rest_api_init e o evento de cron, e nenhuma imprime nada. */
eval( file_get_contents( $raiz . '/snippets/aquametria-sync.php' ) );

/* ---------------------------------------------------------------------------
 * 1. O corpo e o titulo, pelos dois caminhos que o site tem
 * ------------------------------------------------------------------------- */

$arquivo_md = $raiz . '/conteudo/' . $alvo . '.md';
$paginas_casca = aquametria_casca_definicao_paginas();

if ( file_exists( $arquivo_md ) ) {
	/* Caminho A: pagina de conteudo/. Markdown pelo conversor do Sync, os
	   shortcodes do corpo executados, e o escape de "&" por cima. */
	$md = file_get_contents( $arquivo_md );

	/* O TITULO VEM DO MANIFEST, nao do front matter, e essa escolha custou um
	   desembarque inteiro para ser feita.

	   Quem grava o post_title no ar e o Sync, e o Sync le `titulo` do
	   manifest.json — o front matter do .md ele nem abre. Enquanto esta bancada
	   lia o .md, as duas metades liam fontes DIFERENTES para o mesmo dado, e o
	   dia em que os nove titulos foram reescritos o manifest ficou para tras:
	   293 afirmacoes verdes aqui, o Sync respondendo "18 aplicado(s)", o corpo
	   das nove paginas trocado no ar — e o H1 e o <title> das nove continuando
	   os de antes. Nenhum portao podia ver, porque todos renderizavam por aqui.

	   Agora a bancada le a MESMA fonte que o site: manifest desatualizado
	   aparece na primeira medicao, em vez de aparecer depois do desembarque.
	   Quem reespelha o front matter no manifest e ferramentas/atualizar-manifest.py,
	   e conferir-slugs.py cobra que os dois digam a mesma coisa. */
	$titulo = 'Aquametria';
	$manifesto = json_decode( (string) @file_get_contents( $raiz . '/manifest.json' ), true );
	if ( is_array( $manifesto ) && isset( $manifesto['conteudo'] ) ) {
		foreach ( $manifesto['conteudo'] as $entrada ) {
			if ( isset( $entrada['slug'], $entrada['titulo'] ) && $entrada['slug'] === $alvo ) {
				$titulo = $entrada['titulo'];
				break;
			}
		}
	}

	$html = aquametria_sync_md( $md );
	$html = preg_replace_callback(
		'/\[([a-z0-9_]+)\]/i',
		function ( $m ) {
			return isset( $GLOBALS['__shortcodes'][ $m[1] ] )
				? call_user_func( $GLOBALS['__shortcodes'][ $m[1] ] )
				: $m[0];
		},
		$html
	);
	$GLOBALS['__conteudo_pagina'] = $html;
	$corpo_cru = $html;
} elseif ( isset( $paginas_casca[ $alvo ] ) ) {
	/* Caminho B: uma das quatro paginas da casca, que sao shortcode puro. */
	$def = $paginas_casca[ $alvo ];
	$titulo = $def['titulo'];
	$tag    = trim( $def['conteudo'], '[]' );
	if ( ! isset( $GLOBALS['__shortcodes'][ $tag ] ) ) {
		fwrite( STDERR, "shortcode nao registrado: {$tag}\n" );
		exit( 2 );
	}
	$GLOBALS['__conteudo_pagina'] = $def['conteudo'];
	$corpo_cru = call_user_func( $GLOBALS['__shortcodes'][ $tag ] );
} else {
	fwrite( STDERR, "pagina desconhecida: {$alvo}\n" );
	fwrite( STDERR, 'conteudo/: ' . implode( ', ', array_map( 'basename', glob( $raiz . '/conteudo/*.md' ) ) ) . "\n" );
	fwrite( STDERR, 'casca: ' . implode( ', ', array_keys( $paginas_casca ) ) . "\n" );
	exit( 2 );
}

/* O escape que os filtros de texto do conteudo aplicam ao que o shortcode
   devolve. Vem ANTES do the_content de prioridade 20 — que e a ordem do site. */
$corpo = aquametria_teste_escapar_conteudo( $corpo_cru );

/* ---------------------------------------------------------------------------
 * 2. A pagina, montada na ordem do site
 * ------------------------------------------------------------------------- */

$marca     = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/site-title' ) );
$cabecalho = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/navigation' ) );

/* O H1 pelo MESMO bloco que o tema renderiza. E aqui que a trilha entra. */
$h1_cru = '<h1 class="wp-block-post-title">' . htmlspecialchars( $titulo, ENT_QUOTES ) . '</h1>';
$h1     = apply_filters( 'render_block', $h1_cru, array( 'blockName' => 'core/post-title' ) );

/* E aqui que o cluster entra. */
$corpo = apply_filters( 'the_content', $corpo );

ob_start(); do_action( 'wp_head' );   $cabeca = ob_get_clean();
ob_start(); do_action( 'wp_footer' ); $rodape = ob_get_clean();

/* O <title> como o NUCLEO monta: na home "<nome> – <blogdescription>"; na
   interna "<titulo da pagina> – <nome>". Medir outra forma seria bancada
   servindo o que o site nao serve. */
$titulo_aba = ( 'inicio' === $alvo )
	? 'Aquametria – ' . AQUAMETRIA_CASCA_TAGLINE_CURTA
	: $titulo . ' – Aquametria';

echo "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
	. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
	. '<title>' . htmlspecialchars( $titulo_aba, ENT_QUOTES ) . "</title>\n"
	. $cabeca . "</head>\n<body>\n"
	. "<header class=\"aqm-cabecalho-teste\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;\">\n"
	. $marca . "\n" . $cabecalho . "\n</header>\n"
	. "<main style=\"padding:1.2rem;\">\n"
	. $h1 . "\n"
	. $corpo . "\n</main>\n"
	. $rodape . "</body>\n</html>\n";

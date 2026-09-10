<?php
/**
 * Renderiza um ARTIGO de conteudo/ numa pagina HTML solta, do jeito que o site
 * a monta: o Markdown convertido pelo conversor do PROPRIO Sync, o shortcode da
 * resposta direta executado, o escape de "&" que os filtros do the_content
 * aplicam, e o wp_head/wp_footer por cima.
 *
 *   php ferramentas/render-artigo-para-teste.php . quantos-watts-de-aquecedor-para-aquario > /tmp/art-c5.html
 *   node ferramentas/teste-navegador-artigos.mjs /tmp
 *
 * Por que um renderizador separado do render-para-teste.php, e nao um modo dele:
 *
 *   1. Pagina de calculadora e um shortcode so; artigo e um arquivo Markdown
 *      inteiro que precisa passar pelo conversor do Sync. Sem isso o teste mede
 *      o HTML que a gente imaginou, nao o que o site serve.
 *   2. O snippet dos artigos se reconhece pelo SLUG, entao a pagina de teste
 *      precisa dizer qual slug ela e — e isso e o __slug_pagina que este arquivo
 *      define ANTES de carregar os snippets.
 *
 * O conversor vem de snippets/aquametria-sync.php, que o render-para-teste.php
 * pula de proposito (ele fala com o WordPress de verdade). Aqui ele e carregado
 * so pelo aquametria_sync_md(): as unicas coisas que o arquivo registra sao
 * init, rest_api_init e o evento de cron, e nenhuma delas imprime nada.
 */

$raiz  = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$slug  = isset( $argv[2] ) ? $argv[2] : 'quantos-watts-de-aquecedor-para-aquario';

$GLOBALS['__slug_pagina'] = $slug;

require __DIR__ . '/render-para-teste.php';

aquametria_teste_carregar( $raiz );
eval( file_get_contents( $raiz . '/snippets/aquametria-sync.php' ) );

$arquivo = $raiz . '/conteudo/' . $slug . '.md';
if ( ! file_exists( $arquivo ) ) {
	fwrite( STDERR, "artigo nao encontrado: $arquivo\n" );
	exit( 2 );
}

/* Titulo do <title>, como o WordPress faz: vem do front matter, nunca do corpo. */
$md     = file_get_contents( $arquivo );
$titulo = 'Aquametria';
if ( preg_match( '/^titulo:\s*"?(.+?)"?\s*$/m', $md, $m ) ) {
	$titulo = $m[1];
}

/* 1. Markdown -> HTML pelo conversor do proprio Sync. */
$html = aquametria_sync_md( $md );

/* 2. Os shortcodes que o corpo invoca. E aqui que a resposta direta nasce. */
$html = preg_replace_callback(
	'/\[([a-z0-9_]+)\]/i',
	function ( $m ) {
		return isset( $GLOBALS['__shortcodes'][ $m[1] ] )
			? call_user_func( $GLOBALS['__shortcodes'][ $m[1] ] )
			: $m[0];
	},
	$html
);

/* 3. O escape que os filtros de texto do conteudo aplicam. Um "&&" que passe por
      aqui vira "&#038;&#038;" e mata o script inteiro — foi o defeito de
      08/09/2026. O bloco da resposta direta nao tem script, e este passo existe
      justamente para provar isso a cada execucao. */
$corpo = aquametria_teste_escapar_conteudo( $html );

ob_start(); do_action( 'wp_head' );   $cabeca = ob_get_clean();
ob_start(); do_action( 'wp_footer' ); $rodape = ob_get_clean();

echo "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n<title>"
	. htmlspecialchars( $titulo, ENT_QUOTES ) . "</title>\n" . $cabeca . "</head>\n<body>\n"
	. $corpo . "\n" . $rodape . "</body>\n</html>\n";

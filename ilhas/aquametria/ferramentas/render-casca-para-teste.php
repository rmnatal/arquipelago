<?php
/**
 * Monta a CASCA numa pagina solta, para testar cabecalho e icone em navegador.
 *
 *   php ferramentas/render-casca-para-teste.php . > /tmp/casca.html
 *   node ferramentas/teste-navegador-casca.mjs /tmp/casca.html
 *
 * O render-para-teste.php monta pagina DE CALCULADORA: o corpo e o retorno de um
 * shortcode. O cabecalho da Aquametria nao vem de shortcode nenhum — vem do
 * filtro render_block, que troca o bloco core/navigation do tema. Entao aqui a
 * pagina e montada como o tema de blocos monta: wp_head, o cabecalho vindo do
 * filtro, o conteudo, e wp_footer.
 *
 * Uma diferenca que importa: o cabecalho NAO passa pelo escape de "&" dos
 * filtros de conteudo, porque no tema de blocos ele nao esta dentro do
 * the_content. O conteudo, esse sim, continua passando.
 */
require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

/* As tres paginas do menu existem neste site de teste. Sem isto a casca serve
   <span> em vez de <a> — de proposito, para nunca publicar link que da 404 —, e
   o teste estaria conferindo o caso errado. */
$GLOBALS['__paginas'] = array(
	'calculadoras' => true,
	'metodologia'  => true,
	'sobre'        => true,
);

aquametria_teste_carregar( $raiz );

$cabecalho = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/navigation' ) );
$marca     = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/site-title' ) );

$corpo = aquametria_teste_escapar_conteudo( '<h1>Página de teste da casca</h1><p>Corpo qualquer, só para a página ter altura.</p>' );

ob_start(); do_action( 'wp_head' );   $cabeca = ob_get_clean();
ob_start(); do_action( 'wp_footer' ); $rodape = ob_get_clean();

echo "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
	. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
	. "<title>Aquametria — teste da casca</title>\n" . $cabeca . "</head>\n<body>\n"
	. "<header class=\"aqm-cabecalho-teste\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;\">\n"
	. $marca . "\n" . $cabecalho . "\n</header>\n"
	. "<main style=\"padding:1.2rem;min-height:150vh;\">" . $corpo . "</main>\n"
	. $rodape . "</body>\n</html>\n";

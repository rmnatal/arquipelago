<?php
/**
 * Monta UMA pagina da casca inteira — cabeca, cabecalho, titulo, corpo e rodape —
 * para medir o que ela serve antes de publicar.
 *
 *   php ferramentas/render-casca-pagina.php . inicio > /tmp/aqm-inicio.html
 *
 * POR QUE ESTE ARQUIVO EXISTE, ao lado do render-casca-para-teste.php que ja
 * havia: aquele monta o cabecalho com um corpo FALSO ("Corpo qualquer, so para a
 * pagina ter altura"), porque o que ele mede e o menu do celular e o icone. Nao
 * dava para afirmar nada sobre o texto da home com ele — e a partir da 1.4.0 o
 * texto da home e justamente o que tem portao (secao 15 do ARQUIPELAGO.md).
 *
 * DUAS COISAS QUE A BANCADA IMITA DE PROPOSITO, e sem as quais ela mediria menos
 * do que o site serve — o erro que a Robometria pagou tres vezes (secao 8):
 *
 *   1. O H1. No site quem imprime o titulo da pagina e o tema de blocos, a
 *      partir do post_title. Aqui ele sai de aquametria_casca_definicao_paginas(),
 *      que e a MESMA definicao que a casca grava no WordPress desde a 1.4.0.
 *   2. O cabecalho. Ele nao vem de shortcode nenhum: vem do filtro render_block,
 *      que troca core/site-title e core/navigation do tema.
 *
 * E UMA QUE ELE NAO IMITA, declarada para ninguem se enganar: este arquivo monta
 * UMA pagina por processo. Quem quiser medir as quatro chama o comando quatro
 * vezes. Montar varias no mesmo processo faz o que tem `static` dentro (a marca,
 * o estilo, o id do menu) sair na primeira e sumir nas seguintes — a bancada da
 * Robometria mediu 915 KB do que no ar tem 960 KB exatamente assim, sem erro
 * nenhum aparecer.
 */
require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$alvo = isset( $argv[2] ) ? $argv[2] : 'inicio';

/* O que 'existe publicado' neste site de teste. Sem o mapa a casca serve <span>
   em vez de <a> — de proposito, para nunca publicar link que da 404 —, e o teste
   estaria medindo o caso errado. Aqui entram as quatro paginas da casca, as
   cinco calculadoras no ar, a pagina de afiliados e os tres artigos-ancora. */
$GLOBALS['__paginas'] = array(
	'inicio'                                 => true,
	'calculadoras'                           => true,
	'metodologia'                            => true,
	'sobre'                                  => true,
	'divulgacao-de-afiliados'                => true,
	'calculadora-de-litragem'                => true,
	'calculadora-de-vazao-do-filtro'         => true,
	'calculadora-de-potencia-do-aquecedor'   => true,
	'calculadora-de-midia-filtrante'         => true,
	'calculadora-de-iluminacao'              => true,
	'quantos-watts-de-aquecedor-para-aquario' => true,
	'quanta-midia-biologica-o-aquario-precisa' => true,
	'quantos-lumens-por-litro-aquario-plantado' => true,
);

$GLOBALS['__slug_pagina']   = $alvo;
$GLOBALS['__pagina_inicial'] = ( 'inicio' === $alvo );

aquametria_teste_carregar( $raiz );

$paginas = aquametria_casca_definicao_paginas();
if ( ! isset( $paginas[ $alvo ] ) ) {
	fwrite( STDERR, "pagina desconhecida: {$alvo}\n" );
	fwrite( STDERR, 'conhecidas: ' . implode( ', ', array_keys( $paginas ) ) . "\n" );
	exit( 2 );
}

$def = $paginas[ $alvo ];

/* O corpo: o retorno do shortcode, passando pelo mesmo escape de "&" que os
   filtros do the_content aplicam no site. */
$tag = trim( $def['conteudo'], '[]' );
if ( ! isset( $GLOBALS['__shortcodes'][ $tag ] ) ) {
	fwrite( STDERR, "shortcode nao registrado: {$tag}\n" );
	exit( 2 );
}
$GLOBALS['__conteudo_pagina'] = $def['conteudo'];
$retorno = call_user_func( $GLOBALS['__shortcodes'][ $tag ] );
$corpo   = aquametria_teste_escapar_conteudo( $retorno );

$cabecalho = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/navigation' ) );
$marca     = apply_filters( 'render_block', '<!-- bloco do tema -->', array( 'blockName' => 'core/site-title' ) );

ob_start(); do_action( 'wp_head' );   $cabeca = ob_get_clean();
ob_start(); do_action( 'wp_footer' ); $rodape = ob_get_clean();

/* O <title> montado como o NUCLEO do WordPress monta, e nao como desse jeito
   ficasse bonito: na home e "<nome do site> – <blogdescription>"; na pagina
   interna e "<titulo da pagina> – <nome do site>". Medir aqui um titulo com
   outra forma seria bancada servindo o que o site nao serve — e foi assim que a
   tagline antiga ("Calculadoras e dados tecnicos para dimensionar o seu
   aquario") ficou no titulo da home sem nenhum teste ver, ate 11/09/2026. */
$titulo_aba = ( 'inicio' === $alvo )
	? 'Aquametria – ' . AQUAMETRIA_CASCA_TAGLINE_CURTA
	: $def['titulo'] . ' – Aquametria';

echo "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
	. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
	. '<title>' . htmlspecialchars( $titulo_aba, ENT_QUOTES ) . "</title>\n"
	. $cabeca . "</head>\n<body>\n"
	. "<header class=\"aqm-cabecalho-teste\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;\">\n"
	. $marca . "\n" . $cabecalho . "\n</header>\n"
	. "<main style=\"padding:1.2rem;\">\n"
	. '<h1 class="aqm-titulo-pagina">' . htmlspecialchars( $def['titulo'], ENT_QUOTES ) . "</h1>\n"
	. $corpo . "\n</main>\n"
	. $rodape . "</body>\n</html>\n";

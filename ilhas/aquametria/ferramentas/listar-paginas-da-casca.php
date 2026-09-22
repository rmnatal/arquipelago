<?php
/**
 * Imprime, em JSON, TODAS as paginas que a casca cria no WordPress.
 *
 *   php ferramentas/listar-paginas-da-casca.php .
 *
 * POR QUE ELE EXISTE, e a resposta tem data: 22/09/2026, a leva 7 achou quatro
 * paginas no ar havia OITO DIAS que o portao da voz nao media, porque a lista
 * daquele portao era escrita a mao e ninguem a alimentou na leva 6. O portao
 * ficou verde medindo 36 das 40 paginas do site, sem uma falha que avisasse.
 *
 * Quem sabe quais paginas a casca publica e a PROPRIA casca:
 * `aquametria_casca_definicao_paginas()` e a definicao que ela grava no
 * WordPress, e desde a 1.7.0 ela ja traz tambem o que o eixo /peixes/ anuncia
 * pelo filtro `aquametria_paginas`. Este arquivo so pergunta a ela.
 *
 * Ele NAO decide nada e NAO le o banco nem o manifest: devolve slug, titulo e
 * pai, e quem separa a casca do eixo, ou cobra a cobertura, e quem mede. E o
 * mesmo desenho do `listar-paginas-do-eixo.php` e do
 * `listar-categorias-do-eixo.php`, pelo mesmo motivo dos dois: lista escrita a
 * mao envelhece calada, e portao que envelhece calado e pior que portao nenhum.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'inicio';
$GLOBALS['__paginas']     = array();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

if ( ! function_exists( 'aquametria_casca_definicao_paginas' ) ) {
	fwrite( STDERR, "FALHA: aquametria_casca_definicao_paginas() nao foi carregada.\n" );
	exit( 1 );
}

$saida = array();
foreach ( aquametria_casca_definicao_paginas() as $slug => $def ) {
	$saida[ $slug ] = array(
		'titulo' => isset( $def['titulo'] ) ? $def['titulo'] : '',
		'pai'    => isset( $def['pai'] ) ? $def['pai'] : '',
	);
}

if ( ! count( $saida ) ) {
	fwrite( STDERR, "FALHA: a casca nao declarou pagina nenhuma.\n" );
	exit( 1 );
}

echo json_encode( $saida, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ), "\n";

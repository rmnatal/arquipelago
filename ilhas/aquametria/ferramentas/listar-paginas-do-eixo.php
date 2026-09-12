<?php
/**
 * Imprime, em JSON, as paginas que o snippet do eixo /peixes/ registra.
 *
 *   php ferramentas/listar-paginas-do-eixo.php .
 *
 * POR QUE ELE EXISTE. O `gerar-metas-descricao.py` tinha a lista das 13 URLs do
 * sitemap ESCRITA A MAO, com um comentario dizendo "pagina nova entra aqui no
 * mesmo commit em que entra no site — a recusa e o alarme". A leva 1 do eixo
 * /peixes/ publicou cinco URLs em 12/09/2026 e nao tocou nessa lista: o alarme
 * era uma lista digitada, entao ele ficou calado, e as cinco foram ao ar sem
 * <meta name="description"> e sem uma tag og:. Medido no ar em 12/09/2026, com
 * as 13 antigas servindo a delas normalmente — que e o que prova que o defeito
 * era da lista e nao do snippet de SEO.
 *
 * E a mesma cicatriz do "numero de tela nasce contado, nunca digitado" (secao 8
 * do ARQUIPELAGO.md), aplicada a uma lista de portao em vez de a um numero de
 * tela: lista escrita a mao envelhece calada, e portao que envelhece calado e
 * pior que portao nenhum, porque quem le o comentario acredita nele.
 *
 * Entao quem sabe quais paginas o eixo tem e o PROPRIO eixo, e este arquivo so
 * pergunta a ele. Nao decide nada, nao le o banco e nao olha descricao: devolve
 * slug, nivel, pai e titulo, e quem cobra a descricao e o gerador.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'peixes';
$GLOBALS['__paginas']     = array();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

if ( ! function_exists( 'aquametria_peixes_registro' ) ) {
	fwrite( STDERR, "FALHA: aquametria_peixes_registro() nao foi carregada.\n" );
	exit( 1 );
}

$saida = array();
foreach ( aquametria_peixes_registro() as $slug => $def ) {
	$saida[ $slug ] = array(
		'nivel'   => $def['nivel'],
		'pai'     => $def['pai'],
		'titulo'  => $def['titulo'],
		'especie' => isset( $def['especie'] ) ? $def['especie'] : null,
	);
}

echo json_encode( $saida, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ), "\n";

<?php
/**
 * Imprime, em JSON, a PROMESSA NUMERICA do <title> que cada pagina da ilha
 * resolve hoje — e resolve chamando o proprio snippet, nao relendo o banco.
 *
 *   php ferramentas/listar-promessas.php .
 *
 * POR QUE ELE EXISTE, e e a mesma cicatriz do listar-paginas-do-eixo.php um
 * andar acima. A promessa do titulo e um numero que sai do banco em tempo de
 * execucao (secao 2c do aquametria-seo-tecnico.php): o C3 pergunta as bandas de
 * turnover, o C12 as ancoras de midia, o C15 os niveis de lumen, o C5 as regras
 * de W/L e a ficha do betta a base declarada da especie. Um portao que quisesse
 * conferir esses numeros tinha duas saidas, e uma delas e armadilha:
 *
 *   (a) reimplementar a conta em Python — e entao as DUAS metades erram juntas
 *       no dia em que o banco mudar de forma, porque quem erra e a leitura e nao
 *       a conta. E o que o teste-titulos-das-duas-fontes.py chama de "carregar o
 *       PHP para perguntar faria as duas metades errarem juntas";
 *   (b) PERGUNTAR ao snippet qual frase ele serve, e afirmar sobre a frase.
 *
 * Este arquivo e o (b). Ele nao decide nada, nao escolhe pagina e nao mede
 * tamanho: devolve, por slug, a promessa resolvida e a lista de ganchos que a
 * declararam. Quem cobra teto, quem cobra que a meta description cite o mesmo
 * numero e quem cobra que a pagina de controle NAO tenha promessa e o
 * ferramentas/teste-promessa-do-titulo.py.
 *
 * A PAGINA DE CONTROLE APARECE AQUI COM PROMESSA VAZIA, de proposito: a
 * /calculadora-de-litragem/ ficou parada na Proposta 2 da leitura de 07/10/2026
 * para a leitura de 14/10 ter com o que comparar. Promessa vazia e um resultado,
 * nao a ausencia de um — e por isso ela sai no JSON como string vazia em vez de
 * sair de fora.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'inicio';
$GLOBALS['__paginas']     = array();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

foreach ( array( 'aquametria_seo_metas_por_slug', 'aquametria_seo_promessa_do_titulo' ) as $f ) {
	if ( ! function_exists( $f ) ) {
		fwrite( STDERR, "FALHA: $f() nao foi carregada.\n" );
		exit( 1 );
	}
}

$saida = array();
foreach ( aquametria_seo_metas_por_slug() as $slug => $meta ) {
	$GLOBALS['__slug_pagina'] = $slug;
	$saida[ $slug ] = array(
		'titulo'   => isset( $meta['titulo'] ) ? $meta['titulo'] : '',
		'promessa' => aquametria_seo_promessa_do_titulo( $slug ),
	);
}

echo json_encode( $saida, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ), "\n";

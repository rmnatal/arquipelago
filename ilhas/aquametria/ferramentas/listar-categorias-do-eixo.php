<?php
/**
 * Imprime, em JSON, as categorias que o snippet do eixo /peixes/ declara.
 *
 *   php ferramentas/listar-categorias-do-eixo.php .
 *
 * POR QUE ELE EXISTE, e a resposta e uma pergunta que ficou dois blocos sem
 * dono: quem mede a CATEGORIA PREPARADA?
 *
 * Uma categoria deste eixo tem duas vidas. Antes da leva ela existe apenas como
 * declaracao — rotulo, `linha_mestra` e `criterio` escritos, `especies` vazio e
 * nenhuma pagina no registro. Depois da leva ela e uma URL, e ai o
 * `teste-peixes.py` inteiro passa por ela: trilha, tabela, irmas, schema, voz.
 *
 * A primeira vida nunca foi medida. A `bettas` recebeu `criterio` e
 * `linha_mestra` em 13/09/2026 (peixes 1.3.0) e NADA conferia que eles estavam
 * la, nem que a familia que aquele texto declara como criterio tem no banco as
 * tres filhas que o 16.5 exige — as duas coisas que decidem se a leva pode
 * nascer. Ou seja: a preparacao da leva era exatamente o tipo de afirmacao que
 * este eixo ja pagou caro para aprender a cobrar, escrita em prosa e conferida
 * a olho.
 *
 * Ele NAO decide nada e NAO le o banco: devolve o que o snippet declara, e quem
 * recomputa o banco e cobra as duas metades e o `teste-peixes.py`, com a regua
 * dele. Se este arquivo lesse o banco, as duas metades errariam juntas — a
 * cicatriz 1 do cabecalho daquele arquivo.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'peixes';
$GLOBALS['__paginas']     = array();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

if ( ! function_exists( 'aquametria_peixes_categorias' ) ) {
	fwrite( STDERR, "FALHA: aquametria_peixes_categorias() nao foi carregada.\n" );
	exit( 1 );
}

$saida = array();
foreach ( aquametria_peixes_categorias() as $slug => $def ) {
	$saida[ $slug ] = array(
		'rotulo'       => isset( $def['rotulo'] ) ? $def['rotulo'] : '',
		'linha_mestra' => isset( $def['linha_mestra'] ) ? $def['linha_mestra'] : '',
		'criterio'     => isset( $def['criterio'] ) ? $def['criterio'] : '',
		'especies'     => isset( $def['especies'] ) ? array_values( (array) $def['especies'] ) : array(),
	);
}

echo json_encode( $saida, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ), "\n";

<?php
/**
 * Exercita o redirecionamento de apelidos da casca (seção 1b) sem WordPress.
 *
 *   php ferramentas/teste-apelidos.php .
 *
 * Confere três coisas, e a terceira é a que importa mais:
 *   1. cada apelido conhecido resolve para o slug canônico;
 *   2. endereço desconhecido, vazio ou com mais de um segmento NÃO resolve
 *      (redirecionar o que não é apelido sequestraria página legítima);
 *   3. TODO destino do mapa é um slug que existe em conteudo/ — apelido que
 *      aponta para página inexistente troca um 404 por outro.
 */
$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

function sanitize_title( $t ) { return strtolower( preg_replace( '/[^a-z0-9]+/i', '-', $t ) ); }
function apply_filters( $h, $v ) { return $v; }
function add_action( $h, $f, $p = 10, $a = 1 ) {}
function add_filter( $h, $f, $p = 10, $a = 1 ) {}
function add_shortcode( $t, $f ) {}
function did_action( $h ) { return 0; }
define( 'ABSPATH', '/tmp/wp/' );

/* Só as funções da seção 1b interessam; o resto do snippet pede meio WordPress. */
$src = file_get_contents( $raiz . '/snippets/aquametria-casca.php' );
$ini = strpos( $src, "function aquametria_casca_apelidos()" );
$fim = strpos( $src, "if ( ! function_exists( 'aquametria_casca_redirecionar_apelido' ) )" );
if ( false === $ini || false === $fim ) {
	fwrite( STDERR, "FALHA: a seção 1b da casca não foi encontrada no snippet.\n" );
	exit( 1 );
}
eval( "if ( ! function_exists( 'aquametria_casca_apelidos' ) ) {\nfunction " . substr( $src, $ini + strlen( 'function ' ), $fim - $ini - strlen( 'function ' ) ) . "\n" );

$falhas = 0; $casos = 0;
function afirmar( $cond, $rotulo ) {
	global $falhas, $casos;
	$casos++;
	if ( ! $cond ) { $falhas++; echo "  FALHA  $rotulo\n"; }
}

$mapa = aquametria_casca_apelidos();
echo "apelidos no mapa: " . count( $mapa ) . "\n";

/* 1. cada apelido resolve, inclusive com barras em volta */
foreach ( $mapa as $apelido => $canonico ) {
	afirmar( aquametria_casca_apelido_para_slug( $apelido ) === $canonico, "apelido '$apelido'" );
	afirmar( aquametria_casca_apelido_para_slug( '/' . $apelido . '/' ) === $canonico, "apelido '/$apelido/' com barras" );
}

/* 2. o que não é apelido não pode resolver */
foreach ( array( '', '/', 'metodologia', 'calculadoras', 'sobre', 'calculadora-de-litragem',
                 'calculadora-de-potencia-do-aquecedor', 'blog/calculadora-de-aquecedor', 'wp-admin' ) as $fora ) {
	afirmar( '' === aquametria_casca_apelido_para_slug( $fora ), "não-apelido '$fora' deve devolver vazio" );
}

/* 3. todo destino existe em conteudo/ */
$slugs = array();
foreach ( glob( $raiz . '/conteudo/*.md' ) as $arq ) {
	if ( preg_match( '/^---\s*$.*?^slug:\s*(.+?)\s*$/ms', file_get_contents( $arq ), $m ) ) {
		$slugs[ trim( $m[1], "\"' " ) ] = true;
	}
}
foreach ( array_unique( array_values( $mapa ) ) as $destino ) {
	afirmar( isset( $slugs[ $destino ] ), "destino '$destino' precisa existir em conteudo/" );
}

/* controle negativo: um apelido inventado não pode passar */
afirmar( '' === aquametria_casca_apelido_para_slug( 'calculadora-de-coisa-nenhuma' ), 'controle negativo' );

echo "afirmações: $casos · falhas: $falhas\n";
exit( $falhas ? 1 : 0 );

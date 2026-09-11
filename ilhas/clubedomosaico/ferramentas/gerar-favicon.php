<?php
/**
 * Embute o favicon da ilha dentro do snippet da casca, entre os marcadores.
 *
 *   php ferramentas/gerar-favicon.php .
 *
 * POR QUE ESTA FERRAMENTA E DIFERENTE DA DA ROBOMETRIA: la o icone e DESENHADO
 * em codigo, porque o simbolo daquela ilha e geometria (um encaixe) e desenho
 * mantido em dois lugares diverge em silencio. Aqui o simbolo e ARTE ENTREGUE —
 * a lotus que o Raphael subiu em 11/09/2026 —, e o PROMPT.md da ilha proibe
 * redesenhar, vetorizar ou trocar as cores dela. Entao esta ferramenta nao
 * desenha nada: ela LE identidade/logo/favicon-32.png e grava o base64 dele no
 * snippet.
 *
 * A razao de existir e a mesma das duas: o data URI nao se edita a mao. Quem
 * trocar o PNG da pasta roda isto e o snippet acompanha; sem a ferramenta,
 * alguem colaria base64 a mao no arquivo e ninguem saberia de qual imagem ele
 * veio.
 *
 * Sai com codigo 1 quando nao consegue fazer o servico, para nao passar em
 * silencio por um snippet que ficou com o icone velho.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$origem  = $raiz . '/identidade/logo/favicon-32.png';
$destino = $raiz . '/snippets/clubedomosaico-casca.php';

if ( ! is_readable( $origem ) ) {
	fwrite( STDERR, "nao achei $origem\n" );
	exit( 1 );
}
if ( ! is_readable( $destino ) ) {
	fwrite( STDERR, "nao achei $destino\n" );
	exit( 1 );
}

$png = file_get_contents( $origem );

/* Confere que e mesmo um PNG de 32x32, e nao outro arquivo renomeado: o
   navegador aceitaria qualquer coisa e a aba ficaria errada sem aviso. */
if ( "\x89PNG\r\n\x1a\n" !== substr( $png, 0, 8 ) ) {
	fwrite( STDERR, "$origem nao e um PNG\n" );
	exit( 1 );
}
$cabecalho = unpack( 'Nlargura/Naltura', substr( $png, 16, 8 ) );
if ( 32 !== $cabecalho['largura'] || 32 !== $cabecalho['altura'] ) {
	fwrite( STDERR, "esperava 32x32 e achei {$cabecalho['largura']}x{$cabecalho['altura']}\n" );
	exit( 1 );
}

$base64 = base64_encode( $png );

$fonte = file_get_contents( $destino );
$novo  = preg_replace(
	"/(define\( 'CDM_CASCA_ICONE_PNG_32', ')[^']*('\ \);)/",
	'${1}' . $base64 . '${2}',
	$fonte,
	1,
	$trocas
);

if ( 1 !== $trocas || null === $novo ) {
	fwrite( STDERR, "nao achei a constante CDM_CASCA_ICONE_PNG_32 entre os marcadores\n" );
	exit( 1 );
}

file_put_contents( $destino, $novo );

printf(
	"favicon embutido: %d bytes de PNG %dx%d viraram %d bytes de base64 em %s\n",
	strlen( $png ),
	$cabecalho['largura'],
	$cabecalho['altura'],
	strlen( $base64 ),
	basename( $destino )
);

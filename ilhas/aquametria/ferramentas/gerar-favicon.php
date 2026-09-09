<?php
/**
 * Gera o icone do site da Aquametria e grava o bloco de constantes dentro do
 * snippet da casca, entre os marcadores FAVICON-INICIO e FAVICON-FIM.
 *
 *   php ferramentas/gerar-favicon.php .
 *
 * Por que existe um GERADOR para um icone:
 *
 *   1. O icone e o MESMO desenho do logotipo (recipiente graduado com linha de
 *      enchimento). Ele mora aqui uma vez so; quem mexer na marca mexe neste
 *      arquivo e roda o gerador, em vez de manter dois desenhos que divergem em
 *      silencio.
 *   2. O apple-touch-icon PRECISA ser PNG — o iOS nao aceita SVG nesse rel. E a
 *      regra do projeto proibe subir arquivo para a biblioteca de midia do
 *      WordPress, entao o PNG viaja como data URI base64 dentro do snippet,
 *      igual ao catalogo de produtos que viaja dentro da calculadora.
 *
 * Duas decisoes de desenho, e cada uma tem motivo:
 *
 *   - O SVG da aba tem canto arredondado; o PNG do iOS NAO tem. O iOS aplica a
 *     propria mascara em cima do arquivo, e canto arredondado por baixo da
 *     mascara vira borda dupla.
 *   - Nenhum dos dois tem a marca escrita. A 16 px o wordmark vira borrao; o
 *     que sobrevive e o recipiente com a lamina d'agua.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

const AQM_TINTA  = array( 0x0D, 0x1B, 0x22 );
const AQM_LAMINA = array( 0x0E, 0x7C, 0x8C );
const AQM_PAPEL  = array( 0xFF, 0xFF, 0xFF );

/* ---------------------------------------------------------------------------
 * O desenho, em coordenadas de uma grade de 32 x 32. As duas saidas leem daqui.
 * ------------------------------------------------------------------------- */

function aqm_icone_svg( $arredondar = true ) {
	$svg  = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">';
	$svg .= $arredondar
		? '<rect width="32" height="32" rx="6" fill="#0D1B22"/>'
		: '<rect width="32" height="32" fill="#0D1B22"/>';
	// Aro do recipiente.
	$svg .= '<rect x="7" y="4" width="18" height="1.8" rx=".9" fill="#FFFFFF"/>';
	// Corpo do recipiente, fundo arredondado.
	$svg .= '<path d="M9 6.6h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#FFFFFF"/>';
	// Lamina d\'agua.
	$svg .= '<path d="M9 17.4h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#0E7C8C"/>';
	// Graduacao, so na parte clara: a 16 px duas marcas e o limite do legivel.
	$svg .= '<g fill="#0D1B22"><rect x="11.6" y="9.6" width="8.8" height="1.8" rx=".9"/>';
	$svg .= '<rect x="11.6" y="13.2" width="5.4" height="1.8" rx=".9"/></g>';
	$svg .= '</svg>';

	return $svg;
}

/* ---------------------------------------------------------------------------
 * PNG do apple-touch-icon: desenha em 4x e reduz, que e como se consegue borda
 * suave com a GD sem antialias de poligono.
 * ------------------------------------------------------------------------- */

function aqm_cor( $im, $rgb ) {
	return imagecolorallocate( $im, $rgb[0], $rgb[1], $rgb[2] );
}

/** Retangulo de cantos arredondados. $cantos: quais arredondar (cima/baixo). */
function aqm_retangulo( $im, $x1, $y1, $x2, $y2, $r, $cor, $cima = true, $baixo = true ) {
	$rc = $cima ? $r : 0;
	$rb = $baixo ? $r : 0;
	imagefilledrectangle( $im, (int) $x1, (int) ( $y1 + $rc ), (int) $x2, (int) ( $y2 - $rb ), $cor );
	imagefilledrectangle( $im, (int) ( $x1 + $rc ), (int) $y1, (int) ( $x2 - $rc ), (int) ( $y1 + $rc ), $cor );
	imagefilledrectangle( $im, (int) ( $x1 + $rb ), (int) ( $y2 - $rb ), (int) ( $x2 - $rb ), (int) $y2, $cor );
	$d = (int) ( 2 * $r );
	if ( $cima ) {
		imagefilledarc( $im, (int) ( $x1 + $r ), (int) ( $y1 + $r ), $d, $d, 180, 270, $cor, IMG_ARC_PIE );
		imagefilledarc( $im, (int) ( $x2 - $r ), (int) ( $y1 + $r ), $d, $d, 270, 360, $cor, IMG_ARC_PIE );
	}
	if ( $baixo ) {
		imagefilledarc( $im, (int) ( $x1 + $r ), (int) ( $y2 - $r ), $d, $d, 90, 180, $cor, IMG_ARC_PIE );
		imagefilledarc( $im, (int) ( $x2 - $r ), (int) ( $y2 - $r ), $d, $d, 0, 90, $cor, IMG_ARC_PIE );
	}
}

function aqm_icone_png_base64( $lado = 180 ) {
	$s   = 24;            // 32 unidades x 24 = 768 px de tela de desenho
	$tam = 32 * $s;
	$im  = imagecreatetruecolor( $tam, $tam );
	imagealphablending( $im, true );

	$tinta  = aqm_cor( $im, AQM_TINTA );
	$lamina = aqm_cor( $im, AQM_LAMINA );
	$papel  = aqm_cor( $im, AQM_PAPEL );

	// Fundo em sangria, SEM canto arredondado: a mascara e do iOS.
	imagefilledrectangle( $im, 0, 0, $tam - 1, $tam - 1, $tinta );

	// Aro.
	aqm_retangulo( $im, 7 * $s, 4 * $s, 25 * $s, 5.8 * $s, 0.9 * $s, $papel );
	// Corpo do recipiente: topo reto, fundo arredondado.
	aqm_retangulo( $im, 9 * $s, 6.6 * $s, 23 * $s, 28 * $s, 4 * $s, $papel, false, true );
	// Lamina d'agua.
	aqm_retangulo( $im, 9 * $s, 17.4 * $s, 23 * $s, 28 * $s, 4 * $s, $lamina, false, true );
	// Graduacao.
	aqm_retangulo( $im, 11.6 * $s, 9.6 * $s, 20.4 * $s, 11.4 * $s, 0.9 * $s, $tinta );
	aqm_retangulo( $im, 11.6 * $s, 13.2 * $s, 17 * $s, 15 * $s, 0.9 * $s, $tinta );

	$pequeno = imagescale( $im, $lado, $lado, IMG_BICUBIC );

	/* O desenho tem tres cores; a reducao bicubica inventa milhares delas nas
	   bordas e o PNG truecolor sai com 9 KB, que viram 12 KB de base64 dentro do
	   snippet. Reduzir para 64 cores devolve o arquivo ao tamanho de um icone e
	   nao muda o que se ve: o degrade de borda cabe folgado em 64 tons. */
	imagetruecolortopalette( $pequeno, true, 64 );

	ob_start();
	imagepng( $pequeno, null, 9 );
	$bin = ob_get_clean();

	imagedestroy( $im );
	imagedestroy( $pequeno );

	return base64_encode( $bin );
}

/* ---------------------------------------------------------------------------
 * Grava o bloco no snippet da casca.
 * ------------------------------------------------------------------------- */

$svg_aba   = aqm_icone_svg( true );
$png_ios   = aqm_icone_png_base64( 180 );
$png_aba   = aqm_icone_png_base64( 32 );
$arquivo   = $raiz . '/snippets/aquametria-casca.php';
$src       = file_get_contents( $arquivo );

$bloco  = "/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */\n";
$bloco .= "if ( ! defined( 'AQUAMETRIA_CASCA_ICONE_SVG' ) ) {\n";
$bloco .= "\tdefine( 'AQUAMETRIA_CASCA_ICONE_SVG', '" . str_replace( "'", "\\'", $svg_aba ) . "' );\n";
$bloco .= "\tdefine( 'AQUAMETRIA_CASCA_ICONE_PNG_180', '" . $png_ios . "' );\n";
$bloco .= "\tdefine( 'AQUAMETRIA_CASCA_ICONE_PNG_32', '" . $png_aba . "' );\n";
$bloco .= "}\n";
$bloco .= '/* FAVICON-FIM */';

$padrao = '/\/\* FAVICON-INICIO.*?\/\* FAVICON-FIM \*\//s';
if ( ! preg_match( $padrao, $src ) ) {
	fwrite( STDERR, "FALHA: marcadores FAVICON-INICIO/FAVICON-FIM não encontrados em $arquivo\n" );
	exit( 1 );
}
$novo = preg_replace( $padrao, str_replace( '\\', '\\\\', $bloco ), $src );
file_put_contents( $arquivo, $novo );

// Copia solta para conferência visual; NÃO vai para o site nem para o repositório.
if ( isset( $argv[2] ) ) {
	file_put_contents( $argv[2], base64_decode( $png_ios ) );
}

printf(
	"favicon gerado: SVG de %d bytes; PNG 180 de %d bytes (%d em base64); PNG 32 de %d bytes (%d em base64)\n",
	strlen( $svg_aba ),
	strlen( base64_decode( $png_ios ) ),
	strlen( $png_ios ),
	strlen( base64_decode( $png_aba ) ),
	strlen( $png_aba )
);

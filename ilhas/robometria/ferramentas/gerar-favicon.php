<?php
/**
 * Gera o icone do site da Robometria e grava o bloco de constantes dentro do
 * snippet da casca, entre os marcadores FAVICON-INICIO e FAVICON-FIM.
 *
 *   php ferramentas/gerar-favicon.php .
 *   php ferramentas/gerar-favicon.php . /tmp/icone.png   (copia solta para olhar)
 *
 * Por que existe um GERADOR para um icone:
 *
 *   1. O icone e o MESMO desenho do logotipo (anel aberto + peca com lingueta).
 *      Ele mora aqui uma vez so; quem mexer na marca mexe neste arquivo e roda o
 *      gerador, em vez de manter dois desenhos que divergem em silencio.
 *   2. O apple-touch-icon PRECISA ser PNG — o iOS nao aceita SVG nesse rel. E a
 *      regra do projeto proibe subir arquivo para a biblioteca de midia do
 *      WordPress, entao o PNG viaja como data URI base64 dentro do snippet.
 *
 * Tres decisoes de desenho, e cada uma tem motivo:
 *
 *   - O SVG da aba tem canto arredondado; o PNG do iOS NAO tem. O iOS aplica a
 *     propria mascara em cima do arquivo, e canto arredondado por baixo da
 *     mascara vira borda dupla.
 *   - Nenhum dos dois tem a marca escrita. A 16 px o wordmark vira borrao; o que
 *     sobrevive e o encaixe.
 *   - O icone e desenhado no FUNDO GRAFITE, com o anel em piso claro e a peca em
 *     varredura. Na aba, o anel precisa de contraste contra a barra do navegador,
 *     e a peca vermelha e o unico ponto de cor — que e exatamente a regra da
 *     marca: um uso de varredura por tela.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

const RBM_TINTA     = array( 0x16, 0x19, 0x1D );
const RBM_VARREDURA = array( 0xCC, 0x33, 0x11 );
const RBM_PISO      = array( 0xF2, 0xF1, 0xEF );

/* ---------------------------------------------------------------------------
 * O desenho, numa grade de 32 x 32. As duas saidas leem daqui.
 *
 * A geometria e a do PROMPT.md da ilha (viewBox 48, anel de raio 15 com corte de
 * 50 graus a direita, peca com lingueta entrando no corte), reduzida por 2/3 e
 * arredondada para a grade de 32 — em 16 px o traco de 2 unidades e o limite do
 * que sobrevive.
 * ------------------------------------------------------------------------- */

/** Centro do anel, raio e meia-abertura do corte, na grade de 32. */
const RBM_CX    = 14.0;
const RBM_CY    = 16.0;
const RBM_R     = 9.0;
const RBM_TRACO = 2.2;
const RBM_CORTE = 25.0; // graus para cada lado do eixo horizontal direito

/** Ponto do anel no angulo dado (graus, 0 = direita, y cresce para baixo). */
function rbm_ponto( $graus, $raio = RBM_R ) {
	$r = deg2rad( $graus );
	return array( RBM_CX + $raio * cos( $r ), RBM_CY + $raio * sin( $r ) );
}

function rbm_icone_svg( $arredondar = true ) {
	list( $x1, $y1 ) = rbm_ponto( -RBM_CORTE );
	list( $x2, $y2 ) = rbm_ponto( RBM_CORTE );

	$svg  = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">';
	$svg .= $arredondar
		? '<rect width="32" height="32" rx="6" fill="#16191D"/>'
		: '<rect width="32" height="32" fill="#16191D"/>';
	// Anel aberto: do angulo -25 ate +25 pelo lado de fora, deixando o corte a direita.
	$svg .= sprintf(
		'<path d="M%s %s A%s %s 0 1 0 %s %s" fill="none" stroke="#F2F1EF" stroke-width="%s" stroke-linecap="round"/>',
		rbm_n( $x1 ), rbm_n( $y1 ), rbm_n( RBM_R ), rbm_n( RBM_R ), rbm_n( $x2 ), rbm_n( $y2 ), rbm_n( RBM_TRACO )
	);
	// A peca, com a lingueta entrando no corte. Unico vermelho do icone.
	$svg .= '<path d="M24 10 h4.6 v12 h-4.6 v-3 h-2.4 v-6 h2.4 z" fill="#CC3311"/>';
	$svg .= '</svg>';

	return $svg;
}

/** Numero curto no SVG: sem zero a direita, para o data URI nao inchar. */
function rbm_n( $v ) {
	return rtrim( rtrim( number_format( (float) $v, 2, '.', '' ), '0' ), '.' );
}

/* ---------------------------------------------------------------------------
 * PNG do apple-touch-icon: desenha em escala alta e reduz, que e como se
 * consegue borda suave com a GD sem antialias de poligono.
 * ------------------------------------------------------------------------- */

function rbm_cor( $im, $rgb ) {
	return imagecolorallocate( $im, $rgb[0], $rgb[1], $rgb[2] );
}

function rbm_retangulo( $im, $x1, $y1, $x2, $y2, $cor ) {
	imagefilledrectangle( $im, (int) round( $x1 ), (int) round( $y1 ), (int) round( $x2 ), (int) round( $y2 ), $cor );
}

/**
 * O anel aberto, desenhado como coroa circular com o setor do corte poupado.
 * imagefilledarc nao sabe fazer coroa, entao a coroa sai de dois arcos: o de
 * fora na cor do anel e o de dentro na cor do fundo.
 */
function rbm_anel( $im, $s, $cor_anel, $cor_fundo ) {
	$cx = RBM_CX * $s;
	$cy = RBM_CY * $s;
	$de = ( RBM_R + RBM_TRACO / 2 ) * 2 * $s; // diametro externo
	$di = ( RBM_R - RBM_TRACO / 2 ) * 2 * $s; // diametro interno

	// A GD mede angulo em graus, sentido horario, 0 = direita — mesma convencao
	// do SVG aqui, porque nos dois o y cresce para baixo.
	$inicio = RBM_CORTE;
	$fim    = 360 - RBM_CORTE;

	imagefilledarc( $im, (int) $cx, (int) $cy, (int) $de, (int) $de, (int) $inicio, (int) $fim, $cor_anel, IMG_ARC_PIE );
	imagefilledarc( $im, (int) $cx, (int) $cy, (int) $di, (int) $di, 0, 360, $cor_fundo, IMG_ARC_PIE );
}

function rbm_icone_png_base64( $lado = 180 ) {
	$s   = 24;            // 32 unidades x 24 = 768 px de tela de desenho
	$tam = 32 * $s;
	$im  = imagecreatetruecolor( $tam, $tam );
	imagealphablending( $im, true );

	$tinta     = rbm_cor( $im, RBM_TINTA );
	$varredura = rbm_cor( $im, RBM_VARREDURA );
	$piso      = rbm_cor( $im, RBM_PISO );

	// Fundo em sangria, SEM canto arredondado: a mascara e do iOS.
	imagefilledrectangle( $im, 0, 0, $tam - 1, $tam - 1, $tinta );

	rbm_anel( $im, $s, $piso, $tinta );

	// A peca: corpo + lingueta, nas mesmas coordenadas do SVG.
	rbm_retangulo( $im, 24 * $s, 10 * $s, 28.6 * $s, 22 * $s, $varredura );
	rbm_retangulo( $im, 21.6 * $s, 13 * $s, 24 * $s, 19 * $s, $varredura );

	$pequeno = imagescale( $im, $lado, $lado, IMG_BICUBIC );

	/* O desenho tem tres cores; a reducao bicubica inventa milhares delas nas
	   bordas e o PNG truecolor sai grande. Reduzir para 64 cores devolve o
	   arquivo ao tamanho de um icone e nao muda o que se ve. */
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

$svg_aba = rbm_icone_svg( true );
$png_ios = rbm_icone_png_base64( 180 );
$png_aba = rbm_icone_png_base64( 32 );
$arquivo = $raiz . '/snippets/robometria-casca.php';
$src     = file_get_contents( $arquivo );

$bloco  = "/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */\n";
$bloco .= "if ( ! defined( 'ROBOMETRIA_CASCA_ICONE_SVG' ) ) {\n";
$bloco .= "\tdefine( 'ROBOMETRIA_CASCA_ICONE_SVG', '" . str_replace( "'", "\\'", $svg_aba ) . "' );\n";
$bloco .= "\tdefine( 'ROBOMETRIA_CASCA_ICONE_PNG_180', '" . $png_ios . "' );\n";
$bloco .= "\tdefine( 'ROBOMETRIA_CASCA_ICONE_PNG_32', '" . $png_aba . "' );\n";
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

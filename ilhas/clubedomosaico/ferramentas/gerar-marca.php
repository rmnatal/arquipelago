<?php
/**
 * Embute a LOTUS do cabecalho dentro do snippet da casca, entre os marcadores.
 *
 *   php ferramentas/gerar-marca.php .
 *
 * POR QUE ELA EXISTE, e por que ela e diferente da gerar-favicon.php: o favicon
 * e um PNG de 32 px que ja veio pronto na pasta. A marca do cabecalho precisa
 * ser a lotus TRANSPARENTE em tamanho util (80 px, que e o dobro dos 40 px de
 * tela, para nao borrar em retina), e o unico arquivo grande que a ilha tem e
 * identidade/logo/lotus-512.png.
 *
 * O QUE ESTA FERRAMENTA RECUSA, e por que isso e a metade que importa: em
 * 11/09/2026 a Fundacao foi cumprir o despacho do Raphael — "usar o simbolo
 * transparente lotus-512.png no cabecalho claro" — e o arquivo NAO ABRE. O IDAT
 * dele declara 11.638 bytes num arquivo que tem 8.770, com um IEND colado no
 * fim; nao e imagem cortada pela metade, e fluxo corrompido desde o primeiro
 * bloco, e nem uma linha de pixel sai dele. Se esta ferramenta so lesse bytes e
 * gravasse base64, o site teria trocado o logo sumido por um icone de imagem
 * quebrada — que e pior, porque parece descuido em vez de obra em andamento.
 *
 * Entao ela DECODIFICA antes de gravar. Sai com codigo 1 e nao toca no snippet
 * quando o arquivo nao e um PNG que abre, quando ele nao tem canal alfa (lotus
 * sobre fundo solido vira um retangulo colorido no cabecalho branco) ou quando
 * as bordas nao sao transparentes. Enquanto ela recusar, a casca serve o
 * wordmark em texto, que e a outra metade do par que o despacho pediu.
 *
 * Regra herdada da gerar-favicon.php: o data URI nao se edita a mao. Quem
 * trocar o PNG da pasta roda isto e o snippet acompanha.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$origem  = $raiz . '/identidade/logo/lotus-512.png';
$saida   = $raiz . '/identidade/logo/lotus-80.png';
$destino = $raiz . '/snippets/clubedomosaico-casca.php';
$lado    = 80;

if ( ! is_readable( $origem ) ) {
	fwrite( STDERR, "nao achei $origem\n" );
	exit( 1 );
}
if ( ! is_readable( $destino ) ) {
	fwrite( STDERR, "nao achei $destino\n" );
	exit( 1 );
}

$bruto = file_get_contents( $origem );

/* Primeiro a conferencia estrutural, que e a que diz a VERDADE sobre o arquivo
   truncado: percorre os chunks e cobra que nenhum estoure o fim do arquivo.
   Fazer isso aqui, e nao so no imagecreatefrompng, e o que permite dizer no
   erro QUANTOS bytes faltam em vez de "arquivo invalido". */
$erro = cdm_marca_conferir_chunks( $bruto );
if ( '' !== $erro ) {
	fwrite( STDERR, "$origem: $erro\n" );
	fwrite( STDERR, "a casca segue com o wordmark em texto; peca o arquivo de novo ao Raphael\n" );
	exit( 1 );
}

$img = @imagecreatefrompng( $origem );
if ( false === $img ) {
	fwrite( STDERR, "$origem: o PNG nao abre\n" );
	exit( 1 );
}

$largura = imagesx( $img );
$altura  = imagesy( $img );
if ( $largura < $lado || $altura < $lado ) {
	fwrite( STDERR, "$origem: $largura x $altura e menor que $lado px; ampliar borraria a marca\n" );
	exit( 1 );
}

/* Fundo solido no cabecalho claro vira um retangulo. A lotus tem que ter alfa, e
   os quatro cantos tem que ser transparentes de verdade. */
imagealphablending( $img, false );
$cantos = array( array( 0, 0 ), array( $largura - 1, 0 ), array( 0, $altura - 1 ), array( $largura - 1, $altura - 1 ) );
foreach ( $cantos as $c ) {
	$cor   = imagecolorsforindex( $img, imagecolorat( $img, $c[0], $c[1] ) );
	$alfa  = isset( $cor['alpha'] ) ? (int) $cor['alpha'] : 0;
	if ( $alfa < 100 ) { // 127 e totalmente transparente
		fwrite( STDERR, "$origem: o canto ({$c[0]},{$c[1]}) nao e transparente (alfa $alfa)\n" );
		exit( 1 );
	}
}

$novo = imagecreatetruecolor( $lado, $lado );
imagealphablending( $novo, false );
imagesavealpha( $novo, true );
imagefill( $novo, 0, 0, imagecolorallocatealpha( $novo, 0, 0, 0, 127 ) );
/* A lotus entregue nao e quadrada: encaixar sem esticar e o que impede a marca
   de sair achatada num tamanho e nao no outro. */
$escala = min( $lado / $largura, $lado / $altura );
$dw     = (int) round( $largura * $escala );
$dh     = (int) round( $altura * $escala );
imagecopyresampled( $novo, $img, (int) ( ( $lado - $dw ) / 2 ), (int) ( ( $lado - $dh ) / 2 ), 0, 0, $dw, $dh, $largura, $altura );

ob_start();
imagepng( $novo, null, 9 );
$png = ob_get_clean();

if ( ! $png || "\x89PNG\r\n\x1a\n" !== substr( $png, 0, 8 ) ) {
	fwrite( STDERR, "nao consegui gerar o PNG de $lado px\n" );
	exit( 1 );
}

file_put_contents( $saida, $png );

$fonte = file_get_contents( $destino );
$novo_bloco = "/* MARCA-INICIO — gerado por ferramentas/gerar-marca.php, nao edite a mao */\n"
	. "if ( ! defined( 'CDM_CASCA_MARCA_LOTUS' ) ) {\n"
	. "\tdefine( 'CDM_CASCA_MARCA_LOTUS', '" . base64_encode( $png ) . "' );\n"
	. "}\n"
	. "/* MARCA-FIM */";

$trocado = preg_replace( '#/\* MARCA-INICIO.*?/\* MARCA-FIM \*/#s', $novo_bloco, $fonte, 1, $quantos );
if ( 1 !== $quantos ) {
	fwrite( STDERR, "nao achei os marcadores MARCA-INICIO/MARCA-FIM no snippet\n" );
	exit( 1 );
}

file_put_contents( $destino, $trocado );
printf( "lotus-%d.png gravada (%d bytes) e embutida no snippet (%d bytes em base64)\n", $lado, strlen( $png ), strlen( base64_encode( $png ) ) );

/**
 * Percorre os chunks do PNG e devolve '' quando o arquivo esta inteiro.
 *
 * E a leitura que o GD nao da: ele diz "nao e um PNG valido" para qualquer
 * defeito, e a diferenca entre "arquivo trocado" e "arquivo truncado em 2.868
 * bytes" e o que decide se o conserto e pedir de novo ou converter.
 */
function cdm_marca_conferir_chunks( $bruto ) {
	if ( "\x89PNG\r\n\x1a\n" !== substr( $bruto, 0, 8 ) ) {
		return 'nao comeca com a assinatura de PNG';
	}
	$i     = 8;
	$total = strlen( $bruto );
	while ( $i + 8 <= $total ) {
		$tamanho = unpack( 'N', substr( $bruto, $i, 4 ) )[1];
		$tipo    = substr( $bruto, $i + 4, 4 );
		$fim     = $i + 12 + $tamanho;
		if ( $fim > $total ) {
			return sprintf( 'chunk %s declara %d bytes e faltam %d no arquivo (PNG truncado)', $tipo, $tamanho, $fim - $total );
		}
		$crc = unpack( 'N', substr( $bruto, $i + 8 + $tamanho, 4 ) )[1];
		if ( crc32( $tipo . substr( $bruto, $i + 8, $tamanho ) ) !== $crc ) {
			return sprintf( 'chunk %s com CRC errado', $tipo );
		}
		if ( 'IEND' === $tipo ) {
			return '';
		}
		$i = $fim;
	}
	return 'acabou sem IEND';
}

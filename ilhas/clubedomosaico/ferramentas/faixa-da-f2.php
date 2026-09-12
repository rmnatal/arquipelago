<?php
/**
 * A FAIXA DE ENTRADA DA F2, MEDIDA NO PROPRIO SNIPPET — nunca digitada aqui.
 *
 *   php ferramentas/faixa-da-f2.php .            # JSON para a varredura
 *   php ferramentas/faixa-da-f2.php . --humano   # a mesma coisa, legivel
 *
 * POR QUE ESTE ARQUIVO EXISTE, e por que ele nao e uma constante num dos outros
 * dois: a secao 14.3 do ARQUIPELAGO.md manda varrer "a faixa de entrada de cada
 * ferramenta de ponta a ponta". Varredura que anda sobre uma faixa DIGITADA mede
 * a faixa que alguem lembrou, nao a que a ferramenta serve — e no dia em que o
 * campo da junta subir de 12 para 14 mm, a varredura continuaria verde cobrindo
 * 12, sem uma linha de defeito visivel. E a mesma familia do numero de tela
 * digitado (secao 8) e da bancada que le uma fonte enquanto o site le outra.
 *
 * ENTAO ELE NAO LE O CODIGO: ele PROVOCA a ferramenta. Para cada valor de um
 * superconjunto deliberadamente maior que a faixa esperada, ele poe o valor em
 * $_GET, chama `cdm_f2_entrada()` — que e a MESMA funcao que sanea a consulta de
 * quem visita — e pergunta se o valor sobreviveu. Sobreviveu, esta na faixa; caiu
 * no padrao, esta fora. O teto e o piso aparecem sozinhos.
 *
 * O superconjunto tem que passar dos dois lados, ou ele nao mede borda nenhuma:
 * a junta e provocada de 0 a 20 mm, e as dimensoes categoricas levam junto um
 * valor inventado que a ferramenta tem obrigacao de recusar. Se o inventado
 * passar, isto FALHA — saneamento que aceita qualquer coisa nao tem faixa.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$humano = in_array( '--humano', $argv, true );

cdm_teste_carregar( $raiz );
cdm_teste_carregar_options( $raiz );

if ( ! function_exists( 'cdm_f2_entrada' ) || ! function_exists( 'cdm_f2_rotulos' ) ) {
	fwrite( STDERR, "FALHA: a F2 nao carregou; sem ela nao ha faixa a medir.\n" );
	exit( 1 );
}

/* O valor inventado que toda dimensao categorica tem que recusar. */
$INVENTADO = 'valor_que_nao_existe_no_vocabulario';

/**
 * Poe uma consulta em $_GET, deixa a ferramenta sanear, e devolve o que sobrou.
 */
function cdm_faixa_sanear( $campo, $valor ) {
	$_GET = array( $campo => $valor );
	$e    = cdm_f2_entrada();
	$_GET = array();

	$de_para = array( 'base' => 'base', 'onde' => 'ambiente', 'caco' => 'tessela', 'junta' => 'junta' );

	return $e[ $de_para[ $campo ] ];
}

$rot     = cdm_f2_rotulos();
$erros   = array();
$faixa   = array();

/* ---- as tres dimensoes categoricas ------------------------------------- */

$categoricas = array(
	'base'     => array( 'campo' => 'base', 'candidatos' => array_keys( $rot['base'] ) ),
	'ambiente' => array( 'campo' => 'onde', 'candidatos' => array_keys( $rot['ambiente'] ) ),
	'tessela'  => array( 'campo' => 'caco', 'candidatos' => array_keys( $rot['tessela'] ) ),
);

foreach ( $categoricas as $nome => $d ) {
	$aceitos = array();
	foreach ( $d['candidatos'] as $valor ) {
		if ( cdm_faixa_sanear( $d['campo'], $valor ) === $valor ) {
			$aceitos[] = $valor;
		}
	}
	sort( $aceitos );
	$faixa[ $nome ] = $aceitos;

	/* a borda de fora: o inventado TEM que cair */
	if ( cdm_faixa_sanear( $d['campo'], $INVENTADO ) === $INVENTADO ) {
		$erros[] = sprintf(
			'%s: a ferramenta ACEITOU o valor inventado "%s". Saneamento que aceita qualquer coisa nao delimita faixa nenhuma.',
			$nome,
			$INVENTADO
		);
	}
	if ( ! $aceitos ) {
		$erros[] = sprintf( '%s: a ferramenta nao aceitou NENHUM dos proprios rotulos.', $nome );
	}
}

/* ---- a junta, que e numerica e por isso tem teto e piso ------------------ */

/* O superconjunto passa dos dois lados de proposito: 0 esta abaixo de qualquer
   piso plausivel e 20 esta acima de qualquer teto plausivel. Se a faixa medida
   encostar numa das pontas do superconjunto, o superconjunto e que e pequeno —
   e isto FALHA, em vez de devolver um teto que e so o fim da regua. */
$SUPER_MIN = 0;
$SUPER_MAX = 20;

$juntas = array();
for ( $j = $SUPER_MIN; $j <= $SUPER_MAX; $j++ ) {
	if ( (int) cdm_faixa_sanear( 'junta', (string) $j ) === $j ) {
		$juntas[] = $j;
	}
}
$faixa['junta_mm'] = $juntas;

if ( ! $juntas ) {
	$erros[] = 'junta: a ferramenta nao aceitou nenhum valor entre ' . $SUPER_MIN . ' e ' . $SUPER_MAX . '.';
} else {
	if ( min( $juntas ) === $SUPER_MIN ) {
		$erros[] = 'junta: o piso medido e o piso da propria regua (' . $SUPER_MIN . '). O superconjunto nao passa por baixo da faixa, entao ele nao mede o piso.';
	}
	if ( max( $juntas ) === $SUPER_MAX ) {
		$erros[] = 'junta: o teto medido e o teto da propria regua (' . $SUPER_MAX . '). O superconjunto nao passa por cima da faixa, entao ele nao mede o teto.';
	}
	/* faixa com buraco no meio nao e faixa, e a varredura contaria estados que a
	   ferramenta nunca serve */
	if ( count( $juntas ) !== ( max( $juntas ) - min( $juntas ) + 1 ) ) {
		$erros[] = 'junta: a faixa aceita tem buraco no meio (' . implode( ', ', $juntas ) . ').';
	}
}

/* ---- o que a varredura vai andar, contado e nunca digitado --------------- */

$faixa['estados_de_cola']   = count( $faixa['base'] ) * count( $faixa['ambiente'] );
$faixa['estados_de_rejunte'] = count( $faixa['junta_mm'] ) * count( $faixa['ambiente'] );

$saida = array(
	'medido_em'         => gmdate( 'Y-m-d\TH:i\Z' ),
	'medido_por'        => 'ferramentas/faixa-da-f2.php',
	'como'              => 'provocando cdm_f2_entrada() com um superconjunto maior que a faixa, nos dois sentidos; vale o que sobreviveu ao saneamento',
	'fonte_da_verdade'  => 'snippets/clubedomosaico-f2.php',
	'faixa'             => $faixa,
);

if ( $erros ) {
	fwrite( STDERR, "FALHA ao medir a faixa da F2:\n" );
	foreach ( $erros as $e ) {
		fwrite( STDERR, '  - ' . $e . "\n" );
	}
	exit( 1 );
}

if ( $humano ) {
	printf( "Faixa de entrada da F2, medida no snippet em %s\n", $saida['medido_em'] );
	printf( "  bases ............. %d  (%s)\n", count( $faixa['base'] ), implode( ', ', $faixa['base'] ) );
	printf( "  ambientes ......... %d  (%s)\n", count( $faixa['ambiente'] ), implode( ', ', $faixa['ambiente'] ) );
	printf( "  tesselas .......... %d  (%s)\n", count( $faixa['tessela'] ), implode( ', ', $faixa['tessela'] ) );
	printf( "  junta ............. %d a %d mm, de 1 em 1\n", min( $juntas ), max( $juntas ) );
	printf( "  estados de cola ... %d\n", $faixa['estados_de_cola'] );
	printf( "  estados de rejunte  %d\n", $faixa['estados_de_rejunte'] );
	exit( 0 );
}

echo json_encode( $saida, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ), "\n";

<?php
/**
 * O SITE SERVE O QUE O CENSO CONTA? — as duas metades da secao 14.3, cruzadas.
 *
 *   php ferramentas/conferir-cobertura.php .
 *   php ferramentas/conferir-cobertura.php . --celula cola:vidro:interno_seco
 *
 * `dados/cobertura.json` e escrito pela regua PYTHON de `validar-banco.py`, que
 * recompoe a elegibilidade das declaracoes dos fabricantes. Quem serve a pagina e
 * o snippet PHP. Sao duas implementacoes da mesma regra, e ate hoje elas so se
 * cruzavam nas 27 celulas escritas a mao do esquema — 18 de cola e 9 de rejunte,
 * de 45 e 60 que as ferramentas servem. Os outros 78 estados nunca tinham sido
 * comparados com nada: se as duas metades divergissem ali, o censo diria um
 * numero e o site serviria outro, e nenhum portao veria.
 *
 * E A MESMA CICATRIZ DA SECAO 8 DUAS VEZES: "grade tem que incluir a borda,
 * senao e amostra com nome de grade" e "varrer a entrada inteira, nao o
 * caso-ancora". Aqui as duas viram uma coisa so — a grade E a entrada inteira,
 * porque a faixa e medida no proprio snippet por `faixa-da-f2.php`.
 *
 * UM PROCESSO POR ESTADO, e nao e zelo: a casca tem `static` legitimos e as
 * funcoes de perfil da F2 guardam cache por material. Varrer 105 estados no mesmo
 * processo mediria o primeiro e herdaria o resto — foi assim que a Robometria
 * mediu 915 KB do que no ar tem 960 (secao 8). Aqui o cache e por material e nao
 * por estado, entao provavelmente nao mudaria o numero: "provavelmente" e
 * exatamente o que um processo por estado dispensa de ser discutido.
 *
 * O QUE ELE NAO FAZ: nao confere o TEXTO da pagina. Quem mede o que a tela diz
 * sobre cada produto e `teste-prestacao-rejunte.php`, e quem mede a pagina no ar
 * e `conferir-no-ar.py`. Este aqui mede so a contagem de elegiveis, que e a
 * unidade da secao 14.3.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

/* ------------------------------------------------------------------ modo celula
 * Um estado so, num processo so dele. E o que o modo principal chama 105 vezes.
 * Ele imprime JSON e nada mais, para o pai nao ter que adivinhar nada.
 */
$pos_celula = array_search( '--celula', $argv, true );
if ( false !== $pos_celula && isset( $argv[ $pos_celula + 1 ] ) ) {
	cdm_teste_carregar( $raiz );
	cdm_teste_carregar_options( $raiz );

	$partes = explode( ':', $argv[ $pos_celula + 1 ] );
	$tipo   = isset( $partes[0] ) ? $partes[0] : '';

	if ( 'cola' === $tipo && isset( $partes[2] ) ) {
		$c = cdm_f2_celula_cola( $partes[1], $partes[2] );
	} elseif ( 'rejunte' === $tipo && isset( $partes[2] ) ) {
		$c = cdm_f2_celula_rejunte( (int) $partes[1], $partes[2] );
	} else {
		fwrite( STDERR, "celula invalida\n" );
		exit( 2 );
	}

	$eleg = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
	sort( $eleg );
	echo json_encode( array( 'elegiveis' => $eleg ) ), "\n";
	exit( 0 );
}

/* ------------------------------------------------------------------ modo varredura */

$falhas = 0;
$feitos = 0;

function cob_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-72s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-72s %s\n", $rotulo, $medida );
	return false;
}

/** Um estado, servido por um processo so dele. */
function cob_celula_do_snippet( $raiz, $chave ) {
	$saida  = array();
	$codigo = 0;
	exec(
		escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __FILE__ )
		. ' ' . escapeshellarg( $raiz ) . ' --celula ' . escapeshellarg( $chave ) . ' 2>/dev/null',
		$saida,
		$codigo
	);
	if ( 0 !== $codigo ) {
		return null;
	}
	$j = json_decode( implode( "\n", $saida ), true );

	return is_array( $j ) && isset( $j['elegiveis'] ) ? $j['elegiveis'] : null;
}

$caminho = $raiz . '/dados/cobertura.json';
if ( ! file_exists( $caminho ) ) {
	fwrite( STDERR, "FALHA: dados/cobertura.json nao existe. Rode `python3 ferramentas/cobertura.py`.\n" );
	exit( 1 );
}
$censo = json_decode( file_get_contents( $caminho ), true );

printf( "Cobertura — o site contra o censo (%s)\n", $caminho );

/* 1. A FAIXA DO CENSO E A FAIXA DE HOJE. Censo escrito sobre uma faixa que o
      snippet nao serve mais e numero com cara de conferido. */
$saida_faixa = array();
$cod_faixa   = 0;
exec(
	escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/faixa-da-f2.php' )
	. ' ' . escapeshellarg( $raiz ) . ' 2>/dev/null',
	$saida_faixa,
	$cod_faixa
);
$faixa_hoje = ( 0 === $cod_faixa ) ? json_decode( implode( "\n", $saida_faixa ), true ) : null;
cob_ok( null !== $faixa_hoje, 'a faixa de entrada foi medida no snippet agora' );

if ( $faixa_hoje ) {
	$f = $faixa_hoje['faixa'];
	cob_ok(
		(int) $censo['faixa_varrida']['estados_de_cola'] === (int) $f['estados_de_cola'],
		'a faixa de cola do censo e a que o snippet serve hoje',
		$censo['faixa_varrida']['estados_de_cola'] . ' x ' . $f['estados_de_cola']
	);
	cob_ok(
		(int) $censo['faixa_varrida']['estados_de_rejunte'] === (int) $f['estados_de_rejunte'],
		'a faixa de rejunte do censo e a que o snippet serve hoje',
		$censo['faixa_varrida']['estados_de_rejunte'] . ' x ' . $f['estados_de_rejunte']
	);
}

/* 2. O CENSO COBRE A FAIXA INTEIRA. Contado dos dois lados: o numero de estados
      gravados tem que ser o produto das dimensoes medidas, e cada par tem que
      aparecer UMA vez. Censo com 44 dos 45 estados passaria calado sem isto. */
foreach ( array( 'cola', 'rejunte' ) as $tipo ) {
	$esperado = (int) $censo['faixa_varrida'][ 'estados_de_' . $tipo ];
	$gravados = count( $censo['estados'][ $tipo ] );
	cob_ok( $esperado === $gravados, 'o censo de ' . $tipo . ' tem um estado para cada par da faixa',
		$gravados . ' de ' . $esperado );

	$vistos = array();
	foreach ( $censo['estados'][ $tipo ] as $e ) {
		$chave = ( 'cola' === $tipo ? $e['base'] : $e['junta_mm'] ) . '|' . $e['ambiente'];
		$vistos[ $chave ] = isset( $vistos[ $chave ] ) ? $vistos[ $chave ] + 1 : 1;
	}
	$repetidos = array_keys( array_filter( $vistos, function ( $n ) { return $n > 1; } ) );
	cob_ok( ! $repetidos, 'nenhum estado de ' . $tipo . ' aparece duas vezes no censo',
		$repetidos ? implode( ', ', $repetidos ) : count( $vistos ) . ' pares distintos' );
}

/* 3. O CRUZAMENTO, estado a estado, um processo cada. */
$comparados = 0;
$divergentes = array();

foreach ( $censo['estados']['cola'] as $e ) {
	$chave = 'cola:' . $e['base'] . ':' . $e['ambiente'];
	$doSite = cob_celula_do_snippet( $raiz, $chave );
	$comparados++;
	if ( null === $doSite || $doSite !== $e['elegiveis'] ) {
		$divergentes[] = $chave . ' — censo: [' . implode( ', ', $e['elegiveis'] ) . '] / site: ['
			. ( null === $doSite ? 'sem resposta' : implode( ', ', $doSite ) ) . ']';
	}
}

foreach ( $censo['estados']['rejunte'] as $e ) {
	$chave = 'rejunte:' . $e['junta_mm'] . ':' . $e['ambiente'];
	$doSite = cob_celula_do_snippet( $raiz, $chave );
	$comparados++;
	if ( null === $doSite || $doSite !== $e['elegiveis'] ) {
		$divergentes[] = $chave . ' — censo: [' . implode( ', ', $e['elegiveis'] ) . '] / site: ['
			. ( null === $doSite ? 'sem resposta' : implode( ', ', $doSite ) ) . ']';
	}
}

cob_ok(
	$comparados === count( $censo['estados']['cola'] ) + count( $censo['estados']['rejunte'] ),
	'todo estado do censo foi comparado com o snippet, um processo cada',
	$comparados . ' estados'
);
cob_ok( ! $divergentes, 'a regua do censo e a do snippet dao o mesmo elegivel em todo estado',
	$divergentes ? count( $divergentes ) . ' divergencia(s)' : $comparados . ' estados iguais' );
foreach ( $divergentes as $d ) {
	printf( "         %s\n", $d );
}

/* 4. AS CONTAGENS DO RESUMO SAO CONTADAS, nunca digitadas. Este e o numero que
      vai para o REGISTRO.md e para o ESTADO.md, e a secao 8 do contrato cobra que
      ele nasca contado — foi o cartao "0 no banco" desta ilha que ensinou isso. */
foreach ( array( 'cola', 'rejunte' ) as $tipo ) {
	$minimo = (int) $censo['minimo_exigido'];
	$estados = $censo['estados'][ $tipo ];

	$com = 0;
	$sem = 0;
	$zero = 0;
	$teto = 0;
	foreach ( $estados as $e ) {
		$n = count( $e['elegiveis'] );
		cob_ok_silencioso( $n === (int) $e['quantos_elegiveis'] );
		if ( $n >= $minimo ) {
			$com++;
		} else {
			$sem++;
		}
		if ( 0 === $n ) {
			$zero++;
		}
		if ( $n > $teto ) {
			$teto = $n;
		}
	}

	$r = $censo['resumo'][ $tipo ];
	cob_ok( $com === (int) $r['estados_com_o_minimo'], $tipo . ': "com o minimo" bate com a contagem', $com );
	cob_ok( $sem === (int) $r['estados_descobertos'], $tipo . ': "descobertos" bate com a contagem', $sem );
	cob_ok( $zero === (int) $r['estados_sem_nenhum_elegivel'], $tipo . ': "sem nenhum elegivel" bate com a contagem', $zero );
	cob_ok( $teto === (int) $r['maior_numero_de_elegiveis_em_um_estado'], $tipo . ': o teto bate com a contagem', $teto );
	cob_ok( $com + $sem === count( $estados ), $tipo . ': com o minimo mais descobertos fecha a faixa', $com . ' + ' . $sem );
	cob_ok( count( $censo['faixas_descobertas'][ $tipo ] ) === $sem,
		$tipo . ': a lista de faixas descobertas tem uma linha por estado descoberto',
		count( $censo['faixas_descobertas'][ $tipo ] ) . ' de ' . $sem );
}

/* 5. TODA FAIXA DESCOBERTA NOMEIA A CAUSA QUE O CALCULO SEPAROU (secao 7). */
$sem_causa = 0;
foreach ( array( 'cola', 'rejunte' ) as $tipo ) {
	foreach ( $censo['faixas_descobertas'][ $tipo ] as $e ) {
		if ( empty( $e['por_que'] ) ) {
			$sem_causa++;
		}
	}
}
cob_ok( 0 === $sem_causa, 'toda faixa descoberta diz por que esta descoberta', $sem_causa . ' sem causa' );

/* 6. AS CATEGORIAS VAZIAS SAO CONTADAS DO BANCO, nos dois sentidos. */
$por_categoria = $censo['banco_hoje']['por_categoria'];
$vazias        = $censo['banco_hoje']['categorias_do_vocabulario_sem_nenhum_item'];
$intruso       = array_intersect( $vazias, array_keys( $por_categoria ) );
cob_ok( ! $intruso, 'nenhuma categoria declarada vazia tem item no banco',
	$intruso ? implode( ', ', $intruso ) : count( $vazias ) . ' vazias' );

printf( "\n%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas ? 1 : 0 );

function cob_ok_silencioso( $condicao ) {
	global $falhas, $feitos;
	$feitos++;
	if ( ! $condicao ) {
		$falhas++;
		printf( "  FALHA %s\n", 'quantos_elegiveis nao bate com o tamanho da lista de elegiveis' );
	}
}

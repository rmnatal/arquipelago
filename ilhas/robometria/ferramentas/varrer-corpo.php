<?php
/**
 * Varre o CORPO VISIVEL de TODO estado de pagina que esta ilha consegue servir,
 * e escreve cada um na saida padrao precedido de uma linha "=== <estado> ===".
 *
 *   php ferramentas/varrer-corpo.php .            # tudo
 *   php ferramentas/varrer-corpo.php . --estados  # so a lista de estados
 *
 * POR QUE ELE EXISTE, e por que nao bastava o render de bancada:
 *
 * A secao 8 do ARQUIPELAGO.md diz que afirmacao sobre o que a pagina DIZ se mede
 * no CORPO, nunca no HTML completo — e a Robometria ja pagou o preco de medir no
 * lugar errado duas vezes (o `&#038;` contado na pagina inteira, a resposta do
 * FAQPage achada dentro do proprio JSON-LD). Mas ha um segundo jeito de medir a
 * metade errada, e este arquivo existe por causa dele: **render de uma pagina so
 * nao e a pagina toda**. A R1 serve uma resposta por modelo e a R2 uma por
 * situacao; montar a pagina sem consulta mede o caso-ancora e mais nada. Foi
 * exatamente assim que "Aspirador Robo" e "Versao A" ficaram invisiveis para uma
 * medicao que renderizava as nove paginas e se dava por satisfeita: os dois so
 * aparecem quando alguem escolhe um modelo da Multi.
 *
 * Entao a varredura aqui e da ENTRADA INTEIRA, nao de uma amostra:
 *   - as 9 paginas fixas da ilha;
 *   - a R1 em CADA modelo publicavel do banco, mais cada tipo de peca no
 *     modelo-ancora, mais os estados de recusa (entrada vazia, modelo que nao
 *     existe);
 *   - a R2 nas 9 situacoes, em cada modelo de referencia e nas bordas da faixa
 *     de metragem.
 *
 * O que ele devolve e TEXTO, nao HTML: <script> e <style> saem inteiros (com o
 * conteudo), as marcacoes saem, e as entidades voltam a ser caractere. Quem
 * afirma sobre a tela le daqui.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$so_estados = in_array( '--estados', $argv, true );

require __DIR__ . '/render-para-teste.php';

$r1       = json_decode( file_get_contents( $raiz . '/dados/r1-respostas.json' ), true );
$r2       = json_decode( file_get_contents( $raiz . '/dados/r2-respostas.json' ), true );
$cob_r2   = json_decode( file_get_contents( $raiz . '/dados/cobertura-r2.json' ), true );

$GLOBALS['__paginas'] = array(
	'ferramentas'                            => true,
	'metodologia'                            => true,
	'sobre'                                  => true,
	'divulgacao-de-afiliados'                => true,
	'qual-peca-serve-no-meu-robo-aspirador'  => true,
	'filtro-universal-de-robo-aspirador'     => true,
	'quantos-pa-o-robo-aspirador-precisa'    => true,
	'quantos-m2-o-robo-aspirador-limpa-por-carga' => true,
);
$GLOBALS['__entrada_r1'] = array( 'modelo' => null, 'peca' => null );
$GLOBALS['__entrada_r2'] = array( 'area' => null, 'piso' => null, 'pelo' => null, 'referencia' => null );

robometria_teste_carregar( $raiz );

add_filter( 'robometria_r1_dados',     function ( $d ) use ( $r1 ) { return $r1; } );
add_filter( 'robometria_r1_na_pagina', function () { return true; } );
add_filter( 'robometria_r1_entrada',   function ( $e ) { return $GLOBALS['__entrada_r1']; } );
add_filter( 'robometria_r2_dados',     function ( $d ) use ( $r2 ) { return $r2; } );
add_filter( 'robometria_r2_na_pagina', function () { return true; } );
add_filter( 'robometria_r2_entrada',   function ( $e ) { return $GLOBALS['__entrada_r2']; } );

/**
 * Corpo visivel: sem <script>, sem <style>, sem marcacao, com as entidades
 * desfeitas. E o que um leitor le e o que um modelo de linguagem cita.
 */
if ( ! function_exists( 'robometria_corpo_visivel' ) ) {
function robometria_corpo_visivel( $html, $classes_excecao = array(), &$removidos = null ) {
	$removidos = array();
	$t = preg_replace( '#<script\b[^>]*>.*?</script>#is', ' ', $html );
	$t = preg_replace( '#<style\b[^>]*>.*?</style>#is',   ' ', $t );

	/* Bloco que a PÁGINA declara como exceção, por classe no markup.
	   Quem afirma sobre texto não adivinha pela vizinhança: declara. A regra é
	   a da seção 8 do ARQUIPELAGO.md, aprendida no Clube do Mosaico — e vem com
	   a mesma contrapartida, que é o que a impede de virar porta dos fundos: o
	   bloco removido volta para quem chamou, contado, para ser conferido um a
	   um. Exceção que ninguém confere é exceção que aceita qualquer coisa. */
	foreach ( $classes_excecao as $classe ) {
		$padrao = '#<(\w+)[^>]*class="[^"]*\b' . preg_quote( $classe, '#' ) . '\b[^"]*"[^>]*>(.*?)</\1>#s';
		$t = preg_replace_callback( $padrao, function ( $m ) use ( &$removidos, $classe ) {
			$texto = html_entity_decode( preg_replace( '#<[^>]+>#s', '', $m[2] ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
			$removidos[] = array( 'classe' => $classe, 'texto' => trim( $texto ) );
			return ' ';
		}, $t );
	}

	$t = preg_replace( '#<[^>]+>#s', ' ', $t );
	$t = html_entity_decode( $t, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	return trim( preg_replace( '/\s+/u', ' ', $t ) );
}
}

/** Todo estado de pagina que a ilha consegue servir, como (rotulo => fechamento). */
if ( ! function_exists( 'robometria_estados_de_pagina' ) ) {
function robometria_estados_de_pagina( $r1, $r2, $cob_r2 ) {
	$estados = array();

	foreach ( array( 'home', 'ferramentas', 'metodologia', 'sobre', 'afiliados', 'a1', 'a2' ) as $tag ) {
		$estados[ 'pagina:' . $tag ] = function () use ( $tag ) {
			robometria_teste_rebobinar();
			return robometria_teste_pagina( 'robometria_' . $tag, 'Robometria — teste', robometria_teste_slug_do_alvo( 'robometria_' . $tag ) );
		};
	}

	$r1_pagina = function ( $modelo, $peca ) {
		$GLOBALS['__entrada_r1'] = array( 'modelo' => $modelo, 'peca' => $peca );
		robometria_teste_rebobinar();
		return robometria_teste_pagina( 'robometria_r1', 'Robometria — teste', robometria_teste_slug_do_alvo( 'robometria_r1' ) );
	};
	$estados['r1:sem consulta'] = function () use ( $r1_pagina ) { return $r1_pagina( null, null ); };
	foreach ( $r1['modelos'] as $m ) {
		$estados[ 'r1:' . $m['id'] ] = function () use ( $r1_pagina, $m ) { return $r1_pagina( $m['id'], null ); };
	}
	foreach ( $r1['tipos'] as $t ) {
		$estados[ 'r1:ancora+' . $t ] = function () use ( $r1_pagina, $r1, $t ) { return $r1_pagina( $r1['ancora'], $t ); };
	}
	$estados['r1:modelo inexistente'] = function () use ( $r1_pagina ) {
		return $r1_pagina( 'nao-existe-no-banco', 'tipo-que-nao-existe' );
	};

	$r2_pagina = function ( $area, $piso, $pelo, $ref ) {
		$GLOBALS['__entrada_r2'] = array( 'area' => $area, 'piso' => $piso, 'pelo' => $pelo, 'referencia' => $ref );
		robometria_teste_rebobinar();
		return robometria_teste_pagina( 'robometria_r2', 'Robometria — teste', robometria_teste_slug_do_alvo( 'robometria_r2' ) );
	};
	$estados['r2:sem consulta'] = function () use ( $r2_pagina ) { return $r2_pagina( null, null, null, null ); };

	$situacoes = array_keys( $r2['classificacao'] );
	$refs      = array();
	foreach ( $cob_r2['referencias'] as $r ) { $refs[] = $r['modelo']; }
	$areas = array( $r2['entrada']['area_minima'], 60, 200, $r2['entrada']['area_maxima'] );

	foreach ( $situacoes as $s ) {
		list( $piso, $pelo ) = explode( '|', $s );
		$estados[ 'r2:' . $s ] = function () use ( $r2_pagina, $piso, $pelo ) {
			return $r2_pagina( 200, $piso, $pelo, null );
		};
	}
	foreach ( $refs as $ref ) {
		foreach ( $areas as $a ) {
			$estados[ "r2:$ref@$a" ] = function () use ( $r2_pagina, $a, $ref ) {
				return $r2_pagina( $a, 'liso', 'curto', $ref );
			};
		}
	}

	return $estados;
}
}

$estados = robometria_estados_de_pagina( $r1, $r2, $cob_r2 );

if ( $so_estados ) {
	foreach ( array_keys( $estados ) as $rotulo ) { echo $rotulo . "\n"; }
	echo count( $estados ) . " estados\n";
	exit( 0 );
}

/* --com-excecao=classe[,classe] retira do corpo os blocos que a PAGINA declara
   como excecao — e imprime cada um deles, numa linha "--- excecao <classe>: ",
   para quem afirma poder conferi-los um a um. Excecao que some sem ser contada
   e porta dos fundos. */
$classes = array();
foreach ( $argv as $arg ) {
	if ( 0 === strpos( $arg, '--com-excecao=' ) ) {
		$classes = array_filter( explode( ',', substr( $arg, strlen( '--com-excecao=' ) ) ) );
	}
}

/* UM PROCESSO POR ESTADO, e isto nao e zelo: e a unica forma de o estado 2 ser
 * uma pagina inteira.
 *
 * Medido em 11/09/2026, montando os 72 estados no mesmo processo: o cabecalho
 * apareceu no PRIMEIRO e sumiu nos 71 seguintes. A causa e legitima e esta no
 * lugar certo — `robometria_casca_marca_html()` guarda um `static $ja_impressa`
 * para a marca nao sair duas vezes na MESMA pagina, e no site um processo e uma
 * requisicao. Num varredor que monta 72 paginas seguidas, esse static vira
 * contaminacao entre estados, e a varredura passa a medir meia pagina com cara
 * de pagina inteira — exatamente o defeito que a R2 ja pagou quando o render
 * saia sem is_page() e sem as options.
 *
 * Reabrir o processo devolve a fidelidade de graca, e nao so para este static:
 * qualquer estado acumulado (filtro registrado duas vezes, cache de funcao)
 * morre junto. Custa alguns segundos; medir a metade errada custa um bloco.
 */
$um_so = null;
foreach ( $argv as $arg ) {
	if ( 0 === strpos( $arg, '--estado=' ) ) {
		$um_so = substr( $arg, strlen( '--estado=' ) );
	}
}

if ( null !== $um_so ) {
	if ( ! isset( $estados[ $um_so ] ) ) {
		fwrite( STDERR, "estado desconhecido: $um_so\n" );
		exit( 2 );
	}
	$removidos = array();
	$corpo = robometria_corpo_visivel( call_user_func( $estados[ $um_so ] ), $classes, $removidos );
	foreach ( $removidos as $bloco ) {
		echo '--- excecao ' . $bloco['classe'] . ': ' . $bloco['texto'] . "\n";
	}
	echo $corpo . "\n";
	exit( 0 );
}

$argumento_classes = $classes ? ' --com-excecao=' . escapeshellarg( implode( ',', $classes ) ) : '';
foreach ( array_keys( $estados ) as $rotulo ) {
	echo "=== $rotulo ===\n";
	$linhas = array();
	$codigo = 0;
	exec( PHP_BINARY . ' ' . escapeshellarg( __FILE__ ) . ' ' . escapeshellarg( $raiz )
		. ' --estado=' . escapeshellarg( $rotulo ) . $argumento_classes . ' 2>&1', $linhas, $codigo );
	if ( 0 !== $codigo ) {
		fwrite( STDERR, "estado $rotulo falhou (codigo $codigo)\n" );
		exit( $codigo );
	}
	echo implode( "\n", $linhas ) . "\n";
}

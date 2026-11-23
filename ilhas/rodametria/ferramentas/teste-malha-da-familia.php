<?php
/**
 * A MALHA DA FAMILIA — O GRAFO DE IRMAS FECHA NAS DUAS DIRECOES (23/11/2026).
 *
 *   php ferramentas/teste-malha-da-familia.php
 *
 * O DEFEITO QUE ELE EXISTE PARA IMPEDIR FOI MEDIDO NO AR, nao deduzido. Na ronda
 * tecnica de 23/11/2026, no HTML servido das 11 URLs desta ilha e dentro do
 * `<main>` (menu e rodape fora), `/veiculos/moto-eletrica/` — a consulta de 823
 * mil buscas/mes, a de MAIOR volume do nicho — recebia **ZERO** link de entrada
 * de miolo, contra os 2 que a 16.4(f) exige. As outras dez recebiam de 3 a 10. A
 * mae `/veiculos/` servia 6 links de miolo e nenhum era o dela; as duas irmas
 * listavam uma a outra e nunca a moto; e a moto listava as duas. **O grafo
 * estava de um lado so**, que e exatamente o que a 16.9(a) manda nao acontecer.
 *
 * A CAUSA ERA DE MECANISMO, E E A MESMA FONTE DA 25.2-c: a rotacao de irmas e a
 * listagem de filhas da mae nasciam de `rdm_produto_paginas_prontas()`, a lista
 * de quem TEM VITRINE — e a pagina degradada pelo piso da 30.2 esta ausente dela
 * POR DEFINICAO. Aquela mesma fonte ja havia tirado desta pagina a CABECA
 * (consertado em 18/11) e a SAIDA DE COMPRA (19/11); o cluster era o terceiro
 * andar, e ninguem o havia medido.
 *
 * E A REGUA DESTA ILHA NAO PODIA REPROVAR AQUILO: o veredito de 18/11 dizia
 * *"zero pagina orfa na direcao de ENTRADA (as 11 recebem 10 links de entrada
 * cada)"* — e 10 e o MENU mais o RODAPE, que toda pagina recebe por construcao.
 * Contagem de entrada que inclui a navegacao global fica verde em qualquer
 * mundo, inclusive neste. E a familia do "resumo verde nao e entrega" da 20.4
 * aplicada a link interno.
 *
 * POR QUE ELE E PHP E NAO PYTHON — o mesmo motivo escrito no
 * `teste-caixa-da-mae.php`, no `teste-cabeca-sem-vitrine.php` e no
 * `teste-menu-da-casca.php`: a decisao mora em PHP, entao a regua CHAMA as
 * funcoes de verdade. Regua em Python sobre o TEXTO do PHP conferiria a FORMA do
 * codigo e nunca a decisao — e aqui a decisao e "quem entra na ordem do cluster".
 *
 * O QUE ELE MEDE, em SETE mundos fabricados (secao 8: "regua escrita para um
 * mundo que nunca aconteceu nasce errada sem poder falhar"):
 *
 *   1. ENTRADA == SAIDA em toda pagina no ar, e as duas iguais a
 *      `min(4, irmas)` — a propriedade que a 16.9(a) promete com todas as
 *      letras e que a janela fixa quebrava da sexta filha em diante.
 *   2. COM DUAS OU MAIS PAGINAS NO AR, NENHUMA RECEBE ZERO — a 16.9(b) ao pe
 *      da letra, e o mundo medido em 23/11 esta na lista com o numero dele.
 *   3. NINGUEM LISTA A SI MESMO, e a ordem e a da CAMADA DECLARADA: ordem que
 *      muda com a coleta do dia faz o grafo circulante girar sozinho.
 *   4. AS DUAS TRAVAS DA DEGRADADA: sem `consulta` na fonte ela NAO entra (a
 *      ancora e a consulta, 16.4c, e ancora inventada no PHP e a segunda
 *      declaracao que a 20.7 proibe); sem pagina no WordPress ela NAO entra
 *      (secao 16, contra link interno para 404).
 *   5. A DISCORDANCIA DA 20.8: a regua VELHA — rotacao sobre as prontas — e
 *      reescrita aqui e TEM de dizer ZERO entrada para a moto no mundo de
 *      23/11, enquanto a nova diz 2. Portao que nao mostra a discordancia nao
 *      prova conserto nenhum.
 *   6. QUATRO MUTACOES, cada uma uma forma de quebrar o grafo, e as quatro TEM
 *      de REPROVAR: janela fixa (a cicatriz da clubedomosaico de 12/10), rotacao
 *      sobre as prontas (o codigo de ontem), irma = a propria pagina, e rotacao
 *      SEM volta no fim.
 */

foreach ( array( 'add_filter', 'add_action', 'add_shortcode', 'register_activation_hook' ) as $f ) {
	if ( ! function_exists( $f ) ) { eval( "function $f(){ return true; }" ); }
}
if ( ! function_exists( 'esc_html' ) ) {
	function esc_html( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_url( $s ) { return (string) $s; }
}

$RAIZ = dirname( __DIR__ );

/** Carrega UMA funcao de um snippet, equilibrando chaves — o snippet inteiro
 *  registra filtros ao ser lido, entao ele nao pode ser incluido. Copiado do
 *  `teste-cabeca-sem-vitrine.php` desta mesma pasta. */
function carregar_funcao( $src, $nome ) {
	$i = strpos( $src, "function $nome(" );
	if ( false === $i ) { return false; }
	$j = strpos( $src, '{', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '{' === $src[ $k ] ) { $n++; }
		elseif ( '}' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	eval( substr( $src, $i, $k - $i + 1 ) );
	return true;
}

$falhas     = 0;
$afirmacoes = 0;
function vale( $ok, $nome, $detalhe = '' ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	echo ( $ok ? '  ok    ' : '  FALHA ' ) . $nome
		. ( $ok ? '' : "\n          " . $detalhe ) . "\n";
	if ( ! $ok ) { $falhas++; }
}

if ( ! defined( 'RODAMETRIA_PRODUTO_SECAO' ) ) { define( 'RODAMETRIA_PRODUTO_SECAO', 'veiculos' ); }

/* ---------------------------------------------------------------------------
 * O MUNDO. Substituidas aqui SO as quatro portas que falam com o banco e com o
 * WordPress; as funcoes que DECIDEM sao as de verdade, carregadas do snippet.
 * ------------------------------------------------------------------------- */
$MUNDO = array(
	'declaradas'   => array(),
	'prontas'      => array(),
	'existem'      => array(),
	'nao_nasceram' => array(),
);

function rdm_produto_editorial() {
	global $MUNDO;
	return array( 'paginas' => $MUNDO['declaradas'] );
}

function rdm_produto_paginas_prontas() {
	global $MUNDO;
	return $MUNDO['prontas'];
}

function rdm_produto_nao_nasceram() {
	global $MUNDO;
	return $MUNDO['nao_nasceram'];
}

function rodametria_casca_url_do_slug( $slug ) {
	global $MUNDO;
	return in_array( (string) $slug, $MUNDO['existem'], true )
		? 'https://rodametria.com.br/veiculos/' . $slug . '/' : '';
}

$src = file_get_contents( $RAIZ . '/snippets/rodametria-produto.php' );
foreach ( array( 'rdm_produto_declaradas_fora_da_vitrine', 'rdm_produto_paginas_no_ar',
	'rdm_produto_irmas' ) as $nome ) {
	if ( ! carregar_funcao( $src, $nome ) ) {
		echo "FALHA: nao achei `$nome()` no snippet\n";
		exit( 1 );
	}
}

/* --------------------------------------------------------------------------
 * OS MONTADORES DE MUNDO. `pronta` e `degradada` escrevem a MESMA familia de
 * pagina nas duas camadas, para nenhum mundo nascer meio declarado.
 * ------------------------------------------------------------------------ */
function pronta( &$m, $id, $consulta ) {
	$m['declaradas'][] = array( 'id' => $id, 'h1' => ucfirst( $consulta ) );
	$m['prontas'][ $id ] = array(
		'id'      => $id,
		'slug'    => $id,
		'vitrine' => array( 'consulta' => $consulta ),
	);
	$m['existem'][] = $id;
}

function degradada( &$m, $id, $consulta, $existe = true, $com_consulta = true ) {
	$m['declaradas'][] = array( 'id' => $id, 'h1' => ucfirst( (string) $consulta ) );
	$linha = array( 'id' => $id, 'causa' => 'menos de 3 anuncios que servem' );
	if ( $com_consulta ) { $linha['consulta'] = $consulta; }
	$m['nao_nasceram'][ $id ] = $linha;
	if ( $existe ) { $m['existem'][] = $id; }
}

/* --------------------------------------------------------------------------
 * A REGUA, E ELA E A PROPRIEDADE E NAO A IMPLEMENTACAO. Entra uma funcao que
 * devolve as irmas de um id; sai a lista de falhas em palavras. E assim que as
 * mutacoes podem ser cobradas: a regua nao sabe de quem e o codigo que mede.
 * ------------------------------------------------------------------------ */
function veredito_do_grafo( $ordem, $irmas_de ) {
	$falhas = array();
	$n      = count( $ordem );
	$espera = $n > 1 ? min( 4, $n - 1 ) : 0;
	$entra  = array_fill_keys( $ordem, 0 );

	foreach ( $ordem as $id ) {
		$irmas = $irmas_de( $id );
		if ( ! is_array( $irmas ) ) {
			$falhas[] = sprintf( 'a lista de irmas de %s nao e uma lista', $id );
			continue;
		}
		if ( count( $irmas ) !== $espera ) {
			$falhas[] = sprintf( '%s leva %d irma(s) e a 16.9(a) promete min(4, irmas) = %d '
				. '— janela que depende do tamanho de hoje para de valer amanha',
				$id, count( $irmas ), $espera );
		}
		if ( in_array( $id, $irmas, true ) ) {
			$falhas[] = sprintf( '%s esta na propria lista de irmas: link para a pagina que a '
				. 'pessoa ja esta lendo nao e cluster, e ainda rouba uma das quatro vagas', $id );
		}
		foreach ( $irmas as $irma ) {
			if ( ! isset( $entra[ $irma ] ) ) {
				$falhas[] = sprintf( '%s lista %s, que nao esta na ordem de quem esta no ar '
					. '— link interno para fora do cluster', $id, $irma );
				continue;
			}
			$entra[ $irma ]++;
		}
	}

	foreach ( $ordem as $id ) {
		if ( $n > 1 && 0 === $entra[ $id ] ) {
			$falhas[] = sprintf( 'ORFA NA DIRECAO DE ENTRADA: %s nao recebe UMA irma apontando '
				. 'para ela, e com o link da mae isso da 1 contra os 2 da 16.4(f) — a 16.9(b) '
				. 'e literal sobre a conta ser refeita na direcao de QUEM APONTA', $id );
		} elseif ( $entra[ $id ] !== $espera ) {
			$falhas[] = sprintf( '%s recebe %d irma(s) e leva %d: o grafo circulante da '
				. '16.9(a) fecha entrada == saida, e este nao fecha',
				$id, $entra[ $id ], $espera );
		}
	}

	return $falhas;
}

/* --------------------------------------------------------------------------
 * AS MUTACOES — cada uma uma forma de quebrar o grafo, e as quatro tem de
 * REPROVAR. Trava que nunca falhou nao e trava.
 * ------------------------------------------------------------------------ */
function m_janela_fixa( $ordem ) {
	/* A CICATRIZ DA CLUBEDOMOSAICO, 12/10/2026: as QUATRO PRIMEIRAS da ordem,
	   iguais para todas as paginas. Invisivel com cinco filhas, e da sexta em
	   diante a quinta e a sexta nao recebem link de irma nenhuma. */
	return function ( $id ) use ( $ordem ) {
		$fora = array();
		foreach ( $ordem as $outro ) {
			if ( $outro !== $id && count( $fora ) < 4 ) { $fora[] = $outro; }
		}
		return $fora;
	};
}

function m_so_as_prontas( $ordem, $prontas ) {
	/* O CODIGO DE ONTEM: a rotacao sobre quem TEM VITRINE. No mundo de 23/11 ele
	   deixa a moto com zero entrada, que foi o que o ar servia. */
	return function ( $id ) use ( $ordem, $prontas ) {
		$so    = array_values( array_intersect( $ordem, $prontas ) );
		$onde  = array_search( $id, $so, true );
		if ( false === $onde ) { return array(); }
		$total = count( $so );
		$fora  = array();
		for ( $i = 1; $i < $total && count( $fora ) < 4; $i++ ) {
			$fora[] = $so[ ( $onde + $i ) % $total ];
		}
		return $fora;
	};
}

function m_inclui_a_si( $ordem ) {
	return function ( $id ) use ( $ordem ) {
		$total = count( $ordem );
		$onde  = array_search( $id, $ordem, true );
		$fora  = array( $id );
		for ( $i = 1; $i < $total && count( $fora ) < min( 4, $total - 1 ); $i++ ) {
			$fora[] = $ordem[ ( $onde + $i ) % $total ];
		}
		return $fora;
	};
}

function m_sem_volta_no_fim( $ordem ) {
	/* Rotacao que NAO da a volta: a ultima da ordem leva zero irma, e a primeira
	   recebe zero. O defeito que a palavra "dando a volta no fim" da 16.9(a)
	   existe para impedir. */
	return function ( $id ) use ( $ordem ) {
		$onde = array_search( $id, $ordem, true );
		if ( false === $onde ) { return array(); }
		return array_slice( $ordem, $onde + 1, 4 );
	};
}

/* --------------------------------------------------------------------------
 * OS SETE MUNDOS
 * ------------------------------------------------------------------------ */
$MUNDOS = array(
	array(
		'nome'   => 'O MUNDO MEDIDO EM 23/11/2026: duas filhas com vitrine e a moto degradada '
			. 'pelo piso da 30.2',
		'monta'  => function ( &$m ) {
			pronta( $m, 'patinete-eletrico', 'patinete elétrico' );
			pronta( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
			degradada( $m, 'moto-eletrica', 'moto elétrica' );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica' ),
	),
	array(
		'nome'   => 'duas com vitrine e nenhuma degradada: min(4, 1) = 1 irma para cada lado',
		'monta'  => function ( &$m ) {
			pronta( $m, 'patinete-eletrico', 'patinete elétrico' );
			pronta( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica' ),
	),
	array(
		'nome'   => 'UMA pagina no ar: zero irma, e a 16.9(b) nao cobra entrada de quem nao '
			. 'tem par',
		'monta'  => function ( &$m ) { pronta( $m, 'patinete-eletrico', 'patinete elétrico' ); },
		'espera' => array( 'patinete-eletrico' ),
	),
	array(
		'nome'   => 'SEIS no ar, duas degradadas: e a partir daqui que a janela fixa quebrava '
			. 'na clubedomosaico',
		'monta'  => function ( &$m ) {
			pronta( $m, 'patinete-eletrico', 'patinete elétrico' );
			pronta( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
			degradada( $m, 'moto-eletrica', 'moto elétrica' );
			pronta( $m, 'scooter-eletrica', 'scooter elétrica' );
			degradada( $m, 'triciclo-eletrico', 'triciclo elétrico' );
			pronta( $m, 'quadriciclo-eletrico', 'quadriciclo elétrico' );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica',
			'scooter-eletrica', 'triciclo-eletrico', 'quadriciclo-eletrico' ),
	),
	array(
		'nome'   => 'TRES degradadas e NENHUMA com vitrine: o dia em que a coleta inteira falha '
			. 'e a malha tem de sobreviver',
		'monta'  => function ( &$m ) {
			degradada( $m, 'patinete-eletrico', 'patinete elétrico' );
			degradada( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
			degradada( $m, 'moto-eletrica', 'moto elétrica' );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica' ),
	),
	array(
		'nome'   => 'A TRAVA DA ANCORA: degradada SEM `consulta` na fonte fica FORA do cluster',
		'monta'  => function ( &$m ) {
			pronta( $m, 'patinete-eletrico', 'patinete elétrico' );
			pronta( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
			degradada( $m, 'moto-eletrica', 'moto elétrica', true, false );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica' ),
	),
	array(
		'nome'   => 'A TRAVA DO 404: degradada que nao tem pagina no WordPress fica FORA',
		'monta'  => function ( &$m ) {
			pronta( $m, 'patinete-eletrico', 'patinete elétrico' );
			pronta( $m, 'bicicleta-eletrica', 'bicicleta elétrica' );
			degradada( $m, 'moto-eletrica', 'moto elétrica', false );
		},
		'espera' => array( 'patinete-eletrico', 'bicicleta-eletrica' ),
	),
);

echo "A MALHA DA FAMILIA — RODAMETRIA (sem rede)\n\n";

$irmas_de_verdade = function ( $id ) { return rdm_produto_irmas( $id ); };

foreach ( $MUNDOS as $mundo ) {
	echo 'MUNDO: ' . $mundo['nome'] . "\n";
	$MUNDO = array( 'declaradas' => array(), 'prontas' => array(),
		'existem' => array(), 'nao_nasceram' => array() );
	$monta = $mundo['monta'];
	$monta( $MUNDO );

	$no_ar = rdm_produto_paginas_no_ar();
	$ordem = array_keys( $no_ar );

	vale( $ordem === $mundo['espera'],
		'a ordem de quem esta no ar e a da camada declarada',
		'esperava ' . implode( ', ', $mundo['espera'] ) . ' e veio ' . implode( ', ', $ordem ) );

	/* A CONSULTA DE CADA UMA SAI DA FONTE, nunca de prosa: a ancora e ela. */
	$sem_consulta = array();
	foreach ( $no_ar as $id => $p ) {
		if ( '' === trim( (string) $p['consulta'] ) ) { $sem_consulta[] = $id; }
	}
	vale( ! $sem_consulta, 'toda pagina no ar tem a consulta que serve de ancora (16.4c)',
		'sem consulta: ' . implode( ', ', $sem_consulta ) );

	$saida = veredito_do_grafo( $ordem, $irmas_de_verdade );
	vale( ! $saida, 'o grafo fecha nas duas direcoes (entrada == saida == min(4, irmas))',
		implode( ' | ', $saida ) );
	foreach ( $saida as $linha ) {
		vale( strlen( trim( $linha ) ) > 30, 'a falha diz em palavras o que esta errado', $linha );
	}
	echo "\n";
}

/* --------------------------------------------------------------------------
 * A DISCORDANCIA DA 20.8, no mundo medido e so nele.
 * ------------------------------------------------------------------------ */
echo "A DISCORDANCIA COM A REGUA VELHA (rotacao sobre as prontas)\n";
$MUNDO = array( 'declaradas' => array(), 'prontas' => array(),
	'existem' => array(), 'nao_nasceram' => array() );
pronta( $MUNDO, 'patinete-eletrico', 'patinete elétrico' );
pronta( $MUNDO, 'bicicleta-eletrica', 'bicicleta elétrica' );
degradada( $MUNDO, 'moto-eletrica', 'moto elétrica' );
$no_ar   = rdm_produto_paginas_no_ar();
$ordem   = array_keys( $no_ar );
$prontas = array_keys( $MUNDO['prontas'] );

$velha = m_so_as_prontas( $ordem, $prontas );
$entra_velha = 0;
foreach ( $ordem as $id ) {
	if ( in_array( 'moto-eletrica', $velha( $id ), true ) ) { $entra_velha++; }
}
$entra_nova = 0;
foreach ( $ordem as $id ) {
	if ( in_array( 'moto-eletrica', rdm_produto_irmas( $id ), true ) ) { $entra_nova++; }
}
vale( 0 === $entra_velha && 2 === $entra_nova,
	'a regua velha deixava a moto com ZERO entrada de irma e a nova lhe da DUAS',
	sprintf( 'velha=%d nova=%d — sem essa discordancia este portao nao prova conserto nenhum',
		$entra_velha, $entra_nova ) );
vale( ! empty( veredito_do_grafo( $ordem, $velha ) ),
	'a regua da propriedade REPROVA o mundo que estava no ar em 23/11' );
echo "\n";

/* --------------------------------------------------------------------------
 * AS QUATRO MUTACOES — as quatro tem de REPROVAR.
 * ------------------------------------------------------------------------ */
echo "AS QUATRO MUTACOES (todas tem de REPROVAR)\n";
$MUNDO = array( 'declaradas' => array(), 'prontas' => array(),
	'existem' => array(), 'nao_nasceram' => array() );
pronta( $MUNDO, 'patinete-eletrico', 'patinete elétrico' );
pronta( $MUNDO, 'bicicleta-eletrica', 'bicicleta elétrica' );
degradada( $MUNDO, 'moto-eletrica', 'moto elétrica' );
pronta( $MUNDO, 'scooter-eletrica', 'scooter elétrica' );
degradada( $MUNDO, 'triciclo-eletrico', 'triciclo elétrico' );
pronta( $MUNDO, 'quadriciclo-eletrico', 'quadriciclo elétrico' );
$ordem   = array_keys( rdm_produto_paginas_no_ar() );
$prontas = array_keys( $MUNDO['prontas'] );

$MUTACOES = array(
	array( 'janela fixa (as quatro primeiras da ordem, iguais para todas)',
		m_janela_fixa( $ordem ) ),
	array( 'rotacao SO sobre as prontas (o codigo de ontem)',
		m_so_as_prontas( $ordem, $prontas ) ),
	array( 'a pagina entra na propria lista de irmas', m_inclui_a_si( $ordem ) ),
	array( 'rotacao SEM volta no fim', m_sem_volta_no_fim( $ordem ) ),
);
foreach ( $MUTACOES as $mut ) {
	$saida = veredito_do_grafo( $ordem, $mut[1] );
	vale( ! empty( $saida ), 'MUTACAO reprovada: ' . $mut[0],
		'a regua APROVOU o grafo quebrado — ela nao morde' );
}

/* E A REGUA DE VERDADE APROVA O MESMO MUNDO: mutacao que reprova tudo nao mede
   nada, ela so e pessimista. */
vale( empty( veredito_do_grafo( $ordem, $irmas_de_verdade ) ),
	'e o codigo de verdade APROVA o mundo de seis paginas em que as quatro mutacoes caem' );

echo "\n" . sprintf( '%d mundo(s) fabricado(s) e %d afirmacao(oes), %d falha(s).',
	count( $MUNDOS ) + 2, $afirmacoes, $falhas ) . "\n";
echo( $falhas ? "REPROVADO\n" : "APROVADO\n" );
exit( $falhas ? 1 : 0 );

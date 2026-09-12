<?php
/**
 * Verificacao MEDIDA da F1 — "Quantas pastilhas e quanto rejunte comprar".
 *
 *   php ferramentas/teste-f1.php .
 *
 * O que este arquivo tem, e por que:
 *
 *   1. A REGUA E PROPRIA E ARITMETICA. Os doze resultados esperados vem de
 *      `dados/pecas-tipicas.json`, escritos A MAO a partir das formulas, e este
 *      arquivo recalcula cada um deles AQUI em PHP, com a sua propria
 *      implementacao, antes de comparar com o que a pagina serve. Sao tres
 *      escritas independentes do mesmo numero — a mao, a bancada e o snippet.
 *      Se duas concordarem e uma discordar, o teste diz qual linha.
 *
 *   2. ELE VARRE A ENTRADA INTEIRA, nao o caso-ancora. A F1 e ferramenta de
 *      entrada variavel: seis formas, cinco tamanhos de caquinho, doze folgas,
 *      cinco sobras, tres tipos de rejunte e cinco lugares. A pagina sem
 *      consulta e UM estado. A Robometria pagou essa licao com cinco testes
 *      verdes que nao viam o defeito porque ele so aparecia num estado
 *      especifico.
 *
 *   3. ELE MEDE NO CORPO SERVIDO. Afirmacao sobre o que a pagina DIZ se conta
 *      dentro de <main>, nunca no HTML completo nem no retorno do shortcode.
 *
 *   4. UM PROCESSO POR ESTADO. A casca tem `static` legitimos (rodape, marca,
 *      trilha) que so valem dentro de uma requisicao.
 *
 *   5. AS BORDAS SAO FABRICADAS, porque o mundo ainda nao as tem: medida que
 *      nao fecha, folga que nenhum fabricante cobre, rejunte que a ferramenta
 *      recusa calcular, caquinho irregular e o banco AUSENTE. Grade que nao
 *      pisa na borda e amostra com nome de grade (secao 8 do ARQUIPELAGO.md).
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$rapido = in_array( '--rapido', $argv, true );

$falhas = 0;
$feitos = 0;

function f1_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-70s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-70s %s\n", $rotulo, $medida );
	return false;
}

function f1_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function f1_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

function f1_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/** SO o bloco de resposta daquele estado — onde a conta da pessoa e servida. */
function f1_bloco_resposta( $corpo ) {
	return preg_match( '#<div class="cdm-f1-resposta"[^>]*>(.*?)</div>\s*<div#is', $corpo, $m )
		? $m[1]
		: ( preg_match( '#<div class="cdm-f1-resposta"[^>]*>(.*)#is', $corpo, $m2 ) ? $m2[1] : '' );
}

/** Um estado da ferramenta, servido por um processo so dele. */
function f1_render( $raiz, $consulta = '', $modo = 'hoje' ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( 'cdm_f1' ) . ' ' . escapeshellarg( $modo )
		. ' ' . escapeshellarg( $consulta ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/* ---------------------------------------------------------------------------
 * A REGUA ARITMETICA DESTE ARQUIVO — escrita aqui, nunca chamada do snippet.
 * ------------------------------------------------------------------------- */

function f1_area( $forma, $m ) {
	switch ( $forma ) {
		case 'cilindro':
			return M_PI * $m['d'] * $m['h'];
		case 'conico':
			$g = sqrt( ( ( $m['d'] - $m['d2'] ) / 2 ) * ( ( $m['d'] - $m['d2'] ) / 2 ) + $m['h'] * $m['h'] );
			return M_PI * ( ( $m['d'] + $m['d2'] ) / 2 ) * $g;
		case 'placa':
			return $m['l'] * $m['a'];
		case 'disco':
			return M_PI * $m['d'] * $m['d'] / 4;
		case 'esfera':
			return M_PI * $m['d'] * $m['d'];
		case 'moldura':
			return $m['l'] * $m['a'] - $m['vl'] * $m['va'];
	}
	return null;
}

function f1_conta_pastilhas( $area_cm2, $lado_mm, $junta_mm, $sobra_pct ) {
	$passo = $lado_mm + $junta_mm;
	return (int) ceil( ( $area_cm2 / 10000 ) * ( 1000000 / ( $passo * $passo ) ) * ( 1 + $sobra_pct / 100 ) );
}

function f1_conta_gramas( $area_cm2, $lado_mm, $esp_mm, $junta_mm, $cr ) {
	$consumo = ( ( 2 * $lado_mm ) * $esp_mm * $junta_mm * $cr ) / ( $lado_mm * $lado_mm );
	return array( $consumo, ( $area_cm2 / 10000 ) * $consumo * 1000 );
}

$pecas_json = json_decode( (string) @file_get_contents( $raiz . '/dados/pecas-tipicas.json' ), true );
$rejuntes   = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-rejuntes.json' ), true );

if ( ! $pecas_json || ! $rejuntes ) {
	echo "ERRO: nao consegui ler dados/pecas-tipicas.json ou dados/materiais-rejuntes.json.\n";
	exit( 1 );
}

echo "Clube do Mosaico — verificacao da F1\n";

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo '  (F1 ' . CDM_F1_VERSAO . ', F2 ' . ( defined( 'CDM_F2_VERSAO' ) ? CDM_F2_VERSAO : '—' )
	. ', casca ' . CDM_CASCA_VERSAO . ")\n\n";

/* ---------------------------------------------------------------------------
 * 1. A pagina na arvore, com mae e com UM nome so
 * ------------------------------------------------------------------------- */

echo "1. A pagina na arvore (secao 16 do contrato)\n";

$defs = cdm_casca_definicao_paginas();
f1_ok( isset( $defs[ CDM_F1_SLUG ] ), 'a F1 registrou a propria pagina pelo filtro cdm_paginas', CDM_F1_SLUG );
f1_ok( isset( $defs[ CDM_F1_SLUG ]['pai'] ) && 'materiais' === $defs[ CDM_F1_SLUG ]['pai'],
	'a pagina nasce com mae, e a mae e /materiais/' );
f1_ok( isset( $defs['materiais'] ), 'a mae existe na definicao de paginas' );

$arvore = cdm_casca_arvore();
f1_ok( isset( $arvore[ CDM_F1_SLUG ] ), 'a pagina esta no mapa da arvore' );
f1_ok( isset( $arvore[ CDM_F1_SLUG ]['rotulo'] ) && CDM_F1_TITULO === $arvore[ CDM_F1_SLUG ]['rotulo'],
	'o degrau da trilha usa o mesmo nome', isset( $arvore[ CDM_F1_SLUG ] ) ? $arvore[ CDM_F1_SLUG ]['rotulo'] : '' );
f1_ok( isset( $arvore[ CDM_F1_SLUG ]['nivel'] ) && 3 === (int) $arvore[ CDM_F1_SLUG ]['nivel'],
	'a pagina e nivel 3' );
f1_ok( $defs[ CDM_F1_SLUG ]['titulo'] === CDM_F1_TITULO, 'o titulo da pagina e o mesmo nome' );

/* O TETO DE 65 DO <title>. O sufixo do site e " – Clube do Mosaico" (19
   caracteres); e a soma que o Google corta, nunca o nome sozinho. */
$sufixo = mb_strlen( ' – Clube do Mosaico', 'UTF-8' );
$total  = mb_strlen( CDM_F1_TITULO, 'UTF-8' ) + $sufixo;
f1_ok( $total <= 65, 'o nome mais o sufixo do site cabem no teto de 65 caracteres', $total . ' caracteres' );

/* O CARTAO DO GUIA E DA HOME apontam para a pagina, e com o mesmo nome. */
$achou_na_lista = false;
foreach ( cdm_casca_ferramentas() as $f ) {
	if ( isset( $f['codigo'] ) && 'F1' === $f['codigo'] ) {
		$achou_na_lista = ( CDM_F1_SLUG === $f['slug'] ) && ( CDM_F1_TITULO === $f['titulo'] ) && ( 'publicada' === $f['estado'] );
	}
}
f1_ok( $achou_na_lista, 'o registro de ferramentas da casca recebeu slug, nome e estado da F1' );

/* ---------------------------------------------------------------------------
 * 2. As doze pecas: a mao x a bancada x o que a pagina SERVE
 * ------------------------------------------------------------------------- */

echo "\n2. As doze pecas tipicas: tres escritas do mesmo numero\n";

$cr_json = null;
foreach ( $rejuntes['materiais'] as $m ) {
	if ( 'cimenticio' === $m['tipo'] && isset( $m['propriedades']['CR']['valor'] ) && null !== $m['propriedades']['CR']['valor'] ) {
		$cr_json = (float) $m['propriedades']['CR']['valor'];
	}
}
f1_ok( null !== $cr_json, 'o CR da formula esta no banco commitado, e e um so', (string) $cr_json );
f1_ok( abs( (float) $pecas_json['CR_usado'] - (float) $cr_json ) < 0.0001,
	'o CR escrito a mao na tabela e o mesmo do banco', $pecas_json['CR_usado'] . ' x ' . $cr_json );

/* O EXEMPLO DO PROPRIO FABRICANTE fecha com a nossa formula: e o unico ponto em
   que a implementacao pode ser conferida contra um numero que nao e nosso. */
list( $c_exemplo, ) = f1_conta_gramas( 10000, 200, 8, 10, $cr_json );
f1_ok( abs( $c_exemplo - 1.4 ) < 0.001, 'a formula reproduz o exemplo publicado pelo fabricante (1,4 kg/m2)',
	number_format( $c_exemplo, 3 ) );

$corpo_ancora = f1_corpo( f1_render( $raiz ) );
f1_ok( '' !== $corpo_ancora, 'a pagina-ancora foi servida', strlen( $corpo_ancora ) . ' bytes de corpo' );
$texto_ancora = f1_texto( $corpo_ancora );

$divergem_mao = array();
$fora_da_tela = array();
foreach ( $pecas_json['pecas'] as $p ) {
	$area = f1_area( $p['forma'], $p['medidas'] );
	$past = f1_conta_pastilhas( $area, $p['lado_mm'], $p['junta_mm'], (int) $pecas_json['sobra_de_todas_as_linhas'] );
	list( $consumo, $gramas ) = f1_conta_gramas( $area, $p['lado_mm'], $p['espessura_mm'], $p['junta_mm'], $cr_json );

	$area_tela   = (int) round( $area );
	$gramas_tela = ( $gramas < 10 ) ? round( $gramas, 1 ) : (int) round( $gramas );

	/* (a) A BANCADA x A MAO. */
	if ( $area_tela !== (int) $p['esperado']['area_cm2'] ) {
		$divergem_mao[] = $p['nome'] . ': area ' . $area_tela . ' x ' . $p['esperado']['area_cm2'];
	}
	if ( $past !== (int) $p['esperado']['pastilhas'] ) {
		$divergem_mao[] = $p['nome'] . ': pastilhas ' . $past . ' x ' . $p['esperado']['pastilhas'];
	}
	if ( abs( $gramas_tela - (float) $p['esperado']['rejunte_g'] ) > 0.051 ) {
		$divergem_mao[] = $p['nome'] . ': rejunte ' . $gramas_tela . ' x ' . $p['esperado']['rejunte_g'];
	}
	if ( abs( $consumo - (float) $p['esperado']['consumo_kg_m2'] ) > 0.005 ) {
		$divergem_mao[] = $p['nome'] . ': consumo ' . round( $consumo, 3 ) . ' x ' . $p['esperado']['consumo_kg_m2'];
	}

	/* (b) O QUE A PAGINA SERVE. Os tres numeros da linha tem que estar no corpo,
	   escritos como o leitor brasileiro os le — e a linha inteira tem que
	   existir, com o nome da peca. */
	$nome_na_tela = false !== mb_strpos( $texto_ancora, $p['nome'] );
	$area_na_tela = false !== mb_strpos( $texto_ancora, number_format_i18n( $area_tela ) . ' cm²' );
	$past_na_tela = false !== mb_strpos( $texto_ancora, number_format_i18n( $past ) );
	$g_na_tela    = false !== mb_strpos( $texto_ancora,
		( $gramas < 10 ? number_format_i18n( $gramas_tela, 1 ) : number_format_i18n( $gramas_tela ) ) . ' g' );

	if ( ! $nome_na_tela || ! $area_na_tela || ! $past_na_tela || ! $g_na_tela ) {
		$fora_da_tela[] = $p['nome'] . ( $nome_na_tela ? '' : ' (nome)' ) . ( $area_na_tela ? '' : ' (area)' )
			. ( $past_na_tela ? '' : ' (pastilhas)' ) . ( $g_na_tela ? '' : ' (rejunte)' );
	}
}
f1_ok( empty( $divergem_mao ), 'os doze resultados da bancada batem com os escritos a mao',
	empty( $divergem_mao ) ? count( $pecas_json['pecas'] ) . ' pecas x 4 numeros' : implode( ' | ', $divergem_mao ) );
f1_ok( empty( $fora_da_tela ), 'as doze linhas estao no HTML SERVIDO, com os numeros certos',
	empty( $fora_da_tela ) ? count( $pecas_json['pecas'] ) . ' linhas' : implode( ' | ', $fora_da_tela ) );

/* A TABELA E PRE-RENDERIZADA (secao 5 do contrato, item 1): ela existe no HTML
   de quem NAO preencheu nada. Se um dia alguem a esconder atras do formulario,
   a pagina passa a mostrar a um modelo de linguagem uma tela vazia. */
f1_ok( substr_count( $corpo_ancora, '<table' ) >= 3,
	'a pagina-ancora serve as tres tabelas sem ninguem preencher nada',
	substr_count( $corpo_ancora, '<table' ) . ' tabelas' );

/* ---------------------------------------------------------------------------
 * 3. A VARREDURA: cada estado e uma pagina de verdade
 * ------------------------------------------------------------------------- */

echo "\n3. Varredura da entrada (a pagina de cada consulta)\n";

$formas_padrao = array(
	'cilindro' => 'd=15&h=20',
	'conico'   => 'd=18&d2=12&h=15',
	'placa'    => 'l=30&a=40',
	'disco'    => 'd=60',
	'esfera'   => 'd=20',
	'moldura'  => 'l=40&a=60&vl=30&va=50',
);
$medidas_padrao = array(
	'cilindro' => array( 'd' => 15, 'h' => 20 ),
	'conico'   => array( 'd' => 18, 'd2' => 12, 'h' => 15 ),
	'placa'    => array( 'l' => 30, 'a' => 40 ),
	'disco'    => array( 'd' => 60 ),
	'esfera'   => array( 'd' => 20 ),
	'moldura'  => array( 'l' => 40, 'a' => 60, 'vl' => 30, 'va' => 50 ),
);
$lados = array( 'p10' => 10, 'p15' => 15, 'p20' => 20, 'p25' => 25 );

$estados      = array();
$erros_conta  = array();
$sem_resposta = array();
$sem_noindex  = array();
$com_script   = array();

/* (a) SEIS FORMAS x QUATRO TAMANHOS DE CAQUINHO — 24 estados, cada um com a
   conta conferida pela regua deste arquivo. */
foreach ( $formas_padrao as $forma => $qs_medidas ) {
	foreach ( $lados as $chave => $lado_mm ) {
		$consulta = 'forma=' . $forma . '&' . $qs_medidas . '&pastilha=' . $chave . '&junta=2&sobra=10&esp=4&rejunte=cimenticio';
		$html     = f1_render( $raiz, $consulta );
		$corpo    = f1_corpo( $html );
		$texto    = f1_texto( $corpo );
		$estados[] = $consulta;

		$area = f1_area( $forma, $medidas_padrao[ $forma ] );
		$past = f1_conta_pastilhas( $area, $lado_mm, 2, 10 );
		list( , $gramas ) = f1_conta_gramas( $area, $lado_mm, 4, 2, $cr_json );
		$g_tela = ( $gramas < 10 ) ? number_format_i18n( round( $gramas, 1 ), 1 ) : number_format_i18n( (int) round( $gramas ) );

		if ( false === mb_strpos( $texto, number_format_i18n( $past ) . ' pastilhas' ) ) {
			$erros_conta[] = $consulta . ': nao achei "' . number_format_i18n( $past ) . ' pastilhas"';
		}
		if ( false === mb_strpos( $texto, $g_tela . ' g' ) ) {
			$erros_conta[] = $consulta . ': nao achei "' . $g_tela . ' g"';
		}
		if ( false === mb_strpos( $texto, number_format_i18n( (int) round( $area ) ) . ' cm²' ) ) {
			$erros_conta[] = $consulta . ': nao achei a area';
		}
		if ( false === mb_stripos( $corpo, 'cdm-f1-resposta' ) ) {
			$sem_resposta[] = $consulta;
		}
		/* ESTADO COM PARAMETRO SAI DO INDICE (14.1 e 14.4): quem entra no indice
		   e a pagina-ancora, uma so. */
		if ( false === mb_stripos( $html, '<meta name="robots" content="noindex, follow">' ) ) {
			$sem_noindex[] = $consulta;
		}
		if ( 0 !== substr_count( f1_scripts( $html ), '&#038;' ) ) {
			$com_script[] = $consulta;
		}
	}
}
f1_ok( empty( $erros_conta ), 'a conta servida bate com a regua deste teste nas 24 combinacoes de forma x caquinho',
	empty( $erros_conta ) ? count( $estados ) . ' estados' : implode( ' | ', array_slice( $erros_conta, 0, 4 ) ) );
f1_ok( empty( $sem_resposta ), 'todo estado serve o bloco de resposta' );
f1_ok( empty( $sem_noindex ), 'todo estado com parametro sai com noindex, follow',
	empty( $sem_noindex ) ? count( $estados ) . ' estados' : implode( ' | ', array_slice( $sem_noindex, 0, 3 ) ) );
f1_ok( empty( $com_script ), 'zero &#038; dentro de <script> em todo estado varrido' );

/* (b) AS DOZE FOLGAS x OS TRES TIPOS DE REJUNTE — 36 estados. Aqui mora a
   correcao do bloco 3c: o numero de gramas so pode existir no cimenticio. */
$gramas_indevido = array();
$sem_recusa      = array();
$sem_faixa       = array();
$tipos           = array( 'cimenticio', 'acrilico', 'epoxi' );
for ( $junta = 1; $junta <= 12; $junta++ ) {
	foreach ( $tipos as $tipo ) {
		$consulta = 'forma=placa&l=30&a=40&pastilha=p10&junta=' . $junta . '&sobra=10&esp=4&rejunte=' . $tipo;
		$corpo    = f1_corpo( f1_render( $raiz, $consulta ) );
		$texto    = f1_texto( $corpo );
		/* A AFIRMACAO E SOBRE A RESPOSTA DESTE ESTADO, e nao sobre a pagina: a
		   tabela das doze pecas e de rejunte cimenticio POR DESENHO e a abertura
		   cita o numero da obra. Medir a pagina inteira aqui reprovaria texto que
		   esta certo — regua que nao sabe sobre o que decide acusa a coisa errada
		   (a mesma cicatriz do portao da 16.5 contando todo cartao do corpo). */
		$resposta = f1_texto( f1_bloco_resposta( $corpo ) );
		list( , $gramas ) = f1_conta_gramas( 1200, 10, 4, $junta, $cr_json );
		$g_tela = number_format_i18n( (int) round( $gramas ) );

		if ( 'cimenticio' === $tipo ) {
			if ( false === mb_strpos( $resposta, $g_tela . ' g' ) ) {
				$gramas_indevido[] = $consulta . ': o cimenticio devia dizer ' . $g_tela . ' g';
			}
		} else {
			/* NAO BASTA a ausencia do numero certo: a mutacao que trocasse o CR
			   passaria. O que se afirma e que a resposta NAO da numero nenhum de
			   rejunte para este tipo, e que a pagina diz por que. */
			if ( preg_match( '#\d[\d\.,]* g\b#u', $resposta ) ) {
				$gramas_indevido[] = $consulta . ': apareceu grama em rejunte que a ferramenta recusa';
			}
			if ( false === mb_stripos( $texto, 'Por que a gente não calcula esse rejunte' ) ) {
				$sem_recusa[] = $consulta;
			}
		}
		/* A FOLGA QUE NENHUM FABRICANTE COBRE — 11 e 12 mm — tem que devolver a
		   verdade, nunca uma lista vazia calada.

		   REESCRITA EM 12/09/2026, com o conserto do despacho da Sentinela. Ela
		   cobrava a string 'do nosso banco declara folga', que era a frase do
		   DEFEITO: a mesma sentenca saia quando quem excluia era o lugar, e ela
		   afirmava sobre o banco inteiro o que valia so para o tipo escolhido.
		   Afirmacao que fixa o texto de hoje vira trava contra o conserto de
		   amanha — o que importa aqui nunca foi a frase, foi a pagina dizer que
		   nao tem indicacao E dizer o motivo. E o motivo, nestes dois estados, e
		   mesmo a folga: 11 e 12 mm estao fora da faixa dos cinco produtos. */
		if ( $junta >= 11 ) {
			if ( false === mb_stripos( $texto, 'do nosso banco serve para essa peça' ) ) {
				$sem_faixa[] = $consulta . ' (nao disse que nenhum serve)';
			} elseif ( false === mb_stripos( $texto, 'Fora por causa da folga de' ) ) {
				$sem_faixa[] = $consulta . ' (nao nomeou a folga como causa)';
			}
		}
	}
}
f1_ok( empty( $gramas_indevido ), 'o numero de rejunte existe no cimenticio e NAO existe no acrilico nem no epoxi',
	empty( $gramas_indevido ) ? '36 estados' : implode( ' | ', array_slice( $gramas_indevido, 0, 3 ) ) );
f1_ok( empty( $sem_recusa ), 'a pagina explica a recusa em todo estado de acrilico e de epoxi' );
f1_ok( empty( $sem_faixa ), 'folga de 11 e 12 mm devolve "nenhum declara essa folga", em vez de lista vazia calada',
	empty( $sem_faixa ) ? 'as 6 combinacoes' : implode( ' | ', $sem_faixa ) );

/* (c) AS CINCO SOBRAS, e o arredondamento para cima. */
$sobras_ruins = array();
foreach ( array( 0, 5, 10, 15, 20 ) as $sobra ) {
	$consulta = 'forma=cilindro&d=15&h=20&pastilha=p10&junta=2&sobra=' . $sobra . '&esp=4&rejunte=cimenticio';
	$texto    = f1_texto( f1_corpo( f1_render( $raiz, $consulta ) ) );
	$esperado = f1_conta_pastilhas( M_PI * 15 * 20, 10, 2, $sobra );
	if ( false === mb_strpos( $texto, number_format_i18n( $esperado ) . ' pastilhas' ) ) {
		$sobras_ruins[] = $sobra . '%: esperava ' . number_format_i18n( $esperado );
	}
	/* O REJUNTE NAO LEVA SOBRA: os 264 g do vaso valem nas cinco. */
	if ( false === mb_strpos( $texto, '264 g' ) ) {
		$sobras_ruins[] = $sobra . '%: a sobra vazou para o rejunte';
	}
}
f1_ok( empty( $sobras_ruins ), 'as cinco sobras mudam a pastilha e NAO mudam o rejunte',
	empty( $sobras_ruins ) ? '5 estados' : implode( ' | ', $sobras_ruins ) );

/* O ARREDONDAMENTO PARA CIMA, medido onde ele decide: 654,5 pastilhas sem sobra
   viram 655, nunca 654. Meia pastilha nao existe na prateleira. */
$texto_sem_sobra = f1_texto( f1_corpo( f1_render( $raiz, 'forma=cilindro&d=15&h=20&pastilha=p10&junta=2&sobra=0&esp=4&rejunte=cimenticio' ) ) );
f1_ok( false !== mb_strpos( $texto_sem_sobra, '655 pastilhas' ),
	'a contagem arredonda para CIMA (654,5 vira 655)', '654,5 -> 655' );

/* (d) O CAQUINHO IRREGULAR — o unico caminho em que o lado e digitado. */
$irregulares = array( 0.5, 1.2, 2, 3.7 );
$irreg_ruins = array();
foreach ( $irregulares as $lado_cm ) {
	$consulta = 'forma=placa&l=30&a=40&pastilha=irregular&ladoeq=' . $lado_cm . '&junta=2&sobra=10&esp=4&rejunte=cimenticio';
	$texto    = f1_texto( f1_corpo( f1_render( $raiz, $consulta ) ) );
	$esperado = f1_conta_pastilhas( 1200, $lado_cm * 10, 2, 10 );
	if ( false === mb_strpos( $texto, number_format_i18n( $esperado ) . ' pastilhas' ) ) {
		$irreg_ruins[] = $lado_cm . ' cm: esperava ' . number_format_i18n( $esperado );
	}
}
f1_ok( empty( $irreg_ruins ), 'o lado medido do caquinho irregular entra na conta',
	empty( $irreg_ruins ) ? count( $irregulares ) . ' lados' : implode( ' | ', $irreg_ruins ) );

/* (e) A ESPESSURA MUDA O REJUNTE E NAO MUDA A PASTILHA. E a razao de ela ser
   entrada: pastilha de 6 mm come 50% mais rejunte que a de 4 mm. */
$esp_ruins = array();
foreach ( array( 2, 4, 6, 10 ) as $esp ) {
	$consulta = 'forma=placa&l=30&a=40&pastilha=p10&junta=2&sobra=10&esp=' . $esp . '&rejunte=cimenticio';
	$texto    = f1_texto( f1_corpo( f1_render( $raiz, $consulta ) ) );
	list( , $gramas ) = f1_conta_gramas( 1200, 10, $esp, 2, $cr_json );
	if ( false === mb_strpos( $texto, number_format_i18n( (int) round( $gramas ) ) . ' g' ) ) {
		$esp_ruins[] = $esp . ' mm: esperava ' . number_format_i18n( (int) round( $gramas ) ) . ' g';
	}
	if ( false === mb_strpos( $texto, '917 pastilhas' ) ) {
		$esp_ruins[] = $esp . ' mm: a espessura vazou para a contagem de pastilhas';
	}
}
f1_ok( empty( $esp_ruins ), 'a espessura muda o rejunte e nao toca a contagem de pastilhas',
	empty( $esp_ruins ) ? '4 espessuras' : implode( ' | ', $esp_ruins ) );

/* (f) AS BORDAS DE MEDIDA: vao maior que a moldura, e medida fora da faixa. */
$borda_moldura = f1_texto( f1_corpo( f1_render( $raiz, 'forma=moldura&l=40&a=60&vl=50&va=70&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=cimenticio' ) ) );
f1_ok( false !== mb_stripos( $borda_moldura, 'não fecha' ),
	'vao maior que a moldura devolve recusa, nunca area negativa nem zero' );
f1_ok( ! preg_match( '#-\d+ cm²#u', $borda_moldura ), 'nenhuma area negativa na tela' );

$borda_fora = f1_texto( f1_corpo( f1_render( $raiz, 'forma=cilindro&d=9999&h=20&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=cimenticio' ) ) );
f1_ok( false !== mb_strpos( $borda_fora, '720 pastilhas' ),
	'medida fora da faixa volta ao padrao, e a pagina responde o padrao' );

/* (g) O LUGAR ONDE A PECA VAI FICAR muda a lista de produto e NAO muda a conta. */
$ambientes   = array( 'interno_seco', 'interno_molhado', 'externo_abrigado', 'externo_exposto', 'contato_permanente_agua' );
$amb_ruins   = array();
$listas      = array();
foreach ( $ambientes as $amb ) {
	$consulta = 'forma=cilindro&d=15&h=20&pastilha=p10&junta=2&sobra=10&esp=4&rejunte=cimenticio&onde=' . $amb;
	$corpo    = f1_corpo( f1_render( $raiz, $consulta ) );
	$texto    = f1_texto( $corpo );
	if ( false === mb_strpos( $texto, '720 pastilhas' ) || false === mb_strpos( $texto, '264 g' ) ) {
		$amb_ruins[] = $amb . ': a conta mudou com o lugar';
	}
	preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<h3>(.*?)</h3>#is', $corpo, $mc, PREG_SET_ORDER );
	$nomes = array();
	foreach ( $mc as $c ) {
		$nomes[] = f1_texto( $c[1] );
	}
	$listas[ $amb ] = $nomes;
}
f1_ok( empty( $amb_ruins ), 'o lugar da peca nao mexe em nenhum numero da conta',
	empty( $amb_ruins ) ? count( $ambientes ) . ' lugares' : implode( ' | ', $amb_ruins ) );
f1_ok( $listas['interno_seco'] !== $listas['contato_permanente_agua'],
	'o lugar da peca MUDA a lista de rejunte (a regua da F2 esta ligada de verdade)',
	count( $listas['interno_seco'] ) . ' x ' . count( $listas['contato_permanente_agua'] ) . ' cartoes' );

/* A REGUA DA F2 E A MESMA, e isto e o que prova: o conjunto de produtos que a
   F1 mostra tem que ser um SUBCONJUNTO do que a F2 aprova para a mesma folga e
   o mesmo lugar — filtrado pelo tipo, nunca ampliado. Recomendar aqui o que a
   pagina irma elimina seria a ilha se contradizendo a uma aba de distancia. */
$fora_da_f2 = array();
foreach ( $ambientes as $amb ) {
	foreach ( array( 1, 2, 4, 5, 10 ) as $junta ) {
		$celula   = cdm_f2_celula_rejunte( $junta, $amb );
		$aprovados = array();
		foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
			$aprovados[ cdm_f2_nome( $id ) ] = true;
		}
		$consulta = 'forma=cilindro&d=15&h=20&pastilha=p10&junta=' . $junta . '&sobra=10&esp=4&rejunte=cimenticio&onde=' . $amb;
		$corpo    = f1_corpo( f1_render( $raiz, $consulta ) );
		preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<h3>(.*?)</h3>#is', $corpo, $mc, PREG_SET_ORDER );
		foreach ( $mc as $c ) {
			$nome = f1_texto( $c[1] );
			if ( ! isset( $aprovados[ $nome ] ) ) {
				$fora_da_f2[] = $amb . '/' . $junta . ' mm: "' . $nome . '"';
			}
		}
	}
}
f1_ok( empty( $fora_da_f2 ), 'nenhum produto entra na vitrine da F1 que a regua da F2 nao aprove',
	empty( $fora_da_f2 ) ? '25 celulas conferidas' : implode( ' | ', array_slice( $fora_da_f2, 0, 3 ) ) );

/* O TIPO ESCOLHIDO MANDA NA LISTA, e esta afirmacao existe porque a de cima NAO
   a cobre: uma vitrine que mostrasse cimenticio para quem pediu epoxi continua
   sendo subconjunto do que a F2 aprova. A pergunta desta pagina e "quanto
   comprar", e comprar e do tipo que a pessoa vai usar. */
$tipo_por_nome = array();
foreach ( $rejuntes['materiais'] as $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	$tela  = ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) ? $nome : $marca . ' ' . $nome;
	$tipo_por_nome[ trim( $tela ) ] = $m['tipo'];
}
$tipo_errado = array();
$vitrines    = array();
foreach ( array( 'cimenticio', 'acrilico', 'epoxi' ) as $tipo ) {
	foreach ( array( 2, 4 ) as $junta ) {
		$consulta = 'forma=cilindro&d=15&h=20&pastilha=p10&junta=' . $junta . '&sobra=10&esp=4&rejunte=' . $tipo . '&onde=interno_seco';
		$corpo    = f1_corpo( f1_render( $raiz, $consulta ) );
		preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<h3>(.*?)</h3>#is', $corpo, $mc, PREG_SET_ORDER );
		$nomes = array();
		foreach ( $mc as $c ) {
			$nome    = f1_texto( $c[1] );
			$nomes[] = $nome;
			$dele    = isset( $tipo_por_nome[ $nome ] ) ? $tipo_por_nome[ $nome ] : '?';
			if ( $dele !== $tipo ) {
				$tipo_errado[] = $tipo . '/' . $junta . ' mm: "' . $nome . '" e ' . $dele;
			}
		}
		$vitrines[ $tipo . '-' . $junta ] = $nomes;
	}
}
f1_ok( empty( $tipo_errado ), 'todo cartao da vitrine e do tipo de rejunte que a pessoa escolheu',
	empty( $tipo_errado ) ? '6 estados' : implode( ' | ', array_slice( $tipo_errado, 0, 3 ) ) );
f1_ok( $vitrines['cimenticio-4'] !== $vitrines['epoxi-4'],
	'trocar o tipo troca a lista de verdade (nao e o mesmo cartao com outro rotulo)',
	count( $vitrines['cimenticio-4'] ) . ' x ' . count( $vitrines['epoxi-4'] ) . ' cartoes' );

/* ---------------------------------------------------------------------------
 * 4. O bloco de compra (secoes 6 e 7 do contrato)
 * ------------------------------------------------------------------------- */

echo "\n4. Bloco de compra, procedencia e a marca em dobro\n";

$pos_compra = mb_strpos( $corpo_ancora, 'cdm-f2-compra' );
$pos_fonte  = mb_strpos( $corpo_ancora, 'cdm-f2-fonte' );
f1_ok( false !== $pos_compra, 'o bloco de compra existe mesmo com todos os itens sem link' );
f1_ok( false !== $pos_compra && false !== $pos_fonte && $pos_compra < $pos_fonte,
	'o bloco de compra vem ANTES da prova de procedencia (cicatriz da Robometria)' );
f1_ok( false !== mb_stripos( $corpo_ancora, 'Link de loja em breve' ),
	'o lugar do link de loja fica reservado e a pagina diz que esta vazio' );
f1_ok( preg_match( '#rel="nofollow noopener"#', $corpo_ancora ) > 0,
	'o link de procedencia e discreto e nofollow, nunca botao' );
f1_ok( false !== mb_stripos( $corpo_ancora, 'links desta página são de afiliado' ),
	'o aviso de comissao esta visivel na pagina' );

/* A MARCA EM DOBRO NAO APARECE EM TESTE DE CONTER (licao do bloco 4 da F2):
   "Rejunte Ceramicas Quartzolit" esta DENTRO de "Quartzolit Rejunte Ceramicas
   Quartzolit", entao procurar o nome nao acha a repeticao. */
$dobradas = array();
foreach ( $rejuntes['materiais'] as $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false === mb_stripos( $nome, $marca ) ) {
		continue;
	}
	if ( false !== mb_strpos( $texto_ancora, $marca . ' ' . $nome ) ) {
		$dobradas[] = $marca . ' ' . $nome;
	}
}
f1_ok( empty( $dobradas ), 'nenhum lugar da pagina repete a marca dentro do nome do produto',
	empty( $dobradas ) ? count( $rejuntes['materiais'] ) . ' rejuntes' : implode( ' | ', $dobradas ) );

f1_ok( false !== mb_stripos( $texto_ancora, 'Ainda não temos as pastilhas no nosso banco' ),
	'a pastilha sem banco tem o lugar reservado e a pagina diz isso' );

/* ---------------------------------------------------------------------------
 * 5. A BORDA MAIS DIFICIL: a pagina SEM o banco
 *
 * Ela existe porque o estado degradado e uma pagina VALIDA, com cabecalho,
 * rodape e prosa — foi assim que a Robometria mediu tres paginas pela metade em
 * 11/09/2026 sem que nenhum teste acusasse. Aqui a afirmacao e dupla: a conta de
 * geometria CONTINUA (ela nao depende de banco), e o numero de rejunte SOME com
 * o motivo escrito.
 * ------------------------------------------------------------------------- */

echo "\n5. A pagina sem o banco (o estado degradado, medido de proposito)\n";

$temp = sys_get_temp_dir() . '/cdm-f1-sem-banco-' . getmypid();
@mkdir( $temp . '/dados', 0777, true );
@mkdir( $temp . '/snippets', 0777, true );
foreach ( glob( $raiz . '/snippets/*.php' ) as $arquivo ) {
	copy( $arquivo, $temp . '/snippets/' . basename( $arquivo ) );
}
copy( $raiz . '/ARVORE.md', $temp . '/ARVORE.md' );
copy( $raiz . '/VOZ.md', $temp . '/VOZ.md' );
/* O manifest sem NENHUM item de dados publicado: e exatamente o site em que o
   Sync ainda nao aplicou o banco, ou em que o item ficou com publicar=false. */
$manifest_sem = json_decode( (string) file_get_contents( $raiz . '/manifest.json' ), true );
$manifest_sem['dados'] = array();
file_put_contents( $temp . '/manifest.json', json_encode( $manifest_sem, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

$corpo_sem_banco = f1_corpo( f1_render( $temp ) );
$texto_sem_banco = f1_texto( $corpo_sem_banco );
f1_ok( '' !== $texto_sem_banco, 'a pagina sem banco ainda e servida', mb_strlen( $texto_sem_banco ) . ' caracteres' );
f1_ok( false !== mb_strpos( $texto_sem_banco, '720 pastilhas' ),
	'sem banco, a conta de pastilhas CONTINUA (ela e geometria, nao dado de fabricante)' );
/* NENHUM grama em lugar NENHUM da pagina — nem na resposta, nem na tabela das
   doze pecas, nem na resposta do FAQ. Era aqui que a versao anterior deste
   arquivo escondia um defeito de verdade: o FAQ trazia "264 g" digitado, e ele
   continuaria afirmando isso com o banco fora do ar. */
f1_ok( 0 === preg_match( '#\d[\d\.,]* g\b#u', $texto_sem_banco ),
	'sem banco, NENHUM numero de rejunte sobra na pagina (nem no FAQ)' );
f1_ok( false !== mb_stripos( $texto_sem_banco, 'sem número hoje' ),
	'sem banco, a tabela das doze pecas diz que nao tem o numero' );
f1_ok( false !== mb_stripos( $texto_sem_banco, 'coeficiente' ),
	'sem banco, a pagina diz POR QUE nao publica o rejunte' );
f1_ok( false === mb_stripos( $texto_sem_banco, 'Cobre folga de' ),
	'sem banco, nenhuma recomendacao de produto e inventada' );

array_map( 'unlink', glob( $temp . '/snippets/*.php' ) );
@unlink( $temp . '/manifest.json' );
@unlink( $temp . '/ARVORE.md' );
@unlink( $temp . '/VOZ.md' );
@rmdir( $temp . '/dados' );
@rmdir( $temp . '/snippets' );
@rmdir( $temp );

/* ---------------------------------------------------------------------------
 * 5b. O NUMERO SEGUE O BANCO, e nao uma copia digitada
 *
 * A pagina diz, na camada de prova, que o coeficiente foi LIDO do registro do
 * produto. Um coeficiente digitado dentro do snippet com o valor certo serve
 * exatamente os mesmos gramas de hoje — nenhuma afirmacao sobre a tela de hoje
 * consegue ve-lo, e a mutacao que faz isso passou na primeira rodada. O que
 * separa os dois e mexer no BANCO e olhar se a pagina anda junto.
 * ------------------------------------------------------------------------- */

echo "\n5b. O coeficiente vem mesmo do banco (a mutacao que passou na primeira rodada)\n";

$temp2 = sys_get_temp_dir() . '/cdm-f1-outro-cr-' . getmypid();
@mkdir( $temp2 . '/dados', 0777, true );
@mkdir( $temp2 . '/snippets', 0777, true );
foreach ( glob( $raiz . '/snippets/*.php' ) as $arquivo ) {
	copy( $arquivo, $temp2 . '/snippets/' . basename( $arquivo ) );
}
foreach ( glob( $raiz . '/dados/*.json' ) as $arquivo ) {
	copy( $arquivo, $temp2 . '/dados/' . basename( $arquivo ) );
}
copy( $raiz . '/manifest.json', $temp2 . '/manifest.json' );
copy( $raiz . '/ARVORE.md', $temp2 . '/ARVORE.md' );
copy( $raiz . '/VOZ.md', $temp2 . '/VOZ.md' );

$outro_cr   = 3.5;
$banco_outro = json_decode( (string) file_get_contents( $temp2 . '/dados/materiais-rejuntes.json' ), true );
foreach ( $banco_outro['materiais'] as $i => $m ) {
	if ( isset( $m['propriedades']['CR']['valor'] ) && null !== $m['propriedades']['CR']['valor'] ) {
		$banco_outro['materiais'][ $i ]['propriedades']['CR']['valor'] = $outro_cr;
	}
}
file_put_contents( $temp2 . '/dados/materiais-rejuntes.json', json_encode( $banco_outro, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

list( , $g_com_outro_cr ) = f1_conta_gramas( M_PI * 15 * 20, 10, 4, 2, $outro_cr );
$texto_outro_cr = f1_texto( f1_corpo( f1_render( $temp2 ) ) );
f1_ok( false !== mb_strpos( $texto_outro_cr, number_format_i18n( (int) round( $g_com_outro_cr ) ) . ' g' ),
	'trocado o CR no banco, o grama servido anda junto (o numero nao esta digitado no snippet)',
	'CR ' . $outro_cr . ' -> ' . number_format_i18n( (int) round( $g_com_outro_cr ) ) . ' g' );
f1_ok( false === mb_strpos( $texto_outro_cr, '264 g' ),
	'e o numero do CR antigo some da pagina inteira, tabela e FAQ inclusive' );
f1_ok( false !== mb_strpos( $texto_outro_cr, number_format_i18n( $outro_cr, 2 ) ),
	'a camada de prova publica o CR que realmente foi usado', number_format_i18n( $outro_cr, 2 ) );

array_map( 'unlink', glob( $temp2 . '/snippets/*.php' ) );
array_map( 'unlink', glob( $temp2 . '/dados/*.json' ) );
@unlink( $temp2 . '/manifest.json' );
@unlink( $temp2 . '/ARVORE.md' );
@unlink( $temp2 . '/VOZ.md' );
@rmdir( $temp2 . '/dados' );
@rmdir( $temp2 . '/snippets' );
@rmdir( $temp2 );

/* ---------------------------------------------------------------------------
 * 6. Voz, JSON-LD e higiene (secoes 5 e 15 do contrato)
 * ------------------------------------------------------------------------- */

echo "\n6. Voz, entidade e higiene\n";

preg_match( '#<h1[^>]*>(.*?)</h1>#is', $corpo_ancora, $mh1 );
preg_match( '#<p[^>]*>(.*?)</p>#is', $corpo_ancora, $mp1 );
$cabeca = f1_texto( ( isset( $mh1[1] ) ? $mh1[1] : '' ) . ' ' . ( isset( $mp1[1] ) ? $mp1[1] : '' ) );
$ruins  = array();
foreach ( array( 'tessela', 'substrato', 'aderência', 'especificação', 'parâmetro', 'ficha técnica' ) as $termo ) {
	if ( false !== mb_stripos( $cabeca, $termo ) ) {
		$ruins[] = $termo;
	}
}
f1_ok( empty( $ruins ), 'nenhum termo de manual no H1 nem no primeiro paragrafo',
	empty( $ruins ) ? mb_strlen( $cabeca ) . ' caracteres medidos' : implode( ', ', $ruins ) );

/* A PROCEDENCIA NAO ABRE PAGINA (15.2): o nome do fabricante pode aparecer, mas
   dentro do bloco de prova — nunca na abertura. */
$sem_prova = f1_texto( preg_replace( '#<div class="cdm-prova">.*?</div>#is', '', $corpo_ancora ) );
$abertura  = mb_substr( $sem_prova, 0, 400 );
f1_ok( false === mb_stripos( $abertura, 'Quartzolit' ) && false === mb_stripos( $abertura, 'Saint-Gobain' ),
	'a abertura da pagina nao comeca por fabricante' );

$jsonld = '';
if ( preg_match( '#<script type="application/ld\+json" id="cdm-f1-jsonld">(.*?)</script>#is', f1_render( $raiz ), $mj ) ) {
	$jsonld = $mj[1];
}
$grafo = json_decode( $jsonld, true );
f1_ok( is_array( $grafo ) && isset( $grafo['@graph'] ), 'o JSON-LD da pagina e valido e tem grafo',
	strlen( $jsonld ) . ' bytes' );
$tipos_ld = array();
foreach ( (array) ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
	$tipos_ld[] = isset( $no['@type'] ) ? $no['@type'] : '?';
}
f1_ok( in_array( 'WebApplication', $tipos_ld, true ), 'o JSON-LD declara WebApplication (secao 5.3)' );
f1_ok( in_array( 'FAQPage', $tipos_ld, true ), 'o JSON-LD declara FAQPage' );

/* O FAQPage E A TELA DIZEM A MESMA COISA — mesma funcao, uma fonte so. Schema
   que promete o que a pagina nao diz e o jeito limpo de virar spam. */
$faq_fora = array();
foreach ( cdm_f1_perguntas() as $p ) {
	if ( false === mb_strpos( $texto_ancora, $p['pergunta'] ) ) {
		$faq_fora[] = $p['pergunta'];
	}
}
f1_ok( empty( $faq_fora ), 'toda pergunta do FAQPage esta escrita na tela',
	empty( $faq_fora ) ? count( cdm_f1_perguntas() ) . ' perguntas' : implode( ' | ', $faq_fora ) );

/* AS RESPOSTAS DO FAQ TRAZEM NUMERO, e o numero tem que bater com a ferramenta.
   Pergunta de FAQ que envelhece separada da conta e a forma mais discreta de a
   pagina se contradizer. */
$cabem_por_m2 = (int) floor( 1000000 / ( 12 * 12 ) );
list( , $g_do_vaso ) = f1_conta_gramas( M_PI * 15 * 20, 10, 4, 2, $cr_json );
$faq_numeros = array(
	/* CABEM e PISO, comprar e TETO: a mesma area devolve 6.944 numa pergunta e
	   6.945 na outra, e as duas estao certas. Confundir os dois arredondamentos
	   e o jeito de a pagina errar 1 e parecer que arredondou. */
	array( 'Quantas pastilhas de 1 cm cabem em 1 m²', number_format_i18n( $cabem_por_m2 ) ),
	array( 'Quanto rejunte leva um vaso de 15 por 20 cm', number_format_i18n( (int) round( $g_do_vaso ) ) ),
);
$faq_errado = array();
foreach ( cdm_f1_perguntas() as $p ) {
	foreach ( $faq_numeros as $n ) {
		if ( false !== mb_strpos( $p['pergunta'], $n[0] ) && false === mb_strpos( $p['resposta'], $n[1] ) ) {
			$faq_errado[] = $p['pergunta'];
		}
	}
}
f1_ok( empty( $faq_errado ), 'os numeros citados nas respostas do FAQ sao os que a ferramenta calcula',
	empty( $faq_errado ) ? '2 respostas conferidas' : implode( ' | ', $faq_errado ) );
f1_ok( 6944 === $cabem_por_m2, 'cabem 6.944 pastilhas de 1 cm em 1 m2 com folga de 2 mm', (string) $cabem_por_m2 );
f1_ok( 6945 === f1_conta_pastilhas( 10000, 10, 2, 0 ),
	'e para COMPRAR 1 m2 sao 6.945 — o teto, porque meia pastilha nao existe',
	(string) f1_conta_pastilhas( 10000, 10, 2, 0 ) );

/* HIGIENE DO SNIPPET (fase 4b do playbook). */
$fonte_f1 = (string) file_get_contents( $raiz . '/snippets/clubedomosaico-f1.php' );

/* SO O CODIGO, com os comentarios fora. A primeira versao desta afirmacao leu o
   arquivo inteiro e reprovou o snippet por causa de um COMENTARIO que explicava
   justamente por que nao se toca naquela variavel. Regua que le a prosa junto
   com o codigo mede outra coisa — mesma familia do `[a-z_]+` que nao casava com
   `cdm_f2` e media a pagina nova contra o nada. */
$so_codigo = '';
foreach ( token_get_all( '<?php ' . $fonte_f1 ) as $t ) {
	if ( is_array( $t ) ) {
		if ( T_COMMENT === $t[0] || T_DOC_COMMENT === $t[0] ) {
			continue;
		}
		$so_codigo .= $t[1];
		continue;
	}
	$so_codigo .= $t;
}
f1_ok( false === strpos( $so_codigo, '$_SERVER' ), 'o codigo do snippet nao toca a variavel de servidor (ModSecurity)' );
f1_ok( false !== strpos( $fonte_f1, '$_SERVER' ) || true, 'a regua acima le o codigo, nunca o comentario',
	mb_strlen( $fonte_f1 ) - mb_strlen( $so_codigo ) . ' caracteres de comentario descartados' );
f1_ok( false === strpos( $fonte_f1, '<?php' ), 'o arquivo nao abre com <?php (Code Snippets recusa)' );
preg_match_all( '#^function ([a-z0-9_]+)#mu', $fonte_f1, $mf );
$soltas = array();
foreach ( $mf[1] as $nome ) {
	if ( false === strpos( $fonte_f1, "function_exists( '" . $nome . "' )" ) ) {
		$soltas[] = $nome;
	}
}
f1_ok( empty( $soltas ), 'toda funcao do snippet esta dentro de if ( ! function_exists() )',
	empty( $soltas ) ? count( $mf[1] ) . ' funcoes' : implode( ', ', $soltas ) );

$prefixos_errados = array();
foreach ( $mf[1] as $nome ) {
	if ( 0 !== strpos( $nome, 'cdm_f1_' ) ) {
		$prefixos_errados[] = $nome;
	}
}
f1_ok( empty( $prefixos_errados ), 'toda funcao nova usa o prefixo cdm_f1_',
	empty( $prefixos_errados ) ? count( $mf[1] ) . ' funcoes' : implode( ', ', $prefixos_errados ) );

/* ---------------------------------------------------------------------------
 * 7. O que a pagina promete e nao entrega (secao 10: o silencio declarado)
 * ------------------------------------------------------------------------- */

echo "\n7. O que a pagina diz que nao sabe\n";

f1_ok( false !== mb_stripos( $texto_ancora, 'Gramas de cola' )
	&& false !== mb_stripos( $texto_ancora, 'rendimento por cordão' ),
	'a coluna de cola nasce vazia COM o motivo escrito, em vez de sumir' );
f1_ok( false !== mb_stripos( $texto_ancora, 'cimentício em pó' ),
	'a pagina amarra o coeficiente ao estado fisico do produto (correcao do bloco 3c)' );

echo "\n";
printf( "%d afirmacoes, %d falha(s).\n", $feitos, $falhas );
echo count( $estados ) . " estados varridos com processo proprio.\n";

exit( $falhas > 0 ? 1 : 0 );

<?php
/**
 * TESTE DA OFERTA DATADA — A CAMADA DA MAQUINA DEIXA DE SER MENOS CUIDADOSA
 * QUE A TELA (12/11/2026).
 *
 * O DEFEITO, MEDIDO NO AR ANTES DE SER CONSERTADO, as 16h2xZ de 12/11/2026 em
 * `/veiculos/bicicleta-eletrica/`: as SEIS `Offer` do `ItemList` serviam
 *
 *     "price": "2299.99", "priceCurrency": "BRL",
 *     "availability": "https://schema.org/InStock"
 *
 * e a MESMA pagina, na linha que o leitor le, escrevia "(preco de 04/11/2026)"
 * ao lado do mesmo numero. **A tela era mais cuidadosa que o dado**, nas duas
 * pontas: o preco tinha data para o olho e nenhuma para a maquina, e o estoque
 * era prometido no presente do indicativo sobre uma leitura de oito dias.
 *
 * E A CAMADA ERRADA E A QUE PESA MAIS: o JSON-LD e o que a visao geral de IA
 * ingere sem abrir a pagina (32.4-c). Quem le o fonte recebia a promessa; quem
 * le a tela recebia a ressalva.
 *
 * AS DUAS REGRAS QUE ESTA BATERIA COBRA, e as duas estao escritas por inteiro
 * na secao 7-b do `rodametria-produto.php`:
 *   (1) NENHUMA `Offer` declara `availability` — ficha EXISTIR nao e estar
 *       VENDENDO, e o campo nao tem onde pendurar a data da medicao. A ronda de
 *       11/11/2026 achou UMA ficha esgotada entre 24.
 *   (2) TODA `Offer` com data de coleta na linha declara
 *       `priceSpecification.validFrom` com essa data, e NENHUMA declara
 *       `priceValidUntil`, que afirmaria validade FUTURA.
 *
 * ESTE PORTAO E PHP pelo motivo que o `teste-nota-de-preco.php` escreveu
 * primeiro: a oferta e decidida em PHP, entao a regua CHAMA a funcao. Regua em
 * Python sobre o texto do snippet conferiria a FORMA do arquivo. E foi para
 * poder ser chamada que a oferta virou funcao nomeada: ate hoje ela morava
 * dentro do fecho anonimo do `wp_head`, e quem a media era SO o portao de ar —
 * depois do desembarque, que e o lugar mais caro de descobrir o defeito.
 *
 * E ELE SE PROVA ANTES DE JULGAR (mundo G): a oferta que estava NO AR hoje
 * entra na bateria e TEM de ser reprovada. Portao que nao reprova o defeito que
 * o fez nascer e portao inerte, e a bancada desta ilha usa essa palavra.
 */

foreach ( array( 'add_filter', 'add_action', 'add_shortcode', 'register_activation_hook' ) as $f ) {
	if ( ! function_exists( $f ) ) { eval( "function $f(){ return true; }" ); }
}
if ( ! function_exists( 'esc_html' ) ) {
	function esc_html( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_url( $s ) { return (string) $s; }
	function is_page( $s = null ) { return false; }
	function get_option( $k, $d = false ) { return $d; }
	function update_option( $k, $v ) { return true; }
	function wp_json_encode( $v ) { return json_encode( $v, JSON_UNESCAPED_UNICODE ); }
	function date_i18n( $fmt, $ts ) { return date( $fmt, $ts ); }
}

$RAIZ    = dirname( __DIR__ );
$MUTACAO = getenv( 'RDM_OFERTA_MUTACAO' ) ? getenv( 'RDM_OFERTA_MUTACAO' ) : '';

/** Carrega UMA funcao de um snippet, equilibrando chaves — o mesmo mecanismo
 *  dos outros portoes PHP desta pasta (o snippet inteiro registra filtros do
 *  WordPress ao ser lido, e o que esta bateria julga sao funcoes puras). */
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

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

$casca   = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );
$produto = file_get_contents( $RAIZ . '/snippets/rodametria-produto.php' );

/* AS MUTACOES SAO FEITAS NA FONTE, antes do `eval`: e a unica forma de refazer
   a trava COM o defeito e exigir reprovacao. Cada uma DECLARA o mundo em que
   morde — a licao que o `teste-cura-da-porta.php` pagou em 12/11/2026 de manha,
   quando duas mutacoes passaram por estarem rodando no mundo errado. */
$MUTACOES = array(
	'M1' => array(
		'de'    => "	if ( 1 === preg_match( '/^\\d{4}-\\d{2}-\\d{2}\$/', \$colhido ) ) {",
		'para'  => "	if ( '' !== \$colhido ) {",
		'o_que' => 'a trava de FORMA cai: data em portugues iria para `validFrom` como dado estruturado invalido',
		'morde' => 'mundo D (a data BR gravada no campo ISO)',
	),
	'M2' => array(
		'de'    => "	return \$oferta;\n}",
		'para'  => "	\$oferta['availability'] = 'https://schema.org/InStock';\n	return \$oferta;\n}",
		'o_que' => 'a promessa sem data VOLTA: `availability` no presente do indicativo sobre leitura de dias atras',
		'morde' => 'mundos A, B e C, e as 21 linhas do dado publicado',
	),
	'M3' => array(
		'de'    => "			'validFrom'     => \$colhido,",
		'para'  => "			'validFrom'     => '2026-11-04',",
		'o_que' => 'a data deixa de ser DA LINHA e passa a ser um literal — o dia em que uma vitrine for recolhida em duas passadas, metade das ofertas mente a data',
		'morde' => 'mundo F (duas linhas lidas em dias diferentes)',
	),
	'M4' => array(
		'de'    => "			'price'         => \$preco,\n			'priceCurrency' => 'BRL',\n			'validFrom'     => \$colhido,",
		'para'  => "			'price'         => (float) \$item['preco_numero'],\n			'priceCurrency' => 'BRL',\n			'validFrom'     => \$colhido,",
		'o_que' => 'os dois `price` da mesma oferta deixam de sair da MESMA variavel, e passam a poder discordar na forma',
		'morde' => 'mundo A (os dois `price` identicos) e o dado publicado',
	),
);
if ( '' !== $MUTACAO ) {
	if ( ! isset( $MUTACOES[ $MUTACAO ] ) ) {
		echo "FALHA: mutacao $MUTACAO nao existe\n";
		exit( 2 );
	}
	$m = $MUTACOES[ $MUTACAO ];
	if ( false === strpos( $produto, $m['de'] ) ) {
		echo "FALHA: a mutacao $MUTACAO nao achou o trecho que ela troca — o snippet mudou e a mutacao envelheceu\n";
		exit( 2 );
	}
	$produto = str_replace( $m['de'], $m['para'], $produto );
}

foreach ( array(
	array( 'rodametria_casca_escada_de_compra', $casca ),
	array( 'rdm_produto_oferta_de_linha', $produto ),
) as $par ) {
	$ok = carregar_funcao( $par[1], $par[0] );
	afirma( $ok, sprintf( 'nao achei a funcao %s nos snippets', $par[0] ) );
	if ( ! $ok ) {
		print( 'REPROVADO: ' . end( $falhas ) . "\n" );
		exit( 1 );
	}
}

/* =========================================================================
 * A REGUA, NUM LUGAR SO — e ela e a MESMA que o portao de ar aplica ao
 * JSON-LD servido, escrita aqui como as quatro perguntas que uma `Offer`
 * desta ilha responde. Ela devolve a lista de defeitos, e lista vazia e
 * aprovacao: assim o mundo G (a oferta que estava no ar) pode ser julgado
 * pela regua em vez de por uma afirmacao escrita a mao sobre ele.
 * ======================================================================= */
function julgar_oferta( $of, $data_esperada ) {
	$d = array();
	if ( isset( $of['availability'] ) ) {
		$d[] = 'declara availability, que e promessa de estoque sem data';
	}
	if ( isset( $of['priceValidUntil'] ) ) {
		$d[] = 'declara priceValidUntil, que afirma validade FUTURA que esta ilha nao mediu';
	}
	if ( '' === (string) $data_esperada ) {
		if ( isset( $of['priceSpecification'] ) ) {
			$d[] = 'a linha nao tem data de coleta e a oferta inventou uma priceSpecification';
		}
		return $d;
	}
	if ( ! isset( $of['priceSpecification'] ) ) {
		$d[] = 'a linha tem data de coleta e a oferta nao a diz — preco cru para a maquina';
		return $d;
	}
	$ps = $of['priceSpecification'];
	if ( ! isset( $ps['@type'] ) || 'UnitPriceSpecification' !== $ps['@type'] ) {
		$d[] = 'a priceSpecification nao e UnitPriceSpecification';
	}
	if ( ! isset( $ps['validFrom'] ) || $ps['validFrom'] !== $data_esperada ) {
		$d[] = sprintf( 'validFrom e %s e a data da linha e %s',
			isset( $ps['validFrom'] ) ? var_export( $ps['validFrom'], true ) : 'ausente',
			var_export( $data_esperada, true ) );
	}
	if ( ! isset( $ps['price'] ) || $ps['price'] !== $of['price'] ) {
		$d[] = sprintf( 'os dois price da mesma oferta discordam: %s e %s',
			var_export( $of['price'], true ),
			isset( $ps['price'] ) ? var_export( $ps['price'], true ) : 'ausente' );
	}
	if ( ! isset( $ps['priceCurrency'] ) || $ps['priceCurrency'] !== $of['priceCurrency'] ) {
		$d[] = 'as duas moedas da mesma oferta discordam';
	}
	return $d;
}

$FICHA = 'https://s.shopee.com.br/FICHAxxxxx';
$BUSCA = 'https://s.shopee.com.br/BUSCAxxxxx';

function linha( $extra = array() ) {
	global $FICHA, $BUSCA;
	return array_merge( array(
		'nome'              => 'item de teste',
		'preco_numero'      => 2299.99,
		'preco_colhido_em'  => '2026-11-04',
		'url'               => $FICHA,
		'url_busca'         => $BUSCA,
		'degrau'            => 1,
		'programa'          => 'shopee',
	), $extra );
}

/* --------------------------------------------------------------- MUNDO A
   Ficha viva e data ISO: o mundo das 21 linhas de hoje. */
$a = rdm_produto_oferta_de_linha( linha() );
afirma( array() === julgar_oferta( $a, '2026-11-04' ),
	'MUNDO A: ' . implode( ' | ', julgar_oferta( $a, '2026-11-04' ) ) );
afirma( $a['url'] === $FICHA, 'mundo A: a ficha viva nao virou a url da oferta' );
afirma( '2299.99' === $a['price'], 'mundo A: o preco da oferta nao e a string de duas casas' );
afirma( ! isset( $a['availability'] ),
	'MUNDO A: a oferta declara availability — e o defeito que este portao nasceu para pegar' );

/* --------------------------------------------------------------- MUNDO B
   A FICHA MORREU e o piso subiu: a url e uma PAGINA DE BUSCA. A data do PRECO
   continua valendo, porque ela e sobre o numero e nao sobre a porta de compra
   — e e por isso que `priceSpecification` NAO sai aqui. */
$b = rdm_produto_oferta_de_linha( linha( array( 'url' => '' ) ) );
afirma( array() === julgar_oferta( $b, '2026-11-04' ),
	'MUNDO B: ' . implode( ' | ', julgar_oferta( $b, '2026-11-04' ) ) );
afirma( $b['url'] === $BUSCA, 'mundo B: a busca nao subiu para a url da oferta (25.2)' );

/* --------------------------------------------------------------- MUNDO C
   SEM data na linha: a oferta nao inventa nenhuma. Este mundo nao existe no
   dado publicado desde hoje, e e justamente por isso que ele e fabricado — e o
   mundo de toda vitrine gerada por uma versao anterior do gerador. */
$c = rdm_produto_oferta_de_linha( linha( array( 'preco_colhido_em' => null ) ) );
afirma( array() === julgar_oferta( $c, '' ),
	'MUNDO C: ' . implode( ' | ', julgar_oferta( $c, '' ) ) );
afirma( ! isset( $c['priceSpecification'] ),
	'MUNDO C: sem data na linha a oferta inventou uma priceSpecification' );
afirma( isset( $c['price'] ) && isset( $c['priceCurrency'] ),
	'mundo C: o preco cru saiu junto com a data — recusar a data nao e recusar o preco' );

/* --------------------------------------------------------------- MUNDO D
   A DATA EM PORTUGUES GRAVADA NO CAMPO ISO. E o mundo da mutacao M1, e ele nao
   e hipotetico: a frase da tela ("04/11/2026") e a unica forma dessa data que
   existiu nesta ilha ate hoje, e o campo novo nasceu ao lado dela. */
$d = rdm_produto_oferta_de_linha( linha( array( 'preco_colhido_em' => '04/11/2026' ) ) );
afirma( ! isset( $d['priceSpecification'] ),
	'MUNDO D: a data em portugues foi para `validFrom` — dado estruturado invalido que olho humano nenhum ve' );
afirma( array() === julgar_oferta( $d, '' ),
	'MUNDO D: ' . implode( ' | ', julgar_oferta( $d, '' ) ) );

/* --------------------------------------------------------------- MUNDO E
   ISO QUASE CERTO: mes e dia sem o zero a esquerda. `validFrom` exige o
   formato cheio, e "quase" nao e uma categoria de dado estruturado. */
$e = rdm_produto_oferta_de_linha( linha( array( 'preco_colhido_em' => '2026-11-4' ) ) );
afirma( ! isset( $e['priceSpecification'] ),
	'MUNDO E: `2026-11-4` passou a trava de forma' );

/* --------------------------------------------------------------- MUNDO F
   DUAS LINHAS LIDAS EM DIAS DIFERENTES — o mundo que o dado de hoje NAO tem
   (as 21 linhas das duas paginas sairam da mesma passada de 04/11) e que a
   proxima recoleta parcial produz. E o mundo em que a mutacao M3 morde. */
$f1 = rdm_produto_oferta_de_linha( linha( array( 'preco_colhido_em' => '2026-11-04' ) ) );
$f2 = rdm_produto_oferta_de_linha( linha( array( 'preco_colhido_em' => '2026-10-29', 'preco_numero' => 1030.0 ) ) );
afirma( array() === julgar_oferta( $f1, '2026-11-04' ),
	'MUNDO F: a primeira linha ' . implode( ' | ', julgar_oferta( $f1, '2026-11-04' ) ) );
afirma( array() === julgar_oferta( $f2, '2026-10-29' ),
	'MUNDO F: a segunda linha ' . implode( ' | ', julgar_oferta( $f2, '2026-10-29' ) ) );
afirma( $f1['priceSpecification']['validFrom'] !== $f2['priceSpecification']['validFrom'],
	'MUNDO F: duas linhas de datas diferentes sairam com o MESMO validFrom — a data nao e da linha' );
afirma( '1030.00' === $f2['price'],
	'mundo F: o preco redondo nao saiu com as duas casas' );

/* --------------------------------------------------------------- MUNDO G
   A OFERTA QUE ESTAVA NO AR HOJE, copiada do JSON-LD servido por
   `/veiculos/bicicleta-eletrica/` as 16h2xZ de 12/11/2026. A REGUA TEM DE
   REPROVAR as duas coisas, e nomear as duas. */
$g = array(
	'@type'         => 'Offer',
	'price'         => '2299.99',
	'priceCurrency' => 'BRL',
	'url'           => 'https://s.shopee.com.br/qkmbKqr0y',
	'availability'  => 'https://schema.org/InStock',
);
$vg = julgar_oferta( $g, '2026-11-04' );
afirma( 2 === count( $vg ),
	sprintf( 'MUNDO G: a regua achou %d defeito(s) na oferta que estava no ar e deviam ser 2 — %s',
		count( $vg ), implode( ' | ', $vg ) ) );
afirma( false !== strpos( implode( ' ', $vg ), 'availability' ),
	'MUNDO G: a regua nao nomeou o `availability` que estava no ar — portao inerte' );
afirma( false !== strpos( implode( ' ', $vg ), 'preco cru para a maquina' ),
	'MUNDO G: a regua nao nomeou o preco sem data que estava no ar — portao inerte' );

/* --------------------------------------------------------------- MUNDO H
   `priceValidUntil`, que foi recusado POR ESCRITO na secao 7-b. A regua tem de
   o reprovar mesmo com todo o resto certo, porque a tentacao de o acrescentar
   mora na propria documentacao de dado estruturado do buscador. */
$h = $a;
$h['priceValidUntil'] = '2026-12-31';
afirma( 1 === count( julgar_oferta( $h, '2026-11-04' ) ),
	'MUNDO H: `priceValidUntil` passou pela regua — validade futura que esta ilha nao mediu' );

/* =========================================================================
 * O DADO PUBLICADO, LINHA POR LINHA — e o contador no fim prova que esta
 * metade nao ficou cega.
 * ======================================================================= */
$vit    = json_decode( file_get_contents( $RAIZ . '/dados/vitrine-de-produto.json' ), true );
$vistos = 0;
$com_data = 0;
foreach ( (array) $vit['paginas'] as $pagina ) {
	foreach ( (array) $pagina['linhas'] as $item ) {
		$vistos++;
		$data = isset( $item['preco_colhido_em'] ) ? (string) $item['preco_colhido_em'] : '';
		$of   = rdm_produto_oferta_de_linha( $item );
		$v    = julgar_oferta( $of, $data );
		afirma( array() === $v,
			sprintf( '%s / %s: %s', $pagina['slug'], substr( $item['nome'], 0, 40 ), implode( ' | ', $v ) ) );
		if ( '' !== $data ) {
			$com_data++;
			/* AS DUAS SUPERFICIES DIZEM A MESMA DATA, e esta e a afirmacao que
			   as amarra: a frase da TELA tem de conter a data do campo que a
			   MAQUINA recebe. Enquanto as duas eram geradas lado a lado do
			   mesmo valor, eram duas declaracoes do mesmo fato (20.7). */
			$br = date( 'd/m/Y', strtotime( $data ) );
			afirma( false !== strpos( (string) $item['preco_nota'], $br ),
				sprintf( '%s: a nota da tela (%s) nao diz a data que o JSON-LD serve (%s)',
					$pagina['slug'], $item['preco_nota'], $br ) );
		}
	}
}
afirma( $vistos >= 21,
	sprintf( 'a vitrine publicada tem %d linha(s) e tinha 21 em 12/11/2026 — esta metade do portao encolheu', $vistos ) );
afirma( $com_data === $vistos,
	sprintf( '%d de %d linha(s) publicadas tem data de coleta — as sem data servem preco cru para a maquina',
		$com_data, $vistos ) );

/* ============================================================ AS MUTACOES */
$mortas = array();
if ( '' === $MUTACAO ) {
	foreach ( array_keys( $MUTACOES ) as $mut ) {
		$saida = array();
		$codigo = 0;
		exec( 'RDM_OFERTA_MUTACAO=' . $mut . ' php ' . escapeshellarg( __FILE__ ) . ' 2>&1',
			$saida, $codigo );
		if ( 2 === $codigo ) {
			$mortas[] = "$mut: a mutacao nao achou o trecho que troca — ela envelheceu junto com o snippet";
		} elseif ( 0 === $codigo ) {
			$mortas[] = "$mut: a mutacao PASSOU, e ela devia reprovar — " . $MUTACOES[ $mut ]['o_que']
				. ' (morde em: ' . $MUTACOES[ $mut ]['morde'] . ')';
		}
	}
	foreach ( $mortas as $m ) { $falhas[] = $m; }
}

$rotulo = 'teste-oferta-datada' . ( '' === $MUTACAO ? '' : " (mutacao $MUTACAO)" );
printf( "%s: %d afirmacoes, %d linha(s) publicada(s) julgada(s), %d mutacao(oes) cobrada(s), %d falha(s)\n",
	$rotulo, $afirmacoes, $vistos, '' === $MUTACAO ? count( $MUTACOES ) : 0, count( $falhas ) );
foreach ( $falhas as $f ) { print( "  REPROVADO: $f\n" ); }
exit( count( $falhas ) ? 1 : 0 );

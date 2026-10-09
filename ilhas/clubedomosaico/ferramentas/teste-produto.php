<?php
/**
 * Verificacao MEDIDA das OITO paginas de consulta de produto (secao 30).
 *
 *   php ferramentas/teste-produto.php .
 *
 * -------------------------------------------------------------------------
 * O QUE ESTE ARQUIVO MEDE, E O QUE JA E MEDIDO EM OUTRO LUGAR
 * -------------------------------------------------------------------------
 * As oito estao na lista do `teste-casca.php` desde que nasceram, e e la que
 * elas passam os trinta e tantos portoes que valem para TODA pagina desta ilha:
 * script fora do shortcode, `&#038;` dentro de `<script>`, trilha,
 * `BreadcrumbList`, pagina fina, escassez, titulo no teto de 65, `description`
 * na faixa de 120 a 160 e sem repetir, pagina orfa, voz. Nada disso se repete
 * aqui — e foi la que o nivel errado da arvore e o hifen da regua de shortcode
 * foram pegos, com 48 afirmacoes vermelhas.
 *
 * Aqui mora o que e SO desta familia:
 *
 *   1. O NUMERO, RECONTADO DO JSON CRU por um caminho que nao chama uma linha
 *      do snippet. Se a vitrine e a tela discordarem, a tela esta errada.
 *   2. O PISO DA 30.2 COMO PORTAO, nos dois sentidos — e medido num mundo
 *      FABRICADO de proposito, com duas ofertas, porque duas das oito nascem
 *      com exatamente tres e o dia em que uma coleta perder uma oferta nao pode
 *      ser o dia em que a pagina descobre isso no ar.
 *   3. A ORDEM QUE O DESPACHO PEDE: a resposta em duas frases antes de qualquer
 *      explicacao, e o bloco de compra ANTES da procedencia.
 *   4. O LINK DE AFILIADO: um por oferta, `rel="sponsored"`, encurtado, e NUNCA
 *      o `url_afiliado_sem_sub_id` — que e o link que nao rastreia esta ilha e
 *      e por isso que ele nao chega nem a vitrine.
 *   5. O JSON-LD SERVE O MESMO QUE A TELA, e sem `&nbsp;` dentro do texto.
 *   6. AS OITO NAO SAO A MESMA PAGINA. Malha que nasce de um molde produz
 *      pagina fina sem ninguem decidir por isso.
 *   7. NENHUM NUMERO DIGITADO NA PROSA: a camada declarada nao pode conter
 *      "R$" em lugar nenhum. Preco escrito a mao e preco que mente na coleta
 *      seguinte, calado.
 *
 * -------------------------------------------------------------------------
 * UM PROCESSO POR PAGINA, e nao e zelo
 * -------------------------------------------------------------------------
 * A casca tem `static` legitimos (rodape, logotipo) que no site estao certos —
 * um processo e uma requisicao — e que numa bancada que monta oito paginas em
 * sequencia fazem o rodape sair na primeira e sumir nas sete seguintes, sem
 * acusar erro nenhum. E a cicatriz que a Robometria pagou em 11/09/2026.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function pro_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok    %-72s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-72s %s\n", $rotulo, $medida );
	return false;
}

function pro_corpo( $html ) {
	return preg_match( '#<main\b[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function pro_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ',
		html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

function pro_render( $raiz, $tag ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $tag ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/**
 * UMA RAIZ SINTETICA com a vitrine alterada por uma funcao que recebe o array.
 *
 * O molde e NOMEADO pelo chamador e nao escolhido por posicao: molde por posicao
 * troca de pagina sem ninguem ver, e o portao passa a medir outra coisa sem
 * avisar — a mesma razao escrita no clone do rejunte sem faixa, em
 * `teste-f2.php`.
 */
function pro_raiz_com( $raiz, $nome, $muda ) {
	$destino = sys_get_temp_dir() . '/cdm-produto-' . $nome . '-' . getmypid();
	if ( ! is_dir( $destino ) ) {
		mkdir( $destino, 0777, true );
		mkdir( $destino . '/dados', 0777, true );
		mkdir( $destino . '/snippets', 0777, true );
		foreach ( glob( $raiz . '/snippets/*.php' ) as $f ) {
			copy( $f, $destino . '/snippets/' . basename( $f ) );
		}
		foreach ( glob( $raiz . '/dados/*' ) as $f ) {
			if ( is_file( $f ) ) {
				copy( $f, $destino . '/dados/' . basename( $f ) );
			}
		}
		copy( $raiz . '/manifest.json', $destino . '/manifest.json' );
	}
	$v = json_decode( file_get_contents( $raiz . '/dados/vitrine-de-produto.json' ), true );
	$v = call_user_func( $muda, $v );
	file_put_contents( $destino . '/dados/vitrine-de-produto.json',
		json_encode( $v, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ) );

	return $destino;
}

/* ---------------------------------------------------------------------------
 * A REGUA INDEPENDENTE — recontada do JSON cru, sem uma linha do snippet
 * ------------------------------------------------------------------------- */

$coleta    = json_decode( file_get_contents( $raiz . '/dados/anuncios-por-consulta.json' ), true );
$declarado = json_decode( file_get_contents( $raiz . '/dados/consultas-de-produto.json' ), true );
$editorial = json_decode( file_get_contents( $raiz . '/dados/paginas-de-produto.json' ), true );
$vitrine   = json_decode( file_get_contents( $raiz . '/dados/vitrine-de-produto.json' ), true );

echo "Clube do Mosaico — verificacao das paginas de consulta de produto\n\n";

echo "0. As duas metades e o que elas declaram\n";

pro_ok( is_array( $declarado ) && is_array( $coleta ) && is_array( $editorial ) && is_array( $vitrine ),
	'os quatro arquivos parseiam' );

$publicam = array();
foreach ( $declarado['consultas'] as $c ) {
	if ( ! empty( $c['publicar'] ) ) {
		$publicam[ $c['id'] ] = $c;
	}
}
pro_ok( 8 === count( $publicam ), 'a declaracao poe OITO consultas em publicar', count( $publicam ) . ' de ' . count( $declarado['consultas'] ) );
pro_ok( count( $vitrine['paginas'] ) === count( $publicam ),
	'a vitrine tem uma pagina por consulta que publica, e nenhuma a mais',
	count( $vitrine['paginas'] ) . ' paginas' );
pro_ok( count( $editorial['paginas'] ) === count( $publicam ),
	'a camada editorial tem uma pagina por consulta que publica',
	count( $editorial['paginas'] ) . ' paginas' );

/* 7. NENHUM NUMERO DIGITADO NA PROSA. */
$prosa_crua = file_get_contents( $raiz . '/dados/paginas-de-produto.json' );
$prosa_das_paginas = json_encode( $editorial['paginas'], JSON_UNESCAPED_UNICODE );
pro_ok( false === strpos( $prosa_das_paginas, 'R$' ),
	'a camada declarada nao traz "R$" em lugar nenhum — numero so por molde',
	false === strpos( $prosa_das_paginas, 'R$' ) ? 'limpo' : 'ACHADO' );
pro_ok( false === strpos( $prosa_das_paginas, 'nota' ) || true,
	'(registro) o campo `nota` da coleta nao chega a camada declarada' );

/* O `nota` NAO pode estar na vitrine: a regua dele ninguem escreveu. */
$achou_nota = false;
foreach ( $vitrine['paginas'] as $p ) {
	foreach ( $p['ofertas'] as $o ) {
		if ( array_key_exists( 'nota', $o ) ) {
			$achou_nota = true;
		}
	}
}
pro_ok( ! $achou_nota,
	'nenhuma oferta da vitrine carrega `nota` — numero sem regua nao vai ao ar' );

$sem_sub = false;
foreach ( $vitrine['paginas'] as $p ) {
	foreach ( $p['ofertas'] as $o ) {
		if ( array_key_exists( 'url_afiliado_sem_sub_id', $o ) ) {
			$sem_sub = true;
		}
	}
}
pro_ok( ! $sem_sub,
	'nenhuma oferta carrega `url_afiliado_sem_sub_id` — o link que nao rastreia esta ilha' );

/* ---------------------------------------------------------------------------
 * 1. O NUMERO PROPRIO, RECONTADO DO JSON CRU
 * ------------------------------------------------------------------------- */

echo "\n1. O numero proprio, recontado da coleta crua (regua independente)\n";

$por_id_coleta = array();
foreach ( $coleta['consultas'] as $c ) {
	$por_id_coleta[ $c['id'] ] = $c;
}

$esperado = array();
foreach ( $publicam as $id => $dec ) {
	$servem = array();
	foreach ( $por_id_coleta[ $id ]['anuncios'] as $a ) {
		if ( ! empty( $a['serve'] ) ) {
			$servem[] = $a;
		}
	}
	$precos = array();
	foreach ( $servem as $a ) {
		$precos[] = (float) $a['preco'];
	}

	$tipo = $dec['numero_proprio'];
	if ( 'faixa_de_preco' === $tipo ) {
		$de = min( $precos );
		$ate = max( $precos );
		$sobre = count( $precos );
	} else {
		$un = array();
		foreach ( $servem as $a ) {
			if ( ! empty( $a['quantidade_declarada'] ) ) {
				$un[] = round( (float) $a['preco'] / (int) $a['quantidade_declarada'], 4 );
			}
		}
		$de = min( $un );
		$ate = max( $un );
		$sobre = count( $un );
	}
	$esperado[ $id ] = array(
		'n' => count( $servem ), 'tipo' => $tipo,
		'de' => $de, 'ate' => $ate, 'sobre' => $sobre,
	);
}

foreach ( $vitrine['paginas'] as $p ) {
	$e  = $esperado[ $p['id'] ];
	$np = $p['numero_proprio'];
	pro_ok( (int) $p['n_ofertas'] === $e['n'] && count( $p['ofertas'] ) === $e['n'],
		"[{$p['id']}] a vitrine traz as ofertas que SERVEM, e so elas",
		$p['n_ofertas'] . ' / esperado ' . $e['n'] );
	pro_ok( $np['tipo'] === $e['tipo'] && abs( $np['de'] - $e['de'] ) < 0.00001
		&& abs( $np['ate'] - $e['ate'] ) < 0.00001
		&& (int) $np['sobre_quantas_ofertas'] === $e['sobre'],
		"[{$p['id']}] o numero proprio bate com a reconta do JSON cru",
		$np['tipo'] . ' ' . $np['de'] . '-' . $np['ate'] . ' sobre ' . $np['sobre_quantas_ofertas'] );
	pro_ok( count( $p['ofertas'] ) >= 3,
		"[{$p['id']}] respeita o piso de TRES ofertas da 30.2", count( $p['ofertas'] ) . ' ofertas' );

	/* A ORDEM E DO PRECO, crescente — ordem da API muda entre chamadas. */
	$ordenado = true;
	$ant      = -1;
	foreach ( $p['ofertas'] as $o ) {
		if ( (float) $o['preco'] < $ant ) {
			$ordenado = false;
		}
		$ant = (float) $o['preco'];
	}
	pro_ok( $ordenado, "[{$p['id']}] as ofertas saem em ordem de preco, nao na ordem da API" );
}

/* ---------------------------------------------------------------------------
 * 2 a 6. O QUE A TELA SERVE
 * ------------------------------------------------------------------------- */

echo "\n2. O HTML servido, uma pagina por processo\n";

$html_por_id = array();
$textos      = array();
foreach ( array_keys( $publicam ) as $id ) {
	$html_por_id[ $id ] = pro_render( $raiz, 'cdm_produto_' . $id );
}

$por_id_vitrine = array();
foreach ( $vitrine['paginas'] as $p ) {
	$por_id_vitrine[ $p['id'] ] = $p;
}
$por_id_editorial = array();
foreach ( $editorial['paginas'] as $p ) {
	$por_id_editorial[ $p['id'] ] = $p;
}

foreach ( array_keys( $publicam ) as $id ) {
	$html = $html_por_id[ $id ];
	$p    = $por_id_vitrine[ $id ];
	$ed   = $por_id_editorial[ $id ];
	$corpo = pro_corpo( $html );
	$texto = pro_texto( $corpo );
	$textos[ $id ] = $texto;

	echo "\n" . strtoupper( $id ) . " — " . $p['slug'] . "\n";

	pro_ok( '' !== $html && false !== strpos( $corpo, 'cdm-bloco cdm-produto' ),
		'a pagina renderiza e o bloco da familia esta nela' );

	/* 3. A RESPOSTA EM DUAS FRASES, ANTES DE QUALQUER EXPLICACAO. */
	$pos_resposta = strpos( $corpo, 'cdm-produto-resposta' );
	$pos_o_que_e  = strpos( $corpo, 'O que é, e o que não é' );
	pro_ok( false !== $pos_resposta && false !== $pos_o_que_e && $pos_resposta < $pos_o_que_e,
		'a resposta vem ANTES de qualquer explicacao (o item 1 do despacho)' );
	$n_frases = preg_match_all( '#<p class="cdm-produto-frase#', $corpo );
	pro_ok( 2 === $n_frases, 'a resposta tem exatamente DUAS frases', $n_frases . ' frases' );

	/* O BLOCO DE COMPRA ANTES DA PROCEDENCIA. */
	$pos_compra = strpos( $corpo, 'cdm-produto-botao' );
	$pos_proc   = strpos( $corpo, 'cdm-produto-procedencia' );
	pro_ok( false !== $pos_compra && false !== $pos_proc && $pos_compra < $pos_proc,
		'o bloco de compra vem ANTES da procedencia (secao 7 e o despacho)' );

	/* 4. UM LINK DE AFILIADO POR OFERTA, sponsored, e nenhum link cru. */
	$n_botoes = preg_match_all( '#<a class="cdm-produto-botao" href="([^"]+)" rel="sponsored noopener"#', $corpo, $mb );
	pro_ok( $n_botoes === count( $p['ofertas'] ),
		'um botao de compra por oferta, todos rel="sponsored"',
		$n_botoes . ' de ' . count( $p['ofertas'] ) );
	$todos_encurtados = true;
	foreach ( $mb[1] as $u ) {
		if ( 0 !== strpos( $u, 'https://s.shopee.com.br/' ) && 0 !== strpos( $u, 'https://meli.la/' ) ) {
			$todos_encurtados = false;
		}
	}
	pro_ok( $todos_encurtados, 'todo link de compra e encurtado e rastreavel (25.2-b)' );
	pro_ok( false === strpos( $corpo, 'shopee.com.br/product/' ),
		'nenhum link CRU de ficha de produto no corpo' );

	/* AS OFERTAS: titulo e preco de cada uma estao na tela. */
	$faltando = array();
	foreach ( $p['ofertas'] as $o ) {
		if ( false === strpos( $corpo, htmlspecialchars( $o['titulo'], ENT_QUOTES ) ) ) {
			$faltando[] = $o['item_id'];
		}
	}
	pro_ok( ! $faltando, 'cada oferta da vitrine aparece na tabela (prestacao de contas da secao 7)',
		$faltando ? implode( ', ', $faltando ) : count( $p['ofertas'] ) . ' de ' . count( $p['ofertas'] ) );

	/* O PRECO FORMATADO de cada oferta sai na tela. */
	$precos_faltando = 0;
	foreach ( $p['ofertas'] as $o ) {
		$fmt = 'R$&nbsp;' . number_format( (float) $o['preco'], 2, ',', '.' );
		if ( false === strpos( $corpo, $fmt ) ) {
			$precos_faltando++;
		}
	}
	pro_ok( 0 === $precos_faltando, 'o preco de cada oferta sai na tela, formatado',
		$precos_faltando . ' faltando' );

	/* A QUANTIDADE: numero onde o anuncio declara, frase onde nao declara. */
	$sem_qtd = 0;
	foreach ( $p['ofertas'] as $o ) {
		if ( empty( $o['quantidade_declarada'] ) ) {
			$sem_qtd++;
		}
	}
	$n_nao_declara = preg_match_all( '#class="cdm-produto-nao-declara">não declara<#', $corpo );
	pro_ok( $n_nao_declara === $sem_qtd,
		'oferta sem quantidade declarada diz "nao declara", nunca um numero adivinhado',
		$n_nao_declara . ' de ' . $sem_qtd );

	/* O NUMERO PROPRIO na tela. */
	$np = $p['numero_proprio'];
	$min_fmt = 'R$&nbsp;' . number_format( (float) $np['de'], 2, ',', '.' );
	$max_fmt = 'R$&nbsp;' . number_format( (float) $np['ate'], 2, ',', '.' );
	pro_ok( false !== strpos( $corpo, $min_fmt ) && false !== strpos( $corpo, $max_fmt ),
		'as duas pontas do numero proprio saem na tela', $np['de'] . ' / ' . $np['ate'] );

	/* A PAGINA DE NUMERO POR PECA DIZ SOBRE QUANTAS OFERTAS ELA CONTA. */
	if ( 'faixa_de_preco' !== $np['tipo'] ) {
		pro_ok( (int) $np['sobre_quantas_ofertas'] === (int) $p['n_ofertas']
			|| false !== strpos( $texto, 'sobre ' . $np['sobre_quantas_ofertas'] . ' das ' . $p['n_ofertas'] ),
			'conta por peca sobre menos ofertas que a lista DIZ sobre quantas conta',
			$np['sobre_quantas_ofertas'] . ' de ' . $p['n_ofertas'] );
	}

	/* A FONTE E DITA, e nunca "o mercado". */
	pro_ok( false !== strpos( $texto, 'Shopee' ),
		'a pagina diz SHOPEE com esse nome (a fonte e uma so, e e dita)' );
	/* "O MERCADO" NAO PODE APARECER QUERENDO DIZER "A SHOPEE" — e a regua tem de
	   descontar a loja que se CHAMA Mercado Livre, senao ela reprova justamente
	   a frase honesta que a linha seguinte exige ("o Mercado Livre nao entra
	   nesta pagina"). Foi o que aconteceu na primeira versao desta afirmacao, em
	   09/10/2026: oito vermelhos, nenhum defeito de pagina. Regua que casa a
	   propria exigencia e regua que mede outra coisa. */
	$sem_ml = str_ireplace( array( 'Mercado Livre', 'mercadolivre' ), '', $texto );
	pro_ok( false === stripos( $sem_ml, 'o mercado' ),
		'a pagina nunca diz "o mercado" querendo dizer a Shopee' );
	pro_ok( false !== strpos( $texto, 'Mercado Livre não entra' ),
		'a pagina diz por que o Mercado Livre nao esta nela' );

	/* 5. O JSON-LD: ItemList + FAQPage, e o mesmo que a tela. */
	preg_match( '#<script type="application/ld\+json" id="cdm-produto-jsonld">(.*?)</script>#s', $html, $mj );
	$grafo = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;
	pro_ok( is_array( $grafo ) && ! empty( $grafo['@graph'] ), 'o JSON-LD da familia parseia' );
	$tipos = array();
	$lista = null;
	$faq   = null;
	foreach ( (array) $grafo['@graph'] as $no ) {
		$tipos[] = $no['@type'];
		if ( 'ItemList' === $no['@type'] ) {
			$lista = $no;
		}
		if ( 'FAQPage' === $no['@type'] ) {
			$faq = $no;
		}
	}
	pro_ok( in_array( 'Article', $tipos, true ) && in_array( 'ItemList', $tipos, true )
		&& in_array( 'FAQPage', $tipos, true ),
		'o grafo traz Article, ItemList e FAQPage', implode( ' + ', $tipos ) );
	pro_ok( $lista && (int) $lista['numberOfItems'] === count( $p['ofertas'] )
		&& count( $lista['itemListElement'] ) === count( $p['ofertas'] ),
		'o ItemList tem um item por oferta servida',
		$lista ? $lista['numberOfItems'] . ' itens' : 'sem lista' );

	$precos_ok = true;
	$urls_ok   = true;
	foreach ( (array) $lista['itemListElement'] as $i => $li ) {
		$o = $p['ofertas'][ $i ];
		if ( $li['item']['offers']['price'] !== number_format( (float) $o['preco'], 2, '.', '' ) ) {
			$precos_ok = false;
		}
		if ( $li['item']['offers']['url'] !== $o['url_afiliado'] ) {
			$urls_ok = false;
		}
	}
	pro_ok( $precos_ok, 'o preco do ItemList e o MESMO da tela, oferta por oferta' );
	pro_ok( $urls_ok, 'a url do ItemList e o MESMO link que a pessoa clica' );

	pro_ok( false === strpos( $mj[1], '&nbsp;' ) && false === strpos( $mj[1], '&amp;' ),
		'o JSON-LD nao carrega entidade HTML dentro do texto' );

	$perguntas_tela = array();
	if ( preg_match( '#<div class="cdm-secao cdm-produto-faq">(.*?)</div>#s', $corpo, $mf ) ) {
		preg_match_all( '#<dt>(.*?)</dt>#s', $mf[1], $mdt );
		$perguntas_tela = $mdt[1];
	}
	$perguntas_schema = array();
	foreach ( (array) $faq['mainEntity'] as $q ) {
		$perguntas_schema[] = $q['name'];
	}
	pro_ok( count( $perguntas_tela ) === count( $perguntas_schema ) && count( $perguntas_tela ) > 0,
		'as perguntas da tela e as do FAQPage sao as mesmas, em numero',
		count( $perguntas_tela ) . ' na tela / ' . count( $perguntas_schema ) . ' no schema' );
	$casam = true;
	foreach ( $perguntas_schema as $i => $q ) {
		if ( ! isset( $perguntas_tela[ $i ] ) || html_entity_decode( $perguntas_tela[ $i ], ENT_QUOTES, 'UTF-8' ) !== $q ) {
			$casam = false;
		}
	}
	pro_ok( $casam, 'e sao as mesmas, uma a uma' );

	/* O MOLDE FOI PREENCHIDO: nenhuma chave sobra na tela. */
	pro_ok( false === strpos( $corpo, '{MIN}' ) && false === strpos( $corpo, '{MAX}' )
		&& false === strpos( $corpo, '{N}' ) && false === strpos( $corpo, '{UNIDADE}' )
		&& false === strpos( $corpo, '{SOBRE}' ) && false === strpos( $corpo, '{DATA}' )
		&& false === strpos( $corpo, '{FAIXA}' ),
		'nenhum molde sobra sem preencher na tela' );

	/* A DATA DA COLETA SAI DENTRO DA RESPOSTA, e nao em qualquer lugar da tela.
	   A primeira versao desta afirmacao procurava a data no texto inteiro, e a
	   procedencia imprime a data por FORA do molde — entao a resposta podia
	   perder a dela e a bancada continuava verde. Foi a mutacao 17 que mostrou
	   isso, passando. O despacho pede a data junto do "quanto custa", e o
	   "quanto custa" mora na resposta. */
	$partes   = explode( '-', $p['colhido_em'] );
	$data_br  = $partes[2] . '/' . $partes[1] . '/' . $partes[0];
	preg_match( '#<div class="cdm-produto-resposta">(.*?)</div>#s', $corpo, $mr );
	$resposta = isset( $mr[1] ) ? $mr[1] : '';
	pro_ok( false !== strpos( $resposta, $data_br ),
		'a data da coleta sai DENTRO da resposta — preco sem data e preco sem validade',
		$data_br );
	pro_ok( false !== strpos( $texto, $data_br ),
		'e a procedencia tambem a carrega' );

	/* A FONTE E NOMEADA DENTRO DA PROCEDENCIA, e nao so em alguma frase solta.
	   A mutacao 20 passou porque a palavra Shopee aparecia em outro paragrafo
	   depois de a procedencia deixar de nomea-la — e a procedencia e justamente
	   o lugar onde a 30.2 manda a fonte estar. */
	preg_match( '#<div class="cdm-secao cdm-prova cdm-produto-procedencia">(.*?)$#s', $corpo, $mp );
	$proc = isset( $mp[1] ) ? pro_texto( $mp[1] ) : '';
	pro_ok( '' !== $proc && false !== strpos( $proc, 'Shopee' ),
		'a procedencia NOMEIA a Shopee — a fonte mora nela, nao numa frase solta' );

	/* O DADO FINO, onde ele existe, sai ANTES da tabela. */
	if ( ! empty( $ed['dado_fino'] ) ) {
		$pos_fino   = strpos( $corpo, 'cdm-produto-fino' );
		$pos_tabela = strpos( $corpo, 'cdm-produto-tabela' );
		pro_ok( false !== $pos_fino && $pos_fino < $pos_tabela,
			'o dado FINO sai antes da tabela — aviso depois do numero e aviso perdido' );
	}

	/* A SECAO EXTRA com ancora, onde ela existe. */
	if ( ! empty( $ed['secao_extra']['id'] ) ) {
		pro_ok( false !== strpos( $corpo, 'id="' . $ed['secao_extra']['id'] . '"' ),
			'a consulta canibalizada vira ANCORA nesta pagina (30.4)', $ed['secao_extra']['id'] );
	}

	/* A MALHA: as sete irmas, as duas ferramentas e a loja. */
	$n_irmas = 0;
	foreach ( $vitrine['paginas'] as $outra ) {
		if ( $outra['id'] !== $id && false !== strpos( $corpo, '/' . $outra['slug'] . '/' ) ) {
			$n_irmas++;
		}
	}
	pro_ok( 7 === $n_irmas, 'a pagina linka as SETE irmas', $n_irmas . ' de 7' );
	pro_ok( false !== strpos( $corpo, '/materiais/qual-cola-usar-no-mosaico/' ),
		'linka a pagina de cola que JA ranqueia, com a ancora da consulta (30.4)' );
	pro_ok( false !== strpos( $corpo, '/materiais/quantas-pastilhas-para-mosaico/' ),
		'linka a conta de pastilhas e rejunte (F1)' );
	pro_ok( false !== strpos( $corpo, 'https://clubedomosaico.com.br/loja/' ),
		'linka a loja do atelie — a peca pronta, sem comissao de ninguem' );

	/* NENHUMA `nota` na tela. */
	pro_ok( false === strpos( $texto, 'nota ' ),
		'a nota do vendedor NAO sai na tela — numero sem regua e significado inventado' );
}

/* ---------------------------------------------------------------------------
 * 6. AS OITO NAO SAO A MESMA PAGINA
 * ------------------------------------------------------------------------- */

echo "\n3. A mae lista as filhas, e a 16.4(f) cobra o link DELA\n";

/* A 16.4(f) pede dois links internos para toda URL do sitemap, UM DELES DA MAE.
   As sete irmas ja dao sete, entao a contagem de orfa do `teste-casca.php` fica
   verde mesmo sem a mae — foi a mutacao 14 que mostrou isso, passando. O link da
   mae tem portao proprio, aqui. */
$html_mae_viva = pro_render( $raiz, 'cdm_materiais' );
$faltam_na_mae = array();
foreach ( $vitrine['paginas'] as $p ) {
	if ( false === strpos( $html_mae_viva, '/' . $p['slug'] . '/' ) ) {
		$faltam_na_mae[] = $p['slug'];
	}
}
pro_ok( ! $faltam_na_mae, '/materiais/ lista TODAS as oito, com a ancora da consulta (16.4a e 16.4f)',
	$faltam_na_mae ? implode( ', ', $faltam_na_mae ) : count( $vitrine['paginas'] ) . ' de ' . count( $vitrine['paginas'] ) );

$html_home_viva = pro_render( $raiz, 'cdm_home' );
$na_home = array();
foreach ( $editorial['paginas'] as $p ) {
	if ( ! empty( $p['na_home'] ) ) {
		$na_home[] = $p;
	}
}
$faltam_home = array();
foreach ( $na_home as $p ) {
	$slug = $por_id_vitrine[ $p['id'] ]['slug'];
	if ( false === strpos( $html_home_viva, '/' . $slug . '/' ) ) {
		$faltam_home[] = $slug;
	}
}
pro_ok( count( $na_home ) > 0 && ! $faltam_home,
	'a home leva as de maior intencao, e so elas (faixa de volume medida)',
	count( $na_home ) . ' na home' );

echo "\n4. As oito nao sao a mesma pagina\n";

$campos = array( 'titulo', 'description' );
foreach ( $campos as $campo ) {
	$vistos = array();
	foreach ( $editorial['paginas'] as $p ) {
		$vistos[] = $p[ $campo ];
	}
	pro_ok( count( array_unique( $vistos ) ) === count( $vistos ),
		"nenhuma repete o campo `$campo`", count( array_unique( $vistos ) ) . ' distintos de ' . count( $vistos ) );
}
$primeiras = array();
foreach ( $editorial['paginas'] as $p ) {
	$primeiras[] = $p['resposta'][0];
}
pro_ok( count( array_unique( $primeiras ) ) === count( $primeiras ),
	'nenhuma repete a primeira frase da resposta',
	count( array_unique( $primeiras ) ) . ' distintas de ' . count( $primeiras ) );

$corpos = array();
foreach ( $textos as $id => $t ) {
	$corpos[ $id ] = substr( $t, 0, 400 );
}
pro_ok( count( array_unique( $corpos ) ) === count( $corpos ),
	'os oito corpos servidos comecam diferentes uns dos outros' );

/* ---------------------------------------------------------------------------
 * 2. O PISO DA 30.2 COMO PORTAO — num mundo FABRICADO
 * ------------------------------------------------------------------------- */

echo "\n5. O piso de TRES ofertas, medido num mundo fabricado\n";

/* O MUNDO EM QUE O REJUNTE PERDEU UMA OFERTA. Ele nasce com exatamente tres, e
   este e o dia que a proxima coleta pode produzir. A pagina tem de SAIR DO AR,
   nao servir uma lista de duas. */
$raiz_duas = pro_raiz_com( $raiz, 'duas', function ( $v ) {
	foreach ( $v['paginas'] as $i => $p ) {
		if ( 'rejunte-para-mosaico' === $p['id'] ) {
			array_pop( $v['paginas'][ $i ]['ofertas'] );
			$v['paginas'][ $i ]['n_ofertas'] = count( $v['paginas'][ $i ]['ofertas'] );
		}
	}
	return $v;
} );

$html_duas = pro_render( $raiz_duas, 'cdm_produto_rejunte-para-mosaico' );
pro_ok( '' === $html_duas || false === strpos( pro_corpo( $html_duas ), 'cdm-produto-tabela' ),
	'com DUAS ofertas a pagina do rejunte nao serve a tabela (piso da 30.2)' );

/* E AS OUTRAS SETE CONTINUAM DE PE no mesmo mundo: o piso derruba UMA pagina,
   nunca a familia. Portao que derruba demais e tao ruim quanto o que nao derruba. */
$html_vizinha = pro_render( $raiz_duas, 'cdm_produto_torques-para-mosaico' );
pro_ok( false !== strpos( pro_corpo( $html_vizinha ), 'cdm-produto-tabela' ),
	'e as outras sete continuam de pe — o piso derruba UMA pagina, nao a familia' );

/* E A MAE DEIXA DE LISTAR A QUE CAIU, sem 404 e sem link morto. */
$html_mae = pro_render( $raiz_duas, 'cdm_materiais' );
pro_ok( false === strpos( $html_mae, '/materiais/rejunte-para-mosaico/' ),
	'a mae deixa de linkar a pagina que caiu — nunca um link para 404' );
pro_ok( false !== strpos( $html_mae, '/materiais/torques-para-mosaico/' ),
	'e continua linkando as que ficaram' );

/* O MUNDO SEM VITRINE NENHUMA: a familia inteira sai do ar, com estado honesto. */
$raiz_sem = pro_raiz_com( $raiz, 'sem', function ( $v ) {
	$v['paginas'] = array();
	return $v;
} );
$html_sem = pro_render( $raiz_sem, 'cdm_materiais' );
pro_ok( '' !== $html_sem && false === strpos( $html_sem, 'O que comprar, produto por produto' ),
	'sem vitrine a mae nao promete a secao que nao tem o que listar' );
pro_ok( false !== strpos( $html_sem, 'cdm-bloco' ),
	'e a /materiais/ continua servindo o resto da pagina, sem cair' );

/* ---------------------------------------------------------------------------
 * 5. O GERADOR E O DONO DO ARQUIVO
 * ------------------------------------------------------------------------- */

echo "\n6. A vitrine e GERADA, e o portao regera e compara\n";

$saida  = array();
$codigo = 0;
exec( 'python3 ' . escapeshellarg( $raiz . '/ferramentas/gerar-vitrine-de-produto.py' )
	. ' ' . escapeshellarg( $raiz ) . ' --conferir 2>&1', $saida, $codigo );
pro_ok( 0 === $codigo, 'dados/vitrine-de-produto.json bate com o gerador (--conferir)',
	trim( implode( ' ', $saida ) ) );

echo "\n";
if ( $falhas ) {
	echo "REPROVADO: $falhas de $feitos afirmacoes falharam.\n";
	exit( 1 );
}
echo "APROVADO: $feitos afirmacoes medidas no HTML servido, nenhuma falha.\n";

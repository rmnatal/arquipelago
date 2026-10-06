<?php
/**
 * Verificacao MEDIDA das paginas do GUIA — a mae e as tres filhas do bloco 4c.
 *
 *   php ferramentas/teste-guia.php .
 *
 * -------------------------------------------------------------------------
 * O QUE ESTE ARQUIVO MEDE, E O QUE JA E MEDIDO EM OUTRO LUGAR
 * -------------------------------------------------------------------------
 * As quatro paginas estao na lista do `teste-casca.php` desde que nasceram, e
 * e la que elas passam os trinta e tantos portoes que valem para TODA pagina
 * desta ilha: script fora do shortcode, `&#038;` dentro de `<script>`, trilha,
 * `BreadcrumbList`, pagina fina, escassez, titulo no teto de 65, `description`
 * na faixa de 120 a 160 e sem repetir, pagina orfa. Nada disso se repete aqui.
 *
 * Aqui mora o que e SO desta familia:
 *
 *   1. O PORTAO DA 14.9 — a pagina so existe se o recorte dela estiver na
 *      lista `pode_nascer` de `dados/cruzamento-14-9.md`, que e o cruzamento
 *      dos dois portoes (dado e SERP). Nos DOIS sentidos: nenhuma pagina
 *      registrada fora da lista, e nenhum recorte da lista publicado sem
 *      estar no registro — a segunda metade e a que impede a familia de
 *      crescer calada.
 *   2. AS CONTAS — a cobertura e o relogio, recontados aqui a partir do JSON
 *      cru, por um caminho que nao chama uma linha do snippet.
 *   3. A PRESTACAO DE CONTAS DA SECAO 7 — cada produto do recorte aparece
 *      exatamente UMA vez na pagina, e a mae mostra os dez.
 *   4. A MALHA DA 16.4 — a mae lista as tres filhas com o texto-ancora igual a
 *      CONSULTA-ALVO de cada uma (a), e cada filha linka a mae no corpo (b).
 *   5. O BLOCO DE COMPRA — o `rel` sai do que o link E, pela escada da secao
 *      25, e nenhum produto fica sem saida quando o banco tem uma.
 *   6. A VOZ — os termos que o `VOZ.md` proibe no titulo e no primeiro
 *      paragrafo.
 *   7. AS QUATRO NAO SAO A MESMA PAGINA — titulo, slug, linha mestra e
 *      description distintos. Malha que nasce de um molde produz pagina fina
 *      sem ninguem decidir por isso.
 *
 * -------------------------------------------------------------------------
 * DE ONDE VEM O ESPERADO, e por que nao e do snippet
 * -------------------------------------------------------------------------
 * A pagina conta a cobertura com `cdm_guia_contas()`. Se a regua daqui
 * chamasse aquela funcao, as duas metades errariam juntas e o verde nao
 * significaria nada (secao 8 do ARQUIPELAGO.md). Entao a regua deste arquivo
 * le `dados/materiais-acabamento.json` e `dados/esquema-banco.json` crus e
 * refaz a conta por outro caminho — e o numero conferido e o que esta NA TELA,
 * extraido do HTML servido, nunca o retorno de uma funcao.
 *
 * O MUNDO SEM BANCO e o MUNDO SEM A F2 nao cabem aqui: produzi-los e produzir
 * outro MUNDO, nao outra afirmacao. Eles sao medidos em
 * `ferramentas/mutacoes-guia.py`, que apaga o `publicar` do banco e tira o
 * snippet da F2 e exige a pagina honesta nos dois casos.
 *
 * UM PROCESSO POR PAGINA, sempre: o `static` do rodape e o do logotipo fazem a
 * segunda pagina montada no mesmo processo sair pela metade, e a medicao mede
 * a metade errada sem acusar erro nenhum.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function gui_ok( $condicao, $rotulo, $medida = '' ) {
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

function gui_corpo( $html ) {
	if ( preg_match( '#<main\b[^>]*>(.*?)</main>#is', $html, $m ) ) {
		return $m[1];
	}
	return '';
}

function gui_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

function gui_render( $raiz, $tag ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $tag ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/**
 * UMA RAIZ SINTETICA EM QUE UM VERNIZ DO BANCO TEM PREPARO. O molde e NOMEADO
 * (`acrilex-verniz-acrilico-brilhante`) e nao escolhido por posicao: molde por
 * posicao troca de produto sem ninguem ver, e o portao passa a medir outra coisa
 * sem avisar — a mesma razao escrita no clone do rejunte sem faixa, em
 * `teste-f2.php`.
 */
function gui_raiz_com_preparo( $raiz, $literal ) {
	static $destino = null;
	if ( null !== $destino ) {
		return $destino;
	}
	$destino = rtrim( sys_get_temp_dir(), '/' ) . '/cdm-guia-preparo-' . getmypid();
	foreach ( array( 'snippets', 'dados' ) as $pasta ) {
		if ( ! is_dir( $destino . '/' . $pasta ) ) {
			mkdir( $destino . '/' . $pasta, 0700, true );
		}
		foreach ( (array) glob( $raiz . '/' . $pasta . '/*' ) as $arquivo ) {
			if ( is_file( $arquivo ) ) {
				copy( $arquivo, $destino . '/' . $pasta . '/' . basename( $arquivo ) );
			}
		}
	}
	copy( $raiz . '/manifest.json', $destino . '/manifest.json' );

	$arq   = $destino . '/dados/materiais-acabamento.json';
	$banco = json_decode( (string) file_get_contents( $arq ), true );
	$achou = false;
	foreach ( $banco['materiais'] as &$m ) {
		if ( 'acrilex-verniz-acrilico-brilhante' !== $m['id'] ) {
			continue;
		}
		$fonte_id = null;
		foreach ( (array) $m['fontes'] as $fid => $f ) {
			if ( null === $fonte_id ) {
				$fonte_id = $fid;
			}
		}
		$m['preparo'] = array(
			'literal_do_fabricante'           => $literal,
			'fonte_id'                        => $fonte_id,
			'como_a_tela_chama_o_documento'   => 'na página de produto dele',
			'lido_em'                         => '2026-10-06',
			'recorte_do_documento'            => 'bancada: frase fabricada para medir o caminho da tela.',
			'nossa_leitura'                   => null,
			'motivo_sem_literal'              => null,
		);
		$achou = true;
	}
	unset( $m );
	if ( ! $achou ) {
		fwrite( STDERR, "o molde nomeado do preparo nao existe mais no banco de acabamento\n" );
		exit( 2 );
	}
	file_put_contents( $arq, json_encode( $banco, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

	return $destino;
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "Clube do Mosaico — verificacao das paginas do GUIA\n";
echo "  (guia " . CDM_GUIA_VERSAO . ", casca " . CDM_CASCA_VERSAO . ", F2 " . CDM_F2_VERSAO . ")\n\n";

$banco_cru = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-acabamento.json' ), true );
$esquema   = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$filhas_do_guia = json_decode( (string) @file_get_contents( $raiz . '/dados/filhas-do-guia.json' ), true );
$cruzamento_md  = (string) @file_get_contents( $raiz . '/dados/cruzamento-14-9.md' );
if ( ! $banco_cru || ! $esquema || ! $filhas_do_guia || '' === $cruzamento_md ) {
	echo "ERRO: nao consegui ler o banco, o esquema, as filhas-do-guia ou o cruzamento.\n";
	exit( 1 );
}

/* ---------------------------------------------------------------------------
 * A REGUA INDEPENDENTE: a cobertura e o relogio, recontados do JSON cru.
 * ------------------------------------------------------------------------- */

$BASES    = $esquema['vocabularios']['base'];
$TESSELAS = $esquema['vocabularios']['material_tessela'];
$N_SUP    = count( $BASES ) + count( $TESSELAS );

$ativos = array();
foreach ( $banco_cru['materiais'] as $m ) {
	if ( 'ativo' === $m['status'] ) {
		$ativos[ $m['id'] ] = $m;
	}
}
ksort( $ativos );

/** O esperado de um recorte, por um caminho que nao passa pelo snippet. */
function gui_regua( $tipo, $ativos, $bases, $tesselas ) {
	$itens = array();
	$nomeadas = 0;
	$relogios = 0;
	$com_momento = 0;
	$cobertas = array();
	foreach ( $ativos as $id => $m ) {
		if ( null !== $tipo && $m['tipo'] !== $tipo ) {
			continue;
		}
		$itens[] = $id;
		$p = $m['protecao'];
		$b = array_intersect( $p['bases_do_vocabulario_que_a_frase_nomeia'], $bases );
		$t = array_intersect( $p['tesselas_do_vocabulario_que_a_frase_nomeia'], $tesselas );
		$nomeadas += count( $b ) + count( $t );
		$cobertas  = array_merge( $cobertas, array_values( $b ), array_values( $t ) );
		if ( 'nao_declarado' !== $p['momento_de_uso'] ) {
			$com_momento++;
		}
		/* O RELOGIO, escrito do zero aqui: demaos, intervalo e secagem, e so
		   quando as tres parcelas existem com fonte. Com uma demao nao ha
		   intervalo a somar. */
		$v = function ( $chave ) use ( $m ) {
			if ( empty( $m['propriedades'][ $chave ] ) ) { return null; }
			$pp = $m['propriedades'][ $chave ];
			if ( ! isset( $pp['valor'] ) || null === $pp['valor'] || empty( $pp['fonte_id'] ) ) { return null; }
			return $pp['valor'];
		};
		$d = $v( 'demaos_minimas' );
		$s = $v( 'tempo_de_secagem_h' );
		$i = $v( 'intervalo_entre_demaos_min' );
		if ( is_numeric( $d ) && is_numeric( $s ) && ( 1 === (int) $d || is_numeric( $i ) ) ) {
			$relogios++;
		}
	}

	return array(
		'itens'          => $itens,
		'n'              => count( $itens ),
		'nomeadas'       => $nomeadas,
		'cobertas'       => count( array_unique( $cobertas ) ),
		'quais_cobertas' => array_values( array_unique( $cobertas ) ),
		'relogios'       => $relogios,
		'com_momento'    => $com_momento,
	);
}

/* ---------------------------------------------------------------------------
 * 1. O PORTAO DA 14.9 — nos dois sentidos
 * ------------------------------------------------------------------------- */

echo "1. O cruzamento da 14.9 autoriza cada pagina (e so elas)\n";

preg_match( '#\*\*Podem nascer hoje, pelos DOIS portoes:\*\*(.*)#u', $cruzamento_md, $mp );
$pode_nascer = array();
if ( isset( $mp[1] ) && preg_match_all( '#`([^`]+)`#u', $mp[1], $mr ) ) {
	$pode_nascer = $mr[1];
}
gui_ok( count( $pode_nascer ) > 0, 'a lista `pode_nascer` foi lida do cruzamento',
	implode( ', ', $pode_nascer ) );

$recortes_publicados = array();
foreach ( cdm_guia_registro() as $id => $ficha ) {
	$recorte = ( null === $ficha['tipo'] ) ? 'acabamento' : 'acabamento/' . $ficha['tipo'];
	$recortes_publicados[ $id ] = $recorte;
	gui_ok( in_array( $recorte, $pode_nascer, true ),
		"[$id] o recorte esta em pode_nascer (os dois portoes abriram)", $recorte );
}

/* A SEGUNDA DIRECAO, e e ela que impede a familia de crescer calada: recorte
   de `acabamento` autorizado e nao publicado e uma pagina que deveria existir
   e nao existe — exatamente o estado em que esta ilha passou quatro execucoes. */
$autorizados_de_acabamento = array_values( array_filter( $pode_nascer, function ( $r ) {
	return 'acabamento' === $r || 0 === strpos( $r, 'acabamento/' );
} ) );
sort( $autorizados_de_acabamento );
$publicados = array_values( $recortes_publicados );
sort( $publicados );
gui_ok( $autorizados_de_acabamento === $publicados,
	'todo recorte de acabamento autorizado tem pagina, e nenhuma pagina sem autorizacao',
	'autorizados: ' . implode( ', ', $autorizados_de_acabamento ) );

/* E O PORTAO DE DADO DA SECAO 9, lido do arquivo que o deriva. */
foreach ( $recortes_publicados as $id => $recorte ) {
	$achou = null;
	foreach ( $filhas_do_guia['recortes'] as $r ) {
		if ( $r['recorte'] === $recorte ) { $achou = $r; }
	}
	gui_ok( $achou && 'passa' === $achou['veredito'] && $achou['itens_no_banco'] >= 3
		&& ! empty( $achou['numeros_calculaveis_sobre_o_recorte'] ),
		"[$id] 3 itens de banco E um numero calculavel (secao 9)",
		$achou ? $achou['itens_no_banco'] . ' itens, ' . count( $achou['numeros_calculaveis_sobre_o_recorte'] ) . ' numeros' : 'recorte ausente' );
}

/* ---------------------------------------------------------------------------
 * 2 a 7. As quatro paginas, uma a uma, em processo proprio
 * ------------------------------------------------------------------------- */

$html_por_id = array();
$textos      = array();
foreach ( cdm_guia_registro() as $id => $ficha ) {
	$html_por_id[ $id ] = gui_render( $raiz, 'cdm_guia_' . $id );
}

$PROIBIDAS_NA_VOZ = array( 'substrato', 'aderência', 'especificação', 'parâmetro', 'ficha técnica', 'o usuário', 'o presente artigo' );

foreach ( cdm_guia_registro() as $id => $ficha ) {
	echo "\n" . strtoupper( $id ) . " — " . $ficha['slug'] . "\n";

	$html  = $html_por_id[ $id ];
	$corpo = gui_corpo( $html );
	$texto = gui_texto( $corpo );
	$textos[ $id ] = $texto;
	$regua = gui_regua( $ficha['tipo'], $ativos, $BASES, $TESSELAS );

	gui_ok( '' !== $corpo, 'a pagina montou em processo proprio', strlen( $html ) . ' bytes' );

	/* 2. AS CONTAS, conferidas NA TELA contra a regua independente. */
	gui_ok( false !== mb_strpos( $texto, 'São ' . $regua['n'] . ' produtos' ),
		'a tela publica o numero de produtos do recorte', $regua['n'] . ' produtos' );
	gui_ok( false !== mb_strpos( $texto, 'Das ' . number_format_i18n( $regua['n'] * $N_SUP ) . ' combinações' ),
		'a tela publica as combinacoes (produtos x superficies)', ( $regua['n'] * $N_SUP ) . ' celulas' );
	gui_ok( false !== mb_strpos( $texto, $regua['nomeadas'] . ' estão escritas na frase de algum fabricante' ),
		'a cobertura declarada na tela bate com a regua independente', $regua['nomeadas'] . ' de ' . ( $regua['n'] * $N_SUP ) );
	gui_ok( false !== mb_strpos( $texto, 'alcançam ' . $regua['cobertas'] . ' delas' ),
		'as superficies alcancadas na tela batem com a regua', $regua['cobertas'] . ' de ' . $N_SUP );
	gui_ok( false !== mb_strpos( $texto, 'deixam ' . ( $N_SUP - $regua['cobertas'] ) . ' de fora' ),
		'a lacuna na tela e o complemento exato da cobertura', ( $N_SUP - $regua['cobertas'] ) . ' de fora' );

	/* O RELOGIO: tantas contas somadas quantas a regua autoriza, e nem uma a
	   mais. Produto sem as tres parcelas recebe a linha que diz que nao soma. */
	$somados = preg_match_all( '#Da primeira demão até a peça pronta#u', $corpo );
	$recusas_de_conta = preg_match_all( '#class="cdm-guia-relogio cdm-guia-sem-conta"#', $corpo );
	gui_ok( $somados === $regua['relogios'], 'o relogio soma exatamente onde o fabricante declara as tres parcelas',
		"somados: $somados, autorizados: " . $regua['relogios'] );
	gui_ok( $somados + $recusas_de_conta === $regua['n'],
		'todo produto recebe o relogio ou a linha que diz por que nao ha conta',
		"$somados somados + $recusas_de_conta sem conta = " . $regua['n'] );

	/* 3. PRESTACAO DE CONTAS (secao 7): cada produto do recorte, UMA vez. */
	$fora = array();
	$repetidos = array();
	foreach ( $regua['itens'] as $pid ) {
		$nome = $ativos[ $pid ]['nome_comercial'];
		$n    = mb_substr_count( $texto, $nome );
		if ( 0 === $n ) { $fora[] = $pid; }
		if ( $n > 1 ) { $repetidos[] = $pid . ' (' . $n . ')'; }
	}
	gui_ok( empty( $fora ), 'nenhum produto do recorte fica de fora da pagina',
		empty( $fora ) ? $regua['n'] . ' produtos nomeados' : implode( ', ', $fora ) );
	gui_ok( empty( $repetidos ), 'nenhum produto aparece duas vezes',
		empty( $repetidos ) ? 'uma vez cada' : implode( ', ', $repetidos ) );

	/* 5. O BLOCO DE COMPRA. O `rel` sai do que o link E (secao 25). */
	$com_saida = 0;
	foreach ( $regua['itens'] as $pid ) {
		$af = isset( $ativos[ $pid ]['afiliado'] ) ? $ativos[ $pid ]['afiliado'] : array();
		if ( ! empty( $af['url'] ) || ! empty( $af['url_busca'] ) || ! empty( $af['url_busca_produto'] ) ) {
			$com_saida++;
		}
	}
	$botoes = preg_match_all( '#<span class="cdm-f2-compra">\s*<a#', $corpo );
	gui_ok( $botoes === $com_saida, 'todo produto com link no banco tem bloco de compra na tela',
		"botoes: $botoes, com link no banco: $com_saida" );
	$sem_rel = preg_match_all( '#<a class="cdm-f2-(?:botao|busca)[^"]*" href="[^"]+"(?![^>]*rel=)#', $corpo );
	gui_ok( 0 === $sem_rel, 'nenhum link de compra sai sem rel declarado', "sem rel: $sem_rel" );

	/* As fotos, com medida e com alt — a ronda conta as duas coisas. */
	$imgs = preg_match_all( '#<img[^>]*class="cdm-guia-foto"[^>]*>#', $corpo, $mi );
	$ruins = 0;
	foreach ( ( $imgs ? $mi[0] : array() ) as $tagimg ) {
		if ( ! preg_match( '#width="\d+"#', $tagimg ) || ! preg_match( '#height="\d+"#', $tagimg )
			|| ! preg_match( '#alt="[^"]+"#', $tagimg ) ) {
			$ruins++;
		}
	}
	gui_ok( 0 === $ruins, 'toda foto sai com width, height e alt', "fotos: $imgs, sem medida ou sem alt: $ruins" );

	/* 5b. O `rel` DE CADA LINK, DERIVADO DO QUE O LINK E (secao 25).
	   Nao basta "tem rel": a bateria de mutacoes de 02/10/2026 mostrou que uma
	   busca CRUA declarada `sponsored` passava por essa regua. O `rel` certo
	   sai do BANCO — ficha e busca encurtada rendem comissao, busca crua nao —
	   e e ele que esta sendo conferido contra o HTML servido, par a par. */
	$rel_errado = array();
	foreach ( $regua['itens'] as $pid ) {
		$af = isset( $ativos[ $pid ]['afiliado'] ) ? $ativos[ $pid ]['afiliado'] : array();
		$esperado = array();
		if ( ! empty( $af['url'] ) ) {
			$esperado[ $af['url'] ] = 'sponsored noopener';
			if ( ! empty( $af['url_busca'] ) ) {
				$esperado[ $af['url_busca'] ] = 'sponsored noopener';
			}
		} elseif ( ! empty( $af['url_busca'] ) ) {
			$esperado[ $af['url_busca'] ] = 'sponsored noopener';
		} elseif ( ! empty( $af['url_busca_produto'] ) ) {
			/* NINGUEM PAGA POR ESTE CLIQUE: chama-lo de patrocinado e mentir ao
			   leitor sobre a unica coisa que ele tem o direito de saber. */
			$esperado[ $af['url_busca_produto'] ] = 'nofollow noopener';
		}
		foreach ( $esperado as $href => $rel ) {
			$padrao = '#<a[^>]*href="' . preg_quote( htmlspecialchars( $href, ENT_QUOTES ), '#' ) . '"[^>]*rel="' . preg_quote( $rel, '#' ) . '"#';
			if ( ! preg_match( $padrao, $corpo ) ) {
				$rel_errado[] = $pid . ' -> ' . $rel;
			}
		}
	}
	gui_ok( empty( $rel_errado ), 'o rel de cada link sai do que o link E, nunca do formato da pagina',
		empty( $rel_errado ) ? count( $regua['itens'] ) . ' produtos conferidos' : implode( ' | ', $rel_errado ) );

	/* 5c. A FRASE DA LACUNA E DERIVADA, e isto se mede nos DOIS sentidos.
	   A mutacao que a transformou numa lista escrita a mao passou pela primeira
	   versao deste arquivo: ela continua CERTA hoje e so fica errada no dia em
	   que um fabricante novo nomear vidro — o dia em que ninguem vai estar
	   olhando para aquela linha. Entao a afirmacao cobra que a frase nomeie
	   exatamente o que a regua independente diz que falta, e nada do que ela
	   diz que sobra. */
	$rotulos = cdm_f2_rotulos();
	$candidatas = array(
		'base'    => array( 'vidro', 'espelho' ),
		'tessela' => array( 'pastilha_vidro', 'pastilha_ceramica' ),
	);
	$frase_lacuna = '';
	if ( preg_match( '#Entre o que ninguém deste grupo nomeia está(.*?)</p>#su', $corpo, $mfl ) ) {
		$frase_lacuna = gui_texto( $mfl[1] );
	}
	$lacuna_errada = array();
	foreach ( $candidatas as $eixo => $chaves ) {
		$chave_rot = ( 'base' === $eixo ) ? 'base_curto' : 'tessela';
		foreach ( $chaves as $chave ) {
			$nome   = mb_strtolower( $rotulos[ $chave_rot ][ $chave ], 'UTF-8' );
			$falta  = ! in_array( $chave, $regua['quais_cobertas'], true );
			$na_frase = ( '' !== $frase_lacuna && false !== mb_strpos( mb_strtolower( $frase_lacuna, 'UTF-8' ), $nome ) );
			if ( $falta !== $na_frase ) {
				$lacuna_errada[] = $chave . ( $falta ? ' falta e NAO esta na frase' : ' esta coberta e esta na frase' );
			}
		}
	}
	gui_ok( '' !== $frase_lacuna, 'a pagina publica a frase do que ninguem nomeia', mb_substr( $frase_lacuna, 0, 48 ) . '...' );
	gui_ok( empty( $lacuna_errada ), 'a frase da lacuna nomeia exatamente o que a regua diz que falta',
		empty( $lacuna_errada ) ? count( $regua['quais_cobertas'] ) . ' superficies cobertas' : implode( ' | ', $lacuna_errada ) );

	/* 6. A VOZ: o titulo e o primeiro paragrafo falam com a pessoa. */
	$primeiro = '';
	if ( preg_match( '#<p class="cdm-linha-mestra">(.*?)</p>#s', $corpo, $mlm ) ) {
		$primeiro = mb_strtolower( gui_texto( $mlm[1] ), 'UTF-8' );
	}
	$titulo_min = mb_strtolower( $ficha['titulo'], 'UTF-8' );
	$achou_proibida = array();
	foreach ( $PROIBIDAS_NA_VOZ as $termo ) {
		if ( false !== mb_strpos( $titulo_min, $termo ) || false !== mb_strpos( $primeiro, $termo ) ) {
			$achou_proibida[] = $termo;
		}
	}
	gui_ok( '' !== $primeiro, 'a linha mestra abre o corpo', mb_substr( $primeiro, 0, 40 ) . '...' );
	gui_ok( empty( $achou_proibida ), 'nem o titulo nem a linha mestra usam termo que o VOZ.md proibe',
		empty( $achou_proibida ) ? 'limpo' : implode( ', ', $achou_proibida ) );

	/* O JSON-LD desta camada parseia, e o FAQ dele e o MESMO da tela. */
	preg_match( '#<script type="application/ld\+json" id="cdm-guia-jsonld">(.*?)</script>#s', $html, $mj );
	$grafo = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;
	gui_ok( is_array( $grafo ) && ! empty( $grafo['@graph'] ), 'o JSON-LD da pagina parseia' );
	$perguntas_schema = array();
	foreach ( ( $grafo ? $grafo['@graph'] : array() ) as $no ) {
		if ( 'FAQPage' === $no['@type'] ) {
			foreach ( $no['mainEntity'] as $q ) { $perguntas_schema[] = $q['name']; }
		}
	}
	$fora_da_tela = array();
	foreach ( $perguntas_schema as $q ) {
		if ( false === mb_strpos( $texto, $q ) ) { $fora_da_tela[] = mb_substr( $q, 0, 30 ); }
	}
	gui_ok( $perguntas_schema && empty( $fora_da_tela ),
		'toda pergunta do FAQ do schema esta na tela, com as mesmas palavras',
		empty( $fora_da_tela ) ? count( $perguntas_schema ) . ' perguntas' : implode( ' | ', $fora_da_tela ) );
	gui_ok( false === mb_strpos( $texto, '{' ), 'nenhum molde sobrou sem preencher na tela' );
}

/* ---------------------------------------------------------------------------
 * 4. A MALHA DA 16.4
 * ------------------------------------------------------------------------- */

echo "\n4. A malha da 16.4 — a mae lista as filhas, a filha linka a mae\n";

$mae_id    = cdm_guia_mae();
$corpo_mae = gui_corpo( $html_por_id[ $mae_id ] );
foreach ( cdm_guia_filhas() as $fid => $f ) {
	$url = 'https://clubedomosaico.com.br/' . $f['slug'] . '/';
	$ancora = '#<a href="' . preg_quote( $url, '#' ) . '">' . preg_quote( htmlspecialchars( $f['consulta'], ENT_QUOTES ), '#' ) . '</a>#';
	gui_ok( 1 === preg_match( $ancora, $corpo_mae ),
		"16.4(a) a mae linka [$fid] com a consulta-alvo como texto-ancora", $f['consulta'] );

	$corpo_filha = gui_corpo( $html_por_id[ $fid ] );
	$url_mae = 'https://clubedomosaico.com.br/' . cdm_guia_ficha( $mae_id )['slug'] . '/';
	/* NO CORPO, nao na trilha nem no cluster: a 16.4(b) pede os dois, e a
	   trilha sozinha passaria sem a frase. */
	$so_secoes = preg_replace( '#<nav\b.*?</nav>#s', ' ', $corpo_filha );
	gui_ok( false !== strpos( $so_secoes, 'href="' . $url_mae . '"' ),
		"16.4(b) [$fid] linka a mae numa frase do corpo" );
}

/* ---------------------------------------------------------------------------
 * 7. QUATRO PAGINAS NAO SAO A MESMA PAGINA
 * ------------------------------------------------------------------------- */

echo "\n7. As quatro sao paginas diferentes\n";

foreach ( array( 'titulo', 'slug', 'linha_mestra', 'description', 'consulta' ) as $campo ) {
	$valores = array();
	foreach ( cdm_guia_registro() as $ficha ) {
		$valores[] = $ficha[ $campo ];
	}
	gui_ok( count( array_unique( $valores ) ) === count( $valores ), "o campo `$campo` e distinto nas quatro",
		count( array_unique( $valores ) ) . ' de ' . count( $valores ) );
}

/* E o texto de uma nao e copia do da outra: a parte que nao e numero tem de
   divergir. Molde produz pagina fina sem ninguem decidir por isso. */
$ids = array_keys( $textos );
$iguais = array();
for ( $i = 0; $i < count( $ids ); $i++ ) {
	for ( $j = $i + 1; $j < count( $ids ); $j++ ) {
		similar_text( $textos[ $ids[ $i ] ], $textos[ $ids[ $j ] ], $pct );
		if ( $pct > 70 ) {
			$iguais[] = $ids[ $i ] . '/' . $ids[ $j ] . ' ' . round( $pct ) . '%';
		}
	}
}
gui_ok( empty( $iguais ), 'nenhum par de paginas passa de 70% de texto em comum',
	empty( $iguais ) ? count( $ids ) . ' paginas comparadas' : implode( ', ', $iguais ) );

/* ---------------------------------------------------------------------------
 * O PREPARO NA FICHA DO PRODUTO (esquema v12, 06/10/2026) — e aqui ele e CODIGO
 * DORMENTE, o que torna esta secao obrigatoria e nao opcional.
 *
 * Nenhum dos dez itens de `acabamento` tem o campo preenchido hoje, entao as
 * quatro paginas no ar nao servem uma linha de preparo. Codigo que nunca roda e
 * exatamente o `else` que esta ilha mediu morto em 13/09/2026, no ramo das
 * faixas descobertas da F2: ele estava no ar em quatro estados dizendo coisa
 * falsa, e nenhuma regua havia pisado nele porque nenhuma celula o alcancava.
 *
 * Entao esta secao FABRICA O MUNDO: uma raiz sintetica onde um verniz do banco
 * recebe um preparo com literal, fonte e rotulo de tela, e a pagina e renderizada
 * de la. Sao duas afirmacoes, e as duas precisam da outra: a pagina real nao
 * serve nada (porque nao ha dado) e a pagina do mundo fabricado serve (porque o
 * caminho existe). Uma sozinha nao distingue "dormente" de "quebrado".
 * ------------------------------------------------------------------------- */

echo "\n" . "PREPARO NA FICHA — hoje dormente, medido no mundo fabricado\n";

$com_preparo_hoje = 0;
foreach ( (array) $banco_cru['materiais'] as $_m ) {
	if ( ! empty( $_m['preparo']['literal_do_fabricante'] ) ) {
		$com_preparo_hoje++;
	}
}
gui_ok( 0 === $com_preparo_hoje,
	'nenhum item de acabamento tem literal de preparo — o bloco esta dormente por falta de DADO',
	$com_preparo_hoje . ' de ' . count( $banco_cru['materiais'] ) );

$vazou_preparo = array();
foreach ( $html_por_id as $id => $html ) {
	$t = gui_texto( gui_corpo( $html ) );
	if ( false !== mb_strpos( $t, 'Antes de aplicar, o que o fabricante manda fazer' ) ) {
		$vazou_preparo[] = $id;
	}
	/* E a saida degradada NAO pode aparecer com a F2 carregada: ela existe para o
	   dia em que o snippet da F2 cair, e servi-la com ele de pe seria dizer ao
	   leitor que falta algo que nao falta. */
	if ( false !== mb_strpos( $t, 'A parte de preparo está fora do ar' ) ) {
		$vazou_preparo[] = $id . ' (saida degradada com a F2 de pe)';
	}
}
gui_ok( empty( $vazou_preparo ), 'as quatro paginas no ar nao servem bloco de preparo nenhum',
	empty( $vazou_preparo ) ? count( $html_por_id ) . ' paginas' : implode( ', ', $vazou_preparo ) );

$LITERAL_FABRICADO = 'Lixe a peça e remova o pó antes da primeira demão, e aguarde a cura do rejunte.';
$raiz_preparo = gui_raiz_com_preparo( $raiz, $LITERAL_FABRICADO );
$achou_literal = 0;
$achou_fonte   = 0;
foreach ( cdm_guia_registro() as $id => $ficha ) {
	$t = gui_texto( gui_corpo( gui_render( $raiz_preparo, 'cdm_guia_' . $id ) ) );
	if ( false !== mb_strpos( $t, $LITERAL_FABRICADO ) ) {
		$achou_literal++;
		if ( false !== mb_strpos( $t, 'Está escrito na página de produto dele' ) ) {
			$achou_fonte++;
		}
	}
}
gui_ok( $achou_literal > 0,
	'no mundo fabricado a ficha SERVE o literal de preparo — o caminho nao e codigo morto',
	$achou_literal . ' de ' . count( cdm_guia_registro() ) . ' paginas' );
gui_ok( $achou_literal === $achou_fonte && $achou_fonte > 0,
	'e serve junto o documento e a data — frase de fabricante nunca sai sem procedencia',
	$achou_fonte . ' de ' . $achou_literal );

echo "\n";
if ( $falhas ) {
	echo "REPROVADO: $falhas de $feitos verificacoes falharam.\n";
	exit( 1 );
}
echo "APROVADO: $feitos verificacoes, nenhuma falha.\n";

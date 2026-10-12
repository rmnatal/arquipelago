<?php
/**
 * Verificacao MEDIDA das paginas do GUIA — toda mae e toda filha registrada.
 *
 * DESDE A 1.2.0 DO SNIPPET (08/10/2026) ESTE ARQUIVO E POR CATEGORIA, e a
 * mudanca nao e de arrumacao: a regua independente abaixo le o banco da
 * categoria DECLARADA por cada pagina (`cdm_guia_categorias()`), nunca o
 * `materiais-acabamento.json` por nome. Antes, a pagina de uma segunda mae
 * seria conferida contra o banco do acabamento e passaria com os numeros
 * errados — verde que mede outra coisa, que e o pior resultado possivel.
 *
 * E A BANCADA FALHA FECHADA: categoria publicada cuja FAMILIA DE NUMEROS nao
 * tem regua independente aqui REPROVA, com o nome dela na tela. Nao e zelo —
 * a familia do Guia cresce por categoria, e a regua que nao acompanha deixa a
 * pagina nova sem nenhuma afirmacao sobre numero. Reprovar e o que obriga quem
 * publica a segunda mae a escrever a regua dela no mesmo bloco.
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

	/* O ARQUIVO DO BANCO VEM DA DECLARACAO DA CATEGORIA, nunca do nome: este
	   helper fabrica um mundo dentro da categoria `acabamento`, e o id do dado
	   dela e o que `cdm_guia_categorias()` diz que e. Escrito a mao aqui, este
	   caminho quebraria no dia em que o banco fosse renomeado — e quebraria
	   dentro da bancada, que e o pior lugar para um nome velho morar. */
	$id_do_banco = cdm_guia_categorias()['acabamento']['banco'];
	$arq   = $destino . '/dados/' . $id_do_banco . '.json';
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

$esquema   = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$filhas_do_guia = json_decode( (string) @file_get_contents( $raiz . '/dados/filhas-do-guia.json' ), true );
$cruzamento_md  = (string) @file_get_contents( $raiz . '/dados/cruzamento-14-9.md' );
$manifest  = json_decode( (string) @file_get_contents( $raiz . '/manifest.json' ), true );
if ( ! $esquema || ! $filhas_do_guia || '' === $cruzamento_md || ! $manifest ) {
	echo "ERRO: nao consegui ler o esquema, as filhas-do-guia, o cruzamento ou o manifest.\n";
	exit( 1 );
}

/* O BANCO DE CADA CATEGORIA, LIDO PELO ID QUE ELA DECLARA — que e o mesmo id
   do `manifest.json` e, portanto, o mesmo nome de option que o Sync grava. Ler
   por nome de arquivo aqui seria a segunda lista que envelhece calada. */
$banco_por_cat = array();
$ativos_por_cat = array();
foreach ( cdm_guia_categorias() as $cat => $decl ) {
	$id_dado = isset( $decl['banco'] ) ? (string) $decl['banco'] : '';
	$bruto   = ( '' === $id_dado )
		? null
		: json_decode( (string) @file_get_contents( $raiz . '/dados/' . $id_dado . '.json' ), true );
	$banco_por_cat[ $cat ] = is_array( $bruto ) ? $bruto : array( 'materiais' => array() );
	$ativos = array();
	foreach ( (array) $banco_por_cat[ $cat ]['materiais'] as $m ) {
		if ( 'ativo' === $m['status'] ) {
			$ativos[ $m['id'] ] = $m;
		}
	}
	ksort( $ativos );
	$ativos_por_cat[ $cat ] = $ativos;
}

/* ---------------------------------------------------------------------------
 * A REGUA INDEPENDENTE: a cobertura e o relogio, recontados do JSON cru.
 * ------------------------------------------------------------------------- */

$BASES    = $esquema['vocabularios']['base'];
$TESSELAS = $esquema['vocabularios']['material_tessela'];
$N_SUP    = count( $BASES ) + count( $TESSELAS );

/* A REGUA INDEPENDENTE DE CADA FAMILIA DE NUMEROS, pelo nome da regua do
   snippet — nao pelo da categoria. A categoria diz QUAL BANCO ler; a regua diz
   QUE CONTA fazer com ele. Se um dia duas categorias publicarem a mesma familia
   de numeros, elas compartilham esta linha; se uma publicar familia nova, a
   ausencia aqui REPROVA com o nome dela. */
$REGUAS_DA_BANCADA = array( 'acabamento' => 'gui_regua_do_acabamento' );

/** O esperado de um recorte de ACABAMENTO, por um caminho que nao passa pelo snippet. */
function gui_regua_do_acabamento( $tipo, $ativos, $bases, $tesselas, $propriedade = null ) {
	$itens = array();
	$nomeadas = 0;
	$relogios = 0;
	$com_momento = 0;
	$cobertas = array();
	$demaos = array();
	$intervalos = array();
	$diluicoes = array();
	$pigmentos = array();
	$tipos_rec = array();
	foreach ( $ativos as $id => $m ) {
		if ( null !== $tipo && $m['tipo'] !== $tipo ) {
			continue;
		}
		/* A TERCEIRA FORMA DE RECORTE (12/10/2026): os itens que DECLARAM uma
		   propriedade com fonte. Escrita aqui do zero, sem chamar nada do
		   snippet — se as duas metades lessem a mesma funcao, a bancada passaria
		   a confirmar o recorte em vez de conferi-lo, que e o defeito que esta
		   ilha mede com mutacao. */
		if ( null !== $propriedade ) {
			$pp = isset( $m['propriedades'][ $propriedade ] ) ? $m['propriedades'][ $propriedade ] : array();
			if ( ! isset( $pp['valor'] ) || null === $pp['valor'] || empty( $pp['fonte_id'] ) ) {
				continue;
			}
		}
		$itens[] = $id;
		if ( ! empty( $m['tipo'] ) ) { $tipos_rec[ (string) $m['tipo'] ] = true; }
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
		if ( is_numeric( $d ) ) { $demaos[] = (int) $d; }
		if ( is_numeric( $i ) ) { $intervalos[] = (int) $i; }
		/* A DILUICAO, contada aqui do zero como tudo nesta regua. Ela nao e
		   numero: e frase do fabricante, e por isso o que se conta e QUANTOS
		   declaram e QUANTAS RESPOSTAS DIFERENTES saem disso — por igualdade
		   de string, nunca por juizo sobre o que elas querem dizer. Classificar
		   aqui seria a bancada repetindo a decisao do snippet em vez de
		   conferi-la, e seria a bancada arbitrando pelo fabricante. */
		$dl = $v( 'diluicao' );
		if ( null !== $dl && '' !== (string) $dl ) { $diluicoes[] = (string) $dl; }
		/* A PIGMENTACAO, contada aqui do zero pelo mesmo motivo da diluicao, e
		   com a MESMA trava que a regua do snippet: o que se conta e quantos
		   declaram, quantos declaram `'sim'` por igualdade ESTRITA e quantas
		   respostas diferentes saem. A bancada NAO conta o complemento, para
		   nao ser ela a chamar de transparente o que so nao disse `sim`. */
		$pg = $v( 'pigmentado' );
		if ( null !== $pg && '' !== (string) $pg ) { $pigmentos[] = (string) $pg; }
	}
	$acima_de_uma = array_values( array_filter( $demaos, function ( $x ) { return $x > 1; } ) );

	return array(
		'itens'          => $itens,
		'n'              => count( $itens ),
		'com_demaos'     => count( $demaos ),
		'com_uma_demao'  => count( array_keys( $demaos, 1, true ) ),
		'demaos_max'     => $demaos ? max( $demaos ) : null,
		'demaos_min_acima_de_uma' => $acima_de_uma ? min( $acima_de_uma ) : null,
		/* OS TIPOS DO RECORTE E O TOTAL DA CATEGORIA, contados aqui porque
		   duas mutacoes de 12/10/2026 PASSARAM sem eles: a ponte podia cravar
		   "as tres etapas" numa pergunta que atravessa duas, e o denominador
		   do "os outros N nao dizem nada" podia medir o recorte em vez do
		   banco e sair ZERO. As duas publicam numero falso e passavam em tudo,
		   porque 3 e 0 sao inteiros validos. */
		'n_tipos'        => count( $tipos_rec ),
		'n_ativos'       => count( $ativos ),
		'com_diluicao'   => count( $diluicoes ),
		'diluicoes_distintas' => count( array_unique( $diluicoes ) ),
		'com_pigmento'   => count( $pigmentos ),
		'pigmentados'    => count( array_keys( $pigmentos, 'sim', true ) ),
		'pigmentos_distintos' => count( array_unique( $pigmentos ) ),
		'com_intervalo'  => count( $intervalos ),
		'intervalo_min'  => $intervalos ? min( $intervalos ) : null,
		'intervalo_max'  => $intervalos ? max( $intervalos ) : null,
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

/* AS PERGUNTAS NÃO ESTÃO NAQUELA LISTA, E NÃO É ESQUECIMENTO DO CRUZAMENTO: a
   linha `Podem nascer hoje, pelos DOIS portoes` enumera RECORTES DE TIPO, e a
   filha em forma de pergunta tem tabela própria naquele arquivo. Até 12/10/2026
   esta bancada só sabia da primeira, e derivava o recorte de cada página como
   `categoria` ou `categoria/tipo` — com a página de pergunta, cujo `tipo` é
   null, a derivação devolvia o recorte da MÃE e a página passava no lugar dela,
   calada. As duas listas entram, cada uma lida de onde ela mora. */
$pode_nascer_pergunta = array();
if ( preg_match_all( '#^\|\s*`(pergunta:[^`]+)`\s*\|[^|]*\|[^|]*\|[^|]*\|\s*\*\*`([a-z_]+)`\*\*#um',
		$cruzamento_md, $mq, PREG_SET_ORDER ) ) {
	foreach ( $mq as $linha ) {
		if ( 'pode_nascer' === $linha[2] ) {
			$pode_nascer_pergunta[] = $linha[1];
		}
	}
}
gui_ok( count( $pode_nascer_pergunta ) > 0,
	'a tabela das perguntas do cruzamento foi lida, e ao menos uma esta em pode_nascer',
	implode( ', ', $pode_nascer_pergunta ) );

$recortes_publicados = array();
foreach ( cdm_guia_registro() as $id => $ficha ) {
	/* O RECORTE SAI DA CATEGORIA DA PROPRIA PAGINA. Com `acabamento` escrito
	   aqui, a pagina de uma segunda mae seria conferida contra o recorte da
	   primeira e passaria por coincidencia de nome. */
	$cat     = $ficha['categoria'];
	$forma   = cdm_guia_forma( $id );
	$recorte = isset( $ficha['recorte'] ) ? (string) $ficha['recorte'] : '';

	/* O RECORTE É DECLARADO NA FICHA, E AQUI ELE É CONFERIDO CONTRA A FORMA —
	   campo escrito a mão que ninguem confere e campo que nao existe custam o
	   mesmo. Mae tem o nome da categoria, filha de tipo tem `cat/tipo`, filha de
	   pergunta tem um id que comeca com `pergunta:`. */
	$esperado = '';
	if ( 'mae' === $forma ) {
		$esperado = $cat;
	} elseif ( 'tipo' === $forma ) {
		$esperado = $cat . '/' . $ficha['tipo'];
	}
	if ( 'pergunta' === $forma ) {
		gui_ok( 0 === strpos( $recorte, 'pergunta:' ),
			"[$id] o recorte declarado e um id de pergunta", $recorte );
	} else {
		gui_ok( '' !== $esperado && $recorte === $esperado,
			"[$id] o recorte declarado bate com a forma da pagina",
			$recorte . ' (esperado ' . $esperado . ')' );
	}

	$recortes_publicados[ $id ] = $recorte;
	$lista = ( 'pergunta' === $forma ) ? $pode_nascer_pergunta : $pode_nascer;
	gui_ok( in_array( $recorte, $lista, true ),
		"[$id] o recorte esta em pode_nascer (os dois portoes abriram)", $recorte );
}

/* A SEGUNDA DIRECAO, e e ela que impede a familia de crescer calada: recorte
   autorizado e nao publicado e uma pagina que deveria existir e nao existe —
   exatamente o estado em que esta ilha passou quatro execucoes com o 4c.
   A conferencia e POR CATEGORIA PUBLICADA: categoria que ainda nao tem mae
   nenhuma nao e cobrada aqui (a 14.9 autoriza, quem publica e a fila), e
   categoria que ja tem pagina e cobrada INTEIRA. */
$cats_publicadas = array();
foreach ( cdm_guia_registro() as $ficha ) {
	$cats_publicadas[ $ficha['categoria'] ] = true;
}
foreach ( array_keys( $cats_publicadas ) as $cat ) {
	$autorizados = array_values( array_filter( $pode_nascer, function ( $r ) use ( $cat ) {
		return $cat === $r || 0 === strpos( $r, $cat . '/' );
	} ) );
	/* E AS PERGUNTAS DESTA CATEGORIA TAMBÉM, pelo mesmo motivo da direção: a
	   pergunta que os dois portões autorizam e que ninguem publicou e uma pagina
	   que devia existir. A categoria da pergunta e lida do proprio cruzamento,
	   nunca do nome dela — `pergunta:alicate-...` e da `alicate` por declaracao
	   e nao por prefixo. */
	foreach ( $pode_nascer_pergunta as $pid ) {
		if ( preg_match( '#^\|\s*`' . preg_quote( $pid, '#' ) . '`\s*\|\s*`([^`]+)`#um',
				$cruzamento_md, $mc ) && $cat === $mc[1] ) {
			$autorizados[] = $pid;
		}
	}
	sort( $autorizados );
	$publicados = array();
	foreach ( $recortes_publicados as $id => $recorte ) {
		if ( $cat === cdm_guia_registro()[ $id ]['categoria'] ) {
			$publicados[] = $recorte;
		}
	}
	sort( $publicados );
	gui_ok( $autorizados === $publicados,
		"[$cat] todo recorte autorizado tem pagina, e nenhuma pagina sem autorizacao",
		'autorizados: ' . implode( ', ', $autorizados ) );
}

/* E O PORTAO DE DADO DA SECAO 9, lido do arquivo que o deriva. */
foreach ( $recortes_publicados as $id => $recorte ) {
	if ( 'pergunta' === cdm_guia_forma( $id ) ) {
		/* NA PERGUNTA AS TRES AFIRMACOES COINCIDEM, e e o proprio
		   `filhas-do-guia.py` que explica por que: o recorte dela E o conjunto
		   dos itens que declaram o numero com lastro, entao "3 itens", "3 com
		   lastro" e "um numero sobre 3" sao a mesma contagem. Cobrar aqui a
		   coluna `numeros_calculaveis_sobre_o_recorte`, que so existe na tabela
		   dos tipos, reprovaria pagina certa. */
		$achou = null;
		foreach ( $filhas_do_guia['perguntas'] as $p ) {
			if ( $p['pergunta'] === $recorte ) { $achou = $p; }
		}
		gui_ok( $achou && 'passa' === $achou['veredito']
			&& $achou['itens_que_declaram_o_numero'] >= 3
			&& empty( $achou['divergencias_com_a_ancora_a_mao'] ),
			"[$id] 3 itens declaram o numero com lastro, e a ancora a mao nao caiu (secao 9)",
			$achou ? $achou['itens_que_declaram_o_numero'] . ' itens, '
				. count( $achou['divergencias_com_a_ancora_a_mao'] ) . ' divergencia(s)' : 'pergunta ausente' );

		/* E O RECORTE DO PHP TEM DE SER O MESMO QUE O PORTAO MEDIU, item por
		   item. As duas metades contam o lastro por caminhos diferentes — o
		   Python por `propriedades_com_lastro`, o PHP por `cdm_guia_valor()` — e
		   e exatamente o par de contagens que divergiria calado. */
		if ( $achou ) {
			$do_php = cdm_guia_contas( $id )['itens'];
			sort( $do_php );
			$do_portao = $achou['itens'];
			sort( $do_portao );
			gui_ok( $do_php === $do_portao,
				"[$id] o recorte do PHP traz exatamente os itens que o portao de dado mediu",
				implode( ', ', $do_php ) );
		}
		continue;
	}
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
 * 1-b. A ESTRUTURA DE N CATEGORIAS — os portoes que so existem porque o Guia
 * deixou de ser de uma categoria so (snippet 1.2.0, 08/10/2026)
 *
 * Cada afirmacao aqui e um jeito de a segunda mae nascer errada em silencio.
 * Hoje todas passam com uma categoria, e isso nao as torna decorativas: elas
 * sao o portao do dia em que a segunda entrar, e portao escrito depois do
 * defeito e portao escrito tarde.
 * ------------------------------------------------------------------------- */

echo "\n1-b. A estrutura por categoria\n";

$ids_dos_dados = array();
foreach ( (array) $manifest['dados'] as $d ) {
	$ids_dos_dados[ $d['id'] ] = ! empty( $d['publicar'] );
}

foreach ( cdm_guia_registro() as $id => $ficha ) {
	gui_ok( ! empty( $ficha['categoria'] ) && isset( cdm_guia_categorias()[ $ficha['categoria'] ] ),
		"[$id] a pagina declara uma categoria que existe em cdm_guia_categorias()",
		isset( $ficha['categoria'] ) ? (string) $ficha['categoria'] : 'AUSENTE' );
}

foreach ( cdm_guia_categorias() as $cat => $decl ) {
	/* O BANCO DA CATEGORIA E UM DADO DO MANIFEST, E PUBLICADO. Id que nao esta
	   no manifest nunca chega ao site como option, e a pagina sairia com o
	   aviso de "sem medicao" para sempre, sem ninguem saber por que. */
	$id_dado = isset( $decl['banco'] ) ? (string) $decl['banco'] : '';
	gui_ok( '' !== $id_dado && isset( $ids_dos_dados[ $id_dado ] ) && $ids_dos_dados[ $id_dado ],
		"[$cat] o banco declarado esta no manifest com publicar=true", $id_dado );
	gui_ok( ! empty( $banco_por_cat[ $cat ]['materiais'] ),
		"[$cat] o arquivo do banco declarado existe e tem material",
		count( (array) $banco_por_cat[ $cat ]['materiais'] ) . ' no arquivo, '
		. count( $ativos_por_cat[ $cat ] ) . ' ativos' );

	/* OS SEIS PAPEIS DA REGUA, um a um: meia regua serve meia pagina. */
	$faltando = array();
	foreach ( cdm_guia_papeis_da_regua() as $papel ) {
		if ( '' === cdm_guia_regua_da_categoria( $cat, $papel ) ) {
			$faltando[] = $papel;
		}
	}
	gui_ok( empty( $faltando ), "[$cat] a regua declara os " . count( cdm_guia_papeis_da_regua() ) . ' papeis, e todos existem',
		empty( $faltando ) ? $decl['regua'] : 'faltam: ' . implode( ', ', $faltando ) );

	/* E O BANCO DECLARADO E O DA CATEGORIA, nao so um banco que existe. A lista
	   de itens vem de `filhas-do-guia.json`, que varre TODOS os
	   `dados/materiais-*.json` e rotula cada item pela categoria do esquema —
	   caminho que nao passa pela declaracao. Sem esta afirmacao, trocar o
	   `banco` de uma categoria pelo de outra passaria VERDE: a pagina e esta
	   bancada leriam o mesmo arquivo errado e concordariam. E a lacuna que
	   sobra quando as duas metades leem a mesma declaracao. */
	$itens_do_recorte = null;
	foreach ( $filhas_do_guia['recortes'] as $r ) {
		if ( $r['recorte'] === $cat ) {
			$itens_do_recorte = $r['itens'];
		}
	}
	$do_banco  = array_keys( $ativos_por_cat[ $cat ] );
	$esperados = (array) $itens_do_recorte;
	sort( $do_banco );
	sort( $esperados );
	gui_ok( null !== $itens_do_recorte && $do_banco === $esperados,
		"[$cat] o banco declarado traz exatamente os itens que o cruzamento da a esta categoria",
		count( $do_banco ) . ' no banco, ' . count( $esperados ) . ' no recorte' );

	/* E A BANCADA TEM REGUA INDEPENDENTE PARA ESTA FAMILIA. Sem isto a pagina
	   nova nao teria NENHUMA afirmacao de numero conferida — verde por ausencia. */
	$nome_regua = isset( $decl['regua'] ) ? (string) $decl['regua'] : '';
	gui_ok( isset( $REGUAS_DA_BANCADA[ $nome_regua ] ) && function_exists( $REGUAS_DA_BANCADA[ $nome_regua ] ),
		"[$cat] esta bancada tem regua independente para a familia `$nome_regua`",
		isset( $REGUAS_DA_BANCADA[ $nome_regua ] ) ? $REGUAS_DA_BANCADA[ $nome_regua ] : 'NENHUMA' );
}

/* O `tipo` DE CADA FILHA E DO VOCABULARIO DA PROPRIA CATEGORIA. Tipo de outra
   categoria daria recorte que o cruzamento nem conhece, e a mensagem de erro
   sairia sobre o portao errado. */
$tipo_por_cat = $esquema['vocabularios']['tipo_por_categoria'];
foreach ( cdm_guia_registro() as $id => $ficha ) {
	if ( null === $ficha['tipo'] ) {
		continue;
	}
	$cat = $ficha['categoria'];
	gui_ok( isset( $tipo_por_cat[ $cat ] ) && in_array( $ficha['tipo'], (array) $tipo_por_cat[ $cat ], true ),
		"[$id] o tipo esta no vocabulario da categoria `$cat`", (string) $ficha['tipo'] );
}

/* TODA CATEGORIA COM FILHA PUBLICADA TEM A MAE DELA PUBLICADA. Filha pendurada
   em `/materiais/` sem a mae e o cluster ralo da 16.6 — e, no codigo, e o
   `$pai` caindo para `materiais` sem nenhum erro de PHP. */
foreach ( array_keys( $cats_publicadas ) as $cat ) {
	$filhas = cdm_guia_filhas( $cat );
	gui_ok( '' !== cdm_guia_mae( $cat ) || empty( $filhas ),
		"[$cat] a mae da categoria esta publicada, e as filhas penduram nela",
		'mae: ' . ( cdm_guia_mae( $cat ) ?: 'NENHUMA' ) . ', filhas: ' . count( $filhas ) );
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

	/* A REGUA DESTA PAGINA: o banco e o da categoria dela, e a conta e a da
	   familia de numeros que a categoria declara. */
	$cat        = $ficha['categoria'];
	$ativos     = $ativos_por_cat[ $cat ];
	$nome_regua = cdm_guia_categorias()[ $cat ]['regua'];
	$prop       = isset( $ficha['propriedade'] ) ? $ficha['propriedade'] : null;
	$regua      = call_user_func( $REGUAS_DA_BANCADA[ $nome_regua ], $ficha['tipo'], $ativos, $BASES, $TESSELAS, $prop );

	gui_ok( '' !== $corpo, 'a pagina montou em processo proprio', strlen( $html ) . ' bytes' );

	/* 2. AS CONTAS, conferidas NA TELA contra a regua independente.
	   A PAGINA DE PERGUNTA ABRE COM OUTRA FRASE, e de proposito: ela responde a
	   pergunta antes de contar produto, e dizer "Sao N produtos deste tipo" numa
	   pagina que nao tem tipo seria a mentira que o campo `papel` existe para
	   impedir. O numero do recorte continua sendo cobrado NA TELA, na frase que
	   ela usa. */
	if ( 'pergunta' === cdm_guia_forma( $id ) ) {
		/* A BANCADA TAMBEM ERA SINGULAR, e ela acusou isso sozinha em
		   12/10/2026. Este ramo inteiro supunha que TODA pagina-pergunta
		   publica demaos: ele cobrava a faixa de demao e o intervalo na tela
		   de qualquer recorte de pergunta, e a segunda pergunta do acabamento
		   — a da diluicao — reprovou em tres afirmacoes por nao falar de
		   demao, que e exatamente o que ela nao deve falar. O portao estava
		   certo e a suposicao dele estava velha: `'pergunta' === $forma` diz a
		   FORMA e nao a GRANDEZA, e a grandeza e que decide o numero cobrado.
		   Agora o despacho e pela propriedade do recorte, igual ao da regua, e
		   propriedade sem ramo aqui REPROVA em vez de passar calada — pagina
		   com numero nao conferido e o estado em que a `cola` ficou por quatro
		   blocos. */
		gui_ok( null !== $prop, 'a pagina de pergunta declara a propriedade do recorte', (string) $prop );

		/* QUANTAS ETAPAS A PONTE DIZ QUE A PERGUNTA ATRAVESSA, contra a contagem
		   independente. A frase da 1.3.0 dizia "as tres etapas" com a palavra
		   digitada, e a segunda pergunta atravessa DUAS — mutacao de 12/10/2026
		   que PASSOU por falta desta linha. A afirmacao vale para as duas
		   perguntas: e a ponte que nao pode mentir, qualquer que seja a grandeza. */
		$esperado_ponte = ( 3 === $regua['n_tipos'] )
			? 'atravessa as três etapas'
			: ( ( 2 === $regua['n_tipos'] ) ? 'atravessa duas das três etapas' : 'atravessa as etapas' );
		gui_ok( false !== mb_strpos( $texto, $esperado_ponte ),
			'a ponte diz quantas etapas a pergunta atravessa, e bate com a contagem',
			$regua['n_tipos'] . ' tipo(s): ' . $esperado_ponte );

		if ( 'demaos_minimas' === $prop ) {
			gui_ok( false !== mb_strpos( $texto, 'dos ' . $regua['com_demaos'] . ' produtos desta página' ),
				'a tela publica o numero de produtos do recorte (frase da pergunta)',
				$regua['com_demaos'] . ' produtos' );
			gui_ok( $regua['com_demaos'] === $regua['n'],
				'o recorte da pergunta E o conjunto que declara o numero — as duas contagens coincidem',
				$regua['n'] . ' = ' . $regua['com_demaos'] );
			gui_ok( false !== mb_strpos( $texto, 'de ' . $regua['demaos_min_acima_de_uma'] . ' a ' . $regua['demaos_max'] . ' demãos' ),
				'a faixa de demaos de quem pede mais de uma bate com a contagem',
				$regua['demaos_min_acima_de_uma'] . ' a ' . $regua['demaos_max'] );
			gui_ok( false !== mb_strpos( $texto, 'de ' . $regua['intervalo_min'] . ' minutos a ' . $regua['intervalo_max'] ),
				'o intervalo entre demaos na tela bate com a contagem',
				$regua['intervalo_min'] . ' a ' . $regua['intervalo_max'] );
			gui_ok( false !== mb_strpos( $texto, 'Em ' . $regua['com_intervalo'] . ' dos ' . $regua['com_demaos'] . ' dá para somar' ),
				'quantos declaram o intervalo bate com a contagem', (string) $regua['com_intervalo'] );
		} elseif ( 'diluicao' === $prop ) {
			gui_ok( false !== mb_strpos( $texto, 'dos ' . $regua['com_diluicao'] . ' que dizem algo sobre diluição' ),
				'a tela publica o numero de produtos do recorte (frase da pergunta)',
				$regua['com_diluicao'] . ' produtos' );
			gui_ok( $regua['com_diluicao'] === $regua['n'],
				'o recorte da pergunta E o conjunto que declara o numero — as duas contagens coincidem',
				$regua['n'] . ' = ' . $regua['com_diluicao'] );
			gui_ok( false !== mb_strpos( $texto, $regua['diluicoes_distintas'] . ' respostas diferentes' ),
				'quantas respostas diferentes saem das frases bate com a contagem',
				(string) $regua['diluicoes_distintas'] );
			/* A PAGINA NAO PODE ESCOLHER PELO FABRICANTE (26.3), e isto mede
			   isso na TELA e nao na intencao de quem escreveu: a frase da
			   resposta nao nomeia solvente. Quem nomeia e a tabela, item por
			   item, com a fonte — e e por isso que a palavra pode existir no
			   corpo e nao pode existir na resposta. */
			$resp = mb_substr( $texto, 0, false !== mb_strpos( $texto, 'Das ' ) ? mb_strpos( $texto, 'Das ' ) : 400 );
			gui_ok( false === mb_stripos( $resp, 'thinner' ) && false === mb_stripos( $resp, 'base de água' ),
				'a frase de resposta NAO classifica o solvente — quem nomeia e a tabela, com fonte (26.3)', 'limpa' );

			/* O DENOMINADOR DO "OS OUTROS N NAO DIZEM NADA" MEDE O BANCO, NAO O
			   RECORTE. Na pagina-pergunta o recorte E quem declara, entao a conta
			   contra o recorte da ZERO e a frase mente dizendo que a etapa inteira
			   declara. Mutacao de 12/10/2026 que PASSOU por falta desta linha. */
			gui_ok( false !== mb_strpos( $texto, 'Os outros ' ) || false !== mb_strpos( $texto, 'produtos desta etapa não dizem nada' ),
				'a tela publica o numero dos que ficaram de fora do recorte', 'frase presente' );
			gui_ok( false !== mb_strpos( $texto, 'Os outros ' . ( $regua['n_ativos'] - $regua['com_diluicao'] ) . ' produtos desta etapa não dizem nada' ),
				'quem ficou de fora e contado contra o BANCO da categoria, nao contra o recorte',
				( $regua['n_ativos'] - $regua['com_diluicao'] ) . ' de ' . $regua['n_ativos'] );
		} elseif ( 'pigmentado' === $prop ) {
			gui_ok( false !== mb_strpos( $texto, 'dos ' . $regua['com_pigmento'] . ' produtos desta etapa que dizem se têm cor própria' ),
				'a tela publica o numero de produtos do recorte (frase da pergunta)',
				$regua['com_pigmento'] . ' produtos' );
			gui_ok( $regua['com_pigmento'] === $regua['n'],
				'o recorte da pergunta E o conjunto que declara o numero — as duas contagens coincidem',
				$regua['n'] . ' = ' . $regua['com_pigmento'] );
			gui_ok( false !== mb_strpos( $texto, $regua['pigmentados'] . ' se declaram pigmentados' ),
				'quantos se declaram pigmentados bate com a contagem independente',
				(string) $regua['pigmentados'] );
			gui_ok( false !== mb_strpos( $texto, $regua['pigmentos_distintos'] . ' respostas diferentes' ),
				'quantas respostas diferentes saem das frases bate com a contagem',
				(string) $regua['pigmentos_distintos'] );

			/* A TELA NAO PODE CHAMAR DE TRANSPARENTE O QUE SO NAO DISSE `sim`,
			   e isto mede isso na TELA. A frase que a pagina serve e o
			   contrario — ela diz, com essas palavras, que nao dizer nada nao e
			   dizer que e transparente. A afirmacao existe porque a subtracao
			   `com_pigmento - pigmentados` passaria em toda bancada de numero:
			   ela devolve um inteiro valido, e so a leitura e falsa. */
			gui_ok( false === mb_strpos( $texto, 'não pigmentados' )
				&& false !== mb_strpos( $texto, 'não dizer nada não é dizer que é transparente' ),
				'a tela NAO chama de transparente quem so nao declarou, e diz isso por extenso',
				'frase presente e complemento ausente' );

			/* O DENOMINADOR DO "OS OUTROS N" MEDE O BANCO E NAO O RECORTE, a
			   mesma trava da pagina da diluicao: na pagina-pergunta o recorte E
			   quem declara, e a conta contra ele daria ZERO. */
			gui_ok( false !== mb_strpos( $texto, 'Os outros ' . ( $regua['n_ativos'] - $regua['com_pigmento'] ) . ' produtos desta etapa' ),
				'quem ficou de fora e contado contra o BANCO da categoria, nao contra o recorte',
				( $regua['n_ativos'] - $regua['com_pigmento'] ) . ' de ' . $regua['n_ativos'] );
		} else {
			gui_ok( false, 'a grandeza desta pergunta tem ramo de conferencia na bancada',
				'SEM RAMO para `' . (string) $prop . '`' );
		}
	} else {
		gui_ok( false !== mb_strpos( $texto, 'São ' . $regua['n'] . ' produtos' ),
			'a tela publica o numero de produtos do recorte', $regua['n'] . ' produtos' );
	}
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

foreach ( cdm_guia_maes() as $cat_da_mae => $mae_id ) {
$corpo_mae = gui_corpo( $html_por_id[ $mae_id ] );
foreach ( cdm_guia_filhas( $cat_da_mae ) as $fid => $f ) {
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
$total_de_itens   = 0;
foreach ( $banco_por_cat as $_cat => $_b ) {
	foreach ( (array) $_b['materiais'] as $_m ) {
		$total_de_itens++;
		if ( ! empty( $_m['preparo']['literal_do_fabricante'] ) ) {
			$com_preparo_hoje++;
		}
	}
}
gui_ok( 0 === $com_preparo_hoje,
	'nenhum item das categorias publicadas tem literal de preparo — o bloco esta dormente por falta de DADO',
	$com_preparo_hoje . ' de ' . $total_de_itens );

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
gui_ok( empty( $vazou_preparo ), 'as paginas no ar nao servem bloco de preparo nenhum',
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

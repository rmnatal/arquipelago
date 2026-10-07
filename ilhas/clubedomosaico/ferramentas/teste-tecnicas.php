<?php
/**
 * Verificacao MEDIDA das paginas de TECNICA — TODAS as que o snippet publica.
 *
 *   php ferramentas/teste-tecnicas.php .
 *
 * -------------------------------------------------------------------------
 * DE ONDE VEM O ESPERADO, e por que NAO e do snippet
 * -------------------------------------------------------------------------
 * A pagina imprime a decisao de `cdm_f2_celula_cola()`, que e PHP. Se a regua
 * deste arquivo tambem chamasse aquela funcao, as duas metades errariam juntas
 * e o verde nao significaria nada (secao 8 do ARQUIPELAGO.md).
 *
 * Entao o esperado vem de `dados/cobertura.json`, que e gerado por
 * `ferramentas/cobertura.py` a partir da regua do `validar-banco.py` — uma
 * implementacao INDEPENDENTE, em outra linguagem, escrita no bloco 3 antes de
 * existir uma linha do snippet. E a mesma disciplina do `conferir-cobertura.php`:
 * duas metades que tem de dar o mesmo numero nas 45 celulas de cada caquinho.
 *
 * O arquivo de cobertura so vale como regua se estiver FRESCO, entao a primeira
 * coisa que este teste faz e rodar `cobertura.py --conferir`. Regua velha
 * aprovaria a pagina de ontem, que e a cicatriz que a Robometria pagou em
 * 14/09/2026 com 167 afirmacoes verdadeiras sobre uma pagina que ninguem
 * estava recebendo.
 *
 * -------------------------------------------------------------------------
 * POR QUE ELE VAROU DE UMA PAGINA PARA A FAMILIA (1.1.0, 14/09/2026)
 * -------------------------------------------------------------------------
 * A versao de 14/09 media `CDM_TECNICAS_ID` — a tecnica unica, escrita numa
 * constante. Publicar a segunda pagina com o teste assim teria um efeito que
 * nenhum numero mostraria: o teste continuaria verde medindo SO a primeira, e a
 * segunda nasceria sem regua nenhuma. Agora ele varre `cdm_tecnicas_registro()`
 * e repete TODAS as afirmacoes em cada pagina, alem de conferir que o registro
 * e o banco concordam nos dois sentidos.
 *
 * -------------------------------------------------------------------------
 * A AFIRMACAO QUE SO EXISTE COM DOIS CAQUINHOS
 * -------------------------------------------------------------------------
 * O trencadis declara `caco_azulejo` e `caco_louca`. A pagina agrupa os
 * caquinhos cujas grades saem IGUAIS e serve uma tabela por grupo. Este teste
 * reconta o agrupamento pela cobertura — celula a celula, em Python — e cobra
 * (a) que o numero de tabelas servidas seja o numero de grupos que a cobertura
 * enxerga e (b) que a pagina DIGA na tela quantas combinacoes comparou. Sem a
 * segunda metade, uma tabela so continuaria certa e o leitor nao saberia se ela
 * vale para o caco de azulejo, para o de louca ou para os dois.
 *
 * -------------------------------------------------------------------------
 * O QUE ELE MEDE ALEM DA GRADE
 * -------------------------------------------------------------------------
 *   - A prestacao de contas da secao 7: a soma dos nomeados FECHA com o tamanho
 *     do banco, contado do arquivo e nunca digitado. Cada cola aparece UMA vez.
 *   - Nenhum item sem saida de compra, e o `rel` de cada link saindo do que o
 *     link E (secao 25, e a correcao de 14/09 da secao 7).
 *   - A recusa do rejunte esta escrita, com a causa.
 *   - A voz: os termos que o VOZ.md proibe no titulo e no primeiro paragrafo.
 *   - O JSON-LD parseia e o FAQ do schema e o MESMO da tela.
 *   - DUAS PAGINAS NAO SAO A MESMA PAGINA: titulo, slug, linha mestra e
 *     description distintos, e o texto de uma nao e copia do da outra. Malha que
 *     nasce de um molde produz pagina fina sem ninguem decidir por isso.
 *
 * Medido dentro de <main>, sempre: afirmacao sobre o que a pagina DIZ se conta
 * no corpo servido, nao no HTML inteiro.
 *
 * O QUE ESTE ARQUIVO NAO MEDE, E ONDE ISSO E MEDIDO. O caminho sem banco — a
 * pagina dizendo que nao conseguiu medir em vez de inventar — nao cabe aqui:
 * a bancada carrega as options do manifest na entrada do processo, entao
 * produzir a ausencia e produzir outro MUNDO, nao outra afirmacao. Ele e
 * medido em `ferramentas/mutacoes-tecnicas-pagina.py`, que apaga o `publicar`
 * do banco e exige a pagina honesta. A primeira versao deste arquivo tinha
 * uma secao 8 que imprimia `ok` sem medir nada; ficou escrito aqui por que ela
 * saiu, porque afirmacao que nao pode falhar e pior que afirmacao ausente
 * (secao 8 do ARQUIPELAGO.md).
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function tec_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-68s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-68s %s\n", $rotulo, $medida );
	return false;
}

function tec_corpo( $html ) {
	if ( preg_match( '#<main\b[^>]*>(.*?)</main>#is', $html, $m ) ) {
		return $m[1];
	}
	return $html;
}

function tec_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/* ---------------------------------------------------------------------------
 * 0. A regua independente — e ela tem de estar fresca
 * ------------------------------------------------------------------------- */

echo "Clube do Mosaico — verificacao das paginas de TECNICA\n";

$saida  = array();
$codigo = 0;
exec( 'python3 ' . escapeshellarg( __DIR__ . '/cobertura.py' ) . ' --conferir 2>&1', $saida, $codigo );
tec_ok( 0 === $codigo, 'dados/cobertura.json esta fresco (a regua independente vale)',
	trim( implode( ' ', $saida ) ) );
if ( 0 !== $codigo ) {
	echo "\nA regua independente esta velha. Rode `python3 ferramentas/cobertura.py` antes.\n";
	exit( 1 );
}

$cobertura = json_decode( (string) @file_get_contents( $raiz . '/dados/cobertura.json' ), true );
$colas     = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$tecnicas  = json_decode( (string) @file_get_contents( $raiz . '/dados/tecnicas.json' ), true );
if ( ! $cobertura || ! $colas || ! $tecnicas ) {
	echo "ERRO: nao consegui ler cobertura, banco de colas ou banco de tecnicas.\n";
	exit( 1 );
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "  (tecnicas " . CDM_TECNICAS_VERSAO . ", casca " . CDM_CASCA_VERSAO . ", F2 " . CDM_F2_VERSAO . ")\n\n";

/** O nome como a TELA o escreve, recalculado aqui: marca so quando falta. */
function tec_nome_esperado( $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return $nome;
	}

	return $marca . ' ' . $nome;
}

$por_id   = array();
$no_banco = array();
foreach ( $colas['materiais'] as $m ) {
	$por_id[ $m['id'] ] = $m;
	$no_banco[]         = $m['id'];
}

$registro = cdm_tecnicas_registro();

/* ---------------------------------------------------------------------------
 * 1. A FAMILIA: o registro do snippet e a bandeira do banco, nos DOIS sentidos
 *
 * `pagina_publicada` no banco e o que o `validar-banco.py` usa para cobrar o
 * portao de 3 itens; se ela ficar `false` com a pagina no ar, o portao para de
 * morder em silencio, e se ficar `true` sem pagina, o validador cobra um portao
 * de uma pagina que nao existe. Nenhum dos dois casos apareceria sem esta
 * afirmacao, porque cada metade esta certa sozinha.
 * ------------------------------------------------------------------------- */

echo "1. A familia das tecnicas (o registro x o banco)\n";

tec_ok( count( $registro ) >= 1, 'o snippet publica pelo menos uma tecnica', count( $registro ) . ' paginas' );

$registradas = apply_filters( 'cdm_tecnicas_publicadas', array() );
$ids_no_site = array();
foreach ( (array) $registradas as $r ) {
	$ids_no_site[] = $r['id'];
}
sort( $ids_no_site );
$ids_registro = array_keys( $registro );
sort( $ids_registro );
tec_ok( $ids_no_site === $ids_registro,
	'o filtro cdm_tecnicas_publicadas serve exatamente o registro',
	implode( ', ', $ids_no_site ) );

$discordam = array();
foreach ( $tecnicas['tecnicas'] as $t ) {
	$no_banco_bandeira = ! empty( $t['pagina_publicada'] );
	$no_site           = in_array( $t['id'], $ids_no_site, true );
	if ( $no_banco_bandeira !== $no_site ) {
		$discordam[] = $t['id'];
	}
}
tec_ok( empty( $discordam ), 'nenhuma tecnica tem a bandeira do banco discordando do snippet',
	empty( $discordam ) ? count( $tecnicas['tecnicas'] ) . ' tecnicas conferidas' : implode( ', ', $discordam ) );

/* O BANCO DIZ DE SI MESMO QUE E PUBLICADO, e o manifest tem de concordar.
   Estas duas metades ficaram em desacordo desde 14/09/2026 sem nenhum sinal: o
   `publicacao.publicar` do arquivo dizia `false` com o motivo "nenhum snippet le
   este arquivo", escrito antes de a primeira pagina existir, enquanto o manifest
   ja gravava a option que a pagina le. Cada uma estava certa no dia em que foi
   escrita — e e sempre assim que esta divergencia nasce. */
$manifest    = json_decode( (string) @file_get_contents( $raiz . '/manifest.json' ), true );
$no_manifest = null;
foreach ( ( isset( $manifest['dados'] ) ? $manifest['dados'] : array() ) as $d ) {
	if ( 'tecnicas' === $d['id'] ) {
		$no_manifest = ! empty( $d['publicar'] );
	}
}
tec_ok( null !== $no_manifest && $no_manifest === ! empty( $tecnicas['publicacao']['publicar'] ),
	'o banco e o manifest concordam que dados/tecnicas.json vai ao ar',
	'manifest ' . ( $no_manifest ? 'true' : 'false' )
		. ', arquivo ' . ( ! empty( $tecnicas['publicacao']['publicar'] ) ? 'true' : 'false' ) );

$urls_erradas = array();
foreach ( $tecnicas['tecnicas'] as $t ) {
	if ( empty( $t['pagina_publicada'] ) ) {
		continue;
	}
	$esperada = '/' . $registro[ $t['id'] ]['slug'] . '/';
	if ( ( isset( $t['pagina_publicada_url'] ) ? $t['pagina_publicada_url'] : '' ) !== $esperada ) {
		$urls_erradas[] = $t['id'];
	}
}
tec_ok( empty( $urls_erradas ), 'a URL que o banco publica e a que o snippet registra',
	empty( $urls_erradas ) ? count( $ids_no_site ) . ' URLs' : implode( ', ', $urls_erradas ) );

/* DUAS PAGINAS NAO SAO A MESMA PAGINA. Molde repetido e o caminho mais curto
   para malha fina, e ele nao da sinal nenhum: cada pagina, sozinha, esta certa. */
$campos_unicos = array( 'slug', 'titulo', 'linha_mestra', 'description', 'resumo', 'o_que_muda' );
$colisoes      = array();
foreach ( $campos_unicos as $campo ) {
	$vistos = array();
	foreach ( $registro as $id => $ficha ) {
		$valor = isset( $ficha[ $campo ] ) ? $ficha[ $campo ] : '';
		if ( '' === $valor || isset( $vistos[ $valor ] ) ) {
			$colisoes[] = $campo . ' (' . $id . ')';
		}
		$vistos[ $valor ] = true;
	}
}
tec_ok( empty( $colisoes ), 'nenhuma pagina de tecnica repete o texto de outra',
	empty( $colisoes ) ? count( $campos_unicos ) . ' campos x ' . count( $registro ) . ' paginas' : implode( ', ', $colisoes ) );

/* ---------------------------------------------------------------------------
 * 2 em diante: TUDO se repete em cada pagina
 * ------------------------------------------------------------------------- */

$defs   = cdm_casca_definicao_paginas();
$arvore = cdm_casca_arvore();

foreach ( $registro as $id => $ficha ) {

	echo "\n=== " . $ficha['titulo'] . " (/" . $ficha['slug'] . "/)\n";

	/* O registro do banco, lido do ARQUIVO — nunca da funcao do snippet. */
	$reg = null;
	foreach ( $tecnicas['tecnicas'] as $t ) {
		if ( $id === $t['id'] ) {
			$reg = $t;
		}
	}

	echo "\n2. A tecnica sai do banco (secao 10: nunca invente dado)\n";

	tec_ok( is_array( $reg ), 'a tecnica desta pagina existe em dados/tecnicas.json', $id );
	tec_ok( is_array( $reg ) && ! empty( $reg['materiais_tipicos'] ),
		'ela declara o material do caquinho, que e o que liga a pagina ao banco',
		is_array( $reg ) ? implode( ', ', (array) $reg['materiais_tipicos'] ) : '' );

	$tesselas_banco = ( is_array( $reg ) && ! empty( $reg['materiais_tipicos'] ) )
		? array_values( (array) $reg['materiais_tipicos'] ) : array();
	tec_ok( $tesselas_banco === cdm_tecnicas_tesselas( $id ),
		'a pagina resolve TODOS os caquinhos que o banco declara, nao um escrito no snippet',
		implode( ', ', $tesselas_banco ) );

	/* O SLUG E A CONSULTA-ALVO DO BANCO, sem acento e com hifen. Era assim que a
	   pagina do Picassiete nasceu, e sem esta afirmacao a proxima nasceria com o
	   slug que quem escreve achar melhor — que e como a ilha perde a unica
	   ligacao entre o endereco e a busca medida. */
	$consulta = isset( $reg['consulta_alvo'] ) ? (string) $reg['consulta_alvo'] : '';
	$slug_final = substr( $ficha['slug'], strrpos( $ficha['slug'], '/' ) + 1 );
	tec_ok( '' !== $consulta && str_replace( ' ', '-', $consulta ) === $slug_final,
		'o slug e a consulta-alvo do banco, com hifen no lugar do espaco',
		$consulta . ' -> ' . $slug_final );
	tec_ok( isset( $reg['serp_classe'] ) && 'ABERTA' === $reg['serp_classe'],
		'a SERP desta consulta foi classificada ABERTA antes da pagina (secao 14)',
		( isset( $reg['serp_lida_em'] ) ? 'lida em ' . $reg['serp_lida_em'] : '' ) );

	/* O PORTAO DA SECAO 9, RECONTADO AQUI a partir da cobertura, que e a metade
	   independente. A uniao e sobre TODOS os caquinhos da tecnica: e o que a
	   pagina pode recomendar. */
	$celulas_por_tessela = array();
	$uniao               = array();
	foreach ( $tesselas_banco as $tessela ) {
		$celulas_por_tessela[ $tessela ] = array();
		foreach ( $cobertura['estados']['cola'] as $e ) {
			if ( $e['tessela'] !== $tessela ) {
				continue;
			}
			$celulas_por_tessela[ $tessela ][ $e['base'] . '|' . $e['ambiente'] ] = $e;
			foreach ( $e['elegiveis'] as $id_cola ) {
				$uniao[ $id_cola ] = true;
			}
		}
	}
	tec_ok( count( $uniao ) >= 3, 'o portao de 3 itens da secao 9 esta aberto para esta tecnica',
		count( $uniao ) . ' itens de banco' );

	/* O AGRUPAMENTO DOS CAQUINHOS, RECONTADO NA COBERTURA. E o numero de tabelas
	   que a pagina tem de servir. */
	$grupos_esperados = array();
	foreach ( $tesselas_banco as $tessela ) {
		$assinatura = array();
		foreach ( $celulas_por_tessela[ $tessela ] as $chave => $e ) {
			$lista = $e['elegiveis'];
			sort( $lista );
			$assinatura[] = $chave . '=' . implode( ',', $lista );
		}
		sort( $assinatura );
		$grupos_esperados[ implode( ';', $assinatura ) ][] = $tessela;
	}
	$n_grupos = count( $grupos_esperados );

	echo "\n3. A pagina na arvore (secao 16)\n";

	tec_ok( isset( $defs[ $ficha['slug'] ] ), 'o snippet registrou a propria pagina pelo filtro cdm_paginas', $ficha['slug'] );
	tec_ok( isset( $defs[ $ficha['slug'] ]['pai'] ) && 'como-fazer' === $defs[ $ficha['slug'] ]['pai'],
		'a pagina nasce com mae, e a mae e /como-fazer/' );
	tec_ok( isset( $defs['como-fazer'] ), 'a mae existe na definicao de paginas' );
	tec_ok( isset( $arvore[ $ficha['slug'] ] ), 'a pagina esta no mapa da arvore' );
	tec_ok( isset( $arvore[ $ficha['slug'] ]['rotulo'] ) && $ficha['titulo'] === $arvore[ $ficha['slug'] ]['rotulo'],
		'o degrau da trilha usa o mesmo nome (um nome por pagina)' );
	tec_ok( isset( $defs[ $ficha['slug'] ]['titulo'] ) && $ficha['titulo'] === $defs[ $ficha['slug'] ]['titulo'],
		'o H1 usa o mesmo nome' );
	tec_ok( mb_strlen( $ficha['titulo'] . ' — ' . CDM_CASCA_NOME_SITE ) <= 65,
		'o <title> com o sufixo do site cabe em 65 caracteres',
		mb_strlen( $ficha['titulo'] . ' — ' . CDM_CASCA_NOME_SITE ) . ' caracteres' );

	/* CADA PAGINA TEM O PROPRIO SHORTCODE. Sem isto a bancada — que descobre
	   quem esta medindo casando o shortcode com a definicao de paginas — mediria
	   a primeira duas vezes e a segunda nenhuma. */
	$tag = 'cdm_tecnica_' . $id;
	tec_ok( isset( $defs[ $ficha['slug'] ]['conteudo'] ) && '[' . $tag . ']' === $defs[ $ficha['slug'] ]['conteudo'],
		'a pagina serve um shortcode SO dela', $tag );
	tec_ok( isset( $GLOBALS['__shortcodes'][ $tag ] ), 'e esse shortcode esta registrado' );

	/* A MAE LISTA A FILHA (16.4a). Sem isto a pagina nasce orfa. */
	cdm_teste_rebobinar();
	$como_fazer = tec_corpo( cdm_teste_pagina( 'cdm_como_fazer' ) );
	tec_ok( false !== strpos( $como_fazer, '/' . $ficha['slug'] . '/' ),
		'a mae /como-fazer/ publica o link para a filha (16.4a)' );
	tec_ok( false !== strpos( $como_fazer, $ficha['titulo'] ),
		'e o cartao da mae usa o mesmo nome' );

	/* -----------------------------------------------------------------------
	 * 4. A GRADE x a metade independente
	 * --------------------------------------------------------------------- */

	echo "\n4. A grade da pagina x a cobertura gerada em Python\n";

	cdm_teste_rebobinar();
	$html  = cdm_teste_pagina( $tag );
	$corpo = tec_corpo( $html );
	$texto = tec_texto( $corpo );

	$tabelas = preg_match_all( '#<table class="cdm-tec-tabela"#i', $corpo );
	tec_ok( $tabelas === $n_grupos,
		'a pagina serve UMA tabela por grupo de caquinhos que decidem igual',
		$tabelas . ' tabelas, ' . $n_grupos . ' grupos na cobertura' );

	$divergem   = array();
	$sem_nenhum = 0;
	$com_minimo = 0;
	$servidas   = 0;
	$indice     = 0;
	foreach ( $grupos_esperados as $tesselas_do_grupo ) {
		$tessela = $tesselas_do_grupo[0];
		foreach ( $celulas_por_tessela[ $tessela ] as $chave => $e ) {
			list( $base, $ambiente ) = explode( '|', $chave );
			$c         = cdm_tecnicas_celula( $id, $indice, $base, $ambiente );
			$na_pagina = $c ? $c['elegiveis'] : array();
			sort( $na_pagina );
			$esperado = $e['elegiveis'];
			sort( $esperado );
			if ( $na_pagina !== $esperado ) {
				$divergem[] = $chave . ' (pagina: ' . implode( ',', $na_pagina ) . ' | cobertura: ' . implode( ',', $esperado ) . ')';
			}
			$servidas++;
			if ( 0 === count( $esperado ) ) {
				$sem_nenhum++;
			}
			if ( count( $esperado ) >= 3 ) {
				$com_minimo++;
			}
		}
		$indice++;
	}
	tec_ok( 45 * $n_grupos === $servidas, 'a cobertura tem 45 celulas por tabela servida',
		$servidas . ' celulas' );
	tec_ok( empty( $divergem ), 'cada celula servida bate com a regua independente',
		empty( $divergem ) ? $servidas . ' iguais' : implode( ' | ', array_slice( $divergem, 0, 3 ) ) );

	/* OS NUMEROS QUE A PAGINA AFIRMA sao os mesmos que a cobertura conta. Sem isto
	   a frase de resposta poderia envelhecer sozinha, que e o defeito que esta ilha
	   ja pagou com o cabecalho de pecas.json dizendo 32 com 35 no arquivo. */
	tec_ok( false !== strpos( $texto, 'Das ' . $servidas . ' combinações' ),
		'a frase de resposta diz o numero de combinacoes que a cobertura conta', $servidas );
	tec_ok( false !== strpos( $texto, $sem_nenhum . ' não têm nenhuma' ),
		'a frase de resposta diz quantas combinacoes ficam sem resposta', (string) $sem_nenhum );
	tec_ok( false !== strpos( $texto, $com_minimo . ' têm três ou mais' ),
		'a frase de resposta diz quantas chegam a tres opcoes', (string) $com_minimo );

	/* A pagina NOMEIA o caquinho que resolve, com o rotulo do vocabulario. */
	$rot = cdm_f2_rotulos();
	$sem_nome = array();
	foreach ( $tesselas_banco as $tessela ) {
		$rotulo = isset( $rot['tessela'][ $tessela ] ) ? mb_strtolower( $rot['tessela'][ $tessela ] ) : $tessela;
		if ( false === mb_stripos( $texto, $rotulo ) ) {
			$sem_nome[] = $tessela;
		}
	}
	tec_ok( empty( $sem_nome ), 'a pagina nomeia na tela cada caquinho que ela resolve',
		empty( $sem_nome ) ? count( $tesselas_banco ) . ' caquinhos' : implode( ', ', $sem_nome ) );

	/* COM MAIS DE UM CAQUINHO, A PAGINA DIZ QUANTAS COMBINACOES COMPAROU. Uma
	   tabela so, sem essa frase, deixa o leitor sem saber para qual caquinho
	   ela vale — e foi a pergunta que o proprio PROMPT.md mandou responder na
	   tela. */
	if ( count( $tesselas_banco ) > 1 ) {
		$comparadas = 45 * count( $tesselas_banco );
		tec_ok( false !== strpos( $texto, (string) $comparadas ),
			'com mais de um caquinho, a pagina diz quantas combinacoes comparou', $comparadas );
	}

	/* A TABELA PRE-RENDERIZADA existe no HTML SERVIDO, sem JavaScript (secao 5). */
	tec_ok( preg_match_all( '#<tr\b#i', $corpo ) >= 10 * $n_grupos,
		'a tabela pre-renderizada esta no HTML servido, com uma linha por superficie',
		preg_match_all( '#<tr\b#i', $corpo ) . ' linhas' );
	tec_ok( substr_count( $corpo, 'nenhum que o fabricante sustente' ) === $sem_nenhum,
		'a tabela escreve "nao ha" exatamente nas celulas vazias que a cobertura conta',
		substr_count( $corpo, 'nenhum que o fabricante sustente' ) . ' celulas' );

	/* -----------------------------------------------------------------------
	 * 5. A PRESTACAO DE CONTAS (secao 7) — a soma fecha com o BANCO
	 * --------------------------------------------------------------------- */

	echo "\n5. Prestacao de contas: a soma dos nomeados fecha com o banco (secao 7)\n";

	tec_ok( count( $no_banco ) > 0, 'o banco de colas foi contado do arquivo, nunca digitado',
		count( $no_banco ) . ' colas' );

	$nomeados = 0;
	$faltando = array();
	foreach ( $no_banco as $id_cola ) {
		$nome = tec_nome_esperado( $por_id[ $id_cola ] );
		if ( 0 === substr_count( $texto, $nome ) ) {
			$faltando[] = $id_cola;
			continue;
		}
		$nomeados++;
	}
	tec_ok( empty( $faltando ), 'cada cola do banco aparece na prosa da pagina, recomendada ou excluida',
		empty( $faltando ) ? $nomeados . ' de ' . count( $no_banco ) : implode( ', ', $faltando ) );

	/* A VITRINE SERVE EXATAMENTE O QUE A FRASE NOMEIA. Cartao de produto que a
	   frase nao nomeia e o defeito que a F2 desta ilha pagou em 12/09/2026. */
	preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $corpo, $cartoes );
	/* O CARTAO IMPRIME A MARCA E O NOME EM ETIQUETAS SEPARADAS — a marca num
	   <span> e o nome no <h3> —, entao casar pelo nome JUNTO (como a prosa o
	   escreve) nao acha cartao nenhum. Este teste casa pelo <h3>, que e onde o
	   nome comercial esta, e e por isso que ele le o banco em vez de confiar na
	   string da tela. */
	$ids_na_vitrine = array();
	foreach ( $cartoes[1] as $cartao ) {
		if ( ! preg_match( '#<h3>(.*?)</h3>#is', $cartao, $mh ) ) {
			continue;
		}
		$nome_no_cartao = html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' );
		foreach ( $no_banco as $id_cola ) {
			if ( $nome_no_cartao === (string) $por_id[ $id_cola ]['nome_comercial'] ) {
				$ids_na_vitrine[ $id_cola ] = true;
			}
		}
	}
	$esperado_vitrine = array_keys( $uniao );
	sort( $esperado_vitrine );
	$medido_vitrine = array_keys( $ids_na_vitrine );
	sort( $medido_vitrine );
	tec_ok( $esperado_vitrine === $medido_vitrine,
		'a vitrine serve exatamente as colas que a cobertura declara elegiveis',
		count( $medido_vitrine ) . ' cartoes' );

	$fora_esperado = array_values( array_diff( $no_banco, $esperado_vitrine ) );
	sort( $fora_esperado );
	$fora_nomeados = array();
	foreach ( $fora_esperado as $id_cola ) {
		if ( preg_match( '#<li><strong>' . preg_quote( tec_nome_esperado( $por_id[ $id_cola ] ), '#' ) . '</strong>#u', $corpo ) ) {
			$fora_nomeados[] = $id_cola;
		}
	}
	tec_ok( $fora_esperado === $fora_nomeados,
		'quem NAO entra e nomeado numa linha propria, com a causa',
		count( $fora_nomeados ) . ' de ' . count( $fora_esperado ) );
	tec_ok( count( $esperado_vitrine ) + count( $fora_esperado ) === count( $no_banco ),
		'a soma dos nomeados fecha com o tamanho do banco',
		count( $esperado_vitrine ) . ' + ' . count( $fora_esperado ) . ' = ' . count( $no_banco ) );

	/* CAUSA QUE O CODIGO SEPARA, O TEXTO SEPARA. O Durepoxi cai por silencio em 25
	   celulas E aparece com ressalva em 20 — escrever so uma das duas seria
	   inventar a outra. Os baldes sao contados sobre as celulas SERVIDAS, que e o
	   universo de que a frase da pagina fala. */
	foreach ( $fora_esperado as $id_cola ) {
		$baldes = array( 'ressalva' => 0, 'silencio' => 0, 'proibicao' => 0, 'condicao' => 0,
			'peca' => 0, 'amb_substrato' => 0, 'amb_produto' => 0 );
		foreach ( $grupos_esperados as $tesselas_do_grupo ) {
			foreach ( $celulas_por_tessela[ $tesselas_do_grupo[0] ] as $e ) {
				if ( in_array( $id_cola, $e['com_ressalva'], true ) ) { $baldes['ressalva']++; }
				if ( in_array( $id_cola, $e['eliminados_por_silencio'], true ) ) { $baldes['silencio']++; }
				if ( in_array( $id_cola, $e['eliminados_por_proibicao'], true ) ) { $baldes['proibicao']++; }
				if ( in_array( $id_cola, $e['eliminados_por_condicao'], true ) ) { $baldes['condicao']++; }
				/* O QUINTO BALDE (regra 7, 06/10/2026). Ele sai zerado nas duas
				   tecnicas servidas hoje e `array_filter` o descarta, entao a
				   afirmacao abaixo nao muda — mas no dia em que um produto com
				   proibicao de peca for elegivel numa dessas grades, esta linha
				   cobra que a pagina nomeie ESSA causa, em vez de somar a
				   recusa ao silencio. Balde que o calculo separa e o portao nao
				   conta e balde que a tela pode esquecer sem ninguem ver. */
				if ( in_array( $id_cola, $e['eliminados_por_proibicao_da_peca'], true ) ) { $baldes['peca']++; }
				/* O SEXTO E O SETIMO (regras 8 e 3). O primeiro sai zerado nestas
				   duas tecnicas hoje — a cimentcola cai pela regra 2 nas tesselas
				   delas — e o segundo NAO: os dois Cascola delimitam ambiente e
				   declaram as bases destas grades. Sem estas duas linhas, mover 29
				   entradas do silencio para o balde novo baixaria a contagem de
				   silencio da pagina sem nada cobrar a contagem nova, e o portao
				   ficaria verde sobre uma pagina que perdeu uma frase. */
				if ( in_array( $id_cola, $e['eliminados_por_ambiente_do_substrato'], true ) ) { $baldes['amb_substrato']++; }
				if ( in_array( $id_cola, $e['eliminados_por_ambiente_do_produto'], true ) ) { $baldes['amb_produto']++; }
			}
		}
		$quantas       = array_filter( $baldes );
		$todos_na_tela = true;
		foreach ( $quantas as $n ) {
			if ( false === strpos( $texto, 'em ' . $n . ' das ' . $servidas ) ) {
				$todos_na_tela = false;
			}
		}
		tec_ok( $todos_na_tela, 'a recusa de ' . $id_cola . ' nomeia TODAS as causas que o calculo separou',
			implode( ', ', array_map( function ( $k, $v ) { return $k . ' ' . $v; }, array_keys( $quantas ), $quantas ) ) );
	}

	/* -----------------------------------------------------------------------
	 * 6. A ESCADA DE COMPRA (secao 25 e secao 7)
	 * --------------------------------------------------------------------- */

	echo "\n6. Escada de compra: ninguem fica sem saida (secao 25.2)\n";

	$sem_saida = array();
	foreach ( $esperado_vitrine as $id_cola ) {
		$cartao = '';
		foreach ( $cartoes[1] as $c ) {
			if ( preg_match( '#<h3>(.*?)</h3>#is', $c, $mh )
				&& html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' ) === (string) $por_id[ $id_cola ]['nome_comercial'] ) {
				$cartao = $c;
			}
		}
		if ( '' === $cartao || false === strpos( $cartao, 'cdm-f2-compra' ) || ! preg_match( '#<a [^>]*class="cdm-f2-botao#i', $cartao ) ) {
			$sem_saida[] = $id_cola;
		}
	}
	tec_ok( empty( $sem_saida ), 'nenhum cartao da vitrine fica sem saida de compra',
		empty( $sem_saida ) ? count( $esperado_vitrine ) . ' com botao' : implode( ', ', $sem_saida ) );
	tec_ok( false === mb_stripos( $texto, 'link de loja em breve' ),
		'a frase proibida pela secao 7 nao aparece' );

	/* O `rel` SAI DO QUE O LINK E. Busca CRUA nao paga comissao e por isso nunca e
	   `sponsored` — chamar de patrocinado um link que nao paga seria mentir ao
	   leitor sobre a unica coisa que ele tem o direito de saber sobre nos. */
	preg_match_all( '#<a [^>]*class="[^"]*cdm-f2-botao-busca-crua[^"]*"[^>]*>#i', $corpo, $cruas );
	$crua_errada = 0;
	foreach ( $cruas[0] as $a ) {
		if ( false !== stripos( $a, 'sponsored' ) || false === stripos( $a, 'nofollow' ) ) {
			$crua_errada++;
		}
	}
	/* A MEDIDA DIZ QUANDO NAO MEDIU NADA, e isso foi achado em 06/10/2026 por
	   uma mutacao de `mutacoes-tecnicas-pagina.py` que PASSOU: ela troca o `rel`
	   da busca crua para `sponsored` e este portao nao via, porque a pagina de
	   tecnica nao serve NENHUM botao de busca crua — os sete itens de cola do
	   banco tem `url` ou `url_busca`, e o degrau 4 nunca aparece aqui. Entao
	   `0 === $crua_errada` era verdade de graca, e "0 links de busca crua"
	   passava por aprovacao. E a MESMA cicatriz que o `teste-f2.php` ja carrega
	   escrita, desde 25/09: caso que o banco pode deixar de produzir tem de ser
	   PRODUZIDO, nao esperado. O mundo que o produz esta no fim deste arquivo. */
	tec_ok( 0 === $crua_errada, 'a busca crua sai nofollow e NUNCA sponsored',
		$cruas[0]
			? count( $cruas[0] ) . ' links de busca crua'
			: 'ZERO links de busca crua nesta pagina — esta afirmacao nao mediu nada (ver o mundo so_crua no fim)' );

	preg_match_all( '#<a [^>]*rel="sponsored[^"]*"[^>]*>#i', $corpo, $pagos );
	tec_ok( count( $pagos[0] ) > 0, 'os links que rendem comissao saem sponsored',
		count( $pagos[0] ) . ' links' );
	tec_ok( false !== mb_stripos( $texto, 'comissão' ),
		'o aviso de comissao esta visivel na pagina (secao 7)' );

	/* A PROCEDENCIA E DISCRETA e vem DEPOIS do bloco de compra (secao 7, 10/09). */
	$ordem_certa = true;
	foreach ( $cartoes[1] as $c ) {
		$compra = strpos( $c, 'cdm-f2-compra' );
		$fonte  = strpos( $c, 'cdm-f2-fonte' );
		if ( false !== $fonte && false !== $compra && $fonte < $compra ) {
			$ordem_certa = false;
		}
	}
	tec_ok( $ordem_certa, 'o bloco de compra vem ANTES da prova de procedencia, em todo cartao' );

	/* -----------------------------------------------------------------------
	 * 7. A RECUSA, e a voz
	 * --------------------------------------------------------------------- */

	echo "\n7. A recusa nomeada e a voz (secoes 7 e 15)\n";

	tec_ok( false !== mb_stripos( $texto, 'O rejunte.' ),
		'a pagina diz, com todas as letras, que NAO responde o rejunte' );
	tec_ok( false !== mb_stripos( $texto, 'largura da junta' ),
		'e nomeia a causa que ela mediu: a folga em milimetro que nenhuma fonte declara' );

	/* AS RECUSAS DECLARADAS NA FICHA saem na tela, uma a uma. Recusa escrita no
	   registro e nao impressa e pior que recusa ausente: o arquivo diz que a
	   pagina avisa, e ela nao avisa. */
	foreach ( ( isset( $ficha['recusas_declaradas'] ) ? $ficha['recusas_declaradas'] : array() ) as $r ) {
		tec_ok( false !== mb_strpos( $texto, $r['titulo'] ),
			'a recusa declarada na ficha esta impressa na tela', $r['titulo'] );
	}

	$primeiro = '';
	if ( preg_match( '#<p class="cdm-linha-mestra">(.*?)</p>#is', $corpo, $m ) ) {
		$primeiro = tec_texto( $m[1] );
	}
	tec_ok( '' !== $primeiro, 'a pagina abre por uma promessa de uma linha', mb_substr( $primeiro, 0, 60 ) . '…' );
	tec_ok( $primeiro === $ficha['linha_mestra'], 'e a promessa e a desta pagina, nao a da irma' );

	/* OS TERMOS QUE O VOZ.md PROIBE no titulo e no primeiro paragrafo. A lista esta
	   escrita LA e copiada aqui de proposito: e regua, e regua se escreve no teste
	   (secao 8). */
	$proibidos = array( 'tessela', 'substrato', 'aderência', 'especificação', 'parâmetro', 'ficha técnica' );
	$achados   = array();
	foreach ( $proibidos as $p ) {
		if ( false !== mb_stripos( $ficha['titulo'], $p ) || false !== mb_stripos( $primeiro, $p ) ) {
			$achados[] = $p;
		}
	}
	tec_ok( empty( $achados ), 'nenhum termo proibido pelo VOZ.md no titulo nem no primeiro paragrafo',
		empty( $achados ) ? 'limpo' : implode( ', ', $achados ) );

	/* A PROCEDENCIA NAO ABRE A PAGINA: ela desce um paragrafo, marcada como prova. */
	tec_ok( false === mb_stripos( $primeiro, 'fabricante' ) && false === mb_stripos( $primeiro, 'Wikip' ),
		'a procedencia nao abre a pagina (15.2)' );
	tec_ok( false !== strpos( $corpo, 'cdm-prova' ), 'a camada de prova esta marcada no HTML' );
	tec_ok( false !== mb_stripos( $texto, 'não foi revisado' ),
		'a pagina diz que a revisao por quem faz mosaico ainda nao aconteceu' );

	/* -----------------------------------------------------------------------
	 * 8. Cabeca: description e JSON-LD
	 * --------------------------------------------------------------------- */

	echo "\n8. A cabeca da pagina (secao 5)\n";

	$desc = '';
	if ( preg_match( '#<meta name="description" content="(.*?)">#is', $html, $m ) ) {
		$desc = html_entity_decode( $m[1], ENT_QUOTES, 'UTF-8' );
	}
	tec_ok( '' !== $desc, 'a pagina serve meta description' );

	/* A PAGINA QUE DECLARA MOLDE TEM A DESCRIPTION PREENCHIDA PELA REGUA
	   INDEPENDENTE (02/10/2026), e os dois numeros nao vem do snippet: as colas
	   sao `$no_banco`, contadas do arquivo na secao 5 deste mesmo teste, e as
	   celulas sao `$servidas`, contadas da cobertura na secao 4. Se o snippet
	   preencher o molde com outro numero, as duas escritas discordam aqui — que
	   e a trava da secao 8 do contrato aplicada a etiqueta onde o clique se
	   decide. */
	$desc_esperada = isset( $ficha['description'] ) ? (string) $ficha['description'] : '';
	if ( ! empty( $ficha['description_molde'] ) ) {
		$desc_esperada = strtr( (string) $ficha['description_molde'], array(
			'{colas}'   => (string) count( $no_banco ),
			'{celulas}' => (string) $servidas,
		) );
	}
	tec_ok( $desc === $desc_esperada, 'e e a description DESTA pagina, com os numeros da regua independente',
		$desc === $desc_esperada ? 'igual' : 'servida: ' . $desc );

	/* MOLDE CRU NO AR E O UNICO JEITO DE ESTE BLOCO PIORAR O QUE VEIO CONSERTAR. */
	tec_ok( false === strpos( $desc, '{' ) && false === strpos( $desc, '%1$s' ),
		'a description servida nunca traz o molde cru' );
	tec_ok( empty( $ficha['description_molde'] ) || 1 === preg_match( '/\d/', $desc ),
		'a pagina que declara molde serve NUMERO na description (trava 3)' );

	/* A FAIXA E 120 A 160, e nao 200: e a faixa do item 4 do despacho de 28/09,
	   fechada em 02/10. O teto de 200 daqui era o de antes, e deixava passar
	   justamente os 192 caracteres que a pagina do Picassiete servia. */
	tec_ok( mb_strlen( $desc ) >= 120 && mb_strlen( $desc ) <= 160,
		'a description cabe na faixa de 120 a 160', mb_strlen( $desc ) . ' caracteres' );

	/* A FRASE SEM NUMERO, que e a saida da TRAVA 2 desta camada: a pagina que
	   declara molde declara TAMBEM uma `description` sem numero, e ela tem de
	   caber na mesma faixa. Medida na declaracao e nao no ar porque o mundo sem
	   banco desta camada nao se produz dentro do mesmo processo — a cobertura
	   fica em `static`. */
	if ( ! empty( $ficha['description_molde'] ) ) {
		$sem_numero = isset( $ficha['description'] ) ? (string) $ficha['description'] : '';
		tec_ok( mb_strlen( $sem_numero ) >= 120 && mb_strlen( $sem_numero ) <= 160,
			'a frase SEM numero tambem cabe na faixa de 120 a 160', mb_strlen( $sem_numero ) . ' caracteres' );
		tec_ok( 0 === preg_match( '/\d/', $sem_numero ) && false === strpos( $sem_numero, '{' ),
			'e ela nao traz numero nenhum nem molde' );
	}

	/* O TITULO INTEIRO, COM A CAUDA QUE A CASCA DECIDE (02/10/2026).
	   O Picassiete declara promessa e o Trencadis nao — por decisao escrita, para
	   a leitura seguinte ter uma pagina parada com que comparar. O teto e o da
	   casca, contado em caracteres DECODIFICADOS. */
	$titulo_servido = '';
	if ( preg_match( '#<title>(.*?)</title>#is', $html, $mt ) ) {
		$titulo_servido = html_entity_decode( $mt[1], ENT_QUOTES, 'UTF-8' );
	}
	tec_ok( 0 === strpos( $titulo_servido, $ficha['titulo'] ),
		'o <title> comeca pelo NOME da pagina, intocado', $titulo_servido );
	tec_ok( '' !== $titulo_servido && mb_strlen( $titulo_servido ) <= CDM_CASCA_TITULO_TETO,
		'o <title> cabe no teto da casca', mb_strlen( $titulo_servido ) . ' caracteres' );
	$tem_promessa = ( 'picassiette' === $id );
	tec_ok( $tem_promessa === ( 1 === preg_match( '/\d/', $titulo_servido ) ),
		'so a pagina que declara promessa serve digito no <title>',
		$tem_promessa ? 'picassiete promete' : 'trencadis fica como estava' );
	tec_ok( $tem_promessa !== ( false !== strpos( $titulo_servido, CDM_CASCA_NOME_SITE ) ),
		'a marca cede o lugar na que promete, e fica na que nao promete' );

	$ld = '';
	if ( preg_match( '#<script type="application/ld\+json" id="cdm-tecnicas-jsonld">(.*?)</script>#is', $html, $m ) ) {
		$ld = $m[1];
	}
	$grafo = json_decode( $ld, true );
	tec_ok( is_array( $grafo ), 'o JSON-LD desta pagina parseia' );

	$tipos = array();
	foreach ( ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
		$tipos[] = $no['@type'];
	}
	tec_ok( in_array( 'Article', $tipos, true ), 'o grafo publica Article' );
	tec_ok( in_array( 'FAQPage', $tipos, true ), 'o grafo publica FAQPage' );

	$url_artigo = '';
	foreach ( ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
		if ( 'Article' === $no['@type'] ) {
			$url_artigo = isset( $no['url'] ) ? $no['url'] : '';
		}
	}
	tec_ok( false !== strpos( $url_artigo, '/' . $ficha['slug'] . '/' ),
		'o Article aponta para o endereco DESTA pagina', $url_artigo );

	/* O FAQ DO SCHEMA E O MESMO DA TELA — uma fonte so. Schema que promete o que a
	   pagina nao diz e o que faz FAQPage virar spam. */
	$perguntas_schema = array();
	foreach ( ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
		if ( 'FAQPage' === $no['@type'] ) {
			foreach ( $no['mainEntity'] as $q ) {
				$perguntas_schema[] = $q['name'];
			}
		}
	}
	$fora_da_tela = array();
	foreach ( $perguntas_schema as $q ) {
		if ( false === strpos( $texto, $q ) ) {
			$fora_da_tela[] = $q;
		}
	}
	tec_ok( ! empty( $perguntas_schema ) && empty( $fora_da_tela ),
		'toda pergunta do FAQPage esta escrita na tela',
		count( $perguntas_schema ) . ' perguntas' );

	/* O ESCAPE DO "&" — a cicatriz de 08/09/2026. */
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $scripts );
	$entidades = 0;
	foreach ( $scripts[1] as $s ) {
		$entidades += substr_count( $s, '&#038;' );
	}
	tec_ok( 0 === $entidades, 'zero &#038; dentro de <script>' );
	tec_ok( false === strpos( $corpo, '&#038;' ) && false === strpos( $corpo, '&amp;#039;' ),
		'zero escape duplo no corpo servido' );
}

/* ---------------------------------------------------------------------------
 * PRODUZ O MUNDO DO DEGRAU 4
 *
 * Por que ele existe: ver o comentario da afirmacao da busca crua, na secao 6.
 * Sem este bloco, aquela afirmacao e verdadeira e vazia — e foi assim que uma
 * mutacao que troca `nofollow` por `sponsored` num link que NAO rende comissao
 * passou por este portao em 06/10/2026.
 * ------------------------------------------------------------------------- */

echo "\n9. PRODUZ O MUNDO: com so_crua=1 o degrau 4 volta a ser o botao do cartao\n";

/* O MUNDO SAI DE UM PROCESSO PROPRIO, e isso foi medido em duas voltas hoje.
   Primeiro esta secao tentou `$_GET['so_crua']`: aquele bloco mora DENTRO do
   guarda de linha de comando de `render-para-teste.php`
   (`basename(__FILE__) === basename($argv[0])`), e este arquivo o inclui por
   `require`, entao ele nunca roda neste caminho. Depois ela produziu o mundo A
   MAO nas options, no proprio processo, e continuou dando "0 botoes": o banco
   que a F2 serve vem de um `static` dentro de `cdm_f2_banco()`, ja carregado
   pelas oito secoes acima. Mundo produzido depois da primeira leitura nao
   alcanca quem ja leu. Por isso aqui e `exec`, como o `teste-f2.php` faz desde
   25/09 — e por isso a secao nao precisa mais vir no fim por ser destrutiva. */
$saida_crua  = array();
$codigo_crua = 0;
exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
	. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( 'cdm_tecnica_trencadis' )
	. ' ' . escapeshellarg( 'hoje' ) . ' ' . escapeshellarg( 'so_crua=1' ) . ' 2>/dev/null',
	$saida_crua, $codigo_crua );
$mundo_crua = 0 === $codigo_crua ? tec_corpo( implode( "\n", $saida_crua ) ) : '';
tec_ok( '' !== $mundo_crua, 'o processo do mundo so_crua serviu a pagina de tecnica',
	strlen( $mundo_crua ) . ' bytes' );
preg_match_all( '#<a [^>]*class="[^"]*cdm-f2-botao-busca-crua[^"]*"[^>]*>#i', $mundo_crua, $cruas_mundo );
$crua_mentindo = array();
foreach ( $cruas_mundo[0] as $a ) {
	if ( false !== stripos( $a, 'sponsored' ) || false === stripos( $a, 'nofollow' ) ) {
		$crua_mentindo[] = $a;
	}
}
tec_ok( count( $cruas_mundo[0] ) > 0,
	'o mundo so_crua produz botao de busca crua na pagina de tecnica',
	count( $cruas_mundo[0] ) . ' botoes' );
tec_ok( empty( $crua_mentindo ),
	'e nele a busca CRUA sai nofollow e NUNCA sponsored — ela nao rende comissao',
	empty( $crua_mentindo )
		? count( $cruas_mundo[0] ) . ' conferidos'
		: implode( ' | ', array_slice( $crua_mentindo, 0, 2 ) ) );

echo "\n";
if ( $falhas ) {
	echo "REPROVADO: $falhas falha(s) em $feitos verificacoes.\n";
	exit( 1 );
}
echo "APROVADO: $feitos verificacoes, nenhuma falha.\n";

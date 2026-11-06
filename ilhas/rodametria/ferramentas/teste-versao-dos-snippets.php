<?php
/**
 * A VERSAO DE CADA SNIPPET, DO REPOSITORIO ATE O AR — O ESPELHO E A AUSENCIA.
 *
 *   php ferramentas/teste-versao-dos-snippets.php
 *
 * POR QUE ELE NASCEU EM 02/11/2026. Em 30/10 esta ilha mediu, e esta no
 * REGISTRO.md daquele dia, que o comentario da vitrine afirmava que
 * "`atualizar-manifest.py` casa esta constante com o campo `versao` do manifest"
 * e que **nao casava, e nunca casou**: a palavra `versao` nao aparecia uma vez
 * naquela ferramenta e os itens de `snippets` nao tinham o campo.
 * `RODAMETRIA_PRODUTO_VERSAO` e `RODAMETRIA_F2_VERSAO` eram lidas por NINGUEM.
 * O que saiu naquela passada foi a frase que prometia um portao inexistente —
 * e o portao ficou pre-registrado como bloco, porque mexer no manifest e mexer
 * no CONTRATO DO SYNC, o unico canal desta ilha. Este arquivo e esse portao.
 *
 * A LICAO QUE ELE CARREGA E A DA 32.5-d: comentario que declara um mecanismo
 * parece conferido e nao mede nada. Subir uma constante que ninguem le e
 * rastro, nao mecanismo.
 *
 * AS DUAS COISAS QUE ELE SEPARA, e elas nao sao a mesma:
 *
 *   `sha256` do manifest   -> o BYTE que esta no repositorio.
 *   `versao` do manifest   -> QUAL VERSAO esse byte se declara ser.
 *   `/casca` -> `versoes`  -> qual versao o WORDPRESS CARREGOU de verdade.
 *
 * A terceira e a que o sha256 nao alcanca, e a cicatriz tem nome e preco: a
 * 20.4. O Sync grava o snippet INATIVO de proposito e ATIVA depois; quando a
 * ativacao falha ele escreve `gravado (#13) mas NAO ativado` numa linha do log,
 * **segue em frente e sobe a revisao**. Isso custou SETE PAGINAS servindo o
 * tema cru na clubedomosaico, DUAS VEZES em tres dias. O byte estava certo no
 * repositorio nas duas.
 *
 * POR QUE ELE E PHP E NAO PYTHON — o mesmo motivo escrito no
 * `teste-caixa-da-mae.php`, no `teste-nota-de-preco.php` e no
 * `teste-escada-de-compra.php`: a coleta e DECIDIDA em PHP
 * (`rodametria_casca_versoes()`, mais um `add_filter` em cada snippet), entao a
 * regua CHAMA a funcao com `add_filter` e `apply_filters` DE VERDADE. Regua em
 * Python sobre o texto do PHP conferiria a FORMA do codigo, nunca a decisao.
 *
 * E ELE EXISTE TAMBEM PARA NAO REPROVAR A PAGINA CERTA, que pela 20.5 e o
 * caminho mais curto para alguem ignorar um portao. O portao de ar le a ausencia
 * de um `id` no `/casca` como "snippet nao ativado". Essa leitura so e honesta
 * se for impossivel o `id` faltar por descuido do repositorio — e e isto que as
 * afirmacoes 3 e 7 aqui garantem, no chao, antes de o ar ser consultado.
 */

/* ---------------------------------------------------------------------------
   add_filter E apply_filters DE VERDADE. Nao sao enfeite: sao o mecanismo sob
   teste. O registro e por rodada, porque cada mundo fabricado precisa comecar
   limpo.
   --------------------------------------------------------------------------- */
$GLOBALS['REG'] = array();
function add_filter( $gancho, $cb, $p = 10, $n = 1 ) {
	$GLOBALS['REG'][ $gancho ][] = $cb;
	return true;
}
function apply_filters( $gancho, $valor ) {
	foreach ( ( isset( $GLOBALS['REG'][ $gancho ] ) ? $GLOBALS['REG'][ $gancho ] : array() ) as $cb ) {
		$valor = call_user_func( $cb, $valor );
	}
	return $valor;
}

$RAIZ     = dirname( __DIR__ );
$MANIFEST = json_decode( file_get_contents( $RAIZ . '/manifest.json' ), true );

/* OS IDS SAEM DO MANIFEST, E NAO DE UMA LISTA ESCRITA AQUI (06/11/2026).
 *
 * Esta linha era `array( 'rodametria-casca', 'rodametria-f2', 'rodametria-
 * produto', 'rodametria-institucional' )`, escrita a mao em 02/11/2026 quando a
 * ilha tinha exatamente esses quatro snippets. Em 06/11 a F1 nasceu e o portao
 * REPROVOU com a mensagem certa pelo motivo errado: *"o coletor devolve [4] e o
 * manifest publica [5]"*. O coletor estava certo — ele devolve o que esta lista
 * manda carregar — e a lista e que estava velha.
 *
 * E o defeito e mais feio do que parece, porque ele e ASSIMETRICO: snippet novo
 * faz a afirmacao 3 ficar VERMELHA (e isso e sorte, porque e ela que compara com
 * o manifest), mas as afirmacoes 1, 2 e 7 — *cada snippet define exatamente uma
 * constante*, *o manifest espelha a constante*, *cada snippet pendura algo em
 * `rodametria_versoes`* — simplesmente NAO ALCANCAM o snippet que falta na
 * lista, e isso passa em SILENCIO. Um snippet novo com duas constantes de versao,
 * ou com o manifest desespelhado, entraria no ar sem nenhuma dessas tres o ver.
 *
 * E a familia que esta ilha ja nomeou duas vezes: a `bancada.py` nasceu sem
 * lista de proposito (*"portao novo entra no dia em que e escrito"*), e a
 * `atualizar-manifest.py` se proibe de adivinhar a constante *"porque convencao
 * derivada de cabeca acerta em tres dos quatro snippets desta ilha e erra no
 * quarto, e erraria CALADA"*. A lista aqui era a mesma doenca com um dia a mais
 * de vida.
 *
 * A fonte certa e o manifest, que e o CONTRATO do Sync: se o snippet esta nele
 * com `publicar: true`, ele vai ao ar e portanto tem de ser medido. */
$IDS = array();
foreach ( $MANIFEST['snippets'] as $it ) {
	if ( ! empty( $it['publicar'] ) ) { $IDS[] = $it['id']; }
}
sort( $IDS );
$ARQ = array();
foreach ( $IDS as $id ) {
	$caminho = $RAIZ . '/snippets/' . $id . '.php';
	if ( ! is_readable( $caminho ) ) {
		/* DENUNCIA e nunca omissao: id no manifest sem arquivo no repositorio e o
		   Sync com ordem de instalar o que nao existe. */
		echo "REPROVADO: o manifest publica o snippet $id e nao existe snippets/$id.php\n";
		exit( 1 );
	}
	$ARQ[ $id ] = file_get_contents( $caminho );
}

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

/** O item de `snippets` do manifest, pelo id. */
function item_do_manifest( $m, $id ) {
	foreach ( $m['snippets'] as $it ) {
		if ( $it['id'] === $id ) { return $it; }
	}
	return null;
}

/** As constantes `*_VERSAO` que um snippet DEFINE. Lista, nunca uma so: zero e
 *  mais de uma sao as duas respostas erradas, e o portao as separa. */
function versoes_definidas( $src ) {
	preg_match_all( '/define\(\s*[\'"]([A-Z][A-Z0-9_]*_VERSAO)[\'"]\s*,\s*[\'"]([^\'"]+)[\'"]\s*\)/',
		$src, $m, PREG_SET_ORDER );
	$fora = array();
	foreach ( $m as $x ) { $fora[ $x[1] ] = $x[2]; }
	return $fora;
}

/** O bloco `add_filter( 'rodametria_versoes', ... );` inteiro, equilibrando
 *  parenteses a partir do abre de `add_filter`. */
function bloco_do_filtro( $src ) {
	$i = strpos( $src, "add_filter( 'rodametria_versoes'" );
	if ( false === $i ) { return null; }
	$j = strpos( $src, '(', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '(' === $src[ $k ] ) { $n++; }
		elseif ( ')' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	return substr( $src, $i, $k - $i + 1 ) . ';';
}

/** O corpo da funcao coletora da casca, RENOMEADA — PHP nao redefine funcao, e
 *  cada mundo fabricado precisa da sua. */
function coletor_renomeado( $src, $novo ) {
	$i = strpos( $src, 'function rodametria_casca_versoes(' );
	if ( false === $i ) { return null; }
	$j = strpos( $src, '{', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '{' === $src[ $k ] ) { $n++; }
		elseif ( '}' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	$corpo = substr( $src, $i, $k - $i + 1 );
	return str_replace( 'function rodametria_casca_versoes(', 'function ' . $novo . '(', $corpo );
}

/* As constantes de verdade, definidas UMA vez: elas nao mudam entre os mundos,
   e PHP nao as redefine. O mundo que precisa de versao divergente mexe no
   MANIFEST, que e o lado que de fato envelhece calado. */
foreach ( $IDS as $id ) {
	foreach ( versoes_definidas( $ARQ[ $id ] ) as $nome => $valor ) {
		if ( ! defined( $nome ) ) { define( $nome, $valor ); }
	}
}

$rodada = 0;
/**
 * Fabrica um mundo e DEVOLVE o que o coletor da casca responde nele.
 *
 * @param array $fontes  id => fonte PHP (ja mutada, se for o caso)
 */
function coletar( $fontes, $casca_src ) {
	global $rodada;
	$rodada++;
	$nome = 'coletar_r' . $rodada;
	$GLOBALS['REG'] = array();

	foreach ( $fontes as $id => $src ) {
		if ( 'rodametria-casca' === $id ) { continue; }
		$bloco = bloco_do_filtro( $src );
		if ( null !== $bloco ) { eval( $bloco ); }
	}
	$corpo = coletor_renomeado( $casca_src, $nome );
	if ( null === $corpo ) { return null; }
	eval( $corpo );

	return call_user_func( $nome );
}

/* =========================================================================
   1. CADA SNIPPET DEFINE EXATAMENTE UMA CONSTANTE DE VERSAO
   -------------------------------------------------------------------------
   Zero e mais de uma sao as duas respostas erradas, e as duas fariam o espelho
   do `atualizar-manifest.py` adivinhar. Ele se proibe de adivinhar; aqui a
   proibicao e medida.
   ========================================================================= */
$CONST_DE = array();
foreach ( $IDS as $id ) {
	$achadas = versoes_definidas( $ARQ[ $id ] );
	afirma( 1 === count( $achadas ),
		sprintf( '%s define %d constantes `*_VERSAO` (%s) e tinha de definir exatamente 1',
			$id, count( $achadas ), implode( ', ', array_keys( $achadas ) ) ?: 'nenhuma' ) );
	if ( 1 === count( $achadas ) ) {
		$CONST_DE[ $id ] = array( key( $achadas ), current( $achadas ) );
	}
}

/* =========================================================================
   2. O MANIFEST ESPELHA A CONSTANTE, SNIPPET POR SNIPPET
   ========================================================================= */
foreach ( $IDS as $id ) {
	$it = item_do_manifest( $MANIFEST, $id );
	afirma( is_array( $it ), sprintf( '%s nao esta em `snippets` do manifest', $id ) );
	if ( ! is_array( $it ) || ! isset( $CONST_DE[ $id ] ) ) { continue; }
	list( $nome, $valor ) = $CONST_DE[ $id ];
	afirma( isset( $it['versao'] ),
		sprintf( '%s nao tem o campo `versao` no manifest — o espelho de 02/11/2026 nao foi aplicado', $id ) );
	afirma( isset( $it['versao'] ) && $it['versao'] === $valor,
		sprintf( '%s: o manifest diz `versao` %s e o arquivo define %s = %s. Subir a constante sem '
			. 'reespelhar e exatamente o rastro-sem-mecanismo que este portao existe para proibir',
			$id, isset( $it['versao'] ) ? var_export( $it['versao'], true ) : '(ausente)', $nome, $valor ) );
}

/* =========================================================================
   3. O COLETOR DEVOLVE TODO SNIPPET `publicar: true`, E SO ELES
   -------------------------------------------------------------------------
   Esta e a afirmacao que torna HONESTA a leitura do portao de ar. Ele le `id`
   ausente no /casca como "snippet nao ativado" (20.4); isso so vale se o `id`
   nao puder faltar por descuido do repositorio.
   ========================================================================= */
$publicaveis = array();
foreach ( $MANIFEST['snippets'] as $it ) {
	if ( ! empty( $it['publicar'] ) ) { $publicaveis[] = $it['id']; }
}
sort( $publicaveis );

$vivo = coletar( $ARQ, $ARQ['rodametria-casca'] );
afirma( is_array( $vivo ), 'o coletor da casca nao devolveu lista nenhuma' );
$chaves = is_array( $vivo ) ? array_keys( $vivo ) : array();
afirma( $chaves === $publicaveis,
	sprintf( 'o coletor devolve [%s] e o manifest publica [%s] — `id` que falta aqui o portao de ar '
		. 'leria como snippet NAO ATIVADO, e seria alarme falso',
		implode( ', ', $chaves ), implode( ', ', $publicaveis ) ) );

/* 3b. ORDENADO: o `ksort` do coletor e contrato, porque o portao de ar compara
   listas e diferenca de ordem lida como diferenca de conteudo. */
$ordenado = $chaves;
sort( $ordenado );
afirma( $chaves === $ordenado, 'o coletor devolveu as chaves fora de ordem — o `ksort` nao rodou' );

/* =========================================================================
   4. O VALOR QUE O COLETOR DEVOLVE E O DO MANIFEST
   ========================================================================= */
foreach ( ( is_array( $vivo ) ? $vivo : array() ) as $id => $v ) {
	$it = item_do_manifest( $MANIFEST, $id );
	afirma( is_array( $it ) && isset( $it['versao'] ) && $it['versao'] === $v,
		sprintf( '%s: o coletor serve %s e o manifest declara %s', $id, var_export( $v, true ),
			$it && isset( $it['versao'] ) ? var_export( $it['versao'], true ) : '(ausente)' ) );
}

/* =========================================================================
   5. A CASCA SE SEMEIA, ENTAO ELA APARECE MESMO COM ZERO FILTRO PENDURADO
   -------------------------------------------------------------------------
   Mundo fabricado: nenhum snippet pendura nada. A casca tem de continuar la —
   ela e quem responde o endpoint, entao se ela estiver fora a lista inteira e
   suspeita e nao se pode culpar os outros.
   ========================================================================= */
$so_casca = coletar( array(), $ARQ['rodametria-casca'] );
afirma( is_array( $so_casca ) && array_keys( $so_casca ) === array( 'rodametria-casca' ),
	'com zero filtro pendurado o coletor tinha de devolver so a casca, e devolveu ['
	. implode( ', ', is_array( $so_casca ) ? array_keys( $so_casca ) : array() ) . ']' );

/* =========================================================================
   6. O /casca SERVE O CAMPO, SENAO NADA DISTO CHEGA AO AR
   ========================================================================= */
afirma( false !== strpos( $ARQ['rodametria-casca'], "'versoes'" )
	&& false !== strpos( $ARQ['rodametria-casca'], 'rodametria_casca_versoes()' ),
	'a resposta do /casca nao serve `versoes` chamando `rodametria_casca_versoes()` — o espelho '
	. 'pararia no repositorio e o ar seguiria sem regua' );

/* =========================================================================
   7. NINGUEM ESCREVE A VERSAO A MAO AO LADO DA CONSTANTE
   -------------------------------------------------------------------------
   Versao digitada ao lado de versao definida e a familia do NUMERO DE TELA
   DIGITADO, a cicatriz que esta ilha mais paga: as duas comecam iguais e so uma
   sobe.
   ========================================================================= */
foreach ( $IDS as $id ) {
	if ( 'rodametria-casca' === $id ) { continue; }
	$bloco = bloco_do_filtro( $ARQ[ $id ] );
	afirma( null !== $bloco, sprintf( '%s nao pendura nada em `rodametria_versoes`', $id ) );
	if ( null === $bloco ) { continue; }
	afirma( isset( $CONST_DE[ $id ] ) && false !== strpos( $bloco, $CONST_DE[ $id ][0] ),
		sprintf( '%s nao usa a propria constante no filtro', $id ) );
	afirma( ! preg_match( '/[\'"]\d+\.\d+\.\d+[\'"]/', $bloco ),
		sprintf( '%s escreve a versao como LITERAL dentro do filtro — numero digitado ao lado de '
			. 'numero definido sobe sozinho num dos dois lados', $id ) );
	afirma( false !== strpos( $bloco, "'" . $id . "'" ),
		sprintf( '%s nao se registra com o proprio `id` do manifest como chave', $id ) );
}

/* =========================================================================
   AS MUTACOES — trava que nunca falhou nao e trava
   ========================================================================= */
$mutacoes = array(

	'a chave do f2 deixa de ser o `id` do manifest' => function ( $ARQ, $MANIFEST ) {
		$ARQ['rodametria-f2'] = str_replace( "\$v['rodametria-f2']", "\$v['f2']",
			$ARQ['rodametria-f2'] );
		$v = coletar( $ARQ, $ARQ['rodametria-casca'] );
		$pub = array();
		foreach ( $MANIFEST['snippets'] as $it ) {
			if ( ! empty( $it['publicar'] ) ) { $pub[] = $it['id']; }
		}
		sort( $pub );
		return array_keys( $v ) === $pub;   // tem de dar false
	},

	'o produto escreve a versao como literal no lugar da constante' => function ( $ARQ, $MANIFEST ) {
		$bloco = bloco_do_filtro( $ARQ['rodametria-produto'] );
		$mutado = str_replace( 'RODAMETRIA_PRODUTO_VERSAO', "'9.9.9'", $bloco );
		return ! preg_match( '/[\'"]\d+\.\d+\.\d+[\'"]/', $mutado );
	},

	'o institucional para de pendurar o filtro' => function ( $ARQ, $MANIFEST ) {
		$bloco = bloco_do_filtro( $ARQ['rodametria-institucional'] );
		$ARQ['rodametria-institucional'] = str_replace( $bloco, '', $ARQ['rodametria-institucional'] );
		$v = coletar( $ARQ, $ARQ['rodametria-casca'] );
		return in_array( 'rodametria-institucional', array_keys( $v ), true );
	},

	'o manifest declara versao diferente da constante da casca' => function ( $ARQ, $MANIFEST ) {
		foreach ( $MANIFEST['snippets'] as $i => $it ) {
			if ( 'rodametria-casca' === $it['id'] ) { $MANIFEST['snippets'][ $i ]['versao'] = '0.0.1'; }
		}
		$it = item_do_manifest( $MANIFEST, 'rodametria-casca' );
		return $it['versao'] === RODAMETRIA_CASCA_VERSAO;
	},

	'o coletor da casca deixa de semear a propria casca' => function ( $ARQ, $MANIFEST ) {
		$ARQ['rodametria-casca'] = str_replace(
			"array( 'rodametria-casca' => RODAMETRIA_CASCA_VERSAO ) );",
			'array() );', $ARQ['rodametria-casca'] );
		$v = coletar( array(), $ARQ['rodametria-casca'] );
		return is_array( $v ) && array_keys( $v ) === array( 'rodametria-casca' );
	},

	'o /casca para de servir o campo `versoes`' => function ( $ARQ, $MANIFEST ) {
		$src = str_replace( "'versoes'      => rodametria_casca_versoes(),", '',
			$ARQ['rodametria-casca'] );
		return false !== strpos( $src, "'versoes'" )
			&& false !== strpos( $src, 'rodametria_casca_versoes()' );
	},
);

$mordeu = 0;
foreach ( $mutacoes as $nome => $mutante ) {
	$passou = $mutante( $ARQ, $MANIFEST );
	afirma( false === $passou, sprintf( 'MUTACAO SOBREVIVEU: %s', $nome ) );
	if ( false === $passou ) { $mordeu++; }
}

printf( "teste-versao-dos-snippets: %d afirmacoes · %d snippets · %d de %d mutacoes reprovadas · %d falha(s)\n",
	$afirmacoes, count( $IDS ), $mordeu, count( $mutacoes ), count( $falhas ) );
foreach ( $falhas as $f ) { print( "  REPROVADO: $f\n" ); }
exit( count( $falhas ) ? 1 : 0 );

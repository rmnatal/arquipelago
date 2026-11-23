<?php
/**
 * A DATA QUE CADA PAGINA PUBLICA, MEDIDA NO CHAO — o item 2 do despacho da ronda
 * de 04/11/2026.
 *
 *   php ferramentas/teste-data-da-pagina.php
 *
 * O QUE ELE EXISTE PARA IMPEDIR. A ronda de 04/11 mediu ZERO ocorrencia de
 * `dateModified` e ZERO de `datePublished` em todo o JSON-LD das 9 URLs desta
 * ilha — a ilha cujo produto E "o preco de hoje" nao tinha sinal de frescor na
 * camada que o Google e as IAs leem. O conserto foi um FILTRO
 * (`rodametria_data_da_pagina`): a casca serve o no `WebPage` e cada snippet
 * pendura nele a data que a PROPRIA pagina publica em prosa.
 *
 * POR QUE ELE E PHP E NAO PYTHON — o mesmo motivo escrito no
 * `teste-caixa-da-mae.php`, no `teste-rotas.php` e no
 * `teste-versao-dos-snippets.php`: a decisao mora em PHP, entao a regua CHAMA as
 * funcoes de verdade. Regua em Python sobre o TEXTO do PHP conferiria a forma do
 * codigo e nunca a decisao — e aqui a decisao e "de que campo sai a data desta
 * pagina".
 *
 * O QUE ELE MEDE, e nenhuma data e digitada aqui:
 *
 *   1. TODO SLUG QUE A ILHA SERVE RECEBE DATA. Os slugs nao sao uma lista deste
 *      arquivo: saem dos mesmos arquivos de dado de que o site sai — as quatro
 *      da 16.1 de `paginas-institucionais.json`, as de produto da vitrine, a da
 *      F2 e a mae das constantes dos snippets. Slug novo entra nesta regua no
 *      dia em que entra no site.
 *   2. A DATA VEM DO CAMPO CERTO. A esperada e LIDA do JSON (`gerado_em`,
 *      `colhido_em`), nunca escrita aqui: numero digitado em teste e a familia do
 *      numero de tela digitado, e passaria a divergir da fonte no dia seguinte.
 *   3. A MAE SERVE A MAIS RECENTE DAS FILHAS. `dateModified` responde "quando
 *      esta pagina mudou", e a mae muda no dia em que QUALQUER filha e recolhida.
 *      O mundo com datas DIVERGENTES e FABRICADO, porque o banco de hoje tem as
 *      duas filhas no mesmo dia (secao 8: "regua escrita para um mundo que nunca
 *      aconteceu nasce errada sem poder falhar").
 *   4. NADA ESTA GRAMPEADO: trocando a data na fonte, a resposta troca.
 *   5. SEM BANCO, A RESPOSTA E VAZIA — e e isso que faz a casca NAO imprimir o
 *      no. Cair no relogio do servidor publicaria "modificada hoje" em pagina que
 *      nao muda desde 30/10, que e a mentira que um sinal de frescor pode contar.
 *   6. A CASCA VALIDA O FORMATO: o filtro pode devolver qualquer coisa, e
 *      `rodametria_casca_data_da_pagina()` so deixa passar AAAA-MM-DD. Data mal
 *      formada e pior que data ausente — ela entra no dado estruturado e o
 *      buscador a le como quiser.
 */

foreach ( array( 'add_action', 'add_shortcode', 'register_activation_hook' ) as $f ) {
	if ( ! function_exists( $f ) ) { eval( "function $f(){ return true; }" ); }
}
if ( ! function_exists( 'esc_html' ) ) {
	function esc_html( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
	function esc_url( $s ) { return (string) $s; }
	function home_url( $p = '/' ) { return 'https://rodametria.com.br' . $p; }
	function wp_json_encode( $v ) { return json_encode( $v, JSON_UNESCAPED_UNICODE ); }
	function sanitize_key( $k ) { return strtolower( preg_replace( '/[^a-zA-Z0-9_\-]/', '', (string) $k ) ); }
}

/* O FILTRO DE VERDADE, com os callbacks DOS SNIPPETS. `apply_filters` roda a
   cadeia na ordem de registro, que e o que o WordPress faz e o que importa aqui:
   cada callback devolve `$data` intacto quando a pagina nao e dele. */
$GLOBALS['FILTROS'] = array();
function add_filter( $gancho, $cb, $p = 10, $n = 1 ) {
	$GLOBALS['FILTROS'][ $gancho ][] = $cb;
	return true;
}
function apply_filters( $gancho, $valor ) {
	$args = array_slice( func_get_args(), 2 );
	foreach ( ( isset( $GLOBALS['FILTROS'][ $gancho ] ) ? $GLOBALS['FILTROS'][ $gancho ] : array() ) as $cb ) {
		$valor = call_user_func_array( $cb, array_merge( array( $valor ), $args ) );
	}
	return $valor;
}

$RAIZ = dirname( __DIR__ );

/* O BANCO E O ARQUIVO DO REPOSITORIO, que e exatamente o que o Sync grava na
   option: `rodametria_dados_<id>` recebe o JSON inteiro daquele item do
   manifest. Ler o arquivo aqui nao e fingir o banco: e ler a MESMA fonte. */
$GLOBALS['BANCO_RAIZ'] = $RAIZ;
$GLOBALS['BANCO_TROCAS'] = array();
/* O MUNDO DAS FILHAS EM DIAS DIFERENTES e fabricado AQUI, na porta do banco, e
   roda num processo PROPRIO (`--divergente`). A razao e tecnica e vale escrita:
   `rdm_produto_vitrine()` guarda o resultado em `static`, entao trocar o dado
   depois da primeira leitura nao muda nada — e um teste que troca o mundo tarde
   mede o mundo velho e passa. */
$GLOBALS['DIVERGENTE'] = in_array( '--divergente', $GLOBALS['argv'], true );
/* AS DATAS DO MUNDO DIVERGENTE SAO DERIVADAS, UMA POR FILHA, E NAO UMA LISTA DE
   DUAS (16/11/2026). Elas eram `array( '2026-10-20', '2026-11-03' )`, escritas
   quando a secao tinha DUAS filhas, e a injecao abaixo so trocava a data das
   PRIMEIRAS tantas quantas a lista tivesse. No dia em que `/veiculos/moto-eletrica/`
   nasceu, a terceira filha ficou com a data REAL dela — a mais recente de todas —,
   a mae passou a servir essa, e as duas afirmacoes do mundo divergente
   reprovaram. O portao estava certo e o MUNDO dele estava velho: regua escrita
   para um mundo que nao existe mais passa verde ate o dia em que reprova a
   pagina certa (20.5). Derivada do numero de filhas, a lista nasce completa a
   cada passada e a quarta pagina nao a quebra. */
$GLOBALS['DIVERGENTE_DATAS'] = array();

/* O WORDPRESS NAO EXISTE AQUI, e `rdm_produto_declaradas_fora_da_vitrine()` —
   carregada desde 18/11/2026, porque o filtro da data a chama — pergunta a ele
   se a pagina esta publicada. O stub responde pelo MUNDO REAL desta ilha: toda
   pagina que a camada declarada nomeia e que ja nasceu esta no ar, e nenhuma foi
   despublicada. Em `$GLOBALS['NAO_EXISTEM']` entra o slug que um mundo
   especifico queira derrubar; vazio e o caso corrente. */
$GLOBALS['NAO_EXISTEM'] = array();
function rodametria_casca_url_do_slug( $slug ) {
	if ( in_array( $slug, $GLOBALS['NAO_EXISTEM'], true ) ) { return ''; }
	return 'https://rodametria.com.br/' . ltrim( (string) $slug, '/' ) . '/';
}

function rodametria_casca_banco( $id ) {
	if ( array_key_exists( $id, $GLOBALS['BANCO_TROCAS'] ) ) {
		return $GLOBALS['BANCO_TROCAS'][ $id ];
	}
	$arq = $GLOBALS['BANCO_RAIZ'] . '/dados/' . $id . '.json';
	if ( ! file_exists( $arq ) ) { return null; }
	$d = json_decode( file_get_contents( $arq ), true );
	if ( ! is_array( $d ) ) { return null; }
	if ( $GLOBALS['DIVERGENTE'] && defined( 'RODAMETRIA_ID_DADOS_VITRINE' )
		&& RODAMETRIA_ID_DADOS_VITRINE === $id && ! empty( $d['paginas'] ) ) {
		$GLOBALS['DIVERGENTE_DATAS'] = array();
		foreach ( array_keys( $d['paginas'] ) as $i ) {
			/* Uma semana de distancia entre filhas: datas DISTINTAS, validas e em
			   ordem crescente de indice, para `max()` ser sempre a ultima. */
			$data = gmdate( 'Y-m-d', strtotime( '2026-10-01 +' . ( $i * 7 ) . ' days' ) );
			$d['paginas'][ $i ]['colhido_em']  = $data;
			$GLOBALS['DIVERGENTE_DATAS'][ $i ] = $data;
		}
		/* A FILHA DEGRADADA ENTRA NO MUNDO DIVERGENTE (23/11/2026), porque desde
		   hoje ela TAMBEM move a data da mae. Sem esta linha o mundo fabricado
		   tinha as filhas com vitrine em outubro e a degradada no dia de hoje, e
		   o que ele mediria seria o calendario em vez da regra — a mae serviria
		   a data de verdade e a afirmacao reprovaria a pagina certa (20.5). A
		   degradada fica UMA SEMANA DEPOIS da ultima filha, de proposito: assim
		   ela e a mais recente e o mundo prova que a mae a ouve. */
		$i_ultima = count( $d['paginas'] );
		foreach ( array_keys( (array) ( isset( $d['nao_nasceram'] )
			? $d['nao_nasceram'] : array() ) ) as $j ) {
			$data = gmdate( 'Y-m-d',
				strtotime( '2026-10-01 +' . ( ( $i_ultima + $j ) * 7 ) . ' days' ) );
			$d['nao_nasceram'][ $j ]['colhido_em']    = $data;
			$d['nao_nasceram'][ $j ]['colhido_em_br'] = gmdate( 'd/m/Y', strtotime( $data ) );
			$GLOBALS['DIVERGENTE_DATAS'][]            = $data;
		}
		sort( $GLOBALS['DIVERGENTE_DATAS'] );
	}
	return $d;
}

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

/** Carrega UMA funcao de um snippet, equilibrando chaves. */
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

/** Carrega o `add_filter( '<gancho>', function(){...} )` de um snippet.
 *
 *  POR QUE NAO SERVE PROCURAR O MARCADOR NO TEXTO, e isto custou uma passada:
 *  `token_get_all()` parte o fonte em tokens, e NENHUM token contem
 *  "add_filter( 'rodametria_data_da_pagina'" — sao tres. Pior: o nome do gancho
 *  aparece ANTES no arquivo, dentro do `apply_filters()` da propria casca, e
 *  andar para tras dali acharia um `add_filter` de outro assunto. Entao a busca
 *  e por ESTRUTURA: o token do literal do gancho cujos dois tokens anteriores
 *  (fora espaco) sao `(` e `add_filter`. Depois disso os parenteses se
 *  equilibram com o tokenizador, que ja sabe o que e codigo e o que e
 *  comentario — pedir a resposta a quem sabe e mais curto que reimplementar a
 *  pergunta. */
function carregar_add_filter( $src, $gancho ) {
	$ts = token_get_all( $src );
	$texto = function ( $t ) { return is_array( $t ) ? $t[1] : $t; };
	$anteriores = function ( $ts, $i, $quantos ) use ( $texto ) {
		$saida = array();
		for ( $k = $i - 1; $k >= 0 && count( $saida ) < $quantos; $k-- ) {
			$tx = $texto( $ts[ $k ] );
			if ( '' === trim( $tx ) ) { continue; }
			$saida[] = trim( $tx );
		}
		return $saida;
	};

	foreach ( $ts as $i => $t ) {
		$tx = $texto( $t );
		if ( "'" . $gancho . "'" !== trim( $tx ) && '"' . $gancho . '"' !== trim( $tx ) ) { continue; }
		$antes = $anteriores( $ts, $i, 2 );
		if ( count( $antes ) < 2 || '(' !== $antes[0] || 'add_filter' !== $antes[1] ) { continue; }

		$ini = -1;
		for ( $k = $i; $k >= 0; $k-- ) {
			if ( 'add_filter' === trim( $texto( $ts[ $k ] ) ) ) { $ini = $k; break; }
		}
		if ( $ini < 0 ) { return false; }

		$prof  = 0;
		$fonte = '';
		for ( $k = $ini; $k < count( $ts ); $k++ ) {
			$tx = $texto( $ts[ $k ] );
			$fonte .= $tx;
			if ( '(' === $tx ) { $prof++; }
			elseif ( ')' === $tx ) { $prof--; if ( 0 === $prof ) { break; } }
		}
		eval( $fonte . ';' );
		return true;
	}

	return false;
}

$casca   = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );
$f1      = file_get_contents( $RAIZ . '/snippets/rodametria-f1.php' );
$f2      = file_get_contents( $RAIZ . '/snippets/rodametria-f2.php' );
$f3      = file_get_contents( $RAIZ . '/snippets/rodametria-f3.php' );
$produto = file_get_contents( $RAIZ . '/snippets/rodametria-produto.php' );
$inst    = file_get_contents( $RAIZ . '/snippets/rodametria-institucional.php' );

/* As CONSTANTES saem dos snippets, uma por uma, nunca copiadas para ca: a
   derivacao de cabeca erra calada (a licao do `RODAMETRIA_INST_VERSAO`). */
foreach ( array(
	array( 'RODAMETRIA_ID_DADOS_F2', $casca ),
	array( 'RODAMETRIA_ID_DADOS_PRODUTO', $produto ),
	array( 'RODAMETRIA_ID_DADOS_VITRINE', $produto ),
	array( 'RODAMETRIA_PRODUTO_SECAO', $produto ),
	array( 'RODAMETRIA_F2_SLUG', $f2 ),
	/* A F1 E A F3 ENTRARAM EM 23/11/2026, com os callbacks delas. */
	array( 'RODAMETRIA_ID_DADOS_F1', $f1 ),
	array( 'RODAMETRIA_F3_SLUG', $f3 ),
	array( 'RODAMETRIA_ID_DADOS_F3', $f3 ),
	array( 'RODAMETRIA_ID_DADOS_INST', $inst ),
) as $par ) {
	list( $nome, $src ) = $par;
	if ( ! preg_match( "/define\(\s*'" . $nome . "'\s*,\s*'([^']+)'\s*\)/", $src, $m ) ) {
		print( "teste-data-da-pagina: REPROVADO — nao achei a constante $nome no snippet\n" );
		exit( 1 );
	}
	if ( ! defined( $nome ) ) { define( $nome, $m[1] ); }
}

foreach ( array(
	array( 'rodametria_casca_data_da_pagina', $casca ),
	array( 'rdm_produto_piso', $produto ),
	array( 'rdm_produto_editorial', $produto ),
	array( 'rdm_produto_vitrine', $produto ),
	array( 'rdm_produto_paginas_prontas', $produto ),
	/* ACRESCENTADA EM 18/11/2026: o filtro da data ganhou o ramo da pagina que
	   existe e esta sem vitrine, e ele CHAMA esta funcao. Sem ela aqui o portao
	   morria com `Call to undefined function` e a bancada o classificava como
	   INERTE — que e o veredito certo e nao diz qual era a funcao. */
	array( 'rdm_produto_declaradas_fora_da_vitrine', $produto ),
	/* ACRESCENTADAS EM 23/11/2026, com a composicao pelo MAIS RECENTE: a
	   decisao de qual data vence saiu dos seis callbacks e virou UMA funcao da
	   casca, e `paginas_no_ar()` e quem diz quais filhas contam para a mae. */
	array( 'rodametria_casca_data_valida', $casca ),
	array( 'rodametria_casca_data_mais_recente', $casca ),
	array( 'rdm_produto_nao_nasceram', $produto ),
	array( 'rdm_produto_paginas_no_ar', $produto ),
	array( 'rodametria_f1_banco', $f1 ),
	array( 'rdm_inst_declarado', $inst ),
	array( 'rdm_inst_paginas', $inst ),
) as $par ) {
	$ok = carregar_funcao( $par[1], $par[0] );
	afirma( $ok, sprintf( 'nao achei a funcao %s nos snippets', $par[0] ) );
	if ( ! $ok ) {
		print( "teste-data-da-pagina: REPROVADO — " . end( $falhas ) . "\n" );
		exit( 1 );
	}
}

/* OS SEIS CALLBACKS, lidos dos SEIS snippets. Faltar UM e reprovacao e nao
   omissao tolerada: a pagina daquele snippet sairia sem `dateModified`, que e o
   defeito inteiro que este portao existe para pegar.

   ERAM QUATRO ATE 23/11/2026, E A FALTA DOS OUTROS DOIS ERA O DEFEITO INTEIRO
   DESTE PORTAO. A F1 e a F3 penduram data no mesmo filtro — a F1 na prioridade
   **9**, ou seja ANTES de todas — e este arquivo nao as carregava. Com isso ele
   media uma cadeia de quatro onde o ar roda uma de seis, e a diferenca nao era
   teorica: ele EXIGIA que a home servisse o `gerado_em` da F2 (2026-11-18) e o
   ar servia o da F1 (2026-11-11), sete dias mais velho, porque a F1 respondia
   primeiro e a guarda do primeiro-vence calava as outras. **O portao estava
   verde sobre a pagina errada**, que e a cegueira que a 32.5-b nomeia: "regua
   que nao varre todas certifica a pagina que o autor abriu". */
foreach ( array(
	array( 'casca', $casca ),
	array( 'f1', $f1 ),
	array( 'f2', $f2 ),
	array( 'f3', $f3 ),
	array( 'produto', $produto ),
	array( 'institucional', $inst ),
) as $par ) {
	$ok = carregar_add_filter( $par[1], 'rodametria_data_da_pagina' );
	afirma( $ok, sprintf( 'o snippet %s nao pendura nada em `rodametria_data_da_pagina`', $par[0] ) );
}
afirma( 6 === count( isset( $GLOBALS['FILTROS']['rodametria_data_da_pagina'] )
	? $GLOBALS['FILTROS']['rodametria_data_da_pagina'] : array() ),
	sprintf( 'a cadeia do filtro tem %d callback(s) e os snippets desta ilha sao 6',
		count( isset( $GLOBALS['FILTROS']['rodametria_data_da_pagina'] )
			? $GLOBALS['FILTROS']['rodametria_data_da_pagina'] : array() ) ) );

/* ------------------------------------------------------------------ 1 e 2 */
$dados_f2   = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );
$dados_inst = rodametria_casca_banco( RODAMETRIA_ID_DADOS_INST );
$dados_vit  = rodametria_casca_banco( RODAMETRIA_ID_DADOS_VITRINE );

$dados_f1   = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F1 );
$dados_f3   = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F3 );

/* A ESPERADA DE CADA PAGINA E A MAIS RECENTE ENTRE AS FONTES DELA, e nao a de
   uma fonte escolhida a mao (23/11/2026). A home e feita de DOIS bancos — a F1
   ocupa a primeira tela e os tres numeros dela sao contados do banco da F2 —,
   entao ela muda quando o mais novo dos dois muda. Esta linha dizia
   `$dados_f2['gerado_em']` e o ar servia a data da F1; as duas estavam erradas
   pela mesma razao, que e tratar "de que dado a pagina e feita" como se fosse
   "quando a pagina mudou". */
$esperado = array();
$esperado['inicio']              = max( (string) $dados_f1['gerado_em'],
                                        (string) $dados_f2['gerado_em'] );
$esperado[ RODAMETRIA_F2_SLUG ]  = (string) $dados_f2['gerado_em'];
$esperado[ RODAMETRIA_F3_SLUG ]  = (string) $dados_f3['gerado_em'];
foreach ( $dados_inst['paginas'] as $pg ) {
	$esperado[ (string) $pg['slug'] ] = (string) $dados_inst['gerado_em'];
}
$datas_das_filhas = array();
foreach ( $dados_vit['paginas'] as $pg ) {
	$pedacos = explode( '/', (string) $pg['slug'] );
	$esperado[ (string) end( $pedacos ) ] = (string) $pg['colhido_em'];
	$datas_das_filhas[] = (string) $pg['colhido_em'];
}
/* A FILHA DEGRADADA TAMBEM TEM DATA E TAMBEM MOVE A MAE (23/11/2026): a data
   dela e a da ULTIMA TENTATIVA de coleta, e recolher sem alcancar o piso tambem
   e recolher. Ela entra pelo MESMO lugar de onde a casca a le — `nao_nasceram` —
   e so se estiver no ar, que e a trava de `paginas_no_ar()`. */
foreach ( (array) ( isset( $dados_vit['nao_nasceram'] ) ? $dados_vit['nao_nasceram'] : array() )
	as $r ) {
	if ( empty( $r['id'] ) || empty( $r['colhido_em'] ) ) { continue; }
	if ( ! isset( rdm_produto_paginas_no_ar()[ (string) $r['id'] ] ) ) { continue; }
	$esperado[ (string) $r['id'] ] = (string) $r['colhido_em'];
	$datas_das_filhas[]            = (string) $r['colhido_em'];
}
sort( $datas_das_filhas );
$esperado[ RODAMETRIA_PRODUTO_SECAO ] = (string) end( $datas_das_filhas );

afirma( count( $esperado ) >= 9,
	sprintf( 'a ilha serve 9 URLs e esta regua achou %d slug(s) nos arquivos de dado',
		count( $esperado ) ) );

foreach ( $esperado as $slug => $data ) {
	$servido = rodametria_casca_data_da_pagina( $slug );
	afirma( '' !== $servido,
		sprintf( '`%s` nao recebe data nenhuma: a pagina sairia sem `dateModified`', $slug ) );
	afirma( $servido === $data,
		sprintf( '`%s` serve a data %s e a fonte dela diz %s', $slug, $servido ?: '(vazia)', $data ) );
	afirma( 1 === preg_match( '/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/', (string) $servido ),
		sprintf( '`%s` serve %s fora do formato AAAA-MM-DD', $slug, $servido ) );
}

/* ------------------------------------------------------------------ 3 */
/* A MAE SERVE A MAIS RECENTE DAS FILHAS, e o mundo em que as duas discordam e
   FABRICADO: o banco de hoje tem as duas filhas no mesmo dia, e regua escrita
   para um mundo que nunca aconteceu nasce errada sem poder falhar (secao 8). */
if ( $GLOBALS['DIVERGENTE'] ) {
	$mais_nova = max( $GLOBALS['DIVERGENTE_DATAS'] );
	$mais_velha = min( $GLOBALS['DIVERGENTE_DATAS'] );
	afirma( $mais_nova === rodametria_casca_data_da_pagina( RODAMETRIA_PRODUTO_SECAO ),
		sprintf( 'com filhas em %s e %s, a mae serve %s e a mais recente e %s',
			$mais_velha, $mais_nova,
			rodametria_casca_data_da_pagina( RODAMETRIA_PRODUTO_SECAO ) ?: '(vazia)', $mais_nova ) );
	$vistas = array();
	foreach ( rdm_produto_paginas_no_ar() as $pg ) {
		$vistas[] = rodametria_casca_data_da_pagina( $pg['slug'] );
	}
	sort( $vistas );
	afirma( $vistas === $GLOBALS['DIVERGENTE_DATAS'],
		sprintf( 'as filhas deveriam servir %s e serviram %s',
			implode( ', ', $GLOBALS['DIVERGENTE_DATAS'] ), implode( ', ', $vistas ) ) );
	print( sprintf( "teste-data-da-pagina --divergente: %d afirmacoes, %d falha(s)\n",
		$afirmacoes, count( $falhas ) ) );
	foreach ( $falhas as $f ) { print( "  FALHA  $f\n" ); }
	print( count( $falhas ) ? "REPROVADO\n" : "APROVADO\n" );
	exit( count( $falhas ) ? 1 : 0 );
}

/* ------------------------------------------------------------------ 4, 5 e 6 */
/* Estes tres mundos nao dependem das funcoes `static` da vitrine: a home e a F2
   leem o banco da F2 a cada chamada. */
/* NADA ESTA GRAMPEADO: trocando `gerado_em` na fonte, a resposta troca. A
   TROCA E PARA O FUTURO de proposito (23/11/2026): com a composicao pelo MAIS
   RECENTE, trocar a data de UM banco para 2020 nao muda a resposta da home — e
   nao muda CERTO, porque o outro banco dela continua em 2026 e a pagina mudou
   naquele dia. A versao anterior destas duas linhas trocava para `2020-01-02` e
   exigia 2020 na tela: ela media o primeiro-vence, e passou a reprovar a
   resposta certa no minuto em que a regra virou o maximo. */
$f2_trocado = $dados_f2;
$f2_trocado['gerado_em'] = '2030-01-02';
$GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F2 ] = $f2_trocado;
afirma( '2030-01-02' === rodametria_casca_data_da_pagina( 'inicio' ),
	'trocando `gerado_em` da F2 para a data mais recente, a home nao a seguiu: ha data '
	. 'grampeada, ou o filtro da F2 esta sendo calado' );
afirma( '2030-01-02' === rodametria_casca_data_da_pagina( RODAMETRIA_F2_SLUG ),
	'trocando `gerado_em` na fonte, a F2 continuou servindo a data antiga: ha data grampeada' );

/* E O BANCO VELHO NAO PUXA A PAGINA PARA TRAS: a home e feita dos dois, e a
   mais recente e a que responde "quando esta pagina mudou". */
$f2_trocado['gerado_em'] = '2020-01-02';
$GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F2 ] = $f2_trocado;
afirma( (string) $dados_f1['gerado_em'] === rodametria_casca_data_da_pagina( 'inicio' ),
	'com a F2 em 2020 e a F1 em ' . $dados_f1['gerado_em'] . ', a home serve '
	. ( rodametria_casca_data_da_pagina( 'inicio' ) ?: '(vazia)' )
	. ' — a data de uma pagina e a MAIS RECENTE das fontes dela, nunca a mais velha' );

/* DADO MAL FORMADO NAO VENCE, NAO CONTAMINA E NAO APAGA O BOM. AAAA-MM-DD
   compara como texto, e `04/11/2026` compara MAIOR que qualquer ano — sem a
   validacao dos dois lados dentro de `data_mais_recente()`, ele venceria o
   maximo e depois seria descartado pelo validador do fim, deixando a pagina SEM
   data. A versao anterior desta afirmacao exigia cadeia vazia, porque com o
   primeiro-vence a cadeia TODA era aquele unico valor. */
$f2_torto = $dados_f2;
$f2_torto['gerado_em'] = '04/11/2026';
$GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F2 ] = $f2_torto;
afirma( (string) $dados_f1['gerado_em'] === rodametria_casca_data_da_pagina( 'inicio' ),
	'data em formato brasileiro num dos bancos levou a home para '
	. ( rodametria_casca_data_da_pagina( 'inicio' ) ?: '(vazia)' )
	. ': ela devia ser ignorada e a data boa da outra fonte devia ficar' );
afirma( false === strpos( (string) rodametria_casca_data_da_pagina( 'inicio' ), '/' ),
	'a data em formato brasileiro chegou a saida e iria para o dado estruturado' );

$GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F2 ] = null;
afirma( (string) $dados_f1['gerado_em'] === rodametria_casca_data_da_pagina( 'inicio' ),
	'faltando UM dos bancos da home, ela perdeu a data: banco ausente e uma fonte que '
	. 'nao contribui, nao um apagador do que as outras disseram' );

/* E SEM FONTE NENHUMA, A RESPOSTA E VAZIA — e e isso que faz a casca NAO
   imprimir o no. Cair no relogio do servidor publicaria "modificada hoje" em
   pagina que nao muda desde 30/10. */
$GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F1 ] = null;
afirma( '' === rodametria_casca_data_da_pagina( 'inicio' ),
	'sem NENHUM dos bancos, a home devolveu uma data: a casca inventou data e o no '
	. '`WebPage` sairia mentindo' );
unset( $GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F1 ] );
unset( $GLOBALS['BANCO_TROCAS'][ RODAMETRIA_ID_DADOS_F2 ] );

afirma( '' === rodametria_casca_data_da_pagina( 'slug-que-nao-existe-nesta-ilha' ),
	'slug que nao existe recebeu data' );
afirma( '' === rodametria_casca_data_da_pagina( '' ),
	'slug vazio recebeu data' );

/* ------------------------------------------------------------------ 7 */
/* A DISCORDANCIA DA 20.8, NO MUNDO MEDIDO E SO NELE (23/11/2026).

   A COMPOSICAO VELHA era o PRIMEIRO-VENCE: cada callback tinha a guarda
   `if ( '' !== $data ) return $data;`, e a F1 roda na prioridade 9, antes de
   todos. Ela esta reescrita aqui, e SO aqui, para uma coisa: provar que a nova
   DISCORDA dela na home. Portao que nao mostra a discordancia nao prova que o
   conserto conserta — prova que alguem escreveu codigo novo.

   O MUNDO MEDIDO E O DE HOJE, lido dos bancos e nunca digitado. No ar, em
   23/11/2026, a home servia o `dateModified` da F1 enquanto imprimia, no MESMO
   HTML, numeros contados do banco da F2 — mais novo. */
$velha_primeiro_vence = function ( $datas ) {
	foreach ( $datas as $d ) {
		if ( '' !== $d ) { return $d; }
	}
	return '';
};
/* A ORDEM E A DOS FILTROS: F1 (prioridade 9) antes da casca (10). */
$velha = $velha_primeiro_vence( array( (string) $dados_f1['gerado_em'],
                                       (string) $dados_f2['gerado_em'] ) );
$nova  = rodametria_casca_data_da_pagina( 'inicio' );
afirma( $dados_f1['gerado_em'] !== $dados_f2['gerado_em'],
	'os dois bancos da home estao no MESMO dia, e neste mundo as duas composicoes '
	. 'concordam — a discordancia desta metade so se mede quando eles divergem. Nao e '
	. 'falha do conserto: e aviso de que esta afirmacao parou de medir' );
if ( $dados_f1['gerado_em'] !== $dados_f2['gerado_em'] ) {
	afirma( $velha !== $nova,
		sprintf( 'a composicao velha e a nova tinham de DISCORDAR na home e as duas dizem %s',
			$nova ?: '(vazia)' ) );
	afirma( $nova === max( (string) $dados_f1['gerado_em'], (string) $dados_f2['gerado_em'] ),
		sprintf( 'a home serve %s e a mais recente das fontes dela e %s',
			$nova ?: '(vazia)', max( (string) $dados_f1['gerado_em'],
				(string) $dados_f2['gerado_em'] ) ) );
	afirma( $velha === (string) $dados_f1['gerado_em'],
		'a composicao velha nao esta reescrita fielmente: ela tinha de devolver a data da '
		. 'F1, que roda na prioridade 9' );
	print( sprintf( "  . a home: composicao VELHA diz %s (F1, primeiro-vence) e a NOVA diz %s "
		. "(a mais recente das duas fontes) — a discordancia vale o `dateModified` que "
		. "estava no ar\n", $velha, $nova ) );
}

/* E ELAS CONCORDAM ONDE TEM DE CONCORDAR: pagina de uma fonte so. Conserto que
   muda veredito fora do defeito e afrouxamento ou aperto nao pedido. */
afirma( (string) $dados_f3['gerado_em'] === rodametria_casca_data_da_pagina( RODAMETRIA_F3_SLUG ),
	'a F3 sai de um banco so e a composicao nova mudou a resposta dela' );
foreach ( $dados_inst['paginas'] as $pg ) {
	afirma( (string) $dados_inst['gerado_em']
		=== rodametria_casca_data_da_pagina( (string) $pg['slug'] ),
		sprintf( 'a institucional `%s` sai de um banco so e a composicao nova mudou a '
			. 'resposta dela', $pg['slug'] ) );
}

/* O MUNDO DIVERGENTE, num processo proprio (ver o comentario do banco). */
$saida = array();
$codigo = 0;
exec( sprintf( 'php %s --divergente 2>&1', escapeshellarg( __FILE__ ) ), $saida, $codigo );
afirma( 0 === $codigo,
	"o mundo das filhas em dias diferentes REPROVOU:\n         " . implode( "\n         ", $saida ) );
foreach ( $saida as $linha ) {
	if ( preg_match( '/--divergente: (\d+) afirmacoes/', $linha, $m ) ) {
		$afirmacoes += (int) $m[1];
	}
}

print( sprintf( "teste-data-da-pagina: %d afirmacoes, %d falha(s)\n", $afirmacoes, count( $falhas ) ) );
foreach ( $falhas as $f ) { print( "  FALHA  $f\n" ); }
print( count( $falhas ) ? "REPROVADO\n" : "APROVADO\n" );
exit( count( $falhas ) ? 1 : 0 );

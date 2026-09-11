<?php
/**
 * Verificacao MEDIDA da ARVORE da Robometria — secao 16 do ARQUIPELAGO.md.
 *
 *   php ferramentas/teste-arvore.php .
 *
 * TRES COISAS QUE ESTE ARQUIVO FAZ DE PROPOSITO, e cada uma e uma cicatriz:
 *
 *   1. UM PROCESSO POR PAGINA. A trilha tem uma trava `static` para nao sair duas
 *      vezes na MESMA requisicao. Num varredor que monta nove paginas em
 *      sequencia, essa trava faz a trilha aparecer na primeira e sumir nas oito
 *      seguintes — sem erro nenhum, com o teste verde. E a terceira vez que o
 *      Arquipelago paga por isso (Robometria 11/09, Clube do Mosaico 11/09),
 *      entao aqui cada pagina nasce num `php` proprio.
 *   2. A REGUA E DESTE ARQUIVO. Nada aqui chama robometria_casca_degraus() para
 *      conferir o que a pagina serve: as expectativas sao remontadas do ARVORE.md
 *      e do banco, e comparadas com o HTML. Chamar a regua de quem produziu o
 *      dado faria as duas metades errarem juntas.
 *   3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. O HTML completo
 *      carrega JSON-LD, e achar um texto dentro do proprio schema e o jeito mais
 *      facil de aprovar uma pagina que nao diz nada.
 *
 * E ele LE o ARVORE.md: documento e codigo mantidos a mao em dois lugares
 * divergem em silencio, e o documento e o que a proxima execucao vai ler.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function arv_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-64s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-64s %s\n", $rotulo, $medida );
	return false;
}

/** So o miolo: e sobre o CORPO que valem as afirmacoes de texto. */
function arv_corpo( $html ) {
	return preg_match( '#<main\b[^>]*>(.*)</main>#is', $html, $m ) ? $m[1] : '';
}

function arv_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/** Os degraus da trilha servida: rotulo, url ('' quando nao e link), e se e o atual. */
function arv_trilha_servida( $html ) {
	if ( ! preg_match( '#<nav class="rbm-trilha"[^>]*>(.*?)</nav>#is', $html, $m ) ) {
		return null;
	}
	preg_match_all( '#<li>(.*?)</li>#is', $m[1], $li );
	$degraus = array();
	foreach ( $li[1] as $bloco ) {
		if ( preg_match( '#<a href="([^"]+)"[^>]*>(.*?)</a>#is', $bloco, $a ) ) {
			$degraus[] = array( 'rotulo' => html_entity_decode( $a[2], ENT_QUOTES, 'UTF-8' ), 'url' => $a[1], 'atual' => false );
		} elseif ( preg_match( '#<span([^>]*)>(.*?)</span>#is', $bloco, $s ) ) {
			$degraus[] = array(
				'rotulo' => html_entity_decode( $s[2], ENT_QUOTES, 'UTF-8' ),
				'url'    => '',
				'atual'  => ( false !== strpos( $s[1], 'aria-current="page"' ) ),
			);
		}
	}
	return $degraus;
}

robometria_teste_carregar_options( $raiz );
robometria_teste_carregar( $raiz );
$GLOBALS['__paginas'] = robometria_teste_paginas_do_site();

echo "Robometria — verificacao da arvore (secao 16), casca " . ROBOMETRIA_CASCA_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 0. O ARVORE.md, lido como documento — as expectativas saem daqui.
 * ------------------------------------------------------------------------- */

echo "0. O documento (ARVORE.md) existe e e legivel\n";
$doc = @file_get_contents( $raiz . '/ARVORE.md' );
arv_ok( false !== $doc && strlen( $doc ) > 2000, 'ARVORE.md existe e tem conteudo', strlen( (string) $doc ) . ' bytes' );

/* Nivel 1: as linhas `| `/slug/` | ... |` da primeira tabela. */
preg_match_all( '#^\| `/([a-z0-9-]+)/` \|#m', (string) $doc, $m1 );
$doc_secoes = array_values( array_unique( $m1[1] ) );

/* Nivel 2: `| `/secao/cat/` | `/secao/` | ...` */
preg_match_all( '#^\| `/([a-z0-9-]+)/([a-z0-9-]+)/` \| `/([a-z0-9-]+)/` \|#m', (string) $doc, $m2 );
$doc_categorias = array();
foreach ( $m2[2] as $i => $cat ) {
	$doc_categorias[ $m2[1][ $i ] . '/' . $cat ] = $m2[3][ $i ];
}

/* Paginas de hoje: a tabela da secao 3, `| `slug` | papel | mae | destino | ...` */
preg_match_all( '#^\| `([a-z0-9-]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \|#m', (string) $doc, $m3 );
$doc_paginas = array();
foreach ( $m3[1] as $i => $slug ) {
	$doc_paginas[ $slug ] = array(
		'papel'   => trim( $m3[2][ $i ] ),
		'mae'     => trim( $m3[3][ $i ] ),
		'destino' => trim( $m3[4][ $i ] ),
	);
}

echo "\n1. O documento e o codigo dizem a mesma coisa\n";
$cod_secoes = array_keys( robometria_casca_secoes() );
sort( $doc_secoes );
$ordenado = $cod_secoes;
sort( $ordenado );
arv_ok( $doc_secoes === $ordenado, 'as secoes de nivel 1 do ARVORE.md sao as do codigo',
	implode( ' ', $doc_secoes ) . ' / ' . implode( ' ', $ordenado ) );

$cod_categorias = array();
foreach ( robometria_casca_categorias() as $slug => $par ) {
	/* O slug de uma categoria de guia carrega o prefixo no codigo (guias-pecas)
	   para nao colidir com a categoria de peca; no endereco ele e /guias/pecas/. */
	$nome = ( 0 === strpos( $slug, $par[0] . '-' ) ) ? substr( $slug, strlen( $par[0] ) + 1 ) : $slug;
	$cod_categorias[ $par[0] . '/' . $nome ] = $par[0];
}
ksort( $cod_categorias );
ksort( $doc_categorias );
arv_ok( $doc_categorias === $cod_categorias, 'as categorias de nivel 2 do ARVORE.md sao as do codigo',
	count( $doc_categorias ) . ' no documento / ' . count( $cod_categorias ) . ' no codigo' );

/* Toda categoria declarada tem que ter mae declarada como secao. */
$soltas = array();
foreach ( $cod_categorias as $caminho => $secao ) {
	if ( ! in_array( $secao, $cod_secoes, true ) ) { $soltas[] = $caminho; }
}
arv_ok( empty( $soltas ), 'nenhuma categoria com mae fora das secoes de nivel 1', implode( ' ', $soltas ) );

/* AS CATEGORIAS DE PECA SO EXISTEM COM PECA NO BANCO, e a regua e daqui: a
   categoria e o plural do tipo. "reservatorio" tem zero pecas no banco inteiro e
   por isso NAO pode estar declarado — e a 16.5 em forma de numero. */
$tipo_da_categoria = array(
	'filtros'            => 'filtro',
	'escovas-laterais'   => 'escova lateral',
	'escovas-principais' => 'escova principal',
	'mops'               => 'mop',
	'baterias'           => 'bateria',
	'reservatorios'      => 'reservatorio',
);
$pecas_json = json_decode( file_get_contents( $raiz . '/dados/pecas.json' ), true );
$por_tipo   = array();
foreach ( $pecas_json['registros'] as $p ) {
	if ( 'publicavel' !== $p['status'] ) { continue; }
	$por_tipo[ $p['tipo'] ] = isset( $por_tipo[ $p['tipo'] ] ) ? $por_tipo[ $p['tipo'] ] + 1 : 1;
}
/* Duas direcoes, e as duas importam (secao 8: a conferencia cobra os dois lados).
   (a) categoria declarada -> tem peca no banco;
   (b) tipo sem peca nenhuma -> NAO pode ter categoria declarada. */
$declaradas_sem_peca = array();
$declaradas          = 0;
foreach ( $cod_categorias as $caminho => $secao ) {
	if ( 'pecas' !== $secao ) { continue; }
	$cat = substr( $caminho, strlen( 'pecas/' ) );
	$declaradas++;
	$tipo = isset( $tipo_da_categoria[ $cat ] ) ? $tipo_da_categoria[ $cat ] : null;
	arv_ok( null !== $tipo, "a categoria /pecas/$cat/ corresponde a um tipo de peca conhecido" );
	if ( null === $tipo || empty( $por_tipo[ $tipo ] ) ) { $declaradas_sem_peca[] = $cat; }
}
arv_ok( empty( $declaradas_sem_peca ), 'toda categoria de peca declarada tem peca no banco (16.5)',
	$declaradas . ' declaradas / vazias: ' . ( $declaradas_sem_peca ? implode( ', ', $declaradas_sem_peca ) : 'nenhuma' ) );

$tipos_sem_peca = array();
foreach ( json_decode( file_get_contents( $raiz . '/dados/cobertura-r1.json' ), true )['resumo']['tipos_consultaveis'] as $tipo ) {
	if ( empty( $por_tipo[ $tipo ] ) ) { $tipos_sem_peca[] = $tipo; }
}
$proibidas = array();
foreach ( $tipos_sem_peca as $tipo ) {
	foreach ( $tipo_da_categoria as $cat => $t ) {
		if ( $t === $tipo && isset( $cod_categorias[ 'pecas/' . $cat ] ) ) { $proibidas[] = $cat; }
	}
}
arv_ok( empty( $proibidas ) && ! empty( $tipos_sem_peca ),
	'tipo sem peca nenhuma nao vira categoria, e a borda existe no banco de hoje',
	'tipos vazios: ' . ( $tipos_sem_peca ? implode( ', ', $tipos_sem_peca ) : 'NENHUM — esta afirmacao nao mede nada' ) );

/* As categorias de /modelos/ sao as marcas com modelo publicavel — contadas. */
$modelos_json = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$marcas_pub = array();
foreach ( $modelos_json['registros'] as $r ) {
	if ( 'publicavel' === $r['status'] ) { $marcas_pub[ $r['marca'] ] = true; }
}
$cat_modelos = array();
foreach ( $cod_categorias as $caminho => $secao ) {
	if ( 'modelos' === $secao ) { $cat_modelos[] = substr( $caminho, strlen( 'modelos/' ) ); }
}
sort( $cat_modelos );
$esperadas = array_keys( $marcas_pub );
sort( $esperadas );
arv_ok( $cat_modelos === $esperadas, 'as categorias de /modelos/ sao as marcas com modelo publicavel',
	implode( ' ', $cat_modelos ) . ' / ' . implode( ' ', $esperadas ) );

/* ---------------------------------------------------------------------------
 * 2. As nove paginas, cada uma no proprio processo.
 * ------------------------------------------------------------------------- */

$alvos = array( 'robometria_home', 'robometria_ferramentas', 'robometria_metodologia',
	'robometria_sobre', 'robometria_afiliados', 'robometria_r1', 'robometria_r2',
	'robometria_a1', 'robometria_a2' );

$html = array();
$slug_do_alvo = array();
foreach ( $alvos as $alvo ) {
	$slug = robometria_teste_slug_do_alvo( $alvo );
	$slug_do_alvo[ $alvo ] = $slug;
	$cmd = escapeshellarg( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $alvo );
	$html[ $alvo ] = (string) shell_exec( $cmd );
}

echo "\n2. Cada pagina saiu inteira do proprio processo\n";
foreach ( $alvos as $alvo ) {
	arv_ok( strlen( $html[ $alvo ] ) > 20000 && false !== strpos( $html[ $alvo ] , '</html>' ),
		"[$alvo] pagina montada", strlen( $html[ $alvo ] ) . ' bytes' );
	arv_ok( false !== strpos( $html[ $alvo ], 'rbm-rodape' ), "[$alvo] rodape servido" );
	arv_ok( 1 === preg_match_all( '#<h1\b#i', $html[ $alvo ] ), "[$alvo] um H1 e um so" );
}

/* PAGINA FINA NAO ENTRA NO INDICE DE DOMINIO NOVO (secao 8 do contrato). */
echo "\n3. Nenhuma pagina fina (corpo >= 1500 caracteres)\n";
foreach ( $alvos as $alvo ) {
	$texto = trim( html_entity_decode( strip_tags( arv_corpo( $html[ $alvo ] ) ), ENT_QUOTES, 'UTF-8' ) );
	arv_ok( mb_strlen( $texto, 'UTF-8' ) >= 1500, "[$alvo] corpo com tamanho de pagina",
		mb_strlen( $texto, 'UTF-8' ) . ' caracteres' );
}

/* ---------------------------------------------------------------------------
 * 4. A TRILHA (16.3).
 * ------------------------------------------------------------------------- */

echo "\n4. Trilha: onde ela esta, e onde ela nao esta\n";
arv_ok( 0 === preg_match_all( '#class="rbm-trilha"#', $html['robometria_home'] ),
	'a home NAO tem trilha (16.3)' );

$urls = array( 'robometria_home' => 'https://robometria.com.br/' );
foreach ( $alvos as $alvo ) {
	if ( 'robometria_home' === $alvo ) { continue; }
	$urls[ $alvo ] = 'https://robometria.com.br/' . $slug_do_alvo[ $alvo ] . '/';
}
$urls_validas = array_values( $urls );

foreach ( $alvos as $alvo ) {
	if ( 'robometria_home' === $alvo ) { continue; }
	$pagina = $html[ $alvo ];
	$corpo  = arv_corpo( $pagina );

	arv_ok( 1 === preg_match_all( '#class="rbm-trilha"#', $pagina ), "[$alvo] uma trilha, uma so" );

	$pos_trilha = strpos( $corpo, 'rbm-trilha' );
	$pos_h1     = strpos( $corpo, '<h1' );
	arv_ok( false !== $pos_trilha && false !== $pos_h1 && $pos_trilha < $pos_h1,
		"[$alvo] a trilha vem ANTES do H1" );

	$degraus = arv_trilha_servida( $pagina );
	arv_ok( is_array( $degraus ) && count( $degraus ) >= 2, "[$alvo] a trilha tem ao menos dois degraus",
		count( (array) $degraus ) . ' degraus' );

	$ultimo = end( $degraus );
	arv_ok( $ultimo['atual'] && '' === $ultimo['url'], "[$alvo] o degrau atual leva aria-current e nao e link" );

	/* O ultimo degrau e o titulo da pagina — o mesmo texto do H1 servido. */
	preg_match( '#<h1[^>]*>(.*?)</h1>#is', $pagina, $mh );
	$h1 = html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' );
	arv_ok( $ultimo['rotulo'] === $h1, "[$alvo] o degrau atual e o titulo da pagina", $ultimo['rotulo'] );

	arv_ok( 'Início' === $degraus[0]['rotulo'] && 'https://robometria.com.br/' === $degraus[0]['url'],
		"[$alvo] o primeiro degrau e a home, linkada" );

	/* NENHUM DEGRAU APONTA PARA PAGINA QUE NAO EXISTE. */
	$mortos = array();
	foreach ( $degraus as $d ) {
		if ( '' !== $d['url'] && ! in_array( $d['url'], $urls_validas, true ) ) { $mortos[] = $d['url']; }
	}
	arv_ok( empty( $mortos ), "[$alvo] nenhum degrau aponta para pagina inexistente", implode( ' ', $mortos ) );

	/* Rotulo repetido na mesma trilha e sintoma de mae que e a propria pagina. */
	$rotulos = array_column( $degraus, 'rotulo' );
	arv_ok( count( $rotulos ) === count( array_unique( $rotulos ) ), "[$alvo] nenhum rotulo repetido na trilha" );
}

/* A TRILHA QUE O ARVORE.md MANDA, remontada aqui a partir do documento. */
echo "\n5. A trilha servida e a que o ARVORE.md descreve\n";
$rotulo_da_secao = array( 'pecas' => 'Peças', 'succao' => 'Sucção', 'modelos' => 'Modelos', 'guias' => 'Guias' );
foreach ( $alvos as $alvo ) {
	if ( 'robometria_home' === $alvo ) { continue; }
	$slug = $slug_do_alvo[ $alvo ];
	if ( ! isset( $doc_paginas[ $slug ] ) ) {
		arv_ok( false, "[$alvo] o ARVORE.md descreve esta pagina" );
		continue;
	}
	$linha   = $doc_paginas[ $slug ];
	$degraus = arv_trilha_servida( $html[ $alvo ] );
	$vistos  = array_column( $degraus, 'rotulo' );

	if ( 'filha' !== $linha['papel'] ) {
		arv_ok( 2 === count( $vistos ), "[$alvo] pagina de $linha[papel]: dois degraus", implode( ' > ', $vistos ) );
		continue;
	}

	/* Mae de hoje: `/ferramentas/` ou `/guias/ (nao existe)`. Categoria: sai do
	   destino quando ele tem dois niveis. */
	preg_match( '#`/([a-z0-9-]+)/`#', $linha['mae'], $mm );
	$mae_slug   = isset( $mm[1] ) ? $mm[1] : '';
	$mae_existe = ( false === strpos( $linha['mae'], 'não existe' ) );
	$esperados  = array( 'Início' );
	$esperados[] = $mae_existe
		? robometria_casca_titulo_da_pagina( $mae_slug )
		: ( isset( $rotulo_da_secao[ $mae_slug ] ) ? $rotulo_da_secao[ $mae_slug ] : $mae_slug );

	if ( preg_match( '#`/([a-z0-9-]+)/([a-z0-9-]+)/`#', $linha['destino'], $md ) ) {
		$chave = $md[1] . '-' . $md[2];
		$cats  = robometria_casca_categorias();
		$esperados[] = isset( $cats[ $chave ] ) ? $cats[ $chave ][1] : $md[2];
	}
	preg_match( '#<h1[^>]*>(.*?)</h1>#is', $html[ $alvo ], $mh );
	$esperados[] = html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' );

	arv_ok( $vistos === $esperados, "[$alvo] os degraus sao os do documento",
		implode( ' > ', $vistos ) );

	/* Degrau de secao que nao existe sai em TEXTO, nunca em link. */
	if ( ! $mae_existe ) {
		arv_ok( '' === $degraus[1]['url'], "[$alvo] o degrau de secao inexistente nao e link" );
		arv_ok( false !== strpos( $html[ $alvo ], 'rbm-trilha-espera' ), "[$alvo] o degrau em espera e marcado no markup" );
	}
}

/* ---------------------------------------------------------------------------
 * 6. O BreadcrumbList (16.3) — e a regra que ele obedece.
 * ------------------------------------------------------------------------- */

echo "\n6. BreadcrumbList em JSON-LD\n";
arv_ok( false === strpos( $html['robometria_home'], 'BreadcrumbList' ), 'a home nao publica BreadcrumbList' );

foreach ( $alvos as $alvo ) {
	if ( 'robometria_home' === $alvo ) { continue; }
	$pagina = $html[ $alvo ];
	if ( ! preg_match( '#id="robometria-trilha-jsonld">(.*?)</script>#is', $pagina, $mj ) ) {
		arv_ok( false, "[$alvo] BreadcrumbList presente" );
		continue;
	}
	$dados = json_decode( $mj[1], true );
	arv_ok( is_array( $dados ) && 'BreadcrumbList' === $dados['@type'], "[$alvo] BreadcrumbList valido como JSON" );

	$itens = $dados['itemListElement'];
	$pos   = array_column( $itens, 'position' );
	arv_ok( $pos === range( 1, count( $itens ) ), "[$alvo] posicoes de 1 a N, sem buraco", implode( ',', $pos ) );

	/* NENHUM ListItem INTERMEDIARIO SEM `item` — e por isso que o degrau sem
	   endereco fica de fora: um item incompleto no meio invalida a lista inteira
	   para o Google, e lista invalida e lista ignorada. */
	$sem_item = 0;
	foreach ( $itens as $i => $item ) {
		if ( empty( $item['item'] ) ) { $sem_item++; }
	}
	arv_ok( 0 === $sem_item, "[$alvo] todo ListItem tem endereco", "$sem_item sem item" );

	/* O schema leva EXATAMENTE os degraus linkados da trilha, mais o atual. */
	$degraus  = arv_trilha_servida( $pagina );
	$atual    = array_pop( $degraus );
	$linkados = array();
	foreach ( $degraus as $d ) {
		if ( '' !== $d['url'] ) { $linkados[] = $d['rotulo']; }
	}
	$linkados[] = $atual['rotulo'];
	arv_ok( array_column( $itens, 'name' ) === $linkados,
		"[$alvo] o schema leva os degraus com endereco, mais o atual",
		implode( ' > ', array_column( $itens, 'name' ) ) );

	arv_ok( end( $itens )['item'] === $urls[ $alvo ], "[$alvo] o ultimo item do schema e a URL desta pagina" );
}

/* ---------------------------------------------------------------------------
 * 7. O CLUSTER (16.4): irmas, frase da mae, par ferramenta x guia.
 * ------------------------------------------------------------------------- */

echo "\n7. Veja tambem: irmas derivadas e frase da mae\n";
$filhas = array( 'robometria_r1', 'robometria_r2', 'robometria_a1', 'robometria_a2' );
$sem_cluster = array_diff( $alvos, $filhas );

foreach ( $sem_cluster as $alvo ) {
	arv_ok( false === strpos( $html[ $alvo ], 'class="rbm-veja"' ),
		"[$alvo] pagina fora da arvore nao tem Veja tambem" );
}

foreach ( $filhas as $alvo ) {
	$pagina = $html[ $alvo ];
	if ( ! preg_match( '#<nav class="rbm-veja".*?</nav>#is', $pagina, $mv ) ) {
		arv_ok( false, "[$alvo] bloco Veja tambem presente" );
		continue;
	}
	$bloco = $mv[0];
	preg_match_all( '#<li><a href="([^"]+)"[^>]*>(.*?)</a></li>#is', $bloco, $mi );
	$n = count( $mi[1] );
	arv_ok( $n >= 1 && $n <= 4, "[$alvo] de 1 a 4 irmas (teto do 16.4c)", "$n irma(s)" );

	$fora = array();
	foreach ( $mi[1] as $url ) {
		if ( ! in_array( $url, $urls_validas, true ) ) { $fora[] = $url; }
		if ( $url === $urls[ $alvo ] ) { $fora[] = 'a propria pagina'; }
	}
	arv_ok( empty( $fora ), "[$alvo] toda irma e uma pagina que existe, e nunca ela mesma", implode( ' ', $fora ) );

	/* A FRASE DA MAE (16.4b) so sai com mae publicada — e o numero dela e CONTADO.
	   A contagem daqui e propria: ferramentas com pagina no mapa do site. */
	$e_ferramenta = in_array( $alvo, array( 'robometria_r1', 'robometria_r2' ), true );
	$tem_frase    = ( false !== strpos( $bloco, 'rbm-veja-mae' ) );
	arv_ok( $e_ferramenta === $tem_frase,
		"[$alvo] frase da mae presente so quando a mae existe", $tem_frase ? 'presente' : 'ausente' );

	if ( $e_ferramenta ) {
		$quantas = 0;
		foreach ( robometria_casca_ferramentas() as $f ) {
			if ( ! empty( $f['slug'] ) && isset( $GLOBALS['__paginas'][ $f['slug'] ] )
				&& isset( $f['estado'] ) && 'publicada' === $f['estado'] ) {
				$quantas++;
			}
		}
		arv_ok( false !== strpos( $bloco, '>' . $quantas . ' ferramentas que já estão no ar</a>' ),
			"[$alvo] a frase da mae leva o numero contado", "$quantas no ar" );
	}
}

echo "\n8. O par ferramenta x guia (16.4d), nos dois sentidos\n";
/* A regua: o campo `ferramenta` de cada artigo nomeia o titulo da ferramenta que
   ele apoia. O par tem que aparecer no CORPO das duas paginas. Ate 11/09/2026 a
   ferramenta de succao linkava o guia da OUTRA e nao o seu, e nenhum teste
   perguntava se o guia era o CERTO. */
$titulo_da_ferramenta = array();
foreach ( robometria_casca_ferramentas() as $f ) {
	if ( ! empty( $f['slug'] ) ) { $titulo_da_ferramenta[ $f['titulo'] ] = $f['slug']; }
}
$corpo_por_slug = array();
foreach ( $alvos as $alvo ) { $corpo_por_slug[ $slug_do_alvo[ $alvo ] ] = arv_corpo( $html[ $alvo ] ); }

foreach ( robometria_casca_artigos() as $a ) {
	$par = isset( $titulo_da_ferramenta[ $a['ferramenta'] ] ) ? $titulo_da_ferramenta[ $a['ferramenta'] ] : '';
	arv_ok( '' !== $par, "artigo {$a['codigo']}: o campo 'ferramenta' nomeia uma ferramenta do catalogo", $a['ferramenta'] );
	if ( '' === $par ) { continue; }
	$url_artigo    = 'https://robometria.com.br/' . $a['slug'] . '/';
	$url_ferramenta = 'https://robometria.com.br/' . $par . '/';
	arv_ok( false !== strpos( $corpo_por_slug[ $par ], $url_artigo ),
		"a ferramenta $par linka o guia {$a['codigo']} no corpo" );
	arv_ok( false !== strpos( $corpo_por_slug[ $a['slug'] ], $url_ferramenta ),
		"o guia {$a['codigo']} linka a ferramenta $par no corpo" );
}

echo "\n9. Nenhuma pagina orfa (16.4f: ao menos dois links internos)\n";
foreach ( $alvos as $alvo ) {
	$alvo_url = $urls[ $alvo ];
	$quantas  = 0;
	foreach ( $alvos as $outro ) {
		if ( $outro === $alvo ) { continue; }
		$pagina = $html[ $outro ];
		/* A home nunca e contada pelo endereco absoluto sozinho: ela e prefixo de
		   todos os outros. Conta so href exatamente igual. */
		$quantas += preg_match_all( '#href="' . preg_quote( $alvo_url, '#' ) . '"#', $pagina );
	}
	arv_ok( $quantas >= 2, "[$alvo] tem ao menos dois links internos apontando para ela", "$quantas links" );
}

echo "\n10. Higiene: entidades dentro de <script> (secao 8)\n";
foreach ( $alvos as $alvo ) {
	$n = substr_count( arv_scripts( $html[ $alvo ] ), '&#038;' );
	arv_ok( 0 === $n, "[$alvo] zero &#038; dentro de <script>", "achados: $n" );
}

/* ---------------------------------------------------------------------------
 * 11. A BORDA FABRICADA.
 *
 * Com duas ferramentas no ar, NENHUMA pagina chega a ter cinco irmas candidatas
 * — entao trocar o teto de 4 por 5, ou por 40, nao mudaria uma linha do que o
 * site serve, e o portao ficaria verde nas duas versoes. Grade que nao pisa na
 * borda e amostra com nome de grade. Aqui a bancada FABRICA seis ferramentas
 * publicadas para o teto ter o que cortar.
 * ------------------------------------------------------------------------- */

echo "\n11. O teto de quatro irmas corta (borda fabricada)\n";
$fabricadas = array();
for ( $i = 1; $i <= 6; $i++ ) {
	$fabricadas[] = array( 'codigo' => 'F' . $i, 'titulo' => 'Ferramenta fabricada ' . $i,
		'slug' => 'ferramenta-fabricada-' . $i, 'resumo' => '', 'estado' => 'publicada' );
	$GLOBALS['__paginas'][ 'ferramenta-fabricada-' . $i ] = true;
}
add_filter( 'robometria_ferramentas', function () use ( $fabricadas ) { return $fabricadas; } );
$irmas = robometria_casca_irmas( 'ferramenta-fabricada-1' );
arv_ok( 4 === count( $irmas ), 'com seis filhas no ar, a lista de irmas para em quatro', count( $irmas ) . ' irmas' );
$slugs_irmas = array_column( $irmas, 'slug' );
arv_ok( ! in_array( 'ferramenta-fabricada-1', $slugs_irmas, true ), 'a pagina nunca e irma dela mesma' );

/* E a outra borda: filha unica nao tem irma, e entao nao ha bloco de cluster. */
$GLOBALS['__filtros']['robometria_ferramentas'] = array();
$sozinha = array( array( 'codigo' => 'F1', 'titulo' => 'Unica', 'slug' => 'ferramenta-fabricada-1',
	'resumo' => '', 'estado' => 'publicada' ) );
add_filter( 'robometria_ferramentas', function () use ( $sozinha ) { return $sozinha; } );
arv_ok( array() === robometria_casca_irmas( 'ferramenta-fabricada-1' ), 'filha unica nao tem irma' );
arv_ok( '' === robometria_casca_veja_tambem_html( 'ferramenta-fabricada-1' ),
	'sem irma, o bloco Veja tambem nao sai' );

/* ------------------------------------------------------------------------- */

printf( "\n%s: %d afirmacoes, %d falha(s).\n", $falhas ? 'REPROVADO' : 'APROVADO', $feitos, $falhas );
exit( $falhas ? 1 : 0 );

<?php
/**
 * Verificacao MEDIDA da F2 — "Qual cola usar no mosaico, e qual rejunte".
 *
 *   php ferramentas/teste-f2.php .
 *
 * O que este arquivo tem que os outros nao tem, e por que:
 *
 *   1. ELE VARRE A ENTRADA INTEIRA, nao o caso-ancora. A F2 e ferramenta de
 *      entrada variavel: ela serve uma pagina por consulta, e a pagina sem
 *      consulta e so UM dos 45 estados de cola e dos 50 de rejunte. A
 *      Robometria pagou essa licao em 11/09/2026 com cinco testes verdes que
 *      nao viam portugues errado porque ele so aparecia quando alguem escolhia
 *      um modelo especifico. Aqui a afirmacao e sobre a SOMA das respostas.
 *
 *   2. A REGUA E PROPRIA, e ela NAO chama o snippet. O esperado de cada celula
 *      vem de `matriz_esperada_da_F2` e `matriz_esperada_do_rejunte` do
 *      esquema, escritos A MAO no bloco 3 a partir das declaracoes, antes de
 *      existir uma linha do snippet. Se as duas metades errarem, elas nao
 *      erram juntas.
 *
 *   3. ELE MEDE NO CORPO SERVIDO, nunca no HTML completo nem no retorno do
 *      shortcode. Afirmacao sobre o que a pagina DIZ se conta dentro de <main>.
 *
 *   4. UM PROCESSO POR ESTADO. A casca tem `static` legitimos (rodape, marca,
 *      trilha) que so valem dentro de uma requisicao; varredura que monta
 *      muitos estados no mesmo processo mede o segundo pela metade.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$rapido = in_array( '--rapido', $argv, true );

$falhas = 0;
$feitos = 0;

function f2_ok( $condicao, $rotulo, $medida = '' ) {
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

function f2_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function f2_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

function f2_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/** Um estado da ferramenta, servido por um processo so dele. */
function f2_render( $raiz, $consulta = '' ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( 'cdm_f2' ) . ' ' . escapeshellarg( 'hoje' )
		. ' ' . escapeshellarg( $consulta ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/* ---------------------------------------------------------------------------
 * A REGUA, lida do repositorio e nunca do snippet.
 * ------------------------------------------------------------------------- */

$esquema  = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$colas    = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$rejuntes = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-rejuntes.json' ), true );

if ( ! $esquema || ! $colas || ! $rejuntes ) {
	echo "ERRO: nao consegui ler o esquema ou o banco.\n";
	exit( 1 );
}

$por_id = array();
foreach ( array_merge( $colas['materiais'], $rejuntes['materiais'] ) as $m ) {
	$por_id[ $m['id'] ] = $m;
}

/** O nome como a TELA o escreve, recalculado aqui: marca so quando falta. */
function f2_nome_esperado( $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return $nome;
	}

	return $marca . ' ' . $nome;
}

echo "Clube do Mosaico — verificacao da F2 " . ( defined( 'CDM_F2_VERSAO' ) ? CDM_F2_VERSAO : '?' ) . "\n";

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "  (F2 " . CDM_F2_VERSAO . ", casca " . CDM_CASCA_VERSAO . ")\n\n";

/* ---------------------------------------------------------------------------
 * 1. A pagina existe na arvore, com mae, e com UM nome so
 * ------------------------------------------------------------------------- */

echo "1. A pagina na arvore (secao 16 do contrato)\n";

$defs = cdm_casca_definicao_paginas();
f2_ok( isset( $defs[ CDM_F2_SLUG ] ), 'a F2 registrou a propria pagina pelo filtro cdm_paginas', CDM_F2_SLUG );
f2_ok( isset( $defs[ CDM_F2_SLUG ]['pai'] ) && 'materiais' === $defs[ CDM_F2_SLUG ]['pai'],
	'a pagina nasce com mae, e a mae e /materiais/' );
f2_ok( isset( $defs['materiais'] ), 'a mae existe na definicao de paginas' );

/* UM NOME POR PAGINA, em toda superficie. A Aquametria pagou por oito paginas
   em que o degrau da trilha e o H1 diziam nomes diferentes a uma linha de
   distancia. Aqui as quatro superficies sao conferidas contra a MESMA
   constante, e o teste le cada uma de onde ela realmente sai. */
$arvore = cdm_casca_arvore();
f2_ok( isset( $arvore[ CDM_F2_SLUG ] ), 'a pagina esta no mapa da arvore' );
f2_ok( isset( $arvore[ CDM_F2_SLUG ]['rotulo'] ) && CDM_F2_TITULO === $arvore[ CDM_F2_SLUG ]['rotulo'],
	'o degrau da trilha usa o mesmo nome', isset( $arvore[ CDM_F2_SLUG ] ) ? $arvore[ CDM_F2_SLUG ]['rotulo'] : '' );
f2_ok( CDM_F2_TITULO === $defs[ CDM_F2_SLUG ]['titulo'], 'o titulo da pagina usa o mesmo nome' );
$no_cartao = '';
foreach ( cdm_casca_ferramentas() as $f ) {
	if ( 'F2' === $f['codigo'] ) {
		$no_cartao = $f['titulo'];
		f2_ok( 'publicada' === $f['estado'], 'a F2 se declara publicada no registro de ferramentas' );
		f2_ok( CDM_F2_SLUG === $f['slug'], 'o registro aponta para o endereco de nivel 3', $f['slug'] );
	}
}
f2_ok( CDM_F2_TITULO === $no_cartao, 'o cartao da home e do Guia usa o mesmo nome' );

/* O <title> do tema e "<titulo> – <nome do site>". 65 e o teto que a Aquametria
   passou a cobrar em 11/09/2026 depois de servir um de 128 caracteres. */
$titulo_completo = CDM_F2_TITULO . ' – Clube do Mosaico';
f2_ok( mb_strlen( $titulo_completo ) <= 65, 'o <title> cabe em 65 caracteres',
	mb_strlen( $titulo_completo ) . ' caracteres' );

/* ---------------------------------------------------------------------------
 * 2. A pagina-ancora: o que existe quando ninguem preenche nada
 * ------------------------------------------------------------------------- */

echo "\n2. A pagina-ancora (secao 5: o que um modelo de linguagem le)\n";

$ancora = f2_render( $raiz );
f2_ok( '' !== $ancora, 'a ancora foi servida', strlen( $ancora ) . ' bytes' );
$corpo_ancora = f2_corpo( $ancora );
$texto_ancora = f2_texto( $corpo_ancora );

/* Pagina fina nao entra no indice de dominio novo (secao 8). */
f2_ok( mb_strlen( $texto_ancora ) >= 1500, 'o corpo tem tamanho de pagina de verdade',
	mb_strlen( $texto_ancora ) . ' caracteres' );

cdm_teste_rebobinar();
cdm_teste_pagina( 'cdm_f2' );
$cru = $GLOBALS['__retorno_shortcode'];
f2_ok( false === stripos( $cru, '<script' ), 'sem <script> no retorno do shortcode (cicatriz de 08/09/2026)' );
f2_ok( false === stripos( $cru, '<style' ), 'sem <style> no retorno do shortcode' );
f2_ok( 0 === substr_count( f2_scripts( $ancora ), '&#038;' ), 'zero &#038; DENTRO de <script>',
	substr_count( f2_scripts( $ancora ), '&#038;' ) . ' achados' );
f2_ok( 0 !== strncmp( ltrim( $texto_ancora ), '---', 3 ), 'o corpo nao comeca por metadado' );

/* A folha e o script vem do rodape, nao da cabeca nem do corpo. */
$pos_corpo  = mb_strpos( $ancora, '<main' );
$pos_css    = mb_strpos( $ancora, 'id="cdm-f2-css"' );
$pos_js     = mb_strpos( $ancora, 'id="cdm-f2-js"' );
f2_ok( false !== $pos_css && $pos_css > $pos_corpo, 'a folha da F2 sai depois do corpo (wp_footer)' );
f2_ok( false !== $pos_js && $pos_js > $pos_corpo, 'o script da F2 sai depois do corpo (wp_footer)' );

/* A tabela pre-renderizada: as 18 + 9 linhas, no HTML servido. */
$linhas_tabela = preg_match_all( '#<table class="cdm-f2-tabela">.*?</table>#is', $corpo_ancora, $mt );
f2_ok( 2 === $linhas_tabela, 'as duas tabelas pre-renderizadas estao no HTML servido', $linhas_tabela . ' tabelas' );
$esperadas_cola    = count( $esquema['matriz_esperada_da_F2']['celulas'] );
$esperadas_rejunte = count( $esquema['matriz_esperada_do_rejunte']['celulas'] );
if ( 2 === $linhas_tabela ) {
	$n1 = preg_match_all( '#<tr>#', $mt[0][0] ) - 1; // o <tr> do cabecalho
	$n2 = preg_match_all( '#<tr>#', $mt[0][1] ) - 1;
	f2_ok( $n1 === $esperadas_cola, 'a tabela de cola serve as ' . $esperadas_cola . ' celulas conferidas', $n1 . ' linhas' );
	f2_ok( $n2 === $esperadas_rejunte, 'a tabela de rejunte serve as ' . $esperadas_rejunte . ' celulas conferidas', $n2 . ' linhas' );
}

/* Trilha e mae: a 16.4(b) cobra a mae no breadcrumb E numa frase do corpo. */
f2_ok( (bool) preg_match( '#<nav class="cdm-trilha".*?>Materiais<#is', $corpo_ancora ),
	'a trilha mostra a mae com endereco de verdade' );
$sem_trilha = preg_replace( '#<nav class="cdm-trilha".*?</nav>#is', '', $corpo_ancora );
f2_ok( false !== strpos( $sem_trilha, 'href="https://clubedomosaico.com.br/materiais/"' ),
	'o corpo tem uma frase que linka a mae (16.4b)' );

/* ---------------------------------------------------------------------------
 * 3. Cabeca: description, canonical e o robo do estado com parametro
 * ------------------------------------------------------------------------- */

echo "\n3. Cabeca da pagina (secoes 14.1 e 14.4)\n";

preg_match( '#<meta name="description" content="([^"]*)"#', $ancora, $md );
$desc = isset( $md[1] ) ? html_entity_decode( $md[1], ENT_QUOTES, 'UTF-8' ) : '';
f2_ok( '' !== $desc, 'a pagina serve meta description' );
f2_ok( mb_strlen( $desc ) >= 120 && mb_strlen( $desc ) <= 200, 'a description cabe na faixa util',
	mb_strlen( $desc ) . ' caracteres' );
/* UM canonical, e ele aponta para o endereco limpo. O "um" nao e zelo: quem
   imprime o proprio canonical por cima do `rel_canonical()` do nucleo serve
   dois, e a bancada so consegue ver isso porque passou a servir o do nucleo
   tambem (render-para-teste.php). */
f2_ok( 1 === substr_count( $ancora, '<link rel="canonical"' ), 'a ancora serve UM canonical',
	substr_count( $ancora, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $ancora, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'canonical aponta para o endereco limpo' );
f2_ok( false === strpos( $ancora, 'name="robots"' ), 'a ancora NAO sai com noindex' );

$com_parametro = f2_render( $raiz, 'base=espelho&onde=externo_exposto&junta=3' );
f2_ok( false !== strpos( $com_parametro, '<meta name="robots" content="noindex, follow">' ),
	'o estado com parametro sai com noindex, follow' );
f2_ok( 1 === substr_count( $com_parametro, '<link rel="canonical"' ), 'o estado com parametro serve UM canonical',
	substr_count( $com_parametro, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $com_parametro, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'o estado com parametro aponta o canonical para a ancora' );

/* JSON-LD: WebApplication + FAQPage, e o FAQ do schema tem que ser o mesmo que
   a pagina MOSTRA. Schema que promete o que a pagina nao diz e schema ignorado
   na melhor das hipoteses. */
preg_match( '#<script type="application/ld\+json" id="cdm-f2-jsonld">(.*?)</script>#s', $ancora, $mj );
$jsonld = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;
f2_ok( is_array( $jsonld ), 'o JSON-LD da F2 e JSON valido' );
$tipos = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	$tipos[] = $no['@type'];
}
f2_ok( in_array( 'WebApplication', $tipos, true ), 'JSON-LD tem WebApplication (secao 5.3)' );
f2_ok( in_array( 'FAQPage', $tipos, true ), 'JSON-LD tem FAQPage' );
f2_ok( false !== strpos( $ancora, 'id="cdm-trilha-jsonld"' ), 'JSON-LD tem BreadcrumbList (16.3)' );

$perguntas_schema = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		foreach ( $no['mainEntity'] as $q ) {
			$perguntas_schema[] = $q['name'];
		}
	}
}
$fora_da_tela = array();
foreach ( $perguntas_schema as $p ) {
	if ( false === mb_strpos( f2_texto( $corpo_ancora ), $p ) ) {
		$fora_da_tela[] = $p;
	}
}
f2_ok( count( $perguntas_schema ) >= 4, 'o FAQPage tem perguntas', count( $perguntas_schema ) . ' perguntas' );
f2_ok( empty( $fora_da_tela ), 'toda pergunta do schema esta escrita na tela',
	empty( $fora_da_tela ) ? 'as ' . count( $perguntas_schema ) : implode( ' | ', $fora_da_tela ) );

/* ---------------------------------------------------------------------------
 * 4. A VARREDURA DA COLA — 45 estados, um processo cada
 * ------------------------------------------------------------------------- */

echo "\n4. A entrada inteira da cola: " . count( $esquema['vocabularios']['base'] ) . " bases x "
	. count( $esquema['vocabularios']['ambiente'] ) . " ambientes\n";

$bases     = $esquema['vocabularios']['base'];
$ambientes = $esquema['vocabularios']['ambiente'];

/* Os rotulos existem para TODA entrada do vocabulario, e nao existe rotulo sem
   entrada. As duas direcoes, porque vocabulario novo sem rotulo sairia na tela
   como chave crua e rotulo orfao e codigo morto que finge cobertura. */
$rot = cdm_f2_rotulos();
$sem_rotulo = array_diff( $bases, array_keys( $rot['base'] ) );
$rotulo_orfao = array_diff( array_keys( $rot['base'] ), $bases );
f2_ok( empty( $sem_rotulo ), 'toda base do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo ) );
f2_ok( empty( $rotulo_orfao ), 'nenhum rotulo de base sem entrada no vocabulario', implode( ', ', $rotulo_orfao ) );
$sem_rotulo_a = array_diff( $ambientes, array_keys( $rot['ambiente'] ) );
f2_ok( empty( $sem_rotulo_a ), 'todo ambiente do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_a ) );
$sem_rotulo_t = array_diff( $esquema['vocabularios']['material_tessela'], array_keys( $rot['tessela'] ) );
f2_ok( empty( $sem_rotulo_t ), 'toda tessela do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_t ) );

$estados       = 0;
$finas         = array();
$sem_acento    = array();
$incoerentes   = array();
$corpos        = array();

/**
 * Portugues errado que chega a tela. Mede o CORPO, palavra a palavra, contra
 * uma lista de formas que so existem sem acento por erro de digitacao — foi
 * assim que o bloco 4 achou "Silicone Acetico Construcao" servido ao visitante.
 */
$formas_erradas = array(
	'acetico', 'ceramica', 'ceramicas', 'construcao', 'acrilico', 'epoxi', 'plastico',
	'aluminio', 'superficies', 'calcario', 'aquarios', 'corrosivel', 'imersao',
	'liquido', 'area', 'areas', 'agua', 'pagina', 'tecnica', 'tecnico', 'nao',
	'sao', 'liberacao', 'variacao', 'condicao', 'marmore', 'latao', 'papelao',
);

foreach ( $bases as $base ) {
	foreach ( $ambientes as $ambiente ) {
		$html  = f2_render( $raiz, 'base=' . $base . '&onde=' . $ambiente );
		$corpo = f2_corpo( $html );
		$texto = f2_texto( $corpo );
		$corpos[ $base . '|' . $ambiente ] = $corpo;
		$estados++;

		if ( mb_strlen( $texto ) < 1500 ) {
			$finas[] = $base . ' x ' . $ambiente . ' (' . mb_strlen( $texto ) . ')';
		}
		$minusculo = mb_strtolower( $texto, 'UTF-8' );
		foreach ( $formas_erradas as $forma ) {
			if ( preg_match( '/(?<![\p{L}])' . $forma . '(?![\p{L}])/u', $minusculo ) ) {
				$sem_acento[] = $base . ' x ' . $ambiente . ': "' . $forma . '"';
				break;
			}
		}
	}
}
f2_ok( 45 === $estados, 'os 45 estados de cola foram servidos, um processo cada', $estados . ' estados' );
f2_ok( empty( $finas ), 'nenhum estado serve pagina fina', empty( $finas ) ? 'todos acima de 1500' : implode( ' | ', array_slice( $finas, 0, 4 ) ) );
f2_ok( empty( $sem_acento ), 'nenhum estado serve portugues sem acento',
	empty( $sem_acento ) ? '45 estados limpos' : implode( ' | ', array_slice( $sem_acento, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 5. AS 18 CELULAS CONFERIDAS — a regua escrita a mao contra o que a tela diz
 * ------------------------------------------------------------------------- */

echo "\n5. As " . $esperadas_cola . " celulas de cola, contra a matriz escrita a mao no bloco 3\n";

$erros_celula = array();
$graves       = array();

foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
	$chave = $c['base'] . '|' . $c['ambiente'];
	$corpo = isset( $corpos[ $chave ] ) ? $corpos[ $chave ] : '';
	if ( '' === $corpo ) {
		$erros_celula[] = $chave . ': nao foi servida';
		continue;
	}

	/* A FRASE-RESPOSTA e a vitrine sao onde o recomendado aparece. A secao de
	   eliminados fica FORA desta medida de proposito: o nome de um produto
	   proibido aparece la, e contar na pagina inteira encontraria os dois. */
	$pedaco = '';
	if ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>\s*<div class="cdm-f2-secao">\s*<h2>Onde comprar</h2>(.*?)(?=<div class="cdm-f2-secao">)#is', $corpo, $mp ) ) {
		$pedaco = f2_texto( $mp[1] . $mp[2] );
	} elseif ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>#is', $corpo, $mp ) ) {
		$pedaco = f2_texto( $mp[1] );
	}
	$fora_html = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo, $mf ) ? $mf[1] : '';
	$fora      = f2_texto( $fora_html );

	foreach ( $c['recomendados_topo'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $pedaco, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" era para estar recomendado e nao esta';
		}
	}
	foreach ( $c['eliminados_por_proibicao'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			/* COERENCIA DA RECOMENDACAO (secao 12): recomendar em primeiro lugar
			   um produto que a propria pagina diz nao servir e defeito GRAVE. */
			$graves[] = $chave . ': "' . $nome . '" esta recomendado E a pagina diz que ele nao serve';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" nao aparece na secao do que nao usar';
		}
	}
	/* A LISTA DO SILENCIO E CONFERIDA NOS DOIS SENTIDOS, e nao por acaso: sem
	   isto, a mutacao "a categoria some da pergunta" PASSOU. Ela fazia os cinco
	   rejuntes entrarem na decisao de COLAGEM como "eliminados por silencio" —
	   frase sem sentido para um produto que nunca foi candidato a colar nada —
	   e o teste nao via, porque so olhava o topo e os proibidos. Quem afirma
	   sobre uma lista tem que cobrar o que falta E o que sobra. */
	/* O paragrafo do silencio DA COLA, e nao o primeiro do corpo: a secao do
	   rejunte usa a mesma classe, e procurar no corpo inteiro achava o dela —
	   o mesmo erro de contar &#038; na pagina toda em vez de dentro do script. */
	$silencio = preg_match( '#<p class="cdm-f2-silencio">(.*?)</p>#is', $fora_html, $ms ) ? f2_texto( $ms[1] ) : '';
	foreach ( $c['eliminados_por_silencio'] as $id ) {
		if ( false === mb_strpos( $silencio, f2_nome_esperado( $por_id[ $id ] ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $por_id[ $id ] ) . '" era para estar no silencio e nao esta';
		}
	}
	$esperado_no_silencio = $c['eliminados_por_silencio'];
	foreach ( $por_id as $id => $m ) {
		if ( in_array( $id, $esperado_no_silencio, true ) ) {
			continue;
		}
		if ( false !== mb_strpos( $silencio, f2_nome_esperado( $m ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $m ) . '" aparece no silencio e nao devia';
		}
	}

	/* Celula sem recomendado tem que DIZER que nao tem, nunca ficar em branco. */
	if ( ! $c['recomendados_topo'] && false === mb_strpos( f2_texto( $corpo ), 'Não temos cola para indicar' ) ) {
		$erros_celula[] = $chave . ': faixa descoberta sem a frase que a declara';
	}
}
f2_ok( empty( $graves ), 'nenhuma pagina recomenda o que ela mesma diz que nao serve',
	empty( $graves ) ? 'as ' . $esperadas_cola . ' celulas' : implode( ' | ', $graves ) );
f2_ok( empty( $erros_celula ), 'a tela diz o que a matriz escrita a mao manda',
	empty( $erros_celula ) ? $esperadas_cola . ' celulas' : implode( ' | ', array_slice( $erros_celula, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 6. O REJUNTE — a grade pisa na borda de cada faixa declarada
 * ------------------------------------------------------------------------- */

echo "\n6. O rejunte: a grade pisa nas bordas das faixas declaradas\n";

/* A regua das bordas e recalculada AQUI, das faixas do banco, e nao lida da
   observacao que o esquema escreveu ao lado. Grade que nao pisa na borda e
   amostra com nome de grade (secao 8). */
$bordas = array();
foreach ( $rejuntes['materiais'] as $m ) {
	foreach ( array( 'junta_min_mm', 'junta_max_mm' ) as $campo ) {
		$v = isset( $m['propriedades'][ $campo ]['valor'] ) ? $m['propriedades'][ $campo ]['valor'] : null;
		if ( null !== $v ) {
			$bordas[ (int) $v ] = true;
			$bordas[ (int) $v + 1 ] = true;
		}
	}
}
ksort( $bordas );
$na_grade = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$na_grade[ (int) $c['junta_mm'] ] = true;
}
$bordas_uteis = array_filter( array_keys( $bordas ), function ( $v ) { return $v >= 1 && $v <= 12; } );
$faltando     = array_diff( $bordas_uteis, array_keys( $na_grade ) );
f2_ok( empty( $faltando ), 'a grade do esquema pisa em toda borda de faixa declarada',
	empty( $faltando ) ? implode( ', ', array_keys( $na_grade ) ) . ' mm' : 'falta ' . implode( ', ', $faltando ) );

$estados_r    = 0;
$erros_rejunte = array();
for ( $junta = 1; $junta <= 12; $junta++ ) {
	foreach ( $ambientes as $ambiente ) {
		$html = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta );
		$estados_r++;
		$corpo = f2_corpo( $html );
		if ( ! preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)</div>\s*<div class="cdm-f2-secao#is', $corpo, $mr ) ) {
			/* A secao do rejunte e a ultima do bloco de saida em alguns estados. */
			preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*)#is', $corpo, $mr );
		}
		$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
		if ( '' === $trecho ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': secao do rejunte ausente';
			continue;
		}
		if ( false === mb_strpos( $trecho, (string) $junta ) ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': a resposta nao repete a folga escolhida';
		}
	}
}
f2_ok( 60 === $estados_r, 'os 60 estados de rejunte foram servidos', $estados_r . ' estados' );
f2_ok( empty( $erros_rejunte ), 'todo estado de rejunte serve a secao dele',
	empty( $erros_rejunte ) ? '60 estados' : implode( ' | ', array_slice( $erros_rejunte, 0, 4 ) ) );

$erros_matriz_r = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$html   = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $c['ambiente'] . '&junta=' . (int) $c['junta_mm'] );
	$corpo  = f2_corpo( $html );
	preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mr );
	$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
	preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', isset( $mr[1] ) ? $mr[1] : '', $mf );
	$frase = isset( $mf[1] ) ? f2_texto( $mf[1] ) : '';

	foreach ( $c['recomendados_topo'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era topo e nao esta na frase';
		}
	}
	/* OS CARTOES CONTAM TANTO QUANTO A FRASE. Duas mutacoes PASSARAM por esta
	   fresta — "faixa de junta abre 1 mm para baixo" e "faixa pela metade vira
	   sem limite" —, e as duas pelo mesmo motivo: o produto indevido nao subia
	   ao topo, entrava como elegivel ABAIXO do topo, e a frase so nomeia o topo.
	   Recomendar em segundo lugar o que o fabricante nao declara e recomendar. */
	$vitrine_r = '';
	if ( preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>.*?<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $corpo, $mv ) ) {
		$vitrine_r = f2_texto( $mv[1] );
	}
	$recomendaveis = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
	foreach ( array_merge( $c['eliminados_por_ambiente'], $c['eliminados_por_faixa_de_junta'] ) as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na frase e era para estar fora';
		}
		if ( '' !== $vitrine_r && false !== mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na vitrine e era para estar fora';
		}
	}
	foreach ( $recomendaveis as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era elegivel e nao esta na vitrine';
		}
	}
	if ( ! $c['recomendados_topo'] && false === mb_strpos( $trecho, 'Não temos rejunte para indicar' ) ) {
		$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': faixa descoberta sem a frase que a declara';
	}
}
f2_ok( empty( $erros_matriz_r ), 'a tela do rejunte diz o que a matriz escrita a mao manda',
	empty( $erros_matriz_r ) ? $esperadas_rejunte . ' celulas' : implode( ' | ', array_slice( $erros_matriz_r, 0, 4 ) ) );

/* O produto cuja faixa de junta nao foi obtida nao pode ser recomendado em
   NENHUM dos 50 estados. E o achado mais valioso do bloco 3c e o mais facil de
   perder: ele e o unico do banco que nomeia pastilha de vidro submersa. */
$sem_faixa = array();
foreach ( $rejuntes['materiais'] as $m ) {
	$min = isset( $m['propriedades']['junta_min_mm']['valor'] ) ? $m['propriedades']['junta_min_mm']['valor'] : null;
	$max = isset( $m['propriedades']['junta_max_mm']['valor'] ) ? $m['propriedades']['junta_max_mm']['valor'] : null;
	if ( null === $min || null === $max ) {
		$sem_faixa[] = f2_nome_esperado( $m );
	}
}
$vazou = array();
if ( $sem_faixa ) {
	for ( $junta = 1; $junta <= 12; $junta++ ) {
		foreach ( $ambientes as $ambiente ) {
			$corpo = f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta ) );
			/* Frase E vitrine: o produto sem faixa de junta nao pode aparecer em
			   NENHUM dos dois lugares — foi entrando pela vitrine que a mutacao
			   da faixa pela metade passou. */
			preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mf );
			$bloco_r = isset( $mf[1] ) ? $mf[1] : '';
			$recomendado_ali = f2_texto(
				( preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', $bloco_r, $m1 ) ? $m1[1] : '' )
				. ' ' . ( preg_match( '#<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $bloco_r, $m2 ) ? $m2[1] : '' )
			);
			foreach ( $sem_faixa as $nome ) {
				if ( false !== mb_strpos( $recomendado_ali, $nome ) ) {
					$vazou[] = $junta . 'mm x ' . $ambiente . ': ' . $nome;
				}
			}
		}
	}
}
f2_ok( ! empty( $sem_faixa ), 'o banco tem produto com faixa de junta nao obtida, e ele e medido', implode( ', ', $sem_faixa ) );
f2_ok( empty( $vazou ), 'produto sem faixa de junta nunca e recomendado, nos 60 estados',
	empty( $vazou ) ? '60 estados' : implode( ' | ', array_slice( $vazou, 0, 3 ) ) );

/* Entrada fora da faixa volta ao padrao em vez de servir bobagem. */
$fora_da_faixa = f2_corpo( f2_render( $raiz, 'base=inventada&onde=marte&junta=99' ) );
f2_ok( false !== mb_strpos( f2_texto( $fora_da_faixa ), 'Para colar em cerâmica' ),
	'entrada invalida cai no padrao em vez de quebrar a pagina' );

/* A MARCA EM DOBRO NAO APARECE EM TESTE DE CONTER. A mutacao que colava a marca
   em todo nome PASSOU na primeira rodada porque "Rejunte Ceramicas Quartzolit"
   esta DENTRO de "Quartzolit Rejunte Ceramicas Quartzolit" — procurar por
   conter aprova o nome errado que engloba o certo. A regua tem que ser de
   igualdade, e e o <h3> do cartao que carrega o nome. */
$nomes_na_tela = array();
$titulos_ruins = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4' ) as $consulta ) {
	$corpo_c = f2_corpo( f2_render( $raiz, $consulta ) );
	preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<span class="cdm-f2-marca">(.*?)</span>\s*<h3>(.*?)</h3>#is', $corpo_c, $mn, PREG_SET_ORDER );
	foreach ( $mn as $cartao ) {
		$marca_html = f2_texto( $cartao[1] );
		$titulo     = f2_texto( $cartao[2] );
		$nomes_na_tela[ $titulo ] = true;
		/* O <h3> traz o nome comercial; a marca sai no seu proprio campo, uma vez
		   so. Nome que repete a marca ja impressa ao lado dela e marca em dobro. */
		if ( '' !== $marca_html && mb_substr_count( mb_strtolower( $marca_html . ' ' . $titulo, 'UTF-8' ),
				mb_strtolower( $marca_html, 'UTF-8' ) ) > 2 ) {
			$titulos_ruins[] = $marca_html . ' / ' . $titulo;
		}
	}
}
$fora_do_banco = array();
$do_banco = array();
foreach ( $por_id as $m ) {
	$do_banco[ (string) $m['nome_comercial'] ] = true;
}
foreach ( array_keys( $nomes_na_tela ) as $titulo ) {
	if ( ! isset( $do_banco[ $titulo ] ) ) {
		$fora_do_banco[] = $titulo;
	}
}
/* O CARTAO NAO ERA O LUGAR DE MEDIR ISSO, e a mutacao provou: o <h3> traz o
   `nome_comercial` cru e nunca a composicao, entao a marca em dobro so aparece
   na FRASE e nas listas, que e onde `cdm_f2_nome()` e chamada. A regua certa e
   direta e nao depende de onde o nome sai: para todo produto cujo nome
   comercial JA carrega a marca, a composicao "<marca> <nome>" nao pode existir
   em lugar nenhum do corpo. */
$dobradas = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4',
                 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua&junta=3' ) as $consulta ) {
	$texto_c = f2_texto( f2_corpo( f2_render( $raiz, $consulta ) ) );
	foreach ( $por_id as $m ) {
		$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
		$nome  = (string) $m['nome_comercial'];
		if ( '' === $marca || false === mb_stripos( $nome, $marca ) ) {
			continue;
		}
		if ( false !== mb_strpos( $texto_c, $marca . ' ' . $nome ) ) {
			$dobradas[] = ( '' === $consulta ? 'ancora' : $consulta ) . ': "' . $marca . ' ' . $nome . '"';
		}
	}
}
f2_ok( empty( $dobradas ), 'nenhum lugar da pagina repete a marca dentro do nome do produto',
	empty( $dobradas ) ? count( $por_id ) . ' produtos em 5 estados' : implode( ' | ', array_slice( $dobradas, 0, 3 ) ) );
f2_ok( empty( $titulos_ruins ), 'nenhum cartao repete a marca dentro do nome do produto',
	empty( $titulos_ruins ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $titulos_ruins ) );
f2_ok( empty( $fora_do_banco ), 'todo nome de produto na tela e IGUAL ao do banco, nao parecido',
	empty( $fora_do_banco ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $fora_do_banco ) );

/* ---------------------------------------------------------------------------
 * 7. O bloco de compra vem ANTES da procedencia (secao 7, cicatriz da
 *    Robometria de 10/09/2026), e todo item sem link diz isso.
 * ------------------------------------------------------------------------- */

echo "\n7. Compra antes de procedencia, e o que espera link\n";

$cartoes = preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $corpo_ancora, $mc );
f2_ok( $cartoes > 0, 'a ancora serve cartoes de produto', $cartoes . ' cartoes' );
$ordem_errada = 0;
$sem_fonte    = 0;
foreach ( $mc[1] as $cartao ) {
	$p_compra = mb_strpos( $cartao, 'cdm-f2-compra' );
	$p_fonte  = mb_strpos( $cartao, 'cdm-f2-fonte' );
	if ( false === $p_fonte ) {
		$sem_fonte++;
		continue;
	}
	if ( false === $p_compra || $p_compra > $p_fonte ) {
		$ordem_errada++;
	}
}
f2_ok( 0 === $ordem_errada, 'o bloco de compra vem antes da prova de procedencia em todo cartao',
	$ordem_errada . ' fora de ordem' );
f2_ok( 0 === $sem_fonte, 'todo cartao leva o link de procedencia', $sem_fonte . ' sem fonte' );
f2_ok( false === strpos( $corpo_ancora, 'class="cdm-f2-botao" href' ) || false !== strpos( $corpo_ancora, 'rel="sponsored' ),
	'link de afiliado, quando existir, leva rel="sponsored"' );
f2_ok( (bool) preg_match_all( '#rel="nofollow noopener"#', $corpo_ancora ),
	'o link de procedencia e discreto, com rel="nofollow noopener"' );
f2_ok( false !== mb_strpos( f2_texto( $corpo_ancora ), 'comissão' ), 'o aviso de comissao esta visivel na pagina' );

/* Quantos itens esperam link — numero CONTADO do banco, nunca digitado. */
$esperando = 0;
foreach ( $por_id as $m ) {
	if ( empty( $m['afiliado']['url'] ) ) {
		$esperando++;
	}
}
$declarado = (int) $colas['afiliado']['itens_esperando_link'] + (int) $rejuntes['afiliado']['itens_esperando_link'];
f2_ok( $esperando === $declarado, 'o numero de itens esperando link bate com o banco contado',
	$esperando . ' contados, ' . $declarado . ' declarados' );
$sem_loja = substr_count( $corpo_ancora, 'Link de loja em breve' );
f2_ok( $sem_loja > 0, 'a pagina reserva o lugar do link em vez de esconder o cartao', $sem_loja . ' cartoes' );

/* ---------------------------------------------------------------------------
 * 8. As duas faixas descobertas, declaradas em vez de preenchidas no chute
 * ------------------------------------------------------------------------- */

echo "\n8. O que a ilha diz que nao sabe (secao 7 do contrato)\n";

$t = f2_texto( $corpo_ancora );
f2_ok( false !== mb_strpos( $t, 'peça de plástico' ), 'a pagina declara a faixa descoberta do plastico' );
f2_ok( false !== mb_strpos( $t, 'dentro da água o tempo todo' ), 'a pagina declara a faixa descoberta da peca submersa' );
f2_ok( false !== mb_strpos( $t, 'material de imprensa' ),
	'a pagina diz por que a menção de nivel 4 nao vira recomendacao' );

/* O tempo de espera que a ilha NAO tem: o campo existe no banco com o motivo
   escrito, e a pagina diz que nao publica em vez de simplesmente nao ter a
   secao. Ausencia de secao e indistinguivel de "nao importa". */
$mdf = f2_texto( f2_corpo( f2_render( $raiz, 'base=mdf_madeira&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $mdf, 'ainda não publica o tempo de espera' ),
	'quando falta o tempo de espera, a pagina diz que falta' );
$ceramica = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $ceramica, '24 horas' ),
	'quando o fabricante declara a cura, a pagina publica o numero' );

$plastico = f2_texto( f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $plastico, 'Não temos cola para indicar' ),
	'o estado de plastico responde com a faixa descoberta, nao em branco' );
/* DECLARACAO VAGA NAO E SILENCIO, e a pagina separa as duas. Dizer "o
   fabricante nao fala" de um produto cujo fabricante escreveu "certos tipos de
   plastico" seria falso: ele falou, e falou de um jeito que nao decide. */
f2_ok( false !== mb_strpos( $plastico, 'certos tipos de plástico' )
	&& false !== mb_strpos( $plastico, 'não nomeia material nenhum' ),
	'a declaracao vaga aparece separada do silencio, com a frase do fabricante' );
$submerso = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua' ) ) );
f2_ok( false !== mb_strpos( $submerso, 'Não temos cola para indicar' ),
	'o estado submerso responde com a faixa descoberta' );

/* ---------------------------------------------------------------------------
 * Fecho
 * ------------------------------------------------------------------------- */

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

<?php
/**
 * O nó `WebSite` da home existe, e existe SÓ na home.
 *
 *   php ferramentas/teste-site-jsonld.php .
 *
 * Item 1 do despacho da Sentinela de 23/09/2026: a home servia zero ocorrência
 * de `application/ld+json` e zero de `schema.org`, enquanto as outras 47 URLs
 * serviam. Este portão mede a correção NAS DUAS DIREÇÕES, que foi o que o
 * próprio despacho pediu:
 *
 *   1. sem o `WebSite` na home, reprova;
 *   2. com o `WebSite` fora da home, reprova também;
 *   3. com `BreadcrumbList` na home, reprova — a 16.3 não mudou, e a home
 *      continua sendo a única página sem trilha.
 *
 * A TERCEIRA É A QUE JUSTIFICA O PORTÃO EXISTIR. Consertar o item 1 pelo
 * caminho errado é fácil e é tentador: bastaria a trilha deixar de devolver
 * vazio na home e a medição "a home tem JSON-LD" ficaria verde na hora,
 * publicando um breadcrumb de um degrau só na página que não tem degrau
 * nenhum. A afirmação que pega isso não é a presença do nó novo: é a AUSÊNCIA
 * do nó velho, no mesmo render.
 *
 * E A SEGUNDA NÃO É PREOCIOSISMO: `is_front_page()` é a única coisa que separa
 * os dois mundos, e uma guarda que sempre responde `true` (ou que some) passa
 * despercebida por qualquer teste que só olhe a home. Por isso o render da
 * página interna afirma, no mesmo processo, que ELA tem `BreadcrumbList` — sem
 * isso, um render morto (que não emitisse nada) provaria a ausência do
 * `WebSite` sem provar coisa nenhuma.
 */
$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

require __DIR__ . '/render-para-teste.php';

/* As páginas do menu existem neste site de teste; sem isto a casca serve
   <span> em vez de <a> e a trilha da página interna mudaria de forma. */
$GLOBALS['__paginas'] = array(
	'calculadoras' => true,
	'metodologia'  => true,
	'sobre'        => true,
);

aquametria_teste_carregar( $raiz );

$falhas = 0; $casos = 0;
function afirmar( $cond, $rotulo ) {
	global $falhas, $casos;
	$casos++;
	if ( ! $cond ) { $falhas++; echo "  FALHA  $rotulo\n"; }
}

/**
 * Roda o wp_head no mundo pedido e devolve o HTML da cabeça.
 */
function cabeca( $inicial, $slug ) {
	$GLOBALS['__pagina_inicial'] = $inicial;
	$GLOBALS['__slug_pagina']    = $slug;
	aquametria_teste_rebobinar();
	ob_start(); do_action( 'wp_head' ); return ob_get_clean();
}

/**
 * Os blocos ld+json da cabeça, já decodificados. Blocos que não parseiam voltam
 * como null de propósito: JSON quebrado é pior que JSON ausente, porque a
 * presença da tag faz a medição crua ("a home tem ld+json") ficar verde.
 */
function nos( $html ) {
	$fora = array();
	if ( preg_match_all( '#<script type="application/ld\+json"[^>]*>(.*?)</script>#s', $html, $m ) ) {
		foreach ( $m[1] as $corpo ) {
			$fora[] = json_decode( trim( $corpo ), true );
		}
	}
	return $fora;
}

function tipos( $lista ) {
	$fora = array();
	foreach ( $lista as $no ) {
		if ( is_array( $no ) && isset( $no['@type'] ) ) { $fora[] = $no['@type']; }
	}
	return $fora;
}

/* ---- 1. A HOME ---------------------------------------------------------- */

$home = cabeca( true, '' );

afirmar( false !== strpos( $home, 'application/ld+json' ), 'a home serve pelo menos um bloco ld+json' );
afirmar( false !== strpos( $home, 'schema.org' ), 'a home cita schema.org' );

$nos_home = nos( $home );
afirmar( count( $nos_home ) >= 1, 'a home tem ao menos um bloco ld+json extraível' );
foreach ( $nos_home as $i => $no ) {
	afirmar( null !== $no, "o bloco ld+json #$i da home parseia como JSON válido" );
}

$site = null;
foreach ( $nos_home as $no ) {
	if ( is_array( $no ) && isset( $no['@type'] ) && 'WebSite' === $no['@type'] ) { $site = $no; }
}
afirmar( null !== $site, 'a home tem um nó de @type WebSite' );

if ( $site ) {
	afirmar( 'https://schema.org' === ( $site['@context'] ?? '' ), 'o WebSite declara @context schema.org' );
	afirmar( 'Aquametria' === ( $site['name'] ?? '' ), 'o WebSite tem name da ilha' );
	afirmar( 'https://aquametria.com.br/' === ( $site['url'] ?? '' ), 'o WebSite tem url da ilha' );
	afirmar( 'pt-BR' === ( $site['inLanguage'] ?? '' ), 'o WebSite declara inLanguage pt-BR' );

	/* A descrição é a MESMA constante que o núcleo usa para montar o <title> da
	   home. Uma terceira descrição da ilha, escrita só para o robô, é a família
	   do "parece dado": ninguém a lê na tela e ninguém a mantém. */
	afirmar( AQUAMETRIA_CASCA_TAGLINE_CURTA === ( $site['description'] ?? '' ),
		'a description do WebSite é a tagline curta, a mesma do <title> da home' );
	afirmar( false === strpos( $home, 'AQUAMETRIA_CASCA_TAGLINE_CURTA' ),
		'a constante não vaza crua para dentro do JSON' );

	$ed = $site['publisher'] ?? array();
	afirmar( 'Organization' === ( $ed['@type'] ?? '' ), 'o publisher é uma Organization' );
	afirmar( 'Aquametria' === ( $ed['name'] ?? '' ), 'o publisher tem name da ilha' );
	afirmar( 'https://aquametria.com.br/' === ( $ed['url'] ?? '' ), 'o publisher tem url da ilha' );

	/* Prometer caixa de busca que a ilha não serve é publicar o que a página
	   não cumpre. Enquanto não houver busca, o nó não pode declarar a ação. */
	afirmar( ! isset( $site['potentialAction'] ),
		'o WebSite NÃO declara potentialAction: a ilha não serve busca ao visitante' );
}

/* A 16.3 não mudou: a home continua sem trilha, e sem BreadcrumbList. */
afirmar( ! in_array( 'BreadcrumbList', tipos( $nos_home ), true ),
	'a home NÃO serve BreadcrumbList (16.3)' );
afirmar( false === strpos( $home, 'aquametria-trilha-jsonld' ),
	'a home nem sequer imprime a tag da trilha' );

/* ---- 2. UMA PÁGINA INTERNA --------------------------------------------- */

$dentro     = cabeca( false, 'calculadoras' );
$nos_dentro = nos( $dentro );

afirmar( in_array( 'BreadcrumbList', tipos( $nos_dentro ), true ),
	'a página interna serve BreadcrumbList — prova de que este render não está morto' );
afirmar( ! in_array( 'WebSite', tipos( $nos_dentro ), true ),
	'a página interna NÃO serve WebSite: o nó de identidade é da home e de mais ninguém' );
afirmar( false === strpos( $dentro, 'aquametria-site-jsonld' ),
	'a página interna nem sequer imprime a tag do WebSite' );

/* ---- 3. A FUNÇÃO SOZINHA ------------------------------------------------ */

/* Ela não pode depender do mundo em que é chamada: quem decide se o nó sai é o
   gancho, e o conteúdo do nó é sempre o mesmo.

   A PRIMEIRA VERSÃO DISTO NÃO MEDIA NADA, e a bateria de mutações a pegou no
   dia em que as duas nasceram: ela lia `$a` sem montar mundo nenhum, e o mundo
   que sobrava do render anterior já era o de página interna — então `$a` e `$b`
   saíam do MESMO mundo e a comparação era verdadeira por construção. Os dois
   mundos se montam aqui, um para cada lado, de propósito. */
$GLOBALS['__pagina_inicial'] = true;
$a = aquametria_casca_site_jsonld();
$GLOBALS['__pagina_inicial'] = false;
$b = aquametria_casca_site_jsonld();
afirmar( $a === $b, 'o conteúdo do nó não muda com o contexto da página' );
afirmar( null !== json_decode( wp_json_encode( $a ), true ), 'o nó serializa para JSON válido' );

echo $falhas === 0
	? "teste-site-jsonld: APROVADO — $casos afirmações, 0 falha\n"
	: "teste-site-jsonld: REPROVADO — $falhas de $casos\n";
exit( $falhas === 0 ? 0 : 1 );

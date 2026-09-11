<?php
/**
 * Exercita o snippet de SEO técnico sem WordPress.
 *
 *   php ferramentas/teste-seo-tecnico.php .
 *
 * Confere as duas decisões que o despacho da Sentinela de 09/09 cobra, e uma
 * terceira que é o risco real de um snippet que manda noindex:
 *   1. o que TEM que sair do índice sai — arquivo por data, autor, tag, a
 *      categoria não curada (a "sem categoria" inclusive), anexo, busca e 404;
 *   2. o que NÃO pode sair fica — página, artigo e home. Um noindex sobrando
 *      numa calculadora seria um defeito muito pior do que o que se conserta
 *      aqui, porque tiraria do ar exatamente o que a ilha quer indexar;
 *   3. o sitemap perde o provedor de autores sempre, e o de taxonomias enquanto
 *      não houver categoria curada — e volta a tê-lo assim que houver.
 */
$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

define( 'ABSPATH', '/tmp/wp/' );
function add_action( $h, $f, $p = 10, $a = 1 ) {}
function add_filter( $h, $f, $p = 10, $a = 1 ) {}
function apply_filters( $h, $v ) { return $v; }

/* O snippet não tem "<?php" no topo — quem põe é o Code Snippets. O guarda de
   ABSPATH faz um `return` de topo, que dentro de eval() é legítimo. */
$src = file_get_contents( $raiz . '/snippets/aquametria-seo-tecnico.php' );
if ( false === $src ) {
	fwrite( STDERR, "FALHA: snippet não encontrado.\n" );
	exit( 1 );
}
eval( $src );

$falhas = 0; $casos = 0;
function afirmar( $cond, $rotulo ) {
	global $falhas, $casos;
	$casos++;
	if ( ! $cond ) { $falhas++; echo "  FALHA  $rotulo\n"; }
}

/* ---- 1. o que tem que sair do índice ---------------------------------- */
$fora = array(
	'arquivo por data (/2026/09/08/)' => array( 'data' => true ),
	'arquivo de autor'                => array( 'autor' => true ),
	'arquivo de tag'                  => array( 'tag' => true ),
	'sem categoria'                   => array( 'categoria' => true, 'categoria_curada' => false ),
	'categoria nova ainda sem texto'  => array( 'categoria' => true, 'categoria_curada' => false ),
	'página de anexo'                 => array( 'anexo' => true, 'singular' => true ),
	'resultado de busca'              => array( 'busca' => true ),
	'404'                             => array( 'erro_404' => true ),
	'índice do blog fora da home'     => array( 'indice_do_blog' => true, 'pagina_inicial' => false ),
);
foreach ( $fora as $rotulo => $ctx ) {
	afirmar( true === aquametria_seo_deve_noindex( $ctx ), "deveria ser noindex: $rotulo" );
}

/* ---- 2. o que NÃO pode sair do índice --------------------------------- */
$dentro = array(
	'calculadora (página)'            => array( 'singular' => true ),
	'artigo (post)'                   => array( 'singular' => true ),
	'home / página inicial'           => array( 'pagina_inicial' => true, 'indice_do_blog' => true ),
	'página inicial estática'         => array( 'pagina_inicial' => true, 'singular' => true ),
	'categoria curada'                => array( 'categoria' => true, 'categoria_curada' => true ),
	'contexto vazio (padrão indexa)'  => array(),
);
foreach ( $dentro as $rotulo => $ctx ) {
	afirmar( false === aquametria_seo_deve_noindex( $ctx ), "NÃO pode ser noindex: $rotulo" );
}

/* A ordem das perguntas importa: anexo também é singular, e singular sozinho
   indexa. Se a função perguntasse "singular" primeiro, o anexo escaparia. */
afirmar( true === aquametria_seo_deve_noindex( array( 'anexo' => true, 'singular' => true ) ),
	'anexo vence singular na ordem das perguntas' );
afirmar( true === aquametria_seo_deve_noindex( array( 'erro_404' => true, 'categoria' => true, 'categoria_curada' => true ) ),
	'404 dentro de categoria curada continua noindex' );

/* Chave desconhecida não pode derrubar nem inverter a decisão. */
afirmar( false === aquametria_seo_deve_noindex( array( 'singular' => true, 'coisa_nova' => true ) ),
	'chave desconhecida é ignorada' );

/* ---- 3. provedores do sitemap ----------------------------------------- */
afirmar( false === aquametria_seo_provedor_permitido( 'users', array() ),
	'provedor de autores sai sempre' );
afirmar( false === aquametria_seo_provedor_permitido( 'users', array( 'metodos' ) ),
	'provedor de autores sai mesmo com categoria curada' );
afirmar( false === aquametria_seo_provedor_permitido( 'taxonomies', array() ),
	'sem categoria curada, o provedor de taxonomias sai' );
afirmar( true === aquametria_seo_provedor_permitido( 'taxonomies', array( 'metodos' ) ),
	'com categoria curada, o provedor de taxonomias volta' );
afirmar( true === aquametria_seo_provedor_permitido( 'posts', array() ),
	'provedor de posts NUNCA sai — é o sitemap da ilha' );

/* ---- 4. o estado de hoje: a lista de curadas está vazia de propósito --- */
$curadas = aquametria_seo_categorias_no_sitemap();
afirmar( is_array( $curadas ), 'a lista de categorias curadas é um array' );
echo 'categorias curadas hoje: ' . count( $curadas ) . " (zero é o esperado até 16/09)\n";
afirmar( ! in_array( 'uncategorized', $curadas, true ) && ! in_array( 'sem-categoria', $curadas, true ),
	'a "sem categoria" nunca pode entrar na lista de curadas' );

/* ---- 5. o filtro de termos, com a lista vazia, não devolve termo ------- */
$args = aquametria_seo_filtrar_termos( array(), 'category' );
afirmar( isset( $args['include'] ) && array( 0 ) === $args['include'],
	'com lista vazia, a consulta de termos é forçada a vazio' );
$args = aquametria_seo_filtrar_termos( array( 'x' => 1 ), 'post_tag' );
afirmar( array( 'x' => 1 ) === $args, 'taxonomia que não é categoria passa intacta' );

/* ---- 6. só a categoria sobrevive ao filtro de taxonomias -------------- */
$tax = aquametria_seo_filtrar_taxonomias( array( 'category' => 'obj', 'post_tag' => 'obj', 'post_format' => 'obj' ) );
afirmar( array( 'category' => 'obj' ) === $tax, 'tag e formato saem do sitemap de taxonomias' );

/* ---- 7. meta description e cartão de compartilhamento (v1.1.0) --------
 *
 * O mapa é gerado por ferramentas/gerar-metas-descricao.py e conferido por ele
 * (faixa de caracteres, texto repetido, slug faltando). O que se exercita AQUI é
 * o que aquele gerador não alcança: o comportamento da função que monta as tags
 * quando o slug não está no mapa, quando a URL não veio, e a garantia de que a
 * description e a og:description são o mesmo texto — duas descrições diferentes
 * na mesma página é o defeito que ninguém vê olhando a página renderizada.
 * ---------------------------------------------------------------------- */
$metas = aquametria_seo_metas_por_slug();
afirmar( is_array( $metas ) && 13 === count( $metas ),
	'o mapa tem as 13 URLs do sitemap (tem ' . count( $metas ) . ')' );

function aqm_valor_da_tag( $tags, $chave ) {
	foreach ( $tags as $t ) {
		if ( $t['chave'] === $chave ) {
			return $t['valor'];
		}
	}
	return null;
}

foreach ( $metas as $slug => $item ) {
	$n = function_exists( 'mb_strlen' ) ? mb_strlen( $item['descricao'], 'UTF-8' ) : strlen( $item['descricao'] );
	afirmar( $n >= 120 && $n <= 160, "descrição de $slug tem $n caracteres (120 a 160)" );
	afirmar( '' !== trim( $item['titulo'] ), "título presente em $slug" );

	$tags = aquametria_seo_tags_da_pagina( $slug, $metas, 'https://aquametria.com.br/x/', 'Aquametria' );
	afirmar( count( $tags ) > 0, "$slug produz tags" );
	afirmar( aqm_valor_da_tag( $tags, 'description' ) === $item['descricao'],
		"a description de $slug é a do mapa" );
	afirmar( aqm_valor_da_tag( $tags, 'og:description' ) === aqm_valor_da_tag( $tags, 'description' ),
		"description e og:description são o MESMO texto em $slug" );
	afirmar( aqm_valor_da_tag( $tags, 'og:title' ) === $item['titulo'],
		"og:title de $slug é o título do mapa" );
}

/* Duas descrições iguais em URLs diferentes devolvem ao Google o sinal de
   duplicata. O gerador recusa gravar assim; aqui se confere o arquivo no ar. */
$vistas = array();
foreach ( $metas as $slug => $item ) {
	$chave = mb_strtolower( trim( $item['descricao'] ), 'UTF-8' );
	afirmar( ! isset( $vistas[ $chave ] ), "descrição de $slug não se repete" );
	$vistas[ $chave ] = $slug;
}

/* Slug fora do mapa: nada é impresso. Description inventada por nós seria pior
   que o recorte automático do Google, porque pareceria intencional. */
afirmar( array() === aquametria_seo_tags_da_pagina( 'pagina-que-nao-existe', $metas, 'https://x/', 'Aquametria' ),
	'slug fora do mapa não produz tag nenhuma' );
afirmar( array() === aquametria_seo_tags_da_pagina( '', $metas, 'https://x/', 'Aquametria' ),
	'slug vazio não produz tag nenhuma' );
afirmar( array() === aquametria_seo_tags_da_pagina( 'sobre', array( 'sobre' => array( 'titulo' => 'Sobre', 'descricao' => '   ' ) ), 'https://x/', 'Aquametria' ),
	'descrição em branco não produz tag nenhuma' );

/* og:url com endereço errado manda o compartilhamento para outro lugar; sem
   URL resolvida, a tag simplesmente não sai. */
$sem_url = aquametria_seo_tags_da_pagina( 'sobre', $metas, '', 'Aquametria' );
afirmar( null === aqm_valor_da_tag( $sem_url, 'og:url' ), 'sem URL, não sai og:url' );
afirmar( null !== aqm_valor_da_tag( $sem_url, 'description' ), 'sem URL, a description continua saindo' );
$com_url = aquametria_seo_tags_da_pagina( 'sobre', $metas, 'https://aquametria.com.br/sobre/', 'Aquametria' );
afirmar( 'https://aquametria.com.br/sobre/' === aqm_valor_da_tag( $com_url, 'og:url' ), 'og:url sai com a URL resolvida' );
foreach ( $com_url as $t ) {
	if ( 'og:url' === $t['chave'] ) {
		afirmar( ! empty( $t['url'] ), 'og:url é marcada como URL, para o gancho escapar com esc_url' );
	}
}
afirmar( null === aqm_valor_da_tag( $com_url, 'og:image' ),
	'og:image NÃO sai: a ilha ainda não tem imagem própria hospedada' );
afirmar( 'summary' === aqm_valor_da_tag( $com_url, 'twitter:card' ), 'twitter:card summary (sem imagem)' );
afirmar( 'pt_BR' === aqm_valor_da_tag( $com_url, 'og:locale' ), 'og:locale pt_BR' );
afirmar( 'Aquametria' === aqm_valor_da_tag( $com_url, 'og:site_name' ), 'og:site_name presente' );
$sem_site = aquametria_seo_tags_da_pagina( 'sobre', $metas, 'https://x/', '  ' );
afirmar( null === aqm_valor_da_tag( $sem_site, 'og:site_name' ), 'sem nome de site, não sai og:site_name' );

/* Cada tag sai uma vez só: `<head>` com duas descriptions é o Google escolhendo
   por nós. */
$chaves = array();
foreach ( $com_url as $t ) {
	afirmar( ! isset( $chaves[ $t['chave'] ] ), 'tag ' . $t['chave'] . ' aparece uma vez só' );
	$chaves[ $t['chave'] ] = true;
	afirmar( in_array( $t['tipo'], array( 'name', 'property' ), true ), 'tipo válido em ' . $t['chave'] );
}
/* `og:` é property e o resto é name — trocar os dois faz o Facebook ignorar a
   tag em silêncio, que é o pior modo de falhar. */
foreach ( $com_url as $t ) {
	$esperado = ( 0 === strpos( $t['chave'], 'og:' ) ) ? 'property' : 'name';
	afirmar( $esperado === $t['tipo'], $t['chave'] . ' usa ' . $esperado );
}

/* ---- 8. o que sai impresso no <head> -----------------------------------
 *
 * As afirmações acima param na estrutura das tags. O que a Sentinela mede é o
 * HTML servido, e entre os dois existe o gancho: a escolha do slug, a resolução
 * da URL e o escape. Aqui o WordPress é substituído por stubs governados por
 * $GLOBALS, e o que se confere é o texto impresso.
 * ---------------------------------------------------------------------- */
$GLOBALS['aqm_ctx'] = array( 'admin' => false, 'front' => false, 'singular' => true, 'obj' => null, 'permalink' => '' );

function is_admin() { return ! empty( $GLOBALS['aqm_ctx']['admin'] ); }
function is_front_page() { return ! empty( $GLOBALS['aqm_ctx']['front'] ); }
function is_singular() { return ! empty( $GLOBALS['aqm_ctx']['singular'] ); }
function get_queried_object() { return $GLOBALS['aqm_ctx']['obj']; }
function get_permalink( $id ) { return $GLOBALS['aqm_ctx']['permalink']; }
function home_url( $c = '/' ) { return 'https://aquametria.com.br' . $c; }
function get_option( $nome, $padrao = false ) { return 'page_on_front' === $nome ? 7 : $padrao; }
function get_post_field( $campo, $id ) { return ( 'post_name' === $campo && 7 === $id ) ? 'inicio' : ''; }
function esc_attr( $v ) { return htmlspecialchars( (string) $v, ENT_QUOTES, 'UTF-8' ); }
function esc_url( $v ) { return htmlspecialchars( (string) $v, ENT_QUOTES, 'UTF-8' ); }

function aqm_head( $ctx ) {
	$GLOBALS['aqm_ctx'] = array_merge(
		array( 'admin' => false, 'front' => false, 'singular' => true, 'obj' => null, 'permalink' => '' ),
		$ctx
	);
	ob_start();
	aquametria_seo_imprimir_metas();
	return ob_get_clean();
}

/* Uma calculadora: a description dela, e a URL canônica dela. */
$obj  = (object) array( 'ID' => 42, 'post_name' => 'calculadora-de-vazao-do-filtro' );
$html = aqm_head( array( 'obj' => $obj, 'permalink' => 'https://aquametria.com.br/calculadora-de-vazao-do-filtro/' ) );
afirmar( 1 === substr_count( $html, '<meta name="description"' ), 'a calculadora imprime UMA description' );
afirmar( false !== strpos( $html, 'Qual a vazão de filtro para o seu aquário' ), 'é a description daquela calculadora' );
afirmar( false !== strpos( $html, '<meta property="og:url" content="https://aquametria.com.br/calculadora-de-vazao-do-filtro/">' ),
	'og:url é o permalink da própria página' );
afirmar( false === strpos( $html, 'og:image' ), 'nenhuma og:image impressa' );

/* A home é resolvida pela opção page_on_front, não pelo objeto da consulta. */
$html = aqm_head( array( 'front' => true, 'obj' => null ) );
afirmar( false !== strpos( $html, 'Quantos litros tem o seu aquário?' ), 'a home imprime a description dela' );
afirmar( false !== strpos( $html, '<meta property="og:url" content="https://aquametria.com.br/">' ),
	'na home, og:url é a raiz' );

/* Artigo: a chave é o post_name, não a URL com prefixo de data. */
$obj  = (object) array( 'ID' => 9, 'post_name' => 'quantos-watts-de-aquecedor-para-aquario' );
$html = aqm_head( array( 'obj' => $obj, 'permalink' => 'https://aquametria.com.br/2026/09/08/quantos-watts-de-aquecedor-para-aquario/' ) );
afirmar( false !== strpos( $html, 'veio da prateleira' ), 'o artigo acha a description pelo post_name' );
afirmar( false !== strpos( $html, '/2026/09/08/quantos-watts-de-aquecedor-para-aquario/' ), 'og:url do artigo leva a data' );

/* O que NÃO pode imprimir nada. */
afirmar( '' === aqm_head( array( 'admin' => true, 'obj' => $obj ) ), 'no wp-admin não imprime' );
afirmar( '' === aqm_head( array( 'singular' => false, 'obj' => null ) ), 'arquivo/listagem não imprime' );
afirmar( '' === aqm_head( array( 'obj' => (object) array( 'ID' => 1, 'post_name' => 'nao-mapeada' ) ) ),
	'página fora do mapa não imprime' );

/* Aspas no texto quebrariam o atributo se o escape falhasse. A description da
   ilha não tem aspas hoje, e é justamente por isso que se testa com uma que tem:
   o dia em que alguém escrever uma, o teste é que tem que reclamar. */
$html = aqm_head( array( 'obj' => (object) array( 'ID' => 1, 'post_name' => 'sobre' ) ) );
afirmar( false === strpos( $html, "content=\"\"" ), 'nenhum content vazio' );
$falso = array( 'sobre' => array( 'titulo' => 'A "melhor" calculadora', 'descricao' => str_repeat( 'a', 130 ) ) );
$tags  = aquametria_seo_tags_da_pagina( 'sobre', $falso, 'https://x/', 'Aquametria' );
afirmar( 'A "melhor" calculadora' === aqm_valor_da_tag( $tags, 'og:title' ),
	'a função pura não escapa — quem escapa é o gancho' );
afirmar( false !== strpos( esc_attr( aqm_valor_da_tag( $tags, 'og:title' ) ), '&quot;' ),
	'aspas viram entidade no escape do gancho' );

/* Nenhuma tag pode sair com quebra de linha no meio do atributo. */
$html = aqm_head( array( 'obj' => (object) array( 'ID' => 1, 'post_name' => 'metodologia' ) ) );
foreach ( array_filter( explode( "\n", $html ) ) as $linha ) {
	afirmar( 1 === preg_match( '/^<meta (name|property)="[^"]+" content="[^"]*">$/u', $linha ),
		'linha bem formada: ' . substr( $linha, 0, 40 ) );
}

echo "afirmações: $casos · falhas: $falhas\n";
exit( $falhas ? 1 : 0 );

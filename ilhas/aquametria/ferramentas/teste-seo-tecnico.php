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

echo "afirmações: $casos · falhas: $falhas\n";
exit( $falhas ? 1 : 0 );

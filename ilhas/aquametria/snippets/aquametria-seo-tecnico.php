/**
 * Aquametria SEO Técnico — sitemap curado e diretiva de robôs
 * Versão: 1.0.0 (09/09/2026)
 *
 * Nasce do despacho da Sentinela de 09/09/2026, item 1: `/category/uncategorized/`
 * respondia 200 e estava no `wp-sitemap.xml`. Duas coisas erradas ao mesmo tempo,
 * e a segunda é a cara: domínio novo tem orçamento de rastreamento minúsculo
 * (seção 14.1 do ARQUIPELAGO.md) e o sitemap estava gastando esse orçamento
 * pedindo ao Google que fosse buscar uma página que é artefato do CMS, não
 * conteúdo da ilha. Enquanto isso, as 6 páginas da leva de 08/09 não indexaram.
 *
 * A causa de raiz do "sem categoria" está no Sync: ele grava artigo com
 * wp_insert_post e nunca atribui categoria, então o WordPress joga na padrão.
 * Este snippet conserta pelo lado que se auto-corrige — em vez de mexer no Sync
 * (que só chega ao site pelo atualizador, caminho mais longo e mais arriscado),
 * ele varre a categoria padrão e realoca. Artigo novo que o Sync criar amanhã
 * cai na mesma varredura e é realocado sozinho.
 *
 * Faz cinco coisas:
 *   (a) cria a categoria de verdade "Métodos" e move para ela todo post que
 *       estiver na categoria padrão; e passa a categoria padrão a ser ela, para
 *       o problema não voltar pela porta que o criou;
 *   (b) tira do `wp-sitemap.xml` o provedor de autores (arquivo de autor em site
 *       de um autor só é duplicata da lista de posts) e o de taxonomias enquanto
 *       nenhuma categoria estiver curada — sitemap é curadoria, não inventário;
 *   (c) manda `noindex, follow` para arquivo por data, autor, tag, categoria não
 *       curada (a "sem categoria" inclusive), anexo, busca e 404 — pelo filtro
 *       `wp_robots` do núcleo, que é quem imprime a meta, para não sair meta
 *       repetida na página;
 *   (d) desliga a página de anexo pelo interruptor do próprio núcleo
 *       (`wp_attachment_pages_enabled`), em vez de redirecionar por conta própria;
 *   (e) não toca em página, artigo nem na home: essas são o conteúdo da ilha e
 *       precisam ser indexadas.
 *
 * A CATEGORIA "MÉTODOS" NASCE FORA DO SITEMAP E COM `noindex`, DE PROPÓSITO.
 * O item 2 do mesmo despacho congelou página nova até 16/09, porque a leva de
 * 08/09 não indexou; e a seção 14.4 do ARQUIPELAGO.md diz que listagem só existe
 * com texto próprio explicando o critério. Enquanto ela não tiver esse texto, ela
 * é grade de links — página fina. Quando tiver, basta acrescentar o slug em
 * aquametria_seo_categorias_no_sitemap() e ela entra no sitemap e sai do noindex
 * na mesma linha. O que o despacho pedia — o artigo sair de `uncategorized` — já
 * está feito aqui: o que muda depois é só quem entra no sitemap.
 *
 * A decisão de indexar mora numa função pura (aquametria_seo_deve_noindex), que
 * recebe um mapa de contexto em vez de chamar as condicionais do WordPress. É o
 * que deixa `ferramentas/teste-seo-tecnico.php` exercitar as 20 combinações sem
 * subir WordPress nenhum — e verificação que não roda não protege ninguém.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe), sem a
 * superglobal de servidor, toda função dentro de function_exists, texto de tela
 * acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_SEO_VERSAO' ) ) {
	define( 'AQUAMETRIA_SEO_VERSAO', '1.0.0' );
	define( 'AQUAMETRIA_SEO_CATEGORIA_SLUG', 'metodos' );
	define( 'AQUAMETRIA_SEO_CATEGORIA_NOME', 'Métodos' );
}

/* ---------------------------------------------------------------------------
 * 1. Quais categorias podem entrar no sitemap
 *
 * Lista de slugs, hoje vazia de propósito (ver o cabeçalho). Categoria só entra
 * aqui quando tiver: 3 itens ou mais, texto próprio explicando o critério, e a
 * autorização da rampa de indexação. Enquanto a lista estiver vazia, o provedor
 * de taxonomias inteiro sai do sitemap — é mais honesto do que publicar um
 * sitemap de taxonomias com zero URL dentro.
 * ------------------------------------------------------------------------ */
if ( ! function_exists( 'aquametria_seo_categorias_no_sitemap' ) ) {
function aquametria_seo_categorias_no_sitemap() {
	$slugs = array();
	return array_values( array_unique( array_filter( (array) apply_filters( 'aquametria_seo_categorias_no_sitemap', $slugs ) ) ) );
}
}

/* ---------------------------------------------------------------------------
 * 2. A decisão de indexar — função pura, testada fora do WordPress
 *
 * Recebe o contexto já resolvido em booleanos e devolve se a URL deve sair da
 * indexação. Nunca chama condicional do WordPress: é isso que a torna testável.
 * A ordem das perguntas importa — anexo também é "singular", e 404 também pode
 * cair em contexto de arquivo.
 * ------------------------------------------------------------------------ */
if ( ! function_exists( 'aquametria_seo_deve_noindex' ) ) {
function aquametria_seo_deve_noindex( $ctx ) {
	$c = array_merge( array(
		'anexo'            => false,
		'erro_404'         => false,
		'busca'            => false,
		'data'             => false,
		'autor'            => false,
		'tag'              => false,
		'categoria'        => false,
		'categoria_curada' => false,
		'indice_do_blog'   => false,
		'pagina_inicial'   => false,
		'singular'         => false,
	), (array) $ctx );

	if ( $c['anexo'] || $c['erro_404'] || $c['busca'] ) {
		return true;
	}
	if ( $c['data'] || $c['autor'] || $c['tag'] ) {
		return true;
	}
	if ( $c['categoria'] ) {
		return empty( $c['categoria_curada'] );
	}
	if ( $c['indice_do_blog'] && ! $c['pagina_inicial'] ) {
		return true;
	}
	/* Página, artigo e home ficam indexáveis. O padrão é indexar: se um contexto
	   novo aparecer e não estiver listado acima, é melhor ele ser rastreado e a
	   ronda pegar do que sumir do índice em silêncio. */
	return false;
}
}

/* ---------------------------------------------------------------------------
 * 3. Contexto real do WordPress, traduzido para o mapa da função pura
 * ------------------------------------------------------------------------ */
if ( ! function_exists( 'aquametria_seo_contexto_atual' ) ) {
function aquametria_seo_contexto_atual() {
	$curada = false;
	if ( is_category() ) {
		$termo = get_queried_object();
		if ( $termo && isset( $termo->slug ) ) {
			$curada = in_array( $termo->slug, aquametria_seo_categorias_no_sitemap(), true );
		}
	}
	return array(
		'anexo'            => is_attachment(),
		'erro_404'         => is_404(),
		'busca'            => is_search(),
		'data'             => is_date(),
		'autor'            => is_author(),
		'tag'              => is_tag(),
		'categoria'        => is_category(),
		'categoria_curada' => $curada,
		'indice_do_blog'   => is_home(),
		'pagina_inicial'   => is_front_page(),
		'singular'         => is_singular(),
	);
}
}

/* O núcleo imprime a meta a partir deste filtro (wp_robots, no wp_head). Usar o
   filtro em vez de imprimir a meta na mão evita a armadilha de sair duas metas
   "robots" na mesma página, que é o tipo de coisa que o Google resolve pelo lado
   mais restritivo. */
add_filter( 'wp_robots', 'aquametria_seo_robots' );
if ( ! function_exists( 'aquametria_seo_robots' ) ) {
function aquametria_seo_robots( $robots ) {
	if ( is_admin() ) {
		return $robots;
	}
	if ( aquametria_seo_deve_noindex( aquametria_seo_contexto_atual() ) ) {
		$robots['noindex'] = true;
		/* "follow" de propósito: a página não deve ser indexada, mas os links dela
		   para as calculadoras devem continuar valendo como caminho de rastreio. */
		$robots['follow']  = true;
		unset( $robots['max-image-preview'], $robots['max-snippet'], $robots['max-video-preview'] );
	}
	return $robots;
}
}

/* ---------------------------------------------------------------------------
 * 4. Sitemap — curadoria, não inventário (seção 14.1 do ARQUIPELAGO.md)
 * ------------------------------------------------------------------------ */

/* Decisão de provedor isolada em função pura, pelo mesmo motivo da seção 2. */
if ( ! function_exists( 'aquametria_seo_provedor_permitido' ) ) {
function aquametria_seo_provedor_permitido( $nome, $categorias_curadas ) {
	if ( 'users' === $nome ) {
		return false; /* um autor só; o arquivo dele é a lista de posts outra vez */
	}
	if ( 'taxonomies' === $nome ) {
		return count( (array) $categorias_curadas ) > 0;
	}
	return true;
}
}

add_filter( 'wp_sitemaps_add_provider', 'aquametria_seo_filtrar_provedor', 10, 2 );
if ( ! function_exists( 'aquametria_seo_filtrar_provedor' ) ) {
function aquametria_seo_filtrar_provedor( $provedor, $nome ) {
	/* Devolver algo que não seja WP_Sitemaps_Provider tira o provedor — é assim
	   que o próprio núcleo documenta a remoção. */
	return aquametria_seo_provedor_permitido( $nome, aquametria_seo_categorias_no_sitemap() ) ? $provedor : false;
}
}

/* Se um dia a lista tiver slug, o provedor de taxonomias volta — e aí estas duas
   travas garantem que volte só com o que foi curado, nunca com a "sem categoria"
   nem com tag gerada. */
add_filter( 'wp_sitemaps_taxonomies', 'aquametria_seo_filtrar_taxonomias' );
if ( ! function_exists( 'aquametria_seo_filtrar_taxonomias' ) ) {
function aquametria_seo_filtrar_taxonomias( $taxonomias ) {
	return array_intersect_key( (array) $taxonomias, array( 'category' => true ) );
}
}

add_filter( 'wp_sitemaps_taxonomies_query_args', 'aquametria_seo_filtrar_termos', 10, 2 );
if ( ! function_exists( 'aquametria_seo_filtrar_termos' ) ) {
function aquametria_seo_filtrar_termos( $args, $taxonomia ) {
	if ( 'category' !== $taxonomia ) {
		return $args;
	}
	$slugs = aquametria_seo_categorias_no_sitemap();
	if ( ! $slugs ) {
		/* Sem categoria curada não existe termo elegível. 'include' com um id que
		   não existe devolve lista vazia sem depender de o provedor ter sido
		   removido antes — cinto e suspensório, porque quem lê o sitemap é robô. */
		$args['include'] = array( 0 );
		return $args;
	}
	$args['slug'] = $slugs;
	return $args;
}
}

/* ---------------------------------------------------------------------------
 * 5. A categoria de verdade, e o esvaziamento da "sem categoria"
 * ------------------------------------------------------------------------ */

/* A "sem categoria" é procurada pelo slug ANTES da opção default_category,
   porque a seção 5c troca essa opção — depois da troca, a opção aponta para a
   categoria nova e não serve mais para achar a antiga. */
if ( ! function_exists( 'aquametria_seo_termo_sem_categoria' ) ) {
function aquametria_seo_termo_sem_categoria() {
	foreach ( array( 'uncategorized', 'sem-categoria' ) as $slug ) {
		$termo = get_term_by( 'slug', $slug, 'category' );
		if ( $termo && ! is_wp_error( $termo ) ) {
			return $termo;
		}
	}
	$padrao = (int) get_option( 'default_category' );
	if ( $padrao ) {
		$termo = get_term( $padrao, 'category' );
		if ( $termo && ! is_wp_error( $termo ) ) {
			return $termo;
		}
	}
	return null;
}
}

if ( ! function_exists( 'aquametria_seo_categoria_real' ) ) {
function aquametria_seo_categoria_real() {
	$termo = get_term_by( 'slug', AQUAMETRIA_SEO_CATEGORIA_SLUG, 'category' );
	if ( $termo && ! is_wp_error( $termo ) ) {
		return (int) $termo->term_id;
	}
	$novo = wp_insert_term( AQUAMETRIA_SEO_CATEGORIA_NOME, 'category', array(
		'slug'        => AQUAMETRIA_SEO_CATEGORIA_SLUG,
		'description' => 'Os textos que explicam de onde sai cada número das calculadoras da Aquametria: qual é a fórmula, qual é a fonte do fabricante e em que caso a regra de bolso do mercado erra.',
	) );
	if ( is_wp_error( $novo ) ) {
		/* term_exists com outro slug: aproveita o que já existe em vez de insistir. */
		$dado = $novo->get_error_data();
		return is_array( $dado ) && isset( $dado['term_id'] ) ? (int) $dado['term_id'] : ( is_numeric( $dado ) ? (int) $dado : 0 );
	}
	return isset( $novo['term_id'] ) ? (int) $novo['term_id'] : 0;
}
}

if ( ! function_exists( 'aquametria_seo_esvaziar_sem_categoria' ) ) {
function aquametria_seo_esvaziar_sem_categoria() {
	$antiga = aquametria_seo_termo_sem_categoria();
	if ( ! $antiga ) {
		return 0;
	}
	$nova = aquametria_seo_categoria_real();
	if ( ! $nova || (int) $antiga->term_id === $nova ) {
		return 0;
	}

	$posts = get_posts( array(
		'post_type'        => 'post',
		'post_status'      => array( 'publish', 'draft', 'pending', 'private', 'future' ),
		'numberposts'      => 100,
		'fields'           => 'ids',
		'category'         => (int) $antiga->term_id,
		'suppress_filters' => false,
	) );
	$movidos = 0;
	foreach ( $posts as $pid ) {
		$atuais = wp_get_post_categories( $pid );
		$atuais = array_values( array_diff( array_map( 'intval', (array) $atuais ), array( (int) $antiga->term_id ) ) );
		if ( ! in_array( $nova, $atuais, true ) ) {
			$atuais[] = $nova;
		}
		/* Post nunca pode ficar sem categoria nenhuma: o WordPress devolveria a
		   padrão na hora, e a varredura entraria em laço eterno. */
		if ( ! $atuais ) {
			$atuais = array( $nova );
		}
		$r = wp_set_post_categories( $pid, $atuais, false );
		if ( ! is_wp_error( $r ) ) {
			$movidos++;
		}
	}
	if ( $movidos ) {
		wp_update_term_count_now( array( (int) $antiga->term_id, $nova ), 'category' );
	}
	return $movidos;
}
}

/* 5c. A categoria padrão passa a ser a de verdade. Sem isto, o Sync volta a
   despejar artigo novo na "sem categoria" a cada publicação, e a varredura acima
   viraria trabalho eterno em vez de conserto. */
if ( ! function_exists( 'aquametria_seo_ajustar_categoria_padrao' ) ) {
function aquametria_seo_ajustar_categoria_padrao() {
	$antiga = aquametria_seo_termo_sem_categoria();
	$atual  = (int) get_option( 'default_category' );
	if ( ! $antiga || $atual !== (int) $antiga->term_id ) {
		return false; /* já foi trocada, ou o Raphael escolheu outra à mão */
	}
	$nova = aquametria_seo_categoria_real();
	if ( ! $nova || $nova === $atual ) {
		return false;
	}
	update_option( 'default_category', $nova );
	return true;
}
}

/* 5d. Página de anexo desligada pelo interruptor do próprio núcleo. Instalação
   nova do WordPress já nasce assim; a Aquametria nasceu em 06/09 e o valor não
   foi conferido, então confere-se aqui — uma leitura de opção autoloaded por
   requisição, e escrita só na primeira vez. */
if ( ! function_exists( 'aquametria_seo_desligar_pagina_de_anexo' ) ) {
function aquametria_seo_desligar_pagina_de_anexo() {
	if ( '0' !== (string) get_option( 'wp_attachment_pages_enabled' ) ) {
		update_option( 'wp_attachment_pages_enabled', 0 );
		return true;
	}
	return false;
}
}

/* ---------------------------------------------------------------------------
 * 6. Partida
 *
 * A varredura da seção 5 custa uma consulta; por isso ela só acontece quando a
 * "sem categoria" ainda tem post dentro. Quando o conserto terminar, a contagem
 * zera e este boot passa a não fazer nada — que é o comportamento que se quer de
 * um snippet que roda em toda requisição.
 * ------------------------------------------------------------------------ */
add_action( 'init', 'aquametria_seo_boot', 30 );
if ( ! function_exists( 'aquametria_seo_boot' ) ) {
function aquametria_seo_boot() {
	aquametria_seo_desligar_pagina_de_anexo();

	$antiga = aquametria_seo_termo_sem_categoria();
	if ( $antiga && (int) $antiga->count > 0 ) {
		aquametria_seo_esvaziar_sem_categoria();
	}
	aquametria_seo_ajustar_categoria_padrao();
}
}

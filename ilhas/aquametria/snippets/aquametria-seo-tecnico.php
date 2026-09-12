/**
 * Aquametria SEO Técnico — sitemap curado, diretiva de robôs e meta description
 * Versão: 1.1.0 (10/09/2026)
 *
 * v1.1.0 (10/09/2026) — despacho da Sentinela de 10/09, item 1: NENHUMA das 13
 * URLs do sitemap servia `<meta name="description">`, e nenhuma página tinha uma
 * única tag `og:`. O `<head>` trazia 6 elementos `<meta>` e nenhum deles era a
 * description. Isso é caro por dois motivos somados: a meta description é metade
 * da alavanca de CTR da seção 12.1 do ARQUIPELAGO.md (a outra metade é o título),
 * e sem ela quem escreve o resumo do resultado é o Google, recortando um pedaço
 * qualquer do corpo — numa página de calculadora, o pedaço costuma ser o rótulo
 * de um campo de formulário. A meta desta ilha é tráfego, e tráfego passa por
 * clique.
 *
 * A DESCRIÇÃO NÃO É ESCRITA AQUI. O mapa entre os marcadores METAS-INICIO e
 * METAS-FIM é gerado por `ferramentas/gerar-metas-descricao.py`, que lê o campo
 * `meta_descricao` do front matter de cada página de `conteudo/` e o
 * `dados/metas-seo.json` das quatro páginas da casca, e RECUSA gerar se algum
 * texto sair de 120 a 160 caracteres, se dois forem iguais, ou se algum slug do
 * sitemap ficar sem descrição. É o mesmo desenho do favicon (seção 2b da casca):
 * texto mantido em dois lugares diverge em silêncio.
 *
 * PÁGINA FORA DO MAPA NÃO GANHA DESCRIÇÃO INVENTADA. Se um slug não estiver no
 * mapa, o snippet não imprime nada e deixa o `<head>` como estava. Description
 * gerada por recorte automático do corpo é exatamente o que este bloco existe
 * para substituir, e um texto errado escrito por nós seria pior do que o recorte
 * do Google, porque pareceria intencional.
 *
 * SEM `og:image`, DE PROPÓSITO. A ilha não tem imagem de compartilhamento — o
 * favicon é um SVG de 32 px embutido como data URI, e `og:image` exige URL
 * absoluta de arquivo real. Declarar uma imagem que não existe faria o cartão
 * quebrar no lugar de não aparecer. Ela entra quando a vitrine do T8 der à ilha
 * a primeira imagem própria hospedada.
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
	define( 'AQUAMETRIA_SEO_VERSAO', '1.1.0' );
	define( 'AQUAMETRIA_SEO_CATEGORIA_SLUG', 'metodos' );
	define( 'AQUAMETRIA_SEO_CATEGORIA_NOME', 'Métodos' );
	define( 'AQUAMETRIA_SEO_NOME_DO_SITE', 'Aquametria' );
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
 * 3b. Meta description e cartão de compartilhamento
 *
 * O mapa abaixo é gerado — ver o cabeçalho. Depois dele vêm três funções: a que
 * descobre o slug da URL servida, a função PURA que monta a lista de tags, e o
 * gancho que imprime. A separação existe pelo mesmo motivo da seção 2:
 * `ferramentas/teste-seo-tecnico.php` exercita a montagem sem subir WordPress
 * nenhum, e verificação que não roda não protege ninguém.
 * ------------------------------------------------------------------------ */

/* METAS-INICIO — gerado por ferramentas/gerar-metas-descricao.py, nao edite a mao */
if ( ! function_exists( 'aquametria_seo_metas_por_slug' ) ) {
function aquametria_seo_metas_por_slug() {
	return array(
		'inicio' => array(
			'titulo'    => 'As contas do seu aquário',
			'descricao' => 'Quantos litros tem o seu aquário? E quantos watts de aquecedor, qual filtro, quanta luz? As contas do seu aquário, com a fonte de cada número.',
		),
		'calculadoras' => array(
			'titulo'    => 'Calculadoras',
			'descricao' => 'As contas do seu aquário em um lugar só: litros, vazão do filtro, watts do aquecedor, mídia filtrante e luz — cada uma com a fonte do número.',
		),
		'metodologia' => array(
			'titulo'    => 'Como a gente calcula',
			'descricao' => 'De onde sai cada número da Aquametria: o manual do fabricante, a data em que foi conferido e a faixa inteira quando as fontes discordam.',
		),
		'sobre' => array(
			'titulo'    => 'Sobre',
			'descricao' => 'Quem publica a Aquametria e por quê: um site de aquarismo que mostra a conta, cita o manual do fabricante e recusa número sem fonte declarada.',
		),
		'calculadora-de-litragem' => array(
			'titulo'    => 'Quantos litros tem o seu aquário?',
			'descricao' => 'Quantos litros tem o seu aquário? Informe as medidas em centímetros e receba os três volumes: o bruto da etiqueta, o interno e a água real.',
		),
		'calculadora-de-vazao-do-filtro' => array(
			'titulo'    => 'Qual filtro dá conta do seu aquário?',
			'descricao' => 'Qual a vazão de filtro para o seu aquário, em L/h? A faixa vai de 1,76 a 10 renovações por hora, e cada extremo aparece com a fonte dele.',
		),
		'calculadora-de-potencia-do-aquecedor' => array(
			'titulo'    => 'Quantos watts de aquecedor você precisa?',
			'descricao' => 'Quantos watts de aquecedor o seu aquário pede? A conta parte da mínima do seu cômodo, não do genérico 1 W por litro, e filtra pela sua voltagem.',
		),
		'calculadora-de-midia-filtrante' => array(
			'titulo'    => 'Quanta mídia biológica cabe no seu filtro?',
			'descricao' => 'Quanta mídia filtrante o seu aquário pede, em mililitros? Quatro fabricantes declaram dosagens que variam dez vezes; aqui estão as quatro.',
		),
		'calculadora-de-iluminacao' => array(
			'titulo'    => 'Quanta luz o seu aquário precisa?',
			'descricao' => 'Quantos lúmens o seu aquário plantado precisa? A faixa pelas três leituras brasileiras que discordam, mais fotoperíodo, Kelvin e consumo por mês.',
		),
		'divulgacao-de-afiliados' => array(
			'titulo'    => 'Como a Aquametria ganha dinheiro',
			'descricao' => 'A Aquametria recebe comissão por alguns links de loja. O que isso muda na ordem dos produtos recomendados: nada. O critério inteiro, por escrito.',
		),
		'quantos-watts-de-aquecedor-para-aquario' => array(
			'titulo'    => 'Por que o 1 W por litro erra para o mesmo lado',
			'descricao' => 'O 1 W por litro não veio de um cálculo, veio da prateleira. De onde a regra saiu, quando ela acerta por acidente e o que muda ao medir o cômodo.',
		),
		'quanta-midia-biologica-o-aquario-precisa' => array(
			'titulo'    => 'Cada marca pede uma dose diferente de mídia',
			'descricao' => 'Seachem pede 1,25 mL de mídia por litro; Ocean Tech pede 12,5. Dez vezes de diferença para o mesmo trabalho — fomos às declarações originais.',
		),
		'quantos-lumens-por-litro-aquario-plantado' => array(
			'titulo'    => 'Quantos lúmens por litro o aquário plantado precisa',
			'descricao' => 'Três fontes brasileiras chamam a mesma faixa de lúmens por litro com o dobro do número. De onde vem a regra e por que o lúmen é a unidade errada.',
		),
		'corydoras' => array(
			'titulo'    => 'Coridoras: quanto chão o grupo pede',
			'descricao' => 'Coridora se dimensiona pelo chão, não pelo litro: porte, cardume mínimo e base mínima das quatro espécies, com a fonte de cada linha.',
		),
		'peixes' => array(
			'titulo'    => 'Quanto espaço cada peixe pede',
			'descricao' => 'Quanto espaço cada peixe pede, em centímetros de chão e não em litros: o mínimo declarado por fonte com nome e data, espécie por espécie.',
		),
		'quantos-litros-para-coridora-bronze' => array(
			'titulo'    => 'Quantos litros para um cardume de coridora bronze?',
			'descricao' => 'Quantos litros para um cardume de coridora bronze? A base de 80 x 30 cm que a fonte declara, com nome e data, e a conta pelas duas réguas.',
		),
		'quantos-litros-para-coridora-panda' => array(
			'titulo'    => 'Quantos litros para um cardume de coridora panda?',
			'descricao' => 'Quantos litros para um cardume de coridora panda? A base de 45 x 30 cm que a fonte declara — a menor do banco — e a conta em litros.',
		),
		'quantos-litros-para-coridora-pimenta' => array(
			'titulo'    => 'Quantos litros para um cardume de coridora pimenta?',
			'descricao' => 'Quantos litros para um cardume de coridora pimenta? A base mínima declarada por duas fontes que discordam, com os dois números na tela.',
		),
		'quantos-litros-para-coridora-sterbai' => array(
			'titulo'    => 'Quantos litros para um cardume de coridora sterbai?',
			'descricao' => 'Quantos litros para um cardume de coridora sterbai? A base e o cardume mínimo que a ficha da espécie declara, com nome da fonte e data.',
		),
		'quantos-litros-para-mato-grosso' => array(
			'titulo'    => 'Quantos litros para um cardume de mato-grosso?',
			'descricao' => 'Quantos litros para um cardume de mato-grosso? As duas fontes discordam da frente mínima, e esta página publica as duas com o nome de cada uma.',
		),
		'quantos-litros-para-rodostomo' => array(
			'titulo'    => 'Quantos litros para um cardume de rodóstomo?',
			'descricao' => 'Quantos litros para um cardume de rodóstomo? A fonte declara 90 cm de comprimento e nenhuma largura — e esta página diz isso em vez de inventar.',
		),
		'quantos-litros-para-tetra-brilhante' => array(
			'titulo'    => 'Quantos litros para um cardume de tetra-brilhante?',
			'descricao' => 'Quantos litros para um cardume de tetra-brilhante? A base declarada, a divergência de um exemplar no cardume e a conta pelas duas réguas.',
		),
		'quantos-litros-para-tetra-cardinal' => array(
			'titulo'    => 'Quantos litros para um cardume de neon cardinal?',
			'descricao' => 'Quantos litros para um cardume de neon cardinal? A base declarada pela fonte, o cardume mínimo de 8 e a conta em litros pelas duas réguas.',
		),
		'quantos-litros-para-tetra-ember' => array(
			'titulo'    => 'Quantos litros para um cardume de tetra ember?',
			'descricao' => 'Quantos litros para um cardume de tetra ember? A base de 45 × 30 cm que a fonte declara, o cardume mínimo de 8 e a conta pelas duas réguas.',
		),
		'quantos-litros-para-tetra-negro' => array(
			'titulo'    => 'Quantos litros para um cardume de tetra-negro?',
			'descricao' => 'Quantos litros para um cardume de tetra-negro? Cardume mínimo de 5, base declarada de 75 × 30 cm e a divergência de 15 cm entre as duas fontes.',
		),
		'quantos-litros-para-tetra-neon' => array(
			'titulo'    => 'Quantos litros para um cardume de tetra neon?',
			'descricao' => 'Quantos litros para um cardume de tetra neon? A base que a fonte declara, a conta pelas duas réguas de lotação e quantos cabem no seu aquário.',
		),
		'tetras' => array(
			'titulo'    => 'Tetras: quantos litros o cardume pede',
			'descricao' => 'Porte, cardume mínimo e frente mínima dos tetras lado a lado, com a fonte de cada linha — e a conta em litros pelas duas réguas brasileiras.',
		),
	);
}
}
/* METAS-FIM */

/* Qual página está sendo servida, em uma palavra: o `post_name`. Serve para
   página e para artigo com o mesmo código, e é o que o mapa usa como chave — a
   URL do artigo carrega o prefixo de data, que não é dele e mudaria junto com a
   estrutura de permalink. A home é resolvida pela opção `page_on_front` antes de
   qualquer outra pergunta: ela é uma página como as outras, mas a URL dela é a
   raiz, e `get_queried_object()` na raiz depende de o tema não ter mexido na
   consulta principal. */
if ( ! function_exists( 'aquametria_seo_slug_atual' ) ) {
function aquametria_seo_slug_atual() {
	if ( is_front_page() ) {
		$id = (int) get_option( 'page_on_front' );
		if ( $id ) {
			$nome = get_post_field( 'post_name', $id );
			return is_string( $nome ) ? $nome : '';
		}
		return '';
	}
	if ( ! is_singular() ) {
		return '';
	}
	$obj = get_queried_object();
	return ( $obj && isset( $obj->post_name ) ) ? (string) $obj->post_name : '';
}
}

/* Função pura: recebe o que já foi resolvido e devolve a lista de tags como
   pares nome/valor, sem escapar nada. Quem escapa é o gancho, uma vez, no ponto
   em que o valor vira HTML — misturar as duas coisas é como nasce escape duplo.
   Slug fora do mapa devolve lista vazia, e o `<head>` fica como estava. */
if ( ! function_exists( 'aquametria_seo_tags_da_pagina' ) ) {
function aquametria_seo_tags_da_pagina( $slug, $metas, $url, $nome_do_site ) {
	$slug  = (string) $slug;
	$metas = (array) $metas;
	if ( '' === $slug || ! isset( $metas[ $slug ] ) ) {
		return array();
	}
	$item      = (array) $metas[ $slug ];
	$descricao = isset( $item['descricao'] ) ? trim( (string) $item['descricao'] ) : '';
	$titulo    = isset( $item['titulo'] ) ? trim( (string) $item['titulo'] ) : '';
	if ( '' === $descricao ) {
		return array();
	}

	$tags = array(
		array( 'tipo' => 'name', 'chave' => 'description', 'valor' => $descricao ),
		array( 'tipo' => 'property', 'chave' => 'og:description', 'valor' => $descricao ),
		array( 'tipo' => 'property', 'chave' => 'og:type', 'valor' => 'website' ),
		array( 'tipo' => 'property', 'chave' => 'og:locale', 'valor' => 'pt_BR' ),
		array( 'tipo' => 'name', 'chave' => 'twitter:card', 'valor' => 'summary' ),
	);
	if ( '' !== $titulo ) {
		array_splice( $tags, 2, 0, array(
			array( 'tipo' => 'property', 'chave' => 'og:title', 'valor' => $titulo ),
		) );
	}
	if ( '' !== trim( (string) $nome_do_site ) ) {
		$tags[] = array( 'tipo' => 'property', 'chave' => 'og:site_name', 'valor' => trim( (string) $nome_do_site ) );
	}
	/* A URL vai por último e só se existir: `og:url` com endereço errado é pior
	   do que `og:url` ausente, porque manda o compartilhamento para outro lugar. */
	if ( '' !== trim( (string) $url ) ) {
		$tags[] = array( 'tipo' => 'property', 'chave' => 'og:url', 'valor' => trim( (string) $url ), 'url' => true );
	}
	return $tags;
}
}

/* Prioridade 3: depois do ícone da casca (5 é a dela) não importa para o robô,
   mas o `<head>` fica legível para quem abre o código-fonte, e a description
   perto do topo é o que se espera de encontrar. */
add_action( 'wp_head', 'aquametria_seo_imprimir_metas', 3 );
if ( ! function_exists( 'aquametria_seo_imprimir_metas' ) ) {
function aquametria_seo_imprimir_metas() {
	if ( is_admin() || ! function_exists( 'aquametria_seo_metas_por_slug' ) ) {
		return;
	}
	$slug = aquametria_seo_slug_atual();
	if ( '' === $slug ) {
		return;
	}

	$url = '';
	if ( is_front_page() ) {
		$url = home_url( '/' );
	} else {
		$obj = get_queried_object();
		if ( $obj && isset( $obj->ID ) ) {
			$permalink = get_permalink( (int) $obj->ID );
			$url       = is_string( $permalink ) ? $permalink : '';
		}
	}

	$tags = aquametria_seo_tags_da_pagina(
		$slug,
		aquametria_seo_metas_por_slug(),
		$url,
		AQUAMETRIA_SEO_NOME_DO_SITE
	);
	foreach ( $tags as $tag ) {
		$valor = empty( $tag['url'] ) ? esc_attr( $tag['valor'] ) : esc_url( $tag['valor'] );
		echo '<meta ' . ( 'property' === $tag['tipo'] ? 'property' : 'name' ) . '="'
			. esc_attr( $tag['chave'] ) . '" content="' . $valor . '">' . "\n";
	}
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

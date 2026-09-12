/**
 * Clube do Mosaico Loja — peças e vitrine
 * Versão 1.0.0 (12/09/2026) — bloco 4d, o CORTE do despacho do Raphael das
 * 18h20 BRT de 12/09/2026: ele vai à casa dos pais no domingo 13/09 ensinar a
 * própria mãe a cadastrar as peças dela, e o que estiver de pé hoje é o que ela
 * vai usar amanhã.
 *
 * Este arquivo é o MODELO e o LADO PÚBLICO (itens 1 e 5 do corte). A área dela
 * mora no outro snippet, `clubedomosaico-atelie.php` (itens 2, 3 e 4), e a
 * separação não é organização: é o Sync desembarcando um sem o outro. Se o
 * painel tiver defeito, a loja no ar não cai com ele; se a loja mudar, a artesã
 * não perde o acesso.
 *
 * ------------------------------------------------------------------------
 * AS SEIS DECISÕES, e a cicatriz que cada uma evita
 * ------------------------------------------------------------------------
 *
 * 1. O CPT NÃO TEM ARQUIVO PRÓPRIO EM /loja/, E ISSO É DELIBERADO.
 *    A especificação de 10/09 pedia `has_archive` em `/loja/`. Só que /loja/ já
 *    é uma PÁGINA desta ilha desde a casca 1.0.0, criada por
 *    `cdm_casca_definicao_paginas()`, com o texto editorial do VOZ.md, a seção
 *    "Como a compra vai funcionar" e a chamada para o Guia — e ela já lista as
 *    peças publicadas, por `cdm_casca_vitrine_de_pecas_html()`. Um arquivo de
 *    CPT no mesmo endereço disputaria a mesma URL com a página e o vencedor
 *    dependeria da ordem das regras de reescrita, que é a última coisa que se
 *    quer decidindo o que o Google vê na véspera de alguém usar o site. Então:
 *    `has_archive => false`, `rewrite` com slug `loja` — a peça nasce em
 *    `/loja/<slug>/`, dois segmentos, e a página de um segmento continua dela.
 *    Nada foi perdido: quem lista as peças é a página, que é melhor que o
 *    arquivo porque tem texto de verdade em volta (seção 8, página fina).
 *
 * 2. A PÁGINA DA PEÇA É MONTADA POR `the_content`, NÃO POR TEMPLATE.
 *    A artesã nunca vê o editor de blocos (é isso que o despacho de 10/09 pede),
 *    então `post_content` da peça é a descrição dela em texto puro e mais nada.
 *    Montar a ficha aqui, num filtro, faz a peça herdar de graça tudo que a
 *    casca já testou: cabeçalho com o logo, trilha da seção 16, H1 do título,
 *    "Veja também", rodapé, favicon, tag do GA4. Escrever um template seria
 *    reconstruir isso e ficar com duas cascas divergindo em silêncio.
 *
 * 3. A TRILHA E O BreadcrumbList SAEM DO MAPA DA CASCA, pelo filtro `cdm_arvore`.
 *    A peça se declara nível 2 com mãe `loja` na hora em que está sendo servida.
 *    Isto é o oposto de imprimir uma trilha própria: quem monta continua sendo
 *    `cdm_casca_trilha_html()` e `cdm_casca_trilha_jsonld()`, com as quatro
 *    decisões que a seção 3d da casca registra (degrau sem página sai em texto,
 *    JSON-LD não carrega degrau sem endereço). Trilha de peça é a MESMA trilha
 *    do resto da ilha, e é por isso que ela não pode ser um segundo código.
 *
 * 4. AS TAXONOMIAS EXISTEM, AS PÁGINAS DELAS NÃO — e isso é orçamento de
 *    rastreamento, não preguiça. `colecao` e `tecnica` são registradas para o
 *    dado existir desde a primeira peça (é o que liga a peça ao resto do site, e
 *    o formulário as cobra), mas com `public => false`: uma taxonomia pública
 *    nasce com arquivo e entra no `wp-sitemap.xml`, e seriam de sete a doze URLs
 *    finas pedindo rastreamento num domínio de dois dias (seção 14.1). As páginas
 *    de coleção e de técnica estão no corte do despacho como o que NÃO entra
 *    hoje; no dia em que entrarem, é uma linha aqui e o texto editorial lá.
 *
 * 5. O BOTÃO É O WHATSAPP DA ARTESÃ, NÃO O FORMULÁRIO DE LEAD.
 *    O adendo 3 de 11/09 (CPT `lead_peca`, notificação por e-mail, aba
 *    "Interessados") está explicitamente FORA do corte de hoje. O despacho pede
 *    "botão de WhatsApp" no item 5, e é ele que sai: `wa.me` com a mensagem
 *    pronta citando a peça, o preço e a disponibilidade reais. Enquanto a option
 *    `cdm_whatsapp` estiver vazia, o botão NÃO é inventado — a ficha diz que o
 *    contato ainda não foi publicado, que é honesto, e nenhuma peça vai ao ar
 *    com um número de telefone que ninguém atende.
 *
 * 6. PEÇA SEM FOTO OU SEM PREÇO NÃO É PUBLICÁVEL, e a régua mora aqui.
 *    `cdm_loja_peca_publicavel()` é a única régua da ilha sobre isso, e é ela que
 *    o painel chama para habilitar o botão Publicar. Duas metades escrevendo a
 *    mesma regra é o defeito que a seção 8 chama de teste que mede a si mesmo:
 *    quem publica e quem confere têm de olhar para a MESMA função, e quem escreve
 *    a régua contrária é o teste, à mão, em `ferramentas/teste-loja.php`.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTA PÁGINA DIZ QUE NÃO SABE
 * ------------------------------------------------------------------------
 * A peça não afirma nada sobre material de fabricante: ela diz a base e a
 * técnica que a artesã declarou, e manda para o Guia quem quiser saber qual cola
 * aquela base pede. É a mesma escada de fontes da ilha vista do outro lado — aqui
 * a fonte é a pessoa que fez a peça, e ela é a melhor fonte que existe sobre a
 * própria peça e nenhuma fonte sobre química de adesivo.
 */

if ( ! defined( 'CDM_LOJA_VERSAO' ) ) {
	define( 'CDM_LOJA_VERSAO', '1.0.0' );
}
if ( ! defined( 'CDM_LOJA_BASE' ) ) {
	/* O primeiro segmento da URL da peça. É o mesmo slug da página /loja/ de
	   propósito: a página é a mãe na árvore (seção 16) e a peça é filha dela,
	   então a URL tem de mostrar isso. */
	define( 'CDM_LOJA_BASE', 'loja' );
}

/* ---------------------------------------------------------------------------
 * 1. O MODELO — o tipo `peca` e as duas taxonomias
 *
 * `show_ui => false` é requisito escrito do Raphael em 10/09: "eu não quero que
 * ela entre numa área wp-admin". O tipo não aparece no menu do WordPress para
 * NINGUÉM, nem para o administrador — quem cadastra é o painel `/atelie/`, e um
 * segundo caminho de cadastro seria um segundo lugar onde a malha automática da
 * peça pode deixar de acontecer.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_registrar' ) ) {
function cdm_loja_registrar() {
	if ( ! function_exists( 'register_post_type' ) ) {
		return;
	}

	register_post_type( 'peca', array(
		'label'               => 'Peças',
		'labels'              => array(
			'name'          => 'Peças',
			'singular_name' => 'Peça',
		),
		'public'              => true,
		'publicly_queryable'  => true,
		'exclude_from_search' => false,
		'show_ui'             => false,
		'show_in_menu'        => false,
		'show_in_nav_menus'   => false,
		'show_in_rest'        => true,
		'rest_base'           => 'pecas',
		'has_archive'         => false,
		'hierarchical'        => false,
		'rewrite'             => array( 'slug' => CDM_LOJA_BASE, 'with_front' => false ),
		'query_var'           => true,
		/* Capacidades PRÓPRIAS, e é o que permite o papel `artesa` existir sem
		   receber nada de post comum: com `map_meta_cap` o núcleo traduz
		   edit_post/delete_post nas capacidades de baixo olhando o AUTOR, e é
		   assim que ela mexe só nas peças dela sem uma linha de verificação
		   nossa no meio do caminho. */
		'capability_type'     => array( 'peca', 'pecas' ),
		'map_meta_cap'        => true,
		'supports'            => array( 'title', 'editor', 'thumbnail', 'author', 'revisions' ),
		'taxonomies'          => array( 'colecao', 'tecnica' ),
		'menu_icon'           => 'dashicons-art',
	) );

	/* AS DUAS TAXONOMIAS SÃO PRIVADAS HOJE (decisão 4 do cabeçalho). O dado
	   existe, a URL não. */
	register_taxonomy( 'colecao', array( 'peca' ), array(
		'label'              => 'Coleções',
		'hierarchical'       => true,
		'public'             => false,
		'publicly_queryable' => false,
		'show_ui'            => false,
		'show_in_rest'       => true,
		'rewrite'            => false,
	) );

	register_taxonomy( 'tecnica', array( 'peca' ), array(
		'label'              => 'Técnicas',
		'hierarchical'       => true,
		'public'             => false,
		'publicly_queryable' => false,
		'show_ui'            => false,
		'show_in_rest'       => true,
		'rewrite'            => false,
	) );
}
}

if ( ! function_exists( 'cdm_loja_termos_iniciais' ) ) {
/**
 * Os termos que o formulário oferece no dia 1.
 *
 * São as palavras do VOZ.md ("palavras que a pessoa usa"), não o vocabulário da
 * técnica: a coleção é o USO (é assim que quem compra escolhe — "presente",
 * "centro de mesa"), e a técnica é o nome que a artesã usa para o que ela fez.
 * A lista é curta de propósito: campo de escolha com vinte opções é campo que
 * ela vai errar no celular.
 */
function cdm_loja_termos_iniciais() {
	return array(
		'colecao' => array(
			'centro-de-mesa' => 'Centro de mesa',
			'presentes'      => 'Presentes',
			'jardim'         => 'Jardim e varanda',
			'parede'         => 'Parede e quadros',
			'joias'          => 'Colares e joias',
		),
		'tecnica' => array(
			'direto'    => 'Direto',
			'indireto'  => 'Indireto',
			'bizantino' => 'Bizantino',
			'trencadis' => 'Trencadís (caquinho)',
		),
	);
}
}

if ( ! function_exists( 'cdm_loja_garantir_termos' ) ) {
/**
 * Cria os termos que faltam, uma vez, e devolve o relato do que fez.
 *
 * Nunca apaga nem renomeia termo que já existe: o dia em que a artesã tiver
 * peça publicada numa coleção, mexer no termo move a peça de lugar.
 */
function cdm_loja_garantir_termos() {
	$relato = array();
	if ( ! function_exists( 'term_exists' ) || ! function_exists( 'wp_insert_term' ) ) {
		return $relato;
	}
	foreach ( cdm_loja_termos_iniciais() as $taxonomia => $termos ) {
		foreach ( $termos as $slug => $nome ) {
			if ( term_exists( $slug, $taxonomia ) ) {
				continue;
			}
			$r = wp_insert_term( $nome, $taxonomia, array( 'slug' => $slug ) );
			$relato[] = is_wp_error( $r )
				? $taxonomia . '/' . $slug . ': erro — ' . $r->get_error_message()
				: $taxonomia . '/' . $slug . ': criado';
		}
	}
	return $relato;
}
}

add_action( 'init', 'cdm_loja_registrar', 5 );

/* Os termos depois do registro das taxonomias, na mesma passada do `init`. */
add_action( 'init', function () {
	if ( ! function_exists( 'get_option' ) ) {
		return;
	}
	$marca = get_option( 'cdm_loja_termos' );
	if ( CDM_LOJA_VERSAO === $marca ) {
		return;
	}
	$relato = cdm_loja_garantir_termos();
	update_option( 'cdm_loja_termos', CDM_LOJA_VERSAO, false );
	if ( $relato ) {
		update_option( 'cdm_loja_termos_relato', $relato, false );
	}
}, 6 );

/* A REGRA DE REESCRITA NASCE SOZINHA. Mesma cicatriz que a casca 1.6.0 pagou com
   a F1 nascendo 404: registrar o tipo não cria a regra na base, e sem a regra a
   peça publicada responde 404 até alguém salvar os permalinks no wp-admin — que
   é exatamente o lugar onde a artesã não entra. A chave é a versão MAIS o slug
   base, porque trocar o slug também exige remontar. */
add_action( 'init', function () {
	if ( ! function_exists( 'get_option' ) ) {
		return;
	}
	$chave = CDM_LOJA_VERSAO . '|' . CDM_LOJA_BASE;
	if ( get_option( 'cdm_loja_reescrita' ) === $chave ) {
		return;
	}
	flush_rewrite_rules( false );
	update_option( 'cdm_loja_reescrita', $chave, false );
}, 99 );

/* ---------------------------------------------------------------------------
 * 2. OS CAMPOS DA PEÇA — um lugar só, lido pelos dois lados
 *
 * O painel escreve por aqui e a ficha lê por aqui. Duas listas de campos, uma no
 * formulário e outra na página, é o defeito que faz a artesã preencher peso e o
 * site nunca mostrar peso — sem erro nenhum, e sem ninguém notando.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_campos' ) ) {
/**
 * A definição dos metadados da peça.
 *
 *   'rotulo'  — o nome na tela, no vocabulário do VOZ.md
 *   'tipo'    — decimal | inteiro | texto | escolha
 *   'ajuda'   — a linha curta embaixo do campo no painel
 *   'unidade' — o que sai depois do número na ficha
 */
function cdm_loja_campos() {
	return array(
		'_cdm_preco' => array(
			'rotulo'  => 'Preço',
			'tipo'    => 'decimal',
			'ajuda'   => 'Só o número, em reais. Ex.: 180 ou 180,50.',
			'unidade' => '',
		),
		'_cdm_disponibilidade' => array(
			'rotulo'  => 'Disponibilidade',
			'tipo'    => 'escolha',
			'opcoes'  => array(
				'pronta_entrega' => 'Pronta entrega',
				'sob_encomenda'  => 'Sob encomenda',
			),
			'ajuda'   => 'Pronta entrega é peça que já está feita, na sua mão.',
			'unidade' => '',
		),
		'_cdm_prazo_dias' => array(
			'rotulo'  => 'Prazo para fazer',
			'tipo'    => 'inteiro',
			'ajuda'   => 'Em dias, só para peça sob encomenda. Deixe vazio se for pronta entrega.',
			'unidade' => 'dias',
		),
		'_cdm_medidas' => array(
			'rotulo'  => 'Medidas',
			'tipo'    => 'texto',
			'ajuda'   => 'Altura × largura × profundidade, em cm. Ex.: 22 × 15 × 15.',
			'unidade' => 'cm',
		),
		'_cdm_peso_g' => array(
			'rotulo'  => 'Peso',
			'tipo'    => 'inteiro',
			'ajuda'   => 'Em gramas. Serve para calcular o frete.',
			'unidade' => 'g',
		),
		'_cdm_base' => array(
			'rotulo'  => 'Base da peça',
			'tipo'    => 'escolha',
			'opcoes'  => array(
				'ceramica' => 'Cerâmica ou barro',
				'vidro'    => 'Vidro',
				'mdf'      => 'MDF ou madeira',
				'cimento'  => 'Cimento ou concreto',
				'metal'    => 'Metal',
				'outra'    => 'Outra',
			),
			'ajuda'   => 'O que estava embaixo do mosaico.',
			'unidade' => '',
		),
		'_cdm_cores' => array(
			'rotulo'  => 'Cores',
			'tipo'    => 'texto',
			'ajuda'   => 'Como você diria por telefone. Ex.: azul, verde e dourado.',
			'unidade' => '',
		),
		'_cdm_quantidade' => array(
			'rotulo'  => 'Quantas você tem',
			'tipo'    => 'inteiro',
			'ajuda'   => 'Quase sempre 1, porque cada peça é única.',
			'unidade' => '',
		),
	);
}
}

if ( ! function_exists( 'cdm_loja_meta' ) ) {
/** O valor de um campo da peça, sempre como texto, nunca false. */
function cdm_loja_meta( $id, $chave ) {
	$v = get_post_meta( (int) $id, $chave, true );
	return is_scalar( $v ) ? (string) $v : '';
}
}

if ( ! function_exists( 'cdm_loja_galeria' ) ) {
/**
 * Os IDs das fotos da peça, em ordem, só os que ainda são anexo de verdade.
 *
 * A ordem é a que ela arrastou no painel, e a primeira é a capa. Anexo apagado
 * na biblioteca de mídia sai daqui sem quebrar a ficha — foto que não existe
 * mais é `<img>` quebrada na página de um produto, que é o pior lugar possível.
 */
function cdm_loja_galeria( $id ) {
	$bruto = get_post_meta( (int) $id, '_cdm_galeria', true );
	$ids   = array();
	if ( is_array( $bruto ) ) {
		$ids = $bruto;
	} elseif ( is_string( $bruto ) && '' !== $bruto ) {
		$ids = explode( ',', $bruto );
	}
	$limpos = array();
	foreach ( $ids as $i ) {
		$i = (int) $i;
		if ( $i <= 0 || in_array( $i, $limpos, true ) ) {
			continue;
		}
		if ( function_exists( 'wp_attachment_is_image' ) && ! wp_attachment_is_image( $i ) ) {
			continue;
		}
		$limpos[] = $i;
	}
	return $limpos;
}
}

if ( ! function_exists( 'cdm_loja_peca_publicavel' ) ) {
/**
 * A ÚNICA régua da ilha sobre "esta peça pode ir ao ar".
 *
 * Devolve array de motivos; vazio significa publicável. Devolver o motivo em vez
 * de true/false não é enfeite: é o texto que o painel mostra a ela, e é ele que
 * faz a diferença entre "o botão não funciona" e "falta a foto".
 *
 * Quem chama: o painel (para habilitar Publicar) e o próprio `wp_insert_post`
 * pela trava de `transition_post_status` mais abaixo. Régua em UM lugar, seção 8.
 */
function cdm_loja_peca_publicavel( $id ) {
	$motivos = array();
	$id      = (int) $id;

	$titulo = get_post( $id );
	if ( ! $titulo || '' === trim( (string) $titulo->post_title ) ) {
		$motivos[] = 'Falta o nome da peça.';
	}
	if ( ! cdm_loja_galeria( $id ) ) {
		$motivos[] = 'Falta pelo menos uma foto.';
	}
	$preco = cdm_loja_meta( $id, '_cdm_preco' );
	if ( '' === $preco || (float) $preco <= 0 ) {
		$motivos[] = 'Falta o preço.';
	}
	$disp = cdm_loja_meta( $id, '_cdm_disponibilidade' );
	if ( 'sob_encomenda' === $disp ) {
		$prazo = cdm_loja_meta( $id, '_cdm_prazo_dias' );
		if ( '' === $prazo || (int) $prazo <= 0 ) {
			$motivos[] = 'Peça sob encomenda precisa do prazo em dias.';
		}
	}
	if ( ! cdm_loja_termo_da_peca( $id, 'colecao' ) ) {
		$motivos[] = 'Escolha uma coleção.';
	}
	if ( ! cdm_loja_termo_da_peca( $id, 'tecnica' ) ) {
		$motivos[] = 'Escolha a técnica.';
	}

	return $motivos;
}
}

if ( ! function_exists( 'cdm_loja_termo_da_peca' ) ) {
/** O primeiro termo da peça naquela taxonomia, ou null. */
function cdm_loja_termo_da_peca( $id, $taxonomia ) {
	if ( ! function_exists( 'wp_get_object_terms' ) ) {
		return null;
	}
	$termos = wp_get_object_terms( (int) $id, $taxonomia );
	if ( is_wp_error( $termos ) || ! $termos ) {
		return null;
	}
	return $termos[0];
}
}

/* A TRAVA NO NÚCLEO, e não só no botão. O painel não habilita Publicar sem foto
   e sem preço, mas a regra de qualidade do despacho de 10/09 diz "peça sem foto
   ou sem preço NÃO PUBLICA" — e botão desabilitado é regra de tela, que some no
   dia em que alguém publicar por outro caminho (REST, importação, um plugin).
   Aqui ela é regra do site: a peça volta para rascunho e o motivo fica gravado
   para o painel mostrar. */
add_action( 'transition_post_status', function ( $novo, $antigo, $post ) {
	if ( ! is_object( $post ) || 'peca' !== $post->post_type || 'publish' !== $novo ) {
		return;
	}
	$motivos = cdm_loja_peca_publicavel( $post->ID );
	if ( ! $motivos ) {
		delete_post_meta( $post->ID, '_cdm_recusa' );
		return;
	}
	update_post_meta( $post->ID, '_cdm_recusa', $motivos );
	/* `wp_update_post` dentro de `transition_post_status` reentra; a guarda
	   estática evita o laço e é a mesma forma que o núcleo usa. */
	static $dentro = false;
	if ( $dentro ) {
		return;
	}
	$dentro = true;
	wp_update_post( array( 'ID' => $post->ID, 'post_status' => 'draft' ) );
	$dentro = false;
}, 10, 3 );

/* ---------------------------------------------------------------------------
 * 3. A MALHA DA PEÇA — a árvore, e o que a ficha aponta
 *
 * "Cada cadastro de produto já tem que estar pensado na arquitetura completa"
 * (Raphael, 10/09). A artesã preenche o formulário; a árvore, a trilha, o
 * JSON-LD e os links de saída o site faz sozinho no ato de publicar.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_e_peca' ) ) {
/** A peça que está sendo servida agora, ou null. */
function cdm_loja_e_peca() {
	if ( ! function_exists( 'is_singular' ) || ! is_singular( 'peca' ) ) {
		return null;
	}
	$post = function_exists( 'get_post' ) ? get_post() : null;
	return ( $post && 'peca' === $post->post_type ) ? $post : null;
}
}

/* A PEÇA ENTRA NO MAPA DA CASCA, e a trilha vem de graça (decisão 3). Só quando
   ela está sendo servida: o mapa é por requisição, e declarar todas as peças de
   uma vez faria a lista de irmãs de /loja/ encher de peça, que é outra decisão e
   não é a de hoje. */
add_filter( 'cdm_arvore', function ( $mapa ) {
	$peca = cdm_loja_e_peca();
	if ( ! $peca || ! is_array( $mapa ) ) {
		return $mapa;
	}
	$slug = (string) $peca->post_name;
	if ( '' === $slug || isset( $mapa[ $slug ] ) ) {
		return $mapa;
	}
	$mapa[ $slug ] = array(
		'nivel'  => 2,
		'mae'    => CDM_LOJA_BASE,
		'rotulo' => $peca->post_title,
	);

	return $mapa;
} );

if ( ! function_exists( 'cdm_loja_guia_da_base' ) ) {
/**
 * O mapa fixo base → o que o Guia tem a dizer sobre ela.
 *
 * É o item (3) dos links de saída do despacho de 10/09, na versão que cabe hoje:
 * as fichas de categoria (/materiais/colas/, /materiais/rejuntes/) ainda não
 * existem — esperam as três filhas da 16.5 —, então o destino é a FERRAMENTA que
 * responde a pergunta daquela base, que existe e está no ar. Link para página que
 * não existe é link morto, e link morto na ficha de um produto é pior que
 * nenhum link.
 */
function cdm_loja_guia_da_base() {
	return array(
		'ceramica' => array(
			'frase' => 'Vaso de cerâmica ou barro pede cola diferente dentro de casa e na varanda.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
		'vidro'    => array(
			'frase' => 'Em vidro, o adesivo transparente é o que não aparece por trás da pastilha.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
		'mdf'      => array(
			'frase' => 'Em MDF a conversa é cola e acabamento, para a madeira não beber a umidade do rejunte.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
		'cimento'  => array(
			'frase' => 'Peça de cimento aceita argamassa, e é a base que mais muda com o lugar onde ela vai ficar.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
		'metal'    => array(
			'frase' => 'Em metal o que decide é a flexão da chapa, e nem toda cola aguenta.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
		'outra'    => array(
			'frase' => 'Para saber qual cola a sua base pede, a ferramenta pergunta a superfície e o lugar.',
			'slug'  => 'materiais/qual-cola-usar-no-mosaico',
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. A FICHA — o HTML da página da peça
 *
 * Sem uma linha de `<script>` e sem `<style>` no retorno (seção 8): a folha sai
 * no `wp_footer`. O carrossel é `scroll-snap` puro, então ele funciona com o
 * JavaScript desligado, que é o portão 22.8.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_preco_html' ) ) {
/** O preço como a tela mostra: R$ 180,00. Vazio devolve ''. */
function cdm_loja_preco_html( $valor ) {
	if ( '' === $valor || (float) $valor <= 0 ) {
		return '';
	}
	return 'R$&nbsp;' . number_format_i18n( (float) $valor, 2 );
}
}

if ( ! function_exists( 'cdm_loja_disponibilidade_frase' ) ) {
/**
 * A disponibilidade em português de gente, com o prazo dentro quando há prazo.
 *
 * Nunca "últimas unidades", nunca contagem regressiva (seção 6 e VOZ.md): se
 * está no ar, existe; se foi vendida, sai do ar.
 */
function cdm_loja_disponibilidade_frase( $disp, $prazo ) {
	if ( 'sob_encomenda' === $disp ) {
		$dias = (int) $prazo;
		return $dias > 0
			? 'Sob encomenda, feita em ' . $dias . ( 1 === $dias ? ' dia' : ' dias' )
			: 'Sob encomenda';
	}
	if ( 'pronta_entrega' === $disp ) {
		return 'Pronta entrega, já está feita';
	}
	return '';
}
}

if ( ! function_exists( 'cdm_loja_whatsapp' ) ) {
/** O número da artesã, só dígitos, ou '' quando ainda não foi publicado. */
function cdm_loja_whatsapp() {
	$bruto = (string) get_option( 'cdm_whatsapp', '' );
	$so    = preg_replace( '/\D+/', '', $bruto );
	/* DDI + DDD + 8 ou 9 dígitos. Número curto é número errado, e link de
	   WhatsApp errado na página de um produto manda a cliente para o vazio. */
	if ( strlen( $so ) < 12 || strlen( $so ) > 13 ) {
		return '';
	}
	return $so;
}
}

if ( ! function_exists( 'cdm_loja_mensagem_whatsapp' ) ) {
/**
 * A mensagem pronta, no tom do VOZ.md, citando a peça de verdade.
 *
 * Sem emoji, sem "Olá, tudo bem?" — quem clica já sabe o que quer. A quebra de
 * linha é %0A depois do `rawurlencode`, como o playbook manda.
 *
 * NÃO HÁ `str_replace( '%0D%0A', '%0A', ... )` AQUI, e a ausência é o conserto de
 * uma linha que existiu e não fazia nada. Ela foi escrita por precaução contra o
 * retorno de carro do Windows, e a bateria de mutações mostrou que era código
 * morto: a mutação que a apagava não fez um único portão reprovar, porque a string
 * é construída aqui mesmo com `"\n"` literal e `rawurlencode()` de `"\n"` já
 * devolve `%0A`. Linha defensiva contra um caso que não pode acontecer é a
 * "função morta" que a Robometria nomeou em 11/09/2026 — parece cuidado e é ruído
 * que a próxima pessoa vai ter de entender.
 */
function cdm_loja_mensagem_whatsapp( $titulo, $url, $disp, $prazo ) {
	$frase = cdm_loja_disponibilidade_frase( $disp, $prazo );
	$texto = 'Oi! Vi a peça ' . $titulo . ' no site do Clube do Mosaico';
	if ( '' !== $frase ) {
		$texto .= ' (' . lcfirst( $frase ) . ')';
	}
	$texto .= ' e queria saber se ela está disponível.' . "\n" . $url;

	return rawurlencode( $texto );
}
}

if ( ! function_exists( 'cdm_loja_foto_html' ) ) {
/**
 * Uma foto da galeria, com `alt` gerado dos campos (item SEO do despacho).
 *
 * `width`/`height` no HTML é requisito do DESIGN.md e do orçamento de desempenho
 * da 22.4: sem eles a página salta quando a foto carrega, e salto na foto de um
 * produto é a primeira coisa que faz alguém achar o site amador.
 */
function cdm_loja_foto_html( $anexo_id, $titulo, $base_rotulo, $n, $capa ) {
	$src = wp_get_attachment_image_src( (int) $anexo_id, $capa ? 'large' : 'medium_large' );
	if ( ! $src || empty( $src[0] ) ) {
		return '';
	}
	$alt = $titulo . ', mosaico em ' . $base_rotulo . ', foto ' . (int) $n;

	$html  = '<figure class="cdm-foto' . ( $capa ? ' cdm-foto-capa' : '' ) . '" id="cdm-foto-' . (int) $n . '">';
	$html .= '<img src="' . esc_url( $src[0] ) . '"';
	if ( ! empty( $src[1] ) && ! empty( $src[2] ) ) {
		$html .= ' width="' . (int) $src[1] . '" height="' . (int) $src[2] . '"';
	}
	$html .= ' alt="' . esc_attr( $alt ) . '"';
	$html .= $capa ? ' fetchpriority="high" decoding="async"' : ' loading="lazy" decoding="async"';
	$html .= '>';
	$html .= '</figure>';

	return $html;
}
}

if ( ! function_exists( 'cdm_loja_ficha_html' ) ) {
/**
 * A ficha inteira da peça. Recebe o post; não usa nada global além das options.
 *
 * A ORDEM É A DA SEÇÃO 5 DO CONTRATO — resposta antes da explicação. Quem abre a
 * página de uma peça veio ver a peça: foto, nome, preço, disponibilidade e o
 * botão. A ficha técnica, a descrição e o "prefere fazer a sua?" vêm depois.
 */
function cdm_loja_ficha_html( $peca ) {
	$id     = (int) $peca->ID;
	$titulo = (string) $peca->post_title;
	$url    = get_permalink( $peca );

	$campos = cdm_loja_campos();
	$bases  = isset( $campos['_cdm_base']['opcoes'] ) ? $campos['_cdm_base']['opcoes'] : array();

	$preco = cdm_loja_meta( $id, '_cdm_preco' );
	$disp  = cdm_loja_meta( $id, '_cdm_disponibilidade' );
	$prazo = cdm_loja_meta( $id, '_cdm_prazo_dias' );
	$base  = cdm_loja_meta( $id, '_cdm_base' );
	$base_rotulo = isset( $bases[ $base ] ) ? $bases[ $base ] : 'mosaico';

	$colecao = cdm_loja_termo_da_peca( $id, 'colecao' );
	$tecnica = cdm_loja_termo_da_peca( $id, 'tecnica' );
	$galeria = cdm_loja_galeria( $id );

	$html = '<div class="cdm-peca">';

	/* 1. AS FOTOS. Carrossel com scroll-snap: todas as fotos estão no HTML
	   servido (22.3), sem autoplay, e a navegação é o dedo ou a tecla. */
	if ( $galeria ) {
		$html .= '<div class="cdm-peca-fotos">';
		$html .= '<div class="cdm-carrossel" role="group" aria-label="Fotos da peça ' . esc_attr( $titulo ) . '">';
		$n = 0;
		foreach ( $galeria as $anexo ) {
			$n++;
			$html .= cdm_loja_foto_html( $anexo, $titulo, $base_rotulo, $n, 1 === $n );
		}
		$html .= '</div>';
		if ( count( $galeria ) > 1 ) {
			$html .= '<p class="cdm-carrossel-conta">' . count( $galeria ) . ' fotos desta peça. Arraste para o lado.</p>';
		}
		$html .= '</div>';
	}

	/* 2. A RESPOSTA: preço, disponibilidade, botão. */
	$html .= '<div class="cdm-peca-topo">';
	$preco_html = cdm_loja_preco_html( $preco );
	if ( '' !== $preco_html ) {
		$html .= '<p class="cdm-peca-preco"><span class="cdm-preco">' . $preco_html . '</span></p>';
	}
	$frase_disp = cdm_loja_disponibilidade_frase( $disp, $prazo );
	if ( '' !== $frase_disp ) {
		$html .= '<p class="cdm-peca-disp">' . esc_html( $frase_disp ) . '</p>';
	}

	$zap = cdm_loja_whatsapp();
	if ( '' !== $zap ) {
		$link  = 'https://wa.me/' . $zap . '?text=' . cdm_loja_mensagem_whatsapp( $titulo, $url, $disp, $prazo );
		$html .= '<p class="cdm-peca-acao"><a class="cdm-botao" href="' . esc_url( $link ) . '" rel="noopener">Falar com a artesã sobre esta peça</a></p>';
		$html .= '<p class="cdm-peca-nota">Você fala direto com quem fez. Ela confirma se a peça está disponível e como fica o envio.</p>';
	} else {
		$html .= '<div class="cdm-vazio cdm-peca-sem-contato">';
		$html .= '<h3>O contato ainda não foi publicado</h3>';
		$html .= '<p>Esta peça existe e está aqui, mas o canal de conversa do ateliê ainda não foi ligado — e a gente não inventa um número de telefone para o botão parecer pronto. Volte em algumas horas.</p>';
		$html .= '</div>';
	}
	$html .= '</div>';

	/* 3. A DESCRIÇÃO, com as palavras dela. */
	$descricao = trim( (string) $peca->post_content );
	if ( '' !== $descricao ) {
		$html .= '<div class="cdm-peca-texto">' . wpautop( wp_kses_post( $descricao ) ) . '</div>';
	}

	/* 4. A FICHA TÉCNICA, em tabela — o lugar do número (VOZ.md, seção 15). */
	$linhas = array();
	foreach ( array( '_cdm_medidas', '_cdm_peso_g', '_cdm_cores' ) as $chave ) {
		$v = cdm_loja_meta( $id, $chave );
		if ( '' === $v ) {
			continue;
		}
		$unidade = isset( $campos[ $chave ]['unidade'] ) ? $campos[ $chave ]['unidade'] : '';
		$linhas[ $campos[ $chave ]['rotulo'] ] = '' !== $unidade ? $v . ' ' . $unidade : $v;
	}
	if ( '' !== $base && isset( $bases[ $base ] ) ) {
		$linhas['Base'] = $bases[ $base ];
	}
	if ( $tecnica ) {
		$linhas['Técnica'] = $tecnica->name;
	}
	if ( $colecao ) {
		$linhas['Coleção'] = $colecao->name;
	}
	if ( $linhas ) {
		$html .= '<div class="cdm-secao"><h2>A peça em números</h2>';
		$html .= '<div class="cdm-tabela"><table class="cdm-quadro"><tbody>';
		foreach ( $linhas as $rotulo => $valor ) {
			$html .= '<tr><th scope="row">' . esc_html( $rotulo ) . '</th>';
			$html .= '<td class="cdm-medida">' . esc_html( $valor ) . '</td></tr>';
		}
		$html .= '</tbody></table></div></div>';
	}

	/* 5. QUEM FEZ — a assinatura da peça (DESIGN.md, "A artesã"). Sem nome e sem
	   foto enquanto o Raphael não entregar `identidade/artesa/`: o bloco fica de
	   pé e vazio, como o PROMPT.md desta ilha manda, e não inventa uma pessoa. */
	$html .= '<div class="cdm-secao cdm-peca-quem"><h2>Quem fez</h2>';
	$html .= '<p>Esta peça foi montada à mão, pastilha por pastilha, no ateliê de uma artesã — ';
	$html .= 'não é produção em série e não é revenda. A foto é desta peça, não de catálogo.</p>';
	$html .= '</div>';

	/* 6. OS LINKS DE SAÍDA (item 3 da malha automática, na versão de hoje). */
	$guias = cdm_loja_guia_da_base();
	$html .= '<div class="cdm-secao"><h2>Prefere fazer a sua?</h2>';
	if ( isset( $guias[ $base ] ) ) {
		$html .= '<p>' . esc_html( $guias[ $base ]['frase'] ) . ' ';
		$html .= cdm_casca_link_html( $guias[ $base ]['slug'], 'A ferramenta diz qual cola usar' ) . '.</p>';
	}
	$html .= '<p>' . cdm_casca_link_html( 'materiais/quantas-pastilhas-para-mosaico', 'Quantas pastilhas e quanto rejunte' );
	$html .= ' é a conta da peça, e ' . cdm_casca_link_html( CDM_LOJA_BASE, 'a Loja' ) . ' tem as outras peças do ateliê.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
}
}

/* A FICHA ENTRA PELO `the_content`, prioridade 5: antes do cinto de segurança da
   trilha (9) e do "Veja também" (20) da casca, para os dois continuarem
   funcionando exatamente como nas páginas. */
add_filter( 'the_content', function ( $html ) {
	$peca = cdm_loja_e_peca();
	if ( ! $peca ) {
		return $html;
	}
	/* `post_content` é a descrição dela, e a ficha já a imprime no lugar certo —
	   devolver as duas coisas serviria a descrição duas vezes. */
	return cdm_loja_ficha_html( $peca );
}, 5 );

/* ---------------------------------------------------------------------------
 * 5. O QUE VAI NO `<head>` DA PEÇA — descrição, og: e Product+Offer
 *
 * A casca serve Organization, WebSite, favicon, GA4 e o BreadcrumbList; ela NÃO
 * serve descrição nem og:, e é por isso que isto está aqui. A cicatriz é da
 * Aquametria em 12/09/2026: cinco URLs novas foram ao ar servindo ZERO meta
 * description e ZERO og:, e o portão ficou verde porque contava as antigas.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_descricao' ) ) {
/**
 * A meta description da peça, gerada dos campos (item SEO do despacho de 10/09).
 *
 * Ordem: o que é + base + técnica + medidas + disponibilidade. Nunca a descrição
 * dela cortada no meio: frase truncada com "..." é o que toda loja pequena
 * serve, e é ruim de ler na SERP. Teto de 160 caracteres, cortado na palavra.
 */
function cdm_loja_descricao( $peca ) {
	$id     = (int) $peca->ID;
	$campos = cdm_loja_campos();
	$bases  = isset( $campos['_cdm_base']['opcoes'] ) ? $campos['_cdm_base']['opcoes'] : array();

	$base    = cdm_loja_meta( $id, '_cdm_base' );
	$tecnica = cdm_loja_termo_da_peca( $id, 'tecnica' );
	$medidas = cdm_loja_meta( $id, '_cdm_medidas' );
	$disp    = cdm_loja_disponibilidade_frase(
		cdm_loja_meta( $id, '_cdm_disponibilidade' ),
		cdm_loja_meta( $id, '_cdm_prazo_dias' )
	);

	/* UMA FRASE, com os atributos separados por vírgula, e a disponibilidade como
	   segunda frase. A primeira escrita juntava tudo com ponto e a description saía
	   "…feita à mão. base de cerâmica ou barro. técnica direto." — minúscula depois
	   de ponto em cinco lugares, na única linha da peça que aparece na SERP. Foi
	   visto renderizando a primeira ficha na bancada, não em revisão de código. */
	$atributos = array();
	if ( isset( $bases[ $base ] ) ) {
		$atributos[] = 'base de ' . mb_strtolower( $bases[ $base ], 'UTF-8' );
	}
	if ( $tecnica ) {
		$atributos[] = 'técnica ' . mb_strtolower( $tecnica->name, 'UTF-8' );
	}
	if ( '' !== $medidas ) {
		$atributos[] = $medidas . ' cm';
	}

	$texto = (string) $peca->post_title . ', peça de mosaico feita à mão';
	if ( $atributos ) {
		$texto .= ': ' . implode( ', ', $atributos );
	}
	$texto .= '.';
	if ( '' !== $disp ) {
		$texto .= ' ' . $disp . '.';
	}
	if ( mb_strlen( $texto, 'UTF-8' ) <= 160 ) {
		return $texto;
	}
	$curto = mb_substr( $texto, 0, 157, 'UTF-8' );
	$corte = mb_strrpos( $curto, ' ', 0, 'UTF-8' );

	return ( false !== $corte ? mb_substr( $curto, 0, $corte, 'UTF-8' ) : $curto ) . '…';
}
}

if ( ! function_exists( 'cdm_loja_titulo_seo' ) ) {
/**
 * O `<title>` da peça: "<nome> — <coleção> em mosaico | Clube do Mosaico".
 *
 * É o formato que o despacho de 10/09 escreveu. Sem coleção o meio cai fora em
 * vez de sair um travessão solto.
 */
function cdm_loja_titulo_seo( $peca ) {
	$colecao = cdm_loja_termo_da_peca( (int) $peca->ID, 'colecao' );
	$meio    = $colecao ? ' — ' . $colecao->name . ' em mosaico' : ' — mosaico feito à mão';

	return (string) $peca->post_title . $meio . ' | Clube do Mosaico';
}
}

add_filter( 'document_title_parts', function ( $partes ) {
	$peca = cdm_loja_e_peca();
	if ( ! $peca || ! is_array( $partes ) ) {
		return $partes;
	}
	$partes['title'] = cdm_loja_titulo_seo( $peca );
	unset( $partes['tagline'], $partes['site'] );

	return $partes;
} );

add_action( 'wp_head', function () {
	$peca = cdm_loja_e_peca();
	if ( ! $peca ) {
		return;
	}
	$id  = (int) $peca->ID;
	$url = get_permalink( $peca );

	echo '<meta name="description" content="' . esc_attr( cdm_loja_descricao( $peca ) ) . '">' . "\n";

	echo '<meta property="og:type" content="product">' . "\n";
	echo '<meta property="og:title" content="' . esc_attr( $peca->post_title ) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr( cdm_loja_descricao( $peca ) ) . '">' . "\n";
	echo '<meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
	echo '<meta property="og:site_name" content="Clube do Mosaico">' . "\n";
	echo '<meta property="og:locale" content="pt_BR">' . "\n";

	$galeria = cdm_loja_galeria( $id );
	if ( $galeria ) {
		$capa = wp_get_attachment_image_src( (int) $galeria[0], 'large' );
		if ( $capa && ! empty( $capa[0] ) ) {
			echo '<meta property="og:image" content="' . esc_url( $capa[0] ) . '">' . "\n";
			echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
		}
	}
}, 4 );

add_action( 'wp_head', function () {
	$peca = cdm_loja_e_peca();
	if ( ! $peca ) {
		return;
	}
	$id  = (int) $peca->ID;
	$url = get_permalink( $peca );

	$preco = cdm_loja_meta( $id, '_cdm_preco' );
	$disp  = cdm_loja_meta( $id, '_cdm_disponibilidade' );

	$imagens = array();
	foreach ( cdm_loja_galeria( $id ) as $anexo ) {
		$src = wp_get_attachment_image_src( (int) $anexo, 'large' );
		if ( $src && ! empty( $src[0] ) ) {
			$imagens[] = $src[0];
		}
	}

	$produto = array(
		'@type'       => 'Product',
		'@id'         => $url . '#peca',
		'name'        => (string) $peca->post_title,
		'url'         => $url,
		'description' => cdm_loja_descricao( $peca ),
		'brand'       => array( '@type' => 'Brand', 'name' => 'Clube do Mosaico' ),
		'inLanguage'  => 'pt-BR',
	);
	if ( $imagens ) {
		$produto['image'] = $imagens;
	}

	$tecnica = cdm_loja_termo_da_peca( $id, 'tecnica' );
	$base    = cdm_loja_meta( $id, '_cdm_base' );
	$campos  = cdm_loja_campos();
	$bases   = isset( $campos['_cdm_base']['opcoes'] ) ? $campos['_cdm_base']['opcoes'] : array();
	$props   = array();
	if ( $tecnica ) {
		$props[] = array( '@type' => 'PropertyValue', 'name' => 'Técnica', 'value' => $tecnica->name );
	}
	if ( isset( $bases[ $base ] ) ) {
		$props[] = array( '@type' => 'PropertyValue', 'name' => 'Base', 'value' => $bases[ $base ] );
	}
	$medidas = cdm_loja_meta( $id, '_cdm_medidas' );
	if ( '' !== $medidas ) {
		$props[] = array( '@type' => 'PropertyValue', 'name' => 'Medidas', 'value' => $medidas . ' cm' );
	}
	if ( $props ) {
		$produto['additionalProperty'] = $props;
	}
	$peso = cdm_loja_meta( $id, '_cdm_peso_g' );
	if ( '' !== $peso && (int) $peso > 0 ) {
		$produto['weight'] = array( '@type' => 'QuantitativeValue', 'value' => (int) $peso, 'unitCode' => 'GRM' );
	}

	/* A OFERTA SÓ SAI COM PREÇO DE VERDADE. `Offer` sem `price` é dado
	   estruturado inválido, e inválido é ignorado — publicaria MENOS com cara de
	   publicar mais, que é a decisão 3 da seção 3d da casca aplicada aqui. */
	if ( '' !== $preco && (float) $preco > 0 ) {
		$produto['offers'] = array(
			'@type'         => 'Offer',
			'url'           => $url,
			'price'         => number_format( (float) $preco, 2, '.', '' ),
			'priceCurrency' => 'BRL',
			'availability'  => 'sob_encomenda' === $disp
				? 'https://schema.org/PreOrder'
				: 'https://schema.org/InStock',
			'itemCondition' => 'https://schema.org/NewCondition',
			'seller'        => array( '@id' => home_url( '/#organizacao' ) ),
		);
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array( $produto ),
	);

	echo '<script type="application/ld+json" id="cdm-peca-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 9 );

/* ---------------------------------------------------------------------------
 * 6. A VITRINE DA PÁGINA /loja/ — cartões com foto
 *
 * A casca já tem `cdm_casca_vitrine_de_pecas_html()`, e ela está certa para o que
 * foi escrita: nome e preço, sem foto, porque foto de peça não existia. Agora
 * existe, e o DESIGN.md diz que a foto manda (proporção 4:5, `width`/`height` no
 * HTML). Este filtro troca a vitrine pela versão com foto SEM tocar na casca —
 * casca editada por bloco de loja é casca que sai do ar por defeito de loja.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_cartao_html' ) ) {
function cdm_loja_cartao_html( $peca ) {
	$id     = (int) $peca->ID;
	$titulo = (string) $peca->post_title;
	$campos = cdm_loja_campos();
	$bases  = isset( $campos['_cdm_base']['opcoes'] ) ? $campos['_cdm_base']['opcoes'] : array();
	$base   = cdm_loja_meta( $id, '_cdm_base' );
	$base_rotulo = isset( $bases[ $base ] ) ? $bases[ $base ] : 'mosaico';

	$galeria = cdm_loja_galeria( $id );
	$html    = '<li class="cdm-card cdm-card-peca">';

	if ( $galeria ) {
		$src = wp_get_attachment_image_src( (int) $galeria[0], 'medium_large' );
		if ( $src && ! empty( $src[0] ) ) {
			$html .= '<a class="cdm-card-foto" href="' . esc_url( get_permalink( $peca ) ) . '">';
			$html .= '<img src="' . esc_url( $src[0] ) . '"';
			if ( ! empty( $src[1] ) && ! empty( $src[2] ) ) {
				$html .= ' width="' . (int) $src[1] . '" height="' . (int) $src[2] . '"';
			}
			$html .= ' alt="' . esc_attr( $titulo . ', mosaico em ' . $base_rotulo . ', foto 1' ) . '"';
			$html .= ' loading="lazy" decoding="async"></a>';
		}
	}

	$html .= '<h3><a href="' . esc_url( get_permalink( $peca ) ) . '">' . esc_html( $titulo ) . '</a></h3>';

	$preco = cdm_loja_preco_html( cdm_loja_meta( $id, '_cdm_preco' ) );
	if ( '' !== $preco ) {
		$html .= '<p class="cdm-card-preco"><span class="cdm-preco">' . $preco . '</span></p>';
	}

	$medidas = cdm_loja_meta( $id, '_cdm_medidas' );
	$frase   = cdm_loja_disponibilidade_frase(
		cdm_loja_meta( $id, '_cdm_disponibilidade' ),
		cdm_loja_meta( $id, '_cdm_prazo_dias' )
	);
	$linha = array();
	if ( '' !== $medidas ) {
		$linha[] = $medidas . ' cm';
	}
	if ( '' !== $frase ) {
		$linha[] = $frase;
	}
	if ( $linha ) {
		$html .= '<p>' . esc_html( implode( ' · ', $linha ) ) . '</p>';
	}

	$html .= '</li>';

	return $html;
}
}

if ( ! function_exists( 'cdm_loja_vitrine_html' ) ) {
function cdm_loja_vitrine_html( $quantas = 24 ) {
	if ( ! function_exists( 'get_posts' ) ) {
		return '';
	}
	$pecas = get_posts( array(
		'post_type'   => 'peca',
		'post_status' => 'publish',
		'numberposts' => (int) $quantas,
		'orderby'     => 'date',
		'order'       => 'DESC',
	) );
	if ( ! $pecas ) {
		return '';
	}
	$html = '<ul class="cdm-cards cdm-cards-peca">';
	foreach ( $pecas as $p ) {
		$html .= cdm_loja_cartao_html( $p );
	}
	$html .= '</ul>';

	return $html;
}
}

/* A casca chama a vitrine dela; este filtro devolve a nossa quando há peça. O
   estado vazio continua sendo o da casca, que já está no ar e já foi conferido:
   duas versões do estado vazio é uma para envelhecer. */
add_filter( 'cdm_vitrine_de_pecas', function ( $html, $quantas ) {
	$nossa = cdm_loja_vitrine_html( $quantas );

	return '' !== $nossa ? $nossa : $html;
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * 7. A FOLHA — no `wp_footer`, nunca no retorno do filtro (seção 8)
 *
 * O carrossel é CSS puro: `scroll-snap-type` na faixa e `scroll-snap-align` em
 * cada foto. Com o JavaScript desligado ele continua rolando com o dedo e com a
 * barra, que é o portão 22.8 — e não há uma linha de JavaScript neste snippet.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_loja_e_peca() && ! cdm_loja_pagina_com_vitrine() ) {
		return;
	}
	$css = <<<'CSS'
.cdm-peca{max-width:60rem;}
.cdm-peca-fotos{margin:0 0 1.6rem;}
/* A FAIXA DE FOTOS. Uma foto por tela no celular, duas no desktop, todas no HTML
   servido. Sem autoplay e sem JavaScript: quem decide qual foto ver e o dedo. */
.cdm-carrossel{display:flex;gap:.75rem;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding:0 0 .5rem;margin:0;}
.cdm-carrossel .cdm-foto{flex:0 0 100%;scroll-snap-align:start;margin:0;}
.cdm-carrossel img{display:block;width:100%;height:auto;border-radius:14px;background:var(--cdm-traco);}
.cdm-carrossel-conta{margin:.4rem 0 0;font-size:.85rem;color:var(--cdm-legenda);}
.cdm-peca-topo{margin:0 0 1.6rem;}
.cdm-peca-preco{margin:0 0 .3rem;}
.cdm-peca-preco .cdm-preco{font-size:2rem;line-height:1.1;}
.cdm-peca-disp{margin:0 0 1.1rem;color:var(--cdm-legenda);font-size:1rem;}
.cdm-peca-acao{margin:0 0 .6rem;}
.cdm-peca-nota{margin:0;color:var(--cdm-legenda);font-size:.92rem;max-width:34rem;}
.cdm-peca-texto{margin:0 0 1.6rem;max-width:40rem;}
.cdm-peca-texto p{margin:0 0 .8rem;}
.cdm-peca-quem p{max-width:40rem;}
.cdm-peca .cdm-quadro th{width:11rem;}
/* O CARTAO DE PECA do DESIGN.md: a foto manda, proporcao 4:5. */
.cdm-cards-peca{grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));}
.cdm-card-peca{padding:0;overflow:hidden;gap:0;}
.cdm-card-foto{display:block;line-height:0;}
.cdm-card-foto img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;background:var(--cdm-traco);}
.cdm-card-peca h3{margin:0;padding:.9rem 1rem 0;font-size:1.15rem;}
.cdm-card-peca h3 a{text-decoration:none;color:var(--cdm-tinta);}
.cdm-card-peca h3 a:hover{color:var(--cdm-rubi);}
.cdm-card-preco{padding:.35rem 1rem 0;}
.cdm-card-peca p{padding:0 1rem;}
.cdm-card-peca p:last-child{padding-bottom:1rem;}
@media (min-width:52rem){
.cdm-carrossel .cdm-foto{flex:0 0 calc(50% - .375rem);}
.cdm-peca-fotos{margin-bottom:2rem;}
}
CSS;
	echo '<style id="cdm-loja-css">' . $css . '</style>' . "\n";
}, 21 );

if ( ! function_exists( 'cdm_loja_pagina_com_vitrine' ) ) {
/** A home e a /loja/ são as duas páginas onde o cartão de peça aparece. */
function cdm_loja_pagina_com_vitrine() {
	if ( function_exists( 'is_front_page' ) && is_front_page() ) {
		return true;
	}
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_LOJA_BASE === cdm_casca_slug_atual();
}
}

/* ---------------------------------------------------------------------------
 * 8. O QUE A ILHA CONTA SOBRE SI — o número nasce contado (seção 8)
 *
 * `cdm_casca_numeros()` já conta as peças publicadas pelo CPT. O que falta é a
 * contagem das peças que a artesã tem em rascunho, porque é ela que diz se o
 * painel está sendo usado — e é o número que o relatório desta ilha precisa
 * sem ninguém abrir o site.
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_numeros', function ( $n ) {
	if ( ! is_array( $n ) || ! function_exists( 'get_posts' ) ) {
		return $n;
	}
	$rascunhos = get_posts( array(
		'post_type'   => 'peca',
		'post_status' => array( 'draft', 'pending' ),
		'numberposts' => 100,
	) );
	$n['pecas_rascunho'] = is_array( $rascunhos ) ? count( $rascunhos ) : 0;

	return $n;
} );

/* ---------------------------------------------------------------------------
 * 9. O ENDPOINT DE CÓPIA — seção 24 do ARQUIPELAGO.md
 *
 * As peças que ela cadastra são o ÚNICO dado do Arquipélago inteiro que não
 * existe fora do banco do WordPress: não há arquivo no repositório de onde
 * reconstruir. A seção 24 manda nascer com cópia, e o adendo de 11/09 diz como:
 * um endpoint de leitura protegido pelo mesmo token do Sync, devolvendo as peças
 * com metadados e as URLs das fotos, para a ronda diária commitar
 * `dados/pecas.json`.
 *
 * O token é o do Sync, lido da MESMA constante — token novo seria um segredo a
 * mais para guardar, e o Sync já é o portão desta ilha. Comparação por
 * `hash_equals`, nunca `==`.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_loja_token_esperado' ) ) {
/**
 * O token do Sync, lido de onde o Sync o guarda.
 *
 * A função do Sync é preferida porque ela CRIA o token quando ele ainda não
 * existe; a option é o caminho de quem só lê. Os dois lados olham para o mesmo
 * lugar — um segundo segredo para esta ilha seria um segredo a mais para perder,
 * e o Sync já é o portão dela.
 */
function cdm_loja_token_esperado() {
	if ( function_exists( 'clubedomosaico_sync_token' ) ) {
		$t = clubedomosaico_sync_token();
		if ( is_string( $t ) && '' !== $t ) {
			return $t;
		}
	}
	$guardado = get_option( 'clubedomosaico_sync_token', '' );

	return is_string( $guardado ) ? $guardado : '';
}
}

if ( ! function_exists( 'cdm_loja_copia' ) ) {
/**
 * O retrato das peças, para a cópia da seção 24.
 *
 * Inclui rascunho de propósito: peça que ela começou e não publicou é trabalho
 * dela, e é o que mais dói perder. Não inclui NADA de pessoa — o CPT `lead_peca`
 * não existe hoje, e no dia em que existir os leads não entram no repositório
 * (adendo 3: nome e WhatsApp de pessoa não vão para arquivo versionado).
 */
function cdm_loja_copia() {
	$pecas = get_posts( array(
		'post_type'   => 'peca',
		'post_status' => array( 'publish', 'draft', 'pending', 'private' ),
		'numberposts' => 500,
		'orderby'     => 'ID',
		'order'       => 'ASC',
	) );

	$saida = array();
	foreach ( (array) $pecas as $p ) {
		$id  = (int) $p->ID;
		$um  = array(
			'id'        => $id,
			'titulo'    => (string) $p->post_title,
			'slug'      => (string) $p->post_name,
			'estado'    => (string) $p->post_status,
			'criada_em' => (string) $p->post_date_gmt,
			'url'       => get_permalink( $p ),
			'descricao' => (string) $p->post_content,
			'campos'    => array(),
			'colecao'   => null,
			'tecnica'   => null,
			'fotos'     => array(),
		);
		foreach ( array_keys( cdm_loja_campos() ) as $chave ) {
			$um['campos'][ ltrim( $chave, '_' ) ] = cdm_loja_meta( $id, $chave );
		}
		$c = cdm_loja_termo_da_peca( $id, 'colecao' );
		$t = cdm_loja_termo_da_peca( $id, 'tecnica' );
		if ( $c ) {
			$um['colecao'] = array( 'slug' => $c->slug, 'nome' => $c->name );
		}
		if ( $t ) {
			$um['tecnica'] = array( 'slug' => $t->slug, 'nome' => $t->name );
		}
		foreach ( cdm_loja_galeria( $id ) as $anexo ) {
			$src = wp_get_attachment_image_src( (int) $anexo, 'full' );
			$um['fotos'][] = array(
				'id'  => (int) $anexo,
				'url' => ( $src && ! empty( $src[0] ) ) ? $src[0] : wp_get_attachment_url( (int) $anexo ),
			);
		}
		$saida[] = $um;
	}

	return array(
		'ilha'        => 'clubedomosaico',
		'gerado_em'   => gmdate( 'c' ),
		'versao_loja' => CDM_LOJA_VERSAO,
		'total'       => count( $saida ),
		'pecas'       => $saida,
	);
}
}

add_action( 'rest_api_init', function () {
	if ( ! function_exists( 'register_rest_route' ) ) {
		return;
	}
	register_rest_route( 'clubedomosaico/v1', '/pecas', array(
		'methods'             => 'GET',
		'callback'            => function ( $pedido ) {
			return cdm_loja_copia();
		},
		'permission_callback' => function ( $pedido ) {
			$esperado = cdm_loja_token_esperado();
			if ( '' === $esperado ) {
				return false;
			}
			$vindo = (string) $pedido->get_param( 'token' );

			return '' !== $vindo && hash_equals( $esperado, $vindo );
		},
	) );
} );

/* ---------------------------------------------------------------------------
 * 10. O ESTADO DA LOJA EM NÚMERO — endpoint PÚBLICO, e por que não é o /status
 *
 * A vontade era acrescentar a contagem ao `/wp-json/clubedomosaico/v1/status`
 * que a Fundação já lê a cada desembarque. Não dá, e a razão é a mesma que faz
 * esta ilha ter um snippet atualizador: o `/status` mora no snippet do Sync, o
 * Sync SE PULA A SI MESMO por desenho (está escrito no PROMPT.md desta ilha), e
 * ele não aplica filtro nenhum naquela resposta. Um `add_filter( 'clubedomosaico
 * _status', ... )` aqui seria exatamente o "portão que nunca rodou é função
 * morta" que a Robometria nomeou em 11/09/2026 — uma linha bonita, verde para
 * sempre, medindo nada.
 *
 * Então a contagem sai por rota própria, sem token, porque não há segredo em
 * dizer quantas peças a loja tem: é o que qualquer visitante conta abrindo
 * /loja/. O que é dado da artesã (as peças em si, com metadados e fotos) continua
 * atrás do token, na rota de cópia acima.
 * ------------------------------------------------------------------------- */

add_action( 'rest_api_init', function () {
	if ( ! function_exists( 'register_rest_route' ) ) {
		return;
	}
	register_rest_route( 'clubedomosaico/v1', '/loja', array(
		'methods'             => 'GET',
		'permission_callback' => '__return_true',
		'callback'            => function () {
			$pub = get_posts( array( 'post_type' => 'peca', 'post_status' => 'publish', 'numberposts' => 200 ) );
			$ras = get_posts( array( 'post_type' => 'peca', 'post_status' => array( 'draft', 'pending' ), 'numberposts' => 200 ) );

			return array(
				'versao_loja' => CDM_LOJA_VERSAO,
				'publicadas'  => is_array( $pub ) ? count( $pub ) : 0,
				'rascunhos'   => is_array( $ras ) ? count( $ras ) : 0,
				'termos'      => array(
					'colecao' => count( cdm_loja_termos_iniciais()['colecao'] ),
					'tecnica' => count( cdm_loja_termos_iniciais()['tecnica'] ),
				),
			);
		},
	) );
} );

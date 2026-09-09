/**
 * Aquametria Casca — identidade e estrutura do site
 * Versão: 1.3.0 (09/09/2026) — casca no celular e ícone próprio. Duas coisas que
 * a Sentinela Técnica pega abrindo o site no telefone: (a) o menu passa a ser um
 * botão sanfona abaixo de 782 px, com aria-expanded/aria-controls, Escape e clique
 * fora fechando — e os três links continuam no HTML servido, dentro de <nav>, para
 * quem lê sem JavaScript (crawler de IA inclusive); sem JavaScript o menu não some,
 * volta a ser a lista de sempre; (b) o ícone do site deixa de ser o do WordPress e
 * passa a ser o recipiente graduado da marca, em SVG na aba e em PNG no iOS, os dois
 * como data URI dentro do snippet — nada sobe para a biblioteca de mídia.
 * Versão: 1.2.0 (08/09/2026) — apelidos de endereço. Endereço adivinhado a partir do nome da
 * calculadora deixa de dar 404: /calculadora-de-aquecedor-de-aquario/ (o que o Raphael pediu),
 * /calculadora-de-aquecedor/, /calculadora-de-litros/ e mais dezoito irmãos redirecionam 301
 * para a página canônica — e só quando ela existe publicada, para nunca trocar um 404 por outro.
 * Versão: 1.1.0 (08/09/2026) — link do hub nunca mais aponta para página que não existe.
 * O endereço de cada calculadora passa a ser resolvido pelo id do repositório (_aquametria_id),
 * não por slug adivinhado, e o card só vira link se a página estiver publicada de verdade;
 * sem página, fica o selo "Em construção". Corrige o defeito 2 de 08/09/2026: o hub publicava
 * /calculadora-de-aquecedor/ para a C5, cuja página é /calculadora-de-potencia-do-aquecedor/,
 * e o clique dava 404. A 1.0.4 tinha ajustado o resumo da C12 no hub.
 *
 * Dá cara de Aquametria ao tema ativo, sozinho, sem construtor de página e sem
 * plugin de tema. Faz seis coisas:
 *   (a) carrega Chivo, IBM Plex Sans e IBM Plex Mono e injeta a paleta no wp_head;
 *   (b) troca a saída de core/site-title e core/site-logo pelo logotipo em SVG
 *       (recipiente graduado com linha de enchimento) mais o wordmark;
 *   (c) troca a saída de core/navigation pelo menu Calculadoras · Metodologia · Sobre;
 *   (d) cria, casando pelo slug, as páginas inicio, calculadoras, metodologia e sobre,
 *       e fixa inicio como página inicial;
 *   (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (nunca apaga);
 *   (f) substitui a template part 'footer' do tema pelo rodapé da Aquametria
 *       (tagline e nota de fontes), para não ficarem dois rodapés empilhados;
 *   (g) redireciona 301 os apelidos de endereço (seção 1b) para a página canônica;
 *   (h) publica o ícone do site (seção 2b), no lugar do que o WordPress imprimiria.
 *
 * O conteúdo das quatro páginas mora em shortcodes deste snippet: atualizar o
 * snippet atualiza as páginas, sem tocar no editor do WordPress.
 *
 * A lista de calculadoras do hub está em aquametria_casca_calculadoras() e passa
 * pelo filtro 'aquametria_calculadoras' — cada calculadora nova vira 'publicada'
 * aqui (ou se registra pelo filtro no próprio snippet dela).
 *
 * Idempotente: rodar duas vezes não duplica página, não repete lixeira e não
 * reescreve página editada à mão. flush_rewrite_rules() só quando cria página.
 *
 * Regras herdadas (fase 4b): não usa a superglobal de servidor; sem "<?php" no
 * topo (o Code Snippets põe); texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_CASCA_VERSAO' ) ) {
	define( 'AQUAMETRIA_CASCA_VERSAO', '1.3.0' );
	define( 'AQUAMETRIA_CASCA_TAGLINE', 'Calculadoras e dados técnicos para dimensionar o seu aquário' );
}

/* ---------------------------------------------------------------------------
 * 1. Catálogo de calculadoras (fonte do hub e da home)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_calculadoras' ) ) {
function aquametria_casca_calculadoras() {
	$lista = array(
		array(
			'codigo'  => 'C1',
			'titulo'  => 'Litragem e volume útil',
			'slug'    => 'calculadora-de-litragem',
			'resumo'  => 'Medidas em centímetros para litros — volume bruto, lâmina d\'água e volume útil. É o núcleo: o resultado fica guardado no navegador e alimenta as outras calculadoras.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C3',
			'titulo'  => 'Vazão do filtro e turnover',
			'slug'    => 'calculadora-de-vazao-do-filtro',
			'resumo'  => 'Quantas renovações por hora o seu filtro entrega — e por que os fabricantes declaram de 1,8 a 10 x/h para o mesmo aquário, contra as 5 a 10 x/h repetidas na web brasileira.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C5',
			'titulo'  => 'Potência do aquecedor por delta térmico',
			'slug'    => 'calculadora-de-potencia-do-aquecedor',
			'resumo'  => 'Watts a partir da mínima do seu ambiente e da temperatura alvo, não do velho "1 W por litro". A via física fica retida até haver coeficiente térmico com fonte.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C12',
			'titulo'  => 'Mídia filtrante: volume, ordem e troca',
			'slug'    => 'calculadora-de-midia-filtrante',
			'resumo'  => 'Mililitros de mídia biológica por litro de água, pelas quatro dosagens que os fabricantes declaram — e que discordam por dez vezes entre si. Número que nenhuma fonte brasileira publica, com o teto físico do cesto do seu filtro junto.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C15',
			'titulo'  => 'Iluminação e fotoperíodo',
			'slug'    => 'calculadora-de-iluminacao',
			'resumo'  => 'Lúmens por litro nas três faixas que as fontes brasileiras chamam pelo mesmo nome com números diferentes, mais o fotoperíodo por tipo de aquário.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C2',
			'titulo'  => 'Peso do aquário cheio e carga no piso',
			'slug'    => 'calculadora-de-peso-e-carga',
			'resumo'  => 'Peso total e carga por metro quadrado, comparados com a carga de projeto da NBR 6120. Damos o número; a autorização é de engenheiro, nunca nossa.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C7',
			'titulo'  => 'Consumo elétrico e custo mensal',
			'slug'    => 'calculadora-de-consumo-de-energia',
			'resumo'  => 'Custo por mês do filtro, do aquecedor e da luz, com ciclo de trabalho — porque multiplicar a potência do aquecedor por 24 horas erra a conta para cima.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C8',
			'titulo'  => 'Lotação e aquário mínimo',
			'slug'    => 'calculadora-de-lotacao',
			'resumo'  => 'Três critérios de lotação publicados lado a lado, com a atribuição de cada um, e o aquário mínimo por espécie quando a fonte existe.',
			'estado'  => 'em-construcao',
		),
	);

	$lista = apply_filters( 'aquametria_calculadoras', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

/**
 * URL REAL da página, ou '' se ela não existe publicada no site.
 *
 * Duas vias, nesta ordem:
 *   1. o id do repositório, que o Sync grava em _aquametria_id. É a identidade
 *      canônica e sobrevive ao WordPress ter mudado o slug por conflito — quando
 *      o slug pedido já está ocupado, wp_insert_post acrescenta "-2" em silêncio
 *      e o log do Sync ainda diz "ok";
 *   2. o slug, para as páginas que não vieram do Sync.
 *
 * Devolve '' quando nenhuma via acha a página, e quem chama NÃO publica link.
 * Link do hub para página inexistente é 404 no ar: foi o defeito 2 de 08/09/2026.
 */
if ( ! function_exists( 'aquametria_casca_url_se_existir' ) ) {
function aquametria_casca_url_se_existir( $slug ) {
	$slug = sanitize_title( $slug );
	if ( '' === $slug ) {
		return '';
	}

	$achados = get_posts( array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'meta_key'    => '_aquametria_id',
		'meta_value'  => $slug,
		'numberposts' => 1,
	) );
	if ( $achados ) {
		return get_permalink( $achados[0] );
	}

	$pagina = get_page_by_path( $slug, OBJECT, 'page' );
	if ( $pagina && 'publish' === $pagina->post_status ) {
		return get_permalink( $pagina );
	}

	return '';
}
}

/**
 * Link de texto que só vira <a> se a página existir. Sem página, sai o rótulo
 * sozinho — nunca um endereço que devolve 404.
 */
if ( ! function_exists( 'aquametria_casca_link_html' ) ) {
function aquametria_casca_link_html( $slug, $rotulo ) {
	$url = aquametria_casca_url_se_existir( $slug );
	if ( '' === $url ) {
		return '<span class="aqm-sem-link">' . esc_html( $rotulo ) . '</span>';
	}
	return '<a href="' . esc_url( $url ) . '">' . esc_html( $rotulo ) . '</a>';
}
}

if ( ! function_exists( 'aquametria_casca_url_pagina' ) ) {
function aquametria_casca_url_pagina( $slug ) {
	$url = aquametria_casca_url_se_existir( $slug );
	if ( '' !== $url ) {
		return $url;
	}
	/* Último recurso, só para não devolver href vazio a quem ainda chama isto
	   direto. Quem publica link novo deve usar aquametria_casca_link_html(). */
	return home_url( '/' . sanitize_title( $slug ) . '/' );
}
}

/* ---------------------------------------------------------------------------
 * 1b. Apelidos de endereço — o 404 que o visitante não deveria ver
 *
 * Defeito de 08/09/2026: o Raphael pediu /calculadora-de-aquecedor-de-aquario/
 * e levou 404. Não era slug trocado — a página da C5 está publicada em
 * /calculadora-de-potencia-do-aquecedor/ e o hub aponta certo. O endereço
 * pedido é o que qualquer pessoa (e qualquer buscador) ADIVINHA a partir do
 * nome da calculadora, e adivinhar errado não pode custar um 404.
 *
 * Cada apelido plausível redireciona 301 para a página canônica. 301 porque a
 * URL certa é a canônica e é ela que deve acumular sinal de busca; o apelido é
 * porta de entrada, nunca endereço publicado.
 *
 * Trava: o redirecionamento SÓ acontece se a página de destino existir
 * publicada de verdade (mesma verificação do hub). Sem destino, o 404 segue —
 * redirecionar para outro 404 é pior que o 404 original.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_apelidos' ) ) {
function aquametria_casca_apelidos() {
	$mapa = array(
		/* C1 — litragem */
		'calculadora-de-litros'                          => 'calculadora-de-litragem',
		'calculadora-de-volume'                          => 'calculadora-de-litragem',
		'calculadora-de-volume-de-aquario'               => 'calculadora-de-litragem',
		'calculadora-de-litragem-de-aquario'             => 'calculadora-de-litragem',
		'quantos-litros-tem-meu-aquario'                 => 'calculadora-de-litragem',
		/* C3 — vazão */
		'calculadora-de-vazao'                           => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-vazao-de-filtro'                 => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-filtro'                          => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-filtro-de-aquario'               => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-turnover'                        => 'calculadora-de-vazao-do-filtro',
		/* C5 — aquecedor */
		'calculadora-de-aquecedor'                       => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-aquecedor-de-aquario'            => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-potencia-do-aquecedor-de-aquario' => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-watts'                           => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-watts-do-aquecedor'              => 'calculadora-de-potencia-do-aquecedor',
		/* C12 — mídia filtrante */
		'calculadora-de-midia'                           => 'calculadora-de-midia-filtrante',
		'calculadora-de-midia-biologica'                 => 'calculadora-de-midia-filtrante',
		'calculadora-de-midia-filtrante-de-aquario'      => 'calculadora-de-midia-filtrante',
		/* C15 — iluminação */
		'calculadora-de-luz'                             => 'calculadora-de-iluminacao',
		'calculadora-de-lumens'                          => 'calculadora-de-iluminacao',
		'calculadora-de-iluminacao-de-aquario'           => 'calculadora-de-iluminacao',
		'calculadora-de-iluminacao-de-aquario-plantado'  => 'calculadora-de-iluminacao',
	);

	return apply_filters( 'aquametria_apelidos_de_pagina', $mapa );
}
}

/**
 * Slug canônico de um caminho pedido, ou '' se ele não for apelido conhecido.
 * Isolada da requisição de propósito, para o teste poder exercitá-la sozinha.
 */
if ( ! function_exists( 'aquametria_casca_apelido_para_slug' ) ) {
function aquametria_casca_apelido_para_slug( $caminho ) {
	$caminho = trim( (string) $caminho );
	$caminho = trim( $caminho, '/' );
	if ( '' === $caminho || false !== strpos( $caminho, '/' ) ) {
		return '';
	}

	$caminho = sanitize_title( $caminho );
	$mapa    = aquametria_casca_apelidos();

	return isset( $mapa[ $caminho ] ) ? $mapa[ $caminho ] : '';
}
}

/**
 * Caminho pedido nesta requisição, sem a superglobal de servidor (fase 4b).
 * $wp->request já vem sem barra inicial, sem barra final e sem query string.
 */
if ( ! function_exists( 'aquametria_casca_caminho_pedido' ) ) {
function aquametria_casca_caminho_pedido() {
	if ( isset( $GLOBALS['wp'] ) && is_object( $GLOBALS['wp'] ) && isset( $GLOBALS['wp']->request ) ) {
		return (string) $GLOBALS['wp']->request;
	}

	$atual = add_query_arg( array() );
	$atual = strtok( (string) $atual, '?' );

	return trim( (string) $atual, '/' );
}
}

if ( ! function_exists( 'aquametria_casca_redirecionar_apelido' ) ) {
function aquametria_casca_redirecionar_apelido() {
	if ( ! is_404() ) {
		return;
	}

	$destino = aquametria_casca_apelido_para_slug( aquametria_casca_caminho_pedido() );
	if ( '' === $destino ) {
		return;
	}

	$url = aquametria_casca_url_se_existir( $destino );
	if ( '' === $url ) {
		return;
	}

	wp_safe_redirect( $url, 301 );
	exit;
}
}

add_action( 'template_redirect', 'aquametria_casca_redirecionar_apelido' );

/* ---------------------------------------------------------------------------
 * 2. Marca, menu e rodapé
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_logo_svg' ) ) {
function aquametria_casca_logo_svg() {
	$svg  = '<svg viewBox="0 0 40 48" width="30" height="36" role="img" aria-label="Aquametria" focusable="false">';
	$svg .= '<path d="M9 4h22v34a5 5 0 0 1-5 5H14a5 5 0 0 1-5-5z" fill="#FFFFFF" stroke="#0D1B22" stroke-width="2.6" stroke-linejoin="round"/>';
	$svg .= '<path d="M11.6 25h16.8v13a3.4 3.4 0 0 1-3.4 3.4H15a3.4 3.4 0 0 1-3.4-3.4z" fill="#0E7C8C"/>';
	$svg .= '<path d="M11.6 25h16.8" stroke="#0E7C8C" stroke-width="2.6" stroke-linecap="round"/>';
	$svg .= '<g stroke="#0D1B22" stroke-width="1.8" stroke-linecap="round">';
	$svg .= '<path d="M12 10h9"/><path d="M12 14.5h5.5"/><path d="M12 19h9"/>';
	$svg .= '</g>';
	$svg .= '<g stroke="#F4F7F7" stroke-width="1.8" stroke-linecap="round">';
	$svg .= '<path d="M14 30h9"/><path d="M14 34.5h5.5"/>';
	$svg .= '</g>';
	$svg .= '<path d="M7.4 4h25.2" stroke="#0D1B22" stroke-width="2.6" stroke-linecap="round"/>';
	$svg .= '</svg>';

	return $svg;
}
}

if ( ! function_exists( 'aquametria_casca_marca_html' ) ) {
function aquametria_casca_marca_html() {
	static $ja_impressa = false;
	if ( $ja_impressa ) {
		return '';
	}
	$ja_impressa = true;

	return '<a class="aqm-marca" href="' . esc_url( home_url( '/' ) ) . '" rel="home">'
		. aquametria_casca_logo_svg()
		. '<span class="aqm-wordmark">Aquametria</span>'
		. '</a>';
}
}

/**
 * O menu. Abaixo de 782 px ele vira sanfona atrás de um botão; acima, é a mesma
 * fileira de links de sempre.
 *
 * Três decisões, e nenhuma delas é enfeite:
 *
 *   1. Os links saem SEMPRE no HTML servido, dentro de <nav>. O botão não gera
 *      link nenhum: ele só mostra e esconde o que já está lá. É o que faz o menu
 *      continuar existindo para quem lê a página sem executar JavaScript — o
 *      crawler de IA, que é regra de primeira classe do projeto, e o visitante
 *      cujo script não carregou.
 *   2. Quem esconde a lista no celular é o seletor [data-aqm-menu], e esse
 *      atributo quem põe é o JavaScript do rodapé. Sem JavaScript o atributo não
 *      existe, a regra não casa e o menu fica visível como lista, que é
 *      exatamente o que o site fazia antes desta versão. Esconder por padrão e
 *      contar com o script para revelar seria trocar um defeito por outro pior.
 *   3. O id é contado, porque o filtro render_block pode trocar mais de um bloco
 *      core/navigation na mesma página, e aria-controls que aponta para um id
 *      repetido não controla coisa nenhuma.
 */
if ( ! function_exists( 'aquametria_casca_nav_html' ) ) {
function aquametria_casca_nav_html() {
	static $quantos = 0;
	$quantos++;
	$id = 'aqm-nav-lista' . ( $quantos > 1 ? '-' . $quantos : '' );

	$itens = array(
		'calculadoras' => 'Calculadoras',
		'metodologia'  => 'Metodologia',
		'sobre'        => 'Sobre',
	);

	$html  = '<div class="aqm-nav-caixa">';
	$html .= '<button type="button" class="aqm-nav-botao" aria-expanded="false" aria-controls="' . esc_attr( $id ) . '">';
	$html .= '<span class="aqm-nav-tracos" aria-hidden="true"></span>';
	$html .= '<span class="aqm-nav-rotulo">Menu</span>';
	$html .= '</button>';
	$html .= '<nav class="aqm-nav" id="' . esc_attr( $id ) . '" aria-label="Navegação principal"><ul>';
	foreach ( $itens as $slug => $rotulo ) {
		$html .= '<li>' . aquametria_casca_link_html( $slug, $rotulo ) . '</li>';
	}
	$html .= '</ul></nav>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_casca_rodape_impresso' ) ) {
/**
 * Marca e consulta se o rodapé da Aquametria já saiu nesta requisição.
 * Evita rodapé duplicado quando o filtro render_block já trocou a template part.
 */
function aquametria_casca_rodape_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_casca_rodape_html' ) ) {
function aquametria_casca_rodape_html() {
	aquametria_casca_rodape_impresso( true );

	$html  = '<footer class="aqm-rodape"><div class="aqm-rodape-interno">';
	$html .= '<p class="aqm-tagline">' . esc_html( AQUAMETRIA_CASCA_TAGLINE ) . '</p>';
	$html .= '<p>Todo número publicado aqui cita a fonte — manual de fabricante, norma técnica ou fonte brasileira nomeada — e leva a data em que foi verificado. Quando as fontes discordam, a Aquametria publica a divergência com a atribuição de cada extremo, nunca a média. Onde não há fonte aceitável, a página diz por que não publica número.</p>';
	$html .= '<p>' . aquametria_casca_link_html( 'metodologia', 'Metodologia' )
		. ' · ' . aquametria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
		. ' · ' . aquametria_casca_link_html( 'sobre', 'Sobre' )
		. ' · Aquametria ' . esc_html( date_i18n( 'Y' ) ) . '</p>';
	$html .= '</div></footer>';

	return $html;
}
}

add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	$nome = isset( $bloco['blockName'] ) ? $bloco['blockName'] : '';
	if ( 'core/site-title' === $nome || 'core/site-logo' === $nome ) {
		return aquametria_casca_marca_html();
	}
	if ( 'core/navigation' === $nome ) {
		return aquametria_casca_nav_html();
	}
	// A tagline padrão do WordPress ("Just another WordPress site") é resíduo do
	// tema; a tagline da Aquametria mora no rodapé.
	if ( 'core/site-tagline' === $nome ) {
		return '';
	}
	// Em tema de blocos o rodapé é uma template part renderizada DENTRO do fluxo
	// do conteúdo. Trocar a saída dela aqui é o que impede os dois rodapés
	// empilhados (o do tema, com o crédito "Criado com WordPress", e o nosso).
	if ( 'core/template-part' === $nome ) {
		$parte = isset( $bloco['attrs']['slug'] ) ? $bloco['attrs']['slug'] : '';
		if ( 'footer' === $parte || 'rodape' === $parte ) {
			return aquametria_casca_rodape_html();
		}
	}
	return $conteudo;
}, 10, 2 );

// Rede de segurança: se o tema NÃO usa template part de rodapé (ou o filtro não
// pegou), o rodapé sai aqui. Se já saiu no lugar da template part, não repete.
add_action( 'wp_footer', function () {
	if ( aquametria_casca_rodape_impresso() ) {
		return;
	}

	echo aquametria_casca_rodape_html(); // markup próprio, já escapado campo a campo
}, 20 );

/* ---------------------------------------------------------------------------
 * 2b. Ícone do site
 *
 * O WordPress imprime o ícone dele em wp_head na prioridade 99, e sem tirar
 * aquele de lá o site sairia com dois — a aba escolheria um, o iOS outro. Aqui
 * o ícone é o recipiente graduado da marca, viajando dentro do snippet como
 * data URI: nada sobe para a biblioteca de mídia.
 *
 * O desenho não se edita à mão neste arquivo: ele é gerado por
 * ferramentas/gerar-favicon.php, entre os marcadores abaixo, pelo mesmo motivo
 * que o catálogo de produtos é gerado dentro das calculadoras — desenho mantido
 * em dois lugares diverge em silêncio.
 * ------------------------------------------------------------------------- */

/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */
if ( ! defined( 'AQUAMETRIA_CASCA_ICONE_SVG' ) ) {
	define( 'AQUAMETRIA_CASCA_ICONE_SVG', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#0D1B22"/><rect x="7" y="4" width="18" height="1.8" rx=".9" fill="#FFFFFF"/><path d="M9 6.6h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#FFFFFF"/><path d="M9 17.4h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#0E7C8C"/><g fill="#0D1B22"><rect x="11.6" y="9.6" width="8.8" height="1.8" rx=".9"/><rect x="11.6" y="13.2" width="5.4" height="1.8" rx=".9"/></g></svg>' );
	define( 'AQUAMETRIA_CASCA_ICONE_PNG_180', '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' );
	define( 'AQUAMETRIA_CASCA_ICONE_PNG_32', 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAElBMVEX9/f0MeosMGiDX2dkMangyPkRE6xmSAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAATklEQVQoz2NQQgMMZAowQAETVEAZJsCKUwtUCTNJAiBSAa8AMWYoowowKSmQ5g4VQUdBRxFBESQBMKCxgBJEQAiPgCJYADmiVKAmkBW3AE2xNWcHmXfXAAAAAElFTkSuQmCC' );
}
/* FAVICON-FIM */

remove_action( 'wp_head', 'wp_site_icon', 99 );

add_action( 'wp_head', function () {
	if ( ! defined( 'AQUAMETRIA_CASCA_ICONE_SVG' ) ) {
		return;
	}

	echo '<link rel="icon" type="image/svg+xml" href="' . esc_attr( 'data:image/svg+xml,' . rawurlencode( AQUAMETRIA_CASCA_ICONE_SVG ) ) . '">' . "\n";
	// Segunda linha para quem não desenha SVG na aba: o mesmo desenho, em PNG de
	// 32 px. 'alternate icon' é o rel que o navegador só usa quando desiste do
	// primeiro.
	echo '<link rel="alternate icon" type="image/png" sizes="32x32" href="' . esc_attr( 'data:image/png;base64,' . AQUAMETRIA_CASCA_ICONE_PNG_32 ) . '">' . "\n";
	// O iOS não aceita SVG neste rel, e ele aplica a própria máscara de canto —
	// por isso o PNG é quadrado, em sangria, sem arredondamento por baixo.
	echo '<link rel="apple-touch-icon" sizes="180x180" href="' . esc_attr( 'data:image/png;base64,' . AQUAMETRIA_CASCA_ICONE_PNG_180 ) . '">' . "\n";
	echo '<meta name="theme-color" content="#0D1B22">' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * 3. Tipografia e paleta por cima do tema ativo
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$fontes = 'https://fonts.googleapis.com/css2?family=Chivo:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap';

	echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
	echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
	echo '<link rel="stylesheet" href="' . esc_url( $fontes ) . '">' . "\n";

	$css = <<<'CSS'
:root{
--aqm-tinta:#0D1B22;--aqm-lamina:#0E7C8C;--aqm-papel:#F4F7F7;--aqm-superficie:#FFFFFF;
--aqm-traco:#DDE5E6;--aqm-legenda:#5C7075;--aqm-alerta:#B5762A;
--aqm-display:"Chivo","Trebuchet MS",Arial,sans-serif;
--aqm-texto:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--aqm-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
body{
--wp--preset--color--base:#F4F7F7;--wp--preset--color--contrast:#0D1B22;
--wp--preset--color--primary:#0E7C8C;--wp--preset--color--secondary:#5C7075;
--wp--preset--font-family--body:var(--aqm-texto);
--wp--preset--font-family--heading:var(--aqm-display);
}
html body{background-color:var(--aqm-papel);color:var(--aqm-tinta);font-family:var(--aqm-texto);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;}
body h1,body h2,body h3,body h4,body h5,body h6{font-family:var(--aqm-display);color:var(--aqm-tinta);line-height:1.2;letter-spacing:-0.015em;}
body h1{font-weight:900;}
body a{color:var(--aqm-lamina);text-underline-offset:2px;}
body a:hover{color:var(--aqm-tinta);}
body code,body kbd,body samp,body pre,body .aqm-num{font-family:var(--aqm-mono);font-variant-numeric:tabular-nums;}
body .wp-block-button__link,body button,body input[type=submit]{background-color:var(--aqm-lamina);color:var(--aqm-superficie);border:0;border-radius:2px;font-family:var(--aqm-texto);font-weight:600;}
body hr,body .wp-block-separator{border-color:var(--aqm-traco);color:var(--aqm-traco);}
body table{border-collapse:collapse;}
body table th,body table td{border:1px solid var(--aqm-traco);padding:.5rem .7rem;text-align:left;}
body table th{background:var(--aqm-superficie);font-family:var(--aqm-display);font-weight:700;}
body header .wp-block-group,body .wp-block-template-part header{background:var(--aqm-superficie);}
.aqm-marca{display:inline-flex;align-items:center;gap:.6rem;text-decoration:none;}
.aqm-marca:hover{text-decoration:none;}
.aqm-marca svg{display:block;flex:0 0 auto;}
.aqm-wordmark{font-family:var(--aqm-display);font-weight:900;font-size:1.5rem;letter-spacing:-0.03em;color:var(--aqm-tinta);line-height:1;}
.aqm-nav ul{display:flex;flex-wrap:wrap;gap:1.4rem;list-style:none;margin:0;padding:0;}
.aqm-nav li{margin:0;}
.aqm-nav a{font-family:var(--aqm-texto);font-weight:600;font-size:.95rem;color:var(--aqm-tinta);text-decoration:none;padding-bottom:.15rem;border-bottom:2px solid transparent;}
.aqm-nav a:hover{color:var(--aqm-lamina);border-bottom-color:var(--aqm-lamina);}
.aqm-nav-caixa{position:relative;}
/* O botao do menu so aparece no celular, e so quando ha JavaScript para ele
   comandar (o atributo data-aqm-menu e posto pelo script do rodape). */
.aqm-nav-botao{display:none;align-items:center;gap:.55rem;background:transparent;color:var(--aqm-tinta);border:1px solid var(--aqm-traco);border-radius:2px;padding:.5rem .75rem;font-family:var(--aqm-texto);font-weight:600;font-size:.92rem;line-height:1;cursor:pointer;}
.aqm-nav-botao:hover{border-color:var(--aqm-lamina);color:var(--aqm-lamina);}
.aqm-nav-tracos{position:relative;display:block;width:1.05rem;height:2px;background:currentColor;border-radius:2px;}
.aqm-nav-tracos::before,.aqm-nav-tracos::after{content:"";position:absolute;left:0;width:100%;height:2px;background:currentColor;border-radius:2px;}
.aqm-nav-tracos::before{top:-.36rem;}
.aqm-nav-tracos::after{top:.36rem;}
.aqm-nav-botao:focus-visible,.aqm-nav a:focus-visible,.aqm-marca:focus-visible{outline:2px solid var(--aqm-lamina);outline-offset:3px;}
.aqm-bloco{max-width:52rem;}
.aqm-linha-mestra{font-family:var(--aqm-display);font-size:1.35rem;line-height:1.35;font-weight:700;margin:0 0 .8rem;}
.aqm-abertura p{margin:0 0 .7rem;}
.aqm-secao{margin:2.4rem 0 0;}
.aqm-secao h2{margin:0 0 .6rem;font-size:1.35rem;}
.aqm-secao h3{margin:1.4rem 0 .4rem;font-size:1.08rem;}
.aqm-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:1rem;margin:1.4rem 0 0;padding:0;list-style:none;}
.aqm-card{background:var(--aqm-superficie);border:1px solid var(--aqm-traco);border-radius:3px;padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.5rem;margin:0;}
.aqm-card h3{font-family:var(--aqm-display);font-size:1.05rem;margin:0;line-height:1.25;}
.aqm-card p{margin:0;color:var(--aqm-legenda);font-size:.93rem;line-height:1.5;}
.aqm-codigo{font-family:var(--aqm-mono);font-size:.72rem;letter-spacing:.1em;color:var(--aqm-legenda);}
.aqm-acao{margin-top:auto;padding-top:.3rem;}
.aqm-acao a{font-weight:600;text-decoration:none;border-bottom:2px solid var(--aqm-lamina);}
.aqm-sem-link{color:var(--aqm-legenda);}
.aqm-rodape .aqm-sem-link{color:var(--aqm-traco);}
.aqm-tag{display:inline-block;font-family:var(--aqm-mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--aqm-alerta);border:1px solid var(--aqm-alerta);border-radius:2px;padding:.15rem .4rem;}
.aqm-tag-viva{color:var(--aqm-lamina);border-color:var(--aqm-lamina);}
.aqm-nota{border-left:3px solid var(--aqm-lamina);background:var(--aqm-superficie);padding:.85rem 1rem;color:var(--aqm-legenda);font-size:.95rem;margin:1.2rem 0 0;}
.aqm-nota strong{color:var(--aqm-tinta);}
.aqm-lista{margin:.6rem 0 0;padding-left:1.1rem;}
/* Citação em bloco vinda do Markdown do repositório (conversor do Sync 1.1.2):
   é onde mora fórmula e regra citada, então sai em monoespaçada. */
.aqm-citacao{border-left:3px solid var(--aqm-lamina);background:var(--aqm-superficie);margin:1.2rem 0;padding:.9rem 1.1rem;font-size:.95rem;line-height:1.6;}
.aqm-citacao p{margin:0 0 .5rem;font-family:var(--aqm-mono);}
.aqm-citacao p:last-child{margin-bottom:0;}
.aqm-tabela{margin:1.2rem 0;}
.aqm-lista li{margin:0 0 .45rem;}
.aqm-quadro{width:100%;margin:1rem 0 0;font-size:.93rem;}
.aqm-quadro td:first-child{font-family:var(--aqm-mono);font-size:.85rem;white-space:nowrap;}
.aqm-quadro td:last-child{text-align:right;font-family:var(--aqm-mono);}
.aqm-rodape{background:var(--aqm-tinta);color:var(--aqm-papel);padding:2.4rem 1.5rem;margin-top:3.5rem;font-family:var(--aqm-texto);}
.aqm-rodape-interno{max-width:52rem;margin:0 auto;display:flex;flex-direction:column;gap:.7rem;}
.aqm-rodape .aqm-tagline{font-family:var(--aqm-display);font-weight:700;font-size:1.1rem;color:var(--aqm-superficie);margin:0;}
.aqm-rodape p{margin:0;font-size:.86rem;line-height:1.55;color:var(--aqm-traco);}
.aqm-rodape a{color:var(--aqm-papel);}
/* Cinto de segurança do rodapé: o caminho principal é o filtro render_block, que
   troca a template part 'footer' do tema pela da Aquametria. Se ele não pegar,
   o rodapé do tema fica visível acima do nosso — as regras abaixo escondem o
   crédito do tema e, havendo rodapé da Aquametria na página, a template part
   de rodapé que não seja a nossa. */
.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}
body:has(.aqm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.aqm-rodape)){display:none;}
@media (max-width:600px){
.aqm-linha-mestra{font-size:1.15rem;}
.aqm-wordmark{font-size:1.25rem;}
}
/* Menu sanfona. 782 px e a largura em que o proprio WordPress considera que a
   tela virou celular; seguir a mesma quebra evita cabecalho meio empilhado.
   Tudo aqui depende de [data-aqm-menu]: sem JavaScript nada disso vale e o menu
   continua sendo a fileira de links, visivel, que sempre foi. */
@media (max-width:782px){
.aqm-nav-caixa[data-aqm-menu] .aqm-nav-botao{display:inline-flex;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav{display:none;position:absolute;right:0;top:calc(100% + .55rem);z-index:60;min-width:13rem;background:var(--aqm-superficie);border:1px solid var(--aqm-traco);border-radius:3px;box-shadow:0 12px 32px rgba(13,27,34,.16);padding:.35rem 0;}
.aqm-nav-caixa[data-aqm-menu][data-aqm-aberto="1"] .aqm-nav{display:block;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav ul,.aqm-nav-caixa[data-aqm-menu] .aqm-nav li{display:block;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav a,.aqm-nav-caixa[data-aqm-menu] .aqm-nav .aqm-sem-link{display:block;padding:.65rem 1.05rem;font-size:1rem;border-bottom:0;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav a:hover{background:var(--aqm-papel);color:var(--aqm-lamina);}
}
CSS;

	echo '<style id="aquametria-casca">' . $css . '</style>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * 3b. O comando do menu sanfona
 *
 * O script sai no wp_footer, NUNCA dentro do retorno de um shortcode. É a regra
 * que nasceu do defeito de 08/09/2026: o WordPress roda os filtros de texto do
 * conteúdo sobre o que o shortcode devolve, cada "&" vira "&#038;" e o
 * JavaScript inteiro morre com erro de sintaxe. Aqui ele não passa por filtro
 * nenhum.
 *
 * O script não desenha menu: ele só assume o comando do que o PHP já serviu. A
 * primeira coisa que faz é pôr data-aqm-menu na caixa, e é esse atributo que
 * liga as regras de CSS do celular — ou seja, o menu só se fecha depois que
 * existe alguém para reabri-lo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	$js = <<<'JS'
(function () {
	var caixas = document.querySelectorAll('.aqm-nav-caixa');
	if (!caixas.length) { return; }

	Array.prototype.forEach.call(caixas, function (caixa) {
		var botao = caixa.querySelector('.aqm-nav-botao');
		var lista = caixa.querySelector('.aqm-nav');
		if (!botao || !lista) { return; }

		/* A partir daqui o CSS do celular vale: há quem reabra o menu. */
		caixa.setAttribute('data-aqm-menu', '1');

		function aberto() {
			return caixa.getAttribute('data-aqm-aberto') === '1';
		}
		function estado(abrir) {
			caixa.setAttribute('data-aqm-aberto', abrir ? '1' : '0');
			botao.setAttribute('aria-expanded', abrir ? 'true' : 'false');
		}
		estado(false);

		botao.addEventListener('click', function (ev) {
			ev.preventDefault();
			estado(!aberto());
		});

		/* Escape fecha e devolve o foco ao botão: quem abriu pelo teclado não
		   pode ficar com o foco preso num menu que sumiu. */
		caixa.addEventListener('keydown', function (ev) {
			if (!aberto()) { return; }
			if (ev.key === 'Escape' || ev.key === 'Esc') {
				estado(false);
				botao.focus();
			}
		});

		document.addEventListener('click', function (ev) {
			if (aberto() && !caixa.contains(ev.target)) { estado(false); }
		});

		/* Girar o telefone ou alargar a janela passa da faixa do celular: o menu
		   volta a ser fileira de links e não pode continuar marcado como aberto,
		   senão o aria-expanded mente para o leitor de tela. */
		window.addEventListener('resize', function () {
			if (aberto() && window.innerWidth > 782) { estado(false); }
		});
	});
})();
JS;

	echo '<script id="aquametria-casca-menu">' . $js . '</script>' . "\n";
}, 25 );

/* ---------------------------------------------------------------------------
 * 4. Conteúdo das quatro páginas (shortcodes)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_cards_html' ) ) {
function aquametria_casca_cards_html() {
	$html = '<ul class="aqm-cards">';
	foreach ( aquametria_casca_calculadoras() as $c ) {
		$publicada = ( isset( $c['estado'] ) && 'publicada' === $c['estado'] );
		$html     .= '<li class="aqm-card">';
		$html     .= '<span class="aqm-codigo">' . esc_html( $c['codigo'] ) . '</span>';
		$html     .= '<h3>' . esc_html( $c['titulo'] ) . '</h3>';
		$html     .= '<p>' . esc_html( $c['resumo'] ) . '</p>';
		$html     .= '<span class="aqm-acao">';
		$url = $publicada ? aquametria_casca_url_se_existir( $c['slug'] ) : '';
		if ( '' !== $url ) {
			$html .= '<a href="' . esc_url( $url ) . '">Abrir calculadora</a>';
		} else {
			/* A calculadora pode ter se anunciado publicada e a página ainda não
			   existir (Sync atrasado, slug tomado por outra página). Melhor o
			   selo honesto que um link que devolve 404. */
			$html .= '<span class="aqm-tag">Em construção</span>';
		}
		$html .= '</span></li>';
	}
	$html .= '</ul>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_casca_conta_publicadas' ) ) {
function aquametria_casca_conta_publicadas() {
	$n = 0;
	foreach ( aquametria_casca_calculadoras() as $c ) {
		if ( isset( $c['estado'] ) && 'publicada' === $c['estado'] ) {
			$n++;
		}
	}
	return $n;
}
}

add_shortcode( 'aquametria_home', function () {
	$total      = count( aquametria_casca_calculadoras() );
	$publicadas = aquametria_casca_conta_publicadas();

	$html  = '<div class="aqm-bloco">';
	$html .= '<div class="aqm-abertura">';
	$html .= '<p class="aqm-linha-mestra">A Aquametria dimensiona aquário com número que tem fonte: litragem, vazão de filtro, potência de aquecedor, mídia filtrante e iluminação.</p>';
	$html .= '<p>Cada resposta sai como <strong>faixa</strong>, com o critério e a fonte de cada extremo — nunca um número seco. Quando as fontes brasileiras discordam entre si, a discordância vai para a tela com a atribuição de cada lado.</p>';
	$html .= '<p>Onde não existe fonte aceitável, a página diz por que não publica número. É isso, e só isso, que separa uma calculadora de um chute com botão.</p>';
	$html .= '</div>';

	$html .= '<div class="aqm-secao">';
	$html .= '<h2>Calculadoras</h2>';
	if ( 0 === $publicadas ) {
		$html .= '<p>As oito calculadoras do lote inicial já estão especificadas, com fórmula, faixas de saída e a fonte de cada constante. Elas entram no ar uma por vez, na ordem abaixo.</p>';
	} else {
		$html .= '<p>' . esc_html( $publicadas ) . ' de ' . esc_html( $total ) . ' calculadoras do lote inicial já estão no ar. As demais entram uma por vez, na ordem abaixo.</p>';
	}
	$html .= aquametria_casca_cards_html();
	$html .= '</div>';

	$html .= '<div class="aqm-secao">';
	$html .= '<h2>Como a Aquametria calcula</h2>';
	$html .= '<p>Toda constante usada em uma fórmula tem fonte nomeada, endereço e data de verificação, e carrega um status que diz o quanto ela é firme. Constante sem fonte aceitável é proibida em fórmula publicada — fica registrada como pendente e a página explica a ausência.</p>';
	$html .= '<p>' . aquametria_casca_link_html( 'metodologia', 'Ler a metodologia completa' ) . '</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'aquametria_calculadoras', function () {
	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">Oito calculadoras de dimensionamento, publicadas uma por vez.</p>';
	$html .= '<p>A ordem não é aleatória: a calculadora de litragem é o núcleo. O aquário que você descreve nela fica guardado no seu próprio navegador e é reaproveitado pelas outras, para você não redigitar medidas a cada conta. Nada é enviado para servidor nenhum: sem conta, sem login, sem coleta.</p>';
	$html .= aquametria_casca_cards_html();
	$html .= '<p class="aqm-nota"><strong>Em construção não é enfeite.</strong> Uma calculadora só entra no ar com a fonte de cada constante conferida e com a divergência entre fontes exposta na tela. Preferimos uma calculadora impecável a duas medianas.</p>';
	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'aquametria_casca_quadro_constantes' ) ) {
function aquametria_casca_quadro_constantes() {
	$vocabulario = array(
		'fisica'                => 'Valor tabelado de física; a fórmula declara o arredondamento usado.',
		'verificada-fabricante' => 'Lida diretamente na página ou no manual do fabricante.',
		'fabricante-via-busca'  => 'Número do fabricante colhido por resultado de busca, com a página ainda por ler direto. Marcada para reconferência.',
		'norma-via-secundaria'  => 'Valor de norma ABNT citado por fonte secundária — a norma é paga e não foi lida direto.',
		'transcrita-varejo'     => 'Rótulo ou ficha transcrita por varejista. A tela pede que você confira a embalagem.',
		'divergente-fontes-br'  => 'As fontes brasileiras conflitam. A resposta publica a faixa inteira e diz de quem é cada extremo.',
		'convencao-editorial'   => 'Escolha da Aquametria, não dado técnico. A tela precisa dizer isso.',
		'pendente'              => 'Sem fonte aceitável. Proibida em fórmula publicada.',
	);

	// Instantâneo de 07/09/2026; se o banco de constantes estiver publicado no site, conta ao vivo.
	$contagem = array(
		'fisica'                => 1,
		'verificada-fabricante' => 1,
		'fabricante-via-busca'  => 3,
		'norma-via-secundaria'  => 1,
		'transcrita-varejo'     => 3,
		'divergente-fontes-br'  => 24,
		'convencao-editorial'   => 1,
		'pendente'              => 8,
	);

	$dados = get_option( 'aquametria_dados_constantes-calculadoras' );
	if ( is_array( $dados ) && ! empty( $dados['constantes'] ) && is_array( $dados['constantes'] ) ) {
		$viva = array_fill_keys( array_keys( $vocabulario ), 0 );
		foreach ( $dados['constantes'] as $c ) {
			if ( isset( $c['status'] ) && isset( $viva[ $c['status'] ] ) ) {
				$viva[ $c['status'] ]++;
			}
		}
		if ( array_sum( $viva ) > 0 ) {
			$contagem = $viva;
		}
	}

	return array( 'vocabulario' => $vocabulario, 'contagem' => $contagem, 'total' => array_sum( $contagem ) );
}
}

add_shortcode( 'aquametria_metodologia', function () {
	$q = aquametria_casca_quadro_constantes();

	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">A Aquametria não publica número sem fonte, e não esconde quando as fontes discordam.</p>';
	$html .= '<p>Aquarismo brasileiro é um campo em que a mesma pergunta recebe três respostas diferentes, todas escritas com a mesma segurança. A metodologia abaixo existe para você conseguir julgar o número em vez de acreditar nele.</p>';

	$html .= '<div class="aqm-secao"><h2>1. Toda resposta é uma faixa, com critério e fonte em cada extremo</h2>';
	$html .= '<p>Nenhuma calculadora devolve um número seco. A resposta traz o piso, o teto, o critério que define cada um e a fonte que sustenta esse critério. Quando o piso vem de um fabricante e o teto de uma convenção brasileira, isso fica escrito na tela: são coisas de peso diferente.</p></div>';

	$html .= '<div class="aqm-secao"><h2>2. Divergência é publicada, nunca virada em média</h2>';
	$html .= '<p>Tirar média de fontes que discordam fabrica um número que ninguém defende. Um exemplo real do nosso banco: o turnover implícito declarado pelos próprios fabricantes de filtro vai de 1,76 a 10 renovações por hora — os fabricantes divergem entre si por 5,7 vezes, e todos divergem das 5 a 10 x/h repetidas na web brasileira. A calculadora mostra o intervalo inteiro e a atribuição, porque a divergência é a informação.</p></div>';

	$html .= '<div class="aqm-secao"><h2>3. Toda constante tem status</h2>';
	$html .= '<p>Cada número usado numa fórmula está registrado com fonte, endereço, data de verificação e um status que diz o quanto ele é firme. São ' . esc_html( $q['total'] ) . ' constantes registradas até aqui, incluindo as que foram recusadas.</p>';
	$html .= '<table class="aqm-quadro"><tr><th>Status</th><th>O que significa</th><th>Hoje</th></tr>';
	foreach ( $q['vocabulario'] as $status => $descricao ) {
		$n     = isset( $q['contagem'][ $status ] ) ? $q['contagem'][ $status ] : 0;
		$html .= '<tr><td>' . esc_html( $status ) . '</td><td>' . esc_html( $descricao ) . '</td><td>' . esc_html( $n ) . '</td></tr>';
	}
	$html .= '</table>';
	$html .= '<p class="aqm-nota"><strong>Constante com status pendente é proibida em fórmula publicada.</strong> Ela fica no registro para que a ausência seja auditável, e para que qualquer pessoa saiba exatamente o que falta para o número existir.</p></div>';

	$html .= '<div class="aqm-secao"><h2>4. O que a Aquametria não publica, e por quê</h2>';
	$html .= '<p>Esta lista é parte da metodologia, não uma desculpa. Cada item volta no dia em que a fonte aparecer.</p>';
	$html .= '<ul class="aqm-lista">';
	$html .= '<li><strong>Espessura do vidro por litragem.</strong> Não temos tensão admissível e coeficiente de segurança citáveis. Errar aqui alaga casa.</li>';
	$html .= '<li><strong>O veredito "a sua laje aguenta".</strong> Damos a carga por metro quadrado e a carga de projeto da NBR 6120 para comparação. A autorização é de engenheiro, nunca de calculadora.</li>';
	$html .= '<li><strong>O cálculo físico do aquecedor.</strong> A fórmula de perda térmica exige o coeficiente de transmissão do vidro do aquário, e não achamos esse valor com fonte. Publicamos as regras de bolso com a atribuição de cada uma, e dizemos que nenhuma fonte brasileira cobre diferença de temperatura maior que 10 °C.</li>';
	$html .= '<li><strong>O desconto de substrato na litragem.</strong> As fontes brasileiras discordam em 100 % na densidade do substrato e nenhuma publica porosidade. O volume sai superestimado, e cada calculadora diz para que lado isso a torna segura ou insegura.</li>';
	$html .= '<li><strong>A "regra dos 10 %" de lotação.</strong> A fonte não define sobre qual base os 10 % incidem.</li>';
	$html .= '<li><strong>PPFD por litragem.</strong> Lúmen por litro ignora profundidade e espectro, e nenhuma fonte brasileira publica PPFD por litragem.</li>';
	$html .= '<li><strong>Dosagem de condicionador, sal e medicamento.</strong> Risco letal com apenas duas dosagens verificadas no fabricante, e a litragem superestimada erraria para overdose. Fica fora até haver rótulo conferido em quantidade.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="aqm-secao"><h2>5. Procedência e correção</h2>';
	$html .= '<p>No banco de produtos a procedência é por campo, não por ficha: cada dado de um filtro, aquecedor, luminária ou mídia aponta para a fonte que o sustenta, com endereço e data. Campo sem fonte fica vazio, e vazio é melhor que inventado. Preço é série temporal separada, com loja e data de leitura, e nunca entra em critério técnico de sugestão.</p>';
	$html .= '<p>Quando aparece fonte melhor, a constante é substituída e a data de verificação da página muda junto. Correção não é vergonha: é o que a data serve para permitir.</p></div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'aquametria_sobre', function () {
	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">A Aquametria é um instrumento de medida para aquarismo, não um blog de opinião.</p>';
	$html .= '<p>Publicamos calculadoras de dimensionamento e um banco de dados técnico de equipamentos, com uma regra única: todo número cita a fonte e leva a data em que foi verificado.</p>';

	$html .= '<div class="aqm-secao"><h2>Por que existe</h2>';
	$html .= '<p>Ao levantar o que o aquarismo brasileiro publica, encontramos perguntas frequentes que ninguém responde com número de fonte: quanta mídia biológica cabe por litro de aquário, que potência de aquecedor a sua diferença de temperatura real exige, e qual a dureza da água da torneira na sua cidade. O que existe é regra de bolso repetida de site em site, sem origem. A Aquametria começa por esses vazios.</p></div>';

	$html .= '<div class="aqm-secao"><h2>Como é feita</h2>';
	$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é a metodologia e a procedência do dado, e as duas ficam abertas para conferência em cada página. Calculadora e conteúdo são versionados em repositório público antes de chegarem ao site — o que está no ar tem histórico.</p></div>';

	$html .= '<div class="aqm-secao"><h2>O que a Aquametria não faz</h2>';
	$html .= '<ul class="aqm-lista">';
	$html .= '<li>Não vende equipamento nem intermedia venda.</li>';
	$html .= '<li>Não aceita link pago, publieditorial nem posição paga em ranking.</li>';
	$html .= '<li>Não usa preço como critério técnico. Sugestão de produto sai de campo medido — vazão, potência, volume atendido —, e o preço aparece depois, com loja e data.</li>';
	$html .= '<li>Quando houver link para loja, ele será de afiliado e virá declarado. Comissão não muda ordem de sugestão.</li>';
	$html .= '</ul></div>';

	$html .= '<p class="aqm-nota">Achou um número errado ou uma fonte melhor? A página de ' . aquametria_casca_link_html( 'metodologia', 'metodologia' ) . ' mostra o critério que usamos para aceitar ou recusar cada constante. Correção com fonte entra e muda a data de verificação.</p>';
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Estrutura do site: páginas, página inicial e limpeza do tema padrão
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_definicao_paginas' ) ) {
function aquametria_casca_definicao_paginas() {
	return array(
		'inicio'       => array( 'titulo' => 'Início', 'conteudo' => '[aquametria_home]' ),
		'calculadoras' => array( 'titulo' => 'Calculadoras', 'conteudo' => '[aquametria_calculadoras]' ),
		'metodologia'  => array( 'titulo' => 'Metodologia', 'conteudo' => '[aquametria_metodologia]' ),
		'sobre'        => array( 'titulo' => 'Sobre', 'conteudo' => '[aquametria_sobre]' ),
	);
}
}

if ( ! function_exists( 'aquametria_casca_garantir_paginas' ) ) {
function aquametria_casca_garantir_paginas( &$relato ) {
	$ids   = array();
	$criou = false;

	foreach ( aquametria_casca_definicao_paginas() as $slug => $def ) {
		$pagina = get_page_by_path( $slug, OBJECT, 'page' );

		if ( ! $pagina ) {
			$pid = wp_insert_post( array(
				'post_type'    => 'page',
				'post_title'   => $def['titulo'],
				'post_name'    => $slug,
				'post_content' => $def['conteudo'],
				'post_status'  => 'publish',
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $pid ) ) {
				$relato[] = 'página ' . $slug . ': erro — ' . $pid->get_error_message();
				continue;
			}
			update_post_meta( $pid, '_aquametria_casca', '1' );
			$ids[ $slug ] = (int) $pid;
			$criou        = true;
			$relato[]     = 'página ' . $slug . ': criada (#' . $pid . ')';
			continue;
		}

		$pid          = (int) $pagina->ID;
		$ids[ $slug ] = $pid;
		$nossa        = ( '1' === get_post_meta( $pid, '_aquametria_casca', true ) );

		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
			$relato[] = 'página ' . $slug . ': republicada (#' . $pid . ')';
		}
		// Só reescrevemos o corpo de página que é nossa e que perdeu o shortcode.
		if ( $nossa && false === strpos( (string) $pagina->post_content, $def['conteudo'] ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $def['conteudo'] ) );
			$relato[] = 'página ' . $slug . ': shortcode reposto (#' . $pid . ')';
		}
	}

	if ( $criou ) {
		flush_rewrite_rules( false );
	}

	return $ids;
}
}

if ( ! function_exists( 'aquametria_casca_fixar_home' ) ) {
function aquametria_casca_fixar_home( $ids, &$relato ) {
	if ( empty( $ids['inicio'] ) ) {
		return;
	}
	if ( 'page' !== get_option( 'show_on_front' ) ) {
		update_option( 'show_on_front', 'page' );
		$relato[] = 'show_on_front: page';
	}
	if ( (int) get_option( 'page_on_front' ) !== (int) $ids['inicio'] ) {
		update_option( 'page_on_front', (int) $ids['inicio'] );
		$relato[] = 'page_on_front: #' . (int) $ids['inicio'];
	}
}
}

if ( ! function_exists( 'aquametria_casca_limpar_padrao' ) ) {
function aquametria_casca_limpar_padrao( &$relato ) {
	if ( 'feito' === get_option( 'aquametria_casca_limpeza' ) ) {
		return;
	}

	$slugs = array( 'hello-world', 'ola-mundo', 'sample-page', 'pagina-exemplo', 'pagina-de-exemplo' );
	$titulos = array( 'Hello world!', 'Olá, mundo!', 'Ola, mundo!', 'Sample Page', 'Página de exemplo', 'Pagina de exemplo' );

	$candidatos = get_posts( array(
		'post_type'        => array( 'post', 'page' ),
		'post_status'      => array( 'publish', 'draft', 'pending', 'private', 'future' ),
		'numberposts'      => 40,
		'orderby'          => 'ID',
		'order'            => 'ASC',
		'suppress_filters' => true,
	) );

	foreach ( $candidatos as $p ) {
		if ( '1' === get_post_meta( $p->ID, '_aquametria_casca', true ) ) {
			continue;
		}
		$por_slug   = in_array( $p->post_name, $slugs, true );
		$por_titulo = in_array( trim( $p->post_title ), $titulos, true );
		if ( ! $por_slug && ! $por_titulo ) {
			continue;
		}
		if ( (int) get_option( 'page_on_front' ) === (int) $p->ID ) {
			continue;
		}
		wp_trash_post( $p->ID );
		$relato[] = 'lixeira: ' . $p->post_type . ' #' . $p->ID . ' (' . $p->post_name . ')';
	}

	update_option( 'aquametria_casca_limpeza', 'feito', false );
}
}

if ( ! function_exists( 'aquametria_casca_montar' ) ) {
function aquametria_casca_montar( $forcar = false ) {
	$feita = get_option( 'aquametria_casca_estrutura' );
	if ( ! $forcar && AQUAMETRIA_CASCA_VERSAO === $feita ) {
		return array();
	}

	$relato = array();
	$ids    = aquametria_casca_garantir_paginas( $relato );
	aquametria_casca_fixar_home( $ids, $relato );
	aquametria_casca_limpar_padrao( $relato );

	update_option( 'aquametria_casca_paginas', $ids, false );
	update_option( 'aquametria_casca_estrutura', AQUAMETRIA_CASCA_VERSAO, false );

	if ( ! $relato ) {
		$relato[] = 'nada a fazer: estrutura já estava de pé';
	}
	$relato[] = 'casca ' . AQUAMETRIA_CASCA_VERSAO . ' em ' . current_time( 'Y-m-d H:i' );
	update_option( 'aquametria_casca_relato', $relato, false );

	return $relato;
}
}

if ( ! function_exists( 'aquametria_casca_boot' ) ) {
function aquametria_casca_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;

	aquametria_casca_montar( false );

	// Remontagem manual: /?aquametria_casca=refazer (só para quem administra o site).
	$pedido = filter_input( INPUT_GET, 'aquametria_casca', FILTER_DEFAULT );
	if ( 'refazer' === $pedido && current_user_can( 'manage_options' ) ) {
		$relato = aquametria_casca_montar( true );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array( 'versao' => AQUAMETRIA_CASCA_VERSAO, 'relato' => $relato ), JSON_UNESCAPED_UNICODE );
		exit;
	}
}
}

add_action( 'init', 'aquametria_casca_boot', 20 );

if ( did_action( 'init' ) ) {
	aquametria_casca_boot();
}

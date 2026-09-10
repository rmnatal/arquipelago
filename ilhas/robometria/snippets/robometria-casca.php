/**
 * Robometria Casca — identidade e estrutura do site
 * Versão: 1.0.1 (10/09/2026) — despacho da Sentinela: o sitemap servia o XML
 * certo com status 404, porque esta ilha não tem nenhum post publicado e a
 * consulta principal das rotas de sitemap voltava vazia (seção 5b abaixo).
 * Versão 1.0.0 (10/09/2026) — primeira casca da ilha, Bloco 3b. Derivada da casca
 * da Aquametria 1.3.0 por substituição de identidade, não por cópia cega: a paleta,
 * a tipografia, o símbolo, o menu e as páginas são da Robometria, e o que sobrou
 * igual sobrou porque já era regra do Arquipélago (seção 6 do ARQUIPELAGO.md) —
 * menu sanfona com aria-expanded/aria-controls e links no HTML servido, favicon
 * próprio no lugar do ícone do WordPress, e nenhum <script> ou <style> dentro do
 * retorno de shortcode.
 *
 * Dá cara de Robometria ao tema ativo, sozinha, sem construtor de página e sem
 * plugin de tema. Faz oito coisas:
 *   (a) carrega Archivo, IBM Plex Sans e IBM Plex Mono e injeta a paleta no wp_head;
 *   (b) troca a saída de core/site-title e core/site-logo pelo logotipo em SVG
 *       (anel aberto + peça com lingueta que encaixa nele) mais o wordmark;
 *   (c) troca a saída de core/navigation pelo menu Ferramentas · Metodologia · Sobre;
 *   (d) cria, casando pelo slug, as páginas inicio, ferramentas, metodologia, sobre
 *       e divulgacao-de-afiliados, e fixa inicio como página inicial;
 *   (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (nunca apaga) — hoje é o
 *       que o sitemap desta ilha lista, e o sitemap é curadoria (seção 14.1);
 *   (f) substitui a template part 'footer' do tema pelo rodapé da Robometria, para
 *       não ficarem dois rodapés empilhados;
 *   (g) redireciona 301 os apelidos de endereço para a página canônica;
 *   (h) publica o ícone do site e o JSON-LD Organization + WebSite (seção 5.3).
 *
 * O conteúdo das cinco páginas mora em shortcodes deste snippet: atualizar o
 * snippet atualiza as páginas, sem tocar no editor do WordPress.
 *
 * A lista de ferramentas do hub está em robometria_casca_ferramentas() e passa pelo
 * filtro 'robometria_ferramentas' — cada ferramenta nova vira 'publicada' aqui (ou
 * se registra pelo filtro no próprio snippet dela).
 *
 * Idempotente: rodar duas vezes não duplica página, não repete lixeira e não
 * reescreve página editada à mão. flush_rewrite_rules() só quando cria página.
 *
 * Regras herdadas (fase 4b): não usa a superglobal de servidor; sem "<?php" no
 * topo (o Code Snippets põe); texto de tela acentuado em UTF-8; toda função de
 * nível superior dentro de if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'ROBOMETRIA_CASCA_VERSAO' ) ) {
	define( 'ROBOMETRIA_CASCA_VERSAO', '1.0.1' );
	define( 'ROBOMETRIA_CASCA_TAGLINE', 'Qual peça o fabricante declarou para o seu robô aspirador — com código, endereço e data' );
}

/* ---------------------------------------------------------------------------
 * 1. Catálogo de ferramentas (fonte do hub e da home)
 *
 * Os títulos são a pergunta que a pessoa digita, não o nome interno da
 * ferramenta (seção 14.5). "R1" e "R2" existem para a fila da Fundação; o
 * visitante nunca precisa saber deles, e por isso o código sai pequeno, acima do
 * título, em monoespaçada.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_ferramentas' ) ) {
function robometria_casca_ferramentas() {
	$lista = array(
		array(
			'codigo' => 'R1',
			'titulo' => 'Qual peça serve no meu robô aspirador',
			'slug'   => 'qual-peca-serve-no-meu-robo-aspirador',
			'resumo' => 'Filtro, escova lateral, mop e bateria por marca e modelo, com o código do fabricante, o endereço da declaração e a data. Quando o fabricante não declara, a resposta é "não localizamos" — nunca um palpite.',
			'estado' => 'em-construcao',
		),
		array(
			'codigo' => 'R2',
			'titulo' => 'Quantos Pa e quanto tempo o seu robô precisa',
			'slug'   => 'quantos-pa-o-robo-aspirador-precisa',
			'resumo' => 'Sucção em pascal por tipo de piso e por pelo de animal, e quantos ciclos a sua metragem exige a partir dos minutos que o fabricante declara. As faixas de Pa são recomendação editorial e saem com o nome de quem recomenda.',
			'estado' => 'em-construcao',
		),
	);

	$lista = apply_filters( 'robometria_ferramentas', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

/**
 * URL REAL da página, ou '' se ela não existe publicada no site.
 *
 * Duas vias, nesta ordem:
 *   1. o id do repositório, que o Sync grava em _robometria_id. É a identidade
 *      canônica e sobrevive ao WordPress ter mudado o slug por conflito — quando
 *      o slug pedido já está ocupado, wp_insert_post acrescenta "-2" em silêncio;
 *   2. o slug, para as páginas que não vieram do Sync.
 *
 * Devolve '' quando nenhuma via acha a página, e quem chama NÃO publica link.
 * Link do hub para página inexistente é 404 no ar — a Aquametria pagou esse
 * defeito em 08/09/2026 e a Robometria nasce com a trava.
 */
if ( ! function_exists( 'robometria_casca_url_se_existir' ) ) {
function robometria_casca_url_se_existir( $slug ) {
	$slug = sanitize_title( $slug );
	if ( '' === $slug ) {
		return '';
	}

	$achados = get_posts( array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'meta_key'    => '_robometria_id',
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
if ( ! function_exists( 'robometria_casca_link_html' ) ) {
function robometria_casca_link_html( $slug, $rotulo ) {
	$url = robometria_casca_url_se_existir( $slug );
	if ( '' === $url ) {
		return '<span class="rbm-sem-link">' . esc_html( $rotulo ) . '</span>';
	}
	return '<a href="' . esc_url( $url ) . '">' . esc_html( $rotulo ) . '</a>';
}
}

/* ---------------------------------------------------------------------------
 * 1b. Apelidos de endereço — o 404 que o visitante não deveria ver
 *
 * O endereço de uma ferramenta desta ilha é a pergunta inteira, e pergunta
 * inteira é justamente o que ninguém digita igual. Cada apelido plausível
 * redireciona 301 para a página canônica, e o 301 é o que faz o sinal de busca
 * ficar com o endereço canônico em vez de se espalhar.
 *
 * Trava: o redirecionamento SÓ acontece se a página de destino existir
 * publicada. Redirecionar para outro 404 é pior que o 404 original.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_apelidos' ) ) {
function robometria_casca_apelidos() {
	$mapa = array(
		/* R1 — peça compatível */
		'pecas-compativeis'                       => 'qual-peca-serve-no-meu-robo-aspirador',
		'peca-compativel'                         => 'qual-peca-serve-no-meu-robo-aspirador',
		'compatibilidade-de-pecas'                => 'qual-peca-serve-no-meu-robo-aspirador',
		'filtro-compativel-robo-aspirador'        => 'qual-peca-serve-no-meu-robo-aspirador',
		'qual-filtro-serve-no-meu-robo-aspirador' => 'qual-peca-serve-no-meu-robo-aspirador',
		'escova-lateral-compativel'               => 'qual-peca-serve-no-meu-robo-aspirador',
		'mop-compativel-robo-aspirador'           => 'qual-peca-serve-no-meu-robo-aspirador',
		'bateria-compativel-robo-aspirador'       => 'qual-peca-serve-no-meu-robo-aspirador',
		'localizador-de-peca'                     => 'qual-peca-serve-no-meu-robo-aspirador',
		/* R2 — sucção e autonomia */
		'quantos-pa'                              => 'quantos-pa-o-robo-aspirador-precisa',
		'quantos-pa-preciso'                      => 'quantos-pa-o-robo-aspirador-precisa',
		'quantos-pa-robo-aspirador'               => 'quantos-pa-o-robo-aspirador-precisa',
		'calculadora-de-pa'                       => 'quantos-pa-o-robo-aspirador-precisa',
		'calculadora-de-succao'                   => 'quantos-pa-o-robo-aspirador-precisa',
		'robo-aspirador-para-pelo-de-cachorro'    => 'quantos-pa-o-robo-aspirador-precisa',
		'robo-aspirador-para-quantos-m2'          => 'quantos-pa-o-robo-aspirador-precisa',
		'autonomia-robo-aspirador'                => 'quantos-pa-o-robo-aspirador-precisa',
		/* páginas da casca */
		'calculadoras'                            => 'ferramentas',
		'metodo'                                  => 'metodologia',
		'afiliados'                               => 'divulgacao-de-afiliados',
	);

	return apply_filters( 'robometria_apelidos_de_pagina', $mapa );
}
}

/**
 * Slug canônico de um caminho pedido, ou '' se ele não for apelido conhecido.
 * Isolada da requisição de propósito, para o teste poder exercitá-la sozinha.
 */
if ( ! function_exists( 'robometria_casca_apelido_para_slug' ) ) {
function robometria_casca_apelido_para_slug( $caminho ) {
	$caminho = trim( (string) $caminho );
	$caminho = trim( $caminho, '/' );
	if ( '' === $caminho || false !== strpos( $caminho, '/' ) ) {
		return '';
	}

	$caminho = sanitize_title( $caminho );
	$mapa    = robometria_casca_apelidos();

	return isset( $mapa[ $caminho ] ) ? $mapa[ $caminho ] : '';
}
}

/**
 * Caminho pedido nesta requisição, sem a superglobal de servidor (fase 4b: o
 * ModSecurity desta hospedagem mata a gravação do snippet em silêncio quando o
 * nome dela aparece escrito — inclusive dentro de comentário, que foi como o
 * ferramentas/teste-casca.php pegou esta linha antes de ela ir para o site).
 */
if ( ! function_exists( 'robometria_casca_caminho_pedido' ) ) {
function robometria_casca_caminho_pedido() {
	if ( isset( $GLOBALS['wp'] ) && is_object( $GLOBALS['wp'] ) && isset( $GLOBALS['wp']->request ) ) {
		return (string) $GLOBALS['wp']->request;
	}

	$atual = add_query_arg( array() );
	$atual = strtok( (string) $atual, '?' );

	return trim( (string) $atual, '/' );
}
}

if ( ! function_exists( 'robometria_casca_redirecionar_apelido' ) ) {
function robometria_casca_redirecionar_apelido() {
	if ( ! is_404() ) {
		return;
	}

	$destino = robometria_casca_apelido_para_slug( robometria_casca_caminho_pedido() );
	if ( '' === $destino ) {
		return;
	}

	$url = robometria_casca_url_se_existir( $destino );
	if ( '' === $url ) {
		return;
	}

	wp_safe_redirect( $url, 301 );
	exit;
}
}

add_action( 'template_redirect', 'robometria_casca_redirecionar_apelido' );

/* ---------------------------------------------------------------------------
 * 2. Marca, menu e rodapé
 *
 * O símbolo é o ENCAIXE, não o robô: anel aberto com corte de 50° à direita e uma
 * peça com lingueta entrando nesse corte. O assunto desta ilha é compatibilidade,
 * e desenhar o objeto (um robô visto de cima) diria "aspirador", que é o que todo
 * concorrente já diz. A geometria está no PROMPT.md da ilha e é a mesma do ícone.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_logo_svg' ) ) {
function robometria_casca_logo_svg() {
	$svg  = '<svg viewBox="0 0 48 48" width="30" height="30" role="img" aria-label="Robometria" focusable="false">';
	/* Anel aberto: raio 15 em torno de (24,24), com o corte de 50° à direita. */
	$svg .= '<path d="M37.59 17.66 A15 15 0 1 0 37.59 30.34" fill="none" stroke="#16191D" stroke-width="3" stroke-linecap="round"/>';
	/* A peça, com a lingueta entrando no corte. É o único vermelho da marca. */
	$svg .= '<path d="M41 16 h6 v16 h-6 v-4 h-3 v-8 h3 z" fill="#CC3311"/>';
	$svg .= '</svg>';

	return $svg;
}
}

if ( ! function_exists( 'robometria_casca_marca_html' ) ) {
function robometria_casca_marca_html() {
	static $ja_impressa = false;
	if ( $ja_impressa ) {
		return '';
	}
	$ja_impressa = true;

	/* ROBO em 700 e METRIA em 400, coladas, sem espaço — nunca no mesmo peso e
	   nunca separadas (identidade aprovada em 09/09/2026). */
	return '<a class="rbm-marca" href="' . esc_url( home_url( '/' ) ) . '" rel="home">'
		. robometria_casca_logo_svg()
		. '<span class="rbm-wordmark"><b>ROBO</b><i>METRIA</i></span>'
		. '</a>';
}
}

/**
 * O menu. Abaixo de 782 px ele vira sanfona atrás de um botão; acima, é a mesma
 * fileira de links de sempre.
 *
 * Três decisões, e nenhuma é enfeite:
 *
 *   1. Os links saem SEMPRE no HTML servido, dentro de <nav>. O botão não gera
 *      link nenhum: só mostra e esconde o que já está lá. É o que faz o menu
 *      continuar existindo para quem lê sem executar JavaScript — o crawler de
 *      IA, que é regra de primeira classe (seção 5), e o visitante cujo script
 *      não carregou.
 *   2. Quem esconde a lista no celular é o seletor [data-rbm-menu], e esse
 *      atributo quem põe é o JavaScript do rodapé. Sem JavaScript o atributo não
 *      existe, a regra não casa e o menu fica visível como lista. Esconder por
 *      padrão e contar com o script para revelar seria trocar um defeito por
 *      outro pior.
 *   3. O id é contado, porque o filtro render_block pode trocar mais de um bloco
 *      core/navigation na mesma página, e aria-controls apontando para um id
 *      repetido não controla coisa nenhuma.
 */
if ( ! function_exists( 'robometria_casca_nav_html' ) ) {
function robometria_casca_nav_html() {
	static $quantos = 0;
	$quantos++;
	$id = 'rbm-nav-lista' . ( $quantos > 1 ? '-' . $quantos : '' );

	$itens = array(
		'ferramentas' => 'Ferramentas',
		'metodologia' => 'Metodologia',
		'sobre'       => 'Sobre',
	);

	$html  = '<div class="rbm-nav-caixa">';
	$html .= '<button type="button" class="rbm-nav-botao" aria-expanded="false" aria-controls="' . esc_attr( $id ) . '">';
	$html .= '<span class="rbm-nav-tracos" aria-hidden="true"></span>';
	$html .= '<span class="rbm-nav-rotulo">Menu</span>';
	$html .= '</button>';
	$html .= '<nav class="rbm-nav" id="' . esc_attr( $id ) . '" aria-label="Navegação principal"><ul>';
	foreach ( $itens as $slug => $rotulo ) {
		$html .= '<li>' . robometria_casca_link_html( $slug, $rotulo ) . '</li>';
	}
	$html .= '</ul></nav>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'robometria_casca_rodape_impresso' ) ) {
/**
 * Marca e consulta se o rodapé da Robometria já saiu nesta requisição.
 * Evita rodapé duplicado quando o filtro render_block já trocou a template part.
 */
function robometria_casca_rodape_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'robometria_casca_rodape_html' ) ) {
function robometria_casca_rodape_html() {
	robometria_casca_rodape_impresso( true );

	$html  = '<footer class="rbm-rodape"><div class="rbm-rodape-interno">';
	$html .= '<p class="rbm-tagline">' . esc_html( ROBOMETRIA_CASCA_TAGLINE ) . '</p>';
	$html .= '<p>Compatibilidade aqui não se deduz: cada par peça × modelo carrega quem declarou, onde declarou e em que data foi verificado. Quando dois canais do mesmo fabricante discordam, a Robometria publica as duas declarações e vale o conjunto mais estreito — errar para o lado largo faz alguém comprar peça que não encaixa. Onde o fabricante não declara, a página diz isso com todas as letras.</p>';
	$html .= '<p>' . robometria_casca_link_html( 'metodologia', 'Metodologia' )
		. ' · ' . robometria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
		. ' · ' . robometria_casca_link_html( 'sobre', 'Sobre' )
		. ' · Robometria ' . esc_html( date_i18n( 'Y' ) ) . '</p>';
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
		return robometria_casca_marca_html();
	}
	if ( 'core/navigation' === $nome ) {
		return robometria_casca_nav_html();
	}
	// A tagline padrão do WordPress é resíduo do tema; a da Robometria está no rodapé.
	if ( 'core/site-tagline' === $nome ) {
		return '';
	}
	// Em tema de blocos o rodapé é uma template part renderizada DENTRO do fluxo do
	// conteúdo. Trocar a saída dela aqui é o que impede os dois rodapés empilhados.
	if ( 'core/template-part' === $nome ) {
		$parte = isset( $bloco['attrs']['slug'] ) ? $bloco['attrs']['slug'] : '';
		if ( 'footer' === $parte || 'rodape' === $parte ) {
			return robometria_casca_rodape_html();
		}
	}
	return $conteudo;
}, 10, 2 );

// Rede de segurança: se o tema NÃO usa template part de rodapé (ou o filtro não
// pegou), o rodapé sai aqui. Se já saiu no lugar da template part, não repete.
add_action( 'wp_footer', function () {
	if ( robometria_casca_rodape_impresso() ) {
		return;
	}

	echo robometria_casca_rodape_html(); // markup próprio, já escapado campo a campo
}, 20 );

/* ---------------------------------------------------------------------------
 * 2b. Ícone do site
 *
 * O WordPress imprime o ícone dele em wp_head na prioridade 99, e sem tirar
 * aquele de lá o site sairia com dois — a aba escolheria um, o iOS outro. Aqui o
 * ícone é o mesmo encaixe do logotipo, viajando dentro do snippet como data URI:
 * nada sobe para a biblioteca de mídia.
 *
 * O desenho não se edita à mão neste arquivo: ele é gerado por
 * ferramentas/gerar-favicon.php, entre os marcadores abaixo, pelo mesmo motivo
 * que o catálogo de produtos é gerado dentro da ferramenta — desenho mantido em
 * dois lugares diverge em silêncio.
 * ------------------------------------------------------------------------- */

/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */
if ( ! defined( 'ROBOMETRIA_CASCA_ICONE_SVG' ) ) {
	define( 'ROBOMETRIA_CASCA_ICONE_SVG', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#16191D"/><path d="M22.16 12.2 A9 9 0 1 0 22.16 19.8" fill="none" stroke="#F2F1EF" stroke-width="2.2" stroke-linecap="round"/><path d="M24 10 h4.6 v12 h-4.6 v-3 h-2.4 v-6 h2.4 z" fill="#CC3311"/></svg>' );
	define( 'ROBOMETRIA_CASCA_ICONE_PNG_180', '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' );
	define( 'ROBOMETRIA_CASCA_ICONE_PNG_32', 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAD1BMVEXv7+3LMhAUGBytLhLNzcvl1KFZAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAV0lEQVQoz2NQQgMMNBRQYEAVYAACJiQBBgaECANYPRNYFC4Ak2MyFBSCCEANhgkoYAhAzVcSFMQh4IAuwEBQBWFDMdyhhCmA7hcM32KEB2aIYYYplWMOAFdPOlam04yNAAAAAElFTkSuQmCC' );
}
/* FAVICON-FIM */

remove_action( 'wp_head', 'wp_site_icon', 99 );

add_action( 'wp_head', function () {
	if ( ! defined( 'ROBOMETRIA_CASCA_ICONE_SVG' ) || '' === ROBOMETRIA_CASCA_ICONE_SVG ) {
		return;
	}

	echo '<link rel="icon" type="image/svg+xml" href="' . esc_attr( 'data:image/svg+xml,' . rawurlencode( ROBOMETRIA_CASCA_ICONE_SVG ) ) . '">' . "\n";
	// Segunda linha para quem não desenha SVG na aba: o mesmo desenho em PNG de
	// 32 px. 'alternate icon' é o rel que o navegador só usa quando desiste do primeiro.
	echo '<link rel="alternate icon" type="image/png" sizes="32x32" href="' . esc_attr( 'data:image/png;base64,' . ROBOMETRIA_CASCA_ICONE_PNG_32 ) . '">' . "\n";
	// O iOS não aceita SVG neste rel, e aplica a própria máscara de canto — por
	// isso o PNG é quadrado, em sangria, sem arredondamento por baixo.
	echo '<link rel="apple-touch-icon" sizes="180x180" href="' . esc_attr( 'data:image/png;base64,' . ROBOMETRIA_CASCA_ICONE_PNG_180 ) . '">' . "\n";
	echo '<meta name="theme-color" content="#16191D">' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * 2c. JSON-LD de entidade (seção 5.3 e 5.6 do ARQUIPELAGO.md)
 *
 * Organization e WebSite em toda página. O que NÃO sai daqui é o sameAs: a
 * Robometria não tem perfil externo nenhum hoje, e sameAs apontando para perfil
 * inventado seria exatamente a fabricação que esta ilha existe para não fazer.
 * Ele entra no dia em que houver perfil de verdade.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$org = array(
		'@type'       => 'Organization',
		'@id'         => home_url( '/#organizacao' ),
		'name'        => 'Robometria',
		'url'         => home_url( '/' ),
		'description' => 'Banco de compatibilidade de peças de robô aspirador e dimensionamento de sucção e autonomia, com a fonte do fabricante e a data de verificação em cada número.',
		'knowsAbout'  => array( 'robô aspirador', 'filtro HEPA', 'escova lateral', 'mop', 'bateria', 'sucção em pascal', 'autonomia' ),
	);
	if ( defined( 'ROBOMETRIA_CASCA_ICONE_SVG' ) && '' !== ROBOMETRIA_CASCA_ICONE_SVG ) {
		$org['logo'] = 'data:image/svg+xml,' . rawurlencode( ROBOMETRIA_CASCA_ICONE_SVG );
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			$org,
			array(
				'@type'     => 'WebSite',
				'@id'       => home_url( '/#site' ),
				'name'      => 'Robometria',
				'url'       => home_url( '/' ),
				'inLanguage' => 'pt-BR',
				'publisher' => array( '@id' => home_url( '/#organizacao' ) ),
			),
		),
	);

	echo '<script type="application/ld+json" id="robometria-casca-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
}, 6 );

/* ---------------------------------------------------------------------------
 * 3. Tipografia e paleta por cima do tema ativo
 *
 * A cor varredura (#CC3311) é COR DE SINAL: um uso por tela. Na casca esse uso é
 * a peça do logotipo. Por isso link não é vermelho — link é grafite sublinhado, e
 * o vermelho aparece só no estado de foco e de passagem do ponteiro, que são
 * momentâneos e não disputam a tela com a marca. Ressalva técnica é âmbar
 * (#A26A00), nunca vermelho, porque vermelho é a marca.
 *
 * Mono em todo número, unidade e código de peça, com tabular-nums. Texto corrido
 * NUNCA vai em Mono — é a razão de a citação em bloco desta ilha ficar no tipo de
 * texto, ao contrário da casca da Aquametria, onde ela é monoespaçada.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$fontes = 'https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap';

	echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
	echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
	echo '<link rel="stylesheet" href="' . esc_url( $fontes ) . '">' . "\n";

	$css = <<<'CSS'
:root{
--rbm-tinta:#16191D;--rbm-varredura:#CC3311;--rbm-piso:#F2F1EF;--rbm-superficie:#FFFFFF;
--rbm-traco:#DFDCD6;--rbm-legenda:#6B6862;--rbm-alerta:#A26A00;
--rbm-display:"Archivo","Helvetica Neue",Arial,sans-serif;
--rbm-texto:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--rbm-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
body{
--wp--preset--color--base:#F2F1EF;--wp--preset--color--contrast:#16191D;
--wp--preset--color--primary:#16191D;--wp--preset--color--secondary:#6B6862;
--wp--preset--font-family--body:var(--rbm-texto);
--wp--preset--font-family--heading:var(--rbm-display);
}
html body{background-color:var(--rbm-piso);color:var(--rbm-tinta);font-family:var(--rbm-texto);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;}
body h1,body h2,body h3,body h4,body h5,body h6{font-family:var(--rbm-display);color:var(--rbm-tinta);line-height:1.2;letter-spacing:-0.015em;}
body h1{font-weight:700;}
body a{color:var(--rbm-tinta);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;}
body a:hover{color:var(--rbm-varredura);}
body code,body kbd,body samp,body pre,body .rbm-num,body .rbm-codigo-peca{font-family:var(--rbm-mono);font-variant-numeric:tabular-nums;}
body .wp-block-button__link,body button,body input[type=submit]{background-color:var(--rbm-tinta);color:var(--rbm-superficie);border:0;border-radius:2px;font-family:var(--rbm-texto);font-weight:600;}
body hr,body .wp-block-separator{border-color:var(--rbm-traco);color:var(--rbm-traco);}
body table{border-collapse:collapse;}
body table th,body table td{border:1px solid var(--rbm-traco);padding:.5rem .7rem;text-align:left;}
body table th{background:var(--rbm-superficie);font-family:var(--rbm-display);font-weight:600;}
body header .wp-block-group,body .wp-block-template-part header{background:var(--rbm-superficie);}
.rbm-marca{display:inline-flex;align-items:center;gap:.55rem;text-decoration:none;}
.rbm-marca:hover{text-decoration:none;}
.rbm-marca svg{display:block;flex:0 0 auto;}
.rbm-wordmark{font-family:var(--rbm-display);font-size:1.45rem;letter-spacing:-0.02em;color:var(--rbm-tinta);line-height:1;}
.rbm-wordmark b{font-weight:700;}
.rbm-wordmark i{font-weight:400;font-style:normal;}
.rbm-nav ul{display:flex;flex-wrap:wrap;gap:1.4rem;list-style:none;margin:0;padding:0;}
.rbm-nav li{margin:0;}
.rbm-nav a{font-family:var(--rbm-texto);font-weight:600;font-size:.95rem;color:var(--rbm-tinta);text-decoration:none;padding-bottom:.15rem;border-bottom:1px solid transparent;}
.rbm-nav a:hover{color:var(--rbm-varredura);border-bottom-color:var(--rbm-varredura);}
.rbm-nav-caixa{position:relative;}
/* O botao do menu so aparece no celular, e so quando ha JavaScript para ele
   comandar (o atributo data-rbm-menu e posto pelo script do rodape). */
.rbm-nav-botao{display:none;align-items:center;gap:.55rem;background:transparent;color:var(--rbm-tinta);border:1px solid var(--rbm-traco);border-radius:2px;padding:.5rem .75rem;font-family:var(--rbm-texto);font-weight:600;font-size:.92rem;line-height:1;cursor:pointer;}
.rbm-nav-botao:hover{border-color:var(--rbm-varredura);color:var(--rbm-varredura);}
.rbm-nav-tracos{position:relative;display:block;width:1.05rem;height:2px;background:currentColor;border-radius:2px;}
.rbm-nav-tracos::before,.rbm-nav-tracos::after{content:"";position:absolute;left:0;width:100%;height:2px;background:currentColor;border-radius:2px;}
.rbm-nav-tracos::before{top:-.36rem;}
.rbm-nav-tracos::after{top:.36rem;}
.rbm-nav-botao:focus-visible,.rbm-nav a:focus-visible,.rbm-marca:focus-visible,body a:focus-visible{outline:2px solid var(--rbm-varredura);outline-offset:3px;}
.rbm-bloco{max-width:52rem;}
.rbm-linha-mestra{font-family:var(--rbm-display);font-size:1.35rem;line-height:1.35;font-weight:600;margin:0 0 .8rem;}
.rbm-abertura p{margin:0 0 .7rem;}
.rbm-secao{margin:2.4rem 0 0;}
.rbm-secao h2{margin:0 0 .6rem;font-size:1.3rem;}
.rbm-secao h3{margin:1.4rem 0 .4rem;font-size:1.05rem;}
.rbm-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(19rem,1fr));gap:1rem;margin:1.4rem 0 0;padding:0;list-style:none;}
.rbm-card{background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.5rem;margin:0;}
.rbm-card h3{font-family:var(--rbm-display);font-size:1.05rem;margin:0;line-height:1.25;}
.rbm-card p{margin:0;color:var(--rbm-legenda);font-size:.93rem;line-height:1.5;}
.rbm-codigo{font-family:var(--rbm-mono);font-size:.72rem;letter-spacing:.1em;color:var(--rbm-legenda);}
.rbm-acao{margin-top:auto;padding-top:.3rem;}
.rbm-acao a{font-weight:600;text-decoration:none;border-bottom:2px solid var(--rbm-tinta);}
.rbm-sem-link{color:var(--rbm-legenda);}
.rbm-rodape .rbm-sem-link{color:var(--rbm-traco);}
/* Ressalva tecnica em ambar. Nunca vermelho: vermelho e a marca. */
.rbm-tag{display:inline-block;font-family:var(--rbm-mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--rbm-alerta);border:1px solid var(--rbm-alerta);border-radius:2px;padding:.15rem .4rem;}
.rbm-nota{border-left:3px solid var(--rbm-tinta);background:var(--rbm-superficie);padding:.85rem 1rem;color:var(--rbm-legenda);font-size:.95rem;margin:1.2rem 0 0;}
.rbm-nota strong{color:var(--rbm-tinta);}
.rbm-lista{margin:.6rem 0 0;padding-left:1.1rem;}
.rbm-lista li{margin:0 0 .45rem;}
/* Citacao em bloco vinda do Markdown do repositorio (conversor do Sync 1.1.2).
   Fica no tipo de TEXTO, nao em monoespaçada: aqui o que e citado e a frase do
   fabricante, e texto corrido em Mono contraria a identidade desta ilha. */
.rbm-citacao{border-left:3px solid var(--rbm-traco);background:var(--rbm-superficie);margin:1.2rem 0;padding:.9rem 1.1rem;font-size:.95rem;line-height:1.6;}
.rbm-citacao p{margin:0 0 .5rem;}
.rbm-citacao p:last-child{margin-bottom:0;}
.rbm-tabela{margin:1.2rem 0;overflow-x:auto;}
.rbm-quadro{width:100%;margin:1rem 0 0;font-size:.93rem;}
.rbm-quadro td:first-child,.rbm-quadro th:first-child{white-space:nowrap;}
.rbm-quadro .rbm-n{text-align:right;font-family:var(--rbm-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.rbm-rodape{background:var(--rbm-tinta);color:var(--rbm-piso);padding:2.4rem 1.5rem;margin-top:3.5rem;font-family:var(--rbm-texto);}
.rbm-rodape-interno{max-width:52rem;margin:0 auto;display:flex;flex-direction:column;gap:.7rem;}
.rbm-rodape .rbm-tagline{font-family:var(--rbm-display);font-weight:600;font-size:1.1rem;color:var(--rbm-superficie);margin:0;}
.rbm-rodape p{margin:0;font-size:.86rem;line-height:1.55;color:var(--rbm-traco);}
.rbm-rodape a{color:var(--rbm-piso);}
/* Cinto de seguranca do rodape: o caminho principal e o filtro render_block, que
   troca a template part 'footer' do tema pela da Robometria. Se ele nao pegar, o
   rodape do tema fica visivel acima do nosso — as regras abaixo escondem o
   credito do tema e a template part de rodape que nao seja a nossa. */
.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}
body:has(.rbm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.rbm-rodape)){display:none;}
@media (max-width:600px){
.rbm-linha-mestra{font-size:1.15rem;}
.rbm-wordmark{font-size:1.2rem;}
}
/* Menu sanfona. 782 px e a largura em que o proprio WordPress considera que a
   tela virou celular; seguir a mesma quebra evita cabecalho meio empilhado.
   Tudo aqui depende de [data-rbm-menu]: sem JavaScript nada disso vale e o menu
   continua sendo a fileira de links, visivel. */
@media (max-width:782px){
.rbm-nav-caixa[data-rbm-menu] .rbm-nav-botao{display:inline-flex;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav{display:none;position:absolute;right:0;top:calc(100% + .55rem);z-index:60;min-width:13rem;background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;box-shadow:0 12px 32px rgba(22,25,29,.16);padding:.35rem 0;}
.rbm-nav-caixa[data-rbm-menu][data-rbm-aberto="1"] .rbm-nav{display:block;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav ul,.rbm-nav-caixa[data-rbm-menu] .rbm-nav li{display:block;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav a,.rbm-nav-caixa[data-rbm-menu] .rbm-nav .rbm-sem-link{display:block;padding:.65rem 1.05rem;font-size:1rem;border-bottom:0;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav a:hover{background:var(--rbm-piso);color:var(--rbm-varredura);}
}
CSS;

	echo '<style id="robometria-casca">' . $css . '</style>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * 3b. O comando do menu sanfona
 *
 * O script sai no wp_footer, NUNCA dentro do retorno de um shortcode. É a regra
 * da seção 8 do ARQUIPELAGO.md, nascida do defeito de 08/09/2026 na Aquametria:
 * o WordPress roda os filtros de texto do conteúdo sobre o que o shortcode
 * devolve, cada E-comercial vira entidade numérica e o JavaScript inteiro morre
 * com erro de sintaxe. Aqui ele não passa por filtro nenhum.
 *
 * O script não desenha menu: só assume o comando do que o PHP já serviu. A
 * primeira coisa que faz é pôr data-rbm-menu na caixa, e é esse atributo que liga
 * as regras de CSS do celular — ou seja, o menu só se fecha depois que existe
 * alguém para reabri-lo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	$js = <<<'JS'
(function () {
	var caixas = document.querySelectorAll('.rbm-nav-caixa');
	if (!caixas.length) { return; }

	Array.prototype.forEach.call(caixas, function (caixa) {
		var botao = caixa.querySelector('.rbm-nav-botao');
		var lista = caixa.querySelector('.rbm-nav');
		if (!botao || !lista) { return; }

		/* A partir daqui o CSS do celular vale: ha quem reabra o menu. */
		caixa.setAttribute('data-rbm-menu', '1');

		function aberto() {
			return caixa.getAttribute('data-rbm-aberto') === '1';
		}
		function estado(abrir) {
			caixa.setAttribute('data-rbm-aberto', abrir ? '1' : '0');
			botao.setAttribute('aria-expanded', abrir ? 'true' : 'false');
		}
		estado(false);

		botao.addEventListener('click', function (ev) {
			ev.preventDefault();
			estado(!aberto());
		});

		/* Escape fecha e devolve o foco ao botao: quem abriu pelo teclado nao
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
		   volta a ser fileira de links e nao pode continuar marcado como aberto,
		   senao o aria-expanded mente para o leitor de tela. */
		window.addEventListener('resize', function () {
			if (aberto() && window.innerWidth > 782) { estado(false); }
		});
	});
})();
JS;

	echo '<script id="robometria-casca-menu">' . $js . '</script>' . "\n";
}, 25 );

/* ---------------------------------------------------------------------------
 * 4. Conteúdo das páginas (shortcodes)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_cards_html' ) ) {
function robometria_casca_cards_html() {
	$html = '<ul class="rbm-cards">';
	foreach ( robometria_casca_ferramentas() as $f ) {
		$publicada = ( isset( $f['estado'] ) && 'publicada' === $f['estado'] );
		$html     .= '<li class="rbm-card">';
		$html     .= '<span class="rbm-codigo">' . esc_html( $f['codigo'] ) . '</span>';
		$html     .= '<h3>' . esc_html( $f['titulo'] ) . '</h3>';
		$html     .= '<p>' . esc_html( $f['resumo'] ) . '</p>';
		$html     .= '<span class="rbm-acao">';
		$url = $publicada ? robometria_casca_url_se_existir( $f['slug'] ) : '';
		if ( '' !== $url ) {
			$html .= '<a href="' . esc_url( $url ) . '">Abrir ferramenta</a>';
		} else {
			/* A ferramenta pode ter se anunciado publicada e a página ainda não
			   existir (Sync atrasado, slug tomado por outra página). Melhor o selo
			   honesto que um link que devolve 404. */
			$html .= '<span class="rbm-tag">Em construção</span>';
		}
		$html .= '</span></li>';
	}
	$html .= '</ul>';

	return $html;
}
}

/**
 * Números do banco desta ilha, para a tela.
 *
 * Ordem das vias, e ela importa: primeiro o banco publicado nas options pelo Sync
 * (número vivo), depois o instantâneo medido em 10/09/2026 por
 * ferramentas/cobertura-r1.py e ferramentas/validar-banco.py. O instantâneo está
 * aqui porque hoje os itens de dados do manifest estão com publicar=false — são
 * pesquisa, não página — e uma página que promete número não pode ficar em branco
 * esperando. No dia em que o banco virar dado publicado, a via viva assume sozinha.
 */
if ( ! function_exists( 'robometria_casca_numeros' ) ) {
function robometria_casca_numeros() {
	$n = array(
		'medido_em'            => '2026-09-10',
		'marcas'               => 5,
		'modelos_publicaveis'  => 28,
		'pecas_publicaveis'    => 16,
		'pares_declarados'     => 33,
		'r1_responde'          => 15,
		'r1_vazia'             => 12,
		'celulas'              => 168,
		'celulas_sem_resposta' => 116,
		'as_duas'              => 3,
		'esperando_link'       => 44,
	);

	/* A data NÃO vem do arquivo de cobertura: o gerado_em dele é herdado do banco
	   (a data em que as peças foram colhidas), não a data da varredura. Publicar
	   um pelo outro seria dar ao leitor uma data que não é a do número. */
	$cob = get_option( 'robometria_dados_cobertura-r1' );
	if ( is_array( $cob ) && isset( $cob['resumo'] ) && is_array( $cob['resumo'] ) ) {
		$r = $cob['resumo'];
		foreach ( array(
			'modelos_publicaveis' => 'modelos_publicaveis',
			'r1_responde'         => 'modelos_que_respondem',
			'r1_vazia'            => 'modelos_com_entrada_vazia',
			'celulas'             => 'celulas_total',
		) as $destino => $origem ) {
			if ( isset( $r[ $origem ] ) ) {
				$n[ $destino ] = (int) $r[ $origem ];
			}
		}
		if ( isset( $r['celulas']['vazia'] ) ) {
			$n['celulas_sem_resposta'] = (int) $r['celulas']['vazia'];
		}
	}

	return apply_filters( 'robometria_numeros', $n );
}
}

if ( ! function_exists( 'robometria_casca_data_br' ) ) {
/** Data na tela sai como o leitor brasileiro escreve; ISO fica no repositório. */
function robometria_casca_data_br( $iso ) {
	$partes = explode( '-', (string) $iso );
	if ( 3 !== count( $partes ) ) {
		return (string) $iso;
	}
	return $partes[2] . '/' . $partes[1] . '/' . $partes[0];
}
}

if ( ! function_exists( 'robometria_casca_num' ) ) {
/** Número na tela sai sempre em monoespaçada com tabular-nums (identidade da ilha). */
function robometria_casca_num( $valor ) {
	return '<span class="rbm-num">' . esc_html( number_format_i18n( (float) $valor ) ) . '</span>';
}
}

add_shortcode( 'robometria_home', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<div class="rbm-abertura">';
	/* Resposta antes da explicação (seção 5.2): a primeira frase é
	   autossuficiente e sobrevive a ser citada fora de contexto. */
	$html .= '<p class="rbm-linha-mestra">A Robometria diz qual filtro, escova, mop ou bateria o <strong>fabricante</strong> declarou para o seu robô aspirador — com o código da peça, o endereço da declaração e a data em que ela foi verificada.</p>';
	$html .= '<p>Hoje são ' . robometria_casca_num( $n['pares_declarados'] ) . ' pares peça × modelo no banco, em ' . robometria_casca_num( $n['marcas'] ) . ' marcas, <strong>todos declarados pelo fabricante e nenhum inferido</strong>. Quando dois canais do mesmo fabricante discordam sobre quais modelos uma peça atende, a Robometria publica as duas declarações e vale o conjunto mais estreito.</p>';
	$html .= '<p>Não completamos lista por analogia. Um modelo estar na lista de compatibilidade de uma peça não o coloca na lista da peça seguinte — e isso não é cautela nossa, é o que o catálogo dos fabricantes mostra.</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Ferramentas</h2>';
	$html .= '<p>Duas ferramentas, especificadas ponta a ponta, entrando no ar uma por vez.</p>';
	$html .= robometria_casca_cards_html();
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Onde a Robometria ainda não sabe responder</h2>';
	$html .= '<p>Varremos a entrada da ferramenta de peças de ponta a ponta em ' . esc_html( robometria_casca_data_br( $n['medido_em'] ) ) . ': ela responde alguma coisa em ' . robometria_casca_num( $n['r1_responde'] ) . ' dos ' . robometria_casca_num( $n['modelos_publicaveis'] ) . ' modelos do banco e sai vazia em ' . robometria_casca_num( $n['r1_vazia'] ) . '. Das ' . robometria_casca_num( $n['celulas'] ) . ' combinações de modelo e tipo de peça, ' . robometria_casca_num( $n['celulas_sem_resposta'] ) . ' não têm declaração de fabricante que a gente tenha localizado.</p>';
	$html .= '<p class="rbm-nota"><strong>Publicar esse número é parte do método.</strong> Um comparador que nunca diz "não sei" está inventando em algum lugar. A varredura roda de novo a cada leva de coleta, e é ela — não a impressão de quem colhe — que decide o que a ilha vai procurar em seguida.</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Como decidimos o que publicar</h2>';
	$html .= '<p>Toda especificação carrega o nível da fonte que a sustenta: manual lido direto vale mais que página oficial colhida por busca, que vale mais que loja da marca, que vale mais que anúncio de marketplace. Anúncio de marketplace nunca sustenta a palavra "serve".</p>';
	$html .= '<p>' . robometria_casca_link_html( 'metodologia', 'Ler a metodologia completa' ) . '</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'robometria_ferramentas', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">Duas ferramentas: uma responde qual peça serve, a outra responde quanta sucção e quanto tempo a sua casa pede.</p>';
	$html .= '<p>Elas são diferentes de propósito. A de peças tem resposta binária — o fabricante declarou aquele código para aquele modelo, ou não declarou. A de sucção devolve <strong>faixa</strong>, porque quem publica limiar de pascal para casa com pet é veículo editorial, não fabricante, e os veículos discordam entre si.</p>';
	$html .= robometria_casca_cards_html();

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Por que as duas ainda não cobrem os mesmos robôs</h2>';
	$html .= '<p>Só ' . robometria_casca_num( $n['as_duas'] ) . ' dos ' . robometria_casca_num( $n['modelos_publicaveis'] ) . ' modelos do banco são atendidos pelas duas ferramentas ao mesmo tempo, e a causa é do mercado, não da ilha: Electrolux e Multi publicam peça com compatibilidade declarada e <strong>não publicam sucção em pascal</strong>; Xiaomi e WAP publicam pascal e <strong>não publicam código de peça</strong>. Enquanto for assim, um robô costuma ter resposta numa ferramenta e recusa na outra, e a tela diz qual é o caso.</p>';
	$html .= '</div>';

	$html .= '<p class="rbm-nota"><strong>Em construção não é enfeite.</strong> Uma ferramenta só entra no ar com a fonte de cada declaração conferida, com a tabela de exemplos servida no próprio HTML e com a recusa escrita para os casos em que o fabricante não declarou nada. Preferimos uma ferramenta que se recusa a responder a duas que chutam.</p>';
	$html .= '</div>';

	return $html;
} );

/**
 * A escada de fontes, para a tela. Mesma ordem das vias dos números: banco
 * publicado primeiro, instantâneo do esquema depois. O campo "hoje" não é
 * decoração — é a confissão de que a ilha inteira está apoiada nos níveis 3 e 4.
 */
if ( ! function_exists( 'robometria_casca_escada_de_fontes' ) ) {
function robometria_casca_escada_de_fontes() {
	$escada = array(
		array( 'nivel' => 1, 'origem' => 'medição própria', 'sustenta' => 'Desempenho real: sucção medida, autonomia medida, área coberta medida. É a única origem que poderia publicar desempenho.', 'existe' => false ),
		array( 'nivel' => 2, 'origem' => 'manual do fabricante', 'sustenta' => 'Qualquer campo técnico declarado, e vida útil de peça. Exige manual, lâmina ou página oficial LIDA direto.', 'existe' => false ),
		array( 'nivel' => 3, 'origem' => 'fabricante por busca', 'sustenta' => 'Campo técnico atribuído ao fabricante, colhido por busca restrita ao domínio dele, sem a leitura da página. Vai para a tela com "a confirmar no manual".', 'existe' => true ),
		array( 'nivel' => 4, 'origem' => 'varejo oficial da marca', 'sustenta' => 'Campo técnico transcrito pela loja oficial da própria marca no Brasil. Vai para a tela com "confira a embalagem".', 'existe' => true ),
		array( 'nivel' => 5, 'origem' => 'varejo especializado', 'sustenta' => 'Campo técnico transcrito por varejista ou assistência especializada.', 'existe' => false ),
		array( 'nivel' => 6, 'origem' => 'anúncio de marketplace', 'sustenta' => 'APENAS a existência do item, e sempre rotulado como declaração de terceiro. Nunca sustenta especificação nem a palavra "serve".', 'existe' => true ),
		array( 'nivel' => 7, 'origem' => 'editorial', 'sustenta' => 'Recomendação de faixa (quanto pascal uma casa precisa), sempre com o nome de quem publica. Nunca sustenta especificação de aparelho.', 'existe' => true ),
	);

	return apply_filters( 'robometria_escada_de_fontes', $escada );
}
}

add_shortcode( 'robometria_metodologia', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">A Robometria não escreve que uma peça "serve" sem uma declaração do fabricante com endereço e data — e quando não tem, diz que não tem.</p>';
	$html .= '<p>A primeira página de busca para "qual filtro serve no robô X" hoje é, quase inteira, título de anúncio: quem afirma a compatibilidade é o vendedor da peça, sem fonte e sem data. Este site existe para ocupar exatamente esse vazio, e o método abaixo é o que torna isso verificável em vez de prometido.</p>';

	$html .= '<div class="rbm-secao"><h2>1. Compatibilidade se declara, não se deduz — e cada afirmação tem selo</h2>';
	$html .= '<p>Todo par peça × modelo sai da ferramenta com um de três selos, e o selo aparece na frase, não numa legenda de rodapé:</p>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li><strong>Declarada pelo fabricante</strong> — está na página oficial da peça ou no manual. <em>Só este nível pode ser escrito como "serve".</em></li>';
	$html .= '<li><strong>Declarada por terceiro</strong> — quem afirma é lojista ou anunciante. Aparece em seção separada, abaixo, rotulada; nunca misturada com a anterior e nunca em primeiro lugar.</li>';
	$html .= '<li><strong>Não declarada</strong> — não localizamos e paramos ali. A tela diz, com estas palavras: não localizamos declaração do fabricante para esta peça neste modelo, e não vamos supor.</li>';
	$html .= '</ul>';
	$html .= '<p>Compatibilidade também não se herda. No catálogo de um mesmo fabricante, um modelo aparece na lista da escova rotativa central e <strong>não</strong> aparece na do filtro nem na do kit da mesma família. Completar a lista por analogia teria produzido uma recomendação errada — e é por isso que a regra é essa.</p></div>';

	$html .= '<div class="rbm-secao"><h2>2. Quando as fontes discordam, vale o conjunto mais estreito</h2>';
	$html .= '<p>Duas fontes boas discordando é rotina. A saída proibida é a média, porque ela esconde justamente o desacordo que faz a informação valer. A Robometria publica as duas declarações com as duas datas e resolve para o lado em que <strong>errar dói menos</strong> — e aqui esse lado é sempre o mais estreito, porque errar para o lado largo faz alguém comprar uma peça que não encaixa.</p>';
	$html .= '<p>Dois casos reais do nosso banco:</p>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li>Um mesmo código de filtro é anunciado por dois canais do mesmo fabricante com listas de modelos diferentes. Vale a lista menor; a outra fica registrada como divergência, visível na página.</li>';
	$html .= '<li>Um modelo de robô é declarado com <span class="rbm-num">1600</span> Pa na ficha técnica e <span class="rbm-num">2000</span> Pa no texto de venda da <strong>mesma página</strong>. Vale 1600: publicar 2000 faria alguém comprar, por recomendação nossa, um robô mais fraco do que esperava.</li>';
	$html .= '</ul>';
	$html .= '<p>A mesma regra vale para faixa e tolerância declaradas. Quando o fabricante escreve "de 5 a 6 horas" ou "130 minutos ±10 %", guardamos a faixa inteira e resolvemos por campo: sucção e autonomia para baixo, tempo de recarga para cima.</p></div>';

	$html .= '<div class="rbm-secao"><h2>3. Toda origem tem nível, e o nosso está escrito aqui</h2>';
	$html .= '<p>Em conflito, o nível mais alto vence e o outro fica registrado. Dentro do mesmo nível ninguém vence: o campo vira conflito declarado.</p>';
	$html .= '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr><th>Nível</th><th>Origem</th><th>O que pode sustentar</th><th>Temos hoje</th></tr></thead><tbody>';
	foreach ( robometria_casca_escada_de_fontes() as $degrau ) {
		$html .= '<tr>';
		$html .= '<td class="rbm-n">' . esc_html( $degrau['nivel'] ) . '</td>';
		$html .= '<td>' . esc_html( $degrau['origem'] ) . '</td>';
		$html .= '<td>' . esc_html( $degrau['sustenta'] ) . '</td>';
		$html .= '<td>' . ( $degrau['existe'] ? 'sim' : '—' ) . '</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="rbm-nota"><strong>A confissão que essa tabela obriga:</strong> a Robometria não tem nenhuma fonte de nível 1 nem de nível 2 ainda. O banco inteiro está apoiado nos níveis 3 e 4 — página do fabricante colhida por busca e loja oficial da marca — e é por isso que cada campo carrega o canal por onde foi colhido. Ler os manuais em PDF direto é o próximo degrau, e ele está na fila.</p></div>';

	$html .= '<div class="rbm-secao"><h2>4. O que medimos sobre a nossa própria cobertura</h2>';
	$html .= '<p>Contar itens do banco não diz se a ferramenta responde. Por isso a entrada é varrida de ponta a ponta, e o resultado é publicado mesmo quando é desconfortável (medição de ' . esc_html( robometria_casca_data_br( $n['medido_em'] ) ) . '):</p>';
	$html .= '<div class="rbm-tabela"><table class="rbm-quadro"><tbody>';
	$html .= '<tr><td>Marcas no banco</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['marcas'] ) ) . '</td></tr>';
	$html .= '<tr><td>Modelos de robô publicáveis</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['modelos_publicaveis'] ) ) . '</td></tr>';
	$html .= '<tr><td>Peças publicáveis</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['pecas_publicaveis'] ) ) . '</td></tr>';
	$html .= '<tr><td>Pares peça × modelo, todos declarados</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['pares_declarados'] ) ) . '</td></tr>';
	$html .= '<tr><td>Modelos em que a ferramenta de peças responde</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['r1_responde'] ) ) . '</td></tr>';
	$html .= '<tr><td>Modelos em que ela sai vazia</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['r1_vazia'] ) ) . '</td></tr>';
	$html .= '<tr><td>Combinações modelo × tipo de peça sem declaração localizada</td><td class="rbm-n">' . esc_html( number_format_i18n( $n['celulas_sem_resposta'] ) ) . ' de ' . esc_html( number_format_i18n( $n['celulas'] ) ) . '</td></tr>';
	$html .= '</tbody></table></div>';
	$html .= '<p>Um efeito dessa varredura já mudou a interface: o tipo "reservatório" não tem <strong>nenhuma</strong> peça declarada no banco inteiro, então ele sai do seletor da ferramenta. Oferecer uma escolha que sempre devolve recusa é prometer o que não se entrega; o tipo volta no dia em que a primeira peça dele entrar.</p></div>';

	$html .= '<div class="rbm-secao"><h2>5. O que a Robometria não publica, e por quê</h2>';
	$html .= '<p>Esta lista é parte do método, não uma desculpa. Cada item volta no dia em que a fonte aparecer.</p>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li><strong>Área coberta em metros quadrados para a maioria das marcas.</strong> Varremos modelo a modelo: só uma das cinco marcas do banco declara metragem; as outras declaram apenas minutos por carga. Quando um site promete "atende até 120 m²" para um robô cujo fabricante só declarou minutos, esse número foi escolhido por alguém.</li>';
	$html .= '<li><strong>Uma taxa geral de metros quadrados por minuto.</strong> Os dois únicos pares (minutos, m²) declarados que temos são da mesma marca e discordam entre si em <span class="rbm-num">23</span> %. Uma taxa média deles seria um número que nenhum fabricante defende.</li>';
	$html .= '<li><strong>Sucção convertida a partir de potência.</strong> Um modelo declara watts e nenhum pascal. Watt não é pascal e não existe conversão: o campo fica vazio, com o motivo escrito.</li>';
	$html .= '<li><strong>Vida útil de peça emprestada de outro fabricante.</strong> O único prazo de fabricante que temos vale para os modelos daquele manual, e só para eles.</li>';
	$html .= '<li><strong>Especificação vinda de veículo editorial.</strong> Publicações citam números de sucção para linhas inteiras; pela escada acima, editorial nunca sustenta especificação de aparelho. Editorial sustenta recomendação de faixa, e aí aparece com o nome de quem recomenda.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="rbm-secao"><h2>6. Correção</h2>';
	$html .= '<p>Quando aparece fonte melhor, o campo é substituído e a data de verificação da página muda junto. Correção não é vergonha: é para isso que a data serve. Achou uma declaração de fabricante que contradiz o que está aqui? Ela vale mais que a nossa, e entra.</p></div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'robometria_sobre', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">A Robometria é um banco de compatibilidade de peças de robô aspirador, não um site de "melhores do ano".</p>';
	$html .= '<p>Publicamos duas coisas: qual peça o fabricante declarou para qual modelo, e quanta sucção e quanto tempo a sua casa pede. Com uma regra única — todo número cita a fonte e leva a data em que foi verificado.</p>';

	$html .= '<div class="rbm-secao"><h2>Por que existe</h2>';
	$html .= '<p>A busca comercial do nicho ("melhor robô aspirador") está tomada por listas de compra, e nós não disputamos essa. A busca que ninguém responde direito é a de quem <strong>já tem</strong> o robô: qual filtro serve, qual escova lateral encaixa, qual bateria é a certa. Hoje quem responde isso é o título do anúncio de quem vende a peça. Não existe comparador entre marcas com fonte e data — e é esse buraco que este site ocupa.</p></div>';

	$html .= '<div class="rbm-secao"><h2>Como é feita</h2>';
	$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é o método e a procedência do dado, e os dois ficam abertos para conferência em cada página. Ferramentas e conteúdo são versionados em repositório público antes de chegarem ao site, e o banco tem um verificador que reprova registro sem fonte, sem data ou com divergência não resolvida — o que está no ar passou por ele.</p>';
	$html .= '<p>Estado de hoje, sem arredondar para cima: ' . robometria_casca_num( $n['marcas'] ) . ' marcas, ' . robometria_casca_num( $n['modelos_publicaveis'] ) . ' modelos de robô e ' . robometria_casca_num( $n['pares_declarados'] ) . ' pares peça × modelo declarados pelo fabricante. Nenhum par inferido.</p></div>';

	$html .= '<div class="rbm-secao"><h2>O que a Robometria não faz</h2>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li>Não vende peça nem intermedia venda, e não tem estoque.</li>';
	$html .= '<li>Não aceita link pago, publieditorial nem posição paga em lista.</li>';
	$html .= '<li>Não usa preço nem comissão como critério técnico. A ordem de uma lista é: primeiro quem passa em <em>todas</em> as condições declaradas pelo fabricante, depois quem é tecnicamente mais adequado, e só como desempate entre equivalentes quem tem link de loja.</li>';
	$html .= '<li>Não publica contagem regressiva, escassez, selo de "mais vendido" nem nota de avaliação que não tenha medido.</li>';
	$html .= '</ul></div>';

	$html .= '<p class="rbm-nota">Um produto que a própria página diz não servir nunca encabeça uma lista aqui. Se você encontrar um caso desses, é defeito — e a página de ' . robometria_casca_link_html( 'metodologia', 'metodologia' ) . ' mostra o critério que deveria tê-lo impedido.</p>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'robometria_afiliados', function () {
	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">Quando houver link de loja nesta página, ele será link de afiliado — e estará marcado como tal.</p>';
	$html .= '<p>Isso significa que, se você comprar por ele, a Robometria pode receber uma comissão da loja, sem custo adicional para você. Os programas usados são os de afiliados da Shopee e do Mercado Livre.</p>';

	$html .= '<div class="rbm-secao"><h2>O que a comissão nunca muda</h2>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li><strong>A ordem da lista.</strong> Primeiro entra quem cumpre todas as condições declaradas pelo fabricante; depois, entre os que cumprem, quem é tecnicamente mais adequado. Ter link de loja só desempata entre itens equivalentes — e nunca comparamos taxa de comissão entre programas.</li>';
	$html .= '<li><strong>Quem aparece.</strong> Produto que não passa na condição declarada não sobe para o topo por ter link; ele vai para uma seção separada, abaixo, dizendo em qual condição falhou.</li>';
	$html .= '<li><strong>O dado técnico.</strong> A fonte de uma especificação é sempre o fabricante. Um link de loja nunca substitui o endereço de origem do dado.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="rbm-secao"><h2>Preço</h2>';
	$html .= '<p>Nenhum preço aqui é apresentado como o preço de agora. Ou a página não traz preço, ou traz a faixa com a data em que ela foi coletada. Preço muda mais rápido do que qualquer página estática consegue acompanhar, e fingir o contrário seria enganar.</p></div>';

	$html .= '<p class="rbm-nota"><strong>Estado de hoje:</strong> ainda não há nenhum link de afiliado no ar nesta ilha. Esta página existe desde o primeiro dia porque a divulgação precisa estar publicada <em>antes</em> do primeiro link, não depois.</p>';
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Estrutura do site: páginas, página inicial e limpeza do tema padrão
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_definicao_paginas' ) ) {
function robometria_casca_definicao_paginas() {
	return array(
		'inicio'                  => array( 'titulo' => 'Início', 'conteudo' => '[robometria_home]' ),
		'ferramentas'             => array( 'titulo' => 'Ferramentas', 'conteudo' => '[robometria_ferramentas]' ),
		'metodologia'             => array( 'titulo' => 'Metodologia', 'conteudo' => '[robometria_metodologia]' ),
		'sobre'                   => array( 'titulo' => 'Sobre', 'conteudo' => '[robometria_sobre]' ),
		'divulgacao-de-afiliados' => array( 'titulo' => 'Divulgação de afiliados', 'conteudo' => '[robometria_afiliados]' ),
	);
}
}

if ( ! function_exists( 'robometria_casca_garantir_paginas' ) ) {
function robometria_casca_garantir_paginas( &$relato ) {
	$ids   = array();
	$criou = false;

	foreach ( robometria_casca_definicao_paginas() as $slug => $def ) {
		$pagina = get_page_by_path( $slug, OBJECT, 'page' );

		if ( ! $pagina ) {
			$pid = wp_insert_post( array(
				'post_type'      => 'page',
				'post_title'     => $def['titulo'],
				'post_name'      => $slug,
				'post_content'   => $def['conteudo'],
				'post_status'    => 'publish',
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $pid ) ) {
				$relato[] = 'página ' . $slug . ': erro — ' . $pid->get_error_message();
				continue;
			}
			update_post_meta( $pid, '_robometria_casca', '1' );
			$ids[ $slug ] = (int) $pid;
			$criou        = true;
			$relato[]     = 'página ' . $slug . ': criada (#' . $pid . ')';
			continue;
		}

		$pid          = (int) $pagina->ID;
		$ids[ $slug ] = $pid;
		$nossa        = ( '1' === get_post_meta( $pid, '_robometria_casca', true ) );

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

if ( ! function_exists( 'robometria_casca_fixar_home' ) ) {
function robometria_casca_fixar_home( $ids, &$relato ) {
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

/**
 * "Hello world!" e "Sample Page" para a LIXEIRA — nunca apagados de verdade.
 *
 * Nesta ilha isso não é acabamento: enquanto a casca não existe, são esses dois
 * itens que o sitemap submetido ao Search Console lista. O sitemap é curadoria,
 * não inventário (seção 14.1), e página de amostra gasta orçamento de
 * rastreamento de domínio novo ensinando ao robô que aqui se publica coisa que
 * não vale voltar para buscar.
 */
/* ---------------------------------------------------------------------------
 * 5b. O SITEMAP NÃO PODE RESPONDER 404 — despacho da Sentinela de 10/09/2026
 *
 * Medido: wp-sitemap.xml servia o XML certo, com as seis páginas dentro, e um
 * status HTTP 404. Para o Google, sitemap com 404 é sitemap inexistente — foi
 * por isso que o Search Console respondeu "Não foi possível buscar", e é por
 * isso que a rampa da seção 14 desta ilha estava parada num defeito de status.
 *
 * A CAUSA, e ela nasce aqui mesmo, na função logo abaixo: esta ilha tem ZERO
 * posts publicados, porque a casca manda "Hello world!" para a lixeira. As
 * rotas de sitemap do WordPress passam pela consulta principal
 * (index.php?sitemap=…), a consulta volta sem nenhum post, e o handle_404() do
 * núcleo carimba 404 ANTES de o renderizador de sitemap imprimir o XML. Daí o
 * sintoma esquisito de corpo válido com status errado. A Aquametria devolve 200
 * nos mesmos caminhos pelo motivo simétrico: ela tem posts.
 *
 * Não é defeito do núcleo nem da hospedagem: é a consequência de um site que
 * publica só páginas. Por isso o conserto fica ao lado da causa, e não desliga
 * nada — o filtro pre_handle_404 existe no núcleo exatamente para isto, e só
 * age em requisição que JÁ é de sitemap. Toda outra URL continua podendo 404,
 * inclusive as de post, que nesta ilha não existem de propósito.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_sitemap_nao_e_404' ) ) {
function robometria_casca_sitemap_nao_e_404( $curto_circuito, $consulta ) {
	if ( is_object( $consulta ) && method_exists( $consulta, 'get' ) && $consulta->get( 'sitemap' ) ) {
		return true;
	}
	return $curto_circuito;
}
}

add_filter( 'pre_handle_404', 'robometria_casca_sitemap_nao_e_404', 10, 2 );

if ( ! function_exists( 'robometria_casca_limpar_padrao' ) ) {
function robometria_casca_limpar_padrao( &$relato ) {
	if ( 'feito' === get_option( 'robometria_casca_limpeza' ) ) {
		return;
	}

	$slugs   = array( 'hello-world', 'ola-mundo', 'sample-page', 'pagina-exemplo', 'pagina-de-exemplo' );
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
		if ( '1' === get_post_meta( $p->ID, '_robometria_casca', true ) ) {
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

	update_option( 'robometria_casca_limpeza', 'feito', false );
}
}

if ( ! function_exists( 'robometria_casca_montar' ) ) {
function robometria_casca_montar( $forcar = false ) {
	$feita = get_option( 'robometria_casca_estrutura' );
	if ( ! $forcar && ROBOMETRIA_CASCA_VERSAO === $feita ) {
		return array();
	}

	$relato = array();
	$ids    = robometria_casca_garantir_paginas( $relato );
	robometria_casca_fixar_home( $ids, $relato );
	robometria_casca_limpar_padrao( $relato );

	update_option( 'robometria_casca_paginas', $ids, false );
	update_option( 'robometria_casca_estrutura', ROBOMETRIA_CASCA_VERSAO, false );

	if ( ! $relato ) {
		$relato[] = 'nada a fazer: estrutura já estava de pé';
	}
	$relato[] = 'casca ' . ROBOMETRIA_CASCA_VERSAO . ' em ' . current_time( 'Y-m-d H:i' );
	update_option( 'robometria_casca_relato', $relato, false );

	return $relato;
}
}

if ( ! function_exists( 'robometria_casca_boot' ) ) {
function robometria_casca_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;

	robometria_casca_montar( false );

	// Remontagem manual: /?robometria_casca=refazer (só para quem administra o site).
	$pedido = filter_input( INPUT_GET, 'robometria_casca', FILTER_DEFAULT );
	if ( 'refazer' === $pedido && current_user_can( 'manage_options' ) ) {
		$relato = robometria_casca_montar( true );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array( 'versao' => ROBOMETRIA_CASCA_VERSAO, 'relato' => $relato ), JSON_UNESCAPED_UNICODE );
		exit;
	}
}
}

add_action( 'init', 'robometria_casca_boot', 20 );

if ( did_action( 'init' ) ) {
	robometria_casca_boot();
}

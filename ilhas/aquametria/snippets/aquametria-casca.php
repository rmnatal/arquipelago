/**
 * Aquametria Casca — identidade e estrutura do site
 * Versão: 1.0.4 (08/09/2026) — o resumo da C12 no hub passou de duas para quatro âncoras de
 * fabricante, que é o que a coleta de 08/09/2026 trouxe. A 1.0.3 pôs a divulgação de afiliados no rodapé
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
 *       (tagline e nota de fontes), para não ficarem dois rodapés empilhados.
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
	define( 'AQUAMETRIA_CASCA_VERSAO', '1.0.4' );
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
			'slug'    => 'calculadora-de-aquecedor',
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

if ( ! function_exists( 'aquametria_casca_url_pagina' ) ) {
function aquametria_casca_url_pagina( $slug ) {
	$pagina = get_page_by_path( $slug, OBJECT, 'page' );
	if ( $pagina ) {
		return get_permalink( $pagina );
	}
	return home_url( '/' . $slug . '/' );
}
}

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

if ( ! function_exists( 'aquametria_casca_nav_html' ) ) {
function aquametria_casca_nav_html() {
	$itens = array(
		'calculadoras' => 'Calculadoras',
		'metodologia'  => 'Metodologia',
		'sobre'        => 'Sobre',
	);

	$html = '<nav class="aqm-nav" aria-label="Navegação principal"><ul>';
	foreach ( $itens as $slug => $rotulo ) {
		$html .= '<li><a href="' . esc_url( aquametria_casca_url_pagina( $slug ) ) . '">' . esc_html( $rotulo ) . '</a></li>';
	}
	$html .= '</ul></nav>';

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
	$html .= '<p><a href="' . esc_url( aquametria_casca_url_pagina( 'metodologia' ) ) . '">Metodologia</a> · <a href="' . esc_url( aquametria_casca_url_pagina( 'divulgacao-de-afiliados' ) ) . '">Divulgação de afiliados</a> · <a href="' . esc_url( aquametria_casca_url_pagina( 'sobre' ) ) . '">Sobre</a> · Aquametria ' . esc_html( date_i18n( 'Y' ) ) . '</p>';
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
CSS;

	echo '<style id="aquametria-casca">' . $css . '</style>' . "\n";
}, 20 );

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
		if ( $publicada ) {
			$html .= '<a href="' . esc_url( aquametria_casca_url_pagina( $c['slug'] ) ) . '">Abrir calculadora</a>';
		} else {
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
	$html .= '<p><a href="' . esc_url( aquametria_casca_url_pagina( 'metodologia' ) ) . '">Ler a metodologia completa</a></p>';
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

	$html .= '<p class="aqm-nota">Achou um número errado ou uma fonte melhor? A página de <a href="' . esc_url( aquametria_casca_url_pagina( 'metodologia' ) ) . '">metodologia</a> mostra o critério que usamos para aceitar ou recusar cada constante. Correção com fonte entra e muda a data de verificação.</p>';
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

/**
 * Robometria Casca — identidade e estrutura do site
 * Versão: 1.4.1 (12/09/2026) — FONTE NÃO PUBLICADA NÃO VIRA NÚMERO NA TELA.
 *   robometria_casca_numeros() lia a option de dados direto, sem perguntar se o
 *   item que a gerou ainda é publicar=true no manifest. Como o Sync PULA o item
 *   despublicado mas NUNCA apaga a option que já gravou, a página seguiria
 *   servindo o número de uma fonte sem página de origem viva. Agora o número só
 *   sai quando o próprio Sync atesta que aplicou aquele item — e ele só aplica
 *   publicar=true. Sem atestado, array() vazio e a página diz que a medição está
 *   fora do ar; nunca um número de reserva.
 * Versão: 1.4.0 (11/09/2026) — UM NOME POR PÁGINA, e o <title> que o repositório
 *   não escrevia. Seis das nove páginas se chamavam de dois jeitos ao mesmo
 *   tempo, porque havia dois mapas de nome digitados; agora há uma fonte só
 *   (robometria_casca_nome_da_pagina) e o H1, o <title>, o og:title, o degrau da
 *   trilha e o rótulo do cartão derivam dela. A casca também assumiu o <title>,
 *   que na home vinha do campo de descrição curta do wp-admin com 73 caracteres
 *   em vocabulário de dentro da fábrica. As quatro páginas da casca perderam o
 *   nome de gaveta, as aberturas foram para a voz do VOZ.md e a procedência
 *   desceu para a camada de prova (classe rbm-prova, seção 15.2). O aviso de
 *   "estamos sem o banco" ganhou dono único e a marca rbm-sem-banco.
 * Versão: 1.3.0 (11/09/2026) — A ÁRVORE DA SEÇÃO 16 (trilha, BreadcrumbList e
 *   cluster de "Veja também"), e os onze números que a ilha publica sobre si
 *   mesma saindo do snippet para dados/casca-fatos.json. Ver as seções 3f e 3g.
 * Versão: 1.2.0 (11/09/2026) — A ILHA GANHA VOZ (seção 15 do ARQUIPELAGO.md e
 * VOZ.md desta pasta) E CABEÇA DE PÁGINA (despacho da Sentinela de 11/09, itens
 * 1 e 2). Quatro mudanças, e nenhuma é enfeite:
 *   (1) <meta name="description"> por página, mais og:title/description/url/type.
 *       Nenhuma das nove páginas publicadas tinha description: a Sentinela mediu
 *       `document.querySelector('meta[name=description]')` devolvendo null nas
 *       nove. Sem plugin de SEO (decisão de projeto) ninguém mais imprime essa
 *       tag, e a seção 12.1 chama a faixa de posição 4 a 10 de "trabalho de CTR
 *       (título, meta, schema)" — sem description não existe o que ajustar, e o
 *       Google inventa o trecho do resultado.
 *   (2) O H1 da raiz era a palavra "Início". É o H1 da página que disputa a
 *       marca, e ele não nomeava o que a ilha faz.
 *   (3) A home passa a ser A FERRAMENTA (molde FERRAMENTA do VOZ.md): o seletor
 *       de marca e modelo em cima, atalhos por tipo de peça, e o número, a fonte
 *       e a data indo para a camada de prova (seção 15.2) — a confissão de
 *       cobertura, que era manifesto na home, mora agora na metodologia, que é a
 *       página cujo produto é o rigor. A home CHAMA o formulário da R1; ela não
 *       tem uma cópia dele.
 *   (4) A FOLHA DO FORMULÁRIO GANHA UM DONO SÓ, como a porta de compra já tem.
 *       As regras .rbm-promessa e .rbm-form* estavam duplicadas na R1 e na R2, e
 *       já tinham começado a divergir (só a R2 estilizava input[type=number]).
 *       Com a home servindo o mesmo formulário seriam TRÊS cópias — e cópia em
 *       três lugares diverge em silêncio. A casca serve a folha em toda página; a
 *       R1 e a R2 ficam só com o que é delas.
 * Versão: 1.0.2 (10/09/2026) — Bloco 5: a casca passa a ter um catálogo de
 * ARTIGOS, do mesmo jeito que já tinha o de ferramentas, e a listá-los na home e
 * no hub. Sem isso o artigo-âncora da R1 nasceria órfão, e a seção 9 do
 * ARQUIPELAGO.md exige que toda página entre em pelo menos duas listagens. Veio
 * junto a folha compartilhada da PORTA DE COMPRA (seção 1c): as regras do botão
 * de compra, do lugar reservado sem link e do link discreto de procedência
 * passam a ter um dono só, em vez de uma cópia por página que recomenda produto.
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
	define( 'ROBOMETRIA_CASCA_VERSAO', '1.4.1' );
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
			'titulo' => 'Quantos Pa o seu robô aspirador precisa',
			'slug'   => 'quantos-pa-o-robo-aspirador-precisa',
			'resumo' => 'Sucção em pascal por tipo de piso e por pelo de animal, e quantos ciclos a sua metragem exige a partir dos minutos que o fabricante declara. As faixas de Pa são recomendação editorial e saem com o nome de quem recomenda.',
			'estado' => 'em-construcao',
		),
	);

	$lista = apply_filters( 'robometria_ferramentas', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

/* ---------------------------------------------------------------------------
 * 1b. Catálogo de ARTIGOS
 *
 * Existe pelo mesmo motivo que o de ferramentas, e a lista nasce VAZIA de
 * propósito: cada artigo se registra pelo filtro dentro do próprio snippet dele,
 * então a casca nunca precisa saber quantos artigos a ilha tem.
 *
 * Por que a casca ganha isto no Bloco 5: a seção 9 do ARQUIPELAGO.md exige que
 * toda página entre em pelo menos DUAS listagens e aponte para três irmãs. Um
 * artigo-âncora que só fosse alcançável pelo link da ferramenta que ele apoia
 * seria uma página órfã com um link, e a malha da ilha começaria torta na
 * primeira peça. Com o catálogo aqui, cada artigo novo aparece na home e no hub
 * sem que nenhuma delas seja editada de novo.
 *
 * Campo 'ferramenta': o SLUG da ferramenta que o artigo apoia, para a listagem
 * poder dizer ao leitor que os dois são o par informativo e a resposta calculada
 * do mesmo assunto. O nome que aparece na frase é resolvido a partir do slug —
 * o campo já foi um título digitado, e isso fazia o par se desfazer em silêncio
 * no dia em que a ferramenta trocasse de nome.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_artigos' ) ) {
function robometria_casca_artigos() {
	$lista = apply_filters( 'robometria_artigos', array() );

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
		/* A1 — o artigo-âncora da R1. "Filtro universal" é como a busca escreve;
		   o endereço canônico é o do artigo. */
		'filtro-universal'                        => 'filtro-universal-de-robo-aspirador',
		'filtro-hepa-universal'                   => 'filtro-universal-de-robo-aspirador',
		'filtro-universal-robo-aspirador'         => 'filtro-universal-de-robo-aspirador',
		'peca-universal-robo-aspirador'           => 'filtro-universal-de-robo-aspirador',
		'escova-universal-robo-aspirador'         => 'filtro-universal-de-robo-aspirador',

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

	/* OS RÓTULOS SÃO AS PALAVRAS DA PESSOA, e os destinos são as páginas onde ela
	   resolve o problema (molde FERRAMENTA do VOZ.md, 11/09/2026). Até aqui o
	   menu era Ferramentas · Metodologia · Sobre: três substantivos de dentro da
	   fábrica, nenhum deles o que alguém com o robô aberto em cima da mesa
	   digitaria. "Peças" e "Sucção" levam direto às duas ferramentas; "Como
	   conferimos" é a metodologia dita pelo técnico, e não pelo manual.

	   O menu NÃO vira Peças · Modelos · Guias, que é o que o VOZ.md descreve:
	   esses três são níveis da árvore da seção 16 do contrato e ainda não
	   existem como página. Rótulo apontando para página inexistente sai como
	   <span> por desenho (robometria_casca_link_html), e um menu de três spans
	   seria pior do que o menu técnico que ele substitui. Eles entram no bloco da
	   árvore, junto com o breadcrumb.

	   /ferramentas/ e /sobre/ saíram do menu e continuam linkados no rodapé, com
	   o hub também linkado do corpo da home: nenhuma página do sitemap fica com
	   menos de dois links internos (seção 16.4-f). */
	$itens = array(
		'qual-peca-serve-no-meu-robo-aspirador' => 'Peças',
		'quantos-pa-o-robo-aspirador-precisa'   => 'Sucção',
		'metodologia'                           => 'Como conferimos',
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
	/* 'ferramentas' entrou aqui quando o menu do topo passou a apontar direto para
	   as duas ferramentas (v1.2.0): o hub perdeu o link do menu e ficaria com um
	   só, o do corpo da home. Seção 16.4-f: nenhuma URL do sitemap com menos de
	   dois links internos. */
	$html .= '<p>' . robometria_casca_link_html( 'ferramentas', 'Ferramentas' )
		. ' · ' . robometria_casca_link_html( 'metodologia', 'Metodologia' )
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
 * 2b-bis. CABEÇA DE PÁGINA — description e Open Graph (despacho da Sentinela,
 * 11/09/2026, item 1)
 *
 * Nenhuma das nove páginas publicadas tinha <meta name="description">. Esta ilha
 * não tem plugin de SEO por decisão de projeto, então ninguém imprimia essa tag:
 * a única "descrição" que existia ia para dentro do JSON-LD do Organization e
 * nunca virava meta. O Google, sem ela, escreve o trecho do resultado sozinho a
 * partir de um pedaço qualquer da página — e a seção 12.1 do contrato, que manda
 * trabalhar CTR na faixa de posição 4 a 10, fica sem alavanca nenhuma.
 *
 * TRÊS DECISÕES, e a terceira é a que importa:
 *
 *   1. O texto diz O QUE A PÁGINA RESPONDE, não o que ela é — e na voz do
 *      VOZ.md, porque description é texto que a pessoa lê no resultado da busca,
 *      não metadado interno. Verbo na frente, segunda pessoa, palavras dela.
 *   2. ~~og:title existe separado do <title>.~~ **REVOGADO em 11/09/2026**, e a
 *      decisão errada custou seis páginas com dois nomes. A ideia era boa no
 *      papel (o <title> leva a marca, o cartão não precisa), mas o que ela
 *      produziu foi um segundo mapa de nomes digitado ao lado do primeiro:
 *      "Sobre" no H1 e "Quem publica a Robometria" no cartão, "Por que não
 *      existe filtro universal" no H1 e "Existe filtro universal?" no cartão.
 *      Agora o og:title é o NOME da página (robometria_casca_nome_da_pagina) e
 *      a marca entra no <title>, que a casca também passou a escrever.
 *   3. NENHUMA DESCRIÇÃO CARREGA NÚMERO, e isso é regra, não estilo. Descrição
 *      é texto digitado que ninguém relê, e a cicatriz de 11/09/2026 (seção 8 do
 *      contrato, o cartão que dizia "0" depois de a categoria ganhar cinco
 *      produtos) é exatamente sobre número digitado numa metade que não fala com
 *      o banco. Aqui é pior que num cartão: o banco cresce, a descrição
 *      continua no ar mentindo, e ela nem aparece na tela para alguém
 *      estranhar. Número mora na camada de prova (seção 15.2): tabela,
 *      resultado, JSON-LD. O teste de bancada reprova dígito aqui dentro.
 *
 * O mapa passa pelo filtro 'robometria_cabecas' para página nova poder trazer a
 * dela de dentro do próprio snippet, como já acontece com ferramenta e artigo.
 * O portão que impede alguém de esquecer está na bancada, cobrando as DUAS
 * direções: página conhecida sem cabeça reprova, e cabeça sem página também.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_cabecas' ) ) {
function robometria_casca_cabecas() {
	$mapa = array(
		'inicio' => array(
			'tipo'      => 'website',
			'descricao' => 'Diga a marca e o modelo do seu robô aspirador e veja qual filtro, escova, mop ou bateria o fabricante declarou para ele.',
		),
		'ferramentas' => array(
			'tipo'      => 'website',
			'descricao' => 'Uma diz qual peça serve no seu robô aspirador. A outra diz quanta sucção e quanto tempo a metragem da sua casa pede.',
		),
		'metodologia' => array(
			'tipo'      => 'website',
			'descricao' => 'De onde vem cada dado daqui, quando ele vale como "serve", e o que a Robometria ainda não sabe responder sobre o seu robô.',
		),
		'sobre' => array(
			'tipo'      => 'website',
			'descricao' => 'Quem faz a Robometria, por que ela só afirma o que o fabricante declarou, e como avisar quando uma peça daqui não encaixou.',
		),
		'divulgacao-de-afiliados' => array(
			'tipo'      => 'website',
			'descricao' => 'Ganhamos comissão quando você compra pelos nossos links, e isso nunca muda a ordem da lista. Veja como a recomendação é montada.',
		),
		'qual-peca-serve-no-meu-robo-aspirador' => array(
			'tipo'      => 'website',
			'descricao' => 'Escolha a marca e o modelo e veja o filtro, a escova, o mop e a bateria que o fabricante declarou para o seu robô, com código e data.',
		),
		'quantos-pa-o-robo-aspirador-precisa' => array(
			'tipo'      => 'website',
			'descricao' => 'Quanta sucção o seu robô precisa para piso liso, tapete ou pelo de cachorro, e quantos ciclos a metragem da sua casa exige.',
		),
		'filtro-universal-de-robo-aspirador' => array(
			'tipo'      => 'article',
			'descricao' => 'Conferimos peça por peça quantas servem em mais de uma marca, e o que fazer quando o filtro barato do anúncio promete servir em tudo.',
		),
		'quantos-m2-o-robo-aspirador-limpa-por-carga' => array(
			'tipo'      => 'article',
			'descricao' => 'De onde vem o número de metros quadrados por carga que os sites publicam, quais marcas declaram, e o que fazer quando a sua não declara.',
		),
	);

	$mapa = apply_filters( 'robometria_cabecas', $mapa );

	return is_array( $mapa ) ? $mapa : array();
}
}

/**
 * O slug canônico da página que está sendo servida, ou '' quando não é uma
 * página da ilha.
 *
 * A identidade canônica é o meta _robometria_id, que o Sync grava e que
 * sobrevive ao WordPress ter acrescentado "-2" ao slug por conflito. O
 * post_name é a segunda via, para as páginas que não vieram do Sync.
 */
if ( ! function_exists( 'robometria_casca_slug_atual' ) ) {
function robometria_casca_slug_atual() {
	if ( is_front_page() ) {
		return 'inicio';
	}

	$id = (int) get_queried_object_id();
	if ( $id < 1 ) {
		return '';
	}

	$marcado = (string) get_post_meta( $id, '_robometria_id', true );
	if ( '' !== $marcado ) {
		return $marcado;
	}

	$nome = get_post_field( 'post_name', $id );

	return is_string( $nome ) ? $nome : '';
}
}

add_action( 'wp_head', function () {
	$slug   = robometria_casca_slug_atual();
	$cabeca = robometria_casca_cabecas();

	/* Página que a casca não conhece sai SEM description. Inventar uma frase
	   genérica para caber em qualquer página seria publicar a mesma descrição em
	   endereços diferentes, que é o defeito que a tag existe para não ter. */
	if ( '' === $slug || ! isset( $cabeca[ $slug ] ) ) {
		return;
	}

	$c   = $cabeca[ $slug ];
	$url = ( 'inicio' === $slug ) ? home_url( '/' ) : robometria_casca_url_se_existir( $slug );
	if ( '' === $url ) {
		$url = home_url( '/' . $slug . '/' );
	}

	echo '<meta name="description" content="' . esc_attr( $c['descricao'] ) . '">' . "\n";
	echo '<meta property="og:type" content="' . esc_attr( $c['tipo'] ) . '">' . "\n";
	/* O og:title É o nome da página, derivado, e não uma segunda frase digitada
	   ao lado da primeira. Era assim que as seis divergências de nome entravam:
	   o mapa das cabeças trazia um título só dele, ninguém comparava os dois, e
	   a página passava a se chamar de dois jeitos em superfícies que aparecem
	   uma ao lado da outra no resultado da busca. */
	echo '<meta property="og:title" content="' . esc_attr( robometria_casca_nome_da_pagina( $slug ) ) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr( $c['descricao'] ) . '">' . "\n";
	echo '<meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
	echo '<meta property="og:site_name" content="Robometria">' . "\n";
	echo '<meta property="og:locale" content="pt_BR">' . "\n";
}, 4 );

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
/* Listagem de artigos: lista de leitura, nao cartao. O cartao e a forma de quem
   oferece uma acao ("abrir ferramenta"); artigo se oferece pelo titulo. */
.rbm-artigos{list-style:none;margin:1.4rem 0 0;padding:0;display:flex;flex-direction:column;gap:1.1rem;}
.rbm-artigo{margin:0;padding:0 0 1.1rem;border-bottom:1px solid var(--rbm-traco);}
.rbm-artigo:last-child{border-bottom:0;padding-bottom:0;}
.rbm-artigo h3{font-family:var(--rbm-display);font-size:1.08rem;margin:0 0 .3rem;line-height:1.3;}
.rbm-artigo p{margin:0;color:var(--rbm-legenda);font-size:.93rem;line-height:1.5;}
.rbm-artigo-par{font-family:var(--rbm-mono);font-size:.76rem;letter-spacing:.03em;margin-top:.35rem;}
/* Ressalva tecnica em ambar. Nunca vermelho: vermelho e a marca. */
.rbm-tag{display:inline-block;font-family:var(--rbm-mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--rbm-alerta);border:1px solid var(--rbm-alerta);border-radius:2px;padding:.15rem .4rem;}
.rbm-prova{color:var(--rbm-legenda);font-size:.97rem;}
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
/* FORMULARIO DE FERRAMENTA — dono unico, como a porta de compra (v1.2.0).
   Estas regras moravam duplicadas na folha da R1 e na da R2, e ja tinham
   comecado a divergir: so a R2 estilizava input[type=number]. Com a home
   servindo o mesmo formulario, seriam TRES copias — e o dia em que alguem
   ajustar uma delas a ilha passa a ter dois formularios diferentes sem que
   ninguem note. A versao daqui e a UNIAO das duas, entao nenhuma pagina muda de
   aparencia; a R1 e a R2 ficam so com o que e delas.

   min-width:0 nao e detalhe: sem ele o item de flex recebe min-width:auto e a
   largura INTRINSECA do <select> manda — e a intrinseca aqui e o rotulo mais
   longo do seletor ("Multi (ex-Multilaser)" na R1, "Electrolux ERB60 — 166 m2
   por carga" na R2). Medido num Chromium a 360 px antes da correcao: 39 px de
   rolagem horizontal, que a secao 6 do contrato nao admite. */
.rbm-promessa{color:var(--rbm-legenda);margin:0 0 .9rem;font-size:.95rem;}
.rbm-form{display:flex;flex-wrap:wrap;gap:.9rem 1.1rem;align-items:flex-end;background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;padding:1.1rem 1.2rem;margin:0;}
.rbm-form-campo{display:flex;flex-direction:column;gap:.3rem;margin:0;flex:1 1 15rem;min-width:0;}
.rbm-form-campo label{font-family:var(--rbm-texto);font-weight:600;font-size:.88rem;}
.rbm-form select,.rbm-form input[type=number]{font-family:var(--rbm-texto);font-size:1rem;padding:.55rem .6rem;border:1px solid var(--rbm-traco);border-radius:2px;background:var(--rbm-superficie);color:var(--rbm-tinta);width:100%;max-width:100%;}
.rbm-form input[type=number]{font-family:var(--rbm-mono);font-variant-numeric:tabular-nums;}
.rbm-form select:focus-visible,.rbm-form input:focus-visible{outline:2px solid var(--rbm-varredura);outline-offset:2px;}
.rbm-form-acao{margin:0;flex:0 0 auto;}
.rbm-form button{padding:.62rem 1.1rem;font-size:.95rem;cursor:pointer;}
/* Atalhos por tipo de peca, logo abaixo do seletor da home. Sao links de
   verdade, nao botoes de JavaScript: quem le sem executar script (o crawler de
   IA, regra de primeira classe na secao 5) chega na mesma pagina. */
.rbm-atalhos{margin:.9rem 0 0;font-size:.92rem;color:var(--rbm-legenda);}
.rbm-atalhos ul{list-style:none;margin:.4rem 0 0;padding:0;display:flex;flex-wrap:wrap;gap:.5rem .6rem;}
.rbm-atalhos li{margin:0;}
.rbm-atalhos a{display:inline-block;padding:.32rem .7rem;border:1px solid var(--rbm-traco);border-radius:2px;background:var(--rbm-superficie);text-decoration:none;border-bottom:1px solid var(--rbm-traco);}
.rbm-atalhos a:hover{color:var(--rbm-varredura);border-color:var(--rbm-legenda);}
@media (max-width:600px){
.rbm-linha-mestra{font-size:1.15rem;}
.rbm-wordmark{font-size:1.2rem;}
}
/* Menu sanfona. 782 px e a largura em que o proprio WordPress considera que a
   tela virou celular; seguir a mesma quebra evita cabecalho meio empilhado.
   Tudo aqui depende de [data-rbm-menu]: sem JavaScript nada disso vale e o menu
   continua sendo a fileira de links, visivel. */
@media (max-width:782px){
.rbm-form-campo{flex:1 1 100%;}
.rbm-form-acao,.rbm-form button{width:100%;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav-botao{display:inline-flex;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav{display:none;position:absolute;right:0;top:calc(100% + .55rem);z-index:60;min-width:13rem;background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;box-shadow:0 12px 32px rgba(22,25,29,.16);padding:.35rem 0;}
.rbm-nav-caixa[data-rbm-menu][data-rbm-aberto="1"] .rbm-nav{display:block;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav ul,.rbm-nav-caixa[data-rbm-menu] .rbm-nav li{display:block;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav a,.rbm-nav-caixa[data-rbm-menu] .rbm-nav .rbm-sem-link{display:block;padding:.65rem 1.05rem;font-size:1rem;border-bottom:0;}
.rbm-nav-caixa[data-rbm-menu] .rbm-nav a:hover{background:var(--rbm-piso);color:var(--rbm-varredura);}
}
/* A TRILHA (secao 16.3) e o CLUSTER (16.4). A trilha ROLA na horizontal dentro
   da propria caixa quando nao cabe — e o unico jeito de uma trilha longa nao
   empurrar a pagina inteira para o lado num celular de 360 px. O degrau de
   categoria ainda nao publicada sai em texto de legenda, e nunca sublinhado:
   sublinhado promete clique. */
.rbm-trilha{font-family:var(--rbm-texto);font-size:.82rem;line-height:1.5;margin:0 0 1.1rem;max-width:100%;overflow-x:auto;}
.rbm-trilha ol{display:flex;flex-wrap:nowrap;align-items:center;gap:.3rem;list-style:none;margin:0;padding:0;}
.rbm-trilha li{display:flex;align-items:center;gap:.3rem;white-space:nowrap;}
.rbm-trilha li+li::before{content:"\203A";color:var(--rbm-traco);}
.rbm-trilha a{color:var(--rbm-legenda);text-decoration:none;border-bottom:1px solid var(--rbm-traco);}
.rbm-trilha a:hover{color:var(--rbm-varredura);border-bottom-color:var(--rbm-varredura);}
.rbm-trilha [aria-current="page"]{color:var(--rbm-tinta);font-weight:500;}
.rbm-trilha-espera{color:var(--rbm-legenda);}
.rbm-veja{margin:2.6rem 0 0;padding:1.2rem 0 0;border-top:1px solid var(--rbm-traco);max-width:52rem;}
.rbm-veja h2{font-family:var(--rbm-display);font-size:1.1rem;margin:0 0 .6rem;}
.rbm-veja-mae{margin:0 0 .7rem;color:var(--rbm-legenda);font-size:.95rem;}
.rbm-veja ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.5rem;}
.rbm-veja li{margin:0;}
.rbm-veja a{font-weight:500;}
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
/**
 * A listagem de artigos, para a home e para o hub.
 *
 * Sai '' quando não há artigo publicado — listagem vazia com título em cima é
 * promessa não cumprida, e quem chama só imprime a seção se receber HTML.
 */
if ( ! function_exists( 'robometria_casca_artigos_html' ) ) {
function robometria_casca_artigos_html() {
	$itens = array();
	foreach ( robometria_casca_artigos() as $a ) {
		/* Mesma trava dos cartões de ferramenta: sem página publicada, nenhum
		   link é impresso. Link de listagem para página inexistente é 404 no ar. */
		$url = robometria_casca_url_se_existir( isset( $a['slug'] ) ? $a['slug'] : '' );
		if ( '' === $url ) {
			continue;
		}
		$itens[] = '<li class="rbm-artigo">'
			. '<h3><a href="' . esc_url( $url ) . '">' . esc_html( $a['titulo'] ) . '</a></h3>'
			. '<p>' . esc_html( $a['resumo'] ) . '</p>'
			. ( isset( $a['ferramenta'] ) && '' !== robometria_casca_nome_da_pagina( $a['ferramenta'] )
				? '<p class="rbm-artigo-par">Faz par com a ferramenta '
					. esc_html( robometria_casca_nome_da_pagina( $a['ferramenta'] ) ) . '.</p>'
				: '' )
			. '</li>';
	}

	if ( ! $itens ) {
		return '';
	}

	return '<ul class="rbm-artigos">' . implode( '', $itens ) . '</ul>';
}
}

/**
 * A folha da PORTA DE COMPRA, compartilhada por toda página que recomenda item.
 *
 * Fica na casca, e não numa cópia por página, porque os pesos visuais destas
 * duas coisas são regra do Arquipélago (seção 7), não estilo local: o botão de
 * compra tem área de toque de botão, e a procedência é texto pequeno, sem caixa
 * e sem preenchimento, porque ela existe para ser conferida e não para ser
 * clicada. Com uma cópia por página, bastaria alguém ajustar uma delas para a
 * ilha voltar, numa página só e sem ninguém notar, ao defeito de 10/09/2026 —
 * quando o único link clicável levava para a loja do fabricante.
 *
 * Não vai no wp_head global: quem serve vitrine chama esta função dentro da
 * própria folha, e página sem vitrine não carrega regra que não usa.
 */
if ( ! function_exists( 'robometria_casca_css_vitrine' ) ) {
function robometria_casca_css_vitrine() {
	return <<<'CSS'
.rbm-vitrine{display:flex;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;list-style:none;margin:1rem 0 0;padding:0 0 .6rem;}
.rbm-vitrine-item{scroll-snap-align:start;flex:0 0 17rem;max-width:100%;background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;padding:1rem;display:flex;flex-direction:column;gap:.4rem;margin:0;}
.rbm-vitrine-foto{display:flex;aspect-ratio:4/3;max-width:100%;background:var(--rbm-piso);border:1px solid var(--rbm-traco);border-radius:2px;align-items:center;justify-content:center;}
.rbm-vitrine-vazia{display:block;width:2.4rem;height:2.4rem;border:2px solid var(--rbm-traco);border-radius:50%;border-right-color:transparent;}
.rbm-vitrine-tipo{font-family:var(--rbm-display);font-weight:600;font-size:1rem;}
.rbm-vitrine-nome{font-size:.86rem;color:var(--rbm-legenda);line-height:1.45;}
.rbm-vitrine-porque{font-size:.88rem;line-height:1.45;}
.rbm-vitrine-vida{font-size:.84rem;color:var(--rbm-legenda);}
.rbm-vitrine-acao{margin-top:auto;padding-top:.6rem;font-size:.88rem;}
.rbm-comprar{display:block;text-align:center;padding:.6rem .9rem;border:1px solid var(--rbm-tinta);border-radius:2px;background:var(--rbm-tinta);color:var(--rbm-piso);font-family:var(--rbm-texto);font-weight:600;font-size:.9rem;text-decoration:none;}
.rbm-comprar:hover,.rbm-comprar:focus-visible{background:var(--rbm-superficie);color:var(--rbm-tinta);}
.rbm-sem-loja{display:block;text-align:center;padding:.6rem .9rem;border:1px dashed var(--rbm-traco);border-radius:2px;color:var(--rbm-legenda);font-size:.84rem;}
.rbm-vitrine-fonte{font-size:.78rem;color:var(--rbm-legenda);line-height:1.4;}
.rbm-fonte{font-size:.78rem;color:var(--rbm-legenda);text-decoration:underline;}
.rbm-aviso-comissao{font-size:.86rem;color:var(--rbm-legenda);line-height:1.5;margin:.2rem 0 0;}
CSS;
}
}

/**
 * O rótulo do botão de compra: nomeia a loja para quem vai clicar.
 *
 * Programa que o banco ainda não declarou sai como "loja parceira" — nunca
 * inventando o nome de um marketplace que ninguém conferiu.
 */
if ( ! function_exists( 'robometria_casca_rotulo_da_loja' ) ) {
function robometria_casca_rotulo_da_loja( $programa ) {
	$nomes = array(
		'shopee'       => 'na Shopee',
		'mercadolivre' => 'no Mercado Livre',
		'amazon'       => 'na Amazon',
	);
	return isset( $nomes[ $programa ] ) ? $nomes[ $programa ] : 'na loja parceira';
}
}

/**
 * A PORTA DE COMPRA de um item — presente mesmo quando o link ainda não existe.
 *
 * O lugar é RESERVADO em vez de escondido, e a diferença não é cosmética: bloco
 * que só nasce quando o link chega faz a página voltar, sozinha, ao defeito de
 * ter a procedência como única porta clicável durante todas as semanas em que o
 * cano de links está enchendo (seção 7 do ARQUIPELAGO.md).
 *
 * Mora na casca desde 10/09/2026 porque deixou de ser detalhe de uma ferramenta:
 * a partir do artigo-âncora, mais de uma página desta ilha recomenda item, e o
 * lugar de uma regra do Arquipélago é um lugar só.
 */
if ( ! function_exists( 'robometria_casca_porta_de_compra' ) ) {
function robometria_casca_porta_de_compra( $item ) {
	$a   = isset( $item['afiliado'] ) ? $item['afiliado'] : array();
	$url = isset( $a['url'] ) ? $a['url'] : '';

	if ( '' === $url ) {
		return '<span class="rbm-sem-loja">Link de loja em breve</span>';
	}

	/* rel="sponsored" é a declaração que o Google pede para link pago, e vem
	   junto de nofollow e noopener (seção 7 do contrato). */
	return '<a class="rbm-comprar" href="' . esc_url( $url ) . '" target="_blank"'
		. ' rel="sponsored nofollow noopener">'
		. esc_html( 'Ver ' . robometria_casca_rotulo_da_loja(
			isset( $a['programa'] ) ? $a['programa'] : null ) )
		. '</a>';
}
}

/**
 * O link de procedência, discreto por regra: texto "fonte", nunca um botão, e
 * sempre nofollow — ele existe para ser conferido, não para ser clicado.
 */
if ( ! function_exists( 'robometria_casca_fonte_link' ) ) {
function robometria_casca_fonte_link( $url ) {
	if ( empty( $url ) ) {
		return '';
	}
	return '<a class="rbm-fonte" href="' . esc_url( $url )
		. '" target="_blank" rel="nofollow noopener">fonte</a>';
}
}

/**
 * A FONTE PRECISA ESTAR PUBLICADA — e quem atesta isso é o próprio Sync.
 *
 * O defeito que esta função tinha, e que era latente: ela lia a option de dados
 * direto, sem perguntar se o item que a gerou ainda tem `publicar: true` no
 * manifest. O Sync PULA o item despublicado (`$pulados++`) e **nunca apaga a
 * option que já gravou** — então, no dia em que alguém virasse `casca-fatos`
 * para `publicar: false`, a página continuaria servindo aqueles números para
 * sempre, com cara de medição e sem página de origem viva. Foi exatamente essa
 * família de defeito que fez a seção 4 da metodologia servir número digitado
 * durante semanas, lendo a option de `cobertura-r1`, que é `publicar: false`.
 *
 * O ATESTADO. O Sync só escreve `estado['itens']['dados:<id>']` quando APLICA o
 * item, e ele só aplica `publicar: true` (robometria-sync.php, o desvio de
 * `publicar` antes de `robometria_sync_aplicar_dados()`). Logo, a presença desse
 * registro é a única prova, no próprio site, de que a fonte foi publicada. Sem
 * registro, a resposta é NÃO — nada de número.
 *
 * FALHA FECHADA, de propósito: na dúvida a página diz que a medição está fora do
 * ar, que é uma afirmação honesta. Valor de reserva seria mentira com cara de
 * medição, e ninguém a releria para descobrir.
 *
 * LIMITE CONHECIDO, escrito aqui para ninguém confiar demais: depois que o Sync
 * já aplicou o item, o registro fica. Se `publicar` virar `false` mais tarde, o
 * site não tem como distinguir "não mudou" de "foi despublicado" — para fechar
 * esse resto o Sync teria de gravar o `publicar` de cada item, e o snippet do
 * Sync não viaja pelo manifest (ele é colado à mão no Code Snippets).
 */
if ( ! function_exists( 'robometria_casca_fonte_publicada' ) ) {
function robometria_casca_fonte_publicada( $id ) {
	$estado = get_option( 'robometria_sync_estado' );
	if ( ! is_array( $estado ) || empty( $estado['itens'] ) || ! is_array( $estado['itens'] ) ) {
		return false;
	}
	$chave = 'dados:' . $id;
	return ! empty( $estado['itens'][ $chave ]['option'] );
}
}

/**
 * OS NÚMEROS QUE A ILHA PUBLICA SOBRE SI MESMA — todos derivados, nenhum digitado.
 *
 * Até a casca 1.2.0 os onze moravam aqui dentro, escritos à mão, com um caminho
 * "derivado" que NUNCA rodava: ele lia a option `robometria_dados_cobertura-r1`,
 * e `cobertura-r1` tem `publicar: false` no manifest — a option não existe no
 * site. Ou seja: no ar, cada número sempre veio do valor digitado, e o trecho que
 * parecia corrigi-lo era decoração. Ficavam certos porque alguém os copiou à mão
 * no dia certo, e um deles já tinha deixado de estar: a linha "pares peça ×
 * modelo, todos declarados" dizia 33 e o banco de hoje tem 32 pelo critério que a
 * própria frase anuncia — o par que sobrava aponta para um modelo excluído do
 * banco, que o site nunca serve.
 *
 * Agora eles viajam dentro de `casca-fatos.json`, que é publicável, derivado por
 * `ferramentas/gerar-casca-fatos.py` a partir do banco commitado, com a régua de
 * cada um escrita no próprio arquivo (`reguas_da_medicao`).
 *
 * SEM O ARQUIVO, A PÁGINA NÃO INVENTA NÚMERO: devolve array() e quem chama diz
 * que a medição está fora do ar. Valor de reserva aqui seria exatamente o número
 * digitado que este bloco veio tirar — só que invisível, porque ninguém releria.
 */
if ( ! function_exists( 'robometria_casca_numeros' ) ) {
function robometria_casca_numeros() {
	if ( ! robometria_casca_fonte_publicada( 'casca-fatos' ) ) {
		return apply_filters( 'robometria_numeros', array() );
	}

	$fatos = get_option( 'robometria_dados_casca-fatos' );
	if ( ! is_array( $fatos ) || empty( $fatos['medicao'] ) || ! is_array( $fatos['medicao'] ) ) {
		return apply_filters( 'robometria_numeros', array() );
	}

	$n = array();
	foreach ( $fatos['medicao'] as $chave => $valor ) {
		$n[ $chave ] = is_int( $valor ) ? (int) $valor : $valor;
	}

	/* Quantos itens do banco JÁ têm link de loja. A página de divulgação de
	   afiliados afirma isso ao visitante, e afirmação da página sobre o próprio
	   banco se conta (seção 8 do ARQUIPELAGO.md). Dizia, à mão, "ainda não há
	   nenhum link de afiliado no ar" — frase que era verdade no dia em que foi
	   escrita e que ninguém releria no dia em que deixasse de ser. */
	if ( isset( $n['itens_publicaveis'], $n['esperando_link'] ) ) {
		$n['com_link'] = max( 0, (int) $n['itens_publicaveis'] - (int) $n['esperando_link'] );
	}

	return apply_filters( 'robometria_numeros', $n );
}
}

/**
 * A frase que ocupa o lugar do número quando a medição não chegou ao site.
 *
 * Ela existe para a página continuar verdadeira sem o banco: "estamos sem o
 * número" é uma afirmação honesta; um número de reserva seria uma mentira com
 * cara de medição, e ninguém a releria para descobrir.
 */
/**
 * O ESTADO DEGRADADO TEM UMA MARCA SÓ, e ela é para quem mede, não para quem lê.
 *
 * Cinco lugares desta ilha servem uma página válida quando o banco não chegou —
 * as duas ferramentas, os dois artigos e o trecho de números da metodologia. A
 * frase é honesta e a página é inteira: cabeçalho, rodapé, folha e trilha. Foi
 * exatamente por isso que o varredor de corpo passou dois dias medindo três
 * desses estados como se fossem a página real (11/09/2026), sem erro nenhum.
 *
 * A classe `rbm-sem-banco` não muda nada na tela. Ela existe para a bancada
 * conseguir dizer "isto aqui não é a página" — `ferramentas/varrer-corpo.php`
 * imprime `!!! sem-banco` no estado que a carrega, e os portões cobram a
 * ausência. Marca no markup, como manda a seção 8 do `ARQUIPELAGO.md` para toda
 * afirmação sobre o que a página diz: quem decide é a estrutura, nunca a
 * vizinhança das palavras.
 *
 * Fica na casca pelo mesmo motivo da porta de compra: uma cópia por snippet e
 * bastaria alguém esquecer a classe numa delas para a trava voltar a não ver.
 */
if ( ! function_exists( 'robometria_casca_sem_banco_html' ) ) {
function robometria_casca_sem_banco_html( $chamada, $explicacao ) {
	return '<div class="rbm-bloco rbm-sem-banco">'
		. '<p class="rbm-linha-mestra">' . $chamada . '</p>'
		. '<p class="rbm-nota">' . $explicacao . '</p></div>';
}
}

if ( ! function_exists( 'robometria_casca_sem_medicao_html' ) ) {
function robometria_casca_sem_medicao_html() {
	return '<p class="rbm-nota rbm-sem-banco"><strong>A medição não chegou ao site agora.</strong> '
		. 'Esta parte da página conta itens do nosso banco, e preferimos deixar o espaço vazio '
		. 'a publicar um número que não foi contado hoje. Ela volta na próxima atualização.</p>';
}
}

/** A medição chegou ao site? Quem escreve frase com número pergunta isto antes. */
if ( ! function_exists( 'robometria_casca_tem_numeros' ) ) {
function robometria_casca_tem_numeros() {
	$n = robometria_casca_numeros();
	foreach ( array( 'medido_em', 'marcas', 'modelos_publicaveis', 'pecas_publicaveis',
		'pares_declarados', 'r1_responde', 'r1_vazia', 'celulas', 'celulas_sem_resposta',
		'as_duas', 'esperando_link', 'itens_publicaveis', 'com_link' ) as $chave ) {
		if ( ! isset( $n[ $chave ] ) ) {
			return false;
		}
	}
	return true;
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

/**
 * Os atalhos por tipo de peça, logo abaixo do seletor da home.
 *
 * SÃO DERIVADOS, nunca digitados. O VOZ.md pede "as três dúvidas mais comuns
 * (filtro, escova, bateria) como atalhos", e digitar esses três aqui seria
 * repetir a cicatriz de 11/09/2026 da seção 8 do contrato — o cartão que dizia
 * "0" porque o número era digitado numa metade que não falava com o banco. A
 * lista sai de robometria_r1_dados()['tipos'], que é a mesma lista que preenche
 * o seletor: tipo sem nenhuma peça no banco não aparece em lugar nenhum, e tipo
 * novo aparece nos dois sem ninguém vir aqui.
 *
 * rel="nofollow": o destino é uma consulta (?peca=…), e consulta desta ilha sai
 * com noindex,follow e canônica para a página limpa (decisão 4 da R1). O atalho
 * existe para a pessoa, não para o rastreador, e domínio novo não tem orçamento
 * de rastreamento para gastar em variação de formulário (seção 14.1).
 */
if ( ! function_exists( 'robometria_casca_atalhos_html' ) ) {
function robometria_casca_atalhos_html() {
	if ( ! function_exists( 'robometria_r1_dados' ) || ! function_exists( 'robometria_r1_nome_do_tipo' ) ) {
		return '';
	}

	$d = robometria_r1_dados();
	if ( empty( $d['tipos'] ) ) {
		return '';
	}

	$base = function_exists( 'robometria_r1_url_da_pagina' )
		? robometria_r1_url_da_pagina()
		: robometria_casca_url_se_existir( 'qual-peca-serve-no-meu-robo-aspirador' );
	if ( '' === $base ) {
		return '';
	}

	$html = '<div class="rbm-atalhos"><p>Já sabe qual peça é?</p><ul>';
	foreach ( (array) $d['tipos'] as $tipo ) {
		$rotulo = robometria_r1_maiuscula( robometria_r1_nome_do_tipo( $tipo ) );
		$html  .= '<li><a rel="nofollow" href="' . esc_url( $base . '?peca=' . rawurlencode( $tipo ) ) . '">'
			. esc_html( $rotulo ) . '</a></li>';
	}
	$html .= '</ul></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3f. A ÁRVORE — trilha, BreadcrumbList e cluster de "Veja também"
 *
 * Seção 16 do ARQUIPELAGO.md, e o item que o despacho do Raphael de 11/09/2026
 * deixou de pé depois do bloco da voz. O mapa de quem é mãe de quem está escrito
 * em ARVORE.md; aqui ele vira código, e `ferramentas/teste-arvore.php` confere
 * que as duas metades dizem a mesma coisa — documento e código mantidos à mão em
 * dois lugares divergem em silêncio (seção 8 do contrato).
 *
 * CINCO DECISÕES, e nenhuma é enfeite:
 *
 *   1. NADA AQUI CRIA URL. As dezoito páginas de nível 1 e 2 da árvore esperam o
 *      sitemap ser reenviado no Search Console (metade humana do despacho da
 *      Sentinela de 10/09): sem medição não há rampa, e sem rampa página nova é
 *      página no escuro. Trilha e cluster cabem antes porque só usam endereço
 *      que já existe.
 *   2. A MÃE DE TRANSIÇÃO DAS DUAS FERRAMENTAS É `/ferramentas/`, QUE EXISTE.
 *      O destino delas é `/pecas/` e `/succao/`, e a alternativa seria publicar
 *      hoje um degrau em texto apontando para o vazio. Mãe com endereço de
 *      verdade dá ao leitor um lugar para onde subir e ao schema um item a mais;
 *      é estado de transição declarado no ARVORE.md, não desenho. `/ferramentas/`
 *      é retirada com 301 no dia em que as duas seções nascerem — é a única
 *      página desta ilha com prazo de validade.
 *   3. O DEGRAU SEM ENDEREÇO SAI EM TEXTO E NÃO ENTRA NO JSON-LD. Um ListItem
 *      intermediário sem `item` invalida o BreadcrumbList inteiro para o Google,
 *      e lista inválida é lista ignorada — o schema "mais completo" publicaria
 *      MENOS com cara de publicar mais. A trilha na tela continua mostrando a
 *      seção e a categoria, que é o que diz ao leitor onde ele está.
 *   4. AS IRMÃS SÃO DERIVADAS, NUNCA DIGITADAS. Lista de irmã escrita à mão
 *      envelhece no dia da próxima ferramenta — é a cicatriz do número de tela
 *      digitado (seção 8). Elas saem do mesmo registro que alimenta o hub e a
 *      prateleira de artigos, com afinidade declarada: mesma categoria primeiro.
 *   5. A FRASE DE MÃE SÓ SAI COM MÃE PUBLICADA, e o número dela é CONTADO. As
 *      duas ferramentas a têm; os dois guias não, porque `/guias/` não existe —
 *      e o portão cobra a ausência dela, para ninguém fechar isso com um
 *      endereço inventado.
 * ------------------------------------------------------------------------- */

/* NÍVEL 1. O slug é o do ARVORE.md; o rótulo é o nome que a pessoa usa. */
if ( ! function_exists( 'robometria_casca_secoes' ) ) {
function robometria_casca_secoes() {
	return array(
		'pecas'   => 'Peças',
		'succao'  => 'Sucção',
		'modelos' => 'Modelos',
		'guias'   => 'Guias',
	);
}
}

/* NÍVEL 2: slug => array( seção, rótulo ). */
if ( ! function_exists( 'robometria_casca_categorias' ) ) {
function robometria_casca_categorias() {
	return array(
		'filtros'               => array( 'pecas',   'Filtros' ),
		'escovas-laterais'      => array( 'pecas',   'Escovas laterais' ),
		'escovas-principais'    => array( 'pecas',   'Escovas principais' ),
		'mops'                  => array( 'pecas',   'Mops' ),
		'baterias'              => array( 'pecas',   'Baterias' ),
		'pisos-e-pelo'          => array( 'succao',  'Pisos e pelo' ),
		'metragem-e-autonomia'  => array( 'succao',  'Metragem e autonomia' ),
		'electrolux'            => array( 'modelos', 'Electrolux' ),
		'multi'                 => array( 'modelos', 'Multi' ),
		'positivo'              => array( 'modelos', 'Positivo' ),
		'xiaomi'                => array( 'modelos', 'Xiaomi' ),
		'wap'                   => array( 'modelos', 'WAP' ),
		'guias-pecas'           => array( 'guias',   'Peças' ),
		'guias-succao'          => array( 'guias',   'Sucção' ),
	);
}
}

/* AS PÁGINAS QUE FICAM NA RAIZ, fora da árvore (ARVORE.md seção 2). Só os slugs:
   o rótulo do degrau é o TÍTULO da página, lido da definição dela. Rótulo próprio
   aqui seria um segundo nome para a mesma página, e o degrau atual de uma trilha
   que não diz o que o H1 diz manda o leitor conferir se ele está onde pensa. */
if ( ! function_exists( 'robometria_casca_paginas_de_raiz' ) ) {
function robometria_casca_paginas_de_raiz() {
	return array( 'metodologia', 'sobre', 'divulgacao-de-afiliados' );
}
}

/* O título publicado de uma página da casca — o mesmo que vira o H1. */
if ( ! function_exists( 'robometria_casca_titulo_da_pagina' ) ) {
function robometria_casca_titulo_da_pagina( $slug ) {
	$def = robometria_casca_definicao_paginas();
	return isset( $def[ $slug ]['titulo'] ) ? $def[ $slug ]['titulo'] : '';
}
}

/**
 * UM NOME POR PÁGINA, e este é o lugar onde ele mora.
 *
 * Uma página desta ilha aparece com nome em cinco superfícies: o H1 (que é o
 * post_title), a aba do navegador e o resultado do Google (o <title>), o cartão
 * compartilhado (og:title), o degrau atual da trilha e o rótulo do cartão que a
 * lista. Em 11/09/2026 mediu-se que SEIS das nove páginas tinham dois nomes: a
 * cabeça publicava "Quem publica a Robometria" enquanto o H1 dizia "Sobre", e o
 * artigo do filtro universal se chamava de dois jeitos diferentes a uma dobra de
 * distância. Ninguém errou: eram dois mapas digitados, cada um certo no seu
 * lugar, e nenhum deles podia corrigir o outro.
 *
 * A saída é a mesma da Aquametria no mesmo dia e a mesma que esta ilha já usou
 * para os números da tela: uma fonte, e as outras derivadas dela. Quem é dono do
 * nome é quem é dono da página — a definição da casca para as cinco dela, e o
 * catálogo da própria ferramenta ou do próprio artigo para as outras quatro, que
 * é para onde o snippet leva a constante de título com que ele cria a página no
 * WordPress. Nada aqui é digitado duas vezes; página nova chega com nome sozinha.
 *
 * Devolve '' para slug que a ilha não publica — e quem chama nunca inventa um.
 */
if ( ! function_exists( 'robometria_casca_nome_da_pagina' ) ) {
function robometria_casca_nome_da_pagina( $slug ) {
	$slug = (string) $slug;

	$nome = robometria_casca_titulo_da_pagina( $slug );
	if ( '' !== $nome ) {
		return $nome;
	}

	foreach ( array( robometria_casca_ferramentas(), robometria_casca_artigos() ) as $catalogo ) {
		foreach ( (array) $catalogo as $item ) {
			if ( isset( $item['slug'], $item['titulo'] ) && $slug === $item['slug'] ) {
				return (string) $item['titulo'];
			}
		}
	}

	return '';
}
}

/**
 * TODA página publicada da ilha, slug => nome. É sobre esta lista que o portão
 * da voz afirma, e é ela que impede a cobrança de valer só para as páginas que
 * existiam no dia em que o teste foi escrito (a cicatriz do cartão que dizia
 * zero, seção 8 do `ARQUIPELAGO.md`).
 */
if ( ! function_exists( 'robometria_casca_nomes_das_paginas' ) ) {
function robometria_casca_nomes_das_paginas() {
	$nomes = array();

	foreach ( robometria_casca_definicao_paginas() as $slug => $def ) {
		$nomes[ $slug ] = $def['titulo'];
	}
	foreach ( array( robometria_casca_ferramentas(), robometria_casca_artigos() ) as $catalogo ) {
		foreach ( (array) $catalogo as $item ) {
			if ( isset( $item['slug'], $item['titulo'] ) ) {
				$nomes[ $item['slug'] ] = (string) $item['titulo'];
			}
		}
	}

	return $nomes;
}
}

/**
 * O QUE VAI NA ABA E NO RESULTADO DO GOOGLE — e até hoje o repositório não
 * escrevia esta linha.
 *
 * O WordPress monta o <title> sozinho: nas páginas internas é o post_title mais
 * o nome do site, e na HOME é o nome do site mais a descrição curta gravada no
 * wp-admin. Medido em 11/09/2026 na home no ar: "Robometria – Compatibilidade de
 * peças e dimensionamento de robô aspirador", 73 caracteres, escrito em
 * vocabulário de dentro da fábrica e num campo que não existe em arquivo nenhum
 * deste repositório. Era o terceiro nome da página mais importante da ilha, e o
 * único que nenhuma bancada podia ver, porque a fonte dele não é nossa.
 *
 * Aqui o repositório assume o campo: o <title> passa a ser o nome canônico da
 * página mais a marca, nas nove, home inclusive. Página que a ilha não conhece
 * continua com o que o WordPress faz — inventar título para endereço que não é
 * nosso seria pior do que não ter.
 *
 * O teto de 65 caracteres não é estética: acima disso o Google corta o título no
 * meio e mostra um pedaço que ninguém escreveu. Por isso o nome cabe em 52 (65
 * menos " – Robometria") e o portão da bancada cobra isso ANTES de publicar, e
 * não depois de alguém ver a reticência no resultado da busca.
 */
if ( ! defined( 'ROBOMETRIA_MARCA' ) ) {
	define( 'ROBOMETRIA_MARCA', 'Robometria' );
}
if ( ! defined( 'ROBOMETRIA_TITULO_SEPARADOR' ) ) {
	define( 'ROBOMETRIA_TITULO_SEPARADOR', ' – ' );
}
if ( ! defined( 'ROBOMETRIA_TITULO_TETO' ) ) {
	define( 'ROBOMETRIA_TITULO_TETO', 65 );
}

if ( ! function_exists( 'robometria_casca_titulo_do_documento' ) ) {
function robometria_casca_titulo_do_documento( $slug ) {
	$nome = robometria_casca_nome_da_pagina( $slug );
	if ( '' === $nome ) {
		return '';
	}

	return $nome . ROBOMETRIA_TITULO_SEPARADOR . ROBOMETRIA_MARCA;
}
}

add_filter( 'document_title_parts', function ( $partes ) {
	$slug   = robometria_casca_slug_atual();
	$titulo = robometria_casca_titulo_do_documento( $slug );
	if ( '' === $titulo ) {
		return $partes;
	}

	/* Duas partes, e só duas: o nome da página e a marca. O núcleo as junta com
	   o separador logo abaixo, e o resultado é exatamente a string que
	   robometria_casca_titulo_do_documento() devolve — que é a que a bancada
	   mede. Na home isso troca as partes que o WordPress usaria (nome do site
	   mais a descrição curta do wp-admin), que é o campo que não mora aqui. */
	unset( $partes );

	return array( 'title' => robometria_casca_nome_da_pagina( $slug ), 'site' => ROBOMETRIA_MARCA );
}, 10 );

add_filter( 'document_title_separator', function ( $sep ) {
	return trim( ROBOMETRIA_TITULO_SEPARADOR );
}, 10 );

/* A MÃE DE TRANSIÇÃO das ferramentas, e o destino de cada uma quando a seção
   nascer. Mora aqui, e não no snippet da ferramenta, porque é decisão de ÁRVORE:
   quem decide onde a página mora é o mapa do site, não quem escreve o cálculo. */
if ( ! function_exists( 'robometria_casca_mae_das_ferramentas' ) ) {
function robometria_casca_mae_das_ferramentas() {
	return 'ferramentas';
}
}

/* A categoria de nível 2 de cada artigo, pelo slug dele (ARVORE.md seção 3).
   Artigo sem categoria declarada aqui não recebe degrau de categoria — e o
   portão reprova, em vez de inventar uma. */
if ( ! function_exists( 'robometria_casca_categoria_do_artigo' ) ) {
function robometria_casca_categoria_do_artigo() {
	return apply_filters( 'robometria_categoria_do_artigo', array(
		'filtro-universal-de-robo-aspirador'          => 'guias-pecas',
		'quantos-m2-o-robo-aspirador-limpa-por-carga' => 'guias-succao',
	) );
}
}

/**
 * Onde esta página mora. Devolve:
 *   papel  => 'raiz' | 'secao' | 'filha'
 *   nivel1 => array( slug, rotulo ) — '' quando não há
 *   nivel2 => array( slug, rotulo ) — array() quando não há
 *   rotulo => o texto do degrau atual (o título, não o nome interno)
 *   irmas  => array( array('slug','rotulo'), ... ), já escolhidas
 * Devolve array() para a home e para página desconhecida — e quem chama não
 * publica trilha nenhuma, que é melhor do que publicar trilha inventada.
 */
if ( ! function_exists( 'robometria_casca_lugar' ) ) {
function robometria_casca_lugar( $slug ) {
	$slug = sanitize_title( (string) $slug );
	if ( '' === $slug || 'inicio' === $slug ) {
		return array();
	}

	if ( in_array( $slug, robometria_casca_paginas_de_raiz(), true ) ) {
		return array(
			'papel'  => 'raiz',
			'nivel1' => array( '', '' ),
			'nivel2' => array(),
			'rotulo' => robometria_casca_titulo_da_pagina( $slug ),
			'irmas'  => array(),
		);
	}

	/* O hub: mãe de transição das ferramentas, e por isso um degrau só. */
	if ( robometria_casca_mae_das_ferramentas() === $slug ) {
		return array(
			'papel'  => 'secao',
			'nivel1' => array( '', '' ),
			'nivel2' => array(),
			'rotulo' => robometria_casca_titulo_da_pagina( $slug ),
			'irmas'  => array(),
		);
	}

	$categorias = robometria_casca_categorias();

	foreach ( robometria_casca_ferramentas() as $f ) {
		if ( empty( $f['slug'] ) || $f['slug'] !== $slug ) {
			continue;
		}
		$mae = robometria_casca_mae_das_ferramentas();
		return array(
			'papel'  => 'filha',
			/* O rótulo da mãe é o NOME dela, lido da fonte única. Estava digitado
			   aqui — e a trilha de uma filha dizia "Ferramentas" enquanto a
			   página mãe, a um clique de distância, se chamava outra coisa. */
			'nivel1' => array( $mae, robometria_casca_nome_da_pagina( $mae ) ),
			'nivel2' => array(),
			'rotulo' => isset( $f['titulo'] ) ? $f['titulo'] : $slug,
			'irmas'  => robometria_casca_irmas( $slug ),
		);
	}

	$cat_artigo = robometria_casca_categoria_do_artigo();
	foreach ( robometria_casca_artigos() as $a ) {
		if ( empty( $a['slug'] ) || $a['slug'] !== $slug ) {
			continue;
		}
		$c2 = isset( $cat_artigo[ $slug ], $categorias[ $cat_artigo[ $slug ] ] )
			? array( $cat_artigo[ $slug ], $categorias[ $cat_artigo[ $slug ] ][1] )
			: array();
		return array(
			'papel'  => 'filha',
			'nivel1' => array( 'guias', 'Guias' ),
			'nivel2' => $c2,
			'rotulo' => isset( $a['titulo'] ) ? $a['titulo'] : $slug,
			'irmas'  => robometria_casca_irmas( $slug ),
		);
	}

	return array();
}
}

/**
 * As irmãs de uma página: MESMA MÃE, no ar, ordenadas por afinidade — primeiro
 * as da mesma categoria de nível 2, depois as demais na ordem do registro. No
 * máximo quatro, como manda o 16.4(c).
 *
 * Página que não existe publicada não entra: irmã é link, e link morto não é
 * cluster. Ferramenta anunciada como 'em-construcao' também não — o hub já a
 * esconde, e irmã que o hub esconde seria a única porta para uma página que a
 * ilha decidiu não oferecer ainda.
 */
if ( ! function_exists( 'robometria_casca_irmas' ) ) {
function robometria_casca_irmas( $slug ) {
	$slug = sanitize_title( (string) $slug );

	$sou_ferramenta = false;
	foreach ( robometria_casca_ferramentas() as $f ) {
		if ( ! empty( $f['slug'] ) && $f['slug'] === $slug ) {
			$sou_ferramenta = true;
			break;
		}
	}

	if ( $sou_ferramenta ) {
		$irmas = array();
		foreach ( robometria_casca_ferramentas() as $f ) {
			if ( empty( $f['slug'] ) || $f['slug'] === $slug ) {
				continue;
			}
			if ( ! isset( $f['estado'] ) || 'publicada' !== $f['estado'] ) {
				continue;
			}
			if ( '' === robometria_casca_url_se_existir( $f['slug'] ) ) {
				continue;
			}
			$irmas[] = array( 'slug' => $f['slug'], 'rotulo' => $f['titulo'] );
		}
		return array_slice( $irmas, 0, 4 );
	}

	$artigos    = robometria_casca_artigos();
	$cat_artigo = robometria_casca_categoria_do_artigo();
	$sou_artigo = false;
	foreach ( $artigos as $a ) {
		if ( ! empty( $a['slug'] ) && $a['slug'] === $slug ) {
			$sou_artigo = true;
			break;
		}
	}
	if ( ! $sou_artigo ) {
		return array();
	}

	$minha = isset( $cat_artigo[ $slug ] ) ? $cat_artigo[ $slug ] : '';
	$perto = array();
	$longe = array();
	foreach ( $artigos as $a ) {
		if ( empty( $a['slug'] ) || $a['slug'] === $slug ) {
			continue;
		}
		if ( '' === robometria_casca_url_se_existir( $a['slug'] ) ) {
			continue;
		}
		$item = array( 'slug' => $a['slug'], 'rotulo' => $a['titulo'] );
		if ( '' !== $minha && isset( $cat_artigo[ $a['slug'] ] ) && $cat_artigo[ $a['slug'] ] === $minha ) {
			$perto[] = $item;
		} else {
			$longe[] = $item;
		}
	}

	return array_slice( array_merge( $perto, $longe ), 0, 4 );
}
}

/* Quantas ferramentas estão REALMENTE abertas ao visitante: anunciadas como
   publicadas E com página existindo. É este o número que a frase de mãe diz, e
   ele é contado — nunca digitado (seção 8 do contrato). */
if ( ! function_exists( 'robometria_casca_conta_ferramentas_no_ar' ) ) {
function robometria_casca_conta_ferramentas_no_ar() {
	$n = 0;
	foreach ( robometria_casca_ferramentas() as $f ) {
		if ( empty( $f['slug'] ) || ! isset( $f['estado'] ) || 'publicada' !== $f['estado'] ) {
			continue;
		}
		if ( '' !== robometria_casca_url_se_existir( $f['slug'] ) ) {
			$n++;
		}
	}
	return $n;
}
}

/**
 * Os degraus da trilha, do topo até a página atual. Cada degrau:
 *   array( 'rotulo' => ..., 'url' => '' quando a página ainda não existe )
 * O último é sempre a página atual e nunca leva URL — é onde a pessoa já está.
 */
if ( ! function_exists( 'robometria_casca_degraus' ) ) {
function robometria_casca_degraus( $slug ) {
	$lugar = robometria_casca_lugar( $slug );
	if ( ! $lugar ) {
		return array();
	}

	$degraus = array( array( 'rotulo' => 'Início', 'url' => home_url( '/' ) ) );

	if ( 'filha' === $lugar['papel'] ) {
		list( $n1_slug, $n1_rotulo ) = $lugar['nivel1'];
		if ( '' !== $n1_slug ) {
			$degraus[] = array(
				'rotulo' => $n1_rotulo,
				'url'    => robometria_casca_url_se_existir( $n1_slug ),
			);
		}
		if ( ! empty( $lugar['nivel2'] ) ) {
			$degraus[] = array(
				'rotulo' => $lugar['nivel2'][1],
				'url'    => robometria_casca_url_se_existir( $lugar['nivel2'][0] ),
			);
		}
	}

	$degraus[] = array( 'rotulo' => $lugar['rotulo'], 'url' => '' );

	return $degraus;
}
}

/* A trilha visível. <nav> com <ol>, porque é navegação e é ordenada; o degrau
   sem URL sai como texto e o atual leva aria-current. */
if ( ! function_exists( 'robometria_casca_trilha_html' ) ) {
function robometria_casca_trilha_html( $slug ) {
	$degraus = robometria_casca_degraus( $slug );
	if ( count( $degraus ) < 2 ) {
		return '';
	}

	$ultimo = count( $degraus ) - 1;
	$html   = '<nav class="rbm-trilha" aria-label="Você está em"><ol>';
	foreach ( $degraus as $i => $d ) {
		$html .= '<li>';
		if ( $i === $ultimo ) {
			$html .= '<span aria-current="page">' . esc_html( $d['rotulo'] ) . '</span>';
		} elseif ( '' !== $d['url'] ) {
			$html .= '<a href="' . esc_url( $d['url'] ) . '">' . esc_html( $d['rotulo'] ) . '</a>';
		} else {
			/* Seção ou categoria ainda não publicada: texto, nunca link morto. */
			$html .= '<span class="rbm-trilha-espera">' . esc_html( $d['rotulo'] ) . '</span>';
		}
		$html .= '</li>';
	}
	$html .= '</ol></nav>';

	return $html;
}
}

/* O BreadcrumbList. Leva os degraus COM URL mais a página atual, e nada mais —
   ver decisão 3 no topo desta seção. */
if ( ! function_exists( 'robometria_casca_trilha_jsonld' ) ) {
function robometria_casca_trilha_jsonld( $slug ) {
	$degraus = robometria_casca_degraus( $slug );
	if ( count( $degraus ) < 2 ) {
		return array();
	}

	$atual = array_pop( $degraus );
	$itens = array();
	$pos   = 0;

	foreach ( $degraus as $d ) {
		if ( '' === $d['url'] ) {
			continue;
		}
		$pos++;
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $pos,
			'name'     => $d['rotulo'],
			'item'     => $d['url'],
		);
	}

	$url_atual = robometria_casca_url_se_existir( $slug );
	$pos++;
	$ultimo = array(
		'@type'    => 'ListItem',
		'position' => $pos,
		'name'     => $atual['rotulo'],
	);
	if ( '' !== $url_atual ) {
		$ultimo['item'] = $url_atual;
	}
	$itens[] = $ultimo;

	if ( count( $itens ) < 2 ) {
		return array();
	}

	return array(
		'@context'        => 'https://schema.org',
		'@type'           => 'BreadcrumbList',
		'itemListElement' => $itens,
	);
}
}

/* O cluster: a frase que linka a mãe (16.4b) e as irmãs (16.4c). */
if ( ! function_exists( 'robometria_casca_veja_tambem_html' ) ) {
function robometria_casca_veja_tambem_html( $slug ) {
	$lugar = robometria_casca_lugar( $slug );
	if ( ! $lugar || 'filha' !== $lugar['papel'] || empty( $lugar['irmas'] ) ) {
		return '';
	}

	$html = '<nav class="rbm-veja" aria-label="Veja também"><h2>Veja também</h2>';

	/* A frase da mãe, só quando a mãe existe. O número é contado. */
	list( $n1_slug, $n1_rotulo ) = $lugar['nivel1'];
	$url_mae = ( '' !== $n1_slug ) ? robometria_casca_url_se_existir( $n1_slug ) : '';
	if ( '' !== $url_mae && robometria_casca_mae_das_ferramentas() === $n1_slug ) {
		$quantas = robometria_casca_conta_ferramentas_no_ar();
		$html   .= '<p class="rbm-veja-mae">Esta é uma das <a href="' . esc_url( $url_mae ) . '">'
			. esc_html( number_format_i18n( $quantas ) ) . ' ferramentas que já estão no ar</a> aqui na Robometria.</p>';
	}

	$html .= '<ul>';
	foreach ( $lugar['irmas'] as $irma ) {
		$url = robometria_casca_url_se_existir( $irma['slug'] );
		if ( '' === $url ) {
			continue;
		}
		$html .= '<li><a href="' . esc_url( $url ) . '">' . esc_html( $irma['rotulo'] ) . '</a></li>';
	}
	$html .= '</ul></nav>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3g. Onde a trilha e o cluster entram na página
 *
 * A trilha entra no lugar do bloco core/post-title, ANTES do H1 — é o "abaixo do
 * header" do 16.3. Se o tema não renderizar esse bloco, ela cai na rede de
 * segurança do the_content, no mesmo padrão que o rodapé já usa desde a 1.0.0:
 * publicar em um lugar só e torcer para o bloco existir seria o defeito do
 * rodapé duplicado, ao contrário.
 *
 * O cluster entra no FIM do the_content, com prioridade 20 — depois dos filtros
 * de texto, então o que ele acrescenta nunca atravessa o escape que transforma
 * "&" em entidade. Ele não tem script hoje; o lugar certo é o lugar certo mesmo
 * quando o defeito ainda não está ali.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_casca_trilha_impressa' ) ) {
function robometria_casca_trilha_impressa( $marcar = false ) {
	static $impressa = false;
	if ( $marcar ) {
		$impressa = true;
	}
	return $impressa;
}
}

add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	$nome = isset( $bloco['blockName'] ) ? $bloco['blockName'] : '';
	if ( 'core/post-title' !== $nome || robometria_casca_trilha_impressa() ) {
		return $conteudo;
	}
	$trilha = robometria_casca_trilha_html( robometria_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $conteudo;
	}
	robometria_casca_trilha_impressa( true );

	return $trilha . $conteudo;
}, 10, 2 );

/* Rede de segurança: sem bloco core/post-title na página, a trilha sai no topo
   do conteúdo. Prioridade 9 para ficar acima de tudo que o conteúdo traz. */
add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() || robometria_casca_trilha_impressa() ) {
		return $html;
	}
	$trilha = robometria_casca_trilha_html( robometria_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $html;
	}
	robometria_casca_trilha_impressa( true );

	return $trilha . $html;
}, 9 );

add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() ) {
		return $html;
	}

	return $html . robometria_casca_veja_tambem_html( robometria_casca_slug_atual() );
}, 20 );

add_action( 'wp_head', function () {
	$dados = robometria_casca_trilha_jsonld( robometria_casca_slug_atual() );
	if ( ! $dados ) {
		return;
	}
	echo '<script type="application/ld+json" id="robometria-trilha-jsonld">'
		. wp_json_encode( $dados ) . '</script>' . "\n";
}, 22 );

/**
 * A HOME É A FERRAMENTA (molde FERRAMENTA do VOZ.md, 11/09/2026).
 *
 * O que ela era até aqui: um manifesto. Primeira frase em terceira pessoa ("A
 * Robometria diz…"), três parágrafos sobre o método antes de qualquer campo, e
 * uma seção inteira de confissão numérica — quantos pares no banco, quantas
 * combinações sem resposta, em que data foi varrido. Tudo verdade, e tudo no
 * lugar errado: a seção 15.2 do contrato diz que número, código, fabricante e
 * data moram na CAMADA DE PROVA (tabela, resultado, JSON-LD, metodologia), e
 * que a home nunca é manifesto. Quem chega aqui está com o robô aberto em cima
 * da mesa e quer saber se a peça do anúncio serve.
 *
 * Então: promessa numa linha, o seletor de marca e modelo, atalhos por tipo de
 * peça, e só depois o apoio. A confissão de cobertura não foi apagada — ela
 * continua inteira na metodologia, que é a página cujo único produto é o rigor,
 * e a home aponta para lá com uma frase que qualquer pessoa entende.
 *
 * O FORMULÁRIO É O DA R1, CHAMADO, não copiado. Cópia de formulário é a mesma
 * armadilha da folha de estilo que este bloco acabou de desfazer: duas metades
 * que ninguém obriga a concordar. Se o banco não tiver chegado às options, a
 * home NÃO desenha um formulário vazio — diz que o seletor está fora do ar e
 * manda para a página da ferramenta, porque ferramenta que devolve vazio
 * parecendo funcionar é pior do que uma que avisa.
 */
add_shortcode( 'robometria_home', function () {
	$html  = '<div class="rbm-bloco">';
	$html .= '<div class="rbm-abertura">';
	$html .= '<p class="rbm-promessa">Diga a marca e o modelo. A gente mostra o que o fabricante declarou que serve no seu robô — filtro, escova, mop ou bateria — e o que ele não declarou.</p>';

	$tem_banco = function_exists( 'robometria_r1_dados' ) && function_exists( 'robometria_r1_formulario' );
	if ( $tem_banco ) {
		$d         = robometria_r1_dados();
		$tem_banco = ! empty( $d['modelos'] );
	}

	if ( $tem_banco ) {
		$html .= robometria_r1_formulario();
		$html .= robometria_casca_atalhos_html();
	} else {
		$html .= '<p class="rbm-nota"><strong>O seletor está fora do ar neste momento.</strong> '
			. robometria_casca_link_html( 'qual-peca-serve-no-meu-robo-aspirador', 'Abrir a página de peças' )
			. '</p>';
	}
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>As duas perguntas que a gente responde</h2>';
	$html .= '<p>Uma é sobre a peça que você já tem na mão. A outra é sobre o robô que você ainda vai escolher.</p>';
	$html .= robometria_casca_cards_html();
	$html .= '<p>' . robometria_casca_link_html( 'ferramentas', 'Ver as duas lado a lado' ) . '</p>';
	$html .= '</div>';

	$artigos = robometria_casca_artigos_html();
	if ( '' !== $artigos ) {
		$html .= '<div class="rbm-secao">';
		$html .= '<h2>Para ler com calma</h2>';
		$html .= '<p>Quando a resposta curta não basta, estes textos mostram de onde ela saiu.</p>';
		$html .= $artigos;
		$html .= '</div>';
	}

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Quando a gente não sabe</h2>';
	$html .= '<p>Tem robô que a gente ainda não consegue responder: o fabricante nunca publicou a lista de peças dele. Quando for o caso do seu, a página diz isso com todas as letras — não chuta um código parecido só para ter o que mostrar.</p>';
	$html .= '<p>O mesmo vale para a palavra "serve". Ela só aparece aqui quando o fabricante escreveu que serve, em algum lugar que dá para conferir. Anúncio de marketplace dizendo "compatível com todos" não conta.</p>';
	$html .= '<p>' . robometria_casca_link_html( 'metodologia', 'Ver como a gente confere, e onde ainda não chegamos' ) . '</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'robometria_ferramentas', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">Duas perguntas, duas respostas: que peça encaixa no seu robô, e quanta sucção ele precisa para a sua casa.</p>';
	$html .= '<p>Elas são diferentes de propósito. A de peças tem resposta binária — o fabricante declarou aquele código para aquele modelo, ou não declarou. A de sucção devolve <strong>faixa</strong>, porque quem publica limiar de pascal para casa com pet é veículo editorial, não fabricante, e os veículos discordam entre si.</p>';
	$html .= robometria_casca_cards_html();

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Por que as duas ainda não cobrem os mesmos robôs</h2>';
	if ( robometria_casca_tem_numeros() ) {
		$html .= '<p>Só ' . robometria_casca_num( $n['as_duas'] ) . ' dos ' . robometria_casca_num( $n['modelos_publicaveis'] ) . ' modelos do banco são atendidos pelas duas ferramentas ao mesmo tempo, e a causa é do mercado, não da ilha: Electrolux e Multi publicam peça com compatibilidade declarada e <strong>não publicam sucção em pascal</strong>; Xiaomi e WAP publicam pascal e <strong>não publicam código de peça</strong>. Enquanto for assim, um robô costuma ter resposta numa ferramenta e recusa na outra, e a tela diz qual é o caso.</p>';
	} else {
		$html .= '<p>A causa é do mercado, não da ilha: Electrolux e Multi publicam peça com compatibilidade declarada e <strong>não publicam sucção em pascal</strong>; Xiaomi e WAP publicam pascal e <strong>não publicam código de peça</strong>. Enquanto for assim, um robô costuma ter resposta numa ferramenta e recusa na outra, e a tela diz qual é o caso.</p>';
		$html .= robometria_casca_sem_medicao_html();
	}
	$html .= '</div>';

	$artigos = robometria_casca_artigos_html();
	if ( '' !== $artigos ) {
		$html .= '<div class="rbm-secao">';
		$html .= '<h2>O texto que acompanha cada ferramenta</h2>';
		$html .= '<p>A ferramenta responde o seu caso; o texto ao lado mostra o que o banco inteiro diz sobre o assunto, com o número medido e a fonte de cada declaração.</p>';
		$html .= $artigos;
		$html .= '</div>';
	}

	$html .= '<p class="rbm-nota"><strong>Em construção não é enfeite.</strong> Uma ferramenta só entra no ar com a fonte de cada declaração conferida, com a tabela de exemplos servida no próprio HTML e com a recusa escrita para os casos em que o fabricante não declarou nada. Preferimos uma ferramenta que se recusa a responder a duas que chutam.</p>';
	$html .= '</div>';

	return $html;
} );

/**
 * A escada de fontes, para a tela. Mesma ordem das vias dos números: banco
 * publicado primeiro, instantâneo do esquema depois. O campo "hoje" não é
 * decoração — é a confissão de que a ilha inteira está apoiada nos níveis 3 e 4.
 */
/**
 * Quantas fontes de cada nível o banco publicado realmente tem.
 *
 * Isto é DERIVADO, e a razão é uma contradição que ficou meses no ar sem que
 * ninguém percebesse: a tabela abaixo dizia "temos hoje: —" no nível 2 porque
 * alguém digitou `false` ali, enquanto quatro fontes do banco se declaravam
 * nível 2. As duas metades não se falavam, então nenhuma podia corrigir a
 * outra. É o mesmo defeito da tese do artigo-âncora (bloco 5): número que é a
 * afirmação da página não pode estar digitado no HTML, porque passa a mentir
 * em silêncio no dia em que o banco muda — e "em silêncio" é o ponto.
 *
 * Agora a coluna conta o banco. Se alguém acrescentar uma fonte de nível 2, a
 * confissão da página se desfaz sozinha, sem ninguém lembrar de reescrevê-la.
 */
if ( ! function_exists( 'robometria_casca_niveis_no_banco' ) ) {
function robometria_casca_niveis_no_banco() {
	$contagem = array();
	foreach ( range( 1, 7 ) as $nivel ) {
		$contagem[ $nivel ] = 0;
	}

	/* O banco cru NÃO viaja para o site (`pecas.json` e `modelos-robo.json` têm
	   publicar=false, e são 245 KB). Quem viaja é a contagem já derivada por
	   ferramentas/gerar-casca-fatos.py, do mesmo jeito que a tese do artigo-âncora
	   viaja em a1-fatos.json. E ela conta TRÊS arquivos, não dois: as seis fontes
	   editoriais que a R2 cita moram em constantes.json, e uma contagem que as
	   ignorasse publicaria "não temos editorial" com cara de medição. */
	$fatos = get_option( 'robometria_dados_casca-fatos' );
	if ( is_array( $fatos ) && ! empty( $fatos['niveis'] ) ) {
		foreach ( $fatos['niveis'] as $degrau ) {
			if ( isset( $degrau['nivel'], $degrau['fontes_no_banco'] )
				&& isset( $contagem[ (int) $degrau['nivel'] ] ) ) {
				$contagem[ (int) $degrau['nivel'] ] = (int) $degrau['fontes_no_banco'];
			}
		}
	}

	return apply_filters( 'robometria_niveis_no_banco', $contagem );
}
}

if ( ! function_exists( 'robometria_casca_escada_de_fontes' ) ) {
function robometria_casca_escada_de_fontes() {
	$no_banco = robometria_casca_niveis_no_banco();
	$escada = array(
		array( 'nivel' => 1, 'origem' => 'medição própria', 'sustenta' => 'Desempenho real: sucção medida, autonomia medida, área coberta medida. É a única origem que poderia publicar desempenho.', 'existe' => false ),
		array( 'nivel' => 2, 'origem' => 'manual do fabricante', 'sustenta' => 'Qualquer campo técnico declarado, e vida útil de peça. Exige manual, lâmina ou página oficial lida direto NO ENDEREÇO DO FABRICANTE. Documento dele guardado por terceiro não conta.', 'existe' => false ),
		array( 'nivel' => 3, 'origem' => 'fabricante por busca', 'sustenta' => 'Campo técnico atribuído ao fabricante e colhido por busca, sem leitura na fonte primária — tanto faz se a página é do domínio dele ou se é um documento dele guardado por terceiro. Vai para a tela com "a confirmar no manual".', 'existe' => true ),
		array( 'nivel' => 4, 'origem' => 'varejo oficial da marca', 'sustenta' => 'Campo técnico transcrito pela loja oficial da própria marca no Brasil. Vai para a tela com "confira a embalagem".', 'existe' => true ),
		array( 'nivel' => 5, 'origem' => 'varejo especializado', 'sustenta' => 'Campo técnico transcrito por varejista ou assistência especializada.', 'existe' => false ),
		array( 'nivel' => 6, 'origem' => 'anúncio de marketplace', 'sustenta' => 'APENAS a existência do item, e sempre rotulado como declaração de terceiro. Nunca sustenta especificação nem a palavra "serve".', 'existe' => true ),
		array( 'nivel' => 7, 'origem' => 'editorial', 'sustenta' => 'Recomendação de faixa (quanto pascal uma casa precisa), sempre com o nome de quem publica. Nunca sustenta especificação de aparelho.', 'existe' => true ),
	);

	/* A coluna "temos hoje" é CONTADA no banco, nunca digitada aqui. O campo
	   'existe' de cada degrau acima é só o valor de partida para quando o Sync
	   ainda não carregou o banco nas options. */
	foreach ( $escada as $i => $degrau ) {
		$n = isset( $no_banco[ $degrau['nivel'] ] ) ? (int) $no_banco[ $degrau['nivel'] ] : 0;
		if ( array_sum( $no_banco ) > 0 ) {
			$escada[ $i ]['existe'] = $n > 0;
		}
		$escada[ $i ]['fontes_no_banco'] = $n;
	}

	return apply_filters( 'robometria_escada_de_fontes', $escada );
}
}

add_shortcode( 'robometria_metodologia', function () {
	$n = robometria_casca_numeros();

	$html  = '<div class="rbm-bloco">';
	$html .= '<p class="rbm-linha-mestra">Só está escrito aqui que uma peça serve quando quem fabricou o seu robô disse que serve. Quando ninguém disse, você lê "não localizamos" — e nunca um palpite.</p>';
	$html .= '<p class="rbm-prova">A régua inteira é essa: declaração do fabricante com endereço e data, transcrita e conferível na própria página. A primeira página de busca para "qual filtro serve no robô X" hoje é, quase inteira, título de anúncio — quem afirma a compatibilidade é o vendedor da peça, sem fonte e sem data. Este site existe para ocupar exatamente esse vazio, e o método abaixo é o que torna isso verificável em vez de prometido.</p>';

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
		$html .= '<td>' . ( $degrau['existe']
			? esc_html( number_format_i18n( $degrau['fontes_no_banco'] ) . ' no banco' )
			: '—' ) . '</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';

	/* A confissão também é contada, não digitada: ela nomeia os degraus vazios
	   e os que sustentam o banco lendo a mesma tabela que o leitor acabou de
	   ver. Escrita à mão, ela dizia "nenhuma fonte de nível 2" enquanto quatro
	   fontes do banco se declaravam nível 2 — e ninguém tinha como perceber. */
	$vazios     = array();
	$sustentam  = array();
	foreach ( robometria_casca_escada_de_fontes() as $degrau ) {
		if ( $degrau['existe'] ) {
			$sustentam[] = $degrau['nivel'] . ' (' . $degrau['origem'] . ')';
		} elseif ( $degrau['nivel'] <= 2 ) {
			$vazios[] = 'nível ' . $degrau['nivel'];
		}
	}
	$html .= '<p class="rbm-nota"><strong>A confissão que essa tabela obriga:</strong> ';
	$html .= $vazios
		? 'a Robometria não tem nenhuma fonte de ' . esc_html( implode( ' nem de ', $vazios ) ) . ' ainda. '
		: 'a Robometria já tem fonte de medição própria ou de manual lido direto. ';
	$html .= 'O banco está apoiado em ' . esc_html( implode( ', ', $sustentam ) ) . ' — e é por isso que cada campo carrega o canal por onde foi colhido. ';
	$html .= 'Ler os manuais em PDF direto, no endereço do fabricante, é o próximo degrau, e ele está na fila. ';
	$html .= '<strong>Manual do fabricante guardado por terceiro não conta como manual lido:</strong> uma origem tem três elos — quem escreveu, quem guarda e como nós lemos —, e o nível é o do elo mais fraco. Em 11/09/2026 quatro fontes desta ilha desceram de nível por essa regra.</p></div>';

	$html .= '<div class="rbm-secao"><h2>4. O que medimos sobre a nossa própria cobertura</h2>';
	if ( robometria_casca_tem_numeros() ) {
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
		/* A RÉGUA DO PAR, NA PRÓPRIA FRASE. O número da linha "pares" caiu de 33
		   para 32 em 11/09/2026, quando ele deixou de ser digitado: o par que
		   sobrava aponta para um modelo excluído do banco, e o site nunca o serve.
		   Dizer aqui o que conta como par é o que impede o próximo leitor — e a
		   próxima Sentinela — de achar que a contagem encolheu por descuido. */
		$html .= '<p class="rbm-nota">Um par só é contado quando as duas pontas estão publicadas: a peça e o modelo. Peça que declara compatibilidade com um modelo que a gente não publica não vira número aqui, porque não vira resposta em tela nenhuma.</p>';
	} else {
		$html .= '<p>Contar itens do banco não diz se a ferramenta responde. Por isso a entrada é varrida de ponta a ponta, e o resultado é publicado mesmo quando é desconfortável.</p>';
		$html .= robometria_casca_sem_medicao_html();
	}
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
	$html .= '<p class="rbm-linha-mestra">Duas perguntas sobre o seu robô, e só elas: que peça encaixa nele, e quanta sucção ele precisa.</p>';
	$html .= '<p class="rbm-prova">Publicamos qual peça o fabricante declarou para qual modelo, e quanta sucção e quanto tempo a sua casa pede — com uma regra única: todo número cita a fonte e leva a data em que foi verificado. Aqui não tem "melhores do ano".</p>';

	$html .= '<div class="rbm-secao"><h2>Por que existe</h2>';
	$html .= '<p>A busca comercial do nicho ("melhor robô aspirador") está tomada por listas de compra, e nós não disputamos essa. A busca que ninguém responde direito é a de quem <strong>já tem</strong> o robô: qual filtro serve, qual escova lateral encaixa, qual bateria é a certa. Hoje quem responde isso é o título do anúncio de quem vende a peça. Não existe comparador entre marcas com fonte e data — e é esse buraco que este site ocupa.</p></div>';

	$html .= '<div class="rbm-secao"><h2>Como é feita</h2>';
	$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é o método e a procedência do dado, e os dois ficam abertos para conferência em cada página. Ferramentas e conteúdo são versionados em repositório público antes de chegarem ao site, e o banco tem um verificador que reprova registro sem fonte, sem data ou com divergência não resolvida — o que está no ar passou por ele.</p>';
	$html .= robometria_casca_tem_numeros()
		? '<p>Estado de hoje, sem arredondar para cima: ' . robometria_casca_num( $n['marcas'] ) . ' marcas, ' . robometria_casca_num( $n['modelos_publicaveis'] ) . ' modelos de robô e ' . robometria_casca_num( $n['pares_declarados'] ) . ' pares peça × modelo declarados pelo fabricante. Nenhum par inferido.</p>'
		: robometria_casca_sem_medicao_html();
	$html .= '</div>';

	/* BLOCO DE RECUSA, marcado no markup pelo mesmo motivo do da divulgação de
	   afiliados: a frase legítima que recusa a escassez inventada usa as MESMAS
	   palavras que a seção 7 do contrato proíbe, e quem decide qual é qual é a
	   estrutura, nunca a vizinhança (cicatriz do Clube do Mosaico, 11/09/2026).
	   Todo item daqui abre negando, e a bancada conta um a um. */
	$html .= '<div class="rbm-secao"><h2>O que a Robometria não faz</h2>';
	$html .= '<ul class="rbm-lista rbm-recusa">';
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
	$html .= '<p class="rbm-linha-mestra">Quando houver link de loja aqui, ele será link de afiliado: se você comprar por ele, a gente recebe uma comissão da loja, sem custo nenhum para você.</p>';
	$html .= '<p>Isso significa que, se você comprar por ele, a Robometria pode receber uma comissão da loja, sem custo adicional para você. Os programas usados são os de afiliados da Shopee e do Mercado Livre.</p>';

	$html .= '<div class="rbm-secao"><h2>O que a comissão nunca muda</h2>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li><strong>A ordem da lista.</strong> Primeiro entra quem cumpre todas as condições declaradas pelo fabricante; depois, entre os que cumprem, quem é tecnicamente mais adequado. Ter link de loja só desempata entre itens equivalentes — e nunca comparamos taxa de comissão entre programas.</li>';
	$html .= '<li><strong>Quem aparece.</strong> Produto que não passa na condição declarada não sobe para o topo por ter link; ele vai para uma seção separada, abaixo, dizendo em qual condição falhou.</li>';
	$html .= '<li><strong>O dado técnico.</strong> A fonte de uma especificação é sempre o fabricante. Um link de loja nunca substitui o endereço de origem do dado.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="rbm-secao"><h2>Preço</h2>';
	$html .= '<p>Nenhum preço aqui é apresentado como o preço de agora. Ou a página não traz preço, ou traz a faixa com a data em que ela foi coletada. Preço muda mais rápido do que qualquer página estática consegue acompanhar, e fingir o contrário seria enganar.</p></div>';

	$html .= '<div class="rbm-secao"><h2>O que quer dizer "link de loja em breve"</h2>';
	$html .= '<p>Quando uma peça aparece no resultado sem botão de compra, o lugar dele fica reservado com esse aviso. Não é descuido: é o estado real daquele item. A peça entrou no banco porque o fabricante declarou que ela serve no seu robô, e é isso que a página promete responder — o link de loja vem depois, um a um, e leva tempo.</p>';
	$html .= '<p>Esconder o bloco enquanto o link não existe seria pior. A página ficaria com um único endereço clicável, o da declaração do fabricante, e mandaria você comprar na loja da própria marca — onde a Robometria não ganha nada e você não compara preço com ninguém.</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao"><h2>Por que dois programas, e não um</h2>';
	$html .= '<p>Cada marketplace vende as marcas que vende. Peça de reposição de robô aspirador de marca de loja especializada costuma não existir num deles e existir no outro, e ficar com um só significaria deixar de fora justamente a peça certa. Quando o mesmo item está nos dois, o link sai para a Shopee; o Mercado Livre entra onde a Shopee não tem. Isso não é escolha por comissão — a taxa de um programa nunca é comparada com a do outro para decidir nada.</p>';
	$html .= '</div>';

	/* BLOCO DE RECUSA, marcado no markup e não deduzido pela vizinhança das
	   palavras (cicatriz do Clube do Mosaico, 11/09/2026, seção 8 do contrato).
	   Toda frase daqui ABRE negando: é o que separa a recusa legítima de uma
	   promessa escondida dentro de um bloco com nome de recusa. */
	$html .= '<div class="rbm-secao"><h2>O que você nunca vai ver aqui</h2>';
	$html .= '<ul class="rbm-lista rbm-recusa">';
	$html .= '<li>Não publicamos relógio de contagem regressiva nem "últimas unidades".</li>';
	$html .= '<li>Não publicamos selo de "mais vendido": a Robometria não mede venda de ninguém.</li>';
	$html .= '<li>Não publicamos nota nem estrela de avaliação que a gente não tenha medido.</li>';
	$html .= '<li>Não compramos pelos nossos próprios links, e ninguém da casa compra.</li>';
	$html .= '</ul></div>';

	/* A frase abaixo é CONTADA no banco, não digitada — ver robometria_casca_numeros(). */
	$n = robometria_casca_numeros();
	if ( ! robometria_casca_tem_numeros() ) {
		$html .= robometria_casca_sem_medicao_html();
	} else {
		$html .= '<p class="rbm-nota"><strong>Estado de hoje:</strong> ';
		if ( $n['com_link'] < 1 ) {
			$html .= 'nenhum dos ' . robometria_casca_num( $n['itens_publicaveis'] ) . ' itens do banco tem link de loja ainda — os ' . robometria_casca_num( $n['esperando_link'] ) . ' estão esperando. ';
		} else {
			$html .= robometria_casca_num( $n['com_link'] ) . ' dos ' . robometria_casca_num( $n['itens_publicaveis'] ) . ' itens do banco já têm link de loja, e ' . robometria_casca_num( $n['esperando_link'] ) . ' ainda esperam. ';
		}
		$html .= 'Esta página existe desde o primeiro dia porque a divulgação precisa estar publicada <em>antes</em> do primeiro link, não depois.</p>';
	}
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Estrutura do site: páginas, página inicial e limpeza do tema padrão
 * ------------------------------------------------------------------------- */

/**
 * O TÍTULO DE UMA PÁGINA É O H1 DELA, e o da raiz era a palavra "Início"
 * (despacho da Sentinela, 11/09/2026, item 2).
 *
 * Medido em 11/09 às 14h40Z na home no ar: `[...document.querySelectorAll('h1')]`
 * devolvia `["Início"]`. É o H1 da página que disputa a marca, e ele não nomeava
 * nem o assunto da ilha nem nada que alguém digite. "Início" é o nome do LUGAR
 * na estrutura do WordPress, não o nome do que a página responde.
 *
 * As outras quatro continuam com o título que tinham: a seção 15.5 do contrato
 * manda reescrever home e header primeiro, e cada página existente depois, ao
 * passar pela ronda. Trocar tudo de uma vez seria mexer em texto de página
 * posicionada sem a Sentinela ter olhado (seção 12.1).
 */
if ( ! function_exists( 'robometria_casca_definicao_paginas' ) ) {
function robometria_casca_definicao_paginas() {
	return array(
		/* OS NOMES, e por que estes.
		 *
		 * Quatro destas cinco páginas se chamavam pelo nome da gaveta —
		 * "Ferramentas", "Metodologia", "Sobre", "Divulgação de afiliados" —
		 * enquanto a cabeça da MESMA página já publicava, desde a 1.2.0, o nome
		 * na voz do VOZ.md. Não é rebatismo: é a divergência sendo desfeita para
		 * o lado que já estava escrito, e o nome da gaveta some porque a seção
		 * 14.5 do contrato pede o que a pessoa digita, não o nome interno.
		 *
		 * A home encurtou de 63 para 50 caracteres e nada da promessa se perdeu:
		 * as duas metades continuam lá. O motivo é o teto do <title> — 63 mais
		 * " – Robometria" dá 76, e o Google corta em ~65 mostrando um pedaço que
		 * ninguém escreveu. */
		'inicio'                  => array( 'titulo' => 'Seu robô aspirador: qual peça serve, quanta sucção', 'conteudo' => '[robometria_home]' ),
		'ferramentas'             => array( 'titulo' => 'As duas ferramentas', 'conteudo' => '[robometria_ferramentas]' ),
		'metodologia'             => array( 'titulo' => 'Como a gente decide o que publicar', 'conteudo' => '[robometria_metodologia]' ),
		'sobre'                   => array( 'titulo' => 'Quem publica este site', 'conteudo' => '[robometria_sobre]' ),
		'divulgacao-de-afiliados' => array( 'titulo' => 'Como este site ganha dinheiro', 'conteudo' => '[robometria_afiliados]' ),
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

		/* O TÍTULO TAMBÉM É NOSSO, e até a v1.2.0 não era sincronizado: a página
		   nascia com o título da definição e ficava com ele para sempre. Foi por
		   isso que o H1 da raiz continuou sendo "Início" depois de a casca já ter
		   mudado três vezes. Só mexemos em página com a nossa marca, e o
		   post_name NÃO é tocado — a URL da página não muda com o título, que é o
		   que a seção 12.1 do contrato protege. */
		if ( $nossa && (string) $pagina->post_title !== (string) $def['titulo'] ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => $def['titulo'] ) );
			$relato[] = 'página ' . $slug . ': título atualizado (#' . $pid . ')';
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

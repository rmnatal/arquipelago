<?php
/**
 * Verificacao MEDIDA da casca do Clube do Mosaico, sem site e sem rede.
 *
 *   php ferramentas/teste-casca.php .
 *
 * E a secao 8 do ARQUIPELAGO.md executada onde da para executa-la hoje: o
 * gateway da rede das rotinas respondeu 403 ao CONNECT para
 * clubedomosaico.com.br em 11/09/2026, entao a alternativa a este arquivo seria
 * marcar publicar=true por fe. Cada afirmacao abaixo e um numero, nunca uma
 * impressao — e o teste sai com codigo 1 quando qualquer uma falha.
 *
 * AS TRES REGRAS DE MEDICAO DA SECAO 8, e como elas aparecem aqui:
 *
 *   1. QUEM CONFERE ESCREVE A PROPRIA REGUA. Nenhuma afirmacao sobre numero
 *      chama a funcao da casca para descobrir o que esperar: os esperados sao
 *      recontados dos arquivos JSON commitados, aqui dentro. Se a casca e o
 *      banco se separarem, os dois lados nao erram juntos.
 *   2. GRADE TEM QUE INCLUIR A BORDA. A Loja e medida nos DOIS estados — sem
 *      peca cadastrada (o de hoje) e com peca —, porque um teste que so olhasse
 *      o estado vazio aprovaria uma vitrine que nunca mostra peca nenhuma.
 *   3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. Tudo que e sobre
 *      texto visivel e medido dentro de <main>, nunca no HTML completo — e o
 *      mesmo erro de contar &#038; na pagina inteira em vez de dentro do
 *      <script>.
 *
 * O que ele NAO substitui: a conferencia da revisao aplicada no /status depois
 * do Sync (secao 4). Este arquivo prova que o codigo esta certo; so o /status
 * prova que ele esta NO AR.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function cdm_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-64s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-64s %s\n", $rotulo, $medida );
	return false;
}

/** So os blocos <script>, que e onde a contagem de &#038; vale (secao 8). */
function cdm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/** O CORPO da pagina — onde toda afirmacao sobre texto visivel e medida. */
function cdm_corpo( $html ) {
	if ( preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ) {
		return $m[1];
	}
	return '';
}

$GLOBALS['__paginas'] = array(
	'loja'                    => true,
	'materiais/como-sabemos'  => true,
	'materiais'               => true,
	'como-fazer'              => true,
	'sobre'                   => true,
	'contato'                 => true,
	'divulgacao-de-afiliados' => true,
	'privacidade'             => true,
	'materiais/qual-cola-usar-no-mosaico' => true,
	'materiais/quantas-pastilhas-para-mosaico' => true,
);

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );

$paginas = array(
	'cdm_home', 'cdm_loja', 'cdm_materiais', 'cdm_como_sabemos', 'cdm_como_fazer',
	'cdm_sobre', 'cdm_contato', 'cdm_afiliados', 'cdm_privacidade',
	/* AS DUAS FERRAMENTAS entram na lista da casca de proposito: sao trinta e
	   tantos portoes (voz, prova, escassez, trilha, arvore, pagina fina,
	   entidade dentro de <script>) que ja existem e que toda pagina nova tem
	   que passar tambem. O que e SO de cada uma — a regua de elegibilidade da
	   F2, a aritmetica da F1 e a varredura da entrada inteira das duas — mora
	   em ferramentas/teste-f2.php e ferramentas/teste-f1.php, separados. */
	'cdm_f2', 'cdm_f1',
	/* AS QUATRO PAGINAS DO GUIA (bloco 4c, 02/10/2026) entram pelo mesmo motivo
	   que as duas ferramentas: os trinta e tantos portoes desta bancada — voz,
	   prova, escassez, trilha, arvore, pagina fina, entidade dentro de <script>
	   — valem para toda pagina da ilha, e e aqui que eles moram. O que e SO
	   delas (a conta de cobertura, o relogio, a prestacao de contas dos dez
	   produtos, a 16.4(a) da mae) mora em ferramentas/teste-guia.php.
	      E HA UMA RAZAO A MAIS, medida nesta mesma execucao: a contagem de
	   pagina orfa da secao 26 so enxerga link que sai de uma pagina DESTA
	   lista. Sem a mae aqui, as tres filhas de nivel 3 apareciam com ZERO
	   link interno — orfas no numero, linkadas no site. */
	'cdm_guia_acabamento', 'cdm_guia_selador', 'cdm_guia_verniz', 'cdm_guia_impermeabilizante',
);

/* AS PAGINAS DE CONSULTA DE PRODUTO (secao 30, 09/10/2026) entram DERIVADAS do
   registro do snippet, e nao escritas a mao: a familia cresce por coleta, e
   lista copiada envelhece calada. Elas entram pelos dois motivos que o
   comentario do Guia acima ja nomeia, e o segundo foi MEDIDO nesta mesma
   execucao: sem as oito nesta lista, a contagem de pagina orfa da secao 26
   acusou QUATRO delas com UM unico link interno — orfas no numero e linkadas no
   site —, porque a unica fonte de link que a bancada enxergava era a mae. Com as
   oito aqui, as sete irmas de cada uma passam a contar, que e a malha que o
   despacho pediu.

   O QUE E SO DELAS (o numero proprio recontado do JSON cru, o piso de tres
   ofertas, a ordem do bloco de compra, o ItemList) mora em
   ferramentas/teste-produto.php, separado — aqui valem os trinta e tantos
   portoes que sao de TODA pagina desta ilha. */
foreach ( cdm_produto_registro() as $cdm_pid => $cdm_pp ) {
	$GLOBALS['__paginas'][ $cdm_pp['slug'] ] = true;
	$paginas[] = 'cdm_produto_' . $cdm_pid;
}
unset( $cdm_pid, $cdm_pp );

echo "Clube do Mosaico — verificacao da casca " . CDM_CASCA_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria: script dentro do
 *    retorno do shortcode. Aqui ele e medido em cada pagina.
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";

/**
 * UM PROCESSO POR PAGINA, e isto nao e zelo: e a terceira cicatriz da mesma
 * familia no Arquipelago. A casca tem um `static` legitimo em
 * cdm_casca_rodape_impresso() e outro em cdm_casca_marca_html(), que existem
 * para o rodape e o logotipo nao sairem duas vezes na MESMA pagina. No site um
 * processo e uma requisicao e eles estao certos. Numa bancada que monta nove
 * paginas em sequencia, eles fazem o rodape aparecer na primeira e sumir nas
 * oito seguintes — e a medicao mede oito paginas sem rodape sem acusar erro
 * nenhum. Foi exatamente assim que a Robometria mediu 915 KB do que no ar tem
 * 960 KB, em 11/09/2026. Custa segundos; medir a metade errada custa um bloco.
 */
function cdm_render_em_processo_proprio_modo( $raiz, $tag, $modo = 'hoje' ) {
	$saida = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $tag ) . ' ' . escapeshellarg( $modo ) . ' 2>/dev/null', $saida, $codigo );
	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

function cdm_render_em_processo_proprio( $raiz, $tag ) {
	return cdm_render_em_processo_proprio_modo( $raiz, $tag, 'hoje' );
}

$html_por_pagina = array();
foreach ( $paginas as $tag ) {
	cdm_teste_rebobinar();
	cdm_teste_pagina( $tag );
	$html_por_pagina[ $tag ] = cdm_render_em_processo_proprio( $raiz, $tag );
	$cru = $GLOBALS['__retorno_shortcode'];
	cdm_ok( false === stripos( $cru, '<script' ), "[$tag] sem <script> no retorno do shortcode" );
	cdm_ok( false === stripos( $cru, '<style' ), "[$tag] sem <style> no retorno do shortcode" );
	cdm_ok( '' !== $html_por_pagina[ $tag ], "[$tag] o render em processo proprio devolveu pagina",
		strlen( $html_por_pagina[ $tag ] ) . ' bytes' );
}

/* ---------------------------------------------------------------------------
 * 2. Zero &#038; DENTRO de <script>. Contar na pagina inteira e teste ERRADO.
 * ------------------------------------------------------------------------- */

echo "\n2. Entidades dentro de <script> (secao 8, item 2)\n";
foreach ( $paginas as $tag ) {
	$scripts = cdm_scripts( $html_por_pagina[ $tag ] );
	$n = substr_count( $scripts, '&#038;' );
	cdm_ok( 0 === $n, "[$tag] zero &#038; dentro de <script>", "achados: $n" );
}

/* ---------------------------------------------------------------------------
 * 3. Menu: links no HTML servido, botao acessivel, aria-controls que aponta
 *    para um id que existe (secao 6).
 * ------------------------------------------------------------------------- */

echo "\n3. Menu hamburguer (secao 6)\n";
$home = $html_por_pagina['cdm_home'];
preg_match( '#<button[^>]*class="cdm-nav-botao"[^>]*>#i', $home, $mb );
$botao = isset( $mb[0] ) ? $mb[0] : '';
cdm_ok( '' !== $botao, 'botao do menu e <button> de verdade' );
cdm_ok( false !== strpos( $botao, 'aria-expanded="false"' ), 'botao nasce com aria-expanded="false"' );
preg_match( '#aria-controls="([^"]+)"#', $botao, $mc );
$controlado = isset( $mc[1] ) ? $mc[1] : '';
cdm_ok( '' !== $controlado, 'botao declara aria-controls', $controlado );
cdm_ok( '' !== $controlado && false !== strpos( $home, 'id="' . $controlado . '"' ), 'o id de aria-controls existe no HTML servido' );
preg_match( '#<nav class="cdm-nav"[^>]*>(.*?)</nav>#is', $home, $mn );
$nav = isset( $mn[1] ) ? $mn[1] : '';
$links = preg_match_all( '#<a href="https://clubedomosaico\.com\.br/[^"]+"#', $nav );
cdm_ok( 4 === $links, 'os 4 links do menu sao <a href> reais dentro de <nav>', "achados: $links" );
cdm_ok( false !== strpos( $home, 'aria-label="Navegação principal"' ), '<nav> tem rotulo acessivel' );
/* A Loja vem primeiro: e o unico motor de margem cheia, e a secao 9 manda por
   na frente o caminho que termina em compra. */
cdm_ok( preg_match( '#<li>.*?>Loja<#', $nav ) && strpos( $nav, '>Loja<' ) < strpos( $nav, '>Materiais<' ),
	'Loja e o primeiro item do menu (secao 9: intencao de compra na frente)' );

/* ---------------------------------------------------------------------------
 * 4. Favicon proprio no lugar do icone do WordPress (secao 6).
 *
 * A regua e propria: o base64 esperado e recalculado do PNG commitado, aqui.
 * Conferir so "nao esta vazio" deixaria passar um icone de outra ilha.
 * ------------------------------------------------------------------------- */

echo "\n4. Favicon proprio (secao 6)\n";
cdm_ok( false === strpos( $home, 'icone-do-wordpress.png' ), 'o icone padrao do WordPress FOI removido do wp_head' );
cdm_ok( false !== strpos( $home, 'rel="icon" type="image/png" sizes="32x32"' ), 'icone PNG proprio no wp_head' );
cdm_ok( false !== strpos( $home, 'rel="apple-touch-icon"' ), 'apple-touch-icon declarado' );
cdm_ok( false !== strpos( $home, '<meta name="theme-color" content="#FFFFFF">' ), 'theme-color acompanha o cabecalho claro' );

$png_commitado = @file_get_contents( $raiz . '/identidade/logo/favicon-32.png' );
cdm_ok( false !== $png_commitado && "\x89PNG\r\n\x1a\n" === substr( $png_commitado, 0, 8 ),
	'identidade/logo/favicon-32.png existe e e PNG', strlen( (string) $png_commitado ) . ' bytes' );
cdm_ok( base64_encode( (string) $png_commitado ) === CDM_CASCA_ICONE_PNG_32,
	'o base64 do snippet e exatamente o PNG commitado (gerar-favicon.php rodou)' );

/* ---------------------------------------------------------------------------
 * 4b. A TAG DO GA4 (secao 5 do ARQUIPELAGO.md, despacho de 12/09/2026).
 *
 * A REGUA E DESTE ARQUIVO: o ID esperado esta escrito LITERAL abaixo, copiado do
 * PROMPT.md da ilha, e nao lido de CDM_CASCA_GA4_ID. Ler a constante seria
 * afirmar que a casca concorda consigo mesma — que e sempre verdade. O dia em
 * que alguem copiar esta casca para a ilha 4 e esquecer de trocar o ID, e este
 * numero digitado aqui que acusa.
 *
 * E A POSICAO E MEDIDA, nao so a presenca: o despacho pede a tag o mais cedo
 * possivel E proibe que ela passe na frente do title, da meta descricao e do
 * JSON-LD. Portao que so pergunta "existe gtag na pagina?" fica verde com a tag
 * no lugar errado, que e exatamente o unico jeito de esta mudanca fazer mal.
 * ------------------------------------------------------------------------- */

echo "\n4b. Tag do GA4 (secao 5)\n";

/* Copiado do PROMPT.md da ilha, a mao. Nao trocar por CDM_CASCA_GA4_ID. */
$ga4_esperado = 'G-0K5PY39HV7';

foreach ( $paginas as $tag ) {
	$html   = $html_por_pagina[ $tag ];
	$cabeca = preg_match( '#<head\b[^>]*>(.*?)</head>#is', $html, $mh ) ? $mh[1] : '';

	cdm_ok( 1 === substr_count( $cabeca, 'www.googletagmanager.com/gtag/js' ),
		"[$tag] a tag do GA4 sai UMA vez, dentro do <head>",
		substr_count( $cabeca, 'www.googletagmanager.com/gtag/js' ) . 'x' );
	cdm_ok( 1 === substr_count( $html, 'www.googletagmanager.com/gtag/js' ),
		"[$tag] e nao sai uma segunda vez no resto da pagina" );
	cdm_ok( false !== strpos( $cabeca, 'id=' . $ga4_esperado ),
		"[$tag] o ID servido e o desta ilha, e nao o de outra" );
	cdm_ok( preg_match( '#<script async src="https://www\.googletagmanager\.com/gtag/js\?id=' . preg_quote( $ga4_esperado, '#' ) . '"></script>#', $cabeca ),
		"[$tag] o script de terceiro vai com async (22.4)" );
	cdm_ok( false !== strpos( $cabeca, "gtag('config','" . $ga4_esperado . "')" ),
		"[$tag] o config nomeia o mesmo ID do src" );

	/* ORDEM. Cada um destes e uma linha do despacho virada em numero. */
	$p_gtag  = strpos( $html, 'www.googletagmanager.com/gtag/js' );
	$p_title = strpos( $html, '<title>' );
	$p_org   = strpos( $html, 'id="cdm-casca-jsonld"' );
	$p_fonte = strpos( $html, 'fonts.googleapis.com' );

	cdm_ok( false !== $p_title && false !== $p_gtag && $p_title < $p_gtag,
		"[$tag] a tag NAO entra antes do <title>" );
	cdm_ok( false !== $p_org && $p_org < $p_gtag,
		"[$tag] a tag NAO entra antes do JSON-LD Organization" );
	cdm_ok( false !== $p_fonte && $p_gtag < $p_fonte,
		"[$tag] mas entra ANTES da folha de fontes, que e o recurso bloqueante" );

	/* A trilha so existe fora da home (16.3), entao a afirmacao muda de lado
	   junto com ela — em vez de ser pulada, que deixaria o caso sem medida. */
	$p_trilha = strpos( $html, 'id="cdm-trilha-jsonld"' );
	if ( 'cdm_home' === $tag ) {
		cdm_ok( false === $p_trilha, "[$tag] a home nao tem trilha, e a ordem acima ja basta" );
	} else {
		cdm_ok( false !== $p_trilha && $p_trilha < $p_gtag,
			"[$tag] a tag NAO entra antes do BreadcrumbList" );
	}

	/* O UNICO SCRIPT DE TERCEIRO. Qualquer <script src> apontando para fora do
	   dominio da ilha que nao seja o gtag reprova aqui — e a regra do despacho
	   escrita como medida, em vez de como promessa no cabecalho do arquivo. */
	preg_match_all( '#<script[^>]+src="(https?://[^"]+)"#i', $html, $ms );
	$externos = array();
	foreach ( $ms[1] as $src ) {
		if ( false === strpos( $src, 'clubedomosaico.com.br' ) ) {
			$externos[] = $src;
		}
	}
	cdm_ok( 1 === count( $externos ) && false !== strpos( $externos[0], 'googletagmanager.com' ),
		"[$tag] o gtag e o UNICO script de terceiro da pagina",
		count( $externos ) . ' externo(s)' );

	/* A cicatriz da ilha, aplicada ao bloco novo: &#038; dentro de <script>
	   quebra o JavaScript em silencio. A URL do gtag tem um parametro so
	   justamente para nao ter ampersand — e isto mede que continua assim. */
	cdm_ok( false === strpos( $cabeca, 'gtag/js?id=' . $ga4_esperado . '&' ),
		"[$tag] a URL do gtag nao ganhou um segundo parametro (e com ele o &#038;)" );
}

/* AS DUAS BORDAS DA GUARDA DE ID. Sem elas, uma funcao que devolvesse string
   vazia SEMPRE passaria em tudo acima se a constante fosse a unica entrada
   possivel — e uma que imprimisse QUALQUER coisa tambem. */
cdm_ok( '' === cdm_casca_ga4_html( '' ),
	'borda: com ID vazio a funcao nao imprime meia tag' );
cdm_ok( '' === cdm_casca_ga4_html( 'lixo' ),
	'borda: com ID fora do formato a funcao nao imprime nada' );
cdm_ok( '' === cdm_casca_ga4_html( 'g-0k5py39hv7' ),
	'borda: minuscula nao passa (o Google emite maiuscula)' );
cdm_ok( '' !== cdm_casca_ga4_html( 'G-ABC123' ),
	'borda: e um ID BEM formado passa — senao "nunca imprime" viraria a trava' );
cdm_ok( false !== strpos( cdm_casca_ga4_html( 'G-ABC123' ), "gtag('config','G-ABC123')" ),
	'borda: e o que ela imprime e o ID que recebeu, nao o da constante' );

/* A PROMESSA DA PAGINA DE PRIVACIDADE. Ela estava escrita com todas as letras e
   venceu hoje; medir que a frase NOVA chegou sem medir que a VELHA saiu deixaria
   a pagina dizendo as duas coisas ao mesmo tempo. */
$corpo_privacidade = cdm_corpo( $html_por_pagina['cdm_privacidade'] );
cdm_ok( false !== strpos( $corpo_privacidade, 'Google Analytics 4' ),
	'privacidade: a pagina diz que o site mede audiencia com GA4' );
cdm_ok( false !== strpos( $corpo_privacidade, '12 de setembro de 2026' ),
	'privacidade: com a data em que a medicao comecou' );
cdm_ok( false === strpos( $corpo_privacidade, 'Se um dia houver' ),
	'privacidade: a promessa antiga ("se um dia houver") SAIU da pagina' );
cdm_ok( false !== strpos( $corpo_privacidade, 'remarketing' ),
	'privacidade: e o que continua nao acontecendo continua escrito' );

/* ---------------------------------------------------------------------------
 * 5. JSON-LD valido em toda pagina (secao 5.3).
 * ------------------------------------------------------------------------- */

echo "\n5. JSON-LD (secao 5.3)\n";
foreach ( $paginas as $tag ) {
	preg_match( '#<script type="application/ld\+json"[^>]*>(.*?)</script>#is', $html_por_pagina[ $tag ], $mj );
	$bruto = isset( $mj[1] ) ? $mj[1] : '';
	$dados = json_decode( $bruto, true );
	$tipos = array();
	if ( is_array( $dados ) && isset( $dados['@graph'] ) ) {
		foreach ( $dados['@graph'] as $no ) {
			$tipos[] = isset( $no['@type'] ) ? $no['@type'] : '?';
		}
	}
	cdm_ok(
		is_array( $dados ) && in_array( 'Organization', $tipos, true ) && in_array( 'WebSite', $tipos, true ),
		"[$tag] JSON-LD decodifica e traz Organization + WebSite",
		implode( '+', $tipos )
	);
}
/* sameAs so entra quando os perfis da artesa chegarem: perfil inventado seria
   exatamente a fabricacao que o Arquipelago existe para nao cometer. */
cdm_ok( false === strpos( $home, '"sameAs"' ), 'nenhum sameAs inventado no Organization' );
cdm_ok( false !== strpos( $home, '"logo":"' . CDM_CASCA_LOGO_URL . '"' ), 'o logo do Organization e o arquivo oficial' );

/* ---------------------------------------------------------------------------
 * 6. Corpo comeca pelo texto, nunca por metadado (secao 8, item 3).
 * ------------------------------------------------------------------------- */

echo "\n6. Corpo da pagina (secao 8, item 3)\n";
foreach ( $paginas as $tag ) {
	$corpo = trim( cdm_corpo( $html_por_pagina[ $tag ] ) );
	cdm_ok( '' !== $corpo && 0 !== strpos( $corpo, '---' ) && 0 !== strpos( $corpo, 'ilha:' ),
		"[$tag] corpo nao comeca por metadado YAML", strlen( $corpo ) . ' bytes' );
}

/* ---------------------------------------------------------------------------
 * 7. A MARCA E O ARQUIVO ENTREGUE, INTEIRO, e nao um desenho feito aqui.
 *
 * E a regra propria desta ilha: o PROMPT.md proibe reconstruir, redesenhar ou
 * vetorizar o logo, e proibe escrever "clube do mosaico" em texto ao lado dele,
 * porque o arquivo ja traz o wordmark. As duas primeiras ilhas desenham o
 * simbolo em SVG; aqui isso seria defeito.
 *
 * A REGUA E DESTE ARQUIVO, nao do snippet (secao 8: quem confere escreve a
 * propria regua). A URL, a altura e a largura abaixo estao escritas LITERAIS,
 * copiadas do despacho do Raphael de 11/09 e da biblioteca de midia dele — se
 * alguem trocar a constante do snippet por outra imagem, as duas metades nao
 * erram juntas, porque a deste lado nao veio de la.
 * ------------------------------------------------------------------------- */

/* Do despacho: "o cabecalho usa .../logo-clube-do-mosaico.png direto, em <img>,
   alt Clube do Mosaico, link para /. Nenhum texto ao lado. Altura 52 px." */
$logo_oficial = 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png';
$logo_altura  = 52;
$logo_largura = 78; /* 1536x1024 e 3:2, entao 52 px de altura dao 78 de largura. */

echo "\n7. Marca entregue, paleta e rodape\n";
preg_match( '#<a class="cdm-marca".*?</a>#is', $home, $mm );
$marca = isset( $mm[0] ) ? $mm[0] : '';
cdm_ok( '' !== $marca, 'a marca sai no HTML servido' );
cdm_ok( false === stripos( $marca, '<svg' ), 'nenhum logo desenhado em SVG (o PROMPT.md proibe redesenhar)' );

/* O DESPACHO DE 11/09 (2), medido: o arquivo DELE, inteiro, no cabecalho. Ate
   1.3.0 esta mesma secao afirmava o contrario — que o logo nao podia entrar por
   ter fundo preto. O arquivo e transparente; o que sumia o wordmark vinho era o
   cabecalho PRETO de 1.1.0, e isso a 1.2.0 ja tinha consertado. */
preg_match( '#<img[^>]*class="cdm-marca-logo"[^>]*>#i', $marca, $mi );
$img = isset( $mi[0] ) ? $mi[0] : '';
cdm_ok( '' !== $img, 'o cabecalho serve o logo do Raphael em <img>' );
cdm_ok( false !== strpos( $img, 'src="' . $logo_oficial . '"' ),
	'o src e EXATAMENTE o arquivo que ele subiu na biblioteca de midia' );
cdm_ok( false !== strpos( $marca, 'href="https://clubedomosaico.com.br/"' ),
	'o logo e link para a home' );

/* "O nome ja esta embutido no logo, voce nao precisa escrever." Zero caractere
   de texto dentro da marca — nao "pouco texto", nenhum. */
$marca_so_texto = trim( html_entity_decode( strip_tags( $marca ), ENT_QUOTES, 'UTF-8' ) );
cdm_ok( '' === $marca_so_texto,
	'NENHUM texto ao lado do logo: o nome esta dentro da imagem',
	'' === $marca_so_texto ? 'vazio' : '"' . $marca_so_texto . '"' );
/* Sem texto na tela, quem nao ve a imagem depende do alt — e ele diz o nome uma
   vez so, nunca duas (seria a marca em dobro no leitor de tela). */
preg_match( '#alt="([^"]*)"#i', $img, $ma );
cdm_ok( isset( $ma[1] ) && 'Clube do Mosaico' === $ma[1],
	'o alt carrega o nome da marca para quem nao ve a imagem',
	isset( $ma[1] ) ? '"' . $ma[1] . '"' : 'sem alt' );
cdm_ok( 1 === substr_count( $marca, 'alt=' ), 'uma imagem so na marca, um alt so' );

/* Largura e altura declaradas: sem elas a linha do cabecalho pula quando a
   imagem chega, e a proporcao errada distorce o logotipo de outra pessoa. */
preg_match( '#width="(\d+)"#', $img, $mw );
preg_match( '#height="(\d+)"#', $img, $mh2 );
$w = isset( $mw[1] ) ? (int) $mw[1] : 0;
$h = isset( $mh2[1] ) ? (int) $mh2[1] : 0;
cdm_ok( $logo_largura === $w && $logo_altura === $h,
	'width e height declarados, na proporcao 3:2 do arquivo', $w . 'x' . $h );

/* O SRCSET NAO E PORTA DOS FUNDOS PARA OUTRA IMAGEM. Ele existe para nao baixar
   1,26 MB num espaco de 78 px, e so pode oferecer reducoes que o proprio
   WordPress gerou DESTE upload: mesmo nome de arquivo, so com o sufixo de
   tamanho. Qualquer outro endereco aqui seria logo trocado sem ninguem ver. */
$base_logo = preg_replace( '/\.png$/', '', $logo_oficial );
preg_match( '#srcset="([^"]*)"#i', $img, $ms2 );
$candidatos = isset( $ms2[1] ) ? preg_split( '/\s*,\s*/', trim( $ms2[1] ) ) : array();
$intrusos   = array();
foreach ( $candidatos as $c ) {
	$url = trim( explode( ' ', trim( $c ) )[0] );
	if ( '' === $url ) {
		continue;
	}
	if ( 1 !== preg_match( '#^' . preg_quote( $base_logo, '#' ) . '(-\d+x\d+)?\.png$#', $url ) ) {
		$intrusos[] = $url;
	}
}
cdm_ok( empty( $intrusos ), 'todo candidato do srcset e o MESMO arquivo, so menor',
	empty( $intrusos ) ? count( $candidatos ) . ' candidato(s)' : implode( ' ', $intrusos ) );
cdm_ok( false !== strpos( $img, 'sizes="' . $logo_largura . 'px"' ),
	'o sizes diz a largura real na tela, senao o navegador escolhe pelo pior caso' );

/* A lotus solta nao volta ao cabecalho por caminho nenhum: o lugar dela e icone
   pequeno. Se ela aparecer aqui de novo, e marca em dobro ao lado do wordmark
   que ja esta desenhado dentro do logo. */
cdm_ok( false === strpos( $marca, 'cdm-marca-lotus' ) && false === strpos( $marca, 'data:image/png;base64,' ),
	'a lotus solta NAO entra no cabecalho (o logo completo ja a contem)' );

/* E EM TODAS AS NOVE, uma vez por pagina. A afirmacao "o logo esta no
   cabecalho" medida so na home aprovaria um logo que aparece na home e some no
   resto — e o `static` de cdm_casca_marca_html() e exatamente o mecanismo que
   faria isso numa bancada de um processo so (por isso o render acima e um
   processo por pagina). */
foreach ( $paginas as $tag ) {
	$n = substr_count( $html_por_pagina[ $tag ], 'class="cdm-marca-logo"' );
	cdm_ok( 1 === $n, "[$tag] o logo sai no cabecalho, uma vez", "achados: $n" );
}

cdm_ok( 1 === substr_count( $home, 'class="cdm-rodape"' ), 'exatamente um rodape na pagina', substr_count( $home, 'class="cdm-rodape"' ) . ' achado(s)' );

/* O coral e COR DE SINAL: no maximo um botao principal por tela. */
foreach ( $paginas as $tag ) {
	$n = substr_count( cdm_corpo( $html_por_pagina[ $tag ] ), 'class="cdm-botao"' );
	cdm_ok( $n <= 1, "[$tag] no maximo um botao de sinal por tela", "achados: $n" );
}

preg_match( '#<style id="cdm-casca">(.*?)</style>#is', $home, $ms );
$css = isset( $ms[1] ) ? $ms[1] : '';
cdm_ok( '' !== $css, 'CSS da casca servido no wp_head', strlen( $css ) . ' bytes' );
cdm_ok( false === stripos( $css, 'gradient' ), 'nenhum gradiente no CSS (secao 6)' );

/* Toda cor do CSS tem que estar na paleta declarada no PROMPT.md da ilha. */
$paleta = array( '#000000', '#FC483B', '#FA7665', '#69030C', '#8A0F18', '#FFFFFF', '#1F1715', '#E9DCD7', '#6E5F5B', '#B9791A' );
preg_match_all( '/#[0-9A-Fa-f]{6}\b/', $css, $mh );
$fora = array_values( array_unique( array_diff( array_map( 'strtoupper', $mh[0] ), $paleta ) ) );
cdm_ok( empty( $fora ), 'nenhuma cor fora da paleta da ilha no CSS', empty( $fora ) ? count( $mh[0] ) . ' usos' : implode( ' ', $fora ) );
/* Cabecalho CLARO, rodape preto, miolo branco: a regra visual desta ilha depois
   do despacho de 11/09. O cabecalho e medido pelas tres coisas que o Raphael
   reprovou de uma vez: a cor do fundo, a linha que separa em vez da sombra, e a
   cor do texto do menu. */
cdm_ok( preg_match( '#header[^{}]*\{[^{}]*background:var\(--cdm-papel\)#', $css ) === 1,
	'cabecalho no papel da ilha, nao no preto' );
cdm_ok( preg_match( '#header[^{}]*\{[^{}]*border-bottom:1px solid var\(--cdm-traco\)#', $css ) === 1,
	'o cabecalho separa por linha de 1 px (secao 6), nao por sombra' );
cdm_ok( false !== strpos( $css, '.cdm-nav a,.cdm-nav .cdm-sem-link{font-family:var(--cdm-texto);font-weight:500;font-size:.95rem;color:var(--cdm-tinta)' ),
	'menu em texto escuro e peso 500 (despacho de 11/09)' );
cdm_ok( false === strpos( $css, '.cdm-nav a{color:var(--cdm-papel)' ) && false === strpos( $css, 'color:var(--cdm-papel);text-decoration:none;padding-bottom' ),
	'nenhum texto de menu branco sobrou do cabecalho preto' );
cdm_ok( false !== strpos( $css, '.cdm-rodape{background:var(--cdm-noite)' ), 'rodape no preto da ilha' );
cdm_ok( false !== strpos( $css, 'html body{background-color:var(--cdm-papel)' ), 'miolo branco' );

/* O TAMANHO DO LOGO NA TELA, medido no CSS servido (o navegador confere o
   resultado; aqui se confere a regra). Os dois numeros sao do despacho: 52 px de
   imagem numa barra de ~84 px para ela respirar. */
cdm_ok( preg_match( '#\.cdm-marca-logo\{[^{}]*height:' . $logo_altura . 'px#', $css ) === 1,
	'o logo sai com ' . $logo_altura . ' px de altura (despacho de 11/09)' );
cdm_ok( preg_match( '#\.cdm-marca-logo\{[^{}]*width:auto#', $css ) === 1,
	'largura auto: a proporcao do logotipo dele nao se distorce' );
if ( preg_match( '#header[^{}]*\{[^{}]*min-height:([\d.]+)rem#', $css, $mb ) ) {
	$barra = (float) $mb[1] * 16;
	cdm_ok( $barra >= $logo_altura + 24,
		'a barra do cabecalho tem folga em volta do logo', round( $barra ) . ' px para um logo de ' . $logo_altura );
} else {
	cdm_ok( false, 'a barra do cabecalho declara altura minima' );
}
/* O LOGO NUNCA SOBRE FUNDO ESCURO — e a unica coisa que este arquivo nao
   aceita, porque o wordmark dentro dele e vinho (#69030C) e some no preto. Foi
   isso, e nao o arquivo, que sumiu com o logo em 1.1.0. A regra se mede na
   regra do cabecalho, que e onde o logo vive. */
cdm_ok( preg_match( '#header[^{}]*\{[^{}]*background:var\(--cdm-noite\)#', $css ) !== 1,
	'nenhuma regra devolve fundo escuro ao cabecalho onde o logo vive' );

/* ---------------------------------------------------------------------------
 * 8. A LOJA NOS DOIS ESTADOS — a borda da grade (secao 8, regra 2).
 *
 * Sem CPT (o estado de hoje): estado vazio honesto, e NENHUMA peca inventada.
 * Com CPT e peca publicada: a peca aparece, com preco, e o estado vazio some.
 *
 * Testar so o primeiro aprovaria uma vitrine que nunca mostra peca; testar so o
 * segundo aprovaria uma Loja que inventa exemplo quando esta vazia.
 * ------------------------------------------------------------------------- */

echo "\n8. Loja nos dois estados (secao 8, regra 2: a grade inclui a borda)\n";
$corpo_loja = cdm_corpo( $html_por_pagina['cdm_loja'] );
cdm_ok( false !== strpos( $corpo_loja, 'cdm-vazio' ), 'sem CPT: a Loja mostra o estado vazio honesto' );
cdm_ok( false === strpos( $corpo_loja, 'cdm-preco' ), 'sem CPT: nenhum preco na tela' );
cdm_ok( false === strpos( $corpo_loja, 'cdm-cards' ), 'sem CPT: nenhuma grade de peca inventada' );
$corpo_home_vazio = cdm_corpo( $home );
cdm_ok( false !== strpos( $corpo_home_vazio, 'A vitrine abre em breve' ), 'sem CPT: a home diz que a vitrine nao abriu' );

/* Agora a borda: o CPT existe e ha duas pecas publicadas. */
$GLOBALS['__tipos'] = array( 'peca' => true );
$GLOBALS['__pecas'] = array(
	(object) array( 'ID' => 101, 'post_title' => 'Vaso de mosaico azul', 'post_name' => 'loja/vaso-de-mosaico-azul' ),
	(object) array( 'ID' => 102, 'post_title' => 'Colar de tesselas',    'post_name' => 'loja/colar-de-tesselas' ),
);
$GLOBALS['__meta'] = array(
	101 => array( '_cdm_preco' => '189.90' ),
	102 => array( '_cdm_preco' => '74.00' ),
);
cdm_teste_rebobinar();
$loja_com_peca  = cdm_teste_pagina( 'cdm_loja' );
$corpo_com_peca = cdm_corpo( $loja_com_peca );
cdm_ok( false !== strpos( $corpo_com_peca, 'Vaso de mosaico azul' ), 'com CPT: a peca publicada aparece na Loja' );
cdm_ok( false !== strpos( $corpo_com_peca, 'cdm-preco' ), 'com CPT: o preco sai marcado como preco' );
/* PRECO EM FORMATO BRASILEIRO, E COM ESPACO QUE NAO QUEBRA.
 *
 * Era `strpos( ..., 'R$ 189,90' )` com espaco comum, e o bloco 4d trocou a
 * vitrine pela versao com foto — que serve `R$&nbsp;189,90`. A afirmacao caiu, e
 * o certo aqui NAO era afrouxar a regua para aceitar as duas: um preco que quebra
 * a linha entre o "R$" e o numero e defeito de verdade num cartao de produto, e o
 * cartao e a primeira coisa que alguem ve na Loja. Entao a regua APERTOU — ela
 * cobra o espaco inquebravel e proibe o comum, para o dia em que alguem
 * "simplificar" o `&nbsp;` de volta. As duas direcoes, como toda trava desta ilha. */
cdm_ok( false !== strpos( $corpo_com_peca, 'R$&nbsp;189,90' ),
	'com CPT: preco em formato brasileiro, com espaco que nao quebra', '189.90 -> R$&nbsp;189,90' );
cdm_ok( false === strpos( $corpo_com_peca, 'R$ 189,90' ),
	'com CPT: o preco NAO sai com espaco comum (quebraria de linha no cartao)' );
cdm_ok( false === strpos( $corpo_com_peca, 'cdm-vazio' ), 'com CPT: o estado vazio SOME quando ha peca' );

cdm_teste_rebobinar();
$home_com_peca = cdm_corpo( cdm_teste_pagina( 'cdm_home' ) );
cdm_ok( false !== strpos( $home_com_peca, 'Vaso de mosaico azul' ), 'com CPT: a home mostra as ultimas pecas' );
cdm_ok( false === strpos( $home_com_peca, 'A vitrine abre em breve' ), 'com CPT: a home deixa de dizer que a vitrine nao abriu' );

/* Volta ao estado real do site de hoje. */
$GLOBALS['__tipos'] = array();
$GLOBALS['__pecas'] = array();
$GLOBALS['__meta']  = array();

/* ---------------------------------------------------------------------------
 * 9. LINK PARA PAGINA QUE NAO EXISTE E 404 NO AR.
 *
 * Com o mapa de paginas vazio, nenhuma listagem pode imprimir <a> para o
 * dominio da ilha: tudo tem que sair como <span>. Foi o defeito que a Aquametria
 * pagou em 08/09/2026.
 * ------------------------------------------------------------------------- */

echo "\n9. Nenhum link para pagina inexistente (cicatriz da Aquametria)\n";
$paginas_reais          = $GLOBALS['__paginas'];
$GLOBALS['__paginas']   = array();
foreach ( $paginas as $tag ) {
	cdm_teste_rebobinar();
	$corpo = cdm_corpo( cdm_teste_pagina( $tag ) );
	$n = preg_match_all( '#<a href="https://clubedomosaico\.com\.br/#', $corpo );
	cdm_ok( 0 === $n, "[$tag] sem pagina publicada, zero <a> para a ilha no corpo", "achados: $n" );
}
$GLOBALS['__paginas'] = $paginas_reais;

/* ---------------------------------------------------------------------------
 * 10. OS NUMEROS DA TELA BATEM COM O BANCO COMMITADO.
 *
 * Regua propria (secao 8, regra 1): cada esperado abaixo e RECONTADO dos
 * arquivos JSON, nunca perguntado a casca.
 * ------------------------------------------------------------------------- */

echo "\n10. Numeros da tela x banco commitado (secao 10: nunca invente dado)\n";
$colas   = json_decode( file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$esquema = json_decode( file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$celulas = $esquema['matriz_esperada_da_F2']['celulas'];

/* BLOCO 3c: os totais de 'esperando link' e 'sem imagem' sao da ILHA, nao da categoria
   cola — e a secao 7 do contrato manda reportar o numero da ilha em todo bloco. Ate aqui
   este teste lia so materiais-colas.json, e era por isso que ele nao viu o cartao de
   Rejuntes dizendo "0 no banco" no dia em que a categoria ganhou cinco produtos: ele
   media a unica categoria que existia quando foi escrito. Agora varre dados/ inteiro. */
$arquivos_de_banco = glob( $raiz . '/dados/materiais-*.json' );
sort( $arquivos_de_banco );
$banco_por_categoria = array();
$total_esperando_link = 0;
$total_sem_imagem     = 0;
$total_documentos        = 0;
$total_documentos_abertos = 0;
foreach ( $arquivos_de_banco as $arquivo ) {
	$b = json_decode( file_get_contents( $arquivo ), true );
	$banco_por_categoria[ basename( $arquivo, '.json' ) ] = $b;
	$total_esperando_link += (int) $b['afiliado']['itens_esperando_link'];
	$total_sem_imagem     += (int) $b['imagens']['itens_sem_imagem'];
	foreach ( (array) ( isset( $b['materiais'] ) ? $b['materiais'] : array() ) as $_m ) {
		foreach ( (array) ( isset( $_m['fontes'] ) ? $_m['fontes'] : array() ) as $_f ) {
			$total_documentos++;
			if ( ! empty( $_f['tipo_de_origem'] ) ) {
				$total_documentos_abertos++;
			}
		}
	}
}
cdm_ok( $total_documentos_abertos > 0,
	'ha documento aberto pagina a pagina no banco — senao a frase da prova nao morde',
	$total_documentos_abertos . ' de ' . $total_documentos );
$rejuntes = isset( $banco_por_categoria['materiais-rejuntes'] ) ? $banco_por_categoria['materiais-rejuntes'] : null;

$bases_no_esquema     = array();
$ambientes_no_esquema = array();
$com_saida            = 0;
foreach ( $celulas as $c ) {
	$bases_no_esquema[ $c['base'] ]         = true;
	$ambientes_no_esquema[ $c['ambiente'] ] = true;
	if ( ! empty( $c['recomendados_topo'] ) ) {
		$com_saida++;
	}
}
/* bases e ambientes sao os do VOCABULARIO, que e o que a tela promete cobrir —
   a matriz so visita as combinacoes que valem a pena, entao contar as bases
   pelas celulas daria um numero menor que o declarado. */
$bases_vocab     = $esquema['vocabularios']['base'];
$ambientes_vocab = $esquema['vocabularios']['ambiente'];

$esperado = array(
	'materiais_cola'     => count( $colas['materiais'] ),
	'materiais_rejunte'  => $rejuntes ? count( $rejuntes['materiais'] ) : 0,
	'esperando_link'     => $total_esperando_link,
	'sem_imagem'         => $total_sem_imagem,
	'celulas_matriz'     => count( $celulas ),
	'celulas_rejunte'    => count( $esquema['matriz_esperada_do_rejunte']['celulas'] ),
	'celulas_com_saida'  => $com_saida,
	'celulas_sem_saida'  => count( $celulas ) - $com_saida,
	'bases'              => count( $bases_vocab ),
	'ambientes'          => count( $ambientes_vocab ),
	'categorias_do_guia' => 6,
	/* OS DOIS NUMEROS DOS DOCUMENTOS, recontados AQUI a partir dos arquivos
	   commitados (06/10/2026). A frase da camada de prova da F2 publicava, desde
	   11/09, que "nenhum PDF de fabricante foi aberto linha a linha" — e em 05 e
	   06/10 dois boletins foram abertos e lidos pagina a pagina. Nenhuma regua
	   recontava isso, porque a frase era prosa e nao numero: foi so quando ela
	   virou conta que esta linha pudera existir. O marcador de "aberto" e a
	   presenca de `tipo_de_origem` na fonte, nunca a prosa do `tipo` — contar
	   pela frase leria "PDF nao aberto" como aberto no dia em que alguem
	   reescrevesse a frase. */
	'documentos_no_banco' => $total_documentos,
	'documentos_abertos'  => $total_documentos_abertos,
);

$n = cdm_casca_numeros();
foreach ( $esperado as $chave => $valor ) {
	cdm_ok( (int) $n[ $chave ] === (int) $valor, "numero '$chave' bate com o banco", 'tela ' . $n[ $chave ] . ' / banco ' . $valor );
}
cdm_ok( count( cdm_casca_categorias_do_guia() ) === (int) $esperado['categorias_do_guia'],
	'o Guia lista as seis categorias', count( cdm_casca_categorias_do_guia() ) . ' cartoes' );

/* A TRAVA QUE FALTAVA, e que custou um numero falso na tela: TODA categoria do Guia que
   ja tem arquivo de banco tem que mostrar a contagem do arquivo. Antes, so a cola era
   conferida, e as outras cinco podiam ficar com o zero que alguem digitou — foi o que
   aconteceu com Rejuntes. A regua e escrita aqui: o esperado sai do nome do arquivo em
   dados/, nunca da lista de dentro da casca. */
$mapa_codigo_arquivo = array(
	'G-COLAS'     => 'materiais-colas',
	'G-REJUNTES'  => 'materiais-rejuntes',
	'G-PASTILHAS' => 'materiais-pastilhas',
	'G-ALICATES'  => 'materiais-alicates',
	'G-BASES'     => 'materiais-bases',
	'G-ACABAMENTO' => 'materiais-acabamento',
);
$categorias_sem_trava = array();
foreach ( cdm_casca_categorias_do_guia() as $c ) {
	$arquivo = isset( $mapa_codigo_arquivo[ $c['codigo'] ] ) ? $mapa_codigo_arquivo[ $c['codigo'] ] : null;
	if ( null === $arquivo ) {
		$categorias_sem_trava[] = $c['codigo'];
		continue;
	}
	$tem = isset( $banco_por_categoria[ $arquivo ] );
	$esperado_categoria = $tem ? count( $banco_por_categoria[ $arquivo ]['materiais'] ) : 0;
	cdm_ok( (int) $c['no_banco'] === $esperado_categoria,
		"o cartao '" . $c['titulo'] . "' mostra o que o banco tem",
		'tela ' . (int) $c['no_banco'] . ' / banco ' . $esperado_categoria );
}
cdm_ok( empty( $categorias_sem_trava ), 'toda categoria do Guia tem arquivo de banco mapeado',
	empty( $categorias_sem_trava ) ? count( $mapa_codigo_arquivo ) . ' mapeadas' : implode( ', ', $categorias_sem_trava ) );

/* E o contrario tambem: arquivo de banco que exista em dados/ e nao apareca em nenhum
   cartao seria dado colhido que a tela nunca mostra. */
$codigos_conhecidos = array_values( $mapa_codigo_arquivo );
$orfaos = array();
foreach ( array_keys( $banco_por_categoria ) as $nome ) {
	if ( ! in_array( $nome, $codigos_conhecidos, true ) ) {
		$orfaos[] = $nome;
	}
}
cdm_ok( empty( $orfaos ), 'nenhum arquivo de banco fica sem cartao no Guia',
	empty( $orfaos ) ? count( $banco_por_categoria ) . ' arquivos' : implode( ', ', $orfaos ) );

/* Os numeros tem que APARECER na tela, e no corpo — nao basta a funcao devolver
   certo. Medido dentro de <main> (secao 8, regra 3). */
$corpo_materiais = cdm_corpo( $html_por_pagina['cdm_materiais'] );
/* Os numeros do banco mudaram de pagina em 1.2.0 (a camada de prova saiu do
   Guia e foi para /materiais/como-sabemos/), entao e nessa pagina que eles sao
   cobrados agora. Medido no CORPO, como manda a regra 3. */
$corpo_como_sabemos = cdm_corpo( $html_por_pagina['cdm_como_sabemos'] );
cdm_ok( false !== strpos( $corpo_como_sabemos, '>' . $esperado['celulas_matriz'] . '<' ),
	'a pagina Como sabemos publica o total de combinacoes mapeadas' );
cdm_ok( false !== strpos( $corpo_como_sabemos, '>' . $esperado['celulas_sem_saida'] . '<' ),
	'a pagina Como sabemos publica quantas combinacoes ficam SEM resposta' );

/* ---------------------------------------------------------------------------
 * 11. A ESCADA DE FONTES DA TELA E A DO ESQUEMA.
 *
 * Ela e a parte mais facil de envelhecer em silencio: o esquema ganha um nivel,
 * a tela continua com a lista velha e ninguem ve.
 * ------------------------------------------------------------------------- */

echo "\n11. Escada de fontes: tela x esquema\n";
$niveis_esquema = $esquema['escada_de_fontes']['niveis'];
$niveis_tela    = cdm_casca_escada_de_fontes();
cdm_ok( count( $niveis_tela ) === count( $niveis_esquema ), 'mesma quantidade de niveis',
	count( $niveis_tela ) . ' na tela / ' . count( $niveis_esquema ) . ' no esquema' );
$divergentes = array();
foreach ( $niveis_esquema as $i => $degrau ) {
	if ( ! isset( $niveis_tela[ $i ] ) ) {
		$divergentes[] = 'nivel ' . $degrau['nivel'] . ' ausente na tela';
		continue;
	}
	if ( (int) $niveis_tela[ $i ]['nivel'] !== (int) $degrau['nivel'] ) {
		$divergentes[] = 'ordem trocada no nivel ' . $degrau['nivel'];
	}
	if ( (bool) $niveis_tela[ $i ]['existe'] !== (bool) $degrau['existe_hoje'] ) {
		$divergentes[] = 'nivel ' . $degrau['nivel'] . ': existe_hoje diverge';
	}
}
cdm_ok( empty( $divergentes ), 'cada nivel da tela bate com o do esquema (numero e existe_hoje)',
	empty( $divergentes ) ? count( $niveis_tela ) . ' niveis' : implode( ', ', $divergentes ) );

/* ---------------------------------------------------------------------------
 * 12. O sitemap nao pode responder 404 (cicatriz da Robometria, 10/09/2026).
 * ------------------------------------------------------------------------- */

echo "\n12. Sitemap nao responde 404\n";

class CdmConsultaFalsa {
	private $vars;
	public function __construct( $vars ) { $this->vars = $vars; }
	public function get( $chave ) { return isset( $this->vars[ $chave ] ) ? $this->vars[ $chave ] : ''; }
}

$de_sitemap  = new CdmConsultaFalsa( array( 'sitemap' => 'index' ) );
$de_pagina   = new CdmConsultaFalsa( array( 'sitemap' => 'posts', 'sitemap-subtype' => 'page', 'paged' => 1 ) );
$requisicao  = new CdmConsultaFalsa( array( 'pagename' => 'materiais' ) );
$inexistente = new CdmConsultaFalsa( array( 'name' => 'pagina-que-nao-existe' ) );

cdm_ok( true === apply_filters( 'pre_handle_404', false, $de_sitemap ), 'o indice do sitemap deixa de ser 404' );
cdm_ok( true === apply_filters( 'pre_handle_404', false, $de_pagina ), 'o sitemap de paginas deixa de ser 404' );
cdm_ok( false === apply_filters( 'pre_handle_404', false, $requisicao ), 'pagina comum NAO e afetada pelo filtro' );
cdm_ok( false === apply_filters( 'pre_handle_404', false, $inexistente ), 'endereco inexistente continua podendo 404' );
cdm_ok( false === apply_filters( 'pre_handle_404', false, null ), 'filtro sobrevive a consulta ausente sem explodir' );

/* ---------------------------------------------------------------------------
 * 13. Higiene do snippet (secao 8, fase 4b) e apelidos.
 * ------------------------------------------------------------------------- */

echo "\n13. Higiene do snippet e apelidos (secao 8, fase 4b)\n";
$fonte = file_get_contents( $raiz . '/snippets/clubedomosaico-casca.php' );
cdm_ok( 0 === strpos( $fonte, '/**' ), 'o snippet comeca com /** e sem <?php no topo' );
cdm_ok( false === strpos( $fonte, '$_SERVER' ), 'nenhuma superglobal de servidor (o ModSecurity mata a gravacao em silencio)' );

preg_match_all( '/^function\s+([a-z0-9_]+)\s*\(/mi', $fonte, $mf );
$desprotegidas = array();
foreach ( $mf[1] as $nome ) {
	if ( false === strpos( $fonte, "function_exists( '" . $nome . "' )" ) ) {
		$desprotegidas[] = $nome;
	}
}
cdm_ok( empty( $desprotegidas ), 'toda funcao de nivel superior dentro de function_exists',
	empty( $desprotegidas ) ? count( $mf[1] ) . ' funcoes' : implode( ' ', $desprotegidas ) );

$destinos = array_keys( cdm_casca_definicao_paginas() );
foreach ( cdm_casca_ferramentas() as $f ) { $destinos[] = $f['slug']; }
foreach ( cdm_casca_categorias_do_guia() as $c ) { $destinos[] = $c['slug']; }
foreach ( cdm_casca_tutoriais() as $t ) { $destinos[] = $t['slug']; }
$orfaos = array();
foreach ( cdm_casca_apelidos() as $apelido => $destino ) {
	if ( ! in_array( $destino, $destinos, true ) ) { $orfaos[] = $apelido . '->' . $destino; }
	if ( in_array( $apelido, $destinos, true ) ) { $orfaos[] = $apelido . ' (apelido igual a slug real)'; }
}
cdm_ok( empty( $orfaos ), 'todo apelido aponta para pagina conhecida',
	empty( $orfaos ) ? count( cdm_casca_apelidos() ) . ' apelidos' : implode( ', ', $orfaos ) );

/* /atelie/ e o painel da artesa, e desde 12/09/2026 ele EXISTE (bloco 4d).
 *
 * Esta dupla de afirmacoes era uma RESERVA: enquanto o painel nao existia, elas
 * cobravam que nada da casca ocupasse o endereco, para o snippet do Atelie poder
 * nascer sem disputa. A reserva cumpriu o papel e agora se inverte — o que se
 * cobra e que o painel esteja registrado E que nenhum apelido aponte para ele. Um
 * apelido da casca em cima de /atelie/ redirecionaria a artesa para outro lugar
 * na hora em que ela abrisse o link do e-mail, que e o pior momento possivel. */
$apelidos = cdm_casca_apelidos();
cdm_ok( ! isset( $apelidos['atelie'] ), 'o endereco /atelie/ NAO e apelido da casca (e o painel da artesa)' );
cdm_ok( in_array( 'atelie', $destinos, true ), 'o painel da artesa esta registrado em /atelie/' );
$def_atelie = cdm_casca_definicao_paginas();
cdm_ok( '[cdm_atelie]' === ( $def_atelie['atelie']['conteudo'] ?? '' ),
	'a pagina /atelie/ serve o shortcode do painel', $def_atelie['atelie']['conteudo'] ?? '(ausente)' );
cdm_ok( 'privada' === ( $def_atelie['atelie']['camada'] ?? '' ),
	'a pagina /atelie/ se declara camada privada', $def_atelie['atelie']['camada'] ?? '(ausente)' );

/* O apelido resolve de verdade, e so para o que conhece. */
cdm_ok( 'materiais' === cdm_casca_apelido_para_slug( '/guia/' ), 'apelido com barra resolve para o slug canonico' );
cdm_ok( '' === cdm_casca_apelido_para_slug( 'qualquer-coisa' ), 'caminho desconhecido nao vira redirecionamento' );

/* ---------------------------------------------------------------------------
 * 13b. APELIDO DE ENDERECO COM NIVEL (casca 1.22.0)
 *
 * A afirmacao que estava aqui era a CONTRARIA — `'' === apelido_para_slug(
 * 'loja/vaso' )`, com o rotulo "caminho com nivel nao e tratado como apelido".
 * Ela cobrava uma recusa DELIBERADA, e a recusa estava errada por um motivo
 * medido: os enderecos abandonados desta ilha TEM nivel. O M9 do Pente Fino de
 * 21/09/2026 nomeia tres desenhos de endereco escritos para a camada de colecao
 * da Loja e um publicado; `/loja/vasos/` e `/loja/colecao/vasos/` foram medidos
 * em 404 no ar em 09/10/2026, e o unico mecanismo da ilha para alcanca-los
 * recusava a familia inteira numa linha.
 *
 * Ela nao foi apagada: virou a afirmacao contraria, com a trava que faltava.
 * ------------------------------------------------------------------------- */

cdm_ok( 'loja' === cdm_casca_apelido_para_slug( '/loja/vasos/' ),
	'apelido COM NIVEL resolve para o slug canonico (1.22.0)', cdm_casca_apelido_para_slug( '/loja/vasos/' ) );
cdm_ok( 'loja' === cdm_casca_apelido_para_slug( 'loja/colecao/quadros' ),
	'e resolve com tres degraus, que e o desenho do PROMPT.md' );
cdm_ok( '' === cdm_casca_apelido_para_slug( 'loja/vaso' ),
	'caminho com nivel DESCONHECIDO continua sem redirecionamento (vaso, singular)' );
cdm_ok( '' === cdm_casca_apelido_para_slug( 'loja/vasos/mais/um/degrau' ),
	'nem um caminho que COMECA por apelido conhecido e redirecionado' );

/* A normalizacao e por SEGMENTO. `sanitize_title( 'loja/vasos' )` devolve
   `lojavasos`, e um mapa normalizado pela string inteira nunca casaria. */
cdm_ok( 'loja' === cdm_casca_apelido_para_slug( 'LOJA/Vasos' ),
	'a normalizacao e por segmento, nao pela string inteira' );
cdm_ok( 'loja/vasos' === cdm_casca_normalizar_caminho( '//loja///vasos//' ),
	'degrau vazio nao entra no caminho normalizado', cdm_casca_normalizar_caminho( '//loja///vasos//' ) );

/* As duas tabelas nao se misturam: cada uma tem a sua regua. */
$com_nivel = cdm_casca_apelidos_de_caminho();
$sem_barra = array();
foreach ( $com_nivel as $apelido => $destino ) {
	if ( false === strpos( $apelido, '/' ) ) { $sem_barra[] = $apelido; }
}
cdm_ok( empty( $sem_barra ), 'todo apelido da tabela COM NIVEL tem pelo menos uma barra',
	empty( $sem_barra ) ? count( $com_nivel ) . ' apelidos' : implode( ' ', $sem_barra ) );
$com_barra = array();
foreach ( cdm_casca_apelidos() as $apelido => $destino ) {
	if ( false !== strpos( $apelido, '/' ) ) { $com_barra[] = $apelido; }
}
cdm_ok( empty( $com_barra ), 'e nenhum apelido da tabela de UM SEGMENTO tem barra',
	empty( $com_barra ) ? count( cdm_casca_apelidos() ) . ' apelidos' : implode( ' ', $com_barra ) );

/* Todo apelido com nivel aponta para pagina conhecida — a mesma cobranca da
   tabela de cima, pelo mesmo motivo: 301 para 404 e pior que o 404. */
$orfaos_n = array();
foreach ( $com_nivel as $apelido => $destino ) {
	if ( ! in_array( $destino, $destinos, true ) ) { $orfaos_n[] = $apelido . '->' . $destino; }
}
cdm_ok( empty( $orfaos_n ), 'todo apelido COM NIVEL aponta para pagina conhecida',
	empty( $orfaos_n ) ? count( $com_nivel ) . ' apelidos' : implode( ', ', $orfaos_n ) );

/* ---------------------------------------------------------------------------
 * A TRAVA QUE A TABELA DE UM SEGMENTO NAO PRECISAVA.
 *
 * Apelido de um segmento so pode colidir com a RAIZ, e a afirmacao "apelido
 * igual a slug real" ja cobria isso. Apelido com nivel pode sombrear QUALQUER
 * degrau da arvore, inclusive o de uma pagina que ainda NAO NASCEU — e o caso
 * tem nome: `materiais/pastilhas` e slug reservado da categoria G-PASTILHAS do
 * Guia, que a 16.5 ainda nao autoriza. Um apelido ali ficaria verde hoje e
 * tiraria a categoria do ar no dia em que ela nascesse.
 *
 * A comparacao e contra o CAMINHO REAL, nunca contra o slug: o slug da
 * ferramenta da cola e `qual-cola-usar-no-mosaico` e o caminho dela e
 * `materiais/qual-cola-usar-no-mosaico`. Comparar com slug deixaria passar o
 * apelido que sombreia a ferramenta — e a ferramenta da cola e a pagina que
 * mais ranqueia nesta ilha.
 * ------------------------------------------------------------------------- */

/* A divergencia e REAL e foi medida nesta bancada: `cdm_casca_ferramentas()`
   declara `qual-cola-usar-no-mosaico` e a arvore conhece
   `materiais/qual-cola-usar-no-mosaico`. A primeira versao desta afirmacao
   supos a divergencia na direcao contraria e saiu VERMELHA — e foi a bancada,
   nao o olho, que disse em que direcao ela e. */
cdm_ok( 'materiais/qual-cola-usar-no-mosaico' === cdm_casca_caminho_de_slug( 'qual-cola-usar-no-mosaico' ),
	'o CAMINHO REAL se remonta pela arvore mesmo quando so o ultimo degrau e dado',
	cdm_casca_caminho_de_slug( 'qual-cola-usar-no-mosaico' ) );
cdm_ok( 'materiais/acabamento/verniz-para-peca-de-mosaico' === cdm_casca_caminho_de_slug( 'verniz-para-peca-de-mosaico' ),
	'e remonta tres degraus a partir do ultimo', cdm_casca_caminho_de_slug( 'verniz-para-peca-de-mosaico' ) );
cdm_ok( 'materiais/acabamento/verniz-para-peca-de-mosaico' === cdm_casca_caminho_de_slug( 'materiais/acabamento/verniz-para-peca-de-mosaico' ),
	'e o caminho bate consigo mesmo quando o caminho inteiro e dado' );
cdm_ok( '' === cdm_casca_caminho_de_slug( 'pagina-que-nao-existe' ),
	'slug que a arvore nao conhece nao tem caminho' );

/* O conjunto de caminhos reais vem da ARVORE, que e quem os conhece, mais o
   slug declarado de cada destino — pagina da casca na raiz tem caminho igual ao
   slug e pode nao estar na arvore. */
$caminhos_reais = array_keys( cdm_casca_arvore() );
foreach ( $destinos as $slug_real ) {
	$c = cdm_casca_caminho_de_slug( $slug_real );
	if ( '' !== $c ) { $caminhos_reais[] = $c; }
	$caminhos_reais[] = trim( (string) $slug_real, '/' );
}
$caminhos_reais = array_values( array_unique( $caminhos_reais ) );
$sombras = array();
foreach ( $com_nivel as $apelido => $destino ) {
	if ( in_array( $apelido, $caminhos_reais, true ) ) { $sombras[] = $apelido; }
}
cdm_ok( empty( $sombras ), 'nenhum apelido COM NIVEL sombreia o caminho real de pagina registrada',
	empty( $sombras ) ? count( $caminhos_reais ) . ' caminhos reais medidos' : implode( ' ', $sombras ) );

/* O caso nomeado, cobrado por nome e nao so pela varredura acima: se alguem
   acrescentar a categoria reservada ao mapa, esta linha fica vermelha. */
cdm_ok( ! isset( $com_nivel['materiais/pastilhas'] ),
	'`materiais/pastilhas` NAO e apelido (e slug reservado da categoria do Guia)' );
cdm_ok( ! isset( $com_nivel['materiais/acabamento'] ),
	'`materiais/acabamento` NAO e apelido (e a unica categoria do Guia no ar)' );

/* Os tres desenhos de endereco do M9 estao cobertos, e a conta e a dos seis
   termos: 6 pelo tipo/uso + 6 com o segmento `colecao` + a camada sozinha. */
$termos_m9 = array( 'vasos', 'colares', 'quadros', 'centro-de-mesa', 'presentes', 'jardim' );
$faltam_m9 = array();
foreach ( $termos_m9 as $t ) {
	if ( 'loja' !== ( $com_nivel[ 'loja/' . $t ] ?? '' ) )         { $faltam_m9[] = 'loja/' . $t; }
	if ( 'loja' !== ( $com_nivel[ 'loja/colecao/' . $t ] ?? '' ) ) { $faltam_m9[] = 'loja/colecao/' . $t; }
}
cdm_ok( empty( $faltam_m9 ), 'os tres desenhos de endereco do M9 estao no mapa, nos seis termos',
	empty( $faltam_m9 ) ? count( $termos_m9 ) * 2 + 1 . ' enderecos' : implode( ' ', $faltam_m9 ) );

/* ---------------------------------------------------------------------------
 * 14. O QUE A ILHA PROMETEU NAO PUBLICAR.
 *
 * Medido no corpo das oito paginas, nunca no HTML inteiro.
 * ------------------------------------------------------------------------- */

echo "\n14. O que esta ilha nao publica (secao 7 do contrato)\n";
/**
 * A REGUA AQUI E ESTRUTURAL, e chegou a este formato depois de DUAS reprovadas
 * dela mesma — e as duas sao a lição da seção 8 acontecendo de novo.
 *
 *   1ª versão: procurava o termo no corpo inteiro e abria exceção para algumas
 *      negações escritas à mão. Reprovou a página Sobre, que diz com todas as
 *      letras que NÃO publica selo de mais vendido — frase legítima.
 *   2ª versão: separava o corpo em frases e perdoava a frase que tivesse
 *      qualquer negação. Quebrando o código de propósito, ela APROVOU "a ficha
 *      técnica do silicone acético mais vendido do Brasil lista … entre as
 *      superfícies em que o produto NÃO deve ser usado": o "não" da frase negava
 *      outra coisa. Perdoar por presença de palavra é adivinhar.
 *   3ª versão, esta: a página DECLARA no markup qual bloco é recusa
 *      (class="cdm-nao-fazemos"), o teste retira esses blocos e depois proíbe o
 *      termo em qualquer lugar do que sobrou. Não há heurística para enganar.
 *
 * E para a declaração não virar porta dos fundos — bastaria marcar uma promessa
 * de venda como recusa —, o teste também exige que todo bloco marcado seja de
 * fato uma negação e que eles sejam poucos e nomeados.
 *
 * Foi assim que a 2ª versão achou um defeito de verdade escrito pela própria
 * Fundação: a home chamava o produto de "o silicone acético mais vendido para
 * construção", número de venda que esta ilha nunca mediu (seção 7 do contrato).
 */
function cdm_sem_blocos_de_recusa( $corpo, &$recusas ) {
	$recusas = array();
	if ( preg_match_all( '#<(li|p)\s+class="cdm-nao-fazemos">(.*?)</\1>#is', $corpo, $m ) ) {
		$recusas = $m[2];
	}
	return preg_replace( '#<(li|p)\s+class="cdm-nao-fazemos">.*?</\1>#is', ' ', $corpo );
}

$proibidos   = array( 'mais vendido', 'últimas unidades', 'ultimas unidades', 'por tempo limitado', 'oferta relâmpago', 'últimas peças', 'só hoje' );
$achados     = array();
$recusas_tot = 0;
$recusa_ruim = array();
$recusas_por_pagina = array();
foreach ( $paginas as $tag ) {
	$recusas = array();
	$limpo   = mb_strtolower( strip_tags( cdm_sem_blocos_de_recusa( cdm_corpo( $html_por_pagina[ $tag ] ), $recusas ) ), 'UTF-8' );
	$limpo   = html_entity_decode( $limpo, ENT_QUOTES, 'UTF-8' );
	foreach ( $proibidos as $termo ) {
		if ( false !== mb_strpos( $limpo, $termo ) ) {
			$achados[] = $tag . ':' . $termo;
		}
	}
	/* Todo bloco declarado como recusa tem que ABRIR negando.
	 *
	 * "Tem negação em algum lugar do bloco" era frouxo, e a mutação provou: dá
	 * para escrever "Peça mais vendido, últimas unidades!" no começo e deixar um
	 * "que não tenha medido" no fim que o teste perdoava. Recusa de verdade
	 * começa pela negação — é assim que as duas desta casca estão escritas. */
	$recusas_por_pagina[ $tag ] = count( $recusas );
	foreach ( $recusas as $r ) {
		$recusas_tot++;
		$t      = mb_strtolower( trim( html_entity_decode( strip_tags( $r ), ENT_QUOTES, 'UTF-8' ) ), 'UTF-8' );
		$abre   = false;
		foreach ( array( 'não', 'nao', 'nada de', 'nunca', 'jamais', 'sem ' ) as $negacao ) {
			if ( 0 === mb_strpos( $t, $negacao ) ) {
				$abre = true;
				break;
			}
		}
		if ( ! $abre ) {
			$recusa_ruim[] = $tag . ': "' . mb_substr( $t, 0, 50 ) . '"';
		}
	}
}
cdm_ok( empty( $achados ), 'nenhuma escassez ou superlativo nao medido fora de um bloco de recusa',
	empty( $achados ) ? 'limpo' : implode( ' | ', $achados ) );
cdm_ok( empty( $recusa_ruim ), 'todo bloco marcado como recusa e mesmo uma negacao',
	empty( $recusa_ruim ) ? $recusas_tot . ' blocos' : implode( ' | ', $recusa_ruim ) );
/* O TETO DE RECUSA E UM POR PAGINA, E ELE DEIXOU DE SER O NUMERO 4 EM
   02/10/2026. O 4 era o retrato de uma ilha de nove paginas e teria reprovado
   a leva do bloco 4c por existir — quatro paginas novas, uma recusa cada, todas
   legitimas. O que a afirmacao quer dizer e que recusa e EXCECAO na pagina, nao
   um paragrafo de rotina: entao o teto passa a ser medido por pagina, e a ilha
   pode crescer sem o portao virar obstaculo ao trabalho certo. */
$recusa_demais = array();
foreach ( $recusas_por_pagina as $tag => $quantas ) {
	if ( $quantas > 1 ) {
		$recusa_demais[] = $tag . ': ' . $quantas;
	}
}
cdm_ok( $recusas_tot > 0 && empty( $recusa_demais ),
	'bloco de recusa e excecao: no maximo um por pagina',
	empty( $recusa_demais ) ? $recusas_tot . ' blocos em ' . count( $paginas ) . ' paginas' : implode( ' | ', $recusa_demais ) );

/* A distincao que vale para esta ilha: peca propria NAO e afiliado. */
$corpo_afiliados = cdm_corpo( $html_por_pagina['cdm_afiliados'] );
cdm_ok( false !== stripos( $corpo_afiliados, 'produto próprio' ) || false !== stripos( $corpo_afiliados, 'nunca' ),
	'a divulgacao separa peca propria de link de afiliado' );
cdm_ok( false === stripos( $corpo_loja, 'sponsored' ), 'nenhum rel=sponsored na Loja (peca propria)' );

/* A artesa aparece sem nome inventado enquanto o nome nao chega. */
$corpo_sobre = cdm_corpo( $html_por_pagina['cdm_sobre'] );
cdm_ok( false !== stripos( $corpo_sobre, 'uma artesã' ), 'o Sobre fala da artesa sem inventar nome' );
cdm_ok( false === stripos( $corpo_sobre, 'raphael' ), 'o Raphael nao aparece em ilha nenhuma (secao 10)' );

/* ---------------------------------------------------------------------------
 * 13. O PORTAO DE VOZ (secao 15 do contrato e VOZ.md desta ilha)
 *
 * Quem le esta ilha esta escolhendo presente num domingo a tarde ou tem um vaso
 * de barro na mao. O rigor de numero, fonte e data FICA — ele e a tese de SEO e
 * de visibilidade em IA —, mas vira camada de PROVA e sai do titulo e do
 * primeiro paragrafo.
 *
 * A REGUA E ESTRUTURAL, NUNCA POR VIZINHANCA. Foi esta ilha que pagou a licao
 * em 11/09/2026: uma regua que perdoava o termo proibido quando havia uma
 * negacao por perto APROVOU "a ficha tecnica do silicone acetico mais vendido
 * do Brasil lista ... entre as superficies em que o produto NAO deve ser usado".
 * Entao aqui: a pagina MARCA a camada de prova no markup (class cdm-prova), o
 * teste RETIRA esses blocos e cobra o resto — e conta os blocos, porque
 * embrulhar a pagina inteira na marca seria a porta dos fundos obvia.
 * ------------------------------------------------------------------------- */

echo "\n13. Voz da ilha (VOZ.md, secao 15 do contrato)\n";

$voz = (string) @file_get_contents( $raiz . '/VOZ.md' );
cdm_ok( '' !== $voz, 'VOZ.md existe e foi lido', strlen( $voz ) . ' bytes' );

/* A lista e escrita AQUI, e depois conferida contra o VOZ.md: se alguem mexer
   na lista de la sem mexer aqui, esta afirmacao cai. O snippet nao conhece
   nenhuma das duas — nao ha como as duas metades errarem juntas. */
$proibidas_na_voz = array( 'tessela', 'substrato', 'aderência', 'especificação', 'parâmetro', 'ficha técnica' );
$fora_do_voz      = array();
foreach ( $proibidas_na_voz as $termo ) {
	if ( false === mb_stripos( $voz, $termo ) ) {
		$fora_do_voz[] = $termo;
	}
}
cdm_ok( empty( $fora_do_voz ), 'cada termo da regua esta mesmo escrito no VOZ.md',
	empty( $fora_do_voz ) ? count( $proibidas_na_voz ) . ' termos' : implode( ', ', $fora_do_voz ) );

/** Texto visivel, com as tags fora e as entidades resolvidas. */
function cdm_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/** O corpo SEM os blocos declarados como camada de prova. */
function cdm_sem_prova( $corpo ) {
	return preg_replace( '#<div class="cdm-prova">.*?</div>\s*$#is', '', preg_replace( '#<div class="cdm-prova">.*?</div>#is', '', $corpo ) );
}

/* Qual pagina e a unica declarada como camada de prova, e ela e uma so. */
$paginas_de_prova = array();
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	if ( isset( $def['camada'] ) && 'prova' === $def['camada'] ) {
		$paginas_de_prova[ $def['conteudo'] ] = $slug;
	}
}
cdm_ok( 1 === count( $paginas_de_prova ), 'existe UMA unica pagina de camada de prova, e ela e declarada',
	implode( ', ', $paginas_de_prova ) );
foreach ( $paginas_de_prova as $slug_prova ) {
	cdm_ok( in_array( $slug_prova, cdm_casca_paginas_noindex(), true ),
		'a pagina de prova esta fora do indice', $slug_prova );
}

$voz_ruim   = array();
$prova_ruim = array();
foreach ( $paginas as $tag ) {
	$corpo = cdm_corpo( $html_por_pagina[ $tag ] );
	$e_prova = isset( $paginas_de_prova[ '[' . $tag . ']' ] );

	/* O H1 e o primeiro paragrafo: e onde a pessoa decide se esta no lugar
	   certo, e e exatamente onde o termo de manual nao pode estar. */
	preg_match( '#<h1[^>]*>(.*?)</h1>#is', $corpo, $mh1 );
	preg_match( '#<p[^>]*>(.*?)</p>#is', $corpo, $mp1 );
	$cabeca = cdm_texto( ( isset( $mh1[1] ) ? $mh1[1] : '' ) . ' ' . ( isset( $mp1[1] ) ? $mp1[1] : '' ) );

	foreach ( $proibidas_na_voz as $termo ) {
		if ( false !== mb_stripos( $cabeca, $termo ) ) {
			$voz_ruim[] = $tag . ': "' . $termo . '" no titulo ou no primeiro paragrafo';
		}
	}

	/* Fora da pagina de prova, a linguagem de prova so vale dentro de um bloco
	   marcado como prova. */
	if ( ! $e_prova ) {
		$sem_prova = cdm_texto( cdm_sem_prova( $corpo ) );
		foreach ( array( 'ficha técnica', 'revisada em', 'nível de fonte' ) as $termo ) {
			if ( false !== mb_stripos( $sem_prova, $termo ) ) {
				$voz_ruim[] = $tag . ': "' . $termo . '" fora de um bloco de prova';
			}
		}
	}

	/* AS TRES TRAVAS DA PORTA DOS FUNDOS. Sem elas, declarar a pagina inteira
	   como camada de prova desligaria o portao de voz sem mudar uma palavra. */
	/* A TRAVA DEIXOU DE SER UM NUMERO E PASSOU A SER A ESTRUTURA, em 06/10/2026.
	   Ela cobrava no maximo DOIS blocos por pagina, e o 2 era o retrato de uma
	   pagina com duas camadas de prova — a da resposta e o "Como sabemos" do pe.
	   Quando a F2 ganhou o bloco de preparo do rejunte, que e resposta de outra
	   secao e por isso precisa da propria prova ao lado dela (15.2: a prova desce
	   um paragrafo, dentro da mesma caixa), a pagina passou a ter TRES camadas
	   legitimas e a trava reprovou — medindo o acaso do dia em que foi escrita.

	   O QUE ELA QUERIA IMPEDIR, nas palavras dela mesma, e "embrulhar a pagina
	   inteira na marca". Isso nao e uma questao de quantidade: e de SECAO. Quem
	   abre duas camadas de prova dentro do MESMO bloco de texto esta estendendo a
	   marca sobre prosa que nao e prova; quem abre uma por secao esta pondo o
	   rodape onde ele pertence. Entao a regra passa a ser: entre dois blocos de
	   prova tem de existir uma abertura de secao, e continua valendo o teto de
	   tamanho de 50% logo abaixo, que e a metade substantiva da trava.

	   O teto absoluto fica, agora em 5, so para o caso de alguem fabricar secoes
	   vazias para abrir provas — mas quem faz isso cai no teto de 50%.

	   E A LACUNA QUE ESTA TRAVA TEM DESDE QUE NASCEU, escrita aqui porque quem a
	   reescreveu em 06/10 a viu e NAO a fechou: ela conta `class="cdm-prova"`
	   exato, entao `class="cdm-prova cdm-guia-literal"` — a forma que a ficha do
	   Guia usa, e que o bloco de preparo da ficha passou a usar — nao e contada
	   NEM retirada por `cdm_sem_prova()`. Isso e deliberado na ilha (uma pagina
	   de Guia com dez cartoes teria dez camadas de prova e estouraria qualquer
	   teto), mas tem um custo: o texto dentro dessas caixas e medido pelo portao
	   de voz como se estivesse FORA de bloco de prova. Hoje nenhuma delas carrega
	   os termos vigiados, e por isso a lacuna nao e defeito no ar. Fecha-la e
	   bloco — a classe de prova teria de ser medida por prefixo nas DUAS funcoes,
	   e a conta por secao passaria a valer para as paginas do Guia tambem. */
	preg_match_all( '#<div class="cdm-prova">#i', $corpo, $mb, PREG_OFFSET_CAPTURE );
	$quantos_prova = count( $mb[0] );
	if ( $quantos_prova > 5 ) {
		$prova_ruim[] = $tag . ": $quantos_prova blocos de prova (teto absoluto 5)";
	}
	for ( $i = 1; $i < $quantos_prova; $i++ ) {
		$de    = (int) $mb[0][ $i - 1 ][1];
		$ate   = (int) $mb[0][ $i ][1];
		$entre = mb_substr( $corpo, $de, max( 0, $ate - $de ) );
		if ( ! preg_match( '#<(?:div|section|article)\b[^>]*class="[^"]*(?:cdm-f2-secao|cdm-f2-resposta|cdm-guia-|cdm-f1-secao|cdm-bloco)#i', $entre ) ) {
			$prova_ruim[] = $tag . ': duas camadas de prova dentro da mesma secao';
		}
	}
	if ( $quantos_prova ) {
		$posicao = mb_stripos( $corpo, '<div class="cdm-prova">' );
		$fim_do_primeiro_paragrafo = mb_stripos( $corpo, '</p>' );
		if ( false !== $posicao && false !== $fim_do_primeiro_paragrafo && $posicao < $fim_do_primeiro_paragrafo ) {
			$prova_ruim[] = $tag . ': a camada de prova comeca antes do primeiro paragrafo';
		}
		$tamanho_prova = 0;
		preg_match_all( '#<div class="cdm-prova">.*?</div>#is', $corpo, $mp );
		foreach ( $mp[0] as $bloco ) {
			$tamanho_prova += mb_strlen( cdm_texto( $bloco ) );
		}
		$tamanho_total = max( 1, mb_strlen( cdm_texto( $corpo ) ) );
		if ( $tamanho_prova / $tamanho_total > 0.5 ) {
			$prova_ruim[] = $tag . sprintf( ': a prova ocupa %d%% do corpo', (int) round( 100 * $tamanho_prova / $tamanho_total ) );
		}
	}
}
cdm_ok( empty( $voz_ruim ), 'nenhum termo de manual na voz da pagina',
	empty( $voz_ruim ) ? count( $paginas ) . ' paginas' : implode( ' | ', $voz_ruim ) );
cdm_ok( empty( $prova_ruim ), 'a camada de prova e um rodape do texto, nunca o texto inteiro',
	empty( $prova_ruim ) ? 'limpo' : implode( ' | ', $prova_ruim ) );

/* As DUAS frases que o VOZ.md proibe pelo nome, e que estavam na home ate a
   casca 1.1.0. Medido no corpo inteiro: elas nao valem nem dentro da prova. */
$corpo_home_agora = cdm_texto( cdm_corpo( $html_por_pagina['cdm_home'] ) );
foreach ( array( 'faz duas coisas', 'responde com fonte de fabricante', 'Silicone Acético Construção da Tekbond' ) as $frase ) {
	cdm_ok( false === mb_stripos( $corpo_home_agora, $frase ), 'a home nao traz a frase proibida "' . $frase . '"' );
}

/* O TITULO DA HOME. O tema imprime o titulo da pagina como H1, e por isso a
   home exibia a palavra "Inicio" — a reclamacao do Raphael em 11/09/2026. */
$definicoes = cdm_casca_definicao_paginas();
cdm_ok( 'Início' !== $definicoes['inicio']['titulo'], 'a home nao se chama "Início"', $definicoes['inicio']['titulo'] );
preg_match( '#<h1[^>]*>(.*?)</h1>#is', cdm_corpo( $html_por_pagina['cdm_home'] ), $mh );
cdm_ok( isset( $mh[1] ) && 'Início' !== cdm_texto( $mh[1] ), 'o H1 servido na home nao e "Início"',
	isset( $mh[1] ) ? '"' . cdm_texto( $mh[1] ) . '"' : 'sem H1' );
cdm_ok( isset( $mh[1] ) && cdm_texto( $mh[1] ) === $definicoes['inicio']['titulo'],
	'o H1 servido e o titulo da definicao (o titulo se sincroniza)' );
cdm_ok( CDM_CASCA_TAGLINE === $definicoes['inicio']['titulo'],
	'a home, o <title> do site e o rodape dizem a MESMA frase', CDM_CASCA_TAGLINE );

/* ---------------------------------------------------------------------------
 * 14. PAGINA FINA NAO ENTRA NO INDICE DE DOMINIO NOVO (secao 8)
 *
 * Achado desta ilha em 11/09/2026: duas paginas da casca tinham menos de 1.200
 * caracteres de corpo e iam para o sitemap de um dominio recem-nascido gastar
 * orcamento de rastreamento. A trava mede o corpo de TODA pagina.
 * ------------------------------------------------------------------------- */

echo "\n14. Nenhuma pagina fina (secao 8 e 14.1)\n";
$finas = array();
foreach ( $paginas as $tag ) {
	$quantos = mb_strlen( cdm_texto( cdm_corpo( $html_por_pagina[ $tag ] ) ) );
	if ( $quantos < 1500 ) {
		$finas[] = "$tag ($quantos)";
	}
}
cdm_ok( empty( $finas ), 'toda pagina tem corpo de pagina de verdade (>= 1.500 caracteres)',
	empty( $finas ) ? count( $paginas ) . ' paginas medidas' : implode( ', ', $finas ) );

/* E A PAGINA MEDIDA TEM QUE ESTAR INTEIRA. Bancada que serve metade da pagina
   da um numero verde e a sensacao de ter conferido — a Robometria pagou isso
   tres vezes. A conferencia NAO e um numero redondo de bytes (esse eu nao
   consigo calibrar sem o site no ar, e numero redondo nao e criterio): e a
   lista do que uma pagina inteira desta ilha obrigatoriamente carrega. Se um
   dia o render parar de rodar um gancho, alguma destas some e a conta cai. */
$pedacos = array(
	'folha da casca'   => '<style id="cdm-casca">',
	'JSON-LD'          => 'application/ld+json',
	'favicon proprio'  => 'rel="icon" type="image/png"',
	'menu no HTML'     => 'class="cdm-nav"',
	'comando do menu'  => 'id="cdm-casca-menu"',
	'rodape da ilha'   => 'class="cdm-rodape"',
	'titulo como H1'   => '<h1 class="wp-block-post-title">',
);
$incompletas = array();
foreach ( $paginas as $tag ) {
	foreach ( $pedacos as $nome => $agulha ) {
		if ( false === strpos( $html_por_pagina[ $tag ], $agulha ) ) {
			$incompletas[] = "$tag sem $nome";
		}
	}
}
cdm_ok( empty( $incompletas ), 'a pagina medida esta inteira (folha, JSON-LD, menu, rodape e H1)',
	empty( $incompletas ) ? count( $paginas ) * count( $pedacos ) . ' presencas' : implode( ' | ', $incompletas ) );

/* ---------------------------------------------------------------------------
 * 15. NUMERO DE TELA NASCE CONTADO (secao 8)
 *
 * "Hoje 10 dos 5 itens esperam link" esteve no ar nesta ilha. Os dois numeros
 * estavam certos sozinhos — 10 itens esperando link no banco inteiro, 5 colas na
 * categoria cola — e a frase que os juntou era impossivel. Nenhum teste viu,
 * porque cada metade era conferida separada.
 * ------------------------------------------------------------------------- */

echo "\n15. Denominador de frase sobre o proprio banco (secao 8)\n";
$total_no_banco = 0;
foreach ( $banco_por_categoria as $banco ) {
	$total_no_banco += count( $banco['materiais'] );
}
cdm_ok( (int) $n['itens_no_banco'] === $total_no_banco, "numero 'itens_no_banco' e a soma das categorias",
	'tela ' . $n['itens_no_banco'] . ' / banco ' . $total_no_banco );
cdm_ok( (int) $n['esperando_link'] <= (int) $n['itens_no_banco'],
	'quem espera link nunca e mais do que o que existe',
	$n['esperando_link'] . ' de ' . $n['itens_no_banco'] );
cdm_ok( (int) $n['itens_no_banco'] >= (int) $n['materiais_cola'],
	'o total da ilha nunca e menor que uma categoria dela' );

/* E a frase tem que sair na tela com o denominador certo, no CORPO. */
$prova_materiais = '';
if ( preg_match( '#<div class="cdm-prova">(.*?)</div>#is', cdm_corpo( $html_por_pagina['cdm_materiais'] ), $mpv ) ) {
	$prova_materiais = cdm_texto( $mpv[1] );
}
cdm_ok( '' !== $prova_materiais, 'o Guia tem a camada de prova no rodape do texto' );
cdm_ok( false !== mb_strpos( $prova_materiais, $n['itens_no_banco'] . ' itens de fabricante' ),
	'a frase do Guia conta o banco inteiro, nao uma categoria',
	mb_substr( $prova_materiais, 0, 0 ) . $n['itens_no_banco'] . ' itens' );
$corpo_afiliados_texto = cdm_texto( cdm_corpo( $html_por_pagina['cdm_afiliados'] ) );
cdm_ok( false === mb_stripos( $corpo_afiliados_texto, 'não há nenhum link de afiliado' ),
	'a divulgacao nao afirma por escrito o que pode contar' );

/* ---------------------------------------------------------------------------
 * A DIVULGACAO x O `rel` QUE O SITE REALMENTE EMITE (29/09/2026).
 *
 * O defeito que fez estas reguas nascerem, e ele estava no ar: a pagina dizia
 * "essa busca NAO e link de afiliado: ninguem nos paga por aquele clique" sobre
 * 28 botoes que `cdm_f2_compra_html()` emite com `rel="sponsored"`. A ilha
 * declarava a relacao paga ao buscador e a negava a quem le. Nenhuma regua via,
 * porque o texto mora na casca, o `rel` mora na F2, e ninguem comparava os dois.
 *
 * Por isso a regua nao le o texto contra uma frase esperada escrita aqui: ela
 * pergunta ao CODIGO quais estados do botao sao pagos e cobra da PAGINA a mesma
 * classificacao. No dia em que a escada mudar de novo, quem falhar e o par.
 * ------------------------------------------------------------------------- */
echo "\n15c. A divulgacao x o `rel` emitido, e a conta de tres parcelas (25.2-b)\n";

$corpo_afiliados_html = cdm_corpo( $html_por_pagina['cdm_afiliados'] );

/* Os TRES estados da escada da 25.1, montados a mao para a funcao de compra
   responder o que ela faz em cada um. Sao os tres que a pagina descreve. */
$estados_do_botao = array(
	'ficha do produto' => array(
		'afiliado' => array( 'url' => 'https://s.shopee.com.br/FICHA', 'url_busca' => 'https://s.shopee.com.br/BUSCA' ),
		'marcador' => 'ficha do produto',
	),
	'busca encurtada'  => array(
		'afiliado' => array( 'url' => '', 'url_busca' => 'https://s.shopee.com.br/BUSCA' ),
		'marcador' => 'busca daquele produto',
	),
	'busca crua'       => array(
		'afiliado' => array( 'url' => '', 'url_busca' => '', 'url_busca_produto' => 'https://shopee.com.br/search?keyword=x' ),
		'marcador' => 'sem rastreio',
	),
);

cdm_ok( function_exists( 'cdm_f2_compra_html' ), 'a funcao de compra da escada esta carregada no teste da casca' );

$pagos_pelo_codigo  = 0;
$pagos_pela_pagina  = 0;
foreach ( $estados_do_botao as $nome => $e ) {
	$botao = cdm_f2_compra_html( $e['afiliado'] );
	/* O `rel` do BOTAO principal, que e o unico que muda de estado para estado. */
	$paga_no_codigo = ( false !== mb_strpos( $botao, 'cdm-f2-botao' ) && false !== mb_strpos( $botao, 'rel="sponsored' ) );
	if ( 'busca crua' === $nome ) {
		$paga_no_codigo = ( false !== mb_strpos( $botao, 'rel="sponsored' ) );
	}

	/* O <li> daquele estado na pagina, achado pelo marcador do proprio texto. */
	$li = '';
	if ( preg_match_all( '#<li>(.*?)</li>#is', $corpo_afiliados_html, $lis ) ) {
		foreach ( $lis[1] as $candidato ) {
			if ( false !== mb_stripos( cdm_texto( $candidato ), $e['marcador'] ) ) {
				$li = cdm_texto( $candidato );
				break;
			}
		}
	}
	cdm_ok( '' !== $li, 'a divulgacao descreve o estado "' . $nome . '" do botao', $e['marcador'] );

	$diz_que_paga     = ( false !== mb_stripos( $li, 'link de afiliado' ) || false !== mb_stripos( $li, 'render comissão' ) );
	$diz_que_nao_paga = ( false !== mb_stripos( $li, 'ninguém nos paga' ) || false !== mb_stripos( $li, 'não é link de afiliado' ) );
	$paga_na_pagina   = ( $diz_que_paga && ! $diz_que_nao_paga );

	cdm_ok( $paga_no_codigo === $paga_na_pagina,
		'"' . $nome . '": o que a pagina promete e o `rel` que o site emite',
		( $paga_no_codigo ? 'codigo: sponsored' : 'codigo: nao pago' ) . ' / ' . ( $paga_na_pagina ? 'pagina: rende' : 'pagina: nao rende' ) );

	$pagos_pelo_codigo += $paga_no_codigo ? 1 : 0;
	$pagos_pela_pagina += $paga_na_pagina ? 1 : 0;
}
cdm_ok( $pagos_pelo_codigo === $pagos_pela_pagina && 2 === $pagos_pelo_codigo,
	'dois dos tres estados sao pagos, no codigo e na pagina',
	$pagos_pelo_codigo . ' no codigo / ' . $pagos_pela_pagina . ' na pagina' );

/* A FRASE APOSENTADA NAO PODE VOLTAR. Ela e a regressao exata de 25/09 a 29/09,
   e a regua a mede pelo texto servido, nao pelo codigo-fonte do snippet. */
cdm_ok( false === mb_stripos( $corpo_afiliados_texto, 'essa busca não é link de afiliado' ),
	'a frase de 14/09 sobre a busca nao voltou ao ar' );

/* AS TRES PARCELAS, RECONTADAS DOS REGISTROS — nunca dos cabecalhos que a casca
   le. Regra 1 da secao 8: os dois lados nao erram juntos. */
$r_ficha = 0;
$r_busca = 0;
$r_crua  = 0;
$r_nada  = 0;
foreach ( $banco_por_categoria as $banco ) {
	foreach ( $banco['materiais'] as $m ) {
		$af = isset( $m['afiliado'] ) && is_array( $m['afiliado'] ) ? $m['afiliado'] : array();
		if ( ! empty( $af['url'] ) ) {
			$r_ficha++;
		} elseif ( ! empty( $af['url_busca'] ) ) {
			$r_busca++;
		} elseif ( ! empty( $af['url_busca_produto'] ) ) {
			$r_crua++;
		} else {
			$r_nada++;
		}
	}
}
cdm_ok( 0 === $r_nada, 'nenhum item do banco fica sem saida de compra (secao 7)', $r_nada . ' sem saida' );
cdm_ok( $r_ficha + $r_busca + $r_crua === $total_no_banco,
	'as tres parcelas da escada fecham no total do banco',
	$r_ficha . ' + ' . $r_busca . ' + ' . $r_crua . ' = ' . $total_no_banco );

/* E AS TRES TEM QUE CHEGAR A TELA, na mesma ordem em que a frase as apresenta —
   porque o defeito de 25/09 nao foi um numero errado: foram duas parcelas de
   tres, com os 28 do meio ausentes e nenhum digito visivelmente falso. */
cdm_ok( ! empty( $n['numeros_vivos'] ), 'a conta da divulgacao sai pela via viva no teste' );
$frase_conta = '';
if ( preg_match( '#<p class="cdm-nota"><strong>Estado de hoje:(.*?)</p>#is', $corpo_afiliados_html, $mc ) ) {
	$frase_conta = cdm_texto( $mc[1] );
}
cdm_ok( '' !== $frase_conta, 'a divulgacao publica a conta do estado de hoje' );
/* O numero e cobrado NO CONTEXTO da parcela, nunca solto: "0" e "10" aparecem
   em qualquer frase por acidente, e uma regua que aceita o digito solto aprova
   a frase que perdeu a parcela do meio — que e exatamente o defeito de 25/09. */
$n_txt = function ( $v ) {
	return cdm_texto( cdm_casca_num( $v ) );
};
foreach ( array(
	'o total do banco'          => 'os ' . $n_txt( $total_no_banco ) . ' materiais do banco',
	'a parcela da ficha'        => 'Em ' . $n_txt( $r_ficha ) . ' o botão é a ficha do produto',
	'a parcela da busca'        => 'em ' . $n_txt( $r_busca ) . ' é a busca na loja',
	'a soma do que rende'       => 'esses ' . $n_txt( $r_ficha + $r_busca ) . ' são link de afiliado',
	'a parcela sem rastreio'    => 'Em ' . $n_txt( $r_crua ) . ' o botão é a busca sem rastreio',
) as $rotulo => $trecho ) {
	cdm_ok( false !== mb_strpos( $frase_conta, $trecho ),
		'a conta servida traz ' . $rotulo . ', com o numero no lugar', $trecho );
}

/* A BORDA, E ELA NAO E ZELO: SEM ELA UMA TRAVA DESTE BLOCO NASCEU INERTE.
   Hoje `piso_nao_rastreavel` e 0, e com zero a parcela do meio da conta
   (`esperando_link - piso_nao_rastreavel`) tem o MESMO valor de `esperando_link`
   sozinho. Trocar uma pela outra nao muda digito nenhum no mundo de hoje, e a
   bateria de mutacao provou isso: a mutacao "a parcela da busca troca de fonte"
   PASSOU na primeira rodada. O defeito que ela escreve so aparece no dia em que
   um item perder o rastreio — que e o dia em que a pagina voltaria a contar um
   clique que nao paga como se pagasse.
   Entao a bancada fabrica esse dia: um item de alicate perde a busca encurtada e
   fica so com a crua. Regra 2 da secao 8 — grade tem que incluir a borda. */
$chave_borda = 'clubedomosaico_dados_materiais-alicates';
$guardado    = $GLOBALS['__options'][ $chave_borda ];

$GLOBALS['__options'][ $chave_borda ]['afiliado']['itens_com_piso_nao_rastreavel'] = 1;
cdm_teste_rebobinar();
$frase_borda = '';
if ( preg_match( '#<p class="cdm-nota"><strong>Estado de hoje:(.*?)</p>#is', cdm_corpo( cdm_teste_pagina( 'cdm_afiliados' ) ), $mb ) ) {
	$frase_borda = cdm_texto( $mb[1] );
}
cdm_ok( '' !== $frase_borda, 'na borda, a divulgacao continua publicando a conta' );
cdm_ok( false !== mb_strpos( $frase_borda, 'em ' . $n_txt( $r_busca - 1 ) . ' é a busca na loja' ),
	'na borda, a parcela da busca DESCONTA quem perdeu o rastreio',
	'esperado ' . ( $r_busca - 1 ) . ', nunca ' . $r_busca );
cdm_ok( false !== mb_strpos( $frase_borda, 'esses ' . $n_txt( $r_ficha + $r_busca - 1 ) . ' são link de afiliado' ),
	'na borda, a soma do que rende encolhe junto',
	(string) ( $r_ficha + $r_busca - 1 ) );
cdm_ok( false !== mb_strpos( $frase_borda, 'Em ' . $n_txt( 1 ) . ' o botão é a busca sem rastreio' ),
	'na borda, o item sem rastreio aparece na parcela dele' );

$GLOBALS['__options'][ $chave_borda ] = $guardado;
cdm_teste_rebobinar();

/* A escada de fontes tem que CHEGAR A TELA, e nao so estar certa na funcao. */
$corpo_prova = cdm_texto( cdm_corpo( $html_por_pagina['cdm_como_sabemos'] ) );
$degraus_fora = array();
foreach ( cdm_casca_escada_de_fontes() as $degrau ) {
	if ( false === mb_stripos( $corpo_prova, $degrau['origem'] ) ) {
		$degraus_fora[] = $degrau['nivel'];
	}
}
cdm_ok( empty( $degraus_fora ), 'os sete degraus da escada aparecem no corpo da pagina de prova',
	empty( $degraus_fora ) ? '7 degraus' : 'faltam ' . implode( ', ', $degraus_fora ) );

/* ---------------------------------------------------------------------------
 * 16. NOINDEX E SITEMAP — medidos nos DOIS sentidos
 *
 * `noindex` indevido tira do indice uma pagina que rankeia, e e defeito que
 * ninguem ve olhando a tela. Entao o teste cobra as duas direcoes: a pagina
 * declarada sai, e toda outra fica.
 * ------------------------------------------------------------------------- */

echo "\n15b. A meta description das paginas da casca (item 4 do despacho de 28/09)\n";

/* A REGUA E DAQUI, NAO DA CASCA. A faixa 120-160 esta escrita literal nesta
   linha e o veredito de cada pagina sai da contagem de CARACTERES decodificados
   — nao de bytes, que numa lingua com acento dao outro numero. A casca nao tem
   voz nenhuma sobre o que e "faixa util": se alguem afrouxar a regra la, esta
   linha discorda, que e o ponto.
      POR QUE 160 E O TETO: acima disso o Google corta e a promessa da SERP
   termina no meio. As QUATRO descricoes que esta ilha tinha em 28/09/2026
   estavam TODAS acima — 167, 188, 194 e 200 — e as outras OITO paginas nao
   tinham etiqueta nenhuma.
      POR QUE 120 E O PISO: descricao curta demais o Google descarta e escreve a
   dele a partir do texto, e a linha que decide o clique volta a nao ser nossa. */
$PISO_DESC = 120;
$TETO_DESC = 160;

$descricoes  = array();
$sem_desc    = array();
$fora_faixa  = array();
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	if ( ! empty( $def['noindex'] ) ) {
		continue; /* pagina fora do indice nao disputa clique na SERP */
	}
	$d = cdm_casca_descricao_declarada( $slug );
	if ( '' === $d ) {
		$sem_desc[] = $slug;
		continue;
	}
	$n = mb_strlen( $d, 'UTF-8' );
	if ( $n < $PISO_DESC || $n > $TETO_DESC ) {
		$fora_faixa[] = $slug . ' (' . $n . ')';
	}
	$descricoes[ $slug ] = $d;
}

/* AS PAGINAS QUE A CASCA DECLARA, e so elas. As duas ferramentas e os dois
   tutoriais entram na definicao pelo filtro `cdm_paginas`, vindos do proprio
   snippet, e a descricao deles e declarada LA, pelo filtro `cdm_descricao` — a
   da ferramenta no arquivo dela, a do tutorial na ficha de `tecnicas`. Elas nao
   tem a chave `descricao` aqui e nao deveriam ter: dois lugares declarando a
   mesma etiqueta e o defeito que este bloco inteiro conserta.
      AS QUATRO ESTAO ACIMA DE 160 CARACTERES e continuam assim de proposito,
   com o motivo em despacho de prioridade maior: TRES delas estao na primeira
   pagina do Google e o BLOCO A do despacho do Raphael de 24/09 proibe mexer na
   promessa da SERP delas antes de 30/09 — trocar agora misturaria duas causas na
   mesma janela. A quarta (Trencadis) fica parada pelo que o mesmo despacho
   escreve: "deixe uma pagina parada para a proxima leitura ter com o que
   comparar". A afirmacao logo abaixo mede isso e NAO reprova; ela existe para o
   numero ficar visivel em vez de esquecido. */
$declaram_no_proprio_snippet = array(
	'materiais/qual-cola-usar-no-mosaico',
	'materiais/quantas-pastilhas-para-mosaico',
	'como-fazer/o-que-e-mosaico-picassiete',
	'como-fazer/o-que-e-trencadis',
);
$sem_desc_da_casca = array_values( array_diff( $sem_desc, $declaram_no_proprio_snippet ) );
$travadas_presentes = array_values( array_intersect( $declaram_no_proprio_snippet, array_keys( cdm_casca_definicao_paginas() ) ) );
cdm_ok( count( $travadas_presentes ) === count( $declaram_no_proprio_snippet ),
	'as quatro paginas que declaram no proprio snippet continuam registradas na arvore',
	implode( ', ', $travadas_presentes ) );
cdm_ok( empty( $sem_desc_da_casca ), 'toda pagina da casca que entra no indice declara uma description',
	empty( $sem_desc_da_casca ) ? count( $descricoes ) . ' paginas' : implode( ', ', $sem_desc_da_casca ) );
cdm_ok( empty( $fora_faixa ), 'e todas cabem na faixa de 120 a 160 caracteres',
	empty( $fora_faixa ) ? count( $descricoes ) . ' de ' . count( $descricoes ) : implode( ' | ', $fora_faixa ) );

/* NENHUMA SE REPETE. Descricao duplicada entre paginas e o sinal que faz o
   buscador tratar duas URLs como a mesma coisa, e esta ilha tem tres maes que se
   parecem na arvore da secao 16. A comparacao e por texto inteiro E por
   prefixo longo: duas descricoes que so divergem na ultima palavra sao a mesma
   promessa na SERP. */
cdm_ok( count( array_unique( $descricoes ) ) === count( $descricoes ),
	'nenhuma description se repete inteira entre paginas',
	count( $descricoes ) . ' textos, ' . count( array_unique( $descricoes ) ) . ' distintos' );
$prefixos = array();
foreach ( $descricoes as $slug => $d ) {
	$prefixos[ $slug ] = mb_substr( $d, 0, 60, 'UTF-8' );
}
cdm_ok( count( array_unique( $prefixos ) ) === count( $prefixos ),
	'nem nos 60 primeiros caracteres, que e o que a SERP mostra antes de cortar',
	implode( ' | ', array_diff_assoc( $prefixos, array_unique( $prefixos ) ) ) );

/* O EMISSOR E UM SO, e e isto que o item 4 do despacho pede de verdade — ele diz
   com todas as letras que o defeito "nao e o texto de uma pagina: e qual camada
   emite a etiqueta e para quais tipos de pagina". Ate 28/09 cada camada dava
   `echo` na propria e as paginas da casca nao tinham camada nenhuma. Agora quem
   tem descricao DECLARA pelo filtro `cdm_descricao` e quem imprime e a casca.
      A contagem abaixo e sobre o CODIGO dos snippets, e nao sobre o HTML: e a
   unica regua que pega a camada nova que nascer dando echo na propria — que e
   como a etiqueta de ROBO chegou a sair dobrada nesta mesma ilha em 25/09. */
$pasta_snippets = dirname( __DIR__ ) . '/snippets';
$echos_de_description = array();
foreach ( glob( $pasta_snippets . '/*.php' ) as $arquivo ) {
	$fonte = file_get_contents( $arquivo );
	$n     = preg_match_all( '#echo[^\n]{0,8}<meta name="description"#', $fonte );
	if ( $n > 0 && 'clubedomosaico-casca.php' !== basename( $arquivo ) ) {
		$echos_de_description[] = basename( $arquivo ) . ' (' . $n . ')';
	}
}
cdm_ok( empty( $echos_de_description ),
	'nenhum snippet fora da casca imprime a propria meta description',
	empty( $echos_de_description ) ? 'so a casca' : implode( ', ', $echos_de_description ) );
$fonte_casca = file_get_contents( $pasta_snippets . '/clubedomosaico-casca.php' );
cdm_ok( 1 === preg_match_all( '#echo[^\n]{0,8}<meta name="description"#', $fonte_casca ),
	'e a casca imprime em UM lugar so',
	preg_match_all( '#echo[^\n]{0,8}<meta name="description"#', $fonte_casca ) . ' lugares' );

/* PAGINA SEM DESCRICAO SAI SEM ETIQUETA, e nao com uma generica: descricao
   generica repetida e pior que ausencia, porque a ausencia faz o Google escrever
   uma a partir do texto DAQUELA pagina. */
cdm_ok( '' === cdm_casca_descricao_declarada( 'pagina-que-nao-existe' ),
	'slug desconhecido devolve vazio em vez de uma descricao generica' );

echo "\n15d. A promessa numerica do <title> — as tres travas (BLOCO A, fechado em 02/10/2026)\n";

/* A REGUA E DAQUI. `cdm_casca_titulo_do_documento()` e pura — recebe o nome e o
   slug e devolve o texto —, e e por isso que estas afirmacoes podem medir o
   MUNDO e nao o estado de hoje do banco: a promessa de teste nasce aqui, num
   slug que nao existe no site, e as travas sao exercidas uma por uma.
      POR QUE ISTO NAO E LUXO: as travas 1 e 2 sao SILENCIOSAS por desenho — elas
   devolvem a marca e nao falham —, e trava silenciosa que ninguem viu reprovar
   nao mediu nada (secao 8 do ARQUIPELAGO.md). */
$nome_de_teste = 'Nome de pagina com 38 caracteres aqui';

cdm_ok( $nome_de_teste . ' – ' . CDM_CASCA_NOME_SITE === cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-sem-promessa' ),
	'pagina sem promessa serve o nome mais a MARCA, como sempre serviu',
	cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-sem-promessa' ) );

add_filter( 'cdm_promessa', function ( $p, $slug ) {
	if ( 'slug-de-teste-que-cabe' === $slug ) {
		return cdm_casca_preencher_promessa( '{a} colas para {b} bases', array( 'a' => 7, 'b' => 9 ) );
	}
	if ( 'slug-de-teste-que-estoura' === $slug ) {
		return cdm_casca_preencher_promessa( '{a} colas para {b} bases em {c} lugares e {d} caquinhos', array( 'a' => 7, 'b' => 9, 'c' => 5, 'd' => 6 ) );
	}
	if ( 'slug-de-teste-sem-banco' === $slug ) {
		return cdm_casca_preencher_promessa( '{a} colas para {b} bases', array( 'a' => 0, 'b' => 9 ) );
	}
	if ( 'slug-de-teste-com-chave-esquecida' === $slug ) {
		return cdm_casca_preencher_promessa( '{a} colas para {b} bases', array( 'a' => 7 ) );
	}
	return $p;
}, 10, 2 );

cdm_ok( $nome_de_teste . ' – 7 colas para 9 bases' === cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-cabe' ),
	'promessa que cabe no teto ENTRA, e a marca sai do fim',
	cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-cabe' ) );

cdm_ok( mb_strlen( cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-cabe' ), 'UTF-8' ) <= CDM_CASCA_TITULO_TETO,
	'e o titulo inteiro cabe no teto de ' . CDM_CASCA_TITULO_TETO,
	mb_strlen( cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-cabe' ), 'UTF-8' ) . ' caracteres' );

/* TRAVA 1 — a promessa que estoura o teto NAO entra, e o titulo volta a ser o
   nome mais a marca, que e sempre valido. Promessa cortada no meio pelo Google
   e pior que promessa nenhuma. */
cdm_ok( $nome_de_teste . ' – ' . CDM_CASCA_NOME_SITE === cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-estoura' ),
	'TRAVA 1: promessa que estoura o teto devolve a marca',
	cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-que-estoura' ) );

/* TRAVA 2 — banco que nao chegou. Zero e recusa, e nao "0 colas": a frase e
   verdadeira e nao serve, e no resultado da busca ela custa o clique. */
cdm_ok( $nome_de_teste . ' – ' . CDM_CASCA_NOME_SITE === cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-sem-banco' ),
	'TRAVA 2: numero ausente ou zero recusa o molde INTEIRO e devolve a marca',
	cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-sem-banco' ) );

cdm_ok( false === strpos( cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-com-chave-esquecida' ), '{' ),
	'e chave esquecida pelo molde nunca chega ao <title>',
	cdm_casca_titulo_do_documento( $nome_de_teste, 'slug-de-teste-com-chave-esquecida' ) );

cdm_ok( '' === cdm_casca_preencher_promessa( '{a} colas', array( 'a' => 'sete' ) )
	&& '' === cdm_casca_preencher_promessa( '{a} colas', array( 'a' => -3 ) )
	&& '' === cdm_casca_preencher_promessa( '', array( 'a' => 7 ) )
	&& '' === cdm_casca_preencher_promessa( '{a} colas', array() ),
	'o preenchedor recusa texto, negativo, molde vazio e lista vazia' );

cdm_ok( '' === cdm_casca_titulo_do_documento( '', 'slug-de-teste-que-cabe' ),
	'pagina sem nome nao ganha titulo montado a partir da promessa sozinha' );

/* O MONTADOR E UM SO, e esta e a mesma regua do emissor da description: a
   contagem e sobre o CODIGO dos snippets, que e a unica que pega a camada nova
   que nascer penduando o proprio filtro. A Loja tem o dela por desenho (ela
   monta o titulo da PECA, que nao tem nome na arvore da casca); qualquer
   terceiro e defeito. */
$filtros_de_titulo = array();
foreach ( glob( $pasta_snippets . '/*.php' ) as $arquivo ) {
	$fonte = file_get_contents( $arquivo );
	$n     = preg_match_all( "#add_filter\(\s*'document_title_parts'#", $fonte );
	if ( $n > 0 ) {
		$filtros_de_titulo[ basename( $arquivo ) ] = $n;
	}
}
cdm_ok( array( 'clubedomosaico-casca.php' => 1, 'clubedomosaico-loja.php' => 1 ) === $filtros_de_titulo,
	'so a casca e a Loja montam <title>, uma vez cada',
	implode( ', ', array_map( function ( $k, $v ) { return $k . ' (' . $v . ')'; }, array_keys( $filtros_de_titulo ), $filtros_de_titulo ) ) );

/* QUEM DECLARA PROMESSA HOJE: as TRES paginas que a leitura de 23/09 mediu na
   primeira pagina com CTR zero, e mais nenhuma. O Trencadis fica parado de
   proposito, para a leitura seguinte ter com o que comparar — e e por isso que
   esta afirmacao mede a lista INTEIRA, nas duas direcoes, em vez de so conferir
   as tres. */
$com_promessa = array();
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	if ( '' !== cdm_casca_promessa_do_titulo( $slug ) ) {
		$com_promessa[] = $slug;
	}
}
sort( $com_promessa );
$esperadas_com_promessa = array(
	'como-fazer/o-que-e-mosaico-picassiete',
	'materiais/qual-cola-usar-no-mosaico',
	'materiais/quantas-pastilhas-para-mosaico',
);
cdm_ok( $esperadas_com_promessa === $com_promessa,
	'as TRES paginas de primeira pagina declaram promessa, e nenhuma outra',
	implode( ' | ', $com_promessa ) );

echo "\n16. Noindex declarado e sitemap como curadoria (secao 14.1)\n";
$ids_falsos = array();
$i_falso    = 100;
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	$ids_falsos[ $slug ] = $i_falso++;
}
$GLOBALS['__options']['cdm_casca_paginas'] = $ids_falsos;

/* A REGUA DESTA SECAO E DAQUI, e ela e a de um leitor de HTML e nao a da casca
   (regra 1 do cabecalho): `cdm_robots_texto()` monta a etiqueta do jeito que o
   `wp_robots()` do nucleo monta — juntando as diretivas com virgula, chave
   sozinha quando o valor e true, `chave:valor` quando e texto. Se a casca
   devolver o vetor na ordem errada, ou com diretiva a mais, este texto mostra.

   O NUCLEO ENTRA AQUI TAMBEM, e e o que faz a medicao valer: toda chamada parte
   de `array( 'max-image-preview' => 'large' )`, que e exatamente o que o
   `wp_robots_max_image_preview()` do WordPress ja pos no vetor na prioridade 10
   quando a nossa funcao roda na 20. Medir com vetor vazio aprovaria a casca que
   deixa a diretiva do nucleo colada no noindex. */
function cdm_robots_texto( $robots ) {
	$partes = array();
	foreach ( $robots as $diretiva => $valor ) {
		if ( is_string( $valor ) ) {
			$partes[] = $diretiva . ':' . $valor;
		} elseif ( $valor ) {
			$partes[] = $diretiva;
		}
	}
	return implode( ', ', $partes );
}

$do_nucleo = array( 'max-image-preview' => 'large' );
$contexto  = function ( $extra ) use ( $ids_falsos ) {
	return array_merge( array(
		'id'               => 0,
		'ids_da_casca'     => $ids_falsos,
		'arquivo_de_autor' => false,
		'busca'            => false,
	), $extra );
};

$errados = array();
foreach ( $ids_falsos as $slug => $id ) {
	$deve_sair = in_array( $slug, cdm_casca_paginas_noindex(), true );
	$texto     = cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $id ) ) ) );
	$saiu      = ( false !== strpos( $texto, 'noindex' ) );
	if ( $deve_sair !== $saiu ) {
		$errados[] = $slug;
	}
}
cdm_ok( empty( $errados ), 'a etiqueta noindex sai exatamente nas paginas declaradas',
	empty( $errados ) ? count( $ids_falsos ) . ' paginas' : implode( ', ', $errados ) );

$fora_declarada = cdm_casca_paginas_noindex();
$id_declarado   = $ids_falsos[ $fora_declarada[0] ];

cdm_ok( 'noindex, follow' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $id_declarado ) ) ) ),
	'pagina declarada serve EXATAMENTE noindex, follow',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $id_declarado ) ) ) ) );

/* O defeito de 1.12.0, medido no ar em 25/09/2026: a casca injetava a etiqueta
   dela num `wp_head` proprio e o nucleo imprimia a dele, e a pagina saia com
   DUAS <meta name="robots">. Com o filtro isso deixa de ser possivel por
   construcao — o que existe e UM vetor —, e esta afirmacao e quem cobra que o
   caminho continue sendo o filtro: ela falha no dia em que alguem devolver
   markup em vez de diretiva. */
$vetor_declarado = cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $id_declarado ) ) );
$tem_markup      = false;
foreach ( array_merge( array_keys( $vetor_declarado ), array_values( $vetor_declarado ) ) as $pedaco ) {
	if ( is_string( $pedaco ) && false !== strpos( $pedaco, '<' ) ) {
		$tem_markup = true;
	}
}
cdm_ok( ! $tem_markup, 'a casca devolve DIRETIVA, nunca etiqueta pronta (uma meta so)',
	count( $vetor_declarado ) . ' diretivas' );

cdm_ok( ! isset( $vetor_declarado['max-image-preview'] ),
	'max-image-preview sai quando a pagina sai do indice',
	isset( $vetor_declarado['max-image-preview'] ) ? 'ficou' : 'saiu' );

/* Os dois contextos que a Sentinela mediu em 23/09/2026. O arquivo de autor
   tomou impressao na posicao 1,0 sem ser pagina desta ilha; a busca interna
   ainda nao tem sintoma e fecha na mesma linha. */
cdm_ok( 'noindex, follow' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'arquivo_de_autor' => true ) ) ) ),
	'o arquivo de autor sai do indice (/author/mosaico_gestor/)',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'arquivo_de_autor' => true ) ) ) ) );
cdm_ok( 'noindex, follow' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'busca' => true ) ) ) ),
	'a busca interna sai do indice (/?s=<termo>)',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'busca' => true ) ) ) ) );

/* O OUTRO LADO DA BORDA, e e o lado caro: `noindex` indevido tira do indice uma
   pagina que rankeia. As tres paginas com posicao medida desta ilha entram aqui
   por ID, nao por fe. */
cdm_ok( 'max-image-preview:large' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array() ) ) ),
	'sem pagina identificada, o vetor do nucleo passa intacto',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array() ) ) ) );
cdm_ok( 'max-image-preview:large' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => 999 ) ) ) ),
	'pagina de fora da casca nao recebe noindex',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => 999 ) ) ) ) );
cdm_ok( 'max-image-preview:large' === cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $ids_falsos['inicio'] ) ) ) ),
	'a home NAO sai do indice',
	cdm_robots_texto( cdm_casca_robots_diretivas( $do_nucleo, $contexto( array( 'id' => $ids_falsos['inicio'] ) ) ) ) );

$args = cdm_casca_sitemap_sem_noindex( array(), 'page' );
$fora_do_sitemap = isset( $args['post__not_in'] ) ? $args['post__not_in'] : array();
cdm_ok( count( $fora_do_sitemap ) === count( cdm_casca_paginas_noindex() ),
	'o sitemap exclui exatamente as paginas noindex', count( $fora_do_sitemap ) . ' excluidas' );
foreach ( cdm_casca_paginas_noindex() as $slug ) {
	cdm_ok( in_array( $ids_falsos[ $slug ], $fora_do_sitemap, true ), "'$slug' fica fora do sitemap" );
}
$args_post = cdm_casca_sitemap_sem_noindex( array(), 'post' );
cdm_ok( ! isset( $args_post['post__not_in'] ), 'o filtro nao mexe no sitemap de posts' );
$args_ja = cdm_casca_sitemap_sem_noindex( array( 'post__not_in' => array( 7 ) ), 'page' );
cdm_ok( in_array( 7, $args_ja['post__not_in'], true ), 'o filtro preserva exclusao de quem veio antes' );

/* O ARQUIVO DE AUTOR FORA DO SITEMAP — defeito medido no ar em 14/09/2026.
   Ele nasceu sozinho: o provedor `users` do nucleo so lista autor que TEM
   conteudo publicado, e ate 13/09 esta ilha nao tinha peca nenhuma. No minuto em
   que a artesa publicou a primeira, /author/artesa/ entrou no wp-sitemap.xml —
   pagina fina que repete a /loja/, e um endereco que confirma o login dela.
   A regua e escrita a mao: o nome do provedor e a resposta esperada estao nesta
   linha, nao lidos do snippet. */
cdm_ok( false === apply_filters( 'wp_sitemaps_add_provider', 'PROVEDOR', 'users' ),
	'o provedor de autores e removido do sitemap (/author/ nao pede rastreamento)' );
foreach ( array( 'posts', 'taxonomies' ) as $provedor_vivo ) {
	cdm_ok( 'PROVEDOR' === apply_filters( 'wp_sitemaps_add_provider', 'PROVEDOR', $provedor_vivo ),
		"e o provedor '$provedor_vivo' continua de pe (a remocao nao vazou)" );
}
unset( $GLOBALS['__options']['cdm_casca_paginas'] );

/* ---------------------------------------------------------------------------
 * 17. A ARVORE COMECOU (secao 16 do contrato)
 *
 * A primeira pagina de nivel 2 desta ilha. A trava aqui e pequena de proposito:
 * pagina com mae tem que ter a mae criada ANTES dela, senao ela nasce solta na
 * raiz — e pagina sem pai e defeito que nao publica.
 * ------------------------------------------------------------------------- */

echo "\n17. Pagina com mae (secao 16.2)\n";
$ordem  = array_keys( cdm_casca_definicao_paginas() );
$sem_mae = array();
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	if ( empty( $def['pai'] ) ) {
		if ( false !== strpos( $slug, '/' ) ) {
			$sem_mae[] = $slug . ' (tem nivel na URL e nao declara mae)';
		}
		continue;
	}
	if ( ! isset( $definicoes[ $def['pai'] ] ) ) {
		$sem_mae[] = $slug . ' (mae ' . $def['pai'] . ' nao existe)';
		continue;
	}
	if ( array_search( $def['pai'], $ordem, true ) > array_search( $slug, $ordem, true ) ) {
		$sem_mae[] = $slug . ' (a mae vem depois dela na definicao)';
	}
	if ( 0 !== strpos( $slug, $def['pai'] . '/' ) ) {
		$sem_mae[] = $slug . ' (a URL nao mostra a mae)';
	}
}
cdm_ok( empty( $sem_mae ), 'toda pagina de nivel 2 declara a mae, e a mae vem antes',
	empty( $sem_mae ) ? 'ok' : implode( ' | ', $sem_mae ) );
cdm_ok( 'como-sabemos' === cdm_casca_slug_final( 'materiais/como-sabemos' ), 'o slug gravado e o ultimo nivel do caminho' );
cdm_ok( 'materiais' === cdm_casca_slug_final( 'materiais' ), 'caminho de um nivel so continua sendo ele mesmo' );

/* ---------------------------------------------------------------------------
 * 18. AS IMAGENS DA IDENTIDADE ABREM
 *
 * Trava nascida de um achado desta execucao: identidade/logo/lotus-512.png esta
 * TRUNCADO no repositorio (IDAT de 11.638 bytes num arquivo de 8.770) e nao
 * decodifica um unico pixel. O despacho mandava servi-lo no cabecalho claro.
 * A regra que fica: imagem que a casca SERVE tem que abrir, conferida chunk a
 * chunk — "o arquivo existe e tem bytes" nao e medicao de imagem.
 * ------------------------------------------------------------------------- */

echo "\n18. Imagem servida pela casca abre de verdade\n";

/** '' quando o PNG esta inteiro; o motivo quando nao esta. */
function cdm_png_quebrado( $bruto ) {
	if ( "\x89PNG\r\n\x1a\n" !== substr( (string) $bruto, 0, 8 ) ) {
		return 'nao comeca com a assinatura de PNG';
	}
	$i = 8;
	$t = strlen( $bruto );
	while ( $i + 8 <= $t ) {
		$tamanho = unpack( 'N', substr( $bruto, $i, 4 ) )[1];
		$tipo    = substr( $bruto, $i + 4, 4 );
		$fim     = $i + 12 + $tamanho;
		if ( $fim > $t ) {
			return sprintf( 'chunk %s declara %d bytes e faltam %d (truncado)', $tipo, $tamanho, $fim - $t );
		}
		if ( crc32( $tipo . substr( $bruto, $i + 8, $tamanho ) ) !== unpack( 'N', substr( $bruto, $i + 8 + $tamanho, 4 ) )[1] ) {
			return sprintf( 'chunk %s com CRC errado', $tipo );
		}
		if ( 'IEND' === $tipo ) {
			return '';
		}
		$i = $fim;
	}
	return 'acabou sem IEND';
}

/* Os PNG que a casca SERVE sao os que viajam embutidos no snippet. */
$embutidos = array( 'favicon 32' => CDM_CASCA_ICONE_PNG_32 );
if ( defined( 'CDM_CASCA_MARCA_LOTUS' ) && '' !== CDM_CASCA_MARCA_LOTUS ) {
	$embutidos['lotus do cabecalho'] = CDM_CASCA_MARCA_LOTUS;
}
foreach ( $embutidos as $nome => $base64 ) {
	$motivo = cdm_png_quebrado( base64_decode( $base64 ) );
	cdm_ok( '' === $motivo, "o PNG embutido ($nome) abre chunk a chunk", '' === $motivo ? strlen( base64_decode( $base64 ) ) . ' bytes' : $motivo );
}
/* Teste negativo: a regua reprova mesmo. Sem isto ela poderia estar aprovando
   tudo por engano — inclusive o arquivo que motivou a trava. */
cdm_ok( '' !== cdm_png_quebrado( substr( base64_decode( CDM_CASCA_ICONE_PNG_32 ), 0, 200 ) ),
	'a regua de PNG reprova um arquivo cortado (teste negativo)' );
cdm_ok( '' !== cdm_png_quebrado( (string) @file_get_contents( $raiz . '/identidade/logo/lotus-512.png' ) ),
	'a regua reconhece o lotus-512.png truncado como quebrado',
	cdm_png_quebrado( (string) @file_get_contents( $raiz . '/identidade/logo/lotus-512.png' ) ) );

/* ---------------------------------------------------------------------------
 * 19. O TITULO SE SINCRONIZA NA PAGINA QUE JA EXISTE
 *
 * Esta e a trava que o proprio mutante achou faltando: medir o H1 servido na
 * bancada nunca poderia ver este defeito, porque a bancada monta o H1 a partir
 * da DEFINICAO — e a definicao esta certa. O defeito mora no outro lado, no
 * caminho que atualiza a pagina que ja existe no WordPress: sem ele, a pagina
 * nasce com um titulo e fica com ele para sempre, e foi assim que a palavra
 * "Inicio" sobreviveu a duas versoes da casca no ar.
 *
 * Entao aqui o teste simula o site REAL de hoje — as paginas existem, com os
 * titulos velhos — e afirma sobre o que a casca MANDA gravar.
 * ------------------------------------------------------------------------- */

echo "\n19. O titulo da pagina que ja existe se sincroniza (secao 8)\n";

$GLOBALS['__paginas_objeto'] = array();
$GLOBALS['__meta']           = array();
$id_falso                    = 200;
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	$id_falso++;
	$GLOBALS['__paginas_objeto'][ $slug ] = (object) array(
		'ID'           => $id_falso,
		'post_title'   => 'inicio' === $slug ? 'Início' : $def['titulo'],
		'post_name'    => cdm_casca_slug_final( $slug ),
		'post_status'  => 'publish',
		'post_content' => $def['conteudo'],
		'post_parent'  => 0,
	);
	$GLOBALS['__meta'][ $id_falso ] = array( '_cdm_casca' => '1' );
}
$GLOBALS['__updates'] = array();
$relato_teste         = array();
cdm_casca_garantir_paginas( $relato_teste );

$mandou_titulo = array();
$mandou_slug   = false;
foreach ( $GLOBALS['__updates'] as $u ) {
	if ( isset( $u['post_title'] ) ) {
		$mandou_titulo[ (int) $u['ID'] ] = $u['post_title'];
	}
	if ( isset( $u['post_name'] ) ) {
		$mandou_slug = true;
	}
}
$id_da_home = $GLOBALS['__paginas_objeto']['inicio']->ID;
cdm_ok( isset( $mandou_titulo[ $id_da_home ] ) && $definicoes['inicio']['titulo'] === $mandou_titulo[ $id_da_home ],
	'a home que ja existe com o titulo velho recebe o titulo novo',
	isset( $mandou_titulo[ $id_da_home ] ) ? '"' . $mandou_titulo[ $id_da_home ] . '"' : 'nenhuma gravacao' );
cdm_ok( 1 === count( $mandou_titulo ), 'so o titulo que estava diferente e regravado',
	count( $mandou_titulo ) . ' gravacao(oes)' );
/* URL DE PAGINA PUBLICADA NAO SE MOVE (secao 12.1). Sincronizar titulo e uma
   coisa; mexer no endereco e outra, e esta e proibida. */
cdm_ok( false === $mandou_slug, 'nenhuma gravacao toca o post_name (URL publicada nao se move)' );

/* A BORDA: pagina que NAO e nossa nao tem o titulo reescrito. Alguem pode ter
   criado uma pagina com o mesmo slug antes da ilha existir — o dominio teve
   vida anterior —, e a casca nao e dona dela. */
$GLOBALS['__meta'][ $id_da_home ] = array();
$GLOBALS['__updates']             = array();
$relato_teste                     = array();
cdm_casca_garantir_paginas( $relato_teste );
$tocou_alheia = false;
foreach ( $GLOBALS['__updates'] as $u ) {
	if ( (int) $u['ID'] === $id_da_home && isset( $u['post_title'] ) ) {
		$tocou_alheia = true;
	}
}
cdm_ok( ! $tocou_alheia, 'pagina que nao e da casca nao tem o titulo reescrito' );

$GLOBALS['__paginas_objeto'] = array();
$GLOBALS['__meta']           = array();
$GLOBALS['__updates']        = array();

/* ---------------------------------------------------------------------------
 * 20. NOINDEX SO ONDE ELE PODE ESTAR
 *
 * A segunda trava que o mutante achou faltando. O teste da secao 16 conferia que
 * a etiqueta sai nas paginas DECLARADAS — o que e verdade mesmo quando alguem
 * declara a pagina errada. Conferir a declaracao contra ela mesma e a mesma
 * forma do teste que mede a si mesmo: a regua tem que vir de fora.
 *
 * A regua de fora: so a pagina de camada de prova pode sair do indice. A home e
 * toda pagina do menu sao o motivo de a ilha existir; `noindex` nelas e defeito
 * caro e invisivel — na tela nao muda nada.
 * ------------------------------------------------------------------------- */

echo "\n20. Noindex so na pagina de bastidor (secao 14.1)\n";
/* DUAS RAZOES PARA SAIR DO INDICE, E SO DUAS, cada uma DECLARADA na definicao.
 *
 * Isto era "so a pagina de camada de prova sai do indice", e a regra estava certa
 * enquanto a ilha tinha uma razao so. O bloco 4d trouxe a segunda: /atelie/ e a
 * area de uma pessoa. Perdoar o slug 'atelie' por nome seria a heuristica por
 * vizinhanca que a secao 8 proibe — bastaria uma pagina futura se chamar assim.
 * Entao a regua cobra a DECLARACAO, e nomeia as duas camadas admitidas; camada
 * nova exige mexer aqui, que e o ponto.
 *
 * A contagem tambem deixa de ser "uma": ela e recontada das definicoes, e o que
 * se cobra e a EQUIVALENCIA entre "tem noindex" e "declara camada de bastidor".
 * As duas direcoes, porque as duas doem: noindex sem camada e pagina que sumiu do
 * indice sem ninguem declarar, e camada sem noindex e bastidor pedindo
 * rastreamento (secao 14.1). */
$menu_da_ilha = array( 'inicio', 'loja', 'materiais', 'como-fazer', 'sobre' );
$camadas_de_bastidor = array( 'prova', 'privada' );
$fora_indevido = array();
foreach ( cdm_casca_paginas_noindex() as $slug ) {
	$def = $definicoes[ $slug ];
	if ( ! isset( $def['camada'] ) || ! in_array( $def['camada'], $camadas_de_bastidor, true ) ) {
		$fora_indevido[] = $slug . ' (noindex sem camada declarada)';
	}
	if ( in_array( $slug, $menu_da_ilha, true ) ) {
		$fora_indevido[] = $slug . ' (esta no menu da ilha)';
	}
}
/* O outro sentido, que nenhuma versao anterior cobrava. */
foreach ( $definicoes as $slug => $def ) {
	if ( isset( $def['camada'] ) && in_array( $def['camada'], $camadas_de_bastidor, true )
		&& ! in_array( $slug, cdm_casca_paginas_noindex(), true ) ) {
		$fora_indevido[] = $slug . ' (camada ' . $def['camada'] . ' DENTRO do indice)';
	}
}
cdm_ok( empty( $fora_indevido ), 'toda pagina fora do indice declara a camada, e vice-versa',
	empty( $fora_indevido ) ? implode( ', ', cdm_casca_paginas_noindex() ) : implode( ' | ', $fora_indevido ) );

/* E A CAMADA DE PROVA CONTINUA SENDO UMA SO. Era esta a metade que valia da
   afirmacao antiga, e ela nao pode ser perdida no caminho: sem ela bastaria
   declarar a home como prova para o portao de voz da secao 15.2 parar de valer —
   a porta dos fundos que a Aquametria achou em 11/09/2026. */
$de_prova = array();
foreach ( $definicoes as $slug => $def ) {
	if ( isset( $def['camada'] ) && 'prova' === $def['camada'] ) { $de_prova[] = $slug; }
}
cdm_ok( 1 === count( $de_prova ), 'exatamente uma pagina e camada de prova',
	implode( ', ', $de_prova ) );

$indexaveis = array_diff( array_keys( $definicoes ), cdm_casca_paginas_noindex() );
cdm_ok( count( $indexaveis ) === count( $definicoes ) - count( cdm_casca_paginas_noindex() ),
	'as indexaveis sao todas as que nao declaram bastidor',
	count( $indexaveis ) . ' de ' . count( $definicoes ) . ' indexaveis' );

/* ---------------------------------------------------------------------------
 * 21. A ARVORE DA SECAO 16 — trilha, BreadcrumbList e cluster
 *
 * A regua e propria em todas as afirmacoes abaixo (secao 8, regra 1): o esperado
 * sai do ARVORE.md e do VOZ.md, que sao documento, e o medido sai do HTML
 * servido pelo render em processo proprio. Nenhuma afirmacao pergunta a casca o
 * que ela deveria dizer — se codigo e documento se separarem, os dois lados nao
 * erram juntos.
 *
 * E tudo que e sobre texto visivel e medido no CORPO, nunca no HTML completo: a
 * trilha nasce entre o cabecalho e o H1, e afirmar sobre ela lendo a pagina
 * inteira acharia tambem as regras de CSS que carregam o mesmo nome de classe.
 * ------------------------------------------------------------------------- */

echo "\n21. A arvore: documento x codigo (secao 16 e 16.8)\n";

$arvore_md = (string) @file_get_contents( $raiz . '/ARVORE.md' );
cdm_ok( '' !== $arvore_md, 'ARVORE.md existe (item i do 16.8)', strlen( $arvore_md ) . ' bytes' );

/* (a) A TABELA DE ONDE MORA CADA PAGINA, lida do documento. */
$doc_arvore = array();
foreach ( explode( "\n", $arvore_md ) as $linha ) {
	if ( ! preg_match( '#^\|\s*`(/[^`]*)`\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|#u', $linha, $m ) ) {
		continue;
	}
	$caminho = trim( $m[1], '/' );
	$nivel   = trim( $m[2] );
	$mae     = trim( $m[3] );
	if ( '' === $caminho ) {
		continue; // a home, que por 16.3 nao tem trilha e nao entra no mapa
	}
	if ( 'raiz' === $nivel ) {
		$nivel_n = 0;
	} elseif ( ctype_digit( $nivel ) ) {
		$nivel_n = (int) $nivel;
	} else {
		continue; // linha de outra tabela
	}
	if ( 'home' === $mae || '—' === $mae ) {
		$mae_c = '';
	} elseif ( preg_match( '#`(/[^`]*)`#u', $mae, $mm ) ) {
		$mae_c = trim( $mm[1], '/' );
	} else {
		continue;
	}
	$doc_arvore[ $caminho ] = array( 'nivel' => $nivel_n, 'mae' => $mae_c );
}
cdm_ok( count( $doc_arvore ) >= 8, 'ARVORE.md declara onde mora cada pagina que existe hoje',
	count( $doc_arvore ) . ' linhas lidas do documento' );

/* A PECA SAI DO LACO GERAL, e a separacao e a metade honesta do conserto de
   28/09/2026. O mapa da casca e por REQUISICAO e a peca so entra nele quando
   esta sendo servida (decisao declarada no filtro `cdm_arvore` do snippet da
   Loja, para a lista de irmas de /loja/ nao encher de peca). Medir a linha
   dela no mapa montado fora de uma requisicao de peca reprovaria uma pagina
   que esta CERTA — foi por isso que a linha da peca ficou quatorze dias fora
   da tabela. Ela e medida logo abaixo, com a situacao fabricada. */
$doc_pecas = array();
foreach ( array_keys( $doc_arvore ) as $caminho ) {
	if ( 0 === strpos( $caminho, 'loja/' ) ) {
		$doc_pecas[ $caminho ] = $doc_arvore[ $caminho ];
		unset( $doc_arvore[ $caminho ] );
	}
}

$mapa_codigo = cdm_casca_arvore();
$divergem    = array();
foreach ( $doc_arvore as $caminho => $esperado_linha ) {
	if ( ! isset( $mapa_codigo[ $caminho ] ) ) {
		$divergem[] = $caminho . ' (no documento e nao no codigo)';
		continue;
	}
	if ( (int) $mapa_codigo[ $caminho ]['nivel'] !== (int) $esperado_linha['nivel'] ) {
		$divergem[] = $caminho . ' (nivel ' . $mapa_codigo[ $caminho ]['nivel'] . ' no codigo, ' . $esperado_linha['nivel'] . ' no documento)';
	}
	if ( (string) $mapa_codigo[ $caminho ]['mae'] !== (string) $esperado_linha['mae'] ) {
		$divergem[] = $caminho . ' (mae "' . $mapa_codigo[ $caminho ]['mae'] . '" no codigo, "' . $esperado_linha['mae'] . '" no documento)';
	}
}
cdm_ok( empty( $divergem ), 'nivel e mae de cada pagina batem entre ARVORE.md e a casca',
	empty( $divergem ) ? count( $doc_arvore ) . ' paginas conferidas' : implode( ' | ', $divergem ) );

/* E o outro sentido: pagina que a ilha PUBLICA e que o mapa nao conhece nao tem
   trilha, e pagina sem trilha e pagina sem lugar na arvore. A home e a unica
   excecao, e ela e nomeada. */
$sem_lugar = array();
foreach ( cdm_casca_definicao_paginas() as $caminho => $def ) {
	if ( 'inicio' === $caminho ) {
		continue;
	}
	/* A CAMADA PRIVADA FICA FORA DA ARVORE, e e a segunda excecao depois da home.
	   Nao e falta de lugar: e nao TER lugar na arvore publica, de propriedade. O
	   painel da artesa nao e um degrau de trilha nem irma de ninguem — se
	   estivesse no mapa, `cdm_casca_irmas()` o ofereceria como "Veja tambem" nas
	   paginas de raiz e a ilha publicaria um link para a area de uma pessoa em
	   toda pagina institucional. */
	if ( isset( $def['camada'] ) && 'privada' === $def['camada'] ) {
		cdm_ok( ! isset( $mapa_codigo[ $caminho ] ), 'a camada privada NAO entra na arvore', $caminho );
		continue;
	}
	if ( ! isset( $mapa_codigo[ $caminho ] ) ) {
		$sem_lugar[] = $caminho;
	}
}
cdm_ok( empty( $sem_lugar ), 'toda pagina publica tem lugar na arvore (so a home e a privada ficam fora)',
	empty( $sem_lugar ) ? count( cdm_casca_definicao_paginas() ) . ' paginas' : implode( ', ', $sem_lugar ) );

/* (a-bis) A LINHA DA PECA — documento x codigo x REALIDADE (28/09/2026).
 *
 * A peca e a unica pagina desta ilha publicada por uma PESSOA, e ate hoje era
 * a unica sem portao nenhum ligando documento a codigo: a tabela da secao 5 e
 * lida por caminho, e o filtro da Loja chaveava a peca pelo slug nu. Os dois
 * lados nao podiam nem ser comparados. Agora podem, e a comparacao tem TRES
 * pernas, porque duas deixariam o portao vazio:
 *
 *   documento -> codigo   a linha da tabela existe no mapa com a peca servida
 *   documento -> realidade  o slug da linha e uma peca que EXISTE (dados/pecas.json,
 *                         que e a copia da secao 24 — nao um nome digitado aqui)
 *   realidade -> codigo   TODA peca da copia pousa em loja/<slug>, nivel 2, mae loja
 *
 * Sem a segunda perna o portao passaria para uma linha inventada, porque a
 * peca de mentira e fabricada com o slug que a tabela pedir. Sem a terceira,
 * a tabela nomearia uma peca e as outras quatro ficariam sem ninguem olhando.
 * O NUMERO de pecas nao esta escrito no documento de proposito: ele sai da
 * copia, que a artesa move e a Fundacao nao. */

function cdm_casca_servir_peca( $slug, $titulo ) {
	$peca = cdm_teste_peca_de_mentira( array() );
	$peca->post_name  = $slug;
	$peca->post_title = $titulo;
	$antes = array(
		'post' => $GLOBALS['__post_atual'] ?? null, 'id' => $GLOBALS['__id_atual'] ?? null,
		'tipo' => $GLOBALS['__tipo_atual'] ?? null, 'cam' => $GLOBALS['__caminho_atual'] ?? null,
		'home' => $GLOBALS['__e_home'] ?? null,
	);
	$GLOBALS['__pecas_por_id'][ (int) $peca->ID ] = $peca;
	$GLOBALS['__post_atual'] = $peca;   $GLOBALS['__id_atual']      = (int) $peca->ID;
	$GLOBALS['__tipo_atual'] = 'peca';  $GLOBALS['__caminho_atual'] = $slug;
	$GLOBALS['__e_home']     = false;

	$retrato = array( 'mapa' => cdm_casca_arvore(), 'pedido' => cdm_casca_slug_atual() );

	$GLOBALS['__post_atual'] = $antes['post']; $GLOBALS['__id_atual']      = $antes['id'];
	$GLOBALS['__tipo_atual'] = $antes['tipo']; $GLOBALS['__caminho_atual'] = $antes['cam'];
	$GLOBALS['__e_home']     = $antes['home'];

	return $retrato;
}

$copia_pecas = json_decode( (string) @file_get_contents( $raiz . '/dados/pecas.json' ), true );
$slugs_no_ar = array();
foreach ( (array) ( $copia_pecas['pecas'] ?? array() ) as $pp ) {
	if ( ! empty( $pp['slug'] ) ) { $slugs_no_ar[ (string) $pp['slug'] ] = (string) ( $pp['titulo'] ?? $pp['slug'] ); }
}
cdm_ok( count( $slugs_no_ar ) >= 1, 'a copia da secao 24 diz quais pecas existem (dados/pecas.json)',
	count( $slugs_no_ar ) . ' pecas na copia' );

cdm_ok( count( $doc_pecas ) >= 1, 'o ARVORE.md declara onde mora a peca',
	count( $doc_pecas ) . ' linha(s) de peca na tabela: ' . implode( ', ', array_keys( $doc_pecas ) ) );

$peca_divergem = array();
foreach ( $doc_pecas as $caminho => $esperado_linha ) {
	$slug = substr( $caminho, strlen( 'loja/' ) );
	if ( ! isset( $slugs_no_ar[ $slug ] ) ) {
		$peca_divergem[] = $caminho . ' (na tabela e NAO na copia da secao 24)';
		continue;
	}
	$r = cdm_casca_servir_peca( $slug, $slugs_no_ar[ $slug ] );
	if ( ! isset( $r['mapa'][ $caminho ] ) ) {
		$peca_divergem[] = $caminho . ' (no documento e nao no codigo, com a peca servida)';
		continue;
	}
	if ( (int) $r['mapa'][ $caminho ]['nivel'] !== (int) $esperado_linha['nivel'] ) {
		$peca_divergem[] = $caminho . ' (nivel ' . $r['mapa'][ $caminho ]['nivel'] . ' no codigo, ' . $esperado_linha['nivel'] . ' no documento)';
	}
	if ( (string) $r['mapa'][ $caminho ]['mae'] !== (string) $esperado_linha['mae'] ) {
		$peca_divergem[] = $caminho . ' (mae "' . $r['mapa'][ $caminho ]['mae'] . '" no codigo, "' . $esperado_linha['mae'] . '" no documento)';
	}
	if ( $caminho !== $r['pedido'] ) {
		$peca_divergem[] = $caminho . ' (o mapa guarda em "' . $caminho . '" e a casca pede por "' . $r['pedido'] . '")';
	}
}
cdm_ok( empty( $peca_divergem ), 'a linha da peca bate entre ARVORE.md, a copia da secao 24 e a casca',
	empty( $peca_divergem ) ? count( $doc_pecas ) . ' linha(s) conferida(s)' : implode( ' | ', $peca_divergem ) );

$pecas_fora = array();
foreach ( $slugs_no_ar as $slug => $titulo ) {
	$r = cdm_casca_servir_peca( $slug, $titulo );
	$c = 'loja/' . $slug;
	if ( ! isset( $r['mapa'][ $c ] ) || 2 !== (int) $r['mapa'][ $c ]['nivel'] || 'loja' !== (string) $r['mapa'][ $c ]['mae'] || $c !== $r['pedido'] ) {
		$pecas_fora[] = $slug . ' (pedido "' . $r['pedido'] . '")';
	}
	if ( isset( $r['mapa'][ $slug ] ) && ! isset( $doc_arvore[ $slug ] ) ) {
		$pecas_fora[] = $slug . ' (chaveada tambem pelo slug nu)';
	}
}
cdm_ok( empty( $pecas_fora ), 'TODA peca da copia pousa em loja/<slug>, nivel 2, mae loja — nao so a da tabela',
	empty( $pecas_fora ) ? count( $slugs_no_ar ) . ' pecas, uma situacao fabricada por peca' : implode( ' | ', $pecas_fora ) );

/* E A DECISAO QUE O FILTRO DECLARA CONTINUA DE PE: fora de uma requisicao de
   peca o mapa NAO tem filha de /loja/. Sem esta afirmacao o conserto poderia
   ter sido "declarar todas as pecas sempre", que encheria a lista de irmas de
   /loja/ de peca — outra decisao, e nao a de hoje. */
$filhas_de_loja = array();
foreach ( cdm_casca_arvore() as $c => $def ) {
	if ( 'loja' === (string) $def['mae'] ) { $filhas_de_loja[] = $c; }
}
cdm_ok( empty( $filhas_de_loja ), 'fora da requisicao da peca, /loja/ nao tem filha no mapa (o mapa e por requisicao)',
	empty( $filhas_de_loja ) ? 'nenhuma' : implode( ', ', $filhas_de_loja ) );

/* A COLISAO, medida aqui tambem porque quem le este portao e quem mexe na
   tabela: peca com slug de pagina da raiz nao rouba a trilha daquela pagina. */
$roubos = array();
foreach ( array( 'sobre', 'contato', 'privacidade' ) as $slug_raiz ) {
	$r = cdm_casca_servir_peca( $slug_raiz, 'Peca de teste ' . $slug_raiz );
	if ( 'loja/' . $slug_raiz !== $r['pedido'] ) { $roubos[] = $slug_raiz . ' -> ' . $r['pedido']; }
}
cdm_ok( empty( $roubos ), 'peca com slug de pagina da raiz nao herda a trilha daquela pagina',
	empty( $roubos ) ? '3 slugs da raiz' : implode( ', ', $roubos ) );

/* (b) OS SLUGS DE NIVEL 2 SAO OS DO VOZ.md. Era exatamente por aqui que a
   divergencia entrava: o registro do Guia dizia 'materiais/colas' e o VOZ.md
   dizia 'colas-e-adesivos', e nada no repositorio cobrava os dois juntos. */
$voz = (string) @file_get_contents( $raiz . '/VOZ.md' );
$voz_n2 = array();
if ( preg_match( '#^- \*\*?Nível 2\*\*?:.*$#mu', $voz, $mv ) || preg_match( '#^- Nível 2:.*$#mu', $voz, $mv ) ) {
	$antes_do_ponto_e_virgula = explode( ';', $mv[0] );
	preg_match_all( '#`([a-z0-9\-]+)`#u', $antes_do_ponto_e_virgula[0], $mt );
	$voz_n2 = $mt[1];
}
cdm_ok( count( $voz_n2 ) >= 6, 'o VOZ.md nomeia as categorias de nivel 2 do Guia',
	implode( ', ', $voz_n2 ) );
$fora_da_voz = array();
foreach ( cdm_casca_categorias_do_guia() as $c ) {
	$ultimo = cdm_casca_slug_final( $c['slug'] );
	if ( ! in_array( $ultimo, $voz_n2, true ) ) {
		$fora_da_voz[] = $c['slug'];
	}
}
cdm_ok( empty( $fora_da_voz ), 'todo slug de categoria do Guia e um nome escrito no VOZ.md',
	empty( $fora_da_voz ) ? count( cdm_casca_categorias_do_guia() ) . ' categorias' : implode( ', ', $fora_da_voz ) );

/* (c) O CAMINHO SE REMONTA SEM ADIVINHAR: nenhum ultimo nivel se repete na
   definicao de paginas. E a premissa de cdm_casca_slug_atual(), e premissa que
   ninguem confere e premissa que um dia deixa de valer. */
$ultimos = array();
foreach ( array_keys( cdm_casca_definicao_paginas() ) as $caminho ) {
	$ultimos[] = cdm_casca_slug_final( $caminho );
}
cdm_ok( count( $ultimos ) === count( array_unique( $ultimos ) ),
	'nenhum ultimo nivel de slug se repete (premissa do caminho remontado)',
	count( array_unique( $ultimos ) ) . ' de ' . count( $ultimos ) . ' distintos' );

/* (d) NENHUMA MAE EM CIRCULO, e nenhuma mae que nao existe no mapa. */
$maes_quebradas = array();
foreach ( $mapa_codigo as $caminho => $def ) {
	if ( '' !== $def['mae'] && ! isset( $mapa_codigo[ $def['mae'] ] ) ) {
		$maes_quebradas[] = $caminho . ' (mae ' . $def['mae'] . ' nao esta no mapa)';
		continue;
	}
	/* Sobe a pe, com a regua deste teste e nao com a da casca. */
	$visitados = array( $caminho => true );
	$passo     = $def['mae'];
	$giros     = 0;
	while ( '' !== $passo ) {
		if ( isset( $visitados[ $passo ] ) ) {
			$maes_quebradas[] = $caminho . ' (circulo em ' . $passo . ')';
			break;
		}
		$visitados[ $passo ] = true;
		$passo = isset( $mapa_codigo[ $passo ] ) ? $mapa_codigo[ $passo ]['mae'] : '';
		if ( ++$giros > 6 ) {
			$maes_quebradas[] = $caminho . ' (mais de 6 niveis acima)';
			break;
		}
	}
	/* 16.1: sem quarto nivel. */
	if ( (int) $def['nivel'] > 3 ) {
		$maes_quebradas[] = $caminho . ' (nivel ' . $def['nivel'] . ', e a 16.1 para no 3)';
	}
}
cdm_ok( empty( $maes_quebradas ), 'nenhuma mae em circulo, ausente, nem quarto nivel',
	empty( $maes_quebradas ) ? count( $mapa_codigo ) . ' entradas no mapa' : implode( ' | ', $maes_quebradas ) );

/* ---------------------------------------------------------------------------
 * 22. A TRILHA NO HTML SERVIDO (16.3)
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * 21b. A ESTRUTURA SE REMONTA QUANDO ENTRA PAGINA NOVA (defeito de 12/09/2026)
 *
 * A casca 1.5.0 criou o filtro `cdm_paginas` para a ferramenta registrar a
 * propria pagina sem ninguem editar a casca, e a guarda de remontagem continuou
 * sendo a VERSAO DA CASCA: pagina nova entrava na definicao, a versao nao
 * mudava, e a pagina nunca nascia no site. A F1 respondeu 404 no ar depois de um
 * Sync que aplicou tudo e disse revisao 10.
 *
 * A afirmacao abaixo mede o MECANISMO, nunca a versao: duas definicoes
 * diferentes tem que produzir chaves diferentes. Um teste que olhasse
 * CDM_CASCA_VERSAO teria ficado verde com o defeito no ar — foi o que aconteceu
 * por um bloco inteiro.
 * ------------------------------------------------------------------------- */

echo "\n21b. A estrutura se remonta quando entra pagina nova (secao 8)\n";

$impressao_hoje = cdm_casca_impressao_da_estrutura();
cdm_ok( '' !== $impressao_hoje, 'a casca publica uma impressao da estrutura', $impressao_hoje );
cdm_ok( false !== strpos( $impressao_hoje, CDM_CASCA_VERSAO ),
	'a impressao carrega a versao da casca (mudar a casca tambem remonta)' );
cdm_ok( $impressao_hoje !== CDM_CASCA_VERSAO,
	'a impressao NAO e so a versao — era exatamente esse o defeito' );

/* A BORDA FABRICADA: uma pagina a mais na definicao tem que mudar a chave. */
$gancho_extra = function ( $paginas ) {
	$paginas['materiais/pagina-que-so-existe-no-teste'] = array(
		'titulo'   => 'Pagina de teste',
		'conteudo' => '[cdm_teste_borda]',
		'pai'      => 'materiais',
	);
	return $paginas;
};
add_filter( 'cdm_paginas', $gancho_extra );
$impressao_com_pagina_nova = cdm_casca_impressao_da_estrutura();
cdm_ok( $impressao_com_pagina_nova !== $impressao_hoje,
	'pagina nova na definicao MUDA a chave de remontagem (a F1 nascia 404 sem isto)' );

/* E o titulo trocado tambem: e o caso do "Inicio" que sobreviveu a duas versoes
   da casca no ar, e o mesmo que a Robometria achou em seis paginas. */
$gancho_titulo = function ( $paginas ) {
	if ( isset( $paginas['sobre'] ) ) {
		$paginas['sobre']['titulo'] = 'Outro nome, so no teste';
	}
	return $paginas;
};
add_filter( 'cdm_paginas', $gancho_titulo );
cdm_ok( cdm_casca_impressao_da_estrutura() !== $impressao_com_pagina_nova,
	'titulo trocado tambem muda a chave (o titulo se sincroniza na remontagem)' );

/* Desfaz os dois ganchos: a bancada nao pode deixar rastro nas afirmacoes
   seguintes, que leem a mesma definicao. */
$GLOBALS['__filtros']['cdm_paginas'] = array_values( array_filter(
	$GLOBALS['__filtros']['cdm_paginas'],
	function ( $f ) use ( $gancho_extra, $gancho_titulo ) {
		return $f !== $gancho_extra && $f !== $gancho_titulo;
	}
) );
cdm_ok( cdm_casca_impressao_da_estrutura() === $impressao_hoje,
	'a bancada devolveu a definicao ao estado de antes' );

echo "\n22. Trilha visivel no corpo (16.3)\n";

/* tag do shortcode -> caminho da pagina, pela definicao da casca. */
$tag_para_caminho = array();
foreach ( cdm_casca_definicao_paginas() as $caminho => $def ) {
	/* O DIGITO FAZIA FALTA: com `[a-z_]+` o shortcode `[cdm_f2]` nao casava, e a
	   pagina da primeira ferramenta da ilha entrava nesta tabela como caminho
	   VAZIO — a trilha dela, o BreadcrumbList dela e o cluster dela passavam a
	   ser medidos contra o nada, e duas das tres afirmacoes reprovavam sem que a
	   pagina tivesse defeito nenhum. Regua estreita demais nao e regua frouxa: e
	   regua que mede outra coisa.

	   E O HIFEN FEZ FALTA DEPOIS, pela TERCEIRA vez na mesma regua (09/10/2026):
	   as oito paginas de consulta de produto tem id com hifen
	   (`cdm_produto_rejunte-para-mosaico`, que e um nome de shortcode legitimo —
	   o WordPress so proibe `& / < > [ ] =` e espaco). Sem o hifen aqui, as oito
	   entravam nesta tabela com caminho VAZIO e 48 afirmacoes reprovavam sem que
	   as paginas tivessem defeito nenhum: a trilha medida contra o mapa do nada,
	   o degrau atual sem rotulo, as irmas comparadas com mae "". O mesmo defeito
	   da nota acima, e a licao dela e justamente esta — regua que mede outra
	   coisa passa por defeito de pagina. */
	if ( preg_match( '#^\[([a-z0-9_-]+)\]$#', (string) $def['conteudo'], $mt ) ) {
		$tag_para_caminho[ $mt[1] ] = $caminho;
	}
}

/* As URLs que EXISTEM na bancada, recontadas aqui — regua propria. */
$urls_no_ar = array( 'https://clubedomosaico.com.br/' => 'inicio' );
foreach ( array_keys( cdm_teste_paginas_no_ar( 'hoje' ) ) as $caminho ) {
	$urls_no_ar[ 'https://clubedomosaico.com.br/' . $caminho . '/' ] = $caminho;
}

$problemas_trilha = array();
foreach ( $paginas as $tag ) {
	$caminho = isset( $tag_para_caminho[ $tag ] ) ? $tag_para_caminho[ $tag ] : '';
	$html    = $html_por_pagina[ $tag ];
	$corpo   = cdm_corpo( $html );
	$quantas = substr_count( $corpo, '<nav class="cdm-trilha"' );

	if ( 'inicio' === $caminho ) {
		cdm_ok( 0 === $quantas, "[$tag] a home NAO tem trilha (16.3)", "achadas: $quantas" );
		cdm_ok( false === strpos( $html, 'id="cdm-trilha-jsonld"' ), "[$tag] a home nao publica BreadcrumbList" );
		continue;
	}

	cdm_ok( 1 === $quantas, "[$tag] exatamente uma trilha no corpo", "achadas: $quantas" );

	$pos_trilha = strpos( $corpo, '<nav class="cdm-trilha"' );
	$pos_h1     = strpos( $corpo, '<h1' );
	cdm_ok( false !== $pos_trilha && false !== $pos_h1 && $pos_trilha < $pos_h1,
		"[$tag] a trilha vem ANTES do H1 (abaixo do cabecalho, 16.3)" );

	preg_match( '#<nav class="cdm-trilha".*?</nav>#s', $corpo, $mtr );
	$trilha = isset( $mtr[0] ) ? $mtr[0] : '';

	/* O ultimo degrau e a pagina atual, marcada, e com o rotulo do mapa. */
	$rotulo = isset( $mapa_codigo[ $caminho ] ) ? $mapa_codigo[ $caminho ]['rotulo'] : '';
	cdm_ok( '' !== $rotulo && false !== strpos( $trilha, '<span aria-current="page">' . htmlspecialchars( $rotulo, ENT_QUOTES ) . '</span>' ),
		"[$tag] o degrau atual e a propria pagina, com aria-current", $rotulo );

	/* O primeiro degrau e sempre a home. */
	cdm_ok( false !== strpos( $trilha, '<a href="https://clubedomosaico.com.br/">Início</a>' ),
		"[$tag] o primeiro degrau linka a home" );

	/* NENHUM degrau aponta para pagina que nao existe. */
	preg_match_all( '#<a href="([^"]+)"#', $trilha, $ml );
	foreach ( $ml[1] as $url ) {
		if ( ! isset( $urls_no_ar[ $url ] ) ) {
			$problemas_trilha[] = $tag . ': degrau para ' . $url . ', que nao existe';
		}
	}

	/* Tantos degraus quanto o mapa manda: home + ancestrais + a propria. */
	$acima = 0;
	$passo = $mapa_codigo[ $caminho ]['mae'];
	while ( '' !== $passo && isset( $mapa_codigo[ $passo ] ) && $acima < 6 ) {
		$acima++;
		$passo = $mapa_codigo[ $passo ]['mae'];
	}
	$degraus_medidos = substr_count( $trilha, '<li>' );
	cdm_ok( $degraus_medidos === $acima + 2, "[$tag] a trilha tem os degraus que o mapa manda",
		$degraus_medidos . ' na tela / ' . ( $acima + 2 ) . ' pelo mapa' );
}
cdm_ok( empty( $problemas_trilha ), 'nenhum degrau de trilha aponta para pagina inexistente',
	empty( $problemas_trilha ) ? 'nenhum' : implode( ' | ', $problemas_trilha ) );

/* ---------------------------------------------------------------------------
 * 23. O BreadcrumbList PUBLICA MENOS DO QUE A TRILHA MOSTRA, de proposito
 *
 * Um ListItem do meio sem `item` invalida a lista inteira para o Google, e lista
 * invalida e lista ignorada. Entao o schema leva so os degraus COM endereco mais
 * a pagina atual — e e essa relacao, e nao "o schema existe", que o teste cobra.
 * ------------------------------------------------------------------------- */

echo "\n23. BreadcrumbList (16.3)\n";
foreach ( $paginas as $tag ) {
	$caminho = isset( $tag_para_caminho[ $tag ] ) ? $tag_para_caminho[ $tag ] : '';
	if ( 'inicio' === $caminho ) {
		continue;
	}
	$html = $html_por_pagina[ $tag ];
	preg_match( '#<script type="application/ld\+json" id="cdm-trilha-jsonld">(.*?)</script>#s', $html, $mj );
	$dados = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;

	$ok_tipo = is_array( $dados ) && isset( $dados['@type'] ) && 'BreadcrumbList' === $dados['@type']
		&& isset( $dados['itemListElement'] ) && is_array( $dados['itemListElement'] );
	cdm_ok( $ok_tipo, "[$tag] BreadcrumbList valido no wp_head" );
	if ( ! $ok_tipo ) {
		continue;
	}
	$itens = $dados['itemListElement'];

	/* TODO item tem endereco — e isso que mantem a lista valida. */
	$sem_item = 0;
	$posicoes = array();
	foreach ( $itens as $i ) {
		if ( empty( $i['item'] ) ) {
			$sem_item++;
		}
		$posicoes[] = (int) $i['position'];
	}
	cdm_ok( 0 === $sem_item, "[$tag] nenhum ListItem sem `item`", "sem item: $sem_item" );
	cdm_ok( $posicoes === range( 1, count( $itens ) ), "[$tag] as posicoes vao de 1 a n sem buraco",
		implode( ',', $posicoes ) );

	/* A RELACAO: os itens sao os degraus LINKADOS da trilha, mais a pagina atual. */
	$corpo = cdm_corpo( $html );
	preg_match( '#<nav class="cdm-trilha".*?</nav>#s', $corpo, $mtr );
	$linkados = preg_match_all( '#<a href="[^"]+"#', isset( $mtr[0] ) ? $mtr[0] : '' );
	cdm_ok( count( $itens ) === $linkados + 1,
		"[$tag] o schema leva os degraus com endereco mais a pagina atual",
		count( $itens ) . ' itens / ' . $linkados . ' degraus linkados + 1' );

	/* O ultimo item e a propria pagina. */
	$ultimo = end( $itens );
	cdm_ok( isset( $ultimo['item'] ) && $ultimo['item'] === 'https://clubedomosaico.com.br/' . $caminho . '/',
		"[$tag] o ultimo item do schema e a propria URL", isset( $ultimo['item'] ) ? $ultimo['item'] : '—' );
}

/* ---------------------------------------------------------------------------
 * 24. O CLUSTER "VEJA TAMBEM" — as duas direcoes, e a borda FABRICADA
 *
 * Com tres secoes, nenhuma pagina chega a ter cinco irmas candidatas: trocar o
 * teto de 4 do 16.4(c) por 5 nao mudaria uma linha do que o site serve, e o
 * portao ficaria verde nas duas versoes. Grade que nao pisa na borda e amostra
 * com nome de grade. Por isso a bancada FABRICA a borda no modo `todas`, que poe
 * as seis categorias do Guia no ar.
 * ------------------------------------------------------------------------- */

echo "\n24. Cluster Veja tambem (16.4c), nas duas direcoes\n";
foreach ( $paginas as $tag ) {
	$caminho = isset( $tag_para_caminho[ $tag ] ) ? $tag_para_caminho[ $tag ] : '';
	$corpo   = cdm_corpo( $html_por_pagina[ $tag ] );
	$tem     = substr_count( $corpo, '<nav class="cdm-veja"' );

	/* Quantas irmas EXISTEM, recontadas aqui a partir do mapa e da lista de
	   paginas no ar — nunca perguntando a cdm_casca_irmas(). */
	$esperadas = 0;
	if ( '' !== $caminho && isset( $mapa_codigo[ $caminho ] ) && 0 !== (int) $mapa_codigo[ $caminho ]['nivel'] ) {
		$no_ar = cdm_teste_paginas_no_ar( 'hoje' );
		foreach ( $mapa_codigo as $outro => $def ) {
			if ( $outro === $caminho || 0 === (int) $def['nivel'] ) {
				continue;
			}
			if ( $def['mae'] === $mapa_codigo[ $caminho ]['mae'] && ! empty( $no_ar[ $outro ] ) ) {
				$esperadas++;
			}
		}
	}
	$deve = $esperadas >= 2 ? 1 : 0;
	cdm_ok( $tem === $deve, "[$tag] bloco Veja tambem so onde ha 2+ irmas no ar",
		"bloco: $tem / irmas no ar: $esperadas" );

	if ( 1 === $tem ) {
		preg_match( '#<nav class="cdm-veja".*?</nav>#s', $corpo, $mv );
		$bloco = isset( $mv[0] ) ? $mv[0] : '';
		$itens = preg_match_all( '#<li><a href="([^"]+)"#', $bloco, $mi );
		cdm_ok( $itens >= 2 && $itens <= 4, "[$tag] de 2 a 4 irmas listadas (16.4c)", "achadas: $itens" );
		$mortos = array();
		foreach ( $mi[1] as $url ) {
			if ( ! isset( $urls_no_ar[ $url ] ) ) {
				$mortos[] = $url;
			}
		}
		cdm_ok( empty( $mortos ), "[$tag] nenhuma irma aponta para pagina inexistente",
			empty( $mortos ) ? 'nenhuma' : implode( ', ', $mortos ) );
		cdm_ok( false === strpos( $bloco, '>' . htmlspecialchars( $mapa_codigo[ $caminho ]['rotulo'], ENT_QUOTES ) . '<' ),
			"[$tag] a pagina nao se lista como irma de si mesma" );

		/* IRMA E QUEM TEM A MESMA MAE, e ate 12/09/2026 isto nao era medido: o
		   portao contava quantas irmas saiam e se elas estavam no ar, nunca de
		   ONDE elas vinham. A mutacao que fazia o cluster aceitar qualquer mae
		   morria por acidente — com poucas paginas no ar ela estourava a
		   contagem —, e no dia em que a ilha ganhou a terceira filha de
		   /materiais/ o acidente sumiu e a mutacao passou. Trava que reprova por
		   efeito colateral e trava que um dia para de reprovar. */
		$de_outra_mae = array();
		foreach ( $mi[1] as $url ) {
			$caminho_irma = trim( str_replace( 'https://clubedomosaico.com.br/', '', $url ), '/' );
			if ( ! isset( $mapa_codigo[ $caminho_irma ] ) ) {
				$de_outra_mae[] = $caminho_irma . ' (fora do mapa)';
				continue;
			}
			if ( $mapa_codigo[ $caminho_irma ]['mae'] !== $mapa_codigo[ $caminho ]['mae'] ) {
				$de_outra_mae[] = $caminho_irma . ' (mae "' . $mapa_codigo[ $caminho_irma ]['mae']
					. '", nao "' . $mapa_codigo[ $caminho ]['mae'] . '")';
			}
		}
		cdm_ok( empty( $de_outra_mae ), "[$tag] toda irma listada tem a MESMA mae (16.4c)",
			empty( $de_outra_mae ) ? $itens . ' irmas' : implode( ' | ', $de_outra_mae ) );
	}
}

/* A BORDA FABRICADA: com as seis categorias no ar, /materiais/como-sabemos/
   passa a ter seis irmas candidatas e o teto de 4 tem o que cortar. */
$corpo_todas = cdm_corpo( cdm_render_em_processo_proprio_modo( $raiz, 'cdm_como_sabemos', 'todas' ) );
preg_match( '#<nav class="cdm-veja".*?</nav>#s', $corpo_todas, $mvt );
$bloco_todas = isset( $mvt[0] ) ? $mvt[0] : '';
$irmas_todas = preg_match_all( '#<li><a href="#', $bloco_todas );
cdm_ok( 6 === count( cdm_casca_categorias_do_guia() ), 'a borda fabricada tem 6 categorias candidatas',
	count( cdm_casca_categorias_do_guia() ) . ' categorias' );
cdm_ok( 4 === $irmas_todas, 'na borda, o teto de 4 do 16.4(c) CORTA (6 candidatas viram 4)',
	'listadas: ' . $irmas_todas );
/* E com a mae publicada, a frase da mae (16.4b) aparece e linka a mae. */
cdm_ok( false !== strpos( $bloco_todas, 'href="https://clubedomosaico.com.br/materiais/"' ),
	'a frase do cluster linka a mae (16.4b)' );

/* ---------------------------------------------------------------------------
 * 25. 16.5 — CARTAO DE CATEGORIA QUE NAO ABRE NAO CARREGA CONTAGEM DE BANCO
 *
 * Medido por ESTRUTURA, nunca por vizinhanca de palavra: o teste extrai os
 * `cdm-tag` do cartao e proibe digito DENTRO deles. Procurar "5" no corpo do
 * Guia acharia o 5 legitimo da camada de prova, que e onde o numero deve estar.
 * ------------------------------------------------------------------------- */

echo "\n25. Cartao de categoria em breve, sem contagem (16.5)\n";
foreach ( array( 'cdm_home', 'cdm_materiais' ) as $tag ) {
	$corpo = cdm_corpo( $html_por_pagina[ $tag ] );
	/* SO OS CARTOES DE CATEGORIA. A 16.5 fala de categoria do Guia, e desde a
	   casca 1.5.0 a mesma pagina tambem serve cartoes de FERRAMENTA, que viram
	   link legitimamente quando a ferramenta existe. Medir os dois juntos fazia
	   a trava acusar o cartao certo. */
	preg_match( '#<ul class="cdm-cards cdm-cards-guia">(.*?)</ul>#s', $corpo, $mg );
	preg_match_all( '#<span class="cdm-acao">(.*?)</span></li>#s', isset( $mg[1] ) ? $mg[1] : '', $ma );
	$com_numero = array();
	$viraram_link = 0;
	foreach ( $ma[1] as $acao ) {
		if ( false !== strpos( $acao, '<a href=' ) ) {
			$viraram_link++;
			continue;
		}
		if ( preg_match( '#<span class="cdm-tag">(.*?)</span>#s', $acao, $mtg ) && preg_match( '#\d#', $mtg[1] ) ) {
			$com_numero[] = trim( $mtg[1] );
		}
	}
	cdm_ok( empty( $com_numero ), "[$tag] nenhum cartao 'em breve' publica contagem de banco",
		empty( $com_numero ) ? count( $ma[1] ) . ' cartoes' : implode( ' | ', $com_numero ) );
	/* QUANTOS CARTOES ABREM E DERIVADO, NAO CRAVADO (02/10/2026, bloco 4c).
	   Ate hoje esta linha dizia `0 === $viraram_link` com o comentario "hoje",
	   e ela estava certa enquanto nenhuma categoria existia. No dia em que a
	   primeira nasceu — `acabamento`, pela 16.5 cumprida — a afirmacao
	   reprovou a casca por SERVIR O CARTAO CERTO. O que a 16.5 manda e que
	   cartao sem pagina nao vire link; entao o esperado e a contagem de
	   categorias que TEM pagina declarada, e ela cresce sozinha. Frase cravada
	   envelhece calada; frase derivada falha so quando ha defeito. */
	$paginas_declaradas = cdm_casca_definicao_paginas();
	$categorias_com_pagina = 0;
	foreach ( cdm_casca_categorias_do_guia() as $c ) {
		if ( ! empty( $c['slug'] ) && isset( $paginas_declaradas[ $c['slug'] ] ) ) {
			$categorias_com_pagina++;
		}
	}
	cdm_ok( $categorias_com_pagina === $viraram_link,
		"[$tag] so abre o cartao da categoria que TEM pagina (16.5)",
		"abrem: $viraram_link, com pagina: $categorias_com_pagina" );
}
/* E o numero NAO sumiu do site: ele continua na camada de prova, contado. */
$corpo_guia = cdm_corpo( $html_por_pagina['cdm_materiais'] );
preg_match( '#<div class="cdm-prova">.*?</div>#s', $corpo_guia, $mp );
$prova = isset( $mp[0] ) ? $mp[0] : '';
cdm_ok( false !== strpos( $prova, '>' . $esperado['materiais_cola'] . '<' )
	&& false !== strpos( $prova, '>' . $esperado['materiais_rejunte'] . '<' ),
	'a contagem por categoria continua publicada na camada de prova, contada do banco',
	$esperado['materiais_cola'] . ' colas / ' . $esperado['materiais_rejunte'] . ' rejuntes' );

/* ---------------------------------------------------------------------------
 * 26. 16.4(f) — NENHUMA PAGINA ORFA
 *
 * Cada URL que a ilha publica precisa de pelo menos DOIS links internos vindos de
 * OUTRAS paginas. Conta-se sobre a pagina inteira de proposito: menu e rodape sao
 * links internos de verdade, e e deles que vive metade das paginas da raiz.
 * ------------------------------------------------------------------------- */

echo "\n26. Nenhuma pagina orfa (16.4f)\n";
$apontam = array();
foreach ( $paginas as $tag ) {
	$origem = isset( $tag_para_caminho[ $tag ] ) ? $tag_para_caminho[ $tag ] : '';
	preg_match_all( '#href="(https://clubedomosaico\.com\.br/[^"]*)"#', $html_por_pagina[ $tag ], $mh );
	foreach ( array_unique( $mh[1] ) as $url ) {
		if ( ! isset( $urls_no_ar[ $url ] ) ) {
			continue;
		}
		$destino = $urls_no_ar[ $url ];
		if ( $destino === $origem ) {
			continue; // link para si mesma nao tira ninguem de orfa
		}
		$apontam[ $destino ] = isset( $apontam[ $destino ] ) ? $apontam[ $destino ] + 1 : 1;
	}
}
/* A regra e sobre URL DO SITEMAP, e a pagina de camada de prova esta fora dele
   por declaracao (16.5 e 14.1). Ela e excluida pela DECLARACAO, nunca pelo nome —
   e a linha seguinte cobra que ela ainda assim seja citada, para "fora do
   sitemap" nao virar porta dos fundos para publicar pagina que ninguem linka. */
$fora_do_sitemap = cdm_casca_paginas_noindex();
/* AS DUAS CAMADAS DE BASTIDOR SE SEPARAM AQUI, e a regra de uma e o contrario da
   regra da outra: a de PROVA tem de ser citada (senao "fora do sitemap" vira
   porta dos fundos para publicar pagina que ninguem linka) e a PRIVADA nao pode
   ser citada por nenhuma (link publico para a area de uma pessoa e convite a todo
   robo que passar). Ler as duas pela mesma lista, como esta afirmacao fazia antes
   do bloco 4d, cobraria do painel da artesa exatamente o que ele nao deve ter. */
$fora_de_prova   = array();
$fora_privadas   = array();
foreach ( $fora_do_sitemap as $caminho ) {
	$camada = isset( $definicoes[ $caminho ]['camada'] ) ? $definicoes[ $caminho ]['camada'] : '';
	if ( 'privada' === $camada ) { $fora_privadas[] = $caminho; } else { $fora_de_prova[] = $caminho; }
}
$orfas = array();
foreach ( array_keys( cdm_teste_paginas_no_ar( 'hoje' ) ) as $caminho ) {
	if ( in_array( $caminho, $fora_do_sitemap, true ) ) {
		continue;
	}
	$n_links = isset( $apontam[ $caminho ] ) ? $apontam[ $caminho ] : 0;
	if ( $n_links < 2 ) {
		$orfas[] = $caminho . ' (' . $n_links . ')';
	}
}
$prova_sem_citacao = array();
foreach ( $fora_de_prova as $caminho ) {
	if ( ( isset( $apontam[ $caminho ] ) ? $apontam[ $caminho ] : 0 ) < 1 ) {
		$prova_sem_citacao[] = $caminho;
	}
}
cdm_ok( empty( $prova_sem_citacao ), 'a pagina de prova fora do sitemap continua citada por outra pagina',
	empty( $prova_sem_citacao ) ? implode( ', ', $fora_de_prova ) : implode( ', ', $prova_sem_citacao ) );

/* E O CONTRARIO, PARA A CAMADA PRIVADA: zero citacao em pagina publica nenhuma.
   O painel e alcancado pelo link que chegou no e-mail dela, e por mais nada. */
$privada_citada = array();
foreach ( $fora_privadas as $caminho ) {
	$n = isset( $apontam[ $caminho ] ) ? $apontam[ $caminho ] : 0;
	if ( $n > 0 ) { $privada_citada[] = $caminho . ' (' . $n . ' links)'; }
}
cdm_ok( empty( $privada_citada ), 'a camada privada NAO e linkada por nenhuma pagina publica',
	empty( $privada_citada ) ? implode( ', ', $fora_privadas ) . ': 0 links' : implode( ', ', $privada_citada ) );

/* E A CITACAO NO CORPO, medida separada — achado de 12/09/2026.
   A afirmacao de cima passou a ser satisfeita SOZINHA pelo cluster: desde que
   /materiais/ ganhou a terceira filha, o bloco "Veja tambem" das duas
   ferramentas lista a camada de prova automaticamente. Isso e bom e nao
   substitui o que a regra queria: uma frase, no meio do texto, mandando quem
   quiser conferir para o bastidor. A mutacao que apagava essa frase parou de
   morder no dia em que o cluster nasceu — a trava nao afrouxou, ela mudou de
   dono, e o que mudou de dono precisa de trava propria. Aqui os links do
   cluster e da trilha saem da conta de proposito: eles sao gerados, e o que se
   mede e a escolha editorial. */
$citada_no_texto = array();
foreach ( $paginas as $tag ) {
	$corpo_sem_gerado = preg_replace( '#<nav class="cdm-veja".*?</nav>#s', '',
		preg_replace( '#<nav class="cdm-trilha".*?</nav>#s', '', cdm_corpo( $html_por_pagina[ $tag ] ) ) );
	foreach ( $fora_de_prova as $caminho ) {
		if ( false !== strpos( $corpo_sem_gerado, 'href="https://clubedomosaico.com.br/' . $caminho . '/"' ) ) {
			$citada_no_texto[ $caminho ] = isset( $citada_no_texto[ $caminho ] ) ? $citada_no_texto[ $caminho ] + 1 : 1;
		}
	}
}
$sem_frase = array();
foreach ( $fora_de_prova as $caminho ) {
	if ( empty( $citada_no_texto[ $caminho ] ) ) {
		$sem_frase[] = $caminho;
	}
}
cdm_ok( empty( $sem_frase ), 'a pagina fora do sitemap e citada no TEXTO, nao so pelo cluster gerado',
	empty( $sem_frase ) ? implode( ', ', array_map( function ( $k, $v ) { return $k . ':' . $v; },
		array_keys( $citada_no_texto ), $citada_no_texto ) ) : implode( ', ', $sem_frase ) );
cdm_ok( empty( $orfas ), 'toda pagina do sitemap recebe 2+ links internos de outras paginas',
	empty( $orfas ) ? implode( ', ', array_map( function ( $k, $v ) { return $k . ':' . $v; }, array_keys( $apontam ), $apontam ) ) : implode( ' | ', $orfas ) );

/* ---------------------------------------------------------------------------
 * 27. AS DUAS BORDAS QUE O MUNDO AINDA NAO TEM
 *
 * Escrita depois de as mutacoes 'degrau de trilha vira link morto' e 'cluster
 * publicado com uma irma so' PASSAREM na primeira rodada. Nenhuma das duas
 * passou por a trava ser fraca: as duas passaram por serem INERTES. Hoje esta
 * ilha nao tem uma unica pagina cujo degrau do meio esteja sem endereco (as tres
 * secoes de nivel 1 existem), nem uma unica pagina com exatamente UMA irma no ar
 * (elas tem zero ou duas). Mutacao que nao muda nada do que o site serve nao
 * mede nada — e teste verde nos dois lados dela e o sintoma.
 *
 * A saida e a mesma do modo `todas` do render: a bancada FABRICA a borda. Aqui
 * ela e fabricada pelo filtro `cdm_arvore`, que e o mesmo por onde uma pagina
 * nova entrara no mapa de verdade, e as duas situacoes fabricadas sao as duas
 * que esta ilha VAI ter: a primeira ficha de material nascendo antes da
 * categoria dela, e uma categoria com uma irma so.
 * ------------------------------------------------------------------------- */

echo "\n27. As bordas fabricadas: degrau sem endereco e irma unica\n";

$GLOBALS['__arvore_fabricada'] = array();
add_filter( 'cdm_arvore', function ( $mapa ) {
	return $GLOBALS['__arvore_fabricada'] ? $GLOBALS['__arvore_fabricada'] : $mapa;
} );

/* BORDA 1 — a ficha nasce antes da categoria dela. E o estado normal das outras
   duas ilhas e sera o desta no dia da primeira ficha: /materiais/ existe,
   /materiais/rejuntes/ ainda nao, e a ficha embaixo dos dois ja existe. */
$GLOBALS['__arvore_fabricada'] = array(
	'materiais'                                       => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Materiais' ),
	'materiais/rejuntes'                              => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Rejuntes' ),
	'materiais/rejuntes/quanto-rejunte-para-um-vaso'  => array( 'nivel' => 3, 'mae' => 'materiais/rejuntes', 'rotulo' => 'Quanto rejunte para um vaso' ),
);
$alvo    = 'materiais/rejuntes/quanto-rejunte-para-um-vaso';
$trilha_b = cdm_casca_trilha_html( $alvo );
$schema_b = cdm_casca_trilha_jsonld( $alvo );

cdm_ok( 4 === substr_count( $trilha_b, '<li>' ), 'borda 1: a trilha na tela mostra os quatro degraus',
	substr_count( $trilha_b, '<li>' ) . ' degraus' );
cdm_ok( 1 === substr_count( $trilha_b, '<span class="cdm-trilha-espera">Rejuntes</span>' ),
	'borda 1: o degrau sem pagina sai em TEXTO, nunca como link' );
preg_match_all( '#<a href="([^"]+)"#', $trilha_b, $mb );
$fora_do_ar = array();
foreach ( $mb[1] as $url ) {
	if ( ! isset( $urls_no_ar[ $url ] ) ) {
		$fora_do_ar[] = $url;
	}
}
cdm_ok( empty( $fora_do_ar ), 'borda 1: nenhum <a> da trilha aponta para pagina que nao existe',
	empty( $fora_do_ar ) ? implode( ', ', $mb[1] ) : implode( ' | ', $fora_do_ar ) );

/* E o schema publica MENOS do que a trilha mostra, de proposito: o degrau sem
   endereco fica de fora, porque ListItem do meio sem `item` invalida a lista
   inteira — e lista invalida e lista ignorada. */
$nomes_schema = array();
$meio_sem_item = 0;
foreach ( $schema_b['itemListElement'] as $i => $item ) {
	$nomes_schema[] = $item['name'];
	if ( $i < count( $schema_b['itemListElement'] ) - 1 && empty( $item['item'] ) ) {
		$meio_sem_item++;
	}
}
cdm_ok( 0 === $meio_sem_item, 'borda 1: nenhum ListItem do MEIO fica sem `item`', "sem item: $meio_sem_item" );
cdm_ok( ! in_array( 'Rejuntes', $nomes_schema, true ),
	'borda 1: o degrau sem endereco NAO entra no BreadcrumbList', implode( ' > ', $nomes_schema ) );
cdm_ok( in_array( 'Materiais', $nomes_schema, true ) && in_array( 'Quanto rejunte para um vaso', $nomes_schema, true ),
	'borda 1: os degraus com endereco e a pagina atual entram', implode( ' > ', $nomes_schema ) );
$posicoes_b = array();
foreach ( $schema_b['itemListElement'] as $item ) {
	$posicoes_b[] = (int) $item['position'];
}
cdm_ok( $posicoes_b === range( 1, count( $posicoes_b ) ),
	'borda 1: pular um degrau nao abre buraco na numeracao', implode( ',', $posicoes_b ) );

/* BORDA 2 — EXATAMENTE UMA IRMA NO AR. Bloco com um item so nao e cluster: o
   16.4(c) pede de 2 a 4, e listar a unica irma seria publicar meio bloco com
   cara de bloco inteiro. */
$GLOBALS['__arvore_fabricada'] = array(
	'loja'      => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Loja' ),
	'materiais' => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Materiais' ),
);
cdm_ok( 1 === count( cdm_casca_irmas( 'loja' ) ), 'borda 2: a situacao fabricada tem exatamente uma irma no ar',
	count( cdm_casca_irmas( 'loja' ) ) . ' irma' );
cdm_ok( '' === cdm_casca_veja_tambem_html( 'loja' ),
	'borda 2: com uma irma so, o bloco Veja tambem NAO sai (16.4c pede 2 a 4)' );

/* E com duas ele sai — o outro lado da mesma borda, para "nao sai nunca" nao
   passar por trava. */
$GLOBALS['__arvore_fabricada'] = array(
	'loja'       => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Loja' ),
	'materiais'  => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Materiais' ),
	'como-fazer' => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Como fazer' ),
);
cdm_ok( '' !== cdm_casca_veja_tambem_html( 'loja' ),
	'borda 2: com duas irmas o bloco sai (o outro lado da borda)' );

$GLOBALS['__arvore_fabricada'] = array();

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

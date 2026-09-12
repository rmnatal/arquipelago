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
);

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
cdm_ok( false !== strpos( $corpo_com_peca, 'R$ 189,90' ), 'com CPT: preco em formato brasileiro', '189.90 -> R$ 189,90' );
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
foreach ( $arquivos_de_banco as $arquivo ) {
	$b = json_decode( file_get_contents( $arquivo ), true );
	$banco_por_categoria[ basename( $arquivo, '.json' ) ] = $b;
	$total_esperando_link += (int) $b['afiliado']['itens_esperando_link'];
	$total_sem_imagem     += (int) $b['imagens']['itens_sem_imagem'];
}
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

/* /atelie/ e o painel da artesa (bloco 4d). Um apelido da casca apontando para
   outro lugar tiraria o painel do ar no dia em que ele nascesse. */
$apelidos = cdm_casca_apelidos();
cdm_ok( ! isset( $apelidos['atelie'] ), 'o endereco /atelie/ NAO e apelido da casca (e o painel da artesa)' );
cdm_ok( ! in_array( 'atelie', $destinos, true ), 'nenhuma pagina da casca ocupa o slug atelie' );

/* O apelido resolve de verdade, e so para o que conhece. */
cdm_ok( 'materiais' === cdm_casca_apelido_para_slug( '/guia/' ), 'apelido com barra resolve para o slug canonico' );
cdm_ok( '' === cdm_casca_apelido_para_slug( 'qualquer-coisa' ), 'caminho desconhecido nao vira redirecionamento' );
cdm_ok( '' === cdm_casca_apelido_para_slug( 'loja/vaso' ), 'caminho com nivel nao e tratado como apelido' );

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
cdm_ok( $recusas_tot > 0 && $recusas_tot <= 4, 'os blocos de recusa sao poucos e contados', $recusas_tot . ' blocos' );

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
	preg_match_all( '#<div class="cdm-prova">#i', $corpo, $mb );
	$quantos_prova = count( $mb[0] );
	if ( $quantos_prova > 2 ) {
		$prova_ruim[] = $tag . ": $quantos_prova blocos de prova (maximo 2)";
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

echo "\n16. Noindex declarado e sitemap como curadoria (secao 14.1)\n";
$ids_falsos = array();
$i_falso    = 100;
foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
	$ids_falsos[ $slug ] = $i_falso++;
}
$GLOBALS['__options']['cdm_casca_paginas'] = $ids_falsos;

$errados = array();
foreach ( $ids_falsos as $slug => $id ) {
	$deve_sair = in_array( $slug, cdm_casca_paginas_noindex(), true );
	$saiu      = ( '' !== cdm_casca_robots_html( $id ) );
	if ( $deve_sair !== $saiu ) {
		$errados[] = $slug;
	}
}
cdm_ok( empty( $errados ), 'a etiqueta noindex sai exatamente nas paginas declaradas',
	empty( $errados ) ? count( $ids_falsos ) . ' paginas' : implode( ', ', $errados ) );
cdm_ok( '' === cdm_casca_robots_html( 0 ), 'sem pagina identificada, nenhuma etiqueta e impressa' );
cdm_ok( '' === cdm_casca_robots_html( 999 ), 'pagina de fora da casca nao recebe noindex' );

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
$menu_da_ilha = array( 'inicio', 'loja', 'materiais', 'como-fazer', 'sobre' );
$fora_indevido = array();
foreach ( cdm_casca_paginas_noindex() as $slug ) {
	$def = $definicoes[ $slug ];
	if ( ! isset( $def['camada'] ) || 'prova' !== $def['camada'] ) {
		$fora_indevido[] = $slug . ' (nao e camada de prova)';
	}
	if ( in_array( $slug, $menu_da_ilha, true ) ) {
		$fora_indevido[] = $slug . ' (esta no menu da ilha)';
	}
}
cdm_ok( empty( $fora_indevido ), 'so a pagina de camada de prova sai do indice',
	empty( $fora_indevido ) ? implode( ', ', cdm_casca_paginas_noindex() ) : implode( ' | ', $fora_indevido ) );
$indexaveis = array_diff( array_keys( $definicoes ), cdm_casca_paginas_noindex() );
cdm_ok( count( $indexaveis ) === count( $definicoes ) - 1,
	'exatamente uma pagina da ilha esta fora do indice',
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
foreach ( array_keys( cdm_casca_definicao_paginas() ) as $caminho ) {
	if ( 'inicio' === $caminho ) {
		continue;
	}
	if ( ! isset( $mapa_codigo[ $caminho ] ) ) {
		$sem_lugar[] = $caminho;
	}
}
cdm_ok( empty( $sem_lugar ), 'toda pagina publicada tem lugar na arvore (so a home fica fora)',
	empty( $sem_lugar ) ? count( cdm_casca_definicao_paginas() ) . ' paginas' : implode( ', ', $sem_lugar ) );

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
	   regua que mede outra coisa. */
	if ( preg_match( '#^\[([a-z0-9_]+)\]$#', (string) $def['conteudo'], $mt ) ) {
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
	cdm_ok( 0 === $viraram_link, "[$tag] nenhum cartao de categoria e link hoje (16.5)", "links: $viraram_link" );
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
foreach ( $fora_do_sitemap as $caminho ) {
	if ( ( isset( $apontam[ $caminho ] ) ? $apontam[ $caminho ] : 0 ) < 1 ) {
		$prova_sem_citacao[] = $caminho;
	}
}
cdm_ok( empty( $prova_sem_citacao ), 'a pagina fora do sitemap continua citada por outra pagina',
	empty( $prova_sem_citacao ) ? implode( ', ', $fora_do_sitemap ) : implode( ', ', $prova_sem_citacao ) );

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
	foreach ( $fora_do_sitemap as $caminho ) {
		if ( false !== strpos( $corpo_sem_gerado, 'href="https://clubedomosaico.com.br/' . $caminho . '/"' ) ) {
			$citada_no_texto[ $caminho ] = isset( $citada_no_texto[ $caminho ] ) ? $citada_no_texto[ $caminho ] + 1 : 1;
		}
	}
}
$sem_frase = array();
foreach ( $fora_do_sitemap as $caminho ) {
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

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
);

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );

$paginas = array(
	'cdm_home', 'cdm_loja', 'cdm_materiais', 'cdm_como_sabemos', 'cdm_como_fazer',
	'cdm_sobre', 'cdm_contato', 'cdm_afiliados', 'cdm_privacidade',
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
function cdm_render_em_processo_proprio( $raiz, $tag ) {
	$saida = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $tag ) . ' 2>/dev/null', $saida, $codigo );
	return 0 === $codigo ? implode( "\n", $saida ) : '';
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
 * 7. A MARCA E O ARQUIVO ENTREGUE, e nao um desenho feito aqui.
 *
 * E a regra propria desta ilha: o PROMPT.md proibe reconstruir, redesenhar ou
 * vetorizar o logo, e proibe escrever "clube do mosaico" em texto ao lado dele,
 * porque o arquivo ja traz o wordmark. As duas primeiras ilhas desenham o
 * simbolo em SVG; aqui isso seria defeito.
 * ------------------------------------------------------------------------- */

echo "\n7. Marca entregue, paleta e rodape\n";
preg_match( '#<a class="cdm-marca".*?</a>#is', $home, $mm );
$marca = isset( $mm[0] ) ? $mm[0] : '';
cdm_ok( '' !== $marca, 'a marca sai no HTML servido' );
cdm_ok( false === stripos( $marca, '<svg' ), 'nenhum logo desenhado em SVG (o PROMPT.md proibe redesenhar)' );
/* O ARQUIVO DE FUNDO PRETO NAO ENTRA NO CABECALHO CLARO. Ele continua sendo o
   logotipo da entidade no JSON-LD, onde quem le e o Google; aqui, sobre branco,
   ele e um retangulo escuro — foi a metade visivel da reprovacao do Raphael. */
cdm_ok( false === strpos( $marca, CDM_CASCA_LOGO_URL ),
	'o logo de fundo preto NAO e servido no cabecalho claro' );
/* O nome e legivel sem imagem nenhuma: e texto, nao alt de figura. */
$marca_so_texto = trim( html_entity_decode( strip_tags( $marca ), ENT_QUOTES, 'UTF-8' ) );
cdm_ok( 'clube do mosaico' === mb_strtolower( $marca_so_texto, 'UTF-8' ),
	'o wordmark e TEXTO no cabecalho, e so ele', '"' . $marca_so_texto . '"' );
/* A lotus so sai quando existe arquivo valido embutido: sem isso, um <img> com
   src vazio seria icone quebrado no lugar do logo sumido — trocar um defeito
   visivel por outro. Os dois lados sao medidos. */
$tem_lotus = ( defined( 'CDM_CASCA_MARCA_LOTUS' ) && '' !== CDM_CASCA_MARCA_LOTUS );
cdm_ok( $tem_lotus === ( false !== strpos( $marca, 'cdm-marca-lotus' ) ),
	'a lotus aparece no cabecalho se, e so se, ha arquivo embutido',
	$tem_lotus ? 'embutida' : 'ausente (lotus-512.png truncado no repositorio)' );
if ( $tem_lotus ) {
	cdm_ok( false !== strpos( $marca, 'alt=""' ),
		'a lotus e decoracao ao lado do nome escrito (alt vazio, sem marca em dobro)' );
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

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

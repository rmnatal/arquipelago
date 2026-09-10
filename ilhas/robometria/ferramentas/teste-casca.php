<?php
/**
 * Verificacao MEDIDA da casca da Robometria, sem site e sem rede.
 *
 *   php ferramentas/teste-casca.php .
 *
 * E a secao 8 do ARQUIPELAGO.md executada onde da para executa-la nesta ilha: a
 * nuvem nao alcanca robometria.com.br, entao a alternativa a este arquivo seria
 * marcar publicar=true por fe. Cada afirmacao abaixo e um numero, nunca uma
 * impressao — e o teste sai com codigo 1 quando qualquer uma falha.
 *
 * O que ele NAO substitui: a conferencia da revisao aplicada no /status depois do
 * Sync (secao 4), que so a Sentinela faz, no navegador do Raphael. Este arquivo
 * prova que o codigo esta certo; so o /status prova que ele esta NO AR.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function rbm_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-62s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-62s %s\n", $rotulo, $medida );
	return false;
}

/** Só os blocos <script>, que é onde a contagem de &#038; vale (seção 8). */
function rbm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

$GLOBALS['__paginas'] = array(
	'ferramentas'             => true,
	'metodologia'             => true,
	'sobre'                   => true,
	'divulgacao-de-afiliados' => true,
);

robometria_teste_carregar( $raiz );

$paginas = array( 'robometria_home', 'robometria_ferramentas', 'robometria_metodologia', 'robometria_sobre', 'robometria_afiliados' );

echo "Robometria — verificacao da casca " . ROBOMETRIA_CASCA_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria: script dentro do
 *    retorno do shortcode. Aqui ele e medido em cada pagina.
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";
$html_por_pagina = array();
foreach ( $paginas as $tag ) {
	robometria_teste_rebobinar();
	$html_por_pagina[ $tag ] = robometria_teste_pagina( $tag );
	$cru = $GLOBALS['__retorno_shortcode'];
	rbm_ok( false === stripos( $cru, '<script' ), "[$tag] sem <script> no retorno do shortcode" );
	rbm_ok( false === stripos( $cru, '<style' ), "[$tag] sem <style> no retorno do shortcode" );
}

/* ---------------------------------------------------------------------------
 * 2. Zero &#038; DENTRO de <script>. Contar na pagina inteira e teste ERRADO.
 * ------------------------------------------------------------------------- */

echo "\n2. Entidades dentro de <script> (secao 8, item 2)\n";
foreach ( $paginas as $tag ) {
	$scripts = rbm_scripts( $html_por_pagina[ $tag ] );
	$n = substr_count( $scripts, '&#038;' );
	rbm_ok( 0 === $n, "[$tag] zero &#038; dentro de <script>", "achados: $n" );
}

/* ---------------------------------------------------------------------------
 * 3. Menu: links no HTML servido, botao acessivel, aria-controls que aponta para
 *    um id que existe (secao 6).
 * ------------------------------------------------------------------------- */

echo "\n3. Menu hamburguer (secao 6)\n";
$home = $html_por_pagina['robometria_home'];
preg_match( '#<button[^>]*class="rbm-nav-botao"[^>]*>#i', $home, $mb );
$botao = isset( $mb[0] ) ? $mb[0] : '';
rbm_ok( '' !== $botao, 'botao do menu e <button> de verdade' );
rbm_ok( false !== strpos( $botao, 'aria-expanded="false"' ), 'botao nasce com aria-expanded="false"' );
preg_match( '#aria-controls="([^"]+)"#', $botao, $mc );
$controlado = isset( $mc[1] ) ? $mc[1] : '';
rbm_ok( '' !== $controlado, 'botao declara aria-controls', $controlado );
rbm_ok( '' !== $controlado && false !== strpos( $home, 'id="' . $controlado . '"' ), 'o id de aria-controls existe no HTML servido' );
preg_match( '#<nav class="rbm-nav"[^>]*>(.*?)</nav>#is', $home, $mn );
$nav = isset( $mn[1] ) ? $mn[1] : '';
$links = preg_match_all( '#<a href="https://robometria\.com\.br/[^"]+"#', $nav );
rbm_ok( 3 === $links, 'os 3 links do menu sao <a href> reais dentro de <nav>', "achados: $links" );
rbm_ok( false !== strpos( $home, 'aria-label="Navegação principal"' ), '<nav> tem rotulo acessivel' );

/* ---------------------------------------------------------------------------
 * 4. Favicon proprio no lugar do icone do WordPress (secao 6).
 * ------------------------------------------------------------------------- */

echo "\n4. Favicon proprio (secao 6)\n";
rbm_ok( false === strpos( $home, 'icone-do-wordpress.png' ), 'o icone padrao do WordPress FOI removido do wp_head' );
rbm_ok( false !== strpos( $home, 'rel="icon" type="image/svg+xml"' ), 'icone SVG proprio no wp_head' );
rbm_ok( false !== strpos( $home, 'rel="apple-touch-icon"' ), 'apple-touch-icon em PNG' );
rbm_ok( false !== strpos( $home, '<meta name="theme-color" content="#16191D">' ), 'theme-color na cor tinta da ilha' );
rbm_ok( '' !== ROBOMETRIA_CASCA_ICONE_SVG, 'o bloco do favicon foi gerado (nao esta vazio)', strlen( ROBOMETRIA_CASCA_ICONE_SVG ) . ' bytes' );

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
	rbm_ok(
		is_array( $dados ) && in_array( 'Organization', $tipos, true ) && in_array( 'WebSite', $tipos, true ),
		"[$tag] JSON-LD decodifica e traz Organization + WebSite",
		implode( '+', $tipos )
	);
}
/* sameAs so entra quando houver perfil externo de verdade; perfil inventado seria
   exatamente a fabricacao que esta ilha existe para nao cometer. */
rbm_ok( false === strpos( $home, '"sameAs"' ), 'nenhum sameAs inventado no Organization' );

/* ---------------------------------------------------------------------------
 * 6. Corpo comeca pelo texto, nunca por metadado (secao 8, item 3).
 * ------------------------------------------------------------------------- */

echo "\n6. Corpo da pagina (secao 8, item 3)\n";
foreach ( $paginas as $tag ) {
	preg_match( '#<main[^>]*>(.*?)</main>#is', $html_por_pagina[ $tag ], $mm );
	$corpo = isset( $mm[1] ) ? trim( $mm[1] ) : '';
	rbm_ok( 0 !== strpos( $corpo, '---' ) && 0 !== strpos( $corpo, 'ilha:' ), "[$tag] corpo nao comeca por metadado YAML" );
}

/* ---------------------------------------------------------------------------
 * 7. Marca e rodape (secao 6 e identidade da ilha).
 * ------------------------------------------------------------------------- */

echo "\n7. Marca, paleta e rodape\n";
rbm_ok( false !== strpos( $home, '<b>ROBO</b><i>METRIA</i>' ), 'wordmark com ROBO em 700 e METRIA em 400, coladas' );
rbm_ok( false !== strpos( $home, 'aria-label="Robometria"' ), 'logotipo em SVG com rotulo acessivel' );
rbm_ok( false === stripos( $home, '<img' ) || false === stripos( $home, 'wp-content/uploads' ), 'nenhuma imagem subida para a biblioteca de midia' );
rbm_ok( 1 === substr_count( $home, 'class="rbm-rodape"' ), 'exatamente um rodape na pagina', substr_count( $home, 'class="rbm-rodape"' ) . ' achado(s)' );

/* A varredura e COR DE SINAL: um uso por tela. Na casca esse uso e a peca do
   logotipo. Se ela aparecer no corpo servido, a regra da identidade quebrou. */
$corpo_home = '';
if ( preg_match( '#<main[^>]*>(.*?)</main>#is', $home, $mm ) ) { $corpo_home = $mm[1]; }
rbm_ok( 0 === substr_count( strtoupper( $corpo_home ), '#CC3311' ), 'varredura nao aparece no corpo (cor de sinal, um uso por tela)' );

/* Gradiente e sombra colorida sao proibidos no Arquipelago (secao 6). A unica
   sombra permitida e a neutra do menu do celular, que e cinza da propria tinta. */
preg_match( '#<style id="robometria-casca">(.*?)</style>#is', $home, $ms );
$css = isset( $ms[1] ) ? $ms[1] : '';
rbm_ok( '' !== $css, 'CSS da casca servido no wp_head' );
rbm_ok( false === stripos( $css, 'gradient' ), 'nenhum gradiente no CSS' );

/* Toda cor do CSS tem que estar na paleta declarada no PROMPT.md da ilha. */
$paleta = array( '#16191D', '#CC3311', '#F2F1EF', '#FFFFFF', '#DFDCD6', '#6B6862', '#A26A00' );
preg_match_all( '/#[0-9A-Fa-f]{6}\b/', $css, $mh );
$fora = array_values( array_unique( array_diff( array_map( 'strtoupper', $mh[0] ), $paleta ) ) );
rbm_ok( empty( $fora ), 'nenhuma cor fora da paleta da ilha no CSS', empty( $fora ) ? count( $mh[0] ) . ' usos' : implode( ' ', $fora ) );

/* ---------------------------------------------------------------------------
 * 8. Os numeros da tela batem com o banco commitado.
 *
 * E o teste que impede o instantaneo de robometria_casca_numeros() envelhecer em
 * silencio: quem expandir o banco e nao atualizar a casca ve o teste reprovar,
 * em vez de o site publicar um numero que o repositorio nao sustenta.
 * ------------------------------------------------------------------------- */

echo "\n8. Numeros da tela x banco commitado (secao 10: nunca invente dado)\n";
$modelos = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$pecas   = json_decode( file_get_contents( $raiz . '/dados/pecas.json' ), true );
$marcas  = json_decode( file_get_contents( $raiz . '/dados/marcas.json' ), true );
$cob     = json_decode( file_get_contents( $raiz . '/dados/cobertura-r1.json' ), true );
$n       = robometria_casca_numeros();

$esperado = array(
	'marcas'               => count( $marcas['registros'] ),
	'modelos_publicaveis'  => (int) $modelos['contagem']['publicavel'],
	'pecas_publicaveis'    => (int) $pecas['contagem']['publicavel'],
	'pares_declarados'     => (int) $pecas['contagem']['pares_peca_x_modelo_declarados'],
	'esperando_link'       => (int) $modelos['contagem']['esperando_link_de_afiliado'] + (int) $pecas['contagem']['esperando_link_de_afiliado'],
	'r1_responde'          => (int) $cob['resumo']['modelos_que_respondem'],
	'r1_vazia'             => (int) $cob['resumo']['modelos_com_entrada_vazia'],
	'celulas'              => (int) $cob['resumo']['celulas_total'],
	'celulas_sem_resposta' => (int) $cob['resumo']['celulas']['vazia'],
	'as_duas'              => count( $cob['cruzamento_com_a_r2']['as_duas_respondem'] ),
);

foreach ( $esperado as $chave => $valor ) {
	rbm_ok( (int) $n[ $chave ] === $valor, "numero '$chave' bate com o banco", 'tela ' . $n[ $chave ] . ' / banco ' . $valor );
}

/* ---------------------------------------------------------------------------
 * 9. Higiene de snippet (secao 8 e fase 4b do playbook).
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * 8b. O sitemap nao pode responder 404 (despacho da Sentinela de 10/09/2026).
 *
 * Esta ilha nao tem nenhum post publicado — a casca manda "Hello world!" para a
 * lixeira —, entao a consulta principal das rotas de sitemap volta vazia e o
 * handle_404() do nucleo carimba 404 antes de o XML sair. O filtro
 * pre_handle_404 desliga esse carimbo SO na requisicao de sitemap. O teste
 * exercita o retorno do filtro, que e a decisao inteira, e confirma que ele nao
 * transborda para requisicao comum: um filtro que dissesse "nunca 404" faria a
 * ilha responder 200 em endereco que nao existe, e ai o Google indexaria vazio.
 * ------------------------------------------------------------------------- */

echo "\n8b. Sitemap nao responde 404 (despacho da Sentinela, 10/09/2026)\n";

class RbmConsultaFalsa {
	private $vars;
	public function __construct( $vars ) { $this->vars = $vars; }
	public function get( $chave ) { return isset( $this->vars[ $chave ] ) ? $this->vars[ $chave ] : ''; }
}

$de_sitemap  = new RbmConsultaFalsa( array( 'sitemap' => 'index' ) );
$de_pagina   = new RbmConsultaFalsa( array( 'sitemap' => 'posts', 'sitemap-subtype' => 'page', 'paged' => 1 ) );
$requisicao  = new RbmConsultaFalsa( array( 'pagename' => 'metodologia' ) );
$inexistente = new RbmConsultaFalsa( array( 'name' => 'pagina-que-nao-existe' ) );

rbm_ok( true === apply_filters( 'pre_handle_404', false, $de_sitemap ),
	'o indice do sitemap deixa de ser 404' );
rbm_ok( true === apply_filters( 'pre_handle_404', false, $de_pagina ),
	'o sitemap de paginas deixa de ser 404' );
rbm_ok( false === apply_filters( 'pre_handle_404', false, $requisicao ),
	'pagina comum NAO e afetada pelo filtro' );
rbm_ok( false === apply_filters( 'pre_handle_404', false, $inexistente ),
	'endereco inexistente continua podendo 404 — 200 no vazio seria pior' );
rbm_ok( false === apply_filters( 'pre_handle_404', false, null ),
	'filtro sobrevive a consulta ausente sem explodir' );

echo "\n9. Higiene do snippet (secao 8, fase 4b)\n";
$fonte = file_get_contents( $raiz . '/snippets/robometria-casca.php' );
rbm_ok( 0 === strpos( $fonte, '/**' ), 'o snippet comeca com /** e sem <?php no topo' );
rbm_ok( false === strpos( $fonte, '$_SERVER' ), 'nenhuma superglobal de servidor (o ModSecurity mata a gravacao em silencio)' );

preg_match_all( '/^function\s+([a-z0-9_]+)\s*\(/mi', $fonte, $mf );
$desprotegidas = array();
foreach ( $mf[1] as $nome ) {
	if ( false === strpos( $fonte, "function_exists( '" . $nome . "' )" ) ) {
		$desprotegidas[] = $nome;
	}
}
rbm_ok( empty( $desprotegidas ), 'toda funcao de nivel superior dentro de function_exists', empty( $desprotegidas ) ? count( $mf[1] ) . ' funcoes' : implode( ' ', $desprotegidas ) );

/* Apelido tem que apontar para pagina que a casca cria ou para ferramenta do
   catalogo: apelido apontando para slug inexistente e 404 trocado por 404. */
$destinos = array_keys( robometria_casca_definicao_paginas() );
foreach ( robometria_casca_ferramentas() as $f ) { $destinos[] = $f['slug']; }
$orfaos = array();
foreach ( robometria_casca_apelidos() as $apelido => $destino ) {
	if ( ! in_array( $destino, $destinos, true ) ) { $orfaos[] = $apelido . '→' . $destino; }
	if ( in_array( $apelido, $destinos, true ) ) { $orfaos[] = $apelido . ' (apelido igual a slug real)'; }
}
rbm_ok( empty( $orfaos ), 'todo apelido aponta para pagina ou ferramenta conhecida', empty( $orfaos ) ? count( robometria_casca_apelidos() ) . ' apelidos' : implode( ', ', $orfaos ) );

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

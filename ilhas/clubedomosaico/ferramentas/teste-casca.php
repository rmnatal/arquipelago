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
	'cdm_home', 'cdm_loja', 'cdm_materiais', 'cdm_como_fazer',
	'cdm_sobre', 'cdm_contato', 'cdm_afiliados', 'cdm_privacidade',
);

echo "Clube do Mosaico — verificacao da casca " . CDM_CASCA_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria: script dentro do
 *    retorno do shortcode. Aqui ele e medido em cada pagina.
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";
$html_por_pagina = array();
foreach ( $paginas as $tag ) {
	cdm_teste_rebobinar();
	$html_por_pagina[ $tag ] = cdm_teste_pagina( $tag );
	$cru = $GLOBALS['__retorno_shortcode'];
	cdm_ok( false === stripos( $cru, '<script' ), "[$tag] sem <script> no retorno do shortcode" );
	cdm_ok( false === stripos( $cru, '<style' ), "[$tag] sem <style> no retorno do shortcode" );
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
cdm_ok( false !== strpos( $home, '<meta name="theme-color" content="#000000">' ), 'theme-color no preto do cabecalho' );

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
cdm_ok( false !== strpos( $marca, CDM_CASCA_LOGO_URL ), 'a marca usa o arquivo oficial da biblioteca de midia' );
cdm_ok( false !== strpos( $marca, 'alt="Clube do Mosaico"' ), 'o logo tem alt com o nome (quem nao ve a imagem le o nome)' );
cdm_ok( false === stripos( $marca, '<svg' ), 'nenhum logo desenhado em SVG (o PROMPT.md proibe redesenhar)' );
/* O wordmark nao se repete em texto: fora do atributo alt, o nome nao aparece
   dentro do bloco da marca. */
$marca_sem_alt = preg_replace( '#alt="[^"]*"#', '', $marca );
cdm_ok( false === stripos( $marca_sem_alt, 'clube do mosaico' ),
	'o nome nao e escrito em texto ao lado do logo (o arquivo ja tem o wordmark)' );
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
/* Cabecalho e rodape pretos, miolo branco: a regra visual desta ilha. */
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
cdm_ok( false !== strpos( $corpo_home_vazio, 'A vitrine ainda não abriu' ), 'sem CPT: a home diz que a vitrine nao abriu' );

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
cdm_ok( false === strpos( $home_com_peca, 'A vitrine ainda não abriu' ), 'com CPT: a home deixa de dizer que a vitrine nao abriu' );

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
	'esperando_link'     => (int) $colas['afiliado']['itens_esperando_link'],
	'sem_imagem'         => (int) $colas['imagens']['itens_sem_imagem'],
	'celulas_matriz'     => count( $celulas ),
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

/* Os numeros tem que APARECER na tela, e no corpo — nao basta a funcao devolver
   certo. Medido dentro de <main> (secao 8, regra 3). */
$corpo_materiais = cdm_corpo( $html_por_pagina['cdm_materiais'] );
cdm_ok( false !== strpos( $corpo_materiais, '>' . $esperado['celulas_matriz'] . '<' ),
	'a pagina de materiais publica o total de combinacoes mapeadas' );
cdm_ok( false !== strpos( $corpo_materiais, '>' . $esperado['celulas_sem_saida'] . '<' ),
	'a pagina de materiais publica quantas combinacoes ficam SEM resposta' );

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

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

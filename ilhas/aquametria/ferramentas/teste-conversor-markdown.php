<?php
/**
 * Roda o conversor de Markdown do proprio snippet "Aquametria Sync" sobre TODOS os
 * arquivos de conteudo/ e procura residuo de metadado no HTML.
 *
 * Existe por causa de um defeito real: em 08/09/2026 a pagina da C1 estava no ar com
 * o front matter YAML impresso no corpo ("--- id: calculadora-de-litragem tipo: pagina
 * ..."), com os tres hifens virando travessao pelo wptexturize. O repositorio ja estava
 * certo; o site e que rodava uma versao velha do Sync. Este teste garante que o lado do
 * repositorio nunca volte a errar isso em silencio.
 *
 *   php ferramentas/teste-conversor-markdown.php .
 */
define( 'ABSPATH', '/tmp/wp/' );
function add_filter( $h, $f, $p = 10, $a = 1 ) {}
function add_action( $h, $f, $p = 10, $a = 1 ) {}
function esc_html( $t ) { return htmlspecialchars( $t, ENT_QUOTES ); }
function register_rest_route() {}

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
eval( file_get_contents( $raiz . '/snippets/aquametria-sync.php' ) );

$falhas = 0;
$casos  = 0;

/* --- 1. os arquivos reais de conteudo/ --- */
foreach ( glob( $raiz . '/conteudo/*.md' ) as $arquivo ) {
	$nome = basename( $arquivo );
	if ( 'README.md' === $nome ) {
		continue; // documentacao da pasta, nao vai para o site
	}
	$md   = file_get_contents( $arquivo );
	$html = aquametria_sync_md( $md );
	$casos++;

	/* Chaves de front matter que nao podem aparecer em lugar nenhum do HTML. */
	foreach ( array( 'meta_descricao:', 'verificado_em:', 'publicar:', 'slug:', 'cluster:', 'tipo: pagina', 'tipo: artigo' ) as $chave ) {
		if ( false !== strpos( $html, $chave ) ) {
			echo "FALHA $nome: residuo de front matter no HTML — '$chave'\n";
			$falhas++;
		}
	}
	/* O HTML nao pode comecar por uma linha de tres hifens (o wptexturize a transforma
	   em travessao e o leitor ve um travessao solto antes do texto). */
	if ( preg_match( '/\A\s*(<hr\s*\/?>|---)/', $html ) ) {
		echo "FALHA $nome: HTML comeca por separador/hifens\n";
		$falhas++;
	}
	/* O primeiro bloco tem de ser texto de verdade: paragrafo, titulo ou shortcode. */
	if ( ! preg_match( '/\A\s*(<p>|<h[1-6]>|<ul>|<ol>|\[[a-z0-9_]+)/i', $html ) ) {
		echo "FALHA $nome: primeiro bloco do HTML nao e texto (" . substr( trim( $html ), 0, 60 ) . ")\n";
		$falhas++;
	}
	/* O titulo do front matter aparece no <title> do WordPress, nunca no corpo. */
	if ( preg_match( '/^titulo:\s*"?(.+?)"?\s*$/m', $md, $m ) ) {
		if ( false !== strpos( $html, 'titulo: ' ) ) {
			echo "FALHA $nome: a linha 'titulo:' do front matter saiu no corpo\n";
			$falhas++;
		}
	}
	echo sprintf( "ok  %-46s %6d bytes de HTML\n", $nome, strlen( $html ) );
}

/* --- 2. variantes de front matter que a regex tem de tolerar --- */
$corpo    = "Primeiro paragrafo de verdade.\n";
$variacoes = array(
	'unix'              => "---\nid: x\npublicar: true\n---\n" . $corpo,
	'crlf'              => "---\r\nid: x\r\npublicar: true\r\n---\r\n" . $corpo,
	'cr-antigo'         => "---\rid: x\rpublicar: true\r---\r" . $corpo,
	'espaco-a-direita'  => "---  \nid: x\npublicar: true\n---\t\n" . $corpo,
	'bom'               => "\xEF\xBB\xBF---\nid: x\npublicar: true\n---\n" . $corpo,
	'sem-linha-final'   => "---\nid: x\npublicar: true\n---",
	'sem-front-matter'  => $corpo,
	'hr-legitimo-depois' => $corpo . "\n---\n\nSegundo paragrafo.\n",
);
foreach ( $variacoes as $rotulo => $texto ) {
	$casos++;
	$html = aquametria_sync_md( $texto );
	$sujo = ( false !== strpos( $html, 'publicar:' ) ) || ( false !== strpos( $html, 'id: x' ) );
	if ( 'sem-front-matter' === $rotulo || 'hr-legitimo-depois' === $rotulo ) {
		$sujo = false !== strpos( $html, 'publicar:' );
	}
	if ( $sujo ) {
		echo "FALHA variante '$rotulo': front matter sobrou → " . substr( $html, 0, 80 ) . "\n";
		$falhas++;
	} else {
		echo "ok  variante $rotulo\n";
	}
	if ( 'sem-front-matter' !== $rotulo && 'sem-linha-final' !== $rotulo
		&& false === strpos( $html, 'Primeiro paragrafo de verdade' ) ) {
		echo "FALHA variante '$rotulo': o conversor comeu o texto de verdade\n";
		$falhas++;
	}
}

echo "\n$casos caso(s), $falhas falha(s)\n";
exit( $falhas > 0 ? 1 : 0 );

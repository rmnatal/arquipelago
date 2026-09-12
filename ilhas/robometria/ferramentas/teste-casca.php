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

/* AS PAGINAS QUE EXISTEM NO SITE DE TESTE.
 *
 * As quatro de ferramenta e artigo entraram aqui na casca 1.2.0: o menu passou a
 * apontar direto para as duas ferramentas, e link do menu para pagina que a
 * bancada nao conhece sairia como <span> — o teste do menu mediria tres spans e
 * chamaria de aprovado o cabecalho que no ar tem tres links. */
$GLOBALS['__paginas'] = array(
	'ferramentas'                                 => true,
	'metodologia'                                 => true,
	'sobre'                                       => true,
	'divulgacao-de-afiliados'                     => true,
	'qual-peca-serve-no-meu-robo-aspirador'       => true,
	'quantos-pa-o-robo-aspirador-precisa'         => true,
	'filtro-universal-de-robo-aspirador'          => true,
	'quantos-m2-o-robo-aspirador-limpa-por-carga' => true,
);

/* O BANCO, COMO O SYNC O ENTREGA AO SITE.
 *
 * Entrou junto com a casca 1.2.0, e nao e detalhe: a home passou a servir o
 * formulario da R1, e sem as options ela serve o aviso de "seletor fora do ar",
 * que e uma pagina VALIDA. Seria a terceira vez que esta ilha mede uma pagina
 * pela metade sem ver (secao 8 do ARQUIPELAGO.md). */
robometria_teste_carregar_options( $raiz );

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
	$html_por_pagina[ $tag ] = robometria_teste_pagina( $tag, 'Robometria — teste', robometria_teste_slug_do_alvo( $tag ) );
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

/* A REGUA E ESCRITA AQUI, NOS REGISTROS — nunca lida do cabecalho `contagem`.
 *
 * Ate 11/09/2026 este bloco comparava o numero da tela com `contagem.publicavel`
 * e irmaos, que sao campos escritos no proprio arquivo de banco e conferidos por
 * validar-banco.py. Quer dizer: as duas metades da comparacao vinham da mesma
 * regua, e trocar a regra faria as duas errarem juntas — a familia de defeito que
 * a secao 8 do contrato descreve. Agora o teste conta nos registros.
 *
 * E AI APARECEU UM NUMERO QUE NINGUEM PROCURAVA: o par peca x modelo. O
 * cabecalho conta 33 (toda compatibilidade declarada por peca publicavel) e a
 * tela passou a dizer 32, porque o par que sobra aponta para `multi-ho401`, que
 * e `nao_publicavel` — a R1 nunca o oferece, entao ele nao cobre nada. Numa
 * tabela chamada "o que medimos sobre a nossa propria cobertura", o numero certo
 * e o que a ilha CONSEGUE servir. Os dois numeros continuam existindo e medem
 * coisas diferentes: o do arquivo conta o que o banco guarda, o da tela conta o
 * que o site responde. */
$pub_modelos = array();
foreach ( $modelos['registros'] as $r ) {
	if ( 'publicavel' === $r['status'] ) { $pub_modelos[ $r['id'] ] = $r; }
}
$pub_pecas = array();
foreach ( $pecas['registros'] as $r ) {
	if ( 'publicavel' === $r['status'] ) { $pub_pecas[ $r['id'] ] = $r; }
}
$pares_servidos = 0;
foreach ( $pub_pecas as $p ) {
	foreach ( (array) $p['compatibilidade'] as $c ) {
		if ( 'declarada_fabricante' === $c['selo'] && isset( $pub_modelos[ $c['modelo'] ] ) ) {
			$pares_servidos++;
		}
	}
}
$marcas_vistas = array();
$sem_link      = 0;
foreach ( array_merge( array_values( $pub_modelos ), array_values( $pub_pecas ) ) as $r ) {
	$marcas_vistas[ $r['marca'] ] = true;
	if ( empty( $r['afiliado']['url'] ) ) { $sem_link++; }
}
$itens = count( $pub_modelos ) + count( $pub_pecas );

$esperado = array(
	'marcas'               => count( $marcas_vistas ),
	'modelos_publicaveis'  => count( $pub_modelos ),
	'pecas_publicaveis'    => count( $pub_pecas ),
	'pares_declarados'     => $pares_servidos,
	'esperando_link'       => $sem_link,
	'r1_responde'          => (int) $cob['resumo']['modelos_que_respondem'],
	'r1_vazia'             => (int) $cob['resumo']['modelos_com_entrada_vazia'],
	'celulas'              => (int) $cob['resumo']['celulas_total'],
	'celulas_sem_resposta' => (int) $cob['resumo']['celulas']['vazia'],
	'as_duas'              => count( $cob['cruzamento_com_a_r2']['as_duas_respondem'] ),
	/* A pagina de divulgacao de afiliados afirma estes dois ao visitante, e a
	   conta deles e feita AQUI, do banco, nao lida da casca. */
	'itens_publicaveis'    => $itens,
	'com_link'             => $itens - $sem_link,
);

/* A conferencia so vale se a medicao chegou: sem ela a casca devolve array()
   vazio de proposito, e comparar vazio com vazio passaria calado. */
rbm_ok( robometria_casca_tem_numeros(), 'a medicao da ilha chegou as options (casca-fatos)' );
rbm_ok( count( $marcas['registros'] ) === count( $marcas_vistas ),
	'toda marca do arquivo aparece em registro publicavel',
	count( $marcas['registros'] ) . ' no arquivo / ' . count( $marcas_vistas ) . ' em uso' );

foreach ( $esperado as $chave => $valor ) {
	rbm_ok( (int) $n[ $chave ] === $valor, "numero '$chave' bate com o banco", 'tela ' . $n[ $chave ] . ' / banco ' . $valor );
}

/* CONTROLE NEGATIVO da casca 1.4.1: fonte sem publicacao nao vira numero.
   O Sync so registra 'dados:<id>' quando APLICA o item, e ele so aplica
   publicar=true. Tirado o registro, a option continua na mesa — e e exatamente
   esse o caso que a funcao tem de recusar, em vez de servir um numero sem pagina
   de origem viva. Se este teste passar a aprovar com a option sozinha, a trava
   caiu. */
$rbm_estado_guardado = $GLOBALS['__options']['robometria_sync_estado'];
unset( $GLOBALS['__options']['robometria_sync_estado']['itens']['dados:casca-fatos'] );
rbm_ok( array() === robometria_casca_numeros(),
	'sem o registro do Sync, casca_numeros() nao publica numero',
	'a option de casca-fatos continua na mesa' );
rbm_ok( ! robometria_casca_tem_numeros(),
	'e quem chama passa a dizer que a medicao esta fora do ar' );
$GLOBALS['__options']['robometria_sync_estado'] = $rbm_estado_guardado;
rbm_ok( robometria_casca_tem_numeros(),
	'devolvido o registro, os numeros voltam' );

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

/* Apelido tem que apontar para pagina que a casca cria, para ferramenta do
   catalogo ou para ARTIGO do catalogo: apelido apontando para slug inexistente e
   404 trocado por 404. O catalogo de artigos entrou aqui junto com o Bloco 5 —
   sem ele, o primeiro artigo com apelido reprovaria por existir. */
$destinos = array_keys( robometria_casca_definicao_paginas() );
foreach ( robometria_casca_ferramentas() as $f ) { $destinos[] = $f['slug']; }
foreach ( robometria_casca_artigos() as $a ) { $destinos[] = $a['slug']; }
$orfaos = array();
foreach ( robometria_casca_apelidos() as $apelido => $destino ) {
	if ( ! in_array( $destino, $destinos, true ) ) { $orfaos[] = $apelido . '→' . $destino; }
	if ( in_array( $apelido, $destinos, true ) ) { $orfaos[] = $apelido . ' (apelido igual a slug real)'; }
}
rbm_ok( empty( $orfaos ), 'todo apelido aponta para pagina ou ferramenta conhecida', empty( $orfaos ) ? count( robometria_casca_apelidos() ) . ' apelidos' : implode( ', ', $orfaos ) );

/* A FOLHA DO FORMULARIO TEM UM DONO SO (casca 1.2.0).
 *
 * Ela estava copiada na R1 e na R2, ja divergindo, e a home passou a servir o
 * mesmo formulario. Contar aqui e o que impede a copia de voltar: uma regra de
 * layout que vive em tres arquivos e ajustada num deles um dia, e a ilha passa a
 * ter dois formularios diferentes sem que ninguem note. Mesmo desenho da porta
 * de compra, que a R1 ja devolveu a casca em 10/09/2026. */
$donos = array();
foreach ( glob( $raiz . '/snippets/*.php' ) as $arquivo ) {
	$corpo = file_get_contents( $arquivo );
	if ( false !== strpos( $corpo, '.rbm-form{' ) || false !== strpos( $corpo, '.rbm-form-campo{' ) ) {
		$donos[] = basename( $arquivo );
	}
}
rbm_ok( array( 'robometria-casca.php' ) === $donos, 'a folha do formulario existe em UM arquivo so, a casca', implode( ' ', $donos ) );

/* ---------------------------------------------------------------------------
 * 10. CABECA DE PAGINA — description e Open Graph (despacho da Sentinela de
 *     11/09/2026, item 1).
 *
 * A Sentinela mediu no ar: document.querySelector('meta[name=description]')
 * devolvia null nas NOVE paginas do sitemap, e nao havia og: nenhum. Este bloco
 * e o portao que impede a tag de sumir de novo, e ele cobra as DUAS DIRECOES —
 * pagina conhecida sem cabeca reprova, e cabeca sobrando tambem. Cobrar so um
 * lado e o defeito de 11/09 no Clube do Mosaico: o teste media a unica categoria
 * que existia quando ele foi escrito.
 *
 * A REGUA E DESTE ARQUIVO, nao do snippet: os limites de tamanho, a proibicao de
 * digito e a lista de termos proibidos estao escritos aqui, e nao lidos de
 * nenhuma funcao da casca. Chamar a regua de quem produziu o dado e o defeito
 * que a secao 8 do contrato descreve — as duas metades erram juntas e o teste
 * passa.
 * ------------------------------------------------------------------------- */

echo "\n10. Cabeca de pagina: description e Open Graph (secao 12.1)\n";

$cabecas = robometria_casca_cabecas();

/* As duas direcoes. O lado esquerdo e TUDO que a ilha publica como pagina:
   as cinco da casca, as ferramentas do catalogo e os artigos do catalogo. */
$publicadas = array_keys( robometria_casca_definicao_paginas() );
foreach ( robometria_casca_ferramentas() as $f ) { $publicadas[] = $f['slug']; }
foreach ( robometria_casca_artigos() as $a )     { $publicadas[] = $a['slug']; }
$publicadas = array_values( array_unique( $publicadas ) );

$sem_cabeca = array_values( array_diff( $publicadas, array_keys( $cabecas ) ) );
$sem_pagina = array_values( array_diff( array_keys( $cabecas ), $publicadas ) );
rbm_ok( empty( $sem_cabeca ), 'toda pagina publicada tem cabeca declarada', empty( $sem_cabeca ) ? count( $publicadas ) . ' paginas' : implode( ' ', $sem_cabeca ) );
rbm_ok( empty( $sem_pagina ), 'nenhuma cabeca sobrando, sem pagina correspondente', empty( $sem_pagina ) ? 'ok' : implode( ' ', $sem_pagina ) );

/* Tamanho: abaixo de 110 o Google completa com texto da pagina, acima de 160 ele
   corta no meio da frase. Os dois casos devolvem ao visitante um trecho que
   ninguem escreveu. */
$curtas = array();
$longas = array();
foreach ( $cabecas as $slug => $c ) {
	$n = mb_strlen( $c['descricao'], 'UTF-8' );
	if ( $n < 110 ) { $curtas[] = $slug . '(' . $n . ')'; }
	if ( $n > 160 ) { $longas[] = $slug . '(' . $n . ')'; }
}
rbm_ok( empty( $curtas ), 'nenhuma description com menos de 110 caracteres', empty( $curtas ) ? 'ok' : implode( ' ', $curtas ) );
rbm_ok( empty( $longas ), 'nenhuma description com mais de 160 caracteres', empty( $longas ) ? 'ok' : implode( ' ', $longas ) );

/* Texto repetido em endereco diferente e o defeito que a tag existe para nao
   ter: o Google escolhe uma das paginas e descarta a outra. */
$textos = array();
foreach ( $cabecas as $c ) { $textos[] = $c['descricao']; }
rbm_ok( count( array_unique( $textos ) ) === count( $textos ), 'as descriptions sao todas diferentes entre si', count( array_unique( $textos ) ) . ' de ' . count( $textos ) );

/* O NOME DA PAGINA SAIU DAQUI e passou a ser um so (casca 1.4.0): o mapa das
   cabecas nao carrega mais titulo, porque um segundo nome digitado ao lado do
   primeiro foi exatamente como seis das nove paginas ficaram com dois nomes.
   Quem cobra o nome agora e ferramentas/teste-voz.php, nas cinco superficies em
   que ele aparece. Aqui fica so a unicidade, que e da mesma familia da
   description repetida: duas paginas com o mesmo nome disputam uma a outra. */
$nomes = array_values( robometria_casca_nomes_das_paginas() );
rbm_ok( count( array_unique( $nomes ) ) === count( $nomes ), 'os nomes de pagina sao todos diferentes entre si', count( array_unique( $nomes ) ) . ' de ' . count( $nomes ) );
rbm_ok( count( $nomes ) === count( $cabecas ), 'toda pagina nomeada tem cabeca, e toda cabeca tem pagina nomeada', count( $nomes ) . ' nomes / ' . count( $cabecas ) . ' cabecas' );

/* NENHUM DIGITO. Description e texto digitado que ninguem relê: um numero aqui
   dentro passa a mentir em silencio no dia em que o banco crescer, e nem na tela
   ele aparece para alguem estranhar. Numero mora na camada de prova (secao 15.2
   do contrato): tabela, resultado, JSON-LD. */
$com_numero = array();
foreach ( $cabecas as $slug => $c ) {
	if ( preg_match( '/\d/u', $c['descricao'] . ' ' . $c['titulo'] ) ) { $com_numero[] = $slug; }
}
rbm_ok( empty( $com_numero ), 'nenhuma cabeca carrega numero (numero mora na camada de prova)', empty( $com_numero ) ? 'ok' : implode( ' ', $com_numero ) );

/* E o que sai no HTML servido, que e a unica coisa que a Sentinela consegue
   medir no ar. Cada pagina da casca renderizada com o slug dela. */
foreach ( $paginas as $tag ) {
	$slug = robometria_teste_slug_do_alvo( $tag );
	$html = $html_por_pagina[ $tag ];
	$c    = isset( $cabecas[ $slug ] ) ? $cabecas[ $slug ] : null;

	$n_desc = substr_count( $html, '<meta name="description"' );
	rbm_ok( 1 === $n_desc, "[$slug] exatamente uma <meta name=description>", "achadas: $n_desc" );

	$esperada = ( null === $c ) ? '' : htmlspecialchars( $c['descricao'], ENT_QUOTES );
	rbm_ok( '' !== $esperada && false !== strpos( $html, '<meta name="description" content="' . $esperada . '">' ),
		"[$slug] o texto servido e o da cabeca declarada" );

	foreach ( array( 'og:type', 'og:title', 'og:description', 'og:url', 'og:site_name' ) as $prop ) {
		rbm_ok( false !== strpos( $html, '<meta property="' . $prop . '"' ), "[$slug] $prop presente" );
	}
}

/* O NEGATIVO: pagina que a casca NAO conhece nao ganha description nenhuma.
   Sem esta medicao, um mapa vazio passaria em tudo acima menos nisto — e a
   alternativa tentadora (uma frase generica de reserva) publicaria a MESMA
   description em endereco diferente, que e exatamente o defeito. */
robometria_teste_rebobinar();
$html_desconhecida = robometria_teste_pagina( 'robometria_home', 'Robometria — teste', 'pagina-que-a-casca-nao-conhece' );
rbm_ok( 0 === substr_count( $html_desconhecida, '<meta name="description"' ), 'pagina desconhecida NAO ganha description generica' );
rbm_ok( 0 === substr_count( $html_desconhecida, '<meta property="og:' ), 'pagina desconhecida NAO ganha Open Graph' );
robometria_teste_rebobinar();

/* ---------------------------------------------------------------------------
 * 11. A VOZ DA ILHA (secao 15 do ARQUIPELAGO.md e VOZ.md desta pasta).
 *
 * A regra e de LUGAR, nao de vizinhanca: titulo e primeiro paragrafo falam com a
 * pessoa, e o vocabulario de dentro da fabrica mora na camada de prova. Por isso
 * o teste procura os termos SO nesses dois lugares, declarados por estrutura (o
 * titulo da definicao de paginas; o primeiro <p> dentro de <main>) — e nunca
 * pela pagina inteira, que e o erro de contar &#038; fora do <script>.
 * ------------------------------------------------------------------------- */

echo "\n11. A voz da home e do header (secao 15, VOZ.md)\n";

/* Regua deste arquivo, lida do VOZ.md pelas maos de quem escreveu o teste. */
$proibidas = array( 'compatibilidade paramétrica', 'especificação', 'matriz', 'procedência', 'base de dados', 'verificável' );

$def_inicio = robometria_casca_definicao_paginas();
$titulo_h1  = $def_inicio['inicio']['titulo'];

rbm_ok( 'Início' !== $titulo_h1, 'o titulo da raiz nao e mais a palavra "Inicio"', $titulo_h1 );
rbm_ok( false !== mb_stripos( $titulo_h1, 'robô aspirador', 0, 'UTF-8' ), 'o titulo da raiz nomeia o assunto da ilha' );

$achadas = array();
foreach ( $proibidas as $termo ) {
	if ( false !== mb_stripos( $titulo_h1, $termo, 0, 'UTF-8' ) ) { $achadas[] = $termo; }
}
rbm_ok( empty( $achadas ), 'nenhum termo proibido no titulo da raiz', empty( $achadas ) ? 'ok' : implode( ' ', $achadas ) );

preg_match( '#<main[^>]*>(.*?)</main>#is', $html_por_pagina['robometria_home'], $mm );
$corpo_da_home = isset( $mm[1] ) ? $mm[1] : '';
preg_match( '#<p\b[^>]*>(.*?)</p>#is', $corpo_da_home, $mp );
$primeiro_p = isset( $mp[1] ) ? trim( strip_tags( $mp[1] ) ) : '';

rbm_ok( '' !== $primeiro_p, 'a home tem um primeiro paragrafo', mb_substr( $primeiro_p, 0, 48, 'UTF-8' ) . '…' );
$achadas = array();
foreach ( $proibidas as $termo ) {
	if ( false !== mb_stripos( $primeiro_p, $termo, 0, 'UTF-8' ) ) { $achadas[] = $termo; }
}
rbm_ok( empty( $achadas ), 'nenhum termo proibido no primeiro paragrafo da home', empty( $achadas ) ? 'ok' : implode( ' ', $achadas ) );

/* A HOME E A FERRAMENTA (molde FERRAMENTA do VOZ.md): o seletor esta servido no
   HTML, nao atras de um clique nem de um script. Sem esta medicao, a home podia
   voltar a ser manifesto sem nenhum teste reclamar. */
rbm_ok( false !== strpos( $corpo_da_home, '<form class="rbm-form"' ), 'o seletor de marca e modelo esta SERVIDO na home' );
rbm_ok( false !== strpos( $corpo_da_home, 'id="rbm-modelo"' ), 'o campo do modelo existe na home' );
rbm_ok( false !== strpos( $corpo_da_home, 'class="rbm-atalhos"' ), 'os atalhos por tipo de peca estao na home' );

/* OS ATALHOS SAO DERIVADOS DO BANCO, nunca digitados — mesma regra do numero de
   tela (secao 8). Contados aqui contra a lista de tipos que o proprio banco
   commitado declara, lida deste arquivo e nao da casca. */
$r1_banco = json_decode( file_get_contents( $raiz . '/dados/r1-respostas.json' ), true );
$n_tipos  = count( $r1_banco['tipos'] );
preg_match( '#<div class="rbm-atalhos">(.*?)</div>#is', $corpo_da_home, $ma );
$n_atalhos = isset( $ma[1] ) ? preg_match_all( '#<li><a\b#i', $ma[1] ) : 0;
rbm_ok( $n_tipos === $n_atalhos, 'um atalho por tipo de peca do banco, contado', "banco $n_tipos / tela $n_atalhos" );

/* O menu do topo: os tres rotulos sao as palavras da pessoa. */
$nav_home = '';
if ( preg_match( '#<nav class="rbm-nav"[^>]*>(.*?)</nav>#is', $html_por_pagina['robometria_home'], $mn2 ) ) { $nav_home = $mn2[1]; }
rbm_ok( false !== strpos( $nav_home, '>Peças</a>' ), 'o menu leva a "Peças", com a palavra da pessoa' );
rbm_ok( false !== strpos( $nav_home, '>Sucção</a>' ), 'o menu leva a "Sucção", com a palavra da pessoa' );
rbm_ok( false === strpos( $nav_home, '>Ferramentas</a>' ), 'o menu nao usa mais o substantivo de dentro da fabrica' );

/* ---------------------------------------------------------------------------
 * 12. PAGINA FINA (secao 8 do ARQUIPELAGO.md, cicatriz do Clube do Mosaico de
 *     11/09/2026).
 *
 * Entra aqui porque a home v1.2.0 PERDEU uma secao inteira — a confissao
 * numerica foi para a metodologia, que e onde a camada de prova mora. Encolher
 * pagina e trabalho legitimo; encolher abaixo do que entra no indice de dominio
 * novo, nao. Esta medicao e o que separa os dois.
 * ------------------------------------------------------------------------- */

/* O BLOCO DE RECUSA DA PAGINA DE AFILIADOS — declarado no markup e contado um a
 * um (cicatriz do Clube do Mosaico, 11/09/2026, secao 8 do contrato). A seccao 7
 * proibe escassez inventada e selo de "mais vendido", e a frase legitima que
 * RECUSA esses termos usa exatamente as mesmas palavras. Quem decide e a
 * estrutura: a pagina marca o bloco com a classe, e todo item dele tem que ABRIR
 * negando — senao bastaria enfiar uma promessa la dentro para ela ficar imune. */
echo "\n11b. Blocos de recusa (secao 7 e 8)\n";
$blocos_recusa = 0;
$itens_recusa  = 0;
$sem_negacao   = array();
foreach ( $paginas as $tag ) {
	preg_match_all( '#<ul class="[^"]*\brbm-recusa\b[^"]*">(.*?)</ul>#is', $html_por_pagina[ $tag ], $mr );
	foreach ( $mr[1] as $recusa ) {
		$blocos_recusa++;
		preg_match_all( '#<li>(.*?)</li>#is', $recusa, $mi );
		foreach ( $mi[1] as $item ) {
			$itens_recusa++;
			$texto = trim( html_entity_decode( strip_tags( $item ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) );
			if ( 0 !== mb_stripos( $texto, 'não ', 0, 'UTF-8' ) && 0 !== mb_stripos( $texto, 'nunca ', 0, 'UTF-8' ) ) {
				$sem_negacao[] = $tag . ': ' . mb_substr( $texto, 0, 32, 'UTF-8' );
			}
		}
	}
}
rbm_ok( $blocos_recusa >= 2, 'os blocos de recusa estao marcados no markup', $blocos_recusa . ' bloco(s)' );
rbm_ok( $itens_recusa >= 6, 'os itens de recusa sao poucos e contados', $itens_recusa . ' itens' );
rbm_ok( $blocos_recusa <= 4, 'e sao POUCOS blocos — marcacao nao pode virar porta dos fundos', $blocos_recusa . ' bloco(s)' );
rbm_ok( empty( $sem_negacao ), 'todo item de bloco de recusa ABRE negando', empty( $sem_negacao ) ? 'ok' : implode( ' | ', $sem_negacao ) );

/* E fora do bloco marcado, o termo proibido nao aparece em pagina nenhuma. */
$vazamentos = array();
foreach ( $paginas as $tag ) {
	$sem_recusa = preg_replace( '#<ul class="[^"]*\brbm-recusa\b[^"]*">.*?</ul>#is', ' ', $html_por_pagina[ $tag ] );
	preg_match( '#<main[^>]*>(.*?)</main>#is', $sem_recusa, $mv );
	$corpo_sem = isset( $mv[1] ) ? $mv[1] : '';
	/* OS TERMOS SAO RADICAIS, nao palavras inteiras, e isso foi MEDIDO: a primeira
	   versao desta regua listava "mais vendido" e deixou passar a mutacao que
	   escreveu "a peça mais vendida da categoria" no corpo da pagina de
	   afiliados. Genero e numero em portugues sao exatamente o buraco por onde a
	   frase proibida entra inteira. */
	foreach ( array( 'mais vendid', 'última unidade', 'últimas unidade', 'última peça', 'últimas peça', 'por tempo limitado', 'restam apenas' ) as $termo ) {
		if ( false !== mb_stripos( $corpo_sem, $termo, 0, 'UTF-8' ) ) { $vazamentos[] = $tag . ':' . $termo; }
	}
}
rbm_ok( empty( $vazamentos ), 'nenhuma escassez inventada fora do bloco de recusa', empty( $vazamentos ) ? 'ok' : implode( ' ', $vazamentos ) );

echo "\n12. Nenhuma pagina fina (secao 8)\n";
foreach ( $paginas as $tag ) {
	preg_match( '#<main[^>]*>(.*?)</main>#is', $html_por_pagina[ $tag ], $mc );
	$texto = isset( $mc[1] ) ? $mc[1] : '';
	$texto = html_entity_decode( preg_replace( '#<[^>]+>#s', ' ', $texto ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	$texto = trim( preg_replace( '/\s+/u', ' ', $texto ) );
	$n     = mb_strlen( $texto, 'UTF-8' );
	rbm_ok( $n >= 1500, "[$tag] corpo com 1.500 caracteres ou mais", $n . ' caracteres' );
}

echo "\n13. O estado degradado sai MARCADO no markup (secao 8)\n";
/* Toda pagina desta ilha tem um segundo estado valido: "estamos sem o banco".
   Ele tem cabecalho, rodape e prosa, e por isso e invisivel para quem mede o
   corpo — foi assim que tres estados foram varridos pela metade em 11/09/2026.
   A marca existe so para a bancada conseguir dizer "isto nao e a pagina", entao
   a ausencia dela e defeito, mesmo sem nada na tela mudar. */
$aviso = robometria_casca_sem_banco_html( 'chamada de teste', 'explicacao de teste' );
rbm_ok( (bool) preg_match( '#class="[^"]*\brbm-sem-banco\b#', $aviso ),
	'o aviso de "sem banco" carrega a classe que a bancada le' );
rbm_ok( (bool) preg_match( '#class="[^"]*\brbm-sem-banco\b#', robometria_casca_sem_medicao_html() ),
	'o aviso de "medicao nao chegou" carrega a mesma classe' );
/* A CLASSE TEM UM DONO SO, e a cobranca e por ARQUIVO, nao por contagem: o
   numero de mencoes dentro da casca muda com um comentario, e teste que reprova
   por comentario ensina a ignora-lo. O que importa e que nenhum outro snippet
   escreva a marca por conta propria — cada copia seria um lugar a mais de onde
   ela pode sumir sozinha, que e a historia da porta de compra da secao 7. */
$com_copia = array();
foreach ( glob( $raiz . '/snippets/*.php' ) as $arq_snip ) {
	if ( basename( $arq_snip ) === 'robometria-casca.php' ) { continue; }
	if ( false !== strpos( file_get_contents( $arq_snip ), 'rbm-sem-banco' ) ) { $com_copia[] = basename( $arq_snip ); }
}
rbm_ok( empty( $com_copia ), 'nenhum outro snippet escreve a marca por conta propria', empty( $com_copia ) ? 'so a casca' : implode( ' ', $com_copia ) );

echo "\n14. Quem cria pagina sincroniza o TITULO dela (secao 8: duas fontes para o mesmo campo)\n";
/* A bancada nao alcanca o WordPress, entao esta se confere no codigo — e e
   melhor do que nao conferir. O caso real: a casca aprendeu na 1.2.0 a
   reespelhar o post_title quando a definicao muda, e os quatro snippets de
   pagina NAO. A pagina nascia com o titulo da constante e ficava com ele para
   sempre; renomear no repositorio trocava o og:title, o cartao e a trilha (que
   sao derivados) e deixava o H1 e o <title> DO AR com o nome antigo — duas
   fontes para o mesmo campo, que e a cicatriz da Aquametria de 11/09/2026, e
   nenhuma bancada podia ver, porque a bancada le a constante. */
foreach ( glob( $raiz . '/snippets/*.php' ) as $arq_snip ) {
	$nome_arq = basename( $arq_snip );
	$fonte_s  = file_get_contents( $arq_snip );
	/* A cobranca e de quem tem NOME PROPRIO de pagina: as cinco paginas da casca
	   (definicao_paginas) e as quatro que vem de uma constante _TITULO. O Sync
	   fica de fora de proposito e nao por descuido — ele grava titulo de item do
	   manifest, e ja o reespelha a cada aplicacao, porque monta um array so para
	   inserir e atualizar. */
	$tem_nome_proprio = ( false !== strpos( $fonte_s, "_TITULO'" ) )
		|| ( false !== strpos( $fonte_s, 'robometria_casca_definicao_paginas' ) );
	if ( ! $tem_nome_proprio || false === strpos( $fonte_s, 'wp_insert_post' ) ) { continue; }
	$sincroniza = preg_match( "#wp_update_post\(\s*array\(\s*'ID'\s*=>\s*\\\$pid,\s*'post_title'#", $fonte_s );
	rbm_ok( (bool) $sincroniza, "[$nome_arq] reespelha o post_title quando o nome muda" );
}

echo "\n15. A versao do manifest e a do snippet dizem a mesma coisa\n";
/* Achado em 11/09/2026 ao fechar a revisao 17: o manifest dizia que a R2 estava
   na 1.0.2 e a constante do snippet dizia 1.0.1. Ninguem tinha errado nada
   visivel — sao duas copias do mesmo numero, e uma envelheceu sozinha. E o
   mesmo defeito do nome da pagina em dois mapas, numa escala menor e igualmente
   calada: quem le o manifest para saber o que esta no ar le um numero que o
   codigo nao sustenta. */
$manifest = json_decode( file_get_contents( $raiz . '/manifest.json' ), true );
foreach ( (array) $manifest['snippets'] as $item ) {
	$fonte_s = file_get_contents( $raiz . '/' . $item['arquivo'] );
	if ( ! preg_match( "#define\(\s*'ROBOMETRIA_[A-Z0-9]+_VERSAO',\s*'([^']+)'#", $fonte_s, $mv2 ) ) { continue; }
	rbm_ok( $mv2[1] === $item['versao'], "[{$item['id']}] a versao do manifest e a da constante",
		'manifest ' . $item['versao'] . ' / snippet ' . $mv2[1] );
}

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

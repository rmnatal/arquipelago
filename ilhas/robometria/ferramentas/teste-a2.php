<?php
/**
 * Verificacao MEDIDA do artigo-ancora A2, sem site e sem rede.
 *
 *   php ferramentas/teste-a2.php .
 *
 * O QUE ELE MEDE QUE OS OUTROS NAO MEDEM, e e a razao de ele existir: a tese
 * deste artigo e uma CONTAGEM, e a decisao 1 do bloco 5 diz que ela nao pode
 * estar digitada no HTML. Provar isso exige mais do que ler a pagina de hoje —
 * exige PLANTAR um banco diferente e ver o texto mudar de forma. E o que a
 * secao 4 deste arquivo faz: cinco bancos adulterados, cada um escolhido para
 * trocar um molde, e a afirmacao de que os numeros de hoje somem da tela quando
 * o banco deixa de sustenta-los.
 *
 * Trava que nunca foi vista reprovando e trava nao medida — e nesta ilha isso
 * ja custou caro duas vezes na mesma execucao, entao aqui as mutacoes rodam
 * DENTRO do teste, toda vez, em vez de terem sido rodadas uma vez por quem
 * escreveu.
 *
 * O que ele NAO substitui: a conferencia da revisao aplicada no /status depois
 * do Sync (secao 4 do ARQUIPELAGO.md).
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function rbm_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-66s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-66s %s\n", $rotulo, $medida );
	return false;
}

function rbm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

function rbm_sem_acento( $t ) {
	$de   = array( 'á','à','â','ã','ä','é','ê','ë','í','î','ï','ó','ô','õ','ö','ú','û','ü','ç',
	               'Á','À','Â','Ã','É','Ê','Í','Ó','Ô','Õ','Ú','Ç','²' );
	$para = array( 'a','a','a','a','a','e','e','e','i','i','i','o','o','o','o','u','u','u','c',
	               'A','A','A','A','E','E','I','O','O','O','U','C','2' );
	return str_replace( $de, $para, (string) $t );
}

/** Texto visivel da pagina, sem marcacao e com as entidades resolvidas. */
function rbm_texto( $html ) {
	$t = preg_replace( '#<script.*?</script>|<style.*?</style>#s', '', $html );
	$t = html_entity_decode( strip_tags( $t ), ENT_QUOTES, 'UTF-8' );
	return preg_replace( '/\s+/u', ' ', $t );
}

/* ------------------------------------------------------------- Montagem */

$fatos = json_decode( file_get_contents( $raiz . '/dados/a2-fatos.json' ), true );

$GLOBALS['__paginas'] = array(
	'ferramentas'                                 => true,
	'metodologia'                                 => true,
	'sobre'                                       => true,
	'divulgacao-de-afiliados'                     => true,
	'qual-peca-serve-no-meu-robo-aspirador'        => true,
	'filtro-universal-de-robo-aspirador'           => true,
	'quantos-pa-o-robo-aspirador-precisa'          => true,
	'quantos-m2-o-robo-aspirador-limpa-por-carga'  => true,
);
$GLOBALS['__fatos_a2'] = $fatos;

robometria_teste_carregar( $raiz );

add_filter( 'robometria_a2_dados', function ( $d ) {
	return $GLOBALS['__fatos_a2'];
} );
add_filter( 'robometria_a2_na_pagina', function () {
	return true;
} );

/**
 * Monta a pagina do A2 com um banco qualquer.
 *
 * O cache estatico de robometria_a2_dados() morre a cada processo, nao a cada
 * chamada — entao as mutacoes rodam num subprocesso, que e o unico jeito
 * honesto de plantar um banco diferente sem o primeiro contaminar o segundo.
 */
function rbm_a2_pagina() {
	robometria_teste_rebobinar();
	return robometria_teste_pagina( 'robometria_a2' );
}

$pagina  = rbm_a2_pagina();
$retorno = $GLOBALS['__retorno_shortcode'];
$texto   = rbm_texto( $pagina );

echo "Robometria — verificacao do artigo-ancora A2 " . ROBOMETRIA_A2_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. Higiene do retorno do shortcode (secao 8).
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";
rbm_ok( false === stripos( $retorno, '<script' ), 'sem <script> no retorno do shortcode' );
rbm_ok( false === stripos( $retorno, '<style' ), 'sem <style> no retorno do shortcode' );
$n = substr_count( rbm_scripts( $pagina ), '&#038;' );
rbm_ok( 0 === $n, 'zero &#038; dentro de <script>', "achados: $n" );
rbm_ok( 0 !== strpos( ltrim( $pagina ), '---' ), 'o corpo nao comeca por metadado YAML' );

/* ---------------------------------------------------------------------------
 * 2. A tese esta na primeira dobra, e e a do banco de hoje.
 * ------------------------------------------------------------------------- */

echo "\n2. A tese, e os numeros dela\n";

$r = $fatos['resumo'];

rbm_ok( false !== strpos( $retorno, esc_html( robometria_a2_tese_da_area() ) ),
	'a tese da area abre a pagina' );
rbm_ok( false !== strpos( $retorno, esc_html( robometria_a2_tese_do_tempo() ) ),
	'a tese do tempo esta servida' );
rbm_ok( false !== strpos( $retorno, esc_html( robometria_a2_tese_da_dispersao() ) ),
	'a tese da dispersao esta servida' );

/* Os numeros da tese tem que aparecer NO TEXTO, e serem os do banco. */
foreach ( array(
	'modelos publicaveis' => $r['modelos_publicaveis'],
	'com cobertura'       => $r['com_cobertura'],
	'com recarga'         => $r['com_recarga'],
	'pares declarados'    => $r['pares_declarados'],
) as $rotulo => $v ) {
	rbm_ok( false !== strpos( $texto, number_format_i18n( $v ) ),
		"o texto traz o numero medido de $rotulo", (string) $v );
}

/* O portao da secao 9: 3 itens de banco reais E um numero calculado proprio. */
rbm_ok( count( $fatos['pares'] ) >= 3, 'pelo menos 3 itens de banco reais na pagina',
	count( $fatos['pares'] ) . ' pares' );
rbm_ok( false !== strpos( $texto, 'm²/min' ) || false !== strpos( $texto, 'm² por minuto' ),
	'a pagina traz um numero calculado proprio (a taxa implicita)' );

/* E a taxa implicita e declarada como NOSSA, nao do fabricante: e uma divisao
   que fizemos, e vende-la como declaracao seria inventar dado tecnico. */
rbm_ok( false !== stripos( $texto, 'é nossa, não do fabricante' )
	|| false !== stripos( $texto, 'e nossa, nao do fabricante' ),
	'a taxa implicita e declarada como conta nossa, nao do fabricante' );

/* ---------------------------------------------------------------------------
 * 3. JSON-LD — e a coerencia dele com a tela.
 * ------------------------------------------------------------------------- */

echo "\n3. JSON-LD (secao 5, item 3)\n";

preg_match( '#<script type="application/ld\+json" id="robometria-a2-jsonld">(.*?)</script>#s', $pagina, $mj );
rbm_ok( ! empty( $mj[1] ), 'a pagina serve JSON-LD proprio' );
$ld = json_decode( isset( $mj[1] ) ? $mj[1] : '', true );
rbm_ok( is_array( $ld ) && ! empty( $ld['@graph'] ), 'o JSON-LD e JSON valido' );

$tipos = array();
$artigo = null;
$faq    = null;
foreach ( (array) $ld['@graph'] as $no ) {
	$tipos[] = $no['@type'];
	if ( 'Article' === $no['@type'] ) { $artigo = $no; }
	if ( 'FAQPage' === $no['@type'] ) { $faq = $no; }
}
rbm_ok( in_array( 'Article', $tipos, true ), 'Article no artigo' );
rbm_ok( in_array( 'FAQPage', $tipos, true ), 'FAQPage nas perguntas do corpus' );

/* A DESCRICAO E PARTE DA TESE: e a mesma frase derivada que abre a pagina. */
rbm_ok( $artigo['description'] === robometria_a2_tese_da_area(),
	'a description do Article e a tese derivada, e nao um resumo escrito a mao' );

rbm_ok( count( (array) $faq['mainEntity'] ) === count( (array) $fatos['perguntas'] ),
	'toda pergunta dos fatos virou pergunta do FAQPage' );

$reescritas = 0;
foreach ( (array) $faq['mainEntity'] as $i => $q ) {
	if ( $q['acceptedAnswer']['text'] !== $fatos['perguntas'][ $i ]['resposta'] ) {
		$reescritas++;
	}
}
rbm_ok( 0 === $reescritas, 'nenhuma resposta do FAQPage foi reescrita a mao no snippet' );

/**
 * O ACENTO DENTRO DO JSON-LD.
 *
 * Esta medicao nasceu de um defeito real, achado no A1 desta mesma ilha em
 * 10/09/2026: ele publica "Nao. Nas 16 pecas de reposicao..." dentro do
 * FAQPage, em ASCII, porque as respostas vinham do arquivo de fatos escritas
 * como o banco escreve. O banco e ASCII porque ele CITA fontes; o que a ilha
 * ESCREVE sai em portugues de verdade (fase 4b do playbook). E o canal em que o
 * defeito aparece e justamente o que a secao 5 do ARQUIPELAGO.md diz valer
 * tanto quanto ranquear.
 */
$sem_acento = array();
foreach ( (array) $faq['mainEntity'] as $q ) {
	$t = $q['acceptedAnswer']['text'];
	if ( rbm_sem_acento( $t ) === $t ) {
		$sem_acento[] = mb_substr( $q['name'], 0, 40 );
	}
}
rbm_ok( empty( $sem_acento ), 'as respostas do FAQPage saem ACENTUADAS, e nao no ASCII do banco',
	empty( $sem_acento ) ? count( $faq['mainEntity'] ) . ' respostas' : implode( ' | ', $sem_acento ) );

/**
 * E CADA RESPOSTA TEM QUE ESTAR SUSTENTADA PELO CORPO DA PAGINA.
 *
 * A busca e no RETORNO DO SHORTCODE, nunca no HTML inteiro: procurar na pagina
 * completa faz o teste achar o texto dentro do proprio bloco de JSON-LD e passar
 * sempre, inclusive com resposta inventada. Foi exatamente esse o engano que a
 * verificacao da R2 descobriu em si mesma nesta execucao.
 *
 * Aqui a exigencia e pelos NUMEROS: a resposta do FAQPage pode ser mais curta
 * que o paragrafo da tela, mas todo numero que ela afirma tem que estar escrito
 * na pagina que o leitor le.
 */
$faq_sem_lastro = array();
foreach ( (array) $faq['mainEntity'] as $q ) {
	preg_match_all( '/\d[\d.,]*/u', $q['acceptedAnswer']['text'], $mn );
	foreach ( array_unique( $mn[0] ) as $numero ) {
		if ( false === strpos( $texto, $numero ) ) {
			$faq_sem_lastro[] = $numero . ' (' . mb_substr( $q['name'], 0, 30 ) . ')';
		}
	}
}
rbm_ok( empty( $faq_sem_lastro ), 'todo numero das respostas do FAQPage esta escrito no corpo',
	empty( $faq_sem_lastro ) ? 'todos' : implode( ' | ', array_slice( $faq_sem_lastro, 0, 5 ) ) );

rbm_ok( false !== strpos( $pagina, '<link rel="canonical" href="https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/">' ),
	'a canonica aponta para o endereco proprio do artigo' );

/* ---------------------------------------------------------------------------
 * 4. A TESE E DERIVADA — provado plantando bancos diferentes.
 *
 * Esta e a secao que justifica o arquivo. Ler a pagina de hoje so prova que ela
 * esta certa hoje; a decisao 1 do bloco 5 e sobre AMANHA, quando o banco crescer
 * e ninguem reler o artigo. Entao aqui o banco e adulterado de proposito, uma
 * mutacao por molde, e a exigencia e dupla: o texto muda de forma E os numeros
 * de hoje somem dele.
 * ------------------------------------------------------------------------- */

echo "\n4. A tese muda quando o banco muda (decisao 1 do bloco 5)\n";

/** Roda o artigo num SUBPROCESSO com o banco adulterado e devolve o texto. */
function rbm_a2_com_banco( $raiz, $mutacao ) {
	return rbm_texto( rbm_a2_html_com_banco( $raiz, $mutacao ) );
}

function rbm_a2_html_com_banco( $raiz, $mutacao ) {
	$tmp = tempnam( sys_get_temp_dir(), 'a2' );
	file_put_contents( $tmp, json_encode( $mutacao ) );

	$codigo = <<<'PHP'
require $argv[1] . '/ferramentas/render-para-teste.php';
$GLOBALS['__paginas'] = array('metodologia'=>true,'divulgacao-de-afiliados'=>true);
$GLOBALS['__fatos_a2'] = json_decode(file_get_contents($argv[2]), true);
robometria_teste_carregar($argv[1]);
add_filter('robometria_a2_dados', function ($d) { return $GLOBALS['__fatos_a2']; });
add_filter('robometria_a2_na_pagina', function () { return true; });
echo robometria_teste_pagina('robometria_a2');
PHP;
	$arq = tempnam( sys_get_temp_dir(), 'a2run' );
	file_put_contents( $arq, "<?php\n" . $codigo );

	$saida = shell_exec( 'php ' . escapeshellarg( $arq ) . ' '
		. escapeshellarg( $raiz ) . ' ' . escapeshellarg( $tmp ) . ' 2>&1' );

	@unlink( $tmp );
	@unlink( $arq );
	return (string) $saida;
}

/**
 * O PARAGRAFO, e nao a pagina inteira — as duas camadas da abertura, separadas.
 *
 * Medir a tese na pagina toda deixou passar, em 11/09/2026, uma mutacao que
 * mudou a tese de forma: a frase procurada continuava existindo em OUTRA secao
 * do artigo, e o teste aprovou sem olhar para a abertura. E o mesmo erro de
 * contar `&#038;` na pagina inteira em vez de dentro do <script>, e a mesma
 * resposta: quem afirma sobre a abertura le a ABERTURA.
 *
 * `qual`: 'mestra' devolve a linha-mestra; 'prova' devolve os blocos marcados
 * como camada de prova, concatenados.
 */
function rbm_a2_paragrafo( $raiz, $mutacao, $qual ) {
	$html = rbm_a2_html_com_banco( $raiz, $mutacao );
	if ( 'mestra' === $qual ) {
		return preg_match( '#<p class="rbm-linha-mestra">(.*?)</p>#is', $html, $m )
			? rbm_texto( $m[1] ) : '';
	}
	$juntos = '';
	if ( preg_match_all( '#<p[^>]*class="[^"]*\brbm-prova\b[^"]*"[^>]*>(.*?)</p>#is', $html, $m ) ) {
		$juntos = implode( ' ', $m[1] );
	}
	return rbm_texto( $juntos );
}

/* A mutacao 0 nao muda nada: se o subprocesso nao reproduzir a pagina de hoje,
   nenhuma conclusao das mutacoes seguintes vale. */
$controle = rbm_a2_com_banco( $raiz, $fatos );
rbm_ok( false !== strpos( $controle, rbm_sem_acento( '' ) . number_format_i18n( $r['com_cobertura'] ) ),
	'controle: o subprocesso reproduz a pagina de hoje' );

/* --- mutacao A: nenhum fabricante declara area por carga ------------------ */
$m = $fatos;
$m['resumo']['com_cobertura'] = 0;
$m['marcas_que_declaram']     = array();
$m['vitrine']                 = array();
$t = rbm_a2_com_banco( $raiz, $m );
$mestra = rbm_a2_paragrafo( $raiz, $m, 'mestra' );
rbm_ok( false !== stripos( $mestra, 'nenhum dos' ) && false !== stripos( $mestra, 'tem esse número declarado' ),
	'[A] com zero declaracoes, a tese troca de molde', mb_substr( $mestra, 0, 60 ) );
rbm_ok( false !== stripos( $t, 'não há o que listar' ),
	'[A] sem item elegivel o bloco de compra nao lista, e diz por que (secao 7)' );

/* --- mutacao B: duas marcas declaram -------------------------------------- */
$m = $fatos;
$m['marcas_que_declaram']     = array( 'Electrolux', 'Marca Plantada' );
$m['resumo']['com_cobertura'] = 9;
$t      = rbm_a2_com_banco( $raiz, $m );
$mestra = rbm_a2_paragrafo( $raiz, $m, 'mestra' );
$prova  = rbm_a2_paragrafo( $raiz, $m, 'prova' );
rbm_ok( false !== stripos( $mestra, 'em 2 marcas' ) && false === stripos( $mestra, 'Marca Plantada' ),
	'[B] com duas marcas, a tese troca de molde e NAO nomeia marca na abertura', mb_substr( $mestra, 0, 60 ) );
rbm_ok( false !== stripos( $prova, 'Marca Plantada' ) && false !== stripos( $prova, 'Electrolux' ),
	'[B] quem declara e nomeado na camada de prova, um paragrafo abaixo', mb_substr( $prova, 0, 60 ) );
rbm_ok( false === strpos( $t, 'Uma marca só declara' ),
	'[B] o molde de marca unica sai de cena' );

/* --- mutacao C: um modelo passa a ter os tres numeros --------------------- */
$m = $fatos;
$m['resumo']['com_os_tres'] = 2;
$t = rbm_a2_com_banco( $raiz, $m );
rbm_ok( false !== stripos( $t, 'têm os três' ) && false !== stripos( $t, 'a conta fecha' ),
	'[C] com modelo completo, a tese do tempo troca de molde' );
rbm_ok( false === stripos( $t, 'nenhum dos 28 modelos deste banco tem os três' ),
	'[C] a frase do "nenhum" some quando deixa de valer' );

/* --- mutacao D: os pares passam a ser de marcas diferentes ---------------- */
$m = $fatos;
$m['dispersao']['mesma_marca'] = false;
$m['dispersao']['marcas']      = array( 'Electrolux', 'Marca Plantada' );
$t = rbm_a2_com_banco( $raiz, $m );
rbm_ok( false !== stripos( $t, 'Aplicar uma média' ),
	'[D] com marcas diferentes, a tese da dispersao troca de molde' );
rbm_ok( false === stripos( $t, 'dentro do MESMO fabricante' ),
	'[D] a frase do "mesmo fabricante" some quando deixa de valer' );

/* --- mutacao E: so sobra um par ------------------------------------------- */
$m = $fatos;
$m['dispersao'] = null;
$m['pares']     = array( $fatos['pares'][0] );
$t = rbm_a2_com_banco( $raiz, $m );
rbm_ok( false !== stripos( $t, 'um ponto não é um coeficiente' ),
	'[E] com um par so, a pagina diz que um ponto nao e um coeficiente' );

/* --- mutacao F: o banco inteiro muda de tamanho --------------------------- */
/* A prova de que NENHUM numero esta digitado: trocados os totais, os numeros de
   hoje precisam sumir da tela. */
$m = $fatos;
$m['resumo']['modelos_publicaveis'] = 137;
$m['resumo']['com_cobertura']       = 41;
$m['resumo']['com_recarga']         = 19;
$m['resumo']['pares_declarados']    = 41;
/* A lista de pares muda JUNTO com o resumo. Mutacao incoerente — resumo novo e
   lista velha — nao prova nada: o numero antigo sobreviveria na tela por ser
   verdadeiro sobre a lista, e o teste acusaria o codigo de um defeito que e do
   proprio teste. Foi o que aconteceu na primeira rodada desta secao. */
$m['pares'] = array();
for ( $k = 0; $k < 41; $k++ ) {
	$m['pares'][] = array(
		'modelo' => 'plantado-' . $k, 'rotulo' => 'Plantado ' . $k,
		'marca' => 'Marca Plantada', 'cobertura_m2' => 300 + $k,
		'autonomia_min' => 200, 'taxa' => 1.5,
	);
}
$t = rbm_a2_com_banco( $raiz, $m );
rbm_ok( false !== strpos( $t, '137' ) && false !== strpos( $t, '41' ),
	'[F] os numeros novos aparecem na tela' );
$sobreviveu = array();
foreach ( array( $r['modelos_publicaveis'], $r['com_cobertura'], $r['com_recarga'] ) as $v ) {
	/* A vitrine e as tabelas continuam listando os registros de verdade, entao a
	   busca e nas FRASES da abertura — que e onde a tese mora. */
	$abertura = mb_substr( $t, 0, 1200 );
	if ( false !== strpos( $abertura, ' ' . number_format_i18n( $v ) . ' ' ) ) {
		$sobreviveu[] = $v;
	}
}
rbm_ok( empty( $sobreviveu ), '[F] nenhum numero do banco de hoje ficou digitado na tese',
	empty( $sobreviveu ) ? 'nenhum' : implode( ' ', $sobreviveu ) );

/* ---------------------------------------------------------------------------
 * 5. PORTA DE COMPRA x PROCEDENCIA (secao 7).
 * ------------------------------------------------------------------------- */

echo "\n5. Porta de compra e vitrine (secao 7)\n";

rbm_ok( false !== strpos( $pagina, 'rbm-vitrine' ), 'a pagina serve vitrine' );
rbm_ok( false !== strpos( $pagina, 'Link de loja em breve' ),
	'o lugar do link fica reservado enquanto o cano de links enche' );
rbm_ok( false !== strpos( $texto, 'links de afiliado' ),
	'o aviso de comissao aparece dentro do bloco de compra' );
rbm_ok( false !== stripos( $texto, 'não é um ranking' ),
	'a pagina diz que a lista NAO e um ranking de limpeza' );

/* Produto sem imagem nao some: entra com espaco reservado neutro (secao 6). */
$sem_foto = 0;
foreach ( $fatos['vitrine'] as $i ) {
	if ( empty( $i['tem_imagem'] ) ) { $sem_foto++; }
}
/* A contagem e no CORPO, e nao na pagina: a folha da casca tambem cita a classe
   `.rbm-vitrine-vazia`, e conta-la ali daria um a mais sem nenhum item a mais —
   o mesmo engano de contar `&#038;` na pagina inteira em vez de dentro do
   <script> (secao 8 do ARQUIPELAGO.md). */
rbm_ok( substr_count( $retorno, 'rbm-vitrine-vazia' ) === $sem_foto,
	'todo item sem foto entra com espaco reservado, e nenhum some',
	$sem_foto . ' sem foto de ' . count( $fatos['vitrine'] ) );

/* A folha da vitrine vem da CASCA, e nao de uma copia local. */
preg_match( '#<style id="robometria-a2">(.*?)</style>#s', $pagina, $mc );
$css = isset( $mc[1] ) ? $mc[1] : '';
rbm_ok( false !== strpos( $css, '.rbm-vitrine{' ),
	'a folha da vitrine veio da casca, e nao de uma copia local' );
rbm_ok( false === strpos( file_get_contents( $raiz . '/snippets/robometria-a2.php' ), 'rel="sponsored' ),
	'o snippet nao escreve a propria porta de compra — delega para a casca' );

/* ---------------------------------------------------------------------------
 * 6. Malha (secao 9): duas listagens e tres irmas.
 * ------------------------------------------------------------------------- */

echo "\n6. Malha (secao 9)\n";

foreach ( array(
	'quantos-pa-o-robo-aspirador-precisa'   => 'a ferramenta que este artigo apoia',
	'qual-peca-serve-no-meu-robo-aspirador'  => 'a outra ferramenta da ilha',
	'filtro-universal-de-robo-aspirador'     => 'o outro artigo da ilha',
) as $slug => $quem ) {
	rbm_ok( false !== strpos( $pagina, $slug ), "aponta para $quem" );
}

$artigos = robometria_casca_artigos();
$a2 = null;
foreach ( $artigos as $a ) {
	if ( 'A2' === $a['codigo'] ) { $a2 = $a; }
}
rbm_ok( null !== $a2, 'o artigo se registra no catalogo da casca pelo filtro' );
rbm_ok( $a2 && ROBOMETRIA_A2_SLUG === $a2['slug'], 'o slug do cartao e o da pagina' );
rbm_ok( count( $artigos ) >= 2, 'a ilha tem mais de um artigo no catalogo',
	count( $artigos ) . ' artigos' );

/* NAO tem formulario: a consulta e da ferramenta (decisao 3 do bloco 5). Duas
   paginas respondendo a mesma coisa competem entre si no indice (secao 14.4). */
rbm_ok( false === stripos( $retorno, '<form' ), 'o artigo nao repete a ferramenta — sem formulario' );

/* ---------------------------------------------------------------------------
 * 7. A SERP nao foi verificada, e a pagina registra isso (secao 14.9).
 * ------------------------------------------------------------------------- */

echo "\n7. Honestidade sobre a SERP (secao 14.9)\n";

rbm_ok( isset( $fatos['serp'] ), 'os fatos carregam o campo serp' );
rbm_ok( false === $fatos['serp']['verificada_nesta_execucao'],
	'o campo diz que a SERP NAO foi verificada nesta execucao' );
rbm_ok( ! empty( $fatos['serp']['consulta_alvo'] ),
	'a consulta-alvo esta nomeada', $fatos['serp']['consulta_alvo'] );
rbm_ok( ! empty( $fatos['serp']['por_que_chega_as_dez_primeiras'] ),
	'esta escrito por que a pagina consegue chegar as dez primeiras' );

/* ---------------------------------------------------------------------------
 * 8. Identidade e higiene.
 * ------------------------------------------------------------------------- */

echo "\n8. Identidade e higiene (secoes 6 e 8)\n";

rbm_ok( false === stripos( $css, 'gradient' ), 'nenhum gradiente na folha do artigo' );
rbm_ok( false === stripos( $retorno, '#CC3311' ),
	'a varredura nao aparece no corpo — ela e cor de sinal, e o uso da tela e o logotipo' );
rbm_ok( substr_count( $pagina, 'class="rbm-num"' ) > 0,
	'os numeros saem na classe monoespacada da ilha' );

$fonte = file_get_contents( $raiz . '/snippets/robometria-a2.php' );
rbm_ok( 0 === strpos( $fonte, '/**' ), 'o snippet comeca com /** e sem <?php no topo' );
rbm_ok( false === strpos( $fonte, '$_SERVER' ), 'nenhuma superglobal de servidor, nem dentro de comentario' );
rbm_ok( false === strpos( $fonte, '$_GET' ) && false === strpos( $fonte, '$_REQUEST' ),
	'nenhuma superglobal de entrada' );

preg_match_all( '/^function\s+([a-z0-9_]+)\s*\(/mi', $fonte, $mfn );
$desprotegidas = array();
foreach ( $mfn[1] as $nome ) {
	if ( false === strpos( $fonte, "function_exists( '" . $nome . "' )" ) ) {
		$desprotegidas[] = $nome;
	}
}
rbm_ok( empty( $desprotegidas ), 'toda funcao de nivel superior dentro de function_exists',
	empty( $desprotegidas ) ? count( $mfn[1] ) . ' funcoes' : implode( ' ', $desprotegidas ) );

rbm_ok( false !== strpos( $retorno, 'não' ), 'o texto da tela sai acentuado' );

/* ---------------------------------------------------------------------------
 * 9. A PROCEDENCIA DA AREA POR CARGA, no cartao (secoes 5.4 e 7)
 *
 * A area por carga e o unico numero que faz um modelo entrar nesta lista, e ate
 * 12/09/2026 o cartao a publicava sem endereco, sem data e sem degrau, com a
 * atribuicao "O fabricante declara" DIGITADA no molde. Aqui isso nao era nem
 * verdade por coincidencia, como era na R2 antes de 11/09: os cinco modelos que
 * declaram area por carga declaram todos pela fonte f-loja, que e o degrau 4
 * (loja oficial da marca). A pagina no ar emprestava a autoridade do fabricante
 * a quem apenas transcreveu.
 *
 * OS TRES CUIDADOS QUE A R2 JA PAGOU, e que esta secao repete de proposito:
 *
 *   REGUA PROPRIA — o esperado e derivado AQUI, de dados/esquema-banco.json e
 *   dados/modelos-robo.json, e nunca de dados/a2-fatos.json nem de
 *   robometria_a2_dados(). Conferir a tela contra o arquivo que o MESMO gerador
 *   escreveu e conferir uma copia contra a outra: as duas erram juntas.
 *
 *   MEDICAO NO CORPO — cada afirmacao e medida dentro do <li> do cartao, nunca
 *   na pagina inteira. A secao de procedencia do artigo tambem fala em
 *   "fabricante" e em endereco, e medir na pagina inteira aprovaria um cartao
 *   mudo.
 *
 *   A ENTRADA INTEIRA — os cinco cartoes, e nao o primeiro.
 * ------------------------------------------------------------------------- */

echo "\n9. A procedencia da area por carga, no cartao (secoes 5.4 e 7)\n";

/* A REGUA: a escada de fontes e o banco, lidos direto. */
$esquema_r  = json_decode( file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$modelos_r  = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$marcas_r   = json_decode( file_get_contents( $raiz . '/dados/marcas.json' ), true );

$degraus_r = array();
foreach ( $esquema_r['escada_de_fontes']['niveis'] as $n ) {
	$degraus_r[ $n['origem'] ] = $n['na_tela'];
}

/* rotulo do modelo -> o modelo, montado da mesma forma que a ilha monta o nome
   na tela (marca + codigo do fabricante). E uma reimplementacao de uma linha, e
   e de proposito: ela nao passa por nenhum arquivo que o gerador escreve. */
$nome_da_marca = array();
foreach ( (array) $marcas_r['registros'] as $b ) {
	$nome_da_marca[ $b['id'] ] = $b['nome'];
}
$por_rotulo = array();
foreach ( (array) $modelos_r['registros'] as $m ) {
	$por_rotulo[ $nome_da_marca[ $m['marca'] ] . ' ' . $m['codigo_fabricante'] ] = $m;
}

/* Cada cartao, recortado do CORPO. */
preg_match_all( '#<li class="rbm-vitrine-item">(.*?)</li>#s', $retorno, $mcart );
$cartoes = $mcart[1];

rbm_ok( count( $cartoes ) > 0, 'a vitrine serve cartoes no corpo', count( $cartoes ) . ' cartoes' );

$sem_procedencia = array();
$atribuicao_errada = array();
$sem_ressalva      = array();
$sem_endereco      = array();
$fora_de_ordem     = array();
$origens_vistas    = array();

foreach ( $cartoes as $c ) {
	preg_match( '#<span class="rbm-vitrine-tipo">(.*?)</span>#s', $c, $mt );
	$rotulo = isset( $mt[1] ) ? html_entity_decode( $mt[1], ENT_QUOTES, 'UTF-8' ) : '';

	if ( ! isset( $por_rotulo[ $rotulo ] ) ) {
		$sem_procedencia[] = $rotulo . ' (nao achei no banco)';
		continue;
	}
	$m = $por_rotulo[ $rotulo ];

	/* O DEGRAU ESPERADO, derivado do banco pela regua deste arquivo. */
	$fid   = $m['cobertura_m2_declarada']['fonte'];
	$fonte = $m['fontes'][ $fid ];
	$esp   = $degraus_r[ $fonte['origem'] ];
	$origens_vistas[ $fonte['origem'] ] = true;

	$texto_c = rbm_texto( $c );

	/* 1. A ATRIBUICAO E A DO DEGRAU, e nao a digitada. */
	if ( false === strpos( $texto_c, $esp['quem_declara'] ) ) {
		$atribuicao_errada[] = $rotulo . ' (esperava "' . $esp['quem_declara'] . '")';
	}

	/* 1b. O SEGUNDO NUMERO DA FRASE TEM DEGRAU PROPRIO. Hoje os dois saem da
	       mesma fonte nos cinco modelos, entao esta asercao e VAZIA com o banco
	       de hoje — e e por isso que ela existe: no dia em que uma autonomia
	       entrar por outro degrau, o cartao tem que dizer qual, em vez de
	       herdar calado a atribuicao do numero anterior. Quem prova que ela
	       morde e mutacoes-a2-procedencia.py, que produz esse banco. */
	$fa = isset( $m['autonomia_min_declarada']['fonte'] ) ? $m['autonomia_min_declarada']['fonte'] : null;
	if ( null !== $fa ) {
		$origem_aut = $m['fontes'][ $fa ]['origem'];
		if ( $origem_aut === $fonte['origem'] ) {
			if ( false === strpos( $texto_c, 'pela mesma fonte' ) ) {
				$atribuicao_errada[] = $rotulo . ' (autonomia: esperava "pela mesma fonte")';
			}
		} elseif ( false === strpos( $texto_c, $degraus_r[ $origem_aut ]['quem_declara'] ) ) {
			$atribuicao_errada[] = $rotulo . ' (autonomia: esperava "'
				. $degraus_r[ $origem_aut ]['quem_declara'] . '")';
		}
	}

	/* 2. A RESSALVA DO DEGRAU chega a tela, quando o degrau tem uma. */
	if ( ! empty( $esp['ressalva'] ) && false === strpos( $texto_c, $esp['ressalva'] ) ) {
		$sem_ressalva[] = $rotulo;
	}

	/* 3. O ENDERECO E A DATA, dentro do cartao. */
	$data_br = substr( $fonte['verificado_em'], 8, 2 ) . '/'
		. substr( $fonte['verificado_em'], 5, 2 ) . '/'
		. substr( $fonte['verificado_em'], 0, 4 );
	$tem_linha = false !== strpos( $texto_c, 'Como sabemos — ' . $esp['rotulo'] . ', verificado em ' . $data_br );
	if ( ! $tem_linha ) {
		$sem_procedencia[] = $rotulo;
	}
	if ( false === strpos( $c, $fonte['url'] ) ) {
		$sem_endereco[] = $rotulo;
	}

	/* 4. A PORTA DE COMPRA VEM ANTES DA PROCEDENCIA (secao 7). Inverter os dois
	      devolve ao link de procedencia o papel de unica porta clicavel — a
	      cicatriz de 10/09/2026, e ela e medida por POSICAO, nao por presenca. */
	$p_acao  = strpos( $c, 'rbm-vitrine-acao' );
	$p_fonte = strpos( $c, 'rbm-vitrine-fonte' );
	if ( false === $p_acao || false === $p_fonte || $p_acao > $p_fonte ) {
		$fora_de_ordem[] = $rotulo;
	}

	/* 5. E A RESSALVA VEM ANTES DA PORTA DE COMPRA. Esta afirmacao faltava, e
	      quem a cobrou foi uma mutacao: a ressalva podia ser empurrada para
	      depois do botao sem a bancada piscar, porque o teste so media que ela
	      ESTIVESSE na tela. Ressalva que aparece depois da decisao nao e
	      ressalva, e nota de rodape — o elo fraco tem que estar onde o leitor
	      ainda esta decidindo. */
	if ( ! empty( $esp['ressalva'] ) ) {
		$p_tag = strpos( $c, 'rbm-tag' );
		if ( false === $p_tag || false === $p_acao || $p_tag > $p_acao ) {
			$fora_de_ordem[] = $rotulo . ' (ressalva depois do botao)';
		}
	}
}

rbm_ok( empty( $sem_procedencia ), 'todo cartao diz de onde vem a area, com rotulo e data',
	empty( $sem_procedencia ) ? count( $cartoes ) . ' cartoes' : implode( ', ', $sem_procedencia ) );
rbm_ok( empty( $atribuicao_errada ), 'a atribuicao de cada cartao e a do DEGRAU, nao uma digitada',
	empty( $atribuicao_errada ) ? 'os ' . count( $cartoes ) : implode( ', ', $atribuicao_errada ) );
rbm_ok( empty( $sem_ressalva ), 'a ressalva do degrau chega a tela',
	empty( $sem_ressalva ) ? 'em todos que a tem' : implode( ', ', $sem_ressalva ) );
rbm_ok( empty( $sem_endereco ), 'o endereco da fonte esta no cartao',
	empty( $sem_endereco ) ? 'os ' . count( $cartoes ) : implode( ', ', $sem_endereco ) );
rbm_ok( empty( $fora_de_ordem ), 'a porta de compra vem ANTES da procedencia, em todo cartao',
	empty( $fora_de_ordem ) ? 'os ' . count( $cartoes ) : implode( ', ', $fora_de_ordem ) );

/* A ATRIBUICAO FALSA QUE ESTAVA NO AR ATE 12/09/2026. Medida no corpo, e nao na
   pagina: a secao de procedencia do artigo fala de "paginas de fabricante" com
   razao, e medir na pagina inteira reprovaria texto correto. */
$falsa = false;
foreach ( $cartoes as $c ) {
	if ( false !== strpos( rbm_texto( $c ), 'O fabricante declara' ) ) {
		$falsa = true;
	}
}
rbm_ok( ! $falsa, 'nenhum cartao atribui ao fabricante o que a loja oficial declarou' );

/* O TITULO DA SECAO fala dos cinco de uma vez: so nomeia um publicador quando
   TODOS declaram pelo mesmo degrau. Este teste deriva a condicao da regua. */
$origens = array_keys( $origens_vistas );
if ( 1 === count( $origens ) ) {
	$q = $degraus_r[ $origens[0] ]['quem_declara'];
	rbm_ok( false !== strpos( $texto, 'área por carga é declarada ' . $q ),
		'com um degrau so, o titulo da secao nomeia esse degrau', $q );
} else {
	rbm_ok( false !== strpos( $texto, 'declarada, e por quem' ),
		'com degraus misturados, o titulo nao atribui a lista a um publicador',
		count( $origens ) . ' degraus' );
}

/* O TEXTO DO DEGRAU NAO MORA NO SNIPPET. E o portao estrutural: enquanto nenhum
   rotulo, ressalva ou atribuicao da escada aparecer literalmente no CODIGO, nao
   ha como a tela discordar do banco — e trocar o texto de um degrau no esquema
   passa a mudar a pagina sem ninguem reescrever uma linha de codigo.

   A MEDICAO E NO CODIGO, e nao no arquivo: os comentarios deste snippet contam a
   historia do defeito e citam "loja oficial da marca" de proposito, porque e
   assim que a proxima pessoa entende por que a atribuicao e lida e nao escrita.
   Comentario nao chega a tela. Medir o arquivo inteiro aqui seria o mesmo engano
   de contar `&#038;` na pagina toda em vez de dentro do <script> — reprovaria
   justamente a documentacao que faz a trava durar. */
$fonte_a2  = file_get_contents( $raiz . '/snippets/robometria-a2.php' );
$codigo_a2 = preg_replace( '#/\*.*?\*/|//[^\n]*#s', '', $fonte_a2 );
$vazados   = array();
foreach ( $degraus_r as $origem => $t ) {
	foreach ( array( 'rotulo', 'ressalva', 'quem_declara' ) as $campo ) {
		if ( ! empty( $t[ $campo ] ) && false !== strpos( $codigo_a2, $t[ $campo ] ) ) {
			$vazados[] = $origem . '.' . $campo;
		}
	}
}
rbm_ok( empty( $vazados ), 'nenhum texto de degrau esta digitado dentro do snippet',
	empty( $vazados ) ? count( $degraus_r ) . ' degraus conferidos' : implode( ' ', $vazados ) );

/* A TABELA QUE VIAJA PARA O SITE E A ESCADA, e nao uma copia dela. O snippet le
   `rotulos_de_origem` do arquivo de dados, e esse arquivo pode divergir do
   esquema sem ninguem ver — foi o que uma mutacao mostrou, perdendo a ressalva
   do degrau 4 no lado que o site consome enquanto a escada continuava inteira.
   Duas copias do mesmo fato, nenhuma capaz de corrigir a outra: e o defeito que
   a casca 1.2.0 desta ilha ja pagou com dois mapas de nome. */
$tabela   = isset( $fatos['rotulos_de_origem'] ) ? $fatos['rotulos_de_origem'] : array();
$divergem = array();
foreach ( $degraus_r as $origem => $t ) {
	if ( ! isset( $tabela[ $origem ] ) ) {
		$divergem[] = $origem . ' (ausente)';
		continue;
	}
	foreach ( array( 'rotulo', 'ressalva', 'quem_declara' ) as $campo ) {
		$na_tabela = array_key_exists( $campo, $tabela[ $origem ] ) ? $tabela[ $origem ][ $campo ] : false;
		if ( $na_tabela !== $t[ $campo ] ) {
			$divergem[] = $origem . '.' . $campo;
		}
	}
}
rbm_ok( empty( $divergem ), 'a tabela que viaja para o site e igual a escada, degrau a degrau',
	empty( $divergem ) ? count( $degraus_r ) . ' degraus' : implode( ' ', $divergem ) );

/* ------------------------------------------------------------------ RESUMO */

echo "\n";
printf( "%d medicoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

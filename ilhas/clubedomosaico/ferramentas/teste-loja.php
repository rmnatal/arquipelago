<?php
/**
 * Verificacao MEDIDA do snippet da Loja (bloco 4d), sem site e sem rede.
 *
 *   php ferramentas/teste-loja.php .
 *
 * AS TRES REGRAS DA SECAO 8, e onde cada uma aparece aqui:
 *
 *   1. QUEM CONFERE ESCREVE A PROPRIA REGUA. Nenhuma afirmacao chama a funcao do
 *      snippet para descobrir o que esperar. Os slugs dos termos, as frases de
 *      disponibilidade, o formato do preco, os motivos de recusa e as bordas do
 *      telefone estao escritos A MAO aqui embaixo. Se o snippet e este arquivo se
 *      separarem, os dois lados nao erram juntos.
 *   2. GRADE TEM QUE INCLUIR A BORDA. A ficha e varrida em 6 bases x 2
 *      disponibilidades x 3 quantidades de foto (0, 1 e 3) x 2 estados do telefone
 *      = 72 estados, e a regua da publicacao e medida nos dois lados de cada
 *      campo que ela decide — com e sem foto, com e sem preco, prazo zero e prazo
 *      um (que e a fronteira do singular/plural).
 *   3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. Tudo que e texto
 *      visivel e medido dentro de <main>, e o `&#038;` e contado so dentro dos
 *      blocos <script>.
 *
 * E A QUARTA, que custou um render: VARREDURA RODA UM PROCESSO POR ESTADO. O
 * `static` do logotipo da casca faz o cabecalho sumir a partir do segundo render
 * no mesmo processo (cicatriz da Robometria de 11/09/2026), e a bancada mediria
 * menos do que o site serve sem acusar erro nenhum.
 *
 * O que ele NAO substitui: o `/status` com a revisao do manifest depois do Sync, e
 * a conferencia no ar. Este arquivo prova que o codigo esta certo; so o ar prova
 * que ele esta no ar.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$falhas = 0;
$feitos = 0;

function cdm_ok( $condicao, $rotulo, $medida = '' ) {
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

function cdm_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function cdm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/** Um estado da ficha, renderizado em PROCESSO PROPRIO. */
function cdm_render_peca( $raiz, $consulta ) {
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' PECA hoje ' . escapeshellarg( $consulta ) . ' 2>/dev/null',
		$saida, $codigo );
	return array( implode( "\n", $saida ), (int) $codigo );
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
do_action( 'init' );
/* AS ROTAS SO EXISTEM DEPOIS DO `rest_api_init`. Sem disparar, as afirmacoes
   sobre o endpoint de copia da secao 24 mediriam um array vazio e passariam
   dizendo que nao ha rota — portao que nunca rodou, a familia que a Robometria
   nomeou em 11/09/2026. */
do_action( 'rest_api_init' );

/* O PISO DE TAMANHO SAI DE UMA PAGINA REAL DESTA MESMA BANCADA, nunca de um
   numero escolhido a dedo.
 *
 * A primeira escrita deste teste cravou 40 KB — calibrado na F2, que carrega uma
 * ferramenta inteira — e reprovou os estados da ficha a 26 KB. O numero estava
 * errado, nao a ficha: a pagina mais magra da casca nesta bancada e /contato/,
 * com ~23 KB, e e ela que diz o que "pagina montada inteira" pesa aqui. Piso
 * inventado reprova o certo; piso derivado de uma pagina que se sabe boa mede o
 * que a regra queria — "antes de confiar num numero medido em bancada, confira
 * que a pagina medida tem o tamanho da pagina real" (secao 8). */
exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
	. ' ' . escapeshellarg( $raiz ) . ' cdm_contato 2>/dev/null', $s_ref );
$piso_de_tamanho = strlen( implode( "\n", $s_ref ) );

echo "\nVERIFICACAO DA LOJA — bloco 4d, " . date( 'd/m/Y H:i' ) . "\n";
echo str_repeat( '-', 78 ) . "\n";

/* ---------------------------------------------------------------------------
 * 1. O MODELO — o que o site registra, e o que ele NAO registra
 *
 * A regua e escrita a mao: os valores esperados sao os do despacho de 10/09 e da
 * decisao 1 do cabecalho do snippet, nunca lidos do proprio registro.
 * ------------------------------------------------------------------------- */

echo "\n1. O tipo `peca` e as duas taxonomias\n";

$args_peca = isset( $GLOBALS['__tipos_args']['peca'] ) ? $GLOBALS['__tipos_args']['peca'] : array();
cdm_ok( ! empty( $GLOBALS['__tipos']['peca'] ), 'o tipo peca e registrado' );
cdm_ok( true === ( $args_peca['public'] ?? null ), 'peca e publica (a ficha tem de ser indexavel)' );
/* O REQUISITO ESCRITO DO RAPHAEL: "eu nao quero que ela entre numa area wp-admin". */
cdm_ok( false === ( $args_peca['show_ui'] ?? null ), 'peca NAO aparece no wp-admin para ninguem (show_ui false)' );
cdm_ok( false === ( $args_peca['show_in_menu'] ?? null ), 'peca nao entra no menu do wp-admin' );
/* A DECISAO 1: sem arquivo proprio, para nao disputar /loja/ com a pagina. */
cdm_ok( false === ( $args_peca['has_archive'] ?? null ), 'peca NAO tem arquivo proprio (a pagina /loja/ e que lista)' );
cdm_ok( 'loja' === ( $args_peca['rewrite']['slug'] ?? '' ), 'a peca vive sob /loja/', $args_peca['rewrite']['slug'] ?? '(ausente)' );
cdm_ok( false === ( $args_peca['rewrite']['with_front'] ?? null ), 'sem prefixo de front na URL da peca' );
cdm_ok( array( 'peca', 'pecas' ) === ( $args_peca['capability_type'] ?? null ), 'peca tem capacidades proprias' );
cdm_ok( true === ( $args_peca['map_meta_cap'] ?? null ), 'map_meta_cap ligado (e o nucleo que decide pelo autor)' );
cdm_ok( in_array( 'thumbnail', (array) ( $args_peca['supports'] ?? array() ), true ), 'peca suporta imagem destacada' );
cdm_ok( in_array( 'author', (array) ( $args_peca['supports'] ?? array() ), true ), 'peca guarda o autor (e o que separa as peças dela das de outra pessoa)' );

/* AS TAXONOMIAS SAO PRIVADAS HOJE (decisao 4): o dado existe, a URL nao, porque
   taxonomia publica nasce com arquivo e entra no sitemap de um dominio de dois
   dias — de sete a doze URLs finas pedindo rastreamento (secao 14.1). */
foreach ( array( 'colecao', 'tecnica' ) as $tax ) {
	$a = isset( $GLOBALS['__taxonomias'][ $tax ] ) ? $GLOBALS['__taxonomias'][ $tax ] : null;
	cdm_ok( is_array( $a ), "a taxonomia $tax e registrada" );
	cdm_ok( false === ( $a['public'] ?? null ), "$tax e privada hoje (sem pagina, sem sitemap)" );
	cdm_ok( false === ( $a['rewrite'] ?? null ), "$tax nao cria URL" );
}

echo "\n2. Os termos que o formulario oferece\n";

/* A REGUA ESCRITA A MAO: as coleções sao USO (e assim que quem compra escolhe) e
   as tecnicas sao o nome que a artesa usa. Esta lista e o esperado; ela nao vem
   de `cdm_loja_termos_iniciais()`. */
$colecoes_esperadas = array( 'centro-de-mesa', 'presentes', 'jardim', 'parede', 'joias' );
$tecnicas_esperadas = array( 'direto', 'indireto', 'bizantino', 'trencadis' );

foreach ( $colecoes_esperadas as $slug ) {
	cdm_ok( isset( $GLOBALS['__termos']['colecao'][ $slug ] ), "a colecao $slug foi criada no init" );
}
foreach ( $tecnicas_esperadas as $slug ) {
	cdm_ok( isset( $GLOBALS['__termos']['tecnica'][ $slug ] ), "a tecnica $slug foi criada no init" );
}
cdm_ok( count( $GLOBALS['__termos']['colecao'] ?? array() ) === count( $colecoes_esperadas ),
	'nenhuma colecao a mais do que as declaradas',
	count( $GLOBALS['__termos']['colecao'] ?? array() ) . ' de ' . count( $colecoes_esperadas ) );
cdm_ok( count( $GLOBALS['__termos']['tecnica'] ?? array() ) === count( $tecnicas_esperadas ),
	'nenhuma tecnica a mais do que as declaradas',
	count( $GLOBALS['__termos']['tecnica'] ?? array() ) . ' de ' . count( $tecnicas_esperadas ) );

/* A REESCRITA NASCE SOZINHA — a cicatriz da F1, que nasceu 404 porque a regra nao
 * existia na base e a artesa nunca vai ao wp-admin salvar permalinks.
 *
 * A PRIMEIRA ESCRITA DESTA AFIRMACAO ERA `! empty( $GLOBALS['__reescritas'] )`, e a
 * bateria de mutacoes a furou na hora: a CASCA tambem remonta as regras quando cria
 * pagina, entao o contador ja estava acima de zero e apagar o flush da Loja passava
 * verde. Contador compartilhado nao diz QUEM contou. Agora o teste zera o contador,
 * apaga a marca que faz a Loja pular a remontagem, roda o `init` de novo — a casca
 * nao remonta na segunda passada, porque ela so remonta quando CRIA pagina — e
 * afirma sobre o delta. */
$GLOBALS['__reescritas'] = 0;
unset( $GLOBALS['__options']['cdm_loja_reescrita'] );
cdm_teste_rebobinar();
do_action( 'init' );
cdm_ok( ! empty( $GLOBALS['__reescritas'] ),
	'a Loja remonta as regras de reescrita ela mesma (a peca nao nasce 404)',
	(int) ( $GLOBALS['__reescritas'] ?? 0 ) . ' remontagens depois de limpar a marca' );
/* E A MARCA IMPEDE A REMONTAGEM A CADA VISITA: remontar regra de reescrita em toda
   requisicao e uma consulta pesada ao banco por visita. */
$GLOBALS['__reescritas'] = 0;
cdm_teste_rebobinar();
do_action( 'init' );
cdm_ok( 0 === (int) ( $GLOBALS['__reescritas'] ?? 0 ),
	'e NAO remonta de novo na visita seguinte', (int) ( $GLOBALS['__reescritas'] ?? 0 ) . ' remontagens' );

/* O TOKEN E COMPARADO EM TEMPO CONSTANTE.
 *
 * UNICA AFIRMACAO DESTE ARQUIVO QUE LE O FONTE, e a razao e a natureza da
 * propriedade: `===` e `hash_equals()` devolvem o MESMO resultado para toda
 * entrada, e o que muda e o tempo — que nenhuma bancada observa. A mutacao
 * correspondente passou verde por isso, e a escolha foi fechar a trava onde ela
 * pode existir em vez de deixar a mutacao registrada como "nao pegamos". */
$fonte_loja = file_get_contents( $raiz . '/snippets/clubedomosaico-loja.php' );
cdm_ok( false !== strpos( $fonte_loja, 'hash_equals( $esperado, $vindo )' ),
	'o token e comparado com hash_equals (tempo constante)' );
cdm_ok( false === strpos( $fonte_loja, '$esperado === $vindo' ),
	'e NAO com === (que vaza o token por tempo)' );

/* ---------------------------------------------------------------------------
 * 3. A REGUA DA PUBLICACAO — os dois lados de cada campo que ela decide
 *
 * Regua contraria escrita a mao: para cada caso, o que ESTE arquivo diz que
 * deveria faltar. Nao ha chamada a `cdm_loja_peca_publicavel()` para descobrir o
 * esperado — ela e o medido.
 * ------------------------------------------------------------------------- */

echo "\n3. Peca sem foto ou sem preco NAO publica (os dois lados de cada campo)\n";

/** Monta uma peca no banco de mentira e devolve o id. */
function cdm_por_peca( $id, $campos, $galeria, $termos, $titulo = 'Vaso azul' ) {
	$GLOBALS['__pecas_por_id'][ $id ] = (object) array(
		'ID' => $id, 'post_type' => 'peca', 'post_status' => 'draft',
		'post_title' => $titulo, 'post_name' => 'vaso-azul', 'post_content' => 'texto',
		'post_author' => 10, 'post_date_gmt' => '2026-09-12 22:00:00',
	);
	$GLOBALS['__meta'][ $id ] = $campos;
	$GLOBALS['__meta'][ $id ]['_cdm_galeria'] = $galeria;
	foreach ( $galeria as $a ) {
		$GLOBALS['__anexos'][ (int) $a ] = array( 'url' => 'https://clubedomosaico.com.br/f.jpg', 'largura' => 1200, 'altura' => 1500 );
	}
	$GLOBALS['__objeto_termos'][ $id ] = $termos;

	return $id;
}

$completa = array( '_cdm_preco' => '189.90', '_cdm_disponibilidade' => 'pronta_entrega' );
$termos_ok = array( 'colecao' => array( 'centro-de-mesa' ), 'tecnica' => array( 'direto' ) );

/* O caso bom, primeiro: sem ele nenhum dos outros significa nada. */
$id = cdm_por_peca( 201, $completa, array( 901 ), $termos_ok );
cdm_ok( array() === cdm_loja_peca_publicavel( $id ), 'peca completa e publicavel (0 motivos)',
	implode( ' | ', cdm_loja_peca_publicavel( $id ) ) );

/* Cada caso ruim tira UM campo e afirma o motivo que ESTE arquivo espera. */
$casos = array(
	'sem foto'            => array( 'campos' => $completa, 'galeria' => array(), 'termos' => $termos_ok, 'titulo' => 'Vaso azul', 'espera' => 'Falta pelo menos uma foto.' ),
	'sem preco'           => array( 'campos' => array( '_cdm_disponibilidade' => 'pronta_entrega' ), 'galeria' => array( 901 ), 'termos' => $termos_ok, 'titulo' => 'Vaso azul', 'espera' => 'Falta o preço.' ),
	'preco zero'          => array( 'campos' => array( '_cdm_preco' => '0', '_cdm_disponibilidade' => 'pronta_entrega' ), 'galeria' => array( 901 ), 'termos' => $termos_ok, 'titulo' => 'Vaso azul', 'espera' => 'Falta o preço.' ),
	'sem titulo'          => array( 'campos' => $completa, 'galeria' => array( 901 ), 'termos' => $termos_ok, 'titulo' => '   ', 'espera' => 'Falta o nome da peça.' ),
	'sem colecao'         => array( 'campos' => $completa, 'galeria' => array( 901 ), 'termos' => array( 'tecnica' => array( 'direto' ) ), 'titulo' => 'Vaso azul', 'espera' => 'Escolha uma coleção.' ),
	'sem tecnica'         => array( 'campos' => $completa, 'galeria' => array( 901 ), 'termos' => array( 'colecao' => array( 'centro-de-mesa' ) ), 'titulo' => 'Vaso azul', 'espera' => 'Escolha a técnica.' ),
	'encomenda sem prazo' => array( 'campos' => array( '_cdm_preco' => '189.90', '_cdm_disponibilidade' => 'sob_encomenda' ), 'galeria' => array( 901 ), 'termos' => $termos_ok, 'titulo' => 'Vaso azul', 'espera' => 'Peça sob encomenda precisa do prazo em dias.' ),
	'encomenda prazo 0'   => array( 'campos' => array( '_cdm_preco' => '189.90', '_cdm_disponibilidade' => 'sob_encomenda', '_cdm_prazo_dias' => '0' ), 'galeria' => array( 901 ), 'termos' => $termos_ok, 'titulo' => 'Vaso azul', 'espera' => 'Peça sob encomenda precisa do prazo em dias.' ),
);
$n = 210;
foreach ( $casos as $nome => $c ) {
	$id = cdm_por_peca( $n++, $c['campos'], $c['galeria'], $c['termos'], $c['titulo'] );
	$motivos = cdm_loja_peca_publicavel( $id );
	cdm_ok( in_array( $c['espera'], $motivos, true ), "recusa: $nome", implode( ' | ', $motivos ) );
}

/* A BORDA DO OUTRO LADO: encomenda COM prazo 1 passa, e e onde o singular do
   texto e decidido. */
$id = cdm_por_peca( 250, array( '_cdm_preco' => '189.90', '_cdm_disponibilidade' => 'sob_encomenda', '_cdm_prazo_dias' => '1' ), array( 901 ), $termos_ok );
cdm_ok( array() === cdm_loja_peca_publicavel( $id ), 'encomenda com prazo 1 e publicavel' );

/* FOTO QUE NAO E MAIS ANEXO NAO CONTA. A galeria guarda ids, e id de anexo
   apagado na biblioteca de midia e `<img>` quebrada na pagina de um produto. */
$GLOBALS['__meta'][250]['_cdm_galeria'] = array( 4242 ); // nunca virou anexo
cdm_ok( array() === cdm_loja_galeria( 250 ), 'id que nao e anexo sai da galeria' );
cdm_ok( in_array( 'Falta pelo menos uma foto.', cdm_loja_peca_publicavel( 250 ), true ),
	'peca cuja unica foto foi apagada volta a NAO ser publicavel' );

echo "\n4. As frases e os formatos, com as bordas\n";

/* REGUA A MAO: as frases esperadas, escritas aqui, no tom do VOZ.md. */
$frases = array(
	array( 'pronta_entrega', '',   'Pronta entrega, já está feita' ),
	array( 'pronta_entrega', '20', 'Pronta entrega, já está feita' ), // prazo e ignorado, e tem de ser
	array( 'sob_encomenda',  '1',  'Sob encomenda, feita em 1 dia' ),  // singular
	array( 'sob_encomenda',  '2',  'Sob encomenda, feita em 2 dias' ), // plural
	array( 'sob_encomenda',  '0',  'Sob encomenda' ),
	array( 'sob_encomenda',  '',   'Sob encomenda' ),
	array( '',               '',   '' ),
	array( 'invalido',       '5',  '' ),
);
foreach ( $frases as $f ) {
	$medido = cdm_loja_disponibilidade_frase( $f[0], $f[1] );
	cdm_ok( $f[2] === $medido, 'disponibilidade "' . $f[0] . '"/' . ( '' === $f[1] ? 'sem prazo' : $f[1] ), $medido );
}

$precos = array(
	array( '189.90', 'R$&nbsp;189,90' ),
	array( '74',     'R$&nbsp;74,00' ),
	array( '1234.5', 'R$&nbsp;1.234,50' ),
	array( '0',      '' ),
	array( '',       '' ),
);
foreach ( $precos as $p ) {
	$medido = cdm_loja_preco_html( $p[0] );
	cdm_ok( $p[1] === $medido, 'preco ' . ( '' === $p[0] ? '(vazio)' : $p[0] ), $medido );
}

/* O TELEFONE, nas quatro bordas do comprimento. Numero curto e numero errado, e
   link de WhatsApp errado na pagina de um produto manda a cliente para o vazio. */
$zaps = array(
	array( '',                '', 'vazio' ),
	array( '5511',            '', '4 digitos' ),
	array( '551198765432',    '551198765432', '12 digitos (fixo)' ),
	array( '5511987654321',   '5511987654321', '13 digitos (celular)' ),
	array( '55119876543210',  '', '14 digitos' ),
	array( '+55 (11) 98765-4321', '5511987654321', 'com pontuacao' ),
);
foreach ( $zaps as $z ) {
	$GLOBALS['__options']['cdm_whatsapp'] = $z[0];
	cdm_ok( $z[1] === cdm_loja_whatsapp(), 'telefone: ' . $z[2], cdm_loja_whatsapp() );
}
$GLOBALS['__options']['cdm_whatsapp'] = '5511987654321';

/* A MENSAGEM PRONTA: sem emoji, com quebra de linha em %0A, e com a peca citada. */
$msg = cdm_loja_mensagem_whatsapp( 'Vaso azul', 'https://clubedomosaico.com.br/loja/vaso-azul/', 'sob_encomenda', '20' );
cdm_ok( false !== strpos( $msg, '%0A' ), 'a mensagem quebra linha com %0A' );
cdm_ok( false === strpos( $msg, '%0D' ), 'sem retorno de carro na mensagem' );
cdm_ok( false !== strpos( rawurldecode( $msg ), 'Vaso azul' ), 'a mensagem cita a peca pelo nome' );
cdm_ok( false !== strpos( rawurldecode( $msg ), 'sob encomenda, feita em 20 dias' ), 'a mensagem cita a disponibilidade real' );
cdm_ok( 0 === preg_match( '/[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]/u', rawurldecode( $msg ) ), 'sem emoji na mensagem' );

/* O TITULO DE SEO, nos dois lados da coleção. */
$id = cdm_por_peca( 260, $completa, array( 901 ), $termos_ok, 'Vaso azul' );
cdm_ok( 'Vaso azul — Centro de mesa em mosaico | Clube do Mosaico' === cdm_loja_titulo_seo( $GLOBALS['__pecas_por_id'][260] ),
	'title com coleção', cdm_loja_titulo_seo( $GLOBALS['__pecas_por_id'][260] ) );
$id = cdm_por_peca( 261, $completa, array( 901 ), array( 'tecnica' => array( 'direto' ) ), 'Vaso azul' );
cdm_ok( 'Vaso azul — mosaico feito à mão | Clube do Mosaico' === cdm_loja_titulo_seo( $GLOBALS['__pecas_por_id'][261] ),
	'title sem coleção nao deixa travessao solto', cdm_loja_titulo_seo( $GLOBALS['__pecas_por_id'][261] ) );

/* A DESCRICAO: teto de 160 e corte na palavra. A borda e um titulo longo. */
$id = cdm_por_peca( 262, array_merge( $completa, array( '_cdm_medidas' => '22 × 15 × 15' ) ), array( 901 ), $termos_ok,
	'Vaso de barro grande coberto de pastilha azul cobalto com flores de caquinho branco em volta da boca' );
$d = cdm_loja_descricao( $GLOBALS['__pecas_por_id'][262] );
cdm_ok( mb_strlen( $d, 'UTF-8' ) <= 160, 'a description respeita o teto de 160', mb_strlen( $d, 'UTF-8' ) . ' caracteres' );
cdm_ok( '…' === mb_substr( $d, -1, 1, 'UTF-8' ), 'a description longa termina em reticencia' );
cdm_ok( false === strpos( $d, '  ' ), 'a description nao corta no meio de espaco duplo' );
$id = cdm_por_peca( 263, array_merge( $completa, array( '_cdm_base' => 'ceramica' ) ), array( 901 ), $termos_ok, 'Vaso azul' );
$d2 = cdm_loja_descricao( $GLOBALS['__pecas_por_id'][263] );
cdm_ok( 0 === preg_match( '/\. [a-záéíóúâêôãõç]/u', $d2 ), 'a description nao abre frase em minuscula depois de ponto', $d2 );

/* ---------------------------------------------------------------------------
 * 5. A VARREDURA DA FICHA — 72 estados, um processo por estado
 * ------------------------------------------------------------------------- */

echo "\n5. A ficha no HTML servido — 72 estados, um processo cada\n";

$bases  = array( 'ceramica', 'vidro', 'mdf', 'cimento', 'metal', 'outra' );
$disps  = array( 'pronta_entrega', 'sob_encomenda' );
$fotos  = array( 0, 1, 3 );
$zaps   = array( 0, 1 );

$estados      = 0;
$sem_desc     = array();
$sem_og       = array();
$sem_produto  = array();
$sem_trilha   = array();
$com_escape   = array();
$sem_noindex_errado = array();
$menores      = array();
$sem_alt      = array();
$sem_dim      = array();
$sem_botao    = array();
$com_botao_sem_zap = array();
$codigos      = array();
$tamanhos     = array();

foreach ( $bases as $b ) {
	foreach ( $disps as $dp ) {
		foreach ( $fotos as $nf ) {
			foreach ( $zaps as $z ) {
				$estados++;
				$consulta = 'base=' . $b . '&disp=' . $dp . '&fotos=' . $nf . '&zap=' . $z
					. ( 'sob_encomenda' === $dp ? '&prazo=20' : '' );
				list( $html, $codigo ) = cdm_render_peca( $raiz, $consulta );
				$codigos[]  = $codigo;
				$corpo      = cdm_corpo( $html );
				$tamanhos[] = strlen( $html );
				$rotulo     = $b . '/' . $dp . '/' . $nf . 'f/zap' . $z;

				if ( false === strpos( $html, '<meta name="description"' ) ) { $sem_desc[] = $rotulo; }
				if ( false === strpos( $html, 'property="og:title"' ) )      { $sem_og[] = $rotulo; }
				if ( false === strpos( $html, 'id="cdm-peca-jsonld"' ) )     { $sem_produto[] = $rotulo; }
				if ( false === strpos( $corpo, 'cdm-trilha' ) )              { $sem_trilha[] = $rotulo; }
				if ( false !== strpos( cdm_scripts( $html ), '&#038;' ) )    { $com_escape[] = $rotulo; }
				/* A FICHA DA PECA NUNCA SAI DO INDICE. E a pagina que vende. */
				if ( false !== strpos( $html, 'noindex' ) )                  { $sem_noindex_errado[] = $rotulo; }
				/* O BOTAO SAI SE E SO SE HA TELEFONE PUBLICADO. */
				$tem_botao = ( false !== strpos( $corpo, 'https://wa.me/' ) );
				if ( 1 === $z && ! $tem_botao )  { $sem_botao[] = $rotulo; }
				if ( 0 === $z && $tem_botao )    { $com_botao_sem_zap[] = $rotulo; }
				/* TODA FOTO COM alt E COM MEDIDA. */
				preg_match_all( '#<img[^>]*>#i', $corpo, $imgs );
				foreach ( $imgs[0] as $img ) {
					if ( false === strpos( $img, 'alt="' ) )    { $sem_alt[] = $rotulo; }
					if ( false === strpos( $img, 'width="' ) )  { $sem_dim[] = $rotulo; }
				}
				/* PAGINA COM TAMANHO DE PAGINA (secao 8), medido contra o piso que
				   veio de /contato/ nesta mesma bancada. */
				if ( strlen( $html ) < $piso_de_tamanho ) { $menores[] = $rotulo . ' (' . strlen( $html ) . ')'; }
			}
		}
	}
}

cdm_ok( 72 === $estados, 'a varredura cobriu 6 bases x 2 disponibilidades x 3 fotos x 2 telefones', $estados . ' estados' );
cdm_ok( array( 0 ) === array_values( array_unique( $codigos ) ), 'nenhum estado da ficha sai com erro de PHP',
	implode( ',', array_unique( $codigos ) ) );
cdm_ok( empty( $sem_desc ), 'os 72 estados servem meta description', empty( $sem_desc ) ? '72 de 72' : implode( ', ', array_slice( $sem_desc, 0, 4 ) ) );
cdm_ok( empty( $sem_og ), 'os 72 estados servem og:', empty( $sem_og ) ? '72 de 72' : implode( ', ', array_slice( $sem_og, 0, 4 ) ) );
cdm_ok( empty( $sem_produto ), 'os 72 estados servem o JSON-LD da peca', empty( $sem_produto ) ? '72 de 72' : implode( ', ', array_slice( $sem_produto, 0, 4 ) ) );
cdm_ok( empty( $sem_trilha ), 'os 72 estados servem a trilha no corpo', empty( $sem_trilha ) ? '72 de 72' : implode( ', ', array_slice( $sem_trilha, 0, 4 ) ) );
cdm_ok( empty( $com_escape ), 'zero &#038; DENTRO de <script> nos 72 estados', empty( $com_escape ) ? '0' : implode( ', ', array_slice( $com_escape, 0, 4 ) ) );
cdm_ok( empty( $sem_noindex_errado ), 'a ficha da peca NUNCA sai do indice', empty( $sem_noindex_errado ) ? '0 noindex' : implode( ', ', array_slice( $sem_noindex_errado, 0, 4 ) ) );
cdm_ok( empty( $sem_botao ), 'com telefone publicado, os 36 estados tem botao de WhatsApp', empty( $sem_botao ) ? '36 de 36' : implode( ', ', array_slice( $sem_botao, 0, 4 ) ) );
cdm_ok( empty( $com_botao_sem_zap ), 'SEM telefone publicado, nenhum estado inventa botao', empty( $com_botao_sem_zap ) ? '0 de 36' : implode( ', ', array_slice( $com_botao_sem_zap, 0, 4 ) ) );
cdm_ok( empty( $sem_alt ), 'toda foto servida tem alt', empty( $sem_alt ) ? 'todas' : implode( ', ', array_slice( $sem_alt, 0, 4 ) ) );
cdm_ok( empty( $sem_dim ), 'toda foto servida tem width e height (22.4)', empty( $sem_dim ) ? 'todas' : implode( ', ', array_slice( $sem_dim, 0, 4 ) ) );
cdm_ok( empty( $menores ), 'nenhum estado e render pela metade (piso = /contato/ desta bancada)',
	empty( $menores ) ? 'menor: ' . min( $tamanhos ) . ' bytes, piso ' . $piso_de_tamanho : implode( ', ', array_slice( $menores, 0, 3 ) ) );

echo "\n6. A ficha do caso-ancora, celula a celula\n";

list( $html, $cod ) = cdm_render_peca( $raiz, 'base=ceramica&disp=sob_encomenda&prazo=20&fotos=3&zap=1' );
$corpo = cdm_corpo( $html );

/* O JSON-LD, recomputado A MAO: preco com ponto e duas casas, moeda BRL, e
   PreOrder porque a peca e sob encomenda. */
preg_match( '#<script type="application/ld\+json" id="cdm-peca-jsonld">(.*?)</script>#s', $html, $m );
$g = json_decode( $m[1] ?? '{}', true );
$produto = $g['@graph'][0] ?? array();
cdm_ok( 'Product' === ( $produto['@type'] ?? '' ), 'o JSON-LD e um Product' );
cdm_ok( '189.90' === ( $produto['offers']['price'] ?? '' ), 'o preco do Offer sai com ponto e 2 casas', $produto['offers']['price'] ?? '(ausente)' );
cdm_ok( 'BRL' === ( $produto['offers']['priceCurrency'] ?? '' ), 'a moeda e BRL' );
cdm_ok( 'https://schema.org/PreOrder' === ( $produto['offers']['availability'] ?? '' ),
	'sob encomenda vira PreOrder', $produto['offers']['availability'] ?? '(ausente)' );
cdm_ok( 3 === count( (array) ( $produto['image'] ?? array() ) ), 'as 3 fotos entram no image do Product',
	count( (array) ( $produto['image'] ?? array() ) ) . ' fotos' );
cdm_ok( 640 === ( $produto['weight']['value'] ?? 0 ), 'o peso entra em gramas' );
cdm_ok( false !== strpos( $produto['@id'] ?? '', '/loja/vaso-azul-com-flores/' ), 'o @id da peca usa a URL sob /loja/' );

/* E O OUTRO LADO: pronta entrega vira InStock. */
list( $html2 ) = cdm_render_peca( $raiz, 'base=vidro&disp=pronta_entrega&fotos=1&zap=1' );
preg_match( '#id="cdm-peca-jsonld">(.*?)</script>#s', $html2, $m2 );
$p2 = json_decode( $m2[1] ?? '{}', true )['@graph'][0] ?? array();
cdm_ok( 'https://schema.org/InStock' === ( $p2['offers']['availability'] ?? '' ),
	'pronta entrega vira InStock', $p2['offers']['availability'] ?? '(ausente)' );

/* PECA SEM PRECO NAO PUBLICA OFERTA. `Offer` sem `price` e dado invalido, e
   invalido e ignorado: publicaria MENOS com cara de publicar mais. */
list( $html3 ) = cdm_render_peca( $raiz, 'base=mdf&disp=pronta_entrega&fotos=1&zap=1&preco=0' );
preg_match( '#id="cdm-peca-jsonld">(.*?)</script>#s', $html3, $m3 );
$p3 = json_decode( $m3[1] ?? '{}', true )['@graph'][0] ?? array();
cdm_ok( ! isset( $p3['offers'] ), 'peca sem preco NAO publica Offer (schema invalido e schema ignorado)' );
cdm_ok( 'Product' === ( $p3['@type'] ?? '' ), 'e o Product continua saindo, com o resto da ficha' );

/* A TRILHA, com os tres degraus da secao 16, e o BreadcrumbList com tres. */
preg_match( '#id="cdm-trilha-jsonld">(.*?)</script>#s', $html, $mt );
$trilha = json_decode( $mt[1] ?? '{}', true );
$itens  = $trilha['itemListElement'] ?? array();
cdm_ok( 3 === count( $itens ), 'o BreadcrumbList da peca tem 3 degraus', count( $itens ) );
cdm_ok( 'Início' === ( $itens[0]['name'] ?? '' ), 'degrau 1 e Inicio' );
cdm_ok( 'Loja' === ( $itens[1]['name'] ?? '' ), 'degrau 2 e Loja' );
cdm_ok( 'Vaso azul com flores' === ( $itens[2]['name'] ?? '' ), 'degrau 3 e a peca' );
cdm_ok( ! isset( $itens[2]['item'] ), 'o degrau atual nao leva URL (e onde a pessoa ja esta)' );
cdm_ok( 'https://clubedomosaico.com.br/loja/' === ( $itens[1]['item'] ?? '' ), 'o degrau Loja aponta para a pagina que existe' );

/* O CANONICAL e UM SO, e aponta para a URL sob /loja/. */
preg_match_all( '#<link rel="canonical" href="([^"]+)"#', $html, $mc );
cdm_ok( 1 === count( $mc[1] ), 'um canonical, nunca dois', count( $mc[1] ) . ' canonicals' );
cdm_ok( 'https://clubedomosaico.com.br/loja/vaso-azul-com-flores/' === ( $mc[1][0] ?? '' ),
	'o canonical da peca e a URL sob /loja/', $mc[1][0] ?? '(ausente)' );

/* A ORDEM DA SECAO 5: a resposta antes da explicacao. Quem abre a pagina de uma
   peca veio ver a peca — o preco tem de vir ANTES da ficha tecnica e ANTES do
   "prefere fazer a sua". Medido por POSICAO no corpo, nunca por presenca. */
$pos_preco  = strpos( $corpo, 'cdm-peca-preco' );
$pos_botao  = strpos( $corpo, 'https://wa.me/' );
$pos_ficha  = strpos( $corpo, 'A peça em números' );
$pos_guia   = strpos( $corpo, 'Prefere fazer a sua?' );
cdm_ok( false !== $pos_preco && $pos_preco < $pos_ficha, 'o preco vem antes da ficha tecnica' );
cdm_ok( false !== $pos_botao && $pos_botao < $pos_ficha, 'o botao vem antes da ficha tecnica' );
cdm_ok( $pos_ficha < $pos_guia, 'a ficha tecnica vem antes do link para o Guia' );

/* O CORPO COMECA PELO TEXTO, nunca por metadado (secao 8, item 3). */
$comeco = ltrim( preg_replace( '#<nav class="cdm-trilha".*?</nav>#s', '', $corpo ) );
cdm_ok( 0 !== strpos( $comeco, '---' ), 'o corpo nao comeca por front matter' );
cdm_ok( false === strpos( substr( $comeco, 0, 400 ), 'revisao:' ), 'o corpo nao comeca por metadado' );

/* NADA DE SCRIPT NEM STYLE DENTRO DO RETORNO DO FILTRO (secao 8). A ficha e
   montada por `the_content`, e o `<style>` dela sai no rodape. */
$ficha_crua = cdm_loja_ficha_html( cdm_teste_peca_de_mentira( array( 'fotos' => 2, 'zap' => 1 ) ) );
cdm_ok( false === stripos( $ficha_crua, '<script' ), 'a ficha nao carrega <script> (ele mataria no escape do the_content)' );
cdm_ok( false === stripos( $ficha_crua, '<style' ), 'a ficha nao carrega <style>' );
cdm_ok( false !== strpos( $html, 'id="cdm-loja-css"' ), 'a folha da Loja vem do rodape' );

/* SEM UMA LINHA DE JAVASCRIPT NA LOJA (22.8): o carrossel e scroll-snap puro. */
cdm_ok( false === strpos( $html, 'id="cdm-loja-js"' ), 'a Loja nao serve JavaScript nenhum' );
cdm_ok( false !== strpos( $html, 'scroll-snap-type' ), 'o carrossel e CSS puro (funciona com JS desligado)' );

/* TODAS AS FOTOS NO HTML SERVIDO (22.3), nunca carregadas depois. */
list( $html_3 ) = cdm_render_peca( $raiz, 'base=ceramica&disp=pronta_entrega&fotos=3&zap=1' );
preg_match_all( '#peca-([0-9])\.jpg#', cdm_corpo( $html_3 ), $mf );
cdm_ok( 3 === count( array_unique( $mf[1] ) ), 'as 3 fotos estao no HTML servido', count( array_unique( $mf[1] ) ) . ' fotos' );
/* A CAPA CARREGA PRIMEIRO e as outras sao preguicosas — orcamento da 22.4. */
cdm_ok( 1 === preg_match_all( '#fetchpriority="high"#', cdm_corpo( $html_3 ) ), 'exatamente uma foto e prioritaria (a capa)' );
cdm_ok( 2 === preg_match_all( '#loading="lazy"#', cdm_corpo( $html_3 ) ), 'as outras duas sao preguicosas' );

echo "\n7. A peca SEM foto: a ficha nao quebra e nao mente\n";

list( $html_0 ) = cdm_render_peca( $raiz, 'base=ceramica&disp=pronta_entrega&fotos=0&zap=1' );
$corpo_0 = cdm_corpo( $html_0 );
cdm_ok( false === strpos( $corpo_0, 'cdm-carrossel' ), 'sem foto, nao sai carrossel vazio' );
cdm_ok( false !== strpos( $corpo_0, 'cdm-peca-preco' ), 'sem foto, o preco continua saindo' );
preg_match( '#id="cdm-peca-jsonld">(.*?)</script>#s', $html_0, $m0 );
$p0 = json_decode( $m0[1] ?? '{}', true )['@graph'][0] ?? array();
cdm_ok( ! isset( $p0['image'] ), 'sem foto, o Product nao declara image' );
cdm_ok( false === strpos( $html_0, 'property="og:image"' ), 'sem foto, nao sai og:image apontando para nada' );

echo "\n8. O estado vazio da Loja continua sendo o da casca\n";

/* O FILTRO SUBSTITUI A VITRINE QUANDO HA PECA, e devolve o da casca quando nao
   ha. Duas versoes do estado vazio seria uma para envelhecer. */
$GLOBALS['__pecas'] = array();
cdm_ok( '' === cdm_loja_vitrine_html( 24 ), 'sem peca, a vitrine da Loja e vazia' );
cdm_ok( 'PISO' === apply_filters( 'cdm_vitrine_de_pecas', 'PISO', 24 ),
	'sem peca, o filtro devolve o piso da casca intocado' );

$GLOBALS['__pecas'] = array( cdm_teste_peca_de_mentira( array( 'fotos' => 2 ) ) );
$vitrine = cdm_loja_vitrine_html( 24 );
cdm_ok( false !== strpos( $vitrine, 'cdm-card-peca' ), 'com peca, o cartao da Loja e o com foto' );
cdm_ok( false !== strpos( $vitrine, 'aspect-ratio' ) || false !== strpos( $vitrine, 'cdm-card-foto' ),
	'o cartao serve a foto (o DESIGN.md diz que a foto manda)' );
cdm_ok( false !== strpos( $vitrine, 'R$&nbsp;189,90' ), 'o cartao serve o preco em formato brasileiro' );
cdm_ok( $vitrine === apply_filters( 'cdm_vitrine_de_pecas', 'PISO', 24 ),
	'com peca, o filtro substitui o piso da casca' );
cdm_ok( false !== strpos( $vitrine, '/loja/vaso-azul-com-flores/' ), 'o cartao aponta para a URL sob /loja/' );

echo "\n9. A copia da secao 24 — o endpoint protegido\n";

/* A PECA E O UNICO DADO DO ARQUIPELAGO QUE NAO EXISTE FORA DO BANCO DO WORDPRESS.
   A rota existe para a ronda commitar `dados/pecas.json`. */
cdm_ok( isset( $GLOBALS['__rotas']['clubedomosaico/v1/pecas'] ), 'a rota de copia das pecas e registrada' );
cdm_ok( isset( $GLOBALS['__rotas']['clubedomosaico/v1/loja'] ), 'a rota publica de contagem e registrada' );
cdm_ok( 'GET' === ( $GLOBALS['__rotas']['clubedomosaico/v1/pecas']['methods'] ?? '' ), 'a copia e somente leitura' );
cdm_ok( is_callable( $GLOBALS['__rotas']['clubedomosaico/v1/pecas']['permission_callback'] ?? null ),
	'a copia tem portao de permissao' );
/* A CONTAGEM E PUBLICA e a COPIA NAO. Quantas pecas a loja tem qualquer visitante
   conta abrindo /loja/; o que e dado dela fica atras do token. */
cdm_ok( '__return_true' === ( $GLOBALS['__rotas']['clubedomosaico/v1/loja']['permission_callback'] ?? '' ),
	'a contagem e publica (nao ha segredo em quantas pecas existem)' );

$copia = cdm_loja_copia();
cdm_ok( isset( $copia['pecas'] ) && is_array( $copia['pecas'] ), 'a copia devolve a lista de pecas' );
cdm_ok( 'clubedomosaico' === ( $copia['ilha'] ?? '' ), 'a copia se identifica pela ilha' );
$uma = $copia['pecas'][0] ?? array();
cdm_ok( isset( $uma['campos']['cdm_preco'] ), 'a copia leva os campos da peca' );
cdm_ok( isset( $uma['fotos'] ) && is_array( $uma['fotos'] ), 'a copia leva as URLs das fotos' );
cdm_ok( isset( $uma['descricao'] ), 'a copia leva a descricao (o que ela escreveu e o que mais doeria perder)' );
/* NADA DE PESSOA na copia, hoje e sempre: o CPT `lead_peca` nao existe, e no dia
   em que existir os leads NAO vao para o repositorio (adendo 3 de 11/09). */
$json_copia = wp_json_encode( $copia );
cdm_ok( false === strpos( $json_copia, 'whatsapp' ) && false === strpos( $json_copia, 'lead' ),
	'a copia nao carrega nada de pessoa (nem lead, nem telefone)' );

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s). %d estados da ficha, um processo cada.\n", $feitos, $falhas, $estados );
if ( $falhas > 0 ) {
	echo "REPROVADO.\n";
	exit( 1 );
}
echo "APROVADO.\n";

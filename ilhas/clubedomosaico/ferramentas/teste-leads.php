<?php
/**
 * Verificacao MEDIDA do snippet de Leads (adendo 3 do bloco 4d), sem site e sem
 * rede.
 *
 *   php ferramentas/teste-leads.php .
 *
 * AS REGRAS DA SECAO 8, e onde cada uma aparece aqui:
 *
 *   1. QUEM CONFERE ESCREVE A PROPRIA REGUA. A tabela de telefones da secao 2
 *      esta escrita A MAO, entrada por entrada, com o canonico esperado digitado
 *      do lado. Nenhuma afirmacao deste arquivo chama
 *      `cdm_leads_wa_canonico()` para descobrir o que esperar — se a regua do
 *      snippet mudar, esta tabela reprova em vez de concordar.
 *
 *   2. GRADE TEM QUE INCLUIR A BORDA. A tabela pisa nas quatro bordas que a
 *      regra tem: DDD 10 (invalido) e 11 (o primeiro valido), DDD 99 (o ultimo),
 *      assinante de 8 e de 9 digitos, e o 9 inicial do celular de nove. Uma
 *      grade que so testasse "(11) 98765-4321" nao separaria nenhuma delas.
 *
 *   3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. Tudo que e texto
 *      visivel e medido dentro de <main>, e `&#038;` e contado so dentro dos
 *      blocos <script>.
 *
 *   4. VARREDURA RODA UM PROCESSO POR ESTADO. Cada render de ficha e de painel
 *      sai de um `php` proprio (o `static` do logotipo da casca some a partir do
 *      segundo render no mesmo processo — cicatriz da Robometria de 11/09/2026).
 *
 * E A QUINTA, que e deste bloco: O CAMINHO DO ENVIO NAO E UMA PAGINA, E MESMO
 * ASSIM PRECISA DE ESTADO LIMPO. As recusas e o caminho feliz rodam no mesmo
 * processo de proposito — o limite de 5 por hora so significa alguma coisa se os
 * envios se somarem —, mas cada cenario zera transients, leads e e-mails antes
 * de comecar. Sem isso o caminho feliz do cenario 7 passaria porque o 6 ja
 * tinha gravado.
 *
 * O que ele NAO substitui: o `/status` com a revisao do manifest depois do Sync,
 * e a conferencia no ar.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$falhas = 0;
$feitos = 0;
$estados_medidos = 0;

function cdm_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-68s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-68s %s\n", $rotulo, $medida );
	return false;
}

function cdm_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function cdm_cabeca( $html ) {
	return preg_match( '#<head[^>]*>(.*?)</head>#is', $html, $m ) ? $m[1] : '';
}

function cdm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/** Uma ficha de peca, renderizada em PROCESSO PROPRIO. */
function cdm_ficha( $raiz, $consulta = '' ) {
	global $estados_medidos;
	$estados_medidos++;
	$cmd = 'php ' . escapeshellarg( $raiz . '/ferramentas/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' PECA hoje ' . escapeshellarg( $consulta ) . ' 2>&1';

	return (string) shell_exec( $cmd );
}

/** Uma tela do painel, em PROCESSO PROPRIO. */
function cdm_painel( $raiz, $consulta ) {
	global $estados_medidos;
	$estados_medidos++;
	$cmd = 'php ' . escapeshellarg( $raiz . '/ferramentas/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ATELIE hoje ' . escapeshellarg( $consulta ) . ' 2>&1';

	return (string) shell_exec( $cmd );
}

/**
 * Zera o mundo entre cenarios de envio, e devolve a peca de mentira servida.
 *
 * Nao e conveniencia: sem isto, o lead gravado num cenario contaria no seguinte
 * e o limite de 5 por hora seria medido contra um numero que ninguem escolheu.
 */
function cdm_cenario_limpo( $ip = '203.0.113.7' ) {
	$GLOBALS['__transients']   = array();
	$GLOBALS['__leads']        = array();
	$GLOBALS['__leads_por_id'] = array();
	$GLOBALS['__emails']       = array();
	$GLOBALS['__inserts']      = array();
	$_SERVER['REMOTE_ADDR']    = $ip;
	$_POST                     = array();
	$_GET                      = array();

	$peca = cdm_teste_peca_de_mentira( array() );
	$GLOBALS['__pecas_por_id'][ (int) $peca->ID ] = $peca;
	$GLOBALS['__pecas']         = array( $peca );
	$GLOBALS['__post_atual']    = $peca;
	$GLOBALS['__id_atual']      = (int) $peca->ID;
	$GLOBALS['__tipo_atual']    = 'peca';
	$GLOBALS['__caminho_atual'] = $peca->post_name;

	return $peca;
}

/**
 * Manda o formulario e devolve para onde o snippet redirecionou.
 *
 * O nonce e montado com a MESMA acao que o formulario declara, escrita aqui a
 * mao: `cdm_lead_<id>`. Se o snippet trocar a acao do nonce, isto reprova.
 */
function cdm_enviar( $peca, $campos = array() ) {
	$id      = (int) $peca->ID;
	$padrao  = array(
		'cdm_acao'   => 'lead',
		'cdm_peca'   => (string) $id,
		'cdm_nonce'  => wp_create_nonce( 'cdm_lead_' . $id ),
		'cdm_nome'   => 'Ana Clara',
		'cdm_zap'    => '(11) 98765-4321',
		'cdm_ok'     => '1',
		'cdm_origem' => 'https://clubedomosaico.com.br/loja/vaso-azul-com-flores/',
	);
	$_POST = array_merge( $padrao, $campos );
	foreach ( $_POST as $k => $v ) {
		if ( null === $v ) {
			unset( $_POST[ $k ] );
		}
	}
	try {
		cdm_leads_agir();
	} catch ( CdmTesteRedirecionou $e ) {
		return $e->getMessage();
	}

	return '';
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );
do_action( 'init' );

$ids_de_teste = array();
$n = 1;
foreach ( array_keys( cdm_casca_definicao_paginas() ) as $slug ) {
	$ids_de_teste[ $slug ] = $n++;
}
$GLOBALS['__options']['cdm_casca_paginas'] = $ids_de_teste;

echo "TESTE DO SNIPPET DE LEADS — adendo 3 do bloco 4d\n";
echo str_repeat( '=', 78 ) . "\n";

/* ======================================================================== */
echo "\n1. O tipo `lead_peca` — invisivel por todos os lados\n";

$args = isset( $GLOBALS['__tipos_args']['lead_peca'] ) ? $GLOBALS['__tipos_args']['lead_peca'] : array();
cdm_ok( isset( $GLOBALS['__tipos']['lead_peca'] ), 'o tipo lead_peca e registrado' );

/* CADA UM DOS CINCO E UMA PORTA DIFERENTE, e depender da implicacao de `public`
   e como o painel quase foi ao indice em 12/09: a regra que valia era outra. */
cdm_ok( false === ( $args['public'] ?? true ), 'o tipo nao e publico' );
cdm_ok( false === ( $args['publicly_queryable'] ?? true ), 'o tipo nao responde a consulta publica' );
cdm_ok( false === ( $args['show_ui'] ?? true ), 'o tipo nao aparece no wp-admin (nem para o administrador)' );
cdm_ok( false === ( $args['show_in_rest'] ?? true ), 'o tipo nao entra na API REST do nucleo' );
cdm_ok( true === ( $args['exclude_from_search'] ?? false ), 'o tipo fica fora da busca do site' );
cdm_ok( false === ( $args['has_archive'] ?? true ), 'o tipo nao tem arquivo proprio' );
cdm_ok( false === ( $args['rewrite'] ?? true ), 'o tipo nao ganha endereco publico' );
cdm_ok( false === ( $args['query_var'] ?? true ), 'o tipo nao vira parametro de consulta' );

/* NAO HA ROTA REST DE LEAD, e a ausencia e medida porque ausencia some sozinha.
   A copia da secao 24 para o lead e o CSV na mao da artesa; nome e telefone de
   pessoa nao saem por endpoint nem entram em arquivo versionado. */
$rotas_de_lead = array();
foreach ( array_keys( isset( $GLOBALS['__rotas'] ) ? $GLOBALS['__rotas'] : array() ) as $rota ) {
	if ( false !== stripos( $rota, 'lead' ) || false !== stripos( $rota, 'interessad' ) ) {
		$rotas_de_lead[] = $rota;
	}
}
cdm_ok( 0 === count( $rotas_de_lead ), 'NENHUMA rota REST serve lead', implode( ',', $rotas_de_lead ) );

/* ======================================================================== */
echo "\n2. A canonizacao do WhatsApp — regua propria, com as bordas\n";

/* A TABELA E ESCRITA A MAO. O canonico esperado esta digitado; nada aqui chama a
   funcao do snippet para saber o que esperar. */
$telefones = array(
	/* entrada                 esperado           o que a linha separa */
	array( '(11) 98765-4321',  '5511987654321',  'celular com mascara' ),
	array( '11987654321',      '5511987654321',  'celular so em digitos' ),
	array( '11 98765 4321',    '5511987654321',  'celular com espacos' ),
	array( '5511987654321',    '5511987654321',  'ja com DDI — o 55 NAO duplica' ),
	array( '+55 11 98765-4321', '5511987654321', 'DDI com o mais na frente' ),
	array( '011 98765-4321',   '5511987654321',  'o zero de operadora cai' ),
	array( '1133334444',       '551133334444',   'assinante de 8 digitos (fixo) passa' ),
	array( '55 11 3333-4444',  '551133334444',   'fixo com DDI' ),
	array( '1198765432',       '551198765432',   'BORDA: 8 digitos que comecam com 9' ),
	array( '1098765432',       '',               'BORDA: DDD 10 nao existe' ),
	array( '1198765432100',    '',               'BORDA: um digito a mais' ),
	array( '119876543',        '',               'BORDA: um digito a menos' ),
	array( '9998765432',       '559998765432',   'BORDA: DDD 99, o ultimo' ),
	array( '1188765432199',    '',               'entrada longa demais' ),
	array( '11887654321',      '',               'BORDA: 9 digitos que NAO comecam com 9' ),
	array( '11999999999',      '',               'digito repetido e teste de formulario' ),
	array( '',                 '',               'vazio' ),
	array( 'nao tenho',        '',               'texto' ),
	array( '11',               '',               'so o DDD' ),
);
foreach ( $telefones as $linha ) {
	list( $entrada, $esperado, $porque ) = $linha;
	$medido = cdm_leads_wa_canonico( $entrada );
	cdm_ok( $medido === $esperado, 'telefone: ' . $porque,
		'"' . $entrada . '" -> "' . $medido . '" (esperado "' . $esperado . '")' );
}

/* O CAMINHO DE VOLTA. Guardar e mostrar sao coisas diferentes, e as duas
   direcoes precisam fechar: se so a ida fosse medida, a artesa poderia ver na
   tela um numero que nao e o que esta gravado. */
$legiveis = array(
	array( '5511987654321', '(11) 98765-4321' ),
	array( '551133334444',  '(11) 3333-4444' ),
	array( '5599998765432', '(99) 99876-5432' ),
);
foreach ( $legiveis as $par ) {
	cdm_ok( cdm_leads_wa_legivel( $par[0] ) === $par[1], 'o canonico volta legivel: ' . $par[0],
		cdm_leads_wa_legivel( $par[0] ) );
}

cdm_ok( 'Ana' === cdm_leads_primeiro_nome( 'Ana Clara de Souza' ), 'o primeiro nome sai do nome inteiro' );
cdm_ok( 'Joao' === cdm_leads_primeiro_nome( 'Joao' ), 'nome de uma palavra devolve ele mesmo' );

/* ======================================================================== */
echo "\n3. O formulario na ficha da peca — medido no CORPO\n";

$ficha  = cdm_ficha( $raiz );
$corpo  = cdm_corpo( $ficha );
$script = cdm_scripts( $ficha );

cdm_ok( '' !== $corpo, 'a ficha renderizou com corpo', strlen( $corpo ) . ' bytes' );
cdm_ok( false !== strpos( $corpo, 'Verificar disponibilidade' ),
	'o botao principal e "Verificar disponibilidade" (adendo 3)' );
cdm_ok( false === strpos( $corpo, 'Falar com a artesa sobre esta peca' )
	&& false === strpos( $corpo, 'Falar com a artesã sobre esta peça' ),
	'o botao antigo de WhatsApp direto saiu da ficha' );
cdm_ok( false === strpos( $corpo, 'O contato ainda não foi publicado' ),
	'a ficha NAO diz mais que o contato nao foi publicado (a option cdm_whatsapp deixou de decidir isso)' );

/* O <details> e a razao de o formulario funcionar sem JavaScript (22.8). */
cdm_ok( preg_match( '#<details class="cdm-lead"#', $corpo ) === 1, 'o formulario abre por <details>, sem script' );
cdm_ok( preg_match( '#<summary[^>]*class="[^"]*cdm-botao[^"]*"#', $corpo ) === 1,
	'quem abre e um <summary>, que e do proprio HTML' );
cdm_ok( preg_match( '#<form class="cdm-lead-form" method="post"#', $corpo ) === 1, 'o envio e um <form method="post">' );
cdm_ok( preg_match( '#action="[^"]*/loja/vaso-azul-com-flores/\#cdm-quero"#', $corpo ) === 1,
	'o formulario volta para a PROPRIA peca, na ancora do bloco' );

cdm_ok( preg_match( '#name="cdm_nome"[^>]*required#', $corpo ) === 1, 'o nome e obrigatorio' );
cdm_ok( preg_match( '#name="cdm_zap"[^>]*type="tel"#', $corpo ) === 1
	|| preg_match( '#type="tel"[^>]*name="cdm_zap"#', $corpo ) === 1, 'o telefone e campo de telefone' );
cdm_ok( preg_match( '#name="cdm_zap"[^>]*required#', $corpo ) === 1, 'o telefone e obrigatorio' );
cdm_ok( preg_match( '#inputmode="tel"#', $corpo ) === 1, 'o celular abre o teclado numerico' );
cdm_ok( preg_match( '#name="cdm_ok"[^>]*required#', $corpo ) === 1, 'o consentimento e obrigatorio no proprio HTML' );
cdm_ok( preg_match( '#name="cdm_nonce" value="NONCE-#', $corpo ) === 1, 'o formulario leva nonce' );

/* SO DOIS CAMPOS VISIVEIS, que e o que o adendo pede: "Nada mais. Sem e-mail,
   sem CEP." A contagem e contada, nunca digitada — e conta os campos de texto do
   formulario, descontando os escondidos. */
preg_match( '#<form class="cdm-lead-form".*?</form>#s', $corpo, $mf );
$form_html = isset( $mf[0] ) ? $mf[0] : '';
preg_match_all( '#<input[^>]*type="(text|tel|email|number)"[^>]*>#', $form_html, $mi );
$visiveis = 0;
foreach ( $mi[0] as $campo ) {
	if ( false === strpos( $campo, 'tabindex="-1"' ) ) {
		$visiveis++;
	}
}
cdm_ok( 2 === $visiveis, 'o formulario pede DOIS campos e mais nada', $visiveis . ' campo(s) de digitar' );
cdm_ok( false === stripos( $form_html, 'name="cdm_email"' ) && false === stripos( $form_html, 'name="cdm_cpf"' ),
	'nao pede e-mail nem CPF' );

/* O HONEYPOT esta fora da vista E fora do caminho do teclado. Um dos dois
   sozinho nao basta: escondido sem tabindex pega o foco de quem navega por Tab, e
   fora do tab sem esconder aparece na tela. */
cdm_ok( preg_match( '#name="cdm_cep"[^>]*tabindex="-1"#', $form_html ) === 1, 'o honeypot esta fora do caminho do teclado' );
cdm_ok( preg_match( '#class="cdm-lead-hp" aria-hidden="true"#', $form_html ) === 1, 'o honeypot esta fora do leitor de tela' );
cdm_ok( false !== strpos( $ficha, '.cdm-lead-hp{position:absolute;left:-9999px' ), 'o honeypot esta fora da vista' );

/* O TEXTO DO CONSENTIMENTO, palavra por palavra, escrito A MAO aqui. */
$consentimento = 'Ao enviar, você autoriza o Clube do Mosaico a entrar em contato pelo WhatsApp sobre esta peça. '
	. 'Seus dados são usados só para esse atendimento e não são repassados a terceiros.';
cdm_ok( false !== strpos( $corpo, htmlspecialchars( $consentimento, ENT_QUOTES ) )
	|| false !== strpos( $corpo, $consentimento ),
	'o texto do consentimento e o do adendo, palavra por palavra' );
cdm_ok( false !== strpos( $form_html, 'Política de privacidade' ), 'o consentimento linka a politica de privacidade' );

/* A LINHA DE BAIXO CONTINUA SENDO A DA LOJA: a promessa antes do formulario
   (secao 6 do contrato) nao podia sumir com a troca do botao. */
cdm_ok( false !== strpos( $corpo, 'Você fala direto com quem fez' ), 'a promessa antes do formulario continua de pe' );

/* A CICATRIZ DE 08/09/2026: zero `&#038;` DENTRO dos <script>. Contado so ali. */
cdm_ok( false === strpos( $script, '&#038;' ), 'zero &#038; dentro dos <script>' );
cdm_ok( false !== strpos( $ficha, 'id="cdm-leads-mascara"' ), 'a mascara do telefone esta no rodape, nao no shortcode' );
cdm_ok( false === strpos( $corpo, '<script' ), 'nenhum <script> dentro do corpo' );

/* ======================================================================== */
echo "\n4. O filtro que a Loja aplica — os DOIS lados, porque um so nao prova nada\n";

/* Lado A: alguem atende o filtro. Lado B: o que ele devolve e o que a ficha
   serve. A cicatriz de 12/09 nesta ilha foi um `add_filter` sem ninguem do outro
   lado — medir so o lado A repetiria o defeito com outro nome. */
$peca_filtro = cdm_teste_peca_de_mentira( array() );
$GLOBALS['__pecas_por_id'][ (int) $peca_filtro->ID ] = $peca_filtro;
$atendido = apply_filters( 'cdm_peca_acao', 'PISO', $peca_filtro, array(
	'titulo' => $peca_filtro->post_title,
	'url'    => get_permalink( $peca_filtro ),
	'disp'   => 'pronta_entrega',
	'prazo'  => '',
	'preco'  => '189.90',
) );
cdm_ok( 'PISO' !== $atendido, 'o filtro cdm_peca_acao TEM quem o atenda' );
cdm_ok( false !== strpos( $atendido, 'Verificar disponibilidade' ), 'quem atende devolve o formulario' );
cdm_ok( false !== strpos( $corpo, 'Verificar disponibilidade' ),
	'e a ficha servida no ar contem o que ele devolve (o filtro e APLICADO, nao so declarado)' );

/* ======================================================================== */
echo "\n5. O envio — as recusas e o caminho feliz\n";

/* Cada cenario comeca do zero (ver o cabecalho deste arquivo). */

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_nonce' => 'NONCE-INVENTADO' ) );
cdm_ok( false !== strpos( $destino, 'cdm_lead_erro=nonce' ), 'sem nonce valido, recusa' );
cdm_ok( 0 === count( $GLOBALS['__leads'] ), 'sem nonce valido, NADA e gravado' );

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_cep' => 'preenchido por robo' ) );
cdm_ok( false === strpos( $destino, 'cdm_lead_erro' ), 'o honeypot sai em SILENCIO (sem ensinar o robo)' );
cdm_ok( 0 === count( $GLOBALS['__leads'] ), 'o honeypot nao grava nada' );
cdm_ok( 0 === count( $GLOBALS['__emails'] ), 'o honeypot nao manda e-mail' );

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_ok' => null ) );
cdm_ok( false !== strpos( $destino, 'cdm_lead_erro=ok' ), 'sem consentimento, recusa' );
cdm_ok( 0 === count( $GLOBALS['__leads'] ), 'sem consentimento, nada e gravado' );

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_nome' => ' ' ) );
cdm_ok( false !== strpos( $destino, 'cdm_lead_erro=nome' ), 'sem nome, recusa' );

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_zap' => '1234' ) );
cdm_ok( false !== strpos( $destino, 'cdm_lead_erro=zap' ), 'com telefone invalido, recusa' );
cdm_ok( 0 === count( $GLOBALS['__leads'] ), 'telefone invalido nao vira lead' );

$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_peca' => '999999' ) );
cdm_ok( false !== strpos( $destino, 'cdm_lead_erro=peca' ), 'com a peca trocada no formulario, recusa' );

/* --- O CAMINHO FELIZ --- */
$peca = cdm_cenario_limpo();
$destino = cdm_enviar( $peca, array( 'cdm_nome' => '  Ana   Clara  ', 'cdm_zap' => '(11) 98765-4321' ) );
cdm_ok( 1 === count( $GLOBALS['__leads'] ), 'o envio valido grava UM lead', count( $GLOBALS['__leads'] ) . '' );
cdm_ok( preg_match( '#\?cdm_lead=[A-Za-z0-9]{12,40}\#cdm-quero$#', $destino ) === 1,
	'volta para a peca com uma CHAVE, nao com o nome', $destino );
cdm_ok( false === stripos( $destino, 'ana' ), 'o NOME da pessoa nao viaja na URL (decisao 4)' );
cdm_ok( false === stripos( $destino, '98765' ), 'o TELEFONE nao viaja na URL' );

$lead_id = (int) $GLOBALS['__leads'][0]->ID;
cdm_ok( 'Ana Clara' === get_post_meta( $lead_id, '_cdm_nome', true ),
	'o nome e gravado limpo, com os espacos de sobra fora', get_post_meta( $lead_id, '_cdm_nome', true ) );
cdm_ok( '5511987654321' === get_post_meta( $lead_id, '_cdm_whatsapp', true ),
	'o telefone e gravado CANONICO (nao do jeito que foi digitado)' );
cdm_ok( (int) $peca->ID === (int) get_post_meta( $lead_id, '_cdm_peca_id', true ), 'o lead sabe de qual peca e' );
cdm_ok( 'novo' === get_post_meta( $lead_id, '_cdm_status', true ), 'o lead nasce no estado novo' );

$consent = get_post_meta( $lead_id, '_cdm_consentimento', true );
cdm_ok( is_array( $consent ) && ! empty( $consent['em'] ) && ! empty( $consent['texto'] ),
	'o consentimento e gravado com carimbo de hora E o texto exibido (LGPD)' );
cdm_ok( is_array( $consent ) && $consent['texto'] === $consentimento,
	'o texto gravado e o MESMO que a tela mostrou' );

/* O TITULO DO POST NAO LEVA O NOME. */
cdm_ok( false === stripos( (string) $GLOBALS['__leads'][0]->post_title, 'ana' ),
	'o titulo do registro nao carrega o nome da pessoa', (string) $GLOBALS['__leads'][0]->post_title );

/* --- A CONFIRMACAO --- */
preg_match( '#\?cdm_lead=([A-Za-z0-9]+)#', $destino, $mc );
$chave = isset( $mc[1] ) ? $mc[1] : '';
$_GET  = array( 'cdm_lead' => $chave );
$conf  = cdm_leads_confirmacao( (int) $peca->ID );
cdm_ok( is_array( $conf ) && 'Ana Clara' === $conf['nome'], 'a chave devolve a confirmacao desta peca' );
cdm_ok( null === cdm_leads_confirmacao( 99999 ), 'a MESMA chave nao vira "enviado" na ficha de outra peca' );
$_GET = array( 'cdm_lead' => 'chaveinventadaqualquer' );
cdm_ok( null === cdm_leads_confirmacao( (int) $peca->ID ), 'chave inventada nao fabrica a tela de enviado' );

/* A VALIDADE E MEDIDA, senao os 10 minutos sao um numero que ninguem cobra. */
$_GET = array( 'cdm_lead' => $chave );
cdm_teste_envelhecer_transients( 601 );
cdm_ok( null === cdm_leads_confirmacao( (int) $peca->ID ), 'a confirmacao expira depois de 10 minutos' );
$_GET = array();

/* --- O LIMITE DE 5 POR HORA --- */
$peca = cdm_cenario_limpo( '198.51.100.4' );
$recusou_em = 0;
for ( $i = 1; $i <= 7; $i++ ) {
	$d = cdm_enviar( $peca, array( 'cdm_nome' => 'Pessoa ' . $i ) );
	if ( false !== strpos( $d, 'cdm_lead_erro=limite' ) && 0 === $recusou_em ) {
		$recusou_em = $i;
	}
}
cdm_ok( 6 === $recusou_em, 'o 6o envio da mesma origem e recusado (o teto e 5)', 'recusou no ' . $recusou_em . 'o' );
cdm_ok( 5 === count( $GLOBALS['__leads'] ), 'exatamente 5 leads gravados', count( $GLOBALS['__leads'] ) . '' );

/* O ENDERECO NAO E GUARDADO EM TEXTO PURO, nem na chave do balde.
   Esta linha nasceu de uma mutacao que PASSOU: o portao media que o limite
   funcionava e nao media COM O QUE ele o fazia — e o adendo e explicito ("nunca
   gravar IP em texto puro alem do necessario para o limite (hash)"). Dado de
   pessoa guardado sem ninguem perceber e o que ninguem consegue apagar depois. */
$chaves_do_balde = implode( ' ', array_keys( $GLOBALS['__transients'] ) );
cdm_ok( false === strpos( $chaves_do_balde, '198.51.100.4' ),
	'o endereco de quem enviou NAO aparece em texto puro no balde do limite' );
cdm_ok( preg_match( '#cdm_lead_lim_[a-f0-9]{32}#', $chaves_do_balde ) === 1,
	'o balde e indexado por uma impressao de 32 caracteres, nao pelo endereco' );

/* OUTRA ORIGEM NAO HERDA O BALDE — o limite e por endereco, e se fosse global um
   robo calaria o site inteiro para todo mundo. */
$GLOBALS['__leads']     = array();
$_SERVER['REMOTE_ADDR'] = '198.51.100.99';
$d = cdm_enviar( $peca, array( 'cdm_nome' => 'Outra pessoa' ) );
cdm_ok( false === strpos( $d, 'cdm_lead_erro=limite' ), 'outro endereco comeca com o balde vazio' );

/* E A JANELA ACABA. */
$peca = cdm_cenario_limpo( '198.51.100.5' );
for ( $i = 1; $i <= 5; $i++ ) {
	cdm_enviar( $peca, array( 'cdm_nome' => 'Pessoa ' . $i ) );
}
cdm_teste_envelhecer_transients( 3601 );
$d = cdm_enviar( $peca, array( 'cdm_nome' => 'Uma hora depois' ) );
cdm_ok( false === strpos( $d, 'cdm_lead_erro=limite' ), 'passada uma hora, o balde zera' );

/* ======================================================================== */
echo "\n6. O e-mail para a artesa\n";

$peca = cdm_cenario_limpo();
cdm_enviar( $peca, array( 'cdm_nome' => 'Ana Clara', 'cdm_zap' => '(11) 98765-4321' ) );
cdm_ok( 1 === count( $GLOBALS['__emails'] ), 'um lead manda UM e-mail', count( $GLOBALS['__emails'] ) . '' );

$email = $GLOBALS['__emails'][0];
cdm_ok( 'mina196@hotmail.com' === $email['para'], 'vai para a caixa da artesa', $email['para'] );
cdm_ok( 'Novo interessado: Vaso azul com flores — Ana Clara' === $email['assunto'],
	'o assunto e o do adendo, com a peca e o nome', $email['assunto'] );

$cab = implode( "\n", (array) $email['cabecalho'] );
cdm_ok( false !== strpos( $cab, 'From: Clube do Mosaico <contato@clubedomosaico.com.br>' ), 'o From e o do adendo' );
cdm_ok( false !== strpos( $cab, 'text/html' ), 'o e-mail sai em HTML' );
cdm_ok( false === stripos( $cab, 'Reply-To:' ), 'sem Reply-To (responder ao e-mail nao fala com ninguem)' );

$corpo_email = (string) $email['corpo'];
cdm_ok( false !== strpos( $corpo_email, 'Ana Clara' ), 'o e-mail traz o nome do cliente' );
cdm_ok( false !== strpos( $corpo_email, '(11) 98765-4321' ), 'o e-mail traz o telefone LEGIVEL, nao o canonico cru' );
cdm_ok( false !== strpos( $corpo_email, 'Vaso azul com flores' ), 'o e-mail traz o nome da peca' );
cdm_ok( false !== strpos( $corpo_email, 'R$ 189,90' ), 'o e-mail traz o preco de hoje da peca' );
cdm_ok( false !== strpos( $corpo_email, 'Pronta entrega' ), 'o e-mail traz a disponibilidade de hoje' );
cdm_ok( false !== strpos( $corpo_email, 'logo-clube-do-mosaico.png' ), 'o e-mail traz o logo' );
cdm_ok( preg_match( '#<img src="https://clubedomosaico.com.br/wp-content/uploads/vaso-1-full.jpg"#', $corpo_email ) === 1
	|| preg_match( '#<img [^>]*alt="Vaso azul com flores"#', $corpo_email ) === 1,
	'o e-mail traz a foto principal da peca' );
cdm_ok( false !== strpos( $corpo_email, 'Responder no WhatsApp' ), 'o botao grande e "Responder no WhatsApp"' );
cdm_ok( false !== strpos( $corpo_email, 'Ver a peça no site' ), 'o segundo botao e "Ver a peça no site"' );
cdm_ok( false !== strpos( $corpo_email, 'Este e-mail foi enviado pelo Clube do Mosaico porque um cliente pediu para verificar disponibilidade.' ),
	'o rodape e o do adendo, palavra por palavra' );

/* O LINK DE RESPOSTA APONTA PARA O CLIENTE, nunca para a artesa. Esse e o defeito
   que passaria despercebido: um `wa.me` com o numero errado abre uma conversa
   dela com ela mesma, e o e-mail continua parecendo certo. */
preg_match( '#href="(https://wa\.me/[^"]+)"#', $corpo_email, $mw );
$link_wa = isset( $mw[1] ) ? html_entity_decode( $mw[1], ENT_QUOTES ) : '';
cdm_ok( 0 === strpos( $link_wa, 'https://wa.me/5511987654321?text=' ),
	'o wa.me e o do CLIENTE, com a mensagem pronta', substr( $link_wa, 0, 46 ) );

/* A MENSAGEM PRONTA, decodificada e conferida frase a frase — regua escrita aqui. */
$texto_wa = rawurldecode( substr( $link_wa, strpos( $link_wa, '?text=' ) + 6 ) );
cdm_ok( 0 === strpos( $texto_wa, 'Olá, Ana! ' ), 'a mensagem chama pelo PRIMEIRO nome', substr( $texto_wa, 0, 24 ) );
cdm_ok( false !== strpos( $texto_wa, 'Aqui é do Clube do Mosaico' ),
	'sem o nome da artesa DECLARADO, a mensagem usa a casa' );
/* E NUNCA O TEXTO DE ESPERA. Esta linha e a que pegou o defeito: o Ateliê grava
   `first_name` = "Artesã" na criacao da usuaria, e a primeira versao desta
   funcao lia dali — a mensagem sairia "Aqui é Artesã" para uma cliente. */
cdm_ok( false === strpos( $texto_wa, 'Aqui é Artesã' ) && false === strpos( $texto_wa, 'Aqui é artesa' ),
	'a mensagem NUNCA usa o texto de espera do painel como se fosse nome' );

/* PRODUZ O MUNDO: com o nome declarado, ele entra. Sem esta metade, a linha
   acima passaria tambem numa funcao que devolvesse '' para sempre. */
$GLOBALS['__options']['cdm_artesa_nome'] = 'Mina';
cdm_ok( false !== strpos( rawurldecode( cdm_leads_mensagem_para_cliente( 'Ana Clara', 'Vaso azul', 'pronta_entrega', '', 'http://x' ) ), 'Aqui é Mina —' ),
	'com o nome DECLARADO na option, a mensagem passa a assinar com ele' );
unset( $GLOBALS['__options']['cdm_artesa_nome'] );
cdm_ok( false !== strpos( $texto_wa, '*Vaso azul com flores*' ), 'a peca e citada pelo nome, em negrito de WhatsApp' );
cdm_ok( false !== strpos( $texto_wa, 'Ela está pronta, já feita.' ), 'a disponibilidade real entra na mensagem' );
cdm_ok( false !== strpos( $texto_wa, 'Posso te passar os detalhes de pagamento e envio?' ), 'a pergunta do adendo esta la' );
cdm_ok( false !== strpos( $texto_wa, "\n" ), 'a quebra de linha e %0A, como o playbook manda' );
cdm_ok( false === strpos( $link_wa, '%0D' ), 'sem retorno de carro do Windows na mensagem' );

/* A DISPONIBILIDADE MUDA A FRASE, e a frase sem dado NAO SAI. Tres estados, e o
   terceiro e o que impede a mensagem de inventar. */
cdm_ok( 'Ela está pronta, já feita.' === cdm_leads_frase_disponibilidade( 'pronta_entrega', '' ), 'frase: pronta entrega' );
cdm_ok( 'Ela é feita sob encomenda, em 7 dias.' === cdm_leads_frase_disponibilidade( 'sob_encomenda', '7' ), 'frase: encomenda de 7 dias' );
cdm_ok( 'Ela é feita sob encomenda, em 1 dia.' === cdm_leads_frase_disponibilidade( 'sob_encomenda', '1' ), 'BORDA: 1 dia no singular' );
cdm_ok( 'Ela é feita sob encomenda.' === cdm_leads_frase_disponibilidade( 'sob_encomenda', '0' ), 'encomenda sem prazo nao inventa prazo' );
cdm_ok( '' === cdm_leads_frase_disponibilidade( '', '' ), 'sem disponibilidade gravada, a frase NAO sai' );

/* O RAPHAEL NAO RECEBE COPIA, a nao ser que a option exista (adendo, "Quem recebe"). */
$peca = cdm_cenario_limpo();
cdm_enviar( $peca );
cdm_ok( 1 === count( $GLOBALS['__emails'] ), 'sem a option de copia, um e-mail so' );
$GLOBALS['__options']['cdm_email_leads_copia'] = 'raphaeh9@gmail.com';
$peca = cdm_cenario_limpo();
cdm_enviar( $peca );
cdm_ok( 2 === count( $GLOBALS['__emails'] ), 'com a option de copia preenchida, dois' );
unset( $GLOBALS['__options']['cdm_email_leads_copia'] );

/* O E-MAIL QUE FALHA NAO DERRUBA O LEAD. A aba Interessados existe exatamente
   para o dia em que a Hotmail recusar a mensagem. */
$peca = cdm_cenario_limpo();
$GLOBALS['__email_falha'] = true;
cdm_enviar( $peca );
cdm_ok( 1 === count( $GLOBALS['__leads'] ), 'e-mail que falha NAO impede o lead de ser gravado' );
cdm_ok( 'falhou' === get_post_meta( (int) $GLOBALS['__leads'][0]->ID, '_cdm_email_enviado', true ),
	'e a falha fica registrada no proprio lead' );
unset( $GLOBALS['__email_falha'] );

/* ======================================================================== */
echo "\n7. A aba Interessados — vazia e cheia, cada uma em processo proprio\n";

$vazia = cdm_painel( $raiz, 'quem_sou=artesa&estado=interessados' );
$cv    = cdm_corpo( $vazia );
cdm_ok( false !== strpos( $cv, 'Ninguém pediu ainda' ), 'a aba vazia tem estado vazio honesto' );
cdm_ok( false !== strpos( $cv, 'Verificar disponibilidade' ),
	'e explica o que faz o nome aparecer ali' );
cdm_ok( false === strpos( $cv, 'Baixar em CSV' ), 'sem lead nenhum, nao ha o que baixar' );

$cheia = cdm_painel( $raiz, 'quem_sou=artesa&estado=interessados&com_leads=3' );
$cc    = cdm_corpo( $cheia );
cdm_ok( false !== strpos( $cc, 'Ana Clara' ), 'a aba cheia lista o nome' );
cdm_ok( false !== strpos( $cc, '(11) 98765-4321' ), 'a aba cheia lista o telefone legivel' );
cdm_ok( false !== strpos( $cc, '(21) 3456-7890' ), 'BORDA: o fixo de 8 digitos tambem sai legivel' );
cdm_ok( false !== strpos( $cc, '(31) 99988-7766' ), 'BORDA: quem digitou com DDI sai igual aos outros' );
cdm_ok( false !== strpos( $cc, 'Vaso azul com flores' ), 'cada linha diz de qual peca e' );
cdm_ok( substr_count( $cc, 'Responder no WhatsApp' ) === 3, 'cada interessado tem o proprio botao de responder',
	substr_count( $cc, 'Responder no WhatsApp' ) . ' botao(oes)' );

/* A CONTAGEM E CONTADA, NUNCA DIGITADA — a cicatriz dos cartoes da casca desta
   ilha, que diziam "0" com cinco rejuntes no banco. Tres leads, um deles novo. */
cdm_ok( false !== strpos( $cc, '3 pessoas perguntaram' ), 'a contagem bate com o banco', '3' );
cdm_ok( false !== strpos( $cc, '1 sem resposta' ), 'e separa quem ainda nao foi respondido' );

cdm_ok( false !== strpos( $cc, 'Baixar em CSV' ), 'a copia da secao 24 esta na tela dela' );
cdm_ok( preg_match( '#<select[^>]*name="cdm_status"#', $cc ) === 1, 'o estado do lead e editavel' );
cdm_ok( substr_count( $cc, 'value="contatado"' ) === 3, 'os quatro estados aparecem em cada linha' );
cdm_ok( preg_match( '#<option value="contatado" selected#', $cc ) === 1,
	'o estado guardado vem marcado (o segundo lead esta em contatado)' );

/* AS ABAS. "Minhas peças" primeiro, "Interessados" depois — a ordem e do adendo. */
cdm_ok( preg_match( '#<nav class="cdm-at-abas"#', $cc ) === 1, 'o painel tem navegacao entre abas' );
/* A ORDEM SE MEDE DENTRO DO <nav>, e nao na pagina inteira. A primeira versao
   desta linha varria o corpo todo e reprovava com a ordem CERTA: "Interessados"
   tambem e o <h2> da tela, que vem acima da navegacao. E a mesma familia do
   "afirmacao sobre o que a pagina diz se mede no CORPO" — aqui, uma casa
   adentro: afirmacao sobre a NAVEGACAO se mede dentro dela. */
preg_match( '#<nav class="cdm-at-abas".*?</nav>#s', $cc, $mn );
$nav       = isset( $mn[0] ) ? $mn[0] : '';
$pos_pecas = strpos( $nav, 'Minhas peças' );
$pos_inter = strpos( $nav, 'Interessados' );
cdm_ok( false !== $pos_pecas && false !== $pos_inter && $pos_pecas < $pos_inter,
	'"Minhas peças" vem antes de "Interessados" (ordem do adendo)' );
cdm_ok( 2 === substr_count( $nav, '<li' ), 'a navegacao tem DUAS abas e mais nada', substr_count( $nav, '<li' ) . '' );
cdm_ok( preg_match( '#aria-current="page">Interessados<#', $cc ) === 1, 'a aba aberta se declara para o leitor de tela' );

$lista = cdm_painel( $raiz, 'quem_sou=artesa&com_peca=1' );
cdm_ok( false !== strpos( cdm_corpo( $lista ), 'Interessados' ), 'a aba aparece TAMBEM na lista de pecas' );

/* QUEM NAO E DA CASA NAO VE A ABA. */
$estranha = cdm_painel( $raiz, 'quem_sou=estranha&estado=interessados&com_leads=3' );
$ce       = cdm_corpo( $estranha );
cdm_ok( false === strpos( $ce, 'Ana Clara' ), 'pessoa logada sem edit_pecas NAO ve nome de interessado' );
cdm_ok( false === strpos( $ce, '98765-4321' ), 'nem telefone' );

$fora = cdm_painel( $raiz, 'estado=interessados&com_leads=3' );
$cf   = cdm_corpo( $fora );
cdm_ok( false === strpos( $cf, 'Ana Clara' ), 'deslogada NAO ve nome de interessado' );
cdm_ok( false !== strpos( $cf, 'Entrar no meu ateliê' ), 'deslogada ve a tela de entrar' );

/* O PAINEL CONTINUA FORA DO INDICE — a aba nova nao podia furar isso. */
cdm_ok( false !== strpos( cdm_cabeca( $cheia ), 'noindex' ), 'a aba herda o noindex do painel' );

/* --- AS DUAS ACOES DA ABA, medidas dentro do processo ---
 *
 * As duas linhas abaixo nasceram de mutacoes que PASSARAM: o portao media a
 * TELA da aba e nunca as acoes dela. Tela e acao falham por motivos diferentes —
 * e a acao e o lado que grava. */
$GLOBALS['__transients'] = array();
$peca_aba = cdm_cenario_limpo();
cdm_enviar( $peca_aba );
$lead_da_aba = (int) $GLOBALS['__leads'][0]->ID;
/* A pagina atual passa a ser o PAINEL, e isso e mais do que trocar o caminho: o
   `__post_atual` continuava sendo a peca, e `cdm_casca_slug_atual()` le dali —
   entao `cdm_atelie_e_minha_pagina()` respondia nao e a acao voltava sem fazer
   nada. O teste mediria "a artesa nao muda o estado" achando que media a
   capacidade, quando media o endereco. */
$GLOBALS['__caminho_atual'] = 'atelie';
$GLOBALS['__tipo_atual']    = 'page';
$GLOBALS['__post_atual']    = (object) array(
	'ID' => 42, 'post_type' => 'page', 'post_name' => 'atelie',
	'post_status' => 'publish', 'post_title' => 'Ateliê', 'post_content' => '',
);
$GLOBALS['__id_atual']      = 42;

/* (a) QUEM NAO PODE EDITAR PECA NAO MUDA O ESTADO DE UM LEAD, nem com nonce
       valido no bolso: nonce protege do site de fora, capacidade protege da
       pessoa errada logada, e so as duas juntas protegem das duas coisas. */
cdm_teste_logar( 'subscriber', 11, 'outra' );
$_POST = array(
	'cdm_acao'   => 'lead_status',
	'cdm_lead'   => (string) $lead_da_aba,
	'cdm_nonce'  => wp_create_nonce( 'cdm_lead_status_' . $lead_da_aba ),
	'cdm_status' => 'vendido',
);
try {
	cdm_leads_agir_painel();
} catch ( CdmTesteRedirecionou $e ) {
	/* redirecionar e o comportamento certo; o que importa e o que NAO gravou */
}
cdm_ok( 'novo' === get_post_meta( $lead_da_aba, '_cdm_status', true ),
	'pessoa logada SEM edit_pecas nao muda o estado de um lead',
	get_post_meta( $lead_da_aba, '_cdm_status', true ) );

/* (b) E A ARTESA MUDA. Sem esta metade, a de cima passaria numa acao que nunca
       grava nada — a mutacao que produz o mundo, do lado do portao. */
cdm_teste_logar( 'artesa' );
$_POST = array(
	'cdm_acao'   => 'lead_status',
	'cdm_lead'   => (string) $lead_da_aba,
	'cdm_nonce'  => wp_create_nonce( 'cdm_lead_status_' . $lead_da_aba ),
	'cdm_status' => 'vendido',
);
try {
	cdm_leads_agir_painel();
} catch ( CdmTesteRedirecionou $e ) {
	/* idem */
}
cdm_ok( 'vendido' === get_post_meta( $lead_da_aba, '_cdm_status', true ),
	'a artesa muda o estado', get_post_meta( $lead_da_aba, '_cdm_status', true ) );

/* (c) ESTADO INVENTADO NAO ENTRA. */
$_POST['cdm_status'] = 'inventado';
$_POST['cdm_nonce']  = wp_create_nonce( 'cdm_lead_status_' . $lead_da_aba );
try {
	cdm_leads_agir_painel();
} catch ( CdmTesteRedirecionou $e ) {
	/* idem */
}
cdm_ok( 'vendido' === get_post_meta( $lead_da_aba, '_cdm_status', true ),
	'um estado que nao existe na lista nao e gravado' );
$_POST = array();

/* (d) SO ESTADO REGISTRADO COMO ABA E DESPACHADO.
       Esta tambem nasceu de uma mutacao que passou, e pelo motivo mais util: a
       mutacao abria `?estado=qualquer-coisa` ao despacho e NADA mudava, porque
       hoje ninguem responde por um estado que nao registrou. Medi-la exige
       PRODUZIR quem responde — um atendente intrometido, registrado aqui — e ai
       a diferenca aparece: com a regra, o painel devolve a lista; sem ela,
       devolve a tela do intrometido. */
add_filter( 'cdm_atelie_tela', function ( $html, $estado, $usuaria ) {
	return ( 'estado-que-ninguem-registrou' === $estado ) ? '<p>TELA DO INTROMETIDO</p>' : $html;
}, 10, 3 );
cdm_teste_logar( 'artesa' );
$GLOBALS['__pecas'] = array();
$_GET = array( 'estado' => 'estado-que-ninguem-registrou' );
$tela_estranha = call_user_func( $GLOBALS['__shortcodes']['cdm_atelie'] );
cdm_ok( false === strpos( $tela_estranha, 'TELA DO INTROMETIDO' ),
	'estado que ninguem REGISTROU como aba nao e despachado' );
cdm_ok( false !== strpos( $tela_estranha, 'Nova peça' ), 'e o painel cai na lista de pecas, como se nada tivesse sido pedido' );
$_GET = array( 'estado' => 'interessados' );
cdm_ok( false !== strpos( call_user_func( $GLOBALS['__shortcodes']['cdm_atelie'] ), 'Interessados' ),
	'e o estado REGISTRADO continua sendo despachado (a regra nao fechou a porta certa)' );
$_GET = array();

/* ======================================================================== */
echo "\n8. O CSV — a copia da secao 24 para o lead\n";

$linhas_csv = array(
	array(
		'id' => 1, 'nome' => 'Ana; Clara', 'whatsapp' => '5511987654321',
		'legivel' => '(11) 98765-4321', 'peca' => 'Vaso "azul"', 'peca_id' => 300,
		'peca_url' => 'https://clubedomosaico.com.br/loja/vaso-azul-com-flores/',
		'status' => 'novo', 'quando' => '2026-09-13 11:20:00',
		'origem' => 'https://clubedomosaico.com.br/loja/vaso-azul-com-flores/', 'responder' => '',
	),
);
$csv = cdm_leads_csv( $linhas_csv );

cdm_ok( 0 === strpos( $csv, "\xEF\xBB\xBF" ), 'o CSV comeca com BOM (senao o Excel come o acento do nome dela)' );
cdm_ok( false !== strpos( $csv, "quando;nome;whatsapp;peca;status;origem\r\n" ), 'o cabecalho e o esperado' );
cdm_ok( false !== strpos( $csv, '"Ana; Clara"' ), 'o ponto-e-virgula DENTRO do campo nao quebra a coluna' );
cdm_ok( false !== strpos( $csv, '"Vaso ""azul"""' ), 'a aspa dentro do campo e duplicada, como manda o formato' );
cdm_ok( false !== strpos( $csv, '"(11) 98765-4321"' ), 'o telefone sai legivel, para ela poder ligar do celular' );
cdm_ok( false !== strpos( $csv, '"Novo"' ), 'o estado sai no rotulo de gente, nao na chave do codigo' );
cdm_ok( 2 === substr_count( $csv, "\r\n" ), 'uma linha de cabecalho e uma de dado', substr_count( $csv, "\r\n" ) . '' );
cdm_ok( false === strpos( $csv, ',' . '"' ), 'a virgula NAO e o separador (o Excel em portugues a le como decimal)' );

/* ======================================================================== */
echo "\n9. O estado com parametro fica fora do indice\n";

$com_erro = cdm_ficha( $raiz, 'cdm_lead_erro=zap' );
$cabeca_e = cdm_cabeca( $com_erro );
cdm_ok( false !== strpos( $cabeca_e, 'noindex, follow' ), 'a ficha com ?cdm_lead_erro sai noindex' );
cdm_ok( false !== strpos( cdm_corpo( $com_erro ), 'Esse número não parece um WhatsApp com DDD' ),
	'e diz, em portugues, o que faltou' );
cdm_ok( preg_match( '#<details class="cdm-lead" open>#', cdm_corpo( $com_erro ) ) === 1,
	'com erro, o formulario ja abre (nao faz a pessoa clicar de novo para saber)' );

$limpa = cdm_cabeca( cdm_ficha( $raiz ) );
cdm_ok( false === strpos( $limpa, 'noindex' ), 'a ficha LIMPA continua indexavel (o noindex nao vazou)' );

/* ======================================================================== */
echo "\n10. A copia das pecas continua sem nada de pessoa\n";

/* A regra vale nos dois sentidos, e este e o sentido que some sozinho: o
   endpoint das pecas existe desde 12/09 e passou a conviver com um tipo que
   guarda nome e telefone. Nada impede, em codigo, que um bloco futuro os junte. */
$copia = cdm_loja_copia();
$json  = wp_json_encode( $copia );
cdm_ok( false === stripos( $json, 'whatsapp' ), 'a copia das pecas nao carrega telefone' );
cdm_ok( false === stripos( $json, 'lead' ), 'a copia das pecas nao carrega lead' );
cdm_ok( false === stripos( $json, 'consentimento' ), 'a copia das pecas nao carrega consentimento' );

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s). %d estados de pagina, um processo cada.\n", $feitos, $falhas, $estados_medidos );
if ( $falhas > 0 ) {
	echo "REPROVADO.\n";
	exit( 1 );
}
echo "APROVADO.\n";

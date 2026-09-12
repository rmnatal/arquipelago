<?php
/**
 * Verificacao MEDIDA do painel da artesa (bloco 4d), sem site e sem rede.
 *
 *   php ferramentas/teste-atelie.php .
 *
 * ESTE ARQUIVO EXISTE PORQUE O PORTAO DO DESPACHO NAO PODE SER CUMPRIDO PELA
 * FUNDACAO, e isso precisa estar escrito e nao subentendido.
 *
 * O despacho do Raphael de 12/09/2026 manda, antes de dar por pronto: "entre em
 * /atelie/ como `artesa`, numa janela de 360 px, cadastre uma peca de teste com 3
 * fotos, publique, abra a pagina publica, volte, pause e apague". A senha da
 * artesa NAO EXISTE em lugar nenhum a que a Fundacao tenha acesso — por desenho:
 * o snippet gera uma senha aleatoria, descarta sem imprimir, e o que chega a ela
 * e um link por e-mail na caixa dela. Nao ha como a nuvem entrar como `artesa`, e
 * fabricar um jeito (gravar a senha, criar um segundo acesso) seria quebrar a
 * unica coisa que protege a conta de uma pessoa de verdade.
 *
 * Entao o portao se divide em duas metades, e as duas ficam escritas:
 *
 *   A METADE QUE ESTE ARQUIVO MEDE — todo o caminho de dentro do painel, com uma
 *   pessoa logada de mentira que tem as capacidades que o SNIPPET criou: as tres
 *   telas, o formulario, o salvar, o publicar, o pausar, o apagar, as fotos, o
 *   nonce, o bloqueio do wp-admin, e cada recusa com a frase que ela le. Sao
 *   requisicoes de verdade contra o codigo de verdade.
 *
 *   A METADE QUE SO UM HUMANO MEDE — abrir no telefone dela, tocar com o dedo,
 *   fotografar, e a chegada do e-mail na caixa da Hotmail. Essa fica no relatorio
 *   como o que falta, nomeada, nunca como "conferido".
 *
 * As tres regras da secao 8 valem aqui como em todo portao desta ilha: a regua e
 * escrita a mao (as frases esperadas estao neste arquivo, nao lidas de
 * `cdm_atelie_avisos()`), a grade pisa nas bordas (deslogada, logada, logada sem
 * capacidade, nonce certo e errado, peca propria e peca de outra), e a varredura
 * das telas roda UM PROCESSO POR ESTADO.
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

/** Uma tela do painel, renderizada em PROCESSO PROPRIO. */
function cdm_render_atelie( $raiz, $consulta ) {
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ATELIE hoje ' . escapeshellarg( $consulta ) . ' 2>/dev/null',
		$saida, $codigo );
	return array( implode( "\n", $saida ), (int) $codigo );
}

/**
 * Roda uma acao do painel e devolve para onde ela redirecionou.
 *
 * No site toda acao termina em `wp_safe_redirect()` + `exit`; na bancada o
 * redirecionamento e uma excecao que carrega o destino (ver render-para-teste).
 * Quem nao redireciona devolve ''.
 */
function cdm_acao( $post, $get = array() ) {
	$_POST = $post;
	$_GET  = $get;
	try {
		cdm_atelie_agir();
	} catch ( CdmTesteRedirecionou $e ) {
		return $e->destino;
	}
	return '';
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
do_action( 'init' );
do_action( 'rest_api_init' );

/* A bancada tem de saber que pagina esta sendo servida para o painel se
   reconhecer — `cdm_atelie_e_minha_pagina()` le o caminho atual. */
$GLOBALS['__caminho_atual'] = 'atelie';
$GLOBALS['__tipo_atual']    = 'page';

echo "\nVERIFICACAO DO ATELIE — bloco 4d, " . date( 'd/m/Y H:i' ) . "\n";
echo str_repeat( '-', 78 ) . "\n";

/* ---------------------------------------------------------------------------
 * 1. O PAPEL — e sobretudo a capacidade que ele NAO tem
 * ------------------------------------------------------------------------- */

echo "\n1. O papel artesa, e a capacidade que falta de proposito\n";

$papel = get_role( 'artesa' );
cdm_ok( null !== $papel, 'o papel artesa e criado no init' );

/* A REGUA ESCRITA A MAO: exatamente estas capacidades, e nenhuma outra. */
$esperadas = array(
	'read', 'upload_files', 'edit_pecas', 'publish_pecas', 'delete_pecas',
	'edit_published_pecas', 'delete_published_pecas',
);
$tem = $papel ? array_keys( array_filter( (array) $papel->capabilities ) ) : array();
sort( $tem );
$ord = $esperadas;
sort( $ord );
cdm_ok( $ord === $tem, 'a artesa tem exatamente as 7 capacidades declaradas', implode( ', ', $tem ) );

/* A AUSENCIA MAIS IMPORTANTE DO ARQUIVO. Sem `edit_others_pecas` o nucleo recusa,
   por `map_meta_cap`, que ela toque na peca de outra pessoa — sem uma linha de
   verificacao nossa no meio do caminho. */
cdm_ok( empty( $papel->capabilities['edit_others_pecas'] ), 'a artesa NAO pode editar peca de outra pessoa' );
cdm_ok( empty( $papel->capabilities['delete_others_pecas'] ), 'a artesa NAO pode apagar peca de outra pessoa' );
/* E O QUE ELA NAO PODE DE JEITO NENHUM: mexer no site. */
foreach ( array( 'manage_options', 'edit_posts', 'edit_pages', 'edit_theme_options', 'install_plugins', 'list_users' ) as $proibida ) {
	cdm_ok( empty( $papel->capabilities[ $proibida ] ), "a artesa NAO tem $proibida" );
}
/* E UPLOAD ELA TEM, porque sem isso ela nao consegue por foto — e sem foto a peca
   nao publica. As duas metades da mesma regra. */
cdm_ok( ! empty( $papel->capabilities['upload_files'] ), 'a artesa PODE enviar foto (sem isso nada publica)' );

/* O ADMINISTRADOR GANHA AS CAPACIDADES DE `peca`. Com `capability_type` proprio
   ele nao as recebe sozinho, e sem elas o Raphael nao consegue socorrer nada no
   domingo sem uma conversa sobre SQL. */
$admin = get_role( 'administrator' );
cdm_ok( null !== $admin && ! empty( $admin->capabilities['edit_others_pecas'] ),
	'o administrador recebe edit_others_pecas' );

echo "\n2. A usuaria e o e-mail de acesso — o item que tinha de sair mais cedo\n";

$u = cdm_atelie_usuaria();
cdm_ok( false !== $u && null !== $u, 'a usuaria da artesa e criada no init' );
cdm_ok( 'artesa' === ( $u->user_login ?? '' ), 'o login dela e artesa', $u->user_login ?? '' );
cdm_ok( 'mina196@hotmail.com' === ( $u->user_email ?? '' ), 'o e-mail e o dela, dado pelo Raphael em 11/09' );
cdm_ok( in_array( 'artesa', (array) ( $u->roles ?? array() ), true ), 'ela nasce com o papel artesa' );

/* O E-MAIL SAIU, e e isto que o despacho manda escrever no ESTADO.md. */
$emails = $GLOBALS['__emails'] ?? array();
$para_ela = array();
$para_ele = array();
foreach ( $emails as $e ) {
	if ( 'mina196@hotmail.com' === $e['para'] ) { $para_ela[] = $e; }
	if ( 'raphaeh9@gmail.com' === $e['para'] ) { $para_ele[] = $e; }
}
cdm_ok( 1 === count( $para_ela ), 'exatamente UM e-mail para a artesa (Hotmail pune repeticao)', count( $para_ela ) );
cdm_ok( 1 === count( $para_ele ), 'exatamente UM aviso para o Raphael', count( $para_ele ) );

$corpo_dela = $para_ela[0]['corpo'] ?? '';
cdm_ok( false !== strpos( $para_ela[0]['assunto'] ?? '', 'ateliê' ), 'o assunto fala do ateliê dela', $para_ela[0]['assunto'] ?? '' );
cdm_ok( false !== strpos( $corpo_dela, 'Criar minha senha e entrar' ), 'o e-mail tem o botao unico do despacho' );
cdm_ok( 1 === preg_match_all( '#<a [^>]*href="[^"]*criar-senha=#', $corpo_dela ),
	'UM botao de criar senha, nunca dois', preg_match_all( '#criar-senha=#', $corpo_dela ) . ' links de senha' );
cdm_ok( false !== strpos( $corpo_dela, 'logo-clube-do-mosaico.png' ), 'o e-mail leva o logo dela' );
cdm_ok( false !== strpos( $corpo_dela, 'clubedomosaico.com.br/atelie/' ), 'o e-mail diz o endereco do painel, para guardar' );
cdm_ok( false === stripos( $corpo_dela, 'wp-admin' ), 'o e-mail NAO menciona wp-admin' );
cdm_ok( false === stripos( $corpo_dela, 'wp-login' ), 'o e-mail NAO manda para o wp-login (decisao 3)' );
cdm_ok( false !== strpos( $corpo_dela, 'Content-Type' ) || in_array( 'Content-Type: text/html; charset=UTF-8', (array) ( $para_ela[0]['cabecalho'] ?? array() ), true ),
	'o e-mail sai como HTML' );
cdm_ok( false !== strpos( implode( ' ', (array) $para_ela[0]['cabecalho'] ), 'contato@clubedomosaico.com.br' ),
	'o remetente e contato@ do proprio dominio (SPF/DKIM da hospedagem)' );

/* O AVISO DO RAPHAEL NAO LEVA O LINK — exigencia escrita do despacho de 11/09. */
$corpo_dele = $para_ele[0]['corpo'] ?? '';
cdm_ok( false === strpos( $corpo_dele, 'criar-senha=' ), 'o aviso para o Raphael NAO carrega o link de senha' );
cdm_ok( false !== strpos( $corpo_dele, 'mina196@hotmail.com' ), 'o aviso diz para onde o acesso foi' );

/* NENHUMA SENHA EM LUGAR NENHUM — E A VARREDURA E DE TODAS AS OPTIONS.
 *
 * A primeira escrita desta afirmacao olhava dois lugares: os e-mails e a option
 * `cdm_atelie_acesso`. A bateria de mutacoes furou isso na hora — a mutacao que
 * guarda a senha gravou numa TERCEIRA option e passou verde. Regua que nomeia
 * onde procurar so acha o vazamento que ja tinha imaginado. Agora ela varre todas
 * as options gravadas e todos os e-mails enviados, que e a superficie inteira por
 * onde algo pode sair deste snippet.
 *
 * O `wp_generate_password` da bancada devolve 'xxx...' de proposito, para a senha
 * gerada ter uma assinatura que esta varredura consegue reconhecer. */
$tudo_que_saiu = wp_json_encode( $emails ) . wp_json_encode( $GLOBALS['__options'] ?? array() );
cdm_ok( false === strpos( $tudo_que_saiu, str_repeat( 'x', 24 ) ),
	'a senha aleatoria NAO aparece em NENHUM e-mail nem em NENHUMA option' );
cdm_ok( false === stripos( $tudo_que_saiu, 'user_pass' ), 'nenhum campo de senha vaza no relato' );
/* E NENHUMA OPTION COM CARA DE SENHA foi criada. As duas direcoes: a de cima
   procura o valor, esta procura o lugar. */
$suspeitas = array();
foreach ( array_keys( (array) ( $GLOBALS['__options'] ?? array() ) ) as $chave ) {
	if ( preg_match( '/senha|pass/i', $chave ) ) { $suspeitas[] = $chave; }
}
cdm_ok( empty( $suspeitas ), 'nenhuma option com nome de senha foi criada',
	empty( $suspeitas ) ? count( (array) ( $GLOBALS['__options'] ?? array() ) ) . ' options' : implode( ', ', $suspeitas ) );

/* O RELATO GRAVADO — e por ele que a Fundacao confere da nuvem, pela rota REST. */
$acesso = get_option( 'cdm_atelie_acesso' );
cdm_ok( is_array( $acesso ), 'o relato do acesso e gravado em option' );
cdm_ok( ! empty( $acesso['criada'] ), 'o relato diz que a usuaria foi criada' );
cdm_ok( ! empty( $acesso['enviado'] ), 'o relato diz que o e-mail saiu' );
cdm_ok( '' === ( $acesso['erro'] ?? 'x' ), 'o relato nao carrega erro', $acesso['erro'] ?? '' );
cdm_ok( 1 === (int) ( $acesso['tentativas'] ?? 0 ), 'primeira tentativa contada', (int) ( $acesso['tentativas'] ?? 0 ) );
cdm_ok( preg_match( '#^\d{4}-\d{2}-\d{2}T#', (string) ( $acesso['quando'] ?? '' ) ) === 1,
	'o relato guarda a hora em UTC (e o que o ESTADO.md tem de dizer)', $acesso['quando'] ?? '' );

/* NAO REENVIA. Rodar o init de novo nao pode mandar um segundo e-mail: e-mail
   repetido para a Hotmail e o caminho mais curto para a caixa de spam, e caixa de
   spam aqui e uma pessoa esperando na frente do filho sem conseguir entrar. */
$antes = count( $GLOBALS['__emails'] );
cdm_teste_rebobinar();
do_action( 'init' );
cdm_ok( $antes === count( $GLOBALS['__emails'] ), 'o segundo init NAO reenvia o acesso',
	count( $GLOBALS['__emails'] ) . ' e-mails no total' );

/* E O MASCARAMENTO da rota de conferencia: "o e-mail saiu" e o que se confere; o
   endereco inteiro num log de rotina e dado de pessoa a solta. */
cdm_ok( 'mi*****@hotmail.com' === cdm_atelie_email_mascarado( 'mina196@hotmail.com' ),
	'o e-mail sai mascarado na rota', cdm_atelie_email_mascarado( 'mina196@hotmail.com' ) );
cdm_ok( '***' === cdm_atelie_email_mascarado( 'lixo' ), 'endereco sem arroba nao vaza nada' );

cdm_ok( isset( $GLOBALS['__rotas']['clubedomosaico/v1/atelie'] ), 'a rota de conferencia do acesso existe' );
cdm_ok( is_callable( $GLOBALS['__rotas']['clubedomosaico/v1/atelie']['permission_callback'] ?? null ),
	'a rota de conferencia e protegida por token (o estado do acesso de alguem nao e publico)' );
cdm_ok( '__return_true' !== ( $GLOBALS['__rotas']['clubedomosaico/v1/atelie']['permission_callback'] ?? '' ),
	'a rota de conferencia NAO e publica' );

/* O QUE A ROTA RESPONDE DE FATO, e nao so que ela existe.
 *
 * A bateria de mutacoes furou a versao anterior desta secao: ela afirmava que
 * `cdm_atelie_email_mascarado()` funciona, e nunca que a ROTA a usa. A mutacao que
 * trocou a chamada pela constante crua passou verde — funcao certa, chamada que
 * ninguem conferia. Agora o teste CHAMA a rota e afirma sobre o que sai dela. */
$resposta = call_user_func( $GLOBALS['__rotas']['clubedomosaico/v1/atelie']['callback'] );
cdm_ok( is_array( $resposta ), 'a rota devolve um relato' );
cdm_ok( false === strpos( wp_json_encode( $resposta ), 'mina196' ),
	'a rota NAO devolve o e-mail inteiro dela', $resposta['email'] ?? '' );
cdm_ok( false !== strpos( (string) ( $resposta['email'] ?? '' ), '*' ),
	'o e-mail sai mascarado NA RESPOSTA DA ROTA', $resposta['email'] ?? '' );
cdm_ok( ! empty( $resposta['papel_existe'] ), 'a rota confirma que o papel existe' );
cdm_ok( ! empty( $resposta['usuaria_existe'] ), 'a rota confirma que a usuaria existe' );
cdm_ok( ! empty( $resposta['acesso']['enviado'] ), 'a rota confirma que o e-mail saiu' );
cdm_ok( false === strpos( wp_json_encode( $resposta ), 'CHAVE-DE-TESTE' ),
	'a rota NAO devolve a chave de redefinicao' );
cdm_ok( false === strpos( wp_json_encode( $resposta ), str_repeat( 'x', 24 ) ),
	'a rota NAO devolve senha' );

echo "\n2b. O bloqueio duplo do wp-admin\n";

/* AS DUAS MUTACOES QUE PASSARAM NA PRIMEIRA BATERIA ESTAVAM AQUI, e a razao e a
 * mesma nas duas: o portao media o painel e nunca media o que acontece FORA dele.
 * O bloqueio do wp-admin nao aparece em nenhuma tela — e um `admin_init` que
 * redireciona e um filtro que esconde a barra —, entao nenhuma afirmacao sobre
 * HTML podia ve-lo. Quem mede acao tem de DISPARAR a acao. */

/** Dispara um gancho e devolve para onde ele redirecionou, ou ''. */
function cdm_disparar( $gancho ) {
	try {
		do_action( $gancho );
	} catch ( CdmTesteRedirecionou $e ) {
		return $e->destino;
	}
	return '';
}

cdm_teste_logar( 'artesa', 10, 'artesa' );
cdm_ok( cdm_atelie_url() === cdm_disparar( 'admin_init' ),
	'a artesa que tenta o wp-admin e devolvida para /atelie/', cdm_disparar( 'admin_init' ) );
cdm_ok( false === apply_filters( 'show_admin_bar', true ),
	'a barra do WordPress fica escondida para a artesa' );

/* O OUTRO LADO DA BORDA: o administrador NAO e expulso do wp-admin, e continua
   com a barra. Sem esta metade, um bloqueio que expulsasse todo mundo passaria. */
cdm_teste_logar( 'administrator', 12, 'mosaico_gestor' );
cdm_ok( '' === cdm_disparar( 'admin_init' ), 'o administrador NAO e expulso do wp-admin' );
cdm_ok( true === apply_filters( 'show_admin_bar', true ), 'o administrador mantem a barra' );

/* E QUEM NAO ENTROU nao e redirecionado para nada — `admin_init` sem sessao e o
   proprio wp-admin mandando a pessoa para o login, e nao e nosso o caminho. */
cdm_teste_deslogar();
cdm_ok( '' === cdm_disparar( 'admin_init' ), 'sem sessao, o painel nao se mete no caminho' );

/* E O DESTINO DEPOIS DE ENTRAR e o painel, nunca o wp-admin. */
cdm_teste_logar( 'artesa', 10, 'artesa' );
cdm_ok( cdm_atelie_url() === apply_filters( 'login_redirect', '/wp-admin/', '', wp_get_current_user() ),
	'depois de entrar, a artesa vai para o painel e nunca ao wp-admin' );
cdm_teste_logar( 'administrator', 12, 'mosaico_gestor' );
cdm_ok( '/wp-admin/' === apply_filters( 'login_redirect', '/wp-admin/', '', wp_get_current_user() ),
	'o administrador continua indo para onde ia' );

/* ---------------------------------------------------------------------------
 * 2. AS TELAS — varredura, um processo por estado
 * ------------------------------------------------------------------------- */

echo "\n3. As telas no HTML servido\n";

$telas = array(
	'deslogada'         => 'quem_sou=deslogada',
	'artesa sem peca'   => 'quem_sou=artesa',
	'artesa com peca'   => 'quem_sou=artesa&com_peca=1&fotos=2&zap=1',
	'artesa rascunho'   => 'quem_sou=artesa&com_peca=1&fotos=2&estado_peca=draft',
	'formulario novo'   => 'quem_sou=artesa&estado=nova',
	'formulario editar' => 'quem_sou=artesa&com_peca=1&fotos=2&estado=editar&peca=777',
	'criar senha'       => 'criar-senha=CHAVE-DE-TESTE&quem=artesa',
	'chave gasta'       => 'criar-senha=CHAVE-VELHA&quem=artesa',
	'logada sem acesso' => 'quem_sou=estranha',
);

$html_por_tela = array();
foreach ( $telas as $nome => $consulta ) {
	list( $h, $cod ) = cdm_render_atelie( $raiz, $consulta );
	$html_por_tela[ $nome ] = $h;
	cdm_ok( 0 === $cod && '' !== $h, "a tela '$nome' monta sem erro de PHP", strlen( $h ) . ' bytes' );
}

/* O PAINEL NAO ENTRA NO INDICE, em nenhum estado. E a afirmacao mais importante
   deste arquivo: e a area de uma pessoa. */
$indexaveis = array();
foreach ( $html_por_tela as $nome => $h ) {
	if ( false === strpos( $h, 'content="noindex, follow"' ) ) { $indexaveis[] = $nome; }
}
cdm_ok( empty( $indexaveis ), 'TODAS as telas do painel saem com noindex',
	empty( $indexaveis ) ? count( $html_por_tela ) . ' de ' . count( $html_por_tela ) : implode( ', ', $indexaveis ) );

/* E NENHUMA TELA VAZA NADA PARA QUEM NAO ENTROU. */
$corpo_deslogada = cdm_corpo( $html_por_tela['deslogada'] );
cdm_ok( false !== strpos( $corpo_deslogada, 'Entrar no meu ateliê' ), 'deslogada ve a tela de entrar' );
cdm_ok( false !== strpos( $corpo_deslogada, 'name="cdm_senha"' ), 'a tela de entrar tem campo de senha' );
cdm_ok( false !== strpos( $corpo_deslogada, 'Esqueci minha senha' ), 'a tela de entrar oferece recuperar a senha' );
cdm_ok( false === strpos( $corpo_deslogada, 'Nova peça' ), 'deslogada NAO ve o botao de nova peca' );
cdm_ok( false === strpos( $corpo_deslogada, 'Vaso azul' ), 'deslogada NAO ve peca nenhuma' );
cdm_ok( false === stripos( $corpo_deslogada, 'wp-admin' ), 'a tela de entrar nao fala de wp-admin' );

/* A PALAVRA "WORDPRESS" NAO APARECE EM TELA NENHUMA DO PAINEL. E o portao literal
   do despacho: "se qualquer passo exigir saber o que e WordPress, nao esta
   pronto". Medido no CORPO, em todas as telas. */
$fala_wp = array();
foreach ( $html_por_tela as $nome => $h ) {
	$c = cdm_corpo( $h );
	foreach ( array( 'wordpress', 'wp-admin', 'wp-login', 'rascunho pendente', 'custom post type', 'dashboard', 'painel de controle' ) as $palavra ) {
		if ( false !== stripos( $c, $palavra ) ) { $fala_wp[] = $nome . ': ' . $palavra; }
	}
}
cdm_ok( empty( $fala_wp ), 'nenhuma tela do painel diz WordPress, wp-admin ou wp-login',
	empty( $fala_wp ) ? count( $html_por_tela ) . ' telas limpas' : implode( ' | ', $fala_wp ) );

echo "\n4. A lista das pecas dela\n";

$corpo_lista = cdm_corpo( $html_por_tela['artesa com peca'] );
cdm_ok( false !== strpos( $corpo_lista, 'Olá, Mina' ), 'a lista abre com o nome dela' );
cdm_ok( false !== strpos( $corpo_lista, '+ Nova peça' ), 'o botao grande Nova peca esta la' );
cdm_ok( false !== strpos( $corpo_lista, 'Vaso azul com flores' ), 'a peca dela aparece na lista' );
cdm_ok( false !== strpos( $corpo_lista, 'No site' ), 'a peca publicada e etiquetada "No site"' );
cdm_ok( false !== strpos( $corpo_lista, 'Tirar do site' ), 'a peca publicada oferece pausar' );
cdm_ok( false !== strpos( $corpo_lista, 'Ver no site' ), 'a peca publicada oferece abrir a pagina publica' );
cdm_ok( false !== strpos( $corpo_lista, 'R$&nbsp;189,90' ), 'a lista mostra o preco em formato brasileiro' );
cdm_ok( false !== strpos( $corpo_lista, 'Sair' ), 'a lista tem saida' );

$corpo_rascunho = cdm_corpo( $html_por_tela['artesa rascunho'] );
cdm_ok( false !== strpos( $corpo_rascunho, 'Rascunho' ), 'a peca em rascunho e etiquetada Rascunho' );
cdm_ok( false !== strpos( $corpo_rascunho, 'value="publicar"' ), 'o rascunho oferece publicar' );
cdm_ok( false === strpos( $corpo_rascunho, 'Tirar do site' ), 'o rascunho NAO oferece tirar do site' );

$corpo_vazia = cdm_corpo( $html_por_tela['artesa sem peca'] );
cdm_ok( false !== strpos( $corpo_vazia, 'Nenhuma peça ainda' ), 'sem peca, a lista diz isso e ensina o primeiro passo' );
cdm_ok( false !== strpos( $corpo_vazia, 'Nova peça' ), 'sem peca, o botao continua sendo o caminho' );

/* TODA ACAO QUE MUDA O SITE E POST COM NONCE, nunca link — link e seguido por
   qualquer robo que passar, e "Apagar" atras de um GET e peca perdida. */
cdm_ok( 0 === preg_match( '#<a [^>]*href="[^"]*cdm_acao=(publicar|pausar|excluir)#', $corpo_lista ),
	'publicar, pausar e apagar NAO sao links GET' );
cdm_ok( 1 === preg_match( '#<form[^>]*method="post"#', $corpo_lista ), 'as acoes saem em formulario POST' );
cdm_ok( false !== strpos( $corpo_lista, 'name="cdm_nonce"' ), 'o formulario da peca carrega nonce' );

echo "\n5. O formulario, uma tela so\n";

$corpo_form = cdm_corpo( $html_por_tela['formulario novo'] );

/* OS CAMPOS QUE O DESPACHO CORTOU PARA HOJE, item 4: titulo, descricao, fotos,
   preco, disponibilidade + prazo, medidas, base, tecnica, colecao. A lista e
   escrita a mao aqui. */
$campos_do_despacho = array(
	'cdm_titulo'               => 'nome da peca',
	'fotos[]'                  => 'fotos',
	'cdm_descricao'            => 'descricao',
	'cdm_cdm_preco'            => 'preco',
	'cdm_cdm_disponibilidade'  => 'pronta entrega ou sob encomenda',
	'cdm_cdm_prazo_dias'       => 'prazo',
	'cdm_cdm_medidas'          => 'medidas',
	'cdm_cdm_peso_g'           => 'peso',
	'cdm_cdm_base'             => 'base',
	'cdm_colecao'              => 'colecao',
	'cdm_tecnica'              => 'tecnica',
);
foreach ( $campos_do_despacho as $campo => $oque ) {
	cdm_ok( false !== strpos( $corpo_form, 'name="' . $campo . '"' ), "o formulario tem o campo de $oque" );
}

cdm_ok( false !== strpos( $corpo_form, 'enctype="multipart/form-data"' ), 'o formulario aceita arquivo' );
cdm_ok( false !== strpos( $corpo_form, 'multiple' ), 'ela pode escolher varias fotos de uma vez' );
cdm_ok( false !== strpos( $corpo_form, 'accept="image/*"' ), 'o campo de foto abre camera e galeria no celular' );
cdm_ok( false !== strpos( $corpo_form, 'Salvar e terminar depois' ), 'ha como salvar sem publicar' );
cdm_ok( false !== strpos( $corpo_form, 'Publicar no site' ), 'ha como publicar' );
cdm_ok( 1 === preg_match_all( '#<form[^>]*class="cdm-at-form cdm-at-form-peca"#', $corpo_form ),
	'UM formulario de peca, uma tela so' );
/* TODO CAMPO COM RÓTULO LIGADO, que e o que faz o toque no celular funcionar. */
preg_match_all( '#<label for="([^"]+)"#', $corpo_form, $labels );
$sem_campo = array();
foreach ( $labels[1] as $alvo ) {
	if ( false === strpos( $corpo_form, 'id="' . $alvo . '"' ) ) { $sem_campo[] = $alvo; }
}
cdm_ok( empty( $sem_campo ), 'todo rotulo aponta para um campo que existe',
	empty( $sem_campo ) ? count( $labels[1] ) . ' rotulos' : implode( ', ', $sem_campo ) );
/* TODO CAMPO COM AJUDA CURTA, exigencia escrita do despacho de 10/09. */
cdm_ok( preg_match_all( '#class="cdm-at-ajuda"#', $corpo_form ) >= count( $campos_do_despacho ) - 2,
	'quase todo campo tem uma linha de ajuda', preg_match_all( '#class="cdm-at-ajuda"#', $corpo_form ) . ' ajudas' );
/* O TECLADO CERTO NO CELULAR: numero sem recusar a virgula do preco. */
cdm_ok( false !== strpos( $corpo_form, 'inputmode="decimal"' ), 'o preco abre teclado de numero e aceita virgula' );
cdm_ok( false !== strpos( $corpo_form, 'inputmode="numeric"' ), 'peso e prazo abrem teclado de numero' );
cdm_ok( false === strpos( $corpo_form, 'type="number"' ),
	'nenhum campo e type=number (recusaria 180,50, que e como se escreve preco em portugues)' );

/* O FORMULARIO DE EDITAR TRAZ O QUE ELA JA TINHA ESCRITO. */
$corpo_edit = cdm_corpo( $html_por_tela['formulario editar'] );
cdm_ok( false !== strpos( $corpo_edit, 'value="Vaso azul com flores"' ), 'editar traz o nome preenchido' );
cdm_ok( false !== strpos( $corpo_edit, 'value="189.90"' ), 'editar traz o preco preenchido' );
cdm_ok( false !== strpos( $corpo_edit, 'Um vaso de barro' ), 'editar traz a descricao preenchida' );
cdm_ok( false !== strpos( $corpo_edit, 'Fotos desta peça' ), 'editar mostra as fotos que ja estao na peca' );
cdm_ok( false !== strpos( $corpo_edit, 'Capa' ), 'a primeira foto e marcada como capa' );
cdm_ok( false !== strpos( $corpo_edit, 'value="foto_remover"' ), 'ha como remover uma foto' );
cdm_ok( false !== strpos( $corpo_edit, 'value="foto_frente"' ), 'ha como mover foto para frente' );
cdm_ok( false !== strpos( $corpo_edit, 'value="foto_tras"' ), 'ha como mover foto para tras' );
/* A DIRECAO SAI NO `value` DO BOTAO, nunca num campo escondido. A primeira escrita
   punha `<input type="hidden" name="cdm_direcao">` no mesmo formulario — e campo
   escondido e enviado seja qual for o botao apertado, entao o ▶ mandava "para
   tras" junto e a foto andava para o lado errado. */
cdm_ok( false === strpos( $corpo_edit, 'name="cdm_direcao"' ),
	'a direcao NAO vai em campo escondido (ele seria enviado pelos dois botoes)' );

echo "\n6. As duas telas de senha\n";

$corpo_senha = cdm_corpo( $html_por_tela['criar senha'] );
cdm_ok( false !== strpos( $corpo_senha, 'Crie a sua senha' ), 'chave boa abre a tela de criar senha' );
cdm_ok( false !== strpos( $corpo_senha, 'name="cdm_senha2"' ), 'pede a senha duas vezes' );
cdm_ok( false !== strpos( $corpo_senha, 'Criar minha senha e entrar' ), 'o botao e o mesmo texto do e-mail' );
cdm_ok( false !== strpos( $corpo_senha, 'minlength="8"' ), 'o minimo de 8 e cobrado no proprio campo' );

$corpo_gasta = cdm_corpo( $html_por_tela['chave gasta'] );
cdm_ok( false !== strpos( $corpo_gasta, 'não vale mais' ), 'chave gasta diz isso em portugues de gente' );
cdm_ok( false !== strpos( $corpo_gasta, 'value="esqueci"' ), 'chave gasta oferece pedir um link novo ali mesmo' );
cdm_ok( false === strpos( $corpo_gasta, 'name="cdm_senha2"' ), 'chave gasta NAO abre o formulario de senha' );

$corpo_estranha = cdm_corpo( $html_por_tela['logada sem acesso'] );
cdm_ok( false !== strpos( $corpo_estranha, 'Esta área é do ateliê' ), 'quem nao e a artesa ve uma frase, nao um erro' );
cdm_ok( false === strpos( $corpo_estranha, 'Nova peça' ), 'quem nao e a artesa nao ve o cadastro' );
cdm_ok( false === strpos( $corpo_estranha, 'Vaso azul' ), 'quem nao e a artesa nao ve peca de ninguem' );

echo "\n7. Funciona com o JavaScript desligado (portao 22.8)\n";

/* TUDO E FORMULARIO. O script do painel faz DUAS coisas e nenhuma e necessaria:
   a previa das fotos e a confirmacao de apagar. */
foreach ( array( 'deslogada', 'artesa com peca', 'formulario novo', 'formulario editar', 'criar senha' ) as $nome ) {
	$c = cdm_corpo( $html_por_tela[ $nome ] );
	$tem_form   = ( 1 === preg_match( '#<form[^>]*method="post"#', $c ) );
	$tem_onclick = ( false !== stripos( $c, 'onclick=' ) );
	cdm_ok( $tem_form, "'$nome' age por formulario POST" );
	cdm_ok( ! $tem_onclick, "'$nome' nao depende de onclick" );
}
/* NENHUM BOTAO DE ACAO E type=button (que so funciona com JavaScript). */
$so_com_js = array();
foreach ( $html_por_tela as $nome => $h ) {
	if ( false !== strpos( cdm_corpo( $h ), 'type="button"' ) ) { $so_com_js[] = $nome; }
}
cdm_ok( empty( $so_com_js ), 'nenhum botao do painel e type=button',
	empty( $so_com_js ) ? 'nenhum' : implode( ', ', $so_com_js ) );

/* E A FOLHA E O SCRIPT VEM DO RODAPE, nunca do retorno do shortcode (secao 8). */
cdm_ok( false !== strpos( $html_por_tela['formulario novo'], 'id="cdm-atelie-css"' ), 'a folha do painel vem do rodape' );
cdm_ok( false !== strpos( $html_por_tela['formulario novo'], 'id="cdm-atelie-js"' ), 'o script do painel vem do rodape' );
$retorno_cru = $GLOBALS['__retorno_shortcode'] ?? '';
cdm_teste_logar( 'artesa' );
$_GET = array( 'estado' => 'nova' );
$cru  = call_user_func( $GLOBALS['__shortcodes']['cdm_atelie'] );
cdm_ok( false === stripos( $cru, '<script' ), 'o retorno do shortcode NAO carrega <script>' );
cdm_ok( false === stripos( $cru, '<style' ), 'o retorno do shortcode NAO carrega <style>' );

/* ZERO &#038; DENTRO DE <script> em toda tela — a cicatriz de 08/09/2026. */
$com_escape = array();
foreach ( $html_por_tela as $nome => $h ) {
	if ( false !== strpos( cdm_scripts( $h ), '&#038;' ) ) { $com_escape[] = $nome; }
}
cdm_ok( empty( $com_escape ), 'zero &#038; dentro de <script> nas telas do painel',
	empty( $com_escape ) ? count( $html_por_tela ) . ' telas' : implode( ', ', $com_escape ) );

/* ---------------------------------------------------------------------------
 * 3. AS ACOES — o caminho que muda o site, com nonce certo e errado
 * ------------------------------------------------------------------------- */

echo "\n8. As acoes: nonce, capacidade e dono\n";

$u_artesa = cdm_teste_logar( 'artesa', 10, 'artesa' );

/* SEM NONCE NADA ACONTECE. Nonce protege contra o formulario de outro site;
   capacidade protege contra a pessoa errada logada. As duas, sempre. */
/** So os inserts de PECA. `__inserts` tambem guarda as paginas que a casca cria
 *  no `init`, e contar o array inteiro fazia esta afirmacao medir a casca. */
function cdm_pecas_inseridas() {
	$n = 0;
	foreach ( (array) ( $GLOBALS['__inserts'] ?? array() ) as $i ) {
		if ( isset( $i['post_type'] ) && 'peca' === $i['post_type'] ) { $n++; }
	}
	return $n;
}

$destino = cdm_acao( array( 'cdm_acao' => 'salvar', 'cdm_titulo' => 'Vaso novo', 'cdm_nonce' => 'ERRADO' ) );
cdm_ok( false !== strpos( $destino, 'aviso=nonce' ), 'salvar com nonce errado nao grava nada', $destino );
cdm_ok( 0 === cdm_pecas_inseridas(), 'nenhuma peca foi criada pelo nonce errado', cdm_pecas_inseridas() . ' pecas' );

/* SALVAR COMO RASCUNHO — o primeiro salvar cria a peca. */
$antes_inserts = cdm_pecas_inseridas();
$destino = cdm_acao( array(
	'cdm_acao'    => 'salvar',
	'cdm_nonce'   => wp_create_nonce( 'cdm_atelie_salvar' ),
	'cdm_peca'    => '0',
	'cdm_titulo'  => 'Vaso novo do teste',
	'cdm_descricao' => 'Um vaso.',
	'cdm_destino' => 'rascunho',
	'cdm_cdm_preco' => '180,50',
	'cdm_cdm_disponibilidade' => 'pronta_entrega',
	'cdm_colecao' => 'presentes',
	'cdm_tecnica' => 'direto',
) );
cdm_ok( false !== strpos( $destino, 'aviso=salva' ), 'salvar rascunho redireciona com o aviso certo', $destino );
cdm_ok( cdm_pecas_inseridas() > $antes_inserts, 'o primeiro salvar cria a peca',
	cdm_pecas_inseridas() . ' peca(s) inserida(s)' );
preg_match( '#peca=(\d+)#', $destino, $mid );
$nova_id = (int) ( $mid[1] ?? 0 );
cdm_ok( $nova_id > 0, 'o redirecionamento leva o id da peca nova', (string) $nova_id );
cdm_ok( 'draft' === ( $GLOBALS['__pecas_por_id'][ $nova_id ]->post_status ?? '' ),
	'a peca nasce como rascunho, nunca publicada' );

/* O PRECO EM PORTUGUES. Ela vai digitar 180,50 — recusar a virgula seria a tela
   ensinando a pessoa a falar a lingua do banco de dados. */
cdm_ok( '180.5' === cdm_loja_meta( $nova_id, '_cdm_preco' ), 'o preco 180,50 e gravado como 180.5',
	cdm_loja_meta( $nova_id, '_cdm_preco' ) );
/* E AS OUTRAS FORMAS QUE ELA PODE DIGITAR. */
/* LISTA DE PARES, nunca array associativo: em PHP a chave '99' vira o INTEIRO 99,
   e o teste passava a mandar um int onde o navegador sempre manda texto — media o
   PHP em vez de medir o snippet. */
foreach ( array( array( '1.234,56', '1234.56' ), array( '99', '99' ), array( 'R$ 80,00', '80' ), array( '', '' ) ) as $par ) {
	list( $digitado, $esperado ) = $par;
	cdm_acao( array(
		'cdm_acao' => 'salvar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
		'cdm_peca' => (string) $nova_id, 'cdm_titulo' => 'Vaso novo do teste',
		'cdm_destino' => 'rascunho', 'cdm_cdm_preco' => $digitado,
	) );
	cdm_ok( $esperado === cdm_loja_meta( $nova_id, '_cdm_preco' ),
		'preco digitado "' . $digitado . '"', cdm_loja_meta( $nova_id, '_cdm_preco' ) );
}

/* PUBLICAR SEM FOTO NAO PUBLICA, e a tela DIZ o que falta. */
$destino = cdm_acao( array(
	'cdm_acao' => 'salvar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
	'cdm_peca' => (string) $nova_id, 'cdm_titulo' => 'Vaso novo do teste',
	'cdm_destino' => 'publicar', 'cdm_cdm_preco' => '180',
	'cdm_cdm_disponibilidade' => 'pronta_entrega',
	'cdm_colecao' => 'presentes', 'cdm_tecnica' => 'direto',
) );
cdm_ok( false !== strpos( $destino, 'aviso=falta' ), 'publicar sem foto para no aviso de falta', $destino );
cdm_ok( 'draft' === ( $GLOBALS['__pecas_por_id'][ $nova_id ]->post_status ?? '' ), 'e a peca CONTINUA rascunho' );
$recusa = get_post_meta( $nova_id, '_cdm_recusa', true );
cdm_ok( is_array( $recusa ) && in_array( 'Falta pelo menos uma foto.', $recusa, true ),
	'o motivo gravado e a falta da foto', is_array( $recusa ) ? implode( ' ', $recusa ) : '' );

/* COM FOTO, PUBLICA. */
$GLOBALS['__anexos'][911] = array( 'url' => 'https://clubedomosaico.com.br/f.jpg', 'largura' => 1200, 'altura' => 1500 );
update_post_meta( $nova_id, '_cdm_galeria', array( 911 ) );
$destino = cdm_acao( array(
	'cdm_acao' => 'publicar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_peca_' . $nova_id ),
	'cdm_peca' => (string) $nova_id,
) );
cdm_ok( false !== strpos( $destino, 'aviso=publicada' ), 'com foto e preco, publica', $destino );
cdm_ok( 'publish' === ( $GLOBALS['__pecas_por_id'][ $nova_id ]->post_status ?? '' ), 'a peca fica publicada' );

/* PAUSAR volta para rascunho, e a peca continua guardada. */
$destino = cdm_acao( array(
	'cdm_acao' => 'pausar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_peca_' . $nova_id ),
	'cdm_peca' => (string) $nova_id,
) );
cdm_ok( false !== strpos( $destino, 'aviso=pausada' ), 'pausar redireciona com o aviso certo', $destino );
cdm_ok( 'draft' === ( $GLOBALS['__pecas_por_id'][ $nova_id ]->post_status ?? '' ), 'pausar volta para rascunho' );

/* APAGAR VAI PARA A LIXEIRA, nunca exclusao definitiva: ela aperta com o dedo num
   telefone, e a peca tem de dar para voltar. */
$destino = cdm_acao( array(
	'cdm_acao' => 'excluir', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_peca_' . $nova_id ),
	'cdm_peca' => (string) $nova_id,
) );
cdm_ok( false !== strpos( $destino, 'aviso=apagada' ), 'apagar redireciona com o aviso certo', $destino );
cdm_ok( in_array( $nova_id, (array) ( $GLOBALS['__lixeira'] ?? array() ), true ), 'apagar manda para a LIXEIRA' );

echo "\n9. Peca de outra pessoa: ela nao toca\n";

/* A peca 888 e de outra pessoa (autor 99). Sem `edit_others_pecas`, o nucleo
   recusa por `map_meta_cap` — e a recusa e medida pelo caminho de verdade. */
$GLOBALS['__pecas_por_id'][888] = (object) array(
	'ID' => 888, 'post_type' => 'peca', 'post_status' => 'publish',
	'post_title' => 'Peça de outra pessoa', 'post_name' => 'de-outra', 'post_content' => '',
	'post_author' => 99, 'post_date_gmt' => '2026-09-12 22:00:00',
);
cdm_ok( null === cdm_atelie_minha_peca( 888 ), 'a peca de outra pessoa nao e "minha peca"' );
foreach ( array( 'publicar', 'pausar', 'excluir' ) as $acao ) {
	$destino = cdm_acao( array(
		'cdm_acao' => $acao, 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_peca_888' ), 'cdm_peca' => '888',
	) );
	cdm_ok( false !== strpos( $destino, 'aviso=nao-sua' ), "$acao em peca de outra pessoa e recusado", $destino );
	cdm_ok( 'publish' === $GLOBALS['__pecas_por_id'][888]->post_status, "$acao nao mudou a peca da outra pessoa" );
}
/* E A PROPRIA E, com a mesma regua. */
$GLOBALS['__pecas_por_id'][889] = (object) array(
	'ID' => 889, 'post_type' => 'peca', 'post_status' => 'draft',
	'post_title' => 'Minha', 'post_name' => 'minha', 'post_content' => '',
	'post_author' => 10, 'post_date_gmt' => '2026-09-12 22:00:00',
);
cdm_ok( null !== cdm_atelie_minha_peca( 889 ), 'a peca dela E "minha peca" (a regua funciona nos dois lados)' );

echo "\n10. Deslogada nao age\n";

cdm_teste_deslogar();
foreach ( array( 'salvar', 'publicar', 'pausar', 'excluir', 'foto_remover' ) as $acao ) {
	$destino = cdm_acao( array(
		'cdm_acao' => $acao, 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
		'cdm_peca' => '889', 'cdm_titulo' => 'x',
	) );
	cdm_ok( false !== strpos( $destino, 'aviso=entre' ), "deslogada: $acao e recusado", $destino );
}
cdm_ok( 'draft' === $GLOBALS['__pecas_por_id'][889]->post_status, 'nada mudou com a pessoa deslogada' );

echo "\n11. Entrar, sair e esquecer a senha\n";

$destino = cdm_acao( array(
	'cdm_acao' => 'entrar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_entrar' ),
	'cdm_login' => 'artesa', 'cdm_senha' => 'qualquer',
) );
cdm_ok( cdm_atelie_url() === $destino, 'entrar certo vai para o painel', $destino );
$destino = cdm_acao( array(
	'cdm_acao' => 'entrar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_entrar' ),
	'cdm_login' => 'nao-existe', 'cdm_senha' => 'x',
) );
cdm_ok( false !== strpos( $destino, 'aviso=login' ), 'entrar errado volta com aviso, sem dizer qual metade errou', $destino );

/* ESQUECI A SENHA responde IGUAL para e-mail conhecido e desconhecido: dizer
   "esse e-mail nao existe" entrega quem tem conta no site a quem perguntar. */
$antes = count( $GLOBALS['__emails'] );
$d1 = cdm_acao( array( 'cdm_acao' => 'esqueci', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_esqueci' ), 'cdm_email' => 'mina196@hotmail.com' ) );
$meio = count( $GLOBALS['__emails'] );
$d2 = cdm_acao( array( 'cdm_acao' => 'esqueci', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_esqueci' ), 'cdm_email' => 'ninguem@exemplo.com' ) );
cdm_ok( $d1 === $d2, 'esqueci responde igual para e-mail conhecido e desconhecido', $d1 );
cdm_ok( false !== strpos( $d1, 'aviso=enviado' ), 'e o aviso e neutro', $d1 );
cdm_ok( $meio > $antes, 'para o e-mail conhecido, o link sai' );
cdm_ok( count( $GLOBALS['__emails'] ) === $meio, 'para o desconhecido, nenhum e-mail sai' );

echo "\n12. Criar senha pela chave nativa\n";

$d = cdm_acao( array(
	'cdm_acao' => 'criar_senha', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_criar_senha' ),
	'cdm_chave' => 'CHAVE-DE-TESTE', 'cdm_quem' => 'artesa',
	'cdm_senha' => 'senhaboa123', 'cdm_senha2' => 'senhaboa123',
) );
cdm_ok( false !== strpos( $d, 'aviso=bemvinda' ), 'senha criada leva direto ao painel, ja logada', $d );
cdm_ok( in_array( 'artesa', (array) ( $GLOBALS['__senhas_trocadas'] ?? array() ), true ), 'a senha foi trocada pela funcao nativa' );

/* AS TRES RECUSAS, e cada uma volta para a MESMA tela com a chave na mao — senao
   ela perde o link e tem de pedir outro e-mail. */
$recusas = array(
	array( 'curta',  'senha1', 'senha1' ),
	array( 'difere', 'senhaboa123', 'senhaboa124' ),
);
foreach ( $recusas as $r ) {
	$d = cdm_acao( array(
		'cdm_acao' => 'criar_senha', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_criar_senha' ),
		'cdm_chave' => 'CHAVE-DE-TESTE', 'cdm_quem' => 'artesa',
		'cdm_senha' => $r[1], 'cdm_senha2' => $r[2],
	) );
	cdm_ok( false !== strpos( $d, 'aviso=' . $r[0] ), 'recusa: ' . $r[0], $d );
	cdm_ok( false !== strpos( $d, 'criar-senha=CHAVE-DE-TESTE' ), 'a recusa ' . $r[0] . ' NAO perde a chave dela' );
}
$d = cdm_acao( array(
	'cdm_acao' => 'criar_senha', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_criar_senha' ),
	'cdm_chave' => 'CHAVE-VELHA', 'cdm_quem' => 'artesa',
	'cdm_senha' => 'senhaboa123', 'cdm_senha2' => 'senhaboa123',
) );
cdm_ok( false !== strpos( $d, 'aviso=chave' ), 'chave gasta e recusada', $d );

echo "\n13. As fotos: ordem e remocao\n";

cdm_teste_logar( 'artesa', 10, 'artesa' );
$GLOBALS['__pecas_por_id'][890] = (object) array(
	'ID' => 890, 'post_type' => 'peca', 'post_status' => 'draft',
	'post_title' => 'Com fotos', 'post_name' => 'com-fotos', 'post_content' => '',
	'post_author' => 10, 'post_date_gmt' => '2026-09-12 22:00:00',
);
foreach ( array( 921, 922, 923 ) as $a ) {
	$GLOBALS['__anexos'][ $a ] = array( 'url' => 'https://clubedomosaico.com.br/' . $a . '.jpg', 'largura' => 1200, 'altura' => 1500 );
}
update_post_meta( 890, '_cdm_galeria', array( 921, 922, 923 ) );
$nonce890 = wp_create_nonce( 'cdm_atelie_peca_890' );

cdm_acao( array( 'cdm_acao' => 'foto_frente', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '921' ) );
cdm_ok( array( 922, 921, 923 ) === cdm_loja_galeria( 890 ), 'mover para frente troca com a seguinte',
	implode( ',', cdm_loja_galeria( 890 ) ) );
cdm_ok( 922 === (int) ( $GLOBALS['__capa'][890] ?? 0 ), 'a capa acompanha a primeira da ordem' );

cdm_acao( array( 'cdm_acao' => 'foto_tras', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '921' ) );
cdm_ok( array( 921, 922, 923 ) === cdm_loja_galeria( 890 ), 'mover para tras desfaz',
	implode( ',', cdm_loja_galeria( 890 ) ) );

/* AS BORDAS: a primeira nao vai mais para tras, a ultima nao vai mais para frente. */
cdm_acao( array( 'cdm_acao' => 'foto_tras', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '921' ) );
cdm_ok( array( 921, 922, 923 ) === cdm_loja_galeria( 890 ), 'a primeira foto nao sai da borda' );
cdm_acao( array( 'cdm_acao' => 'foto_frente', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '923' ) );
cdm_ok( array( 921, 922, 923 ) === cdm_loja_galeria( 890 ), 'a ultima foto nao sai da borda' );

cdm_acao( array( 'cdm_acao' => 'foto_remover', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '922' ) );
cdm_ok( array( 921, 923 ) === cdm_loja_galeria( 890 ), 'remover tira so aquela foto',
	implode( ',', cdm_loja_galeria( 890 ) ) );
cdm_acao( array( 'cdm_acao' => 'foto_remover', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '921' ) );
cdm_acao( array( 'cdm_acao' => 'foto_remover', 'cdm_nonce' => $nonce890, 'cdm_peca' => '890', 'cdm_anexo' => '923' ) );
cdm_ok( array() === cdm_loja_galeria( 890 ), 'a galeria pode ficar vazia' );
cdm_ok( ! isset( $GLOBALS['__capa'][890] ), 'sem foto, a capa e removida (nao fica apontando para nada)' );
/* COM NONCE ERRADO A ORDEM NAO MUDA. */
update_post_meta( 890, '_cdm_galeria', array( 921, 922 ) );
cdm_acao( array( 'cdm_acao' => 'foto_frente', 'cdm_nonce' => 'ERRADO', 'cdm_peca' => '890', 'cdm_anexo' => '921' ) );
cdm_ok( array( 921, 922 ) === cdm_loja_galeria( 890 ), 'nonce errado nao mexe na ordem das fotos' );

echo "\n14. O prazo nao sobrevive a troca de disponibilidade\n";

/* Deixar o numero de uma escolha anterior gravado faria a ficha dizer "pronta
   entrega, feita em 20 dias" — duas afirmacoes contraditorias na mesma linha. */
$GLOBALS['__pecas_por_id'][891] = (object) array(
	'ID' => 891, 'post_type' => 'peca', 'post_status' => 'draft',
	'post_title' => 'Prazo', 'post_name' => 'prazo', 'post_content' => '',
	'post_author' => 10, 'post_date_gmt' => '2026-09-12 22:00:00',
);
cdm_acao( array(
	'cdm_acao' => 'salvar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
	'cdm_peca' => '891', 'cdm_titulo' => 'Prazo', 'cdm_destino' => 'rascunho',
	'cdm_cdm_disponibilidade' => 'sob_encomenda', 'cdm_cdm_prazo_dias' => '20',
) );
cdm_ok( '20' === cdm_loja_meta( 891, '_cdm_prazo_dias' ), 'sob encomenda guarda o prazo' );
cdm_acao( array(
	'cdm_acao' => 'salvar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
	'cdm_peca' => '891', 'cdm_titulo' => 'Prazo', 'cdm_destino' => 'rascunho',
	'cdm_cdm_disponibilidade' => 'pronta_entrega', 'cdm_cdm_prazo_dias' => '20',
) );
cdm_ok( '' === cdm_loja_meta( 891, '_cdm_prazo_dias' ), 'trocar para pronta entrega APAGA o prazo',
	cdm_loja_meta( 891, '_cdm_prazo_dias' ) );

/* E ESCOLHA INVALIDA NAO ENTRA. O `select` oferece duas opcoes; quem mandar uma
   terceira por fora nao grava nada. */
cdm_acao( array(
	'cdm_acao' => 'salvar', 'cdm_nonce' => wp_create_nonce( 'cdm_atelie_salvar' ),
	'cdm_peca' => '891', 'cdm_titulo' => 'Prazo', 'cdm_destino' => 'rascunho',
	'cdm_cdm_disponibilidade' => 'inventado', 'cdm_cdm_base' => 'plutonio',
) );
cdm_ok( '' === cdm_loja_meta( 891, '_cdm_disponibilidade' ), 'disponibilidade inventada nao grava' );
cdm_ok( '' === cdm_loja_meta( 891, '_cdm_base' ), 'base inventada nao grava' );

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s). %d telas renderizadas, um processo cada.\n",
	$feitos, $falhas, count( $html_por_tela ) );
echo "NAO MEDIDO AQUI, e escrito de proposito: o toque no telefone dela e a chegada\n";
echo "do e-mail na caixa da Hotmail. A senha da artesa nao existe para a Fundacao.\n";
if ( $falhas > 0 ) {
	echo "REPROVADO.\n";
	exit( 1 );
}
echo "APROVADO.\n";

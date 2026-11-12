<?php
/**
 * A CURA DA PORTA DE ENTRADA, MEDIDA NO CHAO — a secao 14 da casca, que e a
 * excecao nomeada da 29.4 do ARQUIPELAGO.md.
 *
 *   php ferramentas/teste-cura-da-porta.php
 *
 * POR QUE ESTE ARQUIVO EXISTE. O item 1 do despacho de classe da Sentinela de
 * 11/11/2026 manda a casca repor sozinha o bloco `# BEGIN WordPress` do
 * `.htaccess` da raiz, e a 29.4 tinha recusado gancho automatico com um
 * argumento que continua inteiro: "porta de entrada que se conserta CALADA a
 * cada carregamento e a que ninguem consegue desfazer no dia em que estiver
 * errada". A diferenca entre a cura e o que a 29.4 recusou nao esta na
 * intencao de ninguem — esta nestas afirmacoes. Sem elas, a excecao da 29.4 e
 * uma promessa.
 *
 * E NESTA ILHA A CONTA DA QUEDA ESTA MEDIDA, nao suposta: a porta desta raiz
 * caiu em 05/11/2026, ficou ~16 horas no chao, e o Googlebot passou DENTRO da
 * janela (ultimo rastreamento de `/veiculos/bicicleta-eletrica/` em 05/11 as
 * 22:14:32). Aquela URL esta fora do indice como 404 ate hoje, e e uma das
 * duas unicas paginas desta ilha com botao de compra.
 *
 * OS MUNDOS, e cada um existe porque um desfecho DIFERENTE tem de sair:
 *
 *   A. porta caida, as quatro grandezas na mesa -> CURA, e UMA linha no log com
 *      o antes e o depois em bytes e em blocos
 *   B. porta de pe, mil requisicoes             -> arquivo intocado (bytes e
 *      mtime), ZERO linha de log, ZERO option gravada
 *   C. mod_rewrite desligado                    -> NAO cura, e o log diz isso
 *   D. raiz nao gravavel                        -> NAO cura, e o log diz isso
 *   E. hora nao vencida                         -> NAO cura e NAO fala
 *   F. o flush roda e o bloco nao volta         -> log diz FALHOU, com palavra
 *      DIFERENTE da do sucesso (e o mundo do `AllowOverride` desligado, que e
 *      chamado na HostGator e nao codigo desta ilha)
 *   G. a rota que MEDE a porta                  -> a cura se cala e nao toca em
 *      nada, senao o retrato da 29.3 nunca mostraria a queda
 *   H. retrato que nao veio / porta sem arquivo / arquivo nao gravavel / sem as
 *      ferramentas de admin -> cada um com o SEU motivo escrito
 *   I. so a option de log (sem as funcoes do Sync) -> cura, e a linha sai com a
 *      MESMA forma; medido em processo filho
 *   J. sem funcao e sem option                  -> NAO cura, NAO toca no
 *      arquivo e NAO queima a hora; medido em processo filho
 *
 * OS MUNDOS C E D SE MEDEM COM RETRATO FABRICADO, e isso nao e atalho: este
 * conteiner roda como root, e o `is_writable()` do PHP responde `true` para
 * diretorio 0444 quando quem pergunta e root. "Raiz nao gravavel" nao se encena
 * no disco daqui. E por isso que a regra inteira mora numa funcao PURA
 * (`rodametria_casca_cura_decidir`), que recebe o retrato e devolve a decisao:
 * o que nao se fabrica no disco se fabrica no retrato.
 *
 * POR QUE PHP E NAO PYTHON — o mesmo motivo do `teste-rotas.php`: a decisao
 * mora em PHP, entao a regua CHAMA as funcoes de verdade. Regua em Python sobre
 * o texto do PHP conferiria a FORMA do codigo, nunca a decisao — e aqui a
 * decisao escreve na porta de entrada do site.
 *
 * O QUE ELE NAO PROVA, escrito para ninguem ler verde aqui como ilha no ar: que
 * o Apache obedece ao arquivo. Isso e o `AllowOverride`, mora no hospedeiro, e
 * so a leitura das URLs no ar responde (29.2 e 29.4).
 */

/* ---------------------------------------------------------------------------
   OS TRES MUNDOS DE LOG SAO EXCLUDENTES, e por isso este arquivo se reexecuta.
   `function_exists()` nao se desfaz depois de definida: nao da para medir o
   caminho da FUNCAO e o da OPTION no mesmo processo. A passada de fora roda com
   as funcoes do Sync (o caminho preferido) e reexecuta duas filhas.
   --------------------------------------------------------------------------- */
$MODO = getenv( 'RDM_CURA_MODO' );
if ( ! in_array( $MODO, array( 'option', 'sem-log' ), true ) ) {
	$MODO = 'funcao';
}
$MUTACAO = (string) getenv( 'RDM_CURA_MUTACAO' );

$RAIZ = dirname( __DIR__ );
$TMP  = sys_get_temp_dir() . '/rdm-cura-' . getmypid();
@mkdir( $TMP . '/wp/wp-admin/includes', 0777, true );

define( 'ABSPATH', $TMP . '/wp/' );
define( 'RODAMETRIA_CASCA_VERSAO', 'teste' );

/* A raiz fabricada: e para ca que `get_home_path()` aponta, e e nela que o
   `.htaccess` de verdade deste teste mora. */
$PORTA = $TMP . '/';
$GLOBALS['PORTA']        = $PORTA;
$GLOBALS['MOD_REWRITE']  = true;
$GLOBALS['FLUSH_NAO_REPOE'] = false;
$GLOBALS['FLUSHES']      = 0;

function get_home_path() { return $GLOBALS['PORTA']; }
function got_mod_rewrite() { return (bool) $GLOBALS['MOD_REWRITE']; }
function save_mod_rewrite_rules() { return true; }
function home_url( $p = '/' ) { return 'https://exemplo.invalido' . $p; }
function site_url( $p = '/' ) { return 'https://exemplo.invalido' . $p; }
function current_time( $f = 'mysql' ) { return gmdate( 'Y-m-d H:i' ); }
function wp_json_encode( $v ) { return json_encode( $v ); }
function apply_filters( $t, $v ) { return $v; }

/* O flush de verdade reescreve o bloco do WordPress. O stub faz o MESMO — e por
   isso o antes e o depois podem ser comparados: sem escrever, `reparado` seria
   um campo que ninguem mediu. `FLUSH_NAO_REPOE` e o mundo F. */
function flush_rewrite_rules( $forte = false ) {
	$GLOBALS['FLUSHES']++;
	if ( ! $forte || $GLOBALS['FLUSH_NAO_REPOE'] ) { return; }
	$arq = $GLOBALS['PORTA'] . '.htaccess';
	$txt = file_exists( $arq ) ? file_get_contents( $arq ) : '';

	/* E ELE ESCREVE COM `fopen`/`fwrite`/`fclose`, NAO COM `file_put_contents`,
	   e isso nao e detalhe: e o que o WordPress faz de verdade
	   (`insert_with_markers()`, que e quem o `save_mod_rewrite_rules()` chama),
	   e e a diferenca que FAZ O CACHE DE `stat` FICAR VELHO. Medido neste
	   conteiner, PHP 8.3.6: depois de um `fwrite` de 500 bytes num arquivo de 3,
	   o `filesize()` responde 3 — e responde 500 depois do `clearstatcache()`.
	   Com `file_put_contents` o cache se invalida sozinho e o mundo do defeito
	   de 03/11 desta ilha NAO SE FABRICA. Stub mais comodo que a realidade
	   aprova o codigo que a realidade reprova. */
	$h = fopen( $arq, 'w' );
	fwrite( $h, "# BEGIN WordPress\nRewriteEngine On\nRewriteBase /\nRewriteRule . /index.php [L]\n# END WordPress\n" . $txt );
	fclose( $h );
}

/* O banco falso de options. */
$GLOBALS['OPT'] = array();
function get_option( $k, $d = false ) {
	return array_key_exists( $k, $GLOBALS['OPT'] ) ? $GLOBALS['OPT'][ $k ] : $d;
}
function update_option( $k, $v, $a = null ) {
	$GLOBALS['OPT'][ $k ] = $v;
	return true;
}
function add_action( $g, $cb, $p = 10, $n = 1 ) { return true; }

/* AS FUNCOES DO SYNC, e e a presenca delas que separa o modo `funcao` do modo
   `option`. A forma e a das irmas, byte por byte (robometria-sync.php, linhas
   66 a 81): `estado` le a option, `log` empilha por cima e corta em 40. */
if ( 'funcao' === $MODO ) {
	function rodametria_sync_estado() {
		$e = get_option( 'rodametria_sync_estado' );
		return is_array( $e ) ? $e : array( 'revisao' => -1, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	}
	function rodametria_sync_log( &$estado, $msg ) {
		array_unshift( $estado['log'], current_time( 'Y-m-d H:i' ) . ' ' . $msg );
		$estado['log'] = array_slice( $estado['log'], 0, 40 );
	}
}

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

/** Carrega UMA funcao de um snippet, equilibrando chaves — o mesmo mecanismo do
 *  `teste-rotas.php` e do `teste-caixa-da-mae.php`: o snippet inteiro registra
 *  filtros e rotas ao ser lido. */
function carregar_funcao( $src, $nome ) {
	$i = strpos( $src, "function $nome(" );
	if ( false === $i ) { return false; }
	$j = strpos( $src, '{', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '{' === $src[ $k ] ) { $n++; }
		elseif ( '}' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	eval( substr( $src, $i, $k - $i + 1 ) );
	return true;
}

$casca = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );

/* AS CONSTANTES SAIEM DO ARQUIVO, nunca digitadas aqui: constante digitada ao
   lado de constante definida e o mesmo numero em dois lugares, e a 32.4 desta
   fabrica ja paga essa divida em prosa. */
foreach ( array( 'RODAMETRIA_CASCA_CURA_INTERVALO', 'RODAMETRIA_CASCA_CURA_OPTION', 'RODAMETRIA_CASCA_SYNC_OPTION' ) as $c ) {
	if ( preg_match( "/define\\(\\s*'" . $c . "',\\s*([^)]+?)\\s*\\)/", $casca, $m ) ) {
		eval( 'define( \'' . $c . '\', ' . trim( $m[1] ) . ' );' );
	}
}
afirma( defined( 'RODAMETRIA_CASCA_CURA_INTERVALO' ) && 3600 === RODAMETRIA_CASCA_CURA_INTERVALO,
	'a trava 2 da 29.4 e "no maximo UMA tentativa por hora", e o intervalo da casca nao e 3600 s' );
afirma( defined( 'RODAMETRIA_CASCA_SYNC_OPTION' ) && 'rodametria_sync_estado' === RODAMETRIA_CASCA_SYNC_OPTION,
	'a option do estado do Sync desta ilha nao e `rodametria_sync_estado` — o `/status` le dali' );

/* AS MUTACOES SAO FEITAS NA FONTE, antes do `eval`: e a unica forma de a trava
   ser refeita COM o defeito e exigir reprovacao. Trava que nunca falhou nao e
   trava, e o `bancada.py` desta ilha cobra as duas metades do veredito. */
$MUTACOES = array(
	'M1' => array(
		'de'   => "if ( ! empty( \$h['tem_wordpress'] ) ) {",
		'para' => "if ( isset( \$h['tem_wordpress'] ) ) {",
		'o_que' => 'a porta DE PE passaria a curar (a trava 4 cai: ela falaria com o bloco no lugar)',
		'modo'  => 'funcao',
	),
	'M2' => array(
		'de'   => "	update_option( RODAMETRIA_CASCA_CURA_OPTION, \$agora, 'no' );",
		'para' => "	/* mutacao: a hora deixa de ser gravada antes de agir */",
		'o_que' => 'a trava 2 cai: sem queimar a hora antes, a requisicao seguinte tenta de novo',
		'modo'  => 'funcao',
	),
	'M3' => array(
		'de'   => "	if ( rodametria_casca_cura_e_a_rota_que_mede() ) {\n\t\treturn '';\n\t}",
		'para' => "	if ( false ) {\n\t\treturn '';\n\t}",
		'o_que' => 'a trava 5 cai: a cura passaria a rodar na rota que MEDE a porta',
		'modo'  => 'funcao',
	),
	'M4' => array(
		'de'   => "	if ( null === rodametria_casca_cura_fonte_do_log() ) {",
		'para' => "	if ( false ) {",
		'o_que' => 'a trava 3 cai: a cura aconteceria sem ter onde escrever a linha',
		/* E ELA SO MORDE NO MUNDO J. Rodada no modo `funcao` ela PASSA, e passa
		   com razao: ali existe onde escrever, e a checagem que ela remove nao
		   decide nada. Foi o proprio portao que disse isto — na primeira
		   passada M4 e M5 passaram, e o que faltava eram os mundos, nao as
		   mutacoes. Mutacao rodada no mundo errado nao mede trava: mede o
		   mundo. */
		'modo'  => 'sem-log',
	),
	'M5' => array(
		/* O `clearstatcache` DO DIAGNOSTICO, que e onde a linha e portadora de
		   peso. A primeira versao desta mutacao atacava o do PRE-FILTRO e
		   PASSAVA — e passava com razao: o pre-filtro so le existencia e
		   legibilidade, e nada que este portao consegue fabricar muda essas
		   duas com o cache quente. Foi o proprio portao que disse isso, na
		   primeira passada. A linha do pre-filtro FICA, como defesa do mundo
		   entre requisicoes, e esta anotada como defesa e nao como mecanismo:
		   trava que nao se consegue fazer morder nao se declara trava. */
		'de'   => "	clearstatcache( true, \$arquivo );\n\n	\$regras = get_option( 'rewrite_rules' );",
		'para' => "\n	\$regras = get_option( 'rewrite_rules' );",
		'o_que' => 'o `depois` do reparo sairia com tamanho de porta caida ao lado de conteudo de porta de pe — a regressao de 03/11/2026 desta ilha, que a 29.4 nomeia',
		'modo'  => 'funcao',
	),
);
if ( '' !== $MUTACAO ) {
	if ( ! isset( $MUTACOES[ $MUTACAO ] ) ) {
		echo "FALHA: mutacao $MUTACAO nao existe\n";
		exit( 2 );
	}
	$m = $MUTACOES[ $MUTACAO ];
	if ( false === strpos( $casca, $m['de'] ) ) {
		echo "FALHA: a mutacao $MUTACAO nao achou o trecho que ela troca — a casca mudou e a mutacao envelheceu\n";
		exit( 2 );
	}
	$casca = str_replace( $m['de'], $m['para'], $casca );
}

foreach ( array(
	'rodametria_casca_carregar_ferramentas_de_admin',
	'rodametria_casca_diagnostico_rotas',
	'rodametria_casca_reparar_rotas',
	'rodametria_casca_fonte_do_token',
	'rodametria_casca_cura_caminho',
	'rodametria_casca_cura_tem_bloco',
	'rodametria_casca_cura_decidir',
	'rodametria_casca_cura_retrato_curto',
	'rodametria_casca_cura_fonte_do_log',
	'rodametria_casca_cura_registrar',
	'rodametria_casca_cura_e_a_rota_que_mede',
	'rodametria_casca_cura_da_porta',
) as $f ) {
	afirma( carregar_funcao( $casca, $f ),
		sprintf( 'nao achei a funcao %s na casca — a secao 14 (excecao da 29.4) foi desfeita', $f ) );
}
if ( ! function_exists( 'rodametria_casca_cura_da_porta' ) ) {
	echo "teste-cura-da-porta: REPROVADO antes de medir — a casca nao define a cura\n";
	foreach ( $falhas as $f ) { echo "  - $f\n"; }
	exit( 1 );
}

/* O `.htaccess` CAIDO, byte por byte como o do ar nas seis quedas desta conta de
   cPanel: UM bloco so, `NFD EPC`, e as linhas de Rewrite* que sobram sem o
   bloco do WordPress. 1.057 bytes foi o tamanho medido na clubedomosaico em
   24/09, 05/10, 08/10 e 11/11, e na robometria em 30/10 e 11/11. */
$CAIDO = "# BEGIN NFD EPC\n<IfModule mod_rewrite.c>\nRewriteEngine On\nRewriteBase /\nRewriteRule ^wp-content/.* - [L]\nRewriteCond %{HTTP_USER_AGENT} !bot\nRewriteCond %{REQUEST_METHOD} GET\nRewriteRule ^(.*)$ - [E=CACHE:1]\nRewriteRule ^$ - [L]\n</IfModule>\n# END NFD EPC\n";
$ARQ   = $PORTA . '.htaccess';

function zerar( $texto ) {
	file_put_contents( $GLOBALS['PORTA'] . '.htaccess', $texto );
	$GLOBALS['OPT'] = array();
	if ( 'sem-log' !== getenv( 'RDM_CURA_MODO' ) ) {
		$GLOBALS['OPT']['rodametria_sync_estado'] = array( 'revisao' => 86, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	}
	$GLOBALS['MOD_REWRITE']     = true;
	$GLOBALS['FLUSH_NAO_REPOE'] = false;
	$GLOBALS['FLUSHES']         = 0;
	unset( $_GET['rest_route'] );
	clearstatcache( true, $GLOBALS['PORTA'] . '.htaccess' );
}

function log_da_cura() {
	$e = get_option( 'rodametria_sync_estado' );
	return is_array( $e ) && isset( $e['log'] ) && is_array( $e['log'] ) ? $e['log'] : array();
}

/* ----------------------------------------------------- A FONTE DO LOG, antes */

$fonte = rodametria_casca_cura_fonte_do_log();
if ( 'funcao' === $MODO ) {
	afirma( 'funcao:rodametria_sync_log' === $fonte,
		'com as funcoes do Sync carregadas a fonte do log tem de ser a FUNCAO, e saiu: ' . var_export( $fonte, true ) );
} elseif ( 'option' === $MODO ) {
	$GLOBALS['OPT']['rodametria_sync_estado'] = array( 'revisao' => 86, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	afirma( 'option:rodametria_sync_estado' === rodametria_casca_cura_fonte_do_log(),
		'sem as funcoes do Sync e COM a option, a fonte tem de ser a OPTION' );
} else {
	afirma( null === $fonte,
		'sem funcao e sem option a fonte do log tem de ser null, e saiu: ' . var_export( $fonte, true ) );
}

/* ------------------------------------------------------------------ MUNDO A */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$bytes_antes = filesize( $ARQ );
	$linha       = rodametria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	$texto_depois = (string) file_get_contents( $ARQ );
	$log          = log_da_cura();

	afirma( 1 === preg_match( '/^#\s*BEGIN\s+WordPress\s*$/mi', $texto_depois ),
		'MUNDO A: a porta estava caida com as quatro grandezas na mesa e o bloco do WordPress NAO voltou' );
	afirma( 1 === count( $log ),
		'MUNDO A: a cura tem de escrever UMA linha no log, e escreveu ' . count( $log ) );
	afirma( isset( $log[0] ) && false !== strpos( $log[0], 'cura da porta: bloco WordPress reposto' ),
		'MUNDO A: a linha do log nao nomeia a reposicao do bloco: ' . ( isset( $log[0] ) ? $log[0] : '(sem linha)' ) );
	afirma( isset( $log[0] ) && 2 === preg_match_all( '/(\d+) bytes \[/', $log[0], $bs ),
		'MUNDO A: a trava 3 exige o antes E o depois em bytes e em blocos, e a linha nao tem os dois retratos' );
	/* E OS DOIS NUMEROS TEM DE SER DIFERENTES, CRESCENDO — esta e a afirmacao
	   que prende a regressao de 03/11/2026 desta ilha, e ela e a razao de o
	   stub acima escrever com `fwrite`. Sem o `clearstatcache()` no topo do
	   diagnostico, `bytes` e `mtime` saem do cache de `stat` e `blocos` e
	   `tem_wordpress` saem frescos: o `depois` sai com TAMANHO DE PORTA CAIDA
	   ao lado de CONTEUDO DE PORTA DE PE. Metade dos campos de um mundo e
	   metade do outro, na mesma linha de log — e o campo que isso corrompe e o
	   `mtime`, que e a prova do chamado na HostGator. */
	afirma( isset( $bs[1][0], $bs[1][1] ) && (int) $bs[1][1] > (int) $bs[1][0],
		'MUNDO A: o `depois` da linha nao cresceu em relacao ao `antes` — tamanho de porta caida ao lado de conteudo de porta de pe, que e o defeito de 03/11 (a 29.4 o descreve com estas palavras)' );
	afirma( isset( $log[0] ) && false === strpos( $log[0], 'HTTP_USER_AGENT' ) && false === strpos( $log[0], 'RewriteCond' ),
		'MUNDO A: o conteudo do arquivo VAZOU para o log, que e publico — a 29.3 proibe' );
	afirma( isset( $log[0] ) && 1 === preg_match( '/^\d{4}-\d{2}-\d{2} \d{2}:\d{2} cura da porta/', $log[0] ),
		'MUNDO A: a linha nao tem a forma do log do Sync (data de minuto na frente): ' . ( isset( $log[0] ) ? $log[0] : '' ) );
	afirma( isset( $log[0] ) && false !== strpos( $log[0], 'NFD EPC' ) && false !== strpos( $log[0], 'WordPress' ),
		'MUNDO A: a linha tem de trazer os NOMES dos blocos do antes e do depois' );
	afirma( (int) get_option( RODAMETRIA_CASCA_CURA_OPTION, 0 ) > 0,
		'MUNDO A: a hora da tentativa nao foi gravada na option' );
	afirma( filesize( $ARQ ) > $bytes_antes,
		'MUNDO A: o arquivo nao cresceu — o bloco reposto tem bytes' );
	afirma( 1 === $GLOBALS['FLUSHES'],
		'MUNDO A: o flush tem de rodar UMA vez, e rodou ' . $GLOBALS['FLUSHES'] );
}

/* ------------------------------------------------------------------ MUNDO B */

zerar( "# BEGIN WordPress\nRewriteEngine On\n# END WordPress\n# BEGIN NFD EPC\n# END NFD EPC\n" );
$b_bytes = filesize( $ARQ );
$b_mtime = filemtime( $ARQ );
$b_falou = 0;
for ( $i = 0; $i < 1000; $i++ ) {
	if ( '' !== rodametria_casca_cura_da_porta() ) { $b_falou++; }
}
clearstatcache( true, $ARQ );
afirma( 0 === $b_falou,
	'MUNDO B: com a porta DE PE a cura falou em ' . $b_falou . ' de 1000 requisicoes (trava 4)' );
afirma( 0 === count( log_da_cura() ),
	'MUNDO B: com a porta de pe o log ganhou ' . count( log_da_cura() ) . ' linha(s) — janela cheia e item que rolou para fora dela (20.4)' );
afirma( $b_bytes === filesize( $ARQ ) && $b_mtime === filemtime( $ARQ ),
	'MUNDO B: a cura ENCOSTOU no .htaccess de uma porta que estava de pe' );
afirma( false === get_option( RODAMETRIA_CASCA_CURA_OPTION ),
	'MUNDO B: a option da hora foi gravada sem haver tentativa nenhuma' );
afirma( 0 === $GLOBALS['FLUSHES'],
	'MUNDO B: o flush rodou com a porta de pe' );

/* ------------------------------------------------------------- MUNDOS C a H */
/* A funcao PURA, com retrato FABRICADO: e aqui que moram os mundos que nao se
   encenam no disco deste conteiner. */

function retrato_de( $muda = array() ) {
	$r = array(
		'mod_rewrite'          => true,
		'raiz_gravavel'        => true,
		'ferramentas_de_admin' => true,
		'htaccess'             => array(
			'existe'        => true,
			'legivel'       => true,
			'gravavel'      => true,
			'bytes'         => 1057,
			'blocos'        => array( 'NFD EPC' ),
			'tem_wordpress' => false,
		),
	);
	foreach ( $muda as $k => $v ) {
		if ( 'htaccess' === $k ) { $r['htaccess'] = array_merge( $r['htaccess'], $v ); }
		else { $r[ $k ] = $v; }
	}
	return $r;
}

$d = rodametria_casca_cura_decidir( retrato_de(), 0, 1000, 3600 );
afirma( ! empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO C/D base: com as quatro grandezas na mesa a decisao tem de ser CURAR, sem motivo a dizer' );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ), 'MUNDO C: curou com mod_rewrite DESLIGADO' );
afirma( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'mod_rewrite' ),
	'MUNDO C: o motivo nao nomeia o mod_rewrite: ' . var_export( $d['motivo'], true ) );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => null ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ),
	'MUNDO C-b: `mod_rewrite: null` e "nao sei", e nao sei NAO autoriza escrever na porta de entrada' );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'raiz_gravavel' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ), 'MUNDO D: curou com a raiz NAO gravavel' );
afirma( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'raiz' ),
	'MUNDO D: o motivo nao nomeia a raiz: ' . var_export( $d['motivo'], true ) );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'gravavel' => false ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'gravavel' ),
	'MUNDO H-a: arquivo nao gravavel tem de recusar COM motivo proprio' );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'ferramentas_de_admin' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'wp-admin' ),
	'MUNDO H-b: sem as ferramentas de admin o flush(true) vira flush(false), e isso tem de ser DITO' );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'existe' => false ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'nao existe' ),
	'MUNDO H-c: arquivo ausente tem de recusar com motivo proprio' );

$d = rodametria_casca_cura_decidir( array(), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'retrato' ),
	'MUNDO H-d: a cura nao age sobre medicao que nao existe, e tem de dizer isso' );

$d = rodametria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'tem_wordpress' => true ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO H-e: porta de pe e o unico desfecho com NADA a dizer (trava 4)' );

/* MUNDO E — hora nao vencida: nao cura e NAO fala. E a ordem importa: o relogio
   e checado ANTES dos motivos de recusa, senao ilha com mod_rewrite desligado
   encheria as 40 linhas do log em um minuto. */
$d = rodametria_casca_cura_decidir( retrato_de(), 1000, 1500, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO E: hora nao vencida tem de recusar CALADA' );
$d = rodametria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => false ) ), 1000, 1500, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO E-b: o relogio tem de ser checado ANTES do motivo de recusa, senao o log enche de ruido' );
$d = rodametria_casca_cura_decidir( retrato_de(), 1000, 1000 + 3600, 3600 );
afirma( ! empty( $d['curar'] ),
	'MUNDO E-c: exatamente no intervalo a hora JA venceu (o teto e `<`, nao `<=`)' );

/* E o mundo E no gancho inteiro, com arquivo de verdade. */
if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$GLOBALS['OPT'][ RODAMETRIA_CASCA_CURA_OPTION ] = time();
	$e_bytes = filesize( $ARQ );
	$e_linha = rodametria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( '' === $e_linha && 0 === count( log_da_cura() ) && $e_bytes === filesize( $ARQ ) && 0 === $GLOBALS['FLUSHES'],
		'MUNDO E (gancho): com a hora nao vencida a cura tem de sair calada e sem tocar no arquivo' );
}

/* ------------------------------------------------------------------ MUNDO F */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$GLOBALS['FLUSH_NAO_REPOE'] = true;
	$f_linha = rodametria_casca_cura_da_porta();
	$f_log   = log_da_cura();
	afirma( 1 === count( $f_log ) && false !== strpos( $f_log[0], 'cura da porta FALHOU' ),
		'MUNDO F: o flush rodou, o bloco nao voltou, e o log nao disse FALHOU: ' . ( isset( $f_log[0] ) ? $f_log[0] : '(sem linha)' ) );
	afirma( isset( $f_log[0] ) && false === strpos( $f_log[0], 'bloco WordPress reposto' ),
		'MUNDO F: a palavra do fracasso e a do sucesso se confundem, e o conserto dos dois mundos nao e o mesmo (20.5)' );
	afirma( isset( $f_log[0] ) && false !== strpos( $f_log[0], 'AllowOverride' ),
		'MUNDO F: a linha nao aponta o `AllowOverride` do hospedeiro, que e onde o conserto deste mundo mora (29.4)' );
}

/* ------------------------------------------------------------------ MUNDO G */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$_GET['rest_route'] = '/rodametria/v1/rotas';
	$g_bytes = filesize( $ARQ );
	$g_linha = rodametria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( '' === $g_linha, 'MUNDO G: a cura falou dentro da rota que MEDE a porta' );
	afirma( $g_bytes === filesize( $ARQ ) && 0 === count( log_da_cura() ) && 0 === $GLOBALS['FLUSHES'],
		'MUNDO G: a cura AGIU na rota de diagnostico — o retrato da 29.3 nunca mostraria a queda (trava 5)' );
	afirma( false === get_option( RODAMETRIA_CASCA_CURA_OPTION ),
		'MUNDO G: a cura queimou a hora na rota que mede, e a hora queimada ali atrasa a cura de verdade' );
	afirma( true === rodametria_casca_cura_e_a_rota_que_mede(),
		'MUNDO G: a propria regua nao reconhece a rota de diagnostico' );
	unset( $_GET['rest_route'] );
	$_GET['rest_route'] = '/rodametria/v1/status';
	afirma( false === rodametria_casca_cura_e_a_rota_que_mede(),
		'MUNDO G-b: a regua confundiu o /status com a rota que mede a porta, e ai a cura nunca roda em requisicao REST' );
	unset( $_GET['rest_route'] );
}

/* ------------------------------------------------------------------ MUNDO J */

if ( 'sem-log' === $MODO ) {
	zerar( $CAIDO );
	$j_bytes = filesize( $ARQ );
	$j_linha = rodametria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( $j_bytes === filesize( $ARQ ),
		'MUNDO J: sem lugar para escrever a linha, a cura TOCOU no arquivo — a trava 3 nao e enfeite do sucesso' );
	afirma( 0 === $GLOBALS['FLUSHES'],
		'MUNDO J: o flush rodou sem haver onde registrar a tentativa' );
	afirma( false === get_option( RODAMETRIA_CASCA_CURA_OPTION ),
		'MUNDO J: a hora foi queimada sem nenhuma tentativa ter acontecido' );
	afirma( false !== strpos( (string) $j_linha, 'nao ha onde escrever' ),
		'MUNDO J: a recusa tem de se NOMEAR para quem chamou, e saiu: ' . var_export( $j_linha, true ) );
	afirma( false === rodametria_casca_cura_registrar( 'x' ),
		'MUNDO J: o registrar devolveu verdadeiro sem ter onde escrever' );
}

/* ------------------------------------------------- O retrato curto, sozinho */

afirma( '1057 bytes [NFD EPC]' === rodametria_casca_cura_retrato_curto( retrato_de() ),
	'o retrato curto mudou de forma: ' . rodametria_casca_cura_retrato_curto( retrato_de() ) );
afirma( 'sem retrato' === rodametria_casca_cura_retrato_curto( array() ),
	'retrato ausente tem de dizer "sem retrato" em vez de "0 bytes []"' );

/* ------------------------------------------------------- O pre-filtro barato */

zerar( $CAIDO );
afirma( false === rodametria_casca_cura_tem_bloco( $ARQ ),
	'o pre-filtro leu o bloco do WordPress num arquivo caido' );
zerar( "# BEGIN WordPress\n# END WordPress\n" );
afirma( true === rodametria_casca_cura_tem_bloco( $ARQ ),
	'o pre-filtro nao achou o bloco do WordPress num arquivo de pe' );
afirma( null === rodametria_casca_cura_tem_bloco( $PORTA . 'nao-existe-nunca' ),
	'arquivo ausente tem de devolver null (nao sei), nunca false (esta caido)' );
afirma( null === rodametria_casca_cura_tem_bloco( '' ),
	'caminho vazio tem de devolver null' );
zerar( "# BEGIN NFD EPC\n# nao mexer: regra do WordPress antiga\n# END NFD EPC\n" );
afirma( false === rodametria_casca_cura_tem_bloco( $ARQ ),
	'o pre-filtro achou o bloco por uma MENCAO a palavra WordPress fora de um `# BEGIN` — e a mesma regua da secao 12' );

/* O CACHE DE `stat` DO PHP, MEDIDO EM VEZ DE SUPOSTO — e a medicao mudou onde
   a mutacao M5 mora.
   `file_exists()` e `is_readable()` LEEM o cache de stat; `file_get_contents()`
   nao. Entao basta perguntar por um arquivo que ainda nao existe — o que grava
   a ausencia no cache — e cria-lo em seguida: sem o `clearstatcache()` no topo,
   o pre-filtro responde `null` ("nao sei") sobre um arquivo que esta de pe na
   frente dele. O efeito nao e catastrofico (o gancho segue para o diagnostico
   completo, que tem o seu proprio `clearstatcache`), e e por isso que ele passa
   desapercebido: o preco e o caminho CARO rodando no mundo barato, a cada
   requisicao, com `require` de `wp-admin/includes` no meio.
   E O QUE A MEDICAO DISSE, neste conteiner e nesta versao (PHP 8.3.6): esta
   afirmacao PASSA com a linha e PASSA sem ela, porque `file_put_contents()` e
   `unlink()` invalidam o cache do proprio processo — so `fwrite()` sobre um
   descritor aberto o deixa velho, e isso nao muda existencia nem legibilidade.
   Logo a linha do pre-filtro e DEFESA (do mundo em que outro processo cria o
   arquivo), nunca mecanismo, e nao se declara trava: a mutacao que a atacava
   passava, e passava com razao. A trava de verdade e a do DIAGNOSTICO, que a
   M5 ataca e que o MUNDO A prende pelos dois numeros de bytes. */
$novo_arq = $PORTA . 'htaccess-do-cache-de-stat';
@unlink( $novo_arq );
clearstatcache( true, $novo_arq );
file_exists( $novo_arq );
file_put_contents( $novo_arq, "# BEGIN WordPress\n# END WordPress\n" );
afirma( true === rodametria_casca_cura_tem_bloco( $novo_arq ),
	'o pre-filtro leu o CACHE DE STAT e disse "nao sei" sobre um arquivo que acabou de nascer de pe' );
@unlink( $novo_arq );

/* ------------------------------------------- A FORMA DA LINHA NOS DOIS MODOS */
/* O caminho de reserva nao inventa formato: formato novo no mesmo log seria o
   mesmo fato dito de duas maneiras. A filha do modo `option` imprime a linha
   que escreveu, e a mae compara com a dela. */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	rodametria_casca_cura_da_porta();
	$lg = log_da_cura();
	$forma = isset( $lg[0] ) ? preg_replace( '/\d/', 'N', $lg[0] ) : '';
	echo "FORMA: $forma\n";
}

/* ------------------------------------------------- AS FILHAS E AS MUTACOES */

$extra  = 0;
$mortas = array();
if ( 'funcao' === $MODO && '' === $MUTACAO ) {

	$formas = array();
	foreach ( array( 'option', 'sem-log' ) as $modo ) {
		$saida = array();
		$cod   = 0;
		exec( 'RDM_CURA_MODO=' . $modo . ' php ' . escapeshellarg( __FILE__ ) . ' 2>&1', $saida, $cod );
		$texto = implode( "\n", $saida );
		afirma( 0 === $cod,
			"o modo de log `$modo` reprovou no processo filho:\n    " . str_replace( "\n", "\n    ", $texto ) );
		if ( preg_match( '/(\d+) afirmacoes/', $texto, $m ) ) { $extra += (int) $m[1]; }
		if ( preg_match( '/^FORMA: (.+)$/m', $texto, $m ) ) { $formas[ $modo ] = $m[1]; }
	}

	zerar( $CAIDO );
	rodametria_casca_cura_da_porta();
	$lg_mae = log_da_cura();
	$forma_mae = isset( $lg_mae[0] ) ? preg_replace( '/\d/', 'N', $lg_mae[0] ) : '';
	afirma( isset( $formas['option'] ) && $formas['option'] === $forma_mae,
		'a linha do caminho de RESERVA tem forma diferente da do caminho da FUNCAO — o mesmo fato dito de duas maneiras no mesmo log. funcao: '
			. $forma_mae . ' / option: ' . ( isset( $formas['option'] ) ? $formas['option'] : '(nao saiu)' ) );

	foreach ( array_keys( $MUTACOES ) as $mut ) {
		$saida = array();
		$cod   = 0;
		exec( 'RDM_CURA_MODO=' . $MUTACOES[ $mut ]['modo'] . ' RDM_CURA_MUTACAO=' . $mut
			. ' php ' . escapeshellarg( __FILE__ ) . ' 2>&1', $saida, $cod );
		if ( 2 === $cod ) {
			$mortas[] = "$mut: a mutacao nao achou o trecho que ela troca — ela envelheceu junto com a casca";
		} elseif ( 0 === $cod ) {
			$mortas[] = "$mut: a mutacao PASSOU, e ela devia reprovar — " . $MUTACOES[ $mut ]['o_que'];
		}
	}
	foreach ( $mortas as $m ) { afirma( false, $m ); }
}

@unlink( $ARQ );
@rmdir( $TMP . '/wp/wp-admin/includes' );
@rmdir( $TMP . '/wp/wp-admin' );
@rmdir( $TMP . '/wp' );
@rmdir( $TMP );

$rotulo = 'teste-cura-da-porta' . ( 'funcao' === $MODO ? '' : " (modo $MODO)" ) . ( '' === $MUTACAO ? '' : " (mutacao $MUTACAO)" );
printf( "%s: %d afirmacoes%s, %d mutacao(oes) cobrada(s), %d falha(s)\n",
	$rotulo, $afirmacoes, $extra ? " (+$extra nos processos filhos)" : '',
	( 'funcao' === $MODO && '' === $MUTACAO ) ? count( $MUTACOES ) : 0, count( $falhas ) );
foreach ( $falhas as $f ) { echo "  - $f\n"; }
echo count( $falhas ) ? "REPROVADO\n" : "APROVADO\n";
exit( count( $falhas ) ? 1 : 0 );

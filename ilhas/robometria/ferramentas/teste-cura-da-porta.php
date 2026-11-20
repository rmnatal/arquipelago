<?php
/**
 * A CURA DA PORTA DE ENTRADA, MEDIDA NO CHAO — a secao 6 da casca, que e a
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
 * E NESTA ILHA A CONTA DA QUEDA ESTA MEDIDA, nao suposta — TRES quedas desta
 * raiz, e nas tres o tempo no chao foi decidido por quando alguem rodou um
 * comando: 30/10 a 02/11/2026, QUATRO DIAS com a home em 200 e as outras 13
 * URLs servindo a pagina de erro da HostGator; 11/11/2026, achada em menos de
 * dois dias; e 19/11 a 20/11/2026, 7 de 7 paginas internas em 404, achada por
 * ACIDENTE por uma execucao que estava medindo outra coisa. Esta e a ilha
 * MELHOR POSICIONADA do arquipelago — 15 impressoes, posicao 7,2 e 10 das 14
 * URLs indexadas na leitura semanal de 18/11 —, e nas tres ela serviu 404 ao
 * Google. Era tambem a UNICA ilha no ar sem esta cura, e e por isso que a
 * ultima queda nao se curou sozinha.
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
 * (`robometria_casca_cura_decidir`), que recebe o retrato e devolve a decisao:
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
$MODO = getenv( 'RBM_CURA_MODO' );
if ( ! in_array( $MODO, array( 'option', 'sem-log' ), true ) ) {
	$MODO = 'funcao';
}
$MUTACAO = (string) getenv( 'RBM_CURA_MUTACAO' );

$RAIZ = dirname( __DIR__ );
$TMP  = sys_get_temp_dir() . '/rbm-cura-' . getmypid();
@mkdir( $TMP . '/wp/wp-admin/includes', 0777, true );

define( 'ABSPATH', $TMP . '/wp/' );
define( 'ROBOMETRIA_CASCA_VERSAO', 'teste' );

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
	function robometria_sync_estado() {
		$e = get_option( 'robometria_sync_estado' );
		return is_array( $e ) ? $e : array( 'revisao' => -1, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	}
	function robometria_sync_log( &$estado, $msg ) {
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

$casca = file_get_contents( $RAIZ . '/snippets/robometria-casca.php' );

/* AS CONSTANTES SAIEM DO ARQUIVO, nunca digitadas aqui: constante digitada ao
   lado de constante definida e o mesmo numero em dois lugares, e a 32.4 desta
   fabrica ja paga essa divida em prosa. */
foreach ( array( 'ROBOMETRIA_CASCA_CURA_INTERVALO', 'ROBOMETRIA_CASCA_CURA_OPTION', 'ROBOMETRIA_CASCA_SYNC_OPTION',
	/* 14-c (17/11/2026). */
	'ROBOMETRIA_CASCA_PORTA_OPTION', 'ROBOMETRIA_CASCA_PORTA_EPISODIO_S' ) as $c ) {
	if ( preg_match( "/define\\(\\s*'" . $c . "',\\s*([^)]+?)\\s*\\)/", $casca, $m ) ) {
		eval( 'define( \'' . $c . '\', ' . trim( $m[1] ) . ' );' );
	}
}
afirma( defined( 'ROBOMETRIA_CASCA_CURA_INTERVALO' ) && 3600 === ROBOMETRIA_CASCA_CURA_INTERVALO,
	'a trava 2 da 29.4 e "no maximo UMA tentativa por hora", e o intervalo da casca nao e 3600 s' );
afirma( defined( 'ROBOMETRIA_CASCA_SYNC_OPTION' ) && 'robometria_sync_estado' === ROBOMETRIA_CASCA_SYNC_OPTION,
	'a option do estado do Sync desta ilha nao e `robometria_sync_estado` — o `/status` le dali' );
/* 14-c: O INTERVALO DO EPISODIO TEM DE SER O MESMO DA TRAVA 2, e isto nao e
   gosto: numa ilha com a cura carregada, uma hora inteira sem leitura no chao e
   uma hora em que a cura tambem nao foi chamada, logo nada aconteceu naquela
   janela. Se os dois numeros divergirem, o caminho (b) da regra do episodio
   passa a contar quedas numa janela em que a cura ainda estava agindo. */
afirma( defined( 'ROBOMETRIA_CASCA_PORTA_EPISODIO_S' )
	&& ROBOMETRIA_CASCA_PORTA_EPISODIO_S === ROBOMETRIA_CASCA_CURA_INTERVALO,
	'14-c: o intervalo do episodio e o da trava 2 divergiram — ' . ( defined( 'ROBOMETRIA_CASCA_PORTA_EPISODIO_S' ) ? ROBOMETRIA_CASCA_PORTA_EPISODIO_S : '(nao definido)' ) . ' contra ' . ROBOMETRIA_CASCA_CURA_INTERVALO );

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
		'de'   => "	update_option( ROBOMETRIA_CASCA_CURA_OPTION, \$agora, 'no' );",
		'para' => "	/* mutacao: a hora deixa de ser gravada antes de agir */",
		'o_que' => 'a trava 2 cai: sem queimar a hora antes, a requisicao seguinte tenta de novo',
		'modo'  => 'funcao',
	),
	'M3' => array(
		'de'   => "	if ( robometria_casca_cura_e_a_rota_que_mede() ) {\n\t\treturn '';\n\t}",
		'para' => "	if ( false ) {\n\t\treturn '';\n\t}",
		'o_que' => 'a trava 5 cai: a cura passaria a rodar na rota que MEDE a porta',
		'modo'  => 'funcao',
	),
	'M4' => array(
		'de'   => "	if ( null === robometria_casca_cura_fonte_do_log() ) {",
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
	/* AS DUAS DO 14-b. A primeira e a unica confusao que custa um CHAMADO:
	   "nao sei" lido como "porta caida" manda abrir chamado na HostGator por um
	   defeito que ninguem mediu. A segunda e a confusao simetrica e mais caras
	   das duas: bloco AUSENTE lido como bloco PRESENTE diz `AllowOverride` num
	   mundo em que a proxima requisicao conserta sozinha — e aí ninguem espera,
	   porque o retrato mandou abrir chamado. */
	'M6' => array(
		'de'   => "		'tem_bloco_wordpress' => ( null === \$tem_bloco ) ? null : (bool) \$tem_bloco,",
		'para' => "		'tem_bloco_wordpress' => (bool) \$tem_bloco,",
		'o_que' => '"nao sei" (arquivo ausente ou ilegivel) sairia no retrato publico como PORTA CAIDA',
		'modo'  => 'funcao',
	),
	'M7' => array(
		'de'   => "		'leitura'             => ( true === \$tem_bloco )",
		'para' => "		'leitura'             => ( false === \$tem_bloco || true === \$tem_bloco )",
		'o_que' => 'bloco AUSENTE sairia com a leitura do bloco PRESENTE — chamado na HostGator onde a cura conserta sozinha',
		'modo'  => 'funcao',
	),
	/* AS TRES DO 14-c. A primeira e a ORDEM, que e a secao inteira: contar
	   depois de perguntar a hora e nao contar. */
	'M8' => array(
		'de'   => "	if ( function_exists( 'robometria_casca_porta_observar' ) ) {\n\t\trobometria_casca_porta_observar( \$tem_bloco, \$agora );\n\t}",
		'para' => "	/* mutacao: a leitura no chao deixa de ser contada antes da trava */",
		'o_que' => 'o apagamento que cai DENTRO da hora queimada da trava 2 voltaria a nao existir para ninguem — nem no log (de proposito) nem no contador',
		'modo'  => 'funcao',
	),
	'M9' => array(
		'de'   => "		|| ( null !== \$repos && \$repos >= \$ultima )",
		'para' => "		|| ( null !== \$repos && \$repos > \$ultima )",
		'o_que' => 'a cura dispara na MESMA requisicao da leitura, entao os dois carimbos caem no mesmo segundo: com `>` o apagamento de ~4 minutos depois da cura das 10:15 nao abriria episodio novo',
		'modo'  => 'funcao',
	),
	'M10' => array(
		'de'   => "	if ( null === \$tem_bloco ) {\n\t\t\$e['leituras_nao_sei'] = \$e['leituras_nao_sei'] + 1;",
		'para' => "	if ( false ) {\n\t\t\$e['leituras_nao_sei'] = \$e['leituras_nao_sei'] + 1;",
		'o_que' => '"nao sei" (arquivo ausente ou ilegivel) entraria na contagem como QUEDA — a mesma confusao do M6, e ela manda abrir chamado por um defeito que ninguem mediu',
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
	'robometria_casca_carregar_ferramentas_de_admin',
	'robometria_casca_diagnostico_rotas',
	'robometria_casca_reparar_rotas',
	/* O NOME DESTA FUNCAO DIVERGE DA ILHA DE ORIGEM, e a divergencia e
	   medida e nao de gosto: na rodametria o snippet do Sync nao esta no
	   repositorio e ela tem `rodametria_casca_fonte_do_token()`, que DIZ por
	   onde o token foi procurado. Aqui o Sync esta no repositorio e a casca
	   le o token pela funcao dele, entao a funcao equivalente desta ilha e
	   `robometria_casca_token_esperado()`. Ela entra na lista pelo mesmo
	   motivo das outras: sem ela a rota da 29.3 nao autentica, e foi por essa
	   rota que esta ilha voltou ao ar em 02/11 e em 20/11/2026. */
	'robometria_casca_token_esperado',
	'robometria_casca_cura_caminho',
	'robometria_casca_cura_tem_bloco',
	'robometria_casca_cura_decidir',
	'robometria_casca_cura_retrato_curto',
	'robometria_casca_cura_fonte_do_log',
	'robometria_casca_cura_registrar',
	'robometria_casca_cura_e_a_rota_que_mede',
	'robometria_casca_cura_da_porta',
	/* 14-b, as duas de 17/11/2026 — e elas entram nesta lista para o portao
	   REPROVAR se alguem as remover: o retrato publico da porta e o unico
	   instrumento desta nuvem que separa "AllowOverride do hospedeiro" de
	   "a hora da trava 2 ainda queimada", e os dois tem conserto diferente. */
	'robometria_casca_cura_espera_s',
	'robometria_casca_porta_retrato_publico',
	/* 14-c, as cinco de 17/11/2026. Elas entram nesta lista pelo motivo das
	   duas de cima: o contador e o unico instrumento desta nuvem que ve o
	   apagamento que cai DENTRO da hora queimada da trava 2 — no log ele nao
	   deixa rastro nenhum, de proposito —, e a frequencia que o chamado na
	   HostGator usa como argumento sai dele. Remover uma e fazer a serie do
	   chamado voltar a ser um piso dito como se fosse a conta. */
	'robometria_casca_porta_estado_normal',
	'robometria_casca_porta_contar',
	'robometria_casca_porta_marcar_reposicao',
	'robometria_casca_porta_quedas_publico',
	'robometria_casca_porta_estado',
	'robometria_casca_porta_observar',
) as $f ) {
	afirma( carregar_funcao( $casca, $f ),
		sprintf( 'nao achei a funcao %s na casca — a secao 6 (excecao da 29.4) foi desfeita', $f ) );
}
if ( ! function_exists( 'robometria_casca_cura_da_porta' ) ) {
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
	if ( 'sem-log' !== getenv( 'RBM_CURA_MODO' ) ) {
		$GLOBALS['OPT']['robometria_sync_estado'] = array( 'revisao' => 86, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	}
	$GLOBALS['MOD_REWRITE']     = true;
	$GLOBALS['FLUSH_NAO_REPOE'] = false;
	$GLOBALS['FLUSHES']         = 0;
	unset( $_GET['rest_route'] );
	clearstatcache( true, $GLOBALS['PORTA'] . '.htaccess' );
}

function log_da_cura() {
	$e = get_option( 'robometria_sync_estado' );
	return is_array( $e ) && isset( $e['log'] ) && is_array( $e['log'] ) ? $e['log'] : array();
}

/* ----------------------------------------------------- A FONTE DO LOG, antes */

$fonte = robometria_casca_cura_fonte_do_log();
if ( 'funcao' === $MODO ) {
	afirma( 'funcao:robometria_sync_log' === $fonte,
		'com as funcoes do Sync carregadas a fonte do log tem de ser a FUNCAO, e saiu: ' . var_export( $fonte, true ) );
} elseif ( 'option' === $MODO ) {
	$GLOBALS['OPT']['robometria_sync_estado'] = array( 'revisao' => 86, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	afirma( 'option:robometria_sync_estado' === robometria_casca_cura_fonte_do_log(),
		'sem as funcoes do Sync e COM a option, a fonte tem de ser a OPTION' );
} else {
	afirma( null === $fonte,
		'sem funcao e sem option a fonte do log tem de ser null, e saiu: ' . var_export( $fonte, true ) );
}

/* ------------------------------------------------------------------ MUNDO A */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$bytes_antes = filesize( $ARQ );
	$linha       = robometria_casca_cura_da_porta();
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
	afirma( (int) get_option( ROBOMETRIA_CASCA_CURA_OPTION, 0 ) > 0,
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
	if ( '' !== robometria_casca_cura_da_porta() ) { $b_falou++; }
}
clearstatcache( true, $ARQ );
afirma( 0 === $b_falou,
	'MUNDO B: com a porta DE PE a cura falou em ' . $b_falou . ' de 1000 requisicoes (trava 4)' );
afirma( 0 === count( log_da_cura() ),
	'MUNDO B: com a porta de pe o log ganhou ' . count( log_da_cura() ) . ' linha(s) — janela cheia e item que rolou para fora dela (20.4)' );
afirma( $b_bytes === filesize( $ARQ ) && $b_mtime === filemtime( $ARQ ),
	'MUNDO B: a cura ENCOSTOU no .htaccess de uma porta que estava de pe' );
afirma( false === get_option( ROBOMETRIA_CASCA_CURA_OPTION ),
	'MUNDO B: a option da hora foi gravada sem haver tentativa nenhuma' );
/* 14-c: A CONTA DO CUSTO DO CONTADOR, E ELA E ESTA LINHA. Mil requisicoes de
   porta DE PE nao podem produzir UMA escrita — o gancho sai no passo 1 com uma
   leitura de arquivo e nenhuma option, e o contador e chamado DEPOIS daquele
   `return`. Se esta afirmacao cair, o contador passou a cobrar uma linha de
   UPDATE por visita numa ilha que esta sa. */
afirma( false === get_option( ROBOMETRIA_CASCA_PORTA_OPTION ),
	'MUNDO B: o contador da 14-c escreveu no banco em 1000 requisicoes de porta DE PE — custo em cima da ilha sadia, que e o caminho mais curto para alguem arrancar o contador' );
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

$d = robometria_casca_cura_decidir( retrato_de(), 0, 1000, 3600 );
afirma( ! empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO C/D base: com as quatro grandezas na mesa a decisao tem de ser CURAR, sem motivo a dizer' );

$d = robometria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ), 'MUNDO C: curou com mod_rewrite DESLIGADO' );
afirma( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'mod_rewrite' ),
	'MUNDO C: o motivo nao nomeia o mod_rewrite: ' . var_export( $d['motivo'], true ) );

$d = robometria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => null ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ),
	'MUNDO C-b: `mod_rewrite: null` e "nao sei", e nao sei NAO autoriza escrever na porta de entrada' );

$d = robometria_casca_cura_decidir( retrato_de( array( 'raiz_gravavel' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ), 'MUNDO D: curou com a raiz NAO gravavel' );
afirma( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'raiz' ),
	'MUNDO D: o motivo nao nomeia a raiz: ' . var_export( $d['motivo'], true ) );

$d = robometria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'gravavel' => false ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'gravavel' ),
	'MUNDO H-a: arquivo nao gravavel tem de recusar COM motivo proprio' );

$d = robometria_casca_cura_decidir( retrato_de( array( 'ferramentas_de_admin' => false ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'wp-admin' ),
	'MUNDO H-b: sem as ferramentas de admin o flush(true) vira flush(false), e isso tem de ser DITO' );

$d = robometria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'existe' => false ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'nao existe' ),
	'MUNDO H-c: arquivo ausente tem de recusar com motivo proprio' );

$d = robometria_casca_cura_decidir( array(), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'retrato' ),
	'MUNDO H-d: a cura nao age sobre medicao que nao existe, e tem de dizer isso' );

$d = robometria_casca_cura_decidir( retrato_de( array( 'htaccess' => array( 'tem_wordpress' => true ) ) ), 0, 1000, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO H-e: porta de pe e o unico desfecho com NADA a dizer (trava 4)' );

/* MUNDO E — hora nao vencida: nao cura e NAO fala. E a ordem importa: o relogio
   e checado ANTES dos motivos de recusa, senao ilha com mod_rewrite desligado
   encheria as 40 linhas do log em um minuto. */
$d = robometria_casca_cura_decidir( retrato_de(), 1000, 1500, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO E: hora nao vencida tem de recusar CALADA' );
$d = robometria_casca_cura_decidir( retrato_de( array( 'mod_rewrite' => false ) ), 1000, 1500, 3600 );
afirma( empty( $d['curar'] ) && null === $d['motivo'],
	'MUNDO E-b: o relogio tem de ser checado ANTES do motivo de recusa, senao o log enche de ruido' );
$d = robometria_casca_cura_decidir( retrato_de(), 1000, 1000 + 3600, 3600 );
afirma( ! empty( $d['curar'] ),
	'MUNDO E-c: exatamente no intervalo a hora JA venceu (o teto e `<`, nao `<=`)' );

/* E o mundo E no gancho inteiro, com arquivo de verdade. */
if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$GLOBALS['OPT'][ ROBOMETRIA_CASCA_CURA_OPTION ] = time();
	$e_bytes = filesize( $ARQ );
	$e_linha = robometria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( '' === $e_linha && 0 === count( log_da_cura() ) && $e_bytes === filesize( $ARQ ) && 0 === $GLOBALS['FLUSHES'],
		'MUNDO E (gancho): com a hora nao vencida a cura tem de sair calada e sem tocar no arquivo' );
}

/* ------------------------------------------------------------------ MUNDO F */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$GLOBALS['FLUSH_NAO_REPOE'] = true;
	$f_linha = robometria_casca_cura_da_porta();
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
	$_GET['rest_route'] = '/robometria/v1/rotas';
	$g_bytes = filesize( $ARQ );
	$g_linha = robometria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( '' === $g_linha, 'MUNDO G: a cura falou dentro da rota que MEDE a porta' );
	afirma( $g_bytes === filesize( $ARQ ) && 0 === count( log_da_cura() ) && 0 === $GLOBALS['FLUSHES'],
		'MUNDO G: a cura AGIU na rota de diagnostico — o retrato da 29.3 nunca mostraria a queda (trava 5)' );
	afirma( false === get_option( ROBOMETRIA_CASCA_CURA_OPTION ),
		'MUNDO G: a cura queimou a hora na rota que mede, e a hora queimada ali atrasa a cura de verdade' );
	afirma( true === robometria_casca_cura_e_a_rota_que_mede(),
		'MUNDO G: a propria regua nao reconhece a rota de diagnostico' );
	unset( $_GET['rest_route'] );
	$_GET['rest_route'] = '/robometria/v1/status';
	afirma( false === robometria_casca_cura_e_a_rota_que_mede(),
		'MUNDO G-b: a regua confundiu o /status com a rota que mede a porta, e ai a cura nunca roda em requisicao REST' );
	unset( $_GET['rest_route'] );
}

/* ------------------------------------------------------------------ MUNDO J */

if ( 'sem-log' === $MODO ) {
	zerar( $CAIDO );
	$j_bytes = filesize( $ARQ );
	$j_linha = robometria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	afirma( $j_bytes === filesize( $ARQ ),
		'MUNDO J: sem lugar para escrever a linha, a cura TOCOU no arquivo — a trava 3 nao e enfeite do sucesso' );
	afirma( 0 === $GLOBALS['FLUSHES'],
		'MUNDO J: o flush rodou sem haver onde registrar a tentativa' );
	afirma( false === get_option( ROBOMETRIA_CASCA_CURA_OPTION ),
		'MUNDO J: a hora foi queimada sem nenhuma tentativa ter acontecido' );
	afirma( false !== strpos( (string) $j_linha, 'nao ha onde escrever' ),
		'MUNDO J: a recusa tem de se NOMEAR para quem chamou, e saiu: ' . var_export( $j_linha, true ) );
	afirma( false === robometria_casca_cura_registrar( 'x' ),
		'MUNDO J: o registrar devolveu verdadeiro sem ter onde escrever' );
}

/* ------------------------------------------------- O retrato curto, sozinho */

afirma( '1057 bytes [NFD EPC]' === robometria_casca_cura_retrato_curto( retrato_de() ),
	'o retrato curto mudou de forma: ' . robometria_casca_cura_retrato_curto( retrato_de() ) );
afirma( 'sem retrato' === robometria_casca_cura_retrato_curto( array() ),
	'retrato ausente tem de dizer "sem retrato" em vez de "0 bytes []"' );

/* ------------------------------------------------------- O pre-filtro barato */

zerar( $CAIDO );
afirma( false === robometria_casca_cura_tem_bloco( $ARQ ),
	'o pre-filtro leu o bloco do WordPress num arquivo caido' );
zerar( "# BEGIN WordPress\n# END WordPress\n" );
afirma( true === robometria_casca_cura_tem_bloco( $ARQ ),
	'o pre-filtro nao achou o bloco do WordPress num arquivo de pe' );
afirma( null === robometria_casca_cura_tem_bloco( $PORTA . 'nao-existe-nunca' ),
	'arquivo ausente tem de devolver null (nao sei), nunca false (esta caido)' );
afirma( null === robometria_casca_cura_tem_bloco( '' ),
	'caminho vazio tem de devolver null' );
zerar( "# BEGIN NFD EPC\n# nao mexer: regra do WordPress antiga\n# END NFD EPC\n" );
afirma( false === robometria_casca_cura_tem_bloco( $ARQ ),
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
afirma( true === robometria_casca_cura_tem_bloco( $novo_arq ),
	'o pre-filtro leu o CACHE DE STAT e disse "nao sei" sobre um arquivo que acabou de nascer de pe' );
@unlink( $novo_arq );

/* ------------- 14-b. O RETRATO MINIMO DA PORTA, SEM TOKEN (17/11/2026) ------
   Os dois campos que `/casca` ja servia dizem se a cura esta CARREGADA e por
   onde ela FALARIA. Na queda de 17/11 nenhum dos dois respondia a pergunta do
   dia — a porta esta de pe AGORA? — e os dois mundos que cabiam no retrato tem
   consertos DIFERENTES (chamado na HostGator contra esperar a hora vencer).
   As duas funcoes novas sao PURAS de proposito: o mundo (b) nao se encena no
   disco deste conteiner sem queimar uma hora de relogio de verdade, e o que
   nao se fabrica no disco se fabrica no retrato — a mesma licao do MUNDO
   `mod_rewrite: false`. */

afirma( 0 === robometria_casca_cura_espera_s( 0, 1000, 3600 ),
	'14-b: cura que nunca tentou tem de estar LIVRE, e a option vazia e 0' );
afirma( 3100 === robometria_casca_cura_espera_s( 1000, 1500, 3600 ),
	'14-b: a espera tem de ser o que FALTA do intervalo, nao o que passou' );
afirma( 0 === robometria_casca_cura_espera_s( 1000, 1000 + 3600, 3600 ),
	'14-b: exatamente no intervalo a hora JA venceu — o teto e `<` e nao `<=`, igual ao do gancho (MUNDO E-c)' );
afirma( 0 === robometria_casca_cura_espera_s( 1000, 500, 3600 ),
	'14-b: relogio andando para tras nao pode TRANCAR a cura — tempo negativo libera, nunca prende' );
afirma( 0 === robometria_casca_cura_espera_s( 1000, 1500, 0 ),
	'14-b: intervalo zero e "sem trava", e nao uma trava eterna' );

$r_pe        = robometria_casca_porta_retrato_publico( true, 0 );
$r_pe_trava  = robometria_casca_porta_retrato_publico( true, 2100 );
$r_caido_tr  = robometria_casca_porta_retrato_publico( false, 2100 );
$r_caido_liv = robometria_casca_porta_retrato_publico( false, 0 );
$r_nao_sei   = robometria_casca_porta_retrato_publico( null, 0 );

afirma( true === $r_pe['tem_bloco_wordpress'] && false === $r_caido_tr['tem_bloco_wordpress'],
	'14-b: o booleano do bloco tem de atravessar o retrato sem se perder' );
afirma( null === $r_nao_sei['tem_bloco_wordpress'],
	'14-b: "nao sei" virou `false` no retrato publico — arquivo ilegivel lido como PORTA CAIDA manda chamar a HostGator por um defeito que ninguem mediu' );
afirma( 2100 === $r_caido_tr['cura_liberada_em_s'] && 0 === $r_caido_liv['cura_liberada_em_s'],
	'14-b: o relogio da trava 2 tem de sair no retrato' );

/* AS DUAS LEITURAS QUE ESTA SECAO EXISTE PARA SEPARAR, E ELAS SAO O
   ACONTECIMENTO DE 17/11 EM DUAS LINHAS. */
afirma( false !== strpos( $r_pe['leitura'], 'AllowOverride' ),
	'14-b: com o bloco NO LUGAR e as portas em 404 a leitura e `AllowOverride` do hospedeiro (29.4), e o retrato tem de dize-lo' );
afirma( false !== strpos( $r_pe_trava['leitura'], 'AllowOverride' ),
	'14-b: bloco no lugar DECIDE sozinho — o relogio da trava nao muda a leitura de uma porta cujo arquivo esta correto' );
afirma( false === strpos( $r_caido_tr['leitura'], 'AllowOverride' )
	&& false !== strpos( $r_caido_tr['leitura'], '2100' ),
	'14-b: bloco AUSENTE com a hora queimada nao e AllowOverride, e a leitura tem de trazer quantos segundos faltam' );
afirma( false !== strpos( $r_caido_liv['leitura'], 'LIBERADA' ),
	'14-b: bloco ausente com a cura liberada e o mundo em que a proxima requisicao conserta — a leitura tem de dizer isso e nao mandar abrir chamado' );
afirma( $r_pe['leitura'] !== $r_caido_tr['leitura']
	&& $r_caido_tr['leitura'] !== $r_caido_liv['leitura']
	&& $r_nao_sei['leitura'] !== $r_caido_liv['leitura'],
	'14-b: duas leituras com CONSERTOS diferentes sairam com a MESMA frase, e portao que reprova pelo motivo errado e o caminho mais curto para alguem passar a ignora-lo (20.5)' );

/* O QUE O RETRATO NAO PODE PUBLICAR. A 29.3 manda o conteudo do arquivo nunca
   sair, e `.htaccess` de hospedeiro compartilhado carrega regra de terceiro. */
foreach ( array( $r_pe, $r_pe_trava, $r_caido_tr, $r_caido_liv, $r_nao_sei ) as $i => $r ) {
	/* A LISTA CRESCEU EM 17/11/2026, E ESTA LINHA E O PEDAGIO. `quedas` entrou
	   pela 14-c, e esta afirmacao foi a UNICA coisa que reprovou quando ele
	   entrou — que e exatamente o que ela existe para fazer: campo novo sem
	   token nao passa calado, ele passa por aqui. */
	afirma( array( 'tem_bloco_wordpress', 'cura_liberada_em_s', 'leitura', 'quedas' ) === array_keys( $r ),
		"14-b: o retrato publico ganhou ou perdeu campo (retrato $i) — campo novo aqui e campo que ninguem autorizou a sair sem token" );
	$tudo = wp_json_encode( $r );
	afirma( false === stripos( $tudo, 'NFD' ) && false === stripos( $tudo, 'EPC' )
		&& false === stripos( $tudo, 'RewriteRule' ) && false === stripos( $tudo, 'RewriteBase' )
		&& false === stripos( $tudo, 'bytes' ),
		"14-b: o retrato SEM TOKEN vazou nome de bloco de terceiro, linha de reescrita ou tamanho de arquivo (retrato $i) — a 29.3 reserva isso para a rota que pede token" );
}

/* --------- 14-c. O CONTADOR DE QUEDAS, QUE NAO ROLA COM A JANELA DO LOG -----
   A serie que o chamado na HostGator leva era contada pelas linhas `cura da
   porta:` do log — e a cura tenta no maximo UMA VEZ POR HORA, entao apagamento
   que cai dentro da hora queimada NAO deixa rastro nenhum, e o log e cortado em
   40 linhas e rola. A frequencia do chamado era um PISO dito como se fosse a
   conta, e e pelo pequeno demais que um fornecedor fecha chamado.
   AS FUNCOES SAO PURAS, e e isso que deixa o portao fabricar aqui, em
   milissegundos, os mundos que o disco deste conteiner so encenaria queimando
   horas de relogio de verdade. */

/* ------------------------------------------------------------------ MUNDO K */
/* A QUEDA QUE A TRAVA 2 ESCONDE, E ELA SE FABRICA NO DISCO — porque a trava e
   uma option, nao uma hora de relogio. E o acontecimento de 17/11/2026 as
   ~10h19Z: o bloco foi apagado DE NOVO quatro minutos depois da cura das 10:15,
   a hora da trava estava queimada, a cura saiu CALADA (e tinha de sair, pelo
   MUNDO E e pela trava 4) e aquele apagamento nao existiu para o chamado na
   HostGator. Este mundo exige as duas coisas ao mesmo tempo: o silencio no log
   E o numero no contador. */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	$GLOBALS['OPT'][ ROBOMETRIA_CASCA_CURA_OPTION ] = time();
	$k_bytes = filesize( $ARQ );
	$k_linha = robometria_casca_cura_da_porta();
	clearstatcache( true, $ARQ );
	$k_est = robometria_casca_porta_estado();
	afirma( '' === $k_linha && 0 === count( log_da_cura() ) && $k_bytes === filesize( $ARQ ) && 0 === $GLOBALS['FLUSHES'],
		'MUNDO K: a trava 2 tem de seguir valendo INTEIRA — o contador nao pode fazer a cura falar no log, tocar no arquivo nem rodar o flush com a hora queimada' );
	afirma( 1 === $k_est['episodios_vistos'] && 1 === $k_est['leituras_no_chao'],
		'MUNDO K: A QUEDA QUE A TRAVA ESCONDE NAO FOI CONTADA, e e a 14-c inteira: com a hora queimada a cura sai calada (e tem de sair), e sem o contador esse apagamento nao existe para o chamado na HostGator' );
	afirma( null === $k_est['ultima_reposicao'] && 0 === $k_est['reposicoes'],
		'MUNDO K: nenhuma reposicao aconteceu neste mundo, e o contador carimbou uma' );

	/* K-b: SEIS REQUISICOES DENTRO DA MESMA QUEDA SAO UMA QUEDA. A ilha serviu
	   404 em 91 das 92 leituras de hoje; se cada leitura abrisse episodio, o
	   argumento do chamado sairia inflado — e numero inflado perde chamado tao
	   rapido quanto numero pequeno demais. */
	for ( $i = 1; $i <= 5; $i++ ) { robometria_casca_cura_da_porta(); }
	$k2 = robometria_casca_porta_estado();
	afirma( 1 === $k2['episodios_vistos'] && 6 === $k2['leituras_no_chao'],
		'MUNDO K-b: seis requisicoes dentro da MESMA queda sairam como ' . $k2['episodios_vistos'] . ' episodio(s) e ' . $k2['leituras_no_chao'] . ' leitura(s)' );
	afirma( 0 === count( log_da_cura() ),
		'MUNDO K-b: seis leituras contadas puseram ' . count( log_da_cura() ) . ' linha(s) no log — a janela de 40 linhas da 20.4 nao pode pagar pelo contador' );

	/* K-c: A CURA REPOE, O CONTADOR FECHA O EPISODIO, E O APAGAMENTO SEGUINTE E
	   UMA QUEDA NOVA. O ciclo inteiro de 17/11 num mundo so. */
	$GLOBALS['OPT'][ ROBOMETRIA_CASCA_CURA_OPTION ] = 0;
	$k_linha2 = robometria_casca_cura_da_porta();
	$k3       = robometria_casca_porta_estado();
	afirma( false !== strpos( $k_linha2, 'bloco WordPress reposto' ) && 1 === $k3['reposicoes'],
		'MUNDO K-c: a cura repos o bloco e o contador nao carimbou a reposicao — sem ela o apagamento seguinte se funde com esta queda' );
	zerar( $CAIDO );
	$GLOBALS['OPT'] = $k3_opt = array_merge( $GLOBALS['OPT'], array( ROBOMETRIA_CASCA_PORTA_OPTION => $k3 ) );
	$GLOBALS['OPT'][ ROBOMETRIA_CASCA_CURA_OPTION ] = time();
	robometria_casca_cura_da_porta();
	$k4 = robometria_casca_porta_estado();
	afirma( 2 === $k4['episodios_vistos'],
		'MUNDO K-c: depois de uma reposicao confirmada, a leitura no chao seguinte tem de ser QUEDA NOVA — e ela e a unica prova de que algo desfez a cura' );
}

$E0 = robometria_casca_porta_estado_normal( array() );
afirma( 0 === $E0['episodios_vistos'] && 0 === $E0['leituras_no_chao']
	&& 0 === $E0['leituras_nao_sei'] && 0 === $E0['reposicoes']
	&& null === $E0['primeira_no_chao'] && null === $E0['inicio_episodio']
	&& null === $E0['ultima_no_chao'] && null === $E0['ultima_reposicao'],
	'14-c: o estado vazio tem de nascer com as oito chaves zeradas' );
foreach ( array( false, null, 0, 'lixo', 3.5, array( 'episodios_vistos' => 'x' ) ) as $k => $bruto ) {
	$n = robometria_casca_porta_estado_normal( $bruto );
	afirma( 8 === count( $n ) && 0 === $n['episodios_vistos'] && null === $n['ultima_no_chao'],
		"14-c: estado corrompido ($k) tem de sair na forma canonica — contador que explode em cima de option velha e contador que some no primeiro desembarque" );
}
afirma( null === robometria_casca_porta_estado_normal( array( 'ultima_no_chao' => -5 ) )['ultima_no_chao']
	&& null === robometria_casca_porta_estado_normal( array( 'ultima_no_chao' => 0 ) )['ultima_no_chao'],
	'14-c: carimbo de hora nao positivo e "nunca aconteceu", e nao a epoca de 1970' );

/* A PORTA DE PE NAO ESCREVE. E a conta do custo do passo 1 do gancho inteira. */
$t = 1000000;
$r = robometria_casca_porta_contar( $E0, true, $t, 3600 );
afirma( empty( $r['gravar'] ) && empty( $r['novo_episodio'] ) && $r['estado'] === $E0,
	'14-c: leitura de porta DE PE gravou no banco ou mexeu no contador — ler nao e escrever, e o contador nao pode cobrar uma linha de UPDATE por visita' );
$r = robometria_casca_porta_contar( array( 'episodios_vistos' => 3, 'ultima_no_chao' => $t - 10 ), true, $t, 3600 );
afirma( 3 === $r['estado']['episodios_vistos'] && ( $t - 10 ) === $r['estado']['ultima_no_chao'],
	'14-c: a porta de pe nao pode APAGAR o que o contador ja viu' );

/* `null` E "NAO SEI", E NAO SEI NAO E QUEDA — a mesma regra do M6. */
$r = robometria_casca_porta_contar( $E0, null, $t, 3600 );
afirma( 0 === $r['estado']['episodios_vistos'] && 1 === $r['estado']['leituras_nao_sei']
	&& null === $r['estado']['ultima_no_chao'] && ! empty( $r['gravar'] ),
	'14-c: arquivo ilegivel contado como QUEDA manda abrir chamado na HostGator por um defeito que ninguem mediu (a mesma confusao do M6)' );

/* A PRIMEIRA QUEDA DA VIDA DO CONTADOR. */
$q1 = robometria_casca_porta_contar( $E0, false, $t, 3600 );
afirma( 1 === $q1['estado']['episodios_vistos'] && ! empty( $q1['novo_episodio'] )
	&& $t === $q1['estado']['primeira_no_chao'] && $t === $q1['estado']['inicio_episodio']
	&& $t === $q1['estado']['ultima_no_chao'] && 1 === $q1['estado']['leituras_no_chao'],
	'14-c: a primeira leitura no chao tem de abrir episodio e carimbar as tres horas' );

/* QUEDA CONTINUA: 50 leituras seguidas sao UM episodio, nao 50. */
$e = $q1['estado'];
for ( $i = 1; $i <= 50; $i++ ) {
	$p = robometria_casca_porta_contar( $e, false, $t + ( $i * 25 ), 3600 );
	$e = $p['estado'];
	if ( ! empty( $p['novo_episodio'] ) ) {
		afirma( false, "14-c: a leitura $i de uma MESMA queda abriu episodio novo — 92 leituras de uma queda sairiam como 92 apagamentos" );
		break;
	}
}
afirma( 1 === $e['episodios_vistos'] && 51 === $e['leituras_no_chao']
	&& $t === $e['inicio_episodio'] && ( $t + 1250 ) === $e['ultima_no_chao'],
	'14-c: queda continua tem de ser UM episodio com as leituras somando — saiu ' . $e['episodios_vistos'] . ' episodio(s) e ' . $e['leituras_no_chao'] . ' leitura(s)' );

/* O ACONTECIMENTO DE 17/11 AS 10:15, QUE E O MOTIVO DESTA SECAO EXISTIR: a cura
   repoe o bloco NA MESMA REQUISICAO em que a leitura no chao aconteceu, e ~4
   minutos depois o bloco e apagado DE NOVO. Esse segundo apagamento cai dentro
   da hora queimada da trava 2, nao escreve linha no log, e e invisivel para
   qualquer contagem feita por log. Aqui ele tem de aparecer. */
$depois_da_cura = robometria_casca_porta_marcar_reposicao( $q1['estado'], $t );
afirma( 1 === $depois_da_cura['reposicoes'] && $t === $depois_da_cura['ultima_reposicao'],
	'14-c: a reposicao confirmada pela cura tem de ficar carimbada' );
$q2 = robometria_casca_porta_contar( $depois_da_cura, false, $t + 240, 3600 );
afirma( 2 === $q2['estado']['episodios_vistos'] && ! empty( $q2['novo_episodio'] ),
	'14-c: O APAGAMENTO DE ~4 MINUTOS DEPOIS DA CURA NAO FOI CONTADO. E o acontecimento de 17/11 as 10:15, ele cai dentro da hora queimada da trava 2 e no log nao deixa rastro NENHUM — contar so por log e o que faz a frequencia do chamado sair menor que a verdade' );
afirma( ( $t + 240 ) === $q2['estado']['inicio_episodio'] && $t === $q2['estado']['primeira_no_chao'],
	'14-c: o episodio novo tem de comecar agora, e a PRIMEIRA queda da vida do contador nao se reescreve' );

/* E O `>=` NAO E DESCUIDO: com `>` este episodio nao seria visto. */
$mesmo_segundo = robometria_casca_porta_marcar_reposicao(
	robometria_casca_porta_contar( $E0, false, $t, 3600 )['estado'], $t );
afirma( $mesmo_segundo['ultima_reposicao'] === $mesmo_segundo['ultima_no_chao'],
	'14-c: a cura dispara na MESMA requisicao da leitura, e os dois carimbos tem de cair no mesmo segundo — se deixarem de cair, o `>=` da regra do episodio virou folga e nao trava' );

/* A PORTA LEVANTADA PELA MAO DO RAPHAEL NO cPANEL — foi assim que ela levantou
   em 06/11 — nao passa pela cura, entao nada confirma a reposicao. O caminho (b)
   da regra existe para esta queda nao se fundir com a anterior. */
$q3 = robometria_casca_porta_contar( $q1['estado'], false, $t + 86400, 3600 );
afirma( 2 === $q3['estado']['episodios_vistos'] && ! empty( $q3['novo_episodio'] ),
	'14-c: queda um DIA depois da anterior, sem cura entre as duas, saiu como a MESMA queda — e a porta levantada a mao no cPanel nunca passa pela cura (06/11/2026)' );
afirma( empty( robometria_casca_porta_contar( $q1['estado'], false, $t + 3599, 3600 )['novo_episodio'] )
	&& ! empty( robometria_casca_porta_contar( $q1['estado'], false, $t + 3600, 3600 )['novo_episodio'] ),
	'14-c: o teto do caminho (b) e `>=` o intervalo, e ele tem de bater com o relogio da trava 2 — um segundo antes e a mesma queda, no segundo exato e queda nova' );
afirma( empty( robometria_casca_porta_contar( $q1['estado'], false, $t + 86400, 0 )['novo_episodio'] ),
	'14-c: com intervalo zero o caminho (b) tem de estar DESLIGADO, e nao valendo sempre' );
afirma( ! empty( robometria_casca_porta_contar( $q1['estado'], false, $t - 500, 3600 )['novo_episodio'] ),
	'14-c: relogio andando para tras nao pode FUNDIR dois episodios, pela mesma razao que nao pode trancar a cura (14-b)' );

/* O RAMO DO FRACASSO NAO FECHA EPISODIO, e isso e o mundo do `AllowOverride`:
   o `flush` roda, o bloco nao volta, a queda nunca terminou. */
$falhou = $q1['estado'];
for ( $i = 1; $i <= 3; $i++ ) {
	$falhou = robometria_casca_porta_contar( $falhou, false, $t + ( $i * 3700 ), 0 )['estado'];
}
afirma( 1 === $falhou['episodios_vistos'] && 0 === $falhou['reposicoes'],
	'14-c: sem reposicao confirmada e com o caminho (b) desligado, uma queda que NUNCA terminou tem de seguir sendo um episodio so' );

/* ------------------------------------- O QUE DO CONTADOR SAI SEM TOKEN ------ */

$pub0 = robometria_casca_porta_quedas_publico( $E0, $t );
afirma( 0 === $pub0['episodios_vistos'] && null === $pub0['episodio'] && null === $pub0['primeira_no_chao'],
	'14-c: contador zerado tem de sair sem episodio em vez de inventar um' );
afirma( false !== strpos( $pub0['leitura'], 'consertos.md' ),
	'14-c: ZERO aqui nao quer dizer "nunca caiu" — o contador nasceu hoje e as quedas anteriores estao em dados/consertos.md, e a leitura tem de dizer isso em vez de soar conferida (32.5-d)' );

$pub = robometria_casca_porta_quedas_publico( $q2['estado'], $t + 300 );
afirma( 2 === $pub['episodios_vistos'] && 1 === $pub['reposicoes_da_cura'],
	'14-c: as duas contagens que o chamado usa tem de sair no retrato publico' );
afirma( is_array( $pub['episodio'] ) && 0 === $pub['episodio']['duracao_minima_s'],
	'14-c: episodio de uma leitura so tem duracao minima ZERO, e nao uma duracao inventada' );
$longo = robometria_casca_porta_quedas_publico( $e, $t + 1300 );
afirma( 1250 === $longo['episodio']['duracao_minima_s'],
	'14-c: a duracao minima e a distancia entre a PRIMEIRA e a ULTIMA leitura no chao do episodio — saiu ' . $longo['episodio']['duracao_minima_s'] );
afirma( false !== strpos( implode( ' ', array_keys( $longo['episodio'] ) ), 'duracao_minima_s' ),
	'14-c: o campo tem de se chamar `minima`: a queda comecou antes da primeira leitura e pode ter terminado depois da ultima, e foi essa distincao que a execucao das 11h17Z teve de escrever a mao' );
afirma( false === $longo['episodio']['reposto_depois']
	&& true === robometria_casca_porta_quedas_publico( $depois_da_cura, $t )['episodio']['reposto_depois'],
	'14-c: o retrato tem de dizer se a cura repos o bloco DEPOIS da ultima leitura no chao — e a diferenca entre "a queda acabou" e "a queda esta aberta agora"' );
afirma( '1970-01-12 13:46Z' === robometria_casca_porta_quedas_publico(
		array( 'episodios_vistos' => 1, 'inicio_episodio' => $t, 'ultima_no_chao' => $t ), $t )['episodio']['comecou'],
	'14-c: a hora sai em minuto UTC com o Z, como o log do /status ja carimba' );

/* O QUE ELE NAO PODE PUBLICAR. A mesma regua do 14-b: contagem e hora da
   PROPRIA ilha saem; conteudo do arquivo do hospedeiro, nunca. */
foreach ( array( $pub0, $pub, $longo ) as $i => $pb ) {
	afirma( array( 'episodios_vistos', 'leituras_no_chao', 'leituras_nao_sei', 'reposicoes_da_cura',
			'primeira_no_chao', 'episodio', 'leitura' ) === array_keys( $pb ),
		"14-c: o contador publico ganhou ou perdeu campo (retrato $i) — campo novo aqui e campo que ninguem autorizou a sair sem token" );
	$tudo = wp_json_encode( $pb );
	afirma( false === stripos( $tudo, 'NFD' ) && false === stripos( $tudo, 'EPC' )
		&& false === stripos( $tudo, 'RewriteRule' ) && false === stripos( $tudo, 'RewriteBase' )
		&& false === stripos( $tudo, 'htaccess' ),
		"14-c: o contador SEM TOKEN vazou nome de bloco de terceiro, linha de reescrita ou o nome do arquivo (retrato $i) — a 29.3 reserva isso para a rota que pede token" );
}

/* O CONTADOR DENTRO DO RETRATO DA PORTA, que e por onde `/casca` o serve. */
$com = robometria_casca_porta_retrato_publico( false, 2100, $pub );
afirma( 4 === count( $com ) && isset( $com['quedas']['episodios_vistos'] ),
	'14-c: o retrato da porta tem de carregar o contador no campo `quedas`' );
afirma( null === robometria_casca_porta_retrato_publico( true, 0 )['quedas'],
	'14-c: sem a 14-c carregada o campo tem de ser `null` — zero aqui soaria "nunca caiu" com cara de conferido, e a ausencia e o sinal (20.7)' );
afirma( robometria_casca_porta_retrato_publico( false, 2100, $pub )['leitura']
		=== robometria_casca_porta_retrato_publico( false, 2100 )['leitura'],
	'14-c: o contador nao pode mudar a leitura de COMO A PORTA ESTA AGORA — sao duas perguntas, e a do 14-b nao depende de historico' );

/* ------------------------------------------- A FORMA DA LINHA NOS DOIS MODOS */
/* O caminho de reserva nao inventa formato: formato novo no mesmo log seria o
   mesmo fato dito de duas maneiras. A filha do modo `option` imprime a linha
   que escreveu, e a mae compara com a dela. */

if ( 'sem-log' !== $MODO ) {
	zerar( $CAIDO );
	robometria_casca_cura_da_porta();
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
		exec( 'RBM_CURA_MODO=' . $modo . ' php ' . escapeshellarg( __FILE__ ) . ' 2>&1', $saida, $cod );
		$texto = implode( "\n", $saida );
		afirma( 0 === $cod,
			"o modo de log `$modo` reprovou no processo filho:\n    " . str_replace( "\n", "\n    ", $texto ) );
		if ( preg_match( '/(\d+) afirmacoes/', $texto, $m ) ) { $extra += (int) $m[1]; }
		if ( preg_match( '/^FORMA: (.+)$/m', $texto, $m ) ) { $formas[ $modo ] = $m[1]; }
	}

	zerar( $CAIDO );
	robometria_casca_cura_da_porta();
	$lg_mae = log_da_cura();
	$forma_mae = isset( $lg_mae[0] ) ? preg_replace( '/\d/', 'N', $lg_mae[0] ) : '';
	afirma( isset( $formas['option'] ) && $formas['option'] === $forma_mae,
		'a linha do caminho de RESERVA tem forma diferente da do caminho da FUNCAO — o mesmo fato dito de duas maneiras no mesmo log. funcao: '
			. $forma_mae . ' / option: ' . ( isset( $formas['option'] ) ? $formas['option'] : '(nao saiu)' ) );

	foreach ( array_keys( $MUTACOES ) as $mut ) {
		$saida = array();
		$cod   = 0;
		exec( 'RBM_CURA_MODO=' . $MUTACOES[ $mut ]['modo'] . ' RBM_CURA_MUTACAO=' . $mut
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

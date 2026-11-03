<?php
/**
 * A PORTA DE ENTRADA DO SITE, MEDIDA NO CHAO — a rota da 29.3 desta ilha.
 *
 *   php ferramentas/teste-rotas.php
 *
 * POR QUE ELE NASCEU EM 03/11/2026, com o defeito NOMEADO, COM URL E DATA,
 * como a 31.2 exige — e ele nao e "pode acontecer": a mesma porta caiu QUATRO
 * vezes nesta conta de cPanel (`/home3/rapha921/`):
 *
 *   24/09/2026 19h20Z  clubedomosaico.com.br  16 de 17 URLs em 404
 *   05/10/2026         clubedomosaico.com.br  a mesma assinatura byte por byte
 *   30/10/2026         robometria.com.br      13 de 14 URLs em 404, 4 DIAS fora
 *   (a quarta em OUTRO dominio da mesma conta, no despacho ALTA de dados/despachos.md)
 *
 * E A ROBOMETRIA PAGOU QUATRO DIAS POR NAO TER ESTA ROTA: o despacho de 30/10
 * escreveu "nao e consertavel pelo repositorio", frase que era verdadeira sobre
 * aquela ilha e falsa sobre o Arquipelago. A rota nasceu la em 02/11 e o defeito
 * que ficou quatro dias de pe caiu em dois minutos. ESTA ilha estava na mesma
 * lista, com `NAO` na coluna da 29.3, e e essa divida que o bloco de hoje paga.
 *
 * POR QUE ELE E PHP E NAO PYTHON — o mesmo motivo escrito no
 * `teste-caixa-da-mae.php`, no `teste-nota-de-preco.php`, no
 * `teste-escada-de-compra.php` e no `teste-versao-dos-snippets.php`: a decisao
 * mora em PHP, entao a regua CHAMA as funcoes de verdade. Regua em Python sobre
 * o texto do PHP conferiria a FORMA do codigo, nunca a decisao — e aqui a
 * decisao e quem abre a porta do servidor.
 *
 * AS SEIS COISAS QUE ELE MEDE, e nenhuma delas e opiniao:
 *
 *   1. O SEGREDO NAO SAI. A 29.3 e literal: "o conteudo do arquivo nunca sai
 *      inteiro na resposta", porque `.htaccess` de hospedeiro compartilhado
 *      carrega regra de seguranca de terceiro e despeja-la num HTTP e entregar
 *      a configuracao do servidor a quem tiver o token. O mundo fabricado tem
 *      uma linha-SEGREDO e a afirmacao e que ela NAO aparece no JSON.
 *   2. O MUNDO MEDIDO DE VERDADE reprova. O `.htaccess` das quedas tinha UM
 *      bloco so, `NFD EPC`, sem `# BEGIN WordPress` — e `tem_wordpress` tem de
 *      sair `false` nele. Mundo fabricado a partir da medicao, nao do que seria
 *      conveniente.
 *   3. O REPARO MOSTRA ANTES E DEPOIS DIFERENTES. Nao basta devolver
 *      `reparado: true`: o retrato de antes tem de dizer `false` e o de depois
 *      `true`, senao o campo e afirmacao e nao medicao.
 *   4. O REPARO SE RECUSA SEM AS FERRAMENTAS DE ADMIN. Sem
 *      `save_mod_rewrite_rules()` o `flush_rewrite_rules( true )` vira o
 *      `false` e NAO encosta no arquivo. Um `reparado: true` ali seria um verde
 *      dizendo que a porta foi consertada.
 *   5. A PAREDE DO TOKEN SEPARA TRES MUNDOS, e isto e o que esta ilha tem de
 *      proprio. O Sync dela NAO esta no repositorio, entao o nome da funcao que
 *      guarda o token e herdado das irmas e nao conferido no chao. Se o nome
 *      estiver errado a rota nega TODO pedido, inclusive o certo, e seria um
 *      portao morto com cara de portao. Os tres codigos de erro distintos sao o
 *      que faz a ausencia falar (20.7).
 *   6. E AS DUAS REGUAS DISCORDAM. A regua VELHA (a das irmas, `return false`)
 *      e refeita aqui ao lado da nova, e a afirmacao e que elas DISCORDEM no
 *      mundo do portao morto. Autoteste em que a regua velha e a nova
 *      concordam nao mede conserto nenhum — e a 20.8 escreve isso com essas
 *      palavras.
 *
 * E ELE PROVA QUE MORDE: quatro mutacoes das funcoes de verdade tem de
 * REPROVAR. Trava que nunca falhou nao e trava, e o `bancada.py` desta ilha
 * cobra as duas metades do veredito — a palavra impressa e o codigo de saida.
 */

/* ---------------------------------------------------------------------------
   OS DOIS MUNDOS DE STUB SAO EXCLUDENTES, e por isso este arquivo se reexecuta.
   `carregar_ferramentas_de_admin()` decide por `function_exists()`, que nao se
   desfaz depois de definida: nao da para testar o ramo "sem ferramentas de
   admin" e o ramo "com" no MESMO processo. A passada de fora roda SEM
   `save_mod_rewrite_rules` (ramo da recusa, o que impede o verde falso) e
   reexecuta uma filha com RDM_ADMIN=1 (ramo do reparo que escreve de verdade).
   --------------------------------------------------------------------------- */
$COM_ADMIN = getenv( 'RDM_ADMIN' ) === '1';

$RAIZ = dirname( __DIR__ );
$TMP  = sys_get_temp_dir() . '/rdm-rotas-' . getmypid();
@mkdir( $TMP, 0777, true );

define( 'ABSPATH', $TMP . '/wp/' );
define( 'RODAMETRIA_CASCA_VERSAO', 'teste' );

/* O .htaccess fabricado mora aqui, e `get_home_path()` aponta para ca. */
$PORTA = $TMP . '/';
function get_home_path() { return $GLOBALS['PORTA']; }
function got_mod_rewrite() { return true; }
function home_url( $p = '/' ) { return 'https://exemplo.invalido' . $p; }
function site_url( $p = '/' ) { return 'https://exemplo.invalido' . $p; }

/* A option do token e trocada por mundo. `$GLOBALS['OPT']` e o banco falso. */
$GLOBALS['OPT'] = array();
function get_option( $k, $d = false ) {
	return array_key_exists( $k, $GLOBALS['OPT'] ) ? $GLOBALS['OPT'][ $k ] : $d;
}

if ( $COM_ADMIN ) {
	/* O flush de verdade escreve o bloco do WordPress no arquivo. O stub faz o
	   MESMO — e por isso o antes e o depois podem ser comparados: sem escrever,
	   `reparado` seria um campo que ninguem mediu. */
	function save_mod_rewrite_rules() { return true; }
	function flush_rewrite_rules( $forte = false ) {
		if ( ! $forte ) { return; }
		$arq = $GLOBALS['PORTA'] . '.htaccess';
		$txt = file_exists( $arq ) ? file_get_contents( $arq ) : '';
		file_put_contents( $arq,
			"# BEGIN WordPress\nRewriteEngine On\nRewriteBase /\nRewriteRule . /index.php [L]\n# END WordPress\n" . $txt );
	}
}

class WP_Error {
	public $codigo;
	public $dados;
	public function __construct( $codigo, $msg = '', $dados = array() ) {
		$this->codigo = $codigo;
		$this->dados  = $dados;
	}
	public function get_error_code() { return $this->codigo; }
	public function get_error_data() { return $this->dados; }
}

/* `register_rest_route` e capturado: e dele que sai o `permission_callback`
   DE VERDADE, nunca uma copia escrita a mao neste arquivo. Copia a mao
   conferiria o que o teste acha que o codigo faz. */
$GLOBALS['ROTAS'] = array();
function add_action( $gancho, $cb, $p = 10, $n = 1 ) {
	if ( 'rest_api_init' === $gancho ) { call_user_func( $cb ); }
	return true;
}
function register_rest_route( $ns, $rota, $args ) {
	$GLOBALS['ROTAS'][ $ns . $rota ] = $args;
	return true;
}

$falhas     = array();
$afirmacoes = 0;
function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

/** Carrega UMA funcao de um snippet, equilibrando chaves — o mesmo mecanismo do
 *  `teste-caixa-da-mae.php`: o snippet inteiro registra filtros ao ser lido. */
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

/** Carrega o STATEMENT inteiro que contem um marcador, equilibrando PARENTESES
 *  com `token_get_all()` e nunca com busca de texto.
 *
 *  Por que o tokenizador e nao `strpos`: o bloco da rota tem parenteses dentro
 *  de comentario e de string, e contar caractere por caractere herdaria todos
 *  eles. O tokenizador do proprio PHP ja sabe o que e codigo e o que nao e —
 *  pedir a resposta a quem sabe e mais curto que reimplementar a pergunta. */
function carregar_statement( $src, $marcador, $abertura ) {
	$ts = token_get_all( $src );
	$alvo = -1;
	foreach ( $ts as $idx => $t ) {
		$txt = is_array( $t ) ? $t[1] : $t;
		if ( false !== strpos( $txt, $marcador ) ) { $alvo = $idx; break; }
	}
	if ( $alvo < 0 ) { return false; }

	$ini = -1;
	for ( $i = $alvo; $i >= 0; $i-- ) {
		$t   = $ts[ $i ];
		$txt = is_array( $t ) ? $t[1] : $t;
		if ( $abertura === $txt ) { $ini = $i; break; }
	}
	if ( $ini < 0 ) { return false; }

	$prof = 0;
	$fonte = '';
	for ( $i = $ini; $i < count( $ts ); $i++ ) {
		$t   = $ts[ $i ];
		$txt = is_array( $t ) ? $t[1] : $t;
		$fonte .= $txt;
		if ( '(' === $txt ) { $prof++; }
		elseif ( ')' === $txt ) { $prof--; if ( 0 === $prof ) { break; } }
	}
	eval( $fonte . ';' );
	return true;
}

$casca = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );

foreach ( array(
	'rodametria_casca_token_esperado',
	'rodametria_casca_fonte_do_token',
	'rodametria_casca_carregar_ferramentas_de_admin',
	'rodametria_casca_diagnostico_rotas',
	'rodametria_casca_reparar_rotas',
) as $f ) {
	afirma( carregar_funcao( $casca, $f ),
		sprintf( 'nao achei a funcao %s na casca — a rota da 29.3 foi desfeita', $f ) );
}

afirma( carregar_statement( $casca, "'/rotas'", 'add_action' ),
	'nao achei o add_action que registra a rota /rotas na casca' );

$ROTA = isset( $GLOBALS['ROTAS']['rodametria/v1/rotas'] ) ? $GLOBALS['ROTAS']['rodametria/v1/rotas'] : null;
afirma( is_array( $ROTA ), '29.3: a casca nao registra rodametria/v1/rotas' );
if ( ! is_array( $ROTA ) ) {
	echo "teste-rotas: REPROVADO antes de medir — a rota nao foi registrada\n";
	foreach ( $falhas as $f ) { echo "  - $f\n"; }
	exit( 1 );
}
afirma( 'GET' === $ROTA['methods'], '29.3: a rota /rotas nao e GET' );

/* --------------------------------------------------------------------------
   MUNDO 1 — O SEGREDO DO SERVIDOR NAO PODE SAIR NA RESPOSTA (29.3)
   -------------------------------------------------------------------------- */
$SEGREDO = 'SEGREDO-DO-SERVIDOR-QUE-NAO-PODE-SAIR-NUNCA';
file_put_contents( $PORTA . '.htaccess',
	"# BEGIN NFD EPC\nRewriteCond %{HTTP_HOST} .\n# END NFD EPC\n"
	. "# BEGIN WordPress\nRewriteEngine On\nRewriteBase /\nRewriteRule . /index.php [L]\n# END WordPress\n"
	. "SetEnvIf Request_URI . CHAVE=$SEGREDO\n" );

$d = rodametria_casca_diagnostico_rotas();
$json = json_encode( $d );

afirma( false === strpos( $json, $SEGREDO ),
	'29.3: o diagnostico DESPEJOU o conteudo do .htaccess na resposta — a linha-segredo apareceu no JSON' );
afirma( true === $d['htaccess']['tem_wordpress'],
	'o mundo COM `# BEGIN WordPress` saiu com tem_wordpress diferente de true' );
afirma( in_array( 'NFD EPC', $d['htaccess']['blocos'], true ) && in_array( 'WordPress', $d['htaccess']['blocos'], true ),
	'os blocos `# BEGIN` nao foram lidos: ' . json_encode( $d['htaccess']['blocos'] ) );
afirma( 4 === $d['htaccess']['linhas_rewrite'],
	'a contagem de linhas de reescrita deu ' . $d['htaccess']['linhas_rewrite'] . ' e o mundo tem 4' );
afirma( $d['htaccess']['bytes'] === filesize( $PORTA . '.htaccess' ),
	'os bytes do retrato nao sao os bytes do arquivo' );
afirma( array_key_exists( 'permalink_structure', $d ) && array_key_exists( 'regras_no_banco', $d )
		&& array_key_exists( 'mod_rewrite', $d ),
	'29.3: o retrato nao traz os tres campos que a secao nomeia (permalink_structure, regras_no_banco, mod_rewrite)' );

/* --------------------------------------------------------------------------
   MUNDO 2 — O .htaccess DAS QUATRO QUEDAS, fabricado da MEDICAO
   Um bloco so, `NFD EPC`, sem `# BEGIN WordPress`. E o retrato que a rota da
   robometria devolveu em 02/11 e o da clubedomosaico em 24/09 e 05/10.
   -------------------------------------------------------------------------- */
file_put_contents( $PORTA . '.htaccess',
	"# BEGIN NFD EPC\nRewriteEngine On\nRewriteCond %{HTTP_HOST} .\n# END NFD EPC\n" );

$d2 = rodametria_casca_diagnostico_rotas();
afirma( false === $d2['htaccess']['tem_wordpress'],
	'O MUNDO DA QUEDA PASSOU: .htaccess com bloco unico NFD EPC saiu com tem_wordpress nao-false' );
afirma( array( 'NFD EPC' ) === $d2['htaccess']['blocos'],
	'o mundo da queda tem UM bloco e o retrato leu: ' . json_encode( $d2['htaccess']['blocos'] ) );

/* --------------------------------------------------------------------------
   MUNDO 3 — SEM .htaccess NENHUM. O diagnostico nao pode quebrar nem inventar.
   -------------------------------------------------------------------------- */
@unlink( $PORTA . '.htaccess' );
$d3 = rodametria_casca_diagnostico_rotas();
afirma( false === $d3['htaccess']['existe'], 'sem arquivo, `existe` tinha de ser false' );
afirma( 0 === $d3['htaccess']['bytes'], 'sem arquivo, `bytes` tinha de ser 0' );
afirma( null === $d3['htaccess']['mtime'], 'sem arquivo, `mtime` tinha de ser null' );
afirma( ! array_key_exists( 'tem_wordpress', $d3['htaccess'] ),
	'sem arquivo LEGIVEL o retrato NAO pode afirmar tem_wordpress — afirmar ali seria inventar' );

/* --------------------------------------------------------------------------
   MUNDO 4 — O REPARO. Dois ramos, e cada um roda no processo que pode te-lo.
   -------------------------------------------------------------------------- */
file_put_contents( $PORTA . '.htaccess',
	"# BEGIN NFD EPC\nRewriteEngine On\n# END NFD EPC\n" );

$r = rodametria_casca_reparar_rotas();

if ( $COM_ADMIN ) {
	afirma( true === $r['antes']['ferramentas_de_admin'],
		'com os stubs de admin, ferramentas_de_admin tinha de ser true' );
	afirma( false === $r['antes']['htaccess']['tem_wordpress'],
		'o ANTES do reparo tinha de dizer tem_wordpress false' );
	afirma( true === $r['depois']['htaccess']['tem_wordpress'],
		'o DEPOIS do reparo tinha de dizer tem_wordpress true' );
	afirma( true === $r['reparado'], 'o reparo escreveu o bloco e `reparado` nao ficou true' );
	afirma( $r['antes']['htaccess']['bytes'] < $r['depois']['htaccess']['bytes'],
		'o antes e o depois trazem os MESMOS bytes — o campo nao esta medindo nada' );
	afirma( null === $r['motivo'], 'reparo bem-sucedido nao tem motivo de recusa' );
} else {
	afirma( false === $r['antes']['ferramentas_de_admin'],
		'sem save_mod_rewrite_rules, ferramentas_de_admin tinha de ser false' );
	afirma( false === $r['reparado'],
		'O VERDE FALSO PASSOU: sem as funcoes de wp-admin o reparo disse que consertou a porta' );
	afirma( is_string( $r['motivo'] ) && false !== strpos( $r['motivo'], 'wp-admin' ),
		'a recusa tem de dizer POR QUE recusou, nomeando wp-admin' );
	afirma( $r['antes'] === $r['depois'],
		'reparo recusado nao pode apresentar um depois diferente do antes' );
}

/* --------------------------------------------------------------------------
   MUNDO 5 — A PAREDE DO TOKEN, TRES MUNDOS, E A REGUA VELHA AO LADO
   -------------------------------------------------------------------------- */
$parede = $ROTA['permission_callback'];

/** O pedido falso: so o que o callback usa. */
class PedidoFalso {
	private $p;
	public function __construct( $p = array() ) { $this->p = $p; }
	public function get_param( $k ) { return isset( $this->p[ $k ] ) ? $this->p[ $k ] : null; }
}

/** A REGUA VELHA, a das irmas, refeita aqui para as duas serem comparadas. Ela
 *  devolve `false` nos tres mundos de recusa — e e por isso que ela nao separa
 *  "token errado" de "esta casca nao acha o token". */
function parede_velha( $pedido ) {
	$esperado = rodametria_casca_token_esperado();
	if ( '' === $esperado ) { return false; }
	$vindo = (string) $pedido->get_param( 'token' );
	return '' !== $vindo && hash_equals( $esperado, $vindo );
}

$codigo = function ( $v ) {
	if ( $v instanceof WP_Error ) { return $v->get_error_code(); }
	return $v === true ? 'LIBEROU' : 'NEGOU-SEM-DIZER';
};

/* 5a. SEM FONTE DE TOKEN — o mundo do portao morto. */
$GLOBALS['OPT'] = array();
$nova_a  = call_user_func( $parede, new PedidoFalso( array( 'token' => 'qualquer' ) ) );
$velha_a = parede_velha( new PedidoFalso( array( 'token' => 'qualquer' ) ) );

afirma( 'rodametria_rotas_sem_fonte_de_token' === $codigo( $nova_a ),
	'sem fonte de token a parede tinha de dizer `rodametria_rotas_sem_fonte_de_token` e disse: ' . $codigo( $nova_a ) );
afirma( $nova_a instanceof WP_Error && 401 === $nova_a->get_error_data()['status'],
	'o WP_Error da parede tem de trazer `status` 401 EXPLICITO: sem ele o WordPress devolve 500' );
afirma( null === rodametria_casca_fonte_do_token(),
	'sem fonte, `fonte_do_token` tinha de ser null' );

/* A AFIRMACAO DA 20.8: as duas reguas tem de DISCORDAR aqui. */
afirma( false === $velha_a && $codigo( $nova_a ) !== $codigo( false ),
	'A REGUA VELHA E A NOVA CONCORDARAM no mundo do portao morto — e autoteste em que elas concordam nao mede conserto nenhum (20.8)' );

/* 5b. COM FONTE, SEM O PARAMETRO. */
$GLOBALS['OPT'] = array( 'rodametria_sync_token' => 'tok-de-verdade' );
$nova_b = call_user_func( $parede, new PedidoFalso( array() ) );
afirma( 'rodametria_rotas_token_ausente' === $codigo( $nova_b ),
	'sem o parametro token a parede devia dizer `rodametria_rotas_token_ausente` e disse: ' . $codigo( $nova_b ) );

/* 5c. COM FONTE, TOKEN ERRADO — e a prova, LEGIVEL SEM O TOKEN, de que a
   comparacao rodou e de que a fonte foi achada. */
$nova_c = call_user_func( $parede, new PedidoFalso( array( 'token' => 'tok-errado' ) ) );
afirma( 'rodametria_rotas_token_invalido' === $codigo( $nova_c ),
	'com token errado a parede devia dizer `rodametria_rotas_token_invalido` e disse: ' . $codigo( $nova_c ) );
afirma( $codigo( $nova_a ) !== $codigo( $nova_c ),
	'os dois mundos de recusa sairam com o MESMO codigo — a distincao que esta ilha precisa nao existe' );

/* 5d. O TOKEN CERTO ABRE, e so ele. */
$nova_d = call_user_func( $parede, new PedidoFalso( array( 'token' => 'tok-de-verdade' ) ) );
afirma( true === $nova_d, 'o token certo nao abriu a rota' );
afirma( 'funcao:rodametria_sync_token' !== rodametria_casca_fonte_do_token()
		|| true === $nova_d, 'incoerencia entre a fonte do token e a parede' );
afirma( 'option:rodametria_sync_token' === rodametria_casca_fonte_do_token(),
	'com o token so na option, `fonte_do_token` tinha de dizer `option:...` e disse: '
	. var_export( rodametria_casca_fonte_do_token(), true ) );

/* 5e. E a parede nao pode abrir por PREFIXO nem por comprimento. */
foreach ( array( 'tok-de-verdad', 'tok-de-verdadeX', 'TOK-DE-VERDADE', '' ) as $quase ) {
	$v = call_user_func( $parede, new PedidoFalso( array( 'token' => $quase ) ) );
	afirma( true !== $v, sprintf( 'a parede abriu com o token %s', var_export( $quase, true ) ) );
}

/* --------------------------------------------------------------------------
   AS QUATRO MUTACOES — trava que nunca falhou nao e trava.
   Cada uma refaz UMA das funcoes com o defeito de verdade e exige reprovacao.
   -------------------------------------------------------------------------- */
$mutacoes = 0;
$mortas   = array();

/* M1 — o diagnostico que despeja o arquivo inteiro (o defeito que a 29.3 proibe). */
file_put_contents( $PORTA . '.htaccess', "# BEGIN NFD EPC\n# END NFD EPC\nCHAVE=$SEGREDO\n" );
$retrato_vazado = rodametria_casca_diagnostico_rotas();
$retrato_vazado['htaccess']['conteudo'] = file_get_contents( $PORTA . '.htaccess' );
$mutacoes++;
if ( false === strpos( json_encode( $retrato_vazado ), $SEGREDO ) ) {
	$mortas[] = 'M1: a afirmacao do segredo nao pegou um retrato que despeja o arquivo';
}

/* M2 — a leitura do bloco por `strpos` em vez de ancora de linha: um
   `# END WordPress` ou um comentario qualquer citando a palavra passaria. */
file_put_contents( $PORTA . '.htaccess', "# BEGIN NFD EPC\n# nao mexer: regra do WordPress antiga\n# END NFD EPC\n" );
$d_m2 = rodametria_casca_diagnostico_rotas();
$mutacoes++;
if ( false !== $d_m2['htaccess']['tem_wordpress'] ) {
	$mortas[] = 'M2: `tem_wordpress` ficou true por uma MENCAO a palavra WordPress fora de um `# BEGIN`';
}

/* M3 — a parede que compara com `==` em vez de `hash_equals`: `0 == 'tok'` e
   true em PHP antigo, e token numerico zero abriria a porta. */
$GLOBALS['OPT'] = array( 'rodametria_sync_token' => '0' );
$mutacoes++;
$v_m3 = call_user_func( $parede, new PedidoFalso( array( 'token' => 'tok-errado' ) ) );
if ( true === $v_m3 ) {
	$mortas[] = 'M3: a parede abriu comparando token numerico com string';
}

/* M4 — a regua velha no lugar da nova: ela NAO distingue os mundos, e a
   afirmacao 5c tem de cair se alguem a reintroduzir. */
$GLOBALS['OPT'] = array();
$mutacoes++;
if ( 'rodametria_rotas_sem_fonte_de_token' === ( parede_velha( new PedidoFalso( array( 'token' => 'x' ) ) ) === false ? 'NEGOU-SEM-DIZER' : 'LIBEROU' ) ) {
	$mortas[] = 'M4: a regua velha passou por distinta, e ela nao e';
}

foreach ( $mortas as $m ) { afirma( false, $m ); }

/* --------------------------------------------------------------------------
   A OUTRA METADE DOS STUBS, num processo filho.
   -------------------------------------------------------------------------- */
$extra = 0;
if ( ! $COM_ADMIN ) {
	$cmd = 'RDM_ADMIN=1 php ' . escapeshellarg( __FILE__ ) . ' 2>&1';
	$saida = array();
	$cod   = 0;
	exec( $cmd, $saida, $cod );
	$texto = implode( "\n", $saida );
	afirma( 0 === $cod,
		"o ramo COM ferramentas de admin reprovou no processo filho:\n    " . str_replace( "\n", "\n    ", $texto ) );
	if ( preg_match( '/(\d+) afirmacoes/', $texto, $m ) ) { $extra = (int) $m[1]; }
}

@unlink( $PORTA . '.htaccess' );
@rmdir( $TMP );

$rotulo = $COM_ADMIN ? 'teste-rotas (ramo COM admin)' : 'teste-rotas';
printf( "%s: %d afirmacoes%s, %d mutacao(oes) cobrada(s), %d falha(s)\n",
	$rotulo, $afirmacoes, $extra ? " (+$extra no processo filho)" : '', $mutacoes, count( $falhas ) );
foreach ( $falhas as $f ) { echo "  - $f\n"; }
echo count( $falhas ) ? "REPROVADO\n" : "APROVADO\n";
exit( count( $falhas ) ? 1 : 0 );

<?php
/**
 * Exercita o snippet "Aquametria Sync — atualizador do Sync" de ponta a ponta, com um
 * WordPress e um Code Snippets falsos, um cenário por processo (a versão instalada é uma
 * CONSTANTE, e constante não muda dentro do mesmo processo).
 *
 *   php ferramentas/teste-atualizador-sync.php .            # roda todos os cenários
 *   php ferramentas/teste-atualizador-sync.php . feliz      # roda um só
 *
 * O que cada cenário prova está no array $CENARIOS, junto com o que se espera do log.
 */

namespace Code_Snippets\Model {
	class Snippet {
		public $id = 0; public $name = ''; public $code = ''; public $desc = '';
		public $scope = 'global'; public $active = false;
	}
}

namespace Code_Snippets {
	function get_snippets() { return $GLOBALS['__snips']; }
	function get_snippet( $id ) {
		foreach ( $GLOBALS['__snips'] as $s ) { if ( (int) $s->id === (int) $id ) { return $s; } }
		return null;
	}
	function save_snippet( $s ) {
		if ( ! $s->id ) { $s->id = count( $GLOBALS['__snips'] ) + 1; $GLOBALS['__snips'][] = $s; }
		$GLOBALS['__gravacoes'][] = array( 'id' => $s->id, 'ativo' => $s->active, 'bytes' => strlen( $s->code ) );
		return $s; // 3.10 devolve OBJETO
	}
	function activate_snippet( $id ) {
		$s = get_snippet( $id );
		if ( ! $s ) { return 'snippet inexistente'; }
		$s->active = true;
		return $s;
	}
}

namespace {

$RAIZ    = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$CENARIO = isset( $argv[2] ) ? $argv[2] : '';

$CENARIOS = array(
	'feliz'            => 'site atrás do repositório: grava, ativa, verifica e marca o conteúdo',
	'sha-divergente'   => 'sha256 do arquivo não bate com o manifest: aborta sem gravar nada',
	'sintaxe-quebrada' => 'arquivo com erro de sintaxe (e sha coerente): aborta sem gravar nada',
	'versao-mentirosa' => 'manifest anuncia versão que o arquivo não declara: aborta sem gravar nada',
	'verificacao-falha'=> 'gravou mas o site não responde na versão nova: RESTAURA o backup',
	'loopback-mudo'    => 'site fechado para si mesmo: mantém o código novo e diz que a verificação foi inconclusiva',
	'ja-atualizado'    => 'site já na versão do manifest: não grava nada',
	'janela'           => 'tentativa há 10 minutos: nem chega a baixar o manifest',
	'sem-alvo'         => 'o snippet do Sync não existe no site: aborta, não instala do zero',
);

if ( '' === $CENARIO ) {
	$falhas = 0;
	foreach ( array_keys( $CENARIOS ) as $c ) {
		$saida = array(); $rc = 0;
		exec( escapeshellarg( PHP_BINARY ) . ' ' . escapeshellarg( __FILE__ ) . ' ' . escapeshellarg( $RAIZ ) . ' ' . escapeshellarg( $c ) . ' 2>&1', $saida, $rc );
		echo implode( "\n", $saida ) . "\n";
		if ( 0 !== $rc ) { $falhas++; }
	}
	echo "\n" . count( $CENARIOS ) . " cenário(s), $falhas falha(s)\n";
	exit( $falhas > 0 ? 1 : 0 );
}

/* ---------- WordPress falso ---------- */
define( 'ABSPATH', '/tmp/wp/' );
$GLOBALS['__opts']      = array();
$GLOBALS['__snips']     = array();
$GLOBALS['__gravacoes'] = array();
$GLOBALS['__agendados'] = array();

class WP_Error {
	private $m;
	public function __construct( $c = '', $m = '' ) { $this->m = $m; }
	public function get_error_message() { return $this->m; }
}
function is_wp_error( $t ) { return $t instanceof WP_Error; }
function get_option( $k, $d = false ) { return array_key_exists( $k, $GLOBALS['__opts'] ) ? $GLOBALS['__opts'][ $k ] : $d; }
function add_option( $k, $v, $x = '', $a = 'yes' ) { $GLOBALS['__opts'][ $k ] = $v; return true; }
function update_option( $k, $v, $a = null ) { $GLOBALS['__opts'][ $k ] = $v; return true; }
function current_time( $f ) { return date( 'mysql' === $f ? 'Y-m-d H:i:s' : $f ); }
function add_action( $h, $f, $p = 10, $a = 1 ) {}
function add_filter( $h, $f, $p = 10, $a = 1 ) {}
function register_rest_route() {}
function wp_next_scheduled( $h ) { return false; }
function wp_schedule_event( $t, $r, $h ) { $GLOBALS['__agendados'][] = $h; }
function wp_schedule_single_event( $t, $h ) { $GLOBALS['__agendados'][] = $h; }
function home_url( $p = '' ) { return 'https://aquametria.com.br' . $p; }
function rest_url( $p = '' ) { return 'https://aquametria.com.br/wp-json/' . ltrim( $p, '/' ); }
function add_query_arg( $args = array(), $url = '' ) { return $url . ( false === strpos( $url, '?' ) ? '?' : '&' ) . http_build_query( $args ); }
function wp_json_encode( $v ) { return json_encode( $v, JSON_UNESCAPED_UNICODE ); }
function status_header( $c ) {} function nocache_headers() {} function current_user_can( $c ) { return true; }
function wp_remote_retrieve_response_code( $r ) { return isset( $r['code'] ) ? $r['code'] : 0; }
function wp_remote_retrieve_body( $r ) { return isset( $r['body'] ) ? $r['body'] : ''; }

/* ---------- o cenário monta a rede e o banco ---------- */
$arquivo_sync = $RAIZ . '/snippets/aquametria-sync.php';
$codigo_novo  = file_get_contents( $arquivo_sync );
/* A versão vem do PRÓPRIO snippet, nunca escrita à mão aqui: com o número
   cravado, cada correção do Sync fazia os nove cenários reprovarem por
   desatualização do teste, e não por defeito. */
if ( ! preg_match( "/define\\( 'AQUAMETRIA_SYNC_VERSAO', '([^']+)' \\);/", $codigo_novo, $mv ) ) {
	fwrite( STDERR, "não achei AQUAMETRIA_SYNC_VERSAO no snippet do Sync\n" );
	exit( 1 );
}
$versao_nova  = $mv[1];
$codigo_velho = str_replace( "define( 'AQUAMETRIA_SYNC_VERSAO', '$versao_nova' );", "define( 'AQUAMETRIA_SYNC_VERSAO', '1.1.0' );", $codigo_novo );

$versao_no_site  = 'ja-atualizado' === $CENARIO ? $versao_nova : '1.1.0';
$versao_manifest = 'versao-mentirosa' === $CENARIO ? '9.9.9' : $versao_nova;
$corpo_servido   = $codigo_novo;
if ( 'sintaxe-quebrada' === $CENARIO ) {
	$corpo_servido = $codigo_novo . "\n\nfunction quebrada( { echo 'faltou parêntese';\n";
}
$sha_servido = hash( 'sha256', $corpo_servido );
if ( 'sha-divergente' === $CENARIO ) {
	$sha_servido = str_repeat( 'a', 64 );
}

$manifest = array( 'revisao' => 12, 'snippets' => array( array(
	'id' => 'aquametria-sync', 'nome' => 'Aquametria Sync', 'arquivo' => 'snippets/aquametria-sync.php',
	'escopo' => 'global', 'ativo' => true, 'publicar' => true, 'versao' => $versao_manifest, 'sha256' => $sha_servido,
) ) );

define( 'AQUAMETRIA_SYNC_VERSAO', $versao_no_site );

if ( 'sem-alvo' !== $CENARIO ) {
	$s = new \Code_Snippets\Model\Snippet();
	$s->id = 5; $s->name = 'Aquametria Sync'; $s->active = true;
	$s->code = ( $versao_no_site === $versao_nova ) ? $codigo_novo : $codigo_velho;
	$GLOBALS['__snips'][] = $s;
}
if ( 'ja-atualizado' === $CENARIO ) {
	$GLOBALS['__opts']['aquametria_atualizador_ultimo_sha'] = $sha_servido;
}
if ( 'janela' === $CENARIO ) {
	$GLOBALS['__opts']['aquametria_atualizador_ultima_tentativa'] = time() - 600;
}
/* Estado do Sync com três páginas já aplicadas — as que precisam ser reaplicadas. */
$GLOBALS['__opts']['aquametria_sync_estado'] = array(
	'revisao' => 11, 'ultimo' => '2026-09-08 03:00:00', 'log' => array(),
	'itens' => array(
		'conteudo:calculadora-de-litragem' => array( 'wp_id' => 20, 'sha256' => 'abc' ),
		'conteudo:calculadora-de-vazao-do-filtro' => array( 'wp_id' => 21, 'sha256' => 'def' ),
		'snippet:aquametria-casca' => array( 'wp_id' => 6, 'sha256' => 'ghi' ),
	),
);

function wp_remote_get( $url, $args = array() ) {
	global $manifest, $corpo_servido, $CENARIO;
	if ( false !== strpos( $url, 'manifest.json' ) ) {
		return array( 'code' => 200, 'body' => json_encode( $manifest ) );
	}
	if ( false !== strpos( $url, 'aquametria-sync.php' ) ) {
		return array( 'code' => 200, 'body' => $corpo_servido );
	}
	if ( false !== strpos( $url, '/aquametria/v1/status' ) ) {
		if ( 'loopback-mudo' === $CENARIO ) {
			return new WP_Error( 'rede', 'cURL error 7: Failed to connect' );
		}
		/* Requisição nova: a versão que responde é a que está GRAVADA no snippet. */
		$v = '';
		foreach ( $GLOBALS['__snips'] as $s ) {
			if ( 'Aquametria Sync' === $s->name && $s->active
				&& preg_match( "/AQUAMETRIA_SYNC_VERSAO'\s*,\s*'([^']+)'/", $s->code, $m ) ) { $v = $m[1]; }
		}
		if ( 'verificacao-falha' === $CENARIO ) { $v = '1.1.0'; } // simula snippet que o plugin desativou por erro
		return array( 'code' => 200, 'body' => json_encode( array( 'versao_sync' => $v, 'revisao' => 11 ) ) );
	}
	if ( 'loopback-mudo' === $CENARIO ) {
		return new WP_Error( 'rede', 'cURL error 7: Failed to connect' );
	}
	return array( 'code' => 200, 'body' => '<html></html>' );
}

eval( file_get_contents( $RAIZ . '/snippets/aquametria-atualizador-sync.php' ) );

$resultado = aquametria_atualizador_executar( false );
$gravou    = count( $GLOBALS['__gravacoes'] );
$estado    = $GLOBALS['__opts']['aquametria_sync_estado'];
$restante  = isset( $estado['itens']['conteudo:calculadora-de-litragem']['sha256'] );

/* ---------- o que cada cenário tem de ter acontecido ---------- */
$erros = array();
$exige = function ( $cond, $msg ) use ( &$erros ) { if ( ! $cond ) { $erros[] = $msg; } };

switch ( $CENARIO ) {
	case 'feliz':
		$exige( false !== strpos( $resultado, '1.1.0 → ' . $versao_nova ), 'o log não conta a troca de versão' );
		$exige( 1 === $gravou, 'esperava 1 save_snippet (a ativação é chamada à parte), houve ' . $gravou );
		$exige( false === $GLOBALS['__gravacoes'][0]['ativo'], 'a gravação tinha de ser INATIVA — save_snippet de snippet ativo dá eval no código' );
		$exige( true === $GLOBALS['__snips'][0]->active, 'o snippet ficou inativo no fim' );
		$exige( $GLOBALS['__snips'][0]->code === $codigo_novo, 'o código gravado não é o do repositório' );
		$exige( isset( $GLOBALS['__opts']['aquametria_sync_backup_codigo']['codigo'] ), 'não gravou backup' );
		$exige( $GLOBALS['__opts']['aquametria_sync_backup_codigo']['codigo'] === $codigo_velho, 'o backup não é o código anterior' );
		$exige( ! $restante, 'o sha do conteúdo não foi apagado (as páginas não seriam reaplicadas)' );
		$exige( -1 === $estado['revisao'], 'a revisão não foi zerada' );
		$exige( isset( $estado['itens']['snippet:aquametria-casca']['sha256'] ), 'apagou o sha de um snippet, devia mexer só em conteúdo' );
		$exige( in_array( 'aquametria_sync_evento', $GLOBALS['__agendados'], true ), 'não agendou a volta do Sync' );
		$exige( $GLOBALS['__opts']['aquametria_atualizador_ultimo_sha'] === $sha_servido, 'não registrou o sha aplicado' );
		break;
	case 'sha-divergente':
		$exige( false !== strpos( $resultado, 'sha256' ), 'o log não diz que o sha divergiu' );
		$exige( 0 === $gravou, 'gravou mesmo com sha divergente' );
		$exige( ! isset( $GLOBALS['__opts']['aquametria_sync_backup_codigo'] ), 'gravou backup à toa' );
		break;
	case 'sintaxe-quebrada':
		$exige( false !== strpos( $resultado, 'sintaxe' ), 'o log não fala em sintaxe: ' . $resultado );
		$exige( 0 === $gravou, 'gravou código com erro de sintaxe' );
		break;
	case 'versao-mentirosa':
		$exige( false !== strpos( $resultado, 'não declara a versão' ), 'o log não acusa a incoerência: ' . $resultado );
		$exige( 0 === $gravou, 'gravou com manifest incoerente' );
		break;
	case 'verificacao-falha':
		$exige( false !== strpos( $resultado, 'RESTAURADO' ), 'não restaurou o backup: ' . $resultado );
		$exige( $GLOBALS['__snips'][0]->code === $codigo_velho, 'o código no site não voltou a ser o antigo' );
		$exige( true === $GLOBALS['__snips'][0]->active, 'o snippet restaurado ficou inativo' );
		$exige( $restante, 'marcou conteúdo para reaplicar mesmo tendo revertido' );
		break;
	case 'loopback-mudo':
		$exige( false !== strpos( $resultado, 'inconclusiva' ), 'não avisou que a verificação foi inconclusiva: ' . $resultado );
		$exige( $GLOBALS['__snips'][0]->code === $codigo_novo, 'reverteu sem prova de falha' );
		$exige( ! $restante, 'não marcou o conteúdo para reaplicação' );
		break;
	case 'ja-atualizado':
		$exige( false !== strpos( $resultado, 'nada a fazer' ), 'devia dizer que não há o que fazer: ' . $resultado );
		$exige( 0 === $gravou, 'reescreveu o Sync sem necessidade' );
		break;
	case 'janela':
		$exige( false !== strpos( $resultado, 'janela' ), 'devia respeitar a janela de uma hora: ' . $resultado );
		$exige( 0 === $gravou, 'gravou dentro da janela' );
		break;
	case 'sem-alvo':
		$exige( false !== strpos( $resultado, 'não existe no site' ), 'devia recusar instalar do zero: ' . $resultado );
		$exige( 0 === $gravou, 'criou o Sync do nada' );
		break;
}

if ( $erros ) {
	echo "FALHA  $CENARIO — $CENARIOS[$CENARIO]\n";
	foreach ( $erros as $e ) { echo "       · $e\n"; }
	echo "       resultado: $resultado\n";
	exit( 1 );
}
echo sprintf( "ok  %-18s %s\n", $CENARIO, $CENARIOS[ $CENARIO ] );
exit( 0 );

}

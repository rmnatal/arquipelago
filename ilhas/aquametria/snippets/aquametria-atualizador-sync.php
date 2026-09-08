/**
 * Aquametria Sync — atualizador do Sync
 * Versão: 1.0.0 (08/09/2026)
 *
 * POR QUE ESTE SNIPPET EXISTE
 * O snippet "Aquametria Sync" se pula a si mesmo de propósito: ao percorrer o manifest
 * ele compara o nome do item com o próprio nome e devolve "pulado". Isso protege o site
 * (o Sync não se reescreve no meio da própria execução) mas cria um gargalo permanente:
 * NENHUMA correção feita no arquivo do Sync, no repositório, chega ao site sozinha. Foi
 * o que aconteceu em 08/09/2026 — o repositório estava na v1.1.3, com o corte do front
 * matter já pronto, e o site continuava na v1.1.0 colada à mão, publicando o YAML dentro
 * do corpo das páginas.
 *
 * Este snippet quebra o gargalo por fora: como o NOME dele é diferente do nome do Sync,
 * o próprio Sync o instala e o ativa pelo caminho que já funciona. E a única coisa que
 * ele faz é reescrever o Sync a partir do repositório.
 *
 * O QUE ELE FAZ, NESTA ORDEM (qualquer passo que falhe interrompe tudo)
 *   1. no máximo uma vez por hora, e só quando a versão do manifest difere da instalada;
 *   2. baixa o manifest e o arquivo do Sync do raw.githubusercontent.com;
 *   3. confere o sha256 do arquivo contra o manifest — divergiu, aborta (nunca grava
 *      código não verificado) — e confere que a versão declarada no arquivo é a mesma
 *      que o manifest anuncia;
 *   4. faz uma checagem de sintaxe de verdade no código baixado, SEM executá-lo
 *      (token_get_all com TOKEN_PARSE devolve ParseError em código quebrado);
 *   5. guarda o código ATUAL do Sync na option aquametria_sync_backup_codigo e relê a
 *      option para confirmar — sem backup gravado, não prossegue;
 *   6. grava pela API do Code Snippets 3.10 (Code_Snippets\Model\Snippet, save_snippet
 *      devolve OBJETO), INATIVO primeiro e ativando depois, tudo em try/catch;
 *   7. verifica numa REQUISIÇÃO NOVA (o código velho ainda está carregado nesta) se o
 *      endpoint de status responde com a versão nova; não respondeu, RESTAURA o backup;
 *   8. marca o conteúdo para ser reaplicado, porque as páginas no ar foram convertidas
 *      pelo Sync velho e trazem o defeito que a versão nova corrige.
 *
 * Gatilhos: WP-Cron de hora em hora; GET /?aquametria_atualizar_sync=TOKEN[&forcar=1]
 *           (mesmo token do Sync); REST POST /wp-json/aquametria/v1/atualizador.
 * Leitura:  REST GET /wp-json/aquametria/v1/atualizador (público, só o log).
 *
 * Regras herdadas (fase 4b): toda função de nível superior dentro de function_exists;
 * não usa a superglobal de servidor; sem "<?php" no topo; texto acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_ATUALIZADOR_VERSAO' ) ) {
	define( 'AQUAMETRIA_ATUALIZADOR_VERSAO', '1.0.0' );
	define( 'AQUAMETRIA_ATUALIZADOR_BASE', 'https://raw.githubusercontent.com/rmnatal/arquipelago/main/ilhas/aquametria/' );
	define( 'AQUAMETRIA_ATUALIZADOR_ALVO_NOME', 'Aquametria Sync' );
	define( 'AQUAMETRIA_ATUALIZADOR_ALVO_ID', 'aquametria-sync' );
	define( 'AQUAMETRIA_ATUALIZADOR_INTERVALO', 3600 );
}

/* ---------- log ---------- */

if ( ! function_exists( 'aquametria_atualizador_log' ) ) {
function aquametria_atualizador_log( $msg ) {
	$log = get_option( 'aquametria_atualizador_log' );
	if ( ! is_array( $log ) ) {
		$log = array();
	}
	array_unshift( $log, current_time( 'Y-m-d H:i' ) . ' ' . $msg );
	$log = array_slice( $log, 0, 30 );
	if ( false === get_option( 'aquametria_atualizador_log' ) ) {
		add_option( 'aquametria_atualizador_log', $log, '', 'no' );
	} else {
		update_option( 'aquametria_atualizador_log', $log, 'no' );
	}
	return $msg;
}
}

/* ---------- utilidades ---------- */

if ( ! function_exists( 'aquametria_atualizador_baixar' ) ) {
function aquametria_atualizador_baixar( $rel ) {
	$url = AQUAMETRIA_ATUALIZADOR_BASE . ltrim( $rel, '/' ) . '?v=' . time();
	$r   = wp_remote_get( $url, array( 'timeout' => 25, 'headers' => array( 'Cache-Control' => 'no-cache' ) ) );
	if ( is_wp_error( $r ) ) {
		return new WP_Error( 'rede', $r->get_error_message() );
	}
	$code = (int) wp_remote_retrieve_response_code( $r );
	if ( 200 !== $code ) {
		return new WP_Error( 'http', 'HTTP ' . $code . ' em ' . $rel );
	}
	return wp_remote_retrieve_body( $r );
}
}

/* Versão que está REALMENTE rodando no site: a constante que o Sync carregado definiu.
   Se o Sync estiver desativado ou ausente, devolve string vazia — que difere de qualquer
   versão do manifest e portanto dispara a gravação. */
if ( ! function_exists( 'aquametria_atualizador_versao_instalada' ) ) {
function aquametria_atualizador_versao_instalada() {
	return defined( 'AQUAMETRIA_SYNC_VERSAO' ) ? (string) AQUAMETRIA_SYNC_VERSAO : '';
}
}

if ( ! function_exists( 'aquametria_atualizador_classe_snippet' ) ) {
function aquametria_atualizador_classe_snippet() {
	if ( class_exists( '\\Code_Snippets\\Model\\Snippet' ) ) {
		return '\\Code_Snippets\\Model\\Snippet';
	}
	if ( class_exists( '\\Code_Snippets\\Snippet' ) ) {
		return '\\Code_Snippets\\Snippet';
	}
	return '';
}
}

if ( ! function_exists( 'aquametria_atualizador_achar_alvo' ) ) {
function aquametria_atualizador_achar_alvo() {
	foreach ( \Code_Snippets\get_snippets() as $s ) {
		if ( trim( $s->name ) === AQUAMETRIA_ATUALIZADOR_ALVO_NOME ) {
			return $s;
		}
	}
	return null;
}
}

/* Sintaxe de verdade, sem executar nada: com TOKEN_PARSE o tokenizador faz o parse
   completo e levanta ParseError em código quebrado. É o mais perto de um "php -l" que
   dá para fazer dentro do WordPress sem eval — e eval aqui seria justamente o erro. */
if ( ! function_exists( 'aquametria_atualizador_sintaxe_ok' ) ) {
function aquametria_atualizador_sintaxe_ok( $codigo, &$erro ) {
	$erro = '';
	if ( ! defined( 'TOKEN_PARSE' ) ) {
		return true; // PHP antigo: não dá para checar, segue com as outras travas
	}
	try {
		token_get_all( "<?php\n" . $codigo, TOKEN_PARSE );
		return true;
	} catch ( \Throwable $e ) {
		$erro = $e->getMessage() . ' (linha ' . $e->getLine() . ')';
		return false;
	}
}
}

/* Gravação pela API do Code Snippets 3.10: grava INATIVO (save_snippet de snippet ativo
   roda test_snippet_code, que dá eval no código na mesma requisição) e ativa em seguida.
   save_snippet devolve OBJETO — ler $ret->id, nunca tratar o retorno como id. */
if ( ! function_exists( 'aquametria_atualizador_gravar_codigo' ) ) {
function aquametria_atualizador_gravar_codigo( $alvo, $codigo, $ativar ) {
	try {
		$alvo->code   = $codigo;
		$alvo->active = false;
		$ret = \Code_Snippets\save_snippet( $alvo );
		$id  = is_object( $ret ) && isset( $ret->id ) ? (int) $ret->id : (int) $ret;
		if ( ! $id ) {
			return 'save_snippet falhou (sem id)';
		}
		$re = \Code_Snippets\get_snippet( $id );
		if ( ! $re || strlen( (string) $re->code ) !== strlen( $codigo ) ) {
			return 'gravação não conferiu (tamanho diferente) — id ' . $id;
		}
		if ( $ativar ) {
			if ( function_exists( '\\Code_Snippets\\activate_snippet' ) ) {
				$a = \Code_Snippets\activate_snippet( $id );
				if ( is_string( $a ) ) {
					return 'gravado (#' . $id . ') mas NÃO ativado: ' . $a;
				}
				if ( is_wp_error( $a ) ) {
					return 'gravado (#' . $id . ') mas NÃO ativado: ' . $a->get_error_message();
				}
			}
			$re2 = \Code_Snippets\get_snippet( $id );
			if ( ! $re2 || empty( $re2->active ) ) {
				return 'gravado (#' . $id . ') mas continua inativo após activate_snippet';
			}
		}
		return '';
	} catch ( \Throwable $e ) {
		return 'ERRO ' . get_class( $e ) . ': ' . $e->getMessage() . ' (' . basename( $e->getFile() ) . ':' . $e->getLine() . ')';
	}
}
}

/* A prova real: uma REQUISIÇÃO NOVA ao site. Nesta requisição aqui o código VELHO do Sync
   continua carregado na memória do PHP, então perguntar à constante não prova nada.
   Devolve 'ok', 'falhou' ou 'inconclusivo' (loopback indisponível — o site pode estar
   fechado para si mesmo, e nesse caso derrubar a versão nova seria pior que mantê-la). */
if ( ! function_exists( 'aquametria_atualizador_verificar' ) ) {
function aquametria_atualizador_verificar( $versao_esperada, &$detalhe ) {
	$url = add_query_arg( array( 'v' => time() ), rest_url( 'aquametria/v1/status' ) );
	$r   = wp_remote_get( $url, array( 'timeout' => 20, 'headers' => array( 'Cache-Control' => 'no-cache' ) ) );
	if ( is_wp_error( $r ) ) {
		$home = wp_remote_get( add_query_arg( array( 'v' => time() ), home_url( '/' ) ), array( 'timeout' => 20 ) );
		if ( is_wp_error( $home ) ) {
			$detalhe = 'loopback indisponível (' . $r->get_error_message() . ')';
			return 'inconclusivo';
		}
		$detalhe = 'o site responde mas o endpoint de status não: ' . $r->get_error_message();
		return 'falhou';
	}
	$code = (int) wp_remote_retrieve_response_code( $r );
	if ( 200 !== $code ) {
		$detalhe = 'status devolveu HTTP ' . $code;
		return 'falhou';
	}
	$j = json_decode( wp_remote_retrieve_body( $r ), true );
	if ( ! is_array( $j ) || empty( $j['versao_sync'] ) ) {
		$detalhe = 'status sem campo versao_sync';
		return 'falhou';
	}
	if ( (string) $j['versao_sync'] !== (string) $versao_esperada ) {
		$detalhe = 'status responde versão ' . $j['versao_sync'] . ', esperada ' . $versao_esperada;
		return 'falhou';
	}
	$detalhe = 'status responde versão ' . $j['versao_sync'];
	return 'ok';
}
}

/* As páginas que já estão no ar foram convertidas pelo Sync VELHO e carregam o defeito
   que a versão nova corrige. O Sync pula arquivo cujo sha256 já foi aplicado, então
   apagar o sha registrado de cada item de conteúdo é o que obriga a reaplicação — sem
   precisar tocar em nada pelo painel. Não rodamos o sync aqui: nesta requisição quem
   está carregado é o conversor velho, que reescreveria o mesmo defeito. */
if ( ! function_exists( 'aquametria_atualizador_marcar_conteudo' ) ) {
function aquametria_atualizador_marcar_conteudo() {
	$estado = get_option( 'aquametria_sync_estado' );
	if ( ! is_array( $estado ) ) {
		return 0;
	}
	$n = 0;
	if ( ! empty( $estado['itens'] ) && is_array( $estado['itens'] ) ) {
		foreach ( $estado['itens'] as $chave => $dados ) {
			if ( 0 === strpos( $chave, 'conteudo:' ) && isset( $estado['itens'][ $chave ]['sha256'] ) ) {
				unset( $estado['itens'][ $chave ]['sha256'] );
				$n++;
			}
		}
	}
	$estado['revisao'] = -1; // obriga o Sync a percorrer o manifest inteiro na próxima volta
	update_option( 'aquametria_sync_estado', $estado, 'no' );
	// Evento avulso: a volta seguinte do Sync já roda com o código novo carregado.
	wp_schedule_single_event( time() + 60, 'aquametria_sync_evento' );
	return $n;
}
}

/* ---------- execução ---------- */

if ( ! function_exists( 'aquametria_atualizador_executar' ) ) {
function aquametria_atualizador_executar( $forcar = false ) {
	$agora  = time();
	$ultima = (int) get_option( 'aquametria_atualizador_ultima_tentativa', 0 );
	if ( ! $forcar && $ultima && ( $agora - $ultima ) < AQUAMETRIA_ATUALIZADOR_INTERVALO ) {
		return 'janela de uma hora ainda não venceu';
	}
	// Marca a tentativa ANTES de tentar: se algo estourar no meio, não entra em laço.
	if ( false === get_option( 'aquametria_atualizador_ultima_tentativa' ) ) {
		add_option( 'aquametria_atualizador_ultima_tentativa', $agora, '', 'no' );
	} else {
		update_option( 'aquametria_atualizador_ultima_tentativa', $agora, 'no' );
	}

	if ( ! function_exists( '\\Code_Snippets\\save_snippet' ) || '' === aquametria_atualizador_classe_snippet() ) {
		return aquametria_atualizador_log( 'abortado: API PHP do Code Snippets indisponível' );
	}

	$bruto = aquametria_atualizador_baixar( 'manifest.json' );
	if ( is_wp_error( $bruto ) ) {
		return aquametria_atualizador_log( 'abortado: manifest não baixou — ' . $bruto->get_error_message() );
	}
	$m = json_decode( $bruto, true );
	if ( ! is_array( $m ) || empty( $m['snippets'] ) ) {
		return aquametria_atualizador_log( 'abortado: manifest inválido' );
	}
	$item = null;
	foreach ( $m['snippets'] as $s ) {
		if ( isset( $s['id'] ) && AQUAMETRIA_ATUALIZADOR_ALVO_ID === $s['id'] ) {
			$item = $s;
			break;
		}
	}
	if ( ! $item || empty( $item['arquivo'] ) || empty( $item['sha256'] ) || empty( $item['versao'] ) ) {
		return aquametria_atualizador_log( 'abortado: manifest sem o item ' . AQUAMETRIA_ATUALIZADOR_ALVO_ID . ' completo (arquivo, sha256 e versao)' );
	}

	$versao_manifest  = (string) $item['versao'];
	$versao_instalada = aquametria_atualizador_versao_instalada();
	$sha_manifest     = strtolower( trim( (string) $item['sha256'] ) );
	$sha_ultimo       = (string) get_option( 'aquametria_atualizador_ultimo_sha', '' );
	if ( ! $forcar && $versao_instalada === $versao_manifest && $sha_ultimo === $sha_manifest ) {
		return 'nada a fazer: o site já roda a ' . $versao_manifest;
	}

	$alvo = aquametria_atualizador_achar_alvo();
	if ( ! $alvo ) {
		return aquametria_atualizador_log( 'abortado: o snippet "' . AQUAMETRIA_ATUALIZADOR_ALVO_NOME . '" não existe no site — este atualizador reescreve, não instala do zero' );
	}

	$corpo = aquametria_atualizador_baixar( $item['arquivo'] );
	if ( is_wp_error( $corpo ) ) {
		return aquametria_atualizador_log( 'abortado: ' . $item['arquivo'] . ' não baixou — ' . $corpo->get_error_message() );
	}
	if ( ! hash_equals( $sha_manifest, hash( 'sha256', $corpo ) ) ) {
		return aquametria_atualizador_log( 'abortado: sha256 do arquivo baixado diverge do manifest — nada foi gravado' );
	}
	$codigo = preg_replace( '/^\s*<\?php\s*/', '', $corpo );
	if ( ! preg_match( "/AQUAMETRIA_SYNC_VERSAO'\s*,\s*'" . preg_quote( $versao_manifest, '/' ) . "'/", $codigo ) ) {
		return aquametria_atualizador_log( 'abortado: o arquivo não declara a versão ' . $versao_manifest . ' que o manifest anuncia' );
	}
	$erro_sintaxe = '';
	if ( ! aquametria_atualizador_sintaxe_ok( $codigo, $erro_sintaxe ) ) {
		return aquametria_atualizador_log( 'abortado: código baixado não passa na checagem de sintaxe — ' . $erro_sintaxe );
	}

	/* Backup, e a releitura que prova que o backup existe. */
	$backup = array(
		'codigo'  => (string) $alvo->code,
		'versao'  => $versao_instalada,
		'wp_id'   => (int) $alvo->id,
		'sha256'  => hash( 'sha256', (string) $alvo->code ),
		'em'      => current_time( 'mysql' ),
	);
	if ( false === get_option( 'aquametria_sync_backup_codigo' ) ) {
		add_option( 'aquametria_sync_backup_codigo', $backup, '', 'no' );
	} else {
		update_option( 'aquametria_sync_backup_codigo', $backup, 'no' );
	}
	$conf = get_option( 'aquametria_sync_backup_codigo' );
	if ( ! is_array( $conf ) || ! isset( $conf['codigo'] ) || strlen( (string) $conf['codigo'] ) !== strlen( (string) $alvo->code ) ) {
		return aquametria_atualizador_log( 'abortado: o backup do código atual não foi gravado — nada foi tocado' );
	}

	$falha = aquametria_atualizador_gravar_codigo( $alvo, $codigo, ! empty( $item['ativo'] ) );
	if ( '' !== $falha ) {
		return aquametria_atualizador_log( 'gravação falhou (' . $versao_instalada . ' → ' . $versao_manifest . '): ' . $falha );
	}

	$detalhe = '';
	$v       = aquametria_atualizador_verificar( $versao_manifest, $detalhe );
	if ( 'falhou' === $v ) {
		$restaurar = aquametria_atualizador_achar_alvo();
		$erro_r    = $restaurar ? aquametria_atualizador_gravar_codigo( $restaurar, (string) $conf['codigo'], true ) : 'snippet sumiu';
		return aquametria_atualizador_log( 'a versão ' . $versao_manifest . ' NÃO respondeu (' . $detalhe . ') — backup '
			. ( '' === $erro_r ? 'RESTAURADO, site de volta na ' . $versao_instalada : 'NÃO restaurou: ' . $erro_r ) );
	}

	if ( false === get_option( 'aquametria_atualizador_ultimo_sha' ) ) {
		add_option( 'aquametria_atualizador_ultimo_sha', $sha_manifest, '', 'no' );
	} else {
		update_option( 'aquametria_atualizador_ultimo_sha', $sha_manifest, 'no' );
	}
	$n = aquametria_atualizador_marcar_conteudo();
	return aquametria_atualizador_log( 'Sync ' . $versao_instalada . ' → ' . $versao_manifest
		. ' (' . ( 'ok' === $v ? $detalhe : 'verificação inconclusiva: ' . $detalhe . ' — código novo mantido' ) . '); '
		. $n . ' página(s) marcada(s) para reaplicação, sync agendado para daqui a 1 minuto' );
}
}

/* ---------- gatilhos ---------- */

add_filter( 'cron_schedules', function ( $s ) {
	$s['aquametria_1h'] = array( 'interval' => 3600, 'display' => 'Aquametria: de hora em hora' );
	return $s;
} );

add_action( 'init', function () {
	if ( ! wp_next_scheduled( 'aquametria_atualizador_evento' ) ) {
		wp_schedule_event( time() + 180, 'aquametria_1h', 'aquametria_atualizador_evento' );
	}
	$token = filter_input( INPUT_GET, 'aquametria_atualizar_sync', FILTER_DEFAULT );
	if ( is_string( $token ) && '' !== $token ) {
		if ( ! function_exists( 'aquametria_sync_token' ) || ! hash_equals( aquametria_sync_token(), $token ) ) {
			status_header( 403 );
			exit( 'token inválido' );
		}
		$forcar = '1' === (string) filter_input( INPUT_GET, 'forcar', FILTER_DEFAULT );
		$msg    = aquametria_atualizador_executar( $forcar );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array(
			'atualizador'      => AQUAMETRIA_ATUALIZADOR_VERSAO,
			'versao_instalada' => aquametria_atualizador_versao_instalada(),
			'resultado'        => $msg,
			'log'              => array_slice( (array) get_option( 'aquametria_atualizador_log', array() ), 0, 10 ),
		), JSON_UNESCAPED_UNICODE );
		exit;
	}
} );

add_action( 'aquametria_atualizador_evento', function () {
	aquametria_atualizador_executar( false );
} );

add_action( 'rest_api_init', function () {
	register_rest_route( 'aquametria/v1', '/atualizador', array(
		array(
			'methods'             => 'GET',
			'permission_callback' => '__return_true',
			'callback'            => function () {
				return array(
					'atualizador'      => AQUAMETRIA_ATUALIZADOR_VERSAO,
					'versao_instalada' => aquametria_atualizador_versao_instalada(),
					'ultima_tentativa' => (int) get_option( 'aquametria_atualizador_ultima_tentativa', 0 ),
					'log'              => array_slice( (array) get_option( 'aquametria_atualizador_log', array() ), 0, 15 ),
				);
			},
		),
		array(
			'methods'             => 'POST',
			'permission_callback' => function () { return current_user_can( 'manage_options' ); },
			'callback'            => function ( $req ) {
				$msg = aquametria_atualizador_executar( (bool) $req->get_param( 'forcar' ) );
				return array(
					'resultado'        => $msg,
					'versao_instalada' => aquametria_atualizador_versao_instalada(),
					'log'              => array_slice( (array) get_option( 'aquametria_atualizador_log', array() ), 0, 15 ),
				);
			},
		),
	) );
} );

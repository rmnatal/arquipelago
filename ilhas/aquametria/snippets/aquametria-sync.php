/**
 * Aquametria Sync
 * Versão: 1.1.4 (08/09/2026) — o corte do front matter ficou tolerante (BOM no começo do
 *   arquivo, quebra de linha antiga só com CR, espaço ou tabulação à direita do delimitador).
 *   Nenhuma dessas variações é visível no editor, e qualquer uma delas devolvia o metadado
 *   impresso no corpo da página. Vem junto o teste ferramentas/teste-conversor-markdown.php,
 *   que roda este conversor sobre todos os arquivos de conteudo/ e recusa resíduo de YAML.
 * Versão: 1.1.3 (08/09/2026) — o conversor de Markdown passou a entender bloco de código
 *   cercado por crases triplas: a fórmula P = U · A · ΔT do artigo do aquecedor sairia com as
 *   crases impressas e viraria um parágrafo qualquer no meio do texto.
 * Versão: 1.1.2 (08/09/2026) — o conversor de Markdown passou a entender citação em bloco
 *   (linha começando com '>'), que antes saía com o '>' escapado no meio do parágrafo.
 * Versão: 1.1.1 (07/09/2026) — o conversor de Markdown passou a descartar o front matter
 *   do arquivo e a deixar a linha que só tem shortcode fora do parágrafo (dois defeitos que
 *   o primeiro conteúdo em Markdown, a página da C1, iria expor).
 * Versão 1.1.0 (07/09/2026) — compatível com Code Snippets 3.10 (classe Code_Snippets\Model\Snippet,
 *   save_snippet devolve objeto), erro de um item não derruba o sync (try/catch), grava inativo e ativa
 *   em seguida, e relata falha de ativação.
 *
 * Puxa o manifest.json da ilha Aquametria no repositório público rmnatal/arquipelago
 * (raw.githubusercontent.com) e aplica no WordPress SOMENTE os itens com publicar=true:
 *   - snippets  → cria/atualiza no Code Snippets (casa pelo nome), ativa/desativa conforme "ativo"
 *   - conteudo  → cria/atualiza post (artigo) ou página (pagina, pagina-programatica), Markdown → HTML
 *   - dados     → grava JSON na option aquametria_dados_{id} (autoload off)
 * Confere sha256 de cada arquivo contra o manifest; divergência = item pulado e registrado.
 * Nunca toca em si mesmo. Nunca apaga nada.
 *
 * Gatilhos: WP-Cron a cada 30 min; GET /?aquametria_sync=TOKEN[&forcar=1];
 *           REST POST /wp-json/aquametria/v1/sync (manage_options).
 * Leitura:  REST GET /wp-json/aquametria/v1/status (público, só o log) e
 *           REST GET /wp-json/aquametria/v1/token (manage_options).
 *
 * Regras herdadas (fase 4b): não usa a superglobal de servidor; sem "<?php" no topo;
 * texto acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_SYNC_VERSAO' ) ) {
	define( 'AQUAMETRIA_SYNC_VERSAO', '1.1.4' );
	define( 'AQUAMETRIA_SYNC_BASE', 'https://raw.githubusercontent.com/rmnatal/arquipelago/main/ilhas/aquametria/' );
	define( 'AQUAMETRIA_SYNC_NOME_PROPRIO', 'Aquametria Sync' );
}

/* ---------- utilidades ---------- */

if ( ! function_exists( 'aquametria_sync_token' ) ) {
function aquametria_sync_token() {
	$t = get_option( 'aquametria_sync_token' );
	if ( ! $t ) {
		$t = wp_generate_password( 32, false, false );
		add_option( 'aquametria_sync_token', $t, '', 'no' );
	}
	return $t;
}
}

if ( ! function_exists( 'aquametria_sync_estado' ) ) {
function aquametria_sync_estado() {
	$e = get_option( 'aquametria_sync_estado' );
	if ( ! is_array( $e ) ) {
		$e = array( 'revisao' => -1, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	}
	return $e;
}
}

if ( ! function_exists( 'aquametria_sync_log' ) ) {
function aquametria_sync_log( &$estado, $msg ) {
	$linha = current_time( 'Y-m-d H:i' ) . ' ' . $msg;
	array_unshift( $estado['log'], $linha );
	$estado['log'] = array_slice( $estado['log'], 0, 40 );
}
}

if ( ! function_exists( 'aquametria_sync_baixar' ) ) {
function aquametria_sync_baixar( $rel ) {
	$url = AQUAMETRIA_SYNC_BASE . ltrim( $rel, '/' ) . '?v=' . time();
	$r   = wp_remote_get( $url, array( 'timeout' => 25, 'headers' => array( 'Cache-Control' => 'no-cache' ) ) );
	if ( is_wp_error( $r ) ) {
		return new WP_Error( 'rede', $r->get_error_message() );
	}
	$code = wp_remote_retrieve_response_code( $r );
	if ( 200 !== (int) $code ) {
		return new WP_Error( 'http', 'HTTP ' . $code . ' em ' . $rel );
	}
	return wp_remote_retrieve_body( $r );
}
}

if ( ! function_exists( 'aquametria_sync_sha_ok' ) ) {
function aquametria_sync_sha_ok( $corpo, $esperado ) {
	if ( empty( $esperado ) ) {
		return true; // sem hash declarado, não bloqueia
	}
	return hash_equals( strtolower( trim( $esperado ) ), hash( 'sha256', $corpo ) );
}
}

/* Markdown mínimo → HTML (títulos, parágrafos, listas, negrito, itálico, links, código, tabelas simples) */
if ( ! function_exists( 'aquametria_sync_md' ) ) {
function aquametria_sync_md( $md ) {
	/* Marca de ordem de byte: alguns editores gravam o arquivo com ela, e o BOM antes
	   do primeiro '---' faz o corte do front matter falhar sem nenhum erro visível. */
	if ( 0 === strncmp( $md, "\xEF\xBB\xBF", 3 ) ) {
		$md = substr( $md, 3 );
	}
	$md = str_replace( array( "\r\n", "\r" ), "\n", $md );
	/* Front matter YAML: é metadado do repositório (título, slug, fontes), não texto
	   de página. Sem este corte ele sairia impresso no topo do post — e sai feio, porque
	   o wptexturize transforma os três hifens em travessão e o leitor vê "— id: ... —"
	   antes do texto. Foi o defeito visto no ar na página da C1 em 08/09/2026.
	   A tolerância importa: espaço ou tabulação à direita de qualquer um dos dois
	   delimitadores é invisível no editor e quebrava o corte em silêncio. */
	$md = preg_replace( '/\A---[ \t]*\n.*?\n---[ \t]*(?:\n|\z)/s', '', $md, 1 );
	$linhas = explode( "\n", $md );
	$html   = '';
	$lista  = null;
	$par    = array();
	$tabela = array();
	$citacao = array();
	$codigo  = null;   /* null = fora do bloco; array = linhas dentro dele */

	$inline = function ( $t ) {
		$t = esc_html( $t );
		$t = preg_replace( '/`([^`]+)`/', '<code>$1</code>', $t );
		$t = preg_replace( '/\*\*(.+?)\*\*/s', '<strong>$1</strong>', $t );
		$t = preg_replace( '/(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])/s', '<em>$1</em>', $t );
		/* Link absoluto (https://...) e link relativo à raiz (/pagina/). O segundo
		   caso faltava e era armadilha silenciosa: o texto saía com os colchetes
		   impressos e ninguém percebia, porque não é erro de sintaxe nenhum. */
		$t = preg_replace( '/\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[^\s)]*)\)/', '<a href="$2">$1</a>', $t );
		return $t;
	};
	$fecha_par = function () use ( &$par, &$html, $inline ) {
		if ( $par ) {
			$html .= '<p>' . $inline( implode( ' ', $par ) ) . "</p>\n";
			$par   = array();
		}
	};
	$fecha_lista = function () use ( &$lista, &$html ) {
		if ( $lista ) {
			$html .= '</' . $lista . ">\n";
			$lista = null;
		}
	};
	$fecha_tabela = function () use ( &$tabela, &$html, $inline ) {
		if ( ! $tabela ) {
			return;
		}
		/* A tabela sai dentro de um bloco que rola: em tela de celular uma tabela
		   de três colunas empurra a página inteira para o lado, e a rolagem
		   horizontal do documento é defeito visível em qualquer artigo. */
		$html .= '<div class="aqm-tabela" style="overflow-x:auto">';
		$html .= '<table>';
		foreach ( $tabela as $i => $cels ) {
			$tag   = 0 === $i ? 'th' : 'td';
			$html .= '<tr>';
			foreach ( $cels as $c ) {
				$html .= '<' . $tag . '>' . $inline( trim( $c ) ) . '</' . $tag . '>';
			}
			$html .= '</tr>';
		}
		$html  .= "</table></div>\n";
		$tabela = array();
	};
	/* Citação em bloco (linha começando com '>'). Sem isto o '>' saía escapado
	   no meio do parágrafo, que foi o que aconteceu com a fórmula do protocolo
	   do balde na página da C3. Linha em branco dentro da citação vira parágrafo
	   novo dentro dela. */
	$fecha_citacao = function () use ( &$citacao, &$html, $inline ) {
		if ( ! $citacao ) {
			return;
		}
		$html .= '<blockquote class="aqm-citacao">';
		foreach ( $citacao as $p ) {
			if ( ! $p ) {
				continue; // parágrafo vazio: veio da linha em branco que fechou a citação
			}
			$html .= '<p>' . $inline( implode( ' ', $p ) ) . '</p>';
		}
		$html   .= "</blockquote>\n";
		$citacao = array();
	};

	/* Bloco de código cercado por ``` — a fórmula P = U . A . deltaT do artigo do
	   aquecedor depende disto. Sem o bloco, as crases sairiam impressas e a
	   fórmula viraria um parágrafo qualquer no meio do texto. Dentro do bloco
	   nada é interpretado: nem negrito, nem link, nem shortcode. */
	$fecha_codigo = function () use ( &$codigo, &$html ) {
		if ( null === $codigo ) {
			return;
		}
		$html .= '<pre class="aqm-codigo"><code>' . esc_html( implode( "\n", $codigo ) ) . "</code></pre>\n";
		$codigo = null;
	};

	foreach ( $linhas as $l ) {
		$t = rtrim( $l );
		if ( preg_match( '/^```/', trim( $t ) ) ) {
			if ( null === $codigo ) {
				$fecha_par(); $fecha_lista(); $fecha_tabela(); $fecha_citacao();
				$codigo = array();
			} else {
				$fecha_codigo();
			}
			continue;
		}
		if ( null !== $codigo ) {
			$codigo[] = $t;
			continue;
		}
		if ( '' === trim( $t ) ) {
			if ( $citacao ) {
				/* Linha em branco dentro da citação: parágrafo novo, a citação segue. */
				if ( end( $citacao ) ) {
					$citacao[] = array();
				}
				continue;
			}
			$fecha_par(); $fecha_lista(); $fecha_tabela();
			continue;
		}
		if ( preg_match( '/^>\s?(.*)$/', $t, $m ) ) {
			$fecha_par(); $fecha_lista(); $fecha_tabela();
			if ( ! $citacao ) {
				$citacao = array( array() );
			}
			if ( '' !== trim( $m[1] ) ) {
				$citacao[ count( $citacao ) - 1 ][] = trim( $m[1] );
			} elseif ( end( $citacao ) ) {
				$citacao[] = array();
			}
			continue;
		}
		$fecha_citacao();
		if ( preg_match( '/^(#{1,6})\s+(.*)$/', $t, $m ) ) {
			$fecha_par(); $fecha_lista(); $fecha_tabela();
			$n     = strlen( $m[1] );
			$html .= '<h' . $n . '>' . $inline( $m[2] ) . '</h' . $n . ">\n";
			continue;
		}
		if ( preg_match( '/^\|(.+)\|\s*$/', $t, $m ) ) {
			$fecha_par(); $fecha_lista();
			if ( preg_match( '/^\|?\s*:?-{2,}/', $t ) ) {
				continue; // linha separadora da tabela
			}
			$tabela[] = explode( '|', $m[1] );
			continue;
		}
		if ( preg_match( '/^\s*[-*]\s+(.*)$/', $t, $m ) ) {
			$fecha_par(); $fecha_tabela();
			if ( 'ul' !== $lista ) { $fecha_lista(); $html .= "<ul>\n"; $lista = 'ul'; }
			$html .= '<li>' . $inline( $m[1] ) . "</li>\n";
			continue;
		}
		if ( preg_match( '/^\s*\d+[.)]\s+(.*)$/', $t, $m ) ) {
			$fecha_par(); $fecha_tabela();
			if ( 'ol' !== $lista ) { $fecha_lista(); $html .= "<ol>\n"; $lista = 'ol'; }
			$html .= '<li>' . $inline( $m[1] ) . "</li>\n";
			continue;
		}
		/* Linha que só tem um shortcode sai sozinha, sem <p>: o shortcode devolve
		   blocos (div, form, table) e <div> dentro de <p> é HTML inválido — o
		   navegador fecha o parágrafo no meio e a página fica remendada. */
		if ( preg_match( '/^\[[a-z0-9_]+(\s[^\]]*)?\]$/i', trim( $t ) ) ) {
			$fecha_par(); $fecha_lista(); $fecha_tabela();
			$html .= trim( $t ) . "\n";
			continue;
		}
		$fecha_lista(); $fecha_tabela();
		$par[] = trim( $t );
	}
	$fecha_par(); $fecha_lista(); $fecha_tabela(); $fecha_citacao(); $fecha_codigo();
	return $html;
}
}

/* ---------- aplicação dos itens ---------- */

if ( ! function_exists( 'aquametria_sync_aplicar_snippet' ) ) {
function aquametria_sync_aplicar_snippet( $item, &$estado ) {
	if ( ! function_exists( '\Code_Snippets\save_snippet' ) ) {
		return 'Code Snippets sem API PHP disponível';
	}
	$classe = class_exists( '\\Code_Snippets\\Model\\Snippet' ) ? '\\Code_Snippets\\Model\\Snippet'
		: ( class_exists( '\\Code_Snippets\\Snippet' ) ? '\\Code_Snippets\\Snippet' : '' );
	if ( '' === $classe ) {
		return 'classe Snippet do Code Snippets não encontrada';
	}
	$nome = isset( $item['nome'] ) ? trim( $item['nome'] ) : '';
	if ( '' === $nome || $nome === AQUAMETRIA_SYNC_NOME_PROPRIO ) {
		return 'pulado (nome vazio ou é o próprio Sync)';
	}
	$corpo = aquametria_sync_baixar( $item['arquivo'] );
	if ( is_wp_error( $corpo ) ) {
		return 'erro download: ' . $corpo->get_error_message();
	}
	if ( ! aquametria_sync_sha_ok( $corpo, isset( $item['sha256'] ) ? $item['sha256'] : '' ) ) {
		return 'sha256 divergente — não aplicado';
	}
	$codigo = preg_replace( '/^\s*<\?php\s*/', '', $corpo );

	$existente = null;
	foreach ( \Code_Snippets\get_snippets() as $s ) {
		if ( trim( $s->name ) === $nome ) {
			$existente = $s;
			break;
		}
	}
	$snip = $existente ? $existente : new $classe();
	if ( ! $existente ) {
		$snip->name = $nome;
	}
	$snip->code   = $codigo;
	$snip->desc   = isset( $item['descricao'] ) ? (string) $item['descricao'] : $snip->desc;
	$escopo       = isset( $item['escopo'] ) ? $item['escopo'] : 'global';
	$snip->scope  = in_array( $escopo, array( 'global', 'front-end', 'admin' ), true ) ? $escopo : 'global';
	// Grava INATIVO: o Code Snippets executa o código ao gravar snippet ativo (test_snippet_code) e,
	// se o snippet já estiver carregado nesta requisição, isso vira erro. A ativação vem depois.
	$snip->active = false;
	$ret = \Code_Snippets\save_snippet( $snip );
	$id  = is_object( $ret ) && isset( $ret->id ) ? (int) $ret->id : (int) $ret;
	if ( ! $id ) {
		return 'save_snippet falhou';
	}
	$re = \Code_Snippets\get_snippet( $id );
	if ( ! $re || strlen( (string) $re->code ) !== strlen( $codigo ) ) {
		return 'gravação não conferiu (tamanho diferente) — id ' . $id;
	}
	if ( ! empty( $item['ativo'] ) ) {
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
	} elseif ( function_exists( '\\Code_Snippets\\deactivate_snippet' ) ) {
		\Code_Snippets\deactivate_snippet( $id );
	}
	$estado['itens'][ 'snippet:' . $item['id'] ] = array( 'wp_id' => $id, 'sha256' => hash( 'sha256', $corpo ) );
	return 'ok (snippet #' . $id . ( $existente ? ' atualizado' : ' criado' ) . ')';
}
}

if ( ! function_exists( 'aquametria_sync_aplicar_conteudo' ) ) {
function aquametria_sync_aplicar_conteudo( $item, &$estado ) {
	$corpo = aquametria_sync_baixar( $item['arquivo'] );
	if ( is_wp_error( $corpo ) ) {
		return 'erro download: ' . $corpo->get_error_message();
	}
	if ( ! aquametria_sync_sha_ok( $corpo, isset( $item['sha256'] ) ? $item['sha256'] : '' ) ) {
		return 'sha256 divergente — não aplicado';
	}
	$tipo     = isset( $item['tipo'] ) ? $item['tipo'] : 'artigo';
	$post_type = ( 'artigo' === $tipo ) ? 'post' : 'page';
	$html     = ( '.html' === substr( $item['arquivo'], -5 ) ) ? $corpo : aquametria_sync_md( $corpo );
	$slug     = isset( $item['slug'] ) ? sanitize_title( $item['slug'] ) : sanitize_title( $item['titulo'] );

	$existente = get_posts( array(
		'post_type'   => $post_type,
		'post_status' => array( 'publish', 'draft', 'pending', 'private' ),
		'meta_key'    => '_aquametria_id',
		'meta_value'  => $item['id'],
		'numberposts' => 1,
	) );
	$dados = array(
		'post_type'    => $post_type,
		'post_title'   => wp_strip_all_tags( $item['titulo'] ),
		'post_name'    => $slug,
		'post_content' => $html,
		'post_status'  => 'publish',
	);
	if ( $existente ) {
		$dados['ID'] = $existente[0]->ID;
		$pid         = wp_update_post( wp_slash( $dados ), true );
	} else {
		$pid = wp_insert_post( wp_slash( $dados ), true );
	}
	if ( is_wp_error( $pid ) ) {
		return 'erro ao gravar: ' . $pid->get_error_message();
	}
	update_post_meta( $pid, '_aquametria_id', $item['id'] );
	update_post_meta( $pid, '_aquametria_cluster', isset( $item['cluster'] ) ? $item['cluster'] : '' );
	update_post_meta( $pid, '_aquametria_verificado_em', isset( $item['verificado_em'] ) ? $item['verificado_em'] : '' );
	update_post_meta( $pid, '_aquametria_fontes', isset( $item['fontes'] ) ? wp_json_encode( $item['fontes'] ) : '' );
	$estado['itens'][ 'conteudo:' . $item['id'] ] = array( 'wp_id' => $pid, 'sha256' => hash( 'sha256', $corpo ) );
	return 'ok (' . $post_type . ' #' . $pid . ( $existente ? ' atualizado' : ' criado' ) . ')';
}
}

if ( ! function_exists( 'aquametria_sync_aplicar_dados' ) ) {
function aquametria_sync_aplicar_dados( $item, &$estado ) {
	$corpo = aquametria_sync_baixar( $item['arquivo'] );
	if ( is_wp_error( $corpo ) ) {
		return 'erro download: ' . $corpo->get_error_message();
	}
	if ( ! aquametria_sync_sha_ok( $corpo, isset( $item['sha256'] ) ? $item['sha256'] : '' ) ) {
		return 'sha256 divergente — não aplicado';
	}
	$formato = isset( $item['formato'] ) ? $item['formato'] : 'json';
	if ( 'json' === $formato ) {
		$dec = json_decode( $corpo, true );
		if ( null === $dec ) {
			return 'JSON inválido';
		}
		$valor = $dec;
	} else {
		$valor = array( 'formato' => $formato, 'bruto' => $corpo );
	}
	$chave = 'aquametria_dados_' . sanitize_key( $item['id'] );
	if ( false === get_option( $chave ) ) {
		add_option( $chave, $valor, '', 'no' );
	} else {
		update_option( $chave, $valor, 'no' );
	}
	$estado['itens'][ 'dados:' . $item['id'] ] = array( 'option' => $chave, 'sha256' => hash( 'sha256', $corpo ) );
	return 'ok (option ' . $chave . ')';
}
}

/* ---------- execução ---------- */

if ( ! function_exists( 'aquametria_sync_executar' ) ) {
function aquametria_sync_executar( $forcar = false ) {
	$estado = aquametria_sync_estado();
	$bruto  = aquametria_sync_baixar( 'manifest.json' );
	if ( is_wp_error( $bruto ) ) {
		aquametria_sync_log( $estado, 'FALHA manifest: ' . $bruto->get_error_message() );
		update_option( 'aquametria_sync_estado', $estado, 'no' );
		return $estado;
	}
	$m = json_decode( $bruto, true );
	if ( ! is_array( $m ) || ! isset( $m['revisao'] ) ) {
		aquametria_sync_log( $estado, 'FALHA manifest: JSON inválido' );
		update_option( 'aquametria_sync_estado', $estado, 'no' );
		return $estado;
	}
	if ( ! $forcar && (int) $m['revisao'] === (int) $estado['revisao'] ) {
		$estado['ultimo'] = current_time( 'mysql' );
		update_option( 'aquametria_sync_estado', $estado, 'no' );
		return $estado; // nada novo
	}

	$aplicados = 0;
	$pulados   = 0;
	foreach ( array( 'snippets', 'conteudo', 'dados' ) as $grupo ) {
		if ( empty( $m[ $grupo ] ) || ! is_array( $m[ $grupo ] ) ) {
			continue;
		}
		foreach ( $m[ $grupo ] as $item ) {
			if ( empty( $item['id'] ) || empty( $item['arquivo'] ) ) {
				continue;
			}
			if ( empty( $item['publicar'] ) || true !== $item['publicar'] ) {
				$pulados++;
				continue;
			}
			$chave = rtrim( $grupo, 's' ) . ':' . $item['id'];
			if ( 'snippets' === $grupo ) { $chave = 'snippet:' . $item['id']; }
			if ( ! $forcar && ! empty( $item['sha256'] ) && isset( $estado['itens'][ $chave ]['sha256'] )
				&& hash_equals( $estado['itens'][ $chave ]['sha256'], strtolower( $item['sha256'] ) ) ) {
				continue; // já aplicado nesta versão
			}
			try {
				if ( 'snippets' === $grupo ) {
					$res = aquametria_sync_aplicar_snippet( $item, $estado );
				} elseif ( 'conteudo' === $grupo ) {
					$res = aquametria_sync_aplicar_conteudo( $item, $estado );
				} else {
					$res = aquametria_sync_aplicar_dados( $item, $estado );
				}
			} catch ( \Throwable $e ) {
				$res = 'ERRO ' . get_class( $e ) . ': ' . $e->getMessage() . ' (' . basename( $e->getFile() ) . ':' . $e->getLine() . ')';
			}
			aquametria_sync_log( $estado, $grupo . '/' . $item['id'] . ': ' . $res );
			if ( 0 === strpos( $res, 'ok' ) ) {
				$aplicados++;
			}
		}
	}
	$estado['revisao'] = (int) $m['revisao'];
	$estado['ultimo']  = current_time( 'mysql' );
	aquametria_sync_log( $estado, 'revisão ' . $m['revisao'] . ': ' . $aplicados . ' aplicado(s), ' . $pulados . ' aguardando desembarque' . ( $forcar ? ' [forçado]' : '' ) );
	update_option( 'aquametria_sync_estado', $estado, 'no' );
	if ( function_exists( 'wp_cache_flush' ) ) {
		wp_cache_flush();
	}
	return $estado;
}
}

/* ---------- gatilhos ---------- */

add_filter( 'cron_schedules', function ( $s ) {
	$s['aquametria_30min'] = array( 'interval' => 1800, 'display' => 'Aquametria: a cada 30 min' );
	return $s;
} );

add_action( 'init', function () {
	if ( ! wp_next_scheduled( 'aquametria_sync_evento' ) ) {
		wp_schedule_event( time() + 120, 'aquametria_30min', 'aquametria_sync_evento' );
	}
	$token = filter_input( INPUT_GET, 'aquametria_sync', FILTER_DEFAULT );
	if ( is_string( $token ) && '' !== $token ) {
		if ( ! hash_equals( aquametria_sync_token(), $token ) ) {
			status_header( 403 );
			exit( 'token inválido' );
		}
		$forcar = '1' === (string) filter_input( INPUT_GET, 'forcar', FILTER_DEFAULT );
		$e      = aquametria_sync_executar( $forcar );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array( 'versao_sync' => AQUAMETRIA_SYNC_VERSAO, 'revisao' => $e['revisao'], 'ultimo' => $e['ultimo'], 'log' => array_slice( $e['log'], 0, 10 ) ), JSON_UNESCAPED_UNICODE );
		exit;
	}
} );

add_action( 'aquametria_sync_evento', function () {
	aquametria_sync_executar( false );
} );

add_action( 'rest_api_init', function () {
	register_rest_route( 'aquametria/v1', '/status', array(
		'methods'             => 'GET',
		'permission_callback' => '__return_true',
		'callback'            => function () {
			$e = aquametria_sync_estado();
			return array( 'versao_sync' => AQUAMETRIA_SYNC_VERSAO, 'revisao' => $e['revisao'], 'ultimo' => $e['ultimo'], 'log' => array_slice( $e['log'], 0, 15 ) );
		},
	) );
	register_rest_route( 'aquametria/v1', '/sync', array(
		'methods'             => 'POST',
		'permission_callback' => function () { return current_user_can( 'manage_options' ); },
		'callback'            => function ( $req ) {
			$e = aquametria_sync_executar( (bool) $req->get_param( 'forcar' ) );
			return array( 'revisao' => $e['revisao'], 'ultimo' => $e['ultimo'], 'log' => array_slice( $e['log'], 0, 15 ), 'itens' => $e['itens'] );
		},
	) );
	register_rest_route( 'aquametria/v1', '/token', array(
		'methods'             => 'GET',
		'permission_callback' => function () { return current_user_can( 'manage_options' ); },
		'callback'            => function () {
			return array( 'token' => aquametria_sync_token(), 'url' => home_url( '/?aquametria_sync=' . aquametria_sync_token() ) );
		},
	) );
} );

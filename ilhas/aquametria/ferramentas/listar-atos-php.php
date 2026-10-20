<?php
/**
 * LISTA OS ATOS SOBRE IRMAO de UM arquivo `.php` de `ferramentas/`, lidos pelo
 * TOKENIZADOR DO PROPRIO PHP — `token_get_all()` —, nunca por varredura de
 * texto.
 *
 * Uso:  php ferramentas/listar-atos-php.php <arquivo.php>
 * Saida: JSON { atos: [...], atribuicoes: {...} }
 *
 * POR QUE ESTE ARQUIVO EXISTE, e a data e 20/10/2026
 * ---------------------------------------------------
 * O item 7 do fecho de 20/10/2026 (13h18Z) deixou escrito que os `.mjs` e os
 * `.php` desta pasta carregam e invocam irmaos e que NINGUEM os mediu — a
 * `regua-alvos-de-portao.py` le a arvore sintatica do Python e diz, no proprio
 * cabecalho, que esses 40 arquivos estao fora do alcance dela.
 *
 * Quem le PHP e o PHP. Esta pasta ja faz isso desde 09/09/2026, no
 * `proteger-funcoes.php`, que usa `token_get_all()` para envolver declaracao de
 * funcao — entao o tokenizador da propria linguagem e idioma desta ilha e nao
 * invencao deste arquivo. Varredura de texto nao distingue string de comentario
 * de codigo, e foi exatamente esse o defeito que a `regua-classes-da-bancada.py`
 * pagou em 20/10 de manha (classificava portao pela marca no TEXTO, prosa
 * incluida).
 *
 * ESTE ARQUIVO NAO AFIRMA NADA E NAO DECIDE POSICAO. Ele devolve a SEQUENCIA DE
 * OPERANDOS de cada sitio de ato, como o tokenizador os ve, e quem decide se o
 * nome do irmao esta literal, indireto ou construido e a
 * `regua-alvos-nao-python.py`, que usa a mesma regra da regua irma. Dividir
 * assim e o que permite encenar mundo que nao existe no disco: o Python recebe
 * texto, nunca caminho.
 *
 * OS TRES ATOS, traduzidos para o idioma do PHP
 * ----------------------------------------------
 *   * carrega: `require`, `require_once`, `include`, `include_once` e `eval` —
 *     o `eval( file_get_contents( X ) )` desta pasta e carga, nao leitura, e por
 *     isso o `file_get_contents` de dentro dele NAO conta uma segunda vez.
 *   * invoca: `exec`, `shell_exec`, `system`, `passthru`, `proc_open`, `popen`.
 *   * abre:   `file_get_contents`, `file`, `fopen`, `readfile`.
 *
 * `__FILE__` e devolvido como operando proprio porque o `teste-atualizador-sync.php`
 * se re-invoca por `exec( ... __FILE__ ... )`: isso e ato sobre SI MESMO, e a
 * regua irma ja descarta `alvo == quem`. Sem este operando o sitio sairia como
 * "nao resolvido" e mentiria sobre um limite que nao existe.
 */

$arquivo = $argv[1] ?? '';
if ( $arquivo === '' || ! is_file( $arquivo ) ) {
	fwrite( STDERR, "uso: php listar-atos-php.php <arquivo.php>\n" );
	exit( 2 );
}

$CARGA = array( T_REQUIRE, T_REQUIRE_ONCE, T_INCLUDE, T_INCLUDE_ONCE, T_EVAL );
$INVOCA = array( 'exec', 'shell_exec', 'system', 'passthru', 'proc_open', 'popen' );
$ABRE   = array( 'file_get_contents', 'file', 'fopen', 'readfile' );

$tokens = token_get_all( (string) file_get_contents( $arquivo ) );
$n      = count( $tokens );

/** Pula espaco e comentario para frente, devolvendo o indice do proximo token util. */
function aqm_proximo( $tokens, $i ) {
	$n = count( $tokens );
	while ( $i < $n ) {
		$t = $tokens[ $i ];
		if ( is_array( $t ) && in_array( $t[0], array( T_WHITESPACE, T_COMMENT, T_DOC_COMMENT ), true ) ) {
			$i++;
			continue;
		}
		return $i;
	}
	return $n;
}

/** Fim do span de uma chamada: do `(` ate o `)` que o fecha. */
function aqm_fim_parenteses( $tokens, $i ) {
	$n     = count( $tokens );
	$prof  = 0;
	for ( $j = $i; $j < $n; $j++ ) {
		$t = $tokens[ $j ];
		if ( $t === '(' ) {
			$prof++;
		} elseif ( $t === ')' ) {
			$prof--;
			if ( 0 === $prof ) {
				return $j;
			}
		}
	}
	return $n - 1;
}

/** Fim do span de um `require`/`include` sem parenteses: ate o `;` de nivel zero. */
function aqm_fim_instrucao( $tokens, $i ) {
	$n    = count( $tokens );
	$prof = 0;
	for ( $j = $i; $j < $n; $j++ ) {
		$t = $tokens[ $j ];
		if ( '(' === $t || '[' === $t ) {
			$prof++;
		} elseif ( ')' === $t || ']' === $t ) {
			$prof--;
		} elseif ( ';' === $t && 0 === $prof ) {
			return $j;
		}
	}
	return $n - 1;
}

/**
 * A SEQUENCIA DE OPERANDOS de um span, na ordem em que o tokenizador os ve.
 *
 * Nao interpreta nada: so diz o que esta ali. `buraco` e toda interpolacao de
 * variavel dentro de string dupla ou heredoc — o pedaco do nome que o
 * tokenizador NAO conhece, e que e a unica razao pela qual um nome pode nao
 * estar escrito no arquivo.
 */
function aqm_operandos( $tokens, $de, $ate ) {
	$fora      = array();
	$em_string = false;
	for ( $j = $de; $j <= $ate; $j++ ) {
		$t = $tokens[ $j ];
		if ( '"' === $t ) {
			$em_string = ! $em_string;
			continue;
		}
		if ( ! is_array( $t ) ) {
			continue;
		}
		switch ( $t[0] ) {
			case T_CONSTANT_ENCAPSED_STRING:
				$fora[] = array( 'k' => 'str', 'v' => aqm_sem_aspas( $t[1] ) );
				break;
			case T_ENCAPSED_AND_WHITESPACE:
				$fora[] = array( 'k' => 'str', 'v' => $t[1] );
				break;
			case T_DIR:
				$fora[] = array( 'k' => 'dir' );
				break;
			case T_FILE:
				$fora[] = array( 'k' => 'file' );
				break;
			case T_VARIABLE:
				$fora[] = array( 'k' => $em_string ? 'buraco' : 'var', 'v' => $t[1] );
				break;
			case T_CURLY_OPEN:
			case T_DOLLAR_OPEN_CURLY_BRACES:
				$fora[] = array( 'k' => 'buraco', 'v' => '{...}' );
				break;
			case T_STRING:
				$fora[] = array( 'k' => 'chamada', 'v' => $t[1] );
				break;
			case T_START_HEREDOC:
				$em_string = true;
				break;
			case T_END_HEREDOC:
				$em_string = false;
				break;
		}
	}
	return $fora;
}

/** Tira as aspas de uma string literal e desfaz as duas escapes que importam. */
function aqm_sem_aspas( $texto ) {
	$dentro = substr( $texto, 1, -1 );
	return str_replace( array( "\\'", '\\"', '\\\\' ), array( "'", '"', '\\' ), $dentro );
}

/** O texto cru do span, para o relatorio poder mostrar o que nao resolveu. */
function aqm_texto( $tokens, $de, $ate ) {
	$s = '';
	for ( $j = $de; $j <= $ate; $j++ ) {
		$t = $tokens[ $j ];
		$s .= is_array( $t ) ? $t[1] : $t;
	}
	return trim( preg_replace( '/\s+/', ' ', $s ) );
}

$atos        = array();
$atribuicoes = array();
$consumido   = array();   // indices ja contados por um ato de fora (eval -> file_get_contents)

for ( $i = 0; $i < $n; $i++ ) {
	$t = $tokens[ $i ];

	// --- atribuicao: $var = <expr>;  e  foreach ( <expr> as $var )
	if ( is_array( $t ) && T_VARIABLE === $t[0] ) {
		$k = aqm_proximo( $tokens, $i + 1 );
		if ( $k < $n && '=' === $tokens[ $k ] ) {
			$fim = aqm_fim_instrucao( $tokens, $k + 1 );
			$atribuicoes[ $t[1] ][] = aqm_operandos( $tokens, $k + 1, $fim );
		}
	}
	if ( is_array( $t ) && T_AS === $t[0] ) {
		$k = aqm_proximo( $tokens, $i + 1 );
		if ( $k < $n && is_array( $tokens[ $k ] ) && T_VARIABLE === $tokens[ $k ][0] ) {
			// o `foreach ( glob(...) as $arquivo )` desta pasta: o nome do irmao vem
			// da pasta e nao do texto, e e o idioma de quem varre tudo.
			$abre = $i;
			while ( $abre > 0 && '(' !== $tokens[ $abre ] ) {
				$abre--;
			}
			if ( $abre > 0 ) {
				$atribuicoes[ $tokens[ $k ][1] ][] = aqm_operandos( $tokens, $abre + 1, $i - 1 );
			}
		}
	}

	if ( in_array( $i, $consumido, true ) ) {
		continue;
	}

	// --- carga por palavra da linguagem
	if ( is_array( $t ) && in_array( $t[0], $CARGA, true ) ) {
		$k = aqm_proximo( $tokens, $i + 1 );
		$fim = ( $k < $n && '(' === $tokens[ $k ] ) ? aqm_fim_parenteses( $tokens, $k ) : aqm_fim_instrucao( $tokens, $i + 1 );
		$de  = ( $k < $n && '(' === $tokens[ $k ] ) ? $k + 1 : $i + 1;
		$atos[] = array(
			'tipo'      => 'carrega',
			'linha'     => $t[2],
			'operandos' => aqm_operandos( $tokens, $de, $fim ),
			'expressao' => aqm_texto( $tokens, $de, $fim ),
		);
		for ( $j = $de; $j <= $fim; $j++ ) {
			$consumido[] = $j;
		}
		continue;
	}

	// --- invocacao e leitura, por nome de funcao
	if ( is_array( $t ) && T_STRING === $t[0] ) {
		$nome = strtolower( $t[1] );
		$tipo = in_array( $nome, $INVOCA, true ) ? 'invoca' : ( in_array( $nome, $ABRE, true ) ? 'abre' : null );
		if ( null === $tipo ) {
			continue;
		}
		$k = aqm_proximo( $tokens, $i + 1 );
		if ( $k >= $n || '(' !== $tokens[ $k ] ) {
			continue;   // `file` como parte de outro nome, nao chamada
		}
		$anterior = $i - 1;
		while ( $anterior > 0 && is_array( $tokens[ $anterior ] ) && T_WHITESPACE === $tokens[ $anterior ][0] ) {
			$anterior--;
		}
		if ( $anterior > 0 && is_array( $tokens[ $anterior ] ) && in_array( $tokens[ $anterior ][0], array( T_OBJECT_OPERATOR, T_DOUBLE_COLON, T_FUNCTION ), true ) ) {
			continue;   // metodo ou declaracao homonima, nao a funcao do PHP
		}
		$fim = aqm_fim_parenteses( $tokens, $k );
		$atos[] = array(
			'tipo'      => $tipo,
			'linha'     => $t[2],
			'operandos' => aqm_operandos( $tokens, $k + 1, $fim ),
			'expressao' => aqm_texto( $tokens, $k + 1, $fim ),
		);
	}
}

echo json_encode(
	array( 'atos' => $atos, 'atribuicoes' => $atribuicoes ),
	JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE
), "\n";

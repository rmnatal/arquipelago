/**
 * Clube do Mosaico F2 — Qual cola usar no mosaico, e qual rejunte
 * Versão 1.0.0 (11/09/2026) — bloco 4 da fila, a primeira ferramenta da ilha e
 * a primeira página de nível 3 dela.
 *
 * O QUE ELA RESPONDE, e por que ganha (seção 14.9 do ARQUIPELAGO.md): a SERP de
 * "qual cola para mosaico" é blog sem fabricante, sem código de documento, sem
 * data e sem separar dentro de casa de sol e chuva — o bloco 1 mediu isso
 * consulta a consulta. Esta página responde a mesma pergunta com a declaração
 * do próprio fabricante do adesivo, e é a única em português que diz o que NÃO
 * usar, e por quê.
 *
 * ------------------------------------------------------------------------
 * AS QUATRO DECISÕES DE DESENHO, e a cicatriz que cada uma evita
 * ------------------------------------------------------------------------
 *
 * 1. A RESPOSTA É SERVIDA PELO SERVIDOR, NUNCA CALCULADA NO NAVEGADOR.
 *    O formulário é um GET para a própria página e o PHP monta a resposta. Não
 *    existe uma linha de decisão em JavaScript, e isso não é purismo: era o
 *    caminho mais curto para o defeito que a seção 5 do contrato nomeia —
 *    ferramenta que calcula no navegador mostra a um modelo de linguagem um
 *    formulário VAZIO. Aqui todo estado da entrada é HTML servido de verdade,
 *    e a segunda metade da mesma decisão é que não há régua duplicada entre PHP
 *    e JS para as duas se separarem em silêncio.
 *    O preço disso é URL com parâmetro, e ele é pago na mesma linha: estado com
 *    parâmetro sai com `noindex, follow` e com `canonical` para o endereço
 *    limpo. Quem entra no índice é a página-âncora, uma só (seções 14.1 e 14.4).
 *
 * 2. A ELEGIBILIDADE É RECOMPUTADA DAS DECLARAÇÕES, NUNCA DIGITADA.
 *    As cinco regras da cola e as quatro do rejunte estão escritas em
 *    `dados/esquema-banco.json` e implementadas aqui em PHP; `ferramentas/
 *    validar-banco.py` as implementa em Python, separado, e as duas metades são
 *    comparadas contra as matrizes escritas À MÃO no mesmo esquema. É a trava da
 *    seção 8: quem confere escreve a própria régua.
 *
 * 3. O BLOCO DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA (seção 7, cicatriz da
 *    Robometria de 10/09/2026). Os dez itens do banco estão com `afiliado.url`
 *    vazio, e mesmo assim o bloco nasce: ele reserva o lugar, diz "link de loja
 *    em breve" e a ilha reporta quantos itens esperam link. O link de
 *    procedência é texto pequeno, `rel="nofollow noopener"`, nunca botão.
 *
 * 4. A CATEGORIA É PARTE DA PERGUNTA. A régua da cola decide sobre BASE; a do
 *    rejunte, sobre LARGURA DE JUNTA. São duas funções separadas de propósito —
 *    rejunte não toca a base, e traduzir uma no vocabulário da outra produz uma
 *    afirmação sem sentido que entra calada no cálculo. Foi o defeito que o
 *    bloco 3c encontrou no validador em 11/09/2026.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTA PÁGINA DIZ QUE NÃO SABE
 * ------------------------------------------------------------------------
 * Duas faixas ficam sem recomendação publicada e a página escreve isso: base de
 * plástico (nenhum fabricante do banco declara colagem sobre plástico — o
 * neutro fala em "certos tipos de plástico", que não nomeia tipo nenhum) e peça
 * em contato permanente com água (a única declaração de colagem submersa que a
 * ilha tem é material de imprensa, nível 4, abaixo do mínimo). Silêncio parece
 * defeito; texto honesto, não.
 */

if ( ! defined( 'CDM_F2_VERSAO' ) ) {
	define( 'CDM_F2_VERSAO', '1.1.0' );
}
if ( ! defined( 'CDM_F2_SLUG' ) ) {
	/* Nível 3 com mãe /materiais/ direto — dois níveis em vez de três, estado de
	   transição declarado na seção 2 do ARVORE.md. A categoria definitiva
	   (`colas-e-adesivos`) só nasce quando tiver três filhas com dado real (16.5),
	   e mover a URL depois disso é proibido para página posicionada (12.1) —
	   por isso a escolha de hoje é a mãe que JÁ existe. */
	define( 'CDM_F2_SLUG', 'materiais/qual-cola-usar-no-mosaico' );
}
if ( ! defined( 'CDM_F2_TITULO' ) ) {
	/* UM NOME POR PÁGINA, em toda superfície: é este texto que sai no cartão da
	   home, no cartão do Guia, no degrau da trilha, no H1 e no <title>. A
	   Aquametria pagou em 11/09/2026 por ter oito páginas em que o degrau e o H1
	   diziam nomes diferentes a uma linha de distância. 41 caracteres; com o
	   sufixo do site o <title> fica em 60, abaixo do teto de 65. */
	define( 'CDM_F2_TITULO', 'Qual cola usar no mosaico, e qual rejunte' );
}

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — a página, o cartão e o degrau da trilha
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	$paginas[ CDM_F2_SLUG ] = array(
		'titulo'   => CDM_F2_TITULO,
		'conteudo' => '[cdm_f2]',
		'pai'      => 'materiais',
	);

	return $paginas;
} );

add_filter( 'cdm_ferramentas', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $f ) {
		if ( isset( $f['codigo'] ) && 'F2' === $f['codigo'] ) {
			$lista[ $i ]['titulo'] = CDM_F2_TITULO;
			$lista[ $i ]['slug']   = CDM_F2_SLUG;
			$lista[ $i ]['estado'] = 'publicada';
		}
	}

	return $lista;
} );

/* ---------------------------------------------------------------------------
 * 2. O banco, lido das options que o Sync grava
 *
 * Sem banco a página NÃO inventa recomendação: ela diz que a medição não chegou.
 * É a mesma trava que a Robometria escreveu em 11/09/2026 depois de descobrir
 * que a option que alimentava os números dela nunca existira no site, porque o
 * item do manifest estava com publicar=false e ninguém tinha olhado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_banco' ) ) {
function cdm_f2_banco() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}

	$esquema  = get_option( 'clubedomosaico_dados_esquema-banco' );
	$colas    = get_option( 'clubedomosaico_dados_materiais-colas' );
	$rejuntes = get_option( 'clubedomosaico_dados_materiais-rejuntes' );

	$materiais = array();
	foreach ( array( $colas, $rejuntes ) as $arquivo ) {
		if ( ! is_array( $arquivo ) || empty( $arquivo['materiais'] ) || ! is_array( $arquivo['materiais'] ) ) {
			continue;
		}
		foreach ( $arquivo['materiais'] as $m ) {
			if ( empty( $m['id'] ) || 'ativo' !== ( isset( $m['status'] ) ? $m['status'] : '' ) ) {
				continue;
			}
			$materiais[ $m['id'] ] = $m;
		}
	}
	ksort( $materiais );

	$banco = array(
		'esquema'   => is_array( $esquema ) ? $esquema : array(),
		'materiais' => $materiais,
		'colas'     => is_array( $colas ) ? $colas : array(),
		'rejuntes'  => is_array( $rejuntes ) ? $rejuntes : array(),
		'completo'  => ( is_array( $esquema ) && $materiais ),
	);

	return $banco;
}
}

if ( ! function_exists( 'cdm_f2_normalizar' ) ) {
/**
 * Minúsculas, sem acento, espaços colapsados — e a comparação com o mapa de
 * termos é EXATA depois disso. "ceramica" (a superfície sobre a qual se cola) e
 * "ceramicas" (a peça que se assenta) são termos diferentes de propósito, e
 * confundi-los foi exatamente o defeito que o bloco 3 achou na cimentcola.
 */
function cdm_f2_normalizar( $texto ) {
	$t = mb_strtolower( trim( (string) $texto ), 'UTF-8' );
	$de = array( 'á','à','â','ã','ä','é','ê','ë','í','ï','ó','ô','õ','ö','ú','ü','ç','ñ' );
	$pa = array( 'a','a','a','a','a','e','e','e','i','i','o','o','o','o','u','u','c','n' );
	$t  = str_replace( $de, $pa, $t );

	return preg_replace( '/\s+/u', ' ', $t );
}
}

if ( ! function_exists( 'cdm_f2_mapa_cola' ) ) {
/** O mapa de termos do fabricante, do esquema, indexado pelo termo normalizado. */
function cdm_f2_mapa_cola() {
	static $mapa = null;
	if ( null !== $mapa ) {
		return $mapa;
	}
	$banco = cdm_f2_banco();
	$fonte = isset( $banco['esquema']['mapa_de_termos_do_fabricante'] ) ? $banco['esquema']['mapa_de_termos_do_fabricante'] : array();
	$mapa  = array( 'termos' => array(), 'vagos' => array(), 'nao_traduz' => array() );

	foreach ( ( isset( $fonte['termos'] ) ? $fonte['termos'] : array() ) as $t ) {
		$chave                    = cdm_f2_normalizar( $t['literal'] );
		$mapa['termos'][ $chave ] = array(
			'base'     => isset( $t['base'] ) ? $t['base'] : array(),
			'ambiente' => isset( $t['ambiente'] ) ? $t['ambiente'] : array(),
		);
		if ( ! empty( $t['vago'] ) ) {
			$mapa['vagos'][ $chave ] = true;
		}
	}
	foreach ( ( isset( $fonte['termos_que_nao_traduzem'] ) ? $fonte['termos_que_nao_traduzem'] : array() ) as $t ) {
		$mapa['nao_traduz'][ cdm_f2_normalizar( $t['literal'] ) ] = true;
	}

	return $mapa;
}
}

if ( ! function_exists( 'cdm_f2_traduzir_cola' ) ) {
/**
 * Uma lista literal do fabricante vira vocabulário da ilha.
 *
 * Devolve também QUAIS literais casaram com cada alvo: é esse pedaço que vai
 * para a tela como "a declaração que fez o produto entrar" (seção 7). Sem ele a
 * página diria "serve" sem dizer por quê, que é a metade que separa esta ilha
 * de um blog.
 */
function cdm_f2_traduzir_cola( $lista ) {
	$mapa = cdm_f2_mapa_cola();
	$out  = array( 'base' => array(), 'ambiente' => array(), 'vago' => array(), 'literais' => array() );

	foreach ( (array) $lista as $literal ) {
		$chave = cdm_f2_normalizar( $literal );
		if ( isset( $mapa['nao_traduz'][ $chave ] ) || ! isset( $mapa['termos'][ $chave ] ) ) {
			continue;
		}
		$alvo = $mapa['termos'][ $chave ];
		foreach ( $alvo['base'] as $b ) {
			if ( isset( $mapa['vagos'][ $chave ] ) ) {
				$out['vago'][ $b ] = true;
			} else {
				$out['base'][ $b ] = true;
			}
			$out['literais'][ $b ][] = $literal;
		}
		foreach ( $alvo['ambiente'] as $a ) {
			$out['ambiente'][ $a ]   = true;
			$out['literais'][ $a ][] = $literal;
		}
	}

	return $out;
}
}

if ( ! function_exists( 'cdm_f2_nivel' ) ) {
/** O nível da fonte de um material é o MELHOR (menor) que ele tem. */
function cdm_f2_nivel( $m ) {
	$niveis = array();
	foreach ( (array) ( isset( $m['fontes'] ) ? $m['fontes'] : array() ) as $f ) {
		if ( isset( $f['nivel'] ) ) {
			$niveis[] = (int) $f['nivel'];
		}
	}

	return $niveis ? min( $niveis ) : 9;
}
}

if ( ! function_exists( 'cdm_f2_perfil_cola' ) ) {
/** As declarações de um adesivo, já traduzidas para o vocabulário da ilha. */
function cdm_f2_perfil_cola( $m ) {
	static $cache = array();
	$id = isset( $m['id'] ) ? $m['id'] : '';
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$d = isset( $m['declaracoes'] ) ? $m['declaracoes'] : array();

	$ind    = cdm_f2_traduzir_cola( isset( $d['indicado_para'] ) ? $d['indicado_para'] : array() );
	$pro1   = cdm_f2_traduzir_cola( isset( $d['nao_usar_em'] ) ? $d['nao_usar_em'] : array() );
	$pro2   = cdm_f2_traduzir_cola( isset( $d['nao_indicado_para'] ) ? $d['nao_indicado_para'] : array() );
	$naorec = cdm_f2_traduzir_cola( isset( $d['nao_recomendado_em'] ) ? $d['nao_recomendado_em'] : array() );
	$delim  = cdm_f2_traduzir_cola( isset( $d['ambientes_declarados'] ) ? $d['ambientes_declarados'] : array() );
	$resist = cdm_f2_traduzir_cola( isset( $d['resistencias_declaradas'] ) ? $d['resistencias_declaradas'] : array() );

	$literais_proibicao = array();
	foreach ( array( $pro1, $pro2 ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais_proibicao[ $alvo ] = array_merge( isset( $literais_proibicao[ $alvo ] ) ? $literais_proibicao[ $alvo ] : array(), $ls );
		}
	}
	$literais_cobertura = array();
	foreach ( array( $delim, $resist, $ind ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais_cobertura[ $alvo ] = array_merge( isset( $literais_cobertura[ $alvo ] ) ? $literais_cobertura[ $alvo ] : array(), $ls );
		}
	}

	$cache[ $id ] = array(
		'bases_indicadas'       => $ind['base'],
		'bases_proibidas'       => $pro1['base'] + $pro2['base'],
		'bases_vagas'           => $ind['vago'] + $naorec['base'] + $naorec['vago'],
		'ambientes_proibidos'   => $pro1['ambiente'] + $pro2['ambiente'],
		'ambientes_delimitados' => $delim['ambiente'],
		'ambientes_cobertos'    => $delim['ambiente'] + $resist['ambiente'] + $ind['ambiente'],
		'literais_indicacao'    => $ind['literais'],
		'literais_proibicao'    => $literais_proibicao,
		'literais_cobertura'    => $literais_cobertura,
		'nivel'                 => cdm_f2_nivel( $m ),
	);

	return $cache[ $id ];
}
}

if ( ! function_exists( 'cdm_f2_criticos_cola' ) ) {
function cdm_f2_criticos_cola() {
	$banco = cdm_f2_banco();
	$r     = isset( $banco['esquema']['regras_de_elegibilidade']['4_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes'] )
		? $banco['esquema']['regras_de_elegibilidade']['4_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes']
		: array();

	return array_flip( (array) $r );
}
}

if ( ! function_exists( 'cdm_f2_nivel_maximo' ) ) {
function cdm_f2_nivel_maximo() {
	$banco = cdm_f2_banco();

	return isset( $banco['esquema']['escada_de_fontes']['nivel_minimo_para_recomendacao_primaria'] )
		? (int) $banco['esquema']['escada_de_fontes']['nivel_minimo_para_recomendacao_primaria']
		: 3;
}
}

if ( ! function_exists( 'cdm_f2_avaliar_cola' ) ) {
/**
 * As cinco regras, na ordem em que elas decidem.
 * Devolve array( situacao, score ). Situação: recomendado | ressalva |
 * proibido | silencio.
 */
function cdm_f2_avaliar_cola( $m, $base, $ambiente ) {
	$p = cdm_f2_perfil_cola( $m );

	/* 1 — proibição vence indicação dentro do mesmo produto. O acético indica
	   "alumínio comum e anodizado" e proíbe "metal corrosível, zinco e chapa
	   galvanizada": vale o conjunto MAIS ESTREITO, porque quem monta mosaico não
	   sabe dizer se a chapa dela é galvanizada. */
	if ( isset( $p['bases_proibidas'][ $base ] ) || isset( $p['ambientes_proibidos'][ $ambiente ] ) ) {
		return array( 'proibido', 0 );
	}
	/* 2 — base sem declaração não é recomendação. Silêncio não vira "pode". */
	if ( ! isset( $p['bases_indicadas'][ $base ] ) ) {
		return array( 'silencio', 0 );
	}
	/* 3 — quem delimita ambiente fica fechado nele. */
	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}
	/* 4 — ambiente crítico exige declaração explícita. */
	$criticos = cdm_f2_criticos_cola();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}

	$score = 2 + ( isset( $p['ambientes_cobertos'][ $ambiente ] ) ? 2 : 0 );

	/* 5 — nível de fonte limita a recomendação primária. */
	if ( $p['nivel'] > cdm_f2_nivel_maximo() ) {
		return array( 'ressalva', $score );
	}

	return array( 'recomendado', $score );
}
}

if ( ! function_exists( 'cdm_f2_celula_cola' ) ) {
/**
 * A célula base × ambiente. SÓ materiais de categoria cola entram aqui — a
 * categoria é parte da pergunta, e um rejunte listado como "eliminado por
 * silêncio" numa célula de colagem é uma frase sem sentido.
 */
function cdm_f2_celula_cola( $base, $ambiente ) {
	$banco       = cdm_f2_banco();
	$recomendados = array();
	$ressalva     = array();
	$proibidos    = array();
	$silencio     = array();

	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'cola' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			continue;
		}
		list( $situacao, $score ) = cdm_f2_avaliar_cola( $m, $base, $ambiente );
		if ( 'recomendado' === $situacao ) {
			$recomendados[ $id ] = $score;
		} elseif ( 'ressalva' === $situacao ) {
			$ressalva[] = $id;
		} elseif ( 'proibido' === $situacao ) {
			$proibidos[] = $id;
		} else {
			$silencio[] = $id;
		}
	}

	$topo   = array();
	$abaixo = array();
	if ( $recomendados ) {
		$maior = max( $recomendados );
		foreach ( $recomendados as $id => $score ) {
			if ( $score === $maior ) {
				$topo[] = $id;
			} else {
				$abaixo[] = $id;
			}
		}
	}
	sort( $topo );
	sort( $abaixo );
	sort( $ressalva );
	sort( $proibidos );
	sort( $silencio );

	return array(
		'recomendados_topo'        => $topo,
		'elegiveis_abaixo_do_topo' => $abaixo,
		'mencionados_com_ressalva' => $ressalva,
		'eliminados_por_proibicao' => $proibidos,
		'eliminados_por_silencio'  => $silencio,
	);
}
}

/* ---------------------------------------------------------------------------
 * 3. O rejunte — régua própria, e a variável que decide é a LARGURA DA JUNTA
 *
 * Isto NÃO reaproveita as funções da cola, e a razão é de conteúdo antes de ser
 * de método: na cola a lista do fabricante nomeia a BASE sobre a qual se cola;
 * no rejunte, a mesma lista nomeia a TESSELA que será rejuntada e o ambiente.
 * Rejunte não toca a base. E a lista de ambientes críticos é maior aqui — três
 * em vez de dois, porque o rejunte é a superfície exposta: na pia e no
 * banheiro, quem falha primeiro é ele.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_mapa_rejunte' ) ) {
function cdm_f2_mapa_rejunte() {
	static $mapa = null;
	if ( null !== $mapa ) {
		return $mapa;
	}
	$banco = cdm_f2_banco();
	$fonte = isset( $banco['esquema']['mapa_de_termos_do_rejunte'] ) ? $banco['esquema']['mapa_de_termos_do_rejunte'] : array();
	$mapa  = array( 'ambiente' => array(), 'tessela' => array(), 'nao_traduz' => array() );

	foreach ( ( isset( $fonte['termos'] ) ? $fonte['termos'] : array() ) as $t ) {
		$mapa['ambiente'][ cdm_f2_normalizar( $t['literal'] ) ] = isset( $t['ambiente'] ) ? $t['ambiente'] : array();
	}
	foreach ( ( isset( $fonte['termos_tessela'] ) ? $fonte['termos_tessela'] : array() ) as $t ) {
		$mapa['tessela'][ cdm_f2_normalizar( $t['literal'] ) ] = isset( $t['tessela'] ) ? $t['tessela'] : array();
	}
	foreach ( ( isset( $fonte['termos_que_nao_traduzem'] ) ? $fonte['termos_que_nao_traduzem'] : array() ) as $t ) {
		$mapa['nao_traduz'][ cdm_f2_normalizar( $t['literal'] ) ] = true;
	}

	return $mapa;
}
}

if ( ! function_exists( 'cdm_f2_traduzir_rejunte' ) ) {
function cdm_f2_traduzir_rejunte( $lista ) {
	$mapa = cdm_f2_mapa_rejunte();
	$out  = array( 'ambiente' => array(), 'tessela' => array(), 'literais' => array() );

	foreach ( (array) $lista as $literal ) {
		$chave = cdm_f2_normalizar( $literal );
		if ( isset( $mapa['nao_traduz'][ $chave ] ) ) {
			continue;
		}
		if ( isset( $mapa['ambiente'][ $chave ] ) ) {
			foreach ( $mapa['ambiente'][ $chave ] as $a ) {
				$out['ambiente'][ $a ]   = true;
				$out['literais'][ $a ][] = $literal;
			}
		} elseif ( isset( $mapa['tessela'][ $chave ] ) ) {
			foreach ( $mapa['tessela'][ $chave ] as $t ) {
				$out['tessela'][ $t ]    = true;
				$out['literais'][ $t ][] = $literal;
			}
		}
	}

	return $out;
}
}

if ( ! function_exists( 'cdm_f2_prop' ) ) {
/** propriedades[campo].valor, aceitando ausência como null. */
function cdm_f2_prop( $m, $campo ) {
	return isset( $m['propriedades'][ $campo ]['valor'] ) ? $m['propriedades'][ $campo ]['valor'] : null;
}
}

if ( ! function_exists( 'cdm_f2_perfil_rejunte' ) ) {
function cdm_f2_perfil_rejunte( $m ) {
	static $cache = array();
	$id = isset( $m['id'] ) ? $m['id'] : '';
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$d = isset( $m['declaracoes'] ) ? $m['declaracoes'] : array();

	$ind    = cdm_f2_traduzir_rejunte( isset( $d['indicado_para'] ) ? $d['indicado_para'] : array() );
	$delim  = cdm_f2_traduzir_rejunte( isset( $d['ambientes_declarados'] ) ? $d['ambientes_declarados'] : array() );
	$resist = cdm_f2_traduzir_rejunte( isset( $d['resistencias_declaradas'] ) ? $d['resistencias_declaradas'] : array() );

	$literais = array();
	foreach ( array( $ind, $delim, $resist ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais[ $alvo ] = array_merge( isset( $literais[ $alvo ] ) ? $literais[ $alvo ] : array(), $ls );
		}
	}

	$cache[ $id ] = array(
		'junta_min'             => cdm_f2_prop( $m, 'junta_min_mm' ),
		'junta_max'             => cdm_f2_prop( $m, 'junta_max_mm' ),
		'ambientes_cobertos'    => $ind['ambiente'] + $delim['ambiente'] + $resist['ambiente'],
		'ambientes_delimitados' => $delim['ambiente'],
		'tesselas_declaradas'   => $ind['tessela'] + $resist['tessela'],
		'literais'              => $literais,
		'nivel'                 => cdm_f2_nivel( $m ),
	);

	return $cache[ $id ];
}
}

if ( ! function_exists( 'cdm_f2_criticos_rejunte' ) ) {
function cdm_f2_criticos_rejunte() {
	$banco = cdm_f2_banco();
	$r     = isset( $banco['esquema']['regras_de_elegibilidade_do_rejunte']['2_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes'] )
		? $banco['esquema']['regras_de_elegibilidade_do_rejunte']['2_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes']
		: array();

	return array_flip( (array) $r );
}
}

if ( ! function_exists( 'cdm_f2_avaliar_rejunte' ) ) {
/** Situação: recomendado | ressalva | fora_da_junta | fora_do_ambiente. */
function cdm_f2_avaliar_rejunte( $m, $junta_mm, $ambiente ) {
	$p = cdm_f2_perfil_rejunte( $m );

	/* 1 — a junta manda, e precisa das DUAS pontas. Faixa com uma ponta só não é
	   faixa aberta, é faixa desconhecida: o produto fica fora da grade inteira e
	   a tela diz que a faixa dele não foi obtida. É o caso do rejunte piscinas,
	   o único do banco que nomeia pastilha de vidro submersa. */
	if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	if ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	/* 3 — quem delimita ambiente fica fechado nele. */
	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'fora_do_ambiente', 0 );
	}
	/* 2 — ambiente crítico exige declaração explícita. */
	$criticos = cdm_f2_criticos_rejunte();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'fora_do_ambiente', 0 );
	}

	$score = 2 + ( isset( $p['ambientes_cobertos'][ $ambiente ] ) ? 2 : 0 );

	/* 4 — nível de fonte limita a recomendação primária. */
	if ( $p['nivel'] > cdm_f2_nivel_maximo() ) {
		return array( 'ressalva', $score );
	}

	return array( 'recomendado', $score );
}
}

if ( ! function_exists( 'cdm_f2_celula_rejunte' ) ) {
function cdm_f2_celula_rejunte( $junta_mm, $ambiente ) {
	$banco        = cdm_f2_banco();
	$recomendados = array();
	$ressalva     = array();
	$fora_junta   = array();
	$fora_amb     = array();

	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'rejunte' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			continue;
		}
		list( $situacao, $score ) = cdm_f2_avaliar_rejunte( $m, $junta_mm, $ambiente );
		if ( 'recomendado' === $situacao ) {
			$recomendados[ $id ] = $score;
		} elseif ( 'ressalva' === $situacao ) {
			$ressalva[] = $id;
		} elseif ( 'fora_da_junta' === $situacao ) {
			$fora_junta[] = $id;
		} else {
			$fora_amb[] = $id;
		}
	}

	$topo   = array();
	$abaixo = array();
	if ( $recomendados ) {
		$maior = max( $recomendados );
		foreach ( $recomendados as $id => $score ) {
			if ( $score === $maior ) {
				$topo[] = $id;
			} else {
				$abaixo[] = $id;
			}
		}
	}
	sort( $topo );
	sort( $abaixo );
	sort( $ressalva );
	sort( $fora_junta );
	sort( $fora_amb );

	return array(
		'recomendados_topo'           => $topo,
		'elegiveis_abaixo_do_topo'    => $abaixo,
		'mencionados_com_ressalva'    => $ressalva,
		'eliminados_por_faixa_de_junta' => $fora_junta,
		'eliminados_por_ambiente'     => $fora_amb,
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. A entrada, no vocabulário da pessoa
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_rotulos' ) ) {
/**
 * Os rótulos da tela. Palavras que a pessoa usa (VOZ.md): vaso, caquinho,
 * pastilha, cola, rejunte. "Substrato", "tessela" e "ficha" ficam de fora do
 * que ela lê — o vocabulário do fabricante aparece só na camada de prova.
 *
 * As CHAVES são o vocabulário controlado do esquema; se alguém acrescentar uma
 * base lá sem rótulo aqui, o teste reprova nas duas direções.
 */
function cdm_f2_rotulos() {
	return array(
		'base' => array(
			'ceramica_esmaltada_porcelana' => 'Cerâmica ou porcelana (vaso, azulejo, prato)',
			'vidro'                        => 'Vidro comum (garrafa, pote, vidro liso)',
			'vidro_laminado'               => 'Vidro laminado (o de para-brisa, com película no meio)',
			'espelho'                      => 'Espelho',
			'mdf_madeira'                  => 'MDF ou madeira',
			'cimento_concreto'             => 'Cimento ou concreto (vaso de cimento, tampo)',
			'alvenaria_tijolo'             => 'Alvenaria, tijolo ou pedra',
			'metal'                        => 'Metal (lata, bandeja, moldura de metal)',
			'plastico'                     => 'Plástico ou acrílico',
		),
		'base_curto' => array(
			'ceramica_esmaltada_porcelana' => 'cerâmica',
			'vidro'                        => 'vidro comum',
			'vidro_laminado'               => 'vidro laminado',
			'espelho'                      => 'espelho',
			'mdf_madeira'                  => 'MDF ou madeira',
			'cimento_concreto'             => 'cimento',
			'alvenaria_tijolo'             => 'alvenaria, tijolo ou pedra',
			'metal'                        => 'metal',
			'plastico'                     => 'plástico',
		),
		'ambiente' => array(
			'interno_seco'            => 'Dentro de casa, em lugar seco',
			'interno_molhado'         => 'Dentro de casa, em área molhada (banheiro, cozinha)',
			'externo_abrigado'        => 'Fora de casa, mas abrigado (varanda coberta)',
			'externo_exposto'         => 'Fora de casa, no sol e na chuva',
			'contato_permanente_agua' => 'Dentro da água o tempo todo (fonte, vaso com água)',
		),
		'ambiente_curto' => array(
			'interno_seco'            => 'dentro de casa, em lugar seco',
			'interno_molhado'         => 'na área molhada',
			'externo_abrigado'        => 'na varanda coberta',
			'externo_exposto'         => 'no sol e na chuva',
			'contato_permanente_agua' => 'dentro da água',
		),
		'tessela' => array(
			'pastilha_vidro'   => 'Pastilha de vidro',
			'pastilha_ceramica' => 'Pastilha de cerâmica',
			'caco_azulejo'     => 'Caquinho de azulejo',
			'caco_louca'       => 'Caquinho de louça ou prato',
			'caco_espelho'     => 'Caquinho de espelho',
			'pedra'            => 'Pedrinha ou pedra natural',
		),
	);
}
}

if ( ! function_exists( 'cdm_f2_entrada' ) ) {
/**
 * O que a pessoa escolheu, saneado contra o vocabulário — nunca contra uma
 * lista escrita aqui. Valor fora do vocabulário volta ao padrão em silêncio, e
 * o padrão é o caso mais comum do nicho: vaso de cerâmica, dentro de casa,
 * junta de 2 mm.
 */
function cdm_f2_entrada() {
	$rot  = cdm_f2_rotulos();
	$base = isset( $_GET['base'] ) ? sanitize_key( wp_unslash( $_GET['base'] ) ) : '';
	$amb  = isset( $_GET['onde'] ) ? sanitize_key( wp_unslash( $_GET['onde'] ) ) : '';
	$tes  = isset( $_GET['caco'] ) ? sanitize_key( wp_unslash( $_GET['caco'] ) ) : '';
	$jun  = isset( $_GET['junta'] ) ? (int) $_GET['junta'] : 0;

	$escolheu = ( isset( $rot['base'][ $base ] ) || isset( $rot['ambiente'][ $amb ] ) || $jun > 0 || isset( $rot['tessela'][ $tes ] ) );

	return array(
		'base'     => isset( $rot['base'][ $base ] ) ? $base : 'ceramica_esmaltada_porcelana',
		'ambiente' => isset( $rot['ambiente'][ $amb ] ) ? $amb : 'interno_seco',
		'tessela'  => isset( $rot['tessela'][ $tes ] ) ? $tes : 'pastilha_vidro',
		/* ATE 12 mm, e o teto NAO e enfeite: a grade conferida no esquema pisa em
		   11 mm de proposito — o primeiro valor depois do maior extremo que
		   algum fabricante declara (10 mm). Com o campo parando em 10, quem
		   tem folga de 11 caia calado no padrao de 2 mm e recebia uma resposta
		   que nao era a dele. Agora ele recebe a verdade: nenhum rejunte do
		   banco cobre essa folga. */
		'junta'    => ( $jun >= 1 && $jun <= 12 ) ? $jun : 2,
		'escolheu' => $escolheu,
	);
}
}

/* ---------------------------------------------------------------------------
 * 5. Peças de tela
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_nome' ) ) {
function cdm_f2_nome( $id ) {
	$banco = cdm_f2_banco();
	if ( ! isset( $banco['materiais'][ $id ] ) ) {
		return $id;
	}
	$m     = $banco['materiais'][ $id ];
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];

	/* A marca só entra quando o nome do produto ainda não a carrega. Sem esta
	   linha a tela dizia "Quartzolit Rejunte Cerâmicas Quartzolit": os cinco
	   rejuntes têm a marca dentro do nome comercial e as cinco colas não. */
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return trim( $nome );
	}

	return trim( $marca . ' ' . $nome );
}
}

if ( ! function_exists( 'cdm_f2_fonte_principal' ) ) {
/** A fonte de melhor nível do material, com a data em que foi lida. */
function cdm_f2_fonte_principal( $m ) {
	$melhor = null;
	foreach ( (array) ( isset( $m['fontes'] ) ? $m['fontes'] : array() ) as $f ) {
		if ( null === $melhor || (int) $f['nivel'] < (int) $melhor['nivel'] ) {
			$melhor = $f;
		}
	}

	return $melhor;
}
}

if ( ! function_exists( 'cdm_f2_lista_humana' ) ) {
/** "a, b e c" — como gente escreve, nunca "a, b, c". */
function cdm_f2_lista_humana( $itens ) {
	$itens = array_values( array_unique( array_filter( (array) $itens ) ) );
	$n     = count( $itens );
	if ( 0 === $n ) {
		return '';
	}
	if ( 1 === $n ) {
		return $itens[0];
	}
	$ultimo = array_pop( $itens );

	return implode( ', ', $itens ) . ' e ' . $ultimo;
}
}

if ( ! function_exists( 'cdm_f2_cartao_html' ) ) {
/**
 * O cartão do bloco de compra (seção 6 e 7 do contrato).
 *
 * Traz a declaração que fez o produto entrar — "cerâmica" e "azulejo" saídos da
 * lista do fabricante, não adjetivo de marketing —, o lugar do link de loja
 * (vazio hoje, e a página diz isso em vez de esconder) e, depois de tudo, o
 * link discreto de procedência. Produto sem foto NÃO some: aparece com espaço
 * reservado neutro, porque perder a recomendação certa por falta de imagem é
 * trocar o certo pelo bonito.
 */
function cdm_f2_cartao_html( $id, $motivo, $classe = '' ) {
	$banco = cdm_f2_banco();
	if ( ! isset( $banco['materiais'][ $id ] ) ) {
		return '';
	}
	$m     = $banco['materiais'][ $id ];
	$fonte = cdm_f2_fonte_principal( $m );

	$html  = '<li class="cdm-f2-cartao' . ( $classe ? ' ' . esc_attr( $classe ) : '' ) . '">';

	if ( ! empty( $m['imagem']['url'] ) ) {
		$html .= '<img class="cdm-f2-foto" src="' . esc_url( $m['imagem']['url'] ) . '"'
			. ' width="' . (int) $m['imagem']['largura'] . '" height="' . (int) $m['imagem']['altura'] . '"'
			. ' loading="lazy" alt="' . esc_attr( $m['imagem']['alt'] ) . '">';
	} else {
		$html .= '<span class="cdm-f2-sem-foto" aria-hidden="true"></span>';
	}

	$html .= '<span class="cdm-f2-marca">' . esc_html( isset( $m['marca'] ) ? $m['marca'] : '' ) . '</span>';
	$html .= '<h3>' . esc_html( $m['nome_comercial'] ) . '</h3>';
	if ( '' !== $motivo ) {
		$html .= '<p class="cdm-f2-motivo">' . $motivo . '</p>';
	}

	/* O BLOCO DE COMPRA VEM ANTES DA PROCEDÊNCIA, e nasce mesmo vazio. */
	$html .= '<span class="cdm-f2-compra">';
	if ( ! empty( $m['afiliado']['url'] ) ) {
		$html .= '<a class="cdm-f2-botao" href="' . esc_url( $m['afiliado']['url'] ) . '"'
			. ' rel="sponsored noopener" target="_blank">Ver na loja</a>';
	} else {
		$html .= '<span class="cdm-f2-sem-loja">Link de loja em breve</span>';
	}
	$html .= '</span>';

	if ( $fonte && ! empty( $fonte['url'] ) ) {
		$html .= '<span class="cdm-f2-fonte"><a href="' . esc_url( $fonte['url'] ) . '"'
			. ' rel="nofollow noopener" target="_blank">fonte</a>'
			. ' · lido em ' . esc_html( cdm_casca_data_br( $fonte['coletado_em'] ) ) . '</span>';
	}

	$html .= '</li>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_motivo_indicacao' ) ) {
/** "o fabricante escreve cerâmica e azulejo" — os literais que casaram. */
function cdm_f2_motivo_indicacao( $id, $base, $ambiente ) {
	$banco = cdm_f2_banco();
	$m     = $banco['materiais'][ $id ];
	$p     = cdm_f2_perfil_cola( $m );
	$termos = isset( $p['literais_indicacao'][ $base ] ) ? $p['literais_indicacao'][ $base ] : array();
	$amb    = isset( $p['literais_cobertura'][ $ambiente ] ) ? $p['literais_cobertura'][ $ambiente ] : array();

	$texto = '';
	if ( $termos ) {
		$texto = 'A ' . esc_html( $m['fabricante'] ) . ' escreve <em>'
			. esc_html( cdm_f2_lista_humana( $termos ) ) . '</em> entre as superfícies deste produto.';
	}
	if ( $amb ) {
		$texto .= ' Declara também <em>' . esc_html( cdm_f2_lista_humana( $amb ) ) . '</em>.';
	}

	return $texto;
}
}

if ( ! function_exists( 'cdm_f2_motivo_proibicao' ) ) {
function cdm_f2_motivo_proibicao( $id, $base, $ambiente ) {
	$banco  = cdm_f2_banco();
	$m      = $banco['materiais'][ $id ];
	$p      = cdm_f2_perfil_cola( $m );
	$termos = array();
	foreach ( array( $base, $ambiente ) as $alvo ) {
		if ( isset( $p['literais_proibicao'][ $alvo ] ) ) {
			$termos = array_merge( $termos, $p['literais_proibicao'][ $alvo ] );
		}
	}
	if ( ! $termos ) {
		return '';
	}

	return 'A ' . esc_html( $m['fabricante'] ) . ' escreve <em>' . esc_html( cdm_f2_lista_humana( $termos ) )
		. '</em> na lista do que este produto não deve tocar.';
}
}

/* ---------------------------------------------------------------------------
 * 6. A resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_resposta_cola_html' ) ) {
function cdm_f2_resposta_cola_html( $base, $ambiente ) {
	$rot    = cdm_f2_rotulos();
	$celula = cdm_f2_celula_cola( $base, $ambiente );
	$nb     = $rot['base_curto'][ $base ];
	$na     = $rot['ambiente_curto'][ $ambiente ];

	$html = '<div class="cdm-f2-resposta">';

	if ( $celula['recomendados_topo'] ) {
		$nomes = array();
		foreach ( $celula['recomendados_topo'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$quantos = count( $nomes );
		$html   .= '<p class="cdm-f2-frase">Para colar em <strong>' . esc_html( $nb ) . '</strong>, numa peça que vai ficar <strong>'
			. esc_html( $na ) . '</strong>, use <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong>'
			. ( $quantos > 1 ? ' — os ' . ( 2 === $quantos ? 'dois' : $quantos ) . ' servem aqui, e a gente não escolhe por você o que o fabricante não separou.' : '.' )
			. '</p>';
	} else {
		$html .= '<p class="cdm-f2-frase cdm-f2-faixa">Não temos cola para indicar em <strong>' . esc_html( $nb )
			. '</strong> ' . esc_html( $na ) . '. Nenhum dos adesivos do nosso banco é declarado pelo próprio fabricante para esse caso — e a gente prefere dizer isso a chutar o de sempre.</p>';
	}

	/* A camada de prova: a mesma resposta, agora com quem declarou, em qual
	   documento e em que dia foi lido (seção 15.2 — a prova desce um parágrafo,
	   dentro da mesma caixa, para quem citar a caixa levar a fonte junto). */
	$provas = array();
	foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
		$banco  = cdm_f2_banco();
		$m      = $banco['materiais'][ $id ];
		$p      = cdm_f2_perfil_cola( $m );
		$fonte  = cdm_f2_fonte_principal( $m );
		$termos = isset( $p['literais_indicacao'][ $base ] ) ? $p['literais_indicacao'][ $base ] : array();
		$provas[] = esc_html( cdm_f2_nome( $id ) ) . ': o fabricante declara <em>'
			. esc_html( cdm_f2_lista_humana( $termos ) ) . '</em> ('
			. esc_html( $fonte ? $fonte['tipo'] : 'fonte não registrada' ) . ', lido em '
			. esc_html( cdm_casca_data_br( $fonte ? $fonte['coletado_em'] : '' ) ) . ')';
	}
	if ( $provas ) {
		$html .= '<div class="cdm-prova"><p>' . implode( '. ', $provas ) . '.</p></div>';
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_vitrine_html' ) ) {
/**
 * O carrossel de compra. Ordem: (1) elegibilidade técnica completa; (2)
 * adequação; (3) ter link de loja SÓ como desempate entre equivalentes. Nunca
 * comparar comissão, nunca promover produto pior porque paga mais.
 */
function cdm_f2_vitrine_html( $base, $ambiente ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente );
	$banco  = cdm_f2_banco();

	$ordem = $celula['recomendados_topo'];
	/* Desempate permitido, e o único: entre equivalentes, quem tem link de loja
	   aparece antes. Estável: quem já estava na frente continua na frente quando
	   nenhum dos dois tem link (que é o estado de hoje, com os dez itens vazios). */
	usort( $ordem, function ( $a, $b ) use ( $banco ) {
		$la = empty( $banco['materiais'][ $a ]['afiliado']['url'] ) ? 1 : 0;
		$lb = empty( $banco['materiais'][ $b ]['afiliado']['url'] ) ? 1 : 0;
		if ( $la === $lb ) {
			return strcmp( $a, $b );
		}

		return $la - $lb;
	} );

	$html = '<div class="cdm-f2-secao">';
	$html .= '<h2>Onde comprar</h2>';

	if ( ! $ordem && ! $celula['elegiveis_abaixo_do_topo'] ) {
		$html .= '<p>Não há o que listar aqui: nesta combinação nenhum produto do nosso banco passa no que o fabricante declara. Listar assim mesmo seria o contrário do que esta página existe para fazer.</p>';
		$html .= '</div>';

		return $html;
	}

	$html .= '<ul class="cdm-f2-vitrine">';
	foreach ( $ordem as $id ) {
		$html .= cdm_f2_cartao_html( $id, cdm_f2_motivo_indicacao( $id, $base, $ambiente ) );
	}
	foreach ( $celula['elegiveis_abaixo_do_topo'] as $id ) {
		$html .= cdm_f2_cartao_html( $id, cdm_f2_motivo_indicacao( $id, $base, $ambiente ), 'cdm-f2-segundo' );
	}
	$html .= '</ul>';
	$html .= '<p class="cdm-f2-aviso">Alguns links desta página são de loja parceira e podem nos render comissão, sem mudar o seu preço — e sem mudar a ordem da lista, que sai do que o fabricante declara. Quem manda aqui é a ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'nossa regra de divulgação' ) . '.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_fora_html' ) ) {
/**
 * "O que não usar neste caso" — a seção que nenhuma outra página em português
 * tem, e a razão de a ferramenta existir.
 *
 * Dois grupos, com frases DIFERENTES, porque as duas coisas são diferentes:
 * proibido pelo fabricante não é a mesma coisa que não declarado por ele.
 * Misturar os dois seria inventar proibição — que é tão desonesto quanto
 * inventar indicação.
 */
function cdm_f2_fora_html( $base, $ambiente ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente );
	$rot    = cdm_f2_rotulos();
	$banco  = cdm_f2_banco();

	if ( ! $celula['eliminados_por_proibicao'] && ! $celula['eliminados_por_silencio'] && ! $celula['mencionados_com_ressalva'] ) {
		return '';
	}

	$html = '<div class="cdm-f2-secao cdm-f2-fora">';
	$html .= '<h2>O que não usar em ' . esc_html( $rot['base_curto'][ $base ] ) . ', e por quê</h2>';

	if ( $celula['eliminados_por_proibicao'] ) {
		$html .= '<ul class="cdm-f2-lista-fora">';
		foreach ( $celula['eliminados_por_proibicao'] as $id ) {
			$html .= '<li><strong>' . esc_html( cdm_f2_nome( $id ) ) . '</strong> — '
				. cdm_f2_motivo_proibicao( $id, $base, $ambiente ) . '</li>';
		}
		$html .= '</ul>';
	}

	if ( $celula['eliminados_por_silencio'] ) {
		$nomes = array();
		foreach ( $celula['eliminados_por_silencio'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$html .= '<p class="cdm-f2-silencio">Estes não estão proibidos, mas também não estão indicados: '
			. esc_html( cdm_f2_lista_humana( $nomes ) )
			. '. O fabricante simplesmente não fala desta superfície, e silêncio não vira "pode".</p>';

		/* A DECLARAÇÃO VAGA NÃO É SILÊNCIO, e merece ser dita com o nome dela.
		   "Certos tipos de plástico" não nomeia tipo nenhum: o produto não entra
		   nos recomendados, mas dizer só "o fabricante não fala" seria falso —
		   ele falou, e falou de um jeito que não dá para usar. É a diferença
		   entre não ter dado e ter dado que não decide. */
		$vagos = array();
		foreach ( $celula['eliminados_por_silencio'] as $id ) {
			$p = cdm_f2_perfil_cola( $banco['materiais'][ $id ] );
			if ( isset( $p['bases_vagas'][ $base ] ) && isset( $p['literais_indicacao'][ $base ] ) ) {
				$vagos[] = esc_html( cdm_f2_nome( $id ) ) . ' (o fabricante escreve <em>'
					. esc_html( cdm_f2_lista_humana( $p['literais_indicacao'][ $base ] ) ) . '</em>)';
			}
		}
		if ( $vagos ) {
			$html .= '<p class="cdm-f2-silencio">Um caso à parte: ' . implode( '; ', $vagos )
				. '. Isso não nomeia material nenhum, então não dá para virar recomendação — é declaração que existe e não decide.</p>';
		}
	}

	if ( $celula['mencionados_com_ressalva'] ) {
		$nomes = array();
		foreach ( $celula['mencionados_com_ressalva'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$html .= '<p class="cdm-f2-ressalva">Existe menção a ' . esc_html( cdm_f2_lista_humana( $nomes ) )
			. ', mas o que sustenta isso é material de imprensa do fabricante, não documento de produto — por isso ele aparece aqui embaixo e não na recomendação.</p>';
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_rejuntes_do_banco' ) ) {
/**
 * Os ids de TODO rejunte do banco, contados — nunca digitados.
 *
 * Existe para a prestação de contas da resposta e da tabela poderem fechar
 * contra o banco em vez de contra um número escrito à mão (seção 8 do
 * `ARQUIPELAGO.md`: número de tela nasce contado). Banco que cresce corrige
 * as duas telas sozinho.
 */
function cdm_f2_rejuntes_do_banco() {
	$banco = cdm_f2_banco();
	$ids   = array();
	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'rejunte' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			$ids[] = $id;
		}
	}
	sort( $ids );

	return $ids;
}
}

if ( ! function_exists( 'cdm_f2_rejunte_nomes' ) ) {
/** Lista de ids → lista de nomes comerciais, na ordem recebida. */
function cdm_f2_rejunte_nomes( $ids ) {
	$nomes = array();
	foreach ( (array) $ids as $id ) {
		$nomes[] = cdm_f2_nome( $id );
	}

	return $nomes;
}
}

if ( ! function_exists( 'cdm_f2_resposta_rejunte_html' ) ) {
/**
 * A resposta do rejunte — e a PRESTAÇÃO DE CONTAS dela.
 *
 * Consertado em 12/09/2026 (despacho da Sentinela de 12/09, item 2). O defeito:
 * a frase dizia "o rejunte é X", no singular e em definitivo, e o bloco de
 * compra logo abaixo servia QUATRO cartões — os três a mais eram os elegíveis
 * abaixo do topo, que entravam na vitrine sem que uma linha da página dissesse
 * o que eles são. Pior: `mencionados_com_ressalva` não era impresso em lugar
 * nenhum, então havia um quinto estado invisível. Somando, a página falava de
 * 2 a 4 dos 5 rejuntes do banco e o leitor não tinha como saber o que era o
 * resto.
 *
 * A regra que passa a valer, e ela é uma só: **todo rejunte do banco é nomeado
 * exatamente uma vez em cada resposta** — ou na frase de recomendação (e aí ele
 * está na vitrine), ou numa linha de prestação de contas que diz por que ele
 * não está. A vitrine serve EXATAMENTE o que a frase nomeia; não existe produto
 * no bloco de compra que o texto não sustente.
 *
 * Por que os elegíveis abaixo do topo continuam à venda, em vez de saírem: eles
 * passam nas duas travas que importam — cobrem a folga e não estão excluídos do
 * lugar. O que os separa do topo é o fabricante não NOMEAR o lugar, e a régua
 * do rejunte só transforma silêncio em exclusão nos ambientes críticos (regra 2
 * do esquema). Tirá-los da vitrine esconderia do leitor produto que serve;
 * mantê-los sem dizer o que são era a contradição. A saída é a frase dizer.
 */
function cdm_f2_resposta_rejunte_html( $junta, $ambiente, $tessela ) {
	$rot    = cdm_f2_rotulos();
	$celula = cdm_f2_celula_rejunte( $junta, $ambiente );
	$banco  = cdm_f2_banco();
	$na     = $rot['ambiente_curto'][ $ambiente ];

	$html  = '<div class="cdm-f2-secao">';
	$html .= '<h2>E o rejunte, que vai entre os caquinhos</h2>';

	if ( $celula['recomendados_topo'] ) {
		$nomes = cdm_f2_rejunte_nomes( $celula['recomendados_topo'] );
		$html .= '<p class="cdm-f2-frase">Com <strong>' . cdm_casca_num( $junta ) . ' mm</strong> de espaço entre uma pastilha e outra, '
			. esc_html( $na ) . ', o rejunte é <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong>'
			. ( count( $nomes ) > 1 ? ' — o fabricante nomeia este lugar nos ' . ( 2 === count( $nomes ) ? 'dois' : count( $nomes ) ) . '.' : '.' )
			. '</p>';

		/* OS SEGUNDOS SÃO NOMEADOS NA FRASE, e é por isso que eles podem ficar
		   na vitrine. Enquanto esta linha não existia, o bloco de compra servia
		   três produtos que o texto da página não sustentava. */
		if ( $celula['elegiveis_abaixo_do_topo'] ) {
			$segundos = cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] );
			$html    .= '<p class="cdm-f2-frase cdm-f2-segunda-linha">Também servem, e por isso estão na lista de compra: <strong>'
				. esc_html( cdm_f2_lista_humana( $segundos ) ) . '</strong>. '
				. ( 1 === count( $segundos ) ? 'Ele cobre' : 'Eles cobrem' ) . ' essa folga e o fabricante não proíbe este lugar — o que ele não faz é '
				. 'nomear o lugar por escrito, e é só isso que separa ' . ( 1 === count( $segundos ) ? 'esse' : 'esses' ) . ' do primeiro.</p>';
		}

		$html .= '<ul class="cdm-f2-vitrine">';
		foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
			$p      = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			$motivo = 'Cobre junta de ' . cdm_casca_num( $p['junta_min'] ) . ' a ' . cdm_casca_num( $p['junta_max'] ) . ' mm.';
			if ( isset( $p['literais'][ $ambiente ] ) ) {
				$motivo .= ' O fabricante declara <em>' . esc_html( cdm_f2_lista_humana( $p['literais'][ $ambiente ] ) ) . '</em>.';
			}
			if ( isset( $p['tesselas_declaradas'][ $tessela ] ) ) {
				$motivo .= ' E nomeia <em>' . esc_html( mb_strtolower( $rot['tessela'][ $tessela ], 'UTF-8' ) ) . '</em> por escrito.';
			}
			$html .= cdm_f2_cartao_html( $id, $motivo, in_array( $id, $celula['recomendados_topo'], true ) ? '' : 'cdm-f2-segundo' );
		}
		$html .= '</ul>';
	} else {
		/* A RECUSA NÃO OFERECE HIPÓTESE — as linhas de prestação de contas logo
		   abaixo nomeiam quem caiu por qual motivo, e é delas que o leitor tira
		   a causa. A versão anterior desta frase enumerava "ou a folga, ou o
		   lugar" tendo as duas listas na mão; a que a substituiu tentou escolher
		   entre três casos (só folga, só lugar, os dois) e o caso "só lugar"
		   nasceu INALCANÇÁVEL, porque o rejunte de faixa desconhecida vive no
		   balde da folga e nunca sai dele. Código que não pode rodar não é
		   cuidado, é um ramo que ninguém vai medir: quem diz a causa são as
		   linhas, uma por motivo. */
		$html .= '<p class="cdm-f2-frase cdm-f2-faixa">Não temos rejunte para indicar com <strong>' . cdm_casca_num( $junta )
			. ' mm</strong> de junta ' . esc_html( $na ) . '. Abaixo, um a um, o motivo de cada produto do nosso banco ter ficado de fora.</p>';
	}

	/* ------------------------------------------------------------------
	 * A PRESTAÇÃO DE CONTAS. Os grupos que NÃO estão na vitrine, cada um com
	 * nome próprio e motivo próprio. Somados aos nomeados na frase, fecham o
	 * banco inteiro — é essa soma que o portão cobra, em toda combinação de
	 * folga × lugar, na resposta e na tabela.
	 *
	 * SÃO QUATRO GRUPOS, e não três: a célula junta num balde só quem tem faixa
	 * publicada e não cobre a folga e quem NÃO TEM FAIXA NENHUMA — para decidir
	 * elegibilidade tanto faz, os dois estão fora. Para o texto não tanto faz:
	 * dizer "fora por causa da folga" de um produto cuja faixa a gente nunca
	 * conseguiu é afirmar sobre uma declaração que não foi lida. A F1 já fazia
	 * esse corte; aqui ele faltava, e era isso que tornava o ramo acima morto.
	 * ------------------------------------------------------------------ */
	$fora_folga = array();
	$sem_faixa  = array();
	foreach ( $celula['eliminados_por_faixa_de_junta'] as $id ) {
		$p = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
		if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
			$sem_faixa[] = $id;
		} else {
			$fora_folga[] = $id;
		}
	}
	if ( $fora_folga ) {
		$linhas = array();
		foreach ( $fora_folga as $id ) {
			$p        = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			$linhas[] = esc_html( cdm_f2_nome( $id ) ) . ' (o fabricante publica de ' . $p['junta_min'] . ' a ' . $p['junta_max'] . ' mm)';
		}
		$html .= '<p class="cdm-f2-silencio">Fora por causa da folga: ' . implode( '; ', $linhas ) . '.</p>';
	}
	if ( $celula['eliminados_por_ambiente'] ) {
		$html .= '<p class="cdm-f2-silencio">Fora porque o fabricante não declara este lugar: '
			. esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['eliminados_por_ambiente'] ) ) ) . '.</p>';
	}
	if ( $celula['mencionados_com_ressalva'] ) {
		/* O QUINTO ESTADO, que não era impresso em lugar nenhum até 12/09/2026.
		   Enquanto o banco tivesse só fonte de nível bom ele ficava vazio, e um
		   grupo vazio não denuncia que a tela não sabe imprimi-lo: no dia em que
		   um rejunte entrasse por fonte fraca, ele sumiria da página inteira —
		   nem na vitrine, nem na prestação de contas. */
		$html .= '<p class="cdm-f2-ressalva">Existe menção a '
			. esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['mencionados_com_ressalva'] ) ) )
			. ', mas o que sustenta isso é material de imprensa do fabricante, não documento de produto — por isso ele não entra na indicação nem na lista de compra.</p>';
	}

	if ( $sem_faixa ) {
		$html .= '<p class="cdm-f2-silencio">De ' . esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $sem_faixa ) ) )
			. ' a gente não conseguiu a faixa de junta que o fabricante publica, então '
			. ( 1 === count( $sem_faixa ) ? 'ele não entra' : 'eles não entram' ) . ' em recomendação nenhuma — '
			. 'nem para dizer que cabe, nem para dizer que não cabe.</p>';
	}
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_espera_html' ) ) {
/**
 * O tempo de espera — o número que a SERP nunca dá, e que é a diferença entre a
 * peça pronta e a peça que solta o caquinho no dia seguinte.
 */
function cdm_f2_espera_html( $base, $ambiente ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente );
	$banco  = cdm_f2_banco();
	$linhas = array();

	foreach ( $celula['recomendados_topo'] as $id ) {
		$m    = $banco['materiais'][ $id ];
		$cura = isset( $m['propriedades']['cura_apos_24h'] ) ? $m['propriedades']['cura_apos_24h'] : null;
		$seca = isset( $m['propriedades']['tempo_de_secagem'] ) ? $m['propriedades']['tempo_de_secagem'] : null;
		if ( $cura ) {
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', a peça descansa <strong>24 horas</strong> antes do rejunte — é o que o fabricante declara para '
				. cdm_casca_num( $cura['valor'] ) . ' mm de cura.';
		} elseif ( $seca && null !== $seca['valor'] ) {
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', o fabricante declara secagem em <strong>'
				. esc_html( is_array( $seca['valor'] ) ? implode( ' a ', $seca['valor'] ) : $seca['valor'] ) . ' ' . esc_html( $seca['unidade'] ) . '</strong>.';
		} elseif ( $seca ) {
			/* O CAMPO EXISTE E ESTA VAZIO COM MOTIVO ESCRITO — e a pagina diz isso,
			   em vez de simplesmente não ter a seção. Sumir com a linha faria a
			   ferramenta parecer que o tempo de espera não importa para este
			   produto; o que acontece é que a gente não colheu. Silêncio parece
			   defeito, texto honesto não (seção 7 do contrato). */
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', a gente ainda não publica o tempo de espera: '
				. 'não achamos essa declaração nas fontes do fabricante que lemos.';
		}
	}

	if ( ! $linhas ) {
		return '';
	}

	return '<div class="cdm-f2-secao"><h2>Quanto esperar antes de rejuntar</h2><p>' . implode( ' ', $linhas ) . '</p></div>';
}
}

/* ---------------------------------------------------------------------------
 * 7. As tabelas pré-renderizadas — o que um modelo de linguagem lê
 *
 * São as células escritas À MÃO no esquema e reconferidas pelo validador, não
 * uma amostra bonita: 18 combinações de base × ambiente e 9 de junta ×
 * ambiente, com a frase de justificativa em cada linha. É esta parte que
 * sobrevive a ser citada fora de contexto, e é ela que existe quando ninguém
 * preenche o formulário.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_tabela_cola_html' ) ) {
function cdm_f2_tabela_cola_html() {
	$banco  = cdm_f2_banco();
	$rot    = cdm_f2_rotulos();
	$grade  = isset( $banco['esquema']['matriz_esperada_da_F2']['celulas'] ) ? $banco['esquema']['matriz_esperada_da_F2']['celulas'] : array();

	if ( ! $grade ) {
		return '';
	}

	$html  = '<div class="cdm-f2-secao"><h2>A tabela inteira, sem preencher nada</h2>';
	$html .= '<p>Cada linha é uma combinação que a gente já conferiu: a base, o lugar onde a peça vai ficar, a cola que serve e a que não serve.</p>';
	$html .= '<div class="cdm-f2-rolagem"><table class="cdm-f2-tabela"><thead><tr>'
		. '<th scope="col">Sobre o que você vai colar</th><th scope="col">Onde a peça vai ficar</th>'
		. '<th scope="col">Use</th><th scope="col">Não use, e por quê</th></tr></thead><tbody>';

	foreach ( $grade as $c ) {
		if ( ! isset( $rot['base_curto'][ $c['base'] ] ) || ! isset( $rot['ambiente_curto'][ $c['ambiente'] ] ) ) {
			continue;
		}
		/* A célula sai RECOMPUTADA das declarações, nunca lida do campo escrito à
		   mão que está ao lado dela no esquema. Se o banco e a matriz se
		   separarem, quem acusa é o validador — a tela nunca finge concordância
		   copiando o esperado. */
		$celula = cdm_f2_celula_cola( $c['base'], $c['ambiente'] );

		$usa = array();
		foreach ( $celula['recomendados_topo'] as $id ) {
			$usa[] = cdm_f2_nome( $id );
		}
		$nao = array();
		foreach ( $celula['eliminados_por_proibicao'] as $id ) {
			$m      = $banco['materiais'][ $id ];
			$p      = cdm_f2_perfil_cola( $m );
			$termos = array();
			foreach ( array( $c['base'], $c['ambiente'] ) as $alvo ) {
				if ( isset( $p['literais_proibicao'][ $alvo ] ) ) {
					$termos = array_merge( $termos, $p['literais_proibicao'][ $alvo ] );
				}
			}
			$nao[] = cdm_f2_nome( $id ) . ' — a ' . $m['fabricante'] . ' escreve ' . cdm_f2_lista_humana( $termos );
		}

		$html .= '<tr>';
		$html .= '<td>' . esc_html( $rot['base_curto'][ $c['base'] ] ) . '</td>';
		$html .= '<td>' . esc_html( $rot['ambiente_curto'][ $c['ambiente'] ] ) . '</td>';
		$html .= '<td>' . ( $usa ? esc_html( cdm_f2_lista_humana( $usa ) ) : '<span class="cdm-f2-vazio">a gente não indica nenhuma</span>' ) . '</td>';
		$html .= '<td>' . ( $nao ? esc_html( cdm_f2_lista_humana( $nao ) ) : '—' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_tabela_rejunte_html' ) ) {
function cdm_f2_tabela_rejunte_html() {
	$banco = cdm_f2_banco();
	$rot   = cdm_f2_rotulos();
	$grade = isset( $banco['esquema']['matriz_esperada_do_rejunte']['celulas'] ) ? $banco['esquema']['matriz_esperada_do_rejunte']['celulas'] : array();

	if ( ! $grade ) {
		return '';
	}

	$html  = '<div class="cdm-f2-secao"><h2>O mesmo, para o rejunte</h2>';
	$html .= '<p>Aqui quem manda é a folga que você deixa entre uma pastilha e outra. A faixa de cada produto é a que o fabricante publica.</p>';
	$html .= '<div class="cdm-f2-rolagem"><table class="cdm-f2-tabela"><thead><tr>'
		. '<th scope="col">Folga entre as pastilhas</th><th scope="col">Onde a peça vai ficar</th>'
		. '<th scope="col">Rejunte que serve</th><th scope="col">Fora, e por quê</th></tr></thead><tbody>';

	foreach ( $grade as $c ) {
		if ( ! isset( $rot['ambiente_curto'][ $c['ambiente'] ] ) ) {
			continue;
		}
		$celula = cdm_f2_celula_rejunte( (int) $c['junta_mm'], $c['ambiente'] );

		/* A MESMA PRESTAÇÃO DE CONTAS DA RESPOSTA, na tabela — e pelo mesmo
		   motivo, que aqui é mais caro ainda: esta é a metade que um modelo de
		   linguagem lê sem preencher formulário nenhum. Até 12/09/2026 a coluna
		   "serve" trazia só o topo e a coluna "fora" só dois dos três grupos, e
		   três das nove linhas não somavam os 5 rejuntes do banco. */
		$usa = array();
		if ( $celula['recomendados_topo'] ) {
			$usa[] = cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['recomendados_topo'] ) )
				. ' (o fabricante nomeia este lugar)';
		}
		if ( $celula['elegiveis_abaixo_do_topo'] ) {
			$usa[] = cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] ) )
				. ( 1 === count( $celula['elegiveis_abaixo_do_topo'] ) ? ' (cobre' : ' (cobrem' )
				. ' a folga, e o fabricante não fala deste lugar)';
		}

		$t_folga = array();
		$t_sem   = array();
		foreach ( $celula['eliminados_por_faixa_de_junta'] as $id ) {
			$p = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
				$t_sem[] = $id;
			} else {
				$t_folga[] = $id;
			}
		}
		$fora = array();
		if ( $t_folga ) {
			$fora[] = count( $t_folga ) . ' por causa da folga';
		}
		if ( $celula['eliminados_por_ambiente'] ) {
			$fora[] = count( $celula['eliminados_por_ambiente'] ) . ' porque o fabricante não declara este lugar';
		}
		if ( $celula['mencionados_com_ressalva'] ) {
			$fora[] = count( $celula['mencionados_com_ressalva'] ) . ' porque a fonte é material de imprensa';
		}
		if ( $t_sem ) {
			$fora[] = count( $t_sem ) . ' porque a faixa de folga dele não foi obtida';
		}

		$html .= '<tr>';
		$html .= '<td>' . cdm_casca_num( $c['junta_mm'] ) . ' mm</td>';
		$html .= '<td>' . esc_html( $rot['ambiente_curto'][ $c['ambiente'] ] ) . '</td>';
		$html .= '<td>' . ( $usa ? esc_html( implode( '; ', $usa ) ) : '<span class="cdm-f2-vazio">a gente não indica nenhum</span>' ) . '</td>';
		$html .= '<td>' . ( $fora ? esc_html( cdm_f2_lista_humana( $fora ) ) : '—' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. O formulário
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_select_html' ) ) {
function cdm_f2_select_html( $nome, $rotulo, $opcoes, $escolhido, $ajuda = '' ) {
	$id    = 'cdm-f2-' . $nome;
	$html  = '<p class="cdm-f2-campo"><label for="' . esc_attr( $id ) . '">' . esc_html( $rotulo ) . '</label>';
	if ( '' !== $ajuda ) {
		$html .= '<span class="cdm-f2-ajuda">' . esc_html( $ajuda ) . '</span>';
	}
	$html .= '<select id="' . esc_attr( $id ) . '" name="' . esc_attr( $nome ) . '">';
	foreach ( $opcoes as $valor => $texto ) {
		$html .= '<option value="' . esc_attr( $valor ) . '"' . ( (string) $valor === (string) $escolhido ? ' selected' : '' )
			. '>' . esc_html( $texto ) . '</option>';
	}
	$html .= '</select></p>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_form_html' ) ) {
function cdm_f2_form_html( $entrada ) {
	$rot = cdm_f2_rotulos();

	$juntas = array();
	for ( $i = 1; $i <= 12; $i++ ) {
		$juntas[ $i ] = $i . ' mm' . ( 2 === $i ? ' (o mais comum)' : '' );
	}

	/* GET para a própria página, e sem $_SERVER literal: o playbook (fase 4b)
	   manda usar add_query_arg( array() ), porque o ModSecurity desta hospedagem
	   mata a gravação em silêncio quando o snippet toca $_SERVER. */
	$html  = '<form class="cdm-f2-form" method="get" action="' . esc_url( add_query_arg( array() ) ) . '#resposta">';
	$html .= cdm_f2_select_html( 'base', 'Sobre o que você vai colar?', $rot['base'], $entrada['base'] );
	$html .= cdm_f2_select_html( 'onde', 'Onde a peça vai ficar?', $rot['ambiente'], $entrada['ambiente'] );
	$html .= cdm_f2_select_html( 'caco', 'O que você vai colar em cima?', $rot['tessela'], $entrada['tessela'],
		'Isto não muda a cola — quem manda na cola é a base. Serve para a gente avisar quando o fabricante do rejunte cita o seu caquinho por escrito.' );
	$html .= cdm_f2_select_html( 'junta', 'Quanto espaço entre uma pastilha e outra?', $juntas, $entrada['junta'],
		'Entre 2 e 3 mm é o comum, mas quem decide é a sua peça.' );
	$html .= '<p class="cdm-f2-acao"><button type="submit" class="cdm-f2-botao">Ver o que usar</button></p>';
	$html .= '</form>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 9. A página
 * ------------------------------------------------------------------------- */

add_shortcode( 'cdm_f2', function () {
	$banco = cdm_f2_banco();

	if ( empty( $banco['completo'] ) ) {
		/* Sem banco a página NÃO inventa: diz que a medição não chegou. Uma
		   ferramenta que responde com o banco vazio é pior que uma fora do ar. */
		return '<div class="cdm-bloco"><p class="cdm-linha-mestra">Esta ferramenta está sem os dados de fabricante neste momento.</p>'
			. '<p>Ela não responde de cabeça: cada recomendação sai do que o fabricante publica sobre o próprio produto. Volte em alguns minutos.</p></div>';
	}

	$e   = cdm_f2_entrada();
	$rot = cdm_f2_rotulos();
	$n   = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco cdm-f2">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Diga sobre o que você vai colar e onde a peça vai ficar. A gente mostra a cola, o rejunte, quanto esperar — e o que <em>não</em> usar no seu caso.</p>';
	$html .= '<p>A resposta muda mais do que parece: a mesma peça feita para a sala e para o jardim leva material diferente, e a cola que a maioria dos tutoriais manda usar é justamente a que o fabricante proíbe em espelho, em cimento e em vidro laminado.</p>';
	$html .= '<p>Esta página faz parte do nosso guia de ' . cdm_casca_link_html( 'materiais', 'Materiais' ) . '.</p>';
	$html .= '</div>';

	$html .= cdm_f2_form_html( $e );

	$html .= '<div class="cdm-f2-saida" id="resposta">';
	$html .= cdm_f2_resposta_cola_html( $e['base'], $e['ambiente'] );
	$html .= cdm_f2_vitrine_html( $e['base'], $e['ambiente'] );
	$html .= cdm_f2_espera_html( $e['base'], $e['ambiente'] );
	$html .= cdm_f2_resposta_rejunte_html( $e['junta'], $e['ambiente'], $e['tessela'] );
	$html .= cdm_f2_fora_html( $e['base'], $e['ambiente'] );
	$html .= '</div>';

	$html .= cdm_f2_tabela_cola_html();
	$html .= cdm_f2_tabela_rejunte_html();

	/* AS DUAS FAIXAS DESCOBERTAS, declaradas em vez de preenchidas no chute. */
	$html .= '<div class="cdm-f2-secao">';
	$html .= '<h2>Duas coisas que a gente ainda não responde</h2>';
	$html .= '<p class="cdm-f2-faixa">Não indicamos cola para <strong>peça de plástico</strong>. Nenhum fabricante do nosso banco declara colagem sobre plástico: o que existe é um "certos tipos de plástico" que não nomeia tipo nenhum, e isso não dá para transformar em recomendação.</p>';
	$html .= '<p class="cdm-f2-faixa">Não indicamos cola para <strong>peça que fica dentro da água o tempo todo</strong> — fonte, bebedouro, vaso com água parada. O rejunte dessa peça a gente tem: o rejunte epóxi Quartzolit é liberado para contato com água em 7 dias, com junta de 1 a 5 mm. A cola, não — a única menção de colagem submersa que achamos veio de material de imprensa, e material de imprensa não sustenta recomendação.</p>';
	$html .= '<p>Ter metade da resposta não é ter a resposta, e a peça precisa das duas.</p>';
	$html .= '</div>';

	/* PERGUNTAS QUE AS PESSOAS REALMENTE FAZEM — as mesmas do FAQPage abaixo. O
	   texto na tela e o do schema saem da MESMA função, senão os dois envelhecem
	   separados e o schema passa a prometer o que a página não diz. */
	$html .= '<div class="cdm-f2-secao"><h2>Perguntas que sempre chegam</h2><dl class="cdm-f2-faq">';
	foreach ( cdm_f2_perguntas() as $p ) {
		$html .= '<dt>' . esc_html( $p['pergunta'] ) . '</dt><dd>' . esc_html( $p['resposta'] ) . '</dd>';
	}
	$html .= '</dl></div>';

	/* A CAMADA DE PROVA da página (15.2): quem declarou, em qual documento, em
	   que dia a gente leu, e o que ainda não foi lido direto. */
	$html .= '<div class="cdm-prova">';
	$html .= '<h2>Como sabemos</h2>';
	$html .= '<p>As ' . cdm_casca_num( $n['materiais_cola'] ) . ' colas e os ' . cdm_casca_num( $n['materiais_rejunte'] )
		. ' rejuntes desta página vêm do que cada fabricante publica sobre o próprio produto, com o documento e a data em que foi lido. A recomendação é <em>recalculada</em> das declarações a cada carregamento, nunca digitada — são '
		. cdm_casca_num( $n['celulas_matriz'] ) . ' combinações de base e ambiente e ' . cdm_casca_num( $n['celulas_rejunte'] )
		. ' de folga e ambiente conferidas uma a uma.</p>';
	$html .= '<p>A mais importante delas é a ficha técnica BRSA004 do Silicone Acético Construção Tekbond, revisada em 10/2025, que lista espelho, concreto, cimento, tijolo, calcário, superfície alcalina, pintada ou porosa, acrílico, aquário, metal corrosível e imersão contínua entre as superfícies em que o produto não deve ser usado. Nenhum PDF de fabricante foi aberto linha a linha: a leitura foi feita no domínio de cada um, em 10 e 11/09/2026, e isso está declarado item a item no nosso banco.</p>';
	$html .= '<p>Hoje ' . cdm_casca_num( $n['esperando_link'] ) . ' dos ' . cdm_casca_num( $n['itens_no_banco'] )
		. ' itens do banco ainda esperam link de loja. O método inteiro está em ' . cdm_casca_link_html( 'materiais/como-sabemos', 'Como sabemos' ) . '.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'cdm_f2_perguntas' ) ) {
/**
 * Uma fonte só para a tela e para o FAQPage. Toda resposta aqui é sustentada
 * por declaração que já está no banco — nenhuma pergunta existe só para encher
 * schema, que é o que faz FAQPage virar spam.
 */
function cdm_f2_perguntas() {
	return array(
		array(
			'pergunta' => 'Posso usar silicone acético para colar caquinho de espelho?',
			'resposta' => 'Não. A Tekbond escreve espelhos na lista do que o Silicone Acético Construção não deve tocar. O Silicone Neutro, do mesmo fabricante, é declarado para espelho — não precisa trocar de marca, precisa pegar o tubo certo na prateleira.',
		),
		array(
			'pergunta' => 'E no vaso de cimento, serve silicone acético?',
			'resposta' => 'Não. Concreto, cimento e superfícies alcalinas estão na lista do que a Tekbond diz para não usar com o acético. Quem responde ao vaso de cimento é o silicone neutro, que declara concreto e alvenaria.',
		),
		array(
			'pergunta' => 'Cola branca serve para mosaico?',
			'resposta' => 'Serve em MDF e madeira, dentro de casa e em lugar seco: a Cascola declara MDF, compensado e madeira para o Cascorez Extra, e delimita o uso a ambientes internos. Em área molhada ou fora de casa ela não declara nada, e a gente não transforma silêncio em indicação.',
		),
		array(
			'pergunta' => 'Quanto tempo esperar antes de rejuntar?',
			'resposta' => 'Com silicone acético, 24 horas: é o tempo em que o fabricante declara 3 mm de cura, a 23 graus e 55% de umidade. Rejuntar antes disso é mexer na peça enquanto a cola ainda está trabalhando.',
		),
		array(
			'pergunta' => 'Qual rejunte para peça que fica no sol e na chuva?',
			'resposta' => 'A gente não tem resposta para esse caso, e prefere dizer isso: nenhum dos cinco rejuntes do nosso banco declara resistência a sol e chuva pelo nome. Peça de jardim, número de casa e mandala de parede externa ficam nessa faixa descoberta.',
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 10. Cabeça da página: description, canonical, robôs e JSON-LD
 *
 * O canonical e o `noindex` do estado com parâmetro andam juntos e existem pela
 * mesma razão: a resposta é servida pelo servidor, então cada combinação é uma
 * URL de verdade — e quem entra no índice tem que ser UMA página, a âncora, com
 * a tabela inteira (seções 14.1 e 14.4 do contrato).
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_e_minha_pagina' ) ) {
function cdm_f2_e_minha_pagina() {
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_F2_SLUG === cdm_casca_slug_atual();
}
}

add_action( 'wp_head', function () {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return;
	}
	$e = cdm_f2_entrada();

	echo '<meta name="description" content="'
		. esc_attr( 'Qual cola usar no mosaico, pela declaração do próprio fabricante: cerâmica, vidro, espelho, MDF, cimento ou metal, dentro de casa ou no sol e na chuva. Com o rejunte e o que não usar.' )
		. '">' . "\n";
	/* O CANONICAL NAO SAI DAQUI, e a ausencia e deliberada: `rel_canonical()` do
	   nucleo ja imprime o permalink limpo em toda pagina singular, e esta ilha
	   nao tem plugin de SEO que o remova. Imprimir o nosso serviria DOIS
	   canonicals identicos — inofensivo para o Google e sujo numa pagina cujo
	   proposito inteiro e ter UM endereco no indice. O que falta ao nucleo e o
	   `noindex` do estado com parametro, e e so isso que sai daqui. */
	if ( $e['escolheu'] ) {
		echo '<meta name="robots" content="noindex, follow">' . "\n";
	}
}, 4 );

add_action( 'wp_head', function () {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return;
	}
	$limpa = home_url( '/' . CDM_F2_SLUG . '/' );

	$perguntas = array();
	foreach ( cdm_f2_perguntas() as $p ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $p['pergunta'],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p['resposta'] ),
		);
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type'                => 'WebApplication',
				'@id'                  => $limpa . '#ferramenta',
				'name'                 => CDM_F2_TITULO,
				'url'                  => $limpa,
				'applicationCategory'  => 'UtilitiesApplication',
				'operatingSystem'      => 'Web',
				'inLanguage'           => 'pt-BR',
				'isAccessibleForFree'  => true,
				'description'          => 'Seletor de cola e rejunte para mosaico artesanal: a recomendação é recalculada das declarações publicadas pelos fabricantes, com a superfície, o ambiente e a largura da junta.',
				'publisher'            => array( '@id' => home_url( '/#organizacao' ) ),
			),
			array(
				'@type'      => 'FAQPage',
				'@id'        => $limpa . '#perguntas',
				'mainEntity' => $perguntas,
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-f2-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 11. Folha e script — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML, matando o script inteiro. Foi
 * o defeito que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 *
 * O script daqui NÃO calcula nada: ele só evita o recarregamento quando a
 * pessoa troca uma opção, e some por inteiro sem JavaScript. A conta é do
 * servidor, e é por isso que esta página existe para um modelo de linguagem.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-f2-css">
.cdm-f2-form{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);}
.cdm-f2-campo{margin:0 0 1rem;display:flex;flex-direction:column;gap:.3rem;}
.cdm-f2-campo:last-of-type{margin-bottom:0;}
.cdm-f2-campo label{font-family:var(--cdm-display);font-weight:600;font-size:1rem;}
.cdm-f2-ajuda{color:var(--cdm-legenda);font-size:.88rem;line-height:1.45;}
.cdm-f2-form select{font-family:var(--cdm-texto);font-size:1rem;padding:.6rem .7rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);color:var(--cdm-tinta);max-width:100%;}
.cdm-f2-acao{margin:1.2rem 0 0;}
.cdm-f2-botao{display:inline-block;background:var(--cdm-coral);color:#FFFFFF;border:0;border-radius:2px;padding:.7rem 1.2rem;font-family:var(--cdm-display);font-weight:600;font-size:1rem;cursor:pointer;text-decoration:none;}
.cdm-f2-botao:hover{background:var(--cdm-vinho);color:#FFFFFF;text-decoration:none;}
.cdm-f2-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-f2-frase{font-size:1.15rem;line-height:1.5;margin:0;}
/* A segunda linha da recomendacao — os que servem sem o fabricante nomear o
   lugar. Ela e frase, nao nota de rodape, entao fica no corpo do texto; o
   degrau de tamanho e o que diz ao olho que o primeiro e o primeiro. */
.cdm-f2-frase.cdm-f2-segunda-linha{font-size:1rem;margin:.7rem 0 0;color:var(--cdm-tinta);}
.cdm-f2-resposta .cdm-prova{margin-top:1rem;}
.cdm-f2-secao{margin:2rem 0;}
.cdm-f2-secao h2{font-size:1.25rem;margin:0 0 .6rem;}
.cdm-f2-vitrine{display:flex;gap:1rem;list-style:none;margin:1rem 0 0;padding:0 0 .6rem;overflow-x:auto;scroll-snap-type:x mandatory;}
.cdm-f2-cartao{scroll-snap-align:start;flex:0 0 15rem;border:1px solid var(--cdm-traco);border-radius:2px;padding:.9rem;display:flex;flex-direction:column;gap:.45rem;}
.cdm-f2-cartao.cdm-f2-segundo{opacity:.85;}
.cdm-f2-foto,.cdm-f2-sem-foto{display:block;width:100%;height:7rem;object-fit:contain;background:#F6F1EE;border-radius:2px;}
.cdm-f2-marca{font-family:var(--cdm-mono);font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--cdm-legenda);}
.cdm-f2-cartao h3{font-size:1rem;margin:0;}
.cdm-f2-motivo{font-size:.9rem;line-height:1.45;margin:0;color:var(--cdm-tinta);}
.cdm-f2-compra{margin-top:auto;}
.cdm-f2-sem-loja{display:inline-block;font-size:.85rem;color:var(--cdm-legenda);border:1px dashed var(--cdm-traco);border-radius:2px;padding:.45rem .7rem;}
.cdm-f2-fonte{font-size:.8rem;color:var(--cdm-legenda);}
.cdm-f2-aviso{font-size:.88rem;color:var(--cdm-legenda);margin:.8rem 0 0;}
.cdm-f2-lista-fora{margin:.6rem 0 0;padding-left:1.1rem;}
.cdm-f2-lista-fora li{margin:0 0 .5rem;}
.cdm-f2-silencio,.cdm-f2-ressalva{font-size:.95rem;color:var(--cdm-legenda);margin:.7rem 0 0;}
.cdm-f2-rolagem{overflow-x:auto;}
.cdm-f2-tabela{width:100%;font-size:.93rem;}
.cdm-f2-vazio{color:var(--cdm-ambar);}
.cdm-f2-faq{margin:.8rem 0 0;}
.cdm-f2-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .25rem;}
.cdm-f2-faq dd{margin:0;}
@media (max-width:600px){
.cdm-f2-cartao{flex:0 0 78%;}
.cdm-f2-frase{font-size:1.05rem;}
}
</style>
<script id="cdm-f2-js">
/* Troca de opcao ja envia o formulario, para a pessoa nao precisar do botao.
   Nada aqui decide nada: quem responde e o servidor, e sem JavaScript a pagina
   continua inteira — o botao esta la, visivel, e faz o mesmo. */
(function(){
	var f = document.querySelector('.cdm-f2-form');
	if (!f) { return; }
	var selects = f.querySelectorAll('select');
	for (var i = 0; i < selects.length; i++) {
		selects[i].addEventListener('change', function(){ f.submit(); });
	}
	/* Chegou com resposta na tela: leva a pessoa ate ela. */
	if (window.location.search.indexOf('base=') !== -1) {
		var alvo = document.getElementById('resposta');
		if (alvo && !window.location.hash) { alvo.scrollIntoView({behavior:'smooth', block:'start'}); }
	}
})();
</script>
HTML;
}, 20 );

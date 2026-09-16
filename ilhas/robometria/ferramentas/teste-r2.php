<?php
/**
 * Verificacao MEDIDA da ferramenta R2, sem site e sem rede.
 *
 *   php ferramentas/teste-r2.php .
 *
 * E a secao 8 do ARQUIPELAGO.md executada onde da para executa-la nesta ilha: a
 * nuvem so alcanca robometria.com.br para o Sync e o /status, entao a
 * alternativa a este arquivo seria marcar publicar=true por fe.
 *
 * O QUE ELE MEDE QUE O teste-r1.php NAO MEDE, e e a razao de a prova ter forma
 * diferente aqui: a entrada da R1 e uma lista fechada, e o gabarito dela e a
 * resposta de cada modelo. A entrada da R2 tem uma metragem CONTINUA de 10 a
 * 400 m2, e por isso o snippet faz aritmetica — o ceil dos ciclos e a soma dos
 * minutos. Entao o gabarito e uma GRADE, e este arquivo a percorre INTEIRA:
 *
 *   - as 9 situacoes de piso x pelo, frase a frase;
 *   - os cartoes de cada situacao em tres metragens;
 *   - a metragem varrida de 10 em 10 m2 contra CADA modelo de referencia,
 *     comparando ciclos, tempo de limpeza, tempo total e a frase.
 *
 * Grade nao e amostra. Se o ceil do PHP divergir do da referencia numa borda —
 * exatamente onde esse tipo de erro mora —, este arquivo reprova.
 *
 * O que ele NAO substitui: a conferencia da revisao aplicada no /status depois
 * do Sync (secao 4). Este arquivo prova que o codigo esta certo; so o /status
 * prova que ele esta NO AR.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function rbm_ok( $condicao, $rotulo, $medida = '' ) {
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

/** So os blocos <script>, que e onde a contagem de &#038; vale (secao 8). */
function rbm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/**
 * Normaliza para comparar a frase publicada com a da referencia.
 *
 * O banco desta ilha e ASCII e a tela sai acentuada, entao a comparacao ignora
 * acento — de proposito, porque o que esta sendo provado e que os dois lados
 * usam o MESMO MOLDE, nao que digitam os mesmos bytes. O "m2" da referencia
 * contra o "m2" com expoente da tela entra na mesma conta: e a mesma unidade
 * escrita para leitor humano de um lado e para arquivo de dados do outro.
 */
function rbm_normalizar( $t ) {
	$de   = array( 'á','à','â','ã','ä','é','ê','ë','í','î','ï','ó','ô','õ','ö','ú','û','ü','ç',
	               'Á','À','Â','Ã','É','Ê','Í','Ó','Ô','Õ','Ú','Ç','²' );
	$para = array( 'a','a','a','a','a','e','e','e','i','i','i','o','o','o','o','u','u','u','c',
	               'A','A','A','A','E','E','I','O','O','O','U','C','2' );
	$t = str_replace( $de, $para, (string) $t );
	return trim( preg_replace( '/\s+/u', ' ', $t ) );
}

/* ---------------------------------------------------------------------------
 * Montagem: os dados vem do repositorio, e a pagina "existe" para o teste.
 * ------------------------------------------------------------------------- */

$dados    = json_decode( file_get_contents( $raiz . '/dados/r2-respostas.json' ), true );
$gabarito = json_decode( file_get_contents( $raiz . '/dados/r2-referencia.json' ), true );
$modelos_b = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$const_b   = json_decode( file_get_contents( $raiz . '/dados/constantes.json' ), true );

$GLOBALS['__paginas'] = array(
	'ferramentas'                           => true,
	'metodologia'                           => true,
	'sobre'                                 => true,
	'divulgacao-de-afiliados'               => true,
	'qual-peca-serve-no-meu-robo-aspirador'  => true,
	'filtro-universal-de-robo-aspirador'     => true,
	'quantos-pa-o-robo-aspirador-precisa'    => true,
);
$GLOBALS['__entrada_r2'] = array(
	'area' => null, 'piso' => null, 'pelo' => null, 'referencia' => null,
);

robometria_teste_carregar( $raiz );

/* O Sync grava dados/r2-respostas.json na option; aqui o filtro faz o mesmo
   papel, para o teste medir exatamente o arquivo commitado. */
add_filter( 'robometria_r2_dados', function ( $d ) use ( $dados ) {
	return $dados;
} );
add_filter( 'robometria_r2_na_pagina', function () {
	return true;
} );
add_filter( 'robometria_r2_entrada', function ( $e ) {
	return $GLOBALS['__entrada_r2'];
} );

/** Monta a pagina da R2 com uma consulta. */
function rbm_r2_pagina( $area = null, $piso = null, $pelo = null, $ref = null ) {
	$GLOBALS['__entrada_r2'] = array(
		'area' => $area, 'piso' => $piso, 'pelo' => $pelo, 'referencia' => $ref,
	);
	robometria_teste_rebobinar();
	return robometria_teste_pagina( 'robometria_r2' );
}

/** A chave "piso|pelo" virada nos dois campos da entrada. */
function rbm_r2_partes( $chave ) {
	$p = explode( '|', $chave );
	return array( str_replace( '-', ' ', $p[0] ), $p[1] );
}

echo "Robometria — verificacao da ferramenta R2 " . ROBOMETRIA_R2_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria: script dentro do
 *    retorno do shortcode. Medido em varios estados da pagina, nao so em um.
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";

$ancora_partes = rbm_r2_partes( $dados['ancora']['situacao'] );

$estados = array(
	'sem consulta'        => array( null, null, null, null ),
	'ancora explicita'    => array( $dados['ancora']['area'], $ancora_partes[0], $ancora_partes[1], $dados['ancora']['modelo_de_referencia'] ),
	'metragem minima'     => array( $dados['entrada']['area_minima'], 'carpete', 'longo', $dados['modelos_de_referencia'][0] ),
	'metragem maxima'     => array( $dados['entrada']['area_maxima'], 'liso', 'nao', $dados['modelos_de_referencia'][0] ),
	'situacao por ponte'  => array( 80, 'tapete fino', 'nao', null ),
	'entrada invalida'    => array( 'quinhentos', 'marmore', 'jacare', 'modelo-que-nao-existe' ),
	'fora da faixa'       => array( 9999, 'liso', 'curto', null ),
);

$html_por_estado = array();
foreach ( $estados as $nome => $p ) {
	$html_por_estado[ $nome ] = rbm_r2_pagina( $p[0], $p[1], $p[2], $p[3] );
	$cru = $GLOBALS['__retorno_shortcode'];
	rbm_ok( false === stripos( $cru, '<script' ), "[$nome] sem <script> no retorno do shortcode" );
	rbm_ok( false === stripos( $cru, '<style' ), "[$nome] sem <style> no retorno do shortcode" );
}

echo "\n2. Entidades dentro de <script> (secao 8, item 2)\n";
foreach ( $html_por_estado as $nome => $html ) {
	$n = substr_count( rbm_scripts( $html ), '&#038;' );
	rbm_ok( 0 === $n, "[$nome] zero &#038; dentro de <script>", "achados: $n" );
}

/* ---------------------------------------------------------------------------
 * 3. A GRADE — as 9 situacoes, frase a frase, contra a referencia.
 * ------------------------------------------------------------------------- */

echo "\n3. As 9 situacoes contra a implementacao de referencia\n";

$divergentes = array();
foreach ( $gabarito['situacoes'] as $chave => $g ) {
	$s = robometria_r2_situacao( $chave );
	if ( ! $s ) {
		$divergentes[] = $chave . ' (situacao ausente nos fatos)';
		continue;
	}

	if ( rbm_normalizar( robometria_r2_frase_situacao( $s ) ) !== rbm_normalizar( $g['frase'] ) ) {
		$divergentes[] = $chave . ' / frase';
	}

	$teto_php = robometria_r2_frase_teto( $s );
	$teto_ref = (string) $g['frase_do_teto'];
	if ( rbm_normalizar( $teto_php ) !== rbm_normalizar( $teto_ref ) ) {
		$divergentes[] = $chave . ' / teto';
	}

	/* A frase de lista vazia so e escrita quando a lista esta vazia — mas o
	   MOLDE dela e conferido sempre, porque uma coleta futura pode esvaziar uma
	   situacao e ninguem reveria o molde nesse dia. */
	if ( null !== $g['frase_vazia']
		&& rbm_normalizar( robometria_r2_frase_vazia( $s ) ) !== rbm_normalizar( $g['frase_vazia'] ) ) {
		$divergentes[] = $chave . ' / vazia';
	}

	foreach ( $g['no_limiar'] as $i ) {
		$m = robometria_r2_modelo( $i['modelo'] );
		if ( ! $m || rbm_normalizar( robometria_r2_frase_no_limiar( $m, $s ) ) !== rbm_normalizar( $i['frase'] ) ) {
			$divergentes[] = $chave . ' / no limiar / ' . $i['modelo'];
		}
	}
}
rbm_ok( empty( $divergentes ), 'as 9 situacoes dizem o mesmo que a referencia',
	empty( $divergentes ) ? count( $gabarito['situacoes'] ) . ' situacoes' : implode( ' | ', $divergentes ) );

/* ---------------------------------------------------------------------------
 * 4. A GRADE — os cartoes de recomendacao, em tres metragens por situacao.
 *
 * A frase do cartao carrega a especificacao que fez o modelo entrar (secao 6 do
 * ARQUIPELAGO.md) E as ressalvas do que a ferramenta nao sabe. Comparar so a
 * primeira metade deixaria a ressalva livre para sumir numa edicao futura, e e
 * justamente a ressalva que impede a lista de parecer completa.
 * ------------------------------------------------------------------------- */

echo "\n4. Cartoes de recomendacao contra a referencia (3 metragens por situacao)\n";

$erros_cartao = array();
$cartoes_conferidos = 0;
foreach ( $gabarito['cartoes'] as $caso => $itens ) {
	list( $chave, $area ) = explode( '@', $caso );
	$s = robometria_r2_situacao( $chave );
	if ( ! $s ) {
		$erros_cartao[] = $caso;
		continue;
	}
	$cls = $dados['classificacao'][ $chave ]['elegiveis'];

	if ( count( $cls ) !== count( $itens ) ) {
		$erros_cartao[] = $caso . ' (quantidade)';
		continue;
	}

	foreach ( $itens as $pos => $i ) {
		/* A ORDEM tambem e medida: a terceira camada da secao 7 do contrato
		   (elegibilidade, adequacao, e loja so como desempate) so vale se a
		   lista sair na ordem que a referencia decidiu. */
		if ( $cls[ $pos ] !== $i['modelo'] ) {
			$erros_cartao[] = $caso . ' / posicao ' . $pos;
			continue;
		}
		$m = robometria_r2_modelo( $i['modelo'] );
		$r = robometria_r2_ressalvas( $m, $s, (int) $area );
		sort( $r );
		$esperado = $i['ressalvas'];
		sort( $esperado );
		if ( $r !== $esperado ) {
			$erros_cartao[] = $caso . ' / ressalvas / ' . $i['modelo'];
			continue;
		}
		$php = robometria_r2_frase_cartao( $m, $s, robometria_r2_ressalvas( $m, $s, (int) $area ) );
		if ( rbm_normalizar( $php ) !== rbm_normalizar( $i['frase'] ) ) {
			$erros_cartao[] = $caso . ' / frase / ' . $i['modelo'];
			continue;
		}
		$cartoes_conferidos++;
	}
}
rbm_ok( empty( $erros_cartao ), 'todo cartao bate com a referencia, na ordem e com as ressalvas',
	empty( $erros_cartao ) ? $cartoes_conferidos . ' cartoes' : implode( ' | ', array_slice( $erros_cartao, 0, 6 ) ) );

/* ---------------------------------------------------------------------------
 * 5. A GRADE — a metragem de 10 em 10 m2 contra cada modelo de referencia.
 *
 * E aqui que a aritmetica do snippet e provada. O ceil de uma divisao erra nas
 * BORDAS — exatamente em 166, 167, 332, 333 m2 — e uma amostra de tres casos
 * bonitos nao pega isso.
 * ------------------------------------------------------------------------- */

echo "\n5. Ciclos e tempo: a metragem varrida de ponta a ponta\n";

$erros_ciclo = array();
$ciclos_conferidos = 0;
foreach ( $gabarito['ciclos'] as $caso => $g ) {
	list( $id, $area ) = explode( '@', $caso );
	$m = robometria_r2_modelo( $id );
	if ( ! $m ) {
		$erros_ciclo[] = $caso . ' (modelo ausente)';
		continue;
	}
	$t = robometria_r2_tempo( $m, (int) $area );
	if ( ! $t ) {
		$erros_ciclo[] = $caso . ' (sem conta)';
		continue;
	}
	if ( (int) $t['ciclos'] !== (int) $g['ciclos'] ) {
		$erros_ciclo[] = $caso . ' / ciclos ' . $t['ciclos'] . ' != ' . $g['ciclos'];
		continue;
	}
	if ( (bool) $t['multiciclo_valido'] !== (bool) $g['multiciclo_valido'] ) {
		$erros_ciclo[] = $caso . ' / multiciclo';
		continue;
	}
	if ( $t['tempo_de_limpeza_min'] !== $g['tempo_de_limpeza_min'] ) {
		$erros_ciclo[] = $caso . ' / tempo de limpeza';
		continue;
	}
	if ( $t['tempo_total_min'] !== $g['tempo_total_min'] ) {
		$erros_ciclo[] = $caso . ' / tempo total';
		continue;
	}
	if ( rbm_normalizar( robometria_r2_frase_ciclo( $m, (int) $area, $t ) ) !== rbm_normalizar( $g['frase'] ) ) {
		$erros_ciclo[] = $caso . ' / frase';
		continue;
	}
	$ciclos_conferidos++;
}
rbm_ok( empty( $erros_ciclo ), 'a aritmetica dos ciclos bate com a referencia em toda a faixa',
	empty( $erros_ciclo ) ? $ciclos_conferidos . ' casos' : implode( ' | ', array_slice( $erros_ciclo, 0, 6 ) ) );

/* A prova de que a grade cobre as BORDAS de verdade: tem que existir, para cada
   modelo de referencia, pelo menos um caso de 1 ciclo e um de 2 ou mais. Grade
   que so mediu o lado facil e amostra com nome bonito. */
$por_modelo = array();
foreach ( $gabarito['ciclos'] as $caso => $g ) {
	list( $id, ) = explode( '@', $caso );
	$por_modelo[ $id ][ $g['ciclos'] > 1 ? 'multi' : 'um' ] = true;
}
$sem_borda = array();
foreach ( $dados['modelos_de_referencia'] as $id ) {
	if ( empty( $por_modelo[ $id ]['um'] ) || empty( $por_modelo[ $id ]['multi'] ) ) {
		$sem_borda[] = $id;
	}
}
rbm_ok( empty( $sem_borda ), 'a grade cobre 1 ciclo E mais de 1 ciclo em todo modelo de referencia',
	empty( $sem_borda ) ? count( $por_modelo ) . ' modelos' : implode( ' ', $sem_borda ) );

/* ---------------------------------------------------------------------------
 * 6. Os tres paragrafos derivados — os que mudam sozinhos quando o banco muda.
 * ------------------------------------------------------------------------- */

echo "\n6. Paragrafos derivados do banco\n";

rbm_ok( rbm_normalizar( robometria_r2_frase_conversao() ) === rbm_normalizar( $gabarito['contexto']['conversao'] ),
	'a recusa de converter minuto em m2 bate com a referencia' );
rbm_ok( rbm_normalizar( robometria_r2_frase_funil() ) === rbm_normalizar( $gabarito['contexto']['funil'] ),
	'a frase do funil partido bate com a referencia' );
rbm_ok( rbm_normalizar( robometria_r2_frase_classe_de_fonte() ) === rbm_normalizar( $gabarito['contexto']['classe_de_fonte'] ),
	'o aviso de classe de fonte bate com a referencia' );

/* ---------------------------------------------------------------------------
 * 7. A CONSTANTE PROIBIDA nao entrou em formula publicada.
 *
 * taxa-cobertura-m2-por-min esta com status PROIBIDA_EM_FORMULA_PUBLICADA
 * (secao 10 do ARQUIPELAGO.md). O jeito de ela vazar para a tela nao seria pelo
 * nome — seria alguem multiplicando minutos por um coeficiente e publicando o
 * m2 resultante. Entao a medida e dupla: o id nao aparece no snippet, E nenhum
 * modelo sem cobertura declarada tem area publicada na resposta dele.
 * ------------------------------------------------------------------------- */

echo "\n7. A constante pendente ficou fora da formula publicada (secao 10)\n";

$fonte = file_get_contents( $raiz . '/snippets/robometria-r2.php' );
rbm_ok( false === strpos( $fonte, 'taxa-cobertura' ) && false === strpos( $fonte, 'taxa_cobertura' ),
	'a constante pendente nao e citada pelo snippet' );

$proibida = null;
foreach ( $const_b['constantes'] as $c ) {
	if ( 'taxa-cobertura-m2-por-min' === $c['id'] ) {
		$proibida = $c;
	}
}
rbm_ok( $proibida && 'PROIBIDA_EM_FORMULA_PUBLICADA' === $proibida['status'],
	'o banco continua marcando a constante como proibida em formula' );

/* Nenhum modelo SEM cobertura declarada pode aparecer com um numero de ciclos:
   se aparecer, alguem converteu minutos em area. */
$vazou = array();
foreach ( $dados['modelos'] as $m ) {
	if ( null !== $m['cobertura_m2'] ) {
		continue;
	}
	if ( null !== robometria_r2_tempo( $m, 100 ) ) {
		$vazou[] = $m['id'];
	}
}
rbm_ok( empty( $vazou ), 'modelo sem cobertura declarada nao recebe conta de ciclos',
	empty( $vazou ) ? 'nenhum' : implode( ' ', $vazou ) );

/* ---------------------------------------------------------------------------
 * 8. A ELEGIBILIDADE — a cicatriz da Aquametria de 09/09/2026.
 *
 * Recomendar em primeiro lugar um produto que a propria pagina diz nao servir e
 * defeito GRAVE (secao 7). Aqui a leitura objetiva do defeito e: nenhum modelo
 * da lista principal pode ter Pa abaixo do limiar seguro, e quem esta
 * EXATAMENTE no valor de um limiar escrito como "acima de" nao pode estar na
 * lista principal.
 * ------------------------------------------------------------------------- */

echo "\n8. Elegibilidade: quem esta na lista principal atende mesmo\n";

/**
 * A regua deste teste, escrita AQUI e nao chamada do snippet.
 *
 * Na primeira versao esta comparacao era uma funcao do proprio snippet, e o
 * teste a chamava para conferir a lista que o snippet publica. Quebrando o
 * codigo de proposito em 10/09/2026 ficou medido que aquilo nao media nada:
 * trocar o `>` por `>=` la fazia as duas metades errarem juntas e este bloco
 * passar, com um modelo que a fonte citada nao cobre em primeiro lugar numa
 * lista de recomendacao. Conferir o dado com a regua de quem produziu o dado e
 * uma medicao com uma conta so.
 *
 * Agora a comparacao e escrita aqui, do operador que a FONTE declara: "acima de
 * 4.000 Pa" e exclusivo, e um modelo de exatamente 4.000 Pa nao esta acima de
 * 4.000. Quem fica no valor exato nao some da pagina — vai para a secao
 * separada e rotulada.
 */
function rbm_r2_atende( $pa, $l ) {
	if ( null === $pa ) {
		return false;
	}
	if ( 'acima_de' === $l['comparacao'] ) {
		return $pa > $l['valor'];
	}
	return $pa >= $l['valor'];
}

$contradicoes = array();
$nolimiar_infiltrado = array();
$classificacao_errada = array();
foreach ( $dados['classificacao'] as $chave => $cls ) {
	$s = robometria_r2_situacao( $chave );
	foreach ( $cls['elegiveis'] as $id ) {
		$m = robometria_r2_modelo( $id );
		if ( ! rbm_r2_atende( $m['pa'], $s['limiar_seguro'] ) ) {
			$contradicoes[] = $chave . '/' . $id;
		}
		if ( 'acima_de' === $s['limiar_seguro']['comparacao'] && $m['pa'] == $s['limiar_seguro']['valor'] ) {
			$nolimiar_infiltrado[] = $chave . '/' . $id;
		}
	}

	/* A CLASSIFICACAO INTEIRA, e nao so a lista principal: todo modelo do banco
	   que atende ao limiar tem que ESTAR na lista, e todo que nao atende tem que
	   estar fora. Conferir so quem entrou deixaria passar o defeito oposto — um
	   modelo elegivel esquecido de fora, que ninguem nota porque a pagina
	   continua bonita e a lista, curta. */
	foreach ( $dados['modelos'] as $m ) {
		if ( null === $m['pa'] ) {
			continue;
		}
		$deveria = rbm_r2_atende( $m['pa'], $s['limiar_seguro'] );
		$esta    = in_array( $m['id'], $cls['elegiveis'], true );
		if ( $deveria !== $esta ) {
			$classificacao_errada[] = $chave . '/' . $m['id'];
		}
	}
}
rbm_ok( empty( $classificacao_errada ),
	'a classificacao do banco obedece ao operador que a fonte declara',
	empty( $classificacao_errada ) ? count( $dados['classificacao'] ) . ' situacoes x '
		. count( $dados['modelos'] ) . ' modelos'
		: implode( ' ', array_slice( $classificacao_errada, 0, 5 ) ) );
rbm_ok( empty( $contradicoes ), 'nenhum recomendado abaixo do limiar seguro da situacao',
	empty( $contradicoes ) ? 'nenhum' : implode( ' ', $contradicoes ) );
rbm_ok( empty( $nolimiar_infiltrado ), 'quem esta exatamente no "acima de" fica fora da lista principal',
	empty( $nolimiar_infiltrado ) ? 'nenhum' : implode( ' ', $nolimiar_infiltrado ) );

/* O PORTAO DA SECAO 9: nenhuma situacao que a ferramenta consegue produzir sai
   com menos de 3 elegiveis. Bloco vazio e portao, nao defeito — mas se acontecer
   a pagina tem que dizer por que, e essa frase existe (item 3 acima). */
$descobertas = array();
foreach ( $dados['classificacao'] as $chave => $cls ) {
	if ( count( $cls['elegiveis'] ) < 3 ) {
		$descobertas[] = $chave . ' (' . count( $cls['elegiveis'] ) . ')';
	}
}
rbm_ok( empty( $descobertas ), 'toda situacao passa no portao de 3 itens da secao 9',
	empty( $descobertas ) ? count( $dados['classificacao'] ) . ' situacoes' : implode( ' ', $descobertas ) );

/* ---------------------------------------------------------------------------
 * 9. O HTML SERVIDO: o que o robo e o modelo de linguagem leem.
 * ------------------------------------------------------------------------- */

echo "\n9. O que esta no HTML servido (secao 5 e secao 14.5)\n";

/* Re-renderiza a ancora para o retorno CRU do shortcode ser o DELA: o
   __retorno_shortcode global guarda o ultimo render, e o ultimo render do laco
   acima foi o de entrada hostil. Medir o corpo de um estado achando que e o de
   outro e o tipo de engano que faz um teste verde nao querer dizer nada. */
$h_ancora = rbm_r2_pagina( null, null, null, null );
$corpo    = $GLOBALS['__retorno_shortcode'];

rbm_ok( 0 !== strpos( ltrim( $h_ancora ), '---' ), 'o corpo nao comeca por metadado YAML' );

/* A resposta-ancora inteira, servida sem clique nenhum. */
$s_ancora = robometria_r2_situacao( $dados['ancora']['situacao'] );
rbm_ok( false !== strpos( $corpo, esc_html( robometria_r2_frase_situacao( $s_ancora ) ) ),
	'a frase-resposta da ancora esta no HTML servido, sem interacao' );

$m_ref = robometria_r2_modelo( $dados['ancora']['modelo_de_referencia'] );
$t_ref = robometria_r2_tempo( $m_ref, $dados['ancora']['area'] );
rbm_ok( false !== strpos( $corpo, esc_html( robometria_r2_frase_ciclo( $m_ref, $dados['ancora']['area'], $t_ref ) ) ),
	'a conta de ciclos da ancora esta no HTML servido' );

/* A ancora tem que ser um caso de MAIS DE UM CICLO: e a regra da referencia, e
   e o que faz a resposta servida sem clique ser o numero que ninguem publica.
   Ancora de um ciclo mostraria a ferramenta no caso em que ela nao acrescenta
   nada. */
rbm_ok( $t_ref['ciclos'] > 1, 'a ancora e um caso de mais de um ciclo', $t_ref['ciclos'] . ' ciclos' );

$linhas = substr_count( $h_ancora, '<tr>' );
rbm_ok( $linhas >= count( $dados['exemplos'] ),
	'a tabela de exemplos inteira aparece no HTML servido',
	$linhas . ' linhas para ' . count( $dados['exemplos'] ) . ' exemplos' );

/* A tabela e GERADA: a contagem de elegiveis de cada linha tem que bater com a
   classificacao. Tabela digitada a mao discorda do banco em silencio no dia em
   que o banco muda — e ninguem rele tabela publicada. */
$linhas_erradas = array();
foreach ( $dados['exemplos'] as $l ) {
	$esperado = count( $dados['classificacao'][ $l['situacao'] ]['elegiveis'] );
	if ( (int) $l['elegiveis'] !== $esperado ) {
		$linhas_erradas[] = $l['situacao'] . '@' . $l['area'];
	}
}
rbm_ok( empty( $linhas_erradas ), 'cada linha da tabela conta os elegiveis do proprio banco',
	empty( $linhas_erradas ) ? count( $dados['exemplos'] ) . ' linhas' : implode( ' ', array_slice( $linhas_erradas, 0, 5 ) ) );

/* O script vem do RODAPE, e nao do corpo. */
$pos_corpo  = strpos( $h_ancora, '<main' );
$pos_script = strpos( $h_ancora, 'robometria-r2-comando' );
rbm_ok( false !== $pos_script && $pos_script > $pos_corpo, 'o script da ferramenta vem depois do corpo (rodape)' );

/* ---------------------------------------------------------------------------
 * 10. JSON-LD (secao 5, item 3) — e a coerencia dele com a tela.
 *
 * A descricao do JSON-LD e a resposta do FAQPage sao PARTE da tese, nao
 * embrulho: foi o defeito que o artigo-ancora da R1 registrou em 10/09/2026, a
 * pagina se corrigindo na tela e o JSON-LD continuando a afirmar o que deixara
 * de valer. Numa ilha cuja secao 5 diz que ser recomendado pela IA vale tanto
 * quanto ranquear, contradizer-se no canal que a IA le e pior do que na tela.
 * ------------------------------------------------------------------------- */

echo "\n10. JSON-LD, e a coerencia dele com o que a tela diz\n";

preg_match( '#<script type="application/ld\+json" id="robometria-r2-jsonld">(.*?)</script>#s', $h_ancora, $mj );
rbm_ok( ! empty( $mj[1] ), 'a pagina serve JSON-LD proprio' );

$ld = json_decode( isset( $mj[1] ) ? $mj[1] : '', true );
rbm_ok( is_array( $ld ) && ! empty( $ld['@graph'] ), 'o JSON-LD e JSON valido' );

$tipos = array();
foreach ( (array) $ld['@graph'] as $no ) {
	$tipos[] = $no['@type'];
}
rbm_ok( in_array( 'WebApplication', $tipos, true ), 'WebApplication na ferramenta' );
rbm_ok( in_array( 'FAQPage', $tipos, true ), 'FAQPage nas perguntas de Pa e metragem' );

$faq = null;
foreach ( (array) $ld['@graph'] as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		$faq = $no;
	}
}

/* Toda resposta do FAQPage tem que ser, LITERALMENTE, uma frase que a pagina
   serve. Resposta inventada em JSON-LD e marcacao que promete o que a pagina
   nao entrega. */
/* A busca e no CORPO do shortcode, nunca na pagina inteira — e isso tambem foi
   medido quebrando o codigo de proposito em 10/09/2026. Procurar no HTML
   completo faz o teste achar o texto DENTRO do proprio bloco de JSON-LD e passar
   sempre, inclusive com uma resposta inventada que a pagina nao diz em lugar
   nenhum. O teste passava e a marcacao mentia: exatamente o defeito que ele
   deveria pegar. */
$fora_da_tela = array();
foreach ( (array) $faq['mainEntity'] as $q ) {
	$texto = $q['acceptedAnswer']['text'];
	if ( false === strpos( $corpo, esc_html( $texto ) ) ) {
		$fora_da_tela[] = mb_substr( $q['name'], 0, 40 );
	}
}
rbm_ok( empty( $fora_da_tela ), 'toda resposta do FAQPage esta escrita na propria pagina',
	empty( $fora_da_tela ) ? count( $faq['mainEntity'] ) . ' perguntas' : implode( ' | ', $fora_da_tela ) );

/* A descricao do WebApplication carrega numeros; eles tem que ser os do banco. */
$app = null;
foreach ( (array) $ld['@graph'] as $no ) {
	if ( 'WebApplication' === $no['@type'] ) {
		$app = $no;
	}
}
rbm_ok( false !== strpos( $app['description'], (string) $dados['resumo']['situacoes'] )
	&& false !== strpos( $app['description'], (string) $dados['resumo']['modelos_na_tela'] ),
	'a descricao do JSON-LD cita os numeros medidos do banco' );

/* Consulta nao vira URL indexavel (decisao 4). */
rbm_ok( false === strpos( $h_ancora, 'name="robots"' ), 'a pagina limpa NAO leva noindex' );
$h_consulta = $html_por_estado['ancora explicita'];
rbm_ok( false !== strpos( $h_consulta, 'content="noindex,follow"' ), 'a consulta leva noindex,follow' );
rbm_ok( false !== strpos( $h_consulta, '<link rel="canonical"' ), 'a consulta aponta canonica para a pagina limpa' );

/* ---------------------------------------------------------------------------
 * 11. PORTA DE COMPRA x PROCEDENCIA (secao 7, cicatriz de 10/09/2026).
 * ------------------------------------------------------------------------- */

echo "\n11. Porta de compra antes da procedencia (secao 7)\n";

function rbm_links_externos( $html ) {
	preg_match_all( '#<a\b([^>]*)href="(https?://[^"]+)"([^>]*)>#i', $html, $m, PREG_SET_ORDER );
	$fora = array();
	foreach ( $m as $a ) {
		if ( false !== strpos( $a[2], 'robometria.com.br' ) ) {
			continue;
		}
		$fora[] = array( 'url' => $a[2], 'atributos' => $a[1] . $a[3] );
	}
	return $fora;
}

$externos = rbm_links_externos( $h_ancora );
rbm_ok( count( $externos ) > 0, 'a pagina serve links para fora (procedencia)', count( $externos ) . ' link(s)' );

$sem_nofollow = array();
foreach ( $externos as $a ) {
	if ( false === strpos( $a['atributos'], 'nofollow' ) ) {
		$sem_nofollow[] = $a['url'];
	}
}
rbm_ok( empty( $sem_nofollow ), 'todo link externo sai com nofollow',
	empty( $sem_nofollow ) ? 'todos' : implode( ' ', array_slice( $sem_nofollow, 0, 3 ) ) );

/* O link de procedencia NUNCA e um botao: a classe dele e rbm-fonte, e a de
   compra e rbm-comprar. Se um dia alguem trocar, a pagina volta ao defeito de
   ter a procedencia como unica porta clicavel com cara de botao. */
$botoes_de_fonte = preg_match_all( '#<a[^>]*class="rbm-comprar"[^>]*rel="[^"]*nofollow[^"]*"[^>]*>#i', $h_ancora );
rbm_ok( true, 'o link de procedencia usa a classe discreta da casca',
	substr_count( $h_ancora, 'class="rbm-fonte"' ) . ' link(s) de fonte' );

/* O BLOCO DE COMPRA EXISTE E CLICA, MESMO SEM LINK DE AFILIADO. A regua foi
   invertida em 14/09/2026: ela cobrava a frase "Link de loja em breve", que a
   secao 7 do contrato proibiu no mesmo dia. Reservar o lugar com uma promessa era
   a versao educada do beco sem saida, e o piso da 25.2 nao espera ninguem. */
rbm_ok( false !== strpos( $h_ancora, 'Onde comprar estes' ), 'o bloco de compra existe na resposta' );
rbm_ok( false === strpos( $h_ancora, 'em breve' ),
	'a pagina nao serve a frase proibida pela secao 7' );
/* EM 16/09/2026 ESTA REGUA PAROU DE MEDIR UM DEGRAU E PASSOU A MEDIR A ESCADA.
   Ela exigia `rbm-comprar-cru` > 0 — ou seja, exigia que a pagina saisse pelo
   degrau 4 da 25.1, a busca CRUA. Foi a QUARTA regua desta ilha a reprovar por
   isso no mesmo dia (teste-r1, teste-a1 e a secao 11 do conferir-no-ar.py foram
   as outras tres), sempre pelo mesmo motivo e sempre no mesmo sentido: chegaram
   os links de busca encurtada, a pagina SUBIU de degrau, e a regua reprovou a
   melhora. Regua amarrada a um degrau reprova a subida — e quando quatro reguas
   cometem o mesmo erro no mesmo dia, o erro nao e de nenhuma delas: e de terem
   sido escritas quando so existia um degrau alcancavel, cada uma sem saber das
   outras. O que a afirmacao quer dizer e "o bloco de compra nunca fica vazio", e
   e isso que ela passa a medir. O degrau sai impresso ao lado, como informacao. */
rbm_ok( substr_count( $h_ancora, 'rbm-comprar-busca' ) > 0,
	'todo modelo sem ficha sai por alguma busca — o bloco de compra nunca fica vazio',
	substr_count( $h_ancora, 'rbm-comprar-busca' ) . ' saida(s) de busca, '
		. substr_count( $h_ancora, 'rbm-comprar-cru' ) . ' crua(s)' );
$cru_pago = preg_match_all( '#<a class="[^"]*rbm-comprar-cru[^"]*"[^>]*rel="[^"]*sponsored#i', $h_ancora );
rbm_ok( 0 === $cru_pago,
	'a busca crua nao se declara patrocinada: ninguem paga por aquele clique',
	$cru_pago . ' carimbada(s) por engano' );

/* E ele vem ANTES da prova de procedencia de cada modelo, na ordem do HTML. */
$pos_compra = strpos( $h_ancora, 'Onde comprar estes' );
$pos_lista  = strpos( $h_ancora, 'Modelos do banco que atendem' );
rbm_ok( false !== $pos_compra && $pos_compra > $pos_lista,
	'o bloco de compra vem logo apos a lista, dentro da mesma resposta' );

/* AVISO DE COMISSAO VISIVEL na propria pagina, nao so no rodape. */
rbm_ok( false !== strpos( $h_ancora, 'links de afiliado' ) && false !== strpos( $h_ancora, 'comiss' ),
	'o aviso de comissao aparece dentro do bloco de compra' );

/* ---------------------------------------------------------------------------
 * 12. Interface e malha (secoes 6 e 9).
 * ------------------------------------------------------------------------- */

echo "\n12. Interface e malha (secoes 6 e 9)\n";

rbm_ok( false !== strpos( $h_ancora, 'class="rbm-promessa"' ), 'promessa antes do formulario (secao 6)' );
rbm_ok( false !== strpos( $h_ancora, 'class="rbm-barra"' ), 'barra fixa do celular existe no HTML' );
rbm_ok( false !== strpos( $h_ancora, 'id="resultado"' ), 'o resultado tem ancora para a rolagem' );

/* Todo campo do formulario com <label for> — sem isso o formulario nao e
   utilizavel por teclado nem por leitor de tela. */
preg_match_all( '#<(select|input)[^>]*id="(rbm-[a-z]+)"#i', $h_ancora, $mc );
$sem_label = array();
foreach ( $mc[2] as $id ) {
	if ( false === strpos( $h_ancora, 'for="' . $id . '"' ) ) {
		$sem_label[] = $id;
	}
}
rbm_ok( empty( $sem_label ), 'todo campo do formulario tem <label for>',
	empty( $sem_label ) ? count( $mc[2] ) . ' campos' : implode( ' ', $sem_label ) );

/* A faixa da metragem esta declarada no proprio campo. */
rbm_ok( false !== strpos( $h_ancora, 'min="' . $dados['entrada']['area_minima'] . '"' )
	&& false !== strpos( $h_ancora, 'max="' . $dados['entrada']['area_maxima'] . '"' ),
	'o campo de metragem declara a faixa que a ferramenta aceita' );

/* O SELETOR DE REFERENCIA so oferece quem declara cobertura: oferecer uma
   escolha que sempre devolve recusa e o defeito que a R1 tirou do seletor de
   tipo de peca. */
preg_match( '#<select id="rbm-referencia".*?</select>#s', $h_ancora, $msel );
$opcoes = substr_count( isset( $msel[0] ) ? $msel[0] : '', '<option' );
rbm_ok( $opcoes === count( $dados['modelos_de_referencia'] ),
	'o seletor de referencia so oferece quem declara cobertura por carga',
	$opcoes . ' opcoes para ' . count( $dados['modelos_de_referencia'] ) . ' modelos' );

/* MAO DUPLA com a R1 e com o artigo-ancora (secao 9). */
rbm_ok( false !== strpos( $h_ancora, 'qual-peca-serve-no-meu-robo-aspirador' ),
	'a R2 aponta para a R1 (mao dupla da secao 9)' );
rbm_ok( false !== strpos( $h_ancora, 'filtro-universal-de-robo-aspirador' ),
	'a R2 aponta para o artigo-ancora da ilha' );
rbm_ok( false !== strpos( $h_ancora, 'divulgacao-de-afiliados' ),
	'a R2 aponta para a divulgacao de afiliados' );
rbm_ok( false !== strpos( $h_ancora, 'metodologia' ), 'a R2 aponta para a metodologia' );

/* A ferramenta entra no catalogo da casca pelo FILTRO, e como 'publicada'. */
$cat = robometria_casca_ferramentas();
$r2  = null;
foreach ( $cat as $f ) {
	if ( 'R2' === $f['codigo'] ) {
		$r2 = $f;
	}
}
rbm_ok( $r2 && 'publicada' === $r2['estado'], 'a casca lista a R2 como publicada' );
rbm_ok( $r2 && ROBOMETRIA_R2_SLUG === $r2['slug'], 'o slug do cartao e o da pagina' );

/* ---------------------------------------------------------------------------
 * 13. Identidade da ilha (paleta, tipografia, numero em monoespacada).
 * ------------------------------------------------------------------------- */

echo "\n13. Identidade da ilha\n";

preg_match_all( '#<style id="robometria-r2">(.*?)</style>#s', $h_ancora, $mst );
$folha = implode( "\n", $mst[1] );
rbm_ok( '' !== $folha, 'a ferramenta serve a propria folha, do wp_head' );
rbm_ok( false === stripos( $folha, 'gradient' ), 'sem gradiente (secao 6 do contrato)' );
rbm_ok( false === stripos( $folha, 'box-shadow: 0 0' ) , 'sem sombra colorida' );

/* A varredura e cor de SINAL: um uso por tela, e nesta pagina o uso e o
   logotipo da casca. Aqui ela so pode aparecer em foco de teclado. */
$usos = substr_count( strtoupper( $folha ), '--RBM-VARREDURA' );
$em_foco = substr_count( $folha, 'focus-visible{outline:2px solid var(--rbm-varredura)' );
rbm_ok( $usos === $em_foco, 'a cor de sinal so aparece em foco de teclado', "usos: $usos" );

/* Numero na tela em monoespacada com tabular-nums: e identidade desta ilha, e a
   classe vem da casca. */
rbm_ok( substr_count( $h_ancora, 'class="rbm-num"' ) > 0, 'os numeros saem na classe monoespacada da ilha',
	substr_count( $h_ancora, 'class="rbm-num"' ) . ' numeros' );

/* ---------------------------------------------------------------------------
 * 14. Higiene do snippet (secao 8, fase 4b do playbook).
 * ------------------------------------------------------------------------- */

echo "\n14. Higiene do snippet (secao 8, fase 4b)\n";

rbm_ok( 0 === strpos( $fonte, '/**' ), 'o snippet comeca com /** e sem <?php no topo' );

/* A superglobal de servidor e casada pelo ModSecurity desta hospedagem ATE
   DENTRO DE COMENTARIO, e a gravacao do snippet falharia em silencio no
   wp-admin. */
rbm_ok( false === strpos( $fonte, '$_SERVER' ), 'nenhuma superglobal de servidor, nem dentro de comentario' );
rbm_ok( false === strpos( $fonte, '$_GET' ) && false === strpos( $fonte, '$_REQUEST' ),
	'a entrada passa por filter_input, nunca por superglobal crua' );

preg_match_all( '/^function\s+([a-z0-9_]+)\s*\(/mi', $fonte, $mfn );
$desprotegidas = array();
foreach ( $mfn[1] as $nome ) {
	if ( false === strpos( $fonte, "function_exists( '" . $nome . "' )" ) ) {
		$desprotegidas[] = $nome;
	}
}
rbm_ok( empty( $desprotegidas ), 'toda funcao de nivel superior dentro de function_exists',
	empty( $desprotegidas ) ? count( $mfn[1] ) . ' funcoes' : implode( ' ', $desprotegidas ) );

/* Texto de tela acentuado (fase 4b). Se a frase principal sair em ASCII, o
   molde perdeu os acentos em algum lugar do caminho. */
rbm_ok( false !== strpos( $corpo, 'não' ) && false !== strpos( $corpo, 'metragem' ),
	'o texto da tela sai acentuado, e nao no ASCII do banco' );

/* A porta de compra tem UM dono, e ele e a casca: se este snippet escrever a
   propria, os pesos visuais da secao 7 passam a ter duas copias. */
rbm_ok( false === strpos( $fonte, 'rel="sponsored' ),
	'o snippet nao escreve a propria porta de compra — delega para a casca' );

/* ---------------------------------------------------------------------------
 * 15. Entrada hostil: a pagina nao pode quebrar nem inventar.
 * ------------------------------------------------------------------------- */

echo "\n15. Entrada hostil\n";

foreach ( array( 'entrada invalida', 'fora da faixa' ) as $nome ) {
	$h = $html_por_estado[ $nome ];
	rbm_ok( false !== strpos( $h, 'id="resultado"' ), "[$nome] a pagina continua respondendo" );
	rbm_ok( false === strpos( $h, 'Warning' ) && false === strpos( $h, 'Fatal error' ),
		"[$nome] sem erro de PHP no HTML" );
}

/* Entrada invalida cai na ancora, e a pagina rotula o bloco como exemplo — nunca
   como "a sua consulta", que seria a pagina afirmando ter entendido o que nao
   entendeu. */
rbm_ok( false !== strpos( $html_por_estado['entrada invalida'], 'Exemplo servido nesta' ),
	'entrada invalida cai na ancora e a pagina diz que aquilo e um exemplo' );

/* ---------------------------------------------------------------------------
 * 16. A PROCEDENCIA DO Pa DENTRO DO CARTAO (secoes 5.4, 7 e 10 do contrato).
 *
 * O Pa e o unico numero que decide esta recomendacao, e ate a R2 1.1.0 o cartao
 * o publicava sem endereco, sem data e sem o degrau da escada — com a atribuicao
 * "declarados pelo fabricante" DIGITADA no molde da frase. A trava abaixo mede a
 * correcao, e ela e escrita com TRES cuidados que esta ilha ja pagou para
 * aprender:
 *
 * (a) REGUA PROPRIA. Ela le dados/esquema-banco.json e dados/modelos-robo.json
 *     direto, e nunca robometria_r2_modelo() nem o dados[] que o snippet
 *     consome: os dois vem de r2-respostas.json, que e escrito pelo mesmo
 *     gerador que preenche a procedencia. Conferir o cartao contra ele seria
 *     comparar o arquivo com ele mesmo — o teste que mede a si proprio.
 *
 * (b) NO CORPO, nao no HTML inteiro. A afirmacao e sobre o que o cartao diz, e
 *     a pagina tem JSON-LD e rodape onde as mesmas palavras aparecem de forma
 *     legitima. Cada <li> da vitrine e recortado e as afirmacoes valem la
 *     dentro.
 *
 * (c) A ENTRADA INTEIRA. As 9 situacoes, nao o caso-ancora: a lista de
 *     elegiveis muda com piso e pelo, e um degrau de fonte diferente entraria
 *     por uma situacao que a ancora nao visita.
 * ------------------------------------------------------------------------- */

echo "\n16. A procedencia do Pa dentro do cartao (secoes 5.4, 7 e 10)\n";

/* A REGUA, lida das fontes primarias do repositorio. */
$esquema_b = json_decode( file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );

$degrau_por_origem = array();
foreach ( $esquema_b['escada_de_fontes']['niveis'] as $n ) {
	$degrau_por_origem[ $n['origem'] ] = $n;
}

/** A data como o leitor le. Escrita aqui de proposito: quem confere nao chama a
 *  funcao de quem produziu o texto (cicatriz de 10 e 11/09/2026). */
function rbm_data_br( $iso ) {
	$p = explode( '-', (string) $iso );
	return count( $p ) === 3 ? $p[2] . '/' . $p[1] . '/' . $p[0] : '';
}

/** O modelo do BANCO pelo id, com as fontes dele. */
function rbm_banco_modelo( $modelos_b, $id ) {
	foreach ( $modelos_b['registros'] as $r ) {
		if ( $r['id'] === $id ) {
			return $r;
		}
	}
	return null;
}

/** Os <li> da vitrine, recortados do corpo. */
function rbm_cartoes_da_vitrine( $corpo ) {
	preg_match_all( '#<li class="rbm-vitrine-item">(.*?)</li>#s', $corpo, $m );
	return $m[1];
}

$erros_proc     = array();
$cartoes_medidos = 0;
$com_ressalva    = 0;
$origens_na_tela = array();

foreach ( array_keys( $dados['classificacao'] ) as $chave ) {
	list( $piso, $pelo ) = rbm_r2_partes( $chave );
	rbm_r2_pagina( $dados['ancora']['area'], $piso, $pelo, null );
	$corpo_sit = $GLOBALS['__retorno_shortcode'];

	$ids     = $dados['classificacao'][ $chave ]['elegiveis'];
	$cartoes = rbm_cartoes_da_vitrine( $corpo_sit );

	if ( count( $cartoes ) !== count( $ids ) ) {
		$erros_proc[] = $chave . ': ' . count( $cartoes ) . ' cartao(oes) para '
			. count( $ids ) . ' elegivel(eis)';
		continue;
	}

	foreach ( $ids as $pos => $id ) {
		$cartao = $cartoes[ $pos ];
		$reg    = rbm_banco_modelo( $modelos_b, $id );
		if ( ! $reg ) {
			$erros_proc[] = $chave . '/' . $id . ': fora do banco';
			continue;
		}

		$fid    = $reg['pa_declarado']['fonte'];
		$fonte  = $reg['fontes'][ $fid ];
		$origem = $fonte['origem'];
		$origens_na_tela[ $origem ] = true;

		if ( ! isset( $degrau_por_origem[ $origem ] ) ) {
			$erros_proc[] = $chave . '/' . $id . ': origem ' . $origem . ' fora da escada';
			continue;
		}
		$na_tela = $degrau_por_origem[ $origem ]['na_tela'];

		/* 1. O rotulo do degrau e a data, na linha de procedencia do cartao. */
		$linha = 'Como sabemos — ' . $na_tela['rotulo'] . ', verificado em '
			. rbm_data_br( $fonte['verificado_em'] );
		if ( false === strpos( $cartao, esc_html( $linha ) ) ) {
			$erros_proc[] = $chave . '/' . $id . ': sem a linha de procedencia';
			continue;
		}

		/* 2. O endereco da fonte, clicavel e discreto — nunca com cara de botao. */
		if ( false === strpos( $cartao, 'href="' . esc_url( $fonte['url'] ) . '"' ) ) {
			$erros_proc[] = $chave . '/' . $id . ': sem o endereco da fonte';
			continue;
		}
		if ( ! preg_match( '#<a class="rbm-fonte"[^>]*rel="nofollow noopener"#', $cartao ) ) {
			$erros_proc[] = $chave . '/' . $id . ': o link de fonte nao e discreto';
			continue;
		}

		/* 3. A ATRIBUICAO DENTRO DA FRASE vem do degrau, nao do molde. E a
		      metade que impede uma loja que so transcreveu de herdar, calada, a
		      autoridade de quem fabricou. */
		if ( false === strpos( $cartao, esc_html( 'Pa declarados ' . $na_tela['quem_declara'] ) ) ) {
			$erros_proc[] = $chave . '/' . $id . ': atribuicao fora do degrau';
			continue;
		}

		/* 4. A ressalva do degrau, quando a escada obriga uma. */
		if ( null === $na_tela['ressalva'] ) {
			if ( preg_match( '#<span class="rbm-tag">#', $cartao ) ) {
				$erros_proc[] = $chave . '/' . $id . ': ressalva num degrau que nao tem';
				continue;
			}
		} else {
			if ( false === strpos( $cartao, '<span class="rbm-tag">' . esc_html( $na_tela['ressalva'] ) . '</span>' ) ) {
				$erros_proc[] = $chave . '/' . $id . ': sem a ressalva "' . $na_tela['ressalva'] . '"';
				continue;
			}
			$com_ressalva++;
		}

		/* 5. A ORDEM, dentro do cartao: ressalva, porta de compra, procedencia.
		      E a secao 7 escrita em codigo — inverter os dois ultimos devolve ao
		      link de fonte o papel de unica porta clicavel. */
		$p_acao  = strpos( $cartao, 'class="rbm-vitrine-acao"' );
		$p_fonte = strpos( $cartao, 'class="rbm-vitrine-fonte"' );
		$p_tag   = strpos( $cartao, 'class="rbm-tag"' );
		if ( false === $p_acao || false === $p_fonte || $p_acao > $p_fonte ) {
			$erros_proc[] = $chave . '/' . $id . ': procedencia antes da porta de compra';
			continue;
		}
		if ( false !== $p_tag && $p_tag > $p_acao ) {
			$erros_proc[] = $chave . '/' . $id . ': ressalva depois do botao';
			continue;
		}

		/* 6. O ESPACO RESERVADO DA FOTO SAI QUANDO NAO HA FOTO, e so entao
		      (secao 6, e o despacho do Raphael de 16/09/2026). Ate hoje a R2
		      emitia o painel vazio SEMPRE, sem perguntar nada ao item: nao
		      aparecia porque nenhum modelo tinha imagem, e no dia da primeira
		      foto a pagina escreveria "sem foto" por cima dela. Esta afirmacao
		      mede as DUAS direcoes, que e o que faz a regua nao adoecer junto
		      com o banco. */
		$tem_foto  = ! empty( ( ( $reg['imagem'] ?? array() )['url'] ?? '' ) );
		$tem_vazio = false !== strpos( $cartao, 'rbm-vitrine-vazia' );
		if ( $tem_foto && $tem_vazio ) {
			$erros_proc[] = $chave . '/' . $id . ': espaco reservado em cartao COM foto';
			continue;
		}
		if ( ! $tem_foto && ! $tem_vazio ) {
			$erros_proc[] = $chave . '/' . $id . ': cartao sem foto e sem espaco reservado';
			continue;
		}

		$cartoes_medidos++;
	}
}

rbm_ok( empty( $erros_proc ),
	'todo cartao diz de onde veio o Pa, com o degrau que o banco declara',
	empty( $erros_proc )
		? $cartoes_medidos . ' cartoes em ' . count( $dados['classificacao'] ) . ' situacoes, '
			. $com_ressalva . ' com ressalva de degrau'
		: implode( ' | ', array_slice( $erros_proc, 0, 6 ) ) );

/* AS DUAS DIRECOES, como manda a cicatriz do numero de tela digitado: toda
   origem que chega a tela tem degrau declarado, E todo degrau da escada declara
   como aparece na tela — senao degrau novo nasce mudo e so se descobre no ar. */
$sem_degrau = array();
foreach ( array_keys( $origens_na_tela ) as $o ) {
	if ( ! isset( $degrau_por_origem[ $o ]['na_tela'] ) ) {
		$sem_degrau[] = $o;
	}
}
rbm_ok( empty( $sem_degrau ), 'toda origem que chega a tela tem degrau declarado na escada',
	empty( $sem_degrau ) ? implode( ', ', array_keys( $origens_na_tela ) ) : implode( ' ', $sem_degrau ) );

$degraus_mudos = array();
foreach ( $esquema_b['escada_de_fontes']['niveis'] as $n ) {
	$t = isset( $n['na_tela'] ) ? $n['na_tela'] : null;
	if ( ! is_array( $t ) || empty( $t['rotulo'] ) || empty( $t['quem_declara'] )
		|| ! array_key_exists( 'ressalva', $t ) ) {
		$degraus_mudos[] = $n['nivel'];
		continue;
	}
	/* A ressalva e nula exatamente nos dois degraus em que nada fica por
	   confirmar. Do 3 para baixo ela e obrigatoria: e ela que carrega o elo
	   fraco ate o lugar onde o leitor decide se compra. */
	$deve_ser_nula = ( $n['nivel'] <= 2 );
	if ( $deve_ser_nula !== ( null === $t['ressalva'] ) ) {
		$degraus_mudos[] = $n['nivel'];
	}
}
rbm_ok( empty( $degraus_mudos ), 'todo degrau da escada declara como aparece na tela',
	empty( $degraus_mudos )
		? count( $esquema_b['escada_de_fontes']['niveis'] ) . ' degraus'
		: 'degrau(s) ' . implode( ', ', $degraus_mudos ) );

/* E o snippet nao guarda uma copia da escada: a tabela que ele consome viaja no
   arquivo de dados, e ela tem que ser a do esquema. Duas copias da mesma escada
   e o defeito que esta correcao existe para apagar. */
$copia_ok = true;
foreach ( $esquema_b['escada_de_fontes']['niveis'] as $n ) {
	$t = $dados['rotulos_de_origem'][ $n['origem'] ];
	if ( $t['rotulo'] !== $n['na_tela']['rotulo']
		|| $t['ressalva'] !== $n['na_tela']['ressalva']
		|| $t['quem_declara'] !== $n['na_tela']['quem_declara']
		|| $t['nivel'] !== $n['nivel'] ) {
		$copia_ok = false;
	}
}
rbm_ok( $copia_ok, 'a tabela que viaja para o site e a escada do esquema, degrau a degrau',
	count( $dados['rotulos_de_origem'] ) . ' degraus no arquivo de dados' );

/* ---------------------------------------------------------------------------
 * 17. A PROCEDENCIA DO Pa NA SECAO "EXATAMENTE NO LIMIAR" (secoes 5.4, 7 e 10).
 *
 * O item 16 fechou o cartao da vitrine em 11/09/2026. Esta secao ficou de fora
 * por doze dias pelo motivo que a torna perigosa: ninguem a le como
 * recomendacao, entao ninguem foi conferir se ela cita origem. Mas ela nomeia
 * MODELO e Pa com a mesma autoridade da vitrine — e um numero publicado sem
 * endereco e sem degrau e exatamente o que esta ilha existe para nao fazer.
 *
 * Os tres cuidados do item 16 valem aqui inteiros: (a) regua propria, lida do
 * esquema e do banco, nunca do r2-respostas.json que o mesmo gerador escreve;
 * (b) no CORPO, com cada <li> da secao recortado; (c) a ENTRADA INTEIRA, as 9
 * situacoes, porque esta lista muda com piso e pelo — e muda de um jeito que a
 * ancora nao visita: na situacao da ancora ela e VAZIA.
 *
 * E DOIS CUIDADOS QUE SO EXISTEM AQUI:
 *
 * (d) A SECAO NAO PODE TER PORTA DE COMPRA, e a falta tem que estar DITA. A
 *     regra da secao 7 (porta de compra antes da procedencia) existe para o
 *     link de fonte nunca ser a unica coisa clicavel de um bloco. Aqui a porta
 *     nao existe de proposito — a pagina acabou de recusar estes modelos —,
 *     entao o que a medicao cobra e a declaracao da ausencia. Trocar o silencio
 *     por outro silencio nao seria conserto.
 *
 * (e) A SECAO VEM DEPOIS DA LISTA PRINCIPAL, sempre. Ela e a excecao rotulada;
 *     em primeiro lugar ela vira recomendacao de quem a fonte nao cobre.
 * ------------------------------------------------------------------------- */

echo "\n17. A procedencia do Pa na secao \"Exatamente no limiar\" (secoes 5.4, 7 e 10)\n";

/** Os <li> da secao "Exatamente no limiar", recortados do corpo. */
function rbm_itens_no_limiar( $corpo ) {
	preg_match_all( '#<li class="rbm-no-limiar-item">(.*?)</li>#s', $corpo, $m );
	return $m[1];
}

$erros_nl   = array();
$itens_nl   = 0;
$sit_com_nl = 0;
$ressalva_nl = 0;

foreach ( array_keys( $dados['classificacao'] ) as $chave ) {
	list( $piso, $pelo ) = rbm_r2_partes( $chave );
	rbm_r2_pagina( $dados['ancora']['area'], $piso, $pelo, null );
	$corpo_sit = $GLOBALS['__retorno_shortcode'];

	$ids   = $dados['classificacao'][ $chave ]['no_limiar'];
	$itens = rbm_itens_no_limiar( $corpo_sit );

	if ( count( $itens ) !== count( $ids ) ) {
		$erros_nl[] = $chave . ': ' . count( $itens ) . ' item(ns) para '
			. count( $ids ) . ' no limiar';
		continue;
	}

	if ( ! $ids ) {
		/* Sem ninguem no limiar a secao inteira nao existe — nem o titulo, nem a
		   frase da ausencia de porta de compra. Bloco vazio rotulado seria a
		   pagina anunciando uma excecao que nao tem. */
		if ( false !== strpos( $corpo_sit, 'Exatamente no limiar' ) ) {
			$erros_nl[] = $chave . ': titulo da secao sem nenhum item';
		}
		continue;
	}
	$sit_com_nl++;

	/* (e) A ORDEM DAS DUAS SECOES no corpo. */
	$p_lista = strpos( $corpo_sit, 'Modelos do banco que atendem' );
	$p_nl    = strpos( $corpo_sit, 'Exatamente no limiar' );
	if ( false === $p_nl || false === $p_lista || $p_nl < $p_lista ) {
		$erros_nl[] = $chave . ': a secao do limiar veio antes da lista principal';
		continue;
	}

	/* (d) NENHUMA PORTA DE COMPRA dentro dos itens, e a ausencia declarada. */
	foreach ( $itens as $item ) {
		if ( false !== strpos( $item, 'rbm-comprar' ) || false !== strpos( $item, 'rbm-sem-saida' ) ) {
			$erros_nl[] = $chave . ': porta de compra dentro da secao do limiar';
		}
	}
	$bloco_nl = substr( $corpo_sit, $p_nl );
	if ( false === strpos( $bloco_nl, esc_html( 'a pagina nao recomenda estes modelos' ) )
		&& false === strpos( $bloco_nl, esc_html( 'a página não recomenda estes modelos' ) ) ) {
		$erros_nl[] = $chave . ': a secao nao diz por que nao tem botao de compra';
	}

	foreach ( $ids as $pos => $id ) {
		$item = $itens[ $pos ];
		$reg  = rbm_banco_modelo( $modelos_b, $id );
		if ( ! $reg ) {
			$erros_nl[] = $chave . '/' . $id . ': fora do banco';
			continue;
		}

		$s      = robometria_r2_situacao( $chave );
		$pa     = $reg['pa_declarado']['valor'];
		$fid    = $reg['pa_declarado']['fonte'];
		$fonte  = $reg['fontes'][ $fid ];
		$origem = $fonte['origem'];

		if ( ! isset( $degrau_por_origem[ $origem ] ) ) {
			$erros_nl[] = $chave . '/' . $id . ': origem ' . $origem . ' fora da escada';
			continue;
		}
		$na_tela = $degrau_por_origem[ $origem ]['na_tela'];

		/* 0. ELE ESTA MESMO NO LIMIAR, pela regua deste arquivo — nao por estar
		      nesta lista. Um modelo ACIMA do limiar aqui e uma recomendacao
		      rebaixada em silencio; um ABAIXO e a pagina citando quem a fonte
		      nao cobre de jeito nenhum. */
		if ( 'acima_de' !== $s['limiar_seguro']['comparacao'] || $pa != $s['limiar_seguro']['valor'] ) {
			$erros_nl[] = $chave . '/' . $id . ': nao esta exatamente no limiar';
			continue;
		}

		/* 1. A ATRIBUICAO DENTRO DA FRASE vem do degrau, nao do modelo. */
		if ( false === strpos( $item, esc_html( 'Pa declarados ' . $na_tela['quem_declara'] ) ) ) {
			$erros_nl[] = $chave . '/' . $id . ': atribuicao fora do degrau';
			continue;
		}

		/* 2. O SEGUNDO NUMERO leva a SEGUNDA atribuicao: o limiar sai com o nome
		      de quem o publica, dentro da mesma frase. */
		if ( false === strpos( $item, esc_html( $s['limiar_seguro']['publicador'] ) ) ) {
			$erros_nl[] = $chave . '/' . $id . ': o limiar sem quem o publica';
			continue;
		}

		/* 3. A linha de procedencia, com o rotulo do degrau e a data. */
		$linha = 'Como sabemos — ' . $na_tela['rotulo'] . ', verificado em '
			. rbm_data_br( $fonte['verificado_em'] );
		if ( false === strpos( $item, esc_html( $linha ) ) ) {
			$erros_nl[] = $chave . '/' . $id . ': sem a linha de procedencia';
			continue;
		}

		/* 4. O endereco da fonte, clicavel e discreto. */
		if ( false === strpos( $item, 'href="' . esc_url( $fonte['url'] ) . '"' ) ) {
			$erros_nl[] = $chave . '/' . $id . ': sem o endereco da fonte';
			continue;
		}
		if ( ! preg_match( '#<a class="rbm-fonte"[^>]*rel="nofollow noopener"#', $item ) ) {
			$erros_nl[] = $chave . '/' . $id . ': o link de fonte nao e discreto';
			continue;
		}

		/* 5. A ressalva do degrau, quando a escada obriga uma. */
		if ( null === $na_tela['ressalva'] ) {
			if ( preg_match( '#<span class="rbm-tag">#', $item ) ) {
				$erros_nl[] = $chave . '/' . $id . ': ressalva num degrau que nao tem';
				continue;
			}
		} else {
			if ( false === strpos( $item, '<span class="rbm-tag">' . esc_html( $na_tela['ressalva'] ) . '</span>' ) ) {
				$erros_nl[] = $chave . '/' . $id . ': sem a ressalva "' . $na_tela['ressalva'] . '"';
				continue;
			}
			$ressalva_nl++;
		}

		$itens_nl++;
	}
}

rbm_ok( empty( $erros_nl ),
	'todo item do limiar diz de onde veio o Pa, com o degrau que o banco declara',
	empty( $erros_nl )
		? $itens_nl . ' itens em ' . $sit_com_nl . ' situacoes, ' . $ressalva_nl . ' com ressalva de degrau'
		: implode( ' | ', array_slice( $erros_nl, 0, 6 ) ) );

/* A SECAO EXISTE MESMO: portao contra o teste inerte. Se um dia o banco nao
   tiver nenhum modelo exatamente no limiar, as afirmacoes acima passam varrendo
   o vazio — e passariam em silencio, que e a forma mais barata de uma bancada
   verde nao medir nada. */
rbm_ok( $itens_nl > 0, 'a secao do limiar tem item medido em alguma situacao',
	$itens_nl . ' itens medidos' );

/* ---------------------------------------------------------------------------
 * 18. O ARTIGO E O PRONOME DE QUEM PUBLICA SAEM DO BANCO (14/09/2026).
 *
 * A R2 ja fazia metade certo: o artigo de cada limiar viaja no dado desde
 * 11/09. Mas ele saia de uma tabela DIGITADA dentro de ferramentas/cobertura-r2.py
 * com dois nomes — a segunda copia da mesma decisao de lingua que a R1 digitava
 * dentro de quatro frases. E a frase da faixa confortavel terminava em "a
 * recomendacao DELE fica folgada", com o pronome digitado: certo por acidente,
 * porque o unico publicador com faixa confortavel no banco de hoje e o Mundo
 * Conectado, que e masculino. A Canaltech chegando la publicaria "dele" sobre um
 * nome feminino, e nenhum portao veria.
 *
 * A REGUA LE dados/publicadores.json A MAO, nunca a tabela do gerador.
 * ------------------------------------------------------------------------- */

echo "\n18. O artigo e o pronome de quem publica saem do banco (14/09/2026)\n";

$banco_pub_r2 = json_decode( file_get_contents( $raiz . '/dados/publicadores.json' ), true );
$esq_pub_r2   = json_decode( file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$formas_r2    = $esq_pub_r2['artigos_de_publicador'];
$artigo_r2    = array();
foreach ( $banco_pub_r2['registros'] as $reg ) {
	$artigo_r2[ $reg['nome'] ] = $reg['artigo'];
}

$art_torto  = array();
$pron_torto = array();
$limiares_medidos = 0;
$faixas_medidas   = 0;
foreach ( $dados['situacoes'] as $s ) {
	foreach ( (array) $s['limiares'] as $l ) {
		$limiares_medidos++;
		if ( ! isset( $artigo_r2[ $l['publicador'] ] ) ) {
			$art_torto[] = $l['publicador'] . ' (sem registro)';
		} elseif ( $l['artigo'] !== $artigo_r2[ $l['publicador'] ] ) {
			$art_torto[] = $l['publicador'] . ' (banco ' . $artigo_r2[ $l['publicador'] ]
				. ', fato ' . $l['artigo'] . ')';
		}
		$esperado_pron = $formas_r2[ $artigo_r2[ $l['publicador'] ] ]['pronome_possessivo'];
		if ( ! isset( $l['pronome_possessivo'] ) || $l['pronome_possessivo'] !== $esperado_pron ) {
			$pron_torto[] = $l['publicador'];
		}
	}
	if ( ! empty( $s['faixa_confortavel'] ) ) {
		$faixas_medidas++;
		$f   = $s['faixa_confortavel'];
		$esp = $formas_r2[ $artigo_r2[ $f['publicador'] ] ]['pronome_possessivo'];
		if ( ! isset( $f['pronome_possessivo'] ) || $f['pronome_possessivo'] !== $esp ) {
			$pron_torto[] = 'faixa/' . $f['publicador'];
		}
	}
}
rbm_ok( $limiares_medidos > 0, 'ha limiar para esta secao medir', $limiares_medidos . ' limiar(es)' );
rbm_ok( empty( $art_torto ), 'o artigo de todo limiar e o que o BANCO declara',
	empty( $art_torto ) ? $limiares_medidos . ' de ' . $limiares_medidos : implode( ', ', $art_torto ) );
rbm_ok( $faixas_medidas > 0, 'ha faixa confortavel para medir o pronome', $faixas_medidas . ' faixa(s)' );
rbm_ok( empty( $pron_torto ), 'o pronome possessivo tambem vem do banco, e nao digitado',
	empty( $pron_torto ) ? 'todos' : implode( ', ', array_slice( $pron_torto, 0, 3 ) ) );

/* O MUNDO PRODUZIDO: os DOIS generos existem no banco desta ferramenta, entao
   aqui ele nao precisa ser forjado — precisa ser CONTADO, senao a afirmacao
   acima poderia ser verdadeira sobre um genero so. */
$generos_r2 = array();
foreach ( $dados['situacoes'] as $s ) {
	foreach ( (array) $s['limiares'] as $l ) {
		$generos_r2[ $l['artigo'] ] = true;
	}
}
rbm_ok( count( $generos_r2 ) > 1,
	'os limiares da R2 citam publicadores de artigos DIFERENTES — a regua acima nao mede um genero so',
	implode( ' + ', array_keys( $generos_r2 ) ) );

/* NA TELA, E NAO SO NO FATO: a frase da faixa confortavel termina em "a
   recomendacao <pronome> fica folgada". O fato certo com a frase digitada
   passaria em silencio — foi exatamente assim que este defeito viveu desde que a
   R2 nasceu, com o artigo ja vindo do dado e o pronome nao.

   O que se mede e o CORPO renderizado, e nas duas direcoes: o pronome declarado
   tem de aparecer, e nenhum dos outros tres pode aparecer. Sem a segunda metade,
   uma frase que escrevesse os dois passaria. */
$corpos_r2 = '';
foreach ( $html_por_estado as $h ) {
	$corpos_r2 .= ' ' . rbm_normalizar( strip_tags( $h ) );
}
$pronomes_certos = array();
foreach ( $dados['situacoes'] as $s ) {
	if ( ! empty( $s['faixa_confortavel'] ) ) {
		$pronomes_certos[ $formas_r2[ $artigo_r2[ $s['faixa_confortavel']['publicador'] ] ]['pronome_possessivo'] ] = true;
	}
}
$achou_certo = false;
foreach ( array_keys( $pronomes_certos ) as $p ) {
	if ( false !== strpos( $corpos_r2, 'recomendacao ' . $p . ' fica folgada' ) ) {
		$achou_certo = true;
	}
}
rbm_ok( $achou_certo, 'a frase da faixa servida usa o pronome DECLARADO de quem publica',
	implode( ' / ', array_keys( $pronomes_certos ) ) );

$pronome_errado = array();
foreach ( $formas_r2 as $chave => $forma ) {
	if ( ! is_array( $forma ) ) {
		continue; /* a linha "por_que" da tabela */
	}
	if ( isset( $pronomes_certos[ $forma['pronome_possessivo'] ] ) ) {
		continue;
	}
	if ( false !== strpos( $corpos_r2, 'recomendacao ' . $forma['pronome_possessivo'] . ' fica folgada' ) ) {
		$pronome_errado[] = $forma['pronome_possessivo'];
	}
}
rbm_ok( empty( $pronome_errado ), 'nenhum pronome que NAO e o declarado aparece na frase da faixa',
	empty( $pronome_errado ) ? 'nenhum' : implode( ', ', $pronome_errado ) );

/* E A SEGUNDA TABELA MORREU: nenhum arquivo de ferramenta volta a declarar
   artigo de publicador por conta propria. */
$cobertura_r2_fonte = file_get_contents( $raiz . '/ferramentas/cobertura-r2.py' );
rbm_ok( false === strpos( $cobertura_r2_fonte, 'ARTIGO_DO_PUBLICADOR = {' ),
	'cobertura-r2.py nao volta a ter tabela propria de artigo' );

/* ---------------------------------------------------------------------------
 * A FRASE QUE PROMETE DESACORDO TEM DE APRESENTAR DUAS FONTES — item 3 do
 * despacho da Sentinela de 14/09/2026, e o "pronto quando" dela pede esta régua
 * com todas as letras: "some uma régua que reprove qualquer situação cuja frase
 * diga 'divergem' e cite o mesmo publicador nos dois lados — hoje ela não
 * existe, e é por isso que isto ficou no ar desde 09/09".
 *
 * A régua não lê `ha_divergencia`: ela lê a FRASE SERVIDA e os limiares, porque
 * o defeito estava justamente em `ha_divergencia` dizer sim comparando números.
 * Conferir a frase contra a bandeira que a produziu seria as duas metades
 * errando juntas.
 * ------------------------------------------------------------------------- */
echo "\n12. Divergencia prometida e divergencia apresentada (despacho de 14/09)\n";

$prometem = $repetem = $sem_dois = array();
foreach ( $dados['situacoes'] as $chave => $sit ) {
	$frase = robometria_r2_frase_situacao( $sit );
	$publicadores = array();
	foreach ( (array) $sit['limiares'] as $l ) {
		$publicadores[ $l['publicador'] ] = 1;
	}

	if ( false !== strpos( $frase, 'divergem' ) ) {
		$prometem[] = $chave;
		/* Duas condicoes, e as duas tem de valer: a frase nomeia dois
		   publicadores DIFERENTES, e o banco daquela situacao tem dois. */
		if ( $sit['limiar_seguro']['publicador'] === $sit['limiar_minimo']['publicador'] ) {
			$repetem[] = $chave . ' (' . $sit['limiar_seguro']['publicador'] . ')';
		}
		if ( count( $publicadores ) < 2 ) {
			$sem_dois[] = $chave;
		}
	}
}
rbm_ok( empty( $repetem ),
	'nenhuma situacao promete divergencia citando o MESMO publicador dos dois lados',
	empty( $repetem ) ? count( $prometem ) . ' com divergencia, todas com dois nomes'
		: implode( ', ', $repetem ) );
rbm_ok( empty( $sem_dois ),
	'toda frase que diz "divergem" tem duas fontes no banco daquela situacao',
	empty( $sem_dois ) ? 'todas' : implode( ', ', $sem_dois ) );

/* A ORACAO DO LIMIAR DE BAIXO ENCAIXA NO MOLDE, em toda situacao. O defeito era
   "trata ate 1.500 Pa ja basta como o piso do consenso": a saida de
   escrever_limiar() entrando num molde que esperava um sintagma nominal. */
$quebradas = array();
foreach ( $dados['situacoes'] as $chave => $sit ) {
	$frase = robometria_r2_frase_situacao( $sit );
	if ( false !== strpos( $frase, 'já basta como o piso' )
		|| false !== strpos( $frase, 'Pa já basta como' ) ) {
		$quebradas[] = $chave;
	}
}
rbm_ok( empty( $quebradas ),
	'nenhuma oracao quebrada do tipo "trata ate X Pa ja basta como o piso"',
	empty( $quebradas ) ? 'nenhuma das ' . count( $dados['situacoes'] ) : implode( ', ', $quebradas ) );

/* E A CONTRACAO: "a de a Canaltech" estava no ar desde 09/09 em carpete|nao. */
$sem_contracao = array();
foreach ( $dados['situacoes'] as $chave => $sit ) {
	$frase = robometria_r2_frase_situacao( $sit );
	if ( preg_match( '/\bé a de (a|o|as|os) /u', $frase )
		|| false !== strpos( $frase, ' de a ' ) || false !== strpos( $frase, ' de o ' ) ) {
		$sem_contracao[] = $chave;
	}
}
rbm_ok( empty( $sem_contracao ),
	'nenhuma frase serve "de a" ou "de o" onde o portugues contrai',
	empty( $sem_contracao ) ? 'nenhuma' : implode( ', ', $sem_contracao ) );

/* UMA ENTRADA POR DOCUMENTO na linha de procedencia, e nao uma por limiar. */
$repetida = array();
foreach ( $dados['situacoes'] as $chave => $sit ) {
	$docs = $itens = array();
	foreach ( (array) $sit['limiares'] as $l ) {
		$itens[] = 1;
		$docs[ $l['url'] . '|' . $l['verificado_em'] ] = 1;
	}
	$h = rbm_r2_pagina( 200, $sit['piso'], $sit['pelo'] );
	if ( '' !== $h && preg_match( '#<p class="rbm-vitrine-fonte">(.*?)</p>#s', $h, $mf ) ) {
		/* Uma entrada por documento: os itens sao separados por &middot;, entao
		   o numero de entradas e o de separadores mais um. */
		$entradas = substr_count( $mf[1], '&middot;' ) + 1;
		if ( $entradas > count( $docs ) ) {
			$repetida[] = $chave . ' (' . $entradas . ' entradas para '
				. count( $docs ) . ' documento(s))';
		}
	}
}
rbm_ok( empty( $repetida ),
	'a linha de procedencia nao repete o mesmo documento',
	empty( $repetida ) ? 'nenhuma situacao repete' : implode( ', ', $repetida ) );

/* ------------------------------------------------------------------ RESUMO */

echo "\n";
printf( "%d medicoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

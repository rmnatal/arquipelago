<?php
/**
 * Verificacao MEDIDA da ferramenta R1, sem site e sem rede.
 *
 *   php ferramentas/teste-r1.php .
 *
 * E a secao 8 do ARQUIPELAGO.md executada onde da para executa-la nesta ilha: a
 * nuvem nao alcanca robometria.com.br a nao ser para o Sync e o /status, entao a
 * alternativa a este arquivo seria marcar publicar=true por fe.
 *
 * O QUE ELE MEDE QUE O teste-casca.php NAO MEDE, e e a razao de ele existir:
 * **cada frase que a R1 publica e comparada com a que a implementacao de
 * referencia escreve** (ferramentas/cobertura-r1.py, pelo gabarito
 * dados/r1-referencia.json), modelo a modelo, item a item, ignorando acento e
 * aplicando a mesma tabela de rotulos de origem. A especificacao exige que a
 * saida do PHP BATA com a da referencia; sem esta comparacao, "bate" seria uma
 * impressao.
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
		printf( "  ok   %-64s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-64s %s\n", $rotulo, $medida );
	return false;
}

/** So os blocos <script>, que e onde a contagem de &#038; vale (secao 8). */
function rbm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/** Comparar frase publicada com frase da referencia so faz sentido sem acento. */
function rbm_sem_acento( $t ) {
	$de   = array( 'á','à','â','ã','ä','é','ê','ë','í','î','ï','ó','ô','õ','ö','ú','û','ü','ç','Á','À','Â','Ã','É','Ê','Í','Ó','Ô','Õ','Ú','Ç' );
	$para = array( 'a','a','a','a','a','e','e','e','i','i','i','o','o','o','o','u','u','u','c','A','A','A','A','E','E','I','O','O','O','U','C' );
	return str_replace( $de, $para, $t );
}

/* ---------------------------------------------------------------------------
 * Montagem: os dados vem do repositorio, e a pagina "existe" para o teste.
 * ------------------------------------------------------------------------- */

$dados     = json_decode( file_get_contents( $raiz . '/dados/r1-respostas.json' ), true );
$gabarito  = json_decode( file_get_contents( $raiz . '/dados/r1-referencia.json' ), true );
$modelos_b = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$pecas_b   = json_decode( file_get_contents( $raiz . '/dados/pecas.json' ), true );

$GLOBALS['__paginas'] = array(
	'ferramentas'                          => true,
	'metodologia'                          => true,
	'sobre'                                => true,
	'divulgacao-de-afiliados'              => true,
	'qual-peca-serve-no-meu-robo-aspirador' => true,
);
$GLOBALS['__entrada_r1'] = array( 'modelo' => null, 'peca' => null );

robometria_teste_carregar( $raiz );

/* O Sync grava dados/r1-respostas.json na option; aqui o filtro faz o mesmo
   papel, para o teste medir exatamente o arquivo commitado. */
add_filter( 'robometria_r1_dados', function ( $d ) use ( $dados ) {
	return $dados;
} );
add_filter( 'robometria_r1_na_pagina', function () {
	return true;
} );
add_filter( 'robometria_r1_entrada', function ( $e ) {
	return $GLOBALS['__entrada_r1'];
} );

/** Monta a pagina da R1 com uma consulta. */
function rbm_r1_pagina( $modelo = null, $peca = null ) {
	$GLOBALS['__entrada_r1'] = array( 'modelo' => $modelo, 'peca' => $peca );
	robometria_teste_rebobinar();
	return robometria_teste_pagina( 'robometria_r1' );
}

echo "Robometria — verificacao da ferramenta R1 " . ROBOMETRIA_R1_VERSAO . "\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria: script dentro do
 *    retorno do shortcode. Medido em varios estados da pagina, nao so em um.
 * ------------------------------------------------------------------------- */

echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";

$estados = array(
	'sem consulta'          => array( null, null ),
	'modelo que responde'   => array( $dados['ancora'], null ),
	'modelo + tipo'         => array( $dados['ancora'], $dados['tipos'][0] ),
	'modelo de entrada vazia' => array( $dados['entrada_vazia'][0], null ),
	'modelo inexistente'    => array( 'nao-existe-no-banco', 'tipo-que-nao-existe' ),
);

$html_por_estado = array();
foreach ( $estados as $nome => $par ) {
	$html_por_estado[ $nome ] = rbm_r1_pagina( $par[0], $par[1] );
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
 * 3. A COMPARACAO COM A IMPLEMENTACAO DE REFERENCIA.
 *
 * Este e o bloco que justifica o arquivo. Cada frase do PHP contra a frase da
 * referencia, sem acento e com o rotulo de origem aplicado dos dois lados.
 * ------------------------------------------------------------------------- */

echo "\n3. Cada frase do PHP x a frase da implementacao de referencia\n";

/** A frase da referencia, com o apelido de origem trocado pelo rotulo de tela. */
function rbm_normalizar_referencia( $frase, $rotulos ) {
	foreach ( $rotulos as $slug => $t ) {
		$frase = str_replace( '(' . $slug . ',', '(' . $t['rotulo'] . ',', $frase );
	}
	return rbm_sem_acento( $frase );
}

$comparadas = 0;
$divergentes = array();

foreach ( $gabarito['respostas'] as $mid => $esperado ) {
	$obtido = $dados['respostas'][ $mid ];

	foreach ( array( 'fabricante', 'terceiro' ) as $grupo ) {
		foreach ( $esperado[ $grupo ] as $k => $ref ) {
			$item = $obtido[ $grupo ][ $k ];
			$php  = rbm_sem_acento( robometria_r1_frase( $item ) );
			$gab  = rbm_normalizar_referencia( $ref['frase'], $dados['rotulos_de_origem'] );
			$comparadas++;
			if ( $php !== $gab ) {
				$divergentes[] = "$mid/$grupo/$k\n      referencia: $gab\n      php ......: $php";
			}
		}
	}

	foreach ( $esperado['kits_sem_composicao'] as $k => $ref ) {
		$php = rbm_sem_acento( robometria_r1_frase_kit( $obtido['kits_sem_composicao'][ $k ] ) );
		$gab = rbm_normalizar_referencia( $ref['frase'], $dados['rotulos_de_origem'] );
		$comparadas++;
		if ( $php !== $gab ) {
			$divergentes[] = "$mid/kit/$k\n      referencia: $gab\n      php ......: $php";
		}
	}

	foreach ( $esperado['recusa_por_tipo'] as $tipo => $ref ) {
		$php = rbm_sem_acento( robometria_r1_frase_recusa( $tipo ) );
		$comparadas++;
		if ( $php !== rbm_sem_acento( $ref ) ) {
			$divergentes[] = "$mid/recusa/$tipo\n      referencia: $ref\n      php ......: $php";
		}
	}

	if ( ! empty( $esperado['aviso_de_variante'] ) ) {
		$php = rbm_sem_acento( robometria_r1_frase_variante( $obtido['aviso_de_variante'] ) );
		$comparadas++;
		if ( $php !== rbm_sem_acento( $esperado['aviso_de_variante'] ) ) {
			$divergentes[] = "$mid/variante\n      referencia: {$esperado['aviso_de_variante']}\n      php ......: $php";
		}
	}
}

rbm_ok( empty( $divergentes ), 'toda frase do PHP bate com a da referencia', "comparadas: $comparadas" );
foreach ( $divergentes as $d ) {
	echo "       . $d\n";
}
rbm_ok( $comparadas >= 100, 'a comparacao cobriu o banco inteiro, nao uma amostra', "$comparadas frases" );

/* ---------------------------------------------------------------------------
 * 4. A resposta esta no HTML SERVIDO, sem depender de JavaScript (secao 5).
 * ------------------------------------------------------------------------- */

echo "\n4. Resposta no HTML servido, sem JavaScript (secao 5 e 14.5)\n";

$sem_consulta = $html_por_estado['sem consulta'];
$ancora       = $dados['ancora'];
$itens_ancora = $dados['respostas'][ $ancora ]['fabricante'];

rbm_ok( '' !== $ancora && ! empty( $itens_ancora ), 'existe modelo-ancora e ele responde alguma peca', $ancora );
rbm_ok( 'positivo-pra500' !== $ancora, 'a ancora NAO e o PRA500, em que a R1 sai vazia', $ancora );

$frase_ancora = robometria_r1_frase( $itens_ancora[0] );
rbm_ok(
	false !== strpos( $sem_consulta, htmlspecialchars( $frase_ancora, ENT_QUOTES ) ),
	'a resposta-ancora inteira sai no HTML sem ninguem clicar em nada'
);

/* A tabela pre-renderizada e o corpo da pagina para um modelo de linguagem. */
preg_match( '#<table class="rbm-quadro">.*?</table>#is', $sem_consulta, $mt );
$linhas_tabela = isset( $mt[0] ) ? substr_count( $mt[0], '<tr>' ) - 1 : 0;
rbm_ok(
	$linhas_tabela === count( $dados['exemplos'] ),
	'a tabela de exemplos serve TODAS as linhas do banco',
	"$linhas_tabela de " . count( $dados['exemplos'] )
);
rbm_ok( count( $dados['exemplos'] ) >= 8, 'a tabela cumpre o minimo de 8 linhas da secao 1.7', count( $dados['exemplos'] ) . ' linhas' );

/* Recusa: a pagina diz que nao sabe, com todas as letras (secao 1.3).
   A contagem e feita DENTRO do <main>: o nome da classe rbm-frase tambem
   aparece na folha de estilo do cabecalho, e contar na pagina inteira seria o
   mesmo erro de metodo que contar &#038; fora dos blocos <script>. */
$vazio = $html_por_estado['modelo de entrada vazia'];
preg_match( '#<main[^>]*>(.*?)</main>#is', $vazio, $mv0 );
$corpo_vazio = isset( $mv0[1] ) ? $mv0[1] : '';
rbm_ok(
	false !== strpos( $corpo_vazio, 'não vamos supor' ),
	'modelo sem declaracao recebe a recusa explicita, nao um vazio'
);
rbm_ok(
	0 === substr_count( $corpo_vazio, 'class="rbm-frase"' ),
	'modelo sem declaracao nao recebe nenhuma frase de compatibilidade',
	substr_count( $corpo_vazio, 'class="rbm-frase"' ) . ' frase(s)'
);
rbm_ok(
	0 === substr_count( $corpo_vazio, 'rbm-vitrine-item' ),
	'modelo sem declaracao nao recebe vitrine — bloco vazio nao lista (secao 7)'
);

/* ---------------------------------------------------------------------------
 * 5. O formulario: lista fechada, e o seletor gerado da varredura (secao 1.2).
 * ------------------------------------------------------------------------- */

echo "\n5. Formulario (secao 1.2 da especificacao e secao 6 do contrato)\n";

preg_match( '#<form class="rbm-form"[^>]*>(.*?)</form>#is', $sem_consulta, $mf );
$form = isset( $mf[1] ) ? $mf[1] : '';
rbm_ok( '' !== $form, 'o formulario existe no HTML servido' );
rbm_ok( false !== strpos( $mf[0], 'method="get"' ), 'o formulario e GET: a consulta vira endereco, e a resposta vem do servidor' );
rbm_ok( 0 === substr_count( $form, '<input type="text"' ) && 0 === substr_count( $form, 'type="search"' ),
	'nenhum campo de texto livre — modelo e lista fechada (secao 1.2)' );

$opcoes_modelo = substr_count( $form, '<option value="' ) - count( $dados['tipos'] ) - 2; // 2 opcoes vazias
rbm_ok( $opcoes_modelo === count( $dados['modelos'] ),
	'o seletor de modelo oferece exatamente os modelos publicaveis do banco',
	"$opcoes_modelo de " . count( $dados['modelos'] ) );

foreach ( (array) $dados['tipos_sem_nenhuma_peca_no_banco'] as $t ) {
	rbm_ok( false === strpos( $form, 'value="' . $t . '"' ),
		"o tipo '$t' NAO esta no seletor (zero pecas no banco inteiro)" );
}
foreach ( (array) $dados['tipos'] as $t ) {
	rbm_ok( false !== strpos( $form, 'value="' . $t . '"' ), "o tipo '$t' esta no seletor" );
}

rbm_ok( false !== strpos( $sem_consulta, 'class="rbm-promessa"' ), 'promessa antes do formulario (secao 6)' );

/* ---------------------------------------------------------------------------
 * 6. Ordem da secao 7: terceiro nunca antes, nunca misturado.
 * ------------------------------------------------------------------------- */

echo "\n6. Ordem da resposta (secao 7 do contrato)\n";

$tem_terceiro = false;
foreach ( $dados['respostas'] as $mid => $r ) {
	if ( ! empty( $r['terceiro'] ) && ! empty( $r['fabricante'] ) ) {
		$tem_terceiro = true;
		$h = rbm_r1_pagina( $mid, null );
		rbm_ok(
			strpos( $h, 'rbm-terceiro' ) > strpos( $h, 'rbm-frase' ),
			"[$mid] declaracao de terceiro vem DEPOIS da do fabricante"
		);
	}
}
if ( ! $tem_terceiro ) {
	rbm_ok( true, 'nenhum par com selo declarada_terceiro no banco hoje', 'nada a ordenar' );
}

/* Nao ha item com link de afiliado nesta ilha ainda, e a pagina precisa dizer
   isso em vez de fingir um botao de compra (secao 7). */
$esperando = 0;
foreach ( $dados['respostas'] as $r ) {
	foreach ( $r['fabricante'] as $i ) {
		if ( ! empty( $i['esperando_link'] ) ) { $esperando++; }
	}
}
$h_ancora = rbm_r1_pagina( $ancora, null );
rbm_ok( $esperando > 0 && false !== strpos( $h_ancora, 'rbm-vitrine-sem-loja' ),
	'peca sem link de loja diz que nao tem link, em vez de mostrar botao' );

/* ---------------------------------------------------------------------------
 * 7. A vitrine (Bloco 4e, secao 6).
 * ------------------------------------------------------------------------- */

echo "\n7. Vitrine dentro do resultado (secao 6)\n";

preg_match( '#<ul class="rbm-vitrine">(.*?)</ul>#is', $h_ancora, $mv );
$vitrine = isset( $mv[1] ) ? $mv[1] : '';
rbm_ok( '' !== $vitrine, 'a vitrine aparece dentro do resultado' );
rbm_ok( 0 === substr_count( $vitrine, 'onclick' ), 'nenhum cartao com onclick — sao <a href> de verdade' );
rbm_ok( substr_count( $vitrine, '<a href="http' ) > 0, 'os cartoes levam ao endereco da declaracao', substr_count( $vitrine, '<a href="http' ) . ' link(s)' );

$pecas_distintas = array();
foreach ( $dados['respostas'][ $ancora ]['fabricante'] as $i ) {
	$pecas_distintas[ $i['peca'] ] = true;
}
rbm_ok( substr_count( $vitrine, 'rbm-vitrine-item' ) === count( $pecas_distintas ),
	'um cartao por PECA, nao por par peca x tipo',
	substr_count( $vitrine, 'rbm-vitrine-item' ) . ' de ' . count( $pecas_distintas ) );
rbm_ok( substr_count( $vitrine, 'rbm-vitrine-vazia' ) === count( $pecas_distintas ),
	'peca sem imagem entra com espaco reservado neutro, e nao some (secao 6)' );

/* ---------------------------------------------------------------------------
 * 8. JSON-LD, canonica e noindex (secoes 5.3 e 14.1).
 * ------------------------------------------------------------------------- */

echo "\n8. JSON-LD, canonica e orcamento de rastreamento\n";

preg_match( '#<script type="application/ld\+json" id="robometria-r1-jsonld">(.*?)</script>#is', $sem_consulta, $mj );
$ld = json_decode( isset( $mj[1] ) ? $mj[1] : '', true );
$tipos_ld = array();
if ( is_array( $ld ) && isset( $ld['@graph'] ) ) {
	foreach ( $ld['@graph'] as $no ) { $tipos_ld[] = $no['@type']; }
}
rbm_ok( in_array( 'WebApplication', $tipos_ld, true ), 'JSON-LD decodifica e traz WebApplication (secao 1.9)', implode( '+', $tipos_ld ) );
rbm_ok( in_array( 'FAQPage', $tipos_ld, true ), 'JSON-LD traz FAQPage (secao 1.9)' );

/* Pergunta de FAQ que a pagina nao responde e marcacao que promete o que nao
   existe. Cada resposta do FAQ tem que ser uma frase servida no HTML. */
$fora_da_pagina = 0;
foreach ( $ld['@graph'] as $no ) {
	if ( 'FAQPage' !== $no['@type'] ) { continue; }
	foreach ( $no['mainEntity'] as $q ) {
		$texto = $q['acceptedAnswer']['text'];
		$modelo_da_pergunta = null;
		foreach ( $dados['exemplos'] as $l ) {
			if ( false !== strpos( $q['name'], $l['modelo_rotulo'] ) ) {
				$modelo_da_pergunta = $l['modelo'];
				break;
			}
		}
		$h = rbm_r1_pagina( $modelo_da_pergunta, null );
		if ( false === strpos( $h, htmlspecialchars( $texto, ENT_QUOTES ) ) ) {
			$fora_da_pagina++;
		}
	}
	rbm_ok( 0 === $fora_da_pagina, 'toda resposta do FAQPage e uma frase que a pagina serve mesmo',
		count( $no['mainEntity'] ) . ' pergunta(s)' );
}

$com_consulta = $html_por_estado['modelo que responde'];
rbm_ok( false !== strpos( $com_consulta, '<meta name="robots" content="noindex,follow">' ),
	'endereco com consulta sai com noindex (secao 14.1: orcamento de rastreamento)' );
rbm_ok( false !== strpos( $com_consulta, 'rel="canonical"' ),
	'endereco com consulta aponta a canonica para a pagina limpa' );
rbm_ok( false === strpos( $sem_consulta, 'noindex' ),
	'a pagina limpa NAO leva noindex — e ela que tem que indexar' );

/* ---------------------------------------------------------------------------
 * 9. Identidade da ilha (secao 6 e PROMPT.md).
 * ------------------------------------------------------------------------- */

echo "\n9. Identidade: paleta, gradiente e cor de sinal\n";

preg_match( '#<style id="robometria-r1">(.*?)</style>#is', $sem_consulta, $ms );
$css = isset( $ms[1] ) ? $ms[1] : '';
rbm_ok( '' !== $css, 'CSS da R1 servido no wp_head, fora do shortcode' );
rbm_ok( false === stripos( $css, 'gradient' ), 'nenhum gradiente no CSS da R1' );

$paleta = array( '#16191D', '#CC3311', '#F2F1EF', '#FFFFFF', '#DFDCD6', '#6B6862', '#A26A00' );
preg_match_all( '/#[0-9A-Fa-f]{6}\b/', $css, $mh );
$fora = array_values( array_unique( array_diff( array_map( 'strtoupper', $mh[0] ), $paleta ) ) );
rbm_ok( empty( $fora ), 'nenhuma cor fora da paleta da ilha no CSS da R1',
	empty( $fora ) ? count( $mh[0] ) . ' hex' : implode( ' ', $fora ) );

/* A ferramenta nao pode ter paleta propria: toda cor dela sai das variaveis da
   casca, para a identidade continuar tendo um dono so. */
rbm_ok( substr_count( $css, 'var(--rbm-' ) > 10, 'a R1 usa as variaveis de cor da casca, e nao cor propria',
	substr_count( $css, 'var(--rbm-' ) . ' usos de var()' );

/* Sombra colorida e proibida (secao 6). A unica sombra desta folha e a da barra
   do celular, e ela tem que ser da propria tinta (22,25,29 = #16191D). */
preg_match_all( '/rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/', $css, $mr, PREG_SET_ORDER );
$sombra_colorida = 0;
foreach ( $mr as $c ) {
	if ( array( '22', '25', '29' ) !== array( $c[1], $c[2], $c[3] ) ) { $sombra_colorida++; }
}
rbm_ok( 0 === $sombra_colorida, 'nenhuma sombra colorida — so a neutra da tinta da ilha',
	count( $mr ) . ' rgba, ' . $sombra_colorida . ' fora da tinta' );

preg_match( '#<main[^>]*>(.*?)</main>#is', $sem_consulta, $mm );
$corpo = isset( $mm[1] ) ? $mm[1] : '';
rbm_ok( 0 === substr_count( strtoupper( $corpo ), '#CC3311' ),
	'a varredura nao aparece no corpo (cor de sinal, um uso por tela)' );
rbm_ok( 0 !== strpos( trim( $corpo ), '---' ) && 0 !== strpos( trim( $corpo ), 'ilha:' ),
	'corpo nao comeca por metadado YAML (secao 8, item 3)' );

/* ---------------------------------------------------------------------------
 * 10. Os numeros da tela batem com o banco commitado (secao 10).
 * ------------------------------------------------------------------------- */

echo "\n10. Numeros da tela x banco commitado (secao 10: nunca invente dado)\n";

$esperado_num = array(
	'pares_declarados'      => (int) $pecas_b['contagem']['pares_peca_x_modelo_declarados'],
	'modelos_publicaveis'   => (int) $modelos_b['contagem']['publicavel'],
	'pecas_publicaveis'     => (int) $pecas_b['contagem']['publicavel'],
);
foreach ( $esperado_num as $chave => $valor ) {
	rbm_ok( (int) $dados['resumo'][ $chave ] === $valor,
		"resumo.$chave bate com o banco", $dados['resumo'][ $chave ] . ' x ' . $valor );
}

$modelos_do_banco = array();
foreach ( $modelos_b['registros'] as $m ) {
	if ( 'publicavel' === $m['status'] ) { $modelos_do_banco[ $m['id'] ] = true; }
}
$intrusos = 0;
foreach ( $dados['modelos'] as $m ) {
	if ( empty( $modelos_do_banco[ $m['id'] ] ) ) { $intrusos++; }
}
rbm_ok( 0 === $intrusos, 'nenhum modelo do seletor esta fora do banco publicavel', "intrusos: $intrusos" );

rbm_ok(
	false !== strpos( $sem_consulta, '>' . number_format_i18n( $esperado_num['pares_declarados'] ) . '<' ),
	'o numero de pares declarados na tela e o do banco',
	$esperado_num['pares_declarados']
);

/* ---------------------------------------------------------------------------
 * 11. Interlinkagem e cartao do hub.
 * ------------------------------------------------------------------------- */

echo "\n11. Interlinkagem (secao 3 da especificacao, secao 9 do contrato)\n";

rbm_ok( false !== strpos( $sem_consulta, 'metodologia' ), 'a R1 aponta para a metodologia' );
rbm_ok( false !== strpos( $sem_consulta, 'divulgacao-de-afiliados' ) || false !== strpos( $sem_consulta, 'Divulgação de afiliados' ),
	'a R1 aponta para a divulgacao de afiliados' );

/* A R2 ainda nao existe publicada: o auxiliar da casca tem que servir texto, e
   nunca um <a> para um 404. */
rbm_ok( false === strpos( $sem_consulta, 'href="https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/"' ),
	'nenhum link para a R2 enquanto a pagina dela nao existe (sem 404 no ar)' );

$ferramentas = apply_filters( 'robometria_ferramentas', robometria_casca_ferramentas() );
$estado_r1 = '';
foreach ( $ferramentas as $f ) {
	if ( 'R1' === $f['codigo'] ) { $estado_r1 = $f['estado'] . '|' . $f['slug']; }
}
rbm_ok( 'publicada|' . ROBOMETRIA_R1_SLUG === $estado_r1,
	'a R1 se registra como publicada no hub da casca', $estado_r1 );

/* ---------------------------------------------------------------------------
 * 12. Higiene do snippet (secao 8, fase 4b do playbook).
 * ------------------------------------------------------------------------- */

echo "\n12. Higiene do snippet (secao 8, fase 4b)\n";

$fonte = file_get_contents( $raiz . '/snippets/robometria-r1.php' );
rbm_ok( 0 === strpos( $fonte, '/**' ), 'o snippet comeca com /** e sem <?php no topo' );

/* A superglobal de servidor e casada pelo ModSecurity desta hospedagem ATE
   DENTRO DE COMENTARIO, e a gravacao do snippet falharia em silencio no
   wp-admin. Foi assim que o teste da casca rendeu na primeira rodada. */
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
rbm_ok( false !== strpos( $corpo, 'compatível' ) || false !== strpos( $corpo, 'não localizamos' ),
	'o texto da tela sai acentuado, e nao no ASCII do banco' );

/* ---------------------------------------------------------------------------
 * Fecho
 * ------------------------------------------------------------------------- */

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d falha(s) em %d medicoes.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d medicoes, nenhuma falha.\n", $feitos );
exit( 0 );

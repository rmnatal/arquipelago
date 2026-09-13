<?php
/**
 * Verificacao MEDIDA da F2 — "Qual cola usar no mosaico, e qual rejunte".
 *
 *   php ferramentas/teste-f2.php .
 *
 * O que este arquivo tem que os outros nao tem, e por que:
 *
 *   1. ELE VARRE A ENTRADA INTEIRA, nao o caso-ancora. A F2 e ferramenta de
 *      entrada variavel: ela serve uma pagina por consulta, e a pagina sem
 *      consulta e so UM dos 45 estados de cola e dos 50 de rejunte. A
 *      Robometria pagou essa licao em 11/09/2026 com cinco testes verdes que
 *      nao viam portugues errado porque ele so aparecia quando alguem escolhia
 *      um modelo especifico. Aqui a afirmacao e sobre a SOMA das respostas.
 *
 *   2. A REGUA E PROPRIA, e ela NAO chama o snippet. O esperado de cada celula
 *      vem de `matriz_esperada_da_F2` e `matriz_esperada_do_rejunte` do
 *      esquema, escritos A MAO no bloco 3 a partir das declaracoes, antes de
 *      existir uma linha do snippet. Se as duas metades errarem, elas nao
 *      erram juntas.
 *
 *   3. ELE MEDE NO CORPO SERVIDO, nunca no HTML completo nem no retorno do
 *      shortcode. Afirmacao sobre o que a pagina DIZ se conta dentro de <main>.
 *
 *   4. UM PROCESSO POR ESTADO. A casca tem `static` legitimos (rodape, marca,
 *      trilha) que so valem dentro de uma requisicao; varredura que monta
 *      muitos estados no mesmo processo mede o segundo pela metade.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$rapido = in_array( '--rapido', $argv, true );

$falhas = 0;
$feitos = 0;

function f2_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-70s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-70s %s\n", $rotulo, $medida );
	return false;
}

function f2_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function f2_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

function f2_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/** Um estado da ferramenta, servido por um processo so dele. */
function f2_render( $raiz, $consulta = '' ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( 'cdm_f2' ) . ' ' . escapeshellarg( 'hoje' )
		. ' ' . escapeshellarg( $consulta ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/* ---------------------------------------------------------------------------
 * A REGUA, lida do repositorio e nunca do snippet.
 * ------------------------------------------------------------------------- */

$esquema  = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$colas    = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$rejuntes = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-rejuntes.json' ), true );

if ( ! $esquema || ! $colas || ! $rejuntes ) {
	echo "ERRO: nao consegui ler o esquema ou o banco.\n";
	exit( 1 );
}

$por_id = array();
foreach ( array_merge( $colas['materiais'], $rejuntes['materiais'] ) as $m ) {
	$por_id[ $m['id'] ] = $m;
}

/** O nome como a TELA o escreve, recalculado aqui: marca so quando falta. */
function f2_nome_esperado( $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return $nome;
	}

	return $marca . ' ' . $nome;
}

echo "Clube do Mosaico — verificacao da F2 " . ( defined( 'CDM_F2_VERSAO' ) ? CDM_F2_VERSAO : '?' ) . "\n";

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "  (F2 " . CDM_F2_VERSAO . ", casca " . CDM_CASCA_VERSAO . ")\n\n";

/* ---------------------------------------------------------------------------
 * 1. A pagina existe na arvore, com mae, e com UM nome so
 * ------------------------------------------------------------------------- */

echo "1. A pagina na arvore (secao 16 do contrato)\n";

$defs = cdm_casca_definicao_paginas();
f2_ok( isset( $defs[ CDM_F2_SLUG ] ), 'a F2 registrou a propria pagina pelo filtro cdm_paginas', CDM_F2_SLUG );
f2_ok( isset( $defs[ CDM_F2_SLUG ]['pai'] ) && 'materiais' === $defs[ CDM_F2_SLUG ]['pai'],
	'a pagina nasce com mae, e a mae e /materiais/' );
f2_ok( isset( $defs['materiais'] ), 'a mae existe na definicao de paginas' );

/* UM NOME POR PAGINA, em toda superficie. A Aquametria pagou por oito paginas
   em que o degrau da trilha e o H1 diziam nomes diferentes a uma linha de
   distancia. Aqui as quatro superficies sao conferidas contra a MESMA
   constante, e o teste le cada uma de onde ela realmente sai. */
$arvore = cdm_casca_arvore();
f2_ok( isset( $arvore[ CDM_F2_SLUG ] ), 'a pagina esta no mapa da arvore' );
f2_ok( isset( $arvore[ CDM_F2_SLUG ]['rotulo'] ) && CDM_F2_TITULO === $arvore[ CDM_F2_SLUG ]['rotulo'],
	'o degrau da trilha usa o mesmo nome', isset( $arvore[ CDM_F2_SLUG ] ) ? $arvore[ CDM_F2_SLUG ]['rotulo'] : '' );
f2_ok( CDM_F2_TITULO === $defs[ CDM_F2_SLUG ]['titulo'], 'o titulo da pagina usa o mesmo nome' );
$no_cartao = '';
foreach ( cdm_casca_ferramentas() as $f ) {
	if ( 'F2' === $f['codigo'] ) {
		$no_cartao = $f['titulo'];
		f2_ok( 'publicada' === $f['estado'], 'a F2 se declara publicada no registro de ferramentas' );
		f2_ok( CDM_F2_SLUG === $f['slug'], 'o registro aponta para o endereco de nivel 3', $f['slug'] );
	}
}
f2_ok( CDM_F2_TITULO === $no_cartao, 'o cartao da home e do Guia usa o mesmo nome' );

/* O <title> do tema e "<titulo> – <nome do site>". 65 e o teto que a Aquametria
   passou a cobrar em 11/09/2026 depois de servir um de 128 caracteres. */
$titulo_completo = CDM_F2_TITULO . ' – Clube do Mosaico';
f2_ok( mb_strlen( $titulo_completo ) <= 65, 'o <title> cabe em 65 caracteres',
	mb_strlen( $titulo_completo ) . ' caracteres' );

/* ---------------------------------------------------------------------------
 * 2. A pagina-ancora: o que existe quando ninguem preenche nada
 * ------------------------------------------------------------------------- */

echo "\n2. A pagina-ancora (secao 5: o que um modelo de linguagem le)\n";

$ancora = f2_render( $raiz );
f2_ok( '' !== $ancora, 'a ancora foi servida', strlen( $ancora ) . ' bytes' );
$corpo_ancora = f2_corpo( $ancora );
$texto_ancora = f2_texto( $corpo_ancora );

/* Pagina fina nao entra no indice de dominio novo (secao 8). */
f2_ok( mb_strlen( $texto_ancora ) >= 1500, 'o corpo tem tamanho de pagina de verdade',
	mb_strlen( $texto_ancora ) . ' caracteres' );

cdm_teste_rebobinar();
cdm_teste_pagina( 'cdm_f2' );
$cru = $GLOBALS['__retorno_shortcode'];
f2_ok( false === stripos( $cru, '<script' ), 'sem <script> no retorno do shortcode (cicatriz de 08/09/2026)' );
f2_ok( false === stripos( $cru, '<style' ), 'sem <style> no retorno do shortcode' );
f2_ok( 0 === substr_count( f2_scripts( $ancora ), '&#038;' ), 'zero &#038; DENTRO de <script>',
	substr_count( f2_scripts( $ancora ), '&#038;' ) . ' achados' );
f2_ok( 0 !== strncmp( ltrim( $texto_ancora ), '---', 3 ), 'o corpo nao comeca por metadado' );

/* A folha e o script vem do rodape, nao da cabeca nem do corpo. */
$pos_corpo  = mb_strpos( $ancora, '<main' );
$pos_css    = mb_strpos( $ancora, 'id="cdm-f2-css"' );
$pos_js     = mb_strpos( $ancora, 'id="cdm-f2-js"' );
f2_ok( false !== $pos_css && $pos_css > $pos_corpo, 'a folha da F2 sai depois do corpo (wp_footer)' );
f2_ok( false !== $pos_js && $pos_js > $pos_corpo, 'o script da F2 sai depois do corpo (wp_footer)' );

/* A tabela pre-renderizada: as 18 + 9 linhas, no HTML servido. */
$linhas_tabela = preg_match_all( '#<table class="cdm-f2-tabela">.*?</table>#is', $corpo_ancora, $mt );
f2_ok( 2 === $linhas_tabela, 'as duas tabelas pre-renderizadas estao no HTML servido', $linhas_tabela . ' tabelas' );
$esperadas_cola    = count( $esquema['matriz_esperada_da_F2']['celulas'] );
$esperadas_rejunte = count( $esquema['matriz_esperada_do_rejunte']['celulas'] );
if ( 2 === $linhas_tabela ) {
	$n1 = preg_match_all( '#<tr>#', $mt[0][0] ) - 1; // o <tr> do cabecalho
	$n2 = preg_match_all( '#<tr>#', $mt[0][1] ) - 1;
	f2_ok( $n1 === $esperadas_cola, 'a tabela de cola serve as ' . $esperadas_cola . ' celulas conferidas', $n1 . ' linhas' );
	f2_ok( $n2 === $esperadas_rejunte, 'a tabela de rejunte serve as ' . $esperadas_rejunte . ' celulas conferidas', $n2 . ' linhas' );
}

/* Trilha e mae: a 16.4(b) cobra a mae no breadcrumb E numa frase do corpo. */
f2_ok( (bool) preg_match( '#<nav class="cdm-trilha".*?>Materiais<#is', $corpo_ancora ),
	'a trilha mostra a mae com endereco de verdade' );
$sem_trilha = preg_replace( '#<nav class="cdm-trilha".*?</nav>#is', '', $corpo_ancora );
f2_ok( false !== strpos( $sem_trilha, 'href="https://clubedomosaico.com.br/materiais/"' ),
	'o corpo tem uma frase que linka a mae (16.4b)' );

/* ---------------------------------------------------------------------------
 * 3. Cabeca: description, canonical e o robo do estado com parametro
 * ------------------------------------------------------------------------- */

echo "\n3. Cabeca da pagina (secoes 14.1 e 14.4)\n";

preg_match( '#<meta name="description" content="([^"]*)"#', $ancora, $md );
$desc = isset( $md[1] ) ? html_entity_decode( $md[1], ENT_QUOTES, 'UTF-8' ) : '';
f2_ok( '' !== $desc, 'a pagina serve meta description' );
f2_ok( mb_strlen( $desc ) >= 120 && mb_strlen( $desc ) <= 200, 'a description cabe na faixa util',
	mb_strlen( $desc ) . ' caracteres' );
/* UM canonical, e ele aponta para o endereco limpo. O "um" nao e zelo: quem
   imprime o proprio canonical por cima do `rel_canonical()` do nucleo serve
   dois, e a bancada so consegue ver isso porque passou a servir o do nucleo
   tambem (render-para-teste.php). */
f2_ok( 1 === substr_count( $ancora, '<link rel="canonical"' ), 'a ancora serve UM canonical',
	substr_count( $ancora, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $ancora, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'canonical aponta para o endereco limpo' );
f2_ok( false === strpos( $ancora, 'name="robots"' ), 'a ancora NAO sai com noindex' );

$com_parametro = f2_render( $raiz, 'base=espelho&onde=externo_exposto&junta=3' );
f2_ok( false !== strpos( $com_parametro, '<meta name="robots" content="noindex, follow">' ),
	'o estado com parametro sai com noindex, follow' );
f2_ok( 1 === substr_count( $com_parametro, '<link rel="canonical"' ), 'o estado com parametro serve UM canonical',
	substr_count( $com_parametro, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $com_parametro, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'o estado com parametro aponta o canonical para a ancora' );

/* JSON-LD: WebApplication + FAQPage, e o FAQ do schema tem que ser o mesmo que
   a pagina MOSTRA. Schema que promete o que a pagina nao diz e schema ignorado
   na melhor das hipoteses. */
preg_match( '#<script type="application/ld\+json" id="cdm-f2-jsonld">(.*?)</script>#s', $ancora, $mj );
$jsonld = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;
f2_ok( is_array( $jsonld ), 'o JSON-LD da F2 e JSON valido' );
$tipos = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	$tipos[] = $no['@type'];
}
f2_ok( in_array( 'WebApplication', $tipos, true ), 'JSON-LD tem WebApplication (secao 5.3)' );
f2_ok( in_array( 'FAQPage', $tipos, true ), 'JSON-LD tem FAQPage' );
f2_ok( false !== strpos( $ancora, 'id="cdm-trilha-jsonld"' ), 'JSON-LD tem BreadcrumbList (16.3)' );

$perguntas_schema = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		foreach ( $no['mainEntity'] as $q ) {
			$perguntas_schema[] = $q['name'];
		}
	}
}
$fora_da_tela = array();
foreach ( $perguntas_schema as $p ) {
	if ( false === mb_strpos( f2_texto( $corpo_ancora ), $p ) ) {
		$fora_da_tela[] = $p;
	}
}
f2_ok( count( $perguntas_schema ) >= 4, 'o FAQPage tem perguntas', count( $perguntas_schema ) . ' perguntas' );
f2_ok( empty( $fora_da_tela ), 'toda pergunta do schema esta escrita na tela',
	empty( $fora_da_tela ) ? 'as ' . count( $perguntas_schema ) : implode( ' | ', $fora_da_tela ) );

/* ---------------------------------------------------------------------------
 * 4. A VARREDURA DA COLA — 45 estados, um processo cada
 * ------------------------------------------------------------------------- */

echo "\n4. A entrada inteira da cola: " . count( $esquema['vocabularios']['base'] ) . " bases x "
	. count( $esquema['vocabularios']['ambiente'] ) . " ambientes\n";

$bases     = $esquema['vocabularios']['base'];
$ambientes = $esquema['vocabularios']['ambiente'];

/* Os rotulos existem para TODA entrada do vocabulario, e nao existe rotulo sem
   entrada. As duas direcoes, porque vocabulario novo sem rotulo sairia na tela
   como chave crua e rotulo orfao e codigo morto que finge cobertura. */
$rot = cdm_f2_rotulos();
$sem_rotulo = array_diff( $bases, array_keys( $rot['base'] ) );
$rotulo_orfao = array_diff( array_keys( $rot['base'] ), $bases );
f2_ok( empty( $sem_rotulo ), 'toda base do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo ) );
f2_ok( empty( $rotulo_orfao ), 'nenhum rotulo de base sem entrada no vocabulario', implode( ', ', $rotulo_orfao ) );
$sem_rotulo_a = array_diff( $ambientes, array_keys( $rot['ambiente'] ) );
f2_ok( empty( $sem_rotulo_a ), 'todo ambiente do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_a ) );
$sem_rotulo_t = array_diff( $esquema['vocabularios']['material_tessela'], array_keys( $rot['tessela'] ) );
f2_ok( empty( $sem_rotulo_t ), 'toda tessela do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_t ) );

$estados       = 0;
$finas         = array();
$sem_acento    = array();
$incoerentes   = array();
$corpos        = array();

/**
 * Portugues errado que chega a tela. Mede o CORPO, palavra a palavra, contra
 * uma lista de formas que so existem sem acento por erro de digitacao — foi
 * assim que o bloco 4 achou "Silicone Acetico Construcao" servido ao visitante.
 */
$formas_erradas = array(
	'acetico', 'ceramica', 'ceramicas', 'construcao', 'acrilico', 'epoxi', 'plastico',
	'aluminio', 'superficies', 'calcario', 'aquarios', 'corrosivel', 'imersao',
	'liquido', 'area', 'areas', 'agua', 'pagina', 'tecnica', 'tecnico', 'nao',
	'sao', 'liberacao', 'variacao', 'condicao', 'marmore', 'latao', 'papelao',
);

foreach ( $bases as $base ) {
	foreach ( $ambientes as $ambiente ) {
		$html  = f2_render( $raiz, 'base=' . $base . '&onde=' . $ambiente );
		$corpo = f2_corpo( $html );
		$texto = f2_texto( $corpo );
		$corpos[ $base . '|' . $ambiente ] = $corpo;
		$estados++;

		if ( mb_strlen( $texto ) < 1500 ) {
			$finas[] = $base . ' x ' . $ambiente . ' (' . mb_strlen( $texto ) . ')';
		}
		$minusculo = mb_strtolower( $texto, 'UTF-8' );
		foreach ( $formas_erradas as $forma ) {
			if ( preg_match( '/(?<![\p{L}])' . $forma . '(?![\p{L}])/u', $minusculo ) ) {
				$sem_acento[] = $base . ' x ' . $ambiente . ': "' . $forma . '"';
				break;
			}
		}
	}
}
f2_ok( 45 === $estados, 'os 45 estados de cola foram servidos, um processo cada', $estados . ' estados' );
f2_ok( empty( $finas ), 'nenhum estado serve pagina fina', empty( $finas ) ? 'todos acima de 1500' : implode( ' | ', array_slice( $finas, 0, 4 ) ) );
f2_ok( empty( $sem_acento ), 'nenhum estado serve portugues sem acento',
	empty( $sem_acento ) ? '45 estados limpos' : implode( ' | ', array_slice( $sem_acento, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 5. AS 18 CELULAS CONFERIDAS — a regua escrita a mao contra o que a tela diz
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * A REGUA DA REGRA 6, escrita AQUI.
 *
 * Ela le `superficies_porosas` do esquema e `condicoes` do banco, e nao chama
 * uma linha do snippet. E a trava da secao 8: duas metades que erram juntas
 * ficam verdes. A varredura acima serve os 45 estados SEM escolher caquinho, e
 * o padrao da ferramenta e pastilha de vidro — que NAO e porosa. Entao a
 * matriz escrita a mao no esquema, que e a camada de DECLARACAO, nao pode ser
 * comparada crua com o que a tela serve: quem carrega condicao cai antes de
 * chegar la, e e esta funcao que diz quem.
 * ------------------------------------------------------------------------- */

$porosas_base    = array_flip( $esquema['superficies_porosas']['bases_porosas'] );
$porosas_tessela = array_flip( $esquema['superficies_porosas']['tesselas_porosas'] );

/** Os elegiveis da camada de declaracao, lidos da matriz escrita a mao. */
function f2_elegiveis_da_matriz( $esquema, $base, $ambiente ) {
	static $cache = array();
	$chave = $base . '|' . $ambiente;
	if ( isset( $cache[ $chave ] ) ) {
		return $cache[ $chave ];
	}
	$cache[ $chave ] = array();
	foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
		if ( $c['base'] === $base && $c['ambiente'] === $ambiente ) {
			$cache[ $chave ] = array_merge(
				isset( $c['recomendados_topo'] ) ? $c['recomendados_topo'] : array(),
				isset( $c['elegiveis_abaixo_do_topo'] ) ? $c['elegiveis_abaixo_do_topo'] : array() );
		}
	}

	return $cache[ $chave ];
}

function f2_exige_porosa_no_banco( $m ) {
	return ! empty( $m['condicoes']['exige_superficie_porosa']['valor'] );
}

function f2_condicao_falha( $m, $base, $tessela ) {
	global $porosas_base, $porosas_tessela;
	if ( ! f2_exige_porosa_no_banco( $m ) ) {
		return false;
	}

	return ! isset( $porosas_base[ $base ] ) && ! isset( $porosas_tessela[ $tessela ] );
}

/* O caquinho que a varredura dos 45 estados realmente serviu. Lido da entrada
   saneada da propria ferramenta e nao digitado aqui: se um dia o padrao mudar,
   este portao acompanha em vez de medir um estado que ninguem ve. */
$entrada_padrao = cdm_f2_entrada();
$tessela_varrida = $entrada_padrao['tessela'];
f2_ok( isset( $rot['tessela'][ $tessela_varrida ] ),
	'o caquinho padrao da varredura e um do vocabulario', $tessela_varrida );

echo "\n5. As " . $esperadas_cola . " celulas de cola, contra a matriz escrita a mao no bloco 3\n";

$erros_celula = array();
$graves       = array();

foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
	$chave = $c['base'] . '|' . $c['ambiente'];
	$corpo = isset( $corpos[ $chave ] ) ? $corpos[ $chave ] : '';
	if ( '' === $corpo ) {
		$erros_celula[] = $chave . ': nao foi servida';
		continue;
	}

	/* A FRASE-RESPOSTA e a vitrine sao onde o recomendado aparece. A secao de
	   eliminados fica FORA desta medida de proposito: o nome de um produto
	   proibido aparece la, e contar na pagina inteira encontraria os dois. */
	$pedaco_html = '';
	if ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>\s*<div class="cdm-f2-secao">\s*<h2>Onde comprar</h2>(.*?)(?=<div class="cdm-f2-secao">)#is', $corpo, $mp ) ) {
		$pedaco_html = $mp[1] . $mp[2];
	} elseif ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>#is', $corpo, $mp ) ) {
		$pedaco_html = $mp[1];
	}
	$pedaco = f2_texto( $pedaco_html );
	$fora_html = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo, $mf ) ? $mf[1] : '';
	$fora      = f2_texto( $fora_html );

	/* O BLOCO DE RECUSA SAI DO PEDACO ANTES DE QUALQUER AFIRMACAO SOBRE QUEM
	   ESTA RECOMENDADO — e isto e a quarta trava da secao 8 do ARQUIPELAGO.md
	   aplicada de novo, agora contra um texto que esta execucao mesma escreveu.
	   A recusa da regra 6 NOMEIA o produto ("o Cascola PL500 e declarado para
	   plastico, mas exige uma condicao..."), porque a secao 7 manda nomear a
	   causa medida. A regua antiga media presenca de palavra dentro da regiao da
	   resposta e leu esse nome como recomendacao: acusou de GRAVE uma pagina que
	   estava dizendo exatamente a verdade. A saida nao e heuristica melhor (
	   procurar "mas exige" perto do nome seria adivinhar pela vizinhanca): e a
	   pagina MARCAR a recusa no markup, que ela ja faz com `cdm-f2-faixa`, e o
	   teste retirar o marcado e proibir o nome em todo o resto.

	   E para a declaracao nao virar porta dos fundos — bastaria embrulhar a
	   vitrine inteira na classe de recusa —, o bloco marcado tem de ABRIR
	   negando, e eles sao CONTADOS: no maximo um por resposta de cola. */
	$blocos_recusa = array();
	if ( preg_match_all( '#<p class="cdm-f2-frase cdm-f2-faixa">(.*?)</p>#is', $pedaco_html, $mr ) ) {
		$blocos_recusa = $mr[1];
	}
	foreach ( $blocos_recusa as $bloco ) {
		$t_bloco = f2_texto( $bloco );
		if ( 0 !== mb_strpos( $t_bloco, 'Não' ) ) {
			$graves[] = $chave . ': bloco marcado como recusa que nao ABRE negando — "'
				. mb_substr( $t_bloco, 0, 40 ) . '"';
		}
	}
	if ( count( $blocos_recusa ) > 1 ) {
		$graves[] = $chave . ': ' . count( $blocos_recusa ) . ' blocos de recusa numa resposta so';
	}
	$pedaco = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '', $pedaco_html ) );

	/* A MATRIZ DO ESQUEMA E A CAMADA DE DECLARACAO; a tela e ela MENOS a regra 6.
	   Quem carrega condicao e nao a cumpre neste par de superficies sai da
	   recomendacao e tem de aparecer no grupo proprio — e as duas metades sao
	   cobradas, porque so cobrar a primeira deixaria o produto sumir da pagina
	   inteira sem ninguem ver. */
	$caidos_pela_condicao = array();
	$elegiveis_da_celula  = array_merge(
		isset( $c['recomendados_topo'] ) ? $c['recomendados_topo'] : array(),
		isset( $c['elegiveis_abaixo_do_topo'] ) ? $c['elegiveis_abaixo_do_topo'] : array() );
	foreach ( $elegiveis_da_celula as $id ) {
		if ( f2_condicao_falha( $por_id[ $id ], $c['base'], $tessela_varrida ) ) {
			$caidos_pela_condicao[] = $id;
		}
	}
	$sobreviventes = array_values( array_diff( $elegiveis_da_celula, $caidos_pela_condicao ) );

	foreach ( $sobreviventes as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $pedaco, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" era para estar recomendado e nao esta';
		}
	}
	foreach ( $caidos_pela_condicao as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			/* Mesmo peso do defeito GRAVE: a pagina estaria recomendando um produto
			   que ela mesma, duas secoes abaixo, diz que nao cumpre a condicao. */
			$graves[] = $chave . ': "' . $nome . '" caiu pela condicao e mesmo assim esta recomendado';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" caiu pela condicao e sumiu da pagina';
		}
	}
	foreach ( $c['eliminados_por_proibicao'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			/* COERENCIA DA RECOMENDACAO (secao 12): recomendar em primeiro lugar
			   um produto que a propria pagina diz nao servir e defeito GRAVE. */
			$graves[] = $chave . ': "' . $nome . '" esta recomendado E a pagina diz que ele nao serve';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" nao aparece na secao do que nao usar';
		}
		/* E APARECE NO BLOCO DA CAUSA CERTA. A afirmacao acima procura o nome na
		   secao inteira, e ficou verde quando uma mutacao fez a regra 6 rodar
		   ANTES das cinco: o produto proibido pelo fabricante saia do bloco da
		   proibicao e caia no da condicao, e a pagina parava de dizer "a Tekbond
		   escreve espelhos na lista do que este produto nao deve tocar" para
		   dizer que faltava porosidade. A elegibilidade nao muda; a frase que o
		   leitor recebe muda inteira, e e a frase que esta pagina vende.
		   Causa se mede pelo BLOCO em que o produto sai, nunca por estar na
		   secao — e o bloco e marcado no markup, como manda a secao 8. */
		$lista_proibicao = preg_match( '#<ul class="cdm-f2-lista-fora">(.*?)</ul>#is', $fora_html, $mlp )
			? f2_texto( $mlp[1] ) : '';
		$blocos_condicao = preg_match_all( '#<p class="cdm-f2-condicao-fora">(.*?)</p>#is', $fora_html, $mbc )
			? f2_texto( implode( ' ', $mbc[1] ) ) : '';
		if ( false === mb_strpos( $lista_proibicao, $nome ) ) {
			$graves[] = $chave . ': "' . $nome . '" e proibido pelo fabricante e nao esta no bloco da proibicao';
		}
		if ( '' !== $blocos_condicao && false !== mb_strpos( $blocos_condicao, $nome ) ) {
			$graves[] = $chave . ': "' . $nome . '" e proibido e aparece como caso de condicao de superficie';
		}
	}
	/* A LISTA DO SILENCIO E CONFERIDA NOS DOIS SENTIDOS, e nao por acaso: sem
	   isto, a mutacao "a categoria some da pergunta" PASSOU. Ela fazia os cinco
	   rejuntes entrarem na decisao de COLAGEM como "eliminados por silencio" —
	   frase sem sentido para um produto que nunca foi candidato a colar nada —
	   e o teste nao via, porque so olhava o topo e os proibidos. Quem afirma
	   sobre uma lista tem que cobrar o que falta E o que sobra. */
	/* O paragrafo do silencio DA COLA, e nao o primeiro do corpo: a secao do
	   rejunte usa a mesma classe, e procurar no corpo inteiro achava o dela —
	   o mesmo erro de contar &#038; na pagina toda em vez de dentro do script. */
	$silencio = preg_match( '#<p class="cdm-f2-silencio">(.*?)</p>#is', $fora_html, $ms ) ? f2_texto( $ms[1] ) : '';
	foreach ( $c['eliminados_por_silencio'] as $id ) {
		if ( false === mb_strpos( $silencio, f2_nome_esperado( $por_id[ $id ] ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $por_id[ $id ] ) . '" era para estar no silencio e nao esta';
		}
	}
	$esperado_no_silencio = $c['eliminados_por_silencio'];
	foreach ( $por_id as $id => $m ) {
		if ( in_array( $id, $esperado_no_silencio, true ) ) {
			continue;
		}
		if ( false !== mb_strpos( $silencio, f2_nome_esperado( $m ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $m ) . '" aparece no silencio e nao devia';
		}
	}

	/* Celula sem recomendado tem que DIZER que nao tem, nunca ficar em branco — e
	   dizer a CAUSA CERTA. Sao duas frases porque sao duas causas: "ninguem
	   declara" e "alguem declara e a condicao nao fecha". Trocar uma pela outra
	   e a afirmacao em bloco com escopo maior do que o medido. */
	if ( ! $sobreviventes ) {
		$t_corpo = f2_texto( $corpo );
		if ( $caidos_pela_condicao ) {
			if ( false === mb_strpos( $t_corpo, 'o motivo não é falta de declaração' ) ) {
				$erros_celula[] = $chave . ': caiu pela condicao e a recusa nao nomeia a causa medida';
			}
			if ( false !== mb_strpos( $t_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
				$graves[] = $chave . ': a pagina nega que exista declaracao e ela mesma cita a declaracao';
			}
		} elseif ( false === mb_strpos( $t_corpo, 'Não temos cola para indicar' ) ) {
			$erros_celula[] = $chave . ': faixa descoberta sem a frase que a declara';
		}
	}
}
f2_ok( empty( $graves ), 'nenhuma pagina recomenda o que ela mesma diz que nao serve',
	empty( $graves ) ? 'as ' . $esperadas_cola . ' celulas' : implode( ' | ', $graves ) );
f2_ok( empty( $erros_celula ), 'a tela diz o que a matriz escrita a mao manda',
	empty( $erros_celula ) ? $esperadas_cola . ' celulas' : implode( ' | ', array_slice( $erros_celula, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 6. O REJUNTE — a grade pisa na borda de cada faixa declarada
 * ------------------------------------------------------------------------- */

echo "\n6. O rejunte: a grade pisa nas bordas das faixas declaradas\n";

/* A regua das bordas e recalculada AQUI, das faixas do banco, e nao lida da
   observacao que o esquema escreveu ao lado. Grade que nao pisa na borda e
   amostra com nome de grade (secao 8). */
$bordas = array();
foreach ( $rejuntes['materiais'] as $m ) {
	foreach ( array( 'junta_min_mm', 'junta_max_mm' ) as $campo ) {
		$v = isset( $m['propriedades'][ $campo ]['valor'] ) ? $m['propriedades'][ $campo ]['valor'] : null;
		if ( null !== $v ) {
			$bordas[ (int) $v ] = true;
			$bordas[ (int) $v + 1 ] = true;
		}
	}
}
ksort( $bordas );
$na_grade = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$na_grade[ (int) $c['junta_mm'] ] = true;
}
$bordas_uteis = array_filter( array_keys( $bordas ), function ( $v ) { return $v >= 1 && $v <= 12; } );
$faltando     = array_diff( $bordas_uteis, array_keys( $na_grade ) );
f2_ok( empty( $faltando ), 'a grade do esquema pisa em toda borda de faixa declarada',
	empty( $faltando ) ? implode( ', ', array_keys( $na_grade ) ) . ' mm' : 'falta ' . implode( ', ', $faltando ) );

$estados_r    = 0;
$erros_rejunte = array();
for ( $junta = 1; $junta <= 12; $junta++ ) {
	foreach ( $ambientes as $ambiente ) {
		$html = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta );
		$estados_r++;
		$corpo = f2_corpo( $html );
		if ( ! preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)</div>\s*<div class="cdm-f2-secao#is', $corpo, $mr ) ) {
			/* A secao do rejunte e a ultima do bloco de saida em alguns estados. */
			preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*)#is', $corpo, $mr );
		}
		$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
		if ( '' === $trecho ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': secao do rejunte ausente';
			continue;
		}
		if ( false === mb_strpos( $trecho, (string) $junta ) ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': a resposta nao repete a folga escolhida';
		}
	}
}
f2_ok( 60 === $estados_r, 'os 60 estados de rejunte foram servidos', $estados_r . ' estados' );
f2_ok( empty( $erros_rejunte ), 'todo estado de rejunte serve a secao dele',
	empty( $erros_rejunte ) ? '60 estados' : implode( ' | ', array_slice( $erros_rejunte, 0, 4 ) ) );

$erros_matriz_r = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$html   = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $c['ambiente'] . '&junta=' . (int) $c['junta_mm'] );
	$corpo  = f2_corpo( $html );
	preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mr );
	$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
	preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', isset( $mr[1] ) ? $mr[1] : '', $mf );
	$frase = isset( $mf[1] ) ? f2_texto( $mf[1] ) : '';

	foreach ( $c['recomendados_topo'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era topo e nao esta na frase';
		}
	}
	/* OS CARTOES CONTAM TANTO QUANTO A FRASE. Duas mutacoes PASSARAM por esta
	   fresta — "faixa de junta abre 1 mm para baixo" e "faixa pela metade vira
	   sem limite" —, e as duas pelo mesmo motivo: o produto indevido nao subia
	   ao topo, entrava como elegivel ABAIXO do topo, e a frase so nomeia o topo.
	   Recomendar em segundo lugar o que o fabricante nao declara e recomendar. */
	$vitrine_r = '';
	if ( preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>.*?<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $corpo, $mv ) ) {
		$vitrine_r = f2_texto( $mv[1] );
	}
	$recomendaveis = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
	foreach ( array_merge( $c['eliminados_por_ambiente'], $c['eliminados_por_faixa_de_junta'] ) as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na frase e era para estar fora';
		}
		if ( '' !== $vitrine_r && false !== mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na vitrine e era para estar fora';
		}
	}
	foreach ( $recomendaveis as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era elegivel e nao esta na vitrine';
		}
	}
	if ( ! $c['recomendados_topo'] && false === mb_strpos( $trecho, 'Não temos rejunte para indicar' ) ) {
		$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': faixa descoberta sem a frase que a declara';
	}
}
f2_ok( empty( $erros_matriz_r ), 'a tela do rejunte diz o que a matriz escrita a mao manda',
	empty( $erros_matriz_r ) ? $esperadas_rejunte . ' celulas' : implode( ' | ', array_slice( $erros_matriz_r, 0, 4 ) ) );

/* O produto cuja faixa de junta nao foi obtida nao pode ser recomendado em
   NENHUM dos 50 estados. E o achado mais valioso do bloco 3c e o mais facil de
   perder: ele e o unico do banco que nomeia pastilha de vidro submersa. */
$sem_faixa = array();
foreach ( $rejuntes['materiais'] as $m ) {
	$min = isset( $m['propriedades']['junta_min_mm']['valor'] ) ? $m['propriedades']['junta_min_mm']['valor'] : null;
	$max = isset( $m['propriedades']['junta_max_mm']['valor'] ) ? $m['propriedades']['junta_max_mm']['valor'] : null;
	if ( null === $min || null === $max ) {
		$sem_faixa[] = f2_nome_esperado( $m );
	}
}
$vazou = array();
if ( $sem_faixa ) {
	for ( $junta = 1; $junta <= 12; $junta++ ) {
		foreach ( $ambientes as $ambiente ) {
			$corpo = f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta ) );
			/* Frase E vitrine: o produto sem faixa de junta nao pode aparecer em
			   NENHUM dos dois lugares — foi entrando pela vitrine que a mutacao
			   da faixa pela metade passou. */
			preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mf );
			$bloco_r = isset( $mf[1] ) ? $mf[1] : '';
			$recomendado_ali = f2_texto(
				( preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', $bloco_r, $m1 ) ? $m1[1] : '' )
				. ' ' . ( preg_match( '#<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $bloco_r, $m2 ) ? $m2[1] : '' )
			);
			foreach ( $sem_faixa as $nome ) {
				if ( false !== mb_strpos( $recomendado_ali, $nome ) ) {
					$vazou[] = $junta . 'mm x ' . $ambiente . ': ' . $nome;
				}
			}
		}
	}
}
f2_ok( ! empty( $sem_faixa ), 'o banco tem produto com faixa de junta nao obtida, e ele e medido', implode( ', ', $sem_faixa ) );
f2_ok( empty( $vazou ), 'produto sem faixa de junta nunca e recomendado, nos 60 estados',
	empty( $vazou ) ? '60 estados' : implode( ' | ', array_slice( $vazou, 0, 3 ) ) );

/* Entrada fora da faixa volta ao padrao em vez de servir bobagem. */
$fora_da_faixa = f2_corpo( f2_render( $raiz, 'base=inventada&onde=marte&junta=99' ) );
f2_ok( false !== mb_strpos( f2_texto( $fora_da_faixa ), 'Para colar em cerâmica' ),
	'entrada invalida cai no padrao em vez de quebrar a pagina' );

/* A MARCA EM DOBRO NAO APARECE EM TESTE DE CONTER. A mutacao que colava a marca
   em todo nome PASSOU na primeira rodada porque "Rejunte Ceramicas Quartzolit"
   esta DENTRO de "Quartzolit Rejunte Ceramicas Quartzolit" — procurar por
   conter aprova o nome errado que engloba o certo. A regua tem que ser de
   igualdade, e e o <h3> do cartao que carrega o nome. */
$nomes_na_tela = array();
$titulos_ruins = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4' ) as $consulta ) {
	$corpo_c = f2_corpo( f2_render( $raiz, $consulta ) );
	preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<span class="cdm-f2-marca">(.*?)</span>\s*<h3>(.*?)</h3>#is', $corpo_c, $mn, PREG_SET_ORDER );
	foreach ( $mn as $cartao ) {
		$marca_html = f2_texto( $cartao[1] );
		$titulo     = f2_texto( $cartao[2] );
		$nomes_na_tela[ $titulo ] = true;
		/* O <h3> traz o nome comercial; a marca sai no seu proprio campo, uma vez
		   so. Nome que repete a marca ja impressa ao lado dela e marca em dobro. */
		if ( '' !== $marca_html && mb_substr_count( mb_strtolower( $marca_html . ' ' . $titulo, 'UTF-8' ),
				mb_strtolower( $marca_html, 'UTF-8' ) ) > 2 ) {
			$titulos_ruins[] = $marca_html . ' / ' . $titulo;
		}
	}
}
$fora_do_banco = array();
$do_banco = array();
foreach ( $por_id as $m ) {
	$do_banco[ (string) $m['nome_comercial'] ] = true;
}
foreach ( array_keys( $nomes_na_tela ) as $titulo ) {
	if ( ! isset( $do_banco[ $titulo ] ) ) {
		$fora_do_banco[] = $titulo;
	}
}
/* O CARTAO NAO ERA O LUGAR DE MEDIR ISSO, e a mutacao provou: o <h3> traz o
   `nome_comercial` cru e nunca a composicao, entao a marca em dobro so aparece
   na FRASE e nas listas, que e onde `cdm_f2_nome()` e chamada. A regua certa e
   direta e nao depende de onde o nome sai: para todo produto cujo nome
   comercial JA carrega a marca, a composicao "<marca> <nome>" nao pode existir
   em lugar nenhum do corpo. */
$dobradas = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4',
                 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua&junta=3' ) as $consulta ) {
	$texto_c = f2_texto( f2_corpo( f2_render( $raiz, $consulta ) ) );
	foreach ( $por_id as $m ) {
		$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
		$nome  = (string) $m['nome_comercial'];
		if ( '' === $marca || false === mb_stripos( $nome, $marca ) ) {
			continue;
		}
		if ( false !== mb_strpos( $texto_c, $marca . ' ' . $nome ) ) {
			$dobradas[] = ( '' === $consulta ? 'ancora' : $consulta ) . ': "' . $marca . ' ' . $nome . '"';
		}
	}
}
f2_ok( empty( $dobradas ), 'nenhum lugar da pagina repete a marca dentro do nome do produto',
	empty( $dobradas ) ? count( $por_id ) . ' produtos em 5 estados' : implode( ' | ', array_slice( $dobradas, 0, 3 ) ) );
f2_ok( empty( $titulos_ruins ), 'nenhum cartao repete a marca dentro do nome do produto',
	empty( $titulos_ruins ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $titulos_ruins ) );
f2_ok( empty( $fora_do_banco ), 'todo nome de produto na tela e IGUAL ao do banco, nao parecido',
	empty( $fora_do_banco ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $fora_do_banco ) );

/* ---------------------------------------------------------------------------
 * 7. O bloco de compra vem ANTES da procedencia (secao 7, cicatriz da
 *    Robometria de 10/09/2026), e todo item sem link diz isso.
 * ------------------------------------------------------------------------- */

echo "\n7. Compra antes de procedencia, e o que espera link\n";

$cartoes = preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $corpo_ancora, $mc );
f2_ok( $cartoes > 0, 'a ancora serve cartoes de produto', $cartoes . ' cartoes' );
$ordem_errada = 0;
$sem_fonte    = 0;
foreach ( $mc[1] as $cartao ) {
	$p_compra = mb_strpos( $cartao, 'cdm-f2-compra' );
	$p_fonte  = mb_strpos( $cartao, 'cdm-f2-fonte' );
	if ( false === $p_fonte ) {
		$sem_fonte++;
		continue;
	}
	if ( false === $p_compra || $p_compra > $p_fonte ) {
		$ordem_errada++;
	}
}
f2_ok( 0 === $ordem_errada, 'o bloco de compra vem antes da prova de procedencia em todo cartao',
	$ordem_errada . ' fora de ordem' );
f2_ok( 0 === $sem_fonte, 'todo cartao leva o link de procedencia', $sem_fonte . ' sem fonte' );
f2_ok( false === strpos( $corpo_ancora, 'class="cdm-f2-botao" href' ) || false !== strpos( $corpo_ancora, 'rel="sponsored' ),
	'link de afiliado, quando existir, leva rel="sponsored"' );
f2_ok( (bool) preg_match_all( '#rel="nofollow noopener"#', $corpo_ancora ),
	'o link de procedencia e discreto, com rel="nofollow noopener"' );
f2_ok( false !== mb_strpos( f2_texto( $corpo_ancora ), 'comissão' ), 'o aviso de comissao esta visivel na pagina' );

/* Quantos itens esperam link — numero CONTADO do banco, nunca digitado. */
$esperando = 0;
foreach ( $por_id as $m ) {
	if ( empty( $m['afiliado']['url'] ) ) {
		$esperando++;
	}
}
$declarado = (int) $colas['afiliado']['itens_esperando_link'] + (int) $rejuntes['afiliado']['itens_esperando_link'];
f2_ok( $esperando === $declarado, 'o numero de itens esperando link bate com o banco contado',
	$esperando . ' contados, ' . $declarado . ' declarados' );
$com_loja = substr_count( $corpo_ancora, 'rel="sponsored' );
f2_ok( $com_loja > 0, 'com link no banco, o cartao serve o botao marcado como patrocinado',
	$com_loja . ' botoes' );
f2_ok( 0 === substr_count( $corpo_ancora, 'Link de loja em breve' ) || $esperando > 0,
	'so promete "em breve" quando ha item de verdade esperando link' );

/* ---------------------------------------------------------------------------
 * 7b. A ESCADA DA SECAO 25 NA TELA — os tres estados, cada um no seu mundo
 *
 * A regua e partida em tres porque cada estado pega um defeito diferente, e
 * duas delas so existem num mundo PRODUZIDO: o banco de hoje tem os dez itens
 * no estado 1, entao medir o estado 2 e o 3 no banco de hoje seria medir o
 * caminho que nenhum cartao percorre — verde com a funcao quebrada, e o dia em
 * que importasse seria o dia em que um link morresse.
 *
 * A ordem das tres importa: (a) sozinha passaria numa funcao que ignora a ficha
 * e serve so a busca; (b) sozinha passaria numa funcao que serve a busca sempre,
 * inclusive por cima da ficha; e (c) e a que pega o erro mais provavel de quem
 * escrever isto com pressa — deixar o "em breve" no lugar do piso, que e
 * exatamente o defeito que este bloco veio consertar E O UNICO QUE (a) E (b)
 * APROVARIAM JUNTAS.
 * ------------------------------------------------------------------------- */

echo "\n7b. A escada da secao 25 chega a tela\n";

/* (a) COM FICHA: a ficha e o botao e a busca desce para a linha discreta. */
$com_ficha = 0;
$sem_segunda_porta = array();
foreach ( $mc[1] as $cartao ) {
	if ( false === mb_strpos( $cartao, 'class="cdm-f2-botao" href' ) ) {
		continue;
	}
	$com_ficha++;
	if ( false === mb_strpos( $cartao, 'cdm-f2-busca' ) ) {
		$sem_segunda_porta[] = trim( f2_texto( $cartao ) );
	}
}
f2_ok( $com_ficha > 0, 'o banco de hoje serve cartao com ficha de produto', $com_ficha . ' cartoes' );
f2_ok( empty( $sem_segunda_porta ), 'cartao com ficha leva TAMBEM a busca, na linha discreta abaixo do botao',
	empty( $sem_segunda_porta ) ? $com_ficha . ' com as duas portas' : count( $sem_segunda_porta ) . ' so com o botao' );
f2_ok( false !== mb_strpos( $corpo_ancora, 'Veja todos disponíveis aqui' ),
	'a linha discreta usa a frase que a 25.2 escreve, palavra por palavra' );
f2_ok( false === mb_strpos( $corpo_ancora, 'cdm-f2-botao cdm-f2-botao-busca' ),
	'com ficha viva, a busca NAO vira botao — ela e a segunda porta, nao a primeira' );

/* TODO link do bloco de compra e link comercial, e os DOIS tem de declarar isso.
   A afirmacao antiga ("quando existir, leva rel=sponsored") olhava a pagina
   inteira e ficava verde com UM link marcado entre dois; esta varre link por
   link dentro do bloco, que e onde a diferenca aparece. Link de busca de
   afiliado e link de afiliado: o atributo declara a relacao comercial, nao o
   formato da pagina de destino. */
$links_sem_sponsored = array();
if ( preg_match_all( '#<span class="cdm-f2-compra">(.*?)</span>\s*<span class="cdm-f2-fonte"#is', $corpo_ancora, $mb ) ) {
	foreach ( $mb[1] as $bloco ) {
		if ( preg_match_all( '#<a\b[^>]*>#i', $bloco, $ml ) ) {
			foreach ( $ml[0] as $tag ) {
				if ( false === mb_strpos( $tag, 'rel="sponsored' ) ) {
					$links_sem_sponsored[] = $tag;
				}
			}
		}
	}
}
f2_ok( ! empty( $mb[1] ), 'a varredura acha os blocos de compra para conferir link por link',
	count( $mb[1] ) . ' blocos' );
f2_ok( empty( $links_sem_sponsored ), 'TODO link do bloco de compra declara rel="sponsored" — a busca tambem',
	empty( $links_sem_sponsored ) ? 'todos marcados' : implode( ' | ', array_slice( $links_sem_sponsored, 0, 2 ) ) );

/* (b) SEM FICHA, COM BUSCA: a busca SOBE e vira o botao. `sem_links=1` apaga a
      ficha e deixa o piso de pe, que e o estado 2 da escada. */
$mundo_so_busca = f2_corpo( f2_render( $raiz, 'sem_links=1' ) );
$botoes_busca   = substr_count( $mundo_so_busca, 'cdm-f2-botao cdm-f2-botao-busca' );
f2_ok( $botoes_busca > 0, 'PRODUZ O MUNDO: sem ficha, a busca sobe e vira o botao do cartao',
	$botoes_busca . ' botoes de busca' );
f2_ok( false !== mb_strpos( $mundo_so_busca, 'Ver as opções na loja' ),
	'o botao de busca tem texto PROPRIO — ele abre uma lista, nao a ficha do produto' );
/* A AFIRMACAO ERA "NUNCA DIZ EM BREVE", E ELA MORREU NO DIA EM QUE O BANCO
   CRESCEU — de um jeito que vale escrever, porque e a forma disfarcada do
   numero digitado. Ela nasceu em 13/09/2026 de manha, quando os CINCO itens de
   cola tinham piso, e naquele mundo ela era exata. Ao entrarem dois produtos
   sem piso, no mesmo dia a tarde, ela passou a reprovar uma pagina CERTA: a
   25.2 manda o cartao reservar o lugar de quem nao tem nem piso, e era isso que
   a tela estava fazendo. O conserto nao e afrouxar — e contar. O numero de
   "em breve" na tela tem de ser IGUAL ao numero de cartoes cujo produto o BANCO
   diz estar sem piso, e essa versao e mais dura que a antiga nas duas direcoes:
   ela reprova o "em breve" a mais (o defeito original) E o "em breve" a menos,
   que seria a pagina escondendo do leitor que aquele produto nao tem para onde
   mandar. A antiga ficaria verde de graca no dia em que todo item tivesse piso
   de novo; esta continua medindo. */
$cartoes_sem_piso_no_banco = 0;
if ( preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $mundo_so_busca, $mcb ) ) {
	foreach ( $mcb[1] as $cartao ) {
		/* O nome sai do <h3> do cartao, que e onde a tela o escreve, e nao de uma
		   busca por substring no cartao inteiro: `strip_tags` cola a marca no
		   nome ("TekbondSilicone Acetico Maxx") e a comparacao ingenua nunca
		   casa. Errar isso deixaria o contador em zero e o portao verde por
		   vacuidade, que e o defeito que este portao existe para pegar. */
		if ( ! preg_match( '#<h3>(.*?)</h3>#is', $cartao, $mh ) ) {
			continue;
		}
		$nome_no_cartao = f2_texto( $mh[1] );
		foreach ( $por_id as $m ) {
			if ( ! empty( $m['afiliado']['url_busca'] ) ) {
				continue;
			}
			if ( $nome_no_cartao === (string) $m['nome_comercial'] ) {
				$cartoes_sem_piso_no_banco++;
				break;
			}
		}
	}
	f2_ok( count( $mcb[1] ) > 0, 'a varredura do mundo sem ficha acha os cartoes para contar',
		count( $mcb[1] ) . ' cartoes' );
}
$em_breve_na_tela = substr_count( $mundo_so_busca, 'Link de loja em breve' );
f2_ok( $em_breve_na_tela === $cartoes_sem_piso_no_banco,
	'25.2: a tela diz "em breve" exatamente para quem o BANCO diz estar sem piso',
	$em_breve_na_tela . ' na tela, ' . $cartoes_sem_piso_no_banco . ' contados no banco' );
f2_ok( false === mb_strpos( $mundo_so_busca, 'Ver na loja</a>' ),
	'sem ficha, nenhum cartao promete "Ver na loja" — a promessa segue o link que existe' );

/* (c) SEM NADA: "em breve" e a resposta certa, e so aqui. */
$mundo_sem_piso = f2_corpo( f2_render( $raiz, 'sem_piso=1' ) );
$sem_loja       = substr_count( $mundo_sem_piso, 'Link de loja em breve' );
f2_ok( $sem_loja > 0, 'PRODUZ O MUNDO: sem ficha E sem piso, o cartao reserva o lugar em vez de sumir',
	$sem_loja . ' cartoes' );
f2_ok( 0 === substr_count( $mundo_sem_piso, 'rel="sponsored' ),
	'sem piso nenhum, nao sobra link de afiliado nenhum na pagina' );
$cartoes_sem_piso = preg_match_all( '#<li class="cdm-f2-cartao[^"]*">#is', $mundo_sem_piso );
f2_ok( $cartoes_sem_piso === $cartoes,
	'o cartao sem compra continua sendo servido: a recomendacao nao depende do link',
	$cartoes_sem_piso . ' cartoes contra ' . $cartoes . ' do banco de hoje' );

/* A ESCADA E DE UMA FUNCAO SO, E ISTO SE MEDE NA MARCACAO, NAO NA PROSA.
   Se a F1, a ficha do Guia ou a pagina da peca reescreverem os tres estados por
   conta propria, dois degraus discordam em silencio. A varredura conta a CLASSE
   emitida — `class="cdm-f2-sem-loja"` so aparece em marcacao, enquanto a frase
   legivel aparece tambem em comentario, e contar a frase mediria o quanto os
   comentarios falam dela. A primeira versao desta linha cometeu esse erro e
   reprovou o proprio comentario que explica a regra. */
$emissoes = array();
foreach ( glob( dirname( __DIR__ ) . '/snippets/*.php' ) as $arquivo ) {
	$fonte = file_get_contents( $arquivo );
	$n     = substr_count( $fonte, 'class="cdm-f2-sem-loja"' )
		+ substr_count( $fonte, 'cdm-f2-botao cdm-f2-botao-busca' )
		+ substr_count( $fonte, 'class="cdm-f2-busca"' );
	if ( $n ) {
		$emissoes[ basename( $arquivo ) ] = $n;
	}
}
f2_ok( array( 'clubedomosaico-f2.php' => 3 ) === $emissoes,
	'os tres degraus sao emitidos por UM snippet so, um lugar cada, nunca copiados',
	json_encode( $emissoes ) );

/* ---------------------------------------------------------------------------
 * 8. As duas faixas descobertas, declaradas em vez de preenchidas no chute
 * ------------------------------------------------------------------------- */

echo "\n8. O que a ilha diz que nao sabe (secao 7 do contrato)\n";

$t = f2_texto( $corpo_ancora );

/* A SECAO DO QUE FALTA E CONTADA, E O PORTAO RECONTA POR UM CAMINHO PROPRIO.
   As duas afirmacoes que estavam aqui procuravam as frases "peça de plástico" e
   "dentro da água o tempo todo" — as duas faixas que a pagina declarava nao
   saber. Elas eram exatas ate 13/09/2026 e viraram falsas no mesmo dia, quando
   os dois produtos novos abriram as duas. Portao que procura a frase de ontem
   passa a cobrar a mentira: por isso ele deixou de procurar texto e passou a
   RECONTAR, com regua propria (le o banco e o esquema, nao chama o snippet) e
   comparar com o numero que a tela publica. */
if ( preg_match( '#<h2>O que a gente ainda não responde</h2>(.*?)</div>#is', $corpo_ancora, $mfx ) ) {
	$texto_faltas = f2_texto( $mfx[1] );
} else {
	$texto_faltas = '';
}
f2_ok( '' !== $texto_faltas, 'a pagina serve a secao do que ela ainda nao responde' );

/* A RECONTAGEM SAI POR DOIS CAMINHOS, E OS DOIS MEDEM COISAS DIFERENTES.
 *
 * (i) O TOTAL e aritmetica do vocabulario: base x lugar x caquinho. Nao depende
 *     de elegibilidade nenhuma, entao ele prova que a pagina esta falando da
 *     entrada INTEIRA e nao de um recorte dela.
 *
 * (ii) O NUMERO DE DESCOBERTAS e recontado VARRENDO AS PAGINAS SERVIDAS, uma
 *      por combinacao, um processo cada. Isso mede a agregacao — o laco que a
 *      secao nova escreveu — contra o que cada estado realmente serve, e e
 *      exatamente onde mora o erro provavel de quem escreve um contador: somar
 *      uma dimensao a menos, ou contar "sem topo" onde ha elegivel abaixo do
 *      topo.
 *
 * O QUE ISTO NAO MEDE, dito em vez de escondido: as duas metades leem a mesma
 * implementacao de elegibilidade, entao esta recontagem NAO e regua independente
 * para as cinco regras — quem faz esse papel sao as 18 celulas escritas a mao no
 * esquema e as 5 ancoras da regra 6 no validador. A independencia que falta tem
 * nome e tamanho: a matriz escrita a mao cobre 18 das 45 celulas de base x
 * lugar, e as outras 27 so passam por aqui. Esta escrito no ESTADO.md como
 * divida nomeada, e o conserto e a matriz chegar a 45 — nunca o portao fingir
 * que ja mede o que nao mede.
 */
$total_combinacoes = count( $esquema['vocabularios']['base'] )
	* count( $esquema['vocabularios']['ambiente'] )
	* count( $esquema['vocabularios']['material_tessela'] );

$descobertos_varridos = 0;
$varridos             = 0;
$sem_resposta_mudos   = array();
$nao_prestados        = array();
foreach ( $esquema['vocabularios']['base'] as $b_ ) {
	foreach ( $esquema['vocabularios']['ambiente'] as $a_ ) {
		foreach ( $esquema['vocabularios']['material_tessela'] as $t_ ) {
			$corpo_ = f2_corpo( f2_render( $raiz, 'base=' . $b_ . '&onde=' . $a_ . '&caco=' . $t_ ) );
			$varridos++;
			$texto_ = f2_texto( $corpo_ );
			$vazio  = ( false !== mb_strpos( $texto_, 'Não temos cola para indicar' )
				|| false !== mb_strpos( $texto_, 'o motivo não é falta de declaração' ) );
			if ( $vazio ) {
				$descobertos_varridos++;
			}
			/* Estado sem recomendacao tem de DIZER isso. Pagina que fica em
			   branco e indistinguivel de pagina quebrada — e some da contagem
			   sem ninguem ver, que e como um contador fica verde errado. */
			if ( ! $vazio && false === mb_strpos( $corpo_, 'class="cdm-f2-cartao' ) ) {
				$sem_resposta_mudos[] = $b_ . ' x ' . $a_ . ' x ' . $t_;
			}

			/* A PRESTACAO DE CONTAS DA COLA, nas 270 respostas (secao 7 do
			   ARQUIPELAGO.md, a regra que nasceu nesta ilha em 12/09/2026).
			   Todo item da categoria consultada aparece EXATAMENTE UMA VEZ na
			   prosa: ou na frase que o recomenda, e ai ele esta na vitrine, ou
			   numa linha que diz por que ele nao esta. O rejunte ja tinha portao
			   proprio para isso; a cola nunca teve, e a regra 6 acabou de criar
			   um QUINTO grupo — que e exatamente a forma como um grupo some da
			   tela sem ninguem ver, porque grupo vazio nao denuncia que a tela
			   nao sabe imprimi-lo.

			   A soma e cobrada contra o banco CONTADO do arquivo, nunca contra
			   um numero digitado aqui. */
			/* O LADO em que o produto cai e decidido pelo MARKUP, nao pela
			   posicao no texto. O bloco de recusa (`cdm-f2-faixa`) mora dentro
			   da regiao da resposta e e, em conteudo, o lado do "por que ele nao
			   esta" — ele nomeia produto para dizer que aquele produto NAO foi
			   indicado. Conta-lo como recomendacao poria o mesmo item nos dois
			   lados e reprovaria uma pagina certa; ignora-lo deixaria passar uma
			   pagina que nomeia o produto sem nunca dizer de que lado ele esta.
			   A regra que a secao 7 cobra e "cada item em exatamente UM lado", e
			   e o lado que se mede. */
			$resposta_html = '';
			if ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>\s*<div class="cdm-f2-secao">\s*<h2>Onde comprar</h2>(.*?)(?=<div class="cdm-f2-secao">)#is', $corpo_, $mr_ ) ) {
				$resposta_html = $mr_[1] . $mr_[2];
			}
			$recusa_html     = '';
			if ( preg_match_all( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', $resposta_html, $mrec_ ) ) {
				$recusa_html = implode( ' ', $mrec_[0] );
			}
			$regiao_resposta = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '', $resposta_html ) );
			$regiao_fora = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo_, $mf_ )
				? f2_texto( $recusa_html . ' ' . $mf_[1] ) : f2_texto( $recusa_html );
			foreach ( $por_id as $id_c => $m_c ) {
				if ( 'cola' !== $m_c['categoria'] || 'ativo' !== $m_c['status'] ) {
					continue;
				}
				$nome_c = (string) $m_c['nome_comercial'];
				$na_resposta = ( false !== mb_strpos( $regiao_resposta, $nome_c ) );
				$no_fora     = ( false !== mb_strpos( $regiao_fora, $nome_c ) );
				if ( ! $na_resposta && ! $no_fora ) {
					$nao_prestados[] = $b_ . ' x ' . $a_ . ' x ' . $t_ . ': ' . $nome_c . ' sumiu da pagina';
				} elseif ( $na_resposta && $no_fora ) {
					$nao_prestados[] = $b_ . ' x ' . $a_ . ' x ' . $t_ . ': ' . $nome_c . ' aparece nos dois lados';
				}
			}
		}
	}
}
f2_ok( $varridos === $total_combinacoes, 'a varredura visitou a entrada inteira, um processo cada',
	$varridos . ' de ' . $total_combinacoes );
$colas_ativas = 0;
foreach ( $por_id as $m_c ) {
	if ( 'cola' === $m_c['categoria'] && 'ativo' === $m_c['status'] ) {
		$colas_ativas++;
	}
}
f2_ok( empty( $nao_prestados ),
	'secao 7: cada cola do banco e nomeada UMA vez em cada uma das ' . $varridos . ' respostas',
	empty( $nao_prestados )
		? ( $colas_ativas * $varridos ) . ' nomeacoes, ' . $colas_ativas . ' colas contadas do arquivo'
		: implode( ' | ', array_slice( $nao_prestados, 0, 3 ) ) );
f2_ok( empty( $sem_resposta_mudos ), 'nenhum estado fica sem cartao E sem dizer que nao tem',
	empty( $sem_resposta_mudos ) ? $varridos . ' estados' : implode( ' | ', array_slice( $sem_resposta_mudos, 0, 3 ) ) );
f2_ok( false !== mb_strpos( $texto_faltas, number_format_i18n( $total_combinacoes ) . ' combinações' ),
	'o total de combinacoes publicado bate com o vocabulario contado', $total_combinacoes . ' combinacoes' );
f2_ok( false !== mb_strpos( $texto_faltas, 'Em ' . number_format_i18n( $descobertos_varridos ) . ' delas' ),
	'o numero de faixas descobertas publicado bate com a varredura das paginas',
	$descobertos_varridos . ' varridas' );
f2_ok( $descobertos_varridos > 0 && $descobertos_varridos < $total_combinacoes,
	'a contagem nao e vacuidade: nem tudo descoberto, nem tudo coberto',
	$descobertos_varridos . ' de ' . $total_combinacoes );

f2_ok( false !== mb_strpos( $t, 'material de imprensa' ),
	'a pagina diz por que a menção de nivel 4 nao vira recomendacao' );

/* O tempo de espera que a ilha NAO tem: o campo existe no banco com o motivo
   escrito, e a pagina diz que nao publica em vez de simplesmente nao ter a
   secao. Ausencia de secao e indistinguivel de "nao importa". */
$mdf = f2_texto( f2_corpo( f2_render( $raiz, 'base=mdf_madeira&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $mdf, 'ainda não publica o tempo de espera' ),
	'quando falta o tempo de espera, a pagina diz que falta' );
$ceramica = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $ceramica, '24 horas' ),
	'quando o fabricante declara a cura, a pagina publica o numero' );

/* PLASTICO: a faixa abriu em 13/09/2026, e o portao mede as DUAS metades dela.
   Com caquinho de vidro continua sem resposta — e agora com a causa certa, que
   e a condicao e nao a ausencia de declaracao. Com caquinho de ceramica ha
   recomendacao. Medir so uma das duas deixaria a regra 6 sem prova: as duas
   telas seriam identicas byte a byte se a condicao nao existisse. */
$plastico = f2_texto( f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_vidro' ) ) );
f2_ok( false !== mb_strpos( $plastico, 'o motivo não é falta de declaração' ),
	'plastico com caquinho liso: a recusa nomeia a condicao, nao a ausencia de declaracao' );

/* A SAIDA QUE A PAGINA OFERECE E CONFERIDA CONTRA O ESQUEMA, nas duas direcoes.
   A frase "trocando por X, ele voltaria a servir" e a unica da pagina que diz a
   pessoa o que FAZER para a peca nao descolar, e ela nasceu com os quatro nomes
   digitados. Digitada, ela erra calada no dia em que uma tessela nova entrar no
   vocabulario — e erra do jeito caro, mandando colar. Aqui o esperado sai do
   esquema e cobra as duas direcoes: toda porosa nomeada, nenhuma nao porosa. */
/* MEDIDO NO BLOCO, NAO NO CORPO — e a primeira versao disto reprovou por isso.
   Ela procurou os nomes no corpo inteiro e achou "Caquinho de espelho" dentro
   do <select> do formulario, que serve as seis opcoes em toda pagina. E o mesmo
   erro de contar &#038; na pagina inteira em vez de dentro do <script>, um
   nivel mais fundo: aqui nem o corpo basta, porque a afirmacao e sobre UMA
   frase. Quem afirma sobre uma frase mede naquela frase. */
$plastico_html = f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_vidro' ) );
$bloco_saida   = preg_match_all( '#<p class="cdm-f2-condicao-fora">(.*?)</p>#is', $plastico_html, $mbs )
	? f2_texto( implode( ' ', $mbs[1] ) ) : '';
$rot_t = $rot['tessela'];
$erros_saida = array();
f2_ok( '' !== $bloco_saida, 'a varredura acha o bloco da condicao para medir a saida oferecida' );
foreach ( $esquema['superficies_porosas']['tesselas_porosas'] as $t_p ) {
	if ( false === mb_stripos( $bloco_saida, $rot_t[ $t_p ] ) ) {
		$erros_saida[] = 'falta ' . $rot_t[ $t_p ];
	}
}
foreach ( $esquema['superficies_porosas']['tesselas_nao_porosas'] as $t_n ) {
	/* O caquinho ESCOLHIDO aparece no mesmo bloco, na frase que diz que ele nao
	   absorve agua — entao a proibicao vale so para os OUTROS nao porosos. */
	if ( 'pastilha_vidro' !== $t_n && false !== mb_stripos( $bloco_saida, $rot_t[ $t_n ] ) ) {
		$erros_saida[] = 'oferece ' . $rot_t[ $t_n ] . ', que nao e porosa';
	}
}
f2_ok( empty( $erros_saida ), 'a saida oferecida bate com a classificacao do esquema, nas duas direcoes',
	empty( $erros_saida ) ? count( $esquema['superficies_porosas']['tesselas_porosas'] ) . ' porosas nomeadas'
		: implode( ' | ', $erros_saida ) );
f2_ok( false === mb_strpos( $plastico, 'Nenhum dos adesivos do nosso banco é declarado' ),
	'plastico com caquinho liso: a pagina NAO nega a declaracao que ela mesma cita' );
$plastico_poroso = f2_texto( f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_ceramica' ) ) );
f2_ok( false !== mb_strpos( $plastico_poroso, 'Cascola Adesivo de Montagem PL500 Interior' ),
	'plastico com caquinho poroso: a faixa que estava descoberta responde' );
f2_ok( false === mb_strpos( $plastico_poroso, 'Não temos cola para indicar' ),
	'plastico com caquinho poroso: a pagina nao diz que nao sabe o que ela sabe' );
f2_ok( false !== mb_strpos( $plastico_poroso, 'somos nós, não ela' ),
	'a atribuicao fica dividida: a condicao e do fabricante, a classificacao e nossa (26.3)' );
/* DECLARACAO VAGA NAO E SILENCIO, e a pagina separa as duas. Dizer "o
   fabricante nao fala" de um produto cujo fabricante escreveu "certos tipos de
   plastico" seria falso: ele falou, e falou de um jeito que nao decide. */
f2_ok( false !== mb_strpos( $plastico, 'certos tipos de plástico' )
	&& false !== mb_strpos( $plastico, 'não nomeia material nenhum' ),
	'a declaracao vaga aparece separada do silencio, com a frase do fabricante' );
/* CONTATO PERMANENTE COM AGUA: aberto em ceramica e SO em ceramica. As duas
   afirmacoes sao o par que impede a faixa de parecer maior do que e. */
$submerso = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua' ) ) );
f2_ok( false !== mb_strpos( $submerso, 'Tekbond Silicone Acético Maxx' ),
	'o estado submerso em ceramica responde: a faixa de nivel 4 virou faixa de nivel 3' );
f2_ok( false === mb_strpos( $submerso, 'Não temos cola para indicar' ),
	'o estado submerso em ceramica nao diz mais que a ilha nao sabe' );
$submerso_vidro = f2_texto( f2_corpo( f2_render( $raiz, 'base=vidro&onde=contato_permanente_agua' ) ) );
f2_ok( false !== mb_strpos( $submerso_vidro, 'Não temos cola para indicar' ),
	'a mesma agua sobre VIDRO continua descoberta — o fabricante nomeia ceramica, nao vidro' );

/* ---------------------------------------------------------------------------
 * Fecho
 * ------------------------------------------------------------------------- */

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

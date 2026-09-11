<?php
/**
 * O PORTAO DA VOZ E DO NOME — as nove paginas, um processo por pagina.
 *
 *   php ferramentas/teste-voz.php .
 *
 * ---------------------------------------------------------------------------
 * POR QUE ELE EXISTE
 * ---------------------------------------------------------------------------
 *
 * Duas familias de defeito, achadas juntas em 11/09/2026, e as duas sao a mesma
 * coisa vista de dois angulos: METADES QUE NAO SE FALAM.
 *
 * (1) SEIS DAS NOVE PAGINAS TINHAM DOIS NOMES. O og:title publicava "Quem
 *     publica a Robometria" e o H1, na mesma pagina, dizia "Sobre". O artigo do
 *     filtro universal se chamava "Por que nao existe filtro universal de robo
 *     aspirador" no H1 e "Existe filtro universal de robo aspirador?" no cartao
 *     compartilhado. Ninguem errou: eram dois mapas digitados, cada um certo no
 *     seu lugar, e nenhum podia corrigir o outro — a mesma forma da coluna
 *     "Temos hoje" digitada ao lado de um banco que ja dizia outra coisa.
 *
 * (2) A VOZ PAROU NA HOME. A casca 1.2.0 reescreveu a home e o cabecalho pelo
 *     VOZ.md, e o teste que nasceu com ela media o titulo da raiz e o primeiro
 *     paragrafo da home. As outras oito paginas nunca foram medidas: duas
 *     ferramentas abriam com "Esta ferramenta responde…" e duas paginas
 *     institucionais abriam falando do site em terceira pessoa.
 *
 * ---------------------------------------------------------------------------
 * AS QUATRO DECISOES DE MEDICAO
 * ---------------------------------------------------------------------------
 *
 * 1. A REGUA E DESTE ARQUIVO. Ele nao chama a funcao da casca que decide o que
 *    a pagina publica para conferir o que a pagina publicou — le o HTML SERVIDO
 *    e compara com o nome canonico lido da fonte unica, uma vez. Trocar a regra
 *    num lugar so tem que fazer este teste reprovar, nunca errar junto.
 * 2. UM PROCESSO POR PAGINA. O `static` da marca do cabecalho (e qualquer outro
 *    residuo) faz a segunda pagina de um mesmo processo sair pela metade. Custa
 *    segundos; medir a metade errada custa um bloco.
 * 3. AFIRMACAO SOBRE TEXTO SE MEDE NO CORPO, e o que e camada de prova a PAGINA
 *    declara no markup (classe `rbm-prova`), nunca a vizinhanca das palavras.
 *    E para a declaracao nao virar porta dos fundos, ela vem com contrapartida:
 *    a linha-mestra NUNCA pode ser um bloco de prova, os blocos marcados sao
 *    contados e impressos um a um, e sao poucos.
 * 4. NENHUMA PAGINA MEDIDA PODE ESTAR NO ESTADO DEGRADADO. Toda pagina desta
 *    ilha tem um segundo estado valido ("estamos sem o banco") com cabecalho,
 *    rodape e prosa. Foi medindo tres desses estados que a varredura de corpo
 *    passou dois dias dando verde sobre paginas de 1.100 caracteres. A marca
 *    `rbm-sem-banco` existe so para isto, e aqui ela reprova.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

/* ---------------------------------------------------------------------------
 * O caminho de UM estado: monta a pagina e imprime o que foi medido nela, em
 * JSON, para o processo-pai comparar. Nada e afirmado aqui dentro.
 * ------------------------------------------------------------------------- */
if ( in_array( '--medir', $argv, true ) ) {
	$alvo = '';
	foreach ( $argv as $a ) {
		if ( 0 === strpos( $a, '--alvo=' ) ) { $alvo = substr( $a, strlen( '--alvo=' ) ); }
	}

	require __DIR__ . '/render-para-teste.php';
	robometria_teste_carregar_options( $raiz );
	robometria_teste_carregar( $raiz );
	$GLOBALS['__paginas'] = robometria_teste_paginas_do_site();
	add_filter( $alvo . '_na_pagina', function () { return true; } );

	$html = robometria_teste_pagina( $alvo, null, robometria_teste_slug_do_alvo( $alvo ) );

	/* O CORPO, e so o corpo: sem <script>, sem <style>, sem marcacao, entidades
	   desfeitas. E o que um leitor le e o que um modelo de linguagem cita. */
	$corpo_html = $html;
	if ( preg_match( '#<main[^>]*>(.*)</main>#is', $html, $m ) ) { $corpo_html = $m[1]; }

	/* A LINHA-MESTRA e o primeiro paragrafo do corpo, seja ele qual for — e e de
	   proposito que este teste pegue o PRIMEIRO <p>, e nao o primeiro com a
	   classe certa: se alguem mudar a ordem e puser prosa antes da linha-mestra,
	   quem abre a pagina passa a ser a prosa, e a medicao tem que enxergar isso. */
	$primeiro = '';
	$primeiro_e_prova = false;
	if ( preg_match( '#<p\b([^>]*)>(.*?)</p>#is', $corpo_html, $mp ) ) {
		$primeiro         = trim( html_entity_decode( preg_replace( '#<[^>]+>#s', '', $mp[2] ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) );
		$primeiro         = trim( preg_replace( '/\s+/u', ' ', $primeiro ) );
		$primeiro_e_prova = (bool) preg_match( '#\brbm-prova\b#', $mp[1] );
	}

	$provas = array();
	if ( preg_match_all( '#<p[^>]*class="[^"]*\brbm-prova\b[^"]*"[^>]*>(.*?)</p>#is', $corpo_html, $mpr ) ) {
		foreach ( $mpr[1] as $t ) {
			$t = trim( preg_replace( '/\s+/u', ' ', html_entity_decode( preg_replace( '#<[^>]+>#s', '', $t ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) );
			$provas[] = $t;
		}
	}

	preg_match( '#<title>(.*?)</title>#is', $html, $mt );
	preg_match( '#<h1[^>]*>(.*?)</h1>#is', $html, $mh );
	preg_match( '#<meta property="og:title" content="([^"]*)"#i', $html, $mo );

	/* O degrau ATUAL da trilha: o ultimo item, o unico sem <a>. */
	$degrau = '';
	if ( preg_match( '#<nav[^>]*class="[^"]*rbm-trilha[^"]*"[^>]*>(.*?)</nav>#is', $html, $mn ) ) {
		if ( preg_match_all( '#<li[^>]*>(.*?)</li>#is', $mn[1], $ml ) ) {
			$ultimo = end( $ml[1] );
			$degrau = trim( html_entity_decode( preg_replace( '#<[^>]+>#s', '', $ultimo ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) );
		}
	}

	$corpo_texto = preg_replace( '#<script\b[^>]*>.*?</script>#is', ' ', $corpo_html );
	$corpo_texto = preg_replace( '#<style\b[^>]*>.*?</style>#is', ' ', $corpo_texto );
	$corpo_texto = trim( preg_replace( '/\s+/u', ' ', html_entity_decode( preg_replace( '#<[^>]+>#s', ' ', $corpo_texto ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) );

	echo wp_json_encode( array(
		'titulo'           => isset( $mt[1] ) ? html_entity_decode( $mt[1], ENT_QUOTES | ENT_HTML5, 'UTF-8' ) : '',
		'h1'               => isset( $mh[1] ) ? trim( html_entity_decode( preg_replace( '#<[^>]+>#s', '', $mh[1] ), ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) : '',
		'og'               => isset( $mo[1] ) ? html_entity_decode( $mo[1], ENT_QUOTES | ENT_HTML5, 'UTF-8' ) : '',
		'degrau'           => $degrau,
		'primeiro'         => $primeiro,
		'primeiro_e_prova' => $primeiro_e_prova,
		'provas'           => $provas,
		'corpo'            => $corpo_texto,
		'sem_banco'        => (bool) preg_match( '#class="[^"]*\brbm-sem-banco\b#', $html ),
	) );
	exit( 0 );
}

/* ---------------------------------------------------------------------------
 * O caminho do PAI: carrega o que a ilha declara, manda medir cada pagina num
 * processo proprio e afirma.
 * ------------------------------------------------------------------------- */

require __DIR__ . '/render-para-teste.php';
robometria_teste_carregar_options( $raiz );
robometria_teste_carregar( $raiz );

$falhas = 0;
$total  = 0;
function voz_ok( $condicao, $rotulo, $medido = '' ) {
	global $falhas, $total;
	$total++;
	if ( $condicao ) {
		printf( "  ok   %-64s %s\n", $rotulo, $medido );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-63s %s\n", $rotulo, $medido );
	return false;
}

/* A LISTA DE PROIBIDAS SAI DO VOZ.md, nao deste arquivo.
 *
 * Copiar a lista para ca seria a segunda copia da regra, que e o defeito que
 * este teste existe para nao ter. O VOZ.md e a declaracao — quem muda a voz da
 * ilha muda um arquivo so, e o portao acompanha. */
$voz = file_get_contents( $raiz . '/VOZ.md' );
if ( false === $voz ) {
	fwrite( STDERR, "VOZ.md nao encontrado — ilha sem VOZ.md nao recebe bloco (secao 15.1)\n" );
	exit( 2 );
}
$proibidas = array();
if ( preg_match( '#Nunca no título nem no primeiro parágrafo:(.*?)\n#u', $voz, $mv ) ) {
	if ( preg_match_all( '#"([^"]+)"#u', $mv[1], $mt2 ) ) { $proibidas = $mt2[1]; }
}
/* A secao "Proibidas" traz FRASES inteiras. Delas o teste guarda o comeco — as
   seis primeiras palavras —, porque e o comeco que caracteriza a forma
   ("Esta ferramenta cruza a matriz de compatibilidade..."), e cobrar a frase
   inteira seria cobrar que alguem a repetisse palavra por palavra, coisa que
   nunca acontece. */
if ( preg_match( '~\n## Proibidas\n(.*?)\n## ~su', $voz . "\n## ", $mp2 ) ) {
	if ( preg_match_all( '~- "([^"…]+)~u', $mp2[1], $mt3 ) ) {
		foreach ( $mt3[1] as $frase ) {
			$palavras = preg_split( '/\s+/u', trim( $frase ) );
			$inicio   = implode( ' ', array_slice( $palavras, 0, 6 ) );
			if ( mb_strlen( $inicio ) > 12 ) { $proibidas[] = $inicio; }
		}
	}
}

echo "PORTAO DA VOZ E DO NOME — Robometria\n";
echo str_repeat( '=', 78 ) . "\n";
echo "\nTermos proibidos lidos do VOZ.md: " . count( $proibidas ) . "\n";
foreach ( $proibidas as $p ) { echo "  · $p\n"; }

/* O NOME CANONICO, lido da fonte unica da casca. */
$nomes = robometria_casca_nomes_das_paginas();

$alvo_do_slug = array();
foreach ( array( 'robometria_home', 'robometria_ferramentas', 'robometria_metodologia',
	'robometria_sobre', 'robometria_afiliados', 'robometria_r1', 'robometria_r2',
	'robometria_a1', 'robometria_a2' ) as $alvo ) {
	$slug = robometria_teste_slug_do_alvo( $alvo );
	$alvo_do_slug[ $slug ] = $alvo;
}

/* AS DUAS DIRECOES, e esta e a trava que a cicatriz do cartao que dizia zero
   deixou: pagina nomeada sem render medido, e render medido sem nome. */
echo "\n1. Toda pagina nomeada e medida, e toda pagina medida tem nome\n";
$sem_render = array_diff( array_keys( $nomes ), array_keys( $alvo_do_slug ) );
$sem_nome   = array_diff( array_keys( $alvo_do_slug ), array_keys( $nomes ) );
voz_ok( empty( $sem_render ), 'nenhuma pagina nomeada fica fora da medicao', empty( $sem_render ) ? count( $nomes ) . ' paginas' : implode( ' ', $sem_render ) );
voz_ok( empty( $sem_nome ), 'nenhuma pagina medida fica sem nome canonico', empty( $sem_nome ) ? 'ok' : implode( ' ', $sem_nome ) );

/* AS MARCAS E OS CODIGOS DO BANCO — a regua de "procedencia nao abre pagina".
   Sai do banco, nao de uma lista digitada: marca nova entra na regra sozinha. */
$marcas_json = json_decode( file_get_contents( $raiz . '/dados/marcas.json' ), true );
$pecas_json  = json_decode( file_get_contents( $raiz . '/dados/pecas.json' ), true );
$publicadores = array();
foreach ( (array) ( isset( $marcas_json['registros'] ) ? $marcas_json['registros'] : array() ) as $m ) {
	foreach ( array( 'nome', 'publicador' ) as $campo ) {
		if ( ! empty( $m[ $campo ] ) ) {
			$nome_marca = trim( preg_replace( '#\(.*?\)#', '', (string) $m[ $campo ] ) );
			if ( mb_strlen( $nome_marca ) >= 3 ) { $publicadores[ $nome_marca ] = true; }
		}
	}
}
$publicadores = array_keys( $publicadores );

$codigos = array();
foreach ( (array) ( isset( $pecas_json['registros'] ) ? $pecas_json['registros'] : array() ) as $p ) {
	if ( ! empty( $p['codigo_fabricante'] ) && preg_match( '#^[A-Z0-9][A-Z0-9\-]{3,}$#', (string) $p['codigo_fabricante'] ) ) {
		$codigos[] = (string) $p['codigo_fabricante'];
	}
	foreach ( (array) ( isset( $p['compatibilidade'] ) ? $p['compatibilidade'] : array() ) as $c ) {
		if ( ! empty( $c['codigo_declarado'] ) && preg_match( '#^[A-Z0-9][A-Z0-9\-]{3,}$#', (string) $c['codigo_declarado'] ) ) {
			$codigos[] = (string) $c['codigo_declarado'];
		}
	}
}
$codigos = array_values( array_unique( $codigos ) );
echo "   (regua de procedencia: " . count( $publicadores ) . " publicadores e " . count( $codigos ) . " codigos, lidos do banco)\n";

/* A ABERTURA NAO NOMEIA A PROPRIA PAGINA — lista fechada, casada no COMECO.
   "Esta ferramenta responde…" e "A Robometria e um banco de…" sao a mesma frase
   com sujeitos diferentes: as duas falam do site para quem entrou querendo
   falar do proprio robo. Casar so no comeco e o que separa isso de heuristica
   por vizinhanca — "a Robometria transcreveu" no meio de uma tese medida e
   procedencia legitima, e continua passando. */
$aberturas_de_si = array(
	'Esta ferramenta', 'Este artigo', 'Este texto', 'Esta pagina', 'Esta página',
	'Este site', 'A Robometria', 'O Robometria', 'Nosso ', 'Nossa ', 'Aqui na Robometria',
);

$teto_nome = 65 - mb_strlen( ' – Robometria' );

/* NOME DE GAVETA — lista fechada, casada no nome INTEIRO.
 *
 * Com uma fonte so de nome, a coerencia entre as cinco superficies deixa de
 * pegar o defeito mais comum de todos: rebatizar a pagina com o nome da pasta.
 * "Sobre" muda H1, <title>, og:title, trilha e cartao de uma vez, todos
 * concordando — e a secao 14.5 do contrato diz que titulo e H1 sao a pergunta
 * que a pessoa digita, nunca o nome interno. Entao a regra de voz sobre o NOME
 * e uma lista fechada, e ela casa o nome inteiro: "As duas ferramentas" passa,
 * "Ferramentas" nao. Lista, e nao heuristica de tamanho, porque nome curto pode
 * ser otimo e nome longo pode ser gaveta com adjetivo. */
$nomes_de_gaveta = array(
	'Início', 'Inicio', 'Home', 'Sobre', 'Sobre nós', 'Contato', 'Ferramentas',
	'Metodologia', 'Divulgação de afiliados', 'Blog', 'Artigos', 'Guias',
	'Página inicial', 'Serviços', 'Produtos',
);

foreach ( $alvo_do_slug as $slug => $alvo ) {
	$nome = isset( $nomes[ $slug ] ) ? $nomes[ $slug ] : '';
	echo "\n[$slug] $nome\n";

	$saida = array();
	$codigo = 0;
	exec( PHP_BINARY . ' ' . escapeshellarg( __FILE__ ) . ' ' . escapeshellarg( $raiz )
		. ' --medir --alvo=' . escapeshellarg( $alvo ) . ' 2>&1', $saida, $codigo );
	if ( 0 !== $codigo ) {
		voz_ok( false, 'a pagina foi montada', 'processo saiu com ' . $codigo . ': ' . implode( ' ', $saida ) );
		continue;
	}
	$m = json_decode( implode( '', $saida ), true );
	if ( ! is_array( $m ) ) {
		voz_ok( false, 'a pagina foi montada', 'saida ilegivel' );
		continue;
	}

	/* 0. A pagina medida e a pagina, e nao o aviso de que o banco nao chegou. */
	voz_ok( ! $m['sem_banco'], 'a pagina medida NAO e o estado degradado', $m['sem_banco'] ? 'rbm-sem-banco servido' : 'ok' );
	voz_ok( mb_strlen( $m['corpo'] ) >= 1500, 'corpo com 1.500 caracteres ou mais', mb_strlen( $m['corpo'] ) . ' caracteres' );

	/* 1. UM NOME, nas superficies em que ele aparece. */
	voz_ok( '' !== $nome, 'a pagina tem nome canonico' );
	voz_ok( $m['h1'] === $nome, 'o H1 e o nome canonico', $m['h1'] );
	voz_ok( $m['og'] === $nome, 'o og:title e o nome canonico', $m['og'] );
	if ( 'inicio' !== $slug ) {
		voz_ok( $m['degrau'] === $nome, 'o degrau atual da trilha e o nome canonico', $m['degrau'] );
	} else {
		voz_ok( '' === $m['degrau'], 'a home nao tem trilha (16.3)', $m['degrau'] );
	}

	/* 2. O <title>: o nome mais a marca, dentro do teto. */
	voz_ok( $m['titulo'] === $nome . ' – Robometria', 'o <title> e o nome mais a marca', $m['titulo'] );
	voz_ok( mb_strlen( $m['titulo'] ) <= 65, 'o <title> cabe em 65 caracteres', mb_strlen( $m['titulo'] ) . ' caracteres' );
	voz_ok( mb_strlen( $nome ) <= $teto_nome, 'o nome cabe no teto do <title>', mb_strlen( $nome ) . ' de ' . $teto_nome );

	$gaveta = false;
	foreach ( $nomes_de_gaveta as $g ) {
		if ( 0 === strcasecmp( trim( $nome ), $g ) ) { $gaveta = true; break; }
	}
	voz_ok( ! $gaveta, 'o nome nao e o nome da gaveta (secao 14.5)', $gaveta ? $nome : 'ok' );

	/* 3. A VOZ no nome e na linha-mestra. */
	$achados = array();
	foreach ( $proibidas as $p ) {
		if ( false !== mb_stripos( $nome, $p ) ) { $achados[] = 'nome: ' . $p; }
		if ( false !== mb_stripos( $m['primeiro'], $p ) ) { $achados[] = 'abertura: ' . $p; }
	}
	voz_ok( empty( $achados ), 'nenhum termo proibido no nome nem na abertura', empty( $achados ) ? 'ok' : implode( ' | ', $achados ) );

	voz_ok( '' !== $m['primeiro'], 'a pagina tem linha-mestra' );
	voz_ok( ! $m['primeiro_e_prova'], 'a linha-mestra NAO e bloco de prova', $m['primeiro_e_prova'] ? 'rbm-prova na abertura' : 'ok' );

	$abre_de_si = '';
	foreach ( $aberturas_de_si as $inicio ) {
		if ( 0 === mb_stripos( $m['primeiro'], $inicio ) ) { $abre_de_si = $inicio; break; }
	}
	voz_ok( '' === $abre_de_si, 'a abertura nao comeca nomeando a propria pagina', '' === $abre_de_si ? mb_substr( $m['primeiro'], 0, 44 ) . '…' : $abre_de_si );

	voz_ok( (bool) preg_match( '#\b(você|voce|seu|sua|seus|suas)\b#ui', $m['primeiro'] ),
		'a abertura fala com quem entrou (segunda pessoa)', mb_substr( $m['primeiro'], 0, 44 ) . '…' );

	/* 4. PROCEDENCIA NAO ABRE PAGINA (15.2): nome de fabricante, data de leitura
	      e codigo de peca moram na camada de prova, um paragrafo abaixo. */
	$proc = array();
	foreach ( $publicadores as $pub ) {
		if ( preg_match( '#\b' . preg_quote( $pub, '#' ) . '\b#ui', $m['primeiro'] ) ) { $proc[] = $pub; }
	}
	foreach ( $codigos as $cod ) {
		if ( preg_match( '#\b' . preg_quote( $cod, '#' ) . '\b#u', $m['primeiro'] ) ) { $proc[] = $cod; }
	}
	if ( preg_match( '#\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b#', $m['primeiro'], $md2 ) ) { $proc[] = $md2[0]; }
	voz_ok( empty( $proc ), 'procedencia NAO abre a pagina (sem marca, codigo nem data)', empty( $proc ) ? 'ok' : implode( ' ', $proc ) );

	/* 5. A EXCECAO E CONTADA E MOSTRADA, uma a uma. Excecao que some sem ser
	      conferida aceita qualquer coisa. */
	voz_ok( count( $m['provas'] ) <= 3, 'poucos blocos de prova na pagina', count( $m['provas'] ) . ' bloco(s)' );
	foreach ( $m['provas'] as $i => $t ) {
		echo '       prova ' . ( $i + 1 ) . ': ' . mb_substr( $t, 0, 96 ) . "…\n";
	}
}

echo "\n" . str_repeat( '=', 78 ) . "\n";
if ( $falhas ) {
	echo "REPROVADO: $total afirmacoes, $falhas falha(s).\n";
	exit( 1 );
}
echo "APROVADO: $total afirmacoes, 0 falha(s).\n";
exit( 0 );

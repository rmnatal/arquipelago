<?php
/**
 * Imprime, em JSON, TODA constante `AQUAMETRIA_*` que os snippets desta ilha
 * definem — e as imprime perguntando ao PHP, nao relendo o texto do `define()`.
 *
 *   php ferramentas/listar-constantes-do-snippet.php .
 *
 * POR QUE ELE EXISTE, e a data e 19/10/2026
 * -----------------------------------------
 * O achado 11 do fecho das 17h04Z desta ilha, deixado sem conserto de proposito
 * pela 19.2: *"esta passada mediu UMA constante compartilhada — o teto do
 * titulo — e nao perguntou se ha outras. Quantas OUTRAS constantes de snippet
 * os portoes desta pasta redigitam hoje e uma pergunta que ninguem fez, e a
 * resposta dela decide se generalizar a varredura vale um bloco. Quem a tomar
 * comeca contando, nao generalizando."*
 *
 * Este arquivo e o COMECO DA CONTAGEM: ele e o `listar-teto-do-titulo.php` com
 * o alvo aberto. Aquele nomeia tres constantes e as devolve; este devolve as
 * que existirem, sem lista nenhuma aqui dentro — o mesmo desenho da
 * `bancada.py` desta pasta, em que a pergunta e feita aos ARQUIVOS e nunca a
 * uma lista escrita a mao. Constante nova num snippet entra na contagem no dia
 * em que e definida, sem ninguem a inscrever.
 *
 * O CAMINHO E O (b), IGUAL AO DO IRMAO MAIS VELHO
 * -----------------------------------------------
 * `get_defined_constants()` depois de carregar os snippets, nunca uma expressao
 * regular sobre o texto do `define()`. O motivo esta escrito no
 * `listar-promessas.php` e vale igual aqui: a regex leria o TEXTO do arquivo e
 * nao o valor que o site usa, e ficaria verde no dia em que alguem definisse a
 * constante antes, por cima do `if ( ! defined( ... ) )`.
 *
 * E ELE DECLARA O QUE NAO CONSEGUE PERGUNTAR, QUE E A METADE HONESTA
 * ------------------------------------------------------------------
 * O `aquametria_teste_carregar()` PULA dois snippets de proposito — o
 * `aquametria-sync.php` e o `aquametria-atualizador-sync.php`, porque os dois
 * falam com o WordPress de verdade. As constantes deles existem no ar e NAO
 * aparecem aqui. Imprimir so o que carregou faria a contagem dizer "estas sao
 * as constantes da ilha" quando o certo e "estas sao as que deu para
 * perguntar" — e a diferenca e exatamente o tipo de silencio que o achado 11
 * descreve. Entao a saida traz `snippets_lidos` e `snippets_pulados`, e quem
 * varre o repositorio usa a segunda lista para dizer NAO MEDIDO em vez de zero.
 *
 * ELE NAO AFIRMA NADA E NAO VARRE NADA. Devolve as constantes e para. Quem
 * pergunta por elas em Python e a `regua-constantes-de-snippet.py`; quem a
 * exercita e o `teste-constantes-de-snippet.py`; quem a mutila e o
 * `mutacoes-constantes-de-snippet.py`.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'inicio';
$GLOBALS['__paginas']     = array();

/* Retrato de ANTES: o que ja estava definido nao e desta ilha e nao entra na
   contagem. Sem isto, uma constante do proprio PHP com este prefixo entraria. */
$antes = get_defined_constants();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

$depois = get_defined_constants();

/* Quais arquivos o carregador leu e quais ele pulou — medido do disco e da
   mesma regra que ele usa, nunca digitado aqui. Se o carregador passar a ler um
   deles, esta lista encolhe sozinha. */
$pulados = array( 'aquametria-sync.php', 'aquametria-atualizador-sync.php' );
$lidos   = array();
$nao     = array();
foreach ( glob( $raiz . '/snippets/*.php' ) as $arquivo ) {
	$base = basename( $arquivo );
	if ( in_array( $base, $pulados, true ) ) {
		$nao[] = $base;
	} else {
		$lidos[] = $base;
	}
}

$constantes = array();
foreach ( $depois as $nome => $valor ) {
	if ( strpos( $nome, 'AQUAMETRIA_' ) !== 0 ) {
		continue;
	}
	if ( array_key_exists( $nome, $antes ) ) {
		continue;
	}
	/* O TIPO VIAJA JUNTO, e nao e enfeite: quem varre precisa saber se o valor e
	   numero ou texto para decidir se `= 65` e `= '65'` sao a mesma coisa. */
	$constantes[ $nome ] = array(
		'valor' => $valor,
		'tipo'  => is_bool( $valor ) ? 'booleano' : ( is_int( $valor ) || is_float( $valor ) ? 'numero' : gettype( $valor ) ),
	);
}

if ( ! $constantes ) {
	fwrite( STDERR, "FALHA: nenhuma constante AQUAMETRIA_* apos carregar os snippets de " . $raiz . "\n" );
	exit( 1 );
}

ksort( $constantes );

echo json_encode(
	array(
		'constantes'       => $constantes,
		'snippets_lidos'   => $lidos,
		'snippets_pulados' => $nao,
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT
), "\n";

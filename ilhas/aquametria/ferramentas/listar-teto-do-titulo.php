<?php
/**
 * Imprime, em JSON, as TRES CONSTANTES que montam o `<title>` desta ilha — e as
 * imprime perguntando ao proprio snippet, nao relendo o texto dele.
 *
 *   php ferramentas/listar-teto-do-titulo.php .
 *
 * POR QUE ELE EXISTE, e a data e 19/10/2026
 * -----------------------------------------
 * O achado 11 do fecho das 13h27Z desta ilha, deixado sem conserto de proposito
 * pela 19.2: *"o teto de 65 esta digitado A MAO em QUATRO arquivos desta pasta
 * (...) o teto e definido num lugar so, o AQUAMETRIA_TITULO_TETO do snippet. No
 * dia em que o Google mudar o corte, tres arquivos vao continuar dizendo 65 e
 * ninguem vai ser avisado. Quem consertar LE o teto do snippet, nao o
 * redigita."*
 *
 * A VARREDURA DESTA PASSADA ACHOU MAIS DO QUE O ACHADO DIZIA, e esta escrito
 * aqui para a conta nao ser refeita de cabeca: sao CINCO arquivos e nao quatro
 * (o `teste-titulo-no-ar.py` tambem tem `TETO = 65`), SEIS posicoes afirmativas
 * (o `teste-voz.mjs` mede o teto DUAS vezes, uma delas com o literal `65`
 * escrito na propria afirmacao da linha 363), e a divida nao e so do teto: o
 * SEPARADOR e a MARCA sao redigitados do mesmo jeito — `SEPARADOR = ' – '` e
 * `MARCA = 'Aquametria'` no `teste-promessa-do-titulo.py`, e
 * `CAUDA = " – Aquametria"` no `teste-titulos-das-duas-fontes.py`. As tres
 * constantes nascem no mesmo trecho do `aquametria-seo-tecnico.php` e as tres
 * tem o mesmo defeito, entao as tres saem por esta porta. Consertar uma e
 * deixar duas seria reescrever o achado em vez de fecha-lo.
 *
 * O CAMINHO E O (b) DO `listar-promessas.php`, e por escolha
 * ---------------------------------------------------------
 * Aquele arquivo escreveu a regra para o numero da promessa e ela vale igual
 * para o teto: *"(a) reimplementar a conta (...) e entao as DUAS metades erram
 * juntas (...); (b) PERGUNTAR ao snippet"*. Uma expressao regular sobre o texto
 * do `define()` seria o (a) com outra roupa — ela leria o texto do arquivo e
 * nao o valor que o site usa, e ficaria verde no dia em que alguem definisse a
 * constante antes, por cima do `if ( ! defined( ... ) )`. Aqui quem resolve a
 * constante e o PHP, como no ar.
 *
 * ELE NAO AFIRMA NADA E NAO MEDE TAMANHO. Devolve as tres constantes e para.
 * Quem pergunta por elas em Python e a `regua-teto-do-titulo.py`; quem a
 * exercita e o `teste-teto-do-titulo.py`; quem a mutila e o
 * `mutacoes-teto-do-titulo.py`.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$GLOBALS['__raiz_ilha']   = $raiz;
$GLOBALS['__slug_pagina'] = 'inicio';
$GLOBALS['__paginas']     = array();

require __DIR__ . '/render-para-teste.php';
aquametria_teste_carregar( $raiz );

/* Constante que nao foi definida e ausencia de resposta, nunca um padrao: quem
   chamar este arquivo tem de reprovar alto, e nao herdar um 65 de consolo. E a
   lição do proprio achado — o valor de consolo e o que faz o defeito ser
   silencioso. */
$faltando = array();
foreach ( array( 'AQUAMETRIA_TITULO_TETO', 'AQUAMETRIA_TITULO_SEPARADOR', 'AQUAMETRIA_TITULO_MARCA' ) as $c ) {
	if ( ! defined( $c ) ) {
		$faltando[] = $c;
	}
}
if ( $faltando ) {
	fwrite( STDERR, 'FALHA: constante nao definida apos carregar os snippets: ' . implode( ', ', $faltando ) . "\n" );
	exit( 1 );
}

echo json_encode(
	array(
		'teto'      => AQUAMETRIA_TITULO_TETO,
		'separador' => AQUAMETRIA_TITULO_SEPARADOR,
		'marca'     => AQUAMETRIA_TITULO_MARCA,
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT
), "\n";

<?php
/**
 * O teste que teria pego o defeito de 08/09/2026, e que existe para que ele
 * nunca mais passe.
 *
 * O que ele afirma, para CADA calculadora publicada:
 *
 *   1. o retorno do shortcode NAO tem <script> nem <style> — porque tudo que
 *      volta do shortcode ainda atravessa os filtros de texto do conteudo do
 *      WordPress, que trocam "&" por "&#038;";
 *   2. a pagina montada (cabeca + conteudo escapado + rodape) NAO tem nenhum
 *      "&#038;" dentro de <script> ou de <style>;
 *   3. o operador "&&" chega inteiro ao navegador;
 *   4. o <script> vem depois do HTML do formulario, e o <style> vem antes;
 *   5. o formulario e os conteineres de saida e de produto existem no HTML.
 *
 *   php ferramentas/teste-escape-shortcode.php .
 */
require __DIR__ . '/render-para-teste.php';

$raiz = isset($argv[1]) ? $argv[1] : dirname(__DIR__);
aquametria_teste_carregar($raiz);

$calculadoras = array(
	'C1'  => array('aquametria_calculadora_litragem',   'aqm-c1'),
	'C3'  => array('aquametria_calculadora_vazao',      'aqm-c3'),
	'C5'  => array('aquametria_calculadora_aquecedor',  'aqm-c5'),
	'C12' => array('aquametria_calculadora_midia',      'aqm-c12'),
	'C15' => array('aquametria_calculadora_iluminacao', 'aqm-c15'),
);

$falhas = 0;
function afirmar($nome, $cond, $extra = '') {
	global $falhas;
	printf("  %-5s %s%s\n", $cond ? 'ok' : 'FALHA', $nome, $extra !== '' ? ' — ' . $extra : '');
	if (!$cond) { $falhas++; }
}

function trechos($html, $tag) {
	preg_match_all('#<' . $tag . '\b[^>]*>(.*?)</' . $tag . '>#s', $html, $m);
	return $m[1];
}

foreach ($calculadoras as $codigo => $par) {
	list($tag, $classe) = $par;
	echo "\n$codigo — [$tag]\n";

	aquametria_teste_rebobinar();
	$html = aquametria_teste_pagina($tag);

	/* 1. o retorno cru do shortcode, guardado pelo montador da pagina */
	$cru = $GLOBALS['__retorno_shortcode'];
	afirmar('retorno do shortcode sem <script>', false === strpos($cru, '<script'));
	afirmar('retorno do shortcode sem <style>',  false === strpos($cru, '<style'));

	/* 2 e 3. nada escapado dentro de script ou style */
	$escapes = 0;
	foreach (array('script', 'style') as $t) {
		foreach (trechos($html, $t) as $bloco) {
			$escapes += substr_count($bloco, '&#038;');
		}
	}
	afirmar('zero &#038; dentro de <script> e <style>', 0 === $escapes, $escapes . ' encontrados');

	$js = implode("\n", trechos($html, 'script'));
	afirmar('script da calculadora presente', '' !== trim($js), strlen($js) . ' bytes');
	afirmar('operador && intacto no script', substr_count($js, '&&') > 0, substr_count($js, '&&') . ' ocorrencias');

	/* 4. ordem: estilo antes do formulario, script depois */
	$pos_style = strpos($html, '<style id="aquametria-' . substr($classe, 4) . '-estilo"');
	$pos_form  = strpos($html, 'class="' . $classe . '"');
	$pos_js    = strpos($html, '<script id="aquametria-' . substr($classe, 4) . '-script"');
	afirmar('estilo antes do HTML', false !== $pos_style && false !== $pos_form && $pos_style < $pos_form);
	afirmar('script depois do HTML', false !== $pos_js && false !== $pos_form && $pos_js > $pos_form);

	/* 5. as pecas que o JavaScript precisa achar */
	afirmar('div raiz .' . $classe . ' no corpo', false !== $pos_form);
	afirmar('formulario no corpo', false !== strpos($html, '<form'));
}

echo "\n" . ($falhas ? "$falhas FALHA(S)\n" : "Todas as afirmacoes passaram.\n");
exit($falhas ? 1 : 0);

<?php
/**
 * TESTE DA NOTA DO PRECO — O ITEM 3 DO DESPACHO DE 30/10/2026.
 *
 * O DEFEITO: dois cartoes do bloco de compra da F2 serviam, lado a lado,
 * "R$ 8.244,00 na Mercado Livre, lido em 27/10/2026" e o botao "Ver ofertas na
 * Shopee". O leitor recebia um preco com procedencia e data e um botao que nao
 * serve aquele preco. Nao e a escolha da loja que estava errada — a regra de
 * dinheiro desta ilha manda preferir o link da Shopee, e a cotacao do Mercado
 * Livre e a unica com procedencia que estes registros tem. Era a FRASE.
 *
 * ESTE PORTAO E PHP porque a frase e decidida em PHP, e a secao 8 do
 * ARQUIPELAGO.md e literal: quem confere escreve a propria regua. Uma regua em
 * Python sobre o texto do PHP conferiria a FORMA do arquivo; esta CHAMA a
 * funcao e le a frase que o leitor recebe.
 *
 * E ELE SE PROVA ANTES DE JULGAR: o primeiro caso da bateria e a frase que
 * estava NO AR em 30/10/2026, e ela TEM de ser reprovada. Portao que nao
 * reprova o defeito que o fez nascer e portao inerte, e a bancada desta ilha
 * nomeia inerte com essa palavra.
 */

foreach (array('add_filter', 'add_action', 'add_shortcode', 'register_activation_hook') as $f) {
	if (!function_exists($f)) { eval("function $f(){ return true; }"); }
}
if (!function_exists('esc_html')) {
	function esc_html($s) { return htmlspecialchars((string) $s, ENT_QUOTES); }
	function esc_attr($s) { return htmlspecialchars((string) $s, ENT_QUOTES); }
	function esc_url($s) { return (string) $s; }
	function is_page($s = null) { return false; }
	function get_option($k, $d = false) { return $d; }
	function update_option($k, $v) { return true; }
	function wp_json_encode($v) { return json_encode($v, JSON_UNESCAPED_UNICODE); }
	function date_i18n($fmt, $ts) { return date($fmt, $ts); }
}

$RAIZ = dirname(__DIR__);

/**
 * Carrega UMA funcao de um snippet, equilibrando chaves. Nao carrega o snippet
 * inteiro de proposito: ele registra filtros do WordPress ao ser lido, e o que
 * este portao julga sao duas funcoes puras.
 */
function carregar_funcao($src, $nome) {
	$i = strpos($src, "function $nome(");
	if ($i === false) { return false; }
	$j = strpos($src, '{', $i);
	$n = 0;
	for ($k = $j; $k < strlen($src); $k++) {
		if ($src[$k] === '{') { $n++; }
		elseif ($src[$k] === '}') { $n--; if ($n === 0) { break; } }
	}
	eval(substr($src, $i, $k - $i + 1));
	return true;
}

$casca = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
$f2    = file_get_contents($RAIZ . '/snippets/rodametria-f2.php');

$falhas = array();
$afirmacoes = 0;
function afirma($cond, $msg) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if (!$cond) { $falhas[] = $msg; }
}

foreach (array(
	array('rodametria_casca_nome_da_loja', $casca),
	array('rodametria_casca_rotulo_da_loja', $casca),
	array('rodametria_f2_data', $f2),
	array('rodametria_f2_nota_de_preco', $f2),
) as $par) {
	$ok = carregar_funcao($par[1], $par[0]);
	afirma($ok, sprintf('nao achei a funcao %s nos snippets — o item 3 do despacho de '
		. '30/10/2026 foi desfeito', $par[0]));
	if (!$ok) {
		print("REPROVADO: " . end($falhas) . "\n");
		exit(1);
	}
}

/**
 * A REGUA: a nota PROMETE O DESTINO quando nomeia uma loja e nao avisa que o
 * botao vai para outra. Ela e escrita aqui, nao importada de ninguem.
 */
function promete_o_destino($nota, $loja_do_botao) {
	// SEM BOTAO NAO HA DESTINO PARA PROMETER, e este ramo nasceu da propria
	// bateria: o mundo "cartao sem botao" reprovava com a nota sadia "na
	// Shopee, lido em 27/10/2026". E o cartao sem link nem chega a tela —
	// rodametria_casca_cartao_de_compra() devolve string vazia quando a url e
	// vazia. Regua que reprova o mundo certo e o caminho mais curto para
	// alguem a ignorar, que e a licao que a 20.5 nomeou.
	if ('' === $loja_do_botao) { return false; }
	if (false === strpos($nota, 'botão abre a')) {
		// A nota nao avisa nada: entao toda loja que ela nomear tem de ser a do botao.
		foreach (array('Shopee', 'Mercado Livre') as $loja) {
			if (false !== strpos($nota, $loja) && $loja !== $loja_do_botao) {
				return true;
			}
		}
	}
	return false;
}

/* ---- O AUTOTESTE DA REGUA, e ele vem antes de qualquer veredito ---- */
afirma(promete_o_destino('na Mercado Livre, lido em 27/10/2026', 'Shopee'),
	'a regua NAO reprova a nota que estava no ar em 30/10/2026: ela e INERTE');
afirma(!promete_o_destino('na Shopee, lido em 27/10/2026', 'Shopee'),
	'a regua reprova nota sadia de loja igual');
afirma(!promete_o_destino('lido na Mercado Livre em 27/10/2026 — o botão abre a Shopee', 'Shopee'),
	'a regua reprova a nota que avisa o destino');
afirma(!promete_o_destino('na Shopee, lido em 27/10/2026', ''),
	'a regua reprova cartao SEM botao, que nao tem destino para prometer');
afirma(promete_o_destino('na Shopee, lido em 27/10/2026', 'Mercado Livre'),
	'a regua nao reprova o ESPELHO do defeito (preco Shopee com botao do Mercado Livre)');

/* ---- OS MUNDOS, inclusive os que o banco de hoje nao tem ---- */
$mundos = array(
	array('nome' => 'loja igual (Shopee nos dois)',
		'f' => array('preco_brl' => 1999.0, 'preco_loja' => 'Shopee', 'preco_programa' => 'shopee',
			'preco_data' => '2026-10-27', 'programa' => 'shopee',
			'url_afiliado_da_ficha' => '', 'url_busca' => 'https://s.shopee.com.br/a'),
		'botao' => 'Shopee'),
	array('nome' => 'loja diferente (preco ML, botao Shopee) — O DEFEITO',
		'f' => array('preco_brl' => 8244.0, 'preco_loja' => 'Mercado Livre',
			'preco_programa' => 'mercado_livre', 'preco_data' => '2026-10-27',
			'programa' => 'shopee', 'url_afiliado_da_ficha' => '',
			'url_busca' => 'https://s.shopee.com.br/b'),
		'botao' => 'Shopee'),
	array('nome' => 'o espelho do defeito (preco Shopee, botao ML)',
		'f' => array('preco_brl' => 3200.0, 'preco_loja' => 'Shopee', 'preco_programa' => 'shopee',
			'preco_data' => '2026-10-27', 'programa' => 'mercado_livre',
			'url_afiliado_da_ficha' => 'https://mercadolivre.com/x', 'url_busca' => ''),
		'botao' => 'Mercado Livre'),
	array('nome' => 'sem programa de link (cartao sem botao)',
		'f' => array('preco_brl' => 500.0, 'preco_loja' => 'Shopee', 'preco_programa' => 'shopee',
			'preco_data' => '2026-10-27', 'programa' => '',
			'url_afiliado_da_ficha' => '', 'url_busca' => ''),
		'botao' => ''),
);

foreach ($mundos as $m) {
	$nota = rodametria_f2_nota_de_preco($m['f']);
	afirma('' !== trim($nota), sprintf('%s: a nota saiu vazia', $m['nome']));
	afirma(false !== strpos($nota, '27/10/2026'),
		sprintf('%s: a nota perdeu a DATA da leitura, que a secao 7 exige: %s', $m['nome'], $nota));
	afirma(!promete_o_destino($nota, $m['botao']),
		sprintf('%s: a nota promete o destino. Botao vai para %s e a nota diz %s',
			$m['nome'], $m['botao'] === '' ? '(nenhum)' : $m['botao'], $nota));
	// A nota e CURTA: ela nasce ACIMA do botao dentro do cartao, e a 32.5 mede o
	// primeiro botao de compra antes de 1.400 px a 390 px.
	afirma(mb_strlen($nota) <= 90,
		sprintf('%s: nota de %d caracteres (%s) — acima do botao, a 32.5 paga a conta',
			$m['nome'], mb_strlen($nota), $nota));
}

/* ---- E AGORA O BANCO DE VERDADE, que e o que a pagina vai servir ---- */
$resp = json_decode(file_get_contents($RAIZ . '/dados/f2-respostas.json'), true);
afirma(is_array($resp), 'nao li dados/f2-respostas.json');
$vistos = 0;
if (is_array($resp) && isset($resp['compra'])) {
	foreach ($resp['compra'] as $chave => $grupo) {
		if (!is_array($grupo)) { continue; }
		foreach ($grupo as $it) {
			if (!is_array($it) || empty($it['preco_brl'])) { continue; }
			$vistos++;
			$botao = empty($it['programa']) ? ''
				: rodametria_casca_nome_da_loja($it['programa']);
			$nota = rodametria_f2_nota_de_preco($it);
			afirma(!promete_o_destino($nota, $botao),
				sprintf('o cartao %s promete o destino: botao vai para %s e a nota diz "%s"',
					isset($it['nome']) ? $it['nome'] : '?', $botao, $nota));
			afirma(!empty($it['preco_programa']),
				sprintf('o cartao %s tem preco e nao tem preco_programa: a tela nao tem como '
					. 'saber se a loja do preco e a do botao',
					isset($it['nome']) ? $it['nome'] : '?'));
		}
	}
}
afirma($vistos > 0, 'nenhum cartao com preco no arquivo publicado — este portao ficou cego');

printf("teste-nota-de-preco: %d afirmacoes sobre %d cartao(oes) com preco, %d falha(s)\n",
	$afirmacoes, $vistos, count($falhas));
foreach ($falhas as $f) { print("  REPROVADO: $f\n"); }
exit(count($falhas) ? 1 : 0);

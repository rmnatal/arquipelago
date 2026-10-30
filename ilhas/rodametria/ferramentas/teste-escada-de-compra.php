<?php
/**
 * TESTE DA ESCADA DE COMPRA NA TELA — A 25.2 NAS DUAS PONTAS, 30/10/2026.
 *
 * O DEFEITO, e ele nunca apareceu numa pagina: `rodametria_casca_cartao_de_compra()`
 * devolvia STRING VAZIA quando `url` chegava vazia. A 25.2 manda o contrario com
 * todas as letras — "quando nao existir, ou quando a ronda marcar como morta, A
 * BUSCA SOBE E VIRA O BOTAO". A F2 nunca sofreu porque resolvia a escada no
 * chamador; a VITRINE de produto passa `url` crua do dado, e no dia em que uma
 * ficha morresse o cartao SUMIRIA da pagina com o piso gravado ao lado, no mesmo
 * registro. A tabela de 16 linhas era pior: servia `esc_url( $item['url'] )` cru,
 * entao o `href` sairia VAZIO — um botao que recarrega a propria pagina com o
 * rotulo "Ver na Shopee" do lado. E o JSON-LD serviria `"url": ""`.
 *
 * POR QUE NADA VIU: os 21 anuncios da vitrine tem ficha, 21 de 21, medido em
 * 30/10/2026. O ramo da ficha morta NAO EXISTE no dado publicado, e regua que le
 * o dado publicado aprova o mundo que existe. E a 32.5-d inteira — "a regra do
 * molde que nunca rodou contra o dado de verdade esta quebrada e parece sa" —, e
 * a saida e a mesma que a ohmetria escreveu: SO A MUTACAO QUE PRODUZ O MUNDO O
 * ENXERGA. Esta bateria fabrica a ficha morta.
 *
 * ESTE PORTAO E PHP pelo motivo que o `teste-nota-de-preco.php` ja escreveu: a
 * escolha e decidida em PHP, entao a regua CHAMA a funcao em vez de ler o
 * arquivo. Regua em Python sobre o texto do PHP conferiria a FORMA.
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

/* A NOTA DA TABELA NAO E O QUE ESTA BATERIA JULGA, entao ela entra como tora.
   Definida ANTES de carregar as funcoes de verdade, para nao haver colisao. */
function rdm_produto_preencher($texto, $pagina) { return $texto; }

$RAIZ = dirname(__DIR__);

/** Carrega UMA funcao de um snippet, equilibrando chaves (mesmo mecanismo do
 *  teste-nota-de-preco.php: o snippet inteiro registra filtros ao ser lido). */
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

$casca   = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
$produto = file_get_contents($RAIZ . '/snippets/rodametria-produto.php');

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
	array('rodametria_casca_rotulo_do_piso', $casca),
	array('rodametria_casca_escada_de_compra', $casca),
	array('rodametria_casca_cartao_de_compra', $casca),
	array('rdm_produto_tabela_html', $produto),
) as $par) {
	$ok = carregar_funcao($par[1], $par[0]);
	afirma($ok, sprintf('nao achei a funcao %s nos snippets — a escada da 25.2 na tela foi desfeita', $par[0]));
	if (!$ok) {
		print("REPROVADO: " . end($falhas) . "\n");
		exit(1);
	}
}

/* =========================================================================
 * 1. A ESCADA, NOS QUATRO MUNDOS QUE O ESQUEMA PERMITE
 *
 * Tres deles NAO EXISTEM no dado publicado hoje, e e exatamente por isso que
 * eles sao fabricados aqui.
 * ======================================================================= */

$FICHA = 'https://s.shopee.com.br/FICHAxxxxx';
$BUSCA = 'https://s.shopee.com.br/BUSCAxxxxx';

/* MUNDO A — ficha viva e busca: o mundo de hoje, 21 de 21. */
$a = rodametria_casca_escada_de_compra(array(
	'url' => $FICHA, 'url_busca' => $BUSCA, 'degrau' => 1, 'programa' => 'shopee'));
afirma($a['url'] === $FICHA, 'mundo A: a ficha viva nao virou o botao');
afirma($a['url_busca'] === $BUSCA, 'mundo A: a busca nao desceu para a linha discreta — a 25.2 diz "nunca sai"');
afirma($a['degrau'] === 1, 'mundo A: o degrau declarado da ficha foi trocado');
afirma($a['piso_subiu'] === false, 'mundo A: a escada diz que o piso subiu e a ficha esta viva');
afirma($a['tem_saida'] === true, 'mundo A: a escada diz que nao ha saida de compra');

/* MUNDO B — A FICHA MORREU E O PISO ESTA NO DADO. Este e o mundo que o defeito
   escondia, e as cinco afirmacoes abaixo sao a regra inteira. */
$b = rodametria_casca_escada_de_compra(array(
	'url' => '', 'url_busca' => $BUSCA, 'degrau' => 1, 'programa' => 'shopee'));
afirma($b['url'] === $BUSCA, 'MUNDO B: a ficha morreu e A BUSCA NAO SUBIU — e o defeito que este portao nasceu para pegar');
afirma($b['url_busca'] === '', 'mundo B: a busca esta no botao E na linha discreta — o mesmo link duas vezes no cartao');
afirma($b['degrau'] === 4, 'MUNDO B: a busca subiu e o DEGRAU ficou para tras — o rotulo vai prometer uma ficha que nao existe');
afirma($b['piso_subiu'] === true, 'mundo B: a escada nao avisa que o piso subiu, e o JSON-LD precisa disso para nao afirmar InStock');
afirma($b['tem_saida'] === true, 'mundo B: a escada diz que nao ha saida e o piso esta gravado no dado');

/* MUNDO C — ficha sem busca: o item sem piso, que a 25.2 chama de defeito da
   19.1. A tela nao o conserta; ela so nao mente sobre ele. */
$c = rodametria_casca_escada_de_compra(array(
	'url' => $FICHA, 'url_busca' => '', 'degrau' => 1, 'programa' => 'shopee'));
afirma($c['url'] === $FICHA, 'mundo C: a ficha sem busca nao virou o botao');
afirma($c['url_busca'] === '', 'mundo C: inventou linha discreta sem busca no dado');
afirma($c['tem_saida'] === true, 'mundo C: a escada diz que nao ha saida e ha ficha');

/* MUNDO D — nem ficha nem busca. */
$d = rodametria_casca_escada_de_compra(array(
	'url' => '', 'url_busca' => '', 'degrau' => 0, 'programa' => 'shopee'));
afirma($d['tem_saida'] === false, 'mundo D: a escada promete saida de compra sem link nenhum');
afirma($d['url'] === '', 'mundo D: a escada devolveu url sem ter link');

/* MUNDO E — CHAVE AUSENTE, nao vazia. O dado da vitrine traz `url_busca` do
   piso da consulta com `.get()`, e `.get()` de chave ausente e `null`. */
$e = rodametria_casca_escada_de_compra(array('programa' => 'shopee'));
afirma($e['tem_saida'] === false, 'mundo E: chave ausente nao foi lida como ausencia');
$e2 = rodametria_casca_escada_de_compra(array('url' => null, 'url_busca' => $BUSCA, 'programa' => 'shopee'));
afirma($e2['url'] === $BUSCA && $e2['degrau'] === 4, 'mundo E: `url` nula nao caiu para a busca');

/* MUNDO F — SO ESPACO NO LUGAR DA FICHA. `"  "` nao e link e nao e vazio, e e o
   que um `strip()` esquecido no gerador produz. */
$f6 = rodametria_casca_escada_de_compra(array(
	'url' => '   ', 'url_busca' => $BUSCA, 'degrau' => 1, 'programa' => 'shopee'));
afirma($f6['url'] === $BUSCA, 'mundo F: ficha so de espaco foi tratada como ficha viva');
afirma($f6['degrau'] === 4, 'mundo F: ficha so de espaco manteve o degrau da ficha');

/* =========================================================================
 * 2. O CARTAO — o mundo B tem de CHEGAR A TELA, e com o rotulo certo
 * ======================================================================= */

$cartao_b = rodametria_casca_cartao_de_compra(array(
	'nome' => 'Patinete de teste', 'url' => '', 'url_busca' => $BUSCA,
	'degrau' => 1, 'programa' => 'shopee', 'preco' => 'R$ 1.000,00'));
afirma($cartao_b !== '', 'O CARTAO SUMIU NO MUNDO B: ficha morta com piso no dado nao chega a tela');
afirma(false !== strpos($cartao_b, $BUSCA), 'o cartao do mundo B nao serve a busca');
afirma(false !== strpos($cartao_b, 'Ver ofertas na Shopee'),
	'o cartao do mundo B promete ficha: o rotulo devia ser "Ver ofertas na Shopee"');
afirma(false === strpos($cartao_b, 'Ver na Shopee'),
	'o cartao do mundo B diz "Ver na Shopee" apontando para uma pagina de busca');
afirma(1 === substr_count($cartao_b, $BUSCA),
	'o cartao do mundo B serve a busca DUAS vezes — botao e linha discreta com o mesmo link');
afirma(false === strpos($cartao_b, rodametria_casca_rotulo_do_piso()),
	'o cartao do mundo B imprime a linha discreta do piso com a busca ja no botao');
afirma(false !== strpos($cartao_b, 'Patinete de teste'),
	'o cartao do mundo B perdeu o nome do produto');

$cartao_a = rodametria_casca_cartao_de_compra(array(
	'nome' => 'Patinete de teste', 'url' => $FICHA, 'url_busca' => $BUSCA,
	'degrau' => 1, 'programa' => 'shopee', 'preco' => 'R$ 1.000,00'));
afirma(false !== strpos($cartao_a, 'Ver na Shopee'), 'o cartao do mundo A perdeu o rotulo de ficha');
afirma(false !== strpos($cartao_a, rodametria_casca_rotulo_do_piso()),
	'o cartao do mundo A perdeu a linha discreta da busca, que a 25.2 diz que "nunca sai"');

$cartao_d = rodametria_casca_cartao_de_compra(array(
	'nome' => 'Sem saida', 'url' => '', 'url_busca' => '', 'degrau' => 0, 'programa' => 'shopee'));
afirma($cartao_d === '', 'o cartao sem link NENHUM foi para a tela: botao sem destino');

/* AS DUAS METADES DO VEREDITO, NO PROPRIO CARTAO: nenhum `href` vazio sai daqui. */
foreach (array('A' => $cartao_a, 'B' => $cartao_b) as $nome => $h) {
	afirma(false === strpos($h, 'href=""'), "o cartao do mundo $nome serve href vazio");
}

/* =========================================================================
 * 3. A TABELA DA VITRINE — nenhum `href=""`, e a linha do piso UMA vez
 * ======================================================================= */

function pagina_de_teste($linhas) {
	return array('vitrine' => array('linhas' => $linhas), 'declarado' => array());
}
function linha($url, $busca, $nome = 'Anuncio') {
	return array('nome' => $nome, 'preco' => 'R$ 1.000,00', 'preco_numero' => 1000.0,
		'especificacao' => '350 W', 'loja' => 'Loja de teste', 'programa' => 'shopee',
		'degrau' => 1, 'url' => $url, 'url_busca' => $busca);
}

/* A tabela do mundo de hoje: tres fichas vivas com o MESMO piso. */
$t_hoje = rdm_produto_tabela_html(pagina_de_teste(array(
	linha($FICHA . '1', $BUSCA, 'Um'), linha($FICHA . '2', $BUSCA, 'Dois'),
	linha($FICHA . '3', $BUSCA, 'Tres'))));
afirma(false === strpos($t_hoje, 'href=""'), 'a tabela de hoje serve href vazio');
afirma(1 === substr_count($t_hoje, rodametria_casca_rotulo_do_piso()),
	'a linha do piso nao saiu UMA vez na tabela: o piso e da consulta, nao do anuncio');
afirma(false !== strpos($t_hoje, $BUSCA), 'a tabela nao serve o piso da 25.2 em lugar nenhum');
afirma(3 === substr_count($t_hoje, 'Ver na Shopee'), 'a tabela de hoje perdeu rotulo de ficha');

/* A TABELA COM UMA FICHA MORTA — o mundo que o dado publicado nao tem. */
$t_morta = rdm_produto_tabela_html(pagina_de_teste(array(
	linha($FICHA . '1', $BUSCA, 'Um'), linha('', $BUSCA, 'Morta'),
	linha($FICHA . '3', $BUSCA, 'Tres'))));
afirma(false === strpos($t_morta, 'href=""'),
	'A TABELA SERVE href VAZIO quando a ficha morre — um botao que recarrega a propria pagina');
afirma(false !== strpos($t_morta, 'Ver ofertas na Shopee'),
	'a linha da ficha morta nao caiu para a busca com o rotulo de busca');
afirma(false !== strpos($t_morta, 'Morta'),
	'a linha da ficha morta SAIU da tabela: a secao 7 manda todo item ser nomeado uma vez');

/* A TABELA SEM SAIDA NENHUMA numa linha: o anuncio continua nomeado. */
$t_sem = rdm_produto_tabela_html(pagina_de_teste(array(
	linha($FICHA . '1', $BUSCA, 'Um'), linha('', '', 'Orfa'))));
afirma(false === strpos($t_sem, 'href=""'), 'a tabela serve href vazio na linha sem saida');
afirma(false !== strpos($t_sem, 'Orfa'), 'a linha sem saida de compra SAIU da tabela');
afirma(false !== strpos($t_sem, 'sem link de compra hoje'),
	'a linha sem saida nao diz o que falta: celula calada e promessa pela metade');

/* DUAS BUSCAS DISTINTAS: a linha do piso NAO sai, em vez de escolher "a primeira". */
$t_duas = rdm_produto_tabela_html(pagina_de_teste(array(
	linha($FICHA . '1', $BUSCA . 'a', 'Um'), linha($FICHA . '2', $BUSCA . 'b', 'Dois'))));
afirma(0 === substr_count($t_duas, rodametria_casca_rotulo_do_piso()),
	'com duas buscas distintas a tabela escolheu uma: "a primeira" e arbitraria');

/* =========================================================================
 * 4. O AUTOTESTE DA BATERIA — ela tem de MORDER
 *
 * Portao que nao reprova o defeito que o fez nascer e INERTE, e a bancada desta
 * ilha nomeia inerte com essa palavra. A escada VELHA e reproduzida aqui, e as
 * afirmacoes do mundo B tem de reprova-la.
 * ======================================================================= */

function escada_velha($item) {
	/* O QUE A CASCA FAZIA ATE 30/10/2026: a `url` crua, e vazio some. */
	$url = isset($item['url']) ? $item['url'] : '';
	return array('url' => $url, 'url_busca' => isset($item['url_busca']) ? $item['url_busca'] : '',
		'degrau' => isset($item['degrau']) ? (int) $item['degrau'] : 0,
		'piso_subiu' => false, 'tem_saida' => ('' !== $url));
}
$velho_b = escada_velha(array('url' => '', 'url_busca' => $BUSCA, 'degrau' => 1));
afirma($velho_b['url'] !== $BUSCA,
	'A BATERIA ESTA INERTE: a escada velha passaria no mundo B, logo a regua nao mede nada');
afirma($velho_b['tem_saida'] === false,
	'a bateria esta inerte: a escada velha ja daria saida de compra no mundo B');
afirma($velho_b['degrau'] !== 4,
	'a bateria esta inerte: a escada velha ja subiria o degrau no mundo B');

/* =========================================================================
 * 5. O DADO PUBLICADO — a premissa de hoje, dita como numero
 * ======================================================================= */

$vistos = 0; $com_ficha = 0; $com_piso = 0; $sem_saida = 0;
$vitrine = json_decode(file_get_contents($RAIZ . '/dados/vitrine-de-produto.json'), true);
afirma(is_array($vitrine) && !empty($vitrine['paginas']), 'nao li dados/vitrine-de-produto.json');

foreach ((array) $vitrine['paginas'] as $pg) {
	$buscas = array();
	foreach ((array) $pg['linhas'] as $l) {
		$vistos++;
		$esc = rodametria_casca_escada_de_compra($l);
		if (!empty($l['url'])) { $com_ficha++; }
		if (!empty($l['url_busca'])) { $com_piso++; $buscas[trim((string) $l['url_busca'])] = true; }
		if (!$esc['tem_saida']) { $sem_saida++; }
		afirma($esc['tem_saida'],
			sprintf('a linha "%s" da pagina %s nao tem saida de compra: defeito da 19.1 pela 25.2',
				isset($l['nome']) ? substr($l['nome'], 0, 30) : '?', $pg['id']));
		afirma(strpos((string) $esc['url'], 'https://') === 0,
			sprintf('a linha "%s" da pagina %s resolve para uma url que nao e https',
				isset($l['nome']) ? substr($l['nome'], 0, 30) : '?', $pg['id']));
	}
	/* A PREMISSA DA LINHA UNICA DO PISO, cobrada em vez de suposta: se um dia o
	   piso deixar de ser da consulta, a tabela deixa de imprimir a linha e ESTA
	   afirmacao e quem diz por que — a pagina nao emudece sozinha. */
	afirma(count($buscas) <= 1,
		sprintf('a pagina %s tem %d buscas distintas: a linha unica do piso da tabela nao sai mais',
			$pg['id'], count($buscas)));
}
afirma($vistos > 0, 'nenhuma linha de vitrine lida — este portao ficou cego');

/* =========================================================================
 * 6. A F2 NAO MUDOU UM BYTE — e isto e cobrado, nao prometido
 *
 * Em 30/10/2026 a escada saiu do CHAMADOR da F2 e virou mecanismo do molde. O
 * comentario que ficou no snippet afirma que a saida e identica, e afirmacao em
 * comentario e numero digitado em outro traje (32.5-d). Entao a regra VELHA do
 * chamador e reproduzida aqui e comparada com a escada, item por item, no dado
 * publicado da F2 — que e o unico lugar desta ilha onde o mundo B JA EXISTE:
 * tres registros sem ficha e com piso, e um sem nenhum dos dois.
 * ======================================================================= */

function escolha_velha_da_f2($f) {
	/* O QUE `rodametria_f2_itens_de_compra()` FAZIA ATE 30/10/2026. */
	$ficha = empty($f['url_afiliado_da_ficha']) ? '' : $f['url_afiliado_da_ficha'];
	return array(
		'url'       => ('' === $ficha) ? (isset($f['url_busca']) ? (string) $f['url_busca'] : '') : $ficha,
		'url_busca' => ('' === $ficha) ? '' : (isset($f['url_busca']) ? (string) $f['url_busca'] : ''),
		'degrau'    => isset($f['degrau']) ? (int) $f['degrau'] : 0,
	);
}

$f2_vistos = 0; $f2_mundo_b = 0;
$resp = json_decode(file_get_contents($RAIZ . '/dados/f2-respostas.json'), true);
afirma(is_array($resp), 'nao li dados/f2-respostas.json');

if (is_array($resp) && isset($resp['compra'])) {
	foreach ((array) $resp['compra'] as $grupo) {
		if (!is_array($grupo)) { continue; }
		foreach ($grupo as $it) {
			if (!is_array($it)) { continue; }
			$f2_vistos++;
			$nome = isset($it['nome']) ? substr($it['nome'], 0, 30) : '?';

			$velha = escolha_velha_da_f2($it);
			/* O ITEM COMO A F2 O ENTREGA DESDE HOJE: os dois links CRUS. */
			$nova = rodametria_casca_escada_de_compra(array(
				'url'       => isset($it['url_afiliado_da_ficha']) ? $it['url_afiliado_da_ficha'] : '',
				'url_busca' => isset($it['url_busca']) ? $it['url_busca'] : '',
				'degrau'    => isset($it['degrau']) ? $it['degrau'] : 0,
			));

			afirma($nova['url'] === $velha['url'],
				sprintf('a F2 MUDOU o link do item %s: era "%s", virou "%s"', $nome, $velha['url'], $nova['url']));
			afirma($nova['url_busca'] === $velha['url_busca'],
				sprintf('a F2 MUDOU a linha discreta do item %s', $nome));
			afirma($nova['degrau'] === $velha['degrau'],
				sprintf('a F2 MUDOU o degrau do item %s: era %d, virou %d', $nome, $velha['degrau'], $nova['degrau']));

			if (empty($it['url_afiliado_da_ficha']) && !empty($it['url_busca'])) {
				$f2_mundo_b++;
				/* O MUNDO B DE VERDADE, no dado publicado: a F2 ja o servia certo
				   porque o GERADOR dela grava `degrau: 4` nestes itens. E a prova
				   de que a escada nova concorda com quem ja acertava. */
				afirma($nova['degrau'] === 4,
					sprintf('o item %s da F2 vive o mundo B e o degrau nao e 4', $nome));
				afirma($nova['url'] === $it['url_busca'],
					sprintf('o item %s da F2 vive o mundo B e a busca nao e o botao', $nome));
			}
		}
	}
}
afirma($f2_vistos > 0, 'nenhum item de compra da F2 lido — esta metade do portao ficou cega');
afirma($f2_mundo_b > 0,
	'nenhum item da F2 vive o mundo B no dado publicado: a comparacao com a regra velha ficou cega '
	. 'justamente no ramo que importa');

printf("teste-escada-de-compra: %d afirmacoes · %d linhas da vitrine (%d com ficha, %d com piso, %d sem saida)"
	. " · %d itens da F2 (%d no mundo B, identicos a regra velha) · %d falha(s)\n",
	$afirmacoes, $vistos, $com_ficha, $com_piso, $sem_saida, $f2_vistos, $f2_mundo_b, count($falhas));
foreach ($falhas as $f) { print("  REPROVADO: $f\n"); }
exit(count($falhas) ? 1 : 0);

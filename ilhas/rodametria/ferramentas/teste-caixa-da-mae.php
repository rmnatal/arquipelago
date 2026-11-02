<?php
/**
 * A CAIXA DE RESPOSTA DA SECAO MAE — OS SETE MUNDOS, E O DADO DE HOJE EXERCITA UM.
 *
 *   php ferramentas/teste-caixa-da-mae.php
 *
 * POR QUE ELE NASCEU EM 02/11/2026, no mesmo bloco que poe `/veiculos/` no molde:
 * a pagina mae servia `<p class="rdm-promessa">` onde a 32.2 pede a CAIXA DE
 * RESPOSTA, e o portao de pixel desta ilha a listava, nas duas passadas de 30/10,
 * como "sem componente de molde nenhum". O custo nao era de aparencia: os 700 px
 * da 32.5 NUNCA A JULGARAM. Regua que nao alcanca a pagina nao a reprova — so a
 * ignora, e a 32.5-c nomeia essa familia inteira.
 *
 * O QUE ELE JULGA, e e por isso que ele e PHP e nao Python: a escolha da frase e
 * decidida em PHP, entao a regua CHAMA a funcao em vez de ler o arquivo. Regua em
 * Python sobre o texto do PHP conferiria a FORMA do codigo, nunca a decisao.
 * (Mesmo motivo escrito no `teste-nota-de-preco.php` e no `teste-escada-de-compra.php`.)
 *
 * OS SETE MUNDOS. O banco de hoje tem DUAS familias prontas, as duas lidas no
 * MESMO dia, e TRES que faltam — um mundo. Os outros seis nao existem no dado, e
 * a 32.5-d e literal sobre o que isso significa: "a regra do molde que nunca
 * rodou contra o dado de verdade esta quebrada e parece sa". Entao esta bateria
 * os FABRICA:
 *
 *   1. duas familias, mesma data, tres faltando   (o mundo de hoje)
 *   2. duas familias lidas em DATAS DIFERENTES    (a frase da data nao pode escolher uma)
 *   3. UMA familia so                             (plural que mentiria: "nas 1 familias")
 *   4. NENHUMA familia pronta                     (a pagina degradada e honesta)
 *   5. UMA familia faltando                       (plural que mentiria: "as outras 1")
 *   6. NENHUMA familia faltando                   (a frase do que falta nao sai)
 *   7. familia pronta SEM FAIXA DE PRECO          (o "de  a ." na tela)
 *   8. preco de TRES DIGITOS ao lado de quatro    (o unico mundo em que a
 *                                                  comparacao por texto erra)
 *
 * E ELE PROVA QUE MORDE: tres mutacoes do codigo de verdade, aplicadas sobre as
 * proprias funcoes, tem de REPROVAR. Trava que nunca falhou nao e trava, e o
 * `bancada.py` desta ilha cobra as duas metades do veredito — palavra impressa e
 * codigo de saida.
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

/** Carrega UMA funcao de um snippet, equilibrando chaves — o snippet inteiro
 *  registra filtros ao ser lido, entao ele nao pode ser incluido. */
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

$produto = file_get_contents($RAIZ . '/snippets/rodametria-produto.php');
$casca   = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
$decl    = json_decode(file_get_contents($RAIZ . '/dados/paginas-de-produto.json'), true);

$falhas = array();
$afirmacoes = 0;
function afirma($cond, $msg) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if (!$cond) { $falhas[] = $msg; }
}

foreach (array(
	array('rdm_produto_agregado_das_prontas', $produto),
	array('rdm_produto_caixa_frases', $produto),
	array('rodametria_casca_caixa', $casca),
) as $par) {
	$ok = carregar_funcao($par[1], $par[0]);
	afirma($ok, sprintf('nao achei a funcao %s nos snippets — a caixa da mae foi desfeita', $par[0]));
	if (!$ok) {
		print("teste-caixa-da-mae: REPROVADO — " . end($falhas) . "\n");
		exit(1);
	}
}

afirma(!empty($decl['mae']['caixa']), 'a camada declarada nao traz `mae.caixa`');
$M = isset($decl['mae']['caixa']) ? $decl['mae']['caixa'] : array();

/* =========================================================================
 * 0. OS MOLDES QUE A FUNCAO PROCURA EXISTEM TODOS NA CAMADA DECLARADA
 *
 * E a cicatriz que o `teste-institucional.py` desta ilha ja cobra na irma:
 * "molde que o preenchedor do PHP nao conhece". Aqui o risco e o inverso e pior,
 * porque e silencioso: molde que o PHP PROCURA e a camada declarada nao tem sai
 * como frase VAZIA, e frase vazia nao deixa rastro na tela.
 * ========================================================================= */

foreach (array('rotulo', 'unidade', 'escopo_muitas', 'escopo_uma', 'escopo_sem_faixa',
	'escopo_sem_faixa_uma', 'escopo_nenhuma', 'data_igual', 'data_divergente',
	'faltam', 'falta_uma') as $chave) {
	afirma(!empty($M[$chave]) && is_string($M[$chave]),
		sprintf('o molde `%s` nao esta na camada declarada da mae', $chave));
}

/* E NENHUM DELES TRAZ DIGITO — o `gerar-vitrine-de-produto.py --conferir` ja
   cobra isso em todo campo da mae, e esta linha e a segunda chave da mesma porta:
   prosa que afirma o estado do banco e numero digitado em outro traje. */
foreach ($M as $chave => $texto) {
	if (!is_string($texto)) { continue; }
	afirma(!preg_match('/\d/', $texto),
		sprintf('o molde `%s` traz digito digitado: %s', $chave, substr($texto, 0, 60)));
}

/* =========================================================================
 * OS MUNDOS. Cada familia e so o que a funcao le dela.
 * ========================================================================= */

function familia($n, $de, $ate, $de_num, $ate_num, $data) {
	return array('vitrine' => array(
		'numeros' => array('n' => $n, 'de' => $de, 'ate' => $ate,
			'de_numero' => $de_num, 'ate_numero' => $ate_num),
		'colhido_em_br' => $data,
	));
}

$PATINETE  = familia(16, 'R$ 1.297,13', 'R$ 3.399,00', 1297.13, 3399.0, '29/10/2026');
$BICICLETA = familia(5, 'R$ 2.299,99', 'R$ 6.199,90', 2299.99, 6199.9, '29/10/2026');
$OUTRO_DIA = familia(5, 'R$ 2.299,99', 'R$ 6.199,90', 2299.99, 6199.9, '31/10/2026');
$SEM_FAIXA = familia(3, '', '', null, null, '29/10/2026');
/* UMA FAMILIA BARATA, e ela existe NESTA BATERIA e nao no banco por um motivo
   que e o do portao inteiro: a comparacao por string so mente quando os precos
   tem CONTAGEM DE DIGITOS DIFERENTE. Com os quatro digitos de hoje
   (`R$ 1.297,13` contra `R$ 2.299,99`) o alfabeto acerta por sorte, e a mutacao
   da faixa SOBREVIVEU na primeira rodada desta bateria — o mutante passou e o
   portao se denunciou. Uma bicicleta de tres digitos e dado plausivel amanha, e
   e nela que `R$ 899,00` perde de `R$ 1.297,13` por comparacao de texto. */
$BARATO    = familia(2, 'R$ 899,00', 'R$ 1.099,00', 899.0, 1099.0, '29/10/2026');

/* -------------------------------------------------------------------------
 * MUNDO 1 — O DE HOJE: duas familias, mesma data, tres faltando.
 * ------------------------------------------------------------------------- */

$ag = rdm_produto_agregado_das_prontas(array($PATINETE, $BICICLETA));
afirma($ag['familias'] === 2, 'mundo 1: nao contou duas familias');
afirma($ag['anuncios'] === 21, sprintf('mundo 1: a soma dos anuncios deu %d e nao 21', $ag['anuncios']));
/* A FAIXA ATRAVESSA AS DUAS FAMILIAS, e e por isso que a comparacao e pelo
   campo numerico: por string, `R$ 1.297,13` perde de `R$ 2.299,99` por sorte do
   alfabeto, e `R$ 6.199,90` perderia de `R$ 3.399,00` — o inverso do certo. */
afirma($ag['de'] === 'R$ 1.297,13', sprintf('mundo 1: o menor preco deu %s', $ag['de']));
afirma($ag['ate'] === 'R$ 6.199,90', sprintf('mundo 1: o maior preco deu %s', $ag['ate']));
afirma($ag['datas'] === array('29/10/2026'), 'mundo 1: as datas iguais nao colapsaram em uma');

$f = rdm_produto_caixa_frases($ag, 3, $M);
afirma(count($f) === 3, sprintf('mundo 1: saiu %d frase(s) e nao 3', count($f)));
afirma(strpos($f[0], 'nas 2 famílias') !== false, 'mundo 1: a frase de escopo nao diz duas familias: ' . $f[0]);
afirma(strpos($f[0], 'R$ 1.297,13') !== false && strpos($f[0], 'R$ 6.199,90') !== false,
	'mundo 1: a faixa nao chegou na frase: ' . $f[0]);
afirma(strpos($f[1], '29/10/2026') !== false, 'mundo 1: a data nao chegou na frase: ' . $f[1]);
afirma(strpos($f[2], 'As outras 3') !== false, 'mundo 1: a frase do que falta nao diz tres: ' . $f[2]);

/* E NENHUMA FRASE PODE SAIR COM MOLDE CRU NA TELA. */
foreach ($f as $frase) {
	afirma(strpos($frase, '{') === false,
		'mundo 1: frase com molde nao preenchido na tela: ' . $frase);
}

/* -------------------------------------------------------------------------
 * MUNDO 2 — DATAS DIFERENTES. A pedra da linha do piso, um andar acima: com
 * duas datas distintas, escolher uma e mentir sobre a outra.
 * ------------------------------------------------------------------------- */

$ag2 = rdm_produto_agregado_das_prontas(array($PATINETE, $OUTRO_DIA));
afirma(count($ag2['datas']) === 2, 'mundo 2: as duas datas nao foram guardadas distintas');
$f2 = rdm_produto_caixa_frases($ag2, 3, $M);
afirma($f2[1] === $M['data_divergente'], 'mundo 2: a frase da data escolheu uma das duas: ' . $f2[1]);
afirma(strpos($f2[1], '29/10') === false && strpos($f2[1], '31/10') === false,
	'mundo 2: a frase da data imprime uma data que nao vale para todas: ' . $f2[1]);

/* -------------------------------------------------------------------------
 * MUNDO 3 — UMA FAMILIA SO. "nas 1 familias" e o plural que mente.
 * ------------------------------------------------------------------------- */

$ag3 = rdm_produto_agregado_das_prontas(array($PATINETE));
$f3  = rdm_produto_caixa_frases($ag3, 3, $M);
afirma($ag3['anuncios'] === 16, 'mundo 3: a soma de uma familia nao e a dela');
afirma(strpos($f3[0], 'única família') !== false, 'mundo 3: o singular nao saiu: ' . $f3[0]);
afirma(strpos($f3[0], ' 1 ') === false, 'mundo 3: a frase imprime "1" onde cabe o singular: ' . $f3[0]);

/* -------------------------------------------------------------------------
 * MUNDO 4 — NENHUMA FAMILIA PRONTA. A pagina tem de dizer isso, nao somar zero
 * e servir faixa vazia. A casca ja tem a cicatriz: "pagina DEGRADADA e honesta
 * em vez de pagina com molde cru".
 * ------------------------------------------------------------------------- */

$ag4 = rdm_produto_agregado_das_prontas(array());
afirma($ag4['familias'] === 0 && $ag4['anuncios'] === 0, 'mundo 4: o agregado vazio nao e zero');
$f4 = rdm_produto_caixa_frases($ag4, 3, $M);
afirma($f4[0] === $M['escopo_nenhuma'], 'mundo 4: o escopo de nenhuma familia nao saiu: ' . $f4[0]);
foreach ($f4 as $frase) {
	afirma(strpos($frase, 'R$') === false, 'mundo 4: frase com preco sem familia nenhuma: ' . $frase);
	afirma(strpos($frase, '{') === false, 'mundo 4: molde cru na tela: ' . $frase);
}
/* E A FRASE DA DATA NAO SAI quando nao ha familia: sem filha nao houve leitura,
   e "cada familia foi lida num dia diferente" seria afirmacao sobre o vazio. */
afirma(!in_array($M['data_igual'], $f4, true) && !in_array($M['data_divergente'], $f4, true),
	'mundo 4: a frase da data saiu sem nenhuma familia para ter data');

/* -------------------------------------------------------------------------
 * MUNDO 5 e 6 — UMA familia faltando, e NENHUMA.
 * ------------------------------------------------------------------------- */

$f5 = rdm_produto_caixa_frases($ag, 1, $M);
afirma(in_array($M['falta_uma'], $f5, true), 'mundo 5: o singular do que falta nao saiu');
foreach ($f5 as $frase) {
	afirma(strpos($frase, 'outras 1') === false, 'mundo 5: "as outras 1" chegou na tela: ' . $frase);
}

$f6 = rdm_produto_caixa_frases($ag, 0, $M);
afirma(count($f6) === 2, sprintf('mundo 6: com nada faltando saiu %d frase(s) e nao 2', count($f6)));
foreach ($f6 as $frase) {
	afirma(strpos($frase, 'ainda não t') === false,
		'mundo 6: a frase do que falta saiu com nada faltando: ' . $frase);
	afirma(strpos($frase, ' 0 ') === false, 'mundo 6: imprime zero no meio da frase: ' . $frase);
}

/* -------------------------------------------------------------------------
 * MUNDO 7 — FAMILIA PRONTA SEM FAIXA DE PRECO. O buraco no lugar do numero
 * ("de  a .") e pior que numero velho: nao parece defeito de dado, parece
 * defeito de texto, e ninguem vai procurar no banco.
 * ------------------------------------------------------------------------- */

$ag7 = rdm_produto_agregado_das_prontas(array($SEM_FAIXA));
afirma($ag7['familias'] === 1 && $ag7['de'] === '' && $ag7['ate'] === '',
	'mundo 7: o agregado inventou faixa onde o dado nao tem');
$f7 = rdm_produto_caixa_frases($ag7, 0, $M);
afirma($f7[0] === $M['escopo_sem_faixa_uma'],
	'mundo 7: o escopo sem faixa no SINGULAR nao saiu: ' . $f7[0]);
$f7b = rdm_produto_caixa_frases(
	rdm_produto_agregado_das_prontas(array($SEM_FAIXA, $SEM_FAIXA)), 0, $M);
afirma(strpos($f7b[0], 'nas 2 famílias') !== false,
	'mundo 7: o escopo sem faixa no plural nao conta as familias: ' . $f7b[0]);
foreach ($f7 as $frase) {
	afirma(strpos($frase, 'de  a') === false && strpos($frase, 'vão de  ') === false,
		'mundo 7: buraco no lugar do preco na tela: ' . $frase);
	afirma(strpos($frase, 'R$') === false, 'mundo 7: serviu `R$` sem preco: ' . $frase);
}

/* -------------------------------------------------------------------------
 * O MUNDO DOS TRES DIGITOS, com a funcao de verdade: e o mundo em que a
 * comparacao por texto erra, e e por isso que ele esta aqui.
 * ------------------------------------------------------------------------- */

$ag8 = rdm_produto_agregado_das_prontas(array($PATINETE, $BARATO));
afirma($ag8['de'] === 'R$ 899,00',
	sprintf('mundo 8: o menor preco de tres digitos nao ganhou: %s', $ag8['de']));
afirma($ag8['ate'] === 'R$ 3.399,00',
	sprintf('mundo 8: o maior preco nao ganhou: %s', $ag8['ate']));
afirma($ag8['anuncios'] === 18, sprintf('mundo 8: a soma deu %d e nao 18', $ag8['anuncios']));

/* =========================================================================
 * A CAIXA, MONTADA PELA CASCA, serve o numero em Mono e as frases na ordem.
 * ========================================================================= */

$html = rodametria_casca_caixa($M['rotulo'], (string) $ag['anuncios'], $M['unidade'], $f, 'neutro');
afirma(strpos($html, 'rdm-molde-caixa') !== false, 'a caixa nao traz a classe do molde');
afirma(strpos($html, '<span class="rdm-num">21</span>') !== false,
	'o numero contado nao saiu em Mono na caixa');
afirma(substr_count($html, 'rdm-molde-caixa-frase') === 3, 'as tres frases nao sairam na caixa');
afirma(strpos($html, 'rdm-molde-caixa-rotulo') !== false, 'o rotulo nao saiu na caixa');

/* =========================================================================
 * PROVA DE QUE MORDE — tres mutacoes no codigo de verdade.
 * ========================================================================= */

$mutacoes = array(
	/* (a) A FAIXA COMPARADA POR STRING, que e o defeito que a ilha nao teria
	   como ver: com os precos de hoje ela devolve `R$ 2.299,99` como o menor. */
	'a faixa comparada por string em vez de numero' => function ($prontas) {
		$de = '';
		foreach ($prontas as $p) {
			$n = $p['vitrine']['numeros'];
			if ($de === '' || (string) $n['de'] < $de) { $de = (string) $n['de']; }
		}
		/* O mutante PASSA se ainda achar o menor preco. Com `R$ 899,00` na mesa
		   ele acha `R$ 1.297,13`, porque o alfabeto poe `1` antes de `8`. */
		return $de === 'R$ 899,00';
	},
	/* (b) A FRASE DA DATA SEMPRE ESCOLHENDO A PRIMEIRA. */
	'a frase da data escolhendo a primeira de duas' => function ($prontas) use ($M) {
		$ag = rdm_produto_agregado_das_prontas($prontas);
		$frase = str_replace('{DATA}', $ag['datas'][0], $M['data_igual']);
		return strpos($frase, '31/10/2026') !== false || count($ag['datas']) === 1;
	},
	/* (c) O PLURAL UNICO, que e o que uma primeira versao escreveria. */
	'uma frase de escopo so, no plural' => function ($prontas) use ($M) {
		$ag = rdm_produto_agregado_das_prontas($prontas);
		$frase = str_replace(array('{NO_AR}', '{DE}', '{ATE}'),
			array((string) $ag['familias'], $ag['de'], $ag['ate']), $M['escopo_muitas']);
		return strpos($frase, 'nas 1 famílias') === false;
	},
);

$mordeu = 0;
foreach ($mutacoes as $nome => $mutante) {
	$passou = true;
	if ($nome === 'a faixa comparada por string em vez de numero') {
		$passou = $mutante(array($PATINETE, $BARATO));
	} elseif ($nome === 'a frase da data escolhendo a primeira de duas') {
		$passou = $mutante(array($PATINETE, $OUTRO_DIA));
	} else {
		$passou = $mutante(array($PATINETE));
	}
	/* O MUTANTE TEM DE FALHAR. Se ele passa, a afirmacao que deveria pega-lo nao
	   existe — e o portao estaria verde sobre uma regra que nao vigia nada. */
	afirma($passou === false, sprintf('MUTACAO SOBREVIVEU: %s', $nome));
	if ($passou === false) { $mordeu++; }
}

printf("teste-caixa-da-mae: %d afirmacoes · 8 mundos fabricados (o dado de hoje e 1) · "
	. "%d de %d mutacoes reprovadas · %d falha(s)\n",
	$afirmacoes, $mordeu, count($mutacoes), count($falhas));
foreach ($falhas as $f) { print("  REPROVADO: $f\n"); }
exit(count($falhas) ? 1 : 0);

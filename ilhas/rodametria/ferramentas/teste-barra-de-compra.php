<?php
/**
 * A BARRA FIXA NAO PROMETE PRODUTO ONDE O BLOCO DE COMPRA DIZ QUE NAO HA
 * (09/11/2026, item 3 do despacho da ronda de hoje).
 *
 *   php ferramentas/teste-barra-de-compra.php
 *
 * O DEFEITO QUE ELE EXISTE PARA IMPEDIR, medido no HTML servido da revisao 70:
 * o componente `rdm-molde-barra` trazia `Ver produtos` ESCRITO A MAO no molde, e
 * em `/` o destino `#comprar` servia *"Nao temos o que recomendar aqui"* e em
 * `/peso-maximo-patinete-eletrico/` servia *"nenhum deles tem oferta aberta
 * hoje. Nao montamos vitrine com item sem link de loja, porque o botao que nao
 * leva a lugar nenhum e pior que a ausencia dele"*. A pagina escrevia a recusa e
 * servia, acima dela, um botao prometendo o que ela acabou de negar. Na F2, com
 * quatro cartoes, o MESMO rotulo estava certo — e e por isso que nenhum portao o
 * via: o literal acerta em um terco das paginas, e o verde dessa pagina ocupa o
 * espaco das outras duas.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a escolha do rotulo e decidida em PHP, e esta
 * regua CHAMA a funcao. Regua em Python sobre o texto do PHP conferiria a FORMA
 * do codigo e nunca a decisao — o mesmo motivo escrito no `teste-caixa-da-mae.php`,
 * no `teste-nota-de-preco.php` e no `teste-escada-de-compra.php`.
 *
 * AS TRES METADES:
 *
 *   1. A DECISAO. Mundos fabricados: lista vazia, um item, muitos, e os tipos
 *      que o PHP deixa chegar aqui (null, string, array associativo).
 *   2. O MUNDO DA DISCORDANCIA (20.8). A regra VELHA era o literal `Ver
 *      produtos`, e ela e refeita aqui ao lado da nova: as duas TEM de discordar
 *      na lista vazia, que e a home e a F3 de hoje. Autoteste em que as duas
 *      concordam nao mede conserto nenhum.
 *   3. TODA CHAMADA PASSA A LISTA. A funcao nao tem padrao para `$itens` de
 *      proposito — padrao `array()` daria o rotulo de "nao ha produto" a uma
 *      pagina COM produto, que e o mesmo defeito com o sinal trocado. O preco
 *      desse rigor e que esquecer o argumento e erro FATAL em PHP, e e por isso
 *      que a contagem de argumentos e conferida AQUI, no chao, antes do ar.
 */

foreach (array('add_filter', 'add_action', 'add_shortcode', 'register_activation_hook') as $f) {
	if (!function_exists($f)) { eval("function $f(){ return true; }"); }
}
if (!function_exists('esc_html')) {
	function esc_html($s) { return htmlspecialchars((string) $s, ENT_QUOTES); }
	function esc_attr($s) { return htmlspecialchars((string) $s, ENT_QUOTES); }
	function esc_url($s) { return (string) $s; }
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

/** OS ARGUMENTOS DE TOPO DE UMA LISTA DE ARGUMENTOS, cortados por virgula.
 *
 *  ELE E CIENTE DE ASPAS, E ISSO FOI MEDIDO POR ESTE PORTAO REPROVANDO NA
 *  SEGUNDA PASSADA (09/11/2026). A primeira versao contava profundidade de
 *  parenteses e colchetes e ignorava literais — e o titulo do bloco de compra da
 *  F2 e `'A venda agora, e o que cada um e'`, COM VIRGULA DENTRO. O corte partia
 *  o titulo em dois e devolvia `e o que cada um e'` como se fosse a lista de
 *  itens, acusando a F2 e a F3 de passarem listas diferentes quando elas passam
 *  a mesma. E a familia exata do corte de frase da regua de habilitacao, de
 *  06/11: o separador que parece obvio atravessa o literal.
 *
 *  UMA FUNCAO SO, usada pela contagem de argumentos E pela comparacao das listas:
 *  duas copias do mesmo corte comecariam iguais e so uma receberia o conserto
 *  (20.7), e e literalmente o defeito que este portao foi escrito para vigiar. */
function argumentos_de_topo($args) {
	$prof = 0; $pedacos = array(''); $aspa = '';
	for ($k = 0; $k < strlen($args); $k++) {
		$c = $args[$k];
		if ($aspa !== '') {
			$pedacos[count($pedacos) - 1] .= $c;
			if ($c === '\\') { $k++; if ($k < strlen($args)) { $pedacos[count($pedacos) - 1] .= $args[$k]; } }
			elseif ($c === $aspa) { $aspa = ''; }
			continue;
		}
		if ($c === '"' || $c === "'") { $aspa = $c; $pedacos[count($pedacos) - 1] .= $c; continue; }
		if ($c === '(' || $c === '[') { $prof++; }
		elseif ($c === ')' || $c === ']') { $prof--; }
		if ($c === ',' && $prof === 0) { $pedacos[] = ''; continue; }
		$pedacos[count($pedacos) - 1] .= $c;
	}
	return $pedacos;
}

$casca = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');

$falhas = array();
$afirmacoes = 0;
function afirma($cond, $msg) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if (!$cond) { $falhas[] = $msg; }
}

foreach (array('rodametria_casca_rotulo_do_atalho', 'rodametria_casca_barra_fixa') as $fn) {
	if (!carregar_funcao($casca, $fn)) {
		print("REPROVADO: `$fn` nao existe em snippets/rodametria-casca.php\n");
		exit(1);
	}
}

/* ---------------------------------------------------------------------------
 * 1. A DECISAO, EM MUNDOS FABRICADOS.
 * ------------------------------------------------------------------------ */
$PROMESSA = 'Ver produtos';

$mundos = array(
	'lista vazia (a home e a F3 de hoje)'      => array(array(),            false),
	'um cartao'                                 => array(array('a'),         true),
	'quatro cartoes (a F2 de hoje)'             => array(array(1, 2, 3, 4),  true),
	'null, que e o que um campo ausente entrega' => array(null,              false),
	'array associativo de cartoes'               => array(array('x' => 1),   true),
);

foreach ($mundos as $nome => $par) {
	list($itens, $deve_prometer) = $par;
	$rotulo = rodametria_casca_rotulo_do_atalho($itens);
	afirma($rotulo !== '', sprintf('mundo %s: o rotulo veio VAZIO. A barra sempre leva ao '
		. 'bloco, e o bloco sempre tem o que dizer', $nome));
	afirma(($rotulo === $PROMESSA) === $deve_prometer,
		sprintf('mundo %s: o rotulo e %s e %s deveria prometer produto',
			$nome, var_export($rotulo, true), $deve_prometer ? 'ELE' : 'NAO'));

	/* E A BARRA SERVIDA TEM DE CARREGAR ESSE ROTULO, nao outro: a funcao do
	   rotulo pode estar certa e a barra ignora-la, que e exatamente o que ela
	   fazia ate hoje. */
	$html = rodametria_casca_barra_fixa('Precisa de', '119', 'kg', $itens);
	afirma(strpos($html, '>' . esc_html($rotulo) . '</a>') !== false,
		sprintf('mundo %s: a barra servida nao traz o rotulo decidido (%s)', $nome, $rotulo));
	afirma(strpos($html, 'href="#comprar"') !== false,
		sprintf('mundo %s: a barra perdeu o atalho para #comprar', $nome));
	if (!$deve_prometer) {
		afirma(strpos($html, $PROMESSA) === false,
			sprintf('mundo %s: a barra servida PROMETE PRODUTO com a lista vazia. E o item 3 '
				. 'do despacho de 09/11/2026 de volta', $nome));
	}
}

/* ---------------------------------------------------------------------------
 * 2. O MUNDO DA DISCORDANCIA (20.8).
 *
 * A regra VELHA, refeita: o literal, sempre. Ela TEM de discordar da nova na
 * lista vazia — se concordarem, este portao nao mede conserto nenhum.
 * ------------------------------------------------------------------------ */
function velha_rotulo_literal($itens) { return 'Ver produtos'; }

$discordou = false;
foreach (array(array(), null) as $vazio) {
	if (rodametria_casca_rotulo_do_atalho($vazio) !== velha_rotulo_literal($vazio)) {
		$discordou = true;
	}
}
afirma($discordou, 'a regra NOVA e a VELHA (o literal `Ver produtos`) CONCORDAM na lista '
	. 'vazia. Concordancia aqui significa que o conserto do item 3 nao mudou nada');

/* E na lista CHEIA as duas tem de concordar: a F2 estava certa, e consertar o
   que nao estava quebrado seria regressao de texto na unica pagina sa. */
afirma(rodametria_casca_rotulo_do_atalho(array(1, 2, 3, 4)) === velha_rotulo_literal(array()),
	'na lista CHEIA a regra nova mudou o rotulo. A F2 servia `Ver produtos` com quatro '
	. 'cartoes e estava CERTA — o conserto nao pode afrouxar nem mexer nela');

/* ---------------------------------------------------------------------------
 * 3. NENHUM LITERAL DE PROMESSA SOBROU DENTRO DA BARRA, e TODA chamada passa a
 *    lista. O corte e sobre o FONTE, porque e la que o literal mora.
 * ------------------------------------------------------------------------ */
$i = strpos($casca, 'function rodametria_casca_barra_fixa(');
$j = strpos($casca, 'function rodametria_casca_rotulo_do_atalho(');
$corpo_barra = substr($casca, $i, strpos($casca, "\n}\n}", $i) - $i);
afirma(strpos($corpo_barra, $PROMESSA) === false,
	'o literal `Ver produtos` voltou para dentro de `rodametria_casca_barra_fixa`. O rotulo '
	. 'sai da decisao, nunca do molde');
afirma($j !== false && strpos($corpo_barra, 'rodametria_casca_rotulo_do_atalho') !== false,
	'`rodametria_casca_barra_fixa` nao chama `rodametria_casca_rotulo_do_atalho`');

/* A CONTAGEM DE ARGUMENTOS DE TODA CHAMADA, em todo snippet. Esquecer o quarto
   argumento e ArgumentCountError em PHP — pagina branca —, e este portao e o que
   impede isso de chegar ao ar. O corte atravessa quebra de linha de proposito:
   as quatro chamadas de verdade quebram a linha no quarto argumento. */
$chamadas = 0;
foreach (glob($RAIZ . '/snippets/*.php') as $arquivo) {
	$src  = file_get_contents($arquivo);
	$base = basename($arquivo);
	$pos  = 0;
	while (($p = strpos($src, 'rodametria_casca_barra_fixa(', $pos)) !== false) {
		$pos = $p + 1;
		/* A DEFINICAO nao e chamada. */
		if (substr($src, max(0, $p - 9), 9) === 'function ') { continue; }
		/* Recorta os argumentos equilibrando parenteses. */
		$abre = strpos($src, '(', $p);
		$n = 0; $fim = $abre;
		for ($k = $abre; $k < strlen($src); $k++) {
			if ($src[$k] === '(') { $n++; }
			elseif ($src[$k] === ')') { $n--; if ($n === 0) { $fim = $k; break; } }
		}
		$args = substr($src, $abre + 1, $fim - $abre - 1);
		$quantos = count(argumentos_de_topo($args));
		$chamadas++;
		afirma($quantos === 4, sprintf('%s: uma chamada a rodametria_casca_barra_fixa passa '
			. '%d argumento(s) e nao 4. O quarto e a MESMA lista que vai para o bloco de '
			. 'compra, e sem ele a chamada e erro fatal em PHP: `%s`',
			$base, $quantos, trim(preg_replace('/\s+/', ' ', $args))));
	}
}
afirma($chamadas >= 4, sprintf('achei %d chamada(s) a rodametria_casca_barra_fixa e esperava '
	. 'pelo menos 4 (F1, F2, F3 e produto). Regua que nao acha a chamada nao a confere',
	$chamadas));

/* E A LISTA DA BARRA E A MESMA EXPRESSAO QUE A DO BLOCO, no mesmo arquivo. Esta
   afirmacao e a que impede a volta do defeito por outro caminho: rotulo derivado
   de uma lista DIFERENTE da que monta o bloco e a mesma mentira com mais passos. */
/* A NORMALIZACAO E AS DUAS COISAS QUE ELA DESFAZ, E AS DUAS FORAM MEDIDAS POR
   ESTE PORTAO REPROVANDO NA PRIMEIRA PASSADA (09/11/2026). A comparacao literal
   acusou dois arquivos em que a lista E a mesma:

     - `rodametria-produto.php`: o bloco recebe `$pagina['vitrine']['cartoes']` e
       a barra recebe `(array) $pagina['vitrine']['cartoes']`. O cast nao e outra
       lista.
     - `rodametria-f2.php`: o bloco recebe `$itens`, atribuido duas linhas antes
       como `$itens = rodametria_f2_itens_da_vitrine( $d );`, e a barra — que mora
       em OUTRA funcao e nao alcanca aquele local — recebe a chamada. Mesma
       decisao, escrita como funcao de um lado e como variavel do outro.

   Entao a regua desfaz o cast e RESOLVE uma atribuicao simples. Ela NAO resolve
   mais de um nivel, e isso e deliberado: cadeia de variaveis e onde a "mesma
   lista" deixa de ser conferivel por leitura, e nesse caso o portao prefere
   REPROVAR e pedir que alguem escreva a expressao. Afrouxar a regua ate ela
   aprovar e o avesso do que a 20.8 manda. */
function normalizar_lista($e) {
	$e = trim(preg_replace('/\s+/', ' ', (string) $e));
	$e = trim(preg_replace('/^\(\s*array\s*\)/', '', $e));
	return trim($e);
}

/** Resolve UM nivel de atribuicao, e DENUNCIA ambiguidade em vez de escolher.
 *
 *  A PRIMEIRA VERSAO ESCOLHIA A PRIMEIRA ATRIBUICAO DO ARQUIVO, e este portao a
 *  reprovou na terceira passada (09/11/2026): na F2, `$itens` era o nome do local
 *  que recebe `rodametria_f2_itens_da_vitrine( $d )` E o nome do acumulador
 *  DENTRO daquela funcao (`$itens = array();`). A resolucao achava `array()`
 *  primeiro e acusava a F2 de passar uma lista diferente — errando pelo motivo
 *  oposto ao que ela vigia. Escolher a primeira de varias e adivinhar, e esta
 *  ilha ja escreveu a regra para isso na 20.7: *"zero `define` ou mais de um e
 *  DENUNCIA, nunca escolha. Espelho que adivinha a fonte nao e espelho."* */
function resolver_variavel($expr, $src) {
	if (!preg_match('/^\$[A-Za-z_][A-Za-z0-9_]*$/', $expr)) { return $expr; }
	$escapada = preg_quote($expr, '/');
	if (!preg_match_all('/' . $escapada . '\s*=\s*([^;]+);/', $src, $m)) {
		return $expr . ' (sem atribuicao achada)';
	}
	if (count($m[1]) > 1) {
		return $expr . ' (AMBIGUO: ' . count($m[1]) . ' atribuicoes no arquivo — '
			. 'escreva a expressao na chamada em vez de passar a variavel)';
	}
	return normalizar_lista($m[1][0]);
}

foreach (array('rodametria-f1.php', 'rodametria-f2.php', 'rodametria-f3.php',
		'rodametria-produto.php') as $base) {
	$src = file_get_contents($RAIZ . '/snippets/' . $base);
	if (!preg_match('/rodametria_casca_barra_fixa\((.*?)\);/s', $src, $mb)) { continue; }
	if (!preg_match('/rodametria_casca_bloco_de_compra\(\s*(.*?)\);/s', $src, $mc)) { continue; }

	/* O QUARTO argumento da barra e a lista; o SEGUNDO do bloco tambem o e
	   (titulo, itens, escopo, causa). Os dois cortes pelo MESMO cortador. */
	$arg_barra = argumentos_de_topo($mb[1]);
	$lista_barra = isset($arg_barra[3]) ? normalizar_lista($arg_barra[3]) : '';
	$lista_barra = resolver_variavel($lista_barra, $src);

	$arg_bloco = argumentos_de_topo($mc[1]);
	$lista_bloco = isset($arg_bloco[1]) ? normalizar_lista($arg_bloco[1]) : '';
	$lista_bloco = resolver_variavel($lista_bloco, $src);

	afirma($lista_barra !== '' && $lista_barra === $lista_bloco,
		sprintf('%s: a barra recebe `%s` e o bloco de compra recebe `%s`. Depois de desfazer '
			. 'o cast e resolver UMA atribuicao, as duas tem de ser a MESMA expressao — '
			. 'rotulo derivado de uma lista PARECIDA e a mesma mentira com mais passos',
			$base, $lista_barra, $lista_bloco));
}

/* ---------------------------------------------------------------------------
 * 4. A BARRA REPETE O NUMERO DA CAIXA, ENTAO REPETE O ROTULO DELA — UMA
 *    DECLARACAO, NAO DUAS (10/11/2026, 19h2xZ)
 * ------------------------------------------------------------------------ */
/* O DEFEITO QUE ISTO EXISTE PARA IMPEDIR, MEDIDO NO HTML SERVIDO DA REVISAO 77:
 * em `/veiculos/patinete-eletrico/` a caixa de resposta servia
 * `Preço mediano hoje` ao lado de `R$ 1.647,95`, e a barra fixa do rodape —
 * que serve O MESMO `$n['mediana']` — servia o adjetivo solto `Mediano`. Duas
 * declaracoes do mesmo fato na mesma pagina, as duas escritas a mao, e so uma
 * com o substantivo que diz mediano de QUE. `/veiculos/bicicleta-eletrica/`
 * servia o mesmo com `R$ 2.299,99`. E a 20.7 literal: *"duas declaracoes do
 * mesmo fato comecam iguais e so uma sobe"*.
 *
 * E A ILHA JA FAZIA CERTO EM QUATRO DOS CINCO LUGARES, o que e o que torna esta
 * regua uma regra medida e nao um gosto: a f1 e a f2 passam `$rotulo`/`$numero`
 * as DUAS chamadas, a f3 passa `$m['rotulo_precisa']`/`$r['carga_minima_tela']`
 * as duas, e so a `rodametria-produto.php` escrevia o rotulo uma SEGUNDA vez.
 * Nenhum portao a via, porque o rotulo da barra mora num `<span>` e as cinco
 * reguas de tela desta ilha leem PROSA (`<p>`, `<li>`, `<td>`...), ATRIBUTO e
 * JSON-LD — nunca `<span>` fora de prosa. E as cinco reguas, medidas sobre o
 * texto `Mediano`, dao ZERO: ele e acentuado, nao e chave de maquina e nao e
 * vocabulario de bastidor. Superficie nova nao pegaria este defeito; o que o
 * pega e exigir UMA declaracao.
 *
 * AS DUAS AFIRMACOES, E A SEGUNDA E A QUE MATA A CLASSE:
 *
 *   (a) MESMA EXPRESSAO. O rotulo e o numero da barra tem de ser, letra por
 *       letra, os de alguma chamada a `rodametria_casca_caixa` do MESMO arquivo
 *       e da MESMA funcao. A comparacao e sobre o TEXTO da expressao e nao
 *       resolve variavel de proposito: onde o texto ja concorda nao ha o que
 *       resolver, e onde ele discorda o portao quer que alguem escreva a
 *       declaracao UMA vez, nao que a regua afrouxe ate aprovar (20.8).
 *   (b) O ROTULO DA BARRA NUNCA E LITERAL. Escrever `'Preço mediano hoje'` nas
 *       duas chamadas satisfaria (a) e seria, no dia seguinte, o mesmo defeito:
 *       duas copias que comecam iguais. Exigir que a barra receba uma
 *       expressao — variavel ou campo do molde — torna a classe inteira
 *       impossivel, que e a licao da 32.1-b: *"prefixo proprio torna a classe
 *       inteira impossivel; conferir contra a lista conserta o caso de hoje"*.
 *       Medido: as quatro chamadas de verdade passam expressao, zero literal.
 *
 * O QUE ELA NAO ALCANCA, ESCRITO PARA NAO PARECER CONFERIDO (20.7): duas
 * variaveis de mesmo NOME em funcoes diferentes comparariam iguais sendo coisas
 * diferentes. E por isso que (a) exige a MESMA FUNCAO, e nao so o mesmo
 * arquivo — e nas quatro chamadas de verdade a caixa e a barra moram na mesma
 * funcao, medido e nao suposto. */

/** O nome da funcao que contem a posicao $pos, ou '' se nenhuma. */
function funcao_que_contem($src, $pos) {
	$nome = '';
	if (preg_match_all('/\bfunction\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(/', substr($src, 0, $pos), $m,
			PREG_OFFSET_CAPTURE)) {
		$ult = end($m[1]);
		$nome = $ult[0];
	}
	return $nome;
}

/** TODAS as chamadas a $nome em $src, como array de (args, posicao, funcao).
 *  A DEFINICAO nao e chamada — e a unica coisa que esta funcao descarta. */
function chamadas_de($src, $nome) {
	$out = array();
	$pos = 0;
	while (($p = strpos($src, $nome . '(', $pos)) !== false) {
		$pos = $p + 1;
		if (substr($src, max(0, $p - 9), 9) === 'function ') { continue; }
		$abre = strpos($src, '(', $p);
		$n = 0; $fim = $abre;
		for ($k = $abre; $k < strlen($src); $k++) {
			if ($src[$k] === '(') { $n++; }
			elseif ($src[$k] === ')') { $n--; if ($n === 0) { $fim = $k; break; } }
		}
		$out[] = array(
			'args'   => argumentos_de_topo(substr($src, $abre + 1, $fim - $abre - 1)),
			'pos'    => $p,
			'funcao' => funcao_que_contem($src, $p),
		);
	}
	return $out;
}

/** OS PROBLEMAS DE UMA FONTE, como lista de frases. Funcao pura sobre o TEXTO,
 *  para que os mundos fabricados abaixo possam prova-la sem tocar no disco. */
function problemas_de_rotulo_da_barra($base, $src) {
	$problemas = array();
	$barras = chamadas_de($src, 'rodametria_casca_barra_fixa');
	$caixas = chamadas_de($src, 'rodametria_casca_caixa');
	foreach ($barras as $b) {
		$rot = isset($b['args'][0]) ? normalizar_lista($b['args'][0]) : '';
		$num = isset($b['args'][1]) ? normalizar_lista($b['args'][1]) : '';

		/* (b) O ROTULO NUNCA E LITERAL. */
		if ($rot === '' || preg_match('/^([\'"]).*\1$/s', $rot)) {
			$problemas[] = sprintf('%s: a barra recebe o rotulo %s, escrito A MAO na chamada. '
				. 'O rotulo da barra e o da caixa que serve o MESMO numero, e declaracao '
				. 'repetida comeca igual e so uma sobe (20.7): passe a expressao que a '
				. 'caixa recebe', $base, $rot === '' ? '(nenhum)' : '`' . $rot . '`');
			continue;
		}

		/* (a) MESMA EXPRESSAO, MESMA FUNCAO. */
		$casou = false;
		$vistos = array();
		foreach ($caixas as $c) {
			$crot = isset($c['args'][0]) ? normalizar_lista($c['args'][0]) : '';
			$cnum = isset($c['args'][1]) ? normalizar_lista($c['args'][1]) : '';
			if ($c['funcao'] !== $b['funcao']) { continue; }
			$vistos[] = $crot . ' / ' . $cnum;
			if ($crot === $rot && $cnum === $num) { $casou = true; break; }
		}
		if (!$casou) {
			$problemas[] = sprintf('%s: a barra da funcao `%s` serve rotulo `%s` e numero `%s`, '
				. 'e nenhuma caixa da MESMA funcao serve esse par. As caixas de la servem: %s. '
				. 'A barra repete o numero da resposta, entao repete o rotulo dela — uma '
				. 'declaracao, nao duas (20.7)',
				$base, $b['funcao'], $rot, $num,
				$vistos ? '`' . implode('`, `', $vistos) . '`' : '(nenhuma)');
		}
	}
	return $problemas;
}

/* OS QUATRO ARQUIVOS DE VERDADE. */
$com_barra = 0;
foreach (glob($RAIZ . '/snippets/*.php') as $arquivo) {
	$src  = file_get_contents($arquivo);
	$base = basename($arquivo);
	if (!chamadas_de($src, 'rodametria_casca_barra_fixa')) { continue; }
	$com_barra++;
	$ps = problemas_de_rotulo_da_barra($base, $src);
	afirma(!$ps, implode(' | ', $ps));
}
afirma($com_barra === 4, sprintf('achei barra fixa em %d arquivo(s) e esperava 4 (f1, f2, f3 '
	. 'e produto). Regua que nao acha a chamada nao a confere', $com_barra));

/* OS MUNDOS FABRICADOS, E O PRIMEIRO E O AR DE VERDADE DA REVISAO 77 (20.8):
   autoteste em que a regua velha e a nova concordam nao mede conserto nenhum. */
$MOLDE = 'function rdm_x() { $rotulo = %s; $numero = $n[\'mediana\']; '
	. '$html = rodametria_casca_caixa( %s, %s, \'\', $f, \'verde\' ); '
	. '$html .= rodametria_casca_barra_fixa( %s, %s, \'\', $c ); return $html; }';

$mundos_de_rotulo = array(
	/* nome => array(rotulo da caixa, numero da caixa, rotulo da barra, numero da barra, deve_reprovar) */
	'O AR DA REVISAO 77: caixa `Preço mediano hoje`, barra `Mediano`, MESMO numero'
		=> array("'Preço mediano hoje'", "\$n['mediana']", "'Mediano'", "\$n['mediana']", true),
	'o conserto desta passada: as duas pela MESMA variavel'
		=> array('$rotulo', '$numero', '$rotulo', '$numero', false),
	'o conserto FALSO: o mesmo literal escrito DUAS vezes (satisfaz (a) e cai em (b))'
		=> array("'Preço mediano hoje'", "\$n['mediana']", "'Preço mediano hoje'", "\$n['mediana']", true),
	'rotulo igual e NUMERO diferente: a barra serve outra resposta'
		=> array('$rotulo', '$numero', '$rotulo', "\$n['faixa']", true),
	'a f3 de hoje: campo do molde nas duas'
		=> array("\$m['rotulo_precisa']", "\$r['carga_minima_tela']",
			"\$m['rotulo_precisa']", "\$r['carga_minima_tela']", false),
);

foreach ($mundos_de_rotulo as $nome => $m) {
	list($crot, $cnum, $brot, $bnum, $deve) = $m;
	$src = sprintf($MOLDE, $crot, $crot, $cnum, $brot, $bnum);
	$ps  = problemas_de_rotulo_da_barra('(mundo fabricado)', $src);
	afirma($deve === (bool) count($ps), sprintf('mundo %s: esperava %s e a regua deu %s%s',
		$nome, $deve ? 'REPROVADO' : 'aprovado', count($ps) ? 'REPROVADO' : 'aprovado',
		count($ps) ? ' (' . implode(' | ', $ps) . ')' : ''));
}

/* A BARRA SEM CAIXA NENHUMA TEM DE REPROVAR: numero na barra que a pagina nao
   declara em lugar nenhum e resposta sem fonte na tela. */
$ps = problemas_de_rotulo_da_barra('(mundo fabricado)',
	'function rdm_y() { return rodametria_casca_barra_fixa( $rotulo, $numero, \'\', $c ); }');
afirma(count($ps) === 1, 'mundo barra SEM caixa: esperava REPROVADO e a regua aprovou');

/* E A FUNCAO IMPORTA: caixa certa em OUTRA funcao nao vale pela barra desta. */
$ps = problemas_de_rotulo_da_barra('(mundo fabricado)',
	'function rdm_a() { return rodametria_casca_caixa( $rotulo, $numero, \'\', $f, \'verde\' ); } '
	. 'function rdm_b() { return rodametria_casca_barra_fixa( $rotulo, $numero, \'\', $c ); }');
afirma(count($ps) === 1,
	'mundo caixa em OUTRA funcao: esperava REPROVADO e a regua aprovou (a variavel tem o '
	. 'mesmo nome e nao e o mesmo local)');

printf("teste-barra-de-compra: %d afirmacoes · %d mundos fabricados · %d chamada(s) "
	. "conferida(s) · %d falha(s)\n",
	$afirmacoes, count($mundos), $chamadas, count($falhas));
foreach ($falhas as $f) { print("  REPROVADO: $f\n"); }
exit(count($falhas) ? 1 : 0);

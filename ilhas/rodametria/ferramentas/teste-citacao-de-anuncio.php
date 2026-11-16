<?php
/**
 * O TITULO DE ANUNCIO QUE PROMETE HABILITACAO VAI ENTRE ASPAS (16/11/2026).
 *
 *   php ferramentas/teste-citacao-de-anuncio.php
 *
 * O DEFEITO QUE ELE EXISTE PARA IMPEDIR FOI MEDIDO NO AR, e nao suposto: as
 * 10h4xZ de 16/11/2026, em `https://rodametria.com.br/veiculos/moto-eletrica/`,
 * revisao 95, `conferir-no-ar.py` reprovou com **6 afirmacoes sobre HABILITACAO
 * sem nenhuma das oracoes de recusa desta ilha**. Nenhuma delas foi escrita por
 * nos: sao os DOIS titulos que a loja devolveu para a chave `moto eletrica
 * adulto` — `(...) Painel Led - SEM CNH` e `(...) Adulto Sem Cnh Bluetooth Re` —
 * servidos no nome do cartao, na celula da tabela e no `name` do `ItemList`.
 *
 * Do lado de fora o elemento do cartao e UMA cadeia so: o titulo da loja mais a
 * nossa prosa ("declara watt, sem dizer se e nominal ou de pico", "Ver na
 * Shopee"). Lida inteira, a pagina PARECE afirmar que a moto dispensa
 * habilitacao — e mandar alguem para a rua sem habilitacao e o unico erro que o
 * "Especifico desta ilha" do `PROMPT.md` chama de grave.
 *
 * A LICENCA NAO FOI INVENTADA: `_so_dentro_de_citacao`, da regua de afirmacao de
 * tela, absolve o token que esta DENTRO de aspas, e a home desta ilha ja cita um
 * titulo de anuncio assim desde 06/11. O que faltava era o titulo CHEGAR entre
 * aspas na pagina de produto.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a decisao e tomada em PHP
 * (`rodametria_casca_nome_de_anuncio()`), e esta regua CHAMA a funcao. Regua em
 * Python sobre o texto do PHP conferiria a FORMA e nunca a decisao — o mesmo
 * motivo escrito no `teste-menu-da-casca.php` e no `teste-barra-de-compra.php`.
 *
 * AS QUATRO METADES:
 *   1. OS DOIS TITULOS DO AR, lidos de `dados/anuncios-por-consulta.json` e
 *      NUNCA digitados aqui: os dois tem de sair entre aspas. No dia em que a
 *      loja os aposentar, a afirmacao cai com eles — e e o que se quer.
 *   2. O MUNDO DA DISCORDANCIA (20.8): a regra VELHA (servir o nome cru) e
 *      refeita ao lado da nova, e as duas TEM de discordar exatamente nos
 *      titulos que carregam o token. Autoteste em que as duas concordam nao
 *      mede conserto nenhum.
 *   3. A CITACAO NAO E ANISTIA: titulo SEM o token sai cru, e titulo que ja
 *      chega entre aspas nao ganha um segundo par.
 *   4. O TOKEN SE ACHA SEM ACENTO (32.4-e): `habilitação` com acento tem de ser
 *      achado, senao a mesma palavra passa com o traje de cima.
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

/** Carrega UMA funcao de um snippet, equilibrando chaves. Copiado do
 *  `teste-menu-da-casca.php` desta mesma pasta. */
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

$falhas = array();
$afirmacoes = 0;
function afirma($cond, $msg) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if (!$cond) { $falhas[] = $msg; }
}

$src = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
if (!carregar_funcao($src, 'rodametria_casca_nome_de_anuncio')) {
	print("REPROVADO: `rodametria_casca_nome_de_anuncio()` nao existe na casca.\n");
	exit(1);
}

$ABRE  = json_decode('"“"');
$FECHA = json_decode('"”"');

/** A regra VELHA, refeita aqui para a 20.8: o nome ia cru para a tela. */
function regra_velha($nome) { return (string) $nome; }

/* --------------------------------------------------------------- 1 e 2 */
/* OS TITULOS SAEM DA COLHEITA, NUNCA DIGITADOS NESTA REGUA. */
$banco = json_decode(file_get_contents($RAIZ . '/dados/anuncios-por-consulta.json'), true);
$com_token = array();
$sem_token = array();
foreach ($banco['consultas'] as $bloco) {
	foreach ($bloco['anuncios'] as $a) {
		$t = (string) $a['titulo'];
		$chato = false;
		foreach (array('cnh', 'habilitac', 'habilitad') as $tok) {
			$plano = @iconv('UTF-8', 'ASCII//TRANSLIT', $t);
			if (false !== strpos(strtolower(false === $plano ? $t : $plano), $tok)) { $chato = true; }
		}
		if ($chato) { $com_token[] = $t; } else { $sem_token[] = $t; }
	}
}

afirma(count($com_token) >= 2,
	sprintf('a colheita desta ilha tem %d titulo(s) com token de habilitacao e esta '
		. 'regua precisa de ao menos 2 para medir o mundo do ar de 16/11', count($com_token)));

foreach ($com_token as $t) {
	$novo = rodametria_casca_nome_de_anuncio($t);
	afirma($novo === $ABRE . $t . $FECHA,
		sprintf('titulo da loja com token NAO saiu entre aspas: %s', mb_substr($novo, 0, 70)));
	afirma($novo !== regra_velha($t),
		sprintf('a regra nova e a VELHA concordam neste titulo, e tinham de discordar: %s',
			mb_substr($t, 0, 70)));
	/* O TEXTO DE DENTRO E O DA LOJA, LETRA POR LETRA: aspas que mexem no titulo
	   deixariam de ser citacao e passariam a ser edicao. */
	afirma(mb_substr($novo, 1, mb_strlen($novo) - 2) === $t,
		'as aspas mexeram no titulo: citacao que edita o citado nao e citacao');
}

/* --------------------------------------------------------------------- 3 */
foreach ($sem_token as $t) {
	$afirmacoes++;
	if (rodametria_casca_nome_de_anuncio($t) !== $t) {
		$falhas[] = sprintf('titulo SEM token ganhou aspas (a citacao viraria anistia geral): %s',
			mb_substr($t, 0, 70));
	}
}
afirma(count($sem_token) >= 10,
	sprintf('a colheita precisa de titulos SEM token para a outra metade da regua: %d',
		count($sem_token)));

$ja_citado = $ABRE . 'Scooter Moto Elétrica 1000w Adulto Sem Cnh Bluetooth Ré' . $FECHA;
afirma(rodametria_casca_nome_de_anuncio($ja_citado) === $ja_citado,
	'titulo que JA chega entre aspas ganhou um segundo par');
afirma(rodametria_casca_nome_de_anuncio('"Moto sem CNH"') === '"Moto sem CNH"',
	'titulo entre aspas RETAS ganhou um segundo par — a regua de citacao le as duas formas');
afirma(rodametria_casca_nome_de_anuncio('') === '',
	'nome vazio nao devolve um par de aspas vazio');

/* --------------------------------------------------------------------- 4 */
$com_acento = 'Moto Elétrica Adulto sem habilitação, 1000w';
afirma(rodametria_casca_nome_de_anuncio($com_acento) === $ABRE . $com_acento . $FECHA,
	'`habilitação` COM acento nao foi achado: a mesma palavra passaria com o traje de cima (32.4-e)');
$vizinho = 'Patinete Elétrico Adulto 350W Dobrável 30km/h';
afirma(rodametria_casca_nome_de_anuncio($vizinho) === $vizinho,
	'titulo de patinete comum ganhou aspas');

print(sprintf("teste-citacao-de-anuncio: %d afirmacoes, %d falha(s)\n", $afirmacoes, count($falhas)));
foreach ($falhas as $f) { print("  FALHA  $f\n"); }
print(count($falhas) ? "REPROVADO\n" : "APROVADO\n");
exit(count($falhas) ? 1 : 0);

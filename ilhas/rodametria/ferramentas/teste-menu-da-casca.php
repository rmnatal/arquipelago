<?php
/**
 * O MENU DO CABECALHO MOSTRA O QUE O MAPA MANDA MOSTRAR, E O CAMPO QUE DECIDE E
 * LIDO (09/11/2026).
 *
 *   php ferramentas/teste-menu-da-casca.php
 *
 * O DEFEITO QUE ELE EXISTE PARA IMPEDIR, MEDIDO NO AR as 19h4xZ de 09/11/2026,
 * no navegador desta nuvem, nas 10 URLs do sitemap: o menu servia TRES itens —
 * `Autonomia` (F2), `Carga maxima` (F3) e `Veiculos` — e a **F1 nao aparecia em
 * nenhum deles**. A F1 e a ferramenta principal desta ilha (a categoria da
 * Resolucao 996/2023, que e a tese do site) e mora NA HOME; quem chegasse por
 * busca numa pagina filha e abrisse o menu no celular nao tinha como chegar a
 * ela por ali. A causa estava em `rodametria_casca_nav_html()`:
 *
 *     if ( 'inicio' === $slug || ! empty( $p['no_menu'] ) ) { continue; }
 *
 * O literal pulava a home SEMPRE, e o mapa da casca declarava
 * `'no_menu' => false` para a mesma pagina, tres linhas acima. **Duas
 * declaracoes do mesmo fato, e a lida era a que ninguem tinha escrito de
 * proposito** — a familia exata da 20.7 do contrato (*"as constantes eram lidas
 * por NINGUEM"*) e da 32.5-d (*"a regra que nunca rodou contra o dado de verdade
 * esta quebrada e parece sa"*). O campo nao estava errado: estava MORTO.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a escolha do item e do rotulo e decidida em
 * PHP, e esta regua CHAMA as funcoes. Regua em Python sobre o texto do PHP
 * conferiria a FORMA do codigo e nunca a decisao — o mesmo motivo escrito no
 * `teste-barra-de-compra.php`, no `teste-caixa-da-mae.php` e no
 * `teste-nota-de-preco.php`.
 *
 * AS TRES METADES:
 *
 *   1. O CAMPO DECIDE. Mundos fabricados: entrada sem `no_menu`, com
 *      `no_menu => false`, com `no_menu => true`, e a home entre elas. Nenhum
 *      slug e tratado por nome.
 *   2. O MUNDO DA DISCORDANCIA (20.8). A regra VELHA — o literal `'inicio' ===
 *      $slug` — e refeita aqui ao lado da nova, e as duas TEM de discordar
 *      exatamente na home. Autoteste em que as duas concordam nao mede conserto
 *      nenhum.
 *   3. O ROTULO NAO ATROPELA A TRILHA. `menu_rotulo` vence `nome` no menu, e
 *      `nome` continua intacto, porque e dele que sai o degrau da trilha da
 *      16.3. Uma afirmacao para cada superficie, separadas, como a 20.5 manda.
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
 *  registra filtros ao ser lido, entao ele nao pode ser incluido. Copiado do
 *  `teste-barra-de-compra.php` desta mesma pasta. */
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

function codigo_sem_comentario($php) {
	$fora = '';
	foreach (token_get_all('<?php ' . $php) as $t) {
		if (is_array($t)) {
			if (T_COMMENT === $t[0] || T_DOC_COMMENT === $t[0]) { $fora .= ' '; continue; }
			$fora .= $t[1];
		} else { $fora .= $t; }
	}
	return $fora;
}

$src = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
$falhas = 0;
$afirmacoes = 0;
function vale($ok, $nome, $detalhe = '') {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	echo ($ok ? "  ok    " : "  FALHA ") . $nome . ($ok ? "" : "\n          " . $detalhe) . "\n";
	if (!$ok) { $falhas++; }
}

/* ------------------------------------------------------------------ 1. O CAMPO
   A funcao do ar monta <li> e depende de `rodametria_casca_url_do_slug()`, que
   fala com o WordPress. Entao a DECISAO e isolada aqui do mesmo jeito que ela
   esta escrita la: o campo `no_menu`, e so ele.                              */
if (!carregar_funcao($src, 'rodametria_casca_rotulo_de_menu')) {
	echo "  FALHA  `rodametria_casca_rotulo_de_menu()` nao existe na casca\n";
	exit(1);
}

/* A LINHA DE DECISAO SAI DO FONTE, nunca e reescrita aqui: portao que copia a
   regra para dentro de si mesmo passa a medir a propria copia, e foi assim que
   um comentario desta ilha declarou um mecanismo que nao existia (20.7).
   E ELE LE CODIGO, NAO PROSA — ESTE PORTAO REPROVOU QUEM O ESCREVEU AQUI, na
   primeira passada, as 19h5xZ de 09/11/2026. O comentario que o conserto deixou
   na casca EXPLICA o literal que saiu (*"antes de 09/11 esta linha trazia tambem
   `'inicio' === $slug`"*), e a busca por texto cru o achou dentro do proprio
   comentario e reprovou a casca JA CONSERTADA. E a 32.4-b pelo avesso: la a
   regua lia o visivel e o defeito morava no comentario; aqui ela lia o
   comentario e o mecanismo morava no codigo. `token_get_all()` separa os dois
   sem adivinhar nada — e ele e do PHP, nao uma regra minha sobre `/*`. */
$i = strpos($src, 'function rodametria_casca_nav_html(');
$corpo = codigo_sem_comentario(substr($src, $i, 1800));
vale(strpos($corpo, "'inicio' === \$slug") === false,
	"o literal `'inicio' === \$slug` NAO decide mais o menu",
	"ele voltou ao corpo de rodametria_casca_nav_html() — e com ele a F1 sai do menu de novo");
vale(strpos($corpo, "! empty( \$p['no_menu'] )") !== false,
	"quem decide e o campo `no_menu`",
	"a condicao do `continue` nao le mais o campo: menu que nao le o mapa nao e menu do mapa");
vale(strpos($corpo, 'rodametria_casca_rotulo_de_menu(') !== false,
	"o rotulo do item sai de `rodametria_casca_rotulo_de_menu()`",
	"voltou a sair de \$p['nome'] direto, e com isso a home volta a se chamar `Inicio` no menu");

/* O campo da home no MAPA, lido do fonte: `no_menu => false` deixou de ser
   declaracao morta, entao se alguem o trocar o menu muda de verdade. */
$j = strpos($src, "'inicio' => array(");
/* SEM COMENTARIO TAMBEM AQUI, e pelo mesmo motivo de cima: a entrada da home
   carrega o paragrafo que explica a troca, e paragrafo que repete o nome do
   campo faria esta afirmacao passar sobre a prosa em vez do codigo. */
$entrada = codigo_sem_comentario(substr($src, $j, 2600));
vale(strpos($entrada, "'no_menu'     => false") !== false,
	"a home declara `no_menu => false` no mapa",
	"sem a declaracao, o menu da ilha perde a pagina da F1 sem nenhum portao vermelho");
vale(preg_match("/'menu_rotulo' => '([^']+)'/", $entrada, $m) === 1,
	"a home declara um `menu_rotulo` proprio");
$rotulo_da_home = isset($m[1]) ? $m[1] : '';
vale($rotulo_da_home !== '' && $rotulo_da_home !== 'Início',
	"o `menu_rotulo` da home NAO e `Inicio`: ele nomeia o que a ferramenta entrega",
	"`Inicio` no menu nomeia o lugar e nao a resposta, e e justamente por isso que a F1 ficava sem nome");
vale(strpos($entrada, "'nome'        => 'Início'") !== false,
	"o `nome` da home continua `Inicio`, porque dele sai a trilha da 16.3",
	"trocar o `nome` conserta o menu e estraga o breadcrumb — uma superficie de cada vez (20.5)");

/* ------------------------------------- 2. A REGRA VELHA AO LADO DA NOVA (20.8)
   As duas TEM de discordar na home. Se concordarem, o conserto nao existe.   */
$mapa_fabricado = array(
	'inicio'    => array('nome' => 'Início', 'menu_rotulo' => 'Categoria e placa', 'no_menu' => false),
	'f2'        => array('nome' => 'Autonomia'),
	'f3'        => array('nome' => 'Carga máxima', 'no_menu' => false),
	'escondida' => array('nome' => 'Nao me mostre', 'no_menu' => true),
	'sem_nome'  => array(),
);
$velha = function ($slug, $p) { return !('inicio' === $slug || !empty($p['no_menu'])); };
$nova  = function ($slug, $p) { return empty($p['no_menu']); };
$discordam = array();
foreach ($mapa_fabricado as $slug => $p) {
	if ($velha($slug, $p) !== $nova($slug, $p)) { $discordam[] = $slug; }
}
vale($discordam === array('inicio'),
	"a regra velha e a nova discordam em EXATAMENTE um slug, e ele e `inicio`",
	"discordaram em: " . (implode(', ', $discordam) ?: 'nenhum') . " — autoteste em que as duas concordam nao mede conserto nenhum");

$mostrados = array();
foreach ($mapa_fabricado as $slug => $p) {
	if ($nova($slug, $p)) { $mostrados[$slug] = rodametria_casca_rotulo_de_menu($slug, $p); }
}
vale(array_keys($mostrados) === array('inicio', 'f2', 'f3', 'sem_nome'),
	"a regra nova mostra as quatro elegiveis e esconde a de `no_menu => true`",
	"mostrou: " . implode(', ', array_keys($mostrados)));
vale(isset($mostrados['inicio']) && 'Categoria e placa' === $mostrados['inicio'],
	"a home entra no menu com o rotulo do campo, nao com o `nome`");
vale(isset($mostrados['f2']) && 'Autonomia' === $mostrados['f2'],
	"entrada SEM `menu_rotulo` usa o `nome`");
vale(isset($mostrados['sem_nome']) && 'sem_nome' === $mostrados['sem_nome'],
	"entrada sem `nome` nenhum cai no slug em vez de sair vazia",
	"item de menu com rotulo vazio e link invisivel: pior que link que falta");

/* ----------------------------------------------- 3. OS TIPOS QUE CHEGAM ALI
   O mapa passa pelo filtro `rodametria_paginas`, entao entrada de snippet pode
   vir de qualquer forma. A funcao nao pode estourar com nenhuma delas.       */
foreach (array('nulo' => null, 'cadeia' => 'x', 'lista' => array(1, 2), 'vazio' => array()) as $nome => $p) {
	$r = rodametria_casca_rotulo_de_menu('alvo', $p);
	vale('alvo' === $r, "entrada do tipo `$nome` cai no slug sem estourar", "devolveu: " . var_export($r, true));
}
vale('' === rodametria_casca_rotulo_de_menu('', array()), "slug vazio devolve cadeia vazia, e nao a palavra `Array`");
vale('Só nome' === rodametria_casca_rotulo_de_menu('x', array('nome' => 'Só nome', 'menu_rotulo' => '')),
	"`menu_rotulo` VAZIO nao ganha do `nome`",
	"cadeia vazia e ausencia, nao escolha — rotulo vazio apagaria o item do menu");

echo "\n";
if ($falhas) {
	echo "  REPROVADO — $falhas de $afirmacoes afirmacoes\n";
	exit(1);
}
echo "  APROVADO — $afirmacoes afirmacoes, 0 falha\n";
exit(0);

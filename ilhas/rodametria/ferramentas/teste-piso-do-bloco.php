<?php
/**
 * O BLOCO DE COMPRA QUE NASCEU SEM CARTAO SERVE O PISO DA 25.2 (25/11/2026).
 *
 *   php ferramentas/teste-piso-do-bloco.php
 *
 * O DEFEITO QUE ELE EXISTE PARA FECHAR FOI MEDIDO NO AR, nas QUATRO categorias
 * que a F1 devolve, pela ronda diaria de 25/11/2026 as 15h1xZ: a HOME — a
 * ferramenta principal desta ilha — servia o bloco "À venda agora nesta
 * categoria" executando o formulario de verdade e contando
 * `a[href*="shopee"]` no documento depois de cada resposta. Quatro medicoes,
 * quatro ZEROS:
 *
 *     350 W  · 25 km/h · so pedal   -> bicicleta eletrica     -> 0 links
 *     500 W  · 25 km/h · acelerador -> autopropelido          -> 0 links
 *   1.500 W  · 40 km/h · acelerador -> ciclomotor             -> 0 links
 *   5.000 W  · 80 km/h · acelerador -> acima do ciclomotor    -> 0 links
 *
 * E O PISO DAQUELAS PRATELEIRAS ESTAVA PUBLICADO NO BANCO DESDE 16/11, com os
 * tres campos nas 3 de 3 consultas. A causa nao era de dado, era de LUGAR — a
 * 25.2-c um andar acima da pagina de produto, que pagou a MESMA classe em
 * 19/11 em `/veiculos/moto-eletrica/`. La o piso morava dentro do bloco da
 * vitrine, que nao nasce quando o mercado nao serve produto; aqui o bloco
 * NASCE, e estava nascendo mudo.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a decisao e tomada em PHP
 * (`rodametria_casca_piso_do_bloco()` e os dois chamadores dela), e esta regua
 * CHAMA as funcoes de verdade. Regua em Python sobre o texto do PHP conferiria
 * a FORMA e nunca a decisao — o mesmo motivo escrito no
 * `teste-piso-da-caixa.php`, no `teste-cabeca-sem-vitrine.php` e no
 * `teste-barra-de-compra.php`.
 *
 * AS SETE METADES:
 *   1. O PISO CHEGA A TELA: bloco sem cartao e com `url_busca` serve a busca
 *      ENCURTADA, byte por byte igual a do dado.
 *   2. `rel="sponsored"` E `noopener` NO PROPRIO `<a>`, cobrados no pedaco de
 *      HTML da tag e nao na pagina inteira: `sponsored` em qualquer outro lugar
 *      nao prova nada sobre ESTE link (a cicatriz da 20.7).
 *   3. A AUSENCIA E DITA, NUNCA MAQUIADA (20.8): sem piso no dado, o bloco diz
 *      que a tela esta sem link de loja e NAO serve `href` vazio — que nao e
 *      botao morto e sim um botao que RECARREGA A PROPRIA PAGINA.
 *   4. A DIVULGACAO ANDA COM O LINK: link de afiliado na tela sem a frase da
 *      comissao e o que a secao 7 proibe, e com cartao ela ja saia; com piso e
 *      sem cartao ela nao saia.
 *   5. BLOCO COM CARTAO NAO SERVE PISO: dentro do cartao a escada da 25.2 ja
 *      decide quem sobe, e um segundo piso ao lado seria a mesma informacao
 *      duas vezes (20.7).
 *   6. AS QUATRO CATEGORIAS DA F1 TEM DESTINO E FRASE, e a frase traz o nome
 *      ACENTUADO da prateleira — nunca a `chave` ASCII do banco. E os dois
 *      mundos sem piso tem frases DIFERENTES: sem categoria e sem prateleira
 *      sao causas diferentes, e causa trocada e causa errada na cara de quem le.
 *   7. O MUNDO DA DISCORDANCIA (20.8): o bloco VELHO — o de antes deste
 *      conserto, refeito aqui ao lado — e o novo TEM de discordar no mundo
 *      medido (zero cartao, piso no dado) e CONCORDAR no mundo sem piso, onde
 *      nenhum dos dois tem o que servir. Autoteste em que as duas reguas
 *      concordam sempre nao mede conserto nenhum.
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
 *  `teste-piso-da-caixa.php` desta mesma pasta. */
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

$falhas = 0;
$afirmacoes = 0;
function vale($ok, $nome, $detalhe = '') {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	echo ($ok ? "  ok    " : "  FALHA ") . $nome . ($ok ? "" : "\n          " . $detalhe) . "\n";
	if (!$ok) { $falhas++; }
}

/* O CARTAO E SUBSTITUIDO e o BLOCO e o de verdade: o que esta sob julgamento e
   a decisao do bloco sobre o piso, nao o traje do cartao — que tem portao
   proprio. */
function rodametria_casca_cartao_de_compra($item) {
	return '<li class="rdm-molde-cartao">' . esc_html((string) $item['nome']) . '</li>';
}

$casca = file_get_contents($RAIZ . '/snippets/rodametria-casca.php');
foreach (array('rodametria_casca_rotulo_do_piso', 'rodametria_casca_piso_do_bloco',
               'rodametria_casca_bloco_de_compra') as $fn) {
	if (!carregar_funcao($casca, $fn)) {
		echo "FALHA: nao achei `$fn()` na casca\n";
		exit(1);
	}
}

$f1src = file_get_contents($RAIZ . '/snippets/rodametria-f1.php');
foreach (array('rodametria_f1_piso_da_categoria', 'rodametria_f1_piso_para_o_js') as $fn) {
	if (!carregar_funcao($f1src, $fn)) {
		echo "FALHA: nao achei `$fn()` no snippet da F1\n";
		exit(1);
	}
}
$f3src = file_get_contents($RAIZ . '/snippets/rodametria-f3.php');
if (!carregar_funcao($f3src, 'rodametria_f3_piso_da_busca')) {
	echo "FALHA: nao achei `rodametria_f3_piso_da_busca()` no snippet da F3\n";
	exit(1);
}

/** O BLOCO VELHO, de antes deste conserto: ele NUNCA serve piso, porque o piso
 *  nao chegava a ele. Existe para DISCORDAR (20.8). */
function bloco_velho($titulo, $itens, $escopo, $vazio) {
	$cartoes = '';
	foreach ((array) $itens as $item) { $cartoes .= rodametria_casca_cartao_de_compra($item); }
	$duplicada = ('' === $cartoes && '' !== trim((string) $vazio)
		&& trim((string) $escopo) === trim((string) $vazio));
	$html = '<section class="rdm-molde-compra" id="comprar">';
	$html .= '<h2 class="rdm-molde-compra-titulo">' . esc_html($titulo) . '</h2>';
	if (!$duplicada) { $html .= '<p class="rdm-molde-compra-escopo">' . esc_html($escopo) . '</p>'; }
	if ('' === $cartoes) {
		$html .= '<p class="rdm-molde-compra-vazio">' . esc_html($vazio) . '</p>';
	} else {
		$html .= '<ul class="rdm-molde-carrossel">' . $cartoes . '</ul>';
	}
	return $html . '</section>';
}

/** O pedaco de HTML da ancora do piso, para as afirmacoes nao medirem a pagina
 *  inteira (20.7). Devolve '' quando nao houver ancora. */
function tag_do_piso($html) {
	$i = strpos($html, '<a ');
	if (false === $i) { return ''; }
	$j = strpos($html, '</a>', $i);
	return substr($html, $i, $j - $i + 4);
}

$DADOS = json_decode(file_get_contents($RAIZ . '/dados/anuncios-por-consulta.json'), true);
$PISO_PATINETE = null;
$PISO_MOTO = null;
foreach ((array) $DADOS['consultas'] as $c) {
	if ('veiculos/patinete-eletrico' === $c['slug']) { $PISO_PATINETE = $c['piso_da_busca']; }
	if ('veiculos/moto-eletrica' === $c['slug']) { $PISO_MOTO = $c['piso_da_busca']; }
}

$F1 = json_decode(file_get_contents($RAIZ . '/dados/f1-respostas.json'), true);
$F3 = json_decode(file_get_contents($RAIZ . '/dados/f3-respostas.json'), true);

echo "O BLOCO DE COMPRA SEM CARTAO SERVE O PISO DA 25.2 — RODAMETRIA (sem rede)\n\n";

/* ---------------------------------------------------------------------------
 * 1 a 4. O MUNDO MEDIDO EM 25/11/2026: bloco sem cartao, piso no dado.
 * ------------------------------------------------------------------------- */
echo "1-4. O MUNDO MEDIDO: zero cartao e piso no dado\n";
$frase = 'A busca desta prateleira está aberta, e ela não é uma lista conferida.';
$novo = rodametria_casca_bloco_de_compra(
	'À venda agora nesta categoria', array(), 'a causa', 'a causa',
	array('url_busca' => $PISO_PATINETE['url_busca'], 'frase' => $frase));

vale(false !== strpos($novo, $PISO_PATINETE['url_busca']),
	'o bloco serve a busca ENCURTADA do dado, byte por byte',
	'nao achei ' . $PISO_PATINETE['url_busca'] . ' em: ' . substr($novo, 0, 400));
vale(false !== strpos($novo, $frase),
	'a frase do chamador vai para a tela (texto de tela da ferramenta mora no dado)');
$tag = tag_do_piso($novo);
vale('' !== $tag && false !== strpos($tag, 'rel="sponsored noopener"'),
	'`rel="sponsored noopener"` no PROPRIO `<a>` do piso', 'a tag veio: ' . $tag);
vale('' !== $tag && false !== strpos($tag, 's.shopee.com.br')
	&& false === strpos($tag, 'rodametria.com.br'),
	'o destino do piso e a LOJA e nunca uma URL desta ilha', 'a tag veio: ' . $tag);
vale(false !== strpos($novo, 'Link de afiliado'),
	'a frase da comissao anda com o link (secao 7): link de afiliado na tela sem '
	. 'ela e o que a secao proibe');
vale(false === strpos($novo, 'href=""'),
	'nenhum `href` vazio — botao que recarrega a propria pagina nao e botao morto, '
	. 'e a cicatriz e de 30/10/2026 nesta ilha');
/* O PISO E ALTO DENTRO DO BLOCO (32.5): ele vem antes do fim da secao e nao
   depois de nenhum `<h2>` novo, porque e a unica saida de compra da tela. */
vale(strpos($novo, '<a ') < strpos($novo, '</section>'),
	'o piso esta DENTRO do bloco de compra, e nao depois dele');

/* ---------------------------------------------------------------------------
 * 3. O MUNDO SEM PISO: a ausencia e dita.
 * ------------------------------------------------------------------------- */
echo "\n3. O MUNDO SEM PISO: a ausencia e dita, nunca maquiada\n";
$sem = rodametria_casca_bloco_de_compra(
	'À venda agora nesta categoria', array(), 'a causa', 'a causa', array());
vale(false === strpos($sem, '<a '),
	'sem piso no dado o bloco nao serve ancora nenhuma');
vale(false === strpos($sem, 'href'),
	'sem piso no dado o bloco nao serve `href` de especie nenhuma');
vale(false !== strpos($sem, 'sem link para a loja hoje'),
	'sem piso o bloco DIZ que a tela esta sem link de loja (25.2-c, regra 2)',
	substr($sem, 0, 400));
vale(false === strpos($sem, 'Link de afiliado'),
	'sem link de afiliado na tela, a frase da comissao nao sai — frase de comissao '
	. 'sem link e promessa de comissao que nao existe');

/* ---------------------------------------------------------------------------
 * 5. BLOCO COM CARTAO NAO SERVE PISO.
 * ------------------------------------------------------------------------- */
echo "\n5. BLOCO COM CARTAO: o piso do bloco nao entra, porque a escada do cartao ja o serve\n";
$com = rodametria_casca_bloco_de_compra(
	'À venda agora', array(array('nome' => 'MAXSHOT V1')), 'o escopo', 'a causa',
	array('url_busca' => $PISO_PATINETE['url_busca'], 'frase' => $frase));
vale(false === strpos($com, $PISO_PATINETE['url_busca']),
	'com cartao na vitrine o piso do BLOCO nao e servido (20.7: a mesma '
	. 'informacao duas vezes sao as duas que um dia discordam)');
vale(false !== strpos($com, 'rdm-molde-carrossel'),
	'com cartao o bloco segue servindo o carrossel');
vale(false !== strpos($com, 'Link de afiliado'),
	'com cartao a frase da comissao segue saindo');

/* ---------------------------------------------------------------------------
 * 6. AS QUATRO CATEGORIAS DA F1.
 * ------------------------------------------------------------------------- */
echo "\n6. AS QUATRO CATEGORIAS DA F1 TEM DESTINO E FRASE\n";
$mapa = $F1['compra']['piso_por_categoria'];
vale(4 === count($mapa), 'o dado publicado traz as QUATRO categorias',
	'veio ' . count($mapa));
foreach (array('bicicleta_eletrica', 'autopropelido', 'ciclomotor', 'acima_do_ciclomotor') as $cat) {
	$p = rodametria_f1_piso_da_categoria($F1, $cat);
	vale('' !== trim((string) $p['url_busca']),
		"a categoria `$cat` tem destino de loja");
	vale('' !== trim((string) $p['frase']) && false === strpos($p['frase'], '{prateleira}'),
		"a frase da categoria `$cat` esta preenchida, sem molde cru na tela",
		(string) $p['frase']);
	/* A CHAVE DO BANCO E ASCII E NAO PODE IR PARA A TELA: esta ilha escreve
	   dado em ASCII de proposito, e texto de tela acentuado. */
	$chave = (string) $mapa[$cat]['chave'];
	vale(false === strpos((string) $p['frase'], $chave),
		"a frase da categoria `$cat` NAO carrega a chave ASCII `$chave` do banco",
		(string) $p['frase']);
	vale(false !== strpos((string) $p['frase'], (string) $mapa[$cat]['prateleira']),
		"a frase da categoria `$cat` nomeia a prateleira acentuada "
		. "`" . $mapa[$cat]['prateleira'] . "`", (string) $p['frase']);
	/* E O BLOCO SERVE AQUILO: a funcao devolver certo e nao chegar a tela foi
	   exatamente o defeito de 25/11. */
	$html = rodametria_casca_bloco_de_compra('t', array(), 'c', 'c', $p);
	vale(false !== strpos($html, (string) $p['url_busca']),
		"o bloco da categoria `$cat` serve o destino na tela");
}
/* A PROCEDENCIA NAO VAZA: a prateleira do ciclomotor e a da moto, e a do
   autopropelido e a do patinete. Piso de uma nao pode sair na outra. */
$pa = rodametria_f1_piso_da_categoria($F1, 'autopropelido');
$pc = rodametria_f1_piso_da_categoria($F1, 'ciclomotor');
vale($pa['url_busca'] === $PISO_PATINETE['url_busca'],
	'o autopropelido serve o piso do PATINETE, e nao o de outra prateleira');
vale($pc['url_busca'] === $PISO_MOTO['url_busca'],
	'o ciclomotor serve o piso da MOTO, e nao o de outra prateleira');

echo "\n6-b. OS DOIS MUNDOS SEM PISO TEM CAUSAS DIFERENTES\n";
$sem_cat = rodametria_f1_piso_da_categoria($F1, '');
vale('' === trim((string) $sem_cat['url_busca']),
	'sem categoria nao ha destino: escolher uma prateleira por quem nao tem '
	. 'resposta seria escolher o veiculo por ela');
vale($sem_cat['frase'] === $F1['frases_molde']['piso_sem_categoria'],
	'sem categoria a frase e a do molde `piso_sem_categoria`',
	(string) $sem_cat['frase']);
/* O MUNDO FABRICADO: a categoria existe e a prateleira perdeu a busca. Hoje as
   quatro tem piso, e regua que nunca viu o mundo dela nasce errada sem poder
   falhar (secao 8). A coleta de 17/11/2026 apagou o piso de DUAS consultas
   desta ilha: este mundo nao e hipotetico. */
$F1_ORFAO = $F1;
$F1_ORFAO['compra']['piso_por_categoria']['ciclomotor']['url_busca'] = '';
$orfao = rodametria_f1_piso_da_categoria($F1_ORFAO, 'ciclomotor');
vale('' === trim((string) $orfao['url_busca']),
	'categoria sem busca encurtada no dado nao serve destino');
vale($orfao['frase'] === $F1['frases_molde']['piso_sem_prateleira'],
	'categoria sem prateleira recebe a frase DELA, e nao a do mundo sem categoria '
	. '— causa trocada e causa errada na cara de quem le',
	(string) $orfao['frase']);
vale($F1['frases_molde']['piso_sem_prateleira'] !== $F1['frases_molde']['piso_sem_categoria'],
	'as duas frases de ausencia sao DIFERENTES no dado');

echo "\n6-c. O PACOTE DO NAVEGADOR SAI DA MESMA FUNCAO QUE O PHP\n";
$js = rodametria_f1_piso_para_o_js($F1);
vale(4 === count($js), 'o pacote leva as quatro categorias', 'veio ' . count($js));
foreach ($js as $cat => $p) {
	$php = rodametria_f1_piso_da_categoria($F1, (string) $cat);
	vale($p['url'] === (string) $php['url_busca'] && $p['frase'] === (string) $php['frase'],
		"o pacote e o HTML concordam em `$cat` (32.5-d: as duas metades lendo o "
		. "mesmo dado nao podem dizer coisas diferentes)");
}

/* ---------------------------------------------------------------------------
 * 6-d. A F3.
 * ------------------------------------------------------------------------- */
echo "\n6-d. A F3 SERVE O PISO DA PRATELEIRA DELA\n";
$p3 = rodametria_f3_piso_da_busca($F3);
vale($p3['url_busca'] === $PISO_PATINETE['url_busca'],
	'a F3 serve o piso de `patinete eletrico adulto`, que e a prateleira dela',
	(string) $p3['url_busca']);
vale('' !== trim((string) $p3['frase']) && false === strpos($p3['frase'], '{prateleira}'),
	'a frase da F3 esta preenchida, sem molde cru na tela', (string) $p3['frase']);
vale(false === strpos((string) $p3['frase'], (string) $F3['compra']['piso_da_busca']['chave']),
	'a frase da F3 NAO carrega a chave ASCII do banco', (string) $p3['frase']);
$h3 = rodametria_casca_bloco_de_compra('t', array(), 'escopo', 'causa', $p3);
$t3 = tag_do_piso($h3);
vale('' !== $t3 && false !== strpos($t3, 'rel="sponsored noopener"'),
	'o link da F3 sai com `rel="sponsored noopener"` no proprio `<a>`', $t3);
$F3_ORFAO = $F3;
$F3_ORFAO['compra']['piso_da_busca']['url_busca'] = '';
$o3 = rodametria_f3_piso_da_busca($F3_ORFAO);
vale('' === trim((string) $o3['url_busca']),
	'F3 sem busca encurtada no dado nao serve destino');

/* ---------------------------------------------------------------------------
 * 7. O MUNDO DA DISCORDANCIA (20.8).
 * ------------------------------------------------------------------------- */
echo "\n7. A REGUA VELHA E A NOVA, NOS DOIS MUNDOS\n";
$velho_medido = bloco_velho('t', array(), 'c', 'c');
$novo_medido  = rodametria_casca_bloco_de_compra('t', array(), 'c', 'c',
	array('url_busca' => $PISO_PATINETE['url_busca'], 'frase' => $frase));
vale(false === strpos($velho_medido, 'shopee') && false !== strpos($novo_medido, 'shopee'),
	'NO MUNDO MEDIDO as duas DISCORDAM: o bloco velho serve zero link de loja e '
	. 'o novo serve o piso. Esta linha e a medicao do conserto');
$velho_sem = bloco_velho('t', array(), 'c', 'c');
$novo_sem  = rodametria_casca_bloco_de_compra('t', array(), 'c', 'c', array());
vale(false === strpos($velho_sem, 'shopee') && false === strpos($novo_sem, 'shopee'),
	'NO MUNDO SEM PISO as duas CONCORDAM em nao servir link — e so a nova DIZ a '
	. 'ausencia');
vale(false === strpos($velho_sem, 'sem link para a loja hoje')
	&& false !== strpos($novo_sem, 'sem link para a loja hoje'),
	'e e a nova, e so ela, que diz a ausencia em vez de calar');

echo "\n" . ($falhas ? "REPROVADO" : "APROVADO") . ": $afirmacoes afirmacoes, $falhas falha(s)\n";
exit($falhas ? 1 : 0);

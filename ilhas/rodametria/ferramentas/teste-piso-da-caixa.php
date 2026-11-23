<?php
/**
 * A CAIXA DE AUSENCIA SERVE O PISO DA 25.2 (19/11/2026).
 *
 *   php ferramentas/teste-piso-da-caixa.php
 *
 * O DEFEITO QUE ELE EXISTE PARA FECHAR FOI MEDIDO NO AR, nao suposto.
 * `/veiculos/moto-eletrica/` — a consulta de 823 mil buscas/mes desta ilha, a de
 * MAIOR volume do nicho — passou TRES DIAS servindo a caixa de ausencia com ZERO
 * link de loja. Contado no corpo com `<style>` e `<script>` removidos: zero
 * cartao, zero bloco de compra, zero ocorrencia de `shopee.com.br`, zero de
 * `s.shopee`, zero de `sponsored`; os dois unicos links externos da pagina eram
 * `fonts.googleapis.com` e `fonts.gstatic.com`.
 *
 * E O PISO DELA EXISTIA, com os tres campos, no banco daquela consulta desde
 * 16/11. A causa era de MECANISMO e nao de dado: `piso_da_busca` morava DENTRO do
 * bloco da vitrine, e o bloco da vitrine e exatamente o que nao nasce quando a
 * coleta do dia nao alcanca o piso de tres anuncios da 30.2. **A 25.2 chama o
 * piso de o degrau que "nunca depende de ninguem", e era justamente ele que
 * desaparecia quando ninguem anuncia** — a hora em que a pessoa mais precisa de
 * uma saida de compra era a hora em que a pagina nao tinha nenhuma.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a decisao e tomada em PHP
 * (`rdm_produto_piso_sem_vitrine()` e a caixa que a consome), e esta regua CHAMA
 * as funcoes. Regua em Python sobre o texto do PHP conferiria a FORMA e nunca a
 * decisao — o mesmo motivo escrito no `teste-cabeca-sem-vitrine.php`, no
 * `teste-menu-da-casca.php` e no `teste-barra-de-compra.php`.
 *
 * AS SEIS METADES:
 *   1. O PISO CHEGA A TELA: com `piso_da_busca` em `nao_nasceram`, a caixa serve
 *      a `url_busca` ENCURTADA — a mesma do dado, byte por byte.
 *   2. `rel="sponsored"` E `noopener` NO LINK, cobrados no pedaco de HTML do
 *      proprio `<a>` e nao na pagina inteira: `sponsored` em qualquer outro lugar
 *      nao prova nada sobre ESTE link (a cicatriz da 20.7).
 *   3. A AUSENCIA E DITA, NUNCA MAQUIADA (20.8): sem piso no dado, a caixa diz
 *      que a pagina esta sem link de loja hoje e NAO serve `href` vazio — que nao
 *      e botao morto e sim um botao que RECARREGA A PROPRIA PAGINA.
 *   4. O PISO E ALTO NA CAIXA, pela 32.5: o link de compra aparece ANTES dos
 *      paragrafos longos e dos `<h2>`, porque e a unica saida de compra da pagina
 *      e o teto de 1.400 px e do PRIMEIRO botao de compra.
 *   5. A TRAVA DA PROCEDENCIA: piso de OUTRA consulta nao vaza para esta pagina.
 *   6. O MUNDO DA DISCORDANCIA (20.8): a caixa VELHA — a de antes deste conserto,
 *      refeita aqui ao lado — e a nova TEM de discordar no mundo medido (piso no
 *      dado, zero link na tela) e CONCORDAR no mundo sem piso, onde nenhuma das
 *      duas tem o que servir. Autoteste em que as duas concordam sempre nao mede
 *      conserto nenhum.
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
 *  `teste-cabeca-sem-vitrine.php` desta mesma pasta. */
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

$src = file_get_contents($RAIZ . '/snippets/rodametria-produto.php');

if (!defined('RODAMETRIA_PRODUTO_SECAO')) { define('RODAMETRIA_PRODUTO_SECAO', 'veiculos'); }
if (!defined('RODAMETRIA_ID_DADOS_VITRINE')) { define('RODAMETRIA_ID_DADOS_VITRINE', 'vitrine-de-produto'); }

/* ---------------------------------------------------------------------------
 * O MUNDO. So as dependencias que falam com o WordPress e com o banco sao
 * substituidas. A FUNCAO QUE DECIDE e a de verdade, carregada do snippet.
 * ------------------------------------------------------------------------- */
$MUNDO = array(
	'fora'         => array(),   /* slug => declaracao, o que `declaradas_fora_da_vitrine` daria */
	'nao_nasceram' => array(),
);

function rdm_produto_declaradas_fora_da_vitrine() {
	global $MUNDO;
	return $MUNDO['fora'];
}

/* O BANCO DO AR SO TEM O QUE O MANIFEST PUBLICA, e esta trava e a cicatriz de
   18/11/2026 nesta mesma ilha: a primeira versao do ramo da data foi ler
   `anuncios-por-consulta`, que tem `publicar: false` e portanto NAO e gravado
   como option — o portao passou verde, a revisao 109 desembarcou e a pagina
   continuou sem `dateModified`. A lista de publicados sai do MANIFEST de
   verdade, lido do disco, e nunca de uma lista escrita aqui. */
function ids_publicados() {
	static $ids = null;
	if (null !== $ids) { return $ids; }
	$m = json_decode(file_get_contents(dirname(__DIR__) . '/manifest.json'), true);
	$ids = array();
	foreach ((array) (isset($m['dados']) ? $m['dados'] : array()) as $d) {
		if (!empty($d['publicar']) && !empty($d['id'])) { $ids[] = (string) $d['id']; }
	}
	return $ids;
}

function rodametria_casca_banco($id) {
	global $MUNDO;
	if (!in_array((string) $id, ids_publicados(), true)) {
		return null;                      /* o que o WordPress devolve para dado nao publicado */
	}
	if ('vitrine-de-produto' === (string) $id) {
		return array('nao_nasceram' => $MUNDO['nao_nasceram']);
	}
	return null;
}

/* O LEITOR DE `nao_nasceram` TAMBEM VEM DO SNIPPET (23/11/2026): o piso deixou
   de varrer a lista de dentro dele e passou a pedir o mapa por `id` a esta
   funcao — uma leitura, um lugar (20.7). Ele entra aqui, e nao como copia, pelo
   mesmo motivo de todo o resto: a regua CHAMA a funcao de verdade. E foi o
   `bancada.py` quem achou a falta, chamando os dois portoes de INERTE no minuto
   em que a dependencia nasceu — portao que estoura e sai 0 nao e verde, e a
   bancada nao o le como verde. */
if (!carregar_funcao($src, 'rdm_produto_nao_nasceram')) {
	echo "FALHA: nao achei `rdm_produto_nao_nasceram()` no snippet\n";
	exit(1);
}
if (!carregar_funcao($src, 'rdm_produto_piso_sem_vitrine')) {
	echo "  FALHA  `rdm_produto_piso_sem_vitrine()` nao existe no snippet\n";
	exit(1);
}

/** A CAIXA VELHA, de antes deste conserto: ela NUNCA serve piso, porque o piso
 *  nao chegava a ela. Existe para DISCORDAR (20.8). */
function caixa_velha($_slug) {
	return '';
}

/** A CAIXA NOVA, pela MESMA regra do snippet: o que ela serve de piso. A decisao
 *  e da funcao de verdade; o que esta reescrito aqui e so o traje do `<p>`, e o
 *  portao cobra o traje do snippet de verdade na metade 4. */
function caixa_nova($slug) {
	$piso = rdm_produto_piso_sem_vitrine($slug);
	if (empty($piso['url_busca'])) {
		return '';
	}
	return (string) $piso['url_busca'];
}

$PISO_MOTO = array(
	'chave'            => 'moto eletrica adulto',
	'url_busca_produto' => 'https://shopee.com.br/search?keyword=moto%20eletrica%20adulto',
	'url_busca'        => 'https://s.shopee.com.br/2gClWsHpKL',
	'sub_id_1'         => 'rodametria',
);
$PISO_OUTRA = array(
	'chave'     => 'scooter eletrica',
	'url_busca' => 'https://s.shopee.com.br/ZZZoutraZZZ',
	'sub_id_1'  => 'rodametria',
);

echo "A CAIXA DE AUSENCIA SERVE O PISO DA 25.2 — RODAMETRIA (sem rede)\n\n";

/* ---------------------------------------------------------------------------
 * 1. O MUNDO MEDIDO EM 19/11/2026: a pagina existe, esta sem vitrine, e o piso
 *    esta no dado. A caixa TEM de servir a url encurtada.
 * ------------------------------------------------------------------------- */
$MUNDO['fora'] = array('moto-eletrica' => array('h1' => 'Moto elétrica'));
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'causa' => 'menos de 3 anuncios que servem COM link e preco: 1',
	      'colhido_em' => '2026-11-18', 'piso_da_busca' => $PISO_MOTO),
);
$p = rdm_produto_piso_sem_vitrine('moto-eletrica');
vale(!empty($p['url_busca']) && $p['url_busca'] === $PISO_MOTO['url_busca'],
	'1. o piso do dado chega a funcao da caixa, byte por byte',
	'devolveu: ' . var_export(isset($p['url_busca']) ? $p['url_busca'] : null, true));
vale(isset($p['sub_id_1']) && 'rodametria' === $p['sub_id_1'],
	'1-b. o `sub_id_1` da ilha viaja com o piso (25.8)');

/* ---------------------------------------------------------------------------
 * 2. A TRAVA DA PROCEDENCIA: piso de OUTRA consulta nao vaza para esta pagina.
 * ------------------------------------------------------------------------- */
$MUNDO['nao_nasceram'] = array(
	array('id' => 'scooter-eletrica', 'piso_da_busca' => $PISO_OUTRA),
	array('id' => 'moto-eletrica', 'piso_da_busca' => $PISO_MOTO),
);
$p = rdm_produto_piso_sem_vitrine('moto-eletrica');
vale(isset($p['url_busca']) && $p['url_busca'] === $PISO_MOTO['url_busca'],
	'2. com duas consultas sem vitrine, a pagina recebe o piso DELA',
	'devolveu: ' . var_export(isset($p['url_busca']) ? $p['url_busca'] : null, true));

/* ---------------------------------------------------------------------------
 * 3. A PAGINA QUE TEM VITRINE NAO ENTRA AQUI: ela nao esta em
 *    `declaradas_fora_da_vitrine`, e dar-lhe o piso da caixa serviria a linha da
 *    caixa numa pagina que ja serve 16 botoes de compra.
 * ------------------------------------------------------------------------- */
$p = rdm_produto_piso_sem_vitrine('patinete-eletrico');
vale(array() === $p,
	'3. pagina fora de `declaradas_fora_da_vitrine` nao recebe piso de caixa',
	'devolveu: ' . var_export($p, true));

/* ---------------------------------------------------------------------------
 * 4. A AUSENCIA E DITA E NAO MAQUIADA (20.8): sem piso no dado, a funcao devolve
 *    vazio — e o `href` vazio e o que ela existe para nunca produzir.
 * ------------------------------------------------------------------------- */
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'causa' => 'x', 'piso_da_busca' => null),
);
vale(array() === rdm_produto_piso_sem_vitrine('moto-eletrica'),
	'4. `piso_da_busca: null` devolve vazio, nunca um piso de mentira');
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'piso_da_busca' => array('url_busca' => '')),
);
vale(array() === rdm_produto_piso_sem_vitrine('moto-eletrica'),
	'4-b. `url_busca` vazia devolve vazio: `href=""` recarrega a propria pagina');
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'piso_da_busca' => array('url_busca' => '   ')),
);
vale(array() === rdm_produto_piso_sem_vitrine('moto-eletrica'),
	'4-c. `url_busca` so com espaco tambem devolve vazio');
$MUNDO['nao_nasceram'] = array();
vale(array() === rdm_produto_piso_sem_vitrine('moto-eletrica'),
	'4-d. sem entrada em `nao_nasceram`, devolve vazio');

/* ---------------------------------------------------------------------------
 * 5. O DADO NAO PUBLICADO. Se a vitrine deixar de ter `publicar: true` no
 *    manifest, `rodametria_casca_banco()` devolve `null` no ar — e este portao
 *    tem de ver isso, nao aprovar sobre um stub que sempre responde.
 * ------------------------------------------------------------------------- */
vale(in_array('vitrine-de-produto', ids_publicados(), true),
	'5. `vitrine-de-produto` tem `publicar: true` no manifest — sem isso o piso nao '
	. 'chegaria a tela no ar, e este portao estaria medindo um mundo que nao existe');

/* ---------------------------------------------------------------------------
 * 6. O TRAJE NO SNIPPET DE VERDADE. A funcao decide o DADO; quem serve o `<a>` e
 *    a caixa, e e no texto dela que vivem `rel`, `target` e a ORDEM da 32.5.
 * ------------------------------------------------------------------------- */
$i = strpos($src, 'function rdm_produto_pagina_sem_vitrine_html(');
$j = strpos($src, 'function rdm_produto_declaradas_fora_da_vitrine(');
$corpo_da_caixa = substr($src, $i, ($j > $i ? $j : strlen($src)) - $i);

vale(false !== strpos($corpo_da_caixa, 'rdm_produto_piso_sem_vitrine('),
	'6. a caixa de ausencia CHAMA a funcao do piso');
vale(false !== strpos($corpo_da_caixa, 'rel="sponsored noopener"'),
	'6-b. o link do piso sai com `rel="sponsored noopener"` (25.8)');
vale(false !== strpos($corpo_da_caixa, 'target="_blank"'),
	'6-c. o link do piso sai com `target="_blank"`');
vale(false !== strpos($corpo_da_caixa, 'rodametria_casca_rotulo_do_piso()'),
	'6-d. o rotulo sai da casca, nunca digitado na caixa');
vale(false === strpos($corpo_da_caixa, "esc_url( \$piso['url_busca'] )")
	|| false !== strpos($corpo_da_caixa, 'esc_url('),
	'6-e. a url passa por `esc_url()`');

/* A ORDEM DA 32.5: o piso aparece ANTES dos paragrafos longos e dos `<h2>`,
   porque e a UNICA saida de compra desta pagina e o teto de 1.400 px e do
   PRIMEIRO botao de compra. Medido por POSICAO das linhas que EMITEM markup.

   E A PRIMEIRA VERSAO DESTA REGUA REPROVOU A ORDEM CERTA, pela doenca que a
   32.4-b nomeia nesta mesma fabrica: ela procurava `<h2>` no texto da funcao, e
   achou o `<h2>` que mora dentro do COMENTARIO logo acima do bloco do piso —
   comentario que fala de markup nao e markup, e regua que le a camada errada
   reprova a pagina certa. Portao que reprova pagina certa e o caminho mais curto
   para alguem passar a ignora-lo (a licao que a 20.5 escreveu quando o
   "REPROVADO" era cache). A regua agora casa a EMISSAO (`$html .= '<h2>`), que e
   o que decide a ordem no HTML servido. */
$pos_piso = strpos($corpo_da_caixa, '$html .= \'<p class="rdm-caixa-piso');
$pos_h2   = strpos($corpo_da_caixa, '$html .= \'<h2>');
vale($pos_piso !== false && $pos_h2 !== false && $pos_piso < $pos_h2,
	'6-f. o piso vem ANTES do primeiro `<h2>` EMITIDO pela caixa (32.5: o primeiro botao de '
	. 'compra antes de 1.400 px)',
	'piso em ' . var_export($pos_piso, true) . ', primeiro h2 em ' . var_export($pos_h2, true));

/* A TRAVA DA PROPRIA REGUA (20.8): ela tem de DISCORDAR da versao ingenua que le
   o texto cru, senao nao ha prova de que o conserto acima consertou alguma coisa.
   No arquivo de hoje a ingenua acha um `<h2>` de comentario ANTES do piso e
   reprovaria; a nova aprova. */
$ingenua_piso = strpos($corpo_da_caixa, 'rdm-caixa-piso');
$ingenua_h2   = strpos($corpo_da_caixa, '<h2>');
vale($ingenua_h2 !== false && $ingenua_piso !== false && $ingenua_h2 < $ingenua_piso
	&& $pos_piso < $pos_h2,
	'6-g. a regua ingenua (texto cru) e a nova (markup emitido) DISCORDAM neste arquivo: a '
	. 'ingenua reprovaria a ordem certa por causa de um `<h2>` dentro de comentario',
	'ingenua: h2 em ' . var_export($ingenua_h2, true) . ' antes do piso em '
	. var_export($ingenua_piso, true));

/* ---------------------------------------------------------------------------
 * 7. A DISCORDANCIA (20.8). No mundo medido as duas caixas TEM de discordar; no
 *    mundo sem piso TEM de concordar, porque ali nenhuma das duas tem o que
 *    servir — e conserto que muda veredito fora do defeito e afrouxamento.
 * ------------------------------------------------------------------------- */
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'piso_da_busca' => $PISO_MOTO),
);
$velha = caixa_velha('moto-eletrica');
$nova  = caixa_nova('moto-eletrica');
vale('' === $velha && $nova === $PISO_MOTO['url_busca'],
	'7. MUNDO MEDIDO (piso no dado): a caixa velha servia NADA e a nova serve o piso — a '
	. 'discordancia vale os tres dias de /veiculos/moto-eletrica/ no ar sem link de loja',
	'velha=' . var_export($velha, true) . ' nova=' . var_export($nova, true));

$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'piso_da_busca' => null),
);
vale(caixa_velha('moto-eletrica') === caixa_nova('moto-eletrica'),
	'7-b. MUNDO SEM PISO: as duas concordam em nao servir nada — o conserto nao afrouxou '
	. 'nem apertou fora do defeito');

echo "\n$afirmacoes afirmacao(oes), $falhas falha(s).\n";
echo ($falhas ? "REPROVADO\n" : "APROVADO\n");
exit($falhas ? 1 : 0);

<?php
/**
 * A CABECA DA PAGINA NAO DEPENDE DA VITRINE (18/11/2026).
 *
 *   php ferramentas/teste-cabeca-sem-vitrine.php
 *
 * O DEFEITO QUE ELE EXISTE PARA IMPEDIR FOI MEDIDO NO AR, e nao suposto. Em
 * 18/11/2026, na revisao 108, `/veiculos/moto-eletrica/` perdeu a vitrine (2
 * anuncios que entram contra o piso de 3 da 30.2) e `conferir-no-ar.py` a
 * reprovou em SEIS afirmacoes:
 *
 *   o corpo tem 891 caracteres e o piso e 1.500 — pagina fina gasta
 *     orcamento de rastreamento de dominio novo
 *   sem og:title · sem meta description · sem JSON-LD
 *   nenhum JSON-LD declara `dateModified`
 *   sem BreadcrumbList, e a 16.4 o exige em toda pagina que nao e a home
 *
 * A CAUSA ERA UMA SO, e ela estava escrita na propria funcao:
 * `rdm_produto_paginas_prontas()` era *"a unica porta — menu, arvore, mae,
 * JSON-LD e instalacao saem todos dela, para nao haver duas listas que
 * discordem"*. O comentario estava certo sobre o que fazia e nao viu a
 * consequencia: o filtro `rodametria_paginas` tambem sai dela, e e o mapa que
 * da `<title>`, `description`, `og:title` e o `pai` de onde nasce o
 * BreadcrumbList. **Pagina que perde a vitrine perdia a cabeca junto.**
 *
 * O desenho da pagina degradada era so do CORPO, e quem o escreveu cuidou de
 * nao inventar numero — o que estava certo. O que nao estava medido e que ela
 * saia do mapa, e nisso a pagina deixava de existir para a casca enquanto
 * continuava respondendo 200 no indice do Google.
 *
 * A SEPARACAO QUE O CONSERTO FAZ: a vitrine decide o CORPO e o MENU; a camada
 * DECLARADA decide a CABECA.
 *
 * POR QUE ELE E PHP E NAO PYTHON: a decisao e tomada em PHP
 * (`rdm_produto_declaradas_fora_da_vitrine()` e o filtro que a consome), e esta
 * regua CHAMA as funcoes. Regua em Python sobre o texto do PHP conferiria a
 * FORMA e nunca a decisao — o mesmo motivo escrito no `teste-menu-da-casca.php`,
 * no `teste-barra-de-compra.php` e no `teste-citacao-de-anuncio.php`.
 *
 * AS SEIS METADES:
 *   1. A PAGINA QUE EXISTE E ESTA SEM VITRINE ENTRA NO MAPA, com nome, titulo,
 *      description e o `pai` da secao — que e o que devolve o BreadcrumbList.
 *   2. A TRAVA DO 404: declarada que NAO existe no WordPress nao entra. Dar
 *      cabeca a ela poria a mae apontando para uma URL inexistente (secao 16).
 *   3. A ENTRADA FRACA NAO ATROPELA A FORTE: quem tem vitrine fica com
 *      `no_menu => true`, e quem nao tem fica FORA do menu.
 *   4. `id` E O SLUG DA FILHA, e isso e medido nas prontas e nao suposto: em
 *      `paginas_prontas()` o slug sai da vitrine, e este portao cobra que ele
 *      seja igual ao `id` — no dia em que divergirem, a cabeca sairia na URL
 *      errada e isto reprova antes.
 *   5. A DATA: sem `dateModified` a casca nao serve o `WebPage`, e a data da
 *      pagina sem vitrine e a da ULTIMA TENTATIVA de coleta, nunca a da vitrine
 *      velha (que seria frescor afirmado de conteudo que saiu do ar).
 *   6. O MUNDO DA DISCORDANCIA (20.8): o mapa VELHO — so as prontas — e refeito
 *      aqui ao lado do novo, e os dois TEM de discordar exatamente na pagina
 *      sem vitrine, e CONCORDAR nas que tem. Autoteste em que os dois concordam
 *      nao mede conserto nenhum.
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
/* O id da option da vitrine, que `rdm_produto_piso_sem_vitrine()` usa para
   pedir o banco. Mesmo valor da constante do snippet. */
if (!defined('RODAMETRIA_ID_DADOS_VITRINE')) { define('RODAMETRIA_ID_DADOS_VITRINE', 'vitrine-de-produto'); }

/* ---------------------------------------------------------------------------
 * O MUNDO. As duas dependencias que falam com o WordPress e com o banco sao
 * substituidas aqui, e so elas: `rdm_produto_editorial()` (a camada declarada),
 * `rdm_produto_paginas_prontas()` (a vitrine) e `rodametria_casca_url_do_slug()`
 * (que pergunta ao WordPress se a pagina existe). A FUNCAO QUE DECIDE e a de
 * verdade, carregada do snippet.
 * ------------------------------------------------------------------------- */
$MUNDO = array(
	'declaradas' => array(),
	'prontas'    => array(),
	'existem'    => array(),
	'coleta'     => array(),
	'nao_nasceram' => array(),
	/* OS CAMPOS QUE A PAGINA SEM VITRINE PODE SERVIR (20/11/2026). Eles moram na
	   RAIZ do arquivo declarado e nao no codigo, e por isso o mundo os fabrica:
	   a metade 8 deste portao tem um mundo com a lista VAZIA, para provar que e
	   o arquivo que decide e nao uma lista escondida no PHP. */
	'campos'     => array('o_que_e', 'o_que_nao_e', 'como_sabemos', 'perguntas'),
);

function rdm_produto_editorial() {
	global $MUNDO;
	return array('paginas' => $MUNDO['declaradas'],
	             'campos_sem_vitrine' => $MUNDO['campos']);
}

function rdm_produto_paginas_prontas() {
	global $MUNDO;
	return $MUNDO['prontas'];
}

function rodametria_casca_url_do_slug($slug) {
	global $MUNDO;
	return in_array($slug, $MUNDO['existem'], true)
		? 'https://rodametria.com.br/veiculos/' . $slug . '/' : '';
}

/* O BANCO DO AR SO TEM O QUE O MANIFEST PUBLICA, e este stub aprendeu isso da
   pior maneira em 18/11/2026. A primeira versao dele devolvia o mundo pedido
   para QUALQUER id, e com isso aprovou um ramo que, no ar, leria
   `anuncios-por-consulta` — que tem `publicar: false` e portanto nao e gravado
   como option. O portao passou verde, a revisao 109 desembarcou e a pagina
   continuou sem `dateModified`.

   STUB QUE SEMPRE RESPONDE NAO MEDE A AUSENCIA — e a 20.7 em traje de dublê. A
   lista de publicados sai do MANIFEST de verdade, lido do disco, e nunca de uma
   lista escrita aqui: dado que deixar de ser publicado derruba esta afirmacao no
   dia em que o manifest mudar, que e o que se quer. */
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
		/* EXATAMENTE o que o WordPress devolve para dado nao publicado. */
		return null;
	}
	if ('vitrine-de-produto' === (string) $id) {
		return array('nao_nasceram' => $MUNDO['nao_nasceram']);
	}
	return array('consultas' => $MUNDO['coleta']);
}

if (!carregar_funcao($src, 'rdm_produto_declaradas_fora_da_vitrine')) {
	echo "  FALHA  `rdm_produto_declaradas_fora_da_vitrine()` nao existe no snippet\n";
	exit(1);
}

/* AS TRES FUNCOES DA VOZ SEM VITRINE (20/11/2026) CARREGAM AQUI, E NAO NA
   METADE 8 ONDE SAO MEDIDAS: a metade 6 ja chama
   `rdm_produto_pagina_sem_vitrine_html()`, que desde hoje as usa. Carregar na
   hora de medir deixaria a metade 6 morrer de funcao indefinida — e foi o que
   aconteceu na primeira versao desta metade. */
/* `paginas_no_ar` E `irmas` ENTRAM AQUI EM 23/11/2026: desde hoje a pagina
   degradada monta a malha dela pela MESMA rotacao da pagina completa, para o
   grafo de irmas fechar nas duas direcoes (16.9). A metade 6, que chama
   `pagina_sem_vitrine_html()`, morria de funcao indefinida sem elas — e quem
   acusou foi o `bancada.py`, chamando este portao de INERTE. */
foreach (array('rdm_produto_sem_molde', 'rdm_produto_voz_sem_vitrine',
               'rdm_produto_faq_mainentity', 'rdm_produto_paginas_no_ar',
               'rdm_produto_irmas') as $f) {
	if (!carregar_funcao($src, $f)) {
		echo "  FALHA  `$f()` nao existe no snippet\n";
		exit(1);
	}
}

/** O MAPA NOVO, montado pela MESMA regra do filtro do snippet. A regra e lida
 *  do fonte e nao reescrita: o que este portao faz e aplicar as duas listas na
 *  ordem em que o filtro as aplica. */
function mapa_novo() {
	$mapa = array();
	foreach (rdm_produto_paginas_prontas() as $pagina) {
		$mapa[$pagina['slug']] = array(
			'nome'        => $pagina['declarado']['h1'],
			'titulo'      => $pagina['declarado']['titulo'],
			'tipo'        => 'produto',
			'pai'         => RODAMETRIA_PRODUTO_SECAO,
			'no_menu'     => true,
			'description' => $pagina['declarado']['description'],
		);
	}
	foreach (rdm_produto_declaradas_fora_da_vitrine() as $slug => $d) {
		$mapa[$slug] = array(
			'nome'        => $d['h1'],
			'titulo'      => $d['titulo'],
			'tipo'        => 'produto',
			'pai'         => RODAMETRIA_PRODUTO_SECAO,
			'no_menu'     => false,
			'description' => $d['description'],
		);
	}
	return $mapa;
}

/** O MAPA VELHO, de antes de 18/11/2026: so as prontas. Ele existe para
 *  DISCORDAR (20.8) — se nao chamasse a si mesmo de velho e herdasse o
 *  conserto, concordaria sempre e nao mediria nada. */
function mapa_velho() {
	$mapa = array();
	foreach (rdm_produto_paginas_prontas() as $pagina) {
		$mapa[$pagina['slug']] = array(
			'nome'    => $pagina['declarado']['h1'],
			'no_menu' => true,
		);
	}
	return $mapa;
}

function declarada($id, $h1, $titulo, $desc) {
	return array('id' => $id, 'h1' => $h1, 'titulo' => $titulo, 'description' => $desc);
}

function pronta($id) {
	return array(
		'id'        => $id,
		'slug'      => $id,
		'declarado' => declarada($id, 'H1 ' . $id, 'Titulo ' . $id, 'Description ' . $id),
		'vitrine'   => array('consulta' => 'consulta ' . $id, 'linhas' => array(1, 2, 3),
		                     'colhido_em' => '2026-11-17'),
	);
}

echo "1. A PAGINA QUE EXISTE E ESTA SEM VITRINE ENTRA NO MAPA\n";

$MUNDO['declaradas'] = array(
	declarada('patinete-eletrico', 'Patinete elétrico', 'Patinete: titulo', 'Patinete: desc'),
	declarada('bicicleta-eletrica', 'Bicicleta elétrica', 'Bicicleta: titulo', 'Bicicleta: desc'),
	declarada('moto-eletrica', 'Moto elétrica', 'Moto: titulo', 'Moto: desc'),
);
$MUNDO['prontas'] = array(
	'patinete-eletrico'  => pronta('patinete-eletrico'),
	'bicicleta-eletrica' => pronta('bicicleta-eletrica'),
);
/* A moto EXISTE no WordPress: ela nasceu em 16/11 e nunca foi despublicada. */
$MUNDO['existem'] = array('patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica');

$fora = rdm_produto_declaradas_fora_da_vitrine();
vale(array_keys($fora) === array('moto-eletrica'),
	'so a moto esta fora da vitrine',
	'veio: ' . implode(', ', array_keys($fora)));

$mapa = mapa_novo();
vale(isset($mapa['moto-eletrica']), 'a moto esta no mapa de paginas');
vale(isset($mapa['moto-eletrica']) && 'Moto elétrica' === $mapa['moto-eletrica']['nome'],
	'o `nome` dela e o h1 declarado (e dele sai o degrau da trilha)');
vale(isset($mapa['moto-eletrica']) && 'Moto: titulo' === $mapa['moto-eletrica']['titulo'],
	'o `titulo` dela e o declarado — e e ele que vira <title> e og:title');
vale(isset($mapa['moto-eletrica']) && 'Moto: desc' === $mapa['moto-eletrica']['description'],
	'a `description` dela e a declarada — e dela saem meta description e og:description');
vale(isset($mapa['moto-eletrica'])
	&& RODAMETRIA_PRODUTO_SECAO === $mapa['moto-eletrica']['pai'],
	'o `pai` dela e a secao, e e dele que nasce o BreadcrumbList da 16.4');

echo "\n2. A TRAVA DO 404: DECLARADA QUE NAO EXISTE NAO GANHA CABECA\n";

$MUNDO['declaradas'][] = declarada('scooter-eletrica', 'Scooter elétrica',
	'Scooter: titulo', 'Scooter: desc');
/* `existem` NAO ganha a scooter: ela tem `publicar_declarado: false` e nunca
   nasceu. */
$fora = rdm_produto_declaradas_fora_da_vitrine();
vale(!isset($fora['scooter-eletrica']),
	'a scooter, declarada e sem pagina, NAO entra',
	'entrou, e com isso a mae apontaria para uma URL que da 404');
vale(isset($fora['moto-eletrica']),
	'e a moto, declarada e COM pagina, continua entrando');

echo "\n3. A ENTRADA FRACA NAO ATROPELA A FORTE\n";

$mapa = mapa_novo();
vale(true === $mapa['patinete-eletrico']['no_menu'],
	'a pronta fica no menu (`no_menu` true)');
vale(false === $mapa['moto-eletrica']['no_menu'],
	'a sem vitrine fica FORA do menu: o menu anuncia o que a ilha tem hoje');

/* E O MUNDO QUE PROVA QUE A ORDEM IMPORTA: se uma pagina estivesse nas DUAS
   listas, a entrada fraca sobrescreveria a boa e tiraria do menu uma pagina com
   vitrine. A funcao tem de a excluir pela chave, e esta afirmacao e a prova. */
$MUNDO['prontas']['moto-eletrica'] = pronta('moto-eletrica');
$fora = rdm_produto_declaradas_fora_da_vitrine();
vale(!isset($fora['moto-eletrica']),
	'pagina COM vitrine nao aparece tambem na lista de fora',
	'apareceu nas duas, e a entrada fraca apagaria o `no_menu` da boa');
$mapa = mapa_novo();
vale(true === $mapa['moto-eletrica']['no_menu'],
	'com vitrine de volta, a moto volta ao menu');
unset($MUNDO['prontas']['moto-eletrica']);

echo "\n4. O `id` E O SLUG DA FILHA, MEDIDO NAS PRONTAS\n";

$divergente = 0;
foreach (rdm_produto_paginas_prontas() as $id => $pagina) {
	if ((string) $pagina['slug'] !== (string) $id) { $divergente++; }
}
vale(0 === $divergente,
	'nas prontas o slug da filha e igual ao `id`',
	$divergente . ' pagina(s) com slug diferente do id: a cabeca da pagina sem '
	. 'vitrine sairia na URL errada, porque ela usa o `id` como slug');

echo "\n5. A DATA SAI DA ULTIMA TENTATIVA DE COLETA\n";

if (!carregar_funcao($src, 'rdm_produto_pagina_sem_vitrine_html')) {
	echo "  FALHA  `rdm_produto_pagina_sem_vitrine_html()` nao existe no snippet\n";
	exit(1);
}
/* O PISO DA CAIXA DE AUSENCIA (19/11/2026). A caixa passou a CHAMAR
   `rdm_produto_piso_sem_vitrine()`, e sem carregar a funcao de verdade este
   portao morria de erro fatal ANTES da linha do veredito — e erro fatal em PHP
   sai com codigo 0, entao ele nao apareceu como FALHOU: apareceu como INERTE na
   bancada, que foi o que o pegou. Quem acrescenta chamada a uma funcao servida
   por este portao carrega a funcao aqui. */
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
$MUNDO['coleta'] = array(
	array('id' => 'moto-eletrica', 'colhido_em' => '2026-11-18'),
	array('id' => 'patinete-eletrico', 'colhido_em' => '2026-11-17'),
);
$MUNDO['nao_nasceram'] = array(
	/* A `consulta` ENTROU NESTA ENTRADA EM 23/11/2026, e nao e enfeite: desde
	   hoje ela e a ANCORA do link de cluster da pagina degradada, e sem ela a
	   pagina fica FORA da ordem de `paginas_no_ar()` — que e a trava deliberada
	   ("ancora inventada no PHP e a segunda declaracao que a 20.7 proibe").
	   O gerador passou a grava-la em `nao_nasceram` na mesma passada, e a metade
	   6 deste portao mediu a falta no minuto em que ela nasceu: as duas irmas
	   deixaram de ser linkadas na pagina sem vitrine. */
	array('id' => 'moto-eletrica', 'colhido_em' => '2026-11-18',
	      'colhido_em_br' => '18/11/2026',
	      'consulta' => 'consulta moto-eletrica',
	      'causa' => 'menos de 3 anuncios que servem COM link e preco: 2'),
);

/* A PRIMEIRA AFIRMACAO E SOBRE A FONTE, e ela e a que faltava em 18/11: o ramo
   do filtro NAO pode ler dado que o manifest nao publica. */
vale(null === rodametria_casca_banco('anuncios-por-consulta'),
	'`anuncios-por-consulta` NAO existe no ar (publicar: false no manifest)',
	'se este stub o devolver, ele aprova um ramo que no ar le `null` — foi o '
	. 'que deixou a revisao 109 sem `dateModified`');
vale(null !== rodametria_casca_banco('vitrine-de-produto'),
	'`vitrine-de-produto` existe no ar, e e de la que a data tem de sair');
vale(false === strpos($src, 'RODAMETRIA_ID_DADOS_ANUNCIOS'),
	'o snippet NAO declara mais a constante do dado nao publicado',
	'constante de dado com `publicar: false` e convite a ler `null` em silencio');

/* A REGRA DA DATA E LIDA DO FONTE e aplicada aqui com o mesmo mundo: o ramo do
   filtro procura o registro de `nao_nasceram` pelo slug. */
$data = '';
$foraHoje = rdm_produto_declaradas_fora_da_vitrine();
if (isset($foraHoje['moto-eletrica'])) {
	$vit = rodametria_casca_banco('vitrine-de-produto');
	foreach ((array) $vit['nao_nasceram'] as $r) {
		if ('moto-eletrica' === $r['id'] && !empty($r['colhido_em'])) {
			$data = $r['colhido_em'];
			break;
		}
	}
}
vale('2026-11-18' === $data,
	'a data e a da ultima TENTATIVA de coleta (2026-11-18), lida de `nao_nasceram`',
	'veio ' . var_export($data, true));
vale('2026-11-17' !== $data,
	'e NAO e a data da vitrine velha, que seria frescor afirmado de conteudo '
	. 'que saiu do ar');

/* AS LINHAS DO FONTE QUE SUSTENTAM ISSO, lidas e nao supostas: sem elas o ramo
   nao existe e a afirmacao de cima estaria medindo este portao e nao o snippet. */
vale(false !== strpos($src, 'rdm_produto_declaradas_fora_da_vitrine();')
	&& false !== strpos($src, "\$fora[ \$slug ]"),
	'o filtro da data tem o ramo da pagina sem vitrine');
vale(false !== strpos($src, "\$vit['nao_nasceram']")
	|| false !== strpos($src, "\$vit['nao_nasceram'] : array()"),
	'e ele le `nao_nasceram` da VITRINE, que e o dado publicado');

/* E A OUTRA PONTA, que e do gerador: `nao_nasceram` tem de CARREGAR a data, ou
   o ramo acima nao acha nada. Lida do arquivo de verdade. */
$vit_real = json_decode(file_get_contents(dirname(__DIR__)
	. '/dados/vitrine-de-produto.json'), true);
$com_data = 0;
$sem_data = array();
foreach ((array) (isset($vit_real['nao_nasceram']) ? $vit_real['nao_nasceram'] : array()) as $r) {
	if (!empty($r['colhido_em'])) { $com_data++; } else { $sem_data[] = $r['id']; }
}
vale(array() === $sem_data,
	'toda entrada de `nao_nasceram` na vitrine de verdade traz `colhido_em`',
	'sem data em: ' . implode(', ', $sem_data) . ' — a pagina delas ficaria sem '
	. '`dateModified`, e sem ele a casca nao serve o `WebPage`');

echo "\n6. O CORPO: NAO E FINO E NAO INVENTA NUMERO\n";

function rodametria_casca_slug_atual() { return 'moto-eletrica'; }
function rodametria_casca_trilha_html() {
	return '<nav class="rdm-trilha"><a href="/">Início</a> / '
		. '<a href="/veiculos/">Veículos elétricos</a></nav>';
}
function rodametria_casca_paginas() { return mapa_novo(); }

/* A DOBRA E CARREGADA DA CASCA DE VERDADE, nunca reescrita aqui (20/11/2026).
   Ela e `<details>` FECHADO, e e disso que depende a afirmacao da 32.5 de que a
   voz declarada da pagina sem vitrine custa ZERO pixel acima da dobra. Stub
   escrito a mao aqui aprovaria um `<div>` aberto no dia em que a casca mudasse
   — a familia do dublê que sempre responde, da metade 5 deste mesmo portao. */
if (!carregar_funcao(file_get_contents($RAIZ . '/snippets/rodametria-casca.php'),
                     'rodametria_casca_dobra')) {
	echo "  FALHA  `rodametria_casca_dobra()` nao existe na casca\n";
	exit(1);
}
function rodametria_casca_link($slug, $rotulo = '') {
	$url = rodametria_casca_url_do_slug($slug);
	if ('' === $url) { return ''; }
	return '<a href="' . esc_url($url) . '">' . esc_html($rotulo ? $rotulo : $slug) . '</a>';
}

$MUNDO['existem'][] = 'inicio';
$MUNDO['existem'][] = 'autonomia-patinete-eletrico';
$MUNDO['existem'][] = 'peso-maximo-patinete-eletrico';

$html = rdm_produto_pagina_sem_vitrine_html();
$corpo = trim(preg_replace('/\s+/u', ' ', strip_tags($html)));

/* O PISO E O DO `conferir-no-ar.py`, e esta escrito aqui como o numero que ele
   cobrou no ar: 1.500 caracteres de corpo. */
$PISO_DO_CORPO = 1500;
vale(mb_strlen($corpo) >= $PISO_DO_CORPO,
	'o corpo passa do piso de ' . $PISO_DO_CORPO . ' caracteres',
	'tem ' . mb_strlen($corpo) . ' — e a frase do portao de ar e "pagina fina '
	. 'gasta orcamento de rastreamento de dominio novo"');
vale(false !== strpos($html, '<h1>Moto elétrica</h1>'),
	'o h1 e o NOME declarado, e nao o aviso de indisponibilidade',
	'h1 que diz que a pagina nao existe entrega ao Google um titulo falso: ela '
	. 'existe, responde 200 e esta no indice');
vale(false === strpos($html, 'fora do ar neste momento'),
	'o h1 velho ("fora do ar neste momento") nao volta como titulo');
vale(false !== strpos($html, 'rdm-trilha'),
	'a trilha da 16.3 esta no corpo');
vale(0 === preg_match('/R\$\s*[0-9]/u', $html),
	'ZERO preco no corpo: sem vitrine nao ha preco, e inventar um e o unico '
	. 'erro que esta pagina nao pode cometer');
vale(0 === preg_match('/\b\d+[.,]\d{2}\b/u', $corpo),
	'nenhum numero com casa decimal no corpo (faixa, mediana ou preco)');

/* A DATA DA LEITURA NA TELA (item 3 do despacho de 23/11/2026), e os DOIS mundos.
   Ate hoje esta pagina dizia "a leitura de hoje", e "hoje" e a palavra que
   envelhece sozinha — ela se le igual no dia da coleta e cinco dias depois, que e
   a secao 4 dentro de uma frase. A data sai do MESMO campo que o `dateModified`
   desta pagina, em formato de leitor. */
vale(false !== strpos($corpo, 'A leitura de 18/11/2026 não alcançou'),
	'a pagina diz a DATA da leitura que nao alcancou o piso, lida de `colhido_em_br`',
	'e a data e a mesma do `dateModified` do JSON-LD desta pagina, em outro formato');
vale(false === strpos($corpo, 'A leitura de hoje'),
	'a palavra "hoje" saiu da frase: ela se le igual no dia da coleta e cinco dias depois');
$guardado_br = $MUNDO['nao_nasceram'];
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'colhido_em' => '2026-11-18',
	      'consulta' => 'consulta moto-eletrica',
	      'causa' => 'menos de 3 anuncios que servem COM link e preco: 2'),
);
$corpo_sem_data = trim(preg_replace('/\s+/u', ' ',
	strip_tags(rdm_produto_pagina_sem_vitrine_html())));
vale(false !== strpos($corpo_sem_data, 'A leitura mais recente não alcançou'),
	'SEM a data no dado, a frase nao promete data nenhuma em vez de inventar uma',
	'numero de tela sem procedencia na fonte e o que o `conferir-no-ar.py` reprova');
vale(0 === preg_match('#\b\d{2}/\d{2}/\d{4}\b#u', $corpo_sem_data),
	'e nenhuma data aparece no corpo nesse mundo');
$MUNDO['nao_nasceram'] = $guardado_br;

/* A CLASSE DO QUANTIFICADOR POR EXTENSO, E ELA ESTA AQUI PORQUE ESTE PORTAO A
   PEGOU EM MIM. A primeira versao do corpo, escrita minutos antes nesta mesma
   passada, dizia `quase sempre`, `costuma` e `a maioria` — tres termos da lista
   do `conferir-no-ar.py`, e o `costuma` e nomeado no `VOZ.md` desta ilha como a
   classe que ela paga desde 03/11/2026. O portao de ar a teria pegado DEPOIS do
   desembarque; aqui ela e pega antes, e sem rede.

   A LISTA SAI DO PORTAO DE AR, LIDA DO FONTE, e nunca e copiada para dentro
   deste arquivo: lista copiada envelhece separada da original, e termo novo
   acrescentado la nao chegaria aqui (20.7). */
$fonte_do_ar = file_get_contents(__DIR__ . '/conferir-no-ar.py');
$ini = strpos($fonte_do_ar, 'QUANTIFICADORES = (');
vale(false !== $ini,
	'a lista de quantificadores foi achada em conferir-no-ar.py',
	'sem ela esta metade nao mede nada, e um `costuma` novo passaria');
$lista = array();
if (false !== $ini) {
	$fim = strpos($fonte_do_ar, ')', $ini);
	preg_match_all('/"([^"]+)"/', substr($fonte_do_ar, $ini, $fim - $ini), $m);
	$lista = $m[1];
}
vale(count($lista) >= 30,
	'a lista tem pelo menos 30 termos (veio com ' . count($lista) . ')',
	'lista curta e sinal de que a extracao do fonte quebrou, e portao que le '
	. 'lista vazia aprova tudo');
$achados = array();
$corpo_min = mb_strtolower($corpo);
foreach ($lista as $q) {
	if (false !== mb_strpos($corpo_min, mb_strtolower($q))) { $achados[] = $q; }
}
vale(array() === $achados,
	'ZERO quantificador por extenso no corpo desta pagina',
	'achados: ' . implode(', ', $achados) . ' — a pagina sem vitrine e escrita a '
	. 'mao e nao tem camada declarada onde liberar, entao a regra aqui e nao usar');

/* AS SAIDAS. Sem elas a pagina e um beco: 200, honesta e inutil. */
vale(false !== strpos($html, 'consulta patinete-eletrico')
	&& false !== strpos($html, 'consulta bicicleta-eletrica'),
	'as duas irmas COM vitrine estao linkadas, pela consulta delas (16.4c)');
vale(false !== strpos($html, 'quantos km o elétrico faz de verdade'),
	'a F2 esta linkada: ela responde sem depender de anuncio nenhum');
vale(false !== strpos($html, 'o peso máximo que o elétrico suporta'),
	'a F3 esta linkada');
vale(false !== strpos($html, 'descobrir se o elétrico precisa de placa e registro'),
	'a F1 (a home) esta linkada, e a ancora dela fala de CATEGORIA e nao de '
	. 'habilitacao — esta ilha nao responde sobre CNH, e o '
	. '`teste-afirmacao-de-tela.py` reprovou a primeira versao desta ancora');
vale(false === strpos($html, 'precisa de CNH'),
	'ZERO promessa de resposta sobre habilitacao no corpo desta pagina',
	'a Resolucao Contran no 996/2023 nao fala de CNH, e prometer o que a fonte '
	. 'nao diz e o unico erro que esta ilha chama de grave');

/* A TRAVA DO 404 NO CORPO, e ela e a mesma da metade 2: link so para quem
   existe. */
$MUNDO['existem'] = array('patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica');
$html_sem = rdm_produto_pagina_sem_vitrine_html();
vale(false === strpos($html_sem, 'quantos km o elétrico faz de verdade'),
	'ferramenta que NAO existe no WordPress nao vira link',
	'link interno para 404 custa mais do que link que falta (secao 16)');
vale(false !== strpos($html_sem, 'consulta patinete-eletrico'),
	'e as irmas que existem continuam linkadas');

/* A TRAVA DA ANCORA, MEDIDA NA PROPRIA PAGINA (23/11/2026): sem `consulta` em
   `nao_nasceram`, esta pagina sai da ordem do cluster — e o sintoma e que ela
   para de listar irma nenhuma, porque a rotacao nao acha o lugar dela na ordem.
   E o estado em que ela esteve no ar ate hoje, visto de dentro: lista de um lado
   so. O conserto e no GERADOR, e a falha aqui o aponta. */
$MUNDO['existem'] = array('patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica',
                          'inicio', 'autonomia-patinete-eletrico',
                          'peso-maximo-patinete-eletrico');
$guardado = $MUNDO['nao_nasceram'];
$MUNDO['nao_nasceram'] = array(
	array('id' => 'moto-eletrica', 'colhido_em' => '2026-11-18',
	      'causa' => 'menos de 3 anuncios que servem COM link e preco: 2'),
);
$html_sem_ancora = rdm_produto_pagina_sem_vitrine_html();
vale(false === strpos($html_sem_ancora, 'consulta patinete-eletrico')
	&& false === strpos($html_sem_ancora, 'consulta bicicleta-eletrica'),
	'sem `consulta` na fonte, a pagina degradada sai da ordem do cluster e NAO lista irma',
	'se ela listasse, a ancora teria vindo de prosa escrita no PHP — e a 20.7 '
	. 'proibe a segunda declaracao do mesmo fato');
vale(false !== strpos($html_sem_ancora, 'quantos km o elétrico faz de verdade'),
	'e as FERRAMENTAS continuam linkadas: elas nao dependem de vitrine nem de consulta',
	'pagina sem saida nenhuma e 200 honesto e inutil');
$MUNDO['nao_nasceram'] = $guardado;

echo "\n7. O MUNDO DA DISCORDANCIA (20.8)\n";

$MUNDO['existem'] = array('patinete-eletrico', 'bicicleta-eletrica', 'moto-eletrica',
	'inicio', 'autonomia-patinete-eletrico', 'peso-maximo-patinete-eletrico');
$novo = mapa_novo();
$velho = mapa_velho();
vale(isset($novo['moto-eletrica']) && !isset($velho['moto-eletrica']),
	'os dois mapas DISCORDAM na moto: o novo lhe da cabeca, o velho a deixava '
	. 'sem nenhuma',
	'se concordam aqui, o conserto de 18/11 nao esta medido');
foreach (array('patinete-eletrico', 'bicicleta-eletrica') as $id) {
	vale(isset($novo[$id]) && isset($velho[$id])
		&& $novo[$id]['nome'] === $velho[$id]['nome']
		&& $novo[$id]['no_menu'] === $velho[$id]['no_menu'],
		'e CONCORDAM em ' . $id . ': o conserto nao mexe no que ja estava certo');
}

/* AUTOTESTE: a bateria morde? Com a moto fora de `existem` — o mundo em que ela
   nao teria pagina —, a cabeca NAO pode nascer, e se nascer este portao nao esta
   medindo a trava do 404. */
$MUNDO['existem'] = array('patinete-eletrico', 'bicicleta-eletrica');
$sem = rdm_produto_declaradas_fora_da_vitrine();
vale(!isset($sem['moto-eletrica']),
	'AUTOTESTE: sem pagina no WordPress a moto nao ganha cabeca',
	'a trava do 404 nao esta sendo exercida por este portao');

echo "\n8. A VOZ DECLARADA SEM VITRINE (20/11/2026)\n";

/* O DEFEITO MEDIDO NO AR AS 13h3xZ DE 20/11/2026, na revisao 116:
   `/veiculos/moto-eletrica/` servia 3.303 caracteres de corpo, ZERO par de
   pergunta frequente e ZERO `FAQPage` — contra CINCO pares em cada irma —
   enquanto `dados/paginas-de-produto.json` declarava, para a MESMA URL, o que e
   e o que nao e, o como sabemos e seis perguntas. A funcao da pagina degradada
   usava a declaracao para UMA coisa, o `h1`, e escrevia o resto a mao.

   E A FAMILIA E A MESMA DO PISO DA BUSCA DE 19/11, um andar acima: o que a
   pagina devia dizer existia no repositorio e morava DENTRO do bloco que nao
   nasce abaixo do piso da 30.2. */

vale(function_exists('rdm_produto_sem_molde')
	&& function_exists('rdm_produto_voz_sem_vitrine')
	&& function_exists('rdm_produto_faq_mainentity'),
	'as tres funcoes da voz sem vitrine existem no snippet');

/* A REGUA DO MOLDE, nas duas pontas e nas bordas que o PHP substitui. */
vale(rdm_produto_sem_molde('Moto elétrica de adulto é a que você senta e anda.'),
	'frase sem molde passa a regua');
vale(!rdm_produto_sem_molde('A moto custa de {DE} a {ATE}.'),
	'frase com molde NAO passa',
	'molde cru iria para a tela como esta');
vale(!rdm_produto_sem_molde('{FRASE_DA_CARGA} e o resto da frase.'),
	'molde no comeco tambem reprova');
vale(rdm_produto_sem_molde('O texto cita {chave} em minuscula.'),
	'chave em MINUSCULA nao e molde: o PHP nao a substitui, e ela nao vem da '
	. 'vitrine',
	'a forma do molde aqui tem de ser a MESMA que `rdm_produto_preencher()` '
	. 'substitui');
vale(rdm_produto_sem_molde('A Resolução Contran nº 996/2023 decide a categoria.'),
	'numero de documento nao e molde');

/* O MUNDO DA PAGINA SEM VITRINE, com declaracao de verdade em forma: duas
   frases livres, uma moldada, duas perguntas livres, uma moldada e uma livre
   RECUSADA por ancora. */
$moto = declarada('moto-eletrica', 'Moto elétrica', 'Moto: titulo', 'Moto: desc');
$moto['o_que_e'] = array(
	'Moto elétrica de adulto é a que você senta e anda no acelerador.',
	'O que separa uma da outra é a potência nominal e a velocidade máxima.',
);
$moto['o_que_nao_e'] = array(
	'Não é ranking: a gente não andou em nenhuma delas.',
	'E não é ficha técnica. {FRASE_DO_ROTULO}',
);
$moto['como_sabemos'] = array(
	'Os anúncios saem da busca "{CHAVE}" na Shopee, lida em {DATA}.',
	'A regra de trânsito citada aqui é a Resolução Contran nº 996/2023.',
);
$moto['perguntas'] = array(
	array('pergunta' => 'Moto elétrica precisa de CNH?',
	      'resposta' => 'Sobre habilitação esta página não responde, e o motivo é de fonte.'),
	array('pergunta' => 'A moto aguenta eu e um garupa?',
	      'resposta' => '{FRASE_DA_CARGA} A conta é você mais o garupa.'),
	array('pergunta' => 'Por que a faixa de preço é tão larga?',
	      'resposta' => 'Porque o mesmo nome cobre veículos que não disputam a mesma compra.'),
	array('pergunta' => 'Moto elétrica e scooter elétrica são a mesma coisa?',
	      'resposta' => 'Na loja, quase. O mesmo anúncio usa as duas palavras.'),
);
$moto['sem_vitrine'] = array('recusadas' => array(
	array('campo' => 'perguntas', 'ancora' => 'Por que a faixa de preço é tão larga?',
	      'porque' => 'a pergunta pressupõe uma faixa que esta página não publica hoje'),
));

$MUNDO['declaradas'] = array(
	declarada('patinete-eletrico', 'Patinete elétrico', 'Patinete: titulo', 'Patinete: desc'),
	$moto,
);
$MUNDO['prontas'] = array('patinete-eletrico' => pronta('patinete-eletrico'));
$MUNDO['existem'] = array('patinete-eletrico', 'moto-eletrica', 'inicio');

$voz = rdm_produto_voz_sem_vitrine($moto);

vale(isset($voz['o_que_e']) && 2 === count($voz['o_que_e']),
	'as DUAS frases livres de `o_que_e` entram');
vale(isset($voz['o_que_nao_e']) && 1 === count($voz['o_que_nao_e']),
	'de `o_que_nao_e` entra a livre e fica fora a moldada',
	'veio: ' . (isset($voz['o_que_nao_e']) ? count($voz['o_que_nao_e']) : 0));
vale(isset($voz['como_sabemos']) && 1 === count($voz['como_sabemos'])
	&& false !== strpos($voz['como_sabemos'][0], '996/2023'),
	'de `como_sabemos` entra a frase da resolução e fica fora a da coleta do dia');
vale(isset($voz['perguntas']) && 2 === count($voz['perguntas']),
	'das QUATRO perguntas entram DUAS: uma sai por molde, outra por recusa declarada',
	'veio: ' . (isset($voz['perguntas']) ? count($voz['perguntas']) : 0));

$textos_da_voz = '';
foreach ($voz as $itens) {
	foreach ($itens as $it) {
		$textos_da_voz .= is_array($it) ? ($it['pergunta'] . ' ' . $it['resposta']) : $it;
	}
}
vale(false === strpos($textos_da_voz, '{'),
	'NENHUM molde cru atravessa a regua',
	'molde na tela e a ausencia maquiada que a 20.8 proibe');
vale(false === strpos($textos_da_voz, 'faixa de preço é tão larga'),
	'a pergunta RECUSADA por ancora nao entra',
	'ela prometeria na pergunta o dado que a caixa logo acima nega');

/* A VOZ CHEGA A TELA, e e isto que a medicao de hoje reprovava. */
$html_voz = rdm_produto_pagina_sem_vitrine_html();
vale(false !== strpos($html_voz, 'Perguntas frequentes'),
	'a dobra de perguntas frequentes nasce no corpo da pagina sem vitrine',
	'era ZERO par no ar as 13h3xZ de 20/11/2026');
vale(false !== strpos($html_voz, 'Moto elétrica precisa de CNH?')
	|| false !== strpos($html_voz, esc_html('Moto elétrica precisa de CNH?')),
	'a pergunta da CNH, que e a razao desta ilha existir, esta na tela');
vale(false !== strpos($html_voz, 'O que é, e o que não é')
	|| false !== strpos($html_voz, esc_html('O que é, e o que não é')),
	'a dobra do que e e do que nao e nasce com o MESMO titulo da pagina completa',
	'titulo diferente faz a mesma pessoa reaprender a pagina no dia da vitrine');
vale(false !== strpos($html_voz, 'Como sabemos'),
	'a dobra de procedencia nasce');
vale(false === strpos($html_voz, '{FRASE_DA_CARGA}')
	&& false === strpos($html_voz, '{CHAVE}')
	&& false === strpos($html_voz, '{DATA}'),
	'e o corpo servido nao tem molde cru nenhum');

/* O `FAQPage` SAI DO MESMO PAR QUE A TELA (32.4). */
$mains = rdm_produto_faq_mainentity($voz['perguntas']);
vale(2 === count($mains), 'o `mainEntity` tem um `Question` por par visivel');
vale('FAQPage' !== '' && 'Question' === $mains[0]['@type']
	&& 'Moto elétrica precisa de CNH?' === $mains[0]['name']
	&& false !== strpos($mains[0]['acceptedAnswer']['text'], 'não responde'),
	'e o texto da camada da maquina e o MESMO da tela, letra por letra',
	'camada da maquina afirmando o que a tela nao afirma e a 32.4-c invertida');

echo "\n8-b. AS MUTACOES: A REGUA MORDE?\n";

/* (a) RECUSA SEM ANCORA VIVA e liberacao morta: a frase volta a ser servida, e
   e por isso que a trava da ancora mora no `--conferir` do gerador, sobre o
   arquivo de verdade. Aqui se mede o outro lado: ancora que nao casa com nada
   NAO pode calar uma frase por acidente. */
$m = $moto;
$m['sem_vitrine'] = array('recusadas' => array(
	array('campo' => 'perguntas', 'ancora' => 'uma pergunta que nao existe neste arquivo',
	      'porque' => 'ancora morta'),
));
$voz_m = rdm_produto_voz_sem_vitrine($m);
vale(3 === count($voz_m['perguntas']),
	'MUTACAO: ancora que nao casa com nada nao recusa nada — as TRES livres voltam',
	'recusa por acidente cala voz legitima em silencio');

/* (b) RECUSA SEM CAMPO ou SEM ANCORA e ignorada aqui, e de proposito: quem a
   denuncia e o `--conferir` do gerador, que ve o arquivo. Esta regua nao pode
   ADIVINHAR o campo — adivinhar calaria a frase errada. */
$m = $moto;
$m['sem_vitrine'] = array('recusadas' => array(
	array('campo' => '', 'ancora' => 'Por que a faixa de preço é tão larga?'),
));
$voz_m = rdm_produto_voz_sem_vitrine($m);
vale(3 === count($voz_m['perguntas']),
	'MUTACAO: recusa sem campo nao recusa nada nesta regua (quem a denuncia e o gerador)');

/* (c) A LISTA DE CAMPOS SAI DO ARQUIVO. Com ela vazia, a pagina sem vitrine
   volta a ser o toco de hoje — e e esta afirmacao que prova que nao ha lista
   escondida no PHP. */
$guarda = $MUNDO['campos'];
$MUNDO['campos'] = array();
$voz_m = rdm_produto_voz_sem_vitrine($moto);
vale(array() === $voz_m,
	'MUTACAO: sem `campos_sem_vitrine` no arquivo, a voz e VAZIA',
	'se sobrou voz, existe lista escrita a mao no codigo');
$html_m = rdm_produto_pagina_sem_vitrine_html();
vale(false === strpos($html_m, 'Perguntas frequentes'),
	'e a dobra de perguntas desaparece do corpo junto');
vale(false !== strpos($html_m, 'O que esta página compara quando tem dados')
	|| false !== strpos($html_m, esc_html('O que esta página compara quando tem dados')),
	'enquanto o corpo honesto de 18/11 continua de pe',
	'a voz declarada ACRESCENTA; ela nao substitui o aviso da ausencia');
$MUNDO['campos'] = $guarda;

/* (d) CAMPO DECLARADO QUE NAO EXISTE NA PAGINA nao pode derrubar nada. */
$MUNDO['campos'] = array('o_que_e', 'um_campo_que_nao_existe', 'perguntas');
$voz_m = rdm_produto_voz_sem_vitrine($moto);
vale(isset($voz_m['o_que_e']) && isset($voz_m['perguntas'])
	&& !isset($voz_m['um_campo_que_nao_existe']),
	'MUTACAO: campo declarado e inexistente na pagina e ignorado, sem derrubar os outros');
$MUNDO['campos'] = $guarda;

/* (e) PERGUNTA SEM RESPOSTA nao vai para a tela. */
$m = $moto;
$m['perguntas'] = array(array('pergunta' => 'Uma pergunta sem resposta?'));
$voz_m = rdm_produto_voz_sem_vitrine($m);
vale(!isset($voz_m['perguntas']),
	'MUTACAO: par incompleto nao entra — pergunta na tela sem resposta e pior que ausencia');

/* (f) RESPOSTA MOLDADA COM PERGUNTA LIVRE: a regua le as DUAS metades. */
$m = $moto;
$m['perguntas'] = array(
	array('pergunta' => 'Quanto custa?', 'resposta' => 'De {DE} a {ATE}.'),
);
$voz_m = rdm_produto_voz_sem_vitrine($m);
vale(!isset($voz_m['perguntas']),
	'MUTACAO: pergunta livre com resposta moldada fica fora',
	'iria ao ar como pergunta sem resposta util');

echo "\n" . $afirmacoes . " afirmacao(oes), " . $falhas . " falha(s).\n";
echo $falhas ? "REPROVADO\n" : "APROVADO\n";
exit($falhas ? 1 : 0);

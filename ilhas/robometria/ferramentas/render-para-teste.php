<?php
/**
 * Monta uma pagina do site da Robometria fora do WordPress, para poder MEDIR o
 * HTML servido sem depender do site no ar.
 *
 *   php ferramentas/render-para-teste.php . robometria_home > /tmp/home.html
 *
 * Existe porque a nuvem nao alcanca o site desta ilha (o proxy de saida bloqueia
 * e quem aciona o Sync e a Sentinela, no navegador do Raphael). Sem isto, a
 * verificacao da secao 8 do ARQUIPELAGO.md so poderia acontecer depois do
 * desembarque — e "aplicado com sucesso" no log do Sync nao e evidencia de nada.
 *
 * O QUE ELE IMITA DE PROPOSITO, e por que:
 *
 *   1. add_action e wp_head/wp_footer sao DE VERDADE, com prioridade. Se algum
 *      dia um <script> voltar para dentro do retorno de um shortcode, o teste
 *      quebra aqui e nao no navegador do Raphael.
 *   2. O retorno do shortcode passa pelo escape de "&" que os filtros de texto do
 *      conteudo do WordPress aplicam ("&" vira "&#038;"). Foi esse escape que
 *      matou cinco calculadoras da Aquametria em 08/09/2026.
 *   3. remove_action casa gancho, funcao e prioridade, como o WordPress. Sem isso
 *      nao daria para provar que o icone do WordPress saiu do wp_head.
 *
 * O que ele NAO e: um WordPress. Nada aqui grava pagina, e as funcoes de escrita
 * (wp_insert_post e irmas) so existem para o boot da casca nao explodir.
 */
define('ABSPATH', '/tmp/wp/'); define('OBJECT','OBJECT'); define('ARRAY_A','ARRAY_A');
$GLOBALS['__filtros']=array(); $GLOBALS['__shortcodes']=array(); $GLOBALS['__acoes']=array();
$GLOBALS['__conteudo_pagina']='';

/* FILTRO COM PRIORIDADE, como o WordPress.
 *
 * Ate a casca 1.2.0 a prioridade era ACEITA E JOGADA FORA aqui, e os filtros
 * rodavam na ordem em que foram registrados. Nao doia porque so havia um filtro
 * por gancho. A arvore da secao 16 acabou com isso: no the_content a trilha e
 * rede de seguranca na prioridade 9, o escape do conteudo vem no meio e o
 * "Veja tambem" entra na 20 — tres ordens diferentes de acordo com quem foi
 * carregado primeiro, e so uma delas e a do site. Bancada que roda na ordem
 * errada mede uma pagina que o site nunca serve. */
function add_filter($h,$f,$p=10,$a=1){ $GLOBALS['__filtros'][$h][]=array($p,count($GLOBALS['__filtros'][$h]??[]),$f); }
function apply_filters($h,$v){ $extra=array_slice(func_get_args(),2);
	$lista = $GLOBALS['__filtros'][$h] ?? array();
	usort($lista, function($a,$b){ return $a[0]===$b[0] ? $a[1]-$b[1] : $a[0]-$b[0]; });
	foreach($lista as $item){ $v=call_user_func_array($item[2], array_merge(array($v),$extra)); } return $v; }
function add_action($h,$f,$p=10,$a=1){ $GLOBALS['__acoes'][$h][]=array($p,count($GLOBALS['__acoes'][$h]??[]),$f); }
function do_action($h){
	$lista = $GLOBALS['__acoes'][$h] ?? array();
	usort($lista, function($a,$b){ return $a[0]===$b[0] ? $a[1]-$b[1] : $a[0]-$b[0]; });
	foreach ($lista as $item) { call_user_func($item[2]); }
}
function add_shortcode($t,$f){ $GLOBALS['__shortcodes'][$t]=$f; }
function remove_action($h,$f,$p=10){
	if (!isset($GLOBALS['__acoes'][$h])) { return false; }
	foreach ($GLOBALS['__acoes'][$h] as $i=>$item) {
		if ($item[2]===$f && $item[0]===$p) { unset($GLOBALS['__acoes'][$h][$i]); return true; }
	}
	return false;
}
/* O icone que o WordPress imprime sozinho, na mesma prioridade do core. A casca
   tira este daqui; se um dia parar de tirar, ele reaparece no HTML do teste. */
function wp_site_icon(){ echo '<link rel="icon" href="https://robometria.com.br/icone-do-wordpress.png">'."\n"; }
function home_url($p=''){ return 'https://robometria.com.br'.$p; }
function esc_url($u){ return htmlspecialchars($u, ENT_QUOTES); }
function esc_html($t){ return htmlspecialchars($t, ENT_QUOTES); }
function esc_attr($t){ return htmlspecialchars($t, ENT_QUOTES); }
function wp_json_encode($v,$o=0){ return json_encode($v, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES|$o); }
function number_format_i18n($n,$d=0){ return number_format($n,$d,',','.'); }
function sanitize_title($t){ return strtolower(preg_replace('/[^a-z0-9]+/i','-',$t)); }
function wp_kses_post($t){ return $t; }
function is_admin(){ return false; } function did_action($h){ return 0; }
function is_404(){ return false; }
function is_singular($t=''){ return true; }
/* QUAL PAGINA ESTA SENDO SERVIDA.
 *
 * A casca imprime <meta name="description"> e og:* escolhidos pelo slug da
 * pagina atual (v1.2.0), e o caminho real dela e is_front_page() +
 * get_queried_object_id() + o meta _robometria_id. Aqui a bancada IMITA esse
 * caminho a partir de __slug_atual, em vez de a casca ganhar um filtro so para
 * o teste: regua de teste que entra no codigo medido e exatamente a familia de
 * defeito que a secao 8 do contrato descreve.
 *
 * Vazio = nenhuma pagina da ilha, que e o caso em que a casca NAO imprime
 * description nenhuma — e esse caso tambem e medido. */
function is_front_page(){ return isset($GLOBALS['__slug_atual']) && 'inicio' === $GLOBALS['__slug_atual']; }
function get_queried_object_id(){ return (isset($GLOBALS['__slug_atual']) && '' !== $GLOBALS['__slug_atual']) ? 7 : 0; }
function get_post_field($campo,$id=0){ return isset($GLOBALS['__slug_atual']) ? $GLOBALS['__slug_atual'] : ''; }
/* Paginas que "existem" no site de teste: mapa slug => true em __paginas.
   Vazio por padrao, entao quem nao mexe nele ve a casca servir <span> em vez de
   <a> — que e o comportamento certo quando a pagina nao existe. */
function get_posts($a=array()){
	$mapa = isset($GLOBALS['__paginas']) ? $GLOBALS['__paginas'] : array();
	$chave = isset($a['meta_value']) ? $a['meta_value'] : '';
	if ('' !== $chave && isset($mapa[$chave])) { return array((object) array('ID'=>1,'post_name'=>$chave)); }
	return array();
}
function get_permalink($p=null){
	if (is_object($p) && isset($p->post_name)) { return 'https://robometria.com.br/'.$p->post_name.'/'; }
	return 'https://robometria.com.br/pagina-de-teste/';
}
function get_page_by_path($p,$saida=null,$tipo=null){ return null; }
function get_post_meta($id,$chave,$unico=false){
	/* A identidade canonica que o Sync grava em toda pagina da ilha. */
	if ('_robometria_id'===$chave) { return isset($GLOBALS['__slug_atual']) ? $GLOBALS['__slug_atual'] : ''; }
	return '';
}
function update_post_meta($id,$chave,$valor){ return true; }
function wp_insert_post($a,$erro=false){ return 0; }
function wp_update_post($a){ return 0; }
function wp_trash_post($id){ return true; }
function is_wp_error($v){ return false; }
function flush_rewrite_rules($dura=true){}
function wp_safe_redirect($u,$c=302){ return true; }
function current_user_can($c){ return false; }
function nocache_headers(){}
function date_i18n($f){ return date($f); }
function current_time($t){ return date('Y-m-d H:i:s'); }
function get_option($k,$d=false){ return isset($GLOBALS['__options'][$k]) ? $GLOBALS['__options'][$k] : $d; }
function update_option($k,$v,$auto=null){ $GLOBALS['__options'][$k]=$v; return true; }
function trailingslashit($s){ return rtrim($s,'/').'/'; } function untrailingslashit($s){ return rtrim($s,'/'); }
function add_query_arg($a=array()){ return '/'; } function __($t,$d=null){ return $t; }

/**
 * O escape que os filtros de texto do conteudo do WordPress aplicam ao que o
 * shortcode devolve: todo "&" que nao abre uma entidade valida vira "&#038;".
 * Fica aqui para o teste sentir a mesma coisa que o site sente.
 */
function robometria_teste_escapar_conteudo($html) {
	return preg_replace('/&(?!#[0-9]{1,6};|#x[0-9a-fA-F]{1,6};|[a-zA-Z][a-zA-Z0-9]{1,8};)/', '&#038;', $html);
}

add_action('wp_head','wp_site_icon',99);

function robometria_teste_carregar($raiz) {
	foreach (glob($raiz.'/snippets/*.php') as $arquivo) {
		if (basename($arquivo) === 'robometria-sync.php') { continue; } // fala com o WP de verdade
		eval(file_get_contents($arquivo));
	}
	/* Retrato dos ganchos registrados na CARGA dos snippets, para quem monta
	   varias paginas no mesmo processo voltar a este ponto entre uma e outra. */
	$GLOBALS['__acoes_carga'] = $GLOBALS['__acoes'];
}

function robometria_teste_rebobinar() {
	$GLOBALS['__acoes'] = isset($GLOBALS['__acoes_carga']) ? $GLOBALS['__acoes_carga'] : array();
}

/**
 * O QUE O SYNC GRAVOU NAS OPTIONS, gravado aqui tambem.
 *
 * Todo item de `dados` com publicar=true vira a option robometria_dados_<id> no
 * site. Sem isto, cada pagina cai no aviso de "estamos sem o banco no momento" —
 * que e uma pagina VALIDA, com folha, cabecalho e rodape, e por isso a falta
 * passa em silencio. Ficou medido em 11/09/2026: a rolagem horizontal do artigo
 * A2 a 360 px deu zero porque o que estava sendo medido era o aviso de tres
 * linhas.
 *
 * Estava so no caminho de linha de comando deste arquivo; virou funcao quando o
 * teste da casca passou a precisar dela tambem — a home v1.2.0 serve o
 * formulario da R1, e sem banco ela serve o aviso de seletor fora do ar.
 */
/**
 * O slug canonico da pagina que um shortcode desta ilha ocupa.
 *
 * As cinco paginas da casca vem da propria definicao dela; as quatro de
 * ferramenta e artigo vem das constantes de slug dos snippets. Nada aqui e
 * digitado duas vezes, entao renomear um slug num snippet chega na bancada
 * sozinho. So pode ser chamada DEPOIS de robometria_teste_carregar().
 */
function robometria_teste_slug_do_alvo($alvo) {
	$mapa = array(
		'robometria_home'        => 'inicio',
		'robometria_ferramentas' => 'ferramentas',
		'robometria_metodologia' => 'metodologia',
		'robometria_sobre'       => 'sobre',
		'robometria_afiliados'   => 'divulgacao-de-afiliados',
	);
	foreach (array('R1','R2','A1','A2') as $codigo) {
		$constante = 'ROBOMETRIA_' . $codigo . '_SLUG';
		if (defined($constante)) { $mapa['robometria_' . strtolower($codigo)] = constant($constante); }
	}
	return isset($mapa[$alvo]) ? $mapa[$alvo] : '';
}

/**
 * TODAS as paginas publicadas da ilha, no formato do mapa __paginas (slug=>true)
 * que get_posts() consulta para dizer se uma pagina existe.
 *
 * Derivada: as cinco da casca vem da definicao dela, as quatro de ferramenta e
 * artigo das constantes de slug. A home fica de fora de proposito — o endereco
 * dela e home_url('/'), nao /inicio/.
 * So pode ser chamada DEPOIS de robometria_teste_carregar().
 */
function robometria_teste_paginas_do_site() {
	$mapa = array();
	foreach (array_keys(robometria_casca_definicao_paginas()) as $slug) {
		if ('inicio' === $slug) { continue; }
		$mapa[$slug] = true;
	}
	foreach (array('R1','R2','A1','A2') as $codigo) {
		$constante = 'ROBOMETRIA_' . $codigo . '_SLUG';
		if (defined($constante)) { $mapa[constant($constante)] = true; }
	}
	return $mapa;
}

/**
 * O H1 da pagina que o shortcode ocupa — o mesmo texto que o WordPress serve no
 * bloco core/post-title.
 *
 * Sai da MESMA definicao que o Sync grava no post_title: as cinco paginas da
 * casca de robometria_casca_definicao_paginas(), e as quatro de ferramenta e
 * artigo das constantes de titulo dos snippets. Nada digitado duas vezes, entao
 * titulo renomeado num snippet chega na bancada sozinho — e um titulo que a
 * bancada nao conhece sai vazio, que e o caso que o teste cobra.
 */
function robometria_teste_titulo_do_alvo($alvo) {
	$slug = robometria_teste_slug_do_alvo($alvo);
	if ('' === $slug) { return ''; }

	$casca = robometria_casca_definicao_paginas();
	if (isset($casca[$slug]['titulo'])) { return $casca[$slug]['titulo']; }

	foreach (array('R1','R2','A1','A2') as $codigo) {
		$c_slug   = 'ROBOMETRIA_' . $codigo . '_SLUG';
		$c_titulo = 'ROBOMETRIA_' . $codigo . '_TITULO';
		if (defined($c_slug) && defined($c_titulo) && constant($c_slug) === $slug) {
			return constant($c_titulo);
		}
	}
	return '';
}

function robometria_teste_carregar_options($raiz) {
	$manifest = json_decode(file_get_contents($raiz . '/manifest.json'), true);
	foreach ((isset($manifest['dados']) ? $manifest['dados'] : array()) as $item) {
		if (empty($item['publicar'])) { continue; }
		$corpo = @file_get_contents($raiz . '/' . $item['arquivo']);
		if (false === $corpo) { continue; }
		$GLOBALS['__options']['robometria_dados_' . $item['id']] = json_decode($corpo, true);
	}
}

/**
 * Monta a pagina como o tema de blocos monta: wp_head, o cabecalho vindo do
 * filtro render_block, o conteudo JA ESCAPADO pelos filtros, e wp_footer.
 *
 * Uma diferenca que importa: o cabecalho NAO passa pelo escape de "&", porque no
 * tema de blocos ele nao esta dentro do the_content. O conteudo, esse sim, passa.
 */
function robometria_teste_pagina($tag, $titulo = 'Robometria — teste', $slug = null) {
	if (null !== $slug) { $GLOBALS['__slug_atual'] = $slug; }
	$GLOBALS['__conteudo_pagina'] = '[' . $tag . ']';

	/* O retorno CRU do shortcode fica guardado: e sobre ele que o teste afirma
	   que nao ha <script> nem <style>. */
	$GLOBALS['__retorno_shortcode'] = call_user_func($GLOBALS['__shortcodes'][$tag]);

	/* O CAMINHO DO CONTEUDO, NA ORDEM DO SITE (casca 1.3.0).
	 *
	 * No WordPress o que o shortcode devolve atravessa os filtros de the_content:
	 * os de texto escapam o "&" pelo meio, e o que entra DEPOIS deles nao e
	 * escapado. A arvore da secao 16 pendura duas coisas nesse gancho — a rede de
	 * seguranca da trilha na prioridade 9 e o "Veja tambem" na 20 —, entao a
	 * bancada roda o gancho de verdade em vez de so escapar a string. O escape
	 * entra como filtro na prioridade 10, que e onde o WordPress o aplica, e
	 * assim quem chega antes e depois dele sente o que sentiria no ar. */
	if (!isset($GLOBALS['__escape_registrado'])) {
		add_filter('the_content', 'robometria_teste_escapar_conteudo', 10);
		$GLOBALS['__escape_registrado'] = true;
	}

	$marca     = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/site-title'));
	$cabecalho = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/navigation'));

	/* O TITULO DA PAGINA E O H1, e ele vem do bloco core/post-title do tema — que
	 * e exatamente onde a trilha da secao 16.3 se pendura, "abaixo do header".
	 * Ate a casca 1.2.0 a bancada nao montava esse bloco: media uma pagina sem H1
	 * nenhum, e trilha que nasce entre o cabecalho e o H1 seria invisivel para
	 * ela. E a cicatriz do render que serve menos que o site, pela quarta vez
	 * nesta ilha.
	 *
	 * ELE VEM ANTES DO the_content, como no tema de blocos, e a ordem nao e
	 * detalhe: os blocos do template renderizam em ordem de documento, e
	 * post-title vem antes de post-content. Montado depois, a rede de seguranca
	 * da trilha (prioridade 9 do the_content) dispara primeiro e a bancada mede o
	 * caminho reserva achando que mediu o principal. */
	$bloco_titulo = apply_filters('render_block',
		'<h1 class="wp-block-post-title">' . htmlspecialchars(robometria_teste_titulo_do_alvo($tag), ENT_QUOTES) . '</h1>',
		array('blockName'=>'core/post-title'));

	$corpo = apply_filters('the_content', $GLOBALS['__retorno_shortcode']);

	ob_start(); do_action('wp_head');   $cabeca = ob_get_clean();
	ob_start(); do_action('wp_footer'); $rodape = ob_get_clean();

	return "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
		. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>"
		. htmlspecialchars($titulo, ENT_QUOTES) . "</title>\n" . $cabeca . "</head>\n<body>\n"
		. "<header class=\"rbm-cabecalho-teste\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;\">\n"
		. $marca . "\n" . $cabecalho . "\n</header>\n"
		. "<main style=\"padding:1.2rem;\">" . $bloco_titulo . $corpo . "</main>\n"
		. $rodape . "</body>\n</html>\n";
}

if (isset($argv[1]) && basename(__FILE__) === basename($argv[0])) {
	$alvo = isset($argv[2]) ? $argv[2] : 'robometria_home';
	/* O que o Sync gravou nas options (ver robometria_teste_carregar_options). */
	robometria_teste_carregar_options($argv[1]);

	robometria_teste_carregar($argv[1]);

	/* AS PAGINAS QUE EXISTEM NO SITE DE TESTE, DERIVADAS.
	   Num render solto todas as paginas publicadas da ilha existem, para o
	   cabecalho, o rodape e a trilha sairem com os <a href> de verdade. A lista
	   sai dos proprios snippets — digitada aqui, ela envelheceria calada: ate a
	   casca 1.2.0 faltava nela a pagina do artigo A2, entao um render solto dele
	   media a ilha com uma pagina a menos do que ela tem. */
	$GLOBALS['__paginas'] = robometria_teste_paginas_do_site();

	/* ESTAMOS NA PAGINA DA FERRAMENTA QUE ESTA SENDO RENDERIZADA.
	 *
	 * Sem isto o render solto saia PELA METADE, e em silencio: cada snippet de
	 * pagina pergunta "estou na minha pagina?" antes de imprimir no wp_head e no
	 * wp_footer, aqui nao existe is_page(), a resposta era nao, e o HTML vinha
	 * sem a folha da ferramenta, sem o JSON-LD, sem a barra do celular e sem o
	 * script do rodape. O shortcode, esse, era chamado direto e aparecia — entao
	 * a pagina PARECIA inteira.
	 *
	 * Ficou medido em 10/09/2026, no Bloco 4: a medicao de rolagem horizontal da
	 * R2 num Chromium a 360 px deu zero porque a folha que ela mede nao tinha
	 * sido servida. Medir o layout de uma pagina sem o CSS dela e pior do que nao
	 * medir — da um numero verde e a sensacao de ter conferido.
	 *
	 * O nome do filtro sai do proprio alvo (robometria_r2 -> robometria_r2_na_pagina),
	 * entao ferramenta nova nao precisa lembrar de vir aqui.
	 */
	add_filter($alvo . '_na_pagina', function () { return true; });

	echo robometria_teste_pagina($alvo, 'Robometria — teste', robometria_teste_slug_do_alvo($alvo));
}

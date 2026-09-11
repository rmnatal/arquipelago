<?php
/**
 * Monta uma pagina do site do Clube do Mosaico fora do WordPress, para poder
 * MEDIR o HTML servido sem depender do site no ar.
 *
 *   php ferramentas/render-para-teste.php . cdm_home > /tmp/home.html
 *
 * Existe porque a rede do ambiente das rotinas nem sempre alcanca o dominio
 * desta ilha (medido em 11/09/2026: o gateway responde 403 ao CONNECT para
 * clubedomosaico.com.br). Sem isto, a verificacao da secao 8 do ARQUIPELAGO.md
 * so poderia acontecer depois do desembarque — e "aplicado com sucesso" no log
 * do Sync nao e evidencia de nada.
 *
 * O QUE ELE IMITA DE PROPOSITO, e por que:
 *
 *   1. add_action e wp_head/wp_footer sao DE VERDADE, com prioridade. Se algum
 *      dia um <script> voltar para dentro do retorno de um shortcode, o teste
 *      quebra aqui e nao no navegador de alguem.
 *   2. O retorno do shortcode passa pelo escape de "&" que os filtros de texto
 *      do conteudo do WordPress aplicam ("&" vira "&#038;"). Foi esse escape que
 *      matou cinco calculadoras da Aquametria em 08/09/2026.
 *   3. remove_action casa gancho, funcao e prioridade, como o WordPress. Sem
 *      isso nao daria para provar que o icone do WordPress saiu do wp_head.
 *   4. O CABECALHO SAI CLARO, como no site depois da casca 1.2.0, com a linha de
 *      1 px embaixo. A bancada repete a cor do site para que uma medicao de
 *      contraste ou de layout aqui valha alguma coisa.
 *   5. O TITULO DA PAGINA SAI COMO H1, que e o que o tema de blocos faz. Sem
 *      isto, "a home nao exibe o titulo Inicio" seria uma afirmacao que a
 *      bancada nao consegue medir — e foi exatamente essa a reclamacao do
 *      Raphael em 11/09/2026. O H1 vem da definicao de paginas da propria
 *      casca, casada pelo shortcode, nunca de um segundo mapa escrito aqui.
 *
 * A CICATRIZ QUE ESTE ARQUIVO HERDA (secao 8, medida na Robometria em
 * 11/09/2026): render de bancada que serve METADE da pagina da um numero verde
 * e a sensacao de ter conferido. Por isso, alem dos ganchos, ele carrega nas
 * options o que o Sync carrega no site — sem isso uma pagina que le o banco
 * cairia no aviso de "estamos sem o banco", que e uma pagina VALIDA, com
 * cabecalho e rodape, e a medicao mediria o aviso.
 *
 * O que ele NAO e: um WordPress. Nada aqui grava pagina, e as funcoes de
 * escrita (wp_insert_post e irmas) so existem para o boot da casca nao explodir.
 */
define('ABSPATH', '/tmp/wp/'); define('OBJECT','OBJECT'); define('ARRAY_A','ARRAY_A');
$GLOBALS['__filtros']=array(); $GLOBALS['__shortcodes']=array(); $GLOBALS['__acoes']=array();
$GLOBALS['__conteudo_pagina']='';

function add_filter($h,$f,$p=10,$a=1){ $GLOBALS['__filtros'][$h][]=$f; }
function apply_filters($h,$v){ $extra=array_slice(func_get_args(),2);
	foreach(($GLOBALS['__filtros'][$h]??[]) as $f){ $v=call_user_func_array($f, array_merge(array($v),$extra)); } return $v; }
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
function wp_site_icon(){ echo '<link rel="icon" href="https://clubedomosaico.com.br/icone-do-wordpress.png">'."\n"; }
function home_url($p=''){ return 'https://clubedomosaico.com.br'.$p; }
function esc_url($u){ return htmlspecialchars($u, ENT_QUOTES); }
function esc_html($t){ return htmlspecialchars($t, ENT_QUOTES); }
function esc_attr($t){ return htmlspecialchars($t, ENT_QUOTES); }
function wp_json_encode($v,$o=0){ return json_encode($v, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES|$o); }
function number_format_i18n($n,$d=0){ return number_format($n,$d,',','.'); }
function sanitize_title($t){ return strtolower(preg_replace('/[^a-z0-9]+/i','-',$t)); }
function wp_kses_post($t){ return $t; }
function is_admin(){ return false; } function did_action($h){ return 0; }
function get_queried_object_id(){ return isset($GLOBALS['__id_atual']) ? (int) $GLOBALS['__id_atual'] : 0; }
function is_404(){ return false; }
function is_singular($t=''){ return true; }
/* QUAL PAGINA ESTA SENDO SERVIDA. Sem isto a trilha da secao 16 nao teria como
   existir na bancada: ela se monta a partir do caminho da pagina atual, e o
   render montava toda pagina sem dizer qual era. O post_name e o ULTIMO nivel,
   como no WordPress — o caminho inteiro quem remonta e a casca. */
function get_post($p=null){
	$caminho = isset($GLOBALS['__caminho_atual']) ? $GLOBALS['__caminho_atual'] : '';
	if ('' === $caminho) { return null; }
	$partes = explode('/', trim($caminho,'/'));
	return (object) array('ID'=>1,'post_name'=>end($partes),'post_status'=>'publish');
}
function is_front_page(){ return !empty($GLOBALS['__e_home']); }
/* A LOJA NAO TEM CPT ATE O BLOCO 4d. Devolver false aqui e o estado real do
   site hoje, e e o que faz o teste medir o ESTADO VAZIO HONESTO — que e
   justamente a parte da Loja que existe nesta versao. Quem for testar a Loja
   com pecas troca este mapa em __tipos. */
function post_type_exists($tipo){
	$mapa = isset($GLOBALS['__tipos']) ? $GLOBALS['__tipos'] : array();
	return !empty($mapa[$tipo]);
}
/* Paginas que "existem" no site de teste: mapa slug => true em __paginas.
   Vazio por padrao, entao quem nao mexe nele ve a casca servir <span> em vez de
   <a> — que e o comportamento certo quando a pagina nao existe. */
function get_posts($a=array()){
	if (isset($a['post_type']) && 'peca' === $a['post_type']) {
		return isset($GLOBALS['__pecas']) ? $GLOBALS['__pecas'] : array();
	}
	$mapa = isset($GLOBALS['__paginas']) ? $GLOBALS['__paginas'] : array();
	$chave = isset($a['meta_value']) ? $a['meta_value'] : '';
	if ('' !== $chave && isset($mapa[$chave])) { return array((object) array('ID'=>1,'post_name'=>$chave)); }
	return array();
}
function get_permalink($p=null){
	if (is_object($p) && isset($p->post_name)) { return 'https://clubedomosaico.com.br/'.$p->post_name.'/'; }
	return 'https://clubedomosaico.com.br/pagina-de-teste/';
}
/* Paginas que JA EXISTEM no site de teste, como objeto: mapa slug => stdClass em
   __paginas_objeto. Vazio por padrao (site novo). E o que permite medir o
   caminho de ATUALIZACAO de cdm_casca_garantir_paginas(), que e onde mora o
   defeito do titulo que nunca sincroniza — e que o render sozinho nao ve,
   porque ele monta o H1 a partir da definicao e nao do banco do WordPress. */
function get_page_by_path($p,$saida=null,$tipo=null){
	$mapa = isset($GLOBALS['__paginas_objeto']) ? $GLOBALS['__paginas_objeto'] : array();
	return isset($mapa[$p]) ? $mapa[$p] : null;
}
function get_post_meta($id,$chave,$unico=false){
	$mapa = isset($GLOBALS['__meta'][$id]) ? $GLOBALS['__meta'][$id] : array();
	return isset($mapa[$chave]) ? $mapa[$chave] : '';
}
function update_post_meta($id,$chave,$valor){ return true; }
function wp_insert_post($a,$erro=false){ $GLOBALS['__inserts'][] = $a; return count($GLOBALS['__inserts']); }
function wp_update_post($a){ $GLOBALS['__updates'][] = $a; return isset($a['ID']) ? (int) $a['ID'] : 0; }
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
function cdm_teste_escapar_conteudo($html) {
	return preg_replace('/&(?!#[0-9]{1,6};|#x[0-9a-fA-F]{1,6};|[a-zA-Z][a-zA-Z0-9]{1,8};)/', '&#038;', $html);
}

add_action('wp_head','wp_site_icon',99);

function cdm_teste_carregar($raiz) {
	foreach (glob($raiz.'/snippets/*.php') as $arquivo) {
		if (basename($arquivo) === 'clubedomosaico-sync.php') { continue; } // fala com o WP de verdade
		eval(file_get_contents($arquivo));
	}
	/* Retrato dos ganchos registrados na CARGA dos snippets, para quem monta
	   varias paginas no mesmo processo voltar a este ponto entre uma e outra. */
	$GLOBALS['__acoes_carga'] = $GLOBALS['__acoes'];
}

function cdm_teste_rebobinar() {
	$GLOBALS['__acoes'] = isset($GLOBALS['__acoes_carga']) ? $GLOBALS['__acoes_carga'] : array();
}

/**
 * O QUE O SYNC GRAVOU NAS OPTIONS, gravado aqui tambem.
 *
 * Todo item de `dados` com publicar=true vira a option
 * clubedomosaico_dados_<id> no site. Sem isto, uma pagina que le o banco cai no
 * caminho de contingencia e a medicao mede o caminho errado.
 */
function cdm_teste_carregar_options($raiz) {
	$manifest = json_decode(file_get_contents($raiz . '/manifest.json'), true);
	foreach ((isset($manifest['dados']) ? $manifest['dados'] : array()) as $item) {
		if (empty($item['publicar'])) { continue; }
		$corpo = @file_get_contents($raiz . '/' . $item['arquivo']);
		if (false === $corpo) { continue; }
		$GLOBALS['__options']['clubedomosaico_dados_' . $item['id']] = json_decode($corpo, true);
	}
}

/**
 * Monta a pagina como o tema de blocos monta: wp_head, o cabecalho vindo do
 * filtro render_block, o conteudo JA ESCAPADO pelos filtros, e wp_footer.
 *
 * Uma diferenca que importa: o cabecalho NAO passa pelo escape de "&", porque no
 * tema de blocos ele nao esta dentro do the_content. O conteudo, esse sim, passa.
 */
/** O caminho da pagina que o shortcode $tag serve — 'materiais/como-sabemos'. */
function cdm_teste_caminho_da_pagina($tag) {
	if (!function_exists('cdm_casca_definicao_paginas')) { return ''; }
	foreach (cdm_casca_definicao_paginas() as $slug => $def) {
		if (isset($def['conteudo']) && $def['conteudo'] === '[' . $tag . ']') { return $slug; }
	}
	return '';
}

function cdm_teste_titulo_da_pagina($tag) {
	$caminho = cdm_teste_caminho_da_pagina($tag);
	$defs = function_exists('cdm_casca_definicao_paginas') ? cdm_casca_definicao_paginas() : array();
	return isset($defs[$caminho]['titulo']) ? $defs[$caminho]['titulo'] : '';
}

function cdm_teste_pagina($tag, $titulo = 'Clube do Mosaico — teste') {
	$GLOBALS['__conteudo_pagina'] = '[' . $tag . ']';

	/* QUEM E ESTA PAGINA. A casca le isto por get_post()/is_front_page() para
	   montar a trilha; sem declarar, a bancada mediria toda pagina como se fosse
	   uma so — e a trilha, que e por pagina, sairia igual nas nove. */
	$GLOBALS['__caminho_atual'] = cdm_teste_caminho_da_pagina($tag);
	$GLOBALS['__e_home']        = ('inicio' === $GLOBALS['__caminho_atual']);

	/* O retorno CRU do shortcode fica guardado: e sobre ele que o teste afirma
	   que nao ha <script> nem <style>. */
	$GLOBALS['__retorno_shortcode'] = call_user_func($GLOBALS['__shortcodes'][$tag]);
	$corpo_cru = cdm_teste_escapar_conteudo( $GLOBALS['__retorno_shortcode'] );

	$marca     = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/site-title'));
	$cabecalho = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/navigation'));

	/* A ORDEM AQUI E A DO TEMA DE BLOCOS, e ela decide onde a trilha sai.
	   No site o bloco core/post-title renderiza ANTES do bloco de conteudo, e e
	   por isso que a trilha (que entra no filtro daquele bloco) nasce acima do
	   H1. A primeira versao desta bancada rodava the_content primeiro, o cinto
	   de seguranca de prioridade 9 disparava, a trilha ia para dentro do corpo —
	   e a medicao reprovou oito paginas por um defeito que so existia aqui.
	   Render de bancada tem que servir o que o site serve (secao 8). */
	$titulo_da_pagina = cdm_teste_titulo_da_pagina($tag);
	$h1 = '' !== $titulo_da_pagina
		? '<h1 class="wp-block-post-title">' . htmlspecialchars($titulo_da_pagina, ENT_QUOTES) . '</h1>'
		: '';
	$h1 = '' !== $h1
		? apply_filters('render_block', $h1, array('blockName'=>'core/post-title')) . "\n"
		: '';

	/* So depois do post-title: e nele que o "Veja tambem" entra (prioridade 20)
	   e que a trilha de contingencia entraria (prioridade 9) se o bloco de
	   titulo nao existisse na pagina. */
	$corpo = apply_filters('the_content', $corpo_cru);

	ob_start(); do_action('wp_head');   $cabeca = ob_get_clean();
	ob_start(); do_action('wp_footer'); $rodape = ob_get_clean();

	return "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
		. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>"
		. htmlspecialchars($titulo, ENT_QUOTES) . "</title>\n" . $cabeca . "</head>\n<body>\n"
		. "<header class=\"wp-block-template-part\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;border-bottom:1px solid #E9DCD7;\">\n"
		. $marca . "\n" . $cabecalho . "\n</header>\n"
		. "<main style=\"padding:1.2rem;\">" . $h1 . $corpo . "</main>\n"
		. $rodape . "</body>\n</html>\n";
}

/**
 * AS PAGINAS QUE "EXISTEM" no site de teste.
 *
 *   'hoje'  — exatamente as nove que estao no ar em 11/09/2026.
 *   'todas' — as nove MAIS as seis categorias do Guia, para FABRICAR A BORDA que
 *             o mundo ainda nao tem: com tres secoes, nenhuma pagina chega a ter
 *             cinco irmas candidatas, entao trocar o teto de 4 do 16.4(c) por 5
 *             nao mudaria nada do que o site serve e o portao ficaria verde nas
 *             duas versoes. Grade que nao pisa na borda e amostra com nome de
 *             grade (secao 8 do ARQUIPELAGO.md).
 */
function cdm_teste_paginas_no_ar($modo = 'hoje') {
	$hoje = array(
		'loja'=>true,'materiais'=>true,'materiais/como-sabemos'=>true,'como-fazer'=>true,
		'sobre'=>true,'contato'=>true,'divulgacao-de-afiliados'=>true,'privacidade'=>true,
	);
	if ('todas' !== $modo) { return $hoje; }
	foreach (cdm_casca_categorias_do_guia() as $c) {
		if (!empty($c['slug'])) { $hoje[$c['slug']] = true; }
	}
	return $hoje;
}

if (isset($argv[1]) && basename(__FILE__) === basename($argv[0])) {
	$alvo = isset($argv[2]) ? $argv[2] : 'cdm_home';
	$modo = isset($argv[3]) ? $argv[3] : 'hoje';
	cdm_teste_carregar_options($argv[1]);
	cdm_teste_carregar($argv[1]);
	/* Depois de carregar a casca, porque o modo 'todas' le o registro dela. */
	$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar($modo);

	echo cdm_teste_pagina($alvo);
}

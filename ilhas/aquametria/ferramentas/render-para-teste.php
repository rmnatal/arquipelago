<?php
/**
 * Renderiza um shortcode de calculadora numa pagina HTML solta, para testar em
 * navegador de verdade sem subir WordPress nenhum.
 *
 *   php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor > /tmp/c5.html
 *   node ferramentas/teste-navegador-c5.mjs /tmp/c5.html
 *
 * O snippet nao depende de WordPress em tempo de execucao — todo o calculo e
 * JavaScript no navegador —, entao basta um punhado de funcoes falsas do WP
 * para o PHP montar o HTML. A casca entra junto porque as calculadoras pedem a
 * ela as URLs das paginas irmas.
 *
 * ATENCAO — o que este arquivo passou a imitar em 08/09/2026, e por que:
 *
 *   1. add_action e wp_head/wp_footer sao DE VERDADE. Ate 08/09 add_action era
 *      um no-op, o script vinha inline dentro do retorno do shortcode e o teste
 *      passava. No site, esse mesmo script vinha inline e MORRIA.
 *   2. O retorno do shortcode passa pelo escape de "&" que os filtros de texto
 *      do conteudo do WordPress aplicam ("&" vira "&#038;"). E o defeito que
 *      matou as cinco primeiras calculadoras: um "&&" escapado assim para o
 *      JavaScript inteiro com SyntaxError.
 *
 * Ou seja: quem puser <script> ou <style> de volta dentro do retorno do
 * shortcode vai ver o teste quebrar aqui, e nao no navegador do Raphael.
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
/* remove_action DE VERDADE: casa gancho, funcao e prioridade, como o WordPress.
   Sem isso nao da para provar que o icone do WordPress saiu do wp_head. */
function remove_action($h,$f,$p=10){
	if (!isset($GLOBALS['__acoes'][$h])) { return false; }
	foreach ($GLOBALS['__acoes'][$h] as $i=>$item) {
		if ($item[2]===$f && $item[0]===$p) { unset($GLOBALS['__acoes'][$h][$i]); return true; }
	}
	return false;
}
/* O icone que o WordPress imprime sozinho, na mesma prioridade do core. A casca
   tira este daqui; se um dia parar de tirar, ele reaparece no HTML do teste. */
function wp_site_icon(){ echo '<link rel="icon" href="https://aquametria.com.br/icone-do-wordpress.png">'."\n"; }
function home_url($p=''){ return 'https://aquametria.com.br'.$p; }
function esc_url($u){ return htmlspecialchars($u, ENT_QUOTES); }
function esc_html($t){ return htmlspecialchars($t, ENT_QUOTES); }
function esc_attr($t){ return htmlspecialchars($t, ENT_QUOTES); }
function wp_json_encode($v){ return json_encode($v, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES); }
function number_format_i18n($n,$d=0){ return number_format($n,$d,',','.'); }
function sanitize_title($t){ return strtolower(preg_replace('/[^a-z0-9]+/i','-',$t)); }
function wp_kses_post($t){ return $t; }
function wp_strip_all_tags($t){ return strip_tags($t); }
function is_admin(){ return false; } function did_action($h){ return 0; }
function is_singular($t=''){ return true; }
function get_post($p=null){ return (object) array('ID'=>1,'post_content'=>$GLOBALS['__conteudo_pagina'],'post_status'=>'publish','post_name'=>'pagina-de-teste'); }
/* Paginas que 'existem' no site de teste: mapa slug => true em __paginas.
   Vazio por padrao, entao quem nao mexe nele continua vendo o que via. */
function get_posts($a=array()){
	$mapa = isset($GLOBALS['__paginas']) ? $GLOBALS['__paginas'] : array();
	$chave = isset($a['meta_value']) ? $a['meta_value'] : '';
	if ('' !== $chave && isset($mapa[$chave])) { return array((object) array('ID'=>1,'post_name'=>$chave)); }
	return array();
}
function get_permalink($p=null){
	if (is_object($p) && isset($p->post_name)) { return 'https://aquametria.com.br/'.$p->post_name.'/'; }
	return 'https://aquametria.com.br/pagina-de-teste/';
}
function get_post_field($c,$p){ return 'pagina-de-teste'; }
function has_shortcode($conteudo,$tag){ return false !== strpos((string)$conteudo, '['.$tag); }
function get_page_by_path($p,$saida=null,$tipo=null){ return null; }
function date_i18n($f){ return date($f); }
function wp_remote_get($u,$a=array()){ return array('body'=>''); }
function current_time($t){ return date('Y-m-d H:i:s'); }
function get_option($k,$d=false){ return $d; } function update_option($k,$v){ return true; }
function register_rest_route(){} function wp_next_scheduled($h){ return false; } function wp_schedule_event(){}
function trailingslashit($s){ return rtrim($s,'/').'/'; } function untrailingslashit($s){ return rtrim($s,'/'); }
function add_query_arg($a=array()){ return '/'; } function __($t,$d=null){ return $t; }

/**
 * O escape que os filtros de texto do conteudo do WordPress aplicam ao que o
 * shortcode devolve: todo "&" que nao abre uma entidade valida vira "&#038;".
 * E exatamente isto que transforma "a && b" em "a &#038;&#038; b" e mata o
 * JavaScript. Fica aqui para o teste sentir a mesma coisa que o site sente.
 */
function aquametria_teste_escapar_conteudo($html) {
	return preg_replace('/&(?!#[0-9]{1,6};|#x[0-9a-fA-F]{1,6};|[a-zA-Z][a-zA-Z0-9]{1,8};)/', '&#038;', $html);
}

add_action('wp_head','wp_site_icon',99);

function aquametria_teste_carregar($raiz) {
	foreach (glob($raiz.'/snippets/*.php') as $arquivo) {
		if (basename($arquivo) === 'aquametria-sync.php') { continue; }            // fala com o WP de verdade
		if (basename($arquivo) === 'aquametria-atualizador-sync.php') { continue; } // idem
		eval(file_get_contents($arquivo));
	}
	/* Retrato dos ganchos registrados na CARGA dos snippets. Quem testa varias
	   calculadoras no mesmo processo volta a este ponto entre uma e outra: zerar
	   a lista inteira apagaria tambem os wp_head registrados aqui, e o estilo
	   sumiria da cabeca sem que houvesse defeito nenhum. */
	$GLOBALS['__acoes_carga'] = $GLOBALS['__acoes'];
}

function aquametria_teste_rebobinar() {
	$GLOBALS['__acoes'] = isset($GLOBALS['__acoes_carga']) ? $GLOBALS['__acoes_carga'] : array();
}

/**
 * Monta a pagina como o WordPress monta: wp_head, depois o conteudo JA
 * ESCAPADO pelos filtros, depois wp_footer.
 */
function aquametria_teste_pagina($tag, $titulo = 'Aquametria — teste') {
	$GLOBALS['__conteudo_pagina'] = '[' . $tag . ']';

	/* O retorno CRU do shortcode fica guardado: e sobre ele que o teste afirma
	   que nao ha <script> nem <style>. O shortcode so responde uma vez por
	   requisicao (estatico $ja_saiu), entao nao da para chamar duas vezes. */
	$GLOBALS['__retorno_shortcode'] = call_user_func($GLOBALS['__shortcodes'][$tag]);
	$corpo = aquametria_teste_escapar_conteudo( $GLOBALS['__retorno_shortcode'] );

	ob_start(); do_action('wp_head');   $cabeca = ob_get_clean();
	ob_start(); do_action('wp_footer'); $rodape = ob_get_clean();

	return "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n<title>"
		. htmlspecialchars($titulo, ENT_QUOTES) . "</title>\n" . $cabeca . "</head>\n<body>\n"
		. $corpo . "\n" . $rodape . "</body>\n</html>\n";
}

if (isset($argv[1]) && basename(__FILE__) === basename($argv[0])) {
	$alvo = isset($argv[2]) ? $argv[2] : 'aquametria_calculadora_aquecedor';
	aquametria_teste_carregar($argv[1]);
	echo aquametria_teste_pagina($alvo);
}

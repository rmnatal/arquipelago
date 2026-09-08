<?php
/**
 * Renderiza um shortcode de calculadora numa pagina HTML solta, para testar em
 * navegador de verdade sem subir WordPress nenhum.
 *
 * O snippet nao depende de WordPress em tempo de execucao — todo o calculo e
 * JavaScript no navegador —, entao basta um punhado de funcoes falsas do WP
 * para o PHP montar o HTML. E o que este arquivo faz.
 *
 *   php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor > /tmp/c5.html
 *   node ferramentas/teste-navegador-c5.mjs /tmp/c5.html
 *
 * A casca entra junto porque as calculadoras pedem a ela as URLs das paginas
 * irmas (aquametria_casca_url_pagina).
 */
define('ABSPATH', '/tmp/wp/'); define('OBJECT','OBJECT'); define('ARRAY_A','ARRAY_A');
$GLOBALS['__filtros']=array(); $GLOBALS['__shortcodes']=array();
function add_filter($h,$f,$p=10,$a=1){ $GLOBALS['__filtros'][$h][]=$f; }
function apply_filters($h,$v){ foreach(($GLOBALS['__filtros'][$h]??[]) as $f){ $v=call_user_func($f,$v);} return $v; }
function add_action($h,$f,$p=10,$a=1){}
function add_shortcode($t,$f){ $GLOBALS['__shortcodes'][$t]=$f; }
function home_url($p=''){ return 'https://aquametria.com.br'.$p; }
function esc_url($u){ return htmlspecialchars($u, ENT_QUOTES); }
function esc_html($t){ return htmlspecialchars($t, ENT_QUOTES); }
function esc_attr($t){ return htmlspecialchars($t, ENT_QUOTES); }
function wp_json_encode($v){ return json_encode($v, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES); }
function number_format_i18n($n,$d=0){ return number_format($n,$d,',','.'); }
function sanitize_title($t){ return strtolower(preg_replace('/[^a-z0-9]+/i','-',$t)); }
function wp_kses_post($t){ return $t; }
function is_admin(){ return false; } function did_action($h){ return 0; }
function get_page_by_path($p){ return null; }
function wp_remote_get($u,$a=array()){ return array('body'=>''); }
function current_time($t){ return date('Y-m-d H:i:s'); }
function get_option($k,$d=false){ return $d; } function update_option($k,$v){ return true; }
function register_rest_route(){} function wp_next_scheduled($h){ return false; } function wp_schedule_event(){}
function trailingslashit($s){ return rtrim($s,'/').'/'; } function untrailingslashit($s){ return rtrim($s,'/'); }
function add_query_arg($a=array()){ return '/'; } function __($t,$d=null){ return $t; }
$alvo = isset($argv[2]) ? $argv[2] : 'aquametria_calculadora_aquecedor';
foreach (glob($argv[1].'/snippets/*.php') as $arquivo) {
	if (basename($arquivo) === 'aquametria-sync.php') { continue; } // o Sync fala com o WP de verdade
	eval(file_get_contents($arquivo));
}
echo "<!doctype html><html lang=\"pt-BR\"><head><meta charset=\"utf-8\"><title>C5</title></head><body>";
echo call_user_func($GLOBALS['__shortcodes'][$alvo]);
echo "</body></html>";

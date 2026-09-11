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
function get_post_meta($id,$chave,$unico=false){ return ''; }
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
 * Monta a pagina como o tema de blocos monta: wp_head, o cabecalho vindo do
 * filtro render_block, o conteudo JA ESCAPADO pelos filtros, e wp_footer.
 *
 * Uma diferenca que importa: o cabecalho NAO passa pelo escape de "&", porque no
 * tema de blocos ele nao esta dentro do the_content. O conteudo, esse sim, passa.
 */
function robometria_teste_pagina($tag, $titulo = 'Robometria — teste') {
	$GLOBALS['__conteudo_pagina'] = '[' . $tag . ']';

	/* O retorno CRU do shortcode fica guardado: e sobre ele que o teste afirma
	   que nao ha <script> nem <style>. */
	$GLOBALS['__retorno_shortcode'] = call_user_func($GLOBALS['__shortcodes'][$tag]);
	$corpo = robometria_teste_escapar_conteudo( $GLOBALS['__retorno_shortcode'] );

	$marca     = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/site-title'));
	$cabecalho = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/navigation'));

	ob_start(); do_action('wp_head');   $cabeca = ob_get_clean();
	ob_start(); do_action('wp_footer'); $rodape = ob_get_clean();

	return "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
		. "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>"
		. htmlspecialchars($titulo, ENT_QUOTES) . "</title>\n" . $cabeca . "</head>\n<body>\n"
		. "<header class=\"rbm-cabecalho-teste\" style=\"display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem 1.2rem;background:#FFFFFF;\">\n"
		. $marca . "\n" . $cabecalho . "\n</header>\n"
		. "<main style=\"padding:1.2rem;\">" . $corpo . "</main>\n"
		. $rodape . "</body>\n</html>\n";
}

if (isset($argv[1]) && basename(__FILE__) === basename($argv[0])) {
	$alvo = isset($argv[2]) ? $argv[2] : 'robometria_home';
	/* Num render solto as paginas do menu existem, para o cabecalho sair com os
	   <a href> de verdade que o teste do menu precisa conferir. */
	$GLOBALS['__paginas'] = array(
		'ferramentas'=>true,'metodologia'=>true,'sobre'=>true,'divulgacao-de-afiliados'=>true,
		'qual-peca-serve-no-meu-robo-aspirador'=>true,'filtro-universal-de-robo-aspirador'=>true,
		'quantos-pa-o-robo-aspirador-precisa'=>true,
	);
	/* O QUE O SYNC GRAVOU NAS OPTIONS, gravado aqui tambem.
	 *
	 * Todo item de `dados` com publicar=true vira a option
	 * robometria_dados_<id> no site (secao 29 do snippet de Sync). Num render
	 * solto essas options nao existiam, entao cada pagina caia no aviso de
	 * "estamos sem o banco no momento" — e caia em SILENCIO, porque o aviso e
	 * uma pagina valida, com folha, cabecalho e rodape.
	 *
	 * Ficou medido em 11/09/2026, no bloco 5: a medicao de rolagem horizontal do
	 * artigo A2 a 360 px deu zero porque o que estava sendo medido era o aviso,
	 * de tres linhas, e nao o artigo. Junto com o filtro de pagina abaixo, este
	 * carregamento e o que faz o render solto reproduzir o que o site serve — que
	 * e a unica coisa que torna a medicao uma medicao.
	 */
	$manifest = json_decode(file_get_contents($argv[1] . '/manifest.json'), true);
	foreach ((isset($manifest['dados']) ? $manifest['dados'] : array()) as $item) {
		if (empty($item['publicar'])) { continue; }
		$corpo = @file_get_contents($argv[1] . '/' . $item['arquivo']);
		if (false === $corpo) { continue; }
		$GLOBALS['__options']['robometria_dados_' . $item['id']] = json_decode($corpo, true);
	}

	robometria_teste_carregar($argv[1]);

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

	echo robometria_teste_pagina($alvo);
}

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
/* QUAL TIPO ESTA SENDO SERVIDO. Era `return true` para qualquer argumento, e com
   isso `is_singular('peca')` respondia sim em TODA pagina — a ficha da peca sairia
   dentro da home. O tipo da pagina atual mora em __tipo_atual e vale 'page' por
   padrao, que e o que as nove URLs da ilha sao. */
function is_singular($t=''){
	$atual = isset($GLOBALS['__tipo_atual']) ? $GLOBALS['__tipo_atual'] : 'page';
	if ('' === $t) { return true; }
	if (is_array($t)) { return in_array($atual, $t, true); }
	return $atual === $t;
}
/* QUAL PAGINA ESTA SENDO SERVIDA. Sem isto a trilha da secao 16 nao teria como
   existir na bancada: ela se monta a partir do caminho da pagina atual, e o
   render montava toda pagina sem dizer qual era. O post_name e o ULTIMO nivel,
   como no WordPress — o caminho inteiro quem remonta e a casca. */
function get_post($p=null){
	/* Uma peca pedida por id vem do banco de mentira em __pecas_por_id — e o
	   mesmo objeto que o render da ficha usa, para a bancada nao ter duas
	   versoes da mesma peca. */
	if (is_numeric($p) && isset($GLOBALS['__pecas_por_id'][(int) $p])) { return $GLOBALS['__pecas_por_id'][(int) $p]; }
	if (is_object($p)) { return $p; }
	if (null === $p && isset($GLOBALS['__post_atual'])) { return $GLOBALS['__post_atual']; }
	$caminho = isset($GLOBALS['__caminho_atual']) ? $GLOBALS['__caminho_atual'] : '';
	if ('' === $caminho) { return null; }
	$partes = explode('/', trim($caminho,'/'));
	return (object) array('ID'=>1,'post_name'=>end($partes),'post_status'=>'publish','post_type'=>'page','post_title'=>'','post_content'=>'');
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
	if (is_numeric($p) && isset($GLOBALS['__pecas_por_id'][(int) $p])) { $p = $GLOBALS['__pecas_por_id'][(int) $p]; }
	if (is_object($p) && isset($p->post_name)) {
		/* A PECA VIVE EM /loja/<slug>/, dois segmentos, porque o CPT e registrado
		   com `rewrite` slug `loja`. Servir aqui um endereco de um segmento faria
		   a bancada medir uma URL que o site nao publica — a familia de cicatriz
		   "a bancada e o site lendo fontes diferentes para o mesmo campo". */
		if (isset($p->post_type) && 'peca' === $p->post_type) {
			$base = defined('CDM_LOJA_BASE') ? CDM_LOJA_BASE : 'loja';
			return 'https://clubedomosaico.com.br/'.$base.'/'.$p->post_name.'/';
		}
		return 'https://clubedomosaico.com.br/'.$p->post_name.'/';
	}
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
/* GRAVAR DE VERDADE (no array). Devolvia true sem guardar nada, e enquanto
   nenhum snippet lia de volta o que acabara de escrever isso passava. O bloco 4d
   le: a galeria da peca e escrita e relida na mesma requisicao, e um stub que
   esquece faria o teste medir uma peca sem foto nenhuma. */
function update_post_meta($id,$chave,$valor){ $GLOBALS['__meta'][(int) $id][$chave] = $valor; return true; }
function wp_insert_post($a,$erro=false){
	$GLOBALS['__inserts'][] = $a;
	/* Peca inserida passa a EXISTIR para get_post(), senao o caminho de salvar do
	   painel gravaria campos num id que a bancada nao conhece. */
	if (isset($a['post_type']) && 'peca' === $a['post_type']) {
		if (!isset($GLOBALS['__proxima_peca'])) { $GLOBALS['__proxima_peca'] = 500; }
		$id = $GLOBALS['__proxima_peca']++;
		$GLOBALS['__pecas_por_id'][$id] = (object) array(
			'ID'=>$id,'post_type'=>'peca','post_title'=>$a['post_title'] ?? '',
			'post_content'=>$a['post_content'] ?? '','post_status'=>$a['post_status'] ?? 'draft',
			'post_name'=>sanitize_title($a['post_title'] ?? 'peca'),
			'post_author'=>$a['post_author'] ?? 0,'post_date_gmt'=>'2026-09-12 22:00:00',
		);
		return $id;
	}
	return count($GLOBALS['__inserts']);
}
function wp_update_post($a){
	$GLOBALS['__updates'][] = $a;
	$id = isset($a['ID']) ? (int) $a['ID'] : 0;
	if ($id && isset($GLOBALS['__pecas_por_id'][$id])) {
		foreach ($a as $k=>$v) { if ('ID' !== $k) { $GLOBALS['__pecas_por_id'][$id]->$k = $v; } }
	}
	return $id;
}
function wp_trash_post($id){ $GLOBALS['__lixeira'][] = (int) $id; if (isset($GLOBALS['__pecas_por_id'][(int) $id])) { $GLOBALS['__pecas_por_id'][(int) $id]->post_status = 'trash'; } return true; }
/* EXISTE PARA A MUTACAO PODER SER MEDIDA, e nao porque algum snippet o chame.
   A mutacao que troca a lixeira por exclusao definitiva quebrava com Fatal error
   em vez de reprovar — e "nao compila" nao e evidencia de que a trava funciona.
   Guarda em lista PROPRIA: e a distincao entre apagar e poder desfazer, que e a
   unica coisa que essa trava protege. */
function wp_delete_post($id,$forcar=false){ $GLOBALS['__apagados'][] = (int) $id; unset($GLOBALS['__pecas_por_id'][(int) $id]); return true; }
function is_wp_error($v){ return ($v instanceof CdmTesteErro); }
function flush_rewrite_rules($dura=true){ $GLOBALS['__reescritas'] = (isset($GLOBALS['__reescritas']) ? $GLOBALS['__reescritas'] : 0) + 1; }
/* O REDIRECIONAMENTO VIRA EXCECAO, e e o unico jeito de medir as acoes do painel
   nesta bancada: no site elas terminam em `wp_safe_redirect()` seguido de `exit`,
   e `exit` mataria o processo do teste no meio da primeira afirmacao. A excecao
   carrega o destino, que e exatamente o que se quer afirmar — para onde o painel
   mandou a pessoa depois de cada acao. */
function wp_safe_redirect($u,$c=302){ throw new CdmTesteRedirecionou($u); }
/* AS CAPACIDADES SAO AS DA PESSOA LOGADA, e `edit_post` e resolvido pelo AUTOR,
   como o `map_meta_cap` do nucleo faz. Sem isto tudo devolvia false e o painel
   responderia "entre com a sua senha" em toda medicao — a pagina VALIDA que a
   secao 8 avisa que a bancada mede por engano. */
function current_user_can($c){
	$args = array_slice(func_get_args(),1);
	$u = !empty($GLOBALS['__usuaria']) ? $GLOBALS['__usuaria'] : null;
	if (!$u) { return false; }
	if (('edit_post' === $c || 'delete_post' === $c) && isset($args[0])) {
		$post = get_post((int) $args[0]);
		if (!$post) { return false; }
		$cap_base = ('edit_post' === $c) ? 'edit_pecas' : 'delete_pecas';
		$meu = ((int) ($post->post_author ?? 0) === (int) $u->ID);
		if ($meu) { return !empty($u->caps[$cap_base]); }
		return !empty($u->caps[str_replace('_pecas','_others_pecas',$cap_base)]);
	}
	return !empty($u->caps[$c]);
}
function nocache_headers(){}
function date_i18n($f){ return date($f); }
function current_time($t){ return date('Y-m-d H:i:s'); }
function get_option($k,$d=false){ return isset($GLOBALS['__options'][$k]) ? $GLOBALS['__options'][$k] : $d; }
function update_option($k,$v,$auto=null){ $GLOBALS['__options'][$k]=$v; return true; }
function trailingslashit($s){ return rtrim($s,'/').'/'; } function untrailingslashit($s){ return rtrim($s,'/'); }
function add_query_arg($a=array()){ return '/'; } function __($t,$d=null){ return $t; }
/* A F2 e servida pelo SERVIDOR e le a escolha da pessoa em $_GET, entao a
   bancada precisa saber varrer a entrada inteira — 45 combinacoes de base x
   ambiente e 50 de junta x ambiente, cada uma um estado de pagina de verdade.
   Sem isto so daria para medir o caso-ancora, que e o defeito que a Robometria
   pagou em 11/09/2026: "o corpo" de uma ferramenta de entrada variavel e o
   corpo de TODAS as respostas dela, nunca o da pagina sem consulta. */
function sanitize_key($k){ return preg_replace('/[^a-z0-9_\-]/','', strtolower((string) $k)); }
function wp_unslash($v){ return is_string($v) ? stripslashes($v) : $v; }

/* ---------------------------------------------------------------------------
 * O QUE O BLOCO 4d TROUXE: tipo de conteudo, taxonomia, papel, sessao e anexo
 *
 * A Loja e o Atelie sao a primeira coisa desta ilha que depende de coisa que
 * antes nao existia na bancada: um CPT, duas taxonomias, uma pessoa logada com
 * capacidades, e foto. Sem isto a medicao do bloco seria a medicao do estado
 * "nao estou na minha pagina", que e uma pagina VALIDA — a cicatriz que a
 * Robometria pagou em 11/09/2026 e que a secao 8 nomeia.
 *
 * NADA AQUI DECIDE REGRA. Os stubs guardam e devolvem; quem decide se a peca
 * pode ir ao ar, quem e a artesa e o que a ficha imprime e o snippet, e a regua
 * contraria e escrita a mao nos testes. Stub que implementasse a regra faria a
 * bancada aprovar a si mesma.
 * ------------------------------------------------------------------------- */

/* --- tipos e taxonomias: registrar e' anotar em __tipos/__taxonomias --- */
function register_post_type($tipo,$args=array()){
	$GLOBALS['__tipos'][$tipo] = true;
	$GLOBALS['__tipos_args'][$tipo] = $args;
	return (object) array('name'=>$tipo);
}
function register_taxonomy($tax,$tipos=array(),$args=array()){
	$GLOBALS['__taxonomias'][$tax] = $args;
	return true;
}
function taxonomy_exists($tax){ return isset($GLOBALS['__taxonomias'][$tax]); }

/* --- termos. __termos[tax][slug] = (object) term --- */
function term_exists($slug,$tax=''){ return isset($GLOBALS['__termos'][$tax][$slug]) ? array('term_id'=>$GLOBALS['__termos'][$tax][$slug]->term_id) : null; }
function wp_insert_term($nome,$tax,$args=array()){
	$slug = isset($args['slug']) ? $args['slug'] : sanitize_title($nome);
	if (!isset($GLOBALS['__proximo_termo'])) { $GLOBALS['__proximo_termo'] = 100; }
	$id = $GLOBALS['__proximo_termo']++;
	$GLOBALS['__termos'][$tax][$slug] = (object) array('term_id'=>$id,'slug'=>$slug,'name'=>$nome,'taxonomy'=>$tax);
	return array('term_id'=>$id);
}
function get_term_by($campo,$valor,$tax=''){
	if ('slug' === $campo) { return isset($GLOBALS['__termos'][$tax][$valor]) ? $GLOBALS['__termos'][$tax][$valor] : false; }
	foreach (($GLOBALS['__termos'][$tax] ?? array()) as $t) { if ((int) $t->term_id === (int) $valor) { return $t; } }
	return false;
}
/* __objeto_termos[post_id][tax] = array de slug */
function wp_get_object_terms($id,$tax,$args=array()){
	$taxs = is_array($tax) ? $tax : array($tax);
	$saida = array();
	foreach ($taxs as $t) {
		foreach (($GLOBALS['__objeto_termos'][(int) $id][$t] ?? array()) as $slug) {
			if (isset($GLOBALS['__termos'][$t][$slug])) { $saida[] = $GLOBALS['__termos'][$t][$slug]; }
		}
	}
	return $saida;
}
function wp_set_object_terms($id,$termos,$tax,$juntar=false){
	$slugs = array();
	foreach ((array) $termos as $t) {
		foreach (($GLOBALS['__termos'][$tax] ?? array()) as $slug=>$obj) { if ((int) $obj->term_id === (int) $t) { $slugs[] = $slug; } }
	}
	$GLOBALS['__objeto_termos'][(int) $id][$tax] = $slugs;
	return $slugs;
}

/* --- papeis e capacidades. __papeis[nome] = (object){capabilities, add_cap} --- */
class CdmTestePapel {
	public $name; public $capabilities = array();
	public function __construct($n,$c=array()){ $this->name=$n; $this->capabilities=$c; }
	public function add_cap($c,$tem=true){ $this->capabilities[$c]=$tem; }
}
function add_role($nome,$rotulo,$caps=array()){
	if (isset($GLOBALS['__papeis'][$nome])) { return null; }
	$GLOBALS['__papeis'][$nome] = new CdmTestePapel($nome,$caps);
	return $GLOBALS['__papeis'][$nome];
}
function get_role($nome){
	/* O `administrator` EXISTE em todo WordPress, e a bancada nao o tinha: sem ele,
	   o trecho do snippet que da ao administrador as capacidades de `peca` caia num
	   `if` falso e nunca era medido. Caminho nao medido e caminho que pode estar
	   quebrado — e este em particular decide se o Raphael consegue socorrer a mae no
	   domingo sem uma conversa sobre SQL. So as capacidades que importam para a
	   medicao, e nenhuma de `peca`, porque quem deve acrescenta-las e o snippet. */
	if ('administrator' === $nome && !isset($GLOBALS['__papeis']['administrator'])) {
		$GLOBALS['__papeis']['administrator'] = new CdmTestePapel('administrator', array(
			'manage_options'=>true,'edit_posts'=>true,'edit_pages'=>true,
			'upload_files'=>true,'read'=>true,'edit_theme_options'=>true,'list_users'=>true,
		));
	}
	return isset($GLOBALS['__papeis'][$nome]) ? $GLOBALS['__papeis'][$nome] : null;
}

/* --- a pessoa logada. __usuaria = null ou (object) --- */
function is_user_logged_in(){ return !empty($GLOBALS['__usuaria']); }
function wp_get_current_user(){
	return !empty($GLOBALS['__usuaria']) ? $GLOBALS['__usuaria'] : (object) array('ID'=>0,'roles'=>array());
}
function get_current_user_id(){ return !empty($GLOBALS['__usuaria']) ? (int) $GLOBALS['__usuaria']->ID : 0; }
function get_user_by($campo,$valor){
	foreach (($GLOBALS['__usuarias'] ?? array()) as $u) {
		if ('login' === $campo && $u->user_login === $valor) { return $u; }
		if ('email' === $campo && $u->user_email === $valor) { return $u; }
		if ('id' === $campo && (int) $u->ID === (int) $valor) { return $u; }
	}
	return false;
}
function user_can($u,$cap){
	if (is_numeric($u)) { $u = get_user_by('id',$u); }
	if (!is_object($u)) { return false; }
	return !empty($u->caps[$cap]);
}
function wp_insert_user($a){
	if (!isset($GLOBALS['__proxima_usuaria'])) { $GLOBALS['__proxima_usuaria'] = 10; }
	$id = $GLOBALS['__proxima_usuaria']++;
	$papel = isset($a['role']) ? $a['role'] : '';
	$caps  = ($papel && isset($GLOBALS['__papeis'][$papel])) ? $GLOBALS['__papeis'][$papel]->capabilities : array();
	$u = new CdmTesteUsuaria(array(
		'ID'=>$id,'user_login'=>$a['user_login'] ?? '','user_email'=>$a['user_email'] ?? '',
		'display_name'=>$a['display_name'] ?? '','first_name'=>$a['first_name'] ?? '',
		'roles'=>$papel ? array($papel) : array(),'caps'=>$caps,
	));
	$GLOBALS['__usuarias'][$id] = $u;
	return $id;
}
function wp_generate_password($n=12,$especial=true,$extra=false){ return str_repeat('x',(int) $n); }

/* --- senha, sessao e e-mail. Nada aqui e criptografia: e registro do que foi
       pedido, para o teste poder afirmar sobre o que o snippet TENTOU fazer. --- */
function get_password_reset_key($u){
	$GLOBALS['__chaves_pedidas'][] = is_object($u) ? $u->user_login : '';
	return isset($GLOBALS['__chave_falha']) && $GLOBALS['__chave_falha'] ? new CdmTesteErro('sem chave') : 'CHAVE-DE-TESTE';
}
function check_password_reset_key($chave,$login){
	if (!empty($GLOBALS['__chave_invalida']) || 'CHAVE-DE-TESTE' !== $chave) { return new CdmTesteErro('chave inválida'); }
	$u = get_user_by('login',$login);
	return $u ? $u : new CdmTesteErro('sem usuária');
}
function reset_password($u,$nova){ $GLOBALS['__senhas_trocadas'][] = is_object($u) ? $u->user_login : ''; return true; }
function wp_signon($c=array(),$ssl=false){
	$GLOBALS['__signon'][] = $c;
	$u = get_user_by('login', $c['user_login'] ?? '');
	return $u ? $u : new CdmTesteErro('login inválido');
}
function wp_logout(){ $GLOBALS['__usuaria'] = null; $GLOBALS['__logout'] = true; }
function is_ssl(){ return true; }
function wp_mail($para,$assunto,$corpo,$cab=array()){
	$GLOBALS['__emails'][] = array('para'=>$para,'assunto'=>$assunto,'corpo'=>$corpo,'cabecalho'=>$cab);
	return empty($GLOBALS['__email_falha']);
}
function remove_filter($h,$f,$p=10){
	if (!isset($GLOBALS['__filtros'][$h])) { return false; }
	foreach ($GLOBALS['__filtros'][$h] as $i=>$g) { if ($g===$f) { unset($GLOBALS['__filtros'][$h][$i]); return true; } }
	return false;
}
function sanitize_email($e){ return filter_var((string) $e, FILTER_VALIDATE_EMAIL) ? (string) $e : ''; }
function sanitize_text_field($t){ return trim(preg_replace('/[\r\n\t]+/',' ', strip_tags((string) $t))); }
function wpautop($t){ return '<p>'.implode('</p><p>', preg_split('/\n\s*\n/', trim((string) $t))).'</p>'; }
function wp_create_nonce($a=-1){ return 'NONCE-'.md5((string) $a); }
function wp_verify_nonce($n,$a=-1){ return ('NONCE-'.md5((string) $a) === $n) ? 1 : false; }
function wp_nonce_field($a=-1,$nome='_wpnonce',$referer=true,$eco=true){
	$html = '<input type="hidden" name="'.esc_attr($nome).'" value="'.esc_attr(wp_create_nonce($a)).'">';
	if ($eco) { echo $html; return; }
	return $html;
}
function register_rest_route($ns,$rota,$args=array()){ $GLOBALS['__rotas'][$ns.$rota] = $args; return true; }

/* --- anexos. __anexos[id] = array(url, largura, altura) --- */
function wp_attachment_is_image($id){ return isset($GLOBALS['__anexos'][(int) $id]); }
function wp_get_attachment_image_src($id,$tam='thumbnail'){
	if (!isset($GLOBALS['__anexos'][(int) $id])) { return false; }
	$a = $GLOBALS['__anexos'][(int) $id];
	return array($a['url'], $a['largura'], $a['altura'], false);
}
function wp_get_attachment_url($id){ return isset($GLOBALS['__anexos'][(int) $id]) ? $GLOBALS['__anexos'][(int) $id]['url'] : ''; }
function set_post_thumbnail($id,$anexo){ $GLOBALS['__capa'][(int) $id] = (int) $anexo; return true; }
function delete_post_thumbnail($id){ unset($GLOBALS['__capa'][(int) $id]); return true; }
function wp_delete_attachment($id,$forcar=false){ unset($GLOBALS['__anexos'][(int) $id]); return true; }
function delete_post_meta($id,$chave,$valor=''){ unset($GLOBALS['__meta'][(int) $id][$chave]); return true; }

class CdmTesteErro {
	private $msg;
	public function __construct($m){ $this->msg = $m; }
	public function get_error_message(){ return $this->msg; }
}

class CdmTesteRedirecionou extends Exception {
	public $destino;
	public function __construct($d){ $this->destino = $d; parent::__construct('redirecionou para '.$d); }
}

/**
 * A usuaria da bancada. E uma CLASSE e nao um stdClass porque o snippet do Atelie
 * chama `$u->set_role()` quando acha alguem com o papel errado — e esse caminho
 * (usuaria que existe com outro papel) e justamente um dos que precisa ser medido.
 */
class CdmTesteUsuaria {
	public $ID = 0, $user_login = '', $user_email = '', $display_name = '', $first_name = '';
	public $roles = array(), $caps = array();
	public function __construct($a = array()){
		foreach ($a as $k=>$v) { $this->$k = $v; }
	}
	public function set_role($papel){
		$this->roles = array($papel);
		$this->caps  = isset($GLOBALS['__papeis'][$papel]) ? $GLOBALS['__papeis'][$papel]->capabilities : array();
		$GLOBALS['__papeis_trocados'][] = $this->user_login.' => '.$papel;
	}
}

/**
 * Poe uma pessoa logada na bancada, com as capacidades do papel pedido.
 *
 * O papel tem de ter sido criado pelo snippet antes (do_action('init')), e isso e
 * de proposito: se o snippet parar de criar o papel, esta funcao devolve alguem
 * SEM capacidade nenhuma e o teste reprova — em vez de a bancada inventar as
 * capacidades que ela queria medir.
 */
function cdm_teste_logar($papel = 'artesa', $id = 10, $login = 'artesa'){
	$caps = isset($GLOBALS['__papeis'][$papel]) ? $GLOBALS['__papeis'][$papel]->capabilities : array();
	$u = new CdmTesteUsuaria(array(
		'ID'=>$id,'user_login'=>$login,'user_email'=>'mina196@hotmail.com',
		'display_name'=>'Artesã','first_name'=>'Mina',
		'roles'=>array($papel),'caps'=>$caps,
	));
	$GLOBALS['__usuaria'] = $u;
	$GLOBALS['__usuarias'][$id] = $u;
	return $u;
}

function cdm_teste_deslogar(){ $GLOBALS['__usuaria'] = null; }

/**
 * O escape que os filtros de texto do conteudo do WordPress aplicam ao que o
 * shortcode devolve: todo "&" que nao abre uma entidade valida vira "&#038;".
 * Fica aqui para o teste sentir a mesma coisa que o site sente.
 */
function cdm_teste_escapar_conteudo($html) {
	return preg_replace('/&(?!#[0-9]{1,6};|#x[0-9a-fA-F]{1,6};|[a-zA-Z][a-zA-Z0-9]{1,8};)/', '&#038;', $html);
}

add_action('wp_head','wp_site_icon',99);

/* O CANONICAL DO NUCLEO, que o site serve e a bancada nao servia.
 *
 * `rel_canonical()` esta ligado por padrao no WordPress e esta ilha nao tem
 * plugin de SEO que o remova, entao toda pagina singular do site ja sai com um
 * canonical apontando para o permalink limpo. Sem isto aqui, um snippet que
 * imprimisse o SEU proprio canonical passaria no teste e serviria DOIS no ar —
 * e a bancada nao teria como ver. E a mesma familia da cicatriz da Aquametria
 * de 11/09/2026: a bancada e o site lendo fontes diferentes para o mesmo campo.
 */
function rel_canonical(){
	$caminho = isset($GLOBALS['__caminho_atual']) ? $GLOBALS['__caminho_atual'] : '';
	if (!empty($GLOBALS['__e_home'])) { echo '<link rel="canonical" href="'.esc_url(home_url('/')).'">'."\n"; return; }
	/* A PECA NAO E UM SLUG DE UM NIVEL. No site `rel_canonical()` imprime o
	   PERMALINK, que para o CPT `peca` e /loja/<slug>/; remontar o endereco a
	   partir do post_name, como a linha de baixo faz para pagina, servia aqui um
	   canonical de um segmento que o site nunca publica. Medido em 12/09/2026 ao
	   renderizar a primeira ficha: a bancada dizia /vaso-azul-com-flores/ e o site
	   diz /loja/vaso-azul-com-flores/. Defeito da bancada, nao do snippet — e
	   exatamente a familia "a bancada e o site lendo fontes diferentes para o
	   mesmo campo", que a secao 8 manda tratar como defeito e nao como detalhe. */
	if (!empty($GLOBALS['__post_atual'])) {
		echo '<link rel="canonical" href="'.esc_url(get_permalink($GLOBALS['__post_atual'])).'">'."\n";
		return;
	}
	if ('' === $caminho) { return; }
	echo '<link rel="canonical" href="'.esc_url(home_url('/'.$caminho.'/')).'">'."\n";
}
add_action('wp_head','rel_canonical',10);

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
	/* Pagina, nunca peca: sem declarar, `is_singular('peca')` do bloco 4d
	   responderia sim aqui e a ficha da peca sairia dentro da home. */
	$GLOBALS['__tipo_atual']    = 'page';
	$GLOBALS['__post_atual']    = null;
	/* QUAL id o site diria que esta pagina tem — e o que faz `cdm_casca_robots_html()`
	   poder reconhece-la como uma das declaradas fora do indice. */
	if (isset($GLOBALS['__ids_de_teste'][$GLOBALS['__caminho_atual']])) {
		$GLOBALS['__id_atual'] = (int) $GLOBALS['__ids_de_teste'][$GLOBALS['__caminho_atual']];
	}

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
 * Monta a PAGINA DE UMA PECA, que nao e uma pagina com shortcode.
 *
 * No site quem serve a ficha e o filtro `the_content` do snippet da Loja sobre um
 * `is_singular('peca')`, e nao um shortcode — entao a bancada tem de chegar ali
 * pelo mesmo caminho, ou mediria HTML que o site nao serve. O H1 vem do titulo da
 * peca, como o bloco core/post-title do tema faz.
 */
function cdm_teste_pagina_peca($peca, $titulo = 'Clube do Mosaico — teste') {
	$GLOBALS['__pecas_por_id'][(int) $peca->ID] = $peca;
	$GLOBALS['__post_atual']    = $peca;
	$GLOBALS['__id_atual']      = (int) $peca->ID;
	$GLOBALS['__tipo_atual']    = 'peca';
	$GLOBALS['__caminho_atual'] = $peca->post_name;
	$GLOBALS['__e_home']        = false;

	$marca     = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/site-title'));
	$cabecalho = apply_filters('render_block', '<!-- bloco do tema -->', array('blockName'=>'core/navigation'));

	$h1 = apply_filters('render_block',
		'<h1 class="wp-block-post-title">'.htmlspecialchars($peca->post_title, ENT_QUOTES).'</h1>',
		array('blockName'=>'core/post-title')
	)."\n";

	/* O conteudo da peca passa pelos filtros do the_content, com o escape do "&"
	   que o site aplica — a mesma cicatriz de 08/09/2026 vale para a ficha. */
	$corpo = apply_filters('the_content', cdm_teste_escapar_conteudo((string) $peca->post_content));

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
		/* As duas ferramentas, nivel 3 com mae /materiais/, desde o bloco 4. */
		'materiais/qual-cola-usar-no-mosaico'=>true,
		'materiais/quantas-pastilhas-para-mosaico'=>true,
	);
	if ('todas' !== $modo) { return $hoje; }
	foreach (cdm_casca_categorias_do_guia() as $c) {
		if (!empty($c['slug'])) { $hoje[$c['slug']] = true; }
	}
	return $hoje;
}

/**
 * UMA PECA DE MENTIRA, montada dos parametros da consulta.
 *
 * Serve a varredura do bloco 4d: base x disponibilidade x numero de fotos x
 * telefone publicado sao 6 x 2 x 3 x 2 = 72 estados de ficha, e cada um tem de
 * ser medido em PROCESSO PROPRIO (secao 8: o `static` do logotipo faz o cabecalho
 * sumir a partir do segundo render no mesmo processo, e a bancada mede menos do
 * que o site serve sem acusar erro nenhum).
 *
 * Os valores sao os da consulta e nada aqui e calculado: quem decide o que a ficha
 * imprime e o snippet, e quem escreve o esperado e o teste, a mao.
 */
function cdm_teste_peca_de_mentira($g = array()) {
	$id     = 777;
	$fotos  = isset($g['fotos']) ? (int) $g['fotos'] : 2;
	$base   = isset($g['base']) ? $g['base'] : 'ceramica';
	$disp   = isset($g['disp']) ? $g['disp'] : 'pronta_entrega';
	$prazo  = isset($g['prazo']) ? $g['prazo'] : '';
	$preco  = isset($g['preco']) ? $g['preco'] : '189.90';

	$GLOBALS['__anexos'] = array();
	$galeria = array();
	for ($i = 1; $i <= $fotos; $i++) {
		$anexo = 900 + $i;
		$GLOBALS['__anexos'][$anexo] = array(
			'url' => 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/peca-'.$i.'.jpg',
			'largura' => 1200, 'altura' => 1500,
		);
		$galeria[] = $anexo;
	}

	$GLOBALS['__meta'][$id] = array(
		'_cdm_preco'           => $preco,
		'_cdm_disponibilidade' => $disp,
		'_cdm_prazo_dias'      => $prazo,
		'_cdm_medidas'         => '22 × 15 × 15',
		'_cdm_peso_g'          => '640',
		'_cdm_cores'           => 'azul, verde e dourado',
		'_cdm_base'            => $base,
		'_cdm_quantidade'      => '1',
		'_cdm_galeria'         => $galeria,
	);

	/* Os termos precisam existir para a peca ter colecao e tecnica — e eles sao
	   criados pelo proprio snippet no `init`, nunca escritos aqui. */
	$GLOBALS['__objeto_termos'][$id] = array('colecao' => array('centro-de-mesa'), 'tecnica' => array('direto'));

	if (!empty($g['zap'])) { $GLOBALS['__options']['cdm_whatsapp'] = '5511987654321'; }

	return (object) array(
		'ID' => $id, 'post_type' => 'peca', 'post_status' => 'publish',
		'post_title' => 'Vaso azul com flores',
		'post_name'  => 'vaso-azul-com-flores',
		'post_content' => "Um vaso de barro que eu cobri de pastilha azul, com flores de caquinho branco em volta.\n\nEle fica bem numa mesa de jantar ou num aparador.",
		'post_author' => 10, 'post_date_gmt' => '2026-09-12 22:00:00',
	);
}

if (isset($argv[1]) && basename(__FILE__) === basename($argv[0])) {
	$alvo = isset($argv[2]) ? $argv[2] : 'cdm_home';
	$modo = isset($argv[3]) ? $argv[3] : 'hoje';
	/* O quarto argumento e a consulta, no formato de query string:
	   'base=espelho&onde=externo_exposto&junta=3'. Vazio = pagina-ancora. */
	if (isset($argv[4]) && '' !== $argv[4]) { parse_str($argv[4], $_GET); }
	cdm_teste_carregar_options($argv[1]);
	cdm_teste_carregar($argv[1]);
	/* Depois de carregar a casca, porque o modo 'todas' le o registro dela. */
	$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar($modo);

	/* O BLOCO 4d PRECISA DO `init`: o CPT `peca`, as taxonomias, os termos e o
	   papel `artesa` nascem la. Sem isto `post_type_exists('peca')` seria false e
	   a bancada mediria a Loja vazia achando que mede a Loja com peca. */
	do_action('init');

	/* OS IDS DAS PAGINAS, que no site o boot da casca grava na option.
	 *
	 * Sem isto `cdm_casca_robots_html()` nao tem com o que comparar e NENHUMA
	 * pagina sai com `noindex` na bancada — o que faria a afirmacao mais
	 * importante do painel da artesa ("ele nao entra no indice") ser inmedivel
	 * aqui, e "inmedivel" e como o site fica para tras em silencio. Ids
	 * inventados de proposito: o que se mede e a CORRESPONDENCIA entre a pagina
	 * atual e a lista de noindex, nunca o numero. */
	$ids_de_teste = array();
	$n = 1;
	foreach (array_keys(cdm_casca_definicao_paginas()) as $slug) { $ids_de_teste[$slug] = $n++; }
	$GLOBALS['__options']['cdm_casca_paginas'] = $ids_de_teste;
	$GLOBALS['__ids_de_teste'] = $ids_de_teste;

	/* PECA e ATELIE nao sao shortcodes de pagina da casca: o primeiro e um
	   `is_singular('peca')` servido pelo filtro `the_content` do snippet da Loja, e
	   o segundo e uma pagina de estado (deslogada, lista, formulario). Os dois
	   entram por aqui para a varredura poder rodar UM PROCESSO POR ESTADO. */
	if ('PECA' === $alvo) {
		echo cdm_teste_pagina_peca(cdm_teste_peca_de_mentira($_GET));
		return;
	}
	if ('ATELIE' === $alvo) {
		$quem = isset($_GET['quem_sou']) ? $_GET['quem_sou'] : 'deslogada';
		if ('artesa' === $quem) {
			cdm_teste_logar('artesa');
		} elseif ('estranha' === $quem) {
			cdm_teste_logar('subscriber', 11, 'outra');
		}
		if (!empty($_GET['com_peca'])) {
			$p = cdm_teste_peca_de_mentira($_GET);
			$p->post_status = isset($_GET['estado_peca']) ? $_GET['estado_peca'] : 'publish';
			$GLOBALS['__pecas_por_id'][(int) $p->ID] = $p;
			$GLOBALS['__pecas'] = array($p);
		}
		echo cdm_teste_pagina('cdm_atelie');
		return;
	}

	echo cdm_teste_pagina($alvo);
}

<?php
/**
 * Verificacao MEDIDA da CURA DA PORTA DE ENTRADA (secao 6-b da casca), sem site
 * e sem rede.
 *
 *   php ferramentas/teste-cura-da-porta.php .
 *
 * POR QUE ESTE ARQUIVO EXISTE. O item 1 do despacho de classe da Sentinela de
 * 11/11/2026 pede que a casca passe a repor sozinha o bloco `# BEGIN WordPress`
 * do `.htaccess` da raiz, e a 29.4 do ARQUIPELAGO.md tinha recusado gancho
 * automatico com um argumento que continua certo: "porta de entrada que se
 * conserta CALADA a cada carregamento e a que ninguem consegue desfazer no dia
 * em que estiver errada". A diferenca entre a cura e o que a 29.4 recusou nao
 * esta na intencao de ninguem — esta nestas afirmacoes. Sem elas, a excecao da
 * 29.4 seria uma promessa.
 *
 * OS SEIS MUNDOS, e cada um existe porque um desfecho diferente tem de sair:
 *
 *   A. porta caida, as quatro grandezas na mesa  -> CURA, e uma linha no log
 *      com o antes e o depois em bytes e em blocos
 *   B. porta de pe, mil requisicoes              -> arquivo intocado (byte,
 *      tamanho e mtime), ZERO linha de log, ZERO option gravada
 *   C. mod_rewrite desligado                     -> NAO cura, e o log diz isso
 *   D. raiz nao gravavel                         -> NAO cura, e o log diz isso
 *   E. hora nao vencida                          -> NAO cura e NAO fala
 *   F. flush roda e o bloco nao volta            -> log diz FALHOU, separado do
 *      sucesso (e o mundo do `AllowOverride` desligado, que e chamado na
 *      HostGator e nao codigo desta ilha)
 *
 * OS MUNDOS C E D SE MEDEM COM RETRATO FABRICADO, e isso nao e atalho: este
 * contentor roda como root, e o `is_writable()` do PHP responde `true` para
 * diretorio 0444 quando quem pergunta e root. "Raiz nao gravavel" nao se encena
 * no disco daqui. E por isso que a regra inteira mora numa funcao PURA
 * (`cdm_casca_cura_decidir`), que recebe o retrato e devolve a decisao: o que
 * nao se fabrica no disco se fabrica no retrato. O mundo A e o B, que sao sobre
 * o arquivo de verdade, rodam contra um `.htaccess` de verdade num diretorio
 * temporario.
 *
 * O QUE ELE NAO PROVA, escrito para ninguem ler verde aqui como ilha no ar: que
 * o Apache obedece ao arquivo. Isso e o `AllowOverride`, mora no hospedeiro, e
 * so a leitura das URLs no ar responde (29.2 e 29.4).
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function cura_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-66s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-66s %s\n", $rotulo, $medida );
	return false;
}

/* O LOG DE MENTIRA, definido ANTES dos snippets. A casca escreve a linha da cura
   pelas funcoes do snippet do Sync, e a bancada nao carrega aquele snippet de
   proposito ("fala com o WP de verdade"). As duas funcoes aqui tem a forma
   exata das de la: `estado` le a option, `log` empilha por cima e corta a lista.
   E a guarda `function_exists` da casca e o que faz esta substituicao valer. */
$GLOBALS['__options']['clubedomosaico_sync_estado'] = array( 'revisao' => 93, 'ultimo' => null, 'itens' => array(), 'log' => array() );
function clubedomosaico_sync_estado() {
	$e = get_option( 'clubedomosaico_sync_estado' );
	return is_array( $e ) ? $e : array( 'revisao' => -1, 'ultimo' => null, 'itens' => array(), 'log' => array() );
}
function clubedomosaico_sync_log( &$estado, $msg ) {
	array_unshift( $estado['log'], current_time( 'Y-m-d H:i' ) . ' ' . $msg );
	$estado['log'] = array_slice( $estado['log'], 0, 40 );
}

cdm_teste_carregar( $raiz );

if ( ! function_exists( 'cdm_casca_cura_da_porta' ) ) {
	echo "FALHA: a casca nao define cdm_casca_cura_da_porta — a secao 6-b nao esta neste repositorio.\n";
	exit( 1 );
}

/* ----------------------------------------------------------------- o mundo */

$dir = sys_get_temp_dir() . '/cdm-cura-' . getmypid();
@mkdir( $dir, 0777, true );
$arq = $dir . '/.htaccess';

/* O `.htaccess` CAIDO, byte por byte como o do ar: um bloco so, `NFD EPC`, e as
   8 linhas de Rewrite* que sobram sem o bloco do WordPress. */
$caido = "# BEGIN NFD EPC\n<IfModule mod_rewrite.c>\nRewriteEngine On\nRewriteBase /\nRewriteRule ^wp-content/.* - [L]\nRewriteCond %{HTTP_USER_AGENT} !bot\nRewriteCond %{REQUEST_METHOD} GET\nRewriteRule ^(.*)$ - [E=CACHE:1]\nRewriteRule ^$ - [L]\n</IfModule>\n# END NFD EPC\n";

function cura_zerar( $arq, $texto ) {
	file_put_contents( $arq, $texto );
	$GLOBALS['__options']['clubedomosaico_sync_estado'] = array( 'revisao' => 93, 'ultimo' => null, 'itens' => array(), 'log' => array() );
	unset( $GLOBALS['__options'][ CDM_CASCA_CURA_OPTION ] );
	$GLOBALS['__reescritas']     = 0;
	$GLOBALS['__mod_rewrite']    = true;
	$GLOBALS['__flush_nao_repoe'] = false;
	clearstatcache( true, $arq );
}

function cura_log() {
	$e = get_option( 'clubedomosaico_sync_estado' );
	return isset( $e['log'] ) && is_array( $e['log'] ) ? $e['log'] : array();
}

$GLOBALS['__raiz_de_teste']     = $dir;
$GLOBALS['__htaccess_de_teste'] = $arq;
unset( $_GET['rest_route'], $_SERVER['REQUEST_URI'] );

echo "\nMUNDO A — a porta esta caida e as quatro grandezas estao na mesa\n";

cura_zerar( $arq, $caido );
$antes_bytes = filesize( $arq );
$linha       = cdm_casca_cura_da_porta();
clearstatcache( true, $arq );
$depois_texto = (string) file_get_contents( $arq );
$log          = cura_log();

cura_ok( 1 === count( $log ), 'a cura escreve EXATAMENTE uma linha no log do /status', count( $log ) . ' linha(s)' );
cura_ok( (bool) preg_match( '/^#\s*BEGIN\s+WordPress\s*$/mi', $depois_texto ), 'o bloco # BEGIN WordPress volta ao arquivo', strlen( $depois_texto ) . ' bytes' );
cura_ok( false !== strpos( $depois_texto, 'NFD EPC' ), 'o bloco do hospedeiro NAO e apagado pela cura', 'NFD EPC preservado' );
cura_ok( false !== strpos( $linha, 'cura da porta: bloco WordPress reposto' ), 'a linha diz que a cura aconteceu, em portugues', substr( $linha, 0, 58 ) );
cura_ok( false !== strpos( $linha, (string) $antes_bytes . ' bytes' ), 'a linha traz os BYTES DE ANTES', $antes_bytes . ' bytes' );
cura_ok( false !== strpos( $linha, (string) strlen( $depois_texto ) . ' bytes' ), 'a linha traz os BYTES DE DEPOIS', strlen( $depois_texto ) . ' bytes' );
cura_ok( false !== strpos( $linha, '[NFD EPC]' ) && false !== strpos( $linha, 'NFD EPC, WordPress' ), 'a linha traz os BLOCOS de antes e de depois', 'antes [NFD EPC] -> depois [NFD EPC, WordPress]' );
cura_ok( false === strpos( $linha, 'RewriteRule' ) && false === strpos( $linha, 'IfModule' ), 'a linha NAO despeja o conteudo do arquivo (29.3: log do /status e publico)', 'nenhuma diretiva na linha' );
cura_ok( (int) get_option( CDM_CASCA_CURA_OPTION, 0 ) > 0, 'a hora da tentativa fica gravada na option', (string) get_option( CDM_CASCA_CURA_OPTION, 0 ) );

echo "\nMUNDO B — a porta esta de pe, e mil requisicoes passam por cima dela\n";

cura_zerar( $arq, $depois_texto );
$assinatura_antes = array( filesize( $arq ), filemtime( $arq ), md5_file( $arq ) );
$falou            = 0;
for ( $i = 0; $i < 1000; $i++ ) {
	if ( '' !== cdm_casca_cura_da_porta() ) { $falou++; }
}
clearstatcache( true, $arq );
$assinatura_depois = array( filesize( $arq ), filemtime( $arq ), md5_file( $arq ) );

cura_ok( 0 === $falou, 'mil requisicoes com a porta de pe nao dizem NADA', $falou . ' linha(s) devolvida(s)' );
cura_ok( 0 === count( cura_log() ), 'o log do /status nao ganha linha nenhuma', count( cura_log() ) . ' linha(s)' );
cura_ok( $assinatura_antes === $assinatura_depois, 'o arquivo fica intocado em byte, tamanho e mtime', 'md5 ' . substr( $assinatura_depois[2], 0, 8 ) );
cura_ok( 0 === (int) $GLOBALS['__reescritas'], 'nenhum flush_rewrite_rules e disparado', (string) (int) $GLOBALS['__reescritas'] );
cura_ok( null === get_option( CDM_CASCA_CURA_OPTION, null ), 'nenhuma option e gravada com a porta de pe', 'option ausente' );

echo "\nMUNDO C — mod_rewrite desligado (retrato fabricado: nao se encena como root)\n";

$retrato_caido = array(
	'mod_rewrite'          => false,
	'raiz_gravavel'        => true,
	'ferramentas_de_admin' => true,
	'htaccess'             => array( 'existe' => true, 'legivel' => true, 'gravavel' => true, 'bytes' => 1057, 'blocos' => array( 'NFD EPC' ), 'tem_wordpress' => false ),
);
$d = cdm_casca_cura_decidir( $retrato_caido, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ), 'com mod_rewrite desligado a cura NAO dispara', 'curar=' . var_export( $d['curar'], true ) );
cura_ok( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'mod_rewrite' ), 'e o motivo nomeia o mod_rewrite', (string) $d['motivo'] );

echo "\nMUNDO D — raiz nao gravavel\n";

$r = $retrato_caido; $r['mod_rewrite'] = true; $r['raiz_gravavel'] = false;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ), 'com a raiz nao gravavel a cura NAO dispara', 'curar=' . var_export( $d['curar'], true ) );
cura_ok( ! empty( $d['motivo'] ) && false !== strpos( $d['motivo'], 'gravavel' ), 'e o motivo nomeia a gravacao', (string) $d['motivo'] );

$r = $retrato_caido; $r['mod_rewrite'] = true; $r['htaccess']['gravavel'] = false;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ) && ! empty( $d['motivo'] ), 'arquivo existente e nao gravavel tambem para a cura, com motivo', (string) $d['motivo'] );

$r = $retrato_caido; $r['mod_rewrite'] = true; $r['ferramentas_de_admin'] = false;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ) && false !== strpos( (string) $d['motivo'], 'wp-admin' ), 'sem as funcoes de wp-admin a cura NAO dispara (o flush(true) viraria flush(false))', (string) $d['motivo'] );

$r = $retrato_caido; $r['mod_rewrite'] = true; $r['htaccess']['existe'] = false;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ) && false !== strpos( (string) $d['motivo'], 'nao existe' ), 'arquivo ausente nao e tratado como porta de pe nem como mundo de cura', (string) $d['motivo'] );

$r = $retrato_caido; $r['mod_rewrite'] = true; $r['htaccess']['tem_wordpress'] = true;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( empty( $d['curar'] ) && null === $d['motivo'], 'porta de pe: nao cura e NAO FALA (motivo null)', 'motivo null' );

$r = $retrato_caido; $r['mod_rewrite'] = true;
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( ! empty( $d['curar'] ) && null === $d['motivo'], 'as quatro grandezas na mesa: cura, sem motivo de recusa', 'curar=true' );

echo "\nMUNDO E — a hora nao venceu\n";

$d = cdm_casca_cura_decidir( $r, 999000, 1000000, 3600 );
cura_ok( empty( $d['curar'] ) && null === $d['motivo'], 'tentativa ha 1.000 s: nao cura e NAO enche o log', '1000 s < 3600 s' );
$d = cdm_casca_cura_decidir( $r, 996000, 1000000, 3600 );
cura_ok( ! empty( $d['curar'] ), 'tentativa ha 4.000 s: cura de novo', '4000 s > 3600 s' );
$d = cdm_casca_cura_decidir( $r, 0, 1000000, 3600 );
cura_ok( ! empty( $d['curar'] ), 'primeira vez de todas (option ausente, vale 0) nao e lida como "ha pouco"', 'ultima=0' );

/* E O MESMO NO GANCHO DE VERDADE, porque a funcao pura concordar com a regra nao
   prova que o gancho a consulta: ele tem um atalho de custo que sai antes dela. */
cura_zerar( $arq, $caido );
$primeira = cdm_casca_cura_da_porta();
$GLOBALS['__options'][ CDM_CASCA_CURA_OPTION ] = time();
file_put_contents( $arq, $caido );
clearstatcache( true, $arq );
$segunda = cdm_casca_cura_da_porta();
clearstatcache( true, $arq );
cura_ok( '' !== $primeira && '' === $segunda, 'no gancho: a 1a requisicao cura, a 2a dentro da hora fica calada', '1a=' . ( '' !== $primeira ? 'falou' : 'calada' ) . ' / 2a=' . ( '' !== $segunda ? 'falou' : 'calada' ) );
cura_ok( false === (bool) preg_match( '/^#\s*BEGIN\s+WordPress\s*$/mi', (string) file_get_contents( $arq ) ), 'e a porta derrubada de novo dentro da hora NAO e tocada', 'arquivo segue sem o bloco' );

echo "\nMUNDO F — o flush roda e o bloco nao volta (AllowOverride do hospedeiro)\n";

cura_zerar( $arq, $caido );
$GLOBALS['__flush_nao_repoe'] = true;
$linha_f = cdm_casca_cura_da_porta();
cura_ok( false !== strpos( $linha_f, 'cura da porta FALHOU' ), 'a linha diz FALHOU, com palavra diferente da do sucesso', substr( $linha_f, 0, 48 ) );
cura_ok( false !== stripos( $linha_f, 'AllowOverride' ), 'e nomeia a hipotese do hospedeiro, que e chamado e nao codigo', 'AllowOverride citado' );
cura_ok( 1 === count( cura_log() ), 'a falha tambem escreve exatamente uma linha', count( cura_log() ) . ' linha(s)' );
cura_ok( 1 === (int) $GLOBALS['__reescritas'], 'e o flush foi de fato chamado uma vez', (string) (int) $GLOBALS['__reescritas'] );

echo "\nMUNDO G — a rota que MEDE a porta nunca e curada no meio da propria medicao\n";

cura_zerar( $arq, $caido );
$_GET['rest_route'] = '/clubedomosaico/v1/rotas';
$linha_g = cdm_casca_cura_da_porta();
clearstatcache( true, $arq );
cura_ok( '' === $linha_g, 'na rota /rotas a cura se cala', 'nada devolvido' );
cura_ok( false === (bool) preg_match( '/^#\s*BEGIN\s+WordPress\s*$/mi', (string) file_get_contents( $arq ) ), 'e o retrato que a Sentinela le continua mostrando a porta caida', 'arquivo intocado' );
/* A FORMA BONITA DA MESMA ROTA NAO E CONFERIDA, E E DE PROPOSITO: com a porta no
   chao `/wp-json/...` morre antes do PHP (29.1), e com a porta de pe a cura sai
   no primeiro passo do gancho. Esta afirmacao mede que o caso que SOBRA — a
   forma bonita com a porta de pe — e silencio por outro caminho, e nao um furo. */
unset( $_GET['rest_route'] );
cura_zerar( $arq, rtrim( $caido, "\n" ) . "\n\n" . cdm_teste_bloco_wordpress() . "\n" );
cura_ok( '' === cdm_casca_cura_da_porta(), 'porta de pe e a cura se cala venha a requisicao de onde vier', 'bloco presente' );
cura_zerar( $arq, $caido );
cura_ok( '' !== cdm_casca_cura_da_porta(), 'e em QUALQUER outra requisicao, com a porta caida, ela volta a curar', 'curou fora da rota' );

echo "\nMUNDO H — DOIS retratos na MESMA requisicao, que e o que o reparo faz\n";

/* A REGRESSAO QUE ESTE MUNDO EXISTE PARA PRENDER, e ela foi medida aqui em
   12/11/2026, nao imaginada: `blocos` e `tem_wordpress` vem de
   `file_get_contents` (sem cache) e `bytes`/`mtime` de `filesize`/`filemtime`
   (com cache de `stat`). Sem o `clearstatcache` que o diagnostico passou a
   fazer, o retrato de DEPOIS saia com o tamanho de ANTES ao lado do conteudo
   de DEPOIS — 255 bytes com [NFD EPC, WordPress] dentro. Um retrato em que
   metade dos campos e de um mundo e metade do outro. */
cura_zerar( $arq, $caido );
$r1 = cdm_casca_diagnostico_rotas();
file_put_contents( $arq, rtrim( $caido, "\n" ) . "\n\n" . cdm_teste_bloco_wordpress() . "\n" );
$r2 = cdm_casca_diagnostico_rotas();
$tamanho_real = strlen( (string) file_get_contents( $arq ) );
cura_ok( (int) $r1['htaccess']['bytes'] === strlen( $caido ), 'o 1o retrato traz o tamanho da porta caida', $r1['htaccess']['bytes'] . ' bytes' );
cura_ok( (int) $r2['htaccess']['bytes'] === $tamanho_real, 'o 2o retrato, na MESMA requisicao, traz o tamanho NOVO e nao o do cache de stat', $r2['htaccess']['bytes'] . ' de ' . $tamanho_real . ' bytes' );
cura_ok( (int) $r2['htaccess']['bytes'] !== (int) $r1['htaccess']['bytes'], 'os dois retratos discordam no tamanho, que e o que prova que o cache saiu', $r1['htaccess']['bytes'] . ' -> ' . $r2['htaccess']['bytes'] );
cura_ok( ! empty( $r2['htaccess']['tem_wordpress'] ) && (int) $r2['htaccess']['linhas_rewrite'] > (int) $r1['htaccess']['linhas_rewrite'], 'e conteudo e tamanho contam a MESMA historia nos dois retratos', $r1['htaccess']['linhas_rewrite'] . ' -> ' . $r2['htaccess']['linhas_rewrite'] . ' linhas de Rewrite*' );

echo "\nMUNDO I — a ROTA da 29.3: o reparo, o antes/depois, e o que NAO pode sair na resposta\n";

/* ESTE MUNDO FECHA O DESPACHO NORMAL DE 03/11/2026 (`dados/despachos.md`), que
   pedia duas coisas desta ilha: a linha `clearstatcache()` no topo do
   diagnostico E O PORTAO JUNTO — "senao a linha e retirada no primeiro dia em
   que alguem a achar redundante", que foi a licao do despacho do `realpath('')`.
   O portao modelo citado la e o `teste-rotas.php` da rodametria, e ele NAO foi
   copiado linha a linha de proposito: metade dele (os tres codigos de erro da
   parede do token) mede uma casca cuja fonte de token nao estava conferida no
   chao, e a desta ilha esta — o `permission_callback` daqui devolve bool, nao
   codigo. O que foi copiado e o que ele MEDE, com as reguas desta casca. */
cura_zerar( $arq, $caido );
$rep = cdm_casca_reparar_rotas();
cura_ok( ! empty( $rep['reparado'] ), 'o reparo devolve reparado=true no mundo medido das seis quedas', var_export( $rep['reparado'], true ) );
cura_ok( empty( $rep['antes']['htaccess']['tem_wordpress'] ) && ! empty( $rep['depois']['htaccess']['tem_wordpress'] ), 'o antes diz false e o depois diz true — o campo e medicao, nao afirmacao', 'false -> true' );
cura_ok( (int) $rep['antes']['htaccess']['bytes'] < (int) $rep['depois']['htaccess']['bytes'], 'o antes e o depois trazem tamanhos DIFERENTES (a afirmacao que reprovava sem clearstatcache)', $rep['antes']['htaccess']['bytes'] . ' < ' . $rep['depois']['htaccess']['bytes'] );
cura_ok( (int) $rep['antes']['htaccess']['linhas_rewrite'] < (int) $rep['depois']['htaccess']['linhas_rewrite'], 'e linhas de Rewrite* tambem crescem', $rep['antes']['htaccess']['linhas_rewrite'] . ' -> ' . $rep['depois']['htaccess']['linhas_rewrite'] );

/* O SEGREDO DO SERVIDOR NAO SAI NA RESPOSTA (29.3, literal). O mundo fabricado
   carrega uma linha que nao pode aparecer em lugar nenhum do JSON. */
$segredo = 'SetEnvIf Request_URI SENHA-DO-TERCEIRO-NAO-PODE-SAIR';
cura_zerar( $arq, "# BEGIN NFD EPC\n" . $segredo . "\nRewriteEngine On\n# END NFD EPC\n" );
$json = json_encode( cdm_casca_diagnostico_rotas() );
cura_ok( false === strpos( $json, 'SENHA-DO-TERCEIRO' ), 'o conteudo do .htaccess NAO sai na resposta da rota (29.3)', 'linha-segredo ausente do JSON' );
cura_ok( false !== strpos( $json, 'NFD EPC' ), 'mas os NOMES dos blocos saem, que e o que a 29.3 manda sair', 'NFD EPC presente' );

/* O ARQUIVO QUE NAO EXISTIA E QUE O REPARO CRIOU. O despacho de 03/11 nomeia
   este caso: `reparado` e calculado sobre `existe`, e com o cache de stat velho
   ele saia `false` DEPOIS de a porta ter sido consertada — reprovacao falsa, que
   a 20.5 diz ser a pior das duas, porque quem a le abre chamado na HostGator por
   um defeito que o reparo ja desfez. */
cura_zerar( $arq, $caido );
@unlink( $arq );
clearstatcache( true, $arq );
$d_sem = cdm_casca_diagnostico_rotas();
cura_ok( empty( $d_sem['htaccess']['existe'] ), 'sem arquivo, o diagnostico diz que ele nao existe', 'existe=false' );
file_put_contents( $arq, rtrim( $caido, "\n" ) . "\n\n" . cdm_teste_bloco_wordpress() . "\n" );
$d_com = cdm_casca_diagnostico_rotas();
cura_ok( ! empty( $d_com['htaccess']['existe'] ) && (int) $d_com['htaccess']['bytes'] > 0, 'e o retrato seguinte, na MESMA requisicao, ve o arquivo que nasceu', $d_com['htaccess']['bytes'] . ' bytes' );

echo "\nMUNDO J — sem as ferramentas de wp-admin, em PROCESSO SEPARADO\n";

/* `function_exists()` nao se desfaz, entao o ramo da recusa mora numa filha com
   CDM_SEM_ADMIN=1. Um `reparado: true` aqui seria um verde dizendo que a porta
   foi consertada quando o flush(true) virou flush(false) e nao encostou no
   arquivo — e e a 4a coisa que o portao modelo da rodametria mede. */
if ( '1' === (string) getenv( 'CDM_SEM_ADMIN' ) ) {
	cura_zerar( $arq, $caido );
	$r = cdm_casca_reparar_rotas();
	$conteudo = (string) file_get_contents( $arq );
	$falhou = ( empty( $r['reparado'] ) && ! empty( $r['motivo'] ) && false === strpos( $conteudo, 'BEGIN WordPress' ) ) ? 0 : 1;
	echo '  filha CDM_SEM_ADMIN=1: reparado=' . var_export( $r['reparado'], true ) . ', motivo=' . var_export( $r['motivo'], true ) . "\n";
	@unlink( $arq ); @rmdir( $dir );
	exit( $falhou );
}
$cmd = escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __FILE__ ) . ' ' . escapeshellarg( $raiz ) . ' 2>&1';
$saida_filha = array();
$codigo_filha = 1;
exec( 'CDM_SEM_ADMIN=1 ' . $cmd, $saida_filha, $codigo_filha );
$texto_filha = implode( "\n", $saida_filha );
cura_ok( 0 === (int) $codigo_filha, 'sem save_mod_rewrite_rules o reparo RECUSA, com motivo, e NAO escreve no arquivo', 'filha saiu ' . (int) $codigo_filha );
cura_ok( false !== strpos( $texto_filha, 'wp-admin' ), 'e o motivo da recusa nomeia wp-admin/includes', 'motivo nomeado na filha' );

echo "\nMUNDO K — A MUTACAO: tirar o clearstatcache do diagnostico tem de REPROVAR\n";

/* TRAVA QUE NUNCA FALHOU NAO E TRAVA. A linha que este bloco acrescentou ao
   diagnostico e de UMA palavra, e e exatamente o tipo de linha que a proxima
   passada apaga por achar redundante — foi a licao do despacho do `realpath('')`,
   citada no despacho de 03/11 que manda copiar o portao junto com a linha.
   Aqui a mutacao e feita de verdade: os snippets sao copiados para um diretorio
   temporario, a linha e retirada, e o portao roda contra a casca mutante numa
   filha que tem de SAIR 1. */
/* A FILHA MUTANTE NAO REFAZ ESTE MUNDO, e esta guarda nao e detalhe: sem ela o
   portao se chama a si mesmo sem fundo — a filha mutante copia snippets JA sem a
   linha, entao a afirmacao "achou a linha" falha nela e ela segue adiante para
   gerar OUTRA filha, para sempre. Medido doendo em 12/11/2026, na primeira
   execucao deste mundo. */
if ( '1' === (string) getenv( 'CDM_MUTANTE' ) ) {
	printf( "\n%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
	echo $falhas ? "REPROVADO\n" : "APROVADO\n";
	@unlink( $arq ); @rmdir( $dir );
	exit( $falhas ? 1 : 0 );
}
$mut = sys_get_temp_dir() . '/cdm-mut-' . getmypid();
@mkdir( $mut . '/snippets', 0777, true );
$copiados = 0;
foreach ( glob( $raiz . '/snippets/*.php' ) as $f ) {
	$corpo = (string) file_get_contents( $f );
	if ( false !== strpos( $corpo, 'clearstatcache( true, $arquivo );' ) ) {
		$corpo = str_replace( 'clearstatcache( true, $arquivo );', '/* MUTANTE: linha retirada */', $corpo );
		$copiados++;
	}
	file_put_contents( $mut . '/snippets/' . basename( $f ), $corpo );
}
cura_ok( 1 === $copiados, 'a mutacao achou a linha do clearstatcache no diagnostico, uma vez', $copiados . ' ocorrencia(s)' );
$saida_mut = array();
$codigo_mut = 0;
exec( 'CDM_MUTANTE=1 ' . escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __FILE__ ) . ' ' . escapeshellarg( $mut ) . ' 2>&1', $saida_mut, $codigo_mut );
cura_ok( 0 !== (int) $codigo_mut, 'o portao REPROVA a casca sem o clearstatcache — a trava morde', 'filha mutante saiu ' . (int) $codigo_mut );
cura_ok( false !== strpos( implode( "\n", $saida_mut ), 'cache de stat' ), 'e reprova NA afirmacao do cache de stat, nao por acidente em outra', 'mundo H acusou' );
foreach ( glob( $mut . '/snippets/*.php' ) as $f ) { @unlink( $f ); }
@rmdir( $mut . '/snippets' ); @rmdir( $mut );

/* -------------------------------------------------------------- fim do mundo */

@unlink( $arq );
@rmdir( $dir );

printf( "\n%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
echo $falhas ? "REPROVADO\n" : "APROVADO\n";
exit( $falhas ? 1 : 0 );

<?php
/**
 * Verificacao MEDIDA do artigo-ancora A1, sem site e sem rede.
 *
 *   php ferramentas/teste-a1.php .
 *
 * E a secao 8 do ARQUIPELAGO.md executada onde da para executa-la, e mede tres
 * coisas que os outros dois testes desta ilha nao medem:
 *
 *   1. A TESE. O artigo afirma um numero — "nenhuma peca atravessa marca", "a
 *      maior lista tem N codigos" — e este arquivo RECALCULA esse numero direto
 *      de dados/pecas.json e dados/modelos-robo.json, em PHP, sem olhar para o
 *      que o gerador em Python escreveu. Se as duas contas divergirem, uma das
 *      duas esta errada e a pagina nao vai ao ar. Nao e redundancia: e a unica
 *      forma de a tese de um artigo ser verificavel em vez de acreditada.
 *   2. A MALHA (secao 9). Duas listagens e tres irmas, com o link de mao dupla
 *      com a R1 conferido nos DOIS sentidos — porque um artigo-ancora que so e
 *      apontado, e nao aponta de volta, e um beco.
 *   3. A ORDEM DA SECAO 7. Porta de compra antes da prova de procedencia, na
 *      pagina e dentro de cada cartao, com o aviso de comissao no bloco de
 *      compra. E a mesma medicao que a R1 ganhou no item 0 do despacho de 10/09,
 *      e ela nasce junto com esta pagina em vez de virar retrofit.
 *
 * O que ele NAO substitui: a conferencia da revisao aplicada no /status depois
 * do Sync (secao 4). Este arquivo prova que o codigo esta certo; so o /status
 * prova que ele esta NO AR.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function rbm_ok( $condicao, $rotulo, $medida = '' ) {
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

/** So os blocos <script>, que e onde a contagem de &#038; vale (secao 8). */
function rbm_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

function rbm_sem_acento( $t ) {
	$de   = array( 'á','à','â','ã','ä','é','ê','ë','í','î','ï','ó','ô','õ','ö','ú','û','ü','ç','Á','À','Â','Ã','É','Ê','Í','Ó','Ô','Õ','Ú','Ç' );
	$para = array( 'a','a','a','a','a','e','e','e','i','i','i','o','o','o','o','u','u','u','c','A','A','A','A','E','E','I','O','O','O','U','C' );
	return str_replace( $de, $para, $t );
}

/* ---------------------------------------------------------------------------
 * Montagem: os fatos vem do repositorio, e as paginas "existem" para o teste.
 * ------------------------------------------------------------------------- */

$fatos     = json_decode( file_get_contents( $raiz . '/dados/a1-fatos.json' ), true );
$modelos_b = json_decode( file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );
$pecas_b   = json_decode( file_get_contents( $raiz . '/dados/pecas.json' ), true );

$GLOBALS['__paginas'] = array(
	'ferramentas'                           => true,
	'metodologia'                           => true,
	'sobre'                                 => true,
	'divulgacao-de-afiliados'               => true,
	'qual-peca-serve-no-meu-robo-aspirador'  => true,
	'filtro-universal-de-robo-aspirador'     => true,
);
$GLOBALS['__options']['robometria_dados_a1-fatos'] = $fatos;

robometria_teste_carregar( $raiz );
add_filter( 'robometria_a1_na_pagina', function ( $v ) { return true; } );

$pagina  = robometria_teste_pagina( 'robometria_a1', 'Robometria — A1' );
$retorno = $GLOBALS['__retorno_shortcode'];

echo "Robometria — verificacao do artigo-ancora A1\n\n";

/* ---------------------------------------------------------------------------
 * 1. O defeito que derrubou cinco calculadoras da Aquametria (secao 8).
 * ------------------------------------------------------------------------- */
echo "1. JS e CSS fora do retorno do shortcode (secao 8)\n";

rbm_ok( false === stripos( $retorno, '<script' ),
	'nenhum <script> dentro do retorno do shortcode' );
rbm_ok( false === stripos( $retorno, '<style' ),
	'nenhum <style> dentro do retorno do shortcode' );
rbm_ok( false !== strpos( $pagina, '<style id="robometria-a1">' ),
	'a folha do artigo sai pelo wp_head, e nao pelo conteudo' );
rbm_ok( false !== strpos( $pagina, 'id="robometria-a1-jsonld"' ),
	'o JSON-LD sai pelo wp_head, e nao pelo conteudo' );

/* ---------------------------------------------------------------------------
 * 2. Entidades dentro de <script> (secao 8, item 2). Contar na pagina inteira
 *    e teste ERRADO: a casca do tema tem ocorrencias legitimas.
 * ------------------------------------------------------------------------- */
echo "\n2. Entidades dentro de <script> (secao 8, item 2)\n";

$scripts = rbm_scripts( $pagina );
rbm_ok( 0 === substr_count( $scripts, '&#038;' ),
	'zero &#038; DENTRO dos blocos <script>',
	substr_count( $scripts, '&#038;' ) . ' ocorrencia(s)' );

/* ---------------------------------------------------------------------------
 * 3. A TESE, RECALCULADA AQUI.
 *
 * Segunda implementacao, em PHP, direto do banco. O gerador em Python nao e
 * consultado — e esse e o ponto: duas contas independentes que batem sao
 * medicao; uma conta sozinha e so o que o autor achou.
 * ------------------------------------------------------------------------- */
echo "\n3. A tese do artigo, recalculada do banco por uma segunda implementacao\n";

$marca_do_modelo = array();
foreach ( $modelos_b['registros'] as $m ) {
	$marca_do_modelo[ $m['id'] ] = $m['marca'];
}

$pecas_pub      = 0;
$pares          = 0;
$atravessam     = 0;
$maior          = 0;
$maior_id       = '';
$conj_por_marca = array();
$pecas_sem_link = 0;

foreach ( $pecas_b['registros'] as $p ) {
	if ( 'publicavel' !== $p['status'] ) {
		continue;
	}
	$pecas_pub++;

	$marcas   = array();
	$conjunto = array();
	foreach ( $p['compatibilidade'] as $c ) {
		$pares++;
		$conjunto[] = $c['modelo'];
		if ( isset( $marca_do_modelo[ $c['modelo'] ] ) ) {
			$marcas[ $marca_do_modelo[ $c['modelo'] ] ] = true;
		}
	}
	if ( count( $marcas ) > 1 ) {
		$atravessam++;
	}
	if ( count( $p['compatibilidade'] ) > $maior ) {
		$maior    = count( $p['compatibilidade'] );
		$maior_id = $p['id'];
	}
	sort( $conjunto );
	$conj_por_marca[ $p['marca'] ]['pecas'] = isset( $conj_por_marca[ $p['marca'] ]['pecas'] )
		? $conj_por_marca[ $p['marca'] ]['pecas'] + 1 : 1;
	$conj_por_marca[ $p['marca'] ]['conjuntos'][ implode( '|', $conjunto ) ] = true;

	if ( empty( $p['afiliado']['url'] ) ) {
		$pecas_sem_link++;
	}
}

$r = $fatos['resumo'];
rbm_ok( (int) $r['pecas_publicaveis'] === $pecas_pub,
	'pecas publicaveis: os fatos batem com o banco',
	$r['pecas_publicaveis'] . ' / ' . $pecas_pub );
rbm_ok( (int) $r['pares_declarados'] === $pares,
	'pares peca x modelo: os fatos batem com o banco',
	$r['pares_declarados'] . ' / ' . $pares );
rbm_ok( (int) $r['pecas_que_atravessam_marca'] === $atravessam,
	'pecas que atravessam marca: os fatos batem com o banco',
	$r['pecas_que_atravessam_marca'] . ' / ' . $atravessam );
rbm_ok( (int) $fatos['maior_alcance']['codigos_declarados'] === $maior
	&& $fatos['maior_alcance']['peca'] === $maior_id,
	'a peca de maior alcance e a mesma nas duas contas',
	$fatos['maior_alcance']['peca'] . ' com ' . $maior . ' codigos' );
rbm_ok( (int) $r['pecas_esperando_link'] === $pecas_sem_link,
	'pecas esperando link de afiliado: os fatos batem com o banco',
	$r['pecas_esperando_link'] . ' / ' . $pecas_sem_link );

$dispersao_ok = true;
foreach ( $fatos['dispersao'] as $d ) {
	$b = isset( $conj_por_marca[ $d['marca'] ] ) ? $conj_por_marca[ $d['marca'] ] : null;
	if ( ! $b || (int) $d['pecas'] !== $b['pecas']
		|| (int) $d['conjuntos_distintos'] !== count( $b['conjuntos'] ) ) {
		$dispersao_ok = false;
	}
}
rbm_ok( $dispersao_ok,
	'dispersao por marca: as duas contas batem em todas as marcas',
	count( $fatos['dispersao'] ) . ' marcas' );

/* A tese do TEXTO so vale enquanto o banco a sustenta. Se um dia uma peca
   atravessar marca, a frase de abertura vira mentira — e este teste reprova
   antes de a pagina ir ao ar, que e a razao de ele existir. */
$abertura = strpos( $pagina, 'rbm-linha-mestra' );
$diz_nenhuma = ( false !== strpos( $pagina, 'nenhuma é declarada para modelos de mais de uma marca' ) );
rbm_ok( ( 0 === $atravessam ) === $diz_nenhuma,
	'a frase de abertura so afirma "nenhuma atravessa marca" se o banco sustentar',
	$atravessam . ' atravessam; texto ' . ( $diz_nenhuma ? 'afirma' : 'nao afirma' ) );

/* ---------------------------------------------------------------------------
 * 4. O portao da secao 9: itens de banco reais e numero calculado proprio.
 * ------------------------------------------------------------------------- */
echo "\n4. Portao da secao 9 (itens de banco reais + numero proprio)\n";

rbm_ok( count( $fatos['vitrine'] ) >= 3,
	'a pagina serve pelo menos 3 itens de banco reais',
	count( $fatos['vitrine'] ) . ' itens' );

$ids_reais = array();
foreach ( $pecas_b['registros'] as $p ) {
	$ids_reais[ $p['id'] ] = true;
}
$forasteiros = array();
foreach ( $fatos['vitrine'] as $v ) {
	if ( ! isset( $ids_reais[ $v['peca'] ] ) ) {
		$forasteiros[] = $v['peca'];
	}
}
rbm_ok( empty( $forasteiros ),
	'todo item da vitrine existe no banco commitado',
	empty( $forasteiros ) ? 'todos' : implode( ' ', $forasteiros ) );

/* Kit sem composicao transcrita NAO pode estar na vitrine: a pagina nao sabe o
   que vem dentro, e oferecer a compra assim e o defeito da secao 7. */
$composicao = array();
foreach ( $pecas_b['registros'] as $p ) {
	if ( 'kit' !== $p['tipo'] ) {
		continue;
	}
	$tem = false;
	foreach ( (array) $p['composicao'] as $i ) {
		if ( ! empty( $i['tipo'] ) ) {
			$tem = true;
		}
	}
	$composicao[ $p['id'] ] = $tem;
}
$kits_cegos = array();
foreach ( $fatos['vitrine'] as $v ) {
	if ( 'kit' === $v['tipo'] && empty( $composicao[ $v['peca'] ] ) ) {
		$kits_cegos[] = $v['peca'];
	}
}
rbm_ok( empty( $kits_cegos ),
	'nenhum kit de composicao nao transcrita na vitrine (secao 7)',
	empty( $kits_cegos ) ? 'nenhum' : implode( ' ', $kits_cegos ) );

rbm_ok( false !== strpos( $pagina, 'class="rbm-num"' ),
	'a pagina publica numero proprio, em monoespaçada tabular (identidade)' );

/* Todo numero do resumo que a pagina imprime tem que sair do arquivo de fatos.
   Conferimos os que aparecem no texto de abertura e na secao de cobertura. */
$texto_visivel = strip_tags( $retorno );
foreach ( array( 'pecas_publicaveis', 'pares_declarados', 'marcas',
	'celulas_total', 'celulas_sem_resposta' ) as $campo ) {
	rbm_ok( false !== strpos( $texto_visivel, number_format_i18n( $r[ $campo ] ) ),
		'o numero "' . $campo . '" dos fatos aparece na tela',
		number_format_i18n( $r[ $campo ] ) );
}

/* ---------------------------------------------------------------------------
 * 5. A ordem da secao 7: compra antes de procedencia.
 * ------------------------------------------------------------------------- */
echo "\n5. Ordem da secao 7 (porta de compra antes da prova de procedencia)\n";

$pos_compra = strpos( $retorno, 'rbm-compra' );
$pos_fonte  = strpos( $retorno, 'class="rbm-fonte"' );
$pos_vfonte = strpos( $retorno, 'rbm-vitrine-fonte' );
$primeira_procedencia = false;
foreach ( array( $pos_fonte, $pos_vfonte ) as $p ) {
	if ( false !== $p && ( false === $primeira_procedencia || $p < $primeira_procedencia ) ) {
		$primeira_procedencia = $p;
	}
}
rbm_ok( false !== $pos_compra && false !== $primeira_procedencia && $pos_compra < $primeira_procedencia,
	'o bloco de compra vem ANTES da primeira prova de procedencia',
	(int) $pos_compra . ' < ' . (int) $primeira_procedencia );

/* Em cada cartao, a acao de compra vem antes da fonte daquele cartao. */
preg_match_all( '#<li class="rbm-vitrine-item">(.*?)</li>#s', $retorno, $cartoes );
$fora_de_ordem = 0;
foreach ( $cartoes[1] as $c ) {
	$a = strpos( $c, 'rbm-vitrine-acao' );
	$f = strpos( $c, 'rbm-vitrine-fonte' );
	if ( false === $a || false === $f || $a > $f ) {
		$fora_de_ordem++;
	}
}
rbm_ok( count( $cartoes[1] ) > 0 && 0 === $fora_de_ordem,
	'em cada cartao, a acao de compra vem antes da fonte',
	count( $cartoes[1] ) . ' cartoes, ' . $fora_de_ordem . ' fora de ordem' );

/* O aviso de comissao mora DENTRO do bloco de compra, nao so no rodape. */
$bloco = substr( $retorno, (int) $pos_compra );
$bloco = substr( $bloco, 0, strpos( $bloco, '</ul></div>' ) );
rbm_ok( false !== strpos( $bloco, 'rbm-aviso-comissao' ),
	'o aviso de comissao esta dentro do bloco de compra (secao 7)' );

/* O lugar reservado existe para toda peca sem link — esconder o bloco enquanto o
   cano de links enche devolveria a procedencia ao papel de unica porta. */
$sem_link_na_tela = substr_count( $retorno, 'rbm-sem-loja' );
$sem_link_nos_fatos = 0;
foreach ( $fatos['vitrine'] as $v ) {
	if ( empty( $v['afiliado']['url'] ) ) {
		$sem_link_nos_fatos++;
	}
}
rbm_ok( $sem_link_na_tela === $sem_link_nos_fatos,
	'um lugar reservado por item sem link, nem a mais nem a menos',
	$sem_link_na_tela . ' de ' . count( $fatos['vitrine'] ) );

/* A procedencia e discreta por regra: texto "fonte", nunca rotulo de botao. */
if ( false !== $pos_fonte ) {
	preg_match( '#<a class="rbm-fonte"[^>]*>(.*?)</a>#s', $retorno, $mf );
	rbm_ok( isset( $mf[1] ) && 'fonte' === trim( $mf[1] ),
		'o link de procedencia tem o texto "fonte", e nunca um rotulo de botao',
		isset( $mf[1] ) ? trim( $mf[1] ) : '(nenhum)' );
} else {
	rbm_ok( false, 'o link de procedencia existe na pagina' );
}
rbm_ok( false === strpos( $retorno, 'class="rbm-fonte rbm-comprar"' )
	&& false === strpos( $retorno, 'class="rbm-comprar rbm-fonte"' ),
	'a fonte nunca acumula a classe do botao de compra' );

/* ---------------------------------------------------------------------------
 * 6. Links para fora: nofollow e noopener, sem excecao.
 * ------------------------------------------------------------------------- */
echo "\n6. Links para fora (secao 7)\n";

preg_match_all( '#<a\b[^>]*href="https?://(?!robometria\.com\.br)[^"]*"[^>]*>#i', $pagina, $externos );
$sem_nofollow = 0;
$sem_noopener = 0;
foreach ( $externos[0] as $a ) {
	if ( false === stripos( $a, 'nofollow' ) ) {
		$sem_nofollow++;
	}
	if ( false === stripos( $a, 'noopener' ) ) {
		$sem_noopener++;
	}
}
rbm_ok( count( $externos[0] ) > 0 && 0 === $sem_nofollow,
	'nenhum link para fora sem nofollow',
	count( $externos[0] ) . ' conferidos' );
rbm_ok( 0 === $sem_noopener,
	'e todo link para fora leva noopener',
	count( $externos[0] ) . ' conferidos' );

/* ---------------------------------------------------------------------------
 * 7. A MALHA (secao 9): duas listagens, tres irmas, mao dupla com a R1.
 * ------------------------------------------------------------------------- */
echo "\n7. Malha de paginas (secao 9)\n";

$irmas = array(
	'qual-peca-serve-no-meu-robo-aspirador' => 'a ferramenta que o artigo apoia',
	'metodologia'                           => 'a metodologia',
	'divulgacao-de-afiliados'               => 'a divulgacao de afiliados',
);
$faltando = array();
foreach ( $irmas as $slug => $nome ) {
	if ( false === strpos( $retorno, '/' . $slug . '/' ) ) {
		$faltando[] = $slug;
	}
}
rbm_ok( empty( $faltando ),
	'o artigo aponta para as 3 irmas exigidas pela regra da malha',
	empty( $faltando ) ? count( $irmas ) . ' irmas' : implode( ' ', $faltando ) );

/* MAO DUPLA: a R1 tem que apontar de volta. Sem isso o artigo e um beco. */
robometria_teste_rebobinar();
$GLOBALS['__options']['robometria_dados_r1-respostas'] =
	json_decode( file_get_contents( $raiz . '/dados/r1-respostas.json' ), true );
$pagina_r1 = robometria_teste_pagina( 'robometria_r1', 'Robometria — R1' );
rbm_ok( false !== strpos( $pagina_r1, '/filtro-universal-de-robo-aspirador/' ),
	'a R1 aponta de volta para o artigo — o link e de mao dupla' );

/* DUAS LISTAGENS: a home e o hub de ferramentas listam o artigo. Sem isso ele
   nasce orfao, e a seccao 9 nao admite pagina orfa. */
robometria_teste_rebobinar();
$home = robometria_teste_pagina( 'robometria_home', 'Robometria' );
robometria_teste_rebobinar();
$hub  = robometria_teste_pagina( 'robometria_ferramentas', 'Ferramentas' );

rbm_ok( false !== strpos( $home, '/filtro-universal-de-robo-aspirador/' ),
	'listagem 1: a home lista o artigo' );
rbm_ok( false !== strpos( $hub, '/filtro-universal-de-robo-aspirador/' ),
	'listagem 2: o hub de ferramentas lista o artigo' );

/* O artigo se registrou no catalogo da casca — e nao foi a casca que ganhou uma
   copia dele dentro. */
$catalogo = robometria_casca_artigos();
rbm_ok( 1 === count( $catalogo ) && 'A1' === $catalogo[0]['codigo'],
	'o artigo se registra pelo filtro, e a casca nao carrega copia dele',
	count( $catalogo ) . ' artigo(s) no catalogo' );

/* Apelido de endereco: quem digita "filtro universal" chega na pagina canonica. */
$apelidos = robometria_casca_apelidos();
rbm_ok( isset( $apelidos['filtro-hepa-universal'] )
	&& 'filtro-universal-de-robo-aspirador' === $apelidos['filtro-hepa-universal'],
	'a formulacao real da busca tem apelido 301 para a pagina canonica' );

/* ---------------------------------------------------------------------------
 * 8. JSON-LD e canonica (secoes 5.3 e 14.1).
 * ------------------------------------------------------------------------- */
echo "\n8. JSON-LD e canonica (secoes 5.3 e 14.1)\n";

preg_match( '#<script type="application/ld\+json" id="robometria-a1-jsonld">(.*?)</script>#s', $pagina, $mld );
$ld = isset( $mld[1] ) ? json_decode( $mld[1], true ) : null;
rbm_ok( is_array( $ld ) && isset( $ld['@graph'] ),
	'o JSON-LD do artigo decodifica' );

$tipos_ld = array();
if ( is_array( $ld ) ) {
	foreach ( (array) $ld['@graph'] as $no ) {
		$tipos_ld[] = $no['@type'];
	}
}
rbm_ok( in_array( 'Article', $tipos_ld, true ),
	'o JSON-LD traz Article', implode( '+', $tipos_ld ) );
rbm_ok( in_array( 'FAQPage', $tipos_ld, true ),
	'o JSON-LD traz FAQPage (secao 5.3)' );

/* Pergunta de FAQ que a pagina nao responde e marcacao que promete o que nao
   entrega: cada resposta do JSON-LD sai dos FATOS, e o numero dela tem que
   aparecer na tela. */
$faq = array();
foreach ( (array) $ld['@graph'] as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		$faq = $no['mainEntity'];
	}
}
rbm_ok( count( $faq ) === count( $fatos['perguntas'] ),
	'toda pergunta dos fatos virou pergunta do FAQPage',
	count( $faq ) . ' de ' . count( $fatos['perguntas'] ) );

$respostas_batem = true;
foreach ( $faq as $i => $q ) {
	if ( rbm_sem_acento( $q['acceptedAnswer']['text'] ) !== rbm_sem_acento( $fatos['perguntas'][ $i ]['resposta'] ) ) {
		$respostas_batem = false;
	}
}
rbm_ok( $respostas_batem,
	'nenhuma resposta do FAQPage foi reescrita a mao no snippet' );

rbm_ok( false !== strpos( $pagina, '<link rel="canonical" href="https://robometria.com.br/filtro-universal-de-robo-aspirador/">' ),
	'a canonica aponta para o endereco proprio do artigo' );

/* ---------------------------------------------------------------------------
 * 9. Identidade da ilha (secao 6 e PROMPT.md).
 * ------------------------------------------------------------------------- */
echo "\n9. Identidade (secao 6 e PROMPT.md)\n";

preg_match( '#<style id="robometria-a1">(.*?)</style>#s', $pagina, $mc );
$css = isset( $mc[1] ) ? $mc[1] : '';

rbm_ok( false === stripos( $css, 'gradient' ),
	'nenhum gradiente na folha do artigo (secao 6)' );
rbm_ok( false === stripos( $css, 'box-shadow' ),
	'nenhuma sombra na folha do artigo (secao 6)' );
rbm_ok( false === stripos( $retorno, '#CC3311' ),
	'a varredura nao aparece no corpo — ela e cor de sinal, e o uso da tela e o logotipo' );
rbm_ok( false !== strpos( $css, '.rbm-vitrine{' ),
	'a folha da vitrine veio da casca, e nao de uma copia local' );

/* A tabela de 5 colunas nao pode rolar a PAGINA (secao 6): ela rola dentro do
   envoltorio que a casca define. */
preg_match_all( '#<table[^>]*>#', $retorno, $tabelas );
$tabelas_soltas = 0;
foreach ( $tabelas[0] as $t ) {
	if ( false === strpos( $t, 'rbm-quadro' ) ) {
		$tabelas_soltas++;
	}
}
rbm_ok( count( $tabelas[0] ) > 0 && 0 === $tabelas_soltas,
	'toda tabela do artigo esta dentro do envoltorio que rola sozinho',
	count( $tabelas[0] ) . ' tabelas' );
rbm_ok( substr_count( $retorno, 'class="rbm-tabela"' ) === count( $tabelas[0] ),
	'um envoltorio por tabela, nem a mais nem a menos' );

rbm_ok( 0 !== strncmp( ltrim( $retorno ), '---', 3 ),
	'o corpo nao comeca por metadado YAML (secao 8, item 3)' );

/* ---------------------------------------------------------------------------
 * 10. Higiene do snippet (secao 8, fase 4b do playbook).
 * ------------------------------------------------------------------------- */
echo "\n10. Higiene do snippet (secao 8, fase 4b)\n";

$fonte = file_get_contents( $raiz . '/snippets/robometria-a1.php' );

rbm_ok( 0 === strncmp( $fonte, '/**', 3 ),
	'o snippet comeca com /** e sem <?php no topo' );
/* O nome da superglobal de servidor e casado pelo ModSecurity ate dentro de
   comentario, e a gravacao no wp-admin falha em silencio. */
rbm_ok( false === strpos( $fonte, '_SER' . 'VER' ),
	'nenhuma superglobal de servidor, nem dentro de comentario' );

preg_match_all( '#^function\s+([a-z0-9_]+)#mi', $fonte, $mf2 );
$desprotegidas = array();
foreach ( $mf2[1] as $nome ) {
	if ( false === strpos( $fonte, "function_exists( '" . $nome . "' )" ) ) {
		$desprotegidas[] = $nome;
	}
}
rbm_ok( empty( $desprotegidas ),
	'toda funcao de nivel superior dentro de function_exists',
	empty( $desprotegidas ) ? count( $mf2[1] ) . ' funcoes' : implode( ' ', $desprotegidas ) );

/* Os nomes de tipo do PHP e os do gerador tem que ser o mesmo texto, a menos de
   acento: se um lado ganhar um tipo que o outro nao tem, a tela publica rotulo
   cru do banco. */
$tipos_divergentes = array();
foreach ( $fatos['cobertura_por_tipo'] as $c ) {
	if ( rbm_sem_acento( robometria_a1_nome_do_tipo( $c['tipo'] ) ) !== $c['nome'] ) {
		$tipos_divergentes[] = $c['tipo'];
	}
}
rbm_ok( empty( $tipos_divergentes ),
	'os nomes de tipo do PHP batem com os do gerador, a menos de acento',
	empty( $tipos_divergentes ) ? count( $fatos['cobertura_por_tipo'] ) . ' tipos' : implode( ' ', $tipos_divergentes ) );

/* O artigo NAO repete a ferramenta: sem formulario, ele nao disputa a mesma
   consulta com a R1 no indice (secao 14.4). */
rbm_ok( false === stripos( $retorno, '<form' ),
	'o artigo nao tem formulario — a consulta e da ferramenta, nao dele' );

echo "\n";
if ( $falhas ) {
	printf( "REPROVADO: %d de %d verificacoes falharam.\n", $falhas, $feitos );
	exit( 1 );
}
printf( "APROVADO: %d verificacoes, nenhuma falha.\n", $feitos );

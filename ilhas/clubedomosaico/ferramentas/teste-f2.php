<?php
/**
 * Verificacao MEDIDA da F2 — "Qual cola usar no mosaico, e qual rejunte".
 *
 *   php ferramentas/teste-f2.php .
 *
 * O que este arquivo tem que os outros nao tem, e por que:
 *
 *   1. ELE VARRE A ENTRADA INTEIRA, nao o caso-ancora. A F2 e ferramenta de
 *      entrada variavel: ela serve uma pagina por consulta, e a pagina sem
 *      consulta e so UM dos 45 estados de cola e dos 50 de rejunte. A
 *      Robometria pagou essa licao em 11/09/2026 com cinco testes verdes que
 *      nao viam portugues errado porque ele so aparecia quando alguem escolhia
 *      um modelo especifico. Aqui a afirmacao e sobre a SOMA das respostas.
 *
 *   2. A REGUA E PROPRIA, e ela NAO chama o snippet. O esperado de cada celula
 *      vem de `matriz_esperada_da_F2` e `matriz_esperada_do_rejunte` do
 *      esquema, escritos A MAO no bloco 3 a partir das declaracoes, antes de
 *      existir uma linha do snippet. Se as duas metades errarem, elas nao
 *      erram juntas.
 *
 *   3. ELE MEDE NO CORPO SERVIDO, nunca no HTML completo nem no retorno do
 *      shortcode. Afirmacao sobre o que a pagina DIZ se conta dentro de <main>.
 *
 *   4. UM PROCESSO POR ESTADO. A casca tem `static` legitimos (rodape, marca,
 *      trilha) que so valem dentro de uma requisicao; varredura que monta
 *      muitos estados no mesmo processo mede o segundo pela metade.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$rapido = in_array( '--rapido', $argv, true );

$falhas = 0;
$feitos = 0;

function f2_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-70s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-70s %s\n", $rotulo, $medida );
	return false;
}

function f2_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function f2_scripts( $html ) {
	preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $m );
	return implode( "\n", $m[1] );
}

/**
 * O TRECHO DE TEXTO QUE COMECA EM UMA FRASE E TERMINA NA PROXIMA FRONTEIRA.
 * Existe porque delimitar bloco por `</div>` nao funciona onde ha aninhamento,
 * e porque a afirmacao que importa aqui e sobre o que a pagina DIZ.
 */
function f2_recorte( $texto, $inicio, $fronteiras ) {
	$i = mb_strpos( $texto, $inicio );
	if ( false === $i ) {
		return '';
	}
	$resto = mb_substr( $texto, $i );
	$fim   = mb_strlen( $resto );
	foreach ( (array) $fronteiras as $f ) {
		$j = mb_strpos( $resto, $f, mb_strlen( $inicio ) );
		if ( false !== $j && $j < $fim ) {
			$fim = $j;
		}
	}
	return mb_substr( $resto, 0, $fim );
}

function f2_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/** Um estado da ferramenta, servido por um processo so dele. */
function f2_render( $raiz, $consulta = '' ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( 'cdm_f2' ) . ' ' . escapeshellarg( 'hoje' )
		. ' ' . escapeshellarg( $consulta ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/* ---------------------------------------------------------------------------
 * A REGUA, lida do repositorio e nunca do snippet.
 * ------------------------------------------------------------------------- */

$esquema  = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$colas    = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$rejuntes = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-rejuntes.json' ), true );

if ( ! $esquema || ! $colas || ! $rejuntes ) {
	echo "ERRO: nao consegui ler o esquema ou o banco.\n";
	exit( 1 );
}

$por_id = array();
foreach ( array_merge( $colas['materiais'], $rejuntes['materiais'] ) as $m ) {
	$por_id[ $m['id'] ] = $m;
}

/** O nome como a TELA o escreve, recalculado aqui: marca so quando falta. */
function f2_nome_esperado( $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return $nome;
	}

	return $marca . ' ' . $nome;
}

/**
 * Uma COPIA do repositorio com um rejunte a mais: clone do registro declarado
 * para pastilha de vidro submersa, com as duas pontas da faixa de junta em
 * null. Serve ao portao da faixa nao obtida, que antes dependia de o banco
 * real ter essa lacuna (ver o comentario do portao, mais abaixo).
 *
 * So `manifest.json`, `snippets/` e `dados/` sao copiados, porque e tudo o que
 * `render-para-teste.php` le da raiz. A copia morre com o processo.
 */
function f2_raiz_com_rejunte_sem_faixa( $raiz ) {
	static $destino = null;
	if ( null !== $destino ) {
		return $destino;
	}

	$destino = rtrim( sys_get_temp_dir(), '/' ) . '/cdm-f2-sem-faixa-' . getmypid();
	if ( ! is_dir( $destino ) && ! mkdir( $destino, 0700, true ) ) {
		fwrite( STDERR, "nao consegui criar a raiz sintetica em $destino\n" );
		exit( 2 );
	}
	foreach ( array( 'snippets', 'dados' ) as $pasta ) {
		if ( ! is_dir( $destino . '/' . $pasta ) ) {
			mkdir( $destino . '/' . $pasta, 0700, true );
		}
		foreach ( (array) glob( $raiz . '/' . $pasta . '/*' ) as $arquivo ) {
			if ( is_file( $arquivo ) ) {
				copy( $arquivo, $destino . '/' . $pasta . '/' . basename( $arquivo ) );
			}
		}
	}
	copy( $raiz . '/manifest.json', $destino . '/manifest.json' );

	$banco = json_decode( (string) file_get_contents( $destino . '/dados/materiais-rejuntes.json' ), true );
	$molde = null;
	foreach ( $banco['materiais'] as $m ) {
		if ( 'quartzolit-rejunte-piscinas' === $m['id'] ) {
			$molde = $m;
		}
	}
	if ( null === $molde ) {
		/* O clone tem molde NOMEADO de proposito: molde escolhido por posicao
		   mudaria de produto sem ninguem ver, e o portao passaria a medir outra
		   coisa calado. Sem o molde, o portao nao existe. */
		fwrite( STDERR, "o molde quartzolit-rejunte-piscinas saiu do banco: o portao da faixa nao obtida perdeu o chao\n" );
		exit( 2 );
	}

	$clone                                      = $molde;
	$clone['id']                                = 'bancada-rejunte-sem-faixa';
	$clone['nome_comercial']                    = 'Rejunte de Bancada Sem Faixa Declarada';
	$clone['marca']                             = 'Bancada';
	$clone['propriedades']['junta_min_mm']      = array(
		'valor'  => null,
		'unidade' => 'mm',
		'motivo' => 'NAO obtida — registro sintetizado por ferramentas/teste-f2.php, nunca vai ao ar.',
	);
	$clone['propriedades']['junta_max_mm']      = $clone['propriedades']['junta_min_mm'];
	$banco['materiais'][]                       = $clone;
	file_put_contents( $destino . '/dados/materiais-rejuntes.json',
		json_encode( $banco, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT ) );

	return $destino;
}

echo "Clube do Mosaico — verificacao da F2 " . ( defined( 'CDM_F2_VERSAO' ) ? CDM_F2_VERSAO : '?' ) . "\n";

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "  (F2 " . CDM_F2_VERSAO . ", casca " . CDM_CASCA_VERSAO . ")\n\n";

/* ---------------------------------------------------------------------------
 * 1. A pagina existe na arvore, com mae, e com UM nome so
 * ------------------------------------------------------------------------- */

echo "1. A pagina na arvore (secao 16 do contrato)\n";

$defs = cdm_casca_definicao_paginas();
f2_ok( isset( $defs[ CDM_F2_SLUG ] ), 'a F2 registrou a propria pagina pelo filtro cdm_paginas', CDM_F2_SLUG );
f2_ok( isset( $defs[ CDM_F2_SLUG ]['pai'] ) && 'materiais' === $defs[ CDM_F2_SLUG ]['pai'],
	'a pagina nasce com mae, e a mae e /materiais/' );
f2_ok( isset( $defs['materiais'] ), 'a mae existe na definicao de paginas' );

/* UM NOME POR PAGINA, em toda superficie. A Aquametria pagou por oito paginas
   em que o degrau da trilha e o H1 diziam nomes diferentes a uma linha de
   distancia. Aqui as quatro superficies sao conferidas contra a MESMA
   constante, e o teste le cada uma de onde ela realmente sai. */
$arvore = cdm_casca_arvore();
f2_ok( isset( $arvore[ CDM_F2_SLUG ] ), 'a pagina esta no mapa da arvore' );
f2_ok( isset( $arvore[ CDM_F2_SLUG ]['rotulo'] ) && CDM_F2_TITULO === $arvore[ CDM_F2_SLUG ]['rotulo'],
	'o degrau da trilha usa o mesmo nome', isset( $arvore[ CDM_F2_SLUG ] ) ? $arvore[ CDM_F2_SLUG ]['rotulo'] : '' );
f2_ok( CDM_F2_TITULO === $defs[ CDM_F2_SLUG ]['titulo'], 'o titulo da pagina usa o mesmo nome' );
$no_cartao = '';
foreach ( cdm_casca_ferramentas() as $f ) {
	if ( 'F2' === $f['codigo'] ) {
		$no_cartao = $f['titulo'];
		f2_ok( 'publicada' === $f['estado'], 'a F2 se declara publicada no registro de ferramentas' );
		f2_ok( CDM_F2_SLUG === $f['slug'], 'o registro aponta para o endereco de nivel 3', $f['slug'] );
	}
}
f2_ok( CDM_F2_TITULO === $no_cartao, 'o cartao da home e do Guia usa o mesmo nome' );

/* O <title> do tema e "<titulo> – <nome do site>". 65 e o teto que a Aquametria
   passou a cobrar em 11/09/2026 depois de servir um de 128 caracteres. */
$titulo_completo = CDM_F2_TITULO . ' – Clube do Mosaico';
f2_ok( mb_strlen( $titulo_completo ) <= 65, 'o <title> cabe em 65 caracteres',
	mb_strlen( $titulo_completo ) . ' caracteres' );

/* ---------------------------------------------------------------------------
 * 2. A pagina-ancora: o que existe quando ninguem preenche nada
 * ------------------------------------------------------------------------- */

echo "\n2. A pagina-ancora (secao 5: o que um modelo de linguagem le)\n";

$ancora = f2_render( $raiz );
f2_ok( '' !== $ancora, 'a ancora foi servida', strlen( $ancora ) . ' bytes' );
$corpo_ancora = f2_corpo( $ancora );
$texto_ancora = f2_texto( $corpo_ancora );

/* Pagina fina nao entra no indice de dominio novo (secao 8). */
f2_ok( mb_strlen( $texto_ancora ) >= 1500, 'o corpo tem tamanho de pagina de verdade',
	mb_strlen( $texto_ancora ) . ' caracteres' );

cdm_teste_rebobinar();
cdm_teste_pagina( 'cdm_f2' );
$cru = $GLOBALS['__retorno_shortcode'];
f2_ok( false === stripos( $cru, '<script' ), 'sem <script> no retorno do shortcode (cicatriz de 08/09/2026)' );
f2_ok( false === stripos( $cru, '<style' ), 'sem <style> no retorno do shortcode' );
f2_ok( 0 === substr_count( f2_scripts( $ancora ), '&#038;' ), 'zero &#038; DENTRO de <script>',
	substr_count( f2_scripts( $ancora ), '&#038;' ) . ' achados' );
f2_ok( 0 !== strncmp( ltrim( $texto_ancora ), '---', 3 ), 'o corpo nao comeca por metadado' );

/* A folha e o script vem do rodape, nao da cabeca nem do corpo. */
$pos_corpo  = mb_strpos( $ancora, '<main' );
$pos_css    = mb_strpos( $ancora, 'id="cdm-f2-css"' );
$pos_js     = mb_strpos( $ancora, 'id="cdm-f2-js"' );
f2_ok( false !== $pos_css && $pos_css > $pos_corpo, 'a folha da F2 sai depois do corpo (wp_footer)' );
f2_ok( false !== $pos_js && $pos_js > $pos_corpo, 'o script da F2 sai depois do corpo (wp_footer)' );

/* A tabela pre-renderizada: as linhas de cola e as de rejunte, no HTML servido.
   Quantas sao NAO se digita aqui — sai do esquema, logo abaixo. A cola foi de 18
   para 45 em 13/09/2026 e este portao acompanhou sozinho, que e o que ele existe
   para fazer. */
$linhas_tabela = preg_match_all( '#<table class="cdm-f2-tabela">.*?</table>#is', $corpo_ancora, $mt );
f2_ok( 2 === $linhas_tabela, 'as duas tabelas pre-renderizadas estao no HTML servido', $linhas_tabela . ' tabelas' );
$esperadas_cola    = count( $esquema['matriz_esperada_da_F2']['celulas'] );
$esperadas_rejunte = count( $esquema['matriz_esperada_do_rejunte']['celulas'] );
if ( 2 === $linhas_tabela ) {
	$n1 = preg_match_all( '#<tr>#', $mt[0][0] ) - 1; // o <tr> do cabecalho
	$n2 = preg_match_all( '#<tr>#', $mt[0][1] ) - 1;
	f2_ok( $n1 === $esperadas_cola, 'a tabela de cola serve as ' . $esperadas_cola . ' celulas conferidas', $n1 . ' linhas' );
	f2_ok( $n2 === $esperadas_rejunte, 'a tabela de rejunte serve as ' . $esperadas_rejunte . ' celulas conferidas', $n2 . ' linhas' );
}

/* Trilha e mae: a 16.4(b) cobra a mae no breadcrumb E numa frase do corpo. */
f2_ok( (bool) preg_match( '#<nav class="cdm-trilha".*?>Materiais<#is', $corpo_ancora ),
	'a trilha mostra a mae com endereco de verdade' );
$sem_trilha = preg_replace( '#<nav class="cdm-trilha".*?</nav>#is', '', $corpo_ancora );
f2_ok( false !== strpos( $sem_trilha, 'href="https://clubedomosaico.com.br/materiais/"' ),
	'o corpo tem uma frase que linka a mae (16.4b)' );

/* ---------------------------------------------------------------------------
 * 3. Cabeca: description, canonical e o robo do estado com parametro
 * ------------------------------------------------------------------------- */

echo "\n3. Cabeca da pagina (secoes 14.1 e 14.4)\n";

preg_match( '#<meta name="description" content="([^"]*)"#', $ancora, $md );
$desc = isset( $md[1] ) ? html_entity_decode( $md[1], ENT_QUOTES, 'UTF-8' ) : '';
f2_ok( '' !== $desc, 'a pagina serve meta description' );
/* A FAIXA E 120 A 160 desde 02/10/2026, e nao 200: e a faixa do item 4 do
   despacho de 28/09, que esta pagina so pode cumprir depois de a janela de
   medicao de 30/09 fechar. O teto de 200 daqui deixava passar os 183 caracteres
   que ela servia. O texto COM OS NUMEROS e conferido contra a regua
   independente na secao 6b deste arquivo, onde os numeros existem contados. */
f2_ok( mb_strlen( $desc ) >= 120 && mb_strlen( $desc ) <= 160, 'a description cabe na faixa de 120 a 160',
	mb_strlen( $desc ) . ' caracteres' );
f2_ok( false === strpos( $desc, '{' ), 'e ela nunca serve o molde cru' );
/* UM canonical, e ele aponta para o endereco limpo. O "um" nao e zelo: quem
   imprime o proprio canonical por cima do `rel_canonical()` do nucleo serve
   dois, e a bancada so consegue ver isso porque passou a servir o do nucleo
   tambem (render-para-teste.php). */
f2_ok( 1 === substr_count( $ancora, '<link rel="canonical"' ), 'a ancora serve UM canonical',
	substr_count( $ancora, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $ancora, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'canonical aponta para o endereco limpo' );
/* A ETIQUETA DE ROBO GANHOU A MESMA CONTAGEM QUE O CANONICAL JA TINHA, e a
   assimetria durou ate 25/09/2026. As duas linhas acima contam `<link
   rel="canonical"` e cobram UM; a de robo procurava a frase `name="robots"` com
   ASPAS DUPLAS — as do `echo` que este snippet fazia — e por isso passava a
   vazio no dia em que quem imprime virou o `wp_robots()` do nucleo, que usa
   aspas simples. Pior: era exatamente a linha que teria pegado o defeito medido
   no ar naquele dia, DUAS etiquetas no estado com parametro desta pagina. */
$re_robots = '#<meta[^>]*name=[\'"]robots[\'"][^>]*>#i';
preg_match_all( $re_robots, $ancora, $m_ancora );
f2_ok( 1 === count( $m_ancora[0] ), 'a ancora serve UMA etiqueta de robo',
	count( $m_ancora[0] ) . ' tags' );
f2_ok( 1 === count( $m_ancora[0] ) && false === stripos( $m_ancora[0][0], 'noindex' ),
	'a ancora NAO sai com noindex', $m_ancora[0] ? $m_ancora[0][0] : '(nenhuma)' );

$com_parametro = f2_render( $raiz, 'base=espelho&onde=externo_exposto&junta=3' );
preg_match_all( $re_robots, $com_parametro, $m_param );
f2_ok( 1 === count( $m_param[0] ), 'o estado com parametro serve UMA etiqueta de robo',
	count( $m_param[0] ) . ' tags' );
f2_ok( 1 === count( $m_param[0] ) && false !== stripos( $m_param[0][0], 'noindex' ),
	'o estado com parametro sai com noindex, follow', $m_param[0] ? $m_param[0][0] : '(nenhuma)' );
f2_ok( 1 === substr_count( $com_parametro, '<link rel="canonical"' ), 'o estado com parametro serve UM canonical',
	substr_count( $com_parametro, '<link rel="canonical"' ) . ' tags' );
f2_ok( false !== strpos( $com_parametro, '<link rel="canonical" href="https://clubedomosaico.com.br/' . CDM_F2_SLUG . '/">' ),
	'o estado com parametro aponta o canonical para a ancora' );

/* OS TRES ESTADOS QUE A RONDA DE 28/09/2026 MEDIU NO AR E ACHOU NO INDICE, e
   eles estao escritos LITERAIS aqui, copiados do despacho — nao derivados do
   vocabulario. E deliberado: o defeito era exatamente ter valor FORA do
   vocabulario, entao uma regua que montasse as consultas a partir do
   vocabulario nunca reproduziria o estado que falhou.
      Os nomes dos quatro parametros sao reais; nenhum dos valores existe aqui —
   as chaves sao `ceramica_esmaltada_porcelana`, `externo_exposto`,
   `mdf_madeira`, `caco_louca`, e `junta` e numero. Ate 28/09 o `noindex` desta
   pagina saia do `escolheu`, que pergunta pelo VALOR, e os tres entravam no
   indice como tres enderecos servindo o HTML da ancora. */
$estados_invalidos = array(
	'base=ceramica&onde=externo',
	'base=mdf',
	'base=ceramica&caco=louca&junta=fina&onde=interno',
);
$sem_noindex_invalido = array();
$escolheu_invalido    = array();
foreach ( $estados_invalidos as $consulta ) {
	$html = f2_render( $raiz, $consulta );
	preg_match_all( $re_robots, $html, $m_inv );
	if ( 1 !== count( $m_inv[0] ) || false === stripos( $m_inv[0][0], 'noindex' ) ) {
		$sem_noindex_invalido[] = $consulta . ' -> ' . ( $m_inv[0] ? $m_inv[0][0] : '(nenhuma)' );
	}
	parse_str( $consulta, $q );
	if ( ! cdm_f2_tem_parametro( $q ) ) {
		$sem_noindex_invalido[] = $consulta . ' -> cdm_f2_tem_parametro() disse nao';
	}
}
f2_ok( empty( $sem_noindex_invalido ),
	'os tres estados de 28/09, com VALOR invalido, saem do indice numa etiqueta so',
	empty( $sem_noindex_invalido ) ? count( $estados_invalidos ) . ' estados' : implode( ' | ', $sem_noindex_invalido ) );

/* O OUTRO LADO DA SEPARACAO, e e ele que impede o conserto de virar mentira na
   tela: `escolheu` continua medindo o VALOR. Valor fora do vocabulario volta ao
   padrao em silencio e a pagina que sai e a ancora — dizer "voce escolheu"
   sobre uma escolha que a pagina nao honrou seria trocar um defeito de indice
   por um defeito de texto. */
foreach ( $estados_invalidos as $consulta ) {
	parse_str( $consulta, $q );
	$_GET = $q;
	$e    = cdm_f2_entrada();
	if ( ! empty( $e['escolheu'] ) ) {
		$escolheu_invalido[] = $consulta;
	}
}
$_GET = array();
f2_ok( empty( $escolheu_invalido ),
	'e `escolheu` continua FALSO neles: o `noindex` mede endereco, a tela mede escolha',
	empty( $escolheu_invalido ) ? 'os tres' : implode( ' | ', $escolheu_invalido ) );

/* A LISTA DE PARAMETROS E A DO FORMULARIO, nao uma copia. Se alguem acrescentar
   uma pergunta a `cdm_f2_entrada()` e esquecer `cdm_f2_parametros()`, o estado
   novo entra no indice calado — e foi calado que os tres de cima entraram. */
$parametros_f2 = cdm_f2_parametros();
sort( $parametros_f2 );
f2_ok( array( 'base', 'caco', 'junta', 'onde' ) === $parametros_f2,
	'os quatro parametros desta ferramenta estao declarados', implode( ', ', $parametros_f2 ) );
f2_ok( ! cdm_f2_tem_parametro( array() ) && ! cdm_f2_tem_parametro( array( 'utm_source' => 'x' ) ),
	'query vazia e query de terceiro NAO tiram a ancora do indice (o lado caro da borda)' );
f2_ok( cdm_f2_tem_parametro( array( 'base' => '' ) ),
	'parametro presente e VAZIO ja e um endereco a mais: `?base=` sai do indice' );

/* JSON-LD: WebApplication + FAQPage, e o FAQ do schema tem que ser o mesmo que
   a pagina MOSTRA. Schema que promete o que a pagina nao diz e schema ignorado
   na melhor das hipoteses. */
preg_match( '#<script type="application/ld\+json" id="cdm-f2-jsonld">(.*?)</script>#s', $ancora, $mj );
$jsonld = isset( $mj[1] ) ? json_decode( $mj[1], true ) : null;
f2_ok( is_array( $jsonld ), 'o JSON-LD da F2 e JSON valido' );
$tipos = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	$tipos[] = $no['@type'];
}
f2_ok( in_array( 'WebApplication', $tipos, true ), 'JSON-LD tem WebApplication (secao 5.3)' );
f2_ok( in_array( 'FAQPage', $tipos, true ), 'JSON-LD tem FAQPage' );
f2_ok( false !== strpos( $ancora, 'id="cdm-trilha-jsonld"' ), 'JSON-LD tem BreadcrumbList (16.3)' );

$perguntas_schema = array();
foreach ( ( isset( $jsonld['@graph'] ) ? $jsonld['@graph'] : array() ) as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		foreach ( $no['mainEntity'] as $q ) {
			$perguntas_schema[] = $q['name'];
		}
	}
}
$fora_da_tela = array();
foreach ( $perguntas_schema as $p ) {
	if ( false === mb_strpos( f2_texto( $corpo_ancora ), $p ) ) {
		$fora_da_tela[] = $p;
	}
}
f2_ok( count( $perguntas_schema ) >= 4, 'o FAQPage tem perguntas', count( $perguntas_schema ) . ' perguntas' );
f2_ok( empty( $fora_da_tela ), 'toda pergunta do schema esta escrita na tela',
	empty( $fora_da_tela ) ? 'as ' . count( $perguntas_schema ) : implode( ' | ', $fora_da_tela ) );

/* ---------------------------------------------------------------------------
 * 4. A VARREDURA DA COLA — 45 estados, um processo cada
 * ------------------------------------------------------------------------- */

echo "\n4. A entrada inteira da cola: " . count( $esquema['vocabularios']['base'] ) . " bases x "
	. count( $esquema['vocabularios']['ambiente'] ) . " ambientes\n";

$bases     = $esquema['vocabularios']['base'];
$ambientes = $esquema['vocabularios']['ambiente'];

/* Os rotulos existem para TODA entrada do vocabulario, e nao existe rotulo sem
   entrada. As duas direcoes, porque vocabulario novo sem rotulo sairia na tela
   como chave crua e rotulo orfao e codigo morto que finge cobertura. */
$rot = cdm_f2_rotulos();
$sem_rotulo = array_diff( $bases, array_keys( $rot['base'] ) );
$rotulo_orfao = array_diff( array_keys( $rot['base'] ), $bases );
f2_ok( empty( $sem_rotulo ), 'toda base do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo ) );
f2_ok( empty( $rotulo_orfao ), 'nenhum rotulo de base sem entrada no vocabulario', implode( ', ', $rotulo_orfao ) );
$sem_rotulo_a = array_diff( $ambientes, array_keys( $rot['ambiente'] ) );
f2_ok( empty( $sem_rotulo_a ), 'todo ambiente do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_a ) );
$sem_rotulo_t = array_diff( $esquema['vocabularios']['material_tessela'], array_keys( $rot['tessela'] ) );
f2_ok( empty( $sem_rotulo_t ), 'toda tessela do vocabulario tem rotulo na tela', implode( ', ', $sem_rotulo_t ) );

$estados       = 0;
$finas         = array();
$sem_acento    = array();
$incoerentes   = array();
$corpos        = array();

/**
 * Portugues errado que chega a tela. Mede o CORPO, palavra a palavra, contra
 * uma lista de formas que so existem sem acento por erro de digitacao — foi
 * assim que o bloco 4 achou "Silicone Acetico Construcao" servido ao visitante.
 */
$formas_erradas = array(
	'acetico', 'ceramica', 'ceramicas', 'construcao', 'acrilico', 'epoxi', 'plastico',
	'aluminio', 'superficies', 'calcario', 'aquarios', 'corrosivel', 'imersao',
	'liquido', 'area', 'areas', 'agua', 'pagina', 'tecnica', 'tecnico', 'nao',
	'sao', 'liberacao', 'variacao', 'condicao', 'marmore', 'latao', 'papelao',
);

foreach ( $bases as $base ) {
	foreach ( $ambientes as $ambiente ) {
		$html  = f2_render( $raiz, 'base=' . $base . '&onde=' . $ambiente );
		$corpo = f2_corpo( $html );
		$texto = f2_texto( $corpo );
		$corpos[ $base . '|' . $ambiente ] = $corpo;
		$estados++;

		if ( mb_strlen( $texto ) < 1500 ) {
			$finas[] = $base . ' x ' . $ambiente . ' (' . mb_strlen( $texto ) . ')';
		}
		$minusculo = mb_strtolower( $texto, 'UTF-8' );
		foreach ( $formas_erradas as $forma ) {
			if ( preg_match( '/(?<![\p{L}])' . $forma . '(?![\p{L}])/u', $minusculo ) ) {
				$sem_acento[] = $base . ' x ' . $ambiente . ': "' . $forma . '"';
				break;
			}
		}
	}
}
f2_ok( 45 === $estados, 'os 45 estados de cola foram servidos, um processo cada', $estados . ' estados' );
f2_ok( empty( $finas ), 'nenhum estado serve pagina fina', empty( $finas ) ? 'todos acima de 1500' : implode( ' | ', array_slice( $finas, 0, 4 ) ) );
f2_ok( empty( $sem_acento ), 'nenhum estado serve portugues sem acento',
	empty( $sem_acento ) ? '45 estados limpos' : implode( ' | ', array_slice( $sem_acento, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 5. AS 18 CELULAS CONFERIDAS — a regua escrita a mao contra o que a tela diz
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * A REGUA DA REGRA 6, escrita AQUI.
 *
 * Ela le `superficies_porosas` do esquema e `condicoes` do banco, e nao chama
 * uma linha do snippet. E a trava da secao 8: duas metades que erram juntas
 * ficam verdes. A varredura acima serve os 45 estados SEM escolher caquinho, e
 * o padrao da ferramenta e pastilha de vidro — que NAO e porosa. Entao a
 * matriz escrita a mao no esquema, que e a camada de DECLARACAO, nao pode ser
 * comparada crua com o que a tela serve: quem carrega condicao cai antes de
 * chegar la, e e esta funcao que diz quem.
 * ------------------------------------------------------------------------- */

$porosas_base    = array_flip( $esquema['superficies_porosas']['bases_porosas'] );
$porosas_tessela = array_flip( $esquema['superficies_porosas']['tesselas_porosas'] );

/** Os elegiveis da camada de declaracao, lidos da matriz escrita a mao. */
function f2_elegiveis_da_matriz( $esquema, $base, $ambiente ) {
	static $cache = array();
	$chave = $base . '|' . $ambiente;
	if ( isset( $cache[ $chave ] ) ) {
		return $cache[ $chave ];
	}
	$cache[ $chave ] = array();
	foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
		if ( $c['base'] === $base && $c['ambiente'] === $ambiente ) {
			$cache[ $chave ] = array_merge(
				isset( $c['recomendados_topo'] ) ? $c['recomendados_topo'] : array(),
				isset( $c['elegiveis_abaixo_do_topo'] ) ? $c['elegiveis_abaixo_do_topo'] : array() );
		}
	}

	return $cache[ $chave ];
}

function f2_exige_porosa_no_banco( $m ) {
	return ! empty( $m['condicoes']['exige_superficie_porosa']['valor'] );
}

function f2_condicao_falha( $m, $base, $tessela ) {
	global $porosas_base, $porosas_tessela;
	if ( ! f2_exige_porosa_no_banco( $m ) ) {
		return false;
	}

	return ! isset( $porosas_base[ $base ] ) && ! isset( $porosas_tessela[ $tessela ] );
}

/* O caquinho que a varredura dos 45 estados realmente serviu. Lido da entrada
   saneada da propria ferramenta e nao digitado aqui: se um dia o padrao mudar,
   este portao acompanha em vez de medir um estado que ninguem ve. */
$entrada_padrao = cdm_f2_entrada();
$tessela_varrida = $entrada_padrao['tessela'];
f2_ok( isset( $rot['tessela'][ $tessela_varrida ] ),
	'o caquinho padrao da varredura e um do vocabulario', $tessela_varrida );

echo "\n5. As " . $esperadas_cola . " celulas de cola, contra a matriz escrita a mao no bloco 3\n";

$erros_celula = array();
$graves       = array();

foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
	$chave = $c['base'] . '|' . $c['ambiente'];
	$corpo = isset( $corpos[ $chave ] ) ? $corpos[ $chave ] : '';
	if ( '' === $corpo ) {
		$erros_celula[] = $chave . ': nao foi servida';
		continue;
	}

	/* A FRASE-RESPOSTA e a vitrine sao onde o recomendado aparece. A secao de
	   eliminados fica FORA desta medida de proposito: o nome de um produto
	   proibido aparece la, e contar na pagina inteira encontraria os dois. */
	$pedaco_html = '';
	if ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>\s*<div class="cdm-f2-secao">\s*<h2>Onde comprar</h2>(.*?)(?=<div class="cdm-f2-secao">)#is', $corpo, $mp ) ) {
		$pedaco_html = $mp[1] . $mp[2];
	} elseif ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>#is', $corpo, $mp ) ) {
		$pedaco_html = $mp[1];
	}
	$pedaco = f2_texto( $pedaco_html );
	$fora_html = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo, $mf ) ? $mf[1] : '';
	$fora      = f2_texto( $fora_html );

	/* O BLOCO DE RECUSA SAI DO PEDACO ANTES DE QUALQUER AFIRMACAO SOBRE QUEM
	   ESTA RECOMENDADO — e isto e a quarta trava da secao 8 do ARQUIPELAGO.md
	   aplicada de novo, agora contra um texto que esta execucao mesma escreveu.
	   A recusa da regra 6 NOMEIA o produto ("o Cascola PL500 e declarado para
	   plastico, mas exige uma condicao..."), porque a secao 7 manda nomear a
	   causa medida. A regua antiga media presenca de palavra dentro da regiao da
	   resposta e leu esse nome como recomendacao: acusou de GRAVE uma pagina que
	   estava dizendo exatamente a verdade. A saida nao e heuristica melhor (
	   procurar "mas exige" perto do nome seria adivinhar pela vizinhanca): e a
	   pagina MARCAR a recusa no markup, que ela ja faz com `cdm-f2-faixa`, e o
	   teste retirar o marcado e proibir o nome em todo o resto.

	   E para a declaracao nao virar porta dos fundos — bastaria embrulhar a
	   vitrine inteira na classe de recusa —, o bloco marcado tem de ABRIR
	   negando, e eles sao CONTADOS: no maximo um por resposta de cola. */
	$blocos_recusa = array();
	if ( preg_match_all( '#<p class="cdm-f2-frase cdm-f2-faixa">(.*?)</p>#is', $pedaco_html, $mr ) ) {
		$blocos_recusa = $mr[1];
	}
	foreach ( $blocos_recusa as $bloco ) {
		$t_bloco = f2_texto( $bloco );
		if ( 0 !== mb_strpos( $t_bloco, 'Não' ) ) {
			$graves[] = $chave . ': bloco marcado como recusa que nao ABRE negando — "'
				. mb_substr( $t_bloco, 0, 40 ) . '"';
		}
	}
	if ( count( $blocos_recusa ) > 1 ) {
		$graves[] = $chave . ': ' . count( $blocos_recusa ) . ' blocos de recusa numa resposta so';
	}
	$pedaco = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '', $pedaco_html ) );

	/* A MATRIZ DO ESQUEMA E A CAMADA DE DECLARACAO; a tela e ela MENOS a regra 7 e
	   MENOS a regra 6, nessa ordem. Quem carrega condicao e nao a cumpre neste par
	   de superficies, ou carrega proibicao de peca que morde este caquinho, sai da
	   recomendacao e tem de aparecer no grupo proprio — e as duas metades sao
	   cobradas, porque so cobrar a primeira deixaria o produto sumir da pagina
	   inteira sem ninguem ver.
	   A REGRA 7 ENTROU AQUI EM 06/10/2026, e ela faltava desde que nasceu, de
	   manha: esta secao descontava so a regra 6 porque nenhum produto com
	   proibicao de peca era elegivel em celula nenhuma — o acetico sai por
	   proibicao de BASE onde a peca tambem o pegaria. No dia em que a REGRA 8 fez
	   a cimentcola virar recomendavel em cinco celulas, as quatro de cimento
	   falharam de uma vez, cada uma acusando que a tela nao recomendava quem a
	   matriz manda. A matriz estava certa e a tela estava certa: era a regua que
	   media a camada errada. */
	$caidos_pela_condicao = array();
	$caidos_pela_peca     = array();
	$grupos_do_esquema    = isset( $esquema['grupos_de_tessela_proibidos']['grupos'] )
		? $esquema['grupos_de_tessela_proibidos']['grupos'] : array();
	$elegiveis_da_celula  = array_merge(
		isset( $c['recomendados_topo'] ) ? $c['recomendados_topo'] : array(),
		isset( $c['elegiveis_abaixo_do_topo'] ) ? $c['elegiveis_abaixo_do_topo'] : array() );
	foreach ( $elegiveis_da_celula as $id ) {
		/* A ORDEM E A DO ESQUEMA: a 7 ANTES da 6, porque proibicao e afirmacao
		   mais forte que condicao nao cumprida. Quem cai nas duas sai pela 7. */
		if ( f2_peca_proibida_no_banco( $por_id[ $id ], $tessela_varrida, $grupos_do_esquema ) ) {
			$caidos_pela_peca[] = $id;
		} elseif ( f2_condicao_falha( $por_id[ $id ], $c['base'], $tessela_varrida ) ) {
			$caidos_pela_condicao[] = $id;
		}
	}
	$sobreviventes = array_values( array_diff( $elegiveis_da_celula,
		$caidos_pela_condicao, $caidos_pela_peca ) );

	foreach ( $sobreviventes as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $pedaco, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" era para estar recomendado e nao esta';
		}
	}
	/* E QUEM CAIU PELA PECA TEM DE SAIR DA RECOMENDACAO E APARECER NA PAGINA, pelas
	   duas metades, igual a condicao. Sem a segunda, o produto poderia sumir da
	   pagina inteira e a regua ficaria verde — foi essa a licao da regra 6. */
	foreach ( $caidos_pela_peca as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			$graves[] = $chave . ': "' . $nome . '" caiu pela proibicao de peca e mesmo assim esta recomendado';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" caiu pela proibicao de peca e sumiu da pagina';
		}
	}
	foreach ( $caidos_pela_condicao as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			/* Mesmo peso do defeito GRAVE: a pagina estaria recomendando um produto
			   que ela mesma, duas secoes abaixo, diz que nao cumpre a condicao. */
			$graves[] = $chave . ': "' . $nome . '" caiu pela condicao e mesmo assim esta recomendado';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" caiu pela condicao e sumiu da pagina';
		}
	}
	foreach ( $c['eliminados_por_proibicao'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $pedaco, $nome ) ) {
			/* COERENCIA DA RECOMENDACAO (secao 12): recomendar em primeiro lugar
			   um produto que a propria pagina diz nao servir e defeito GRAVE. */
			$graves[] = $chave . ': "' . $nome . '" esta recomendado E a pagina diz que ele nao serve';
		}
		if ( false === mb_strpos( $fora, $nome ) ) {
			$erros_celula[] = $chave . ': "' . $nome . '" nao aparece na secao do que nao usar';
		}
		/* E APARECE NO BLOCO DA CAUSA CERTA. A afirmacao acima procura o nome na
		   secao inteira, e ficou verde quando uma mutacao fez a regra 6 rodar
		   ANTES das cinco: o produto proibido pelo fabricante saia do bloco da
		   proibicao e caia no da condicao, e a pagina parava de dizer "a Tekbond
		   escreve espelhos na lista do que este produto nao deve tocar" para
		   dizer que faltava porosidade. A elegibilidade nao muda; a frase que o
		   leitor recebe muda inteira, e e a frase que esta pagina vende.
		   Causa se mede pelo BLOCO em que o produto sai, nunca por estar na
		   secao — e o bloco e marcado no markup, como manda a secao 8. */
		$lista_proibicao = preg_match( '#<ul class="cdm-f2-lista-fora">(.*?)</ul>#is', $fora_html, $mlp )
			? f2_texto( $mlp[1] ) : '';
		$blocos_condicao = preg_match_all( '#<p class="cdm-f2-condicao-fora">(.*?)</p>#is', $fora_html, $mbc )
			? f2_texto( implode( ' ', $mbc[1] ) ) : '';
		if ( false === mb_strpos( $lista_proibicao, $nome ) ) {
			$graves[] = $chave . ': "' . $nome . '" e proibido pelo fabricante e nao esta no bloco da proibicao';
		}
		if ( '' !== $blocos_condicao && false !== mb_strpos( $blocos_condicao, $nome ) ) {
			$graves[] = $chave . ': "' . $nome . '" e proibido e aparece como caso de condicao de superficie';
		}
	}
	/* A LISTA DO SILENCIO E CONFERIDA NOS DOIS SENTIDOS, e nao por acaso: sem
	   isto, a mutacao "a categoria some da pergunta" PASSOU. Ela fazia os cinco
	   rejuntes entrarem na decisao de COLAGEM como "eliminados por silencio" —
	   frase sem sentido para um produto que nunca foi candidato a colar nada —
	   e o teste nao via, porque so olhava o topo e os proibidos. Quem afirma
	   sobre uma lista tem que cobrar o que falta E o que sobra. */
	/* O paragrafo do silencio DA COLA, e nao o primeiro do corpo: a secao do
	   rejunte usa a mesma classe, e procurar no corpo inteiro achava o dela —
	   o mesmo erro de contar &#038; na pagina toda em vez de dentro do script. */
	$silencio = preg_match( '#<p class="cdm-f2-silencio">(.*?)</p>#is', $fora_html, $ms ) ? f2_texto( $ms[1] ) : '';
	foreach ( $c['eliminados_por_silencio'] as $id ) {
		if ( false === mb_strpos( $silencio, f2_nome_esperado( $por_id[ $id ] ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $por_id[ $id ] ) . '" era para estar no silencio e nao esta';
		}
	}
	$esperado_no_silencio = $c['eliminados_por_silencio'];
	foreach ( $por_id as $id => $m ) {
		if ( in_array( $id, $esperado_no_silencio, true ) ) {
			continue;
		}
		if ( false !== mb_strpos( $silencio, f2_nome_esperado( $m ) ) ) {
			$erros_celula[] = $chave . ': "' . f2_nome_esperado( $m ) . '" aparece no silencio e nao devia';
		}
	}

	/* Celula sem recomendado tem que DIZER que nao tem, nunca ficar em branco — e
	   dizer a CAUSA CERTA. Sao duas frases porque sao duas causas: "ninguem
	   declara" e "alguem declara e a condicao nao fecha". Trocar uma pela outra
	   e a afirmacao em bloco com escopo maior do que o medido. */
	if ( ! $sobreviventes ) {
		$t_corpo = f2_texto( $corpo );
		/* A TERCEIRA CAUSA entrou aqui em 13/09/2026, junto com as 27 celulas
		   novas, e ela e a razao de esta secao ter valido o bloco: as 18 celulas
		   antigas TODAS tinham recomendacao, entao a regua escrita a mao nunca
		   tinha pisado numa faixa descoberta, e o ramo de baixo so cobrava a
		   PRESENCA da frase — nunca qual causa ela nomeia. No ar, em quatro
		   estados (vidro, madeira, alvenaria e metal dentro da agua), a pagina
		   dizia "nenhum dos adesivos e declarado" e duas secoes abaixo imprimia
		   "existe mencao a Loctite Durepoxi". Quem manda aqui e a MATRIZ, nao o
		   que a tela devolveu: `mencionados_com_ressalva` e escrito a mao. */
		$ressalva_da_matriz = isset( $c['mencionados_com_ressalva'] ) ? $c['mencionados_com_ressalva'] : array();
		if ( $caidos_pela_peca ) {
			/* A QUINTA CAUSA de celula sem recomendacao, e ela nao tinha ramo aqui
			   porque nunca tinha acontecido. A pagina nao pode dizer "ninguem
			   declara": o fabricante declarou a superficie, declarou o ambiente, e
			   proibiu o caquinho. */
			if ( false !== mb_strpos( $t_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
				$graves[] = $chave . ': caiu pela proibicao de peca e a pagina nega que exista declaracao';
			}
			foreach ( $caidos_pela_peca as $id ) {
				if ( false === mb_strpos( $t_corpo, f2_nome_esperado( $por_id[ $id ] ) ) ) {
					$erros_celula[] = $chave . ': caiu pela proibicao de peca e o produto nao e nomeado';
				}
			}
		} elseif ( $caidos_pela_condicao ) {
			if ( false === mb_strpos( $t_corpo, 'o motivo não é falta de declaração' ) ) {
				$erros_celula[] = $chave . ': caiu pela condicao e a recusa nao nomeia a causa medida';
			}
			if ( false !== mb_strpos( $t_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
				$graves[] = $chave . ': a pagina nega que exista declaracao e ela mesma cita a declaracao';
			}
		} elseif ( $ressalva_da_matriz ) {
			if ( false !== mb_strpos( $t_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
				$graves[] = $chave . ': faixa descoberta com mencao de nivel 4, e a pagina nega que exista declaracao';
			}
			if ( false === mb_strpos( $t_corpo, 'o motivo não é falta de declaração' ) ) {
				$erros_celula[] = $chave . ': faixa descoberta por procedencia, e a recusa nao nomeia essa causa';
			}
			/* A causa medida se nomeia com o PRODUTO e com o TIPO DO DOCUMENTO,
			   e o tipo sai do banco em disco — digitar "material de imprensa"
			   aqui mediria a frase contra ela mesma. */
			foreach ( $ressalva_da_matriz as $id ) {
				$nome = f2_nome_esperado( $por_id[ $id ] );
				if ( false === mb_strpos( $t_corpo, $nome ) ) {
					$erros_celula[] = $chave . ': a recusa por procedencia nao nomeia "' . $nome . '"';
				}
				$fonte = null;
				foreach ( (array) $por_id[ $id ]['fontes'] as $f ) {
					if ( null === $fonte || (int) $f['nivel'] < (int) $fonte['nivel'] ) {
						$fonte = $f;
					}
				}
				if ( $fonte && false === mb_strpos( $t_corpo, $fonte['tipo'] ) ) {
					$erros_celula[] = $chave . ': a recusa por procedencia nao cita o documento ("' . $fonte['tipo'] . '")';
				}
			}
			/* E a vitrine vazia tem de contar a MESMA historia da resposta: era
			   ela que repetia a frase errada uma secao abaixo. */
			if ( false !== mb_strpos( $t_corpo, 'nenhum produto do nosso banco passa no que o fabricante declara' ) ) {
				$graves[] = $chave . ': a vitrine vazia nega a declaracao que a resposta acabou de citar';
			}
		} elseif ( false === mb_strpos( $t_corpo, 'Não temos cola para indicar' ) ) {
			$erros_celula[] = $chave . ': faixa descoberta sem a frase que a declara';
		} elseif ( false === mb_strpos( $t_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
			/* O outro lado da mesma moeda: silencio de verdade tem de dizer que
			   e silencio. Sem esta linha, a frase da procedencia poderia vazar
			   para as sete celulas em que ninguem declarou nada. */
			$erros_celula[] = $chave . ': silencio de verdade, e a pagina nao diz que ninguem declara';
		}
	}
}
f2_ok( empty( $graves ), 'nenhuma pagina recomenda o que ela mesma diz que nao serve',
	empty( $graves ) ? 'as ' . $esperadas_cola . ' celulas' : implode( ' | ', $graves ) );
f2_ok( empty( $erros_celula ), 'a tela diz o que a matriz escrita a mao manda',
	empty( $erros_celula ) ? $esperadas_cola . ' celulas' : implode( ' | ', array_slice( $erros_celula, 0, 4 ) ) );

/* ---------------------------------------------------------------------------
 * 6. O REJUNTE — a grade pisa na borda de cada faixa declarada
 * ------------------------------------------------------------------------- */

echo "\n6. O rejunte: a grade pisa nas bordas das faixas declaradas\n";

/* A regua das bordas e recalculada AQUI, das faixas do banco, e nao lida da
   observacao que o esquema escreveu ao lado. Grade que nao pisa na borda e
   amostra com nome de grade (secao 8). */
$bordas = array();
foreach ( $rejuntes['materiais'] as $m ) {
	foreach ( array( 'junta_min_mm', 'junta_max_mm' ) as $campo ) {
		$v = isset( $m['propriedades'][ $campo ]['valor'] ) ? $m['propriedades'][ $campo ]['valor'] : null;
		if ( null !== $v ) {
			$bordas[ (int) $v ] = true;
			$bordas[ (int) $v + 1 ] = true;
		}
	}
}
ksort( $bordas );
$na_grade = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$na_grade[ (int) $c['junta_mm'] ] = true;
}
$bordas_uteis = array_filter( array_keys( $bordas ), function ( $v ) { return $v >= 1 && $v <= 12; } );
$faltando     = array_diff( $bordas_uteis, array_keys( $na_grade ) );
f2_ok( empty( $faltando ), 'a grade do esquema pisa em toda borda de faixa declarada',
	empty( $faltando ) ? implode( ', ', array_keys( $na_grade ) ) . ' mm' : 'falta ' . implode( ', ', $faltando ) );

$estados_r    = 0;
$erros_rejunte = array();
$secoes_rejunte = array();
for ( $junta = 1; $junta <= 12; $junta++ ) {
	foreach ( $ambientes as $ambiente ) {
		$html = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta );
		$estados_r++;
		$corpo = f2_corpo( $html );
		if ( ! preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)</div>\s*<div class="cdm-f2-secao#is', $corpo, $mr ) ) {
			/* A secao do rejunte e a ultima do bloco de saida em alguns estados. */
			preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*)#is', $corpo, $mr );
		}
		$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
		/* E A SECAO IRMA DO PREPARO, que mora FORA do bloco da prestacao de
		   contas de proposito (ver o comentario no snippet): a conta da 12/09
		   exige que todo rejunte seja nomeado uma vez so la dentro, e instrucao
		   de aplicacao nao e prestacao de contas. Para a afirmacao do preparo ela
		   entra aqui, concatenada, porque o que se mede e o que a PAGINA diz. */
		preg_match( '#<div class="cdm-f2-secao cdm-f2-preparo-secao">(.*?)(?=<div class="cdm-f2-secao[ "]|<h2|$)#is', $corpo, $mpr );
		$secoes_rejunte[ $junta . '|' . $ambiente ] = $trecho
			. ( isset( $mpr[1] ) ? ' ' . f2_texto( $mpr[1] ) : '' );
		if ( '' === $trecho ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': secao do rejunte ausente';
			continue;
		}
		if ( false === mb_strpos( $trecho, (string) $junta ) ) {
			$erros_rejunte[] = $junta . 'mm x ' . $ambiente . ': a resposta nao repete a folga escolhida';
		}
	}
}
f2_ok( 60 === $estados_r, 'os 60 estados de rejunte foram servidos', $estados_r . ' estados' );
f2_ok( empty( $erros_rejunte ), 'todo estado de rejunte serve a secao dele',
	empty( $erros_rejunte ) ? '60 estados' : implode( ' | ', array_slice( $erros_rejunte, 0, 4 ) ) );

$erros_matriz_r = array();
foreach ( $esquema['matriz_esperada_do_rejunte']['celulas'] as $c ) {
	$html   = f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=' . $c['ambiente'] . '&junta=' . (int) $c['junta_mm'] );
	$corpo  = f2_corpo( $html );
	preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mr );
	$trecho = isset( $mr[1] ) ? f2_texto( $mr[1] ) : '';
	preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', isset( $mr[1] ) ? $mr[1] : '', $mf );
	$frase = isset( $mf[1] ) ? f2_texto( $mf[1] ) : '';

	foreach ( $c['recomendados_topo'] as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era topo e nao esta na frase';
		}
	}
	/* OS CARTOES CONTAM TANTO QUANTO A FRASE. Duas mutacoes PASSARAM por esta
	   fresta — "faixa de junta abre 1 mm para baixo" e "faixa pela metade vira
	   sem limite" —, e as duas pelo mesmo motivo: o produto indevido nao subia
	   ao topo, entrava como elegivel ABAIXO do topo, e a frase so nomeia o topo.
	   Recomendar em segundo lugar o que o fabricante nao declara e recomendar. */
	$vitrine_r = '';
	if ( preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>.*?<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $corpo, $mv ) ) {
		$vitrine_r = f2_texto( $mv[1] );
	}
	$recomendaveis = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
	foreach ( array_merge( $c['eliminados_por_ambiente'], $c['eliminados_por_faixa_de_junta'] ) as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false !== mb_strpos( $frase, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na frase e era para estar fora';
		}
		if ( '' !== $vitrine_r && false !== mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" esta na vitrine e era para estar fora';
		}
	}
	foreach ( $recomendaveis as $id ) {
		$nome = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $vitrine_r, $nome ) ) {
			$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': "' . $nome . '" era elegivel e nao esta na vitrine';
		}
	}
	if ( ! $c['recomendados_topo'] && false === mb_strpos( $trecho, 'Não temos rejunte para indicar' ) ) {
		$erros_matriz_r[] = $c['junta_mm'] . 'mm x ' . $c['ambiente'] . ': faixa descoberta sem a frase que a declara';
	}
}
f2_ok( empty( $erros_matriz_r ), 'a tela do rejunte diz o que a matriz escrita a mao manda',
	empty( $erros_matriz_r ) ? $esperadas_rejunte . ' celulas' : implode( ' | ', array_slice( $erros_matriz_r, 0, 4 ) ) );

/* O produto cuja faixa de junta nao foi obtida nao pode ser recomendado em
   NENHUM dos 60 estados.
 *
 * ESTE PORTAO DEPENDIA DE O BANCO TER UMA LACUNA, E A LACUNA FECHOU (05/10/2026).
 * Ate hoje a regua era: varra o banco, ache o produto com `junta_min_mm` ou
 * `junta_max_mm` em null, e exija que ele nunca apareca recomendado. Isso media
 * de verdade enquanto existisse um produto assim — e o canario ao lado
 * (`! empty( $sem_faixa )`) existia justo para provar que existia. Quando o
 * boletim do Rejunte Piscinas foi aberto e a faixa de 2 a 10 mm entrou no
 * banco, o ULTIMO produto sem faixa desapareceu: o canario reprovou e o portao
 * de verdade virou VACUO — zero produto varrido, zero estado medido, verde.
 * E a mutacao `faixa pela metade vira sem limite` do `mutacoes-f2.py`, que
 * completa as pontas null, ficou INERTE pelo mesmo motivo: sem ponta null no
 * banco, nao ha o que completar.
 *
 * O CONSERTO NAO E APAGAR O CANARIO — e parar de depender da sorte do banco.
 * A bancada SINTETIZA o produto sem faixa, numa copia do repositorio, e mede
 * contra ela. O sintetico e um CLONE do registro mais perigoso que existe (o
 * unico declarado para pastilha de vidro submersa), com as duas pontas da faixa
 * em null e outro nome. Assim o portao morde para sempre, com banco lacunoso ou
 * sem nenhuma lacuna, e a mutacao volta a ter alvo.
 *
 * E ele mede as DUAS direcoes, porque sintetico que o render engole em silencio
 * seria o mesmo vacuo com outra roupa: (a) o nome nao aparece em recomendacao
 * em nenhum dos 60 estados, e (b) ele APARECE na lista do que ficou de fora,
 * com a frase que declara a faixa nao obtida — prova de que o render leu o
 * registro em vez de descarta-lo antes da conta. */
$raiz_sem_faixa = f2_raiz_com_rejunte_sem_faixa( $raiz );
$nome_sintetico = 'Rejunte de Bancada Sem Faixa Declarada';
$vazou          = array();
$declarou       = 0;
foreach ( $ambientes as $ambiente ) {
	for ( $junta = 1; $junta <= 12; $junta++ ) {
		$corpo = f2_corpo( f2_render( $raiz_sem_faixa, 'base=ceramica_esmaltada_porcelana&onde=' . $ambiente . '&junta=' . $junta ) );
		/* Frase E vitrine: o produto sem faixa de junta nao pode aparecer em
		   NENHUM dos dois lugares — foi entrando pela vitrine que a mutacao
		   da faixa pela metade passou. */
		preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?:<div class="cdm-f2-secao cdm-f2-fora">|<h2>A tabela inteira)#is', $corpo, $mf );
		$bloco_r = isset( $mf[1] ) ? $mf[1] : '';
		$recomendado_ali = f2_texto(
			( preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', $bloco_r, $m1 ) ? $m1[1] : '' )
			. ' ' . ( preg_match( '#<ul class="cdm-f2-vitrine">(.*?)</ul>#is', $bloco_r, $m2 ) ? $m2[1] : '' )
		);
		if ( false !== mb_strpos( $recomendado_ali, $nome_sintetico ) ) {
			$vazou[] = $junta . 'mm x ' . $ambiente . ': ' . $nome_sintetico;
		}
		$texto_todo = f2_texto( $corpo );
		if ( false !== mb_strpos( $texto_todo, $nome_sintetico )
			&& false !== mb_strpos( $texto_todo, 'a gente não conseguiu a faixa de junta' ) ) {
			$declarou++;
		}
	}
}
f2_ok( 60 === $declarou,
	'o produto sem faixa sintetizado e LIDO pelo render, e a faixa nao obtida e declarada',
	$declarou . ' de 60 estados' );
f2_ok( empty( $vazou ), 'produto sem faixa de junta nunca e recomendado, nos 60 estados',
	empty( $vazou ) ? '60 estados' : implode( ' | ', array_slice( $vazou, 0, 3 ) ) );

/* Entrada fora da faixa volta ao padrao em vez de servir bobagem. */
$fora_da_faixa = f2_corpo( f2_render( $raiz, 'base=inventada&onde=marte&junta=99' ) );
f2_ok( false !== mb_strpos( f2_texto( $fora_da_faixa ), 'Para colar em cerâmica' ),
	'entrada invalida cai no padrao em vez de quebrar a pagina' );

/* A MARCA EM DOBRO NAO APARECE EM TESTE DE CONTER. A mutacao que colava a marca
   em todo nome PASSOU na primeira rodada porque "Rejunte Ceramicas Quartzolit"
   esta DENTRO de "Quartzolit Rejunte Ceramicas Quartzolit" — procurar por
   conter aprova o nome errado que engloba o certo. A regua tem que ser de
   igualdade, e e o <h3> do cartao que carrega o nome. */
$nomes_na_tela = array();
$titulos_ruins = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4' ) as $consulta ) {
	$corpo_c = f2_corpo( f2_render( $raiz, $consulta ) );
	preg_match_all( '#<li class="cdm-f2-cartao[^"]*">.*?<span class="cdm-f2-marca">(.*?)</span>\s*<h3>(.*?)</h3>#is', $corpo_c, $mn, PREG_SET_ORDER );
	foreach ( $mn as $cartao ) {
		$marca_html = f2_texto( $cartao[1] );
		$titulo     = f2_texto( $cartao[2] );
		$nomes_na_tela[ $titulo ] = true;
		/* O <h3> traz o nome comercial; a marca sai no seu proprio campo, uma vez
		   so. Nome que repete a marca ja impressa ao lado dela e marca em dobro. */
		if ( '' !== $marca_html && mb_substr_count( mb_strtolower( $marca_html . ' ' . $titulo, 'UTF-8' ),
				mb_strtolower( $marca_html, 'UTF-8' ) ) > 2 ) {
			$titulos_ruins[] = $marca_html . ' / ' . $titulo;
		}
	}
}
$fora_do_banco = array();
$do_banco = array();
foreach ( $por_id as $m ) {
	$do_banco[ (string) $m['nome_comercial'] ] = true;
}
foreach ( array_keys( $nomes_na_tela ) as $titulo ) {
	if ( ! isset( $do_banco[ $titulo ] ) ) {
		$fora_do_banco[] = $titulo;
	}
}
/* O CARTAO NAO ERA O LUGAR DE MEDIR ISSO, e a mutacao provou: o <h3> traz o
   `nome_comercial` cru e nunca a composicao, entao a marca em dobro so aparece
   na FRASE e nas listas, que e onde `cdm_f2_nome()` e chamada. A regua certa e
   direta e nao depende de onde o nome sai: para todo produto cujo nome
   comercial JA carrega a marca, a composicao "<marca> <nome>" nao pode existir
   em lugar nenhum do corpo. */
$dobradas = array();
foreach ( array( '', 'base=espelho&onde=interno_seco', 'base=mdf_madeira&onde=interno_seco',
                 'base=ceramica_esmaltada_porcelana&onde=interno_molhado&junta=4',
                 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua&junta=3' ) as $consulta ) {
	$texto_c = f2_texto( f2_corpo( f2_render( $raiz, $consulta ) ) );
	foreach ( $por_id as $m ) {
		$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
		$nome  = (string) $m['nome_comercial'];
		if ( '' === $marca || false === mb_stripos( $nome, $marca ) ) {
			continue;
		}
		if ( false !== mb_strpos( $texto_c, $marca . ' ' . $nome ) ) {
			$dobradas[] = ( '' === $consulta ? 'ancora' : $consulta ) . ': "' . $marca . ' ' . $nome . '"';
		}
	}
}
f2_ok( empty( $dobradas ), 'nenhum lugar da pagina repete a marca dentro do nome do produto',
	empty( $dobradas ) ? count( $por_id ) . ' produtos em 5 estados' : implode( ' | ', array_slice( $dobradas, 0, 3 ) ) );
f2_ok( empty( $titulos_ruins ), 'nenhum cartao repete a marca dentro do nome do produto',
	empty( $titulos_ruins ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $titulos_ruins ) );
f2_ok( empty( $fora_do_banco ), 'todo nome de produto na tela e IGUAL ao do banco, nao parecido',
	empty( $fora_do_banco ) ? count( $nomes_na_tela ) . ' nomes' : implode( ' | ', $fora_do_banco ) );

/* ---------------------------------------------------------------------------
 * 7. O bloco de compra vem ANTES da procedencia (secao 7, cicatriz da
 *    Robometria de 10/09/2026), e todo item sem link diz isso.
 * ------------------------------------------------------------------------- */

echo "\n7. Compra antes de procedencia, e o que espera link\n";

$cartoes = preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $corpo_ancora, $mc );
f2_ok( $cartoes > 0, 'a ancora serve cartoes de produto', $cartoes . ' cartoes' );
$ordem_errada = 0;
$sem_fonte    = 0;
foreach ( $mc[1] as $cartao ) {
	$p_compra = mb_strpos( $cartao, 'cdm-f2-compra' );
	$p_fonte  = mb_strpos( $cartao, 'cdm-f2-fonte' );
	if ( false === $p_fonte ) {
		$sem_fonte++;
		continue;
	}
	if ( false === $p_compra || $p_compra > $p_fonte ) {
		$ordem_errada++;
	}
}
f2_ok( 0 === $ordem_errada, 'o bloco de compra vem antes da prova de procedencia em todo cartao',
	$ordem_errada . ' fora de ordem' );
f2_ok( 0 === $sem_fonte, 'todo cartao leva o link de procedencia', $sem_fonte . ' sem fonte' );
f2_ok( false === strpos( $corpo_ancora, 'class="cdm-f2-botao" href' ) || false !== strpos( $corpo_ancora, 'rel="sponsored' ),
	'link de afiliado, quando existir, leva rel="sponsored"' );
f2_ok( (bool) preg_match_all( '#rel="nofollow noopener"#', $corpo_ancora ),
	'o link de procedencia e discreto, com rel="nofollow noopener"' );
f2_ok( false !== mb_strpos( f2_texto( $corpo_ancora ), 'comissão' ), 'o aviso de comissao esta visivel na pagina' );

/* Quantos itens esperam link — numero CONTADO do banco, nunca digitado. */
$esperando = 0;
foreach ( $por_id as $m ) {
	if ( empty( $m['afiliado']['url'] ) ) {
		$esperando++;
	}
}
$declarado = (int) $colas['afiliado']['itens_esperando_link'] + (int) $rejuntes['afiliado']['itens_esperando_link'];
f2_ok( $esperando === $declarado, 'o numero de itens esperando link bate com o banco contado',
	$esperando . ' contados, ' . $declarado . ' declarados' );
$com_loja = substr_count( $corpo_ancora, 'rel="sponsored' );
f2_ok( $com_loja > 0, 'com link no banco, o cartao serve o botao marcado como patrocinado',
	$com_loja . ' botoes' );
f2_ok( 0 === substr_count( $corpo_ancora, 'Link de loja em breve' ) || $esperando > 0,
	'so promete "em breve" quando ha item de verdade esperando link' );

/* ---------------------------------------------------------------------------
 * 7b. A ESCADA DA SECAO 25 NA TELA — os tres estados, cada um no seu mundo
 *
 * A regua e partida em tres porque cada estado pega um defeito diferente, e
 * duas delas so existem num mundo PRODUZIDO: o banco de hoje tem os dez itens
 * no estado 1, entao medir o estado 2 e o 3 no banco de hoje seria medir o
 * caminho que nenhum cartao percorre — verde com a funcao quebrada, e o dia em
 * que importasse seria o dia em que um link morresse.
 *
 * A ordem das tres importa: (a) sozinha passaria numa funcao que ignora a ficha
 * e serve so a busca; (b) sozinha passaria numa funcao que serve a busca sempre,
 * inclusive por cima da ficha; e (c) e a que pega o erro mais provavel de quem
 * escrever isto com pressa — deixar o "em breve" no lugar do piso, que e
 * exatamente o defeito que este bloco veio consertar E O UNICO QUE (a) E (b)
 * APROVARIAM JUNTAS.
 * ------------------------------------------------------------------------- */

echo "\n7b. A escada da secao 25 chega a tela\n";

/* (a) COM FICHA: a ficha e o botao e a busca desce para a linha discreta. */
$com_ficha = 0;
$sem_segunda_porta = array();
foreach ( $mc[1] as $cartao ) {
	if ( false === mb_strpos( $cartao, 'class="cdm-f2-botao" href' ) ) {
		continue;
	}
	$com_ficha++;
	if ( false === mb_strpos( $cartao, 'cdm-f2-busca' ) ) {
		$sem_segunda_porta[] = trim( f2_texto( $cartao ) );
	}
}
f2_ok( $com_ficha > 0, 'o banco de hoje serve cartao com ficha de produto', $com_ficha . ' cartoes' );
f2_ok( empty( $sem_segunda_porta ), 'cartao com ficha leva TAMBEM a busca, na linha discreta abaixo do botao',
	empty( $sem_segunda_porta ) ? $com_ficha . ' com as duas portas' : count( $sem_segunda_porta ) . ' so com o botao' );
f2_ok( false !== mb_strpos( $corpo_ancora, 'Veja todos disponíveis aqui' ),
	'a linha discreta usa a frase que a 25.2 escreve, palavra por palavra' );
/* A AFIRMACAO ERA SOBRE A PAGINA INTEIRA E PASSOU A SER SOBRE O CARTAO, em
   14/09/2026, e a mudanca e de ESCOPO e nao de rigor. Ate a f2 1.4.0 nenhum
   cartao servia busca como botao, entao "a pagina nao tem esta classe" e "cartao
   com ficha nao promove a busca" eram a mesma frase. Com o degrau 4 no ar, dois
   cartoes de cola LEGITIMAMENTE servem busca como botao — eles nao tem ficha —, e
   a frase antiga passou a reprovar a pagina certa. E a mesma familia da afirmacao
   em bloco com escopo maior do que o que foi medido, que a secao 7 do contrato
   nomeia: o que se quer dizer e sobre o cartao COM ficha, entao e nele que se
   mede. */
$ficha_com_busca_de_botao = array();
foreach ( $mc[1] as $cartao ) {
	if ( false === mb_strpos( $cartao, 'class="cdm-f2-botao" href' ) ) {
		continue;
	}
	if ( false !== mb_strpos( $cartao, 'cdm-f2-botao cdm-f2-botao-busca' ) ) {
		$ficha_com_busca_de_botao[] = trim( f2_texto( $cartao ) );
	}
}
f2_ok( empty( $ficha_com_busca_de_botao ),
	'com ficha viva, a busca NAO vira botao — ela e a segunda porta, nao a primeira',
	empty( $ficha_com_busca_de_botao ) ? $com_ficha . ' cartoes com ficha conferidos' : count( $ficha_com_busca_de_botao ) . ' promovem a busca' );

/* TODO link do bloco de compra e link comercial, e os DOIS tem de declarar isso.
   A afirmacao antiga ("quando existir, leva rel=sponsored") olhava a pagina
   inteira e ficava verde com UM link marcado entre dois; esta varre link por
   link dentro do bloco, que e onde a diferenca aparece. Link de busca de
   afiliado e link de afiliado: o atributo declara a relacao comercial, nao o
   formato da pagina de destino. */
$links_sem_sponsored = array();
$crua_com_sponsored  = array();
$cruas               = 0;
if ( preg_match_all( '#<span class="cdm-f2-compra">(.*?)</span>\s*<span class="cdm-f2-fonte"#is', $corpo_ancora, $mb ) ) {
	foreach ( $mb[1] as $bloco ) {
		if ( preg_match_all( '#<a\b[^>]*>#i', $bloco, $ml ) ) {
			foreach ( $ml[0] as $tag ) {
				/* O REL SAI DO QUE O LINK E, NUNCA DO FORMATO DA PAGINA DE DESTINO.
				   Ficha e busca ENCURTADA sao links de afiliado e rendem comissao:
				   `sponsored`. A busca CRUA nao rende nada — ninguem paga por aquele
				   clique —, entao ela e `nofollow` e NAO pode ser `sponsored`. As duas
				   direcoes sao medidas: chamar de patrocinado o que nao paga e mentir
				   ao leitor sobre a unica coisa que ele tem o direito de saber sobre
				   nos, e deixar de marcar o que paga e o defeito oposto. */
				$e_crua = ( false !== mb_strpos( $tag, 'cdm-f2-botao-busca-crua' ) );
				if ( $e_crua ) {
					$cruas++;
					if ( false !== mb_strpos( $tag, 'rel="sponsored' ) ) {
						$crua_com_sponsored[] = $tag;
					}
					if ( false === mb_strpos( $tag, 'rel="nofollow' ) ) {
						$crua_com_sponsored[] = $tag;
					}
					continue;
				}
				if ( false === mb_strpos( $tag, 'rel="sponsored' ) ) {
					$links_sem_sponsored[] = $tag;
				}
			}
		}
	}
}
f2_ok( ! empty( $mb[1] ), 'a varredura acha os blocos de compra para conferir link por link',
	count( $mb[1] ) . ' blocos' );
f2_ok( empty( $links_sem_sponsored ), 'TODO link que RENDE comissao declara rel="sponsored" — a busca encurtada tambem',
	empty( $links_sem_sponsored ) ? 'todos marcados' : implode( ' | ', array_slice( $links_sem_sponsored, 0, 2 ) ) );
/* A BUSCA CRUA DEIXOU DE EXISTIR NO BANCO EM 25/09/2026, e a regua mudou de
   lugar em vez de mudar de exigencia.

   Ate aqui esta linha cobrava `$cruas > 0` na pagina REAL — uma protecao contra
   medir vazio, e ela estava certa em existir. So que as 10h40Z daquele dia os
   31 links desta ilha foram regerados pela Open API e os treze itens de
   pastilha subiram do degrau 4 para o 3; depois disso NENHUM item do banco esta
   na busca crua, e a bancada ficou vermelha por a ilha ter melhorado. O irmao
   `sem_piso` do render ja tinha escrito essa cicatriz em 14/09, sobre si mesmo:
   caso que o banco pode deixar de produzir tem de ser PRODUZIDO, nao esperado.

   Entao agora sao DUAS afirmacoes, e juntas dizem mais do que a antiga: o banco
   de hoje nao tem ninguem no degrau 4 (medido do banco, nao cravado), e o
   `rel` da busca crua e conferido no mundo `so_crua=1`, que a produz. */
f2_ok( 0 === $cruas, 'o banco de hoje nao tem ninguem no degrau 4 — a busca crua sumiu da pagina real',
	$cruas . ' botoes de busca crua na ancora' );

$mundo_so_crua      = f2_corpo( f2_render( $raiz, 'so_crua=1' ) );
$cruas_produzidos   = 0;
$crua_com_sponsored = array();
if ( preg_match_all( '#<span class="cdm-f2-compra">(.*?)</span>\s*<span class="cdm-f2-fonte"#is', $mundo_so_crua, $mb_crua ) ) {
	foreach ( $mb_crua[1] as $bloco ) {
		if ( preg_match_all( '#<a\b[^>]*>#i', $bloco, $ml_crua ) ) {
			foreach ( $ml_crua[0] as $tag ) {
				if ( false === mb_strpos( $tag, 'cdm-f2-botao-busca-crua' ) ) {
					continue;
				}
				$cruas_produzidos++;
				if ( false !== mb_strpos( $tag, 'rel="sponsored' ) ) { $crua_com_sponsored[] = $tag; }
				if ( false === mb_strpos( $tag, 'rel="nofollow' ) )  { $crua_com_sponsored[] = $tag; }
			}
		}
	}
}
f2_ok( $cruas_produzidos > 0, 'PRODUZ O MUNDO: com so_crua=1 a busca crua volta a ser o botao do cartao',
	$cruas_produzidos . ' botoes de busca crua' );
f2_ok( empty( $crua_com_sponsored ), 'a busca CRUA sai nofollow e NUNCA sponsored — ela nao rende comissao',
	empty( $crua_com_sponsored ) ? $cruas_produzidos . ' conferidos' : implode( ' | ', array_slice( $crua_com_sponsored, 0, 2 ) ) );

/* (b) SEM FICHA, COM BUSCA: a busca SOBE e vira o botao. `sem_links=1` apaga a
      ficha e deixa o piso de pe, que e o estado 2 da escada. */
$mundo_so_busca = f2_corpo( f2_render( $raiz, 'sem_links=1' ) );
$botoes_busca   = substr_count( $mundo_so_busca, 'cdm-f2-botao cdm-f2-botao-busca' );
f2_ok( $botoes_busca > 0, 'PRODUZ O MUNDO: sem ficha, a busca sobe e vira o botao do cartao',
	$botoes_busca . ' botoes de busca' );
f2_ok( false !== mb_strpos( $mundo_so_busca, 'Ver as opções na loja' ),
	'o botao de busca tem texto PROPRIO — ele abre uma lista, nao a ficha do produto' );
/* A CONTAGEM DE "EM BREVE" MORREU EM 14/09/2026, E ELA ESTAVA CERTA ATE MORRER.
   A historia inteira vale, porque e a terceira vida desta mesma afirmacao. Ela
   nasceu em 13/09 de manha como "a tela NUNCA diz em breve", quando os cinco
   itens de cola tinham piso; ao entrarem dois sem piso na mesma tarde, ela
   passou a reprovar uma pagina certa e virou uma CONTAGEM — "em breve" na tela
   tem de ser igual ao numero de cartoes que o banco diz sem piso. Em 14/09 a
   secao 7 do contrato proibiu a frase, e a contagem certa passou a ser ZERO em
   qualquer mundo. O que sobra nao e a frase: e a pergunta que ela sempre tentou
   responder — TODO cartao servido tem para onde mandar quem quer comprar? — e
   essa se mede contando LINKS, nao promessas. */
$em_breve_na_tela = substr_count( $mundo_so_busca, 'Link de loja em breve' );
f2_ok( 0 === $em_breve_na_tela,
	'secao 7: a frase "link de loja em breve" NAO existe na tela, em mundo nenhum',
	$em_breve_na_tela . ' ocorrencias' );

$cartoes_sem_saida = array();
if ( preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $mundo_so_busca, $mcb ) ) {
	foreach ( $mcb[1] as $cartao ) {
		if ( ! preg_match( '#<span class="cdm-f2-compra">(.*?)</span>#is', $cartao, $mcp ) ) {
			$cartoes_sem_saida[] = 'cartao sem bloco de compra nenhum';
			continue;
		}
		if ( 0 === preg_match_all( '#<a\b[^>]*>#i', $mcp[1], $mla ) ) {
			$nome = preg_match( '#<h3>(.*?)</h3>#is', $cartao, $mh ) ? f2_texto( $mh[1] ) : '?';
			$cartoes_sem_saida[] = $nome;
		}
	}
	f2_ok( count( $mcb[1] ) > 0, 'a varredura do mundo sem ficha acha os cartoes para contar',
		count( $mcb[1] ) . ' cartoes' );
}
f2_ok( empty( $cartoes_sem_saida ),
	'25.2: sem ficha, TODO cartao servido continua com uma saida de compra clicavel',
	empty( $cartoes_sem_saida ) ? count( $mcb[1] ) . ' cartoes, todos com link' : implode( ' | ', $cartoes_sem_saida ) );
f2_ok( false === mb_strpos( $mundo_so_busca, 'Ver na loja</a>' ),
	'sem ficha, nenhum cartao promete "Ver na loja" — a promessa segue o link que existe' );

/* (c) SEM NADA — E AGORA ESTE MUNDO NAO PODE CHEGAR AO AR.
   Ate 14/09 ele era o unico lugar onde "em breve" era a resposta certa. Com a
   frase proibida, o que a tela faz aqui e NAO PROMETER: o bloco de compra sai
   vazio, e quem impede o mundo de existir e o `validar-banco.py`, que reprova
   item sem nenhuma das tres saidas. A afirmacao mede as duas metades — a tela
   nao inventa promessa, e o cartao continua sendo servido, porque a recomendacao
   nunca dependeu do link. */
$mundo_sem_piso = f2_corpo( f2_render( $raiz, 'sem_piso=1' ) );
f2_ok( 0 === substr_count( $mundo_sem_piso, 'Link de loja em breve' ),
	'PRODUZ O MUNDO: sem ficha, sem busca e sem busca crua, a tela nao promete nada' );
$blocos_vazios = 0;
if ( preg_match_all( '#<span class="cdm-f2-compra">(.*?)</span>#is', $mundo_sem_piso, $mcv ) ) {
	foreach ( $mcv[1] as $bloco ) {
		if ( '' === trim( $bloco ) ) {
			$blocos_vazios++;
		}
	}
}
f2_ok( $blocos_vazios > 0, 'PRODUZ O MUNDO: o bloco de compra fica VAZIO em vez de reservar o lugar com promessa',
	$blocos_vazios . ' blocos vazios' );
f2_ok( 0 === substr_count( $mundo_sem_piso, 'rel="sponsored' ) && 0 === substr_count( $mundo_sem_piso, 'cdm-f2-botao-busca-crua' ),
	'sem saida nenhuma, nao sobra link de compra nenhum na pagina' );
$cartoes_sem_piso = preg_match_all( '#<li class="cdm-f2-cartao[^"]*">#is', $mundo_sem_piso );
f2_ok( $cartoes_sem_piso === $cartoes,
	'o cartao sem compra continua sendo servido: a recomendacao nao depende do link',
	$cartoes_sem_piso . ' cartoes contra ' . $cartoes . ' do banco de hoje' );

/* A ESCADA E DE UMA FUNCAO SO, E ISTO SE MEDE NA MARCACAO, NAO NA PROSA.
   Se a F1, a ficha do Guia ou a pagina da peca reescreverem os tres estados por
   conta propria, dois degraus discordam em silencio. A varredura conta a CLASSE
   emitida — `class="cdm-f2-sem-loja"` so aparece em marcacao, enquanto a frase
   legivel aparece tambem em comentario, e contar a frase mediria o quanto os
   comentarios falam dela. A primeira versao desta linha cometeu esse erro e
   reprovou o proprio comentario que explica a regra. */
/* E A SOMA FOI PARTIDA EM 14/09/2026, porque ela sobreviveu a mudanca dando o
   mesmo numero por OUTRA composicao — que e a forma mais silenciosa de um portao
   parar de medir. Antes: 1 etiqueta "sem loja" + 1 botao de busca + 1 linha
   discreta = 3. Depois da f2 1.5.0: 0 etiquetas + 2 botoes de busca (encurtada e
   crua) + 1 linha discreta = 3 de novo. A soma ficou verde enquanto um degrau
   inteiro sumia e outro nascia. Agora cada degrau e contado pelo proprio
   marcador, e o esperado e escrito degrau a degrau. */
$por_degrau = array();
foreach ( glob( dirname( __DIR__ ) . '/snippets/*.php' ) as $arquivo ) {
	$fonte = file_get_contents( $arquivo );
	$conta = array(
		'ficha'          => substr_count( $fonte, 'class="cdm-f2-botao" href' ),
		'linha_discreta' => substr_count( $fonte, 'class="cdm-f2-busca"' ),
		'busca_encurtada' => substr_count( $fonte, 'cdm-f2-botao cdm-f2-botao-busca" href' ),
		'busca_crua'     => substr_count( $fonte, 'cdm-f2-botao-busca-crua' ),
	);
	if ( array_sum( $conta ) ) {
		$por_degrau[ basename( $arquivo ) ] = $conta;
	}
}
$esperado_degraus = array(
	'clubedomosaico-f2.php' => array(
		'ficha'           => 1,
		'linha_discreta'  => 1,
		'busca_encurtada' => 1,
		'busca_crua'      => 1,
	),
);
f2_ok( $esperado_degraus === $por_degrau,
	'os QUATRO degraus sao emitidos por UM snippet so, um lugar cada, nunca copiados',
	json_encode( $por_degrau ) );

/* ---------------------------------------------------------------------------
 * 8. As duas faixas descobertas, declaradas em vez de preenchidas no chute
 * ------------------------------------------------------------------------- */

echo "\n8. O que a ilha diz que nao sabe (secao 7 do contrato)\n";

$t = f2_texto( $corpo_ancora );

/* A SECAO DO QUE FALTA E CONTADA, E O PORTAO RECONTA POR UM CAMINHO PROPRIO.
   As duas afirmacoes que estavam aqui procuravam as frases "peça de plástico" e
   "dentro da água o tempo todo" — as duas faixas que a pagina declarava nao
   saber. Elas eram exatas ate 13/09/2026 e viraram falsas no mesmo dia, quando
   os dois produtos novos abriram as duas. Portao que procura a frase de ontem
   passa a cobrar a mentira: por isso ele deixou de procurar texto e passou a
   RECONTAR, com regua propria (le o banco e o esquema, nao chama o snippet) e
   comparar com o numero que a tela publica. */
if ( preg_match( '#<h2>O que a gente ainda não responde</h2>(.*?)</div>#is', $corpo_ancora, $mfx ) ) {
	$texto_faltas = f2_texto( $mfx[1] );
} else {
	$texto_faltas = '';
}
f2_ok( '' !== $texto_faltas, 'a pagina serve a secao do que ela ainda nao responde' );

/* A RECONTAGEM SAI POR DOIS CAMINHOS, E OS DOIS MEDEM COISAS DIFERENTES.
 *
 * (i) O TOTAL e aritmetica do vocabulario: base x lugar x caquinho. Nao depende
 *     de elegibilidade nenhuma, entao ele prova que a pagina esta falando da
 *     entrada INTEIRA e nao de um recorte dela.
 *
 * (ii) O NUMERO DE DESCOBERTAS e recontado VARRENDO AS PAGINAS SERVIDAS, uma
 *      por combinacao, um processo cada. Isso mede a agregacao — o laco que a
 *      secao nova escreveu — contra o que cada estado realmente serve, e e
 *      exatamente onde mora o erro provavel de quem escreve um contador: somar
 *      uma dimensao a menos, ou contar "sem topo" onde ha elegivel abaixo do
 *      topo.
 *
 * O QUE ISTO NAO MEDE, dito em vez de escondido: as duas metades leem a mesma
 * implementacao de elegibilidade, entao esta recontagem NAO e regua independente
 * para as cinco regras — quem faz esse papel sao as celulas escritas a mao no
 * esquema e as 5 ancoras da regra 6 no validador.
 *
 * A DIVIDA QUE ESTE COMENTARIO DECLARAVA FOI PAGA EM 13/09/2026: ate aquela data
 * a matriz escrita a mao cobria 18 das 45 celulas de base x lugar, e as outras 27
 * so passavam por aqui — portao verde que media a AGREGACAO e nao a decisao. Agora
 * a matriz tem as 45, derivadas a mao das declaracoes ANTES de o validador rodar, e
 * o bloco 5 acima varre TODAS elas contra o que a tela diz. A recontagem desta secao
 * continua nao sendo regua independente, e continua escrita aqui por isso: ela mede
 * outra coisa (o laco que agrega), e quem mede a decisao esta uma secao acima.
 */
$total_combinacoes = count( $esquema['vocabularios']['base'] )
	* count( $esquema['vocabularios']['ambiente'] )
	* count( $esquema['vocabularios']['material_tessela'] );

$descobertos_varridos = 0;
$varridos             = 0;
$sem_resposta_mudos   = array();
$nao_prestados        = array();
foreach ( $esquema['vocabularios']['base'] as $b_ ) {
	foreach ( $esquema['vocabularios']['ambiente'] as $a_ ) {
		foreach ( $esquema['vocabularios']['material_tessela'] as $t_ ) {
			$corpo_ = f2_corpo( f2_render( $raiz, 'base=' . $b_ . '&onde=' . $a_ . '&caco=' . $t_ ) );
			$varridos++;
			$texto_ = f2_texto( $corpo_ );
			$vazio  = ( false !== mb_strpos( $texto_, 'Não temos cola para indicar' )
				|| false !== mb_strpos( $texto_, 'o motivo não é falta de declaração' ) );
			if ( $vazio ) {
				$descobertos_varridos++;
			}
			/* Estado sem recomendacao tem de DIZER isso. Pagina que fica em
			   branco e indistinguivel de pagina quebrada — e some da contagem
			   sem ninguem ver, que e como um contador fica verde errado. */
			if ( ! $vazio && false === mb_strpos( $corpo_, 'class="cdm-f2-cartao' ) ) {
				$sem_resposta_mudos[] = $b_ . ' x ' . $a_ . ' x ' . $t_;
			}

			/* A PRESTACAO DE CONTAS DA COLA, nas 270 respostas (secao 7 do
			   ARQUIPELAGO.md, a regra que nasceu nesta ilha em 12/09/2026).
			   Todo item da categoria consultada aparece EXATAMENTE UMA VEZ na
			   prosa: ou na frase que o recomenda, e ai ele esta na vitrine, ou
			   numa linha que diz por que ele nao esta. O rejunte ja tinha portao
			   proprio para isso; a cola nunca teve, e a regra 6 acabou de criar
			   um QUINTO grupo — que e exatamente a forma como um grupo some da
			   tela sem ninguem ver, porque grupo vazio nao denuncia que a tela
			   nao sabe imprimi-lo.

			   A soma e cobrada contra o banco CONTADO do arquivo, nunca contra
			   um numero digitado aqui. */
			/* O LADO em que o produto cai e decidido pelo MARKUP, nao pela
			   posicao no texto. O bloco de recusa (`cdm-f2-faixa`) mora dentro
			   da regiao da resposta e e, em conteudo, o lado do "por que ele nao
			   esta" — ele nomeia produto para dizer que aquele produto NAO foi
			   indicado. Conta-lo como recomendacao poria o mesmo item nos dois
			   lados e reprovaria uma pagina certa; ignora-lo deixaria passar uma
			   pagina que nomeia o produto sem nunca dizer de que lado ele esta.
			   A regra que a secao 7 cobra e "cada item em exatamente UM lado", e
			   e o lado que se mede. */
			$resposta_html = '';
			if ( preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>\s*<div class="cdm-f2-secao">\s*<h2>Onde comprar</h2>(.*?)(?=<div class="cdm-f2-secao">)#is', $corpo_, $mr_ ) ) {
				$resposta_html = $mr_[1] . $mr_[2];
			}
			$recusa_html     = '';
			if ( preg_match_all( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', $resposta_html, $mrec_ ) ) {
				$recusa_html = implode( ' ', $mrec_[0] );
			}
			$regiao_resposta = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '', $resposta_html ) );
			$regiao_fora = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo_, $mf_ )
				? f2_texto( $recusa_html . ' ' . $mf_[1] ) : f2_texto( $recusa_html );
			foreach ( $por_id as $id_c => $m_c ) {
				if ( 'cola' !== $m_c['categoria'] || 'ativo' !== $m_c['status'] ) {
					continue;
				}
				$nome_c = (string) $m_c['nome_comercial'];
				$na_resposta = ( false !== mb_strpos( $regiao_resposta, $nome_c ) );
				$no_fora     = ( false !== mb_strpos( $regiao_fora, $nome_c ) );
				if ( ! $na_resposta && ! $no_fora ) {
					$nao_prestados[] = $b_ . ' x ' . $a_ . ' x ' . $t_ . ': ' . $nome_c . ' sumiu da pagina';
				} elseif ( $na_resposta && $no_fora ) {
					$nao_prestados[] = $b_ . ' x ' . $a_ . ' x ' . $t_ . ': ' . $nome_c . ' aparece nos dois lados';
				}
			}
		}
	}
}
f2_ok( $varridos === $total_combinacoes, 'a varredura visitou a entrada inteira, um processo cada',
	$varridos . ' de ' . $total_combinacoes );
$colas_ativas = 0;
foreach ( $por_id as $m_c ) {
	if ( 'cola' === $m_c['categoria'] && 'ativo' === $m_c['status'] ) {
		$colas_ativas++;
	}
}
f2_ok( empty( $nao_prestados ),
	'secao 7: cada cola do banco e nomeada UMA vez em cada uma das ' . $varridos . ' respostas',
	empty( $nao_prestados )
		? ( $colas_ativas * $varridos ) . ' nomeacoes, ' . $colas_ativas . ' colas contadas do arquivo'
		: implode( ' | ', array_slice( $nao_prestados, 0, 3 ) ) );
f2_ok( empty( $sem_resposta_mudos ), 'nenhum estado fica sem cartao E sem dizer que nao tem',
	empty( $sem_resposta_mudos ) ? $varridos . ' estados' : implode( ' | ', array_slice( $sem_resposta_mudos, 0, 3 ) ) );
f2_ok( false !== mb_strpos( $texto_faltas, number_format_i18n( $total_combinacoes ) . ' combinações' ),
	'o total de combinacoes publicado bate com o vocabulario contado', $total_combinacoes . ' combinacoes' );
f2_ok( false !== mb_strpos( $texto_faltas, 'Em ' . number_format_i18n( $descobertos_varridos ) . ' delas' ),
	'o numero de faixas descobertas publicado bate com a varredura das paginas',
	$descobertos_varridos . ' varridas' );
/* ---------------------------------------------------------------------------
 * 6b. A PROMESSA DA SERP — titulo e description com os numeros desta varredura
 *
 * Acrescentada em 02/10/2026 com o BLOCO A do despacho do Raphael de 24/09. Os
 * tres numeros usados aqui — colas, combinacoes e descobertas — sao os que ESTE
 * arquivo contou sozinho (`$colas_ativas` do banco, `$total_combinacoes` do
 * vocabulario, `$descobertos_varridos` das 270 paginas servidas). Se o snippet
 * preencher a frase com outro numero, as duas escritas discordam aqui.
 *   POR QUE ISTO E O PORTAO QUE IMPORTA: a promessa do resultado da busca e a
 * unica afirmacao desta ilha que ninguem de dentro le. Quem a ve e quem decide
 * clicar, e ele nao tem como conferir nada.
 * ------------------------------------------------------------------------- */
$desc_esperada_f2 = 'Qual cola e qual rejunte pela declaração do fabricante: '
	. number_format_i18n( $colas_ativas ) . ' colas em ' . number_format_i18n( $total_combinacoes )
	. ' casos de base, lugar e caquinho, e os ' . number_format_i18n( $descobertos_varridos )
	. ' que a gente ainda não responde.';
f2_ok( $desc === $desc_esperada_f2,
	'a description serve os TRES numeros que esta bancada contou sozinha',
	$desc === $desc_esperada_f2 ? 'igual' : 'servida: ' . $desc );

$titulo_f2 = '';
if ( preg_match( '#<title>(.*?)</title>#is', $ancora, $mt_f2 ) ) {
	$titulo_f2 = html_entity_decode( $mt_f2[1], ENT_QUOTES, 'UTF-8' );
}
$titulo_esperado_f2 = CDM_F2_TITULO . ' – ' . number_format_i18n( $colas_ativas )
	. ' colas para ' . number_format_i18n( count( $esquema['vocabularios']['base'] ) ) . ' bases';
f2_ok( $titulo_f2 === $titulo_esperado_f2,
	'o <title> e o NOME da pagina mais a promessa contada, e a marca saiu do fim',
	$titulo_f2 );
f2_ok( '' !== $titulo_f2 && mb_strlen( $titulo_f2 ) <= CDM_CASCA_TITULO_TETO,
	'e ele cabe no teto de ' . CDM_CASCA_TITULO_TETO, mb_strlen( $titulo_f2 ) . ' caracteres' );
f2_ok( 0 === strpos( $titulo_f2, CDM_F2_TITULO ),
	'o nome da pagina nao foi tocado — ele continua sendo o mesmo do H1 e da trilha' );

/* O MUNDO EM QUE O BANCO NAO CHEGOU — a TRAVA 2 exercida na pagina, e nao so na
   funcao pura. Sem numero nao ha promessa: a marca volta ao fim do titulo e a
   `description` cai na frase sem numero, que tem de caber na MESMA faixa de 120
   a 160. Frase curta aqui seria trocar um defeito por outro no lugar onde o
   clique se decide — o Google descarta description curta e escreve a dele. */
$html_sem_banco = f2_render( $raiz, 'sem_banco=1' );
$titulo_sb = '';
if ( preg_match( '#<title>(.*?)</title>#is', $html_sem_banco, $mt_sb ) ) {
	$titulo_sb = html_entity_decode( $mt_sb[1], ENT_QUOTES, 'UTF-8' );
}
$desc_sb = '';
if ( preg_match( '#<meta name="description" content="([^"]*)"#', $html_sem_banco, $md_sb ) ) {
	$desc_sb = html_entity_decode( $md_sb[1], ENT_QUOTES, 'UTF-8' );
}
f2_ok( $titulo_sb === CDM_F2_TITULO . ' – ' . CDM_CASCA_NOME_SITE,
	'TRAVA 2 no ar: sem banco, a marca volta ao fim do <title>', $titulo_sb );
f2_ok( '' !== $desc_sb && 0 === preg_match( '/\d/', $desc_sb ),
	'e a description cai na frase SEM numero', $desc_sb );
f2_ok( mb_strlen( $desc_sb ) >= 120 && mb_strlen( $desc_sb ) <= 160,
	'e a frase sem numero cabe na mesma faixa de 120 a 160', mb_strlen( $desc_sb ) . ' caracteres' );

f2_ok( $descobertos_varridos > 0 && $descobertos_varridos < $total_combinacoes,
	'a contagem nao e vacuidade: nem tudo descoberto, nem tudo coberto',
	$descobertos_varridos . ' de ' . $total_combinacoes );

f2_ok( false !== mb_strpos( $t, 'material de imprensa' ),
	'a pagina diz por que a menção de nivel 4 nao vira recomendacao' );

/* ---------------------------------------------------------------------------
 * A TABELA PRE-RENDERIZADA, E A COLUNA DA CONDICAO.
 *
 * Esta afirmacao nasceu de uma mutacao que PASSOU: apagar a coluna da condicao
 * da tabela deixava o portao inteiro verde. O defeito era real e o ar o pegava,
 * mas conferir-no-ar.py e outro portao — e defeito pego pela regra VIZINHA
 * prova que ALGUMA trava existe, nunca que ESTA existe. Enquanto a bancada nao
 * medisse, a tabela podia perder a coluna e so o desembarque diria.
 *
 * E ela e a metade mais cara de errar: a tabela e o que um modelo de linguagem
 * le sem preencher formulario, e ela nao tem a coluna do caquinho — a linha
 * "plastico, dentro de casa: use PL500" sai servida no HTML como se valesse
 * sempre. A coluna da condicao e o escopo dessa linha, e sem ela a tabela
 * afirma num escopo maior do que o medido.
 *
 * A regua e propria: quem carrega condicao sai do BANCO lido do disco, e o
 * texto esperado e o literal do fabricante gravado la — nunca o que o snippet
 * imprime.
 * ------------------------------------------------------------------------- */

$com_condicao_no_banco = array();
foreach ( $por_id as $id_c => $m_c ) {
	if ( 'cola' === $m_c['categoria'] && 'ativo' === $m_c['status']
		&& ! empty( $m_c['condicoes']['exige_superficie_porosa']['valor'] ) ) {
		$com_condicao_no_banco[ (string) $m_c['nome_comercial'] ] =
			(string) $m_c['condicoes']['exige_superficie_porosa']['literal'];
	}
}
f2_ok( ! empty( $com_condicao_no_banco ),
	'o banco tem produto com condicao declarada — sem isso esta secao nao mede nada',
	count( $com_condicao_no_banco ) . ' com condicao' );

$tabela_html = preg_match( '#<h2>A tabela inteira, sem preencher nada</h2>(.*?)</table>#is', $corpo_ancora, $mt )
	? $mt[1] : '';
f2_ok( '' !== $tabela_html, 'a tabela pre-renderizada esta no HTML servido' );
f2_ok( false !== mb_strpos( $tabela_html, 'Com que condição' ),
	'a tabela declara a coluna da condicao no cabecalho' );

$linhas_tabela = preg_match_all( '#<tr>(?!<th)(.*?)</tr>#is', $tabela_html, $mlt ) ? $mlt[1] : array();
$erros_tabela  = array();
$linhas_com_condicao = 0;
foreach ( $linhas_tabela as $linha ) {
	if ( ! preg_match_all( '#<td>(.*?)</td>#is', $linha, $mtd ) || count( $mtd[1] ) < 5 ) {
		continue;
	}
	$usa   = f2_texto( $mtd[1][2] );
	$cond  = f2_texto( $mtd[1][4] );
	foreach ( $com_condicao_no_banco as $nome_c => $literal_c ) {
		$na_coluna_usa = ( false !== mb_strpos( $usa, $nome_c ) );
		$na_coluna_cond = ( false !== mb_strpos( $cond, $nome_c ) );
		if ( $na_coluna_usa ) {
			$linhas_com_condicao++;
			if ( ! $na_coluna_cond ) {
				$erros_tabela[] = '"' . $usa . '" indica ' . $nome_c . ' e a linha nao diz a condicao';
			} elseif ( false === mb_strpos( $cond, $literal_c ) ) {
				$erros_tabela[] = '"' . $usa . '" diz a condicao sem o texto literal do fabricante';
			}
		} elseif ( $na_coluna_cond ) {
			$erros_tabela[] = 'linha cita a condicao de ' . $nome_c . ' sem indicar o produto';
		}
	}
}
f2_ok( $linhas_com_condicao > 0,
	'ha linha da tabela que indica produto com condicao — senao a afirmacao abaixo nao morde',
	$linhas_com_condicao . ' linhas' );
f2_ok( empty( $erros_tabela ), 'toda linha que indica produto com condicao publica a condicao literal',
	empty( $erros_tabela ) ? $linhas_com_condicao . ' linhas conferidas' : implode( ' | ', array_slice( $erros_tabela, 0, 3 ) ) );

/* O tempo de espera que a ilha NAO tem: o campo existe no banco com o motivo
   escrito, e a pagina diz que nao publica em vez de simplesmente nao ter a
   secao. Ausencia de secao e indistinguivel de "nao importa". */
$mdf = f2_texto( f2_corpo( f2_render( $raiz, 'base=mdf_madeira&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $mdf, 'ainda não publica o tempo de espera' ),
	'quando falta o tempo de espera, a pagina diz que falta' );
$ceramica = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=interno_seco' ) ) );
f2_ok( false !== mb_strpos( $ceramica, '24 horas' ),
	'quando o fabricante declara a cura, a pagina publica o numero' );

/* PLASTICO: a faixa abriu em 13/09/2026, e o portao mede as DUAS metades dela.
   Com caquinho de vidro continua sem resposta — e agora com a causa certa, que
   e a condicao e nao a ausencia de declaracao. Com caquinho de ceramica ha
   recomendacao. Medir so uma das duas deixaria a regra 6 sem prova: as duas
   telas seriam identicas byte a byte se a condicao nao existisse. */
$plastico = f2_texto( f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_vidro' ) ) );
f2_ok( false !== mb_strpos( $plastico, 'o motivo não é falta de declaração' ),
	'plastico com caquinho liso: a recusa nomeia a condicao, nao a ausencia de declaracao' );

/* A SAIDA QUE A PAGINA OFERECE E CONFERIDA CONTRA O ESQUEMA, nas duas direcoes.
   A frase "trocando por X, ele voltaria a servir" e a unica da pagina que diz a
   pessoa o que FAZER para a peca nao descolar, e ela nasceu com os quatro nomes
   digitados. Digitada, ela erra calada no dia em que uma tessela nova entrar no
   vocabulario — e erra do jeito caro, mandando colar. Aqui o esperado sai do
   esquema e cobra as duas direcoes: toda porosa nomeada, nenhuma nao porosa. */
/* MEDIDO NO BLOCO, NAO NO CORPO — e a primeira versao disto reprovou por isso.
   Ela procurou os nomes no corpo inteiro e achou "Caquinho de espelho" dentro
   do <select> do formulario, que serve as seis opcoes em toda pagina. E o mesmo
   erro de contar &#038; na pagina inteira em vez de dentro do <script>, um
   nivel mais fundo: aqui nem o corpo basta, porque a afirmacao e sobre UMA
   frase. Quem afirma sobre uma frase mede naquela frase. */
$plastico_html = f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_vidro' ) );
$bloco_saida   = preg_match_all( '#<p class="cdm-f2-condicao-fora">(.*?)</p>#is', $plastico_html, $mbs )
	? f2_texto( implode( ' ', $mbs[1] ) ) : '';
$rot_t = $rot['tessela'];
$erros_saida = array();
f2_ok( '' !== $bloco_saida, 'a varredura acha o bloco da condicao para medir a saida oferecida' );
foreach ( $esquema['superficies_porosas']['tesselas_porosas'] as $t_p ) {
	if ( false === mb_stripos( $bloco_saida, $rot_t[ $t_p ] ) ) {
		$erros_saida[] = 'falta ' . $rot_t[ $t_p ];
	}
}
foreach ( $esquema['superficies_porosas']['tesselas_nao_porosas'] as $t_n ) {
	/* O caquinho ESCOLHIDO aparece no mesmo bloco, na frase que diz que ele nao
	   absorve agua — entao a proibicao vale so para os OUTROS nao porosos. */
	if ( 'pastilha_vidro' !== $t_n && false !== mb_stripos( $bloco_saida, $rot_t[ $t_n ] ) ) {
		$erros_saida[] = 'oferece ' . $rot_t[ $t_n ] . ', que nao e porosa';
	}
}
f2_ok( empty( $erros_saida ), 'a saida oferecida bate com a classificacao do esquema, nas duas direcoes',
	empty( $erros_saida ) ? count( $esquema['superficies_porosas']['tesselas_porosas'] ) . ' porosas nomeadas'
		: implode( ' | ', $erros_saida ) );
f2_ok( false === mb_strpos( $plastico, 'Nenhum dos adesivos do nosso banco é declarado' ),
	'plastico com caquinho liso: a pagina NAO nega a declaracao que ela mesma cita' );
$plastico_poroso = f2_texto( f2_corpo( f2_render( $raiz, 'base=plastico&onde=interno_seco&caco=pastilha_ceramica' ) ) );
f2_ok( false !== mb_strpos( $plastico_poroso, 'Cascola Adesivo de Montagem PL500 Interior' ),
	'plastico com caquinho poroso: a faixa que estava descoberta responde' );
f2_ok( false === mb_strpos( $plastico_poroso, 'Não temos cola para indicar' ),
	'plastico com caquinho poroso: a pagina nao diz que nao sabe o que ela sabe' );
f2_ok( false !== mb_strpos( $plastico_poroso, 'somos nós, não ela' ),
	'a atribuicao fica dividida: a condicao e do fabricante, a classificacao e nossa (26.3)' );
/* DECLARACAO VAGA NAO E SILENCIO, e a pagina separa as duas. Dizer "o
   fabricante nao fala" de um produto cujo fabricante escreveu "certos tipos de
   plastico" seria falso: ele falou, e falou de um jeito que nao decide. */
f2_ok( false !== mb_strpos( $plastico, 'certos tipos de plástico' )
	&& false !== mb_strpos( $plastico, 'não nomeia material nenhum' ),
	'a declaracao vaga aparece separada do silencio, com a frase do fabricante' );
/* CONTATO PERMANENTE COM AGUA: aberto em ceramica e SO em ceramica. As duas
   afirmacoes sao o par que impede a faixa de parecer maior do que e. */
$submerso = f2_texto( f2_corpo( f2_render( $raiz, 'base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua' ) ) );
f2_ok( false !== mb_strpos( $submerso, 'Tekbond Silicone Acético Maxx' ),
	'o estado submerso em ceramica responde: a faixa de nivel 4 virou faixa de nivel 3' );
f2_ok( false === mb_strpos( $submerso, 'Não temos cola para indicar' ),
	'o estado submerso em ceramica nao diz mais que a ilha nao sabe' );
$submerso_vidro = f2_texto( f2_corpo( f2_render( $raiz, 'base=vidro&onde=contato_permanente_agua' ) ) );
f2_ok( false !== mb_strpos( $submerso_vidro, 'Não temos cola para indicar' ),
	'a mesma agua sobre VIDRO continua descoberta — o fabricante nomeia ceramica, nao vidro' );

/* ---------------------------------------------------------------------------
 * A REGUA DA REGRA 7, escrita AQUI — 06/10/2026
 *
 * Ela le `grupos_de_tessela_proibidos` do esquema e `condicoes` do banco em
 * disco, e nao chama uma linha do snippet. Mesma trava da secao 8 que a regra 6
 * tem, e aqui ela e mais necessaria, nao menos: a ANCORA escrita a mao da regra
 * 6 em 13/09/2026 declarava o Tekbond Silicone Acetico Construcao no topo de
 * `vidro` + `caco de espelho`, e o produto estava proibido em espelho desde
 * 10/09. As duas metades estavam certas sobre a regra 6 e as duas eram cegas
 * para a MESMA frase. Portao independente mede divergencia entre as metades,
 * nunca a lacuna que as duas tem — e e por isso que esta secao varre o
 * CAQUINHO, que a varredura dos 45 estados nao varre.
 * ------------------------------------------------------------------------- */

echo "\n9. A regra 7: a proibicao declarada sobre a PECA\n";

$grupos_esq = isset( $esquema['grupos_de_tessela_proibidos']['grupos'] )
	? $esquema['grupos_de_tessela_proibidos']['grupos'] : array();
f2_ok( ! empty( $grupos_esq ), 'o esquema traz os grupos de peca — sem eles esta secao nao mede nada',
	count( $grupos_esq ) . ' grupos' );

/** Os caquinhos que ESTE produto proibe, pela declaracao dele cruzada com a lista do esquema. */
function f2_peca_proibida_no_banco( $m, $tessela, $grupos_esq ) {
	$dec = isset( $m['condicoes']['proibe_grupos_de_tessela']['valor'] )
		? (array) $m['condicoes']['proibe_grupos_de_tessela']['valor'] : array();
	$morde = array();
	foreach ( $dec as $g ) {
		if ( isset( $grupos_esq[ $g ] )
			&& in_array( $tessela, (array) $grupos_esq[ $g ]['tesselas_no_grupo'], true ) ) {
			$morde[] = $g;
		}
	}

	return $morde;
}

/* Quem carrega proibicao de peca, e todo caquinho que algum grupo alcanca. Os
   dois contados do disco: digitar aqui faria o portao medir o mundo de hoje. */
$com_proibicao_de_peca = array();
foreach ( $por_id as $id_p => $m_p ) {
	if ( ! empty( $m_p['condicoes']['proibe_grupos_de_tessela']['valor'] ) ) {
		$com_proibicao_de_peca[] = $id_p;
	}
}
f2_ok( ! empty( $com_proibicao_de_peca ),
	'o banco tem produto com proibicao de peca declarada — senao a regra 7 nao morde em nada',
	count( $com_proibicao_de_peca ) . ' produtos' );

$caquinhos_proibidos = array();
foreach ( $grupos_esq as $g_ => $d_ ) {
	foreach ( (array) $d_['tesselas_no_grupo'] as $t_ ) {
		$caquinhos_proibidos[ $t_ ] = true;
	}
}
$caquinhos_livres = array_values( array_diff(
	$esquema['vocabularios']['material_tessela'], array_keys( $caquinhos_proibidos ) ) );
f2_ok( ! empty( $caquinhos_livres ),
	'ha caquinho FORA de todo grupo — senao a celula de controle nao existe',
	implode( ', ', $caquinhos_livres ) );

/* O ALVO DA VARREDURA: as celulas em que a regra 7 TEM de morder, derivadas da
   matriz escrita a mao (camada de declaracao) cruzada com os caquinhos
   proibidos. Produto que a matriz nao poe como elegivel nao e candidato — e e
   essa a invariante que a cimentcola AC-II carrega: ela declara DOIS grupos e
   nao aparece em nenhuma celula aqui, porque a regra 2 a tira antes. */
$alvos_peca = array();
foreach ( $esquema['matriz_esperada_da_F2']['celulas'] as $c7 ) {
	$eleg7 = f2_elegiveis_da_matriz( $esquema, $c7['base'], $c7['ambiente'] );
	foreach ( array_keys( $caquinhos_proibidos ) as $t7 ) {
		$esperados = array();
		foreach ( $eleg7 as $id7 ) {
			if ( f2_peca_proibida_no_banco( $por_id[ $id7 ], $t7, $grupos_esq ) ) {
				$esperados[] = $id7;
			}
		}
		if ( $esperados ) {
			$alvos_peca[ $c7['base'] . '|' . $c7['ambiente'] . '|' . $t7 ] = $esperados;
		}
	}
}
f2_ok( ! empty( $alvos_peca ),
	'a regra 7 morde em pelo menos uma celula servida — regra que nunca morde nao foi medida',
	count( $alvos_peca ) . ' celulas base x lugar x caquinho' );

$erros_peca   = array();
$graves_peca  = array();
$medidas_peca = 0;
foreach ( $alvos_peca as $chave7 => $esperados ) {
	list( $b7, $a7, $t7 ) = explode( '|', $chave7 );
	$html7 = f2_corpo( f2_render( $raiz, 'base=' . $b7 . '&onde=' . $a7 . '&caco=' . $t7 ) );
	$medidas_peca++;

	$resp_html = preg_match( '#<div class="cdm-f2-resposta">(.*?)</div>#is', $html7, $mr7 ) ? $mr7[1] : '';
	/* O bloco de recusa sai da resposta antes de qualquer afirmacao sobre quem
	   esta recomendado — mesma trava que a regra 6 pagou em 13/09: a recusa
	   NOMEIA o produto, e medir presenca de nome na regiao inteira leria a
	   verdade como defeito. */
	$resp = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '', $resp_html ) );
	$fora_html7 = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $html7, $mf7 ) ? $mf7[1] : '';
	$blocos_peca = preg_match_all( '#<p class="cdm-f2-peca-fora">(.*?)</p>#is', $fora_html7, $mbp )
		? $mbp[1] : array();
	$texto_peca  = f2_texto( implode( ' ', $blocos_peca ) );
	$blocos_cond7 = preg_match_all( '#<p class="cdm-f2-condicao-fora">(.*?)</p>#is', $fora_html7, $mbc7 )
		? f2_texto( implode( ' ', $mbc7[1] ) ) : '';

	foreach ( $esperados as $id7 ) {
		$m7   = $por_id[ $id7 ];
		$nome7 = f2_nome_esperado( $m7 );
		if ( false !== mb_strpos( $resp, $nome7 ) ) {
			/* GRAVE pelo mesmo motivo da regra 6: a pagina estaria recomendando
			   um produto que ela mesma, duas secoes abaixo, diz que o fabricante
			   proibe no que se cola. */
			$graves_peca[] = $chave7 . ': "' . $nome7 . '" e proibido neste caquinho e esta recomendado';
		}
		if ( false === mb_strpos( $texto_peca, $nome7 ) ) {
			$erros_peca[] = $chave7 . ': "' . $nome7 . '" saiu pela proibicao de peca e nao esta no bloco dela';
			continue;
		}
		if ( '' !== $blocos_cond7 && false !== mb_strpos( $blocos_cond7, $nome7 ) ) {
			/* Causa se mede pelo BLOCO em que o produto sai. Proibicao de peca
			   lida como condicao de superficie troca a frase inteira que o
			   leitor recebe: ele passa a ler que falta porosidade onde o
			   fabricante escreveu para nao usar. */
			$graves_peca[] = $chave7 . ': "' . $nome7 . '" sai pela proibicao de peca e aparece como caso de condicao';
		}
		/* A ATRIBUICAO DIVIDIDA (26.3) e a CITACAO: as duas metades sao cobradas
		   no bloco, nao na pagina. A frase nossa sem a frase dele e acusacao sem
		   prova; a frase dele sem a nossa e emprestimo de autoridade. */
		foreach ( f2_peca_proibida_no_banco( $m7, $t7, $grupos_esq ) as $g7 ) {
			$lit7 = isset( $m7['condicoes']['proibe_grupos_de_tessela']['literais'][ $g7 ] )
				? $m7['condicoes']['proibe_grupos_de_tessela']['literais'][ $g7 ] : '';
			if ( '' === $lit7 || false === mb_strpos( $texto_peca, $lit7 ) ) {
				$erros_peca[] = $chave7 . ': o bloco nao cita a frase do fabricante do grupo ' . $g7;
			}
		}
		if ( false === mb_strpos( $texto_peca, 'somos nós, não ela' ) ) {
			$graves_peca[] = $chave7 . ': o bloco nao separa a classificacao nossa da declaracao dela (26.3)';
		}
		/* A SAIDA OFERECIDA, nas duas direcoes, igual a da regra 6: todo caquinho
		   que ESTE produto nao proibe tem de ser nomeado, e nenhum que ele proiba.
		   Digitada, esta frase erra calada no dia em que um caquinho novo entrar
		   — e erra mandando colar.

		   A PRIMEIRA VERSAO DESTA AFIRMACAO REPROVOU A PAGINA E A PAGINA ESTAVA
		   CERTA: ela media a saida contra a uniao dos grupos de TODOS os
		   produtos, e acusou o acetico de oferecer pastilha de vidro — que so e
		   proibida pela cimentcola AC-II, outro registro. A frase da pagina diz
		   "com X ELE voltaria a servir", no singular, e e por produto que ela
		   tem de ser medida. Grupo e do PRODUTO, nunca do caquinho em abstrato,
		   e esta a linha que o esquema escreve em
		   `o_grupo_e_do_PRODUTO_e_nao_do_CAQUINHO`. */
		$proibidos_deste = array();
		foreach ( (array) $m7['condicoes']['proibe_grupos_de_tessela']['valor'] as $gd ) {
			foreach ( (array) $grupos_esq[ $gd ]['tesselas_no_grupo'] as $td ) {
				$proibidos_deste[ $td ] = true;
			}
		}
		foreach ( $esquema['vocabularios']['material_tessela'] as $tl ) {
			$nome_tl = $rot['tessela'][ $tl ];
			if ( isset( $proibidos_deste[ $tl ] ) ) {
				if ( $tl !== $t7 && false !== mb_stripos( $texto_peca, $nome_tl ) ) {
					$erros_peca[] = $chave7 . ': a saida oferece ' . $nome_tl
						. ', que este mesmo produto proibe';
				}
			} elseif ( false === mb_stripos( $texto_peca, $nome_tl ) ) {
				$erros_peca[] = $chave7 . ': a saida nao oferece ' . $nome_tl;
			}
		}
	}

	/* A CELULA SEM SOBREVIVENTE TEM DE NOMEAR *ESTA* CAUSA — e esta afirmacao
	   nasceu de uma MUTACAO QUE PASSOU. Apagar o ramo da recusa da regra 7 do
	   snippet nao reprovou nada na primeira rodada da bateria, e o motivo e que
	   HOJE nao existe celula em que a regra 7 esvazie a recomendacao: nas seis
	   que ela morde, sempre sobra alguem. O ramo e codigo que o portao nao
	   alcanca — a mesma familia do `else` que ficou morto na regra 6 ate a
	   matriz ir de 18 para 45 celulas em 13/09/2026, e que no ar dizia a frase
	   errada em quatro estados.

	   Entao a afirmacao fica escrita AGORA, cobrando a causa certa no dia em que
	   a celula esvaziar, e a bateria passa a PRODUZIR esse mundo para medi-la.
	   Sem as duas, a frase mais honesta desta pagina seria servida sem ninguem
	   nunca a ter visto. */
	$sobrevive = array();
	foreach ( f2_elegiveis_da_matriz( $esquema, $b7, $a7 ) as $id_s ) {
		if ( in_array( $id_s, $esperados, true ) ) {
			continue;
		}
		if ( f2_condicao_falha( $por_id[ $id_s ], $b7, $t7 ) ) {
			continue;
		}
		$sobrevive[] = $id_s;
	}
	if ( ! $sobrevive ) {
		$t7_corpo = f2_texto( $html7 );
		if ( false === mb_strpos( $t7_corpo, 'para indicar cola aqui com esse caquinho' ) ) {
			$erros_peca[] = $chave7 . ': celula esvaziada pela regra 7 e a recusa nao nomeia essa causa';
		}
		if ( false !== mb_strpos( $t7_corpo, 'Nenhum dos adesivos do nosso banco é declarado' ) ) {
			$graves_peca[] = $chave7 . ': a pagina nega que exista declaracao e ela mesma cita a proibicao';
		}
	}

	/* A CELULA DE CONTROLE: o MESMO estado trocando so o caquinho por um livre.
	   Sem ela, uma regra larga demais — que tirasse o produto de todo caquinho —
	   passaria por todas as afirmacoes acima. */
	$t_livre = $caquinhos_livres[0];
	$html_c  = f2_corpo( f2_render( $raiz, 'base=' . $b7 . '&onde=' . $a7 . '&caco=' . $t_livre ) );
	/* A FRONTEIRA DA CAIXA DE RESPOSTA E O MARCADOR DA SECAO SEGUINTE, nunca o
	   primeiro `</div>`. A forma antiga — `<div class="cdm-f2-resposta">(.*?)</div>`
	   — fechava no primeiro aninhamento, e por isso ela media "a frase mais o que
	   vier antes do proximo </div>": enquanto a camada de prova era o primeiro
	   filho, dava certo por acidente de ordem. Em 06/10/2026 o bloco de preparo
	   entrou antes dela e esta afirmacao caiu em duas celulas, sem que nada da
	   regra 7 tivesse mudado. Regua que depende de contar `</div>` mede o HTML;
	   fronteira de teste e marcador escrito — a mesma cicatriz que a Robometria
	   deixou em 13/09/2026 e que o `pr_bloco_f1` do teste-prestacao-rejunte cita. */
	$resp_c  = f2_texto( preg_replace( '#<p class="cdm-f2-frase cdm-f2-faixa">.*?</p>#is', '',
		preg_match( '#<div class="cdm-f2-resposta">(.*?)(?=<div class="cdm-f2-secao[ "]|<h2|$)#is', $html_c, $mrc ) ? $mrc[1] : '' ) );
	$peca_c  = preg_match_all( '#<p class="cdm-f2-peca-fora">(.*?)</p>#is', $html_c, $mpc )
		? f2_texto( implode( ' ', $mpc[1] ) ) : '';
	foreach ( $esperados as $id7 ) {
		$nome7 = f2_nome_esperado( $por_id[ $id7 ] );
		if ( false !== mb_strpos( $peca_c, $nome7 ) ) {
			$graves_peca[] = $b7 . '|' . $a7 . '|' . $t_livre . ': "' . $nome7
				. '" sai pela proibicao de peca com caquinho que nenhum grupo alcanca';
		}
		if ( false === mb_strpos( $resp_c, $nome7 ) ) {
			$erros_peca[] = $b7 . '|' . $a7 . '|' . $t_livre . ': "' . $nome7
				. '" era para voltar a ser recomendado com caquinho livre e nao esta';
		}
	}
}

f2_ok( empty( $graves_peca ), 'GRAVE: nenhuma pagina recomenda produto proibido no caquinho escolhido',
	empty( $graves_peca ) ? $medidas_peca . ' celulas medidas, mais a de controle de cada uma'
		: implode( ' | ', array_slice( $graves_peca, 0, 3 ) ) );
f2_ok( empty( $erros_peca ), 'a regra 7 sai no bloco dela, com a frase do fabricante e a saida certa',
	empty( $erros_peca ) ? $medidas_peca . ' celulas conferidas' : implode( ' | ', array_slice( $erros_peca, 0, 3 ) ) );

/* A TABELA PRE-RENDERIZADA, pela mesma aritmetica da coluna da condicao: ela e a
   camada de DECLARACAO e nao tem o caquinho, entao a linha que indica um produto
   com proibicao de peca seria lida como se valesse para qualquer caquinho. E a
   metade da pagina que um modelo de linguagem le sem preencher formulario. */
f2_ok( '' !== $tabela_html, 'a tabela pre-renderizada foi achada para medir a regra 7' );
$linhas7       = preg_match_all( '#<tr>(?!<th)(.*?)</tr>#is', $tabela_html, $ml7 ) ? $ml7[1] : array();
$erros_tabela7 = array();
$linhas_com_peca = 0;
foreach ( $linhas7 as $linha7 ) {
	$cels7 = preg_match_all( '#<td>(.*?)</td>#is', $linha7, $mc7l ) ? $mc7l[1] : array();
	if ( count( $cels7 ) < 5 ) {
		continue;
	}
	$usa7  = f2_texto( $cels7[2] );
	$cond7 = f2_texto( $cels7[4] );
	foreach ( $com_proibicao_de_peca as $id7 ) {
		$nome7 = f2_nome_esperado( $por_id[ $id7 ] );
		if ( false === mb_strpos( $usa7, $nome7 ) ) {
			continue;
		}
		$linhas_com_peca++;
		if ( false === mb_strpos( $cond7, $nome7 ) || false === mb_strpos( $cond7, 'não com ' ) ) {
			$erros_tabela7[] = '"' . $usa7 . '" indica ' . $nome7 . ' e a linha nao diz o caquinho proibido';
			continue;
		}
		$grupos7 = (array) $por_id[ $id7 ]['condicoes']['proibe_grupos_de_tessela']['valor'];
		foreach ( $grupos7 as $g7 ) {
			$lit7 = isset( $por_id[ $id7 ]['condicoes']['proibe_grupos_de_tessela']['literais'][ $g7 ] )
				? $por_id[ $id7 ]['condicoes']['proibe_grupos_de_tessela']['literais'][ $g7 ] : '';
			if ( '' !== $lit7 && false === mb_strpos( $cond7, $lit7 ) ) {
				$erros_tabela7[] = '"' . $usa7 . '" diz o caquinho proibido sem o texto literal do fabricante';
			}
		}
	}
}
f2_ok( $linhas_com_peca > 0,
	'ha linha da tabela que indica produto com proibicao de peca — senao a afirmacao abaixo nao morde',
	$linhas_com_peca . ' linhas' );
f2_ok( empty( $erros_tabela7 ),
	'toda linha que indica produto com proibicao de peca publica o caquinho e a frase literal',
	empty( $erros_tabela7 ) ? $linhas_com_peca . ' linhas conferidas' : implode( ' | ', array_slice( $erros_tabela7, 0, 3 ) ) );

/* ---------------------------------------------------------------------------
 * O PREPARO NA TELA (esquema v12, 06/10/2026) — e a regua aqui e a INVERSA da
 * do resto deste arquivo.
 *
 * As outras afirmacoes partem da matriz escrita a mao e cobram que a pagina
 * concorde com ela. Esta parte da PAGINA SERVIDA: ela le, no texto, quem a
 * pagina acabou de recomendar, e so entao vai ao banco buscar o que aquele
 * produto declara. O motivo e que o defeito que este bloco conserta nao era de
 * calculo e sim de OMISSAO — nove declaracoes gravadas e nenhuma tela servindo-as
 * —, e omissao nao aparece numa regua que mede concordancia entre duas listas.
 *
 * As tres afirmacoes, e a terceira e a que importa mais:
 *   1. produto recomendado que TEM literal serve o literal, em toda celula;
 *   2. produto recomendado que NAO tem literal aparece pelo nome, com a causa —
 *      lista que so mostra quem passou faz o leitor ler ausencia como "nao
 *      precisa de preparo", e nao e isso que a ausencia quer dizer;
 *   3. NENHUMA parafrase nossa aparece em estado nenhum. E a unica das tres que
 *      mede o defeito de 26.3 — a nossa frase saindo com o nome do fabricante
 *      embaixo — e ela varre os 45 corpos de cola e as 60 secoes de rejunte
 *      contra TODAS as parafrases do banco, nao so as dos recomendados.
 * ------------------------------------------------------------------------- */

$com_literal   = array();   // nome comercial => literal
$sem_literal   = array();   // nome comercial => true
$parafrases    = array();   // nome comercial => parafrase que NAO pode subir
foreach ( array( $colas, $rejuntes ) as $_banco ) {
	foreach ( (array) $_banco['materiais'] as $_m ) {
		$_nome = $_m['nome_comercial'];
		$_p    = isset( $_m['preparo'] ) && is_array( $_m['preparo'] ) ? $_m['preparo'] : array();
		if ( ! empty( $_p['literal_do_fabricante'] ) ) {
			$com_literal[ $_nome ] = $_p['literal_do_fabricante'];
		} else {
			$sem_literal[ $_nome ] = true;
		}
		if ( ! empty( $_p['nossa_leitura'] ) ) {
			$parafrases[ $_nome ] = $_p['nossa_leitura'];
		}
	}
}

f2_ok( count( $com_literal ) > 0 && count( $sem_literal ) > 0 && count( $parafrases ) > 0,
	'o banco tem os TRES estados do preparo — senao as afirmacoes abaixo nao mordem',
	count( $com_literal ) . ' com literal, ' . count( $sem_literal ) . ' sem, '
		. count( $parafrases ) . ' parafrases guardadas' );

$faltou_literal = array();
$faltou_causa   = array();
$celulas_com_preparo = 0;

foreach ( $corpos as $chave => $corpo ) {
	$texto = f2_texto( $corpo );
	/* Quem a PAGINA recomendou, lido do texto dela: o nome aparece na frase de
	   indicacao. Nada de ler a celula do esquema aqui — a inversao e o ponto. */
	/* O BLOCO SE DELIMITA PELO TEXTO, e nao por `</div>`: dentro dele mora a
	   caixa `cdm-prova` de cada literal, entao `(.*?)</div></div>` fecha no
	   primeiro aninhamento e, quando a celula nao tem cola recomendada, engole a
	   pagina a partir da secao do rejunte. Foi assim que a primeira versao desta
	   afirmacao acusou tres colas em `vidro x contato permanente com agua`, que e
	   uma celula SEM cola nenhuma. Regua que depende de contar `</div>` mede o
	   HTML; esta mede o que a pagina diz. */
	$bloco_preparo = f2_recorte( $texto, 'Antes de colar, o que o fabricante manda fazer',
		array( 'Antes de rejuntar, o que o fabricante manda fazer', 'E o rejunte, que vai entre os caquinhos' ) );
	if ( '' === $bloco_preparo ) {
		continue;
	}
	$celulas_com_preparo++;
	foreach ( $com_literal as $nome => $literal ) {
		if ( false !== mb_strpos( $bloco_preparo, $nome ) ) {
			if ( false === mb_strpos( $bloco_preparo, f2_texto( $literal ) ) ) {
				$faltou_literal[] = $chave . ': ' . $nome;
			}
		}
	}
	foreach ( $sem_literal as $nome => $_ ) {
		if ( false !== mb_strpos( $bloco_preparo, $nome )
			&& false === mb_strpos( $bloco_preparo, 'não tem a instrução de preparo' ) ) {
			$faltou_causa[] = $chave . ': ' . $nome;
		}
	}
}

f2_ok( $celulas_com_preparo > 0, 'ha celula de cola servindo o bloco de preparo',
	$celulas_com_preparo . ' de 45' );
f2_ok( empty( $faltou_literal ),
	'todo produto recomendado que tem literal de preparo serve o literal',
	empty( $faltou_literal ) ? $celulas_com_preparo . ' celulas conferidas'
		: implode( ' | ', array_slice( $faltou_literal, 0, 3 ) ) );
f2_ok( empty( $faltou_causa ),
	'todo produto recomendado SEM literal aparece pelo nome, com a causa',
	empty( $faltou_causa ) ? $celulas_com_preparo . ' celulas conferidas'
		: implode( ' | ', array_slice( $faltou_causa, 0, 3 ) ) );

$rejunte_sem_literal = array();
$rejunte_com_bloco   = 0;
foreach ( $secoes_rejunte as $chave => $trecho ) {
	if ( false === mb_strpos( $trecho, 'Antes de rejuntar' ) ) {
		continue;
	}
	$rejunte_com_bloco++;
	$bloco_r = f2_recorte( $trecho, 'Antes de rejuntar, o que o fabricante manda fazer', array() );
	foreach ( $com_literal as $nome => $literal ) {
		if ( false !== mb_strpos( $bloco_r, $nome )
			&& false === mb_strpos( $bloco_r, 'não tem a instrução de preparo na palavra' )
			&& false === mb_strpos( $bloco_r, f2_texto( $literal ) ) ) {
			$rejunte_sem_literal[] = $chave . ': ' . $nome;
		}
	}
}
f2_ok( $rejunte_com_bloco > 0, 'ha estado de rejunte servindo o bloco de preparo',
	$rejunte_com_bloco . ' de 60' );
f2_ok( empty( $rejunte_sem_literal ), 'no rejunte, quem abre o bloco de preparo abre com o literal',
	empty( $rejunte_sem_literal ) ? $rejunte_com_bloco . ' estados conferidos'
		: implode( ' | ', array_slice( $rejunte_sem_literal, 0, 3 ) ) );

/* A TERCEIRA, e a que mede o defeito da 26.3: nenhuma parafrase nossa em
   estado nenhum, nem na cola nem no rejunte. */
$parafrase_no_ar = array();
foreach ( $parafrases as $nome => $parafrase ) {
	$agulha = f2_texto( $parafrase );
	if ( mb_strlen( $agulha ) < 20 ) {
		continue;
	}
	foreach ( $corpos as $chave => $corpo ) {
		if ( false !== mb_strpos( f2_texto( $corpo ), $agulha ) ) {
			$parafrase_no_ar[] = 'cola ' . $chave . ': ' . $nome;
			break;
		}
	}
	foreach ( $secoes_rejunte as $chave => $trecho ) {
		if ( false !== mb_strpos( $trecho, $agulha ) ) {
			$parafrase_no_ar[] = 'rejunte ' . $chave . ': ' . $nome;
			break;
		}
	}
}
f2_ok( empty( $parafrase_no_ar ),
	'nenhuma parafrase NOSSA de preparo chega a tela, em 45 + 60 estados',
	empty( $parafrase_no_ar ) ? count( $parafrases ) . ' parafrases procuradas'
		: implode( ' | ', array_slice( $parafrase_no_ar, 0, 3 ) ) );

/* A QUARTA AFIRMACAO, e ela existe porque uma frase deste repositorio prometeu o
   que nao aconteceu. O registro da `quartzolit-cimentcola-externo-acii` dizia,
   desde 05/10, que a cura de 180 dias nao podia ser gravada porque "a F2 NAO
   serve preparo em lugar nenhum" — e dai se leu que servir preparo poria a cura
   na tela. NAO POS: este produto e eliminado por SILENCIO nas 45 celulas,
   porque `indicado_para` nao nomeia nenhuma base do vocabulario, e o bloco de
   preparo so alcanca quem a pagina RECOMENDA. Servir preparo era necessario e
   nao suficiente; o terceiro bloqueio e JUSANTE do segundo.

   Esta afirmacao fixa o estado de hoje nos DOIS sentidos, e e por isso que ela
   nao e uma linha so: enquanto o literal nao estiver em celula nenhuma, ela
   cobra ZERO; no dia em que o substrato entrar, ela cai, e quem a vir cair tem o
   comentario aqui dizendo que a queda e a ENTREGA e nao o defeito. Afirmacao que
   so sabe dizer "continua zero" deixaria a cura entrar na tela sem ninguem
   conferir que ela entrou junto com a recomendacao. */
$CURA_DA_CIMENTCOLA = 'Paredes de concreto curado há 180 dias';
$NOME_AC            = 'Argamassa Cimentcola Externo AC-II Quartzolit';

/* (A) OS 45 ESTADOS DA VARREDURA, e os DOIS lados lidos da PAGINA SERVIDA.
   Esta afirmacao comparava o texto servido com a MATRIZ do esquema, e isso media
   duas camadas diferentes: a matriz e a de DECLARACAO (regras 1 a 5 e 8) e a
   pagina serve a de declaracao MENOS as regras 7 e 6. O caquinho padrao da
   varredura e `pastilha_vidro`, que e justamente um dos que esta argamassa
   proibe nos DOIS grupos dela — entao nos 45 estados a cimentcola nunca chega a
   ser recomendada, e a cura nao sai. Comparar com a matriz cobrava cinco
   presencas que a pagina esta CERTA em nao ter.
   Lida dos dois lados na propria pagina, a afirmacao volta a dizer uma coisa
   verdadeira e util: a cura sai exatamente onde o produto e recomendado. */
$com_cura    = array();
$recomenda_ac = array();
foreach ( $corpos as $chave => $corpo ) {
	$texto = f2_texto( $corpo );
	if ( false !== mb_strpos( $texto, $CURA_DA_CIMENTCOLA ) ) {
		$com_cura[] = $chave;
	}
	$bloco = f2_recorte( $texto, 'Antes de colar, o que o fabricante manda fazer',
		array( 'Antes de rejuntar, o que o fabricante manda fazer', 'E o rejunte, que vai entre os caquinhos' ) );
	if ( '' !== $bloco && false !== mb_strpos( $bloco, $NOME_AC ) ) {
		$recomenda_ac[] = $chave;
	}
}
sort( $com_cura );
sort( $recomenda_ac );
f2_ok( $com_cura === $recomenda_ac,
	'nos 45 estados, a cura de 180 dias sai exatamente onde a pagina recomenda a cimentcola',
	$com_cura === $recomenda_ac
		? count( $com_cura ) . ' estados (o caquinho padrao da varredura e proibido por ela)'
		: 'com a cura: ' . ( implode( ', ', $com_cura ) ?: 'nenhum' )
			. ' | recomendam: ' . ( implode( ', ', $recomenda_ac ) ?: 'nenhum' ) );

/* (B) A ENTREGA DE 06/10/2026, MEDIDA ONDE ELA ACONTECE — e esta parte existe
   porque a (A) nao consegue ve-la. A cura entrou na tela JUNTO com a
   recomendacao, e para um leitor de verdade: quem vai colar CACO DE AZULEJO
   sobre cimento. `caco_azulejo` e o unico caquinho fora dos dois grupos que esta
   argamassa proibe, e e por isso que ele e o caquinho desta medicao — a escolha
   nao e de gosto e esta conferida contra o esquema, logo abaixo.
   A regua tem os DOIS SENTIDOS, e e por isso que ela vale um bloco: nas celulas
   em que a matriz indica a argamassa a cura TEM de sair, e numa celula em que a
   REGRA 8 a tira ela NAO pode sair. Sem o segundo sentido, uma implementacao que
   servisse a cura em toda pagina de cimento ficaria verde. */
$CAQUINHO_LIVRE = 'caco_azulejo';
$grupos_da_ac = array();
foreach ( (array) $por_id['quartzolit-cimentcola-externo-acii']['condicoes']['proibe_grupos_de_tessela']['valor'] as $g ) {
	$grupos_da_ac[] = $g;
}
$livre_de_verdade = true;
foreach ( $grupos_da_ac as $g ) {
	if ( in_array( $CAQUINHO_LIVRE, (array) $esquema['grupos_de_tessela_proibidos']['grupos'][ $g ]['tesselas_no_grupo'], true ) ) {
		$livre_de_verdade = false;
	}
}
f2_ok( $livre_de_verdade && count( $grupos_da_ac ) > 0,
	'o caquinho desta medicao esta fora dos grupos que a cimentcola proibe — senao ela mede o nada',
	$CAQUINHO_LIVRE . ' contra ' . count( $grupos_da_ac ) . ' grupos declarados' );

$indicam_na_matriz = array();
foreach ( (array) $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
	$todos = array_merge( (array) ( isset( $c['recomendados_topo'] ) ? $c['recomendados_topo'] : array() ),
		(array) ( isset( $c['elegiveis_abaixo_do_topo'] ) ? $c['elegiveis_abaixo_do_topo'] : array() ) );
	if ( in_array( 'quartzolit-cimentcola-externo-acii', $todos, true ) ) {
		$indicam_na_matriz[] = $c['base'] . '|' . $c['ambiente'];
	}
}
f2_ok( count( $indicam_na_matriz ) > 0,
	'a matriz indica a cimentcola em pelo menos uma celula — senao a entrega nao existe para medir',
	count( $indicam_na_matriz ) . ' celulas' );

$sem_a_cura = array();
foreach ( $indicam_na_matriz as $chave ) {
	list( $b_, $a_ ) = explode( '|', $chave );
	$t_ = f2_texto( f2_corpo( f2_render( $raiz, 'base=' . $b_ . '&onde=' . $a_ . '&caco=' . $CAQUINHO_LIVRE ) ) );
	if ( false === mb_strpos( $t_, $CURA_DA_CIMENTCOLA ) || false === mb_strpos( $t_, $NOME_AC ) ) {
		$sem_a_cura[] = $chave;
	}
}
f2_ok( empty( $sem_a_cura ),
	'com caquinho que ela nao proibe, a cura de 180 dias esta na tela em TODA celula que a indica',
	empty( $sem_a_cura ) ? count( $indicam_na_matriz ) . ' celulas conferidas com ' . $CAQUINHO_LIVRE
		: implode( ', ', $sem_a_cura ) );

/* O OUTRO SENTIDO, na celula que a REGRA 8 decide: mesmo caquinho, mesma base de
   alvenaria, trocando so o LUGAR. Aqui a argamassa nao e recomendada, entao a
   cura NAO pode aparecer — e a frase da regra 8 TEM de aparecer, com a citacao
   do fabricante, porque a causa que o codigo separa o texto separa. */
$t_fora = f2_texto( f2_corpo( f2_render( $raiz,
	'base=alvenaria_tijolo&onde=externo_abrigado&caco=' . $CAQUINHO_LIVRE ) ) );
f2_ok( '' !== $t_fora && false === mb_strpos( $t_fora, $CURA_DA_CIMENTCOLA ),
	'na celula que a regra 8 tira, a cura NAO vai a tela — instrucao sem indicacao seria receita do que nao serve',
	'' === $t_fora ? 'o render falhou' : 'alvenaria_tijolo x externo_abrigado' );
f2_ok( false !== mb_strpos( $t_fora, 'declara esta superfície, e declara com o lugar dentro da frase' )
	&& false !== mb_strpos( $t_fora, 'em paredes internas' ),
	'e a frase da regra 8 sai com a citacao do fabricante, nao com o nosso vocabulario',
	'alvenaria_tijolo x externo_abrigado' );

/* ---------------------------------------------------------------------------
 * 10. A REGRA 3: o ambiente DO PRODUTO, e a frase que ela tirou do silencio
 *
 * Esta secao mede a causa que atravessou 27 dias no ar. A regra 3 existe desde o
 * bloco 3, sempre eliminou certo, e mandava quem ela eliminava para o balde do
 * SILENCIO — que serve "O fabricante simplesmente nao fala desta superficie" sobre
 * produtos cujos fabricantes a declaram em `indicado_para`. Nenhuma regua viu,
 * porque todas mediam ELEGIBILIDADE, e a elegibilidade nunca mudou.
 *
 * Por isso as afirmacoes aqui sao sobre a FRASE e sobre os DOIS SENTIDOS da lista.
 * A do silencio, na secao 7, ja cobra o que falta e o que sobra; se a matriz e o
 * snippet discordarem sobre quem saiu dela, aquela secao reprova. Esta cobra o
 * outro lado: que quem saiu de la esteja NO BALDE NOVO, com o literal do fabricante
 * ao lado e sem a palavra que diz que ele nao falou.
 * ------------------------------------------------------------------------- */

echo "\n10. A regra 3: o ambiente DO PRODUTO\n";

$REGRAS_AMB = isset( $esquema['regras_do_balde_do_ambiente_do_produto'] )
	? $esquema['regras_do_balde_do_ambiente_do_produto'] : array();
f2_ok( ! empty( $REGRAS_AMB['produtos_que_delimitam_ambiente_hoje'] ),
	'o esquema traz os produtos que delimitam ambiente — sem eles esta secao nao mede nada',
	count( (array) ( isset( $REGRAS_AMB['produtos_que_delimitam_ambiente_hoje'] )
		? $REGRAS_AMB['produtos_que_delimitam_ambiente_hoje'] : array() ) ) . ' produtos' );

/* Os literais que a tela tem de citar, LIDOS DO BANCO e nao desta tabela: o que o
   esquema escreve e conferido pelo validador contra o registro, e aqui quem manda e
   o registro, para as duas metades nao se apoiarem uma na outra. */
$LITERAIS_DELIM = array();
foreach ( $por_id as $id => $m ) {
	/* SO COLA. A categoria e parte da pergunta, e `$por_id` carrega o banco inteiro:
	   sem este filtro a evidencia desta linha listava `quartzolit-rejunte-acrilico`
	   entre os produtos de cola. A afirmacao nao mudava — os ids conferidos saem da
	   matriz, que e de cola — e o numero impresso mentia, que e a familia do defeito
	   que esta secao existe para medir um andar acima. */
	if ( 'cola' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
		continue;
	}
	$ad = isset( $m['declaracoes']['ambientes_declarados'] ) ? (array) $m['declaracoes']['ambientes_declarados'] : array();
	if ( $ad ) {
		$LITERAIS_DELIM[ $id ] = $ad;
	}
}
ksort( $LITERAIS_DELIM );
f2_ok( count( $LITERAIS_DELIM ) > 0,
	'ha produto de cola com `ambientes_declarados` no banco — senao a regra 3 nao morde em nada',
	implode( ', ', array_keys( $LITERAIS_DELIM ) ) );

/* AS CELULAS EM QUE A REGRA MORDE, lidas da MATRIZ escrita a mao — nunca do
   snippet. Regua que pergunta ao medido quais celulas medir nao e regua. */
$celulas_amb_produto = array();
foreach ( (array) $esquema['matriz_esperada_da_F2']['celulas'] as $c ) {
	if ( ! empty( $c['eliminados_por_ambiente_do_produto'] ) ) {
		$celulas_amb_produto[ $c['base'] . '|' . $c['ambiente'] ] = (array) $c['eliminados_por_ambiente_do_produto'];
	}
}
f2_ok( count( $celulas_amb_produto ) > 0,
	'a regra 3 morde em pelo menos uma celula da matriz — regra que nunca morde nao foi medida',
	count( $celulas_amb_produto ) . ' celulas base x lugar' );

$faltam_no_balde   = array();
$sobram_no_balde   = array();
$frases_fundidas   = array();
$sem_o_literal     = array();
$negam_que_ele_fala = array();
$no_silencio_errado = array();
foreach ( $celulas_amb_produto as $chave => $esperados ) {
	list( $b_, $a_ ) = explode( '|', $chave );
	$html_ = f2_render( $raiz, 'base=' . $b_ . '&onde=' . $a_ . '&caco=' . $CAQUINHO_LIVRE );
	$corpo_ = f2_corpo( $html_ );
	$blocos = preg_match_all( '#<p class="cdm-f2-ambiente-do-produto">(.*?)</p>#is', $corpo_, $mb )
		? $mb[1] : array();
	$texto_balde = f2_texto( implode( ' ', $blocos ) );
	/* A celula com tessela nao e a celula de declaracao: a regra 7 e a 6 podem ter
	   tirado um dos esperados ANTES — mas elas rodam DEPOIS da 3, entao quem a 3
	   pegou nao pode ter sido movido por nenhuma das duas. Por isso a lista
	   esperada aqui e a da matriz, inteira. */
	foreach ( $esperados as $id ) {
		$nome_ = f2_nome_esperado( $por_id[ $id ] );
		if ( false === mb_strpos( $texto_balde, $nome_ ) ) {
			$faltam_no_balde[] = $chave . ' / ' . $nome_;
			continue;
		}
		/* O LITERAL DO FABRICANTE, e e esta a afirmacao que a regra existe para
		   sustentar (26.3): ao menos um dos literais de `ambientes_declarados`
		   daquele produto tem de estar na tela. */
		$achou_literal = false;
		foreach ( $LITERAIS_DELIM[ $id ] as $lit ) {
			if ( false !== mb_strpos( $texto_balde, $lit ) ) {
				$achou_literal = true;
			}
		}
		if ( ! $achou_literal ) {
			$sem_o_literal[] = $chave . ' / ' . $nome_;
		}
	}
	/* E O OUTRO SENTIDO, que e o que impede o balde de encher roubando do silencio. */
	foreach ( $por_id as $id => $m ) {
		if ( in_array( $id, $esperados, true ) ) {
			continue;
		}
		if ( false !== mb_strpos( $texto_balde, f2_nome_esperado( $m ) ) ) {
			$sobram_no_balde[] = $chave . ' / ' . f2_nome_esperado( $m );
		}
	}
	/* A PALAVRA PROIBIDA NESTE BLOCO. Ela e a frase do balde do silencio, e sair
	   dentro deste paragrafo seria o defeito consertado voltando com outra
	   formatacao: dizer "ele nao fala" de uma superficie que ele declara. */
	if ( '' !== $texto_balde && false !== mb_strpos( $texto_balde, 'não fala desta superfície' ) ) {
		$negam_que_ele_fala[] = $chave;
	}
	/* AS DUAS FRASES DE AMBIENTE TEM DE SER DIFERENTES, E ESTA LINHA NASCEU DE UMA
	   MUTACAO QUE PASSOU. A t05 da `mutacoes-ambiente-do-produto.py` troca a frase do
	   balde da regra 3 pela da regra 8, palavra por palavra — e a bancada ficou VERDE,
	   porque tudo o que ela media era a PRESENCA do nome do produto e do literal, e os
	   dois continuam ali. Juntar as duas frases e exatamente o que o PROMPT.md deste
	   bloco proibiu com todas as letras, e era a unica coisa que nenhuma afirmacao olhava.
	   A regua e a frase CARACTERISTICA de cada balde, nas duas direcoes: a da 3 fala do
	   PRODUTO, a da 8 fala da frase que nomeia o SUBSTRATO. */
	if ( '' !== $texto_balde ) {
		if ( false !== mb_strpos( $texto_balde, 'declara com o lugar dentro da frase' ) ) {
			$frases_fundidas[] = $chave . ' (a 3 usando a frase da 8)';
		}
		if ( false === mb_strpos( $texto_balde, 'delimitou o produto inteiro' ) ) {
			$frases_fundidas[] = $chave . ' (a 3 sem a frase propria dela)';
		}
	}
	$blocos_8 = preg_match_all( '#<p class="cdm-f2-ambiente-substrato">(.*?)</p>#is', $corpo_, $m8 )
		? f2_texto( implode( ' ', $m8[1] ) ) : '';
	if ( '' !== $blocos_8 && false !== mb_strpos( $blocos_8, 'delimitou o produto inteiro' ) ) {
		$frases_fundidas[] = $chave . ' (a 8 usando a frase da 3)';
	}
	/* E A CONFERENCIA CRUZADA: nenhum dos eliminados por ambiente do produto pode
	   aparecer no paragrafo do SILENCIO da cola. A secao 7 ja mede isso pela lista
	   da matriz; aqui ela e medida pelo balde, que e o outro caminho para o mesmo
	   fato — duas metades que nao se apoiam uma na outra. */
	$fora_html_ = preg_match( '#<div class="cdm-f2-secao cdm-f2-fora">(.*?)</div>#is', $corpo_, $mf )
		? $mf[1] : '';
	$sil_ = preg_match( '#<p class="cdm-f2-silencio">(.*?)</p>#is', $fora_html_, $msx )
		? f2_texto( $msx[1] ) : '';
	foreach ( $esperados as $id ) {
		if ( '' !== $sil_ && false !== mb_strpos( $sil_, f2_nome_esperado( $por_id[ $id ] ) ) ) {
			$no_silencio_errado[] = $chave . ' / ' . f2_nome_esperado( $por_id[ $id ] );
		}
	}
}
f2_ok( empty( $faltam_no_balde ),
	'todo produto que a matriz poe no balde da regra 3 sai NOMEADO no bloco dele',
	empty( $faltam_no_balde ) ? count( $celulas_amb_produto ) . ' celulas conferidas'
		: implode( '; ', array_slice( $faltam_no_balde, 0, 4 ) ) );
f2_ok( empty( $sobram_no_balde ),
	'e ninguem mais aparece nele — balde que enche roubando do silencio troca uma causa pela outra',
	empty( $sobram_no_balde ) ? count( $celulas_amb_produto ) . ' celulas conferidas nos dois sentidos'
		: implode( '; ', array_slice( $sobram_no_balde, 0, 4 ) ) );
f2_ok( empty( $sem_o_literal ),
	'a frase cita o literal de `ambientes_declarados` do fabricante, nao o nosso vocabulario',
	empty( $sem_o_literal ) ? count( $celulas_amb_produto ) . ' celulas conferidas'
		: implode( '; ', array_slice( $sem_o_literal, 0, 4 ) ) );
f2_ok( empty( $negam_que_ele_fala ),
	'GRAVE: o bloco da regra 3 nunca diz que o fabricante nao fala da superficie que ele declara',
	empty( $negam_que_ele_fala ) ? count( $celulas_amb_produto ) . ' celulas conferidas'
		: implode( ', ', array_slice( $negam_que_ele_fala, 0, 4 ) ) );
f2_ok( empty( $no_silencio_errado ),
	'GRAVE: e nenhum deles continua no paragrafo do silencio — era exatamente ali que eles estavam',
	empty( $no_silencio_errado ) ? count( $celulas_amb_produto ) . ' celulas conferidas'
		: implode( '; ', array_slice( $no_silencio_errado, 0, 4 ) ) );
f2_ok( empty( $frases_fundidas ),
	'GRAVE: as frases dos DOIS baldes de ambiente sao diferentes, nas duas direcoes',
	empty( $frases_fundidas ) ? count( $celulas_amb_produto ) . ' celulas conferidas, a frase de cada balde e a dele'
		: implode( '; ', array_slice( $frases_fundidas, 0, 4 ) ) );

/* OS DOIS BALDES DE AMBIENTE NA MESMA PAGINA, e e a afirmacao que impede a fusao
   deles: a celula alvenaria x externo_abrigado tem a cimentcola no balde da regra 8
   e NENHUM produto no da regra 3, e as duas frases sao diferentes palavra por
   palavra. Se alguem juntar os dois baldes num so, esta linha fica vermelha. */
$t_dois = f2_corpo( f2_render( $raiz,
	'base=alvenaria_tijolo&onde=externo_abrigado&caco=' . $CAQUINHO_LIVRE ) );
f2_ok( false !== mb_strpos( $t_dois, 'cdm-f2-ambiente-substrato' )
	&& false === mb_strpos( $t_dois, 'cdm-f2-ambiente-do-produto' ),
	'os dois baldes de ambiente nao se cruzam: onde a regra 8 morde, a 3 nao escreve nada',
	'alvenaria_tijolo x externo_abrigado' );

/* E O LADO QUE A REGRA DEIXA PASSAR, que e a trava que impede a regra 3 de tirar o
   produto do ambiente que o fabricante DECLARA: mesma base, trocando so o lugar
   para o que os dois Cascola nomeiam. */
$t_passa = f2_corpo( f2_render( $raiz, 'base=mdf_madeira&onde=interno_seco&caco=' . $CAQUINHO_LIVRE ) );
f2_ok( '' !== $t_passa && false === mb_strpos( $t_passa, 'cdm-f2-ambiente-do-produto' ),
	'no lugar que o fabricante declara, o balde da regra 3 fica VAZIO — senao a regra morde sempre',
	'mdf_madeira x interno_seco' );

/* ---------------------------------------------------------------------------
 * Fecho
 * ------------------------------------------------------------------------- */

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

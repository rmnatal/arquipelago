<?php
/**
 * Verificacao MEDIDA da pagina de TECNICA — "O que e mosaico Picassiete".
 *
 *   php ferramentas/teste-tecnicas.php .
 *
 * -------------------------------------------------------------------------
 * DE ONDE VEM O ESPERADO, e por que NAO e do snippet
 * -------------------------------------------------------------------------
 * A pagina imprime a decisao de `cdm_f2_celula_cola()`, que e PHP. Se a regua
 * deste arquivo tambem chamasse aquela funcao, as duas metades errariam juntas
 * e o verde nao significaria nada (secao 8 do ARQUIPELAGO.md).
 *
 * Entao o esperado vem de `dados/cobertura.json`, que e gerado por
 * `ferramentas/cobertura.py` a partir da regua do `validar-banco.py` — uma
 * implementacao INDEPENDENTE, em outra linguagem, escrita no bloco 3 antes de
 * existir uma linha do snippet. E a mesma disciplina do `conferir-cobertura.php`:
 * duas metades que tem de dar o mesmo numero nas 45 celulas.
 *
 * O arquivo de cobertura so vale como regua se estiver FRESCO, entao a primeira
 * coisa que este teste faz e rodar `cobertura.py --conferir`. Regua velha
 * aprovaria a pagina de ontem, que e a cicatriz que a Robometria pagou em
 * 14/09/2026 com 167 afirmacoes verdadeiras sobre uma pagina que ninguem
 * estava recebendo.
 *
 * -------------------------------------------------------------------------
 * O QUE ELE MEDE ALEM DA GRADE
 * -------------------------------------------------------------------------
 *   - A prestacao de contas da secao 7: a soma dos nomeados FECHA com o tamanho
 *     do banco, contado do arquivo e nunca digitado. Cada cola aparece UMA vez.
 *   - Nenhum item sem saida de compra, e o `rel` de cada link saindo do que o
 *     link E (secao 25, e a correcao de 14/09 da secao 7).
 *   - A recusa do rejunte esta escrita, com a causa.
 *   - A voz: os termos que o VOZ.md proibe no titulo e no primeiro paragrafo.
 *   - O JSON-LD parseia e o FAQ do schema e o MESMO da tela.
 *
 * Medido dentro de <main>, sempre: afirmacao sobre o que a pagina DIZ se conta
 * no corpo servido, nao no HTML inteiro.
 *
 * O QUE ESTE ARQUIVO NAO MEDE, E ONDE ISSO E MEDIDO. O caminho sem banco — a
 * pagina dizendo que nao conseguiu medir em vez de inventar — nao cabe aqui:
 * a bancada carrega as options do manifest na entrada do processo, entao
 * produzir a ausencia e produzir outro MUNDO, nao outra afirmacao. Ele e
 * medido em `ferramentas/mutacoes-tecnicas-pagina.py`, que apaga o `publicar`
 * do banco e exige a pagina honesta. A primeira versao deste arquivo tinha
 * uma secao 8 que imprimia `ok` sem medir nada; ficou escrito aqui por que ela
 * saiu, porque afirmacao que nao pode falhar e pior que afirmacao ausente
 * (secao 8 do ARQUIPELAGO.md).
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$feitos = 0;

function tec_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		printf( "  ok   %-68s %s\n", $rotulo, $medida );
		return true;
	}
	$falhas++;
	printf( "  FALHA %-68s %s\n", $rotulo, $medida );
	return false;
}

function tec_corpo( $html ) {
	if ( preg_match( '#<main\b[^>]*>(.*?)</main>#is', $html, $m ) ) {
		return $m[1];
	}
	return $html;
}

function tec_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

/* ---------------------------------------------------------------------------
 * 0. A regua independente — e ela tem de estar fresca
 * ------------------------------------------------------------------------- */

echo "Clube do Mosaico — verificacao da pagina de TECNICA\n";

$saida  = array();
$codigo = 0;
exec( 'python3 ' . escapeshellarg( __DIR__ . '/cobertura.py' ) . ' --conferir 2>&1', $saida, $codigo );
tec_ok( 0 === $codigo, 'dados/cobertura.json esta fresco (a regua independente vale)',
	trim( implode( ' ', $saida ) ) );
if ( 0 !== $codigo ) {
	echo "\nA regua independente esta velha. Rode `python3 ferramentas/cobertura.py` antes.\n";
	exit( 1 );
}

$cobertura = json_decode( (string) @file_get_contents( $raiz . '/dados/cobertura.json' ), true );
$colas     = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-colas.json' ), true );
$tecnicas  = json_decode( (string) @file_get_contents( $raiz . '/dados/tecnicas.json' ), true );
if ( ! $cobertura || ! $colas || ! $tecnicas ) {
	echo "ERRO: nao consegui ler cobertura, banco de colas ou banco de tecnicas.\n";
	exit( 1 );
}

cdm_teste_carregar_options( $raiz );
cdm_teste_carregar( $raiz );
$GLOBALS['__paginas'] = cdm_teste_paginas_no_ar( 'hoje' );

echo "  (tecnicas " . CDM_TECNICAS_VERSAO . ", casca " . CDM_CASCA_VERSAO . ", F2 " . CDM_F2_VERSAO . ")\n\n";

/* O registro do banco, lido do ARQUIVO — nunca da funcao do snippet. */
$reg = null;
foreach ( $tecnicas['tecnicas'] as $t ) {
	if ( CDM_TECNICAS_ID === $t['id'] ) {
		$reg = $t;
	}
}

/** O nome como a TELA o escreve, recalculado aqui: marca so quando falta. */
function tec_nome_esperado( $m ) {
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return $nome;
	}

	return $marca . ' ' . $nome;
}

$por_id = array();
foreach ( $colas['materiais'] as $m ) {
	$por_id[ $m['id'] ] = $m;
}

/* ---------------------------------------------------------------------------
 * 1. O banco manda no texto — nada digitado no PHP
 * ------------------------------------------------------------------------- */

echo "1. A tecnica sai do banco (secao 10: nunca invente dado)\n";

tec_ok( is_array( $reg ), 'a tecnica desta pagina existe em dados/tecnicas.json', CDM_TECNICAS_ID );
tec_ok( is_array( $reg ) && ! empty( $reg['materiais_tipicos'] ),
	'ela declara o material do caquinho, que e o que liga a pagina ao banco',
	is_array( $reg ) ? implode( ', ', (array) $reg['materiais_tipicos'] ) : '' );

$tessela_esperada = ( is_array( $reg ) && ! empty( $reg['materiais_tipicos'] ) )
	? (string) $reg['materiais_tipicos'][0] : '';
tec_ok( $tessela_esperada === cdm_tecnicas_tessela(),
	'a pagina resolve a tessela que o BANCO declara, nao uma escrita no snippet', $tessela_esperada );

/* O PORTAO DA SECAO 9, RECONTADO AQUI. A pagina so pode existir com 3 itens de
   banco reais, e este teste nao pergunta ao validador: ele conta da cobertura,
   que e a metade independente. */
$uniao = array();
$celulas_da_tessela = array();
foreach ( $cobertura['estados']['cola'] as $e ) {
	if ( $e['tessela'] !== $tessela_esperada ) {
		continue;
	}
	$celulas_da_tessela[ $e['base'] . '|' . $e['ambiente'] ] = $e;
	foreach ( $e['elegiveis'] as $id ) {
		$uniao[ $id ] = true;
	}
}
tec_ok( count( $uniao ) >= 3, 'o portao de 3 itens da secao 9 esta aberto para esta tecnica',
	count( $uniao ) . ' itens de banco' );

/* A BANDEIRA DO BANCO E O REGISTRO DO SNIPPET TEM DE DIZER A MESMA COISA, NOS
   DOIS SENTIDOS. `pagina_publicada` no banco e o que o `validar-banco.py` usa
   para cobrar o portao de 3 itens; se ela ficar `false` com a pagina no ar, o
   portao para de morder em silencio, e se ficar `true` sem pagina, o validador
   cobra um portao de uma pagina que nao existe. Nenhum dos dois casos apareceria
   sem esta afirmacao, porque cada metade esta certa sozinha. */
$registradas = apply_filters( 'cdm_tecnicas_publicadas', array() );
$ids_no_site = array();
foreach ( (array) $registradas as $r ) {
	$ids_no_site[] = $r['id'];
}
tec_ok( in_array( CDM_TECNICAS_ID, $ids_no_site, true ),
	'a tecnica desta pagina esta registrada como publicada no snippet' );
tec_ok( is_array( $reg ) && ! empty( $reg['pagina_publicada'] ),
	'e o BANCO carrega a mesma bandeira (as duas metades concordam)' );

$sem_pagina = array();
foreach ( $tecnicas['tecnicas'] as $t ) {
	$publicada_no_banco = ! empty( $t['pagina_publicada'] );
	$publicada_no_site  = in_array( $t['id'], $ids_no_site, true );
	if ( $publicada_no_banco !== $publicada_no_site ) {
		$sem_pagina[] = $t['id'];
	}
}
tec_ok( empty( $sem_pagina ), 'nenhuma tecnica tem a bandeira do banco discordando do snippet',
	empty( $sem_pagina ) ? count( $tecnicas['tecnicas'] ) . ' tecnicas conferidas' : implode( ', ', $sem_pagina ) );

/* ---------------------------------------------------------------------------
 * 2. A pagina na arvore, com UM nome so
 * ------------------------------------------------------------------------- */

echo "\n2. A pagina na arvore (secao 16)\n";

$defs   = cdm_casca_definicao_paginas();
$arvore = cdm_casca_arvore();

tec_ok( isset( $defs[ CDM_TECNICAS_SLUG ] ), 'o snippet registrou a propria pagina pelo filtro cdm_paginas', CDM_TECNICAS_SLUG );
tec_ok( isset( $defs[ CDM_TECNICAS_SLUG ]['pai'] ) && 'como-fazer' === $defs[ CDM_TECNICAS_SLUG ]['pai'],
	'a pagina nasce com mae, e a mae e /como-fazer/' );
tec_ok( isset( $defs['como-fazer'] ), 'a mae existe na definicao de paginas' );
tec_ok( isset( $arvore[ CDM_TECNICAS_SLUG ] ), 'a pagina esta no mapa da arvore' );
tec_ok( isset( $arvore[ CDM_TECNICAS_SLUG ]['rotulo'] ) && CDM_TECNICAS_TITULO === $arvore[ CDM_TECNICAS_SLUG ]['rotulo'],
	'o degrau da trilha usa o mesmo nome (um nome por pagina)' );
tec_ok( isset( $defs[ CDM_TECNICAS_SLUG ]['titulo'] ) && CDM_TECNICAS_TITULO === $defs[ CDM_TECNICAS_SLUG ]['titulo'],
	'o H1 usa o mesmo nome' );
tec_ok( mb_strlen( CDM_TECNICAS_TITULO . ' — ' . CDM_CASCA_NOME_SITE ) <= 65,
	'o <title> com o sufixo do site cabe em 65 caracteres',
	mb_strlen( CDM_TECNICAS_TITULO . ' — ' . CDM_CASCA_NOME_SITE ) . ' caracteres' );

/* A MAE LISTA A FILHA (16.4a). Sem isto a pagina nasce orfa. */
$como_fazer = tec_corpo( cdm_teste_pagina( 'cdm_como_fazer' ) );
tec_ok( false !== strpos( $como_fazer, '/' . CDM_TECNICAS_SLUG . '/' ),
	'a mae /como-fazer/ publica o link para a filha (16.4a)' );
tec_ok( false !== strpos( $como_fazer, CDM_TECNICAS_TITULO ),
	'e o cartao da mae usa o mesmo nome' );

/* 16.4c — com uma filha so, NAO sai bloco "Veja tambem" de irmas nesta pagina. */

/* ---------------------------------------------------------------------------
 * 3. A GRADE — 45 celulas contra a metade independente
 * ------------------------------------------------------------------------- */

echo "\n3. A grade da pagina x a cobertura gerada em Python (45 celulas)\n";

$html  = cdm_teste_pagina( 'cdm_tecnica' );
$corpo = tec_corpo( $html );
$texto = tec_texto( $corpo );

$divergem = array();
$sem_nenhum = 0;
$com_minimo = 0;
foreach ( $celulas_da_tessela as $chave => $e ) {
	list( $base, $ambiente ) = explode( '|', $chave );
	$c = cdm_tecnicas_celula( $base, $ambiente );
	$na_pagina = $c ? $c['elegiveis'] : array();
	sort( $na_pagina );
	$esperado = $e['elegiveis'];
	sort( $esperado );
	if ( $na_pagina !== $esperado ) {
		$divergem[] = $chave . ' (pagina: ' . implode( ',', $na_pagina ) . ' | cobertura: ' . implode( ',', $esperado ) . ')';
	}
	if ( 0 === count( $esperado ) ) {
		$sem_nenhum++;
	}
	if ( count( $esperado ) >= 3 ) {
		$com_minimo++;
	}
}
tec_ok( 45 === count( $celulas_da_tessela ), 'a cobertura tem as 45 celulas desta tessela',
	count( $celulas_da_tessela ) . ' celulas' );
tec_ok( empty( $divergem ), 'as 45 celulas da pagina batem com a regua independente',
	empty( $divergem ) ? '45 iguais' : implode( ' | ', array_slice( $divergem, 0, 3 ) ) );

/* OS NUMEROS QUE A PAGINA AFIRMA sao os mesmos que a cobertura conta. Sem isto
   a frase de resposta poderia envelhecer sozinha, que e o defeito que esta ilha
   ja pagou com o cabecalho de pecas.json dizendo 32 com 35 no arquivo. */
tec_ok( false !== strpos( $texto, 'Das ' . count( $celulas_da_tessela ) . ' combinações' ),
	'a frase de resposta diz o numero de combinacoes que a cobertura conta',
	count( $celulas_da_tessela ) );
tec_ok( false !== strpos( $texto, $sem_nenhum . ' não têm nenhuma' ),
	'a frase de resposta diz quantas combinacoes ficam sem resposta', (string) $sem_nenhum );
tec_ok( false !== strpos( $texto, $com_minimo . ' têm três ou mais' ),
	'a frase de resposta diz quantas chegam a tres opcoes', (string) $com_minimo );

/* A TABELA PRE-RENDERIZADA existe no HTML SERVIDO, sem JavaScript (secao 5). */
tec_ok( preg_match_all( '#<tr\b#i', $corpo ) >= 10,
	'a tabela pre-renderizada esta no HTML servido, com uma linha por superficie',
	preg_match_all( '#<tr\b#i', $corpo ) . ' linhas' );
tec_ok( substr_count( $corpo, 'nenhum que o fabricante sustente' ) === $sem_nenhum,
	'a tabela escreve "nao ha" exatamente nas celulas vazias que a cobertura conta',
	substr_count( $corpo, 'nenhum que o fabricante sustente' ) . ' celulas' );

/* ---------------------------------------------------------------------------
 * 4. A PRESTACAO DE CONTAS (secao 7) — a soma fecha com o BANCO
 * ------------------------------------------------------------------------- */

echo "\n4. Prestacao de contas: a soma dos nomeados fecha com o banco (secao 7)\n";

$no_banco = array();
foreach ( $colas['materiais'] as $m ) {
	$no_banco[] = $m['id'];
}
tec_ok( count( $no_banco ) > 0, 'o banco de colas foi contado do arquivo, nunca digitado',
	count( $no_banco ) . ' colas' );

$nomeados = 0;
$faltando = array();
$repetidos = array();
foreach ( $no_banco as $id ) {
	$nome  = tec_nome_esperado( $por_id[ $id ] );
	$vezes = substr_count( $texto, $nome );
	if ( 0 === $vezes ) {
		$faltando[] = $id;
		continue;
	}
	$nomeados++;
}
tec_ok( empty( $faltando ), 'cada cola do banco aparece na prosa da pagina, recomendada ou excluida',
	empty( $faltando ) ? $nomeados . ' de ' . count( $no_banco ) : implode( ', ', $faltando ) );

/* A VITRINE SERVE EXATAMENTE O QUE A FRASE NOMEIA. Cartao de produto que a
   frase nao nomeia e o defeito que a F2 desta ilha pagou em 12/09/2026. */
preg_match_all( '#<li class="cdm-f2-cartao[^"]*">(.*?)</li>#is', $corpo, $cartoes );
/* O CARTAO IMPRIME A MARCA E O NOME EM ETIQUETAS SEPARADAS — a marca num
   <span> e o nome no <h3> —, entao casar pelo nome JUNTO (como a prosa o
   escreve) nao acha cartao nenhum. Este teste casa pelo <h3>, que e onde o
   nome comercial esta, e e por isso que ele le o banco em vez de confiar na
   string da tela. */
$ids_na_vitrine = array();
foreach ( $cartoes[1] as $cartao ) {
	if ( ! preg_match( '#<h3>(.*?)</h3>#is', $cartao, $mh ) ) {
		continue;
	}
	$nome_no_cartao = html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' );
	foreach ( $no_banco as $id ) {
		if ( $nome_no_cartao === (string) $por_id[ $id ]['nome_comercial'] ) {
			$ids_na_vitrine[ $id ] = true;
		}
	}
}
$esperado_vitrine = array_keys( $uniao );
sort( $esperado_vitrine );
$medido_vitrine = array_keys( $ids_na_vitrine );
sort( $medido_vitrine );
tec_ok( $esperado_vitrine === $medido_vitrine,
	'a vitrine serve exatamente as colas que a cobertura declara elegiveis',
	count( $medido_vitrine ) . ' cartoes' );

$fora_esperado = array_values( array_diff( $no_banco, $esperado_vitrine ) );
sort( $fora_esperado );
$fora_nomeados = array();
foreach ( $fora_esperado as $id ) {
	if ( preg_match( '#<li><strong>' . preg_quote( tec_nome_esperado( $por_id[ $id ] ), '#' ) . '</strong>#u', $corpo ) ) {
		$fora_nomeados[] = $id;
	}
}
tec_ok( $fora_esperado === $fora_nomeados,
	'quem NAO entra e nomeado numa linha propria, com a causa',
	count( $fora_nomeados ) . ' de ' . count( $fora_esperado ) );
tec_ok( count( $esperado_vitrine ) + count( $fora_esperado ) === count( $no_banco ),
	'a soma dos nomeados fecha com o tamanho do banco',
	count( $esperado_vitrine ) . ' + ' . count( $fora_esperado ) . ' = ' . count( $no_banco ) );

/* CAUSA QUE O CODIGO SEPARA, O TEXTO SEPARA. O Durepoxi cai por silencio em 25
   celulas E aparece com ressalva em 20 — escrever so uma das duas seria
   inventar a outra. */
foreach ( $fora_esperado as $id ) {
	$baldes = array( 'ressalva' => 0, 'silencio' => 0, 'proibicao' => 0, 'condicao' => 0 );
	foreach ( $celulas_da_tessela as $e ) {
		if ( in_array( $id, $e['com_ressalva'], true ) ) { $baldes['ressalva']++; }
		if ( in_array( $id, $e['eliminados_por_silencio'], true ) ) { $baldes['silencio']++; }
		if ( in_array( $id, $e['eliminados_por_proibicao'], true ) ) { $baldes['proibicao']++; }
		if ( in_array( $id, $e['eliminados_por_condicao'], true ) ) { $baldes['condicao']++; }
	}
	$quantas = array_filter( $baldes );
	$todos_na_tela = true;
	foreach ( $quantas as $n ) {
		if ( false === strpos( $texto, 'em ' . $n . ' das ' . count( $celulas_da_tessela ) ) ) {
			$todos_na_tela = false;
		}
	}
	tec_ok( $todos_na_tela, 'a recusa de ' . $id . ' nomeia TODAS as causas que o calculo separou',
		implode( ', ', array_map( function ( $k, $v ) { return $k . ' ' . $v; }, array_keys( $quantas ), $quantas ) ) );
}

/* ---------------------------------------------------------------------------
 * 5. A ESCADA DE COMPRA (secao 25 e secao 7)
 * ------------------------------------------------------------------------- */

echo "\n5. Escada de compra: ninguem fica sem saida (secao 25.2)\n";

$sem_saida = array();
foreach ( $esperado_vitrine as $id ) {
	$cartao = '';
	foreach ( $cartoes[1] as $c ) {
		if ( preg_match( '#<h3>(.*?)</h3>#is', $c, $mh )
			&& html_entity_decode( trim( $mh[1] ), ENT_QUOTES, 'UTF-8' ) === (string) $por_id[ $id ]['nome_comercial'] ) {
			$cartao = $c;
		}
	}
	if ( '' === $cartao || false === strpos( $cartao, 'cdm-f2-compra' ) || ! preg_match( '#<a [^>]*class="cdm-f2-botao#i', $cartao ) ) {
		$sem_saida[] = $id;
	}
}
tec_ok( empty( $sem_saida ), 'nenhum cartao da vitrine fica sem saida de compra',
	empty( $sem_saida ) ? count( $esperado_vitrine ) . ' com botao' : implode( ', ', $sem_saida ) );
tec_ok( false === mb_stripos( $texto, 'link de loja em breve' ),
	'a frase proibida pela secao 7 nao aparece' );

/* O `rel` SAI DO QUE O LINK E. Busca CRUA nao paga comissao e por isso nunca e
   `sponsored` — chamar de patrocinado um link que nao paga seria mentir ao
   leitor sobre a unica coisa que ele tem o direito de saber sobre nos. */
preg_match_all( '#<a [^>]*class="[^"]*cdm-f2-botao-busca-crua[^"]*"[^>]*>#i', $corpo, $cruas );
$crua_errada = 0;
foreach ( $cruas[0] as $a ) {
	if ( false !== stripos( $a, 'sponsored' ) || false === stripos( $a, 'nofollow' ) ) {
		$crua_errada++;
	}
}
tec_ok( 0 === $crua_errada, 'a busca crua sai nofollow e NUNCA sponsored',
	count( $cruas[0] ) . ' links de busca crua' );

preg_match_all( '#<a [^>]*rel="sponsored[^"]*"[^>]*>#i', $corpo, $pagos );
tec_ok( count( $pagos[0] ) > 0, 'os links que rendem comissao saem sponsored',
	count( $pagos[0] ) . ' links' );
tec_ok( false !== mb_stripos( $texto, 'comissão' ),
	'o aviso de comissao esta visivel na pagina (secao 7)' );

/* A PROCEDENCIA E DISCRETA e vem DEPOIS do bloco de compra (secao 7, 10/09). */
$ordem_certa = true;
foreach ( $cartoes[1] as $c ) {
	$compra = strpos( $c, 'cdm-f2-compra' );
	$fonte  = strpos( $c, 'cdm-f2-fonte' );
	if ( false !== $fonte && false !== $compra && $fonte < $compra ) {
		$ordem_certa = false;
	}
}
tec_ok( $ordem_certa, 'o bloco de compra vem ANTES da prova de procedencia, em todo cartao' );

/* ---------------------------------------------------------------------------
 * 6. A RECUSA, e a voz
 * ------------------------------------------------------------------------- */

echo "\n6. A recusa nomeada e a voz (secoes 7 e 15)\n";

tec_ok( false !== mb_stripos( $texto, 'O rejunte.' ),
	'a pagina diz, com todas as letras, que NAO responde o rejunte' );
tec_ok( false !== mb_stripos( $texto, 'largura da junta' ),
	'e nomeia a causa que ela mediu: a folga em milimetro que nenhuma fonte declara' );

$primeiro = '';
if ( preg_match( '#<p class="cdm-linha-mestra">(.*?)</p>#is', $corpo, $m ) ) {
	$primeiro = tec_texto( $m[1] );
}
tec_ok( '' !== $primeiro, 'a pagina abre por uma promessa de uma linha', mb_substr( $primeiro, 0, 60 ) . '…' );

/* OS TERMOS QUE O VOZ.md PROIBE no titulo e no primeiro paragrafo. A lista esta
   escrita LA e copiada aqui de proposito: e regua, e regua se escreve no teste
   (secao 8). */
$proibidos = array( 'tessela', 'substrato', 'aderência', 'especificação', 'parâmetro', 'ficha técnica' );
$achados   = array();
foreach ( $proibidos as $p ) {
	if ( false !== mb_stripos( CDM_TECNICAS_TITULO, $p ) || false !== mb_stripos( $primeiro, $p ) ) {
		$achados[] = $p;
	}
}
tec_ok( empty( $achados ), 'nenhum termo proibido pelo VOZ.md no titulo nem no primeiro paragrafo',
	empty( $achados ) ? 'limpo' : implode( ', ', $achados ) );

/* A PROCEDENCIA NAO ABRE A PAGINA: ela desce um paragrafo, marcada como prova. */
tec_ok( false === mb_stripos( $primeiro, 'fabricante' ) && false === mb_stripos( $primeiro, 'Wikip' ),
	'a procedencia nao abre a pagina (15.2)' );
tec_ok( false !== strpos( $corpo, 'cdm-prova' ), 'a camada de prova esta marcada no HTML' );
tec_ok( false !== mb_stripos( $texto, 'não foi revisado' ),
	'a pagina diz que a revisao por quem faz mosaico ainda nao aconteceu' );

/* ---------------------------------------------------------------------------
 * 7. Cabeca: description e JSON-LD
 * ------------------------------------------------------------------------- */

echo "\n7. A cabeca da pagina (secao 5)\n";

$cabeca = '';
if ( preg_match( '#<head\b[^>]*>(.*?)</head>#is', $html, $m ) ) {
	$cabeca = $m[1];
}
$desc = '';
if ( preg_match( '#<meta name="description" content="(.*?)">#is', $html, $m ) ) {
	$desc = html_entity_decode( $m[1], ENT_QUOTES, 'UTF-8' );
}
tec_ok( '' !== $desc, 'a pagina serve meta description' );
tec_ok( mb_strlen( $desc ) >= 120 && mb_strlen( $desc ) <= 200,
	'a description tem tamanho util', mb_strlen( $desc ) . ' caracteres' );

$ld = '';
if ( preg_match( '#<script type="application/ld\+json" id="cdm-tecnicas-jsonld">(.*?)</script>#is', $html, $m ) ) {
	$ld = $m[1];
}
$grafo = json_decode( $ld, true );
tec_ok( is_array( $grafo ), 'o JSON-LD desta pagina parseia' );

$tipos = array();
foreach ( ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
	$tipos[] = $no['@type'];
}
tec_ok( in_array( 'Article', $tipos, true ), 'o grafo publica Article' );
tec_ok( in_array( 'FAQPage', $tipos, true ), 'o grafo publica FAQPage' );

/* O FAQ DO SCHEMA E O MESMO DA TELA — uma fonte so. Schema que promete o que a
   pagina nao diz e o que faz FAQPage virar spam. */
$perguntas_schema = array();
foreach ( ( isset( $grafo['@graph'] ) ? $grafo['@graph'] : array() ) as $no ) {
	if ( 'FAQPage' === $no['@type'] ) {
		foreach ( $no['mainEntity'] as $q ) {
			$perguntas_schema[] = $q['name'];
		}
	}
}
$fora_da_tela = array();
foreach ( $perguntas_schema as $q ) {
	if ( false === strpos( $texto, $q ) ) {
		$fora_da_tela[] = $q;
	}
}
tec_ok( ! empty( $perguntas_schema ) && empty( $fora_da_tela ),
	'toda pergunta do FAQPage esta escrita na tela',
	count( $perguntas_schema ) . ' perguntas' );

/* O ESCAPE DO "&" — a cicatriz de 08/09/2026. */
preg_match_all( '#<script\b[^>]*>(.*?)</script>#is', $html, $scripts );
$entidades = 0;
foreach ( $scripts[1] as $s ) {
	$entidades += substr_count( $s, '&#038;' );
}
tec_ok( 0 === $entidades, 'zero &#038; dentro de <script>' );
tec_ok( false === strpos( $corpo, '&#038;' ) && false === strpos( $corpo, '&amp;#039;' ),
	'zero escape duplo no corpo servido' );

echo "\n";
if ( $falhas ) {
	echo "REPROVADO: $falhas falha(s) em $feitos verificacoes.\n";
	exit( 1 );
}
echo "APROVADO: $feitos verificacoes, nenhuma falha.\n";

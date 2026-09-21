<?php
/**
 * Verificacao MEDIDA da MALHA DE PECAS — bloco 5b, secoes 9, 13, 14.9 e 16.
 *
 *   php ferramentas/teste-malha.php .
 *
 * O QUE ESTA BANCADA COBRA QUE NENHUMA OUTRA COBRA
 * ------------------------------------------------
 * O teste-arvore.php ja mede trilha, BreadcrumbList, cluster, pagina fina e
 * orfandade, e desde 21/09/2026 ele mede isso nas cinco paginas novas tambem,
 * porque a lista de alvos dele virou derivada. O que sobra, e e o que esta aqui:
 *
 *   1. AS FRASES DAS DUAS IMPLEMENTACOES SAO A MESMA FRASE. O PHP escreve
 *      acentuado e a referencia escreve em ASCII; a comparacao ignora acento,
 *      como no teste-r1.php. Sem isto, as duas metades divergem caladas — que e
 *      o defeito que esta ilha ja pagou em cinco lugares diferentes.
 *   2. O PORTAO DE DADO DA SECAO 13 E DA 16.5, CONTADO NO BANCO. Categoria com
 *      menos de tres filhas de dado real nao pode estar publicada, e filha com
 *      menos de tres itens tambem nao. A conta e refeita aqui a partir de
 *      dados/pecas.json, por um caminho que NAO e o do gerador.
 *   3. CARTAO DE CATEGORIA QUE NAO EXISTE NAO PUBLICA CONTAGEM (16.5), e diz
 *      "em breve". Contagem ali e promessa datada.
 *   4. OS DOIS COMPROMISSOS DA 14.9 ESTAO ESCRITOS NO PROPRIO ARQUIVO: consulta
 *      e por_que_top10, em toda pagina do registro.
 *   5. A PORTA DE COMPRA VEM ANTES DA PROCEDENCIA (secao 7), e o aviso de
 *      comissao mora dentro do bloco de compra.
 *   6. NENHUMA PAGINA SERVE O ESTADO DEGRADADO ("estamos sem o banco"), que e
 *      uma pagina valida com cabecalho e rodape — foi medindo tres desses que a
 *      varredura de corpo desta ilha deu verde sobre paginas de 1.100
 *      caracteres.
 *
 * UM PROCESSO POR PAGINA, pela mesma razao do teste-arvore.php: a trilha tem
 * trava `static` por requisicao, e um varredor que monta cinco paginas em
 * sequencia mede a trilha na primeira e o vazio nas outras quatro, com o teste
 * verde.
 */

require __DIR__ . '/render-para-teste.php';

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

/* ---------------------------------------------------------------------------
 * O MUNDO SEM BANCO, num processo proprio (secao 9 deste arquivo).
 *
 * Ele roda ANTES de tudo e imprime uma pagina so: a option dos fatos e retirada
 * depois de carregada, e o que se mede e a pagina que o site serviria se o Sync
 * nunca tivesse levado dados/malha-pecas.json. Precisa ser outro processo
 * porque as options sao globais e o caminho de medicao ja as carregou.
 * ------------------------------------------------------------------------- */
if ( in_array( '--mundo-sem-banco', $argv, true ) ) {
	robometria_teste_carregar_options( $raiz );
	unset( $GLOBALS['__options']['robometria_dados_malha-pecas'] );
	unset( $GLOBALS['__options']['robometria_sync_estado']['itens']['dados:malha-pecas'] );
	robometria_teste_carregar( $raiz );
	$GLOBALS['__paginas'] = robometria_teste_paginas_do_site();
	echo robometria_teste_pagina( 'robometria_pecas_filtros_xiaomi',
		'Robometria — teste', 'pecas-filtros-xiaomi' );
	exit( 0 );
}

$falhas = 0;
$feitos = 0;

function mal_ok( $condicao, $rotulo, $medida = '' ) {
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

/** So o miolo: e sobre o CORPO que valem as afirmacoes de texto. */
function mal_corpo( $html ) {
	return preg_match( '#<main\b[^>]*>(.*)</main>#is', $html, $m ) ? $m[1] : '';
}

/** O texto que um leitor le: sem marcacao, sem entidade, espacos normalizados. */
function mal_texto( $html ) {
	$texto = html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' );
	return trim( preg_replace( '/\s+/u', ' ', $texto ) );
}

/**
 * A NORMALIZACAO DA COMPARACAO: sem acento e com o sinal de multiplicacao
 * virando "x".
 *
 * O acento sai porque o banco e a referencia sao ASCII e a tela e acentuada
 * (fase 4b do playbook). O "×" sai porque e a mesma decisao um passo adiante: a
 * tela publica o sinal tipografico e a referencia escreve a letra, e comparar os
 * dois como se fossem caracteres diferentes obrigaria a referencia a carregar
 * tipografia — que e trabalho de tela, nao de regra.
 */
function mal_normalizar( $t ) {
	$t = str_replace( array( '×', '–', '—' ), array( 'x', '-', '-' ), (string) $t );
	$t = iconv( 'UTF-8', 'ASCII//TRANSLIT', $t );
	return trim( preg_replace( '/\s+/', ' ', mb_strtolower( (string) $t, 'UTF-8' ) ) );
}

robometria_teste_carregar_options( $raiz );
robometria_teste_carregar( $raiz );
$GLOBALS['__paginas'] = robometria_teste_paginas_do_site();

echo "Robometria — verificacao da malha de pecas, snippet " . ROBOMETRIA_MALHA_VERSAO . "\n\n";

$registro = robometria_malha_paginas();
$chaves   = array_keys( $registro );

/* ---------------------------------------------------------------------------
 * 0. O registro e coerente consigo mesmo
 * ------------------------------------------------------------------------- */

echo "0. O registro das paginas\n";
mal_ok( count( $chaves ) >= 1, 'o registro tem pagina', count( $chaves ) . ' paginas' );

foreach ( $registro as $chave => $def ) {
	mal_ok( ! empty( $def['titulo'] ) && ! empty( $def['caminho'] ) && isset( $def['papel'] ),
		"[$chave] titulo, caminho e papel declarados" );

	/* 14.9: os DOIS compromissos, escritos no proprio arquivo. */
	mal_ok( ! empty( $def['consulta'] ) && mb_strlen( $def['consulta'], 'UTF-8' ) > 10,
		"[$chave] declara a consulta-alvo (14.9)" );
	mal_ok( ! empty( $def['por_que_top10'] ) && mb_strlen( $def['por_que_top10'], 'UTF-8' ) > 40,
		"[$chave] declara por que chega a primeira pagina (14.9)" );

	/* O caminho e a linhagem, e as duas tem de dizer a mesma coisa: caminho
	   digitado ao lado de mae digitada diverge no dia da categoria nova. */
	$esperado = $def['post_name'];
	$sobe     = isset( $def['mae'] ) ? $def['mae'] : '';
	while ( '' !== $sobe && isset( $registro[ $sobe ] ) ) {
		$esperado = $registro[ $sobe ]['post_name'] . '/' . $esperado;
		$sobe     = isset( $registro[ $sobe ]['mae'] ) ? $registro[ $sobe ]['mae'] : '';
	}
	mal_ok( $esperado === $def['caminho'], "[$chave] o caminho e a linhagem das maes",
		$esperado . ' / ' . $def['caminho'] );

	/* A CHAVE E O CAMINHO SEM BARRA: e o que faz o meta canonico, a tag do
	   shortcode e o ARVORE.md poderem ser derivados um do outro. */
	mal_ok( str_replace( '/', '-', $def['caminho'] ) === $chave,
		"[$chave] a chave e o caminho sem barra" );

	/* Sem quarto nivel (16.1). */
	mal_ok( substr_count( $def['caminho'], '/' ) <= 2, "[$chave] no maximo tres niveis" );
}

/* ---------------------------------------------------------------------------
 * 1. O PORTAO DE DADO — recontado aqui, sem passar pelo gerador
 *
 * A conta e refeita de dados/pecas.json e dados/modelos-robo.json: perguntar ao
 * gerador se o gerador acertou e a definicao de regua inutil.
 * ------------------------------------------------------------------------- */

echo "\n1. O portao de dado da secao 13 e da 16.5, recontado do banco\n";

$banco_pecas   = json_decode( (string) file_get_contents( $raiz . '/dados/pecas.json' ), true );
$banco_modelos = json_decode( (string) file_get_contents( $raiz . '/dados/modelos-robo.json' ), true );

$modelo_publicavel = array();
foreach ( $banco_modelos['registros'] as $m ) {
	if ( 'publicavel' === $m['status'] ) {
		$modelo_publicavel[ $m['id'] ] = $m['marca'];
	}
}

/** Quantos itens de banco REAIS uma marca tem naquele tipo de peca. */
function mal_itens_da_marca( $banco_pecas, $modelo_publicavel, $tipo, $marca ) {
	$n = 0;
	foreach ( $banco_pecas['registros'] as $p ) {
		if ( 'publicavel' !== $p['status'] || $p['marca'] !== $marca ) {
			continue;
		}
		$entrega = ( $p['tipo'] === $tipo );
		if ( ! $entrega && 'kit' === $p['tipo'] ) {
			foreach ( (array) ( isset( $p['composicao'] ) ? $p['composicao'] : array() ) as $c ) {
				if ( isset( $c['tipo'] ) && $c['tipo'] === $tipo ) {
					$entrega = true;
				}
			}
		}
		if ( ! $entrega ) {
			continue;
		}
		foreach ( $p['compatibilidade'] as $par ) {
			if ( isset( $modelo_publicavel[ $par['modelo'] ] ) ) {
				$n++;
				break;
			}
		}
	}
	return $n;
}

$tipo_da_categoria = array();
foreach ( robometria_malha_dados()['categorias'] as $c ) {
	$tipo_da_categoria[ $c['slug'] ] = $c['tipo'];
}

foreach ( $registro as $chave => $def ) {
	if ( 'filha' !== $def['papel'] ) {
		continue;
	}
	$tipo  = $tipo_da_categoria[ $def['mae'] ];
	$itens = mal_itens_da_marca( $banco_pecas, $modelo_publicavel, $tipo, $def['marca'] );
	mal_ok( $itens >= 3, "[$chave] tem 3 ou mais itens de banco reais (secao 13)", $itens . ' itens' );
}

foreach ( $registro as $chave => $def ) {
	if ( 'categoria' !== $def['papel'] ) {
		continue;
	}
	$filhas = 0;
	foreach ( $registro as $outro ) {
		if ( ! empty( $outro['mae'] ) && $outro['mae'] === $chave ) {
			$filhas++;
		}
	}
	mal_ok( $filhas >= 3, "[$chave] publicada com 3 ou mais filhas (16.5)", $filhas . ' filhas' );
}

/* ---------------------------------------------------------------------------
 * 2. AS PAGINAS, cada uma no proprio processo
 * ------------------------------------------------------------------------- */

echo "\n2. As paginas saem inteiras e nenhuma esta no estado degradado\n";

$html = array();
foreach ( $chaves as $chave ) {
	$alvo = robometria_malha_tag_da_chave( $chave );
	$cmd  = escapeshellarg( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $alvo );
	$html[ $chave ] = (string) shell_exec( $cmd );

	mal_ok( strlen( $html[ $chave ] ) > 20000 && false !== strpos( $html[ $chave ], '</html>' ),
		"[$chave] pagina montada", strlen( $html[ $chave ] ) . ' bytes' );
	mal_ok( false === strpos( $html[ $chave ], 'rbm-sem-banco' ),
		"[$chave] NAO esta no estado degradado" );
	mal_ok( 1 === preg_match_all( '#<h1\b#i', $html[ $chave ] ), "[$chave] um H1 e um so" );
}

/* ---------------------------------------------------------------------------
 * 3. AS FRASES SAO AS DA REFERENCIA
 * ------------------------------------------------------------------------- */

echo "\n3. Cada frase servida e a frase da implementacao de referencia\n";

$ref = json_decode( (string) file_get_contents( $raiz . '/dados/malha-pecas-referencia.json' ), true );
mal_ok( is_array( $ref ) && ! empty( $ref['filhas'] ), 'o gabarito da referencia existe e parseia' );

foreach ( $registro as $chave => $def ) {
	$texto = mal_normalizar( mal_texto( mal_corpo( $html[ $chave ] ) ) );

	if ( 'filha' === $def['papel'] ) {
		$frases = $ref['filhas'][ $chave ];
	} elseif ( 'categoria' === $def['papel'] ) {
		$frases = $ref['categorias'][ $chave ];
	} else {
		$frases = $ref['secao']['frases'];
	}

	foreach ( $frases as $nome => $frase ) {
		if ( '' === $frase ) {
			continue;
		}
		mal_ok( false !== strpos( $texto, mal_normalizar( $frase ) ),
			"[$chave] serve a frase '$nome' da referencia",
			false !== strpos( $texto, mal_normalizar( $frase ) ) ? '' : mal_normalizar( $frase ) );
	}
}

/* ---------------------------------------------------------------------------
 * 4. 16.5: cartao de categoria que nao existe nao leva contagem
 * ------------------------------------------------------------------------- */

echo "\n4. O cartao 'em breve' nao publica contagem de banco (16.5)\n";

foreach ( $registro as $chave => $def ) {
	if ( 'filha' === $def['papel'] ) {
		continue;
	}
	if ( ! preg_match_all( '#<li class="rbm-cartao rbm-cartao-espera">(.*?)</li>#is',
		$html[ $chave ], $m ) ) {
		mal_ok( 'secao' !== $def['papel'], "[$chave] tem cartao em espera quando deveria" );
		continue;
	}
	$com_digito = array();
	foreach ( $m[1] as $cartao ) {
		$texto = mal_texto( $cartao );
		if ( preg_match( '/\d/', $texto ) ) {
			$com_digito[] = $texto;
		}
		mal_ok( false !== mb_stripos( $texto, 'em breve' ),
			"[$chave] o cartao em espera diz 'em breve'", $texto );
	}
	mal_ok( empty( $com_digito ), "[$chave] nenhum cartao em espera publica numero",
		implode( ' | ', $com_digito ) );
}

/* ---------------------------------------------------------------------------
 * 5. A PORTA DE COMPRA (secao 7 e 25.2)
 * ------------------------------------------------------------------------- */

echo "\n5. A porta de compra vem antes da procedencia, e o aviso mora no bloco\n";

foreach ( $registro as $chave => $def ) {
	if ( 'filha' !== $def['papel'] ) {
		continue;
	}
	$corpo = mal_corpo( $html[ $chave ] );

	preg_match_all( '#<li class="rbm-vitrine-item">(.*?)</li>#is', $corpo, $cartoes );
	mal_ok( count( $cartoes[1] ) >= 3, "[$chave] tres ou mais cartoes de item",
		count( $cartoes[1] ) . ' cartoes' );

	$sem_porta = 0;
	$ordem     = 0;
	foreach ( $cartoes[1] as $cartao ) {
		$acao  = strpos( $cartao, 'rbm-vitrine-acao' );
		$fonte = strpos( $cartao, 'rbm-vitrine-fonte' );
		if ( false === $acao || false === $fonte || $acao > $fonte ) {
			$ordem++;
		}
		if ( false !== strpos( $cartao, 'rbm-sem-saida' ) ) {
			$sem_porta++;
		}
	}
	mal_ok( 0 === $ordem, "[$chave] em todo cartao a compra vem antes da procedencia" );
	mal_ok( 0 === $sem_porta, "[$chave] nenhum item sem saida de compra (25.2)" );

	/* O aviso de comissao ANTES do primeiro botao, e uma vez so. */
	$pos_aviso = strpos( $corpo, 'rbm-aviso-comissao' );
	$pos_botao = strpos( $corpo, 'rbm-comprar' );
	mal_ok( false !== $pos_aviso && false !== $pos_botao && $pos_aviso < $pos_botao,
		"[$chave] o aviso de comissao vem antes do primeiro botao" );
	mal_ok( 1 === substr_count( $corpo, 'rbm-aviso-comissao' ),
		"[$chave] um aviso de comissao, um so" );

	/* Link de busca crua NAO e patrocinado: ninguem paga por aquele clique. */
	preg_match_all( '#<a class="rbm-comprar([^"]*)"[^>]*rel="([^"]+)"#i', $corpo, $links );
	$erradas = array();
	foreach ( $links[1] as $i => $classe ) {
		$cru  = ( false !== strpos( $classe, 'rbm-comprar-cru' ) );
		$rel  = $links[2][ $i ];
		$pago = ( false !== strpos( $rel, 'sponsored' ) );
		if ( $cru === $pago ) {
			$erradas[] = $classe . ' -> ' . $rel;
		}
	}
	mal_ok( empty( $erradas ), "[$chave] so o link que paga comissao leva sponsored",
		implode( ' | ', $erradas ) );
}

/* ---------------------------------------------------------------------------
 * 6. A TABELA PRE-RENDERIZADA (secao 5: visibilidade em IA)
 * ------------------------------------------------------------------------- */

echo "\n6. A tabela pre-renderizada, com a procedencia dentro da linha\n";

foreach ( $registro as $chave => $def ) {
	if ( 'secao' === $def['papel'] ) {
		continue;
	}
	$corpo = mal_corpo( $html[ $chave ] );
	mal_ok( 1 === substr_count( $corpo, '<table class="rbm-tabela">' ),
		"[$chave] uma tabela, uma so" );

	preg_match_all( '#<tbody>(.*?)</tbody>#is', $corpo, $tb );
	$linhas = preg_match_all( '#<tr>#', isset( $tb[1][0] ) ? $tb[1][0] : '', $x );
	mal_ok( $linhas >= 3, "[$chave] tres ou mais linhas de dado real", $linhas . ' linhas' );

	$sem_fonte = preg_match_all( '#<tr>(?:(?!rbm-fonte).)*?</tr>#is',
		isset( $tb[1][0] ) ? $tb[1][0] : '', $y );
	mal_ok( 0 === $sem_fonte, "[$chave] toda linha da tabela leva o link da fonte",
		$sem_fonte . ' sem fonte' );
}

/* ---------------------------------------------------------------------------
 * 7. O JSON-LD
 * ------------------------------------------------------------------------- */

echo "\n7. CollectionPage e ItemList\n";

foreach ( $registro as $chave => $def ) {
	if ( ! preg_match( '#<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"CollectionPage".*?)</script>#is',
		$html[ $chave ], $m ) ) {
		mal_ok( false, "[$chave] CollectionPage presente" );
		continue;
	}
	$doc = json_decode( $m[1], true );
	mal_ok( is_array( $doc ), "[$chave] CollectionPage valido como JSON" );
	mal_ok( ! empty( $doc['url'] ) && false !== strpos( $doc['url'], $def['caminho'] ),
		"[$chave] a url do schema e a da pagina", isset( $doc['url'] ) ? $doc['url'] : '' );
	mal_ok( ! empty( $doc['datePublished'] ) && ! empty( $doc['dateModified'] ),
		"[$chave] publica as duas datas" );
	mal_ok( ! empty( $doc['mainEntity']['itemListElement'] )
		&& count( $doc['mainEntity']['itemListElement'] ) === (int) $doc['mainEntity']['numberOfItems'],
		"[$chave] ItemList com numberOfItems contado",
		isset( $doc['mainEntity']['numberOfItems'] ) ? $doc['mainEntity']['numberOfItems'] . ' itens' : '' );

	/* Zero entidade HTML dentro do script — o defeito que esta ilha mede desde
	   11/09/2026. */
	mal_ok( false === strpos( $m[1], '&#038;' ), "[$chave] zero &#038; dentro do JSON-LD" );
}

/* ---------------------------------------------------------------------------
 * 8. A VOZ: nenhuma palavra proibida na linha-mestra (VOZ.md)
 * ------------------------------------------------------------------------- */

echo "\n8. A linha-mestra fala a lingua de quem chega (VOZ.md)\n";

$proibidas = array( 'compatibilidade paramétrica', 'especificação', 'matriz', 'procedência',
	'base de dados' );

foreach ( $registro as $chave => $def ) {
	if ( ! preg_match( '#<p class="rbm-linha-mestra">(.*?)</p>#is', $html[ $chave ], $m ) ) {
		mal_ok( false, "[$chave] tem linha-mestra" );
		continue;
	}
	$linha   = mb_strtolower( mal_texto( $m[1] ), 'UTF-8' );
	$achadas = array();
	foreach ( $proibidas as $palavra ) {
		if ( false !== mb_strpos( $linha, mb_strtolower( $palavra, 'UTF-8' ) ) ) {
			$achadas[] = $palavra;
		}
	}
	mal_ok( empty( $achadas ), "[$chave] a linha-mestra nao usa palavra proibida",
		implode( ' | ', $achadas ) );
	mal_ok( mb_strlen( $linha, 'UTF-8' ) <= 260, "[$chave] linha-mestra curta",
		mb_strlen( $linha, 'UTF-8' ) . ' caracteres' );
}

/* ---------------------------------------------------------------------------
 * 9. A MUTACAO: a regua e vista REPROVANDO
 *
 * Regua que nunca foi vista reprovando e regua nao medida (secao 8). Aqui o
 * mundo e adulterado de proposito, num processo proprio, e o que se cobra e que
 * a pagina MUDE de forma — nao que ela continue valida.
 * ------------------------------------------------------------------------- */

echo "\n9. Mutacao: sem os fatos no ar, a pagina diz que esta sem banco\n";

$cmd = escapeshellarg( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/teste-malha.php' )
	. ' ' . escapeshellarg( $raiz ) . ' --mundo-sem-banco';
$sem_banco = (string) shell_exec( $cmd );

mal_ok( false !== strpos( $sem_banco, 'rbm-sem-banco' ),
	'sem a option dos fatos, a pagina serve o aviso honesto' );
/* NO CORPO, e nao na pagina: a folha de estilo da malha declara .rbm-tabela no
   wp_head de toda pagina, e procurar a classe no HTML inteiro daria FALHA sobre
   uma pagina correta — medir o lugar errado e a familia de erro que esta ilha
   mais paga. */
mal_ok( false === strpos( mal_corpo( $sem_banco ), 'rbm-tabela' ),
	'sem a option dos fatos, nenhuma tabela com numero e servida no corpo' );

printf( "\n%s: %d afirmacoes, %d falha(s).\n", $falhas ? 'REPROVADO' : 'APROVADO', $feitos, $falhas );
exit( $falhas ? 1 : 0 );

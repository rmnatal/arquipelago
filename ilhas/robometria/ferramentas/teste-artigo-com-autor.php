<?php
/**
 * Portao: TODO no `Article` que esta ilha serve declara `author`?
 *
 *   php ferramentas/teste-artigo-com-autor.php .
 *
 * NASCEU EM 26/10/2026, FECHANDO O ITEM 1 DO DESPACHO DA SENTINELA DE 16/10 —
 * aberto 10 dias e reconferido no ar em 23/10. A ronda mediu, com quebra de
 * cache e `Accept-Encoding: identity`:
 *
 *   /filtro-universal-de-robo-aspirador/        `Article` COM `author`
 *   /quantos-m2-o-robo-aspirador-limpa-por-carga/   `Article` SEM `author`
 *
 * Duas paginas de artigo da MESMA ilha, servidas pelo MESMO emissor, e so uma
 * declarava autor. No repositorio a diferenca era UMA LINHA de array: o de
 * `robometria-a1.php` trazia `author` e o de `robometria-a2.php` nao.
 *
 * POR QUE NENHUM PORTAO VIA, e esta e a parte que vale guardar. A ilha tem
 * `teste-a1.php` e `teste-a2.php`, cada um medindo a SUA pagina, e nenhum dos
 * dois afirmava nada sobre `author` — entao o certo e o errado conviviam a uma
 * linha de distancia, no mesmo repositorio, e nada punha os dois frente a
 * frente. **Regua por pagina nao enxerga o que duas paginas deviam ter em
 * comum.** E a mesma familia do `pares_declarados` que esta ilha acabou de
 * consertar no mesmo dia: duas metades contando a mesma coisa sem nunca se
 * falarem.
 *
 * POR QUE ELE NAO TEM LISTA DE PAGINA. A exigencia do despacho e literal — *"uma
 * afirmacao que REPROVA no `Article` sem `author` em QUALQUER URL que tenha
 * `Article`"* —, e lista de duas paginas envelhece no dia do terceiro artigo,
 * que e exatamente o defeito que ele existe para pegar. Entao ele DESCOBRE: vai
 * a `robometria_teste_alvos_do_site()`, que deriva os alvos da definicao da
 * casca, das constantes de slug dos snippets e do registro da malha, monta cada
 * pagina, le TODO bloco de JSON-LD, desce o grafo inteiro e julga cada no cujo
 * `@type` inclua `Article`. Pagina nova entra na regua no dia em que nasce.
 *
 * O QUE ELE COBRA DE CADA NO `Article`:
 *   1. `author` presente;
 *   2. `author` apontando para a MESMA entidade que o `publisher` da ilha
 *      (`/#organizacao`), porque esta ilha nao tem pessoa em cena por decisao
 *      escrita no `VOZ.md` e no `/sobre/` — nao havia autor a escolher, so a
 *      declarar;
 *   3. e a simetria dita ao contrario: no que declara `publisher` e nao declara
 *      `author` e o defeito de 16/10 tal e qual.
 *
 * E ELE AFIRMA TAMBEM QUE ACHOU ARTIGO. Portao que varre e nao encontra nada
 * imprime verde sem medir — a "morte por melhora" que esta ilha ja pagou. Se o
 * numero de nos `Article` cair a zero, ele REPROVA e diz que a varredura nao
 * achou o que deveria.
 */

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

require __DIR__ . '/render-para-teste.php';
robometria_teste_carregar_options( $raiz );
robometria_teste_carregar( $raiz );

/* O grafo inteiro, e nao so o primeiro nivel: o JSON-LD desta ilha sai em
   `@graph`, e no de artigo pode estar aninhado dentro de `mentions`,
   `isPartOf` ou `isBasedOn`. Quem olha so o topo mede metade. */
function rbm_nos_do_json( $valor, &$saida ) {
	if ( is_array( $valor ) ) {
		$tipos = isset( $valor['@type'] ) ? (array) $valor['@type'] : array();
		if ( in_array( 'Article', $tipos, true ) ) {
			$saida[] = $valor;
		}
		foreach ( $valor as $filho ) {
			if ( is_array( $filho ) ) {
				rbm_nos_do_json( $filho, $saida );
			}
		}
	}
}

function rbm_artigos_da_pagina( $html ) {
	preg_match_all( '#<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>#is', $html, $m );
	$artigos = array();
	foreach ( $m[1] as $bruto ) {
		$doc = json_decode( html_entity_decode( $bruto, ENT_QUOTES, 'UTF-8' ), true );
		if ( null === $doc ) {
			$doc = json_decode( $bruto, true );
		}
		if ( is_array( $doc ) ) {
			rbm_nos_do_json( $doc, $artigos );
		}
	}
	return $artigos;
}

function rbm_id_de( $valor ) {
	if ( is_string( $valor ) ) { return $valor; }
	if ( is_array( $valor ) && isset( $valor['@id'] ) ) { return (string) $valor['@id']; }
	if ( is_array( $valor ) && isset( $valor['name'] ) ) { return 'name:' . $valor['name']; }
	return '';
}

$alvos = robometria_teste_alvos_do_site();

echo "Robometria — `author` em todo no `Article` servido (despacho de 16/10, item 1)\n";
echo str_repeat( '=', 78 ) . "\n";
printf( "  alvos descobertos: %d  (%s)\n\n", count( $alvos ), implode( ' ', $alvos ) );

$esperado   = home_url( '/#organizacao' );
$total_nos  = 0;
$com_artigo = array();
$nos_por_alvo = array();

/* O RETRATO DOS FILTROS, E ELE FOI A SEGUNDA COISA QUE ESTE PORTAO ERROU.
 *
 * `robometria_teste_rebobinar()` devolve as ACOES ao estado da carga e NAO
 * toca em `$GLOBALS['__filtros']` — nao precisava, porque nenhuma bancada
 * desta ilha montava mais de uma pagina pedindo "estou na minha pagina?" para
 * alvos diferentes no mesmo processo. Este portao monta QUATORZE, e sem o
 * retrato o filtro de cada alvo FICA ligado para os seguintes: medido, a
 * primeira versao credtou o `Article` do A1 a `/pecas/`, `/pecas/filtros/` e as
 * tres filhas de marca, e o do A2 junto — 13 nos em 7 paginas, quando a
 * verdade do site e 2 nos em 2 paginas, exatamente como a ronda de 16/10 media
 * no ar ("as outras 12 URLs nao tem no `Article`").
 *
 * E o jeito mais caro de errar: o portao nao reprovava nada, ele AFIRMAVA
 * SOBRE PAGINA ERRADA. Um `Article` quebrado em `/pecas/` seria lido como
 * quebrado em todas, e um sadio emprestado pelo vizinho esconderia o defeito
 * da pagina que nao serve nenhum. Medir a pagina com o estado de outra e a
 * mesma familia do render sem a folha de estilo que o `render-para-teste.php`
 * descreve, do lado do grafo em vez do lado do pixel.
 */
$filtros_da_carga = $GLOBALS['__filtros'];

foreach ( $alvos as $alvo ) {
	robometria_teste_rebobinar();
	$GLOBALS['__filtros'] = $filtros_da_carga;
	/* "ESTAMOS NA PAGINA QUE ESTA SENDO RENDERIZADA", e sem esta linha o portao
	   mede metade EM SILENCIO. Cada snippet de pagina pergunta "estou na minha
	   pagina?" antes de imprimir no `wp_head`; na bancada nao existe `is_page()`,
	   a resposta e NAO, e o HTML sai sem a folha, sem a barra do celular e — o
	   que importa aqui — SEM O JSON-LD. O shortcode e chamado direto e aparece,
	   entao a pagina PARECE inteira. O aviso esta escrito dentro do
	   `render-para-teste.php` desde 10/09/2026, e a primeira versao deste arquivo
	   cometeu o erro exatamente como ele descreve: achou ZERO no `Article` em 14
	   alvos. Quem o pegou foi a afirmacao de que a varredura precisa ACHAR o que
	   julga — sem ela, este portao teria nascido verde e vazio.
	   O nome do filtro sai do proprio alvo, entao pagina nova nao precisa vir
	   aqui ser lembrada. */
	add_filter( $alvo . '_na_pagina', function () { return true; } );
	$html = robometria_teste_pagina(
		$alvo,
		robometria_teste_titulo_do_alvo( $alvo ),
		robometria_teste_slug_do_alvo( $alvo )
	);
	$artigos = rbm_artigos_da_pagina( $html );
	if ( empty( $artigos ) ) {
		continue;
	}
	$com_artigo[] = $alvo;
	$nos_por_alvo[ $alvo ] = count( $artigos );
	foreach ( $artigos as $i => $no ) {
		$total_nos++;
		$onde   = sprintf( '[%s] Article #%d', $alvo, $i + 1 );
		$autor  = isset( $no['author'] ) ? rbm_id_de( $no['author'] ) : '';
		$edita  = isset( $no['publisher'] ) ? rbm_id_de( $no['publisher'] ) : '';
		rbm_ok( '' !== $autor, "$onde declara author", '' === $autor ? 'AUSENTE — e o defeito de 16/10' : $autor );
		if ( '' !== $autor ) {
			rbm_ok( $autor === $esperado, "$onde aponta o author para a organizacao da ilha",
				$autor . ' / ' . $esperado );
		}
		/* A SIMETRIA DITA AO CONTRARIO: o defeito de 16/10 era exatamente um no
		   com publisher e sem author. Esta afirmacao o nomeia pelo que ele e, e
		   nao pela ausencia de um campo — ela morde mesmo que alguem invente um
		   author que nao seja a organizacao. */
		rbm_ok( ( '' === $edita ) || ( '' !== $autor ),
			"$onde nao declara publisher sem declarar author", 'publisher ' . $edita . ', author ' . $autor );
	}
}

echo "\n";
/* A TRAVA CONTRA A MORTE POR MELHORA: varredura que nao acha nada aprova sem
   medir, e esta ilha ja pagou por isso. Dois artigos e o mundo de hoje; o
   portao cobra ao menos um, e imprime quantos achou para a diferenca aparecer. */
rbm_ok( $total_nos > 0,
	'a varredura achou no `Article` para julgar',
	$total_nos . ' no(s) em ' . count( $com_artigo ) . ' pagina(s): ' . implode( ' ', $com_artigo ) );
/* E CADA PAGINA SERVE NO MAXIMO UM `Article`: O SEU. A afirmacao existe por
   causa do defeito acima — ela e o que impede o vazamento de filtro de voltar
   calado. Pagina que servir dois nos `Article` esta servindo o do vizinho, e
   isso nao e defeito de JSON-LD: e a medicao descrevendo um site que nao
   existe. */
$dobrada = array();
foreach ( $nos_por_alvo as $alvo => $quantos ) {
	if ( $quantos > 1 ) { $dobrada[] = $alvo . ' (' . $quantos . ')'; }
}
rbm_ok( empty( $dobrada ),
	'nenhuma pagina serve mais de um no `Article` — o do vizinho nao vaza',
	empty( $dobrada ) ? 'uma por pagina' : implode( ' ', $dobrada ) );

printf( "\n%d medicoes, %d falha(s)\n", $feitos, $falhas );
exit( $falhas > 0 ? 1 : 0 );

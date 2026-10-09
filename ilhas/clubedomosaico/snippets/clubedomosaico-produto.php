/**
 * Clube do Mosaico — PÁGINAS DE CONSULTA DE PRODUTO (seção 30 do ARQUIPELAGO.md)
 *
 * Versão 1.0.0 — 09/10/2026
 *
 * O MOTOR DAS OITO PÁGINAS que nascem do despacho do Raphael de 09/10/2026 (3):
 * uma página por consulta de produto, slug igual à consulta, filha direta de
 * `/materiais/`. Elas respondem "o que comprar quando a pessoa digita o NOME DO
 * PRODUTO" — torquês, alicate, cortador, pastilhas, pastilha de vidro, base de
 * MDF, espelho e rejunte.
 *
 * -------------------------------------------------------------------------
 * POR QUE ELE É UM SNIPPET NOVO, E NÃO UMA RÉGUA DENTRO DO GUIA
 * -------------------------------------------------------------------------
 * O Guia (`clubedomosaico-guia.php`) serve FICHA DE PRODUTO com declaração de
 * FABRICANTE: a camada de prova dele é a frase literal do fabricante, com
 * documento e data de leitura. Estas oito páginas servem OFERTA DE LOJA, cuja
 * procedência é um anúncio datado da Shopee — outra fonte, outra régua de
 * honestidade e outro prazo de validade. Enfiar as duas no mesmo registro faria
 * o `cdm_guia_pronta()` do Guia decidir sobre dado que ele não sabe medir, e a
 * primeira vez que um anúncio saísse do ar a ficha de fabricante cairia junto.
 *
 * -------------------------------------------------------------------------
 * AS DUAS METADES, E POR QUE ELAS MORAM EM ARQUIVOS SEPARADOS
 * -------------------------------------------------------------------------
 *   - `dados/paginas-de-produto.json` é DECLARADO e escrito à mão: título,
 *     `description`, a resposta em duas frases, o que é e o que não é, o "qual
 *     escolher" e as perguntas. É a voz do `VOZ.md`.
 *   - `dados/vitrine-de-produto.json` é GERADO de `anuncios-por-consulta.json`
 *     por `ferramentas/gerar-vitrine-de-produto.py`, que recalcula o número
 *     próprio das ofertas que entram e sai com código 1 se discordar da coleta.
 *
 * NENHUM NÚMERO É DIGITADO NA PROSA. A prosa traz moldes — `{MIN}`, `{MAX}`,
 * `{FAIXA}`, `{N}`, `{UNIDADE}`, `{SOBRE}`, `{DATA}` — e quem os preenche é
 * `cdm_produto_preencher()`, da vitrine. Preço escrito à mão na frase é preço
 * que mente na coleta seguinte, calado, e esta ilha já pagou essa conta.
 *
 * -------------------------------------------------------------------------
 * A TABELA NÃO TEM AS COLUNAS QUE O DESPACHO PEDIU, E A DIFERENÇA É HONESTIDADE
 * -------------------------------------------------------------------------
 * O despacho pede "tabela comparando os produtos (tipo, medida, quantidade,
 * preço, para que serve)". `tipo`, `medida` e `para que serve` NÃO EXISTEM como
 * campo em nenhum anúncio da coleta: o que o anúncio sustenta é título, preço,
 * foto e a quantidade quando ele a declara — está escrito com essas palavras no
 * próprio despacho, duas linhas abaixo. Então a tabela serve o que foi medido, e
 * a página DIZ que o anúncio não declara os outros, em vez de preencher coluna
 * com palavra tirada do título. A classificação por uso, que é o que "para que
 * serve" quer, sai no "qual escolher" — escrita por quem leu os anúncios, na
 * camada declarada, e não fingida de dado.
 *
 * -------------------------------------------------------------------------
 * O PISO DA 30.2 É PORTÃO AQUI TAMBÉM, E NÃO SÓ NO GERADOR
 * -------------------------------------------------------------------------
 * Página com menos de TRÊS ofertas não é registrada: ela não ganha endereço, não
 * entra na árvore e não aparece em `/materiais/`. Duas das oito nascem com
 * exatamente três (`base-de-mdf` e `rejunte`), então o dia em que uma coleta
 * perder uma oferta a página SAI DO AR em vez de servir uma lista de duas — e o
 * `cdm_casca_link_html()` faz o link virar texto sozinho, sem 404.
 *
 * Sem `<script>` e sem `<style>` no retorno do shortcode (seção 8): o JSON-LD sai
 * no `wp_head` e a folha no `wp_footer`. Foi o E-comercial duplo dentro de
 * `<script>` que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 */

/* A VERSAO MORA NUMA CONSTANTE, e nao so no comentario do topo: o
   `atualizar-manifest.py` casa esta constante com o campo `versao` do manifest e
   RECUSA gravar quando as duas discordam. A cicatriz e da casca — o manifest
   declarou 1.6.0 enquanto o arquivo definia 1.5.0, com o sha certo, e por isso o
   portao nasceu. Foi ele que pegou a ausencia desta linha em 09/10/2026. */
if ( ! defined( 'CDM_PRODUTO_VERSAO' ) ) {
	define( 'CDM_PRODUTO_VERSAO', '1.0.0' );
}

/* ---------------------------------------------------------------------------
 * 1. As duas metades, lidas das options que o Sync grava
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_produto_piso' ) ) {
/** O piso da 30.2. Mora numa função para a bancada poder citá-lo sem copiá-lo. */
function cdm_produto_piso() {
	return 3;
}
}

if ( ! function_exists( 'cdm_produto_editorial' ) ) {
/** A camada declarada: a voz. Sem ela, nenhuma página existe. */
function cdm_produto_editorial() {
	static $d = null;
	if ( null !== $d ) {
		return $d;
	}
	$bruto = get_option( 'clubedomosaico_dados_paginas-de-produto' );
	$d     = ( is_array( $bruto ) && ! empty( $bruto['paginas'] ) && is_array( $bruto['paginas'] ) )
		? $bruto['paginas'] : array();

	return $d;
}
}

if ( ! function_exists( 'cdm_produto_vitrine' ) ) {
/** A camada gerada: o número e o link. */
function cdm_produto_vitrine() {
	static $v = null;
	if ( null !== $v ) {
		return $v;
	}
	$bruto = get_option( 'clubedomosaico_dados_vitrine-de-produto' );
	$v     = ( is_array( $bruto ) && ! empty( $bruto['paginas'] ) && is_array( $bruto['paginas'] ) )
		? $bruto['paginas'] : array();

	return $v;
}
}

if ( ! function_exists( 'cdm_produto_registro' ) ) {
/**
 * O REGISTRO: as páginas que EXISTEM, com as duas metades casadas pelo `id`.
 *
 * As três travas, e cada uma tira a página do ar em vez de a servir pela metade:
 *   (a) sem a metade editorial, a página não tem voz — não nasce;
 *   (b) sem a metade da vitrine, ela não tem número nem link — não nasce;
 *   (c) com menos de três ofertas, ela viola o piso da 30.2 — não nasce.
 *
 * A ORDEM É A DA DECLARAÇÃO, e não a do arquivo gerado: quem decide em que ordem
 * as irmãs se listam é quem escreveu a voz, não a ordem em que a API respondeu.
 */
function cdm_produto_registro() {
	static $r = null;
	if ( null !== $r ) {
		return $r;
	}

	$vitrine = array();
	foreach ( cdm_produto_vitrine() as $v ) {
		if ( ! empty( $v['id'] ) ) {
			$vitrine[ $v['id'] ] = $v;
		}
	}

	$r = array();
	foreach ( cdm_produto_editorial() as $e ) {
		if ( empty( $e['id'] ) || ! isset( $vitrine[ $e['id'] ] ) ) {
			continue;
		}
		$v = $vitrine[ $e['id'] ];
		if ( empty( $v['ofertas'] ) || ! is_array( $v['ofertas'] )
			|| count( $v['ofertas'] ) < cdm_produto_piso() ) {
			continue;
		}
		if ( empty( $v['slug'] ) || empty( $e['titulo'] ) ) {
			continue;
		}
		$r[ $e['id'] ] = array_merge( $e, $v );
	}

	return $r;
}
}

if ( ! function_exists( 'cdm_produto_ids' ) ) {
function cdm_produto_ids() {
	return array_keys( cdm_produto_registro() );
}
}

if ( ! function_exists( 'cdm_produto_pagina' ) ) {
function cdm_produto_pagina( $id ) {
	$r = cdm_produto_registro();

	return isset( $r[ $id ] ) ? $r[ $id ] : null;
}
}

if ( ! function_exists( 'cdm_produto_id_do_slug' ) ) {
function cdm_produto_id_do_slug( $slug ) {
	$slug = trim( (string) $slug, '/' );
	foreach ( cdm_produto_registro() as $id => $p ) {
		if ( $p['slug'] === $slug ) {
			return $id;
		}
	}

	return '';
}
}

/* ---------------------------------------------------------------------------
 * 2. O número, formatado — e os moldes da prosa
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_produto_moeda' ) ) {
/**
 * R$ 68,99, nos DOIS modos, e a diferença não é cosmética.
 *
 * Na TELA o espaço é inquebrável, para o preço não virar de linha no meio. No
 * JSON-LD o espaço é normal: `&nbsp;` lá seria publicado como se fosse o texto
 * da resposta — a máquina de busca leria "R$&nbsp;68,99" e uma revisão humana
 * nunca veria a diferença, porque na tela as duas saem idênticas.
 */
function cdm_produto_moeda( $valor, $modo = 'html' ) {
	$espaco = ( 'texto' === $modo ) ? ' ' : '&nbsp;';

	return 'R$' . $espaco . number_format_i18n( (float) $valor, 2 );
}
}

if ( ! function_exists( 'cdm_produto_unidade_html' ) ) {
/**
 * O preço por peça, de ponta a ponta, com o nome da peça que a página usa.
 *
 * Duas casas, porque é dinheiro que a pessoa vai comparar na banca: a conta fina
 * (R$ 0,0358 por pastilha) fica na TABELA, por oferta, onde ela pode ser
 * conferida contra o preço e a contagem do próprio anúncio.
 */
function cdm_produto_unidade_html( $p, $modo = 'html' ) {
	$np = $p['numero_proprio'];
	$u  = ! empty( $p['unidade_singular'] ) ? ' ' . $p['unidade_singular'] : '';
	$u  = ( 'texto' === $modo ) ? $u : esc_html( $u );

	return cdm_produto_moeda( $np['de'], $modo ) . ' a '
		. cdm_produto_moeda( $np['ate'], $modo ) . $u;
}
}

if ( ! function_exists( 'cdm_produto_preencher' ) ) {
/**
 * OS MOLDES DA PROSA, preenchidos da vitrine.
 *
 * O texto entra ESCAPADO e sai com as entidades do preço (`&nbsp;`) inteiras:
 * por isso o escape acontece aqui, antes da troca, e nunca depois — escapar
 * depois transformaria `&nbsp;` em `&amp;nbsp;` na tela, que é a mesma família
 * do defeito de 08/09/2026 na Aquametria.
 */
function cdm_produto_preencher( $texto, $p, $modo = 'html' ) {
	$np    = $p['numero_proprio'];
	$faixa = cdm_produto_moeda( $np['de'], $modo ) . ' a ' . cdm_produto_moeda( $np['ate'], $modo );
	$data  = cdm_casca_data_br( $p['colhido_em'] );

	$troca = array(
		'{MIN}'     => cdm_produto_moeda( $np['de'], $modo ),
		'{MAX}'     => cdm_produto_moeda( $np['ate'], $modo ),
		'{FAIXA}'   => $faixa,
		'{N}'       => number_format_i18n( (int) $p['n_ofertas'] ),
		'{SOBRE}'   => number_format_i18n( (int) $np['sobre_quantas_ofertas'] ),
		'{UNIDADE}' => cdm_produto_unidade_html( $p, $modo ),
		'{DATA}'    => ( 'texto' === $modo ) ? $data : esc_html( $data ),
	);

	$base = ( 'texto' === $modo ) ? (string) $texto : esc_html( $texto );

	return str_replace( array_keys( $troca ), array_values( $troca ), $base );
}
}

/* ---------------------------------------------------------------------------
 * 3. Endereço e árvore
 *
 * NÍVEL 2, filha direta de `/materiais/`: é página-folha de produto, e a 16.5
 * não se aplica a ela — a mesma leitura que deixou
 * `/como-fazer/o-que-e-mosaico-picassiete/` nascer filha direta. Quando uma
 * ganhar três filhas, ela vira mãe sem trocar de URL.
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	foreach ( cdm_produto_registro() as $id => $p ) {
		$paginas[ $p['slug'] ] = array(
			'titulo'    => $p['titulo'],
			'conteudo'  => '[cdm_produto_' . $id . ']',
			'pai'       => 'materiais',
			'descricao' => $p['description'],
		);
	}

	return $paginas;
} );

add_filter( 'cdm_arvore', function ( $mapa ) {
	if ( ! is_array( $mapa ) ) {
		return $mapa;
	}
	foreach ( cdm_produto_registro() as $p ) {
		if ( isset( $mapa[ $p['slug'] ] ) ) {
			continue;
		}
		/* NÍVEL 3 COM A MÃE DE NÍVEL 1 DIRETO, e o número não é a contagem de
		   barras da URL: nesta casca `nivel` é o lugar na ÁRVORE FINAL, e está
		   escrito com essas palavras no registro das ferramentas ("o nível
		   declarado é o da árvore final, não o da contagem de barras"). É o
		   mesmo estado de transição da F1, da F2 e das duas técnicas: dois
		   segmentos hoje, categoria quando houver três filhas (16.5), sem mover
		   a URL — e é exatamente o precedente que o despacho cita,
		   `/como-fazer/o-que-e-mosaico-picassiete/`, que é `nivel => 3`.

		   DECLARAR 2 AQUI CUSTOU 48 AFIRMAÇÕES, medidas em 09/10/2026: o nível 2
		   é o da CATEGORIA, então as oito entravam como irmãs dos seis cartões
		   de prateleira e da camada de prova, a trilha saía com três degraus
		   contra dois do mapa e cada página se listava como irmã de si mesma. */
		$mapa[ $p['slug'] ] = array(
			'nivel'  => 3,
			'mae'    => 'materiais',
			'rotulo' => $p['titulo'],
		);
	}

	return $mapa;
} );

/* O `<title>` NÃO TEM FILTRO AQUI, E A AUSÊNCIA É A REGRA DESTA ILHA.
   O nome da página é UM — a consulta exata — e ele sai no H1, no cartão de
   `/materiais/`, no degrau da trilha e na primeira metade do `<title>`. Quem
   monta o `<title>` é a casca, uma vez, acrescentando a cauda da marca
   (`cdm_casca_titulo_do_documento()`). Declarar aqui um título próprio, mais
   longo, seria dar dois nomes ao mesmo endereço — o defeito que a Aquametria
   pagou em 11/09/2026, com o `<title>` e o H1 discordando a uma linha de
   distância. E nenhuma destas oito declara `cdm_promessa`: a alavanca da 12.1 é
   para página que já está na banda de 4 a 10 e não é clicada, e estas nascem
   com zero impressão. */

add_filter( 'cdm_descricao', function ( $d, $slug ) {
	$id = cdm_produto_id_do_slug( (string) $slug );
	if ( '' === $id ) {
		return $d;
	}
	$p = cdm_produto_pagina( $id );

	return isset( $p['description'] ) ? (string) $p['description'] : $d;
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * 4. O HTML da página
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_produto_oferta_linha_html' ) ) {
/**
 * UMA LINHA DA TABELA. O botão de compra mora AQUI, dentro da linha do produto,
 * e é isso que põe o bloco de compra ANTES da procedência que fecha a página —
 * a ordem que o despacho pede com essas palavras.
 *
 * `rel="sponsored noopener"` é o mesmo da F2, porque é link de afiliado: a
 * seção 7 do contrato não admite link de comissão sem a marcação, e a página
 * de divulgação está linkada no rodapé de toda página desta ilha.
 */
function cdm_produto_oferta_linha_html( $o, $p ) {
	$np       = $p['numero_proprio'];
	$por_peca = ( 'faixa_de_preco' !== $np['tipo'] );

	$html = '<tr>';

	$html .= '<th scope="row" class="cdm-produto-prod">';
	if ( ! empty( $o['imagem_url'] ) ) {
		$html .= '<img class="cdm-produto-foto" src="' . esc_url( $o['imagem_url'] ) . '"'
			. ' width="64" height="64" loading="lazy" alt="' . esc_attr( $o['titulo'] ) . '">';
	} else {
		$html .= '<span class="cdm-produto-sem-foto" aria-hidden="true"></span>';
	}
	$html .= '<span class="cdm-produto-titulo">' . esc_html( $o['titulo'] ) . '</span>';
	/* O VENDEDOR SAI; A NOTA DELE NÃO, E A AUSÊNCIA É A DECISÃO.
	   A coleta traz um campo `nota` cuja régua ninguém escreveu: 31 das 58
	   ofertas vêm com `"0"` e uma com `"1"`. Servido na tela, isso publica
	   "produto péssimo" em mais da metade da lista e "nota 1" num produto que
	   esta própria página recomenda. O que o anúncio sustenta é título, preço,
	   foto e quantidade declarada — nota não está nessa lista, e número sem
	   régua é significado inventado. Por isso ele não chega nem à vitrine. */
	if ( ! empty( $o['loja'] ) ) {
		$html .= '<span class="cdm-produto-loja">' . esc_html( $o['loja'] ) . '</span>';
	}
	$html .= '</th>';

	/* QUANTIDADE: só sai número quando o ANÚNCIO a declara. Onde ele não
	   declara, sai a frase de que não declara — nunca uma contagem adivinhada
	   do título, que é o jeito barato de errar em dado comercial. */
	$html .= '<td class="cdm-produto-qtd">';
	if ( ! empty( $o['quantidade_declarada'] ) ) {
		$html .= number_format_i18n( (int) $o['quantidade_declarada'] );
	} else {
		$html .= '<span class="cdm-produto-nao-declara">não declara</span>';
	}
	$html .= '</td>';

	$html .= '<td class="cdm-produto-preco">' . cdm_produto_moeda( $o['preco'] ) . '</td>';

	if ( $por_peca ) {
		$html .= '<td class="cdm-produto-unit">';
		if ( ! empty( $o['quantidade_declarada'] ) ) {
			$html .= 'R$&nbsp;' . number_format_i18n(
				round( (float) $o['preco'] / (int) $o['quantidade_declarada'], 4 ), 4 );
		} else {
			$html .= '<span class="cdm-produto-nao-declara">—</span>';
		}
		$html .= '</td>';
	}

	$html .= '<td class="cdm-produto-compra">'
		. '<a class="cdm-produto-botao" href="' . esc_url( $o['url_afiliado'] ) . '"'
		. ' rel="sponsored noopener" target="_blank">Ver na loja</a></td>';

	$html .= '</tr>';

	return $html;
}
}

if ( ! function_exists( 'cdm_produto_html' ) ) {
function cdm_produto_html( $id ) {
	$p = cdm_produto_pagina( $id );
	if ( ! $p ) {
		/* A PÁGINA SEM DADO NÃO INVENTA e não finge estar cheia: ela diz que a
		   medição não chegou e manda a pessoa para a ferramenta, que funciona
		   sem este banco. É a mesma trava do Guia e das técnicas. */
		return '<div class="cdm-bloco"><div class="cdm-vazio">'
			. '<h3>A lista desta página ainda não chegou ao site</h3>'
			. '<p>A gente não vai inventar preço nem oferta enquanto isso. Use o '
			. ( function_exists( 'cdm_casca_link_html' )
				? cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
				: 'guia de materiais' )
			. ', que pergunta a base e o lugar da peça.</p></div></div>';
	}

	$np       = $p['numero_proprio'];
	$por_peca = ( 'faixa_de_preco' !== $np['tipo'] );

	$html = '<div class="cdm-bloco cdm-produto">';

	/* 1. A RESPOSTA EM DUAS FRASES, ANTES DE QUALQUER EXPLICAÇÃO: o que comprar
	      e quanto custa. É o item que o despacho põe em primeiro lugar. */
	$html .= '<div class="cdm-produto-resposta">';
	foreach ( $p['resposta'] as $i => $frase ) {
		$html .= '<p class="cdm-produto-frase' . ( 0 === $i ? ' cdm-produto-frase-1' : '' ) . '">'
			. cdm_produto_preencher( $frase, $p ) . '</p>';
	}
	$html .= '</div>';

	/* 2. O DADO FINO, quando a faixa esconde algo — e ele vem ANTES da tabela,
	      porque é aviso sobre o número que a pessoa está a um parágrafo de ler.
	      É o caso do rejunte, nomeado no despacho: a faixa é larga porque uma
	      das três ofertas é rejunte metálico de especialidade, e servir a faixa
	      sem dizer isso seria servi-la como se fosse a do rejunte comum. */
	if ( ! empty( $p['dado_fino'] ) ) {
		$html .= '<p class="cdm-produto-fino"><strong>Antes de olhar a faixa:</strong> '
			. cdm_produto_preencher( $p['dado_fino'], $p ) . '</p>';
	}

	/* 3. O QUE É, E O QUE NÃO É — a armadilha da busca, medida e dita. */
	$html .= '<div class="cdm-secao"><h2>O que é, e o que não é</h2>';
	$html .= '<p>' . cdm_produto_preencher( $p['o_que_e'], $p ) . '</p>';
	$html .= '<p>' . cdm_produto_preencher( $p['o_que_nao_e'], $p ) . '</p></div>';

	/* 4. A TABELA, com o bloco de compra dentro de cada linha. */
	$html .= '<div class="cdm-secao"><h2>As ' . number_format_i18n( (int) $p['n_ofertas'] )
		. ' ofertas que a gente conferiu</h2>';
	$html .= '<div class="cdm-produto-rolagem"><table class="cdm-produto-tabela">';
	$html .= '<thead><tr><th scope="col">Produto</th><th scope="col">Peças no anúncio</th>'
		. '<th scope="col">Preço</th>'
		. ( $por_peca ? '<th scope="col">' . esc_html( trim( str_replace( 'por ', 'Por ', isset( $p['unidade_singular'] ) ? $p['unidade_singular'] : 'Por peça' ) ) ) . '</th>' : '' )
		. '<th scope="col">Onde comprar</th></tr></thead><tbody>';
	foreach ( $p['ofertas'] as $o ) {
		$html .= cdm_produto_oferta_linha_html( $o, $p );
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="cdm-produto-nota-tabela">O anúncio declara título, preço, foto e, quando quer, '
		. 'quantas peças vêm. Ele não declara medida nem para que serve — então essas duas não têm '
		. 'coluna aqui, e quem as responde é o "qual escolher" abaixo.</p>';
	$html .= '</div>';

	/* 5. QUAL ESCOLHER, por uso. */
	$html .= '<div class="cdm-secao"><h2>Qual escolher</h2><dl class="cdm-produto-usos">';
	foreach ( $p['qual_escolher'] as $u ) {
		$html .= '<dt>' . esc_html( $u['uso'] ) . '</dt>'
			. '<dd>' . cdm_produto_preencher( $u['frase'], $p ) . '</dd>';
	}
	$html .= '</dl></div>';

	/* 6. A SEÇÃO EXTRA COM ÂNCORA — hoje só a pinça, dentro do alicate. É o que
	      a 30.4 manda fazer com consulta que canibaliza uma irmã: ela vira
	      âncora da página que já responde, não uma segunda URL. */
	if ( ! empty( $p['secao_extra']['id'] ) ) {
		$s     = $p['secao_extra'];
		$html .= '<div class="cdm-secao" id="' . esc_attr( $s['id'] ) . '">'
			. '<h2>' . esc_html( $s['titulo'] ) . '</h2>';
		foreach ( $s['frases'] as $f ) {
			$html .= '<p>' . cdm_produto_preencher( $f, $p ) . '</p>';
		}
		$html .= '</div>';
	}

	/* 7. AS PERGUNTAS, com os números da própria página. */
	$html .= '<div class="cdm-secao cdm-produto-faq"><h2>Perguntas</h2><dl>';
	foreach ( cdm_produto_faq( $id ) as $q ) {
		$html .= '<dt>' . esc_html( $q['pergunta'] ) . '</dt><dd>' . $q['resposta_html'] . '</dd>';
	}
	$html .= '</dl></div>';

	/* 8. A MALHA: as ferramentas, as irmãs, a cola que já ranqueia e a loja.
	      Nenhuma órfã, e nenhum "saiba mais" — a âncora é a consulta (16.4-a). */
	$html .= cdm_produto_malha_html( $id );

	/* 9. A PROCEDÊNCIA, por último e DEPOIS do bloco de compra. */
	$html .= '<div class="cdm-secao cdm-prova cdm-produto-procedencia"><h2>Como a gente sabe</h2>';
	$html .= '<p>Os ' . number_format_i18n( (int) $p['n_ofertas'] ) . ' anúncios desta página foram lidos na '
		. '<strong>Shopee</strong> em ' . esc_html( cdm_casca_data_br( $p['colhido_em'] ) )
		. ', pela busca <em>' . esc_html( $p['consulta'] ) . '</em>, e cada um passou por uma regra '
		. 'escrita antes da leitura — é ela que tirou daqui a peça de reposição, o quadro decorativo '
		. 'e o revestimento de obra que essa busca também devolve.</p>';
	$html .= '<p>É uma leitura só, de um dia só: a loja devolve conjuntos diferentes a cada consulta, '
		. 'então a faixa acima é a da nossa coleta e não o catálogo inteiro da Shopee. Preço muda; '
		. 'a gente republica quando mede de novo.</p>';
	/* A FRASE NÃO CITA O ERRO QUE ELA EVITA. A versão anterior terminava em
	   «e em nenhum lugar "o mercado"» — e a própria página passava a conter a
	   expressão que a regra proíbe, o que derrubou a afirmação da bancada em
	   todas as oito. Regra declarada dentro do texto que ela governa é regra que
	   se contradiz na primeira medição. */
	$html .= '<p>O <strong>Mercado Livre não entra nesta página</strong>, e não é escolha nossa: '
		. 'nas três tentativas de 09/10/2026 ele recusou a leitura automática. Então quando esta '
		. 'página diz Shopee, é Shopee — e ela não fala de preço que não mediu.</p>';
	if ( $por_peca ) {
		$html .= '<p>A conta por peça é o preço do anúncio dividido pelas peças que ele declara, e ela '
			. 'sai sobre ' . number_format_i18n( (int) $np['sobre_quantas_ofertas'] ) . ' das '
			. number_format_i18n( (int) $p['n_ofertas'] ) . ' ofertas — as outras não declaram quantidade, '
			. 'e dividir sem a contagem seria inventar o número.</p>';
	}
	$html .= '</div>';

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_produto_faq' ) ) {
/**
 * As perguntas, com os moldes preenchidos — nas DUAS formas.
 *
 * `resposta_html` vai para a tela (com `&nbsp;` dentro do preço) e `resposta`
 * vai para o JSON-LD, em texto limpo. Mandar o HTML para o JSON-LD publicaria
 * `R$&nbsp;68,99` como se fosse o texto da resposta, e é o tipo de diferença que
 * passa por toda revisão humana e nenhuma máquina de busca perdoa.
 */
function cdm_produto_faq( $id ) {
	$p = cdm_produto_pagina( $id );
	if ( ! $p || empty( $p['faq'] ) ) {
		return array();
	}
	$saida = array();
	foreach ( $p['faq'] as $q ) {
		$saida[] = array(
			'pergunta'      => $q['pergunta'],
			'resposta_html' => cdm_produto_preencher( $q['resposta'], $p, 'html' ),
			'resposta'      => cdm_produto_preencher( $q['resposta'], $p, 'texto' ),
		);
	}

	return $saida;
}
}

if ( ! function_exists( 'cdm_produto_malha_html' ) ) {
/**
 * A MALHA DESTA PÁGINA, e as quatro direções são as do despacho.
 *
 * A COLA NÃO GANHA PÁGINA NOVA e ganha link de todas: `qual-cola-usar-no-mosaico`
 * já está na primeira página do Google pela consulta "cola para mosaico", e uma
 * segunda URL a canibalizaria (30.4). Toda página nova linka para ela com a
 * âncora que a pessoa digita.
 */
function cdm_produto_malha_html( $id ) {
	$p    = cdm_produto_pagina( $id );
	$html = '<div class="cdm-secao cdm-produto-malha"><h2>Para continuar</h2>';

	$html .= '<h3>As contas que estas compras pedem</h3><ul>';
	$html .= '<li>' . cdm_casca_link_html( 'materiais/quantas-pastilhas-para-mosaico',
		'quantas pastilhas e quanto rejunte a sua peça precisa' ) . '</li>';
	$html .= '<li>' . cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico',
		'qual cola usar no mosaico' ) . '</li>';
	$html .= '</ul>';

	$irmas = array();
	foreach ( cdm_produto_registro() as $outro_id => $o ) {
		if ( $outro_id === $id ) {
			continue;
		}
		$irmas[] = '<li>' . cdm_casca_link_html( $o['slug'], $o['consulta'] ) . '</li>';
	}
	if ( $irmas ) {
		$html .= '<h3>O resto do material</h3><ul>' . implode( '', $irmas ) . '</ul>';
	}

	$html .= '<h3>Prefere a peça pronta?</h3><p>A gente faz mosaico à mão, uma peça por vez. '
		. 'As que estão disponíveis ficam na ' . cdm_casca_link_html( 'loja', 'loja do ateliê' )
		. ' — ali o preço é o nosso, sem comissão de ninguém.</p>';

	$html .= '<p class="cdm-produto-volta">Voltar para '
		. cdm_casca_link_html( 'materiais', 'materiais para mosaico' ) . '.</p>';

	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 4b. A MÃE LISTA AS FILHAS, E A HOME LEVA AS DE MAIOR INTENÇÃO
 *
 * `/materiais/` lista TODAS as oito, com a âncora igual à consulta — 16.4(a) ao
 * pé da letra, e nunca "saiba mais". A home leva só as de maior intenção, e quem
 * decide isso é a faixa de volume MEDIDA em 10/09/2026 e declarada em
 * `na_home`, não o gosto de quem publica.
 *
 * As duas entram pelos pontos de extensão da casca (`cdm_materiais_secoes` e
 * `cdm_home_secoes`) em vez de a casca listar as oito à mão: família nova não
 * deve obrigar a editar a casca, que é o argumento que ela mesma escreveu em
 * 1.5.0 para os cartões de ferramenta.
 *
 * SEM ISTO AS OITO SERIAM ÓRFÃS pela 16.4(f), que cobra dois links internos para
 * toda URL do sitemap, um deles da mãe. As irmãs linkam umas para as outras, o
 * que já dá sete — mas nenhum vindo da mãe, e é o da mãe que a regra nomeia.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_produto_cartoes_html' ) ) {
/** Os cartões de uma lista de páginas, com a âncora igual à consulta. */
function cdm_produto_cartoes_html( $paginas ) {
	if ( ! $paginas ) {
		return '';
	}
	$html = '<ul class="cdm-produto-cartoes">';
	foreach ( $paginas as $p ) {
		$np    = $p['numero_proprio'];
		$html .= '<li><h3>' . cdm_casca_link_html( $p['slug'], $p['consulta'] ) . '</h3>'
			. '<p class="cdm-produto-cartao-faixa">'
			. cdm_produto_moeda( $np['de'] ) . ' a ' . cdm_produto_moeda( $np['ate'] )
			. ( ! empty( $p['unidade_singular'] ) ? ' ' . esc_html( $p['unidade_singular'] ) : '' )
			. '</p>'
			. '<p class="cdm-produto-cartao-conta">' . number_format_i18n( (int) $p['n_ofertas'] )
			. ' ofertas conferidas</p></li>';
	}

	return $html . '</ul>';
}
}

add_filter( 'cdm_materiais_secoes', function ( $html ) {
	$todas = cdm_produto_registro();
	if ( ! $todas ) {
		return $html;
	}

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>O que comprar, produto por produto</h2>';
	$html .= '<p>Uma página por material, com as ofertas que a gente conferiu uma a uma e o '
		. 'preço do dia da leitura. Nenhuma delas diz "o mercado" querendo dizer uma loja só.</p>';
	$html .= cdm_produto_cartoes_html( $todas );
	$html .= '</div>';

	return $html;
} );

add_filter( 'cdm_home_secoes', function ( $html ) {
	$destaque = array();
	foreach ( cdm_produto_registro() as $p ) {
		if ( ! empty( $p['na_home'] ) ) {
			$destaque[] = $p;
		}
	}
	if ( ! $destaque ) {
		return $html;
	}

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Materiais para mosaico</h2>';
	$html .= '<p>O caquinho, o vidro e a ferramenta de cortar: o que comprar, quanto custa hoje '
		. 'e qual serve para a peça que você tem na mão.</p>';
	$html .= cdm_produto_cartoes_html( $destaque );
	$html .= '<p>' . cdm_casca_link_html( 'materiais', 'ver todos os materiais' ) . '.</p>';
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Os shortcodes — UM POR PÁGINA
 *
 * Um por página, e não um só resolvendo pela página servida: é assim que a
 * bancada sabe QUAL página está medindo. Duas páginas com o mesmo shortcode
 * seriam medidas como se fossem a mesma, e a segunda nunca teria sido medida —
 * a cicatriz que as técnicas desta ilha pagaram na 1.1.0.
 * ------------------------------------------------------------------------- */

foreach ( cdm_produto_ids() as $cdm_produto_id ) {
	add_shortcode( 'cdm_produto_' . $cdm_produto_id, function () use ( $cdm_produto_id ) {
		return cdm_produto_html( $cdm_produto_id );
	} );
}
unset( $cdm_produto_id );

/* ---------------------------------------------------------------------------
 * 6. Cabeça da página — JSON-LD
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_produto_id_da_pagina_atual' ) ) {
function cdm_produto_id_da_pagina_atual() {
	if ( ! function_exists( 'cdm_casca_slug_atual' ) ) {
		return '';
	}

	return cdm_produto_id_do_slug( cdm_casca_slug_atual() );
}
}

add_action( 'wp_head', function () {
	$id = cdm_produto_id_da_pagina_atual();
	if ( '' === $id ) {
		return;
	}
	$p     = cdm_produto_pagina( $id );
	$limpa = home_url( '/' . $p['slug'] . '/' );

	$perguntas = array();
	foreach ( cdm_produto_faq( $id ) as $q ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $q['pergunta'],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $q['resposta'] ),
		);
	}

	/* O ItemList SERVE AS OFERTAS QUE A TELA SERVE, na mesma ordem e com o mesmo
	   preço. A `url` de cada item é o link de afiliado — o mesmo endereço do
	   botão —, porque publicar no dado estruturado um endereço diferente do que
	   a pessoa clica é dizer uma coisa para a máquina e outra para ela. */
	$itens = array();
	foreach ( $p['ofertas'] as $i => $o ) {
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $i + 1,
			'item'     => array(
				'@type' => 'Product',
				'name'  => $o['titulo'],
				'image' => ! empty( $o['imagem_url'] ) ? $o['imagem_url'] : null,
				'offers' => array(
					'@type'         => 'Offer',
					'price'         => number_format( (float) $o['preco'], 2, '.', '' ),
					'priceCurrency' => 'BRL',
					'url'           => $o['url_afiliado'],
					'availability'  => 'https://schema.org/InStock',
					'seller'        => ! empty( $o['loja'] )
						? array( '@type' => 'Organization', 'name' => $o['loja'] ) : null,
				),
			),
		);
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type'       => 'Article',
				'@id'         => $limpa . '#artigo',
				'headline'    => $p['titulo'],
				'url'         => $limpa,
				'inLanguage'  => 'pt-BR',
				'description' => $p['description'],
				'about'       => array( '@type' => 'Thing', 'name' => $p['consulta'] ),
				'publisher'   => array( '@id' => home_url( '/#organizacao' ) ),
				'isPartOf'    => array( '@id' => home_url( '/#site' ) ),
			),
			array(
				'@type'           => 'ItemList',
				'@id'             => $limpa . '#ofertas',
				'name'            => $p['titulo'],
				'numberOfItems'   => count( $itens ),
				'itemListOrder'   => 'https://schema.org/ItemListOrderAscending',
				'itemListElement' => $itens,
			),
			array(
				'@type'      => 'FAQPage',
				'@id'        => $limpa . '#perguntas',
				'mainEntity' => $perguntas,
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-produto-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 7. Folha — no rodapé, NUNCA dentro do retorno do shortcode
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	/* A FOLHA SAI TAMBÉM NA MÃE E NA HOME, e não só nas oito: os cartões do
	   bloco acima moram nelas. Sem esta condição os cartões sairiam sem estilo
	   exatamente nas duas páginas mais vistas da ilha — e a bancada, que mede as
	   oito, ficaria verde. */
	$slug = function_exists( 'cdm_casca_slug_atual' ) ? cdm_casca_slug_atual() : '';
	$mae_ou_home = ( 'materiais' === $slug || 'inicio' === $slug || '' === $slug );
	if ( '' === cdm_produto_id_da_pagina_atual() && ! $mae_ou_home ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-produto-css">
.cdm-produto-cartoes{list-style:none;margin:1rem 0;padding:0;display:grid;gap:1rem;}
.cdm-produto-cartoes li{border:1px solid var(--cdm-traco);border-radius:2px;padding:1rem;}
.cdm-produto-cartoes h3{margin:0 0 .35rem;font-size:1.05rem;}
.cdm-produto-cartao-faixa{margin:0;font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;font-weight:600;}
.cdm-produto-cartao-conta{margin:.25rem 0 0!important;color:var(--cdm-legenda);font-size:.88rem;}
@media (min-width:640px){.cdm-produto-cartoes{grid-template-columns:repeat(2,1fr);}}
@media (min-width:900px){.cdm-produto-cartoes{grid-template-columns:repeat(4,1fr);}}
.cdm-produto-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-produto-frase{margin:0 0 .6rem;line-height:1.55;}
.cdm-produto-frase:last-child{margin-bottom:0;}
.cdm-produto-frase-1{font-size:1.15rem;}
.cdm-produto-fino{margin:1.2rem 0;padding:.9rem 1rem;border-left:3px solid var(--cdm-ambar,#B9791A);background:#FFFBF4;border-radius:2px;font-size:.96rem;line-height:1.55;}
.cdm-produto-rolagem{overflow-x:auto;margin:1rem 0;}
.cdm-produto-tabela{width:100%;border-collapse:collapse;font-size:.94rem;}
.cdm-produto-tabela th,.cdm-produto-tabela td{text-align:left;padding:.6rem .5rem;border-bottom:1px solid var(--cdm-traco);vertical-align:top;}
.cdm-produto-tabela thead th{font-family:var(--cdm-display);font-size:.82rem;letter-spacing:.04em;text-transform:uppercase;color:var(--cdm-legenda);white-space:nowrap;}
.cdm-produto-prod{font-weight:400;max-width:26rem;}
.cdm-produto-foto{float:left;width:64px;height:64px;object-fit:cover;margin:0 .7rem .2rem 0;border-radius:2px;}
.cdm-produto-sem-foto{float:left;width:64px;height:64px;margin:0 .7rem .2rem 0;background:var(--cdm-traco);border-radius:2px;display:block;}
.cdm-produto-titulo{display:block;line-height:1.35;}
.cdm-produto-loja{display:block;clear:both;padding-top:.3rem;font-family:var(--cdm-mono);font-size:.76rem;color:var(--cdm-legenda);}
.cdm-produto-qtd,.cdm-produto-preco,.cdm-produto-unit{font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.cdm-produto-preco{font-weight:600;}
.cdm-produto-nao-declara{font-family:var(--cdm-texto);color:var(--cdm-legenda);font-size:.88rem;}
.cdm-produto-botao{display:inline-block;padding:.45rem .8rem;background:var(--cdm-coral);color:#fff;border-radius:2px;text-decoration:none;font-size:.88rem;white-space:nowrap;}
.cdm-produto-botao:hover{background:var(--cdm-rubi,#8A0F18);}
.cdm-produto-nota-tabela{color:var(--cdm-legenda);font-size:.9rem;margin:.6rem 0 0;}
.cdm-produto-usos dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .3rem;}
.cdm-produto-usos dd{margin:0;}
.cdm-produto-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .3rem;}
.cdm-produto-faq dd{margin:0;}
.cdm-produto-malha h3{font-size:1rem;margin:1.2rem 0 .4rem;}
.cdm-produto-malha ul{margin:.2rem 0 .6rem 1.1rem;padding:0;}
.cdm-produto-malha li{margin:.25rem 0;}
.cdm-produto-volta{margin-top:1rem;}
@media (max-width:640px){.cdm-produto-prod{min-width:15rem;}}
</style>
HTML;
}, 20 );

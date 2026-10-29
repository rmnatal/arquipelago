<?php
/**
 * RODAMETRIA — PAGINAS PELO NOME DO PRODUTO (secao 30 do ARQUIPELAGO.md)
 *
 * O motor da secao `/veiculos/` e das paginas de consulta de produto que nascem
 * filhas diretas dela: uma pagina por consulta de compra, slug igual a consulta.
 * Elas respondem "o que comprar quando a pessoa digita o NOME DO PRODUTO".
 *
 * -------------------------------------------------------------------------
 * POR QUE ELE E UM SNIPPET NOVO, E NAO UMA REGUA DENTRO DA F2
 * -------------------------------------------------------------------------
 * A F2 serve CONTA: ela recebe tensao e amperagem e devolve Wh e faixa de km,
 * e a camada de prova dela e a constante com fonte. Estas paginas servem
 * OFERTA DE LOJA, cuja procedencia e um anuncio datado — outra fonte, outra
 * regua de honestidade e outro prazo de validade. Juntar as duas faria a F2
 * decidir sobre dado que ela nao sabe medir, e a primeira vez que um anuncio
 * saisse do ar a calculadora cairia junto.
 *
 * -------------------------------------------------------------------------
 * AS DUAS METADES, E NENHUM NUMERO E DIGITADO AQUI
 * -------------------------------------------------------------------------
 *   - `dados/paginas-de-produto.json` e DECLARADO: titulo, description, a
 *     resposta em duas frases, o "qual escolher" e as perguntas. E a voz do
 *     `VOZ.md`, e a prosa dela traz MOLDES — {N}, {DE}, {ATE}, {MEDIANA},
 *     {DECLARAM_WATT}, {DIZEM_QUAL_WATT}, {SEM_WATT}, {LIDAS}, {RECUSADAS},
 *     {FRASE_DO_ROTULO}, {CHAVE}, {DATA}.
 *   - `dados/vitrine-de-produto.json` e GERADO por
 *     `ferramentas/gerar-vitrine-de-produto.py`, que RECONTA tudo de
 *     `dados/anuncios-por-consulta.json` e sai com codigo 1 se discordar.
 *
 * Quem preenche os moldes e `rdm_produto_preencher()`. Preco escrito a mao na
 * frase e preco que mente na coleta seguinte, calado.
 *
 * -------------------------------------------------------------------------
 * A ORDEM DA TELA E A DA 32.2, E ELA NAO E A DA 32.1
 * -------------------------------------------------------------------------
 * Esta familia de pagina nao tem FORMULARIO, entao o teto de 700 px da 32.5 e
 * da CAIXA DE RESPOSTA e nao de um formulario que nao existe — e a 32.5-b e
 * explicita nisso ("portao que reprova pagina certa e o caminho mais curto para
 * alguem passar a ignora-lo"). De cima para baixo: trilha e H1 · caixa de
 * resposta com o numero em Mono · bloco de compra com `id="comprar"` · a
 * tabela-resumo VISIVEL, que e o que as IAs citam · a malha, tambem visivel
 * porque e alvo de link · o resto nas dobras · a barra fixa do telefone.
 *
 * -------------------------------------------------------------------------
 * O QUE A TABELA NAO TEM, E A DIFERENCA E HONESTIDADE
 * -------------------------------------------------------------------------
 * A 30.3 pede "tabela comparando os produtos". Potencia nominal, velocidade
 * maxima, acelerador e carga maxima NAO estao aqui, e nao e esquecimento: o
 * `niveis_minimos_por_campo` do esquema desta ilha exige nivel 5 ou melhor
 * nesses quatro, e titulo de anuncio e nivel 6. Entao a coluna diz o que o
 * anuncio DECLARA — "declara watt, sem dizer se e nominal ou de pico" — em vez
 * de preencher coluna tecnica com palavra tirada do titulo. A 30.2 manda
 * exatamente isso: "onde faltar, a pagina diz que falta e nao inventa".
 *
 * Sem `<script>` e sem `<style>` no retorno do shortcode (secao 8): o JSON-LD
 * sai no `wp_head` e a folha no `wp_footer`. Foi o E-comercial duplo dentro de
 * `<script>` que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 */

/* A VERSAO MORA NUMA CONSTANTE, e nao so no comentario: `atualizar-manifest.py`
   casa esta constante com o campo `versao` do manifest. */
if ( ! defined( 'RODAMETRIA_PRODUTO_VERSAO' ) ) {
	define( 'RODAMETRIA_PRODUTO_VERSAO', '1.0.0' );
}
if ( ! defined( 'RODAMETRIA_PRODUTO_SECAO' ) ) {
	define( 'RODAMETRIA_PRODUTO_SECAO', 'veiculos' );
}
/* Os ids das options que o Sync grava. Eles saem de constante porque a casca
   1.0.0 digitou `f2_respostas` com sublinhado onde o manifest diz `f2-respostas`
   com hifen, e a pagina caiu no estado degradado honesto sem uma linha vermelha
   em lugar nenhum. */
if ( ! defined( 'RODAMETRIA_ID_DADOS_PRODUTO' ) ) {
	define( 'RODAMETRIA_ID_DADOS_PRODUTO', 'paginas-de-produto' );
}
if ( ! defined( 'RODAMETRIA_ID_DADOS_VITRINE' ) ) {
	define( 'RODAMETRIA_ID_DADOS_VITRINE', 'vitrine-de-produto' );
}

/* ---------------------------------------------------------------------------
 * 1. AS DUAS METADES, LIDAS DAS OPTIONS QUE O SYNC GRAVA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_piso' ) ) {
/** O piso da 30.2. Mora numa funcao para a bancada poder cita-lo sem copia-lo. */
function rdm_produto_piso() {
	return 3;
}
}

if ( ! function_exists( 'rdm_produto_editorial' ) ) {
/** A camada declarada: a voz. Sem ela, nenhuma pagina existe. */
function rdm_produto_editorial() {
	static $d = null;
	if ( null !== $d ) {
		return $d;
	}
	$bruto = rodametria_casca_banco( RODAMETRIA_ID_DADOS_PRODUTO );
	$d     = is_array( $bruto ) ? $bruto : array();

	return $d;
}
}

if ( ! function_exists( 'rdm_produto_vitrine' ) ) {
/** A camada gerada: o numero e o link. */
function rdm_produto_vitrine() {
	static $v = null;
	if ( null !== $v ) {
		return $v;
	}
	$bruto = rodametria_casca_banco( RODAMETRIA_ID_DADOS_VITRINE );
	$v     = array();
	if ( is_array( $bruto ) && ! empty( $bruto['paginas'] ) && is_array( $bruto['paginas'] ) ) {
		foreach ( $bruto['paginas'] as $p ) {
			if ( ! empty( $p['id'] ) ) {
				$v[ $p['id'] ] = $p;
			}
		}
	}

	return $v;
}
}

if ( ! function_exists( 'rdm_produto_paginas_prontas' ) ) {
/**
 * As paginas que EXISTEM: tem camada declarada, tem vitrine, e a vitrine passa o
 * piso da 30.2. Esta funcao e a unica porta — menu, arvore, mae, JSON-LD e
 * instalacao saem todos dela, para nao haver duas listas que discordem.
 *
 * Pagina que perde um anuncio na coleta seguinte SAI DO AR em vez de servir uma
 * lista de dois, e `rodametria_casca_link()` faz o link da mae virar texto
 * sozinho, sem 404.
 */
function rdm_produto_paginas_prontas() {
	static $prontas = null;
	if ( null !== $prontas ) {
		return $prontas;
	}
	$ed      = rdm_produto_editorial();
	$vit     = rdm_produto_vitrine();
	$prontas = array();

	if ( empty( $ed['paginas'] ) || ! is_array( $ed['paginas'] ) ) {
		return $prontas;
	}
	foreach ( $ed['paginas'] as $p ) {
		$id = isset( $p['id'] ) ? $p['id'] : '';
		if ( '' === $id || empty( $vit[ $id ]['linhas'] ) ) {
			continue;
		}
		if ( count( $vit[ $id ]['linhas'] ) < rdm_produto_piso() ) {
			continue;
		}
		$slug = isset( $vit[ $id ]['slug'] ) ? $vit[ $id ]['slug'] : '';
		/* O slug da vitrine vem com a secao na frente (`veiculos/patinete-eletrico`)
		   porque e assim que a arvore da 16.1 o escreve; no WordPress o que vale e
		   a ultima parte, e o pai e quem monta o caminho. */
		$pedacos = explode( '/', $slug );
		$prontas[ $id ] = array(
			'id'          => $id,
			'slug'        => (string) end( $pedacos ),
			'declarado'   => $p,
			'vitrine'     => $vit[ $id ],
		);
	}

	return $prontas;
}
}

/* ---------------------------------------------------------------------------
 * 2. OS MOLDES — nenhum numero e digitado na prosa
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_preencher' ) ) {
function rdm_produto_preencher( $texto, $pagina ) {
	$n = $pagina['vitrine']['numeros'];
	$de = array(
		'{N}'                => (string) $n['n'],
		'{DE}'               => (string) $n['de'],
		'{ATE}'              => (string) $n['ate'],
		'{MEDIANA}'          => (string) $n['mediana'],
		'{DECLARAM_WATT}'    => (string) $n['declaram_watt'],
		'{DIZEM_QUAL_WATT}'  => (string) $n['dizem_qual_watt'],
		'{SEM_WATT}'         => (string) $n['sem_watt'],
		'{LIDAS}'            => (string) $n['lidas'],
		'{RECUSADAS}'        => (string) $n['recusadas'],
		'{FRASE_DO_ROTULO}'  => (string) $n['frase_do_rotulo'],
		'{CHAVE}'            => (string) $pagina['vitrine']['chave_da_loja'],
		'{DATA}'             => (string) $pagina['vitrine']['colhido_em_br'],
	);

	return str_replace( array_keys( $de ), array_values( $de ), (string) $texto );
}
}

if ( ! function_exists( 'rdm_produto_paragrafos' ) ) {
function rdm_produto_paragrafos( $lista, $pagina, $classe = '' ) {
	$html = '';
	foreach ( (array) $lista as $t ) {
		$html .= '<p' . ( '' !== $classe ? ' class="' . esc_attr( $classe ) . '"' : '' ) . '>'
			. esc_html( rdm_produto_preencher( $t, $pagina ) ) . '</p>';
	}

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3. O MAPA DAS PAGINAS — a secao e as filhas entram pelo filtro da casca
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_paginas', function ( $mapa ) {
	$ed = rdm_produto_editorial();
	if ( ! empty( $ed['mae'] ) ) {
		$mapa[ RODAMETRIA_PRODUTO_SECAO ] = array(
			'nome'        => (string) $ed['mae']['nome'],
			'titulo'      => (string) $ed['mae']['titulo'],
			'tipo'        => 'secao',
			'pai'         => 'inicio',
			'no_menu'     => false,
			'description' => (string) $ed['mae']['description'],
		);
	}
	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		$mapa[ $pagina['slug'] ] = array(
			'nome'        => (string) $pagina['declarado']['h1'],
			'titulo'      => (string) $pagina['declarado']['titulo'],
			'tipo'        => 'produto',
			'pai'         => RODAMETRIA_PRODUTO_SECAO,
			'no_menu'     => true,
			'description' => (string) $pagina['declarado']['description'],
		);
	}

	return $mapa;
}, 20 );

if ( ! function_exists( 'rdm_produto_atual' ) ) {
/** A pagina de produto desta requisicao, ou null. */
function rdm_produto_atual() {
	$slug = rodametria_casca_slug_atual();
	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		if ( $pagina['slug'] === $slug ) {
			return $pagina;
		}
	}

	return null;
}
}

/* ---------------------------------------------------------------------------
 * 4. A TABELA-RESUMO — visivel, e e ela que nomeia TODO anuncio uma vez
 *
 * A secao 7 manda: "TODO ITEM DO BANCO E NOMEADO UMA VEZ EM CADA RESPOSTA". O
 * carrossel leva de 3 a 5 pela 32.1; a tabela leva todos, e e por isso que ela
 * nao e recolhida.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_tabela_html' ) ) {
function rdm_produto_tabela_html( $pagina ) {
	$html  = '<div class="rdm-tabela-rolo"><table class="rdm-tabela">';
	$html .= '<caption>Todos os anúncios que entraram, com o preço do dia da leitura'
		. ' e o que cada um declara</caption>';
	$html .= '<thead><tr><th scope="col">Anúncio</th><th scope="col">Preço</th>'
		. '<th scope="col">O que o anúncio declara</th><th scope="col">Loja</th>'
		. '<th scope="col">Comprar</th></tr></thead><tbody>';

	foreach ( $pagina['vitrine']['linhas'] as $item ) {
		$html .= '<tr>';
		$html .= '<td>' . esc_html( $item['nome'] ) . '</td>';
		$html .= '<td class="rdm-num">' . esc_html( $item['preco'] ) . '</td>';
		$html .= '<td>' . esc_html( $item['especificacao'] ) . '</td>';
		$html .= '<td>' . esc_html( $item['loja'] ) . '</td>';
		/* O ROTULO SAI DA CASCA, nunca digitado aqui: ela guarda numa funcao so
		   o rotulo por degrau da escada da 25.1, e a secao 8 registra sete
		   reguas que quebraram por procurar o rotulo de UM degrau. */
		$html .= '<td><a href="' . esc_url( $item['url'] ) . '"'
			. ' rel="sponsored noopener" target="_blank">'
			. esc_html( rodametria_casca_rotulo_da_loja(
				$item['programa'], $item['degrau'] ) ) . '</a></td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	$html .= '<p class="rdm-tabela-nota">'
		. esc_html( rdm_produto_preencher(
			'Preços lidos em {DATA}. Preço de marketplace muda: o que está aqui é o do dia '
			. 'da leitura, não o de agora.', $pagina ) )
		. '</p>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 5. A MALHA — 16.4, e ela e bidirecional e ROTACIONA
 *
 * A 16.9(a) e literal: "cada pagina leva as ate-quatro irmas que vem DEPOIS
 * dela na ordem do mapa, dando a volta no fim". Janela fixa fica verde enquanto
 * a categoria e pequena e deixa a quinta e a sexta filha sem link de entrada
 * nenhum. Com duas filhas, `min(4, irmas)` e UMA, e e isso que sai — e a conta
 * de ENTRADA fecha igual, que e o que a 16.9(b) cobra.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_irmas' ) ) {
function rdm_produto_irmas( $id_atual ) {
	$ordem = array_keys( rdm_produto_paginas_prontas() );
	$onde  = array_search( $id_atual, $ordem, true );
	if ( false === $onde ) {
		return array();
	}
	$total = count( $ordem );
	$fora  = array();
	for ( $i = 1; $i < $total && count( $fora ) < 4; $i++ ) {
		$fora[] = $ordem[ ( $onde + $i ) % $total ];
	}

	return $fora;
}
}

if ( ! function_exists( 'rdm_produto_malha_html' ) ) {
function rdm_produto_malha_html( $pagina ) {
	$prontas = rdm_produto_paginas_prontas();
	$html    = '<nav class="rdm-malha" aria-label="Veja também">';
	$html   .= '<h2>Veja também</h2><ul>';

	foreach ( rdm_produto_irmas( $pagina['id'] ) as $id ) {
		/* A ancora e a CONSULTA da irma, nunca "saiba mais" (16.4c). */
		$link = rodametria_casca_link( $prontas[ $id ]['slug'],
			(string) $prontas[ $id ]['vitrine']['consulta'] );
		if ( '' !== $link ) {
			$html .= '<li>' . $link . '</li>';
		}
	}

	/* 16.4(d): a ferramenta e a pagina que a explica se linkam no corpo. */
	$calc = function_exists( 'rodametria_f2_url' )
		? rodametria_casca_link( 'autonomia-patinete-eletrico',
			'quantos km o elétrico faz de verdade' )
		: '';
	if ( '' !== $calc ) {
		$html .= '<li>' . $calc . '</li>';
	}

	/* 16.4(b): a filha linka a mae no corpo, e nao so na trilha. */
	$mae = rodametria_casca_link( RODAMETRIA_PRODUTO_SECAO, 'todos os veículos elétricos' );
	if ( '' !== $mae ) {
		$html .= '<li>' . $mae . '</li>';
	}

	$html .= '</ul></nav>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6. A PAGINA DE CONSULTA DE PRODUTO
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_pagina_html' ) ) {
function rdm_produto_pagina_html() {
	$pagina = rdm_produto_atual();

	if ( ! $pagina ) {
		/* Pagina DEGRADADA e honesta. Nunca molde cru, nunca numero inventado. */
		return '<div class="rdm-faixa rdm-pagina">'
			. rodametria_casca_trilha_html()
			. '<h1>Esta página está fora do ar neste momento</h1>'
			. '<p class="rdm-promessa">Os anúncios que ela compara não chegaram nesta '
			. 'atualização. Nenhum preço desta página é estimado, então ela prefere não '
			. 'responder a responder errado.</p>'
			. '</div>';
	}

	$d = $pagina['declarado'];
	$n = $pagina['vitrine']['numeros'];

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>' . esc_html( $d['h1'] ) . '</h1>';

	/* (32.2) A CAIXA DE RESPOSTA NO TOPO: o numero e a condicao em uma frase.
	   O numero e a MEDIANA e nao a faixa, porque numero grande em Mono e um
	   numero so — a faixa inteira vive na frase logo abaixo, onde ela cabe. */
	$html .= rodametria_casca_caixa(
		'Preço mediano hoje',
		$n['mediana'],
		'',
		array_map(
			function ( $t ) use ( $pagina ) {
				return rdm_produto_preencher( $t, $pagina );
			},
			(array) $d['resposta'] ),
		'verde' );

	/* (32.2) O BLOCO DE COMPRA logo abaixo da resposta, com `id="comprar"`. */
	$html .= rodametria_casca_bloco_de_compra(
		'À venda agora',
		$pagina['vitrine']['cartoes'],
		rdm_produto_preencher(
			'Os {N} anúncios abaixo foram lidos em {DATA} na busca por "{CHAVE}". '
			. 'A ordem é por venda medida e depois por preço.', $pagina ),
		'Nenhum anúncio desta família passou pela nossa conferência nesta leitura.' );

	/* (32.2) A TABELA-RESUMO VISIVEL — e o que as IAs citam. */
	$html .= '<h2>Todos os anúncios que entraram</h2>';
	$html .= rdm_produto_tabela_html( $pagina );

	/* A PRESTACAO DE CONTAS DA SECAO 7: quem NAO entrou, e por que. A frase e
	   CONTADA da propria vitrine, nunca digitada. */
	$html .= rdm_produto_recusas_html( $pagina );

	/* A malha fica VISIVEL e fora de dobra: ela e alvo de link e nem todo
	   navegador abre um `<details>` fechado ao pular para dentro dele. */
	$html .= rdm_produto_malha_html( $pagina );

	/* (32.2) O RESTO DO TEXTO NAS DOBRAS — e pela 32.3 e pela 22.8 ele continua
	   inteiro no HTML servido, legivel com o JavaScript desligado. */
	$html .= rodametria_casca_dobra( 'O que é, e o que não é',
		rdm_produto_paragrafos( $d['o_que_e'], $pagina )
		. rdm_produto_paragrafos( $d['o_que_nao_e'], $pagina ) );

	$escolher = '<dl class="rdm-escolher">';
	foreach ( (array) $d['qual_escolher'] as $caso ) {
		$escolher .= '<dt>' . esc_html( rdm_produto_preencher( $caso['para'], $pagina ) ) . '</dt>';
		$escolher .= '<dd>' . esc_html( rdm_produto_preencher( $caso['o_que_olhar'], $pagina ) ) . '</dd>';
	}
	$escolher .= '</dl>';
	$html .= rodametria_casca_dobra( 'Qual escolher, pelo seu uso', $escolher );

	$faq = '';
	foreach ( (array) $d['perguntas'] as $q ) {
		$faq .= '<h3>' . esc_html( rdm_produto_preencher( $q['pergunta'], $pagina ) ) . '</h3>';
		$faq .= '<p>' . esc_html( rdm_produto_preencher( $q['resposta'], $pagina ) ) . '</p>';
	}
	$html .= rodametria_casca_dobra( 'Perguntas frequentes', $faq );

	$html .= rodametria_casca_dobra( 'Como sabemos',
		rdm_produto_paragrafos( $d['como_sabemos'], $pagina )
		. '<p>' . esc_html( (string) $d['aviso_de_afiliado'] ) . '</p>' );

	$html .= '</div>';

	/* (32.1, ultima linha) A barra fixa do telefone com o numero e o botao. */
	$html .= rodametria_casca_barra_fixa( 'Mediano', $n['mediana'], '' );

	return $html;
}
}

if ( ! function_exists( 'rdm_produto_recusas_html' ) ) {
/**
 * O QUE A LOJA DEVOLVEU E NAO ENTROU, com a causa CONTADA.
 *
 * A secao 7 manda nomear quem nao entrou e proibe oferecer hipotese: "a recusa
 * nomeia a causa que a pagina MEDIU". Aqui a causa de cada recusa esta gravada
 * no anuncio, e esta funcao so a traduz para portugues de leitor.
 */
function rdm_produto_recusas_html( $pagina ) {
	$n = $pagina['vitrine']['numeros'];
	if ( empty( $n['recusadas'] ) ) {
		return '';
	}
	$nomes = array(
		'acessorio'       => 'acessório (capacete, capa de chuva, pneu, buzina)',
		'brinquedo'       => 'veículo de criança',
		'outro_veiculo'   => 'outro tipo de veículo (triciclo, quadriciclo, hoverboard)',
		'kit_multiplo'    => 'kit com mais de uma unidade',
		'fora_da_familia' => 'outra família de produto',
		'sem_qualificador' => 'anúncio que não diz ser de adulto',
	);
	$pedacos = array();
	foreach ( (array) $n['recusas_por_causa'] as $causa => $quantos ) {
		$rotulo    = isset( $nomes[ $causa ] ) ? $nomes[ $causa ] : $causa;
		$pedacos[] = $quantos . ' ' . $rotulo;
	}

	return '<p class="rdm-recusas">'
		. esc_html( sprintf(
			'A mesma busca devolveu %d ofertas, e %d ficaram de fora: %s. '
			. 'Elas não estão na tabela porque não são o produto desta página.',
			(int) $n['lidas'], (int) $n['recusadas'], implode( ' · ', $pedacos ) ) )
		. '</p>';
}
}

add_shortcode( 'rodametria_produto', 'rdm_produto_pagina_html' );

/* ---------------------------------------------------------------------------
 * 7. A SECAO MAE — 16.4(a): ela lista TODAS as filhas, com a consulta de ancora
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_mae_html' ) ) {
function rdm_produto_mae_html() {
	$ed = rdm_produto_editorial();
	if ( empty( $ed['mae'] ) ) {
		return '<div class="rdm-faixa rdm-pagina">' . rodametria_casca_trilha_html()
			. '<h1>Veículos elétricos</h1>'
			. '<p class="rdm-promessa">Esta seção está fora do ar neste momento.</p></div>';
	}
	$mae     = $ed['mae'];
	$prontas = rdm_produto_paginas_prontas();

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>' . esc_html( $mae['h1'] ) . '</h1>';
	foreach ( (array) $mae['resposta'] as $t ) {
		$html .= '<p class="rdm-promessa">' . esc_html( $t ) . '</p>';
	}

	$html .= '<ul class="rdm-cartoes">';
	foreach ( $prontas as $pagina ) {
		$n    = $pagina['vitrine']['numeros'];
		$link = rodametria_casca_link( $pagina['slug'],
			(string) $pagina['vitrine']['consulta'] );
		if ( '' === $link ) {
			continue;
		}
		$html .= '<li class="rdm-cartao"><h2>' . $link . '</h2>'
			. '<p>' . esc_html( sprintf(
				'%d anúncios de adulto à venda, de %s a %s.',
				(int) $n['n'], (string) $n['de'], (string) $n['ate'] ) ) . '</p></li>';
	}

	/* 16.5, e a nota dela: o cartao da pagina que ainda nao nasceu NAO e link, e
	   a frase diz a CAUSA medida em vez de prometer data. "Em breve" de
	   categoria nao e a frase proibida pela secao 7 — aquela e "link de loja em
	   breve", dentro do bloco de compra, e nao existe aqui. */
	$faltam = rdm_produto_familias_que_faltam();
	if ( $faltam ) {
		$html .= '<li class="rdm-cartao rdm-cartao-mudo"><h2>Ainda não nasceram</h2><ul>';
		foreach ( $faltam as $f ) {
			$html .= '<li><strong>' . esc_html( $f['consulta'] ) . '</strong> — '
				. esc_html( $f['causa'] ) . '</li>';
		}
		$html .= '</ul></li>';
	}
	$html .= '</ul>';

	if ( ! empty( $mae['o_que_falta_dizer'] ) ) {
		$html .= '<p>' . esc_html( (string) $mae['o_que_falta_dizer'] ) . '</p>';
	}

	$calc = rodametria_casca_link( 'autonomia-patinete-eletrico',
		'quantos km o elétrico faz de verdade' );
	if ( '' !== $calc ) {
		$html .= '<p>Antes de fechar a compra, faça a conta de bateria: ' . $calc . '.</p>';
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'rdm_produto_familias_que_faltam' ) ) {
/**
 * As familias que a mae nomeia e que ainda nao tem pagina, com a causa CURTA.
 *
 * A causa longa e medida mora em `dados/consultas-de-produto.json`, que NAO vai
 * para o site (`publicar: false`): ela e cheia de vocabulario de bastidor que a
 * 32.4 proibe na pagina publica. O que vai para a tela e a frase de leitor, e
 * ela mora na camada declarada ao lado da familia.
 */
function rdm_produto_familias_que_faltam() {
	$ed = rdm_produto_editorial();

	return ( ! empty( $ed['mae']['familias_que_faltam'] ) && is_array( $ed['mae']['familias_que_faltam'] ) )
		? $ed['mae']['familias_que_faltam'] : array();
}
}

add_shortcode( 'rodametria_veiculos', 'rdm_produto_mae_html' );

/* ---------------------------------------------------------------------------
 * 8. JSON-LD — ItemList na pagina de produto (30.3) e FAQPage onde ha pergunta
 *
 * O BreadcrumbList nao se repete aqui: ele e da casca.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$pagina = rdm_produto_atual();
	if ( ! $pagina ) {
		return;
	}
	$d = $pagina['declarado'];

	$itens = array();
	foreach ( $pagina['vitrine']['linhas'] as $i => $item ) {
		$produto = array(
			'@type' => 'Product',
			'name'  => $item['nome'],
			'offers' => array(
				'@type'         => 'Offer',
				'price'         => number_format( (float) $item['preco_numero'], 2, '.', '' ),
				'priceCurrency' => 'BRL',
				'url'           => $item['url'],
				'availability'  => 'https://schema.org/InStock',
			),
		);
		if ( ! empty( $item['imagem']['url'] ) ) {
			$produto['image'] = $item['imagem']['url'];
		}
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $i + 1,
			'item'     => $produto,
		);
	}

	$lista = array(
		'@context'        => 'https://schema.org',
		'@type'           => 'ItemList',
		'name'            => $d['h1'],
		'description'     => $d['description'],
		'numberOfItems'   => count( $itens ),
		'itemListElement' => $itens,
	);

	$perguntas = array();
	foreach ( (array) $d['perguntas'] as $q ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => rdm_produto_preencher( $q['pergunta'], $pagina ),
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => rdm_produto_preencher( $q['resposta'], $pagina ),
			),
		);
	}
	$faq = array(
		'@context'   => 'https://schema.org',
		'@type'      => 'FAQPage',
		'mainEntity' => $perguntas,
	);

	$opcoes = JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE;
	echo '<script type="application/ld+json">' . wp_json_encode( $lista, $opcoes ) . "</script>\n";
	if ( $perguntas ) {
		echo '<script type="application/ld+json">' . wp_json_encode( $faq, $opcoes ) . "</script>\n";
	}
}, 20 );

/* ---------------------------------------------------------------------------
 * 9. A FOLHA — no rodape, nunca dentro do shortcode (secao 8)
 *
 * Ela redecora o MINIMO: os componentes do molde sao da casca, e a 32.5-c
 * aprendeu no Clube do Mosaico que folha de snippet que redecora a caixa do
 * molde vence por ordem de carga e desfaz a regra de telefone. Daqui so saem as
 * classes que SO existem nesta familia de pagina.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! rdm_produto_atual() && ! is_page( RODAMETRIA_PRODUTO_SECAO ) ) {
		return;
	}
	?>
<style id="rodametria-produto-css">
body.rdm .rdm-tabela-rolo{overflow-x:auto;-webkit-overflow-scrolling:touch}
body.rdm .rdm-tabela-nota,body.rdm .rdm-recusas{font-size:.9rem;color:var(--rdm-legenda)}
body.rdm .rdm-escolher{margin:0}
body.rdm .rdm-escolher dt{font-family:"Barlow Semi Condensed",Barlow,sans-serif;font-weight:700;margin-top:1rem}
body.rdm .rdm-escolher dd{margin:.25rem 0 0}
body.rdm .rdm-malha{margin:2rem 0}
body.rdm .rdm-malha ul{list-style:none;padding:0;margin:0}
body.rdm .rdm-malha li{padding:.5rem 0;border-top:1px solid var(--rdm-traco)}
body.rdm .rdm-cartoes{list-style:none;padding:0;margin:1.5rem 0;display:grid;gap:1rem}
body.rdm .rdm-cartao{border:1px solid var(--rdm-traco);background:var(--rdm-superficie);padding:1rem}
body.rdm .rdm-cartao h2{margin:0 0 .5rem;font-size:1.15rem}
body.rdm .rdm-cartao p{margin:0}
body.rdm .rdm-cartao-mudo ul{margin:.5rem 0 0;padding-left:1.1rem}
body.rdm .rdm-cartao-mudo li{padding:.25rem 0}
@media (min-width:52rem){body.rdm .rdm-cartoes{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>
	<?php
}, 30 );

/* ---------------------------------------------------------------------------
 * 10. INSTALACAO — pelo gancho da casca, nunca em toda requisicao
 *
 * A mae nasce primeiro: o pai tem de existir antes da filha, senao a 16.2
 * ("pagina sem pai e defeito e nao publica") e a trilha da 16.3 saem erradas.
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_instalar', function ( $relato ) {
	$ed = rdm_produto_editorial();
	if ( empty( $ed['mae'] ) ) {
		$relato[] = 'produto: ERRO — a camada declarada nao chegou';

		return $relato;
	}

	$mae = rodametria_casca_garantir_pagina(
		RODAMETRIA_PRODUTO_SECAO,
		(string) $ed['mae']['titulo'],
		'[rodametria_veiculos]' );

	if ( empty( $mae['id'] ) ) {
		$relato[] = 'veiculos: ERRO — ' . ( isset( $mae['erro'] ) ? $mae['erro'] : 'sem id' );

		return $relato;
	}
	$relato[] = 'veiculos: #' . $mae['id'] . ' (' . $mae['slug'] . ')'
		. ( empty( $mae['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );

	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		$p = rodametria_casca_garantir_pagina(
			$pagina['slug'],
			(string) $pagina['declarado']['titulo'],
			'[rodametria_produto]',
			(int) $mae['id'] );
		if ( empty( $p['id'] ) ) {
			$relato[] = 'produto/' . $pagina['slug'] . ': ERRO — '
				. ( isset( $p['erro'] ) ? $p['erro'] : 'sem id' );
			continue;
		}
		$relato[] = 'produto/' . $pagina['slug'] . ': #' . $p['id'] . ' (' . $p['slug'] . ')'
			. ( empty( $p['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );
	}

	return $relato;
}, 20 );

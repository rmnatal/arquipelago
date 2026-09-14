/**
 * CLUBE DO MOSAICO — A FAMÍLIA DAS TÉCNICAS
 * Snippet "Clube do Mosaico Técnicas", registrado pelo Sync.
 *
 * A primeira página da Escola, e a que o Raphael pediu por nome em 14/09/2026:
 * o Picassiete, o mosaico feito de louça quebrada.
 *
 * -------------------------------------------------------------------------
 * POR QUE ELA NASCE HOJE, depois de duas execuções dizendo que não nascia
 * -------------------------------------------------------------------------
 * A `ARVORE.md` seção 4b tinha três portões fechados e os três decidiam errado,
 * o que foi remedido às 21h17Z de 14/09/2026 e está escrito lá:
 *
 *   1. O portão de 3 itens de banco (seção 9 do ARQUIPELAGO.md) contava só
 *      TESSELA — quantos produtos da categoria `pastilha` o banco tem com o
 *      tipo que a técnica cita. Caco de prato não tem fabricante, então ele
 *      lia zero e leria zero para sempre. Só que esta página não recomenda
 *      caquinho: ela responde COM O QUE COLAR o caquinho, e isso é produto
 *      com fabricante, declaração datada e link. São CINCO.
 *   2. A 16.5 (categoria só nasce com 3 filhas) não se aplica: a técnica nasce
 *      filha DIRETA de `/como-fazer/`, não dentro de uma categoria.
 *   3. "Nenhum número autoriza leva nova" é o oposto do que a seção 21.1 diz
 *      para ilha ABAIXO DO PISO, e esta tem 11 URLs e `piso: abaixo` escrito
 *      no cabeçalho do `ESTADO.md`. Virou a 21.8 do contrato.
 *
 * -------------------------------------------------------------------------
 * A DECISÃO DE DESENHO QUE MANDA NESTE ARQUIVO: ELE NÃO DECIDE NADA
 * -------------------------------------------------------------------------
 * Nenhuma linha daqui escolhe cola. Quem escolhe é `cdm_f2_celula_cola()`, a
 * régua da F2, que já está no ar desde 11/09/2026 e já é medida por
 * `teste-f2.php` e pelo `validar-banco.py`. Esta página CHAMA aquela régua para
 * a louça quebrada e imprime o resultado.
 *
 * Isso não é economia de linha: é a única forma de a grade desta página não
 * envelhecer separada da ferramenta. Uma segunda cópia da decisão é a cicatriz
 * que esta ilha pagou duas vezes só em 14/09 — com a palavra-chave da busca que
 * existia no banco e que nenhum snippet lia, e com o `itens_sem_piso`, que
 * contava uma coisa e chamava de outra. A mesma razão vale para o texto: a
 * definição, a fonte e a consulta-alvo do Picassiete saem de `dados/tecnicas.json`,
 * que é o banco, e não de uma frase digitada aqui.
 *
 * O QUE ACONTECE QUANDO A F2 NÃO ESTÁ CARREGADA: a página diz que não conseguiu
 * medir, e não inventa. É a mesma trava do banco ausente que a Robometria
 * escreveu em 11/09/2026.
 *
 * -------------------------------------------------------------------------
 * A PRESTAÇÃO DE CONTAS DA SEÇÃO 7, e ela é o portão mais duro desta página
 * -------------------------------------------------------------------------
 * "Cada item da categoria consultada aparece exatamente uma vez na prosa da
 * resposta — ou na frase que o recomenda, e aí ele está na vitrine, ou numa
 * linha que diz por que ele não está." São 7 colas no banco: 5 entram e 2 não.
 * As duas que não entram são nomeadas com a causa que a PÁGINA MEDIU, contada
 * célula a célula, nunca com uma hipótese escrita à mão.
 *
 * -------------------------------------------------------------------------
 * O QUE ESTA PÁGINA SE RECUSA A RESPONDER, e diz isso ao leitor
 * -------------------------------------------------------------------------
 * O REJUNTE. A régua do rejunte decide por largura de junta em milímetro e por
 * ambiente, e não olha o material do caquinho; e as cinco técnicas do banco têm
 * `junta_tipica_mm` null, porque nenhuma fonte colhida declara folga em
 * milímetro para elas. Escolher um rejunte por semelhança seria inventar o
 * número que falta. A página manda para a F2, que pergunta a junta.
 */

if ( ! defined( 'CDM_TECNICAS_VERSAO' ) ) {
	define( 'CDM_TECNICAS_VERSAO', '1.0.0' );
}

/* A TÉCNICA DESTA PÁGINA. Uma constante e não um laço sobre o banco, e a razão
   é a mesma da seção 4b da ARVORE: das cinco técnicas do banco, só DUAS passam
   no portão de 3 itens hoje (trencadís e Picassiete), e a leva desta execução é
   de UMA página. Quem publicar a segunda acrescenta o slug e o id aqui — e o
   `teste-tecnicas.php` cobra que toda técnica registrada tenha passado no
   portão, medido contra o banco. */
if ( ! defined( 'CDM_TECNICAS_ID' ) ) {
	define( 'CDM_TECNICAS_ID', 'picassiette' );
}
if ( ! defined( 'CDM_TECNICAS_SLUG' ) ) {
	/* Nível 3 com a mãe de nível 1 direto — DOIS segmentos de URL em vez de três,
	   o mesmo estado de transição em que a F2 e a F1 vivem desde o bloco 4 (ver a
	   seção 2 do ARVORE.md). O nível declarado é o da árvore final, não a contagem
	   de barras. NÃO é
	   `/tecnicas/Picassiete/`, que foi o endereço que o despacho pediu: a 16.1
	   proíbe página solta na raiz desde 11/09/2026. E não é
	   `/como-fazer/tecnicas/o-que-e-mosaico-picassiete/` porque a categoria de
	   nível 2 só nasce com três filhas (16.5), e mover URL de página posicionada
	   é proibido pela 12.1 — então o endereço de hoje tem a mãe que JÁ existe.
	   O slug é a consulta-alvo do banco, sem acento e com hífen. */
	define( 'CDM_TECNICAS_SLUG', 'como-fazer/o-que-e-mosaico-picassiete' );
}
if ( ! defined( 'CDM_TECNICAS_TITULO' ) ) {
	/* UM NOME POR PÁGINA, em toda superfície: cartão da Escola, degrau da
	   trilha, H1 e <title>. 40 caracteres; com o sufixo do site o <title> fica
	   em 59, abaixo do teto de 65. E ele carrega a consulta-alvo do banco
	   ("o que e mosaico picassiete") com as palavras que a pessoa digita. */
	define( 'CDM_TECNICAS_TITULO', 'O que é mosaico Picassiete, e como colar' );
}

/* A TESSELA QUE ESTA PÁGINA RESOLVE não é escrita aqui: sai do campo
   `materiais_tipicos` do banco de técnicas. Se um dia a fonte mudar, a página
   muda junto — e se o campo ficar vazio, a página não recomenda nada. */

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — a página e o cartão na Escola
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	$paginas[ CDM_TECNICAS_SLUG ] = array(
		'titulo'   => CDM_TECNICAS_TITULO,
		'conteudo' => '[cdm_tecnica]',
		'pai'      => 'como-fazer',
	);

	return $paginas;
} );

add_filter( 'cdm_tecnicas_publicadas', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	$lista[] = array(
		'id'     => CDM_TECNICAS_ID,
		'slug'   => CDM_TECNICAS_SLUG,
		'titulo' => CDM_TECNICAS_TITULO,
		'resumo' => 'Mosaico de louça quebrada — prato, xícara, azulejo antigo. O que é, de onde vem o nome e com o que colar o caquinho em cada superfície.',
	);

	return $lista;
} );

/* ---------------------------------------------------------------------------
 * 2. O banco de técnicas, lido da option que o Sync grava
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_banco' ) ) {
function cdm_tecnicas_banco() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}
	$bruto = get_option( 'clubedomosaico_dados_tecnicas' );
	if ( is_string( $bruto ) ) {
		$bruto = json_decode( $bruto, true );
	}
	$banco = array( 'tecnicas' => array() );
	if ( is_array( $bruto ) && ! empty( $bruto['tecnicas'] ) && is_array( $bruto['tecnicas'] ) ) {
		foreach ( $bruto['tecnicas'] as $t ) {
			if ( ! empty( $t['id'] ) ) {
				$banco['tecnicas'][ $t['id'] ] = $t;
			}
		}
	}

	return $banco;
}
}

if ( ! function_exists( 'cdm_tecnicas_atual' ) ) {
/** O registro da técnica desta página, ou array() quando o banco não chegou. */
function cdm_tecnicas_atual() {
	$banco = cdm_tecnicas_banco();

	return isset( $banco['tecnicas'][ CDM_TECNICAS_ID ] ) ? $banco['tecnicas'][ CDM_TECNICAS_ID ] : array();
}
}

if ( ! function_exists( 'cdm_tecnicas_tessela' ) ) {
/**
 * O material do caquinho, lido do banco. '' quando o banco não declara.
 *
 * UMA tessela, e a página é honesta sobre isso: o Picassiete declara
 * `caco_louca` e só. Se um dia declarar duas, a primeira é a que manda a grade
 * e o teste cobra que a página diga qual — grade que soma duas tesselas
 * diferentes numa célula só afirma sobre um material que não existe.
 */
function cdm_tecnicas_tessela() {
	$t = cdm_tecnicas_atual();
	$m = ( isset( $t['materiais_tipicos'] ) && is_array( $t['materiais_tipicos'] ) ) ? $t['materiais_tipicos'] : array();

	return $m ? (string) reset( $m ) : '';
}
}

if ( ! function_exists( 'cdm_tecnicas_pronta' ) ) {
/** Dá para medir? Precisa do banco de técnicas E da régua da F2. */
function cdm_tecnicas_pronta() {
	return '' !== cdm_tecnicas_tessela()
		&& function_exists( 'cdm_f2_celula_cola' )
		&& function_exists( 'cdm_f2_rotulos' );
}
}

/* ---------------------------------------------------------------------------
 * 3. A GRADE — 9 superfícies x 5 lugares, calculada pela régua da F2
 *
 * É a "tabela de exemplos pré-renderizada" da seção 5 do contrato: casos já
 * resolvidos, servidos no HTML, cobrindo a faixa real de uso. Um modelo de
 * linguagem lê os 45 casos sem preencher formulário nenhum — que é exatamente o
 * defeito que a Aquametria descobriu tarde e que a seção 5 existe para impedir.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_grade' ) ) {
function cdm_tecnicas_grade() {
	static $grade = null;
	if ( null !== $grade ) {
		return $grade;
	}
	$grade = array();
	if ( ! cdm_tecnicas_pronta() ) {
		return $grade;
	}
	$rot     = cdm_f2_rotulos();
	$tessela = cdm_tecnicas_tessela();

	foreach ( array_keys( $rot['base'] ) as $base ) {
		foreach ( array_keys( $rot['ambiente'] ) as $ambiente ) {
			$c        = cdm_f2_celula_cola( $base, $ambiente, $tessela );
			$elegivel = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
			$grade[]  = array(
				'base'       => $base,
				'ambiente'   => $ambiente,
				'topo'       => $c['recomendados_topo'],
				'elegiveis'  => $elegivel,
				'quantos'    => count( $elegivel ),
				'ressalva'   => $c['mencionados_com_ressalva'],
				'proibicao'  => $c['eliminados_por_proibicao'],
				'silencio'   => $c['eliminados_por_silencio'],
				'condicao'   => $c['eliminados_por_condicao'],
			);
		}
	}

	return $grade;
}
}

if ( ! function_exists( 'cdm_tecnicas_celula' ) ) {
function cdm_tecnicas_celula( $base, $ambiente ) {
	foreach ( cdm_tecnicas_grade() as $c ) {
		if ( $c['base'] === $base && $c['ambiente'] === $ambiente ) {
			return $c;
		}
	}

	return null;
}
}

if ( ! function_exists( 'cdm_tecnicas_contas' ) ) {
/**
 * Os números que a página afirma — TODOS contados da grade, nenhum digitado.
 *
 * `fora` é a prestação de contas da seção 7: para cada cola do banco que não
 * entra em célula nenhuma, em quantas das 45 ela aparece em cada balde. A causa
 * que a página escreve é a do balde de maior contagem, e vem com o número do
 * lado. É a diferença entre "a recusa nomeia a causa que a página mediu" e uma
 * hipótese com cara de explicação, que é o que a seção 7 proíbe desde 12/09.
 */
function cdm_tecnicas_contas() {
	static $contas = null;
	if ( null !== $contas ) {
		return $contas;
	}
	$grade = cdm_tecnicas_grade();

	$dentro  = array();
	$celulas = count( $grade );
	$com_min = 0;
	$zeradas = 0;
	$baldes  = array();

	foreach ( $grade as $c ) {
		foreach ( $c['elegiveis'] as $id ) {
			$dentro[ $id ] = true;
		}
		if ( $c['quantos'] >= 3 ) {
			$com_min++;
		}
		if ( 0 === $c['quantos'] ) {
			$zeradas++;
		}
		foreach ( array( 'ressalva', 'proibicao', 'silencio', 'condicao' ) as $balde ) {
			foreach ( $c[ $balde ] as $id ) {
				if ( ! isset( $baldes[ $id ] ) ) {
					$baldes[ $id ] = array( 'ressalva' => 0, 'proibicao' => 0, 'silencio' => 0, 'condicao' => 0 );
				}
				$baldes[ $id ][ $balde ]++;
			}
		}
	}

	/* O BANCO INTEIRO, não só quem apareceu: a soma dos nomeados tem de fechar
	   com o tamanho do banco, e isso se conta varrendo o banco, nunca a lista de
	   quem passou (seção 7, 12/09/2026). */
	$todas = array();
	if ( function_exists( 'cdm_f2_banco' ) ) {
		foreach ( cdm_f2_banco()['materiais'] as $id => $m ) {
			if ( 'cola' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
				$todas[] = $id;
			}
		}
	}

	$fora = array();
	foreach ( $todas as $id ) {
		if ( isset( $dentro[ $id ] ) ) {
			continue;
		}
		$b = isset( $baldes[ $id ] ) ? $baldes[ $id ] : array( 'ressalva' => 0, 'proibicao' => 0, 'silencio' => 0, 'condicao' => 0 );

		/* TODOS OS BALDES COM CONTAGEM, não só o maior. A seção 7 do contrato é
		   literal desde 12/09/2026: "causa que o código separa, o texto separa —
		   misturar duas causas numa frase é inventar uma delas". O Durepoxi é o
		   caso vivo: ele cai por silêncio em 25 células E aparece com ressalva em
		   20, e escrever só o silêncio faria a página afirmar que o fabricante
		   nunca nomeia uma dessas superfícies, o que é falso em 20 delas. */
		arsort( $b );
		$causas = array();
		foreach ( $b as $nome => $n ) {
			if ( $n > 0 ) {
				$causas[] = array( 'causa' => $nome, 'quantas' => $n );
			}
		}
		$fora[] = array( 'id' => $id, 'causas' => $causas, 'baldes' => $b );
	}

	$contas = array(
		'celulas'        => $celulas,
		'com_o_minimo'   => $com_min,
		'sem_nenhuma'    => $zeradas,
		'dentro'         => array_keys( $dentro ),
		'fora'           => $fora,
		'colas_no_banco' => count( $todas ),
	);

	return $contas;
}
}

/* ---------------------------------------------------------------------------
 * 4. O texto — a resposta antes da explicação (seção 5, item 2)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_causa_em_palavras' ) ) {
/**
 * As causas de um produto ficar fora, UMA FRASE POR CAUSA e com o número ao lado.
 *
 * A seção 7 do contrato, desde 12/09/2026: "causa que o código separa, o texto
 * separa — grupo por motivo, com nome próprio; misturar duas causas numa frase é
 * inventar uma delas". Aqui o código separa quatro e o texto separa quatro.
 */
function cdm_tecnicas_causa_em_palavras( $causas, $celulas ) {
	$mapa = array(
		'silencio'  => 'o fabricante não declara essa superfície',
		'proibicao' => 'o próprio fabricante desaconselha',
		'ressalva'  => 'entra só com ressalva, porque a melhor fonte que temos dele não é a ficha técnica — e ressalva não vira recomendação aqui',
		'condicao'  => 'o fabricante exige que uma das superfícies seja porosa, e louça esmaltada não é',
	);
	$partes = array();
	foreach ( (array) $causas as $c ) {
		$texto    = isset( $mapa[ $c['causa'] ] ) ? $mapa[ $c['causa'] ] : 'não há declaração que o sustente';
		$partes[] = $texto . ' em ' . (int) $c['quantas'] . ' das ' . (int) $celulas;
	}

	return implode( '; ', $partes );
}
}

if ( ! function_exists( 'cdm_tecnicas_faq' ) ) {
/**
 * Uma fonte só para a tela e para o FAQPage — o mesmo desenho da F2. Schema que
 * promete resposta que a página não dá é o que faz FAQPage virar spam.
 */
function cdm_tecnicas_faq() {
	$t       = cdm_tecnicas_atual();
	$contas  = cdm_tecnicas_contas();
	$interno = cdm_tecnicas_celula( 'ceramica_esmaltada_porcelana', 'interno_seco' );
	$nomes   = array();
	if ( $interno ) {
		foreach ( $interno['elegiveis'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
	}

	return array(
		array(
			'pergunta' => 'O que é mosaico Picassiete?',
			'resposta' => isset( $t['definicao'] ) ? (string) $t['definicao']
				: 'Mosaico feito com louça quebrada — prato, xícara, azulejo antigo — no lugar da pastilha comprada.',
		),
		array(
			'pergunta' => 'Qual cola usar para colar caquinho de louça num vaso de cerâmica dentro de casa?',
			'resposta' => $nomes
				? 'Sobre cerâmica, dentro de casa e em lugar seco, ' . count( $nomes ) . ' adesivos do nosso banco servem: '
					. cdm_f2_lista_humana( $nomes ) . '. Todos entram pela lista que o próprio fabricante publica.'
				: 'A medição não chegou ao site; a resposta não é chutada.',
		),
		array(
			'pergunta' => 'Dá para fazer Picassiete em peça que fica no sol e na chuva?',
			'resposta' => 'Dá, e a escolha muda: das ' . (int) $contas['celulas'] . ' combinações de superfície e lugar desta página, '
				. (int) $contas['sem_nenhuma'] . ' não têm nenhum adesivo que o fabricante sustente — e a maioria delas é justamente o contato permanente com água. A página diz quais são, em vez de empurrar um produto.',
		),
		array(
			'pergunta' => 'E o rejunte do Picassiete?',
			'resposta' => 'Esta página não responde. O rejunte se decide pela largura da junta em milímetro, e nenhuma fonte que lemos sobre Picassiete declara essa folga — então perguntamos a junta na ferramenta, em vez de escolher por semelhança.',
		),
	);
}
}

add_shortcode( 'cdm_tecnica', function () {
	$t   = cdm_tecnicas_atual();
	$rot = function_exists( 'cdm_f2_rotulos' ) ? cdm_f2_rotulos() : array();

	if ( ! cdm_tecnicas_pronta() ) {
		return '<div class="cdm-bloco"><div class="cdm-vazio">'
			. '<h3>A medição desta página ainda não chegou ao site</h3>'
			. '<p>Ela não vai inventar uma recomendação enquanto isso. Volte daqui a pouco, ou use o '
			. ( function_exists( 'cdm_casca_link_html' ) ? cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' ) : 'guia de materiais' )
			. ', que pergunta a superfície e o lugar.</p></div></div>';
	}

	$contas  = cdm_tecnicas_contas();
	$tessela = cdm_tecnicas_tessela();
	$html    = '<div class="cdm-bloco cdm-tec">';

	/* A LINHA MESTRA — o que a pessoa recebe, em uma linha. Sem fabricante, sem
	   data, sem a palavra `tessela`: o VOZ.md manda isso para a camada de prova. */
	$html .= '<p class="cdm-linha-mestra">Picassiete é mosaico de louça quebrada — prato, xícara, azulejo antigo. Aqui está o que é, de onde vem o nome, e com o que colar o caquinho em cada superfície e em cada lugar da casa.</p>';

	/* A RESPOSTA ANTES DA EXPLICAÇÃO (seção 5, item 2), em frase que sobrevive a
	   ser citada fora de contexto. O número é contado da grade. */
	$html .= '<div class="cdm-tec-resposta">';
	$html .= '<p class="cdm-tec-frase">Para colar caquinho de louça, <strong>' . count( $contas['dentro'] ) . ' dos '
		. (int) $contas['colas_no_banco'] . ' adesivos do nosso banco</strong> servem em pelo menos uma situação — e qual deles serve muda com a superfície e com o lugar. '
		. 'Das <strong>' . (int) $contas['celulas'] . '</strong> combinações desta página, '
		. (int) $contas['com_o_minimo'] . ' têm três ou mais opções e <strong>' . (int) $contas['sem_nenhuma']
		. ' não têm nenhuma</strong>, e a gente diz quais são em vez de empurrar um produto.</p>';

	/* A PROCEDÊNCIA DESCE UM PARÁGRAFO, dentro da caixa da resposta e marcada
	   como prova — o mesmo desenho que a Aquametria adotou em 11/09/2026 para a
	   seção 5 continuar inteira sem a voz do VOZ.md ser quebrada no topo. */
	if ( ! empty( $t['definicao_fonte_id'] ) && ! empty( $t['fontes'][ $t['definicao_fonte_id'] ] ) ) {
		$f     = $t['fontes'][ $t['definicao_fonte_id'] ];
		$html .= '<p class="cdm-prova cdm-tec-prova">Cada adesivo entra ou sai pela lista que o próprio fabricante publica, recalculada na hora; a definição do Picassiete vem de '
			. esc_html( isset( $f['o_que_e'] ) ? $f['o_que_e'] : 'uma fonte de enciclopédia' )
			. ( ! empty( $f['url'] ) ? ' (<a href="' . esc_url( $f['url'] ) . '" rel="nofollow noopener" target="_blank">fonte</a>)' : '' )
			. ( ! empty( $f['data_leitura'] ) ? ', lida em ' . esc_html( cdm_casca_data_br( $f['data_leitura'] ) ) : '' )
			. '.</p>';
	}
	$html .= '</div>';

	/* O QUE É — o texto vem do banco, nunca digitado aqui. */
	$html .= '<div class="cdm-secao"><h2>O que é, e de onde vem o nome</h2>';
	if ( ! empty( $t['definicao'] ) ) {
		$html .= '<p>' . esc_html( $t['definicao'] ) . '</p>';
	}
	$html .= '<p>A diferença para o resto do mosaico está no material: em vez de pastilha comprada em placa, entra o que sobrou de uma louça. Isso muda duas coisas práticas — o caquinho tem espessuras diferentes na mesma peça, e a face esmaltada do prato é lisa, então a cola precisa segurar sobre esmalte e não sobre porosidade.</p>';
	$html .= '<p>O ' . cdm_casca_link_html( 'como-fazer', 'Como fazer' ) . ' é a seção onde este tipo de página vive; o '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
		. ' responde a mesma pergunta para qualquer caquinho, perguntando a superfície e o lugar.</p></div>';

	/* A GRADE PRÉ-RENDERIZADA */
	$html .= '<div class="cdm-secao"><h2>Com o que colar, superfície por superfície</h2>';
	$html .= '<p>A linha é a superfície sobre a qual você vai colar — o vaso, o quadro, o tampo. A coluna é onde a peça vai viver. Em cada cruzamento está o que os fabricantes sustentam, e quando não há nada, está escrito que não há.</p>';
	$html .= '<div class="cdm-tec-rolagem"><table class="cdm-tec-tabela"><thead><tr><th scope="col">Sobre o que você vai colar</th>';
	foreach ( $rot['ambiente'] as $amb => $rotulo ) {
		$html .= '<th scope="col">' . esc_html( $rot['ambiente_curto'][ $amb ] ) . '</th>';
	}
	$html .= '</tr></thead><tbody>';
	foreach ( $rot['base'] as $base => $rotulo ) {
		$html .= '<tr><th scope="row">' . esc_html( $rotulo ) . '</th>';
		foreach ( array_keys( $rot['ambiente'] ) as $amb ) {
			$c = cdm_tecnicas_celula( $base, $amb );
			if ( ! $c || 0 === $c['quantos'] ) {
				$html .= '<td class="cdm-tec-vazia">nenhum que o fabricante sustente</td>';
				continue;
			}
			$nomes = array();
			foreach ( $c['topo'] as $id ) {
				$nomes[] = esc_html( cdm_f2_nome( $id ) );
			}
			$extra  = $c['quantos'] - count( $c['topo'] );
			$html  .= '<td>' . cdm_f2_lista_humana( $nomes )
				. ( $extra > 0 ? '<span class="cdm-tec-mais"> e mais ' . (int) $extra . '</span>' : '' )
				. '</td>';
		}
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="cdm-tec-legenda">Cada célula traz o que ficou em primeiro lugar naquela combinação; "e mais" é quanta opção sobra abaixo dele. Quem quiser a lista inteira de uma combinação, com o que foi descartado e por quê, abre o '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor' ) . '.</p></div>';

	/* A VITRINE — bloco de compra ANTES da prova de procedência (seção 7). */
	$html .= '<div class="cdm-secao"><h2>Os adesivos que entram</h2>';
	$nomes_dentro = array();
	foreach ( $contas['dentro'] as $id ) {
		$nomes_dentro[] = cdm_f2_nome( $id );
	}
	$html .= '<p>São estes ' . count( $contas['dentro'] ) . ', e cada um entra por uma combinação diferente: '
		. cdm_f2_lista_humana( array_map( 'esc_html', $nomes_dentro ) ) . '.</p>';
	$html .= '<ul class="cdm-f2-cartoes">';
	foreach ( $contas['dentro'] as $id ) {
		$onde = array();
		foreach ( cdm_tecnicas_grade() as $c ) {
			if ( in_array( $id, $c['elegiveis'], true ) ) {
				$onde[ $c['base'] ] = true;
			}
		}
		$quantas = count( $onde );
		$motivo  = 'serve em ' . $quantas . ' das ' . count( $rot['base'] ) . ' superfícies desta página, pela lista do fabricante';
		$html   .= cdm_f2_cartao_html( $id, esc_html( $motivo ) );
	}
	$html .= '</ul>';
	$html .= '<p class="cdm-tec-aviso">Alguns links acima são de afiliado: se você comprar por eles, a gente ganha uma comissão e você não paga nada a mais. O link de <em>fonte</em> em cada cartão não é de afiliado — ele existe para você conferir a declaração do fabricante.</p></div>';

	/* A PRESTAÇÃO DE CONTAS — quem NÃO entrou, e por quê (seção 7). */
	if ( $contas['fora'] ) {
		$html .= '<div class="cdm-secao"><h2>E os que não entram</h2>';
		$html .= '<p>O banco tem ' . (int) $contas['colas_no_banco'] . ' adesivos. ' . count( $contas['dentro'] )
			. ' aparecem acima; os outros ' . count( $contas['fora'] ) . ' não entram em nenhuma das '
			. (int) $contas['celulas'] . ' combinações, e ficam nomeados aqui para a conta fechar:</p><ul class="cdm-lista">';
		foreach ( $contas['fora'] as $f ) {
			$html .= '<li><strong>' . esc_html( cdm_f2_nome( $f['id'] ) ) . '</strong> — '
				. esc_html( cdm_tecnicas_causa_em_palavras( $f['causas'], $contas['celulas'] ) ) . '.</li>';
		}
		$html .= '</ul></div>';
	}

	/* A RECUSA, com a causa medida (seção 7). */
	$html .= '<div class="cdm-secao"><h2>O que esta página não responde</h2>';
	$html .= '<p><strong>O rejunte.</strong> Ele não se escolhe pelo material do caquinho: escolhe-se pela largura da junta, em milímetro, e pelo lugar. Nenhuma das fontes que lemos sobre Picassiete declara essa folga — as duas falam do espaço entre os cacos sem dar número —, e escolher por semelhança seria inventar justamente o número que falta. Quem já sabe a junta da peça pergunta no '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor' ) . ', que responde rejunte junto com a cola.</p></div>';

	/* FAQ na tela — mesma fonte do FAQPage. */
	$html .= '<div class="cdm-secao"><h2>Perguntas que chegam</h2><dl class="cdm-tec-faq">';
	foreach ( cdm_tecnicas_faq() as $p ) {
		$html .= '<dt>' . esc_html( $p['pergunta'] ) . '</dt><dd>' . esc_html( $p['resposta'] ) . '</dd>';
	}
	$html .= '</dl></div>';

	/* COMO SABEMOS — camada de prova, no fim, como o VOZ.md manda. */
	$html .= '<div class="cdm-secao cdm-prova"><h2>Como sabemos</h2>';
	$html .= '<p>A recomendação de cola desta página não é escrita: é recalculada, a cada carregamento, das listas que os fabricantes publicam, pela mesma régua do '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola' )
		. ' — não há uma segunda tabela aqui que possa envelhecer sozinha. Produto cuja melhor fonte não é a ficha técnica não vira recomendação; ele aparece como possibilidade, e esta página não o conta.</p>';
	if ( ! empty( $t['fontes'] ) ) {
		$html .= '<ul class="cdm-lista">';
		foreach ( $t['fontes'] as $f ) {
			$html .= '<li>' . esc_html( isset( $f['o_que_e'] ) ? $f['o_que_e'] : '' )
				. ( ! empty( $f['url'] ) ? ' — <a href="' . esc_url( $f['url'] ) . '" rel="nofollow noopener" target="_blank">fonte</a>' : '' )
				. ( ! empty( $f['data_leitura'] ) ? ', lida em ' . esc_html( cdm_casca_data_br( $f['data_leitura'] ) ) : '' )
				. ( ! empty( $f['leitura'] ) ? '. ' . esc_html( $f['leitura'] ) : '' )
				. '</li>';
		}
		$html .= '</ul>';
	}
	if ( ! empty( $t['revisao_tecnica'] ) && 'revisada' !== $t['revisao_tecnica'] ) {
		$html .= '<p>O texto sobre a técnica ainda <strong>não foi revisado por quem faz mosaico à mão</strong>. Está escrito assim de propósito: a revisora existe, é a artesã do ateliê, e esta página prefere dizer que a revisão não aconteceu a carimbar uma que não houve.</p>';
	}
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Cabeça da página — description e JSON-LD
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_e_minha_pagina' ) ) {
function cdm_tecnicas_e_minha_pagina() {
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_TECNICAS_SLUG === cdm_casca_slug_atual();
}
}

add_action( 'wp_head', function () {
	if ( ! cdm_tecnicas_e_minha_pagina() ) {
		return;
	}

	echo '<meta name="description" content="'
		. esc_attr( 'Mosaico Picassiete: o que é o mosaico de louça quebrada e com o que colar o caquinho em cada superfície — cerâmica, vidro, espelho, MDF, cimento ou metal — dentro de casa ou no sol e na chuva.' )
		. '">' . "\n";

	$limpa     = home_url( '/' . CDM_TECNICAS_SLUG . '/' );
	$t         = cdm_tecnicas_atual();
	$perguntas = array();
	foreach ( cdm_tecnicas_faq() as $p ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $p['pergunta'],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p['resposta'] ),
		);
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type'         => 'Article',
				'@id'           => $limpa . '#artigo',
				'headline'      => CDM_TECNICAS_TITULO,
				'url'           => $limpa,
				'inLanguage'    => 'pt-BR',
				'description'   => isset( $t['definicao'] ) ? (string) $t['definicao'] : '',
				'about'         => array(
					'@type' => 'Thing',
					'name'  => isset( $t['nome'] ) ? (string) $t['nome'] : 'Picassiete',
				),
				'publisher'     => array( '@id' => home_url( '/#organizacao' ) ),
				'isPartOf'      => array( '@id' => home_url( '/#site' ) ),
			),
			array(
				'@type'      => 'FAQPage',
				'@id'        => $limpa . '#perguntas',
				'mainEntity' => $perguntas,
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-tecnicas-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 6. Folha — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML. Foi o defeito que derrubou
 * cinco calculadoras da Aquametria em 08/09/2026.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_tecnicas_e_minha_pagina() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-tecnicas-css">
.cdm-tec-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-tec-frase{font-size:1.15rem;line-height:1.5;margin:0;}
.cdm-tec-prova{margin:1rem 0 0;}
.cdm-tec-rolagem{overflow-x:auto;margin:1.2rem 0;}
.cdm-tec-tabela{border-collapse:collapse;width:100%;min-width:42rem;font-size:.95rem;}
.cdm-tec-tabela th,.cdm-tec-tabela td{border:1px solid var(--cdm-traco);padding:.55rem .6rem;text-align:left;vertical-align:top;}
.cdm-tec-tabela thead th{font-family:var(--cdm-display);font-weight:600;background:var(--cdm-papel);}
.cdm-tec-tabela tbody th{font-weight:600;background:var(--cdm-papel);}
.cdm-tec-vazia{color:var(--cdm-legenda);}
.cdm-tec-mais{color:var(--cdm-legenda);}
.cdm-tec-legenda{color:var(--cdm-legenda);font-size:.9rem;}
.cdm-tec-aviso{color:var(--cdm-legenda);font-size:.9rem;}
.cdm-tec-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .3rem;}
.cdm-tec-faq dd{margin:0;}
@media (max-width:600px){.cdm-tec-tabela{min-width:34rem;font-size:.9rem;}}
</style>
HTML;
}, 20 );

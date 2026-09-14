/**
 * CLUBE DO MOSAICO — A FAMÍLIA DAS TÉCNICAS
 * Snippet "Clube do Mosaico Técnicas", registrado pelo Sync.
 *
 * A primeira página da Escola nasceu em 14/09/2026: o Picassiete, o mosaico
 * feito de louça quebrada, que o Raphael pediu por nome. A segunda nasce aqui:
 * o trencadís, o caquinho de Gaudí.
 *
 * -------------------------------------------------------------------------
 * O QUE MUDOU NA 1.1.0, e é a razão de este arquivo ter sido reescrito
 * -------------------------------------------------------------------------
 * A 1.0.0 era uma página, não uma família: o id, o slug e o título eram três
 * CONSTANTES, e a grade, as contas e a cabeça liam essas constantes direto. O
 * comentário dela já dizia "quem publicar a segunda acrescenta o slug e o id
 * aqui" — e isso é verdade para UM campo, não para um arquivo que tem quatro
 * funções com `static` guardando o resultado da técnica única.
 *
 * A 1.1.0 troca as três constantes por um REGISTRO (`cdm_tecnicas_registro()`),
 * e toda função passa a receber o id da técnica. Cada página ganha o próprio
 * shortcode (`[cdm_tecnica_<id>]`), e isso não é gosto: a bancada descobre QUE
 * página está medindo casando o shortcode com a definição de páginas
 * (`cdm_teste_caminho_da_pagina`), então duas páginas com o mesmo shortcode
 * seriam medidas como se fossem a mesma — e a segunda nunca teria sido medida.
 * O `[cdm_tecnica]` da 1.0.0 continua registrado como atalho que resolve pela
 * página servida, para o caso de a atualização do conteúdo da página não pegar
 * no Sync: sem ele, a página do Picassiete imprimiria o colchete cru.
 *
 * -------------------------------------------------------------------------
 * A DECISÃO DE DESENHO QUE MANDA NESTE ARQUIVO: ELE NÃO DECIDE NADA
 * -------------------------------------------------------------------------
 * Nenhuma linha daqui escolhe cola. Quem escolhe é `cdm_f2_celula_cola()`, a
 * régua da F2, que já está no ar desde 11/09/2026 e já é medida por
 * `teste-f2.php` e pelo `validar-banco.py`. Esta página CHAMA aquela régua para
 * o caquinho da técnica e imprime o resultado.
 *
 * Isso não é economia de linha: é a única forma de a grade desta página não
 * envelhecer separada da ferramenta. Uma segunda cópia da decisão é a cicatriz
 * que esta ilha pagou duas vezes só em 14/09 — com a palavra-chave da busca que
 * existia no banco e que nenhum snippet lia, e com o `itens_sem_piso`, que
 * contava uma coisa e chamava de outra. A mesma razão vale para o texto: a
 * definição, a fonte e a consulta-alvo de cada técnica saem de
 * `dados/tecnicas.json`, que é o banco, e não de uma frase digitada aqui.
 *
 * O QUE ACONTECE QUANDO A F2 NÃO ESTÁ CARREGADA: a página diz que não conseguiu
 * medir, e não inventa. É a mesma trava do banco ausente que a Robometria
 * escreveu em 11/09/2026.
 *
 * -------------------------------------------------------------------------
 * A TÉCNICA COM DOIS CAQUINHOS, e a medição que decidiu o formato da página
 * -------------------------------------------------------------------------
 * O Picassiete declara UM material (`caco_louca`); o trencadís declara DOIS
 * (`caco_azulejo` e `caco_louca`). A pergunta "uma grade ou duas?" não foi
 * respondida por gosto: este arquivo calcula UMA GRADE POR CAQUINHO e AGRUPA as
 * que saírem idênticas, célula a célula. Hoje as duas do trencadís saem iguais
 * nas 45 combinações, e a página serve uma tabela só DIZENDO que comparou as 90
 * e por quê — o caquinho entra na régua da F2 num único lugar, a condição de
 * superfície porosa, e os dois cacos estão do mesmo lado dessa classificação.
 *
 * O dia em que uma técnica declarar dois caquinhos de porosidades diferentes
 * (por exemplo `caco_espelho` ao lado de `caco_louca`), o agrupamento devolve
 * dois grupos e a página serve DUAS tabelas, cada uma com o nome do caquinho em
 * cima. Esse caminho não espera aquele dia para ser medido: a mutação
 * `a tecnica passa a declarar dois caquinhos que decidem diferente` fabrica o
 * mundo e cobra as duas tabelas.
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
 * O QUE ESTAS PÁGINAS SE RECUSAM A RESPONDER, e dizem isso ao leitor
 * -------------------------------------------------------------------------
 * O REJUNTE, nas duas. A régua do rejunte decide por largura de junta em
 * milímetro e por ambiente, e não olha o material do caquinho; e as cinco
 * técnicas do banco têm `junta_tipica_mm` null, porque nenhuma fonte colhida
 * declara folga em milímetro para elas. Escolher um rejunte por semelhança
 * seria inventar o número que falta. A página manda para a F2, que pergunta a
 * junta.
 *
 * E no trencadís, mais uma: o CACO DE VIDRO COMUM. As fontes citam vidro entre
 * os cacos de Gaudí e o vocabulário `material_tessela` desta ilha não tem valor
 * para caco de vidro comum — tem `caco_espelho`, que é outra coisa. Responder
 * pelo mais parecido seria escolher o valor errado de propósito, então a página
 * diz que não responde e por quê. A recusa sai do próprio banco
 * (`recusas_declaradas` no registro abaixo), não de uma frase lembrada.
 */

if ( ! defined( 'CDM_TECNICAS_VERSAO' ) ) {
	define( 'CDM_TECNICAS_VERSAO', '1.1.0' );
}

/* ---------------------------------------------------------------------------
 * 0. O REGISTRO DAS PÁGINAS PUBLICADAS
 *
 * O que mora aqui é o que NÃO é dado: o endereço, o nome na tela e a prosa
 * editorial de cada página. Definição, fonte, data de leitura, consulta-alvo e
 * material do caquinho vêm do banco — e o `teste-tecnicas.php` cobra que toda
 * técnica registrada aqui tenha passado no portão de 3 itens da seção 9, medido
 * contra o banco, e que a bandeira `pagina_publicada` do banco concorde com
 * esta lista nos dois sentidos.
 *
 * O SLUG É A CONSULTA-ALVO DO BANCO, sem acento e com hífen. Nível 3 com a mãe
 * de nível 1 direto — DOIS segmentos de URL em vez de três, o mesmo estado de
 * transição em que a F2 e a F1 vivem desde o bloco 4 (ver a seção 2 do
 * ARVORE.md). O nível declarado é o da árvore final, não a contagem de barras.
 * NÃO é `/tecnicas/<nome>/`, que a 16.1 proíbe desde 11/09/2026; e não é
 * `/como-fazer/tecnicas/<consulta>/` porque a categoria de nível 2 só nasce com
 * três filhas (16.5), e mover URL de página posicionada é proibido pela 12.1.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_registro' ) ) {
function cdm_tecnicas_registro() {
	return array(
		'picassiette' => array(
			'slug'   => 'como-fazer/o-que-e-mosaico-picassiete',
			/* UM NOME POR PÁGINA, em toda superfície: cartão da Escola, degrau
			   da trilha, H1 e <title>. 40 caracteres; com o sufixo do site o
			   <title> fica em 59, abaixo do teto de 65. */
			'titulo' => 'O que é mosaico Picassiete, e como colar',
			'curto'  => 'Picassiete',
			'resumo' => 'Mosaico de louça quebrada — prato, xícara, azulejo antigo. O que é, de onde vem o nome e com o que colar o caquinho em cada superfície.',
			'linha_mestra' => 'Picassiete é mosaico de louça quebrada — prato, xícara, azulejo antigo. Aqui está o que é, de onde vem o nome, e com o que colar o caquinho em cada superfície e em cada lugar da casa.',
			'description'  => 'Mosaico Picassiete: o que é o mosaico de louça quebrada e com o que colar o caquinho em cada superfície — cerâmica, vidro, espelho, MDF, cimento ou metal — dentro de casa ou no sol e na chuva.',
			'o_que_muda'   => 'A diferença para o resto do mosaico está no material: em vez de pastilha comprada em placa, entra o que sobrou de uma louça. Isso muda duas coisas práticas — o caquinho tem espessuras diferentes na mesma peça, e a face esmaltada do prato é lisa, então a cola precisa segurar sobre esmalte e não sobre porosidade.',
			'faq_propria'  => array(
				array(
					'pergunta' => 'Dá para fazer Picassiete em peça que fica no sol e na chuva?',
					'resposta' => 'Dá, e a escolha muda: das {celulas} combinações de superfície e lugar desta página, {sem_nenhuma} não têm nenhum adesivo que o fabricante sustente — e a maioria delas é justamente o contato permanente com água. A página diz quais são, em vez de empurrar um produto.',
				),
			),
			'recusas_declaradas' => array(),
		),
		'trencadis' => array(
			'slug'   => 'como-fazer/o-que-e-trencadis',
			/* 42 caracteres; com o sufixo do site, 61. "Caco" e não "caquinho"
			   porque a versão com caquinho dá 66 e estoura o teto de 65 por um
			   caractere — e o teto é portão, não preferência. A palavra
			   caquinho abre o resumo, a linha mestra e o corpo, que é onde ela
			   cabe inteira. */
			'titulo' => 'O que é trencadís, e com o que colar o caco',
			'curto'  => 'trencadís',
			'resumo' => 'O caquinho quebrado a martelo — azulejo, louça — que ficou conhecido pela obra de Gaudí. O que é, de onde vem o nome e com o que colar cada caco.',
			'linha_mestra' => 'Trencadís é o caquinho quebrado a martelo e encaixado um a um — azulejo, louça, o que sobrou da obra. Aqui está o que é, de onde vem o nome, e com o que colar o caco em cada superfície e em cada lugar da casa.',
			'description'  => 'Trencadís: o que é o mosaico de caco quebrado a martelo, de onde vem o nome ligado a Gaudí, e com o que colar caco de azulejo ou de louça em cerâmica, vidro, espelho, MDF, cimento ou metal.',
			'o_que_muda'   => 'A diferença para o resto do mosaico está no material: em vez de pastilha comprada em placa, entra caco quebrado a martelo — azulejo que sobrou de obra, louça que trincou, peça irregular e de espessura desigual. Isso muda a colagem de um jeito que decide a cola: o caco assenta pelo lado quebrado ou pelo tardoz, e essa é a parte que absorve. Há adesivo no nosso banco que só cura se uma das duas superfícies absorver, e é por aí que o caquinho entra na conta.',
			'faq_propria'  => array(
				array(
					'pergunta' => 'Caco de azulejo e caco de louça pedem colas diferentes?',
					'resposta' => 'Nas {celulas} combinações desta página, não: a gente calculou as {celulas_por_caquinho_total} — {quantos_caquinhos} caquinhos vezes {celulas} situações — e comparou célula a célula, e as listas saíram iguais em todas. Quem muda a resposta é a superfície e o lugar. O caquinho só muda quando ele não absorve, como o caco de espelho, e nenhum dos dois é o caso.',
				),
				array(
					'pergunta' => 'E o caco de vidro de garrafa, serve para trencadís?',
					'resposta' => 'As fontes que lemos citam vidro entre os cacos, e esta página não responde por ele: a nossa lista de caquinhos não tem um valor para caco de vidro comum — tem caco de espelho, que é outra coisa, porque tem prata atrás. Responder pelo mais parecido seria escolher o valor errado de propósito. Fica registrado como o que falta colher, e não como resposta.',
				),
			),
			'recusas_declaradas' => array(
				array(
					'titulo' => 'O caco de vidro comum.',
					'texto'  => 'As fontes que sustentam a definição desta página citam vidro entre os cacos, e a nossa lista de caquinhos não tem um valor para caco de vidro de garrafa ou de pote — ela tem caco de espelho, que é vidro com prata atrás e cai do outro lado da conta que decide a cola. Escolher o mais parecido seria trocar um material por outro no meio de uma recomendação. Enquanto esse valor não existir, a pergunta fica sem resposta aqui e o {link_seletor} também não a responde.',
				),
			),
		),
	);
}
}

if ( ! function_exists( 'cdm_tecnicas_ids' ) ) {
function cdm_tecnicas_ids() {
	return array_keys( cdm_tecnicas_registro() );
}
}

if ( ! function_exists( 'cdm_tecnicas_ficha' ) ) {
/** A ficha editorial de uma técnica publicada, ou array() se ela não existe. */
function cdm_tecnicas_ficha( $id ) {
	$r = cdm_tecnicas_registro();

	return isset( $r[ $id ] ) ? $r[ $id ] : array();
}
}

if ( ! function_exists( 'cdm_tecnicas_id_do_slug' ) ) {
/** Qual técnica mora neste endereço. '' quando nenhuma. */
function cdm_tecnicas_id_do_slug( $slug ) {
	foreach ( cdm_tecnicas_registro() as $id => $ficha ) {
		if ( $ficha['slug'] === $slug ) {
			return $id;
		}
	}

	return '';
}
}

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — as páginas e os cartões na Escola
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	foreach ( cdm_tecnicas_registro() as $id => $ficha ) {
		$paginas[ $ficha['slug'] ] = array(
			'titulo'   => $ficha['titulo'],
			'conteudo' => '[cdm_tecnica_' . $id . ']',
			'pai'      => 'como-fazer',
		);
	}

	return $paginas;
} );

add_filter( 'cdm_tecnicas_publicadas', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( cdm_tecnicas_registro() as $id => $ficha ) {
		$lista[] = array(
			'id'     => $id,
			'slug'   => $ficha['slug'],
			'titulo' => $ficha['titulo'],
			'resumo' => $ficha['resumo'],
		);
	}

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

if ( ! function_exists( 'cdm_tecnicas_do_banco' ) ) {
/** O registro de banco de uma técnica, ou array() quando o banco não chegou. */
function cdm_tecnicas_do_banco( $id ) {
	$banco = cdm_tecnicas_banco();

	return isset( $banco['tecnicas'][ $id ] ) ? $banco['tecnicas'][ $id ] : array();
}
}

if ( ! function_exists( 'cdm_tecnicas_tesselas' ) ) {
/**
 * Os materiais do caquinho, lidos do banco. array() quando o banco não declara.
 *
 * SÃO TODOS, não o primeiro: a 1.0.0 devolvia só `reset()` porque a única
 * página publicada declarava um. Ficar no primeiro com duas declaradas seria
 * responder sobre um caquinho e deixar o outro fora da conta em silêncio — e o
 * leitor não teria como saber qual dos dois a tabela resolveu.
 */
function cdm_tecnicas_tesselas( $id ) {
	$t = cdm_tecnicas_do_banco( $id );
	$m = ( isset( $t['materiais_tipicos'] ) && is_array( $t['materiais_tipicos'] ) ) ? $t['materiais_tipicos'] : array();
	$saida = array();
	foreach ( $m as $v ) {
		$v = (string) $v;
		if ( '' !== $v ) {
			$saida[] = $v;
		}
	}

	return $saida;
}
}

if ( ! function_exists( 'cdm_tecnicas_pronta' ) ) {
/** Dá para medir? Precisa do banco de técnicas E da régua da F2. */
function cdm_tecnicas_pronta( $id ) {
	return cdm_tecnicas_tesselas( $id )
		&& function_exists( 'cdm_f2_celula_cola' )
		&& function_exists( 'cdm_f2_rotulos' );
}
}

/* ---------------------------------------------------------------------------
 * 3. A GRADE — 9 superfícies x 5 lugares por caquinho, pela régua da F2
 *
 * É a "tabela de exemplos pré-renderizada" da seção 5 do contrato: casos já
 * resolvidos, servidos no HTML, cobrindo a faixa real de uso. Um modelo de
 * linguagem lê os 45 casos sem preencher formulário nenhum — que é exatamente o
 * defeito que a Aquametria descobriu tarde e que a seção 5 existe para impedir.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_grade_de_uma_tessela' ) ) {
function cdm_tecnicas_grade_de_uma_tessela( $tessela ) {
	$grade = array();
	$rot   = cdm_f2_rotulos();
	foreach ( array_keys( $rot['base'] ) as $base ) {
		foreach ( array_keys( $rot['ambiente'] ) as $ambiente ) {
			$c        = cdm_f2_celula_cola( $base, $ambiente, $tessela );
			$elegivel = array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] );
			$grade[]  = array(
				'base'      => $base,
				'ambiente'  => $ambiente,
				'topo'      => $c['recomendados_topo'],
				'elegiveis' => $elegivel,
				'quantos'   => count( $elegivel ),
				'ressalva'  => $c['mencionados_com_ressalva'],
				'proibicao' => $c['eliminados_por_proibicao'],
				'silencio'  => $c['eliminados_por_silencio'],
				'condicao'  => $c['eliminados_por_condicao'],
			);
		}
	}

	return $grade;
}
}

if ( ! function_exists( 'cdm_tecnicas_assinatura_da_grade' ) ) {
/** A grade reduzida ao que a página AFIRMA, para duas grades poderem ser
    comparadas por igualdade em vez de por olho. */
function cdm_tecnicas_assinatura_da_grade( $grade ) {
	$partes = array();
	foreach ( $grade as $c ) {
		$partes[] = $c['base'] . '|' . $c['ambiente'] . '|' . implode( ',', $c['elegiveis'] )
			. '|' . implode( ',', $c['topo'] );
	}

	return implode( ';', $partes );
}
}

if ( ! function_exists( 'cdm_tecnicas_grupos' ) ) {
/**
 * Os caquinhos da técnica AGRUPADOS pelas grades que saem iguais.
 *
 * Um grupo = uma tabela na tela. Com um caquinho é sempre um grupo; com dois
 * que decidem igual, um grupo e a página diz que comparou; com dois que decidem
 * diferente, dois grupos e duas tabelas. Quem decide é a comparação, nunca uma
 * frase escrita aqui.
 */
function cdm_tecnicas_grupos( $id ) {
	static $cache = array();
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$grupos = array();
	if ( ! cdm_tecnicas_pronta( $id ) ) {
		$cache[ $id ] = $grupos;

		return $grupos;
	}
	$por_assinatura = array();
	foreach ( cdm_tecnicas_tesselas( $id ) as $tessela ) {
		$grade = cdm_tecnicas_grade_de_uma_tessela( $tessela );
		$chave = cdm_tecnicas_assinatura_da_grade( $grade );
		if ( ! isset( $por_assinatura[ $chave ] ) ) {
			$por_assinatura[ $chave ] = array( 'tesselas' => array(), 'grade' => $grade );
		}
		$por_assinatura[ $chave ]['tesselas'][] = $tessela;
	}
	$grupos       = array_values( $por_assinatura );
	$cache[ $id ] = $grupos;

	return $grupos;
}
}

if ( ! function_exists( 'cdm_tecnicas_celula' ) ) {
/** Uma célula do grupo `$g` (índice), ou null. */
function cdm_tecnicas_celula( $id, $g, $base, $ambiente ) {
	$grupos = cdm_tecnicas_grupos( $id );
	if ( ! isset( $grupos[ $g ] ) ) {
		return null;
	}
	foreach ( $grupos[ $g ]['grade'] as $c ) {
		if ( $c['base'] === $base && $c['ambiente'] === $ambiente ) {
			return $c;
		}
	}

	return null;
}
}

if ( ! function_exists( 'cdm_tecnicas_contas' ) ) {
/**
 * Os números que a página afirma — TODOS contados das grades, nenhum digitado.
 *
 * `celulas` conta as combinações SERVIDAS, que é uma por linha de tabela na
 * tela: 45 quando os caquinhos decidem igual, 45 por grupo quando não decidem.
 * Contar 90 com uma tabela de 45 seria afirmar sobre linhas que a página não
 * tem, e é a mesma família do "escopo maior do que o medido" que a home desta
 * ilha já pagou.
 *
 * `fora` é a prestação de contas da seção 7: para cada cola do banco que não
 * entra em célula nenhuma, em quantas das servidas ela aparece em cada balde. A
 * causa que a página escreve é a de TODO balde com contagem, e vem com o número
 * do lado. É a diferença entre "a recusa nomeia a causa que a página mediu" e
 * uma hipótese com cara de explicação, que é o que a seção 7 proíbe desde
 * 12/09.
 */
function cdm_tecnicas_contas( $id ) {
	static $cache = array();
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$grupos = cdm_tecnicas_grupos( $id );

	$dentro  = array();
	$celulas = 0;
	$com_min = 0;
	$zeradas = 0;
	$baldes  = array();

	foreach ( $grupos as $grupo ) {
		foreach ( $grupo['grade'] as $c ) {
			$celulas++;
			foreach ( $c['elegiveis'] as $id_cola ) {
				$dentro[ $id_cola ] = true;
			}
			if ( $c['quantos'] >= 3 ) {
				$com_min++;
			}
			if ( 0 === $c['quantos'] ) {
				$zeradas++;
			}
			foreach ( array( 'ressalva', 'proibicao', 'silencio', 'condicao' ) as $balde ) {
				foreach ( $c[ $balde ] as $id_cola ) {
					if ( ! isset( $baldes[ $id_cola ] ) ) {
						$baldes[ $id_cola ] = array( 'ressalva' => 0, 'proibicao' => 0, 'silencio' => 0, 'condicao' => 0 );
					}
					$baldes[ $id_cola ][ $balde ]++;
				}
			}
		}
	}

	/* O BANCO INTEIRO, não só quem apareceu: a soma dos nomeados tem de fechar
	   com o tamanho do banco, e isso se conta varrendo o banco, nunca a lista de
	   quem passou (seção 7, 12/09/2026). */
	$todas = array();
	if ( function_exists( 'cdm_f2_banco' ) ) {
		foreach ( cdm_f2_banco()['materiais'] as $id_cola => $m ) {
			if ( 'cola' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
				$todas[] = $id_cola;
			}
		}
	}

	$fora = array();
	foreach ( $todas as $id_cola ) {
		if ( isset( $dentro[ $id_cola ] ) ) {
			continue;
		}
		$b = isset( $baldes[ $id_cola ] ) ? $baldes[ $id_cola ] : array( 'ressalva' => 0, 'proibicao' => 0, 'silencio' => 0, 'condicao' => 0 );

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
		$fora[] = array( 'id' => $id_cola, 'causas' => $causas, 'baldes' => $b );
	}

	$tesselas = cdm_tecnicas_tesselas( $id );
	$por_grupo = $grupos ? count( $grupos[0]['grade'] ) : 0;

	$cache[ $id ] = array(
		'celulas'          => $celulas,
		'celulas_por_grupo' => $por_grupo,
		'com_o_minimo'     => $com_min,
		'sem_nenhuma'      => $zeradas,
		'dentro'           => array_keys( $dentro ),
		'fora'             => $fora,
		'colas_no_banco'   => count( $todas ),
		'grupos'           => count( $grupos ),
		'tesselas'         => $tesselas,
		'quantos_caquinhos' => count( $tesselas ),
		/* As combinações que a página COMPAROU para chegar a uma tabela só. Com
		   um caquinho é igual ao número servido; com dois iguais, o dobro. */
		'celulas_comparadas' => $por_grupo * count( $tesselas ),
	);

	return $cache[ $id ];
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
		'condicao'  => 'o fabricante exige que uma das superfícies seja porosa, e essa combinação não tem nenhuma',
	);
	$partes = array();
	foreach ( (array) $causas as $c ) {
		$texto    = isset( $mapa[ $c['causa'] ] ) ? $mapa[ $c['causa'] ] : 'não há declaração que o sustente';
		$partes[] = $texto . ' em ' . (int) $c['quantas'] . ' das ' . (int) $celulas;
	}

	return implode( '; ', $partes );
}
}

if ( ! function_exists( 'cdm_tecnicas_preencher' ) ) {
/** Os números da página dentro de uma frase editorial, sempre contados. */
function cdm_tecnicas_preencher( $texto, $contas ) {
	return strtr( (string) $texto, array(
		'{celulas}'                     => (string) (int) $contas['celulas'],
		'{sem_nenhuma}'                 => (string) (int) $contas['sem_nenhuma'],
		'{com_o_minimo}'                => (string) (int) $contas['com_o_minimo'],
		'{quantos_caquinhos}'           => (string) (int) $contas['quantos_caquinhos'],
		'{celulas_por_caquinho_total}'  => (string) (int) $contas['celulas_comparadas'],
		'{link_seletor}'                => function_exists( 'cdm_casca_link_html' )
			? cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
			: 'seletor de cola e rejunte',
	) );
}
}

if ( ! function_exists( 'cdm_tecnicas_faq' ) ) {
/**
 * Uma fonte só para a tela e para o FAQPage — o mesmo desenho da F2. Schema que
 * promete resposta que a página não dá é o que faz FAQPage virar spam.
 */
function cdm_tecnicas_faq( $id ) {
	$t       = cdm_tecnicas_do_banco( $id );
	$ficha   = cdm_tecnicas_ficha( $id );
	$contas  = cdm_tecnicas_contas( $id );
	$curto   = isset( $ficha['curto'] ) ? $ficha['curto'] : $id;
	$interno = cdm_tecnicas_celula( $id, 0, 'ceramica_esmaltada_porcelana', 'interno_seco' );
	$nomes   = array();
	if ( $interno ) {
		foreach ( $interno['elegiveis'] as $id_cola ) {
			$nomes[] = cdm_f2_nome( $id_cola );
		}
	}
	$rot      = function_exists( 'cdm_f2_rotulos' ) ? cdm_f2_rotulos() : array( 'tessela' => array() );
	$primeira = $contas['tesselas'] ? $contas['tesselas'][0] : '';
	$nome_caquinho = isset( $rot['tessela'][ $primeira ] ) ? mb_strtolower( $rot['tessela'][ $primeira ] ) : 'caquinho';

	$faq = array(
		array(
			'pergunta' => 'O que é ' . ( 'trencadis' === $id ? 'trencadís' : 'mosaico ' . $curto ) . '?',
			'resposta' => isset( $t['definicao'] ) ? (string) $t['definicao']
				: 'A definição desta técnica vem do banco, e ele não chegou ao site.',
		),
		array(
			'pergunta' => 'Qual cola usar para colar ' . $nome_caquinho . ' num vaso de cerâmica dentro de casa?',
			'resposta' => $nomes
				? 'Sobre cerâmica, dentro de casa e em lugar seco, ' . count( $nomes ) . ' adesivos do nosso banco servem: '
					. cdm_f2_lista_humana( $nomes ) . '. Todos entram pela lista que o próprio fabricante publica.'
				: 'A medição não chegou ao site; a resposta não é chutada.',
		),
	);

	foreach ( ( isset( $ficha['faq_propria'] ) ? $ficha['faq_propria'] : array() ) as $p ) {
		$faq[] = array(
			'pergunta' => $p['pergunta'],
			'resposta' => cdm_tecnicas_preencher( $p['resposta'], $contas ),
		);
	}

	$faq[] = array(
		'pergunta' => 'E o rejunte?',
		'resposta' => 'Esta página não responde. O rejunte se decide pela largura da junta em milímetro, e nenhuma fonte que lemos sobre esta técnica declara essa folga — então perguntamos a junta na ferramenta, em vez de escolher por semelhança.',
	);

	return $faq;
}
}

/* ---------------------------------------------------------------------------
 * 5. O corpo da página
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_html' ) ) {
function cdm_tecnicas_html( $id ) {
	$t     = cdm_tecnicas_do_banco( $id );
	$ficha = cdm_tecnicas_ficha( $id );
	$rot   = function_exists( 'cdm_f2_rotulos' ) ? cdm_f2_rotulos() : array();

	if ( ! cdm_tecnicas_pronta( $id ) || ! $ficha ) {
		return '<div class="cdm-bloco"><div class="cdm-vazio">'
			. '<h3>A medição desta página ainda não chegou ao site</h3>'
			. '<p>Ela não vai inventar uma recomendação enquanto isso. Volte daqui a pouco, ou use o '
			. ( function_exists( 'cdm_casca_link_html' ) ? cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' ) : 'guia de materiais' )
			. ', que pergunta a superfície e o lugar.</p></div></div>';
	}

	$contas = cdm_tecnicas_contas( $id );
	$grupos = cdm_tecnicas_grupos( $id );
	$html   = '<div class="cdm-bloco cdm-tec">';

	/* A LINHA MESTRA — o que a pessoa recebe, em uma linha. Sem fabricante, sem
	   data, sem a palavra `tessela`: o VOZ.md manda isso para a camada de prova. */
	$html .= '<p class="cdm-linha-mestra">' . esc_html( $ficha['linha_mestra'] ) . '</p>';

	/* A RESPOSTA ANTES DA EXPLICAÇÃO (seção 5, item 2), em frase que sobrevive a
	   ser citada fora de contexto. O número é contado da grade. */
	$html .= '<div class="cdm-tec-resposta">';
	/* O NOME DO CAQUINHO SAI DO VOCABULÁRIO, nunca de uma frase digitada: é o
	   mesmo rótulo que a F2 imprime no formulário dela, então as duas páginas
	   chamam a mesma coisa pelo mesmo nome. */
	$nomes_caquinho = array();
	foreach ( $contas['tesselas'] as $tessela ) {
		$nomes_caquinho[] = isset( $rot['tessela'][ $tessela ] ) ? mb_strtolower( $rot['tessela'][ $tessela ] ) : $tessela;
	}
	$html .= '<p class="cdm-tec-frase">Para colar ' . esc_html( cdm_f2_lista_humana( $nomes_caquinho ) ) . ', <strong>' . count( $contas['dentro'] ) . ' dos '
		. (int) $contas['colas_no_banco'] . ' adesivos do nosso banco</strong> servem em pelo menos uma situação — e qual deles serve muda com a superfície e com o lugar. '
		. 'Das <strong>' . (int) $contas['celulas'] . '</strong> combinações desta página, '
		. (int) $contas['com_o_minimo'] . ' têm três ou mais opções e <strong>' . (int) $contas['sem_nenhuma']
		. ' não têm nenhuma</strong>, e a gente diz quais são em vez de empurrar um produto.</p>';

	/* A PROCEDÊNCIA DESCE UM PARÁGRAFO, dentro da caixa da resposta e marcada
	   como prova — o mesmo desenho que a Aquametria adotou em 11/09/2026 para a
	   seção 5 continuar inteira sem a voz do VOZ.md ser quebrada no topo. */
	if ( ! empty( $t['definicao_fonte_id'] ) && ! empty( $t['fontes'][ $t['definicao_fonte_id'] ] ) ) {
		$f     = $t['fontes'][ $t['definicao_fonte_id'] ];
		$html .= '<p class="cdm-prova cdm-tec-prova">Cada adesivo entra ou sai pela lista que o próprio fabricante publica, recalculada na hora; a definição desta técnica vem de '
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
	$html .= '<p>' . esc_html( $ficha['o_que_muda'] ) . '</p>';
	$html .= '<p>O ' . cdm_casca_link_html( 'como-fazer', 'Como fazer' ) . ' é a seção onde este tipo de página vive; o '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
		. ' responde a mesma pergunta para qualquer caquinho, perguntando a superfície e o lugar.</p></div>';

	/* A GRADE PRÉ-RENDERIZADA, uma tabela por grupo de caquinhos. */
	$html .= '<div class="cdm-secao"><h2>Com o que colar, superfície por superfície</h2>';
	$html .= '<p>A linha é a superfície sobre a qual você vai colar — o vaso, o quadro, o tampo. A coluna é onde a peça vai viver. Em cada cruzamento está o que os fabricantes sustentam, e quando não há nada, está escrito que não há.</p>';

	/* A FRASE QUE DIZ QUAL CAQUINHO A TABELA RESOLVE, e ela é medição e não
	   promessa: com mais de um caquinho declarado, a página conta quantas
	   combinações comparou e diz se elas saíram iguais. */
	if ( $contas['quantos_caquinhos'] > 1 ) {
		$nomes_caq = array();
		foreach ( $contas['tesselas'] as $tessela ) {
			$nomes_caq[] = isset( $rot['tessela'][ $tessela ] ) ? mb_strtolower( $rot['tessela'][ $tessela ] ) : $tessela;
		}
		if ( 1 === $contas['grupos'] ) {
			$html .= '<p class="cdm-tec-caquinhos">Esta técnica usa mais de um caquinho — ' . esc_html( cdm_f2_lista_humana( $nomes_caq ) )
				. ' —, e a tabela é <strong>uma só</strong> porque as listas saíram iguais. A gente calculou as '
				. (int) $contas['celulas_comparadas'] . ' combinações (' . (int) $contas['quantos_caquinhos'] . ' caquinhos × '
				. (int) $contas['celulas_por_grupo'] . ' situações) e comparou uma a uma: nenhuma diferença. '
				. 'O caquinho só muda a resposta quando ele não absorve — há adesivo aqui que precisa de uma superfície porosa para curar —, e esses caem do mesmo lado dessa conta.</p>';
		} else {
			$html .= '<p class="cdm-tec-caquinhos">Esta técnica usa mais de um caquinho — ' . esc_html( cdm_f2_lista_humana( $nomes_caq ) )
				. ' —, e eles <strong>não</strong> resolvem igual: são ' . (int) $contas['grupos']
				. ' tabelas, uma para cada resposta diferente, e o nome do caquinho está em cima de cada uma.</p>';
		}
	}

	foreach ( $grupos as $indice => $grupo ) {
		if ( count( $grupos ) > 1 ) {
			$nomes_g = array();
			foreach ( $grupo['tesselas'] as $tessela ) {
				$nomes_g[] = isset( $rot['tessela'][ $tessela ] ) ? $rot['tessela'][ $tessela ] : $tessela;
			}
			$html .= '<h3 class="cdm-tec-titulo-tabela">' . esc_html( implode( ' e ', $nomes_g ) ) . '</h3>';
		}
		$html .= '<div class="cdm-tec-rolagem"><table class="cdm-tec-tabela"><thead><tr><th scope="col">Sobre o que você vai colar</th>';
		foreach ( $rot['ambiente'] as $amb => $rotulo ) {
			$html .= '<th scope="col">' . esc_html( $rot['ambiente_curto'][ $amb ] ) . '</th>';
		}
		$html .= '</tr></thead><tbody>';
		foreach ( $rot['base'] as $base => $rotulo ) {
			$html .= '<tr><th scope="row">' . esc_html( $rotulo ) . '</th>';
			foreach ( array_keys( $rot['ambiente'] ) as $amb ) {
				$c = cdm_tecnicas_celula( $id, $indice, $base, $amb );
				if ( ! $c || 0 === $c['quantos'] ) {
					$html .= '<td class="cdm-tec-vazia">nenhum que o fabricante sustente</td>';
					continue;
				}
				$nomes = array();
				foreach ( $c['topo'] as $id_cola ) {
					$nomes[] = esc_html( cdm_f2_nome( $id_cola ) );
				}
				$extra  = $c['quantos'] - count( $c['topo'] );
				$html  .= '<td>' . cdm_f2_lista_humana( $nomes )
					. ( $extra > 0 ? '<span class="cdm-tec-mais"> e mais ' . (int) $extra . '</span>' : '' )
					. '</td>';
			}
			$html .= '</tr>';
		}
		$html .= '</tbody></table></div>';
	}

	$html .= '<p class="cdm-tec-legenda">Cada célula traz o que ficou em primeiro lugar naquela combinação; "e mais" é quanta opção sobra abaixo dele. Quem quiser a lista inteira de uma combinação, com o que foi descartado e por quê, abre o '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor' ) . '.</p></div>';

	/* A VITRINE — bloco de compra ANTES da prova de procedência (seção 7). */
	$html .= '<div class="cdm-secao"><h2>Os adesivos que entram</h2>';
	$nomes_dentro = array();
	foreach ( $contas['dentro'] as $id_cola ) {
		$nomes_dentro[] = cdm_f2_nome( $id_cola );
	}
	$html .= '<p>São estes ' . count( $contas['dentro'] ) . ', e cada um entra por uma combinação diferente: '
		. cdm_f2_lista_humana( array_map( 'esc_html', $nomes_dentro ) ) . '.</p>';
	$html .= '<ul class="cdm-f2-cartoes">';
	foreach ( $contas['dentro'] as $id_cola ) {
		$onde = array();
		foreach ( $grupos as $grupo ) {
			foreach ( $grupo['grade'] as $c ) {
				if ( in_array( $id_cola, $c['elegiveis'], true ) ) {
					$onde[ $c['base'] ] = true;
				}
			}
		}
		$quantas = count( $onde );
		$motivo  = 'serve em ' . $quantas . ' das ' . count( $rot['base'] ) . ' superfícies desta página, pela lista do fabricante';
		$html   .= cdm_f2_cartao_html( $id_cola, esc_html( $motivo ) );
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

	/* AS RECUSAS, com a causa medida (seção 7). A do rejunte vale para toda
	   técnica; as outras vêm declaradas na ficha da técnica. */
	$html .= '<div class="cdm-secao"><h2>O que esta página não responde</h2>';
	$html .= '<p><strong>O rejunte.</strong> Ele não se escolhe pelo material do caquinho: escolhe-se pela largura da junta, em milímetro, e pelo lugar. Nenhuma das fontes que lemos sobre esta técnica declara essa folga — elas falam do espaço entre os cacos sem dar número —, e escolher por semelhança seria inventar justamente o número que falta. Quem já sabe a junta da peça pergunta no '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor' ) . ', que responde rejunte junto com a cola.</p>';
	foreach ( ( isset( $ficha['recusas_declaradas'] ) ? $ficha['recusas_declaradas'] : array() ) as $r ) {
		$html .= '<p><strong>' . esc_html( $r['titulo'] ) . '</strong> '
			. cdm_tecnicas_preencher( esc_html( $r['texto'] ), $contas ) . '</p>';
	}
	$html .= '</div>';

	/* FAQ na tela — mesma fonte do FAQPage. */
	$html .= '<div class="cdm-secao"><h2>Perguntas que chegam</h2><dl class="cdm-tec-faq">';
	foreach ( cdm_tecnicas_faq( $id ) as $p ) {
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
}
}

/* UM SHORTCODE POR PÁGINA. Ver o cabeçalho: a bancada casa o shortcode com a
   definição de páginas para saber QUEM está medindo, e dois endereços com o
   mesmo shortcode seriam medidos como um só. */
foreach ( cdm_tecnicas_ids() as $cdm_tecnica_id ) {
	add_shortcode( 'cdm_tecnica_' . $cdm_tecnica_id, function () use ( $cdm_tecnica_id ) {
		return cdm_tecnicas_html( $cdm_tecnica_id );
	} );
}
unset( $cdm_tecnica_id );

/* O ATALHO DA 1.0.0, e ele é rede de segurança e não legado decorativo: o
   conteúdo da página do Picassiete no WordPress diz `[cdm_tecnica]` até o Sync
   reescrevê-lo. Se essa reescrita falhar, sem isto a página imprime o colchete
   cru para o leitor. Ele resolve pelo endereço servido — nunca por um id
   escolhido aqui, que serviria a técnica errada. */
add_shortcode( 'cdm_tecnica', function () {
	$id = function_exists( 'cdm_casca_slug_atual' ) ? cdm_tecnicas_id_do_slug( cdm_casca_slug_atual() ) : '';

	return cdm_tecnicas_html( $id );
} );

/* ---------------------------------------------------------------------------
 * 6. Cabeça da página — description e JSON-LD
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_tecnicas_id_da_pagina_atual' ) ) {
function cdm_tecnicas_id_da_pagina_atual() {
	if ( ! function_exists( 'cdm_casca_slug_atual' ) ) {
		return '';
	}

	return cdm_tecnicas_id_do_slug( cdm_casca_slug_atual() );
}
}

add_action( 'wp_head', function () {
	$id = cdm_tecnicas_id_da_pagina_atual();
	if ( '' === $id ) {
		return;
	}
	$ficha = cdm_tecnicas_ficha( $id );

	echo '<meta name="description" content="' . esc_attr( $ficha['description'] ) . '">' . "\n";

	$limpa     = home_url( '/' . $ficha['slug'] . '/' );
	$t         = cdm_tecnicas_do_banco( $id );
	$perguntas = array();
	foreach ( cdm_tecnicas_faq( $id ) as $p ) {
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
				'@type'       => 'Article',
				'@id'         => $limpa . '#artigo',
				'headline'    => $ficha['titulo'],
				'url'         => $limpa,
				'inLanguage'  => 'pt-BR',
				'description' => isset( $t['definicao'] ) ? (string) $t['definicao'] : '',
				'about'       => array(
					'@type' => 'Thing',
					'name'  => isset( $t['nome'] ) ? (string) $t['nome'] : $ficha['titulo'],
				),
				'publisher'   => array( '@id' => home_url( '/#organizacao' ) ),
				'isPartOf'    => array( '@id' => home_url( '/#site' ) ),
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
 * 7. Folha — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML. Foi o defeito que derrubou
 * cinco calculadoras da Aquametria em 08/09/2026.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( '' === cdm_tecnicas_id_da_pagina_atual() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-tecnicas-css">
.cdm-tec-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-tec-frase{font-size:1.15rem;line-height:1.5;margin:0;}
.cdm-tec-prova{margin:1rem 0 0;}
.cdm-tec-caquinhos{color:var(--cdm-legenda);font-size:.95rem;}
.cdm-tec-titulo-tabela{font-family:var(--cdm-display);font-size:1.05rem;margin:1.4rem 0 .2rem;}
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

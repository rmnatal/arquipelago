/**
 * Robometria — MALHA DE PEÇAS (bloco 5b, primeira leva)
 *
 * Cinco páginas, uma árvore de três níveis:
 *
 *   /pecas/                        seção (nível 1)
 *   /pecas/filtros/                categoria (nível 2)
 *   /pecas/filtros/xiaomi/         filha (nível 3)
 *   /pecas/filtros/wap/            filha
 *   /pecas/filtros/electrolux/     filha
 *
 * VERSÃO 1.0.0 — 21/09/2026.
 *
 * POR QUE ESTA LEVA, E POR QUE SÓ ELA
 * -----------------------------------
 * A ordem de levas do `ARVORE.md` (seção 5) manda abrir a mãe e as TRÊS
 * primeiras filhas de maior intenção de compra, nunca uma filha de cada
 * categoria espalhada — cluster ralo não passa autoridade (16.6). São 5 URLs,
 * dentro do teto de 10 por leva da 21.4. As outras quatro categorias de peça
 * saem como cartão sem link, e **sem contagem de banco**, que é o que a 16.5
 * manda: contagem no cartão de categoria que não existe é promessa datada.
 *
 * A HIERARQUIA É DE VERDADE, E ELA CUSTOU UMA FUNÇÃO NOVA
 * -------------------------------------------------------
 * `robometria_casca_garantir_paginas()` cria página por slug plano, e a 16.2
 * exige que nível 1 e nível 2 sejam páginas-mãe de verdade (post_parent), para
 * a URL mostrar os três níveis. Quem cria as páginas desta malha é
 * `robometria_malha_garantir_paginas()`, aqui embaixo, na ordem da árvore: a
 * mãe primeiro, porque o WordPress precisa do ID dela para o post_parent da
 * filha. A identidade canônica de cada uma é o meta `_robometria_id` com a
 * CHAVE (pecas-filtros-xiaomi), nunca o post_name — que é só o último degrau
 * (xiaomi) e colide com a categoria de modelos da mesma marca no dia em que
 * `/modelos/xiaomi/` nascer.
 *
 * O QUE ESTE ARQUIVO NÃO DECIDE
 * -----------------------------
 * Nenhum número e nenhuma frase de resposta nascem aqui: os dois vêm de
 * `dados/malha-pecas.json`, derivado do banco por
 * `ferramentas/gerar-malha-pecas.py`, que é a implementação de REFERÊNCIA desta
 * camada. É a decisão 2 do bloco 4 do `PROMPT.md`, a mesma que a R1 e os dois
 * artigos seguem, e `ferramentas/teste-malha.php` compara frase a frase, sem
 * acento, o que este PHP escreve com o que a referência escreveu.
 *
 * SEM O BANCO NO AR A PÁGINA DIZ ISSO — não inventa número, não esconde bloco.
 */

if ( ! defined( 'ROBOMETRIA_MALHA_VERSAO' ) ) {
	define( 'ROBOMETRIA_MALHA_VERSAO', '1.0.0' );
}

/* ---------------------------------------------------------------------------
 * 1. O REGISTRO DAS PÁGINAS PUBLICADAS
 *
 * Esta lista é a única coisa que decide o que está NO AR. O gerador conta a
 * grade inteira (todo tipo de peça × toda marca) e não sabe o que foi
 * publicado, de propósito: publicar é URL nova, e URL nova obedece ao teto da
 * 21.4 e à rampa da seção 9. Abrir a próxima categoria é acrescentar linhas
 * aqui — e recontar antes, como o `ARVORE.md` manda.
 *
 * CADA PÁGINA CARREGA OS DOIS COMPROMISSOS DA 14.9 ESCRITOS NO PRÓPRIO ARQUIVO:
 * a consulta que ela mira e por que ela consegue chegar às dez primeiras. A
 * classificação de SERP que sustenta cada `por_que_top10` está medida em
 * `dados/serp-malha-pecas-2026-09-21.md`, com data e com o que ocupa o top 10.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_paginas' ) ) {
function robometria_malha_paginas() {
	return array(
		'pecas' => array(
			'papel'    => 'secao',
			'caminho'  => 'pecas',
			'post_name' => 'pecas',
			'mae'      => '',
			'secao'    => 'pecas',
			'titulo'   => 'Peças de reposição de robô aspirador',
			'consulta' => 'peças de reposição para robô aspirador: quais servem',
			'por_que_top10' => 'a primeira página é loja pequena e post genérico de blog '
				. '("7 peças que você pode trocar"); ninguém publica quantas peças de cada '
				. 'tipo o fabricante declarou, por marca e por modelo, com o código e a data.',
		),
		'pecas-filtros' => array(
			'papel'    => 'categoria',
			'caminho'  => 'pecas/filtros',
			'post_name' => 'filtros',
			'mae'      => 'pecas',
			'secao'    => 'pecas',
			'categoria' => 'filtros',
			'titulo'   => 'Filtro de robô aspirador: qual serve no seu',
			'consulta' => 'filtro de robô aspirador: compatibilidade por marca e modelo',
			'por_que_top10' => 'a consulta comercial curta está tomada por TechTudo e '
				. 'Canaltech e esta página NÃO a disputa; a paramétrica de compatibilidade '
				. 'devolve resposta genérica sem número ("como escolher o modelo certo") e '
				. 'nenhuma tabela de marca × modelo com fonte do fabricante.',
		),
		'pecas-filtros-xiaomi' => array(
			'papel'    => 'filha',
			'caminho'  => 'pecas/filtros/xiaomi',
			'post_name' => 'xiaomi',
			'mae'      => 'pecas-filtros',
			'secao'    => 'pecas',
			'categoria' => 'filtros',
			'marca'    => 'xiaomi',
			'titulo'   => 'Filtro de robô aspirador Xiaomi',
			'consulta' => 'filtro de robô aspirador Xiaomi: qual serve no meu modelo',
			'por_que_top10' => 'medido em 21/09/2026: o top 10 é anúncio do APARELHO '
				. '(Camicado, Amazon, Carrefour, Kabum) e PDF de manual; nenhuma página '
				. 'responde qual código de filtro serve em qual modelo.',
		),
		'pecas-filtros-wap' => array(
			'papel'    => 'filha',
			'caminho'  => 'pecas/filtros/wap',
			'post_name' => 'wap',
			'mae'      => 'pecas-filtros',
			'secao'    => 'pecas',
			'categoria' => 'filtros',
			'marca'    => 'wap',
			'titulo'   => 'Filtro de robô aspirador WAP',
			'consulta' => 'filtro de robô aspirador WAP W300: qual serve',
			'por_que_top10' => 'medido em 21/09/2026: a loja oficial e os marketplaces '
				. 'ocupam o top 10 com a ficha do robô; a única página que cita o código '
				. 'FW006270 é de loja, sem lista de modelos e sem data.',
		),
		'pecas-filtros-electrolux' => array(
			'papel'    => 'filha',
			'caminho'  => 'pecas/filtros/electrolux',
			'post_name' => 'electrolux',
			'mae'      => 'pecas-filtros',
			'secao'    => 'pecas',
			'categoria' => 'filtros',
			'marca'    => 'electrolux',
			'titulo'   => 'Filtro de robô aspirador Electrolux',
			'consulta' => 'filtro do robô aspirador Electrolux ERB60: qual serve',
			'por_que_top10' => 'medido em 21/09/2026: as dez primeiras são a ficha de '
				. 'venda do ERB60 (loja oficial, Kabum, Extra, Casas Bahia, Fast Shop). '
				. 'ZERO resultados sobre a peça — e é a marca em que o filtro, em cinco '
				. 'dos nove modelos, só vem dentro do kit.',
		),
	);
}
}

/* A chave da página a partir da tag do shortcode: robometria_pecas_filtros_wap
   -> pecas-filtros-wap. Derivada, para o shortcode não ser um segundo mapa. */
if ( ! function_exists( 'robometria_malha_chave_da_tag' ) ) {
function robometria_malha_chave_da_tag( $tag ) {
	return str_replace( '_', '-', substr( (string) $tag, strlen( 'robometria_' ) ) );
}
}

if ( ! function_exists( 'robometria_malha_tag_da_chave' ) ) {
function robometria_malha_tag_da_chave( $chave ) {
	return 'robometria_' . str_replace( '-', '_', (string) $chave );
}
}

/* ---------------------------------------------------------------------------
 * 2. OS FATOS — lidos da option que o Sync gravou, nunca calculados aqui.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_dados' ) ) {
function robometria_malha_dados() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}

	$dados = array();
	if ( function_exists( 'robometria_casca_fonte_publicada' )
		&& robometria_casca_fonte_publicada( 'malha-pecas' ) ) {
		$d = get_option( 'robometria_dados_malha-pecas' );
		if ( is_array( $d ) && ! empty( $d['categorias'] ) ) {
			$dados = $d;
		}
	}

	$cache = apply_filters( 'robometria_malha_dados', $dados );
	return $cache;
}
}

/* A categoria pelo slug de registro (pecas-filtros), ou array() quando o banco
   não chegou. */
if ( ! function_exists( 'robometria_malha_categoria' ) ) {
function robometria_malha_categoria( $chave ) {
	$d = robometria_malha_dados();
	foreach ( (array) ( isset( $d['categorias'] ) ? $d['categorias'] : array() ) as $c ) {
		if ( isset( $c['slug'] ) && $c['slug'] === $chave ) {
			return $c;
		}
	}
	return array();
}
}

if ( ! function_exists( 'robometria_malha_filha' ) ) {
function robometria_malha_filha( $chave ) {
	$d = robometria_malha_dados();
	foreach ( (array) ( isset( $d['categorias'] ) ? $d['categorias'] : array() ) as $c ) {
		foreach ( (array) ( isset( $c['filhas'] ) ? $c['filhas'] : array() ) as $f ) {
			if ( isset( $f['slug'] ) && $f['slug'] === $chave ) {
				return $f;
			}
		}
	}
	return array();
}
}

/* ---------------------------------------------------------------------------
 * 3. A ÁRVORE — a casca pergunta a este registro quem é mãe de quem.
 *
 * O filtro `robometria_malha` é o que faz a trilha, o BreadcrumbList, as irmãs
 * e o nome de cada página saírem da MESMA lista que cria as páginas. Sem ele a
 * casca teria um segundo mapa da árvore, digitado ao lado deste — que é o
 * defeito que esta ilha já pagou três vezes (o nome da página em 11/09, a lista
 * de categorias em 17/09, as contagens da R1 em 14/09).
 * ------------------------------------------------------------------------- */

add_filter( 'robometria_malha', 'robometria_malha_paginas' );

/* As cabeças: `<title>`, description e og:*. Uma por página, com a promessa
   numérica de fora — nenhuma destas cinco tem impressão medida, e trocar a
   marca por um número antes de haver o que comparar torna a leitura seguinte
   ilegível (a mesma escolha que a casca fez em 17/09/2026). */
add_filter( 'robometria_cabecas', 'robometria_malha_cabecas' );

if ( ! function_exists( 'robometria_malha_cabecas' ) ) {
function robometria_malha_cabecas( $mapa ) {
	$mapa['pecas'] = array(
		'tipo'      => 'website',
		'descricao' => 'Filtro, escova, mop e bateria de robô aspirador: o que o '
			. 'fabricante declarou para cada modelo, com o código da peça, o endereço '
			. 'da declaração e a data.',
	);
	$mapa['pecas-filtros'] = array(
		'tipo'      => 'website',
		'descricao' => 'Qual filtro serve em qual robô aspirador, marca por marca, '
			. 'pelo que o fabricante declarou — com código, modelos e data. Filtro de '
			. 'robô não é universal.',
	);
	$mapa['pecas-filtros-xiaomi'] = array(
		'tipo'      => 'website',
		'descricao' => 'Os filtros Xiaomi que o fabricante declarou, em quais modelos '
			. 'cada um serve, e em quais modelos Xiaomi não localizamos declaração '
			. 'nenhuma.',
	);
	$mapa['pecas-filtros-wap'] = array(
		'tipo'      => 'website',
		/* SEM CÓDIGO DE MODELO NA DESCRIÇÃO: o portão da casca reprova dígito em
		   cabeça, e ele está certo em não saber distinguir "W300" de um número
		   medido. Número em cabeça só entra derivado do banco, pelo mecanismo de
		   `numeros` da casca — e estas cinco páginas não declaram promessa. */
		'descricao' => 'Os filtros WAP declarados pela loja oficial, com código e '
			. 'modelo — inclusive os dois filtros diferentes que o mesmo robô pede.',
	);
	$mapa['pecas-filtros-electrolux'] = array(
		'tipo'      => 'website',
		'descricao' => 'O filtro avulso da Electrolux, os Kits Performance que trazem '
			. 'filtro, e em quais modelos a Electrolux não vende o filtro separado.',
	);
	return $mapa;
}
}

/* ---------------------------------------------------------------------------
 * 4. AS PEÇAS DE TELA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_num' ) ) {
function robometria_malha_num( $n ) {
	return '<span class="rbm-num">' . esc_html( number_format_i18n( (float) $n ) ) . '</span>';
}
}

/* ---------------------------------------------------------------------------
 * AS FRASES — escritas aqui, acentuadas, com o MESMO molde da referência.
 *
 * Este é o único lugar em que o PHP desta camada escreve texto, e ele não
 * inventa nenhum: cada molde abaixo é o gêmeo acentuado de um molde de
 * `ferramentas/gerar-malha-pecas.py`, e `ferramentas/teste-malha.php` compara os
 * dois, frase a frase, ignorando acento. Se um dos lados mudar sozinho, a
 * bancada reprova — que é a única coisa que impede duas implementações da mesma
 * frase de divergirem caladas (decisão 2 do bloco 4 do PROMPT.md).
 *
 * A GRAMÁTICA DO TIPO VEM NOS FATOS, nunca de uma tabela daqui: "a escova
 * lateral avulsa" e "o filtro avulso" flexionam, e uma segunda tabela de língua
 * dentro do snippet é a forma mais barata de a página passar a escrever "o
 * escova lateral" no dia em que a categoria nova nascer.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_frase_avulsos' ) ) {
function robometria_malha_frase_avulsos( $n, $singular, $plural, $g ) {
	if ( 1 === (int) $n ) {
		return sprintf( '1 %s %s', $singular, $g['avulso'] );
	}
	return sprintf( '%s %s %s', number_format_i18n( $n ), $plural, $g['avulsos'] );
}
}

if ( ! function_exists( 'robometria_malha_frase_kits' ) ) {
function robometria_malha_frase_kits( $n ) {
	return ( 1 === (int) $n ) ? '1 kit' : sprintf( '%s kits', number_format_i18n( $n ) );
}
}

if ( ! function_exists( 'robometria_malha_frases_da_filha' ) ) {
function robometria_malha_frases_da_filha( $f, $c ) {
	$g        = $c['gramatica'];
	$singular = $c['singular'];
	$plural   = $c['plural'];
	$marca    = $f['marca_rotulo'];
	$n        = (int) $f['itens_no_banco'];
	$cobertos = (int) $f['modelos_cobertos'];
	$total    = (int) $f['modelos_publicaveis_da_marca'];

	if ( $f['itens_em_kit'] > 0 ) {
		$quantos = sprintf(
			'São %s itens %s que entregam %s: %s e %s que %s %s na composição.',
			number_format_i18n( $n ), $marca, $singular,
			robometria_malha_frase_avulsos( $f['itens_avulsos'], $singular, $plural, $g ),
			robometria_malha_frase_kits( $f['itens_em_kit'] ),
			$f['itens_em_kit'] > 1 ? 'declaram' : 'declara',
			$singular
		);
		$sujeito = $n > 1 ? 'Eles servem' : 'Ele serve';
	} else {
		$quantos = ( $n > 1 )
			? sprintf( 'São %s %s %s no banco.', number_format_i18n( $n ), $plural, $marca )
			: sprintf( 'É 1 %s %s no banco.', $singular, $marca );
		$sujeito = $n > 1
			? $g['sujeito_plural'] . ' servem'
			: $g['sujeito_singular'] . ' serve';
	}

	$serve = ( $cobertos === $total )
		? sprintf( '%s em todos os %s modelos %s que a gente acompanha.',
			$sujeito, number_format_i18n( $total ), $marca )
		: sprintf( '%s em %s dos %s modelos %s que a gente acompanha.',
			$sujeito, number_format_i18n( $cobertos ), number_format_i18n( $total ), $marca );

	$faltam = $total - $cobertos;
	if ( $faltam > 1 ) {
		$residuo = sprintf(
			'Nos outros %s modelos não localizamos declaração do fabricante de %s; não vamos supor.',
			number_format_i18n( $faltam ), $singular );
	} elseif ( 1 === $faltam ) {
		$residuo = sprintf(
			'No outro modelo não localizamos declaração do fabricante de %s; não vamos supor.',
			$singular );
	} else {
		$residuo = '';
	}

	$so_kit = count( (array) $f['modelos_so_por_kit'] );
	if ( $so_kit > 0 ) {
		$kit = sprintf(
			'Em %s desses modelos %s %s só vem dentro do kit: %s não vende %s %s %s para %s.',
			number_format_i18n( $so_kit ), $g['artigo'], $singular,
			$f['gramatica_do_publicador'], $g['artigo'], $singular, $g['avulso'],
			$so_kit > 1 ? 'eles' : 'ele'
		);
	} else {
		$kit = '';
	}

	$marca_cruzada = ( 0 === (int) $f['itens_que_atravessam_marca'] )
		? sprintf( '%s %s %s serve em robô de outra marca, pelo que o fabricante declara.',
			$g['nenhum'], $g['desses'], $plural )
		: sprintf( '%s %s %s servem também em robô de outra marca, pelo que o fabricante declara.',
			number_format_i18n( $f['itens_que_atravessam_marca'] ), $g['desses'], $plural );

	/* "têm" com dois ou mais, "tem" com um: o verbo concorda com o sujeito, que
	   é o número de modelos. A referência é ASCII e não distingue os dois — a
	   comparação ignora acento, então é aqui que a conjugação certa existe. */
	$cobertura = sprintf( '%s de %s modelos %s do banco %s %s %s pelo fabricante.',
		number_format_i18n( $cobertos ), number_format_i18n( $total ), $marca,
		$cobertos > 1 ? 'têm' : 'tem', $singular, $g['declarado'] );

	return array(
		'quantos'       => $quantos,
		'serve'         => $serve,
		'residuo'       => $residuo,
		'kit'           => $kit,
		'marca_cruzada' => $marca_cruzada,
		'cobertura'     => $cobertura,
	);
}
}

if ( ! function_exists( 'robometria_malha_frase_dos_tipos' ) ) {
function robometria_malha_frase_dos_tipos( $secao ) {
	$nomes = array();
	foreach ( (array) $secao['tipos'] as $t ) {
		$nomes[] = $t['rotulo_singular'];
	}
	return sprintf( 'São %s tipos de peça no banco: %s.',
		number_format_i18n( count( $nomes ) ), robometria_malha_lista( $nomes ) );
}
}

if ( ! function_exists( 'robometria_malha_frases_da_categoria' ) ) {
function robometria_malha_frases_da_categoria( $c ) {
	$g        = $c['gramatica'];
	$singular = $c['singular'];
	$plural   = $c['plural'];

	$marcas = ( $c['marcas_no_banco'] > 1 )
		? sprintf( '%s marcas', number_format_i18n( $c['marcas_no_banco'] ) )
		: '1 marca';
	$modelos = ( $c['modelos_cobertos'] > 1 )
		? sprintf( '%s modelos de robô', number_format_i18n( $c['modelos_cobertos'] ) )
		: '1 modelo de robô';

	if ( $c['itens_em_kit'] > 0 ) {
		$quantos = sprintf(
			'São %s itens de reposição que entregam %s em %s: %s e %s que declaram %s na composição.',
			number_format_i18n( $c['itens_no_banco'] ), $singular, $marcas,
			robometria_malha_frase_avulsos( $c['itens_avulsos'], $singular, $plural, $g ),
			robometria_malha_frase_kits( $c['itens_em_kit'] ), $singular );
		$sujeito = 'Juntos, eles servem';
	} else {
		$quantos = sprintf( 'São %s %s de %s no banco.',
			number_format_i18n( $c['itens_no_banco'] ), $plural, $marcas );
		$sujeito = sprintf( '%s, %s servem', $g['juntos'], $g['eles'] );
	}

	$serve = sprintf( '%s em %s.', $sujeito, $modelos );

	$cruz = ( 0 === (int) $c['itens_que_atravessam_marca'] )
		? sprintf( '%s %s serve em mais de uma marca: %s de robô aspirador não é universal, e o encaixe é por modelo.',
			$g['nenhum'], $g['deles'], $singular )
		: sprintf( '%s %s servem em mais de uma marca; %s %s %s são de uma marca só.',
			number_format_i18n( $c['itens_que_atravessam_marca'] ), $g['deles'],
			( 'a' === $g['artigo'] ) ? 'as' : 'os', $g['outros'],
			number_format_i18n( $c['itens_no_banco'] - $c['itens_que_atravessam_marca'] ) );

	return array( 'quantos' => $quantos, 'serve' => $serve, 'marca_cruzada' => $cruz );
}
}

/**
 * O CARTÃO DE UM ITEM — mesma vitrine da R1, e de propósito.
 *
 * A seção 22 do contrato manda uma ilha ter UM padrão de interface: o leitor
 * que veio da ferramenta reconhece o cartão, e o CSS já existe na casca
 * (`robometria_casca_css_vitrine()`). A ordem dos dois últimos blocos é a regra
 * da seção 7 escrita em código — porta de compra ANTES da procedência.
 */
if ( ! function_exists( 'robometria_malha_cartao' ) ) {
function robometria_malha_cartao( $item, $singular, $curto = false ) {
	$html  = '<li class="rbm-vitrine-item">';
	$html .= robometria_casca_painel_da_foto( isset( $item['imagem'] ) ? $item['imagem'] : null );

	$html .= '<span class="rbm-vitrine-tipo">'
		. esc_html( $item['dentro_de_kit'] ? 'kit com ' . $singular : $singular ) . '</span>';
	$html .= '<span class="rbm-codigo-peca">'
		. esc_html( empty( $item['codigo'] ) ? 'sem código publicado' : $item['codigo'] )
		. '</span>';
	$html .= '<span class="rbm-vitrine-nome">' . esc_html( $item['nome_na_fonte'] ) . '</span>';

	$modelos = robometria_malha_rotulos( $item['modelos'], $curto );
	$html .= '<span class="rbm-vitrine-porque">' . esc_html(
		sprintf(
			/* translators: 1: publicador, 2: verbo, 3: lista de modelos */
			$item['dentro_de_kit']
				? '%1$s %2$s este kit para %3$s, e é dentro dele que vem o ' . $singular
				: '%1$s %2$s esta peça para %3$s',
			$item['publicador'],
			'declara',
			robometria_malha_lista( $modelos )
		)
	) . '</span>';

	if ( ! empty( $item['vida_util'] ) && null !== $item['vida_util']['valor'] ) {
		$html .= '<span class="rbm-vitrine-vida">vida útil declarada: <span class="rbm-num">'
			. esc_html( $item['vida_util']['valor'] ) . '</span> '
			. esc_html( $item['vida_util']['unidade'] ) . '</span>';
	}

	$html .= '<span class="rbm-vitrine-acao">' . robometria_casca_porta_de_compra( $item ) . '</span>';

	$html .= '<span class="rbm-vitrine-fonte">' . esc_html( 'Como sabemos — ' . $item['publicador'] )
		. ( empty( $item['verificado_em'] ) ? '' : esc_html( ' · ' . robometria_casca_data_br( $item['verificado_em'] ) ) )
		. ( empty( $item['url'] ) ? '' : ' · ' . robometria_casca_fonte_link( $item['url'] ) )
		. '</span>';

	$html .= '</li>';
	return $html;
}
}

/* Os rótulos de uma lista de modelos — com a marca, ou só o código. */
/* Primeira letra maiúscula, respeitando acento. */
if ( ! function_exists( 'robometria_malha_maiuscula' ) ) {
function robometria_malha_maiuscula( $t ) {
	$t = (string) $t;
	return mb_strtoupper( mb_substr( $t, 0, 1, 'UTF-8' ), 'UTF-8' ) . mb_substr( $t, 1, null, 'UTF-8' );
}
}

if ( ! function_exists( 'robometria_malha_rotulos' ) ) {
function robometria_malha_rotulos( $modelos, $curto = false ) {
	$saida = array();
	foreach ( (array) $modelos as $m ) {
		$saida[] = ( $curto && ! empty( $m['rotulo_curto'] ) ) ? $m['rotulo_curto'] : $m['rotulo'];
	}
	return $saida;
}
}

if ( ! function_exists( 'robometria_malha_lista' ) ) {
function robometria_malha_lista( $itens ) {
	$itens = array_values( array_filter( (array) $itens ) );
	if ( ! $itens ) {
		return '';
	}
	if ( 1 === count( $itens ) ) {
		return $itens[0];
	}
	$ultimo = array_pop( $itens );
	return implode( ', ', $itens ) . ' e ' . $ultimo;
}
}

/**
 * A TABELA PRÉ-RENDERIZADA (seção 5 do contrato).
 *
 * Ela existe para o leitor E para o modelo de linguagem: é a resposta inteira
 * em campos, sem clique nenhum. Cada linha carrega o código, os modelos, o
 * publicador e a data — a procedência DENTRO da linha, nunca numa nota de
 * rodapé que a citação perde.
 */
if ( ! function_exists( 'robometria_malha_tabela' ) ) {
function robometria_malha_tabela( $itens, $singular, $com_marca = false ) {
	/* Na tabela da categoria o rótulo do modelo leva a marca, porque ali há
	   várias; na da marca, não leva — a marca já está no H1 e na trilha. */
	$curto = ! $com_marca;
	$html = '<div class="rbm-tabela-rolagem"><table class="rbm-tabela"><thead><tr>';
	$html .= '<th scope="col">Código</th>';
	if ( $com_marca ) {
		$html .= '<th scope="col">Marca</th>';
	}
	$html .= '<th scope="col">Peça</th><th scope="col">Serve em</th>'
		. '<th scope="col">Quem declarou</th></tr></thead><tbody>';

	foreach ( (array) $itens as $i ) {
		$modelos = robometria_malha_rotulos( $i['modelos'], $curto );
		$html .= '<tr>';
		$html .= '<td><span class="rbm-codigo-peca">'
			. esc_html( empty( $i['codigo'] ) ? 'sem código' : $i['codigo'] ) . '</span></td>';
		if ( $com_marca ) {
			$html .= '<td>' . esc_html( $i['marca_rotulo'] ) . '</td>';
		}
		$html .= '<td>' . esc_html( $i['nome_na_fonte'] )
			. ( $i['dentro_de_kit'] ? ' <em>(o ' . esc_html( $singular ) . ' vem dentro do kit)</em>' : '' )
			. '</td>';
		$html .= '<td>' . esc_html( robometria_malha_lista( $modelos ) ) . '</td>';
		$html .= '<td>' . esc_html( $i['publicador'] )
			. ( empty( $i['verificado_em'] ) ? '' : esc_html( ' · ' . robometria_casca_data_br( $i['verificado_em'] ) ) )
			. ( empty( $i['url'] ) ? '' : ' · ' . robometria_casca_fonte_link( $i['url'] ) )
			. '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	return $html;
}
}

/* O aviso de comissão, dentro do bloco de compra e não no rodapé (seção 7 e a
   página de divulgação). Texto igual ao da R1 porque é a mesma promessa. */
if ( ! function_exists( 'robometria_malha_aviso_comissao' ) ) {
function robometria_malha_aviso_comissao() {
	$url = robometria_casca_url_se_existir( 'divulgacao-de-afiliados' );
	$fim = ( '' === $url ) ? '' : ' <a href="' . esc_url( $url ) . '">Como este site ganha dinheiro</a>.';
	return '<p class="rbm-aviso-comissao">Parte dos botões de compra abaixo são links de '
		. 'afiliado: se você comprar por eles, a Robometria pode receber comissão, sem custo '
		. 'a mais para você. Isso não muda a ordem da lista — ela é decidida pela declaração '
		. 'do fabricante, e só por ela.' . $fim . '</p>';
}
}

/* Os cartões das filhas de uma mãe (16.4a): TODAS as filhas, com âncora igual à
   consulta-alvo de cada uma. A que não está publicada sai sem link e diz "em
   breve", SEM contagem de banco — 16.5. */
if ( ! function_exists( 'robometria_malha_cartoes_de_filhas' ) ) {
function robometria_malha_cartoes_de_filhas( $chave_da_mae, $previstas ) {
	$paginas = robometria_malha_paginas();
	$html    = '<ul class="rbm-cartoes">';

	foreach ( $paginas as $chave => $def ) {
		if ( empty( $def['mae'] ) || $def['mae'] !== $chave_da_mae ) {
			continue;
		}
		$url = robometria_casca_url_se_existir( $chave );
		if ( '' === $url ) {
			continue;
		}
		$html .= '<li class="rbm-cartao"><a href="' . esc_url( $url ) . '">'
			. esc_html( $def['titulo'] ) . '</a></li>';
	}

	foreach ( (array) $previstas as $rotulo ) {
		$html .= '<li class="rbm-cartao rbm-cartao-espera">'
			. '<span>' . esc_html( $rotulo ) . '</span>'
			. '<span class="rbm-cartao-nota">em breve</span></li>';
	}

	$html .= '</ul>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 5. AS TRÊS PÁGINAS
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_pagina_secao' ) ) {
function robometria_malha_pagina_secao() {
	$d = robometria_malha_dados();
	if ( empty( $d['secao'] ) ) {
		return robometria_casca_sem_banco_html(
			'Esta é a estante de peças da Robometria.',
			'A medição está fora do ar neste momento, então não mostramos número nenhum aqui '
				. '— número sem banco atrás é chute, e chute é o que este site não faz.'
		);
	}

	$secao   = $d['secao'];
	$numeros = robometria_casca_numeros();

	/* A RESPOSTA VEM PRIMEIRO, e os três números dela são os da casca — os
	   mesmos que a metodologia e a home publicam, com a mesma régua. Recontar
	   aqui criaria a segunda cópia de `pares_declarados` que a R1 1.8.0 mediu no
	   ar com dois valores. Sem os três, a frase não sai pela metade: cai no
	   aviso honesto. */
	$resposta = robometria_casca_preencher_molde(
		'O banco tem %1$s peças publicáveis de %2$s marcas e %3$s pares peça × modelo, '
			. 'todos declarados pelo fabricante.',
		array( 'pecas_publicaveis', 'marcas', 'pares_declarados' )
	);
	if ( '' === $resposta ) {
		return robometria_casca_sem_banco_html(
			'Esta é a estante de peças da Robometria.',
			'A medição está fora do ar neste momento, então não mostramos número nenhum aqui.'
		);
	}

	$html  = '<div class="rbm-malha rbm-malha-secao">';
	$html .= '<p class="rbm-linha-mestra">Quer trocar uma peça do seu robô e saber se ela '
		. 'encaixa? Escolha o tipo de peça abaixo, ou vá direto para a ferramenta e diga a '
		. 'marca e o modelo.</p>';
	$html .= '<p class="rbm-prova">' . esc_html( $resposta ) . '</p>';

	/* A ferramenta é a porta principal desta seção: a filha de maior intenção
	   de compra da ilha inteira, e ela já está no ar (VOZ.md, molde FERRAMENTA). */
	$url_r1 = robometria_casca_url_se_existir( 'qual-peca-serve-no-meu-robo-aspirador' );
	if ( '' !== $url_r1 ) {
		$html .= '<p class="rbm-malha-ferramenta"><a href="' . esc_url( $url_r1 ) . '">'
			. 'Qual peça serve no meu robô aspirador</a> — diga a marca e o modelo e veja '
			. 'filtro, escova, mop e bateria de uma vez.</p>';
	}

	$html .= '<h2>Por tipo de peça</h2>';

	/* AS CATEGORIAS AINDA NÃO PUBLICADAS SAEM SEM CONTAGEM (16.5). O rótulo sai
	   do mesmo lugar que a categoria publicada — os fatos —, então a próxima
	   leva não precisa editar esta lista. */
	$previstas = array();
	foreach ( (array) $secao['tipos'] as $t ) {
		if ( '' !== robometria_casca_url_se_existir( $t['categoria'] ) ) {
			continue;
		}
		$previstas[] = $t['rotulo'];
	}
	$html .= robometria_malha_cartoes_de_filhas( 'pecas', $previstas );

	/* O QUE JA ESTA NO AR — a tabela pré-renderizada desta página (seção 5).
	   Ela fala só das filhas PUBLICADAS: contagem de categoria que não existe é
	   promessa datada, e é isso que a 16.5 proíbe no cartão em espera. */
	$linhas = robometria_malha_linhas_publicadas();
	if ( $linhas ) {
		$html .= '<h2>O que já está no ar</h2>';
		$html .= '<div class="rbm-tabela-rolagem"><table class="rbm-tabela"><thead><tr>'
			. '<th scope="col">Página</th><th scope="col">Itens no banco</th>'
			. '<th scope="col">Modelos que ela responde</th></tr></thead><tbody>';
		foreach ( $linhas as $l ) {
			$html .= '<tr><td><a href="' . esc_url( $l['url'] ) . '">' . esc_html( $l['titulo'] )
				. '</a></td><td><span class="rbm-num">' . esc_html( number_format_i18n( $l['itens'] ) )
				. '</span></td><td><span class="rbm-num">'
				. esc_html( number_format_i18n( $l['modelos'] ) ) . '</span> de <span class="rbm-num">'
				. esc_html( number_format_i18n( $l['modelos_da_marca'] ) ) . '</span> '
				. esc_html( $l['marca_rotulo'] ) . '</td></tr>';
		}
		$html .= '</tbody></table></div>';
	}

	$html .= '<h2>O que a gente já conferiu</h2>';
	$html .= '<p>' . esc_html( robometria_malha_frase_dos_tipos( $secao ) ) . '</p>';
	$html .= '<p class="rbm-prova">Toda linha deste site sai de uma declaração do fabricante '
		. 'com endereço e data. Quando ele não declara, a resposta é “não localizamos” — a '
		. 'gente não supõe compatibilidade, porque peça que não encaixa é dinheiro perdido '
		. 'de quem comprou.</p>';

	$html .= '<h2>Três coisas que mudam a resposta</h2>';
	$html .= '<p><strong>O código na etiqueta manda.</strong> Robô da mesma linha e do mesmo '
		. 'ano troca de peça sem trocar de nome comercial. Confere o código embaixo do '
		. 'aparelho, na etiqueta de série, e compara com o código que o fabricante declarou — '
		. 'é ele que está nas tabelas daqui, nunca o nome do anúncio.</p>';
	$html .= '<p><strong>Tem peça que só existe dentro do kit.</strong> Em algumas marcas o '
		. 'fabricante não vende o filtro ou a escova separados: a única forma de comprar a '
		. 'peça original é o kit de manutenção do modelo. Quando é esse o caso, a página diz, '
		. 'e diz em quais modelos — porque comprar o kit sem saber disso é pagar por três '
		. 'peças para trocar uma.</p>';
	$html .= '<p><strong>Quando dois canais do fabricante discordam, vale o mais estreito.</strong> '
		. 'Acontece de a loja oficial listar um modelo a mais do que o manual. Nesse caso a '
		. 'Robometria publica as duas declarações com as duas datas e fica com a lista menor: '
		. 'errar para o lado largo faz alguém comprar peça que não encaixa.</p>';

	$html .= '</div>';
	return $html;
}
}

/* As filhas publicadas de toda categoria, com a contagem de cada uma — a linha
   da tabela de /pecas/. Contada do registro mais os fatos; nada digitado. */
if ( ! function_exists( 'robometria_malha_linhas_publicadas' ) ) {
function robometria_malha_linhas_publicadas() {
	$linhas  = array();
	$paginas = robometria_malha_paginas();

	foreach ( $paginas as $chave => $def ) {
		if ( 'filha' !== $def['papel'] ) {
			continue;
		}
		$url = robometria_casca_url_se_existir( $chave );
		if ( '' === $url ) {
			continue;
		}
		$f = robometria_malha_filha( $chave );
		if ( empty( $f['itens'] ) ) {
			continue;
		}
		$linhas[] = array(
			'titulo'           => $def['titulo'],
			'url'              => $url,
			'itens'            => (int) $f['itens_no_banco'],
			'modelos'          => (int) $f['modelos_cobertos'],
			'modelos_da_marca' => (int) $f['modelos_publicaveis_da_marca'],
			'marca_rotulo'     => $f['marca_rotulo'],
		);
	}

	return $linhas;
}
}

if ( ! function_exists( 'robometria_malha_pagina_categoria' ) ) {
function robometria_malha_pagina_categoria( $chave ) {
	$c = robometria_malha_categoria( $chave );
	if ( empty( $c['filhas'] ) ) {
		return robometria_casca_sem_banco_html(
			'Aqui ficam os filtros de robô aspirador, marca por marca.',
			'A medição está fora do ar neste momento, então não mostramos número nenhum.'
		);
	}

	$singular = $c['singular'];
	$plural   = $c['plural'];

	$frases = robometria_malha_frases_da_categoria( $c );

	/* A ABERTURA FALA COM QUEM ENTROU, e a prova desce um parágrafo (VOZ.md e o
	   portão da voz). A frase derivada continua servida — ela é o veredito —,
	   mas dentro do bloco de prova: quem chega irritado com a peça na mão não
	   entra para ler uma contagem, entra para saber se encaixa. */
	$html  = '<div class="rbm-malha rbm-malha-categoria">';
	$html .= '<p class="rbm-linha-mestra">' . esc_html( sprintf(
		'%s de robô aspirador não é peça universal: o encaixe é por modelo, e o que serve '
			. 'no seu não serve no do vizinho. Escolha a marca do seu robô e veja o que o '
			. 'fabricante declarou.',
		robometria_malha_maiuscula( $singular ) ) ) . '</p>';
	$html .= '<p class="rbm-prova">' . esc_html( $frases['quantos'] ) . ' '
		. esc_html( $frases['serve'] ) . ' ' . esc_html( $frases['marca_cruzada'] ) . '</p>';

	$html .= '<h2>Escolha a marca do seu robô</h2>';

	$previstas = array();
	foreach ( (array) $c['filhas'] as $f ) {
		if ( '' !== robometria_casca_url_se_existir( $f['slug'] ) ) {
			continue;
		}
		$previstas[] = $f['marca_rotulo'];
	}
	$html .= robometria_malha_cartoes_de_filhas( $chave, $previstas );

	/* A TABELA INTEIRA DA CATEGORIA, com a coluna de marca: é a resposta que um
	   modelo de linguagem cita, e ela não depende de clicar em filha nenhuma. */
	$todos = array();
	foreach ( (array) $c['filhas'] as $f ) {
		foreach ( (array) $f['itens'] as $i ) {
			$i['marca_rotulo'] = $f['marca_rotulo'];
			$todos[]           = $i;
		}
	}
	$html .= '<h2>Todos os ' . esc_html( $plural ) . ' que o fabricante declarou</h2>';
	$html .= robometria_malha_tabela( $todos, $singular, true );

	$url_a1 = robometria_casca_url_se_existir( 'filtro-universal-de-robo-aspirador' );
	if ( '' !== $url_a1 ) {
		$html .= '<p class="rbm-malha-par">Por que não existe <a href="' . esc_url( $url_a1 )
			. '">filtro universal de robô aspirador</a>: a gente conferiu peça por peça.</p>';
	}

	$html .= '</div>';
	return $html;
}
}

if ( ! function_exists( 'robometria_malha_pagina_filha' ) ) {
function robometria_malha_pagina_filha( $chave ) {
	$f = robometria_malha_filha( $chave );
	if ( empty( $f['itens'] ) ) {
		return robometria_casca_sem_banco_html(
			'Aqui ficam os filtros desta marca, com o código e os modelos.',
			'A medição está fora do ar neste momento, então não mostramos número nenhum.'
		);
	}

	$paginas  = robometria_malha_paginas();
	$def      = isset( $paginas[ $chave ] ) ? $paginas[ $chave ] : array();
	$cat      = robometria_malha_categoria( isset( $def['mae'] ) ? $def['mae'] : '' );
	$singular = isset( $cat['singular'] ) ? $cat['singular'] : $f['tipo'];
	$plural   = isset( $cat['plural'] ) ? $cat['plural'] : $f['tipo'];

	$html  = '<div class="rbm-malha rbm-malha-filha">';

	/* O VEREDITO ACIMA DA DOBRA (DESIGN.md): a resposta primeiro, a explicação
	   depois — e a explicação só se a pessoa descer. */
	$frases = robometria_malha_frases_da_filha( $f, $cat );

	$html .= '<p class="rbm-linha-mestra">' . esc_html( sprintf(
		'Antes de comprar %s %s, confere o código na etiqueta embaixo do seu robô: é ele '
			. 'que manda, não o nome do anúncio.',
		( 'a' === $cat['gramatica']['artigo'] ) ? 'uma' : 'um', $singular ) ) . '</p>';

	$html .= '<p class="rbm-prova">' . esc_html( $frases['quantos'] ) . ' '
		. esc_html( $frases['serve'] ) . '</p>';

	if ( '' !== $frases['kit'] ) {
		$html .= '<p class="rbm-ressalva">' . esc_html( $frases['kit'] ) . '</p>';
	}

	/* A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA (seção 7, decisão 5
	   do bloco 4). O aviso de comissão mora DENTRO do bloco. */
	$html .= '<h2>Onde comprar ' . esc_html( 1 === count( $f['itens'] ) ? 'este ' . $singular : 'estes ' . $plural ) . '</h2>';
	$html .= robometria_malha_aviso_comissao();
	$html .= '<ul class="rbm-vitrine">';
	foreach ( (array) $f['itens'] as $i ) {
		$html .= robometria_malha_cartao( $i, $singular, true );
	}
	$html .= '</ul>';

	$html .= '<h2>O que serve em qual modelo</h2>';
	$html .= robometria_malha_tabela( $f['itens'], $singular, false );
	$html .= '<p class="rbm-prova">' . esc_html( $frases['marca_cruzada'] ) . '</p>';

	/* O NÚMERO PRÓPRIO DESTA PÁGINA, e é o que nenhum concorrente publica: a
	   COBERTURA da marca — quantos modelos dela têm a peça declarada, e quais
	   ficam de fora, com nome. Dizer o que não se sabe é metade do produto
	   desta ilha (seção 7: silêncio parece defeito). */
	$html .= '<h2>Em quais modelos ' . esc_html( $f['marca_rotulo'] ) . ' a gente já sabe responder</h2>';
	$html .= '<p>' . esc_html( $frases['cobertura'] ) . '</p>';

	if ( ! empty( $f['modelos_sem_a_peca'] ) ) {
		$fora = robometria_malha_rotulos( $f['modelos_sem_a_peca'], true );
		$html .= '<p class="rbm-ressalva">' . esc_html( $frases['residuo'] ) . ' '
			. esc_html( sprintf( 'São eles: %s.', robometria_malha_lista( $fora ) ) ) . '</p>';
	}

	/* A FRASE QUE LINKA A MÃE, no corpo (16.4b). O bloco "Veja também" com as
	   irmãs é da casca e entra no fim do conteúdo. */
	/* A FRASE DA MÃE (16.4b), com o nome dela lido do registro — nunca digitado
	   aqui, que foi como seis páginas desta ilha passaram a ter dois nomes em
	   11/09/2026. A contagem de marcas é CONTADA: quantas filhas da mesma mãe
	   estão publicadas. */
	$chave_mae = isset( $def['mae'] ) ? $def['mae'] : '';
	$url_mae   = robometria_casca_url_se_existir( $chave_mae );
	if ( '' !== $url_mae && isset( $paginas[ $chave_mae ] ) ) {
		$irmas = 0;
		foreach ( $paginas as $chave_irma => $irma ) {
			if ( ! empty( $irma['mae'] ) && $irma['mae'] === $chave_mae
				&& '' !== robometria_casca_url_se_existir( $chave_irma ) ) {
				$irmas++;
			}
		}
		$html .= '<p class="rbm-malha-mae">' . esc_html( sprintf(
			'Esta é uma das %s marcas desta prateleira. Veja',
			number_format_i18n( $irmas ) ) )
			. ' <a href="' . esc_url( $url_mae ) . '">'
			. esc_html( sprintf( 'todos os %s de robô aspirador, marca por marca', $plural ) )
			. '</a>.</p>';
	}

	$url_r1 = robometria_casca_url_se_existir( 'qual-peca-serve-no-meu-robo-aspirador' );
	if ( '' !== $url_r1 ) {
		$html .= '<p class="rbm-malha-ferramenta">Quer conferir as outras peças do mesmo robô? '
			. '<a href="' . esc_url( $url_r1 ) . '">Qual peça serve no meu robô aspirador</a> '
			. 'responde filtro, escova, mop e bateria de uma vez.</p>';
	}

	$html .= '</div>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6. O JSON-LD — CollectionPage + ItemList
 *
 * ItemList com `name`, e não Product: esta ilha não publica preço nem
 * disponibilidade, e Product sem offers é schema que o Google marca como
 * incompleto. O que a página tem de verdade é uma LISTA de peças com código e
 * modelos, então é isso que ela declara. A data sai de
 * robometria_casca_datas_da_pagina() — sem ela, nenhuma data é publicada.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_jsonld' ) ) {
function robometria_malha_jsonld( $chave ) {
	$paginas = robometria_malha_paginas();
	if ( ! isset( $paginas[ $chave ] ) ) {
		return array();
	}
	$def = $paginas[ $chave ];
	$url = robometria_casca_url_se_existir( $chave );
	if ( '' === $url ) {
		return array();
	}

	$cabeca = robometria_casca_cabeca_resolvida( $chave );
	$itens  = array();

	if ( 'filha' === $def['papel'] ) {
		$f = robometria_malha_filha( $chave );
		foreach ( (array) ( isset( $f['itens'] ) ? $f['itens'] : array() ) as $n => $i ) {
			$modelos = array();
			foreach ( (array) $i['modelos'] as $m ) {
				$modelos[] = $m['rotulo'];
			}
			$itens[] = array(
				'@type'    => 'ListItem',
				'position' => $n + 1,
				'name'     => trim( $i['nome_na_fonte'] . ( empty( $i['codigo'] ) ? '' : ' (' . $i['codigo'] . ')' ) ),
				'description' => sprintf( 'Declarado por %s para %s.', $i['publicador'],
					robometria_malha_lista( $modelos ) ),
			);
		}
	} else {
		foreach ( $paginas as $chave_filha => $filha ) {
			if ( empty( $filha['mae'] ) || $filha['mae'] !== $chave ) {
				continue;
			}
			$url_filha = robometria_casca_url_se_existir( $chave_filha );
			if ( '' === $url_filha ) {
				continue;
			}
			$itens[] = array(
				'@type'    => 'ListItem',
				'position' => count( $itens ) + 1,
				'name'     => $filha['titulo'],
				'url'      => $url_filha,
			);
		}
	}

	$doc = array(
		'@context' => 'https://schema.org',
		'@type'    => 'CollectionPage',
		'@id'      => $url . '#pagina',
		'url'      => $url,
		'name'     => $def['titulo'],
		'inLanguage' => 'pt-BR',
	);
	if ( ! empty( $cabeca['descricao'] ) ) {
		$doc['description'] = $cabeca['descricao'];
	}

	$datas = robometria_casca_datas_da_pagina( $chave );
	if ( ! empty( $datas['datePublished'] ) ) {
		$doc['datePublished'] = $datas['datePublished'];
	}
	if ( ! empty( $datas['dateModified'] ) ) {
		$doc['dateModified'] = $datas['dateModified'];
	}

	if ( $itens ) {
		$doc['mainEntity'] = array(
			'@type'           => 'ItemList',
			'numberOfItems'   => count( $itens ),
			'itemListElement' => $itens,
		);
	}

	return $doc;
}
}

add_action( 'wp_head', function () {
	if ( ! function_exists( 'robometria_casca_slug_atual' ) ) {
		return;
	}
	$chave   = robometria_casca_slug_atual();
	$paginas = robometria_malha_paginas();
	if ( ! isset( $paginas[ $chave ] ) ) {
		return;
	}
	$doc = robometria_malha_jsonld( $chave );
	if ( ! $doc ) {
		return;
	}
	echo '<script type="application/ld+json">' . wp_json_encode( $doc ) . '</script>' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * 7. O CSS — no wp_head, NUNCA dentro do retorno do shortcode.
 *
 * O WordPress passa o conteúdo por wpautop e por wptexturize, e `<style>` ali
 * dentro vira parágrafo quebrado e `&` vira `&#038;`. Foi assim que a Aquametria
 * perdeu cinco calculadoras, e é o que a seção 8 do contrato cobra.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$css = <<<'CSS'
.rbm-malha h2{margin:2rem 0 .6rem;font-size:1.25rem;}
.rbm-malha .rbm-linha-mestra{font-family:var(--rbm-display);font-weight:700;font-size:1.25rem;line-height:1.35;margin:0 0 .6rem;border-left:4px solid var(--rbm-varredura);padding-left:.8rem;}
.rbm-malha .rbm-ressalva{color:var(--rbm-alerta);font-size:.94rem;line-height:1.55;}
.rbm-malha .rbm-malha-mae,.rbm-malha .rbm-malha-ferramenta,.rbm-malha .rbm-malha-par{font-size:.96rem;line-height:1.55;}
.rbm-cartoes{list-style:none;margin:.6rem 0 0;padding:0;display:grid;gap:.6rem;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));}
.rbm-cartao{background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:4px;padding:.9rem;display:flex;flex-direction:column;gap:.2rem;font-size:.96rem;}
.rbm-cartao-espera{color:var(--rbm-legenda);}
.rbm-cartao-nota{font-size:.8rem;color:var(--rbm-legenda);}
.rbm-tabela-rolagem{overflow-x:auto;}
.rbm-tabela{width:100%;border-collapse:collapse;background:var(--rbm-superficie);font-size:.92rem;}
.rbm-tabela th{text-align:left;font-size:.8rem;text-transform:uppercase;letter-spacing:.04em;color:var(--rbm-legenda);border-bottom:1px solid var(--rbm-traco);padding:.5rem .6rem;}
.rbm-tabela td{border-bottom:1px solid var(--rbm-traco);padding:.55rem .6rem;vertical-align:top;line-height:1.45;}
CSS;

	if ( function_exists( 'robometria_casca_css_vitrine' ) ) {
		$css = robometria_casca_css_vitrine() . "\n" . $css;
	}
	echo '<style id="robometria-malha">' . $css . '</style>' . "\n";
}, 12 );

/* ---------------------------------------------------------------------------
 * 8. OS SHORTCODES — um por página, registrados a partir do registro.
 *
 * Um shortcode só, resolvido pela página atual, seria mais curto e teria um
 * defeito: as bancadas desta ilha montam cada página a partir da TAG dela, num
 * processo próprio, e uma tag para cinco páginas mediria a mesma página cinco
 * vezes sem ninguém ver. A tag sai da chave por regra (str_replace), então nada
 * aqui é digitado duas vezes.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_render' ) ) {
function robometria_malha_render( $chave ) {
	$paginas = robometria_malha_paginas();
	if ( ! isset( $paginas[ $chave ] ) ) {
		return '';
	}
	switch ( $paginas[ $chave ]['papel'] ) {
		case 'secao':
			return robometria_malha_pagina_secao();
		case 'categoria':
			return robometria_malha_pagina_categoria( $chave );
		default:
			return robometria_malha_pagina_filha( $chave );
	}
}
}

foreach ( array_keys( robometria_malha_paginas() ) as $__rbm_chave ) {
	/* A CHAVE VIAJA NO FECHAMENTO, e não no terceiro argumento do shortcode: o
	   WordPress passa a tag para quem a declara, mas nem todo chamador passa —
	   a bancada monta a página chamando o shortcode sem argumento nenhum, que é
	   o que o `do_shortcode` de um conteúdo sem atributo também faz. Fechamento
	   que depende de um argumento opcional é fechamento que funciona no site e
	   morre na régua. */
	add_shortcode( robometria_malha_tag_da_chave( $__rbm_chave ),
		function () use ( $__rbm_chave ) {
			return robometria_malha_render( $__rbm_chave );
		} );
}
unset( $__rbm_chave );

/* ---------------------------------------------------------------------------
 * 9. AS PÁGINAS NO WORDPRESS — com pai de verdade (16.2)
 *
 * A ordem do registro É a ordem da criação: mãe antes de filha, porque o
 * post_parent precisa do ID dela. Página cuja mãe não existe NÃO é criada — e o
 * relato diz por quê, em vez de nascer uma página solta na raiz com o slug da
 * filha, que é o defeito que ninguém veria até o endereço aparecer no sitemap.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_malha_garantir_paginas' ) ) {
function robometria_malha_garantir_paginas() {
	$feita = get_option( 'robometria_malha_estrutura' );
	if ( ROBOMETRIA_MALHA_VERSAO === $feita ) {
		return;
	}

	$ids   = array();
	$criou = false;

	foreach ( robometria_malha_paginas() as $chave => $def ) {
		$conteudo = '[' . robometria_malha_tag_da_chave( $chave ) . ']';
		$pai      = 0;
		if ( ! empty( $def['mae'] ) ) {
			if ( empty( $ids[ $def['mae'] ] ) ) {
				continue;
			}
			$pai = (int) $ids[ $def['mae'] ];
		}

		$pagina = robometria_malha_pagina_existente( $chave, $def, $pai );

		if ( ! $pagina ) {
			$pid = wp_insert_post( array(
				'post_type'      => 'page',
				'post_title'     => $def['titulo'],
				'post_name'      => $def['post_name'],
				'post_parent'    => $pai,
				'post_content'   => $conteudo,
				'post_status'    => 'publish',
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $pid ) ) {
				continue;
			}
			update_post_meta( $pid, '_robometria_casca', '1' );
			update_post_meta( $pid, '_robometria_id', $chave );
			$ids[ $chave ] = (int) $pid;
			$criou         = true;
			continue;
		}

		$pid           = (int) $pagina->ID;
		$ids[ $chave ] = $pid;
		$nossa         = ( '1' === get_post_meta( $pid, '_robometria_casca', true ) );

		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
		}
		if ( $nossa && false === strpos( (string) $pagina->post_content, $conteudo ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $conteudo ) );
		}
		/* O TÍTULO É NOSSO e é reespelhado; o post_name NÃO é tocado — a URL não
		   muda com o nome (12.1). O PAI é corrigido quando estiver errado: uma
		   página desta malha na raiz é uma URL fora da árvore, e a 16.2 diz que
		   página sem pai é defeito. */
		if ( $nossa && (string) $pagina->post_title !== (string) $def['titulo'] ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => $def['titulo'] ) );
		}
		if ( $nossa && (int) $pagina->post_parent !== $pai ) {
			wp_update_post( array( 'ID' => $pid, 'post_parent' => $pai ) );
			$criou = true;
		}
	}

	if ( $criou ) {
		flush_rewrite_rules( false );
	}

	update_option( 'robometria_malha_estrutura', ROBOMETRIA_MALHA_VERSAO, false );
}
}

/**
 * A página desta chave, se já existir — pelo meta canônico primeiro.
 *
 * O caminho pelo `get_page_by_path()` vem depois e usa o CAMINHO inteiro
 * (pecas/filtros/xiaomi), nunca o último degrau: `xiaomi` sozinho pega a página
 * errada no dia em que `/modelos/xiaomi/` existir.
 */
if ( ! function_exists( 'robometria_malha_pagina_existente' ) ) {
function robometria_malha_pagina_existente( $chave, $def, $pai ) {
	$achados = get_posts( array(
		'post_type'   => 'page',
		'post_status' => 'any',
		'meta_key'    => '_robometria_id',
		'meta_value'  => $chave,
		'numberposts' => 1,
	) );
	if ( $achados ) {
		return $achados[0];
	}

	$pagina = get_page_by_path( $def['caminho'], OBJECT, 'page' );
	return $pagina ? $pagina : null;
}
}

if ( ! function_exists( 'robometria_malha_boot' ) ) {
function robometria_malha_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;
	robometria_malha_garantir_paginas();
}
}

add_action( 'init', 'robometria_malha_boot', 22 );

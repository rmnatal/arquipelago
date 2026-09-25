/**
 * Clube do Mosaico F1 — Quantas pastilhas e quanto rejunte comprar
 * Versão 1.0.0 (11/09/2026) — bloco 4 da fila, a segunda ferramenta da ilha.
 *
 * O QUE ELA RESPONDE, e por que ganha (seção 14.9 do ARQUIPELAGO.md): o bloco 1
 * mediu que a primeira página inteira de "rejunte para mosaico" responde à
 * pergunta de OBRA — 0,2 a 0,4 kg/m², "1 kg faz 3 m²" —, e esses números foram
 * calculados com azulejo grande e junta larga. Aplicando a fórmula publicada
 * pelo PRÓPRIO fabricante ao tamanho real da pastilha de artesanato, o consumo é
 * 2,8 kg/m² para pastilha de 1×1 cm com junta de 2 mm: sete a catorze vezes o
 * que a SERP publica. Esta página não disputa aquelas — ela responde outra
 * pergunta, e hoje é a única em português que a responde com a conta à vista.
 *
 * ------------------------------------------------------------------------
 * AS CINCO DECISÕES DE DESENHO, e a cicatriz que cada uma evita
 * ------------------------------------------------------------------------
 *
 * 1. A CONTA É DO SERVIDOR, como na F2. O formulário é um GET para a própria
 *    página e o PHP responde. Não existe uma linha de decisão em JavaScript:
 *    ferramenta que calcula no navegador mostra a um modelo de linguagem um
 *    formulário VAZIO (seção 5 do contrato), e régua duplicada entre PHP e JS é
 *    duas réguas que se separam em silêncio. O preço é URL com parâmetro, pago
 *    na mesma linha: estado com parâmetro sai com `noindex, follow`, e quem
 *    entra no índice é a página-âncora, uma só.
 *
 * 2. A GEOMETRIA É NOSSA; O CONSUMO É DO FABRICANTE. Área e contagem de
 *    pastilha são aritmética desta ilha e não dependem de banco nenhum. Já os
 *    gramas de rejunte saem da fórmula de consumo publicada pela Quartzolit, e
 *    o coeficiente dela é LIDO DO BANCO — nunca digitado aqui. Sem banco, a
 *    página continua respondendo área e pastilhas e diz, com todas as letras,
 *    que não publica os gramas. Meia resposta declarada vale mais que uma
 *    resposta inteira inventada (seção 10).
 *
 * 3. O CR VALE PARA REJUNTE CIMENTÍCIO, E A TELA DIZ ISSO. É a correção do
 *    bloco 3c: o 1,75 sai do exemplo publicado pelo fabricante, e esse exemplo
 *    é de rejunte cimentício em pó. Dos cinco rejuntes do banco, dois não são
 *    pó — o acrílico é pronto uso em pote e o epóxi é bicomponente. Aplicar o
 *    coeficiente de um pó a eles seria supor que a fórmula vale sem olhar o
 *    estado físico do produto. Então a ferramenta RECUSA o número para esses
 *    dois e nomeia o que falta. E se dois produtos do banco declararem
 *    coeficientes diferentes, ela também recusa: escolher um dos dois calado é
 *    a mesma coisa com outra roupa.
 *
 * 4. A RÉGUA DO REJUNTE JÁ TEM DONO. Quem decide qual rejunte serve para a
 *    folga e para o lugar é a F2 — `cdm_f2_celula_rejunte()`, com as quatro
 *    regras do esquema. Esta página CHAMA aquela régua em vez de escrever uma
 *    segunda: duas implementações da mesma decisão no mesmo site é o defeito
 *    que a Robometria pagou comparando duas cópias da mesma régua. Se a F2 não
 *    estiver no ar, a F1 responde a conta e diz que a recomendação de produto
 *    está fora — não a improvisa.
 *
 * 5. A SOBRA VAI NA PASTILHA E NÃO NO REJUNTE, e ela arredonda PARA CIMA. Lote
 *    novo de pastilha muda de cor: faltar dez peças no meio da peça é pior que
 *    sobrar dez. O rejunte sai do saco e não tem esse problema, então ele sai
 *    limpo, do jeito que a fórmula do fabricante devolve.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTA PÁGINA DIZ QUE NÃO SABE
 * ------------------------------------------------------------------------
 * A coluna de gramas de COLA nasce vazia, com o motivo escrito: o fabricante do
 * silicone declara rendimento por cordão, não por área, e o consumo por área da
 * cimentcola não foi obtido. As duas pendências estão nomeadas no
 * `dados/constantes.json`.
 *
 * ------------------------------------------------------------------------
 * VERSÃO 1.2.0 (13/09/2026) — A VITRINE DE PASTILHA
 * ------------------------------------------------------------------------
 * Até a 1.1.0 esta página dizia "ainda não temos as pastilhas no nosso banco".
 * O banco existia desde 12/09/2026, com treze itens em 13/09, publicado como
 * option e lido pela casca — e nenhuma linha de código desta ferramenta o abria.
 * Dado no banco e tela sem leitor é o mesmo defeito que a F2 tinha com o
 * `url_busca`, e aqui era mais caro: esta é a ferramenta cuja pergunta É
 * "quantas pastilhas comprar".
 *
 * O que entrou, e o comentário do bloco 6b explica cada um: a vitrine filtrada
 * pelo lado, com as três travas em ordem (lado, formato, fonte) e uma frase por
 * causa; a prestação de contas das quatro listas disjuntas, que somam o banco
 * contado do arquivo; a porta do caquinho irregular para os lados que o seletor
 * não oferece; e a tabela pré-renderizada do banco inteiro, que existe porque o
 * estado-âncora desta página é 1 cm e 1 cm tem zero item.
 *
 * O que NÃO entrou, e é declarado: quantas pastilhas vêm na placa. Nenhum dos
 * treze fabricantes publica, a divisão ingênua não fecha em 9 dos 13 e fecha
 * exigindo junta zero nos outros 4 — então o cartão fala em PLACA, que é conta
 * de área e não supõe nada, e a página diz na cara que a peça a gente não
 * converte. Os treze também estão sem link e sem piso de busca, o que é defeito
 * declarado da 19.1: gerar o link exige a sessão do painel de afiliado, e o
 * cartão reserva o lugar em vez de sumir.
 *
 * ------------------------------------------------------------------------
 * VERSÃO 1.3.0 (14/09/2026) — A ORDEM DAS DUAS VITRINES, E O FIM DO TÍTULO
 * QUE DEPENDIA DE ESTAR EM SEGUNDO LUGAR
 * ------------------------------------------------------------------------
 * Até a 1.2.0 o bloco do REJUNTE vinha antes do bloco da PASTILHA, e a ordem
 * não era uma decisão: era herança. Quando a vitrine de rejunte nasceu, o lugar
 * da pastilha era uma frase de espera ("ainda não temos as pastilhas no nosso
 * banco"), então o rejunte era o único bloco de compra que a página tinha. A
 * 1.2.0 encheu o lugar da frase de espera com treze produtos e manteve a
 * sequência de chamada, que é como uma ordem provisória sobrevive a quem a
 * tornou errada.
 *
 * POR QUE A PASTILHA VEM PRIMEIRO, e a razão é a mesma em três superfícies: o
 * `<title>`, o H1 e a frase de resposta desta página falam de PASTILHA — "leva
 * cerca de N pastilhas de X cm" é a primeira coisa que a página afirma, e o
 * rejunte entra nela como o segundo número. A seção 22.1 do ARQUIPELAGO.md põe
 * ranqueamento antes de conversão e conversão antes de beleza; aqui as três
 * apontam para o mesmo lado, porque quem chega por "quantas pastilhas para
 * mosaico" veio comprar pastilha. O `VOZ.md` desta ilha diz "produto primeiro".
 * Nada da seção 22.2 se move: a resposta continua antes da explicação, os dois
 * blocos de compra continuam ANTES da camada de prova (seção 7), e nenhuma URL,
 * trilha, âncora ou JSON-LD muda.
 *
 * O QUE A TROCA REVELOU, e é o que fez disto um bloco em vez de um `swap`: o
 * título do bloco da pastilha era "E onde comprar a pastilha". Aquele "E" é
 * conector — ele só faz sentido depois de outro bloco de compra, e é um título
 * que MENTE quando a ordem muda. Pior: a seção 5 do contrato pede frase
 * autossuficiente, que sobreviva a ser citada fora de contexto, e é justamente
 * o título que um modelo de linguagem cita sozinho. Agora os dois títulos são
 * autossuficientes — "Onde comprar a pastilha" e "Qual rejunte cabe nessa
 * folga" —, e nenhum depende da posição em que foi servido.
 *
 * E A FRONTEIRA DOS DOIS BLOCOS PASSOU A TER NOME. A bancada e a conferência no
 * ar extraíam cada vitrine pelo TEXTO do `<h2>` — régua que morre calada no dia
 * em que o título muda, e que no estado degradado do rejunte (sem a F2 no ar, o
 * título é outro) nunca conseguiu extrair nada. Cada seção agora declara o que
 * ela é na própria classe: `cdm-f1-vitrine-pastilha` e `cdm-f1-vitrine-rejunte`,
 * em TODAS as saídas, inclusive as degradadas. É a cicatriz da Robometria de
 * 13/09/2026 escrita nesta ilha: fronteira de teste é marcador escrito, nunca
 * "a primeira coisa parecida com".
 */

if ( ! defined( 'CDM_F1_VERSAO' ) ) {
	define( 'CDM_F1_VERSAO', '1.3.1' );
}
if ( ! defined( 'CDM_F1_SLUG' ) ) {
	/* Mesma escolha da F2, pelo mesmo motivo (ARVORE.md, seção 2): nível 3 com
	   mãe /materiais/ direto. A categoria definitiva — `pastilhas` ou
	   `rejuntes` — só nasce com três filhas de dado real (16.5), e esta página
	   atravessa as duas. Pôr a ferramenta debaixo de categoria que não existe
	   criaria degrau de trilha sem endereço e obrigaria a mover a URL depois. */
	define( 'CDM_F1_SLUG', 'materiais/quantas-pastilhas-para-mosaico' );
}
if ( ! defined( 'CDM_F1_TITULO' ) ) {
	/* UM NOME POR PÁGINA, em toda superfície: cartão da home, cartão do Guia,
	   degrau da trilha, H1 e <title>. 41 caracteres; com o sufixo do site o
	   <title> fica em 60, abaixo do teto de 65. */
	define( 'CDM_F1_TITULO', 'Quantas pastilhas e quanto rejunte comprar' );
}

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — a página, o cartão e o degrau da trilha
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	$paginas[ CDM_F1_SLUG ] = array(
		'titulo'   => CDM_F1_TITULO,
		'conteudo' => '[cdm_f1]',
		'pai'      => 'materiais',
	);

	return $paginas;
} );

add_filter( 'cdm_ferramentas', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $f ) {
		if ( isset( $f['codigo'] ) && 'F1' === $f['codigo'] ) {
			$lista[ $i ]['titulo'] = CDM_F1_TITULO;
			$lista[ $i ]['slug']   = CDM_F1_SLUG;
			$lista[ $i ]['estado'] = 'publicada';
		}
	}

	return $lista;
} );

/* ---------------------------------------------------------------------------
 * 2. A geometria — aritmética desta ilha, sem banco e sem fonte externa
 *
 * Cada fórmula é a da superfície que REALMENTE recebe caquinho. O vaso reto é
 * só a lateral (o fundo não se reveste), o cônico é o tronco de cone pela
 * geratriz — não pela altura, que é o erro que diminui a área em peça bojuda —,
 * e a moldura é o retângulo menos o vão.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_formas' ) ) {
/**
 * As formas, com os campos que cada uma pede e o exemplo que abre a página.
 * As CHAVES dos campos são o vocabulário da entrada; quem acrescentar forma
 * aqui ganha o formulário, a conta e a varredura do teste de graça.
 */
function cdm_f1_formas() {
	return array(
		'cilindro' => array(
			'rotulo'  => 'Vaso reto ou cilindro (a lateral)',
			'campos'  => array( 'd' => 'Diâmetro, em cm', 'h' => 'Altura, em cm' ),
			'padrao'  => array( 'd' => 15, 'h' => 20 ),
			'formula' => 'a volta do vaso vezes a altura',
		),
		'conico' => array(
			'rotulo'  => 'Vaso cônico ou cachepô (a lateral)',
			'campos'  => array( 'd' => 'Diâmetro da boca, em cm', 'd2' => 'Diâmetro do fundo, em cm', 'h' => 'Altura, em cm' ),
			'padrao'  => array( 'd' => 18, 'd2' => 12, 'h' => 15 ),
			'formula' => 'a volta média vezes a lateral inclinada',
		),
		'placa' => array(
			'rotulo'  => 'Placa, quadro ou bandeja (um retângulo)',
			'campos'  => array( 'l' => 'Largura, em cm', 'a' => 'Altura, em cm' ),
			'padrao'  => array( 'l' => 30, 'a' => 40 ),
			'formula' => 'largura vezes altura',
		),
		'disco' => array(
			'rotulo'  => 'Tampo redondo ou mandala (um círculo)',
			'campos'  => array( 'd' => 'Diâmetro, em cm' ),
			'padrao'  => array( 'd' => 60 ),
			'formula' => 'a área do círculo',
		),
		'esfera' => array(
			'rotulo'  => 'Esfera ou bola',
			'campos'  => array( 'd' => 'Diâmetro, em cm' ),
			'padrao'  => array( 'd' => 20 ),
			'formula' => 'a área da esfera inteira',
		),
		'moldura' => array(
			'rotulo'  => 'Moldura de espelho ou quadro (com vão no meio)',
			'campos'  => array(
				'l'  => 'Largura de fora, em cm',
				'a'  => 'Altura de fora, em cm',
				'vl' => 'Largura do vão, em cm',
				'va' => 'Altura do vão, em cm',
			),
			'padrao'  => array( 'l' => 40, 'a' => 60, 'vl' => 30, 'va' => 50 ),
			'formula' => 'o retângulo de fora menos o vão',
		),
	);
}
}

if ( ! function_exists( 'cdm_f1_area_cm2' ) ) {
/**
 * A área a revestir, em cm². Devolve null quando a medida não fecha — moldura
 * com vão maior que a peça, cone com fundo maior que a boca invertido, zero.
 * Devolver zero seria pior: zero vira "compre nada" com cara de resposta.
 */
function cdm_f1_area_cm2( $forma, $m ) {
	$d  = isset( $m['d'] ) ? (float) $m['d'] : 0.0;
	$d2 = isset( $m['d2'] ) ? (float) $m['d2'] : 0.0;
	$h  = isset( $m['h'] ) ? (float) $m['h'] : 0.0;
	$l  = isset( $m['l'] ) ? (float) $m['l'] : 0.0;
	$a  = isset( $m['a'] ) ? (float) $m['a'] : 0.0;
	$vl = isset( $m['vl'] ) ? (float) $m['vl'] : 0.0;
	$va = isset( $m['va'] ) ? (float) $m['va'] : 0.0;

	switch ( $forma ) {
		case 'cilindro':
			return ( $d > 0 && $h > 0 ) ? M_PI * $d * $h : null;

		case 'conico':
			if ( $d <= 0 || $d2 <= 0 || $h <= 0 ) {
				return null;
			}
			/* A GERATRIZ, não a altura. Num cachepô de 18 para 12 cm com 15 cm de
			   altura a diferença é de 2%; num vaso bem bojudo passa de 10%, e
			   ela sempre erra para MENOS — quem usa a altura compra pastilha de
			   menos, que é o lado caro do erro. */
			$geratriz = sqrt( pow( ( $d - $d2 ) / 2, 2 ) + pow( $h, 2 ) );
			return M_PI * ( ( $d + $d2 ) / 2 ) * $geratriz;

		case 'placa':
			return ( $l > 0 && $a > 0 ) ? $l * $a : null;

		case 'disco':
			return ( $d > 0 ) ? M_PI * pow( $d, 2 ) / 4 : null;

		case 'esfera':
			return ( $d > 0 ) ? M_PI * pow( $d, 2 ) : null;

		case 'moldura':
			if ( $l <= 0 || $a <= 0 || $vl < 0 || $va < 0 ) {
				return null;
			}
			if ( $vl >= $l || $va >= $a ) {
				return null; // vão maior que a peça: não é moldura, é engano de digitação
			}
			return ( $l * $a ) - ( $vl * $va );
	}

	return null;
}
}

if ( ! function_exists( 'cdm_f1_pastilhas' ) ) {
/**
 * Quantas pastilhas, já com a sobra, SEMPRE para cima.
 *
 * O passo é o lado mais a junta: é a distância de um canto ao canto seguinte, e
 * é ela que manda — não o lado sozinho. Com junta de 2 mm, a pastilha de 1 cm
 * ocupa 1,2 cm de parede, e 100 delas cobrem 144 cm², não 100.
 */
function cdm_f1_pastilhas( $area_cm2, $lado_mm, $junta_mm, $sobra_pct ) {
	if ( null === $area_cm2 || $area_cm2 <= 0 || $lado_mm <= 0 || $junta_mm < 0 ) {
		return null;
	}
	$passo_mm = $lado_mm + $junta_mm;
	$area_m2  = $area_cm2 / 10000;
	$por_m2   = 1000000 / ( $passo_mm * $passo_mm );

	return (int) ceil( $area_m2 * $por_m2 * ( 1 + ( $sobra_pct / 100 ) ) );
}
}

if ( ! function_exists( 'cdm_f1_por_m2' ) ) {
/** Pastilhas por metro quadrado, sem sobra — o número que a tabela cita. */
function cdm_f1_por_m2( $lado_mm, $junta_mm ) {
	$passo_mm = $lado_mm + $junta_mm;
	if ( $passo_mm <= 0 ) {
		return null;
	}

	return 1000000 / ( $passo_mm * $passo_mm );
}
}

/* ---------------------------------------------------------------------------
 * 3. O consumo de rejunte — a fórmula é do fabricante e o CR vem do banco
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_banco_rejuntes' ) ) {
/**
 * O banco de rejuntes, lido da option que o Sync grava.
 *
 * Lido AQUI e não pela F2: a conta de gramas não depende da régua de
 * elegibilidade, e fazer a F1 depender da F2 para ler um número do banco seria
 * criar uma dependência que a página não precisa ter para responder.
 */
function cdm_f1_banco_rejuntes() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}
	$bruto = get_option( 'clubedomosaico_dados_materiais-rejuntes' );
	$banco = ( is_array( $bruto ) && ! empty( $bruto['materiais'] ) ) ? $bruto : array( 'materiais' => array() );

	return $banco;
}
}

if ( ! function_exists( 'cdm_f1_banco_pastilhas' ) ) {
/**
 * O banco de pastilhas, lido da option que o Sync grava. Só item `ativo`.
 *
 * Ele existe desde 12/09/2026 e até a 1.1.0 nenhuma linha de código o lia: a
 * página dizia "ainda não temos as pastilhas no nosso banco" com treze itens
 * gravados e publicados como option. É o mesmo defeito que a F2 tinha com o
 * `url_busca` — dado no banco, tela sem leitor — e o custo aqui era maior,
 * porque esta é a ferramenta cuja pergunta É "quantas pastilhas comprar".
 */
function cdm_f1_banco_pastilhas() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}
	$bruto = get_option( 'clubedomosaico_dados_materiais-pastilhas' );
	$itens = array();
	if ( is_array( $bruto ) && ! empty( $bruto['materiais'] ) && is_array( $bruto['materiais'] ) ) {
		foreach ( $bruto['materiais'] as $m ) {
			if ( empty( $m['id'] ) || 'ativo' !== ( isset( $m['status'] ) ? $m['status'] : '' ) ) {
				continue;
			}
			$itens[] = $m;
		}
	}
	$banco = array( 'materiais' => $itens );

	return $banco;
}
}

if ( ! function_exists( 'cdm_f1_coeficiente' ) ) {
/**
 * O CR da fórmula de consumo, tirado do banco — e a recusa quando ele não dá.
 *
 * Devolve array( valor, produto, fonte, coletado_em ) ou null com o motivo.
 * Três caminhos, e os três são resposta:
 *   - um único CR declarado entre os rejuntes cimentícios: é ele;
 *   - nenhum: a página não publica gramas e diz que o coeficiente não veio;
 *   - dois valores diferentes: TAMBÉM não publica. Escolher um dos dois em
 *     silêncio é a mesma invenção, só que disfarçada de cálculo.
 */
function cdm_f1_coeficiente() {
	static $cr = null;
	if ( null !== $cr ) {
		return $cr;
	}

	$valores = array();
	$origem  = array();
	foreach ( cdm_f1_banco_rejuntes()['materiais'] as $m ) {
		if ( 'cimenticio' !== ( isset( $m['tipo'] ) ? $m['tipo'] : '' ) ) {
			continue;
		}
		if ( 'ativo' !== ( isset( $m['status'] ) ? $m['status'] : '' ) ) {
			continue;
		}
		$valor = isset( $m['propriedades']['CR']['valor'] ) ? $m['propriedades']['CR']['valor'] : null;
		if ( null === $valor || (float) $valor <= 0 ) {
			continue;
		}
		$chave             = (string) (float) $valor;
		$valores[ $chave ] = (float) $valor;
		if ( ! isset( $origem[ $chave ] ) ) {
			$origem[ $chave ] = $m;
		}
	}

	if ( 1 !== count( $valores ) ) {
		$cr = array(
			'valor'  => null,
			'motivo' => count( $valores ) > 1
				? 'o banco tem mais de um coeficiente declarado e eles não são iguais'
				: 'o coeficiente da fórmula não está no banco',
		);

		return $cr;
	}

	$chave = key( $valores );
	$m     = $origem[ $chave ];
	$fonte = null;
	$id_f  = isset( $m['propriedades']['CR']['fonte_id'] ) ? $m['propriedades']['CR']['fonte_id'] : '';
	if ( '' !== $id_f && isset( $m['fontes'][ $id_f ] ) ) {
		$fonte = $m['fontes'][ $id_f ];
	}

	$cr = array(
		'valor'         => $valores[ $chave ],
		'produto'       => isset( $m['nome_comercial'] ) ? $m['nome_comercial'] : '',
		'fabricante'    => isset( $m['fabricante'] ) ? $m['fabricante'] : '',
		'url'           => ( $fonte && ! empty( $fonte['url'] ) ) ? $fonte['url'] : '',
		'coletado_em'   => ( $fonte && ! empty( $fonte['coletado_em'] ) ) ? $fonte['coletado_em'] : '',
		'declarado_como' => isset( $m['propriedades']['CR']['declarado_como'] ) ? $m['propriedades']['CR']['declarado_como'] : '',
		'motivo'        => '',
	);

	return $cr;
}
}

if ( ! function_exists( 'cdm_f1_consumo_kg_m2' ) ) {
/**
 * ((A + B) × E × L × CR) / (A × B) — a fórmula publicada pelo fabricante, com A
 * e B os lados da pastilha em mm, E a espessura, L a junta.
 *
 * Confere sozinha com o exemplo do próprio fabricante: peça de 200×200 mm, 8 mm
 * de espessura, junta de 10 mm e CR 1,75 dão 1,4 kg/m². É esse exemplo que
 * amarra o coeficiente ao rejunte cimentício em pó.
 */
function cdm_f1_consumo_kg_m2( $lado_mm, $espessura_mm, $junta_mm, $cr ) {
	if ( $lado_mm <= 0 || $espessura_mm <= 0 || $junta_mm <= 0 || $cr <= 0 ) {
		return null;
	}

	return ( ( $lado_mm + $lado_mm ) * $espessura_mm * $junta_mm * $cr ) / ( $lado_mm * $lado_mm );
}
}

if ( ! function_exists( 'cdm_f1_gramas' ) ) {
/** Gramas de rejunte para a área. Sem sobra: o saco não muda de cor. */
function cdm_f1_gramas( $area_cm2, $consumo_kg_m2 ) {
	if ( null === $area_cm2 || null === $consumo_kg_m2 ) {
		return null;
	}

	return ( $area_cm2 / 10000 ) * $consumo_kg_m2 * 1000;
}
}

if ( ! function_exists( 'cdm_f1_gramas_na_tela' ) ) {
/**
 * Peça de colar consome 3,5 g e vaso grande consome 577 g: arredondar tudo para
 * inteiro transformaria a primeira em "4 g" — e a diferença entre 3,5 e 4 numa
 * peça de 25 cm² é 14%. Abaixo de 10 g sai com uma casa; acima, inteiro.
 */
function cdm_f1_gramas_na_tela( $g ) {
	if ( null === $g ) {
		return '';
	}
	if ( $g < 10 ) {
		return '<span class="cdm-num">' . esc_html( number_format_i18n( round( $g, 1 ), 1 ) ) . '</span>';
	}

	return cdm_casca_num( round( $g ) );
}
}

/* ---------------------------------------------------------------------------
 * 4. As doze peças típicas — a tabela pré-renderizada
 *
 * São as ENTRADAS, e só elas. Nenhum resultado está escrito aqui: os números da
 * tabela saem das mesmas funções que respondem ao formulário, então tabela e
 * resposta não podem discordar. Os valores esperados, escritos à mão no bloco 2
 * a partir das fórmulas, moram em `dados/pecas-tipicas.json` e são lidos pela
 * bancada — nunca por esta página. É a trava da seção 8: quem confere escreve a
 * própria régua, e as duas escritas são independentes.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_pecas_tipicas' ) ) {
function cdm_f1_pecas_tipicas() {
	return array(
		array( 'nome' => 'Vaso cilíndrico de 15 cm de diâmetro por 20 de altura', 'forma' => 'cilindro', 'medidas' => array( 'd' => 15, 'h' => 20 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Cachepô cônico de 18 para 12 cm, 15 de altura', 'forma' => 'conico', 'medidas' => array( 'd' => 18, 'd2' => 12, 'h' => 15 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Tampo redondo de 60 cm', 'forma' => 'disco', 'medidas' => array( 'd' => 60 ), 'lado_mm' => 20, 'junta_mm' => 3, 'espessura_mm' => 4 ),
		array( 'nome' => 'Quadro ou placa de 30 × 40 cm', 'forma' => 'placa', 'medidas' => array( 'l' => 30, 'a' => 40 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Moldura de espelho 40 × 60, vão de 30 × 50', 'forma' => 'moldura', 'medidas' => array( 'l' => 40, 'a' => 60, 'vl' => 30, 'va' => 50 ), 'lado_mm' => 20, 'junta_mm' => 3, 'espessura_mm' => 4 ),
		array( 'nome' => 'Esfera decorativa de 20 cm', 'forma' => 'esfera', 'medidas' => array( 'd' => 20 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Mandala em disco de 40 cm', 'forma' => 'disco', 'medidas' => array( 'd' => 40 ), 'lado_mm' => 25, 'junta_mm' => 4, 'espessura_mm' => 5 ),
		array( 'nome' => 'Filtro de barro de 30 cm de diâmetro por 40 de altura', 'forma' => 'cilindro', 'medidas' => array( 'd' => 30, 'h' => 40 ), 'lado_mm' => 20, 'junta_mm' => 3, 'espessura_mm' => 4 ),
		array( 'nome' => 'Placa de número de casa, 20 × 30 cm', 'forma' => 'placa', 'medidas' => array( 'l' => 20, 'a' => 30 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Bandeja de 25 × 35 cm', 'forma' => 'placa', 'medidas' => array( 'l' => 25, 'a' => 35 ), 'lado_mm' => 10, 'junta_mm' => 2, 'espessura_mm' => 4 ),
		array( 'nome' => 'Vaso grande de 25 cm de diâmetro por 35 de altura', 'forma' => 'cilindro', 'medidas' => array( 'd' => 25, 'h' => 35 ), 'lado_mm' => 25, 'junta_mm' => 3, 'espessura_mm' => 5 ),
		array( 'nome' => 'Pingente de colar, 5 × 5 cm', 'forma' => 'placa', 'medidas' => array( 'l' => 5, 'a' => 5 ), 'lado_mm' => 10, 'junta_mm' => 1, 'espessura_mm' => 4 ),
	);
}
}

/* ---------------------------------------------------------------------------
 * 5. A entrada
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_pastilhas_disponiveis' ) ) {
/**
 * Os tamanhos de pastilha da tela. A chave é o vocabulário da entrada (sem
 * ponto, porque ela viaja na URL e passa por sanitize_key); o valor é o lado em
 * milímetros, que é a unidade da fórmula do fabricante.
 */
function cdm_f1_pastilhas_disponiveis() {
	return array(
		'p10'       => array( 'rotulo' => 'Pastilha de 1 × 1 cm', 'lado_mm' => 10 ),
		'p15'       => array( 'rotulo' => 'Pastilha de 1,5 × 1,5 cm', 'lado_mm' => 15 ),
		'p20'       => array( 'rotulo' => 'Pastilha de 2 × 2 cm', 'lado_mm' => 20 ),
		'p25'       => array( 'rotulo' => 'Pastilha de 2,5 × 2,5 cm', 'lado_mm' => 25 ),
		'irregular' => array( 'rotulo' => 'Caquinho irregular (eu meço o lado médio)', 'lado_mm' => null ),
	);
}
}

if ( ! function_exists( 'cdm_f1_sobras' ) ) {
function cdm_f1_sobras() {
	return array(
		0  => 'Sem sobra — eu tenho as peças contadas',
		5  => '5% de sobra',
		10 => '10% de sobra (o comum)',
		15 => '15% de sobra',
		20 => '20% de sobra — vou recortar muito',
	);
}
}

if ( ! function_exists( 'cdm_f1_tipos_de_rejunte' ) ) {
/**
 * Os três estados físicos, com o nome do pote. Não é gosto: é exatamente o que
 * decide se a fórmula do fabricante vale para o produto (decisão 3 do topo).
 */
function cdm_f1_tipos_de_rejunte() {
	return array(
		'cimenticio' => 'Rejunte cimentício — o que vem em pó, para misturar',
		'acrilico'   => 'Rejunte acrílico — o pronto para usar, em pote',
		'epoxi'      => 'Rejunte epóxi — o de duas partes, que se mistura na hora',
	);
}
}

if ( ! function_exists( 'cdm_f1_numero' ) ) {
/** Número digitado pela pessoa: vírgula é vírgula, e fora da faixa volta ao padrão. */
function cdm_f1_numero( $bruto, $minimo, $maximo, $padrao ) {
	if ( ! is_string( $bruto ) && ! is_numeric( $bruto ) ) {
		return $padrao;
	}
	$texto = str_replace( ',', '.', trim( (string) $bruto ) );
	if ( '' === $texto || ! is_numeric( $texto ) ) {
		return $padrao;
	}
	$valor = (float) $texto;
	if ( $valor < $minimo || $valor > $maximo ) {
		return $padrao;
	}

	return $valor;
}
}

if ( ! function_exists( 'cdm_f1_entrada' ) ) {
/**
 * O que a pessoa escolheu, saneado contra o vocabulário. Valor fora da faixa
 * volta ao padrão, e o padrão é a peça mais comum do nicho: vaso cilíndrico de
 * 15 por 20, pastilha de 1 cm, junta de 2 mm, 10% de sobra.
 */
function cdm_f1_entrada() {
	$formas = cdm_f1_formas();
	$tam    = cdm_f1_pastilhas_disponiveis();
	$sobras = cdm_f1_sobras();
	$tipos  = cdm_f1_tipos_de_rejunte();

	$forma = isset( $_GET['forma'] ) ? sanitize_key( wp_unslash( $_GET['forma'] ) ) : '';
	$forma = isset( $formas[ $forma ] ) ? $forma : 'cilindro';

	$tamanho = isset( $_GET['pastilha'] ) ? sanitize_key( wp_unslash( $_GET['pastilha'] ) ) : '';
	$tamanho = isset( $tam[ $tamanho ] ) ? $tamanho : 'p10';

	$junta = isset( $_GET['junta'] ) ? (int) $_GET['junta'] : 0;
	$sobra = isset( $_GET['sobra'] ) ? (int) $_GET['sobra'] : -1;
	$tipo  = isset( $_GET['rejunte'] ) ? sanitize_key( wp_unslash( $_GET['rejunte'] ) ) : '';

	/* As medidas: só as que a forma escolhida pede, cada uma na faixa do que é
	   peça de artesanato. 500 cm é teto generoso — acima disso não é peça, é
	   parede, e parede é outra conta (a de obra, que a SERP já responde). */
	$medidas = array();
	foreach ( $formas[ $forma ]['campos'] as $campo => $rotulo ) {
		$padrao            = isset( $formas[ $forma ]['padrao'][ $campo ] ) ? $formas[ $forma ]['padrao'][ $campo ] : 10;
		$medidas[ $campo ] = cdm_f1_numero( isset( $_GET[ $campo ] ) ? wp_unslash( $_GET[ $campo ] ) : null, 0.5, 500, $padrao );
	}

	/* O LADO DO CAQUINHO IRREGULAR é entrada, não constante — pastilha
	   industrializada tem lado; caco de prato quebrado não tem. */
	$lado_eq = cdm_f1_numero( isset( $_GET['ladoeq'] ) ? wp_unslash( $_GET['ladoeq'] ) : null, 0.3, 10, 2 );
	$lado_mm = ( 'irregular' === $tamanho ) ? $lado_eq * 10 : $tam[ $tamanho ]['lado_mm'];

	/* A ESPESSURA TAMBÉM É ENTRADA. Nenhum fabricante de pastilha de artesanato
	   publica espessura padronizada, então a ilha não finge conhecê-la: o campo
	   vem com valor sugerido e com o aviso de medir a sua. */
	$espessura = cdm_f1_numero( isset( $_GET['esp'] ) ? wp_unslash( $_GET['esp'] ) : null, 1, 20, 4 );

	$escolheu = ( isset( $_GET['forma'] ) || isset( $_GET['pastilha'] ) || isset( $_GET['junta'] )
		|| isset( $_GET['sobra'] ) || isset( $_GET['rejunte'] ) || isset( $_GET['d'] ) || isset( $_GET['h'] )
		|| isset( $_GET['l'] ) || isset( $_GET['a'] ) || isset( $_GET['esp'] ) || isset( $_GET['onde'] ) );

	return array(
		'forma'     => $forma,
		'medidas'   => $medidas,
		'tamanho'   => $tamanho,
		'lado_eq'   => $lado_eq,
		'lado_mm'   => $lado_mm,
		'espessura' => $espessura,
		/* Até 12 mm pelo mesmo motivo da F2: a grade pisa em 11, que é o
		   primeiro valor depois do maior extremo que algum fabricante declara.
		   Quem tem folga de 11 mm recebe a verdade — nenhum rejunte do banco
		   cobre essa folga — em vez de cair calado no padrão de 2 mm. */
		'junta'     => ( $junta >= 1 && $junta <= 12 ) ? $junta : 2,
		'sobra'     => isset( $sobras[ $sobra ] ) ? $sobra : 10,
		'rejunte'   => isset( $tipos[ $tipo ] ) ? $tipo : 'cimenticio',
		'ambiente'  => cdm_f1_ambiente_escolhido(),
		'escolheu'  => $escolheu,
	);
}
}

if ( ! function_exists( 'cdm_f1_ambiente_escolhido' ) ) {
/**
 * O lugar onde a peça vai ficar, no VOCABULÁRIO DA F2 — e só quando a F2 está
 * no ar. Sem ela, esta página não tem régua para decidir produto e não finge
 * ter: não há segunda lista de ambientes escrita aqui, porque duas listas do
 * mesmo vocabulário no mesmo site envelhecem separadas.
 */
function cdm_f1_ambiente_escolhido() {
	if ( ! function_exists( 'cdm_f2_rotulos' ) ) {
		return '';
	}
	$rot = cdm_f2_rotulos();
	$amb = isset( $_GET['onde'] ) ? sanitize_key( wp_unslash( $_GET['onde'] ) ) : '';

	return isset( $rot['ambiente'][ $amb ] ) ? $amb : 'interno_seco';
}
}

/* ---------------------------------------------------------------------------
 * 6. A resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_calcular' ) ) {
/**
 * Uma entrada, todos os números. É esta função que a tabela das doze peças e o
 * formulário chamam — as duas telas não podem discordar porque não há duas
 * contas.
 */
function cdm_f1_calcular( $forma, $medidas, $lado_mm, $junta_mm, $espessura_mm, $sobra_pct, $tipo_rejunte = 'cimenticio' ) {
	$area = cdm_f1_area_cm2( $forma, $medidas );
	$cr   = cdm_f1_coeficiente();

	$consumo = null;
	$gramas  = null;
	$recusa  = '';

	if ( 'cimenticio' !== $tipo_rejunte ) {
		/* A RECUSA DO BLOCO 3c, e ela é do TIPO, não do produto. */
		$recusa = 'tipo';
	} elseif ( null === $cr['valor'] ) {
		$recusa = 'coeficiente';
	} else {
		$consumo = cdm_f1_consumo_kg_m2( $lado_mm, $espessura_mm, $junta_mm, $cr['valor'] );
		$gramas  = cdm_f1_gramas( $area, $consumo );
	}

	return array(
		'area_cm2'  => $area,
		'pastilhas' => cdm_f1_pastilhas( $area, $lado_mm, $junta_mm, $sobra_pct ),
		'por_m2'    => cdm_f1_por_m2( $lado_mm, $junta_mm ),
		'consumo'   => $consumo,
		'gramas'    => $gramas,
		'recusa'    => $recusa,
		'cr'        => $cr,
	);
}
}

if ( ! function_exists( 'cdm_f1_medida_em_texto' ) ) {
/** "15 cm de diâmetro por 20 de altura" — a peça dita como gente diz. */
function cdm_f1_medida_em_texto( $forma, $medidas ) {
	$n = function ( $v ) {
		return cdm_casca_num( ( (float) $v == (int) $v ) ? (int) $v : round( $v, 1 ) );
	};

	switch ( $forma ) {
		case 'cilindro':
			return $n( $medidas['d'] ) . ' cm de diâmetro por ' . $n( $medidas['h'] ) . ' cm de altura';
		case 'conico':
			return $n( $medidas['d'] ) . ' cm na boca, ' . $n( $medidas['d2'] ) . ' cm no fundo e ' . $n( $medidas['h'] ) . ' cm de altura';
		case 'placa':
			return $n( $medidas['l'] ) . ' por ' . $n( $medidas['a'] ) . ' cm';
		case 'disco':
		case 'esfera':
			return $n( $medidas['d'] ) . ' cm de diâmetro';
		case 'moldura':
			return $n( $medidas['l'] ) . ' por ' . $n( $medidas['a'] ) . ' cm, com vão de '
				. $n( $medidas['vl'] ) . ' por ' . $n( $medidas['va'] ) . ' cm';
	}

	return '';
}
}

if ( ! function_exists( 'cdm_f1_lado_em_texto' ) ) {
function cdm_f1_lado_em_texto( $lado_mm ) {
	$cm = $lado_mm / 10;

	return number_format_i18n( ( (float) $cm == (int) $cm ) ? $cm : round( $cm, 1 ), ( (float) $cm == (int) $cm ) ? 0 : 1 );
}
}

if ( ! function_exists( 'cdm_f1_resposta_html' ) ) {
/**
 * A RESPOSTA ANTES DA EXPLICAÇÃO (seção 5 do contrato, item 2): o número e o
 * critério nos primeiros parágrafos, em frase que sobrevive a ser citada fora
 * de contexto — com a peça, o tamanho do caquinho, a folga e a sobra dentro da
 * própria frase.
 */
function cdm_f1_resposta_html( $e ) {
	$r     = cdm_f1_calcular( $e['forma'], $e['medidas'], $e['lado_mm'], $e['junta'], $e['espessura'], $e['sobra'], $e['rejunte'] );
	$forma = cdm_f1_formas();

	$html = '<div class="cdm-f1-resposta" id="resposta">';

	if ( null === $r['area_cm2'] ) {
		$html .= '<p class="cdm-f1-frase cdm-f1-faixa">Com essas medidas a peça não fecha: o vão ficou maior que a moldura, '
			. 'ou alguma medida ficou em branco. Confira os números aí em cima e a gente responde.</p></div>';

		return $html;
	}

	$html .= '<p class="cdm-f1-frase">Uma peça assim, de <strong>' . cdm_f1_medida_em_texto( $e['forma'], $e['medidas'] )
		. '</strong>, tem <strong>' . cdm_casca_num( round( $r['area_cm2'] ) ) . ' cm²</strong> para revestir'
		. ' e leva cerca de <strong>' . cdm_casca_num( $r['pastilhas'] ) . ' pastilhas</strong> de '
		. esc_html( cdm_f1_lado_em_texto( $e['lado_mm'] ) ) . ' cm';

	if ( $e['sobra'] > 0 ) {
		$html .= ' — já com ' . cdm_casca_num( $e['sobra'] ) . '% de sobra para quebra e recorte —';
	}
	$html .= ', com ' . cdm_casca_num( $e['junta'] ) . ' mm de folga entre uma e outra.';

	if ( null !== $r['gramas'] ) {
		$html .= ' O rejunte cimentício dessa peça dá <strong>' . cdm_f1_gramas_na_tela( $r['gramas'] ) . ' g</strong>, '
			. 'na conta de ' . esc_html( number_format_i18n( round( $r['consumo'], 2 ), 2 ) ) . ' kg por metro quadrado.';
	}
	$html .= '</p>';

	/* O QUE A PESSOA VAI FAZER COM O NÚMERO: a área em m², que é a unidade em
	   que o material é vendido, e o rendimento por metro. Sem isso a resposta
	   serve para conferir e não para comprar. */
	$html .= '<ul class="cdm-f1-numeros">';
	$html .= '<li><span class="cdm-f1-rotulo">Área a revestir</span><span class="cdm-f1-valor">'
		. cdm_casca_num( round( $r['area_cm2'] ) ) . ' cm² <span class="cdm-f1-nota">('
		. esc_html( number_format_i18n( round( $r['area_cm2'] / 10000, 3 ), 3 ) ) . ' m², que é como o material é vendido)</span></span></li>';
	$html .= '<li><span class="cdm-f1-rotulo">Pastilhas por metro quadrado</span><span class="cdm-f1-valor">'
		. cdm_casca_num( round( $r['por_m2'] ) ) . ' <span class="cdm-f1-nota">(sem a sobra; o passo é '
		. esc_html( number_format_i18n( ( $e['lado_mm'] + $e['junta'] ) / 10, 1 ) ) . ' cm)</span></span></li>';
	$html .= '<li><span class="cdm-f1-rotulo">Pastilhas para comprar</span><span class="cdm-f1-valor">'
		. cdm_casca_num( $r['pastilhas'] ) . ' <span class="cdm-f1-nota">(arredondado para cima, sempre)</span></span></li>';

	if ( null !== $r['gramas'] ) {
		$html .= '<li><span class="cdm-f1-rotulo">Rejunte cimentício</span><span class="cdm-f1-valor">'
			. cdm_f1_gramas_na_tela( $r['gramas'] ) . ' g <span class="cdm-f1-nota">('
			. esc_html( number_format_i18n( round( $r['consumo'], 2 ), 2 ) ) . ' kg/m², com pastilha de '
			. esc_html( number_format_i18n( $e['espessura'], 0 ) ) . ' mm de espessura)</span></span></li>';
	} elseif ( 'tipo' === $r['recusa'] ) {
		$tipos = cdm_f1_tipos_de_rejunte();
		$html .= '<li><span class="cdm-f1-rotulo">Rejunte</span><span class="cdm-f1-valor cdm-f1-vazio">a gente não calcula para esse'
			. ' <span class="cdm-f1-nota">(veja logo abaixo por quê)</span></span></li>';
		unset( $tipos );
	} else {
		$html .= '<li><span class="cdm-f1-rotulo">Rejunte</span><span class="cdm-f1-valor cdm-f1-vazio">sem número hoje'
			. ' <span class="cdm-f1-nota">(' . esc_html( $r['cr']['motivo'] ) . ')</span></span></li>';
	}

	/* A COLUNA DE COLA NASCE VAZIA, COM O MOTIVO — e não some. Sumir faria
	   parecer que a cola não entra na conta; o que acontece é que a gente não
	   tem o número, e dizer isso é a resposta honesta (seção 10 do contrato). */
	$html .= '<li><span class="cdm-f1-rotulo">Gramas de cola</span><span class="cdm-f1-valor cdm-f1-vazio">a gente ainda não publica'
		. ' <span class="cdm-f1-nota">(o fabricante do silicone declara rendimento por cordão, não por área, e o consumo por área da cimentcola a gente não conseguiu)</span></span></li>';
	$html .= '</ul>';

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_recusa_html' ) ) {
/**
 * Por que a ferramenta não calcula o rejunte que não é pó. É a correção do
 * bloco 3c na tela, e ela é do ESTADO FÍSICO do produto — não do fabricante,
 * não da marca.
 */
function cdm_f1_recusa_html( $e ) {
	if ( 'cimenticio' === $e['rejunte'] ) {
		return '';
	}
	$qual = ( 'acrilico' === $e['rejunte'] )
		? 'O acrílico é monocomponente, vem pronto no pote e é vendido por quilo de pote'
		: 'O epóxi é bicomponente, vem em duas partes que se misturam na hora';

	$html  = '<div class="cdm-f1-secao">';
	$html .= '<h2>Por que a gente não calcula esse rejunte</h2>';
	$html .= '<p class="cdm-f1-faixa">A fórmula de consumo que a gente usa vem do fabricante, e o coeficiente dela sai de um '
		. 'exemplo publicado por ele com rejunte cimentício em pó. ' . esc_html( $qual ) . ' — é outro produto, com outro jeito de render. '
		. 'Aplicar a ele o coeficiente do pó seria fazer conta sem olhar o que está dentro do pote, e um número errado aqui vira rejunte comprado a mais ou a menos.</p>';
	$html .= '<p>O que falta é pouco e é nomeado: o coeficiente de consumo desse tipo, publicado pelo fabricante. Enquanto ele não vier, '
		. 'a conta de pastilhas aí em cima continua valendo igual — ela não depende do rejunte que você escolher.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_nomes_de' ) ) {
/** Ids → nomes comerciais, pela mesma fonte que a F2 usa. Sem segundo mapa. */
function cdm_f1_nomes_de( $ids ) {
	$nomes = array();
	foreach ( (array) $ids as $id ) {
		$nomes[] = cdm_f2_nome( $id );
	}

	return $nomes;
}
}

if ( ! function_exists( 'cdm_f1_faixas_de' ) ) {
/**
 * Ids → "Nome (de X a Y mm)", para a recusa por folga dizer QUAL é a faixa que
 * o fabricante publica em vez de só afirmar que a folga não cabe. Faixa que o
 * banco não tem sai dita, nunca inventada.
 */
function cdm_f1_faixas_de( $ids, $por_id ) {
	$linhas = array();
	foreach ( (array) $ids as $id ) {
		$p = cdm_f2_perfil_rejunte( $por_id[ $id ] );
		if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
			$linhas[] = esc_html( cdm_f2_nome( $id ) ) . ' (não conseguimos a faixa de folga dele)';
		} else {
			$linhas[] = esc_html( cdm_f2_nome( $id ) ) . ' (o fabricante publica de '
				. cdm_casca_num( $p['junta_min'] ) . ' a ' . cdm_casca_num( $p['junta_max'] ) . ' mm)';
		}
	}

	return $linhas;
}
}

if ( ! function_exists( 'cdm_f1_vitrine_html' ) ) {
/**
 * O bloco de compra (seções 6 e 7 do contrato), ANTES da prova de procedência.
 *
 * Quem decide qual rejunte serve é a régua da F2 — a mesma, chamada daqui.
 * Filtrada pelo tipo que a pessoa escolheu, porque a pergunta desta página é
 * "quanto comprar", e comprar é do tipo que ela vai usar.
 */
function cdm_f1_vitrine_html( $e ) {
	if ( ! function_exists( 'cdm_f2_celula_rejunte' ) || ! function_exists( 'cdm_f2_cartao_html' ) ) {
		return '<div class="cdm-f1-secao cdm-f1-vitrine-rejunte"><h2>Onde comprar o rejunte</h2>'
			. '<p class="cdm-f1-faixa">A lista de produtos está fora do ar neste momento. A conta acima continua de pé — ela não depende dela.</p></div>';
	}

	$celula = cdm_f2_celula_rejunte( $e['junta'], $e['ambiente'] );
	$banco  = cdm_f1_banco_rejuntes();
	$tipos  = cdm_f1_tipos_de_rejunte();

	$por_id = array();
	foreach ( $banco['materiais'] as $m ) {
		if ( ! empty( $m['id'] ) ) {
			$por_id[ $m['id'] ] = $m;
		}
	}

	$do_tipo    = array();
	$outro_tipo = array();
	foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
		if ( ! isset( $por_id[ $id ] ) ) {
			continue;
		}
		if ( $e['rejunte'] === ( isset( $por_id[ $id ]['tipo'] ) ? $por_id[ $id ]['tipo'] : '' ) ) {
			$do_tipo[] = $id;
		} else {
			$outro_tipo[] = $id;
		}
	}

	/* POR QUE A LISTA VOLTOU VAZIA — a causa, lida da própria célula, e não uma
	   hipótese oferecida ao leitor. Ver o comentário do bloco abaixo.

	   Os grupos são do TIPO ESCOLHIDO: produto de outro tipo cair pela folga não
	   diz nada sobre a pergunta que esta pessoa fez. E são TRÊS, não dois: a
	   célula da F2 junta num balde só quem tem faixa publicada e não cobre a
	   folga e quem NÃO TEM FAIXA NENHUMA — para ela tanto faz, os dois estão
	   fora. Para esta frase não tanto faz: dizer "não cobre 4 mm" de um produto
	   cuja faixa a gente nunca conseguiu é afirmar sobre uma declaração que não
	   foi lida, que é exatamente o que esta ilha existe para não fazer. */
	$fora_folga  = array();
	$sem_faixa   = array();
	$fora_lugar  = array();
	foreach ( $celula['eliminados_por_faixa_de_junta'] as $id ) {
		if ( ! isset( $por_id[ $id ] ) || $e['rejunte'] !== ( isset( $por_id[ $id ]['tipo'] ) ? $por_id[ $id ]['tipo'] : '' ) ) {
			continue;
		}
		$p = cdm_f2_perfil_rejunte( $por_id[ $id ] );
		if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
			$sem_faixa[] = $id;
		} else {
			$fora_folga[] = $id;
		}
	}
	foreach ( $celula['eliminados_por_ambiente'] as $id ) {
		if ( isset( $por_id[ $id ] ) && $e['rejunte'] === ( isset( $por_id[ $id ]['tipo'] ) ? $por_id[ $id ]['tipo'] : '' ) ) {
			$fora_lugar[] = $id;
		}
	}

	/* O nome do tipo em texto corrido. `strtok( $rotulo, ' —' )` cortava no
	   PRIMEIRO espaço e devolvia só "Rejunte", então a frase saía dizendo
	   "nenhum rejunte do nosso banco" — uma afirmação sobre o banco INTEIRO
	   onde cabia só uma sobre o tipo escolhido. Foi metade do defeito que a
	   Sentinela mediu em 12/09/2026. */
	$nome_tipo = mb_strtolower( trim( strtok( $tipos[ $e['rejunte'] ], '—' ) ), 'UTF-8' );

	$lugar = ( function_exists( 'cdm_f2_rotulos' ) && isset( $e['ambiente'] ) )
		? cdm_f2_rotulos()['ambiente_curto'][ $e['ambiente'] ]
		: '';
	$mm    = '<strong>' . cdm_casca_num( $e['junta'] ) . ' mm</strong>';

	$html  = '<div class="cdm-f1-secao cdm-f1-vitrine-rejunte">';
	$html .= '<h2>Qual rejunte cabe nessa folga</h2>';

	if ( $do_tipo ) {
		$html .= '<p>Com ' . $mm . ' de folga, e para peça ' . esc_html( $lugar )
			. ', estes são os ' . esc_html( $nome_tipo ) . ' que o fabricante declara:</p>';
		$html .= '<ul class="cdm-f1-vitrine">';
		foreach ( $do_tipo as $id ) {
			$p      = cdm_f2_perfil_rejunte( $por_id[ $id ] );
			$motivo = 'Cobre folga de ' . cdm_casca_num( $p['junta_min'] ) . ' a ' . cdm_casca_num( $p['junta_max'] ) . ' mm.';
			$html  .= cdm_f2_cartao_html( $id, $motivo );
		}
		$html .= '</ul>';
	} elseif ( ! $fora_folga && ! $sem_faixa && ! $fora_lugar ) {
		/* Nem eliminado, nem elegível: o tipo não existe no banco. */
		$html .= '<p class="cdm-f1-faixa">Ainda não temos nenhum ' . esc_html( $nome_tipo ) . ' no nosso banco — nenhuma marca, '
			. 'nenhuma faixa de folga. Quando tiver, o cartão aparece aqui com a medida que fez o produto entrar na lista.</p>';
	} else {
		/* A RECUSA NOMEIA A CAUSA CERTA — despacho da Sentinela de 12/09/2026,
		   item 1. A frase antiga culpava SEMPRE a folga ("Nenhum … declara folga
		   de N mm"), inclusive quando a folga cabia perfeitamente e quem excluía
		   era o lugar; e como a linha de "outro tipo" vinha logo depois dizendo
		   "dentro dessa folga", a página chegava a negar e afirmar o mesmo fato
		   em duas frases seguidas. A célula da F2 já separava os dois motivos —
		   o que faltava era esta tela ler a separação em vez de adivinhar.
		   O molde é o da F2, que faz isto certo desde o primeiro dia. */
		$html .= '<p class="cdm-f1-faixa">Nenhum ' . esc_html( $nome_tipo ) . ' do nosso banco serve para essa peça '
			. ( $lugar ? esc_html( $lugar ) : '' ) . ', com ' . $mm . ' de folga.</p>';
	}

	/* ------------------------------------------------------------------
	 * A PRESTAÇÃO DE CONTAS DO TIPO ESCOLHIDO, e ela sai SEMPRE — inclusive
	 * quando a lista de cima tem produto.
	 *
	 * Este pedaço nasceu de um buraco no próprio conserto deste despacho,
	 * achado pelo portão antes do desembarque: a primeira versão só explicava
	 * os excluídos quando a lista voltava vazia, então em 27 estados a página
	 * listava dois cimentícios e não dizia uma palavra sobre o terceiro. É o
	 * mesmo defeito do item 2 do despacho, um andar acima — produto do banco
	 * que some da tela sem que nada diga por quê. A regra vale para as duas
	 * ferramentas: todo rejunte é nomeado uma vez, ou na lista, ou aqui.
	 *
	 * Uma frase por CAUSA, cada uma nomeando quem caiu por ela. Quando a causa
	 * é o lugar, a página diz isso com todas as letras — quem cai pelo lugar
	 * passou pela folga antes (a régua da F2 testa a folga primeiro), então "a
	 * folga cabe" não é suposição, é o que a ordem das travas garante.
	 * ------------------------------------------------------------------ */
	if ( $fora_lugar ) {
		$html .= '<p class="cdm-f1-faixa">O que exclui ' . esc_html( cdm_f2_lista_humana( cdm_f1_nomes_de( $fora_lugar ) ) )
			. ' é o LUGAR, não a folga: ' . $mm . ' cabe na faixa que o fabricante publica para '
			. ( 1 === count( $fora_lugar ) ? 'ele' : 'eles' ) . ', e o que ele não declara é peça '
			. esc_html( $lugar ) . '.</p>';
	}
	if ( $fora_folga ) {
		$html .= '<p class="cdm-f1-faixa">Fora por causa da folga de ' . $mm . ': '
			. implode( '; ', cdm_f1_faixas_de( $fora_folga, $por_id ) ) . '.</p>';
	}
	if ( $sem_faixa ) {
		$html .= '<p class="cdm-f1-faixa">De ' . esc_html( cdm_f2_lista_humana( cdm_f1_nomes_de( $sem_faixa ) ) )
			. ' a gente não conseguiu a faixa de folga que o fabricante publica, então '
			. ( 1 === count( $sem_faixa ) ? 'ele não entra' : 'eles não entram' ) . ' em recomendação nenhuma — '
			. 'nem para dizer que cabe, nem para dizer que não cabe.</p>';
	}

	if ( $outro_tipo ) {
		/* A célula da F2 já filtrou pela folga E pelo lugar, então dizer só
		   "dentro dessa folga" dizia menos do que a página sabe — e era a metade
		   que produzia a contradição. */
		$html .= '<p class="cdm-f1-nota-lista">De outro tipo, e que servem nessa folga e nesse lugar: '
			. esc_html( cdm_f2_lista_humana( cdm_f1_nomes_de( $outro_tipo ) ) )
			. '. Eles servem para a peça — o que a gente não tem é o número de consumo deles.</p>';
	}

	$html .= '<p class="cdm-f1-aviso">Alguns links desta página são de afiliado: se você comprar por eles, a gente pode receber uma comissão, '
		. 'sem custo nenhum para você. Isso não muda a ordem da lista — quem decide é a declaração do fabricante.</p>';
	$html .= '<p>Para escolher entre eles pelo lugar onde a peça vai ficar, e para saber a cola, veja '
		. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'qual cola usar no mosaico, e qual rejunte' ) . '.</p>';
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6b. A VITRINE DE PASTILHA — e o eixo dela é a GEOMETRIA, não a matriz da cola
 *
 * Até a 1.1.0 este bloco era uma frase só: "ainda não temos as pastilhas no
 * nosso banco". Ela nasceu verdadeira em 11/09/2026 e ficou falsa em 12/09,
 * quando o bloco 3d gravou dez itens, e mais falsa em 13/09, quando entraram os
 * outros três — com a option publicada e lida pela casca o tempo inteiro. É o
 * mesmo defeito que a F2 tinha com o `url_busca`: dado no banco, tela sem
 * leitor. Aqui custava mais, porque a pergunta desta página É "quantas
 * pastilhas comprar" e ela respondia sem ter o que vender.
 *
 * O QUE DECIDE UMA PASTILHA NÃO É O QUE DECIDE UMA COLA, e esta é a primeira
 * coisa que o código declara. A cola se escolhe por base × ambiente; o rejunte,
 * pela largura da folga. A pastilha entrou no banco pela GEOMETRIA — o próprio
 * arquivo diz isso, e diz por quê: o fabricante não nomeia substrato nem
 * ambiente na ficha dela. Varrer a pastilha com a régua da cola produziria a
 * mesma afirmação sem sentido que a Robometria e esta ilha já pagaram
 * ("eliminado por silêncio" num produto que nunca foi candidato a colar nada).
 * Então aqui a elegibilidade tem três travas, NESTA ORDEM, e a ordem é o que
 * faz cada frase de recusa poder ser verdadeira:
 *
 *   1. O LADO. Tem de ser exatamente o lado que a pessoa escolheu (ou digitou,
 *      no caquinho irregular). Quem não tem esse lado sai por aqui, e a frase
 *      dele fala de lado — nunca de fonte, nunca de formato.
 *   2. O FORMATO. O seletor oferece pastilha QUADRADA ("2 × 2 cm"), e o banco
 *      tem um strip retangular de 1,2 cm. Mesmo lado não é mesma peça: quem cai
 *      aqui já passou pelo lado, então "o lado é o mesmo" não é suposição.
 *   3. A FONTE. Recomendação primária exige nível <= 3 (escada de fontes do
 *      esquema). O único item de 1,5 cm do banco é sustentado por distribuidor,
 *      e é por isso que 1,5 sai com ZERO elegível tendo um item — a causa é a
 *      fonte, não o tamanho, e a tela diz qual das duas é.
 *
 * PRESTAÇÃO DE CONTAS (seção 7 do contrato): as quatro listas são disjuntas e
 * somam o banco inteiro, contado do arquivo. Todo item aparece uma vez — no
 * cartão que o recomenda, ou numa linha que diz por que ele não está. Nenhum
 * número desta tela é digitado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_nivel_da_pastilha' ) ) {
/**
 * O nível da melhor fonte do item. A escada de fontes é regra do Arquipélago e
 * a implementação dela nesta ilha é `cdm_f2_nivel()` — uma segunda cópia aqui
 * seria a régua duplicada que a Robometria pagou comparando duas metades que
 * erram juntas. Quem chama isto já conferiu que a F2 está de pé.
 */
function cdm_f1_nivel_da_pastilha( $m ) {
	return cdm_f2_nivel( $m );
}
}

if ( ! function_exists( 'cdm_f1_pastilhas_classificadas' ) ) {
/**
 * As quatro listas disjuntas, para um lado pedido em milímetros.
 *
 * `recomendadas` vai para a vitrine; as outras três vão para a prosa, cada uma
 * com a sua causa. A soma das quatro é sempre o banco inteiro.
 */
function cdm_f1_pastilhas_classificadas( $lado_mm ) {
	$itens = cdm_f1_banco_pastilhas()['materiais'];
	$teto  = cdm_f2_nivel_maximo();

	$saida = array(
		'recomendadas'   => array(),
		'fonte_fraca'    => array(),
		'outro_formato'  => array(),
		'outro_lado'     => array(),
		'total'          => count( $itens ),
		'teto_de_fonte'  => $teto,
	);

	foreach ( $itens as $m ) {
		$g    = isset( $m['geometria'] ) ? $m['geometria'] : array();
		$lado = isset( $g['lado_anunciado_cm'] ) ? (float) $g['lado_anunciado_cm'] * 10 : null;

		if ( null === $lado || abs( $lado - (float) $lado_mm ) > 0.001 ) {
			$saida['outro_lado'][] = $m;
			continue;
		}
		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) ) {
			$saida['outro_formato'][] = $m;
			continue;
		}
		if ( cdm_f1_nivel_da_pastilha( $m ) > $teto ) {
			$saida['fonte_fraca'][] = $m;
			continue;
		}
		$saida['recomendadas'][] = $m;
	}

	return $saida;
}
}

if ( ! function_exists( 'cdm_f1_placas_para' ) ) {
/**
 * Quantas placas a peça pede — e ela é conta de ÁREA, de propósito.
 *
 * Converter "N pastilhas" em "M placas" exigiria quantas pastilhas vêm na
 * placa, e NENHUM fabricante brasileiro declara esse campo: nos treze itens ele
 * é null com o motivo escrito. Área, sim, se converte sem supor nada — a placa
 * cobre o seu próprio tamanho, seja qual for o arranjo das peças dentro dela, e
 * recortar placa para caber é o normal do trabalho. A sobra que a pessoa
 * escolheu entra aqui também, e o arredondamento é para cima pelo mesmo motivo
 * da contagem de peças: lote novo muda de cor.
 */
function cdm_f1_placas_para( $m, $area_cm2, $sobra_pct ) {
	$g = isset( $m['geometria'] ) ? $m['geometria'] : array();
	$a = isset( $g['placa_lado_a_cm'] ) ? (float) $g['placa_lado_a_cm'] : 0;
	$b = isset( $g['placa_lado_b_cm'] ) ? (float) $g['placa_lado_b_cm'] : 0;

	if ( $a <= 0 || $b <= 0 || null === $area_cm2 || $area_cm2 <= 0 ) {
		return null;
	}

	return (int) ceil( ( $area_cm2 * ( 1 + $sobra_pct / 100 ) ) / ( $a * $b ) );
}
}

if ( ! function_exists( 'cdm_f1_pastilha_codigo' ) ) {
/** O nome curto do item na prosa: o código do fabricante, que é como a loja o chama. */
function cdm_f1_pastilha_codigo( $m ) {
	if ( ! empty( $m['codigo_fabricante'] ) ) {
		return (string) $m['codigo_fabricante'];
	}

	return isset( $m['nome_comercial'] ) ? (string) $m['nome_comercial'] : '';
}
}

if ( ! function_exists( 'cdm_f1_pastilha_codigos' ) ) {
function cdm_f1_pastilha_codigos( $itens ) {
	$fora = array();
	foreach ( $itens as $m ) {
		$fora[] = cdm_f1_pastilha_codigo( $m );
	}

	return $fora;
}
}

if ( ! function_exists( 'cdm_f1_lado_de' ) ) {
/** O lado anunciado do item, em centímetros, como a tela escreve. */
function cdm_f1_lado_de( $m ) {
	$lado = isset( $m['geometria']['lado_anunciado_cm'] ) ? (float) $m['geometria']['lado_anunciado_cm'] : null;

	return null === $lado ? '' : number_format_i18n( $lado, ( (float) $lado == (int) $lado ) ? 0 : 1 );
}
}

if ( ! function_exists( 'cdm_f1_pastilha_fonte' ) ) {
/** A melhor fonte do item — a que sustenta a medida, para o link discreto. */
function cdm_f1_pastilha_fonte( $m ) {
	$melhor = null;
	foreach ( (array) ( isset( $m['fontes'] ) ? $m['fontes'] : array() ) as $f ) {
		if ( ! isset( $f['nivel'] ) ) {
			continue;
		}
		if ( null === $melhor || (int) $f['nivel'] < (int) $melhor['nivel'] ) {
			$melhor = $f;
		}
	}

	return $melhor;
}
}

if ( ! function_exists( 'cdm_f1_cartao_pastilha_html' ) ) {
/**
 * O cartão de pastilha. Mesmo molde do cartão da F2 — as mesmas classes, o
 * mesmo bloco de compra e a mesma ordem: a declaração que fez o item entrar, o
 * bloco de compra, e só depois a procedência discreta.
 *
 * A ESCADA DA SEÇÃO 25 NÃO É REESCRITA AQUI: quem serve os três estados é
 * `cdm_f2_compra_html()`, que nasceu em 13/09/2026 dizendo, no próprio
 * comentário, que a vitrine de pastilha da F1 a chamaria em vez de copiá-la.
 * Hoje os treze itens caem no terceiro estado — sem ficha e sem piso —, e isso
 * é defeito declarado da 19.1, não estado de espera: o cartão reserva o lugar e
 * a página conta quantos estão assim.
 */
function cdm_f1_cartao_pastilha_html( $m, $area_cm2, $sobra_pct ) {
	$g     = isset( $m['geometria'] ) ? $m['geometria'] : array();
	$fonte = cdm_f1_pastilha_fonte( $m );
	$html  = '<li class="cdm-f2-cartao">';

	if ( ! empty( $m['imagem']['url'] ) ) {
		$html .= '<img class="cdm-f2-foto" src="' . esc_url( $m['imagem']['url'] ) . '"'
			. ' width="' . (int) $m['imagem']['largura'] . '" height="' . (int) $m['imagem']['altura'] . '"'
			. ' loading="lazy" alt="' . esc_attr( $m['imagem']['alt'] ) . '">';
	} else {
		$html .= '<span class="cdm-f2-sem-foto" aria-hidden="true"></span>';
	}

	$html .= '<span class="cdm-f2-marca">' . esc_html( isset( $m['marca'] ) ? $m['marca'] : '' ) . '</span>';
	$html .= '<h3>' . esc_html( isset( $m['nome_comercial'] ) ? $m['nome_comercial'] : '' ) . '</h3>';

	/* A DECLARAÇÃO QUE FEZ O ITEM ENTRAR (seção 6): lado, placa e espessura,
	   como o fabricante publica. Nada aqui é derivado. */
	$motivo = 'Caquinho de ' . esc_html( cdm_f1_lado_de( $m ) ) . ' cm em placa de '
		. esc_html( number_format_i18n( (float) $g['placa_lado_a_cm'], 1 ) ) . ' × '
		. esc_html( number_format_i18n( (float) $g['placa_lado_b_cm'], 1 ) ) . ' cm';
	if ( ! empty( $g['espessura_mm'] ) ) {
		$motivo .= ', com ' . cdm_casca_num( $g['espessura_mm'] ) . ' mm de espessura';
	}
	$motivo .= '.';

	$placas = cdm_f1_placas_para( $m, $area_cm2, $sobra_pct );
	if ( null !== $placas ) {
		$motivo .= ' A sua peça pede <strong>' . cdm_casca_num( $placas ) . ' placa'
			. ( $placas > 1 ? 's' : '' ) . '</strong> dessa, com a sobra já dentro.';
	}
	$html .= '<p class="cdm-f2-motivo">' . $motivo . '</p>';

	$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );

	if ( $fonte && ! empty( $fonte['url'] ) ) {
		$html .= '<span class="cdm-f2-fonte"><a href="' . esc_url( $fonte['url'] ) . '"'
			. ' rel="nofollow noopener" target="_blank">fonte</a>'
			. ' · lido em ' . esc_html( cdm_casca_data_br( $fonte['coletado_em'] ) ) . '</span>';
	}

	$html .= '</li>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_vitrine_pastilha_html' ) ) {
/**
 * A vitrine de pastilha, filtrada pelo lado que a pessoa pediu.
 *
 * A CAUSA QUE O CÓDIGO SEPARA, O TEXTO SEPARA (seção 7): uma frase por lista,
 * cada uma nomeando quem caiu por ela. E cada frase só pode ser dita porque a
 * ordem das travas garante o que ela afirma — quem cai pelo formato já passou
 * pelo lado, quem cai pela fonte já passou pelos dois.
 *
 * A PORTA DO CAQUINHO IRREGULAR é a resposta desta tela para a pendência que o
 * banco abriu em 13/09/2026: seis dos treze itens têm lado que o seletor não
 * lista (3 cm, 2,3 cm, 1,2 cm). Esconder isso seria publicar um catálogo menor
 * do que o banco; inventar opção nova no seletor seria prometer cobertura que a
 * seção 14.3 não tem. O campo do caquinho irregular já aceita qualquer lado de
 * 0,3 a 10 cm, e é por ele que esses itens se alcançam — a página diz isso com
 * os lados nomeados, em vez de deixar a pessoa descobrir.
 */
function cdm_f1_vitrine_pastilha_html( $e ) {
	/* O TÍTULO NÃO TEM CONECTOR, e isso é decisão da 1.3.0: ele já foi "E onde
	   comprar a pastilha", e aquele "E" só era verdade enquanto este bloco vinha
	   em segundo lugar. Título é a frase que um modelo de linguagem cita sozinho
	   (seção 5), então ele não pode depender da posição em que foi servido. */
	$html = '<div class="cdm-f1-secao cdm-f1-vitrine-pastilha"><h2>Onde comprar a pastilha</h2>';

	/* Sem a F2 de pé não há escada de compra nem escada de fontes, e esta página
	   não escreve uma segunda. Mesma saída do bloco do rejunte. */
	if ( ! function_exists( 'cdm_f2_compra_html' ) || ! function_exists( 'cdm_f2_nivel' )
		|| ! function_exists( 'cdm_f2_nivel_maximo' ) || ! function_exists( 'cdm_f2_lista_humana' ) ) {
		return $html . '<p class="cdm-f1-faixa">A lista de pastilhas está fora do ar neste momento. '
			. 'A conta acima continua de pé — ela não depende dela.</p></div>';
	}

	$c     = cdm_f1_pastilhas_classificadas( $e['lado_mm'] );
	$lado  = cdm_f1_lado_em_texto( $e['lado_mm'] );
	$area  = cdm_f1_area_cm2( $e['forma'], $e['medidas'] );

	if ( 0 === $c['total'] ) {
		return $html . '<p class="cdm-f1-faixa">O nosso banco de pastilhas não chegou ao site nesta hora. '
			. 'A conta acima continua valendo — leve o número de pastilhas e o tamanho para qualquer loja.</p></div>';
	}

	if ( $c['recomendadas'] ) {
		$quantas = count( $c['recomendadas'] );
		$html   .= 1 === $quantas
			? '<p>Para caquinho de <strong>' . esc_html( $lado ) . ' cm</strong>, o nosso banco tem <strong>uma</strong> pastilha, '
				. 'com a medida publicada pelo próprio fabricante:</p>'
			: '<p>Para caquinho de <strong>' . esc_html( $lado ) . ' cm</strong>, estas são as <strong>'
				. cdm_casca_num( $quantas ) . '</strong> pastilhas do nosso banco — cada uma com a medida '
				. 'publicada pelo próprio fabricante:</p>';
		$html .= '<ul class="cdm-f1-vitrine">';
		foreach ( $c['recomendadas'] as $m ) {
			$html .= cdm_f1_cartao_pastilha_html( $m, $area, $e['sobra'] );
		}
		$html .= '</ul>';
	} elseif ( $c['fonte_fraca'] || $c['outro_formato'] ) {
		/* Tem item desse lado, e o que o exclui está nomeado nas linhas abaixo —
		   por isso esta frase NÃO diz qual é a causa: dizer aqui seria repetir, e
		   escolher uma das duas seria afirmar sobre a outra. */
		$html .= '<p class="cdm-f1-faixa">Nenhuma pastilha de ' . esc_html( $lado )
			. ' cm entra na nossa recomendação hoje, e não é por falta de produto desse lado — é pelo que está escrito aqui embaixo.</p>';
	} else {
		$por_lado = cdm_f1_lados_com_elegivel();
		$html    .= '<p class="cdm-f1-faixa">A gente não tem nenhuma pastilha de ' . esc_html( $lado )
			. ' cm no banco — nem uma marca.';
		if ( $por_lado ) {
			$html .= ' O que a gente tem, por lado: ' . esc_html( cdm_f2_lista_humana( $por_lado ) ) . '.';
		}
		$html .= '</p>';
		if ( 10 === (int) $e['lado_mm'] ) {
			/* SÓ QUANDO A CONTAGEM DESSE LADO É ZERO, e é por isso que a frase pode
			   ser dita: ela afirma sobre o mercado, e no dia em que um 1 cm de
			   fabricante entrar no banco esta linha deixa de sair sozinha. */
			$html .= '<p class="cdm-f1-faixa">E isso não é descuido de coleta: 1 cm é o tamanho mais usado do mosaico '
				. 'e não aparece em catálogo de fabricante nenhum. Quem vende é armarinho e marketplace, a peso ou por peça solta — '
				. 'e a peso a gente não consegue dizer quantas peças vêm, porque ninguém publica o peso de uma pastilha.</p>';
		}
	}

	/* --- as três listas que não foram para a vitrine, uma frase por causa --- */

	if ( $c['outro_formato'] ) {
		$html .= '<p class="cdm-f1-faixa">Do mesmo lado de ' . esc_html( $lado ) . ' cm, mas de outro formato: '
			. esc_html( cdm_f2_lista_humana( cdm_f1_pastilha_codigos( $c['outro_formato'] ) ) )
			. '. ' . ( 1 === count( $c['outro_formato'] ) ? 'Ele não é' : 'Eles não são' )
			. ' quadradinho — a conta aqui em cima é de peça quadrada, então '
			. ( 1 === count( $c['outro_formato'] ) ? 'ele fica' : 'eles ficam' ) . ' fora da lista.</p>';
	}

	if ( $c['fonte_fraca'] ) {
		$html .= '<p class="cdm-f1-faixa">O lado de ' . esc_html( $lado ) . ' cm é o mesmo em '
			. esc_html( cdm_f2_lista_humana( cdm_f1_pastilha_codigos( $c['fonte_fraca'] ) ) )
			. ', e o que ' . ( 1 === count( $c['fonte_fraca'] ) ? 'exclui ele' : 'exclui eles' )
			. ' é quem publica a medida: um distribuidor, não o fabricante. A gente só recomenda pelo que o fabricante publica.</p>';
	}

	if ( $c['outro_lado'] ) {
		$html .= '<p class="cdm-f1-nota-lista">De outro lado, e no nosso banco: '
			. esc_html( cdm_f2_lista_humana( cdm_f1_grupos_por_lado( $c['outro_lado'] ) ) ) . '.</p>';

		/* O LADO EM QUE A PESSOA JÁ ESTÁ SAI DESTA LISTA: ela chegou aqui, o item
		   daquele lado foi recusado por formato ou por fonte, e mandá-la de volta
		   pelo caquinho irregular seria mandá-la ao lugar onde ela está. */
		$fora = cdm_f1_lados_fora_do_seletor( $e['lado_mm'] );
		if ( $fora ) {
			$html .= '<p class="cdm-f1-nota-lista">Os tamanhos aí em cima são cinco, e o nosso banco tem lado que eles não listam: '
				. esc_html( cdm_f2_lista_humana( $fora ) ) . '. Para comprar '
				. ( 1 === count( $fora ) ? 'esse' : 'esses' ) . ', escolha <em>caquinho irregular</em> no formulário e digite o lado — '
				. 'a conta é a mesma, e a lista daqui passa a mostrar o que serve.</p>';
		}
	}

	/* O QUE A PLACA NÃO DIZ, dito uma vez e não em treze cartões. */
	$html .= '<p class="cdm-f1-nota-lista">Uma coisa que nenhuma dessas placas diz: quantas pastilhas vêm nela. '
		. 'A gente procurou nos ' . cdm_casca_num( $c['total'] ) . ' produtos do nosso banco e o fabricante não publica — '
		. 'por isso o cartão fala em placa, e não em peça. '
		. 'A tabela da placa, mais abaixo, mostra como você descobre isso com a embalagem na mão.</p>';

	$html .= '<p class="cdm-f1-aviso">Alguns links desta página são de afiliado: se você comprar por eles, a gente pode receber uma comissão, '
		. 'sem custo nenhum para você. Isso não muda a ordem da lista — quem decide é a declaração do fabricante.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_lados_com_elegivel' ) ) {
/**
 * "3 de 2 cm e 4 de 2,5 cm" — os lados que TÊM item elegível, contados do
 * banco. Existe para a frase do lado vazio poder apontar para onde há produto
 * sem que ninguém digite um número.
 */
function cdm_f1_lados_com_elegivel() {
	$teto  = cdm_f2_nivel_maximo();
	$conta = array();
	foreach ( cdm_f1_banco_pastilhas()['materiais'] as $m ) {
		$g = isset( $m['geometria'] ) ? $m['geometria'] : array();
		if ( 'quadrada' !== ( isset( $g['formato'] ) ? $g['formato'] : '' ) || empty( $g['lado_anunciado_cm'] ) ) {
			continue;
		}
		if ( cdm_f1_nivel_da_pastilha( $m ) > $teto ) {
			continue;
		}
		$chave = (string) (float) $g['lado_anunciado_cm'];
		$conta[ $chave ] = isset( $conta[ $chave ] ) ? $conta[ $chave ] + 1 : 1;
	}
	ksort( $conta, SORT_NUMERIC );

	$fora = array();
	foreach ( $conta as $lado => $n ) {
		$fora[] = number_format_i18n( $n ) . ' de ' . cdm_f1_lado_em_texto( (float) $lado * 10 ) . ' cm';
	}

	return $fora;
}
}

if ( ! function_exists( 'cdm_f1_grupos_por_lado' ) ) {
/** "4 de 2,5 cm (K2501, K2502, MIX2510 e 102)" — cada item nomeado uma vez. */
function cdm_f1_grupos_por_lado( $itens ) {
	$grupos = array();
	foreach ( $itens as $m ) {
		$lado = isset( $m['geometria']['lado_anunciado_cm'] ) ? (string) (float) $m['geometria']['lado_anunciado_cm'] : '0';
		$grupos[ $lado ][] = cdm_f1_pastilha_codigo( $m );
	}
	ksort( $grupos, SORT_NUMERIC );

	$fora = array();
	foreach ( $grupos as $lado => $codigos ) {
		$fora[] = number_format_i18n( count( $codigos ) ) . ' de ' . cdm_f1_lado_em_texto( (float) $lado * 10 )
			. ' cm (' . cdm_f2_lista_humana( $codigos ) . ')';
	}

	return $fora;
}
}

if ( ! function_exists( 'cdm_f1_lados_fora_do_seletor' ) ) {
/**
 * Os lados do banco que o seletor não oferece — medidos nos DOIS lados, o banco
 * e a própria lista da ferramenta. Digitar essa lista seria repetir o defeito
 * que o `validar-pastilhas.py` achou em 13/09/2026 do outro lado da cerca: a
 * régua tinha quatro tamanhos escritos à mão e a ferramenta servia cinco.
 */
function cdm_f1_lados_fora_do_seletor( $exceto_mm = null ) {
	$do_seletor = array();
	foreach ( cdm_f1_pastilhas_disponiveis() as $t ) {
		if ( null !== $t['lado_mm'] ) {
			$do_seletor[ (string) (float) $t['lado_mm'] ] = true;
		}
	}

	$fora = array();
	foreach ( cdm_f1_banco_pastilhas()['materiais'] as $m ) {
		$lado = isset( $m['geometria']['lado_anunciado_cm'] ) ? (float) $m['geometria']['lado_anunciado_cm'] * 10 : null;
		if ( null === $lado || isset( $do_seletor[ (string) $lado ] ) ) {
			continue;
		}
		if ( null !== $exceto_mm && abs( $lado - (float) $exceto_mm ) < 0.001 ) {
			continue;
		}
		$fora[ (string) $lado ] = cdm_f1_lado_em_texto( $lado ) . ' cm';
	}
	ksort( $fora, SORT_NUMERIC );

	return array_values( $fora );
}
}

/* ---------------------------------------------------------------------------
 * 7. As tabelas pré-renderizadas — o que um modelo de linguagem lê
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_tabela_pecas_html' ) ) {
function cdm_f1_tabela_pecas_html() {
	$html  = '<div class="cdm-f1-secao"><h2>Doze peças já calculadas, sem preencher nada</h2>';
	$html .= '<p>Se a sua peça for parecida com alguma destas, o número já está aqui. Todas com 10% de sobra, '
		. 'e a espessura da pastilha está escrita em cada linha porque ela muda o rejunte.</p>';
	$html .= '<div class="cdm-f1-rolagem"><table class="cdm-f1-tabela"><thead><tr>'
		. '<th scope="col">Peça</th><th scope="col">Área</th><th scope="col">Pastilha · folga · espessura</th>'
		. '<th scope="col">Pastilhas</th><th scope="col">Rejunte cimentício</th></tr></thead><tbody>';

	foreach ( cdm_f1_pecas_tipicas() as $p ) {
		$r = cdm_f1_calcular( $p['forma'], $p['medidas'], $p['lado_mm'], $p['junta_mm'], $p['espessura_mm'], 10, 'cimenticio' );

		$html .= '<tr>';
		$html .= '<td>' . esc_html( $p['nome'] ) . '</td>';
		$html .= '<td>' . cdm_casca_num( round( $r['area_cm2'] ) ) . ' cm²</td>';
		$html .= '<td>' . esc_html( cdm_f1_lado_em_texto( $p['lado_mm'] ) ) . ' cm · '
			. cdm_casca_num( $p['junta_mm'] ) . ' mm · ' . cdm_casca_num( $p['espessura_mm'] ) . ' mm</td>';
		$html .= '<td>' . cdm_casca_num( $r['pastilhas'] ) . '</td>';
		$html .= '<td>' . ( null !== $r['gramas'] ? cdm_f1_gramas_na_tela( $r['gramas'] ) . ' g' : '<span class="cdm-f1-vazio">sem número hoje</span>' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_tabela_pastilhas_html' ) ) {
/**
 * O BANCO DE PASTILHAS INTEIRO, PRÉ-RENDERIZADO — a metade que um modelo de
 * linguagem lê sem preencher formulário (seção 5 do contrato, item 1) e a
 * segunda superfície da prestação de contas (seção 7).
 *
 * Ela existe por uma razão que a vitrine sozinha não resolve: o estado-âncora
 * desta página é caquinho de 1 cm, e 1 cm tem ZERO item no banco. Sem esta
 * tabela, a página indexada — a única sem parâmetro, a que o Google e as IAs
 * leem — não citaria um único produto do nosso catálogo de pastilha. A vitrine
 * responde a quem escolheu um lado; a tabela responde a quem só chegou.
 *
 * Cada item aparece em EXATAMENTE uma linha, e o total da legenda é contado do
 * arquivo. A última coluna é a cobertura da seção 14.3 publicada em vez de
 * medida só na bancada: ela diz, item por item, se o seletor desta ferramenta
 * oferece aquele lado — e é assim que a pessoa descobre que o mercado tem
 * tamanho que o formulário não lista.
 */
function cdm_f1_tabela_pastilhas_html() {
	$itens = cdm_f1_banco_pastilhas()['materiais'];
	if ( ! $itens ) {
		return '';
	}

	$do_seletor = array();
	foreach ( cdm_f1_pastilhas_disponiveis() as $t ) {
		if ( null !== $t['lado_mm'] ) {
			$do_seletor[ (string) (float) $t['lado_mm'] ] = true;
		}
	}

	$marcas = array();
	foreach ( $itens as $m ) {
		if ( ! empty( $m['marca'] ) ) {
			$marcas[ $m['marca'] ] = true;
		}
	}

	$html  = '<div class="cdm-f1-secao"><h2>As pastilhas que a gente já conferiu</h2>';
	$html .= '<p>São <strong>' . cdm_casca_num( count( $itens ) ) . '</strong> produtos de '
		. cdm_casca_num( count( $marcas ) ) . ' marcas, com a medida que o próprio fabricante publica. '
		. 'A última coluna diz se o formulário aí em cima oferece aquele lado: quando não oferece, '
		. 'o caminho é o caquinho irregular, digitando o lado.</p>';
	$html .= '<div class="cdm-f1-rolagem"><table class="cdm-f1-tabela cdm-f1-tabela-pastilhas"><thead><tr>'
		. '<th scope="col">Produto</th><th scope="col">Caquinho</th><th scope="col">Placa</th>'
		. '<th scope="col">Espessura</th><th scope="col">A caixa</th><th scope="col">Está no formulário?</th>'
		. '</tr></thead><tbody>';

	foreach ( $itens as $m ) {
		$g     = isset( $m['geometria'] ) ? $m['geometria'] : array();
		$props = isset( $m['propriedades'] ) ? $m['propriedades'] : array();
		$lado  = isset( $g['lado_anunciado_cm'] ) ? (float) $g['lado_anunciado_cm'] * 10 : null;
		$tem   = ( null !== $lado && isset( $do_seletor[ (string) $lado ] ) );

		$caixa = '<span class="cdm-f1-vazio">não publicada</span>';
		if ( isset( $props['placas_por_caixa']['valor'] ) && isset( $props['m2_por_caixa']['valor'] ) ) {
			$caixa = cdm_casca_num( $props['placas_por_caixa']['valor'] ) . ' placas · '
				. esc_html( number_format_i18n( $props['m2_por_caixa']['valor'], 2 ) ) . ' m²';
		}

		$html .= '<tr>';
		$html .= '<td>' . esc_html( isset( $m['marca'] ) ? $m['marca'] : '' ) . ' '
			. esc_html( cdm_f1_pastilha_codigo( $m ) ) . '</td>';
		$html .= '<td>' . esc_html( cdm_f1_lado_de( $m ) ) . ' cm'
			. ( 'quadrada' === ( isset( $g['formato'] ) ? $g['formato'] : '' ) ? '' : ' (não é quadrado)' ) . '</td>';
		$html .= '<td>' . esc_html( number_format_i18n( (float) $g['placa_lado_a_cm'], 1 ) ) . ' × '
			. esc_html( number_format_i18n( (float) $g['placa_lado_b_cm'], 1 ) ) . ' cm</td>';
		$html .= '<td>' . cdm_casca_num( $g['espessura_mm'] ) . ' mm</td>';
		$html .= '<td>' . $caixa . '</td>';
		$html .= '<td>' . ( $tem ? 'sim' : '<span class="cdm-f1-vazio">não</span>' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_tabela_consumo_html' ) ) {
/**
 * O consumo por metro quadrado, lado a lado com o que a primeira página do
 * Google publica. É a tabela que sustenta a tese da página, e é a única em que
 * a comparação aparece com os dois números juntos.
 *
 * As duas linhas de obra saem da MESMA fórmula, com as medidas do azulejo e do
 * piso: não são número de outra fonte, são a nossa conta aplicada ao caso que a
 * SERP responde. É isso que torna a comparação honesta.
 */
function cdm_f1_tabela_consumo_html() {
	$cr = cdm_f1_coeficiente();
	if ( null === $cr['valor'] ) {
		return '';
	}

	$linhas = array(
		array( 'Pastilha de 1 × 1 cm, folga de 2 mm', 10, 4, 2, 'peça de artesanato' ),
		array( 'Pastilha de 1 × 1 cm, folga de 3 mm', 10, 4, 3, 'peça de artesanato' ),
		array( 'Pastilha de 2 × 2 cm, folga de 2 mm', 20, 4, 2, 'peça de artesanato' ),
		array( 'Pastilha de 2 × 2 cm, folga de 3 mm', 20, 4, 3, 'peça de artesanato' ),
		array( 'Pastilha de 2,5 × 2,5 cm, folga de 3 mm', 25, 5, 3, 'peça de artesanato' ),
		array( 'Azulejo de 10 × 10 cm, folga de 3 mm', 100, 7, 3, 'obra' ),
		array( 'Piso de 20 × 20 cm, folga de 10 mm', 200, 8, 10, 'obra' ),
	);

	$html  = '<div class="cdm-f1-secao"><h2>Por que a conta que circula por aí não serve para a sua peça</h2>';
	$html .= '<p>Todas as linhas saem da mesma fórmula, com o mesmo coeficiente. O que muda é o tamanho do caquinho — '
		. 'e é ele que manda no consumo, muito mais do que a marca do rejunte.</p>';
	$html .= '<div class="cdm-f1-rolagem"><table class="cdm-f1-tabela"><thead><tr>'
		. '<th scope="col">Tamanho da peça colada</th><th scope="col">Espessura</th><th scope="col">Rejunte por m²</th>'
		. '<th scope="col">Onde essa conta aparece</th></tr></thead><tbody>';

	foreach ( $linhas as $l ) {
		list( $rotulo, $lado_mm, $esp_mm, $junta_mm, $onde ) = $l;
		$consumo = cdm_f1_consumo_kg_m2( $lado_mm, $esp_mm, $junta_mm, $cr['valor'] );
		$html   .= '<tr' . ( 'obra' === $onde ? ' class="cdm-f1-linha-obra"' : '' ) . '>';
		$html   .= '<td>' . esc_html( $rotulo ) . '</td>';
		$html   .= '<td>' . cdm_casca_num( $esp_mm ) . ' mm</td>';
		$html   .= '<td>' . esc_html( number_format_i18n( round( $consumo, 2 ), 2 ) ) . ' kg/m²</td>';
		$html   .= '<td>' . ( 'obra' === $onde ? 'é a conta de obra, a que a busca devolve' : 'a sua peça' ) . '</td>';
		$html   .= '</tr>';
	}

	$html .= '</tbody></table></div>';

	/* A RAZAO SAI DAS PROPRIAS LINHAS DA TABELA, nunca digitada ao lado dela. */
	$c_pastilha = cdm_f1_consumo_kg_m2( 10, 4, 2, $cr['valor'] );
	$c_azulejo  = cdm_f1_consumo_kg_m2( 100, 7, 3, $cr['valor'] );
	$c_piso     = cdm_f1_consumo_kg_m2( 200, 8, 10, $cr['valor'] );
	$html      .= '<p>A pastilha de 1 cm com folga de 2 mm come <strong>'
		. esc_html( number_format_i18n( round( $c_pastilha / $c_azulejo, 1 ), 1 ) ) . ' vezes</strong> o rejunte do azulejo de 10 cm '
		. 'e <strong>' . esc_html( number_format_i18n( round( $c_pastilha / $c_piso, 1 ), 1 ) ) . ' vezes</strong> o do piso de 20 cm, '
		. 'que são as duas linhas de obra desta mesma tabela. Quem compra pelo número da obra leva rejunte de menos e descobre no meio da peça.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_placa_html' ) ) {
/**
 * A conversão entre unidades de venda — achado do bloco 1, e aritmética pura.
 *
 * A placa não diz o tamanho da pastilha; ela diz quantas pastilhas tem. O passo
 * é o lado da placa dividido pela raiz de quantas pastilhas ela traz, e é aí
 * que a comparação de preço entre duas placas engana: 225 numa placa de 30 cm é
 * pastilha de 2 cm, não de 1 cm.
 */
function cdm_f1_placa_html() {
	$exemplos = array( 900, 400, 225, 144 );

	$html  = '<div class="cdm-f1-secao"><h2>A placa engana na hora de comparar preço</h2>';
	$html .= '<p>Pastilha vendida em placa costuma vir colada numa tela, e a etiqueta diz o tamanho da placa e o número de peças — '
		. 'não o tamanho de cada peça. Para achar o tamanho real, divida o lado da placa pela raiz quadrada do número de pastilhas. '
		. 'Numa placa de 30 cm:</p>';
	$html .= '<div class="cdm-f1-rolagem"><table class="cdm-f1-tabela"><thead><tr>'
		. '<th scope="col">Pastilhas na placa de 30 cm</th><th scope="col">Passo de uma à outra</th>'
		. '<th scope="col">Ou seja</th></tr></thead><tbody>';

	foreach ( $exemplos as $n ) {
		$passo_cm = 30 / sqrt( $n );
		$html    .= '<tr><td>' . cdm_casca_num( $n ) . '</td>';
		$html    .= '<td>' . esc_html( number_format_i18n( round( $passo_cm, 2 ), 2 ) ) . ' cm</td>';
		$html    .= '<td>pastilha de cerca de ' . esc_html( number_format_i18n( round( $passo_cm, 1 ), 1 ) ) . ' cm, com a folga já incluída</td></tr>';
	}

	$html .= '</tbody></table></div>';
	$html .= '<p>Por isso duas placas do mesmo preço podem ser negócios bem diferentes: a de 900 peças traz pastilha de 1 cm, '
		. 'a de 225 traz pastilha de 2 cm, e a sua peça come um número bem diferente de cada uma.</p>';
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. O formulário
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_select_html' ) ) {
function cdm_f1_select_html( $nome, $rotulo, $opcoes, $escolhido, $ajuda = '' ) {
	$id    = 'cdm-f1-' . $nome;
	$html  = '<p class="cdm-f1-campo"><label for="' . esc_attr( $id ) . '">' . esc_html( $rotulo ) . '</label>';
	if ( '' !== $ajuda ) {
		$html .= '<span class="cdm-f1-ajuda">' . esc_html( $ajuda ) . '</span>';
	}
	$html .= '<select id="' . esc_attr( $id ) . '" name="' . esc_attr( $nome ) . '">';
	foreach ( $opcoes as $valor => $texto ) {
		$html .= '<option value="' . esc_attr( $valor ) . '"' . ( (string) $valor === (string) $escolhido ? ' selected' : '' )
			. '>' . esc_html( $texto ) . '</option>';
	}
	$html .= '</select></p>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_numero_html' ) ) {
function cdm_f1_numero_html( $nome, $rotulo, $valor, $min, $max, $passo = '0.5', $ajuda = '' ) {
	$id    = 'cdm-f1-' . $nome;
	$html  = '<p class="cdm-f1-campo"><label for="' . esc_attr( $id ) . '">' . esc_html( $rotulo ) . '</label>';
	if ( '' !== $ajuda ) {
		$html .= '<span class="cdm-f1-ajuda">' . esc_html( $ajuda ) . '</span>';
	}
	$html .= '<input type="number" inputmode="decimal" id="' . esc_attr( $id ) . '" name="' . esc_attr( $nome ) . '"'
		. ' value="' . esc_attr( ( (float) $valor == (int) $valor ) ? (int) $valor : $valor ) . '"'
		. ' min="' . esc_attr( $min ) . '" max="' . esc_attr( $max ) . '" step="' . esc_attr( $passo ) . '"></p>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_form_html' ) ) {
function cdm_f1_form_html( $e ) {
	$formas = cdm_f1_formas();
	$tam    = cdm_f1_pastilhas_disponiveis();

	$rotulos_forma = array();
	foreach ( $formas as $chave => $f ) {
		$rotulos_forma[ $chave ] = $f['rotulo'];
	}
	$rotulos_tam = array();
	foreach ( $tam as $chave => $t ) {
		$rotulos_tam[ $chave ] = $t['rotulo'];
	}
	$juntas = array();
	for ( $i = 1; $i <= 12; $i++ ) {
		$juntas[ $i ] = $i . ' mm' . ( 2 === $i ? ' (o mais comum)' : '' );
	}

	/* GET para a própria página, e sem tocar na variável de servidor: o playbook
	   (fase 4b) manda usar add_query_arg( array() ), porque o ModSecurity desta
	   hospedagem mata a gravação em silêncio quando o snippet lê aquela caixa. */
	$html  = '<form class="cdm-f1-form" method="get" action="' . esc_url( add_query_arg( array() ) ) . '#resposta">';
	$html .= cdm_f1_select_html( 'forma', 'Que peça você vai fazer?', $rotulos_forma, $e['forma'] );

	$html .= '<div class="cdm-f1-medidas">';
	foreach ( $formas[ $e['forma'] ]['campos'] as $campo => $rotulo ) {
		$html .= cdm_f1_numero_html( $campo, $rotulo, $e['medidas'][ $campo ], '0.5', '500' );
	}
	$html .= '</div>';

	$html .= cdm_f1_select_html( 'pastilha', 'Qual o tamanho do caquinho?', $rotulos_tam, $e['tamanho'] );
	if ( 'irregular' === $e['tamanho'] ) {
		$html .= cdm_f1_numero_html( 'ladoeq', 'Lado médio do seu caquinho, em cm', $e['lado_eq'], '0.3', '10', '0.1',
			'Meça uns cinco caquinhos e use a média. Não precisa ser exato: erro de 1 mm no lado muda pouco o total.' );
	}
	$html .= cdm_f1_numero_html( 'esp', 'Espessura da pastilha, em mm', $e['espessura'], '1', '20', '0.5',
		'Meça a sua com uma régua. 4 mm é o que costuma vir, mas isso muda de fabricante para fabricante, e a espessura mexe direto no rejunte.' );
	$html .= cdm_f1_select_html( 'junta', 'Quanto espaço entre uma pastilha e outra?', $juntas, $e['junta'],
		'Entre 2 e 3 mm é o comum, mas quem decide é a sua peça.' );
	$html .= cdm_f1_select_html( 'sobra', 'Quanto de sobra você quer?', cdm_f1_sobras(), $e['sobra'],
		'Lote novo de pastilha muda de cor. Faltar dez peças no fim é pior que sobrar dez.' );
	$html .= cdm_f1_select_html( 'rejunte', 'Qual rejunte você vai usar?', cdm_f1_tipos_de_rejunte(), $e['rejunte'] );

	if ( '' !== $e['ambiente'] && function_exists( 'cdm_f2_rotulos' ) ) {
		$rot   = cdm_f2_rotulos();
		$html .= cdm_f1_select_html( 'onde', 'Onde a peça vai ficar?', $rot['ambiente'], $e['ambiente'],
			'Isto não muda a conta. Serve para a gente só mostrar rejunte que o fabricante declara para esse lugar.' );
	}

	$html .= '<p class="cdm-f1-acao"><button type="submit" class="cdm-f1-botao">Ver a conta da minha peça</button></p>';
	$html .= '</form>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 9. A página
 * ------------------------------------------------------------------------- */

add_shortcode( 'cdm_f1', function () {
	$e = cdm_f1_entrada();

	$html  = '<div class="cdm-bloco cdm-f1">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Diga o tamanho da sua peça e o do caquinho. A gente mostra quantas pastilhas comprar, '
		. 'já com sobra, e quanto rejunte levar — na conta da pastilha pequena, não na do azulejo de obra.</p>';
	$html .= '<p>É a diferença que faz você voltar à loja no meio da peça: a conta que circula por aí foi feita com azulejo grande, '
		. 'e caquinho pequeno come muito mais rejunte que isso. Quanto mais, a tabela aqui embaixo mostra com os dois números lado a lado.</p>';
	$html .= '<p>Esta página faz parte do nosso guia de ' . cdm_casca_link_html( 'materiais', 'Materiais' ) . '.</p>';
	$html .= '</div>';

	$html .= cdm_f1_form_html( $e );
	$html .= cdm_f1_resposta_html( $e );
	$html .= cdm_f1_recusa_html( $e );
	/* A ORDEM DOS DOIS BLOCOS DE COMPRA É DECISÃO, e o cabeçalho deste arquivo
	   (versão 1.3.0) diz por quê: a pastilha primeiro, porque é dela que falam o
	   título, o H1 e a primeira frase da resposta. Os dois continuam ANTES da
	   camada de prova, que é o que a seção 7 do contrato manda. */
	$html .= cdm_f1_vitrine_pastilha_html( $e );
	$html .= cdm_f1_vitrine_html( $e );
	$html .= cdm_f1_tabela_pecas_html();
	$html .= cdm_f1_tabela_pastilhas_html();
	$html .= cdm_f1_tabela_consumo_html();
	$html .= cdm_f1_placa_html();

	/* PERGUNTAS QUE AS PESSOAS REALMENTE FAZEM — as mesmas do FAQPage. O texto
	   da tela e o do schema saem da MESMA função, senão os dois envelhecem
	   separados e o schema passa a prometer o que a página não diz. */
	$html .= '<div class="cdm-f1-secao"><h2>Perguntas que sempre chegam</h2><dl class="cdm-f1-faq">';
	foreach ( cdm_f1_perguntas() as $p ) {
		$html .= '<dt>' . esc_html( $p['pergunta'] ) . '</dt><dd>' . esc_html( $p['resposta'] ) . '</dd>';
	}
	$html .= '</dl></div>';

	/* A CAMADA DE PROVA da página (15.2): de onde vem cada número, o documento e
	   o dia em que foi lido, e o que a gente ainda não tem. */
	$html .= cdm_f1_prova_html();

	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'cdm_f1_prova_html' ) ) {
function cdm_f1_prova_html() {
	$cr = cdm_f1_coeficiente();

	$html  = '<div class="cdm-prova">';
	$html .= '<h2>Como sabemos</h2>';
	$html .= '<p>A área e a contagem de pastilhas são conta nossa, de geometria: a superfície da peça dividida pelo passo, '
		. 'que é o lado do caquinho mais a folga. Não há fonte externa nisso, e não precisa haver — dá para conferir com régua e calculadora.</p>';

	if ( null !== $cr['valor'] ) {
		$html .= '<p>O consumo de rejunte sai da fórmula publicada pela ' . esc_html( $cr['fabricante'] )
			. ', <code>((A + B) × E × L × CR) / (A × B)</code>, com os lados e a espessura da pastilha e a largura da folga em milímetros. '
			. 'O coeficiente CR que usamos é <strong>' . esc_html( number_format_i18n( $cr['valor'], 2 ) ) . '</strong>, '
			. 'lido do registro do ' . esc_html( $cr['produto'] ) . ' no nosso banco';
		if ( '' !== $cr['coletado_em'] ) {
			$html .= ' em ' . esc_html( cdm_casca_data_br( $cr['coletado_em'] ) );
		}
		$html .= '. Ele vem do exemplo que o próprio fabricante publica junto da fórmula — peça de 200 × 200 mm, 8 mm de espessura e '
			. 'folga de 10 mm dando 1,4 kg/m² —, e esse exemplo é de rejunte cimentício em pó. '
			. 'É por isso que a gente não estende esse número ao acrílico nem ao epóxi';
		if ( '' !== $cr['url'] ) {
			$html .= ' (<a href="' . esc_url( $cr['url'] ) . '" rel="nofollow noopener" target="_blank">fonte</a>)';
		}
		$html .= '.</p>';
	} else {
		$html .= '<p>O consumo de rejunte não está publicado nesta página hoje: ' . esc_html( $cr['motivo'] ) . '. '
			. 'A conta de pastilhas não depende dele e continua valendo.</p>';
	}

	/* A PROCEDÊNCIA DA PASTILHA, com os números CONTADOS do banco. A frase mais
	   importante desta seção é a última: ela diz o que a gente NÃO tem, e é a que
	   explica por que o cartão fala em placa e não em peça. */
	$pastilhas = cdm_f1_banco_pastilhas()['materiais'];
	if ( $pastilhas ) {
		$sem_peca = 0;
		foreach ( $pastilhas as $m ) {
			if ( ! isset( $m['geometria']['pastilhas_por_placa'] ) || null === $m['geometria']['pastilhas_por_placa'] ) {
				$sem_peca++;
			}
		}
		$html .= '<p>As medidas das pastilhas — lado, placa, espessura e o que vem na caixa — saem da página de produto de cada '
			. 'fabricante, lida por busca no domínio dele, e cada item do nosso banco guarda o endereço e o dia da leitura. '
			. 'São ' . cdm_casca_num( count( $pastilhas ) ) . ' produtos conferidos assim. '
			. 'Em ' . cdm_casca_num( $sem_peca ) . ' deles o fabricante não publica quantas pastilhas vêm na placa, '
			. 'e a gente não deduz esse número dividindo o lado da placa pelo lado do caquinho: a divisão não fecha em '
			. 'quase todos, e onde fecha só fecha com folga zero entre as peças — que é placa que não se rejunta.</p>';
	}

	$html .= '<p>Nenhum documento de fabricante foi aberto linha a linha daqui: a leitura foi feita no domínio de cada um, '
		. 'e cada item do nosso banco diz qual documento sustenta qual número. O método inteiro está em '
		. cdm_casca_link_html( 'materiais/como-sabemos', 'Como sabemos' ) . '.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f1_resposta_da_obra' ) ) {
/**
 * A comparação com a conta de obra, derivada — os dois números saem da mesma
 * fórmula e do mesmo coeficiente que a tabela usa, e somem juntos quando o
 * coeficiente não chega.
 */
function cdm_f1_resposta_da_obra() {
	$cr = cdm_f1_coeficiente();
	if ( null === $cr['valor'] ) {
		return 'Porque as outras respondem à pergunta da obra, feita com azulejo grande e folga larga, e o tamanho do caquinho é o que manda no consumo. '
			. 'Os números dessa comparação a gente não publica hoje: ' . $cr['motivo'] . '.';
	}

	$piso     = cdm_f1_consumo_kg_m2( 200, 8, 10, $cr['valor'] );
	$pastilha = cdm_f1_consumo_kg_m2( 10, 4, 2, $cr['valor'] );

	return 'Porque as outras respondem à pergunta da obra. A mesma fórmula, aplicada a piso de 20 cm com folga de 10 mm, dá '
		. number_format_i18n( round( $piso, 1 ), 1 ) . ' kg por metro quadrado; aplicada a pastilha de 1 cm com folga de 2 mm, dá '
		. number_format_i18n( round( $pastilha, 1 ), 1 ) . '. O tamanho do caquinho é o que manda no consumo.';
}
}

if ( ! function_exists( 'cdm_f1_resposta_do_vaso' ) ) {
/**
 * A resposta do vaso de 15 × 20, DERIVADA da mesma conta que a ferramenta faz.
 *
 * Podia ser uma frase digitada — e foi, no primeiro rascunho. Frase digitada é
 * exatamente o jeito discreto de a página se contradizer: no dia em que o
 * coeficiente do banco mudar, ou em que ele não chegar, o FAQ continuaria
 * afirmando 264 g enquanto a ferramenta logo acima diz outra coisa. Quando não
 * há número, esta resposta diz que não há.
 */
function cdm_f1_resposta_do_vaso() {
	$r = cdm_f1_calcular( 'cilindro', array( 'd' => 15, 'h' => 20 ), 10, 2, 4, 10, 'cimenticio' );

	$area = number_format_i18n( round( $r['area_cm2'] ) );

	if ( null === $r['gramas'] ) {
		return 'A superfície é de ' . $area . ' cm² e leva ' . number_format_i18n( $r['pastilhas'] )
			. ' pastilhas de 1 cm com 10% de sobra. O número de rejunte a gente não publica hoje: '
			. $r['cr']['motivo'] . '.';
	}

	return 'Cerca de ' . number_format_i18n( round( $r['gramas'] ) ) . ' g de rejunte cimentício, com pastilha de 1 cm de lado e '
		. '4 mm de espessura e folga de 2 mm. A superfície é de ' . $area . ' cm², e o consumo dá '
		. number_format_i18n( round( $r['consumo'], 2 ), 2 ) . ' kg por metro quadrado.';
}
}

if ( ! function_exists( 'cdm_f1_perguntas' ) ) {
/**
 * Uma fonte só para a tela e para o FAQPage. Toda resposta aqui é sustentada
 * pela conta desta página ou por declaração que já está no banco — nenhuma
 * pergunta existe só para encher schema, que é o que faz FAQPage virar spam.
 */
function cdm_f1_perguntas() {
	return array(
		array(
			'pergunta' => 'Quantas pastilhas de 1 cm cabem em 1 m²?',
			'resposta' => 'Com folga de 2 mm, cabem ' . number_format_i18n( floor( cdm_f1_por_m2( 10, 2 ) ) )
				. ' — cada pastilha ocupa 1,2 cm de parede, não 1 cm. Com folga de 3 mm caem para '
				. number_format_i18n( floor( cdm_f1_por_m2( 10, 3 ) ) )
				. '. É por isso que a folga entra na conta antes do tamanho da peça.',
		),
		array(
			'pergunta' => 'Quanto rejunte leva um vaso de 15 por 20 cm?',
			'resposta' => cdm_f1_resposta_do_vaso(),
		),
		array(
			'pergunta' => 'Por que o número de rejunte daqui é tão maior que o das outras páginas?',
			'resposta' => cdm_f1_resposta_da_obra(),
		),
		array(
			'pergunta' => 'Quanta sobra de pastilha eu devo comprar?',
			'resposta' => '10% é o que a gente usa por padrão, e o arredondamento é sempre para cima. O motivo não é o preço: lote novo de pastilha muda de cor, e faltar dez peças no fim da peça é pior que sobrar dez.',
		),
		array(
			'pergunta' => 'A conta serve para rejunte epóxi ou acrílico?',
			'resposta' => 'A de pastilhas serve para qualquer um. A de gramas, não: o coeficiente que a gente tem vem de um exemplo publicado com rejunte cimentício em pó, e o acrílico é pronto uso em pote e o epóxi é bicomponente. Enquanto o fabricante não publicar o coeficiente desses dois, a gente diz que não calcula em vez de chutar.',
		),
		array(
			'pergunta' => 'A placa de 30 cm com 225 pastilhas é de 1 cm?',
			'resposta' => 'Não. O passo é 30 dividido pela raiz de 225, ou seja 2 cm — é pastilha de 2 cm com a folga incluída. Quem compara o preço dessa placa com o de uma de 900 peças está comparando pastilha de 2 cm com pastilha de 1 cm.',
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 10. Cabeça da página: description, robôs e JSON-LD
 *
 * O canonical NÃO sai daqui, e a ausência é deliberada: `rel_canonical()` do
 * núcleo já imprime o permalink limpo em toda página singular, e esta ilha não
 * tem plugin de SEO que o remova. O que falta ao núcleo é o `noindex` do estado
 * com parâmetro, e é só isso que sai daqui.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f1_e_minha_pagina' ) ) {
function cdm_f1_e_minha_pagina() {
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_F1_SLUG === cdm_casca_slug_atual();
}
}

add_action( 'wp_head', function () {
	if ( ! cdm_f1_e_minha_pagina() ) {
		return;
	}
	$e = cdm_f1_entrada();

	echo '<meta name="description" content="'
		. esc_attr( 'Quantas pastilhas e quanto rejunte a sua peça de mosaico precisa: vaso, tampo, quadro, esfera ou moldura, com a conta da pastilha pequena e não a do azulejo de obra.' )
		. '">' . "\n";
}, 4 );

/* O ESTADO COM PARAMETRO SAI DO INDICE, e quem IMPRIME a etiqueta e a casca.
   Ate 25/09/2026 este arquivo imprimia a propria `<meta name="robots">` aqui, e
   o resultado servido eram DUAS etiquetas — a do nucleo e esta. Agora a
   condicao e declarada e a casca junta tudo num vetor so (casca 1.13.0). */
add_filter( 'cdm_fora_do_indice', function ( $fora ) {
	if ( ! cdm_f1_e_minha_pagina() ) {
		return $fora;
	}
	$e = cdm_f1_entrada();

	return $fora || ! empty( $e['escolheu'] );
} );

add_action( 'wp_head', function () {
	if ( ! cdm_f1_e_minha_pagina() ) {
		return;
	}
	$limpa = home_url( '/' . CDM_F1_SLUG . '/' );

	$perguntas = array();
	foreach ( cdm_f1_perguntas() as $p ) {
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
				'@type'               => 'WebApplication',
				'@id'                 => $limpa . '#ferramenta',
				'name'                => CDM_F1_TITULO,
				'url'                 => $limpa,
				'applicationCategory' => 'UtilitiesApplication',
				'operatingSystem'     => 'Web',
				'inLanguage'          => 'pt-BR',
				'isAccessibleForFree' => true,
				'description'         => 'Calculadora de pastilhas e rejunte para mosaico artesanal: área por forma da peça, contagem de pastilhas com sobra e consumo de rejunte pela fórmula publicada pelo fabricante.',
				'publisher'           => array( '@id' => home_url( '/#organizacao' ) ),
			),
			array(
				'@type'      => 'FAQPage',
				'@id'        => $limpa . '#perguntas',
				'mainEntity' => $perguntas,
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-f1-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 11. Folha e script — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML, matando o script inteiro. Foi
 * o defeito que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 *
 * O script daqui NÃO calcula nada: ele só evita o recarregamento quando a
 * pessoa troca uma opção, e some por inteiro sem JavaScript.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_f1_e_minha_pagina() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-f1-css">
.cdm-f1-form{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);}
.cdm-f1-campo{margin:0 0 1rem;display:flex;flex-direction:column;gap:.3rem;}
.cdm-f1-campo:last-of-type{margin-bottom:0;}
.cdm-f1-campo label{font-family:var(--cdm-display);font-weight:600;font-size:1rem;}
.cdm-f1-ajuda{color:var(--cdm-legenda);font-size:.88rem;line-height:1.45;}
.cdm-f1-form select,.cdm-f1-form input[type=number]{font-family:var(--cdm-texto);font-size:1rem;padding:.6rem .7rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);color:var(--cdm-tinta);max-width:100%;}
.cdm-f1-form input[type=number]{font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;max-width:10rem;}
.cdm-f1-medidas{display:flex;flex-wrap:wrap;gap:1rem;margin:0 0 1rem;}
.cdm-f1-medidas .cdm-f1-campo{margin:0;flex:1 1 12rem;}
.cdm-f1-acao{margin:1.2rem 0 0;}
.cdm-f1-botao{display:inline-block;background:var(--cdm-coral);color:#FFFFFF;border:0;border-radius:2px;padding:.7rem 1.2rem;font-family:var(--cdm-display);font-weight:600;font-size:1rem;cursor:pointer;text-decoration:none;}
.cdm-f1-botao:hover{background:var(--cdm-vinho);color:#FFFFFF;text-decoration:none;}
.cdm-f1-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-f1-frase{font-size:1.15rem;line-height:1.5;margin:0;}
.cdm-f1-numeros{list-style:none;margin:1.1rem 0 0;padding:0;display:flex;flex-direction:column;gap:.7rem;}
.cdm-f1-numeros li{display:flex;flex-wrap:wrap;gap:.2rem 1rem;align-items:baseline;border-top:1px solid var(--cdm-traco);padding-top:.6rem;}
.cdm-f1-rotulo{font-family:var(--cdm-display);font-weight:600;flex:0 0 14rem;}
.cdm-f1-valor{font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;}
.cdm-f1-nota{font-family:var(--cdm-texto);font-size:.88rem;color:var(--cdm-legenda);}
.cdm-f1-nota-lista{font-size:.95rem;color:var(--cdm-legenda);}
.cdm-f1-secao{margin:2rem 0;}
.cdm-f1-secao h2{font-size:1.25rem;margin:0 0 .6rem;}
.cdm-f1-vitrine{display:flex;gap:1rem;list-style:none;margin:1rem 0 0;padding:0 0 .6rem;overflow-x:auto;scroll-snap-type:x mandatory;}
.cdm-f1-vitrine .cdm-f2-cartao{scroll-snap-align:start;}
.cdm-f1-aviso{font-size:.88rem;color:var(--cdm-legenda);margin:.8rem 0 0;}
.cdm-f1-rolagem{overflow-x:auto;}
.cdm-f1-tabela{width:100%;font-size:.93rem;}
.cdm-f1-tabela td:nth-child(2),.cdm-f1-tabela td:nth-child(4),.cdm-f1-tabela td:nth-child(5){font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.cdm-f1-linha-obra td{color:var(--cdm-legenda);}
.cdm-f1-vazio{color:var(--cdm-ambar);}
.cdm-f1-faixa{border-left:3px solid var(--cdm-ambar);padding-left:.9rem;}
.cdm-f1-faq{margin:.8rem 0 0;}
.cdm-f1-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .25rem;}
.cdm-f1-faq dd{margin:0;}
@media (max-width:600px){
.cdm-f1-frase{font-size:1.05rem;}
.cdm-f1-rotulo{flex:1 1 100%;}
.cdm-f1-medidas .cdm-f1-campo{flex:1 1 100%;}
}
</style>
<script id="cdm-f1-js">
/* Troca de opcao ja envia o formulario, para a pessoa nao precisar do botao.
   Nada aqui decide nada: quem responde e o servidor, e sem JavaScript a pagina
   continua inteira — o botao esta la, visivel, e faz o mesmo. */
(function(){
	var f = document.querySelector('.cdm-f1-form');
	if (!f) { return; }
	var selects = f.querySelectorAll('select');
	for (var i = 0; i < selects.length; i++) {
		selects[i].addEventListener('change', function(){ f.submit(); });
	}
	/* Chegou com resposta na tela: leva a pessoa ate ela. */
	if (window.location.search.indexOf('forma=') !== -1) {
		var alvo = document.getElementById('resposta');
		if (alvo) { if (!window.location.hash) { alvo.scrollIntoView({behavior:'smooth', block:'start'}); } }
	}
})();
</script>
HTML;
}, 20 );

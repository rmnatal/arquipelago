/**
 * Robometria R2 — Quantos Pa e quanto tempo o seu robô precisa
 * Versão: 1.0.0 (10/09/2026) — Bloco 4 da fila para a segunda ferramenta da
 * ilha, nascendo com as CINCO decisões de desenho que a R1 fixou em 10/09/2026
 * (PROMPT.md da ilha), e não com retrofit depois.
 *
 * A ferramenta de dimensionamento desta ilha: dada a metragem livre de piso, o
 * tipo de piso e o pelo do animal da casa, ela diz quantos pascal as fontes
 * brasileiras recomendam para aquela situação — com o nome de quem recomenda
 * cada número — e, escolhido um modelo de referência que declare cobertura por
 * carga, quantos ciclos a metragem exige.
 *
 * ---------------------------------------------------------------------------
 * AS CINCO DECISÕES HERDADAS DA R1, e como cada uma aparece aqui
 * ---------------------------------------------------------------------------
 *
 * 1. A RESPOSTA É SERVIDA PELO SERVIDOR. Formulário GET para a própria página,
 *    resposta montada em PHP. Sem JavaScript a ferramenta funciona por completo,
 *    e cada consulta tem a resposta inteira no HTML servido. Calculadora que só
 *    calcula no navegador mostra a um modelo de linguagem um formulário vazio
 *    (seção 5 do ARQUIPELAGO.md).
 *
 * 2. A REGRA MORA NA IMPLEMENTAÇÃO DE REFERÊNCIA, e este arquivo não a
 *    reescreve. Qual fonte se aplica a qual situação, qual limiar vale, quem
 *    passa na elegibilidade e em que ordem a lista sai — tudo isso vem apurado
 *    de ferramentas/cobertura-r2.py, por dados/r2-respostas.json. O que este
 *    arquivo faz é escrever a frase, em português acentuado, e a ARITMÉTICA
 *    declarada dos ciclos, que a entrada contínua da R2 obriga a fazer aqui.
 *    ferramentas/teste-r2.php percorre a GRADE inteira do gabarito — as 9
 *    situações e a metragem de 10 em 10 m² contra cada modelo de referência —
 *    e prova que as duas contas dão a mesma coisa. Grade não é amostra.
 *
 * 3. O CASO-ÂNCORA É ESCOLHIDO POR REGRA, nunca a dedo, e sai no HTML sem
 *    clique nenhum. A regra está na referência: a situação com mais
 *    publicadores distintos nomeando-a, e a menor metragem do corpus que o
 *    modelo de referência NÃO termina numa carga — para a resposta servida sem
 *    interação nenhuma ser justamente o número que ninguém publica.
 *
 * 4. CONSULTA NÃO VIRA URL INDEXÁVEL. Endereço com ?area=… sai com noindex e
 *    canônica para a página limpa. A faixa de 10 a 400 m² cruzada com 9
 *    situações e 5 modelos de referência daria milhares de URLs finas, e
 *    domínio novo tem orçamento de rastreamento minúsculo (seção 14.1).
 *
 * 5. A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA, e existe antes do
 *    link. O bloco nasce mesmo com afiliado.url vazio, reservando o lugar com
 *    "Link de loja em breve"; a procedência é link de texto "fonte", nunca um
 *    botão. As funções são as da casca (robometria_casca_porta_de_compra e
 *    irmãs): os pesos visuais são regra do Arquipélago, não estilo local.
 *
 * ---------------------------------------------------------------------------
 * O QUE ESTA PÁGINA PUBLICA QUE NINGUÉM PUBLICA — e o que ela se recusa a fazer
 * ---------------------------------------------------------------------------
 *
 * A especificação define TEMPO REAL ATÉ TERMINAR = ciclos × autonomia +
 * (ciclos − 1) × recarga. A varredura desta execução mediu que a fórmula precisa
 * de três números declarados pelo fabricante e que NENHUM modelo do banco tem os
 * três: quem declara cobertura por carga (Electrolux) não declara recarga; quem
 * declara recarga (Xiaomi S20, Positivo PRA2000) não declara cobertura. Então a
 * página publica os ciclos e o tempo de limpeza somado, e diz com todas as
 * letras que o total depende de um número que o fabricante não publica.
 *
 * E ela não converte minutos em metros quadrados. Das cinco marcas publicáveis
 * do banco, quatro não declaram área coberta em canal nenhum, e entre os dois
 * pares declarados — os dois da mesma marca — a taxa varia 23%. Uma taxa geral
 * não existe publicada; inventá-la é o que a seção 10 do contrato proíbe.
 *
 * Regras herdadas: sem "<?php" no topo (o Code Snippets põe); nenhuma
 * superglobal de servidor; nenhum <script> nem <style> dentro do retorno do
 * shortcode (o WordPress passa os filtros do the_content sobre ele e cada
 * E-comercial vira entidade — foi o que derrubou cinco calculadoras da
 * Aquametria em 08/09/2026); toda função de nível superior dentro de
 * if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'ROBOMETRIA_R2_VERSAO' ) ) {
	define( 'ROBOMETRIA_R2_VERSAO', '1.0.0' );
	define( 'ROBOMETRIA_R2_SLUG', 'quantos-pa-o-robo-aspirador-precisa' );
	define( 'ROBOMETRIA_R2_TITULO', 'Quantos Pa e quanto tempo o seu robô precisa' );
	define( 'ROBOMETRIA_R2_DADOS', 'robometria_dados_r2-respostas' );
}

/* ---------------------------------------------------------------------------
 * 1. Os dados: o que o Sync trouxe do repositório
 *
 * Quando a option não existe, a página NÃO finge: diz que o banco não chegou e
 * não mostra formulário. Ferramenta que devolve vazio parecendo funcionar é pior
 * do que uma que avisa.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_dados' ) ) {
function robometria_r2_dados() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}

	$d = get_option( ROBOMETRIA_R2_DADOS );
	$d = apply_filters( 'robometria_r2_dados', $d );

	if ( ! is_array( $d ) || empty( $d['situacoes'] ) || empty( $d['modelos'] ) ) {
		$cache = array();
		return $cache;
	}

	$cache = $d;
	return $cache;
}
}

/** Um modelo do banco pelo id, ou null. */
if ( ! function_exists( 'robometria_r2_modelo' ) ) {
function robometria_r2_modelo( $id ) {
	$d = robometria_r2_dados();
	foreach ( (array) $d['modelos'] as $m ) {
		if ( $m['id'] === $id ) {
			return $m;
		}
	}
	return null;
}
}

/** Uma situação pela chave "piso|pelo", ou null. */
if ( ! function_exists( 'robometria_r2_situacao' ) ) {
function robometria_r2_situacao( $chave ) {
	$d = robometria_r2_dados();
	return isset( $d['situacoes'][ $chave ] ) ? $d['situacoes'][ $chave ] : null;
}
}

if ( ! function_exists( 'robometria_r2_rotulo_do_piso' ) ) {
function robometria_r2_rotulo_do_piso( $id ) {
	$d = robometria_r2_dados();
	foreach ( (array) $d['entrada']['pisos'] as $p ) {
		if ( $p['id'] === $id ) {
			return $p['rotulo'];
		}
	}
	return $id;
}
}

if ( ! function_exists( 'robometria_r2_rotulo_do_pelo' ) ) {
function robometria_r2_rotulo_do_pelo( $id ) {
	$d = robometria_r2_dados();
	foreach ( (array) $d['entrada']['pelos'] as $p ) {
		if ( $p['id'] === $id ) {
			return $p['rotulo'];
		}
	}
	return $id;
}
}

/** 2026-09-09 -> 09/09/2026. A frase publicada leva data em português. */
if ( ! function_exists( 'robometria_r2_data' ) ) {
function robometria_r2_data( $iso ) {
	if ( function_exists( 'robometria_casca_data_br' ) ) {
		return robometria_casca_data_br( $iso );
	}
	$p = explode( '-', (string) $iso );
	return ( 3 === count( $p ) ) ? $p[2] . '/' . $p[1] . '/' . $p[0] : (string) $iso;
}
}

/** 1500 -> 1.500. O separador de milhar do texto publicado é o ponto. */
if ( ! function_exists( 'robometria_r2_n' ) ) {
function robometria_r2_n( $v ) {
	return number_format_i18n( (float) $v );
}
}

/**
 * "a Canaltech", "o Mundo Conectado".
 *
 * O artigo vem do dado, nunca de uma tabela escrita aqui: ele é derivado na
 * implementação de referência e viaja dentro de cada limiar. Se ficasse neste
 * arquivo, publicador novo sairia na tela com o artigo errado, em silêncio, no
 * meio de uma frase que a página afirma.
 */
if ( ! function_exists( 'robometria_r2_com_artigo' ) ) {
function robometria_r2_com_artigo( $limiar ) {
	$artigo = isset( $limiar['artigo'] ) ? $limiar['artigo'] : '';
	return trim( $artigo . ' ' . $limiar['publicador'] );
}
}

/** Como cada limiar é escrito na frase, respeitando o operador da fonte. */
if ( ! function_exists( 'robometria_r2_escrever_limiar' ) ) {
function robometria_r2_escrever_limiar( $l ) {
	if ( 'acima_de' === $l['comparacao'] ) {
		return 'acima de ' . robometria_r2_n( $l['valor'] ) . ' Pa';
	}
	if ( 'suficiente' === $l['comparacao'] ) {
		return 'até ' . robometria_r2_n( $l['valor'] ) . ' Pa já basta';
	}
	return robometria_r2_n( $l['valor'] ) . ' Pa';
}
}

/*
 * NÃO EXISTE AQUI UMA FUNÇÃO QUE DECIDA QUEM ATENDE AO LIMIAR, e a ausência é
 * deliberada — foi medida em 10/09/2026, quebrando o código de propósito.
 *
 * A primeira versão deste arquivo tinha uma `atende( $pa, $limiar )` que
 * respeitava o operador da fonte ("acima de 4.000 Pa" é exclusivo, e um modelo
 * de exatamente 4.000 Pa não está acima de 4.000). Ela nunca era chamada na
 * montagem da página: quem classifica é a implementação de referência, e a
 * lista chega pronta em dados/r2-respostas.json. Só o teste de bancada a
 * chamava — para conferir a lista. Ou seja, o teste conferia o dado com a régua
 * do próprio snippet: trocar o `>` por `>=` aqui fazia as duas metades errarem
 * juntas e o teste passar, com um modelo que a fonte citada não cobre em
 * primeiro lugar numa lista de recomendação. É exatamente a família de defeito
 * que a seção 7 do ARQUIPELAGO.md chama de GRAVE.
 *
 * Então a régua saiu daqui. Quem compara Pa com limiar é (1) a referência, que
 * classifica, e (2) ferramentas/teste-r2.php, que escreve a comparação por
 * conta própria, lendo o operador do dado — duas contas independentes, que é o
 * que faz uma medição. Função morta num snippet publicado não é neutra: ela
 * parece a regra, e um dia alguém a usa.
 */

/* ---------------------------------------------------------------------------
 * 2. A aritmética dos ciclos
 *
 * É a única conta que este arquivo faz, e ela é declarada:
 *
 *   CICLOS = teto( área ÷ cobertura declarada por carga )
 *   TEMPO REAL = ciclos × autonomia + (ciclos − 1) × recarga
 *
 * A segunda linha quase nunca fecha, e a página diz por quê em vez de preencher
 * o buraco com média de mercado. E a conta de mais de um ciclo só é publicada
 * quando o fabricante declara que o modelo retoma de onde parou: sem isso o robô
 * não termina a casa sozinho e o número perderia o sentido (honestidade 2 da
 * seção 2.2 da especificação).
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_tempo' ) ) {
function robometria_r2_tempo( $m, $area ) {
	$cob = isset( $m['cobertura_m2'] ) ? $m['cobertura_m2'] : null;
	if ( null === $cob || ! $cob ) {
		return null;
	}

	$n      = (int) ceil( (float) $area / (float) $cob );
	$aut    = isset( $m['autonomia_min'] ) ? $m['autonomia_min'] : null;
	$rec    = isset( $m['recarga_min'] ) ? $m['recarga_min'] : null;
	$retoma = isset( $m['retoma_apos_recarga'] ) ? $m['retoma_apos_recarga'] : null;

	$valido = ( 1 === $n ) || ( true === $retoma );

	$t = array(
		'ciclos'               => $n,
		'cobertura_m2'         => $cob,
		'autonomia_min'        => $aut,
		'recarga_min'          => $rec,
		'retoma_apos_recarga'  => $retoma,
		'multiciclo_valido'    => $valido,
		'tempo_de_limpeza_min' => ( $valido && null !== $aut ) ? ( $aut * $n ) : null,
		'tempo_total_min'      => null,
	);

	if ( $valido && null !== $aut ) {
		if ( 1 === $n ) {
			$t['tempo_total_min'] = $aut;
		} elseif ( null !== $rec ) {
			$t['tempo_total_min'] = $aut * $n + $rec * ( $n - 1 );
		}
	}

	return $t;
}
}

/** "1 recarga" / "2 recargas". Contador solto na frase denuncia texto de máquina. */
if ( ! function_exists( 'robometria_r2_plural' ) ) {
function robometria_r2_plural( $n, $singular, $plural ) {
	return robometria_r2_n( $n ) . ' ' . ( 1 === (int) $n ? $singular : $plural );
}
}

/* ---------------------------------------------------------------------------
 * 3. As frases
 *
 * Cada molde abaixo tem um gêmeo em ferramentas/cobertura-r2.py, e o teste de
 * bancada compara os dois ignorando acento. O molde é escolhido por MEDIÇÃO —
 * quantas fontes nomeiam a situação, quantos ciclos a metragem exige, se o
 * fabricante declara a retomada — e nunca por um "se" escrito na tela.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_frase_situacao' ) ) {
function robometria_r2_frase_situacao( $s ) {
	$piso   = robometria_r2_rotulo_do_piso( $s['piso'] );
	$pelo   = robometria_r2_rotulo_do_pelo( $s['pelo'] );
	$seguro = $s['limiar_seguro'];
	$minimo = $s['limiar_minimo'];

	if ( ! empty( $s['por_ponte'] ) ) {
		return sprintf(
			'Para %s %s, nenhuma das fontes brasileiras deste banco nomeia a situação. As duas vizinhas que elas nomeiam são %s (%s) e %s (%s), e esta página resolve para a de cima — errar para baixo aqui faz comprar um robô que não dá conta, e a compra inteira se perde.',
			$piso, $pelo,
			robometria_r2_escrever_limiar( $minimo ), robometria_r2_com_artigo( $minimo ),
			robometria_r2_escrever_limiar( $seguro ), robometria_r2_com_artigo( $seguro )
		);
	}

	if ( ! empty( $s['ha_divergencia'] ) ) {
		return sprintf(
			'Para %s %s, as fontes brasileiras divergem: %s recomenda %s e %s trata %s como o piso do consenso (verificado em %s). Esta página trabalha com o MAIOR limiar citado, porque errar para baixo custa a compra inteira.',
			$piso, $pelo,
			robometria_r2_com_artigo( $seguro ), robometria_r2_escrever_limiar( $seguro ),
			robometria_r2_com_artigo( $minimo ), robometria_r2_escrever_limiar( $minimo ),
			robometria_r2_data( $seguro['verificado_em'] )
		);
	}

	return sprintf(
		'Para %s %s, a única recomendação brasileira deste banco é a de %s: %s (verificado em %s).',
		$piso, $pelo,
		robometria_r2_com_artigo( $seguro ), robometria_r2_escrever_limiar( $seguro ),
		robometria_r2_data( $seguro['verificado_em'] )
	);
}
}

/**
 * O teto de utilidade — a constante que trabalha CONTRA o próprio nicho.
 *
 * É o que impede esta página de virar corrida de pascal. Uma ferramenta de
 * afiliado que só empurra o número para cima acaba recomendando sempre o mais
 * caro; aqui a própria fonte diz onde o número para de comprar melhora.
 */
if ( ! function_exists( 'robometria_r2_frase_teto' ) ) {
function robometria_r2_frase_teto( $s ) {
	if ( empty( $s['teto'] ) ) {
		return '';
	}
	$t = $s['teto'];
	return sprintf(
		'Acima de %s Pa, %s escreve que o resultado já fica próximo do limite prático percebido — daí para cima, mais sucção deixa de comprar melhora que alguém note (verificado em %s).',
		robometria_r2_n( $t['valor'] ), robometria_r2_com_artigo( $t ),
		robometria_r2_data( $t['verificado_em'] )
	);
}
}

/**
 * O aviso de classe de fonte, que é regra e não rodapé (seção 2.5 da
 * especificação): fabricante declara o Pa do aparelho; quanto Pa uma casa
 * precisa é opinião publicada, e opinião publicada tem autor. Confundir os dois
 * é vender editorial como dado técnico, que é o que as fazendas fazem.
 */
if ( ! function_exists( 'robometria_r2_frase_classe_de_fonte' ) ) {
function robometria_r2_frase_classe_de_fonte() {
	return 'Os limiares de Pa desta página NÃO são especificação de fabricante: são recomendação publicada por veículo brasileiro, e cada uma sai com o nome de quem a recomenda. O Pa de cada robô, esse sim, é declarado pelo fabricante.';
}
}

/**
 * O que a ferramenta NÃO sabe sobre um modelo, dito no próprio cartão.
 *
 * A condição (2) da elegibilidade — se a metragem passa da cobertura por carga,
 * o modelo precisa retomar depois de recarregar — é hoje INVERIFICÁVEL para todo
 * modelo que declara Pa, porque nenhum deles declara cobertura. Calar isso
 * deixaria a lista com cara de completa; dizer transforma a lacuna em
 * informação, que é o que separa esta página de um comparativo de anúncio.
 */
if ( ! function_exists( 'robometria_r2_ressalvas' ) ) {
function robometria_r2_ressalvas( $m, $s, $area ) {
	$r   = array();
	$cob = isset( $m['cobertura_m2'] ) ? $m['cobertura_m2'] : null;

	if ( null === $cob ) {
		$r[] = 'cobertura_nao_declarada';
	} elseif ( null !== $area && $area > $cob ) {
		$r[] = ( true === $m['retoma_apos_recarga'] )
			? 'passa_da_carga_mas_retoma'
			: 'passa_da_carga_e_nao_declara_retomada';
	}

	if ( ! empty( $s['teto'] ) && null !== $m['pa'] && $m['pa'] > $s['teto']['valor'] ) {
		$r[] = 'acima_do_teto_de_utilidade';
	}

	return $r;
}
}

/** A especificação que fez o produto entrar (seção 6 do ARQUIPELAGO.md). */
if ( ! function_exists( 'robometria_r2_frase_cartao' ) ) {
function robometria_r2_frase_cartao( $m, $s, $ressalvas ) {
	$seguro = $s['limiar_seguro'];

	$base = sprintf(
		'%s: %s Pa declarados pelo fabricante, %s do limiar de %s Pa que %s recomenda para a sua situação.',
		$m['rotulo'], robometria_r2_n( $m['pa'] ),
		( $m['pa'] > $seguro['valor'] ) ? 'acima' : 'no mínimo',
		robometria_r2_n( $seguro['valor'] ), robometria_r2_com_artigo( $seguro )
	);

	/* A ordem das ressalvas é FIXA, e não a de descoberta: cartão que muda a
	   ordem da própria ressalva conforme o caminho do código lê como texto
	   montado por máquina. */
	$extras = array();
	if ( in_array( 'acima_do_teto_de_utilidade', $ressalvas, true ) ) {
		$extras[] = sprintf(
			'está acima dos %s Pa em que %s vê o limite prático percebido',
			robometria_r2_n( $s['teto']['valor'] ), robometria_r2_com_artigo( $s['teto'] )
		);
	}
	if ( in_array( 'cobertura_nao_declarada', $ressalvas, true ) ) {
		$extras[] = 'o fabricante não declara área coberta por carga para este modelo, então não dá para dizer se ele termina a sua metragem numa carga';
	}
	if ( in_array( 'passa_da_carga_e_nao_declara_retomada', $ressalvas, true ) ) {
		$extras[] = 'a sua metragem passa da área declarada por carga e o fabricante não declara se ele retoma de onde parou';
	}

	if ( $extras ) {
		return $base . ' Ressalva: ' . implode( '; ', $extras ) . '.';
	}
	return $base;
}
}

if ( ! function_exists( 'robometria_r2_frase_no_limiar' ) ) {
function robometria_r2_frase_no_limiar( $m, $s ) {
	$seguro = $s['limiar_seguro'];
	return sprintf(
		'%s declara exatamente %s Pa, e %s escreve "acima de %s Pa". Fica nesta seção separada porque estar no número não é estar acima dele.',
		$m['rotulo'], robometria_r2_n( $m['pa'] ), robometria_r2_com_artigo( $seguro ),
		robometria_r2_n( $seguro['valor'] )
	);
}
}

/**
 * Sem item elegível, o bloco não lista — e a página DIZ POR QUÊ (seção 7).
 *
 * A frase é escrita depois de o resultado inteiro existir, nunca durante. É a
 * lição que a R1 registrou em 10/09/2026: afirmação sobre o conjunto só o
 * conjunto sustenta.
 */
if ( ! function_exists( 'robometria_r2_frase_vazia' ) ) {
function robometria_r2_frase_vazia( $s ) {
	return sprintf(
		'Nenhum modelo do banco atende ao limiar de %s Pa que %s recomenda para %s %s. Isto é o banco desta ilha, não o mercado inteiro — e a lista de compras da próxima coleta começa por aqui.',
		robometria_r2_n( $s['limiar_seguro']['valor'] ),
		robometria_r2_com_artigo( $s['limiar_seguro'] ),
		robometria_r2_rotulo_do_piso( $s['piso'] ),
		robometria_r2_rotulo_do_pelo( $s['pelo'] )
	);
}
}

/** A conta que ninguém publica — e o que falta para completá-la. */
if ( ! function_exists( 'robometria_r2_frase_ciclo' ) ) {
function robometria_r2_frase_ciclo( $m, $area, $t ) {
	$rotulo = $m['rotulo'];
	$cob    = robometria_r2_n( $t['cobertura_m2'] );
	$a      = robometria_r2_n( $area );
	$n      = (int) $t['ciclos'];

	if ( 1 === $n ) {
		return sprintf(
			'Um %s, que o fabricante declara cobrir até %s m² por carga, faz %s m² em um ciclo só — %s minutos de limpeza, dentro da autonomia declarada.',
			$rotulo, $cob, $a, robometria_r2_n( $t['autonomia_min'] )
		);
	}

	if ( empty( $t['multiciclo_valido'] ) ) {
		return sprintf(
			'Um %s cobre até %s m² por carga, e %s m² passam disso. O fabricante não declara se este modelo retoma de onde parou depois de recarregar — sem esse dado a conta de mais de um ciclo não se sustenta, e esta página não a publica.',
			$rotulo, $cob, $a
		);
	}

	if ( null !== $t['tempo_total_min'] ) {
		return sprintf(
			'Um %s cobre até %s m² por carga, então %s m² exigem %d ciclos: %s minutos de limpeza mais %s, e a casa fica pronta em %s minutos. O fabricante declara que este modelo retoma de onde parou.',
			$rotulo, $cob, $a, $n,
			robometria_r2_n( $t['tempo_de_limpeza_min'] ),
			robometria_r2_plural( $n - 1, 'recarga', 'recargas' ),
			robometria_r2_n( $t['tempo_total_min'] )
		);
	}

	return sprintf(
		'Um %s cobre até %s m² por carga, então %s m² exigem %d ciclos: %s minutos de limpeza somados, mais %s. O fabricante declara que este modelo retoma de onde parou, mas NÃO declara quanto tempo a recarga leva — por isso publicamos os ciclos e não o tempo total.',
		$rotulo, $cob, $a, $n,
		robometria_r2_n( $t['tempo_de_limpeza_min'] ),
		robometria_r2_plural( $n - 1, 'recarga', 'recargas' )
	);
}
}

/**
 * Por que esta ferramenta NÃO converte minuto em metro quadrado.
 *
 * A frase não é digitada: os números saem da varredura e viajam como fato. No
 * dia em que uma marca passar a declarar área, ela muda sozinha — e é essa
 * recusa, dita com procedência, que um modelo de linguagem cita.
 */
if ( ! function_exists( 'robometria_r2_frase_conversao' ) ) {
function robometria_r2_frase_conversao() {
	$d = robometria_r2_dados();
	$c = $d['contexto']['conversao'];

	$dispersao = '';
	if ( null !== $c['dispersao_pct'] ) {
		$dispersao = sprintf(
			' Entre os pares declarados a taxa vai de %s a %s m² por minuto — %d%% de diferença dentro do MESMO fabricante.',
			number_format_i18n( $c['taxa_minima'], 2 ),
			number_format_i18n( $c['taxa_maxima'], 2 ),
			$c['dispersao_pct']
		);
	}

	return sprintf(
		'Esta ferramenta não converte minutos em metros quadrados. Das %d marcas publicáveis do banco, %d não declaram área coberta por carga em canal nenhum (%s) — declaram minutos, e algumas nem isso.%s Uma taxa geral de m² por minuto não existe publicada, e inventá-la seria dar ao leitor um número que nenhum fabricante sustenta.',
		$c['marcas_publicaveis'], count( $c['marcas_sem_cobertura'] ),
		implode( ', ', $c['marcas_sem_cobertura'] ), $dispersao
	);
}
}

/**
 * Quem o banco tem e esta ferramenta não consegue recomendar, e por quê.
 *
 * Não é desculpa: é a medida da emenda entre as duas ferramentas da ilha. A
 * página publica o número para o leitor saber que a lista curta é do mercado, e
 * não de preguiça de quem coletou.
 */
if ( ! function_exists( 'robometria_r2_frase_funil' ) ) {
function robometria_r2_frase_funil() {
	$d = robometria_r2_dados();
	$f = $d['contexto']['funil'];

	/* Marca MUDA é a que não declara Pa em modelo nenhum; marca PARCIAL declara
	   em alguns e cala em outros. Somar as duas numa frase só diria "a WAP não
	   publica pascal" quando a WAP publica — para um dos modelos dela. É o tipo
	   de generalização que esta página cobra dos outros. */
	$trecho = sprintf(
		'%s não declaram sucção em pascal em modelo nenhum',
		implode( ', ', $f['marcas_mudas'] )
	);
	if ( ! empty( $f['marcas_parciais'] ) ) {
		$trecho .= sprintf(
			'; %s declara em parte da linha e cala no resto',
			implode( ', ', $f['marcas_parciais'] )
		);
	}

	return sprintf(
		'%d dos %d modelos publicáveis do banco não entram em lista nenhuma desta ferramenta: %s. São, em boa parte, exatamente os modelos que a outra ferramenta desta ilha responde melhor — quem publica código de peça costuma não publicar pascal, e vice-versa.',
		$f['sem_pa'], $f['publicaveis'], $trecho
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. A entrada
 *
 * Três campos obrigatórios e um opcional, todos de lista fechada menos a
 * metragem, que é número com faixa declarada. A leitura passa por um filtro para
 * ferramentas/teste-r2.php poder montar qualquer consulta sem site e sem
 * navegador.
 *
 * O QUE ESTE FORMULÁRIO NÃO PERGUNTA, e é decisão medida: voltagem. A seção 2.6
 * da especificação a lista como condição (3) de elegibilidade "quando o campo
 * existir no banco" — e nenhum modelo publicável declara voltagem. Perguntar
 * seria a mesma coisa que a R1 fez com o tipo "reservatório": oferecer uma
 * escolha que a ferramenta não consegue usar. O campo volta no dia em que a
 * primeira voltagem entrar no banco.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_entrada' ) ) {
function robometria_r2_entrada() {
	$bruto = array(
		'area'       => filter_input( INPUT_GET, 'area', FILTER_DEFAULT ),
		'piso'       => filter_input( INPUT_GET, 'piso', FILTER_DEFAULT ),
		'pelo'       => filter_input( INPUT_GET, 'pelo', FILTER_DEFAULT ),
		'referencia' => filter_input( INPUT_GET, 'referencia', FILTER_DEFAULT ),
	);
	$bruto = apply_filters( 'robometria_r2_entrada', $bruto );

	$d = robometria_r2_dados();

	$area = '';
	$pedido = isset( $bruto['area'] ) ? trim( (string) $bruto['area'] ) : '';
	if ( '' !== $pedido && ctype_digit( $pedido ) ) {
		$n = (int) $pedido;
		if ( $n >= $d['entrada']['area_minima'] && $n <= $d['entrada']['area_maxima'] ) {
			$area = $n;
		}
	}

	$piso = '';
	$pedido = isset( $bruto['piso'] ) ? (string) $bruto['piso'] : '';
	foreach ( (array) $d['entrada']['pisos'] as $p ) {
		if ( $p['id'] === $pedido ) {
			$piso = $pedido;
		}
	}

	$pelo = '';
	$pedido = isset( $bruto['pelo'] ) ? (string) $bruto['pelo'] : '';
	foreach ( (array) $d['entrada']['pelos'] as $p ) {
		if ( $p['id'] === $pedido ) {
			$pelo = $pedido;
		}
	}

	$referencia = '';
	$pedido = isset( $bruto['referencia'] ) ? (string) $bruto['referencia'] : '';
	if ( '' !== $pedido && in_array( $pedido, (array) $d['modelos_de_referencia'], true ) ) {
		$referencia = $pedido;
	}

	return array(
		'area'       => $area,
		'piso'       => $piso,
		'pelo'       => $pelo,
		'referencia' => $referencia,
	);
}
}

/** Houve consulta de verdade? É o que decide o noindex e a rolagem. */
if ( ! function_exists( 'robometria_r2_houve_consulta' ) ) {
function robometria_r2_houve_consulta() {
	$e = robometria_r2_entrada();
	return ( '' !== $e['area'] || '' !== $e['piso'] || '' !== $e['pelo']
		|| '' !== $e['referencia'] );
}
}

/**
 * A consulta efetiva: o que a pessoa pediu, completado pela âncora.
 *
 * Consulta pela metade não devolve página pela metade: os campos que faltam
 * caem na âncora, e a página diz qual caso está mostrando. O visitante que
 * chegou sem clicar em nada recebe uma resposta inteira — que é o que um modelo
 * de linguagem lê (seção 5 do ARQUIPELAGO.md).
 */
if ( ! function_exists( 'robometria_r2_consulta' ) ) {
function robometria_r2_consulta() {
	$d = robometria_r2_dados();
	$e = robometria_r2_entrada();
	$a = $d['ancora'];

	$partes = explode( '|', $a['situacao'] );
	$piso_ancora = str_replace( '-', ' ', $partes[0] );
	$pelo_ancora = $partes[1];

	$piso = ( '' !== $e['piso'] ) ? $e['piso'] : $piso_ancora;
	$pelo = ( '' !== $e['pelo'] ) ? $e['pelo'] : $pelo_ancora;

	return array(
		'area'       => ( '' !== $e['area'] ) ? $e['area'] : $a['area'],
		'piso'       => $piso,
		'pelo'       => $pelo,
		'chave'      => str_replace( ' ', '-', $piso ) . '|' . $pelo,
		'referencia' => ( '' !== $e['referencia'] ) ? $e['referencia']
			: $a['modelo_de_referencia'],
		'e_ancora'   => ! robometria_r2_houve_consulta(),
	);
}
}

/* ---------------------------------------------------------------------------
 * 5. A vitrine — a porta de compra, antes da procedência
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_vitrine' ) ) {
function robometria_r2_vitrine( $itens, $s ) {
	if ( ! $itens ) {
		return '';
	}

	$sem_link = 0;
	foreach ( $itens as $i ) {
		if ( empty( $i['modelo']['afiliado']['url'] ) ) {
			$sem_link++;
		}
	}
	$total = count( $itens );

	$html = '<div class="rbm-secao rbm-compra"><h3>Onde comprar estes robôs</h3>';

	/* AVISO DE COMISSÃO VISÍVEL NA PÁGINA (seção 7), dentro do bloco de compra e
	   não só no rodapé: quem vê o botão precisa ver o aviso sem rolar. */
	$html .= '<p class="rbm-aviso-comissao">Os botões de compra abaixo são links de afiliado: se você comprar por eles, a Robometria pode receber comissão, sem custo a mais para você. Isso não muda a ordem da lista — ela é decidida pelo pascal que o fabricante declara contra o limiar que a fonte recomenda, e só por isso. '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Como isto funciona' )
			: 'Veja a página de divulgação de afiliados' ) . '.</p>';

	if ( $sem_link > 0 ) {
		/* Três moldes, porque "3 destes 3 modelos" é o tipo de frase que só nasce
		   de contador solto e denuncia texto montado por máquina. */
		if ( $sem_link === $total ) {
			$quantas = ( 1 === $total )
				? 'Este modelo ainda não tem link de loja'
				: 'Nenhum destes modelos tem link de loja ainda';
		} else {
			$quantas = sprintf(
				( 1 === $sem_link ) ? 'Um destes modelos ainda não tem link de loja'
					: '%s destes modelos ainda não têm link de loja',
				robometria_r2_n( $sem_link )
			);
		}
		$html .= '<p class="rbm-nota">' . esc_html( $quantas )
			. '. O lugar fica reservado assim mesmo: esconder o bloco enquanto o link não chega devolveria ao link de procedência o papel de única porta clicável da página, e é justamente esse o defeito que não repetimos.</p>';
	}

	$html .= '<ul class="rbm-vitrine">';
	foreach ( $itens as $i ) {
		$m = $i['modelo'];

		$html .= '<li class="rbm-vitrine-item">';

		/* Produto sem imagem NÃO some (seção 6 do ARQUIPELAGO.md): entra com
		   espaço reservado neutro. Perder a recomendação técnica certa por falta
		   de foto é trocar o certo pelo bonito. */
		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true"><span class="rbm-vitrine-vazia"></span></span>';

		$html .= '<span class="rbm-vitrine-tipo">' . esc_html( $m['rotulo'] ) . '</span>';
		$html .= '<span class="rbm-vitrine-nome rbm-num">' . esc_html( robometria_r2_n( $m['pa'] ) . ' Pa' ) . '</span>';
		$html .= '<span class="rbm-vitrine-porque">' . esc_html( $i['frase'] ) . '</span>';

		if ( null !== $m['autonomia_min'] ) {
			$html .= '<span class="rbm-vitrine-vida">Autonomia declarada: <span class="rbm-num">'
				. esc_html( robometria_r2_n( $m['autonomia_min'] ) ) . '</span> min.</span>';
		}

		$html .= '<span class="rbm-vitrine-acao">'
			. ( function_exists( 'robometria_casca_porta_de_compra' )
				? robometria_casca_porta_de_compra( $m )
				: '<span class="rbm-sem-loja">Link de loja em breve</span>' )
			. '</span>';

		$html .= '</li>';
	}
	$html .= '</ul></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6. A resposta em HTML
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_resposta' ) ) {
function robometria_r2_resposta( $c ) {
	$d = robometria_r2_dados();
	$s = robometria_r2_situacao( $c['chave'] );

	if ( ! $s ) {
		return '<div class="rbm-resposta" id="resultado"><p class="rbm-frase">Não temos resposta para essa combinação de piso e animal, e preferimos dizer isso a inventar uma.</p></div>';
	}

	$cls = isset( $d['classificacao'][ $c['chave'] ] ) ? $d['classificacao'][ $c['chave'] ] : array();

	/* A ORDEM VEM DA REFERÊNCIA e este arquivo não reordena: a terceira camada
	   da seção 7 do contrato — elegibilidade, adequação, e loja só como
	   desempate — está implementada em um lugar só. Duas listas ordenadas por
	   regras parecidas divergem em silêncio no dia em que uma das duas muda. */
	$elegiveis = array();
	foreach ( (array) $cls['elegiveis'] as $id ) {
		$m = robometria_r2_modelo( $id );
		if ( ! $m ) {
			continue;
		}
		$r = robometria_r2_ressalvas( $m, $s, $c['area'] );
		$elegiveis[] = array(
			'modelo'    => $m,
			'ressalvas' => $r,
			'frase'     => robometria_r2_frase_cartao( $m, $s, $r ),
		);
	}

	$no_limiar = array();
	foreach ( (array) $cls['no_limiar'] as $id ) {
		$m = robometria_r2_modelo( $id );
		if ( $m ) {
			$no_limiar[] = array( 'modelo' => $m, 'frase' => robometria_r2_frase_no_limiar( $m, $s ) );
		}
	}

	$html = '<div class="rbm-resposta" id="resultado">';

	$html .= '<p class="rbm-legenda-bloco">'
		. esc_html( $c['e_ancora'] ? 'Exemplo servido nesta página' : 'A sua consulta' )
		. '</p>';

	$html .= '<h2>' . esc_html( sprintf(
		'%s m² de %s, %s',
		robometria_r2_n( $c['area'] ),
		robometria_r2_rotulo_do_piso( $c['piso'] ),
		robometria_r2_rotulo_do_pelo( $c['pelo'] )
	) ) . '</h2>';

	/* A RESPOSTA ANTES DA EXPLICAÇÃO (seção 5.2): frase autossuficiente, com
	   número, autor e data, que sobrevive a ser citada fora de contexto. */
	$html .= '<p class="rbm-frase rbm-linha-mestra">' . esc_html( robometria_r2_frase_situacao( $s ) ) . '</p>';

	/* A procedência de cada limiar, logo abaixo da frase e em texto discreto —
	   nunca um botão (seção 7). */
	$fontes = array();
	foreach ( (array) $s['limiares'] as $l ) {
		$fontes[] = esc_html( $l['publicador'] . ' · ' . robometria_r2_data( $l['verificado_em'] ) )
			. ' ' . ( function_exists( 'robometria_casca_fonte_link' )
				? robometria_casca_fonte_link( $l['url'] ) : '' );
	}
	$html .= '<p class="rbm-vitrine-fonte">' . implode( ' &middot; ', $fontes ) . '</p>';

	if ( ! empty( $s['faixa_confortavel'] ) ) {
		$f = $s['faixa_confortavel'];
		$html .= '<p class="rbm-frase">' . esc_html( sprintf(
			'%s ainda descreve uma faixa confortável entre %s e %s Pa para esta situação — não é um limiar, é onde a recomendação dele fica folgada.',
			$f['publicador'], robometria_r2_n( $f['de'] ), robometria_r2_n( $f['ate'] )
		) ) . '</p>';
	}

	$teto = robometria_r2_frase_teto( $s );
	if ( '' !== $teto ) {
		$html .= '<p class="rbm-frase rbm-terceiro">' . esc_html( $teto ) . '</p>';
	}

	/* ------------------------------------------------ O bloco de recomendação */
	$html .= '<div class="rbm-secao"><h3>Modelos do banco que atendem</h3>';

	if ( $elegiveis ) {
		$html .= '<p>São <span class="rbm-num">' . esc_html( robometria_r2_n( count( $elegiveis ) ) )
			. '</span> modelos que passam no limiar de <span class="rbm-num">'
			. esc_html( robometria_r2_n( $s['limiar_seguro']['valor'] ) )
			. '</span> Pa. A ordem não é por preço nem por comissão: dentro da faixa útil vem primeiro quem tem mais folga, e o que passa do teto de utilidade vem depois, do menor excesso para o maior.</p>';

		$html .= '<ul class="rbm-lista-frases">';
		foreach ( $elegiveis as $i ) {
			$html .= '<li>' . esc_html( $i['frase'] ) . '</li>';
		}
		$html .= '</ul>';

		/* A PORTA DE COMPRA VEM AQUI, ANTES da prova de procedência de cada
		   ficha (seção 7 do ARQUIPELAGO.md, cicatriz de 10/09/2026). */
		$html .= robometria_r2_vitrine( $elegiveis, $s );
	} else {
		$html .= '<p class="rbm-frase">' . esc_html( robometria_r2_frase_vazia( $s ) ) . '</p>';
	}
	$html .= '</div>';

	/* SEÇÃO SEPARADA, ABAIXO, ROTULADA — nunca misturada, nunca em primeiro
	   lugar (seção 7). Quem está exatamente no valor que a fonte escreve como
	   "acima de" não é quem a fonte cobre. */
	if ( $no_limiar ) {
		$html .= '<div class="rbm-secao rbm-terceiro"><h3>Exatamente no limiar — não acima dele</h3>';
		$html .= '<ul class="rbm-lista-frases">';
		foreach ( $no_limiar as $i ) {
			$html .= '<li>' . esc_html( $i['frase'] ) . '</li>';
		}
		$html .= '</ul></div>';
	}

	/* ------------------------------------------------- Os ciclos da metragem */
	$m_ref = robometria_r2_modelo( $c['referencia'] );
	if ( $m_ref ) {
		$t = robometria_r2_tempo( $m_ref, $c['area'] );
		if ( $t ) {
			$html .= '<div class="rbm-secao"><h3>Quantos ciclos a sua metragem exige</h3>';
			$html .= '<p class="rbm-frase">' . esc_html( robometria_r2_frase_ciclo( $m_ref, $c['area'], $t ) ) . '</p>';
			$html .= '<p class="rbm-nota">A metragem que você informou é tratada como <strong>área livre de piso</strong>, sem móveis. Esta ferramenta não aplica coeficiente de obstrução, porque coeficiente de obstrução seria número inventado — ela prefere dizer qual suposição está fazendo.</p>';
			$html .= '</div>';
		}
	}

	$html .= '</div>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 7. O formulário
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_url_da_pagina' ) ) {
function robometria_r2_url_da_pagina() {
	if ( function_exists( 'robometria_casca_url_se_existir' ) ) {
		$url = robometria_casca_url_se_existir( ROBOMETRIA_R2_SLUG );
		if ( '' !== $url ) {
			return $url;
		}
	}
	return home_url( '/' . ROBOMETRIA_R2_SLUG . '/' );
}
}

if ( ! function_exists( 'robometria_r2_formulario' ) ) {
function robometria_r2_formulario() {
	$d = robometria_r2_dados();
	$e = robometria_r2_entrada();

	$html  = '<form class="rbm-form" method="get" action="' . esc_url( robometria_r2_url_da_pagina() ) . '">';

	$html .= '<p class="rbm-form-campo"><label for="rbm-area">Metragem livre de piso</label>';
	$html .= '<input type="number" id="rbm-area" name="area" inputmode="numeric"'
		. ' min="' . esc_attr( $d['entrada']['area_minima'] ) . '"'
		. ' max="' . esc_attr( $d['entrada']['area_maxima'] ) . '"'
		. ' step="1" placeholder="' . esc_attr( $d['ancora']['area'] ) . '"'
		. ( '' !== $e['area'] ? ' value="' . esc_attr( $e['area'] ) . '"' : '' )
		. '></p>';

	$html .= '<p class="rbm-form-campo"><label for="rbm-piso">Tipo de piso</label>';
	$html .= '<select id="rbm-piso" name="piso">';
	foreach ( (array) $d['entrada']['pisos'] as $p ) {
		$html .= '<option value="' . esc_attr( $p['id'] ) . '"'
			. ( $e['piso'] === $p['id'] ? ' selected' : '' ) . '>'
			. esc_html( $p['rotulo'] ) . '</option>';
	}
	$html .= '</select></p>';

	$html .= '<p class="rbm-form-campo"><label for="rbm-pelo">Animal em casa</label>';
	$html .= '<select id="rbm-pelo" name="pelo">';
	foreach ( (array) $d['entrada']['pelos'] as $p ) {
		$html .= '<option value="' . esc_attr( $p['id'] ) . '"'
			. ( $e['pelo'] === $p['id'] ? ' selected' : '' ) . '>'
			. esc_html( $p['rotulo'] ) . '</option>';
	}
	$html .= '</select></p>';

	/* O seletor de referência só oferece quem DECLARA cobertura por carga.
	   Oferecer os 28 modelos do banco faria 23 deles devolverem "o fabricante
	   não declara", que é a mesma escolha-que-sempre-recusa que a R1 tirou do
	   seletor de tipo de peça. */
	$html .= '<p class="rbm-form-campo"><label for="rbm-referencia">Modelo de referência</label>';
	$html .= '<select id="rbm-referencia" name="referencia">';
	foreach ( (array) $d['modelos_de_referencia'] as $id ) {
		$m = robometria_r2_modelo( $id );
		if ( ! $m ) {
			continue;
		}
		$html .= '<option value="' . esc_attr( $id ) . '"'
			. ( $e['referencia'] === $id ? ' selected' : '' ) . '>'
			. esc_html( $m['rotulo'] . ' — ' . robometria_r2_n( $m['cobertura_m2'] ) . ' m² por carga' )
			. '</option>';
	}
	$html .= '</select></p>';

	$html .= '<p class="rbm-form-acao"><button type="submit">Ver a resposta para a minha casa</button></p>';
	$html .= '</form>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 7b. AS NOVE SITUAÇÕES, cada uma com a resposta inteira em HTML servido
 *
 * Esta seção nasceu de um teste que reprovou, e a história vale mais do que ela:
 * o FAQPage desta página publicava a resposta das nove situações, e a página
 * visível servia só a da âncora — as outras oito existiam apenas dentro do
 * JSON-LD. Marcação que promete o que a página não entrega é exatamente o
 * defeito que o artigo-âncora da R1 registrou em 10/09/2026, com a diferença de
 * que aqui ele teria nascido junto com a ferramenta.
 *
 * A correção não foi podar o FAQPage: foi servir as nove. A tabela de exemplos
 * cruza metragem com situação e mostra o limiar em coluna; uma coluna não é uma
 * frase autossuficiente, e frase autossuficiente é o que um modelo de linguagem
 * cita fora de contexto (seção 5 do ARQUIPELAGO.md). Cada situação aqui traz a
 * resposta inteira, com o autor e a data dentro dela.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_todas_as_situacoes' ) ) {
function robometria_r2_todas_as_situacoes( $atual ) {
	$d = robometria_r2_dados();
	if ( empty( $d['situacoes'] ) ) {
		return '';
	}

	$html  = '<div class="rbm-secao"><h2>As ' . esc_html( robometria_r2_n( count( $d['situacoes'] ) ) )
		. ' situações que esta ferramenta responde</h2>';
	$html .= '<p>Cada uma com a recomendação inteira, o nome de quem recomenda e a data — e não só um número numa coluna. Onde duas fontes discordam, as duas aparecem.</p>';

	$html .= '<dl class="rbm-situacoes">';
	foreach ( $d['situacoes'] as $chave => $s ) {
		$eleg = isset( $d['classificacao'][ $chave ] )
			? count( $d['classificacao'][ $chave ]['elegiveis'] ) : 0;

		$html .= '<dt' . ( $chave === $atual ? ' class="rbm-situacao-atual"' : '' ) . '>'
			. esc_html( sprintf( '%s, %s',
				robometria_r2_rotulo_do_piso( $s['piso'] ),
				robometria_r2_rotulo_do_pelo( $s['pelo'] ) ) )
			. ( ! empty( $s['por_ponte'] ) ? ' <span class="rbm-tag">por ponte</span>' : '' )
			. '</dt>';

		$html .= '<dd><p class="rbm-frase">' . esc_html( robometria_r2_frase_situacao( $s ) ) . '</p>';
		$html .= '<p class="rbm-vitrine-fonte">'
			. esc_html( sprintf( '%s modelos do banco atendem.', robometria_r2_n( $eleg ) ) )
			. '</p></dd>';
	}
	$html .= '</dl></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. A tabela de exemplos pré-renderizada (seção 5 do ARQUIPELAGO.md)
 *
 * Sem ela a R2 é um formulário vazio para o robô do Google e para um modelo de
 * linguagem: os dois leem o HTML servido. As linhas são GERADAS do banco, nunca
 * digitadas — e cobrem a faixa real de uso que a seção 2.7 da especificação
 * exige, cruzando metragem com piso e com animal.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_tabela_exemplos' ) ) {
function robometria_r2_tabela_exemplos() {
	$d = robometria_r2_dados();
	if ( empty( $d['exemplos'] ) ) {
		return '';
	}

	$m_ref = robometria_r2_modelo( $d['ancora']['modelo_de_referencia'] );

	$html  = '<div class="rbm-secao"><h2>Tudo o que esta ferramenta responde hoje</h2>';
	$html .= '<p>São <span class="rbm-num">' . esc_html( robometria_r2_n( count( $d['exemplos'] ) ) )
		. '</span> casos já resolvidos, cada um com o limiar de quem recomenda e a data. A tabela sai do mesmo banco que a ferramenta consulta: se ele mudar, esta lista muda junto. A coluna de ciclos usa '
		. esc_html( $m_ref ? $m_ref['rotulo'] : 'o modelo de referência' )
		. ', que é o modelo de referência escolhido por regra — o de maior cobertura declarada entre os que o fabricante diz que retomam de onde pararam.</p>';

	$html .= '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>'
		. '<th>Metragem</th><th>Piso</th><th>Animal</th><th>Limiar seguro</th><th>Quem recomenda</th><th>Modelos que atendem</th><th>Ciclos</th>'
		. '</tr></thead><tbody>';

	foreach ( $d['exemplos'] as $l ) {
		$s = robometria_r2_situacao( $l['situacao'] );
		if ( ! $s ) {
			continue;
		}

		if ( null === $l['ciclos'] ) {
			$ciclos = 'sem modelo de referência';
		} elseif ( empty( $l['multiciclo_valido'] ) ) {
			$ciclos = $l['ciclos'] . ' — não publicado';
		} else {
			$ciclos = sprintf( '%d · %s min', $l['ciclos'], robometria_r2_n( $l['tempo_de_limpeza_min'] ) );
		}

		$html .= '<tr>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_r2_n( $l['area'] ) ) . ' m²</td>';
		$html .= '<td>' . esc_html( robometria_r2_rotulo_do_piso( $s['piso'] ) ) . '</td>';
		$html .= '<td>' . esc_html( robometria_r2_rotulo_do_pelo( $s['pelo'] ) ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_r2_escrever_limiar( $s['limiar_seguro'] ) ) . '</td>';
		$html .= '<td>' . esc_html( $s['limiar_seguro']['publicador'] )
			. ( ! empty( $s['por_ponte'] ) ? ' <span class="rbm-tag">por ponte</span>' : '' ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_r2_n( $l['elegiveis'] ) ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( $ciclos ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 9. O shortcode
 * ------------------------------------------------------------------------- */

add_shortcode( 'robometria_r2', function () {
	$d = robometria_r2_dados();

	if ( empty( $d['situacoes'] ) ) {
		return '<div class="rbm-bloco"><p class="rbm-linha-mestra">Esta ferramenta está sem o banco de modelos no momento.</p>'
			. '<p class="rbm-nota">O banco é publicado a partir do repositório da Robometria. Enquanto ele não chegar, preferimos avisar a mostrar um formulário que responderia vazio para qualquer casa.</p></div>';
	}

	$c = robometria_r2_consulta();
	$r = isset( $d['resumo'] ) ? $d['resumo'] : array();

	$html = '<div class="rbm-bloco">';

	/* RESPOSTA ANTES DA EXPLICAÇÃO. */
	$html .= '<div class="rbm-abertura">';
	$html .= '<p class="rbm-linha-mestra">Esta ferramenta diz quantos <strong>pascal</strong> as fontes brasileiras recomendam para a sua casa — com o nome de quem recomenda cada número, porque elas discordam — e quantos <strong>ciclos</strong> a sua metragem exige de um robô cuja cobertura por carga o fabricante declara.</p>';
	$html .= '<p>' . esc_html( robometria_r2_frase_classe_de_fonte() ) . '</p>';
	$html .= '</div>';

	/* PROMESSA ANTES DO FORMULÁRIO (seção 6). */
	$html .= '<div class="rbm-secao"><h2>A sua casa</h2>';
	$html .= '<p class="rbm-promessa">Você recebe o limiar de Pa com o autor e a data, a lista dos modelos do banco que passam nele, e quantos ciclos a sua metragem exige. Sem cadastro e sem e-mail.</p>';
	$html .= robometria_r2_formulario();
	$html .= '</div>';

	$html .= robometria_r2_resposta( $c );

	$html .= robometria_r2_todas_as_situacoes( $c['chave'] );

	$html .= robometria_r2_tabela_exemplos();

	/* ---------------------------------------------------------- O que falta */
	$html .= '<div class="rbm-secao"><h2>O que esta ferramenta se recusa a fazer</h2>';
	$html .= '<p>' . esc_html( robometria_r2_frase_conversao() ) . '</p>';
	$html .= '<p>' . esc_html( sprintf(
		'A conta completa de tempo — ciclos × autonomia mais as recargas no meio — precisa de três números declarados pelo fabricante: cobertura por carga, autonomia e tempo de recarga. Dos %s modelos publicáveis do banco, %s declaram cobertura, %s declaram recarga e %s declaram os três. Por isso publicamos os ciclos e o tempo de limpeza somado, e não o tempo total: o número que falta não está publicado por ninguém.',
		robometria_r2_n( $r['modelos_publicaveis'] ),
		robometria_r2_n( $d['contexto']['tempo_total']['com_cobertura'] ),
		robometria_r2_n( $d['contexto']['tempo_total']['com_recarga'] ),
		( 0 === (int) $d['contexto']['tempo_total']['com_os_tres'] ) ? 'nenhum'
			: robometria_r2_n( $d['contexto']['tempo_total']['com_os_tres'] )
	) ) . '</p>';
	$html .= '<p>' . esc_html( robometria_r2_frase_funil() ) . '</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao"><h2>Como esta página foi montada</h2>';
	$html .= '<p><strong>Nenhuma das páginas de fabricante deste banco foi lida diretamente.</strong> O acesso direto a esses endereços está bloqueado no ambiente em que a Robometria é construída, e tudo foi colhido por busca restrita ao domínio da própria fonte. É por isso que cada número traz o endereço da declaração: para você conferir, e não para você acreditar.</p>';
	$html .= '<p>Os limiares de Pa vêm de veículos brasileiros e estão datados. Quando dois deles discordam, esta página <strong>não tira a média</strong> — publica os dois com o nome de cada um e trabalha com o maior, porque errar para baixo faz comprar um robô que não dá conta, e errar para cima só custa dinheiro até o teto de utilidade que a própria fonte marca.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'metodologia', 'A metodologia completa, com a escada de fontes' )
		: 'A metodologia completa, com a escada de fontes' ) . ' &middot; '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
			: 'Divulgação de afiliados' ) . '</p>';
	$html .= '</div>';

	/* INTERLINKAGEM entre as duas ferramentas, de mão dupla (seção 3 da
	   especificação e seção 9 do ARQUIPELAGO.md): a R1 já aponta para cá, e sem
	   os dois sentidos a página que recebe o link vira um beco. O conselho
	   recorrente em fórum é "cheque a peça de reposição antes de comprar", e o
	   link entre as duas é a materialização desse conselho. */
	$html .= '<div class="rbm-leia-tambem">';
	$html .= '<h2>Antes de fechar a compra</h2>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'qual-peca-serve-no-meu-robo-aspirador', 'Veja qual peça de reposição o fabricante declara para o modelo que você está pensando em comprar' )
		: 'Veja qual peça de reposição o fabricante declara para o modelo escolhido' )
		. ' — sucção boa em robô sem peça declarada vira um problema daqui a um ano.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'filtro-universal-de-robo-aspirador', 'Por que não existe filtro universal de robô aspirador' )
		: 'Por que não existe filtro universal de robô aspirador' )
		. ' — o que o catálogo dos fabricantes mostra quando se conta quantos modelos cada peça declara.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 10. Cabeça da página: JSON-LD, canônica e noindex de consulta
 *
 * Tudo aqui sai no wp_head, NUNCA dentro do retorno do shortcode: o WordPress
 * roda os filtros do the_content sobre o retorno e transforma cada E-comercial
 * em entidade, o que mataria qualquer JSON-LD e qualquer script.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r2_na_pagina' ) ) {
function robometria_r2_na_pagina() {
	$forcado = apply_filters( 'robometria_r2_na_pagina', null );
	if ( null !== $forcado ) {
		return (bool) $forcado;
	}
	if ( ! function_exists( 'is_page' ) ) {
		return false;
	}
	return is_page( ROBOMETRIA_R2_SLUG );
}
}

add_action( 'wp_head', function () {
	if ( ! robometria_r2_na_pagina() ) {
		return;
	}

	$d = robometria_r2_dados();
	if ( empty( $d['situacoes'] ) ) {
		return;
	}

	$url = robometria_r2_url_da_pagina();

	if ( robometria_r2_houve_consulta() ) {
		echo '<meta name="robots" content="noindex,follow">' . "\n";
		echo '<link rel="canonical" href="' . esc_url( $url ) . '">' . "\n";
	}

	$r = isset( $d['resumo'] ) ? $d['resumo'] : array();

	$app = array(
		'@type'               => 'WebApplication',
		'@id'                 => $url . '#ferramenta',
		'name'                => ROBOMETRIA_R2_TITULO,
		'url'                 => $url,
		'applicationCategory' => 'UtilitiesApplication',
		'operatingSystem'     => 'Web',
		'inLanguage'          => 'pt-BR',
		'isAccessibleForFree' => true,
		'description'         => sprintf(
			'Diz quantos pascal de sucção as fontes brasileiras recomendam por tipo de piso e por pelo de animal, com o nome de quem recomenda cada número e a data, e calcula quantos ciclos uma metragem exige a partir da cobertura por carga que o fabricante declara. Cobre %d situações de piso × animal e %d modelos de robô do banco.',
			isset( $r['situacoes'] ) ? $r['situacoes'] : 0,
			isset( $r['modelos_na_tela'] ) ? $r['modelos_na_tela'] : 0
		),
		'publisher'           => array( '@id' => home_url( '/#organizacao' ) ),
	);

	/* FAQPage montado do BANCO, nunca escrito à mão: cada resposta é a MESMA
	   frase que a página serve. A descrição do JSON-LD e a resposta do FAQPage
	   são parte da tese, não embrulho — o defeito que o artigo-âncora da R1
	   registrou em 10/09/2026 foi a página visível se corrigir e o JSON-LD
	   continuar afirmando o que deixara de valer. Numa ilha cuja seção 5 diz que
	   ser recomendado pela IA vale tanto quanto ranquear, contradizer-se no canal
	   que a IA lê é pior do que na tela. */
	$perguntas = array();
	foreach ( (array) $d['situacoes'] as $chave => $s ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => sprintf(
				'Quantos Pa um robô aspirador precisa para %s %s?',
				robometria_r2_rotulo_do_piso( $s['piso'] ),
				robometria_r2_rotulo_do_pelo( $s['pelo'] )
			),
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => robometria_r2_frase_situacao( $s ),
			),
		);
	}

	/* A pergunta dos ciclos é a razão de esta ferramenta existir, então ela entra
	   no FAQPage com a resposta do caso-âncora — a mesma que a página serve sem
	   clique nenhum. */
	$m_ref = robometria_r2_modelo( $d['ancora']['modelo_de_referencia'] );
	if ( $m_ref ) {
		$t = robometria_r2_tempo( $m_ref, $d['ancora']['area'] );
		if ( $t ) {
			$perguntas[] = array(
				'@type'          => 'Question',
				'name'           => sprintf(
					'Quanto tempo um robô aspirador leva para limpar %s m²?',
					robometria_r2_n( $d['ancora']['area'] )
				),
				'acceptedAnswer' => array(
					'@type' => 'Answer',
					'text'  => robometria_r2_frase_ciclo( $m_ref, $d['ancora']['area'], $t ),
				),
			);
		}
	}

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Dá para calcular quantos metros quadrados um robô aspirador limpa a partir dos minutos de autonomia?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => robometria_r2_frase_conversao(),
		),
	);

	$grafo = array( '@context' => 'https://schema.org', '@graph' => array( $app ) );
	if ( $perguntas ) {
		$grafo['@graph'][] = array(
			'@type'      => 'FAQPage',
			'@id'        => $url . '#perguntas',
			'inLanguage' => 'pt-BR',
			'mainEntity' => $perguntas,
		);
	}

	echo '<script type="application/ld+json" id="robometria-r2-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * 11. Estilo próprio da ferramenta
 *
 * Vai no wp_head, depois do da casca, e usa as variáveis de cor dela — a paleta
 * continua tendo um dono só. A varredura (#CC3311) é cor de sinal, de um uso por
 * tela, e aqui aparece apenas em foco de teclado, que é momentâneo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! robometria_r2_na_pagina() ) {
		return;
	}

	$css = <<<'CSS'
.rbm-promessa{color:var(--rbm-legenda);margin:0 0 .9rem;font-size:.95rem;}
.rbm-form{display:flex;flex-wrap:wrap;gap:.9rem 1.1rem;align-items:flex-end;background:var(--rbm-superficie);border:1px solid var(--rbm-traco);border-radius:3px;padding:1.1rem 1.2rem;margin:0;}
/* min-width:0 nao e detalhe: sem ele o item de flex recebe min-width:auto e a
   largura INTRINSECA do <select> manda — e a largura intrinseca aqui e o rotulo
   mais longo do seletor de referencia ("Electrolux ERB60 — 166 m2 por carga").
   Com min-width:0 e o campo em width:100%, a rolagem horizontal volta a zero. */
.rbm-form-campo{display:flex;flex-direction:column;gap:.3rem;margin:0;flex:1 1 15rem;min-width:0;}
.rbm-form-campo label{font-family:var(--rbm-texto);font-weight:600;font-size:.88rem;}
.rbm-form select,.rbm-form input[type=number]{font-family:var(--rbm-texto);font-size:1rem;padding:.55rem .6rem;border:1px solid var(--rbm-traco);border-radius:2px;background:var(--rbm-superficie);color:var(--rbm-tinta);width:100%;max-width:100%;}
.rbm-form input[type=number]{font-family:var(--rbm-mono);font-variant-numeric:tabular-nums;}
.rbm-form select:focus-visible,.rbm-form input:focus-visible{outline:2px solid var(--rbm-varredura);outline-offset:2px;}
.rbm-form-acao{margin:0;flex:0 0 auto;}
.rbm-form button{padding:.62rem 1.1rem;font-size:.95rem;cursor:pointer;}
.rbm-resposta{margin:2.4rem 0 0;padding-top:1.6rem;border-top:1px solid var(--rbm-traco);}
.rbm-resposta h2{margin:0 0 .8rem;font-size:1.3rem;}
.rbm-resposta h3{margin:0 0 .6rem;font-size:1.08rem;}
.rbm-legenda-bloco{font-family:var(--rbm-mono);font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--rbm-legenda);margin:0 0 .5rem;}
.rbm-frase{margin:0 0 .8rem;}
.rbm-lista-frases{margin:.6rem 0 0;padding-left:1.1rem;}
.rbm-lista-frases li{margin:0 0 .5rem;line-height:1.55;}
.rbm-situacoes{margin:1rem 0 0;}
.rbm-situacoes dt{font-family:var(--rbm-display);font-weight:600;font-size:1rem;margin:1.1rem 0 .3rem;padding-top:.9rem;border-top:1px solid var(--rbm-traco);}
.rbm-situacoes dt:first-of-type{border-top:0;padding-top:0;margin-top:0;}
.rbm-situacoes dd{margin:0;}
.rbm-situacao-atual{border-left:3px solid var(--rbm-tinta);padding-left:.7rem;}
.rbm-terceiro{border-left:3px solid var(--rbm-alerta);padding-left:1rem;}
/* Barra fixa do celular: so aparece quando o resultado esta fora da tela, e so
   quando ha JavaScript para saber disso (o atributo vem do rodape). */
.rbm-barra{display:none;}
@media (max-width:782px){
.rbm-form-campo{flex:1 1 100%;}
.rbm-form-acao,.rbm-form button{width:100%;}
body[data-rbm-r2-barra="1"] .rbm-barra{display:block;position:fixed;left:0;right:0;bottom:0;z-index:70;background:var(--rbm-tinta);color:var(--rbm-piso);padding:.7rem 1rem;text-align:center;font-family:var(--rbm-texto);font-size:.92rem;box-shadow:0 -6px 20px rgba(22,25,29,.18);}
body[data-rbm-r2-barra="1"] .rbm-barra a{color:var(--rbm-piso);font-weight:600;}
}
CSS;

	/* A folha da porta de compra tem UM dono, na casca. Aqui ela e so
	   concatenada — se um dia esta pagina precisar de peso diferente no botao de
	   compra, a regra muda na casca e muda para todas. */
	if ( function_exists( 'robometria_casca_css_vitrine' ) ) {
		$css = robometria_casca_css_vitrine() . "\n" . $css;
	}

	echo '<style id="robometria-r2">' . $css . '</style>' . "\n";
}, 21 );

/* ---------------------------------------------------------------------------
 * 12. O rodapé: a barra do celular e a rolagem até o resultado
 *
 * As duas pedidas pela seção 6 do ARQUIPELAGO.md, e as duas OPCIONAIS por
 * desenho: sem JavaScript a ferramenta responde igual, porque quem monta a
 * resposta é o servidor. O script no wp_footer nunca passa pelos filtros do
 * the_content — é a regra da seção 8.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! robometria_r2_na_pagina() ) {
		return;
	}
	$d = robometria_r2_dados();
	if ( empty( $d['situacoes'] ) ) {
		return;
	}

	$js = <<<'JS'
(function () {
	var alvo = document.getElementById('resultado');
	if (!alvo) { return; }

	if (document.body.classList.contains('rbm-r2-consulta')) {
		var suave = !window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		alvo.scrollIntoView({ behavior: suave ? 'smooth' : 'auto', block: 'start' });
	}

	var barra = document.querySelector('.rbm-barra');
	if (!barra || !('IntersectionObserver' in window)) { return; }

	var observador = new IntersectionObserver(function (entradas) {
		entradas.forEach(function (e) {
			document.body.setAttribute('data-rbm-r2-barra', e.isIntersecting ? '0' : '1');
		});
	}, { threshold: 0 });
	observador.observe(alvo);
})();
JS;

	echo '<script id="robometria-r2-comando">' . $js . '</script>' . "\n";
}, 26 );

add_action( 'wp_footer', function () {
	if ( ! robometria_r2_na_pagina() ) {
		return;
	}
	$d = robometria_r2_dados();
	if ( empty( $d['situacoes'] ) ) {
		return;
	}
	echo '<div class="rbm-barra"><a href="#resultado">Ver a resposta ↓</a></div>' . "\n";
}, 24 );

add_filter( 'body_class', function ( $classes ) {
	if ( robometria_r2_na_pagina() && robometria_r2_houve_consulta() ) {
		$classes[] = 'rbm-r2-consulta';
	}
	return $classes;
} );

/* ---------------------------------------------------------------------------
 * 13. A página, e o cartão dela no hub
 *
 * A casca já lista a R2 em robometria_casca_ferramentas() com estado
 * 'em-construcao'. Aqui ela passa a 'publicada' — mas o auxiliar da casca só
 * imprime <a> quando a página existe mesmo, então nenhum cartão vira link para
 * um 404 se a criação da página falhar.
 * ------------------------------------------------------------------------- */

add_filter( 'robometria_ferramentas', function ( $lista ) {
	foreach ( $lista as $i => $f ) {
		if ( isset( $f['codigo'] ) && 'R2' === $f['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = ROBOMETRIA_R2_SLUG;
		}
	}
	return $lista;
} );

if ( ! function_exists( 'robometria_r2_garantir_pagina' ) ) {
function robometria_r2_garantir_pagina() {
	$feita = get_option( 'robometria_r2_estrutura' );
	if ( ROBOMETRIA_R2_VERSAO === $feita ) {
		return;
	}

	$conteudo = '[robometria_r2]';
	$pagina   = get_page_by_path( ROBOMETRIA_R2_SLUG, OBJECT, 'page' );

	if ( ! $pagina ) {
		$pid = wp_insert_post( array(
			'post_type'      => 'page',
			'post_title'     => ROBOMETRIA_R2_TITULO,
			'post_name'      => ROBOMETRIA_R2_SLUG,
			'post_content'   => $conteudo,
			'post_status'    => 'publish',
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		), true );
		if ( is_wp_error( $pid ) ) {
			return;
		}
		update_post_meta( $pid, '_robometria_casca', '1' );
		update_post_meta( $pid, '_robometria_id', ROBOMETRIA_R2_SLUG );
		flush_rewrite_rules( false );
	} else {
		$pid = (int) $pagina->ID;
		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
		}
		/* Só repomos o shortcode em página que é nossa: página editada à mão
		   pelo Raphael não é reescrita por snippet. */
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& false === strpos( (string) $pagina->post_content, $conteudo ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $conteudo ) );
		}
	}

	update_option( 'robometria_r2_estrutura', ROBOMETRIA_R2_VERSAO, false );
}
}

if ( ! function_exists( 'robometria_r2_boot' ) ) {
function robometria_r2_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;
	robometria_r2_garantir_pagina();
}
}

add_action( 'init', 'robometria_r2_boot', 22 );

if ( did_action( 'init' ) ) {
	robometria_r2_boot();
}

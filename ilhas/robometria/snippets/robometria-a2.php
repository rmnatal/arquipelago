/**
 * Robometria A2 — Quantos m² um robô aspirador limpa por carga
 * Versão: 1.0.0 (10/09/2026) — Bloco 5 da fila, pareado com a R2 e nascido na
 * MESMA execução que ela, como o PROMPT.md desta ilha manda.
 *
 * O artigo-âncora do eixo de dimensionamento. A R2 responde à pergunta com a
 * casa da pessoa dentro ("quantos Pa e quantos ciclos para os meus m²"); este
 * artigo responde à pergunta anterior a ela, e que é de outra natureza: **de
 * onde vem o número de m² que os sites publicam.**
 *
 * ---------------------------------------------------------------------------
 * AS TRÊS DECISÕES QUE O BLOCO 5 FIXOU NO A1, e como cada uma aparece aqui
 * ---------------------------------------------------------------------------
 *
 * 1. A TESE É DERIVADA, NUNCA DIGITADA. As três afirmações deste artigo são
 *    contagens — quantos fabricantes declaram área por carga, quantos modelos
 *    têm os três números que a conta de tempo exige, e quanto as taxas
 *    implícitas divergem entre si. Cada uma tem mais de uma forma, escolhida
 *    pela própria contagem. Um artigo cuja tese é um número e que traz esse
 *    número digitado dentro do HTML passa a mentir em silêncio no dia em que o
 *    banco cresce — e "em silêncio" é o ponto: ninguém relê artigo publicado.
 *
 * 2. A DESCRIÇÃO DO JSON-LD E A RESPOSTA DO FAQPage SÃO PARTE DA TESE, não
 *    embrulho. Numa ilha cuja seção 5 do ARQUIPELAGO.md diz que ser recomendado
 *    pela IA vale tanto quanto ranquear, contradizer-se no canal que a IA lê é
 *    pior do que na tela. Aqui os três lugares saem do mesmo arquivo de fatos, e
 *    ferramentas/teste-a2.php exige que cada número de cada resposta do FAQPage
 *    apareça no corpo servido — não só dentro do próprio JSON-LD, que foi o
 *    engano que a verificação da R2 descobriu em si mesma nesta execução.
 *
 * 3. O ARTIGO NÃO REPETE A FERRAMENTA. Sem formulário: a consulta é da R2, e
 *    duas páginas respondendo a mesma coisa competem entre si no índice (seção
 *    14.4). Este artigo conta o catálogo; a R2 calcula a casa.
 *
 * ---------------------------------------------------------------------------
 * A SERP DESTA CONSULTA NÃO FOI VERIFICADA NESTA EXECUÇÃO, e a página diz isso
 * ---------------------------------------------------------------------------
 *
 * A seção 14.9 do ARQUIPELAGO.md manda classificar a SERP antes de criar a
 * página, e manda escrever "não verifiquei" em vez de inventar diagnóstico. O
 * egresso desta nuvem alcança apenas os domínios das ilhas e não houve busca web
 * nesta execução. Então vale a classificação herdada da seção 2.1 da
 * especificação, de 09/09/2026: a CABEÇA desta família ("o que é Pa", "quantos
 * m² um robô limpa") está tomada por veículo grande e a Robometria não a
 * disputa; este artigo mira a pergunta de PROCEDÊNCIA do número, que nenhuma
 * daquelas páginas responde. O campo `serp` de dados/a2-fatos.json guarda isso
 * por escrito.
 *
 * Regras herdadas: sem "<?php" no topo; nenhuma superglobal de servidor; nenhum
 * <script> nem <style> dentro do retorno do shortcode; toda função de nível
 * superior dentro de if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'ROBOMETRIA_A2_VERSAO' ) ) {
	define( 'ROBOMETRIA_A2_VERSAO', '1.0.0' );
	define( 'ROBOMETRIA_A2_SLUG', 'quantos-m2-o-robo-aspirador-limpa-por-carga' );
	define( 'ROBOMETRIA_A2_TITULO', 'Quantos m² um robô aspirador limpa por carga' );
	define( 'ROBOMETRIA_A2_DADOS', 'robometria_dados_a2-fatos' );
}

/* ---------------------------------------------------------------------------
 * 1. Os dados
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a2_dados' ) ) {
function robometria_a2_dados() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}

	$d = get_option( ROBOMETRIA_A2_DADOS );
	$d = apply_filters( 'robometria_a2_dados', $d );

	if ( ! is_array( $d ) || empty( $d['resumo'] ) || empty( $d['perguntas'] ) ) {
		$cache = array();
		return $cache;
	}

	$cache = $d;
	return $cache;
}
}

if ( ! function_exists( 'robometria_a2_n' ) ) {
function robometria_a2_n( $v ) {
	return number_format_i18n( (float) $v );
}
}

if ( ! function_exists( 'robometria_a2_dec' ) ) {
function robometria_a2_dec( $v ) {
	return number_format_i18n( (float) $v, 2 );
}
}

/** Lista em português: "a, b e c". Contador solto denuncia texto de máquina. */
if ( ! function_exists( 'robometria_a2_lista' ) ) {
function robometria_a2_lista( $itens ) {
	$itens = array_values( array_filter( (array) $itens ) );
	$n     = count( $itens );
	if ( 0 === $n ) {
		return '';
	}
	if ( 1 === $n ) {
		return $itens[0];
	}
	$ultimo = array_pop( $itens );
	return implode( ', ', $itens ) . ' e ' . $ultimo;
}
}

/* ---------------------------------------------------------------------------
 * 2. As três teses, cada uma com o molde escolhido pela contagem
 *
 * Nenhum número abaixo está digitado. Se a coleta trouxer amanhã a recarga de um
 * modelo que já declara cobertura, a terceira tese muda de forma sozinha — e o
 * teste de bancada reprova a página antes de ela ir ao ar dizendo o que o banco
 * deixou de sustentar.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a2_tese_da_area' ) ) {
function robometria_a2_tese_da_area() {
	$d = robometria_a2_dados();
	$r = $d['resumo'];

	if ( 0 === (int) $r['com_cobertura'] ) {
		return sprintf(
			'Nenhum dos %s modelos de robô aspirador deste banco tem área por carga declarada pelo fabricante. Todo número de m² que circula sobre eles foi calculado por terceiros a partir dos minutos de autonomia.',
			robometria_a2_n( $r['modelos_publicaveis'] )
		);
	}

	if ( 1 === count( (array) $d['marcas_que_declaram'] ) ) {
		return sprintf(
			'Uma marca só declara. Dos %s modelos de robô aspirador deste banco, %s trazem área coberta por carga declarada pelo fabricante — e os %s são da %s. As outras %s marcas não publicam esse número em canal nenhum: declaram minutos, e algumas nem isso.',
			robometria_a2_n( $r['modelos_publicaveis'] ),
			robometria_a2_n( $r['com_cobertura'] ),
			robometria_a2_n( $r['com_cobertura'] ),
			$d['marcas_que_declaram'][0],
			robometria_a2_n( count( (array) $d['marcas_que_nao_declaram'] ) )
		);
	}

	return sprintf(
		'Poucas marcas declaram. Dos %s modelos de robô aspirador deste banco, %s trazem área coberta por carga declarada pelo fabricante, em %s marcas (%s). As outras %s não publicam esse número em canal nenhum.',
		robometria_a2_n( $r['modelos_publicaveis'] ),
		robometria_a2_n( $r['com_cobertura'] ),
		robometria_a2_n( count( (array) $d['marcas_que_declaram'] ) ),
		robometria_a2_lista( $d['marcas_que_declaram'] ),
		robometria_a2_n( count( (array) $d['marcas_que_nao_declaram'] ) )
	);
}
}

if ( ! function_exists( 'robometria_a2_tese_do_tempo' ) ) {
function robometria_a2_tese_do_tempo() {
	$d = robometria_a2_dados();
	$r = $d['resumo'];

	if ( 0 === (int) $r['com_os_tres'] ) {
		return sprintf(
			'A conta do tempo total precisa de três números declarados — área por carga, autonomia e tempo de recarga — e nenhum dos %s modelos deste banco tem os três. %s declaram a área, %s declaram a recarga, e os dois conjuntos não se encontram em modelo nenhum: quem publica um não publica o outro.',
			robometria_a2_n( $r['modelos_publicaveis'] ),
			robometria_a2_n( $r['com_cobertura'] ),
			robometria_a2_n( $r['com_recarga'] )
		);
	}

	return sprintf(
		'A conta do tempo total precisa de três números declarados — área por carga, autonomia e tempo de recarga — e %s dos %s modelos deste banco têm os três. Para eles a conta fecha com dado de fabricante; para os outros, qualquer tempo total publicado usou um número que ninguém declarou.',
		robometria_a2_n( $r['com_os_tres'] ),
		robometria_a2_n( $r['modelos_publicaveis'] )
	);
}
}

if ( ! function_exists( 'robometria_a2_tese_da_dispersao' ) ) {
function robometria_a2_tese_da_dispersao() {
	$d = robometria_a2_dados();

	if ( empty( $d['dispersao'] ) ) {
		return sprintf(
			'Este banco tem %s par (minutos, m²) declarado pelo próprio fabricante, e um ponto não é um coeficiente: com ele não se estima nada sobre um robô diferente.',
			robometria_a2_n( count( (array) $d['pares'] ) )
		);
	}

	$s = $d['dispersao'];

	if ( ! empty( $s['mesma_marca'] ) ) {
		return sprintf(
			'E os pares que existem discordam entre si. Os %s pares (minutos, m²) declarados deste banco são todos da mesma marca, e mesmo assim a taxa implícita vai de %s a %s m² por minuto — %s%% de diferença dentro do MESMO fabricante. Quem não é consistente consigo mesmo não sustenta uma taxa de mercado.',
			robometria_a2_n( count( (array) $d['pares'] ) ),
			robometria_a2_dec( $s['taxa_minima'] ),
			robometria_a2_dec( $s['taxa_maxima'] ),
			robometria_a2_n( $s['pct'] )
		);
	}

	return sprintf(
		'E os pares que existem discordam entre si. Entre os %s pares (minutos, m²) declarados deste banco, em %s marcas, a taxa implícita vai de %s a %s m² por minuto — %s%% de diferença. Aplicar uma média a um robô que não está nessa lista é dar ao leitor um número que nenhum fabricante sustenta.',
		robometria_a2_n( count( (array) $d['pares'] ) ),
		robometria_a2_n( count( (array) $s['marcas'] ) ),
		robometria_a2_dec( $s['taxa_minima'] ),
		robometria_a2_dec( $s['taxa_maxima'] ),
		robometria_a2_n( $s['pct'] )
	);
}
}

/* ---------------------------------------------------------------------------
 * 3. As tabelas — o catálogo contado, servido em HTML
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a2_tabela_pares' ) ) {
function robometria_a2_tabela_pares() {
	$d = robometria_a2_dados();
	if ( empty( $d['pares'] ) ) {
		return '';
	}

	$html  = '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>'
		. '<th>Modelo</th><th>Área por carga</th><th>Autonomia</th><th>Taxa implícita</th>'
		. '</tr></thead><tbody>';
	foreach ( $d['pares'] as $p ) {
		$html .= '<tr>';
		$html .= '<td>' . esc_html( $p['rotulo'] ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_a2_n( $p['cobertura_m2'] ) ) . ' m²</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_a2_n( $p['autonomia_min'] ) ) . ' min</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_a2_dec( $p['taxa'] ) ) . ' m²/min</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="rbm-nota">A taxa implícita da última coluna é <strong>nossa</strong>, não do fabricante: é a divisão dos dois números que ele declara. Ela está aqui para mostrar o espalhamento, e é justamente por causa desse espalhamento que ela não é usada em conta nenhuma desta ilha.</p>';
	return $html;
}
}

if ( ! function_exists( 'robometria_a2_tabela_tres_numeros' ) ) {
function robometria_a2_tabela_tres_numeros() {
	$d = robometria_a2_dados();
	$r = $d['resumo'];

	$linhas = array(
		array( 'Área coberta por carga', $r['com_cobertura'], 'sem ela não dá para saber quantos ciclos a sua casa exige' ),
		array( 'Autonomia em minutos', $r['com_autonomia'], 'é o número que quase todo anúncio traz, e sozinho ele não responde nada' ),
		array( 'Tempo de recarga', $r['com_recarga'], 'sem ele não dá para somar as paradas no meio do serviço' ),
		array( 'Os três, no mesmo modelo', $r['com_os_tres'], 'é aqui que a conta do tempo total fecharia' ),
	);

	$html = '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>'
		. '<th>O que a conta precisa</th><th>Modelos que declaram</th><th>Por que importa</th>'
		. '</tr></thead><tbody>';
	foreach ( $linhas as $l ) {
		$html .= '<tr>';
		$html .= '<td>' . esc_html( $l[0] ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_a2_n( $l[1] ) ) . ' de '
			. esc_html( robometria_a2_n( $r['modelos_publicaveis'] ) ) . '</td>';
		$html .= '<td>' . esc_html( $l[2] ) . '</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 4. A vitrine — e o cuidado de não a transformar num ranking que ela não é
 *
 * A lista é dos modelos cujo fabricante PUBLICA a área por carga. Isso é uma
 * informação de compra de verdade — com esse número dá para calcular ciclos, sem
 * ele não dá — mas NÃO é um ranking de qualidade de limpeza, e a página escreve
 * isso com todas as letras. A ordem é por área declarada, e o desempate é o
 * identificador: nunca a comissão, nunca quem tem link (seção 7).
 *
 * A porta de compra vem da casca e existe mesmo com afiliado.url vazio, porque
 * esconder o bloco enquanto o cano de links enche devolveria à procedência o
 * papel de única porta clicável — a cicatriz de 10/09/2026.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a2_vitrine' ) ) {
function robometria_a2_vitrine() {
	$d = robometria_a2_dados();
	if ( empty( $d['vitrine'] ) ) {
		/* Bloco vazio é PORTÃO, não defeito — mas silêncio parece defeito, então
		   a página diz por quê (seção 7). */
		return '<div class="rbm-secao"><h2>Onde comprar</h2><p>Nenhum modelo deste banco tem área por carga declarada pelo fabricante hoje, então não há o que listar aqui — e listar assim mesmo seria recomendar pelo que não sabemos.</p></div>';
	}

	$itens    = $d['vitrine'];
	$total    = count( $itens );
	$sem_link = 0;
	foreach ( $itens as $i ) {
		if ( empty( $i['afiliado']['url'] ) ) {
			$sem_link++;
		}
	}

	$html  = '<div class="rbm-secao rbm-compra"><h2>Os modelos cujo fabricante publica o número</h2>';
	$html .= '<p>São os <span class="rbm-num">' . esc_html( robometria_a2_n( $total ) )
		. '</span> modelos deste banco sobre os quais a pergunta do título tem resposta do próprio fabricante. <strong>Isto não é um ranking de limpeza</strong> — é a lista de quem publica a área por carga, que é o número sem o qual nenhuma conta de tempo começa.</p>';

	$html .= '<p class="rbm-aviso-comissao">Os botões de compra abaixo são links de afiliado: se você comprar por eles, a Robometria pode receber comissão, sem custo a mais para você. Isso não muda a ordem da lista — ela é decidida pela área que o fabricante declara, e só por isso. '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Como isto funciona' )
			: 'Veja a página de divulgação de afiliados' ) . '.</p>';

	if ( $sem_link > 0 ) {
		if ( $sem_link === $total ) {
			$quantas = ( 1 === $total )
				? 'Este modelo ainda não tem link de loja'
				: 'Nenhum destes modelos tem link de loja ainda';
		} else {
			$quantas = ( 1 === $sem_link )
				? 'Um destes modelos ainda não tem link de loja'
				: sprintf( '%s destes modelos ainda não têm link de loja', robometria_a2_n( $sem_link ) );
		}
		$html .= '<p class="rbm-nota">' . esc_html( $quantas )
			. '. O lugar fica reservado assim mesmo: esconder o bloco enquanto o link não chega devolveria ao link de procedência o papel de única porta clicável da página.</p>';
	}

	$html .= '<ul class="rbm-vitrine">';
	foreach ( $itens as $i ) {
		$html .= '<li class="rbm-vitrine-item">';
		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true"><span class="rbm-vitrine-vazia"></span></span>';
		$html .= '<span class="rbm-vitrine-tipo">' . esc_html( $i['rotulo'] ) . '</span>';
		$html .= '<span class="rbm-vitrine-nome rbm-num">'
			. esc_html( robometria_a2_n( $i['cobertura_m2'] ) . ' m² por carga' ) . '</span>';

		/* A ESPECIFICAÇÃO QUE FEZ O PRODUTO ENTRAR (seção 6), e a ressalva junto:
		   declarar a área não é a mesma coisa que a conta fechar. */
		$porque = sprintf(
			'O fabricante declara %s m² por carga',
			robometria_a2_n( $i['cobertura_m2'] )
		);
		if ( null !== $i['autonomia_min'] ) {
			$porque .= sprintf( ' e %s minutos de autonomia', robometria_a2_n( $i['autonomia_min'] ) );
		}
		$porque .= '. ';
		if ( null === $i['recarga_min'] ) {
			$porque .= 'Não declara quanto tempo a recarga leva, então o tempo total até a casa ficar pronta continua sem conta fechada.';
		} else {
			$porque .= sprintf( 'Declara também %s minutos de recarga, e por isso a conta de tempo fecha para este modelo.',
				robometria_a2_n( $i['recarga_min'] ) );
		}
		if ( true !== $i['retoma_apos_recarga'] ) {
			$porque .= ' E não declara se ele retoma de onde parou depois de recarregar — sem isso a conta de mais de um ciclo não se sustenta.';
		}
		$html .= '<span class="rbm-vitrine-porque">' . esc_html( $porque ) . '</span>';

		$html .= '<span class="rbm-vitrine-acao">'
			. ( function_exists( 'robometria_casca_porta_de_compra' )
				? robometria_casca_porta_de_compra( $i )
				: '<span class="rbm-sem-loja">Link de loja em breve</span>' )
			. '</span>';
		$html .= '</li>';
	}
	$html .= '</ul></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 5. O shortcode
 * ------------------------------------------------------------------------- */

add_shortcode( 'robometria_a2', function () {
	$d = robometria_a2_dados();

	if ( empty( $d['resumo'] ) ) {
		return '<div class="rbm-bloco"><p class="rbm-linha-mestra">Este artigo está sem o banco de modelos no momento.</p>'
			. '<p class="rbm-nota">A tese deste texto é uma contagem do banco publicado a partir do repositório da Robometria. Sem o banco, preferimos avisar a servir um texto cujos números não podem ser conferidos.</p></div>';
	}

	$r = $d['resumo'];

	$html = '<div class="rbm-bloco rbm-artigo">';

	/* RESPOSTA ANTES DA EXPLICAÇÃO (seção 5.2): a tese inteira na primeira dobra,
	   em frase autossuficiente que sobrevive a ser citada fora de contexto. */
	$html .= '<div class="rbm-abertura">';
	$html .= '<p class="rbm-linha-mestra">' . esc_html( robometria_a2_tese_da_area() ) . '</p>';
	$html .= '<p>' . esc_html( robometria_a2_tese_do_tempo() ) . '</p>';
	$html .= '<p>' . esc_html( robometria_a2_tese_da_dispersao() ) . '</p>';
	$html .= '</div>';

	/* -------------------------------------------------- o que o catálogo mostra */
	$html .= '<div class="rbm-secao"><h2>Os pares que o fabricante realmente declara</h2>';
	/* A contagem sai da LISTA, e nunca do resumo: o resumo tem um campo
	   `pares_declarados` que diz a mesma coisa, e duas contagens da mesma coisa
	   divergem em silêncio no dia em que uma das duas for atualizada sozinha. A
	   tese da dispersão também conta a lista, então há uma fonte só. */
	$html .= '<p>Um par é um modelo em que o fabricante publica <strong>os dois</strong> números: a área que ele cobre numa carga e quantos minutos essa carga dura. É o único material a partir do qual alguém poderia estimar qualquer coisa — e são <span class="rbm-num">'
		. esc_html( robometria_a2_n( count( (array) $d['pares'] ) ) ) . '</span> em <span class="rbm-num">'
		. esc_html( robometria_a2_n( $r['modelos_publicaveis'] ) ) . '</span> modelos.</p>';
	$html .= robometria_a2_tabela_pares();
	$html .= '</div>';

	/* ------------------------------------------------------ os três números */
	$html .= '<div class="rbm-secao"><h2>Por que ninguém consegue dizer quanto tempo o robô leva</h2>';
	$html .= '<p>A pergunta que a pessoa faz não é "quantos minutos dura a bateria" — é <strong>quando a casa fica limpa</strong>. Para responder isso é preciso somar os ciclos e as recargas no meio, e a soma pede três números que o fabricante teria que declarar.</p>';
	$html .= robometria_a2_tabela_tres_numeros();
	if ( ! empty( $d['com_recarga_ids'] ) ) {
		$nomes = array();
		foreach ( $d['com_recarga_ids'] as $m ) {
			$nomes[] = $m['rotulo'];
		}
		$html .= '<p>Os modelos que declaram recarga são ' . esc_html( robometria_a2_lista( $nomes ) )
			. ' — e nenhum deles declara área por carga. É por isso que a linha da última coluna dá <span class="rbm-num">'
			. esc_html( robometria_a2_n( $r['com_os_tres'] ) )
			. '</span>: os dois conjuntos não se encontram.</p>';
	}
	$html .= '</div>';

	/* ------------------------------------------------------------- a vitrine */
	$html .= robometria_a2_vitrine();

	/* --------------------------------------------------- como foi feito */
	$html .= '<div class="rbm-secao"><h2>Como esta página foi montada</h2>';
	$html .= '<p><strong>Nenhuma das páginas de fabricante deste banco foi lida diretamente.</strong> O acesso direto a esses endereços está bloqueado no ambiente em que a Robometria é construída, e tudo foi colhido por busca restrita ao domínio da própria fonte. Cada número traz o endereço da declaração para você conferir, e não para você acreditar.</p>';
	$html .= '<p>Os números deste texto não estão escritos dentro dele: são recontados do banco a cada publicação. Se um fabricante passar a declarar área por carga amanhã, é a frase de abertura que muda — não um parágrafo que alguém teria que lembrar de reescrever.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'metodologia', 'A metodologia completa, com a escada de fontes' )
		: 'A metodologia completa, com a escada de fontes' ) . ' &middot; '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
			: 'Divulgação de afiliados' ) . '</p>';
	$html .= '</div>';

	/* MALHA (seção 9): três irmãs e mão dupla. Este artigo aponta para a
	   ferramenta que ele apoia, para a outra ferramenta da ilha e para o outro
	   artigo — e as três apontam de volta. */
	$html .= '<div class="rbm-leia-tambem">';
	$html .= '<h2>Leia também</h2>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'quantos-pa-o-robo-aspirador-precisa', 'Quantos Pa e quantos ciclos a sua casa exige' )
		: 'Quantos Pa e quantos ciclos a sua casa exige' )
		. ' — este texto conta o catálogo; a ferramenta faz a conta com a sua metragem dentro.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'qual-peca-serve-no-meu-robo-aspirador', 'Qual peça de reposição o fabricante declara para o seu modelo' )
		: 'Qual peça de reposição o fabricante declara para o seu modelo' )
		. ' — a mesma pergunta de procedência, do outro lado do robô.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'filtro-universal-de-robo-aspirador', 'Por que não existe filtro universal de robô aspirador' )
		: 'Por que não existe filtro universal de robô aspirador' )
		. ' — a outra contagem do catálogo desta ilha.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 6. Cabeça da página: JSON-LD e canônica
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a2_na_pagina' ) ) {
function robometria_a2_na_pagina() {
	$forcado = apply_filters( 'robometria_a2_na_pagina', null );
	if ( null !== $forcado ) {
		return (bool) $forcado;
	}
	if ( ! function_exists( 'is_page' ) ) {
		return false;
	}
	return is_page( ROBOMETRIA_A2_SLUG );
}
}

if ( ! function_exists( 'robometria_a2_url_da_pagina' ) ) {
function robometria_a2_url_da_pagina() {
	if ( function_exists( 'robometria_casca_url_se_existir' ) ) {
		$url = robometria_casca_url_se_existir( ROBOMETRIA_A2_SLUG );
		if ( '' !== $url ) {
			return $url;
		}
	}
	return home_url( '/' . ROBOMETRIA_A2_SLUG . '/' );
}
}

add_action( 'wp_head', function () {
	if ( ! robometria_a2_na_pagina() ) {
		return;
	}

	$d = robometria_a2_dados();
	if ( empty( $d['resumo'] ) ) {
		return;
	}

	$url = robometria_a2_url_da_pagina();
	$r   = $d['resumo'];

	/* A DESCRIÇÃO É PARTE DA TESE, não embrulho: ela é a mesma frase derivada que
	   abre a página. Marcação que afirma o que a página deixou de afirmar é pior
	   do que marcação nenhuma, porque é justamente ela que um modelo de
	   linguagem lê como resposta (seção 5 do ARQUIPELAGO.md). */
	$artigo = array(
		'@type'            => 'Article',
		'@id'              => $url . '#artigo',
		'headline'         => ROBOMETRIA_A2_TITULO,
		'url'              => $url,
		'inLanguage'       => 'pt-BR',
		'description'      => robometria_a2_tese_da_area(),
		'articleSection'   => 'Dimensionamento',
		'dateModified'     => isset( $d['gerado_em'] ) ? $d['gerado_em'] : '',
		'publisher'        => array( '@id' => home_url( '/#organizacao' ) ),
		'isBasedOn'        => array(
			'@type'       => 'Dataset',
			'name'        => 'Banco de modelos de robô aspirador da Robometria',
			'description' => sprintf(
				'%d modelos publicáveis em %d marcas, com o que cada fabricante declara sobre área por carga, autonomia e recarga.',
				$r['modelos_publicaveis'], $r['marcas']
			),
		),
	);

	$perguntas = array();
	foreach ( (array) $d['perguntas'] as $p ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $p['pergunta'],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p['resposta'] ),
		);
	}

	$grafo = array( '@context' => 'https://schema.org', '@graph' => array( $artigo ) );
	if ( $perguntas ) {
		$grafo['@graph'][] = array(
			'@type'      => 'FAQPage',
			'@id'        => $url . '#perguntas',
			'inLanguage' => 'pt-BR',
			'mainEntity' => $perguntas,
		);
	}

	echo '<script type="application/ld+json" id="robometria-a2-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
	echo '<link rel="canonical" href="' . esc_url( $url ) . '">' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * 7. Estilo próprio do artigo
 *
 * A folha da vitrine vem da casca, que é dona dela. Aqui fica só o que é do
 * texto: largura de leitura e a tabela que rola sozinha no celular sem levar a
 * página junto — a seção 6 do contrato não admite rolagem horizontal na página.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! robometria_a2_na_pagina() ) {
		return;
	}

	$css = <<<'CSS'
.rbm-artigo p{max-width:44rem;}
.rbm-artigo .rbm-abertura p:first-child{max-width:46rem;}
.rbm-artigo .rbm-secao h2{margin:0 0 .6rem;}
.rbm-artigo .rbm-nota{color:var(--rbm-legenda);font-size:.92rem;}
.rbm-leia-tambem{margin:2.4rem 0 0;padding-top:1.4rem;border-top:1px solid var(--rbm-traco);}
.rbm-leia-tambem h2{margin:0 0 .5rem;font-size:1.15rem;}
CSS;

	if ( function_exists( 'robometria_casca_css_vitrine' ) ) {
		$css = robometria_casca_css_vitrine() . "\n" . $css;
	}

	echo '<style id="robometria-a2">' . $css . '</style>' . "\n";
}, 21 );

/* ---------------------------------------------------------------------------
 * 8. O cartão no catálogo de artigos, e a página
 * ------------------------------------------------------------------------- */

add_filter( 'robometria_artigos', function ( $lista ) {
	$lista[] = array(
		'codigo'     => 'A2',
		'titulo'     => ROBOMETRIA_A2_TITULO,
		'slug'       => ROBOMETRIA_A2_SLUG,
		'ferramenta' => 'Quantos Pa e quanto tempo o seu robô precisa',
		'resumo'     => 'O número de m² que os sites publicam quase nunca é do fabricante. A contagem do catálogo mostra quantas marcas declaram área por carga, quantos modelos têm os três números que a conta de tempo exige, e o quanto as taxas implícitas divergem entre si.',
	);
	return $lista;
} );

if ( ! function_exists( 'robometria_a2_garantir_pagina' ) ) {
function robometria_a2_garantir_pagina() {
	$feita = get_option( 'robometria_a2_estrutura' );
	if ( ROBOMETRIA_A2_VERSAO === $feita ) {
		return;
	}

	$conteudo = '[robometria_a2]';
	$pagina   = get_page_by_path( ROBOMETRIA_A2_SLUG, OBJECT, 'page' );

	if ( ! $pagina ) {
		$pid = wp_insert_post( array(
			'post_type'      => 'page',
			'post_title'     => ROBOMETRIA_A2_TITULO,
			'post_name'      => ROBOMETRIA_A2_SLUG,
			'post_content'   => $conteudo,
			'post_status'    => 'publish',
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		), true );
		if ( is_wp_error( $pid ) ) {
			return;
		}
		update_post_meta( $pid, '_robometria_casca', '1' );
		update_post_meta( $pid, '_robometria_id', ROBOMETRIA_A2_SLUG );
		flush_rewrite_rules( false );
	} else {
		$pid = (int) $pagina->ID;
		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
		}
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& false === strpos( (string) $pagina->post_content, $conteudo ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $conteudo ) );
		}
	}

	update_option( 'robometria_a2_estrutura', ROBOMETRIA_A2_VERSAO, false );
}
}

if ( ! function_exists( 'robometria_a2_boot' ) ) {
function robometria_a2_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;
	robometria_a2_garantir_pagina();
}
}

add_action( 'init', 'robometria_a2_boot', 23 );

if ( did_action( 'init' ) ) {
	robometria_a2_boot();
}

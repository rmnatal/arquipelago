<?php
/**
 * RODAMETRIA F3 — "AGUENTA O MEU PESO?"
 *
 * A TERCEIRA E ULTIMA DAS TRES FERRAMENTAS QUE ESTA ILHA EXISTE PARA TER. A F2
 * esta no ar desde 29/10/2026 e a F1 desde 06/11/2026 pela manha; esta nasceu
 * na tarde do mesmo dia.
 *
 * ESTE ARQUIVO E TRADUTOR, frase a frase, de `regras/f3.py`. Nenhum numero e
 * nenhuma frase de resposta e digitado aqui: tudo vem da option que o Sync
 * grava de `dados/f3-respostas.json`, escrito por `ferramentas/gerar-f3.py` a
 * partir de `regras/f3.py` e de `dados/constantes.json`. O motivo esta na
 * secao 8 do ARQUIPELAGO.md: a regra da DECISAO se escreve duas vezes de
 * proposito, e o FATO EXTERNO mora num lugar so.
 *
 * O QUE SEPARA ESTA FERRAMENTA DAS DUAS IRMAS, e e por isso que ela pode ir ao
 * ar hoje: A RESPOSTA PRINCIPAL NAO DEPENDE DO BANCO. Dado o peso de quem
 * pilota e o que ele carrega, a carga maxima a procurar sai de
 * `total x (1 + margem)` — aritmetica sobre a entrada da pessoa mais UMA
 * constante desta ilha. A vitrine e a segunda camada, e hoje ela esta VAZIA
 * por um motivo que a pagina NOMEIA com os numeros contados: os tres registros
 * do banco que declaram carga maxima declaram 120 kg, os tres lidos em ficha de
 * varejo grande, e NENHUM dos tres tem oferta aberta — pela 25.2 item sem piso
 * de compra nao entra em vitrine.
 *
 * A VIRADA QUE A TABELA PRE-RENDERIZADA PUBLICA E A TESE DESTA ILHA: com a
 * folga de 10%, 109 kg e o ultimo peso total que os 120 kg do teto de varejo
 * acolhem, e 110 kg ja nao. A pessoa do `VOZ.md` — "o patinete aguenta 100 kg,
 * voce e a mochila dao 108" — cabe por um quilo, e e por isso que o caso de
 * exemplo desta pagina e ela e nao um caso que passa folgado (32.1 item 4).
 *
 * 1.0.0 (06/11/2026) — a F3 nasce, com os campos ja prefixados pela 32.1-b e
 * com o `<noscript>` pelo componente da casca. Ela e a primeira ferramenta
 * desta ilha a nascer DENTRO do conserto da 32.1-b, que e exatamente o que a
 * regra pede ao mandar o componente morar na casca.
 */

if ( ! defined( 'RODAMETRIA_F3_VERSAO' ) ) {
	define( 'RODAMETRIA_F3_VERSAO', '1.4.0' );
}

/* A VERSAO DESTE SNIPPET VAI AO AR (20.7). A CHAVE E O `id` DO manifest.json, e
 * o que esta linha mede e a ATIVACAO e nao o byte: snippet gravado e NAO
 * ATIVADO (a 20.4) nao roda, este filtro nao e pendurado, e o `id` SIMPLESMENTE
 * NAO APARECE no /casca. A ausencia e o sinal. */
add_filter( 'rodametria_versoes', function ( $v ) {
	$v['rodametria-f3'] = RODAMETRIA_F3_VERSAO;

	return $v;
} );

if ( ! defined( 'RODAMETRIA_F3_SLUG' ) ) {
	/* A URL carrega a consulta MEDIDA do eixo C do corpus
	   (`patinete eletrico peso maximo suportado`, bloco 1, 28/10/2026), e nao
	   a pergunta do H1. Pela 32.3 ela nao muda mais depois de publicada. */
	define( 'RODAMETRIA_F3_SLUG', 'peso-maximo-patinete-eletrico' );
}

if ( ! defined( 'RODAMETRIA_ID_DADOS_F3' ) ) {
	define( 'RODAMETRIA_ID_DADOS_F3', 'f3-respostas' );
}

/* A pagina entra no mapa da casca por filtro: a casca nao conhece o nome dela
   (32.6-b — a casca nao cresce quando a ilha cresce). */
add_filter( 'rodametria_paginas', function ( $mapa ) {
	$mapa[ RODAMETRIA_F3_SLUG ] = array(
		'nome'    => 'Carga máxima',
		'titulo'  => 'Peso máximo suportado por patinete elétrico — quanto você precisa',
		'tipo'    => 'ferramenta',
		'pai'     => 'inicio',
		'no_menu' => false,
		/* 160 e o teto que o portao de ar cobra (item 5 do despacho de 30/10).
		   E ela PROMETE O QUE A PAGINA ENTREGA: a carga minima a procurar, que
		   nao depende do banco. Nao promete vitrine, porque a vitrine esta
		   vazia — descricao que promete o que a primeira tela recusa e a
		   pagina se desdizendo na propria aba, e foi o defeito que a F1
		   consertou na `description` dela hoje de manha. */
		'description' => 'Diga o seu peso e o que você carrega: a conta devolve a carga '
			. 'máxima que o patinete precisa declarar na ficha, com a folga que a gente '
			. 'exige e o motivo dela.',
	);

	return $mapa;
} );

if ( ! function_exists( 'rodametria_f3_na_pagina' ) ) {
function rodametria_f3_na_pagina() {
	return rodametria_casca_slug_atual() === RODAMETRIA_F3_SLUG;
}
}

if ( ! function_exists( 'rodametria_f3_url' ) ) {
function rodametria_f3_url() {
	return home_url( '/' . RODAMETRIA_F3_SLUG . '/' );
}
}

/** Numero em portugues. NENHUMA conta mora aqui: so a forma. */
if ( ! function_exists( 'rodametria_f3_numero' ) ) {
function rodametria_f3_numero( $v ) {
	$f = (float) $v;
	if ( $f === floor( $f ) ) {
		return number_format( $f, 0, ',', '.' );
	}

	return rtrim( rtrim( number_format( $f, 1, ',', '.' ), '0' ), ',' );
}
}

/* ---------------------------------------------------------------------------
 * O FORMULARIO (32.1, item 3) — JA PREENCHIDO com o caso de exemplo.
 *
 * OS NOMES DOS CAMPOS CARREGAM O PREFIXO DA ILHA (32.1-b), e esta ferramenta e
 * a primeira a nascer com eles. O motivo nao e arrumacao: o formulario e
 * `method="get"` para a propria pagina e o JavaScript e quem chama
 * `preventDefault()`, entao a URL que o botao monta e uma pagina de verdade. Um
 * campo chamado `peso` ou `carga` nao colide com query var do WordPress HOJE —
 * foi medido —, mas a lista reservada tem mais de trinta nomes curtos e muda
 * com a versao. Prefixo proprio torna a classe inteira impossivel.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_formulario_html' ) ) {
function rodametria_f3_formulario_html( $d ) {
	$ex = $d['campos']['exemplo'];

	$html  = '<form class="rdm-f-formulario rdm-f3" data-rdm-f3-form'
		. ' method="get" action="' . esc_url( rodametria_f3_url() ) . '">';
	$html .= '<div class="rdm-f-campos">';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f3-peso">Seu peso</label>'
		. '<input id="rdm-f3-peso" name="rdm_peso" type="number" inputmode="numeric"'
		. ' min="' . esc_attr( (int) $d['campos']['peso_minimo_kg'] ) . '"'
		. ' max="' . esc_attr( (int) $d['campos']['peso_maximo_kg'] ) . '"'
		. ' step="1" value="' . esc_attr( (int) $ex['peso_piloto_kg'] ) . '" data-rdm-f3-peso>'
		. '<span class="rdm-f-dica">Em kg, só você</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f3-carga">O que você carrega</label>'
		. '<input id="rdm-f3-carga" name="rdm_carga" type="number" inputmode="numeric"'
		. ' min="0" max="' . esc_attr( (int) $d['campos']['carga_maxima_kg'] ) . '"'
		. ' step="1" value="' . esc_attr( (int) $ex['carga_kg'] ) . '" data-rdm-f3-carga>'
		. '<span class="rdm-f-dica">Mochila, compras, capacete — 0 se não leva nada</span></p>';

	$html .= '</div>';
	$html .= '<p class="rdm-f-acao"><button class="rdm-f-botao" type="submit">'
		. 'Ver de quanto eu preciso</button></p>';
	$html .= '</form>';

	return $html;
}
}

/**
 * O AVISO DE JAVASCRIPT DESLIGADO (32.1-b). A FORMA vem da casca (32.6-b); o
 * TEXTO e desta pagina, porque o que ela oferece a quem esta sem JavaScript —
 * a tabela de pesos ja calculados — e dela. OS NUMEROS SAEM DO BANCO.
 */
if ( ! function_exists( 'rodametria_f3_noscript_html' ) ) {
function rodametria_f3_noscript_html( $d ) {
	$ex = $d['campos']['exemplo'];

	return rodametria_casca_noscript( array(
		'A conta responde no seu navegador. Com o JavaScript desligado, o botão '
		. 'recarrega a página e a resposta abaixo continua sendo a do exemplo já '
		. 'preenchido no formulário — '
		. rodametria_f3_numero( $ex['peso_piloto_kg'] ) . ' kg de pessoa e '
		. rodametria_f3_numero( $ex['carga_kg'] ) . ' kg de carga. A tabela '
		. '“Já calculado para outros pesos”, mais abaixo, responde sem precisar de '
		. 'conta: ela traz a carga mínima de cada peso, inclusive o seu.',
	) );
}
}

/* ---------------------------------------------------------------------------
 * A CAIXA DE RESULTADO (32.1, item 4), JA PRE-RENDERIZADA.
 *
 * O numero e a carga minima recomendada — a resposta que nao depende do banco.
 * O rotulo e MOLDE e nao literal, porque ele aparece em TRES lugares (a caixa,
 * a barra fixa do telefone e a recomputacao do navegador) e literal repetido em
 * tres lugares diverge em dois deles.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_resultado_html' ) ) {
function rodametria_f3_resultado_html( $d ) {
	$r = $d['resposta_exemplo'];
	$m = $d['frases_molde'];

	$frases = array( $r['frase_precisa'], $r['frase_margem'] );

	return rodametria_casca_caixa(
		$m['rotulo_precisa'], $r['carga_minima_tela'], 'kg', $frases, 'verde',
		' data-rdm-f3-caixa' )
		. rodametria_casca_barra_fixa( $m['rotulo_precisa'], $r['carga_minima_tela'], 'kg' );
}
}

/* ---------------------------------------------------------------------------
 * OS TRES GRUPOS DA 3.2, NA ORDEM EM QUE A PAGINA OS SERVE.
 *
 * A ORDEM E REGRA E NAO ARRUMACAO: a 3.2 e literal ao dizer que o grupo do
 * meio "nunca aparece em primeiro lugar", porque a secao 7 chama de defeito
 * GRAVE recomendar em primeiro lugar um produto que a propria pagina diz nao
 * servir. A ordem sai de `grupos_em_ordem` do banco, nunca escrita aqui.
 *
 * O CONTEINER EXISTE NO HTML MESMO VAZIO, porque e nele que o navegador
 * reescreve os grupos quando a pessoa troca o peso.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_grupos_html' ) ) {
function rodametria_f3_grupos_html( $d ) {
	$r = $d['resposta_exemplo'];
	$m = $d['frases_molde'];

	$titulo_do_grupo = array(
		'folga'       => $m['titulo_folga'],
		'no_limite'   => $m['titulo_no_limite'],
		'nao_aguenta' => $m['titulo_nao_aguenta'],
	);

	$html = '<div class="rdm-f3-grupos" data-rdm-f3-grupos>';

	foreach ( (array) $d['grupos_em_ordem'] as $g ) {
		$linhas = isset( $r['linhas'][ $g ] ) ? (array) $r['linhas'][ $g ] : array();
		if ( ! $linhas ) {
			continue;
		}
		$html .= '<h3 class="rdm-f3-grupo-titulo">'
			. esc_html( $titulo_do_grupo[ $g ] ) . '</h3>';
		$html .= '<ul class="rdm-f3-lista">';
		foreach ( $linhas as $l ) {
			$html .= '<li>' . esc_html( $l['frase'] ) . '</li>';
		}
		$html .= '</ul>';

		/* A RESSALVA SOURCED DA 3.4 vem logo DEPOIS do grupo do meio, e so
		   quando ele existe: a pagina avisando sobre um grupo que ela nao
		   mostra seria a pagina se desdizendo. */
		if ( 'no_limite' === $g ) {
			foreach ( (array) $r['frases_ressalva'] as $f ) {
				$html .= '<p class="rdm-f3-ressalva">' . esc_html( $f ) . '</p>';
			}
		}
	}

	/* A CAUSA DE LISTA VAZIA NAO MORA AQUI, E ISSO FOI MEDIDO NO AR EM
	   06/11/2026, LENDO A PAGINA. Ela moro aqui ate a primeira leitura: o
	   paragrafo de 300 caracteres saia DUAS VEZES na mesma pagina — uma como
	   causa do bloco de compra vazio e outra logo abaixo, neste bloco —, e as
	   duas eram byte por byte a mesma frase.
	   E O DEFEITO ERA MEU, no mesmo arquivo em que eu acabara de consertar o
	   gemeo dele na casca: a afirmacao de ar que escrevi compara os dois
	   paragrafos DENTRO do bloco de compra, e esta duplicata atravessa dois
	   blocos. Um fato, um lugar (20.7): a causa mora no BLOCO DE COMPRA, que e
	   quem precisa explicar por que nao ha o que comprar, e e la que o
	   navegador a reescreve. Este bloco fica com o que e dele — os grupos e os
	   nomes. */

	/* E OS NOMES DE QUEM SERVIRIA E NAO TEM LINK, porque a secao 7 manda
	   nomear em vez de sumir — e a frase de vazio acima aponta para eles. */
	$servem = isset( $d['compra']['serviriam_sem_oferta'] )
		? (array) $d['compra']['serviriam_sem_oferta'] : array();
	if ( $servem ) {
		/* ROTULO PROPRIO, e nao o da prestacao de contas: os dois blocos mostram
		   os mesmos nomes por motivos diferentes (aqui, a carga de cada um;
		   la, a conta que fecha os 17), e dois blocos com o MESMO titulo leem
		   como a pagina se repetindo. */
		$html .= '<h3 class="rdm-f3-grupo-titulo">'
			. esc_html( $m['titulo_aguentam_sem_link'] ) . '</h3>';
		$html .= '<ul class="rdm-f3-lista">';
		foreach ( $servem as $s ) {
			$html .= '<li>' . esc_html( $s['nome'] ) . ' — '
				. '<span class="rdm-num">'
				. esc_html( rodametria_f3_numero( $s['carga_max_kg'] ) )
				. '</span> kg declarados</li>';
		}
		$html .= '</ul>';
	}

	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A PRESTACAO DE CONTAS DA SECAO 7 — todo registro em EXATAMENTE um grupo, com
 * nome proprio, e os numeros CONTADOS do banco e nunca digitados aqui.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_contas_html' ) ) {
function rodametria_f3_contas_html( $d ) {
	$c = $d['compra']['contagem'];
	$g = $d['compra']['grupos'];
	$m = $d['frases_molde'];

	$nomes = function ( $lista ) {
		$out = array();
		foreach ( (array) $lista as $x ) {
			$out[] = $x['nome'];
		}

		return implode( ', ', $out );
	};

	$rotulos = array(
		'nao_declaram_carga'  => $m['titulo_sem_carga'],
		'sem_saida_de_compra' => $m['titulo_sem_compra'],
	);

	$html = '<div class="rdm-f3-contas">';

	$html .= '<p>Dos <span class="rdm-num">'
		. esc_html( rodametria_f3_numero( $d['compra']['total_registros_veiculos'] ) )
		. '</span> veículos que o nosso banco tem, <span class="rdm-num">'
		. esc_html( rodametria_f3_numero( $d['compra']['quantos_declaram_carga'] ) )
		. '</span> declaram a carga máxima na ficha. Os outros não entram nesta conta, '
		. 'e a razão está dita abaixo: a gente não estima carga máxima por tamanho de '
		. 'roda, por potência nem por aparência.</p>';

	foreach ( $rotulos as $chave => $rotulo ) {
		$quantos = isset( $c[ $chave ] ) ? (int) $c[ $chave ] : 0;
		if ( ! $quantos ) {
			continue;
		}
		$html .= '<h3 class="rdm-f3-grupo-titulo">' . esc_html( $rotulo )
			. ' (<span class="rdm-num">' . esc_html( rodametria_f3_numero( $quantos ) )
			. '</span>)</h3>';
		$html .= '<p>' . esc_html( $nomes( isset( $g[ $chave ] ) ? $g[ $chave ] : array() ) )
			. '</p>';
	}

	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A TABELA PRE-RENDERIZADA (32.1, item 6) — VISIVEL, nunca recolhida: e o que
 * as IAs citam. Cada linha e um PESO, e a carga minima de cada uma vem
 * recomputada pela referencia, nunca digitada.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_tabela_html' ) ) {
function rodametria_f3_tabela_html( $d ) {
	$html  = '<div class="rdm-tabela-rolo"><table class="rdm-tabela">';
	$html .= '<thead><tr>'
		. '<th scope="col">Você mais o que carrega</th>'
		. '<th scope="col">Carga mínima a procurar</th>'
		. '<th scope="col">Do nosso banco, quantos aguentariam</th>'
		. '</tr></thead><tbody>';

	foreach ( (array) $d['tabela']['linhas'] as $l ) {
		$html .= '<tr>';
		$html .= '<td><span class="rdm-num">'
			. esc_html( rodametria_f3_numero( $l['peso_total_kg'] ) ) . '</span> kg</td>';
		$html .= '<td><span class="rdm-num">'
			. esc_html( $l['carga_minima_tela'] ) . '</span> kg</td>';
		$html .= '<td><span class="rdm-num">'
			. esc_html( rodametria_f3_numero( $l['quantos_do_banco_aguentariam'] ) )
			. '</span> de <span class="rdm-num">'
			. esc_html( rodametria_f3_numero( $d['compra']['quantos_declaram_carga'] ) )
			. '</span></td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';

	return $html;
}
}

/** A data em portugues. A irma tem a dela; esta nao vai para a casca porque
 * duas linhas repetidas custam menos que um componente que ninguem procura. */
if ( ! function_exists( 'rodametria_f3_data' ) ) {
function rodametria_f3_data( $iso ) {
	if ( ! $iso ) {
		return 'data não registrada';
	}
	$t = strtotime( $iso );

	return $t ? date_i18n( 'd/m/Y', $t ) : (string) $iso;
}
}

/* ---------------------------------------------------------------------------
 * AS DOBRAS (32.1, item 7). O texto continua no HTML servido e legivel com o
 * JavaScript desligado (32.3 e 22.8).
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_dobras_html' ) ) {
function rodametria_f3_dobras_html( $d ) {
	$r = $d['resposta_exemplo'];
	$html = '';

	/* COMO CHEGAMOS NO NUMERO.
	   A `frase_margem` NAO SE REPETE AQUI, e isso foi medido no ar em
	   06/11/2026: ela ja esta na CAIXA DE RESULTADO, e a pagina servia os
	   mesmos 200 caracteres duas vezes. A dobra explica o MECANISMO; o numero e
	   a razao dele ficam na caixa, que e onde a pessoa olha primeiro. */
	$corpo = '<p>A conta é uma só: somamos o seu peso com o que você carrega e '
		. 'acrescentamos a folga. O resultado é a carga máxima que a ficha do veículo '
		. 'precisa declarar — não é o peso que ele “provavelmente” aguenta.</p>';
	foreach ( (array) $r['frases_mercado'] as $f ) {
		$corpo .= '<p>' . esc_html( $f ) . '</p>';
	}
	$html .= rodametria_casca_dobra( 'Como chegamos nesse número', $corpo );

	/* O QUE ESTA CONTA SE RECUSA A FAZER (3.5) */
	$corpo = '<ul>';
	$corpo .= '<li>Não estimamos a carga máxima de um veículo que não a declara. '
		. 'Sem o número na ficha, ele fica de fora da comparação e aparece nomeado, '
		. 'com a causa.</li>';
	$corpo .= '<li>Não falamos de garupa, carona nem bagageiro: não medimos nada '
		. 'disso, e o que não medimos a gente não publica.</li>';
	$corpo .= '<li>Não devolvemos lista vazia em silêncio. Quando ninguém serve, a '
		. 'página diz por que e com quantos veículos ela contou.</li>';
	$corpo .= '<li>A folga é critério nosso e a página nunca a atribui a ninguém. '
		. 'Procuramos uma régua publicada em percentual e não achamos: o que existe '
		. 'publicado é qualitativo.</li>';
	$corpo .= '</ul>';
	$html .= rodametria_casca_dobra( 'O que esta conta se recusa a fazer', $corpo );

	/* COMO SABEMOS — fonte nomeada e data (32.4: procedencia continua) */
	$corpo = '<ul>';
	foreach ( (array) $d['constantes_usadas'] as $c ) {
		if ( empty( $c['fonte'] ) ) {
			continue;
		}
		$corpo .= '<li>' . esc_html( $c['fonte'] );
		if ( ! empty( $c['verificado_em'] ) ) {
			$corpo .= ' <span class="rdm-f3-data">(conferido em '
				. esc_html( rodametria_f3_data( $c['verificado_em'] ) )
				. ')</span>';
		}
		$corpo .= '</li>';
	}
	/* A DATA QUE A PROSA DECLARA, E ELA TEM DE SER A MESMA DO `dateModified` DO
	   JSON-LD (20.7: um fato, uma fonte). O portao de ar REPROVOU esta pagina
	   por isso na primeira conferencia: o JSON-LD dizia 06/11/2026 e a prosa
	   trazia so os 28/10/2026 das constantes — duas declaracoes do mesmo fato
	   comecam iguais e so uma sobe. As duas saem agora de `gerado_em`. */
	$corpo .= '</ul>';
	$corpo .= '<p class="rdm-fonte">Esta página foi gerada a partir do nosso banco em '
		. esc_html( rodametria_f3_data( isset( $d['gerado_em'] ) ? $d['gerado_em'] : '' ) )
		. ', e os números de veículos citados nela são contados no banco, nunca '
		. 'escritos à mão.</p>';
	$html .= rodametria_casca_dobra( 'Como sabemos', $corpo );

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A PAGINA, na ordem da 32.1.
 * ------------------------------------------------------------------------- */
if ( ! function_exists( 'rodametria_f3_pagina_html' ) ) {
function rodametria_f3_pagina_html() {
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F3 );

	if ( ! $d || empty( $d['campos'] ) || empty( $d['resposta_exemplo'] ) ) {
		/* Pagina DEGRADADA e honesta. Nunca molde cru, nunca numero inventado. */
		return '<div class="rdm-faixa rdm-pagina">'
			. rodametria_casca_trilha_html()
			. '<h1>Peso máximo suportado por patinete elétrico</h1>'
			. '<p class="rdm-promessa">A calculadora está fora do ar neste momento: o banco '
			. 'de dados que alimenta as contas não chegou ao site nesta atualização. Nenhum '
			. 'número desta página é estimado, então ela prefere não responder a responder '
			. 'errado.</p>'
			. '</div>';
	}

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>Peso máximo suportado por patinete elétrico</h1>';
	$html .= '<p class="rdm-promessa">Diga o seu peso e o que você leva: sai a carga '
		. 'máxima que a ficha precisa declarar, com a folga que a gente exige e o '
		. 'motivo dela.</p>';

	$html .= rodametria_f3_formulario_html( $d );
	$html .= rodametria_f3_noscript_html( $d );
	$html .= rodametria_f3_resultado_html( $d );

	/* O BLOCO DE COMPRA VEM IMEDIATAMENTE ABAIXO DO RESULTADO (32.1, item 5), e
	   hoje ele esta VAZIO. A frase que entra no lugar sai da referencia e nomeia
	   a causa medida — a 32.1 proibe bloco de compra vazio SEM causa, nunca
	   bloco de compra honesto sobre a falta. */
	$causa = '';
	foreach ( (array) $d['resposta_exemplo']['frases_vazio'] as $f ) {
		$causa = $f;
		break;
	}
	/* DOIS TEXTOS DIFERENTES, E ISSO E REGRA DESDE 06/11/2026: o de ESCOPO diz
	   o que entra neste bloco, e o da CAUSA diz por que ele esta vazio hoje. A
	   casca passou a nao imprimir o escopo quando os dois sao iguais — porque a
	   home foi ao ar hoje de manha com o paragrafo DUPLICADO —, e aqui eles
	   nascem distintos. O de escopo NAO carrega numero: contagem fica na
	   prestacao de contas, que a conta do banco. */
	$html .= rodametria_casca_bloco_de_compra(
		'À venda agora, e o que cada um aguenta',
		(array) $d['compra']['vitrine'],
		'Entram aqui os veículos que declaram a carga máxima na ficha e têm link de '
			. 'loja aberto. Quem declara a carga e não tem link aparece logo abaixo, '
			. 'nomeado.',
		$causa );

	$html .= '<h2>O que o nosso banco tem para o seu peso</h2>';
	$html .= rodametria_f3_grupos_html( $d );

	/* O CONVITE PARA A F2 (3.4 e 32.2), E A CHAMADA E GUARDADA.
	   `rodametria_f2_url()` mora em OUTRO snippet, e pela cicatriz da 20.4 um
	   snippet pode estar gravado e NAO ATIVADO — e ai a chamada direta seria
	   erro fatal, ou seja TELA BRANCA nesta pagina por causa da irma. O snippet
	   `rodametria-produto` ja guardava esta mesma funcao desde 29/10 e a licao
	   nao havia viajado (32.5-c outra vez, dentro da mesma ilha). Sem a F2, o
	   convite simplesmente NAO NASCE: a pagina perde um link e nao cai. */
	if ( function_exists( 'rodametria_f2_url' ) ) {
		$html .= '<p class="rdm-f3-convite">'
			. esc_html( $d['resposta_exemplo']['frase_convite_f2'] ) . ' '
			. '<a href="' . esc_url( add_query_arg(
				'rdm_peso',
				(int) $d['campos']['exemplo']['peso_piloto_kg'],
				rodametria_f2_url() ) ) . '">Ver a conta de autonomia com o seu peso</a>.</p>';
	}

	$html .= '<h2>Quem entrou, quem não entrou, e por quê</h2>';
	$html .= rodametria_f3_contas_html( $d );

	$html .= '<h2>Já calculado para outros pesos</h2>';
	$html .= rodametria_f3_tabela_html( $d );

	$html .= '<h2>O resto da conta</h2>';
	$html .= rodametria_f3_dobras_html( $d );

	$html .= '</div>';

	return $html;
}
}

add_shortcode( 'rodametria_f3', 'rodametria_f3_pagina_html' );

/* A DATA QUE ESTA PAGINA PUBLICA, pendurada no filtro da casca. Sai de
   `gerado_em` do banco da F3 — o MESMO campo que a dobra "Como sabemos" ja
   usa. Um fato, uma fonte (20.7). */
add_filter( 'rodametria_data_da_pagina', function ( $data, $slug ) {
	if ( RODAMETRIA_F3_SLUG !== $slug || '' !== $data ) {
		return $data;
	}
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F3 );

	return ( $d && ! empty( $d['gerado_em'] ) ) ? (string) $d['gerado_em'] : $data;
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * JSON-LD — FAQPage montado CAMPO POR CAMPO do mesmo banco que a pagina serve,
 * para a camada que a IA le e a que a pessoa le nao poderem divergir. Nao
 * repete o BreadcrumbList, que e da casca.
 * ------------------------------------------------------------------------- */
add_action( 'wp_head', function () {
	if ( ! rodametria_f3_na_pagina() ) {
		return;
	}
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F3 );
	if ( ! $d || empty( $d['resposta_exemplo'] ) ) {
		return;
	}
	$r = $d['resposta_exemplo'];

	$perguntas = array(
		array(
			'De quanta carga máxima eu preciso?',
			$r['frase_precisa'] . ' ' . $r['frase_margem'],
		),
	);

	/* A pergunta da tabela sai da propria tabela, com a VIRADA nomeada: e a
	   linha que mostra a tese desta ferramenta. */
	$virada = null;
	$anterior = null;
	foreach ( (array) $d['tabela']['linhas'] as $l ) {
		if ( null !== $anterior
			&& (int) $anterior['quantos_do_banco_aguentariam'] > 0
			&& 0 === (int) $l['quantos_do_banco_aguentariam'] ) {
			$virada = array( $anterior, $l );
			break;
		}
		$anterior = $l;
	}
	if ( $virada ) {
		$perguntas[] = array(
			'Quantos quilos o patinete elétrico aguenta?',
			'Na faixa que vimos no varejo brasileiro, a carga máxima declarada mais '
			. 'comum é de ' . rodametria_f3_numero( $d['compra']['teto_do_banco_kg'] )
			. ' kg. Com a nossa folga, isso acolhe até '
			. rodametria_f3_numero( $virada[0]['peso_total_kg'] )
			. ' kg de pessoa mais carga; a partir de '
			. rodametria_f3_numero( $virada[1]['peso_total_kg'] )
			. ' kg nenhum dos modelos com carga declarada no nosso banco serve.',
		);
	}

	foreach ( (array) $r['frases_vazio'] as $f ) {
		$perguntas[] = array( 'Quais modelos vocês indicam para o meu peso?', $f );
		break;
	}

	$itens = array();
	foreach ( $perguntas as $p ) {
		$itens[] = array(
			'@type'          => 'Question',
			'name'           => $p[0],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
		);
	}

	echo "\n" . '<script type="application/ld+json">'
		. wp_json_encode( array(
			'@context'   => 'https://schema.org',
			'@type'      => 'FAQPage',
			'mainEntity' => $itens,
		), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
		. '</script>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * A RECOMPUTACAO NO NAVEGADOR.
 *
 * A DECISAO ESTA ESCRITA DUAS VEZES DE PROPOSITO (secao 8): aqui e em
 * `regras/f3.py`. O que NAO esta escrito duas vezes e a FRASE — todo molde vem
 * do banco, e o portao `teste-f3.py` proibe prosa literal dentro deste bloco.
 * Duas metades escrevendo a propria frase dizem duas coisas para a mesma
 * entrada, e nenhum portao ve.
 * ------------------------------------------------------------------------- */
add_action( 'wp_footer', function () {
	if ( ! rodametria_f3_na_pagina() ) {
		return;
	}
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F3 );
	if ( ! $d || empty( $d['frases_molde'] ) ) {
		return;
	}

	$pacote = array(
		'moldes'   => $d['frases_molde'],
		'margem'   => $d['margem_pct'],
		'ordem'    => $d['grupos_em_ordem'],
		'servem'   => $d['compra']['serviriam_sem_oferta'],
		/* A VITRINE DE VERDADE (carga declarada E oferta aberta). Hoje e vazia, e
		   ela viaja porque e dela que o navegador reclassifica os grupos: sem
		   ela, o dia em que um registro ganhasse link seria o dia em que a
		   recomputacao o deixaria CAIR DA TELA. 32.5-d fechada, nao
		   pre-registrada. */
		'vitrine'  => isset( $d['compra']['com_oferta'] ) ? $d['compra']['com_oferta'] : array(),
		'declaram' => $d['compra']['quantos_declaram_carga'],
		'teto'     => $d['compra']['teto_do_banco_kg'],
	);
	?>
<script id="rodametria-f3-js">
(function(){
  var D = <?php echo wp_json_encode( $pacote, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ); ?>;
  var form = document.querySelector('[data-rdm-f3-form]');
  if (!form) { return; }
  var campoPeso = form.querySelector('[data-rdm-f3-peso]');
  var campoCarga = form.querySelector('[data-rdm-f3-carga]');
  var caixa = document.querySelector('[data-rdm-f3-caixa]');
  var grupos = document.querySelector('[data-rdm-f3-grupos]');

  function num(x){
    return String(Math.round(x)).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }
  function preencher(molde, vals){
    return molde.replace(/\{(\w+)\}/g, function(_, k){
      return (k in vals) ? vals[k] : '';
    });
  }
  /* O ARREDONDAMENTO ANDA PARA CIMA, igual a referencia. Para baixo publicaria
     um numero MENOR do que a folga pede, e o erro caro aqui e o permissivo. */
  function minimo(total){
    var exato = total * (100 + D.margem) / 100;
    var teto = Math.ceil(exato - 1e-9);
    return teto;
  }
  function grupoDe(cargaMax, total){
    if (cargaMax >= minimo(total)) { return 'folga'; }
    if (total <= cargaMax) { return 'no_limite'; }
    return 'nao_aguenta';
  }

  function responder(){
    var peso = parseFloat(campoPeso.value);
    var carga = parseFloat(campoCarga.value);
    if (!(peso > 0)) { return; }
    if (!(carga >= 0)) { carga = 0; }
    var total = peso + carga;
    var min = minimo(total);

    if (caixa) {
      var alvo = caixa.querySelector('.rdm-molde-caixa-numero .rdm-num');
      if (alvo) { alvo.textContent = num(min); }
      var frases = caixa.querySelectorAll('.rdm-molde-caixa-frase');
      if (frases.length >= 1) {
        frases[0].textContent = carga > 0
          ? preencher(D.moldes.precisa, {total: num(total), minimo: num(min)})
          : preencher(D.moldes.precisa_sem_carga, {piloto: num(peso), minimo: num(min)});
      }
      if (frases.length >= 2) {
        frases[1].textContent = preencher(D.moldes.margem,
          {minimo: num(min), total: num(total), pct: num(D.margem)});
      }
    }
    /* O atributo dedicado, que e o que as duas irmas usam.  dentro
       da barra tambem casaria hoje, e casaria por acidente: ele e a classe de
       TODO numero desta ilha, e no dia em que a barra ganhar um segundo numero
       o seletor pegaria o primeiro que aparecesse. */
    var barra = document.querySelector('[data-rdm-barra-numero]');
    if (barra) { barra.textContent = num(min); }

    if (!grupos) { return; }
    /* DOIS conjuntos, e eles nao se misturam: `baldes` e a VITRINE (tem link) e
       `sem` e quem aguenta e nao tem link. O servidor serve os dois separados e
       o navegador tem de servir os dois separados tambem. */
    var baldes = {folga: [], no_limite: [], nao_aguenta: []};
    var sem = {folga: [], no_limite: [], nao_aguenta: []};
    var i;
    for (i = 0; i < D.vitrine.length; i++) {
      var v = D.vitrine[i];
      baldes[grupoDe(v.carga_max_kg, total)].push(v);
    }
    for (i = 0; i < D.servem.length; i++) {
      var s = D.servem[i];
      sem[grupoDe(s.carga_max_kg, total)].push(s);
    }
    var html = '';
    var titulos = {folga: D.moldes.titulo_folga, no_limite: D.moldes.titulo_no_limite,
                   nao_aguenta: D.moldes.titulo_nao_aguenta};
    for (i = 0; i < D.ordem.length; i++) {
      var g = D.ordem[i];
      var lista = baldes[g];
      if (!lista || !lista.length) { continue; }
      html += '<h3 class="rdm-f3-grupo-titulo">' + titulos[g] + '</h3><ul class="rdm-f3-lista">';
      for (var j = 0; j < lista.length; j++) {
        var it = lista[j];
        var frase;
        if (g === 'folga') {
          frase = preencher(D.moldes.linha_folga, {nome: it.nome,
            carga: num(it.carga_max_kg), sobra: num(it.carga_max_kg - min)});
        } else if (g === 'no_limite') {
          frase = preencher(D.moldes.linha_no_limite, {nome: it.nome,
            carga: num(it.carga_max_kg), total: num(total), pct: num(D.margem)});
        } else {
          frase = preencher(D.moldes.linha_nao_aguenta, {nome: it.nome,
            carga: num(it.carga_max_kg), faltam: num(total - it.carga_max_kg)});
        }
        html += '<li>' + frase + '</li>';
      }
      html += '</ul>';
      if (g === 'no_limite') {
        html += '<p class="rdm-f3-ressalva">' + D.moldes.ressalva_no_limite + '</p>';
      }
    }
    /* A VITRINE E VAZIA HOJE, e a frase de vazio e escolhida pela MESMA causa
       que a referencia usa: se algum do banco aguentaria e nao ha link, a
       frase e a da falta de oferta; se nenhum aguenta, e a da carga. */
    /* A FRASE DE LISTA VAZIA ESCOLHE PELA MESMA CAUSA QUE A REFERENCIA USA, e as
       duas causas sao de eixos diferentes: `baldes.folga` vazio diz que a
       VITRINE nao tem o que mostrar, e `sem.folga` diz se o que falta e o LINK
       ou a CARGA. Molde unico aqui mentiu na primeira versao da ferramenta. */
    /* A CAUSA E REESCRITA NO BLOCO DE COMPRA, que e onde ela mora — nunca aqui.
       Ate 06/11/2026 ela era escrita nos dois lugares e a pagina servia o
       paragrafo DUAS VEZES. */
    var pVazio = document.querySelector('.rdm-molde-compra-vazio');
    if (pVazio) {
      if (!baldes.folga.length && sem.folga.length) {
        pVazio.textContent = preencher(D.moldes.vazio_por_falta_de_oferta,
          {quantos_servem: num(sem.folga.length), quantos: num(D.declaram),
           total: num(total)});
      } else if (!baldes.folga.length) {
        pVazio.textContent = preencher(D.moldes.vazio_por_carga,
          {quantos: num(D.declaram), total: num(total), teto: num(D.teto)});
      }
    }
    /* E OS NOMES DE QUEM AGUENTA E NAO TEM LINK, nomeados e nunca sumidos
       (secao 7) — independentes da vitrine estar cheia ou vazia. */
    if (sem.folga.length) {
      html += '<h3 class="rdm-f3-grupo-titulo">' + D.moldes.titulo_aguentam_sem_link + '</h3>';
      html += '<ul class="rdm-f3-lista">';
      for (i = 0; i < sem.folga.length; i++) {
        html += '<li>' + sem.folga[i].nome + '</li>';
      }
      html += '</ul>';
    }
    grupos.innerHTML = html;
  }

  form.addEventListener('submit', function(e){ e.preventDefault(); responder(); });
  campoPeso.addEventListener('change', responder);
  campoCarga.addEventListener('change', responder);
})();
</script>
	<?php
}, 30 );

/* A PAGINA NASCE NA INSTALACAO, pelo filtro da casca. A casca reinstala quando
   a ASSINATURA do mapa muda — e foi ela que fez as quatro paginas do bloco 5d
   nascerem sem ninguem acionar nada. */
add_filter( 'rodametria_instalar', function ( $relato ) {
	$p = rodametria_casca_garantir_pagina(
		RODAMETRIA_F3_SLUG,
		'Peso máximo suportado por patinete elétrico',
		'[rodametria_f3]' );

	if ( empty( $p['id'] ) ) {
		$relato[] = 'f3: ERRO — ' . ( isset( $p['erro'] ) ? $p['erro'] : 'sem id' );

		return $relato;
	}
	$relato[] = 'f3: #' . $p['id'] . ' (' . $p['slug'] . ')'
		. ( empty( $p['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );

	return $relato;
} );

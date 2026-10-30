<?php
/**
 * RODAMETRIA — F2: "QUANTOS KM ELE FAZ DE VERDADE?"
 *
 * A primeira ferramenta desta ilha a ir ao ar, e a primeira pagina que um
 * visitante ve. A ordem da tela e a da 32.1, de cima para baixo: trilha e H1,
 * uma frase de promessa, o FORMULARIO ja preenchido, a CAIXA DE RESULTADO ja
 * pre-renderizada, o BLOCO DE COMPRA, a tabela visivel, e o resto em <details>.
 *
 * POR QUE A F2 E NAO A F1, e e decisao registrada e nao atalho: o limiar legal
 * da F1 esta `pendente` — o texto oficial da Resolucao Contran nao abre pelo
 * canal de leitura desta nuvem (medido em 28/10 e remedido em 29/10/2026, cinco
 * dominios oficiais em recusa). A especificacao desta ilha diz, com todas as
 * letras: "A F1 segue sem poder ir ao ar. A F2 e a F3 podem ir ao ar". E a F3
 * depende de `carga_max_kg`, que so tres registros do banco declaram, nenhum
 * deles com oferta aberta.
 *
 * ESTE ARQUIVO NAO DIGITA UM NUMERO E NAO ESCREVE UMA FRASE DE RESPOSTA. Tudo
 * vem da option que o Sync grava de `dados/f2-respostas.json`, que por sua vez
 * e escrito por `ferramentas/gerar-f2.py` a partir de `ferramentas/
 * f2-referencia.py` e de `dados/constantes.json`. E a regra da secao 8 do
 * ARQUIPELAGO.md: para cada campo publicado, aponte quem e a fonte, e numero de
 * tela nasce contado, nunca digitado.
 *
 * E O JS ESTA NO RODAPE, NUNCA DENTRO DO SHORTCODE. O WordPress roda os filtros
 * do the_content sobre o retorno do shortcode e troca && por &#038;&#038;,
 * matando o script — foi o defeito que derrubou cinco calculadoras da Aquametria
 * em 08/09/2026.
 */

if ( ! defined( 'RODAMETRIA_F2_VERSAO' ) ) {
	define( 'RODAMETRIA_F2_VERSAO', '1.3.1' );
}
if ( ! defined( 'RODAMETRIA_F2_SLUG' ) ) {
	define( 'RODAMETRIA_F2_SLUG', 'autonomia-patinete-eletrico' );
}

/* A pagina entra no mapa da casca por filtro: a casca nao conhece o nome dela. */
add_filter( 'rodametria_paginas', function ( $mapa ) {
	$mapa[ RODAMETRIA_F2_SLUG ] = array(
		'nome'        => 'Autonomia',
		'titulo'      => 'Quantos km o patinete elétrico faz de verdade — a conta por Wh',
		'tipo'        => 'ferramenta',
		'pai'         => 'inicio',
		'no_menu'     => false,
		/* ITENS 5 E 2 DO DESPACHO DE 30/10/2026, NA MESMA FRASE.
		   O 5: tinha 193 caracteres no HTML servido, contra o teto de 160 que o
		   portao de ar passou a cobrar. 151 agora, contados.
		   O 2: O PESO SAIU DA PROMESSA. Esta frase prometia "a faixa de km que da
		   para esperar com o seu peso", e o peso NAO entra em conta nenhuma — a
		   constante de consumo por quilo esta `pendente` e pela secao 10 nao pode
		   entrar em formula. O relevo, que FICOU na promessa, entra de verdade:
		   e o fator medido no estudo de Quito. Prometer o relevo e entregar o
		   relevo; prometer o peso era prometer o que nao se entrega. */
		'description' => 'Diga a tensão e a amperagem da bateria: a conta devolve os watt-hora '
			. 'e a faixa de km que dá para esperar no relevo do seu trajeto, ao lado do '
			. 'anúncio.',
	);

	return $mapa;
} );

if ( ! function_exists( 'rodametria_f2_na_pagina' ) ) {
function rodametria_f2_na_pagina() {
	return is_page( RODAMETRIA_F2_SLUG );
}
}

if ( ! function_exists( 'rodametria_f2_url' ) ) {
function rodametria_f2_url() {
	$u = rodametria_casca_url_do_slug( RODAMETRIA_F2_SLUG );

	return '' !== $u ? $u : home_url( '/' . RODAMETRIA_F2_SLUG . '/' );
}
}

/* ---------------------------------------------------------------------------
 * O FORMULARIO (32.1, item 3) — JA PREENCHIDO COM O CASO DE EXEMPLO
 *
 * As opcoes de V e Ah saem do banco publicado, nunca de uma lista escrita aqui:
 * formulario que oferece combinacao que nenhuma ficha declara convida a pessoa a
 * perguntar algo que a ilha nao mediu.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_formulario_html' ) ) {
function rodametria_f2_formulario_html( $d ) {
	$ex = $d['campos']['exemplo'];

	$opcoes = function ( $lista, $atual, $sufixo ) {
		$html = '';
		foreach ( $lista as $v ) {
			$rotulo = rodametria_f2_numero( $v ) . ' ' . $sufixo;
			$html  .= '<option value="' . esc_attr( $v ) . '"'
				. ( (float) $v === (float) $atual ? ' selected' : '' ) . '>'
				. esc_html( $rotulo ) . '</option>';
		}

		return $html;
	};

	$html  = '<form class="rdm-f-formulario rdm-f2" data-rdm-f2-form'
		. ' method="get" action="' . esc_url( rodametria_f2_url() ) . '">';
	$html .= '<div class="rdm-f-campos">';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f2-v">Tensão da bateria</label>'
		. '<select id="rdm-f2-v" name="v" data-rdm-f2-v>'
		. $opcoes( $d['campos']['tensoes_v'], $ex['tensao_v'], 'V' )
		. '</select><span class="rdm-f-dica">Vem na etiqueta da bateria</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f2-ah">Amperagem</label>'
		. '<select id="rdm-f2-ah" name="ah" data-rdm-f2-ah>'
		. $opcoes( $d['campos']['amperagens_ah'], $ex['amperagem_ah'], 'Ah' )
		. '</select><span class="rdm-f-dica">Também na etiqueta, ao lado dos volts</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f2-peso">Seu peso</label>'
		. '<input id="rdm-f2-peso" name="peso" type="number" inputmode="numeric" min="30" max="200"'
		. ' step="1" value="' . esc_attr( (int) $ex['peso_piloto_kg'] ) . '" data-rdm-f2-peso>'
		. '<span class="rdm-f-dica">Em kg, com mochila se você leva</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f2-relevo">O seu trajeto</label>'
		. '<select id="rdm-f2-relevo" name="relevo" data-rdm-f2-relevo>';
	$nomes = array( 'plano' => 'Plano', 'misto' => 'Um pouco de subida', 'ladeira' => 'Ladeira de verdade' );
	foreach ( $d['campos']['relevos'] as $r ) {
		$html .= '<option value="' . esc_attr( $r ) . '"'
			. ( $r === $ex['relevo'] ? ' selected' : '' ) . '>'
			. esc_html( isset( $nomes[ $r ] ) ? $nomes[ $r ] : $r ) . '</option>';
	}
	$html .= '</select><span class="rdm-f-dica">É o que mais muda o resultado</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f2-aut">Km que o anúncio promete</label>'
		. '<input id="rdm-f2-aut" name="aut" type="number" inputmode="numeric" min="1" max="400"'
		. ' step="1" value="' . esc_attr( (int) $ex['autonomia_declarada_km'] ) . '" data-rdm-f2-aut>'
		. '<span class="rdm-f-dica">Opcional — sem ele a gente só dá os Wh</span></p>';

	$html .= '</div>';
	$html .= '<p class="rdm-f-acao"><button class="rdm-f-botao" type="submit">Calcular a autonomia</button></p>';
	$html .= '</form>';

	return $html;
}
}

/** Numero em portugues, para rotulo de opcao. Nenhuma conta mora aqui. */
if ( ! function_exists( 'rodametria_f2_numero' ) ) {
function rodametria_f2_numero( $v ) {
	$f = (float) $v;
	if ( $f === floor( $f ) ) {
		return number_format( $f, 0, ',', '.' );
	}

	return rtrim( rtrim( number_format( $f, 1, ',', '.' ), '0' ), ',' );
}
}

/* ---------------------------------------------------------------------------
 * A CAIXA DE RESULTADO (32.1, item 4) — PRE-RENDERIZADA NO HTML
 *
 * Pre-renderizada e OBRIGATORIO por duas razoes diferentes: a 32.1 quer o
 * resultado na primeira tela sem depender de clique, e a secao 5 (visibilidade
 * em IA) quer a resposta legivel por quem nao preenche formulario. Com o
 * JavaScript desligado a pagina continua respondendo o caso de exemplo —
 * exigencia literal da 22.8 e da 32.5.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_nota_de_preco' ) ) {
/**
 * A NOTA DO PRECO (item 3 do despacho de 30/10/2026).
 *
 * Duas frases, e quem decide qual e a comparacao entre o programa da COTACAO e
 * o programa do LINK. Mesma loja: a nota de sempre. Lojas diferentes: a nota
 * nomeia as duas, porque preco com procedencia e data ao lado de um botao que
 * vai para outro lugar e a pagina prometendo o que nao entrega.
 *
 * O nome da loja NAO e escrito aqui: vem de rodametria_casca_nome_da_loja(),
 * que e o unico lugar desta ilha que sabe traduzir programa em nome.
 */
function rodametria_f2_nota_de_preco( $f ) {
	$data = rodametria_f2_data( $f['preco_data'] );
	$loja_do_preco = ! empty( $f['preco_programa'] )
		? rodametria_casca_nome_da_loja( $f['preco_programa'] )
		: (string) $f['preco_loja'];

	$programa_do_botao = empty( $f['url_afiliado_da_ficha'] ) && empty( $f['url_busca'] )
		? '' : (string) $f['programa'];
	$loja_do_botao = '' === $programa_do_botao
		? '' : rodametria_casca_nome_da_loja( $programa_do_botao );

	if ( '' === $loja_do_botao || $loja_do_preco === $loja_do_botao ) {
		return 'na ' . $loja_do_preco . ', lido em ' . $data;
	}

	return 'lido na ' . $loja_do_preco . ' em ' . $data
		. ' — o botão abre a ' . $loja_do_botao;
}
}

if ( ! function_exists( 'rodametria_f2_resultado_html' ) ) {
function rodametria_f2_resultado_html( $d ) {
	$r = $d['resposta_exemplo'];

	$frases = array();
	$frases[] = $r['frase_wh'];
	foreach ( (array) $r['frases_km'] as $f ) {
		$frases[] = $f;
	}

	$tem_km = ( null !== $r['piso_km_tela'] );
	$numero = $tem_km
		? ( $r['piso_km_tela'] === $r['teto_km_tela']
			? $r['teto_km_tela']
			: $r['piso_km_tela'] . ' a ' . $r['teto_km_tela'] )
		: $r['wh_tela'];
	$unidade = $tem_km ? 'km' : 'Wh';
	/* O rotulo tambem e MOLDE, e nao literal: ele aparece na caixa, na barra
	   fixa do telefone e na recomputacao do navegador — tres lugares. A bateria
	   de mutacoes achou este defeito em 29/10/2026, com a trava "o JS volta a
	   escrever frase propria" passando: o JS tinha o rotulo escrito dentro dele
	   e esta funcao tinha o mesmo rotulo escrito aqui. */
	$m       = $d['frases_molde'];
	$rotulo  = $tem_km ? $m['rotulo_km'] : $m['rotulo_wh'];

	return rodametria_casca_caixa( $rotulo, $numero, $unidade, $frases, 'verde',
		' data-rdm-f2-caixa' )
		. rodametria_casca_barra_fixa( $rotulo, $numero, $unidade );
}
}

/**
 * A RESSALVA DO PESO, abaixo do bloco de compra (ver o comentario acima).
 * O contêiner existe no HTML mesmo quando vazio, porque e nele que o navegador
 * reescreve a ressalva quando a pessoa troca o peso ou o relevo.
 */
if ( ! function_exists( 'rodametria_f2_ressalva_html' ) ) {
function rodametria_f2_ressalva_html( $d ) {
	$html = '<div class="rdm-f2-ressalva" data-rdm-f2-ressalva>';
	foreach ( (array) $d['resposta_exemplo']['frases_peso'] as $f ) {
		$html .= '<p>' . esc_html( $f ) . '</p>';
	}
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * O BLOCO DE COMPRA (32.1, item 5) E A PRESTACAO DE CONTAS (secao 7)
 *
 * A VERDADE DESTA PAGINA, E ELA ESTA ESCRITA NA TELA EM VEZ DE ESCONDIDA: o
 * criterio de entrada do produto nesta ferramenta e o Wh (2.6 da
 * especificacao), e NENHUM registro do banco declara V e Ah junto com oferta
 * aberta — medido, nao suposto: dos registros nao excluidos, os que declaram
 * V e Ah nao tem saida de compra, e os que tem saida de compra nao declaram
 * V nem Ah. A intersecao e vazia.
 *
 * Entao o bloco NAO apresenta os cartoes como "o que a conta escolheu". Ele diz
 * o que eles sao: patinetes e scooters com oferta aberta cuja ficha nao declara
 * a bateria. A secao 7 proibe bloco de compra vazio e proibe recomendar em
 * primeiro lugar o que a pagina diz nao servir — as duas coisas sao obedecidas
 * dizendo a causa, com os grupos por motivo e cada registro nomeado uma vez.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_itens_da_vitrine' ) ) {
function rodametria_f2_itens_da_vitrine( $d ) {
	$itens = array();
	foreach ( (array) $d['compra']['vitrine'] as $f ) {
		$spec = array();
		/* ESTA PAGINA RESPONDE AUTONOMIA, ENTAO A AUTONOMIA VEM PRIMEIRO. Ate
		   29/10/2026 as 16h3xZ o cartao do Honeywhale M2 MAX era medido no ar
		   servindo `500 W no anúncio · bateria não declarada · a ficha não
		   declara a bateria` — e a oferta que o botao dele abre declara, no
		   proprio titulo, 22 km de autonomia, que e exatamente o numero desta
		   pagina. O cartao da pagina de autonomia estava calado sobre
		   autonomia. O numero vem com a atribuicao do nivel dele ao lado, que
		   o gerador le da escada do esquema: nivel 6 e declaracao de vendedor,
		   e numero de vendedor na tela sem dono vira promessa da ilha. */
		if ( ! empty( $f['autonomia_declarada_km'] ) ) {
			$spec[] = rodametria_f2_numero( $f['autonomia_declarada_km'] ) . ' km'
				. ( empty( $f['autonomia_quem_declara'] ) ? ''
					: ' declarados ' . $f['autonomia_quem_declara'] );
		}
		if ( ! empty( $f['watt_sem_rotulo'] ) ) {
			$spec[] = rodametria_f2_numero( $f['watt_sem_rotulo'] ) . ' W no anúncio';
		}
		/* A especificacao que fez o produto entrar (32.1). Quando ela EXISTE,
		   o cartao a serve; quando nao existe, o cartao NAO diz isso aqui —
		   `rotulo_do_grupo` logo abaixo ja e literalmente `a ficha não declara
		   a bateria`, e as duas linhas juntas eram a MESMA frase duas vezes no
		   mesmo cartao, medida no ar em 29/10/2026 (e uma terceira vez no
		   paragrafo de abertura do bloco). Dizer tres vezes nao informa mais:
		   gasta a primeira tela, que a 32.5 mede em pixel. */
		if ( ! empty( $f['tensao_v'] ) && ! empty( $f['amperagem_ah'] ) ) {
			$spec[] = rodametria_f2_numero( $f['tensao_v'] ) . ' V × '
				. rodametria_f2_numero( $f['amperagem_ah'] ) . ' Ah';
		}
		if ( ! empty( $f['rotulo_do_grupo'] ) ) {
			$spec[] = $f['rotulo_do_grupo'];
		}

		$itens[] = array(
			'nome'          => $f['nome'],
			'especificacao' => implode( ' · ', $spec ),
			'preco'         => empty( $f['preco_brl'] ) ? ''
				: 'R$ ' . number_format( (float) $f['preco_brl'], 2, ',', '.' ),
			/* ITEM 3 DO DESPACHO DE 30/10/2026 — O PRECO ERA DE UMA LOJA E O
			   BOTAO IA PARA OUTRA, e a nota antiga ('na Mercado Livre, lido
			   em 27/10/2026') prometia o destino: dois cartoes serviam esse
			   preco com o botao 'Ver ofertas na Shopee' do lado.
			   NAO E A ESCOLHA DA LOJA QUE MUDA — a regra de dinheiro desta
			   ilha manda preferir o link da Shopee, e o preco do Mercado
			   Livre e a unica cotacao com procedencia e data que estes
			   registros tem. O que muda e a FRASE: quando as duas lojas
			   divergem, a nota diz onde o preco foi lido E para onde o botao
			   vai, entao ela deixa de prometer o destino.
			   A nota continua CURTA de proposito: ela nasce ACIMA do botao
			   dentro do cartao, e a 32.5 mede o primeiro botao de compra a
			   1.400 px. */
			'preco_nota'    => empty( $f['preco_brl'] ) ? ''
				: rodametria_f2_nota_de_preco( $f ),
			/* A 25.2 em uma linha: a FICHA vira o botao quando existe, e a
			   BUSCA desce para a linha discreta — nunca sai. Quando nao ha
			   ficha, a busca sobe e e o botao, que e o estado em que esta
			   ilha nasceu. */
			'url'           => empty( $f['url_afiliado_da_ficha'] )
				? $f['url_busca'] : $f['url_afiliado_da_ficha'],
			'url_busca'     => empty( $f['url_afiliado_da_ficha'] )
				? '' : $f['url_busca'],
			'programa'      => $f['programa'],
			'degrau'        => $f['degrau'],
			'imagem'        => $f['imagem'],
		);
	}

	return $itens;
}
}

if ( ! function_exists( 'rodametria_f2_data' ) ) {
function rodametria_f2_data( $iso ) {
	if ( ! $iso ) {
		return 'data não registrada';
	}
	$t = strtotime( $iso );

	return $t ? date_i18n( 'd/m/Y', $t ) : (string) $iso;
}
}

if ( ! function_exists( 'rodametria_f2_contas_html' ) ) {
function rodametria_f2_contas_html( $d ) {
	$g     = $d['compra']['grupos'];
	$total = (int) $d['compra']['total_registros_veiculos'];

	$nomes = function ( $lista ) {
		$ns = array();
		foreach ( (array) $lista as $f ) {
			$ns[] = $f['nome'];
		}

		return implode( ', ', $ns );
	};

	$linhas = array();

	$linhas[] = array(
		'Cabem no Wh que você pediu',
		count( $g['cabem_no_wh'] ),
		$g['cabem_no_wh']
			? 'Estão na vitrine acima: ' . $nomes( $g['cabem_no_wh'] ) . '.'
			: 'Nenhum, e a causa é a mesma da linha de baixo: para entrar por Wh o anúncio '
				. 'precisa declarar tensão e amperagem junto com a oferta aberta, e isso não '
				. 'acontece em nenhum registro que colhemos até agora.',
	);
	$linhas[] = array(
		'De outro Wh',
		count( $g['de_outro_wh'] ),
		$g['de_outro_wh']
			? $nomes( $g['de_outro_wh'] ) . ' — a bateria deles é de outra faixa de energia.'
			: 'Nenhum: não há registro com bateria declarada e oferta aberta para comparar.',
	);
	$linhas[] = array(
		'Não declaram tensão nem amperagem',
		count( $g['nao_declaram_v_ou_ah'] ),
		$nomes( $g['nao_declaram_v_ou_ah'] ) . '. É a lacuna mais comum do varejo: o anúncio '
			. 'grita o watt do motor e cala a energia da bateria, que é o que de fato decide '
			. 'quantos km dá. Os que têm oferta aberta estão na vitrine acima, com esse rótulo.',
	);
	$linhas[] = array(
		'Declaram a bateria, mas não têm oferta aberta',
		count( $g['sem_saida_de_compra'] ),
		$g['sem_saida_de_compra']
			? $nomes( $g['sem_saida_de_compra'] ) . ' — declaram tensão e amperagem, e é por isso '
				. 'que eles estão na tabela abaixo; o que falta é a oferta, e sem oferta aberta '
				. 'nós não publicamos botão.'
			: 'Nenhum.',
	);
	$linhas[] = array(
		'Fora do banco',
		count( $g['fora_do_banco'] ),
		$g['fora_do_banco']
			? $nomes( $g['fora_do_banco'] ) . ' — saíram por não serem veículo de mobilidade '
				. 'elétrica, e não contam em nenhuma conta desta página.'
			: 'Nenhum.',
	);

	$html  = '<ul class="rdm-contas">';
	$soma  = 0;
	foreach ( $linhas as $l ) {
		$soma += (int) $l[1];
		$html .= '<li><b>' . esc_html( $l[0] ) . ': <span class="rdm-num">'
			. (int) $l[1] . '</span></b><br>' . esc_html( $l[2] ) . '</li>';
	}
	$html .= '</ul>';

	/* A soma fecha o banco, e o numero e CONTADO aqui e nao digitado — secao 7:
	   "a soma dos nomeados fecha o banco, e isso se mede". */
	$html .= '<p class="rdm-fonte">São <span class="rdm-num">' . (int) $soma . '</span> veículos '
		. 'nomeados de <span class="rdm-num">' . $total . '</span> no banco. '
		. ( $soma === $total
			? 'A conta fecha: nenhum registro deixou de ser dito nesta página.'
			: 'A conta NÃO fecha, e isso é defeito desta página, não do banco.' ) . '</p>';

	$pecas = (array) $d['compra']['pecas_publicaveis'];
	$html .= '<p>E as peças que esta resposta pede — bateria por V/Ah e carregador pela tensão — '
		. ( $pecas
			? 'ainda não estão no nosso banco com oferta aberta; o que temos de peça hoje é outra '
				. 'coisa (' . esc_html( count( $pecas ) ) . ' item com oferta), e peça de outra '
				. 'função não entra numa resposta de autonomia.'
			: 'ainda não estão no nosso banco.' )
		. ' Enquanto não estiverem, esta página não oferece bateria nem carregador — oferecer '
		. 'qualquer um dos dois sem a tensão certa é vender a peça errada.</p>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A TABELA PRE-RENDERIZADA (32.1, item 6; e a secao 5, visibilidade em IA)
 *
 * Visivel, NUNCA recolhida — e a metade que um modelo de linguagem le sem
 * preencher formulario. As linhas do banco e as externas ficam em blocos
 * separados, com a fonte dentro da linha: a 2.5 da especificacao manda
 * "combinacoes de V x Ah colhidas em ficha real", e medicao de moto nao se
 * mistura com ficha de patinete.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_tabela_html' ) ) {
function rodametria_f2_tabela_html( $d ) {
	$relevos = array( 'plano' => 'Plano', 'misto' => 'Pouca subida', 'ladeira' => 'Ladeira' );

	$linha = function ( $l ) use ( $relevos ) {
		$html  = '<tr><th scope="row">' . esc_html( $l['rotulo'] ) . '</th>';
		$html .= '<td class="rdm-num">' . esc_html( rodametria_f2_numero( $l['tensao_v'] ) ) . '</td>';
		$html .= '<td class="rdm-num">' . esc_html( rodametria_f2_numero( $l['amperagem_ah'] ) ) . '</td>';
		$html .= '<td class="rdm-num">' . esc_html( $l['wh'] ) . '</td>';
		$html .= '<td class="rdm-num">' . ( null === $l['autonomia_declarada_km']
			? '—' : esc_html( rodametria_f2_numero( $l['autonomia_declarada_km'] ) ) ) . '</td>';
		foreach ( array_keys( $relevos ) as $r ) {
			$f = $l['faixas'][ $r ];
			if ( null === $f['piso_km'] ) {
				$html .= '<td class="rdm-num">—</td>';
				continue;
			}
			$html .= '<td class="rdm-num">' . esc_html(
				$f['piso_km'] === $f['teto_km'] ? $f['piso_km'] : $f['piso_km'] . '–' . $f['teto_km'] )
				. '</td>';
		}
		$html .= '</tr>';

		return $html;
	};

	$cabeca  = '<thead><tr><th scope="col">De onde saiu</th><th scope="col" class="rdm-num">V</th>'
		. '<th scope="col" class="rdm-num">Ah</th><th scope="col" class="rdm-num">Wh</th>'
		. '<th scope="col" class="rdm-num">km no anúncio</th>';
	foreach ( $relevos as $nome ) {
		$cabeca .= '<th scope="col" class="rdm-num">' . esc_html( $nome ) . '</th>';
	}
	$cabeca .= '</tr></thead>';

	$html  = '<div class="rdm-tabela-rolagem"><table class="rdm-tabela">';
	$html .= '<caption>Combinações de bateria que a gente já colheu, com os watt-hora '
		. 'calculados e a faixa de km em cada relevo. As três últimas colunas são km.</caption>';
	$html .= $cabeca . '<tbody>';
	foreach ( (array) $d['tabela']['do_banco'] as $l ) {
		$html .= $linha( $l );
	}
	$html .= '</tbody></table></div>';

	if ( ! empty( $d['tabela']['externas'] ) ) {
		$html .= '<h3>Duas combinações que não são ficha de loja</h3>';
		$html .= '<div class="rdm-tabela-rolagem"><table class="rdm-tabela">';
		$html .= '<caption>Estas duas não estão à venda aqui: entram porque são as únicas '
			. 'medições com a ficha ao lado que a gente conseguiu ler.</caption>';
		$html .= $cabeca . '<tbody>';
		foreach ( (array) $d['tabela']['externas'] as $l ) {
			$html .= $linha( $l );
		}
		$html .= '</tbody></table></div>';
		$html .= '<ul class="rdm-fonte">';
		foreach ( (array) $d['tabela']['externas'] as $l ) {
			$html .= '<li><b>' . esc_html( $l['rotulo'] ) . '</b> — ' . esc_html( $l['fonte'] )
				. ( empty( $l['nota'] ) ? '' : '. ' . esc_html( $l['nota'] ) ) . '</li>';
		}
		$html .= '</ul>';
	}

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * AS DOBRAS (32.1, item 7) — o texto inteiro continua no HTML servido
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_dobras_html' ) ) {
function rodametria_f2_dobras_html( $d ) {
	$c = $d['constantes_usadas'];
	$f = $d['fatores_de_relevo_tela'];

	/* --- como chegamos no numero --- */
	$conta  = '<p>A conta tem três degraus, e eles têm força de prova diferente. A gente os '
		. 'mantém separados de propósito: misturar identidade matemática com medição de '
		. 'terceiro e com decisão nossa é como se publica número sem procedência.</p>';
	$conta .= '<h3>Degrau 1 — a energia</h3>';
	$conta .= '<p><span class="rdm-num">Wh = V × Ah</span>. Isso é identidade de unidades, não '
		. 'fonte: volt vezes ampère-hora dá watt-hora, e não depende de ninguém publicar nada. '
		. 'É também metade do valor desta página, porque o anúncio compara autonomia por '
		. '<em>watt do motor</em> — e watt de motor não é a grandeza que armazena energia.</p>';
	$conta .= '<h3>Degrau 2 — o relevo, por razão e nunca por valor absoluto</h3>';
	$conta .= '<p>Na mesma rota, com o mesmo veículo e a mesma bateria, a medição de Quito '
		. 'registrou <span class="rdm-num">97,74</span> Wh/km numa subida de 12% de inclinação '
		. 'média contra <span class="rdm-num">41,29</span> Wh/km no trecho plano. A razão entre '
		. 'os dois é <span class="rdm-num">' . esc_html( $f['ladeira'] ) . '</span>, e é ela que a '
		. 'gente usa — nunca os valores absolutos, que são de uma moto de 1.800 Wh e não '
		. 'transferem para patinete.</p>';
	$conta .= '<p>O relevo “pouca subida” é <span class="rdm-num">' . esc_html( $f['misto'] )
		. '</span>, e esse número é <strong>decisão da Rodametria</strong>, não medição: é o '
		. 'meio-caminho geométrico entre os dois extremos medidos. A gente escolheu o geométrico '
		. 'e não a média simples porque a grandeza é um multiplicador, e a média simples puxaria '
		. 'o meio para perto da ladeira sem base. O estudo também mediu uma condição mista, mas a '
		. 'mista dele é a rota dele, com a proporção de subida dele — usar aquele número aqui '
		. 'seria emprestar a geografia de Quito ao seu trajeto.</p>';
	$conta .= '<h3>Degrau 3 — o consumo por km, e ele não existe aqui</h3>';
	$conta .= '<p>Para dizer quantos km uma bateria faz <em>sem</em> olhar o número do anúncio, '
		. 'faltaria uma régua de quantos watt-hora um patinete gasta por quilômetro. A gente '
		. 'procurou e não publicou nenhuma, e os motivos de cada candidato estão logo abaixo. '
		. 'Enquanto não houver, esta página degrada o número que o fabricante declarou — e diz '
		. 'que é isso que está fazendo.</p>';

	/* --- as reguas, uma a uma, com fonte e data --- */
	$reguas = '<ul>';
	foreach ( $c as $id => $k ) {
		$valor = $k['valor'];
		$reguas .= '<li><b>' . esc_html( rodametria_f2_nome_da_regua( $id ) ) . '</b> — '
			. ( null === $valor
				? 'sem valor publicável.'
				: '<span class="rdm-num">' . esc_html( is_string( $valor ) ? $valor
					: rodametria_f2_numero( $valor ) ) . '</span>.' )
			. ' Tipo: ' . esc_html( rodametria_f2_nome_do_tipo( $k['tipo'] ) ) . '.'
			. ( empty( $k['fonte'] ) ? '' : ' ' . esc_html( $k['fonte'] ) )
			. ( empty( $k['url'] ) ? '' : ' <a href="' . esc_url( $k['url'] )
				. '" rel="nofollow noopener">fonte</a>' )
			. ( empty( $k['verificado_em'] ) ? '' : ' Lido em '
				. esc_html( rodametria_f2_data( $k['verificado_em'] ) ) . '.' )
			. '</li>';
	}
	$reguas .= '</ul>';

	/* --- perguntas frequentes, e as respostas sao as recusas da 2.4 --- */
	$faq  = '<h3>Por que vocês não dizem direto quantos km ele faz?</h3>';
	$faq .= '<p>Porque para isso faltaria o degrau 3 acima, e a gente não inventa número. Com os '
		. 'km do anúncio na mão, o que esta página faz é descontar o relevo e mostrar os '
		. 'watt-hora ao lado — quem conclui é você.</p>';
	$faq .= '<h3>Vocês estão dizendo que o fabricante mente?</h3>';
	$faq .= '<p>Não. A gente põe os watt-hora ao lado do número declarado e a faixa descontada '
		. 'pelo relevo. O número do fabricante costuma ser de condição ideal; o seu trajeto não é '
		. 'condição ideal.</p>';
	$faq .= '<h3>E o meu peso, não conta nada?</h3>';
	$faq .= '<p>Conta na vida real, e não conta na nossa conta — e isso está dito na resposta em '
		. 'vez de disfarçado. A gente não achou, em fonte que alcance, nenhuma régua de quantos '
		. 'watt-hora por km cada quilo de quem pilota custa. O seu peso entra aqui escolhendo o '
		. 'que esperar da faixa, e numa pergunta mais dura: se o modelo aguenta você.</p>';
	$faq .= '<h3>Serve para bateria usada?</h3>';
	$faq .= '<p>Não. Bateria perde capacidade com os ciclos, e a gente não tem fonte para dizer '
		. 'quanto. A conta aqui é da bateria como ela é declarada.</p>';

	/* --- como sabemos --- */
	$como  = '<p>Toda linha da tabela traz de onde ela saiu. As combinações de bateria vieram das '
		. 'fichas que a gente colheu dos anúncios, com a data da leitura; as duas medições de '
		. 'terceiros estão nomeadas com autor, instituição e ano, e ficam em bloco separado '
		. 'justamente para ninguém as confundir com ficha de loja.</p>';
	$como .= '<p>O que a gente <em>não</em> publicou, e por quê, está na lista das réguas acima: '
		. 'candidato reprovado por canal de leitura, por classe de veículo errada, por conta '
		. 'circular ou por interesse comercial do publicador. A gente prefere dizer “não sabemos” '
		. 'a preencher a lacuna com estimativa.</p>';
	$como .= '<p class="rdm-fonte">Esta página foi gerada a partir do nosso banco em '
		. esc_html( rodametria_f2_data( isset( $d['gerado_em'] ) ? $d['gerado_em'] : '' ) )
		. ', e o número de veículos citado nela é contado no banco, nunca escrito à mão.</p>';

	return rodametria_casca_dobra( 'Como chegamos nesse número', $conta )
		. rodametria_casca_dobra( 'As réguas que a conta usa, uma a uma', $reguas )
		. rodametria_casca_dobra( 'Perguntas frequentes', $faq )
		. rodametria_casca_dobra( 'Como sabemos', $como );
}
}

if ( ! function_exists( 'rodametria_f2_nome_da_regua' ) ) {
function rodametria_f2_nome_da_regua( $id ) {
	$mapa = array(
		'energia-wh-tensao-vezes-amperagem'            => 'Watt-hora = volt × ampère-hora',
		'fator-relevo-ladeira-contra-plano'            => 'Quanto a ladeira custa contra o plano',
		'fator-relevo-misto'                           => 'O multiplicador de “pouca subida”',
		'calibracao-autonomia-declarada-contra-medida' => 'Quanto do declarado uma medição real entregou',
		'consumo-absoluto-wh-por-km-patinete'          => 'Consumo de um patinete por km',
		'teto-de-carga-do-mercado-brasileiro'          => 'Maior carga máxima que vimos no varejo',
	);

	return isset( $mapa[ $id ] ) ? $mapa[ $id ] : $id;
}
}

if ( ! function_exists( 'rodametria_f2_nome_do_tipo' ) ) {
function rodametria_f2_nome_do_tipo( $tipo ) {
	$mapa = array(
		'identidade_matematica' => 'identidade matemática, não depende de fonte',
		'medicao_de_terceiro'   => 'medição de terceiro, nomeada',
		'decisao_da_ilha'       => 'decisão nossa, e está dito que é nossa',
		'pendente'              => 'pendente, sem valor publicado',
	);

	return isset( $mapa[ $tipo ] ) ? $mapa[ $tipo ] : (string) $tipo;
}
}

/* ---------------------------------------------------------------------------
 * A PAGINA INTEIRA, NA ORDEM DA 32.1
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f2_pagina_html' ) ) {
function rodametria_f2_pagina_html() {
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );

	if ( ! $d || empty( $d['campos'] ) || empty( $d['resposta_exemplo'] ) ) {
		/* Pagina DEGRADADA e honesta. Nunca molde cru, nunca numero inventado. */
		return '<div class="rdm-faixa rdm-pagina">'
			. rodametria_casca_trilha_html()
			. '<h1>Quantos km o patinete elétrico faz de verdade</h1>'
			. '<p class="rdm-promessa">A calculadora está fora do ar neste momento: o banco de '
			. 'dados que alimenta as contas não chegou ao site nesta atualização. Nenhum número '
			. 'desta página é estimado, então ela prefere não responder a responder errado.</p>'
			. '</div>';
	}

	$itens = rodametria_f2_itens_da_vitrine( $d );

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>Quantos km o patinete elétrico faz de verdade</h1>';
	$html .= '<p class="rdm-promessa">Diga a tensão e a amperagem da bateria: saem os watt-hora e '
		. 'a faixa de km do seu trajeto, ao lado do número que o anúncio promete.</p>';

	$html .= rodametria_f2_formulario_html( $d );
	$html .= rodametria_f2_resultado_html( $d );

	/* A frase de abertura NAO E DIGITADA AQUI. Ate 29/10/2026 ela era, e dizia
	   "Nenhum destes entrou pela conta de Wh" — afirmacao sobre o estado do
	   banco, escrita a mao, que nenhum portao conferia e que viraria mentira
	   calada no dia em que um registro declarasse V e Ah com oferta aberta.
	   Agora ela sai contada da propria vitrine, em gerar-f2.py. */
	$html .= rodametria_casca_bloco_de_compra(
		'À venda agora, e o que cada um é',
		$itens,
		(string) $d['compra']['frase_de_abertura'],
		'Nenhum veículo do nosso banco tem oferta aberta neste momento.' );

	$html .= rodametria_f2_ressalva_html( $d );

	$html .= '<h2>Quem entrou, quem não entrou, e por quê</h2>';
	$html .= rodametria_f2_contas_html( $d );

	$html .= '<h2>Já calculado para outras baterias</h2>';
	$html .= rodametria_f2_tabela_html( $d );

	foreach ( (array) $d['resposta_exemplo']['frases_calibracao'] as $f ) {
		$html .= '<p>' . esc_html( $f ) . '</p>';
	}

	$html .= '<h2>O resto da conta</h2>';
	$html .= rodametria_f2_dobras_html( $d );

	$html .= '</div>';

	return $html;
}
}

add_shortcode( 'rodametria_f2', 'rodametria_f2_pagina_html' );

/* ---------------------------------------------------------------------------
 * JSON-LD da ferramenta — e ele nao repete o BreadcrumbList, que e da casca
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! rodametria_f2_na_pagina() ) {
		return;
	}
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );
	if ( ! $d ) {
		return;
	}

	$perguntas = array(
		array(
			'Quantos km um patinete elétrico faz de verdade?',
			'Depende da energia da bateria (volt × ampère-hora = watt-hora) e do relevo do '
				. 'trajeto. A Rodametria desconta o relevo do número que o fabricante declara, '
				. 'pela razão medida entre subida de 12% e trecho plano, e mostra os watt-hora '
				. 'ao lado. Não estimamos km sem o número declarado: falta uma medição de '
				. 'consumo por km de patinete em fonte que a gente consiga ler.',
		),
		array(
			'Como calcular os watt-hora da bateria de um patinete?',
			'Multiplique a tensão pela amperagem: 48 V × 20 Ah são 960 Wh; 60 V × 20 Ah são '
				. '1.200 Wh. É identidade de unidades, não estimativa. O watt do motor não '
				. 'serve para isso — ele não é a grandeza que armazena energia.',
		),
		array(
			'O peso de quem pilota muda a autonomia?',
			'Muda na vida real, mas a Rodametria não converte peso em km: não existe, em fonte '
				. 'que a gente consiga ler, régua de quantos watt-hora por km cada quilo de '
				. 'condutor custa. O peso entra na expectativa — com peso alto e ladeira, espere '
				. 'o piso da faixa — e na pergunta sobre a carga máxima do modelo.',
		),
	);

	$faq = array( '@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => array() );
	foreach ( $perguntas as $p ) {
		$faq['mainEntity'][] = array(
			'@type'          => 'Question',
			'name'           => $p[0],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
		);
	}

	echo '<script type="application/ld+json">'
		. wp_json_encode( $faq, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
		. '</script>' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * O JS DA F2 — NO RODAPE, E ELE NAO ESCREVE UMA FRASE SOZINHO
 *
 * Os moldes de frase e os fatores de relevo viajam da MESMA option que o PHP
 * leu. O navegador preenche o molde; ele nao tem texto proprio. E por isso que
 * a pagina nao pode dizer uma coisa no HTML servido e outra depois do clique.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! rodametria_f2_na_pagina() ) {
		return;
	}
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2 );
	if ( ! $d ) {
		return;
	}

	$pacote = array(
		'fatores'   => $d['fatores_de_relevo'],
		'moldes'    => $d['frases_molde'],
		'relevo'    => $d['relevo_frase'],
		'degrau3'   => ! empty( $d['degrau_3_disponivel'] ),
		'tetoCarga' => isset( $d['constantes_usadas']['teto-de-carga-do-mercado-brasileiro']['valor'] )
			? $d['constantes_usadas']['teto-de-carga-do-mercado-brasileiro']['valor'] : null,
		'calibracao' => isset( $d['constantes_usadas']['calibracao-autonomia-declarada-contra-medida']['valor'] )
			? $d['constantes_usadas']['calibracao-autonomia-declarada-contra-medida']['valor'] : null,
	);
	?>
<script id="rodametria-f2-js">
(function(){
  var D = <?php echo wp_json_encode( $pacote, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ); ?>;
  var form = document.querySelector('[data-rdm-f2-form]');
  var caixa = document.querySelector('[data-rdm-f2-caixa]');
  if (!form || !caixa) { return; }

  function num(x, casas){
    casas = casas || 0;
    var s = (Math.round(x * Math.pow(10, casas)) / Math.pow(10, casas))
      .toFixed(casas);
    var p = s.split('.');
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return p.join(',');
  }
  function preencher(molde, vals){
    return molde.replace(/\{(\w+)\}/g, function(_, k){
      return (k in vals) ? vals[k] : '{' + k + '}';
    });
  }
  function fracao(txt){
    if (txt.indexOf('/') === -1) { return parseFloat(txt); }
    var p = txt.split('/');
    return parseFloat(p[0]) / parseFloat(p[1]);
  }

  var elV = form.querySelector('[data-rdm-f2-v]');
  var elAh = form.querySelector('[data-rdm-f2-ah]');
  var elPeso = form.querySelector('[data-rdm-f2-peso]');
  var elRelevo = form.querySelector('[data-rdm-f2-relevo]');
  var elAut = form.querySelector('[data-rdm-f2-aut]');

  function responder(){
    var v = parseFloat(elV.value);
    var ah = parseFloat(elAh.value);
    var peso = parseFloat(elPeso.value);
    var relevo = elRelevo.value;
    var aut = elAut.value === '' ? null : parseFloat(elAut.value);
    if (!(v > 0) || !(ah > 0) || !(peso > 0)) { return; }

    var wh = v * ah;
    var fator = fracao(String(D.fatores[relevo]));
    var frases = [];
    frases.push(preencher(D.moldes.wh, {v: num(v), ah: num(ah, 1), wh: num(wh)}));

    var rotulo, numero, unidade;
    if (aut !== null && aut > 0) {
      var piso = aut / fator;
      if (piso === aut) {
        frases.push(preencher(D.moldes.km_plano, {teto: num(aut)}));
        numero = num(aut);
      } else {
        frases.push(preencher(D.moldes.km_degradado, {
          relevo_frase: D.relevo[relevo] || relevo,
          piso: num(piso), teto: num(aut)
        }));
        numero = num(piso) + ' a ' + num(aut);
      }
      rotulo = D.moldes.rotulo_km;
      unidade = 'km';
    } else {
      frases.push(D.moldes.km_recusa);
      rotulo = D.moldes.rotulo_wh;
      numero = num(wh);
      unidade = 'Wh';
    }

    /* A RESSALVA DO PESO, abaixo do bloco de compra. Ela NAO sobe para a caixa:
       o item 2 do despacho de 30/10/2026 foi fechado pela segunda saida (o peso
       sai da PROMESSA), porque a primeira foi medida em navegador a 390 px e nao
       cabe — frase nova na caixa custa 97 px FIXOS e a 32.5 tinha 20 px de folga.
       E `peso_ladeira` so nasce onde existe faixa com DUAS PONTAS: ela fala do
       PISO DA FAIXA, e com ladeira sem autonomia declarada a caixa RECUSA o km,
       entao a ressalva mandava esperar o piso de uma faixa que nao existe. */
    var faixaComDuasPontas = (aut !== null && aut > 0 && fator !== 1);
    var ressalvas = [preencher(D.moldes.peso, {peso: num(peso)})];
    if (relevo === 'ladeira' && faixaComDuasPontas) {
      ressalvas.push(preencher(D.moldes.peso_ladeira, {peso: num(peso)}));
    }
    if (D.tetoCarga !== null && peso > D.tetoCarga) {
      ressalvas.push(preencher(D.moldes.peso_acima_do_teto, {
        peso: num(peso), teto_carga: num(D.tetoCarga)
      }));
    }

    caixa.querySelector('.rdm-molde-caixa-rotulo').textContent = rotulo;
    caixa.querySelector('.rdm-molde-caixa-numero').innerHTML =
      '<span class="rdm-num"></span> <span class="rdm-molde-caixa-unidade"></span>';
    caixa.querySelector('.rdm-molde-caixa-numero .rdm-num').textContent = numero;
    caixa.querySelector('.rdm-molde-caixa-unidade').textContent = unidade;

    var antigas = caixa.querySelectorAll('.rdm-molde-caixa-frase');
    for (var i = 0; i < antigas.length; i++) { antigas[i].remove(); }
    frases.forEach(function(f){
      var p = document.createElement('p');
      p.className = 'rdm-molde-caixa-frase';
      p.textContent = f;
      caixa.appendChild(p);
    });

    var alvoRessalva = document.querySelector('[data-rdm-f2-ressalva]');
    if (alvoRessalva) {
      alvoRessalva.textContent = '';
      ressalvas.forEach(function(f){
        var p = document.createElement('p');
        p.textContent = f;
        alvoRessalva.appendChild(p);
      });
    }

    var barra = document.querySelector('[data-rdm-barra]');
    if (barra) {
      barra.querySelector('[data-rdm-barra-numero]').textContent = numero;
      barra.querySelector('.rdm-molde-barra-rotulo').textContent = rotulo;
    }
  }

  [elV, elAh, elPeso, elRelevo, elAut].forEach(function(el){
    el.addEventListener('change', responder);
    el.addEventListener('input', responder);
  });
  form.addEventListener('submit', function(e){
    e.preventDefault();
    responder();
    caixa.scrollIntoView({behavior: 'smooth', block: 'start'});
  });
})();
</script>
	<?php
}, 30 );

/* ---------------------------------------------------------------------------
 * INSTALACAO DA PAGINA — pelo gancho da casca, nunca em toda requisicao
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_instalar', function ( $relato ) {
	$p = rodametria_casca_garantir_pagina(
		RODAMETRIA_F2_SLUG,
		'Quantos km o patinete elétrico faz de verdade',
		'[rodametria_f2]' );

	if ( empty( $p['id'] ) ) {
		$relato[] = 'f2: ERRO — ' . ( isset( $p['erro'] ) ? $p['erro'] : 'sem id' );

		return $relato;
	}
	$relato[] = 'f2: #' . $p['id'] . ' (' . $p['slug'] . ')'
		. ( empty( $p['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );

	return $relato;
} );

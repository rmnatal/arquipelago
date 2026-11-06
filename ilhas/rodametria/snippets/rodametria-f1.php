<?php
/**
 * RODAMETRIA — F1: "ESSE ELETRICO PRECISA DE CNH?"
 *
 * A ferramenta que a ilha existe para ter, e a razao do nicho: o bloco 1 mediu
 * SETE consultas independentes do eixo da CNH e nao achou UMA ferramenta que
 * receba potencia e velocidade e devolva categoria. *"Todos falam, ninguem
 * calcula."*
 *
 * ELA FICOU NOVE DIAS SEM PODER IR AO AR, e o motivo esta escrito no comentario
 * da home desta casca: o limiar legal estava `pendente` porque o texto oficial
 * da Resolucao Contran 996/2023 nao abre pelo canal de leitura desta nuvem. Em
 * 05/11/2026, ~23h3x de Brasilia, o Raphael abriu o PDF oficial do Ministerio
 * dos Transportes no Chrome dele e preencheu a secao 5 de
 * `dados/fonte-oficial-f1.md`. A constante destravou editando UM objeto JSON, e
 * nenhuma linha de logica mudou — era essa a aposta da secao 1.3 da
 * especificacao, e ela pagou.
 *
 * ESTE ARQUIVO NAO DIGITA UM NUMERO E NAO ESCREVE UMA FRASE DE RESPOSTA. Tudo
 * vem da option que o Sync grava de `dados/f1-respostas.json`, que e escrito por
 * `ferramentas/gerar-f1.py` a partir de `regras/f1.py` e de
 * `dados/constantes.json`.
 *
 * O QUE ESTA FERRAMENTA NAO RESPONDE, E ELA DIZ ISSO NA PRIMEIRA TELA: a
 * exigencia de HABILITACAO. A 996/2023 nao tem artigo nenhum sobre CNH — decide
 * a CATEGORIA e decide PLACA, REGISTRO, LICENCIAMENTO (arts. 12 e 13) e
 * CAPACETE (art. 19 V). Habilitacao vem do CTB, que esta ilha ainda nao leu em
 * fonte oficial. A constante `exigencia-de-habilitacao-por-categoria-ctb` nasceu
 * `pendente` para esse silencio ter NOME, e o portao da ferramenta cobra que as
 * frases "dispensa CNH" e "exige habilitacao" NAO apareçam em texto de tela
 * enquanto ela for pendente. O `VOZ.md` traz as duas nos exemplos aprovados,
 * escritos em 27/10 — antes de alguem ter lido a resolucao — e o mesmo `VOZ.md`
 * proibe nominalmente *"qualquer frase que afirme o que a resolucao nao diz"*.
 * Onde os dois lados dele divergem, manda a proibicao.
 *
 * E ELA E A HOME, nao uma pagina nova: a casca promete isso desde 29/10 com
 * todas as letras — *"no dia em que a resolucao for lida, a F1 toma a primeira
 * tela da home e os cartoes descem, e NENHUMA URL muda, que e o que a 32.3
 * protege"*. Entao este snippet nao cria pagina: ele se pendura em DOIS filtros
 * novos da casca (`rodametria_home_ferramenta` e `rodametria_home_cartoes`),
 * pela 32.6-b — a casca nao cresce quando a ilha cresce, e a ferramenta nao
 * edita a casca para aparecer.
 *
 * E O JS ESTA NO RODAPE, NUNCA DENTRO DO SHORTCODE. O WordPress roda os filtros
 * do the_content sobre o retorno do shortcode e troca && por &#038;&#038;,
 * matando o script — o defeito que derrubou cinco calculadoras da Aquametria em
 * 08/09/2026.
 */

if ( ! defined( 'RODAMETRIA_F1_VERSAO' ) ) {
	define( 'RODAMETRIA_F1_VERSAO', '1.0.0' );
}

if ( ! defined( 'RODAMETRIA_ID_DADOS_F1' ) ) {
	define( 'RODAMETRIA_ID_DADOS_F1', 'f1-respostas' );
}

/* A VERSAO DESTE SNIPPET VAI AO AR, pela 20.7. A chave e o `id` do
   manifest.json, nunca o nome da constante — e a AUSENCIA dela no /casca e o
   sinal de snippet gravado e NAO ativado, que e a cicatriz da 20.4. */
add_filter( 'rodametria_versoes', function ( $v ) {
	$v['rodametria-f1'] = RODAMETRIA_F1_VERSAO;

	return $v;
} );

if ( ! function_exists( 'rodametria_f1_na_pagina' ) ) {
function rodametria_f1_na_pagina() {
	return is_front_page();
}
}

if ( ! function_exists( 'rodametria_f1_banco' ) ) {
function rodametria_f1_banco() {
	$d = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F1 );
	if ( ! is_array( $d ) || empty( $d['campos'] ) || empty( $d['resposta_exemplo'] ) ) {
		return null;
	}

	/* O PORTAO DE DADO DO PROPRIO SNIPPET: sem limiar nao ha ferramenta, e a
	   ferramenta NAO aparece. Nao e defesa teorica — foi o estado real desta
	   pagina por nove dias, e o dia em que a constante voltar a `pendente` (por
	   erro de fase, por exemplo) a home tem de voltar a ser HUB sozinha, sem
	   ninguem editar PHP. Ler o status aqui e o que faz isso acontecer. */
	if ( empty( $d['limiares'] ) ) {
		return null;
	}

	return $d;
}
}

/* ---------------------------------------------------------------------------
 * O FORMULARIO (32.1, item 3) — JA PREENCHIDO, E O PIVO NO MESMO NIVEL VISUAL
 *
 * A 1.1 e literal sobre o campo 3: *"na tela ele e um par de botoes de radio no
 * mesmo nivel visual dos dois numeros, nunca um checkbox abaixo do botao de
 * calcular"*. Ele nao e caixinha opcional: sem ele NENHUMA potencia classifica.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_formulario_html' ) ) {
function rodametria_f1_formulario_html( $d ) {
	$ex = $d['campos']['exemplo'];
	$r  = $d['rotulos'];

	$opcoes = function ( $lista, $atual, $sufixo ) {
		$html = '';
		foreach ( $lista as $v ) {
			$html .= '<option value="' . esc_attr( $v ) . '"'
				. ( (float) $v === (float) $atual ? ' selected' : '' ) . '>'
				. esc_html( rodametria_f1_numero( $v ) . ' ' . $sufixo ) . '</option>';
		}

		return $html;
	};

	$html  = '<form class="rdm-f-formulario rdm-f1" data-rdm-f1-form'
		. ' method="get" action="' . esc_url( home_url( '/' ) ) . '">';
	$html .= '<div class="rdm-f-campos">';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f1-w">' . esc_html( $r['potencia_nominal_w'] )
		. '</label><select id="rdm-f1-w" name="w" data-rdm-f1-w>'
		. $opcoes( $d['campos']['potencias_w'], $ex['potencia_nominal_w'], 'W' )
		. '</select><span class="rdm-f-dica">A da ficha, não a do título do anúncio</span></p>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f1-kmh">' . esc_html( $r['velocidade_max_kmh'] )
		. '</label><select id="rdm-f1-kmh" name="kmh" data-rdm-f1-kmh>'
		. $opcoes( $d['campos']['velocidades_kmh'], $ex['velocidade_max_kmh'], 'km/h' )
		. '</select><span class="rdm-f-dica">A de fábrica, não a que ele já fez</span></p>';

	/* O PIVO. Radio, no mesmo nivel dos dois numeros (1.1). O terceiro valor do
	   enum (`nao_declarado`) NAO entra como opcao de formulario: aqui e a PESSOA
	   que responde, e ela sabe se o veiculo dela tem acelerador. `nao_declarado`
	   e para o BANCO, onde ele significa "a ficha nao diz". */
	$html .= '<fieldset class="rdm-f-campo rdm-f-campo-pivo">'
		. '<legend>' . esc_html( $r['acelerador'] ) . '</legend>';
	foreach ( array( 'manual', 'so_pedal_assistido' ) as $opt ) {
		$id = 'rdm-f1-acel-' . str_replace( '_', '-', $opt );
		$html .= '<label class="rdm-f-radio" for="' . esc_attr( $id ) . '">'
			. '<input type="radio" id="' . esc_attr( $id ) . '" name="acel" value="' . esc_attr( $opt ) . '"'
			. ( $opt === $ex['acelerador'] ? ' checked' : '' ) . ' data-rdm-f1-acel>'
			. '<span>' . esc_html( $r[ 'acelerador_' . $opt ] ) . '</span></label>';
	}
	$html .= '<span class="rdm-f-dica">É o que mais muda a resposta</span></fieldset>';

	$html .= '<p class="rdm-f-campo"><label for="rdm-f1-mun">' . esc_html( $r['municipio'] )
		. '</label><input id="rdm-f1-mun" name="mun" type="text" autocomplete="address-level2"'
		. ' value="' . esc_attr( (string) $ex['municipio'] ) . '" data-rdm-f1-mun>'
		. '<span class="rdm-f-dica">A categoria é nacional; o limite da rua é local</span></p>';

	$html .= '</div>';
	$html .= '<p class="rdm-f-acao"><button class="rdm-f-botao" type="submit">Ver a categoria</button></p>';
	$html .= '</form>';

	return $html;
}
}

/** Numero em portugues, para rotulo de opcao. Nenhuma conta mora aqui. */
if ( ! function_exists( 'rodametria_f1_numero' ) ) {
function rodametria_f1_numero( $v ) {
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
 * O numero grande da caixa da F1 NAO e um numero: e a CATEGORIA. Entao o lugar
 * do numero recebe o nome curto dela e a unidade fica vazia — a categoria e o
 * veredito, e veredito e o que a pessoa le primeiro.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_nome_curto' ) ) {
function rodametria_f1_nome_curto( $categoria ) {
	/* O nome CURTO da caixa, e ele e diferente do nome longo que a prosa usa.
	   Os dois saem do banco: o longo em `nome_da_categoria`, o curto aqui, e o
	   curto existe porque "equipamento de mobilidade individual autopropelido"
	   nao cabe no lugar do numero a 390 px. Nenhum dos dois e inventado — o
	   curto e a primeira palavra do longo, que e como a propria resolucao o
	   chama no corpo do texto. */
	$curtos = array(
		'bicicleta_eletrica'  => 'bicicleta elétrica',
		'autopropelido'       => 'autopropelido',
		'ciclomotor'          => 'ciclomotor',
		'acima_do_ciclomotor' => 'acima do ciclomotor',
	);

	return isset( $curtos[ $categoria ] ) ? $curtos[ $categoria ] : '';
}
}

if ( ! function_exists( 'rodametria_f1_resultado_html' ) ) {
function rodametria_f1_resultado_html( $d ) {
	$r = $d['resposta_exemplo'];

	$frases = array();
	foreach ( (array) $r['frases_categoria'] as $f ) {
		$frases[] = $f;
	}

	$classifica = ! empty( $r['classifica'] );
	$numero     = $classifica ? rodametria_f1_nome_curto( $r['categoria'] ) : 'sem resposta';
	$rotulo     = $d['rotulos']['titulo_categoria'];
	$tom        = (string) $r['tom'];

	$html  = rodametria_casca_caixa( $rotulo, $numero, '', $frases, $tom,
		' data-rdm-f1-caixa' );

	/* A CAMADA 2 EM BLOCO SEPARADO, COM TITULO PROPRIO (1.2). A especificacao e
	   literal: *"as duas camadas saem em blocos separados com titulo proprio.
	   Fundi-las numa frase e o defeito que a secao 7 nomeia como inventar uma
	   das causas."* O conteiner existe no HTML mesmo para o navegador reescrever
	   a camada 2 quando a pessoa troca a cidade. */
	$html .= '<div class="rdm-f1-municipal" data-rdm-f1-municipal>';
	$html .= '<h2 class="rdm-f1-municipal-titulo">'
		. esc_html( $d['rotulos']['titulo_municipal'] ) . '</h2>';
	foreach ( (array) $r['frases_municipal'] as $f ) {
		$html .= '<p>' . esc_html( $f ) . '</p>';
	}
	$html .= '</div>';

	$html .= rodametria_casca_barra_fixa( $rotulo, $numero, '' );

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * AS RESSALVAS (1.4) — abaixo do bloco de compra, e elas NAO sao rodape
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_ressalva_html' ) ) {
function rodametria_f1_ressalva_html( $d ) {
	$html = '<div class="rdm-f1-ressalva" data-rdm-f1-ressalva>';
	if ( ! empty( $d['resposta_exemplo']['frases_ressalva'] ) ) {
		$html .= '<h2>' . esc_html( $d['rotulos']['titulo_ressalva'] ) . '</h2>';
		foreach ( (array) $d['resposta_exemplo']['frases_ressalva'] as $f ) {
			$html .= '<p>' . esc_html( $f ) . '</p>';
		}
	}
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A PRESTACAO DE CONTAS DA SECAO 7 (1.7) — TODO veiculo aparece UMA VEZ
 *
 * Os nomes e a contagem saem do banco, contados por `grupos_de_compra()` em
 * `regras/f1.py`. Nenhum numero e digitado aqui, e a soma dos grupos fecha o
 * total de registros — a assercao mora na propria funcao que agrupa.
 *
 * E O QUE ESTA SECAO PUBLICA HOJE E A TESE DA ILHA, nao um buraco nela: ZERO
 * dos registros declara potencia NOMINAL, contra 14 que declaram um watt SEM
 * ROTULO. A F1 nao tem o que vender porque o varejo nao publica o numero que a
 * regra le — e a pagina diz isso com os nomes contados.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_contas_html' ) ) {
function rodametria_f1_contas_html( $d ) {
	$c = $d['compra'];
	$grupos = array(
		'cabem_na_categoria'   => 'Cabem nesta categoria',
		'de_outra_categoria'   => 'São de outra categoria',
		'nao_declaram_nominal' => 'Não dá para classificar: a ficha não declara o que a regra lê',
		'sem_saida_de_compra'  => 'Classificam, mas ainda não têm saída de compra',
		'fora_do_banco'        => 'Fora do banco, e cada um diz por quê',
	);

	$html  = '<p>Nossa regra é simples e a gente a cumpre à vista: <b>todo</b> veículo que a '
		. 'gente colheu aparece aqui exatamente uma vez, no grupo que explica por que ele está '
		. 'ou não está na recomendação. A soma fecha os '
		. '<span class="rdm-num">' . (int) $c['total_registros_veiculos'] . '</span> '
		. 'registros do banco, contada e nunca digitada.</p>';

	$html .= '<ul class="rdm-contas">';
	foreach ( $grupos as $chave => $titulo ) {
		$nomes = isset( $c['nomes_por_grupo'][ $chave ] ) ? (array) $c['nomes_por_grupo'][ $chave ] : array();
		$html .= '<li><b>' . esc_html( $titulo ) . ':</b> '
			. '<span class="rdm-num">' . count( $nomes ) . '</span>';
		if ( $nomes ) {
			$html .= ' — ' . esc_html( implode( ', ', $nomes ) );
		}
		$html .= '</li>';
	}
	$html .= '</ul>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A TABELA DA REGRA (32.1, item 6) — visivel, NUNCA recolhida
 *
 * POR QUE ELA EXISTE E A 1.6 NAO A PREVIA: a 1.6 pede uma tabela de combinacoes
 * colhidas e proibe grade sintetica. Esta nao e nem uma nem outra — ela e a
 * FONTE pre-renderizada, uma linha por categoria, com o artigo ao lado. E a
 * unica coisa desta pagina que responde a quem NAO sabe os numeros do proprio
 * veiculo, e e a metade que a visao geral de IA le sem preencher formulario.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_tabela_regra_html' ) ) {
function rodametria_f1_tabela_regra_html( $d ) {
	$html  = '<div class="rdm-tabela-rolagem"><table class="rdm-tabela">';
	$html .= '<caption>Os limites que a Resolução Contran nº 996/2023 fixa para cada categoria, '
		. 'com o artigo de onde cada linha saiu. Watt é potência nominal; km/h é velocidade '
		. 'máxima de fábrica.</caption>';
	$html .= '<thead><tr><th scope="col">Categoria</th>'
		. '<th scope="col" class="rdm-num">W</th><th scope="col" class="rdm-num">km/h</th>'
		. '<th scope="col">Acelerador</th><th scope="col">Tamanho</th>'
		. '<th scope="col">Registro e placa</th><th scope="col">Artigo</th></tr></thead><tbody>';

	foreach ( (array) $d['tabela_regra'] as $l ) {
		$html .= '<tr><th scope="row">' . esc_html( $l['nome'] ) . '</th>';
		$html .= '<td class="rdm-num">' . esc_html( $l['potencia_w'] ) . '</td>';
		$html .= '<td class="rdm-num">' . esc_html( $l['velocidade_kmh'] ) . '</td>';
		$html .= '<td>' . esc_html( $l['acelerador'] ) . '</td>';
		$html .= '<td>' . esc_html( $l['dimensao'] ) . '</td>';
		$html .= '<td>' . esc_html( $l['placa'] ) . '</td>';
		$html .= '<td>' . esc_html( $l['artigo'] ) . '</td></tr>';
	}

	$html .= '</tbody></table></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * A TABELA DO BANCO (1.6) — e a coluna `categoria` NASCE, com a recusa dentro
 *
 * A 1.6 dizia: *"a coluna categoria desta tabela esta VAZIA neste bloco, e isso
 * e proposital. Ela so pode ser preenchida pelos limiares da 1.3."* Os limiares
 * chegaram e a coluna nasceu — com o que a arvore devolve para cada registro,
 * que hoje e RECUSA em todos, porque nenhum declara o watt nominal. A coluna
 * nao fica vazia e NAO e preenchida com o watt sem rotulo: ela diz a causa.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_causa_na_tela' ) ) {
function rodametria_f1_causa_na_tela( $causa ) {
	$frases = array(
		'acelerador_nao_declarado'  => 'a ficha não diz se tem acelerador',
		'potencia_nominal_ausente'  => 'o watt do anúncio não diz se é nominal',
		'velocidade_max_ausente'    => 'a ficha não declara a velocidade de fábrica',
		'entrada_nao_positiva'      => 'o número declarado não é utilizável',
		'limiar_legal_pendente'     => 'ainda não lemos o texto oficial',
	);

	return isset( $frases[ $causa ] ) ? $frases[ $causa ] : 'não classificável';
}
}

if ( ! function_exists( 'rodametria_f1_tabela_banco_html' ) ) {
function rodametria_f1_tabela_banco_html( $d ) {
	$t = $d['tabela_banco'];

	$html  = '<div class="rdm-tabela-rolagem"><table class="rdm-tabela">';
	$html .= '<caption>Os anúncios que a gente colheu, com o que cada ficha declara. A última '
		. 'coluna é o que a regra consegue dizer sobre cada um — e onde ela não consegue, diz '
		. 'por quê.</caption>';
	$html .= '<thead><tr><th scope="col">Anúncio</th>'
		. '<th scope="col" class="rdm-num">W nominal</th>'
		. '<th scope="col" class="rdm-num">W sem rótulo</th>'
		. '<th scope="col" class="rdm-num">km/h</th>'
		. '<th scope="col">Acelerador</th>'
		. '<th scope="col">O que a regra diz</th></tr></thead><tbody>';

	$acel = array(
		'manual'             => 'tem',
		'so_pedal_assistido' => 'só pedalando',
		'nao_declarado'      => 'não declara',
	);

	foreach ( (array) $t['linhas'] as $l ) {
		$html .= '<tr><th scope="row">' . esc_html( $l['rotulo'] ) . '</th>';
		$html .= '<td class="rdm-num">' . ( null === $l['watt_nominal'] ? '—'
			: esc_html( $l['watt_nominal'] ) ) . '</td>';
		$html .= '<td class="rdm-num">' . ( null === $l['watt_sem_rotulo'] ? '—'
			: esc_html( $l['watt_sem_rotulo'] ) ) . '</td>';
		$html .= '<td class="rdm-num">' . ( null === $l['velocidade_kmh'] ? '—'
			: esc_html( $l['velocidade_kmh'] ) ) . '</td>';
		$html .= '<td>' . esc_html( isset( $acel[ $l['acelerador'] ] ) ? $acel[ $l['acelerador'] ]
			: (string) $l['acelerador'] ) . '</td>';
		$html .= '<td>' . ( null === $l['categoria']
			? esc_html( rodametria_f1_causa_na_tela( $l['causa_da_recusa'] ) )
			: '<b>' . esc_html( $l['categoria_nome'] ) . '</b>' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';

	$html .= '<p>De <span class="rdm-num">' . (int) $t['total'] . '</span> anúncios colhidos, '
		. '<span class="rdm-num">' . (int) $t['com_nominal'] . '</span> declaram a potência '
		. 'nominal e <span class="rdm-num">' . (int) $t['classificaveis'] . '</span> dão para '
		. 'classificar. Esse é o tamanho real do problema, e é por isso que esta ferramenta '
		. 'pergunta os números a você em vez de prometer uma lista pronta.</p>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * AS DOBRAS (32.1, item 7) — o texto inteiro continua no HTML servido
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_dobras_html' ) ) {
function rodametria_f1_dobras_html( $d ) {
	$c = $d['constantes_usadas'];

	$lim = isset( $c['limiares-categoria-contran-996-2023'] )
		? $c['limiares-categoria-contran-996-2023'] : array();
	$hab = isset( $c['exigencia-de-habilitacao-por-categoria-ctb'] )
		? $c['exigencia-de-habilitacao-por-categoria-ctb'] : array();

	/* --- de onde saem os limites --- */
	$fonte  = '<p>Os quatro limites que decidem a categoria vieram de uma leitura só, e ela está '
		. 'nomeada: <b>' . esc_html( isset( $lim['fonte'] ) ? (string) $lim['fonte'] : '' )
		. '</b></p>';
	if ( ! empty( $lim['url'] ) ) {
		$fonte .= '<p><a href="' . esc_url( (string) $lim['url'] ) . '" rel="nofollow noopener">'
			. 'O arquivo oficial da resolução</a> — lido em '
			. esc_html( rodametria_f1_data( (string) $lim['verificado_em'] ) ) . '.</p>';
	}
	$fonte .= '<p>Antes dessa leitura a gente tinha três números diferentes para a mesma '
		. 'pergunta, colhidos em páginas que se apresentam como quem sabe — e <b>duas páginas do '
		. 'mesmo site</b> citavam esta mesma resolução com limites diferentes. A leitura oficial '
		. 'desfez a contradição e mostrou de que lado estava o erro: os dois números existem, '
		. 'para categorias diferentes. Um é o teto do autopropelido; o outro é o do ciclomotor. '
		. 'Enquanto a gente não tinha o texto, esta ferramenta ficou fora do ar — porque errar '
		. 'para o lado permissivo aqui manda alguém para a rua sem habilitação.</p>';

	/* --- a metade que a gente nao responde, e ela e uma dobra PROPRIA --- */
	$cnh  = '<p>' . esc_html( (string) $d['frases_molde']['habilitacao_pendente'] ) . '</p>';
	$cnh .= '<p>A resolução que decide a categoria responde <b>placa, registro, licenciamento e '
		. 'capacete</b>, e é isso que a caixa de resposta mostra, com o artigo ao lado. A '
		. 'habilitação está em outra lei, e a gente só vai publicar o que ela diz depois de ler '
		. 'nela.</p>';

	/* --- como a conta decide --- */
	$conta  = '<p>A decisão é uma árvore de três perguntas, nesta ordem, e a primeira é a que '
		. 'mais gente erra:</p>';
	$conta .= '<ol><li><b>Tem acelerador?</b> Acelerador manual tira o veículo da definição de '
		. 'bicicleta elétrica <i>mesmo</i> com a potência abaixo do limite. E o autopropelido, ao '
		. 'contrário, <i>pode</i> ter acelerador. É o campo que decide, não o que completa — sem '
		. 'ele nenhuma potência classifica.</li>';
	$conta .= '<li><b>A potência nominal e a velocidade de fábrica cabem no limite?</b> As duas '
		. 'juntas, nunca uma só.</li>';
	$conta .= '<li><b>Se não cabem, cabem no teto do ciclomotor?</b> Se também não, a resolução '
		. 'manda classificar como motocicleta, motoneta ou triciclo, conforme o caso — e não diz '
		. 'qual. A gente não escolhe por ela.</li></ol>';
	$conta .= '<p>Os números dos limites não estão escritos dentro do nosso programa: eles moram '
		. 'num único lugar, lido da resolução, e a árvore os chama pelo nome. Foi isso que fez a '
		. 'ferramenta poder ser construída inteira antes de a gente conseguir ler o texto '
		. 'oficial — quando ele chegou, destravou sem uma linha de lógica mudar.</p>';

	/* A DATA QUE ESTA PAGINA PUBLICA, EM PROSA, e ela nao e enfeite: o portao de
	   ar cruza o `dateModified` do JSON-LD com as datas que a prosa traz, e
	   reprovou esta pagina na primeira passada por servir `2026-11-06` na camada
	   que a maquina le e em lugar nenhum na camada que a pessoa le. Duas
	   declaracoes do mesmo fato comecam iguais e so uma sobe (20.7) — a saida
	   nao e tirar o JSON-LD, e a pagina DIZER a data. */
	$fonte .= '<p>Esta página foi gerada a partir do nosso banco em '
		. esc_html( rodametria_f1_data( (string) $d['gerado_em'] ) ) . '.</p>';

	$html  = rodametria_casca_dobra( 'De onde saíram os limites', $fonte );
	$html .= rodametria_casca_dobra( 'Por que esta página não responde sobre CNH', $cnh );
	$html .= rodametria_casca_dobra( 'Como a conta decide', $conta );

	return $html;
}
}

/**
 * A FRASE DO PICO, MONTADA DO MOLDE E DA CONTAGEM — um lugar so.
 *
 * Ela e pedida em DOIS lugares: a ressalva da pagina (que vem pre-renderizada do
 * cerebro) e a resposta do `FAQPage`. A versao do FAQ era prosa escrita a mao e
 * foi ao ar com o quantificador `costuma` e com `0 de 14 declaram` — os dois
 * defeitos que a camada visivel ja nao tinha. Esta funcao existe para a pergunta
 * do JSON-LD ler o MESMO molde que a tela le.
 *
 * Os dois moldes (zero nominal e algum nominal) sao escolhidos pela CONTAGEM,
 * como no cerebro e no JS: tres lugares, uma decisao, nenhuma frase digitada.
 * Sem titulo ou sem contagem a funcao devolve string vazia, e quem a chama fica
 * sem a frase — nunca com a frase pela metade.
 */
if ( ! function_exists( 'rodametria_f1_frase_do_pico' ) ) {
function rodametria_f1_frase_do_pico( $d ) {
	$c = isset( $d['contagem_de_fichas'] ) ? $d['contagem_de_fichas'] : null;
	$titulo = isset( $d['constantes_usadas']['watt-sem-rotulo-no-titulo-caso-medido']['valor'] )
		? (string) $d['constantes_usadas']['watt-sem-rotulo-no-titulo-caso-medido']['valor'] : '';

	if ( ! is_array( $c ) || '' === $titulo ) {
		return '';
	}

	$chave = ( (int) $c['com_nominal'] > 0 )
		? 'ressalva_pico_com_nominal' : 'ressalva_pico_nenhum_nominal';
	if ( empty( $d['frases_molde'][ $chave ] ) ) {
		return '';
	}

	$molde = (string) $d['frases_molde'][ $chave ];
	$vals  = array(
		'{titulo}'      => $titulo,
		'{colhidos}'    => number_format( (float) $c['colhidos'], 0, ',', '.' ),
		'{sem_rotulo}'  => number_format( (float) $c['sem_rotulo'], 0, ',', '.' ),
		'{com_nominal}' => number_format( (float) $c['com_nominal'], 0, ',', '.' ),
	);

	return strtr( $molde, $vals );
}
}

if ( ! function_exists( 'rodametria_f1_data' ) ) {
function rodametria_f1_data( $iso ) {
	if ( ! preg_match( '/^(\d{4})-(\d{2})-(\d{2})$/', (string) $iso, $m ) ) {
		return (string) $iso;
	}

	return $m[3] . '/' . $m[2] . '/' . $m[1];
}
}

/* ---------------------------------------------------------------------------
 * A FERRAMENTA INTEIRA, pendurada na PRIMEIRA TELA DA HOME
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rodametria_f1_html' ) ) {
function rodametria_f1_html() {
	$d = rodametria_f1_banco();
	if ( ! $d ) {
		/* Sem banco ou sem limiar a ferramenta NAO aparece, e a home volta a ser
		   HUB sozinha. Nunca molde cru, nunca numero inventado. */
		return '';
	}

	$html  = '<h2 class="rdm-f1-pergunta">Esse elétrico precisa de CNH?</h2>';
	$html .= rodametria_f1_formulario_html( $d );
	$html .= rodametria_f1_resultado_html( $d );

	$html .= rodametria_casca_bloco_de_compra(
		'À venda agora nesta categoria',
		array(),
		(string) $d['compra']['frase_de_abertura'],
		(string) $d['compra']['frase_de_abertura'] );

	$html .= rodametria_f1_ressalva_html( $d );

	$html .= '<h2>Quem entrou, quem não entrou, e por quê</h2>';
	$html .= rodametria_f1_contas_html( $d );

	$html .= '<h2>' . esc_html( $d['rotulos']['titulo_tabela_regra'] ) . '</h2>';
	$html .= rodametria_f1_tabela_regra_html( $d );

	$html .= '<h2>' . esc_html( $d['rotulos']['titulo_tabela_banco'] ) . '</h2>';
	$html .= rodametria_f1_tabela_banco_html( $d );

	$html .= '<h2>Como sabemos</h2>';
	$html .= rodametria_f1_dobras_html( $d );

	return $html;
}
}

/* A PRIMEIRA TELA DA HOME. Vazio = a casca imprime a home HUB de 29/10, byte
   por byte — e e isso que acontece se o banco nao chegar ou se o limiar voltar
   a `pendente`. */
add_filter( 'rodametria_home_ferramenta', function ( $html ) {
	$meu = rodametria_f1_html();

	return '' !== $meu ? $meu : $html;
} );

/* O CARTAO DA F1 SAI DA LISTA quando a F1 esta na primeira tela: cartao que
   aponta para a propria pagina em que esta e ruido, e o `VOZ.md` e literal —
   *"a ferramenta principal em cima; as OUTRAS ferramentas entram como
   cartoes"*. A remocao e por CHAVE e nao por posicao: lista que depende da
   ordem de hoje quebra calada no dia em que a F3 entrar. */
add_filter( 'rodametria_home_cartoes', function ( $cartoes ) {
	if ( ! rodametria_f1_banco() ) {
		return $cartoes;
	}
	unset( $cartoes['f1'] );

	return $cartoes;
} );

/* A DATA QUE A HOME PUBLICA passa a sair do banco da F1, porque e a F1 que
   ocupa a primeira tela dela. A prioridade 9 roda ANTES do filtro da casca, que
   a tira do banco da F2 e que devolve o que achar se `$data` ja estiver
   preenchido. Um fato, uma fonte (20.7). */
add_filter( 'rodametria_data_da_pagina', function ( $data, $slug ) {
	if ( 'inicio' !== $slug || '' !== $data ) {
		return $data;
	}
	$d = rodametria_f1_banco();

	return ( $d && ! empty( $d['gerado_em'] ) ) ? (string) $d['gerado_em'] : $data;
}, 9, 2 );

/* ---------------------------------------------------------------------------
 * JSON-LD — FAQPage com as perguntas que a ferramenta responde
 *
 * Ele NAO repete o WebSite nem o Organization, que sao da casca, e nao repete o
 * BreadcrumbList, que a home nao tem (16.3).
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! rodametria_f1_na_pagina() ) {
		return;
	}
	$d = rodametria_f1_banco();
	if ( ! $d ) {
		return;
	}

	$t = array();
	foreach ( (array) $d['tabela_regra'] as $l ) {
		$t[ $l['categoria'] ] = $l;
	}

	$bike = $t['bicicleta_eletrica'];
	$auto = $t['autopropelido'];
	$ciclo = $t['ciclomotor'];

	/* AS RESPOSTAS SAO MONTADAS DOS CAMPOS DA TABELA, nunca digitadas: e o mesmo
	   dado que a tabela visivel publica, entao a camada que a IA le e a camada
	   que a pessoa le nao podem divergir. */
	$perguntas = array(
		array(
			'Quando um veículo elétrico é bicicleta elétrica?',
			'Pela Resolução Contran nº 996/2023, quando o motor auxiliar tem até '
				. $bike['potencia_w'] . ' W de potência nominal, a velocidade do motor não passa de '
				. $bike['velocidade_kmh'] . ' km/h, o veículo só funciona quando a pessoa pedala e '
				. 'ele não tem acelerador. Nessa categoria, o ' . $bike['artigo'] . ' diz que o '
				. 'veículo ' . $bike['placa'] . '.',
		),
		array(
			'Quando é autopropelido, e o que muda em relação à bicicleta elétrica?',
			'O autopropelido tem os mesmos tetos de ' . $auto['potencia_w'] . ' W e '
				. $auto['velocidade_kmh'] . ' km/h, e a diferença é o acelerador: ele PODE ter, e a '
				. 'bicicleta elétrica não pode. A resolução também limita o tamanho dele — '
				. $auto['dimensao'] . '. Pelo ' . $auto['artigo'] . ', ele ' . $auto['placa'] . '.',
		),
		array(
			'Quando o elétrico passa a ser ciclomotor?',
			'Quando a potência nominal ou a velocidade de fábrica passam dos tetos do '
				. 'autopropelido e ainda cabem em ' . $ciclo['potencia_w'] . ' W e '
				. $ciclo['velocidade_kmh'] . ' km/h. Aí o ' . $ciclo['artigo'] . ' manda que ele '
				. 'seja ' . $ciclo['placa'] . '.',
		),
		array(
			'A potência de pico do anúncio serve para classificar?',
			/* A RESPOSTA SAI DO MOLDE, E ELA NAO ERA ASSIM. Esta era prosa escrita
			   A MAO aqui, e foi ao ar com DOIS defeitos que a propria pagina ja
			   tinha consertado na camada visivel, medidos no JSON-LD servido em
			   06/11/2026: o quantificador `costuma` (a classe que esta ilha paga
			   desde 03/11) e `0 de 14 declaram`, que e o plural que mente.
			   A CAUSA E ESTRUTURAL E VALE MAIS QUE AS DUAS FRASES: a varredura de
			   quantificador do portao de ar le o TEXTO VISIVEL, e
			   `corpo_da_pagina()` tira `<script>` antes de medir — com razao, porque
			   ali mora CSS e JSON. Entao o JSON-LD escapa dela. E ele e justamente
			   a camada que a visao geral de IA ingere: defeito ali vale MAIS do que
			   na prosa, nao menos. E a familia da 32.4-b (o comentario de CSS que
			   nenhum portao via) um andar acima.
			   O conserto nao e consertar a frase: e a frase deixar de existir aqui.
			   O molde ja e contado, ja escolhe o plural por mundo e ja passou pelas
			   guardas do gerador. */
			'Não. A regra lê a potência NOMINAL, que fica na ficha. '
				. rodametria_f1_frase_do_pico( $d ),
		),
		array(
			'Essa resolução diz se precisa de CNH?',
			(string) $d['frases_molde']['habilitacao_pendente'],
		),
	);

	$itens = array();
	foreach ( $perguntas as $p ) {
		$itens[] = array(
			'@type'          => 'Question',
			'name'           => $p[0],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
		);
	}

	$dados = array(
		'@context'   => 'https://schema.org',
		'@type'      => 'FAQPage',
		'mainEntity' => $itens,
	);

	echo "\n" . '<script type="application/ld+json" id="rodametria-f1-faq">'
		. wp_json_encode( $dados, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
		. '</script>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * O JS DO RODAPE — ele PREENCHE MOLDE e DECIDE a arvore; nunca escreve frase
 *
 * A arvore esta escrita DUAS VEZES de proposito, e isto e a secao 8 e nao
 * descuido: a decisao e o que se escreve duas vezes, porque e ali que a
 * divergencia ensina algo. O que NAO se escreve duas vezes e o FATO EXTERNO —
 * os limiares e os moldes viajam inteiros, de um lugar so, no pacote abaixo.
 *
 * E A DIVERGENCIA E MEDIDA, nao prometida: `ferramentas/teste-f1-arvore.mjs`
 * extrai a funcao `categoria()` deste arquivo, escreve uma TERCEIRA arvore em
 * JavaScript e compara as duas sobre a grade dos limiares ficticios — a mesma
 * grade que `ferramentas/teste-f1.py` usa contra `regras/f1.py`.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! rodametria_f1_na_pagina() ) {
		return;
	}
	$d = rodametria_f1_banco();
	if ( ! $d ) {
		return;
	}

	$pacote = array(
		'limiares'    => $d['limiares'],
		'moldes'      => $d['frases_molde'],
		'curtos'      => array(
			'bicicleta_eletrica'  => 'bicicleta elétrica',
			'autopropelido'       => 'autopropelido',
			'ciclomotor'          => 'ciclomotor',
			'acima_do_ciclomotor' => 'acima do ciclomotor',
		),
		'consequencias' => isset( $d['constantes_usadas']['consequencias-por-categoria-contran-996-2023']['valor'] )
			? $d['constantes_usadas']['consequencias-por-categoria-contran-996-2023']['valor']
			: array(),
		'habilitacao' => ! empty( $d['habilitacao_respondida'] ),
		'assistenciaPe' => isset( $d['constantes_usadas']['assistencia-a-pe-contran-996-2023']['valor'] )
			? $d['constantes_usadas']['assistencia-a-pe-contran-996-2023']['valor'] : null,
		'alteracao'   => isset( $d['constantes_usadas']['alteracao-pos-compra-caso-medido']['valor'] )
			? $d['constantes_usadas']['alteracao-pos-compra-caso-medido']['valor'] : null,
		'tituloPico'  => isset( $d['constantes_usadas']['watt-sem-rotulo-no-titulo-caso-medido']['valor'] )
			? $d['constantes_usadas']['watt-sem-rotulo-no-titulo-caso-medido']['valor'] : null,
		'contagem'    => isset( $d['contagem_de_fichas'] ) ? $d['contagem_de_fichas'] : null,
		'municipios'  => rodametria_f1_municipios_para_o_js(),
	);
	?>
<script id="rodametria-f1-js">
(function(){
  var D = <?php echo wp_json_encode( $pacote, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ); ?>;
  var form = document.querySelector('[data-rdm-f1-form]');
  var caixa = document.querySelector('[data-rdm-f1-caixa]');
  var blocoMun = document.querySelector('[data-rdm-f1-municipal]');
  var blocoRes = document.querySelector('[data-rdm-f1-ressalva]');
  if (!form || !caixa) { return; }

  function num(x){
    var s = String(Math.round(x));
    return s.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }
  function preencher(molde, vals){
    return molde.replace(/\{(\w+)\}/g, function(_, k){
      return (k in vals) ? vals[k] : '{' + k + '}';
    });
  }
  function lim(nome){ return parseFloat(D.limiares[nome]); }

  /* A ARVORE, ESCRITA AQUI PELA SEGUNDA VEZ (secao 8). Ela nao le numero
     nenhum escrito neste arquivo: `lim()` vai ao pacote, que vem da constante. */
  function categoria(w, kmh, acel){
    if (!(w > 0) || !(kmh > 0)) { return null; }
    if (acel !== 'manual' && acel !== 'so_pedal_assistido') { return null; }
    if (acel === 'so_pedal_assistido'
        && w <= lim('LIMIAR_BIKE_W') && kmh <= lim('LIMIAR_BIKE_KMH')) {
      return 'bicicleta_eletrica';
    }
    if (w <= lim('LIMIAR_AUTOPROP_W') && kmh <= lim('LIMIAR_AUTOPROP_KMH')) {
      return 'autopropelido';
    }
    if (w <= lim('LIMIAR_CICLOMOTOR_W') && kmh <= lim('LIMIAR_CICLOMOTOR_KMH')) {
      return 'ciclomotor';
    }
    return 'acima_do_ciclomotor';
  }

  /* QUAL MOLDE DO VEREDITO, pela CAUSA do estouro — e nunca os dois ao mesmo
     tempo. O defeito que isto evita foi medido no cerebro em 06/11/2026: a
     frase dizia "1.000 W passa dos 1.000 W" ao lado da metade verdadeira. */
  function moldeDoEstouro(eW, eKmh, soW, soKmh, osDois){
    if (eW && eKmh) { return osDois; }
    return eW ? soW : soKmh;
  }

  var elW = form.querySelector('[data-rdm-f1-w]');
  var elKmh = form.querySelector('[data-rdm-f1-kmh]');
  var elMun = form.querySelector('[data-rdm-f1-mun]');

  /* A RESSALVA DO PICO, com a contagem CONTADA do banco e dois moldes por
     mundo. O molde do zero existe porque o mundo de hoje e o do zero, e "e 0
     declaram o nominal" e o plural que mente — a cicatriz que a clubedomosaico
     pagou em 12/10/2026. Sem titulo ou sem contagem a ressalva NAO SAI. */
  function ressalvaPico(){
    var c = D.contagem;
    if (!D.tituloPico || !c) { return ''; }
    var chave = c.com_nominal > 0 ? 'ressalva_pico_com_nominal' : 'ressalva_pico_nenhum_nominal';
    return preencher(D.moldes[chave], {
      titulo: D.tituloPico, colhidos: num(c.colhidos),
      sem_rotulo: num(c.sem_rotulo), com_nominal: num(c.com_nominal)
    });
  }

  function acelEscolhido(){
    var rs = form.querySelectorAll('[data-rdm-f1-acel]');
    for (var i = 0; i < rs.length; i++) { if (rs[i].checked) { return rs[i].value; } }
    return null;
  }

  function camadaMunicipal(nome){
    nome = (nome || '').trim();
    if (!nome) { return D.moldes.municipal_generica; }
    var alvo = nome.toLowerCase();
    for (var i = 0; i < D.municipios.length; i++) {
      var m = D.municipios[i];
      if (m.nome.toLowerCase() === alvo || m.id.toLowerCase() === alvo) {
        if (m.ato_lido && m.limite_kmh !== null) {
          return preencher(D.moldes.municipal_conhecido,
            {municipio: m.nome, limite_kmh: num(m.limite_kmh)});
        }
        return preencher(D.moldes.municipal_conhecido_pendente, {municipio: m.nome});
      }
    }
    return preencher(D.moldes.municipal_desconhecido, {municipio: nome});
  }

  function responder(){
    var w = parseFloat(elW.value);
    var kmh = parseFloat(elKmh.value);
    var acel = acelEscolhido();
    var cat = categoria(w, kmh, acel);

    var frases = [];
    var ressalvas = [];
    var tom = 'neutro';
    var numeroCaixa = 'sem resposta';

    if (cat === null) {
      frases.push(acel === null ? D.moldes.recusa_acelerador : D.moldes.recusa_nao_positivo);
      if (ressalvaPico()) { ressalvas.push(ressalvaPico()); }
    } else {
      numeroCaixa = D.curtos[cat];
      tom = (cat === 'ciclomotor' || cat === 'acima_do_ciclomotor') ? 'alerta' : 'verde';

      if (cat === 'bicicleta_eletrica') {
        frases.push(preencher(D.moldes.veredito_bicicleta_eletrica, {
          w: num(w), kmh: num(kmh),
          lim_w: num(lim('LIMIAR_BIKE_W')), lim_kmh: num(lim('LIMIAR_BIKE_KMH'))
        }));
      } else if (cat === 'autopropelido') {
        frases.push(preencher(D.moldes.veredito_autopropelido, {
          w: num(w), kmh: num(kmh),
          lim_w: num(lim('LIMIAR_AUTOPROP_W')), lim_kmh: num(lim('LIMIAR_AUTOPROP_KMH'))
        }));
        /* O DIVISOR E DEZ. Ele foi 100 por meia hora em 06/11/2026, nos TRES
           lugares que convertem mm para cm, e a pagina foi ao ar dizendo "7 cm
           de largura" onde a resolucao diz 70. O portao da ferramenta cobra a
           conta agora, com a regua escrita do outro lado (cm x 10 == mm). */
        ressalvas.push(preencher(D.moldes.ressalva_dimensao_autopropelido, {
          largura_cm: num(lim('LIMIAR_AUTOPROP_LARGURA_MM') / 10),
          eixos_cm: num(lim('LIMIAR_AUTOPROP_ENTRE_EIXOS_MM') / 10)
        }));
      } else if (cat === 'ciclomotor') {
        frases.push(preencher(D.moldes[moldeDoEstouro(
          w > lim('LIMIAR_AUTOPROP_W'), kmh > lim('LIMIAR_AUTOPROP_KMH'),
          'veredito_ciclomotor_por_potencia', 'veredito_ciclomotor_por_velocidade',
          'veredito_ciclomotor_por_dois')], {
          w: num(w), kmh: num(kmh),
          lim_autoprop_w: num(lim('LIMIAR_AUTOPROP_W')),
          lim_autoprop_kmh: num(lim('LIMIAR_AUTOPROP_KMH')),
          lim_w: num(lim('LIMIAR_CICLOMOTOR_W')), lim_kmh: num(lim('LIMIAR_CICLOMOTOR_KMH'))
        }));
      } else {
        frases.push(preencher(D.moldes[moldeDoEstouro(
          w > lim('LIMIAR_CICLOMOTOR_W'), kmh > lim('LIMIAR_CICLOMOTOR_KMH'),
          'veredito_acima_por_potencia', 'veredito_acima_por_velocidade',
          'veredito_acima_por_dois')], {
          w: num(w), kmh: num(kmh),
          lim_w: num(lim('LIMIAR_CICLOMOTOR_W')), lim_kmh: num(lim('LIMIAR_CICLOMOTOR_KMH'))
        }));
      }

      var c = D.consequencias[cat];
      if (c) {
        var exig = c.registro_licenciamento_emplacamento;
        var chave = exig === 'nao_sujeito' ? 'placa_nao_sujeito'
          : (exig === 'exigido' ? 'placa_exigido' : 'placa_nao_decidido');
        frases.push(preencher(D.moldes[chave], {artigo: c.artigo}));
      }
      if (!D.habilitacao) { frases.push(D.moldes.habilitacao_pendente); }

      if (ressalvaPico()) { ressalvas.push(ressalvaPico()); }
      if (acel === 'manual' && D.assistenciaPe !== null
          && w <= lim('LIMIAR_BIKE_W') && kmh <= lim('LIMIAR_BIKE_KMH')) {
        ressalvas.push(preencher(D.moldes.ressalva_assistencia_a_pe,
          {kmh_pe: num(D.assistenciaPe)}));
      }
      if (D.alteracao) {
        ressalvas.push(preencher(D.moldes.ressalva_alteracao, {
          kmh_flagrado: num(D.alteracao.kmh_flagrado),
          kmh_fabrica: num(D.alteracao.kmh_fabrica)
        }));
      }
    }

    /* A CAIXA: so os nos de texto trocam, e o tom troca de classe. O markup e o
       que a casca imprimiu — o JS nao remonta componente de molde. */
    caixa.className = 'rdm-molde-caixa rdm-molde-caixa-' + tom;
    var elNum = caixa.querySelector('.rdm-molde-caixa-numero .rdm-num');
    if (elNum) { elNum.textContent = numeroCaixa; }
    var antigas = caixa.querySelectorAll('.rdm-molde-caixa-frase');
    for (var j = 0; j < antigas.length; j++) { antigas[j].remove(); }
    for (var k = 0; k < frases.length; k++) {
      var p = document.createElement('p');
      p.className = 'rdm-molde-caixa-frase';
      p.textContent = frases[k];
      caixa.appendChild(p);
    }
    var barra = document.querySelector('[data-rdm-barra-numero]');
    if (barra) { barra.textContent = numeroCaixa; }

    if (blocoMun) {
      var ps = blocoMun.querySelectorAll('p');
      for (var m2 = 0; m2 < ps.length; m2++) { ps[m2].remove(); }
      var pm = document.createElement('p');
      pm.textContent = camadaMunicipal(elMun ? elMun.value : '');
      blocoMun.appendChild(pm);
    }

    if (blocoRes) {
      var pr = blocoRes.querySelectorAll('p');
      for (var n2 = 0; n2 < pr.length; n2++) { pr[n2].remove(); }
      for (var q = 0; q < ressalvas.length; q++) {
        var pp = document.createElement('p');
        pp.textContent = ressalvas[q];
        blocoRes.appendChild(pp);
      }
    }
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); responder(); });
  form.addEventListener('change', responder);
  if (elMun) { elMun.addEventListener('input', responder); }
})();
</script>
<?php
}, 20 );

/* Os municipios que o JS precisa, com o STATUS e nunca so o numero: municipio
   com ato NAO LIDO tem frase propria, e mandar o numero dele faria o navegador
   publicar um limite que a pagina se recusa a publicar. */
if ( ! function_exists( 'rodametria_f1_municipios_para_o_js' ) ) {
function rodametria_f1_municipios_para_o_js() {
	$banco = rodametria_casca_banco( 'municipios' );
	$saida = array();
	if ( ! is_array( $banco ) || empty( $banco['registros'] ) ) {
		return $saida;
	}
	foreach ( (array) $banco['registros'] as $m ) {
		$saida[] = array(
			'id'          => isset( $m['id'] ) ? (string) $m['id'] : '',
			'nome'        => isset( $m['nome'] ) ? (string) $m['nome'] : '',
			/* A CHAVE NAO SE CHAMA `publicavel`, E ISSO FOI MEDIDO NO AR: a 32.4
			   lista essa palavra entre as de bastidor, e o portao de ar a achou
			   CINCO vezes no HTML servido da home em 06/11/2026 — dentro deste
			   pacote JSON. Invisivel para o visitante e perfeitamente legivel
			   para quem le o fonte, que e o que a visao geral de IA ingere.
			   `ato_lido` diz o que o campo significa, e em portugues. */
			'ato_lido'    => ( isset( $m['status'] ) && 'publicavel' === $m['status'] ),
			'limite_kmh'  => isset( $m['limite_velocidade_kmh'] ) ? $m['limite_velocidade_kmh'] : null,
		);
	}

	return $saida;
}
}

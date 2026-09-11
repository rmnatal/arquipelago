/**
 * Robometria A1 — Existe filtro universal de robô aspirador?
 * Versão: 1.1.0 (11/09/2026) — o título deixou de afirmar a tese. A tese tem duas
 * formas escolhidas pela contagem do banco; o título tinha uma só, digitada, e ia
 * junto para o headline do JSON-LD. Virou pergunta, que sobrevive às duas. O par
 * com a ferramenta passou a ser por slug, e o post_title é reespelhado.
 * Versão: 1.0.0 (10/09/2026) — Bloco 5 da fila: o artigo-âncora da R1.
 *
 * A R1 nasceu sem ele porque o Bloco 4 já era grande, e sem ele a ferramenta
 * ficava com uma listagem só e nenhuma irmã — a regra da malha da seção 9 do
 * ARQUIPELAGO.md pede pelo menos duas listagens e três irmãs por página. Este
 * artigo é a segunda listagem da R1 e a mão dupla dela.
 *
 * ---------------------------------------------------------------------------
 * POR QUE ESTE ASSUNTO, e não um "guia de compra"
 * ---------------------------------------------------------------------------
 *
 * O corpus de buscas desta ilha (dados/corpus-buscas.md, cluster A1) registrou
 * uma consulta com sinal invertido: "filtro hepa universal robô aspirador".
 * Quem digita isso está prestes a comprar a peça errada, e a única página do
 * nicho que hoje avisa contra isso é um blog que avisa sem dado — "os encaixes
 * são diferentes", sem contar nada. A Robometria tem o catálogo dos fabricantes
 * transcrito; então aqui a mesma frase vira medição, e é essa a diferença entre
 * este artigo e um texto de fazenda de conteúdo.
 *
 * ---------------------------------------------------------------------------
 * AS QUATRO DECISÕES, herdadas da R1 e uma nova
 * ---------------------------------------------------------------------------
 *
 * 1. O NÚMERO DA TESE NÃO É DIGITADO AQUI. Ele vem de dados/a1-fatos.json, que
 *    ferramentas/gerar-a1.py deriva do mesmo banco que alimenta a R1. Um artigo
 *    cuja tese é um número não pode ter esse número dentro do HTML: no dia em
 *    que o banco crescer e uma peça atravessar marca, o texto passaria a mentir
 *    em silêncio. Assim, ou o número muda junto, ou ferramentas/teste-a1.php
 *    reprova a página antes de ela ir ao ar.
 * 2. A RESPOSTA VEM ANTES DA EXPLICAÇÃO, e inteira no HTML servido. Não há
 *    JavaScript nenhum nesta página: a primeira frase responde a pergunta do
 *    título com o número e sobrevive a ser citada fora de contexto (seção 5).
 * 3. A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA (seção 7, item 0 do
 *    despacho de 10/09). Um artigo que termina em "confira no fabricante" é a
 *    mesma armadilha que a R1 1.0.0 caiu: a página fica impecável e a única
 *    porta clicável leva para a loja da marca. Aqui a vitrine vem antes, e a
 *    procedência é link de texto "fonte", com nofollow, nunca um botão.
 * 4. O ARTIGO NÃO REPETE A FERRAMENTA. Ele não tem formulário e não responde
 *    "qual peça serve no MEU modelo" — essa pergunta é da R1, e o artigo manda
 *    para lá. Duas páginas respondendo a mesma coisa competem entre si no
 *    índice, que é o defeito que a seção 14.4 chama de listagem que não é
 *    página de verdade.
 *
 * Regras herdadas: sem "<?php" no topo (o Code Snippets põe); nenhuma
 * superglobal de servidor; nenhum <script> nem <style> dentro do retorno do
 * shortcode; toda função de nível superior dentro de if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'ROBOMETRIA_A1_VERSAO' ) ) {
	define( 'ROBOMETRIA_A1_VERSAO', '1.1.0' );
	define( 'ROBOMETRIA_A1_SLUG', 'filtro-universal-de-robo-aspirador' );
	/* O TÍTULO DEIXOU DE AFIRMAR A TESE, e este é o terceiro lugar da mesma
	   família. A tese deste artigo é uma contagem do banco, e por isso a frase de
	   abertura, a description do JSON-LD e a resposta do FAQPage têm DUAS formas,
	   escolhidas pela contagem do dia. O título não tinha: ele afirmava a forma
	   de hoje ("Por que não existe"), digitada, e no dia em que uma peça do banco
	   atravessar marca ele seria a única metade da página a continuar dizendo o
	   que deixou de valer — e ainda por cima dentro do headline do JSON-LD, que é
	   o canal que a seção 5 do contrato diz valer tanto quanto ranquear.
	   A pergunta sobrevive às duas formas, e é também o que a pessoa digita. */
	define( 'ROBOMETRIA_A1_TITULO', 'Existe filtro universal de robô aspirador?' );
	define( 'ROBOMETRIA_A1_DADOS', 'robometria_dados_a1-fatos' );
}

/* ---------------------------------------------------------------------------
 * 1. Os fatos: o que o Sync trouxe do repositório
 *
 * Mesmo caminho da R1: dados/a1-fatos.json entra no manifest com publicar=true e
 * o Sync o grava numa option. Sem a option, a página NÃO finge — ela diz que os
 * números não chegaram, porque um artigo de tese medida sem a medição é só
 * opinião com cara de dado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a1_fatos' ) ) {
function robometria_a1_fatos() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}

	$d = get_option( ROBOMETRIA_A1_DADOS );
	$d = apply_filters( 'robometria_a1_fatos', $d );

	if ( ! is_array( $d ) || empty( $d['resumo'] ) || empty( $d['alcance'] ) ) {
		$cache = array();
		return $cache;
	}

	$cache = $d;
	return $cache;
}
}

/* ---------------------------------------------------------------------------
 * 2. As peças de texto
 *
 * O banco é ASCII e o texto de tela sai acentuado (fase 4b do playbook). Estas
 * tabelas são o par acentuado das do gerador, e ferramentas/teste-a1.php compara
 * as duas ignorando acento — se uma ganhar um tipo que a outra não tem, ele
 * reprova em vez de a página publicar um rótulo vazio.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a1_nome_do_tipo' ) ) {
function robometria_a1_nome_do_tipo( $tipo ) {
	$nomes = array(
		'filtro'           => 'filtro',
		'escova lateral'   => 'escova lateral',
		'escova principal' => 'escova principal',
		'mop'              => 'mop',
		'bateria'          => 'bateria',
		'reservatorio'     => 'reservatório',
		'kit'              => 'kit',
	);
	return isset( $nomes[ $tipo ] ) ? $nomes[ $tipo ] : $tipo;
}
}

/** Plural do tipo, para o cabeçalho de uma linha de tabela. */
if ( ! function_exists( 'robometria_a1_plural_do_tipo' ) ) {
function robometria_a1_plural_do_tipo( $tipo ) {
	$plurais = array(
		'filtro'           => 'filtros',
		'escova lateral'   => 'escovas laterais',
		'escova principal' => 'escovas principais',
		'mop'              => 'mops',
		'bateria'          => 'baterias',
		'reservatorio'     => 'reservatórios',
	);
	return isset( $plurais[ $tipo ] ) ? $plurais[ $tipo ] : robometria_a1_nome_do_tipo( $tipo );
}
}

/** Lista em português: a, b e c. */
if ( ! function_exists( 'robometria_a1_lista' ) ) {
function robometria_a1_lista( $itens ) {
	$itens = array_values( array_filter( (array) $itens, 'strlen' ) );
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

/** Número na tela, sempre em monoespaçada com tabular-nums (identidade da ilha). */
if ( ! function_exists( 'robometria_a1_num' ) ) {
function robometria_a1_num( $valor ) {
	return '<span class="rbm-num">' . esc_html( number_format_i18n( (float) $valor ) ) . '</span>';
}
}

if ( ! function_exists( 'robometria_a1_data' ) ) {
function robometria_a1_data( $iso ) {
	if ( function_exists( 'robometria_casca_data_br' ) ) {
		return robometria_casca_data_br( $iso );
	}
	$partes = explode( '-', (string) $iso );
	return 3 === count( $partes ) ? $partes[2] . '/' . $partes[1] . '/' . $partes[0] : (string) $iso;
}
}

/**
 * Como a peça é chamada na tela.
 *
 * Nem todo fabricante publica código: a Electrolux identifica várias peças só
 * pelo título. Nesse caso o título entra como transcrição, entre aspas, e a
 * página diz que o fabricante não publica código — que é a mesma regra da R1 e
 * do banco. Inventar um código para preencher a coluna seria dado inventado.
 */
if ( ! function_exists( 'robometria_a1_identificacao' ) ) {
function robometria_a1_identificacao( $linha, $com_titulo = false ) {
	if ( empty( $linha['sem_codigo_publicado'] ) ) {
		return esc_html( $linha['identificacao'] );
	}

	/* Sem codigo, o rotulo sozinho nao identifica nada — e numa tabela com duas
	   pecas do mesmo fabricante e do mesmo tipo, duas linhas identicas sao um
	   defeito de leitura, nao um detalhe. Entao a celula carrega o TITULO da
	   fonte, que e transcricao e vai entre aspas, com o aviso embaixo. */
	if ( $com_titulo && ! empty( $linha['nome_na_fonte'] ) ) {
		return '<span class="rbm-titulo-fonte">' . esc_html( '"' . $linha['nome_na_fonte'] . '"' ) . '</span>'
			. '<span class="rbm-sem-codigo">sem código publicado</span>';
	}

	return '<span class="rbm-sem-codigo">sem código publicado</span>';
}
}

/* ---------------------------------------------------------------------------
 * 3. Os blocos da página
 * ------------------------------------------------------------------------- */

/**
 * A tabela do alcance: quantos códigos de modelo cada peça declara.
 *
 * É a prova direta da tese, e ela é uma TABELA e não um parágrafo de propósito:
 * quem chegou perguntando por peça universal quer conferir a própria marca, e
 * conferir é ler uma linha, não uma frase. As linhas são as peças de maior
 * alcance — se a maior lista do banco é curta, todas as outras são mais curtas
 * ainda, e é isso que a tabela mostra sem precisar listar as dezesseis.
 */
if ( ! function_exists( 'robometria_a1_tabela_alcance' ) ) {
function robometria_a1_tabela_alcance( $f, $quantas = 6 ) {
	/* O envoltorio com overflow proprio e da casca, e nao e detalhe: sao cinco
	   colunas, e sem ele quem rola no celular e a PAGINA (secao 6). */
	$html  = '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>';
	$html .= '<th scope="col">Peça</th><th scope="col">Tipo</th><th scope="col">Fabricante</th>';
	$html .= '<th scope="col">Modelos que o fabricante declara</th>';
	$html .= '<th scope="col">Marcas atendidas</th>';
	$html .= '</tr></thead><tbody>';

	foreach ( array_slice( (array) $f['alcance'], 0, $quantas ) as $l ) {
		$html .= '<tr>';
		$html .= '<td class="rbm-peca">' . robometria_a1_identificacao( $l, true ) . '</td>';
		$html .= '<td>' . esc_html( robometria_a1_nome_do_tipo( $l['tipo'] ) ) . '</td>';
		$html .= '<td>' . esc_html( $l['publicador'] ) . '</td>';
		$html .= '<td>' . robometria_a1_num( $l['codigos_declarados'] ) . ' — '
			. esc_html( implode( ', ', (array) $l['codigos_na_fonte'] ) ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( number_format_i18n( count( (array) $l['marcas_atendidas'] ) ) ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	return $html;
}
}

/**
 * A tabela da dispersão dentro da marca — o achado menos óbvio do artigo.
 *
 * Se compatibilidade se herdasse do modelo para a classe de peça, as peças de
 * uma marca repetiriam o mesmo conjunto de modelos e a coluna da direita seria
 * quase sempre 1. Quando ela é igual à da esquerda, nenhuma peça daquela marca
 * repete a lista de outra — e é exatamente aí que mora o erro de quem compra
 * por semelhança dentro da própria marca.
 */
if ( ! function_exists( 'robometria_a1_tabela_dispersao' ) ) {
function robometria_a1_tabela_dispersao( $f ) {
	$html  = '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>';
	$html .= '<th scope="col">Fabricante</th>';
	$html .= '<th scope="col">Peças no banco</th>';
	$html .= '<th scope="col">Conjuntos de modelos diferentes</th>';
	$html .= '</tr></thead><tbody>';

	foreach ( (array) $f['dispersao'] as $d ) {
		$html .= '<tr>';
		$html .= '<td>' . esc_html( $d['publicador'] ) . '</td>';
		$html .= '<td>' . robometria_a1_num( $d['pecas'] ) . '</td>';
		$html .= '<td>' . robometria_a1_num( $d['conjuntos_distintos'] )
			. ( ! empty( $d['nenhuma_repete'] )
				? ' <span class="rbm-tag">nenhuma repete a lista de outra</span>'
				: '' )
			. '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	return $html;
}
}

/**
 * A vitrine: os itens de banco reais, com a porta de compra ANTES da fonte.
 *
 * A ORDEM É TÉCNICA e é a da própria tese: alcance declarado, do maior para o
 * menor. Ter ou não ter link de loja não reordena nada (seção 7 do contrato) —
 * hoje, aliás, nenhum destes itens tem link, e o número de peças esperando link
 * sai na tela porque é trabalho pendente de verdade, não estatística interna.
 */
if ( ! function_exists( 'robometria_a1_vitrine' ) ) {
function robometria_a1_vitrine( $f ) {
	$itens = isset( $f['vitrine'] ) ? (array) $f['vitrine'] : array();
	if ( ! $itens ) {
		return '';
	}

	$sem_link = 0;
	foreach ( $itens as $i ) {
		if ( empty( $i['afiliado']['url'] ) ) {
			$sem_link++;
		}
	}
	$total = count( $itens );

	$html  = '<div class="rbm-secao rbm-compra"><h2>As peças de maior alcance declarado</h2>';
	$html .= '<p>Nenhuma delas serve em tudo — e é essa a questão. Cada cartão diz quantos códigos de modelo o fabricante nomeou, porque é essa lista, e não a palavra "compatível" do anúncio, que decide se a peça encaixa.</p>';

	/* AVISO DE COMISSÃO VISÍVEL NO BLOCO DE COMPRA (seção 7), não só no rodapé.
	   Quem vê o botão precisa ver o aviso sem rolar. */
	$html .= '<p class="rbm-aviso-comissao">Os botões de compra abaixo são links de afiliado: se você comprar por eles, a Robometria pode receber comissão, sem custo a mais para você. Isso não muda a ordem da lista — ela é decidida pelo número de modelos que o fabricante declarou, e só por ele. '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Como isto funciona' )
			: 'Veja a página de divulgação de afiliados' ) . '.</p>';

	if ( $sem_link > 0 ) {
		if ( $sem_link === $total ) {
			$quantas = 1 === $total
				? 'Esta peça ainda não tem link de loja'
				: sprintf( 'Nenhuma destas %d peças tem link de loja ainda', $total );
		} elseif ( 1 === $sem_link ) {
			$quantas = sprintf( 'Uma destas %d peças ainda não tem link de loja', $total );
		} else {
			$quantas = sprintf( '%d destas %d peças ainda não têm link de loja', $sem_link, $total );
		}
		$html .= '<p class="rbm-nota">' . esc_html( $quantas )
			. esc_html( ', e o cartão diz isso em vez de fazer o bloco sumir. Enquanto o link não existe, o endereço da declaração do fabricante continua aqui — embaixo de cada cartão, como "fonte", para você conferir.' )
			. '</p>';
	}

	$html .= '<ul class="rbm-vitrine">';

	foreach ( $itens as $i ) {
		$html .= '<li class="rbm-vitrine-item">';

		/* Espaço reservado neutro: a peça não tem foto e a página não finge que
		   tem. Item sem imagem NÃO some da vitrine (seção 6). */
		$tem_imagem = ! empty( $i['imagem']['url'] );
		$html      .= '<span class="rbm-vitrine-foto" aria-hidden="true">'
			. ( $tem_imagem ? '' : '<span class="rbm-vitrine-vazia"></span>' )
			. '</span>';

		$html .= '<span class="rbm-vitrine-tipo">'
			. esc_html( robometria_a1_nome_do_tipo( $i['tipo'] ) ) . '</span>';
		$html .= '<span class="rbm-codigo-peca">' . robometria_a1_identificacao( $i ) . '</span>';
		$html .= '<span class="rbm-vitrine-nome">' . esc_html( $i['nome_na_fonte'] ) . '</span>';

		/* A ESPECIFICAÇÃO QUE FEZ O ITEM ENTRAR (seção 6). Aqui ela é o alcance
		   declarado, porque é sobre alcance que este artigo fala — e os códigos
		   saem inteiros para o leitor achar o dele sem abrir mais nada. */
		$html .= '<span class="rbm-vitrine-porque">' . esc_html( sprintf(
			'kit' === $i['tipo']
				? 'a %1$s declara este kit para %2$d código%3$s de modelo: %4$s'
				: 'a %1$s declara esta peça para %2$d código%3$s de modelo: %4$s',
			$i['publicador'],
			$i['codigos_declarados'],
			1 === (int) $i['codigos_declarados'] ? '' : 's',
			implode( ', ', (array) $i['codigos_na_fonte'] )
		) ) . '</span>';

		if ( ! empty( $i['tipos_do_kit'] ) ) {
			$nomes  = array_map( 'robometria_a1_nome_do_tipo', (array) $i['tipos_do_kit'] );
			$html  .= '<span class="rbm-vitrine-vida">o fabricante declara dentro deste kit: '
				. esc_html( robometria_a1_lista( $nomes ) ) . '</span>';
		}

		/* PRIMEIRO A PORTA DE COMPRA. A ordem destes dois <span> é a regra da
		   seção 7 escrita em código: inverter os dois é reabrir o defeito de
		   10/09/2026. */
		$html .= '<span class="rbm-vitrine-acao">'
			. ( function_exists( 'robometria_casca_porta_de_compra' )
				? robometria_casca_porta_de_compra( $i )
				: '<span class="rbm-sem-loja">Link de loja em breve</span>' )
			. '</span>';

		/* DEPOIS A PROCEDÊNCIA, discreta. */
		$html .= '<span class="rbm-vitrine-fonte">'
			. esc_html( 'Como sabemos — ' . $i['fonte_publicador'] . ', verificado em '
				. robometria_a1_data( $i['verificado_em'] ) )
			. ( empty( $i['fonte_url'] ) || ! function_exists( 'robometria_casca_fonte_link' )
				? ''
				: ' · ' . robometria_casca_fonte_link( $i['fonte_url'] ) )
			. '</span>';

		$html .= '</li>';
	}

	$html .= '</ul></div>';
	return $html;
}
}

/**
 * A tabela de cobertura por tipo — a confissão que a seção 5 pede.
 *
 * Publicar onde a ilha NÃO sabe responder é parte do método: um comparador que
 * nunca diz "não sei" está inventando em algum lugar. E aqui ela também é útil
 * ao leitor, porque diz de cara se o tipo de peça que ele procura é um dos que
 * o banco cobre bem.
 */
if ( ! function_exists( 'robometria_a1_tabela_cobertura' ) ) {
function robometria_a1_tabela_cobertura( $f ) {
	$total = (int) $f['resumo']['modelos_publicaveis'];

	$html  = '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>';
	$html .= '<th scope="col">Tipo de peça</th>';
	$html .= '<th scope="col">Modelos com declaração do fabricante</th>';
	$html .= '</tr></thead><tbody>';

	foreach ( (array) $f['cobertura_por_tipo'] as $c ) {
		$html .= '<tr>';
		$html .= '<td>' . esc_html( robometria_a1_plural_do_tipo( $c['tipo'] ) ) . '</td>';
		$html .= '<td>' . robometria_a1_num( $c['modelos_com_declaracao'] )
			. ' de ' . robometria_a1_num( $total ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 4. A página
 * ------------------------------------------------------------------------- */

add_shortcode( 'robometria_a1', function () {
	$f = robometria_a1_fatos();

	if ( empty( $f['resumo'] ) ) {
		return robometria_casca_sem_banco_html(
			'Este texto está sem a medição do banco no momento.',
			'A tese deste artigo é um número, e o número é publicado a partir do repositório da Robometria. Enquanto ele não chegar, preferimos avisar a servir o texto sem o dado que o sustenta.'
		);
	}

	$r     = $f['resumo'];
	$maior = $f['maior_alcance'];
	$html  = '<div class="rbm-bloco">';

	/* RESPOSTA ANTES DA EXPLICAÇÃO (seção 5.2): a primeira frase responde o
	   título com número e critério, e sobrevive a ser citada fora de contexto. */
	$atravessam = (int) $r['pecas_que_atravessam_marca'];

	$html .= '<div class="rbm-abertura">';

	/* A FRASE DE ABERTURA É DERIVADA, e não digitada, porque ela É a tese. No dia
	   em que uma peça do banco atravessar marca, esta página tem que dizer isso
	   na primeira linha em vez de repetir uma afirmação que deixou de valer — e
	   ferramentas/teste-a1.php confere que os dois lados continuam batendo. */
	if ( 0 === $atravessam ) {
		$html .= '<p class="rbm-linha-mestra">Não existe filtro universal que sirva no seu robô aspirador, e escova, mop e bateria também não: nas '
			. robometria_a1_num( $r['pecas_publicaveis'] )
			. ' peças de reposição com compatibilidade declarada pelo fabricante que a Robometria transcreveu, <strong>nenhuma é declarada para modelos de mais de uma marca</strong>, e a lista mais longa do banco nomeia apenas '
			. robometria_a1_num( $maior['codigos_declarados'] ) . ' códigos de modelo — todos do mesmo fabricante.</p>';
	} else {
		$html .= '<p class="rbm-linha-mestra">Peça universal que sirva no seu robô aspirador quase não existe: de '
			. robometria_a1_num( $r['pecas_publicaveis'] )
			. ' peças de reposição com compatibilidade declarada pelo fabricante que a Robometria transcreveu, apenas '
			. robometria_a1_num( $atravessam )
			. ' é declarada para modelos de mais de uma marca, e a lista mais longa do banco nomeia '
			. robometria_a1_num( $maior['codigos_declarados'] ) . ' códigos de modelo.</p>';
	}
	$html .= '<p>São ' . robometria_a1_num( $r['pares_declarados'] ) . ' pares peça × modelo, em '
		. robometria_a1_num( $r['marcas'] ) . ' marcas, colhidos do catálogo dos próprios fabricantes e verificados em '
		. esc_html( robometria_a1_data( $f['gerado_em'] ) )
		. '. Nenhum foi inferido: quando o fabricante não declara, o banco não completa por analogia.</p>';
	$html .= '<p>Isso não quer dizer que a peça anunciada como universal não caiba fisicamente em nada. Quer dizer que <strong>ninguém declarou que ela cabe no seu modelo</strong> — e num item que gira encostado no piso, o que decide não é caber, é o encaixe e a vedação que o fabricante especificou.</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>O maior alcance do banco tem ' . esc_html( $maior['codigos_declarados'] ) . ' modelos</h2>';
	$html .= '<p>A peça que mais longe chega, entre todas as que a Robometria transcreveu, é '
		. robometria_a1_identificacao( $maior ) . ', '
		. esc_html( robometria_a1_nome_do_tipo( $maior['tipo'] ) ) . ' da '
		. esc_html( $maior['publicador'] ) . ': o fabricante a declara para '
		. esc_html( implode( ', ', (array) $maior['codigos_na_fonte'] ) )
		. '. É o teto do que "universal" poderia significar neste nicho — e ele para dentro de uma marca só.</p>';
	$html .= robometria_a1_tabela_alcance( $f );
	/* Dois moldes, e o segundo existe para o dia em que o banco mudar: "0 peça
	   atravessa marca" não é português, e um artigo que descobre uma peça
	   multimarca precisa dizer isso, não emudecer. */
	$html .= '<p class="rbm-nota"><strong>A coluna da direita é a que responde o título.</strong> '
		. ( 0 === $atravessam
			? 'Ela vale 1 em todas as linhas, e em todas as ' . robometria_a1_num( $r['pecas_publicaveis'] )
				. ' peças do banco: nenhuma peça é declarada para modelos de mais de uma marca. Não é uma amostra escolhida a dedo — é o banco inteiro.'
			: esc_html( sprintf(
				1 === $atravessam
					? 'Uma das %d peças do banco é declarada para modelos de mais de uma marca, e ela está na tabela acima: é a exceção, e a página prefere mostrá-la a escondê-la.'
					: '%2$d das %1$d peças do banco são declaradas para modelos de mais de uma marca, e elas estão na tabela acima.',
				$r['pecas_publicaveis'], $atravessam ) ) )
		. '</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>E não se herda nem dentro da mesma marca</h2>';
	$html .= '<p>Esta é a parte que pega quem já sabe que peça de marca não serve em outra. Dentro do catálogo de um mesmo fabricante, cada peça tem a <em>sua</em> lista de modelos, e uma lista não vale para a peça seguinte.</p>';
	$html .= robometria_a1_tabela_dispersao( $f );
	$html .= '<p>Leia a tabela assim: quando os dois números são iguais, nenhuma peça daquele fabricante repete a lista de modelos de outra. O seu robô estar na lista do filtro não o coloca na lista da escova, e é por isso que a Robometria trata o par peça × modelo como a unidade — nunca a marca, nunca a linha.</p>';
	$html .= '</div>';

	/* A PORTA DE COMPRA VEM AQUI, ANTES DA PROVA DE PROCEDÊNCIA (seção 7). */
	$html .= robometria_a1_vitrine( $f );

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Como achar o código certo do seu modelo</h2>';
	$html .= '<p>O caminho é um só: procurar o <strong>seu</strong> modelo dentro da lista de compatibilidade que o fabricante publicou, e não procurar uma peça que diga servir no seu modelo. A diferença entre as duas coisas é quem está afirmando — no primeiro caso, o fabricante; no segundo, quem está vendendo.</p>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'qual-peca-serve-no-meu-robo-aspirador', 'A ferramenta de compatibilidade faz essa busca por você' )
		: 'A ferramenta de compatibilidade faz essa busca por você' )
		. ' — escolha marca e modelo e ela devolve o código da peça, o conjunto de modelos que o fabricante citou, o endereço da declaração e a data em que ela foi verificada. Quando não há declaração, ela responde "não localizamos" com essas palavras.</p>';
	$html .= '</div>';

	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Onde a Robometria ainda não sabe responder</h2>';
	$html .= '<p>Das ' . robometria_a1_num( $r['celulas_total'] ) . ' combinações de modelo e tipo de peça que o banco cobre, '
		. robometria_a1_num( $r['celulas_sem_resposta'] )
		. ' não têm nenhuma declaração de fabricante que a gente tenha localizado. Publicar esse número é parte do método — e por tipo de peça ele fica assim:</p>';
	$html .= robometria_a1_tabela_cobertura( $f );
	$html .= '<p>Um tipo com poucos modelos cobertos não quer dizer que a peça não exista: quer dizer que o fabricante não publicou a lista de compatibilidade dela em canal nenhum que a gente tenha alcançado. Nesses casos a resposta certa é "não sabemos", e ela é dada com essas palavras.</p>';
	$html .= '</div>';

	/* A MALHA (seção 9): três irmãs, e a mão dupla com a ferramenta que este
	   artigo apoia — a R1 aponta de volta para cá. */
	$html .= '<div class="rbm-secao">';
	$html .= '<h2>Continue por aqui</h2>';
	$html .= '<ul class="rbm-lista">';
	$html .= '<li>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'qual-peca-serve-no-meu-robo-aspirador', 'Qual peça serve no meu robô aspirador' )
		: 'Qual peça serve no meu robô aspirador' )
		. ' — a mesma pergunta, respondida para o seu modelo.</li>';
	$html .= '<li>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'metodologia', 'A metodologia, com a escada de fontes' )
		: 'A metodologia, com a escada de fontes' )
		. ' — o que vale como prova aqui, e o que não vale.</li>';
	$html .= '<li>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
		: 'Divulgação de afiliados' )
		. ' — como a Robometria se sustenta, e por que isso não muda a ordem das listas.</li>';
	$html .= '</ul>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Cabeça da página: JSON-LD e canônica
 *
 * Tudo no wp_head, NUNCA dentro do retorno do shortcode — o WordPress roda os
 * filtros do the_content sobre o retorno e transforma cada E-comercial em
 * entidade, o que mataria o JSON-LD inteiro.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_a1_na_pagina' ) ) {
function robometria_a1_na_pagina() {
	$forcado = apply_filters( 'robometria_a1_na_pagina', null );
	if ( null !== $forcado ) {
		return (bool) $forcado;
	}
	if ( ! function_exists( 'is_page' ) ) {
		return false;
	}
	return is_page( ROBOMETRIA_A1_SLUG );
}
}

if ( ! function_exists( 'robometria_a1_url_da_pagina' ) ) {
function robometria_a1_url_da_pagina() {
	if ( function_exists( 'robometria_casca_url_se_existir' ) ) {
		$url = robometria_casca_url_se_existir( ROBOMETRIA_A1_SLUG );
		if ( '' !== $url ) {
			return $url;
		}
	}
	return home_url( '/' . ROBOMETRIA_A1_SLUG . '/' );
}
}

add_action( 'wp_head', function () {
	if ( ! robometria_a1_na_pagina() ) {
		return;
	}

	$f = robometria_a1_fatos();
	if ( empty( $f['resumo'] ) ) {
		return;
	}

	$url = robometria_a1_url_da_pagina();

	$artigo = array(
		'@type'            => 'Article',
		'@id'              => $url . '#artigo',
		'headline'         => ROBOMETRIA_A1_TITULO,
		'url'              => $url,
		'inLanguage'       => 'pt-BR',
		'datePublished'    => '2026-09-10',
		'dateModified'     => isset( $f['gerado_em'] ) ? $f['gerado_em'] : '2026-09-10',
		/* A DESCRIÇÃO É DERIVADA, pelo mesmo motivo da frase de abertura — e
		   aqui o motivo é mais forte: é esta linha que um modelo de linguagem lê
		   como resposta (seção 5). Uma página que se corrige na tela e mantém a
		   afirmação antiga no JSON-LD se contradiz exatamente no canal que a
		   ilha existe para ocupar. */
		'description'      => 0 === (int) $f['resumo']['pecas_que_atravessam_marca']
			? sprintf(
				'Nas %d peças de reposição de robô aspirador com compatibilidade declarada pelo fabricante que a Robometria transcreveu, nenhuma é declarada para modelos de mais de uma marca, e a lista mais longa nomeia %d códigos de modelo. São %d pares peça × modelo em %d marcas.',
				$f['resumo']['pecas_publicaveis'],
				$f['maior_alcance']['codigos_declarados'],
				$f['resumo']['pares_declarados'],
				$f['resumo']['marcas']
			)
			: sprintf(
				'Das %d peças de reposição de robô aspirador com compatibilidade declarada pelo fabricante que a Robometria transcreveu, apenas %d é declarada para modelos de mais de uma marca, e a lista mais longa nomeia %d códigos de modelo. São %d pares peça × modelo em %d marcas.',
				$f['resumo']['pecas_publicaveis'],
				$f['resumo']['pecas_que_atravessam_marca'],
				$f['maior_alcance']['codigos_declarados'],
				$f['resumo']['pares_declarados'],
				$f['resumo']['marcas']
			),
		'publisher'        => array( '@id' => home_url( '/#organizacao' ) ),
		'author'           => array( '@id' => home_url( '/#organizacao' ) ),
		/* O artigo é sobre a ferramenta e aponta para ela também na marcação: as
		   duas páginas são um assunto só, e o link de mão dupla existe nos dois
		   lados do HTML e nos dois lados do grafo. */
		'mentions'         => array(
			'@type' => 'WebApplication',
			'name'  => 'Qual peça serve no meu robô aspirador',
			'url'   => home_url( '/qual-peca-serve-no-meu-robo-aspirador/' ),
		),
	);

	/* FAQPage montado dos FATOS, nunca escrito à mão: cada pergunta é uma
	   formulação real do corpus e cada resposta é o que a própria página serve. */
	$perguntas = array();
	foreach ( (array) $f['perguntas'] as $p ) {
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

	echo '<script type="application/ld+json" id="robometria-a1-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
	echo '<link rel="canonical" href="' . esc_url( $url ) . '">' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * 6. Estilo próprio do artigo
 *
 * A folha da porta de compra vem da casca, que é dona dela (seção 1c). Aqui fica
 * só o que é do texto: largura de leitura e a tabela que rola sozinha no celular
 * sem levar a página junto — as tabelas deste artigo têm cinco colunas, e a
 * seção 6 do contrato não admite rolagem horizontal na página.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! robometria_a1_na_pagina() ) {
		return;
	}

	$css = <<<'CSS'
.rbm-sem-codigo{display:block;font-family:var(--rbm-texto);font-style:italic;font-size:.82rem;color:var(--rbm-legenda);letter-spacing:0;}
.rbm-titulo-fonte{display:block;font-size:.88rem;line-height:1.4;}
/* A primeira coluna desta tabela e um titulo inteiro, entao ela e a unica que
   NAO pode herdar o white-space:nowrap que a casca da a toda primeira coluna. */
.rbm-quadro td.rbm-peca{white-space:normal;min-width:12rem;}
.rbm-compra{margin-top:2.4rem;padding-top:1.6rem;border-top:1px solid var(--rbm-traco);}
CSS;

	if ( function_exists( 'robometria_casca_css_vitrine' ) ) {
		$css = robometria_casca_css_vitrine() . "\n" . $css;
	}

	echo '<style id="robometria-a1">' . $css . '</style>' . "\n";
}, 21 );

/* ---------------------------------------------------------------------------
 * 7. A página, e o registro dela nas listagens
 *
 * O artigo se registra no catálogo da casca pelo filtro, do mesmo jeito que a
 * ferramenta faz — a casca nunca precisa saber quantos artigos a ilha tem. Com
 * isso ele aparece na home e no hub de ferramentas, que são as duas listagens
 * que a seção 9 do ARQUIPELAGO.md exige, e o auxiliar da casca só imprime <a>
 * quando a página existe mesmo publicada.
 * ------------------------------------------------------------------------- */

add_filter( 'robometria_artigos', function ( $lista ) {
	$lista[] = array(
		'codigo'     => 'A1',
		'titulo'     => ROBOMETRIA_A1_TITULO,
		'slug'       => ROBOMETRIA_A1_SLUG,
		/* O PAR É POR ENDEREÇO, NÃO POR NOME. Até 11/09/2026 este campo trazia o
		   título da ferramenta digitado, e o cartão o imprimia: uma quarta cópia
		   do nome de uma página, que o portão da árvore pegou no dia em que a R2
		   foi renomeada — o par simplesmente deixou de existir. Com o slug, o par
		   sobrevive a qualquer troca de nome, e quem escreve a frase do cartão lê
		   o nome da fonte única. */
		'ferramenta' => ROBOMETRIA_R1_SLUG,
		'resumo'     => 'Peça anunciada como universal não tem declaração de compatibilidade com o seu modelo. A contagem do catálogo dos fabricantes mostra o tamanho real do alcance de cada peça — e por que ele não atravessa marca nem se herda de uma peça para a seguinte.',
	);
	return $lista;
} );

if ( ! function_exists( 'robometria_a1_garantir_pagina' ) ) {
function robometria_a1_garantir_pagina() {
	$feita = get_option( 'robometria_a1_estrutura' );
	if ( ROBOMETRIA_A1_VERSAO === $feita ) {
		return;
	}

	$conteudo = '[robometria_a1]';
	$pagina   = get_page_by_path( ROBOMETRIA_A1_SLUG, OBJECT, 'page' );

	if ( ! $pagina ) {
		$pid = wp_insert_post( array(
			'post_type'      => 'page',
			'post_title'     => ROBOMETRIA_A1_TITULO,
			'post_name'      => ROBOMETRIA_A1_SLUG,
			'post_content'   => $conteudo,
			'post_status'    => 'publish',
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		), true );
		if ( is_wp_error( $pid ) ) {
			return;
		}
		update_post_meta( $pid, '_robometria_casca', '1' );
		update_post_meta( $pid, '_robometria_id', ROBOMETRIA_A1_SLUG );
		flush_rewrite_rules( false );
	} else {
		$pid = (int) $pagina->ID;
		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
		}
		/* Só repomos o shortcode em página que é nossa: página editada à mão pelo
		   Raphael não é reescrita por snippet. */
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& false === strpos( (string) $pagina->post_content, $conteudo ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $conteudo ) );
		}

		/* O TÍTULO TAMBÉM É NOSSO — e esta linha faltava nos quatro snippets de
		   página desta ilha. A casca aprendeu isso na 1.2.0 (o H1 da raiz ficou
		   "Início" depois de a casca já ter mudado três vezes); ferramenta e
		   artigo, não. A página nascia com o título da constante e ficava com
		   ele para sempre: renomear aqui mudaria o og:title, o cartão e a
		   trilha — que são derivados — e deixaria o H1 e o <title> do ar com o
		   nome antigo, que é a divergência que este bloco existe para desfazer,
		   agora em duas fontes que nenhuma bancada compara. O post_name NÃO é
		   tocado: a URL não muda com o nome (seção 12.1 do contrato). */
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& (string) $pagina->post_title !== (string) ROBOMETRIA_A1_TITULO ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => ROBOMETRIA_A1_TITULO ) );
		}
	}

	update_option( 'robometria_a1_estrutura', ROBOMETRIA_A1_VERSAO, false );
}
}

if ( ! function_exists( 'robometria_a1_boot' ) ) {
function robometria_a1_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;
	robometria_a1_garantir_pagina();
}
}

add_action( 'init', 'robometria_a1_boot', 22 );

if ( did_action( 'init' ) ) {
	robometria_a1_boot();
}

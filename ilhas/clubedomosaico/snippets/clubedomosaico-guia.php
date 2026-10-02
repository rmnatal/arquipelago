/**
 * CLUBE DO MOSAICO — O GUIA DE MATERIAIS, CATEGORIA POR CATEGORIA (bloco 4c)
 * Snippet "Clube do Mosaico Guia", registrado pelo Sync.
 *
 * A primeira categoria do Guia a nascer é a `acabamento`, em 02/10/2026, e ela
 * não foi escolhida: foi o `ferramentas/cruzamento-14-9.py` que a apontou. Ela é
 * o único recorte do Guia em que os DOIS portões da 14.9 abriram ao mesmo tempo
 * — o de DADO (3 itens reais e um número calculado, seção 9) na mãe e nas três
 * filhas, e o de SERP (quem ocupa o top 10) nas quatro consultas medidas. O
 * veredito por recorte está em `dados/cruzamento-14-9.md`, e quem publicar a
 * próxima categoria LÊ O VEREDITO em vez de cruzar os dois arquivos na cabeça.
 *
 * São quatro páginas numa leva só, e isso é a 16.6 ao pé da letra: "primeiro a
 * mãe e suas 3 primeiras filhas", nunca uma filha de cada categoria espalhada.
 * A mãe só pôde nascer porque tem as três filhas da 16.5 — e filha, aqui, é
 * filha no CRUZAMENTO, não no banco: a `pastilha` tem 13 itens, mais banco que
 * qualquer outra categoria desta ilha, e ZERO filhas que possam nascer, porque
 * a SERP dela é de marketplace.
 *
 * -------------------------------------------------------------------------
 * O NÚMERO QUE ESTAS PÁGINAS PUBLICAM, E POR QUE ELE É ESTE
 * -------------------------------------------------------------------------
 * A seção 9 exige um número calculado próprio por página, e o calculado destas
 * quatro é a COBERTURA DECLARADA: das 15 superfícies que o vocabulário desta
 * ilha nomeia (9 bases e 6 caquinhos), quantas a frase do próprio fabricante de
 * cada produto nomeia — e, portanto, quantas ele NÃO nomeia.
 *
 * Isso não é um número de enfeite escolhido para preencher o portão: é o que a
 * medição de SERP de 02/10/2026 escreveu, com estas palavras, como "o número
 * que a SERP não publica". Os dez resultados que ocupam a consulta de
 * impermeabilizante dizem "emulsão de silicone", "tinta betuminosa" e "silicone
 * ou verniz" — tipo de produto, sem marca e sem número. Nenhum deles diz sobre
 * O QUÊ o fabricante escreveu que o produto pode ir. A ausência medida é o
 * produto desta ilha, e é ela que a tabela publica.
 *
 * O SEGUNDO NÚMERO É O RELÓGIO, e ele é aritmética desta ilha sobre declaração
 * do fabricante, no mesmo desenho dos gramas de rejunte da F1: a espera total,
 * da primeira demão até a peça pronta, é `(demãos − 1) × intervalo entre demãos
 * + secagem final`. Ele sai em 2 dos 10 produtos e SÓ nesses dois — onde falta
 * uma das três parcelas, a página diz que o fabricante não declara, em vez de
 * emprestar o número do irmão de banco. Emprestar é exatamente o erro que o
 * `quartzolit-fundo-selador` tem escrito dentro do registro dele.
 *
 * -------------------------------------------------------------------------
 * A DECISÃO DE DESENHO QUE MANDA AQUI: ESTE ARQUIVO NÃO ESCOLHE PRODUTO
 * -------------------------------------------------------------------------
 * Nenhuma linha daqui recomenda um acabamento para uma base. E não é omissão —
 * é o esquema: `regras_da_categoria_acabamento` diz, desde 25/09/2026, que
 * acabamento NÃO entra na matriz base × ambiente, porque "acabamento não adere
 * duas coisas uma na outra e não se escolhe por ambiente declarado: o eixo dele
 * é SOBRE O QUE se passa e EM QUE MOMENTO". Todo registro de acabamento nasce
 * com as seis listas de `declaracoes` vazias, e isso é portão no
 * `validar-banco.py`, não prosa.
 *
 * Então estas páginas fazem o que o dado sustenta: LISTAM o que cada fabricante
 * escreveu, com a frase dele, e deixam a escolha com quem lê. Montar uma régua
 * de "qual verniz para qual peça" em cima de declarações que não falam de peça
 * de mosaico seria inventar a recomendação — a mesma família do número de tela
 * digitado.
 *
 * -------------------------------------------------------------------------
 * O QUE ESTAS PÁGINAS SE RECUSAM A RESPONDER, E DIZEM ISSO AO LEITOR
 * -------------------------------------------------------------------------
 * O VIDRO E O REJUNTE, nas quatro. Das 15 superfícies do vocabulário, as dez
 * declarações de fabricante deste banco nomeiam 4 — e nenhuma delas é vidro,
 * pastilha de vidro ou rejunte, que é exatamente o que uma peça de mosaico
 * expõe ao verniz. A pendência tem nome no banco
 * (`acabamento-nenhum-nomeia-vidro-nem-rejunte`, aberta em 25/09/2026) e a
 * recusa sai do banco CONTADA, nunca de uma frase lembrada: se um fabricante
 * novo nomear vidro, a recusa some sozinha.
 */

if ( ! defined( 'CDM_GUIA_VERSAO' ) ) {
	define( 'CDM_GUIA_VERSAO', '1.0.0' );
}

/* ---------------------------------------------------------------------------
 * 0. O REGISTRO DAS PÁGINAS PUBLICADAS
 *
 * O que mora aqui é o que NÃO é dado: o endereço, o nome na tela, a consulta
 * que a página mira e a prosa editorial. Produto, propriedade, frase do
 * fabricante, fonte e data vêm do banco (`dados/materiais-acabamento.json`),
 * e nenhum número é digitado neste arquivo.
 *
 * `tipo => null` é a MÃE (o recorte é a categoria inteira); `tipo => 'verniz'`
 * é a filha daquele tipo. É o mesmo recorte que `dados/filhas-do-guia.json` e
 * `dados/cruzamento-14-9.md` usam, e o `teste-guia.php` cobra que toda página
 * registrada aqui tenha veredito `pode_nascer` no cruzamento.
 *
 * O SLUG É A CONSULTA MEDIDA, sem acento e com hífen, e aqui a árvore sai
 * INTEIRA pela primeira vez nesta ilha: `/materiais/acabamento/<consulta>/`,
 * três segmentos, que é o que a 16.1 pede. A F2, a F1 e as duas técnicas vivem
 * em dois segmentos porque nasceram antes de a categoria delas existir — este
 * bloco é o primeiro em que a categoria nasce ANTES da filha, e por isso é o
 * primeiro que não precisa do estado de transição.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_guia_registro' ) ) {
function cdm_guia_registro() {
	return array(
		/* A MÃE. 42 caracteres; com o separador e a marca, o `<title>` fica em
		   61, abaixo do teto de 65. A palavra "Acabamento" abre o nome porque
		   ela é o degrau da trilha e o cartão no Guia — um nome por página, nas
		   cinco superfícies, que é a cicatriz que a Aquametria pagou em
		   11/09/2026. */
		'acabamento' => array(
			'tipo'     => null,
			'slug'     => 'materiais/acabamento',
			'titulo'   => 'Acabamento: o que passar depois do rejunte',
			'curto'    => 'Acabamento',
			'consulta' => 'acabamento para peça de mosaico: qual produto passar depois do rejunte',
			'resumo'   => 'Verniz, impermeabilizante e selador: o que cada um faz, em que momento ele entra e o que o fabricante escreveu que ele atende.',
			'linha_mestra' => 'Depois que a peça está rejuntada e seca, sobra uma pergunta: passa alguma coisa em cima? Aqui estão os três produtos que entram nessa etapa, o que cada um faz e em que momento ele entra.',
			'description'  => 'O que passar na peça de mosaico depois do rejunte: verniz, impermeabilizante e selador, com a frase do próprio fabricante de cada produto.',
			'o_que_e'  => 'Acabamento, aqui, é o que se passa na peça depois de ela estar montada e rejuntada — verniz e impermeabilizante — mais o selador, que é o contrário: vai na base antes de colar. Os três andam juntos porque são a mesma etapa da conversa, a de proteger, e separados porque entram em horas diferentes do trabalho.',
			'o_que_nao_e' => 'O que acabamento não é: cola, que une o caquinho à base, e rejunte, que preenche a junta entre eles. Esses dois têm ferramenta própria nesta casa e a resposta deles muda com a superfície e com o lugar.',
			'faq_propria' => array(
				array(
					'pergunta' => 'Preciso passar alguma coisa na peça depois do rejunte?',
					'resposta' => 'Depende de onde ela vai ficar, e a gente não vai fingir que tem a resposta pronta. Dos {itens} produtos deste banco, {com_momento} dizem com todas as letras em que momento entram; nos outros {sem_momento} o fabricante não data o produto, e deduzir pelo mecanismo seria afirmar no lugar dele.',
				),
				array(
					'pergunta' => 'Os fabricantes falam de peça de mosaico?',
					'resposta' => 'Quase nunca. Das {celulas} combinações de produto e superfície desta página — {itens} produtos vezes as {superficies} superfícies que a gente nomeia —, só {nomeadas} estão escritas na frase de algum fabricante. Nenhuma delas é vidro, e nenhuma é rejunte.',
				),
			),
		),

		/* AS TRÊS FILHAS, na ordem da intenção de compra (seção 9): quem procura
		   impermeabilizante tem a peça pronta no jardim e o problema na mão;
		   quem procura verniz está decidindo o visual; quem procura selador
		   ainda nem colou. A ordem da leva é esta; a ordem na tela é a da
		   linha do tempo do trabalho, que é como a pessoa entende. */
		'selador' => array(
			'tipo'     => 'selador',
			'slug'     => 'materiais/acabamento/selar-a-base-antes-de-fazer-mosaico',
			'titulo'   => 'Selar a base antes de fazer mosaico',
			'curto'    => 'Selador',
			'consulta' => 'selar a base antes de fazer mosaico: precisa de selador?',
			'resumo'   => 'O produto que vai na base antes de colar o caquinho — e a hora de espera que cada fabricante declara até dar para seguir.',
			'linha_mestra' => 'Selador é o único desta etapa que entra antes de tudo: ele vai na base, sozinho, e você espera. Aqui está quanto cada um manda esperar, e sobre o que cada fabricante escreveu que ele pode ir.',
			'description'  => 'Precisa selar a base antes de colar o mosaico? Os seladores do nosso banco, o tempo de secagem que cada fabricante declara e sobre o que ele escreveu.',
			'o_que_e'  => 'Selador é o produto que se passa na base crua para ela parar de beber — a parede nova, o MDF, o vaso de barro sem esmalte. Ele não cola nada e não protege a peça pronta: ele muda a superfície antes de o caquinho encostar nela.',
			'o_que_nao_e' => 'O que ele não é: verniz, que vem no fim, nem impermeabilizante, que é para a peça já montada. Quem confunde os dois momentos sela a peça depois do rejunte e fica sem o efeito.',
			'faq_propria' => array(
				array(
					'pergunta' => 'Quanto tempo preciso esperar depois de selar?',
					'resposta' => 'Os {itens} seladores do nosso banco declaram secagem final, e os números não são próximos. Está na tabela, um a um, com a frase de onde o número saiu. Em {com_relogio} deles dá para somar a espera inteira — demãos mais intervalo mais secagem; nos outros o fabricante não declara uma das parcelas, e a gente não empresta a do vizinho.',
				),
				array(
					'pergunta' => 'Serve para selar um vaso de cerâmica antes do mosaico?',
					'resposta' => 'Nenhum dos {itens} diz isso. As frases deles nomeiam {bases_cobertas} das {bases_no_vocabulario} superfícies que a gente lista, e cerâmica esmaltada não está entre elas. A gente prefere dizer que não sabe a escolher a mais parecida por você.',
				),
			),
		),
		'verniz' => array(
			'tipo'     => 'verniz',
			'slug'     => 'materiais/acabamento/verniz-para-peca-de-mosaico',
			'titulo'   => 'Verniz para peça de mosaico',
			'curto'    => 'Verniz',
			'consulta' => 'verniz para peça de mosaico artesanal: qual usar',
			'resumo'   => 'Brilhante ou fosco, película transparente, demãos e consumo — o que cada fabricante declara, e o que nenhum deles declara.',
			'linha_mestra' => 'Verniz é o que decide se a peça fica brilhante ou fosca, e é a última camada do trabalho. Aqui estão os vernizes do nosso banco com o acabamento que cada fabricante declara e o que ele deixa sobre a peça.',
			'description'  => 'Qual verniz usar na peça de mosaico: brilhante ou fosco, película, demãos e consumo, com a frase que cada fabricante publica sobre o produto.',
			'o_que_e'  => 'Verniz é a camada final: passa na peça já rejuntada e seca, e muda o aspecto dela — brilhante ou fosco — enquanto protege o que está embaixo. É o produto desta etapa que mais gente procura, e o único em que a escolha é também de gosto.',
			'o_que_nao_e' => 'O que ele não é: impermeabilizante. Os dois formam película e as embalagens se parecem, mas um é feito para o visual e o outro para a água, e a frase do fabricante separa os dois melhor que a prateleira.',
			'faq_propria' => array(
				array(
					'pergunta' => 'Verniz brilhante ou fosco, qual é melhor para mosaico?',
					'resposta' => 'Nenhum dos {itens} fabricantes responde isso, e é gosto. O que dá para dizer com fonte está na tabela: qual deles declara brilhante, qual declara fosco e o que cada um deixa sobre a peça depois de seco.',
				),
				array(
					'pergunta' => 'Posso passar verniz em cima de pastilha de vidro?',
					'resposta' => 'Nenhuma das {celulas} combinações desta página diz isso. Das {superficies} superfícies que a gente nomeia, as frases destes {itens} vernizes alcançam {nomeadas} — e vidro, pastilha de vidro e rejunte ficam de fora das três. É a lacuna que a gente registrou em vez de preencher com palpite.',
				),
			),
		),
		'impermeabilizante' => array(
			'tipo'     => 'impermeabilizante',
			'slug'     => 'materiais/acabamento/impermeabilizar-peca-de-mosaico',
			'titulo'   => 'Impermeabilizar a peça de mosaico',
			'curto'    => 'Impermeabilizante',
			'consulta' => 'como impermeabilizar peça de mosaico para ficar no jardim, na chuva',
			'resumo'   => 'Peça que fica no sol e na chuva: o que cada fabricante escreveu, de que o produto é feito e onde ele próprio manda não usar.',
			'linha_mestra' => 'Peça que vai para o jardim leva sol, chuva e geada, e a pergunta é o que passar nela. Aqui estão os impermeabilizantes do nosso banco, do que cada um é feito e onde o próprio fabricante escreve para não usar.',
			'description'  => 'Como impermeabilizar a peça de mosaico que fica no jardim: o que cada fabricante declara, a base química do produto e onde ele manda não usar.',
			'o_que_e'  => 'Impermeabilizante é o que se passa na peça pronta para a água não entrar. Nesta etapa ele é o produto da peça que vive fora de casa — o vaso no canteiro, o número de casa no muro, o tampo da varanda.',
			'o_que_nao_e' => 'O que ele não é: verniz de acabamento. Um dos três do nosso banco é vendido como resina e dá brilho, e ainda assim o fabricante escreve que ele não vai em superfície horizontal — que é exatamente o tampo e o centro de mesa.',
			'faq_propria' => array(
				array(
					'pergunta' => 'Serve para o tampo de mesa de mosaico que fica na varanda?',
					'resposta' => 'Um dos {itens} exclui esse caso por escrito: o fabricante diz que não se recomenda o uso em superfícies horizontais. A frase inteira está na tabela, e é dele, não nossa. Os outros não falam de tampo nem para sim nem para não.',
				),
				array(
					'pergunta' => 'Dá para impermeabilizar por cima do rejunte?',
					'resposta' => 'Nenhum dos {itens} escreve a palavra rejunte, e isso a gente contou: nas {celulas} combinações desta página, as frases nomeiam {nomeadas} superfícies e o rejunte não é uma delas. Concluir pelo mecanismo — poroso, logo pega — seria afirmar no lugar do fabricante.',
				),
			),
		),
	);
}
}

if ( ! function_exists( 'cdm_guia_ids' ) ) {
function cdm_guia_ids() {
	return array_keys( cdm_guia_registro() );
}
}

if ( ! function_exists( 'cdm_guia_ficha' ) ) {
/** A ficha editorial de uma página do Guia, ou array() se ela não existe. */
function cdm_guia_ficha( $id ) {
	$r = cdm_guia_registro();

	return isset( $r[ $id ] ) ? $r[ $id ] : array();
}
}

if ( ! function_exists( 'cdm_guia_id_do_slug' ) ) {
/** Qual página do Guia mora neste endereço. '' quando nenhuma. */
function cdm_guia_id_do_slug( $slug ) {
	foreach ( cdm_guia_registro() as $id => $ficha ) {
		if ( $ficha['slug'] === $slug ) {
			return $id;
		}
	}

	return '';
}
}

if ( ! function_exists( 'cdm_guia_mae' ) ) {
/** O id da mãe desta família — a página cujo recorte é a categoria inteira. */
function cdm_guia_mae() {
	foreach ( cdm_guia_registro() as $id => $ficha ) {
		if ( null === $ficha['tipo'] ) {
			return $id;
		}
	}

	return '';
}
}

if ( ! function_exists( 'cdm_guia_filhas' ) ) {
/** As filhas, na ordem do registro. */
function cdm_guia_filhas() {
	$filhas = array();
	foreach ( cdm_guia_registro() as $id => $ficha ) {
		if ( null !== $ficha['tipo'] ) {
			$filhas[ $id ] = $ficha;
		}
	}

	return $filhas;
}
}

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — as páginas, a árvore e o cartão do Guia
 *
 * A ORDEM IMPORTA e ela é garantida pelo registro: a mãe vem primeiro, e
 * `cdm_casca_garantir_paginas()` adia a filha cuja mãe ainda não existe. Esta é
 * a primeira camada desta ilha a registrar FILHA DE FILHA, e o comentário do
 * filtro `cdm_paginas` já avisava, desde a casca 1.5.0, que quem fizer isso
 * cuida da própria ordem.
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	foreach ( cdm_guia_registro() as $id => $ficha ) {
		$pai = ( null === $ficha['tipo'] ) ? 'materiais' : cdm_guia_registro()[ cdm_guia_mae() ]['slug'];
		$paginas[ $ficha['slug'] ] = array(
			'titulo'    => $ficha['titulo'],
			'conteudo'  => '[cdm_guia_' . $id . ']',
			'pai'       => $pai,
			'descricao' => $ficha['description'],
		);
	}

	return $paginas;
} );

/* O CARTÃO DA CATEGORIA NO GUIA RECEBE O NOME DA PÁGINA, e quem o troca é quem
   publica a página — o mesmo desenho que a F2 usa com `cdm_ferramentas` desde
   11/09/2026. Sem esta linha a ilha teria dois nomes para o mesmo endereço: o
   cartão e o degrau da trilha diriam "Acabamento" e o H1 diria outra coisa, que
   é a cicatriz de 11/09/2026 na Aquametria. O `resumo` também vem daqui, porque
   ele passou a descrever uma página que existe em vez de uma promessa. */
add_filter( 'cdm_categorias_do_guia', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	$mae = cdm_guia_ficha( cdm_guia_mae() );
	if ( ! $mae ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['slug'] ) && $mae['slug'] === $c['slug'] ) {
			$lista[ $i ]['titulo'] = $mae['titulo'];
			$lista[ $i ]['resumo'] = $mae['resumo'];
		}
	}

	return $lista;
} );

/* AS FILHAS ENTRAM NA ÁRVORE COM A MÃE DE NÍVEL 2, nível 3 de verdade. É a
   primeira vez nesta ilha: as duas ferramentas e as duas técnicas penduram em
   nível 1 porque a categoria delas não existia quando nasceram. A mãe não
   precisa de linha aqui — ela entra pelo mesmo registro de categorias que
   desenha os cartões, e é assim que o mapa não envelhece. */
add_filter( 'cdm_arvore', function ( $mapa ) {
	if ( ! is_array( $mapa ) ) {
		return $mapa;
	}
	$mae = cdm_guia_ficha( cdm_guia_mae() );
	foreach ( cdm_guia_filhas() as $ficha ) {
		if ( isset( $mapa[ $ficha['slug'] ] ) ) {
			continue;
		}
		$mapa[ $ficha['slug'] ] = array(
			'nivel'  => 3,
			'mae'    => $mae ? $mae['slug'] : 'materiais',
			'rotulo' => $ficha['titulo'],
		);
	}

	return $mapa;
} );

/* ---------------------------------------------------------------------------
 * 2. O banco, lido da option que o Sync grava
 *
 * Sem banco a página NÃO inventa: ela diz que a medição não chegou. É a mesma
 * trava que a Robometria escreveu em 11/09/2026 e que a F2 e as técnicas desta
 * ilha repetem — e o `render-para-teste.php` sabe fabricar esse mundo
 * (`sem_banco=1`), que é o que faz a trava ser medida em vez de suposta.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_guia_banco' ) ) {
function cdm_guia_banco() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}

	$arquivo = get_option( 'clubedomosaico_dados_materiais-acabamento' );
	if ( is_string( $arquivo ) ) {
		$arquivo = json_decode( $arquivo, true );
	}

	$itens = array();
	if ( is_array( $arquivo ) && ! empty( $arquivo['materiais'] ) && is_array( $arquivo['materiais'] ) ) {
		foreach ( $arquivo['materiais'] as $m ) {
			if ( empty( $m['id'] ) || 'ativo' !== ( isset( $m['status'] ) ? $m['status'] : '' ) ) {
				continue;
			}
			$itens[ $m['id'] ] = $m;
		}
	}
	ksort( $itens );

	$esquema = get_option( 'clubedomosaico_dados_esquema-banco' );
	if ( is_string( $esquema ) ) {
		$esquema = json_decode( $esquema, true );
	}

	$banco = array(
		'itens'    => $itens,
		'esquema'  => is_array( $esquema ) ? $esquema : array(),
		'completo' => ( $itens && is_array( $esquema ) && ! empty( $esquema['vocabularios'] ) ),
	);

	return $banco;
}
}

if ( ! function_exists( 'cdm_guia_superficies' ) ) {
/**
 * AS SUPERFÍCIES DO VOCABULÁRIO — as 9 bases e os 6 caquinhos, lidas do esquema
 * e NUNCA escritas aqui.
 *
 * É o denominador do número que estas páginas publicam, e por isso ele tem de
 * crescer sozinho: no dia em que o vocabulário ganhar `ceramica_crua`, a conta
 * de cobertura muda na mesma passada, sem ninguém editar este arquivo. Uma
 * segunda lista aqui seria a cópia que envelhece calada.
 */
function cdm_guia_superficies() {
	$banco = cdm_guia_banco();
	$v     = isset( $banco['esquema']['vocabularios'] ) ? $banco['esquema']['vocabularios'] : array();
	$bases = ( isset( $v['base'] ) && is_array( $v['base'] ) ) ? array_values( $v['base'] ) : array();
	$tess  = ( isset( $v['material_tessela'] ) && is_array( $v['material_tessela'] ) ) ? array_values( $v['material_tessela'] ) : array();

	return array( 'base' => $bases, 'tessela' => $tess );
}
}

if ( ! function_exists( 'cdm_guia_rotulo' ) ) {
/**
 * O nome na tela de um valor do vocabulário.
 *
 * QUEM MANDA É A F2: é ela que imprime esses rótulos no formulário desde
 * 11/09/2026, e duas páginas que chamam a mesma coisa por nomes diferentes são
 * duas páginas que a pessoa lê como dois assuntos. Quando a F2 não está
 * carregada — mundo que a bancada fabrica com `sem_f2=1` — a chave do
 * vocabulário sai legível, e isso não é uma segunda decisão: é a mesma lista,
 * sem a tradução de quem é dono dela.
 */
function cdm_guia_rotulo( $eixo, $valor ) {
	if ( function_exists( 'cdm_f2_rotulos' ) ) {
		$rot   = cdm_f2_rotulos();
		$chave = ( 'base' === $eixo ) ? 'base_curto' : 'tessela';
		if ( isset( $rot[ $chave ][ $valor ] ) ) {
			return mb_strtolower( $rot[ $chave ][ $valor ], 'UTF-8' );
		}
	}

	return str_replace( '_', ' ', (string) $valor );
}
}

if ( ! function_exists( 'cdm_guia_lista_humana' ) ) {
/** "a, b e c". A régua é a da F2; sem ela, a mesma junção, escrita curta. */
function cdm_guia_lista_humana( $itens ) {
	if ( function_exists( 'cdm_f2_lista_humana' ) ) {
		return cdm_f2_lista_humana( $itens );
	}
	$itens = array_values( array_unique( array_filter( (array) $itens ) ) );
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

/* ---------------------------------------------------------------------------
 * 3. AS CONTAS — tudo o que a página publica como número sai daqui
 *
 * Uma função, um recorte, nenhum número digitado. É ela que o `teste-guia.php`
 * mede contra uma régua escrita à parte, e é ela que preenche a `description`
 * com número e a promessa do `<title>`: a frase da busca e a frase da tela não
 * podem sair de duas contas.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_guia_valor' ) ) {
/** O valor declarado de uma propriedade, ou null. Propriedade sem fonte não é valor. */
function cdm_guia_valor( $item, $propriedade ) {
	if ( empty( $item['propriedades'][ $propriedade ] ) || ! is_array( $item['propriedades'][ $propriedade ] ) ) {
		return null;
	}
	$p = $item['propriedades'][ $propriedade ];
	if ( ! isset( $p['valor'] ) || null === $p['valor'] ) {
		return null;
	}
	if ( empty( $p['fonte_id'] ) ) {
		return null;
	}

	return $p['valor'];
}
}

if ( ! function_exists( 'cdm_guia_relogio' ) ) {
/**
 * A ESPERA INTEIRA, da primeira demão até a peça pronta, em horas.
 *
 *   (demãos − 1) × intervalo entre demãos + secagem final
 *
 * Aritmética desta ilha sobre três declarações do fabricante, no mesmo desenho
 * dos gramas de rejunte da F1. Devolve null quando QUALQUER uma das parcelas
 * falta — e esse null é o produto, não a falha: é ele que faz a página escrever
 * "o fabricante não declara" em vez de emprestar o número do irmão de banco.
 *
 * Com uma demão só não há intervalo a somar, e aí a espera é a secagem final.
 */
function cdm_guia_relogio( $item ) {
	$demaos   = cdm_guia_valor( $item, 'demaos_minimas' );
	$secagem  = cdm_guia_valor( $item, 'tempo_de_secagem_h' );
	$intervalo = cdm_guia_valor( $item, 'intervalo_entre_demaos_min' );

	if ( ! is_numeric( $demaos ) || ! is_numeric( $secagem ) ) {
		return null;
	}
	$demaos  = (int) $demaos;
	$secagem = (float) $secagem;
	if ( $demaos < 1 ) {
		return null;
	}
	if ( 1 === $demaos ) {
		return $secagem;
	}
	if ( ! is_numeric( $intervalo ) ) {
		return null;
	}

	return ( $demaos - 1 ) * ( (float) $intervalo / 60.0 ) + $secagem;
}
}

if ( ! function_exists( 'cdm_guia_contas' ) ) {
function cdm_guia_contas( $id ) {
	static $cache = array();
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}

	$ficha = cdm_guia_ficha( $id );
	$banco = cdm_guia_banco();
	$sup   = cdm_guia_superficies();
	$tipo  = isset( $ficha['tipo'] ) ? $ficha['tipo'] : null;

	$itens = array();
	foreach ( $banco['itens'] as $chave => $m ) {
		if ( null !== $tipo && ( ! isset( $m['tipo'] ) || $m['tipo'] !== $tipo ) ) {
			continue;
		}
		$itens[ $chave ] = $m;
	}

	$n_sup      = count( $sup['base'] ) + count( $sup['tessela'] );
	$nomeadas   = 0;
	$bases_cob  = array();
	$tess_cob   = array();
	$momentos   = array();
	$relogios   = array();
	$nomeia_rej = 0;

	foreach ( $itens as $chave => $m ) {
		$p = isset( $m['protecao'] ) && is_array( $m['protecao'] ) ? $m['protecao'] : array();

		$b = isset( $p['bases_do_vocabulario_que_a_frase_nomeia'] ) ? (array) $p['bases_do_vocabulario_que_a_frase_nomeia'] : array();
		$t = isset( $p['tesselas_do_vocabulario_que_a_frase_nomeia'] ) ? (array) $p['tesselas_do_vocabulario_que_a_frase_nomeia'] : array();
		/* SÓ CONTA O QUE ESTÁ NO VOCABULÁRIO DE HOJE. Valor que saiu do
		   vocabulário e ficou no registro contaria uma cobertura que o site não
		   sabe mais nomear — e o denominador já é o vocabulário. */
		$b = array_values( array_intersect( $b, $sup['base'] ) );
		$t = array_values( array_intersect( $t, $sup['tessela'] ) );

		$nomeadas += count( $b ) + count( $t );
		$bases_cob = array_merge( $bases_cob, $b );
		$tess_cob  = array_merge( $tess_cob, $t );

		$momento = isset( $p['momento_de_uso'] ) ? (string) $p['momento_de_uso'] : 'nao_declarado';
		if ( ! isset( $momentos[ $momento ] ) ) {
			$momentos[ $momento ] = array();
		}
		$momentos[ $momento ][] = $chave;

		$h = cdm_guia_relogio( $m );
		if ( null !== $h ) {
			$relogios[ $chave ] = $h;
		}
		if ( ! empty( $p['nomeia_rejunte'] ) ) {
			$nomeia_rej++;
		}
	}

	$bases_cob = array_values( array_unique( $bases_cob ) );
	$tess_cob  = array_values( array_unique( $tess_cob ) );

	$com_momento = 0;
	foreach ( $momentos as $m => $lista ) {
		if ( 'nao_declarado' !== $m ) {
			$com_momento += count( $lista );
		}
	}

	$contas = array(
		'itens'                 => array_keys( $itens ),
		'n_itens'               => count( $itens ),
		'bases_no_vocabulario'  => count( $sup['base'] ),
		'tesselas_no_vocabulario' => count( $sup['tessela'] ),
		'superficies'           => $n_sup,
		'celulas'               => count( $itens ) * $n_sup,
		'nomeadas'              => $nomeadas,
		'bases_cobertas'        => $bases_cob,
		'tesselas_cobertas'     => $tess_cob,
		'momentos'              => $momentos,
		'com_momento'           => $com_momento,
		'sem_momento'           => count( $itens ) - $com_momento,
		'relogios'              => $relogios,
		'com_relogio'           => count( $relogios ),
		'nomeiam_rejunte'       => $nomeia_rej,
	);

	$cache[ $id ] = $contas;

	return $contas;
}
}

if ( ! function_exists( 'cdm_guia_pronta' ) ) {
/** A página só se serve inteira com banco e vocabulário no site, e com item. */
function cdm_guia_pronta( $id ) {
	$banco = cdm_guia_banco();
	if ( ! $banco['completo'] ) {
		return false;
	}
	$c = cdm_guia_contas( $id );

	return ( $c['n_itens'] > 0 && $c['superficies'] > 0 );
}
}

if ( ! function_exists( 'cdm_guia_preencher' ) ) {
/** Troca as chaves de um molde pelas contas da própria página. */
function cdm_guia_preencher( $texto, $contas ) {
	$troca = array();
	foreach ( array(
		'itens'                => $contas['n_itens'],
		'celulas'              => $contas['celulas'],
		'superficies'          => $contas['superficies'],
		'nomeadas'             => $contas['nomeadas'],
		'com_momento'          => $contas['com_momento'],
		'sem_momento'          => $contas['sem_momento'],
		'com_relogio'          => $contas['com_relogio'],
		'bases_cobertas'       => count( $contas['bases_cobertas'] ),
		'bases_no_vocabulario' => $contas['bases_no_vocabulario'],
	) as $chave => $valor ) {
		$troca[ '{' . $chave . '}' ] = number_format_i18n( (float) $valor );
	}

	return strtr( (string) $texto, $troca );
}
}

if ( ! function_exists( 'cdm_guia_lacunas' ) ) {
/**
 * AS SUPERFÍCIES QUE NENHUM FABRICANTE DO RECORTE NOMEIA.
 *
 * É o complemento da cobertura, e é o que a página publica como achado. Sai
 * derivado dos dois lados — vocabulário menos cobertura —, então no dia em que
 * um fabricante novo nomear vidro, a frase do vidro some sozinha da página. Foi
 * para isso que ela não foi escrita à mão: frase cravada envelhece calada.
 */
function cdm_guia_lacunas( $id ) {
	$c   = cdm_guia_contas( $id );
	$sup = cdm_guia_superficies();

	return array(
		'base'    => array_values( array_diff( $sup['base'], $c['bases_cobertas'] ) ),
		'tessela' => array_values( array_diff( $sup['tessela'], $c['tesselas_cobertas'] ) ),
	);
}
}

if ( ! function_exists( 'cdm_guia_frase_da_lacuna' ) ) {
/**
 * A frase que diz o que falta, montada do que falta — nunca uma lista digitada.
 *
 * O vidro e o rejunte entram por nome quando estão de fora porque são o que
 * uma peça de mosaico expõe: a pastilha é de vidro e a junta é de rejunte. Mas
 * quem decide se eles entram na frase é a conta, não este comentário.
 */
function cdm_guia_frase_da_lacuna( $id ) {
	$c    = cdm_guia_contas( $id );
	$lac  = cdm_guia_lacunas( $id );
	$nomes = array();

	foreach ( array( 'vidro', 'espelho' ) as $chave ) {
		if ( in_array( $chave, $lac['base'], true ) ) {
			$nomes[] = cdm_guia_rotulo( 'base', $chave );
		}
	}
	foreach ( array( 'pastilha_vidro', 'pastilha_ceramica' ) as $chave ) {
		if ( in_array( $chave, $lac['tessela'], true ) ) {
			$nomes[] = cdm_guia_rotulo( 'tessela', $chave );
		}
	}
	if ( 0 === (int) $c['nomeiam_rejunte'] ) {
		$nomes[] = 'o rejunte';
	}

	if ( ! $nomes ) {
		return '';
	}

	return 'Entre o que ninguém deste grupo nomeia está ' . cdm_guia_lista_humana( $nomes )
		. ' — que é justamente o que uma peça de mosaico mostra por fora.';
}
}

/* ---------------------------------------------------------------------------
 * 4. A PÁGINA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_guia_numero' ) ) {
/** Número com vírgula decimal e sem casa à toa: 20 e 2,5, nunca 20,0. */
function cdm_guia_numero( $valor ) {
	$valor = (float) $valor;
	$casas = ( abs( $valor - round( $valor ) ) < 0.01 ) ? 0 : 1;

	return number_format_i18n( $valor, $casas );
}
}

if ( ! function_exists( 'cdm_guia_fonte_principal' ) ) {
/** A fonte de MENOR nível (o boletim antes da página de produto), ou array(). */
function cdm_guia_fonte_principal( $item ) {
	$melhor = array();
	foreach ( (array) ( isset( $item['fontes'] ) ? $item['fontes'] : array() ) as $f ) {
		if ( ! is_array( $f ) || empty( $f['url'] ) ) {
			continue;
		}
		$nivel = isset( $f['nivel'] ) ? (int) $f['nivel'] : 9;
		if ( ! $melhor || $nivel < (int) $melhor['nivel'] ) {
			$melhor          = $f;
			$melhor['nivel'] = $nivel;
		}
	}

	return $melhor;
}
}

if ( ! function_exists( 'cdm_guia_numeros_do_item' ) ) {
/**
 * OS NÚMEROS DECLARADOS DE UM PRODUTO, na ordem em que a pessoa os usa.
 *
 * A lista de propriedades é fixa porque o esquema a fixa — ela é
 * `as_propriedades_tem_NOME_FIXO_e_esta_e_a_lista` de
 * `regras_da_categoria_acabamento`. O que NÃO é fixo é quais delas cada
 * produto declara: propriedade sem valor não vira linha, e é esse silêncio que
 * a coluna da tabela mostra.
 */
function cdm_guia_numeros_do_item( $item ) {
	$mapa = array(
		'demaos_minimas'            => array( 'demãos', '' ),
		'intervalo_entre_demaos_min' => array( 'entre demãos', 'min' ),
		'tempo_de_secagem_h'        => array( 'secagem final', 'h' ),
		'consumo_ml_m2'             => array( 'consumo', 'mL/m²' ),
		'liberacao_trafego_leve_h'  => array( 'liberação para uso leve', 'h' ),
		'liberacao_total_dias'      => array( 'liberação total', 'dias' ),
		'elasticidade_pct'          => array( 'elasticidade', '%' ),
		'temperatura_min_c'         => array( 'aplicar acima de', '°C' ),
		'temperatura_max_c'         => array( 'aplicar abaixo de', '°C' ),
		'acabamento_visual'         => array( 'acabamento', '' ),
		'pelicula'                  => array( 'deixa película', '' ),
		'base_quimica'              => array( 'feito de', '' ),
		'pigmentado'                => array( 'pigmentado', '' ),
		'forma_de_aplicacao'        => array( 'aplicação', '' ),
		'diluicao'                  => array( 'diluição', '' ),
	);

	$linhas = array();
	foreach ( $mapa as $propriedade => $par ) {
		$valor = cdm_guia_valor( $item, $propriedade );
		if ( null === $valor ) {
			continue;
		}
		$texto = is_numeric( $valor ) ? cdm_guia_numero( $valor ) : (string) $valor;
		if ( '' !== $par[1] ) {
			$texto .= ' ' . $par[1];
		}
		$linhas[] = array( 'rotulo' => $par[0], 'valor' => $texto );
	}

	return $linhas;
}
}

if ( ! function_exists( 'cdm_guia_ficha_do_produto_html' ) ) {
/**
 * A FICHA DE UM PRODUTO: o que o fabricante escreveu, os números dele e o
 * bloco de compra.
 *
 * O BLOCO DE COMPRA DESCE A ESCADA DA SEÇÃO 25 pela função da F2, que é a dona
 * dela desde 11/09/2026 e que diz, no próprio cabeçalho, "quem for servir a
 * escada na ficha do Guia (...) chama esta função em vez de reescrever os
 * quatro estados". Sem a F2 carregada, o bloco diz que a lista está fora do ar
 * — é a saída degradada que a F1 já tem em duas vitrines.
 */
function cdm_guia_ficha_do_produto_html( $item ) {
	$p     = isset( $item['protecao'] ) && is_array( $item['protecao'] ) ? $item['protecao'] : array();
	$fonte = cdm_guia_fonte_principal( $item );
	$sup   = cdm_guia_superficies();

	$html = '<li class="cdm-guia-cartao">';

	if ( ! empty( $item['imagem']['url'] ) ) {
		$html .= '<img class="cdm-guia-foto" src="' . esc_url( $item['imagem']['url'] ) . '"'
			. ' width="' . (int) $item['imagem']['largura'] . '" height="' . (int) $item['imagem']['altura'] . '"'
			. ' loading="lazy" alt="' . esc_attr( isset( $item['imagem']['alt'] ) ? $item['imagem']['alt'] : $item['nome_comercial'] ) . '">';
	} else {
		$html .= '<span class="cdm-guia-sem-foto" aria-hidden="true"></span>';
	}

	$html .= '<span class="cdm-guia-marca">' . esc_html( isset( $item['marca'] ) ? $item['marca'] : '' ) . '</span>';
	$html .= '<h3>' . esc_html( $item['nome_comercial'] ) . '</h3>';

	/* SOBRE O QUE O FABRICANTE ESCREVEU QUE ELE VAI, no vocabulário desta ilha.
	   Quando a frase não encosta em nenhuma das nossas superfícies, a página
	   diz isso — é a informação, não a falta dela. */
	$nomeia = array();
	foreach ( array_intersect( (array) ( isset( $p['bases_do_vocabulario_que_a_frase_nomeia'] ) ? $p['bases_do_vocabulario_que_a_frase_nomeia'] : array() ), $sup['base'] ) as $b ) {
		$nomeia[] = cdm_guia_rotulo( 'base', $b );
	}
	foreach ( array_intersect( (array) ( isset( $p['tesselas_do_vocabulario_que_a_frase_nomeia'] ) ? $p['tesselas_do_vocabulario_que_a_frase_nomeia'] : array() ), $sup['tessela'] ) as $t ) {
		$nomeia[] = cdm_guia_rotulo( 'tessela', $t );
	}
	if ( $nomeia ) {
		$html .= '<p class="cdm-guia-nomeia">Das superfícies que a gente lista, a frase dele nomeia <strong>'
			. esc_html( cdm_guia_lista_humana( $nomeia ) ) . '</strong>.</p>';
	} else {
		$html .= '<p class="cdm-guia-nomeia">A frase dele não nomeia nenhuma das superfícies que a gente lista.</p>';
	}

	$numeros = cdm_guia_numeros_do_item( $item );
	if ( $numeros ) {
		$html .= '<dl class="cdm-guia-numeros">';
		foreach ( $numeros as $linha ) {
			$html .= '<dt>' . esc_html( $linha['rotulo'] ) . '</dt><dd>' . esc_html( $linha['valor'] ) . '</dd>';
		}
		$html .= '</dl>';
	}

	$relogio = cdm_guia_relogio( $item );
	if ( null !== $relogio ) {
		$html .= '<p class="cdm-guia-relogio">Da primeira demão até a peça pronta, pela conta do próprio fabricante: <strong>'
			. esc_html( cdm_guia_numero( $relogio ) ) . ' horas</strong>.</p>';
	} else {
		$html .= '<p class="cdm-guia-relogio cdm-guia-sem-conta">O fabricante não declara as três partes da espera, então a gente não soma — '
			. 'emprestar o número do vizinho de prateleira seria inventar o que falta.</p>';
	}

	/* A FRASE DO FABRICANTE, INTEIRA E ENTRE ASPAS. É a camada de prova desta
	   página: a recomendação não é nossa, e quem quiser conferir tem o
	   endereço e a data da leitura logo abaixo. */
	if ( ! empty( $p['literal_do_fabricante'] ) ) {
		$html .= '<blockquote class="cdm-prova cdm-guia-literal"><p>'
			. esc_html( $p['literal_do_fabricante'] ) . '</p></blockquote>';
	}

	if ( function_exists( 'cdm_f2_compra_html' ) ) {
		$html .= cdm_f2_compra_html( isset( $item['afiliado'] ) ? $item['afiliado'] : array() );
	} else {
		$html .= '<p class="cdm-guia-sem-loja">A lista de onde comprar está fora do ar neste momento. O produto e a declaração acima continuam de pé.</p>';
	}

	if ( $fonte && ! empty( $fonte['url'] ) ) {
		$html .= '<span class="cdm-guia-fonte"><a href="' . esc_url( $fonte['url'] ) . '"'
			. ' rel="nofollow noopener" target="_blank">fonte</a>'
			. ( ! empty( $fonte['coletado_em'] ) && function_exists( 'cdm_casca_data_br' )
				? ' · lido em ' . esc_html( cdm_casca_data_br( $fonte['coletado_em'] ) ) : '' )
			. '</span>';
	}

	$html .= '</li>';

	return $html;
}
}

if ( ! function_exists( 'cdm_guia_html' ) ) {
function cdm_guia_html( $id ) {
	$ficha = cdm_guia_ficha( $id );
	if ( ! $ficha ) {
		return '';
	}

	if ( ! cdm_guia_pronta( $id ) ) {
		return '<div class="cdm-bloco"><div class="cdm-vazio">'
			. '<h3>A medição desta página ainda não chegou ao site</h3>'
			. '<p>Ela não vai inventar uma recomendação enquanto isso. Volte daqui a pouco, ou use o '
			. ( function_exists( 'cdm_casca_link_html' ) ? cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' ) : 'guia de materiais' )
			. ', que pergunta a superfície e o lugar.</p></div></div>';
	}

	$c     = cdm_guia_contas( $id );
	$banco = cdm_guia_banco();
	$mae   = cdm_guia_ficha( cdm_guia_mae() );
	$e_mae = ( null === $ficha['tipo'] );

	$html = '<div class="cdm-bloco cdm-guia">';

	/* A LINHA MESTRA — o que a pessoa recebe, em uma linha, na voz do VOZ.md:
	   sem fabricante, sem data e sem a palavra "substrato". */
	$html .= '<p class="cdm-linha-mestra">' . esc_html( $ficha['linha_mestra'] ) . '</p>';

	/* A RESPOSTA ANTES DA EXPLICAÇÃO, com o número contado do banco. */
	$html .= '<div class="cdm-guia-resposta"><p class="cdm-guia-frase">';
	if ( $e_mae ) {
		$html .= 'São <strong>' . (int) $c['n_itens'] . ' produtos</strong> no nosso banco para esta etapa, em três grupos. '
			. 'Deles, <strong>' . (int) $c['com_momento'] . '</strong> dizem com todas as letras em que momento entram, e '
			. (int) $c['sem_momento'] . ' não dizem — e a gente não deduz pelo mecanismo. ';
	} else {
		$html .= 'São <strong>' . (int) $c['n_itens'] . ' produtos</strong> deste tipo no nosso banco, '
			. 'e o que cada um atende sai da frase do próprio fabricante, não da nossa opinião. ';
	}
	$html .= 'Das <strong>' . (int) $c['celulas'] . '</strong> combinações de produto e superfície desta página — '
		. (int) $c['n_itens'] . ' produtos vezes as ' . (int) $c['superficies'] . ' superfícies que a gente nomeia —, '
		. '<strong>' . (int) $c['nomeadas'] . '</strong> estão escritas na frase de algum fabricante.';
	$html .= '</p>';
	$html .= '<p class="cdm-prova cdm-guia-prova">Cada número desta página é lido do que o fabricante publicou, '
		. 'com o endereço e a data da leitura na ficha de cada produto. Onde ele não declara, está escrito que não declara.</p>';
	$html .= '</div>';

	/* A MÃE LISTA TODAS AS FILHAS, com o texto-âncora igual à consulta-alvo de
	   cada uma — 16.4(a) ao pé da letra, e nunca "saiba mais". */
	if ( $e_mae ) {
		$html .= '<div class="cdm-secao"><h2>As três etapas, e a hora de cada uma</h2>';
		$html .= '<ul class="cdm-guia-filhas">';
		foreach ( cdm_guia_filhas() as $fid => $f ) {
			$cf    = cdm_guia_contas( $fid );
			$html .= '<li><h3>' . cdm_casca_link_html( $f['slug'], $f['consulta'] ) . '</h3>'
				. '<p>' . esc_html( $f['resumo'] ) . '</p>'
				. '<p class="cdm-guia-conta-filha">' . (int) $cf['n_itens'] . ' produtos no banco.</p></li>';
		}
		$html .= '</ul></div>';
	}

	/* O QUE É, E O QUE NÃO É. */
	$html .= '<div class="cdm-secao"><h2>O que é, e o que não é</h2>';
	$html .= '<p>' . esc_html( $ficha['o_que_e'] ) . '</p>';
	$html .= '<p>' . esc_html( $ficha['o_que_nao_e'] ) . '</p>';
	if ( $e_mae ) {
		$html .= '<p>Quem está escolhendo cola ou rejunte está uma etapa antes: o '
			. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
			. ' pergunta a superfície e o lugar, e a '
			. cdm_casca_link_html( 'materiais/quantas-pastilhas-para-mosaico', 'conta de quantas pastilhas e quanto rejunte' )
			. ' diz quanto comprar. Esta página fica com o que vem depois deles.</p>';
	} else {
		/* 16.4(b): a filha linka a mãe no breadcrumb E numa frase do corpo. */
		$html .= '<p>Esta é uma das três etapas do '
			. cdm_casca_link_html( $mae['slug'], 'acabamento da peça de mosaico' )
			. ', que é a página onde as três aparecem lado a lado. Um passo antes dela, o '
			. cdm_casca_link_html( 'materiais/qual-cola-usar-no-mosaico', 'seletor de cola e rejunte' )
			. ' responde o que une o caquinho à base.</p>';
	}
	$html .= '</div>';

	/* PRODUTO POR PRODUTO. Na mãe, agrupado pelos três tipos, para os dez
	   aparecerem exatamente uma vez — que é a prestação de contas da seção 7. */
	$html .= '<div class="cdm-secao"><h2>Produto por produto, com a frase do fabricante</h2>';
	if ( $e_mae ) {
		foreach ( cdm_guia_filhas() as $fid => $f ) {
			$cf = cdm_guia_contas( $fid );
			if ( ! $cf['itens'] ) {
				continue;
			}
			$html .= '<h3 class="cdm-guia-grupo">' . cdm_casca_link_html( $f['slug'], $f['titulo'] ) . '</h3>';
			$html .= '<ul class="cdm-guia-cartoes">';
			foreach ( $cf['itens'] as $chave ) {
				$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ] );
			}
			$html .= '</ul>';
		}
	} else {
		$html .= '<ul class="cdm-guia-cartoes">';
		foreach ( $c['itens'] as $chave ) {
			$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ] );
		}
		$html .= '</ul>';
	}
	$html .= '</div>';

	/* O QUE NINGUÉM DECLARA — o achado desta família, contado. */
	$html .= '<div class="cdm-secao"><h2>O que nenhum destes fabricantes diz</h2>';
	$lac   = cdm_guia_lacunas( $id );
	$faltam = count( $lac['base'] ) + count( $lac['tessela'] );
	$html .= '<p>A gente nomeia ' . (int) $c['superficies'] . ' superfícies — ' . (int) $c['bases_no_vocabulario']
		. ' bases e ' . (int) $c['tesselas_no_vocabulario'] . ' tipos de caquinho. '
		. 'As frases ' . ( $e_mae ? 'destes ' . (int) $c['n_itens'] . ' produtos' : 'destes ' . (int) $c['n_itens'] . ' produtos' )
		. ' alcançam <strong>' . ( (int) $c['superficies'] - $faltam ) . '</strong> delas, e deixam <strong>'
		. (int) $faltam . '</strong> de fora. ' . esc_html( cdm_guia_frase_da_lacuna( $id ) ) . '</p>';
	$html .= '<p class="cdm-nao-fazemos">Não vamos escolher por semelhança o que o fabricante não escreveu. '
		. 'Enquanto a frase dele não nomear a superfície da sua peça, esta página diz que não sabe — '
		. 'e isso vale inclusive quando a química parece óbvia.</p>';
	$html .= '</div>';

	/* AS PERGUNTAS, com os números da própria página. */
	$html .= '<div class="cdm-secao cdm-guia-faq"><h2>Perguntas</h2><dl>';
	foreach ( cdm_guia_faq( $id ) as $p ) {
		$html .= '<dt>' . esc_html( $p['pergunta'] ) . '</dt><dd>' . esc_html( $p['resposta'] ) . '</dd>';
	}
	$html .= '</dl></div>';

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_guia_faq' ) ) {
/** As perguntas da página, com os moldes já preenchidos pelas contas dela. */
function cdm_guia_faq( $id ) {
	$ficha = cdm_guia_ficha( $id );
	if ( empty( $ficha['faq_propria'] ) ) {
		return array();
	}
	$c    = cdm_guia_contas( $id );
	$saida = array();
	foreach ( $ficha['faq_propria'] as $p ) {
		$saida[] = array(
			'pergunta' => cdm_guia_preencher( $p['pergunta'], $c ),
			'resposta' => cdm_guia_preencher( $p['resposta'], $c ),
		);
	}

	return $saida;
}
}

/* ---------------------------------------------------------------------------
 * 5. Os shortcodes — UM POR PÁGINA
 *
 * Um shortcode por página e não um só resolvendo pela página servida: é assim
 * que a bancada descobre QUE página está medindo, casando o shortcode com a
 * definição de páginas. Duas páginas com o mesmo shortcode seriam medidas como
 * se fossem a mesma, e a segunda nunca teria sido medida — a cicatriz que as
 * técnicas pagaram na 1.1.0.
 * ------------------------------------------------------------------------- */

foreach ( cdm_guia_ids() as $cdm_guia_id ) {
	add_shortcode( 'cdm_guia_' . $cdm_guia_id, function () use ( $cdm_guia_id ) {
		return cdm_guia_html( $cdm_guia_id );
	} );
}
unset( $cdm_guia_id );

/* ---------------------------------------------------------------------------
 * 6. Cabeça da página — description e JSON-LD
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_guia_id_da_pagina_atual' ) ) {
function cdm_guia_id_da_pagina_atual() {
	if ( ! function_exists( 'cdm_casca_slug_atual' ) ) {
		return '';
	}

	return cdm_guia_id_do_slug( cdm_casca_slug_atual() );
}
}

/* A `description` É DECLARADA, NÃO IMPRESSA — quem imprime é a casca, uma vez.
   Aqui ela já chega pela definição de páginas (o campo `descricao` do filtro
   `cdm_paginas`), e este filtro existe só para a camada ser a dona da sua
   etiqueta quando um dia ela quiser um número dentro. */
add_filter( 'cdm_descricao', function ( $d, $slug ) {
	$id = cdm_guia_id_do_slug( (string) $slug );
	if ( '' === $id ) {
		return $d;
	}
	$ficha = cdm_guia_ficha( $id );

	return isset( $ficha['description'] ) ? (string) $ficha['description'] : $d;
}, 10, 2 );

/* ESTAS QUATRO PÁGINAS NÃO DECLARAM PROMESSA NO `<title>`, E A AUSÊNCIA É A
   DECISÃO — não um esquecimento.

   A promessa numérica é a alavanca que a 12.1 nomeia para a banda de POSIÇÃO 4
   a 10: título que promete o número numa página que já está na primeira página
   e não é clicada. As três que a declaram nesta ilha são as três que a leitura
   de 23/09/2026 mediu ali, com CTR zero. Estas quatro nascem hoje, com zero
   impressão e sem posição nenhuma — não há CTR a consertar, e prometer um
   número antes de existir o problema gasta o teto de 65 caracteres com o que
   ainda não se sabe se ajuda.

   A `description` delas já carrega o conteúdo sem número, dentro da faixa de
   120 a 160. Quando a leitura semanal der posição a alguma destas quatro, a
   promessa entra com um `cdm_promessa` de três linhas, e aí ela será medida
   contra uma leitura anterior em vez de contra nada — que é o argumento que o
   despacho de 23/09 chamou de "deixe uma página parada". */

add_action( 'wp_head', function () {
	$id = cdm_guia_id_da_pagina_atual();
	if ( '' === $id || ! cdm_guia_pronta( $id ) ) {
		return;
	}
	$ficha = cdm_guia_ficha( $id );
	$limpa = home_url( '/' . $ficha['slug'] . '/' );

	$perguntas = array();
	foreach ( cdm_guia_faq( $id ) as $p ) {
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
				'description' => $ficha['description'],
				'about'       => array( '@type' => 'Thing', 'name' => $ficha['consulta'] ),
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

	echo '<script type="application/ld+json" id="cdm-guia-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 7. Folha — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML. Foi o defeito que derrubou
 * cinco calculadoras da Aquametria em 08/09/2026.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( '' === cdm_guia_id_da_pagina_atual() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-guia-css">
.cdm-guia-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-guia-frase{font-size:1.15rem;line-height:1.5;margin:0;}
.cdm-guia-prova{margin:1rem 0 0;}
.cdm-guia-filhas{list-style:none;margin:1rem 0;padding:0;display:grid;gap:1rem;}
.cdm-guia-filhas li{border:1px solid var(--cdm-traco);border-radius:2px;padding:1rem;}
.cdm-guia-filhas h3{margin:0 0 .35rem;font-size:1.05rem;}
.cdm-guia-filhas p{margin:0;}
.cdm-guia-conta-filha{color:var(--cdm-legenda);font-size:.9rem;margin-top:.4rem!important;font-family:var(--cdm-mono);}
.cdm-guia-grupo{font-size:1.05rem;margin:1.8rem 0 .4rem;}
.cdm-guia-cartoes{list-style:none;margin:1rem 0;padding:0;display:grid;gap:1.2rem;}
.cdm-guia-cartao{border:1px solid var(--cdm-traco);border-radius:2px;padding:1rem;}
.cdm-guia-cartao h3{margin:.2rem 0 .5rem;font-size:1.05rem;}
.cdm-guia-foto{float:right;width:88px;height:auto;margin:0 0 .6rem .8rem;border-radius:2px;}
.cdm-guia-sem-foto{float:right;display:block;width:88px;height:88px;margin:0 0 .6rem .8rem;background:var(--cdm-traco);border-radius:2px;}
.cdm-guia-marca{display:block;font-family:var(--cdm-mono);font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--cdm-legenda);}
.cdm-guia-nomeia{margin:.3rem 0;}
.cdm-guia-numeros{display:grid;grid-template-columns:auto 1fr;gap:.2rem .8rem;margin:.7rem 0;font-size:.95rem;}
.cdm-guia-numeros dt{color:var(--cdm-legenda);}
.cdm-guia-numeros dd{margin:0;font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;}
.cdm-guia-relogio{margin:.6rem 0;}
.cdm-guia-sem-conta{color:var(--cdm-legenda);font-size:.92rem;}
.cdm-guia-literal{margin:.8rem 0;padding:.6rem .9rem;border-left:2px solid var(--cdm-traco);}
.cdm-guia-literal p{margin:0;font-size:.92rem;color:var(--cdm-legenda);}
.cdm-guia-fonte{display:block;margin-top:.5rem;font-size:.85rem;color:var(--cdm-legenda);clear:both;}
.cdm-guia-sem-loja{color:var(--cdm-legenda);font-size:.92rem;}
.cdm-guia-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .3rem;}
.cdm-guia-faq dd{margin:0;}
@media (min-width:640px){.cdm-guia-filhas{grid-template-columns:repeat(3,1fr);}}
</style>
HTML;
}, 20 );

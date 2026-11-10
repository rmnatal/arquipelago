<?php
/**
 * RODAMETRIA — PAGINAS PELO NOME DO PRODUTO (secao 30 do ARQUIPELAGO.md)
 *
 * O motor da secao `/veiculos/` e das paginas de consulta de produto que nascem
 * filhas diretas dela: uma pagina por consulta de compra, slug igual a consulta.
 * Elas respondem "o que comprar quando a pessoa digita o NOME DO PRODUTO".
 *
 * -------------------------------------------------------------------------
 * POR QUE ELE E UM SNIPPET NOVO, E NAO UMA REGUA DENTRO DA F2
 * -------------------------------------------------------------------------
 * A F2 serve CONTA: ela recebe tensao e amperagem e devolve Wh e faixa de km,
 * e a camada de prova dela e a constante com fonte. Estas paginas servem
 * OFERTA DE LOJA, cuja procedencia e um anuncio datado — outra fonte, outra
 * regua de honestidade e outro prazo de validade. Juntar as duas faria a F2
 * decidir sobre dado que ela nao sabe medir, e a primeira vez que um anuncio
 * saisse do ar a calculadora cairia junto.
 *
 * -------------------------------------------------------------------------
 * AS DUAS METADES, E NENHUM NUMERO E DIGITADO AQUI
 * -------------------------------------------------------------------------
 *   - `dados/paginas-de-produto.json` e DECLARADO: titulo, description, a
 *     resposta em duas frases, o "qual escolher" e as perguntas. E a voz do
 *     `VOZ.md`, e a prosa dela traz MOLDES — {N}, {DE}, {ATE}, {MEDIANA},
 *     {DECLARAM_WATT}, {DIZEM_QUAL_WATT}, {SEM_WATT}, {LIDAS}, {RECUSADAS},
 *     {FRASE_DO_ROTULO}, {FRASE_DA_CARGA}, {DECLARAM_CARGA}, {CARGA_DE},
 *     {CARGA_ATE}, {CHAVE}, {DATA}.
 *   - `dados/vitrine-de-produto.json` e GERADO por
 *     `ferramentas/gerar-vitrine-de-produto.py`, que RECONTA tudo de
 *     `dados/anuncios-por-consulta.json` e sai com codigo 1 se discordar.
 *
 * Quem preenche os moldes e `rdm_produto_preencher()`. Preco escrito a mao na
 * frase e preco que mente na coleta seguinte, calado.
 *
 * -------------------------------------------------------------------------
 * A ORDEM DA TELA E A DA 32.2, E ELA NAO E A DA 32.1
 * -------------------------------------------------------------------------
 * Esta familia de pagina nao tem FORMULARIO, entao o teto de 700 px da 32.5 e
 * da CAIXA DE RESPOSTA e nao de um formulario que nao existe — e a 32.5-b e
 * explicita nisso ("portao que reprova pagina certa e o caminho mais curto para
 * alguem passar a ignora-lo"). De cima para baixo: trilha e H1 · caixa de
 * resposta com o numero em Mono · bloco de compra com `id="comprar"` · a
 * tabela-resumo VISIVEL, que e o que as IAs citam · a malha, tambem visivel
 * porque e alvo de link · o resto nas dobras · a barra fixa do telefone.
 *
 * -------------------------------------------------------------------------
 * O QUE A TABELA NAO TEM, E A DIFERENCA E HONESTIDADE
 * -------------------------------------------------------------------------
 * A 30.3 pede "tabela comparando os produtos". Potencia nominal, velocidade
 * maxima, acelerador e carga maxima NAO estao aqui, e nao e esquecimento: o
 * `niveis_minimos_por_campo` do esquema desta ilha exige nivel 5 ou melhor
 * nesses quatro, e titulo de anuncio e nivel 6. Entao a coluna diz o que o
 * anuncio DECLARA — "declara watt, sem dizer se e nominal ou de pico" — em vez
 * de preencher coluna tecnica com palavra tirada do titulo. A 30.2 manda
 * exatamente isso: "onde faltar, a pagina diz que falta e nao inventa".
 *
 * Sem `<script>` e sem `<style>` no retorno do shortcode (secao 8): o JSON-LD
 * sai no `wp_head` e a folha no `wp_footer`. Foi o E-comercial duplo dentro de
 * `<script>` que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 *
 * 1.2.0 (02/11/2026) — A MAE ENTROU NO MOLDE, e ela estava FORA dele desde que
 * nasceu. O portao de pixel desta ilha a listava como "sem componente de molde
 * nenhum", e o preco disso nao era feio: era que os 700 px da 32.5 NUNCA a
 * julgaram — regua que nao alcanca a pagina nao a reprova, so a ignora (32.5-c).
 * Entrou a CAIXA DE RESPOSTA da 32.2, com o numero AGREGADO das filhas prontas
 * (`rdm_produto_agregado_das_prontas()`) e a prosa escolhida por mundo numa
 * funcao PURA (`rdm_produto_caixa_frases()`), mais o SEGUNDO BOTAO do cartao de
 * cada familia, que cai no `id="comprar"` da filha. O titulo do cartao nao
 * mudou um byte: a 32.3 protege ancora e link interno.
 */

/* A VERSAO MORA NUMA CONSTANTE.
   ESTE COMENTARIO AFIRMAVA, ATE 30/10/2026, que "`atualizar-manifest.py` casa
   esta constante com o campo `versao` do manifest". NAO CASA, e nunca casou:
   a palavra `versao` nao aparece uma vez em `atualizar-manifest.py` (que espelha
   sha256 e sobe a revisao, e so), e os itens de `snippets` do `manifest.json` nao
   tem campo `versao` — medido nos quatro itens. Esta constante e a do
   `rodametria-f2` sao LIDAS POR NINGUEM; a da casca e a unica viva, porque e o
   gatilho de reinstalacao dela.
   E a familia do `height:44px` morto que a 32.5-d registra: comentario que
   declara um mecanismo parece conferido e nao mede nada. A constante fica, porque
   subi-la junto com o snippet e barato e e o rastro que a Robometria pagou para
   aprender; o que sai e a frase que prometia um portao inexistente. O portao que
   faltaria esta nomeado no `REGISTRO.md` desta ilha, na entrada de 30/10/2026, com
   a decisao de NAO mexer no esquema do `manifest.json` na mesma passada que leva a
   escada da 25.2 ao ar: aquele arquivo e o contrato do Sync, e o Sync e o unico
   canal de desembarque desta ilha. (`dados/consertos.md` e da Sentinela, nao da
   Fundacao — por isso este achado nao foi escrito la.) */
/* 1.7.0 (04/11/2026) — A FILHA E A MAE DECLARAM A DATA QUE PUBLICAM, pendurada
   no filtro `rodametria_data_da_pagina` da casca (item 2 do despacho da ronda de
   04/11): a filha serve `colhido_em` da sua vitrine, o mesmo campo que a prosa
   imprime como {DATA}; a mae serve a MAIS RECENTE das datas das filhas, porque a
   pergunta que `dateModified` responde e "quando esta pagina mudou", e a mae muda
   no dia em que QUALQUER filha e recolhida. */
if ( ! defined( 'RODAMETRIA_PRODUTO_VERSAO' ) ) {
	define( 'RODAMETRIA_PRODUTO_VERSAO', '1.9.0' );
}

/* A VERSAO DESTE SNIPPET VAI AO AR, pelo filtro que a casca 1.6.0 abriu
 * (`rodametria_casca_versoes()`, e o porque esta escrito la por inteiro).
 *
 * A CHAVE E O `id` DO manifest.json, nao o nome da constante: o portao de ar
 * tem o manifest na mao, e casar por nome de constante o obrigaria a saber que
 * este arquivo abrevia o nome — a derivacao de cabeca que o espelho do manifest
 * se proibe de fazer.
 *
 * E O QUE ESTA LINHA MEDE E A ATIVACAO, nao o byte: se este snippet estiver
 * gravado e NAO ATIVADO (a 20.4, que custou sete paginas na clubedomosaico duas
 * vezes em tres dias), ele nao roda, este filtro nao e pendurado, e o `id`
 * SIMPLESMENTE NAO APARECE no /casca. A ausencia e o sinal. */
add_filter( 'rodametria_versoes', function ( $v ) {
	$v['rodametria-produto'] = RODAMETRIA_PRODUTO_VERSAO;

	return $v;
} );
if ( ! defined( 'RODAMETRIA_PRODUTO_SECAO' ) ) {
	define( 'RODAMETRIA_PRODUTO_SECAO', 'veiculos' );
}
/* Os ids das options que o Sync grava. Eles saem de constante porque a casca
   1.0.0 digitou `f2_respostas` com sublinhado onde o manifest diz `f2-respostas`
   com hifen, e a pagina caiu no estado degradado honesto sem uma linha vermelha
   em lugar nenhum. */
if ( ! defined( 'RODAMETRIA_ID_DADOS_PRODUTO' ) ) {
	define( 'RODAMETRIA_ID_DADOS_PRODUTO', 'paginas-de-produto' );
}
if ( ! defined( 'RODAMETRIA_ID_DADOS_VITRINE' ) ) {
	define( 'RODAMETRIA_ID_DADOS_VITRINE', 'vitrine-de-produto' );
}

/* ---------------------------------------------------------------------------
 * 1. AS DUAS METADES, LIDAS DAS OPTIONS QUE O SYNC GRAVA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_piso' ) ) {
/** O piso da 30.2. Mora numa funcao para a bancada poder cita-lo sem copia-lo. */
function rdm_produto_piso() {
	return 3;
}
}

if ( ! function_exists( 'rdm_produto_editorial' ) ) {
/** A camada declarada: a voz. Sem ela, nenhuma pagina existe. */
function rdm_produto_editorial() {
	static $d = null;
	if ( null !== $d ) {
		return $d;
	}
	$bruto = rodametria_casca_banco( RODAMETRIA_ID_DADOS_PRODUTO );
	$d     = is_array( $bruto ) ? $bruto : array();

	return $d;
}
}

if ( ! function_exists( 'rdm_produto_vitrine' ) ) {
/** A camada gerada: o numero e o link. */
function rdm_produto_vitrine() {
	static $v = null;
	if ( null !== $v ) {
		return $v;
	}
	$bruto = rodametria_casca_banco( RODAMETRIA_ID_DADOS_VITRINE );
	$v     = array();
	if ( is_array( $bruto ) && ! empty( $bruto['paginas'] ) && is_array( $bruto['paginas'] ) ) {
		foreach ( $bruto['paginas'] as $p ) {
			if ( ! empty( $p['id'] ) ) {
				$v[ $p['id'] ] = $p;
			}
		}
	}

	return $v;
}
}

if ( ! function_exists( 'rdm_produto_paginas_prontas' ) ) {
/**
 * As paginas que EXISTEM: tem camada declarada, tem vitrine, e a vitrine passa o
 * piso da 30.2. Esta funcao e a unica porta — menu, arvore, mae, JSON-LD e
 * instalacao saem todos dela, para nao haver duas listas que discordem.
 *
 * Pagina que perde um anuncio na coleta seguinte SAI DO AR em vez de servir uma
 * lista de dois, e `rodametria_casca_link()` faz o link da mae virar texto
 * sozinho, sem 404.
 */
function rdm_produto_paginas_prontas() {
	static $prontas = null;
	if ( null !== $prontas ) {
		return $prontas;
	}
	$ed      = rdm_produto_editorial();
	$vit     = rdm_produto_vitrine();
	$prontas = array();

	if ( empty( $ed['paginas'] ) || ! is_array( $ed['paginas'] ) ) {
		return $prontas;
	}
	foreach ( $ed['paginas'] as $p ) {
		$id = isset( $p['id'] ) ? $p['id'] : '';
		if ( '' === $id || empty( $vit[ $id ]['linhas'] ) ) {
			continue;
		}
		if ( count( $vit[ $id ]['linhas'] ) < rdm_produto_piso() ) {
			continue;
		}
		$slug = isset( $vit[ $id ]['slug'] ) ? $vit[ $id ]['slug'] : '';
		/* O slug da vitrine vem com a secao na frente (`veiculos/patinete-eletrico`)
		   porque e assim que a arvore da 16.1 o escreve; no WordPress o que vale e
		   a ultima parte, e o pai e quem monta o caminho. */
		$pedacos = explode( '/', $slug );
		$prontas[ $id ] = array(
			'id'          => $id,
			'slug'        => (string) end( $pedacos ),
			'declarado'   => $p,
			'vitrine'     => $vit[ $id ],
		);
	}

	return $prontas;
}
}

/* ---------------------------------------------------------------------------
 * 2. OS MOLDES — nenhum numero e digitado na prosa
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_preencher' ) ) {
function rdm_produto_preencher( $texto, $pagina ) {
	$n = $pagina['vitrine']['numeros'];
	$de = array(
		'{N}'                => (string) $n['n'],
		'{DE}'               => (string) $n['de'],
		'{ATE}'              => (string) $n['ate'],
		'{MEDIANA}'          => (string) $n['mediana'],
		'{DECLARAM_WATT}'    => (string) $n['declaram_watt'],
		'{DIZEM_QUAL_WATT}'  => (string) $n['dizem_qual_watt'],
		'{SEM_WATT}'         => (string) $n['sem_watt'],
		'{LIDAS}'            => (string) $n['lidas'],
		'{RECUSADAS}'        => (string) $n['recusadas'],
		'{FRASE_DO_ROTULO}'  => (string) $n['frase_do_rotulo'],
		/* A CARGA MAXIMA DECLARADA NO TITULO — 03/11/2026. A frase e CONTADA no
		   gerador, nunca digitada na camada declarada, e a forma dela muda com o
		   mundo (zero declarando, um so, todos no mesmo numero, faixa de
		   verdade). Ela entrou porque a prosa que estava aqui afirmava o estado
		   do catalogo e a medicao a reprovou: a pagina do patinete dizia que a
		   carga "quase nunca esta no titulo" com SEIS dos DEZESSEIS anuncios
		   dela declarando. Os tres moldes de numero existem para quem quiser
		   escrever a frase de outro jeito; a frase inteira e o molde seguro. */
		'{FRASE_DA_CARGA}'   => (string) $n['frase_da_carga'],
		/* O PIVO DA F1 E O DOBRAVEL — 04/11/2026. A frase do pivo e a contagem
		   mais importante desta ilha e entrou pelo mesmo motivo que a da carga, um
		   grau acima: a camada declarada da pagina da bicicleta afirmava os DOIS
		   lados do pivo — "de pedal assistido" embaixo e "tem acelerador" em cima —
		   com ZERO dos seis anuncios declarando qualquer um dos dois, separando-os
		   por PRECO. A especificacao desta ilha proibe isso no BANCO com todas as
		   letras ("nunca cai no lado 'so pedal assistido' por omissao") e a prosa
		   fazia exatamente isso na TELA, na metade que decide se precisa de CNH. */
		'{FRASE_DO_PIVO}'     => (string) $n['frase_do_pivo'],
		'{FRASE_DO_DOBRAVEL}' => (string) $n['frase_do_dobravel'],
		/* O PAR DE ENTRADA DA F2 — 04/11/2026. Entrou porque a camada declarada
		   desta ilha mandava "olhar a tensao e a amperagem" (instrucao certa) e
		   emendava que bateria pequena em ladeira era "a RECLAMACAO MAIS COMUM de
		   quem compra sem fazer essa conta" — ranqueamento que esta ilha nunca
		   mediu, e que a lista de quantificadores dos portoes nao via porque e um
		   SUPERLATIVO e nao um quantificador. O numero que ela devia dizer: ZERO
		   dos 22 anuncios desta vitrine declara os DOIS no titulo. */
		'{FRASE_DO_PAR_DA_F2}' => (string) $n['frase_do_par_da_f2'],
		'{PAR_DA_F2_OS_DOIS}'  => (string) $n['par_da_f2_os_dois'],
		'{DECLARAM_PIVO}'     => (string) $n['declaram_pivo'],
		'{DOBRAVEIS}'         => (string) $n['dobraveis'],
		'{DECLARAM_CARGA}'   => (string) $n['declaram_carga'],
		'{CARGA_DE}'         => ( null === $n['carga_de'] ) ? '' : (string) $n['carga_de'],
		'{CARGA_ATE}'        => ( null === $n['carga_ate'] ) ? '' : (string) $n['carga_ate'],
		'{CHAVE}'            => (string) $pagina['vitrine']['chave_da_loja'],
		'{DATA}'             => (string) $pagina['vitrine']['colhido_em_br'],
	);

	return str_replace( array_keys( $de ), array_values( $de ), (string) $texto );
}
}

if ( ! function_exists( 'rdm_produto_paragrafos' ) ) {
function rdm_produto_paragrafos( $lista, $pagina, $classe = '' ) {
	$html = '';
	foreach ( (array) $lista as $t ) {
		$html .= '<p' . ( '' !== $classe ? ' class="' . esc_attr( $classe ) . '"' : '' ) . '>'
			. esc_html( rdm_produto_preencher( $t, $pagina ) ) . '</p>';
	}

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3. O MAPA DAS PAGINAS — a secao e as filhas entram pelo filtro da casca
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_paginas', function ( $mapa ) {
	$ed = rdm_produto_editorial();
	if ( ! empty( $ed['mae'] ) ) {
		$mapa[ RODAMETRIA_PRODUTO_SECAO ] = array(
			'nome'        => (string) $ed['mae']['nome'],
			'titulo'      => (string) $ed['mae']['titulo'],
			'tipo'        => 'secao',
			'pai'         => 'inicio',
			'no_menu'     => false,
			'description' => (string) $ed['mae']['description'],
		);
	}
	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		$mapa[ $pagina['slug'] ] = array(
			'nome'        => (string) $pagina['declarado']['h1'],
			'titulo'      => (string) $pagina['declarado']['titulo'],
			'tipo'        => 'produto',
			'pai'         => RODAMETRIA_PRODUTO_SECAO,
			'no_menu'     => true,
			'description' => (string) $pagina['declarado']['description'],
		);
	}

	return $mapa;
}, 20 );

if ( ! function_exists( 'rdm_produto_atual' ) ) {
/** A pagina de produto desta requisicao, ou null. */
function rdm_produto_atual() {
	$slug = rodametria_casca_slug_atual();
	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		if ( $pagina['slug'] === $slug ) {
			return $pagina;
		}
	}

	return null;
}
}

/* ---------------------------------------------------------------------------
 * 4. A TABELA-RESUMO — visivel, e e ela que nomeia TODO anuncio uma vez
 *
 * A secao 7 manda: "TODO ITEM DO BANCO E NOMEADO UMA VEZ EM CADA RESPOSTA". O
 * carrossel leva de 3 a 5 pela 32.1; a tabela leva todos, e e por isso que ela
 * nao e recolhida.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_tabela_html' ) ) {
function rdm_produto_tabela_html( $pagina ) {
	$html  = '<div class="rdm-tabela-rolo"><table class="rdm-tabela">';
	$html .= '<caption>Todos os anúncios que entraram, com o preço do dia da leitura'
		. ' e o que cada um declara</caption>';
	/* A COLUNA DA CARGA ENTROU EM 03/11/2026, e ela fica NA TABELA e nao na
	   primeira tela por uma razao de pixel: a 32.5 poe teto de 1.400 px no
	   primeiro botao de compra, a tabela vive DEPOIS do bloco de compra, e
	   coluna aqui custa ZERO pixel acima dele. A tabela e tambem o que a 32.1
	   chama de "o que as IAs citam", que e onde este numero vale mais. */
	$html .= '<thead><tr><th scope="col">Anúncio</th><th scope="col">Preço</th>'
		. '<th scope="col">O que o anúncio declara</th>'
		. '<th scope="col">Carga máxima no título</th>'
		. '<th scope="col">Loja</th>'
		. '<th scope="col">Comprar</th></tr></thead><tbody>';

	/* O PISO DA 25.2 E DA CONSULTA, NAO DO ANUNCIO, e e por isso que ele aparece
	   UMA VEZ embaixo da tabela em vez de uma vez por linha: a chave que achou
	   todos os anuncios desta pagina e uma so, entao a mesma `url_busca` esta
	   gravada nas 16 linhas da pagina do patinete e nas 5 da bicicleta — medido
	   em 30/10/2026, UMA url distinta por pagina nas duas. Repeti-la por linha
	   seria o mesmo link dezesseis vezes.
	   Se um dia houver mais de uma, a linha NAO sai: escolher "a primeira" seria
	   arbitrario, e o portao desta regra reprova o caso em vez de o maquiar. */
	$buscas = array();
	foreach ( $pagina['vitrine']['linhas'] as $item ) {
		$b = isset( $item['url_busca'] ) ? trim( (string) $item['url_busca'] ) : '';
		if ( '' !== $b ) {
			$buscas[ $b ] = true;
		}
	}

	foreach ( $pagina['vitrine']['linhas'] as $item ) {
		/* A ESCADA DA 25.2 DECIDE AQUI TAMBEM, e nao so no cartao. Antes de
		   30/10/2026 esta celula servia `esc_url( $item['url'] )` cru: no dia em
		   que a ficha morresse, o `href` sairia VAZIO — e `href=""` nao e botao
		   morto, e um botao que recarrega a propria pagina, com o rotulo "Ver na
		   Shopee" do lado. Pior que o cartao do carrossel, que ao menos sumia. */
		$escada = rodametria_casca_escada_de_compra( $item );

		$html .= '<tr>';
		$html .= '<td>' . esc_html( $item['nome'] ) . '</td>';
		$html .= '<td class="rdm-num">' . esc_html( $item['preco'] ) . '</td>';
		$html .= '<td>' . esc_html( $item['especificacao'] ) . '</td>';
		/* A CELULA NUNCA NASCE VAZIA: ou traz o numero que o titulo declara, ou
		   diz que o titulo nao declara. Coluna vazia deixaria o leitor sem saber
		   se ninguem declarou ou se ninguem leu.

		   O `title` LEVA UMA DE DUAS COISAS, E O DADO DIZ QUAL — este comentario
		   dizia "nunca uma frase nossa" e era FALSO nas duas pontas, medido no ar
		   em 10/11/2026 as 16h3xZ: esta celula servia `o titulo nao declara nenhum
		   kg` NOVE vezes nesta pagina e SEIS na da bicicleta (frase nossa, e sem
		   acento), e `suporta ate 150kg` onde o anuncio escreve `Suporta Até
		   150kg` (a normalizacao do pedaco, que nao se acha no anuncio). Comentario
		   que declara um mecanismo parece conferido e nao mede nada (20.7), e
		   nenhum portao desta ilha lia texto de ATRIBUTO.

		   `carga_porque_e_citacao` true  -> pedaco LITERAL do titulo, conferivel
		                                     abrindo o anuncio (secao 24);
		                        false -> frase nossa, na voz do leitor e acentuada.
		   O PHP serve o campo como ele vem: quem garante o conteudo das duas
		   metades e o portao de `gerar-vitrine-de-produto.py`, e quem o confere no
		   ar e a regua de atributo de `conferir-no-ar.py`. */
		$carga = isset( $item['carga'] ) ? (string) $item['carga'] : '';
		$porque = isset( $item['carga_porque'] ) ? (string) $item['carga_porque'] : '';
		$html .= '<td class="rdm-tabela-carga" title="' . esc_attr( $porque ) . '">'
			. esc_html( '' === $carga ? 'o título não declara' : $carga ) . '</td>';
		$html .= '<td>' . esc_html( $item['loja'] ) . '</td>';
		/* O ROTULO SAI DA CASCA, nunca digitado aqui: ela guarda numa funcao so
		   o rotulo por degrau da escada da 25.1, e a secao 8 registra sete
		   reguas que quebraram por procurar o rotulo de UM degrau. O degrau que
		   ela recebe e o RESOLVIDO pela escada, nunca o do dado: quando a busca
		   sobe, o degrau sobe com ela e o rotulo passa a dizer "Ver ofertas". */
		if ( $escada['tem_saida'] ) {
			$html .= '<td><a href="' . esc_url( $escada['url'] ) . '"'
				. ' rel="sponsored noopener" target="_blank">'
				. esc_html( rodametria_casca_rotulo_da_loja(
					$item['programa'], $escada['degrau'] ) ) . '</a></td>';
		} else {
			/* NEM FICHA NEM BUSCA. O anuncio continua NOMEADO na tabela, porque
			   a secao 7 manda todo item ser nomeado uma vez em cada resposta —
			   o que sai e a promessa de compra, nunca o produto. */
			$html .= '<td class="rdm-tabela-sem-saida">sem link de compra hoje</td>';
		}
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div>';
	$html .= '<p class="rdm-tabela-nota">'
		. esc_html( rdm_produto_preencher(
			'Preços lidos em {DATA}. Preço de marketplace muda: o que está aqui é o do dia '
			. 'da leitura, não o de agora.', $pagina ) )
		. '</p>';

	/* A LINHA DISCRETA DO PISO, que esta tabela devia a quem le desde que nasceu:
	   ela serve so a ficha de cada anuncio, e anuncio de marketplace esgota. */
	if ( 1 === count( $buscas ) ) {
		$busca = key( $buscas );
		$html .= '<p class="rdm-tabela-piso"><a href="' . esc_url( $busca ) . '"'
			. ' rel="sponsored noopener" target="_blank">'
			. esc_html( rodametria_casca_rotulo_do_piso() ) . '</a></p>';
	}

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 5. A MALHA — 16.4, e ela e bidirecional e ROTACIONA
 *
 * A 16.9(a) e literal: "cada pagina leva as ate-quatro irmas que vem DEPOIS
 * dela na ordem do mapa, dando a volta no fim". Janela fixa fica verde enquanto
 * a categoria e pequena e deixa a quinta e a sexta filha sem link de entrada
 * nenhum. Com duas filhas, `min(4, irmas)` e UMA, e e isso que sai — e a conta
 * de ENTRADA fecha igual, que e o que a 16.9(b) cobra.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_irmas' ) ) {
function rdm_produto_irmas( $id_atual ) {
	$ordem = array_keys( rdm_produto_paginas_prontas() );
	$onde  = array_search( $id_atual, $ordem, true );
	if ( false === $onde ) {
		return array();
	}
	$total = count( $ordem );
	$fora  = array();
	for ( $i = 1; $i < $total && count( $fora ) < 4; $i++ ) {
		$fora[] = $ordem[ ( $onde + $i ) % $total ];
	}

	return $fora;
}
}

if ( ! function_exists( 'rdm_produto_malha_html' ) ) {
function rdm_produto_malha_html( $pagina ) {
	$prontas = rdm_produto_paginas_prontas();
	$html    = '<nav class="rdm-malha" aria-label="Veja também">';
	$html   .= '<h2>Veja também</h2><ul>';

	foreach ( rdm_produto_irmas( $pagina['id'] ) as $id ) {
		/* A ancora e a CONSULTA da irma, nunca "saiba mais" (16.4c). */
		$link = rodametria_casca_link( $prontas[ $id ]['slug'],
			(string) $prontas[ $id ]['vitrine']['consulta'] );
		if ( '' !== $link ) {
			$html .= '<li>' . $link . '</li>';
		}
	}

	/* 16.4(d): a ferramenta e a pagina que a explica se linkam no corpo. */
	$calc = function_exists( 'rodametria_f2_url' )
		? rodametria_casca_link( 'autonomia-patinete-eletrico',
			'quantos km o elétrico faz de verdade' )
		: '';
	if ( '' !== $calc ) {
		$html .= '<li>' . $calc . '</li>';
	}

	/* A TERCEIRA PERGUNTA DA ILHA, pelo item 1 do despacho de 06/11/2026.
	   A F3 nasceu com ZERO link de miolo apontando para ela — so o menu e o
	   rodape, que a casca serve em toda pagina, e navegacao NAO e cluster: a
	   16.4(f) fala de QUEM APONTA, nao de quantos `href` existem no documento.
	   Estas duas paginas de familia sao justamente onde a pergunta da carga
	   nasce, porque e nelas que a ilha conta, anuncio por anuncio, qual titulo
	   declarou o peso e qual se calou.

	   A ancora e a CONSULTA e nunca "saiba mais" (16.4c), e o link so sai se a
	   PAGINA existir — `rodametria_casca_link()` devolve vazio quando nao
	   existe, que e a trava da secao 16 contra link interno para 404. */
	$carga = rodametria_casca_link( 'peso-maximo-patinete-eletrico',
		'o peso máximo que o elétrico suporta' );
	if ( '' !== $carga ) {
		$html .= '<li>' . $carga . '</li>';
	}

	/* 16.4(b): a filha linka a mae no corpo, e nao so na trilha. */
	$mae = rodametria_casca_link( RODAMETRIA_PRODUTO_SECAO, 'todos os veículos elétricos' );
	if ( '' !== $mae ) {
		$html .= '<li>' . $mae . '</li>';
	}

	$html .= '</ul></nav>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6. A PAGINA DE CONSULTA DE PRODUTO
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_produto_pagina_html' ) ) {
function rdm_produto_pagina_html() {
	$pagina = rdm_produto_atual();

	if ( ! $pagina ) {
		/* Pagina DEGRADADA e honesta. Nunca molde cru, nunca numero inventado. */
		return '<div class="rdm-faixa rdm-pagina">'
			. rodametria_casca_trilha_html()
			. '<h1>Esta página está fora do ar neste momento</h1>'
			. '<p class="rdm-promessa">Os anúncios que ela compara não chegaram nesta '
			. 'atualização. Nenhum preço desta página é estimado, então ela prefere não '
			. 'responder a responder errado.</p>'
			. '</div>';
	}

	$d = $pagina['declarado'];
	$n = $pagina['vitrine']['numeros'];

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>' . esc_html( $d['h1'] ) . '</h1>';

	/* (32.2) A CAIXA DE RESPOSTA NO TOPO: o numero e a condicao em uma frase.
	   O numero e a MEDIANA e nao a faixa, porque numero grande em Mono e um
	   numero so — a faixa inteira vive na frase logo abaixo, onde ela cabe.

	   O ROTULO E O NUMERO SAO DECLARADOS UMA VEZ, AQUI, porque a barra fixa do
	   rodape (32.1, ultima linha) serve O MESMO NUMERO no fim desta funcao —
	   e, pela 20.7, "duas declaracoes do mesmo fato comecam iguais e so uma
	   sobe". Medido no ar as 19h2xZ de 10/11/2026: a barra servia 'Mediano' ao
	   lado de R$ 1.647,95 enquanto esta caixa servia 'Preço mediano hoje' para
	   o MESMO R$ 1.647,95 — adjetivo solto, sem o substantivo que diz mediano
	   de QUE, na superficie que o visitante de telefone le por mais tempo. As
	   outras quatro barras desta ilha ja nasciam certas por construcao (f1 e
	   f2 passam `$rotulo`/`$numero`, a f3 passa `$m['rotulo_precisa']`): esta
	   era a UNICA que escrevia o rotulo a mao uma segunda vez. Quem cobra isso
	   e `ferramentas/teste-barra-de-compra.php`, que exige que toda barra case
	   com uma caixa do mesmo arquivo pela MESMA EXPRESSAO. */
	$rotulo  = 'Preço mediano hoje';
	$numero  = $n['mediana'];
	$unidade = '';

	$html .= rodametria_casca_caixa(
		$rotulo,
		$numero,
		$unidade,
		array_map(
			function ( $t ) use ( $pagina ) {
				return rdm_produto_preencher( $t, $pagina );
			},
			(array) $d['resposta'] ),
		'verde' );

	/* (32.2) O BLOCO DE COMPRA logo abaixo da resposta, com `id="comprar"`. */
	$html .= rodametria_casca_bloco_de_compra(
		'À venda agora',
		$pagina['vitrine']['cartoes'],
		rdm_produto_preencher(
			'Os {N} anúncios abaixo foram lidos em {DATA} na busca por "{CHAVE}". '
			. 'A ordem é por venda medida e depois por preço.', $pagina ),
		'Nenhum anúncio desta família passou pela nossa conferência nesta leitura.' );

	/* (32.2) A TABELA-RESUMO VISIVEL — e o que as IAs citam. */
	$html .= '<h2>Todos os anúncios que entraram</h2>';
	$html .= rdm_produto_tabela_html( $pagina );

	/* A PRESTACAO DE CONTAS DA SECAO 7: quem NAO entrou, e por que. A frase e
	   CONTADA da propria vitrine, nunca digitada. */
	$html .= rdm_produto_recusas_html( $pagina );

	/* A malha fica VISIVEL e fora de dobra: ela e alvo de link e nem todo
	   navegador abre um `<details>` fechado ao pular para dentro dele. */
	$html .= rdm_produto_malha_html( $pagina );

	/* (32.2) O RESTO DO TEXTO NAS DOBRAS — e pela 32.3 e pela 22.8 ele continua
	   inteiro no HTML servido, legivel com o JavaScript desligado. */
	$html .= rodametria_casca_dobra( 'O que é, e o que não é',
		rdm_produto_paragrafos( $d['o_que_e'], $pagina )
		. rdm_produto_paragrafos( $d['o_que_nao_e'], $pagina ) );

	$escolher = '<dl class="rdm-escolher">';
	foreach ( (array) $d['qual_escolher'] as $caso ) {
		$escolher .= '<dt>' . esc_html( rdm_produto_preencher( $caso['para'], $pagina ) ) . '</dt>';
		$escolher .= '<dd>' . esc_html( rdm_produto_preencher( $caso['o_que_olhar'], $pagina ) ) . '</dd>';
	}
	$escolher .= '</dl>';
	$html .= rodametria_casca_dobra( 'Qual escolher, pelo seu uso', $escolher );

	$faq = '';
	foreach ( (array) $d['perguntas'] as $q ) {
		$faq .= '<h3>' . esc_html( rdm_produto_preencher( $q['pergunta'], $pagina ) ) . '</h3>';
		$faq .= '<p>' . esc_html( rdm_produto_preencher( $q['resposta'], $pagina ) ) . '</p>';
	}
	$html .= rodametria_casca_dobra( 'Perguntas frequentes', $faq );

	$html .= rodametria_casca_dobra( 'Como sabemos',
		rdm_produto_paragrafos( $d['como_sabemos'], $pagina )
		. '<p>' . esc_html( (string) $d['aviso_de_afiliado'] ) . '</p>' );

	$html .= '</div>';

	/* (32.1, ultima linha) A barra fixa do telefone com o numero e o botao.
	   O rotulo, o numero e a unidade sao os DA CAIXA, pela MESMA expressao
	   (20.7): a barra repete o numero da resposta, entao repete o rotulo dela. */
	$html .= rodametria_casca_barra_fixa( $rotulo, $numero, $unidade,
		(array) $pagina['vitrine']['cartoes'] );

	return $html;
}
}

if ( ! function_exists( 'rdm_produto_recusas_html' ) ) {
/**
 * O QUE A LOJA DEVOLVEU E NAO ENTROU, com a causa CONTADA.
 *
 * A secao 7 manda nomear quem nao entrou e proibe oferecer hipotese: "a recusa
 * nomeia a causa que a pagina MEDIU". Aqui a causa de cada recusa esta gravada
 * no anuncio, e esta funcao so a traduz para portugues de leitor.
 */
function rdm_produto_recusas_html( $pagina ) {
	$n = $pagina['vitrine']['numeros'];
	if ( empty( $n['recusadas'] ) ) {
		return '';
	}
	$nomes = array(
		'acessorio'       => 'acessório (capacete, capa de chuva, pneu, buzina)',
		'brinquedo'       => 'veículo de criança',
		'outro_veiculo'   => 'outro tipo de veículo (triciclo, quadriciclo, hoverboard)',
		'kit_multiplo'    => 'kit com mais de uma unidade',
		'fora_da_familia' => 'outra família de produto',
		'sem_qualificador' => 'anúncio que não diz ser de adulto',
	);
	$pedacos = array();
	foreach ( (array) $n['recusas_por_causa'] as $causa => $quantos ) {
		$rotulo    = isset( $nomes[ $causa ] ) ? $nomes[ $causa ] : $causa;
		$pedacos[] = $quantos . ' ' . $rotulo;
	}

	return '<p class="rdm-recusas">'
		. esc_html( sprintf(
			'A mesma busca devolveu %d ofertas, e %d ficaram de fora: %s. '
			. 'Elas não estão na tabela porque não são o produto desta página.',
			(int) $n['lidas'], (int) $n['recusadas'], implode( ' · ', $pedacos ) ) )
		. '</p>';
}
}

add_shortcode( 'rodametria_produto', 'rdm_produto_pagina_html' );

/* ---------------------------------------------------------------------------
 * 7. A SECAO MAE — 16.4(a): ela lista TODAS as filhas, com a consulta de ancora
 * ------------------------------------------------------------------------- */

/**
 * O AGREGADO DAS FILHAS PRONTAS, e ele e FUNCAO PURA sobre a lista.
 *
 * A mae nao tem consulta propria: o numero dela e a soma das filhas, e a faixa
 * de preco vai do MENOR `de` de todas ao MAIOR `ate` de todas — comparados pelo
 * campo numerico da vitrine (`de_numero`/`ate_numero`), nunca pela string com
 * `R$` e virgula, que ordena por texto e poe `R$ 6.199,90` antes de
 * `R$ 1.297,13` sem reclamar. A string formatada que sai e a do registro que
 * ganhou a comparacao, nunca remontada aqui.
 *
 * As DATAS saem como lista de distintas, e nao como "a data": duas filhas lidas
 * em dias diferentes nao tem uma data, e a frase que escolher uma delas mente
 * sobre a outra. E a mesma pedra da linha do piso na tabela da filha — "com
 * duas buscas distintas a linha NAO sai, porque a primeira e arbitraria".
 */
if ( ! function_exists( 'rdm_produto_agregado_das_prontas' ) ) {
function rdm_produto_agregado_das_prontas( $prontas ) {
	$ag = array(
		'familias' => 0,
		'anuncios' => 0,
		'de'       => '',
		'ate'      => '',
		'datas'    => array(),
		/* A CARGA AGREGADA — 04/11/2026. A mae tinha, escrita a mao, a frase que
		   a execucao de 03/11 aposentou da pagina do patinete: "o filtro que
		   quase ninguem olha e que QUASE NUNCA ESTA NO TITULO". Ela sobreviveu um
		   dia inteiro no ar aqui porque o conserto foi feito na pagina onde o
		   defeito foi ACHADO, e esta pagina e outra familia — a 32.5-c um andar
		   acima do CSS. O numero dela e a soma das filhas, contado aqui. */
		'carga_declaram' => 0,
		'carga_de'       => null,
		'carga_ate'      => null,
	);
	$de_num  = null;
	$ate_num = null;

	foreach ( (array) $prontas as $p ) {
		$n = ( isset( $p['vitrine']['numeros'] ) && is_array( $p['vitrine']['numeros'] ) )
			? $p['vitrine']['numeros'] : array();

		$ag['familias']++;
		$ag['anuncios'] += isset( $n['n'] ) ? (int) $n['n'] : 0;

		$ag['carga_declaram'] += isset( $n['declaram_carga'] ) ? (int) $n['declaram_carga'] : 0;
		if ( isset( $n['carga_de'] ) && null !== $n['carga_de']
			&& ( null === $ag['carga_de'] || (int) $n['carga_de'] < $ag['carga_de'] ) ) {
			$ag['carga_de'] = (int) $n['carga_de'];
		}
		if ( isset( $n['carga_ate'] ) && null !== $n['carga_ate']
			&& ( null === $ag['carga_ate'] || (int) $n['carga_ate'] > $ag['carga_ate'] ) ) {
			$ag['carga_ate'] = (int) $n['carga_ate'];
		}

		if ( isset( $n['de_numero'], $n['de'] )
			&& ( null === $de_num || (float) $n['de_numero'] < $de_num ) ) {
			$de_num   = (float) $n['de_numero'];
			$ag['de'] = (string) $n['de'];
		}
		if ( isset( $n['ate_numero'], $n['ate'] )
			&& ( null === $ate_num || (float) $n['ate_numero'] > $ate_num ) ) {
			$ate_num   = (float) $n['ate_numero'];
			$ag['ate'] = (string) $n['ate'];
		}

		$data = isset( $p['vitrine']['colhido_em_br'] ) ? (string) $p['vitrine']['colhido_em_br'] : '';
		if ( '' !== $data && ! in_array( $data, $ag['datas'], true ) ) {
			$ag['datas'][] = $data;
		}
	}

	return $ag;
}
}

/**
 * AS FRASES DA CAIXA DA MAE — UMA FRASE POR MUNDO, escolhida aqui e escrita no
 * `dados/paginas-de-produto.json`.
 *
 * POR QUE FUNCAO PURA, e a secao 8 escreveu o motivo com todas as letras: "toda
 * recusa que depende de uma relacao entre os dados — empate, ausencia, borda,
 * limite — mora numa funcao pura que recebe a relacao JA CALCULADA; recusa
 * escrita dentro do laco que a calcula so e testavel no dia em que o banco
 * produzir o caso, e e esse o dia em que ela vai estar errada". Hoje esta ilha
 * tem DUAS familias prontas, as duas lidas no MESMO dia, e TRES que faltam: de
 * sete mundos possiveis o dado exercita um. `teste-caixa-da-mae.php` fabrica os
 * outros seis.
 *
 * E a frase do que falta SO SAI quando falta algo, pelo mesmo motivo que o
 * gerador da vitrine ja cobra na frase do rotulo de potencia: "imprime zero no
 * meio da frase" e falha nomeada naquele portao.
 */
/**
 * A FRASE DA CARGA AGREGADA DA SECAO MAE — UMA FRASE POR MUNDO (04/11/2026).
 *
 * POR QUE ELA EXISTE, e a causa e a mais instrutiva desta ilha: a execucao de
 * 03/11 achou, na pagina do patinete, a frase declarada *"a carga maxima (...)
 * QUASE NUNCA ESTA NO TITULO"* com SEIS dos DEZESSEIS anuncios daquela pagina
 * declarando, e a trocou por uma contagem. **A MESMA AFIRMACAO VIVIA AQUI**, no
 * `o_que_decide` da mae — *"o filtro que quase ninguem olha e que quase nunca
 * esta no titulo"* — e sobreviveu o dia inteiro no ar, porque o conserto foi
 * feito na pagina onde o defeito foi ACHADO. E a 32.5-c um andar acima do CSS: a
 * metade que aprendeu nao contou a irma. O portao escrito no mesmo dia para
 * impedir o retorno da frase tambem nao a pegou, porque ele varria as paginas de
 * FILHA e a mae nao e uma delas.
 *
 * FUNCAO PURA sobre a relacao ja calculada, pelo mesmo motivo da irma de baixo: o
 * mundo "todos declaram" e o mundo "todos no mesmo numero" nao existem no dado de
 * hoje, e recusa escrita dentro do laco que a calcula so e testavel no dia em que
 * o banco produzir o caso — que e o dia em que ela vai estar errada.
 *
 * E ELA E AGREGADA DE PROPOSITO: a mae nao tem anuncio proprio. O numero dela e a
 * soma das filhas publicadas, e a faixa e o menor e o maior entre todas — nunca a
 * faixa de uma familia servida como se fosse da secao.
 */
if ( ! function_exists( 'rdm_produto_frase_da_carga_agregada' ) ) {
function rdm_produto_frase_da_carga_agregada( $ag, $moldes ) {
	$n        = isset( $ag['anuncios'] ) ? (int) $ag['anuncios'] : 0;
	$declaram = isset( $ag['carga_declaram'] ) ? (int) $ag['carga_declaram'] : 0;
	$de       = ( isset( $ag['carga_de'] ) && null !== $ag['carga_de'] ) ? (int) $ag['carga_de'] : null;
	$ate      = ( isset( $ag['carga_ate'] ) && null !== $ag['carga_ate'] ) ? (int) $ag['carga_ate'] : null;

	if ( 0 === $declaram || null === $de || null === $ate ) {
		/* O RAMO DO ZERO VEM PRIMEIRO E COBRE TAMBEM A FAIXA AUSENTE: sem ele a
		   frase sairia com "de  a  kg" na tela, que e pior que numero velho
		   porque nao parece defeito de dado, parece defeito de texto. */
		$molde = isset( $moldes['nenhum'] ) ? $moldes['nenhum'] : '';
	} elseif ( $de === $ate ) {
		/* TODOS NO MESMO NUMERO. Sem este ramo a frase diria "de 60 a 60 kg". */
		$molde = ( 1 === $declaram )
			? ( isset( $moldes['um'] ) ? $moldes['um'] : '' )
			: ( isset( $moldes['mesmo_valor'] ) ? $moldes['mesmo_valor'] : '' );
	} elseif ( $declaram === $n ) {
		$molde = isset( $moldes['todos'] ) ? $moldes['todos'] : '';
	} else {
		$molde = isset( $moldes['faixa'] ) ? $moldes['faixa'] : '';
	}

	return str_replace(
		array( '{N}', '{DECLARAM}', '{CARGA_DE}', '{CARGA_ATE}' ),
		array( (string) $n, (string) $declaram,
			( null === $de ) ? '' : (string) $de,
			( null === $ate ) ? '' : (string) $ate ),
		(string) $molde );
}
}

if ( ! function_exists( 'rdm_produto_caixa_frases' ) ) {
function rdm_produto_caixa_frases( $ag, $faltam, $moldes ) {
	$familias = isset( $ag['familias'] ) ? (int) $ag['familias'] : 0;
	$datas    = ( isset( $ag['datas'] ) && is_array( $ag['datas'] ) ) ? $ag['datas'] : array();
	$faltam   = (int) $faltam;
	$frases   = array();

	$tem_faixa = ( '' !== (string) $ag['de'] && '' !== (string) $ag['ate'] );

	if ( 0 === $familias ) {
		$frases[] = isset( $moldes['escopo_nenhuma'] ) ? $moldes['escopo_nenhuma'] : '';
	} elseif ( ! $tem_faixa ) {
		/* FAMILIA PRONTA SEM FAIXA DE PRECO. Sem este ramo a frase sairia com
		   "de  a ." na tela — buraco no lugar do numero, que e pior que numero
		   velho porque nao parece defeito de dado, parece defeito de texto.
		   E ELE TAMBEM TEM SINGULAR: a primeira versao deste ramo nao tinha, e o
		   portao o pegou no minuto em que nasceu, servindo "nas 1 familias" —
		   o MESMO plural que mente que o ramo com faixa ja pagava ao lado. */
		$chave    = ( 1 === $familias ) ? 'escopo_sem_faixa_uma' : 'escopo_sem_faixa';
		$frases[] = isset( $moldes[ $chave ] ) ? $moldes[ $chave ] : '';
	} elseif ( 1 === $familias ) {
		$frases[] = isset( $moldes['escopo_uma'] ) ? $moldes['escopo_uma'] : '';
	} else {
		$frases[] = isset( $moldes['escopo_muitas'] ) ? $moldes['escopo_muitas'] : '';
	}

	if ( $familias > 0 && 1 === count( $datas ) ) {
		$frases[] = isset( $moldes['data_igual'] ) ? $moldes['data_igual'] : '';
	} elseif ( $familias > 0 && count( $datas ) > 1 ) {
		$frases[] = isset( $moldes['data_divergente'] ) ? $moldes['data_divergente'] : '';
	}

	if ( $faltam > 0 ) {
		$frases[] = ( 1 === $faltam && isset( $moldes['falta_uma'] ) )
			? $moldes['falta_uma']
			: ( isset( $moldes['faltam'] ) ? $moldes['faltam'] : '' );
	}

	$troca = array(
		'{N}'      => (string) ( isset( $ag['anuncios'] ) ? (int) $ag['anuncios'] : 0 ),
		'{NO_AR}'  => (string) $familias,
		'{FALTAM}' => (string) $faltam,
		'{DE}'     => (string) $ag['de'],
		'{ATE}'    => (string) $ag['ate'],
		'{DATA}'   => ( 1 === count( $datas ) ) ? (string) $datas[0] : '',
	);

	$saida = array();
	foreach ( $frases as $f ) {
		$f = str_replace( array_keys( $troca ), array_values( $troca ), (string) $f );
		if ( '' !== trim( $f ) ) {
			$saida[] = $f;
		}
	}

	return $saida;
}
}

if ( ! function_exists( 'rdm_produto_mae_html' ) ) {
function rdm_produto_mae_html() {
	$ed = rdm_produto_editorial();
	if ( empty( $ed['mae'] ) ) {
		return '<div class="rdm-faixa rdm-pagina">' . rodametria_casca_trilha_html()
			. '<h1>Veículos elétricos</h1>'
			. '<p class="rdm-promessa">Esta seção está fora do ar neste momento.</p></div>';
	}
	$mae     = $ed['mae'];
	$prontas = rdm_produto_paginas_prontas();
	/* 16.5: as familias que a mae nomeia e ainda nao tem pagina. SOBIU para ca
	   em 02/11/2026 porque a caixa de resposta as CONTA, e a lista continua
	   servindo os cartoes mudos mais abaixo — uma leitura, dois usos. */
	$faltam  = rdm_produto_familias_que_faltam();

	$html  = '<div class="rdm-faixa rdm-pagina">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>' . esc_html( $mae['h1'] ) . '</h1>';
	foreach ( (array) $mae['resposta'] as $t ) {
		$html .= '<p class="rdm-promessa">' . esc_html( $t ) . '</p>';
	}

	/* (32.2) A CAIXA DE RESPOSTA NO TOPO, E ELA FALTAVA DESDE QUE A SECAO NASCEU.
	   O portao de pixel desta ilha dizia isso com essas palavras — "sem
	   componente de molde nenhum" —, e a consequencia nao era feia: era que os
	   700 px da 32.5 NUNCA JULGARAM esta pagina. Ela servia
	   `<p class="rdm-promessa">` onde o molde pede a caixa, entao o portao a
	   listava FORA DO MOLDE e ia embora. E a 32.5-c em estado puro: a familia de
	   pagina que entra depois nao herda a regra por intencao, so por seletor.

	   O NUMERO E AGREGADO DAS FILHAS, contado na hora de servir, e a prosa sai
	   da camada declarada com moldes. Pagina que fala do estado do banco e
	   justamente onde numero digitado passa a mentir calado (secao 8). */
	$caixa = ( isset( $mae['caixa'] ) && is_array( $mae['caixa'] ) ) ? $mae['caixa'] : array();
	/* UMA LEITURA, DOIS USOS: o agregado sai do laco das filhas uma vez e serve a
	   caixa de resposta E a frase da carga do `o_que_decide`. Calcula-lo duas
	   vezes abriria a porta para as duas metades divergirem, que e a 32.5-c. */
	$ag = rdm_produto_agregado_das_prontas( $prontas );
	if ( $caixa ) {
		$html .= rodametria_casca_caixa(
			isset( $caixa['rotulo'] ) ? (string) $caixa['rotulo'] : '',
			(string) (int) $ag['anuncios'],
			isset( $caixa['unidade'] ) ? (string) $caixa['unidade'] : '',
			rdm_produto_caixa_frases( $ag, count( $faltam ), $caixa ),
			'neutro' );
	}

	$html .= '<ul class="rdm-cartoes">';
	foreach ( $prontas as $pagina ) {
		$n    = $pagina['vitrine']['numeros'];
		$link = rodametria_casca_link( $pagina['slug'],
			(string) $pagina['vitrine']['consulta'] );
		if ( '' === $link ) {
			continue;
		}
		$html .= '<li class="rdm-cartao"><h2>' . $link . '</h2>'
			. '<p>' . esc_html( sprintf(
				'%d anúncios de adulto à venda, de %s a %s.',
				(int) $n['n'], (string) $n['de'], (string) $n['ate'] ) ) . '</p>';

		/* (32.2) O SEGUNDO BOTAO DO CARTAO: "Ver produtos" da secao, e ele cai no
		   BLOCO DE COMPRA da filha (`id="comprar"`), nao no topo dela. O titulo
		   do cartao continua levando a pagina inteira — o link de cima nao muda
		   um byte, porque a 32.3 protege ancora e link interno.

		   O SEGUNDO BOTAO DA 32.2 SERIA "Calcular", e ELE NAO SAI AQUI, com o
		   motivo escrito para a proxima execucao nao o "consertar": a 32.2 pede
		   a ferramenta "com o parametro da pagina ja passado na URL", e a F2
		   desta ilha recebe tensao e amperagem de BATERIA — familia de veiculo
		   nao e parametro dela. Botao por familia seria o MESMO link duas vezes,
		   a mesma pedra que a linha do piso da tabela ja paga ("repeti-la seria o
		   mesmo link dezesseis vezes"). A conta de bateria continua linkada UMA
		   vez, mais abaixo, na frase que ja existia. */
		$url_filha = rodametria_casca_url_do_slug( $pagina['slug'] );
		$rotulo    = isset( $mae['rotulo_do_botao_da_filha'] )
			? (string) $mae['rotulo_do_botao_da_filha'] : '';
		if ( '' !== $url_filha && '' !== $rotulo ) {
			$html .= '<p><a class="rdm-molde-cartao-botao" href="'
				. esc_url( $url_filha . '#comprar' ) . '">'
				. esc_html( $rotulo ) . '</a></p>';
		}

		$html .= '</li>';
	}

	/* 16.5, e a nota dela: o cartao da pagina que ainda nao nasceu NAO e link, e
	   a frase diz a CAUSA medida em vez de prometer data. "Em breve" de
	   categoria nao e a frase proibida pela secao 7 — aquela e "link de loja em
	   breve", dentro do bloco de compra, e nao existe aqui. */
	if ( $faltam ) {
		$html .= '<li class="rdm-cartao rdm-cartao-mudo"><h2>Ainda não nasceram</h2><ul>';
		foreach ( $faltam as $f ) {
			$html .= '<li><strong>' . esc_html( $f['consulta'] ) . '</strong> — '
				. esc_html( $f['causa'] ) . '</li>';
		}
		$html .= '</ul></li>';
	}
	$html .= '</ul>';

	if ( ! empty( $mae['o_que_falta_dizer'] ) ) {
		$html .= '<p>' . esc_html( (string) $mae['o_que_falta_dizer'] ) . '</p>';
	}

	/* OS TRES NUMEROS. Eles nao sao enchimento de pagina: sao o produto desta
	   casa, escritos na secao que lista as familias porque e ali que a pessoa
	   decide qual familia olhar. Entraram depois de a conta do corpo medir
	   1.253 caracteres contra o piso de 1.500 que a secao 8 cobra de pagina de
	   dominio novo — e o conserto de pagina fina nunca e texto a mais, e o
	   texto que faltava. */
	if ( ! empty( $mae['o_que_decide'] ) ) {
		$html .= '<h2>' . esc_html( (string) $mae['o_que_decide_rotulo'] ) . '</h2>';
		$html .= '<dl class="rdm-escolher">';
		$moldes_carga = ( isset( $mae['carga'] ) && is_array( $mae['carga'] ) )
			? $mae['carga'] : array();
		$frase_carga  = rdm_produto_frase_da_carga_agregada( $ag, $moldes_carga );
		foreach ( (array) $mae['o_que_decide'] as $item ) {
			/* O PREENCHEDOR DA MAE — 04/11/2026. Este laco servia a prosa CRUA, e
			   era por isso que a afirmacao da carga estava escrita a mao aqui: nao
			   havia por onde um molde entrar. Molde cru na tela e reprovado pelo
			   `conferir-produto-no-ar.py`, que ja varre `{...}` nesta pagina. */
			$porque = str_replace( '{FRASE_DA_CARGA_AGREGADA}', $frase_carga,
				(string) $item['porque'] );
			$html .= '<dt>' . esc_html( $item['numero'] ) . '</dt>';
			$html .= '<dd>' . esc_html( $porque ) . '</dd>';
		}
		$html .= '</dl>';
	}

	$calc = rodametria_casca_link( 'autonomia-patinete-eletrico',
		'quantos km o elétrico faz de verdade' );
	if ( '' !== $calc ) {
		$html .= '<p>Antes de fechar a compra, faça a conta de bateria: ' . $calc . '.</p>';
	}

	if ( ! empty( $mae['como_sabemos'] ) ) {
		$corpo = '';
		foreach ( (array) $mae['como_sabemos'] as $t ) {
			$corpo .= '<p>' . esc_html( $t ) . '</p>';
		}
		$html .= rodametria_casca_dobra( 'Como sabemos', $corpo );
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'rdm_produto_familias_que_faltam' ) ) {
/**
 * As familias que a mae nomeia e que ainda nao tem pagina, com a causa CURTA.
 *
 * A causa longa e medida mora em `dados/consultas-de-produto.json`, que NAO vai
 * para o site (`publicar: false`): ela e cheia de vocabulario de bastidor que a
 * 32.4 proibe na pagina publica. O que vai para a tela e a frase de leitor, e
 * ela mora na camada declarada ao lado da familia.
 */
function rdm_produto_familias_que_faltam() {
	$ed = rdm_produto_editorial();

	return ( ! empty( $ed['mae']['familias_que_faltam'] ) && is_array( $ed['mae']['familias_que_faltam'] ) )
		? $ed['mae']['familias_que_faltam'] : array();
}
}

add_shortcode( 'rodametria_veiculos', 'rdm_produto_mae_html' );

/* ---------------------------------------------------------------------------
 * A DATA QUE ESTAS PAGINAS PUBLICAM, pendurada no filtro da casca (item 2 do
 * despacho de 04/11/2026). O mecanismo e o comentario estao em
 * `rodametria_casca_data_da_pagina()`; aqui fica so o que e DESTE snippet.
 *
 * A FILHA: `colhido_em` da sua propria vitrine — o MESMO campo que a prosa
 * imprime como {DATA} em `colhido_em_br` ("os 16 anuncios que a gente conferiu
 * em 04/11/2026"). Um fato, uma fonte (20.7).
 *
 * A MAE: a MAIS RECENTE das datas das filhas, e nao a unica. A caixa dela ja
 * trata os dois mundos — `data_igual` quando as filhas foram lidas no mesmo dia
 * e `data_divergente` quando nao — e `dateModified` nao tem dois mundos: a
 * pergunta que ele responde e "quando esta pagina mudou pela ultima vez", e a
 * mae muda no dia em que QUALQUER filha e recolhida. Com datas divergentes, a
 * mais antiga seria falsa.
 * ------------------------------------------------------------------------- */
add_filter( 'rodametria_data_da_pagina', function ( $data, $slug ) {
	if ( '' !== $data ) {
		return $data;
	}
	$prontas = rdm_produto_paginas_prontas();

	foreach ( $prontas as $pagina ) {
		if ( $pagina['slug'] === $slug && ! empty( $pagina['vitrine']['colhido_em'] ) ) {
			return (string) $pagina['vitrine']['colhido_em'];
		}
	}

	if ( RODAMETRIA_PRODUTO_SECAO === $slug ) {
		$datas = array();
		foreach ( $prontas as $pagina ) {
			if ( ! empty( $pagina['vitrine']['colhido_em'] ) ) {
				$datas[] = (string) $pagina['vitrine']['colhido_em'];
			}
		}
		if ( $datas ) {
			sort( $datas );          /* AAAA-MM-DD ordena como texto */
			return (string) end( $datas );
		}
	}

	return $data;
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * 8. JSON-LD — ItemList na pagina de produto (30.3) e FAQPage onde ha pergunta
 *
 * O BreadcrumbList nao se repete aqui: ele e da casca.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$pagina = rdm_produto_atual();
	if ( ! $pagina ) {
		return;
	}
	$d = $pagina['declarado'];

	$itens = array();
	foreach ( $pagina['vitrine']['linhas'] as $i => $item ) {
		/* O TERCEIRO LUGAR QUE LIA A `url` CRUA, e o mais silencioso dos tres:
		   com a ficha morta, a `Offer` saia com `"url": ""` — dado estruturado
		   invalido que nenhum olho humano ve na pagina. */
		$escada = rodametria_casca_escada_de_compra( $item );

		$oferta = array(
			'@type'         => 'Offer',
			'price'         => number_format( (float) $item['preco_numero'], 2, '.', '' ),
			'priceCurrency' => 'BRL',
		);
		if ( $escada['tem_saida'] ) {
			$oferta['url'] = $escada['url'];
		}
		/* `InStock` E UMA AFIRMACAO, E ELA SO VALE SOBRE UMA FICHA. Quando o piso
		   sobe, a url da oferta e uma PAGINA DE BUSCA: dizer que um resultado de
		   busca esta em estoque e afirmar o que ninguem mediu, e a secao 7 desta
		   fabrica nao deixa. Sem o campo, o buscador nao recebe promessa nenhuma
		   — que e a verdade daquele momento. */
		if ( ! $escada['piso_subiu'] ) {
			$oferta['availability'] = 'https://schema.org/InStock';
		}

		$produto = array(
			'@type'  => 'Product',
			'name'   => $item['nome'],
			'offers' => $oferta,
		);
		if ( ! empty( $item['imagem']['url'] ) ) {
			$produto['image'] = $item['imagem']['url'];
		}
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $i + 1,
			'item'     => $produto,
		);
	}

	$lista = array(
		'@context'        => 'https://schema.org',
		'@type'           => 'ItemList',
		'name'            => $d['h1'],
		'description'     => $d['description'],
		'numberOfItems'   => count( $itens ),
		'itemListElement' => $itens,
	);

	$perguntas = array();
	foreach ( (array) $d['perguntas'] as $q ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => rdm_produto_preencher( $q['pergunta'], $pagina ),
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => rdm_produto_preencher( $q['resposta'], $pagina ),
			),
		);
	}
	$faq = array(
		'@context'   => 'https://schema.org',
		'@type'      => 'FAQPage',
		'mainEntity' => $perguntas,
	);

	$opcoes = JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE;
	echo '<script type="application/ld+json">' . wp_json_encode( $lista, $opcoes ) . "</script>\n";
	if ( $perguntas ) {
		echo '<script type="application/ld+json">' . wp_json_encode( $faq, $opcoes ) . "</script>\n";
	}
}, 20 );

/* ---------------------------------------------------------------------------
 * 9. A FOLHA — no rodape, nunca dentro do shortcode (secao 8)
 *
 * Ela redecora o MINIMO: os componentes do molde sao da casca, e a 32.5-c
 * aprendeu no Clube do Mosaico que folha de snippet que redecora a caixa do
 * molde vence por ordem de carga e desfaz a regra de telefone. Daqui so saem as
 * classes que SO existem nesta familia de pagina.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! rdm_produto_atual() && ! is_page( RODAMETRIA_PRODUTO_SECAO ) ) {
		return;
	}
	?>
<?php rodametria_casca_abrir_folha(); ?>
body.rdm .rdm-tabela-rolo{overflow-x:auto;-webkit-overflow-scrolling:touch}
body.rdm .rdm-tabela-nota,body.rdm .rdm-recusas{font-size:.9rem;color:var(--rdm-legenda)}
/* A CELULA SEM SAIDA e a LINHA DO PISO, as duas de 30/10/2026. A celula nao e
   alerta: e ausencia, e cor de alerta aqui gritaria sobre o que o leitor nao
   pode resolver. A linha do piso copia a `.rdm-molde-cartao-todos` da casca de
   proposito — e a MESMA frase no mesmo papel, uma vez por pagina em vez de uma
   por cartao, porque o piso e da consulta e nao do anuncio. */
body.rdm .rdm-tabela-sem-saida{color:var(--rdm-legenda);font-size:.875rem}
body.rdm .rdm-tabela-piso{margin:0 0 var(--rdm-e4);font-size:.9rem}
body.rdm .rdm-tabela-piso a{color:var(--rdm-legenda);text-decoration:underline}
body.rdm .rdm-escolher{margin:0}
body.rdm .rdm-escolher dt{font-family:"Barlow Semi Condensed",Barlow,sans-serif;font-weight:700;margin-top:1rem}
body.rdm .rdm-escolher dd{margin:.25rem 0 0}
body.rdm .rdm-malha{margin:2rem 0}
body.rdm .rdm-malha ul{list-style:none;padding:0;margin:0}
body.rdm .rdm-malha li{padding:.5rem 0;border-top:1px solid var(--rdm-traco)}
body.rdm .rdm-cartoes{list-style:none;padding:0;margin:1.5rem 0;display:grid;gap:1rem}
body.rdm .rdm-cartao{border:1px solid var(--rdm-traco);background:var(--rdm-superficie);padding:1rem}
body.rdm .rdm-cartao h2{margin:0 0 .5rem;font-size:1.15rem}
body.rdm .rdm-cartao p{margin:0}
body.rdm .rdm-cartao-mudo ul{margin:.5rem 0 0;padding-left:1.1rem}
body.rdm .rdm-cartao-mudo li{padding:.25rem 0}
@media (min-width:52rem){body.rdm .rdm-cartoes{grid-template-columns:repeat(2,minmax(0,1fr))}}
<?php rodametria_casca_fechar_folha( 'rodametria-produto-css' ); ?>
	<?php
}, 30 );

/* ---------------------------------------------------------------------------
 * 10. INSTALACAO — pelo gancho da casca, nunca em toda requisicao
 *
 * A mae nasce primeiro: o pai tem de existir antes da filha, senao a 16.2
 * ("pagina sem pai e defeito e nao publica") e a trilha da 16.3 saem erradas.
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_instalar', function ( $relato ) {
	$ed = rdm_produto_editorial();
	if ( empty( $ed['mae'] ) ) {
		$relato[] = 'produto: ERRO — a camada declarada nao chegou';

		return $relato;
	}

	$mae = rodametria_casca_garantir_pagina(
		RODAMETRIA_PRODUTO_SECAO,
		(string) $ed['mae']['titulo'],
		'[rodametria_veiculos]' );

	if ( empty( $mae['id'] ) ) {
		$relato[] = 'veiculos: ERRO — ' . ( isset( $mae['erro'] ) ? $mae['erro'] : 'sem id' );

		return $relato;
	}
	$relato[] = 'veiculos: #' . $mae['id'] . ' (' . $mae['slug'] . ')'
		. ( empty( $mae['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );

	foreach ( rdm_produto_paginas_prontas() as $pagina ) {
		$p = rodametria_casca_garantir_pagina(
			$pagina['slug'],
			(string) $pagina['declarado']['titulo'],
			'[rodametria_produto]',
			(int) $mae['id'] );
		if ( empty( $p['id'] ) ) {
			$relato[] = 'produto/' . $pagina['slug'] . ': ERRO — '
				. ( isset( $p['erro'] ) ? $p['erro'] : 'sem id' );
			continue;
		}
		$relato[] = 'produto/' . $pagina['slug'] . ': #' . $p['id'] . ' (' . $p['slug'] . ')'
			. ( empty( $p['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );
	}

	return $relato;
}, 20 );

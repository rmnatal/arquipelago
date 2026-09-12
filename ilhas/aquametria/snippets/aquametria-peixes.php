/**
 * Aquametria Peixes — a malha do eixo /peixes/
 * Versão: 1.2.0 (12/09/2026)
 *
 * T4 do PROMPT.md, leva 1: cinco URLs novas no eixo que a Bússola verificou
 * ABERTO e que é o de maior volume de busca da ilha — "quantos litros para X
 * peixes". Nível 1 `/peixes/`, nível 2 `/peixes/tetras/` e três fichas de
 * nível 3, na ordem do 16.6 (a mãe e as três primeiras filhas de maior
 * intenção, nunca uma filha de cada categoria espalhada).
 *
 * A TESE DESTA LEVA, e é ela que justifica a página existir: AS FONTES
 * DECLARAM A BASE DO AQUÁRIO, NÃO O LITRO. As sete primeiras respostas da
 * SERP brasileira (medidas em 12/09/2026, ver `consulta` de cada ficha) dão
 * litro sem fonte — "8 a 10 neons em 40 litros", "3 a 5 litros por neon" — e
 * discordam entre si. O banco desta ilha tem, para cada espécie, a base mínima
 * declarada por compêndio com nome e data, e as duas réguas brasileiras de
 * lotação com a atribuição de cada extremo. A página serve as duas coisas lado
 * a lado, e é isso que nenhum dos sete serve.
 *
 * SEIS DECISÕES, e nenhuma é de estilo:
 *
 *   1. NENHUM NÚMERO DESTA PÁGINA É DIGITADO. Frente mínima, litro por altura,
 *      lotação pelos três critérios, quantas espécies têm ficha, quantas estão
 *      no banco: tudo sai do catálogo gerado do banco, contado na hora de
 *      imprimir. É a cicatriz de 11/09 (seção 8): número de tela que era
 *      verdade no dia em que foi escrito mente em silêncio no dia seguinte.
 *
 *   2. A FRENTE MÍNIMA NÃO SE EXTRAPOLA POR INDIVÍDUO. O esquema do banco
 *      declara o derivado `frente_por_individuo_cm` (frente mínima ÷ cardume
 *      mínimo) e ele sai na tela como leitura per capita do mínimo declarado —
 *      mas NUNCA multiplicado para "quantos cm para 10 peixes". Os 60 cm que a
 *      fonte declara para 5 neons são o piso de onde o cardume consegue nadar
 *      em cardume, não o preço de cinco peixes: multiplicar daria 120 cm para
 *      dez neons, que contradiz todas as fontes e seria regra de bolso nossa
 *      com cara de dado. Quem responde "e para dez?" são os três critérios de
 *      lotação, que é exatamente para isso que eles existem.
 *
 *   3. CONFLITO DECLARADO SAI COM OS DOIS EXTREMOS E O NOME DE CADA UM. O
 *      mato-grosso tem 60 cm na FishBase e 80 cm no Seriously Fish; o cardinal
 *      tem 2,5 e 3,0 cm de porte. A ilha nunca tira média (rodapé da casca), e
 *      onde o número entra em conta a página usa o extremo SEGURO — aquário
 *      maior, peixe maior — e diz que escolheu e por quê.
 *
 *   4. ESPÉCIE NÃO É PRODUTO, então aqui não tem bloco de compra — e a página
 *      DIZ isso, porque silêncio parece defeito (seção 7). Peixe vivo não se
 *      vende por link de afiliado, e o equipamento que o cardume pede sai nas
 *      calculadoras, onde a vitrine já existe. As fichas linkam C1, C5 e C3
 *      pelo corpo, que é o 16.4(d) e é também o caminho do dinheiro.
 *
 *   5. A LISTA DE QUEM DIVIDE A ÁGUA NÃO É VEREDITO DE CONVIVÊNCIA. O esquema
 *      do banco recusa compatibilidade como campo booleano, de propósito:
 *      convivência depende de volume, de layout e de ordem de introdução. O
 *      que a página publica é o que ela mede — interseção das faixas de
 *      temperatura declaradas, com o critério escrito na frente da lista — e
 *      quem o banco declara agressivo fica fora com o nome na tela.
 *
 *   7. A SEGUNDA CATEGORIA (leva 3, 12/09/2026) SEPAROU O DECLARADO DO
 *      DIGITADO. Enquanto /peixes/tetras/ foi a única mãe de nível 2, três
 *      coisas eram indistinguíveis de suas versões corretas: "a mãe" e "a mãe
 *      certa"; "as fichas do eixo" e "as fichas desta categoria"; e o
 *      substantivo da abertura, que era a palavra "tetras" escrita no meio do
 *      HTML ao lado de uma contagem derivada. A primeira renderização de
 *      /peixes/corydoras/ serviu "São 4 tetras" — contagem certa, substantivo
 *      mentindo —, e o portão pegou antes do ar porque a régua do teste passou
 *      a declarar o rótulo em vez de derivá-lo do slug. Agora `plural` e
 *      `linha_mestra` moram na declaração da categoria, junto do `criterio`.
 *
 *   6. O JSON-LD SAI NO wp_head, NUNCA no retorno do shortcode. O retorno
 *      atravessa os filtros do the_content, que trocam "&" pela entidade
 *      numérica e quebrariam o JSON do mesmo jeito que quebraram o JavaScript
 *      das cinco calculadoras em 08/09/2026.
 *
 *   7. A PÁGINA SÓ AFIRMA O QUE A FONTE DECLAROU, E "BASE" NÃO É "FRENTE"
 *      (leva 2, 12/09/2026). A linha mestra da ficha terminava sempre em "e a
 *      fonte declara a BASE, não o litro". Era verdade nas três fichas da leva
 *      1, porque as três têm `base_minima_cm` preenchida — e é falsa em 14 dos
 *      36 registros do banco, onde a fonte declara só o COMPRIMENTO mínimo e
 *      nunca disse uma palavra sobre o fundo. O rodóstomo, desta leva, é o
 *      primeiro caso: o Seriously Fish declara "no mínimo 90 cm de
 *      comprimento" e ponto. Nesses registros a frase passa a dizer
 *      COMPRIMENTO, as duas tabelas que dependem do fundo não saem — e a
 *      página DIZ que não saíram e por quê, em vez de simplesmente encolher.
 *      Sumiço silencioso de tabela é a forma disfarçada do "silêncio parece
 *      defeito" da seção 7: quem lê não tem como saber se a ilha não sabe ou
 *      se esqueceu.
 *
 *   8. ESPÉCIE DE CARDUME SEM O NÚMERO DO CARDUME NÃO VIRA FICHA. O título
 *      deste eixo é "quantos litros para um cardume de X" e a linha mestra
 *      abre por "para os N X que a fonte declara como cardume mínimo". Sem N a
 *      página caía num ramo que escrevia a frase sem o número e abria a tabela
 *      pré-renderizada em UM exemplar — numa página que, duas telas abaixo,
 *      diz que a espécie só vive em grupo. O esquema já cobrava esse número no
 *      portão da C8 desde que o banco nasceu; o que faltava era a página
 *      cobrar o mesmo, com a mesma frase. `aquametria_peixes_pode_virar_ficha()`
 *      é a régua DESTE lado, escrita aqui e não importada do gerador — quem
 *      confere escreve a própria régua (seção 8 do contrato).
 *
 * O QUE ESTE SNIPPET NÃO FAZ: criar página. Quem cria é a casca, pelo filtro
 * `aquametria_paginas` (casca 1.7.0) — inclusive o pai de cada uma, que é o que
 * faz a URL mostrar os três níveis da seção 16.1.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'AQUAMETRIA_PEIXES_VERSAO' ) ) {
	define( 'AQUAMETRIA_PEIXES_VERSAO', '1.2.0' );
}

/* A data em que a SERP das consultas foi classificada (seção 14.9). Está aqui
   uma vez só: data escrita à mão em sete páginas envelhece em duas. As quatro
   consultas da leva 2 foram classificadas na MESMA data das três da leva 1 —
   se uma leva futura sair em outro dia, esta constante deixa de servir para
   todas e vira campo do registro. */
if ( ! defined( 'AQUAMETRIA_PEIXES_SERP_EM' ) ) {
	define( 'AQUAMETRIA_PEIXES_SERP_EM', '12/09/2026' );
}

/* As duas réguas brasileiras de lotação, com o extremo de cada uma. Vêm de
   `dados/constantes-calculadoras.json` (lotacao-1cm-por-litro e
   lotacao-litros-por-cm), colhidas em 04/09/2026 no levantamento do Bloco 1.
   Estão aqui em CONSTANTE e não no meio de uma função porque é o que muda de
   ilha para ilha, e porque a tela precisa nomear quem publicou cada extremo. */
if ( ! defined( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA' ) ) {
	define( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA', 1.0 );   // 1 cm de peixe por litro
	define( 'AQUAMETRIA_PEIXES_LOTACAO_MEIO', 1.5 );       // 1,5 L por cm de peixe
	define( 'AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA', 4.0 ); // 4 L por cm de peixe
}

/* ---------------------------------------------------------------------------
 * 1. O catálogo — gerado do banco, nunca editado à mão
 *
 * `ferramentas/gerar-catalogo-especies.py` reescreve o bloco abaixo. Só entra
 * quem passa no portão de página do esquema (sete campos e duas fontes de
 * corpos distintos), e nada derivado é gravado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_catalogo' ) ) {
function aquametria_peixes_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */
	static $catalogo = null;
	if ( null !== $catalogo ) {
		return $catalogo;
	}
	$catalogo = array(
		'hyphessobrycon-amandae' => array(
			'id' => 'hyphessobrycon-amandae',
			'cientifico' => 'Hyphessobrycon amandae',
			'sinonimos' => array(),
			'populares' => array(
				'tetra ember',
				'tetra fogo',
				'ember tetra',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => 'America do Sul: bacia do rio Araguaia',
			'porte_cm' => 2,
			'porte_medida' => 'SL',
			'cardume' => 8,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'temp_min' => 20,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/12376',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
					),
					'referencia' => 'FishBase - ficha da especie: max length 2,0 cm SL macho/nao-sexado; tropical, 24 a 28 C; familia Acestrorhamphidae (tetras americanos); America do Sul, bacia do rio Araguaia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hyphessobrycon-amandae',
					'em' => '2026-09-11',
					'campos' => array(
						'temperatura_C',
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
						'convivencia',
						'comportamento',
					),
					'referencia' => 'Seriously Fish - ficha da especie: aquario com base de no minimo 45 x 30 cm (18 x 12 pol) ou equivalente; temperatura de 20 a 28 C, com a agua de pH levemente acido a neutro e a temperatura na ponta ALTA da faixa; gregaria e formando cardume por natureza, com a compra minima recomendada de 8 a 10 exemplares, porque em numero menor fica arisca; muito pacifica, nao compete com companheiros agitados ou bem maiores.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'temperatura_C',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 24,
								'max' => 28,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: tropical, 24 a 28 C',
						),
						array(
							'valor' => array(
								'min' => 20,
								'max' => 28,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: 20 a 28 C, com a recomendacao de manter na ponta alta da faixa',
						),
					),
					'razao' => 'Temperatura e campo de MANUTENCAO, e a tabela dominio_por_campo poe o compendio acima da base cientifica justamente nesses campos: a FishBase descreve a agua onde o peixe vive, o compendio descreve a agua em que ele e mantido. As duas faixas nao se contradizem - 24 a 28 cabe dentro de 20 a 28 -, e o piso mais baixo e uma permissao do compendio, nao uma recomendacao: a mesma frase manda ficar na ponta alta. Quem dimensiona aquecedor pelo piso de 20 C encomenda mais potencia, que e o lado seguro do erro.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'paracheirodon-innesi' => array(
			'id' => 'paracheirodon-innesi',
			'cientifico' => 'Paracheirodon innesi',
			'sinonimos' => array(),
			'populares' => array(
				'tetra neon',
				'neon',
				'neon comum',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 2.2,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Paracheirodon-innesi',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 2,2 cm SL; 20 a 26 C; pH 5,0 a 7,0; dH 1 a 2; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/paracheirodon-innesi/',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 60 x 30 cm ou maior; agua tipicamente acida, de dureza de carbonatos desprezivel, tingida por substancias humicas.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.org/summary/10691',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Characiformes > Acestrorhamphidae (tetras americanos).',
				),
			),
			'conflitos' => array(),
		),
		'paracheirodon-axelrodi' => array(
			'id' => 'paracheirodon-axelrodi',
			'cientifico' => 'Paracheirodon axelrodi',
			'sinonimos' => array(
				'Cheirodon axelrodi',
				'Hyphessobrycon cardinalis',
			),
			'populares' => array(
				'neon cardinal',
				'tetra cardinal',
				'cardinal',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => 'Alto Orinoco e bacia do rio Negro, America do Sul',
			'porte_cm' => 3,
			'porte_medida' => 'SL',
			'cardume' => 8,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'temp_min' => 23,
			'temp_max' => 27,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/paracheirodon-axelrodi.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'nivel_natacao',
						'origem_geografica',
					),
					'referencia' => 'FishBase — ficha da especie: 23 a 27 C, pH 4,0 a 6,0, dH 5 a 12; ocorre sobretudo em cardumes nas camadas medias da coluna; alto Orinoco e rio Negro. Max 2,5 cm SL na busca restrita de 09/09/2026 e 3,0 cm SL na busca aberta do mesmo dia (ver conflitos).',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/paracheirodon-axelrodi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 60 x 30 cm ou maior; manter em grupo misto de pelo menos 8 a 10 exemplares, e junto de outros cardumes para dar seguranca ao grupo.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/paracheirodon-axelrodi.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Characiformes > Acestrorhamphidae (tetras americanos). A familia mudou de nome na revisao recente dos caracideos: a ficha nao diz mais Characidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'porte_adulto_cm',
					'valores' => array(
						array(
							'valor' => 2.5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, leitura por busca restrita ao dominio em 09/09/2026: max 2,5 cm SL',
						),
						array(
							'valor' => 3,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, leitura por busca aberta em 09/09/2026, com a atribuicao explicita a FishBase no resumo: 3,0 cm SL',
						),
					),
					'razao' => 'Duas leituras da MESMA fonte, no mesmo dia, devolveram 2,5 e 3,0 cm SL. Nao e divergencia entre autores: e o limite de colher numero por resumo de busca sem poder abrir a pagina. Enquanto o egresso nao abrir, o banco publica os dois e usa o maior, porque em lotacao errar o porte para menos e o lado que lota demais.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'hemigrammus-erythrozonus' => array(
			'id' => 'hemigrammus-erythrozonus',
			'cientifico' => 'Hemigrammus erythrozonus',
			'sinonimos' => array(),
			'populares' => array(
				'tetra-brilhante',
				'glowlight',
				'tetra-luminoso',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 3.3,
			'porte_medida' => 'TL',
			'cardume' => 6,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 37.5,
			'temp_min' => 24,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10642',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Acestrorhamphidae (tetras americanos); max 3,3 cm TL; pH 6,0 a 8,0; dH 5 a 12; 24 a 28 C; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hemigrammus-erythrozonus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
						'ph',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 60 x 37,5 x 30 cm (70 litros) abriga confortavelmente um grupo pequeno; comprar sempre grupo de pelo menos 6, de preferencia 10 ou mais, porque e especie de cardume e vai muito melhor entre os seus; pH 5,5 a 7,5, mais colorida em agua acida; e um dos melhores tetras para o aquario comunitario geral: ativa, colorida e pacifica.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pelo menos 6, de preferencia 10 ou mais',
						),
					),
					'razao' => 'Campo de bem-estar com divergencia de um individuo: fica o maior, 6.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 6,
								'max' => 8,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 6,0 a 8,0',
						),
						array(
							'valor' => array(
								'min' => 5.5,
								'max' => 7.5,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pH 5,5 a 7,5, mais colorida em agua acida',
						),
					),
					'razao' => 'Faixas deslocadas em meio ponto de pH nas duas pontas. Campo de manutencao: manda o compendio.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'otocinclus-vittatus' => array(
			'id' => 'otocinclus-vittatus',
			'cientifico' => 'Otocinclus vittatus',
			'sinonimos' => array(),
			'populares' => array(
				'otocinclo',
				'oto',
				'limpa-vidro',
			),
			'familia' => 'Loricariidae',
			'origem' => '',
			'porte_cm' => 3.3,
			'porte_medida' => 'TL',
			'cardume' => 6,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 20,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Otocinclus-vittatus',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: max 3,3 cm TL; 20 a 25 C; pH 6,0 a 7,5; dH 2 a 18.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/otocinclus-macrospilus/',
					'em' => '2026-09-09',
					'campos' => array(
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
						'alimentacao',
						'exige_aquario_maduro',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish — ficha do genero Otocinclus (pagina de O. macrospilus): sao gregarios por natureza e o ideal e manter em grupo de 6 exemplares ou mais; o menor aquario a considerar seguro para o genero tem pelo menos 45 cm de comprimento, por causa das arrancadas de nado; a unica atividade diurna e raspar alga de folha, tronco, rocha e vidro, e sem planta e superficie em abundancia o peixe se sente exposto, o que traz doenca e morte precoce; muitos aquaristas relatam menos problema quando os peixes entram em aquario maduro e plantado, com qualidade de agua estavel e microrganismos e algas em quantidade.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Otocinclus-vittatus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Loricariidae (Armored catfishes) > subfamilia Hypoptopomatinae.',
				),
			),
			'conflitos' => array(),
		),
		'corydoras-panda' => array(
			'id' => 'corydoras-panda',
			'cientifico' => 'Corydoras panda',
			'sinonimos' => array(
				'Hoplisoma panda',
			),
			'populares' => array(
				'coridora-panda',
				'cory-panda',
			),
			'familia' => 'Callichthyidae',
			'origem' => '',
			'porte_cm' => 3.8,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'temp_min' => 20,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/corydoras-panda.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie (hoje publicada como Hoplisoma panda): familia Callichthyidae (callichthyid armored catfishes); max 3,8 cm SL; pH 6,0 a 8,0; dH 2 a 25; 20 a 25 C; alto Amazonas.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-panda',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 45 x 30 x 30 cm ja atende um grupo pequeno; coridoras devem ser mantidas em grupo, e um grupo de pelo menos SEIS e o melhor; temperatura em torno de 24 C esta bem.',
				),
			),
			'conflitos' => array(),
		),
		'danio-rerio' => array(
			'id' => 'danio-rerio',
			'cientifico' => 'Danio rerio',
			'sinonimos' => array(
				'Brachydanio rerio',
				'Brachydanio frankei',
			),
			'populares' => array(
				'paulistinha',
				'zebrafish',
				'peixe-zebra',
			),
			'familia' => 'Danionidae',
			'origem' => '',
			'porte_cm' => 3.8,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 90,
			'base_comprimento' => 90,
			'base_largura' => 30,
			'temp_min' => 18,
			'temp_max' => 24,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/danio-rerio.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 3,8 cm SL; 18 a 24 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/danio-rerio/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'comportamento',
					),
					'referencia' => 'Seriously Fish — ficha da especie (publicada como Brachydanio rerio): especie ativa, entao mesmo um grupo pequeno precisa de aquario com base minima de 90 x 30 cm; tamanho usual de 40 a 50 mm; e pacifica, rustica e barata.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/danio-rerio.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Teleostei > Cypriniformes (Carps) > Danionidae (Danios) > Danioninae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 90,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: especie ativa, base minima de 90 x 30 cm mesmo para grupo pequeno',
						),
					),
					'razao' => 'Meia diferenca de frente para o mesmo peixe de 4 cm. O compendio manda em campo de manutencao e o campo e de bem-estar: fica o maior, 90 cm, e a ficha publica o outro numero atribuido.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'hyphessobrycon-eques' => array(
			'id' => 'hyphessobrycon-eques',
			'cientifico' => 'Hyphessobrycon eques',
			'sinonimos' => array(
				'Hyphessobrycon callistus',
				'Hyphessobrycon serpae',
				'Megalamphodus eques',
			),
			'populares' => array(
				'mato-grosso',
				'serpae',
				'tetra-serpae',
			),
			'familia' => 'Characidae',
			'origem' => '',
			'porte_cm' => 4,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => 'agressivo',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'temp_min' => 22,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/Summary/SpeciesSummary.php?id=46294',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
						'cardume_minimo',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Characidae (subfamilia Stethaprioninae); max 4 cm SL macho/nao sexado; pH 5,0 a 7,8; dH 10 a 25; 22 a 26 C; secao de aquario: agressivo, em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hyphessobrycon-eques/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'ph',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 80 x 30 cm ou equivalente e o minimo absoluto a considerar (volume citado de 72 litros); os exemplares de criadouro sao adaptaveis quanto a quimica da agua e ficam bem na faixa de pH 5,0 a 7,5.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 80,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 80 x 30 cm e o minimo absoluto',
						),
					),
					'razao' => 'Um terco a mais de frente para o mesmo peixe de 4 cm. O compendio manda em campo de manutencao e o campo e de bem-estar: fica o maior, 80 cm.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7.8,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 5,0 a 7,8',
						),
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7.5,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: exemplares de criadouro ficam bem de 5,0 a 7,5',
						),
					),
					'razao' => 'Divergencia pequena (0,3 no teto) e no mesmo sentido. pH e campo de manutencao: fica o do compendio, que e tambem o mais estreito.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'tanichthys-albonubes' => array(
			'id' => 'tanichthys-albonubes',
			'cientifico' => 'Tanichthys albonubes',
			'sinonimos' => array(),
			'populares' => array(
				'peixe-neve',
				'white cloud',
				'paulistinha-da-montanha',
				'tanictis',
			),
			'familia' => 'Tanichthyidae',
			'origem' => 'Asia: China e Vietna',
			'porte_cm' => 4,
			'porte_medida' => 'TL',
			'cardume' => 10,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 14,
			'temp_max' => 22,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Tanichthys-albonubes',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 4,0 cm TL; 18 a 22 C, sobrevivendo a agua de ate 5 C; pH 6,0 a 8,0; dH 5 a 19; familia Tanichthyidae; Asia, China e Vietna; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/tanichthys-albonubes',
					'em' => '2026-09-11',
					'campos' => array(
						'temperatura_C',
						'cardume_minimo',
						'convivencia',
						'comportamento',
					),
					'referencia' => 'Seriously Fish - ficha da especie: manter a 14 a 22 C (57 a 72 F); peixe de cardume por natureza, o ideal e comprar um grupo de 10 ou mais exemplares, porque assim os individuos ficam menos nervosos, o conjunto fica mais natural e os machos mostram a melhor cor disputando as femeas; muito pacifico e residente ideal de aquario comunitario bem mantido, desde que a exigencia de temperatura seja respeitada; micropredador que come pequenos insetos, vermes, crustaceos e zooplancton.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'temperatura_C',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 18,
								'max' => 22,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: 18 a 22 C, sobrevivendo a agua de ate 5 C',
						),
						array(
							'valor' => array(
								'min' => 14,
								'max' => 22,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: manter a 14 a 22 C',
						),
					),
					'razao' => 'Campo de manutencao: o compendio manda, pela tabela dominio_por_campo. O teto e o mesmo nas duas fontes e so o piso desce, de 18 para 14 C. Nao muda o que esta especie ja significava para a ilha - ela e a segunda que dispensa aquecedor em boa parte do Brasil -, mas muda o lado oposto da conta: com teto de 22 C, o risco desta especie no verao brasileiro e de agua QUENTE demais, e nenhuma calculadora da ilha dimensiona resfriamento hoje.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: secao de aquario, manter em grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 10,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: o ideal e um grupo de 10 ou mais exemplares',
						),
					),
					'razao' => 'As duas regras do esquema apontam para o mesmo lado aqui, o que e raro: o compendio manda em campo de manutencao, E o conservador de campo de bem-estar e o MAIOR. O banco publica 10. O numero importa porque ele multiplica a frente por individuo: com 60 cm declarados, 5 peixes dao 12 cm de frente por individuo e 10 peixes dao 6 cm - a mesma especie, o dobro de densidade, dependendo de qual fonte a pagina citar. Publicar as duas e o unico jeito honesto.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'mikrogeophagus-ramirezi' => array(
			'id' => 'mikrogeophagus-ramirezi',
			'cientifico' => 'Mikrogeophagus ramirezi',
			'sinonimos' => array(
				'Apistogramma ramirezi',
				'Papiliochromis ramirezi',
				'Microgeophagus ramirezi',
			),
			'populares' => array(
				'ramirezi',
				'borboleta-boliviana',
				'acará-borboleta',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 4.2,
			'porte_medida' => 'SL',
			'cardume' => null,
			'convivencia' => 'casal',
			'comportamento' => 'territorial',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 27,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Mikrogeophagus-ramirezi',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae; max 4,2 cm SL; pH 5,0 a 6,0; dH 5 a 12; 27 a 30 C; secao de aquario: aquario minimo de 60 cm, aos pares.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/mikrogeophagus-ramirezi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: ao atingir a maturidade sexual os ramirezi formam casais, e cada casal passa a defender um territorio de cerca de meio metro de diametro.',
				),
			),
			'conflitos' => array(),
		),
		'hemigrammus-rhodostomus' => array(
			'id' => 'hemigrammus-rhodostomus',
			'cientifico' => 'Hemigrammus rhodostomus',
			'sinonimos' => array(
				'Petitella rhodostoma',
			),
			'populares' => array(
				'rodóstomo',
				'nariz-vermelho',
				'cabeça-de-fósforo',
			),
			'familia' => 'Characidae',
			'origem' => '',
			'porte_cm' => 5,
			'porte_medida' => 'TL',
			'cardume' => 10,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 90,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 26.5,
			'temp_max' => 29,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Hemigrammus-rhodostomus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (hoje publicada como Petitella rhodostoma): familia Characidae; max 5,0 cm TL; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 80 cm; especie tropical das bacias do baixo Amazonas e do Orinoco.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hemigrammus-rhodostomus',
					'em' => '2026-09-09',
					'campos' => array(
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'Seriously Fish — ficha da especie: agua mole e acida, pH 5,5 a 6,5, gH 1 a 5, temperatura em torno de 26,5 a 29 C; manter em grupos de 10 ou de preferencia mais, porque e um dos pequenos tetras de cardume mais coeso e nao vai bem em numero insuficiente; a natacao ativa pede aquario de no minimo 90 cm de comprimento.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais',
						),
						array(
							'valor' => 10,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupos de 10 ou de preferencia mais',
						),
					),
					'razao' => 'O dobro de peixes para o mesmo cardume. Campo de bem-estar: fica o maior, 10, e o numero da base sai publicado do lado. Dobrar o cardume dobra a carga biologica, entao esta divergencia muda o filtro e o aquario que a pessoa compra.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 80,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 80 cm',
						),
						array(
							'valor' => 90,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: no minimo 90 cm de comprimento',
						),
					),
					'razao' => 'Campo de bem-estar com duas declaracoes proximas: fica o maior, 90 cm.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'trigonostigma-heteromorpha' => array(
			'id' => 'trigonostigma-heteromorpha',
			'cientifico' => 'Trigonostigma heteromorpha',
			'sinonimos' => array(
				'Rasbora heteromorpha',
			),
			'populares' => array(
				'rasbora arlequim',
				'arlequim',
				'rasbora',
			),
			'familia' => 'Danionidae',
			'origem' => 'Sudeste asiatico: Malasia, Singapura e Indonesia',
			'porte_cm' => 5,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'temp_min' => 22,
			'temp_max' => 25,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10881',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'origem_geografica',
						'nivel_natacao',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 5,0 cm TL; 22 a 25 C; pH 5,0 a 7,0; dH 5 a 12; bentopelagica; Malasia, Singapura e Indonesia; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trigonostigma-heteromorpha',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 60 x 30 cm deve ser a menor a considerar, porque a especie tem de ser mantida em numero; pH 5,0 a 6,0 e dureza de 1 a 5 graus, com a temperatura na parte alta da faixa.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/trigonostigma-heteromorpha.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Danionidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 5,0 a 7,0',
						),
						array(
							'valor' => array(
								'min' => 5,
								'max' => 6,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pH 5,0 a 6,0, dureza de 1 a 5 graus',
						),
					),
					'razao' => 'Intervalos encaixados, nao contraditorios: o compendio e mais estreito e mais acido. Campo de manutencao que NAO e de bem-estar direto, entao vale a intersecao conservadora da regra V17 do banco de produtos — a afirmacao que as duas fontes sustentam e 5,0 a 6,0.',
					'tratamento' => 'intersecao-conservadora',
				),
			),
		),
		'xiphophorus-maculatus' => array(
			'id' => 'xiphophorus-maculatus',
			'cientifico' => 'Xiphophorus maculatus',
			'sinonimos' => array(),
			'populares' => array(
				'platy',
				'plati',
				'moeda',
			),
			'familia' => 'Poeciliidae',
			'origem' => '',
			'porte_cm' => 6,
			'porte_medida' => 'TL',
			'cardume' => null,
			'convivencia' => 'harem',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 18,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-maculatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'FishBase — ficha da especie: max 4,0 cm TL macho e 6,0 cm TL femea; 18 a 25 C; pH 7,0 a 8,0; dH 9 a 19; secao de aquario: aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/xiphophorus-maculatus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: muito pacifico e convive com a maioria das especies comunitarias, sem a agressividade de alguns espadas e molinesias, com os machos se tolerando; quando machos e femeas dividem o aquario deve haver mais femeas que machos, para dissipar o assedio dos machos; macho cerca de 5 cm e femea cerca de 7,5 cm; a agua do habitat natural fica em media entre 23 e 24 C.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-maculatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Cyprinodontiformes > Poeciliidae (Poeciliids).',
				),
			),
			'conflitos' => array(),
		),
		'betta-splendens' => array(
			'id' => 'betta-splendens',
			'cientifico' => 'Betta splendens',
			'sinonimos' => array(
				'Micracanthus marchei',
			),
			'populares' => array(
				'betta',
				'beta',
				'peixe-de-briga',
			),
			'familia' => 'Osphronemidae',
			'origem' => '',
			'porte_cm' => 6.5,
			'porte_medida' => 'TL',
			'cardume' => null,
			'convivencia' => 'solitario',
			'comportamento' => 'agressivo',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'temp_min' => 24,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/betta-splendens.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: max 6,5 cm TL para o macho; 24 a 30 C; pH 6,0 a 8,0; dH 5 a 19.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/betta-splendens/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'convivencia',
						'comportamento',
						'ph',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 45 x 30 cm ou equivalente ja e grande para um macho sozinho ou um casal; melhor manter sozinho, as linhagens ornamentais sao mais agressivas que qualquer outra especie de Betta e na maioria dos casos so um individuo por aquario; manter o aquario bem tampado e nao encher ate a borda, porque a especie precisa de acesso a camada de ar umido acima da agua e e excelente saltadora; exemplares selvagens preferem pH entre 5,0 e 7,0 e as linhagens ornamentais aceitam de 6,0 a 8,0.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/speciessummary.php?id=4768',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Osphronemidae (gouramis).',
				),
			),
			'conflitos' => array(),
		),
		'nannostomus-beckfordi' => array(
			'id' => 'nannostomus-beckfordi',
			'cientifico' => 'Nannostomus beckfordi',
			'sinonimos' => array(
				'Nannostomus anomalus',
				'Nannostomus aripirangensis',
			),
			'populares' => array(
				'peixe-lápis',
				'peixe lápis dourado',
				'nannostomus beckfordi',
			),
			'familia' => 'Lebiasinidae',
			'origem' => '',
			'porte_cm' => 6.5,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 24,
			'temp_max' => 26,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Nannostomus-beckfordi',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 6,5 cm SL; 24 a 26 C; pH 6,0 a 8,0; dH 5 a 19; familia Lebiasinidae; habita rios pequenos de pouca correnteza e brejos, formando grupos em que os machos dominam para defender territorio; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/nannostomus-beckfordi/',
					'em' => '2026-09-11',
					'campos' => array(
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: como os demais Nannostomus, o N. beckfordi deve ser mantido em grupo; e bastante comum no comercio aquarista e uma excelente escolha para quem esta comecando, por ser menos exigente que a maioria das congeneres.',
				),
			),
			'conflitos' => array(),
		),
		'corydoras-paleatus' => array(
			'id' => 'corydoras-paleatus',
			'cientifico' => 'Corydoras paleatus',
			'sinonimos' => array(
				'Hoplisoma paleatum',
			),
			'populares' => array(
				'coridora pimenta',
				'coridora paleatus',
				'cory paleatus',
			),
			'familia' => 'Callichthyidae',
			'origem' => '',
			'porte_cm' => 6.6,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 61,
			'base_comprimento' => 61,
			'base_largura' => 38,
			'temp_min' => 18,
			'temp_max' => 23,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Corydoras-paleatus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie (publicada tambem como Hoplisoma paleatum): max length 6,6 cm SL macho/nao-sexado e 7,1 cm SL femea; 18 a 23 C; pH 6,0 a 8,0; dH 5 a 19; familia Callichthyidae; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-paleatus',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish - ficha da especie: base recomendada de 61 x 38 cm (24 x 15 pol).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 61,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'corydoras-sterbai' => array(
			'id' => 'corydoras-sterbai',
			'cientifico' => 'Corydoras sterbai',
			'sinonimos' => array(
				'Hoplisoma sterbai',
			),
			'populares' => array(
				'coridora sterbai',
				'cory sterbai',
			),
			'familia' => 'Callichthyidae',
			'origem' => 'America do Sul: Brasil central e Bolivia',
			'porte_cm' => 6.8,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'temp_min' => 21,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/corydoras-sterbai.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase - ficha da especie (publicada tambem como Hoplisoma sterbai): max length 6,8 cm SL macho/nao-sexado; 21 a 25 C; pH 6,0 a 8,0; dH 2 a 25; familia Callichthyidae; America do Sul, Brasil central e Bolivia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-sterbai/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'convivencia',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish - ficha da especie: um aquario de 45 x 30 x 30 cm (42,5 litros) e grande o bastante para um grupo pequeno desta especie.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-sterbai/',
					'em' => '2026-09-12',
					'campos' => array(
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: a especie deve ser mantida SEMPRE em grupo, porque fica bem mais confiante e ativa na presenca dos seus, e um grupo de pelo menos SEIS e o melhor.',
				),
			),
			'conflitos' => array(),
		),
		'puntigrus-tetrazona' => array(
			'id' => 'puntigrus-tetrazona',
			'cientifico' => 'Puntigrus tetrazona',
			'sinonimos' => array(
				'Puntius tetrazona',
				'Systomus tetrazona',
				'Barbus tetrazona',
			),
			'populares' => array(
				'barbo sumatra',
				'sumatrano',
				'tigre',
			),
			'familia' => 'Cyprinidae',
			'origem' => '',
			'porte_cm' => 7,
			'porte_medida' => 'TL',
			'cardume' => 8,
			'convivencia' => 'cardume',
			'comportamento' => 'semi-agressivo',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Puntigrus-tetrazona',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (barbo-de-sumatra): max 7,0 cm TL; 20 a 26 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, NAO manter com peixes de nadadeiras longas, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/puntigrus-tetrazona/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
						'comportamento',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 80 x 30 cm ou equivalente deve ser a menor a considerar; grupo de pelo menos 8 a 10 exemplares deve ser a compra minima, porque assim os peixes se distraem entre si em vez de perturbar os companheiros de aquario, e o conjunto fica mais natural.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Puntigrus-tetrazona',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cyprinidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 8,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupo de pelo menos 8 a 10 exemplares como compra minima',
						),
					),
					'razao' => 'Campo de manutencao e de bem-estar: manda o compendio e vence o maior. Aqui o numero maior nao e so conforto do peixe, e seguranca dos vizinhos: as duas fontes ligam grupo pequeno a agressao dirigida para fora do cardume.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'corydoras-aeneus' => array(
			'id' => 'corydoras-aeneus',
			'cientifico' => 'Corydoras aeneus',
			'sinonimos' => array(
				'Osteogaster aenea',
				'Corydoras schultzei',
				'Corydoras venezuelanus',
			),
			'populares' => array(
				'coridora bronze',
				'coridora',
				'cascudinho',
			),
			'familia' => 'Callichthyidae',
			'origem' => 'America do Sul, da Colombia e Trinidad ate a bacia do Prata, a leste dos Andes',
			'porte_cm' => 7.5,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'temp_min' => 25,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/7777',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'nivel_natacao',
						'origem_geografica',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (publicada tambem como Osteogaster aenea): max 7,5 cm SL; 25 a 28 C; pH 6,0 a 8,0; dH 5 a 19; demersal; da Colombia e Trinidad ate a bacia do Prata; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-aeneus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 80 x 30 cm ou equivalente para manutencao de longo prazo; areia fina e o substrato ideal, cascalho arredondado serve desde que mantido escrupulosamente limpo; grupo de pelo menos seis da o comportamento e a confianca normais do genero.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Corydoras-aeneus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie (publicada como Osteogaster aenea): Siluriformes (Catfishes) > Callichthyidae (Callichthyid armored catfishes) > subfamilia Corydoradinae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 80,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 80 x 30 cm ou equivalente para manutencao de longo prazo',
						),
					),
					'razao' => 'Campo de manutencao: pela tabela dominio_por_campo quem manda e o compendio, e o compendio pede mais espaco. Como e campo de bem-estar, o conservador e o MAIOR, e as duas declaracoes saem atribuidas na ficha.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupo de pelo menos seis',
						),
					),
					'razao' => 'Mesma logica: campo de manutencao e de bem-estar, vence o maior, e os dois numeros ficam publicados.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'gymnocorymbus-ternetzi' => array(
			'id' => 'gymnocorymbus-ternetzi',
			'cientifico' => 'Gymnocorymbus ternetzi',
			'sinonimos' => array(),
			'populares' => array(
				'tetra-negro',
				'viúva-negra',
				'tetra-preto',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 7.5,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 75,
			'base_comprimento' => 75,
			'base_largura' => 30,
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4682',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Acestrorhamphidae (tetras americanos); max 7,5 cm SL; pH 6,0 a 8,0; dH 5 a 19; 20 a 26 C (subtropical); peixe de cardume pacifico.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/gymnocorymbus-ternetzi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um grupo pode ser mantido em aquario padrao de 75 x 30 cm (70 litros); especie ativa, que quer bastante espaco aberto para nadar mais areas de plantio denso e vegetacao flutuante para amenizar a luz.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4682',
					'em' => '2026-09-12',
					'campos' => array(
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'FishBase - secao de aquario: manter em grupos de 5 ou mais individuos; aquario minimo de 60 cm.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 75,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: um grupo pode ser mantido em aquario padrao de 75 x 30 cm',
						),
					),
					'razao' => 'Quinze centimetros de frente entre as duas declaracoes, e as DUAS reguas do esquema apontam para o mesmo lado, o que e raro e vale registrar: comprimento_minimo_aquario_cm e campo de MANUTENCAO, e a tabela dominio_por_campo poe o compendio acima da base cientifica nesses campos; e a regra de assimetria de custo do banco de especies manda ficar com o MAIOR, porque errar espaco para cima so custa aquario mais largo. Fica 75. A divergencia nao e conflito de fato: a base cientifica declara o piso de onde a especie sobrevive e o compendio declara a base de onde o cardume nada em cardume - e e o segundo que a pergunta desta ilha faz.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'melanotaenia-boesemani' => array(
			'id' => 'melanotaenia-boesemani',
			'cientifico' => 'Melanotaenia boesemani',
			'sinonimos' => array(),
			'populares' => array(
				'peixe arco-íris boesemani',
				'rainbow boesemani',
				'arco-íris de boeseman',
			),
			'familia' => 'Melanotaeniidae',
			'origem' => 'Asia/Oceania: lagos Ajamaru, peninsula de Vogelkop, Irian Jaya, Indonesia',
			'porte_cm' => 9,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => 120,
			'base_largura' => 30,
			'temp_min' => 27,
			'temp_max' => 30,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/10489',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 9,0 cm SL macho/nao-sexado e 7,0 cm SL femea; 27 a 30 C; pH 7,0 a 8,0; dH 9 a 19; familia Melanotaeniidae; conhecida apenas dos lagos Ajamaru, Irian Jaya; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 80 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/melanotaenia-boesemani',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'cardume_minimo',
					),
					'referencia' => 'Seriously Fish - ficha da especie: base de 120 x 30 cm (48 x 12 pol); a especie pede aquario de pelo menos 120 x 30 x 30 cm; deve ser mantida em cardume de ao menos 6 a 8 individuos, de preferencia mais.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 80,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 120,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'trichogaster-lalius' => array(
			'id' => 'trichogaster-lalius',
			'cientifico' => 'Trichogaster lalius',
			'sinonimos' => array(
				'Colisa lalia',
			),
			'populares' => array(
				'colisa',
				'colisa-anão',
				'gurami-anão',
			),
			'familia' => 'Osphronemidae',
			'origem' => 'Asia: Paquistao, India e Bangladesh',
			'porte_cm' => 9.5,
			'porte_medida' => 'TL',
			'cardume' => null,
			'convivencia' => 'casal',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'temp_min' => 25,
			'temp_max' => 28,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4774',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Osphronemidae; max 9,5 cm TL macho/nao sexado; pH 6,0 a 8,0; dH 5 a 19; 25 a 28 C; Asia: Paquistao, India e Bangladesh.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trichogaster-lalius/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 60 x 30 x 30 cm (56 litros) e apenas grande o bastante para UM CASAL, desde que montado corretamente; peixe timido, que pede aquario densamente plantado, substrato escuro e vegetacao flutuante; populacoes selvagens vivem em agua mole e acida.',
				),
			),
			'conflitos' => array(),
		),
		'pterophyllum-scalare' => array(
			'id' => 'pterophyllum-scalare',
			'cientifico' => 'Pterophyllum scalare',
			'sinonimos' => array(),
			'populares' => array(
				'acará-bandeira',
				'bandeira',
				'anjo',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 15,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'convivencia' => 'grupo',
			'comportamento' => 'semi-agressivo',
			'frente_cm' => 100,
			'base_comprimento' => 100,
			'base_largura' => 40,
			'temp_min' => 24,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Pterophyllum-scalare.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 15 cm TL; 24 a 30 C; pH 6,0 a 8,0; dH 5 a 13; secao de aquario: manter em grupos de 5 ou mais individuos, casais em aquario pequeno so para reproducao, aquario minimo de 100 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/pterophyllum-scalare/',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
						'altura_minima_cm',
						'comportamento',
						'alimentacao',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base minima de 100 x 40 x 50 cm, com altura de pelo menos 50 cm para o adulto, e e despropositado sugerir que o adulto caiba em aquario bem menor; ciclideo geralmente pacifico que briga com os proprios, melhor em grupo pequeno; bom peixe comunitario, mas come peixe pequeno como tetras; onivoro, o selvagem come sobretudo pequenos crustaceos e invertebrados aquaticos e o de criadouro aceita racao.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/4717',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae.',
				),
			),
			'conflitos' => array(),
		),
		'xiphophorus-hellerii' => array(
			'id' => 'xiphophorus-hellerii',
			'cientifico' => 'Xiphophorus hellerii',
			'sinonimos' => array(
				'Xiphophorus helleri',
				'Xiphophorus guntheri',
			),
			'populares' => array(
				'espada',
				'espadinha',
				'peixe-espada',
			),
			'familia' => 'Poeciliidae',
			'origem' => '',
			'porte_cm' => 16,
			'porte_medida' => 'TL',
			'cardume' => null,
			'convivencia' => 'harem',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => 120,
			'base_largura' => 30,
			'temp_min' => 22,
			'temp_max' => 28,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-hellerii.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Poeciliidae; macho ate 14,0 cm TL e femea ate 16,0 cm TL; 22 a 28 C; pH 7,0 a 8,0; dH 9 a 19.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/xiphophorus-hellerii/',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 120 x 30 cm ou equivalente e o menor a considerar (volume citado de 108 litros); machos ate 14 cm e femeas ate 16 cm TL; havendo machos e femeas juntos, manter varias femeas para cada macho, porque o assedio do macho e implacavel.',
				),
			),
			'conflitos' => array(),
		),
		'chromobotia-macracanthus' => array(
			'id' => 'chromobotia-macracanthus',
			'cientifico' => 'Chromobotia macracanthus',
			'sinonimos' => array(
				'Botia macracanthus',
				'Botia macracantha',
			),
			'populares' => array(
				'botia-palhaço',
				'botia',
			),
			'familia' => 'Botiidae',
			'origem' => '',
			'porte_cm' => 30.5,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 180,
			'base_comprimento' => 180,
			'base_largura' => 60,
			'temp_min' => 25,
			'temp_max' => 30,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10897',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Botiidae (pointface loaches); max 30,5 cm TL macho/nao sexado; pH 5,0 a 8,0; dH 5 a 12; 25 a 30 C; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 150 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/chromobotia-macracanthus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario com base de 180 x 60 cm ou equivalente e o minimo absoluto para abrigar um grupo (volume citado de 648 litros).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 150,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 150 cm',
						),
						array(
							'valor' => 180,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 180 x 60 cm e o minimo absoluto',
						),
					),
					'razao' => 'Campo de bem-estar: fica o maior, 180 cm. A diferenca entre os dois numeros, na pratica, e de 648 para cerca de 450 litros — nenhum dos dois cabe na sala de quem comprou cinco filhotes de 4 cm.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'astronotus-ocellatus' => array(
			'id' => 'astronotus-ocellatus',
			'cientifico' => 'Astronotus ocellatus',
			'sinonimos' => array(
				'Lobotes ocellatus',
				'Astronotus orbiculatus',
			),
			'populares' => array(
				'oscar',
				'apaiari',
				'acará-açu',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 45.7,
			'porte_medida' => 'TL',
			'cardume' => null,
			'convivencia' => 'solitario',
			'comportamento' => '',
			'frente_cm' => 150,
			'base_comprimento' => 150,
			'base_largura' => 60,
			'temp_min' => 22,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Astronotus-ocellatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae; max 45,7 cm TL; pH 6,0 a 8,0; dH 5 a 19; 22 a 25 C; habita aguas rasas e paradas de fundo de lama ou areia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/astronotus-ocellatus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'convivencia',
						'expectativa_vida_anos',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario com base de 150 x 60 cm e apenas grande o bastante para abrigar UM adulto, e um casal ou grupo exige mais espaco; e peixe de aquario popular, mas o tamanho adulto e a expectativa de vida tipica de 10 a 20 anos tem de ser considerados antes da compra.',
				),
			),
			'conflitos' => array(),
		),
		'carassius-auratus' => array(
			'id' => 'carassius-auratus',
			'cientifico' => 'Carassius auratus',
			'sinonimos' => array(),
			'populares' => array(
				'kinguio',
				'peixe dourado',
				'japonês',
			),
			'familia' => 'Cyprinidae',
			'origem' => '',
			'porte_cm' => 48,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 100,
			'base_comprimento' => null,
			'base_largura' => null,
			'temp_min' => 0,
			'temp_max' => 41,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Carassius-auratus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 48,0 cm TL; faixa termica de 0 a 41 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 100 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/stunted-growth-means-stunted-lives/',
					'em' => '2026-09-09',
					'campos' => array(
						'expectativa_vida_anos',
					),
					'referencia' => 'Seriously Fish — artigo \'Stunted growth means stunted lives\': mantido de forma correta, C. auratus chega a 30 cm e vive 30 ou 40 anos; um kinguio mantido em aquario de 30 x 20 cm pode sobreviver alguns anos e continuar com poucos centimetros, e isso e nanismo severo, nao tamanho natural.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/271',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cyprinidae (minnows, carps).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'porte_adulto_cm',
					'valores' => array(
						array(
							'valor' => 48,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: max 48,0 cm TL',
						),
						array(
							'valor' => 30,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: mantido de forma correta chega a 30 cm',
						),
					),
					'razao' => 'Nao e a mesma grandeza: 48 cm e o maximo registrado da especie e 30 cm e o que se espera em aquario bem mantido. Porte e campo de BIOLOGIA, entao pela tabela dominio_por_campo fica o valor da base cientifica, e o numero do compendio sai publicado do lado porque e ele que descreve o que o leitor vai ter em casa.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
	);
	return $catalogo;
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 2. As páginas desta leva, e as duas promessas da seção 14.9
 *
 * `consulta` é a consulta-alvo, e `porque` é por que esta página consegue
 * chegar às dez primeiras. As duas são obrigatórias e o teste cobra as duas:
 * página que não sabe o que mira não deveria ter nascido.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_registro' ) ) {
function aquametria_peixes_registro() {
	return array(
		'peixes' => array(
			'nivel'    => 1,
			'pai'      => '',
			'titulo'   => 'Quanto espaço cada peixe pede',
			'conteudo' => '[aquametria_peixes_secao]',
			'consulta' => 'quantos litros por peixe aquário',
			'porque'   => 'É a mãe do eixo e existe para o cluster, não para ranquear sozinha: ela recebe a autoridade do menu e do rodapé e passa para as fichas, que são as páginas de consulta. O que ela tem de próprio é o critério — por que a ilha responde em centímetros de base antes de responder em litros.',
		),
		'tetras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Tetras: quantos litros o cardume pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para tetras',
			'porque'   => 'A SERP desta consulta é de blog de nicho sem fonte, e nenhum dos sete primeiros publica a base mínima declarada por espécie numa tabela comparável. Esta página é a tabela: porte, cardume mínimo e frente mínima das sete espécies do banco, lado a lado, com a fonte de cada linha.',
		),
		'quantos-litros-para-tetra-neon' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'paracheirodon-innesi',
			'titulo'   => 'Quantos litros para um cardume de tetra neon?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra neon',
			'porque'   => 'Medido em 12/09/2026: o top 7 é blog de nicho (aquariovivo, chaveinspiradora, aquarioepeixes, peixemania, aquariopedia), uma loja e um portal de artigo. Nenhum é domínio forte, nenhum atribui o número a fonte nomeada e eles discordam entre si (40 L para 8 a 10 neons contra 20 L para 6 a 8). É resposta genérica que não dá número com procedência — o caso que a 14.9 classifica como ALVO.',
		),
		'quantos-litros-para-tetra-cardinal' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'paracheirodon-axelrodi',
			'titulo'   => 'Quantos litros para um cardume de neon cardinal?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para neon cardinal',
			'porque'   => 'Medido em 12/09/2026: o top 9 tem blog de nicho, três lojas e um portal estrangeiro, e o único que declara base (60 × 30 × 30 cm) não diz de onde tirou. Nenhum publica o cardume mínimo de 8 ao lado da base, que é a conta que decide a compra.',
		),
		'quantos-litros-para-mato-grosso' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hyphessobrycon-eques',
			'titulo'   => 'Quantos litros para um cardume de mato-grosso?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para mato grosso peixe',
			'porque'   => 'Medido em 12/09/2026: o top 8 é blog antigo, duas lojas e dois portais de ração, com números que se contradizem na mesma página de resultados — 40 L de mínimo contra 60 L para 6 a 8, cardume de 3 contra cardume de 6, e porte de 3 cm contra 5 cm. É a SERP mais frouxa das três, e a única em que as duas fontes do nosso banco também discordam: a página publica as duas.',
		),

		/* --- LEVA 2, 12/09/2026: as quatro que faltavam para fechar a
		   categoria. Nenhuma URL da leva 1 muda, nenhum endereço se move. --- */

		'quantos-litros-para-tetra-ember' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hyphessobrycon-amandae',
			'titulo'   => 'Quantos litros para um cardume de tetra ember?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra ember',
			'porque'   => 'Medido em 12/09/2026: o top 8 não tem um domínio brasileiro forte — é revista de loja estrangeira (zooplus.pt), blog (blogdopescador), três lojas hispano-americanas, uma ficha de aquarismo e uma loja brasileira. Os números discordam na mesma página de resultados (30 L, 40 L para 10 exemplares, 50 L para 10) e nenhum atribui o número a fonte nomeada. O caso que a 14.9 classifica como ALVO.',
		),
		'quantos-litros-para-tetra-brilhante' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hemigrammus-erythrozonus',
			'titulo'   => 'Quantos litros para um cardume de tetra-brilhante?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra brilhante',
			'porque'   => 'Medido em 12/09/2026: o top 10 é seis lojas (rsdiscus, proaquarista, kauar, barretos, aquastuchi), duas fichas de aquarismo, um portal e um WordPress de 2011. Dão 40, 50 e 60 L sem fonte, e a própria página de resultados mistura outras espécies (tetra gold, neon verde) na resposta — sinal de SERP frouxa. É ALVO, e o registro do nosso banco é o mais bem sustentado da categoria: as duas fontes concordam na frente e divergem em um exemplar de cardume.',
		),
		'quantos-litros-para-rodostomo' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hemigrammus-rhodostomus',
			'titulo'   => 'Quantos litros para um cardume de rodóstomo?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para rodostomo',
			'porque'   => 'Medido em 12/09/2026: o top 9 é três fichas de aquarismo (aquarismopaulista, peixeseaquarismo, blogdopescador) e seis lojas. É a única das sete consultas deste eixo em que alguém do top publica a base (80 × 30 × 40 cm) — e publica sem dizer de onde tirou, ao lado de outra resposta que diz 60 L para o mesmo cardume. Segue ALVO, e aqui a vantagem da ilha não é o ineditismo do número: é a atribuição, e é a página assumir que o fundo NÃO está declarado por ninguém em vez de completá-lo de cabeça.',
		),
		'quantos-litros-para-tetra-negro' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'gymnocorymbus-ternetzi',
			'titulo'   => 'Quantos litros para um cardume de tetra-negro?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra negro',
			'porque'   => 'Medido em 12/09/2026: é a SERP mais disputada das sete deste eixo — tem a Petz, que é domínio forte, ao lado de zooplus.pt, PetMag, aquarismopaulista e três lojas. Segue ALVO porque um domínio forte não é "quase tudo" (14.9) e porque o que ele serve é blog de varejo sem número atribuído: a mesma página de resultados dá 60 L, 70 L e 112 L, e o conselho de "três a seis indivíduos de cada tipo", que é regra de aquário comunitário e não cardume mínimo da espécie. As duas fontes do nosso banco declaram 5 ou mais, e discordam da frente em 15 cm.',
		),

		/* --- LEVA 3, 12/09/2026: a segunda categoria do eixo. A mãe e as
		   QUATRO filhas saem juntas, que é o 16.6 (a categoria inteira, nunca
		   uma filha de cada). Nenhuma URL das levas 1 e 2 muda. --- */

		'corydoras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Coridoras: quanto chão o grupo pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para coridoras',
			'porque'   => 'Medido em 12/09/2026: o top 7 não tem um domínio forte e tem um POST DE GRUPO DO FACEBOOK — três fichas de aquarismo (myaquarium, peixeseaquarismo, peixepedia), um blog de loja estrangeira (tiendanimal.pt), um site que não é de aquarismo (caiaque.net) e a pergunta de um aquarista no Facebook. É a SERP mais frouxa das cinco desta leva. Os números se contradizem na mesma página de resultados — 54 L "para a maioria das espécies", 40 L para um grupo de 3, e "7 litros por cada coridora que você adicionar" — e o terceiro é justamente a conta per capita que esta ilha se recusa a fazer desde a leva 1, publicada ali como se fosse regra. Ela vale a categoria inteira: é a página que explica por que coridora se dimensiona por CHÃO e não por litro, e as quatro fichas pendem dela.',
		),
		'quantos-litros-para-coridora-bronze' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-aeneus',
			'titulo'   => 'Quantos litros para um cardume de coridora bronze?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora bronze',
			'porque'   => 'Medido em 12/09/2026: o top 8 é uma ficha de aquarismo forte no nicho (aquarismopaulista), o aquaonline, o blogdopescador e cinco lojas (proaquarista duas vezes, fazendasubmersa, myaquarium). Nenhum domínio forte de fora do nicho. A contradição está dentro da mesma página de resultados: "60 x 30 x 40 cm (72 litros)", "60 litros no mínimo" e "70 litros comportam com folga cinco coridoras" — e a última briga com o cardume de 6 que a mesma resposta declara duas linhas acima. Nenhum atribui o número. O nosso registro é o que pede MAIS espaço da categoria (80 x 30 cm, Seriously Fish), e a página ganha por assumir isso com o nome da fonte em vez de competir por baixo.',
		),
		'quantos-litros-para-coridora-pimenta' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-paleatus',
			'titulo'   => 'Quantos litros para um cardume de coridora pimenta?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora pimenta',
			'porque'   => 'Medido em 12/09/2026: o top 9 é seis lojas (rioaqua, aquaverso.pt, aquariumcrystal, aquastuchi, rsdiscus, proaquarista), duas fichas de aquarismo e um portal generalista de 2010 (culturamix). Duas lojas do top vendem a espécie com nomes populares diferentes — "pimenta" e "mármore" — o que reparte a própria SERP. Os números discordam (60 x 30 x 30 cm contra "mínimo 70 litros") e nenhum diz de onde saiu. É a única das quatro em que o nosso banco tem CONFLITO declarado de frente (60 cm na FishBase, 61 no compêndio), e a ficha publica os dois com a atribuição de cada um — que é exatamente o que o top 9 não faz.',
		),
		'quantos-litros-para-coridora-panda' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-panda',
			'titulo'   => 'Quantos litros para um cardume de coridora panda?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora panda',
			'porque'   => 'Medido em 12/09/2026: o top 8 é blog (blogdopescador), duas fichas de aquarismo (aquarismopaulista, myaquarium), um Blogspot de 2006 e quatro lojas (rsdiscus, fazendasubmersa, proaquarista, rolizoo). Nenhum domínio forte. Eles dão "60 litros para 5 a 6" e "60 x 30 x 30 cm (54 litros)" na mesma resposta, que são dois números diferentes para a mesma pergunta, e nenhum é atribuído. Aqui a vantagem da ilha é incomum e vale dizer: o nosso número é MENOR que o do top — 45 x 30 cm declarados pelo compêndio contra os 60 cm que a SERP repete —, e é o registro que sustenta o aquário de 30 a 40 litros sem mentir. Número menor com fonte nomeada é mais difícil de publicar que número maior, e é o que a página faz.',
		),
		'quantos-litros-para-coridora-sterbai' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-sterbai',
			'titulo'   => 'Quantos litros para um cardume de coridora sterbai?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora sterbai',
			'porque'   => 'Medido em 12/09/2026: o top 10 é o aquaonline, o blogdopescador, duas fichas de aquarismo e seis lojas (fazendasubmersa duas vezes, rsdiscus, proaquarista, myaquarium). Nenhum domínio forte, e é a SERP mais contraditória das cinco: a mesma página de resultados dá 54 L, 90 L "para um grupo de seis" e "70 litros comportam com folga cinco" — três respostas para uma pergunta só, nenhuma com fonte. É também a ficha que esta leva destravou: até 12/09 o cardume mínimo desta espécie era null no banco e ela não podia virar página, porque ficha que se chama "quantos litros para um cardume" e não sabe o cardume abre a tabela em um exemplar. O número veio da ficha da própria espécie no compêndio, por busca restrita, e o registro guarda a recusa da alternativa fácil ao lado dele.',
		),
	);
}
}

/* Os nomes de nível 2 do eixo, na ordem do ARVORE.md seção 3. Categoria só
   nasce com 3 filhas de dado real (16.5); as outras cinco ficam sem link e sem
   contagem, que é o que a regra manda. A pertinência é por ESPÉCIE, escrita
   aqui: derivar "tetra" da família daria a lista errada nas duas direções — o
   banco tem tetra em Acestrorhamphidae e em Characidae ao mesmo tempo (nota de
   taxonomia do próprio banco), e Characidae também carrega quem o comércio
   brasileiro não vende como tetra. */
if ( ! function_exists( 'aquametria_peixes_categorias' ) ) {
function aquametria_peixes_categorias() {
	return array(
		'tetras' => array(
			'rotulo'  => 'Tetras',
			'plural'  => 'tetras',
			'linha_mestra' => 'Tetra pequeno não quer dizer aquário pequeno: o que decide o mínimo do seu aquário é o cardume, e não o tamanho do peixe.',
			'criterio' => 'As espécies que a loja brasileira vende como tetra: os Paracheirodon, os Hemigrammus, os Hyphessobrycon e o Gymnocorymbus. A família não serve de critério aqui — a revisão recente dos caracídeos deixou o banco com tetra em duas famílias diferentes, e Characidae carrega peixe que ninguém vende como tetra.',
			'especies' => array(
				'paracheirodon-innesi',
				'paracheirodon-axelrodi',
				'hyphessobrycon-amandae',
				'hyphessobrycon-eques',
				'hemigrammus-erythrozonus',
				'hemigrammus-rhodostomus',
				'gymnocorymbus-ternetzi',
			),
		),
		'corydoras' => array(
			'rotulo'   => 'Corydoras',
			'plural'   => 'coridoras',
			'linha_mestra' => 'Coridora é peixe de fundo, e peixe de fundo se mede pelo chão: o que decide o mínimo do seu aquário é quantos centímetros de base o grupo tem para vasculhar, não quantos litros cabem em cima.',
			'criterio' => 'Os peixes de fundo que a loja brasileira vende como coridora, da subfamília Corydoradinae. O gênero Corydoras não serve de critério, e aqui pelo motivo oposto ao dos tetras: a revisão recente da subfamília tirou as quatro do gênero na própria fonte — a ficha já publica Hoplisoma panda, Hoplisoma paleatum, Hoplisoma sterbai e Osteogaster aenea —, então filtrar por Corydoras devolveria lista vazia para uma categoria que o aquarista brasileiro compra pelo nome todo dia. O banco guarda os dois nomes de cada uma e esta página serve os dois.',
			'especies' => array(
				'corydoras-aeneus',
				'corydoras-paleatus',
				'corydoras-panda',
				'corydoras-sterbai',
			),
		),
		'bettas' => array(
			'rotulo'   => 'Bettas e gouramis',
			'criterio' => '',
			'especies' => array(),
		),
		'ciclideos-anoes' => array(
			'rotulo'   => 'Ciclídeos anões',
			'criterio' => '',
			'especies' => array(),
		),
		'plecos-e-limpa-vidros' => array(
			'rotulo'   => 'Plecos e limpa-vidros',
			'criterio' => '',
			'especies' => array(),
		),
		'vivaparos' => array(
			'rotulo'   => 'Vivíparos',
			'criterio' => '',
			'especies' => array(),
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 3. A aritmética — toda ela derivada, nenhuma gravada
 * ------------------------------------------------------------------------- */

/**
 * A faixa de porte de uma espécie: [min, max] em cm.
 *
 * Igual nos dois extremos quando não há divergência declarada; os dois valores
 * do conflito quando há. Quem escolhe o extremo é quem CONSOME: para lotação
 * vale o peixe maior, porque errar para cima de carga é o lado seguro.
 */
if ( ! function_exists( 'aquametria_peixes_porte_faixa' ) ) {
function aquametria_peixes_porte_faixa( $e ) {
	$valores = array( (float) $e['porte_cm'] );
	foreach ( (array) $e['conflitos'] as $c ) {
		if ( 'porte_adulto_cm' !== $c['campo'] ) {
			continue;
		}
		foreach ( (array) $c['valores'] as $v ) {
			if ( is_numeric( $v['valor'] ) ) {
				$valores[] = (float) $v['valor'];
			}
		}
	}
	return array( min( $valores ), max( $valores ) );
}
}

/**
 * O portão de PÁGINA, deste lado — decisão 8 do cabeçalho.
 *
 * Estar no catálogo não basta para ter página própria: a ficha deste eixo se
 * chama "quantos litros para um cardume de X" e abre pela frase que nomeia o
 * cardume mínimo. Espécie que o banco declara de cardume ou de grupo SEM o
 * número não passa. Quem declara convivência solitário, casal ou harém passa
 * sem o número — ali a ausência é a declaração, não o buraco.
 *
 * A régua está ESCRITA aqui e não importada do gerador de catálogo. É a mesma
 * frase que o esquema usa (`minimo_para_sugerir.pagina-especie`), e é o teste
 * que cobra que as duas digam o mesmo — se este arquivo chamasse a régua de
 * quem produziu o dado, as duas metades errariam juntas (seção 8 do contrato).
 */
if ( ! function_exists( 'aquametria_peixes_pode_virar_ficha' ) ) {
function aquametria_peixes_pode_virar_ficha( $e ) {
	if ( ! empty( $e['cardume'] ) ) {
		return true;
	}
	return in_array( $e['convivencia'], array( 'solitario', 'casal', 'harem' ), true );
}
}

/**
 * A faixa de frente mínima declarada: [min, max] em cm. Mesma regra do porte,
 * e aqui o extremo seguro é o MAIOR — aquário maior nunca fez mal a cardume.
 */
if ( ! function_exists( 'aquametria_peixes_frente_faixa' ) ) {
function aquametria_peixes_frente_faixa( $e ) {
	$valores = array( (float) $e['frente_cm'] );
	foreach ( (array) $e['conflitos'] as $c ) {
		if ( 'comprimento_minimo_aquario_cm' !== $c['campo'] ) {
			continue;
		}
		foreach ( (array) $c['valores'] as $v ) {
			if ( is_numeric( $v['valor'] ) ) {
				$valores[] = (float) $v['valor'];
			}
		}
	}
	return array( min( $valores ), max( $valores ) );
}
}

/**
 * A leitura per capita do mínimo declarado: frente mínima ÷ cardume mínimo.
 *
 * Derivado `frente_por_individuo_cm` do esquema. Sai na tela como leitura, e
 * NUNCA multiplicado para extrapolar cardume — ver decisão 2 do cabeçalho.
 * Devolve null quando a espécie não declara cardume (solitário, casal, harém).
 */
if ( ! function_exists( 'aquametria_peixes_frente_por_individuo' ) ) {
function aquametria_peixes_frente_por_individuo( $e ) {
	if ( empty( $e['cardume'] ) ) {
		return null;
	}
	$frente = aquametria_peixes_frente_faixa( $e );
	return $frente[1] / (float) $e['cardume'];
}
}

/** Volume bruto da lâmina, em litros: a conta de C1, antes de vidro e substrato. */
if ( ! function_exists( 'aquametria_peixes_volume_bruto' ) ) {
function aquametria_peixes_volume_bruto( $comprimento_cm, $largura_cm, $altura_cm ) {
	if ( ! $comprimento_cm || ! $largura_cm || ! $altura_cm ) {
		return null;
	}
	return ( (float) $comprimento_cm * (float) $largura_cm * (float) $altura_cm ) / 1000.0;
}
}

/** As três alturas comuns de aquário que a tabela varre. A fonte declara base, nunca altura. */
if ( ! function_exists( 'aquametria_peixes_alturas' ) ) {
function aquametria_peixes_alturas() {
	return array( 30, 35, 40 );
}
}

/**
 * Litros que N exemplares pedem, pelos três critérios brasileiros.
 * Recebe a soma dos comprimentos adultos em cm e devolve os três números.
 */
if ( ! function_exists( 'aquametria_peixes_litros_por_criterio' ) ) {
function aquametria_peixes_litros_por_criterio( $soma_cm ) {
	$soma_cm = (float) $soma_cm;
	return array(
		'classica'     => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_CLASSICA,
		'meio'         => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_MEIO,
		'conservadora' => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA,
	);
}
}

/**
 * Quantos exemplares caberiam num volume, pelos três critérios. É a pergunta
 * inversa, e é a que a pessoa faz de verdade quando já tem o aquário.
 */
if ( ! function_exists( 'aquametria_peixes_quantos_cabem' ) ) {
function aquametria_peixes_quantos_cabem( $litros, $porte_cm ) {
	if ( ! $litros || ! $porte_cm ) {
		return array();
	}
	$litros  = (float) $litros;
	$porte   = (float) $porte_cm;
	return array(
		'classica'     => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA ) / $porte ),
		'meio'         => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_MEIO ) / $porte ),
		'conservadora' => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA ) / $porte ),
	);
}
}

/** Os cardumes que a tabela pré-renderizada varre, sempre incluindo o mínimo declarado. */
if ( ! function_exists( 'aquametria_peixes_degraus_de_cardume' ) ) {
function aquametria_peixes_degraus_de_cardume( $e ) {
	$minimo = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : 1;
	$degraus = array( $minimo );
	foreach ( array( 6, 8, 10, 12, 15, 20 ) as $n ) {
		if ( $n > $minimo ) {
			$degraus[] = $n;
		}
	}
	sort( $degraus );
	return array_values( array_unique( $degraus ) );
}
}

/**
 * Quem divide a MESMA ÁGUA: interseção das faixas de temperatura declaradas.
 *
 * NÃO é veredito de convivência — ver decisão 5 do cabeçalho. Três condições,
 * todas medidas em campo declarado:
 *   1. a faixa de temperatura encosta na da espécie da página em 2 °C ou mais;
 *   2. a frente mínima declarada do companheiro cabe na frente da página, ou
 *      seja: o aquário mínimo desta ficha também serve para ele;
 *   3. o banco não declara o companheiro agressivo.
 *
 * Devolve array( 'dentro' => ids, 'maior' => ids, 'agressivos' => ids ), porque
 * a página deve ao leitor o nome de quem ficou de fora e por qual das duas
 * causas (seção 7: causa que o código separa, o texto separa).
 */
if ( ! function_exists( 'aquametria_peixes_mesma_agua' ) ) {
function aquametria_peixes_mesma_agua( $id ) {
	$catalogo = aquametria_peixes_catalogo();
	if ( ! isset( $catalogo[ $id ] ) ) {
		return array( 'dentro' => array(), 'maior' => array(), 'agressivos' => array() );
	}
	$alvo   = $catalogo[ $id ];
	$frente = aquametria_peixes_frente_faixa( $alvo );

	$dentro     = array();
	$maior      = array();
	$agressivos = array();

	foreach ( $catalogo as $outro_id => $o ) {
		if ( $outro_id === $id ) {
			continue;
		}
		$sobreposicao = min( (float) $alvo['temp_max'], (float) $o['temp_max'] )
			- max( (float) $alvo['temp_min'], (float) $o['temp_min'] );
		if ( $sobreposicao < 2 ) {
			continue;
		}
		if ( 'agressivo' === $o['comportamento'] ) {
			$agressivos[] = $outro_id;
			continue;
		}
		$frente_outro = aquametria_peixes_frente_faixa( $o );
		if ( $frente_outro[1] > $frente[1] ) {
			$maior[] = $outro_id;
			continue;
		}
		$dentro[ $outro_id ] = $sobreposicao;
	}

	/* Ordem: maior sobreposição primeiro, e entre iguais o peixe menor antes —
	   afinidade declarada, nunca sorteio (16.4c). */
	uksort( $dentro, function ( $a, $b ) use ( $dentro, $catalogo ) {
		if ( $dentro[ $a ] !== $dentro[ $b ] ) {
			return ( $dentro[ $a ] < $dentro[ $b ] ) ? 1 : -1;
		}
		$pa = (float) $catalogo[ $a ]['porte_cm'];
		$pb = (float) $catalogo[ $b ]['porte_cm'];
		if ( $pa === $pb ) {
			return strcmp( $a, $b );
		}
		return ( $pa > $pb ) ? 1 : -1;
	} );

	return array(
		'dentro'     => array_keys( $dentro ),
		'maior'      => $maior,
		'agressivos' => $agressivos,
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. Texto: nome, número e unidade
 * ------------------------------------------------------------------------- */

/**
 * Como a espécie vive, na língua de quem compra.
 *
 * O banco guarda `cardume`, `grupo`, `solitario`, `casal`, `harem` — vocabulário
 * de campo do esquema, não de tela. A tradução é palavra por palavra e não
 * acrescenta juízo nenhum: o que a fonte declarou continua sendo o que a tela
 * diz. Termo que não estiver no mapa sai como veio, porque inventar tradução
 * para valor novo é pior que mostrar o valor cru.
 */
if ( ! function_exists( 'aquametria_peixes_como_vive' ) ) {
function aquametria_peixes_como_vive( $e ) {
	$convivencia = array(
		'cardume'   => 'em cardume',
		'grupo'     => 'em grupo',
		'solitario' => 'sozinho',
		'casal'     => 'em casal',
		'harem'     => 'em harém, uma macho para várias fêmeas',
	);
	$comportamento = array(
		'pacifico'  => 'pacífico',
		'agressivo' => 'agressivo',
	);

	$texto = isset( $convivencia[ $e['convivencia'] ] ) ? $convivencia[ $e['convivencia'] ] : $e['convivencia'];
	if ( $e['comportamento'] ) {
		$c = isset( $comportamento[ $e['comportamento'] ] ) ? $comportamento[ $e['comportamento'] ] : $e['comportamento'];
		$texto .= ', e a fonte o declara ' . $c;
	}
	return $texto;
}
}

/** O nome que a pessoa digita: o primeiro popular do banco. */
if ( ! function_exists( 'aquametria_peixes_nome' ) ) {
function aquametria_peixes_nome( $e ) {
	return isset( $e['populares'][0] ) ? $e['populares'][0] : $e['cientifico'];
}
}

/** Número com vírgula decimal e sem zero à direita inútil. */
if ( ! function_exists( 'aquametria_peixes_num' ) ) {
function aquametria_peixes_num( $v, $casas = 1 ) {
	if ( null === $v ) {
		return '—';
	}
	$v = (float) $v;
	if ( abs( $v - round( $v ) ) < 0.05 ) {
		return number_format_i18n( round( $v ), 0 );
	}
	return number_format_i18n( $v, $casas );
}
}

/** "2,2 cm" ou "2,5 a 3,0 cm" quando a fonte discorda. */
if ( ! function_exists( 'aquametria_peixes_faixa_texto' ) ) {
function aquametria_peixes_faixa_texto( $faixa, $unidade = 'cm' ) {
	if ( abs( $faixa[0] - $faixa[1] ) < 0.01 ) {
		return aquametria_peixes_num( $faixa[0] ) . ' ' . $unidade;
	}
	return aquametria_peixes_num( $faixa[0] ) . ' a ' . aquametria_peixes_num( $faixa[1] ) . ' ' . $unidade;
}
}

/**
 * O nome de um campo do banco, na língua de quem lê — e a unidade dele.
 *
 * `comprimento_minimo_aquario_cm` é nome de campo de esquema, e ele chegou a
 * sair na tela do bloco de divergência antes desta função existir. Campo que
 * não estiver no mapa sai como veio, de propósito: nome cru é feio e avisa,
 * enquanto nome inventado engana.
 */
if ( ! function_exists( 'aquametria_peixes_campo_na_tela' ) ) {
function aquametria_peixes_campo_na_tela( $campo ) {
	$mapa = array(
		'porte_adulto_cm'               => array( 'o porte adulto', 'cm' ),
		'comprimento_minimo_aquario_cm' => array( 'a frente mínima do aquário', 'cm' ),
		'base_minima_cm'                => array( 'a base mínima do aquário', 'cm' ),
		'temperatura_C'                 => array( 'a temperatura', '°C' ),
		'cardume_minimo'                => array( 'o cardume mínimo', 'exemplares' ),
		'ph'                            => array( 'o pH', '' ),
		'dureza_dgh'                    => array( 'a dureza da água', 'dGH' ),
		'expectativa_vida_anos'         => array( 'a expectativa de vida', 'anos' ),
	);
	return isset( $mapa[ $campo ] ) ? $mapa[ $campo ] : array( $campo, '' );
}
}

/** dd/mm/aaaa a partir da data ISO do banco. */
if ( ! function_exists( 'aquametria_peixes_data_br' ) ) {
function aquametria_peixes_data_br( $iso ) {
	$partes = explode( '-', (string) $iso );
	if ( 3 !== count( $partes ) ) {
		return (string) $iso;
	}
	return $partes[2] . '/' . $partes[1] . '/' . $partes[0];
}
}

/** O corpo de fonte que sustenta um campo, com a data. '' quando nenhum sustenta. */
if ( ! function_exists( 'aquametria_peixes_fonte_do_campo' ) ) {
function aquametria_peixes_fonte_do_campo( $e, $campo ) {
	foreach ( (array) $e['fontes'] as $f ) {
		if ( in_array( $campo, (array) $f['campos'], true ) ) {
			return $f;
		}
	}

	/* Duas substituições declaradas, e as duas são do MESMO fato colhido:
	   - o nome científico é nomeado por quem classifica a espécie, e no banco
	     quem sustenta `familia` é o corpo taxonômico. Sem esta linha a ficha
	     dizia "sem fonte que sustente" para o nome científico que a própria
	     FishBase publicou, o que é falso na direção pior — a de parecer que a
	     ilha não sabe de onde veio o dado que ela tem;
	   - a frente mínima e a base mínima são o mesmo número lido de dois jeitos
	     (comprimento, ou comprimento × largura), e há registro em que a fonte
	     declara só um dos dois campos. */
	$substitutos = array(
		'nome_cientifico'               => 'familia',
		'comprimento_minimo_aquario_cm' => 'base_minima_cm',
		'base_minima_cm'                => 'comprimento_minimo_aquario_cm',
	);
	if ( isset( $substitutos[ $campo ] ) ) {
		foreach ( (array) $e['fontes'] as $f ) {
			if ( in_array( $substitutos[ $campo ], (array) $f['campos'], true ) ) {
				return $f;
			}
		}
	}

	return array();
}
}

/* ---------------------------------------------------------------------------
 * 5. A ficha de espécie (nível 3)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_ficha_html' ) ) {
function aquametria_peixes_ficha_html( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ]['especie'] ) ) {
		return '';
	}
	$catalogo = aquametria_peixes_catalogo();
	$id       = $registro[ $slug ]['especie'];
	if ( ! isset( $catalogo[ $id ] ) ) {
		/* Espécie que saiu do portão de página some da tela em vez de servir
		   ficha pela metade. Página sem corpo é página fina, e o teste reprova. */
		return '';
	}
	if ( ! aquametria_peixes_pode_virar_ficha( $catalogo[ $id ] ) ) {
		/* Decisão 8: espécie de cardume sem o número do cardume não vira ficha.
		   Devolver vazio aqui é o mesmo tratamento de quem sai do catálogo —
		   página sem corpo é página fina, e o portão do teste reprova antes de
		   a URL nascer. */
		return '';
	}
	$e      = $catalogo[ $id ];
	$nome   = aquametria_peixes_nome( $e );
	$porte  = aquametria_peixes_porte_faixa( $e );
	$frente = aquametria_peixes_frente_faixa( $e );
	$larg   = $e['base_largura'] ? (float) $e['base_largura'] : null;
	$card   = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : null;

	$html = '<div class="aqm-px aqm-px-ficha">';

	/* --- 5.1 A resposta antes da explicação (seção 5, item 2). Frase
	   autossuficiente: sobrevive a ser citada fora de contexto. --- */
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">';
	if ( $card ) {
		$html .= 'Para os ' . esc_html( $card ) . ' ' . esc_html( $nome )
			. ' que a fonte declara como cardume mínimo, o seu aquário precisa de '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm de frente';
	} else {
		$html .= 'Para o ' . esc_html( $nome ) . ', o seu aquário precisa de '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm de frente';
	}
	if ( $larg ) {
		$html .= ' por ' . esc_html( aquametria_peixes_num( $larg ) )
			. ' cm de fundo — e a fonte declara a BASE, não o litro.</p>';
	} else {
		/* Decisão 7: a frase tem o escopo do que foi medido. Aqui a fonte
		   declarou o comprimento e não disse uma palavra sobre o fundo, então
		   a página não pode dizer "base" — em 14 dos 36 registros do banco é
		   exatamente esse o caso. */
		$html .= ' — e a fonte declara o COMPRIMENTO do aquário, não o litro.</p>';
	}

	$alturas = aquametria_peixes_alturas();
	$litros_alturas = array();
	foreach ( $alturas as $a ) {
		$v = aquametria_peixes_volume_bruto( $frente[1], $larg, $a );
		if ( null !== $v ) {
			$litros_alturas[ $a ] = $v;
		}
	}
	if ( $litros_alturas ) {
		$primeira = min( array_keys( $litros_alturas ) );
		$ultima   = max( array_keys( $litros_alturas ) );
		/* O contraexemplo é CALCULADO, não escolhido: o cubo de mesmo volume é o
		   aquário com a menor frente possível para aquele litro, então ele é o
		   pior caso honesto — e a diferença em centímetros sai da subtração, não
		   de uma fração escrita à mão. */
		$cubo = pow( $litros_alturas[ $ultima ] * 1000, 1 / 3 );
		$html .= '<p>Essa base dá de ' . esc_html( aquametria_peixes_num( $litros_alturas[ $primeira ] ) )
			. ' litros a ' . esc_html( aquametria_peixes_num( $litros_alturas[ $ultima ] ) )
			. ' litros de lâmina, conforme a altura do aquário ser '
			. esc_html( aquametria_peixes_num( $primeira ) ) . ' ou '
			. esc_html( aquametria_peixes_num( $ultima ) ) . ' cm. '
			. 'E é por isso que responder só em litros engana: um aquário cúbico de '
			. esc_html( aquametria_peixes_num( $litros_alturas[ $ultima ] ) ) . ' litros tem '
			. esc_html( aquametria_peixes_num( $cubo ) ) . ' cm de lado — o litro certo e '
			. esc_html( aquametria_peixes_num( $frente[1] - $cubo ) )
			. ' cm de frente a menos do que este cardume pede.</p>';
	} else {
		/* Decisão 7, a outra metade: sem o fundo declarado, as duas tabelas que
		   dependem dele não saem — e a página DIZ que não saíram e por quê. A
		   versão anterior deste código simplesmente encolhia, e quem lesse não
		   tinha como distinguir "a ilha não sabe" de "a ilha esqueceu". */
		$html .= '<p class="aqm-px-sem-fundo"><strong>O fundo do aquário, esta página não tem como dizer — e isso é o que a fonte declarou, não um buraco nosso.</strong> '
			. 'Para o ' . esc_html( $nome ) . ' a fonte publica o comprimento mínimo e para aí: não há largura declarada por ninguém. '
			. 'Sem os dois lados do chão não existe litro, então aqui não sai a tabela de litros por altura nem a de quantos cabem no aquário mínimo — elas sairiam de um fundo que a gente teria inventado. '
			. 'O que a página responde com o que está medido é a outra metade, e ela está logo abaixo: quantos litros o cardume pede pelas duas réguas brasileiras de lotação, que partem do comprimento dos peixes e não do chão do aquário.</p>';
	}

	/* A camada de prova: fonte pelo nome e data, um parágrafo abaixo (15.2). */
	$fonte_frente = aquametria_peixes_fonte_do_campo( $e, 'comprimento_minimo_aquario_cm' );
	if ( ! $fonte_frente ) {
		$fonte_frente = aquametria_peixes_fonte_do_campo( $e, 'base_minima_cm' );
	}
	$html .= '<p class="aqm-prova">';
	if ( $fonte_frente ) {
		$html .= 'Quem declara ' . ( $larg ? 'essa base' : 'esse comprimento' ) . ' é o '
			. esc_html( $fonte_frente['corpo'] )
			. ', na ficha da espécie, colhido em ' . esc_html( aquametria_peixes_data_br( $fonte_frente['em'] ) ) . '. ';
	}
	if ( count( (array) $e['conflitos'] ) ) {
		$html .= 'Esta espécie tem divergência declarada entre fontes, e ela está publicada mais abaixo com o nome de quem disse cada número. ';
	}
	$html .= 'A página não foi lida direto: o egresso da nuvem barra os domínios das duas fontes, então cada número veio de busca restrita ao domínio — está na lista de reconferência da ilha.</p>';
	$html .= '</div>';

	/* --- 5.2 Quantos litros para N exemplares: a tabela pré-renderizada
	   (seção 5, item 1). É o que um modelo de linguagem lê sem preencher
	   formulário, e é a metade em que o erro é mais caro (seção 7). --- */
	$html .= '<h2>Quantos litros para N ' . esc_html( $nome ) . '</h2>';
	$html .= '<p>A base declarada é o piso do aquário; quem responde "e para dez?" são as duas réguas de lotação que circulam no aquarismo brasileiro. Elas discordam em quatro vezes, e a Aquametria publica as duas com o nome de quem disse cada uma em vez de tirar média.</p>';
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
	$html .= '<caption>Litros para um cardume de ' . esc_html( $nome )
		. ', pelas duas réguas brasileiras. O porte adulto usado é '
		. esc_html( aquametria_peixes_faixa_texto( $porte ) )
		. ( abs( $porte[0] - $porte[1] ) > 0.01 ? ' — a coluna usa o extremo maior, porque errar carga para cima é o lado seguro' : '' )
		. '.</caption>';
	$html .= '<thead><tr><th scope="col">Exemplares</th><th scope="col">Soma dos comprimentos</th>'
		. '<th scope="col">Regra clássica (1 cm/L)</th><th scope="col">Critério intermediário (1,5 L/cm)</th>'
		. '<th scope="col">Critério conservador (4 L/cm)</th></tr></thead><tbody>';
	foreach ( aquametria_peixes_degraus_de_cardume( $e ) as $n ) {
		$soma = $n * $porte[1];
		$l    = aquametria_peixes_litros_por_criterio( $soma );
		$marca = ( $card && $n === $card ) ? ' class="aqm-px-linha-minima"' : '';
		$html .= '<tr' . $marca . '><th scope="row">' . esc_html( $n )
			. ( ( $card && $n === $card ) ? ' (cardume mínimo)' : '' ) . '</th>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $soma ) ) . ' cm</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['classica'] ) ) . ' L</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['meio'] ) ) . ' L</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['conservadora'] ) ) . ' L</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="aqm-prova">A regra clássica de 1 cm de peixe por litro e o critério de 1,5 a 4 litros por cm de peixe saíram do levantamento de fontes brasileiras da ilha, em 04/09/2026, e as duas são publicadas com a ressalva das próprias fontes: elas contam comprimento e ignoram massa, formato e carga biológica. A "regra dos 10 %" ficou de fora porque nenhuma das fontes diz 10 % de quê.</p>';

	/* --- 5.3 O inverso: quantos cabem na base declarada. --- */
	if ( $litros_alturas ) {
		$html .= '<h2>E quantos ' . esc_html( $nome ) . ' cabem no aquário mínimo</h2>';
		$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
		$html .= '<caption>A base de ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' × '
			. esc_html( aquametria_peixes_num( $larg ) ) . ' cm em três alturas de aquário. '
			. 'O litro é o bruto da lâmina, antes de descontar vidro e substrato — a conta cheia está na calculadora de litragem.</caption>';
		$html .= '<thead><tr><th scope="col">Altura</th><th scope="col">Litros brutos</th>'
			. '<th scope="col">Pela regra clássica</th><th scope="col">Pelo intermediário</th>'
			. '<th scope="col">Pelo conservador</th></tr></thead><tbody>';
		foreach ( $litros_alturas as $a => $v ) {
			$q = aquametria_peixes_quantos_cabem( $v, $porte[1] );
			$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_num( $a ) ) . ' cm</th>';
			$html .= '<td>' . esc_html( aquametria_peixes_num( $v ) ) . ' L</td>';
			$html .= '<td>' . esc_html( $q['classica'] ) . '</td>';
			$html .= '<td>' . esc_html( $q['meio'] ) . '</td>';
			$html .= '<td>' . esc_html( $q['conservadora'] ) . '</td>';
			$html .= '</tr>';
		}
		$html .= '</tbody></table></div>';
		$meio_altura = $alturas[1];
		if ( isset( $litros_alturas[ $meio_altura ] ) ) {
			$q = aquametria_peixes_quantos_cabem( $litros_alturas[ $meio_altura ], $porte[1] );
			$html .= '<p>Traduzindo a linha do meio: no aquário mínimo com '
				. esc_html( aquametria_peixes_num( $meio_altura ) ) . ' cm de altura cabem '
				. esc_html( $q['conservadora'] ) . ' ' . esc_html( $nome )
				. ' pelo critério apertado e ' . esc_html( $q['classica'] )
				. ' pelo critério folgado. A diferença entre os dois é de '
				. esc_html( aquametria_peixes_num( AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA ) )
				. ' vezes, e é assim que as fontes brasileiras estão. Quem está montando o primeiro aquário faz melhor ficando perto do número apertado: o que sobra de espaço vira margem para o dia em que a filtragem falhar.</p>';
		}
	}

	/* --- 5.4 O que a fonte declara, campo por campo. --- */
	$html .= '<h2>O que as fontes declaram sobre o ' . esc_html( $nome ) . '</h2>';
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela aqm-px-declarado">';
	$html .= '<caption>Cada linha com o corpo que a sustenta e a data em que foi colhida.</caption>';
	$html .= '<thead><tr><th scope="col">O que</th><th scope="col">Declarado</th><th scope="col">Quem declara</th></tr></thead><tbody>';

	$linhas = array(
		array( 'Nome científico', esc_html( $e['cientifico'] ), 'nome_cientifico' ),
		array( 'Porte adulto', esc_html( aquametria_peixes_faixa_texto( $porte ) ) . ' (' . esc_html( $e['porte_medida'] ) . ')', 'porte_adulto_cm' ),
		array( 'Temperatura', esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' a ' . esc_html( aquametria_peixes_num( $e['temp_max'] ) ) . ' °C', 'temperatura_C' ),
		array( 'Frente mínima do aquário', esc_html( aquametria_peixes_faixa_texto( $frente ) ), 'comprimento_minimo_aquario_cm' ),
		array( 'Como vive', esc_html( aquametria_peixes_como_vive( $e ) ), 'convivencia' ),
	);
	if ( $card ) {
		$linhas[] = array( 'Cardume mínimo', esc_html( $card ) . ' exemplares', 'cardume_minimo' );
	}
	if ( $e['origem'] ) {
		$linhas[] = array( 'De onde vem', esc_html( $e['origem'] ), 'origem_geografica' );
	}
	foreach ( $linhas as $linha ) {
		$f = aquametria_peixes_fonte_do_campo( $e, $linha[2] );
		$html .= '<tr><th scope="row">' . $linha[0] . '</th><td>' . $linha[1] . '</td><td>';
		if ( $f ) {
			$html .= esc_html( $f['corpo'] ) . ', ' . esc_html( aquametria_peixes_data_br( $f['em'] ) );
		} else {
			$html .= 'sem fonte que sustente — e por isso não entra em conta nenhuma';
		}
		$html .= '</td></tr>';
	}
	$html .= '</tbody></table></div>';

	$por_individuo = aquametria_peixes_frente_por_individuo( $e );
	if ( null !== $por_individuo ) {
		$html .= '<p>Dividindo o mínimo declarado pelo cardume mínimo dá '
			. esc_html( aquametria_peixes_num( $por_individuo ) )
			. ' cm de frente por exemplar — e esse número serve para comparar espécies, não para multiplicar. '
			. 'Os ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm que a fonte declara são o espaço de onde o cardume consegue nadar em cardume, não o preço de '
			. esc_html( $card ) . ' peixes: multiplicar diria que dez ' . esc_html( $nome ) . ' precisam de '
			. esc_html( aquametria_peixes_num( $por_individuo * 10 ) ) . ' cm, o que nenhuma fonte sustenta.</p>';
	}

	/* --- 5.5 A divergência, publicada com os dois nomes. --- */
	if ( count( (array) $e['conflitos'] ) ) {
		$html .= '<h2>Onde as fontes discordam</h2>';
		$html .= '<p>A Aquametria nunca tira média de fontes que discordam: publica os dois extremos com o nome de quem disse cada um. '
			. 'E onde o número entra numa conta desta página, vale o extremo seguro — aquário maior, peixe maior —, porque errar espaço para cima não machuca ninguém.</p>';
		foreach ( (array) $e['conflitos'] as $c ) {
			list( $rotulo_campo, $unidade ) = aquametria_peixes_campo_na_tela( $c['campo'] );
			$html  .= '<p><strong>Sobre ' . esc_html( $rotulo_campo ) . ':</strong> ';
			$partes = array();
			foreach ( (array) $c['valores'] as $v ) {
				$valor = $v['valor'];
				if ( is_array( $valor ) ) {
					$valor = aquametria_peixes_num( isset( $valor['min'] ) ? $valor['min'] : null )
						. ' a ' . aquametria_peixes_num( isset( $valor['max'] ) ? $valor['max'] : null );
				} else {
					$valor = aquametria_peixes_num( $valor );
				}
				$partes[] = esc_html( trim( $valor . ' ' . $unidade ) ) . ' pelo ' . esc_html( $v['fonte'] );
			}
			$html .= implode( ', e ', $partes ) . '. ';

			/* Qual extremo esta página usou, e onde. A razão escrita no banco NÃO
			   vem para cá de propósito: ela é nota interna, escrita sem acento e
			   no vocabulário do esquema ("campo de manutenção"), e texto de tela
			   desta ilha sai acentuado e na língua de quem compra. O que o leitor
			   precisa saber é qual número a conta usou — e isso a página sabe
			   dizer sozinha, porque é ela que escolhe. */
			if ( 'comprimento_minimo_aquario_cm' === $c['campo'] || 'base_minima_cm' === $c['campo'] ) {
				$html .= '<span class="aqm-px-razao">As contas desta página usam '
					. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm, o maior dos dois.</span>';
			} elseif ( 'porte_adulto_cm' === $c['campo'] ) {
				$html .= '<span class="aqm-px-razao">As tabelas de lotação desta página usam '
					. esc_html( aquametria_peixes_num( $porte[1] ) ) . ' cm, o maior dos dois.</span>';
			} else {
				$html .= '<span class="aqm-px-razao">Este número não entra em nenhuma conta desta página; está aqui porque o banco registrou a divergência e esconder divergência é escolher um lado em silêncio.</span>';
			}
			$html .= '</p>';
		}
	}

	/* --- 5.6 Quem divide a mesma água. Critério na frente da lista (14.4). --- */
	$vizinhos = aquametria_peixes_mesma_agua( $id );

	/* ESPÉCIE QUE O BANCO DECLARA AGRESSIVA NÃO GANHA LISTA DE COMPANHEIRO, e
	   isto não é excesso de zelo: o filtro da função acima tira o companheiro
	   agressivo da lista, e não olhava o peixe da PRÓPRIA ficha. Na primeira
	   versão desta página o mato-grosso — que a FishBase declara agressivo —
	   servia tetra ember e tetra neon na tabela de quem divide a água, com uma
	   nota dizendo que não era veredito de convivência. Nota não desfaz tabela:
	   quem lê vê a lista, não a ressalva.
	   E a saída honesta não é uma lista menor, é NÃO publicar lista: o esquema
	   do banco recusa compatibilidade como campo justamente porque ela depende
	   de volume, layout e ordem de introdução, e para peixe agressivo é aí que
	   a resposta mora. Então a página conta o que mediu (quantas espécies do
	   banco dividem a faixa) e diz por que não recomenda nenhuma. */
	if ( 'agressivo' === $e['comportamento'] ) {
		$total_faixa = count( $vizinhos['dentro'] ) + count( $vizinhos['maior'] ) + count( $vizinhos['agressivos'] );
		$html .= '<h2>Com quem esse cardume divide o aquário</h2>';
		$html .= '<p>Esta ficha <strong>não publica lista de companheiro</strong>, e a razão está duas tabelas acima: a fonte declara o '
			. esc_html( $nome ) . ' <strong>agressivo</strong>. '
			. esc_html( $total_faixa ) . ' das ' . esc_html( count( aquametria_peixes_catalogo() ) )
			. ' espécies do banco dividem faixa de temperatura com ele, e nenhuma delas vira recomendação por causa disso: '
			. 'temperatura é o que a gente mediu, e convivência com peixe agressivo depende do volume, do layout e da ordem em que os peixes entram no aquário — nada disso cabe numa tabela, e o banco desta ilha não guarda compatibilidade como campo justamente por isso.</p>';
		$html .= '<p class="aqm-px-fora">O que dá para dizer com o que está medido: quanto mais espaço além dos '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm mínimos, e quanto maior o cardume, menos a agressão se concentra num alvo só — '
			. 'é a mesma razão por que a fonte declara cardume mínimo de ' . esc_html( $card ) . ' e não de dois.</p>';
	} elseif ( $vizinhos['dentro'] ) {
		$html .= '<h2>Quem divide a mesma faixa de temperatura</h2>';
		$html .= '<p>Isto não é veredito de convivência, e a diferença importa: o que está medido aqui é a <strong>interseção das faixas de temperatura declaradas</strong>, com dois filtros a mais — o aquário mínimo do companheiro cabe nos '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm desta ficha, e o banco não o declara agressivo. '
			. 'Quem decide convivência de verdade é o volume, o layout e a ordem em que os peixes entram, e isso nenhuma tabela resolve.</p>';
		$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela"><caption>Espécies do banco cuja faixa declarada encosta na do '
			. esc_html( $nome ) . ' em 2 °C ou mais.</caption>';
		$html .= '<thead><tr><th scope="col">Espécie</th><th scope="col">Temperatura declarada</th>'
			. '<th scope="col">Onde as duas faixas se encontram</th>'
			. '<th scope="col">Porte adulto</th><th scope="col">Frente mínima</th></tr></thead><tbody>';
		$catalogo = aquametria_peixes_catalogo();
		foreach ( $vizinhos['dentro'] as $outro_id ) {
			$o  = $catalogo[ $outro_id ];
			$op = aquametria_peixes_porte_faixa( $o );
			$of = aquametria_peixes_frente_faixa( $o );
			$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_nome( $o ) )
				. ' <span class="aqm-px-cientifico">' . esc_html( $o['cientifico'] ) . '</span></th>';
			$html .= '<td>' . esc_html( aquametria_peixes_num( $o['temp_min'] ) ) . ' a '
				. esc_html( aquametria_peixes_num( $o['temp_max'] ) ) . ' °C</td>';
			/* A largura da interseção sai na tela de propósito: sem ela, a
			   espécie que só encosta em 2 °C fica com a mesma cara de quem
			   compartilha a faixa inteira, e o leitor não tem como ver a
			   diferença. Coluna que mostra o quanto a afirmação é folgada é o
			   contrário de colher cereja. */
			$html .= '<td>' . esc_html( aquametria_peixes_num( max( (float) $e['temp_min'], (float) $o['temp_min'] ) ) )
				. ' a ' . esc_html( aquametria_peixes_num( min( (float) $e['temp_max'], (float) $o['temp_max'] ) ) )
				. ' °C</td>';
			$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( $op ) ) . '</td>';
			$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( $of ) ) . '</td></tr>';
		}
		$html .= '</tbody></table></div>';

		/* Prestação de contas: quem ficou de fora, e por qual das duas causas
		   (seção 7 — causa que o código separa, o texto separa). */
		$html .= '<p class="aqm-px-fora">';
		$total_faixa = count( $vizinhos['dentro'] ) + count( $vizinhos['maior'] ) + count( $vizinhos['agressivos'] );
		$html .= 'Entre as ' . esc_html( $total_faixa ) . ' espécies do banco com faixa de temperatura que encosta na do '
			. esc_html( $nome ) . ', ' . esc_html( count( $vizinhos['dentro'] ) ) . ' estão na tabela acima. ';
		if ( $vizinhos['maior'] ) {
			$nomes = array();
			foreach ( $vizinhos['maior'] as $outro_id ) {
				$of = aquametria_peixes_frente_faixa( $catalogo[ $outro_id ] );
				$nomes[] = aquametria_peixes_nome( $catalogo[ $outro_id ] ) . ' (' . aquametria_peixes_num( $of[1] ) . ' cm)';
			}
			$html .= esc_html( count( $vizinhos['maior'] ) ) . ' ficaram fora por pedir aquário mais largo que esta ficha: '
				. esc_html( implode( ', ', $nomes ) ) . '. ';
		}
		if ( $vizinhos['agressivos'] ) {
			$nomes = array();
			foreach ( $vizinhos['agressivos'] as $outro_id ) {
				$nomes[] = aquametria_peixes_nome( $catalogo[ $outro_id ] );
			}
			$html .= esc_html( count( $vizinhos['agressivos'] ) ) . ' ficaram fora porque o banco os declara agressivos: '
				. esc_html( implode( ', ', $nomes ) ) . '. ';
		}
		$html .= '</p>';
	}

	/* --- 5.7 O equipamento que este cardume pede — o 16.4(d), e o caminho do
	   dinheiro. A vitrine não mora aqui: mora na calculadora. --- */
	$html .= '<h2>O equipamento que esse aquário pede</h2>';
	$html .= '<p>';
	$url_c1 = aquametria_casca_url_se_existir( 'calculadora-de-litragem' );
	$url_c5 = aquametria_casca_url_se_existir( 'calculadora-de-potencia-do-aquecedor' );
	$url_c3 = aquametria_casca_url_se_existir( 'calculadora-de-vazao-do-filtro' );
	if ( '' !== $url_c1 ) {
		$html .= 'O litro bruto da tabela acima não é a água que você vai tratar: vidro e substrato comem uma parte, e a '
			. '<a href="' . esc_url( $url_c1 ) . '">conta dos litros</a> devolve os três números com as suas medidas. ';
	}
	if ( '' !== $url_c5 ) {
		$html .= 'O ' . esc_html( $nome ) . ' pede água entre '
			. esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' e '
			. esc_html( aquametria_peixes_num( $e['temp_max'] ) )
			. ' °C, e quanto de aquecedor isso custa depende do frio que faz no seu cômodo — é a '
			. '<a href="' . esc_url( $url_c5 ) . '">conta dos watts</a>. ';
	}
	if ( '' !== $url_c3 ) {
		$html .= 'Cardume come e cardume suja, então a vazão do filtro sai da '
			. '<a href="' . esc_url( $url_c3 ) . '">conta do filtro</a>, com a faixa que os fabricantes declaram.';
	}
	$html .= '</p>';
	$html .= '<p class="aqm-px-sem-loja"><strong>Nesta página não tem link de loja, e isso é decisão, não esquecimento.</strong> '
		. 'Peixe vivo não se compra por link de afiliado — quem vende é a loja da sua cidade, e a Aquametria não tem como conferir o lote nem a aclimatação de ninguém. '
		. 'O equipamento tem link, e ele está dentro das calculadoras acima, onde o produto entra como consequência do número que você calculou.</p>';

	/* --- 5.8 A mãe no corpo, e as irmãs. 16.4(b) e 16.4(c). --- */
	$html .= aquametria_peixes_frase_de_mae_html( $slug );

	/* --- 5.9 A consulta-alvo e a classificação da SERP, no corpo, porque quem
	   confere a 14.9 é quem lê a página. --- */
	$html .= '<p class="aqm-px-consulta">Esta página mira a consulta <strong>“'
		. esc_html( $registro[ $slug ]['consulta'] ) . '”</strong>. A SERP dessa consulta foi classificada em '
		. esc_html( AQUAMETRIA_PEIXES_SERP_EM ) . ' antes de a página nascer, como manda o critério da ilha, e a classificação está escrita no snippet que serve esta página.</p>';

	$html .= '</div>';

	return $html;
}
}

/**
 * A frase do corpo que linka a mãe — o 16.4(b), a metade que não é breadcrumb.
 *
 * As IRMÃS não saem daqui: quem publica o bloco "Veja também" é a casca, para
 * toda página da ilha, e duas marcações para o mesmo cluster viram dois CSS e,
 * mais cedo do que se pensa, duas aparências. O que este snippet faz é dizer à
 * casca quem são as irmãs, pelo filtro `aquametria_peixes`.
 *
 * A frase só sai com mãe PUBLICADA. Frase apontando para página inexistente é
 * link morto, e o portão cobra a ausência dela justamente para ninguém fechar
 * isso com um endereço inventado.
 */
if ( ! function_exists( 'aquametria_peixes_frase_de_mae_html' ) ) {
function aquametria_peixes_frase_de_mae_html( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return '';
	}
	$pai = $registro[ $slug ]['pai'];
	if ( '' === $pai || ! isset( $registro[ $pai ] ) ) {
		return '';
	}
	$url_pai = aquametria_casca_url_se_existir( $pai );
	if ( '' === $url_pai ) {
		return '';
	}

	$irmas = aquametria_peixes_irmas( $slug );
	if ( 3 === $registro[ $slug ]['nivel'] ) {
		return '<p class="aqm-px-mae">Esta é uma das ' . esc_html( count( $irmas ) + 1 )
			. ' fichas de <a href="' . esc_url( $url_pai ) . '">'
			. esc_html( $registro[ $pai ]['titulo'] ) . '</a>, onde a mesma conta aparece para todas elas na mesma tabela.</p>';
	}

	return '<p class="aqm-px-mae">Esta lista é uma das categorias de <a href="'
		. esc_url( $url_pai ) . '">' . esc_html( $registro[ $pai ]['titulo'] )
		. '</a>, que é onde o critério inteiro da ilha para este assunto está escrito.</p>';
}
}

/** As irmãs de uma página do eixo: mesma mãe, no registro, nunca digitadas. */
if ( ! function_exists( 'aquametria_peixes_irmas' ) ) {
function aquametria_peixes_irmas( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return array();
	}
	$pai   = $registro[ $slug ]['pai'];
	$irmas = array();
	foreach ( $registro as $outro => $def ) {
		if ( $outro === $slug || $def['pai'] !== $pai || '' === $pai ) {
			continue;
		}
		$irmas[] = $outro;
	}
	return $irmas;
}
}

/* ---------------------------------------------------------------------------
 * 6. A categoria (nível 2) — listagem com critério próprio, nunca grade de links
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_categoria_html' ) ) {
function aquametria_peixes_categoria_html( $slug ) {
	$categorias = aquametria_peixes_categorias();
	if ( ! isset( $categorias[ $slug ] ) ) {
		return '';
	}
	$cat      = $categorias[ $slug ];
	$catalogo = aquametria_peixes_catalogo();
	$registro = aquametria_peixes_registro();

	$dentro = array();
	foreach ( $cat['especies'] as $id ) {
		if ( isset( $catalogo[ $id ] ) ) {
			$dentro[ $id ] = $catalogo[ $id ];
		}
	}

	$com_ficha = array();
	foreach ( $registro as $s => $def ) {
		if ( isset( $def['especie'] ) && isset( $dentro[ $def['especie'] ] ) ) {
			$com_ficha[ $def['especie'] ] = $s;
		}
	}

	/* O SUBSTANTIVO DA CATEGORIA VEM DECLARADO, e isto é conserto de um defeito
	   que o portão pegou nesta leva antes de ir ao ar: a abertura dizia "São N
	   tetras" com o "tetras" digitado, e a página das coridoras serviu "São 4
	   tetras" na primeira renderização. A contagem estava certa e o substantivo
	   mentia — a forma mais silenciosa do número de tela que envelhece, porque
	   aqui nem número era. Enquanto houve uma categoria só, digitado e derivado
	   eram indistinguíveis; a segunda separou os dois. */
	$html  = '<div class="aqm-px aqm-px-categoria">';
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">' . esc_html( $cat['linha_mestra'] ) . '</p>';
	$html .= '<p>São ' . esc_html( count( $dentro ) ) . ' '
		. esc_html( $cat['plural'] )
		. ' com aquário mínimo declarado por fonte com nome e data, e o mínimo vai de '
		. esc_html( aquametria_peixes_num( aquametria_peixes_menor_frente( $dentro ) ) ) . ' a '
		. esc_html( aquametria_peixes_num( aquametria_peixes_maior_frente( $dentro ) ) )
		. ' cm de frente — com o cardume mínimo indo de '
		. esc_html( aquametria_peixes_menor_cardume( $dentro ) ) . ' a '
		. esc_html( aquametria_peixes_maior_cardume( $dentro ) )
		. ' exemplares. A tabela abaixo põe os dois números lado a lado, que é a comparação que nenhuma das respostas de busca desta consulta publica.</p>';
	$html .= '</div>';

	$html .= '<h2>' . esc_html( ucfirst( $cat['plural'] ) ) . ' do banco, com o mínimo declarado de cada um</h2>';
	$html .= '<p class="aqm-px-criterio"><strong>O critério desta lista:</strong> ' . esc_html( $cat['criterio'] ) . '</p>';
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
	$html .= '<caption>Porte adulto, cardume mínimo e frente mínima declarada. Onde as fontes discordam, a coluna traz os dois extremos.</caption>';
	$html .= '<thead><tr><th scope="col">Espécie</th><th scope="col">Porte adulto</th>'
		. '<th scope="col">Cardume mínimo</th><th scope="col">Frente mínima</th>'
		. '<th scope="col">Temperatura</th><th scope="col">A conta inteira</th></tr></thead><tbody>';

	/* Ordem: frente mínima crescente, e entre iguais o peixe menor antes. Quem
	   procura "tetra para aquário pequeno" lê de cima para baixo. */
	uasort( $dentro, function ( $a, $b ) {
		$fa = aquametria_peixes_frente_faixa( $a );
		$fb = aquametria_peixes_frente_faixa( $b );
		if ( $fa[1] !== $fb[1] ) {
			return ( $fa[1] > $fb[1] ) ? 1 : -1;
		}
		if ( (float) $a['porte_cm'] === (float) $b['porte_cm'] ) {
			return strcmp( $a['id'], $b['id'] );
		}
		return ( (float) $a['porte_cm'] > (float) $b['porte_cm'] ) ? 1 : -1;
	} );

	foreach ( $dentro as $id => $e ) {
		$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_nome( $e ) )
			. ' <span class="aqm-px-cientifico">' . esc_html( $e['cientifico'] ) . '</span></th>';
		$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( aquametria_peixes_porte_faixa( $e ) ) ) . '</td>';
		$html .= '<td>' . ( $e['cardume'] ? esc_html( $e['cardume'] ) : 'não declarado' ) . '</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( aquametria_peixes_frente_faixa( $e ) ) ) . '</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' a '
			. esc_html( aquametria_peixes_num( $e['temp_max'] ) ) . ' °C</td>';
		$html .= '<td>';
		if ( isset( $com_ficha[ $id ] ) ) {
			$url = aquametria_casca_url_se_existir( $com_ficha[ $id ] );
			if ( '' !== $url ) {
				/* Âncora = o TÍTULO da filha, que nesta ilha é a pergunta que a
				   pessoa digita — é o que o 16.4(a) pede e é o mesmo nome que a
				   filha usa na trilha, no H1 e no <title>. */
				$html .= '<a href="' . esc_url( $url ) . '">'
					. esc_html( $registro[ $com_ficha[ $id ] ]['titulo'] ) . '</a>';
			} else {
				$html .= 'em breve';
			}
		} else {
			$html .= 'em breve';
		}
		$html .= '</td></tr>';
	}
	$html .= '</tbody></table></div>';

	/* Prestação de contas da listagem: quantas têm página, quantas esperam. A
	   frase muda de forma quando a fila zera, porque "0 estão na fila, e a
	   próxima leva sai depois" é uma promessa sobre uma leva que não existe. */
	$na_fila = count( $dentro ) - count( $com_ficha );
	$html .= '<p class="aqm-px-fora">';
	if ( $na_fila > 0 ) {
		$html .= 'Das ' . esc_html( count( $dentro ) ) . ' espécies da tabela, '
			. esc_html( count( $com_ficha ) ) . ' já têm a conta inteira numa página própria e '
			. esc_html( $na_fila )
			. ' estão na fila. A ordem não é alfabética nem por gosto: sai primeiro a que mais gente procura, e a próxima leva sai depois de medirmos se estas foram indexadas.';
	} else {
		$html .= 'As ' . esc_html( count( $dentro ) )
			. ' espécies da tabela têm a conta inteira numa página própria — esta lista está fechada, e fechada quer dizer que todo tetra que o banco desta ilha sustenta com duas fontes já tem a página dele. '
			. 'A lista cresce quando o banco crescer, não quando der vontade de escrever: espécie sem duas fontes de corpos distintos não entra na tabela, e espécie de cardume sem o número do cardume declarado não ganha página, porque a página começa justamente por esse número.';
	}
	$html .= '</p>';

	$html .= '<h2>Por que a gente responde em centímetros antes de responder em litros</h2>';
	$html .= '<p>Quem pergunta "quantos litros para dez neons" quer um número, e a resposta honesta tem duas partes. '
		. 'A primeira é a base: as fontes de aquarismo declaram o tamanho do <strong>chão</strong> do aquário, porque é ele que decide se o cardume nada em cardume ou fica encolhido num canto. '
		. 'A segunda é a lotação, e aí entram as duas réguas brasileiras que discordam em quatro vezes. '
		. 'Um aquário alto e estreito pode ter o litro certo e o chão errado — e é por isso que a tabela acima tem a coluna em centímetros.</p>';

	$html .= aquametria_peixes_frase_de_mae_html( $slug );
	$html .= '<p class="aqm-px-consulta">Esta página mira a consulta <strong>“'
		. esc_html( $registro[ $slug ]['consulta'] ) . '”</strong>, e a SERP dela foi classificada em '
		. esc_html( AQUAMETRIA_PEIXES_SERP_EM ) . ' antes de a página nascer.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_peixes_menor_frente' ) ) {
function aquametria_peixes_menor_frente( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		$f = aquametria_peixes_frente_faixa( $e );
		$v = ( null === $v ) ? $f[1] : min( $v, $f[1] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_maior_frente' ) ) {
function aquametria_peixes_maior_frente( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		$f = aquametria_peixes_frente_faixa( $e );
		$v = ( null === $v ) ? $f[1] : max( $v, $f[1] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_menor_cardume' ) ) {
function aquametria_peixes_menor_cardume( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		if ( empty( $e['cardume'] ) ) {
			continue;
		}
		$v = ( null === $v ) ? (int) $e['cardume'] : min( $v, (int) $e['cardume'] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_maior_cardume' ) ) {
function aquametria_peixes_maior_cardume( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		if ( empty( $e['cardume'] ) ) {
			continue;
		}
		$v = ( null === $v ) ? (int) $e['cardume'] : max( $v, (int) $e['cardume'] );
	}
	return $v;
}
}

/* ---------------------------------------------------------------------------
 * 7. A seção (nível 1)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_secao_html' ) ) {
function aquametria_peixes_secao_html() {
	$catalogo   = aquametria_peixes_catalogo();
	$categorias = aquametria_peixes_categorias();
	$registro   = aquametria_peixes_registro();

	$com_ficha = 0;
	foreach ( $registro as $def ) {
		if ( isset( $def['especie'] ) && isset( $catalogo[ $def['especie'] ] ) ) {
			$com_ficha++;
		}
	}

	$html  = '<div class="aqm-px aqm-px-secao">';
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">O número que decide se o peixe cabe no seu aquário é o tamanho do chão, em centímetros — não o litro. E é isso que quase nenhuma resposta de busca diz.</p>';
	$html .= '<p>São ' . esc_html( count( $catalogo ) ) . ' espécies de água doce com o mínimo declarado por fonte com nome e data. '
		. 'Para cada uma, a ilha publica o que a fonte declarou (a base do aquário e o cardume mínimo) e o que as duas réguas brasileiras de lotação calculam para o número de peixes que você quer — que discordam em quatro vezes entre si. '
		. 'As duas coisas na mesma tela, com o nome de quem disse cada número.</p>';
	$html .= '</div>';

	$html .= '<h2>Por onde começar</h2>';
	$html .= '<ul class="aqm-px-cats">';
	foreach ( $categorias as $slug => $cat ) {
		$url = '';
		if ( $cat['especies'] ) {
			$url = aquametria_casca_url_se_existir( $slug );
		}
		$html .= '<li class="aqm-px-cat">';
		if ( '' !== $url ) {
			$html .= '<h3><a href="' . esc_url( $url ) . '">'
				. esc_html( isset( $registro[ $slug ]['titulo'] ) ? $registro[ $slug ]['titulo'] : $cat['rotulo'] )
				. '</a></h3>';
			$quantas = 0;
			foreach ( $cat['especies'] as $id ) {
				if ( isset( $catalogo[ $id ] ) ) {
					$quantas++;
				}
			}
			$html .= '<p>' . esc_html( $quantas ) . ' espécies com o mínimo declarado, da menor frente para a maior.</p>';
		} else {
			/* Categoria sem as 3 filhas de dado real não é link e não mostra
			   contagem: é a regra 16.5, e ela existe para categoria vazia não
			   entrar no índice de domínio novo como página fina. */
			$html .= '<h3>' . esc_html( $cat['rotulo'] ) . '</h3>';
			$html .= '<p><span class="aqm-tag">Em breve</span></p>';
		}
		$html .= '</li>';
	}
	$html .= '</ul>';

	$html .= '<h2>O que esta parte do site responde</h2>';
	$html .= '<p>Uma pergunta só, e ela tem duas metades. A primeira: <strong>qual é o aquário mínimo desta espécie</strong> — e a resposta vem em centímetros de frente e de fundo, porque é assim que os compêndios de aquarismo declaram. '
		. 'A segunda: <strong>quantos exemplares cabem no aquário que você tem</strong> — e aí a resposta é uma faixa, porque as fontes brasileiras de lotação vão de 1 cm de peixe por litro até 4 litros por cm de peixe, e isso é quatro vezes de diferença para o mesmo peixe no mesmo aquário.</p>';
	$html .= '<p>A ilha não escolhe uma das duas réguas para você. Ela publica as duas com a atribuição de cada extremo e diz o que cada uma ignora — as duas contam comprimento e nenhuma conta massa, formato ou carga biológica. '
		. 'Onde o banco não tem fonte que preste, a ficha diz que não tem, em vez de chutar um número redondo.</p>';
	$html .= '<p class="aqm-prova">' . esc_html( $com_ficha ) . ' espécies têm ficha própria no ar hoje, e a contagem desta frase é feita na hora de imprimir a página, não digitada. '
		. 'Todo número do banco veio de busca restrita ao domínio da fonte, porque o egresso da nuvem barra a leitura direta das duas bases usadas — é reconferência em aberto, e está escrita na nota do banco.</p>';

	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. Shortcodes — a página se reconhece pelo SLUG
 *
 * Pelo slug e não pelo atributo do shortcode: os cinco corpos são
 * `[aquametria_peixes_ficha]` sem parâmetro nenhum, então não existe o caso de
 * alguém editar a página no wp-admin e passar o id de outra espécie.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_slug_atual' ) ) {
function aquametria_peixes_slug_atual() {
	$registro = aquametria_peixes_registro();

	/* Na bancada o slug chega pelo global, como nos outros renderizadores. */
	if ( ! empty( $GLOBALS['__slug_pagina'] ) && isset( $registro[ $GLOBALS['__slug_pagina'] ] ) ) {
		return $GLOBALS['__slug_pagina'];
	}
	if ( ! function_exists( 'is_singular' ) || ! is_singular() ) {
		return null;
	}
	$pagina = get_post();
	if ( ! $pagina || empty( $pagina->post_name ) ) {
		return null;
	}
	return isset( $registro[ $pagina->post_name ] ) ? $pagina->post_name : null;
}
}

add_shortcode( 'aquametria_peixes_ficha', function () {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return '';
	}
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_ficha_html( $slug );
} );

add_shortcode( 'aquametria_peixes_categoria', function () {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return '';
	}
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_categoria_html( $slug );
} );

add_shortcode( 'aquametria_peixes_secao', function () {
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_secao_html();
} );

/* ---------------------------------------------------------------------------
 * 9. A casca: as páginas e a árvore
 *
 * Quem cria página é a casca (1.7.0), pelo filtro `aquametria_paginas`. Quem
 * diz onde cada uma mora na árvore é o filtro `aquametria_peixes`, no mesmo
 * molde do hub de calculadoras e da prateleira de guias: a casca não guarda
 * cópia de título nenhum, e página nova aparece na trilha sozinha.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_registrar_paginas' ) ) {
function aquametria_peixes_registrar_paginas( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		$paginas = array();
	}
	foreach ( aquametria_peixes_registro() as $slug => $def ) {
		$paginas[ $slug ] = array(
			'titulo'   => $def['titulo'],
			'conteudo' => $def['conteudo'],
			'pai'      => $def['pai'],
		);
	}
	return $paginas;
}
}
add_filter( 'aquametria_paginas', 'aquametria_peixes_registrar_paginas' );

if ( ! function_exists( 'aquametria_peixes_registrar_arvore' ) ) {
function aquametria_peixes_registrar_arvore( $lista ) {
	if ( ! is_array( $lista ) ) {
		$lista = array();
	}
	$categorias = aquametria_peixes_categorias();
	foreach ( aquametria_peixes_registro() as $slug => $def ) {
		$cat = ( 3 === $def['nivel'] && isset( $categorias[ $def['pai'] ] ) )
			? array( $def['pai'], $categorias[ $def['pai'] ]['rotulo'] )
			: array();
		$lista[ $slug ] = array(
			'nivel'  => $def['nivel'],
			'pai'    => $def['pai'],
			'rotulo' => $def['titulo'],
			'nivel2' => $cat,
		);
	}
	return $lista;
}
}
add_filter( 'aquametria_peixes', 'aquametria_peixes_registrar_arvore' );

/* ---------------------------------------------------------------------------
 * 10. Estilo e JSON-LD — os dois no wp_head, nunca no retorno do shortcode
 *
 * Classes NOVAS de propósito (aqm-px-*). A ilha já pagou duas rodadas de teste
 * por reaproveitar classe que um teste de navegador usa como localizador.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_css' ) ) {
function aquametria_peixes_css() {
	return <<<'CSS'
.aqm-px{--px-tinta:var(--aqm-tinta,#0D1B22);--px-lamina:var(--aqm-lamina,#0E7C8C);
--px-papel:var(--aqm-papel,#F4F7F7);--px-superficie:var(--aqm-superficie,#FFFFFF);
--px-traco:var(--aqm-traco,#DDE5E6);--px-legenda:var(--aqm-legenda,#5C7075);
--px-alerta:var(--aqm-alerta,#B5762A);
--px-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--px-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--px-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
font-family:var(--px-texto);color:var(--px-tinta);max-width:56rem;}
.aqm-px h2{font-family:var(--px-display);font-size:1.18rem;font-weight:600;
margin:2rem 0 .6rem;line-height:1.3;}
.aqm-px p{line-height:1.65;margin:0 0 .9rem;}
.aqm-px-direta{background:var(--px-papel);border:1px dashed var(--px-traco);
border-radius:3px;padding:1rem 1.1rem;margin:0 0 1.4rem;font-size:.96rem;}
.aqm-px-direta p:last-child{margin-bottom:0;}
.aqm-px-linha-mestra{font-family:var(--px-display);font-size:1.1rem;font-weight:600;
line-height:1.35;}
.aqm-px-rolagem{overflow-x:auto;margin:0 0 1rem;}
.aqm-px-tabela{border-collapse:collapse;width:100%;font-size:.88rem;
background:var(--px-superficie);}
.aqm-px-tabela caption{caption-side:top;text-align:left;font-size:.8rem;
color:var(--px-legenda);padding:0 0 .5rem;line-height:1.5;}
.aqm-px-tabela th,.aqm-px-tabela td{border:1px solid var(--px-traco);
padding:.42rem .55rem;text-align:left;vertical-align:top;}
.aqm-px-tabela thead th{font-family:var(--px-texto);font-weight:600;font-size:.8rem;
background:var(--px-papel);}
.aqm-px-tabela td{font-family:var(--px-mono);font-variant-numeric:tabular-nums;}
.aqm-px-tabela tbody th{font-weight:500;}
.aqm-px-linha-minima td,.aqm-px-linha-minima th{background:var(--px-papel);}
.aqm-px-cientifico{display:block;font-family:var(--px-mono);font-size:.72rem;
font-style:italic;color:var(--px-legenda);}
.aqm-px-criterio,.aqm-px-fora,.aqm-px-sem-loja{font-size:.86rem;
color:var(--px-legenda);border-left:2px solid var(--px-traco);
padding:.1rem 0 .1rem .7rem;}
.aqm-px-sem-loja{border-left-color:var(--px-alerta);}
.aqm-px-razao{display:block;font-size:.84rem;color:var(--px-legenda);margin:.2rem 0 0;}
.aqm-px-consulta{font-family:var(--px-mono);font-size:.76rem;color:var(--px-legenda);
border-top:1px solid var(--px-traco);margin:1.4rem 0 0;padding:.6rem 0 0;}
.aqm-px-irmas,.aqm-px-cats{list-style:none;padding:0;margin:0 0 1.2rem;}
.aqm-px-irmas li{border-bottom:1px solid var(--px-traco);padding:.5rem 0;}
.aqm-px-cats{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:.8rem;}
.aqm-px-cat{border:1px solid var(--px-traco);border-radius:3px;padding:.8rem .9rem;
background:var(--px-superficie);}
.aqm-px-cat h3{font-family:var(--px-display);font-size:.98rem;margin:0 0 .4rem;}
.aqm-px-cat p{font-size:.84rem;color:var(--px-legenda);margin:0;}
.aqm-px a{color:var(--px-lamina);}
@media (max-width:600px){.aqm-px-direta{font-size:.92rem;padding:.85rem .9rem;}
.aqm-px-tabela{font-size:.82rem;}}
CSS;
}
}

if ( ! function_exists( 'aquametria_peixes_estilo_impresso' ) ) {
function aquametria_peixes_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_peixes_imprimir_estilo' ) ) {
function aquametria_peixes_imprimir_estilo() {
	if ( aquametria_peixes_estilo_impresso() ) {
		return;
	}
	aquametria_peixes_estilo_impresso( true );
	echo '<style id="aquametria-peixes-estilo">' . "\n" . aquametria_peixes_css() . "\n" . '</style>' . "\n";
}
}

/**
 * O JSON-LD de cada página do eixo.
 *
 * Ficha: Article + FAQPage, porque o H1 É a pergunta e a resposta está servida
 * no HTML. NÃO é Product — espécie não é produto, e declarar Product sem preço
 * nem disponibilidade é schema inválido com cara de válido.
 * Seção e categoria: CollectionPage + ItemList com as filhas que EXISTEM
 * publicadas, pelo mesmo motivo de o breadcrumb não carregar degrau sem
 * endereço: item de lista sem URL é lista pior, não lista maior.
 */
if ( ! function_exists( 'aquametria_peixes_jsonld_dados' ) ) {
function aquametria_peixes_jsonld_dados( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return array();
	}
	$def  = $registro[ $slug ];
	$url  = aquametria_casca_url_se_existir( $slug );
	$nos  = array();

	if ( 3 === $def['nivel'] && isset( $def['especie'] ) ) {
		$catalogo = aquametria_peixes_catalogo();
		if ( ! isset( $catalogo[ $def['especie'] ] ) ) {
			return array();
		}
		$e      = $catalogo[ $def['especie'] ];
		$nome   = aquametria_peixes_nome( $e );
		$porte  = aquametria_peixes_porte_faixa( $e );
		$frente = aquametria_peixes_frente_faixa( $e );
		$card   = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : null;
		$larg   = $e['base_largura'] ? (float) $e['base_largura'] : null;

		$resposta = 'O aquário mínimo declarado para o ' . $nome . ' é de '
			. aquametria_peixes_num( $frente[1] ) . ' cm de frente'
			. ( $larg ? ' por ' . aquametria_peixes_num( $larg ) . ' cm de fundo' : '' )
			. ( $card ? ', para o cardume mínimo de ' . $card . ' exemplares' : '' ) . '.';
		$v35 = aquametria_peixes_volume_bruto( $frente[1], $larg, 35 );
		if ( null !== $v35 ) {
			$resposta .= ' Com 35 cm de altura isso dá ' . aquametria_peixes_num( $v35 )
				. ' litros brutos de lâmina.';
		}
		$fonte = aquametria_peixes_fonte_do_campo( $e, 'comprimento_minimo_aquario_cm' );
		if ( ! $fonte ) {
			$fonte = aquametria_peixes_fonte_do_campo( $e, 'base_minima_cm' );
		}
		if ( $fonte ) {
			$resposta .= ' Declarado pelo ' . $fonte['corpo'] . ', colhido em '
				. aquametria_peixes_data_br( $fonte['em'] ) . '.';
		}

		$perguntas = array(
			array( $def['titulo'], $resposta ),
		);
		if ( $card ) {
			$l = aquametria_peixes_litros_por_criterio( $card * $porte[1] );
			$perguntas[] = array(
				'Quantos litros para ' . $card . ' ' . $nome . '?',
				$card . ' ' . $nome . ' somam ' . aquametria_peixes_num( $card * $porte[1] )
					. ' cm de peixe adulto. Pela regra clássica brasileira de 1 cm por litro isso pede '
					. aquametria_peixes_num( $l['classica'] ) . ' litros; pelo critério conservador de 4 litros por cm, '
					. aquametria_peixes_num( $l['conservadora'] )
					. ' litros. A Aquametria publica os dois extremos com a atribuição de cada um em vez de tirar média.',
			);
		}
		$perguntas[] = array(
			'Qual é a temperatura do ' . $nome . '?',
			'As fontes declaram de ' . aquametria_peixes_num( $e['temp_min'] ) . ' a '
				. aquametria_peixes_num( $e['temp_max'] ) . ' °C para o ' . $nome
				. ' (' . $e['cientifico'] . ').',
		);

		$faq = array();
		foreach ( $perguntas as $p ) {
			$faq[] = array(
				'@type'          => 'Question',
				'name'           => $p[0],
				'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
			);
		}

		$artigo = array(
			'@type'         => 'Article',
			'headline'      => $def['titulo'],
			'about'         => array(
				'@type' => 'Thing',
				'name'  => $nome,
				'alternateName' => $e['cientifico'],
			),
			'inLanguage'    => 'pt-BR',
			'isAccessibleForFree' => true,
		);
		if ( '' !== $url ) {
			$artigo['mainEntityOfPage'] = $url;
		}
		$nos[] = $artigo;
		$nos[] = array( '@type' => 'FAQPage', 'mainEntity' => $faq );

		return $nos;
	}

	/* Seção e categoria: CollectionPage + ItemList das filhas publicadas. */
	$itens = array();
	$posicao = 0;
	foreach ( $registro as $outro => $outra ) {
		if ( $outra['pai'] !== $slug ) {
			continue;
		}
		$url_filha = aquametria_casca_url_se_existir( $outro );
		if ( '' === $url_filha ) {
			continue;
		}
		$posicao++;
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $posicao,
			'name'     => $outra['titulo'],
			'item'     => $url_filha,
		);
	}

	$colecao = array(
		'@type'      => 'CollectionPage',
		'name'       => $def['titulo'],
		'inLanguage' => 'pt-BR',
	);
	if ( '' !== $url ) {
		$colecao['mainEntityOfPage'] = $url;
	}
	$nos[] = $colecao;
	if ( $itens ) {
		$nos[] = array(
			'@type'           => 'ItemList',
			'name'            => $def['titulo'],
			'numberOfItems'   => count( $itens ),
			'itemListElement' => $itens,
		);
	}

	return $nos;
}
}

if ( ! function_exists( 'aquametria_peixes_imprimir_jsonld' ) ) {
function aquametria_peixes_imprimir_jsonld( $slug ) {
	foreach ( aquametria_peixes_jsonld_dados( $slug ) as $no ) {
		$no = array_merge( array( '@context' => 'https://schema.org' ), $no );
		echo '<script type="application/ld+json">'
			. wp_json_encode( $no, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
			. '</script>' . "\n";
	}
}
}

if ( ! function_exists( 'aquametria_peixes_cabeca' ) ) {
function aquametria_peixes_cabeca() {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return;
	}
	aquametria_peixes_imprimir_estilo();
	aquametria_peixes_imprimir_jsonld( $slug );
}
}
add_action( 'wp_head', 'aquametria_peixes_cabeca', 21 );

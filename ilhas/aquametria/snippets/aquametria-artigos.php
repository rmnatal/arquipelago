/**
 * Aquametria Artigos — visibilidade em IA
 * Versão: 1.2.0 (11/09/2026) — A VOZ CHEGA AOS TRÊS ARTIGOS. A caixa da resposta
 * direta passa a ter duas camadas: o primeiro parágrafo responde à pessoa na
 * língua dela, e a procedência (fabricante, fonte, data de leitura) desce um
 * parágrafo e é marcada com `aqm-prova`. A seção 5 continua inteira — quem cita
 * a caixa leva a fonte junto —, e a 15.2 passa a valer, que proíbe fabricante e
 * data de leitura no primeiro parágrafo. Os três títulos longos com parênteses
 * viraram o mesmo texto da manchete: um nome por página, em toda superfície.
 *
 * Versão: 1.1.0 (11/09/2026) — os três artigos passam a se anunciar na
 * prateleira de guias da home, pelo filtro 'aquametria_guias' da casca. Nada do
 * que já estava aqui mudou: é uma função de anúncio, no molde do hub de
 * calculadoras, para a home listar guia sem guardar cópia de título nenhum.
 *
 * Fecha o T7 (seção 5 do ARQUIPELAGO.md) nas três páginas que sobraram do
 * retrofit: os artigos-âncora. As cinco calculadoras já tinham as três peças
 * desde 10/09/2026; os artigos tinham ZERO, medido pela Sentinela Técnica em
 * 09/09/2026 (JSON-LD zero em 13 de 13 páginas da ilha).
 *
 * O QUE NÃO SE COPIA DO MOLDE DAS CALCULADORAS, e é a razão de este snippet
 * existir separado:
 *
 *   1. Artigo não tem formulário nem shortcode de ferramenta, então NÃO dá para
 *      descobrir a página pelo has_shortcode(), que é como cada calculadora se
 *      reconhece. Aqui a página é reconhecida pelo SLUG, o mesmo que está no
 *      front matter do Markdown e no manifest.
 *   2. Artigo não é WebApplication. O nó é Article, e o FAQPage vem junto.
 *   3. TABELA PRÉ-RENDERIZADA NÃO SE INVENTA. Os três artigos já servem tabelas
 *      próprias no HTML — a linha comercial Eheim Jäger, as quatro dosagens de
 *      mídia, as três leituras de lm/L —, escritas em Markdown e convertidas
 *      pelo Sync. Acrescentar uma tabela nossa por cima seria decoração, e
 *      tabela decorativa é pior que nenhuma: o portão da seção 5 é servir
 *      resposta citável, não servir uma tabela.
 *
 * O QUE ELE ACRESCENTA, e onde cada coisa sai:
 *
 *   - [aquametria_artigo_resposta] — a resposta ANTES da explicação, no topo do
 *     Markdown de cada artigo. É frase autossuficiente: precisa sobreviver a
 *     ser citada fora de contexto por um modelo que leu só aquele parágrafo,
 *     então repete o número, a unidade, o critério, a fonte pelo nome e a data.
 *   - JSON-LD (Article + FAQPage) no wp_head, NUNCA dentro do retorno do
 *     shortcode: o retorno atravessa os filtros do the_content, que trocam cada
 *     "&" pela entidade numérica dele e quebrariam o JSON tanto quanto
 *     quebraram o JavaScript das cinco calculadoras em 08/09/2026.
 *   - O estilo também no wp_head, pelo mesmo motivo.
 *
 * REGRA DE CONTEÚDO QUE ESTE ARQUIVO OBEDECE: todo número que sai daqui existe
 * no corpo do artigo servido na mesma página. Resposta direta que cita número
 * que a página não mostra, e FAQPage que promete o que a página não tem, são
 * lixo — e lixo detectável. É isso que ferramentas/teste-navegador-artigos.mjs
 * mede, com o JavaScript desligado.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'AQUAMETRIA_ARTIGOS_VERSAO' ) ) {
	define( 'AQUAMETRIA_ARTIGOS_VERSAO', '1.2.0' );
}

/* Data de verificação declarada no front matter dos três artigos. Está aqui
   uma vez só porque a procedência tem de aparecer DENTRO da frase, e frase
   com data escrita à mão em três lugares envelhece em dois deles. */
if ( ! defined( 'AQUAMETRIA_ARTIGOS_VERIFICADO_EM' ) ) {
	define( 'AQUAMETRIA_ARTIGOS_VERIFICADO_EM', '08/09/2026' );
}

/* Data do levantamento de fontes brasileiras (Bloco 1), citada nos três. */
if ( ! defined( 'AQUAMETRIA_ARTIGOS_CORPUS_EM' ) ) {
	define( 'AQUAMETRIA_ARTIGOS_CORPUS_EM', '04/09/2026' );
}

if ( ! function_exists( 'aquametria_artigos_url' ) ) {
function aquametria_artigos_url( $slug ) {
	return home_url( '/' . $slug . '/' );
}
}

/* ---------------------------------------------------------------------------
 * 1. O registro dos três artigos
 *
 * Cada entrada carrega o que o Article precisa declarar, a resposta direta e o
 * FAQ. Texto de tela sai ACENTUADO daqui (regra da ilha desde 07/09/2026), e
 * nenhum "&" entra: o que este arquivo devolve pelo shortcode atravessa os
 * filtros de conteúdo do WordPress.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_registro' ) ) {
function aquametria_artigos_registro() {
	$corpus = AQUAMETRIA_ARTIGOS_CORPUS_EM;
	$col    = AQUAMETRIA_ARTIGOS_VERIFICADO_EM;

	return array(

		/* ------------------------------------------------------ C5 · aquecedor */
		'quantos-watts-de-aquecedor-para-aquario' => array(
			'codigo'    => 'C5',
			'manchete'  => 'Por que o 1 W por litro erra para o mesmo lado',
			'titulo'    => 'Por que o 1 W por litro erra para o mesmo lado',
			'consulta'  => 'quantos watts de aquecedor para aquário',
			'resumo'    => 'A regra de 1 W por litro não veio de um cálculo: veio da prateleira. '
				. 'A única fonte brasileira que declara a condição em que o número vale sustenta de 1,0 a 1,5 W por litro para até 10 °C de diferença entre a água e o cômodo.',
			'publicado' => '2026-09-08',
			'assuntos'  => array( 'Aquecedor de aquário', 'Dimensionamento de aquário', 'Aquarismo' ),
			'ferramenta' => array(
				'slug'   => 'calculadora-de-potencia-do-aquecedor',
				'rotulo' => 'calculadora de potência do aquecedor',
			),
			'fontes' => array(
				'ReefFlow — de 1,0 a 1,5 W por litro para até 10 °C de diferença (levantamento da Aquametria, ' . $corpus . ')',
				'Casa da Ada — até 2,0 W por litro na região Sul (levantamento da Aquametria, ' . $corpus . ')',
				'eHow — 1,3 W por litro, sem condição declarada (levantamento da Aquametria, ' . $corpus . ')',
				'Catálogo Eheim Jäger e tabelas de varejo, nove tamanhos de 25 a 300 W, transcritos em ' . $col,
				'Fichas de varejo brasileiro da linha Roxin HT-1300/Q3, coletadas em 07 e ' . $col,
			),
			'resposta' => array(
				array(
					'rotulo' => 'A resposta curta.',
					'texto'  => 'Não existe um número de watts por litro que sirva para o Brasil inteiro: o que manda no aquecedor é quantos graus ele tem de vencer entre a água que você quer e o frio do cômodo, não o volume sozinho. '
						. 'Com até 10 °C de diferença, um aquário de 100 litros de água real pede de 100 a 150 W. '
						. 'Passando disso, essa faixa vira piso e não resposta — quem mora onde o inverno morde de verdade precisa de mais.',
				),
				array(
					'prova'  => true,
					'rotulo' => 'De onde sai esse número.',
					'texto'  => 'Das quatro afirmações que o levantamento de fontes brasileiras da Aquametria encontrou em ' . $corpus . ', uma só declara a condição em que vale: a ReefFlow publica de 1,0 a 1,5 W por litro para até 10 °C de diferença. '
						. 'Acima de 10 °C nenhuma fonte do levantamento cobre o caso.',
				),
				array(
					'rotulo' => 'De onde veio o “1 W por litro”, e por que ele erra sempre para o mesmo lado.',
					'texto'  => 'Ele não veio de física: veio da prateleira. A linha de aquecedores Eheim Jäger inteira, transcrita em ' . $col . ', nomeia cada aparelho pelo volume que dá exatamente 1,00 W por litro — 25 W para 25 L, 50 W para 50 L, 100 W para 100 L, 150 W para 150 L —, seis degraus seguidos. '
						. 'A regra brasileira leu a caixa e transformou o rótulo em lei. '
						. 'Como a caixa foi calibrada num clima que não é o do Brasil inteiro, a regra responde os mesmos 100 W para um aquário de 100 litros em Belém, onde o quarto cai a 23 °C e a diferença é de 3 °C, e para o mesmo aquário em Curitiba, onde o quarto cai a 11 °C e a diferença é de 15 °C. '
						. 'Cinco vezes mais frio a vencer, com a mesma resposta.',
				),
				array(
					'rotulo' => 'O volume declarado na caixa não dimensiona.',
					'texto'  => 'Dentro da própria linha Eheim, o 200 W é declarado para 300 a 400 litros — 0,50 W por litro, metade do resto da linha — e, no catálogo geral, para 30 a 400 litros, uma faixa de treze vezes. '
						. 'Na linha popular brasileira Roxin HT-1300/Q3, com fichas de varejo coletadas em 07 e ' . $col . ', a razão vai de 0,67 a 2,00 W por litro entre modelos da mesma família, e um aquário de 60 litros cabe ao mesmo tempo no 50 W, no 100 W e no 200 W pela declaração do próprio fabricante. '
						. 'A via física, P = U · A · ΔT, é o que a Aquametria quer publicar e ainda não publica: falta o coeficiente de troca do vidro de aquário, com água de um lado e ar do outro, e constante pendente é proibida dentro de fórmula publicada aqui.',
				),
			),
			'faq' => array(
				array(
					'p' => 'Quantos watts de aquecedor por litro de água de aquário?',
					'r' => 'Depende de quanto o cômodo esfria, e só uma das quatro fontes brasileiras do levantamento da Aquametria de ' . $corpus . ' declara essa condição: a ReefFlow, com 1,0 a 1,5 W por litro para até 10 °C de diferença entre a água e o ar. '
						. 'As outras três publicam número sem condição: 1,0 W por litro sem autoria única, 1,3 W por litro no eHow e até 2,0 W por litro na região Sul pela Casa da Ada. '
						. 'Duas fontes genéricas discordando em 30 % para a mesma pergunta, sem nenhuma condição que explique a diferença, é a prova de que ninguém ali está calculando nada.',
				),
				array(
					'p' => 'Quantos watts de aquecedor para um aquário de 100 litros?',
					'r' => 'Num cômodo que não fica mais de 10 °C abaixo da temperatura da água, de 100 a 150 W, pela única fonte do levantamento da Aquametria que amarra o número a uma diferença de temperatura (ReefFlow, 1,0 a 1,5 W por litro, ' . $corpus . '). '
						. 'Na prateleira brasileira isso cai no degrau de 150 W. '
						. 'Se o cômodo esfriar mais que 10 °C, nenhuma fonte cobre o caso, e essa faixa deixa de ser resposta e vira piso: pode não segurar a madrugada.',
				),
				array(
					'p' => 'De onde veio a regra de 1 watt por litro para aquecedor de aquário?',
					'r' => 'Da prateleira, não de um modelo térmico. A linha Eheim Jäger inteira, transcrita em ' . $col . ', nomeia cada aparelho pelo volume que dá exatamente 1,00 W por litro: 25 W para 25 L, 50 W para 50 L, 75 W para 75 L, 100 W para 100 L, 125 W para 125 L e 150 W para 150 L. '
						. 'Seis degraus com o mesmo 1,00 na coluna da direita. É por isso que fontes que não se citam repetem o mesmo número: todas leram a mesma caixa.',
				),
				array(
					'p' => 'O volume declarado na caixa do aquecedor serve para dimensionar?',
					'r' => 'Não, e a própria linha que criou a regra mostra por quê: o Eheim Jäger de 200 W é declarado para 300 a 400 litros, ou seja 0,50 W por litro, metade dos degraus abaixo dele, e o catálogo geral do mesmo fabricante declara esse mesmo aparelho para 30 a 400 litros, treze vezes de faixa. '
						. 'Na linha Roxin HT-1300/Q3 a razão vai de 0,67 a 2,00 W por litro dentro de uma única família, com sobreposição de três modelos entre 50 e 150 litros. '
						. 'O volume da caixa serve para escolher entre dois modelos parecidos; não serve para dimensionar.',
				),
				array(
					'p' => 'A regra de 1 W por litro vale igual em Belém e em Curitiba?',
					'r' => 'Não, e a diferença é de cinco vezes. Um aquário de 100 litros a 26 °C num quarto que cai a 23 °C tem 3 °C de diferença para vencer; o mesmo aquário num quarto que cai a 11 °C tem 15 °C. '
						. 'O "1 W por litro" responde 100 W para os dois. No primeiro caso é folga; no segundo é um aquecedor que passa a madrugada ligado e pode não segurar. '
						. 'Meça o frio do cômodo onde o aquário está, com um termômetro, na semana mais fria — esse número vale mais que a média da cidade.',
				),
				array(
					'p' => 'Aquário destampado precisa de aquecedor mais forte?',
					'r' => 'Perde mais calor, sim, e perde principalmente por evaporação na lâmina livre, que costuma ser a maior parcela da perda. '
						. 'Mas a Aquametria não corrige o número por isso: a constante que quantificaria essa perda está pendente no banco, sem fonte, e escrever “some 20 %” seria inventar constante. '
						. 'Com o aquário aberto, trate a faixa de 1,0 a 1,5 W por litro como piso e considere o degrau comercial seguinte.',
				),
				array(
					'p' => 'É melhor um aquecedor grande ou dois menores no mesmo aquário?',
					'r' => 'Acima de 150 W vale considerar dois aparelhos de metade da potência, e o argumento é modo de falha, não economia: travado ligado, um aquecedor menor faz menos estrago; travado desligado, o outro ainda segura alguma coisa. '
						. 'A partir de 300 litros isso deixa de ser preferência e vira necessidade, porque a faixa calculada passa do maior degrau da linha de referência, que é o de 300 W. '
						. 'Esse raciocínio é da Aquametria e está declarado como tal: não é regra publicada por fabricante nenhum.',
				),
				array(
					'p' => 'Por que a Aquametria não publica a fórmula física do aquecedor?',
					'r' => 'Porque falta uma peça com fonte. A conta certa é P = U · A · ΔT — coeficiente global de troca, vezes a área que troca calor, vezes a diferença de temperatura —, e ela sabe distinguir aquário alto de aquário baixo e vidro de 6 mm de vidro de 10 mm. '
						. 'O que não temos é o U do aquário: não o U tabelado de janela, que descreve ar dos dois lados, mas o de água de um lado, ar do outro e lâmina livre por cima, onde a evaporação responde pela maior parte da perda. '
						. 'A constante u-vidro-aquario segue pendente, e constante pendente é proibida dentro de fórmula publicada aqui.',
				),
			),
		),

		/* ---------------------------------------------------------- C12 · mídia */
		'quanta-midia-biologica-o-aquario-precisa' => array(
			'codigo'    => 'C12',
			'manchete'  => 'Cada marca pede uma dose diferente de mídia',
			'titulo'    => 'Cada marca pede uma dose diferente de mídia',
			'consulta'  => 'quanta mídia biológica para aquário',
			'resumo'    => 'Seachem pede 1,25 mL de mídia por litro de água; Ocean Tech pede 12,50. '
				. 'As quatro dosagens declaradas por fabricante, com a área que cada uma entrega por litro de água e o que nenhuma delas pergunta.',
			'publicado' => '2026-09-08',
			'assuntos'  => array( 'Mídia filtrante', 'Filtragem biológica', 'Aquarismo' ),
			'ferramenta' => array(
				'slug'   => 'calculadora-de-midia-filtrante',
				'rotulo' => 'calculadora de mídia filtrante',
			),
			'fontes' => array(
				'Seachem, página do Matrix — 250 mL para 200 L de água (1,25 mL/L) e 1 L para 100 galões (2,64 mL/L), coletado em ' . $col,
				'JBL, ficha do MicroMec — 650 g para 200 L, embalagem vendida como 1 L (5,00 mL/L), coletado em ' . $col,
				'Ocean Tech, ficha do Bio Glass — 1 L para cada 80 L de água (12,50 mL/L), coletado em ' . $col,
				'Eheim, Substrat pro — 450 m² por litro de mídia, sem dosagem publicada, coletado em ' . $col,
				'Seachem Tidal 55 — 1,2 L de mídia para até 200 L, e Eheim classic 250 — 3,0 L para até 250 L, coletados em ' . $col,
			),
			'resposta' => array(
				array(
					'rotulo' => 'A resposta curta.',
					'texto'  => 'As marcas que publicam quanta mídia biológica usar não concordam nem na ordem de grandeza. '
						. 'No seu aquário de 100 litros, seguir uma ou outra é a diferença entre você comprar 125 mL de mídia e comprar 1,25 litro — dez vezes, para o mesmo trabalho. '
						. 'Nenhuma delas está errada sozinha; o que não existe é um número único para copiar.',
				),
				array(
					'prova'  => true,
					'rotulo' => 'As quatro dosagens, com o nome de quem publicou.',
					'texto'  => 'Coletadas em ' . $col . ' e atribuídas ao próprio fabricante: Seachem Matrix, 1,25 mL por litro de água, e 2,64 mL por litro numa segunda leitura da mesma marca; JBL MicroMec, 5,00; Ocean Tech Bio Glass, 12,50.',
				),
				array(
					'rotulo' => 'O argumento de venda do setor não explica a diferença — ele a contradiz.',
					'texto'  => 'Multiplicando a dosagem declarada pela área declarada, a área de mídia entregue por litro de água vai de 0,88 m² na Seachem, que declara mais de 700 m² por litro de mídia a 1,25 mL/L, a 7,5 m² na JBL e 18,8 m² na Ocean Tech. '
						. 'Vinte e uma vezes de diferença. E repare na direção: a marca que declara mais área por litro de mídia, a Ocean Tech com 1.500 m²/L, é a que pede dez vezes mais mídia que a Seachem, que declara menos. '
						. 'Se a área colonizável fosse o critério, a relação seria a inversa. Nenhuma das quatro publica o método com que mediu a própria área.',
				),
				array(
					'rotulo' => 'E há uma pergunta que nenhuma das quatro faz.',
					'texto'  => 'Todas as dosagens são por litro de água, mas o trabalho da mídia biológica depende da amônia que entra no sistema — ou seja, da carga de peixes, que nenhuma das declarações pergunta. '
						. 'Do outro lado do balcão o número muda de novo, porque quem vende filtro declara mídia total: o Eheim classic 250 leva 3,0 L para até 250 litros de aquário, 12 mL por litro, contra 1,2 L para até 200 litros do Seachem Tidal 55, 6 mL por litro — a mesma Seachem que, como fabricante de mídia, diz que 1,25 mL por litro bastam. '
						. 'Por isso esta página publica as quatro dosagens com o nome de quem as sustenta e a data, em vez de escolher uma: escolher seria fabricar um consenso que os fabricantes não têm.',
				),
			),
			'faq' => array(
				array(
					'p' => 'Quanta mídia biológica para um aquário de 100 litros?',
					'r' => 'Depende de qual fabricante você seguir, e a diferença é de dez vezes: 125 mL pela dosagem da Seachem para o Matrix (1,25 mL por litro de água), 264 mL pela segunda leitura da própria Seachem (2,64 mL/L), 500 mL pela JBL para o MicroMec (5,00 mL/L) e 1,25 litro pela Ocean Tech para o Bio Glass (12,50 mL/L). '
						. 'Todas as quatro foram coletadas em ' . $col . ' e atribuídas ao próprio fabricante. A Aquametria publica as quatro em vez de escolher uma.',
				),
				array(
					'p' => 'Por que os fabricantes de mídia biológica discordam tanto na dosagem?',
					'r' => 'Não sabemos, e é por não saber que não escolhemos um número. O que dá para medir é a incoerência: cruzando dosagem com área declarada, a área entregue por litro de água vai de 0,88 m² (Seachem) a 7,5 m² (JBL) e 18,8 m² (Ocean Tech), vinte e uma vezes de diferença. '
						. 'Ou os números de área não são comparáveis porque cada empresa mede de um jeito, e nenhuma das quatro publica o método, ou as dosagens não derivam da área, ou as duas coisas ao mesmo tempo.',
				),
				array(
					'p' => 'Mídia com mais área de superfície precisa de menos volume?',
					'r' => 'Pela lógica do argumento de venda, sim; pelos números publicados, não. A Ocean Tech declara 1.500 m² por litro de mídia e pede 12,50 mL por litro de água; a Seachem declara mais de 700 m² por litro e pede 1,25 mL. '
						. 'Ou seja, a marca que diz ter mais área pede dez vezes mais mídia — exatamente o contrário do que a área explicaria. Não compare marcas por área de superfície: é o número mais repetido do setor e o menos sustentado.',
				),
				array(
					'p' => 'Quanta mídia cabe no meu filtro?',
					'r' => 'O cesto é o teto, e ele decide antes da dosagem. Quem vende filtro declara mídia total: o Eheim classic 250 leva 3,0 litros de mídia para até 250 litros de aquário, 12 mL por litro de água, e o Seachem Tidal 55 leva 1,2 litro para até 200 litros, 6 mL por litro. '
						. 'Se a camada biológica sozinha já estoura o cesto na dosagem que você pretende seguir, o problema não é a mídia: é o filtro, e comprar mais mídia não resolve.',
				),
				array(
					'p' => 'De quanto em quanto tempo trocar o carvão ativado do filtro?',
					'r' => 'As duas respostas publicadas estão muito longe uma da outra. A regra que circula no aquarismo brasileiro é 1 a 2 gramas por litro de água, trocado a cada 15 a 30 dias. '
						. 'A Seachem declara, para o MatrixCarbon, 250 mL para 400 litros de água — 0,625 mL por litro — durando vários meses. '
						. 'Não dá para comparar as quantidades sem a densidade aparente do carvão, que não temos com fonte, mas a frequência compara sem conversão nenhuma: a regra brasileira manda trocar de quatro a dez vezes mais vezes do que o fabricante do carvão.',
				),
				array(
					'p' => 'Posso trocar toda a mídia biológica de uma vez?',
					'r' => 'Não. A colônia de bactérias nitrificantes leva semanas para se estabelecer, e substituir tudo de uma vez — ou lavar tudo em água de torneira, que tem cloro justamente para matar bactéria — reinicia o ciclo do aquário com os peixes dentro. '
						. 'A troca é sempre parcial: troque uma parte e deixe a colônia da parte que ficou recolonizar a nova. Para tirar a sujeira grossa, use a água que saiu na troca parcial. '
						. 'Isso vale qualquer que seja a dosagem que você tenha seguido, 1,25, 2,64, 5,00 ou 12,50 mL por litro de água: a dosagem declarada pelo fabricante diz quanto comprar, e nunca com que velocidade substituir.',
				),
				array(
					'p' => 'A quantidade de mídia depende de quantos peixes eu tenho?',
					'r' => 'Deveria, e nenhuma das quatro dosagens pergunta. Todas são expressas por litro de água, mas o trabalho da mídia depende da amônia que entra no sistema, que vem dos peixes, da ração que sobra e do que apodrece no fundo. '
						. 'Um aquário de 100 litros com três tetras e um de 100 litros com vinte ciclídeos não produzem a mesma amônia. É por isso que quatro empresas competentes chegam a números tão distantes: todas estimam por cima de uma variável que só se correlaciona com a resposta certa.',
				),
				array(
					'p' => 'A ficha do meu canister diz a capacidade de mídia, mas a conta não fecha. Por quê?',
					'r' => 'Porque a ficha é ambígua e o varejo replica o mesmo texto. O Atman AT-3338 declara três cestos de 17 x 17 x 6 cm com capacidade de 1,6 litro de mídia, o que pode ser 1,6 L no total ou 1,6 L por cesto, 4,8 L. '
						. 'No modelo irmão AT-3338S a mesma frase dá 3,5 litros, só que os cestos declarados, de 21 x 21 x 7 cm, têm 3,09 litros brutos cada e não comportam 3,5 litros. '
						. 'A mesma construção de frase, dois modelos, e em cada um só uma das leituras fecha com as próprias dimensões publicadas. A Aquametria publica as duas leituras em vez de desempatar.',
				),
			),
		),

		/* ---------------------------------------------------- C15 · iluminação */
		'quantos-lumens-por-litro-aquario-plantado' => array(
			'codigo'    => 'C15',
			'manchete'  => 'Quantos lúmens por litro o aquário plantado precisa',
			'titulo'    => 'Quantos lúmens por litro o aquário plantado precisa',
			'consulta'  => 'quantos lúmens por litro aquário plantado',
			'resumo'    => 'Três fontes brasileiras chamam a mesma faixa de iluminação pelo mesmo nome com o dobro do número. '
				. 'De onde vem a régua de lúmens por litro, por que ela penaliza a luminária feita para planta e onde a trilha do PPFD termina.',
			'publicado' => '2026-09-08',
			'assuntos'  => array( 'Iluminação de aquário', 'Aquário plantado', 'Aquarismo' ),
			'ferramenta' => array(
				'slug'   => 'calculadora-de-iluminacao',
				'rotulo' => 'calculadora de iluminação e fotoperíodo',
			),
			'fontes' => array(
				'peixeseaquarismo, aquarioturbinado e aquariosplantados — as três réguas de lúmens por litro do levantamento da Aquametria de ' . $corpus,
				'Fórum de suporte da Chihiros — não existe teste de PAR oficial da linha WRGB II Pro, coletado em ' . $col,
				'Fichas de varejo brasileiro das luminárias Chihiros WRGB II Pro 60 e Ista IL-401 60, coletadas em ' . $col,
			),
			'resposta' => array(
				array(
					'rotulo' => 'A resposta curta.',
					'texto'  => 'As réguas de lúmens por litro que circulam no aquarismo brasileiro chamam a mesma faixa pelo mesmo nome com o dobro do número. '
						. 'Num aquário plantado de 100 litros, iluminação baixa vai de 1.000 a 2.000 lúmens conforme a régua que você abrir — e é essa dúvida que separa duas luminárias de preço bem diferente. '
						. 'Elas concordam na ordem de grandeza, entre 10 e 60 lm/L; discordam nas fronteiras, que é justo onde quem vai comprar precisa de precisão.',
				),
				array(
					'prova'  => true,
					'rotulo' => 'As três réguas, com o nome de quem publicou.',
					'texto'  => 'No levantamento da Aquametria de ' . $corpus . ', “baixa” é 20 lm/L na peixeseaquarismo, 10 a 20 lm/L na aquarioturbinado e 15 lm/L na aquariosplantados; “alta” é 60, acima de 40, e 60.',
				),
				array(
					'rotulo' => 'A régua é frágil por definição, não por descuido de quem a publica.',
					'texto'  => 'O lúmen mede fluxo luminoso ponderado pela sensibilidade do olho humano, com pico perto de 555 nanômetros, no verde, e desconta fortemente o azul profundo e o vermelho profundo — que são justamente as duas faixas em que a clorofila trabalha. '
						. 'A consequência é que a luminária projetada para planta tende a marcar menos lúmens que uma calha branca de mesmo consumo, e a régua de lm/L a considera pior. '
						. 'No banco da Aquametria, com fichas de varejo coletadas em ' . $col . ', a Chihiros WRGB II Pro 60 declara 74 W para 6.630 lm, 89,6 lm por watt, e a Ista IL-401 60, uma calha branca, declara 35 W para 3.717 lm, 106 lm por watt. '
						. 'Dois produtos são indício, não demonstração, e é assim que esta página os apresenta.',
				),
				array(
					'rotulo' => 'A medida certa existe, e a trilha dela termina antes do Brasil.',
					'texto'  => 'É o PPFD, o fluxo de fótons fotossinteticamente ativos, em µmol/m²/s, medido na profundidade em que a planta está. '
						. 'Procurando a tabela de PAR da linha WRGB II Pro em ' . $col . ', chegamos ao fórum de suporte da própria Chihiros — marca cujo argumento de venda é intensidade de PAR — e a resposta oficial publicada lá é que não existe teste de PAR oficial desses modelos e que o usuário procure medições de terceiros no YouTube. '
						. 'Por isso a constante ppfd-por-litragem continua pendente aqui, e proibida em fórmula publicada. '
						. 'Enquanto ela não existir, lm/L é o que dá para publicar com honestidade — com as três leituras nomeadas, nunca com a média delas.',
				),
			),
			'faq' => array(
				array(
					'p' => 'Quantos lúmens por litro para aquário plantado?',
					'r' => 'As três fontes brasileiras do levantamento da Aquametria de ' . $corpus . ' discordam nas fronteiras. Para iluminação baixa: 20 lm/L na peixeseaquarismo, 10 a 20 lm/L na aquarioturbinado e 15 lm/L na aquariosplantados. '
						. 'Para média: 30 a 40, 20 a 40 e 30 lm/L. Para alta: 60, acima de 40, e 60 lm/L. '
						. 'Elas concordam na ordem e na ordem de grandeza — a régua inteira vive entre 10 e 60 lm/L — e discordam exatamente onde quem vai comprar precisa decidir.',
				),
				array(
					'p' => 'Quantos lúmens para um aquário plantado de 100 litros?',
					'r' => 'Para iluminação baixa, de 1.000 a 2.000 lúmens conforme a fonte, porque “baixa” é 10, 15 ou 20 lm/L dependendo de quem publica. '
						. 'Para média, de 2.000 a 4.000 lúmens. Para alta, 6.000 lúmens por duas das fontes e acima de 4.000 pela terceira. '
						. 'A Aquametria publica a faixa que as três sustentam juntas e mostra as três leituras com nome, porque média aqui seria fabricar consenso onde não há.',
				),
				array(
					'p' => 'O lúmen é a unidade certa para medir luz de aquário plantado?',
					'r' => 'Não, e isso não é opinião: é a definição da unidade. O lúmen pondera o fluxo pela sensibilidade do olho humano, com pico perto de 555 nanômetros, no verde, e desconta o azul profundo e o vermelho profundo, que são as faixas de absorção da clorofila. '
						. 'Duas luminárias com o mesmo número de lúmens e espectros diferentes não entregam a mesma fotossíntese — e a luminária feita para planta tende a marcar menos lúmens que uma calha branca de mesmo consumo, o que faz a régua penalizar justamente o produto feito para a tarefa.',
				),
				array(
					'p' => 'Por que os fabricantes de luminária não publicam PPFD?',
					'r' => 'A trilha termina antes do Brasil. Procurando a tabela de PAR da linha WRGB II Pro em ' . $col . ', a Aquametria chegou ao fórum de suporte da própria Chihiros, e a resposta oficial publicada lá é que não existe teste de PAR oficial desses modelos e que o usuário procure medições de terceiros no YouTube. '
						. 'A fonte brasileira que copiaria esse dado não tem de onde copiar. E o número que circula por aí, PAR de 50 a 60 no substrato, costuma vir sem a distância em centímetros, o que o torna inútil: PPFD sem distância declarada não diz nada, porque a intensidade cai com o caminho percorrido.',
				),
				array(
					'p' => 'Uma luminária de 60 cm serve num aquário de 60 cm?',
					'r' => 'Nem sempre, e o número do nome é a primeira armadilha: a Ista IL-401 vendida como 60 cm mede 56 cm na ficha de dimensões da mesma página de varejo. '
						. 'A segunda armadilha é que a cobertura declarada não é proporcional ao comprimento da peça: nos registros do banco que declaram os dois números, o teto declarado vai de 1,15 a 1,59 vez o comprimento da peça, e a SunSun ADE-400C, de 41 cm, é declarada para aquários de 48 a 65 cm porque acompanha hastes reguláveis. '
						. 'É por isso que a Aquametria não converte comprimento de peça em cobertura de aquário: a razão varia demais entre produtos para virar constante.',
				),
				array(
					'p' => 'Aumentar o fotoperíodo compensa uma luminária fraca?',
					'r' => 'Não. A planta responde à intensidade que recebe enquanto a luz está acesa, e abaixo de um certo patamar hora a mais não vira crescimento: vira tempo a mais de nutriente disponível na água com planta parada, que é a condição em que a alga leva vantagem. '
						. 'Não por acaso, o regime de 5 a 6 horas aparece nas fontes brasileiras rotulado como combate a alga, e não como dimensionamento. '
						. 'Os quatro regimes do levantamento — low tech 6 a 8 h, high tech 8 a 10 h, combate a alga 5 a 6 h e ciclagem 4 a 6 h — são faixas repetidas sem medição publicada por trás, e estão na calculadora com esse rótulo.',
				),
				array(
					'p' => 'Dá para escolher luminária de aquário pelo watt?',
					'r' => 'Não: watt é consumo, não luz. Dentro do próprio banco da Aquametria a eficácia dos LEDs vendidos no Brasil vai de 89 a 107 lm por watt, e uma peça de 60 cm pode ser de 24 W ou de 74 W — três vezes de diferença — cabendo as duas no mesmo aquário. '
						. 'Comece pelo lúmen declarado. Se a ficha não traz lúmen, você não tem como dimensionar a peça, e isso deveria pesar na comparação de preço: no banco, onze luminárias continuam barradas por não declarar lúmen, oito delas da linha Soma WRGB, vendida em nove lojas brasileiras.',
				),
				array(
					'p' => 'A régua de lúmens por litro vale para aquário fundo?',
					'r' => 'Vale cada vez pior à medida que a lâmina cresce, e ela não sabe disso. Dois aquários de 100 litros — um de 80 x 30 cm com 40 cm de lâmina, outro de 40 x 40 cm com 62 cm — têm a mesma resposta em lúmens por litro e entregam luz muito diferente no substrato, porque a água absorve e espalha luz ao longo do caminho. '
						. 'A Aquametria não publica fator de correção por profundidade: seria número inventado no formato mais perigoso, o que parece preciso. O que a calculadora faz é avisar, acima de 45 cm de lâmina, que ali a régua começa a mentir.',
				),
			),
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 1b. Anúncio na prateleira de guias da casca
 *
 * A casca pergunta pelo filtro 'aquametria_guias' e quem responde é este
 * arquivo, que é quem sabe quais artigos existem. Vale a mesma razão do hub de
 * calculadoras: a home precisa mostrar os guias sem guardar cópia dos títulos —
 * cópia envelhece em silêncio, e o dia em que nasce o quarto artigo é
 * justamente o dia em que ninguém lembra de ir atualizar a home.
 *
 * A manchete (curta) vai para o cartão; o título longo continua sendo o H1 e o
 * headline do JSON-LD do artigo.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_registrar_guias' ) ) {
function aquametria_artigos_registrar_guias( $lista ) {
	if ( ! is_array( $lista ) ) {
		$lista = array();
	}
	foreach ( aquametria_artigos_registro() as $slug => $a ) {
		$lista[] = array(
			'slug'     => $slug,
			'manchete' => isset( $a['manchete'] ) ? $a['manchete'] : $a['titulo'],
			'resumo'   => isset( $a['resumo'] ) ? $a['resumo'] : '',
		);
	}
	return $lista;
}
}
add_filter( 'aquametria_guias', 'aquametria_artigos_registrar_guias' );

/* ---------------------------------------------------------------------------
 * 2. Que artigo é esta página
 *
 * Pelo SLUG, e não por shortcode: artigo não tem shortcode de ferramenta, e
 * amarrar o JSON-LD à presença do shortcode da resposta direta faria a página
 * perder o schema no dia em que alguém tirasse o bloco do topo.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_atual' ) ) {
function aquametria_artigos_atual() {
	if ( ! is_singular() ) {
		return null;
	}
	$pagina = get_post();
	if ( ! $pagina || empty( $pagina->post_name ) ) {
		return null;
	}
	$registro = aquametria_artigos_registro();
	return isset( $registro[ $pagina->post_name ] ) ? $pagina->post_name : null;
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo — no wp_head, nunca no retorno do shortcode
 *
 * Classes NOVAS de propósito (aqm-art-*). A ilha já pagou duas rodadas de teste
 * por reaproveitar classe que um teste de navegador usa como localizador.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_css' ) ) {
function aquametria_artigos_css() {
	return <<<'CSS'
.aqm-art-direta{--art-tinta:var(--aqm-tinta,#0D1B22);--art-lamina:var(--aqm-lamina,#0E7C8C);
--art-papel:var(--aqm-papel,#F4F7F7);--art-traco:var(--aqm-traco,#DDE5E6);
--art-legenda:var(--aqm-legenda,#5C7075);--art-alerta:var(--aqm-alerta,#B5762A);
--art-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--art-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--art-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--art-texto);color:var(--art-tinta);
background:var(--art-papel);border:1px dashed var(--art-traco);border-radius:3px;
padding:1rem 1.1rem;font-size:.94rem;line-height:1.6;margin:0 0 1.4rem;}
.aqm-art-direta p{margin:0 0 .7rem;}
.aqm-art-direta p:last-child{margin-bottom:0;}
.aqm-art-direta strong{color:var(--art-tinta);}
.aqm-art-selo{display:inline-block;font-family:var(--art-mono);font-size:.66rem;
letter-spacing:.08em;text-transform:uppercase;color:var(--art-alerta);
border:1px solid var(--art-alerta);border-radius:2px;padding:.1rem .35rem;
margin:0 0 .6rem;}
.aqm-art-consulta{font-family:var(--art-mono);font-size:.78rem;color:var(--art-legenda);
border-top:1px solid var(--art-traco);margin:.8rem 0 0;padding:.6rem 0 0;}
.aqm-art-consulta a{color:var(--art-lamina);}
@media (max-width:600px){.aqm-art-direta{font-size:.9rem;padding:.85rem .9rem;}}
CSS;
}
}

if ( ! function_exists( 'aquametria_artigos_estilo_impresso' ) ) {
function aquametria_artigos_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_artigos_imprimir_estilo' ) ) {
function aquametria_artigos_imprimir_estilo() {
	if ( aquametria_artigos_estilo_impresso() ) {
		return;
	}
	aquametria_artigos_estilo_impresso( true );
	echo '<style id="aquametria-artigos-estilo">' . "\n" . aquametria_artigos_css() . "\n" . '</style>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 4. A resposta antes da explicação (seção 5, item 2 do ARQUIPELAGO.md)
 *
 * Precisa sobreviver a ser citada fora de contexto, por um modelo que leu só
 * este bloco. Por isso repete o número, a unidade, o critério, a fonte pelo
 * nome e a data, em vez de dizer "como se vê abaixo".
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_resposta_html' ) ) {
function aquametria_artigos_resposta_html( $slug ) {
	$registro = aquametria_artigos_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return '';
	}
	$a = $registro[ $slug ];

	$h  = '<div class="aqm-art-direta">';
	$h .= '<span class="aqm-art-selo">Resposta direta</span>';

	/* A CAIXA TEM DUAS CAMADAS, e é isso que deixa a seção 5 e a 15.2 valerem
	   juntas na mesma caixa. A seção 5 exige que este bloco sobreviva a ser
	   citado fora de contexto — com número, critério, fonte pelo nome e data. A
	   15.2 proíbe fabricante, fonte e data de leitura no PRIMEIRO parágrafo, que
	   é a camada de voz. Então o primeiro parágrafo responde à pessoa na língua
	   dela, e a procedência vem logo abaixo, DENTRO da mesma caixa, marcada com
	   `aqm-prova`: quem cita a caixa continua levando a fonte junto, e quem
	   chega pela busca lê primeiro a resposta. */
	foreach ( $a['resposta'] as $p ) {
		$classe = ! empty( $p['prova'] ) ? ' class="aqm-prova"' : '';
		$h .= '<p' . $classe . '><strong>' . esc_html( $p['rotulo'] ) . '</strong> ' . esc_html( $p['texto'] ) . '</p>';
	}

	$h .= '<p class="aqm-art-consulta aqm-prova">Verificado em ' . esc_html( AQUAMETRIA_ARTIGOS_VERIFICADO_EM )
		. '. O número do seu caso sai da <a href="' . esc_url( aquametria_artigos_url( $a['ferramenta']['slug'] ) ) . '">'
		. esc_html( $a['ferramenta']['rotulo'] ) . '</a>; o critério de fonte está em '
		. '<a href="' . esc_url( home_url( '/metodologia/' ) ) . '">como a Aquametria calcula</a>.</p>';

	$h .= '</div>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_artigos_shortcode' ) ) {
function aquametria_artigos_shortcode() {
	$slug = aquametria_artigos_atual();
	if ( null === $slug ) {
		return '';
	}

	static $ja_saiu = false;
	if ( $ja_saiu ) {
		return '';
	}
	$ja_saiu = true;

	/* Rede de segurança: se o wp_head não enxergou a página (bloco, template,
	   widget), o estilo ainda sai pelo rodapé — atrasado, mas sai. */
	add_action( 'wp_footer', 'aquametria_artigos_imprimir_estilo', 20 );

	return aquametria_artigos_resposta_html( $slug );
}
}
add_shortcode( 'aquametria_artigo_resposta', 'aquametria_artigos_shortcode' );

/* ---------------------------------------------------------------------------
 * 5. JSON-LD — Article + FAQPage, no wp_head
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_artigos_jsonld_dados' ) ) {
function aquametria_artigos_jsonld_dados( $slug ) {
	$registro = aquametria_artigos_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return null;
	}
	$a   = $registro[ $slug ];
	$url = aquametria_artigos_url( $slug );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$assuntos = array();
	foreach ( $a['assuntos'] as $nome ) {
		$assuntos[] = array( '@type' => 'Thing', 'name' => $nome );
	}

	$artigo = array(
		'@type'              => 'Article',
		'@id'                => $url . '#artigo',
		'url'                => $url,
		'mainEntityOfPage'   => $url,
		'headline'           => $a['manchete'],
		'alternativeHeadline' => $a['titulo'],
		'description'        => $a['resumo'],
		'inLanguage'         => 'pt-BR',
		'datePublished'      => $a['publicado'],
		'dateModified'       => '2026-09-10',
		'author'             => $editora,
		'publisher'          => $editora,
		'about'              => $assuntos,
		'keywords'           => $a['consulta'],
		'citation'           => $a['fontes'],
		'isBasedOn'          => 'Levantamento de fontes brasileiras da Aquametria de ' . AQUAMETRIA_ARTIGOS_CORPUS_EM
			. ' e fichas de fabricante e de varejo coletadas em ' . AQUAMETRIA_ARTIGOS_VERIFICADO_EM,
		'mentions'           => array(
			array(
				'@type' => 'WebApplication',
				'name'  => $a['ferramenta']['rotulo'],
				'url'   => aquametria_artigos_url( $a['ferramenta']['slug'] ),
			),
		),
	);

	$perguntas = array();
	foreach ( $a['faq'] as $q ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $q['p'],
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => $q['r'],
			),
		);
	}

	$faq = array(
		'@type'      => 'FAQPage',
		'@id'        => $url . '#faq',
		'url'        => $url,
		'inLanguage' => 'pt-BR',
		'mainEntity' => $perguntas,
	);

	return array(
		'@context' => 'https://schema.org',
		'@graph'   => array( $artigo, $faq ),
	);
}
}

if ( ! function_exists( 'aquametria_artigos_imprimir_jsonld' ) ) {
function aquametria_artigos_imprimir_jsonld( $slug ) {
	$dados = aquametria_artigos_jsonld_dados( $slug );
	if ( null === $dados ) {
		return;
	}
	$json = wp_json_encode( $dados, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-artigos-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
}
}

if ( ! function_exists( 'aquametria_artigos_cabeca' ) ) {
function aquametria_artigos_cabeca() {
	$slug = aquametria_artigos_atual();
	if ( null === $slug ) {
		return;
	}
	aquametria_artigos_imprimir_estilo();
	aquametria_artigos_imprimir_jsonld( $slug );
}
}
add_action( 'wp_head', 'aquametria_artigos_cabeca', 20 );

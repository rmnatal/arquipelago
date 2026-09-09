/**
 * Aquametria Calculadora de Iluminação e Fotoperíodo — C15
 * Versão: 1.1.1 (09/09/2026) — só o catálogo embutido mudou: entraram quatro Chihiros
 *   A-Series (A301, A361, A601, A801), as únicas do banco que declaram fluxo luminoso em
 *   toda a escada de tamanhos. Nenhuma linha de cálculo foi tocada; o bloco entre
 *   CATALOGO-INICIO e CATALOGO-FIM foi reescrito por
 *   ferramentas/gerar-catalogo-iluminacao.py, como manda a regra.
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.0 (08/09/2026)
 *
 * Quinta calculadora do lote e a que tem o maior cluster de buscas empatado do
 * levantamento (83 consultas). O achado que ela existe para publicar é o
 * seguinte: três fontes brasileiras chamam a MESMA faixa pelo MESMO nome com
 * números que diferem por duas vezes. "Iluminação baixa" é 20 lm/L para uma,
 * 10 a 20 lm/L para outra e 15 lm/L para a terceira. A resposta mostra as três,
 * lado a lado, com o nome de quem publicou cada uma — nunca a média delas.
 *
 * Registra o shortcode [aquametria_calculadora_iluminacao] e se anuncia no hub
 * pelo filtro 'aquametria_calculadoras' da casca.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não publica PPFD (PAR) por litragem. É a medida correta — lm/L ignora a
 *   profundidade e o espectro — e a constante 'ppfd-por-litragem' está
 *   pendente. Em 08/09/2026 a coleta achou o motivo a montante: no próprio
 *   fórum de suporte da Chihiros, cujo argumento de venda é PAR, a resposta
 *   oficial é que não existe teste de PAR oficial e que o usuário procure
 *   medições no YouTube. A tela diz isso com todas as letras.
 * - Não converte o comprimento da peça em cobertura de aquário. Nos cinco
 *   registros do banco que declaram os dois números, o teto declarado vai de
 *   1,15 a 1,59 vez o comprimento da peça: não há razão constante a extrair.
 *   Constante 'cobertura-luminaria-declarada', convenção editorial declarada.
 * - Não publica preço nem tarifa de energia. O consumo sai em kWh por mês, que
 *   é física; o custo em reais só aparece se a pessoa digitar a própria tarifa.
 *
 * Bloco de produto: as luminárias vêm do catálogo embutido mais abaixo, gerado
 * por ferramentas/gerar-catalogo-iluminacao.py a partir de
 * dados/produtos-iluminacao.json. Mexeu no banco, rode o gerador. A ordem é por
 * adequação técnica; link de afiliado não ordena nem filtra (regra V16). A lista
 * de BARRADOS também viaja no snippet e é publicada: quem não entra e por quê é
 * o conteúdo desta entidade.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C15_VERSAO' ) ) {
	define( 'AQUAMETRIA_C15_VERSAO', '1.2.0' );
	define( 'AQUAMETRIA_C15_SLUG', 'calculadora-de-iluminacao' );
	define( 'AQUAMETRIA_C15_VERIFICADO_EM', '08/09/2026' );
	define( 'AQUAMETRIA_C15_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
	define( 'AQUAMETRIA_C15_ARTIGO', 'quantos-lumens-por-litro-aquario-plantado' );
	/* Constante 'temperatura-de-cor': 6500 a 8000 K para aquário plantado. */
	define( 'AQUAMETRIA_C15_K_MIN', 6500 );
	define( 'AQUAMETRIA_C15_K_MAX', 8000 );
	/* Profundidade a partir da qual lm/L deixa de descrever o que chega ao
	   substrato. Convenção editorial declarada, não constante de terceiro. */
	define( 'AQUAMETRIA_C15_LAMINA_FUNDA_CM', 45 );
	/* Convencao editorial declarada da Aquametria, a mesma da C1: aquario cheio
	   ate a borda nao existe, e a agua real desconta 3 cm da altura do vidro. */
	define( 'AQUAMETRIA_C15_BORDA_LIVRE_CM', 3 );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_registrar_no_hub' ) ) {
function aquametria_c15_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C15' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C15_SLUG;
			$lista[ $i ]['resumo'] = 'Lúmens por litro nas três leituras brasileiras que chamam a mesma faixa pelo mesmo nome com o dobro do número, '
				. 'mais o fotoperíodo por regime, a faixa de Kelvin, o aviso de CO2 e o consumo em kWh por mês do fotoperíodo escolhido.';
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c15_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Catálogo de luminárias
 *
 * NÃO EDITE À MÃO os trechos entre os marcadores. Eles são a cópia, dentro do
 * snippet, do que dados/produtos-iluminacao.json já tem — porque o site não lê o
 * repositório em tempo de execução. Depois de mexer no banco:
 *
 *     python3 ferramentas/gerar-catalogo-iluminacao.py
 *
 * Entra no catálogo quem o validador considera apto a ser sugerido pela C15
 * (minimo_para_sugerir do esquema): lúmens, potência, voltagem e o comprimento
 * de aquário DECLARADO. Os barrados vêm no segundo bloco, com o motivo, porque
 * a tela publica essa lista.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_catalogo' ) ) {
function aquametria_c15_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-iluminacao.py */
	return array(
		array(
			'id' => 'ista-i-401-45',
			'marca' => 'Ista',
			'modelo' => 'I-401 45 cm',
			'tipo' => 'led-calha',
			'potencia_w' => 7.6,
			'fluxo_lm' => 810,
			'kelvin' => null,
			'espectro' => 'branco',
			'peca_cm' => 47,
			'aquario_min_cm' => null,
			'aquario_max_cm' => 45,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Aquarius Hobby (varejo BR especializado), ficha da Ista I-401 45 cm luz branca: 7,6 W, 810 lm, 47 x 6,8 x 1,8 cm, 110-240 V 50-60 Hz, corpo de aluminio anodizado, indicada para aquarios de ate 45 cm',
			'fonte_url' => 'https://aquariushobby.commercesuite.com.br/agua-doce/iluminacao/luminarias/ista-luminaria-aquario-led-i-401-45cm-branca-bivolt',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-07',
			'link' => 'https://s.shopee.com.br/1Vz0l9vrvm',
			'anuncio' => 'Ista Luminária Aquário LED I-401 45cm Branca Bivolt',
			'loja' => 'shopee',
			'conflito' => null,
			'observacao' => 'Variante de 45 cm da mesma familia do registro ista-il-401-60, e o unico dos dois com anuncio na Shopee. O varejo brasileiro escreve o 45 cm ora \'I-401\' ora \'IL-400\' (a Pro-Aquarista chama o 45 cm de IL-400 e o 60 cm de IL-401): a equivalencia NAO foi confirmada no fabricante e por isso \'IL-400\' nao entrou em nomes_alternativos. 107 lm/W, coerente com o 60 cm da mesma linha.',
		),
		array(
			'id' => 'aquarios-do-rio-led-60cm',
			'marca' => null,
			'modelo' => 'Luminaria LED Aquario 60 cm full spectrum',
			'tipo' => 'led-calha',
			'potencia_w' => 24,
			'fluxo_lm' => 2400,
			'kelvin' => 6500,
			'espectro' => 'full-spectrum',
			'peca_cm' => 60,
			'aquario_min_cm' => 55,
			'aquario_max_cm' => 75,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'temporizador',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Aquarios do Rio (varejo BR), ficha da luminaria LED 60 cm (24 W, 2400 lm, branco 6500 K + azul 460 nm + vermelho 660 nm + verde 520 nm)',
			'fonte_url' => 'https://aquariosdorio.com.br/loja/iluminacao/luminaria-led-aquario-60cm/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Produto sem marca declarada (importado revendido com nome da loja) — situacao comum no Brasil e o motivo de marca aceitar null com o id derivado da loja. Sem marca, casar cotacoes entre lojas fica impossivel: e o pior caso do banco. 100 lm/W. Segue \'parcial\' por causa da marca ausente, e nao por falta de numero: e apto a ser sugerido pela C15. Em 08/09/2026 saiu do barrado: a segunda leitura da ficha trouxe voltagem (bivolt), cobertura declarada de 55 a 75 cm e timer, e com isso passou a ser o registro de MAIOR cobertura declarada do banco de iluminacao — uma peca de 60 cm que a propria loja diz cobrir ate 75 cm de aquario.',
		),
		array(
			'id' => 'chihiros-a-series-a301',
			'marca' => 'Chihiros',
			'modelo' => 'A301',
			'tipo' => 'led-barra',
			'potencia_w' => 18,
			'fluxo_lm' => 2800,
			'kelvin' => 8000,
			'espectro' => 'branco',
			'peca_cm' => 29.0,
			'aquario_min_cm' => 30,
			'aquario_max_cm' => 30,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Chihiros Aquatic Studio, ficha da A-Series A301: consumo 18 W, fluxo luminoso 2800 lm, 54 LEDs, temperatura de cor de cerca de 8.000 K, peca de 290 mm, alimentacao AC 100-240 V 50/60 Hz, para aquario de 30 cm',
			'fonte_url' => 'https://www.chihirosaquaticstudio.com/products/chihiros-a-series-led-light',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Entrou em 09/09/2026 no bloco T3(a2), e o motivo de entrar e cobertura, nao marca: a linha A-Series e a unica do catalogo que DECLARA fluxo luminoso em toda a escada de tamanhos, e fluxo e o campo que barra a C15. As oito luminarias Soma, que cobririam de 20 a 130 cm e ja tem link de afiliado, continuam barradas porque nem a marca nem nove lojas brasileiras publicam lumen - e estimar lumen a partir do watt seria inventar numero. SEM LINK DE AFILIADO: quem gera o link e a Sentinela Estrategica. O espectro e branco de 8.000 K, sem RGB: a C15 dimensiona por lm/L e o cartao tem de dizer que esta peca nao tem a renderizacao de cor que a linha WRGB entrega. O fabricante declara UM comprimento de aquario (30 cm), nao uma faixa - a mesma leitura que ja valia para a A451M e a A901. Fica \'parcial\' por UM campo: disponibilidade_br. A ficha tecnica veio do fabricante, mas nenhuma loja brasileira foi conferida para este tamanho em 09/09/2026 - e disponibilidade no Brasil so o varejo brasileiro sustenta (nivel 4 ou 5 da escada). A C15 continua podendo sugerir: o campo que falta nao esta no minimo_para_sugerir dela.',
		),
		array(
			'id' => 'chihiros-a-series-a361',
			'marca' => 'Chihiros',
			'modelo' => 'A361',
			'tipo' => 'led-barra',
			'potencia_w' => 21,
			'fluxo_lm' => 3450,
			'kelvin' => 8000,
			'espectro' => 'branco',
			'peca_cm' => 36.0,
			'aquario_min_cm' => 36,
			'aquario_max_cm' => 36,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Chihiros Aquatic Studio, ficha da A-Series A361: consumo 21 W, fluxo luminoso 3450 lm, 63 LEDs, temperatura de cor de cerca de 8.000 K, peca de 360 mm, alimentacao AC 100-240 V 50/60 Hz, para aquario de 36 cm',
			'fonte_url' => 'https://www.chihirosaquaticstudio.com/products/chihiros-a-series-led-light',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Entrou em 09/09/2026 no bloco T3(a2), e o motivo de entrar e cobertura, nao marca: a linha A-Series e a unica do catalogo que DECLARA fluxo luminoso em toda a escada de tamanhos, e fluxo e o campo que barra a C15. As oito luminarias Soma, que cobririam de 20 a 130 cm e ja tem link de afiliado, continuam barradas porque nem a marca nem nove lojas brasileiras publicam lumen - e estimar lumen a partir do watt seria inventar numero. SEM LINK DE AFILIADO: quem gera o link e a Sentinela Estrategica. O espectro e branco de 8.000 K, sem RGB: a C15 dimensiona por lm/L e o cartao tem de dizer que esta peca nao tem a renderizacao de cor que a linha WRGB entrega. O fabricante declara UM comprimento de aquario (36 cm), nao uma faixa - a mesma leitura que ja valia para a A451M e a A901. Fica \'parcial\' por UM campo: disponibilidade_br. A ficha tecnica veio do fabricante, mas nenhuma loja brasileira foi conferida para este tamanho em 09/09/2026 - e disponibilidade no Brasil so o varejo brasileiro sustenta (nivel 4 ou 5 da escada). A C15 continua podendo sugerir: o campo que falta nao esta no minimo_para_sugerir dela.',
		),
		array(
			'id' => 'chihiros-a-series-a451m',
			'marca' => 'Chihiros',
			'modelo' => 'A451M',
			'tipo' => 'led-barra',
			'potencia_w' => 27,
			'fluxo_lm' => 3500,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => 45.0,
			'aquario_min_cm' => 45,
			'aquario_max_cm' => 45,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'dimmer',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Varejo especializado (Water Plant Street, Pro-Aquarium, IndianAquarium) e anuncio de varejo BR na Amazon, ficha da Chihiros Marine A-Series A451M: 45 x 6 x 5 cm, 27 W, 3.500 lm, 99 LEDs (33 brancos, 50 azuis, 8 vermelhos, 8 verdes), dimmer de 6 passos, para aquarios de 45 cm',
			'fonte_url' => 'https://www.waterplantstreet.com/chihiros-a-series-led-lighting-system-marine-type.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/6Akt2vHtq4',
			'anuncio' => 'Chihiros Marine A-Series A451M 45 cm 27 W 3.850 lm bivolt',
			'loja' => 'shopee',
			'conflito' => null,
			'observacao' => 'Luminaria MARINHA: 50 dos 99 LEDs sao azuis. 3.500 lm com 27 W da 130 lm/W. A C15 dimensiona planta por lm/L e esta peca nao foi feita para planta — quando ela sair no resultado, o cartao tem de dizer que o espectro e de aquario marinho. O fabricante declara UM comprimento (45 cm), nao uma faixa.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-slim-90',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II Slim 90',
			'tipo' => 'led-barra',
			'potencia_w' => 69,
			'fluxo_lm' => 3600,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => null,
			'aquario_min_cm' => 90,
			'aquario_max_cm' => 110,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'aplicativo',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Green Aqua e Aqua Zones (varejo especializado estrangeiro), ficha da Chihiros WRGB II Slim 90: tamanho de aquario de 90 a 110 cm, consumo de 69 W, fluxo luminoso de 3.600 lm',
			'fonte_url' => 'https://www.aquazones.in/chihiros-wrgb-ii-slim-90-cm-led-light/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Fica \'parcial\' por UM campo: nenhuma das fichas conferidas publica o comprimento da PECA da Slim 90 — a irma de 120 cm publica 1184 x 128 x 15 mm e esta nao publica nada. E ausencia de fonte, nao de importancia: o comprimento da peca nao entra no criterio da C15 (que dimensiona por lumen e por cobertura declarada), entao o registro continua sendo sugerido normalmente. disponibilidade_br ficou \'desconhecido\' porque nenhuma das lojas brasileiras conferidas em 09/09/2026 anuncia a versao Slim, so a WRGB II e a WRGB II Pro. O registro entra porque a C15 dimensiona por lumen e cobertura, nao por loja, e porque a Slim e o contraponto util da familia: mesma cobertura de 90 a 110 cm com 3.600 lm contra os 9.250 lm da Pro — 2,6 vezes menos luz no mesmo aquario, o que separa exigencia baixa de exigencia alta melhor do que qualquer regra de bolso.',
		),
		array(
			'id' => 'ista-il-401-60',
			'marca' => 'Ista',
			'modelo' => 'IL-401 60 cm',
			'tipo' => 'led-calha',
			'potencia_w' => 35,
			'fluxo_lm' => 3717,
			'kelvin' => null,
			'espectro' => null,
			'peca_cm' => 56,
			'aquario_min_cm' => 56,
			'aquario_max_cm' => 66,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha da luminaria Ista IL-401 60 cm para aquarios plantados',
			'fonte_url' => 'https://www.proaquarista.com.br/produto/luminaria-led-ista-60-cm-p-aquarios-plantados-il-401.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => array(
				'campo' => 'comprimento_luminaria_cm',
				'tratamento' => 'nivel-mais-alto-vence',
				'valores' => array( array(
					'valor' => 60,
					'origem' => 'marketplace-anuncio',
				), array(
					'valor' => 56,
					'origem' => 'varejo',
				) ),
			),
			'observacao' => 'Unico registro da semente com lumen declarado alto (3717 lm) e agora com voltagem: em 08/09/2026 saiu do barrado e virou o registro mais forte do banco de iluminacao — 106 lm/W, cobertura declarada de 56 a 66 cm. Continua SEM link de afiliado: o anuncio disponivel na Shopee e o da variante de 45 cm (registro ista-i-401-45), com 7,6 W e 810 lm. Traz o conflito nome-contra-ficha: vendida como \'60 cm\', a peca mede 56 cm.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-slim-120',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II Slim 120',
			'tipo' => 'led-barra',
			'potencia_w' => 90,
			'fluxo_lm' => 4800,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => 118.4,
			'aquario_min_cm' => 120,
			'aquario_max_cm' => 140,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'aplicativo',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Green Aqua e Aqua Zones (varejo especializado estrangeiro), ficha da Chihiros WRGB II Slim 120: tamanho de aquario de 120 a 140 cm, consumo de 90 W, fluxo luminoso de 4.800 lm, 80 LEDs, grau de protecao IP 43, peca de 1184 x 128 x 15 mm',
			'fonte_url' => 'https://www.aquazones.in/chihiros-wrgb-ii-slim-120-cm-led-light/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Mesma razao da Slim 90 para o disponibilidade_br. A peca mede 118,4 cm e a cobertura declarada e de 120 a 140 cm: e mais um caso do padrao que a ilha ja registrou tres vezes — o numero do nome nao e o tamanho da peca, e a peca nao e a cobertura. Aqui o proprio fabricante declara os dois numeros e eles nao coincidem, o que e justamente a prova de que converter um no outro seria inventar faixa. Sobre o status: \'desconhecido\' e um valor do vocabulario, nao um campo vazio, entao o registro e COMPLETO e a C15 pode sugeri-lo. A incerteza fica onde ela existe de verdade, que e dentro do campo de disponibilidade, e a tela diz que nao confirmamos loja brasileira para este modelo.',
		),
		array(
			'id' => 'chihiros-a-series-a601',
			'marca' => 'Chihiros',
			'modelo' => 'A601',
			'tipo' => 'led-barra',
			'potencia_w' => 39,
			'fluxo_lm' => 5800,
			'kelvin' => 8000,
			'espectro' => 'branco',
			'peca_cm' => 60.0,
			'aquario_min_cm' => 60,
			'aquario_max_cm' => 60,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Chihiros Aquatic Studio, ficha da A-Series A601: consumo 39 W, fluxo luminoso 5800 lm, 117 LEDs, temperatura de cor de cerca de 8.000 K, peca de 600 mm, alimentacao AC 100-240 V 50/60 Hz, para aquario de 60 cm',
			'fonte_url' => 'https://www.chihirosaquaticstudio.com/products/chihiros-a-series-led-light',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Entrou em 09/09/2026 no bloco T3(a2), e o motivo de entrar e cobertura, nao marca: a linha A-Series e a unica do catalogo que DECLARA fluxo luminoso em toda a escada de tamanhos, e fluxo e o campo que barra a C15. As oito luminarias Soma, que cobririam de 20 a 130 cm e ja tem link de afiliado, continuam barradas porque nem a marca nem nove lojas brasileiras publicam lumen - e estimar lumen a partir do watt seria inventar numero. SEM LINK DE AFILIADO: quem gera o link e a Sentinela Estrategica. O espectro e branco de 8.000 K, sem RGB: a C15 dimensiona por lm/L e o cartao tem de dizer que esta peca nao tem a renderizacao de cor que a linha WRGB entrega. O fabricante declara UM comprimento de aquario (60 cm), nao uma faixa - a mesma leitura que ja valia para a A451M e a A901. Fica \'parcial\' por UM campo: disponibilidade_br. A ficha tecnica veio do fabricante, mas nenhuma loja brasileira foi conferida para este tamanho em 09/09/2026 - e disponibilidade no Brasil so o varejo brasileiro sustenta (nivel 4 ou 5 da escada). A C15 continua podendo sugerir: o campo que falta nao esta no minimo_para_sugerir dela.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-pro-60',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II Pro 60',
			'tipo' => 'led-barra',
			'potencia_w' => 74,
			'fluxo_lm' => 6630,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => 60,
			'aquario_min_cm' => 60,
			'aquario_max_cm' => 80,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'app',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Green Aqua (varejo especializado, HU), ficha do Chihiros WRGB II Pro 60: 74 W, 6630 lm, para aquarios de 60 a 80 cm, 60 LEDs WRGB, IP43, controle Bluetooth pelo app My Chihiros',
			'fonte_url' => 'https://greenaqua.hu/en/chihiros-wrgb-ii-pro-60-cm-led-light-60-80-cm-74-w-6630-lm.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/20vHM7AtT6',
			'anuncio' => 'Chihiros WRGB-2 PRO 60cm- Luminária P/ Aquário Plantado High',
			'loja' => 'shopee',
			'conflito' => null,
			'observacao' => 'Substitui o registro aquario-projetado-x1-fr-60w (removido em 07/09/2026: produto sem marca, sem comprimento declarado e sem anuncio real). E o unico registro do banco que declara comprimento de aquario E lumen — mas a voltagem nao e declarada em nenhuma das fontes, e voltagem e requisito para a C15 SUGERIR: enquanto nao houver, ele entra como ficha e nao como sugestao. 89,6 lm/W. O PAR ~50-60 citado pelo varejo vem \'no substrato\', sem distancia em cm: sem distancia o PPFD e inutil e o validador o rejeita (V5), entao nao foi gravado. DESTRAVADA EM 09/09/2026, na leva de fechamento de faixa: a voltagem apareceu quando a familia WRGB II inteira entrou no banco. A AquaBetta, varejo BR especializado, declara BIVOLT no titulo de dois membros diferentes da linha (WRGB2 Pro 90 cm e WRGB 2 Series 45 cm), e a ficha da serie descreve a alimentacao como entrada de 100 a 240 V por fonte externa de 12 V. Nao e inferencia de voltagem, que a ilha proibe: e declaracao de varejo sobre a linha, e a familia inteira acende pela mesma fonte externa. Consequencia direta: esta e a PRIMEIRA luminaria com link de afiliado que sai de barrada para sugerida sem ter mudado nada nela — o que faltava era um campo colhido para outro produto.',
		),
		array(
			'id' => 'chihiros-a-series-a801',
			'marca' => 'Chihiros',
			'modelo' => 'A801',
			'tipo' => 'led-barra',
			'potencia_w' => 50,
			'fluxo_lm' => 7200,
			'kelvin' => 8000,
			'espectro' => 'branco',
			'peca_cm' => 80.0,
			'aquario_min_cm' => 80,
			'aquario_max_cm' => 80,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Chihiros Aquatic Studio, ficha da A-Series A801: consumo 50 W, fluxo luminoso 7200 lm, 162 LEDs, temperatura de cor de cerca de 8.000 K, peca de 800 mm, alimentacao AC 100-240 V 50/60 Hz, para aquario de 80 cm',
			'fonte_url' => 'https://www.chihirosaquaticstudio.com/products/chihiros-a-series-led-light',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Entrou em 09/09/2026 no bloco T3(a2), e o motivo de entrar e cobertura, nao marca: a linha A-Series e a unica do catalogo que DECLARA fluxo luminoso em toda a escada de tamanhos, e fluxo e o campo que barra a C15. As oito luminarias Soma, que cobririam de 20 a 130 cm e ja tem link de afiliado, continuam barradas porque nem a marca nem nove lojas brasileiras publicam lumen - e estimar lumen a partir do watt seria inventar numero. SEM LINK DE AFILIADO: quem gera o link e a Sentinela Estrategica. O espectro e branco de 8.000 K, sem RGB: a C15 dimensiona por lm/L e o cartao tem de dizer que esta peca nao tem a renderizacao de cor que a linha WRGB entrega. O fabricante declara UM comprimento de aquario (80 cm), nao uma faixa - a mesma leitura que ja valia para a A451M e a A901. Fica \'parcial\' por UM campo: disponibilidade_br. A ficha tecnica veio do fabricante, mas nenhuma loja brasileira foi conferida para este tamanho em 09/09/2026 - e disponibilidade no Brasil so o varejo brasileiro sustenta (nivel 4 ou 5 da escada). A C15 continua podendo sugerir: o campo que falta nao esta no minimo_para_sugerir dela.',
		),
		array(
			'id' => 'chihiros-a-series-a901',
			'marca' => 'Chihiros',
			'modelo' => 'A901',
			'tipo' => 'led-barra',
			'potencia_w' => 55,
			'fluxo_lm' => 8200,
			'kelvin' => null,
			'espectro' => 'full-spectrum',
			'peca_cm' => 90.0,
			'aquario_min_cm' => 90,
			'aquario_max_cm' => 90,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => null,
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Varejo especializado internacional (Aquariums India, IndianAquarium, Water Plant Street), ficha da Chihiros A-Series A901: 90 x 6 x 5 cm, 55 W, 8.200 lm, 180 LEDs, espectro completo de 400 a 700 nm, para aquarios de 90 cm',
			'fonte_url' => 'https://www.aquariumsindia.com/shop/lighting-units/chihiros-led-lighting-system-a901/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/2BEkHXpG4E',
			'anuncio' => 'Chihiros A-Series A901 90 cm 55 W 8.200 lm bivolt',
			'loja' => 'shopee',
			'conflito' => null,
			'observacao' => '8.200 lm com 55 W da 149 lm/W, a maior eficacia do banco — numero de varejo, nao de fabricante. Atencao a geracao: a Serie A II 901, outra versao da mesma marca, e publicada com 7.200 lm pelo varejo europeu (Aquasabi); sao produtos diferentes e a ficha aqui e da A901 da A-Series. O fabricante declara UM comprimento (90 cm), nao uma faixa, entao a C15 so sugere esta luminaria para aquario de 90 cm: transformar peca de 90 cm em cobertura mais larga seria inventar faixa.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-90',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II 90',
			'tipo' => 'led-barra',
			'potencia_w' => 100,
			'fluxo_lm' => 8400,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => null,
			'aquario_min_cm' => 90,
			'aquario_max_cm' => 110,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'aplicativo',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Green Aqua e Aqua Zones (varejo especializado estrangeiro), ficha da Chihiros WRGB II 90: tamanho de aquario de 90 a 110 cm de largura, consumo de 100 W, fluxo luminoso de 8.400 lm, 90 LEDs WRGB, controle pelo aplicativo My Chihiros',
			'fonte_url' => 'https://www.aquazones.in/chihiros-wrgb-ii-90-cm-led-light/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'Entrou pela mesma razao da Pro 90: cobre a FAIXA de 90 a 110 cm, que estava vazia. O conflito de fluxo dentro de uma unica pagina de loja e o segundo achado do bloco e vale como conteudo: quando o proprio varejo especializado nao consegue manter dois numeros iguais na mesma pagina, a regra de bolso de \'lumens por litro\' que a web brasileira repete esta sendo aplicada sobre um dado que ninguem confere.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-pro-90',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II Pro 90',
			'tipo' => 'led-barra',
			'potencia_w' => 110,
			'fluxo_lm' => 9250,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => 90.0,
			'aquario_min_cm' => 90,
			'aquario_max_cm' => 110,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'aplicativo',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Fazenda Submersa e AquaBetta (varejo BR especializado), ficha da Chihiros WRGB II Pro 90 cm: tamanho da luminaria 90 x 14 x 1,8 cm, consumo de 110 W, 90 LEDs, fluxo luminoso de 9.250 lm, LEDs WRGB, grau de protecao IP 43, controlador Bluetooth integrado e aplicativo My Chihiros',
			'fonte_url' => 'https://www.fazendasubmersa.com.br/marcas/chihiros/luminaria-chihiros-wrgb-ii-pro90',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'PRIMEIRA luminaria do banco que cobre uma FAIXA acima de 80 cm em vez de um comprimento unico, e por isso e a que mais move a cobertura da C15: as duas Chihiros A-Series que ja existiam ali declaram 80 cm e 90 cm cravados, entao 95, 100, 105 e 110 cm saiam sem nenhuma opcao. 9.250 lm com 110 W da 84,1 lm/W, abaixo da Ista branca de 106 lm/W — que e exatamente o indicio do artigo da C15: o lumen e ponderado pela visao humana e desconta o azul e o vermelho, as duas faixas da clorofila, entao a luminaria feita para planta tende a marcar MENOS lumen que a calha branca de mesmo consumo.',
		),
		array(
			'id' => 'chihiros-wrgb-ii-120',
			'marca' => 'Chihiros',
			'modelo' => 'WRGB II 120',
			'tipo' => 'led-barra',
			'potencia_w' => 130,
			'fluxo_lm' => 11000,
			'kelvin' => null,
			'espectro' => 'wrgb',
			'peca_cm' => 120.0,
			'aquario_min_cm' => 120,
			'aquario_max_cm' => 140,
			'voltagem' => array( 'bivolt' ),
			'regulagem' => 'aplicativo',
			'ppfd' => null,
			'ppfd_distancia_cm' => null,
			'fonte_ref' => 'Green Aqua e Aqua Zones (varejo especializado estrangeiro), ficha da Chihiros WRGB II 120: tamanho de aquario de 120 a 140 cm de largura, consumo de 130 W, fluxo luminoso de 11.000 lm, 120 LEDs, peca de 1200 x 140 x 18 mm',
			'fonte_url' => 'https://www.aquazones.in/chihiros-wrgb-ii-120-cm-led-light/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'conflito' => null,
			'observacao' => 'O registro e completo; disponibilidade_br fica \'desconhecido\': das lojas brasileiras conferidas em 09/09/2026, so a Fazenda Submersa anuncia um modelo de 120 cm da familia, e o dela e o PRO. Este registro fecha o degrau de 120 cm que a varredura mediu VAZIO em toda a escala de exigencia. Sobre o status: \'desconhecido\' e um valor do vocabulario, nao um campo vazio, entao o registro e COMPLETO e a C15 pode sugeri-lo. A incerteza fica onde ela existe de verdade, que e dentro do campo de disponibilidade, e a tela diz que nao confirmamos loja brasileira para este modelo.',
		),
	);
	/* CATALOGO-FIM */
}
}

if ( ! function_exists( 'aquametria_c15_barrados' ) ) {
function aquametria_c15_barrados() {
	/* BARRADOS-INICIO — gerado por ferramentas/gerar-catalogo-iluminacao.py */
	return array(
		array(
			'id' => 'chihiros-wrgb-ii-pro-120',
			'nome' => 'Chihiros WRGB II Pro 120',
			'motivo' => 'não declara o fluxo luminoso (lúmens); não declara a potência',
			'tem_link' => false,
		),
		array(
			'id' => 'soma-s-200-wrgb',
			'nome' => 'Soma S-200',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-300-wrgb',
			'nome' => 'Soma S-300',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-400-wrgb',
			'nome' => 'Soma S-400',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'sunsun-ade-400c',
			'nome' => 'SunSun ADE-400c',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-500-wrgb',
			'nome' => 'Soma S-500',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-600-wrgb',
			'nome' => 'Soma S-600',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-800-wrgb',
			'nome' => 'Soma S-800',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-1000-wrgb',
			'nome' => 'Soma S-1000',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'soma-s-1200-wrgb',
			'nome' => 'Soma S-1200',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => true,
		),
		array(
			'id' => 'wfish-wf-h600-wrgb',
			'nome' => 'WFish WF-H600 WRGB',
			'motivo' => 'não declara o fluxo luminoso (lúmens)',
			'tem_link' => false,
		),
	);
	/* BARRADOS-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_css' ) ) {
function aquametria_c15_css() {
	return <<<'CSS'
.aqm-c15{--c15-tinta:var(--aqm-tinta,#0D1B22);--c15-lamina:var(--aqm-lamina,#0E7C8C);
--c15-papel:var(--aqm-papel,#F4F7F7);--c15-superficie:var(--aqm-superficie,#FFFFFF);
--c15-traco:var(--aqm-traco,#DDE5E6);--c15-legenda:var(--aqm-legenda,#5C7075);
--c15-alerta:var(--aqm-alerta,#B5762A);
--c15-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c15-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c15-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c15-texto);color:var(--c15-tinta);}
.aqm-c15 *{box-sizing:border-box;}
.aqm-c15 form{margin:0;}
.aqm-c15-painel{background:var(--c15-superficie);border:1px solid var(--c15-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c15-painel h3{font-family:var(--c15-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c15-painel .aqm-c15-sub{color:var(--c15-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c15-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.9rem;}
.aqm-c15-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c15-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c15-campo .aqm-c15-dica{font-size:.74rem;color:var(--c15-legenda);line-height:1.35;}
.aqm-c15 input[type=text],.aqm-c15 select{width:100%;font-family:var(--c15-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c15-traco);border-radius:2px;background:var(--c15-superficie);color:var(--c15-tinta);}
.aqm-c15 select{font-family:var(--c15-texto);}
.aqm-c15 input:focus,.aqm-c15 select:focus{outline:2px solid var(--c15-lamina);outline-offset:1px;}
.aqm-c15 input.aqm-c15-erro{border-color:var(--c15-alerta);}
.aqm-c15-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c15-caixa input{margin-top:.2rem;}
.aqm-c15-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c15 button{font-family:var(--c15-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c15-lamina);color:var(--c15-superficie);cursor:pointer;}
.aqm-c15 button.aqm-c15-secundario{background:transparent;color:var(--c15-lamina);border:1px solid var(--c15-traco);}
.aqm-c15 button:hover{filter:brightness(1.08);}
.aqm-c15-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c15-avisos li{font-size:.88rem;color:var(--c15-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c15-resultado{margin:0 0 1.2rem;}
.aqm-c15-faixa{background:var(--c15-superficie);border:2px solid var(--c15-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c15-rotulo{font-family:var(--c15-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c15-legenda);}
.aqm-c15-valor{font-family:var(--c15-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c15-valor .aqm-c15-unidade{font-size:.95rem;font-weight:500;color:var(--c15-legenda);margin-left:.3rem;}
.aqm-c15-criterio{font-size:.83rem;color:var(--c15-legenda);line-height:1.5;margin:0;}
.aqm-c15-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c15-cartao{background:var(--c15-superficie);border:1px solid var(--c15-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c15-cartao .aqm-c15-valor{font-size:1.5rem;}
.aqm-c15-nota{border-left:3px solid var(--c15-lamina);background:var(--c15-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c15-legenda);margin:0 0 1rem;}
.aqm-c15-nota strong{color:var(--c15-tinta);}
.aqm-c15-nota.aqm-c15-nota-alerta{border-left-color:var(--c15-alerta);}
.aqm-c15-produtos{margin:0 0 1.2rem;}
.aqm-c15-produtos h3{font-family:var(--c15-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c15-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c15-produto{background:var(--c15-superficie);border:1px solid var(--c15-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c15-placa{background:var(--c15-papel);border:1px solid var(--c15-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c15-placa .aqm-c15-marca{font-family:var(--c15-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c15-placa .aqm-c15-numero{font-family:var(--c15-mono);font-size:1.15rem;font-weight:600;color:var(--c15-lamina);line-height:1.1;}
.aqm-c15-placa .aqm-c15-un{font-family:var(--c15-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c15-legenda);}
.aqm-c15-produto h4{font-family:var(--c15-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c15-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c15-porque strong{font-family:var(--c15-mono);font-size:.86rem;}
.aqm-c15-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c15-legenda);line-height:1.5;}
.aqm-c15-ficha li{margin:0;}
.aqm-c15-ficha b{font-family:var(--c15-mono);font-weight:600;color:var(--c15-tinta);}
.aqm-c15-loja{display:inline-block;font-family:var(--c15-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c15-lamina);color:var(--c15-superficie);text-decoration:none;}
.aqm-c15-loja:hover{filter:brightness(1.08);color:var(--c15-superficie);}
.aqm-c15-semloja{font-size:.82rem;color:var(--c15-legenda);font-style:italic;}
.aqm-c15-aviso-afiliado,.aqm-c15-aviso-tabela{background:var(--c15-papel);border:1px solid var(--c15-traco);border-left:3px solid var(--c15-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c15-legenda);margin:1rem 0 0;}
.aqm-c15-aviso-afiliado strong,.aqm-c15-aviso-tabela strong{color:var(--c15-tinta);}
.aqm-c15-citar{background:var(--c15-papel);border:1px dashed var(--c15-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c15-citar p{margin:0 0 .6rem;}
.aqm-c15-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c15-fontes,.aqm-c15-exemplos{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c15-fontes th,.aqm-c15-fontes td,.aqm-c15-exemplos th,.aqm-c15-exemplos td{border:1px solid var(--c15-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c15-fontes th,.aqm-c15-exemplos th{background:var(--c15-papel);font-family:var(--c15-display);font-size:.8rem;}
.aqm-c15-fontes td:first-child,.aqm-c15-exemplos td:first-child{font-family:var(--c15-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c15-leituras{width:100%;min-width:30rem;font-size:.88rem;border-collapse:collapse;margin:.6rem 0 0;}
.aqm-c15-leituras th,.aqm-c15-leituras td{border:1px solid var(--c15-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c15-leituras th{background:var(--c15-papel);font-family:var(--c15-display);font-size:.8rem;}
.aqm-c15-leituras td.aqm-c15-num,.aqm-c15-leituras th.aqm-c15-num{font-family:var(--c15-mono);white-space:nowrap;font-variant-numeric:tabular-nums;}
.aqm-c15-leituras tr.aqm-c15-linha-escolhida td{background:var(--c15-papel);font-weight:600;}
.aqm-c15-selo{display:inline-block;font-family:var(--c15-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c15-alerta);border:1px solid var(--c15-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c15-barrados{list-style:none;margin:.6rem 0 0;padding:0;font-size:.85rem;color:var(--c15-legenda);line-height:1.5;}
.aqm-c15-barrados li{margin:0 0 .35rem;padding-left:1rem;position:relative;}
.aqm-c15-barrados li:before{content:"—";position:absolute;left:0;color:var(--c15-alerta);}
.aqm-c15-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c15-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c15-oculto{display:none;}
@media (max-width:600px){.aqm-c15-valor{font-size:1.6rem;}
.aqm-c15-produto{grid-template-columns:1fr;}
.aqm-c15-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_js' ) ) {
function aquametria_c15_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var K_MIN = 6500, K_MAX = 8000;      /* temperatura-de-cor */
	var LAMINA_FUNDA = 45;               /* convenção editorial declarada */

	/* Constante 'iluminacao-lumen-por-litro'. Três fontes brasileiras, o mesmo
	   rótulo, números diferentes. A faixa consolidada é a união do que as três
	   afirmam; as leituras individuais saem na tela, com o nome de cada uma.
	   Nada aqui é média: média apagaria justamente o que a página tem a dizer. */
	var NIVEIS = {
		baixa: {
			rotulo: 'plantas de baixa exigência',
			exemplo: 'anúbias, musgos, samambaias e cripitas — as que crescem devagar e vivem à sombra',
			consolidado: [10, 20],
			leituras: [
				{ fonte: 'peixeseaquarismo', faixa: [20, 20] },
				{ fonte: 'aquarioturbinado', faixa: [10, 20] },
				{ fonte: 'aquariosplantados', faixa: [15, 15] }
			]
		},
		media: {
			rotulo: 'plantas de exigência média',
			exemplo: 'a maioria das plantas de haste, vallisnerias e echinodorus',
			consolidado: [20, 40],
			leituras: [
				{ fonte: 'peixeseaquarismo', faixa: [30, 40] },
				{ fonte: 'aquarioturbinado', faixa: [20, 40] },
				{ fonte: 'aquariosplantados', faixa: [30, 30] }
			]
		},
		alta: {
			rotulo: 'plantas de alta exigência',
			exemplo: 'carpetes, plantas vermelhas e o aquário plantado de competição',
			consolidado: [40, 60],
			leituras: [
				{ fonte: 'peixeseaquarismo', faixa: [60, 60] },
				{ fonte: 'aquarioturbinado', faixa: [40, null] },
				{ fonte: 'aquariosplantados', faixa: [60, 60] }
			]
		}
	};

	/* Constante 'fotoperiodo'. Quatro regimes, cada um com a sua faixa. */
	var FOTOPERIODO = {
		lowtech:  { rotulo: 'low tech (sem CO2)',   faixa: [6, 8] },
		hightech: { rotulo: 'high tech (com CO2)',  faixa: [8, 10] },
		alga:     { rotulo: 'combate a alga',       faixa: [5, 6] },
		ciclagem: { rotulo: 'durante a ciclagem',   faixa: [4, 6] }
	};

	/* Constante 'co2-concentracao'. Os dois extremos SE SOBREPÕEM: 35 mg/L é ao
	   mesmo tempo teto da faixa útil e início da faixa tóxica. A tela mostra a
	   sobreposição em vez de escolher um número. */
	var CO2 = { util: [15, 35], toxico: [30, 35] };

	var raiz = document.querySelector('.aqm-c15');
	if (!raiz) { return; }

	function el(id) { return raiz.querySelector('#' + id); }

	function num(v) {
		if (v === null || v === undefined) { return null; }
		var t = String(v).trim().replace(/\s/g, '').replace(',', '.');
		if (t === '') { return null; }
		var n = parseFloat(t);
		return isFinite(n) ? n : null;
	}

	function fmt(n, casas) {
		if (n === null || n === undefined || !isFinite(n)) { return '—'; }
		return n.toLocaleString('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas });
	}

	/* Lúmen é número grosso: arredondar para a dezena (ou a centena, acima de
	   10 000) evita a falsa precisão de "2 137 lm". */
	function lm(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		var passo = n >= 10000 ? 100 : 10;
		return fmt(Math.round(n / passo) * passo, 0);
	}

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	/* O banco de produtos e escrito sem acento, de proposito, e a tela da
	   Aquametria sai acentuada: por isso o gerador manda a ESTRUTURA do conflito
	   (campo, valor e origem de cada leitura) e a frase e escrita aqui. */
	var ROTULO_ORIGEM = {
		'fabricante': 'o fabricante',
		'fabricante-via-busca': 'o fabricante',
		'manual': 'o manual',
		'varejo': 'a ficha do varejo especializado',
		'marketplace-anuncio': 'o nome comercial do anúncio',
		'medicao-propria': 'a nossa medição'
	};

	var ROTULO_CAMPO = {
		'comprimento_luminaria_cm': 'o comprimento da peça',
		'comprimento_aquario_cm': 'o comprimento de aquário coberto'
	};

	function fraseDeConflito(c) {
		var campo = ROTULO_CAMPO[c.campo] || c.campo;
		var partes = (c.valores || []).map(function (v) {
			return fmt(v.valor, 0) + ' cm segundo ' + (ROTULO_ORIGEM[v.origem] || v.origem);
		});
		return 'as fontes discordam sobre ' + campo + ': ' + partes.join(', contra ')
			+ '. Publicamos o número da fonte de maior nível e deixamos os dois à vista — '
			+ 'o número que aparece no nome do produto não é ficha técnica, e no varejo brasileiro de iluminação ele costuma indicar o aquário de destino, não a peça.';
	}

	function esc(t) {
		return String(t === null || t === undefined ? '' : t)
			.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
	}

	function dataBr(iso) {
		if (!iso) { return 'data não registrada'; }
		var p = String(iso).split('-');
		return p.length === 3 ? p[2] + '/' + p[1] + '/' + p[0] : iso;
	}

	function campos() {
		return {
			volume: num(el('aqm-c15-volume').value),
			comprimento: num(el('aqm-c15-comprimento').value),
			lamina: num(el('aqm-c15-lamina').value),
			nivel: el('aqm-c15-nivel').value,
			co2: el('aqm-c15-co2').checked,
			regime: el('aqm-c15-regime').value,
			tipo: el('aqm-c15-tipo').value
		};
	}

	/* ------------------------------------------------------------- o cálculo */

	function calcular(d) {
		var r = { erros: [], avisos: [] };

		if (d.volume === null) {
			r.erros.push({ campo: 'volume', texto: 'Informe o volume real de água do aquário, em litros.' });
		} else if (d.volume <= 0) {
			r.erros.push({ campo: 'volume', texto: 'O volume precisa ser maior que zero.' });
		} else if (d.volume > 20000) {
			r.erros.push({ campo: 'volume', texto: 'Acima de 20 000 L: confira a unidade (o campo é em litros).' });
		}
		if (d.comprimento !== null && (d.comprimento <= 0 || d.comprimento > 400)) {
			r.erros.push({ campo: 'comprimento', texto: 'Comprimento do aquário em centímetros, entre 1 e 400.' });
		}
		if (d.lamina !== null && (d.lamina <= 0 || d.lamina > 200)) {
			r.erros.push({ campo: 'lamina', texto: 'Altura da lâmina d\'água em centímetros, entre 1 e 200.' });
		}
		if (!NIVEIS[d.nivel]) { d.nivel = 'media'; }
		if (r.erros.length) { return r; }

		var V = d.volume;
		var nivel = NIVEIS[d.nivel];
		r.entradas = d;
		r.nivel = nivel;
		r.min = V * nivel.consolidado[0];
		r.max = V * nivel.consolidado[1];
		r.aberto = d.nivel === 'alta';   /* "> 40 lm/L" não tem teto declarado */

		/* Cada leitura vira lúmens no volume da pessoa, com a atribuição. */
		r.leituras = nivel.leituras.map(function (l) {
			return {
				fonte: l.fonte,
				lmL: l.faixa,
				lm_min: V * l.faixa[0],
				lm_max: l.faixa[1] === null ? null : V * l.faixa[1]
			};
		});

		/* A divergência é o resultado: mede-se pelo maior sobre o menor piso. */
		var pisos = nivel.leituras.map(function (l) { return l.faixa[0]; });
		r.divergencia = Math.max.apply(null, pisos) / Math.min.apply(null, pisos);

		/* Regime do fotoperíodo: a ciclagem e o combate a alga mandam no CO2. */
		if (d.regime === 'alga') { r.regime = FOTOPERIODO.alga; r.regime_id = 'alga'; }
		else if (d.regime === 'ciclagem') { r.regime = FOTOPERIODO.ciclagem; r.regime_id = 'ciclagem'; }
		else if (d.co2) { r.regime = FOTOPERIODO.hightech; r.regime_id = 'hightech'; }
		else { r.regime = FOTOPERIODO.lowtech; r.regime_id = 'lowtech'; }
		r.horas_medias = (r.regime.faixa[0] + r.regime.faixa[1]) / 2;

		if (d.nivel === 'alta' && !d.co2) {
			r.avisos.push('Você escolheu o nível alto sem CO2. Luz forte sem carbono disponível é a receita clássica de alga: '
				+ 'a planta não consegue usar a luz que recebe e a alga usa. As fontes que publicam 40 a 60 lm/L publicam esse número junto de CO2 injetado. '
				+ 'Ou você desce para o nível médio, ou entra CO2 na conta.');
		}
		if (d.lamina !== null && d.lamina > LAMINA_FUNDA) {
			r.avisos.push('A sua lâmina tem ' + fmt(d.lamina, 0) + ' cm, acima dos ' + LAMINA_FUNDA + ' cm em que a regra de lúmens por litro começa a mentir. '
				+ 'Lúmen por litro não sabe a que profundidade a luz precisa chegar: o mesmo número de lúmens entrega muito menos luz no substrato de um aquário fundo. '
				+ 'A medida que resolveria isso é PPFD por profundidade, e ela não está publicada aqui porque não temos fonte — veja abaixo por quê.');
		}
		if (d.comprimento === null) {
			r.avisos.push('Sem o comprimento do aquário não dá para conferir se a luminária cobre a peça inteira, e por isso a lista de produtos não aparece. '
				+ 'Luminária curta demais ilumina o meio e deixa as pontas na sombra — e nenhum varejo avisa disso.');
		}

		r.produtos = escolher(r, d);
		return r;
	}

	/* Adequação técnica, e só ela: lúmens dentro da faixa calculada e cobertura
	   de comprimento DECLARADA que contenha o aquário. Link de afiliado não entra
	   no critério nem na ordem (regra V16 do esquema do banco). */
	/* Cobertura declarada em texto. A Chihiros A-Series declara UM comprimento de
	   aquário (90 cm), não uma faixa: imprimir '90 a 90 cm' seria defeito visível. */
	function cobertura(p) {
		if (p.aquario_min_cm === null) { return 'até ' + fmt(p.aquario_max_cm, 0) + ' cm'; }
		if (p.aquario_max_cm === null) { return 'a partir de ' + fmt(p.aquario_min_cm, 0) + ' cm'; }
		if (p.aquario_min_cm === p.aquario_max_cm) { return 'exatamente ' + fmt(p.aquario_min_cm, 0) + ' cm'; }
		return fmt(p.aquario_min_cm, 0) + ' a ' + fmt(p.aquario_max_cm, 0) + ' cm';
	}

	function escolher(r, d) {
		var fora = [];
		var regulaveis = [];
		var dentro = [];

		if (d.comprimento === null) {
			r.fora_da_lista = fora;
			r.regulaveis = regulaveis;
			return dentro;
		}

		AQM_C15_CATALOGO.forEach(function (p) {
			if (d.tipo !== 'qualquer' && p.tipo !== d.tipo) { return; }

			var cobre = (p.aquario_min_cm === null || d.comprimento >= p.aquario_min_cm)
				&& (p.aquario_max_cm === null || d.comprimento <= p.aquario_max_cm);
			if (!cobre) {
				fora.push(nome(p) + ' entrega ' + lm(p.fluxo_lm) + ' lm, mas o fabricante declara cobertura de '
					+ cobertura(p)
					+ ' de aquário, e o seu tem ' + fmt(d.comprimento, 0) + ' cm.');
				return;
			}
			if (p.fluxo_lm >= r.min && (r.aberto || p.fluxo_lm <= r.max)) {
				dentro.push(p);
				return;
			}
			if (p.fluxo_lm > r.max && podeRegular(p)) {
				regulaveis.push(p);
				return;
			}
			fora.push(nome(p) + ' entrega ' + lm(p.fluxo_lm) + ' lm, '
				+ (p.fluxo_lm < r.min ? 'abaixo dos ' + lm(r.min) + ' lm que o seu aquário pede neste nível'
					: 'acima dos ' + lm(r.max) + ' lm do nível escolhido, e não declara regulagem de intensidade')
				+ '.');
		});

		var meio = (r.min + r.max) / 2;
		dentro.sort(function (a, b) {
			return Math.abs(a.fluxo_lm - meio) - Math.abs(b.fluxo_lm - meio);
		});
		regulaveis.sort(function (a, b) { return a.fluxo_lm - b.fluxo_lm; });

		r.fora_da_lista = fora;
		r.regulaveis = regulaveis.slice(0, 2);
		return dentro.slice(0, 5);
	}

	/* Temporizador não regula intensidade: liga e desliga. Só dimmer, app e
	   controlador permitem baixar a luz de um modelo acima da faixa. */
	function podeRegular(p) {
		return p.regulagem === 'dimmer' || p.regulagem === 'app' || p.regulagem === 'controlador';
	}

	function nome(p) {
		return (p.marca ? p.marca + ' ' : '') + p.modelo;
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c15-saida');
		var ul = el('aqm-c15-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c15-erro').forEach(function (n) { n.classList.remove('aqm-c15-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c15-' + er.campo);
				if (campo) { campo.classList.add('aqm-c15-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c15-oculto');
			return;
		}

		alvo.classList.remove('aqm-c15-oculto');

		el('aqm-c15-faixa-valor').innerHTML = lm(r.min) + ' a ' + lm(r.max) + (r.aberto ? '+' : '')
			+ '<span class="aqm-c15-unidade">lúmens</span>';
		el('aqm-c15-faixa-criterio').textContent =
			'Para ' + litros(r.entradas.volume) + ' L de água e ' + r.nivel.rotulo + ', na faixa consolidada de '
			+ fmt(r.nivel.consolidado[0], 0) + ' a ' + fmt(r.nivel.consolidado[1], 0) + (r.aberto ? '+' : '') + ' lm/L. '
			+ 'Essa faixa não é a média das fontes: é o que as três, juntas, sustentam. Isoladas, elas discordam por '
			+ fmt(r.divergencia, 1) + ' vezes sobre o mesmo rótulo — a tabela abaixo mostra quem publicou o quê.'
			+ (r.aberto ? ' O nível alto não tem teto declarado: uma das fontes escreve "acima de 40 lm/L" e para por aí.' : '');

		pintarLeituras(r);

		var lista = el('aqm-c15-cartoes');
		lista.innerHTML = '';

		lista.appendChild(cartao(
			'Fotoperíodo — ' + r.regime.rotulo,
			fmt(r.regime.faixa[0], 0) + ' a ' + fmt(r.regime.faixa[1], 0) + '<span class="aqm-c15-unidade">h/dia</span>',
			'É o regime que corresponde ao que você marcou. Fotoperíodo é hora de luz por dia, contínua ou em duas sessões; '
			+ 'os outros três regimes estão logo abaixo, porque o seu aquário pode passar por todos eles.'
		));

		lista.appendChild(cartao(
			'Temperatura de cor',
			fmt(K_MIN, 0) + ' a ' + fmt(K_MAX, 0) + '<span class="aqm-c15-unidade">K</span>',
			'Faixa que as fontes brasileiras repetem para aquário plantado. Abaixo de 6500 K a água puxa para o amarelo e '
			+ 'a planta perde a faixa azul; acima de 8000 K o visual esfria. Kelvin é aparência e espectro, não quantidade de luz: '
			+ 'não substitui os lúmens acima.'
		));

		lista.appendChild(cartao(
			'Consumo do fotoperíodo',
			fmt(kwhMes(potenciaAlvo(r), r.horas_medias), 1) + '<span class="aqm-c15-unidade">kWh/mês</span>',
			potenciaAlvo(r) === null
				? 'Informe a potência da sua luminária no painel de consumo abaixo para ver este número no seu caso.'
				: 'Com ' + fmt(potenciaAlvo(r), 0) + ' W ligados ' + fmt(r.horas_medias, 1) + ' h por dia, 30 dias. '
					+ 'Custo em reais só sai com a sua tarifa: não publicamos tarifa de energia, ela muda por distribuidora e por bandeira.'
		));

		pintarFotoperiodos(r);
		pintarCo2(r);

		var av = el('aqm-c15-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		pintarProdutos(r);
		pintarConsumo(r);

		el('aqm-c15-citacao').textContent =
			'Aquário de ' + litros(r.entradas.volume) + ' L de água real, ' + r.nivel.rotulo + ': a iluminação pedida vai de '
			+ lm(r.min) + ' a ' + lm(r.max) + (r.aberto ? '+' : '') + ' lúmens ('
			+ fmt(r.nivel.consolidado[0], 0) + ' a ' + fmt(r.nivel.consolidado[1], 0) + ' lm/L), com fotoperíodo de '
			+ fmt(r.regime.faixa[0], 0) + ' a ' + fmt(r.regime.faixa[1], 0) + ' h/dia no regime ' + r.regime.rotulo
			+ ' e temperatura de cor de ' + fmt(K_MIN, 0) + ' a ' + fmt(K_MAX, 0) + ' K. '
			+ 'As três fontes brasileiras do levantamento discordam por ' + fmt(r.divergencia, 1) + ' vezes sobre esse mesmo rótulo. '
			+ 'Calculado pela Aquametria, ' + AQM_C15_DATA + '.';

		guardar(r);
		atualizarEndereco(r.entradas);
	}

	function cartao(rotulo, valor, criterio) {
		var li = document.createElement('li');
		li.className = 'aqm-c15-cartao';
		var t = document.createElement('span');
		t.className = 'aqm-c15-rotulo';
		t.textContent = rotulo;
		var v = document.createElement('span');
		v.className = 'aqm-c15-valor';
		v.innerHTML = valor;
		var c = document.createElement('p');
		c.className = 'aqm-c15-criterio';
		c.textContent = criterio;
		li.appendChild(t); li.appendChild(v); li.appendChild(c);
		return li;
	}

	/* A honestidade número 1 da página: as três leituras, sem média. */
	function pintarLeituras(r) {
		var corpo = el('aqm-c15-leituras-corpo');
		corpo.innerHTML = '';
		var V = r.entradas.volume;

		Object.keys(NIVEIS).forEach(function (chave) {
			var n = NIVEIS[chave];
			n.leituras.forEach(function (l, i) {
				var tr = document.createElement('tr');
				if (chave === r.entradas.nivel) { tr.className = 'aqm-c15-linha-escolhida'; }
				var faixaTexto = l.faixa[1] === null
					? 'acima de ' + fmt(l.faixa[0], 0)
					: (l.faixa[0] === l.faixa[1] ? fmt(l.faixa[0], 0) : fmt(l.faixa[0], 0) + ' a ' + fmt(l.faixa[1], 0));
				var lmTexto = l.faixa[1] === null
					? 'acima de ' + lm(V * l.faixa[0])
					: (l.faixa[0] === l.faixa[1] ? lm(V * l.faixa[0]) : lm(V * l.faixa[0]) + ' a ' + lm(V * l.faixa[1]));
				tr.innerHTML = '<td>' + (i === 0 ? esc(n.rotulo) : '') + '</td>'
					+ '<td>' + esc(l.fonte) + '</td>'
					+ '<td class="aqm-c15-num">' + faixaTexto + '</td>'
					+ '<td class="aqm-c15-num">' + lmTexto + '</td>';
				corpo.appendChild(tr);
			});
		});

		el('aqm-c15-leituras-nota').textContent =
			'Três fontes brasileiras, o mesmo rótulo, números que diferem por até ' + fmt(r.divergencia, 1)
			+ ' vezes. Nenhuma das três publica de onde tirou o número, e nenhuma cita as outras duas. '
			+ 'Por isso a resposta acima é uma faixa com atribuição, e não a média: a média inventaria um consenso que não existe.';
	}

	function pintarFotoperiodos(r) {
		var ul = el('aqm-c15-fotoperiodos');
		ul.innerHTML = '';
		Object.keys(FOTOPERIODO).forEach(function (chave) {
			var f = FOTOPERIODO[chave];
			var li = document.createElement('li');
			li.className = 'aqm-c15-criterio';
			li.innerHTML = '<b>' + esc(f.rotulo) + '</b>: ' + fmt(f.faixa[0], 0) + ' a ' + fmt(f.faixa[1], 0) + ' h/dia'
				+ (chave === r.regime_id ? ' — <strong>é o seu caso agora</strong>' : '');
			ul.appendChild(li);
		});
	}

	function pintarCo2(r) {
		var bloco = el('aqm-c15-co2-bloco');
		if (r.entradas.nivel !== 'alta' && !r.entradas.co2) {
			bloco.classList.add('aqm-c15-oculto');
			return;
		}
		bloco.classList.remove('aqm-c15-oculto');
		el('aqm-c15-co2-texto').innerHTML =
			'A faixa útil publicada é de <b>' + fmt(CO2.util[0], 0) + ' a ' + fmt(CO2.util[1], 0) + ' mg/L</b>, e a mesma fonte diz que '
			+ '<b>acima de ' + fmt(CO2.toxico[0], 0) + ' a ' + fmt(CO2.toxico[1], 0) + ' mg/L</b> há risco de toxicidade para os peixes. '
			+ 'Repare que os dois extremos se sobrepõem: 35 mg/L é ao mesmo tempo o teto do que é útil e o começo do que é perigoso. '
			+ 'Não escolhemos um lado dessa sobreposição, porque a fonte não escolheu — e porque, entre errar para mais e errar para menos, '
			+ 'errar para mais mata peixe. O que resolve não é conta: é medição. '
			+ 'O drop checker mostra <b>azul</b> para CO2 baixo, <b>verde</b> para dentro da faixa e <b>amarelo</b> para excesso, '
			+ 'com um atraso de 1 a 2 horas em relação ao que está acontecendo na água.';
	}

	/* ------------------------------------------------------------- produtos */

	function pintarProdutos(r) {
		var bloco = el('aqm-c15-produtos');
		var lista = el('aqm-c15-produtos-lista');
		var nada = el('aqm-c15-produtos-nada');
		lista.innerHTML = '';

		if (!r.produtos.length && !(r.regulaveis || []).length) {
			bloco.classList.add('aqm-c15-oculto');
			nada.classList.remove('aqm-c15-oculto');
			nada.textContent = r.entradas.comprimento === null
				? 'A lista de luminárias só aparece com o comprimento do aquário preenchido: sem ele não dá para conferir se a peça cobre o seu vidro, '
					+ 'e recomendar luminária que deixa as pontas na sombra seria pior que não recomendar nada.'
				: 'Nenhuma luminária do nosso banco entrega entre ' + lm(r.min) + ' e ' + lm(r.max) + ' lm com cobertura declarada para um aquário de '
					+ fmt(r.entradas.comprimento, 0) + ' cm'
					+ (r.entradas.tipo !== 'qualquer' ? ' no tipo que você escolheu' : '') + '. '
					+ 'O banco tem ' + AQM_C15_CATALOGO.length + ' luminária(s) com ficha completa hoje, e '
					+ AQM_C15_BARRADOS.length + ' que existem no banco e não podem ser sugeridas (a lista e o motivo estão logo abaixo). '
					+ 'Preferimos não mostrar produto nenhum a mostrar um que não atende o seu número.';
			pintarBarrados(r);
			return;
		}

		nada.classList.add('aqm-c15-oculto');
		bloco.classList.remove('aqm-c15-oculto');
		el('aqm-c15-produtos-sub').textContent =
			'São as luminárias do nosso banco cujo fluxo declarado cai dentro da faixa que o seu aquário pede — ' + lm(r.min) + ' a '
			+ lm(r.max) + ' lm — e cujo fabricante ou lojista declara cobrir um aquário de ' + fmt(r.entradas.comprimento, 0) + ' cm. '
			+ 'A ordem é por proximidade do meio da faixa. Nada aqui é ordenado por comissão, e modelo sem link de loja aparece do mesmo jeito.';

		r.produtos.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r, false));
		});
		(r.regulaveis || []).forEach(function (p) {
			lista.appendChild(produtoHtml(p, r, true));
		});

		if (r.fora_da_lista && r.fora_da_lista.length) {
			var li = document.createElement('li');
			li.className = 'aqm-c15-criterio';
			li.textContent = 'Fora da lista neste aquário: ' + r.fora_da_lista.join(' ');
			lista.appendChild(li);
		}

		pintarBarrados(r);
	}

	/* A lista dos que o banco tem e a calculadora NÃO pode sugerir. Ela é
	   conteúdo, não desculpa: é o retrato da lacuna da entidade. */
	function pintarBarrados(r) {
		var ul = el('aqm-c15-barrados');
		ul.innerHTML = '';
		if (!AQM_C15_BARRADOS.length) {
			el('aqm-c15-barrados-bloco').classList.add('aqm-c15-oculto');
			return;
		}
		el('aqm-c15-barrados-bloco').classList.remove('aqm-c15-oculto');
		AQM_C15_BARRADOS.forEach(function (b) {
			var li = document.createElement('li');
			li.innerHTML = '<b>' + esc(b.nome) + '</b> — ' + esc(b.motivo) + '.'
				+ (b.tem_link ? ' <em>Tem link de afiliado no nosso painel e mesmo assim não é sugerida: link não promove produto barrado.</em>' : '');
			ul.appendChild(li);
		});
	}

	function produtoHtml(p, r, acimaComRegulagem) {
		var V = r.entradas.volume;
		var lmL = p.fluxo_lm / V;

		var li = document.createElement('li');
		li.className = 'aqm-c15-produto';

		var placa = document.createElement('div');
		placa.className = 'aqm-c15-placa';
		placa.innerHTML = '<span class="aqm-c15-marca">' + esc(p.marca || 'sem marca declarada') + '</span>'
			+ '<span class="aqm-c15-numero">' + lm(p.fluxo_lm) + '</span>'
			+ '<span class="aqm-c15-un">lúmens</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = nome(p);
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c15-porque';
		porque.innerHTML = 'No seu aquário de ' + litros(V) + ' L, esta luminária entrega <strong>'
			+ fmt(Math.round(lmL * 10) / 10, 1) + ' lm/L</strong>, que fica '
			+ (acimaComRegulagem
				? 'ACIMA da faixa de ' + fmt(r.nivel.consolidado[0], 0) + ' a ' + fmt(r.nivel.consolidado[1], 0)
					+ ' lm/L do nível escolhido. Ela está aqui porque tem regulagem de intensidade (' + esc(p.regulagem)
					+ '): dá para trabalhar abaixo do máximo. Sem regulagem, um modelo acima da faixa não teria como ser recomendado.'
				: 'dentro da faixa de ' + fmt(r.nivel.consolidado[0], 0) + ' a ' + fmt(r.nivel.consolidado[1], 0)
					+ ' lm/L que este nível pede.')
			+ ' A cobertura declarada é de '
			+ cobertura(p)
			+ ' de aquário, e o seu tem ' + fmt(r.entradas.comprimento, 0) + ' cm.';
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c15-ficha';
		var linhas = [
			'Tipo: <b>' + esc(p.tipo) + '</b>',
			'Potência: <b>' + fmt(p.potencia_w, 0) + ' W</b> — eficácia de <b>'
				+ fmt(Math.round((p.fluxo_lm / p.potencia_w) * 10) / 10, 1) + ' lm/W</b> (cálculo nosso, a partir dos dois números declarados)',
			'Comprimento da peça: <b>' + (p.peca_cm === null ? 'não declarado' : fmt(p.peca_cm, 1) + ' cm') + '</b>',
			'Voltagem: <b>' + (p.voltagem.length ? p.voltagem.join(' ou ') : 'não declarada') + '</b>',
			'Regulagem: <b>' + (p.regulagem ? esc(p.regulagem) : 'não declarada') + '</b>'
		];
		if (p.kelvin) { linhas.push('Temperatura de cor: <b>' + fmt(p.kelvin, 0) + ' K</b>'); }
		if (p.espectro) { linhas.push('Espectro: <b>' + esc(p.espectro) + '</b>'); }
		linhas.push('Consumo no seu fotoperíodo: <b>' + fmt(kwhMes(p.potencia_w, r.horas_medias), 1) + ' kWh/mês</b> ('
			+ fmt(r.horas_medias, 1) + ' h/dia, 30 dias)');
		if (p.ppfd && p.ppfd_distancia_cm) {
			linhas.push('PPFD declarado: <b>' + fmt(p.ppfd, 0) + ' µmol/m²/s a ' + fmt(p.ppfd_distancia_cm, 0) + ' cm</b>');
		} else {
			linhas.push('PPFD declarado: <b>nenhum</b> — como em todo o resto do banco');
		}
		if (p.conflito) { linhas.push('<span class="aqm-c15-selo">conflito registrado</span> ' + fraseDeConflito(p.conflito)); }
		linhas.push('Ficha conferida em ' + esc(dataBr(p.verificado_em))
			+ (p.fonte_url ? ' — <a href="' + esc(p.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (p.fonte_status ? ' (' + esc(p.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (p.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c15-loja';
			a.href = p.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja);
			corpo.appendChild(a);
			var nota = document.createElement('p');
			nota.className = 'aqm-c15-semloja';
			nota.textContent = 'Link patrocinado. Confira no anúncio a voltagem e o comprimento exato antes de comprar — '
				+ 'o anúncio não é nossa fonte técnica, e a ficha acima é.';
			corpo.appendChild(nota);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c15-semloja';
			sem.textContent = 'Ainda não temos link de loja para este modelo. Ele aparece aqui porque atende ao seu número, e é só isso que decide a lista.';
			corpo.appendChild(sem);
		}

		li.appendChild(placa);
		li.appendChild(corpo);
		return li;
	}

	/* ------------------------------------------------------------- consumo */

	function kwhMes(w, horas) {
		if (w === null || !isFinite(w)) { return null; }
		return w * horas * 30 / 1000;
	}

	/* A potência que o painel de consumo usa: a que a pessoa digitou; se não
	   digitou, a do primeiro produto sugerido; se não há produto, nada. */
	function potenciaAlvo(r) {
		var digitada = num(el('aqm-c15-watts').value);
		if (digitada !== null && digitada > 0) { return digitada; }
		if (r.produtos && r.produtos.length) { return r.produtos[0].potencia_w; }
		return null;
	}

	function pintarConsumo(r) {
		var w = potenciaAlvo(r);
		var tarifa = num(el('aqm-c15-tarifa').value);
		var saida = el('aqm-c15-consumo-saida');

		if (w === null) {
			saida.textContent = 'Informe a potência da luminária, em watts — é o número que vem na caixa e na etiqueta da peça.';
			return;
		}

		var kwh = kwhMes(w, r.horas_medias);
		var texto = fmt(w, 0) + ' W ligados ' + fmt(r.horas_medias, 1) + ' h por dia consomem '
			+ fmt(kwh, 1) + ' kWh por mês, ou ' + fmt(kwh * 12, 0) + ' kWh por ano. '
			+ 'Essa parte é física: potência vezes horas, sem margem de erro nem divergência de fonte. ';
		if (tarifa !== null && tarifa > 0) {
			texto += 'Com a tarifa de R$ ' + fmt(tarifa, 2) + ' por kWh que você informou, dá R$ ' + fmt(kwh * tarifa, 2)
				+ ' por mês e R$ ' + fmt(kwh * tarifa * 12, 2) + ' por ano. Esse número é seu: usamos a sua tarifa, não uma média nossa.';
		} else {
			texto += 'Para ver em reais, informe a tarifa da sua conta de luz (R$ por kWh, o valor com impostos). '
				+ 'Não publicamos uma tarifa padrão: ela muda por distribuidora, por bandeira e por faixa de consumo, e um número velho na tela seria pior que nenhum.';
		}
		texto += ' Comparação útil: no mesmo mês, o filtro fica ligado 24 h por dia e a luz só ' + fmt(r.horas_medias, 1) + ' h.';
		saida.textContent = texto;
	}

	/* ------------------------------------------- o caminho inverso */

	function inverso() {
		var q = num(el('aqm-c15-tenho').value);
		var V = num(el('aqm-c15-volume').value);
		var saida = el('aqm-c15-tenho-saida');

		if (q === null || q <= 0) {
			saida.textContent = 'Informe o fluxo luminoso da luminária, em lúmens. Se a caixa não traz esse número — o que é comum no Brasil — '
				+ 'ela não pode ser dimensionada por esta regra, e a página explica isso mais abaixo.';
			return;
		}

		var partes = [];
		Object.keys(NIVEIS).forEach(function (chave) {
			var n = NIVEIS[chave];
			var vmax = q / n.consolidado[0];
			var vmin = n.consolidado[1] === null ? null : q / n.consolidado[1];
			partes.push(n.rotulo + ': de ' + litros(vmin) + ' a ' + litros(vmax) + ' L');
		});

		var texto = 'Uma luminária de ' + lm(q) + ' lm cobre, pela faixa consolidada de cada nível — ' + partes.join('; ') + '. ';

		if (V !== null && V > 0) {
			var lmL = q / V;
			var onde = lmL < 10 ? 'abaixo até do piso do nível baixo: para planta, é pouco em qualquer leitura'
				: (lmL <= 20 ? 'no nível de baixa exigência'
					: (lmL <= 40 ? 'no nível médio'
						: 'no nível alto, que as fontes só publicam junto de CO2 injetado'));
			texto += 'No seu aquário de ' + litros(V) + ' L, ela entrega ' + fmt(Math.round(lmL * 10) / 10, 1) + ' lm/L, o que a coloca ' + onde + '. ';
		}
		texto += 'Lembre que lúmen é luz que o olho humano enxerga, não luz que a planta usa: duas luminárias de mesmo lúmen e espectros diferentes '
			+ 'não entregam a mesma fotossíntese. A grandeza certa seria PPFD, e ela não está publicada aqui porque não temos fonte.';
		saida.textContent = texto;
	}

	/* ------------------------------------------------- estado compartilhado */

	function recuperar() {
		try {
			var bruto = window.localStorage.getItem(CHAVE);
			if (!bruto) { return null; }
			var o = JSON.parse(bruto);
			return (o && typeof o === 'object') ? o : null;
		} catch (erro) { return null; }
	}

	/* Mescla: a C1 é dona das medidas e dos volumes, e esta calculadora não
	   pode apagar o que ela nem as outras gravaram. Só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c15-iluminacao' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.entradas.volume) {
			estado.volumes.real_L = r.entradas.volume;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C15'; }
		}
		if (r.entradas.comprimento !== null) {
			estado.medidas = estado.medidas || {};
			if (!estado.medidas.comprimento_cm) { estado.medidas.comprimento_cm = r.entradas.comprimento; }
		}
		estado.iluminacao = {
			nivel_planta: r.entradas.nivel,
			lumens_alvo: [Math.round(r.min), Math.round(r.max)],
			lm_por_L: r.nivel.consolidado,
			fotoperiodo_h: r.regime.faixa,
			regime: r.regime_id,
			usa_co2: !!r.entradas.co2
		};
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c15-guardado').classList.remove('aqm-c15-oculto');
		} catch (erro) {
			el('aqm-c15-guardado').classList.add('aqm-c15-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'n=' + d.nivel, 'rg=' + d.regime, 't=' + d.tipo];
		if (d.comprimento !== null) { q.push('c=' + d.comprimento); }
		if (d.lamina !== null) { q.push('lam=' + d.lamina); }
		if (d.co2) { q.push('co2=1'); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c15-link').value = window.location.origin + url;
	}

	function lerQuery() {
		var busca = window.location.search;
		if (!busca || busca.length < 2) { return null; }
		var fora = {};
		busca.substring(1).split('&').forEach(function (par) {
			var p = par.split('=');
			if (p.length === 2) { fora[decodeURIComponent(p[0])] = decodeURIComponent(p[1]); }
		});
		return fora.v ? fora : null;
	}

	function preencher(fora) {
		if (fora.v) { el('aqm-c15-volume').value = fora.v; }
		if (fora.c) { el('aqm-c15-comprimento').value = fora.c; }
		if (fora.lam) { el('aqm-c15-lamina').value = fora.lam; }
		if (fora.n && NIVEIS[fora.n]) { el('aqm-c15-nivel').value = fora.n; }
		if (fora.rg) { el('aqm-c15-regime').value = fora.rg; }
		if (fora.t) { el('aqm-c15-tipo').value = fora.t; }
		if (fora.co2 === '1') { el('aqm-c15-co2').checked = true; }
	}

	/* ---------------------------------------------------------- ligações */

	el('aqm-c15-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
	});

	el('aqm-c15-limpar').addEventListener('click', function () {
		el('aqm-c15-form').reset();
		el('aqm-c15-saida').classList.add('aqm-c15-oculto');
		el('aqm-c15-erros').innerHTML = '';
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c15-copiar').addEventListener('click', function () {
		var campo = el('aqm-c15-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c15-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c15-tenho-calcular').addEventListener('click', inverso);

	el('aqm-c15-consumo-calcular').addEventListener('click', function () {
		var r = calcular(campos());
		if (r.erros && r.erros.length) {
			el('aqm-c15-consumo-saida').textContent = 'Preencha o volume do aquário lá em cima: o consumo depende do fotoperíodo, e o fotoperíodo sai do cálculo principal.';
			return;
		}
		pintarConsumo(r);
	});

	/* Query string manda; senão, o aquário que a C1 guardou neste navegador. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		pintar(calcular(campos()));
	} else {
		var antes = recuperar();
		var volume = antes && antes.volumes ? antes.volumes.real_L : null;
		if (volume) {
			el('aqm-c15-volume').value = String(volume).replace('.', ',');
			var medidas = antes.medidas || {};
			var agua = antes.agua || {};
			if (medidas.comprimento_cm) { el('aqm-c15-comprimento').value = String(medidas.comprimento_cm).replace('.', ','); }
			if (agua.altura_lamina_cm) { el('aqm-c15-lamina').value = String(Math.round(agua.altura_lamina_cm * 10) / 10).replace('.', ','); }
			if ((antes.perfil || {}).tipo_aquario === 'plantado') { el('aqm-c15-nivel').value = 'media'; }
			var retomado = el('aqm-c15-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que a calculadora de litragem guardou neste navegador'
				+ (medidas.comprimento_cm ? ', com ' + fmt(medidas.comprimento_cm, 0) + ' cm de comprimento' : '') + '.';
			retomado.classList.remove('aqm-c15-oculto');
			pintar(calcular(campos()));
		} else {
			el('aqm-c15-semvolume').classList.remove('aqm-c15-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_url' ) ) {
function aquametria_c15_url( $slug ) {
	return function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( $slug )
		: home_url( '/' . $slug . '/' );
}
}

if ( ! function_exists( 'aquametria_c15_form_html' ) ) {
function aquametria_c15_form_html() {
	$c1 = aquametria_c15_url( 'calculadora-de-litragem' );

	$h  = '<form id="aqm-c15-form" class="aqm-c15-painel" novalidate>';
	$h .= '<h3>O seu aquário e as suas plantas</h3>';
	$h .= '<p class="aqm-c15-sub">Se você já usou a calculadora de litragem neste navegador, o volume, o comprimento e a lâmina vêm preenchidos daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c15-grade">';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c15-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c15-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-comprimento">Comprimento do aquário (cm)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c15-comprimento" name="comprimento" placeholder="60">';
	$h .= '<span class="aqm-c15-dica">Necessário para a lista de luminárias: é ele que diz se a peça cobre o vidro inteiro.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-lamina">Altura da lâmina d\'água (cm)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c15-lamina" name="lamina" placeholder="ex.: 40">';
	$h .= '<span class="aqm-c15-dica">Da superfície até o substrato. Acima de ' . esc_html( AQUAMETRIA_C15_LAMINA_FUNDA_CM ) . ' cm, lúmen por litro começa a mentir — e a tela avisa.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-nivel">Exigência das plantas</label>';
	$h .= '<select id="aqm-c15-nivel" name="nivel">';
	$h .= '<option value="baixa">baixa (anúbias, musgos, cripitas)</option>';
	$h .= '<option value="media" selected>média (hastes, vallisnerias, echinodorus)</option>';
	$h .= '<option value="alta">alta (carpete, plantas vermelhas)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c15-dica">Aquário só de peixes, sem planta viva? A luz vira decoração: mire o nível baixo e olhe o fotoperíodo.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-regime">Momento do aquário</label>';
	$h .= '<select id="aqm-c15-regime" name="regime">';
	$h .= '<option value="normal" selected>rodando normalmente</option>';
	$h .= '<option value="ciclagem">em ciclagem</option>';
	$h .= '<option value="alga">com alga, quero reduzir</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c15-dica">Muda o fotoperíodo, não a quantidade de luz.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-campo">';
	$h .= '<label for="aqm-c15-tipo">Tipo de luminária</label>';
	$h .= '<select id="aqm-c15-tipo" name="tipo">';
	$h .= '<option value="qualquer">tanto faz</option>';
	$h .= '<option value="led-barra">LED em barra</option>';
	$h .= '<option value="led-calha">LED em calha</option>';
	$h .= '<option value="led-tampa">LED de tampa</option>';
	$h .= '<option value="led-pendente">LED pendente</option>';
	$h .= '<option value="refletor">refletor</option>';
	$h .= '<option value="fluorescente">fluorescente</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c15-dica">Filtra a lista de produtos, não o cálculo.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c15-caixa"><input type="checkbox" id="aqm-c15-co2"> <span>Injeto CO2 no aquário</span></label>';

	$h .= '<div class="aqm-c15-botoes">';
	$h .= '<button type="submit">Calcular a iluminação</button>';
	$h .= '<button type="button" class="aqm-c15-secundario" id="aqm-c15-limpar">Limpar</button>';
	$h .= '<span class="aqm-c15-dica aqm-c15-oculto" id="aqm-c15-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c15-avisos" id="aqm-c15-erros"></ul>';
	$h .= '<p class="aqm-c15-criterio aqm-c15-oculto" id="aqm-c15-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre e o substrato tiram uma parte. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_resposta_html' ) ) {
function aquametria_c15_resposta_html() {
	$artigo = aquametria_c15_url( AQUAMETRIA_C15_ARTIGO );

	$h  = '<div class="aqm-c15-resultado aqm-c15-oculto" id="aqm-c15-saida" aria-live="polite">';

	$h .= '<div class="aqm-c15-faixa">';
	$h .= '<span class="aqm-c15-rotulo">Lúmens que o seu aquário pede</span>';
	$h .= '<span class="aqm-c15-valor" id="aqm-c15-faixa-valor">—</span>';
	$h .= '<p class="aqm-c15-criterio" id="aqm-c15-faixa-criterio"></p>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-painel">';
	$h .= '<h3>As três leituras brasileiras, lado a lado</h3>';
	$h .= '<p class="aqm-c15-sub">A linha destacada é o nível que você escolheu. Os números de lm/L são das fontes; os lúmens são o seu volume multiplicado por eles.</p>';
	$h .= '<div class="aqm-c15-rolagem"><table class="aqm-c15-leituras">';
	$h .= '<thead><tr><th>Nível</th><th>Quem publicou</th><th class="aqm-c15-num">lm/L</th><th class="aqm-c15-num">No seu aquário</th></tr></thead>';
	$h .= '<tbody id="aqm-c15-leituras-corpo"></tbody>';
	$h .= '</table></div>';
	$h .= '<p class="aqm-c15-criterio" id="aqm-c15-leituras-nota" style="margin-top:.7rem"></p>';
	$h .= '<p class="aqm-c15-criterio" style="margin-top:.5rem">Por que elas discordam, e o que fazer com isso, está no artigo ';
	$h .= '<a href="' . esc_url( $artigo ) . '">quantos lúmens por litro o aquário plantado precisa</a>.</p>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c15-cartoes" id="aqm-c15-cartoes"></ul>';

	$h .= '<div class="aqm-c15-painel">';
	$h .= '<h3>Os quatro regimes de fotoperíodo</h3>';
	$h .= '<p class="aqm-c15-sub">O mesmo aquário passa por mais de um deles ao longo da vida. Todos vêm do levantamento de fontes brasileiras, e nenhum tem origem publicada pelo autor.</p>';
	$h .= '<ul class="aqm-c15-barrados" id="aqm-c15-fotoperiodos"></ul>';
	$h .= '<p class="aqm-c15-criterio" style="margin-top:.6rem">Fotoperíodo maior não compensa luminária fraca: a planta responde à intensidade que recebe, e o excesso de horas alimenta alga antes de alimentar planta. ';
	$h .= 'Se falta luz, o que falta é lúmen, não hora.</p>';
	$h .= '</div>';

	$h .= '<div class="aqm-c15-nota aqm-c15-nota-alerta aqm-c15-oculto" id="aqm-c15-co2-bloco">';
	$h .= '<strong>CO2: os dois limites publicados se sobrepõem, e a tela não vai esconder isso.</strong><br>';
	$h .= '<span id="aqm-c15-co2-texto"></span>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c15-avisos" id="aqm-c15-avisos"></ul>';

	$h .= aquametria_c15_produtos_html();

	$h .= '<div class="aqm-c15-citar">';
	$h .= '<p id="aqm-c15-citacao"></p>';
	$h .= '<div class="aqm-c15-campo"><label for="aqm-c15-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c15-link" readonly></div>';
	$h .= '<div class="aqm-c15-botoes"><button type="button" class="aqm-c15-secundario" id="aqm-c15-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c15-dica" id="aqm-c15-copiado"></span></div>';
	$h .= '<p class="aqm-c15-dica" id="aqm-c15-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_produtos_html' ) ) {
function aquametria_c15_produtos_html() {
	$divulgacao = aquametria_c15_url( AQUAMETRIA_C15_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c15-produtos aqm-c15-painel aqm-c15-oculto" id="aqm-c15-produtos">';
	$h .= '<h3>Luminárias que entregam essa faixa no seu comprimento</h3>';
	$h .= '<p class="aqm-c15-sub" id="aqm-c15-produtos-sub"></p>';
	$h .= '<ul class="aqm-c15-lista" id="aqm-c15-produtos-lista"></ul>';
	$h .= '<p class="aqm-c15-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista nem em que ordem — a ordem é pelo fluxo mais próximo do meio da faixa que o seu aquário pede, e modelo sem link aparece do mesmo jeito. ';
	$h .= 'A luminária mais cara do nosso banco, aliás, tem link e não é sugerida, porque ninguém declara a voltagem dela. ';
	$h .= 'A ficha técnica de cada peça vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'Também não publicamos preço nesta página: preço muda toda semana e um número velho na tela seria pior que nenhum. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c15-nota aqm-c15-oculto" id="aqm-c15-produtos-nada"></p>';

	$h .= '<div class="aqm-c15-painel aqm-c15-oculto" id="aqm-c15-barrados-bloco">';
	$h .= '<h3>O que está no nosso banco e não pode ser sugerido</h3>';
	$h .= '<p class="aqm-c15-sub">Esta lista é o retrato do problema desta categoria no Brasil: o varejo vende luminária por centímetro de peça e omite a grandeza que dimensiona. ';
	$h .= 'Enquanto o número não existir com fonte, o produto fica aqui — como ficha, nunca como recomendação.</p>';
	$h .= '<ul class="aqm-c15-barrados" id="aqm-c15-barrados"></ul>';
	$h .= '</div>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_consumo_html' ) ) {
function aquametria_c15_consumo_html() {
	$h  = '<div class="aqm-c15-painel">';
	$h .= '<h3>Quanto custa manter essa luz acesa</h3>';
	$h .= '<p class="aqm-c15-sub">A parte física — watts vezes horas — sai daqui. A parte em reais depende da sua tarifa, e é você quem informa: não publicamos tarifa de energia, porque ela muda por distribuidora, por bandeira e por faixa de consumo.</p>';
	$h .= '<div class="aqm-c15-grade">';
	$h .= '<div class="aqm-c15-campo"><label for="aqm-c15-watts">Potência da luminária (W)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c15-watts" placeholder="24">';
	$h .= '<span class="aqm-c15-dica">Em branco, usamos a potência da primeira luminária sugerida acima.</span></div>';
	$h .= '<div class="aqm-c15-campo"><label for="aqm-c15-tarifa">Sua tarifa (R$/kWh)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c15-tarifa" placeholder="ex.: 0,95">';
	$h .= '<span class="aqm-c15-dica">Está na sua conta de luz, já com impostos.</span></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c15-botoes"><button type="button" id="aqm-c15-consumo-calcular">Calcular o consumo</button></div>';
	$h .= '<p class="aqm-c15-criterio" id="aqm-c15-consumo-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_inverso_html' ) ) {
function aquametria_c15_inverso_html() {
	$h  = '<div class="aqm-c15-painel">';
	$h .= '<h3>Caminho inverso: a luminária que eu já tenho serve?</h3>';
	$h .= '<p class="aqm-c15-sub">Informe o fluxo em lúmens e devolvemos o volume que ela cobre em cada nível — e, se o volume estiver preenchido acima, quantos lm/L ela entrega no seu aquário.</p>';
	$h .= '<div class="aqm-c15-grade">';
	$h .= '<div class="aqm-c15-campo"><label for="aqm-c15-tenho">Fluxo da luminária (lm)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c15-tenho" placeholder="2400"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c15-botoes"><button type="button" id="aqm-c15-tenho-calcular">Ver o que ela cobre</button></div>';
	$h .= '<p class="aqm-c15-criterio" id="aqm-c15-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_fontes_html' ) ) {
function aquametria_c15_fontes_html() {
	$h  = '<div class="aqm-c15-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c15-sub">Verificado em ' . esc_html( AQUAMETRIA_C15_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C15_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c15-rolagem"><table class="aqm-c15-fontes">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>iluminacao-lumen-por-litro</td><td>baixa 10 a 20 · média 20 a 40 · alta 40 a 60+ lm/L</td>';
	$h .= '<td>Três fontes brasileiras do levantamento de 04/09/2026 <span class="aqm-c15-selo">divergente entre fontes BR</span>: peixeseaquarismo, aquarioturbinado e aquariosplantados. ';
	$h .= 'Elas chamam a mesma faixa pelo mesmo nome com números que diferem por até duas vezes — "baixa" é 20 lm/L para uma, 10 a 20 para outra e 15 para a terceira. ';
	$h .= 'Publicamos as três com atribuição e a faixa que as três, juntas, sustentam. Nunca a média.</td></tr>';

	$h .= '<tr><td>fotoperiodo</td><td>4 a 10 h/dia, conforme o regime</td>';
	$h .= '<td>Quatro regimes do mesmo levantamento <span class="aqm-c15-selo">divergente entre fontes BR</span>: low tech 6 a 8 h, high tech 8 a 10 h, combate a alga 5 a 6 h, ciclagem 4 a 6 h. ';
	$h .= 'Nenhuma fonte publica a medição por trás dos limites.</td></tr>';

	$h .= '<tr><td>temperatura-de-cor</td><td>' . esc_html( AQUAMETRIA_C15_K_MIN ) . ' a ' . esc_html( AQUAMETRIA_C15_K_MAX ) . ' K</td>';
	$h .= '<td>Faixa repetida pelas fontes brasileiras para aquário plantado <span class="aqm-c15-selo">divergente entre fontes BR</span>. ';
	$h .= 'Kelvin descreve a aparência da luz, não a quantidade: é critério de gosto e de espectro, e não entra no dimensionamento acima.</td></tr>';

	$h .= '<tr><td>co2-concentracao</td><td>15 a 35 mg/L úteis; risco acima de 30 a 35 mg/L</td>';
	$h .= '<td>CO2Art, pelo levantamento <span class="aqm-c15-selo">divergente entre fontes BR</span>. Os dois extremos se sobrepõem, e a tela mostra a sobreposição em vez de escolher um número. ';
	$h .= 'Quem resolve é o drop checker, que é medição.</td></tr>';

	$h .= '<tr><td>cobertura-luminaria-declarada</td><td>só entra na lista quem declara o comprimento de aquário coberto</td>';
	$h .= '<td>Convenção editorial da Aquametria, de 08/09/2026 <span class="aqm-c15-selo">convenção editorial</span>, derivada dos registros do nosso banco: ';
	$h .= 'nos cinco que declaram os dois números, o teto de cobertura vai de 1,15 a 1,59 vez o comprimento da peça — uma peça de 41 cm que cobre 65 cm, outra de 60 cm que cobre 66. ';
	$h .= 'Não há razão constante a extrair, e inventar uma seria inventar número. Por isso não convertemos comprimento de peça em cobertura.</td></tr>';

	$h .= '<tr><td>ppfd-por-litragem</td><td>sem valor <span class="aqm-c15-selo">pendente</span></td>';
	$h .= '<td>PPFD (ou PAR) é a medida correta: conta os fótons que a planta usa, na profundidade em que ela está. Lúmen conta o que o olho humano enxerga, na superfície. ';
	$h .= 'Nenhuma fonte brasileira publica PPFD por litragem, e em 08/09/2026 achamos o motivo a montante: no fórum de suporte da própria Chihiros — marca cujo argumento de venda é PAR — ';
	$h .= 'a resposta oficial sobre a tabela de PAR da linha WRGB II Pro é que não existe teste oficial e que o usuário procure medições no YouTube. ';
	$h .= 'Enquanto não houver PPFD declarado com a distância em centímetros, esta calculadora não publica nenhum.</td></tr>';

	$h .= '<tr><td>fichas das luminárias</td><td>ver cada cartão</td>';
	$h .= '<td>Banco de produtos da Aquametria (dados/produtos-iluminacao.json), com fonte, endereço e data por campo. ';
	$h .= 'Hoje o banco tem seis registros e só três podem ser sugeridos: três são barrados por não declararem voltagem ou lúmens.</td></tr>';

	$h .= '</table></div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c15_adiante_html' ) ) {
function aquametria_c15_adiante_html() {
	$hub    = aquametria_c15_url( 'calculadoras' );
	$meto   = aquametria_c15_url( 'metodologia' );
	$c1     = aquametria_c15_url( 'calculadora-de-litragem' );
	$c3     = aquametria_c15_url( 'calculadora-de-vazao-do-filtro' );
	$c5     = aquametria_c15_url( 'calculadora-de-potencia-do-aquecedor' );
	$c12    = aquametria_c15_url( 'calculadora-de-midia-filtrante' );
	$divul  = aquametria_c15_url( AQUAMETRIA_C15_PAGINA_AFILIADOS );
	$artigo = aquametria_c15_url( AQUAMETRIA_C15_ARTIGO );

	$h  = '<div class="aqm-c15-painel aqm-c15-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $artigo ) . '"><strong>Quantos lúmens por litro o aquário plantado precisa</strong></a> — o artigo pareado com esta calculadora: de onde saiu a regra de lm/L, por que as três fontes brasileiras discordam por duas vezes sobre o mesmo rótulo e onde a régua quebra.</li>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vêm o volume real, o comprimento e a lâmina que esta página usa. Se os campos vieram preenchidos, vieram de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c3 ) . '"><strong>Vazão do filtro (C3)</strong></a> — o mesmo volume, do outro lado do aquário. Aquário plantado pede corrente mais lenta, e a faixa de lá muda por causa disso.</li>';
	$h .= '<li><a href="' . esc_url( $c5 ) . '"><strong>Potência do aquecedor (C5)</strong></a> — o aparelho que mais pesa na conta de luz, e o único que pergunta quanto frio faz no seu cômodo. Luminária potente também aquece a água: em aquário pequeno e tampado, isso conta.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — luz forte com CO2 acelera o crescimento das plantas e a carga do filtro junto. É a mesma decisão vista pela filtragem.</li>';
	$h .= '<li><strong>Consumo elétrico (C7)</strong> — vai juntar a luminária, o filtro e o aquecedor na mesma conta mensal, com ciclo de trabalho. Ainda em construção; o painel de consumo desta página é a parte dela que já dá para publicar.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com três fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c15-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 6. Entrega do estilo e do comportamento — FORA do retorno do shortcode
 *
 * REGRA PERMANENTE DO PROJETO, escrita com sangue em 08/09/2026: JS e CSS de
 * shortcode NUNCA vao dentro do que o shortcode retorna. O retorno do shortcode
 * ainda atravessa os filtros de texto do conteúdo, que trocam cada "&" por
 * a entidade numérica dele — e um único "&&" escapado assim mata o script INTEIRO com
 * SyntaxError: o formulário nunca calcula, a resposta nunca aparece e o bloco de
 * produto com os links de afiliado nunca sai da classe "-oculto". Foi o que
 * derrubou as cinco primeiras calculadoras da ilha.
 *
 * O caminho seguro é imprimir fora dos filtros de conteúdo:
 *   - o estilo no wp_head, para a pagina nao piscar sem estilo;
 *   - o comportamento no wp_footer, depois do HTML que ele controla.
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * 5c. Seis aquários resolvidos no servidor, e o JSON-LD
 *
 * Escrito em 09/09/2026, e o motivo é uma medição, não um gosto: todo o cálculo
 * desta página é JavaScript no navegador, de propósito (o site está atrás de
 * cache de página). A consequência é que um modelo de linguagem — ou o leitor
 * que não preenche formulário — recebia um formulário VAZIO e ia embora sem um
 * lúmen sequer. É o defeito que a seção 5 do ARQUIPELAGO.md chama pelo nome, e
 * que a C5 já tinha consertado; aqui a C15 recebe o mesmo tratamento.
 *
 * As funções abaixo resolvem seis aquários em PHP, com as MESMAS regras do
 * script, e o resultado sai no HTML servido. Onde o script arredonda, elas
 * arredondam igual — tabela servida que contradiz a calculadora logo acima dela
 * é pior que tabela nenhuma.
 * ------------------------------------------------------------------------- */

/* Espelho em PHP do lm() do script: lúmen é número grosso, então arredonda para
   a dezena, ou para a centena acima de 10 000. */
if ( ! function_exists( 'aquametria_c15_lm' ) ) {
function aquametria_c15_lm( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	$passo = ( $n >= 10000 ) ? 100 : 10;
	return number_format_i18n( round( $n / $passo ) * $passo, 0 );
}
}

/* Espelho em PHP do litros() do script. */
if ( ! function_exists( 'aquametria_c15_litros' ) ) {
function aquametria_c15_litros( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return ( $n >= 100 ) ? number_format_i18n( round( $n ), 0 ) : number_format_i18n( round( $n * 10 ) / 10, 1 );
}
}

/* Espelho em PHP do NIVEIS do script. Se um número divergir entre os dois, a
   página passa a afirmar duas coisas — por isso o teste de navegador compara a
   tabela servida com o que a calculadora devolve para a mesma entrada. */
if ( ! function_exists( 'aquametria_c15_niveis' ) ) {
function aquametria_c15_niveis() {
	return array(
		'baixa' => array( 'rotulo' => 'baixa exigência', 'consolidado' => array( 10, 20 ), 'aberto' => false ),
		'media' => array( 'rotulo' => 'exigência média', 'consolidado' => array( 20, 40 ), 'aberto' => false ),
		'alta'  => array( 'rotulo' => 'alta exigência',  'consolidado' => array( 40, 60 ), 'aberto' => true ),
	);
}
}

/* Os seis aquários. As medidas são as do comércio brasileiro, e o volume de
   água NÃO é o produto das três: desconta-se a borda livre de 3 cm, que é a
   convenção editorial declarada da Aquametria e a mesma que a C1 usa. Escrever
   "60 × 30 × 35 = 63 L" seria publicar um aquário cheio até a borda, que não
   existe. */
if ( ! function_exists( 'aquametria_c15_casos_exemplo' ) ) {
function aquametria_c15_casos_exemplo() {
	$casos = array(
		array( 'c' => 30,  'l' => 20, 'a' => 25 ),
		array( 'c' => 45,  'l' => 25, 'a' => 30 ),
		array( 'c' => 60,  'l' => 30, 'a' => 35 ),
		array( 'c' => 80,  'l' => 35, 'a' => 40 ),
		array( 'c' => 90,  'l' => 45, 'a' => 45 ),
		array( 'c' => 120, 'l' => 50, 'a' => 50 ),
	);
	foreach ( $casos as $i => $caso ) {
		$lamina                 = $caso['a'] - AQUAMETRIA_C15_BORDA_LIVRE_CM;
		$casos[ $i ]['lamina']  = $lamina;
		$casos[ $i ]['volume']  = ( $caso['c'] * $caso['l'] * $lamina ) / 1000;
		$casos[ $i ]['funda']   = ( $lamina > AQUAMETRIA_C15_LAMINA_FUNDA_CM );
	}
	return $casos;
}
}

/* Resolve um aquário num nível de exigência, com as regras do script. */
if ( ! function_exists( 'aquametria_c15_exemplo' ) ) {
function aquametria_c15_exemplo( $volume, $comprimento, $nivel_id ) {
	$niveis = aquametria_c15_niveis();
	$nivel  = isset( $niveis[ $nivel_id ] ) ? $niveis[ $nivel_id ] : $niveis['media'];

	$r = array(
		'nivel_id' => $nivel_id,
		'rotulo'   => $nivel['rotulo'],
		'aberto'   => $nivel['aberto'],
		'min'      => $volume * $nivel['consolidado'][0],
		'max'      => $volume * $nivel['consolidado'][1],
		'lm_l'     => $nivel['consolidado'],
	);

	/* Mesma peneira do escolher() do script: primeiro a cobertura declarada pelo
	   fabricante, depois o fluxo dentro da faixa. A ordem importa e é a da seção
	   7 do ARQUIPELAGO.md — elegibilidade técnica COMPLETA antes de qualquer
	   coisa. Peça que não cobre o vidro não entra na lista nem em último lugar. */
	$dentro = array();
	foreach ( aquametria_c15_catalogo() as $p ) {
		$cobre = ( null === $p['aquario_min_cm'] || $comprimento >= $p['aquario_min_cm'] )
			&& ( null === $p['aquario_max_cm'] || $comprimento <= $p['aquario_max_cm'] );
		if ( ! $cobre ) {
			continue;
		}
		if ( null === $p['fluxo_lm'] ) {
			continue;
		}
		if ( $p['fluxo_lm'] >= $r['min'] && ( $r['aberto'] || $p['fluxo_lm'] <= $r['max'] ) ) {
			$dentro[] = $p;
		}
	}

	/* Desempate: o mais perto do meio da faixa, exatamente como o script. */
	$meio = ( $r['min'] + $r['max'] ) / 2;
	usort( $dentro, function ( $a, $b ) use ( $meio ) {
		$da = abs( $a['fluxo_lm'] - $meio );
		$db = abs( $b['fluxo_lm'] - $meio );
		if ( $da === $db ) {
			return 0;
		}
		return ( $da < $db ) ? -1 : 1;
	} );

	$r['produtos'] = array_slice( $dentro, 0, 5 );
	$r['produto']  = $dentro ? $dentro[0] : null;
	return $r;
}
}

/* O nome do produto como a tela escreve — o banco é gravado sem acento de
   propósito, e a frase é montada aqui. */
if ( ! function_exists( 'aquametria_c15_produto_nome' ) ) {
function aquametria_c15_produto_nome( $p ) {
	return trim( ( $p['marca'] ? $p['marca'] . ' ' : '' ) . $p['modelo'] );
}
}

/* A célula do produto. Sem item que atenda, ela DIZ por quê: a seção 7 do
   contrato trata bloco vazio como portão, não como defeito — mas silêncio
   parece defeito, e por isso a frase existe. */
if ( ! function_exists( 'aquametria_c15_produto_celula_html' ) ) {
function aquametria_c15_produto_celula_html( $e ) {
	if ( null === $e['produto'] ) {
		return '<td><span class="aqm-c15-semloja">nenhuma luminária do banco cobre esse comprimento dentro de '
			. esc_html( aquametria_c15_lm( $e['min'] ) ) . ' a ' . esc_html( aquametria_c15_lm( $e['max'] ) )
			. ' lm — é faixa vazia do catálogo brasileiro, não erro da conta</span></td>';
	}
	$p = $e['produto'];
	$h = '<td><span class="aqm-c15-num">' . esc_html( aquametria_c15_produto_nome( $p ) ) . '</span>';
	$h .= '<span class="aqm-c15-un">' . esc_html( aquametria_c15_lm( $p['fluxo_lm'] ) ) . ' lm · cobre ';
	$h .= esc_html( ( null === $p['aquario_min_cm'] ? 'até ' : number_format_i18n( $p['aquario_min_cm'], 0 ) . ' a ' )
		. ( null === $p['aquario_max_cm'] ? 'qualquer' : number_format_i18n( $p['aquario_max_cm'], 0 ) ) . ' cm' );
	$h .= $p['link'] ? '' : ' · sem link de loja';
	$h .= '</span></td>';
	return $h;
}
}

/* ---- A resposta antes da explicação (seção 5, item 2 do ARQUIPELAGO.md) ---
   Frase autossuficiente: precisa sobreviver a ser citada fora de contexto, por
   um modelo de linguagem que leu só este parágrafo. Por isso repete o número, a
   unidade, a condição e a data em vez de dizer "veja acima". */
if ( ! function_exists( 'aquametria_c15_resposta_direta_html' ) ) {
function aquametria_c15_resposta_direta_html() {
	$e60 = aquametria_c15_exemplo( 57.6, 60, 'media' );
	$b60 = aquametria_c15_exemplo( 57.6, 60, 'baixa' );
	$a60 = aquametria_c15_exemplo( 57.6, 60, 'alta' );

	$h  = '<div class="aqm-c15-citar">';
	$h .= '<p><strong>A resposta curta.</strong> Um aquário plantado pede de <strong>20 a 40 lúmens por litro</strong> de água real para plantas de exigência média, ';
	$h .= 'de 10 a 20 lm/L para plantas de baixa exigência e de 40 a 60 lm/L para as de alta exigência, que só fazem sentido com CO2 injetado. ';
	$h .= 'Num aquário de 60 cm com ' . esc_html( aquametria_c15_litros( 57.6 ) ) . ' litros de água, isso dá ';
	$h .= '<strong>' . esc_html( aquametria_c15_lm( $e60['min'] ) ) . ' a ' . esc_html( aquametria_c15_lm( $e60['max'] ) ) . ' lm</strong> no nível médio, ';
	$h .= esc_html( aquametria_c15_lm( $b60['min'] ) ) . ' a ' . esc_html( aquametria_c15_lm( $b60['max'] ) ) . ' lm no baixo e ';
	$h .= 'a partir de ' . esc_html( aquametria_c15_lm( $a60['min'] ) ) . ' lm no alto.</p>';

	$h .= '<p><strong>De onde vem esse número, e por que ele é uma faixa e não um valor.</strong> ';
	$h .= 'Três fontes brasileiras publicam lúmens por litro com o mesmo rótulo e números diferentes: peixeseaquarismo, aquarioturbinado e aquariosplantados. ';
	$h .= 'A Aquametria publica a união do que as três afirmam, com o nome de cada uma ao lado, e <strong>não tira média</strong> — média apagaria justamente o desacordo que faz esta página valer. ';
	$h .= 'Levantamento verificado em ' . esc_html( AQUAMETRIA_C15_VERIFICADO_EM ) . '.</p>';

	$h .= '<p><strong>E o que essa conta não sabe.</strong> Lúmen por litro ignora a profundidade: acima de ' . esc_html( AQUAMETRIA_C15_LAMINA_FUNDA_CM ) . ' cm de lâmina d\'água ';
	$h .= 'o mesmo número de lúmens entrega muito menos luz no substrato, e a medida que resolveria isso — PPFD por profundidade — não está publicada aqui porque não temos fonte para ela. ';
	$h .= 'Dizer o que a conta não alcança é parte da resposta.</p>';
	$h .= '</div>';

	return $h;
}
}

/* ---- A tabela de exemplos servida (seção 5, item 1) ---------------------- */
if ( ! function_exists( 'aquametria_c15_exemplos_html' ) ) {
function aquametria_c15_exemplos_html() {
	$h  = '<div class="aqm-c15-painel">';
	$h .= '<h3>Seis aquários já resolvidos, nos três níveis de exigência</h3>';
	$h .= '<p class="aqm-c15-sub">É a mesma conta do formulário acima, aplicada a seis medidas comuns do comércio brasileiro. ';
	$h .= 'Estes números estão prontos no HTML desta página — não é preciso preencher nada, e quem lê sem executar JavaScript vê os mesmos valores que a calculadora devolve.</p>';

	/* Classe propria, e nao .aqm-c15-fontes: aquela e a tabela de divergencia das
	   fontes, e o teste de navegador a localiza pelo seletor. Duas tabelas com a
	   mesma classe quebram o localizador — foi o teste que pegou isto. */
	$h .= '<div class="aqm-c15-rolagem"><table class="aqm-c15-exemplos">';
	$h .= '<tr><th>Aquário</th><th>Água real</th><th>Baixa exigência</th><th>Exigência média</th><th>Alta exigência</th><th>Luminária do banco para o nível médio</th></tr>';

	foreach ( aquametria_c15_casos_exemplo() as $caso ) {
		$b = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'baixa' );
		$m = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'media' );
		$a = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'alta' );

		$h .= '<tr>';
		$h .= '<td><span class="aqm-c15-num">' . esc_html( number_format_i18n( $caso['c'], 0 ) ) . ' cm</span>';
		$h .= '<span class="aqm-c15-un">' . esc_html( number_format_i18n( $caso['c'], 0 ) . ' × ' . number_format_i18n( $caso['l'], 0 ) . ' × ' . number_format_i18n( $caso['a'], 0 ) ) . ' cm</span></td>';

		$h .= '<td><span class="aqm-c15-num">' . esc_html( aquametria_c15_litros( $caso['volume'] ) ) . ' L</span>';
		$h .= '<span class="aqm-c15-un">lâmina de ' . esc_html( number_format_i18n( $caso['lamina'], 0 ) ) . ' cm';
		$h .= $caso['funda'] ? ' — funda' : '';
		$h .= '</span></td>';

		$h .= '<td><span class="aqm-c15-num">' . esc_html( aquametria_c15_lm( $b['min'] ) ) . ' a ' . esc_html( aquametria_c15_lm( $b['max'] ) ) . ' lm</span>';
		$h .= '<span class="aqm-c15-un">10 a 20 lm/L</span></td>';

		$h .= '<td><span class="aqm-c15-num">' . esc_html( aquametria_c15_lm( $m['min'] ) ) . ' a ' . esc_html( aquametria_c15_lm( $m['max'] ) ) . ' lm</span>';
		$h .= '<span class="aqm-c15-un">20 a 40 lm/L</span></td>';

		$h .= '<td><span class="aqm-c15-num">a partir de ' . esc_html( aquametria_c15_lm( $a['min'] ) ) . ' lm</span>';
		$h .= '<span class="aqm-c15-un">40 lm/L, sem teto declarado</span></td>';

		$h .= aquametria_c15_produto_celula_html( $m );
		$h .= '</tr>';
	}

	$h .= '</table></div>';

	$h .= '<p class="aqm-c15-criterio" style="margin-top:.8rem">Como ler a tabela. ';
	$h .= 'A água real desconta 3 cm de borda livre da altura do vidro — é a convenção editorial declarada da Aquametria, a mesma da calculadora de litragem, e existe porque aquário cheio até a borda não existe. ';
	$h .= 'A coluna da alta exigência não tem teto porque a fonte aquarioturbinado publica "acima de 40 lm/L" sem dizer até onde, e inventar um teto para fechar a faixa seria inventar constante. ';
	$h .= 'A palavra "funda" na segunda coluna marca as lâminas acima de ' . esc_html( AQUAMETRIA_C15_LAMINA_FUNDA_CM ) . ' cm, em que lúmen por litro começa a mentir e o número da linha vale menos do que parece. ';
	$h .= 'Nenhum valor desta tabela foi digitado à mão: todos saem das mesmas regras que a calculadora usa, calculados no servidor a cada carregamento.</p>';

	$divulgacao = aquametria_c15_url( AQUAMETRIA_C15_PAGINA_AFILIADOS );

	/* Classe propria, e nao a mesma do aviso de publicidade la de cima: o teste de
	   navegador localiza aquele por .aqm-c15-aviso-afiliado, e duas ocorrencias
	   da mesma classe quebram o localizador. Foi o teste que pegou isto. */
	$h .= '<p class="aqm-c15-aviso-tabela"><strong>Sobre a última coluna.</strong> ';
	$h .= 'Ela mostra a luminária do banco técnico da Aquametria que <em>cobre o comprimento daquele aquário segundo o fabricante</em> e cujo fluxo cai mais perto do meio da faixa do nível médio. ';
	$h .= 'Os dois cortes nessa ordem, e a comissão não entra em nenhum deles: peça que não cobre o vidro não aparece nem em último lugar, e modelo sem link de loja aparece do mesmo jeito — a coluna diz quando é o caso. ';
	$h .= 'Onde a célula diz que nada atende, é faixa vazia do catálogo brasileiro medida por nós, não erro da conta. ';
	$h .= 'Alguns desses nomes levam a lojas por link de afiliado, marcado como patrocinado: se você comprar por ele, a Aquametria pode receber comissão, sem custo a mais para você. ';
	$h .= 'Não publicamos preço aqui, porque preço muda toda semana e número velho na tela é pior que nenhum. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';

	$h .= '</div>';
	return $h;
}
}

/* ---- JSON-LD (seção 5, item 3) ------------------------------------------
 * Sai no wp_head, e por isso NUNCA dentro do retorno do shortcode: o retorno
 * atravessa os filtros do the_content, que trocariam cada "&" pela entidade
 * numérica e quebrariam o JSON. Mesma regra do script, mesmo motivo.
 *
 * Cada resposta do FAQ existe, com o mesmo número, na tabela servida acima —
 * FAQPage que promete o que a página não mostra é lixo, e seria lixo detectável.
 * ---------------------------------------------------------------------- */
if ( ! function_exists( 'aquametria_c15_jsonld_dados' ) ) {
function aquametria_c15_jsonld_dados() {
	$url    = aquametria_c15_url( AQUAMETRIA_C15_SLUG );
	$artigo = aquametria_c15_url( AQUAMETRIA_C15_ARTIGO );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$app = array(
		'@type'                  => 'WebApplication',
		'@id'                    => $url . '#calculadora',
		'name'                   => 'Calculadora de iluminação de aquário plantado',
		'alternateName'          => 'Aquametria C15 — quantos lúmens por litro',
		'url'                    => $url,
		'inLanguage'             => 'pt-BR',
		'applicationCategory'    => 'UtilitiesApplication',
		'applicationSubCategory' => 'Calculadora de dimensionamento de aquário',
		'operatingSystem'        => 'Qualquer navegador com JavaScript',
		'browserRequirements'    => 'Requer JavaScript. O cálculo roda no navegador e nenhum dado é enviado a servidor.',
		'isAccessibleForFree'    => true,
		'offers'                 => array(
			'@type'         => 'Offer',
			'price'         => '0',
			'priceCurrency' => 'BRL',
		),
		'softwareVersion' => AQUAMETRIA_C15_VERSAO,
		'description'     => 'Converte o volume real de água e a exigência das plantas na faixa de lúmens que o aquário pede, '
			. 'e cruza essa faixa com o comprimento do vidro para dizer quais luminárias do banco técnico realmente cobrem a peça. '
			. 'Publica as três leituras brasileiras de lúmens por litro separadas, com o nome de cada fonte, em vez de tirar média delas.',
		'featureList' => array(
			'Faixa de lúmens a partir do volume real de água e do nível de exigência das plantas',
			'As três leituras brasileiras de lúmens por litro, cada uma com o nome da fonte',
			'Fotoperíodo por regime: low tech, high tech com CO2, combate a alga e ciclagem',
			'Aviso quando o nível alto é escolhido sem CO2 injetado',
			'Aviso quando a lâmina d\'água passa dos ' . AQUAMETRIA_C15_LAMINA_FUNDA_CM . ' cm em que lúmen por litro começa a mentir',
			'Barreira de cobertura declarada pelo fabricante antes de sugerir qualquer luminária',
			'Caminho inverso: a luminária que você já tem serve para qual aquário',
			'Tabela pré-calculada para seis aquários de 30 a 120 cm, nos três níveis de exigência',
			'Luminária do banco indicada para cada um desses seis aquários, já no HTML servido',
		),
		'publisher'  => $editora,
		'isBasedOn'  => 'Levantamento de fontes brasileiras da Aquametria e fichas de fabricante e de varejo especializado coletadas até ' . AQUAMETRIA_C15_VERIFICADO_EM,
		'mainEntityOfPage' => $artigo,
	);

	$perguntas = array();

	foreach ( aquametria_c15_casos_exemplo() as $caso ) {
		$b = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'baixa' );
		$m = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'media' );
		$a = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'alta' );

		$texto = 'Um aquário de ' . number_format_i18n( $caso['c'], 0 ) . ' cm com '
			. aquametria_c15_litros( $caso['volume'] ) . ' litros de água real pede de '
			. aquametria_c15_lm( $m['min'] ) . ' a ' . aquametria_c15_lm( $m['max'] ) . ' lúmens para plantas de exigência média (20 a 40 lm/L), '
			. 'de ' . aquametria_c15_lm( $b['min'] ) . ' a ' . aquametria_c15_lm( $b['max'] ) . ' lm para plantas de baixa exigência (10 a 20 lm/L) '
			. 'e a partir de ' . aquametria_c15_lm( $a['min'] ) . ' lm para as de alta exigência (40 lm/L, sem teto declarado pelas fontes). '
			. 'A faixa é a união do que três fontes brasileiras publicam sob o mesmo rótulo — peixeseaquarismo, aquarioturbinado e aquariosplantados — '
			. 'e a Aquametria não tira média delas de propósito: a média apagaria o desacordo, que é o que a página tem a dizer. '
			. 'Verificado em ' . AQUAMETRIA_C15_VERIFICADO_EM . '.';

		if ( $caso['funda'] ) {
			$texto .= ' Atenção neste tamanho: a lâmina d\'água tem ' . number_format_i18n( $caso['lamina'], 0 ) . ' cm, acima dos '
				. AQUAMETRIA_C15_LAMINA_FUNDA_CM . ' cm em que lúmen por litro começa a mentir — o mesmo número de lúmens entrega menos luz no substrato de um aquário fundo.';
		}

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Quantos lúmens de luminária para um aquário de ' . number_format_i18n( $caso['c'], 0 ) . ' cm?',
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $texto ),
		);
	}

	foreach ( aquametria_c15_casos_exemplo() as $caso ) {
		$m = aquametria_c15_exemplo( $caso['volume'], $caso['c'], 'media' );

		if ( null === $m['produto'] ) {
			/* Faixa vazia é resposta legítima, e é dita com essas palavras: um FAQ
			   que fica calado onde o banco não cobre parece defeito. */
			$texto = 'Hoje, nenhuma. O banco técnico da Aquametria não tem luminária que ao mesmo tempo declare cobrir '
				. number_format_i18n( $caso['c'], 0 ) . ' cm de aquário e entregue entre '
				. aquametria_c15_lm( $m['min'] ) . ' e ' . aquametria_c15_lm( $m['max'] ) . ' lúmens, que é o que esse aquário pede no nível médio. '
				. 'Isso é uma faixa vazia do catálogo brasileiro medida por nós, não um erro da conta — e está na nossa lista de compras do banco. '
				. 'Preferimos dizer isso a empurrar uma peça que não cobre o vidro.';
		} else {
			$p     = $m['produto'];
			$texto = 'Para um aquário de ' . number_format_i18n( $caso['c'], 0 ) . ' cm com ' . aquametria_c15_litros( $caso['volume'] )
				. ' litros de água real e plantas de exigência média, a faixa é de ' . aquametria_c15_lm( $m['min'] ) . ' a '
				. aquametria_c15_lm( $m['max'] ) . ' lúmens, e a luminária do banco técnico da Aquametria que cai mais perto do meio dela é a '
				. aquametria_c15_produto_nome( $p ) . ', com ' . aquametria_c15_lm( $p['fluxo_lm'] ) . ' lm declarados. '
				. 'Ela entra na lista por dois cortes nessa ordem: o fabricante declara que ela cobre '
				. ( null === $p['aquario_min_cm'] ? 'até ' : number_format_i18n( $p['aquario_min_cm'], 0 ) . ' a ' )
				. ( null === $p['aquario_max_cm'] ? 'qualquer comprimento' : number_format_i18n( $p['aquario_max_cm'], 0 ) . ' cm' )
				. ' de aquário, e só então o fluxo dela é comparado com a faixa. '
				. 'A comissão não entra no critério: '
				. ( $p['link'] ? 'este modelo tem link de loja, e teria aparecido na mesma posição sem ele.' : 'este modelo NÃO tem link de loja no nosso banco e aparece assim mesmo.' )
				. ' Antes de comprar, confira a voltagem e se a peça cabe no móvel: a ficha declara '
				. ( $p['peca_cm'] ? number_format_i18n( $p['peca_cm'], 0 ) . ' cm de peça' : 'o comprimento da peça sem confirmação' ) . '.';
		}

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Qual luminária comprar para um aquário plantado de ' . number_format_i18n( $caso['c'], 0 ) . ' cm?',
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $texto ),
		);
	}

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'Quantos lúmens por litro um aquário plantado precisa?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Depende da exigência das plantas, e a resposta honesta é uma faixa, não um número. '
				. 'De 10 a 20 lm/L para plantas de baixa exigência — anúbias, musgos, samambaias e cripitas, as que crescem devagar e vivem à sombra. '
				. 'De 20 a 40 lm/L para exigência média, que é a maioria das plantas de haste, vallisnerias e echinodorus. '
				. 'De 40 lm/L para cima na alta exigência: carpetes, plantas vermelhas e o aquário de competição. '
				. 'Essas faixas são a união de três fontes brasileiras que publicam o mesmo rótulo com números diferentes: peixeseaquarismo (20, 30 a 40 e 60 lm/L), '
				. 'aquarioturbinado (10 a 20, 20 a 40 e acima de 40) e aquariosplantados (15, 30 e 60). A Aquametria publica as três com o nome de cada uma '
				. 'em vez de tirar média, porque a média esconderia exatamente o desacordo que o leitor precisa ver.',
		),
	);

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'Luz forte causa alga no aquário plantado?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Luz forte sem carbono disponível causa, e a distinção importa. '
				. 'As fontes que publicam de 40 a 60 lm/L publicam esse número junto de CO2 injetado: com luz nesse patamar e sem CO2, a planta não consegue usar a luz que recebe e a alga usa. '
				. 'Por isso esta calculadora avisa quando o nível alto é escolhido sem CO2, e a saída é uma das duas — descer para o nível médio, ou pôr CO2 na conta. '
				. 'Reduzir o fotoperíodo ajuda como medida de combate (de 5 a 6 horas), mas não conserta um aquário iluminado acima do que ele consegue processar.',
		),
	);

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'Lúmen por litro serve para aquário fundo?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Cada vez menos, à medida que a lâmina d\'água aumenta, e acima de ' . AQUAMETRIA_C15_LAMINA_FUNDA_CM . ' cm a Aquametria avisa na tela. '
				. 'O motivo é que lúmen por litro não sabe a que profundidade a luz precisa chegar: o mesmo número de lúmens entrega muito menos luz no substrato de um aquário fundo do que num raso de mesmo volume. '
				. 'A medida que resolveria isso é PPFD por profundidade, e ela NÃO está publicada aqui porque não temos fonte de fabricante para ela — '
				. 'a maioria das luminárias vendidas no Brasil não declara PPFD, e inventar a conversão seria inventar constante. '
				. 'Nesse caso, trate a faixa como piso e trate a escolha como aproximada.',
		),
	);

	$faq = array(
		'@type'      => 'FAQPage',
		'@id'        => $url . '#faq',
		'inLanguage' => 'pt-BR',
		'url'        => $url,
		'mainEntity' => $perguntas,
	);

	return array(
		'@context' => 'https://schema.org',
		'@graph'   => array( $app, $faq ),
	);
}
}

if ( ! function_exists( 'aquametria_c15_imprimir_jsonld' ) ) {
function aquametria_c15_imprimir_jsonld() {
	$json = wp_json_encode( aquametria_c15_jsonld_dados(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-c15-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c15_estilo_impresso' ) ) {
function aquametria_c15_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c15_pagina_usa' ) ) {
function aquametria_c15_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_iluminacao' );
}
}

if ( ! function_exists( 'aquametria_c15_imprimir_estilo' ) ) {
function aquametria_c15_imprimir_estilo() {
	if ( aquametria_c15_estilo_impresso() ) {
		return;
	}
	aquametria_c15_estilo_impresso( true );
	echo '<style id="aquametria-c15-estilo">' . "\n" . aquametria_c15_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c15_cabeca' ) ) {
function aquametria_c15_cabeca() {
	if ( ! aquametria_c15_pagina_usa() ) {
		return;
	}
	aquametria_c15_imprimir_estilo();
	aquametria_c15_imprimir_jsonld();
}
}
add_action( 'wp_head', 'aquametria_c15_cabeca', 20 );

if ( ! function_exists( 'aquametria_c15_rodape' ) ) {
function aquametria_c15_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c15_imprimir_estilo();

	$js  = 'var AQM_C15_DATA = ' . wp_json_encode( AQUAMETRIA_C15_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C15_CATALOGO = ' . wp_json_encode( array_values( aquametria_c15_catalogo() ) ) . ";\n";
	$js .= 'var AQM_C15_BARRADOS = ' . wp_json_encode( array_values( aquametria_c15_barrados() ) ) . ";\n";
	$js .= aquametria_c15_js();
	echo '<script id="aquametria-c15-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 7. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c15_shortcode' ) ) {
function aquametria_c15_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c15_rodape', 20 );

	$h  = '<div class="aqm-c15">';
	$h .= aquametria_c15_resposta_direta_html();
	$h .= aquametria_c15_form_html();
	$h .= aquametria_c15_resposta_html();
	$h .= aquametria_c15_exemplos_html();
	$h .= aquametria_c15_consumo_html();
	$h .= aquametria_c15_inverso_html();
	$h .= aquametria_c15_fontes_html();
	$h .= aquametria_c15_adiante_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_iluminacao', 'aquametria_c15_shortcode' );

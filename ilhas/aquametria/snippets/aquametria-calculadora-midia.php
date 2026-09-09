/**
 * Aquametria Calculadora de Mídia Filtrante — C12
 * Versão: 1.2.0 (09/09/2026) — VISIBILIDADE EM IA (seção 5 do ARQUIPELAGO.md), as três peças de
 *   uma vez: resposta antes da explicação, tabela de exemplos pré-renderizada de 30 a 300 L e
 *   JSON-LD com WebApplication e FAQPage no wp_head. Nenhuma fórmula mudou: tudo que a tabela
 *   servida mostra sai de ESPELHOS em PHP das funções do próprio script (mL, litros, pct,
 *   ancorasBio, ancorasFiltro), porque tabela servida que contradiz a calculadora logo acima
 *   dela é pior que tabela nenhuma. A constante de versão também foi acertada: ela tinha ficado
 *   em 1.0.1 quando a 1.1.0 saiu, e é ela que a página imprime na tela.
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.1 (08/09/2026) — o painel de ligações passou a linkar a C15, publicada nesta data.
 * A 1.0.0 estreou a calculadora
 *
 * Quarta calculadora do lote e a que o levantamento do Bloco 1 apontou como o
 * VÁCUO DE CONTEÚDO Nº 1: nenhuma fonte brasileira publica quanta mídia
 * biológica um aquário precisa. Fala-se em "encher o cesto", em "quanto mais
 * melhor", em ordem das camadas — nunca em mililitros por litro de água.
 *
 * Os fabricantes publicam. Só que discordam por dez vezes, e ninguém no Brasil
 * põe as declarações lado a lado. Esta página põe:
 *
 *   Seachem Matrix       1,25 mL/L   (leitura "250 mL para 200 L")
 *   Seachem Matrix       2,64 mL/L   (leitura "1 L para 100 galões", mesma copy)
 *   JBL MicroMec         5,00 mL/L   (650 g = 1 L para 200 L)
 *   Ocean Tech Bio Glass 12,50 mL/L  (1 L para cada 80 L — marca brasileira)
 *
 * E, do outro lado do balcão, quem vende FILTRO declara quanto de mídia cabe
 * nele — mídia total, todas as camadas — o que dá a segunda família de âncoras,
 * calculada aqui a partir do volume útil de mídia dividido pelo volume de
 * aquário que o próprio fabricante declara atender.
 *
 * Registra o shortcode [aquametria_calculadora_midia] e se anuncia no hub pelo
 * filtro 'aquametria_calculadoras' da casca.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem, então HTML que dependesse da query string seria
 * servido errado para o visitante seguinte. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não escolhe uma das âncoras. Publicar 1,25 mL/L como "o" número seria
 *   fingir que a Ocean Tech não existe, e vice-versa. A resposta é a faixa
 *   inteira, com o nome de quem sustenta cada extremo.
 * - Não publica a PROPORÇÃO entre as camadas (quanto do cesto é mecânica,
 *   quanto é biológica, quanto é química). Nenhuma fonte do corpus declara
 *   isso, e repartir o cesto em porcentagens inventadas seria exatamente o
 *   tipo de número que este site existe para não publicar. Publicamos a ORDEM,
 *   que tem fonte, e o teto físico, que é do fabricante do filtro.
 * - Não converte a regra brasileira de carvão ativado (1 a 2 g por litro) na
 *   dosagem que o fabricante publica (0,625 mL por litro). Falta a densidade
 *   aparente do carvão com fonte; sem ela, transformar grama em mililitro é
 *   inventar constante. As duas saem em suas próprias unidades, lado a lado.
 * - Não estima quantos meses a mídia biológica "dura". A colônia não vence:
 *   o que envelhece é a porosidade entupida, e nenhuma fonte do corpus mede
 *   isso. Publicamos a substituição PARCIAL de 6 a 12 meses, que tem fonte.
 *
 * Bloco de produto: as mídias vêm do catálogo embutido mais abaixo, gerado por
 * ferramentas/gerar-catalogo-midias.py a partir de dados/produtos-midia.json e
 * dados/produtos-filtro.json. Mexeu no banco, rode o gerador. A ordem é pela
 * dosagem declarada, da mais econômica para a mais generosa — critério técnico
 * declarado na tela, e não comissão (regra V16). Preço não entra: snippet é
 * estático e preço envelhece na tela.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C12_VERSAO' ) ) {
	define( 'AQUAMETRIA_C12_VERSAO', '1.2.0' );
	define( 'AQUAMETRIA_C12_SLUG', 'calculadora-de-midia-filtrante' );
	define( 'AQUAMETRIA_C12_VERIFICADO_EM', '08/09/2026' );
	define( 'AQUAMETRIA_C12_ARTIGO', 'quanta-midia-biologica-o-aquario-precisa' );
	define( 'AQUAMETRIA_C12_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_registrar_no_hub' ) ) {
function aquametria_c12_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C12' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C12_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c12_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Catálogos embutidos (gerados — não edite à mão)
 *
 * O site não lê o repositório em tempo de execução. Depois de mexer em
 * dados/produtos-midia.json ou em dados/produtos-filtro.json:
 *     python3 ferramentas/gerar-catalogo-midias.py
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_catalogo_midias' ) ) {
function aquametria_c12_catalogo_midias() {
	/* CATALOGO-MIDIAS-INICIO — gerado por ferramentas/gerar-catalogo-midias.py */
	return array(
		array(
			'id' => 'seachem-purigen-100ml',
			'marca' => 'Seachem',
			'modelo' => 'Purigen 100 mL',
			'tipo' => 'quimica',
			'material' => 'resina',
			'embalagem_L' => 0.1,
			'peso_g' => null,
			'area_m2_L' => null,
			'dose_mL_por_L' => 0.25,
			'dose_texto' => '100 mL para 400 L',
			'dose_alt_mL_por_L' => null,
			'dose_alt_texto' => null,
			'dose_alt_ref' => null,
			'granulometria_mm' => null,
			'regeneravel' => true,
			'vida_util_meses' => 6,
			'posicao' => 'polimento',
			'volume_max_L' => 400,
			'fonte_ref' => 'Seachem, ficha do Purigen replicada pelo varejo BR (Atlantida Aquarios, Aqua Ura, Pro-Aquarista, Fazenda Submersa): 100 mL tratam ate 400 L, ou 1 mL para cada 4 L, por ate 6 meses; polimero macro e microporoso; escurece conforme esgota e e regenerado com solucao de agua sanitaria 1:1 por 24 h, seguida de enxague e neutralizacao',
			'fonte_url' => 'https://atlantidaaquarios.com.br/loja1/purigen-100-ml-seachem-trata-400-litros.html',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Entra no banco como a midia de polimento com dosagem declarada mais precisa que achamos: 0,25 mL por litro de agua, com validade declarada em meses e nao em \'ate saturar\'. E a prova de que a industria SABE publicar dosagem por litro quando quer - o que torna o silencio sobre a midia biologica ainda mais estranho.',
		),
		array(
			'id' => 'seachem-matrixcarbon-250ml',
			'marca' => 'Seachem',
			'modelo' => 'MatrixCarbon 250 mL',
			'tipo' => 'quimica',
			'material' => 'carvao-ativado',
			'embalagem_L' => 0.25,
			'peso_g' => null,
			'area_m2_L' => null,
			'dose_mL_por_L' => 0.625,
			'dose_texto' => '250 mL para 400 L',
			'dose_alt_mL_por_L' => null,
			'dose_alt_texto' => null,
			'dose_alt_ref' => null,
			'granulometria_mm' => null,
			'regeneravel' => false,
			'vida_util_meses' => null,
			'posicao' => 'quimica',
			'volume_max_L' => 400,
			'fonte_ref' => 'Seachem, ficha do MatrixCarbon replicada pelo varejo BR (Aqua SN, Fazenda Submersa, Aqua e Pesca, BR Fish): \'250 mL tratam facilmente 400 L por varios meses\'; carvao macroporoso de carvao betuminoso, baixo teor de cinzas, nao eleva o pH acima de 7,0 nem em agua destilada',
			'fonte_url' => 'https://www.aquasn.com.br/seachem-matrix-carbon-250ml-trata-400-litros',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'O contraponto de fabricante a regra brasileira de carvao ativado. O corpus BR (constante carvao-ativado) manda 1 a 2 g por litro de agua e troca a cada 15 a 30 dias; o fabricante declara 250 mL para 400 L, ou seja 0,625 mL por litro, durando varios meses. NAO da para converter uma coisa na outra nesta pagina: falta a densidade aparente do carvao com fonte, e sem ela transformar mL em g seria inventar constante. A C12 publica as duas em suas proprias unidades e diz por que nao converte.',
		),
		array(
			'id' => 'seachem-matrix-1l',
			'marca' => 'Seachem',
			'modelo' => 'Matrix 1 L',
			'tipo' => 'biologica',
			'material' => 'silicato-poroso',
			'embalagem_L' => 1.0,
			'peso_g' => null,
			'area_m2_L' => 700,
			'dose_mL_por_L' => 1.25,
			'dose_texto' => '250 mL para 200 L',
			'dose_alt_mL_por_L' => 2.642,
			'dose_alt_texto' => '1000 mL para 378.5 L',
			'dose_alt_ref' => 'Seachem, copy do produto em outra leitura (1 L para 100 galoes americanos = 2,6 mL por litro)',
			'granulometria_mm' => 10,
			'regeneravel' => null,
			'vida_util_meses' => null,
			'posicao' => 'biologica',
			'volume_max_L' => 200,
			'fonte_ref' => 'Seachem, pagina do Matrix (mais de 700 m2 de area por litro; particula de cerca de 10 mm; use 250 mL de Matrix para cada 200 L de agua); mesma coleta que gerou a constante seachem-matrix-dosagem do Bloco 2',
			'fonte_url' => 'https://www.seachem.com/matrix.php',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-07',
			'link' => 'https://s.shopee.com.br/9Khs5ozO8W',
			'anuncio' => 'Mídia biológica - Matrix 1 Litro (Granel) com Bolsa - Seachem',
			'loja' => 'shopee',
			'observacao' => 'Ancora principal da C12 e a primeira publicacao brasileira de mL de midia por litro com fonte de fabricante. O conflito e do proprio fabricante consigo mesmo, entao a C12 publica as duas leituras com atribuicao. Compare com o cesto do Eheim classic 250 (3,0 L de midia para 250 L = 12 mL/L): a diferenca entre a dosagem da marca de midia e o cesto do fabricante de filtro chega a uma ordem de grandeza, e ninguem no Brasil discute isso.',
		),
		array(
			'id' => 'jbl-micromec-1l',
			'marca' => 'JBL',
			'modelo' => 'MicroMec 1 L',
			'tipo' => 'biologica',
			'material' => 'vidro-sinterizado',
			'embalagem_L' => 1.0,
			'peso_g' => 650,
			'area_m2_L' => 1500,
			'dose_mL_por_L' => 5.0,
			'dose_texto' => '1000 mL para 200 L',
			'dose_alt_mL_por_L' => null,
			'dose_alt_texto' => null,
			'dose_alt_ref' => null,
			'granulometria_mm' => 14,
			'regeneravel' => null,
			'vida_util_meses' => 6,
			'posicao' => 'biologica',
			'volume_max_L' => 200,
			'fonte_ref' => 'JBL, pagina do MicroMec (650 g indicado para aquario de 200 L, troca a cada 6 meses; 1 L com 1500 m2 de superficie de colonizacao; esferas de vidro sinterizado com cerca de 14 mm; usar como penultimo estagio de filtragem)',
			'fonte_url' => 'https://www.jbl.de/pt/produtos/detail/2418/jbl-micromec',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'A TERCEIRA ancora de mL de midia biologica por litro de agua, e a que faltava para a C12 deixar de ser um duelo: 1000 mL para 200 L = 5,0 mL/L. Cai exatamente entre a Seachem (1,25 a 2,6 mL/L) e a Ocean Tech (12,5 mL/L). Repare que a area declarada, 1500 m2/L, e o MESMO numero que a Ocean Tech declara para outro produto, de outro material - sem nenhum dos dois publicar metodo de medicao.',
		),
		array(
			'id' => 'ocean-tech-bio-glass-1l',
			'marca' => 'Ocean Tech',
			'modelo' => 'Bio Glass 1 L',
			'tipo' => 'biologica',
			'material' => 'vidro-sinterizado',
			'embalagem_L' => 1.0,
			'peso_g' => null,
			'area_m2_L' => 1500,
			'dose_mL_por_L' => 12.5,
			'dose_texto' => '1000 mL para 80 L',
			'dose_alt_mL_por_L' => null,
			'dose_alt_texto' => null,
			'dose_alt_ref' => null,
			'granulometria_mm' => null,
			'regeneravel' => null,
			'vida_util_meses' => null,
			'posicao' => 'biologica',
			'volume_max_L' => 80,
			'fonte_ref' => 'Ocean Tech, ficha do Bio Glass replicada pelo varejo BR especializado (Aqua Life Brasil, Aquaricamp, Portal dos Bichos, Betta Aquarismo): midia de vidro sinterizado de alta porosidade chegando a 1500 m2 por litro; dosagem recomendada de 1 litro para cada 80 litros de agua; poros de 60 a 300 micrometros',
			'fonte_url' => 'https://www.aqualifebrasil.com.br/midias-filtrantes/midia-biologica-bio-glass-ceramica-1-litro-oceantech',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'A UNICA dosagem de midia biologica por litro de agua publicada por uma marca BRASILEIRA que o levantamento achou: 1 L para cada 80 L = 12,5 mL/L. E DEZ VEZES a leitura mais economica da Seachem (1,25 mL/L) para a mesma funcao. Nao ha metodo publicado dos dois lados que explique a diferenca - e e por isso que a C12 nao escolhe.',
		),
		array(
			'id' => 'eheim-substrat-pro-1l',
			'marca' => 'Eheim',
			'modelo' => 'SUBSTRAT pro 1 L',
			'tipo' => 'biologica',
			'material' => 'vidro-sinterizado',
			'embalagem_L' => 1.0,
			'peso_g' => null,
			'area_m2_L' => 450,
			'dose_mL_por_L' => null,
			'dose_texto' => null,
			'dose_alt_mL_por_L' => null,
			'dose_alt_texto' => null,
			'dose_alt_ref' => null,
			'granulometria_mm' => null,
			'regeneravel' => null,
			'vida_util_meses' => null,
			'posicao' => 'biologica',
			'volume_max_L' => null,
			'fonte_ref' => 'Eheim, SUBSTRAT pro (vidro sinterizado em esferas, cerca de 450 m2 de area por litro); midia de fabrica do classic 250 (2213)',
			'fonte_url' => 'https://eheim.com/en_GB/products/filter-media/biological/substrat',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-07',
			'link' => 'https://s.shopee.com.br/9051hAWjge',
			'anuncio' => 'Mídia Biológica Eheim Substrat Pro 1L',
			'loja' => 'shopee',
			'observacao' => 'Sem dosagem declarada e sem volume atendido, so entra na C12 pelo caminho da area superficial. Fica como o contraponto do Matrix: 450 contra mais de 700 m2/L, medidos por metodos que nenhum dos dois fabricantes publica.',
		),
	);
	/* CATALOGO-MIDIAS-FIM */
}
}

if ( ! function_exists( 'aquametria_c12_catalogo_filtros' ) ) {
function aquametria_c12_catalogo_filtros() {
	/* CATALOGO-FILTROS-INICIO — gerado por ferramentas/gerar-catalogo-midias.py */
	return array(
		array(
			'id' => 'seachem-tidal-55',
			'marca' => 'Seachem',
			'modelo' => 'Tidal 55',
			'tipo' => 'hang-on',
			'midia_L' => 1.2,
			'midia_L_alt' => null,
			'midia_alt_ref' => null,
			'midia_ref' => null,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'fonte_ref' => 'Seachem, pagina comparativa da linha Tidal (Tidal 55: filter volume 0,32 US gal = 1,2 L) e ficha do Tidal 55 replicada por varejo especializado internacional',
			'fonte_url' => 'https://www.seachem.com/tidal-compare.php',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
		),
		array(
			'id' => 'atman-at-3338',
			'marca' => 'Atman',
			'modelo' => 'AT-3338',
			'tipo' => 'canister',
			'midia_L' => 1.6,
			'midia_L_alt' => 4.8,
			'midia_alt_ref' => 'leitura generosa: \'1,6 litros\' lido como a capacidade de CADA um dos tres cestos (1,6 x 3), que e o que a geometria de 17 x 17 x 6 cm por cesto comporta',
			'midia_ref' => 'leitura conservadora: \'1,6 litros de midia\' lido como a capacidade do CONJUNTO dos tres cestos',
			'volume_min_L' => null,
			'volume_max_L' => 450,
			'fonte_ref' => 'Ficha replicada pelo varejo BR especializado (Aquaricamp, KZ Power, Aquarismo Total): \'3 cestos para midia filtrante com dimensoes de 17x17x6 e capacidade de 1,6 litros de midia\'',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-canister-at-3338-vaz-o-1200-l-h-gratis-1-litro-ceramica.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
		),
		array(
			'id' => 'sunsun-hw-603b',
			'marca' => 'SunSun',
			'modelo' => 'HW-603B',
			'tipo' => 'canister',
			'midia_L' => 2.3,
			'midia_L_alt' => null,
			'midia_alt_ref' => null,
			'midia_ref' => null,
			'volume_min_L' => null,
			'volume_max_L' => 80,
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha do SunSun HW-603B: 400 L/h, 2,3 L de camara de midia, 110 V',
			'fonte_url' => 'https://www.proaquarista.com.br/produto/sunsun-canister-hw-603b-23l-400lh-110v.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
		),
		array(
			'id' => 'eheim-classic-250-2213',
			'marca' => 'Eheim',
			'modelo' => 'classic 250 (2213)',
			'tipo' => 'canister',
			'midia_L' => 3.0,
			'midia_L_alt' => null,
			'midia_alt_ref' => null,
			'midia_ref' => null,
			'volume_min_L' => null,
			'volume_max_L' => 250,
			'fonte_ref' => 'Eheim, dados do classic 250 (2213); mesma coleta que gerou a constante eheim-classic-250-2213 do Bloco 2',
			'fonte_url' => 'https://eheim.com/en_GB/aquatics/aquarium-technology/filter/external-filter/classic-250',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-07',
		),
		array(
			'id' => 'atman-at-3338s',
			'marca' => 'Atman',
			'modelo' => 'AT-3338S',
			'tipo' => 'canister',
			'midia_L' => 3.5,
			'midia_L_alt' => 10.5,
			'midia_alt_ref' => 'leitura por cesto: 3,5 L em cada um dos tres cestos. E como a mesma frase e lida no AT-3338, e por isso fica registrada - mas as dimensoes do proprio anuncio a contradizem',
			'midia_ref' => 'leitura do conjunto: \'3,5 litros de midia\' como capacidade dos tres cestos somados. E a unica coerente com as dimensoes declaradas, porque um cesto de 21 x 21 x 7 cm tem 3,09 L brutos e nao comporta 3,5 L',
			'volume_min_L' => 150,
			'volume_max_L' => 400,
			'fonte_ref' => 'Ficha replicada pelo varejo BR especializado (Aqua SN): \'3 cestos para midia filtrante com dimensoes de 21x21x7 cm e capacidade de 3,5 litros de midia\'',
			'fonte_url' => 'https://www.aquasn.com.br/atman-filtro-canister-at-3338s-1500-lh-220v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
		),
	);
	/* CATALOGO-FILTROS-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_css' ) ) {
function aquametria_c12_css() {
	return <<<'CSS'
.aqm-c12{--c12-tinta:var(--aqm-tinta,#0D1B22);--c12-lamina:var(--aqm-lamina,#0E7C8C);
--c12-papel:var(--aqm-papel,#F4F7F7);--c12-superficie:var(--aqm-superficie,#FFFFFF);
--c12-traco:var(--aqm-traco,#DDE5E6);--c12-legenda:var(--aqm-legenda,#5C7075);
--c12-alerta:var(--aqm-alerta,#B5762A);
--c12-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c12-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c12-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c12-texto);color:var(--c12-tinta);}
.aqm-c12 *{box-sizing:border-box;}
.aqm-c12 form{margin:0;}
.aqm-c12-painel{background:var(--c12-superficie);border:1px solid var(--c12-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c12-painel h3{font-family:var(--c12-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c12-painel h4{font-family:var(--c12-display);font-size:.95rem;margin:1.1rem 0 .3rem;}
.aqm-c12-painel .aqm-c12-sub{color:var(--c12-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c12-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));gap:.9rem;}
.aqm-c12-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c12-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c12-campo .aqm-c12-dica{font-size:.74rem;color:var(--c12-legenda);line-height:1.35;}
.aqm-c12 input[type=text],.aqm-c12 input[type=date],.aqm-c12 select{width:100%;font-family:var(--c12-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c12-traco);border-radius:2px;background:var(--c12-superficie);color:var(--c12-tinta);}
.aqm-c12 select{font-family:var(--c12-texto);}
.aqm-c12 input:focus,.aqm-c12 select:focus{outline:2px solid var(--c12-lamina);outline-offset:1px;}
.aqm-c12 input.aqm-c12-erro{border-color:var(--c12-alerta);}
.aqm-c12-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c12-caixa input{margin-top:.2rem;}
.aqm-c12-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c12 button{font-family:var(--c12-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c12-lamina);color:var(--c12-superficie);cursor:pointer;}
.aqm-c12 button.aqm-c12-secundario{background:transparent;color:var(--c12-lamina);border:1px solid var(--c12-traco);}
.aqm-c12 button:hover{filter:brightness(1.08);}
.aqm-c12-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c12-avisos li{font-size:.88rem;color:var(--c12-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c12-resultado{margin:0 0 1.2rem;}
.aqm-c12-faixa{background:var(--c12-superficie);border:2px solid var(--c12-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c12-rotulo{font-family:var(--c12-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c12-legenda);}
.aqm-c12-valor{font-family:var(--c12-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c12-valor .aqm-c12-unidade{font-size:.95rem;font-weight:500;color:var(--c12-legenda);margin-left:.3rem;}
.aqm-c12-criterio{font-size:.83rem;color:var(--c12-legenda);line-height:1.5;margin:0;}
.aqm-c12-delta{display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:baseline;margin:.6rem 0 0;font-family:var(--c12-mono);font-size:.86rem;color:var(--c12-legenda);}
.aqm-c12-delta b{color:var(--c12-tinta);font-weight:600;}
.aqm-c12-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c12-cartao{background:var(--c12-superficie);border:1px solid var(--c12-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c12-cartao .aqm-c12-valor{font-size:1.5rem;}
.aqm-c12-cartao-total{border-style:dashed;}
.aqm-c12-nota{border-left:3px solid var(--c12-lamina);background:var(--c12-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c12-legenda);margin:0 0 1rem;}
.aqm-c12-nota strong{color:var(--c12-tinta);}
.aqm-c12-nota.aqm-c12-nota-alerta{border-left-color:var(--c12-alerta);}
.aqm-c12-barra{height:.6rem;background:var(--c12-papel);border:1px solid var(--c12-traco);border-radius:2px;overflow:hidden;margin:.35rem 0 .2rem;}
.aqm-c12-barra span{display:block;height:100%;background:var(--c12-lamina);}
.aqm-c12-barra.aqm-c12-barra-estoura span{background:var(--c12-alerta);}
.aqm-c12-ordem{list-style:none;margin:.6rem 0 0;padding:0;display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;}
.aqm-c12-ordem li{font-family:var(--c12-mono);font-size:.8rem;background:var(--c12-papel);border:1px solid var(--c12-traco);border-radius:2px;padding:.3rem .55rem;}
.aqm-c12-ordem li.aqm-c12-seta{border:0;background:transparent;color:var(--c12-legenda);padding:0 .1rem;}
.aqm-c12-produtos{margin:0 0 1.2rem;}
.aqm-c12-produtos h3{font-family:var(--c12-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c12-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c12-produto{background:var(--c12-superficie);border:1px solid var(--c12-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c12-produto.aqm-c12-produto-sem{border-style:dashed;}
.aqm-c12-placa{background:var(--c12-papel);border:1px solid var(--c12-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c12-placa .aqm-c12-marca{font-family:var(--c12-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c12-placa .aqm-c12-numero{font-family:var(--c12-mono);font-size:1.15rem;font-weight:600;color:var(--c12-lamina);line-height:1.1;}
.aqm-c12-placa .aqm-c12-un{font-family:var(--c12-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c12-legenda);}
.aqm-c12-produto h4{font-family:var(--c12-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c12-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c12-porque strong{font-family:var(--c12-mono);font-size:.86rem;}
.aqm-c12-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c12-legenda);line-height:1.5;}
.aqm-c12-ficha li{margin:0;}
.aqm-c12-ficha b{font-family:var(--c12-mono);font-weight:600;color:var(--c12-tinta);}
.aqm-c12-loja{display:inline-block;font-family:var(--c12-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c12-lamina);color:var(--c12-superficie);text-decoration:none;}
.aqm-c12-loja:hover{filter:brightness(1.08);color:var(--c12-superficie);}
.aqm-c12-semloja{font-size:.82rem;color:var(--c12-legenda);font-style:italic;}
.aqm-c12-aviso-afiliado{background:var(--c12-papel);border:1px solid var(--c12-traco);border-left:3px solid var(--c12-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c12-legenda);margin:1rem 0 0;}
.aqm-c12-aviso-afiliado strong{color:var(--c12-tinta);}
.aqm-c12-citar{background:var(--c12-papel);border:1px dashed var(--c12-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c12-citar p{margin:0 0 .6rem;}
.aqm-c12-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c12-tabela,.aqm-c12-exemplos{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c12-tabela th,.aqm-c12-tabela td,.aqm-c12-exemplos th,.aqm-c12-exemplos td{border:1px solid var(--c12-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c12-tabela th,.aqm-c12-exemplos th{background:var(--c12-papel);font-family:var(--c12-display);font-size:.8rem;}
.aqm-c12-tabela td:first-child{font-family:var(--c12-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c12-tabela td.aqm-c12-num{font-family:var(--c12-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.aqm-c12-exemplos{min-width:46rem;}
.aqm-c12-exemplos .aqm-c12-num{display:block;font-family:var(--c12-mono);font-variant-numeric:tabular-nums;font-size:.92rem;font-weight:600;color:var(--c12-tinta);line-height:1.25;}
.aqm-c12-exemplos .aqm-c12-un{display:block;font-size:.76rem;color:var(--c12-legenda);line-height:1.35;margin-top:.15rem;}
.aqm-c12-exemplos .aqm-c12-estoura{color:var(--c12-alerta);font-weight:600;}
.aqm-c12-direta{background:var(--c12-papel);border:1px dashed var(--c12-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.55;margin:0 0 1.2rem;}
.aqm-c12-direta p{margin:0 0 .6rem;}
.aqm-c12-direta p:last-child{margin-bottom:0;}
.aqm-c12-aviso-tabela{background:var(--c12-papel);border:1px solid var(--c12-traco);border-left:3px solid var(--c12-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c12-legenda);margin:1rem 0 0;}
.aqm-c12-aviso-tabela strong{color:var(--c12-tinta);}
.aqm-c12-selo{display:inline-block;font-family:var(--c12-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c12-alerta);border:1px solid var(--c12-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c12-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c12-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c12-oculto{display:none;}
@media (max-width:600px){.aqm-c12-valor{font-size:1.6rem;}
.aqm-c12-produto{grid-template-columns:1fr;}
.aqm-c12-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_js' ) ) {
function aquametria_c12_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';

	/* Constantes do corpus do Bloco 1. Cada uma com o nome de quem publicou:
	   nenhuma delas é medição nossa, e nenhuma delas é consenso. */
	var CARVAO_G_POR_L = [1, 2];        /* carvao-ativado, Aquarismo Paulista */
	var CARVAO_TROCA_DIAS = [15, 30];   /* carvao-ativado, Aquarismo Paulista */
	var PERLON_TROCA_DIAS = [7, 15];    /* perlon-troca: semanal a quinzenal */
	var CERAMICA_TROCA_MESES = [6, 12]; /* ceramica-regeneracao */
	var TPA_AMPLA = [10, 30];           /* tpa-percentual, Escola de Aquário */
	var TPA_SEMANAL = [25, 30];         /* tpa-percentual, Aquário Vivo */
	var TPA_TETO = 50;                  /* tpa-percentual, teto sem estresse */

	/* ordem-midias-canister (AquaPeixes). Vale como ORDEM, nunca como
	   proporção: nenhuma fonte do corpus reparte o cesto em porcentagens. */
	var ORDEM = ['cerâmica / argila expandida', 'perlon', 'carvão', 'perlon', 'cerâmica', 'perlon'];

	var raiz = document.querySelector('.aqm-c12');
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

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	/* Mililitro de mídia é número grosso: ninguém mede 137,5 mL com colher.
	   Acima de 1 L a resposta sai em litros, que é como a mídia se compra. */
	function mL(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		if (n >= 1000) { return fmt(Math.round(n / 25) * 25 / 1000, 2) + ' L'; }
		return fmt(Math.round(n / 5) * 5, 0) + ' mL';
	}

	function pct(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return fmt(Math.round(n), 0) + ' %';
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

	/* ------------------------------------------------------------- âncoras */

	/* As âncoras NÃO são digitadas aqui: saem do banco de produtos, que é a
	   fonte da verdade. Mídia nova com dosagem declarada entra na tabela
	   sozinha, no próximo gerador de catálogo. */
	function ancorasBio() {
		var out = [];
		AQM_C12_MIDIAS.forEach(function (m) {
			if (m.tipo !== 'biologica' || m.dose_mL_por_L === null) { return; }
			out.push({
				id: m.id, marca: m.marca, modelo: m.modelo, mlL: m.dose_mL_por_L,
				texto: m.dose_texto, leitura: null, ref: m.fonte_ref, url: m.fonte_url,
				status: m.fonte_status, verificado: m.verificado_em
			});
			if (m.dose_alt_mL_por_L !== null && m.dose_alt_mL_por_L !== undefined) {
				out.push({
					id: m.id + '-alt', marca: m.marca, modelo: m.modelo, mlL: m.dose_alt_mL_por_L,
					texto: m.dose_alt_texto, leitura: m.dose_alt_ref, ref: m.fonte_ref,
					url: m.fonte_url, status: m.fonte_status, verificado: m.verificado_em
				});
			}
		});
		out.sort(function (a, b) { return a.mlL - b.mlL; });
		return out;
	}

	/* A segunda família: quem vende FILTRO declara quanto de mídia cabe nele e
	   para que aquário ele serve. A divisão das duas declarações é mídia TOTAL
	   por litro de água — todas as camadas, não só a biológica. O divisor é o
	   MAIOR volume que o fabricante declara atender, que é a leitura menos
	   favorável a ele. */
	function ancorasFiltro() {
		var out = [];
		AQM_C12_FILTROS.forEach(function (f) {
			if (!f.midia_L || !f.volume_max_L) { return; }
			var item = {
				id: f.id, marca: f.marca, modelo: f.modelo, tipo: f.tipo,
				mlL: Math.round(f.midia_L * 1000 / f.volume_max_L * 100) / 100,
				midia_L: f.midia_L, volume_max_L: f.volume_max_L,
				ref: f.fonte_ref, url: f.fonte_url, status: f.fonte_status,
				verificado: f.verificado_em, midia_ref: f.midia_ref,
				alt_mlL: null, alt_midia_L: null, alt_ref: f.midia_alt_ref
			};
			if (f.midia_L_alt) {
				item.alt_midia_L = f.midia_L_alt;
				item.alt_mlL = Math.round(f.midia_L_alt * 1000 / f.volume_max_L * 100) / 100;
			}
			out.push(item);
		});
		out.sort(function (a, b) { return a.mlL - b.mlL; });
		return out;
	}

	function filtroPorId(id) {
		for (var i = 0; i < AQM_C12_FILTROS.length; i++) {
			if (AQM_C12_FILTROS[i].id === id) { return AQM_C12_FILTROS[i]; }
		}
		return null;
	}

	/* ------------------------------------------------------------- entradas */

	function campos() {
		return {
			volume: num(el('aqm-c12-volume').value),
			filtro: el('aqm-c12-filtro').value,
			midiaManual: num(el('aqm-c12-midia-manual').value),
			perfil: el('aqm-c12-perfil').value,
			quimica: el('aqm-c12-quimica').checked,
			data: el('aqm-c12-data').value
		};
	}

	/* ------------------------------------------------------------- o cálculo */

	function calcular(d) {
		var erros = [];
		if (d.volume === null || d.volume <= 0) {
			erros.push('Informe o volume real de água, em litros — é sobre a água que existe que a conta é feita, não sobre a etiqueta do aquário.');
		} else if (d.volume > 20000) {
			erros.push('Acima de 20.000 L isto deixa de ser aquário e vira lago ou sistema comercial, que tem outra engenharia. Não temos fonte para esse porte.');
		}
		if (erros.length) { return { erros: erros }; }

		var V = d.volume;
		var bio = ancorasBio().map(function (a) {
			return { ancora: a, mL: a.mlL * V };
		});
		var totais = ancorasFiltro().map(function (a) {
			return { ancora: a, mL: a.mlL * V, mL_alt: a.alt_mlL === null ? null : a.alt_mlL * V };
		});

		/* O filtro escolhido: do catálogo, ou digitado à mão. */
		var filtro = null;
		var midiaL = null;
		var midiaLalt = null;
		var midiaOrigem = null;
		if (d.filtro && d.filtro !== 'outro') {
			filtro = filtroPorId(d.filtro);
			if (filtro) {
				midiaL = filtro.midia_L;
				midiaLalt = filtro.midia_L_alt;
				midiaOrigem = 'catalogo';
			}
		} else if (d.midiaManual !== null && d.midiaManual > 0) {
			midiaL = d.midiaManual;
			midiaOrigem = 'manual';
		}

		var ocupacao = null;
		if (midiaL) {
			ocupacao = bio.map(function (b) {
				return {
					ancora: b.ancora,
					mL: b.mL,
					pct: b.mL / (midiaL * 1000) * 100,
					pct_alt: midiaLalt ? b.mL / (midiaLalt * 1000) * 100 : null
				};
			});
		}

		/* Química: cada mídia responde pela SUA dosagem declarada. Não há
		   dosagem média de mídia química, e não inventamos uma. */
		var quimicas = [];
		AQM_C12_MIDIAS.forEach(function (m) {
			if (m.tipo !== 'quimica' || m.dose_mL_por_L === null) { return; }
			var precisa = m.dose_mL_por_L * V;
			quimicas.push({
				midia: m,
				mL: precisa,
				embalagens: m.embalagem_L ? Math.ceil(precisa / (m.embalagem_L * 1000)) : null
			});
		});

		return {
			erros: [],
			entradas: d,
			V: V,
			bio: bio,
			piso: bio.length ? bio[0] : null,
			teto: bio.length ? bio[bio.length - 1] : null,
			totais: totais,
			filtro: filtro,
			midiaL: midiaL,
			midiaLalt: midiaLalt,
			midiaOrigem: midiaOrigem,
			ocupacao: ocupacao,
			quimicas: quimicas,
			carvao_g: [CARVAO_G_POR_L[0] * V, CARVAO_G_POR_L[1] * V],
			tpa: {
				ampla: [TPA_AMPLA[0] / 100 * V, TPA_AMPLA[1] / 100 * V],
				semanal: [TPA_SEMANAL[0] / 100 * V, TPA_SEMANAL[1] / 100 * V],
				teto: TPA_TETO / 100 * V
			},
			calendario: calendario(d.data)
		};
	}

	/* --------------------------------------------------------- calendário */

	/* Data digitada é lida como data LOCAL, não UTC: 'new Date("2026-09-08")'
	   vira meia-noite em Greenwich e volta um dia no Brasil. */
	function lerData(texto) {
		var p = String(texto || '').split('-');
		if (p.length !== 3) { return null; }
		var d = new Date(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10));
		return isFinite(d.getTime()) ? d : null;
	}

	function maisDias(base, dias) {
		var d = new Date(base.getTime());
		d.setDate(d.getDate() + dias);
		return d;
	}

	function maisMeses(base, meses) {
		var d = new Date(base.getTime());
		d.setMonth(d.getMonth() + meses);
		return d;
	}

	function escrever(d) {
		return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric' });
	}

	function calendario(texto) {
		var base = lerData(texto);
		if (!base) { return null; }
		return {
			base: escrever(base),
			perlon: [escrever(maisDias(base, PERLON_TROCA_DIAS[0])), escrever(maisDias(base, PERLON_TROCA_DIAS[1]))],
			carvao: [escrever(maisDias(base, CARVAO_TROCA_DIAS[0])), escrever(maisDias(base, CARVAO_TROCA_DIAS[1]))],
			ceramica: [escrever(maisMeses(base, CERAMICA_TROCA_MESES[0])), escrever(maisMeses(base, CERAMICA_TROCA_MESES[1]))]
		};
	}

	/* ------------------------------------------------------------- a tela */

	function pintar(r) {
		var erros = el('aqm-c12-erros');
		erros.innerHTML = '';
		if (r.erros && r.erros.length) {
			r.erros.forEach(function (t) {
				var li = document.createElement('li');
				li.textContent = t;
				erros.appendChild(li);
			});
			el('aqm-c12-saida').classList.add('aqm-c12-oculto');
			return;
		}

		el('aqm-c12-saida').classList.remove('aqm-c12-oculto');

		pintarFaixa(r);
		pintarAncoras(r);
		pintarCesto(r);
		pintarCamadas(r);
		pintarQuimica(r);
		pintarManutencao(r);
		pintarEditoriais(r);
		pintarProdutos(r);
		pintarCitacao(r);

		guardar(r);
		atualizarEndereco(r.entradas);
	}

	function pintarFaixa(r) {
		if (!r.piso || !r.teto) {
			el('aqm-c12-faixa-valor').textContent = '—';
			el('aqm-c12-faixa-criterio').textContent = 'O banco de mídias não tem hoje nenhuma dosagem declarada por fabricante. Sem isso, esta página não publica número.';
			return;
		}
		el('aqm-c12-faixa-valor').innerHTML = mL(r.piso.mL) + ' a ' + mL(r.teto.mL)
			+ '<span class="aqm-c12-unidade">de mídia biológica</span>';

		var vezes = r.teto.ancora.mlL / r.piso.ancora.mlL;
		el('aqm-c12-faixa-criterio').innerHTML =
			'Para os <strong>' + litros(r.V) + ' L</strong> de água do seu aquário, segundo as '
			+ r.bio.length + ' dosagens que fabricantes de mídia declaram e que estão no nosso banco. '
			+ 'O piso é ' + esc(r.piso.ancora.marca) + ' (' + fmt(r.piso.ancora.mlL, 2) + ' mL/L) e o teto é '
			+ esc(r.teto.ancora.marca) + ' (' + fmt(r.teto.ancora.mlL, 2) + ' mL/L). '
			+ '<strong>A faixa é ' + fmt(Math.round(vezes * 10) / 10, 1) + ' vezes larga porque os fabricantes discordam '
			+ fmt(Math.round(vezes * 10) / 10, 1) + ' vezes entre si</strong> — não porque a conta seja imprecisa. '
			+ 'Nenhuma fonte brasileira que o nosso levantamento encontrou publica este número, nem sequer para discordar dele.';

		var delta = el('aqm-c12-delta');
		delta.innerHTML = '';
		[
			['faixa em mL por litro', fmt(r.piso.ancora.mlL, 2) + ' a ' + fmt(r.teto.ancora.mlL, 2)],
			['dosagens no banco', String(r.bio.length)],
			['volume usado', litros(r.V) + ' L']
		].forEach(function (par) {
			var s = document.createElement('span');
			s.innerHTML = par[0] + ': <b>' + par[1] + '</b>';
			delta.appendChild(s);
		});
	}

	function pintarAncoras(r) {
		var corpo = el('aqm-c12-ancoras-corpo');
		corpo.innerHTML = '';

		r.bio.forEach(function (b) {
			var tr = document.createElement('tr');
			tr.innerHTML = '<td>' + esc(b.ancora.marca) + '</td>'
				+ '<td class="aqm-c12-num">' + fmt(b.ancora.mlL, 2) + ' mL/L</td>'
				+ '<td class="aqm-c12-num">' + mL(b.mL) + '</td>'
				+ '<td>' + esc(b.ancora.modelo) + ', declarado como "' + esc(b.ancora.texto) + '"'
				+ (b.ancora.leitura ? ' <span class="aqm-c12-selo">segunda leitura</span> ' + esc(b.ancora.leitura) : '')
				+ (b.ancora.url ? ' — <a href="' + esc(b.ancora.url) + '" target="_blank" rel="noopener nofollow">fonte</a>' : '')
				+ (b.ancora.status ? ' (' + esc(b.ancora.status) + ', conferido em ' + esc(dataBr(b.ancora.verificado)) + ')' : '')
				+ '</td>';
			corpo.appendChild(tr);
		});

		var corpoT = el('aqm-c12-totais-corpo');
		corpoT.innerHTML = '';
		if (!r.totais.length) {
			el('aqm-c12-totais').classList.add('aqm-c12-oculto');
		} else {
			el('aqm-c12-totais').classList.remove('aqm-c12-oculto');
			r.totais.forEach(function (t) {
				var faixa = t.mL_alt === null
					? mL(t.mL)
					: mL(Math.min(t.mL, t.mL_alt)) + ' a ' + mL(Math.max(t.mL, t.mL_alt));
				var razao = t.mL_alt === null
					? fmt(t.ancora.mlL, 2) + ' mL/L'
					: fmt(Math.min(t.ancora.mlL, t.ancora.alt_mlL), 2) + ' a ' + fmt(Math.max(t.ancora.mlL, t.ancora.alt_mlL), 2) + ' mL/L';
				var tr = document.createElement('tr');
				tr.innerHTML = '<td>' + esc(t.ancora.marca) + '</td>'
					+ '<td class="aqm-c12-num">' + razao + '</td>'
					+ '<td class="aqm-c12-num">' + faixa + '</td>'
					+ '<td>' + esc(t.ancora.modelo) + ': ' + fmt(t.ancora.midia_L, 1) + ' L de mídia'
					+ (t.ancora.alt_midia_L ? ' (ou ' + fmt(t.ancora.alt_midia_L, 1) + ' L, na outra leitura da mesma ficha)' : '')
					+ ' para até ' + litros(t.ancora.volume_max_L) + ' L de aquário'
					+ (t.ancora.url ? ' — <a href="' + esc(t.ancora.url) + '" target="_blank" rel="noopener nofollow">fonte</a>' : '')
					+ (t.ancora.status ? ' (' + esc(t.ancora.status) + ')' : '')
					+ '</td>';
				corpoT.appendChild(tr);
			});
		}
	}

	/* O teto físico. É o número que decide a compra e que ninguém publica:
	   a dosagem só vale se couber no cesto que a pessoa já tem. */
	function pintarCesto(r) {
		var bloco = el('aqm-c12-cesto');
		var lista = el('aqm-c12-cesto-lista');
		var sem = el('aqm-c12-cesto-sem');
		lista.innerHTML = '';

		if (!r.midiaL) {
			bloco.classList.add('aqm-c12-oculto');
			sem.classList.remove('aqm-c12-oculto');
			sem.innerHTML = '<strong>Escolha o filtro para ver o teto físico.</strong> '
				+ 'A dosagem só vale se a mídia couber no cesto que você já tem — e essa é a conta que decide a compra. '
				+ 'O nosso banco tem ' + AQM_C12_FILTROS.length + ' filtro(s) com volume útil de mídia declarado. '
				+ 'Se o seu não estiver na lista, meça o cesto e digite o volume: comprimento × largura × altura em centímetros, dividido por mil, dá litros.';
			return;
		}

		sem.classList.add('aqm-c12-oculto');
		bloco.classList.remove('aqm-c12-oculto');

		var nome = r.filtro ? (r.filtro.marca + ' ' + r.filtro.modelo) : 'o filtro que você mediu';
		el('aqm-c12-cesto-sub').innerHTML =
			'Em <strong>' + esc(nome) + '</strong> cabem <strong>' + fmt(r.midiaL, 1) + ' L</strong> de mídia'
			+ (r.midiaLalt ? ' por uma leitura da ficha, ou <strong>' + fmt(r.midiaLalt, 1) + ' L</strong> pela outra — a ficha do varejo é ambígua e nós não desempatamos' : '')
			+ '. Abaixo, quanto desse espaço cada dosagem declarada ocuparia só com a mídia biológica. '
			+ 'O que sobrar precisa acomodar a mecânica e a química, que também moram lá dentro.';

		r.ocupacao.forEach(function (o) {
			var li = document.createElement('li');
			li.className = 'aqm-c12-cartao';
			var estoura = o.pct > 100;
			li.innerHTML = '<span class="aqm-c12-rotulo">' + esc(o.ancora.marca)
				+ (o.ancora.leitura ? ' · segunda leitura' : '') + '</span>'
				+ '<span class="aqm-c12-valor">' + pct(Math.min(o.pct, 999)) + '</span>'
				+ '<div class="aqm-c12-barra' + (estoura ? ' aqm-c12-barra-estoura' : '') + '">'
				+ '<span style="width:' + Math.min(o.pct, 100) + '%"></span></div>'
				+ '<p class="aqm-c12-criterio">' + mL(o.mL) + ' de mídia biológica a ' + fmt(o.ancora.mlL, 2) + ' mL/L. '
				+ (estoura
					? '<strong>Não cabe.</strong> Nesta dosagem, o seu filtro não comporta nem a camada biológica sozinha — antes de comprar mídia, o problema é o filtro.'
					: 'Sobram ' + pct(100 - o.pct) + ' do cesto para a mecânica e a química.')
				+ (o.pct_alt !== null ? ' Pela outra leitura da ficha do filtro: ' + pct(Math.min(o.pct_alt, 999)) + '.' : '')
				+ '</p>';
			lista.appendChild(li);
		});
	}

	function pintarCamadas(r) {
		var ol = el('aqm-c12-ordem');
		ol.innerHTML = '';
		ORDEM.forEach(function (camada, i) {
			if (i > 0) {
				var seta = document.createElement('li');
				seta.className = 'aqm-c12-seta';
				seta.textContent = '→';
				ol.appendChild(seta);
			}
			var li = document.createElement('li');
			li.textContent = camada;
			ol.appendChild(li);
		});
	}

	function pintarQuimica(r) {
		var bloco = el('aqm-c12-quimica-bloco');
		if (!r.entradas.quimica) {
			bloco.classList.add('aqm-c12-oculto');
			return;
		}
		bloco.classList.remove('aqm-c12-oculto');

		el('aqm-c12-carvao-br').innerHTML =
			'<strong>Pela regra brasileira</strong> (1 a 2 g por litro de água, Aquarismo Paulista): '
			+ '<b>' + fmt(Math.round(r.carvao_g[0]), 0) + ' a ' + fmt(Math.round(r.carvao_g[1]), 0) + ' g</b> de carvão ativado, '
			+ 'trocado a cada ' + CARVAO_TROCA_DIAS[0] + ' a ' + CARVAO_TROCA_DIAS[1] + ' dias.';

		var lista = el('aqm-c12-quimica-lista');
		lista.innerHTML = '';
		if (!r.quimicas.length) {
			var vazio = document.createElement('li');
			vazio.className = 'aqm-c12-criterio';
			vazio.textContent = 'O banco ainda não tem mídia química com dosagem declarada.';
			lista.appendChild(vazio);
		}
		r.quimicas.forEach(function (q) {
			var li = document.createElement('li');
			li.className = 'aqm-c12-criterio';
			li.innerHTML = '<strong>' + esc(q.midia.marca) + ' ' + esc(q.midia.modelo) + '</strong> declara '
				+ esc(q.midia.dose_texto) + ' (' + fmt(q.midia.dose_mL_por_L, 3) + ' mL/L): para o seu aquário, <b>'
				+ mL(q.mL) + '</b>'
				+ (q.embalagens ? ', que é ' + q.embalagens + ' embalagem(ns) de ' + fmt(q.midia.embalagem_L, 2) + ' L' : '')
				+ (q.midia.vida_util_meses ? ', com validade declarada de ' + q.midia.vida_util_meses + ' meses' : '')
				+ '.';
			lista.appendChild(li);
		});
	}

	function pintarManutencao(r) {
		var cal = r.calendario;
		var corpo = el('aqm-c12-calendario-corpo');
		corpo.innerHTML = '';
		var linhas = [
			['Perlon (mecânica fina)', 'semanal a quinzenal', cal ? cal.perlon[0] + ' a ' + cal.perlon[1] : '—', 'perlon-troca'],
			['Carvão ativado', CARVAO_TROCA_DIAS[0] + ' a ' + CARVAO_TROCA_DIAS[1] + ' dias', cal ? cal.carvao[0] + ' a ' + cal.carvao[1] : '—', 'carvao-ativado'],
			['Cerâmica / mídia biológica', 'substituição PARCIAL a cada ' + CERAMICA_TROCA_MESES[0] + ' a ' + CERAMICA_TROCA_MESES[1] + ' meses', cal ? cal.ceramica[0] + ' a ' + cal.ceramica[1] : '—', 'ceramica-regeneracao']
		];
		linhas.forEach(function (l) {
			var tr = document.createElement('tr');
			tr.innerHTML = '<td>' + l[3] + '</td><td>' + l[0] + '</td><td>' + l[1] + '</td><td class="aqm-c12-num">' + l[2] + '</td>';
			corpo.appendChild(tr);
		});
		el('aqm-c12-calendario-sub').textContent = cal
			? 'Contado a partir de ' + cal.base + '. As datas são a aritmética da faixa que cada fonte publica, não uma recomendação nossa de dia exato.'
			: 'Preencha a data da última manutenção para ver as datas calculadas.';

		el('aqm-c12-tpa-texto').innerHTML =
			'Trocar <b>' + litros(r.tpa.ampla[0]) + ' a ' + litros(r.tpa.ampla[1]) + ' L</b> por vez '
			+ '(' + TPA_AMPLA[0] + ' a ' + TPA_AMPLA[1] + ' % do volume, Escola de Aquário), ou <b>'
			+ litros(r.tpa.semanal[0]) + ' a ' + litros(r.tpa.semanal[1]) + ' L</b> por semana '
			+ '(' + TPA_SEMANAL[0] + ' a ' + TPA_SEMANAL[1] + ' %, Aquário Vivo). '
			+ 'Teto sem estresse: <b>' + litros(r.tpa.teto) + ' L</b> (' + TPA_TETO + ' %). '
			+ 'A água nova entra com no máximo 1 °C de diferença da água do aquário; acima de 2 °C é choque térmico.';
	}

	function pintarEditoriais(r) {
		var ul = el('aqm-c12-editoriais');
		ul.innerHTML = '';
		var itens = [
			'<strong>Não escolhemos uma dosagem.</strong> A resposta é a faixa inteira, com o nome de quem sustenta cada extremo. Publicar um número só seria fingir que os outros fabricantes não existem.',
			'<strong>Não repartimos o cesto em porcentagens.</strong> Nenhuma fonte do nosso corpus diz quanto do volume é mecânica, quanto é biológica e quanto é química. Publicamos a ordem, que tem fonte, e o teto físico, que é do fabricante do filtro.',
			'<strong>Não convertemos grama em mililitro.</strong> A regra brasileira de carvão é em gramas por litro; a do fabricante é em mililitros por litro. Sem a densidade aparente do carvão com fonte, converter uma na outra seria inventar constante.',
			'<strong>A área de superfície não compara marcas.</strong> Cada fabricante mede como quer e nenhum publica o método. Os números aparecem com atribuição e nunca como ranking.',
			'<strong>A ordem dos produtos é a da dosagem declarada</strong>, da mais econômica para a mais generosa. É critério técnico, e não comissão: mídia sem link de loja aparece na mesma lista, na mesma ordem.'
		];
		if (r.midiaOrigem === 'manual') {
			itens.push('<strong>O volume de mídia foi medido por você</strong>, não declarado pelo fabricante. A conta do teto físico é tão boa quanto a sua fita métrica.');
		}
		itens.forEach(function (t) {
			var li = document.createElement('li');
			li.className = 'aqm-c12-criterio';
			li.style.margin = '0 0 .5rem';
			li.innerHTML = t;
			ul.appendChild(li);
		});
	}

	function pintarCitacao(r) {
		el('aqm-c12-citacao').innerHTML =
			'<strong>Para citar esta resposta:</strong> aquário de ' + litros(r.V) + ' L; mídia biológica de '
			+ mL(r.piso.mL) + ' a ' + mL(r.teto.mL) + ' segundo as dosagens declaradas por '
			+ esc(r.piso.ancora.marca) + ' (' + fmt(r.piso.ancora.mlL, 2) + ' mL/L) e '
			+ esc(r.teto.ancora.marca) + ' (' + fmt(r.teto.ancora.mlL, 2) + ' mL/L). '
			+ 'Aquametria, calculadora de mídia filtrante, verificada em ' + AQM_C12_DATA + '.';
	}

	/* ------------------------------------------------- bloco de produto */

	/* O bloco nasce DENTRO da resposta: são as mídias que atendem à faixa que
	   a sua água pede, cada uma medida pela dosagem que ela mesma declara.
	   Mídia sem dosagem declarada não é dimensionada — sai numa lista à parte,
	   dizendo que o fabricante não publica o número. */
	function pintarProdutos(r) {
		var bloco = el('aqm-c12-produtos');
		var lista = el('aqm-c12-produtos-lista');
		var nada = el('aqm-c12-produtos-nada');
		lista.innerHTML = '';

		var comDose = [];
		var semDose = [];
		AQM_C12_MIDIAS.forEach(function (m) {
			if (m.tipo !== 'biologica') { return; }
			if (m.dose_mL_por_L === null) { semDose.push(m); } else { comDose.push(m); }
		});

		if (!comDose.length && !semDose.length) {
			bloco.classList.add('aqm-c12-oculto');
			nada.classList.remove('aqm-c12-oculto');
			nada.textContent = 'O nosso banco ainda não tem mídia biológica com ficha suficiente para sugerir. '
				+ 'Preferimos não mostrar produto nenhum a mostrar um que não sabemos dimensionar.';
			return;
		}

		nada.classList.add('aqm-c12-oculto');
		bloco.classList.remove('aqm-c12-oculto');
		el('aqm-c12-produtos-sub').innerHTML =
			'São as mídias biológicas do nosso banco, cada uma medida pela <strong>dosagem que ela mesma declara</strong> — '
			+ 'e é por isso que a quantidade muda de marca para marca na mesma coluna de água. '
			+ 'A ordem é da dosagem declarada mais econômica para a mais generosa, que é a única ordem que as próprias '
			+ 'declarações sustentam; não é ranking de qualidade e não é ordem de comissão. '
			+ 'Mídia sem link de loja aparece na mesma lista, no mesmo lugar.';

		comDose.forEach(function (m) { lista.appendChild(produtoHtml(m, r, true)); });
		semDose.forEach(function (m) { lista.appendChild(produtoHtml(m, r, false)); });

		if (r.entradas.quimica) {
			AQM_C12_MIDIAS.forEach(function (m) {
				if (m.tipo === 'quimica') { lista.appendChild(produtoHtml(m, r, m.dose_mL_por_L !== null)); }
			});
		}
	}

	function produtoHtml(m, r, dimensionavel) {
		var li = document.createElement('li');
		li.className = 'aqm-c12-produto' + (dimensionavel ? '' : ' aqm-c12-produto-sem');

		var precisa = dimensionavel ? m.dose_mL_por_L * r.V : null;
		var embalagens = (dimensionavel && m.embalagem_L)
			? Math.ceil(precisa / (m.embalagem_L * 1000)) : null;

		var placa = document.createElement('div');
		placa.className = 'aqm-c12-placa';
		placa.innerHTML = '<span class="aqm-c12-marca">' + esc(m.marca) + '</span>'
			+ '<span class="aqm-c12-numero">' + (dimensionavel ? mL(precisa) : '—') + '</span>'
			+ '<span class="aqm-c12-un">' + (dimensionavel ? 'no seu aquário' : 'sem dosagem') + '</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = m.marca + ' ' + m.modelo;
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c12-porque';
		if (dimensionavel) {
			porque.innerHTML = 'O fabricante declara <strong>' + esc(m.dose_texto) + '</strong>, ou seja '
				+ fmt(m.dose_mL_por_L, 2) + ' mL por litro de água. '
				+ 'Nos seus ' + litros(r.V) + ' L isso dá <strong>' + mL(precisa) + '</strong>'
				+ (embalagens ? ', que são <strong>' + embalagens + ' embalagem(ns)</strong> de ' + fmt(m.embalagem_L, 2) + ' L' : '')
				+ '.'
				+ (m.dose_alt_mL_por_L
					? ' A mesma comunicação do fabricante tem uma segunda leitura, ' + fmt(m.dose_alt_mL_por_L, 2)
						+ ' mL/L (' + esc(m.dose_alt_texto) + '), que daria ' + mL(m.dose_alt_mL_por_L * r.V)
						+ '. Publicamos as duas porque quem discorda aqui é o fabricante consigo mesmo.'
					: '')
				+ (r.midiaL
					? ' Ocuparia ' + pct(precisa / (r.midiaL * 1000) * 100) + ' do volume de mídia do filtro que você escolheu.'
					: '');
		} else {
			porque.innerHTML = '<strong>Este fabricante não publica dosagem por litro de água.</strong> '
				+ 'A ficha traz área de superfície e material, mas não diz quanta mídia o seu aquário precisa — '
				+ 'então esta página não dimensiona a compra por ela. Fica na lista porque a ficha vale como informação, '
				+ 'e porque o silêncio dela é parte do assunto.';
		}
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c12-ficha';
		var linhas = [];
		linhas.push('Tipo: <b>' + esc(m.tipo) + '</b>, material <b>' + esc(m.material) + '</b>');
		if (m.embalagem_L) {
			linhas.push('Embalagem: <b>' + fmt(m.embalagem_L, 2) + ' L</b>'
				+ (m.peso_g ? ' (<b>' + fmt(m.peso_g, 0) + ' g</b>, o que fixa a densidade aparente em '
					+ fmt(Math.round(m.peso_g / m.embalagem_L), 0) + ' g/L)' : ''));
		}
		if (m.area_m2_L) {
			linhas.push('Área declarada: <b>' + fmt(m.area_m2_L, 0) + ' m²/L</b> <span class="aqm-c12-selo">não compara marcas</span> '
				+ 'nenhum fabricante publica o método de medição');
		}
		if (m.volume_max_L) {
			linhas.push('Uma embalagem atende, pela declaração do fabricante: <b>até ' + litros(m.volume_max_L) + ' L</b> de aquário');
		}
		if (m.granulometria_mm) { linhas.push('Granulometria: <b>' + fmt(m.granulometria_mm, 0) + ' mm</b>'); }
		if (m.regeneravel === true) { linhas.push('Regenerável: <b>sim</b>, pelo procedimento que vem na embalagem'); }
		if (m.regeneravel === false) { linhas.push('Regenerável: <b>não</b>'); }
		if (m.vida_util_meses) { linhas.push('Validade declarada: <b>' + m.vida_util_meses + ' meses</b>'); }
		linhas.push('Ficha conferida em ' + esc(dataBr(m.verificado_em))
			+ (m.fonte_url ? ' — <a href="' + esc(m.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (m.fonte_status ? ' (' + esc(m.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (m.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c12-loja';
			a.href = m.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (m.loja === 'shopee' ? 'Shopee' : m.loja);
			corpo.appendChild(a);
			var patro = document.createElement('p');
			patro.className = 'aqm-c12-semloja';
			patro.textContent = 'Link patrocinado. Confira o volume da embalagem no anúncio: a mesma mídia é vendida '
				+ 'em vários tamanhos e a granel, e o nosso número é por litro. O anúncio não é a nossa fonte técnica; a ficha acima é.';
			corpo.appendChild(patro);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c12-semloja';
			sem.textContent = 'Ainda não temos link de loja para esta mídia. Ela aparece aqui porque a ficha atende ao seu caso, '
				+ 'e é só isso que decide a lista.';
			corpo.appendChild(sem);
		}

		li.appendChild(placa);
		li.appendChild(corpo);
		return li;
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

	/* Mescla: a C1 é dona das medidas e dos volumes, a C3 do perfil e a C5 do
	   clima. Esta calculadora só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c12-midia-filtrante' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.V) {
			estado.volumes.real_L = r.V;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C12'; }
		}
		estado.perfil = estado.perfil || {};
		if (r.entradas.perfil === 'plantado' || r.entradas.perfil === 'comunitario') {
			estado.perfil.tipo_aquario = r.entradas.perfil;
			estado.perfil.especies_sensiveis = false;
		} else if (r.entradas.perfil === 'sensiveis') {
			estado.perfil.especies_sensiveis = true;
		}
		estado.equipamentos = estado.equipamentos || {};
		estado.equipamentos.filtro_id = r.filtro ? r.filtro.id : null;
		estado.equipamentos.filtro_midia_L = r.midiaL;
		estado.midia = estado.midia || {};
		estado.midia.biologica_mL = (r.piso && r.teto)
			? [Math.round(r.piso.mL), Math.round(r.teto.mL)]
			: null;
		estado.midia.usa_quimica = !!r.entradas.quimica;
		estado.manutencao = estado.manutencao || {};
		estado.manutencao.ultima = r.entradas.data || null;
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c12-guardado').classList.remove('aqm-c12-oculto');
		} catch (erro) {
			el('aqm-c12-guardado').classList.add('aqm-c12-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'p=' + d.perfil];
		if (d.filtro) { q.push('f=' + encodeURIComponent(d.filtro)); }
		if (d.midiaManual !== null) { q.push('m=' + d.midiaManual); }
		if (d.quimica) { q.push('q=1'); }
		if (d.data) { q.push('dt=' + d.data); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c12-link').value = window.location.origin + url;
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

	/* ------------------------------------ o caminho inverso: eu tenho mídia */

	function veredito() {
		var litrosMidia = num(el('aqm-c12-tenho').value);
		var saida = el('aqm-c12-tenho-saida');

		if (litrosMidia === null || litrosMidia <= 0) {
			saida.textContent = 'Informe quantos litros de mídia biológica você já tem — o volume da embalagem, não o peso.';
			return;
		}

		var ancoras = ancorasBio();
		if (!ancoras.length) {
			saida.textContent = 'O banco não tem hoje nenhuma dosagem declarada para fazer esta conta.';
			return;
		}

		var partes = ancoras.map(function (a) {
			return 'até ' + litros(litrosMidia * 1000 / a.mlL) + ' L pela dosagem da ' + a.marca
				+ ' (' + fmt(a.mlL, 2) + ' mL/L' + (a.leitura ? ', segunda leitura' : '') + ')';
		});

		saida.innerHTML = fmt(litrosMidia, 2) + ' L de mídia biológica cobrem ' + partes.join('; ') + '. '
			+ 'A distância entre o primeiro e o último número desta frase é o assunto inteiro desta página: '
			+ 'a mesma mídia, medida pelas declarações de fabricantes diferentes, atende de '
			+ litros(litrosMidia * 1000 / ancoras[ancoras.length - 1].mlL) + ' a '
			+ litros(litrosMidia * 1000 / ancoras[0].mlL) + ' L de água.';
	}

	/* ---------------------------------------------------------- ligações */

	function mostrarManual() {
		var manual = el('aqm-c12-midia-manual-campo');
		if (el('aqm-c12-filtro').value === 'outro') {
			manual.classList.remove('aqm-c12-oculto');
		} else {
			manual.classList.add('aqm-c12-oculto');
		}
	}

	function preencher(fora) {
		if (fora.v) { el('aqm-c12-volume').value = fora.v; }
		if (fora.f) { el('aqm-c12-filtro').value = fora.f; }
		if (fora.m) { el('aqm-c12-midia-manual').value = fora.m; }
		if (fora.p === 'plantado' || fora.p === 'comunitario' || fora.p === 'sensiveis') {
			el('aqm-c12-perfil').value = fora.p;
		}
		if (fora.q === '1') { el('aqm-c12-quimica').checked = true; }
		if (fora.dt) { el('aqm-c12-data').value = fora.dt; }
		mostrarManual();
	}

	el('aqm-c12-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
	});

	el('aqm-c12-filtro').addEventListener('change', mostrarManual);

	el('aqm-c12-limpar').addEventListener('click', function () {
		el('aqm-c12-form').reset();
		el('aqm-c12-saida').classList.add('aqm-c12-oculto');
		el('aqm-c12-erros').innerHTML = '';
		mostrarManual();
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c12-copiar').addEventListener('click', function () {
		var campo = el('aqm-c12-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c12-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c12-tenho-calcular').addEventListener('click', veredito);

	mostrarManual();

	/* Query string manda; senão, o aquário que as outras calculadoras
	   guardaram neste navegador. Aqui o volume basta para calcular. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		pintar(calcular(campos()));
	} else {
		var antes = recuperar();
		var volume = antes && antes.volumes ? antes.volumes.real_L : null;
		if (volume) {
			el('aqm-c12-volume').value = String(volume).replace('.', ',');
			var perfil = (antes.perfil || {}).tipo_aquario;
			if (perfil === 'plantado' || perfil === 'comunitario') { el('aqm-c12-perfil').value = perfil; }
			if ((antes.perfil || {}).especies_sensiveis) { el('aqm-c12-perfil').value = 'sensiveis'; }
			var filtroId = (antes.equipamentos || {}).filtro_id;
			if (filtroId && filtroPorId(filtroId)) { el('aqm-c12-filtro').value = filtroId; }
			var ultima = (antes.manutencao || {}).ultima;
			if (ultima) { el('aqm-c12-data').value = ultima; }
			mostrarManual();
			var retomado = el('aqm-c12-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que as outras calculadoras guardaram neste navegador.';
			retomado.classList.remove('aqm-c12-oculto');
			pintar(calcular(campos()));
		} else {
			el('aqm-c12-semvolume').classList.remove('aqm-c12-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_url' ) ) {
function aquametria_c12_url( $slug ) {
	return function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( $slug )
		: home_url( '/' . $slug . '/' );
}
}

if ( ! function_exists( 'aquametria_c12_opcoes_filtro' ) ) {
function aquametria_c12_opcoes_filtro() {
	$h = '<option value="">— não sei / ainda não escolhi —</option>';
	foreach ( aquametria_c12_catalogo_filtros() as $f ) {
		$rotulo = $f['marca'] . ' ' . $f['modelo'] . ' (' . str_replace( '.', ',', (string) $f['midia_L'] ) . ' L de mídia';
		if ( ! empty( $f['midia_L_alt'] ) ) {
			$rotulo .= ' ou ' . str_replace( '.', ',', (string) $f['midia_L_alt'] ) . ' L';
		}
		$rotulo .= ')';
		$h .= '<option value="' . esc_attr( $f['id'] ) . '">' . esc_html( $rotulo ) . '</option>';
	}
	$h .= '<option value="outro">outro filtro — vou digitar o volume de mídia</option>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_form_html' ) ) {
function aquametria_c12_form_html() {
	$c1 = aquametria_c12_url( 'calculadora-de-litragem' );

	$h  = '<form id="aqm-c12-form" class="aqm-c12-painel" novalidate>';
	$h .= '<h3>O seu aquário e o seu filtro</h3>';
	$h .= '<p class="aqm-c12-sub">A pergunta que ninguém responde no Brasil não é qual mídia comprar — é <em>quanta</em>. ';
	$h .= 'Se você já usou as outras calculadoras neste navegador, o volume vem preenchido daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c12-grade">';

	$h .= '<div class="aqm-c12-campo">';
	$h .= '<label for="aqm-c12-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c12-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c12-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c12-campo">';
	$h .= '<label for="aqm-c12-filtro">Filtro</label>';
	$h .= '<select id="aqm-c12-filtro" name="filtro">' . aquametria_c12_opcoes_filtro() . '</select>';
	$h .= '<span class="aqm-c12-dica">Traz do nosso banco o volume útil de mídia declarado. É ele que diz se a dosagem cabe.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c12-campo aqm-c12-oculto" id="aqm-c12-midia-manual-campo">';
	$h .= '<label for="aqm-c12-midia-manual">Volume de mídia do filtro (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c12-midia-manual" name="midia" placeholder="3,0">';
	$h .= '<span class="aqm-c12-dica">Meça o cesto: comprimento × largura × altura em centímetros, dividido por mil, dá litros.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c12-campo">';
	$h .= '<label for="aqm-c12-perfil">Perfil do aquário</label>';
	$h .= '<select id="aqm-c12-perfil" name="perfil">';
	$h .= '<option value="comunitario" selected>comunitário</option>';
	$h .= '<option value="plantado">plantado</option>';
	$h .= '<option value="sensiveis">espécies sensíveis</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c12-dica">Muda o alvo de nitrato citado na manutenção. Não muda o volume de mídia: nenhuma fonte do nosso corpus liga uma coisa à outra.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c12-campo">';
	$h .= '<label for="aqm-c12-data">Data da última manutenção</label>';
	$h .= '<input type="date" id="aqm-c12-data" name="data">';
	$h .= '<span class="aqm-c12-dica">Em branco, o calendário de trocas sai sem datas. Preenchida, vira agenda.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c12-caixa"><input type="checkbox" id="aqm-c12-quimica"> <span>Uso (ou quero usar) mídia química — carvão ativado, resina de polimento</span></label>';

	$h .= '<div class="aqm-c12-botoes">';
	$h .= '<button type="submit">Calcular a mídia</button>';
	$h .= '<button type="button" class="aqm-c12-secundario" id="aqm-c12-limpar">Limpar</button>';
	$h .= '<span class="aqm-c12-dica aqm-c12-oculto" id="aqm-c12-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c12-avisos" id="aqm-c12-erros"></ul>';
	$h .= '<p class="aqm-c12-criterio aqm-c12-oculto" id="aqm-c12-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre, o substrato e as rochas tiram uma parte, e a mídia é dimensionada sobre a água que existe. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_resposta_html' ) ) {
function aquametria_c12_resposta_html() {
	$h  = '<div class="aqm-c12-resultado aqm-c12-oculto" id="aqm-c12-saida" aria-live="polite">';

	$h .= '<div class="aqm-c12-faixa">';
	$h .= '<span class="aqm-c12-rotulo">Mídia biológica que o seu aquário pede</span>';
	$h .= '<span class="aqm-c12-valor" id="aqm-c12-faixa-valor">—</span>';
	$h .= '<p class="aqm-c12-criterio" id="aqm-c12-faixa-criterio"></p>';
	$h .= '<div class="aqm-c12-delta" id="aqm-c12-delta"></div>';
	$h .= '</div>';

	/* Tabela 1: quem vende mídia. */
	$h .= '<div class="aqm-c12-painel">';
	$h .= '<h3>As dosagens que os fabricantes de mídia declaram</h3>';
	$h .= '<p class="aqm-c12-sub">Cada linha é a declaração de um fabricante, não uma média nossa. ';
	$h .= 'A distância entre a primeira e a última é o motivo de esta página existir.</p>';
	$h .= '<div class="aqm-c12-rolagem"><table class="aqm-c12-tabela">';
	$h .= '<tr><th>Marca</th><th>Dosagem declarada</th><th>No seu aquário</th><th>O que a fonte diz, exatamente</th></tr>';
	$h .= '<tbody id="aqm-c12-ancoras-corpo"></tbody>';
	$h .= '</table></div>';

	/* Tabela 2: quem vende filtro. */
	$h .= '<div id="aqm-c12-totais">';
	$h .= '<h4>E as contas de quem vende filtro</h4>';
	$h .= '<p class="aqm-c12-sub" style="margin-bottom:.4rem">O fabricante do filtro declara duas coisas: quanto de mídia cabe lá dentro e para que aquário o aparelho serve. ';
	$h .= 'Dividir uma pela outra dá mídia <strong>total</strong> por litro de água — todas as camadas, não só a biológica. ';
	$h .= 'Por isso estes números são naturalmente maiores que os de cima, e por isso não se comparam de igual para igual com eles. ';
	$h .= 'O divisor é sempre o maior volume que o fabricante declara atender, que é a leitura menos favorável a ele.</p>';
	$h .= '<div class="aqm-c12-rolagem"><table class="aqm-c12-tabela">';
	$h .= '<tr><th>Marca</th><th>Mídia total por litro</th><th>No seu aquário</th><th>De onde sai a divisão</th></tr>';
	$h .= '<tbody id="aqm-c12-totais-corpo"></tbody>';
	$h .= '</table></div>';
	$h .= '</div>';
	$h .= '</div>';

	/* O teto físico. */
	$h .= '<p class="aqm-c12-nota aqm-c12-oculto" id="aqm-c12-cesto-sem"></p>';
	$h .= '<div class="aqm-c12-painel aqm-c12-oculto" id="aqm-c12-cesto">';
	$h .= '<h3>Cabe no seu filtro?</h3>';
	$h .= '<p class="aqm-c12-sub" id="aqm-c12-cesto-sub"></p>';
	$h .= '<ul class="aqm-c12-cartoes" id="aqm-c12-cesto-lista"></ul>';
	$h .= '<p class="aqm-c12-criterio">Este é o número que decide a compra e que nenhuma fonte brasileira publica: ';
	$h .= 'a dosagem só vale se a mídia couber. Quando a camada biológica sozinha já estoura o cesto, o problema não é a mídia — é o filtro.</p>';
	$h .= '</div>';

	/* Camadas e ordem. */
	$h .= '<div class="aqm-c12-painel">';
	$h .= '<h3>A ordem das camadas, do fluxo de entrada ao de saída</h3>';
	$h .= '<p class="aqm-c12-sub">Fonte: AquaPeixes, do levantamento de 04/09/2026. ';
	$h .= 'Vale como sequência típica de canister e <strong>não substitui o manual do seu modelo</strong>: cada fabricante especifica a sua, e o cesto de fábrica costuma vir com a ordem impressa na tampa.</p>';
	$h .= '<ul class="aqm-c12-ordem" id="aqm-c12-ordem"></ul>';
	$h .= '<p class="aqm-c12-criterio" style="margin-top:.8rem"><strong>O que esta página não publica:</strong> quanto do cesto é mecânica, quanto é biológica e quanto é química. ';
	$h .= 'Nenhuma fonte do nosso corpus reparte o volume em porcentagens, e repartir por conta própria seria inventar exatamente o tipo de número que este site existe para não publicar. ';
	$h .= 'A ordem tem fonte; a proporção, não.</p>';
	$h .= '</div>';

	/* Química, só quando pedida. */
	$h .= '<div class="aqm-c12-painel aqm-c12-oculto" id="aqm-c12-quimica-bloco">';
	$h .= '<h3>A camada química, em duas unidades que não conversam</h3>';
	$h .= '<p class="aqm-c12-sub">A regra brasileira mede carvão em gramas por litro de água. O fabricante mede em mililitros de mídia por litro de água. ';
	$h .= 'São duas grandezas diferentes, e <strong>esta página não converte uma na outra</strong>: faltaria a densidade aparente do carvão com fonte, e sem ela a conversão seria uma constante inventada. ';
	$h .= 'As duas saem lado a lado, cada uma na sua unidade e com o nome de quem a publica.</p>';
	$h .= '<p class="aqm-c12-criterio" id="aqm-c12-carvao-br"></p>';
	$h .= '<ul style="list-style:none;margin:.8rem 0 0;padding:0;display:grid;gap:.5rem" id="aqm-c12-quimica-lista"></ul>';
	$h .= '<p class="aqm-c12-criterio" style="margin-top:.8rem">Repare na distância entre as duas linhas. A regra repetida na web brasileira pede muito mais carvão, e trocado muito mais vezes, ';
	$h .= 'do que o fabricante do carvão pede. Nenhum dos dois lados publica o método que sustenta o próprio número.</p>';
	$h .= '</div>';

	/* Manutenção e o aviso obrigatório. */
	$h .= '<div class="aqm-c12-painel">';
	$h .= '<h3>Quando trocar cada camada</h3>';
	$h .= '<p class="aqm-c12-sub" id="aqm-c12-calendario-sub"></p>';
	$h .= '<div class="aqm-c12-rolagem"><table class="aqm-c12-tabela">';
	$h .= '<tr><th>Constante</th><th>Camada</th><th>Frequência publicada</th><th>Próxima, no seu caso</th></tr>';
	$h .= '<tbody id="aqm-c12-calendario-corpo"></tbody>';
	$h .= '</table></div>';

	$h .= '<h4>Troca parcial de água</h4>';
	$h .= '<p class="aqm-c12-criterio" id="aqm-c12-tpa-texto"></p>';
	$h .= '<p class="aqm-c12-criterio" style="margin-top:.5rem">Gatilhos de nitrato do corpus: acima de <b>40 ppm</b> a troca é urgente; ';
	$h .= 'o teto para espécies sensíveis é <b>20 ppm</b> (Aquário Vivo); em plantado o alvo publicado é de <b>5 a 10 ppm</b> (aquariosplantados). ';
	$h .= 'Três fontes, três números, e nenhuma delas mede o seu aquário — quem mede é o teste de nitrato.</p>';

	$h .= '<p class="aqm-c12-nota aqm-c12-nota-alerta" style="margin-top:1rem"><strong>Nunca lave toda a mídia biológica de uma vez, e nunca em água de torneira.</strong> ';
	$h .= 'O que faz a filtragem biológica funcionar não é a pedra: é a colônia de bactérias nitrificantes que mora nos poros dela, e que leva semanas para se estabelecer. ';
	$h .= 'A água tratada da rede leva cloro ou cloramina justamente para matar bactéria — é para isso que ela existe. ';
	$h .= 'Lavar a mídia inteira na torneira mata a colônia de uma vez, e o aquário volta ao começo do ciclo, com pico de amônia e de nitrito na água onde os peixes estão vivendo. ';
	$h .= 'Por isso a substituição da cerâmica é <strong>parcial</strong>: troca-se uma parte, a colônia da parte que ficou recoloniza a nova. ';
	$h .= 'Quando precisar tirar a sujeira grossa, use a água que saiu do próprio aquário na troca parcial, que já não tem cloro e está na mesma temperatura.</p>';
	$h .= '</div>';

	/* Critérios editoriais. */
	$h .= '<div class="aqm-c12-painel"><h3>O que aqui é critério nosso, e não fonte de terceiro</h3>';
	$h .= '<p class="aqm-c12-sub" style="margin-bottom:.4rem">Constante tem origem e data; escolha editorial tem nome e fica declarada. Estas são as desta resposta.</p>';
	$h .= '<ul id="aqm-c12-editoriais" style="list-style:none;margin:0;padding:0"></ul></div>';

	$h .= aquametria_c12_produtos_html();

	$h .= '<div class="aqm-c12-citar">';
	$h .= '<p id="aqm-c12-citacao"></p>';
	$h .= '<div class="aqm-c12-campo"><label for="aqm-c12-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c12-link" readonly></div>';
	$h .= '<div class="aqm-c12-botoes"><button type="button" class="aqm-c12-secundario" id="aqm-c12-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c12-dica" id="aqm-c12-copiado"></span></div>';
	$h .= '<p class="aqm-c12-dica" id="aqm-c12-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_produtos_html' ) ) {
function aquametria_c12_produtos_html() {
	$divulgacao = aquametria_c12_url( AQUAMETRIA_C12_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c12-produtos aqm-c12-painel aqm-c12-oculto" id="aqm-c12-produtos">';
	$h .= '<h3>As mídias do nosso banco, medidas pela dosagem de cada fabricante</h3>';
	$h .= '<p class="aqm-c12-sub" id="aqm-c12-produtos-sub"></p>';
	$h .= '<ul class="aqm-c12-lista" id="aqm-c12-produtos-lista"></ul>';
	$h .= '<p class="aqm-c12-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista nem em que ordem — a ordem é a da dosagem declarada, da mais econômica para a mais generosa, e mídia sem link aparece do mesmo jeito e no mesmo lugar. ';
	$h .= 'A quantidade que aparece em cada cartão é calculada com a dosagem que <em>aquele</em> fabricante publica, e não com um número escolhido por nós. ';
	$h .= 'A ficha técnica de cada mídia vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'Também não publicamos preço nesta página: preço muda toda semana e um número velho na tela seria pior que nenhum. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c12-nota aqm-c12-oculto" id="aqm-c12-produtos-nada"></p>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_tenho_html' ) ) {
function aquametria_c12_tenho_html() {
	$h  = '<div class="aqm-c12-painel">';
	$h .= '<h3>Caminho inverso: a mídia que eu já tenho dá para quanto aquário?</h3>';
	$h .= '<p class="aqm-c12-sub">Informe quantos litros de mídia biológica você já tem e devolvemos, por cada dosagem declarada, até que volume de água ela cobre.</p>';
	$h .= '<div class="aqm-c12-grade">';
	$h .= '<div class="aqm-c12-campo"><label for="aqm-c12-tenho">Mídia biológica que eu tenho (L)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c12-tenho" placeholder="1,0"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c12-botoes"><button type="button" id="aqm-c12-tenho-calcular">Ver o que ela cobre</button></div>';
	$h .= '<p class="aqm-c12-criterio" id="aqm-c12-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_fontes_html' ) ) {
function aquametria_c12_fontes_html() {
	$artigo = aquametria_c12_url( AQUAMETRIA_C12_ARTIGO );

	$h  = '<div class="aqm-c12-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c12-sub">Verificado em ' . esc_html( AQUAMETRIA_C12_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C12_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c12-rolagem"><table class="aqm-c12-tabela">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>seachem-matrix-dosagem</td><td>1,25 e 2,64 mL/L</td>';
	$h .= '<td>Seachem, página do Matrix <span class="aqm-c12-selo">fabricante via busca</span>. ';
	$h .= 'Duas leituras da <strong>mesma</strong> comunicação do fabricante: "250 mL para 200 L" e "1 L para 100 galões". ';
	$h .= 'Discordam por 2,1 vezes. A página do fabricante não pôde ser lida direto (o servidor da nuvem não alcança seachem.com) e os números vieram por resultado de busca, ';
	$h .= 'reconfirmados no varejo brasileiro que replica a mesma ficha. <strong>Confira na embalagem.</strong></td></tr>';

	$h .= '<tr><td>jbl-micromec-dosagem</td><td>5,00 mL/L</td>';
	$h .= '<td>JBL, ficha do MicroMec <span class="aqm-c12-selo">fabricante via busca</span>. ';
	$h .= '650 g indicados para aquário de 200 L, e a mesma embalagem é vendida como 1 L — o que fixa a densidade aparente em 650 g/L e permite ler a dosagem em volume. ';
	$h .= 'Coletada em 08/09/2026 para esta calculadora. É a âncora que faltava para a comparação deixar de ser um duelo entre duas marcas.</td></tr>';

	$h .= '<tr><td>ocean-tech-bio-glass-dosagem</td><td>12,50 mL/L</td>';
	$h .= '<td>Ocean Tech, ficha do Bio Glass replicada por pelo menos quatro lojas brasileiras <span class="aqm-c12-selo">fabricante via busca</span>. ';
	$h .= '"1 litro para cada 80 litros de água". É a <strong>única dosagem de mídia biológica por litro publicada por uma marca brasileira</strong> que o nosso levantamento encontrou — ';
	$h .= 'e é dez vezes a leitura mais econômica da Seachem, para a mesma função. Coletada em 08/09/2026.</td></tr>';

	$h .= '<tr><td>eheim-classic-250-2213</td><td>12,0 mL/L (mídia total)</td>';
	$h .= '<td>Eheim classic 250, especificação replicada pelo varejo <span class="aqm-c12-selo">fabricante via busca</span>. ';
	$h .= '3,0 L de volume de filtragem para até 250 L de aquário. É mídia <strong>total</strong>, com mecânica e química dentro, e por isso não se compara de igual para igual com as dosagens de cima.</td></tr>';

	$h .= '<tr><td>carvao-ativado</td><td>1 a 2 g/L, troca em 15 a 30 dias</td>';
	$h .= '<td>Aquarismo Paulista, do levantamento de 04/09/2026 <span class="aqm-c12-selo">divergente entre fontes BR</span>. ';
	$h .= 'Convive nesta página com a declaração do fabricante de carvão (Seachem MatrixCarbon: 250 mL para 400 L, durando "vários meses"), que é uma ordem de grandeza mais econômica. ';
	$h .= 'As duas ficam publicadas nas suas próprias unidades porque converter grama em mililitro exigiria uma densidade que não temos com fonte.</td></tr>';

	$h .= '<tr><td>perlon-troca</td><td>semanal a quinzenal</td>';
	$h .= '<td>Aquarismo Paulista <span class="aqm-c12-selo">divergente entre fontes BR</span>. O perlon é a camada que se descarta sem dó: ele segura partícula, não colônia.</td></tr>';

	$h .= '<tr><td>ceramica-regeneracao</td><td>parcial, a cada 6 a 12 meses</td>';
	$h .= '<td>Aquarismo Paulista <span class="aqm-c12-selo">divergente entre fontes BR</span>. A palavra que importa é <strong>parcial</strong>: trocar tudo de uma vez é reiniciar o ciclo do aquário.</td></tr>';

	$h .= '<tr><td>ordem-midias-canister</td><td>cerâmica → perlon → carvão → perlon → cerâmica → perlon</td>';
	$h .= '<td>AquaPeixes <span class="aqm-c12-selo">divergente entre fontes BR</span>. Sequência típica, não norma. O manual do seu modelo manda mais que esta linha.</td></tr>';

	$h .= '<tr><td>tpa-percentual</td><td>10 a 30 % · 25 a 30 % semanal · teto de 50 %</td>';
	$h .= '<td>Escola de Aquário e Aquário Vivo <span class="aqm-c12-selo">divergente entre fontes BR</span>. Três recortes que a web brasileira publica sem se falarem.</td></tr>';

	$h .= '<tr><td>nitrato-limites</td><td>&gt; 40 ppm urgente · ≤ 20 ppm sensíveis · 5 a 10 ppm plantado</td>';
	$h .= '<td>Corpus do Bloco 1 <span class="aqm-c12-selo">divergente entre fontes BR</span>. São gatilhos de manutenção, não metas de dimensionamento de mídia.</td></tr>';

	$h .= '<tr><td>tpa-diferenca-termica</td><td>até 1 °C tolerado; acima de 2 °C, choque</td>';
	$h .= '<td>Corpus do Bloco 1 <span class="aqm-c12-selo">divergente entre fontes BR</span>.</td></tr>';

	$h .= '<tr><td>proporcao-entre-camadas</td><td>sem valor <span class="aqm-c12-selo">não publicamos</span></td>';
	$h .= '<td>Quanto do cesto é mecânica, quanto é biológica, quanto é química. Nenhuma fonte do corpus declara, e não inventamos. ';
	$h .= 'É a próxima coleta óbvia desta calculadora: manual de canister costuma trazer o esquema de carga por cesto, e é de lá que o número deve sair.</td></tr>';

	$h .= '<tr><td>densidade-aparente-carvao</td><td>sem valor <span class="aqm-c12-selo">pendente</span></td>';
	$h .= '<td>Sem ela, a regra brasileira em gramas e a declaração do fabricante em mililitros não se comparam. É o que impede esta página de dizer qual das duas pede mais carvão.</td></tr>';

	$h .= '</table></div>';
	$h .= '<p class="aqm-c12-criterio" style="margin-top:.8rem">A discussão longa de por que esses fabricantes discordam por dez vezes, e do que acontece quando se segue cada um deles, está em ';
	$h .= '<a href="' . esc_url( $artigo ) . '">quanta mídia biológica o aquário realmente precisa</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c12_adiante_html' ) ) {
function aquametria_c12_adiante_html() {
	$hub    = aquametria_c12_url( 'calculadoras' );
	$meto   = aquametria_c12_url( 'metodologia' );
	$c1     = aquametria_c12_url( 'calculadora-de-litragem' );
	$c3     = aquametria_c12_url( 'calculadora-de-vazao-do-filtro' );
	$c5     = aquametria_c12_url( 'calculadora-de-potencia-do-aquecedor' );
	$c15    = aquametria_c12_url( 'calculadora-de-iluminacao' );
	$artigo = aquametria_c12_url( AQUAMETRIA_C12_ARTIGO );
	$divul  = aquametria_c12_url( AQUAMETRIA_C12_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c12-painel aqm-c12-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $artigo ) . '"><strong>Quanta mídia biológica o aquário realmente precisa</strong></a> — o texto que mostra de onde vêm as dosagens, por que elas discordam por dez vezes e o que muda quando se segue cada uma.</li>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vem o volume real que esta página usa. Se o número acima veio preenchido, veio de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c3 ) . '"><strong>Vazão do filtro (C3)</strong></a> — o filtro que você escolheu aqui é o mesmo que vira renovações por hora lá. Vazão e mídia são as duas metades da mesma decisão: a água precisa passar, e precisa passar por alguma coisa.</li>';
	$h .= '<li><a href="' . esc_url( $c5 ) . '"><strong>Potência do aquecedor (C5)</strong></a> — usa o mesmo volume de água. A colônia nitrificante também depende de temperatura: aquário frio cicla mais devagar.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — luz forte com CO2 acelera o crescimento das plantas e a carga do filtro junto: mais matéria orgânica para a mídia processar. É a mesma decisão vista pelo outro lado.</li>';
	$h .= '<li><strong>Lotação e aquário mínimo (C8)</strong> — quantos peixes o volume comporta, que é o que gera a amônia que a mídia biológica processa. Ainda em construção.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c12-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 5b. VISIBILIDADE EM IA (seção 5 do ARQUIPELAGO.md) — as três peças
 *
 * Uma calculadora que só calcula em JavaScript mostra a um modelo de linguagem
 * um formulário VAZIO, nunca um número. As três peças que resolvem isso são a
 * resposta antes da explicação, a tabela de exemplos já resolvida no HTML
 * servido e o JSON-LD — e nenhuma delas pode contradizer a calculadora logo
 * acima dela. Por isso tudo aqui é ESPELHO em PHP das mesmas funções do script,
 * função a função, e o teste de navegador compara a tabela servida com o que a
 * calculadora devolve para a mesma entrada.
 * ------------------------------------------------------------------------- */

/* Espelho em PHP do fmt() do script. */
if ( ! function_exists( 'aquametria_c12_fmt' ) ) {
function aquametria_c12_fmt( $n, $casas ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return number_format_i18n( $n, $casas );
}
}

/* Espelho em PHP do litros() do script. */
if ( ! function_exists( 'aquametria_c12_litros' ) ) {
function aquametria_c12_litros( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return ( $n >= 100 ) ? aquametria_c12_fmt( round( $n ), 0 ) : aquametria_c12_fmt( round( $n * 10 ) / 10, 1 );
}
}

/* Espelho em PHP do mL() do script. Mililitro de mídia é número grosso: ninguém
   mede 137,5 mL com colher, e acima de 1 L a mídia se compra em litro. Se este
   arredondamento divergir do JavaScript, a tabela servida passa a afirmar um
   número e a calculadora outro na mesma página. */
if ( ! function_exists( 'aquametria_c12_ml' ) ) {
function aquametria_c12_ml( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	if ( $n >= 1000 ) {
		return aquametria_c12_fmt( round( $n / 25 ) * 25 / 1000, 2 ) . ' L';
	}
	return aquametria_c12_fmt( round( $n / 5 ) * 5, 0 ) . ' mL';
}
}

/* Espelho em PHP do pct() do script. */
if ( ! function_exists( 'aquametria_c12_pct' ) ) {
function aquametria_c12_pct( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return aquametria_c12_fmt( round( $n ), 0 ) . ' %';
}
}

/* Espelho em PHP do ancorasBio(). As âncoras NÃO são digitadas aqui: saem do
   catálogo embutido, que sai do banco. Mídia nova com dosagem declarada entra
   na tabela servida sozinha, no próximo gerador de catálogo. */
if ( ! function_exists( 'aquametria_c12_ancoras_bio' ) ) {
function aquametria_c12_ancoras_bio() {
	$out = array();
	foreach ( aquametria_c12_catalogo_midias() as $m ) {
		if ( 'biologica' !== $m['tipo'] || null === $m['dose_mL_por_L'] ) {
			continue;
		}
		$out[] = array(
			'id'          => $m['id'],
			'marca'       => $m['marca'],
			'modelo'      => $m['modelo'],
			'mlL'         => $m['dose_mL_por_L'],
			'texto'       => $m['dose_texto'],
			'leitura'     => null,
			'embalagem_L' => $m['embalagem_L'],
			'link'        => $m['link'],
			'verificado'  => $m['verificado_em'],
		);
		if ( null !== $m['dose_alt_mL_por_L'] ) {
			$out[] = array(
				'id'          => $m['id'] . '-alt',
				'marca'       => $m['marca'],
				'modelo'      => $m['modelo'],
				'mlL'         => $m['dose_alt_mL_por_L'],
				'texto'       => $m['dose_alt_texto'],
				'leitura'     => $m['dose_alt_ref'],
				'embalagem_L' => $m['embalagem_L'],
				'link'        => $m['link'],
				'verificado'  => $m['verificado_em'],
			);
		}
	}
	usort( $out, function ( $a, $b ) {
		if ( $a['mlL'] === $b['mlL'] ) {
			return 0;
		}
		return ( $a['mlL'] < $b['mlL'] ) ? -1 : 1;
	} );
	return $out;
}
}

/* Espelho em PHP do ancorasFiltro(). A segunda família: quem vende FILTRO
   declara quanto de mídia cabe nele e para que aquário ele serve. O divisor é o
   MAIOR volume declarado, que é a leitura menos favorável ao fabricante. */
if ( ! function_exists( 'aquametria_c12_ancoras_filtro' ) ) {
function aquametria_c12_ancoras_filtro() {
	$out = array();
	foreach ( aquametria_c12_catalogo_filtros() as $f ) {
		if ( ! $f['midia_L'] || ! $f['volume_max_L'] ) {
			continue;
		}
		$item = array(
			'id'           => $f['id'],
			'marca'        => $f['marca'],
			'modelo'       => $f['modelo'],
			'tipo'         => $f['tipo'],
			'mlL'          => round( $f['midia_L'] * 1000 / $f['volume_max_L'] * 100 ) / 100,
			'midia_L'      => $f['midia_L'],
			'volume_max_L' => $f['volume_max_L'],
			'alt_mlL'      => null,
			'alt_midia_L'  => null,
			'verificado'   => $f['verificado_em'],
		);
		if ( $f['midia_L_alt'] ) {
			$item['alt_midia_L'] = $f['midia_L_alt'];
			$item['alt_mlL']     = round( $f['midia_L_alt'] * 1000 / $f['volume_max_L'] * 100 ) / 100;
		}
		$out[] = $item;
	}
	usort( $out, function ( $a, $b ) {
		if ( $a['mlL'] === $b['mlL'] ) {
			return 0;
		}
		return ( $a['mlL'] < $b['mlL'] ) ? -1 : 1;
	} );
	return $out;
}
}

/* Os seis aquários da tabela servida. Mesma escada de 30 a 300 L da C3 e da C5,
   de propósito: é a escada que as três calculadoras respondem, e repetir a
   mesma faixa deixa as três páginas comparáveis entre si. */
if ( ! function_exists( 'aquametria_c12_casos_exemplo' ) ) {
function aquametria_c12_casos_exemplo() {
	return array( 30, 60, 100, 150, 200, 300 );
}
}

/* Resolve um volume, com as mesmas regras do calcular() do script. */
if ( ! function_exists( 'aquametria_c12_exemplo' ) ) {
function aquametria_c12_exemplo( $volume ) {
	$bio = array();
	foreach ( aquametria_c12_ancoras_bio() as $a ) {
		$bio[] = array( 'ancora' => $a, 'mL' => $a['mlL'] * $volume );
	}

	$totais = array();
	foreach ( aquametria_c12_ancoras_filtro() as $a ) {
		$totais[] = array(
			'ancora' => $a,
			'mL'     => $a['mlL'] * $volume,
			'mL_alt' => ( null === $a['alt_mlL'] ) ? null : $a['alt_mlL'] * $volume,
		);
	}

	$piso = $bio ? $bio[0] : null;
	$teto = $bio ? $bio[ count( $bio ) - 1 ] : null;

	/* A faixa da mídia TOTAL abre em todas as leituras publicadas, inclusive as
	   alternativas: a C12 publica as duas leituras das fichas ambíguas em vez de
	   desempatar, e esconder uma delas aqui contradiria a própria página. */
	$total_min = null;
	$total_max = null;
	foreach ( $totais as $t ) {
		foreach ( array( $t['mL'], $t['mL_alt'] ) as $v ) {
			if ( null === $v ) {
				continue;
			}
			$total_min = ( null === $total_min || $v < $total_min ) ? $v : $total_min;
			$total_max = ( null === $total_max || $v > $total_max ) ? $v : $total_max;
		}
	}

	/* O TETO FÍSICO, que é a saída que ninguém publica em português: escolhido um
	   filtro que o fabricante declara atender esse volume, quanto do cesto dele a
	   dosagem do teto ocuparia só com a camada biológica.

	   Qual filtro: entre os que DECLARAM cobrir o volume, o de menor volume
	   declarado — é o que a pessoa realmente compraria para aquele aquário, e é a
	   leitura mais apertada, que é onde o teto estoura. Elegibilidade declarada
	   primeiro, adequação depois: filtro que o fabricante não declara para o
	   volume não entra na célula nem em último lugar. */
	$filtro = null;
	foreach ( aquametria_c12_ancoras_filtro() as $f ) {
		if ( $f['volume_max_L'] < $volume ) {
			continue;
		}
		if ( null === $filtro || $f['volume_max_L'] < $filtro['volume_max_L'] ) {
			$filtro = $f;
		}
	}

	$ocupacao = null;
	if ( $filtro && $teto ) {
		$ocupacao = $teto['mL'] / ( $filtro['midia_L'] * 1000 ) * 100;
	}

	/* A mídia do banco para comprar: a primeira da ordem que a própria
	   calculadora usa — dosagem declarada, da mais econômica para a mais
	   generosa. Comissão não entra em nenhum degrau (V16); leitura alternativa da
	   mesma ficha não é produto, então só entra registro de verdade. */
	$compra = null;
	foreach ( $bio as $b ) {
		if ( substr( $b['ancora']['id'], -4 ) === '-alt' ) {
			continue;
		}
		$compra = $b;
		break;
	}

	return array(
		'V'         => $volume,
		'bio'       => $bio,
		'piso'      => $piso,
		'teto'      => $teto,
		'totais'    => $totais,
		'total_min' => $total_min,
		'total_max' => $total_max,
		'filtro'    => $filtro,
		'ocupacao'  => $ocupacao,
		'compra'    => $compra,
	);
}
}

/* O nome como a tela escreve: o banco é gravado sem acento de propósito, e a
   frase é montada aqui. */
if ( ! function_exists( 'aquametria_c12_ancora_nome' ) ) {
function aquametria_c12_ancora_nome( $a ) {
	return trim( ( $a['marca'] ? $a['marca'] . ' ' : '' ) . $a['modelo'] );
}
}

/* A célula do teto físico. Sem filtro que declare cobrir o volume, ela DIZ por
   quê: bloco vazio é portão (seção 7 do contrato), mas silêncio parece defeito. */
if ( ! function_exists( 'aquametria_c12_teto_celula_html' ) ) {
function aquametria_c12_teto_celula_html( $e ) {
	if ( null === $e['filtro'] || null === $e['ocupacao'] ) {
		return '<td><span class="aqm-c12-semloja">nenhum filtro do nosso banco declara atender '
			. esc_html( aquametria_c12_litros( $e['V'] ) ) . ' L, então não há cesto conhecido para medir — '
			. 'é faixa vazia do catálogo brasileiro, não erro da conta</span></td>';
	}
	$f      = $e['filtro'];
	$estoura = ( $e['ocupacao'] > 100 );

	$h  = '<td><span class="aqm-c12-num' . ( $estoura ? ' aqm-c12-estoura' : '' ) . '">';
	$h .= esc_html( aquametria_c12_pct( $e['ocupacao'] ) ) . ( $estoura ? ' — não cabe' : '' ) . '</span>';
	$h .= '<span class="aqm-c12-un">' . esc_html( aquametria_c12_ancora_nome( $f ) ) . ' — cesto de '
		. esc_html( aquametria_c12_fmt( $f['midia_L'], 1 ) ) . ' L, declarado até '
		. esc_html( aquametria_c12_fmt( $f['volume_max_L'], 0 ) ) . ' L';
	$h .= $estoura ? ' · o problema não é a mídia, é o filtro' : '';
	$h .= '</span></td>';
	return $h;
}
}

/* A célula do produto: a mídia do banco, a quantidade que ESSE fabricante manda
   pôr nesse aquário, e quanto rende a embalagem. */
if ( ! function_exists( 'aquametria_c12_compra_celula_html' ) ) {
function aquametria_c12_compra_celula_html( $e ) {
	if ( null === $e['compra'] ) {
		return '<td><span class="aqm-c12-semloja">nenhuma mídia do nosso banco publica dosagem por litro — '
			. 'sem dosagem declarada não dimensionamos, e não inventamos o número</span></td>';
	}
	$c = $e['compra'];
	$a = $c['ancora'];

	$h  = '<td><span class="aqm-c12-num">' . esc_html( aquametria_c12_ancora_nome( $a ) ) . '</span>';
	$h .= '<span class="aqm-c12-un">' . esc_html( aquametria_c12_ml( $c['mL'] ) ) . ' pela dosagem que a própria marca publica ('
		. esc_html( aquametria_c12_fmt( $a['mlL'], 2 ) ) . ' mL/L)';

	if ( $a['embalagem_L'] ) {
		$embalagens = (int) ceil( $c['mL'] / ( $a['embalagem_L'] * 1000 ) );
		$rende      = $a['embalagem_L'] * 1000 / $a['mlL'];
		$h         .= ' · ' . esc_html( aquametria_c12_fmt( $embalagens, 0 ) ) . ( 1 === $embalagens ? ' embalagem de ' : ' embalagens de ' )
			. esc_html( aquametria_c12_fmt( $a['embalagem_L'], 0 ) ) . ' L, que nessa dosagem rende até '
			. esc_html( aquametria_c12_litros( $rende ) ) . ' L de aquário';
	}

	$h .= $a['link'] ? '' : ' · sem link de loja';
	$h .= '</span></td>';
	return $h;
}
}

/* ---- A resposta antes da explicação (seção 5, item 2 do ARQUIPELAGO.md) ---
   Frase autossuficiente: precisa sobreviver a ser citada fora de contexto, por
   um modelo de linguagem que leu só este parágrafo. Por isso repete o número, a
   unidade, quem declarou e a data em vez de dizer "veja acima". */
if ( ! function_exists( 'aquametria_c12_resposta_direta_html' ) ) {
function aquametria_c12_resposta_direta_html() {
	$e100 = aquametria_c12_exemplo( 100 );

	$piso = $e100['piso'];
	$teto = $e100['teto'];

	$h  = '<div class="aqm-c12-direta">';

	$h .= '<p><strong>A resposta curta.</strong> Não existe um número: existe uma faixa, e ela é larga porque os fabricantes discordam. ';
	if ( $piso && $teto ) {
		$h .= 'Para um aquário de 100 litros de água, as dosagens declaradas pedem de <strong>'
			. esc_html( aquametria_c12_ml( $piso['mL'] ) ) . ' a ' . esc_html( aquametria_c12_ml( $teto['mL'] ) )
			. ' de mídia biológica</strong> — ' . esc_html( aquametria_c12_ml( $piso['mL'] ) ) . ' pela leitura mais econômica da '
			. esc_html( aquametria_c12_ancora_nome( $piso['ancora'] ) ) . ' (' . esc_html( aquametria_c12_fmt( $piso['ancora']['mlL'], 2 ) ) . ' mL por litro de água) ';
		$h .= 'e ' . esc_html( aquametria_c12_ml( $teto['mL'] ) ) . ' pela ' . esc_html( aquametria_c12_ancora_nome( $teto['ancora'] ) )
			. ' (' . esc_html( aquametria_c12_fmt( $teto['ancora']['mlL'], 2 ) ) . ' mL/L), que é a única marca brasileira que publica o número. ';
		$h .= 'São <strong>' . esc_html( aquametria_c12_fmt( round( $teto['ancora']['mlL'] / $piso['ancora']['mlL'] * 10 ) / 10, 1 ) )
			. ' vezes de diferença</strong> para a mesma função, e nenhuma das duas publica o método de medição. ';
	}
	$h .= 'Verificado em ' . esc_html( AQUAMETRIA_C12_VERIFICADO_EM ) . '.</p>';

	$h .= '<p><strong>Por que a Aquametria não escolhe uma delas.</strong> ';
	$h .= 'Publicar ' . ( $piso ? esc_html( aquametria_c12_fmt( $piso['ancora']['mlL'], 2 ) ) : '1,25' ) . ' mL/L como "o" número seria fingir que a Ocean Tech não existe, e o contrário também. ';
	$h .= 'Também não tiramos média: a média apagaria justamente o desacordo que faz esta página valer, e não há fonte nenhuma sustentando o valor do meio. ';
	$h .= 'Cada extremo sai com o nome de quem o declarou, o endereço da ficha e a data em que foi conferido. ';
	$h .= 'E há um segundo desacordo, entre balcões diferentes: quem vende <em>filtro</em> declara quanto de mídia cabe no aparelho — mídia total, com mecânica e química dentro — ';
	if ( null !== $e100['total_min'] && null !== $e100['total_max'] ) {
		$h .= 'o que dá de ' . esc_html( aquametria_c12_ml( $e100['total_min'] ) ) . ' a ' . esc_html( aquametria_c12_ml( $e100['total_max'] ) )
			. ' para os mesmos 100 L. As duas famílias não se comparam de igual para igual, e por isso saem em tabelas separadas.</p>';
	} else {
		$h .= 'e essa segunda família sai em tabela separada, porque não se compara de igual para igual com a primeira.</p>';
	}

	$h .= '<p><strong>O que ninguém publica, e esta página publica: o teto físico.</strong> ';
	if ( null !== $e100['ocupacao'] && $e100['filtro'] ) {
		$h .= 'A dosagem mais generosa nem sempre cabe no filtro que a pessoa tem. Nos mesmos 100 L, os '
			. esc_html( aquametria_c12_ml( $teto['mL'] ) ) . ' do teto ocupariam <strong>' . esc_html( aquametria_c12_pct( $e100['ocupacao'] ) ) . '</strong> '
			. 'do cesto do ' . esc_html( aquametria_c12_ancora_nome( $e100['filtro'] ) ) . ' — o menor filtro do nosso banco que o fabricante declara para esse volume — '
			. 'e isso só com a camada biológica, antes da mecânica e da química. ';
		$h .= 'Quando estoura, o problema não é a mídia: é o filtro. É conta trivial, e não a encontramos publicada em português. ';
	}
	$h .= '</p>';

	$h .= '<p><strong>E o que esta conta não sabe.</strong> As quatro dosagens são por litro de <em>água</em>, mas o trabalho da mídia depende da amônia que entra — ';
	$h .= 'ou seja, da carga de peixes, que nenhuma das declarações pergunta. Todas dimensionam um processo biológico pela variável errada. ';
	$h .= 'Registramos isso como constante pendente em vez de esconder: dizer o que a conta não alcança é parte da resposta.</p>';

	$h .= '</div>';
	return $h;
}
}

/* ---- A tabela de exemplos servida (seção 5, item 1) ---------------------- */
if ( ! function_exists( 'aquametria_c12_exemplos_html' ) ) {
function aquametria_c12_exemplos_html() {
	/* A classe -bloco-exemplos marca o BLOCO (painel inteiro); a -exemplos marca a
	   TABELA. São duas coisas, e separá-las é o que permite ao
	   teste-navegador-visibilidade-ia.mjs achar a tabela, o aviso e a coluna de
	   produto sem depender de qual calculadora está sendo medida. */
	$h  = '<div class="aqm-c12-painel aqm-c12-bloco-exemplos">';
	$h .= '<h3>Seis aquários já resolvidos, do piso ao teto declarado</h3>';
	$h .= '<p class="aqm-c12-sub">É a mesma conta do formulário acima, aplicada a seis volumes comuns. ';
	$h .= 'Estes números estão prontos no HTML desta página — não é preciso preencher nada, e quem lê sem executar JavaScript vê os mesmos valores que a calculadora devolve.</p>';

	/* Classe própria, e não .aqm-c12-tabela: aquela é a tabela de constantes, e o
	   teste de navegador a localiza pelo seletor. Duas tabelas com a mesma classe
	   quebram o localizador — foi assim que a C15 custou duas rodadas de teste. */
	$h .= '<div class="aqm-c12-rolagem"><table class="aqm-c12-exemplos">';
	$h .= '<tr><th>Aquário</th><th>Mídia biológica, do piso ao teto</th>';
	$h .= '<th>Mídia TOTAL que quem vende filtro reserva</th>';
	$h .= '<th>Teto físico: quanto o teto ocuparia do cesto</th>';
	$h .= '<th>Mídia do banco para esse aquário</th></tr>';

	foreach ( aquametria_c12_casos_exemplo() as $volume ) {
		$e = aquametria_c12_exemplo( $volume );

		$h .= '<tr>';
		$h .= '<td><span class="aqm-c12-num">' . esc_html( aquametria_c12_litros( $volume ) ) . ' L</span>';
		$h .= '<span class="aqm-c12-un">de água real, não a etiqueta do aquário</span></td>';

		if ( $e['piso'] && $e['teto'] ) {
			$h .= '<td><span class="aqm-c12-num">' . esc_html( aquametria_c12_ml( $e['piso']['mL'] ) ) . ' a '
				. esc_html( aquametria_c12_ml( $e['teto']['mL'] ) ) . '</span>';
			$h .= '<span class="aqm-c12-un">' . esc_html( aquametria_c12_ancora_nome( $e['piso']['ancora'] ) ) . ' ('
				. esc_html( aquametria_c12_fmt( $e['piso']['ancora']['mlL'], 2 ) ) . ' mL/L) → '
				. esc_html( aquametria_c12_ancora_nome( $e['teto']['ancora'] ) ) . ' ('
				. esc_html( aquametria_c12_fmt( $e['teto']['ancora']['mlL'], 2 ) ) . ' mL/L)</span></td>';
		} else {
			$h .= '<td><span class="aqm-c12-semloja">sem dosagem declarada no banco</span></td>';
		}

		if ( null !== $e['total_min'] && null !== $e['total_max'] ) {
			$h .= '<td><span class="aqm-c12-num">' . esc_html( aquametria_c12_ml( $e['total_min'] ) ) . ' a '
				. esc_html( aquametria_c12_ml( $e['total_max'] ) ) . '</span>';
			$h .= '<span class="aqm-c12-un">' . esc_html( aquametria_c12_fmt( count( $e['totais'] ), 0 ) )
				. ' filtros do banco, todas as camadas juntas</span></td>';
		} else {
			$h .= '<td><span class="aqm-c12-semloja">nenhum filtro do banco declara volume útil de mídia</span></td>';
		}

		$h .= aquametria_c12_teto_celula_html( $e );
		$h .= aquametria_c12_compra_celula_html( $e );
		$h .= '</tr>';
	}

	$h .= '</table></div>';

	$h .= '<p class="aqm-c12-criterio" style="margin-top:.8rem">Como ler a tabela. ';
	$h .= 'A primeira coluna é o volume de <strong>água real</strong>, não o número da etiqueta: é sobre a água que existe que a conta é feita, e é por isso que a calculadora de litragem vem antes desta. ';
	$h .= 'A segunda coluna abre na dosagem declarada mais econômica e fecha na mais generosa, com o nome de quem declarou cada extremo — não é uma faixa de segurança nossa, é o tamanho do desacordo entre fabricantes. ';
	$h .= 'A terceira é a outra família de âncoras, a de quem vende filtro, e mede mídia <strong>total</strong>: mecânica, biológica e química somadas. As duas não se comparam de igual para igual, e por isso estão em colunas separadas em vez de numa faixa só. ';
	$h .= 'A quarta é o teto físico, e é a coluna que não existe em nenhum outro lugar em português. ';
	$h .= 'Nenhum valor desta tabela foi digitado à mão: todos saem das mesmas regras que a calculadora usa, calculados no servidor a cada carregamento.</p>';

	$divulgacao = aquametria_c12_url( AQUAMETRIA_C12_PAGINA_AFILIADOS );

	/* Classe própria, e não a do aviso de publicidade do bloco de produto: o teste
	   de navegador localiza aquele por .aqm-c12-aviso-afiliado em modo estrito, e
	   duas ocorrências da mesma classe quebram o localizador. */
	$h .= '<p class="aqm-c12-aviso-tabela"><strong>Sobre a última coluna.</strong> ';
	$h .= 'Ela mostra a mídia do banco técnico da Aquametria que abre a faixa — a de dosagem declarada mais econômica — com a quantidade calculada pela dosagem que <em>aquela</em> marca publica, nunca por um número escolhido por nós. ';
	$h .= 'A ordem é essa e só essa: dosagem declarada, da mais econômica para a mais generosa. A comissão não entra em degrau nenhum, e mídia sem link de loja aparece do mesmo jeito e no mesmo lugar — a coluna diz quando é o caso. ';
	$h .= 'Escolher a mais econômica não é dizer que ela é a melhor: é o piso da faixa, e a página inteira existe para mostrar que o teto está dez vezes acima dele. ';
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
 * numérica e quebrariam o JSON tanto quanto quebraram o JavaScript em 08/09.
 *
 * Cada resposta do FAQ existe, com o mesmo número, na tabela servida acima —
 * FAQPage que promete o que a página não mostra é lixo, e seria lixo detectável.
 * ---------------------------------------------------------------------- */
if ( ! function_exists( 'aquametria_c12_jsonld_dados' ) ) {
function aquametria_c12_jsonld_dados() {
	$url    = aquametria_c12_url( AQUAMETRIA_C12_SLUG );
	$artigo = aquametria_c12_url( AQUAMETRIA_C12_ARTIGO );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$app = array(
		'@type'                  => 'WebApplication',
		'@id'                    => $url . '#calculadora',
		'name'                   => 'Calculadora de mídia filtrante para aquário',
		'alternateName'          => 'Aquametria C12 — quanta mídia biológica o aquário precisa',
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
		'softwareVersion' => AQUAMETRIA_C12_VERSAO,
		'description'     => 'Converte o volume real de água no volume de mídia biológica que cada fabricante declara, publicando as quatro dosagens lado a lado '
			. 'em vez de escolher uma delas ou tirar média. Cruza esse volume com o cesto do filtro para mostrar o teto físico — quanto da capacidade de mídia '
			. 'a camada biológica ocuparia — e avisa quando a dosagem simplesmente não cabe no aparelho.',
		'featureList' => array(
			'Volume de mídia biológica pelas quatro dosagens declaradas por fabricante, cada uma com o nome da marca',
			'Faixa do piso ao teto, com a divergência de dez vezes publicada em vez de escondida',
			'Segunda família de âncoras: a mídia total que quem vende filtro reserva no aparelho',
			'Teto físico — quanto do cesto do filtro a camada biológica ocuparia, com aviso quando estoura',
			'Dosagem de mídia química calculada pela declaração de cada fabricante, sem média inventada',
			'Ordem das camadas no cesto, com fonte, e recusa explícita de repartir o cesto em porcentagens',
			'Calendário de troca de perlon, carvão e cerâmica a partir da data da última manutenção',
			'Tabela pré-calculada para seis aquários de 30 a 300 L, já no HTML servido',
		),
		'publisher'        => $editora,
		'isBasedOn'        => 'Fichas de fabricante e de varejo especializado coletadas pela Aquametria até ' . AQUAMETRIA_C12_VERIFICADO_EM,
		'mainEntityOfPage' => $artigo,
	);

	$perguntas = array();

	foreach ( aquametria_c12_casos_exemplo() as $volume ) {
		$e = aquametria_c12_exemplo( $volume );
		if ( ! $e['piso'] || ! $e['teto'] ) {
			continue;
		}

		$texto = 'Um aquário com ' . aquametria_c12_litros( $volume ) . ' litros de água real pede de '
			. aquametria_c12_ml( $e['piso']['mL'] ) . ' a ' . aquametria_c12_ml( $e['teto']['mL'] ) . ' de mídia biológica, '
			. 'dependendo de qual fabricante você seguir: ' . aquametria_c12_ml( $e['piso']['mL'] ) . ' pela leitura mais econômica da '
			. aquametria_c12_ancora_nome( $e['piso']['ancora'] ) . ' (' . aquametria_c12_fmt( $e['piso']['ancora']['mlL'], 2 ) . ' mL por litro de água) '
			. 'e ' . aquametria_c12_ml( $e['teto']['mL'] ) . ' pela ' . aquametria_c12_ancora_nome( $e['teto']['ancora'] ) . ' ('
			. aquametria_c12_fmt( $e['teto']['ancora']['mlL'], 2 ) . ' mL/L). '
			. 'A Aquametria publica os dois extremos com o nome de quem declarou cada um e não tira média entre eles, '
			. 'porque a média apagaria o desacordo e não há fonte nenhuma sustentando o valor do meio. ';

		if ( null !== $e['total_min'] && null !== $e['total_max'] ) {
			$texto .= 'Quem vende filtro declara outra coisa — mídia total, com mecânica e química dentro — e para esse volume isso daria de '
				. aquametria_c12_ml( $e['total_min'] ) . ' a ' . aquametria_c12_ml( $e['total_max'] ) . '. '
				. 'As duas famílias não se comparam de igual para igual. ';
		}

		$texto .= 'Verificado em ' . AQUAMETRIA_C12_VERIFICADO_EM . '.';

		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => 'Quanta mídia biológica para um aquário de ' . aquametria_c12_litros( $volume ) . ' litros?',
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $texto ),
		);
	}

	foreach ( aquametria_c12_casos_exemplo() as $volume ) {
		$e = aquametria_c12_exemplo( $volume );
		if ( null === $e['ocupacao'] || ! $e['filtro'] || ! $e['teto'] ) {
			continue;
		}

		$estoura = ( $e['ocupacao'] > 100 );
		$texto   = 'Depende do filtro, e é uma conta que quase ninguém faz antes de comprar a mídia. '
			. 'O menor filtro do banco técnico da Aquametria que o fabricante declara para ' . aquametria_c12_litros( $volume )
			. ' L é o ' . aquametria_c12_ancora_nome( $e['filtro'] ) . ', com cesto de '
			. aquametria_c12_fmt( $e['filtro']['midia_L'], 1 ) . ' L de volume útil de mídia declarado para até '
			. aquametria_c12_fmt( $e['filtro']['volume_max_L'], 0 ) . ' L de aquário. '
			. 'A dosagem do teto (' . aquametria_c12_ancora_nome( $e['teto']['ancora'] ) . ', '
			. aquametria_c12_fmt( $e['teto']['ancora']['mlL'], 2 ) . ' mL/L) pede ' . aquametria_c12_ml( $e['teto']['mL'] )
			. ', que ocupa ' . aquametria_c12_pct( $e['ocupacao'] ) . ' desse cesto — e isso só com a camada biológica, antes da mecânica e da química. ';

		if ( $estoura ) {
			$texto .= 'Ou seja: nesse volume a dosagem mais generosa NÃO CABE no aparelho. Quando isso acontece, o problema não é a mídia, é o filtro — '
				. 'e a saída honesta é filtro maior, não espremer mídia num cesto que não comporta.';
		} else {
			$texto .= 'Ou seja: nesse volume até a dosagem mais generosa cabe, e ainda sobra espaço para as outras camadas.';
		}

		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => 'A mídia biológica cabe no filtro de um aquário de ' . aquametria_c12_litros( $volume ) . ' litros?',
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $texto ),
		);
	}

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Quantos mililitros de mídia biológica por litro de água?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Os fabricantes que publicam o número declaram de 1,25 a 12,50 mL de mídia biológica por litro de água — dez vezes de diferença para a mesma função. '
				. 'Seachem Matrix: 1,25 mL/L numa leitura da própria copy ("250 mL para 200 L") e 2,64 mL/L noutra ("1 L para 100 galões"), o mesmo fabricante discordando de si mesmo por 2,1 vezes. '
				. 'JBL MicroMec: 5,00 mL/L (650 g, que é 1 L, para 200 L). Ocean Tech Bio Glass: 12,50 mL/L (1 L para cada 80 L), a única marca brasileira que publica o número. '
				. 'A Aquametria publica as quatro com atribuição e data em vez de escolher uma, e não tira média — nenhuma fonte sustenta o valor do meio. '
				. 'Pior: a marca que declara MAIS área por litro de mídia é a que pede DEZ VEZES menos mídia, o inverso do que se esperaria, e nenhuma das quatro publica método de medição.',
		),
	);

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Encher o cesto do filtro de mídia biológica é melhor?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Não é o que os fabricantes declaram, e em vários volumes o cesto nem comporta a dosagem mais generosa: '
				. 'num aquário de 200 L, os 2,50 L que a dosagem do teto pede ocupariam 208 % do cesto de 1,2 L do Seachem Tidal 55, '
				. 'que é o menor filtro do nosso banco declarado para esse volume — ou seja, não cabe, e isso só com a camada biológica. '
				. 'O cesto tem de acomodar as três camadas — mecânica, biológica e química — e a Aquametria publica a ORDEM delas, que tem fonte, '
				. 'em 6 posições (cerâmica ou argila expandida, perlon, carvão, perlon, cerâmica, perlon), mas se recusa a repartir o cesto em porcentagens: '
				. 'nenhuma fonte do levantamento declara essa proporção, e inventar percentuais seria exatamente o tipo de número que este site existe para não publicar. '
				. 'O que dá para dizer com número é o teto físico: quanto do volume útil de mídia declarado pelo fabricante do filtro cada dosagem ocuparia. '
				. 'E há uma regra de segurança que vale mais que qualquer volume: nunca lave toda a mídia biológica de uma vez, e nunca em água de torneira — '
				. 'o cloro existe para matar bactéria, e é a colônia nitrificante que faz a filtragem funcionar.',
		),
	);

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Por que a quantidade de mídia não depende de quantos peixes eu tenho?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Porque nenhuma das dosagens declaradas pergunta isso — e essa é a crítica de fundo que a Aquametria registra em vez de esconder. '
				. 'As quatro dosagens são por litro de água, mas o trabalho da mídia depende da amônia que entra no sistema, ou seja, da carga de peixes e de ração. '
				. 'Dois aquários de 100 L com lotações muito diferentes recebem a mesma recomendação de mídia de todos os fabricantes. '
				. 'Todas dimensionam um processo biológico pela variável errada. A constante que fecharia isso — taxa de nitrificação por área de mídia — '
				. 'não foi encontrada publicada com fonte, e por isso está registrada como pendente e NÃO entra em nenhuma fórmula desta página. '
				. 'Constante pendente dentro de fórmula publicada é proibida na Aquametria.',
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

if ( ! function_exists( 'aquametria_c12_imprimir_jsonld' ) ) {
function aquametria_c12_imprimir_jsonld() {
	$json = wp_json_encode( aquametria_c12_jsonld_dados(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-c12-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
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

if ( ! function_exists( 'aquametria_c12_estilo_impresso' ) ) {
function aquametria_c12_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c12_pagina_usa' ) ) {
function aquametria_c12_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_midia' );
}
}

if ( ! function_exists( 'aquametria_c12_imprimir_estilo' ) ) {
function aquametria_c12_imprimir_estilo() {
	if ( aquametria_c12_estilo_impresso() ) {
		return;
	}
	aquametria_c12_estilo_impresso( true );
	echo '<style id="aquametria-c12-estilo">' . "\n" . aquametria_c12_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c12_cabeca' ) ) {
function aquametria_c12_cabeca() {
	if ( ! aquametria_c12_pagina_usa() ) {
		return;
	}
	aquametria_c12_imprimir_estilo();
	aquametria_c12_imprimir_jsonld();
}
}
add_action( 'wp_head', 'aquametria_c12_cabeca', 20 );

if ( ! function_exists( 'aquametria_c12_rodape' ) ) {
function aquametria_c12_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c12_imprimir_estilo();

	$js  = 'var AQM_C12_DATA = ' . wp_json_encode( AQUAMETRIA_C12_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C12_MIDIAS = ' . wp_json_encode( array_values( aquametria_c12_catalogo_midias() ) ) . ";\n";
	$js .= 'var AQM_C12_FILTROS = ' . wp_json_encode( array_values( aquametria_c12_catalogo_filtros() ) ) . ";\n";
	$js .= aquametria_c12_js();
	echo '<script id="aquametria-c12-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 7. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c12_shortcode' ) ) {
function aquametria_c12_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c12_rodape', 20 );

	$h  = '<div class="aqm-c12">';
	$h .= aquametria_c12_resposta_direta_html();
	$h .= aquametria_c12_form_html();
	$h .= aquametria_c12_resposta_html();
	$h .= aquametria_c12_exemplos_html();
	$h .= aquametria_c12_tenho_html();
	$h .= aquametria_c12_fontes_html();
	$h .= aquametria_c12_adiante_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_midia', 'aquametria_c12_shortcode' );

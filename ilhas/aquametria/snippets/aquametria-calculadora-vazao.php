/**
 * Aquametria Calculadora de Vazão do Filtro — C3
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.3 (08/09/2026) — o painel de ligações passou a linkar a C15, publicada nesta data:
 * em aquário plantado a corrente e a iluminação decidem juntas o que acontece com o CO2. A 1.0.2 linkou a C12, publicada
 * data: é ela que diz quanta mídia o filtro escolhido aqui precisa carregar. A 1.0.1 linkou a C5
 *
 * Segunda calculadora do lote e a primeira com bloco de produto. Converte o
 * volume real do aquário (herdado da C1 pelo localStorage) na faixa de vazão
 * que os filtros precisam entregar — e publica o achado que a página existe
 * para publicar: o fabricante dimensiona 1,76 renovações por hora e a web
 * brasileira pede de 3 a 10. É uma divergência de até 5,7 vezes, e nenhuma
 * fonte brasileira do nosso levantamento confronta as duas.
 *
 * Registra o shortcode [aquametria_calculadora_vazao] e se anuncia no hub pelo
 * filtro 'aquametria_calculadoras' da casca: enquanto este snippet estiver
 * ativo, o cartão da C3 aparece como publicada. Nada para editar em dois lugares.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem, então HTML que dependesse da query string seria
 * servido errado para o visitante seguinte. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não aplica fator de perda de carga. Vazão nominal é medida sem mídia e a
 *   coluna zero; a perda com mídia suja não tem fonte no nosso levantamento e
 *   constante inventada é proibida aqui. Em vez do fator, a página entrega o
 *   protocolo do balde, que é medição própria do visitante.
 * - Não publica turnover para aquário marinho: o corpus não tem essa constante.
 *   Quem marca "tenho sump" recebe o volume mínimo do sump, que tem fonte, e a
 *   página diz que o resto não tem.
 *
 * Bloco de produto: os filtros vêm do catálogo embutido mais abaixo, gerado por
 * ferramentas/gerar-catalogo-filtros.py a partir de dados/produtos-filtro.json.
 * Mexeu no banco, rode o gerador — as duas cópias não podem divergir. A ordem é
 * por adequação técnica ao resultado; link de afiliado não ordena nem filtra
 * (regra V16 do esquema). Produto sem link aparece igual, só que sem botão de
 * loja. Preço não entra: snippet é estático e preço envelhece na tela.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C3_VERSAO' ) ) {
	define( 'AQUAMETRIA_C3_VERSAO', '1.0.3' );
	define( 'AQUAMETRIA_C3_SLUG', 'calculadora-de-vazao-do-filtro' );
	define( 'AQUAMETRIA_C3_VERIFICADO_EM', '08/09/2026' );
	/* Constante 'eheim-classic-250-2213' (dados/constantes-calculadoras.json):
	   440 L/h declarados para até 250 L, ou seja 1,76 renovações por hora. É o
	   contraponto do fabricante às regras de bolso brasileiras. */
	define( 'AQUAMETRIA_C3_FABRICANTE_XH', 1.76 );
	/* Constante 'sump-proporcao-minima': 20 % do volume do aquário. */
	define( 'AQUAMETRIA_C3_SUMP_PCT', 20 );
	define( 'AQUAMETRIA_C3_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_registrar_no_hub' ) ) {
function aquametria_c3_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C3' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C3_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c3_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Catálogo de filtros
 *
 * NÃO EDITE À MÃO o trecho entre os marcadores. Ele é a cópia, dentro do
 * snippet, do que dados/produtos-filtro.json já tem — porque o site não lê o
 * repositório em tempo de execução. Depois de mexer no banco:
 *
 *     python3 ferramentas/gerar-catalogo-filtros.py
 *
 * Entra no catálogo quem o validador considera apto a ser sugerido pela C3
 * (minimo_para_sugerir do esquema) e não está em rascunho nem em revalidar.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_catalogo' ) ) {
function aquametria_c3_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-filtros.py */
	return array(
		array(
			'id' => 'sunsun-hw-603b',
			'marca' => 'SunSun',
			'modelo' => 'HW-603B',
			'tipo' => 'canister',
			'vazao_lh' => 400,
			'potencia_w' => 6,
			'coluna_m' => 0.85,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 80,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'manta' ),
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha do SunSun HW-603B: 400 L/h, 2,3 L de camara de midia, 110 V',
			'fonte_url' => 'https://www.proaquarista.com.br/produto/sunsun-canister-hw-603b-23l-400lh-110v.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Primeiro canister de verdade do banco para aquario pequeno: 2,3 L de camara de midia para os 80 L declarados dao 28,8 mL de midia por litro de agua, contra os 12 mL/L do cesto do Eheim classic 250 e os 6,0 mL/L do Seachem Tidal 55. E o item que faltava para a faixa de 30 a 80 L tanto na C3 quanto na C12. O campo de volume atendido carrega os 80 L do varejo BR, que e a declaracao mais conservadora das duas; a de 120 L do varejo estrangeiro sai atribuida ao lado. Coluna maxima de 0,85 m: nao vence movel alto, e isso precisa aparecer na tela.',
		),
		array(
			'id' => 'eheim-classic-250-2213',
			'marca' => 'Eheim',
			'modelo' => 'classic 250 (2213)',
			'tipo' => 'canister',
			'vazao_lh' => 440,
			'potencia_w' => 8,
			'coluna_m' => 1.5,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 250,
			'voltagem' => array( '110' ),
			'uv_w' => null,
			'midia' => array( 'EHEIM SUBSTRAT pro' ),
			'fonte_ref' => 'Eheim, dados do classic 250 (2213); mesma coleta que gerou a constante eheim-classic-250-2213 do Bloco 2',
			'fonte_url' => 'https://eheim.com/en_GB/aquatics/aquarium-technology/filter/external-filter/classic-250',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-07',
			'link' => 'https://s.shopee.com.br/6fh6u1wYls',
			'anuncio' => 'Filtro Canister Classic 250 440lh Eheim - 2213',
			'loja' => 'shopee',
			'observacao' => 'O registro que ancora a C3: 440 L/h para 250 L da 1,8 renovacoes/h, de 3 a 6 vezes ABAIXO das 5 a 10 x/h que as fontes brasileiras repetem. Voltagem 110 V confirmada em varejo BR em 08/09/2026, o que libera a sugestao da C3. ATENCAO: o anuncio de afiliado nao declara voltagem, e por isso o cartao de produto obriga o aviso de conferir a voltagem antes de comprar.',
		),
		array(
			'id' => 'atman-hf-0400',
			'marca' => 'Atman',
			'modelo' => 'HF-0400',
			'tipo' => 'hang-on',
			'vazao_lh' => 440,
			'potencia_w' => 6.0,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 90,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado), ficha do Atman HF-0400: vazao 440 L/h, 6,0 W, aquarios de ate 90 L',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-externo-hang-on-hf-0400-440l-h.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Hang-on: nao tem altura maxima de recalque, bombeia contra a propria carcaca (coluna_maxima_nao_se_aplica). 440 L/h para os 90 L declarados da 4,9 renovacoes/h, dentro da faixa de bolso brasileira de 5 a 10 x/h e muito acima das 1,8 x/h que a Eheim declara no classic 250. E a opcao de entrada do banco para a faixa de 30 a 90 L, que ate 09/09/2026 nao tinha filtro nenhum sugerivel.',
		),
		array(
			'id' => 'atman-hf-0600',
			'marca' => 'Atman',
			'modelo' => 'HF-0600',
			'tipo' => 'hang-on',
			'vazao_lh' => 650,
			'potencia_w' => 8.0,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 150,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado), ficha do Atman HF-0600: 650 L/h, 8 W, aquarios de ate 150 L',
			'fonte_url' => 'https://www.aquaricamp.com.br/filtro-atman-hang-on-650l-h-60hz-4404.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Hang-on (coluna_maxima_nao_se_aplica). 650 L/h para 150 L declarados da 4,3 renovacoes/h. Cobre a faixa de 100 a 150 L, que so tinha canister ate 09/09/2026.',
		),
		array(
			'id' => 'atman-at-3336',
			'marca' => 'Atman',
			'modelo' => 'AT-3336',
			'tipo' => 'canister',
			'vazao_lh' => 800,
			'potencia_w' => 20,
			'coluna_m' => 1.8,
			'coluna_na' => false,
			'volume_min_L' => 180,
			'volume_max_L' => 250,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'ceramica', 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp e Atlantida Aquarios (varejo BR especializado), ficha do canister Atman AT-3336: 800 L/h, 20 W, 1,8 m de coluna, aquarios de 180 a 250 L, 3 cestas',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-canister-at-3336-vaz-o-800-l-h.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Irmao menor do AT-3338 (CF-1200) que ja estava no banco. 800 L/h para os 250 L do topo declarado da 3,2 renovacoes/h. Volume util de midia nao publicado por nenhuma das fontes vistas — por isso nao entra na sugestao da C12, so na da C3 e da C7.',
		),
		array(
			'id' => 'atman-hf-0800',
			'marca' => 'Atman',
			'modelo' => 'HF-0800',
			'tipo' => 'hang-on',
			'vazao_lh' => 900,
			'potencia_w' => 8.3,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 250,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Pet Sonaga (varejo BR), ficha do Atman HF-0800: 900 L/h, 8,3 W, 110 V — a unica fonte vista que publica a potencia com uma casa decimal',
			'fonte_url' => 'https://www.petsonaga.com.br/aquario/bomba/aquario/filtro-externo-atman-hf-0800-900lh-8-3w-110v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Hang-on (coluna_maxima_nao_se_aplica). Com 900 L/h para 250 L sao 3,6 renovacoes/h; com os 750 L/h da fonte divergente, 3,0 x/h. A tela precisa dizer que a vazao do HF-800 nao e consenso entre as lojas brasileiras.',
		),
		array(
			'id' => 'seachem-tidal-55',
			'marca' => 'Seachem',
			'modelo' => 'Tidal 55',
			'tipo' => 'hang-on',
			'vazao_lh' => 1000,
			'potencia_w' => 6,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'Seachem Matrix' ),
			'fonte_ref' => 'Seachem/Sicce, manual do Tidal 55/75/110 (250 US gph = 1000 L/h; 55 US gal = 200 L; 6 W em 120 V/60 Hz e 5 W em 230 V/50 Hz; cesto de 0,32 US gal = 1,2 L)',
			'fonte_url' => 'https://www.sicce.com/media/wysiwyg/ISTRUZIONI/80N567-A_Tidal_instructions.pdf',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/1LfaYURnHi',
			'anuncio' => 'Filtro externo (Hang-on) - Tidal 55 - Seachem',
			'loja' => 'shopee',
			'observacao' => 'Hang-on. NAO tem altura maxima de recalque: o filtro fica pendurado na borda e bombeia contra a propria carcaca, entao coluna_maxima_m nao se aplica (campo coluna_maxima_nao_se_aplica). Em 08/09/2026 saiu de \'revalidar\' para \'completo\': a eficiencia de 167 L/h por W, que o validador apontava como implausivel, e a declaracao do proprio fabricante e coerente com um hang-on trabalhando a coluna quase zero - o limite de 120 L/h por W foi calibrado para canister, e a regra V10 passou a valer so para canister e sump. Em 08/09/2026 ganhou volume_filtragem_L = 1,2 L (coleta da C12): 1,2 L de midia para os 200 L que o fabricante declara atender da 6,0 mL de midia por litro de agua - metade dos 12 mL/L do cesto do Eheim classic 250. Dois fabricantes, o mesmo problema, o dobro de midia.',
		),
		array(
			'id' => 'atman-at-3338',
			'marca' => 'Atman',
			'modelo' => 'AT-3338',
			'tipo' => 'canister',
			'vazao_lh' => 1200,
			'potencia_w' => 35,
			'coluna_m' => 1.8,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 450,
			'voltagem' => array( '110', '127', '220' ),
			'uv_w' => null,
			'midia' => array( 'ceramica' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado) e outras lojas brasileiras que replicam a mesma ficha',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-canister-at-3338-vaz-o-1200-l-h-gratis-1-litro-ceramica.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => '1200 L/h para ate 450 L = 2,7 renovacoes/h declaradas pela propria ficha. Primeiro registro da semente com todos os campos obrigatorios da entidade preenchidos. Em 08/09/2026 a coleta da C12 trouxe o volume de midia, e trouxe junto uma ambiguidade que a C12 publica em vez de esconder: 1,6 L no conjunto ou 1,6 L por cesto (4,8 L). Pelos 450 L que a ficha declara atender, isso e a diferenca entre 3,6 e 10,7 mL de midia por litro de agua.',
		),
		array(
			'id' => 'sunsun-hw-303b',
			'marca' => 'SunSun',
			'modelo' => 'HW-303B',
			'tipo' => 'canister',
			'vazao_lh' => 1400,
			'potencia_w' => 35,
			'coluna_m' => 2.0,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 350,
			'voltagem' => array( '110', '220' ),
			'uv_w' => 9,
			'midia' => array( 'ceramica', 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'SunSun, especificacao do HW-303B (370 GPH = 1400 L/h; UV 9 W), replicada na pagina do produto na Amazon.com.br',
			'fonte_url' => 'https://www.amazon.com.br/SunSun-Hw303B-370GPH-filtro-esterilizador/dp/B00MH2NRIQ',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'Em 09/09/2026 ganhou coluna_maxima_m = 2,0 m e mangueira de 16 mm, colhidos no varejo especializado estrangeiro, e passou a ser sugerivel pela C3 — era o filtro de maior vazao do banco e estava barrado por um campo so. Saiu de \'parcial\' para \'completo\': todos os obrigatorios de filtro estao preenchidos com fonte. O volume util de midia (volume_filtragem_L) continua sem fonte nenhuma, e por isso o filtro nao entra na C12 — campo opcional na ficha, requisito daquela calculadora. 1400 L/h para 350 L = 4,0 renovacoes/h.',
		),
		array(
			'id' => 'atman-at-3338s',
			'marca' => 'Atman',
			'modelo' => 'AT-3338S',
			'tipo' => 'canister',
			'vazao_lh' => 1500,
			'potencia_w' => 18,
			'coluna_m' => 1.5,
			'coluna_na' => false,
			'volume_min_L' => 150,
			'volume_max_L' => 400,
			'voltagem' => array( '220' ),
			'uv_w' => null,
			'midia' => array(),
			'fonte_ref' => 'AquaSN (varejo BR especializado), ficha do AT-3338S 220 V',
			'fonte_url' => 'https://www.aquasn.com.br/atman-filtro-canister-at-3338s-1500-lh-220v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'observacao' => 'O caso que justificou o campo variante: uma letra a mais no modelo muda vazao (1200 para 1500 L/h), potencia (35 para 18 W), coluna (1,8 para 1,5 m) e volume atendido (ate 450 para 150 a 400 L). Sao dois produtos, nunca um. Turnover implicito de 3,8 (no teto) a 10,0 (no piso) renovacoes/h. Em 08/09/2026 ganhou volume_filtragem_L pela coleta da C12. Aqui a ficha se contradiz sozinha: as dimensoes que ela mesma publica nao comportam a capacidade que ela mesma declara por cesto.',
		),
	);
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_css' ) ) {
function aquametria_c3_css() {
	return <<<'CSS'
.aqm-c3{--c3-tinta:var(--aqm-tinta,#0D1B22);--c3-lamina:var(--aqm-lamina,#0E7C8C);
--c3-papel:var(--aqm-papel,#F4F7F7);--c3-superficie:var(--aqm-superficie,#FFFFFF);
--c3-traco:var(--aqm-traco,#DDE5E6);--c3-legenda:var(--aqm-legenda,#5C7075);
--c3-alerta:var(--aqm-alerta,#B5762A);
--c3-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c3-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c3-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c3-texto);color:var(--c3-tinta);}
.aqm-c3 *{box-sizing:border-box;}
.aqm-c3 form{margin:0;}
.aqm-c3-painel{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c3-painel h3{font-family:var(--c3-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c3-painel .aqm-c3-sub{color:var(--c3-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c3-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.9rem;}
.aqm-c3-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c3-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c3-campo .aqm-c3-dica{font-size:.74rem;color:var(--c3-legenda);line-height:1.35;}
.aqm-c3 input[type=text],.aqm-c3 select{width:100%;font-family:var(--c3-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c3-traco);border-radius:2px;background:var(--c3-superficie);color:var(--c3-tinta);}
.aqm-c3 select{font-family:var(--c3-texto);}
.aqm-c3 input:focus,.aqm-c3 select:focus{outline:2px solid var(--c3-lamina);outline-offset:1px;}
.aqm-c3 input.aqm-c3-erro{border-color:var(--c3-alerta);}
.aqm-c3-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c3-caixa input{margin-top:.2rem;}
.aqm-c3-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c3 button{font-family:var(--c3-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c3-lamina);color:var(--c3-superficie);cursor:pointer;}
.aqm-c3 button.aqm-c3-secundario{background:transparent;color:var(--c3-lamina);border:1px solid var(--c3-traco);}
.aqm-c3 button:hover{filter:brightness(1.08);}
.aqm-c3-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c3-avisos li{font-size:.88rem;color:var(--c3-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c3-resultado{margin:0 0 1.2rem;}
.aqm-c3-faixa{background:var(--c3-superficie);border:2px solid var(--c3-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c3-rotulo{font-family:var(--c3-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c3-legenda);}
.aqm-c3-valor{font-family:var(--c3-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c3-valor .aqm-c3-unidade{font-size:.95rem;font-weight:500;color:var(--c3-legenda);margin-left:.3rem;}
.aqm-c3-criterio{font-size:.83rem;color:var(--c3-legenda);line-height:1.5;margin:0;}
.aqm-c3-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c3-cartao{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c3-cartao .aqm-c3-valor{font-size:1.5rem;}
.aqm-c3-nota{border-left:3px solid var(--c3-lamina);background:var(--c3-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c3-legenda);margin:0 0 1rem;}
.aqm-c3-nota strong{color:var(--c3-tinta);}
.aqm-c3-nota.aqm-c3-nota-alerta{border-left-color:var(--c3-alerta);}
.aqm-c3-vazio{font-family:var(--c3-texto);font-size:.95rem;color:var(--c3-legenda);font-weight:500;}
.aqm-c3-produtos{margin:0 0 1.2rem;}
.aqm-c3-produtos h3{font-family:var(--c3-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c3-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c3-produto{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c3-placa{background:var(--c3-papel);border:1px solid var(--c3-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c3-placa .aqm-c3-marca{font-family:var(--c3-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c3-placa .aqm-c3-numero{font-family:var(--c3-mono);font-size:1.15rem;font-weight:600;color:var(--c3-lamina);line-height:1.1;}
.aqm-c3-placa .aqm-c3-un{font-family:var(--c3-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c3-legenda);}
.aqm-c3-produto h4{font-family:var(--c3-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c3-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c3-porque strong{font-family:var(--c3-mono);font-size:.86rem;}
.aqm-c3-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c3-legenda);line-height:1.5;}
.aqm-c3-ficha li{margin:0;}
.aqm-c3-ficha b{font-family:var(--c3-mono);font-weight:600;color:var(--c3-tinta);}
.aqm-c3-loja{display:inline-block;font-family:var(--c3-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c3-lamina);color:var(--c3-superficie);text-decoration:none;}
.aqm-c3-loja:hover{filter:brightness(1.08);color:var(--c3-superficie);}
.aqm-c3-semloja{font-size:.82rem;color:var(--c3-legenda);font-style:italic;}
.aqm-c3-aviso-afiliado{background:var(--c3-papel);border:1px solid var(--c3-traco);border-left:3px solid var(--c3-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c3-legenda);margin:1rem 0 0;}
.aqm-c3-aviso-afiliado strong{color:var(--c3-tinta);}
.aqm-c3-citar{background:var(--c3-papel);border:1px dashed var(--c3-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c3-citar p{margin:0 0 .6rem;}
.aqm-c3-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c3-fontes{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c3-fontes th,.aqm-c3-fontes td{border:1px solid var(--c3-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c3-fontes th{background:var(--c3-papel);font-family:var(--c3-display);font-size:.8rem;}
.aqm-c3-fontes td:first-child{font-family:var(--c3-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c3-selo{display:inline-block;font-family:var(--c3-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c3-alerta);border:1px solid var(--c3-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c3-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c3-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c3-oculto{display:none;}
@media (max-width:600px){.aqm-c3-valor{font-size:1.6rem;}
.aqm-c3-produto{grid-template-columns:1fr;}
.aqm-c3-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_js' ) ) {
function aquametria_c3_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var FABRICANTE_XH = 1.76;   /* eheim-classic-250-2213: 440 L/h para 250 L */
	var SUMP_PCT = 20;          /* sump-proporcao-minima */

	/* Bandas de turnover, por perfil. Cada uma é uma constante do registro em
	   dados/constantes-calculadoras.json, com fonte e data. Não há banda para
	   aquário marinho: o levantamento não trouxe nenhuma, e aqui não se inventa. */
	var BANDAS = {
		comunitario: [
			{ id: 'turnover-comunitario-mybest', rotulo: 'Leitura conservadora BR', curto: 'leitura conservadora da my-best BR', faixa: [4, 5], fonte: 'my-best BR' },
			{ id: 'turnover-comunitario-br', rotulo: 'Regra de bolso BR', curto: 'regra de bolso brasileira', faixa: [5, 10], fonte: 'Aquarismo Paulista; AquaOnline' }
		],
		plantado: [
			{ id: 'turnover-plantado', rotulo: 'Plantado BR', curto: 'faixa brasileira para plantado', faixa: [3, 5], fonte: 'AquaPeixes' }
		]
	};

	var raiz = document.querySelector('.aqm-c3');
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

	/* Vazão é número grosso: arredondar para dezena abaixo de 1000 e para
	   cinquentena acima disso evita a falsa precisão de "437 L/h". */
	function lh(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		var passo = n >= 1000 ? 50 : 10;
		return fmt(Math.round(n / passo) * passo, 0);
	}

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	function campos() {
		return {
			volume: num(el('aqm-c3-volume').value),
			perfil: el('aqm-c3-perfil').value === 'plantado' ? 'plantado' : 'comunitario',
			carga: el('aqm-c3-carga').value,
			coluna: num(el('aqm-c3-coluna').value),
			tipo: el('aqm-c3-tipo').value,
			sump: el('aqm-c3-sump').checked
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
		if (d.coluna !== null && (d.coluna < 0 || d.coluna > 6)) {
			r.erros.push({ campo: 'coluna', texto: 'Altura de coluna em metros, entre 0 e 6.' });
		}
		if (r.erros.length) { return r; }

		var V = d.volume;
		r.entradas = d;
		r.piso = V * FABRICANTE_XH;
		r.bandas = BANDAS[d.perfil].map(function (b) {
			return {
				id: b.id, rotulo: b.rotulo, fonte: b.fonte, xh: b.faixa,
				min: V * b.faixa[0], max: V * b.faixa[1]
			};
		});

		var tetos = r.bandas.map(function (b) { return b.max; });
		r.teto = Math.max.apply(null, tetos);
		r.teto_xh = r.teto / V;
		r.razao = r.teto / r.piso;

		/* A banda de bolso é a última da lista: é ela que a maioria das fontes
		   brasileiras repete, e é sobre ela que a carga de peixes se posiciona. */
		r.bolso = r.bandas[r.bandas.length - 1];

		if (d.sump) {
			r.sump_L = V * SUMP_PCT / 100;
		}

		if (d.coluna !== null && d.coluna > 0) {
			r.avisos.push('A vazão nominal do catálogo é medida a coluna zero e sem mídia. Com ' + fmt(d.coluna, 1)
				+ ' m de coluna e o cesto cheio, a vazão que chega ao aquário é menor — quanto menor, não sabemos: '
				+ 'não existe fator de perda com fonte no nosso levantamento, e aqui não se inventa constante. Meça com o protocolo do balde.');
		}

		r.produtos = escolher(r, d);
		return r;
	}

	/* Adequação técnica, e só ela: vazão dentro da faixa calculada, coluna
	   suficiente, tipo compatível. Link de afiliado não entra no critério nem
	   na ordem (regra V16 do esquema do banco). */
	function escolher(r, d) {
		var meio = (r.piso + r.teto) / 2;
		var fora = [];
		var dentro = AQM_C3_CATALOGO.filter(function (p) {
			if (d.tipo !== 'qualquer' && p.tipo !== d.tipo) { return false; }
			if (p.vazao_lh < r.piso || p.vazao_lh > r.teto) { return false; }
			if (d.coluna !== null && d.coluna > 0 && !p.coluna_na && p.coluna_m !== null && p.coluna_m < d.coluna) {
				fora.push(p.marca + ' ' + p.modelo + ' atende a faixa, mas a coluna máxima declarada ('
					+ fmt(p.coluna_m, 1) + ' m) é menor que os ' + fmt(d.coluna, 1) + ' m que você informou.');
				return false;
			}
			return true;
		});

		dentro.sort(function (a, b) {
			return Math.abs(a.vazao_lh - meio) - Math.abs(b.vazao_lh - meio);
		});

		r.barrados_por_coluna = fora;
		return dentro.slice(0, 5);
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c3-saida');
		var ul = el('aqm-c3-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c3-erro').forEach(function (n) { n.classList.remove('aqm-c3-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c3-' + er.campo);
				if (campo) { campo.classList.add('aqm-c3-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c3-oculto');
			return;
		}

		alvo.classList.remove('aqm-c3-oculto');

		el('aqm-c3-faixa-valor').innerHTML = lh(r.piso) + ' a ' + lh(r.teto) + '<span class="aqm-c3-unidade">L/h</span>';
		el('aqm-c3-faixa-criterio').textContent =
			'Do piso ao teto: ' + fmt(FABRICANTE_XH, 2) + ' renovações por hora, que é o que o próprio fabricante dimensiona, até '
			+ fmt(r.teto_xh, 0) + ' renovações por hora, que é o teto da regra de bolso brasileira para aquário '
			+ (r.entradas.perfil === 'plantado' ? 'plantado' : 'comunitário') + '. '
			+ 'A faixa é larga porque as fontes discordam em ' + fmt(r.razao, 1) + ' vezes — e essa discordância é o resultado, não um defeito dele.';

		var lista = el('aqm-c3-bandas');
		lista.innerHTML = '';

		lista.appendChild(cartao(
			'Piso do fabricante',
			lh(r.piso) + '<span class="aqm-c3-unidade">L/h</span>',
			'O Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 L: são ' + fmt(FABRICANTE_XH, 2)
			+ ' renovações por hora. Aplicado ao seu volume, dá este número. É o único extremo da faixa que vem de quem fabrica o filtro.'
		));

		r.bandas.forEach(function (b) {
			lista.appendChild(cartao(
				b.rotulo + ' (' + fmt(b.xh[0], 0) + ' a ' + fmt(b.xh[1], 0) + ' x/h)',
				lh(b.min) + ' a ' + lh(b.max) + '<span class="aqm-c3-unidade">L/h</span>',
				'Regra repetida por ' + b.fonte + ', do nosso levantamento de setembro de 2026. '
				+ 'Nenhuma das fontes brasileiras explica de onde saiu o número nem confronta o dimensionamento do fabricante.'
			));
		});

		if (r.sump_L) {
			lista.appendChild(cartao(
				'Volume mínimo do sump',
				litros(r.sump_L) + '<span class="aqm-c3-unidade">L</span>',
				SUMP_PCT + ' % do volume do aquário, mínimo repetido pela AquaOnline. É a única constante de sump que o levantamento trouxe: '
				+ 'turnover de aquário marinho não tem fonte no nosso corpus, então esta calculadora não publica um.'
			));
		}

		var pos = { leve: ['o piso', r.bolso.min], media: ['o meio', (r.bolso.min + r.bolso.max) / 2], pesada: ['o topo', r.bolso.max] };
		var escolha = pos[r.entradas.carga] || pos.media;
		el('aqm-c3-carga-nota').innerHTML =
			'<strong>Com a carga de peixes que você informou, mire ' + escolha[0] + ' da faixa de bolso: cerca de '
			+ lh(escolha[1]) + ' L/h.</strong> Onde mirar dentro de uma faixa publicada é convenção da Aquametria, não constante com fonte — '
			+ 'os números dos extremos têm origem; a posição dentro deles é critério editorial, e está declarado.';

		var av = el('aqm-c3-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		pintarProdutos(r);

		el('aqm-c3-citacao').textContent =
			'Aquário de ' + litros(r.entradas.volume) + ' L de água real, perfil '
			+ (r.entradas.perfil === 'plantado' ? 'plantado' : 'comunitário') + ': a vazão de filtro pedida vai de '
			+ lh(r.piso) + ' a ' + lh(r.teto) + ' L/h, conforme a fonte — ' + fmt(FABRICANTE_XH, 2)
			+ ' renovações por hora pelo dimensionamento do fabricante, até ' + fmt(r.teto_xh, 0)
			+ ' pela regra de bolso brasileira. Calculado pela Aquametria, ' + AQM_C3_DATA + '.';

		guardar(r);
		atualizarEndereco(r.entradas);
	}

	function cartao(rotulo, valor, criterio) {
		var li = document.createElement('li');
		li.className = 'aqm-c3-cartao';
		var r = document.createElement('span');
		r.className = 'aqm-c3-rotulo';
		r.textContent = rotulo;
		var v = document.createElement('span');
		v.className = 'aqm-c3-valor';
		v.innerHTML = valor;
		var c = document.createElement('p');
		c.className = 'aqm-c3-criterio';
		c.textContent = criterio;
		li.appendChild(r); li.appendChild(v); li.appendChild(c);
		return li;
	}

	/* ------------------------------------------------------------- produtos */

	function pintarProdutos(r) {
		var bloco = el('aqm-c3-produtos');
		var lista = el('aqm-c3-produtos-lista');
		var nada = el('aqm-c3-produtos-nada');
		lista.innerHTML = '';

		if (!r.produtos.length) {
			bloco.classList.add('aqm-c3-oculto');
			nada.classList.remove('aqm-c3-oculto');
			nada.textContent = 'Nenhum filtro do nosso banco entrega entre ' + lh(r.piso) + ' e ' + lh(r.teto)
				+ ' L/h com ficha técnica conferida'
				+ (r.entradas.tipo !== 'qualquer' ? ' no tipo que você escolheu' : '')
				+ (r.barrados_por_coluna.length ? ', e ' + r.barrados_por_coluna.length + ' modelo(s) foram barrados pela altura da coluna' : '')
				+ '. O banco tem ' + AQM_C3_CATALOGO.length + ' filtro(s) com ficha completa hoje e cresce a cada coleta. '
				+ 'Preferimos não mostrar produto nenhum a mostrar um que não atende o seu número.';
			return;
		}

		nada.classList.add('aqm-c3-oculto');
		bloco.classList.remove('aqm-c3-oculto');
		el('aqm-c3-produtos-sub').textContent =
			'São os filtros do nosso banco cuja vazão declarada cai dentro da faixa que o seu aquário pede — '
			+ lh(r.piso) + ' a ' + lh(r.teto) + ' L/h. A ordem é por proximidade do meio da faixa. '
			+ 'Nada aqui é ordenado por comissão, e produto sem link de loja aparece do mesmo jeito.';

		r.produtos.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r));
		});

		if (r.barrados_por_coluna.length) {
			var li = document.createElement('li');
			li.className = 'aqm-c3-criterio';
			li.textContent = 'Fora da lista pela coluna: ' + r.barrados_por_coluna.join(' ');
			lista.appendChild(li);
		}
	}

	function produtoHtml(p, r) {
		var V = r.entradas.volume;
		var turno = p.vazao_lh / V;

		var li = document.createElement('li');
		li.className = 'aqm-c3-produto';

		var placa = document.createElement('div');
		placa.className = 'aqm-c3-placa';
		placa.innerHTML = '<span class="aqm-c3-marca">' + esc(p.marca) + '</span>'
			+ '<span class="aqm-c3-numero">' + lh(p.vazao_lh) + '</span>'
			+ '<span class="aqm-c3-un">L/h nominais</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = p.marca + ' ' + p.modelo;
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c3-porque';
		porque.innerHTML = 'No seu aquário de ' + litros(V) + ' L, este filtro entrega <strong>'
			+ fmt(Math.round(turno * 10) / 10, 1) + ' renovações por hora</strong>. '
			+ (p.volume_max_L
				? 'O fabricante declara que ele atende até ' + litros(p.volume_max_L) + ' L'
					+ (p.volume_max_L >= V
						? ' — o seu volume cabe nessa declaração.'
						: ' — o seu volume passa disso, e a declaração do fabricante não cobre o seu caso.')
				: 'O fabricante não declara volume atendido para este modelo.');
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c3-ficha';
		var linhas = [
			'Tipo: <b>' + esc(p.tipo) + '</b>',
			'Potência: <b>' + fmt(p.potencia_w, 0) + ' W</b>',
			(p.coluna_na
				? 'Coluna máxima: <b>não se aplica</b> (hang-on fica na borda do aquário)'
				: (p.coluna_m !== null ? 'Coluna máxima: <b>' + fmt(p.coluna_m, 1) + ' m</b>' : 'Coluna máxima: <b>não declarada</b>')),
			'Voltagem: <b>' + (p.voltagem.length ? p.voltagem.join(' ou ') + ' V' : 'não declarada') + '</b>'
		];
		if (p.uv_w) { linhas.push('UV embutido: <b>' + fmt(p.uv_w, 0) + ' W</b>'); }
		if (p.midia.length) { linhas.push('Mídia inclusa: ' + esc(p.midia.join(', '))); }
		linhas.push('Ficha conferida em ' + esc(dataBr(p.verificado_em))
			+ (p.fonte_url ? ' — <a href="' + esc(p.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (p.fonte_status ? ' (' + esc(p.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (p.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c3-loja';
			a.href = p.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja);
			corpo.appendChild(a);
			var nota = document.createElement('p');
			nota.className = 'aqm-c3-semloja';
			nota.textContent = 'Link patrocinado. Confira no anúncio a voltagem e o modelo exato antes de comprar — '
				+ 'o anúncio não é nossa fonte técnica, e a ficha acima é.';
			corpo.appendChild(nota);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c3-semloja';
			sem.textContent = 'Ainda não temos link de loja para este modelo. Ele aparece aqui porque atende ao seu número, e é só isso que decide a lista.';
			corpo.appendChild(sem);
		}

		li.appendChild(placa);
		li.appendChild(corpo);
		return li;
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
	   pode apagar o que ela gravou. Só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c3-vazao-filtro' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.entradas.volume) {
			estado.volumes.real_L = r.entradas.volume;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C3'; }
		}
		estado.perfil = estado.perfil || {};
		estado.perfil.tipo_aquario = r.entradas.perfil;
		estado.perfil.carga_peixes = r.entradas.carga;
		estado.perfil.tem_sump = !!r.entradas.sump;
		estado.equipamentos = estado.equipamentos || {};
		estado.equipamentos.filtro_coluna_m = r.entradas.coluna;
		estado.equipamentos.filtro_vazao_alvo_lh = [Math.round(r.piso), Math.round(r.teto)];
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c3-guardado').classList.remove('aqm-c3-oculto');
		} catch (erro) {
			el('aqm-c3-guardado').classList.add('aqm-c3-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'p=' + d.perfil, 'cg=' + d.carga, 't=' + d.tipo];
		if (d.coluna !== null) { q.push('col=' + d.coluna); }
		if (d.sump) { q.push('sump=1'); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c3-link').value = window.location.origin + url;
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

	/* ------------------------------------- o filtro que a pessoa já tem */

	function veredito() {
		var q = num(el('aqm-c3-tenho').value);
		var V = num(el('aqm-c3-volume').value);
		var saida = el('aqm-c3-tenho-saida');

		if (q === null || q <= 0) {
			saida.textContent = 'Informe a vazão nominal do filtro, em litros por hora — é o número que vem na caixa.';
			return;
		}

		var texto = 'Um filtro de ' + lh(q) + ' L/h cobre ';
		var partes = [];
		partes.push('até ' + litros(q / FABRICANTE_XH) + ' L pelo dimensionamento do fabricante (' + fmt(FABRICANTE_XH, 2) + ' x/h)');
		var perfil = el('aqm-c3-perfil').value === 'plantado' ? 'plantado' : 'comunitario';
		BANDAS[perfil].forEach(function (b) {
			partes.push('de ' + litros(q / b.faixa[1]) + ' a ' + litros(q / b.faixa[0]) + ' L pela ' + b.curto
				+ ' (' + fmt(b.faixa[0], 0) + ' a ' + fmt(b.faixa[1], 0) + ' x/h)');
		});
		texto += partes.join('; ') + '. ';

		if (V !== null && V > 0) {
			var t = q / V;
			texto += 'No seu aquário de ' + litros(V) + ' L, ele entrega ' + fmt(Math.round(t * 10) / 10, 1) + ' renovações por hora — '
				+ (t < FABRICANTE_XH
					? 'abaixo até do que o fabricante do 2213 considera suficiente.'
					: (t < BANDAS[perfil][BANDAS[perfil].length - 1].faixa[0]
						? 'acima do dimensionamento do fabricante e abaixo do que as regras de bolso brasileiras pedem. É exatamente a faixa onde as fontes discordam.'
						: 'dentro do que as regras de bolso brasileiras pedem.'));
		}
		texto += ' Vazão nominal é medida sem mídia e a coluna zero: no seu aquário, com o cesto cheio, chega menos que isso.';
		saida.textContent = texto;
	}

	/* ---------------------------------------------------------- ligações */

	function preencher(fora) {
		if (fora.v) { el('aqm-c3-volume').value = fora.v; }
		if (fora.p === 'plantado' || fora.p === 'comunitario') { el('aqm-c3-perfil').value = fora.p; }
		if (fora.cg) { el('aqm-c3-carga').value = fora.cg; }
		if (fora.t) { el('aqm-c3-tipo').value = fora.t; }
		if (fora.col) { el('aqm-c3-coluna').value = fora.col; }
		if (fora.sump === '1') { el('aqm-c3-sump').checked = true; }
	}

	el('aqm-c3-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
	});

	el('aqm-c3-limpar').addEventListener('click', function () {
		el('aqm-c3-form').reset();
		el('aqm-c3-saida').classList.add('aqm-c3-oculto');
		el('aqm-c3-erros').innerHTML = '';
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c3-copiar').addEventListener('click', function () {
		var campo = el('aqm-c3-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c3-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c3-tenho-calcular').addEventListener('click', veredito);

	/* Query string manda; senão, o aquário que a C1 guardou neste navegador. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		pintar(calcular(campos()));
	} else {
		var guardadoAntes = recuperar();
		var volume = guardadoAntes && guardadoAntes.volumes ? guardadoAntes.volumes.real_L : null;
		if (volume) {
			el('aqm-c3-volume').value = String(volume).replace('.', ',');
			var perfilGuardado = (guardadoAntes.perfil || {}).tipo_aquario;
			if (perfilGuardado === 'plantado' || perfilGuardado === 'plantado-low-tech') {
				el('aqm-c3-perfil').value = 'plantado';
			}
			if ((guardadoAntes.perfil || {}).carga_peixes) {
				el('aqm-c3-carga').value = guardadoAntes.perfil.carga_peixes;
			}
			var retomado = el('aqm-c3-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que a calculadora de litragem guardou neste navegador.';
			retomado.classList.remove('aqm-c3-oculto');
			pintar(calcular(campos()));
		} else {
			el('aqm-c3-semvolume').classList.remove('aqm-c3-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_form_html' ) ) {
function aquametria_c3_form_html() {
	$c1 = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-litragem' ) : home_url( '/calculadora-de-litragem/' );

	$h  = '<form id="aqm-c3-form" class="aqm-c3-painel" novalidate>';
	$h .= '<h3>O seu aquário</h3>';
	$h .= '<p class="aqm-c3-sub">Se você já usou a calculadora de litragem neste navegador, o volume vem preenchido daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c3-grade">';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c3-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c3-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-perfil">Perfil do aquário</label>';
	$h .= '<select id="aqm-c3-perfil" name="perfil">';
	$h .= '<option value="comunitario">comunitário (peixes, pouca planta)</option>';
	$h .= '<option value="plantado">plantado</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Marinho não está aqui: o nosso levantamento não trouxe turnover de marinho com fonte.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-carga">Carga de peixes</label>';
	$h .= '<select id="aqm-c3-carga" name="carga">';
	$h .= '<option value="leve">leve (poucos peixes pequenos)</option>';
	$h .= '<option value="media" selected>média</option>';
	$h .= '<option value="pesada">pesada (peixes grandes ou aquário cheio)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Move a mira dentro da faixa, não a faixa.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-coluna">Altura da coluna (m)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c3-coluna" name="coluna" placeholder="ex.: 0,8">';
	$h .= '<span class="aqm-c3-dica">Do filtro até a superfície da água. Só importa para canister e sump; em branco, não filtramos por coluna.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-tipo">Tipo de filtro</label>';
	$h .= '<select id="aqm-c3-tipo" name="tipo">';
	$h .= '<option value="qualquer">tanto faz</option>';
	$h .= '<option value="canister">canister</option>';
	$h .= '<option value="hang-on">hang-on (cascata)</option>';
	$h .= '<option value="interno">interno</option>';
	$h .= '<option value="sump">sump</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Filtra a lista de produtos, não o cálculo.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c3-caixa"><input type="checkbox" id="aqm-c3-sump"> <span>Tenho ou vou ter sump — quero também o volume mínimo dele</span></label>';

	$h .= '<div class="aqm-c3-botoes">';
	$h .= '<button type="submit">Calcular a vazão</button>';
	$h .= '<button type="button" class="aqm-c3-secundario" id="aqm-c3-limpar">Limpar</button>';
	$h .= '<span class="aqm-c3-dica aqm-c3-oculto" id="aqm-c3-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c3-avisos" id="aqm-c3-erros"></ul>';
	$h .= '<p class="aqm-c3-criterio aqm-c3-oculto" id="aqm-c3-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre e as rochas tiram uma parte. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_resposta_html' ) ) {
function aquametria_c3_resposta_html() {
	$h  = '<div class="aqm-c3-resultado aqm-c3-oculto" id="aqm-c3-saida" aria-live="polite">';

	$h .= '<div class="aqm-c3-faixa">';
	$h .= '<span class="aqm-c3-rotulo">Vazão nominal que o seu aquário pede</span>';
	$h .= '<span class="aqm-c3-valor" id="aqm-c3-faixa-valor">—</span>';
	$h .= '<p class="aqm-c3-criterio" id="aqm-c3-faixa-criterio"></p>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c3-cartoes" id="aqm-c3-bandas"></ul>';

	$h .= '<p class="aqm-c3-nota" id="aqm-c3-carga-nota"></p>';

	$h .= '<ul class="aqm-c3-avisos" id="aqm-c3-avisos"></ul>';

	$h .= '<p class="aqm-c3-nota aqm-c3-nota-alerta"><strong>Vazão nominal não é a vazão que chega ao seu aquário.</strong> ';
	$h .= 'O número da caixa é medido sem mídia dentro do filtro e com a bomba na altura da água. No seu móvel, com o cesto cheio e a mangueira subindo, chega menos. ';
	$h .= 'Quanto menos, nós não publicamos: não existe fator de perda com fonte no nosso levantamento, e constante sem origem é proibida aqui. ';
	$h .= 'O que existe é medição sua: com o filtro ligado, aponte a saída para um balde de volume conhecido e cronometre. Vazão real em L/h = volume do balde em litros ÷ tempo em horas — ';
	$h .= '10 litros em 45 segundos são 800 L/h. Vale mais que qualquer número de catálogo, inclusive o nosso.</p>';

	$h .= aquametria_c3_produtos_html();

	$h .= '<div class="aqm-c3-citar">';
	$h .= '<p id="aqm-c3-citacao"></p>';
	$h .= '<div class="aqm-c3-campo"><label for="aqm-c3-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c3-link" readonly></div>';
	$h .= '<div class="aqm-c3-botoes"><button type="button" class="aqm-c3-secundario" id="aqm-c3-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c3-dica" id="aqm-c3-copiado"></span></div>';
	$h .= '<p class="aqm-c3-dica" id="aqm-c3-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_produtos_html' ) ) {
function aquametria_c3_produtos_html() {
	$divulgacao = function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS )
		: home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );

	$h  = '<div class="aqm-c3-produtos aqm-c3-painel aqm-c3-oculto" id="aqm-c3-produtos">';
	$h .= '<h3>Filtros que atendem essa faixa</h3>';
	$h .= '<p class="aqm-c3-sub" id="aqm-c3-produtos-sub"></p>';
	$h .= '<ul class="aqm-c3-lista" id="aqm-c3-produtos-lista"></ul>';
	$h .= '<p class="aqm-c3-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista nem em que ordem — a ordem é pela vazão mais próxima do meio da faixa que o seu aquário pede, e modelo sem link aparece do mesmo jeito. ';
	$h .= 'A ficha técnica de cada filtro vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'Também não publicamos preço nesta página: preço muda toda semana e um número velho na tela seria pior que nenhum. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c3-nota aqm-c3-oculto" id="aqm-c3-produtos-nada"></p>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_tenho_html' ) ) {
function aquametria_c3_tenho_html() {
	$h  = '<div class="aqm-c3-painel">';
	$h .= '<h3>Caminho inverso: o filtro que eu já tenho serve?</h3>';
	$h .= '<p class="aqm-c3-sub">Informe a vazão que vem na caixa e devolvemos até quantos litros ele cobre por cada critério — e, se o volume estiver preenchido acima, quantas renovações por hora ele entrega no seu aquário.</p>';
	$h .= '<div class="aqm-c3-grade">';
	$h .= '<div class="aqm-c3-campo"><label for="aqm-c3-tenho">Vazão do filtro (L/h)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c3-tenho" placeholder="1000"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c3-botoes"><button type="button" id="aqm-c3-tenho-calcular">Ver o que ele cobre</button></div>';
	$h .= '<p class="aqm-c3-criterio" id="aqm-c3-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_fontes_html' ) ) {
function aquametria_c3_fontes_html() {
	$h  = '<div class="aqm-c3-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c3-sub">Verificado em ' . esc_html( AQUAMETRIA_C3_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C3_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c3-rolagem"><table class="aqm-c3-fontes">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>eheim-classic-250-2213</td><td>' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' x/h</td>';
	$h .= '<td>O Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 L. A divisão dá 1,76 renovações por hora — o piso da faixa, e o único extremo que vem de quem fabrica filtro. ';
	$h .= 'Ficha coletada em 07/09/2026 <span class="aqm-c3-selo">fabricante via busca</span>: a página do fabricante não foi lida direto, reconferir no manual.</td></tr>';

	$h .= '<tr><td>turnover-comunitario-br</td><td>5 a 10 x/h</td>';
	$h .= '<td>Regra repetida por Aquarismo Paulista e AquaOnline, do levantamento de 04/09/2026 <span class="aqm-c3-selo">divergente entre fontes BR</span>. ';
	$h .= 'Nenhuma das duas explica a origem do número nem cita o dimensionamento do fabricante.</td></tr>';

	$h .= '<tr><td>turnover-comunitario-mybest</td><td>4 a 5 x/h</td>';
	$h .= '<td>Leitura conservadora da mesma pergunta, publicada pela my-best BR <span class="aqm-c3-selo">divergente entre fontes BR</span>. Está aqui porque discorda da anterior, e a discordância é o conteúdo.</td></tr>';

	$h .= '<tr><td>turnover-plantado</td><td>3 a 5 x/h</td>';
	$h .= '<td>AquaPeixes, para aquário plantado <span class="aqm-c3-selo">divergente entre fontes BR</span>. Corrente mais lenta é o argumento repetido; nenhuma fonte publica a medição que sustentaria o número.</td></tr>';

	$h .= '<tr><td>sump-proporcao-minima</td><td>' . esc_html( AQUAMETRIA_C3_SUMP_PCT ) . ' % do volume</td>';
	$h .= '<td>Mínimo repetido pela AquaOnline <span class="aqm-c3-selo">divergente entre fontes BR</span>. É a única constante de sump do levantamento.</td></tr>';

	$h .= '<tr><td>fator de perda de carga</td><td>sem valor <span class="aqm-c3-selo">pendente</span></td>';
	$h .= '<td>Quanto a vazão cai com mídia e coluna. Nenhuma fonte brasileira do levantamento publica, e o fabricante só declara a coluna máxima. Sem fonte, esta calculadora não aplica fator nenhum e entrega o protocolo do balde no lugar.</td></tr>';

	$h .= '<tr><td>turnover marinho</td><td>sem valor <span class="aqm-c3-selo">pendente</span></td>';
	$h .= '<td>O levantamento não trouxe turnover de aquário marinho com fonte brasileira. Por isso o perfil não está no formulário: quem tem sump recebe o volume mínimo dele, que tem fonte, e nada além disso.</td></tr>';

	$h .= '</table></div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_adiante_html' ) ) {
function aquametria_c3_adiante_html() {
	$hub   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadoras' ) : home_url( '/calculadoras/' );
	$meto  = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'metodologia' ) : home_url( '/metodologia/' );
	$c1    = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-litragem' ) : home_url( '/calculadora-de-litragem/' );
	$divul = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS ) : home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );
	$c5    = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-potencia-do-aquecedor' ) : home_url( '/calculadora-de-potencia-do-aquecedor/' );
	$c12   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-midia-filtrante' ) : home_url( '/calculadora-de-midia-filtrante/' );
	$c15   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-iluminacao' ) : home_url( '/calculadora-de-iluminacao/' );

	$h  = '<div class="aqm-c3-painel aqm-c3-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vem o volume real que esta página usa. Se o número acima veio preenchido, veio de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c5 ) . '"><strong>Potência do aquecedor (C5)</strong></a> — o outro aparelho que o seu volume dimensiona, e o único que pergunta quanto frio faz no seu cômodo. Usa o mesmo volume real desta página.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — quantos mililitros de mídia biológica o seu filtro precisa carregar, e se isso cabe no cesto dele. Usa o mesmo volume e o mesmo modelo de filtro que você escolheu aqui. A água precisa passar, e precisa passar por alguma coisa: vazão e mídia são as duas metades da mesma decisão.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — o mesmo volume, do outro lado do aquário. Se o seu é plantado, a faixa de vazão desta página já é mais lenta por causa disso: planta quer corrente suave, e luz forte com CO2 pede que o gás não escape na superfície agitada.</li>';
	$h .= '<li><strong>Consumo elétrico (C7)</strong> — o filtro fica ligado 24 horas por dia, e é ele que pesa na conta. Vai ler a potência do modelo escolhido aqui. Ainda em construção.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com duas fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c3-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
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

if ( ! function_exists( 'aquametria_c3_estilo_impresso' ) ) {
function aquametria_c3_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c3_pagina_usa' ) ) {
function aquametria_c3_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_vazao' );
}
}

if ( ! function_exists( 'aquametria_c3_imprimir_estilo' ) ) {
function aquametria_c3_imprimir_estilo() {
	if ( aquametria_c3_estilo_impresso() ) {
		return;
	}
	aquametria_c3_estilo_impresso( true );
	echo '<style id="aquametria-c3-estilo">' . "\n" . aquametria_c3_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c3_cabeca' ) ) {
function aquametria_c3_cabeca() {
	if ( ! aquametria_c3_pagina_usa() ) {
		return;
	}
	aquametria_c3_imprimir_estilo();
}
}
add_action( 'wp_head', 'aquametria_c3_cabeca', 20 );

if ( ! function_exists( 'aquametria_c3_rodape' ) ) {
function aquametria_c3_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c3_imprimir_estilo();

	$js  = 'var AQM_C3_DATA = ' . wp_json_encode( AQUAMETRIA_C3_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C3_CATALOGO = ' . wp_json_encode( array_values( aquametria_c3_catalogo() ) ) . ";\n";
	$js .= aquametria_c3_js();
	echo '<script id="aquametria-c3-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 7. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_shortcode' ) ) {
function aquametria_c3_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c3_rodape', 20 );

	$h  = '<div class="aqm-c3">';
	$h .= aquametria_c3_form_html();
	$h .= aquametria_c3_resposta_html();
	$h .= aquametria_c3_tenho_html();
	$h .= aquametria_c3_fontes_html();
	$h .= aquametria_c3_adiante_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_vazao', 'aquametria_c3_shortcode' );

/**
 * Aquametria Calculadora de Potência do Aquecedor — C5
 * Versão: 1.0.2 (08/09/2026) — o painel de ligações passou a linkar a C15, publicada nesta data.
 * A 1.0.1 linkou a C12, publicada no mesmo dia
 *
 * Terceira calculadora do lote e a primeira que pergunta uma coisa que nenhuma
 * fonte brasileira do nosso levantamento pergunta: quanto frio faz onde o
 * aquário está. Toda a web repete "1 W por litro" sem dizer para qual diferença
 * de temperatura o número vale — e um aquário a 26 °C num quarto que cai a
 * 22 °C não é o mesmo problema que o mesmo aquário num quarto que cai a 12 °C.
 * Este é o vácuo de conteúdo nº 2 do levantamento do Bloco 1.
 *
 * Registra o shortcode [aquametria_calculadora_aquecedor] e se anuncia no hub
 * pelo filtro 'aquametria_calculadoras' da casca.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem, então HTML que dependesse da query string seria
 * servido errado para o visitante seguinte. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não publica o cálculo físico P = U · A · ΔT. Falta a constante
 *   'u-vidro-aquario' (status pendente): o coeficiente global de troca do vidro
 *   com convecção natural nas duas faces, mais a perda por evaporação na lâmina
 *   livre, que costuma dominar. Sem fonte, não sai. É a via B da especificação,
 *   e vale um bloco próprio — quando sair, esta página deixa de depender de
 *   regra de bolso e passa a ser a única do nicho no Brasil com física atrás.
 * - Não corrige a potência por aquário tampado ou destampado. A perda pela
 *   lâmina livre é justamente a parcela que a constante pendente cobriria.
 *   O campo existe no formulário e muda o TEXTO, nunca o número: dizer "some
 *   20 % se for destampado" seria inventar constante, e aqui isso é proibido.
 * - Não usa temperatura mínima por cidade. A constante
 *   'temperatura-minima-por-cidade' também está pendente (a coleta prevista é a
 *   Normal Climatológica do INMET 1991-2020). Enquanto não houver a tabela, a
 *   mínima é entrada da pessoa, que é quem sabe quanto esfria no cômodo dela.
 * - Não extrapola regra de bolso para ΔT acima de 10 °C. A única fonte do corpus
 *   que amarrou W/L a um delta declarou até 10 °C. Passou disso, a tela diz com
 *   essas palavras que nenhuma fonte cobre o caso.
 *
 * Bloco de produto: os aquecedores vêm do catálogo embutido mais abaixo, gerado
 * por ferramentas/gerar-catalogo-aquecedores.py a partir de
 * dados/produtos-aquecedor.json. Mexeu no banco, rode o gerador. A ordem é por
 * adequação técnica; link de afiliado não ordena nem filtra (regra V16). Duas
 * barreiras de segurança vêm antes de tudo: a voltagem da tomada (aquecedor na
 * voltagem errada queima) e a faixa de ajuste alcançar a temperatura-alvo
 * (regra V18). Preço não entra: snippet é estático e preço envelhece na tela.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C5_VERSAO' ) ) {
	define( 'AQUAMETRIA_C5_VERSAO', '1.0.2' );
	define( 'AQUAMETRIA_C5_SLUG', 'calculadora-de-potencia-do-aquecedor' );
	define( 'AQUAMETRIA_C5_VERIFICADO_EM', '08/09/2026' );
	define( 'AQUAMETRIA_C5_ARTIGO', 'quantos-watts-de-aquecedor-para-aquario' );
	define( 'AQUAMETRIA_C5_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
	/* Constante 'wl-delta-ate-10' (ReefFlow): a ÚNICA do corpus que amarra
	   W/L a uma diferença de temperatura declarada. Vale até 10 °C. */
	define( 'AQUAMETRIA_C5_DELTA_COBERTO', 10 );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_registrar_no_hub' ) ) {
function aquametria_c5_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C5' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C5_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c5_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Catálogo de aquecedores
 *
 * NÃO EDITE À MÃO o trecho entre os marcadores. Ele é a cópia, dentro do
 * snippet, do que dados/produtos-aquecedor.json já tem — porque o site não lê o
 * repositório em tempo de execução. Depois de mexer no banco:
 *
 *     python3 ferramentas/gerar-catalogo-aquecedores.py
 *
 * Entra no catálogo quem o validador considera apto a ser sugerido pela C5
 * (minimo_para_sugerir do esquema) e não está em rascunho nem em revalidar.
 * O campo ajuste_conservador marca quem chegou aqui pela regra V17: a faixa de
 * ajuste é a interseção das fontes em conflito, e a tela diz isso.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_catalogo' ) ) {
function aquametria_c5_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-aquecedores.py */
	return array(
		array(
			'id' => 'roxin-ht-1300-q3-25w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 25 W',
			'tipo' => 'quartzo',
			'potencia_w' => 25,
			'volume_min_L' => 20,
			'volume_max_L' => 35,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => 23.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'WorldFish e AquaMaeda (varejo BR), fichas do HT-1300/Q3 25 W (20 a 35 L, 2,3 x 23 cm, cabo de 90 cm, IP68)',
			'fonte_url' => 'https://worldfish.com.br/produtos/termostato-com-aquecedor-roxin-ht-1300-q3-25w-110v/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
		),
		array(
			'id' => 'eheim-jager-50w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 50 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 50,
			'volume_min_L' => 25,
			'volume_max_L' => 50,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 25.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-50w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 50 W',
			'tipo' => 'quartzo',
			'potencia_w' => 50,
			'volume_min_L' => 40,
			'volume_max_L' => 60,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => 23.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'WorldFish e AquaMaeda (varejo BR), fichas do HT-1300/Q3 50 W (40 a 60 L, 2,3 x 23 cm, cabo de 90 cm, IP68)',
			'fonte_url' => 'https://worldfish.com.br/produtos/termostato-com-aquecedor-roxin-ht-1300-q3-50w-220v/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
		),
		array(
			'id' => 'eheim-jager-100w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 100 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 100,
			'volume_min_L' => 75,
			'volume_max_L' => 100,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 32.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-100w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 100 W',
			'tipo' => 'quartzo',
			'potencia_w' => 100,
			'volume_min_L' => 50,
			'volume_max_L' => 150,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Mega Aquarios e RS Discus (varejo BR especializado), fichas do HT-1300/Q3 100 W',
			'fonte_url' => 'https://www.megaaquarios.com.br/termostato-aquecedor-roxin-q3-100w-termometro-aquario.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/50YsvKBY0s',
			'anuncio' => 'ROXIN HT-1300 Q3 100W 127V para aquario ate 100 litros',
			'voltagem_anuncio' => '127',
			'loja' => 'shopee',
			'conflito_volume' => null,
		),
		array(
			'id' => 'eheim-jager-150w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 150 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 150,
			'volume_min_L' => 125,
			'volume_max_L' => 150,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 35.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => '125 a 150 L segundo tabela da linha Jager no varejo europeu/americano (Aquaeden, Top Corals); 200 a 300 L segundo Agrosete (varejo BR), ficha do Eheim 150 W 220 V',
		),
		array(
			'id' => 'eheim-jager-200w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 200 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 200,
			'volume_min_L' => 30,
			'volume_max_L' => 400,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 41.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Eheim, linha Jager (25 a 300 W, 9 tamanhos, 20 a 1000 L; ajuste 18 a 34 C com precisao de 0,5 C; 200 W declarado para 30 a 400 L, 400 mm de comprimento, 24,5 mm de diametro, cabo de 170 cm, vidro Schott DURAN, desliga fora d\'agua); mesma coleta que gerou a constante eheim-jager-dimensionamento do Bloco 2',
			'fonte_url' => 'https://eheim.com/en_GB/products/technology/heating/thermocontrol/jager',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => '30 a 400 L segundo catalogo do proprio fabricante (Eheim), linha Jager; 300 a 400 L segundo varejo BR e tabela de varejo da linha (Pata Mania, Aquaeden, Top Corals)',
		),
		array(
			'id' => 'roxin-ht-1300-q3-200w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 200 W',
			'tipo' => 'quartzo',
			'potencia_w' => 200,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Petlove e Fundo do Mar Aquarios (varejo BR), ficha do HT-1300 200 W',
			'fonte_url' => 'https://www.petlove.com.br/termostato-com-aquecedor-roxin-ht-1300-200w/p',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/6L4GVnErqJ',
			'anuncio' => 'Roxin Q3 Ht-1300 Q3 200w 110V',
			'voltagem_anuncio' => '110',
			'loja' => 'shopee',
			'conflito_volume' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-300w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 300 W',
			'tipo' => 'quartzo',
			'potencia_w' => 300,
			'volume_min_L' => 250,
			'volume_max_L' => 350,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Mega Aquarios (varejo BR especializado), ficha do Q3 300 W',
			'fonte_url' => 'https://www.megaaquarios.com.br/termostato-aquecedor-roxin-300w-termometro-aquario.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/AUtpTbdMqc',
			'anuncio' => 'Termostato Com Aquecedor Roxin HT-1300 - Q3 - 300w - 220v',
			'voltagem_anuncio' => '220',
			'loja' => 'shopee',
			'conflito_volume' => null,
		),
	);
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_css' ) ) {
function aquametria_c5_css() {
	return <<<'CSS'
.aqm-c5{--c5-tinta:var(--aqm-tinta,#0D1B22);--c5-lamina:var(--aqm-lamina,#0E7C8C);
--c5-papel:var(--aqm-papel,#F4F7F7);--c5-superficie:var(--aqm-superficie,#FFFFFF);
--c5-traco:var(--aqm-traco,#DDE5E6);--c5-legenda:var(--aqm-legenda,#5C7075);
--c5-alerta:var(--aqm-alerta,#B5762A);
--c5-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c5-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c5-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c5-texto);color:var(--c5-tinta);}
.aqm-c5 *{box-sizing:border-box;}
.aqm-c5 form{margin:0;}
.aqm-c5-painel{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c5-painel h3{font-family:var(--c5-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c5-painel .aqm-c5-sub{color:var(--c5-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c5-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.9rem;}
.aqm-c5-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c5-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c5-campo .aqm-c5-dica{font-size:.74rem;color:var(--c5-legenda);line-height:1.35;}
.aqm-c5 input[type=text],.aqm-c5 select{width:100%;font-family:var(--c5-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c5-traco);border-radius:2px;background:var(--c5-superficie);color:var(--c5-tinta);}
.aqm-c5 select{font-family:var(--c5-texto);}
.aqm-c5 input:focus,.aqm-c5 select:focus{outline:2px solid var(--c5-lamina);outline-offset:1px;}
.aqm-c5 input.aqm-c5-erro{border-color:var(--c5-alerta);}
.aqm-c5-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c5-caixa input{margin-top:.2rem;}
.aqm-c5-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c5 button{font-family:var(--c5-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c5-lamina);color:var(--c5-superficie);cursor:pointer;}
.aqm-c5 button.aqm-c5-secundario{background:transparent;color:var(--c5-lamina);border:1px solid var(--c5-traco);}
.aqm-c5 button:hover{filter:brightness(1.08);}
.aqm-c5-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c5-avisos li{font-size:.88rem;color:var(--c5-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c5-resultado{margin:0 0 1.2rem;}
.aqm-c5-faixa{background:var(--c5-superficie);border:2px solid var(--c5-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c5-rotulo{font-family:var(--c5-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c5-legenda);}
.aqm-c5-valor{font-family:var(--c5-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c5-valor .aqm-c5-unidade{font-size:.95rem;font-weight:500;color:var(--c5-legenda);margin-left:.3rem;}
.aqm-c5-criterio{font-size:.83rem;color:var(--c5-legenda);line-height:1.5;margin:0;}
.aqm-c5-delta{display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:baseline;margin:.6rem 0 0;font-family:var(--c5-mono);font-size:.86rem;color:var(--c5-legenda);}
.aqm-c5-delta b{color:var(--c5-tinta);font-weight:600;}
.aqm-c5-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c5-cartao{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c5-cartao .aqm-c5-valor{font-size:1.5rem;}
.aqm-c5-cartao.aqm-c5-cartao-fora{border-style:dashed;border-color:var(--c5-alerta);}
.aqm-c5-nota{border-left:3px solid var(--c5-lamina);background:var(--c5-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c5-legenda);margin:0 0 1rem;}
.aqm-c5-nota strong{color:var(--c5-tinta);}
.aqm-c5-nota.aqm-c5-nota-alerta{border-left-color:var(--c5-alerta);}
.aqm-c5-produtos{margin:0 0 1.2rem;}
.aqm-c5-produtos h3{font-family:var(--c5-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c5-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c5-produto{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c5-placa{background:var(--c5-papel);border:1px solid var(--c5-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c5-placa .aqm-c5-marca{font-family:var(--c5-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c5-placa .aqm-c5-numero{font-family:var(--c5-mono);font-size:1.15rem;font-weight:600;color:var(--c5-lamina);line-height:1.1;}
.aqm-c5-placa .aqm-c5-un{font-family:var(--c5-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c5-legenda);}
.aqm-c5-produto h4{font-family:var(--c5-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c5-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c5-porque strong{font-family:var(--c5-mono);font-size:.86rem;}
.aqm-c5-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c5-legenda);line-height:1.5;}
.aqm-c5-ficha li{margin:0;}
.aqm-c5-ficha b{font-family:var(--c5-mono);font-weight:600;color:var(--c5-tinta);}
.aqm-c5-loja{display:inline-block;font-family:var(--c5-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c5-lamina);color:var(--c5-superficie);text-decoration:none;}
.aqm-c5-loja:hover{filter:brightness(1.08);color:var(--c5-superficie);}
.aqm-c5-semloja{font-size:.82rem;color:var(--c5-legenda);font-style:italic;}
.aqm-c5-voltaviso{font-size:.82rem;color:var(--c5-alerta);font-weight:600;margin:.4rem 0 0;line-height:1.45;}
.aqm-c5-aviso-afiliado{background:var(--c5-papel);border:1px solid var(--c5-traco);border-left:3px solid var(--c5-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c5-legenda);margin:1rem 0 0;}
.aqm-c5-aviso-afiliado strong{color:var(--c5-tinta);}
.aqm-c5-citar{background:var(--c5-papel);border:1px dashed var(--c5-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c5-citar p{margin:0 0 .6rem;}
.aqm-c5-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c5-fontes{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c5-fontes th,.aqm-c5-fontes td{border:1px solid var(--c5-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c5-fontes th{background:var(--c5-papel);font-family:var(--c5-display);font-size:.8rem;}
.aqm-c5-fontes td:first-child{font-family:var(--c5-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c5-selo{display:inline-block;font-family:var(--c5-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c5-alerta);border:1px solid var(--c5-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c5-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c5-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c5-oculto{display:none;}
@media (max-width:600px){.aqm-c5-valor{font-size:1.6rem;}
.aqm-c5-produto{grid-template-columns:1fr;}
.aqm-c5-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_js' ) ) {
function aquametria_c5_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var DELTA_COBERTO = 10;   /* wl-delta-ate-10: a fonte declarou até 10 °C */

	/* As regras de bolso do corpus, cada uma com a condição que o PRÓPRIO autor
	   declarou. Não há média entre elas: a faixa vai do menor W/L aplicável ao
	   maior, e cada extremo carrega o nome de quem o publicou.
	   'sempre' = o autor não declarou condição nenhuma — que é justamente o
	   problema que esta calculadora existe para expor. */
	var REGRAS = [
		{ id: 'wl-delta-ate-10', wl: [1.0, 1.5], quando: 'delta', fonte: 'ReefFlow',
		  rotulo: 'Regra com delta declarado',
		  nota: 'A única fonte do nosso levantamento que amarra watts por litro a uma diferença de temperatura: de 1,0 a 1,5 W/L para até 10 °C de diferença entre o ambiente e a água.' },
		{ id: 'wl-sul', wl: [2.0, 2.0], quando: 'sul', fonte: 'Casa da Ada',
		  rotulo: 'Leitura do Sul',
		  nota: 'Até 2,0 W/L para a região Sul. É a única fonte do corpus que reconhece que o Brasil não tem um clima só — mas ela também não diz para qual diferença de temperatura o número vale.' },
		{ id: 'wl-generico', wl: [1.0, 1.0], quando: 'sempre', fonte: 'repetida sem autoria única na web BR',
		  rotulo: 'Regra genérica',
		  nota: '1 W por litro. É o número que quase toda página brasileira publica, sem autor identificável e sem dizer para qual diferença de temperatura vale.' },
		{ id: 'wl-ehow', wl: [1.3, 1.3], quando: 'sempre', fonte: 'eHow',
		  rotulo: 'Variante da regra genérica',
		  nota: '1,3 W por litro, também sem condição declarada. Está aqui porque discorda do 1,0 W/L — e a discordância é o conteúdo.' }
	];

	/* Constante 'eheim-jager-linha-comercial': os 9 tamanhos da linha. Aquecedor
	   não se vende em qualquer potência; a escolha real é entre estes degraus. */
	var LINHA = [25, 50, 75, 100, 125, 150, 200, 250, 300];

	/* Constante 'especies-parametros-iniciais' (Petz; Aquarismo Paulista). São 8
	   espécies com ficha e fonte. Espécie sem ficha não entra: aqui não se
	   inventa temperatura de peixe. */
	var ESPECIES = [
		{ id: 'betta', nome: 'Betta', t: [24, 28], fonte: 'Petz' },
		{ id: 'kinguio', nome: 'Kinguio', t: [18, 24], fonte: 'Petz' },
		{ id: 'guppy', nome: 'Guppy', t: [23, 26], fonte: 'Petz' },
		{ id: 'acara-disco', nome: 'Acará-disco', t: [26, 30], fonte: 'Petz' },
		{ id: 'tetra', nome: 'Tetra', t: [26, 30], fonte: 'Petz' },
		{ id: 'acara-bandeira', nome: 'Acará-bandeira', t: [24, 28], fonte: 'Petz' },
		{ id: 'barbo-sumatra', nome: 'Barbo-sumatra', t: [20, 28], fonte: 'Aquarismo Paulista' },
		{ id: 'paulistinha', nome: 'Paulistinha', t: [18, 28], fonte: 'Aquarismo Paulista' }
	];

	var raiz = document.querySelector('.aqm-c5');
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

	/* Watts é número grosso: arredondar para 5 W evita a falsa precisão de
	   "137,5 W" numa conta que vem de regra de bolso. */
	function watts(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return fmt(Math.round(n / 5) * 5, 0);
	}

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	function graus(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return fmt(Math.round(n * 10) / 10, 1);
	}

	function especiePorId(id) {
		for (var i = 0; i < ESPECIES.length; i++) {
			if (ESPECIES[i].id === id) { return ESPECIES[i]; }
		}
		return null;
	}

	function campos() {
		var esp = el('aqm-c5-especie').value;
		return {
			volume: num(el('aqm-c5-volume').value),
			especie: esp,
			alvo: num(el('aqm-c5-alvo').value),
			minima: num(el('aqm-c5-minima').value),
			sul: el('aqm-c5-sul').checked,
			tampado: el('aqm-c5-tampado').value,
			voltagem: el('aqm-c5-voltagem').value
		};
	}

	/* --------------------------------------------------------------- alvo */

	/* A temperatura-alvo vem da ficha da espécie, quando há espécie escolhida, e
	   é o MEIO da faixa publicada — que é convenção da Aquametria, declarada na
	   tela, e não constante com fonte. Quem digita o alvo manda sobre a ficha. */
	function resolverAlvo(d) {
		if (d.alvo !== null) {
			return { valor: d.alvo, origem: 'manual' };
		}
		var esp = especiePorId(d.especie);
		if (esp) {
			return {
				valor: (esp.t[0] + esp.t[1]) / 2,
				origem: 'especie',
				especie: esp
			};
		}
		return { valor: null, origem: 'nenhuma' };
	}

	/* ------------------------------------------------------------- o cálculo */

	function calcular(d) {
		var r = { erros: [], avisos: [], editoriais: [] };

		if (d.volume === null) {
			r.erros.push({ campo: 'volume', texto: 'Informe o volume real de água do aquário, em litros.' });
		} else if (d.volume <= 0) {
			r.erros.push({ campo: 'volume', texto: 'O volume precisa ser maior que zero.' });
		} else if (d.volume > 20000) {
			r.erros.push({ campo: 'volume', texto: 'Acima de 20 000 L: confira a unidade (o campo é em litros).' });
		}

		var alvo = resolverAlvo(d);
		if (alvo.valor === null) {
			r.erros.push({ campo: 'alvo', texto: 'Escolha uma espécie ou digite a temperatura-alvo, em graus Celsius.' });
		} else if (alvo.valor < 10 || alvo.valor > 40) {
			r.erros.push({ campo: 'alvo', texto: 'Temperatura-alvo entre 10 e 40 °C. Fora disso, confira a unidade.' });
		}

		if (d.minima === null) {
			r.erros.push({ campo: 'minima', texto: 'Informe a temperatura mínima do cômodo onde o aquário fica, na noite mais fria do ano. É a pergunta que muda tudo — e a que nenhuma outra calculadora faz.' });
		} else if (d.minima < -5 || d.minima > 40) {
			r.erros.push({ campo: 'minima', texto: 'Temperatura mínima do ambiente entre -5 e 40 °C.' });
		}

		if (r.erros.length) { return r; }

		r.entradas = d;
		r.alvo = alvo;
		r.delta = alvo.valor - d.minima;

		if (r.delta <= 0) {
			r.sem_delta = true;
			return r;
		}

		r.delta_coberto = r.delta <= DELTA_COBERTO;

		var V = d.volume;
		r.regras = [];
		REGRAS.forEach(function (g) {
			var vale = (g.quando === 'sempre')
				|| (g.quando === 'delta' && r.delta_coberto)
				|| (g.quando === 'sul' && d.sul);
			if (!vale) {
				r.regras.push({ regra: g, aplicavel: false, motivo: motivoFora(g, r, d) });
				return;
			}
			r.regras.push({
				regra: g, aplicavel: true,
				min: V * g.wl[0], max: V * g.wl[1]
			});
		});

		var aplicaveis = r.regras.filter(function (x) { return x.aplicavel; });
		r.piso = Math.min.apply(null, aplicaveis.map(function (x) { return x.min; }));
		r.teto = Math.max.apply(null, aplicaveis.map(function (x) { return x.max; }));
		r.wl_piso = r.piso / V;
		r.wl_teto = r.teto / V;

		/* Potência comercial: o degrau da linha que cobre o topo da faixa.
		   Escolher o topo é convenção editorial declarada, não constante. */
		r.comercial = LINHA.filter(function (w) { return w >= r.teto; })[0] || null;
		r.comercial_piso = LINHA.filter(function (w) { return w >= r.piso; })[0] || null;
		r.editoriais.push('Entre dois degraus da linha comercial, esta página indica o que cobre o TOPO da faixa. '
			+ 'O motivo: aquecedor subdimensionado trabalha ligado o tempo todo e, na noite mais fria, ainda assim não segura a temperatura; '
			+ 'superdimensionado com termostato que funcione apenas liga menos vezes. É critério editorial da Aquametria, declarado aqui, e não constante com fonte.');

		if (!r.delta_coberto) {
			r.avisos.push('A diferença que você informou é de ' + graus(r.delta) + ' °C, e nenhuma fonte do nosso levantamento cobre esse caso. '
				+ 'A única que amarrou watts por litro a uma diferença de temperatura (ReefFlow) declarou o número para até ' + DELTA_COBERTO + ' °C. '
				+ 'Acima disso, o que sobra são as regras genéricas, que não dizem para qual diferença valem — então a faixa abaixo é um PISO, e pode ser insuficiente. '
				+ 'Extrapolar a regra de bolso para além do delta que a fonte declarou seria inventar constante, e aqui isso não se faz.');
		}

		if (d.tampado === 'nao') {
			r.avisos.push('Aquário destampado perde mais calor, e perde principalmente por evaporação na lâmina livre — que costuma ser a maior parcela da perda. '
				+ 'Não corrigimos o número por isso: a constante que quantificaria essa perda (u-vidro-aquario) está pendente no nosso banco, sem fonte. '
				+ 'Na prática, com o aquário aberto, trate a faixa abaixo como piso e considere o degrau comercial seguinte.');
		}

		if (r.comercial && r.comercial >= 150) {
			r.editoriais.push('Acima de 150 W vale considerar dois aquecedores de metade da potência em vez de um só. '
				+ 'O argumento é modo de falha, não eficiência: termostato que trava ligado num aquecedor de metade da potência aquece menos o aquário, '
				+ 'e termostato que trava desligado deixa o outro segurando alguma coisa. É raciocínio editorial da Aquametria — nenhuma fonte do nosso levantamento publica isso como regra.');
		}

		if (r.alvo.origem === 'especie') {
			r.editoriais.push('A temperatura-alvo veio do meio da faixa que a ficha da espécie publica ('
				+ graus(r.alvo.especie.t[0]) + ' a ' + graus(r.alvo.especie.t[1]) + ' °C, ' + r.alvo.especie.fonte + '). '
				+ 'Mirar no meio de uma faixa publicada é convenção da Aquametria; a faixa é que tem fonte. Se você quer outro ponto dela, digite o alvo.');
		}

		r.produtos = escolher(r, d);
		return r;
	}

	function motivoFora(g, r, d) {
		if (g.quando === 'delta') {
			return 'Vale só até ' + DELTA_COBERTO + ' °C de diferença, e a sua é de ' + graus(r.delta) + ' °C. A fonte não cobre o seu caso.';
		}
		if (g.quando === 'sul') {
			return 'Vale para a região Sul, e você não marcou essa opção.';
		}
		return '';
	}

	/* Adequação técnica, e só ela. Duas barreiras de segurança vêm antes:
	   a voltagem da tomada e a faixa de ajuste alcançar o alvo (regra V18).
	   Link de afiliado não entra no critério nem na ordem (regra V16). */
	function escolher(r, d) {
		var barrados = [];
		var teto = r.comercial || r.teto;
		var dentro = AQM_C5_CATALOGO.filter(function (p) {
			/* A potência vem primeiro, e de propósito: modelo que nunca esteve na
			   faixa não é "barrado", é irrelevante, e listá-lo encheria a tela de
			   ruído. Só quem serviria pela potência merece explicação de por que
			   ficou de fora. */
			if (p.potencia_w < r.piso || p.potencia_w > teto) { return false; }

			if (p.voltagem.indexOf(d.voltagem) === -1) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas as fichas que consultamos não o trazem em ' + d.voltagem + ' V.');
				return false;
			}
			if (p.ajuste_max_C !== null && r.alvo.valor > p.ajuste_max_C) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas o termostato vai só até '
					+ graus(p.ajuste_max_C) + ' °C' + (p.ajuste_conservador ? ' pela faixa conservadora' : '')
					+ ' e você quer ' + graus(r.alvo.valor) + ' °C.');
				return false;
			}
			if (p.ajuste_min_C !== null && r.alvo.valor < p.ajuste_min_C) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas o termostato começa em '
					+ graus(p.ajuste_min_C) + ' °C' + (p.ajuste_conservador ? ' pela faixa conservadora' : '')
					+ ' e você quer ' + graus(r.alvo.valor) + ' °C.');
				return false;
			}
			return true;
		});

		/* A ordem é a distância até o topo da faixa, que é onde a convenção
		   editorial manda mirar. Comissão não ordena nada. */
		dentro.sort(function (a, b) {
			return Math.abs(a.potencia_w - r.teto) - Math.abs(b.potencia_w - r.teto);
		});

		r.barrados = barrados;
		return dentro.slice(0, 5);
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c5-saida');
		var ul = el('aqm-c5-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c5-erro').forEach(function (n) { n.classList.remove('aqm-c5-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c5-' + er.campo);
				if (campo) { campo.classList.add('aqm-c5-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c5-oculto');
			return;
		}

		alvo.classList.remove('aqm-c5-oculto');

		/* Delta zero ou negativo: não há conta de potência a fazer, e dizer isso
		   é mais honesto que devolver um número. */
		var semDelta = el('aqm-c5-semdelta');
		if (r.sem_delta) {
			el('aqm-c5-corpo').classList.add('aqm-c5-oculto');
			semDelta.classList.remove('aqm-c5-oculto');
			semDelta.innerHTML = '<strong>Com os números que você informou, a água nunca cai abaixo da temperatura-alvo.</strong> '
				+ 'A mínima do ambiente (' + graus(r.entradas.minima) + ' °C) é igual ou maior que o alvo (' + graus(r.alvo.valor) + ' °C), '
				+ 'então a diferença de temperatura é zero ou negativa e não existe potência a calcular: nenhuma regra do nosso levantamento dimensiona aquecedor para esse caso. '
				+ 'O que um aquecedor ainda faz aí é segurar a oscilação do dia para a noite, e isso não é conta de watts — é termostato. '
				+ 'Se a sua dúvida é o contrário, ou seja, como impedir que a água passe do alvo no verão, esse é outro problema (resfriamento) e nós ainda não publicamos número sobre ele.';
			guardar(r);
			atualizarEndereco(r.entradas);
			return;
		}
		semDelta.classList.add('aqm-c5-oculto');
		el('aqm-c5-corpo').classList.remove('aqm-c5-oculto');

		el('aqm-c5-faixa-valor').innerHTML = watts(r.piso) + ' a ' + watts(r.teto) + '<span class="aqm-c5-unidade">W</span>';
		el('aqm-c5-faixa-criterio').textContent =
			'São ' + fmt(r.wl_piso, 2) + ' a ' + fmt(r.wl_teto, 2) + ' watts por litro aplicados aos ' + litros(r.entradas.volume) + ' L de água. '
			+ (r.delta_coberto
				? 'A faixa é larga porque as fontes brasileiras discordam entre si — e porque só uma delas diz para qual diferença de temperatura o número dela vale.'
				: 'Trate esta faixa como piso: a sua diferença de temperatura está fora do que a única fonte com delta declarado cobre.');

		el('aqm-c5-delta').innerHTML =
			'<span>alvo <b>' + graus(r.alvo.valor) + ' °C</b></span>'
			+ '<span>mínima do cômodo <b>' + graus(r.entradas.minima) + ' °C</b></span>'
			+ '<span>diferença <b>' + graus(r.delta) + ' °C</b></span>'
			+ '<span>potência comercial <b>' + (r.comercial ? fmt(r.comercial, 0) + ' W' : 'acima da linha') + '</b></span>';

		var lista = el('aqm-c5-regras');
		lista.innerHTML = '';
		r.regras.forEach(function (x) {
			var g = x.regra;
			if (x.aplicavel) {
				lista.appendChild(cartao(
					g.rotulo,
					(x.min === x.max ? watts(x.min) : watts(x.min) + ' a ' + watts(x.max)) + '<span class="aqm-c5-unidade">W</span>',
					g.nota + ' Fonte: ' + g.fonte + ', do nosso levantamento de setembro de 2026.',
					false
				));
			} else {
				lista.appendChild(cartao(
					g.rotulo + ' — não se aplica',
					'<span class="aqm-c5-vazio">fora do caso</span>',
					x.motivo + ' Ela aparece aqui porque saber qual regra NÃO vale para você é parte da resposta.',
					true
				));
			}
		});

		el('aqm-c5-comercial').innerHTML = r.comercial
			? '<strong>Na prateleira, isso vira um aquecedor de ' + fmt(r.comercial, 0) + ' W.</strong> '
				+ 'Aquecedor não se vende em qualquer potência: a linha comercial tem degraus (' + LINHA.join(', ') + ' W), '
				+ 'e o degrau que cobre o topo da sua faixa é o de ' + fmt(r.comercial, 0) + ' W'
				+ (r.comercial_piso && r.comercial_piso !== r.comercial
					? ' — o de ' + fmt(r.comercial_piso, 0) + ' W cobre só o piso dela.'
					: '.')
			: '<strong>A sua faixa passa do maior degrau da linha comercial de referência (' + LINHA[LINHA.length - 1] + ' W).</strong> '
				+ 'Aquário desse tamanho normalmente é aquecido por mais de um aparelho, ou por aquecedor externo em linha, que é outra categoria de produto e ainda não está no nosso banco.';

		el('aqm-c5-confronto').innerHTML =
			'<strong>Não use o volume que vem na caixa do aquecedor para dimensionar.</strong> '
			+ 'A Eheim declara o modelo de 200 W para aquários de 30 a 400 L: uma faixa de 13 vezes, ou de 0,5 a 6,7 W por litro dentro de um mesmo produto. '
			+ 'Na mesma linha, o 25 W é declarado para 25 L, o 50 W para 50 L, o 100 W para 100 L e o 150 W para 150 L — exatamente 1,0 W/L, que é a regra de bolso brasileira. '
			+ 'E há ficha de varejo brasileiro que declara o mesmo 150 W para 200 a 300 L, ou seja, metade disso. '
			+ 'O volume da embalagem serve para escolher entre dois modelos parecidos; ele não sabe quanto frio faz no seu quarto, e é por isso que esta página pergunta.';

		var av = el('aqm-c5-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		var ed = el('aqm-c5-editoriais');
		ed.innerHTML = '';
		(r.editoriais || []).forEach(function (t) {
			var li = document.createElement('li');
			li.className = 'aqm-c5-criterio';
			li.style.margin = '.35rem 0 0';
			li.textContent = t;
			ed.appendChild(li);
		});

		pintarProdutos(r);

		el('aqm-c5-citacao').textContent =
			'Aquário de ' + litros(r.entradas.volume) + ' L de água real, alvo de ' + graus(r.alvo.valor)
			+ ' °C e mínima de ' + graus(r.entradas.minima) + ' °C no cômodo — diferença de ' + graus(r.delta) + ' °C: '
			+ 'a potência de aquecedor pedida vai de ' + watts(r.piso) + ' a ' + watts(r.teto) + ' W conforme a fonte, '
			+ 'o que na linha comercial vira ' + (r.comercial ? fmt(r.comercial, 0) + ' W' : 'mais de um aparelho')
			+ '. Calculado pela Aquametria, ' + AQM_C5_DATA + '.';

		guardar(r);
		atualizarEndereco(r.entradas);
	}

	function cartao(rotulo, valor, criterio, fora) {
		var li = document.createElement('li');
		li.className = 'aqm-c5-cartao' + (fora ? ' aqm-c5-cartao-fora' : '');
		var r = document.createElement('span');
		r.className = 'aqm-c5-rotulo';
		r.textContent = rotulo;
		var v = document.createElement('span');
		v.className = 'aqm-c5-valor';
		v.innerHTML = valor;
		var c = document.createElement('p');
		c.className = 'aqm-c5-criterio';
		c.textContent = criterio;
		li.appendChild(r); li.appendChild(v); li.appendChild(c);
		return li;
	}

	/* ------------------------------------------------------------- produtos */

	function pintarProdutos(r) {
		var bloco = el('aqm-c5-produtos');
		var lista = el('aqm-c5-produtos-lista');
		var nada = el('aqm-c5-produtos-nada');
		lista.innerHTML = '';

		if (!r.produtos.length) {
			bloco.classList.add('aqm-c5-oculto');
			nada.classList.remove('aqm-c5-oculto');
			nada.textContent = 'Nenhum aquecedor do nosso banco entrega entre ' + watts(r.piso) + ' e '
				+ (r.comercial ? fmt(r.comercial, 0) : watts(r.teto)) + ' W em tomada de ' + r.entradas.voltagem
				+ ' V com termostato que alcance ' + graus(r.alvo.valor) + ' °C'
				+ (r.barrados.length ? ', e ' + r.barrados.length + ' modelo(s) tinham a potência certa mas foram barrados pela voltagem ou pela faixa de ajuste' : '')
				+ '. O banco tem ' + AQM_C5_CATALOGO.length + ' aquecedor(es) com ficha completa hoje e cresce a cada coleta. '
				+ 'Preferimos não mostrar produto nenhum a mostrar um que não atende o seu número — ou pior, que não liga na sua tomada.';
			if (r.barrados.length) {
				nada.textContent += ' Fora da lista: ' + r.barrados.join(' ');
			}
			return;
		}

		nada.classList.add('aqm-c5-oculto');
		bloco.classList.remove('aqm-c5-oculto');
		el('aqm-c5-produtos-sub').textContent =
			'São os aquecedores do nosso banco que entregam entre ' + watts(r.piso) + ' e '
			+ (r.comercial ? fmt(r.comercial, 0) : watts(r.teto)) + ' W, existem em ' + r.entradas.voltagem
			+ ' V e têm termostato capaz de chegar aos ' + graus(r.alvo.valor) + ' °C que você quer. '
			+ 'A ordem é pela proximidade do topo da faixa. Nada aqui é ordenado por comissão, e modelo sem link de loja aparece do mesmo jeito.';

		r.produtos.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r));
		});

		if (r.barrados.length) {
			var li = document.createElement('li');
			li.className = 'aqm-c5-criterio';
			li.textContent = 'Fora da lista: ' + r.barrados.join(' ');
			lista.appendChild(li);
		}
	}

	function produtoHtml(p, r) {
		var V = r.entradas.volume;
		var wl = p.potencia_w / V;

		var li = document.createElement('li');
		li.className = 'aqm-c5-produto';

		var placa = document.createElement('div');
		placa.className = 'aqm-c5-placa';
		placa.innerHTML = '<span class="aqm-c5-marca">' + esc(p.marca) + '</span>'
			+ '<span class="aqm-c5-numero">' + fmt(p.potencia_w, 0) + '</span>'
			+ '<span class="aqm-c5-un">watts</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = p.marca + ' ' + p.modelo;
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c5-porque';
		porque.innerHTML = 'No seu aquário de ' + litros(V) + ' L, este aquecedor entrega <strong>'
			+ fmt(Math.round(wl * 100) / 100, 2) + ' W por litro</strong>, contra os '
			+ fmt(r.wl_piso, 2) + ' a ' + fmt(r.wl_teto, 2) + ' W/L que a sua diferença de '
			+ graus(r.delta) + ' °C pede. '
			+ (p.volume_max_L
				? 'O fabricante declara que ele atende '
					+ (p.volume_min_L ? 'de ' + litros(p.volume_min_L) + ' a ' : 'até ') + litros(p.volume_max_L) + ' L'
					+ (p.volume_max_L >= V && (!p.volume_min_L || p.volume_min_L <= V)
						? ' — o seu volume cabe nessa declaração, mas repare que a declaração não sabe quanto frio faz aí.'
						: ' — o seu volume está fora dessa declaração, e ainda assim a potência bate com a conta. É o problema desta categoria inteira.')
				: 'O fabricante não declara volume atendido para este modelo.');
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c5-ficha';
		var linhas = [
			'Tipo: <b>' + esc(p.tipo) + '</b>',
			'Faixa de ajuste: <b>' + graus(p.ajuste_min_C) + ' a ' + graus(p.ajuste_max_C) + ' °C</b>'
				+ (p.ajuste_conservador
					? ' <span class="aqm-c5-selo">faixa conservadora</span>'
					: ''),
			'Voltagem: <b>' + (p.voltagem.length ? p.voltagem.join(' ou ') + ' V' : 'não declarada') + '</b>'
		];
		if (p.precisao_C) { linhas.push('Precisão declarada: <b>± ' + graus(p.precisao_C) + ' °C</b>'); }
		if (p.comprimento_cm) { linhas.push('Comprimento: <b>' + graus(p.comprimento_cm) + ' cm</b> — confira se cabe deitado ou em pé no seu aquário'); }
		if (p.seco === true) { linhas.push('Desliga sozinho fora da água: <b>sim</b>'); }
		if (p.ajuste_conservador && p.ajuste_derivacao) {
			linhas.push('Por que a faixa é conservadora: ' + esc(p.ajuste_derivacao));
		}
		if (p.conflito_volume) {
			linhas.push('Volume declarado, em conflito entre fontes: ' + esc(p.conflito_volume));
		}
		linhas.push('Ficha conferida em ' + esc(dataBr(p.verificado_em))
			+ (p.fonte_url ? ' — <a href="' + esc(p.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (p.fonte_status ? ' (' + esc(p.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (p.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c5-loja';
			a.href = p.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja);
			corpo.appendChild(a);
			var nota = document.createElement('p');
			nota.className = 'aqm-c5-voltaviso';
			nota.textContent = 'Confira a voltagem no anúncio antes de comprar'
				+ (p.voltagem_anuncio ? ': o anúncio que conferimos em 07/09/2026 era da versão de ' + p.voltagem_anuncio + ' V, e você marcou ' + r.entradas.voltagem + ' V.' : '.')
				+ ' A mesma potência é vendida nas duas tomadas e o anúncio pode mudar. Aquecedor na voltagem errada queima — ou, pior, esquenta demais.';
			corpo.appendChild(nota);
			var patro = document.createElement('p');
			patro.className = 'aqm-c5-semloja';
			patro.textContent = 'Link patrocinado. O anúncio não é a nossa fonte técnica; a ficha acima é.';
			corpo.appendChild(patro);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c5-semloja';
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
	   pode apagar o que ela nem o que a C3 gravaram. Só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c5-aquecedor-delta' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.entradas.volume) {
			estado.volumes.real_L = r.entradas.volume;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C5'; }
		}
		estado.clima = estado.clima || {};
		estado.clima.temp_alvo_C = r.alvo.valor;
		estado.clima.temp_alvo_origem = r.alvo.origem;
		estado.clima.especie = r.alvo.especie ? r.alvo.especie.id : null;
		estado.clima.temp_min_ambiente_C = r.entradas.minima;
		estado.clima.delta_C = r.delta;
		estado.clima.regiao_sul = !!r.entradas.sul;
		estado.perfil = estado.perfil || {};
		estado.perfil.tampado = r.entradas.tampado;
		estado.eletrica = estado.eletrica || {};
		estado.eletrica.voltagem = r.entradas.voltagem;
		estado.equipamentos = estado.equipamentos || {};
		estado.equipamentos.aquecedor_potencia_alvo_w = r.sem_delta
			? null
			: [Math.round(r.piso), Math.round(r.teto)];
		estado.equipamentos.aquecedor_potencia_comercial_w = r.comercial || null;
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c5-guardado').classList.remove('aqm-c5-oculto');
		} catch (erro) {
			el('aqm-c5-guardado').classList.add('aqm-c5-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'min=' + d.minima, 'volt=' + d.voltagem, 'tp=' + d.tampado];
		if (d.alvo !== null) { q.push('alvo=' + d.alvo); }
		if (d.especie) { q.push('esp=' + d.especie); }
		if (d.sul) { q.push('sul=1'); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c5-link').value = window.location.origin + url;
	}

	function lerQuery() {
		var busca = window.location.search;
		if (!busca || busca.length < 2) { return null; }
		var fora = {};
		busca.substring(1).split('&').forEach(function (par) {
			var p = par.split('=');
			if (p.length === 2) { fora[decodeURIComponent(p[0])] = decodeURIComponent(p[1]); }
		});
		return (fora.v && fora.min) ? fora : null;
	}

	/* ------------------------------------ o aquecedor que a pessoa já tem */

	function veredito() {
		var w = num(el('aqm-c5-tenho').value);
		var V = num(el('aqm-c5-volume').value);
		var saida = el('aqm-c5-tenho-saida');

		if (w === null || w <= 0) {
			saida.textContent = 'Informe a potência do aquecedor, em watts — é o número que vem na caixa e no próprio aparelho.';
			return;
		}

		var texto = 'Um aquecedor de ' + fmt(w, 0) + ' W cobre ';
		var partes = [];
		partes.push('até ' + litros(w / 1.5) + ' L pela regra com delta declarado (1,0 a 1,5 W/L até 10 °C de diferença, ReefFlow), no extremo mais exigente dela, e até '
			+ litros(w / 1.0) + ' L no extremo mais folgado');
		partes.push('até ' + litros(w / 2.0) + ' L pela leitura do Sul (2,0 W/L, Casa da Ada)');
		partes.push('até ' + litros(w / 1.3) + ' L pela variante de 1,3 W/L (eHow)');
		texto += partes.join('; ') + '. ';

		if (V !== null && V > 0) {
			var wl = w / V;
			texto += 'No seu aquário de ' + litros(V) + ' L, ele entrega ' + fmt(Math.round(wl * 100) / 100, 2) + ' W por litro — '
				+ (wl < 1.0
					? 'abaixo de todas as regras do nosso levantamento, inclusive da mais folgada.'
					: (wl < 1.5
						? 'dentro da faixa que a única fonte com delta declarado publica para até 10 °C de diferença. Se onde você mora esfria mais que isso, essa fonte não cobre o seu caso.'
						: 'acima de 1,5 W/L, ou seja, folgado até para a leitura do Sul se a diferença de temperatura for grande.'));
		}
		texto += ' Nenhum desses números pergunta quanto frio faz no seu cômodo — o cálculo lá em cima pergunta.';
		saida.textContent = texto;
	}

	/* ---------------------------------------------------------- ligações */

	function preencher(fora) {
		if (fora.v) { el('aqm-c5-volume').value = fora.v; }
		if (fora.min) { el('aqm-c5-minima').value = fora.min; }
		if (fora.alvo) { el('aqm-c5-alvo').value = fora.alvo; }
		if (fora.esp && especiePorId(fora.esp)) { el('aqm-c5-especie').value = fora.esp; }
		if (fora.volt === '110' || fora.volt === '220') { el('aqm-c5-voltagem').value = fora.volt; }
		if (fora.tp === 'sim' || fora.tp === 'nao' || fora.tp === 'nao-sei') { el('aqm-c5-tampado').value = fora.tp; }
		if (fora.sul === '1') { el('aqm-c5-sul').checked = true; }
	}

	/* A ficha da espécie escolhida aparece embaixo do campo, com a fonte, antes
	   mesmo de calcular: é ela que vira o alvo. */
	function mostrarEspecie() {
		var esp = especiePorId(el('aqm-c5-especie').value);
		var d = el('aqm-c5-especie-ficha');
		if (!esp) {
			d.textContent = 'Sem espécie escolhida, digite a temperatura-alvo ao lado.';
			return;
		}
		d.textContent = esp.nome + ': ' + graus(esp.t[0]) + ' a ' + graus(esp.t[1]) + ' °C, segundo ' + esp.fonte
			+ '. Sem alvo digitado, usamos o meio dessa faixa (' + graus((esp.t[0] + esp.t[1]) / 2) + ' °C).';
	}

	el('aqm-c5-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
	});

	el('aqm-c5-especie').addEventListener('change', mostrarEspecie);

	el('aqm-c5-limpar').addEventListener('click', function () {
		el('aqm-c5-form').reset();
		el('aqm-c5-saida').classList.add('aqm-c5-oculto');
		el('aqm-c5-erros').innerHTML = '';
		mostrarEspecie();
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c5-copiar').addEventListener('click', function () {
		var campo = el('aqm-c5-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c5-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c5-tenho-calcular').addEventListener('click', veredito);

	mostrarEspecie();

	/* Query string manda; senão, o aquário que a C1 guardou neste navegador.
	   Diferente da C3, aqui o volume não basta para calcular: a mínima do
	   ambiente é entrada e ninguém a adivinha. Então preenchemos e esperamos. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		mostrarEspecie();
		pintar(calcular(campos()));
	} else {
		var guardadoAntes = recuperar();
		var volume = guardadoAntes && guardadoAntes.volumes ? guardadoAntes.volumes.real_L : null;
		if (volume) {
			el('aqm-c5-volume').value = String(volume).replace('.', ',');
			var clima = guardadoAntes.clima || {};
			if (clima.temp_min_ambiente_C !== null && clima.temp_min_ambiente_C !== undefined) {
				el('aqm-c5-minima').value = String(clima.temp_min_ambiente_C).replace('.', ',');
			}
			if (clima.regiao_sul) { el('aqm-c5-sul').checked = true; }
			if (clima.especie && especiePorId(clima.especie)) {
				el('aqm-c5-especie').value = clima.especie;
				mostrarEspecie();
			}
			var voltagemGuardada = (guardadoAntes.eletrica || {}).voltagem;
			if (voltagemGuardada === '110' || voltagemGuardada === '220') {
				el('aqm-c5-voltagem').value = voltagemGuardada;
			}
			var retomado = el('aqm-c5-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que as outras calculadoras guardaram neste navegador.';
			retomado.classList.remove('aqm-c5-oculto');
			if (num(el('aqm-c5-minima').value) !== null) {
				pintar(calcular(campos()));
			}
		} else {
			el('aqm-c5-semvolume').classList.remove('aqm-c5-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_url' ) ) {
function aquametria_c5_url( $slug ) {
	return function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( $slug )
		: home_url( '/' . $slug . '/' );
}
}

if ( ! function_exists( 'aquametria_c5_form_html' ) ) {
function aquametria_c5_form_html() {
	$c1 = aquametria_c5_url( 'calculadora-de-litragem' );

	$h  = '<form id="aqm-c5-form" class="aqm-c5-painel" novalidate>';
	$h .= '<h3>O seu aquário e o seu inverno</h3>';
	$h .= '<p class="aqm-c5-sub">A pergunta que decide a potência não é quantos litros o aquário tem — é quanto o cômodo esfria. ';
	$h .= 'Se você já usou as outras calculadoras neste navegador, o volume vem preenchido daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c5-grade">';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c5-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-minima">Mínima do cômodo (°C)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-minima" name="minima" placeholder="18">';
	$h .= '<span class="aqm-c5-dica">Quanto o ar do cômodo chega a marcar na noite mais fria do ano — não a média da cidade. É a entrada que nenhuma outra calculadora pede.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-especie">Espécie principal</label>';
	$h .= '<select id="aqm-c5-especie" name="especie">';
	$h .= '<option value="">— escolher, ou digitar o alvo ao lado —</option>';
	$h .= '<option value="betta">Betta (24 a 28 °C)</option>';
	$h .= '<option value="kinguio">Kinguio (18 a 24 °C)</option>';
	$h .= '<option value="guppy">Guppy (23 a 26 °C)</option>';
	$h .= '<option value="acara-disco">Acará-disco (26 a 30 °C)</option>';
	$h .= '<option value="tetra">Tetra (26 a 30 °C)</option>';
	$h .= '<option value="acara-bandeira">Acará-bandeira (24 a 28 °C)</option>';
	$h .= '<option value="barbo-sumatra">Barbo-sumatra (20 a 28 °C)</option>';
	$h .= '<option value="paulistinha">Paulistinha (18 a 28 °C)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica" id="aqm-c5-especie-ficha"></span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-alvo">Temperatura-alvo (°C)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-alvo" name="alvo" placeholder="26">';
	$h .= '<span class="aqm-c5-dica">Em branco, usamos a ficha da espécie. Preenchido, o seu número manda.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-voltagem">Voltagem da tomada</label>';
	$h .= '<select id="aqm-c5-voltagem" name="voltagem">';
	$h .= '<option value="110">110 V (ou 127 V)</option>';
	$h .= '<option value="220">220 V</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica">Filtra a lista de produtos, não o cálculo. Aquecedor na voltagem errada queima.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-tampado">O aquário é tampado?</label>';
	$h .= '<select id="aqm-c5-tampado" name="tampado">';
	$h .= '<option value="sim">sim, tem tampa</option>';
	$h .= '<option value="nao">não, é aberto</option>';
	$h .= '<option value="nao-sei" selected>não sei ainda</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica">Muda o texto da resposta, não o número: quantificar essa perda exigiria uma constante que ainda não temos com fonte.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c5-caixa"><input type="checkbox" id="aqm-c5-sul"> <span>Moro na região Sul — quero que a leitura de 2,0 W/L entre na conta</span></label>';

	$h .= '<div class="aqm-c5-botoes">';
	$h .= '<button type="submit">Calcular a potência</button>';
	$h .= '<button type="button" class="aqm-c5-secundario" id="aqm-c5-limpar">Limpar</button>';
	$h .= '<span class="aqm-c5-dica aqm-c5-oculto" id="aqm-c5-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c5-avisos" id="aqm-c5-erros"></ul>';
	$h .= '<p class="aqm-c5-criterio aqm-c5-oculto" id="aqm-c5-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre e as rochas tiram uma parte, e a potência do aquecedor é calculada sobre a água que existe. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_resposta_html' ) ) {
function aquametria_c5_resposta_html() {
	$h  = '<div class="aqm-c5-resultado aqm-c5-oculto" id="aqm-c5-saida" aria-live="polite">';

	$h .= '<p class="aqm-c5-nota aqm-c5-nota-alerta aqm-c5-oculto" id="aqm-c5-semdelta"></p>';

	$h .= '<div id="aqm-c5-corpo">';

	$h .= '<div class="aqm-c5-faixa">';
	$h .= '<span class="aqm-c5-rotulo">Potência de aquecedor que o seu caso pede</span>';
	$h .= '<span class="aqm-c5-valor" id="aqm-c5-faixa-valor">—</span>';
	$h .= '<p class="aqm-c5-criterio" id="aqm-c5-faixa-criterio"></p>';
	$h .= '<div class="aqm-c5-delta" id="aqm-c5-delta"></div>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c5-cartoes" id="aqm-c5-regras"></ul>';

	$h .= '<p class="aqm-c5-nota" id="aqm-c5-comercial"></p>';

	$h .= '<ul class="aqm-c5-avisos" id="aqm-c5-avisos"></ul>';

	$h .= '<p class="aqm-c5-nota aqm-c5-nota-alerta" id="aqm-c5-confronto"></p>';

	$h .= '<div class="aqm-c5-painel"><h3>O que aqui é critério nosso, e não fonte de terceiro</h3>';
	$h .= '<p class="aqm-c5-sub" style="margin-bottom:.4rem">Constante tem origem e data; escolha editorial tem nome e fica declarada. Estas são as desta resposta.</p>';
	$h .= '<ul id="aqm-c5-editoriais" style="list-style:none;margin:0;padding:0"></ul></div>';

	$h .= aquametria_c5_produtos_html();

	$h .= '<div class="aqm-c5-citar">';
	$h .= '<p id="aqm-c5-citacao"></p>';
	$h .= '<div class="aqm-c5-campo"><label for="aqm-c5-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c5-link" readonly></div>';
	$h .= '<div class="aqm-c5-botoes"><button type="button" class="aqm-c5-secundario" id="aqm-c5-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c5-dica" id="aqm-c5-copiado"></span></div>';
	$h .= '<p class="aqm-c5-dica" id="aqm-c5-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_produtos_html' ) ) {
function aquametria_c5_produtos_html() {
	$divulgacao = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c5-produtos aqm-c5-painel aqm-c5-oculto" id="aqm-c5-produtos">';
	$h .= '<h3>Aquecedores que atendem essa potência</h3>';
	$h .= '<p class="aqm-c5-sub" id="aqm-c5-produtos-sub"></p>';
	$h .= '<ul class="aqm-c5-lista" id="aqm-c5-produtos-lista"></ul>';
	$h .= '<p class="aqm-c5-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista nem em que ordem — a ordem é pela potência mais próxima do topo da faixa que o seu caso pede, e modelo sem link aparece do mesmo jeito. ';
	$h .= 'Antes da adequação, duas barreiras de segurança: só entra quem existe na voltagem da sua tomada e cujo termostato alcança a sua temperatura-alvo. ';
	$h .= 'A ficha técnica de cada aquecedor vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'Também não publicamos preço nesta página: preço muda toda semana e um número velho na tela seria pior que nenhum. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c5-nota aqm-c5-oculto" id="aqm-c5-produtos-nada"></p>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_tenho_html' ) ) {
function aquametria_c5_tenho_html() {
	$h  = '<div class="aqm-c5-painel">';
	$h .= '<h3>Caminho inverso: o aquecedor que eu já tenho serve?</h3>';
	$h .= '<p class="aqm-c5-sub">Informe a potência que vem na caixa e devolvemos até quantos litros ele cobre por cada regra — e, se o volume estiver preenchido acima, quantos watts por litro ele entrega no seu aquário.</p>';
	$h .= '<div class="aqm-c5-grade">';
	$h .= '<div class="aqm-c5-campo"><label for="aqm-c5-tenho">Potência do aquecedor (W)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c5-tenho" placeholder="100"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c5-botoes"><button type="button" id="aqm-c5-tenho-calcular">Ver o que ele cobre</button></div>';
	$h .= '<p class="aqm-c5-criterio" id="aqm-c5-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_fontes_html' ) ) {
function aquametria_c5_fontes_html() {
	$artigo = aquametria_c5_url( AQUAMETRIA_C5_ARTIGO );

	$h  = '<div class="aqm-c5-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c5-sub">Verificado em ' . esc_html( AQUAMETRIA_C5_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C5_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c5-rolagem"><table class="aqm-c5-fontes">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>wl-delta-ate-10</td><td>1,0 a 1,5 W/L</td>';
	$h .= '<td>ReefFlow, do levantamento de 04/09/2026 <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'É a <strong>única</strong> fonte do nosso corpus que amarra watts por litro a uma diferença de temperatura declarada: vale para até ' . esc_html( AQUAMETRIA_C5_DELTA_COBERTO ) . ' °C entre o ambiente e a água. ';
	$h .= 'Acima disso, ela não afirma nada — e nós também não.</td></tr>';

	$h .= '<tr><td>wl-sul</td><td>2,0 W/L</td>';
	$h .= '<td>Casa da Ada, para a região Sul <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'É a única fonte do corpus que reconhece que o Brasil tem mais de um clima. Ainda assim não declara para qual diferença de temperatura o número vale.</td></tr>';

	$h .= '<tr><td>wl-generico</td><td>1,0 W/L</td>';
	$h .= '<td>Repetida sem autoria única na web brasileira <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'Nenhuma fonte diz de onde o número saiu nem para qual clima vale. É o vácuo que esta página existe para preencher.</td></tr>';

	$h .= '<tr><td>wl-ehow</td><td>1,3 W/L</td>';
	$h .= '<td>eHow <span class="aqm-c5-selo">divergente entre fontes BR</span>. Também sem condição declarada. Está aqui porque discorda da anterior em 30 %, e a discordância é o conteúdo.</td></tr>';

	$h .= '<tr><td>eheim-jager-linha-comercial</td><td>25 a 300 W, 9 tamanhos</td>';
	$h .= '<td>Eheim Jager / Thermocontrol, ficha do fabricante e tabelas de varejo, completada em 08/09/2026 <span class="aqm-c5-selo">transcrita de varejo</span>. ';
	$h .= 'Dela sai o degrau comercial. E dela sai o achado: 25 W para 25 L, 50 W para 50 L, 100 W para 100 L e 150 W para 150 L — o catálogo do fabricante é construído sobre a mesma regra de 1 W/L que a web repete, ';
	$h .= 'enquanto o mesmo catálogo declara 200 W para 30 a 400 L, uma faixa de 13 vezes.</td></tr>';

	$h .= '<tr><td>especies-parametros-iniciais</td><td>8 espécies</td>';
	$h .= '<td>Petz e Aquarismo Paulista <span class="aqm-c5-selo">transcrita de varejo</span>. Só entram no seletor espécies com ficha e fonte; ';
	$h .= 'o banco completo de espécies é trabalho da C10, ainda em construção.</td></tr>';

	$h .= '<tr><td>u-vidro-aquario</td><td>sem valor <span class="aqm-c5-selo">pendente</span></td>';
	$h .= '<td>O coeficiente de troca térmica do vidro do aquário, que permitiria calcular a potência pela física (P = U · A · ΔT) em vez de por regra de bolso. ';
	$h .= 'Sem ele, esta página não corrige por área, por espessura de vidro nem por tampa. É a entrega que tornaria a Aquametria a única referência do nicho no Brasil, e ela ainda não saiu.</td></tr>';

	$h .= '<tr><td>temperatura-minima-por-cidade</td><td>sem valor <span class="aqm-c5-selo">pendente</span></td>';
	$h .= '<td>A mínima do ar por cidade brasileira. A coleta prevista é a Normal Climatológica do INMET (1991-2020), mínima média do mês mais frio por estação. ';
	$h .= 'Enquanto não existir, a mínima é entrada sua — e é melhor assim: a mínima do seu quarto não é a mínima da sua cidade.</td></tr>';

	$h .= '</table></div>';
	$h .= '<p class="aqm-c5-criterio" style="margin-top:.8rem">A discussão longa de por que essas fontes discordam, e do que acontece quando se segue cada uma delas, está em ';
	$h .= '<a href="' . esc_url( $artigo ) . '">quantos watts de aquecedor o seu aquário precisa</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_adiante_html' ) ) {
function aquametria_c5_adiante_html() {
	$hub    = aquametria_c5_url( 'calculadoras' );
	$meto   = aquametria_c5_url( 'metodologia' );
	$c1     = aquametria_c5_url( 'calculadora-de-litragem' );
	$c3     = aquametria_c5_url( 'calculadora-de-vazao-do-filtro' );
	$c12    = aquametria_c5_url( 'calculadora-de-midia-filtrante' );
	$c15    = aquametria_c5_url( 'calculadora-de-iluminacao' );
	$artigo = aquametria_c5_url( AQUAMETRIA_C5_ARTIGO );
	$divul  = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c5-painel aqm-c5-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $artigo ) . '"><strong>Quantos watts de aquecedor o seu aquário precisa</strong></a> — o texto que explica por que o "1 W por litro" não erra por acaso, e de onde ele veio.</li>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vem o volume real que esta página usa. Se o número acima veio preenchido, veio de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c3 ) . '"><strong>Vazão do filtro (C3)</strong></a> — usa o mesmo volume. O filtro fica ligado 24 horas por dia; o aquecedor, não. Quanto tempo cada um fica ligado é o que a C7 vai calcular.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — quanta mídia biológica o mesmo volume de água pede, pelas quatro dosagens que os fabricantes declaram. A colônia nitrificante também depende de temperatura: aquário frio cicla mais devagar, e é este aquecedor que decide isso.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — o outro aparelho que consome energia no aquário, e o único que você pode desligar por 16 horas por dia. Luminária potente também aquece a água: em aquário pequeno e tampado, isso conta contra o trabalho deste aquecedor.</li>';
	$h .= '<li><strong>Consumo elétrico (C7)</strong> — a conta de luz do aquário. Vai ler daqui a potência do aquecedor e a diferença de temperatura, porque é o ciclo do aquecedor que pesa no inverno. Ainda em construção.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c5-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 6. Shortcode
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_shortcode' ) ) {
function aquametria_c5_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	$js  = 'var AQM_C5_DATA = ' . wp_json_encode( AQUAMETRIA_C5_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C5_CATALOGO = ' . wp_json_encode( array_values( aquametria_c5_catalogo() ) ) . ";\n";
	$js .= aquametria_c5_js();

	$h  = '<div class="aqm-c5">';
	$h .= '<style id="aquametria-c5-estilo">' . aquametria_c5_css() . '</style>';
	$h .= aquametria_c5_form_html();
	$h .= aquametria_c5_resposta_html();
	$h .= aquametria_c5_tenho_html();
	$h .= aquametria_c5_fontes_html();
	$h .= aquametria_c5_adiante_html();
	$h .= '<script id="aquametria-c5-script">' . $js . '</script>';
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_aquecedor', 'aquametria_c5_shortcode' );

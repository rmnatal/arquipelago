/**
 * Aquametria Calculadora de Litragem — C1
 * Versão: 1.2.0 (10/09/2026) — VISIBILIDADE EM IA (seção 5 do ARQUIPELAGO.md), as três peças de
 *   uma vez: resposta antes da explicação, tabela de exemplos pré-renderizada com seis aquários
 *   de 30 a 120 cm de frente, e JSON-LD (WebApplication + FAQPage) no wp_head. Era a última
 *   calculadora da ilha sem as três, e a única com jsonld_ok=0 no conferir-entidades.mjs.
 *   Nenhuma linha de cálculo mudou: tudo que a tabela servida imprime é ESPELHO em PHP das
 *   mesmas funções do script (fmt, litros, e as regras de calcular()), porque tabela que
 *   arredonda diferente da calculadora logo acima dela faz a página se contradizer sozinha.
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.4 (08/09/2026) — o painel "o que este resultado alimenta" agora linka a C15, que
 * lê daqui não só o volume, mas também o comprimento e a altura da lâmina. A 1.0.3 linkou a C12,
 * publicada nesta data. A 1.0.2 fez guardar() MESCLAR o estado compartilhado em vez de
 * substituí-lo; a 1.0.1 linkou a C3
 *
 * Núcleo do lote de calculadoras. Converte as medidas do aquário em três
 * volumes — bruto, interno e real de referência — e grava o resultado no
 * navegador do visitante (localStorage, chave 'aquametria.aquario'), que é o
 * estado compartilhado que as outras calculadoras leem.
 *
 * Registra o shortcode [aquametria_calculadora_litragem] e se anuncia no hub
 * pelo filtro 'aquametria_calculadoras' da casca: enquanto este snippet estiver
 * ativo, o cartão da C1 aparece como publicada; desativado, o hub volta a
 * dizer "em construção" sozinho. Nada para editar em dois lugares.
 *
 * Todo o cálculo é JavaScript no navegador, e é de propósito: o site está atrás
 * do cache de página da hospedagem, então HTML que dependesse da query string
 * seria servido errado para o visitante seguinte. Nada é enviado a servidor
 * nenhum — sem conta, sem login, sem coleta.
 *
 * O que esta calculadora NÃO faz, e por quê: não desconta o substrato. As
 * constantes 'substrato-densidade' (conflito de 100 % entre as fontes do
 * corpus) e 'substrato-porosidade' (nenhuma fonte publica) estão pendentes, e
 * constante pendente é proibida em fórmula publicada. A página declara a
 * consequência: o volume real fica superestimado, e a direção do erro é segura
 * para filtro, aquecedor e mídia, insegura para lotação e dosagem.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C1_VERSAO' ) ) {
	define( 'AQUAMETRIA_C1_VERSAO', '1.2.0' );
	define( 'AQUAMETRIA_C1_SLUG', 'calculadora-de-litragem' );
	define( 'AQUAMETRIA_C1_VERIFICADO_EM', '07/09/2026' );
	define( 'AQUAMETRIA_C1_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
	/* Constante 'borda-livre-padrao' (dados/constantes-calculadoras.json):
	   3 cm, status convencao-editorial. NÃO é dado técnico — é valor inicial
	   do campo, e a tela diz isso ao lado dele. */
	define( 'AQUAMETRIA_C1_BORDA_LIVRE_CM', 3 );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_registrar_no_hub' ) ) {
function aquametria_c1_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C1' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C1_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c1_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_css' ) ) {
function aquametria_c1_css() {
	return <<<'CSS'
.aqm-c1{--c1-tinta:var(--aqm-tinta,#0D1B22);--c1-lamina:var(--aqm-lamina,#0E7C8C);
--c1-papel:var(--aqm-papel,#F4F7F7);--c1-superficie:var(--aqm-superficie,#FFFFFF);
--c1-traco:var(--aqm-traco,#DDE5E6);--c1-legenda:var(--aqm-legenda,#5C7075);
--c1-alerta:var(--aqm-alerta,#B5762A);
--c1-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c1-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c1-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c1-texto);color:var(--c1-tinta);}
.aqm-c1 *{box-sizing:border-box;}
.aqm-c1 form{margin:0;}
.aqm-c1-painel{background:var(--c1-superficie);border:1px solid var(--c1-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c1-painel h3{font-family:var(--c1-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c1-painel .aqm-c1-sub{color:var(--c1-legenda);font-size:.9rem;margin:0 0 1rem;}
.aqm-c1-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(9.5rem,1fr));gap:.9rem;}
.aqm-c1-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c1-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c1-campo .aqm-c1-dica{font-size:.74rem;color:var(--c1-legenda);line-height:1.35;}
.aqm-c1 input[type=number],.aqm-c1 input[type=text],.aqm-c1 select{width:100%;font-family:var(--c1-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c1-traco);border-radius:2px;background:var(--c1-superficie);color:var(--c1-tinta);}
.aqm-c1 input:focus,.aqm-c1 select:focus{outline:2px solid var(--c1-lamina);outline-offset:1px;}
.aqm-c1 input.aqm-c1-erro{border-color:var(--c1-alerta);}
.aqm-c1-opcoes{display:flex;flex-wrap:wrap;gap:1.2rem;margin:.2rem 0 1rem;}
.aqm-c1-opcoes label{display:inline-flex;align-items:center;gap:.35rem;font-size:.9rem;font-weight:600;}
.aqm-c1-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c1 button{font-family:var(--c1-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c1-lamina);color:var(--c1-superficie);cursor:pointer;}
.aqm-c1 button.aqm-c1-secundario{background:transparent;color:var(--c1-lamina);border:1px solid var(--c1-traco);}
.aqm-c1 button:hover{filter:brightness(1.08);}
.aqm-c1-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c1-avisos li{font-size:.88rem;color:var(--c1-alerta);margin:.25rem 0 0;}
.aqm-c1-resultado{margin:0 0 1.2rem;}
.aqm-c1-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c1-cartao{background:var(--c1-superficie);border:1px solid var(--c1-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c1-cartao.aqm-c1-destaque{border-color:var(--c1-lamina);border-width:2px;}
.aqm-c1-rotulo{font-family:var(--c1-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c1-legenda);}
.aqm-c1-valor{font-family:var(--c1-mono);font-size:1.9rem;font-weight:600;line-height:1.05;font-variant-numeric:tabular-nums;}
.aqm-c1-valor .aqm-c1-unidade{font-size:.95rem;font-weight:500;color:var(--c1-legenda);margin-left:.25rem;}
.aqm-c1-criterio{font-size:.83rem;color:var(--c1-legenda);line-height:1.45;margin:0;}
.aqm-c1-vazio{font-family:var(--c1-texto);font-size:.95rem;color:var(--c1-legenda);font-weight:500;}
.aqm-c1-nota{border-left:3px solid var(--c1-lamina);background:var(--c1-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c1-legenda);margin:0 0 1rem;}
.aqm-c1-nota strong{color:var(--c1-tinta);}
.aqm-c1-nota.aqm-c1-nota-alerta{border-left-color:var(--c1-alerta);}
.aqm-c1-citar{background:var(--c1-papel);border:1px dashed var(--c1-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c1-citar p{margin:0 0 .6rem;}
.aqm-c1-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c1-fontes{width:100%;min-width:30rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c1-fontes th,.aqm-c1-fontes td{border:1px solid var(--c1-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c1-fontes th{background:var(--c1-papel);font-family:var(--c1-display);font-size:.8rem;}
.aqm-c1-fontes td:first-child{font-family:var(--c1-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c1-selo{display:inline-block;font-family:var(--c1-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c1-alerta);border:1px solid var(--c1-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c1-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c1-adiante li{margin:0 0 .4rem;font-size:.94rem;}
.aqm-c1-oculto{display:none;}
.aqm-c1-exemplos{width:100%;min-width:46rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c1-exemplos th,.aqm-c1-exemplos td{border:1px solid var(--c1-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c1-exemplos th{background:var(--c1-papel);font-family:var(--c1-display);font-size:.8rem;}
.aqm-c1-exemplos .aqm-c1-num{display:block;font-family:var(--c1-mono);font-variant-numeric:tabular-nums;font-size:.92rem;font-weight:600;color:var(--c1-tinta);line-height:1.25;}
.aqm-c1-exemplos .aqm-c1-un{display:block;font-size:.76rem;color:var(--c1-legenda);line-height:1.35;margin-top:.15rem;}
.aqm-c1-direta{background:var(--c1-papel);border:1px dashed var(--c1-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.55;margin:0 0 1.2rem;}
.aqm-c1-direta p{margin:0 0 .6rem;}
.aqm-c1-direta p:last-child{margin-bottom:0;}
.aqm-c1-aviso-tabela{background:var(--c1-papel);border:1px solid var(--c1-traco);border-left:3px solid var(--c1-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c1-legenda);margin:1rem 0 0;}
.aqm-c1-aviso-tabela strong{color:var(--c1-tinta);}
@media (max-width:600px){.aqm-c1-valor{font-size:1.6rem;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 3. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_js' ) ) {
function aquametria_c1_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var BORDA_LIVRE = 3;          /* cm — constante borda-livre-padrao, convenção editorial */
	var VERSAO = 1;

	var raiz = document.querySelector('.aqm-c1');
	if (!raiz) { return; }

	function el(id) { return raiz.querySelector('#' + id); }

	/* Aceita vírgula decimal, que é como se escreve número no Brasil. */
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

	/* Litro: inteiro a partir de 100 L, uma casa abaixo disso. */
	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	function campos() {
		return {
			apelido: (el('aqm-c1-apelido').value || '').trim().slice(0, 40),
			medida: el('aqm-c1-medida').value === 'interna' ? 'interna' : 'externa',
			c: num(el('aqm-c1-c').value),
			l: num(el('aqm-c1-l').value),
			a: num(el('aqm-c1-a').value),
			e: num(el('aqm-c1-e').value),
			lamina: num(el('aqm-c1-lamina').value),
			substrato: num(el('aqm-c1-substrato').value),
			rochas: num(el('aqm-c1-rochas').value)
		};
	}

	/* Núcleo do cálculo. Devolve o objeto de resposta do contrato da Aquametria:
	   nunca um número seco — cada saída carrega o critério que a define. */
	function calcular(d) {
		var r = { erros: [], avisos: [] };

		['c', 'l', 'a'].forEach(function (k) {
			var v = d[k];
			if (v === null) { r.erros.push({ campo: k, texto: 'Informe as três medidas.' }); }
			else if (v <= 0) { r.erros.push({ campo: k, texto: 'Medida precisa ser maior que zero.' }); }
			else if (v > 500) { r.erros.push({ campo: k, texto: 'Acima de 500 cm: confira a unidade (o campo é em centímetros).' }); }
		});
		if (d.e !== null && (d.e <= 0 || d.e > 30)) {
			r.erros.push({ campo: 'e', texto: 'Espessura em milímetros, entre 1 e 30.' });
		}
		if (d.rochas !== null && d.rochas < 0) {
			r.erros.push({ campo: 'rochas', texto: 'Volume de rochas não pode ser negativo.' });
		}
		if (d.substrato !== null && d.substrato < 0) {
			r.erros.push({ campo: 'substrato', texto: 'Altura do substrato não pode ser negativa.' });
		}
		if (r.erros.length) { return r; }

		var e_cm = d.e === null ? null : d.e / 10;
		var externa = (d.medida === 'externa');

		/* Interno: as laterais descontam duas espessuras, a base uma. */
		var c_int = (externa && e_cm !== null) ? d.c - 2 * e_cm : d.c;
		var l_int = (externa && e_cm !== null) ? d.l - 2 * e_cm : d.l;
		var a_int = (externa && e_cm !== null) ? d.a - e_cm : d.a;

		if (c_int <= 0 || l_int <= 0 || a_int <= 0) {
			r.erros.push({ campo: 'e', texto: 'A espessura informada é maior que o próprio aquário. Confira o valor.' });
			return r;
		}

		r.bruto = d.c * d.l * d.a / 1000;

		if (externa && e_cm === null) {
			r.interno = null;
			r.interno_motivo = 'Informe a espessura do vidro. Sem ela não existe volume interno: o desconto do vidro é exatamente a espessura.';
			r.avisos.push('Sem a espessura do vidro, a lâmina foi calculada com as medidas externas e o volume real sai superestimado — em um aquário de 80 × 40 cm, um vidro de 8 mm já responde por cerca de 4 % do volume.');
		} else if (!externa) {
			r.interno = r.bruto;
			r.interno_motivo = 'Você informou medidas internas: o volume interno é o próprio bruto, e não existe desconto de vidro a fazer.';
		} else {
			r.interno = c_int * l_int * a_int / 1000;
		}

		var lamina_max = a_int;
		var lamina = d.lamina;
		if (lamina === null) {
			lamina = Math.max(0, a_int - BORDA_LIVRE);
			r.lamina_padrao = true;
		}
		if (lamina > lamina_max) {
			lamina = lamina_max;
			r.avisos.push('A lâmina informada passava da altura interna do aquário (' + fmt(lamina_max, 1) + ' cm). Usamos a altura interna cheia, que é o máximo físico.');
		}
		if (lamina < 0) { lamina = 0; }
		r.lamina_cm = lamina;
		r.lamina_L = c_int * l_int * lamina / 1000;

		var rochas = d.rochas === null ? 0 : d.rochas;
		r.rochas_L = rochas;
		r.real = r.lamina_L - rochas;
		if (r.real < 0) {
			r.real = 0;
			r.avisos.push('O volume de rochas informado é maior que o volume de água. Confira o número.');
		}

		r.substrato_cm = d.substrato === null ? 0 : d.substrato;
		r.entradas = d;
		r.c_int = c_int; r.l_int = l_int; r.a_int = a_int;
		return r;
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c1-saida');
		var ul = el('aqm-c1-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c1-erro').forEach(function (n) { n.classList.remove('aqm-c1-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c1-' + er.campo);
				if (campo) { campo.classList.add('aqm-c1-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c1-oculto');
			return;
		}

		alvo.classList.remove('aqm-c1-oculto');

		el('aqm-c1-bruto').innerHTML = litros(r.bruto) + '<span class="aqm-c1-unidade">L</span>';
		el('aqm-c1-real').innerHTML = litros(r.real) + '<span class="aqm-c1-unidade">L</span>';

		var cInterno = el('aqm-c1-interno');
		var cIntCrit = el('aqm-c1-interno-criterio');
		if (r.interno === null) {
			cInterno.innerHTML = '<span class="aqm-c1-vazio">sem número</span>';
			cIntCrit.textContent = r.interno_motivo;
		} else {
			cInterno.innerHTML = litros(r.interno) + '<span class="aqm-c1-unidade">L</span>';
			cIntCrit.textContent = r.interno_motivo
				|| ('Medidas internas ' + fmt(r.c_int, 1) + ' × ' + fmt(r.l_int, 1) + ' × ' + fmt(r.a_int, 1) + ' cm, depois de descontar duas espessuras nas laterais e uma na base.');
		}

		el('aqm-c1-real-criterio').textContent =
			'Lâmina de ' + fmt(r.lamina_cm, 1) + ' cm sobre ' + fmt(r.c_int, 1) + ' × ' + fmt(r.l_int, 1) + ' cm'
			+ (r.rochas_L > 0 ? ', menos ' + fmt(r.rochas_L, 1) + ' L de rochas e decoração' : '')
			+ (r.lamina_padrao ? '. A lâmina veio do valor inicial: altura interna menos ' + BORDA_LIVRE + ' cm de borda livre — convenção da Aquametria, ajuste para a sua borda.' : '.');

		var subs = el('aqm-c1-substrato-nota');
		if (r.substrato_cm > 0) {
			subs.classList.remove('aqm-c1-oculto');
			el('aqm-c1-substrato-valor').textContent = fmt(r.substrato_cm, 1);
		} else {
			subs.classList.add('aqm-c1-oculto');
		}

		var av = el('aqm-c1-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		var medidas = fmt(r.entradas.c, 1) + ' × ' + fmt(r.entradas.l, 1) + ' × ' + fmt(r.entradas.a, 1) + ' cm'
			+ (r.entradas.medida === 'externa' ? ' (externas)' : ' (internas)')
			+ (r.entradas.e !== null ? ', vidro de ' + fmt(r.entradas.e, 1) + ' mm' : '');
		el('aqm-c1-citacao').textContent =
			'Aquário de ' + medidas + ', lâmina de ' + fmt(r.lamina_cm, 1) + ' cm: '
			+ litros(r.bruto) + ' L brutos'
			+ (r.interno !== null ? ', ' + litros(r.interno) + ' L internos' : '')
			+ ' e ' + litros(r.real) + ' L reais de referência (substrato não descontado). '
			+ 'Calculado pela Aquametria, ' + AQM_C1_DATA + '.';

		guardar(r);
		atualizarEndereco(r.entradas);
	}

	/* ------------------------------------------------- estado compartilhado */

	/* A C1 é dona das medidas e dos volumes, e sobrescreve os dela sem cerimônia.
	   O que ela NÃO pode fazer é apagar o que as outras calculadoras guardaram
	   sobre o mesmo aquário — voltar aqui para corrigir uma medida não deve
	   zerar a vazão que a C3 calculou nem o clima que a C5 perguntou. Por isso
	   isto é mescla, e não substituição. */
	function guardar(r) {
		var d = r.entradas;
		var estado = recuperar() || {};
		estado.versao = VERSAO;
		estado.calculado_em = new Date().toISOString().slice(0, 10);
		estado.calculadora = 'c1-litragem';
		estado.apelido = d.apelido || estado.apelido || null;
		estado.medidas = { comprimento_cm: d.c, largura_cm: d.l, altura_cm: d.a, tipo_medida: d.medida };
		estado.vidro = { espessura_mm: d.e };
		estado.agua = { altura_lamina_cm: r.lamina_cm, borda_livre_cm: Math.max(0, r.a_int - r.lamina_cm) };
		estado.substrato = { altura_cm: r.substrato_cm || null, tipo: null, porosidade_medida: null };
		estado.decoracao = { volume_rochas_L: r.rochas_L || null };
		estado.volumes = {
			bruto_L: Math.round(r.bruto * 10) / 10,
			interno_L: r.interno === null ? null : Math.round(r.interno * 10) / 10,
			lamina_L: Math.round(r.lamina_L * 10) / 10,
			real_L: Math.round(r.real * 10) / 10,
			real_incerteza: 'substrato não descontado',
			origem: 'calculado na C1'
		};
		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c1-guardado').classList.remove('aqm-c1-oculto');
		} catch (erro) {
			el('aqm-c1-guardado').classList.add('aqm-c1-oculto');
		}
	}

	/* Aceita qualquer estado do aquário, tenha ou não medidas: a C3 e a C5 gravam
	   sem elas, e é justamente esse estado que a mescla precisa preservar. Quem
	   quiser só o aquário já medido confere o.medidas antes de usar. */
	function recuperar() {
		try {
			var bruto = window.localStorage.getItem(CHAVE);
			if (!bruto) { return null; }
			var o = JSON.parse(bruto);
			return (o && typeof o === 'object') ? o : null;
		} catch (erro) { return null; }
	}

	/* ------------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['c=' + d.c, 'l=' + d.l, 'a=' + d.a, 'm=' + d.medida];
		if (d.e !== null) { q.push('e=' + d.e); }
		if (d.lamina !== null) { q.push('lam=' + d.lamina); }
		if (d.substrato !== null) { q.push('sub=' + d.substrato); }
		if (d.rochas !== null) { q.push('roc=' + d.rochas); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c1-link').value = window.location.origin + url;
	}

	function lerQuery() {
		var busca = window.location.search;
		if (!busca || busca.length < 2) { return null; }
		var fora = {};
		busca.substring(1).split('&').forEach(function (par) {
			var p = par.split('=');
			if (p.length === 2) { fora[decodeURIComponent(p[0])] = decodeURIComponent(p[1]); }
		});
		if (!fora.c || !fora.l || !fora.a) { return null; }
		return fora;
	}

	/* ------------------------------------------------------- caminho inverso */

	function inverso() {
		var alvo = el('aqm-c1-inv-alvo').value;
		var v = num(el('aqm-c1-inv-volume').value);
		var m1 = num(el('aqm-c1-inv-m1').value);
		var m2 = num(el('aqm-c1-inv-m2').value);
		var saida = el('aqm-c1-inv-saida');

		if (v === null || m1 === null || m2 === null || v <= 0 || m1 <= 0 || m2 <= 0) {
			saida.textContent = 'Informe o volume desejado e as duas medidas que você já tem, todos maiores que zero.';
			return;
		}
		var terceira = v * 1000 / (m1 * m2);
		var nomes = { comprimento: 'comprimento', largura: 'largura', altura: 'altura' };
		var texto = 'Para ' + fmt(v, 0) + ' L brutos com as outras duas medidas informadas, a ' + nomes[alvo]
			+ ' precisa ser de ' + fmt(Math.round(terceira * 10) / 10, 1) + ' cm.';
		if (alvo === 'altura') {
			var lamina = Math.max(0, terceira - BORDA_LIVRE);
			texto += ' Com a borda livre de ' + BORDA_LIVRE + ' cm, a lâmina ficaria em ' + fmt(Math.round(lamina * 10) / 10, 1)
				+ ' cm e a água em cerca de ' + litros(m1 * m2 * lamina / 1000) + ' L — o volume bruto não é o volume de água.';
		} else {
			texto += ' O número é bruto, medida externa: a água que cabe é sempre menos.';
		}
		saida.textContent = texto;
	}

	/* ------------------------------------------------------------ ligações */

	function preencher(fora) {
		if (fora.c) { el('aqm-c1-c').value = fora.c; }
		if (fora.l) { el('aqm-c1-l').value = fora.l; }
		if (fora.a) { el('aqm-c1-a').value = fora.a; }
		if (fora.e) { el('aqm-c1-e').value = fora.e; }
		if (fora.m === 'interna' || fora.m === 'externa') { el('aqm-c1-medida').value = fora.m; }
		if (fora.lam) { el('aqm-c1-lamina').value = fora.lam; }
		if (fora.sub) { el('aqm-c1-substrato').value = fora.sub; }
		if (fora.roc) { el('aqm-c1-rochas').value = fora.roc; }
	}

	function doEstado(o) {
		var m = o.medidas || {};
		preencher({
			c: m.comprimento_cm, l: m.largura_cm, a: m.altura_cm, m: m.tipo_medida,
			e: (o.vidro || {}).espessura_mm,
			lam: (o.agua || {}).altura_lamina_cm,
			sub: (o.substrato || {}).altura_cm,
			roc: (o.decoracao || {}).volume_rochas_L
		});
		if (o.apelido) { el('aqm-c1-apelido').value = o.apelido; }
	}

	el('aqm-c1-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
	});

	el('aqm-c1-limpar').addEventListener('click', function () {
		el('aqm-c1-form').reset();
		el('aqm-c1-saida').classList.add('aqm-c1-oculto');
		el('aqm-c1-erros').innerHTML = '';
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c1-copiar').addEventListener('click', function () {
		var campo = el('aqm-c1-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c1-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c1-inv-calcular').addEventListener('click', inverso);

	/* Query string manda; senão, o aquário guardado no navegador. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		pintar(calcular(campos()));
	} else {
		var guardadoAntes = recuperar();
		/* Estado gravado só pela C3 ou pela C5 não tem medidas — nesse caso não
		   há o que retomar aqui, e o formulário abre limpo. */
		if (guardadoAntes && guardadoAntes.medidas) {
			doEstado(guardadoAntes);
			el('aqm-c1-retomado').classList.remove('aqm-c1-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_form_html' ) ) {
function aquametria_c1_form_html() {
	$borda = AQUAMETRIA_C1_BORDA_LIVRE_CM;

	$h  = '<form id="aqm-c1-form" class="aqm-c1-painel" novalidate>';
	$h .= '<h3>As medidas do seu aquário</h3>';
	$h .= '<p class="aqm-c1-sub">Em centímetros. O resultado fica guardado no seu navegador e é reaproveitado pelas outras calculadoras — nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c1-opcoes">';
	$h .= '<div class="aqm-c1-campo" style="max-width:16rem">';
	$h .= '<label for="aqm-c1-medida">As medidas que você tem são</label>';
	$h .= '<select id="aqm-c1-medida" name="medida">';
	$h .= '<option value="externa">externas (medidas por fora, com o vidro)</option>';
	$h .= '<option value="interna">internas (por dentro, sem o vidro)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c1-dica">Fita métrica por fora é o caso comum. A loja também anuncia por fora.</span>';
	$h .= '</div></div>';

	$h .= '<div class="aqm-c1-grade">';
	$h .= aquametria_c1_campo( 'c', 'Comprimento (cm)', 'a maior medida da frente', '80' );
	$h .= aquametria_c1_campo( 'l', 'Largura (cm)', 'a profundidade, da frente ao fundo', '40' );
	$h .= aquametria_c1_campo( 'a', 'Altura (cm)', 'do chão do aquário até a borda', '40' );
	$h .= aquametria_c1_campo( 'e', 'Espessura do vidro (mm)', 'sem ela não há volume interno', '8' );
	$h .= aquametria_c1_campo( 'lamina', 'Altura da lâmina d\'água (cm)', 'em branco: altura interna menos ' . $borda . ' cm de borda livre — valor inicial, ajuste para a sua borda', 'ex.: ' . ( 40 - $borda ) );
	$h .= aquametria_c1_campo( 'substrato', 'Altura do substrato (cm)', 'entra como aviso, não como desconto — veja por quê abaixo', 'ex.: 5' );
	$h .= aquametria_c1_campo( 'rochas', 'Rochas e decoração (L)', 'desconto direto, se você souber o volume', 'ex.: 3' );
	$h .= '<div class="aqm-c1-campo">';
	$h .= '<label for="aqm-c1-apelido">Apelido do aquário</label>';
	$h .= '<input type="text" id="aqm-c1-apelido" name="apelido" maxlength="40" placeholder="opcional">';
	$h .= '<span class="aqm-c1-dica">Só para você reconhecer o aquário guardado.</span>';
	$h .= '</div>';
	$h .= '</div>';

	$h .= '<div class="aqm-c1-botoes">';
	$h .= '<button type="submit">Calcular</button>';
	$h .= '<button type="button" class="aqm-c1-secundario" id="aqm-c1-limpar">Limpar</button>';
	$h .= '<span class="aqm-c1-dica aqm-c1-oculto" id="aqm-c1-retomado">Retomamos o aquário que estava guardado neste navegador.</span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c1-avisos" id="aqm-c1-erros"></ul>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c1_campo' ) ) {
function aquametria_c1_campo( $id, $rotulo, $dica, $exemplo ) {
	$h  = '<div class="aqm-c1-campo">';
	$h .= '<label for="aqm-c1-' . esc_attr( $id ) . '">' . esc_html( $rotulo ) . '</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c1-' . esc_attr( $id ) . '"';
	$h .= ' name="' . esc_attr( $id ) . '" placeholder="' . esc_attr( $exemplo ) . '">';
	$h .= '<span class="aqm-c1-dica">' . esc_html( $dica ) . '</span>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c1_resposta_html' ) ) {
function aquametria_c1_resposta_html() {
	$h  = '<div class="aqm-c1-resultado aqm-c1-oculto" id="aqm-c1-saida" aria-live="polite">';

	$h .= '<ul class="aqm-c1-cartoes">';
	$h .= '<li class="aqm-c1-cartao"><span class="aqm-c1-rotulo">Volume bruto</span>';
	$h .= '<span class="aqm-c1-valor" id="aqm-c1-bruto">—<span class="aqm-c1-unidade">L</span></span>';
	$h .= '<p class="aqm-c1-criterio">Comprimento × largura × altura ÷ 1000. É o número que a loja anuncia e o que a busca pergunta — não é a água que cabe.</p></li>';

	$h .= '<li class="aqm-c1-cartao"><span class="aqm-c1-rotulo">Volume interno</span>';
	$h .= '<span class="aqm-c1-valor" id="aqm-c1-interno">—</span>';
	$h .= '<p class="aqm-c1-criterio" id="aqm-c1-interno-criterio"></p></li>';

	$h .= '<li class="aqm-c1-cartao aqm-c1-destaque"><span class="aqm-c1-rotulo">Volume real de referência</span>';
	$h .= '<span class="aqm-c1-valor" id="aqm-c1-real">—<span class="aqm-c1-unidade">L</span></span>';
	$h .= '<p class="aqm-c1-criterio" id="aqm-c1-real-criterio"></p></li>';
	$h .= '</ul>';

	$h .= '<ul class="aqm-c1-avisos" id="aqm-c1-avisos"></ul>';

	$h .= '<p class="aqm-c1-nota"><strong>É o volume real que vale.</strong> Ele é a única entrada de volume que as outras calculadoras da Aquametria leem — filtro, aquecedor, mídia, consumo e lotação partem dele, não do número da loja. ';
	$h .= '<span id="aqm-c1-guardado" class="aqm-c1-oculto">Este aquário ficou guardado neste navegador.</span></p>';

	$h .= '<p class="aqm-c1-nota aqm-c1-nota-alerta aqm-c1-oculto" id="aqm-c1-substrato-nota">';
	$h .= '<strong>O seu substrato de <span id="aqm-c1-substrato-valor">0</span> cm não foi descontado, e isso é deliberado.</strong> ';
	$h .= 'Descontar substrato exige saber a porosidade do leito — quanta água fica entre os grãos. As fontes brasileiras divergem em 100 % na densidade do substrato (1 a 2 kg/L contra 1 kg ≈ 1 L) e nenhuma publica porosidade, então a constante está pendente e constante pendente é proibida em fórmula publicada aqui. ';
	$h .= 'Consequência assumida: o volume real acima está <strong>superestimado</strong>. Para filtro, aquecedor e mídia o erro é seguro (pede equipamento maior). Para lotação e dosagem ele é inseguro — por isso a calculadora de lotação usa o pior caso, e a de dosagem não entrou no lote inicial.</p>';

	$h .= '<div class="aqm-c1-citar">';
	$h .= '<p id="aqm-c1-citacao"></p>';
	$h .= '<div class="aqm-c1-campo"><label for="aqm-c1-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c1-link" readonly></div>';
	$h .= '<div class="aqm-c1-botoes"><button type="button" class="aqm-c1-secundario" id="aqm-c1-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c1-dica" id="aqm-c1-copiado"></span></div>';
	$h .= '</div>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c1_inverso_html' ) ) {
function aquametria_c1_inverso_html() {
	$h  = '<div class="aqm-c1-painel">';
	$h .= '<h3>Caminho inverso: quero um aquário de tantos litros</h3>';
	$h .= '<p class="aqm-c1-sub">Você tem o volume que quer e duas das três medidas. Devolvemos a terceira, no volume bruto.</p>';
	$h .= '<div class="aqm-c1-grade">';
	$h .= '<div class="aqm-c1-campo"><label for="aqm-c1-inv-volume">Volume desejado (L)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c1-inv-volume" placeholder="100"></div>';
	$h .= '<div class="aqm-c1-campo"><label for="aqm-c1-inv-alvo">Quero descobrir a</label>';
	$h .= '<select id="aqm-c1-inv-alvo"><option value="altura">altura</option><option value="comprimento">comprimento</option><option value="largura">largura</option></select></div>';
	$h .= '<div class="aqm-c1-campo"><label for="aqm-c1-inv-m1">Primeira medida que tenho (cm)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c1-inv-m1" placeholder="80"></div>';
	$h .= '<div class="aqm-c1-campo"><label for="aqm-c1-inv-m2">Segunda medida que tenho (cm)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c1-inv-m2" placeholder="40"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c1-botoes"><button type="button" id="aqm-c1-inv-calcular">Descobrir a medida</button></div>';
	$h .= '<p class="aqm-c1-criterio" id="aqm-c1-inv-saida"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c1_fontes_html' ) ) {
function aquametria_c1_fontes_html() {
	$h  = '<div class="aqm-c1-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c1-sub">Verificado em ' . esc_html( AQUAMETRIA_C1_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C1_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c1-rolagem"><table class="aqm-c1-fontes">';
	$h .= '<tr><th>Constante ou regra</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';
	$h .= '<tr><td>volume</td><td>C × L × A ÷ 1000</td><td>Geometria. Não é constante nem opinião: é a definição de litro em centímetros cúbicos. Aqui as fontes convergem, então a resposta é um número só — e a página diz que houve convergência, em vez de fabricar uma faixa.</td></tr>';
	$h .= '<tr><td>desconto do vidro</td><td>2 espessuras nas laterais, 1 na base</td><td>Geometria da caixa colada: cada parede lateral entra duas vezes no comprimento e na largura; a base entra uma vez na altura. O vidro da tampa não conta porque a água não chega nela.</td></tr>';
	$h .= '<tr><td>borda-livre-padrao</td><td>' . esc_html( AQUAMETRIA_C1_BORDA_LIVRE_CM ) . ' cm <span class="aqm-c1-selo">convenção editorial</span></td><td>Convenção da Aquametria para o valor inicial do campo da lâmina, não dado técnico de fabricante. Ajuste para a sua borda: a diferença entre 2 e 5 cm de borda livre chega a 7 % do volume em um aquário de 40 cm de altura.</td></tr>';
	$h .= '<tr><td>substrato-porosidade</td><td>sem valor <span class="aqm-c1-selo">pendente</span></td><td>Nenhuma fonte brasileira publica a fração de vazios do leito. Sem ela não há como converter altura de substrato em volume deslocado, e a Aquametria não publica número que não tem origem. A medição própria está desenhada: recipiente graduado, substrato seco até uma marca, água até cobrir os grãos, três repetições por tipo de grão.</td></tr>';
	$h .= '<tr><td>substrato-densidade</td><td>1 a 2 kg/L contra 1 kg ≈ 1 L <span class="aqm-c1-selo">pendente</span></td><td>Duas fontes brasileiras do levantamento, com 100 % de diferença entre si. Divergência desse tamanho não vira média: fica registrada e a fórmula não usa nenhuma das duas.</td></tr>';
	$h .= '</table></div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c1_adiante_html' ) ) {
function aquametria_c1_adiante_html() {
	$hub  = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadoras' ) : home_url( '/calculadoras/' );
	$meto = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'metodologia' ) : home_url( '/metodologia/' );
	$c3   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-vazao-do-filtro' ) : home_url( '/calculadora-de-vazao-do-filtro/' );
	$c5   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-potencia-do-aquecedor' ) : home_url( '/calculadora-de-potencia-do-aquecedor/' );
	$c12  = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-midia-filtrante' ) : home_url( '/calculadora-de-midia-filtrante/' );
	$c15  = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-iluminacao' ) : home_url( '/calculadora-de-iluminacao/' );

	$h  = '<div class="aqm-c1-painel aqm-c1-adiante">';
	$h .= '<h3>O que este resultado alimenta</h3>';
	$h .= '<p class="aqm-c1-sub">O volume real fica guardado no seu navegador e é lido por todas as calculadoras abaixo. Você não vai redigitar medidas.</p>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $c3 ) . '"><strong>Vazão do filtro e turnover (C3)</strong></a> — <strong>já no ar.</strong> Quantas renovações por hora o seu filtro entrega, e por que o fabricante dimensiona 1,76 x/h enquanto a web brasileira pede de 5 a 10. Ela lê o volume desta página sozinha.</li>';
	$h .= '<li><a href="' . esc_url( $c5 ) . '"><strong>Potência do aquecedor (C5)</strong></a> — <strong>já no ar.</strong> Watts a partir da mínima do cômodo onde o aquário fica, e não do velho "1 W por litro" que nenhuma fonte explica. Também lê o volume desta página sozinha.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — <strong>já no ar.</strong> Mililitros de mídia biológica por litro de água, pelas quatro dosagens que os fabricantes declaram e que discordam por dez vezes entre si — mais o teto físico do cesto do seu filtro. Também lê o volume desta página sozinha.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — <strong>já no ar.</strong> Quantos lúmens o volume desta página pede, pelas três leituras brasileiras que chamam a mesma faixa pelo mesmo nome com o dobro do número. Ela lê daqui o volume, o comprimento e a altura da lâmina — e é a lâmina que decide se a régua de lúmens por litro ainda descreve o seu aquário.</li>';
	$h .= '<li><strong>Lotação (C8)</strong> — três critérios publicados lado a lado. É a única que trata o volume desta página pelo pior caso, porque aqui o erro do substrato seria inseguro.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c1-criterio">Elas entram no ar uma por vez, e cada uma só entra com a fonte de cada constante conferida. Acompanhe em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>, ou leia antes <a href="' . esc_url( $meto ) . '">como a Aquametria calcula</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 4b. VISIBILIDADE EM IA (seção 5 do ARQUIPELAGO.md) — as três peças
 *
 * Uma calculadora que só calcula em JavaScript mostra a um modelo de linguagem
 * um formulário VAZIO, nunca um número. As três peças que resolvem isso são a
 * resposta antes da explicação, a tabela de exemplos já resolvida no HTML
 * servido e o JSON-LD — e nenhuma delas pode contradizer a calculadora logo
 * acima dela. Por isso tudo aqui é ESPELHO em PHP das mesmas funções do script,
 * função a função, e o teste de navegador compara a tabela servida com o que a
 * calculadora devolve para a mesma entrada.
 *
 * O EIXO DESTA TABELA É O CENTÍMETRO, e não o litro como na C3, na C5 e na C12.
 * Não é gosto: aqui o litro é a SAÍDA. Quem procura esta página digita as
 * medidas que tem na fita métrica ("quantos litros tem um aquário de 60 × 30 ×
 * 35"), nunca o volume — se soubesse o volume, não precisaria da calculadora.
 * Uma tabela indexada por litro responderia à pergunta que a pessoa ainda não
 * consegue fazer. A escada de comprimento é a mesma da C15 (30, 45, 60, 80, 90
 * e 120 cm), de propósito: é a escada em que a luminária é vendida, e repetir a
 * mesma faixa deixa as duas páginas comparáveis entre si.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_url' ) ) {
function aquametria_c1_url( $slug ) {
	return function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( $slug )
		: home_url( '/' . $slug . '/' );
}
}

/* Espelho em PHP do fmt() do script. */
if ( ! function_exists( 'aquametria_c1_fmt' ) ) {
function aquametria_c1_fmt( $n, $casas ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return number_format_i18n( $n, $casas );
}
}

/* Espelho em PHP do litros() do script: inteiro a partir de 100 L, uma casa
   abaixo disso. Se este arredondamento divergir do JavaScript, a tabela servida
   passa a afirmar um número e a calculadora outro na mesma página. */
if ( ! function_exists( 'aquametria_c1_litros' ) ) {
function aquametria_c1_litros( $n ) {
	if ( null === $n || ! is_numeric( $n ) ) {
		return '—';
	}
	return ( $n >= 100 ) ? aquametria_c1_fmt( round( $n ), 0 ) : aquametria_c1_fmt( round( $n * 10 ) / 10, 1 );
}
}

/* Os seis aquários da tabela servida.
 *
 * ATENÇÃO ao que estas linhas são e ao que NÃO são: são as ENTRADAS de um
 * exemplo — medidas de fita métrica e espessura de vidro digitadas no
 * formulário —, exatamente como os volumes de 30 a 300 L são entradas nas
 * tabelas da C3 e da C5. Não são um catálogo de modelos de fabricante e não são
 * recomendação de espessura: a Aquametria não dimensiona vidro, e a tabela diz
 * isso na nota logo abaixo dela. A saída, essa sim, é dado próprio: sai da
 * geometria, que é definição e não constante de terceiro.
 */
if ( ! function_exists( 'aquametria_c1_casos_exemplo' ) ) {
function aquametria_c1_casos_exemplo() {
	return array(
		array( 'c' => 30,  'l' => 25, 'a' => 30, 'e' => 4 ),
		array( 'c' => 45,  'l' => 30, 'a' => 30, 'e' => 5 ),
		array( 'c' => 60,  'l' => 30, 'a' => 35, 'e' => 6 ),
		array( 'c' => 80,  'l' => 40, 'a' => 40, 'e' => 8 ),
		array( 'c' => 90,  'l' => 45, 'a' => 45, 'e' => 8 ),
		array( 'c' => 120, 'l' => 50, 'a' => 50, 'e' => 10 ),
	);
}
}

/* Resolve um caso com as MESMAS regras do calcular() do script, no ramo em que
   a tabela o coloca: medidas externas, lâmina em branco (ou seja, o valor
   inicial de altura interna menos a borda livre), sem substrato e sem rochas.
   Qualquer divergência daqui para lá é a página se contradizendo. */
if ( ! function_exists( 'aquametria_c1_exemplo' ) ) {
function aquametria_c1_exemplo( $caso ) {
	$e_cm = $caso['e'] / 10;

	$c_int = $caso['c'] - 2 * $e_cm;
	$l_int = $caso['l'] - 2 * $e_cm;
	$a_int = $caso['a'] - $e_cm;

	$bruto   = $caso['c'] * $caso['l'] * $caso['a'] / 1000;
	$interno = $c_int * $l_int * $a_int / 1000;

	$lamina = max( 0, $a_int - AQUAMETRIA_C1_BORDA_LIVRE_CM );
	$real   = $c_int * $l_int * $lamina / 1000;

	return array(
		'c'         => $caso['c'],
		'l'         => $caso['l'],
		'a'         => $caso['a'],
		'e'         => $caso['e'],
		'c_int'     => $c_int,
		'l_int'     => $l_int,
		'a_int'     => $a_int,
		'bruto'     => $bruto,
		'interno'   => $interno,
		'lamina_cm' => $lamina,
		'real'      => $real,
		/* A porcentagem sai dos valores CRUS, nunca da subtração dos números já
		   arredondados da tela — senão a coluna passaria a discordar de si mesma
		   por causa da própria formatação. */
		'perda_pct' => ( $bruto > 0 ) ? ( $bruto - $real ) / $bruto * 100 : null,
	);
}
}

/* ---- A resposta antes da explicação (seção 5, item 2 do ARQUIPELAGO.md) ---
   Frase autossuficiente: precisa sobreviver a ser citada fora de contexto, por
   um modelo de linguagem que leu só este parágrafo. Por isso repete as medidas,
   os três números, a unidade e a data em vez de dizer "veja acima". */
if ( ! function_exists( 'aquametria_c1_resposta_direta_html' ) ) {
function aquametria_c1_resposta_direta_html() {
	$casos = aquametria_c1_casos_exemplo();
	$e80   = aquametria_c1_exemplo( $casos[3] ); /* 80 × 40 × 40, vidro de 8 mm */
	$e120  = aquametria_c1_exemplo( $casos[5] );

	$h  = '<div class="aqm-c1-direta">';

	$h .= '<p><strong>A resposta curta.</strong> Um aquário não tem um volume: tem três, e eles não são o mesmo número. ';
	$h .= 'Um aquário de ' . esc_html( aquametria_c1_fmt( $e80['c'], 0 ) ) . ' × ' . esc_html( aquametria_c1_fmt( $e80['l'], 0 ) )
		. ' × ' . esc_html( aquametria_c1_fmt( $e80['a'], 0 ) ) . ' cm medidos por fora, com vidro de '
		. esc_html( aquametria_c1_fmt( $e80['e'], 0 ) ) . ' mm, tem <strong>' . esc_html( aquametria_c1_litros( $e80['bruto'] ) )
		. ' L brutos</strong> — que é o número da etiqueta —, <strong>' . esc_html( aquametria_c1_litros( $e80['interno'] ) )
		. ' L internos</strong> depois de descontar o vidro, e <strong>' . esc_html( aquametria_c1_litros( $e80['real'] ) )
		. ' L de água de verdade</strong> com a lâmina em ' . esc_html( aquametria_c1_fmt( $e80['lamina_cm'], 1 ) ) . ' cm. ';
	$h .= 'São ' . esc_html( aquametria_c1_fmt( round( $e80['perda_pct'] ), 0 ) ) . ' % a menos que a etiqueta. ';
	$h .= 'Verificado em ' . esc_html( AQUAMETRIA_C1_VERIFICADO_EM ) . '.</p>';

	$h .= '<p><strong>É o terceiro número que dimensiona o equipamento.</strong> ';
	$h .= 'Filtro, aquecedor, mídia biológica e iluminação são escolhidos pela água que existe, não pela que caberia se o aquário fosse uma caixa vazia sem vidro e cheia até a borda. ';
	$h .= 'Dimensionar pelo número da loja é dimensionar por um aquário que não existe — e o erro cresce com a espessura do vidro e com a borda livre: ';
	$h .= 'de ' . esc_html( aquametria_c1_fmt( round( $e120['perda_pct'] ), 0 ) ) . ' % num aquário de '
		. esc_html( aquametria_c1_fmt( $e120['c'], 0 ) ) . ' cm de frente a '
		. esc_html( aquametria_c1_fmt( round( aquametria_c1_exemplo( $casos[0] )['perda_pct'] ), 0 ) ) . ' % num nano de '
		. esc_html( aquametria_c1_fmt( $casos[0]['c'], 0 ) ) . ' cm, onde o vidro pesa mais em proporção.</p>';

	$h .= '<p><strong>De onde vem cada conta, sem constante emprestada.</strong> ';
	$h .= 'O volume bruto é comprimento × largura × altura ÷ 1000: geometria, a definição de litro em centímetros cúbicos, e não uma constante de terceiro que precise de fonte. ';
	$h .= 'O desconto do vidro também é geometria da caixa colada — duas espessuras no comprimento, duas na largura, uma na base; o vidro da tampa não entra porque a água não chega nele. ';
	$h .= 'A única escolha editorial da página é a borda livre de ' . esc_html( AQUAMETRIA_C1_BORDA_LIVRE_CM ) . ' cm, que é o valor inicial do campo da lâmina, está rotulada como convenção da Aquametria e é para você ajustar: ';
	$h .= 'num aquário de 40 cm de altura, a diferença entre 2 e 5 cm de borda livre chega a 7 % do volume.</p>';

	$h .= '<p><strong>E o que esta conta não desconta: o substrato.</strong> ';
	$h .= 'Descontar substrato exige a porosidade do leito — quanta água fica entre os grãos —, e nenhuma fonte brasileira do levantamento publica esse número; ';
	$h .= 'as duas que publicam densidade discordam em 100 % entre si — uma diz de 1 a 2 kg por litro, a outra trata 1 kg como um litro. ';
	$h .= 'Constante pendente é proibida dentro de fórmula publicada aqui, então a página não desconta e declara a consequência: ';
	$h .= 'o volume real acima está <strong>superestimado</strong>. Para filtro, aquecedor e mídia esse erro é seguro, porque pede equipamento maior; para lotação e dosagem ele é inseguro, e é por isso que a calculadora de lotação trata este número pelo pior caso.</p>';

	$h .= '</div>';
	return $h;
}
}

/* ---- A tabela de exemplos servida (seção 5, item 1) ---------------------- */
if ( ! function_exists( 'aquametria_c1_exemplos_html' ) ) {
function aquametria_c1_exemplos_html() {
	/* A classe -bloco-exemplos marca o BLOCO (painel inteiro); a -exemplos marca a
	   TABELA. São duas coisas, e separá-las é o que permite ao
	   teste-navegador-visibilidade-ia.mjs achar a tabela, o aviso e a última
	   coluna sem depender de qual calculadora está sendo medida. Nenhuma delas
	   reaproveita .aqm-c1-fontes, que é o localizador da tabela de constantes —
	   duas tabelas com a mesma classe quebram o teste, e isso já custou duas
	   rodadas na C15. */
	$h  = '<div class="aqm-c1-painel aqm-c1-bloco-exemplos">';
	$h .= '<h3>Seis aquários já resolvidos, do nano ao de sala</h3>';
	$h .= '<p class="aqm-c1-sub">É a mesma conta do formulário acima, aplicada a seis conjuntos de medidas, com a lâmina no valor inicial e sem substrato nem rochas. ';
	$h .= 'Estes números estão prontos no HTML desta página — não é preciso preencher nada, e quem lê sem executar JavaScript vê os mesmos valores que a calculadora devolve.</p>';

	$h .= '<div class="aqm-c1-rolagem"><table class="aqm-c1-exemplos">';
	$h .= '<tr><th>Aquário</th><th>Volume bruto</th><th>Volume interno</th>';
	$h .= '<th>Volume real de referência</th><th>O que muda ao usar o número certo</th></tr>';

	foreach ( aquametria_c1_casos_exemplo() as $caso ) {
		$e = aquametria_c1_exemplo( $caso );

		$medidas = aquametria_c1_fmt( $e['c'], 0 ) . ' × ' . aquametria_c1_fmt( $e['l'], 0 ) . ' × ' . aquametria_c1_fmt( $e['a'], 0 );

		$h .= '<tr>';

		$h .= '<td><span class="aqm-c1-num">' . esc_html( aquametria_c1_fmt( $e['c'], 0 ) ) . ' cm</span>';
		$h .= '<span class="aqm-c1-un">' . esc_html( $medidas ) . ' cm por fora, vidro de '
			. esc_html( aquametria_c1_fmt( $e['e'], 0 ) ) . ' mm</span></td>';

		$h .= '<td><span class="aqm-c1-num">' . esc_html( aquametria_c1_litros( $e['bruto'] ) ) . ' L</span>';
		$h .= '<span class="aqm-c1-un">' . esc_html( $medidas ) . ' ÷ 1000 — é o que a loja anuncia</span></td>';

		$h .= '<td><span class="aqm-c1-num">' . esc_html( aquametria_c1_litros( $e['interno'] ) ) . ' L</span>';
		$h .= '<span class="aqm-c1-un">por dentro: ' . esc_html( aquametria_c1_fmt( $e['c_int'], 1 ) ) . ' × '
			. esc_html( aquametria_c1_fmt( $e['l_int'], 1 ) ) . ' × ' . esc_html( aquametria_c1_fmt( $e['a_int'], 1 ) )
			. ' cm, já sem o vidro</span></td>';

		$h .= '<td><span class="aqm-c1-num">' . esc_html( aquametria_c1_litros( $e['real'] ) ) . ' L</span>';
		$h .= '<span class="aqm-c1-un">lâmina de ' . esc_html( aquametria_c1_fmt( $e['lamina_cm'], 1 ) )
			. ' cm, que é a altura interna menos a borda livre de ' . esc_html( AQUAMETRIA_C1_BORDA_LIVRE_CM )
			. ' cm — substrato não descontado</span></td>';

		$h .= '<td><span class="aqm-c1-num">' . esc_html( aquametria_c1_fmt( round( $e['perda_pct'] ), 0 ) ) . ' % a menos</span>';
		$h .= '<span class="aqm-c1-un">é este volume real, e não os ' . esc_html( aquametria_c1_litros( $e['bruto'] ) )
			. ' L da etiqueta, que a vazão do filtro, a potência do aquecedor, a mídia biológica e a iluminação leem — '
			. 'dimensionar pelo bruto compra equipamento para uma água que não está lá</span></td>';

		$h .= '</tr>';
	}

	$h .= '</table></div>';

	$h .= '<p class="aqm-c1-criterio" style="margin-top:.8rem">Como ler a tabela. ';
	$h .= 'A primeira coluna é o comprimento da frente, que é como o aquário e a luminária são vendidos — as medidas completas e a espessura vêm logo abaixo dele, e são as <strong>entradas</strong> do exemplo, não um catálogo de modelos: ';
	$h .= 'a Aquametria não dimensiona vidro e esta página não diz qual espessura o seu aquário deveria ter. ';
	$h .= 'A segunda coluna é o número da etiqueta. A terceira desconta o vidro. A quarta é a água que existe, e é a única que dimensiona equipamento. ';
	$h .= 'A quinta é a distância entre a primeira e a quarta, que é justamente o motivo de esta página existir. ';
	$h .= 'Nenhum valor foi digitado à mão: todos saem das mesmas regras que a calculadora usa, calculados no servidor a cada carregamento.</p>';

	$divulgacao = aquametria_c1_url( AQUAMETRIA_C1_PAGINA_AFILIADOS );

	/* Classe própria (-aviso-tabela), e não a do aviso de publicidade do bloco de
	   produto: o teste de navegador localiza o aviso da tabela em modo estrito, e
	   duas ocorrências da mesma classe quebram o localizador. */
	$h .= '<p class="aqm-c1-aviso-tabela"><strong>Sobre a última coluna, e sobre o que esta tabela não faz.</strong> ';
	$h .= 'Nenhuma linha aqui leva a loja nenhuma, e isso não é esquecimento: litragem é geometria, e geometria não escolhe produto. ';
	$h .= 'Quem escolhe filtro, aquecedor, mídia ou luminária são as calculadoras que leem este volume, e é lá que o bloco de produto nasce — dentro da resposta, como consequência do cálculo, com a especificação que fez cada produto entrar. ';
	$h .= 'Por isso esta página não tem link de afiliado e não gera comissão nenhuma. Onde eles existem na Aquametria, saem marcados como patrocinados, com o aviso ao lado. ';
	$h .= 'Preço não entra nem aqui nem lá: preço muda toda semana e número velho na tela é pior que nenhum, então o que publicamos é a especificação e a data em que ela foi conferida. ';
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
if ( ! function_exists( 'aquametria_c1_jsonld_dados' ) ) {
function aquametria_c1_jsonld_dados() {
	$url = aquametria_c1_url( AQUAMETRIA_C1_SLUG );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$app = array(
		'@type'                  => 'WebApplication',
		'@id'                    => $url . '#calculadora',
		'name'                   => 'Calculadora de litragem de aquário',
		'alternateName'          => 'Aquametria C1 — quantos litros tem o seu aquário',
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
		'softwareVersion' => AQUAMETRIA_C1_VERSAO,
		'description'     => 'Converte as medidas do aquário em centímetros nos três volumes que não são o mesmo número: o bruto que a loja anuncia, '
			. 'o interno depois de descontar a espessura do vidro e o volume real de água, que é a lâmina sobre a área interna menos rochas e decoração. '
			. 'É o volume real que dimensiona filtro, aquecedor, mídia e iluminação, e ele fica guardado no navegador do visitante para as outras calculadoras da Aquametria lerem.',
		'featureList' => array(
			'Volume bruto, interno e real de referência separados, cada um com o critério que o define',
			'Desconto do vidro pela geometria da caixa colada: duas espessuras nas laterais, uma na base',
			'Lâmina d\'água com valor inicial declarado como convenção editorial, não como dado de fabricante',
			'Recusa explícita de descontar substrato, com a consequência do erro declarada na tela',
			'Caminho inverso: o volume desejado e duas medidas devolvem a terceira',
			'Resultado guardado no próprio navegador e reaproveitado pelas outras calculadoras, sem conta e sem envio a servidor',
			'Link permanente da resposta, para conferir ou compartilhar o mesmo cálculo',
			'Tabela pré-calculada para seis aquários de 30 a 120 cm de frente, já no HTML servido',
		),
		'publisher'        => $editora,
		'isBasedOn'        => 'Geometria (definição de litro em centímetro cúbico), mais a convenção editorial de borda livre da Aquametria, declarada como tal em '
			. AQUAMETRIA_C1_VERIFICADO_EM,
		'mainEntityOfPage' => $url,
	);

	$perguntas = array();

	foreach ( aquametria_c1_casos_exemplo() as $caso ) {
		$e = aquametria_c1_exemplo( $caso );

		$medidas = aquametria_c1_fmt( $e['c'], 0 ) . ' × ' . aquametria_c1_fmt( $e['l'], 0 ) . ' × ' . aquametria_c1_fmt( $e['a'], 0 );

		$texto = 'Tem três volumes diferentes, e nenhum deles é o outro. O volume bruto é ' . aquametria_c1_litros( $e['bruto'] )
			. ' L (' . $medidas . ' ÷ 1000), que é o número anunciado pela loja. '
			. 'Com vidro de ' . aquametria_c1_fmt( $e['e'], 0 ) . ' mm, o volume interno cai para ' . aquametria_c1_litros( $e['interno'] )
			. ' L, porque cada parede lateral entra duas vezes no comprimento e na largura e a base entra uma vez na altura. '
			. 'E a água de verdade são ' . aquametria_c1_litros( $e['real'] ) . ' L, com a lâmina em '
			. aquametria_c1_fmt( $e['lamina_cm'], 1 ) . ' cm — a altura interna menos ' . AQUAMETRIA_C1_BORDA_LIVRE_CM
			. ' cm de borda livre, que é convenção editorial da Aquametria e não dado de fabricante. '
			. 'Ou seja, ' . aquametria_c1_fmt( round( $e['perda_pct'] ), 0 ) . ' % a menos que a etiqueta. '
			. 'É o volume real que dimensiona filtro, aquecedor, mídia e iluminação. O substrato não está descontado, então esse número está superestimado. '
			. 'Verificado em ' . AQUAMETRIA_C1_VERIFICADO_EM . '.';

		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => 'Quantos litros tem um aquário de ' . $medidas . ' cm?',
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $texto ),
		);
	}

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'O volume que a loja anuncia é a água que cabe no aquário?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Não, e a diferença não é pequena: nos seis aquários calculados nesta página ela vai de 13 % a 17 % do volume anunciado. '
				. 'O número da loja é o volume bruto, comprimento × largura × altura por fora, dividido por 1000 — uma caixa maciça, sem vidro e cheia até a borda. '
				. 'A água real é menor por dois motivos somados: o vidro ocupa espaço (duas espessuras no comprimento, duas na largura, uma na base) e a lâmina d\'água para antes da borda. '
				. 'Num aquário de 80 × 40 × 40 cm com vidro de 8 mm, os 128 L da etiqueta viram 118 L internos e 109 L de água com a lâmina em 36,2 cm. '
				. 'Rochas e substrato ainda tiram mais. Dimensionar filtro ou aquecedor pelo número da etiqueta é dimensionar por um aquário que não existe.',
		),
	);

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Como descontar a espessura do vidro do volume do aquário?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Pela geometria da caixa colada, não por um percentual de segurança. Cada parede lateral entra DUAS vezes no comprimento e duas vezes na largura, '
				. 'e a base entra UMA vez na altura; o vidro da tampa não conta, porque a água não chega nele. '
				. 'Com vidro de 8 mm (0,8 cm), um aquário de 80 × 40 × 40 cm por fora tem 78,4 × 38,4 × 39,2 cm por dentro, ou seja, 118 L internos contra 128 L brutos: quase 10 L só de vidro. '
				. 'Sem a espessura informada esse número não existe, e a Aquametria devolve "sem número" em vez de chutar uma espessura provável — '
				. 'chutar 6 ou 10 mm mudaria o resultado em vários litros sem que o visitante soubesse que houve chute.',
		),
	);

	$perguntas[] = array(
		'@type'          => 'Question',
		'name'           => 'Por que a calculadora não desconta o substrato do volume?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Porque o desconto correto depende da porosidade do leito — quanta água fica entre os grãos —, e nenhuma fonte brasileira do levantamento publica esse número. '
				. 'As duas que publicam densidade de substrato discordam em 100 % entre si: uma diz de 1 a 2 kg por litro, a outra trata 1 kg como 1 litro. '
				. 'Divergência desse tamanho não vira média na Aquametria, e constante com status pendente é proibida dentro de fórmula publicada. '
				. 'A consequência é declarada em vez de escondida: o volume real fica superestimado. '
				. 'Para filtro, aquecedor e mídia esse erro é seguro, porque leva a equipamento maior; para lotação e dosagem ele é inseguro, '
				. 'e por isso a calculadora de lotação usa o pior caso e a de dosagem não entrou no lote inicial. '
				. 'A medição própria já está desenhada: recipiente graduado, substrato seco até uma marca, água até cobrir os grãos, três repetições por tipo de grão.',
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

if ( ! function_exists( 'aquametria_c1_imprimir_jsonld' ) ) {
function aquametria_c1_imprimir_jsonld() {
	$json = wp_json_encode( aquametria_c1_jsonld_dados(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-c1-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 5. Entrega do estilo e do comportamento — FORA do retorno do shortcode
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

if ( ! function_exists( 'aquametria_c1_estilo_impresso' ) ) {
function aquametria_c1_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c1_pagina_usa' ) ) {
function aquametria_c1_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_litragem' );
}
}

if ( ! function_exists( 'aquametria_c1_imprimir_estilo' ) ) {
function aquametria_c1_imprimir_estilo() {
	if ( aquametria_c1_estilo_impresso() ) {
		return;
	}
	aquametria_c1_estilo_impresso( true );
	echo '<style id="aquametria-c1-estilo">' . "\n" . aquametria_c1_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c1_cabeca' ) ) {
function aquametria_c1_cabeca() {
	if ( ! aquametria_c1_pagina_usa() ) {
		return;
	}
	aquametria_c1_imprimir_estilo();
	aquametria_c1_imprimir_jsonld();
}
}
add_action( 'wp_head', 'aquametria_c1_cabeca', 20 );

if ( ! function_exists( 'aquametria_c1_rodape' ) ) {
function aquametria_c1_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c1_imprimir_estilo();

	$js = 'var AQM_C1_DATA = ' . wp_json_encode( AQUAMETRIA_C1_VERIFICADO_EM ) . ";\n" . aquametria_c1_js();
	echo '<script id="aquametria-c1-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 6. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c1_shortcode' ) ) {
function aquametria_c1_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c1_rodape', 20 );

	$h  = '<div class="aqm-c1">';
	$h .= aquametria_c1_resposta_direta_html();
	$h .= aquametria_c1_form_html();
	$h .= aquametria_c1_resposta_html();
	$h .= aquametria_c1_exemplos_html();
	$h .= aquametria_c1_inverso_html();
	$h .= aquametria_c1_fontes_html();
	$h .= aquametria_c1_adiante_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_litragem', 'aquametria_c1_shortcode' );

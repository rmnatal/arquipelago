/**
 * Aquametria Calculadora de Litragem — C1
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
	define( 'AQUAMETRIA_C1_VERSAO', '1.0.4' );
	define( 'AQUAMETRIA_C1_SLUG', 'calculadora-de-litragem' );
	define( 'AQUAMETRIA_C1_VERIFICADO_EM', '07/09/2026' );
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
	$h .= aquametria_c1_form_html();
	$h .= aquametria_c1_resposta_html();
	$h .= aquametria_c1_inverso_html();
	$h .= aquametria_c1_fontes_html();
	$h .= aquametria_c1_adiante_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_litragem', 'aquametria_c1_shortcode' );

/**
 * O PISO DA 25.2 NAS QUATRO CATEGORIAS DA F1, MEDIDO COMO A RONDA MEDIU.
 *
 *   node ferramentas/conferir-piso-no-navegador.mjs --autoteste   # sem rede
 *   node ferramentas/conferir-piso-no-navegador.mjs               # a home no ar
 *
 * POR QUE ELE EXISTE. A ronda diaria de 25/11/2026 as 15h1xZ abriu a home no
 * Chrome, EXECUTOU o formulario de verdade e contou `a[href*="shopee"]` no
 * documento depois de cada uma das quatro respostas. Quatro medicoes, quatro
 * ZEROS — e o piso das tres prateleiras estava publicado no banco desde 16/11.
 * **Nenhum portao desta ilha media isso**, e nao por esquecimento: os portoes de
 * ar leem o HTML SERVIDO, e a categoria da F1 e decidida no NAVEGADOR. O que o
 * servidor manda e uma categoria so — a do exemplo —, entao a unica regua capaz
 * de ver as outras tres e uma que preenche o formulario.
 *
 * E E O "PRONTO QUANDO" DO DESPACHO, ao pe da letra: *"executar o formulario no
 * ar e contar `a[href*="shopee"]` no documento depois de cada uma das quatro
 * respostas. Zero em qualquer uma das quatro reprova."* A regua do despacho
 * virou portao em vez de virar uma medicao de um dia.
 *
 * O QUE ELE COBRA, por categoria:
 *   1. a categoria que a tela diz ser (a caixa do veredito), para a entrada nao
 *      ser lida como se tivesse dado outra resposta;
 *   2. pelo menos UM link de loja VISIVEL — visibilidade medida pelo navegador
 *      (`offsetParent`), porque link escondido conta no `querySelectorAll` e nao
 *      e saida de compra para ninguem;
 *   3. `rel` com `sponsored` NO PROPRIO link;
 *   4. a frase do piso nao vazia e sem molde cru (`{prateleira}` na tela);
 *   5. nenhum `href` vazio na pagina — botao que recarrega a propria pagina com o
 *      rotulo da loja do lado e a cicatriz de 30/10/2026 nesta ilha.
 *
 * `createRequire` E NAO `import { chromium } from 'playwright'`: nesta nuvem o
 * playwright e alcancado por `NODE_PATH` e o resolvedor de ESM nao le
 * `NODE_PATH` — a causa do despacho de 26/10/2026 ("21 DOS 26 PORTOES DE
 * NAVEGADOR DO ARQUIPELAGO ESTAO INERTES"). Quem copiar este portao copia estas
 * duas linhas junto.
 */
import { createRequire } from 'node:module';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const exigir = createRequire(import.meta.url);

const SITE = process.env.RDM_SITE || 'https://rodametria.com.br';
const LARGURA = 390;

/* As QUATRO entradas sao as da ronda de 25/11/2026, com a categoria que cada uma
   tem de devolver escrita do lado — a regua nao pergunta a resposta ao mesmo
   codigo que a produz. */
const ENTRADAS = [
	{ w: 350, kmh: 25, acel: 'so_pedal_assistido', categoria: 'bicicleta elétrica' },
	{ w: 500, kmh: 25, acel: 'manual', categoria: 'autopropelido' },
	{ w: 1500, kmh: 40, acel: 'manual', categoria: 'ciclomotor' },
	{ w: 5000, kmh: 80, acel: 'manual', categoria: 'acima do ciclomotor' },
];

function acharChrome() {
	if (process.env.RDM_CHROME) return process.env.RDM_CHROME;
	const raiz = process.env.PLAYWRIGHT_BROWSERS_PATH || '/opt/pw-browsers';
	if (!existsSync(raiz)) return null;
	for (const dir of readdirSync(raiz).filter((d) => d.startsWith('chromium')).sort().reverse()) {
		for (const sub of ['chrome-linux64/chrome', 'chrome-linux/chrome']) {
			const caminho = join(raiz, dir, sub);
			if (existsSync(caminho)) return caminho;
		}
	}
	return null;
}

/* ------------------------------------------------------------------ o veredito

   Funcao PURA sobre o que a pagina disse, para o autoteste FABRICAR os mundos
   que a ilha sadia nao tem — e o mundo que importa (zero link de loja) e
   exatamente o que estava no ar hoje e nao esta mais. Regua que nunca viu o
   vermelho nao se sabe viva.                                                 */
export function vereditoDoPiso(colhido) {
	const faltas = [];
	if (colhido.categoriaNaTela !== colhido.categoriaEsperada) {
		faltas.push('a tela diz `' + colhido.categoriaNaTela + '` e a entrada tinha de dar `'
			+ colhido.categoriaEsperada + '`');
	}
	if (!(colhido.linksVisiveis > 0)) {
		faltas.push('ZERO link de loja VISIVEL (25.2-c, regra 2: a pagina serve o piso ou DIZ '
			+ 'que esta sem link de loja — e a frase servida nao diz)');
	}
	if (colhido.linksVisiveis > 0 && !colhido.relSponsored) {
		faltas.push('o link de loja nao traz `sponsored` no proprio `rel`');
	}
	if (!String(colhido.frase || '').trim()) {
		faltas.push('a frase do piso veio vazia: link sem frase e saida de compra sem causa');
	}
	if (String(colhido.frase || '').includes('{')) {
		faltas.push('molde cru na tela: ' + colhido.frase);
	}
	if (colhido.hrefVazio) {
		faltas.push('a pagina serve `href` vazio — botao que recarrega a propria pagina '
			+ '(cicatriz de 30/10/2026)');
	}
	return { aprovado: faltas.length === 0, faltas };
}

function autoteste() {
	const sao = {
		categoriaNaTela: 'ciclomotor', categoriaEsperada: 'ciclomotor',
		linksVisiveis: 1, relSponsored: true, frase: 'a busca de moto elétrica', hrefVazio: false,
	};
	const casos = [
		['o mundo sao', sao, true, 0],
		['O MUNDO MEDIDO EM 25/11: zero link de loja',
			{ ...sao, linksVisiveis: 0 }, false, 1],
		['link escondido nao conta como saida',
			{ ...sao, linksVisiveis: 0 }, false, 1],
		['link sem `sponsored` reprova', { ...sao, relSponsored: false }, false, 1],
		['frase vazia reprova', { ...sao, frase: '   ' }, false, 1],
		['molde cru na tela reprova',
			{ ...sao, frase: 'a busca de {prateleira}' }, false, 1],
		['`href` vazio reprova', { ...sao, hrefVazio: true }, false, 1],
		['categoria trocada reprova', { ...sao, categoriaNaTela: 'autopropelido' }, false, 1],
		['duas faltas somam',
			{ ...sao, linksVisiveis: 0, frase: '' }, false, 2],
	];
	let falhas = 0;
	for (const [nome, mundo, aprovadoEsperado, faltasEsperadas] of casos) {
		const v = vereditoDoPiso(mundo);
		const ok = v.aprovado === aprovadoEsperado && v.faltas.length === faltasEsperadas;
		console.log((ok ? '  ok   ' : '  FALHA') + '  ' + nome
			+ ' -> aprovado=' + v.aprovado + ', faltas=' + v.faltas.length);
		if (!ok) falhas++;
	}

	/* A REGUA VELHA AO LADO DA NOVA, E AS DUAS TEM DE DISCORDAR (20.8). A velha e
	   a que esta ilha tinha: os portoes de ar leem o HTML SERVIDO, onde existe UMA
	   categoria — a do exemplo. Lida assim, a home de hoje as 15h1xZ passava, e
	   passou: o despacho de 25/11 nasceu de uma medicao FEITA A MAO, nao de um
	   portao. A nova varre as quatro. */
	const velha = (mundos) => mundos.slice(0, 1).every((m) => vereditoDoPiso(m).aprovado);
	const nova = (mundos) => mundos.every((m) => vereditoDoPiso(m).aprovado);
	const mundoMedido = [
		sao,                                   /* a do exemplo, que o servidor serve */
		{ ...sao, categoriaNaTela: 'bicicleta elétrica',
			categoriaEsperada: 'bicicleta elétrica', linksVisiveis: 0 },
	];
	const discordam = velha(mundoMedido) === true && nova(mundoMedido) === false;
	console.log((discordam ? '  ok   ' : '  FALHA')
		+ '  NO MUNDO MEDIDO a regua VELHA (so a categoria servida) aprova e a NOVA '
		+ '(as quatro) reprova');
	if (!discordam) falhas++;
	const mundoSao = [sao, { ...sao, categoriaNaTela: 'bicicleta elétrica',
		categoriaEsperada: 'bicicleta elétrica' }];
	const concordam = velha(mundoSao) === true && nova(mundoSao) === true;
	console.log((concordam ? '  ok   ' : '  FALHA')
		+ '  NO MUNDO SAO as duas CONCORDAM — o conserto nao aperta o que nao e defeito');
	if (!concordam) falhas++;

	console.log('');
	console.log(falhas ? 'REPROVADO: ' + falhas + ' falha(s)' : 'APROVADO: ' + (casos.length + 2) + ' mundos');
	return falhas ? 1 : 0;
}

async function medir() {
	const { chromium } = exigir('playwright');
	const exe = acharChrome();
	const nav = await chromium.launch(exe ? { executablePath: exe, args: ['--no-sandbox'] } : {});
	const pag = await (await nav.newContext({ viewport: { width: LARGURA, height: 900 } })).newPage();
	let falhas = 0;

	await pag.goto(SITE + '/?v=' + Date.now(), { waitUntil: 'networkidle' });

	for (const e of ENTRADAS) {
		await pag.selectOption('[data-rdm-f1-w]', String(e.w));
		await pag.selectOption('[data-rdm-f1-kmh]', String(e.kmh));
		await pag.check('#rdm-f1-acel-' + e.acel.replace(/_/g, '-'));
		await pag.waitForTimeout(250);

		const colhido = await pag.evaluate(() => {
			const num = document.querySelector('.rdm-molde-caixa-numero .rdm-num');
			const frase = document.querySelector('[data-rdm-piso-frase]');
			const links = Array.from(document.querySelectorAll('a[href*="shopee"]'));
			const visiveis = links.filter((a) => a.offsetParent !== null);
			return {
				categoriaNaTela: num ? num.textContent.trim() : '(sem caixa)',
				frase: frase ? frase.textContent.trim() : '',
				linksTotais: links.length,
				linksVisiveis: visiveis.length,
				destinos: visiveis.map((a) => a.getAttribute('href')),
				relSponsored: visiveis.length > 0
					&& visiveis.every((a) => (a.getAttribute('rel') || '').includes('sponsored')),
				hrefVazio: Array.from(document.querySelectorAll('a')).some(
					(a) => a.hasAttribute('href') && a.getAttribute('href').trim() === ''),
			};
		});
		colhido.categoriaEsperada = e.categoria;
		const v = vereditoDoPiso(colhido);
		console.log((v.aprovado ? '  ok    ' : '  FALHA ')
			+ e.w + ' W · ' + e.kmh + ' km/h · ' + e.acel
			+ ' -> `' + colhido.categoriaNaTela + '`, '
			+ colhido.linksVisiveis + ' link(s) de loja visivel(eis) de '
			+ colhido.linksTotais + ' no documento'
			+ (colhido.destinos.length ? ' -> ' + colhido.destinos.join(' , ') : ''));
		if (colhido.frase) console.log('           frase: ' + colhido.frase);
		for (const f of v.faltas) console.log('           FALTA: ' + f);
		if (!v.aprovado) falhas++;
	}

	await nav.close();
	console.log('');
	console.log(falhas ? 'REPROVADO: ' + falhas + ' de ' + ENTRADAS.length + ' categoria(s)'
		: 'APROVADO: ' + ENTRADAS.length + ' de ' + ENTRADAS.length + ' categorias com piso visivel');
	return falhas ? 1 : 0;
}

const codigo = process.argv.includes('--autoteste') ? autoteste() : await medir();
process.exit(codigo);

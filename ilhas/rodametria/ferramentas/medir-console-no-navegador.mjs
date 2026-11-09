/**
 * "CONSOLE LIMPO" DA 32.5, MEDIDO NAS PAGINAS QUE O SITEMAP SERVE.
 *
 *   node ferramentas/medir-console-no-navegador.mjs --autoteste   # sem rede
 *   node ferramentas/medir-console-no-navegador.mjs               # as paginas do sitemap
 *   node ferramentas/medir-console-no-navegador.mjs --uma /veiculos/
 *
 * POR QUE ELE EXISTE, e a causa esta escrita em `dados/consertos.md` quatro
 * vezes: "console limpo" e uma das cinco exigencias do "pronto quando" da 32.5,
 * e foi a exigencia que as rondas de 04, 06 e 09/11/2026 declararam NAO MEDIDA,
 * sempre pela mesma frase — "nao havia navegador". A frase media a ausencia das
 * ferramentas de navegador (a extensao, o embutido, o shell do computador do
 * Raphael) e nao a ausencia de NAVEGADOR: esta nuvem tem Chromium e Playwright
 * pre-instalados, e a propria ilha ja tinha um portao de pixel usando os dois
 * desde 29/10. O instrumento estava na pasta ao lado da afirmacao "nao medido".
 *
 * O QUE ELE MEDE, por pagina, a 390 px (o telefone que a 32.5 nomeia) e com
 * quebra de cache:
 *
 *   1. toda mensagem de console, POR TIPO — nunca so `error`. Procurar `error` e
 *      a leitura pelo avesso que a 20.8 nomeia: ela acha o que alguem ja
 *      imaginou, e `warning` novo passa calado. O veredito reprova `error` e
 *      `pageerror`, e IMPRIME o resto em vez de o calar.
 *   2. excecao de JavaScript que nao passa pelo console (`pageerror`).
 *   3. requisicao que o navegador tentou e NAO conseguiu (`requestfailed`), que e
 *      como se ve recurso da pagina caido sem nenhum erro de script.
 *   4. resposta com codigo >= 400 entre os recursos da pagina. A pagina responde
 *      200 e carrega uma folha em 404 sem dizer nada a ninguem.
 *
 * ELE DESCOBRE AS PAGINAS: le o `wp-sitemap.xml` no ar. A 32.5-b e literal —
 * "regua que nao varre todas certifica a pagina que o autor abriu".
 *
 * `createRequire` E NAO `import { chromium } from 'playwright'`: nesta nuvem o
 * playwright e alcancado por `NODE_PATH` e o resolvedor de ESM nao le
 * `NODE_PATH`. E o defeito do despacho de 26/10/2026 em `dados/despachos.md`
 * ("21 DOS 26 PORTOES DE NAVEGADOR DO ARQUIPELAGO ESTAO INERTES"), e este
 * arquivo tropecou nele as 19h2xZ de 09/11/2026 — a QUARTA confirmacao da mesma
 * causa. Quem copiar este portao copia estas duas linhas junto.
 */
import { createRequire } from 'node:module';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const exigir = createRequire(import.meta.url);
const { chromium } = exigir('playwright');

const SITE = process.env.RDM_SITE || 'https://rodametria.com.br';
const LARGURA = 390;

/* O caminho do Chromium se DESCOBRE, nunca se fixa: o `teste-navegador-casca.mjs`
   da aquametria aponta para `chromium-1194`, que nao existe mais. Copiado do
   `conferir-32-5-no-navegador.mjs` desta mesma pasta. */
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

   Funcao PURA sobre o que a pagina disse, para o autoteste poder fabricar os
   mundos que a ilha sadia nao tem — regua que nunca viu o vermelho nao se sabe
   viva. REPROVA `error` e `pageerror`; `requestfailed` e resposta >= 400 tambem,
   porque recurso caido e defeito no ar. `warning`, `info` e `log` NAO reprovam e
   sao IMPRESSOS: a 20.8 manda afirmacao positiva, e calar o que nao esta na
   lista e como `gravado mas NAO ativado` chegou ao ar duas vezes.            */
export function vereditoDoConsole(colhido) {
	const porTipo = {};
	for (const m of colhido.mensagens || []) porTipo[m.tipo] = (porTipo[m.tipo] || 0) + 1;
	const graves = [
		...(colhido.mensagens || []).filter((m) => m.tipo === 'error').map((m) => 'console.error: ' + m.texto),
		...(colhido.excecoes || []).map((t) => 'excecao de JavaScript: ' + t),
		...(colhido.falhas || []).map((f) => 'requisicao falhou: ' + f),
		...(colhido.ruins || []).map((r) => 'recurso em ' + r),
	];
	return { limpo: graves.length === 0, graves, porTipo, total: (colhido.mensagens || []).length };
}

function autoteste() {
	const casos = [
		['pagina muda', { mensagens: [], excecoes: [], falhas: [], ruins: [] }, true, 0],
		['so um log', { mensagens: [{ tipo: 'log', texto: 'oi' }] }, true, 0],
		['um warning NAO reprova mas aparece', { mensagens: [{ tipo: 'warning', texto: 'x' }] }, true, 0],
		['console.error reprova', { mensagens: [{ tipo: 'error', texto: 'x is not defined' }] }, false, 1],
		['excecao reprova', { mensagens: [], excecoes: ['TypeError: x'] }, false, 1],
		['recurso caido reprova', { mensagens: [], falhas: ['https://x/f.css (net::ERR)'] }, false, 1],
		['folha em 404 reprova', { mensagens: [], ruins: ['404: https://x/f.css'] }, false, 1],
		['dois graves somam', { mensagens: [{ tipo: 'error', texto: 'a' }], excecoes: ['b'] }, false, 2],
		['colhido vazio nao estoura', {}, true, 0],
	];
	let falhas = 0;
	for (const [nome, mundo, limpoEsperado, gravesEsperados] of casos) {
		const v = vereditoDoConsole(mundo);
		const ok = v.limpo === limpoEsperado && v.graves.length === gravesEsperados;
		console.log((ok ? '  ok   ' : '  FALHA') + '  ' + nome + ' -> limpo=' + v.limpo + ', graves=' + v.graves.length);
		if (!ok) falhas++;
	}
	/* A REGUA INGENUA AO LADO DA NOVA, E AS DUAS TEM DE DISCORDAR (20.8): quem
	   procura a palavra `error` no texto nao ve excecao nem recurso caido, e ve
	   defeito onde um `console.log("sem error")` nao e defeito nenhum. */
	const ingenua = (m) => JSON.stringify(m).includes('error');
	const discorda = [
		['excecao de JavaScript', { mensagens: [], excecoes: ['TypeError: x'] }],
		['log que contem a palavra', { mensagens: [{ tipo: 'log', texto: 'nenhum error aqui' }] }],
	];
	for (const [nome, mundo] of discorda) {
		const ok = vereditoDoConsole(mundo).limpo !== !ingenua(mundo);
		console.log((ok ? '  ok   ' : '  FALHA') + '  a ingenua discorda da nova em: ' + nome);
		if (!ok) falhas++;
	}
	console.log('');
	console.log(falhas ? '  REPROVADO — ' + falhas + ' afirmacao(oes) do autoteste' : '  APROVADO — ' + (casos.length + discorda.length) + ' afirmacoes, 0 falha, sem uma requisicao de rede');
	return falhas ? 1 : 0;
}

/* O SITEMAP SE LE PELO `request` DA ABA, NUNCA POR `page.content()`, E O PORTAO
   REPROVOU QUEM O ESCREVEU NESTE MESMO PONTO. Primeira versao deste arquivo
   lia o XML com `page.content()`: o Chromium embrulha XML no proprio visualizador,
   o `<loc>` sai dentro de `<span>`, o padrao nao casou com nenhum, a lista veio
   VAZIA — e o veredito imprimiu `APROVADO — 0 de 0 paginas com console limpo`.
   Aprovar sobre o NADA, com cara de medicao, as 19h3xZ de 09/11/2026. Dai as
   duas correcoes: o XML vem pelo `request` (texto cru, sem visualizador) e LISTA
   VAZIA REPROVA — nenhuma pagina medida nunca e o mesmo que nenhuma pagina
   suja. */
async function paginasDoSitemap(aba) {
	const quebra = (u) => u + (u.includes('?') ? '&' : '?') + 'v=' + Date.now();
	const ler = async (endereco) => {
		const r = await aba.request.get(quebra(endereco));
		if (r.status() !== 200) throw new Error('o sitemap ' + endereco + ' respondeu ' + r.status());
		const xml = await r.text();
		return [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
	};
	const urls = new Set();
	for (const sub of await ler(SITE + '/wp-sitemap.xml')) {
		if (sub.includes('wp-sitemap')) {
			for (const u of await ler(sub)) if (u.startsWith(SITE) && !u.includes('wp-sitemap')) urls.add(u);
		} else if (sub.startsWith(SITE)) urls.add(sub);
	}
	return [...urls].sort();
}

async function principal() {
	const argv = process.argv.slice(2);
	if (argv.includes('--autoteste')) process.exit(autoteste());

	const chrome = acharChrome();
	const navegador = await chromium.launch(chrome ? { executablePath: chrome } : {});
	let saida = 0;
	try {
		const ctx = await navegador.newContext({ viewport: { width: LARGURA, height: 844 }, deviceScaleFactor: 1 });
		const aba = await ctx.newPage();
		const i = argv.indexOf('--uma');
		const lista = i >= 0 ? [SITE + argv[i + 1]] : await paginasDoSitemap(aba);
		if (!lista.length) {
			console.log('  REPROVADO — o sitemap nao devolveu URL nenhuma. Zero pagina medida nao e zero pagina suja.');
			await navegador.close();
			process.exit(1);
		}
		console.log('  ' + lista.length + ' pagina(s), a ' + LARGURA + ' px, com quebra de cache');
		console.log('');
		let sujas = 0;
		for (const url of lista) {
			const colhido = { mensagens: [], excecoes: [], falhas: [], ruins: [] };
			const p = await ctx.newPage();
			p.on('console', (m) => colhido.mensagens.push({ tipo: m.type(), texto: m.text().slice(0, 160) }));
			p.on('pageerror', (e) => colhido.excecoes.push(String(e.message).slice(0, 160)));
			p.on('requestfailed', (r) => colhido.falhas.push(r.url().slice(0, 120) + ' (' + (r.failure() ? r.failure().errorText : '?') + ')'));
			p.on('response', (r) => { if (r.status() >= 400) colhido.ruins.push(r.status() + ': ' + r.url().slice(0, 120)); });
			try {
				const r = await p.goto(url + (url.includes('?') ? '&' : '?') + 'v=' + Date.now(), { waitUntil: 'networkidle', timeout: 60000 });
				const v = vereditoDoConsole(colhido);
				const tipos = Object.entries(v.porTipo).map(([t, n]) => t + '=' + n).join(' ') || 'nenhuma mensagem';
				const caminho = url.replace(SITE, '') || '/';
				console.log('  ' + (v.limpo ? 'ok   ' : 'FALHA') + ' ' + caminho.padEnd(34) + ' HTTP ' + (r ? r.status() : '?') + '   console: ' + tipos);
				for (const g of v.graves) console.log('          ' + g);
				if (!v.limpo) { sujas++; saida = 1; }
			} catch (e) {
				console.log('  FALHA ' + url + ' nao abriu: ' + e.message);
				sujas++; saida = 1;
			} finally { await p.close(); }
		}
		console.log('');
		console.log(saida
			? '  REPROVADO — ' + sujas + ' de ' + lista.length + ' pagina(s) com console sujo. A 32.5 pede console limpo.'
			: '  APROVADO — ' + lista.length + ' de ' + lista.length + ' paginas com console limpo (0 error, 0 excecao, 0 recurso caido).');
	} finally {
		await navegador.close();
	}
	process.exit(saida);
}

principal().catch((e) => { console.log('  REPROVADO — ' + e.message); process.exit(1); });

/**
 * A REGUA DA 32.5, NO AR, NUM NAVEGADOR DE VERDADE, EM TODAS AS PAGINAS DO MOLDE.
 *
 *   npm i --no-save playwright@1.56.1
 *   node ferramentas/conferir-32-5-no-navegador.mjs
 *   node ferramentas/conferir-32-5-no-navegador.mjs --uma /materiais/acabamento/peca-de-mosaico-esbranquicada/
 *
 * POR QUE ELE EXISTE, e a data faz parte do motivo. Item 1 do despacho da
 * Sentinela de 23/10/2026: `/materiais/acabamento/peca-de-mosaico-esbranquicada/`
 * servia o primeiro link de loja a 1.495 px contra o teto de 1.400 px da 32.5 —
 * e era a UNICA das 20 paginas do mutirao de 21/10 que nao passava. O
 * `ESTADO.md` daquele dia registrou "20 de 20 passam a 32.5 no ar"; a medicao
 * independente da ronda achou 19. O despacho escreveu a licao numa frase, e ela
 * e o contrato deste arquivo:
 *
 *     "regua que nao varre todas certifica a pagina que o autor abriu".
 *
 * POR QUE NAVEGADOR E NAO `curl`. A 32.5 e uma regua de PIXEL — onde a caixa de
 * resposta comeca, onde o primeiro botao de compra aparece — e pixel nao existe
 * no HTML: existe depois de o CSS ser aplicado, com a fonte da casca carregada,
 * na largura real do telefone. Nenhuma afirmacao sobre texto servido pode
 * responder "a 1.495 px". E a largura nao e redonda por acaso: 390 e o telefone
 * que a 32.5 nomeia.
 *
 * POR QUE ELE NAO TEM LISTA DE PAGINA. A lista das 20 do mutirao envelhece no
 * dia em que a 21a nascer, e o defeito que ele existe para pegar foi
 * exatamente o de uma pagina ficar FORA da conta. Entao ele DESCOBRE: le o
 * `wp-sitemap.xml` no ar, abre cada URL e julga a que SERVE o molde — a que
 * tem `.cdm-molde-compra` ou `.cdm-molde-resultado` na pagina. Pagina sem
 * molde e listada como fora do molde, nunca aprovada em silencio.
 *
 * O QUE ELE MEDE, por pagina do molde, a 390 px de largura real e com quebra de
 * cache, e os tres primeiros sao o "pronto quando" da 32.5:
 *
 *   1. onde a PRIMEIRA CAIXA comeca  — caixa de resposta (`.cdm-molde-resultado`)
 *      ou formulario da ferramenta. Teto: 700 px.
 *   2. onde o PRIMEIRO BOTAO DE COMPRA aparece. Teto: 1.400 px. Em pagina com
 *      link de afiliado e o primeiro `a[rel~=sponsored]`; nas pecas de `/loja/`,
 *      que nao tem link de loja por desenho (peca da artesa nao e afiliado), e
 *      o primeiro controle de compra de dentro do bloco `.cdm-molde-compra`.
 *   3. ROLAGEM HORIZONTAL, que tem de ser zero.
 *
 * E mais duas que custam o mesmo e dizem se a medicao vale: a ALTURA da pagina
 * e o numero de erros de JavaScript. Pagina que estourou no console pode ter
 * medido um layout que o visitante nao ve.
 *
 * O QUE ELE NAO PROMETE: a metade da 32.5 que fala do HTML servido com
 * JavaScript desligado (o texto inteiro continuar na pagina) e do `title`, `h1`,
 * trilha e JSON-LD identicos — isso e do `conferir-no-ar.py` e do
 * `leitura-do-visitante.py`, que leem o servido. Este arquivo mede pixel.
 */
import { chromium } from 'playwright';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const SITE = process.env.CDM_SITE || 'https://clubedomosaico.com.br';

/* O CHROMIUM DA NUVEM NAO MORA NUM CAMINHO FIXO, e um caminho fixo e como esta
   bancada para de rodar sem ninguem mexer nela: o `teste-navegador-casca.mjs`
   aponta para `chromium-1194`, que nao existe mais nesta maquina (ha `1243`).
   Entao o caminho se DESCOBRE: a pasta de navegadores do ambiente, qualquer
   revisao que tenha binario; e, se nada casar, deixa o playwright resolver
   sozinho — sem `executablePath`. */
function acharChrome() {
	if (process.env.CDM_CHROME) return process.env.CDM_CHROME;
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
const CHROME = acharChrome();
const TETO_CAIXA = 700;
const TETO_COMPRA = 1400;
const LARGURA = 390;

const argv = process.argv.slice(2);
const uma = argv.includes('--uma') ? argv[argv.indexOf('--uma') + 1] : null;

function cacheBreak(url) {
	const u = new URL(url);
	u.searchParams.set('v', String(Date.now()));
	return u.toString();
}

async function sitemapUrls(pagina) {
	const indice = await (await pagina.request.get(cacheBreak(`${SITE}/wp-sitemap.xml`))).text();
	const sub = [...indice.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
	const urls = new Set();
	for (const s of sub) {
		const xml = await (await pagina.request.get(cacheBreak(s))).text();
		for (const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) {
			if (m[1].startsWith(SITE) && !m[1].includes('wp-sitemap')) urls.add(m[1]);
		}
	}
	return [...urls].sort();
}

const navegador = await chromium.launch(CHROME ? { executablePath: CHROME } : {});
const contexto = await navegador.newContext({
	viewport: { width: LARGURA, height: 844 },
	deviceScaleFactor: 2,
	userAgent:
		'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
});
const pagina = await contexto.newPage();

const lista = uma ? [new URL(uma, SITE).toString()] : await sitemapUrls(pagina);

const molde = [];
const fora = [];
let falhas = 0;

for (const url of lista) {
	const erros = [];
	pagina.removeAllListeners('pageerror');
	pagina.on('pageerror', (e) => erros.push(String(e.message || e)));
	await pagina.goto(cacheBreak(url), { waitUntil: 'load', timeout: 60000 });
	await pagina.evaluate(() => document.fonts && document.fonts.ready);
	await pagina.waitForTimeout(250);

	const m = await pagina.evaluate(() => {
		const topo = (el) => (el ? Math.round(el.getBoundingClientRect().top + window.scrollY) : null);
		const visivel = (el) => !!(el && el.getClientRects().length);
		const primeiro = (sel) => [...document.querySelectorAll(sel)].find(visivel) || null;

		const bloco = document.querySelector('.cdm-molde-compra');
		const caixa = primeiro('.cdm-molde-resultado') || primeiro('form.cdm-f1-form, form.cdm-f2-form, main form');
		const patrocinado = primeiro('a[rel~="sponsored"]');
		const controle = bloco
			? [...bloco.querySelectorAll('a[rel~="sponsored"], a.cdm-botao, summary.cdm-botao, a.cdm-f2-botao, a.cdm-f1-botao, button.cdm-botao')].find(visivel) || null
			: null;
		const compra = patrocinado || controle;

		return {
			tem_molde: !!(bloco || document.querySelector('.cdm-molde-resultado')),
			caixa: topo(caixa),
			caixa_alt: caixa ? Math.round(caixa.getBoundingClientRect().height) : null,
			compra: topo(compra),
			compra_rotulo: compra ? (compra.textContent || '').trim().slice(0, 32) : null,
			compra_patrocinada: !!patrocinado,
			altura: Math.round(document.documentElement.scrollHeight),
			rolagem_h: Math.max(0, document.documentElement.scrollWidth - window.innerWidth),
		};
	});
	m.url = url.replace(SITE, '');
	m.erros = erros.length;

	if (!m.tem_molde) {
		fora.push(m);
		continue;
	}
	molde.push(m);

	const problemas = [];
	if (m.caixa === null || m.caixa >= TETO_CAIXA) problemas.push(`caixa a ${m.caixa} px (teto ${TETO_CAIXA})`);
	if (m.compra === null || m.compra >= TETO_COMPRA) problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA})`);
	if (m.rolagem_h > 0) problemas.push(`rolagem horizontal ${m.rolagem_h} px`);
	if (m.erros > 0) problemas.push(`${m.erros} erro(s) de JavaScript`);
	m.problemas = problemas;
	if (problemas.length) falhas++;

	const marca = problemas.length ? 'FALHA' : 'ok   ';
	console.log(
		`  ${marca} ${m.url.padEnd(56)} caixa ${String(m.caixa).padStart(5)} px  compra ${String(m.compra).padStart(5)} px  altura ${String(m.altura).padStart(5)} px` +
			(problemas.length ? `\n         ${problemas.join('; ')}` : '')
	);
}

await navegador.close();

console.log('');
console.log(`  paginas com molde: ${molde.length}   fora do molde: ${fora.length}   (sitemap: ${lista.length})`);
if (fora.length) console.log(`  fora do molde: ${fora.map((f) => f.url).join(' ')}`);
const piorCaixa = molde.reduce((a, b) => (a === null || (b.caixa ?? 1e9) > a ? b.caixa ?? 1e9 : a), null);
const piorCompra = molde.reduce((a, b) => (a === null || (b.compra ?? 1e9) > a ? b.compra ?? 1e9 : a), null);
console.log(`  pior caixa: ${piorCaixa} px (teto ${TETO_CAIXA})   pior compra: ${piorCompra} px (teto ${TETO_COMPRA})`);
console.log(falhas ? `  REPROVADO — ${falhas} pagina(s) do molde fora da 32.5` : `  APROVADO — ${molde.length} de ${molde.length} paginas do molde dentro da 32.5`);
process.exit(falhas ? 1 : 0);

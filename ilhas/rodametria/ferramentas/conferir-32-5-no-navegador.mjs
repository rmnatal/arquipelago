/**
 * A REGUA DA 32.5, NO AR, NUM NAVEGADOR DE VERDADE, EM TODAS AS PAGINAS DO MOLDE.
 *
 *   node ferramentas/conferir-32-5-no-navegador.mjs
 *   node ferramentas/conferir-32-5-no-navegador.mjs --uma /autonomia-patinete-eletrico/
 *
 * COPIADO DO MODELO DA CLUBEDOMOSAICO em 29/10/2026, como a 32.5-b manda com
 * todas as letras: "o modelo esta escrito e rodando: ilhas/clubedomosaico/
 * ferramentas/conferir-32-5-no-navegador.mjs — quem copiar troca o dominio e os
 * nomes de classe da ilha". Trocaram o dominio, o prefixo das classes (cdm- ->
 * rdm-) e o seletor do formulario de ferramenta desta ilha.
 *
 * POR QUE ELE EXISTE AQUI, no dia em que a primeira pagina desta ilha foi ao ar:
 * a 32.5 e o "pronto quando" do molde, e a 32.5-b diz por que ele nao pode ter
 * lista — "regua que nao varre todas certifica a pagina que o autor abriu". Numa
 * ilha de duas paginas a lista pareceria inofensiva, e e justamente agora que
 * ela e barata de nao escrever.
 *
 * POR QUE NAVEGADOR E NAO `curl`. A 32.5 e uma regua de PIXEL — onde o
 * formulario comeca, onde o primeiro botao de compra aparece — e pixel nao
 * existe no HTML: existe depois de o CSS ser aplicado, com a fonte da casca
 * carregada, na largura real do telefone. Nenhuma afirmacao sobre texto servido
 * responde "a 1.495 px". E 390 nao e largura redonda por acaso: e o telefone que
 * a 32.5 nomeia.
 *
 * ELE DESCOBRE AS PAGINAS: le o `wp-sitemap.xml` no ar, abre cada URL e julga a
 * que SERVE o molde — a que tem `.rdm-molde-compra` ou `.rdm-molde-caixa`.
 * Pagina sem molde e listada como FORA DO MOLDE, nunca aprovada em silencio.
 *
 * O QUE ELE MEDE, por pagina do molde, a 390 px e com quebra de cache:
 *
 *   1. onde a PRIMEIRA CAIXA comeca. Teto: 700 px. Em pagina de FERRAMENTA e o
 *      FORMULARIO (`form.rdm-f2`), porque a ordem da 32.1 o poe antes da caixa
 *      de resultado; na home desta ilha, que e HUB e nao tem formulario, e a
 *      caixa de resposta (`.rdm-molde-caixa`). A 32.5-b e explicita sobre nao
 *      trocar os dois: "trocar os dois reprova pagina certa", e portao que
 *      reprova pagina certa e o caminho mais curto para alguem passar a
 *      ignora-lo (a licao que a 20.5 nomeou quando o REPROVADO era cache). O
 *      formulario se nomeia pela CLASSE DA FERRAMENTA e nunca por `main form`.
 *   2. onde o PRIMEIRO BOTAO DE COMPRA aparece. Teto: 1.400 px. E o primeiro
 *      `a[rel~=sponsored]`, ou um controle de compra de dentro do bloco.
 *   3. ROLAGEM HORIZONTAL, que tem de ser zero.
 *
 * E mais duas que custam o mesmo e dizem se a medicao vale: a ALTURA da pagina e
 * o numero de erros de JavaScript. Pagina que estourou no console pode ter
 * medido um layout que o visitante nao ve.
 *
 * O QUE ELE NAO PROMETE: a metade da 32.5 que fala do HTML servido com
 * JavaScript desligado, do `title`, do `h1`, da trilha e do JSON-LD — isso e do
 * `conferir-no-ar.py`, que le o servido. Este arquivo mede pixel.
 */
/* ---------------------------------------------------------------------------
 * POR QUE `createRequire` E NAO `import { chromium } from 'playwright'`.
 *
 * E o defeito do despacho aberto de `dados/despachos.md` — "21 DOS 26 PORTOES DE
 * NAVEGADOR DO ARQUIPELAGO ESTAO INERTES NESTA NUVEM, PELA MESMA LINHA DE
 * `import`" —, medido aqui as 11h2xZ de 29/10/2026 no dia em que este portao
 * nasceu: `node ferramentas/conferir-32-5-no-navegador.mjs` morre em
 * `ERR_MODULE_NOT_FOUND: Cannot find package 'playwright'`, enquanto
 * `node -e "require('playwright')"` resolve em
 * `/opt/node-tools/node_modules/playwright/index.js`.
 *
 * A CAUSA, e ela cabe numa frase: nesta nuvem o playwright e alcancado por
 * `NODE_PATH`, e o resolvedor de ESM NAO LE `NODE_PATH` — so o de CommonJS le.
 * Entao `import` de pacote nao resolve de dentro de `ferramentas/`, e nenhum
 * `--loader` conserta isso. `createRequire` usa o resolvedor de CommonJS, que
 * le `NODE_PATH`, e continua funcionando numa maquina que tenha o pacote em
 * `node_modules` local.
 *
 * ISTO NAO E GAMBIARRA DESTE ARQUIVO: e o conserto que o despacho pede, e o
 * portao que nao roda nao e trava, e arquivo. Quem copiar este portao para
 * outra ilha copia estas tres linhas junto.
 * ------------------------------------------------------------------------- */
import { createRequire } from 'node:module';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const exigir = createRequire(import.meta.url);
const { chromium } = exigir('playwright');

const SITE = process.env.RDM_SITE || 'https://rodametria.com.br';

/* O CHROMIUM DA NUVEM NAO MORA NUM CAMINHO FIXO, e um caminho fixo e como esta
   bancada para de rodar sem ninguem mexer nela: o `teste-navegador-casca.mjs`
   aponta para `chromium-1194`, que nao existe mais nesta maquina (ha `1243`).
   Entao o caminho se DESCOBRE: a pasta de navegadores do ambiente, qualquer
   revisao que tenha binario; e, se nada casar, deixa o playwright resolver
   sozinho — sem `executablePath`. */
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

		const bloco = document.querySelector('.rdm-molde-compra');

		/* QUEM E A "PRIMEIRA CAIXA" DEPENDE DO TIPO DE PAGINA, e trocar os dois
		   e reprovar pagina certa (32.5-b). A 32.5 diz: "o formulario (ou a caixa
		   de resposta, em ficha) comeca antes de 700 px". Em pagina de FERRAMENTA a
		   ordem da 32.1 poe o FORMULARIO antes da caixa de resultado, entao medir a
		   caixa ali e medir o degrau de baixo. Nesta ilha a F2 tem formulario e a
		   home e HUB, sem formulario nenhum — as duas familias existem desde o
		   primeiro dia, e e por isso que a regua ja nasce com as duas. */
		const formulario = primeiro('form.rdm-f2');
		const caixa = formulario || primeiro('.rdm-molde-caixa');
		const patrocinado = primeiro('a[rel~="sponsored"]');
		const controle = bloco
			? [...bloco.querySelectorAll('a[rel~="sponsored"], a.rdm-molde-cartao-botao, a.rdm-molde-barra-botao')].find(visivel) || null
			: null;
		const compra = patrocinado || controle;

		return {
			tem_molde: !!(bloco || formulario),
			tem_caixa_sem_molde: !!(!bloco && !formulario && document.querySelector('.rdm-molde-caixa')),
			caixa: topo(caixa),
			caixa_que: formulario ? 'formulario' : 'resposta',
			caixa_alt: caixa ? Math.round(caixa.getBoundingClientRect().height) : null,
			resposta: topo(primeiro('.rdm-molde-caixa')),
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
		/* Pagina sem o contrato de conversao: sem bloco de compra E sem
		   formulario de ferramenta. Ela sai da conta do molde, mas NUNCA em
		   silencio — o motivo vai impresso, com a caixa medida mesmo assim,
		   para quem ler saber que ela foi aberta e julgada. */
		fora.push(m);
		console.log(
			`  fora  ${m.url.padEnd(56)} ${m.tem_caixa_sem_molde ? 'tem caixa de resposta e NAO tem bloco de compra nem formulario' : 'sem componente de molde'}` +
				(m.caixa !== null ? `  (caixa a ${m.caixa} px)` : '')
		);
		continue;
	}
	molde.push(m);

	const problemas = [];
	if (m.caixa === null || m.caixa >= TETO_CAIXA) problemas.push(`${m.caixa_que} a ${m.caixa} px (teto ${TETO_CAIXA})`);
	if (m.compra === null || m.compra >= TETO_COMPRA) problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA})`);
	if (m.rolagem_h > 0) problemas.push(`rolagem horizontal ${m.rolagem_h} px`);
	if (m.erros > 0) problemas.push(`${m.erros} erro(s) de JavaScript`);
	m.problemas = problemas;
	if (problemas.length) falhas++;

	const marca = problemas.length ? 'FALHA' : 'ok   ';
	console.log(
		`  ${marca} ${m.url.padEnd(56)} ${m.caixa_que.padEnd(11)} ${String(m.caixa).padStart(5)} px  compra ${String(m.compra).padStart(5)} px  altura ${String(m.altura).padStart(5)} px` +
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

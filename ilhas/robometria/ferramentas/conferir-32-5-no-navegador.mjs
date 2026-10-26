/**
 * A REGUA DA 32.5, NO AR, NUM NAVEGADOR DE VERDADE, EM TODAS AS PAGINAS DO MOLDE.
 *
 *   npm i --no-save playwright@1.56.1
 *   node ferramentas/conferir-32-5-no-navegador.mjs
 *   node ferramentas/conferir-32-5-no-navegador.mjs --uma /filtro-universal-de-robo-aspirador/
 *
 * PORTADO DA CLUBEDOMOSAICO EM 26/10/2026, pela execucao da Fundacao que fechou
 * o item 1 do despacho de 02/10 desta ilha. A 32.5-b manda, com todas as letras:
 * *"em toda ilha com molde, quem mexe em pagina de molde conferiu a 32.5 com um
 * portao que le o wp-sitemap.xml no ar"*, e nomeia o modelo
 * (`ilhas/clubedomosaico/ferramentas/conferir-32-5-no-navegador.mjs`) dizendo
 * que quem copiar troca o dominio e os nomes de classe da ilha. Esta ilha nao
 * tinha o portao: o bloco de 23/10 mediu "a 390 px" A MAO, pagina por pagina das
 * que o autor abriu — que e exatamente o que a frase do despacho de 23/10 proibe
 * ("regua que nao varre todas certifica a pagina que o autor abriu"). O bloco de
 * hoje mexeu em QUATRO snippets de pagina do molde (casca, r1, a1, malha), entao
 * a divida virou trabalho da propria passada.
 *
 * O QUE MUDOU NO PORTE, e sao tres nomes de classe:
 *   formulario de ferramenta  `form.cdm-f1-form, form.cdm-f2-form` -> `form.rbm-form`
 *   caixa de resposta         `.cdm-molde-resultado`               -> `.rbm-caixa`
 *   bloco de compra           `.cdm-molde-compra`                  -> `.rbm-compra`
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
 * tem `.rbm-compra` ou `.rbm-caixa` na pagina. Pagina sem
 * molde e listada como fora do molde, nunca aprovada em silencio.
 *
 * O QUE ELE MEDE, por pagina do molde, a 390 px de largura real e com quebra de
 * cache, e os tres primeiros sao o "pronto quando" da 32.5:
 *
 *   1. onde a PRIMEIRA CAIXA comeca. Teto: 700 px. Em pagina de FERRAMENTA e o
 *      FORMULARIO (`form.rbm-form`), porque a ordem da 32.1 o poe antes da caixa
 *      de resultado; em artigo e pagina de malha, que nao tem formulario, e a
 *      caixa de resposta (`.rbm-caixa`).
 *   2. onde o PRIMEIRO BOTAO DE COMPRA aparece. Teto: 1.400 px. E o primeiro
 *      `a[rel~=sponsored]`; onde a escada da 25.1 desceu ate a busca crua, que
 *      sai SEM `rel=sponsored` de proposito (busca crua nao rende comissao), e o
 *      primeiro controle de compra de dentro do bloco `.rbm-compra`.
 *   3. ROLAGEM HORIZONTAL, que tem de ser zero.
 *
 * E mais duas que custam o mesmo e dizem se a medicao vale: a ALTURA da pagina
 * e o numero de erros de JavaScript. Pagina que estourou no console pode ter
 * medido um layout que o visitante nao ve.
 *
 * O QUE ELE NAO PROMETE: a metade da 32.5 que fala do HTML servido com
 * JavaScript desligado (o texto inteiro continuar na pagina) e do `title`, `h1`,
 * trilha e JSON-LD identicos — isso e do `conferir-no-ar.py` desta ilha, que le
 * o servido. Este arquivo mede pixel.
 *
 * E ELE FICA FORA DA `bancada.py` POR DESENHO, nao por esquecimento: a bancada
 * classifica `*.mjs` como "navegador, fora desta bancada (denunciado, nao
 * rodado)", porque precisa de npm e de rede. Quem mexe em pagina do molde o
 * roda a mao e escreve os numeros no `REGISTRO.md` e no `dados/consertos.md`.
 */
/* O `import { chromium } from 'playwright'` DO ORIGINAL NAO RESOLVE NESTA NUVEM,
   e a diferenca entre os dois caminhos de resolucao e a causa: o playwright mora
   em /opt/node-tools/node_modules, que `require()` de CommonJS encontra de
   qualquer pasta e o `import` de ESM NAO — e `NODE_PATH` nao vale para ESM.
   Medido em 26/10/2026: `node -e "require.resolve('playwright')"` responde o
   caminho e o `import` do mesmo pacote morre em ERR_MODULE_NOT_FOUND na mesma
   maquina. Entao o require de CommonJS e trazido para dentro do modulo, que e o
   unico jeito de o arquivo rodar sem `npm i` local (e `npm i` aqui seria uma
   SEGUNDA copia do playwright, que a nota do ambiente proibe por achar outro
   navegador). A linha de uso do cabecalho fica, porque numa maquina com install
   local as duas resolucoes dao no mesmo pacote.
   ISTO E DIVIDA DA CLUBEDOMOSAICO TAMBEM — o original de la tem a mesma linha e
   vai morrer do mesmo jeito. Esta escrito no REGISTRO desta ilha, na entrada de
   26/10, para a proxima execucao que tocar aquela ilha. */
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const SITE = process.env.RBM_SITE || 'https://robometria.com.br';

/* O CHROMIUM DA NUVEM NAO MORA NUM CAMINHO FIXO, e um caminho fixo e como esta
   bancada para de rodar sem ninguem mexer nela: o `teste-navegador-casca.mjs`
   aponta para `chromium-1194`, que nao existe mais nesta maquina (ha `1243`).
   Entao o caminho se DESCOBRE: a pasta de navegadores do ambiente, qualquer
   revisao que tenha binario; e, se nada casar, deixa o playwright resolver
   sozinho — sem `executablePath`. */
function acharChrome() {
	if (process.env.RBM_CHROME) return process.env.RBM_CHROME;
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
const navegacao = [];
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

		const bloco = document.querySelector('.rbm-compra');

		/* QUEM E A "PRIMEIRA CAIXA" DEPENDE DO TIPO DE PAGINA, e trocar os dois
		   e reprovar pagina certa. A 32.5 diz: "o formulario (ou a caixa de
		   resposta, em ficha) comeca antes de 700 px". Em pagina de FERRAMENTA a
		   ordem da 32.1 poe o FORMULARIO antes da caixa de resultado, entao
		   medir a caixa ali e medir o degrau de baixo: medido em 23/10/2026,
		   `/materiais/qual-cola-usar-no-mosaico/` tem formulario a 439 px e
		   caixa a 777 px, e `/materiais/quantas-pastilhas-para-mosaico/` tem
		   462 px e 884 px — as duas PASSAM pela regua certa e as duas seriam
		   REPROVADAS pela caixa. Portao que reprova pagina certa nao e rigor: e
		   o caminho mais curto para alguem passar a ignora-lo (a licao da 20.5).
		   O formulario se nomeia por CLASSE DE FERRAMENTA (`rbm-form`) e nunca
		   por `main form`: a classe e a que a casca desta ilha estiliza, e e ela
		   que a R1 e a R2 usam. */
		const formulario = primeiro('form.rbm-form');
		const caixa = formulario || primeiro('.rbm-caixa');
		const patrocinado = primeiro('a[rel~="sponsored"]');
		/* A BUSCA CRUA DA ESCADA DA 25.1 NAO LEVA `rel=sponsored`, e isso e
		   decisao escrita da casca 1.6.0: ninguem paga por aquele clique, entao
		   carimba-lo de patrocinado afirmaria uma relacao que nao existe. Em
		   pagina cujo ultimo degrau e a busca crua, procurar so por
		   `rel~=sponsored` mediria `null` e REPROVARIA pagina certa. */
		const controle = bloco
			? [...bloco.querySelectorAll('a[rel~="sponsored"], a.rbm-comprar, a.rbm-comprar-busca, a.rbm-comprar-cru, a.rbm-fonte')].find(visivel) || null
			: null;
		const compra = patrocinado || controle;

		return {
			tem_molde: !!(bloco || document.querySelector('.rbm-caixa')),
			/* A TERCEIRA FAMILIA DE PAGINA DESTA ILHA, e ela nao existe na
			   clubedomosaico: a pagina de MALHA de navegacao. /pecas/ e
			   /pecas/filtros/ servem caixa de resposta e apontam para as
			   filhas; nao ha item para comprar nelas, e por isso nao ha bloco
			   `.rbm-compra`. Cobrar teto de compra ali REPROVA PAGINA CERTA, que
			   e o caminho mais curto para alguem passar a ignorar o portao (a
			   licao da 20.5, repetida na 32.5-b).
			   E A SAIDA NAO E UMA LISTA DE EXCECAO, que envelheceria no dia da
			   proxima filha: a pagina so e de navegacao se NAO tiver bloco de
			   compra E NAO tiver nenhum link de afiliado em lugar nenhum. Pagina
			   com `rel=sponsored` solto e sem bloco de compra e defeito de
			   verdade — e a ordem da 32.1 quebrada — e continua reprovando. */
			sponsored_total: document.querySelectorAll('a[rel~="sponsored"]').length,
			tem_bloco_de_compra: !!bloco,
			caixa: topo(caixa),
			caixa_que: formulario ? 'formulario' : 'resposta',
			caixa_alt: caixa ? Math.round(caixa.getBoundingClientRect().height) : null,
			resposta: topo(primeiro('.rbm-caixa')),
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
	if (m.caixa === null || m.caixa >= TETO_CAIXA) problemas.push(`${m.caixa_que} a ${m.caixa} px (teto ${TETO_CAIXA})`);
	m.navegacao = !m.tem_bloco_de_compra && m.sponsored_total === 0;
	if (m.navegacao) {
		navegacao.push(m);
	} else if (m.compra === null || m.compra >= TETO_COMPRA) {
		problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA})`);
		if (!m.tem_bloco_de_compra && m.sponsored_total > 0) {
			problemas.push(`${m.sponsored_total} link(s) de afiliado FORA de um bloco .rbm-compra`);
		}
	}
	if (m.rolagem_h > 0) problemas.push(`rolagem horizontal ${m.rolagem_h} px`);
	if (m.erros > 0) problemas.push(`${m.erros} erro(s) de JavaScript`);
	m.problemas = problemas;
	if (problemas.length) falhas++;

	const marca = problemas.length ? 'FALHA' : 'ok   ';
	console.log(
		`  ${marca} ${m.url.padEnd(56)} ${m.caixa_que.padEnd(11)} ${String(m.caixa).padStart(5)} px  compra ${m.navegacao ? ' nav.' : String(m.compra).padStart(5)} px  altura ${String(m.altura).padStart(5)} px` +
			(problemas.length ? `\n         ${problemas.join('; ')}` : '')
	);
}

await navegador.close();

console.log('');
console.log(`  paginas com molde: ${molde.length}   fora do molde: ${fora.length}   (sitemap: ${lista.length})`);
if (fora.length) console.log(`  fora do molde: ${fora.map((f) => f.url).join(' ')}`);
if (navegacao.length) {
	console.log(`  de NAVEGACAO (caixa de resposta, nada para comprar, zero link de afiliado): ${navegacao.map((f) => f.url).join(' ')}`);
}
const comCompra = molde.filter((m) => !m.navegacao);
const piorCaixa = molde.reduce((a, b) => (a === null || (b.caixa ?? 1e9) > a ? b.caixa ?? 1e9 : a), null);
const piorCompra = comCompra.reduce((a, b) => (a === null || (b.compra ?? 1e9) > a ? b.compra ?? 1e9 : a), null);
console.log(`  pior caixa: ${piorCaixa} px (teto ${TETO_CAIXA})   pior compra: ${piorCompra} px (teto ${TETO_COMPRA})`);
console.log(falhas ? `  REPROVADO — ${falhas} pagina(s) do molde fora da 32.5` : `  APROVADO — ${molde.length} de ${molde.length} paginas do molde dentro da 32.5 (${comCompra.length} com compra, ${navegacao.length} de navegacao)`);
process.exit(falhas ? 1 : 0);

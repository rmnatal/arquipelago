/*
 * MEDE UMA FOTO DE CARTAO COMO O NAVEGADOR DO VISITANTE A MEDE — `naturalWidth`
 * NO DOM, E NUNCA SO O CODIGO HTTP (19/11/2026).
 *
 *     node ferramentas/medir-foto-no-navegador.mjs <url> [<url> ...]
 *     echo '["https://...","https://..."]' | node ferramentas/medir-foto-no-navegador.mjs -
 *     node ferramentas/medir-foto-no-navegador.mjs --autoteste   # sem rede
 *
 * Saida: JSON em stdout, um objeto por URL, com `desfecho`, `largura`,
 * `altura`, `status_http`, `tipo` e `como_foi_medido`.
 *
 * POR QUE ESTE SEGUNDO INSTRUMENTO EXISTE, e ele nao e zelo. O `medir_foto` do
 * coletor le os primeiros bytes com `Range` e tira a dimensao do CABECALHO do
 * arquivo. Isso prova que a origem respondeu e que os bytes comecam como JPEG,
 * PNG ou WebP — e NAO prova que o navegador decodifica a imagem. Foi
 * exatamente a diferenca que a ronda de 18/11/2026 mediu no Chrome do Raphael:
 * `complete: true` com `naturalWidth: 0`, que e uma imagem que o navegador
 * aceitou e nao conseguiu pintar. Cartao com foto QUEBRADA e pior que cartao
 * sem foto, porque promete uma imagem e entrega o icone de imagem rota no
 * espaco mais caro da pagina.
 *
 * A REGRA QUE ESTE PORTAO SERVE: foto SO volta ao banco quando DOIS
 * instrumentos independentes a medem viva — o cabecalho do arquivo (coletor) e
 * o DOM (este) —, e o registro diz de QUAL AMBIENTE cada medicao saiu. Esta
 * nuvem nao e o navegador do visitante, e nenhuma medicao daqui afirma nada
 * sobre o de fora.
 *
 * OS QUATRO DESFECHOS SAO DITOS SEPARADOS, como o item 2 do despacho de 18/11
 * obrigou o portao de pixel desta ilha a fazer: a origem respondeu e a imagem
 * pintou (`viva`); a origem respondeu e a imagem NAO pintou (`quebrada`, e e
 * defeito); o pedido NAO CHEGOU a origem (`nao_medida`, e NAO e defeito — e
 * ausencia de medicao, que e outra coisa); e a rede falhou por motivo que nao
 * esta na lista fechada de "nao chegou" (`rede_nao_explica`, que reprova com a
 * causa em aberto). O 403 nao escolhe pai. E `ERR_BLOCKED_BY_ORB` cai em
 * `rede_nao_explica` e NUNCA em `nao_medida`: ele significa que a resposta
 * CHEGOU e o navegador a recusou por nao ser imagem — o status nao chega ao
 * instrumento, mas a origem respondeu, e chamar isso de "nao medi" seria o
 * instrumento sumindo com o que mediu.
 *
 * A PAGINA E LOCAL E NAO E A DA ILHA, de proposito: o que se mede aqui e a
 * FOTO, nao a pagina. Medir a foto dentro da pagina da ilha mistura o veredito
 * da CDN com o do site, e a coleta roda antes de qualquer pagina existir.
 */
import { createRequire } from 'node:module';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

/* As tres linhas do `conferir-32-5-no-navegador.mjs`, e elas viajam juntas:
   nesta nuvem o playwright e alcancado por `NODE_PATH`, que o resolvedor de
   ESM nao le. Ver o cabecalho daquele arquivo. */
const exigir = createRequire(import.meta.url);

/* O PEDIDO NEM CHEGOU A ORIGEM: so estes erros do Chromium afirmam isso, e a
   lista e fechada de proposito. Erro de rede que NAO esta aqui vira
   `rede_nao_explica`, que REPROVA com a causa em aberto — e nunca
   `nao_medida`, porque "nao medi" e uma afirmacao forte e barata de fazer. */
const NAO_CHEGOU_A_ORIGEM = [
	'ERR_TUNNEL_CONNECTION_FAILED', 'ERR_PROXY_CONNECTION_FAILED',
	'ERR_NAME_NOT_RESOLVED', 'ERR_CONNECTION_REFUSED', 'ERR_CONNECTION_RESET',
	'ERR_CONNECTION_TIMED_OUT', 'ERR_INTERNET_DISCONNECTED',
	'ERR_SOCKS_CONNECTION_FAILED', 'ERR_CERT_AUTHORITY_INVALID',
];

const ESPERA_MS = 6000;   /* a espera da ronda de 18/11 no Chrome do Raphael */
const LARGURA = 390;

export function classificar(pintou, rede) {
	if (pintou) return 'viva';
	if (rede.status_http) return 'quebrada';
	const falha = rede.falha || '';
	if (!falha) return 'quebrada';
	if (NAO_CHEGOU_A_ORIGEM.some((t) => falha.includes(t))) return 'nao_medida';
	return 'rede_nao_explica';
}

/* ------------------------------------------------------------- o autoteste
 * OS MUNDOS SAO FABRICADOS, porque os que importam nao existem no dado de
 * hoje: em 19/11/2026 as dez fotos remedidas sairam `viva` nos dois
 * instrumentos, e e justamente por isso que os outros tres desfechos precisam
 * de mundo proprio — ramo que o dado nao tem e a 32.5-d, e esta ilha a pagou
 * duas vezes. */
const MUNDOS = [
	['pintou, logo viva — e o status nem e consultado',
		[true, { status_http: 200, tipo: 'image/jpeg' }], 'viva'],
	['pintou mesmo sem status nenhum: o DOM e quem decide `viva`',
		[true, {}], 'viva'],
	['a origem respondeu 503 e a imagem nao pintou: QUEBRADA, e e defeito',
		[false, { status_http: 503 }], 'quebrada'],
	['a origem respondeu 200 e a imagem nao pintou (naturalWidth 0): QUEBRADA',
		[false, { status_http: 200, tipo: 'image/jpeg' }], 'quebrada'],
	['o egresso recusou o CONNECT: NAO MEDIDA, e isto NAO reprova',
		[false, { falha: 'net::ERR_TUNNEL_CONNECTION_FAILED' }], 'nao_medida'],
	['o dominio nao resolve: NAO MEDIDA',
		[false, { falha: 'net::ERR_NAME_NOT_RESOLVED' }], 'nao_medida'],
	['ORB recusou a resposta que CHEGOU: rede_nao_explica, nunca nao_medida',
		[false, { falha: 'net::ERR_BLOCKED_BY_ORB' }], 'rede_nao_explica'],
	['erro de rede fora da lista fechada: rede_nao_explica, causa em aberto',
		[false, { falha: 'net::ERR_HTTP2_PROTOCOL_ERROR' }], 'rede_nao_explica'],
	['sem pintar, sem status e sem falha: QUEBRADA, porque calar nao e medir',
		[false, {}], 'quebrada'],
	/* A MUTACAO COBRADA: a regua INGENUA — "nao pintou e nao tenho status, logo
	   nao medi" — e a que estava escrita na primeira versao deste arquivo, e ela
	   APROVA o ORB como ausencia de medicao. Este mundo e o que a separa da
	   regua de hoje; se alguem reescrever `classificar` daquele jeito, esta
	   linha fica vermelha. */
	['a regua ingenua (sem status => nao_medida) tem de DISCORDAR aqui',
		[false, { falha: 'net::ERR_BLOCKED_BY_ORB' }], 'rede_nao_explica'],
];

function autoteste() {
	let afirmacoes = 0;
	const falhas = [];
	for (const [nome, [pintou, rede], esperado] of MUNDOS) {
		afirmacoes += 1;
		const deu = classificar(pintou, rede);
		if (deu !== esperado) falhas.push(`${nome}: esperava ${esperado}, deu ${deu}`);
	}
	/* A REGUA INGENUA REPRODUZIDA, para provar que este autoteste MORDE: se ela
	   passasse nos dez mundos, os dez nao estariam medindo nada. */
	afirmacoes += 1;
	const ingenua = (pintou, rede) => (pintou ? 'viva' : (rede.status_http ? 'quebrada' : 'nao_medida'));
	const discordancias = MUNDOS.filter(([, [p, r], esp]) => ingenua(p, r) !== esp).length;
	if (discordancias === 0) {
		falhas.push('a regua ingenua passou nos dez mundos: o autoteste nao esta medindo nada');
	}
	for (const f of falhas) process.stdout.write(`FALHA: ${f}\n`);
	process.stdout.write(`\n${afirmacoes} afirmacao(oes), ${falhas.length} falha(s).\n`);
	process.stdout.write(`${falhas.length ? 'REPROVADO' : 'APROVADO'}\n`);
	process.stdout.write(`a regua ingenua discorda em ${discordancias} de ${MUNDOS.length} mundos\n`);
	return falhas.length ? 1 : 0;
}

/* ------------------------------------------------------------- a medicao */
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

/* `-` sozinho significa "a lista vem pela entrada padrao", que e como a
   ferramenta que grava a entrega: um JSON de URLs, sem passar nenhuma delas
   pela linha de comando. `null` aqui e o sinal de stdin, nunca "nao ha URL". */
function daLinhaDeComando() {
	const argv = process.argv.slice(2);
	if (argv.length === 1 && argv[0] === '-') return null;
	return argv;
}

async function daEntradaPadrao() {
	const pedacos = [];
	for await (const p of process.stdin) pedacos.push(p);
	return JSON.parse(Buffer.concat(pedacos).toString('utf8'));
}

async function medir(urls) {
	const { chromium } = exigir('playwright');
	const CHROME = acharChrome();
	const navegador = await chromium.launch(CHROME ? { executablePath: CHROME } : {});
	const pagina = await navegador.newPage({ viewport: { width: LARGURA, height: 844 } });

	/* O QUE A REDE DISSE, POR URL. `response` e `requestfailed` sao as duas
	   unicas fontes honestas sobre a origem ter respondido: o `onerror` do
	   `<img>` nao distingue "a origem recusou" de "o pedido nem saiu". */
	const daRede = new Map();
	const entrada = (url) => {
		if (!daRede.has(url)) daRede.set(url, { status_http: null, tipo: null, falha: null });
		return daRede.get(url);
	};
	pagina.on('response', (r) => {
		const e = entrada(r.url());
		e.status_http = r.status();
		e.tipo = r.headers()['content-type'] || null;
	});
	/* A FALHA NAO APAGA O STATUS, e esta linha e um defeito consertado no dia em
	   que este arquivo nasceu: um `set` aqui sobrescrevia o `response` que ja
	   havia chegado, e o pedido que a origem RESPONDEU 404 saia classificado
	   como `nao_medida`. E a familia do erro sobrescrito de `urls_do_sitemap`,
	   achado nesta ilha na manha de 19/11/2026: instrumento que some com o que
	   mediu produz diagnostico errado com dono errado. */
	pagina.on('requestfailed', (r) => {
		entrada(r.url()).falha = r.failure()?.errorText || 'falha sem texto';
	});

	const corpo = urls
		.map((u, i) => `<img id="f${i}" src="${u.replace(/"/g, '&quot;')}" loading="eager" decoding="sync" alt="">`)
		.join('\n');
	await pagina.setContent(`<!doctype html><meta charset="utf-8"><title>bancada</title>${corpo}`,
		{ waitUntil: 'load' });
	await pagina.waitForTimeout(ESPERA_MS);

	const doDom = await pagina.evaluate((n) => {
		const saida = [];
		for (let i = 0; i < n; i += 1) {
			const el = document.getElementById(`f${i}`);
			saida.push({
				src: el.src, complete: el.complete,
				naturalWidth: el.naturalWidth, naturalHeight: el.naturalHeight,
			});
		}
		return saida;
	}, urls.length);

	await navegador.close();

	return doDom.map((d) => {
		const rede = daRede.get(d.src) || {};
		const pintou = d.naturalWidth > 0 && d.naturalHeight > 0;
		return {
			url: d.src,
			desfecho: classificar(pintou, rede),
			largura: pintou ? d.naturalWidth : null,
			altura: pintou ? d.naturalHeight : null,
			status_http: rede.status_http ?? null,
			tipo: rede.tipo ?? null,
			falha_de_rede: rede.falha ?? null,
			complete: d.complete,
			como_foi_medido: `naturalWidth no DOM do Chromium desta nuvem, ${LARGURA} px, loading eager, ${ESPERA_MS / 1000} s de espera`,
		};
	});
}

if (process.argv.includes('--autoteste')) {
	process.exit(autoteste());
}

const urls = daLinhaDeComando() || (await daEntradaPadrao());
if (!urls.length) {
	process.stderr.write('medir-foto-no-navegador: nenhuma URL na entrada\n');
	process.exit(2);
}
process.stdout.write(`${JSON.stringify(await medir(urls), null, 1)}\n`);

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

/* ======================================================================
   O AUTOTESTE — fabrica as paginas que o ar nao tem (20/11/2026)

   ELE NAO PRECISA DE REDE e por isso roda SEMPRE na bancada, antes de qualquer
   medicao no ar: `oferece_autoteste()` do `bancada.py` o descobre lendo este
   arquivo. Portao que depende de alguem lembrar nao roda.

   E O QUE ELE EXISTE PARA PROVAR E UMA COISA SO: que a regua NOVA e a regua de
   COMPONENTE **discordam** na pagina que serve link de compra sem ter componente
   de molde nenhum (20.8). Autoteste em que as duas concordam prova o que o portao
   velho ja provava.

   A medicao e fabricada como objeto, nao renderizada num navegador, porque o que
   esta sendo medido aqui e o JULGAMENTO e nao o pixel. O pixel se mede no ar, com
   Chromium, na largura do telefone — e e a outra metade deste arquivo.
   ====================================================================== */
function mundo(extra) {
	return {
		url: '/fabricada/',
		caixa: 400, caixa_que: 'resposta', caixa_alt: 120,
		resposta: 400, compra: 900, compra_rotulo: 'Ver na Shopee',
		compra_em_bloco: true, blocos_de_compra: 1,
		compra_patrocinada: true,
		componente_de_molde: true, vende_algo: true,
		tem_compra: true, tem_patrocinado: true, tem_bloco_de_compra: true,
		sponsored_total: 1, altura: 3000, rolagem_h: 0, erros: 0,
		...extra,
	};
}

if (argv.includes('--autoteste')) {
	let ruins = 0;
	const diz = (cond, rotulo, medido = '') => {
		console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${rotulo.padEnd(84)} ${medido}`);
		if (!cond) ruins++;
	};
	console.log('AUTOTESTE DA REGUA DA 32.5 — o julgamento, fabricado (o pixel se mede no ar)');
	console.log('='.repeat(100));

	// ---- 1. O MUNDO SADIO COMUM: cartao de molde, tudo dentro dos tetos ----
	diz(reguaDePixel(mundo()).length === 0, '1. cartao de molde com caixa a 400 e compra a 900: PASSA nas duas reguas',
		JSON.stringify(reguaDePixel(mundo())));
	diz(reguaDeComponente(mundo()).length === 0, '1-b. e a regua de COMPONENTE concorda neste mundo');

	// ---- 2. O MUNDO QUE O CONSERTO EXISTE PARA VER ----
	// Pagina que VENDE e nao tem componente nenhum: sem o conserto ela sai da
	// conta JA VENDENDO, e o teto de 1.400 px nunca e cobrado dela.
	const soLink = mundo({
		componente_de_molde: false, tem_compra: false, caixa: null, caixa_que: 'resposta',
		resposta: null, compra: 1800, compra_em_bloco: false, blocos_de_compra: 0,
	});
	const novaSoLink = reguaDePixel(soLink);
	const velhaSoLink = reguaDeComponente(soLink);
	diz(novaSoLink.some((x) => x.includes('compra a 1800')),
		'2. pagina que SERVE compra a 1800 px e nao tem componente: a regua NOVA REPROVA',
		JSON.stringify(novaSoLink));
	diz(velhaSoLink[0] === 'fora da conta — sem componente de molde nenhum',
		'2-b. e a regua de COMPONENTE a tira da conta — AS DUAS DISCORDAM (20.8)',
		JSON.stringify(velhaSoLink));
	diz(!novaSoLink.some((x) => x.includes('teto 700')),
		'2-c. e a NOVA nao cobra caixa dela: sem componente, nao ha degrau prometido a faltar');
	diz(novaSoLink.some((x) => x.includes('FORA de qualquer bloco')),
		'2-d. e a linha diz ONDE o link mora, porque o lugar deixou de ser obvio');

	// ---- 2-e. O ESCAPE QUE ESTA ILHA TINHA, E ELE NAO E O DA IRMA ----
	// Medido no ar em 20/11/2026: nas 14 URLs desta ilha, NENHUMA pagina estava
	// fora da conta vendendo — as 4 de fora servem zero link de compra, e as 3
	// de `/pecas/filtros/*` que servem link sem bloco `.rbm-compra` ja eram
	// medidas, porque os botoes delas carregam `rel=sponsored`. A consequencia do
	// defeito nesta ilha era ZERO paginas hoje, contra 59 de 97 na
	// clubedomosaico. O QUE A SALVAVA ERA UM ACIDENTE: o `rel=sponsored`.
	// ESTE MUNDO E O QUE NAO ERA ACIDENTE. Pagina que vende SO por busca crua
	// (`a.rbm-comprar-cru`, que sai sem `rel=sponsored` por decisao da casca
	// 1.6.0) e sem bloco de molde: a classificacao velha a chamava DE NAVEGACAO e
	// ela escapava do teto inteira, vendendo.
	const soBuscaCrua = mundo({
		componente_de_molde: false, tem_compra: false, tem_patrocinado: false,
		sponsored_total: 0, caixa: null, resposta: null,
		compra: 1750, compra_em_bloco: false, blocos_de_compra: 0,
	});
	diz(classificacaoVelhaDeNavegacao(soBuscaCrua) === true,
		'2-e. pagina que vende SO por busca crua: a classificacao VELHA a chamava de NAVEGACAO',
		`navegacao_velha=${classificacaoVelhaDeNavegacao(soBuscaCrua)}`);
	diz(soBuscaCrua.vende_algo === true,
		'2-f. e ela VENDE: o criterio novo a poe na conta pelo que ela serve');
	diz(reguaDePixel(soBuscaCrua).some((x) => x.includes('compra a 1750')),
		'2-g. e a regua NOVA a REPROVA a 1750 px — o escape de 1.400 px fechado',
		JSON.stringify(reguaDePixel(soBuscaCrua)));
	diz(classificacaoVelhaDeNavegacao(mundo({ tem_compra: false, sponsored_total: 0, vende_algo: false, compra: null, compra_em_bloco: false, blocos_de_compra: 0 })) === true
		&& reguaDePixel(mundo({ vende_algo: false, tem_compra: false, sponsored_total: 0, compra: null, compra_em_bloco: false, blocos_de_compra: 0 })).length === 0,
		'2-h. e a pagina de navegacao DE VERDADE continua passando nas duas — o conserto nao reprova pagina certa');

	// ---- 3. OS DOIS MUNDOS QUE ACOMPANHAM A SAIDA DA PONTA VELHA ----
	// A ponta velha REPROVAVA link patrocinado sem bloco de compra, com a frase
	// "o teto de compra nao tem o que medir". Ela existia contra ESCAPE do teto.
	// Tira-la sozinha seria afrouxar o portao; estes dois mundos poem o MESMO
	// link ABAIXO do teto e exigem que a regua nova continue REPROVANDO quando
	// ele passa dele. Sem eles, o conserto seria um furo.
	const abaixoDoTeto = mundo({
		componente_de_molde: false, tem_compra: false, caixa: null,
		compra: 1399, compra_em_bloco: false, blocos_de_compra: 0,
	});
	diz(reguaDePixel(abaixoDoTeto).length === 0,
		'3. o MESMO link, a 1399 px (um pixel abaixo do teto): a NOVA aprova',
		JSON.stringify(reguaDePixel(abaixoDoTeto)));
	const noTeto = mundo({
		componente_de_molde: false, tem_compra: false, caixa: null,
		compra: 1400, compra_em_bloco: false, blocos_de_compra: 0,
	});
	diz(reguaDePixel(noTeto).some((x) => x.includes('compra a 1400')),
		'3-b. e EXATAMENTE no teto (1400 px) ela REPROVA — estar no numero nao e estar abaixo dele',
		JSON.stringify(reguaDePixel(noTeto)));
	const semPixel = mundo({
		componente_de_molde: false, tem_compra: false, caixa: null, compra: null,
		vende_algo: true, compra_em_bloco: false, blocos_de_compra: 0,
	});
	diz(reguaDePixel(semPixel).some((x) => x.includes('compra a null')),
		'3-c. link que a pagina serve e o portao nao consegue medir REPROVA — nao medido nao e aprovado',
		JSON.stringify(reguaDePixel(semPixel)));

	// ---- 4. O DEGRAU PROMETIDO E AUSENTE, que a linha velha pegava ----
	// Este ramo NAO se pode perder no conserto: componente de molde na pagina e
	// nenhuma caixa nem formulario para medir e defeito de verdade.
	const prometeENaoTem = mundo({ caixa: null, resposta: null });
	diz(reguaDePixel(prometeENaoTem).some((x) => x.includes('NENHUMA caixa nem formulario')),
		'4. componente de molde SEM caixa nem formulario: REPROVA, e o ramo da linha velha sobrevive',
		JSON.stringify(reguaDePixel(prometeENaoTem)));
	diz(reguaDePixel(mundo({ caixa: 700 })).some((x) => x.includes('teto 700')),
		'4-b. caixa EXATAMENTE no teto de 700 px REPROVA');
	diz(reguaDePixel(mundo({ caixa: 699 })).length === 0,
		'4-c. e a 699 px passa');

	// ---- 5. A PAGINA DE NAVEGACAO: esta na conta e nao vende nada ----
	const navegacaoPura = mundo({
		vende_algo: false, tem_compra: false, tem_patrocinado: false,
		compra: null, sponsored_total: 0, compra_em_bloco: false, blocos_de_compra: 0,
	});
	diz(reguaDePixel(navegacaoPura).length === 0,
		'5. pagina de navegacao (caixa a 400, nada para comprar): PASSA — cobrar teto de compra ali reprova pagina certa',
		JSON.stringify(reguaDePixel(navegacaoPura)));
	diz(reguaDePixel(mundo({ vende_algo: false, compra: 9999 })).length === 0,
		'5-b. e pixel de compra numa pagina que NAO vende nao e cobrado: o criterio e o que ela serve');

	// ---- 5-c. ONDE MORA O LINK: o mundo de VARIOS CARTOES ----
	// ESTE BLOCO EXISTE POR UM DEFEITO MEDIDO NO AR HOJE, e por isso a frase
	// deixou de ser decidida dentro do navegador. A pergunta era contra o
	// PRIMEIRO `.rbm-compra`, e tres paginas desta ilha servem SEIS cada.
	const seisCartoes = mundo({ compra_em_bloco: true, blocos_de_compra: 6 });
	diz(ondeMoraOLink(seisCartoes) === 'dentro de um bloco .rbm-compra (6 na pagina)',
		'5-c. link no SEXTO cartao de uma pagina com 6 blocos: a frase diz DENTRO — o defeito de 20/11/2026',
		ondeMoraOLink(seisCartoes));
	diz(!ondeMoraOLink(seisCartoes).startsWith('FORA'),
		'5-d. e ela NAO comeca por FORA, que e o que a linha impressa usa para decidir se avisa');
	const foraComBlocos = mundo({ compra_em_bloco: false, blocos_de_compra: 6 });
	diz(ondeMoraOLink(foraComBlocos) === 'FORA dos 6 bloco(s) .rbm-compra da pagina',
		'5-e. link solto numa pagina QUE TEM 6 blocos: a frase diz FORA e diz quantos ha',
		ondeMoraOLink(foraComBlocos));
	const foraSemBlocos = mundo({ compra_em_bloco: false, blocos_de_compra: 0 });
	diz(ondeMoraOLink(foraSemBlocos).includes('nao tem nenhum'),
		'5-f. link solto em pagina SEM bloco nenhum: outra frase, porque o conserto e outro (20.5)',
		ondeMoraOLink(foraSemBlocos));
	diz(ondeMoraOLink(mundo({ vende_algo: false, compra_em_bloco: false, blocos_de_compra: 0 }))
		=== 'nenhum link de compra na pagina',
		'5-g. pagina que nao vende: a frase diz isso, nao "FORA de bloco"');
	diz(reguaDePixel(mundo({ compra: 1500, compra_em_bloco: true, blocos_de_compra: 6 }))
		.some((x) => x.includes('dentro de um bloco')),
		'5-h. e a REPROVACAO carrega a frase: quem le sabe onde procurar o botao');

	// ---- 6. AS DUAS TRAVAS QUE NAO SAO DE MOLDE ----
	diz(reguaDePixel(mundo({ rolagem_h: 3 })).some((x) => x.includes('rolagem horizontal 3')),
		'6. rolagem horizontal de 3 px REPROVA');
	diz(reguaDePixel(mundo({ erros: 2 })).some((x) => x.includes('2 erro(s)')),
		'6-b. erro de JavaScript REPROVA');

	console.log('='.repeat(100));
	console.log(ruins ? `  REPROVADO — ${ruins} afirmacao(oes) do autoteste da 32.5` : '  APROVADO — autoteste da regua da 32.5 inteiro, 0 falha');
	process.exit(ruins ? 1 : 0);
}

const navegador = await chromium.launch(CHROME ? { executablePath: CHROME } : {});
const contexto = await navegador.newContext({
	viewport: { width: LARGURA, height: 844 },
	deviceScaleFactor: 2,
	userAgent:
		'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
});
const pagina = await contexto.newPage();

/* ======================================================================
   AS DUAS REGUAS, E AS DUAS EXISTEM PARA DISCORDAR (20.8)

   O julgamento saiu de dentro do laco em 20/11/2026 e virou FUNCAO PURA, e isso
   nao e asseio: sem funcao pura o `--autoteste` nao consegue fabricar a pagina
   que serve compra sem componente, e regua que so roda no ar e regua que estreia
   no dia em que a pagina errada for publicada.
   ====================================================================== */

/* ONDE MORA O LINK DE COMPRA — funcao PURA, e ela e pura por cicatriz.

   A primeira versao desta decisao morava dentro do `page.evaluate`, e perguntava
   `bloco.contains(compra)` com `bloco` sendo o PRIMEIRO `.rbm-compra` do
   documento. Pagina desta ilha com varios cartoes tem UM BLOCO POR CARTAO:
   medido no ar em 20/11/2026, `/pecas/filtros/electrolux/`, `/pecas/filtros/wap/`
   e `/pecas/filtros/xiaomi/` servem SEIS `.rbm-compra` cada, e o portao imprimiu
   nas tres "compra FORA de qualquer bloco .rbm-compra" — rotulo FALSO sobre
   pagina certa. O autoteste nao podia te-lo pego: ele fabrica a medicao, e aquela
   frase era decidida no navegador, onde nenhuma afirmacao alcanca.

   A LICAO, e ela vale para quem copiar este portao: o que o `evaluate` devolve e
   FATO (`compra_em_bloco`, `blocos_de_compra`); quem transforma fato em frase e
   funcao pura, do lado de fora, onde o autoteste a chama. */
function ondeMoraOLink(m) {
	if (!m.vende_algo) return 'nenhum link de compra na pagina';
	if (m.compra_em_bloco) return `dentro de um bloco .rbm-compra (${m.blocos_de_compra} na pagina)`;
	if (m.blocos_de_compra > 0) {
		return `FORA dos ${m.blocos_de_compra} bloco(s) .rbm-compra da pagina`;
	}
	return 'FORA de qualquer bloco .rbm-compra, e a pagina nao tem nenhum';
}

/* A REGUA NOVA, de PIXEL. A pagina entra na conta pelo que SERVE. */
function reguaDePixel(m) {
	const problemas = [];
	/* O TETO DE CAIXA SE JULGA ONDE HA CAIXA, e ate 19/11/2026 isso era o mesmo
	   que "estar na conta" — por isso a linha era `caixa === null || caixa >=
	   TETO`. Deixou de ser: a pagina entra na conta por `vende_algo`, e existe
	   pagina na conta com link de compra e SEM formulario e SEM caixa de
	   resposta. Cobrar `caixa === null` dela seria reprovar o degrau que ela nao
	   tem. OS TRES RAMOS SE DIZEM SEPARADOS porque o conserto de cada um e
	   diferente (20.5): ha caixa, mede; nao ha caixa mas ha COMPONENTE de molde,
	   REPROVA — o componente promete o degrau e ele falta, que e o defeito que a
	   linha velha pegava e que nao se pode perder no conserto; nao ha nem
	   componente, o teto nao tem o que medir e a linha impressa DIZ isso, em vez
	   de aprovar nem reprovar calado. */
	if (m.caixa !== null) {
		if (m.caixa >= TETO_CAIXA) problemas.push(`${m.caixa_que} a ${m.caixa} px (teto ${TETO_CAIXA})`);
	} else if (m.componente_de_molde) {
		problemas.push(`componente de molde na pagina e NENHUMA caixa nem formulario para medir (teto ${TETO_CAIXA})`);
	}
	/* O TETO DE COMPRA E DO PRIMEIRO LINK DE COMPRA QUE A PAGINA SERVE, tenha ela
	   componente de molde ou nao.
	   E A PONTA VELHA QUE SAI, dita para ninguem a repor sem ler: ela REPROVAVA
	   pagina com `rel=sponsored` solto e sem bloco de compra, com a frase "o teto
	   de compra nao tem o que medir". Ela existia contra ESCAPE do teto — para
	   ninguem fugir da regua por nao ter o componente. MEDIR E MAIS FORTE QUE
	   REPROVAR: agora nada escapa, porque o teto julga o link e nao o cartao, e o
	   que esta certo passa. A saida dela esta acompanhada dos dois mundos de
	   autoteste que poem o MESMO link ABAIXO do teto e exigem REPROVADO — sem
	   eles, tirar a ponta velha seria afrouxar o portao. */
	if (m.vende_algo) {
		if (m.compra === null || m.compra >= TETO_COMPRA) {
			problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA}) — ${ondeMoraOLink(m)}`);
		}
	}
	if (m.rolagem_h > 0) problemas.push(`rolagem horizontal ${m.rolagem_h} px`);
	if (m.erros > 0) problemas.push(`${m.erros} erro(s) de JavaScript`);
	return problemas;
}

/* A CLASSIFICACAO VELHA DE "NAVEGACAO", DE ATE 19/11/2026 — e ela e o escape que
   esta ilha tinha, medido e nao suposto.

   A linha era, literal: `m.navegacao = !m.tem_bloco_de_compra && m.sponsored_total
   === 0`. Pagina sem bloco `.rbm-compra` E sem nenhum `rel=sponsored` era
   declarada DE NAVEGACAO, e pagina de navegacao nao era cobrada pelo teto de
   compra — por desenho, para nao reprovar `/pecas/` e `/pecas/filtros/`, que
   apontam para as filhas e nao tem o que vender.

   E ELA TEM UM BURACO QUE NAO E TEORICO NESTA ILHA: a escada da 25.1 desce ate a
   BUSCA CRUA, e a busca crua sai SEM `rel=sponsored` de proposito — decisao
   escrita da casca 1.6.0, porque ninguem paga por aquele clique. Entao pagina
   cujos botoes sao todos `a.rbm-comprar-cru`, sem bloco, tinha `sponsored_total
   === 0` e `tem_bloco_de_compra === false`: era classificada DE NAVEGACAO e
   ESCAPAVA do teto de 1.400 px inteira, VENDENDO. E o banco desta ilha tem 40
   pecas e 31 modelos no degrau 4 (busca), contados na leitura semanal de 18/11 —
   o mundo que produz essa pagina nao e remoto, e a proxima ficha que nascer no
   degrau 4 sem cartao de molde o produz. */
function classificacaoVelhaDeNavegacao(m) {
	return !m.tem_compra && m.sponsored_total === 0;
}

/* A REGUA DE COMPONENTE, a de ate 19/11/2026. Ela existe para o autoteste poder
   EXIGIR que as duas discordem na pagina que serve compra sem componente nenhum.
   Autoteste em que a regua velha e a nova concordam prova o que o portao velho ja
   provava, e nao mede conserto nenhum. */
function reguaDeComponente(m) {
	if (!m.componente_de_molde) return ['fora da conta — sem componente de molde nenhum'];
	const problemas = [];
	if (m.caixa === null || m.caixa >= TETO_CAIXA) problemas.push(`${m.caixa_que} a ${m.caixa} px (teto ${TETO_CAIXA})`);
	if (m.tem_compra) {
		if (m.compra === null || m.compra >= TETO_COMPRA) problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA})`);
	} else if (m.tem_patrocinado) {
		problemas.push('serve link patrocinado e NAO tem bloco de compra — o teto de compra nao tem o que medir');
	}
	return problemas;
}

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
		/* O CONTROLE DE COMPRA DEIXA DE SER PROCURADO SO DENTRO DO BLOCO
		   (20/11/2026, despacho NORMAL de 19/11). Ate hoje esta linha era
		   `bloco ? [...bloco.querySelectorAll(...)] : null`, e era por ela que
		   pagina com botao de compra e SEM componente de molde saia da conta JA
		   VENDENDO. O escopo passa a ser o documento, e a ORDEM do `find` e a
		   ordem do DOM: o primeiro controle de compra que a pagina serve. */
		const controle =
			[...document.querySelectorAll(
				'a[rel~="sponsored"], a.rbm-comprar, a.rbm-comprar-busca, a.rbm-comprar-cru'
			)].find(visivel) || null;
		const compra = patrocinado || controle;
		/* ONDE o link de compra mora, porque com o componente fora do critERIO o
		   lugar deixa de ser obvio e a linha impressa tem de dizer.
		   E A PERGUNTA E CONTRA TODOS OS BLOCOS, NAO CONTRA O PRIMEIRO. A
		   primeira versao desta linha, escrita hoje mesmo, perguntava
		   `bloco.contains(compra)` — e `bloco` e o PRIMEIRO `.rbm-compra` do
		   documento. Pagina desta ilha com varios cartoes tem um bloco por
		   cartao: medido no ar em 20/11/2026, `/pecas/filtros/electrolux/`,
		   `/pecas/filtros/wap/` e `/pecas/filtros/xiaomi/` servem SEIS
		   `.rbm-compra` cada e o portao imprimiu, nas tres, "compra FORA de
		   qualquer bloco .rbm-compra" — rotulo FALSO sobre pagina certa, do
		   mesmo lado do numero de tela digitado. O conserto foi achado pelo
		   proprio relatorio dele, lendo a linha contra o HTML servido. */
		const blocos = [...document.querySelectorAll('.rbm-compra')];
		/* O NAVEGADOR DEVOLVE FATO, NUNCA FRASE. A frase se monta em
		   `ondeMoraOLink()`, funcao pura, fora daqui — porque foi exatamente uma
		   FRASE decidida aqui dentro que saiu errada hoje e o autoteste nao
		   tinha como pegar: o julgamento mora em funcao pura e o autoteste a
		   chama, mas a frase morava no `evaluate`, onde nenhuma afirmacao
		   alcanca. Trecho de decisao dentro do navegador e trecho sem regua. */
		const compra_em_bloco = !!compra && blocos.some((b) => b.contains(compra));
		const blocos_de_compra = blocos.length;

		return {
			/* A PAGINA ENTRA NA CONTA PELO QUE ELA SERVE, NAO PELO COMPONENTE
			   QUE ELA TEM (20/11/2026, despacho NORMAL de 19/11/2026, medido na
			   rodametria e lido no codigo desta ilha).
			   ATE HOJE ESTA LINHA ERA `!!(bloco || document.querySelector(
			   '.rbm-caixa'))` — criterio de COMPONENTE puro. O defeito que isso
			   produz esta medido na irma clubedomosaico, nas 97 URLs dela, uma
			   por uma: 76 paginas servem pelo menos um `rel="...sponsored"` e 59
			   delas nao tem componente de molde nenhum. Ou seja, 59 paginas que
			   VENDEM ALGO e que o portao jogava fora da conta — e o teto de
			   1.400 px da 32.5 nunca era cobrado delas. Pagina que vende algo e
			   sai da conta sai JA VENDENDO.
			   E O DEFEITO AGRAVADO ERA DO PORTAO DA IRMA E NAO DESTE: o dela faz
			   `fora.push(m); continue;` sem imprimir nada. Este imprime a lista
			   de `fora do molde` no rodape — e desde hoje imprime o MOTIVO de
			   cada uma, porque "fora da conta" sem motivo e portao que cala. */
			tem_molde: !!(bloco || formulario || document.querySelector('.rbm-caixa') || compra),
			componente_de_molde: !!(bloco || formulario || document.querySelector('.rbm-caixa')),
			vende_algo: !!compra,
			compra_em_bloco,
			blocos_de_compra,
			tem_patrocinado: !!patrocinado,
			tem_compra: !!bloco,
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

	m.navegacao = !m.vende_algo;
	if (m.navegacao) navegacao.push(m);
	const problemas = reguaDePixel(m);
	m.problemas = problemas;
	if (problemas.length) falhas++;

	const marca = problemas.length ? 'FALHA' : 'ok   ';
	/* A LINHA DIZ ONDE O LINK DE COMPRA MORA, e nao so o pixel dele: com o
	   componente fora do critERIO, "compra a 358 px" nao diz mais se o botao
	   estava num cartao de molde ou solto na pagina. */
	const ondeCurto = m.navegacao ? ' nav.' : String(m.compra).padStart(5);
	console.log(
		`  ${marca} ${m.url.padEnd(56)} ${m.caixa_que.padEnd(11)} ${String(m.caixa).padStart(5)} px  compra ${ondeCurto} px  altura ${String(m.altura).padStart(5)} px` +
			(m.vende_algo && ondeMoraOLink(m).startsWith('FORA') ? `  [compra ${ondeMoraOLink(m)}]` : '') +
			(problemas.length ? `\n         ${problemas.join('; ')}` : '')
	);
}

await navegador.close();

console.log('');
console.log(`  paginas na conta: ${molde.length}   fora da conta: ${fora.length}   (sitemap: ${lista.length})`);
/* O MOTIVO DE CADA UMA QUE FICA FORA, E NAO SO O NOME DELA. O portao da irma faz
   `fora.push(m); continue;` sem imprimir uma palavra, e foi por isso que 59
   paginas que vendem algo sairam da conta dela em silencio — "e a 32.5-b ao
   contrario: nao e portao que mente, e portao que CALA". Aqui, fora da conta e
   pagina que nao tem componente de molde E nao serve link de compra nenhum;
   dizer isso linha por linha e o que permite alguem discordar da classificacao. */
if (fora.length) {
	console.log('  fora da conta (sem componente de molde E sem link de compra nenhum):');
	for (const f of fora) console.log(`    ${f.url}`);
}
if (navegacao.length) {
	console.log(`  de NAVEGACAO (esta na conta, nada para comprar): ${navegacao.map((f) => f.url).join(' ')}`);
}
const comCompra = molde.filter((m) => m.vende_algo);
/* A PIOR CAIXA SE CONTA SO ONDE HA CAIXA. A linha anterior era
   `molde.reduce(... b.caixa ?? 1e9 ...)`, e com a pagina sem caixa dentro da
   conta ela publicaria **1e9** como numero medido — exatamente o que a 23.4
   proibe. O mesmo vale para a pior compra, que se conta so entre as que vendem. */
const comCaixa = molde.filter((m) => m.caixa !== null);
const piorCaixa = comCaixa.length ? Math.max(...comCaixa.map((m) => m.caixa)) : null;
const comPixelDeCompra = comCompra.filter((m) => m.compra !== null);
const piorCompra = comPixelDeCompra.length ? Math.max(...comPixelDeCompra.map((m) => m.compra)) : null;
console.log(
	`  pior caixa: ${piorCaixa === null ? 'nenhuma pagina com caixa' : piorCaixa + ' px'} (teto ${TETO_CAIXA}, contada em ${comCaixa.length} de ${molde.length})` +
		`   pior compra: ${piorCompra === null ? 'nenhuma pagina com link de compra medido' : piorCompra + ' px'} (teto ${TETO_COMPRA}, contada em ${comPixelDeCompra.length} de ${comCompra.length} que vendem algo)`
);
console.log(`  paginas que VENDEM ALGO: ${comCompra.length} — contadas pelo que servem, nao pelo componente que tem`);
console.log(falhas ? `  REPROVADO — ${falhas} pagina(s) na conta fora da 32.5` : `  APROVADO — ${molde.length} de ${molde.length} paginas na conta dentro da 32.5 (${comCompra.length} que vendem algo, ${navegacao.length} de navegacao)`);
process.exit(falhas ? 1 : 0);

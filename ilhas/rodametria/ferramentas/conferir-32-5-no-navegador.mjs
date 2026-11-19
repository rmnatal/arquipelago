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
 * que SERVE o molde — a que tem bloco de compra, formulario de ferramenta OU
 * caixa de resposta. Pagina sem nenhum dos tres e listada como FORA DO MOLDE,
 * nunca aprovada em silencio.
 *
 * CORRIGIDO EM 30/10/2026, E A CAUSA E A 32.5-c: ate aquele dia "estar no molde"
 * exigia bloco de compra OU formulario, entao pagina com caixa de resposta e sem
 * nada para vender caia em FORA DO MOLDE — a caixa dela era medida, impressa e
 * NUNCA julgada contra os 700 px. No dia em que as quatro paginas da 16.1
 * nasceram (bloco 5d), eram quatro paginas de molde que este portao abria e
 * deixava passar. A 32.5 e literal: ter caixa de resposta ja e estar no molde.
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
 *      `a[rel~=sponsored]`, ou um controle de compra de dentro do bloco. ESTE
 *      TETO SO VALE ONDE HA O QUE COMPRAR: pagina que nao vende nada — as
 *      quatro da 16.1, pela 32.2 — recebe "nao se aplica" impresso, nunca um
 *      pulo calado. E a outra metade e cobrada: pagina que serve link
 *      patrocinado FORA de um bloco de compra e REPROVADA, porque sem o
 *      componente o teto nao teria o que medir.
 *   3. ROLAGEM HORIZONTAL, que tem de ser zero.
 *
 * E mais duas que custam o mesmo e dizem se a medicao vale: a ALTURA da pagina e
 * o numero de erros de JavaScript. Pagina que estourou no console pode ter
 * medido um layout que o visitante nao ve.
 *
 * DUAS AFIRMACOES NOVAS, DE 04/11/2026, E AS DUAS SAO DA 32.5-d
 * -------------------------------------------------------------
 *
 * 4. A FOTO DO CARTAO E DE VERDADE, e o portao DIZ quantos cartoes tem foto e
 *    quantos tem o espaco reservado. A 32.5-d existe porque "o portao de pixel
 *    da 32.5 aprovava a pagina de verdade, com o numero de verdade, sobre um
 *    cartao que nenhum visitante com foto jamais veria" — e o portao que ela
 *    consertou CONTINUAVA SEM SABER DIZER QUAL DOS DOIS MUNDOS ELE MEDIU. A
 *    ronda de 04/11 cobrou exatamente isso no "pronto quando" do item 1: as
 *    paginas de molde medidas "com foto de verdade no cartao". Agora:
 *      - `<img>` de cartao que NAO carregou (`complete` falso ou
 *        `naturalHeight` 0) REPROVA a pagina, porque a medicao de pixel foi
 *        feita sobre uma imagem que o visitante nao viu;
 *      - a contagem foto/reservado vai IMPRESSA em toda pagina que vende algo,
 *        para "1.380 px" nunca mais ser lido sem se saber sobre o que.
 *
 * 5. A DECLARACAO DO MOLDE VENCE A REGRA GENERICA DA CASCA — e aqui esta a
 *    segunda metade da 32.5-d, que ficou cinco dias de pe. Em 29/10 ela mediu
 *    que `body.rdm img` (0,1,2) vence `.rdm-molde-cartao-foto` (0,1,0) e
 *    consertou O SELETOR DA FOTO. As OUTRAS declaracoes do molde ficaram em
 *    (0,1,0) e perdiam para `body.rdm p{margin:0 0 16px}` e `body.rdm h2`:
 *    medido nesta nuvem em 04/11 as 16h3xZ, 21 declaracoes perdidas so na
 *    pagina da F2, tres delas dentro do cartao e logo acima do botao que a
 *    32.5 mede (48 px), e o bloco de telefone inteiro — escrito em 29/10 para
 *    COMPRAR pixel — nunca valeu um pixel, porque media query nao acrescenta
 *    especificidade.
 *
 *    Entao o portao varre, em cada pagina do molde, TODO elemento com classe
 *    `rdm-`, acha a regra do molde de maior especificidade e a regra NAO-molde
 *    de maior especificidade para cada propriedade de espaco, e:
 *      - a generica vence E o valor servido discorda do declarado -> REPROVA,
 *        nomeando seletor, propriedade, declarado e servido;
 *      - a generica vence com o MESMO valor -> LATENTE, impresso como registro
 *        e nao como falha. E a licao da nota da secao 2: regra que se comporta
 *        como o valor certo espera o dia em que o valor certo muda.
 *
 * O `--autoteste` NAO PRECISA DE REDE e por isso roda SEMPRE na bancada: ele
 * fabrica as paginas com `setContent`, e um dos mundos refaz a REGUA VELHA (so
 * pixel) ao lado da nova e EXIGE que as duas discordem — autoteste em que as
 * duas concordam nao mede conserto nenhum (20.8).
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

/* AS FOTOS DO CARTAO SAO FORCADAS A CARREGAR ANTES DA MEDICAO, e isto nao e
   conveniencia: e o que torna a medida REPETIVEL.

   Medido em 04/11/2026 as 16h5xZ, no dia em que a contagem de foto entrou neste
   portao: a mesma pagina devolveu `foto 1/4 real` numa passada e `0/4` na
   seguinte, com a CDN da loja respondendo 200 e 197 KB para `curl` nas duas. A
   causa e o `loading="lazy"` do cartao — ele esta a 1.128 px, fora da primeira
   tela, e `waitUntil: 'load'` NAO espera imagem preguicosa que o navegador
   ainda nao decidiu buscar. Entao a foto "nao carregada" era um palpite do
   navegador sobre rolagem, e nao um fato sobre a pagina.

   Portao que responde diferente na mesma pagina e portao que alguem passa a
   ignorar — a licao que a 20.5 nomeou quando o REPROVADO era cache. Aqui a
   pagina e posta no estado em que o visitante a ve quando chega ao bloco de
   compra: `eager` e `decode()`, com UMA segunda tentativa recarregando o `src`.
   Foto que nao carrega em DUAS tentativas e defeito de verdade — ou a URL morreu
   na loja, ou a medicao de pixel seria feita sobre espaco reservado, que e
   exatamente o buraco da 32.5-d. */
async function carregarFotos(pagina) {
	await pagina.evaluate(async () => {
		const imgs = [...document.querySelectorAll('.rdm-molde-compra img')];
		const prazo = (p, ms) => Promise.race([p, new Promise((r) => setTimeout(r, ms))]);
		await Promise.all(imgs.map(async (i) => {
			i.loading = 'eager';
			if (!(i.complete && i.naturalHeight > 0)) {
				await prazo(i.decode().catch(() => {}), 8000);
			}
			if (!(i.complete && i.naturalHeight > 0)) {
				const u = i.currentSrc || i.getAttribute('src') || '';
				i.removeAttribute('src');
				i.setAttribute('src', u);
				await prazo(i.decode().catch(() => {}), 8000);
			}
		}));
	});
	await pagina.waitForTimeout(150);
}

/* A REGUA VELHA, de pixel SO. Ela nao e historia: e o que o autoteste usa para
   exigir que a regua NOVA e ela DISCORDEM no mundo em que a declaracao do molde
   perde a disputa (20.8). Autoteste que prova o que o portao velho ja provava
   nao mede conserto nenhum. */
function reguaDePixel(m) {
	const problemas = [];
	/* O TETO DE CAIXA SE JULGA ONDE HA CAIXA, e ate 19/11/2026 isso era o mesmo
	   que "estar na conta" — por isso a linha era `caixa === null || caixa >=
	   TETO`. Deixou de ser: desde hoje a pagina entra na conta pelo que SERVE
	   (`vende_algo`), e existe pagina na conta com link de compra e SEM
	   formulario e SEM caixa de resposta — `/veiculos/moto-eletrica/` e ela.
	   Cobrar `caixa === null` dessa pagina seria reprovar o degrau que ela nao
	   tem. Os tres ramos se dizem SEPARADOS porque o conserto de cada um e
	   diferente (20.5): ha caixa, mede; nao ha caixa mas ha COMPONENTE de molde,
	   REPROVA (o componente promete o degrau e ele falta, que e o defeito que a
	   linha velha pegava); nao ha nem componente, o teto nao tem o que medir e a
	   linha impressa DIZ isso, em vez de aprovar nem reprovar calado. */
	if (m.caixa !== null) {
		if (m.caixa >= TETO_CAIXA) problemas.push(`${m.caixa_que} a ${m.caixa} px (teto ${TETO_CAIXA})`);
	} else if (m.componente_de_molde) {
		problemas.push(`componente de molde na pagina e NENHUMA caixa nem formulario para medir (teto ${TETO_CAIXA})`);
	}
	/* O TETO DE COMPRA E DO PRIMEIRO LINK DE COMPRA QUE A PAGINA SERVE, tenha ela
	   cartao de molde ou nao (19/11/2026, despacho NORMAL do mesmo dia).
	   Ate hoje esta trava era de DUAS pontas e as DUAS liam COMPONENTE:
	   `tem_compra` (bloco cheio) media o pixel, e `tem_patrocinado` sem bloco
	   REPROVAVA com "o teto de compra nao tem o que medir". A segunda ponta
	   existia para que ninguem ESCAPASSE do teto por nao ter o componente — e no
	   dia em que a 25.2-c pos o piso da busca DENTRO da caixa de ausencia, ela
	   passou a reprovar a pagina que obedece ao contrato. MEDIR E MAIS FORTE QUE
	   REPROVAR: nada escapa do teto, e o que esta certo passa. A frase diz ONDE o
	   link mora, porque com o componente fora da conta o lugar deixa de ser
	   obvio. */
	if (m.vende_algo) {
		if (m.compra === null || m.compra >= TETO_COMPRA) {
			problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA}) — ${m.compra_onde}`);
		}
	}
	if (m.rolagem_h > 0) problemas.push(`rolagem horizontal ${m.rolagem_h} px`);
	if (m.erros > 0) problemas.push(`${m.erros} erro(s) de JavaScript`);
	return problemas;
}

/* A REGUA DE COMPONENTE, a de ate 19/11/2026, e ela existe pelo mesmo motivo da
   de cima: o autoteste exige que a regua NOVA e ela DISCORDEM na pagina que
   SERVE compra sem ter componente de molde nenhum (20.8). Sem ela, o mundo novo
   do autoteste provaria o que o portao velho ja provava. */
function reguaDeComponente(m) {
	if (!m.componente_de_molde) return ['fora da conta — sem componente de molde nenhum'];
	const problemas = [];
	if (m.tem_compra) {
		if (m.compra === null || m.compra >= TETO_COMPRA) problemas.push(`compra a ${m.compra} px (teto ${TETO_COMPRA})`);
	} else if (m.tem_patrocinado) {
		problemas.push('serve link patrocinado e NAO tem bloco de compra — o teto de compra nao tem o que medir');
	}
	return problemas;
}

/* ----------------------------------------------------------------------
   QUAL DAS DUAS? — a classificacao de cada foto que o DOM achou quebrada.

   Ela recebe as URLs COMPLETAS (`quebradas_url`, que a medicao passou a
   devolver ao lado do rabo de 60 caracteres que vai para a tela) e o mapa de
   rede daquela pagina. Tres desfechos, e eles se dizem SEPARADOS porque o
   conserto de cada um e diferente (20.5):

     - `pela_cdn`      a origem RESPONDEU, com status proprio (503, 404...).
                       Isto e defeito que o visitante ve, e REPROVA.
     - `nao_medidas`   a requisicao nem saiu: `ERR_TUNNEL_CONNECTION_FAILED`,
                       `ERR_PROXY_*`, ou um 403 vindo do proxy desta nuvem.
                       Nao se sabe nada da foto, e NAO REPROVA — imprime NAO
                       MEDIDO, que e a unica frase honesta.
     - `sem_veredito`  o DOM diz quebrada e a rede nao tem linha dela (pode
                       nem ter sido pedida). Tambem NAO REPROVA, e e DITA: a
                       afirmacao e positiva (20.8), nunca "o que sobrou e
                       falha".

   O 403 TEM DOIS PAIS, E ISTO E A PARTE QUE PRECISA DE CUIDADO: 403 de proxy e
   403 de CDN sao o mesmo numero. Entao `status` sozinho nao decide — o que
   decide e o `errorText` quando a requisicao falhou, e, no caso de resposta
   403, a frase diz os DOIS mundos possiveis em vez de escolher um. Ela nao
   reprova por 403 nenhum, de proposito: na nuvem em que o egresso recusa este
   dominio, atribuir 403 a CDN e exatamente o erro de 18/11. */
const PROXY_NO_TEXTO = /TUNNEL|PROXY|ERR_CONNECTION_REFUSED|ERR_NAME_NOT_RESOLVED|ERR_SOCKS/i;

function classificarFotos(fotos, rede) {
	const f = fotos || {};
	const urls = f.quebradas_url || [];
	const pela_cdn = [];
	const nao_medidas = [];
	const sem_veredito = [];

	for (const u of urls) {
		const curta = String(u).slice(-60);
		const linha = rede.get(u);
		if (!linha) {
			sem_veredito.push(`${curta} — o DOM diz quebrada e a rede nao tem linha dela`);
			continue;
		}
		if (linha.tipo === 'falha') {
			if (PROXY_NO_TEXTO.test(linha.texto)) {
				nao_medidas.push(`${curta} — ${linha.texto}: o egresso desta nuvem recusou, a foto NAO foi medida`);
			} else {
				pela_cdn.push(`${curta} — a requisicao falhou em ${linha.texto}`);
			}
			continue;
		}
		if (linha.status === 403) {
			nao_medidas.push(`${curta} — HTTP 403, e ele tem dois pais: pode ser a CDN recusando ou o proxy desta nuvem. NAO MEDIDO`);
			continue;
		}
		pela_cdn.push(`${curta} — a CDN respondeu HTTP ${linha.status}`);
	}

	return Object.assign({}, f, { pela_cdn, nao_medidas, sem_veredito });
}


/* A REGUA INTEIRA: pixel, foto de verdade e a disputa de especificidade. */
function julgar(m) {
	const problemas = reguaDePixel(m);
	const f = m.fotos || { quebradas: [] };
	/* SO REPROVA A FOTO CUJA ORIGEM RESPONDEU (item 2 do despacho de 18/11/2026).
	   O que o egresso desta nuvem recusou nao e falha da pagina e nao e veredito
	   nenhum — ele sai no relato, como NAO MEDIDO, e e o Raphael que o destrava
	   pondo `cf.shopee.com.br` na lista de dominios permitidos da conta. */
	if (f.pela_cdn && f.pela_cdn.length) {
		problemas.push(`${f.pela_cdn.length} foto(s) de cartao que a ORIGEM recusou (${f.pela_cdn.join(', ')})`
			+ ' — a medicao de pixel foi feita sobre imagem que o visitante nao viu (32.5-d)');
	}
	/* O TERCEIRO DESFECHO TAMBEM REPROVA, e numa frase SEPARADA: foto que o DOM
	   diz quebrada e a rede nao explica continua quebrada para quem olha a tela
	   — `data:` corrompido cai aqui, e e o mundo 3 do autoteste. O que ela NAO
	   pode e sair com a frase da CDN, porque o conserto nao e o mesmo (20.5). */
	if (f.sem_veredito && f.sem_veredito.length) {
		problemas.push(`${f.sem_veredito.length} foto(s) de cartao que NAO carregaram e a rede nao explica (${f.sem_veredito.join(', ')})`
			+ ' — quebrada para quem olha a tela, e a causa fica em aberto');
	}
	for (const d of (m.disputas || []).filter((x) => x.muda)) {
		problemas.push(`"${d.molde}" [${d.molde_media}] declara ${d.prop}: ${d.declarado} e a pagina serve `
			+ `${d.servido} (o molde pedia ${d.esperado}) — perde por especificidade para "${d.generica}". `
			+ 'Resolva por especificidade e nunca com !important (32.5-d)');
	}
	return problemas;
}

function medirPagina() {
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
	/* O SELETOR DO FORMULARIO E A CLASSE DO COMPONENTE, NAO A DA FERRAMENTA
	   (06/11/2026). Esta linha dizia `form.rdm-f2`, literal, e o comentario acima
	   dizia com todas as letras que "a home e HUB, sem formulario nenhum" — a
	   regra escrita para o mundo que existia. No dia em que a F1 tomou a primeira
	   tela da home, a home PASSOU A TER FORMULARIO e este portao mediu a CAIXA DE
	   RESPOSTA dela, a 792 px, reprovando a pagina pelo degrau de baixo: o
	   formulario de verdade estava a 331 px, com folga de 369 px no teto. E a
	   32.5-c literal — "regra de celular escrita para uma familia de cartao nao
	   alcanca a outra" — com o sinal invertido, porque aqui ela reprovava em vez
	   de aprovar calado.
	   `form.rdm-f-formulario` e a classe do COMPONENTE de formulario desta ilha,
	   que a F1 e a F2 carregam as duas e que toda ferramenta futura vai carregar;
	   `rdm-f1`/`rdm-f2` seguem no HTML como a classe da ferramenta, para a folha.
	   Continua sendo seletor desta ilha e nunca `main form`, que e o que a 32.5-b
	   proibe. */
	const formulario = primeiro('form.rdm-f-formulario');
	const caixa = formulario || primeiro('.rdm-molde-caixa');
	const patrocinado = primeiro('a[rel~="sponsored"]');
	const controle = bloco
		? [...bloco.querySelectorAll('a[rel~="sponsored"], a.rdm-molde-cartao-botao, a.rdm-molde-barra-botao')].find(visivel) || null
		: null;
	const compra = patrocinado || controle;
	/* ONDE O LINK DE COMPRA MORA — e isto nasceu em 19/11/2026 junto com o teto
	   que mede a pagina sem componente de molde. Com o componente fora da conta,
	   "compra a 358 px" nao diz mais sozinho se o link e cartao, barra ou piso da
	   busca, e sao tres consertos diferentes se o numero estourar. A classificacao
	   e por ANCESTRAL e nunca por intencao: cada ramo nomeia a classe que o
	   decidiu. */
	const onde = !compra
		? null
		: (compra.closest('.rdm-molde-compra')
			? 'dentro do bloco de compra (.rdm-molde-compra)'
			: (compra.closest('.rdm-caixa-ausencia')
				? 'dentro da caixa de ausencia (.rdm-caixa-ausencia: o piso da 25.2-c)'
				: 'fora de componente de molde'));

	const medida = {
		/* FAMILIA NOVA ENTRA NO MOLDE PELO SELETOR, NUNCA PELA INTENCAO (32.5-c).
		   Ate 30/10/2026 esta linha dizia `tem_molde: !!(bloco || formulario)`, e
		   com isso TODA pagina que tem caixa de resposta e NAO vende nada caia em
		   "fora do molde": a caixa dela era medida, impressa — e nunca JULGADA
		   contra o teto de 700 px. No dia em que as quatro paginas da 16.1
										nasceram (bloco 5d), eram quatro paginas de molde que o portao
		   abria e nao julgava. A 32.5 e explicita: "o formulario (ou a caixa de
		   resposta, em ficha) comeca antes de 700 px" — ter caixa JA e estar no
		   molde. O teto de COMPRA e que passa a ser julgado so onde ha o que
		   comprar, e onde nao ha o portao DIZ que nao se aplica, em vez de pular
		   calado. */
		/* E A MESMA FAMILIA DO CONSERTO DE 30/10, UM ANDAR ABAIXO (19/11/2026).
		   Ali o portao perdia a pagina que tinha CAIXA e nao vendia nada; aqui
		   perdia a pagina que VENDE e nao tem componente nenhum. Medido no ar:
		   `/veiculos/moto-eletrica/` — a consulta de 823 mil buscas/mes — saia
		   como `fora — sem componente de molde nenhum` e, desde a revisao 116,
		   serve o primeiro link de compra da vida dela, com `rel=sponsored`, dentro
		   da caixa de ausencia da 25.2-c. A pagina passou a ter exatamente a
		   grandeza que este portao existe para medir e continuava fora da conta
		   dele. O criterio deixa de ser o COMPONENTE e passa a ser o que a pagina
		   SERVE: caixa, formulario, bloco — ou link de compra. */
		componente_de_molde: !!(bloco || formulario || primeiro('.rdm-molde-caixa')),
		vende_algo: !!compra,
		compra_onde: onde,
		tem_molde: !!(bloco || formulario || primeiro('.rdm-molde-caixa') || compra),
		/* BLOCO DE COMPRA VAZIO NAO E BLOCO DE COMPRA, E A DIFERENCA E MEDIDA E
		   NAO SUPOSTA (06/11/2026). `!!bloco` sozinho reprovava a home no dia em
		   que a F1 chegou: a 1.7 da especificacao manda a F1 servir o bloco de
		   compra com o produto DA CATEGORIA que a pessoa recebeu, e hoje ZERO dos
		   17 registros do banco declara potencia nominal — entao o bloco existe,
		   imprime A CAUSA (que e o que a secao 7 manda e o que o componente da
		   casca faz por desenho) e NAO tem botao nenhum para medir. O portao dizia
		   `compra a null px` e reprovava uma pagina que esta certa.
		   A distincao nao e por intencao: o estado vazio tem CLASSE PROPRIA
		   (`.rdm-molde-compra-vazio`), escrita pela casca, e e ela que o portao le.
		   E a trava NAO afrouxa, porque a outra metade continua de pe: link
		   patrocinado servido com o bloco vazio cai em `tem_patrocinado` e
		   REPROVA — "isso e defeito, nao isencao". */
		bloco_vazio: !!(bloco && bloco.querySelector('.rdm-molde-compra-vazio')),
		tem_compra: !!(bloco && !bloco.querySelector('.rdm-molde-compra-vazio')),
		tem_patrocinado: !!patrocinado,
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
	/* --------------------------------------------------------------------
	   4. A FOTO DO CARTAO E DE VERDADE? (32.5-d, e o "pronto quando" do item 1
	      do despacho de 04/11/2026)

	   O reservado NAO e um `<img>` — e um `<span>` — e foi isso que escondeu o
	   defeito de 29/10: "a regra generica de imagem nao o alcancava, entao ele
	   obedecia ao molde e media certo". Entao a contagem separa os tres estados,
	   e so o terceiro e falha.
	   -------------------------------------------------------------------- */
	const cartoes = bloco ? [...bloco.querySelectorAll('.rdm-molde-cartao')] : [];
	const imgs = bloco ? [...bloco.querySelectorAll('img')] : [];
	const fotos = {
		cartoes: cartoes.length,
		reais: imgs.filter((i) => i.complete && i.naturalHeight > 0).length,
		quebradas: imgs
			.filter((i) => !(i.complete && i.naturalHeight > 0))
			.map((i) => (i.currentSrc || i.getAttribute('src') || '(sem src)').slice(-60)),
		/* A URL INTEIRA, porque o rabo de 60 caracteres e para a tela e NAO serve
		   de chave: o mapa de rede e indexado pela URL completa (18/11/2026). */
		quebradas_url: imgs
			.filter((i) => !(i.complete && i.naturalHeight > 0))
			.map((i) => i.currentSrc || i.getAttribute('src') || ''),
		reservados: bloco ? bloco.querySelectorAll('.rdm-molde-cartao-sem-foto').length : 0,
		alturas: imgs.map((i) => Math.round(i.getBoundingClientRect().height)),
	};

	/* --------------------------------------------------------------------
	   5. A DECLARACAO DO MOLDE VENCE A REGRA GENERICA? (segunda metade da 32.5-d)

	   A especificidade e contada aqui, a mao e grosseiramente de proposito: o que
	   importa e a ORDEM entre duas regras que casam no MESMO elemento, nao um
	   numero exato de CSS. `:where()` nao conta, como manda a norma.
	   -------------------------------------------------------------------- */
	const PROPS = ['margin-top', 'margin-bottom', 'font-size', 'line-height', 'height',
		'padding-top', 'padding-bottom'];

	const especificidade = (sel) => {
		const s = String(sel).replace(/:where\([^)]*\)/g, ' ');
		const ids = (s.match(/#[\w-]+/g) || []).length;
		const cls = (s.match(/\.[\w-]+|\[[^\]]+\]|:(?!:)[\w-]+(\([^)]*\))?/g) || []).length;
		const tags = (s.replace(/\.[\w-]+|#[\w-]+|\[[^\]]+\]|:+[\w-]+(\([^)]*\))?/g, ' ')
			.match(/[a-zA-Z][\w-]*/g) || []).length;
		return ids * 10000 + cls * 100 + tags;
	};

	const regras = [];
	for (const folha of document.styleSheets) {
		let lista;
		try { lista = folha.cssRules; } catch (e) { continue; }
		const andar = (rs, media) => {
			for (const r of rs) {
				if (r.cssRules && r.conditionText !== undefined) andar(r.cssRules, r.conditionText);
				else if (r.selectorText) regras.push({ sel: r.selectorText, media, st: r.style });
			}
		};
		andar(lista, '');
	}

	const disputas = [];
	const vistas = new Set();
	for (const el of document.querySelectorAll('[class*="rdm-"]')) {
		/* As regras que casam neste elemento, uma vez por ELEMENTO e nao uma vez
		   por propriedade: sao sete propriedades e `el.matches` nao e barato. */
		const casam = [];
		for (const r of regras) {
			if (r.media && !window.matchMedia(r.media).matches) continue;
			let casa = false;
			try { casa = el.matches(r.sel); } catch (e) { casa = false; }
			if (!casa) continue;
			const partes = r.sel.split(',').filter((x) => { try { return el.matches(x); } catch (e) { return false; } });
			casam.push({
				sel: r.sel,
				st: r.st,
				media: r.media,
				e: Math.max(...partes.map(especificidade)),
				/* "do molde" se o pedaco que CASOU neste elemento nomeia uma classe
				   `rdm-`. Regra generica da casca (`body.rdm p`) nao nomeia nenhuma. */
				doMolde: /\.rdm-/.test(partes.join(' ')),
			});
		}
		if (!casam.length) continue;
		const cs = getComputedStyle(el);

		for (const prop of PROPS) {
			const atalho = prop.startsWith('margin') ? 'margin' : (prop.startsWith('padding') ? 'padding' : '');
			let nosso = null;
			let outro = null;
			for (const r of casam) {
				const curto = r.st.getPropertyValue(prop);
				const largo = atalho ? r.st.getPropertyValue(atalho) : '';
				if (!curto && !largo) continue;
				const reg = {
					sel: r.sel, e: r.e, media: r.media,
					prop_aplicar: curto ? prop : atalho,
					valor: curto || largo,
				};
				if (r.doMolde) { if (!nosso || r.e >= nosso.e) nosso = reg; }
				else if (!outro || r.e >= outro.e) outro = reg;
			}
			if (!nosso || !outro || outro.e <= nosso.e) continue;
			const chave = nosso.sel + '|' + prop + '|' + outro.sel;
			if (vistas.has(chave)) continue;
			vistas.add(chave);

			/* MUDA O PIXEL? A declaracao do molde e aplicada INLINE no proprio
			   elemento — estilo inline vence tudo, e as variaveis resolvem no lugar
			   certo da arvore — e o computado volta a ser lido. Quando o que o molde
			   pedia e o que a pagina serve sao o mesmo valor, a disputa e LATENTE:
			   nao custa pixel HOJE, e por isso e impressa em vez de calada. */
			const antes = el.getAttribute('style');
			el.style.setProperty(nosso.prop_aplicar, nosso.valor);
			const esperado = getComputedStyle(el).getPropertyValue(prop);
			if (antes === null) el.removeAttribute('style');
			else el.setAttribute('style', antes);
			const servido = cs.getPropertyValue(prop);

			disputas.push({
				prop,
				molde: nosso.sel,
				molde_media: nosso.media || 'all',
				declarado: (nosso.prop_aplicar === prop ? '' : '(' + nosso.prop_aplicar + ') ') + nosso.valor,
				generica: outro.sel,
				generica_valor: outro.valor,
				servido,
				esperado,
				muda: esperado !== '' && esperado !== servido,
			});
		}
	}

	return Object.assign(medida, { fotos, disputas });
}

const navegador = await chromium.launch(CHROME ? { executablePath: CHROME } : {});
const contexto = await navegador.newContext({
	viewport: { width: LARGURA, height: 844 },
	deviceScaleFactor: 2,
	userAgent:
		'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
});
const pagina = await contexto.newPage();
/* ===========================================================================
 * O AUTOTESTE — mundos FABRICADOS, sem uma requisicao de rede
 *
 * Por que ele existe e por que roda SEMPRE: a bancada pergunta ao arquivo se ele
 * aceita `--autoteste` e roda essa metade no conjunto sem rede, porque "portao
 * que depende de alguem lembrar nao roda". E ele segue a regra do conserto
 * medido (20.8): traz o mundo DE VERDADE que motivou a trava — o cartao da F2 em
 * 04/11/2026, com `body.rdm p` vencendo um `margin:0` do molde — e exige que a
 * regua VELHA e a NOVA DISCORDEM nele.
 * ========================================================================= */
const PNG_1PX = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC';
const PNG_QUEBRADO = 'data:image/png;base64,QUJDREVG';

function paginaFabricada({ prefixo, foto, margemGenerica }) {
	/* `prefixo` liga e desliga o `body.rdm` nas regras do molde, e e a UNICA
	   diferenca entre o mundo de hoje e o de 29/10 a 04/11/2026. A
	   `margemGenerica` e o valor que a regra generica da casca impoe: quando ele
	   e igual ao do molde, a disputa e LATENTE. */
	const q = prefixo ? 'body.rdm ' : '';
	return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><style>
  :root{--rdm-e2:8px;--rdm-e4:16px}
  *{box-sizing:border-box}
  body.rdm{margin:0;font:17px/1.4 sans-serif}
  body.rdm p{margin:0 0 ${margemGenerica};max-width:68ch}
  body.rdm h2{font-size:1.75rem;margin-top:24px}
  .rdm-molde-caixa{padding:8px;border:1px solid #ccc}
  .rdm-f-formulario{padding:8px;border:1px solid #ccc;height:180px}
  .rdm-molde-compra{margin:0}
  ${q}.rdm-molde-cartao-nome{margin:0}
  ${q}.rdm-molde-cartao-spec{margin:0}
  ${q}.rdm-molde-cartao-preco{margin:0}
  body.rdm .rdm-molde-cartao-foto,.rdm-molde-cartao-sem-foto{display:block;width:100%;height:96px;object-fit:contain;background:#eee}
  .rdm-molde-cartao{display:flex;flex-direction:column;gap:4px;border:1px solid #ccc;padding:8px}
  .rdm-molde-cartao-botao{display:block;padding:9px 10px;background:#13212B;color:#fff;text-decoration:none}
  @media (max-width:719px){ ${q}.rdm-molde-cartao-spec{font-size:.6875rem;line-height:1.3} }
</style></head><body class="rdm">
<nav class="rdm-trilha"><a href="/">Inicio</a></nav><h1>Fabricada</h1>
<p class="rdm-promessa">Uma frase de promessa.</p>
<form class="rdm-f2 rdm-f-formulario"><label>Tensao <input value="48"></label></form>
<div class="rdm-molde-caixa"><p class="rdm-molde-caixa-frase">Resposta de exemplo.</p></div>
<section class="rdm-molde-compra" id="comprar"><h2 class="rdm-molde-compra-titulo">A venda agora</h2>
 <p class="rdm-molde-compra-escopo">Escopo em uma frase.</p>
 <ul class="rdm-molde-carrossel" style="display:flex;gap:8px;list-style:none;margin:0;padding:0">
  <li class="rdm-molde-cartao">
   ${foto === 'nenhuma'
		? '<span class="rdm-molde-cartao-sem-foto" aria-hidden="true"></span>'
		: `<img class="rdm-molde-cartao-foto" width="1024" height="1024" src="${foto === 'quebrada' ? PNG_QUEBRADO : PNG_1PX}" alt="">`}
   <p class="rdm-molde-cartao-nome">Modelo X</p>
   <p class="rdm-molde-cartao-spec">500 W no anuncio</p>
   <p class="rdm-molde-cartao-preco">R$ 1.000,00</p>
   <a class="rdm-molde-cartao-botao" rel="sponsored noopener" href="https://exemplo.invalid/x">Ver na loja</a>
  </li>
 </ul>
 <p class="rdm-molde-compra-comissao">Link de afiliado.</p>
</section></body></html>`;
}

if (argv.includes('--autoteste')) {
	const casos = [];
	const medirFabricada = async (html, rede) => {
		await pagina.setContent(html, { waitUntil: 'load' });
		await pagina.waitForTimeout(150);
		await carregarFotos(pagina);
		const m = await pagina.evaluate(medirPagina);
		m.url = '(fabricada)';
		m.erros = 0;
		/* A CLASSIFICACAO E PARTE DA MEDICAO, e o autoteste a CHAMA (nunca uma
		   copia dela): sem isto o mundo da foto quebrada mediria o DOM e
		   deixaria sem prova exatamente a funcao que nasceu em 18/11/2026. O
		   mapa vem fabricado porque rede de verdade nao se fabrica. */
		m.fotos = classificarFotos(m.fotos, rede || new Map());
		return m;
	};
	const afirmar = (nome, ok, detalhe) => {
		casos.push({ nome, ok });
		console.log(`  ${ok ? 'ok   ' : 'FALHA'} ${nome}${ok ? '' : `\n         ${detalhe}`}`);
	};

	/* MUNDO 1 — o de HOJE: o molde carrega `body.rdm` e vence a disputa. */
	const bom = await medirFabricada(paginaFabricada({ prefixo: true, foto: 'real', margemGenerica: '16px' }));
	afirmar('mundo 1: molde prefixado vence — nenhuma disputa custa pixel',
		julgar(bom).length === 0 && bom.disputas.filter((d) => d.muda).length === 0,
		`problemas=${JSON.stringify(julgar(bom))} mudam=${JSON.stringify(bom.disputas.filter((d) => d.muda))}`);
	afirmar('mundo 1: a foto do cartao e contada como REAL',
		bom.fotos.reais === 1 && bom.fotos.quebradas.length === 0 && bom.fotos.cartoes === 1,
		JSON.stringify(bom.fotos));

	/* MUNDO 2 — o de 29/10 a 04/11: o molde SEM prefixo, e a generica da casca
	   vence o `margin:0` dos paragrafos do cartao. E ESTE o mundo em que as duas
	   reguas tem de discordar. */
	const mau = await medirFabricada(paginaFabricada({ prefixo: false, foto: 'real', margemGenerica: '16px' }));
	const mudam = mau.disputas.filter((d) => d.muda);
	afirmar('mundo 2: a declaracao perdida e PEGA, com seletor, propriedade e os dois valores',
		mudam.some((d) => d.molde.includes('rdm-molde-cartao-nome') && d.prop === 'margin-bottom'
			&& d.servido === '16px' && d.esperado === '0px' && d.generica.includes('body.rdm p')),
		JSON.stringify(mudam));
	afirmar('mundo 2: a REGUA VELHA (so pixel) APROVA o mesmo mundo — as duas discordam',
		reguaDePixel(mau).length === 0 && julgar(mau).length > 0,
		`velha=${JSON.stringify(reguaDePixel(mau))} nova=${JSON.stringify(julgar(mau))}`);

	/* MUNDO 3 — a foto que nao carrega SEM a rede explicar: `data:` corrompido,
	   que nao gera evento de rede nenhum. Continua reprovando, e a frase diz que
	   a causa ficou em aberto em vez de atribui-la a CDN. */
	const htmlQuebrada = paginaFabricada({ prefixo: true, foto: 'quebrada', margemGenerica: '16px' });
	const quebrada = await medirFabricada(htmlQuebrada);
	afirmar('mundo 3: foto que NAO carregou reprova a pagina',
		quebrada.fotos.quebradas.length === 1 && julgar(quebrada).some((x) => x.includes('a rede nao explica')),
		`fotos=${JSON.stringify(quebrada.fotos)} problemas=${JSON.stringify(julgar(quebrada))}`);

	/* ------------------------------------------------------------------
	   MUNDOS 3-b E 3-c — ITEM 2 DO DESPACHO DE 18/11/2026, E ELES SAO A RAZAO
	   DA CLASSIFICACAO EXISTIR. A mesma foto quebrada, o mesmo DOM, os mesmos
	   `naturalWidth: 0` — e DOIS vereditos opostos, decididos pela camada de
	   rede. Em 18/11 este portao reprovou tres paginas e uma era falso
	   positivo, porque ele nao tinha como distinguir os dois.
	   ------------------------------------------------------------------ */
	const urlDaFoto = quebrada.fotos.quebradas_url[0];

	const cdn503 = await medirFabricada(htmlQuebrada,
		new Map([[urlDaFoto, { tipo: 'resposta', status: 503 }]]));
	afirmar('mundo 3-b: a ORIGEM respondeu 503 — REPROVA, e a frase diz o status',
		cdn503.fotos.pela_cdn.length === 1
			&& cdn503.fotos.pela_cdn[0].includes('HTTP 503')
			&& cdn503.fotos.nao_medidas.length === 0
			&& julgar(cdn503).some((x) => x.includes('a ORIGEM recusou')),
		`fotos=${JSON.stringify(cdn503.fotos)} problemas=${JSON.stringify(julgar(cdn503))}`);

	const egresso = await medirFabricada(htmlQuebrada,
		new Map([[urlDaFoto, { tipo: 'falha', texto: 'net::ERR_TUNNEL_CONNECTION_FAILED' }]]));
	afirmar('mundo 3-c: o EGRESSO recusou — NAO reprova e sai como NAO MEDIDO',
		egresso.fotos.nao_medidas.length === 1
			&& egresso.fotos.nao_medidas[0].includes('NAO foi medida')
			&& egresso.fotos.pela_cdn.length === 0
			&& julgar(egresso).length === 0,
		`fotos=${JSON.stringify(egresso.fotos)} problemas=${JSON.stringify(julgar(egresso))}`);

	/* A REGUA VELHA OBRIGADA A DISCORDAR (20.8): a de antes de hoje reprovava
	   QUALQUER foto que o DOM achasse quebrada, e e exatamente o mundo 3-c que
	   ela errava. Autoteste em que as duas concordam nao mede conserto nenhum. */
	const reguaVelhaDeFoto = (m) => ((m.fotos.quebradas || []).length ? ['foto quebrada'] : []);
	afirmar('mundo 3-c: a REGUA VELHA de foto REPROVA o mesmo mundo — as duas discordam',
		reguaVelhaDeFoto(egresso).length === 1 && julgar(egresso).length === 0,
		`velha=${JSON.stringify(reguaVelhaDeFoto(egresso))} nova=${JSON.stringify(julgar(egresso))}`);

	/* E O 403 NAO E ATRIBUIDO A NINGUEM, de proposito: proxy e CDN devolvem o
	   mesmo numero, e foi atribui-lo a CDN que produziu a frase errada de
	   18/11 de manha ("a CDN da loja respondeu 503" onde a nuvem nao chegou a
	   CDN). Ele sai como NAO MEDIDO dizendo os dois mundos possiveis. */
	const tresZeroTres = await medirFabricada(htmlQuebrada,
		new Map([[urlDaFoto, { tipo: 'resposta', status: 403 }]]));
	afirmar('mundo 3-d: 403 nao escolhe pai — sai NAO MEDIDO dizendo os dois',
		tresZeroTres.fotos.nao_medidas.length === 1
			&& tresZeroTres.fotos.nao_medidas[0].includes('dois pais')
			&& julgar(tresZeroTres).length === 0,
		`fotos=${JSON.stringify(tresZeroTres.fotos)} problemas=${JSON.stringify(julgar(tresZeroTres))}`);

	/* MUNDO 4 — a disputa LATENTE: a generica vence com o MESMO valor. Nao e
	   falha hoje, e nao pode ser silencio. */
	const latente = await medirFabricada(paginaFabricada({ prefixo: false, foto: 'nenhuma', margemGenerica: '0px' }));
	const doNome = latente.disputas.filter((d) => d.molde.includes('rdm-molde-cartao-nome'));
	afirmar('mundo 4: disputa que a generica ganha com o MESMO valor e LATENTE, nao falha',
		doNome.some((d) => !d.muda) && !doNome.some((d) => d.muda) && julgar(latente).length === 0,
		JSON.stringify(doNome) + ' problemas=' + JSON.stringify(julgar(latente)));
	afirmar('mundo 4: cartao sem foto conta RESERVADO e nao foto quebrada',
		latente.fotos.reservados === 1 && latente.fotos.reais === 0 && latente.fotos.quebradas.length === 0,
		JSON.stringify(latente.fotos));

	/* MUNDO 5 — O FORMULARIO DE OUTRA FERRAMENTA. Em 06/11/2026 o seletor deste
	   portao era `form.rdm-f2`, literal, e no dia em que a F1 tomou a primeira
	   tela da home ele mediu a CAIXA DE RESPOSTA dela (792 px) em vez do
	   FORMULARIO (331 px), reprovando a pagina pelo degrau de baixo. Este mundo
	   fabrica uma pagina com formulario de uma ferramenta QUALQUER — `rdm-f9`, que
	   nao existe — e exige que o portao o ache: regua que depende do nome da
	   ferramenta de hoje e regua que quebra na proxima. */
	const comFormulario = await medirFabricada(
		'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		/* AS ALTURAS SAO ESCOLHIDAS PARA AS DUAS REGUAS DISCORDAREM, e isso e o
		   ponto do mundo: o formulario fica ABAIXO de 700 px (300) e a caixa de
		   resposta ACIMA (300 + 450). A primeira versao deste mundo punha a caixa
		   a 637 px, dentro do teto, e as duas reguas APROVAVAM — autoteste em que
		   elas concordam nao mede conserto nenhum (20.8). */
		+ '<style>body{margin:0;font:16px sans-serif}.alto{height:300px}'
		+ '.mais-alto{height:450px}</style></head>'
		+ '<body class="rdm"><div class="alto"></div>'
		+ '<form class="rdm-f-formulario rdm-f9"><input name="x"></form>'
		+ '<div class="mais-alto"></div>'
		+ '<div class="rdm-molde-caixa"><p class="rdm-molde-caixa-numero">x</p></div>'
		+ '</body></html>');
	afirmar('mundo 5: o portao mede o FORMULARIO de uma ferramenta que ele nao conhece',
		comFormulario.caixa_que === 'formulario' && comFormulario.caixa < 700,
		`caixa_que=${comFormulario.caixa_que} caixa=${comFormulario.caixa}`);
	afirmar('mundo 5: a REGUA VELHA, que media a caixa, REPROVA o mesmo mundo — as duas discordam',
		(() => {
			const velha = { ...comFormulario, caixa: comFormulario.resposta, caixa_que: 'resposta' };
			return reguaDePixel(velha).length > 0 && reguaDePixel(comFormulario).length === 0;
		})(),
		`resposta=${comFormulario.resposta} formulario=${comFormulario.caixa}`);

	/* MUNDO 6 — O BLOCO DE COMPRA VAZIO. A 1.7 da F1 manda servir o bloco com o
	   produto da categoria, e hoje o banco nao tem nenhum classificavel: o bloco
	   imprime A CAUSA e nao tem botao. `!!bloco` sozinho reprovava com
	   `compra a null px` uma pagina que esta certa. E a trava NAO afrouxa: o
	   mundo 6b serve link patrocinado com o bloco vazio e TEM de reprovar. */
	const vazio = await medirFabricada(
		'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		+ '<style>body{margin:0;font:16px sans-serif}</style></head>'
		+ '<body class="rdm">'
		+ '<div class="rdm-molde-caixa"><p class="rdm-molde-caixa-numero">x</p></div>'
		+ '<section class="rdm-molde-compra" id="comprar">'
		+ '<p class="rdm-molde-compra-vazio">Nenhum anuncio colhido declara o que a regra le.</p>'
		+ '</section></body></html>');
	afirmar('mundo 6: bloco de compra VAZIO nao e julgado pelo teto de 1.400 px',
		vazio.bloco_vazio === true && vazio.tem_compra === false && julgar(vazio).length === 0,
		`vazio=${vazio.bloco_vazio} tem_compra=${vazio.tem_compra} problemas=${JSON.stringify(julgar(vazio))}`);

	const vazioComLink = await medirFabricada(
		'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		+ '<style>body{margin:0;font:16px sans-serif}</style></head>'
		+ '<body class="rdm">'
		+ '<div class="rdm-molde-caixa"><p class="rdm-molde-caixa-numero">x</p></div>'
		+ '<section class="rdm-molde-compra" id="comprar">'
		+ '<p class="rdm-molde-compra-vazio">Nenhum anuncio.</p></section>'
		+ '<p><a rel="sponsored nofollow" href="https://exemplo/x">Comprar</a></p>'
		+ '</body></html>');
	/* MUNDO 6b — REESCRITO EM 19/11/2026, E A REESCRITA E O CONSERTO. Ate hoje
	   esta afirmacao exigia que o link patrocinado fora de um bloco REPROVASSE,
	   com a frase "o teto de compra nao tem o que medir". A trava existia contra
	   ESCAPE do teto, e no dia em que a 25.2-c pos o piso da busca dentro da
	   caixa de ausencia ela passou a reprovar a pagina que obedece ao contrato.
	   Agora o link e MEDIDO: aqui ele esta no alto, logo PASSA — e a regua de
	   COMPONENTE, a de ontem, reprova o mesmo mundo. As duas discordam (20.8). */
	afirmar('mundo 6b: bloco VAZIO com link patrocinado ACIMA do teto PASSA — ele e medido, nao reprovado de saida',
		vazioComLink.vende_algo === true && vazioComLink.compra !== null
			&& vazioComLink.compra < TETO_COMPRA && julgar(vazioComLink).length === 0,
		`vende=${vazioComLink.vende_algo} compra=${vazioComLink.compra} problemas=${JSON.stringify(julgar(vazioComLink))}`);
	afirmar('mundo 6b: a REGUA DE COMPONENTE, a de ontem, REPROVA o mesmo mundo — as duas discordam',
		reguaDeComponente(vazioComLink).some((x) => x.includes('patrocinado')) && julgar(vazioComLink).length === 0,
		`componente=${JSON.stringify(reguaDeComponente(vazioComLink))} nova=${JSON.stringify(julgar(vazioComLink))}`);

	/* MUNDO 6c — A OUTRA METADE, E ELA E QUE PROVA QUE NADA AFROUXOU: o mesmo
	   link patrocinado fora de bloco, agora ABAIXO do teto de 1.400 px, TEM de
	   reprovar, e a frase tem de trazer o pixel e o lugar. A regua de ontem
	   tambem reprovava este mundo — pela razao errada, e sem o numero. */
	const vazioComLinkFundo = await medirFabricada(
		'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		+ '<style>body{margin:0;font:16px sans-serif}</style></head>'
		+ '<body class="rdm">'
		+ '<div class="rdm-molde-caixa"><p class="rdm-molde-caixa-numero">x</p></div>'
		+ '<section class="rdm-molde-compra" id="comprar">'
		+ '<p class="rdm-molde-compra-vazio">Nenhum anuncio.</p></section>'
		+ '<div style="height:1600px"></div>'
		+ '<p><a rel="sponsored nofollow" href="https://exemplo/x">Comprar</a></p>'
		+ '</body></html>');
	afirmar('mundo 6c: o MESMO link, abaixo do teto de 1.400 px, REPROVA com o pixel e o lugar',
		julgar(vazioComLinkFundo).some((x) => x.includes(`teto ${TETO_COMPRA}`) && x.includes('fora de componente de molde')),
		JSON.stringify(julgar(vazioComLinkFundo)));

	/* MUNDO 7 — O MUNDO DE VERDADE, medido no ar em 19/11/2026 as 16h4xZ em
	   `/veiculos/moto-eletrica/`, a consulta de 823 mil buscas/mes: ZERO
	   componente de molde no corpo servido (nem bloco, nem formulario, nem caixa
	   de resposta) e UM link `rel=sponsored` dentro da caixa de ausencia da
	   25.2-c. Era o mundo que o portao classificava como `fora — sem componente
	   de molde nenhum` e nunca media, DEPOIS de a pagina ganhar botao de compra.
	   O HTML abaixo e o do ar, reduzido ao que o portao le. */
	const ausencia = (altura) => '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		+ '<style>body{margin:0;font:16px sans-serif}</style></head>'
		+ '<body class="rdm">'
		+ `<div style="height:${altura}px"></div>`
		+ '<div class="rdm-caixa rdm-caixa-ausencia" role="note">'
		+ '<p class="rdm-promessa">A comparacao de precos desta pagina esta sem dados hoje.</p>'
		+ '<p class="rdm-caixa-piso">A loja continua com a busca aberta para esta categoria. '
		+ '<a href="https://s.shopee.com.br/x" rel="sponsored noopener" target="_blank">Veja todos disponiveis aqui</a></p>'
		+ '</div></body></html>';
	const soPiso = await medirFabricada(ausencia(200));
	afirmar('mundo 7: pagina SEM componente de molde e COM link de compra entra na conta',
		soPiso.tem_molde === true && soPiso.componente_de_molde === false && soPiso.vende_algo === true,
		`tem_molde=${soPiso.tem_molde} componente=${soPiso.componente_de_molde} vende=${soPiso.vende_algo}`);
	afirmar('mundo 7: o teto de caixa NAO se aplica, e o de compra mede o piso da 25.2-c',
		soPiso.caixa === null && soPiso.compra !== null && julgar(soPiso).length === 0
			&& soPiso.compra_onde.includes('caixa de ausencia'),
		`caixa=${soPiso.caixa} compra=${soPiso.compra} onde=${soPiso.compra_onde} problemas=${JSON.stringify(julgar(soPiso))}`);
	afirmar('mundo 7: a REGUA DE COMPONENTE joga a pagina FORA DA CONTA — as duas discordam',
		reguaDeComponente(soPiso).some((x) => x.includes('fora da conta')) && julgar(soPiso).length === 0,
		`componente=${JSON.stringify(reguaDeComponente(soPiso))} nova=${JSON.stringify(julgar(soPiso))}`);
	/* E A TRAVA TEM DE MORDER NESSA MESMA PAGINA: o piso empurrado para baixo do
	   teto REPROVA. Sem este mundo, "entrar na conta" poderia ser entrar e passar
	   sempre, que e aprovar calado com um nome novo. */
	const soPisoFundo = await medirFabricada(ausencia(1600));
	afirmar('mundo 7b: o MESMO piso, abaixo de 1.400 px, REPROVA dizendo a caixa de ausencia',
		julgar(soPisoFundo).some((x) => x.includes(`teto ${TETO_COMPRA}`) && x.includes('caixa de ausencia')),
		JSON.stringify(julgar(soPisoFundo)));

	/* MUNDO 8 — O RAMO DO MEIO DO TETO DE CAIXA, que a reescrita de hoje criou e
	   que ninguem pediu: componente de molde PRESENTE e nenhuma caixa nem
	   formulario para medir. A linha velha o pegava de graca (`caixa === null`
	   reprovava); se a nova so medisse "onde ha caixa", este defeito passaria
	   calado — e afrouxar uma trava ao consertar outra e o que a 32.5-b proibe. */
	const blocoSemCaixa = await medirFabricada(
		'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
		+ '<meta name="viewport" content="width=device-width,initial-scale=1">'
		+ '<style>body{margin:0;font:16px sans-serif}</style></head>'
		+ '<body class="rdm">'
		+ '<section class="rdm-molde-compra" id="comprar">'
		+ '<p class="rdm-molde-compra-vazio">Nenhum anuncio.</p></section>'
		+ '</body></html>');
	afirmar('mundo 8: componente de molde SEM caixa nem formulario continua REPROVANDO',
		blocoSemCaixa.componente_de_molde === true && blocoSemCaixa.caixa === null
			&& julgar(blocoSemCaixa).some((x) => x.includes('NENHUMA caixa nem formulario')),
		`componente=${blocoSemCaixa.componente_de_molde} caixa=${blocoSemCaixa.caixa} problemas=${JSON.stringify(julgar(blocoSemCaixa))}`);

	await navegador.close();
	const ruins = casos.filter((c) => !c.ok).length;
	console.log('');
	console.log(`  ${casos.length} afirmacao(oes) em 9 mundo(s) fabricado(s), sem uma requisicao de rede.`);
	console.log(ruins ? `  REPROVADO — ${ruins} afirmacao(oes) do autoteste` : '  APROVADO — autoteste da regua da 32.5 inteiro');
	process.exit(ruins ? 1 : 0);
}


const lista = uma ? [new URL(uma, SITE).toString()] : await sitemapUrls(pagina);

const molde = [];
const fora = [];
let falhas = 0;
let latentes = 0;

for (const url of lista) {
	const erros = [];
	pagina.removeAllListeners('pageerror');
	pagina.on('pageerror', (e) => erros.push(String(e.message || e)));

	/* ------------------------------------------------------------------
	   O DESFECHO DE REDE DE CADA FOTO, OUVIDO ANTES DE A PAGINA PEDIR —
	   ITEM 2 DO DESPACHO DA RONDA DE 18/11/2026.

	   O defeito era deste portao e nao da pagina: ao achar foto que nao
	   carregou, ele escrevia "foto de cartao que NAO carregou" e REPROVAVA,
	   sem ter como saber se a CDN respondeu mal ou se o EGRESSO desta nuvem
	   nunca a deixou sair. Em 18/11 ele reprovou TRES paginas e uma das tres
	   era falso positivo: `cf.shopee.com.br` devolve `CONNECT tunnel failed,
	   response 403` ao egresso desta nuvem (medido duas vezes por URL na ronda
	   daquele dia), e a execucao da manha escreveu "a CDN da loja respondeu
	   503" para um caso em que a nuvem NUNCA CHEGOU a CDN.

	   Veredito de portao que confunde "nao medi" com "esta quebrado" e pior que
	   portao nenhum: ele gasta execucao consertando o que nao esta roto e, na
	   passada seguinte, ensina a ignorar o vermelho dele.

	   A ESCOLHA E DE FONTE: quem sabe a diferenca nao e o DOM — ali os dois
	   mundos sao `naturalWidth: 0` iguaizinhos — e sim a CAMADA DE REDE.
	   `response` traz status da origem; `requestfailed` traz o `errorText` do
	   Chromium, e e nele que mora `ERR_TUNNEL_CONNECTION_FAILED`. Os dois sao
	   guardados por URL, e a classificacao e feita DEPOIS, sobre o que a
	   medicao do DOM achou quebrado.
	   ------------------------------------------------------------------ */
	const rede = new Map();
	pagina.removeAllListeners('response');
	pagina.removeAllListeners('requestfailed');
	pagina.on('response', (r) => {
		rede.set(r.url(), { tipo: 'resposta', status: r.status() });
	});
	pagina.on('requestfailed', (r) => {
		const texto = String((r.failure() && r.failure().errorText) || 'falha sem texto');
		rede.set(r.url(), { tipo: 'falha', texto });
	});

	await pagina.goto(cacheBreak(url), { waitUntil: 'load', timeout: 60000 });
	await pagina.evaluate(() => document.fonts && document.fonts.ready);
	await pagina.waitForTimeout(250);
	await carregarFotos(pagina);

	const m = await pagina.evaluate(medirPagina);
	m.url = url.replace(SITE, '');
	m.erros = erros.length;
	m.fotos = classificarFotos(m.fotos, rede);

	if (!m.tem_molde) {
		/* Pagina que nao serve NENHUMA das grandezas da 32.5: sem bloco de compra,
		   sem formulario de ferramenta, sem caixa de resposta E sem link de compra.
		   Ela sai da conta, mas NUNCA em silencio — o motivo vai impresso para
		   quem ler saber que ela foi aberta. O `link de compra` entrou nesta frase
		   em 19/11/2026: ate aqui o criterio era so componente, e com isso a
		   pagina de 823 mil buscas/mes saia por esta linha JA SERVINDO botao. */
		fora.push(m);
		console.log(`  fora  ${m.url.padEnd(56)} nem componente de molde nem link de compra`);
		continue;
	}
	molde.push(m);

	const problemas = julgar(m);
	m.problemas = problemas;
	if (problemas.length) falhas++;
	latentes += (m.disputas || []).filter((d) => !d.muda).length;

	/* O "nao se aplica" TEM DUAS CAUSAS E ELAS SE DIZEM SEPARADAS, porque o
	   conserto de cada uma e diferente: pagina sem bloco nenhum e desenho (a home
	   HUB, a secao mae, as quatro da 16.1), e bloco PRESENTE e VAZIO e falta de
	   DADO — na F1 de hoje, zero registro com potencia nominal declarada. Fundir
	   as duas numa frase apagaria exatamente a informacao que a secao 7 manda a
	   pagina publicar. */
	const compraTexto = m.vende_algo
		? `compra ${String(m.compra).padStart(5)} px`
		: (m.bloco_vazio
			? 'compra  nao se aplica (bloco de compra VAZIO: a pagina diz a causa)'
			: 'compra  nao se aplica (a pagina nao vende nada)');
	/* O TETO DE CAIXA TAMBEM TEM "NAO SE APLICA", e ele nasceu em 19/11/2026 com a
	   pagina que entra na conta por VENDER: `caixa` vem `null` e imprimi-lo como
	   `resposta  null px` leria como falha o degrau que a pagina nao tem. */
	const caixaTexto = m.caixa === null
		? 'caixa        nao se aplica (sem formulario e sem caixa de resposta)'
		: `${m.caixa_que.padEnd(11)} ${String(m.caixa).padStart(5)} px `;
	/* ONDE O LINK MORA vai impresso em toda pagina que vende algo, pelo mesmo
	   motivo da conta de foto: e o que diz SOBRE QUE MUNDO o pixel ao lado foi
	   medido. */
	const ondeTexto = m.vende_algo ? `  [${m.compra_onde}]` : '';
	/* A CONTA DA FOTO VAI IMPRESSA em toda pagina que vende algo: e ela que diz
	   SOBRE QUE MUNDO o numero de pixel ao lado foi medido (32.5-d). */
	const fotoTexto = m.tem_compra
		? `  foto ${m.fotos.reais}/${m.fotos.cartoes} real, ${m.fotos.reservados} reservado`
		: '';
	const marca = problemas.length ? 'FALHA' : 'ok   ';
	console.log(
		`  ${marca} ${m.url.padEnd(56)} ${caixaTexto} ${compraTexto}  altura ${String(m.altura).padStart(5)} px${fotoTexto}${ondeTexto}` +
			(problemas.length ? `\n         ${problemas.join('; ')}` : '')
	);
}

await navegador.close();

console.log('');
console.log(`  paginas medidas: ${molde.length}   fora da conta: ${fora.length}   (sitemap: ${lista.length})`);
if (fora.length) console.log(`  fora da conta: ${fora.map((f) => f.url).join(' ')}`);
/* A PIOR CAIXA SE MEDE ENTRE AS PAGINAS QUE TEM CAIXA (19/11/2026). Com a
   pagina que entra por VENDER, `caixa ?? 1e9` punha 1e9 na conta da pior e
   imprimia um numero inventado como se fosse medido — a familia do numero sem
   procedencia que a 23.4 proibe. */
const comCaixa = molde.filter((m) => m.caixa !== null);
const piorCaixa = comCaixa.reduce((a, b) => (a === null || (b.caixa ?? 1e9) > a ? b.caixa ?? 1e9 : a), null);
/* QUEM "VENDE ALGO" E QUEM SERVE LINK DE COMPRA, e nao quem tem o componente:
   era `tem_compra` (bloco de molde cheio) e por isso o rodape dizia TRES
   paginas no dia em que as que vendem algo nesta ilha ja eram QUATRO. */
const comCompra = molde.filter((m) => m.vende_algo);
const piorCompra = comCompra.reduce((a, b) => (a === null || (b.compra ?? 1e9) > a ? b.compra ?? 1e9 : a), null);
console.log(`  pior caixa: ${piorCaixa} px (teto ${TETO_CAIXA}) em ${comCaixa.length} pagina(s) com caixa   pior compra: ${piorCompra} px (teto ${TETO_COMPRA}) em ${comCompra.length} pagina(s) que vendem algo`);
console.log(`  disputa(s) de especificidade LATENTE(s) (a generica vence com o MESMO valor): ${latentes} — nao custam pixel hoje, e e por isso que vao impressas`);
console.log(falhas ? `  REPROVADO — ${falhas} pagina(s) medida(s) fora da 32.5` : `  APROVADO — ${molde.length} de ${molde.length} paginas medidas dentro da 32.5`);
process.exit(falhas ? 1 : 0);

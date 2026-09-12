/**
 * Mede o painel da artesa e a ficha da peca num navegador de verdade.
 *
 *   npm i --no-save playwright@1.56.1
 *   php ferramentas/render-para-teste.php . ATELIE hoje "quem_sou=artesa&estado=nova" > /tmp/at/form.html
 *   node ferramentas/teste-navegador-atelie.mjs /tmp/at
 *
 * POR QUE ELE EXISTE, e e a razao mais direta de toda esta ilha: o despacho do
 * Raphael de 12/09/2026 escreve o portao com uma medida dentro dele — "entre em
 * /atelie/ como `artesa`, NUMA JANELA DE 360 PX, cadastre uma peca de teste com 3
 * fotos". A metade do "entre como artesa" a Fundacao nao consegue cumprir, e isso
 * esta explicado no `teste-atelie.php`: a senha dela nao existe para a nuvem, por
 * desenho. Mas a metade da LARGURA da tela uma maquina cumpre melhor que um
 * humano, e e ela que este arquivo cumpre.
 *
 * O QUE SO APARECE DEPOIS DE O CSS SER APLICADO, e por isso o `teste-atelie.php`
 * nao pode ver:
 *
 *   1. ROLAGEM LATERAL. O formulario tem campo largo, `select` e area de texto, e
 *      qualquer um deles estourando a caixa faz a pagina rolar de lado — no
 *      telefone dela, com o dedo, isso e a diferenca entre usar e desistir.
 *   2. ALVO DE TOQUE. Botao de 28 px e botao que ela erra. O piso escrito aqui e
 *      44 px, que e o minimo da diretriz de acessibilidade para toque, e ele vale
 *      para TODO botao e TODO campo do painel — nao so para o principal.
 *   3. O ZOOM QUE O iOS DA SOZINHO. Campo com fonte abaixo de 16 px faz o Safari
 *      do iPhone ampliar a pagina ao receber o foco, a tela pula, e ela perde o
 *      lugar onde estava digitando. A regra e conhecida e invisivel no HTML: so o
 *      motor de layout sabe qual fonte o campo ficou tendo.
 *   4. O FORMULARIO EM UMA COLUNA. Duas colunas a 360 px sao dois campos de 160
 *      px, e o despacho pede "uma tela so", nao "uma tela apertada".
 *
 * A REGUA E DESTE ARQUIVO: 44 px, 16 px e as larguras estao escritos aqui, nao
 * lidos do CSS do snippet. Perguntar ao CSS se ele acha que esta bom nao mede nada
 * (secao 8 do ARQUIPELAGO.md).
 *
 * E A CICATRIZ QUE ELE HERDA, a mesma do `teste-navegador-casca.mjs`: render de
 * bancada que serve METADE da pagina da 0 px de rolagem e a sensacao de ter
 * conferido. Por isso a primeira coisa que ele faz e cobrar que a pagina medida
 * TENHA TAMANHO DE PAGINA — sem a folha do painel, ele reprova antes de medir
 * largura nenhuma.
 */
import { chromium } from 'playwright';
import { readdirSync } from 'node:fs';
import { join } from 'node:path';

const CHROME = process.env.CDM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const pasta = process.argv[2] || '/tmp/at';

/* 360 e o telefone pequeno comum e a medida ESCRITA no despacho; 390 o iPhone
   atual; 412 o Android comum; 782 a borda do menu sanfona desta casca; 1200 o
   desktop. Medir so 360 deixaria a borda de fora, e borda e onde o layout quebra. */
const larguras = [360, 390, 412, 782, 1200];

/* O piso do alvo de toque, em px. Escrito aqui, nao lido do CSS. */
const TOQUE_MINIMO = 44;
/* A fonte minima de campo que nao faz o iOS dar zoom ao focar. */
const FONTE_MINIMA = 16;

let falhas = 0;
let feitos = 0;
function ok(condicao, rotulo, medida = '') {
	feitos++;
	if (condicao) { console.log(`  ok    ${rotulo.padEnd(62)} ${medida}`); return true; }
	falhas++;
	console.log(`  FALHA ${rotulo.padEnd(62)} ${medida}`);
	return false;
}

const arquivos = readdirSync(pasta).filter((a) => a.endsWith('.html')).sort();
if (!arquivos.length) {
	console.log(`Nenhum .html em ${pasta} — renderize antes com render-para-teste.php.`);
	process.exit(1);
}

const navegador = await chromium.launch({ executablePath: CHROME });

/**
 * TODA REQUISICAO QUE SAI DA MAQUINA E ABORTADA, e a medicao fica mais honesta por
 * isso — nao so mais rapida.
 *
 * Medido em 12/09/2026: sem isto, cada `goto` de um `file://` ficava pendurado
 * esperando a folha de fontes do Google, que o egresso deste ambiente nao alcanca,
 * e o arquivo inteiro levava dezenas de minutos para nada. Mas a razao principal
 * nao e o minuto: o que este arquivo mede e o LAYOUT que o CSS da ilha produz, e
 * uma fonte remota que nao carrega nao e defeito da pagina. Deixar a rede no meio
 * faria a medicao depender de uma coisa que nao esta sendo medida.
 *
 * O preco, declarado: as larguras sao medidas com a pilha de recuo da fonte
 * (`Helvetica Neue`, Arial, system-ui), e nao com Outfit. Para rolagem lateral,
 * alvo de toque e tamanho de campo isso e conservador — as fontes de recuo sao
 * mais largas que Outfit nesta escala, entao uma pagina que nao rola de lado aqui
 * tambem nao rola com a fonte certa. O que este arquivo NAO pode afirmar e sobre
 * quebra de linha exata de um texto.
 */
async function semRede(p) {
	await p.route('**/*', (rota) => {
		const url = rota.request().url();
		return url.startsWith('file://') ? rota.continue() : rota.abort();
	});
	p.setDefaultTimeout(20000);
	p.setDefaultNavigationTimeout(20000);
	return p;
}

const pagina = await semRede(await navegador.newPage());

console.log('\nO PAINEL NUM NAVEGADOR DE VERDADE — bloco 4d');
console.log('-'.repeat(80));

console.log('\n0. A pagina medida tem tamanho de pagina (a cicatriz, antes de medir nada)');
for (const arquivo of arquivos) {
	await pagina.goto('file://' + join(pasta, arquivo));
	const retrato = await pagina.evaluate(() => ({
		folhas: document.querySelectorAll('style').length,
		temFolhaDaCasca: !!document.getElementById('cdm-casca'),
		temFolhaDoPainel: !!document.getElementById('cdm-atelie-css') || !!document.getElementById('cdm-loja-css'),
		corpo: (document.querySelector('main') || document.body).innerText.trim().length,
		acoes: document.querySelectorAll('main button, main a.cdm-botao, main a.cdm-at-botao-fraco').length,
		fundo: getComputedStyle(document.body).backgroundColor,
	}));
	ok(retrato.temFolhaDaCasca, `[${arquivo}] a folha da casca esta no head`, `${retrato.folhas} folhas`);
	ok(retrato.temFolhaDoPainel, `[${arquivo}] a folha do bloco 4d esta no head`);
	/* O PISO DE TEXTO DE UM PAINEL NAO E O DE UMA PAGINA DE CONTEUDO, e a primeira
	   escrita deste arquivo confundiu os dois: cravou 200 caracteres — emprestado da
	   regra de pagina fina da secao 8, que existe para pagina que vai ao INDICE — e
	   reprovou a tela de entrar com 162, a lista com 118 e a de criar senha com 195.
	   As tres estao certas: tela de acao boa tem pouco texto e um caminho claro. O
	   painel e `noindex` e nao disputa busca nenhuma, entao o que "pagina montada
	   inteira" significa aqui e outra coisa — ter a folha (medido acima) e ter pelo
	   menos um lugar onde a pessoa AGE, que e o que a linha de baixo cobra. */
	ok(retrato.corpo > 80, `[${arquivo}] o corpo tem texto`, `${retrato.corpo} caracteres`);
	ok(retrato.acoes > 0, `[${arquivo}] a pagina tem pelo menos um lugar onde agir`, `${retrato.acoes} acoes`);
	ok('rgb(255, 255, 255)' === retrato.fundo, `[${arquivo}] miolo branco, como o DESIGN.md manda`, retrato.fundo);
}

console.log('\n1. Rolagem lateral: tem que ser ZERO em toda largura');
for (const arquivo of arquivos) {
	await pagina.goto('file://' + join(pasta, arquivo));
	const medidas = [];
	for (const largura of larguras) {
		await pagina.setViewportSize({ width: largura, height: 900 });
		medidas.push([largura, await pagina.evaluate(() =>
			Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth))]);
	}
	const ruins = medidas.filter(([, excesso]) => excesso > 0);
	ok(0 === ruins.length, `[${arquivo}] sem rolagem lateral em ${larguras.join('/')} px`,
		ruins.length ? ruins.map(([l, e]) => `${l}px: ${e}px`).join(' ') : '0 px em todas');
}

console.log(`\n2. Alvo de toque: TODO botao e TODO campo com ${TOQUE_MINIMO} px ou mais, a 360 px`);
for (const arquivo of arquivos) {
	await pagina.setViewportSize({ width: 360, height: 900 });
	await pagina.goto('file://' + join(pasta, arquivo));
	const pequenos = await pagina.evaluate((minimo) => {
		const alvos = [...document.querySelectorAll(
			'main button, main input:not([type=hidden]), main select, main textarea, main a.cdm-botao, main a.cdm-at-botao-fraco'
		)];
		return alvos.map((e) => {
			const c = e.getBoundingClientRect();
			return { nome: (e.name || e.id || e.value || e.tagName).toString().slice(0, 28), a: Math.round(c.height), l: Math.round(c.width) };
		}).filter((m) => m.a > 0 && m.a < minimo);
	}, TOQUE_MINIMO);
	ok(0 === pequenos.length, `[${arquivo}] nenhum alvo de toque abaixo de ${TOQUE_MINIMO} px`,
		pequenos.length ? pequenos.map((p) => `${p.nome} ${p.l}x${p.a}`).join(', ') : 'todos acima');
}

console.log(`\n3. O zoom que o iOS da sozinho: campo com fonte de ${FONTE_MINIMA} px ou mais`);
for (const arquivo of arquivos) {
	await pagina.setViewportSize({ width: 360, height: 900 });
	await pagina.goto('file://' + join(pasta, arquivo));
	const miudos = await pagina.evaluate((minima) => {
		const campos = [...document.querySelectorAll('main input:not([type=hidden]), main select, main textarea')];
		return campos.map((e) => ({
			nome: (e.name || e.id || e.tagName).toString().slice(0, 28),
			px: parseFloat(getComputedStyle(e).fontSize),
		})).filter((m) => m.px < minima);
	}, FONTE_MINIMA);
	ok(0 === miudos.length, `[${arquivo}] nenhum campo abaixo de ${FONTE_MINIMA} px (sem zoom no iPhone)`,
		miudos.length ? miudos.map((m) => `${m.nome} ${m.px}px`).join(', ') : 'todos em 16px ou mais');
}

console.log('\n4. Uma coluna a 360 px: nenhum campo lado a lado');
for (const arquivo of arquivos) {
	await pagina.setViewportSize({ width: 360, height: 900 });
	await pagina.goto('file://' + join(pasta, arquivo));
	const lado_a_lado = await pagina.evaluate(() => {
		const campos = [...document.querySelectorAll('main input:not([type=hidden]), main select, main textarea')];
		const caixas = campos.map((e) => ({ nome: (e.name || e.id || 'campo').toString().slice(0, 24), ...e.getBoundingClientRect().toJSON() }));
		const pares = [];
		for (let i = 0; i < caixas.length; i++) {
			for (let j = i + 1; j < caixas.length; j++) {
				const a = caixas[i], b = caixas[j];
				/* Mesma faixa vertical E sem sobreposicao horizontal = duas colunas. */
				const mesmaLinha = a.top < b.bottom - 4 && b.top < a.bottom - 4;
				const separados = a.right <= b.left + 1 || b.right <= a.left + 1;
				if (mesmaLinha && separados) { pares.push(`${a.nome}|${b.nome}`); }
			}
		}
		return pares;
	});
	ok(0 === lado_a_lado.length, `[${arquivo}] nenhum par de campos lado a lado a 360 px`,
		lado_a_lado.length ? lado_a_lado.slice(0, 3).join(', ') : 'uma coluna');
}

console.log('\n5. O que a pessoa ve sem rolar, a 360 px (a primeira tela decide)');
/* DUAS REGUAS COM DOIS NOMES, e o erro do meio do caminho vale ser registrado: a
   primeira escrita cobrava "dois elementos na primeira tela" de TODA pagina, e
   reprovou a ficha da peca, que mostra a foto grande e o titulo — exatamente o que
   o DESIGN.md manda ("a foto manda, proporcao 4:5"). Apertar a regua errada
   reprovaria o desenho certo. No PAINEL a primeira tela tem de mostrar por onde
   comecar (titulo mais uma acao); na FICHA ela mostra a peca, e o que importa e o
   PRECO nao ficar enterrado — medido em duas telas, nao em uma. */
const ehFicha = (a) => a.includes('peca');
for (const arquivo of arquivos) {
	await pagina.setViewportSize({ width: 360, height: 640 });
	await pagina.goto('file://' + join(pasta, arquivo));
	if (ehFicha(arquivo)) {
		const alturas = await pagina.evaluate(() => {
			const p = document.querySelector('.cdm-peca-preco');
			const h1 = document.querySelector('h1');
			return {
				preco: p ? Math.round(p.getBoundingClientRect().top) : -1,
				titulo: h1 ? Math.round(h1.getBoundingClientRect().top) : -1,
				tela: window.innerHeight,
			};
		});
		ok(alturas.titulo >= 0 && alturas.titulo < alturas.tela,
			`[${arquivo}] o nome da peca aparece sem rolar`, `${alturas.titulo} px`);
		ok(alturas.preco > 0 && alturas.preco < alturas.tela * 2,
			`[${arquivo}] o preco nao fica enterrado (duas telas)`, `${alturas.preco} px de ${alturas.tela * 2}`);
		continue;
	}
	const primeira = await pagina.evaluate(() => {
		const visiveis = [];
		for (const e of document.querySelectorAll('main h1, main h2, main label, main button, main a.cdm-botao')) {
			const c = e.getBoundingClientRect();
			if (c.top < window.innerHeight && c.bottom > 0 && c.height > 0) {
				visiveis.push((e.innerText || e.value || '').trim().slice(0, 40));
			}
		}
		return visiveis.filter(Boolean);
	});
	ok(primeira.length >= 2, `[${arquivo}] a primeira tela do painel ja mostra por onde comecar`,
		primeira.slice(0, 3).join(' / '));
}

console.log('\n6. Sem JavaScript o painel continua inteiro (portao 22.8)');
/* CONTEXTO PROPRIO COM JS DESLIGADO. E o unico jeito de medir de verdade o que a
   22.8 pede: nao "existe um formulario no HTML", e sim que o que a pessoa ve e
   usa continua de pe quando o script nao roda. */
const contextoSemJs = await navegador.newContext({ javaScriptEnabled: false });
const semJs = await semRede(await contextoSemJs.newPage());
for (const arquivo of arquivos) {
	await semJs.setViewportSize({ width: 360, height: 900 });
	await semJs.goto('file://' + join(pasta, arquivo));
	const retrato = await semJs.evaluate(() => {
		const forms = [...document.querySelectorAll('main form')];
		const botoes = [...document.querySelectorAll('main button[type=submit], main button:not([type])')];
		return {
			forms: forms.length,
			postam: forms.filter((f) => (f.method || '').toLowerCase() === 'post').length,
			botoes: botoes.length,
			visiveis: botoes.filter((b) => b.getBoundingClientRect().height > 0).length,
			links: document.querySelectorAll('main a[href^="https://wa.me/"], main a.cdm-botao').length,
			corpo: (document.querySelector('main') || document.body).innerText.trim().length,
			rolagem: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
		};
	});
	/* A FICHA DA PECA NAO TEM FORMULARIO, e nao deve ter: o botao dela e um link
	   `wa.me`, que e a coisa que mais funciona sem JavaScript que existe. Cobrar
	   formulario dela era a regua do painel aplicada na pagina errada — o que se
	   cobra aqui e que o caminho de acao continue de pe, e ele e outro. */
	if (ehFicha(arquivo)) {
		ok(retrato.links > 0, `[${arquivo}] sem JS: o link de contato continua de pe`, `${retrato.links} links`);
		ok(0 === retrato.forms, `[${arquivo}] sem JS: e ela nao depende de formulario nenhum`);
	} else {
		ok(retrato.forms > 0 && retrato.forms === retrato.postam,
			`[${arquivo}] sem JS: todo formulario ainda POSTa`, `${retrato.postam}/${retrato.forms}`);
		ok(retrato.botoes > 0 && retrato.botoes === retrato.visiveis,
			`[${arquivo}] sem JS: todo botao continua visivel`, `${retrato.visiveis}/${retrato.botoes}`);
	}
	ok(retrato.corpo > 80, `[${arquivo}] sem JS: o corpo continua inteiro`, `${retrato.corpo} caracteres`);
	ok(0 === retrato.rolagem, `[${arquivo}] sem JS: sem rolagem lateral`, `${retrato.rolagem} px`);
}
await contextoSemJs.close();

console.log('\n7. O console nao fala uma linha');
for (const arquivo of arquivos) {
	const vozes = [];
	const p2 = await semRede(await navegador.newPage());
	p2.on('console', (m) => { if (['error', 'warning'].includes(m.type())) vozes.push(`${m.type()}: ${m.text().slice(0, 60)}`); });
	p2.on('pageerror', (e) => vozes.push('pageerror: ' + String(e).slice(0, 60)));
	await p2.setViewportSize({ width: 360, height: 900 });
	await p2.goto('file://' + join(pasta, arquivo));
	await p2.waitForTimeout(250);
	await p2.close();
	/* A folha de fontes do Google nao carrega de um file://, e isso nao e defeito
	   da pagina — as falhas de rede sao descartadas por nome, nunca por serem
	   inconvenientes. */
	const reais = vozes.filter((v) => !/fonts\.googleapis|fonts\.gstatic|googletagmanager|ERR_/.test(v));
	ok(0 === reais.length, `[${arquivo}] console limpo`, reais.length ? reais.slice(0, 2).join(' | ') : 'nenhuma mensagem');
}

await navegador.close();

console.log('\n' + '-'.repeat(80));
console.log(`${feitos} medicoes em ${arquivos.length} paginas x ${larguras.length} larguras, ${falhas} falha(s).`);
console.log('O QUE ISTO NAO SUBSTITUI: o dedo dela na tela. Um motor de layout mede');
console.log('largura, alvo de toque e fonte; ele nao mede se o caminho faz sentido');
console.log('para quem nunca viu um painel. Essa metade continua precisando do domingo.');
process.exit(falhas ? 1 : 0);

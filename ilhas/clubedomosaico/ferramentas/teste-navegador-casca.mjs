/**
 * Mede a casca do Clube do Mosaico num navegador de verdade.
 *
 *   npm i --no-save playwright@1.56.1
 *   php ferramentas/render-para-teste.php . cdm_home > /tmp/render/cdm_home.html
 *   node ferramentas/teste-navegador-casca.mjs /tmp/render
 *
 * O teste-casca.php mede o HTML: o que a pagina DIZ e como ela esta escrita.
 * Este mede o que o HTML VIRA quando um motor de layout o desenha — rolagem
 * horizontal, area de toque do botao do menu e contraste do texto sobre o preto
 * do cabecalho. Sao coisas que so aparecem depois de o CSS ser aplicado.
 *
 * A CICATRIZ QUE ELE CARREGA (secao 8, medida na Robometria em 11/09/2026):
 * render de bancada que serve METADE da pagina da 0 px de rolagem e a sensacao
 * de ter conferido. Por isso a primeira coisa que este arquivo faz e conferir
 * que a pagina medida TEM TAMANHO DE PAGINA: sem a folha da casca no head, sem
 * o cabecalho preto e sem o rodape, ele reprova antes de medir qualquer largura.
 *
 * As larguras nao sao redondas por acaso: 360 e o telefone pequeno comum, 390 o
 * iPhone atual, 782 a quebra em que o proprio WordPress considera que a tela
 * virou celular (e a borda exata do menu sanfona desta casca), e 1200 o
 * desktop. Medir so 360 e 1200 deixaria a borda de fora — e borda e onde o
 * layout quebra.
 */
import { chromium } from 'playwright';
import { readdirSync } from 'node:fs';
import { join } from 'node:path';

const CHROME = process.env.CDM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const pasta = process.argv[2] || '/tmp/render';
const larguras = [360, 390, 781, 782, 783, 1200];

let falhas = 0;
let feitos = 0;
function ok(condicao, rotulo, medida = '') {
	feitos++;
	if (condicao) { console.log(`  ok   ${rotulo.padEnd(58)} ${medida}`); return true; }
	falhas++;
	console.log(`  FALHA ${rotulo.padEnd(58)} ${medida}`);
	return false;
}

const arquivos = readdirSync(pasta).filter((f) => f.endsWith('.html')).sort();
if (!arquivos.length) {
	console.error(`nenhum .html em ${pasta} — rode o render-para-teste.php antes`);
	process.exit(1);
}

const navegador = await chromium.launch({ executablePath: CHROME });
const pagina = await navegador.newPage();

console.log('Clube do Mosaico — medicao da casca num navegador\n');

console.log('0. A pagina medida tem tamanho de pagina (a cicatriz da bancada pela metade)');
for (const arquivo of arquivos) {
	await pagina.setViewportSize({ width: 1200, height: 900 });
	await pagina.goto('file://' + join(pasta, arquivo));
	const retrato = await pagina.evaluate(() => ({
		folha: !!document.getElementById('cdm-casca'),
		cssBytes: (document.getElementById('cdm-casca')?.textContent || '').length,
		rodape: document.querySelectorAll('.cdm-rodape').length,
		marcaTexto: (document.querySelector('.cdm-marca')?.textContent || '').trim(),
		marcaImg: document.querySelectorAll('.cdm-marca img').length,
		fundoCabecalho: getComputedStyle(document.querySelector('header')).backgroundColor,
		corDoMenu: getComputedStyle(document.querySelector('.cdm-nav a') || document.body).color,
		nav: document.querySelectorAll('.cdm-nav a, .cdm-nav .cdm-sem-link').length,
		corpo: (document.querySelector('main')?.textContent || '').trim().length,
	}));
	ok(
		retrato.folha && retrato.cssBytes > 4000 && 1 === retrato.rodape && 'clube do mosaico' === retrato.marcaTexto && 4 === retrato.nav && retrato.corpo > 1200,
		`[${arquivo}] folha, marca legivel, 4 itens de menu, 1 rodape e corpo cheio`,
		`css ${retrato.cssBytes}B · marca "${retrato.marcaTexto}" · nav ${retrato.nav} · corpo ${retrato.corpo} caracteres`
	);
	/* O CABECALHO CLARO, MEDIDO PELO NAVEGADOR e nao pelo texto do CSS: e a
	   diferenca entre "a regra esta escrita" e "a cor que sai na tela". O
	   Raphael reprovou a cor que saiu na tela. */
	ok(
		'rgb(255, 255, 255)' === retrato.fundoCabecalho,
		`[${arquivo}] o cabecalho e claro de verdade no navegador`,
		retrato.fundoCabecalho
	);
	ok(
		'rgb(31, 23, 21)' === retrato.corDoMenu,
		`[${arquivo}] o menu sai em texto escuro sobre o cabecalho claro`,
		retrato.corDoMenu
	);
}

console.log('\n1. Rolagem horizontal: tem que ser ZERO em toda largura');
for (const arquivo of arquivos) {
	/* Uma navegacao por pagina, e depois so o redimensionamento: o reflow de
	   trocar a viewport e o mesmo que o de girar o telefone, e recarregar 6 vezes
	   o mesmo arquivo so gastava minuto. */
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

console.log('\n2. O menu sanfona na borda dos 782 px (secao 6)');
await pagina.goto('file://' + join(pasta, 'cdm_home.html'));
for (const [largura, deveAparecer] of [[360, true], [782, true], [783, false], [1200, false]]) {
	await pagina.setViewportSize({ width: largura, height: 900 });
	const visivel = await pagina.evaluate(() => {
		const b = document.querySelector('.cdm-nav-botao');
		return !!b && getComputedStyle(b).display !== 'none';
	});
	ok(visivel === deveAparecer, `[${largura} px] botao do menu ${deveAparecer ? 'aparece' : 'some'}`, `visivel: ${visivel}`);
}

console.log('\n3. O menu abre, fecha e conta a verdade ao leitor de tela');
await pagina.setViewportSize({ width: 360, height: 900 });
await pagina.goto('file://' + join(pasta, 'cdm_home.html'));
let estado = await pagina.evaluate(() => {
	const b = document.querySelector('.cdm-nav-botao');
	const n = document.querySelector('.cdm-nav');
	return { aria: b.getAttribute('aria-expanded'), lista: getComputedStyle(n).display };
});
ok('false' === estado.aria && 'none' === estado.lista, 'fechado ao carregar, e o aria diz isso', `aria=${estado.aria} display=${estado.lista}`);

await pagina.click('.cdm-nav-botao');
estado = await pagina.evaluate(() => {
	const b = document.querySelector('.cdm-nav-botao');
	const n = document.querySelector('.cdm-nav');
	const caixa = n.getBoundingClientRect();
	return { aria: b.getAttribute('aria-expanded'), lista: getComputedStyle(n).display, direita: caixa.right, largura: window.innerWidth };
});
ok('true' === estado.aria && 'none' !== estado.lista, 'clicou e abriu, e o aria acompanha', `aria=${estado.aria} display=${estado.lista}`);
ok(estado.direita <= estado.largura + 1, 'o menu aberto nao sai pela direita da tela', `borda ${Math.round(estado.direita)} px de ${estado.largura}`);

await pagina.keyboard.press('Escape');
estado = await pagina.evaluate(() => ({
	aria: document.querySelector('.cdm-nav-botao').getAttribute('aria-expanded'),
	focoNoBotao: document.activeElement === document.querySelector('.cdm-nav-botao'),
}));
ok('false' === estado.aria, 'Escape fecha o menu', `aria=${estado.aria}`);
ok(estado.focoNoBotao, 'Escape devolve o foco ao botao (nao deixa foco preso no que sumiu)');

console.log('\n4. Area de toque e contraste');
await pagina.setViewportSize({ width: 360, height: 900 });
await pagina.goto('file://' + join(pasta, 'cdm_home.html'));
const toque = await pagina.evaluate(() => {
	const b = document.querySelector('.cdm-nav-botao').getBoundingClientRect();
	return { largura: b.width, altura: b.height };
});
ok(toque.altura >= 32 && toque.largura >= 32, 'o botao do menu tem area de toque de botao',
	`${Math.round(toque.largura)} x ${Math.round(toque.altura)} px`);

/* Contraste calculado aqui, com a formula da WCAG escrita neste arquivo — a
   regua e propria de proposito: perguntar ao CSS se ele acha que esta legivel
   nao mede nada. */
const contraste = await pagina.evaluate(() => {
	function canal(c) { const s = c / 255; return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4); }
	function lum(rgb) {
		const [r, g, b] = rgb.match(/\d+/g).map(Number);
		return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b);
	}
	function razao(frente, fundo) {
		const a = lum(frente), b = lum(fundo);
		return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
	}
	const link = document.querySelector('.cdm-nav a');
	const rodape = document.querySelector('.cdm-rodape p');
	const corpo = document.querySelector('main p');
	return {
		/* O cabecalho ficou CLARO em 1.2.0: o fundo contra o qual o menu e lido
		   passa a ser o do proprio cabecalho, medido, e nao uma cor escrita aqui —
		   senao esta conta continuaria conferindo contra um preto que saiu da tela. */
		menu: razao(getComputedStyle(link).color, getComputedStyle(document.querySelector('header')).backgroundColor),
		marca: razao(getComputedStyle(document.querySelector('.cdm-marca-nome')).color, getComputedStyle(document.querySelector('header')).backgroundColor),
		rodape: razao(getComputedStyle(rodape).color, 'rgb(0, 0, 0)'),
		corpo: razao(getComputedStyle(corpo).color, 'rgb(255, 255, 255)'),
	};
});
ok(contraste.menu >= 4.5, 'link do menu sobre o cabecalho claro', contraste.menu.toFixed(2) + ':1');
ok(contraste.marca >= 4.5, 'o wordmark sobre o cabecalho claro', contraste.marca.toFixed(2) + ':1');
ok(contraste.rodape >= 4.5, 'texto do rodape sobre o preto', contraste.rodape.toFixed(2) + ':1');
ok(contraste.corpo >= 4.5, 'texto do corpo sobre o branco', contraste.corpo.toFixed(2) + ':1');

/* ---------------------------------------------------------------------------
 * 5. A MESMA PAGINA COM O JAVASCRIPT DESLIGADO.
 *
 * E o que um crawler de IA recebe, e por isso e regra de primeira classe (secao
 * 5 do ARQUIPELAGO.md). Menu sanfona que engole o menu de quem nao executa
 * script trocaria um defeito de celular por um defeito de indexacao — bem pior,
 * porque ninguem o ve.
 *
 * Esta casca foi escrita para sobreviver a isso: quem esconde a lista no
 * celular e o seletor [data-cdm-menu], e esse atributo quem poe e o proprio
 * script. Sem script, o atributo nao existe, a regra de CSS nao casa, e o menu
 * volta a ser o que sempre foi no HTML servido: uma fileira de <a href>.
 * ------------------------------------------------------------------------- */

console.log('\n5. Com o JavaScript DESLIGADO (o que o crawler de IA recebe)');
const semScript = await navegador.newContext({ javaScriptEnabled: false });
const pagina2 = await semScript.newPage();
await pagina2.setViewportSize({ width: 360, height: 900 });
await pagina2.goto('file://' + join(pasta, 'cdm_home.html'));
const semJs = await pagina2.evaluate === undefined ? null : await pagina2.evaluate(() => {
	const links = Array.from(document.querySelectorAll('nav.cdm-nav a'));
	const visiveis = links.filter((a) => a.getBoundingClientRect().height > 0);
	return {
		total: links.length,
		visiveis: visiveis.length,
		rotulos: visiveis.map((a) => a.textContent.trim()).join(' · '),
		textoDoCorpo: (document.querySelector('main')?.textContent || '').trim().length,
		excesso: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
	};
});
ok(4 === semJs.total, 'sem JavaScript, os 4 links do menu existem no HTML', `${semJs.total} links`);
ok(4 === semJs.visiveis, 'sem JavaScript, os 4 continuam VISIVEIS (nao sumiram atras do botao)', semJs.rotulos);
ok(semJs.textoDoCorpo > 1200, 'sem JavaScript, o corpo da pagina continua inteiro', `${semJs.textoDoCorpo} caracteres`);
ok(0 === semJs.excesso, 'sem JavaScript, nenhuma rolagem lateral a 360 px', `${semJs.excesso} px`);
await semScript.close();

await navegador.close();

console.log('');
if (falhas) {
	console.log(`REPROVADO: ${falhas} de ${feitos} medicoes falharam.`);
	process.exit(1);
}
console.log(`APROVADO: ${feitos} medicoes, nenhuma falha.`);

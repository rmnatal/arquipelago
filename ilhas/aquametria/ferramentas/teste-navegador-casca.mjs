// A casca no navegador: o menu do celular e o icone do site.
//
// Os dois itens do bloco 4d de 09/09/2026 sao de CASCA, nao de calculadora, e
// nenhum teste do projeto olhava para o cabecalho. Este olha, e olha do jeito
// que a Sentinela Tecnica das 11h30 olha: abrindo a pagina em Chromium de
// verdade, em tela de celular e em tela de desktop, clicando e teclando.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-casca-para-teste.php . > /tmp/casca.html
//   node ferramentas/teste-navegador-casca.mjs /tmp/casca.html
//
// O caso 8 e o que justifica o desenho todo: ele abre a MESMA pagina com o
// JavaScript DESLIGADO, que e o que um crawler de IA recebe, e exige os tres
// links visiveis dentro de <nav>. Menu sanfona que engole o menu de quem nao
// executa script trocaria um defeito de celular por um defeito de indexacao.

import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

const ARQUIVO = process.argv[2] || '/tmp/casca.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const URL = 'file://' + ARQUIVO;

let falhas = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

const html = readFileSync(ARQUIVO, 'utf8');
const browser = await chromium.launch({ executablePath: CHROME });

/* -------------------------------------------------------------------------
 * 1. O que esta no HTML SERVIDO, antes de qualquer navegador.
 * ---------------------------------------------------------------------- */
console.log('\nHTML servido');
{
  const nav = html.match(/<nav class="aqm-nav"[^>]*>[\s\S]*?<\/nav>/);
  ok('existe <nav class="aqm-nav">', !!nav);
  const links = nav ? nav[0].match(/<a href="[^"]+"/g) || [] : [];
  ok('tres <a href> dentro do <nav>', links.length === 3, `achei ${links.length}`);
  ok('botao declara aria-controls', /aria-controls="aqm-nav-lista"/.test(html));
  ok('botao nasce fechado', /class="aqm-nav-botao" aria-expanded="false"/.test(html));
  ok('o id do <nav> e o que o botao controla', /<nav class="aqm-nav" id="aqm-nav-lista"/.test(html));

  ok('icone SVG na aba', /<link rel="icon" type="image\/svg\+xml" href="data:image\/svg\+xml,/.test(html));
  ok('apple-touch-icon de 180 px em PNG', /<link rel="apple-touch-icon" sizes="180x180" href="data:image\/png;base64,/.test(html));
  ok('o icone do WordPress saiu do wp_head', !/icone-do-wordpress/.test(html));

  // Regra permanente do projeto: script vem do rodape e nao pode ter passado
  // pelos filtros de conteudo, que trocam "&" por "&#038;".
  const scripts = html.match(/<script[\s\S]*?<\/script>/g) || [];
  const escapados = scripts.join('').match(/&#038;/g) || [];
  ok('zero &#038; dentro de <script>', escapados.length === 0, `achei ${escapados.length}`);
  ok('o script do menu existe', scripts.some(s => s.includes('aquametria-casca-menu')));
}

/* -------------------------------------------------------------------------
 * 2. Desktop: nada de botao, os links na fileira.
 * ---------------------------------------------------------------------- */
console.log('\nDesktop (1100 x 900)');
{
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
  const p = await ctx.newPage();
  await p.goto(URL);
  ok('botao escondido', !(await p.locator('.aqm-nav-botao').isVisible()));
  ok('os tres links visiveis', (await p.locator('.aqm-nav a:visible').count()) === 3);
  await ctx.close();
}

/* -------------------------------------------------------------------------
 * 3. Celular: sanfona, teclado e foco.
 * ---------------------------------------------------------------------- */
console.log('\nCelular (390 x 740)');
{
  const ctx = await browser.newContext({ viewport: { width: 390, height: 740 }, hasTouch: true });
  const p = await ctx.newPage();
  await p.goto(URL);

  const botao = p.locator('.aqm-nav-botao');
  const nav = p.locator('.aqm-nav');

  ok('o script assumiu o comando (data-aqm-menu)',
    await p.locator('.aqm-nav-caixa[data-aqm-menu]').count() === 1);
  ok('botao visivel', await botao.isVisible());
  ok('menu comeca fechado', !(await nav.isVisible()));
  ok('aria-expanded=false ao abrir a pagina', (await botao.getAttribute('aria-expanded')) === 'false');

  await botao.click();
  ok('clicar abre o menu', await nav.isVisible());
  ok('aria-expanded=true com o menu aberto', (await botao.getAttribute('aria-expanded')) === 'true');
  ok('os tres links viraram visiveis', (await p.locator('.aqm-nav a:visible').count()) === 3);

  // Escape fecha e devolve o foco ao botao.
  await p.keyboard.press('Escape');
  ok('Escape fecha', !(await nav.isVisible()));
  ok('Escape devolve o foco ao botao',
    await p.evaluate(() => document.activeElement && document.activeElement.classList.contains('aqm-nav-botao')));

  // Teclado puro: Enter no botao abre, Tab chega ao primeiro link.
  await p.keyboard.press('Enter');
  ok('Enter no botao abre', await nav.isVisible());
  await p.keyboard.press('Tab');
  const foco = await p.evaluate(() => {
    const a = document.activeElement;
    return { tag: a.tagName, href: a.getAttribute('href') || '', dentro: !!a.closest('.aqm-nav') };
  });
  ok('Tab leva ao primeiro link do menu', foco.tag === 'A' && foco.dentro, `foco em ${foco.tag}`);
  ok('e o link tem endereco de verdade', /^https?:\/\//.test(foco.href), foco.href);

  // Clique fora fecha.
  await p.locator('main').click({ position: { x: 10, y: 10 } });
  ok('clique fora fecha', !(await nav.isVisible()));

  // Alargar a janela com o menu aberto nao pode deixar aria-expanded mentindo.
  await botao.click();
  await p.setViewportSize({ width: 1100, height: 900 });
  await p.waitForTimeout(120);
  ok('alargar a janela reseta o aria-expanded', (await botao.getAttribute('aria-expanded')) === 'false');

  await ctx.close();
}

/* -------------------------------------------------------------------------
 * 4. O caso do crawler: celular COM JAVASCRIPT DESLIGADO.
 * ---------------------------------------------------------------------- */
console.log('\nCelular sem JavaScript (o que o crawler de IA recebe)');
{
  const ctx = await browser.newContext({ viewport: { width: 390, height: 740 }, javaScriptEnabled: false });
  const p = await ctx.newPage();
  await p.goto(URL);
  ok('sem JavaScript o menu NAO some', (await p.locator('.aqm-nav a:visible').count()) === 3);
  ok('sem JavaScript o botao nao aparece', !(await p.locator('.aqm-nav-botao').isVisible()));
  await ctx.close();
}

/* -------------------------------------------------------------------------
 * 5. Os icones carregam de verdade (data URI que nao decodifica e link morto).
 * ---------------------------------------------------------------------- */
console.log('\nIcone do site');
{
  const ctx = await browser.newContext();
  const p = await ctx.newPage();
  await p.goto(URL);

  const medida = await p.evaluate(async () => {
    function medir(href) {
      return new Promise(res => {
        const img = new Image();
        img.onload = () => res({ w: img.naturalWidth, h: img.naturalHeight });
        img.onerror = () => res({ w: 0, h: 0 });
        img.src = href;
      });
    }
    const svg = document.querySelector('link[rel="icon"][type="image/svg+xml"]');
    const png = document.querySelector('link[rel="apple-touch-icon"]');
    const alt = document.querySelector('link[rel="alternate icon"]');
    return {
      svg: svg ? await medir(svg.href) : null,
      png: png ? await medir(png.href) : null,
      alt: alt ? await medir(alt.href) : null,
      svgTexto: svg ? decodeURIComponent(svg.href.replace('data:image/svg+xml,', '')) : '',
      temaCor: (document.querySelector('meta[name="theme-color"]') || {}).content || '',
    };
  });

  ok('o SVG da aba decodifica e desenha', !!medida.svg && medida.svg.w > 0, JSON.stringify(medida.svg));
  ok('o SVG usa a paleta da marca', /#0D1B22/.test(medida.svgTexto) && /#0E7C8C/.test(medida.svgTexto));
  ok('o PNG do iOS tem 180 x 180', !!medida.png && medida.png.w === 180 && medida.png.h === 180, JSON.stringify(medida.png));
  ok('o PNG alternativo tem 32 x 32', !!medida.alt && medida.alt.w === 32 && medida.alt.h === 32, JSON.stringify(medida.alt));
  ok('theme-color e a tinta da marca', medida.temaCor === '#0D1B22', medida.temaCor);
  await ctx.close();
}

await browser.close();
console.log(falhas ? `\n${falhas} FALHA(S)\n` : '\nTudo passou.\n');
process.exit(falhas ? 1 : 0);

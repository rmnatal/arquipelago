// As quatro páginas da casca num Chromium de verdade: rolagem horizontal e
// console limpo, nas larguras que a Sentinela Técnica usa.
//
//   php ferramentas/render-casca-pagina.php . <slug> > /tmp/aqm-<slug>.html   (as quatro)
//   node ferramentas/teste-navegador-casca-paginas.mjs /tmp
//
// Por que existe, ao lado do teste-voz.mjs: aquele mede o que a página DIZ, e
// mede no texto servido, sem navegador. Este mede o que ela FAZ quando alguém
// abre no telefone. A casca 1.4.0 acrescentou um botão grande e uma prateleira
// de guias — layout novo é onde nasce rolagem horizontal, e 1 px de rolagem no
// celular é defeito que a pessoa sente antes de ler qualquer coisa.
//
// 390 px é o iPhone da vida real; 360 px é o Android mais estreito que ainda
// aparece; 781, 782 e 783 cercam a quebra do menu sanfona — a borda é onde o
// defeito mora, e grade que não pisa na borda é amostra com nome de grade.

import { chromium } from 'playwright';

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
/* As quatro da casca saem do render-casca-pagina.php; as cinco do eixo /peixes/
   (T4, leva 1) saem do render-pagina-completa.php, porque o corpo delas é
   shortcode de outro snippet. Este teste não se importa com quem renderizou: ele
   abre o arquivo aqm-<slug>.html e mede o que o navegador faz. Elas entram aqui
   porque trazem o layout mais largo que a ilha já publicou — cinco tabelas, uma
   delas de seis colunas —, e tabela larga é onde a rolagem horizontal nasce. */
const PAGINAS = [
  'inicio', 'calculadoras', 'metodologia', 'sobre',
  'peixes', 'tetras',
  'quantos-litros-para-tetra-neon',
  'quantos-litros-para-tetra-cardinal',
  'quantos-litros-para-mato-grosso',
];
const LARGURAS = [360, 390, 781, 782, 783, 1200];

let falhas = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

const browser = await chromium.launch({ executablePath: CHROME });

for (const slug of PAGINAS) {
  console.log(`\n/${slug === 'inicio' ? '' : slug + '/'}`);
  const erros = [];
  const page = await browser.newPage();
  page.on('console', (m) => {
    if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|TUNNEL|PROXY)/.test(m.text())) {
      erros.push(m.text());
    }
  });
  page.on('pageerror', (e) => erros.push(String(e)));

  await page.goto('file://' + DIR + '/aqm-' + slug + '.html');

  /* O tamanho da página medida, dito em voz alta. Bancada que serve menos que o
     site mede a metade errada sem nenhum erro aparecer (seção 8 do contrato):
     quem lê este número consegue comparar com o que está no ar. */
  const corpo = await page.evaluate(() => (document.querySelector('main') || document.body).innerText.length);
  console.log(`       corpo medido: ${corpo} caracteres`);

  for (const w of LARGURAS) {
    await page.setViewportSize({ width: w, height: 900 });
    const sobra = await page.evaluate(() =>
      Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth));
    ok(`sem rolagem horizontal a ${w} px`, sobra === 0, `${sobra} px`);
  }

  ok('console sem mensagem', erros.length === 0, erros.slice(0, 2).join(' | '));
  await page.close();
}

await browser.close();
console.log(falhas === 0 ? '\nTUDO OK' : `\n${falhas} FALHA(S)`);
process.exit(falhas === 0 ? 0 : 1);

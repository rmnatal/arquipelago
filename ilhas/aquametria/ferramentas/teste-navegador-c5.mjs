// Teste de navegador da C5 — a calculadora de potência do aquecedor.
//
// Roda a calculadora num Chromium de verdade e confere 15 cenários, entre eles
// os que a revisão de cada calculadora exige: atributos do link de afiliado,
// aviso de comissão visível, as duas barreiras de segurança (voltagem e faixa
// de ajuste), o caso em que nenhuma fonte cobre o delta, o caso sem produto
// que atenda, a mescla do estado compartilhado com a C1 e a C3, e o celular
// de 390 px sem rolagem horizontal.
//
// Como rodar (o container da nuvem já traz o Chromium do Playwright):
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . > /tmp/c5.html   # ou o gerador que você usar
//   node ferramentas/teste-navegador-c5.mjs /tmp/c5.html
//
// O arquivo HTML de entrada é o que o shortcode devolve, dentro de uma página
// mínima. O snippet não depende de WordPress em tempo de execução: todo o
// cálculo é JavaScript no navegador.
//
// O caminho do Chromium abaixo é o do container do Claude Code na nuvem
// (PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers). Em outra máquina, troque.

import { chromium } from 'playwright';

const URL = 'file://' + process.argv[2];
let falhas = 0;
function ok(nome, cond, extra='') {
  console.log(`  ${cond ? 'ok  ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
const page = await ctx.newPage();
const erros = [];
page.on('console', m => { if (m.type() === 'error') erros.push(m.text()); });
page.on('pageerror', e => erros.push('pageerror: ' + e.message));

async function preencher(v, min, opts = {}) {
  await page.evaluate(() => { try { localStorage.clear(); } catch(e){} });
  await page.goto(URL);
  await page.fill('#aqm-c5-volume', String(v));
  await page.fill('#aqm-c5-minima', String(min));
  if (opts.alvo !== undefined) await page.fill('#aqm-c5-alvo', String(opts.alvo));
  if (opts.especie) await page.selectOption('#aqm-c5-especie', opts.especie);
  if (opts.voltagem) await page.selectOption('#aqm-c5-voltagem', opts.voltagem);
  if (opts.tampado) await page.selectOption('#aqm-c5-tampado', opts.tampado);
  if (opts.sul) await page.check('#aqm-c5-sul');
  await page.click('#aqm-c5-form button[type=submit]');
  await page.waitForTimeout(120);
}
const txt = s => page.locator(s).innerText();

console.log('\n1. caso base — 110 L, alvo 26 (betta? nao: manual), minima 20, 110 V');
await preencher('110', '20', { alvo: '26', voltagem: '110' });
ok('faixa 110 a 165 W', (await txt('#aqm-c5-faixa-valor')).replace(/\s+/g,' ').includes('110 a 165'), await txt('#aqm-c5-faixa-valor'));
ok('delta 6,0 C', (await txt('#aqm-c5-delta')).includes('6,0'), (await txt('#aqm-c5-delta')).replace(/\n/g,' | '));
ok('comercial 200 W', (await txt('#aqm-c5-comercial')).includes('200 W'));
const prods = await page.locator('#aqm-c5-produtos-lista .aqm-c5-produto').count();
// A regra do projeto e de 3 a 5 produtos no bloco, ordenados por adequacao tecnica.
// Ate 08/09/2026 o banco so tinha aquecedor para tres cartoes nesse caso; com a expansao
// do catalogo (09/09) sao cinco. Fixar o numero em 3 fazia o teste reprovar a cada produto
// novo, entao ele passou a conferir a FAIXA que a regra manda.
ok('de 3 a 5 produtos na lista', prods >= 3 && prods <= 5, `veio ${prods}`);
ok('bloco de produto visivel', await page.locator('#aqm-c5-produtos').isVisible());

console.log('\n2. atributos do link de afiliado (exigencia do projeto)');
const links = page.locator('#aqm-c5-produtos-lista a.aqm-c5-loja');
const nlinks = await links.count();
ok('ha pelo menos um link de loja', nlinks > 0, `${nlinks} link(s)`);
for (let i = 0; i < nlinks; i++) {
  const rel = await links.nth(i).getAttribute('rel');
  const tgt = await links.nth(i).getAttribute('target');
  const href = await links.nth(i).getAttribute('href');
  ok(`link ${i+1} rel/target/https`, rel === 'sponsored noopener' && tgt === '_blank' && href.startsWith('https://'), `${rel} | ${tgt}`);
}
ok('aviso de comissao visivel', await page.locator('.aqm-c5-aviso-afiliado').isVisible());
ok('aviso de voltagem em todo cartao com link', await page.locator('.aqm-c5-voltaviso').count() === nlinks);

console.log('\n3. seguranca: voltagem 220 V filtra a lista');
await preencher('110', '20', { alvo: '26', voltagem: '220' });
const sub220 = await txt('#aqm-c5-produtos-sub');
ok('subtitulo cita 220 V', sub220.includes('220 V'));
const link220 = await page.locator('#aqm-c5-produtos-lista a.aqm-c5-loja').first().innerText().catch(()=>'');
const aviso220 = await page.locator('.aqm-c5-voltaviso').first().innerText().catch(()=>'');
ok('aviso avisa que o anuncio era de outra voltagem', aviso220.includes('220 V'), aviso220.slice(0,110));

console.log('\n4. seguranca: alvo de 33 C barra o Roxin pela faixa conservadora');
await preencher('200', '25', { alvo: '33', voltagem: '110' });
const fora = await page.locator('#aqm-c5-produtos-lista li.aqm-c5-criterio').innerText().catch(()=>'');
ok('Roxin barrado com motivo na tela', fora.includes('Roxin') && fora.includes('32'), fora.slice(0,150));
ok('Eheim continua na lista', (await page.locator('#aqm-c5-produtos-lista .aqm-c5-produto').count()) > 0);

console.log('\n5. alvo de 20 C barra o Roxin pelo piso conservador (22 C)');
await preencher('60', '14', { alvo: '20', voltagem: '110' });
const fora2 = await page.locator('#aqm-c5-produtos-lista li.aqm-c5-criterio').innerText().catch(()=>'') + await page.locator('#aqm-c5-produtos-nada').innerText().catch(()=>'');
ok('motivo do piso conservador aparece', fora2.includes('começa em') && fora2.includes('22'), fora2.slice(0,150));

console.log('\n6. delta acima de 10 C: nenhuma fonte cobre');
await preencher('200', '14', { alvo: '28', voltagem: '110' });
const av = await txt('#aqm-c5-avisos');
ok('diz que nenhuma fonte cobre', av.includes('nenhuma fonte do nosso levantamento cobre'), av.slice(0,120));
ok('regra do delta marcada como nao aplicavel', (await page.locator('#aqm-c5-regras .aqm-c5-cartao-fora').count()) >= 1);
ok('faixa vira 1,0 a 1,3 W/L', (await txt('#aqm-c5-faixa-criterio')).includes('1,00 a 1,30'), await txt('#aqm-c5-faixa-criterio'));

console.log('\n7. regiao Sul entra na conta');
await preencher('110', '18', { alvo: '26', voltagem: '110', sul: true });
ok('teto vira 220 W (2,0 W/L)', (await txt('#aqm-c5-faixa-valor')).includes('220'), await txt('#aqm-c5-faixa-valor'));
ok('cartao do Sul aplicavel', (await txt('#aqm-c5-regras')).toLowerCase().includes('leitura do sul'));

console.log('\n8. delta zero ou negativo: nao devolve numero');
await preencher('110', '28', { alvo: '26', voltagem: '110' });
ok('painel de delta zero visivel', await page.locator('#aqm-c5-semdelta').isVisible());
ok('corpo do resultado escondido', !(await page.locator('#aqm-c5-corpo').isVisible()));
ok('texto explica', (await txt('#aqm-c5-semdelta')).includes('nunca cai abaixo'));

console.log('\n9. especie preenche o alvo pelo meio da faixa, com fonte');
await preencher('30', '20', { especie: 'betta', voltagem: '110' });
ok('alvo 26,0 (meio de 24-28)', (await txt('#aqm-c5-delta')).includes('26,0'), (await txt('#aqm-c5-delta')).replace(/\n/g,' | '));
ok('declara a convencao do meio da faixa', (await txt('#aqm-c5-editoriais')).includes('meio da faixa'));
ok('ficha da especie cita a Petz', (await txt('#aqm-c5-especie-ficha')).includes('Petz'));

console.log('\n10. aquario sem produto que atenda');
await preencher('900', '10', { alvo: '28', voltagem: '110' });
ok('bloco de produto some', !(await page.locator('#aqm-c5-produtos').isVisible()));
ok('explica por que nao ha produto', (await txt('#aqm-c5-produtos-nada')).includes('banco'), (await txt('#aqm-c5-produtos-nada')).slice(0,140));
ok('diz que passa da linha comercial', (await txt('#aqm-c5-comercial')).includes('maior degrau'));

console.log('\n11. estado compartilhado com a C1/C3');
await page.goto(URL);
await page.evaluate(() => localStorage.setItem('aquametria.aquario', JSON.stringify({
  versao:1, calculadora:'c1-litragem', apelido:'meu 60',
  medidas:{comprimento_cm:60,largura_cm:30,altura_cm:36},
  volumes:{real_L:54.5}, perfil:{tipo_aquario:'plantado'},
  equipamentos:{filtro_vazao_alvo_lh:[96,545]}
})));
await page.goto(URL);
await page.waitForTimeout(100);
ok('volume veio da C1', (await page.inputValue('#aqm-c5-volume')) === '54,5', await page.inputValue('#aqm-c5-volume'));
ok('avisa que retomou', await page.locator('#aqm-c5-retomado').isVisible());
ok('nao calcula sem a minima', !(await page.locator('#aqm-c5-saida').isVisible()));
await page.fill('#aqm-c5-minima', '19');
await page.fill('#aqm-c5-alvo', '26');
await page.click('#aqm-c5-form button[type=submit]');
await page.waitForTimeout(120);
const estado = await page.evaluate(() => JSON.parse(localStorage.getItem('aquametria.aquario')));
ok('mescla preserva medidas da C1', estado.medidas && estado.medidas.comprimento_cm === 60);
ok('mescla preserva o que a C3 gravou', estado.equipamentos.filtro_vazao_alvo_lh[1] === 545);
ok('C5 grava a potencia alvo', Array.isArray(estado.equipamentos.aquecedor_potencia_alvo_w), JSON.stringify(estado.equipamentos.aquecedor_potencia_alvo_w));
ok('C5 grava o clima', estado.clima.delta_C === 7 && estado.clima.temp_min_ambiente_C === 19, JSON.stringify(estado.clima));
ok('C5 grava a voltagem', estado.eletrica.voltagem === '110');

console.log('\n12. permalink e caminho inverso');
const link = await page.inputValue('#aqm-c5-link');
ok('permalink tem volume, minima e alvo', link.includes('v=54.5') && link.includes('min=19') && link.includes('alvo=26'), link);
await page.fill('#aqm-c5-tenho', '100');
await page.click('#aqm-c5-tenho-calcular');
await page.waitForTimeout(60);
const inv = await txt('#aqm-c5-tenho-saida');
ok('caminho inverso responde com as regras', inv.includes('ReefFlow') && inv.includes('W por litro'), inv.slice(0,130));

console.log('\n13. erro de unidade e campos obrigatorios');
await page.goto(URL);
await page.evaluate(() => { try { localStorage.clear(); } catch(e){} });
await page.goto(URL);
await page.click('#aqm-c5-form button[type=submit]');
await page.waitForTimeout(80);
ok('lista os 3 erros', (await page.locator('#aqm-c5-erros li').count()) === 3, String(await page.locator('#aqm-c5-erros li').count()));
ok('resultado escondido', !(await page.locator('#aqm-c5-saida').isVisible()));
await page.fill('#aqm-c5-volume', '99999');
await page.fill('#aqm-c5-minima', '18');
await page.fill('#aqm-c5-alvo', '26');
await page.click('#aqm-c5-form button[type=submit]');
await page.waitForTimeout(80);
ok('barra volume absurdo', (await txt('#aqm-c5-erros')).includes('confira a unidade'));

console.log('\n14. celular de 390 px, sem rolagem horizontal');
const mob = await browser.newContext({ viewport: { width: 390, height: 800 } });
const p2 = await mob.newPage();
p2.on('pageerror', e => erros.push('pageerror mobile: ' + e.message));
await p2.goto(URL);
await p2.fill('#aqm-c5-volume', '110');
await p2.fill('#aqm-c5-minima', '20');
await p2.fill('#aqm-c5-alvo', '26');
await p2.click('#aqm-c5-form button[type=submit]');
await p2.waitForTimeout(150);
const larg = await p2.evaluate(() => ({ doc: document.documentElement.scrollWidth, win: window.innerWidth }));
ok('sem rolagem horizontal', larg.doc <= larg.win + 1, JSON.stringify(larg));

console.log('\n15. console limpo');
ok('zero erro de console', erros.length === 0, erros.join(' | '));

await browser.close();
console.log(`\n=== ${falhas === 0 ? 'TODOS OS CASOS PASSARAM' : falhas + ' FALHA(S)'} ===`);
process.exit(falhas ? 1 : 0);

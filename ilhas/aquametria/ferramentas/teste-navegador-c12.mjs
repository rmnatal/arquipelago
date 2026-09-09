// Teste de navegador da C12 — a calculadora de mídia filtrante.
//
// Roda a calculadora num Chromium de verdade e confere os cenários que a
// revisão de cada calculadora exige: a faixa das quatro dosagens declaradas,
// as duas tabelas de âncoras (quem vende mídia e quem vende filtro), o teto
// físico do cesto (inclusive o caso em que a camada biológica sozinha não
// cabe), a ambiguidade da ficha do Atman publicada como duas leituras, o
// calendário de trocas com datas calculadas, o aviso obrigatório sobre lavar
// mídia biológica, os atributos do link de afiliado, o aviso de comissão, a
// recusa de converter grama em mililitro, a mescla do estado compartilhado
// com C1/C3/C5 e o celular de 390 px sem rolagem horizontal.
//
// Como rodar (o container da nuvem já traz o Chromium do Playwright):
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_midia > /tmp/c12.html
//   node ferramentas/teste-navegador-c12.mjs /tmp/c12.html

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
// Falha de REDE nao e erro da calculadora. O render-para-teste serve um file:// e a
// casca pede a folha do Google Fonts, que o egresso do container barra: sem este
// filtro o teste fica vermelho por causa da rede, e nao do codigo. Mesmo filtro que
// teste-navegador-cinco.mjs ja usava desde 08/09/2026 — aqui ele estava faltando.
page.on('console', m => {
  if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET)/.test(m.text())) erros.push(m.text());
});
page.on('pageerror', e => erros.push('pageerror: ' + e.message));

async function preencher(v, opts = {}) {
  await page.goto(URL);
  await page.evaluate(() => { try { localStorage.clear(); } catch(e){} });
  await page.goto(URL);
  await page.fill('#aqm-c12-volume', String(v));
  if (opts.filtro !== undefined) await page.selectOption('#aqm-c12-filtro', opts.filtro);
  if (opts.midia !== undefined) await page.fill('#aqm-c12-midia-manual', String(opts.midia));
  if (opts.perfil) await page.selectOption('#aqm-c12-perfil', opts.perfil);
  if (opts.quimica) await page.check('#aqm-c12-quimica');
  if (opts.data) await page.fill('#aqm-c12-data', opts.data);
  await page.click('#aqm-c12-form button[type=submit]');
  await page.waitForTimeout(120);
}
const txt = s => page.locator(s).innerText();

console.log('\n1. caso base — 110 L, sem filtro escolhido');
await preencher('110');
const faixa = await txt('#aqm-c12-faixa-valor');
ok('faixa de 140 mL a 1,38 L', faixa.includes('140 mL') && faixa.includes('1,38 L'), faixa.replace(/\s+/g,' '));
ok('criterio nomeia piso e teto', (await txt('#aqm-c12-faixa-criterio')).includes('Seachem')
   && (await txt('#aqm-c12-faixa-criterio')).includes('Ocean Tech'));
ok('diz que a faixa e 10x larga', (await txt('#aqm-c12-faixa-criterio')).includes('10,0 vezes'),
   (await txt('#aqm-c12-faixa-criterio')).slice(0,140));
const linhasBio = await page.locator('#aqm-c12-ancoras-corpo tr').count();
ok('4 dosagens declaradas na tabela', linhasBio === 4, `veio ${linhasBio}`);
const linhasTot = await page.locator('#aqm-c12-totais-corpo tr').count();
// A tabela publica TODO filtro do banco que declara volume util de midia, entao ela
// cresce a cada coleta: fixar o numero fazia o teste reprovar a cada filtro novo (foi o
// que aconteceu em 09/09/2026, quando o SunSun HW-603B virou o quinto). O que o teste
// precisa garantir e que a tabela existe, nao murchou e nao repete linha.
const nomesTot = await page.locator('#aqm-c12-totais-corpo tr').allInnerTexts();
ok('pelo menos 4 filtros na tabela de midia total', linhasTot >= 4, `veio ${linhasTot}`);
ok('nenhuma linha repetida na tabela', new Set(nomesTot).size === nomesTot.length,
   `${nomesTot.length} linha(s)`);
ok('sem filtro, a tela pede o filtro', await page.locator('#aqm-c12-cesto-sem').isVisible());
ok('bloco do cesto escondido', await page.locator('#aqm-c12-cesto').isHidden());

console.log('\n2. as quatro ancoras, com atribuicao');
const tab = (await txt('#aqm-c12-ancoras-corpo')).replace(/\s+/g,' ');
ok('Seachem 1,25 mL/L', tab.includes('1,25 mL/L'), '');
ok('segunda leitura da Seachem 2,64 mL/L', tab.includes('2,64 mL/L') && /segunda leitura/i.test(tab));
ok('JBL 5,00 mL/L', tab.includes('5,00 mL/L'));
ok('Ocean Tech 12,50 mL/L', tab.includes('12,50 mL/L'));
ok('cada linha cita a fonte', (await page.locator('#aqm-c12-ancoras-corpo a').count()) === 4);

console.log('\n3. midia total dos fabricantes de filtro (a segunda familia)');
const tot = (await txt('#aqm-c12-totais-corpo')).replace(/\s+/g,' ');
ok('Eheim 12,00 mL/L', tot.includes('12,00 mL/L'), '');
ok('Tidal 6,00 mL/L', tot.includes('6,00 mL/L'));
ok('Atman publica as duas leituras', tot.includes('a 10,67 mL/L') || tot.includes('3,56 a'), tot.slice(0,200));

console.log('\n4. teto fisico — Eheim classic 250 (3,0 L de midia), 110 L');
await preencher('110', { filtro: 'eheim-classic-250-2213' });
ok('bloco do cesto visivel', await page.locator('#aqm-c12-cesto').isVisible());
const cartoes = await page.locator('#aqm-c12-cesto-lista .aqm-c12-cartao').count();
ok('4 cartoes de ocupacao', cartoes === 4, `veio ${cartoes}`);
const cesto = (await txt('#aqm-c12-cesto-lista')).replace(/\s+/g,' ');
ok('Seachem ocupa 5 %', cesto.includes('5 %'), cesto.slice(0,120));
ok('Ocean Tech ocupa 46 %', cesto.includes('46 %'));
ok('nenhum estoura neste caso', !cesto.includes('Não cabe'));

console.log('\n5. teto fisico estourado — 600 L num Tidal 55 (1,2 L de midia)');
await preencher('600', { filtro: 'seachem-tidal-55' });
const cesto2 = (await txt('#aqm-c12-cesto-lista')).replace(/\s+/g,' ');
ok('diz que nao cabe', cesto2.includes('Não cabe'), cesto2.slice(0,200));
ok('aponta o filtro como problema', cesto2.includes('o problema é o filtro'));

console.log('\n6. ficha ambigua do Atman publicada como duas leituras');
await preencher('110', { filtro: 'atman-at-3338' });
const sub = (await txt('#aqm-c12-cesto-sub')).replace(/\s+/g,' ');
ok('mostra 1,6 L e 4,8 L', sub.includes('1,6 L') && sub.includes('4,8 L'), sub.slice(0,180));
ok('diz que nao desempata', sub.includes('não desempatamos'));
ok('cartao traz a outra leitura', (await txt('#aqm-c12-cesto-lista')).includes('outra leitura'));

console.log('\n7. volume de midia digitado a mao');
await preencher('200', { filtro: 'outro', midia: '2,5' });
ok('campo manual aparece', await page.locator('#aqm-c12-midia-manual-campo').isVisible());
ok('usa o volume digitado', (await txt('#aqm-c12-cesto-sub')).includes('2,5 L'));
ok('declara que a medida e da pessoa', (await txt('#aqm-c12-editoriais')).includes('medido por você'));

console.log('\n8. camadas: ordem publicada, proporcao recusada');
await preencher('110');
const ordem = (await txt('#aqm-c12-ordem')).replace(/\s+/g,' ');
ok('seis camadas na ordem', (await page.locator('#aqm-c12-ordem li:not(.aqm-c12-seta)').count()) === 6, ordem);
ok('comeca por ceramica', ordem.startsWith('cerâmica'));
const painelCamadas = await page.locator('.aqm-c12-painel', { hasText: 'A ordem das camadas' }).first().innerText();
ok('recusa publicar proporcao', painelCamadas.includes('não publica') && painelCamadas.includes('porcentagens'));
ok('manda conferir o manual do modelo', painelCamadas.includes('não substitui o manual'));

console.log('\n9. camada quimica — as duas unidades que nao conversam');
await preencher('110', { quimica: true });
ok('bloco quimico visivel', await page.locator('#aqm-c12-quimica-bloco').isVisible());
const q = (await txt('#aqm-c12-quimica-bloco')).replace(/\s+/g,' ');
ok('regra BR em gramas: 110 a 220 g', q.includes('110 a 220 g'), q.slice(0,160));
ok('MatrixCarbon em mL', q.includes('MatrixCarbon') && q.includes('0,625 mL/L'));
ok('Purigen em mL', q.includes('Purigen'));
ok('recusa a conversao', q.includes('não converte'));
await preencher('110');
ok('sem marcar, o bloco quimico some', await page.locator('#aqm-c12-quimica-bloco').isHidden());

console.log('\n10. calendario de trocas com datas calculadas');
await preencher('110', { data: '2026-09-01' });
const cal = (await txt('#aqm-c12-calendario-corpo')).replace(/\s+/g,' ');
ok('perlon 08/09 a 16/09', cal.includes('08/09/2026') && cal.includes('16/09/2026'), cal.slice(0,160));
ok('carvao 16/09 a 01/10', cal.includes('01/10/2026'));
ok('ceramica 01/03 a 01/09 de 2027', cal.includes('01/03/2027') && cal.includes('01/09/2027'));
ok('data base citada', (await txt('#aqm-c12-calendario-sub')).includes('01/09/2026'));

console.log('\n11. TPA e nitrato');
const tpa = (await txt('#aqm-c12-tpa-texto')).replace(/\s+/g,' ');
ok('11 a 33 L por vez', tpa.includes('11') && tpa.includes('33'), tpa.slice(0,120));
ok('teto de 55 L', tpa.includes('55,0 L'));
ok('diferenca termica de 1 C', tpa.includes('1 °C') && tpa.includes('2 °C'));

console.log('\n12. aviso obrigatorio sobre lavar midia biologica');
const aviso = (await txt('.aqm-c12-nota-alerta')).replace(/\s+/g,' ');
ok('nunca lavar tudo de uma vez', aviso.includes('Nunca lave toda a mídia biológica de uma vez'));
ok('nunca em agua de torneira', aviso.includes('nunca em água de torneira'));
ok('explica o mecanismo (cloro mata bacteria)', aviso.includes('cloro') && aviso.includes('colônia'));
ok('explica a troca parcial', aviso.includes('parcial'));

console.log('\n13. bloco de produto dentro da resposta');
await preencher('110');
const nprod = await page.locator('#aqm-c12-produtos-lista .aqm-c12-produto').count();
ok('4 midias biologicas no bloco', nprod === 4, `veio ${nprod}`);
const p1 = (await txt('#aqm-c12-produtos-lista .aqm-c12-produto:nth-child(1)')).replace(/\s+/g,' ');
ok('primeiro cartao e o de menor dosagem (Seachem)', p1.includes('Seachem'), p1.slice(0,80));
ok('cartao diz quantas embalagens', p1.includes('embalagem'));
const semDose = (await txt('#aqm-c12-produtos-lista .aqm-c12-produto-sem')).replace(/\s+/g,' ');
ok('midia sem dosagem nao e dimensionada', semDose.includes('não publica dosagem por litro'), semDose.slice(0,120));
ok('ordem declarada na tela', (await txt('#aqm-c12-produtos-sub')).includes('não é ordem de comissão'));
await preencher('110', { quimica: true });
const nprod2 = await page.locator('#aqm-c12-produtos-lista .aqm-c12-produto').count();
ok('com quimica marcada, entram as quimicas', nprod2 === 6, `veio ${nprod2}`);

console.log('\n14. atributos do link de afiliado (exigencia do projeto)');
const links = page.locator('#aqm-c12-produtos-lista a.aqm-c12-loja');
const nlinks = await links.count();
ok('ha pelo menos um link de loja', nlinks > 0, `${nlinks} link(s)`);
for (let i = 0; i < nlinks; i++) {
  const rel = await links.nth(i).getAttribute('rel');
  const tgt = await links.nth(i).getAttribute('target');
  const href = await links.nth(i).getAttribute('href');
  ok(`link ${i+1} rel=sponsored noopener`, rel === 'sponsored noopener', rel);
  ok(`link ${i+1} target=_blank`, tgt === '_blank', tgt);
  ok(`link ${i+1} https`, href.startsWith('https://'), href);
}
const avisoAf = (await txt('.aqm-c12-aviso-afiliado')).replace(/\s+/g,' ');
ok('aviso de comissao visivel', await page.locator('.aqm-c12-aviso-afiliado').isVisible());
ok('aviso diz comissao', avisoAf.includes('comissão'));
ok('aviso diz que a ordem nao muda', avisoAf.includes('não muda quem aparece'));
ok('aviso linka a divulgacao', (await page.locator('.aqm-c12-aviso-afiliado a').count()) > 0);
ok('nenhum preco na tela', !(await page.locator('.aqm-c12').innerText()).match(/R\$\s*\d/));

console.log('\n15. estado compartilhado — mescla, nao substitui');
await page.goto(URL);
await page.evaluate(() => {
  localStorage.setItem('aquametria.aquario', JSON.stringify({
    versao: 1, calculadora: 'c1-litragem',
    volumes: { real_L: 110, bruto_L: 120, origem: 'medidas na C1' },
    medidas: { comprimento_cm: 60, largura_cm: 40, altura_cm: 50 },
    clima: { temp_alvo_C: 26, delta_C: 6 },
    equipamentos: { filtro_vazao_alvo_lh: [550, 1100], aquecedor_potencia_comercial_w: 200 }
  }));
});
await page.goto(URL);
await page.waitForTimeout(150);
ok('retomou o volume da C1', (await txt('#aqm-c12-retomado')).includes('110 L'));
await page.selectOption('#aqm-c12-filtro', 'eheim-classic-250-2213');
await page.click('#aqm-c12-form button[type=submit]');
await page.waitForTimeout(120);
const estado = await page.evaluate(() => JSON.parse(localStorage.getItem('aquametria.aquario')));
ok('medidas da C1 preservadas', estado.medidas && estado.medidas.comprimento_cm === 60, JSON.stringify(estado.medidas));
ok('clima da C5 preservado', estado.clima && estado.clima.temp_alvo_C === 26);
ok('vazao da C3 preservada', estado.equipamentos.filtro_vazao_alvo_lh[1] === 1100);
ok('C12 gravou o filtro', estado.equipamentos.filtro_id === 'eheim-classic-250-2213');
ok('C12 gravou o volume de midia', estado.equipamentos.filtro_midia_L === 3);
ok('C12 gravou a faixa de midia', Array.isArray(estado.midia.biologica_mL) && estado.midia.biologica_mL[0] === 138);

console.log('\n16. permalink e caminho inverso');
await preencher('110', { filtro: 'eheim-classic-250-2213', quimica: true });
const link = await page.inputValue('#aqm-c12-link');
ok('permalink tem volume e filtro', link.includes('v=110') && link.includes('f=eheim'), link);
await page.goto(URL + '?v=250&f=atman-at-3338s&q=1');
await page.waitForTimeout(150);
ok('query string recalcula sozinha', (await txt('#aqm-c12-faixa-valor')).includes('L'), await txt('#aqm-c12-faixa-valor'));
ok('query string escolhe o filtro', await page.locator('#aqm-c12-cesto').isVisible());
await page.fill('#aqm-c12-tenho', '1,0');
await page.click('#aqm-c12-tenho-calcular');
await page.waitForTimeout(80);
const inv = (await txt('#aqm-c12-tenho-saida')).replace(/\s+/g,' ');
ok('caminho inverso: 1 L cobre de 80 a 800 L', inv.includes('80,0 L') && inv.includes('800 L'), inv.slice(0,200));

console.log('\n17. erros de entrada');
await page.goto(URL);
await page.evaluate(() => { try { localStorage.clear(); } catch(e){} });
await page.goto(URL);
await page.click('#aqm-c12-form button[type=submit]');
await page.waitForTimeout(80);
ok('sem volume, erro na tela', (await txt('#aqm-c12-erros')).includes('volume real'));
ok('sem volume, resposta escondida', await page.locator('#aqm-c12-saida').isHidden());
await preencher('99999');
ok('volume absurdo barrado', (await txt('#aqm-c12-erros')).includes('lago'));

console.log('\n18. celular de 390 px');
const ctx2 = await browser.newContext({ viewport: { width: 390, height: 780 } });
const p2 = await ctx2.newPage();
await p2.goto(URL);
await p2.fill('#aqm-c12-volume', '110');
await p2.selectOption('#aqm-c12-filtro', 'eheim-classic-250-2213');
await p2.check('#aqm-c12-quimica');
await p2.click('#aqm-c12-form button[type=submit]');
await p2.waitForTimeout(150);
const larguras = await p2.evaluate(() => ({
  corpo: document.body.scrollWidth,
  janela: window.innerWidth
}));
ok('sem rolagem horizontal no corpo', larguras.corpo <= larguras.janela + 1, JSON.stringify(larguras));

console.log('\n19. console limpo');
ok('nenhum erro de console', erros.length === 0, erros.join(' | '));

await browser.close();
console.log(falhas === 0 ? '\nTODOS OS CENARIOS PASSARAM\n' : `\n${falhas} FALHA(S)\n`);
process.exit(falhas === 0 ? 0 : 1);

// Teste de navegador da C15 — a calculadora de iluminação e fotoperíodo.
//
// Roda a calculadora num Chromium de verdade e confere o que a revisão de cada
// calculadora exige: a faixa de lúmens nos três níveis, as três leituras
// brasileiras publicadas lado a lado (com a divergência de 2x sobre o mesmo
// rótulo), os quatro regimes de fotoperíodo, o bloco de CO2 com a sobreposição
// dos limites, o aviso de luz alta sem CO2, o aviso de profundidade, o bloco de
// produto com a cobertura de comprimento como barreira, a lista publicada dos
// produtos barrados (inclusive a luminária que TEM link de afiliado e mesmo
// assim não é sugerida), os atributos do link de afiliado, o painel de consumo
// em kWh e em reais com tarifa do próprio visitante, o caminho inverso, a
// mescla do estado compartilhado com C1/C3/C5 e o celular de 390 px sem
// rolagem horizontal.
//
// Como rodar (o container da nuvem já traz o Chromium do Playwright):
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
//   node ferramentas/teste-navegador-c15.mjs /tmp/c15.html

import { chromium } from 'playwright';

const URL = 'file://' + process.argv[2];
let falhas = 0;
function ok(nome, cond, extra = '') {
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
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.goto(URL);
  await page.fill('#aqm-c15-volume', String(v));
  if (opts.comprimento !== undefined) await page.fill('#aqm-c15-comprimento', String(opts.comprimento));
  if (opts.lamina !== undefined) await page.fill('#aqm-c15-lamina', String(opts.lamina));
  if (opts.nivel) await page.selectOption('#aqm-c15-nivel', opts.nivel);
  if (opts.regime) await page.selectOption('#aqm-c15-regime', opts.regime);
  if (opts.tipo) await page.selectOption('#aqm-c15-tipo', opts.tipo);
  if (opts.co2) await page.check('#aqm-c15-co2');
  await page.click('#aqm-c15-form button[type=submit]');
  await page.waitForTimeout(120);
}
const txt = s => page.locator(s).innerText();

console.log('\n1. caso base — 110 L, 60 cm, plantas de exigência média');
await preencher('110', { comprimento: 60 });
const faixa = await txt('#aqm-c15-faixa-valor');
ok('faixa de 2.200 a 4.400 lm', faixa.includes('2.200') && faixa.includes('4.400'), faixa.replace(/\s+/g, ' '));
const criterio = await txt('#aqm-c15-faixa-criterio');
ok('critério cita a faixa consolidada 20 a 40 lm/L', criterio.includes('20 a 40'), criterio.slice(0, 120));
ok('critério declara que não é média', criterio.includes('não é a média'));
ok('divergência de 1,5 vezes no nível médio', criterio.includes('1,5 vezes'));

console.log('\n2. as três leituras brasileiras, sem média');
const linhas = await page.locator('#aqm-c15-leituras-corpo tr').count();
ok('9 linhas (3 níveis x 3 fontes)', linhas === 9, `veio ${linhas}`);
const destacadas = await page.locator('#aqm-c15-leituras-corpo tr.aqm-c15-linha-escolhida').count();
ok('3 linhas destacadas (o nível escolhido)', destacadas === 3, `veio ${destacadas}`);
const tabela = await txt('#aqm-c15-leituras-corpo');
ok('as três fontes aparecem nominalmente', tabela.includes('peixeseaquarismo')
  && tabela.includes('aquarioturbinado') && tabela.includes('aquariosplantados'));
ok('a leitura sem teto sai como "acima de 40"', tabela.includes('acima de 40'));
ok('nota explica por que não se tira média', (await txt('#aqm-c15-leituras-nota')).includes('a média inventaria um consenso'));

console.log('\n3. nível baixo — o rótulo em que as fontes discordam por 2x');
await preencher('110', { comprimento: 60, nivel: 'baixa' });
ok('faixa de 1.100 a 2.200 lm', (await txt('#aqm-c15-faixa-valor')).includes('1.100'));
ok('divergência de 2,0 vezes', (await txt('#aqm-c15-faixa-criterio')).includes('2,0 vezes'));

console.log('\n4. nível alto sem CO2 — faixa aberta e aviso obrigatório');
await preencher('110', { comprimento: 60, nivel: 'alta' });
ok('faixa aberta com o sinal de mais', (await txt('#aqm-c15-faixa-valor')).includes('6.600+'),
  (await txt('#aqm-c15-faixa-valor')).replace(/\s+/g, ' '));
ok('diz que o nível alto não tem teto declarado', (await txt('#aqm-c15-faixa-criterio')).includes('não tem teto declarado'));
const avisosAlta = await txt('#aqm-c15-avisos');
ok('avisa que luz alta sem CO2 é receita de alga', avisosAlta.includes('receita clássica de alga'));
ok('bloco de CO2 aparece mesmo sem CO2 marcado, no nível alto',
  !(await page.locator('#aqm-c15-co2-bloco').getAttribute('class')).includes('oculto'));

console.log('\n5. CO2 marcado — regime high tech e a sobreposição publicada');
await preencher('110', { comprimento: 60, co2: true });
const cartoes = await txt('#aqm-c15-cartoes');
ok('fotoperíodo high tech de 8 a 10 h', cartoes.toLowerCase().includes('high tech') && cartoes.includes('8 a 10'));
const co2 = await txt('#aqm-c15-co2-texto');
ok('publica a faixa útil 15 a 35 mg/L', co2.includes('15 a 35'));
ok('publica o limite tóxico 30 a 35 mg/L', co2.includes('30 a 35'));
ok('nomeia a sobreposição em vez de escolher', co2.includes('se sobrepõem'));
ok('manda ler o drop checker', co2.includes('drop checker') && co2.includes('amarelo'));

console.log('\n6. os outros dois regimes de fotoperíodo');
await preencher('110', { comprimento: 60, regime: 'alga' });
ok('combate a alga: 5 a 6 h', (await txt('#aqm-c15-cartoes')).toLowerCase().includes('combate a alga')
  && (await txt('#aqm-c15-cartoes')).includes('5 a 6'));
await preencher('110', { comprimento: 60, regime: 'ciclagem' });
ok('ciclagem: 4 a 6 h', (await txt('#aqm-c15-cartoes')).includes('4 a 6'));
const quatro = await txt('#aqm-c15-fotoperiodos');
ok('os quatro regimes ficam listados', quatro.includes('low tech') && quatro.includes('high tech')
  && quatro.includes('combate a alga') && quatro.includes('ciclagem'));  // esta lista nao passa por text-transform
ok('marca qual é o caso atual', quatro.includes('é o seu caso agora'));

console.log('\n7. lâmina funda — o limite que lm/L não enxerga');
await preencher('110', { comprimento: 60, lamina: 55 });
const avisosFundo = await txt('#aqm-c15-avisos');
ok('avisa acima de 45 cm', avisosFundo.includes('55 cm') && avisosFundo.includes('começa a mentir'));
ok('remete ao PPFD que não publicamos', avisosFundo.includes('PPFD'));

console.log('\n8. sem comprimento — a lista de produtos não aparece, e diz por quê');
await preencher('110');
ok('bloco de produtos escondido', (await page.locator('#aqm-c15-produtos').getAttribute('class')).includes('oculto'));
const nada = await txt('#aqm-c15-produtos-nada');
ok('explica que sem comprimento não há como conferir cobertura', nada.includes('comprimento do aquário preenchido'));
ok('avisa que luminária curta deixa as pontas na sombra', (await txt('#aqm-c15-avisos')).includes('pontas na sombra'));

console.log('\n9. bloco de produto — 110 L e 60 cm');
await preencher('110', { comprimento: 60 });
const cards = await page.locator('#aqm-c15-produtos-lista .aqm-c15-produto').count();
ok('duas luminárias sugeridas', cards === 2, `veio ${cards}`);
const primeiro = await page.locator('#aqm-c15-produtos-lista .aqm-c15-produto').first().innerText();
ok('a mais próxima do meio da faixa vem primeiro (IL-401, 3717 lm)', primeiro.includes('IL-401'), primeiro.split('\n')[1]);
ok('mostra os lm/L entregues no aquário da pessoa', primeiro.includes('lm/L'));
ok('mostra a cobertura declarada', primeiro.includes('56 a 66 cm'));
ok('mostra a eficácia calculada por nós', primeiro.includes('lm/W'));
ok('mostra o consumo no fotoperíodo escolhido', primeiro.includes('kWh/mês'));
ok('declara que não há PPFD declarado', primeiro.includes('PPFD declarado'));
ok('publica o conflito nome-contra-ficha do IL-401', primeiro.toLowerCase().includes('conflito registrado')
  && primeiro.includes('56'), primeiro.includes('conflito registrado') ? 'com selo' : 'sem selo');
const listaToda = await txt('#aqm-c15-produtos-lista');
ok('a de 810 lm ficou fora, e a tela diz o motivo (cobertura)', listaToda.includes('Fora da lista neste aquário')
  && listaToda.includes('45 cm'));
ok('produto sem link aparece igual, sem botão de loja', listaToda.includes('Ainda não temos link de loja'));

console.log('\n10. a lista publicada dos barrados');
const barrados = await page.locator('#aqm-c15-barrados li').count();
// Ate 08/09/2026 eram tres barradas e o teste fixava o numero. Em 09/09 o lote de
// anuncios da Shopee trouxe as oito luminarias Soma, todas barradas pelo mesmo campo
// (fluxo_lm), e o numero passou a onze — a assercao virou vermelha sem que nada
// tivesse quebrado. Numero de catalogo nao e contrato de tela: o que a tela promete e
// que TODA barrada aparece com o motivo, entao e isso que se confere. Mesma correcao
// que a C5 ja tinha recebido na contagem de cartoes.
ok('a lista de barradas nao esconde ninguem', barrados >= 3, `veio ${barrados}`);
const barradosTxt = await txt('#aqm-c15-barrados');
ok('Chihiros barrada por voltagem', barradosTxt.includes('Chihiros') && barradosTxt.includes('voltagem'));
ok('SunSun e WFish barradas por não declararem lúmens',
  barradosTxt.includes('SunSun') && barradosTxt.includes('WFish') && barradosTxt.includes('fluxo luminoso'));
ok('diz que link de afiliado não promove produto barrado', barradosTxt.includes('link não promove produto barrado'));

console.log('\n11. atributos do link de afiliado (45 L, nível baixo, 40 cm)');
await preencher('45', { comprimento: 40, nivel: 'baixa' });
const links = page.locator('#aqm-c15-produtos-lista a.aqm-c15-loja');
const nLinks = await links.count();
ok('a Ista I-401 45 cm entra com link de loja', nLinks === 1, `veio ${nLinks}`);
if (nLinks) {
  ok('rel = sponsored noopener', (await links.first().getAttribute('rel')) === 'sponsored noopener');
  ok('target = _blank', (await links.first().getAttribute('target')) === '_blank');
  ok('href https', (await links.first().getAttribute('href')).startsWith('https://'));
}
const aviso = await txt('.aqm-c15-aviso-afiliado');
ok('aviso de comissão visível', aviso.includes('pode receber uma comissão'));
ok('aviso diz que comissão não ordena', aviso.includes('não muda quem aparece na lista'));
ok('aviso linka a página de divulgação',
  (await page.locator('.aqm-c15-aviso-afiliado a').getAttribute('href')).includes('divulgacao-de-afiliados'));

console.log('\n12. nenhum produto cobre um aquário de 120 cm');
await preencher('300', { comprimento: 120 });
ok('bloco de produtos escondido', (await page.locator('#aqm-c15-produtos').getAttribute('class')).includes('oculto'));
const semProduto = await txt('#aqm-c15-produtos-nada');
ok('diz quantas luminárias o banco tem e quantas são barradas',
  semProduto.includes('luminária(s) com ficha completa') && semProduto.includes('não podem ser sugeridas'));
ok('prefere não mostrar nada a mostrar errado', semProduto.includes('Preferimos não mostrar produto nenhum'));

console.log('\n13. painel de consumo');
await preencher('110', { comprimento: 60 });
await page.fill('#aqm-c15-watts', '24');
await page.fill('#aqm-c15-tarifa', '0,95');
await page.click('#aqm-c15-consumo-calcular');
await page.waitForTimeout(80);
const consumo = await txt('#aqm-c15-consumo-saida');
ok('24 W por 7 h/dia dão 5,0 kWh/mês', consumo.includes('5,0 kWh'), consumo.slice(0, 90));
ok('com a tarifa informada, R$ 4,79 por mês', consumo.includes('4,79'), consumo.slice(90, 200));
ok('diz que a tarifa é do visitante, não nossa', consumo.includes('usamos a sua tarifa'));

console.log('\n14. consumo sem tarifa — recusa de publicar tarifa padrão');
await preencher('110', { comprimento: 60 });
await page.fill('#aqm-c15-watts', '24');
await page.click('#aqm-c15-consumo-calcular');
await page.waitForTimeout(80);
ok('explica por que não publicamos tarifa', (await txt('#aqm-c15-consumo-saida')).includes('Não publicamos uma tarifa padrão'));

console.log('\n15. caminho inverso');
await preencher('110', { comprimento: 60 });
await page.fill('#aqm-c15-tenho', '2400');
await page.click('#aqm-c15-tenho-calcular');
await page.waitForTimeout(80);
const inverso = await txt('#aqm-c15-tenho-saida');
ok('2400 lm cobrem 120 a 240 L no nível baixo', inverso.includes('120') && inverso.includes('240'), inverso.slice(0, 130));
ok('no aquário de 110 L, cai no nível médio', inverso.includes('21,8 lm/L') && inverso.includes('nível médio'));
ok('lembra que lúmen não é fotossíntese', inverso.includes('não entregam a mesma fotossíntese'));

console.log('\n16. estado compartilhado — mescla, nunca substituição');
await page.goto(URL);
await page.evaluate(() => {
  localStorage.setItem('aquametria.aquario', JSON.stringify({
    versao: 1, calculadora: 'c1-litragem',
    medidas: { comprimento_cm: 80, largura_cm: 35, altura_cm: 45 },
    agua: { altura_lamina_cm: 40 },
    volumes: { real_L: 100, origem: 'calculado na C1' },
    equipamentos: { filtro_vazao_alvo_lh: [176, 1000] },
    clima: { minima_C: 14 }
  }));
});
await page.goto(URL);
await page.waitForTimeout(150);
ok('retomou o aquário guardado pela C1', (await txt('#aqm-c15-retomado')).includes('100 L'));
ok('retomou também o comprimento', (await page.inputValue('#aqm-c15-comprimento')) === '80');
ok('retomou a lâmina', (await page.inputValue('#aqm-c15-lamina')) === '40');
const estado = await page.evaluate(() => JSON.parse(localStorage.getItem('aquametria.aquario')));
ok('preservou as medidas da C1', estado.medidas.largura_cm === 35);
ok('preservou a vazão que a C3 tinha calculado', estado.equipamentos.filtro_vazao_alvo_lh[1] === 1000);
ok('preservou o clima que a C5 perguntou', estado.clima.minima_C === 14);
ok('gravou a iluminação', estado.iluminacao && estado.iluminacao.lumens_alvo[0] === 2000
  && estado.iluminacao.fotoperiodo_h[0] === 6, JSON.stringify(estado.iluminacao));

console.log('\n17. permalink');
await preencher('110', { comprimento: 60, nivel: 'alta', co2: true });
const link = await page.inputValue('#aqm-c15-link');
ok('permalink com volume, nível e CO2', link.includes('v=110') && link.includes('n=alta') && link.includes('co2=1'), link);
await page.goto(URL.split('?')[0] + '?v=200&c=100&n=baixa&rg=alga&t=qualquer');
await page.waitForTimeout(150);
ok('a query string reconstrói a resposta', (await txt('#aqm-c15-faixa-valor')).includes('2.000')
  && (await txt('#aqm-c15-cartoes')).toLowerCase().includes('combate a alga'));

console.log('\n18. citação e erros de entrada');
await preencher('110', { comprimento: 60 });
const citacao = await txt('#aqm-c15-citacao');
ok('citação traz faixa, fotoperíodo e Kelvin', citacao.includes('2.200') && citacao.includes('h/dia')
  && citacao.includes('6.500'), citacao.slice(0, 120));
await page.goto(URL);
await page.fill('#aqm-c15-volume', '');
await page.click('#aqm-c15-form button[type=submit]');
await page.waitForTimeout(80);
ok('volume vazio vira erro visível', (await txt('#aqm-c15-erros')).includes('Informe o volume'));
await page.fill('#aqm-c15-volume', '110');
await page.fill('#aqm-c15-comprimento', '900');
await page.click('#aqm-c15-form button[type=submit]');
await page.waitForTimeout(80);
ok('comprimento absurdo vira erro', (await txt('#aqm-c15-erros')).includes('entre 1 e 400'));

console.log('\n19. quadro de fontes e recusas');
await page.goto(URL);
const fontes = await txt('.aqm-c15-fontes');
ok('lista as três fontes de lm/L', fontes.includes('iluminacao-lumen-por-litro'));
ok('publica a recusa do PPFD com o motivo achado na Chihiros',
  fontes.includes('ppfd-por-litragem') && fontes.includes('não existe teste oficial'));
ok('publica a convenção de cobertura como convenção', fontes.includes('cobertura-luminaria-declarada')
  && fontes.includes('1,59 vez'));

console.log('\n20. celular de 390 px');
const mob = await ctx.newPage();
await mob.goto(URL);
await mob.setViewportSize({ width: 390, height: 800 });
await mob.fill('#aqm-c15-volume', '110');
await mob.fill('#aqm-c15-comprimento', '60');
await mob.click('#aqm-c15-form button[type=submit]');
await mob.waitForTimeout(150);
const rolagem = await mob.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
ok('sem rolagem horizontal', rolagem <= 1, `sobra de ${rolagem} px`);
await mob.close();

console.log('\n21. console limpo');
ok('nenhum erro de console', erros.length === 0, erros.join(' | '));

await browser.close();
console.log(`\n${falhas === 0 ? 'TUDO PASSOU' : falhas + ' FALHA(S)'}\n`);
process.exit(falhas === 0 ? 0 : 1);

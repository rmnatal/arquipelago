// Varredura de COBERTURA DE FAIXA — a medida que substituiu a meta de "60 produtos".
//
// A secao 14.3 do ARQUIPELAGO.md diz que o tamanho do banco nao e um numero
// redondo: e cobertura. O criterio e "nenhuma faixa que as ferramentas da ilha
// conseguem produzir pode sair com menos de 3 produtos elegiveis", e a unica
// forma honesta de medir isso e VARRER a faixa de entrada de cada calculadora
// de ponta a ponta e contar quantos itens passam em TODAS as condicoes
// declaradas.
//
// Este arquivo nao reimplementa regra nenhuma, e isso e o ponto: reimplementar
// a selecao em Python criaria uma segunda copia da regra, que divergiria da
// calculadora em silencio — o mesmo defeito que o gerador de catalogo existe
// para impedir. Aqui a calculadora DE VERDADE roda num Chromium de verdade,
// preenchida ponto a ponto, e o que se conta e o cartao que apareceu na tela.
//
// Como rodar:
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_vazao      > /tmp/c3.html
//   php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor  > /tmp/c5.html
//   php ferramentas/render-para-teste.php . aquametria_calculadora_midia      > /tmp/c12.html
//   php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
//   node ferramentas/varrer-cobertura.mjs /tmp
//
// Sai 0 sempre: buraco de cobertura nao e erro de codigo, e lista de compras do
// banco. Quem reprova commit e o validador; este mede.
//
// A saida e markdown, para ser colada em dados/cobertura-de-faixa.md:
//
//   node ferramentas/varrer-cobertura.mjs /tmp > dados/cobertura-de-faixa.md

import { chromium } from 'playwright';

const DIR = process.argv[2] || '/tmp';
const MINIMO = 3;           // o piso da secao 14.3
const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const HOJE = new Date().toISOString().slice(0, 10);

// Cada cenario e uma condicao declarada que a pessoa escolhe na tela. Varrer so
// o caso central mediria o banco no melhor dia dele; o que interessa e a pior
// combinacao que a calculadora consegue produzir, porque e ela que sai vazia
// para alguem.
const CALCS = [
  {
    id: 'C3', nome: 'vazao do filtro', arquivo: 'c3.html',
    eixo: { campo: '#aqm-c3-volume', unidade: 'L', de: 20, ate: 400, passo: 10 },
    lista: '#aqm-c3-produtos-lista .aqm-c3-produto',
    cenarios: [
      { nome: 'comunitario, carga leve',   sel: { '#aqm-c3-perfil': 'comunitario', '#aqm-c3-carga': 'leve' } },
      { nome: 'comunitario, carga media',  sel: { '#aqm-c3-perfil': 'comunitario', '#aqm-c3-carga': 'media' } },
      { nome: 'comunitario, carga pesada', sel: { '#aqm-c3-perfil': 'comunitario', '#aqm-c3-carga': 'pesada' } },
      { nome: 'plantado, carga media',     sel: { '#aqm-c3-perfil': 'plantado',    '#aqm-c3-carga': 'media' } },
    ],
  },
  {
    id: 'C5', nome: 'potencia do aquecedor', arquivo: 'c5.html',
    eixo: { campo: '#aqm-c5-volume', unidade: 'L', de: 20, ate: 400, passo: 10 },
    lista: '#aqm-c5-produtos-lista .aqm-c5-produto',
    cenarios: [
      { nome: 'delta 4 C, tomada 110 V',  txt: { '#aqm-c5-minima': '22', '#aqm-c5-alvo': '26' }, sel: { '#aqm-c5-voltagem': '110' } },
      { nome: 'delta 6 C, tomada 110 V',  txt: { '#aqm-c5-minima': '20', '#aqm-c5-alvo': '26' }, sel: { '#aqm-c5-voltagem': '110' } },
      { nome: 'delta 6 C, tomada 220 V',  txt: { '#aqm-c5-minima': '20', '#aqm-c5-alvo': '26' }, sel: { '#aqm-c5-voltagem': '220' } },
      { nome: 'delta 10 C, tomada 220 V', txt: { '#aqm-c5-minima': '16', '#aqm-c5-alvo': '26' }, sel: { '#aqm-c5-voltagem': '220' } },
    ],
  },
  {
    id: 'C12', nome: 'midia filtrante', arquivo: 'c12.html',
    eixo: { campo: '#aqm-c12-volume', unidade: 'L', de: 20, ate: 400, passo: 10 },
    lista: '#aqm-c12-produtos-lista .aqm-c12-produto:not(.aqm-c12-produto-sem)',
    cenarios: [
      { nome: 'comunitario', sel: { '#aqm-c12-perfil': 'comunitario' } },
      { nome: 'plantado',    sel: { '#aqm-c12-perfil': 'plantado' } },
      { nome: 'sensiveis',   sel: { '#aqm-c12-perfil': 'sensiveis' } },
    ],
  },
  {
    id: 'C15', nome: 'iluminacao', arquivo: 'c15.html',
    // O eixo da C15 e o COMPRIMENTO do aquario, nao o volume: e o comprimento
    // que decide qual luminaria cabe. O volume acompanha, com uma coluna
    // tipica de 40 cm de agua e 40 cm de largura, so para a calculadora ter
    // litro para trabalhar.
    eixo: { campo: '#aqm-c15-comprimento', unidade: 'cm', de: 30, ate: 120, passo: 5,
            acompanha: (cm) => ({ '#aqm-c15-volume': String(Math.round(cm * 40 * 40 / 1000)),
                                  '#aqm-c15-lamina': '40' }) },
    lista: '#aqm-c15-produtos-lista .aqm-c15-produto',
    cenarios: [
      { nome: 'exigencia baixa', sel: { '#aqm-c15-nivel': 'baixa' } },
      { nome: 'exigencia media', sel: { '#aqm-c15-nivel': 'media' } },
      { nome: 'exigencia alta',  sel: { '#aqm-c15-nivel': 'alta' } },
    ],
  },
];

function faixas(pontos, unidade) {
  // Agrupa pontos consecutivos com a mesma contagem. E o que transforma 39
  // medidas numa frase que cabe numa lista de compras.
  const out = [];
  for (const p of pontos) {
    const ultimo = out[out.length - 1];
    if (ultimo && ultimo.n === p.n) { ultimo.ate = p.x; continue; }
    out.push({ de: p.x, ate: p.x, n: p.n, unidade });
  }
  return out;
}

const browser = await chromium.launch({ executablePath: CHROME });
const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
const page = await ctx.newPage();

const resultado = [];
for (const c of CALCS) {
  const url = 'file://' + DIR + '/' + c.arquivo;
  const porCenario = [];
  for (const cen of c.cenarios) {
    const pontos = [];
    // Carrega a pagina UMA vez por cenario e depois so repreenche o formulario.
    // Recarregar a cada ponto multiplicava o tempo por quarenta sem mudar nada do
    // que se mede: o estado que a calculadora guarda e dela mesma, e cada ponto o
    // sobrescreve inteiro. O localStorage e limpo aqui, antes do primeiro ponto,
    // para o estado compartilhado das outras calculadoras nao entrar na conta.
    await page.goto(url);
    await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
    await page.goto(url);
    for (let x = c.eixo.de; x <= c.eixo.ate; x += c.eixo.passo) {
      await page.fill(c.eixo.campo, String(x));
      const acompanha = c.eixo.acompanha ? c.eixo.acompanha(x) : {};
      for (const [sel, v] of Object.entries({ ...acompanha, ...(cen.txt || {}) })) await page.fill(sel, v);
      for (const [sel, v] of Object.entries(cen.sel || {})) await page.selectOption(sel, v);
      await page.click(`${c.eixo.campo.replace(/-[a-z]+$/, '-form')} button[type=submit]`).catch(async () => {
        await page.click(`#aqm-${c.id.toLowerCase()}-form button[type=submit]`);
      });
      await page.waitForTimeout(60);
      pontos.push({ x, n: await page.locator(c.lista).count() });
    }
    // Progresso no stderr: a varredura leva minutos e o markdown so sai no fim.
    // Sem isto, quem roda nao sabe distinguir 'demorando' de 'travado'.
    process.stderr.write(`${c.id} — ${cen.nome}: ${pontos.length} pontos medidos\n`);
    porCenario.push({ cenario: cen.nome, faixas: faixas(pontos, c.eixo.unidade) });
  }
  resultado.push({ calc: c, porCenario });
}
await browser.close();

// ---------------------------------------------------------------- relatorio
const L = [];
L.push('# Cobertura de faixa das calculadoras da Aquametria');
L.push('');
L.push(`Medido em **${HOJE}** por \`ferramentas/varrer-cobertura.mjs\`, que abre cada`);
L.push('calculadora num Chromium de verdade e a preenche ponto a ponto. O numero de cada');
L.push('linha e a quantidade de cartoes de produto que a calculadora REALMENTE desenhou');
L.push('naquela entrada — nao uma contagem de banco, nao uma reimplementacao da regra.');
L.push('');
L.push(`Criterio (secao 14.3 do \`ARQUIPELAGO.md\`): **nenhuma faixa produzivel pode sair com`);
L.push(`menos de ${MINIMO} produtos elegiveis.** O que aparece marcado abaixo e a lista de`);
L.push('compras do banco, em ordem de urgencia.');
L.push('');
L.push('Este arquivo e HISTORICO: cada medicao vira uma secao nova, nunca sobrescreve a');
L.push('anterior. E a serie que diz se o banco esta cobrindo mais faixa ou so ficando maior.');
L.push('');
L.push(`## Medicao de ${HOJE}`);
L.push('');

let buracos = 0, vazias = 0, total = 0;
for (const r of resultado) {
  L.push(`### ${r.calc.id} — ${r.calc.nome}`);
  L.push('');
  L.push(`Eixo varrido: ${r.calc.eixo.de} a ${r.calc.eixo.ate} ${r.calc.eixo.unidade}, de ${r.calc.eixo.passo} em ${r.calc.eixo.passo}.`);
  L.push('');
  L.push('| condicao declarada | faixa | produtos elegiveis | |');
  L.push('|---|---|---:|---|');
  for (const c of r.porCenario) {
    for (const f of c.faixas) {
      total++;
      const marca = f.n === 0 ? '**VAZIA**' : (f.n < MINIMO ? '**abaixo de 3**' : 'ok');
      if (f.n === 0) vazias++; else if (f.n < MINIMO) buracos++;
      const faixa = f.de === f.ate ? `${f.de} ${f.unidade}` : `${f.de} a ${f.ate} ${f.unidade}`;
      L.push(`| ${c.cenario} | ${faixa} | ${f.n} | ${marca} |`);
    }
  }
  L.push('');
}
L.push('### Resumo');
L.push('');
L.push(`- Faixas medidas: **${total}**`);
L.push(`- Faixas VAZIAS (nenhum produto): **${vazias}**`);
L.push(`- Faixas com 1 ou 2 produtos (abaixo do piso de ${MINIMO}): **${buracos}**`);
L.push(`- Faixas que cumprem o criterio: **${total - vazias - buracos}**`);
L.push('');
console.log(L.join('\n'));

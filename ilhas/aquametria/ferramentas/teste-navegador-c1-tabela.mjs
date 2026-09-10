// A tabela pre-renderizada da C1 contra a propria C1, num Chromium de verdade.
//
// O teste-navegador-visibilidade-ia.mjs prova que a tabela EXISTE no HTML
// servido e que um numero ancora aparece nela. Isso nao prova o que mais
// importa: que a tabela e a calculadora logo abaixo dela digam a MESMA coisa
// para a MESMA entrada. Tabela servida que arredonda diferente do script faz a
// pagina se contradizer sozinha, e ninguem percebe pela tela — o leitor ve dois
// numeros em lugares diferentes e acredita nos dois.
//
// Como este arquivo evita a assercao que vence sozinha (quatro delas venceram
// em duas execucoes seguidas na ilha, todas do mesmo tipo): ele NAO guarda
// nenhum numero esperado. As entradas saem da propria tabela, lidas da coluna
// do aquario; os valores esperados saem da propria tabela; e o que se compara e
// o que a calculadora devolve quando recebe essas entradas. Mudar as medidas dos
// exemplos, a borda livre ou o arredondamento nao reprova nada — o teste
// continua afirmando a PROMESSA ("a tabela nao contradiz a calculadora"), nunca
// o ESTADO ("o aquario de 80 cm da 109 L").
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_litragem > /tmp/c1.html
//   node ferramentas/teste-navegador-c1-tabela.mjs /tmp/c1.html

import { chromium } from 'playwright';

const ARQUIVO = process.argv[2] || '/tmp/c1.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

let falhas = 0;
function ok(m, extra) { console.log('  ok    ' + m + (extra ? ' — ' + extra : '')); }
function ruim(m, extra) { falhas++; console.log('  FALHA ' + m + (extra ? ' — ' + extra : '')); }
function conferir(cond, m, extra) { cond ? ok(m, extra) : ruim(m, extra); }

// A calculadora imprime "128" e um <span> com a unidade. Interessa o numero
// como texto, com a virgula decimal brasileira preservada.
function soNumero(t) {
  const m = String(t).replace(/\s+/g, ' ').match(/-?[\d.]+(?:,\d+)?/);
  return m ? m[0] : null;
}

const navegador = await chromium.launch({ executablePath: CHROME });
const ctx = await navegador.newContext();
const pagina = await ctx.newPage();

const erros = [];
pagina.on('pageerror', e => erros.push('pageerror: ' + e.message));
pagina.on('console', m => { if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|BLOCKED)/.test(m.text())) { erros.push(m.text()); } });

await pagina.goto('file://' + ARQUIVO);

console.log('C1 — a tabela servida contra a calculadora (JavaScript LIGADO)');

// As linhas da tabela, lidas do HTML SERVIDO. A primeira celula carrega as
// medidas e a espessura que geraram a linha; as tres seguintes, os volumes.
const linhas = await pagina.$$eval('.aqm-c1-exemplos tr', trs => trs.slice(1).map(tr => {
  const td = Array.from(tr.querySelectorAll('td'));
  return td.map(c => c.innerText.replace(/\s+/g, ' ').trim());
}));

conferir(linhas.length >= 6, 'a tabela servida tem pelo menos seis linhas de exemplo', linhas.length + ' linhas');

for (const celulas of linhas) {
  // "80 cm 80 × 40 × 40 cm por fora, vidro de 8 mm"
  const medidas = celulas[0].match(/(\d+(?:,\d+)?) ?× ?(\d+(?:,\d+)?) ?× ?(\d+(?:,\d+)?) cm/);
  const vidro = celulas[0].match(/vidro de (\d+(?:,\d+)?) mm/);

  if (!medidas || !vidro) {
    ruim('a coluna do aquario declara as medidas e a espessura que geraram a linha', celulas[0]);
    continue;
  }

  const entrada = [medidas[1], medidas[2], medidas[3], vidro[1]];
  const rotulo = entrada.slice(0, 3).join(' × ') + ' cm, vidro de ' + entrada[3] + ' mm';

  await pagina.fill('#aqm-c1-c', entrada[0]);
  await pagina.fill('#aqm-c1-l', entrada[1]);
  await pagina.fill('#aqm-c1-a', entrada[2]);
  await pagina.fill('#aqm-c1-e', entrada[3]);
  // A tabela e calculada com a lamina no valor inicial e sem substrato nem
  // rochas, e diz isso no proprio texto. Os campos vao vazios de proposito: e
  // esse o ramo do calcular() que a tabela representa.
  await pagina.fill('#aqm-c1-lamina', '');
  await pagina.fill('#aqm-c1-substrato', '');
  await pagina.fill('#aqm-c1-rochas', '');
  await pagina.click('#aqm-c1-form button[type=submit]');

  const medido = {
    bruto: soNumero(await pagina.innerText('#aqm-c1-bruto')),
    interno: soNumero(await pagina.innerText('#aqm-c1-interno')),
    real: soNumero(await pagina.innerText('#aqm-c1-real')),
  };

  const servido = {
    bruto: soNumero(celulas[1]),
    interno: soNumero(celulas[2]),
    real: soNumero(celulas[3]),
  };

  for (const chave of ['bruto', 'interno', 'real']) {
    conferir(servido[chave] !== null && servido[chave] === medido[chave],
      'o volume ' + chave + ' da tabela e o mesmo que a calculadora devolve (' + rotulo + ')',
      'tabela ' + servido[chave] + ' · calculadora ' + medido[chave]);
  }

  // A lamina e a unica escolha editorial da pagina, e a tabela promete usar o
  // valor inicial. Se um dia o script mudar a borda livre e a tabela nao, e aqui
  // que a divergencia aparece.
  const laminaServida = (celulas[3].match(/l[âa]mina de (\d+(?:,\d+)?) cm/i) || [])[1] || null;
  const criterio = (await pagina.innerText('#aqm-c1-real-criterio')).replace(/\s+/g, ' ');
  const laminaMedida = (criterio.match(/L[âa]mina de (\d+(?:,\d+)?) cm/i) || [])[1] || null;
  conferir(laminaServida !== null && laminaServida === laminaMedida,
    'a lamina que a tabela declara e a que a calculadora usou (' + rotulo + ')',
    'tabela ' + laminaServida + ' · calculadora ' + laminaMedida);
}

// A resposta direta do topo cita um caso concreto. Ela nao pode ser a unica
// parte da pagina que ninguem confere: todo numero seguido de " L" que ela
// afirma tem de existir tambem na tabela, que por sua vez acabou de ser
// conferida contra a calculadora.
// Comparacao por TOKEN, nunca por includes(): "1 L" e substring de "261 L", e um
// teste que passa por coincidencia de substring nao esta conferindo nada.
const VOLUME = /(?:^|[^\d.,])(\d+(?:,\d+)?) L(?![a-zà-ú])/g;
function volumes(t) { return new Set(Array.from(t.matchAll(VOLUME), m => m[1])); }

const direta = (await pagina.innerText('.aqm-c1-direta')).replace(/\s+/g, ' ');
const tabelaTexto = (await pagina.innerText('.aqm-c1-exemplos')).replace(/\s+/g, ' ');
const naTabela = volumes(tabelaTexto);
const litrosNaDireta = Array.from(volumes(direta));
const orfaos = litrosNaDireta.filter(v => !naTabela.has(v));
conferir(litrosNaDireta.length > 0, 'a resposta direta afirma volumes em litros',
  litrosNaDireta.map(v => v + ' L').join(', '));
conferir(orfaos.length === 0,
  'todo volume citado na resposta direta existe na tabela ja conferida',
  orfaos.length ? 'sem lastro: ' + orfaos.map(v => v + ' L').join(', ')
    : litrosNaDireta.length + ' volumes com lastro');

// Erro de resource bloqueado pelo egresso (fonte do Google) nao conta: e ruido
// do ambiente, nao da pagina.
conferir(erros.length === 0, 'o console fica sem erro de pagina', erros.join(' || ') || 'limpo');

await ctx.close();
await navegador.close();

console.log('');
if (falhas) { console.log('=== ' + falhas + ' FALHA(S) ==='); process.exit(1); }
console.log('=== tudo passou ===');

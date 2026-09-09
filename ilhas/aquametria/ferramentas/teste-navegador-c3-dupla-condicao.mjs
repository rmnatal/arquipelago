// O teste do defeito que o Raphael viu na C3 no ar em 09/09/2026, com o caso
// dele: aquario de 189,6 L, plantado, carga media.
//
// O que estava errado: a elegibilidade olhava so a VAZAO. O primeiro item
// recomendado era o Atman HF-0600 (650 L/h, dentro da faixa) e o proprio cartao
// dele escrevia que o fabricante declara o modelo para ate 150 L e que "a
// declaracao do fabricante nao cobre o seu caso". A pagina recomendava em
// PRIMEIRO lugar um filtro que ela mesma dizia nao servir.
//
// Este arquivo executa o calculo num Chromium de verdade e mede as duas regras
// novas (V22 do esquema, e o desempate da V16):
//
//   1. nenhum recomendado tem volume declarado menor que o aquario;
//   2. o Atman HF-0600 NAO esta entre os recomendados;
//   3. ele esta na secao separada, rotulada, e ela vem DEPOIS no HTML;
//   4. o primeiro recomendado tem link de loja, quando existe um elegivel com
//      link no mesmo degrau de adequacao;
//   5. todo link do bloco continua sponsored + noopener + aba nova.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_vazao > /tmp/c3.html
//   node ferramentas/teste-navegador-c3-dupla-condicao.mjs /tmp/c3.html

import { chromium } from 'playwright';

const ARQUIVO = process.argv[2] || '/tmp/c3.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const VOLUME = '189,6';
const VOLUME_N = 189.6;

let falhas = 0;
function ok(nome, medida) {
  console.log('  ok    ' + nome + (medida === undefined ? '' : ' — ' + medida));
}
function nok(nome, medida) {
  falhas += 1;
  console.log('  FALHOU ' + nome + (medida === undefined ? '' : ' — ' + medida));
}
function conferir(nome, condicao, medida) {
  (condicao ? ok : nok)(nome, medida);
}

const navegador = await chromium.launch({ executablePath: CHROME });
const pagina = await navegador.newPage();
const erros = [];
pagina.on('pageerror', (e) => erros.push(String(e)));

await pagina.goto('file://' + ARQUIVO);
await pagina.fill('#aqm-c3-volume', VOLUME);
await pagina.selectOption('#aqm-c3-perfil', 'plantado');
await pagina.selectOption('#aqm-c3-carga', 'media');
await pagina.click('#aqm-c3-form button[type="submit"]');
await pagina.waitForSelector('#aqm-c3-produtos:not(.aqm-c3-oculto)', { timeout: 5000 });

conferir('nenhum erro de script ao calcular', erros.length === 0, erros.join(' | ') || 'console limpo');

// O catalogo que o snippet embute e a fonte de verdade do que DEVERIA acontecer:
// o teste nao repete a regra em JavaScript proprio, ele confere a tela contra o
// dado. Se repetisse a regra, passaria mesmo com a regra errada nos dois lados.
const catalogo = await pagina.evaluate(() => window.AQM_C3_CATALOGO || null);

const recomendados = await pagina.$$eval('#aqm-c3-produtos-lista .aqm-c3-produto h4',
  (ns) => ns.map((n) => n.textContent.trim()));
const separados = await pagina.$$eval('#aqm-c3-fora-lista .aqm-c3-produto h4',
  (ns) => ns.map((n) => n.textContent.trim()));

conferir('a lista de recomendados nao esta vazia', recomendados.length > 0,
  recomendados.length + ' item(ns): ' + recomendados.join(' / '));

// O nome de tela carrega a voltagem quando o registro declara uma so — o banco
// tem o Eheim 2217 duas vezes, em 127 V e em 220 V, e sem isso a lista mostra
// dois itens de nome identico. Este espelho precisa acompanhar, senao o teste
// deixa de casar nome com ficha e passa a aprovar tudo por nao achar nada.
function nomeDeTela(p) {
  return p.marca + ' ' + p.modelo
    + (p.voltagem && p.voltagem.length === 1 ? ' (' + p.voltagem[0] + ' V)' : '');
}

function fichaDe(nome) {
  if (!catalogo) { return null; }
  return catalogo.find((p) => nomeDeTela(p) === nome) || null;
}

// Um teste que nao acha a ficha do que esta na tela nao mede nada. Isto reprova
// em vez de passar em silencio.
function exigirFichas(nomes, rotulo) {
  const orfaos = nomes.filter((n) => fichaDe(n) === null);
  conferir('toda linha ' + rotulo + ' casa com uma ficha do catalogo embutido',
    orfaos.length === 0, orfaos.length ? orfaos.join(' / ') : nomes.length + ' linha(s)');
}

exigirFichas(recomendados, 'dos recomendados');
exigirFichas(separados, 'da secao separada');

const furamVolume = recomendados.filter((nome) => {
  const p = fichaDe(nome);
  if (!p) { return false; }
  if (p.volume_max_L !== null && VOLUME_N > p.volume_max_L) { return true; }
  if (p.volume_min_L !== null && VOLUME_N < p.volume_min_L) { return true; }
  return false;
});
conferir('nenhum recomendado tem volume declarado que nao cubra o aquario',
  furamVolume.length === 0, furamVolume.length ? furamVolume.join(' / ') : 'nenhum');

conferir('o Atman HF-0600 nao esta entre os recomendados',
  !recomendados.some((n) => n.indexOf('HF-0600') !== -1),
  recomendados.join(' / '));

const temCandidatoSeparado = (catalogo || []).some(
  (p) => p.volume_max_L !== null && VOLUME_N > p.volume_max_L
);
if (temCandidatoSeparado) {
  conferir('a secao separada existe e traz pelo menos um modelo', separados.length > 0,
    separados.length + ' item(ns): ' + separados.join(' / '));
  const rotulo = await pagina.textContent('#aqm-c3-fora h3');
  conferir('a secao separada esta rotulada pelo que ela e',
    /n[aã]o cobre esse volume/i.test(rotulo || ''), rotulo);
  const ordem = await pagina.evaluate(() => {
    const a = document.querySelector('#aqm-c3-produtos');
    const b = document.querySelector('#aqm-c3-fora');
    if (!a || !b) { return 'faltou um dos blocos'; }
    return (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) ? 'abaixo' : 'acima';
  });
  conferir('a secao separada vem ABAIXO dos recomendados no HTML', ordem === 'abaixo', ordem);
}

// Degrau de adequacao: espelho do que o snippet calcula. Serve so para dizer
// QUAIS itens sao equivalentes; quem ordena e a pagina.
const faixa = await pagina.evaluate(() => {
  const t = document.querySelector('#aqm-c3-faixa-valor').textContent;
  const n = t.replace(/[^0-9.,a ]/g, '').split(' a ');
  return n.map((x) => parseFloat(x.replace(/\./g, '').replace(',', '.')));
});
const [piso, teto] = faixa;
const meio = (piso + teto) / 2;
const passo = (teto - piso) / 10;
const degrau = (p) => (passo <= 0 ? Math.abs(p.vazao_lh - meio)
  : Math.floor(Math.abs(p.vazao_lh - meio) / passo));

const primeiro = fichaDe(recomendados[0]);
if (primeiro) {
  const equivalentes = recomendados.map(fichaDe).filter(Boolean)
    .filter((p) => degrau(p) === degrau(primeiro));
  const algumComLink = equivalentes.some((p) => p.link);
  conferir('se ha link entre os equivalentes do topo, o primeiro da lista tem link',
    !algumComLink || !!primeiro.link,
    (primeiro.marca + ' ' + primeiro.modelo) + (primeiro.link ? ' (com link)' : ' (sem link)'));

  const foraDeOrdem = recomendados.map(fichaDe).filter(Boolean)
    .map(degrau).some((g, i, todos) => i > 0 && g < todos[i - 1]);
  conferir('a ordem tecnica nao foi invertida pelo desempate de link', !foraDeOrdem,
    recomendados.map((n) => { const p = fichaDe(n); return p ? degrau(p) : '?'; }).join(' '));
}

const links = await pagina.$$eval('#aqm-c3-produtos a.aqm-c3-loja, #aqm-c3-fora a.aqm-c3-loja',
  (ns) => ns.map((n) => ({ rel: n.getAttribute('rel') || '', alvo: n.getAttribute('target') || '',
    texto: (n.textContent || '').trim() })));
conferir('todo botao de loja e sponsored + noopener + aba nova e tem texto',
  links.every((l) => /sponsored/.test(l.rel) && /noopener/.test(l.rel) && l.alvo === '_blank' && l.texto.length > 0),
  links.length + ' link(s)');

const aviso = await pagina.textContent('#aqm-c3-produtos .aqm-c3-aviso-afiliado');
conferir('o aviso de comissao continua junto do bloco e diz a palavra comissao',
  /comiss[aã]o/i.test(aviso || ''), (aviso || '').slice(0, 60) + '...');

// SEGUNDO CASO, e ele existe por um motivo: no aquario plantado do Raphael a
// faixa e estreita e nenhum par de filtros cai no mesmo degrau, entao o
// desempate por link nunca dispara e o teste acima nao prova que ele funciona.
// O mesmo volume em perfil COMUNITARIO abre a faixa ate 10 renovacoes/h e
// coloca varios modelos no mesmo degrau — e ai o desempate tem de aparecer.
console.log('\ncaso 2 — mesmo volume, perfil comunitario (faixa larga)');

await pagina.selectOption('#aqm-c3-perfil', 'comunitario');
await pagina.click('#aqm-c3-form button[type="submit"]');
await pagina.waitForSelector('#aqm-c3-produtos:not(.aqm-c3-oculto)', { timeout: 5000 });

const rec2 = await pagina.$$eval('#aqm-c3-produtos-lista .aqm-c3-produto h4',
  (ns) => ns.map((n) => n.textContent.trim()));
const faixa2 = await pagina.evaluate(() => {
  const t = document.querySelector('#aqm-c3-faixa-valor').textContent;
  return t.replace(/[^0-9.,a ]/g, '').split(' a ')
    .map((x) => parseFloat(x.replace(/\./g, '').replace(',', '.')));
});
const meio2 = (faixa2[0] + faixa2[1]) / 2;
const passo2 = (faixa2[1] - faixa2[0]) / 10;
const degrau2 = (p) => (passo2 <= 0 ? Math.abs(p.vazao_lh - meio2)
  : Math.floor(Math.abs(p.vazao_lh - meio2) / passo2));

exigirFichas(rec2, 'dos recomendados do caso 2');
const fichas2 = rec2.map(fichaDe).filter(Boolean);
const grupos = {};
fichas2.forEach((p) => { const g = degrau2(p); (grupos[g] = grupos[g] || []).push(p); });
const empatados = Object.keys(grupos).filter((g) => grupos[g].length > 1);

conferir('a faixa larga produz pelo menos um grupo de equivalentes', empatados.length > 0,
  'degraus com mais de um item: ' + (empatados.join(', ') || 'nenhum'));

const desempateOk = empatados.every((g) => {
  const lista = grupos[g];
  let viuSemLink = false;
  return lista.every((p) => {
    if (!p.link) { viuSemLink = true; return true; }
    return !viuSemLink;
  });
});
conferir('dentro de cada grupo de equivalentes, quem tem link vem antes de quem nao tem',
  desempateOk, rec2.map((n) => {
    const p = fichaDe(n);
    return p ? degrau2(p) + (p.link ? '+' : '-') : '?';
  }).join(' '));

const ordemOk2 = fichas2.map(degrau2).every((g, i, todos) => i === 0 || g >= todos[i - 1]);
conferir('a ordem por adequacao tecnica continua mandando entre grupos', ordemOk2,
  rec2.join(' / '));

await navegador.close();

console.log(falhas === 0 ? '\n=== tudo passou ===' : '\n=== ' + falhas + ' falha(s) ===');
process.exit(falhas === 0 ? 0 : 1);

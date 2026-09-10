// O teste que faltava: EXECUTA o cálculo das cinco calculadoras num Chromium de
// verdade e confere na tela o que o Raphael conferiu à mão em 08/09/2026.
//
// Regra permanente do projeto, escrita depois daquele dia: calculadora só conta
// como entregue depois que alguém EXECUTOU o cálculo e viu o resultado e os
// links na tela. Página que carrega não é calculadora que funciona.
//
// Os testes por calculadora (teste-navegador-c5.mjs e irmãos) cobrem o miolo de
// cada uma; este cobre, nas cinco de uma vez, exatamente a cadeia que estava
// quebrada: script inteiro chega ao navegador → clicar em Calcular calcula →
// a resposta sai do estado oculto → o bloco de produto aparece com link de
// afiliado marcado como sponsored.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . <shortcode> > /tmp/cN.html   (as cinco)
//   node ferramentas/teste-navegador-cinco.mjs /tmp
//
// O caminho do Chromium é o do container do Claude Code na nuvem.

import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const CASOS = [
  { codigo: 'c1',  arquivo: 'c1.html',  produtos: false,
    preencher: async p => { await p.fill('#aqm-c1-c', '80'); await p.fill('#aqm-c1-l', '35'); await p.fill('#aqm-c1-a', '45'); } },
  { codigo: 'c3',  arquivo: 'c3.html',  produtos: true,
    preencher: async p => { await p.fill('#aqm-c3-volume', '100'); await p.selectOption('#aqm-c3-perfil', 'comunitario'); } },
  { codigo: 'c5',  arquivo: 'c5.html',  produtos: true,
    preencher: async p => { await p.fill('#aqm-c5-volume', '100'); await p.fill('#aqm-c5-minima', '18'); await p.fill('#aqm-c5-alvo', '26'); } },
  { codigo: 'c12', arquivo: 'c12.html', produtos: true,
    preencher: async p => { await p.fill('#aqm-c12-volume', '100'); await p.selectOption('#aqm-c12-perfil', 'comunitario'); } },
  // C15: até 09/09/2026 este caso trazia semProduto:true, porque as luminárias
  // do catálogo estavam barradas por falta de lúmen ou voltagem declarados. A
  // leva de catálogo daquele mesmo dia fechou a lacuna (a Chihiros WRGB II Pro
  // 60 ganhou voltagem e a C15 foi de 3 para 9 aptas), e a asserção passou a
  // REPROVAR exatamente o trabalho que a fila mandou fazer. O sinalizador saiu:
  // ver a regra escrita logo abaixo, na afirmação 5.
  { codigo: 'c15', arquivo: 'c15.html', produtos: true,
    preencher: async p => { await p.fill('#aqm-c15-volume', '100'); await p.fill('#aqm-c15-comprimento', '80'); await p.fill('#aqm-c15-lamina', '45'); await p.selectOption('#aqm-c15-regime', 'normal'); } },
];

let falhas = 0;
// Quantos links de afiliado bem marcados o conjunto das cinco calculadoras
// serviu. Existe porque a afirmação por calculadora NÃO pode exigir link: a
// ordem é por adequação técnica, e catálogo maior chega a REDUZIR links na tela
// (medido em 09/09/2026) — exigir link por página seria pedir que o banco não
// melhorasse. Mas se NENHUMA das cinco servir um link marcado, o encanamento do
// afiliado quebrou, e isso é defeito de verdade.
let linksMarcadosNoTotal = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

const browser = await chromium.launch({ executablePath: CHROME });
const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });

for (const caso of CASOS) {
  console.log(`\n${caso.codigo.toUpperCase()} — ${caso.arquivo}`);
  const page = await ctx.newPage();
  const erros = [];
  // ERR_CONNECTION_RESET é a Google Fonts barrada pelo proxy do container, não
  // defeito da calculadora: só erro de JavaScript conta aqui.
  page.on('pageerror', e => erros.push('pageerror: ' + e.message));
  // O filtro derruba SO falha de rede, nunca falha de script. ERR_TUNNEL entrou
  // em 10/09/2026, com a vitrine da C3: os cartoes carregam foto do CDN da
  // Shopee, e o egresso desta nuvem responde ERR_TUNNEL_CONNECTION_FAILED em
  // todo dominio de loja. No Chrome do Raphael as mesmas URLs carregam. Quem
  // confere que a URL da foto e a do banco e o teste-navegador-c3-vitrine, por
  // dado; quem confere que a imagem ABRE e a Sentinela Tecnica, no navegador
  // dela. Manter este erro aqui faria o teste reprovar todo dia por um motivo
  // que nao e defeito — e teste que reprova sempre e teste que ninguem le.
  page.on('console', m => { if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|TUNNEL|PROXY)/.test(m.text())) erros.push(m.text()); });

  await page.goto('file://' + DIR + '/' + caso.arquivo);
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();

  // 1. O script chegou inteiro? Um "&&" escapado matava tudo com SyntaxError.
  ok('nenhum SyntaxError no carregamento', erros.length === 0, erros.join(' | '));
  const html = await page.content();
  ok('zero &#038; no HTML servido', !html.includes('&#038;'));

  // 2. O comportamento realmente ligou: a raiz responde ao JavaScript.
  const ligou = await page.evaluate(c => {
    const f = document.querySelector('#aqm-' + c + '-form');
    return !!f;
  }, caso.codigo);
  ok('formulário presente', ligou);

  // 3. Calcular calcula.
  const antes = await page.getAttribute('#aqm-' + caso.codigo + '-saida', 'class');
  await caso.preencher(page);
  // Marca que só sobrevive se a página NÃO recarregar. Com o script morto, o
  // clique virava submit nativo do formulário e a página inteira recarregava —
  // era esse o sintoma na tela. A querystring, sozinha, não serve de sinal: as
  // calculadoras reescrevem a URL de propósito, para o resultado ser
  // compartilhável.
  await page.evaluate(() => { window.__aqmNaoRecarregou = true; });
  await page.click('#aqm-' + caso.codigo + '-form button[type="submit"]');
  await page.waitForTimeout(350);
  const depois = await page.getAttribute('#aqm-' + caso.codigo + '-saida', 'class');
  // O contêiner nasce oculto no HTML servido — é casca estática. Quem tira a
  // classe é o script. Se ele morre, o contêiner fica oculto para sempre, que
  // foi o que o Raphael viu nas cinco páginas em 08/09/2026.
  // Precisa ser o HTML SERVIDO, lido do arquivo: no DOM vivo o script já tirou
  // a classe, e a afirmação passaria sem querer dizer nada.
  const servido = readFileSync(DIR + '/' + caso.arquivo, 'utf8');
  ok('contêiner nasce oculto no HTML servido',
     new RegExp('class="[^"]*' + caso.codigo + '-oculto[^"]*" id="aqm-' + caso.codigo + '-saida"').test(servido));
  ok('resposta visível depois de calcular', !/oculto/.test(depois || '') && await page.isVisible('#aqm-' + caso.codigo + '-saida'),
     `depois="${depois}"`);

  const numero = await page.textContent('#aqm-' + caso.codigo + '-faixa-valor').catch(() => null)
    || await page.textContent('#aqm-' + caso.codigo + '-real').catch(() => null);
  ok('número calculado na tela', !!numero && numero.trim().length > 0, (numero || '').trim().slice(0, 60));

  // 4. A página não recarregou: submit nativo era o sintoma do script morto.
  const sobreviveu = await page.evaluate(() => window.__aqmNaoRecarregou === true);
  ok('sem submit nativo (a página não recarregou)', sobreviveu);

  // 5. O bloco de produto e o link de afiliado.
  //
  // A REGRA, escrita em 09/09/2026 na terceira vez que a ilha tropeçou nela:
  // teste que exige que um buraco de catálogo continue ABERTO reprova
  // exatamente o trabalho que a fila manda fazer. Este caso trazia
  // semProduto:true para a C15 e virou vermelho no dia em que a leva de
  // catálogo lhe deu luminária apta — sem nenhum defeito de código.
  //
  // Então aqui não se afirma mais QUAL dos dois estados a página deve ter: os
  // dois são legítimos, e o catálogo decide qual é hoje. Bloco vazio é PORTÃO,
  // não defeito (seção 7 do contrato) — o que não pode é ele sair calado. E
  // bloco cheio não pode sair com link mal marcado. Afirma-se a promessa de
  // cada estado, que é o que não envelhece quando o banco cresce.
  if (caso.produtos) {
    const visivel = await page.isVisible('#aqm-' + caso.codigo + '-produtos');
    const links = await page.$$eval('#aqm-' + caso.codigo + '-produtos a[href*="shopee"]',
      as => as.map(a => ({ rel: a.getAttribute('rel') || '', target: a.getAttribute('target') || '' })));

    if (visivel) {
      ok('bloco de produto visível, e então tem de estar bem formado',
         true, links.length + ' link(s) de loja');
      // Cartão sem link é legítimo (V16: produto apto sem link aparece igual, só
      // sem botão). O que se exige é que o link QUE EXISTIR esteja marcado.
      ok('todo link leva rel=sponsored', links.every(l => l.rel.includes('sponsored')));
      ok('todo link leva noopener', links.every(l => l.rel.includes('noopener')));
      ok('todo link abre em nova aba', links.every(l => l.target === '_blank'));
      linksMarcadosNoTotal += links.filter(
        l => l.rel.includes('sponsored') && l.rel.includes('noopener') && l.target === '_blank').length;
      const aviso = await page.textContent('#aqm-' + caso.codigo + '-produtos');
      ok('aviso de comissão visível no bloco', /comiss/i.test(aviso || ''));
    } else {
      ok('bloco de produto oculto, e então a página tem de dizer por quê',
         links.length === 0, 'nenhum link vazando de bloco oculto');
      const barrados = await page.textContent('#aqm-' + caso.codigo + '-barrados').catch(() => '');
      const nada = await page.textContent('#aqm-' + caso.codigo + '-produtos-nada').catch(() => '');
      ok('a página publica por que não sugere produto',
         /declara|atende|nenhum|faixa/i.test((barrados || '') + ' ' + (nada || '')));
    }
  }

  await page.close();
}

await browser.close();

// A afirmação de conjunto: nenhuma calculadora é obrigada a ter link, mas o
// arquipélago inteiro não pode ficar sem nenhum — aí não é catálogo, é
// encanamento quebrado.
console.log('\nO CONJUNTO DAS CINCO');
ok('pelo menos um link de afiliado bem marcado no conjunto das cinco',
   linksMarcadosNoTotal > 0, linksMarcadosNoTotal + ' link(s) marcados');

console.log(falhas ? `\n=== ${falhas} FALHA(S) ===` : '\n=== tudo passou ===');
process.exit(falhas ? 1 : 0);

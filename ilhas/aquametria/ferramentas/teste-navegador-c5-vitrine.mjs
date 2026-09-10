// O portao da VITRINE da C5 (bloco T8, 10/09/2026).
//
// Copia o desenho do teste-navegador-c3-vitrine.mjs e acrescenta o que so a C5
// tem. A vitrine e o unico bloco da pagina que pode ficar bonito e errado ao
// mesmo tempo: ela mostra foto, preco e botao de loja, e essas tres coisas sao
// exatamente as que empurram uma pagina para vender o que paga mais em vez do
// que atende. Por isso este arquivo nao mede aparencia. Ele mede o que, se
// ceder, transforma a Aquametria numa fazenda de conteudo:
//
//   1. A ORDEM DA VITRINE E IDENTICA A DA LISTA TECNICA, cartao por cartao. Se
//      um dia alguem ordenar por comissao, por preco ou por "quem tem foto",
//      este teste reprova.
//   2. O GRUPO DE CADA CARTAO E O MESMO DA LISTA TECNICA. Isto e da C5 e nao
//      existe na C3: a lista aqui e partida em "dentro da faixa calculada" e "o
//      degrau comercial acima". Um cartao de vitrine nao comporta cabecalho de
//      grupo, entao a distincao viaja na frase do cartao — e um cartao do degrau
//      acima que diga "dentro da faixa" e a contradicao do item 2 do despacho da
//      Sentinela de 10/09/2026 reencenada em foto e botao de loja.
//   3. NENHUM PRODUTO SOME POR NAO TER FOTO OU LINK. Nesta calculadora isso e a
//      regra e nao a excecao: 16 dos 18 aquecedores do catalogo nao tem foto.
//   4. O PRECO E SEMPRE COTACAO COM DATA, e bate com o banco.
//   5. A VITRINE VEM ANTES DA PROCEDENCIA no HTML (contrato 7).
//
// E mede as duas metades da pagina, porque elas falham por motivos diferentes:
// a vitrine SERVIDA com o JavaScript DESLIGADO (e o que um crawler de IA recebe)
// e a vitrine PINTADA com ele ligado (e o que o comprador ve).
//
// O teste nao guarda numero esperado nenhum: ele le AQM_C5_CATALOGO, que e o
// dado que o snippet embute, e confere a tela contra ele.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor > /tmp/c5.html
//   node ferramentas/teste-navegador-c5-vitrine.mjs /tmp/c5.html

import { chromium } from 'playwright';

const ARQUIVO = process.argv[2] || '/tmp/c5.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

// O caso do teste: 108 L de agua real, comodo que cai a 16 C e alvo de 26 C.
// Escolhido porque e o MESMO caso do despacho da Sentinela de 10/09/2026, o que
// deu origem ao conserto da 1.4.0: a faixa sai 110 a 160 W, a prateleira nao tem
// 160 W, e a lista nasce com os dois grupos ao mesmo tempo — a unica combinacao
// capaz de pegar de uma vez a ordem, os grupos, os cartoes com e sem link e os
// cartoes com e sem foto.
const VOLUME = '108';
const VOLUME_N = 108;
const MINIMA = '16';
const ALVO = '26';
const VOLTAGEM = '110';

// O caso da vitrine SERVIDA e propriedade do snippet, nao do teste: e o aquario
// de referencia de 100 L que a pagina publica no HTML.
const VOLUME_SERVIDO = 100;

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

const br = (n, casas) => n.toLocaleString('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas });
const watts = (n) => br(Math.round(n / 5) * 5, 0);
const litros = (n) => (n >= 100 ? br(Math.round(n), 0) : br(Math.round(n * 10) / 10, 1));

function dataBr(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || ''));
  return m ? m[3] + '/' + m[2] + '/' + m[1] : String(iso);
}

// A leitura de um trilho de vitrine, seja ele o servido ou o pintado. Devolve
// para cada cartao so o que o teste julga — nunca o HTML inteiro, que mudaria a
// cada ajuste de estilo e faria o teste reprovar por motivo errado.
const LER_TRILHO = (seletor) => {
  const trilho = document.querySelector(seletor);
  if (!trilho) { return null; }
  return Array.from(trilho.querySelectorAll('.aqm-c5-vt-item')).map((li) => {
    const cartao = li.querySelector('.aqm-c5-vt-cartao');
    const img = li.querySelector('.aqm-c5-vt-foto img');
    const t = (s) => {
      const n = li.querySelector(s);
      return n ? n.textContent.trim() : null;
    };
    return {
      tag: cartao ? cartao.tagName.toLowerCase() : null,
      href: cartao && cartao.tagName.toLowerCase() === 'a' ? cartao.getAttribute('href') : null,
      rel: cartao ? cartao.getAttribute('rel') : null,
      alvo: cartao ? cartao.getAttribute('target') : null,
      marca: t('.aqm-c5-vt-marca'),
      modelo: t('.aqm-c5-vt-modelo'),
      espec: t('.aqm-c5-vt-espec'),
      ressalva: t('.aqm-c5-vt-ressalva'),
      preco: t('.aqm-c5-vt-preco'),
      botao: t('.aqm-c5-vt-botao'),
      espera: t('.aqm-c5-vt-espera'),
      temFoto: !!img,
      imgSrc: img ? img.getAttribute('src') : null,
      imgAlt: img ? img.getAttribute('alt') : null,
      imgLazy: img ? img.getAttribute('loading') : null,
      placeholder: !!li.querySelector('.aqm-c5-vt-foto-vazia'),
    };
  });
};

const navegador = await chromium.launch({ executablePath: CHROME });

/* ===================================================================== */
/* 1. A vitrine SERVIDA, com o JavaScript DESLIGADO                      */
/* ===================================================================== */

console.log('\nvitrine SERVIDA (JavaScript desligado — o que um crawler de IA recebe)');

const ctxSemJs = await navegador.newContext({ javaScriptEnabled: false });
const semJs = await ctxSemJs.newPage();
await semJs.goto('file://' + ARQUIVO, { waitUntil: 'domcontentloaded' });

const servidos = await semJs.evaluate(LER_TRILHO, '.aqm-c5-vitrine-servida .aqm-c5-vt-trilho');

conferir('a vitrine servida existe no HTML', Array.isArray(servidos) && servidos.length > 0,
  (servidos ? servidos.length : 0) + ' cartao(oes)');

if (servidos && servidos.length) {
  conferir('a vitrine servida tem pelo menos 3 cartoes (portao de dado da secao 9)',
    servidos.length >= 3, servidos.length + ' cartao(oes)');
  conferir('a vitrine servida para em 5 cartoes, como a pintada (secao 7: de tres a cinco)',
    servidos.length <= 5, servidos.length + ' cartao(oes)');

  const semEspec = servidos.filter((c) => !c.espec || !/^\d/.test(c.espec) || !/ W — /.test(c.espec));
  conferir('todo cartao servido diz a especificacao que fez o produto entrar, em watts',
    semEspec.length === 0,
    semEspec.length ? semEspec.map((c) => c.modelo + ': ' + c.espec).join(' / ') : servidos[0].espec);

  const volErrado = servidos.filter((c) => !/degrau comercial acima/.test(c.espec)
    && !c.espec.includes(litros(VOLUME_SERVIDO) + ' L'));
  conferir('a especificacao servida cita o volume do exemplo publicado',
    volErrado.length === 0,
    volErrado.length ? volErrado.map((c) => c.espec).join(' / ') : VOLUME_SERVIDO + ' L em todos');

  const semMarca = servidos.filter((c) => !c.marca);
  conferir('todo cartao servido tem marca', semMarca.length === 0,
    semMarca.length ? semMarca.length + ' sem marca' : 'todos');

  const repetido = servidos.filter((c) => c.marca && c.modelo && c.modelo.startsWith(c.marca + ' '));
  conferir('o modelo NAO repete a marca no cartao', repetido.length === 0,
    repetido.length ? repetido.map((c) => c.modelo).join(' / ') : 'nenhuma repeticao');

  const anco = servidos.filter((c) => c.tag === 'a');
  const semLink = servidos.filter((c) => c.tag !== 'a');

  conferir('cartao com link e ancora de verdade, nunca div com onclick',
    anco.every((c) => c.href && /^https?:/.test(c.href)),
    anco.length + ' ancora(s)');
  conferir('toda ancora da vitrine e sponsored + noopener em aba nova',
    anco.every((c) => /sponsored/.test(c.rel || '') && /noopener/.test(c.rel || '') && c.alvo === '_blank'),
    anco.map((c) => c.rel).join(' | ') || 'nenhuma');
  conferir('toda ancora da vitrine tem botao de loja escrito',
    anco.every((c) => c.botao && c.botao.length > 0),
    anco.map((c) => c.botao).join(' / ') || 'nenhuma');

  conferir('cartao SEM link nao vira ancora e reserva o lugar do botao (contrato 7)',
    semLink.every((c) => c.espera && /link de loja em breve/i.test(c.espera)),
    semLink.length ? semLink.length + ' cartao(oes) com o lugar reservado' : 'nenhum cartao sem link neste caso');

  const comFoto = servidos.filter((c) => c.temFoto);
  conferir('toda imagem da vitrine tem alt descritivo',
    comFoto.every((c) => c.imgAlt && c.imgAlt.length >= 20),
    comFoto.length + ' imagem(ns)' + (comFoto.length
      ? ', menor alt com ' + Math.min(...comFoto.map((c) => (c.imgAlt || '').length)) + ' caracteres'
      : ''));
  conferir('toda imagem da vitrine e loading=lazy',
    comFoto.every((c) => c.imgLazy === 'lazy'), comFoto.length + ' imagem(ns)');
  conferir('cartao sem foto NAO some: sai com espaco reservado neutro',
    servidos.every((c) => c.temFoto || c.placeholder),
    servidos.filter((c) => c.placeholder).length + ' com espaco reservado');

  const precoSemData = servidos.filter((c) => c.preco && /R\$/.test(c.preco) && !/cotado em \d{2}\/\d{2}\/\d{4}/.test(c.preco));
  conferir('nenhum preco aparece sem a data da coleta ao lado',
    precoSemData.length === 0,
    precoSemData.length ? precoSemData.map((c) => c.preco).join(' / ')
      : servidos.filter((c) => /R\$/.test(c.preco || '')).length + ' com cotacao datada');
}

// A pagina nao pode mais dizer que nao publica preco: ela publica, datado.
const corpoServido = await semJs.evaluate(() => document.body.innerText);
conferir('a pagina NAO diz mais que nao publica preco (a vitrine publica, com data)',
  !/n[aã]o publicamos pre[çc]o/i.test(corpoServido),
  (corpoServido.match(/n[aã]o publicamos pre[çc]o/gi) || []).join(' / ') || 'nenhuma ocorrencia');

// A promessa e a ordem dos blocos no HTML servido.
const promessa = await semJs.$eval('.aqm-c5-promessa', (n) => n.textContent.trim()).catch(() => null);
conferir('a linha de promessa esta no topo, no HTML servido',
  !!promessa && promessa.length > 20, promessa || 'ausente');
conferir('a promessa nao tem tom de anuncio (sem exclamacao)',
  !!promessa && !/!/.test(promessa), promessa || 'ausente');

const promessaAntes = await semJs.evaluate(() => {
  const p = document.querySelector('.aqm-c5-promessa');
  const form = document.querySelector('#aqm-c5-form');
  if (!p || !form) { return null; }
  return !!(p.compareDocumentPosition(form) & Node.DOCUMENT_POSITION_FOLLOWING);
});
conferir('a promessa vem ANTES do formulario', promessaAntes === true, String(promessaAntes));

await ctxSemJs.close();

/* ===================================================================== */
/* 2. A vitrine PINTADA, com o JavaScript ligado                         */
/* ===================================================================== */

console.log('\nvitrine PINTADA (JavaScript ligado — o que o comprador ve)');

const ctx = await navegador.newContext({ viewport: { width: 1200, height: 900 } });
const pagina = await ctx.newPage();
const erros = [];
pagina.on('pageerror', (e) => erros.push(String(e)));

await pagina.goto('file://' + ARQUIVO, { waitUntil: 'domcontentloaded' });
await pagina.fill('#aqm-c5-volume', VOLUME);
await pagina.fill('#aqm-c5-minima', MINIMA);
await pagina.fill('#aqm-c5-alvo', ALVO);
await pagina.selectOption('#aqm-c5-voltagem', VOLTAGEM);
await pagina.click('#aqm-c5-form button[type="submit"]');
await pagina.waitForSelector('#aqm-c5-vitrine:not(.aqm-c5-oculto)', { timeout: 5000 });

conferir('nenhum erro de script ao pintar a vitrine', erros.length === 0,
  erros.join(' | ') || 'console limpo');

const catalogo = await pagina.evaluate(() => window.AQM_C5_CATALOGO || null);
conferir('o catalogo embutido chegou ao navegador', Array.isArray(catalogo),
  (catalogo ? catalogo.length : 0) + ' aquecedor(es)');

// A regra que nao pode ceder: comissao nao viaja para o snippet.
const chavesComissao = JSON.stringify(catalogo || []).match(/"[^"]*comiss[^"]*"/gi) || [];
conferir('nenhuma comissao viaja dentro do catalogo do snippet',
  chavesComissao.length === 0, chavesComissao.join(' / ') || 'nenhuma chave de comissao');

const pintados = await pagina.evaluate(LER_TRILHO, '#aqm-c5-vitrine-trilho');

// A lista tecnica: nome E grupo de cada item, na ordem do DOM.
const fichas = await pagina.$$eval('#aqm-c5-produtos-lista .aqm-c5-produto',
  (ns) => ns.map((n) => ({
    nome: n.querySelector('h4').textContent.trim().replace(/\s+/g, ' '),
    acima: n.classList.contains('aqm-c5-produto-acima'),
  })));

conferir('a vitrine pintada nao esta vazia', pintados && pintados.length > 0,
  (pintados ? pintados.length : 0) + ' cartao(oes)');
conferir('o caso do teste produz os DOIS grupos, que e o que ele existe para medir',
  fichas.some((f) => f.acima) && fichas.some((f) => !f.acima),
  fichas.filter((f) => !f.acima).length + ' dentro da faixa, ' + fichas.filter((f) => f.acima).length + ' no degrau acima');

// A faixa publicada, para conferir a frase dos cartoes contra o que a pagina diz.
const faixa = await pagina.$eval('#aqm-c5-faixa-valor', (n) => n.textContent.trim());
console.log('  nota  faixa publicada nesta entrada: ' + faixa);

// ---- O portao central: a vitrine NAO reordena nada. -------------------------
const nomeVitrine = (c) => (c.marca + ' ' + c.modelo).replace(/\s+/g, ' ').trim();
const ordemVitrine = (pintados || []).map(nomeVitrine);
const ordemFicha = fichas.map((f) => f.nome);

conferir('a vitrine tem exatamente os mesmos itens da lista tecnica',
  ordemVitrine.length === ordemFicha.length,
  ordemVitrine.length + ' na vitrine, ' + ordemFicha.length + ' na lista');
conferir('A ORDEM DA VITRINE E IDENTICA A DA LISTA TECNICA (nada reordena por foto, preco ou comissao)',
  JSON.stringify(ordemVitrine) === JSON.stringify(ordemFicha),
  ordemVitrine.join(' > ') + '   ||   ' + ordemFicha.join(' > '));

// ---- Contrato 7: o bloco de compra vem ANTES da prova de procedencia. -------
const vitrineAntes = await pagina.evaluate(() => {
  const vitrine = document.querySelector('#aqm-c5-vitrine');
  const ficha = document.querySelector('#aqm-c5-produtos-lista');
  if (!vitrine || !ficha) { return null; }
  return !!(vitrine.compareDocumentPosition(ficha) & Node.DOCUMENT_POSITION_FOLLOWING);
});
conferir('a vitrine vem ANTES da ficha e da procedencia no HTML (contrato 7)',
  vitrineAntes === true, String(vitrineAntes));

// ---- O portao que so a C5 tem: o GRUPO de cada cartao. ----------------------
if (pintados && pintados.length === fichas.length) {
  const grupoErrado = pintados
    .map((c, i) => ({ c, ficha: fichas[i] }))
    .filter(({ c, ficha }) => /degrau comercial acima/.test(c.espec) !== ficha.acima);
  conferir('CADA CARTAO DIZ O GRUPO EM QUE A LISTA TECNICA O POS, e nao outro',
    grupoErrado.length === 0,
    grupoErrado.length
      ? grupoErrado.map(({ c, ficha }) => nomeVitrine(c) + ': cartao diz ' +
          (/degrau comercial acima/.test(c.espec) ? 'acima' : 'dentro') +
          ', a lista diz ' + (ficha.acima ? 'acima' : 'dentro')).join(' / ')
      : pintados.filter((c) => /degrau comercial acima/.test(c.espec)).length + ' no degrau acima, o resto dentro da faixa');

  const dentroMentindo = pintados
    .map((c, i) => ({ c, ficha: fichas[i] }))
    .filter(({ c, ficha }) => ficha.acima && /dentro dos/.test(c.espec));
  conferir('nenhum cartao do degrau acima diz "dentro dos" (a contradicao do despacho de 10/09)',
    dentroMentindo.length === 0,
    dentroMentindo.map(({ c }) => nomeVitrine(c) + ': ' + c.espec).join(' / ') || 'nenhum');
}

// ---- Cada cartao contra o dado que o gerou. ---------------------------------
if (pintados && pintados.length && Array.isArray(catalogo)) {
  const porNome = {};
  catalogo.forEach((p) => {
    let modelo = p.modelo;
    if (p.voltagem && p.voltagem.length === 1) { modelo += ' (' + p.voltagem[0] + ' V)'; }
    porNome[(p.marca + ' ' + modelo).replace(/\s+/g, ' ').trim()] = p;
  });

  const semDado = pintados.filter((c) => !porNome[nomeVitrine(c)]);
  conferir('todo cartao da vitrine corresponde a um registro do catalogo',
    semDado.length === 0, semDado.map(nomeVitrine).join(' / ') || 'todos');

  // A faixa que a propria pagina publicou, lida do texto, para o teste nao
  // repetir a formula de piso e teto em JavaScript proprio.
  const nums = faixa.replace(/\./g, '').match(/[\d,]+/g) || [];
  const piso = nums[0];
  const teto = nums[1];

  const especErrada = pintados.filter((c, i) => {
    const p = porNome[nomeVitrine(c)];
    if (!p) { return true; }
    const esperado = fichas[i] && fichas[i].acima
      ? br(p.potencia_w, 0) + ' W — degrau comercial acima dos ' + teto + ' W do topo'
      : br(p.potencia_w, 0) + ' W — dentro dos ' + piso + ' a ' + teto + ' W que os ' + litros(VOLUME_N) + ' L pedem';
    return c.espec !== esperado;
  });
  conferir('a especificacao de cada cartao e a potencia do banco com a faixa que a pagina publicou',
    especErrada.length === 0,
    especErrada.length ? especErrada.map((c) => c.espec).join(' / ') : pintados[0].espec);

  const precoErrado = pintados.filter((c) => {
    const p = porNome[nomeVitrine(c)];
    if (!p) { return true; }
    if (!p.preco) { return c.preco !== 'sem cotação coletada'; }
    return !c.preco.includes(dataBr(p.preco.coletado_em)) || !c.preco.includes(br(p.preco.min, 2));
  });
  conferir('o preco de cada cartao e a cotacao do banco, com a data da coleta',
    precoErrado.length === 0,
    precoErrado.length ? precoErrado.map((c) => nomeVitrine(c) + ': ' + c.preco).join(' / ')
      : pintados.map((c) => c.preco).join(' | '));

  const linkErrado = pintados.filter((c) => {
    const p = porNome[nomeVitrine(c)];
    if (!p) { return true; }
    return p.link ? c.href !== p.link : c.tag === 'a';
  });
  conferir('cartao aponta para o link do banco, e cartao sem link nao vira ancora',
    linkErrado.length === 0, linkErrado.map(nomeVitrine).join(' / ') || 'todos conferidos');

  const fotoErrada = pintados.filter((c) => {
    const p = porNome[nomeVitrine(c)];
    if (!p) { return true; }
    return (p.imagem && p.imagem.url) ? c.imgSrc !== p.imagem.url : !c.placeholder;
  });
  conferir('cartao usa a foto do banco, e sem foto usa o espaco reservado neutro',
    fotoErrada.length === 0, fotoErrada.map(nomeVitrine).join(' / ') || 'todos conferidos');

  // A ressalva de volume declarado nao pode sumir no cartao bonito: quem so olha
  // a vitrine merece o mesmo aviso que a ficha da.
  const ressalvaFaltando = pintados.filter((c) => {
    const p = porNome[nomeVitrine(c)];
    if (!p || p.volume_max_L === null || p.volume_max_L >= VOLUME_N) { return false; }
    return !c.ressalva || !c.ressalva.includes(litros(p.volume_max_L));
  });
  conferir('cartao cujo volume declarado nao cobre o aquario diz isso, como a ficha diz',
    ressalvaFaltando.length === 0,
    ressalvaFaltando.map(nomeVitrine).join(' / ') ||
      pintados.filter((c) => c.ressalva).length + ' cartao(oes) com ressalva de volume');

  const esperando = pintados.filter((c) => c.tag !== 'a').length;
  console.log('  nota  ' + esperando + ' de ' + pintados.length +
    ' cartoes deste caso esperam link de afiliado');
  console.log('  nota  ' + pintados.filter((c) => c.temFoto).length + ' de ' + pintados.length +
    ' cartoes deste caso tem foto');
}

// ---- O carrossel e CSS puro, e rola. ---------------------------------------
const snap = await pagina.$eval('#aqm-c5-vitrine-trilho',
  (n) => getComputedStyle(n).scrollSnapType + ' | ' + getComputedStyle(n).overflowX);
conferir('o trilho tem scroll-snap em CSS puro e rola na horizontal',
  /x/.test(snap) && /auto|scroll/.test(snap), snap);

/* ===================================================================== */
/* 3. Celular: barra fixa enquanto o resultado esta fora da tela          */
/* ===================================================================== */

console.log('\ncelular (390 x 720)');

const barraNoDesktop = await pagina.$eval('#aqm-c5-barra', (n) => getComputedStyle(n).display);
conferir('a barra fixa NAO aparece em tela larga', barraNoDesktop === 'none', barraNoDesktop);

await ctx.close();

const ctxCel = await navegador.newContext({ viewport: { width: 390, height: 720 } });
const cel = await ctxCel.newPage();
const errosCel = [];
cel.on('pageerror', (e) => errosCel.push(String(e)));

await cel.goto('file://' + ARQUIVO, { waitUntil: 'domcontentloaded' });
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.fill('#aqm-c5-volume', VOLUME);
await cel.fill('#aqm-c5-minima', MINIMA);
await cel.fill('#aqm-c5-alvo', ALVO);
await cel.click('#aqm-c5-form button[type="submit"]');
await cel.waitForSelector('#aqm-c5-vitrine:not(.aqm-c5-oculto)', { timeout: 5000 });
await cel.waitForTimeout(700);

conferir('nenhum erro de script no celular', errosCel.length === 0,
  errosCel.join(' | ') || 'console limpo');

const rolou = await cel.evaluate(() => window.scrollY);
conferir('calcular rola a pagina ate o resultado', rolou > 0, 'scrollY = ' + rolou);

const resultadoAVista = await cel.evaluate(() => {
  const c = document.querySelector('#aqm-c5-saida').getBoundingClientRect();
  return c.top >= -5 && c.top < window.innerHeight;
});
conferir('depois da rolagem o resultado esta na tela', resultadoAVista === true, String(resultadoAVista));

// Sem rolagem horizontal a 390 px, com o trilho da vitrine na tela.
const rolagemH = await cel.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
conferir('nenhuma rolagem horizontal na pagina a 390 px', rolagemH <= 0, rolagemH + ' px');

// Longe do resultado, a barra tem que aparecer.
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.waitForTimeout(600);
const barraNoTopo = await cel.$eval('#aqm-c5-barra',
  (n) => getComputedStyle(n).display + ' | ' + n.getAttribute('aria-hidden'));
conferir('com o resultado fora da tela, a barra do celular aparece',
  /flex/.test(barraNoTopo) && /false/.test(barraNoTopo), barraNoTopo);

const textoBarra = await cel.$eval('#aqm-c5-barra-texto', (n) => n.textContent.trim());
conferir('a barra do celular carrega a faixa calculada, nao um texto generico',
  / W /.test(textoBarra) && textoBarra.includes(litros(VOLUME_N)), textoBarra);

// O botao dela leva ao resultado, e ai ela some.
await cel.click('#aqm-c5-barra-ir');
await cel.waitForTimeout(700);
const barraNoResultado = await cel.$eval('#aqm-c5-barra',
  (n) => getComputedStyle(n).display + ' | ' + n.getAttribute('aria-hidden'));
conferir('com o resultado a vista, a barra some',
  /none/.test(barraNoResultado) && /true/.test(barraNoResultado), barraNoResultado);

// Limpar tem que desligar a barra, senao ela fica prometendo um resultado morto.
await cel.click('#aqm-c5-limpar');
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.waitForTimeout(500);
const barraDepoisDeLimpar = await cel.$eval('#aqm-c5-barra', (n) => getComputedStyle(n).display);
conferir('limpar o formulario desliga a barra', barraDepoisDeLimpar === 'none', barraDepoisDeLimpar);

await ctxCel.close();
await navegador.close();

console.log('\n' + (falhas === 0 ? 'TUDO OK' : falhas + ' FALHA(S)'));
process.exit(falhas === 0 ? 0 : 1);

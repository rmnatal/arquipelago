// O portao da VITRINE da C15 (bloco T8, 11/09/2026).
//
// Copia o desenho do teste-navegador-c5-vitrine.mjs e acrescenta o que so a C15
// tem. A vitrine e o unico bloco da pagina que pode ficar bonito e errado ao
// mesmo tempo: ela mostra foto, preco e botao de loja, e essas tres coisas sao
// exatamente as que empurram uma pagina para vender o que paga mais em vez do
// que atende. Por isso este arquivo nao mede aparencia. Ele mede o que, se
// ceder, transforma a Aquametria numa fazenda de conteudo:
//
//   1. A ORDEM DA VITRINE E IDENTICA A DA LISTA TECNICA, cartao por cartao. Se
//      um dia alguem ordenar por comissao, por preco ou por "quem tem foto",
//      este teste reprova.
//   2. O GRUPO DE CADA CARTAO E O MESMO DA LISTA TECNICA — e aqui o grupo e
//      OUTRO, nao o da C5. O nivel de alta exigencia tem a faixa ABERTA por
//      cima: a fonte aquarioturbinado publica "acima de 40 lm/L" e nao diz ate
//      onde. Entao existem dois grupos, "dentro do intervalo que as tres fontes
//      publicam" e "acima do teto da leitura mais alta". Ate a 1.2.0 o cartao
//      dizia "dentro da faixa de 40 a 60 lm/L" para TODO mundo, inclusive para
//      uma luminaria de 115 lm/L. O caso deste teste reproduz exatamente isso.
//   3. NENHUM PRODUTO SOME POR NAO TER FOTO OU LINK. Nesta calculadora isso e a
//      regra e nao a excecao: 13 das 15 luminarias do catalogo nao tem foto, e
//      as 8 que tem foto e nao entram sao as que nao declaram lumen.
//   4. O PRECO E SEMPRE COTACAO COM DATA, e bate com o banco.
//   5. A VITRINE VEM ANTES DA PROCEDENCIA no HTML (contrato 7).
//
// E mede as duas metades da pagina, porque elas falham por motivos diferentes:
// a vitrine SERVIDA com o JavaScript DESLIGADO (e o que um crawler de IA recebe)
// e a vitrine PINTADA com ele ligado (e o que o comprador ve).
//
// O teste nao guarda numero esperado nenhum: ele le AQM_C15_CATALOGO, que e o
// dado que o snippet embute, e confere a tela contra ele. A regua da faixa vem
// do TEXTO que a propria pagina publicou (o valor da faixa e a legenda de lm/L),
// nunca de uma copia da formula aqui dentro — teste que chama a regua de quem
// produziu o dado e um teste verde que nao mede nada (secao 8 do ARQUIPELAGO.md).
//
//   npm i --no-save playwright
//   php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
//   node ferramentas/teste-navegador-c15-vitrine.mjs /tmp/c15.html

import { chromium } from 'playwright';

const ARQUIVO = process.argv[2] || '/tmp/c15.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

// O caso do teste: aquario de 60 cm com 57,6 L de agua real, plantas de alta
// exigencia. Escolhido porque e o unico que produz os DOIS grupos de uma vez —
// a Aquarios do Rio de 2 400 lm cai dentro dos 40 a 60 lm/L, e a Ista IL-401, a
// Chihiros A601 e a WRGB II Pro 60 ficam acima do teto de 60 lm/L, a ultima
// delas entregando 115 lm/L. Era esta a lista que a 1.2.0 rotulava inteira como
// "dentro da faixa de 40 a 60 lm/L".
const VOLUME = '57,6';
const VOLUME_N = 57.6;
const COMPRIMENTO = '60';
const COMPRIMENTO_N = 60;
const NIVEL = 'alta';

// O caso da vitrine SERVIDA e propriedade do snippet, nao do teste: e o aquario
// de referencia de 90 cm que a pagina publica no HTML.
const COMPRIMENTO_SERVIDO = 90;

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

// Espelho do lm() da pagina, escrito AQUI e nao chamado de la: quem confere
// escreve a propria regua. Lumen e numero grosso — dezena ate 10 000, centena
// acima disso.
const lumens = (n) => {
  const passo = n >= 10000 ? 100 : 10;
  return br(Math.round(n / passo) * passo, 0);
};

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
  return Array.from(trilho.querySelectorAll('.aqm-c15-vt-item')).map((li) => {
    const cartao = li.querySelector('.aqm-c15-vt-cartao');
    const img = li.querySelector('.aqm-c15-vt-foto img');
    const t = (s) => {
      const n = li.querySelector(s);
      return n ? n.textContent.trim() : null;
    };
    return {
      tag: cartao ? cartao.tagName.toLowerCase() : null,
      href: cartao && cartao.tagName.toLowerCase() === 'a' ? cartao.getAttribute('href') : null,
      rel: cartao ? cartao.getAttribute('rel') : null,
      alvo: cartao ? cartao.getAttribute('target') : null,
      marca: t('.aqm-c15-vt-marca'),
      modelo: t('.aqm-c15-vt-modelo'),
      espec: t('.aqm-c15-vt-espec'),
      cobertura: t('.aqm-c15-vt-cobertura'),
      ressalva: t('.aqm-c15-vt-ressalva'),
      preco: t('.aqm-c15-vt-preco'),
      botao: t('.aqm-c15-vt-botao'),
      espera: t('.aqm-c15-vt-espera'),
      temFoto: !!img,
      imgSrc: img ? img.getAttribute('src') : null,
      imgAlt: img ? img.getAttribute('alt') : null,
      imgLazy: img ? img.getAttribute('loading') : null,
      placeholder: !!li.querySelector('.aqm-c15-vt-foto-vazia'),
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

const servidos = await semJs.evaluate(LER_TRILHO, '.aqm-c15-vitrine-servida .aqm-c15-vt-trilho');

conferir('a vitrine servida existe no HTML', Array.isArray(servidos) && servidos.length > 0,
  (servidos ? servidos.length : 0) + ' cartao(oes)');

if (servidos && servidos.length) {
  conferir('a vitrine servida tem pelo menos 3 cartoes (secao 7: de tres a cinco)',
    servidos.length >= 3, servidos.length + ' cartao(oes)');
  conferir('a vitrine servida para em 5 cartoes, como a pintada',
    servidos.length <= 5, servidos.length + ' cartao(oes)');

  const semEspec = servidos.filter((c) => !c.espec || !/^\d/.test(c.espec) || !/ lm — .* lm\/L, /.test(c.espec));
  conferir('todo cartao servido diz a especificacao que fez o produto entrar, em lumens e lm/L',
    semEspec.length === 0,
    semEspec.length ? semEspec.map((c) => c.modelo + ': ' + c.espec).join(' / ') : servidos[0].espec);

  const semCobertura = servidos.filter((c) => !c.cobertura
    || !c.cobertura.includes('o seu tem ' + br(COMPRIMENTO_SERVIDO, 0) + ' cm'));
  conferir('todo cartao servido diz a SEGUNDA condicao de elegibilidade: a cobertura declarada',
    semCobertura.length === 0,
    semCobertura.length ? semCobertura.map((c) => c.modelo + ': ' + c.cobertura).join(' / ') : servidos[0].cobertura);

  const semMarca = servidos.filter((c) => !c.marca);
  conferir('todo cartao servido tem linha de marca', semMarca.length === 0,
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
  conferir('o alt das imagens sai ACENTUADO, como todo texto de tela da ilha',
    comFoto.every((c) => /[áàâãéêíóôõúç]/i.test(c.imgAlt || '')),
    comFoto.map((c) => (c.imgAlt || '').slice(0, 40)).join(' / ') || 'nenhuma imagem neste caso');
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

// A pagina nao pode mais dizer que nao publica preco: ela publica, datado. A
// medicao e no CORPO, nunca no HTML completo — procurar a frase na pagina
// inteira acharia texto dentro de JSON-LD ou de comentario e passaria por
// motivo errado (secao 8 do ARQUIPELAGO.md).
const corpoServido = await semJs.evaluate(() => document.body.innerText);
conferir('a pagina NAO diz mais que nao publica preco (a vitrine publica, com data)',
  !/n[aã]o publicamos pre[çc]o/i.test(corpoServido),
  (corpoServido.match(/n[aã]o publicamos pre[çc]o/gi) || []).join(' / ') || 'nenhuma ocorrencia');
conferir('a pagina continua dizendo que NAO publica tarifa de energia (isso nao mudou)',
  /n[aã]o publicamos tarifa de energia/i.test(corpoServido), 'presente');

// Por que este aquario de referencia, dito na propria pagina: escolher o caso e
// calar o motivo seria colher cereja.
conferir('a vitrine servida explica por que o exemplo e este aquario, e nao um de 60 cm',
  /Por que o exemplo é um aquário grande e de alta exigência/.test(corpoServido),
  'justificativa publicada');

// A promessa e a ordem dos blocos no HTML servido.
const promessa = await semJs.$eval('.aqm-c15-promessa', (n) => n.textContent.trim()).catch(() => null);
conferir('a linha de promessa esta no topo, no HTML servido',
  !!promessa && promessa.length > 20, promessa || 'ausente');
conferir('a promessa nao tem tom de anuncio (sem exclamacao)',
  !!promessa && !/!/.test(promessa), promessa || 'ausente');

const promessaAntes = await semJs.evaluate(() => {
  const p = document.querySelector('.aqm-c15-promessa');
  const form = document.querySelector('#aqm-c15-form');
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
await pagina.fill('#aqm-c15-volume', VOLUME);
await pagina.fill('#aqm-c15-comprimento', COMPRIMENTO);
await pagina.selectOption('#aqm-c15-nivel', NIVEL);
await pagina.click('#aqm-c15-form button[type="submit"]');
await pagina.waitForSelector('#aqm-c15-vitrine:not(.aqm-c15-oculto)', { timeout: 5000 });

conferir('nenhum erro de script ao pintar a vitrine', erros.length === 0,
  erros.join(' | ') || 'console limpo');

const catalogo = await pagina.evaluate(() => window.AQM_C15_CATALOGO || null);
conferir('o catalogo embutido chegou ao navegador', Array.isArray(catalogo),
  (catalogo ? catalogo.length : 0) + ' luminaria(s)');

// A regra que nao pode ceder: comissao nao viaja para o snippet.
const chavesComissao = JSON.stringify(catalogo || []).match(/"[^"]*comiss[^"]*"/gi) || [];
conferir('nenhuma comissao viaja dentro do catalogo do snippet',
  chavesComissao.length === 0, chavesComissao.join(' / ') || 'nenhuma chave de comissao');

const pintados = await pagina.evaluate(LER_TRILHO, '#aqm-c15-vitrine-trilho');

// A lista tecnica: nome E grupo de cada item, na ordem do DOM.
const fichas = await pagina.$$eval('#aqm-c15-produtos-lista .aqm-c15-produto',
  (ns) => ns.map((n) => ({
    nome: n.querySelector('h4').textContent.trim().replace(/\s+/g, ' '),
    acima: n.classList.contains('aqm-c15-produto-acima'),
    regulavel: n.classList.contains('aqm-c15-produto-regulavel'),
    porque: n.querySelector('.aqm-c15-porque').textContent.replace(/\s+/g, ' ').trim(),
  })));

conferir('a vitrine pintada nao esta vazia', pintados && pintados.length > 0,
  (pintados ? pintados.length : 0) + ' cartao(oes)');
conferir('o caso do teste produz os DOIS grupos, que e o que ele existe para medir',
  fichas.some((f) => f.acima) && fichas.some((f) => !f.acima),
  fichas.filter((f) => !f.acima).length + ' dentro do intervalo publicado, '
    + fichas.filter((f) => f.acima).length + ' acima do teto da leitura mais alta');

// A faixa publicada e a legenda de lm/L, lidas do TEXTO da pagina, para o teste
// nao repetir a formula aqui dentro.
const faixa = await pagina.$eval('#aqm-c15-faixa-valor', (n) => n.textContent.trim());
const criterio = await pagina.$eval('#aqm-c15-faixa-criterio', (n) => n.textContent.trim());
console.log('  nota  faixa publicada nesta entrada: ' + faixa.replace(/\s+/g, ' '));

const lmL = criterio.match(/de (\d+) a (\d+)\+? lm\/L/);
conferir('a pagina publica a faixa de lm/L deste nivel, que e a regua dos cartoes',
  !!lmL, lmL ? lmL[1] + ' a ' + lmL[2] + ' lm/L' : criterio.slice(0, 80));
const pisoLmL = lmL ? lmL[1] : null;
const tetoLmL = lmL ? lmL[2] : null;

// ---- O portao central: a vitrine NAO reordena nada. -------------------------
const nomeVitrine = (c) => ((c.marca === 'sem marca declarada' ? '' : c.marca + ' ') + c.modelo)
  .replace(/\s+/g, ' ').trim();
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
  const vitrine = document.querySelector('#aqm-c15-vitrine');
  const ficha = document.querySelector('#aqm-c15-produtos-lista');
  if (!vitrine || !ficha) { return null; }
  return !!(vitrine.compareDocumentPosition(ficha) & Node.DOCUMENT_POSITION_FOLLOWING);
});
conferir('a vitrine vem ANTES da ficha e da procedencia no HTML (contrato 7)',
  vitrineAntes === true, String(vitrineAntes));

// ---- O portao do rotulo: o defeito que a 1.3.0 consertou. -------------------
if (pintados && pintados.length === fichas.length) {
  const grupoErrado = pintados
    .map((c, i) => ({ c, ficha: fichas[i] }))
    .filter(({ c, ficha }) => /acima dos .* da leitura mais alta/.test(c.espec) !== ficha.acima);
  conferir('CADA CARTAO DIZ O GRUPO EM QUE A LISTA TECNICA O POS, e nao outro',
    grupoErrado.length === 0,
    grupoErrado.length
      ? grupoErrado.map(({ c, ficha }) => nomeVitrine(c) + ': cartao diz '
          + (/acima dos .* da leitura mais alta/.test(c.espec) ? 'acima' : 'dentro')
          + ', a lista diz ' + (ficha.acima ? 'acima' : 'dentro')).join(' / ')
      : pintados.filter((c) => /da leitura mais alta/.test(c.espec)).length
          + ' acima do teto, o resto dentro do intervalo publicado');

  const dentroMentindo = pintados
    .map((c, i) => ({ c, ficha: fichas[i] }))
    .filter(({ c, ficha }) => ficha.acima && /dentro dos/.test(c.espec));
  conferir('NENHUM cartao acima do teto diz "dentro dos" (o defeito de rotulo da 1.2.0)',
    dentroMentindo.length === 0,
    dentroMentindo.map(({ c }) => nomeVitrine(c) + ': ' + c.espec).join(' / ') || 'nenhum');

  // E a mesma afirmacao do outro lado: a frase da FICHA tambem nao pode dizer
  // "dentro da faixa" para quem passou do teto. O defeito morava la, nao aqui.
  const fichaMentindo = fichas.filter((f) => f.acima && /fica dentro da faixa de/.test(f.porque));
  conferir('NENHUMA ficha de item acima do teto diz "fica dentro da faixa"',
    fichaMentindo.length === 0,
    fichaMentindo.map((f) => f.nome).join(' / ') || 'nenhuma');

  // O numero, e nao so o rotulo: quem esta acima do teto precisa MOSTRAR o lm/L
  // que entrega, senao o leitor nao tem como julgar o quanto acima ele esta.
  if (tetoLmL) {
    const semNumero = pintados
      .map((c, i) => ({ c, ficha: fichas[i] }))
      .filter(({ c, ficha }) => {
        if (!ficha.acima) { return false; }
        const m = c.espec.match(/([\d.,]+) lm\/L/);
        if (!m) { return true; }
        return parseFloat(m[1].replace(/\./g, '').replace(',', '.')) <= parseFloat(tetoLmL);
      });
    conferir('o cartao acima do teto mostra o lm/L que ele realmente entrega, e ele passa do teto publicado',
      semNumero.length === 0,
      semNumero.length ? semNumero.map(({ c }) => nomeVitrine(c) + ': ' + c.espec).join(' / ')
        : 'teto publicado: ' + tetoLmL + ' lm/L');
  }
}

// ---- Cada cartao contra o dado que o gerou. ---------------------------------
if (pintados && pintados.length && Array.isArray(catalogo)) {
  const porNome = {};
  catalogo.forEach((p) => {
    porNome[((p.marca ? p.marca + ' ' : '') + p.modelo).replace(/\s+/g, ' ').trim()] = p;
  });

  const semDado = pintados.filter((c) => !porNome[nomeVitrine(c)]);
  conferir('todo cartao da vitrine corresponde a um registro do catalogo',
    semDado.length === 0, semDado.map(nomeVitrine).join(' / ') || 'todos');

  const especErrada = pintados.filter((c, i) => {
    const p = porNome[nomeVitrine(c)];
    if (!p || !pisoLmL) { return true; }
    const valor = br(Math.round((p.fluxo_lm / VOLUME_N) * 10) / 10, 1);
    const cabeca = lumens(p.fluxo_lm) + ' lm — ' + valor + ' lm/L, ';
    const esperado = fichas[i] && fichas[i].acima
      ? cabeca + 'acima dos ' + tetoLmL + ' lm/L da leitura mais alta, na parte da faixa que a fonte deixou aberta'
      : cabeca + 'dentro dos ' + pisoLmL + ' a ' + tetoLmL + ' lm/L que este nível pede';
    return c.espec !== esperado;
  });
  conferir('a especificacao de cada cartao e o fluxo do banco com a faixa que a pagina publicou',
    especErrada.length === 0,
    especErrada.length ? especErrada.map((c) => c.espec).join(' / ') : pintados[0].espec);

  // A cobertura declarada e a SEGUNDA condicao de elegibilidade, e o cartao a
  // repete: a peca que nao cobre o vidro nao entra nem em ultimo lugar, e quem
  // so olha a vitrine merece ver esse criterio.
  const coberturaErrada = pintados.filter((c) => {
    const p = porNome[nomeVitrine(c)];
    if (!p) { return true; }
    const cobre = (p.aquario_min_cm === null || COMPRIMENTO_N >= p.aquario_min_cm)
      && (p.aquario_max_cm === null || COMPRIMENTO_N <= p.aquario_max_cm);
    return !cobre || !c.cobertura || !c.cobertura.includes('o seu tem ' + br(COMPRIMENTO_N, 0) + ' cm');
  });
  conferir('todo cartao cobre o comprimento do aquario segundo o banco, e diz isso',
    coberturaErrada.length === 0,
    coberturaErrada.map(nomeVitrine).join(' / ') || pintados[0].cobertura);

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

  // A ressalva nao pode sumir no cartao bonito: peca acima do teto e SEM
  // regulagem declarada nao tem como ser baixada ate o nivel escolhido.
  const ressalvaFaltando = pintados.filter((c, i) => {
    const p = porNome[nomeVitrine(c)];
    if (!p || !fichas[i] || !fichas[i].acima || p.regulagem) { return false; }
    return !c.ressalva || !/sem regulagem declarada/.test(c.ressalva);
  });
  conferir('cartao acima do teto e sem regulagem declarada diz isso, como a ficha diz',
    ressalvaFaltando.length === 0,
    ressalvaFaltando.map(nomeVitrine).join(' / ') ||
      pintados.filter((c) => c.ressalva).length + ' cartao(oes) com ressalva de regulagem');

  const esperando = pintados.filter((c) => c.tag !== 'a').length;
  console.log('  nota  ' + esperando + ' de ' + pintados.length +
    ' cartoes deste caso esperam link de afiliado');
  console.log('  nota  ' + pintados.filter((c) => c.temFoto).length + ' de ' + pintados.length +
    ' cartoes deste caso tem foto');
}

// ---- O carrossel e CSS puro, e rola. ---------------------------------------
const snap = await pagina.$eval('#aqm-c15-vitrine-trilho',
  (n) => getComputedStyle(n).scrollSnapType + ' | ' + getComputedStyle(n).overflowX);
conferir('o trilho tem scroll-snap em CSS puro e rola na horizontal',
  /x/.test(snap) && /auto|scroll/.test(snap), snap);

// ---- A vitrine some quando nao ha o que mostrar. ---------------------------
// Portao, nao defeito (secao 7): nenhuma luminaria do banco declara cobrir um
// aquario de 115 cm — as duas maiores comecam em 120 —, e a pagina precisa DIZER
// por que em vez de calar.
//
// O caso NAO e "60 cm no nivel medio", que foi a primeira tentativa e reprovou
// com razao: ali a lista fica sem ninguem DENTRO da faixa, mas ainda tem os
// regulaveis, que sao modelos acima do teto com dimmer declarado. Lista vazia de
// verdade e outra coisa, e e esta.
await pagina.fill('#aqm-c15-comprimento', '115');
await pagina.click('#aqm-c15-form button[type="submit"]');
await pagina.waitForTimeout(300);
const vazio = await pagina.evaluate(() => ({
  vitrine: document.querySelector('#aqm-c15-vitrine').classList.contains('aqm-c15-oculto'),
  bloco: document.querySelector('#aqm-c15-produtos').classList.contains('aqm-c15-oculto'),
  nada: document.querySelector('#aqm-c15-produtos-nada').textContent.trim(),
}));
conferir('sem item que atenda, a vitrine se esconde em vez de mostrar cartao vazio',
  vazio.vitrine === true && vazio.bloco === true, JSON.stringify(vazio).slice(0, 120));
conferir('e a pagina DIZ por que a lista esta vazia (silencio parece defeito)',
  vazio.nada.length > 80 && /Nenhuma luminária/.test(vazio.nada), vazio.nada.slice(0, 120) + '...');

/* ===================================================================== */
/* 3. Celular: barra fixa enquanto o resultado esta fora da tela          */
/* ===================================================================== */

console.log('\ncelular (390 x 720)');

const barraNoDesktop = await pagina.$eval('#aqm-c15-barra', (n) => getComputedStyle(n).display);
conferir('a barra fixa NAO aparece em tela larga', barraNoDesktop === 'none', barraNoDesktop);

await ctx.close();

const ctxCel = await navegador.newContext({ viewport: { width: 390, height: 720 } });
const cel = await ctxCel.newPage();
const errosCel = [];
cel.on('pageerror', (e) => errosCel.push(String(e)));

await cel.goto('file://' + ARQUIVO, { waitUntil: 'domcontentloaded' });
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.fill('#aqm-c15-volume', VOLUME);
await cel.fill('#aqm-c15-comprimento', COMPRIMENTO);
await cel.selectOption('#aqm-c15-nivel', NIVEL);
await cel.click('#aqm-c15-form button[type="submit"]');
await cel.waitForSelector('#aqm-c15-vitrine:not(.aqm-c15-oculto)', { timeout: 5000 });
await cel.waitForTimeout(700);

conferir('nenhum erro de script no celular', errosCel.length === 0,
  errosCel.join(' | ') || 'console limpo');

const rolou = await cel.evaluate(() => window.scrollY);
conferir('calcular rola a pagina ate o resultado', rolou > 0, 'scrollY = ' + rolou);

const resultadoAVista = await cel.evaluate(() => {
  const c = document.querySelector('#aqm-c15-saida').getBoundingClientRect();
  return c.top >= -5 && c.top < window.innerHeight;
});
conferir('depois da rolagem o resultado esta na tela', resultadoAVista === true, String(resultadoAVista));

// Sem rolagem horizontal a 390 px, com o trilho da vitrine na tela.
const rolagemH = await cel.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
conferir('nenhuma rolagem horizontal na pagina a 390 px', rolagemH <= 0, rolagemH + ' px');

// E a pagina medida tem o tamanho da pagina de verdade: render de bancada que
// serve metade mede 0 px de rolagem por nao ter o que estourar (secao 8).
const tamanho = await cel.evaluate(() => document.documentElement.outerHTML.length);
conferir('a pagina medida tem o tamanho da pagina real, e nao a metade',
  tamanho > 100000, Math.round(tamanho / 1024) + ' KB');

// Longe do resultado, a barra tem que aparecer.
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.waitForTimeout(600);
const barraNoTopo = await cel.$eval('#aqm-c15-barra',
  (n) => getComputedStyle(n).display + ' | ' + n.getAttribute('aria-hidden'));
conferir('com o resultado fora da tela, a barra do celular aparece',
  /flex/.test(barraNoTopo) && /false/.test(barraNoTopo), barraNoTopo);

const textoBarra = await cel.$eval('#aqm-c15-barra-texto', (n) => n.textContent.trim());
conferir('a barra do celular carrega a faixa calculada, nao um texto generico',
  / lm /.test(textoBarra) && textoBarra.includes(br(VOLUME_N, 1)), textoBarra);

// O botao dela leva ao resultado, e ai ela some.
await cel.click('#aqm-c15-barra-ir');
await cel.waitForTimeout(700);
const barraNoResultado = await cel.$eval('#aqm-c15-barra',
  (n) => getComputedStyle(n).display + ' | ' + n.getAttribute('aria-hidden'));
conferir('com o resultado a vista, a barra some',
  /none/.test(barraNoResultado) && /true/.test(barraNoResultado), barraNoResultado);

// Limpar tem que desligar a barra, senao ela fica prometendo um resultado morto.
await cel.click('#aqm-c15-limpar');
await cel.evaluate(() => window.scrollTo(0, 0));
await cel.waitForTimeout(500);
const barraDepoisDeLimpar = await cel.$eval('#aqm-c15-barra', (n) => getComputedStyle(n).display);
conferir('limpar o formulario desliga a barra', barraDepoisDeLimpar === 'none', barraDepoisDeLimpar);

await ctxCel.close();
await navegador.close();

console.log('\n' + (falhas === 0 ? 'TUDO OK' : falhas + ' FALHA(S)'));
process.exit(falhas === 0 ? 0 : 1);

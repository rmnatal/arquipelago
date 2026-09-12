// O portao da VITRINE da C12 (bloco T8, 11/09/2026).
//
// Copia o desenho do teste-navegador-c15-vitrine.mjs e mede o que so a C12 tem.
// A vitrine e o unico bloco da pagina que pode ficar bonito e errado ao mesmo
// tempo: ela mostra foto, preco e botao de loja, e essas tres coisas sao
// exatamente as que empurram uma pagina a vender o que paga mais em vez do que
// atende. Este arquivo nao mede aparencia. Ele mede:
//
//   1. A ORDEM DA VITRINE E IDENTICA A DA LISTA TECNICA, cartao por cartao.
//      Se um dia alguem ordenar por comissao, por preco ou por "quem tem foto",
//      este teste reprova.
//   2. O GRUPO DE CADA CARTAO E O MESMO DA LISTA TECNICA — e aqui o grupo e
//      OUTRO, nao o da C5 nem o da C15. Nesta calculadora nenhuma midia e
//      eliminada pelo volume do aquario; o que existe e uma midia que responde
//      METADE da pergunta. O Eheim SUBSTRAT pro entra pela area declarada e o
//      fabricante nao publica dosagem por litro nenhuma — e ele e uma das duas
//      midias COM link de loja. Um cartao com um numero ao lado do nome dele
//      faria o leitor achar que aquele numero e dele.
//   3. O RENDIMENTO DA EMBALAGEM E CONTA NOSSA, e nao o denominador da dose.
//      Foi o defeito que este bloco achou: a ficha dizia "uma embalagem atende
//      ate 200 L" para o Seachem Matrix, cuja embalagem de 1 L sao QUATRO doses
//      de 250 mL, enquanto a tabela servida da mesma pagina dizia 800 L.
//   4. NENHUMA MIDIA SOME POR NAO TER FOTO OU LINK (3 das 4 biologicas nao tem
//      foto; 2 das 4 nao tem link).
//   5. O PRECO E SEMPRE COTACAO COM DATA, e bate com o catalogo.
//   6. A VITRINE VEM ANTES DA PROCEDENCIA no HTML (contrato 7).
//
// E mede as duas metades da pagina, porque elas falham por motivos diferentes:
// a vitrine SERVIDA com o JavaScript DESLIGADO (e o que um crawler de IA
// recebe) e a vitrine PINTADA com ele ligado (e o que o comprador ve).
//
// A REGUA E DAQUI. O teste le AQM_C12_MIDIAS — o dado que o snippet embute — e
// recalcula sozinho mL, embalagens e rendimento. Ele nunca chama uma funcao da
// pagina para conferir o que a pagina publica: teste que chama a regua de quem
// produziu o dado e um teste verde que nao mede nada (secao 8 do ARQUIPELAGO.md).
//
// E VARRE A ENTRADA INTEIRA, nao o caso-ancora: os seis volumes da tabela mais
// as bordas de arredondamento de embalagem, porque ferramenta de entrada
// variavel serve uma resposta por consulta e amostra com nome de varredura e o
// mesmo defeito da grade que nao pisa na borda.
//
//   npm i --no-save playwright
//   php ferramentas/render-para-teste.php . aquametria_calculadora_midia > /tmp/c12.html
//   node ferramentas/teste-navegador-c12-vitrine.mjs /tmp/c12.html

import { chromium } from 'playwright';

const ARQUIVO = process.argv[2] || '/tmp/c12.html';
const URL = 'file://' + ARQUIVO;
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

// O aquario de referencia da vitrine SERVIDA e propriedade do snippet, nao do
// teste: e o de 60 L que a pagina publica no HTML, com o motivo escrito nela.
const VITRINE_SERVIDA_L = 60;

// A varredura. Os seis casos da tabela, as bordas de arredondamento de
// embalagem das tres midias dimensionadas (80/81 para a Ocean Tech, 200/201
// para a JBL, 800/801 para o Matrix) e os extremos aceitos pelo formulario.
const VOLUMES = [1, 30, 60, 79, 80, 81, 100, 150, 199, 200, 201, 300, 800, 801, 20000];

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

// Espelhos escritos AQUI, e nao chamados de la. Mililitro de midia e numero
// grosso (multiplo de 5 ate 1 L, de 25 mL acima disso) e litro ganha uma casa
// abaixo de 100.
const mLtexto = (n) => (n >= 1000
  ? br(Math.round(n / 25) * 25 / 1000, 2) + ' L'
  : br(Math.round(n / 5) * 5, 0) + ' mL');
const litros = (n) => (n >= 100 ? br(Math.round(n), 0) : br(Math.round(n * 10) / 10, 1));

function dataBr(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || ''));
  return m ? m[3] + '/' + m[2] + '/' + m[1] : String(iso);
}

// A leitura de um trilho de vitrine, servido ou pintado. Devolve so o que o
// teste julga — nunca o HTML inteiro, que mudaria a cada ajuste de estilo.
const LER_TRILHO = (seletor) => {
  const trilho = document.querySelector(seletor);
  if (!trilho) { return null; }
  return Array.from(trilho.querySelectorAll('.aqm-c12-vt-item')).map((li) => {
    const cartao = li.querySelector('.aqm-c12-vt-cartao');
    const img = li.querySelector('.aqm-c12-vt-foto img');
    const t = (s) => {
      const n = li.querySelector(s);
      return n ? n.textContent.trim() : null;
    };
    return {
      grupo: (li.className.match(/aqm-c12-vt-grupo-([a-z-]+)/) || [null, null])[1],
      tracejado: !!li.querySelector('.aqm-c12-vt-sem-dose'),
      tag: cartao ? cartao.tagName.toLowerCase() : null,
      href: cartao && cartao.tagName.toLowerCase() === 'a' ? cartao.getAttribute('href') : null,
      rel: cartao ? cartao.getAttribute('rel') : null,
      alvo: cartao ? cartao.getAttribute('target') : null,
      marca: t('.aqm-c12-vt-marca'),
      modelo: t('.aqm-c12-vt-modelo'),
      espec: t('.aqm-c12-vt-espec'),
      rende: t('.aqm-c12-vt-rende'),
      preco: t('.aqm-c12-vt-preco'),
      botao: t('.aqm-c12-vt-botao'),
      espera: t('.aqm-c12-vt-espera'),
      temFoto: !!img,
      imgAlt: img ? img.getAttribute('alt') : null,
      imgLazy: img ? img.getAttribute('loading') : null,
      placeholder: !!li.querySelector('.aqm-c12-vt-foto-vazia'),
    };
  });
};

// A lista TECNICA, que e o outro lado da comparacao. O grupo dela esta na
// classe aqm-c12-produto-sem, que existia antes desta versao.
const LER_LISTA = () => {
  const lista = document.querySelector('#aqm-c12-produtos-lista');
  if (!lista) { return null; }
  return Array.from(lista.querySelectorAll('.aqm-c12-produto')).map((li) => ({
    titulo: li.querySelector('h4') ? li.querySelector('h4').textContent.trim() : null,
    sem: li.classList.contains('aqm-c12-produto-sem'),
    ficha: Array.from(li.querySelectorAll('.aqm-c12-ficha li')).map((x) => x.textContent.trim()),
    porque: li.querySelector('.aqm-c12-porque') ? li.querySelector('.aqm-c12-porque').textContent.trim() : '',
  }));
};

// A sequencia ESPERADA, montada aqui a partir do catalogo: biologicas com
// dosagem na ordem do catalogo, depois a sem dosagem, e as quimicas so quando
// pedidas. Se o snippet mudar a ordem, esta e a linha que reprova.
function esperada(midias, comQuimica) {
  const bio = midias.filter((m) => m.tipo === 'biologica');
  const seq = bio.filter((m) => m.dose_mL_por_L !== null).map((m) => ({ m, grupo: 'dimensionada' }))
    .concat(bio.filter((m) => m.dose_mL_por_L === null).map((m) => ({ m, grupo: 'sem-dose' })));
  if (!comQuimica) { return seq; }
  return seq.concat(midias.filter((m) => m.tipo === 'quimica')
    .map((m) => ({ m, grupo: m.dose_mL_por_L === null ? 'sem-dose' : 'quimica' })));
}

const navegador = await chromium.launch({ executablePath: CHROME });

// O egresso do container barra fonts.googleapis.com, e cada page.goto() ficava
// esperando o timeout de 30 s por navegacao — com uma varredura de quinze
// volumes isso e um quarto de hora de espera por uma folha de estilo que nem
// entra no que este teste mede. Recusar de saida tudo que nao e o proprio
// arquivo deixa a varredura em segundos e, de quebra, prova que a pagina nao
// depende de recurso de terceiro para servir a vitrine.
async function semRedeExterna(ctx) {
  await ctx.route('**/*', (rota) => {
    const url = rota.request().url();
    if (url.startsWith('file://') || url.startsWith('data:') || url.startsWith('about:')) {
      return rota.continue();
    }
    return rota.abort();
  });
}

/* ---------------------------------------------------------------- SERVIDA */
// Com o JavaScript DESLIGADO: e o que o crawler recebe.
const ctxSemJs = await navegador.newContext({ javaScriptEnabled: false, viewport: { width: 1100, height: 900 } });
await semRedeExterna(ctxSemJs);
const semJs = await ctxSemJs.newPage();
await semJs.goto(URL);

console.log('\n1. a vitrine SERVIDA, com o JavaScript desligado');

const servida = await semJs.evaluate(LER_TRILHO, '.aqm-c12-vitrine-servida .aqm-c12-vt-trilho');
conferir('existe vitrine servida no HTML', Array.isArray(servida) && servida.length > 0,
  servida ? servida.length + ' cartoes' : 'nenhuma');

// O catalogo, lido do HTML servido (a variavel esta no script do rodape, que
// nao roda com o JS desligado — entao ela e extraida do texto).
const bruto = await semJs.evaluate(() => {
  const t = Array.from(document.querySelectorAll('script')).map((s) => s.textContent).join('\n');
  const i = t.indexOf('var AQM_C12_MIDIAS = ');
  if (i < 0) { return null; }
  const fim = t.indexOf(';\n', i);
  return t.slice(i + 'var AQM_C12_MIDIAS = '.length, fim);
});
const MIDIAS = JSON.parse(bruto);
conferir('o catalogo viaja dentro do snippet', Array.isArray(MIDIAS) && MIDIAS.length > 0,
  MIDIAS.length + ' midias');

const esperadaServida = esperada(MIDIAS, false);

conferir('a vitrine servida tem os mesmos cartoes, na mesma ordem',
  servida.length === esperadaServida.length
    && servida.every((c, i) => c.modelo === esperadaServida[i].m.modelo),
  servida.map((c) => c.modelo).join(' > '));

conferir('o grupo de cada cartao servido e o do catalogo',
  servida.every((c, i) => c.grupo === esperadaServida[i].grupo),
  servida.map((c) => c.grupo).join(', '));

// A regua do numero, escrita aqui.
esperadaServida.forEach((item, i) => {
  const c = servida[i];
  const m = item.m;
  if (item.grupo === 'dimensionada') {
    const alvo = m.dose_mL_por_L + ' mL/L'.replace('.', ',');
    const frase = br(m.dose_mL_por_L, 2) + ' mL/L — ' + mLtexto(m.dose_mL_por_L * VITRINE_SERVIDA_L)
      + ' nos seus ' + litros(VITRINE_SERVIDA_L) + ' L';
    conferir('servido: ' + m.modelo + ' diz a dose e a quantidade do aquario de referencia',
      c.espec === frase, c.espec);
    const embalagens = Math.ceil((m.dose_mL_por_L * VITRINE_SERVIDA_L) / (m.embalagem_L * 1000));
    const rende = m.embalagem_L * 1000 / m.dose_mL_por_L;
    const fraseRende = embalagens + (embalagens === 1 ? ' embalagem de ' : ' embalagens de ')
      + br(m.embalagem_L, 2) + ' L; cada uma rende até ' + litros(rende) + ' L nessa dosagem';
    conferir('servido: ' + m.modelo + ' diz quanto a EMBALAGEM rende, pela conta embalagem/dosagem',
      c.rende === fraseRende, c.rende);
    // A armadilha que este bloco achou: o rendimento NAO e o volume declarado.
    if (m.volume_max_L && Math.abs(rende - m.volume_max_L) > 0.5) {
      conferir('servido: ' + m.modelo + ' nao confunde o volume da DOSE com o da embalagem',
        c.rende.indexOf(litros(rende) + ' L') >= 0 && c.rende.indexOf('até ' + litros(m.volume_max_L) + ' L') < 0,
        'dose atende ' + m.volume_max_L + ' L, embalagem rende ' + rende + ' L');
    }
  } else {
    conferir('servido: ' + m.modelo + ' nao recebe numero nenhum, porque nao ha dosagem declarada',
      c.espec.indexOf('mL') < 0 && /não dimensiona/.test(c.rende), c.espec + ' / ' + c.rende);
    conferir('servido: ' + m.modelo + ' sai com a borda tracejada', c.tracejado === true);
  }

  // Foto e link nao decidem quem aparece.
  if (m.imagem && m.imagem.url) {
    conferir('servido: ' + m.modelo + ' serve a foto com alt e lazy',
      c.temFoto && c.imgAlt === m.imagem.alt && c.imgLazy === 'lazy', c.imgAlt);
  } else {
    conferir('servido: ' + m.modelo + ' sem foto fica com espaco reservado, e nao some',
      c.placeholder === true && c.temFoto === false);
  }

  if (m.link) {
    conferir('servido: ' + m.modelo + ' tem cartao ancora com sponsored',
      c.tag === 'a' && c.href === m.link && /sponsored/.test(c.rel) && /noopener/.test(c.rel) && c.alvo === '_blank',
      c.rel);
  } else {
    conferir('servido: ' + m.modelo + ' sem link nao vira ancora falsa',
      c.tag === 'div' && c.href === null && /link de loja em breve/.test(c.espera || ''));
  }

  if (m.preco) {
    conferir('servido: ' + m.modelo + ' publica cotacao COM data, nunca preco de hoje',
      c.preco.indexOf('R$ ' + br(m.preco.min, 2)) === 0
        && c.preco.indexOf('cotado em ' + dataBr(m.preco.coletado_em)) > 0,
      c.preco);
  } else {
    conferir('servido: ' + m.modelo + ' sem cotacao diz que nao tem', /sem cotação/.test(c.preco), c.preco);
  }
});

// Contrato 7: a compra vem antes da prova.
const ordemNoHtml = await semJs.evaluate(() => {
  const vitrine = document.querySelector('.aqm-c12-vitrine-servida');
  const fontes = Array.from(document.querySelectorAll('h3')).find((h) => /De onde vem cada n/.test(h.textContent));
  if (!vitrine || !fontes) { return null; }
  return (vitrine.compareDocumentPosition(fontes) & Node.DOCUMENT_POSITION_FOLLOWING) ? 'antes' : 'depois';
});
conferir('a vitrine servida vem ANTES da procedencia (contrato 7)', ordemNoHtml === 'antes', ordemNoHtml);

// O motivo do aquario de referencia esta publicado na propria pagina.
const motivo = await semJs.evaluate(() => {
  const p = Array.from(document.querySelectorAll('.aqm-c12-vitrine-servida .aqm-c12-criterio'))
    .map((x) => x.textContent).join(' ');
  return p;
});
conferir('a pagina publica POR QUE o aquario de referencia e esse',
  /Por que o exemplo/.test(motivo) && /teto físico/.test(motivo), motivo.slice(0, 90) + '…');
conferir('a pagina conta quantos cartoes tem link, em vez de calar',
  /de \d+ têm link de loja hoje/.test(motivo));

await ctxSemJs.close();

/* ---------------------------------------------------------------- PINTADA */
const ctx = await navegador.newContext({ viewport: { width: 1100, height: 900 } });
await semRedeExterna(ctx);
const page = await ctx.newPage();
const erros = [];
// Recurso de fora recusado pela rota acima NAO e erro da calculadora: e este
// teste barrando a folha do Google Fonts de proposito. O que continua contando
// e qualquer mensagem que a pagina produza sozinha.
page.on('console', (m) => {
  if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|FAILED)/.test(m.text())) { erros.push(m.text()); }
});
page.on('pageerror', (e) => erros.push('pageerror: ' + e.message));

// Uma navegacao so, e depois e o proprio formulario que muda de estado: cada
// goto extra e uma pagina inteira remontada para medir a mesma coisa.
await page.goto(URL);
await page.evaluate(() => { try { localStorage.clear(); } catch (e) { /* ignora */ } });

async function calcular(v, opts = {}) {
  await page.fill('#aqm-c12-volume', String(v).replace('.', ','));
  if (opts.quimica === false) { await page.uncheck('#aqm-c12-quimica'); }
  if (opts.quimica) { await page.check('#aqm-c12-quimica'); }
  await page.click('#aqm-c12-form button[type=submit]');
  await page.waitForTimeout(120);
}

console.log('\n2. a vitrine PINTADA, varrendo a entrada inteira (' + VOLUMES.length + ' volumes)');

for (const V of VOLUMES) {
  await calcular(V);
  const pintada = await page.evaluate(LER_TRILHO, '#aqm-c12-vitrine-trilho');
  const lista = await page.evaluate(LER_LISTA);
  const alvo = esperada(MIDIAS, false);

  conferir('V=' + V + ': a vitrine desenha a MESMA sequencia da lista tecnica',
    pintada.length === lista.length
      && pintada.every((c, i) => lista[i].titulo === (alvo[i].m.marca + ' ' + alvo[i].m.modelo)
        && c.modelo === alvo[i].m.modelo),
    pintada.map((c) => c.modelo).join(' > '));

  conferir('V=' + V + ': o grupo do cartao e o mesmo grupo da lista tecnica',
    pintada.every((c, i) => (c.grupo === 'sem-dose') === lista[i].sem),
    pintada.map((c) => c.grupo).join(', '));

  alvo.forEach((item, i) => {
    const m = item.m;
    const c = pintada[i];
    if (item.grupo !== 'dimensionada') { return; }
    const frase = br(m.dose_mL_por_L, 2) + ' mL/L — ' + mLtexto(m.dose_mL_por_L * V)
      + ' nos seus ' + litros(V) + ' L';
    if (c.espec !== frase) {
      nok('V=' + V + ': ' + m.modelo + ' — a quantidade do cartao bate com a regua deste teste', c.espec + ' != ' + frase);
    }
    const embalagens = Math.ceil((m.dose_mL_por_L * V) / (m.embalagem_L * 1000));
    if (c.rende.indexOf(embalagens + (embalagens === 1 ? ' embalagem' : ' embalagens')) !== 0) {
      nok('V=' + V + ': ' + m.modelo + ' — o numero de embalagens bate com o ceil deste teste', c.rende);
    }
  });
  ok('V=' + V + ': quantidade e embalagens de cada cartao conferem com a regua propria');
}

console.log('\n3. a midia que a pagina NAO dimensiona');
await calcular(100);
const pintada100 = await page.evaluate(LER_TRILHO, '#aqm-c12-vitrine-trilho');
const lista100 = await page.evaluate(LER_LISTA);
const semDose = pintada100.filter((c) => c.grupo === 'sem-dose');
conferir('existe exatamente uma midia biologica sem dosagem declarada', semDose.length === 1,
  semDose.map((c) => c.modelo).join(', '));
conferir('o cartao dela nao publica nenhum numero em mL',
  semDose.every((c) => c.espec.indexOf('mL') < 0), semDose[0] && semDose[0].espec);
conferir('e ela tem link de loja — o cartao com botao e justamente o que nao tem numero',
  semDose[0] && semDose[0].tag === 'a', semDose[0] && semDose[0].href);

console.log('\n4. a ficha da lista tecnica separa a DECLARACAO da conta nossa');
const matrix = MIDIAS.find((m) => m.id === 'seachem-matrix-1l');
const fichaMatrix = lista100.find((x) => x.titulo.indexOf('Matrix') >= 0).ficha.join(' | ');
const rendeMatrix = matrix.embalagem_L * 1000 / matrix.dose_mL_por_L;
conferir('a ficha diz o que o FABRICANTE declara, com a quantidade que ele nomeia',
  fichaMatrix.indexOf('O fabricante declara que ' + matrix.dose_texto + ' atendem até ' + litros(matrix.volume_max_L) + ' L') >= 0,
  matrix.dose_texto + ' / ' + matrix.volume_max_L + ' L');
conferir('a ficha diz, em outra linha, quanto a EMBALAGEM rende — e marca como conta nossa',
  fichaMatrix.indexOf('rende até ' + litros(rendeMatrix) + ' L') >= 0 && /conta nossa/.test(fichaMatrix),
  'embalagem de ' + matrix.embalagem_L + ' L rende ' + rendeMatrix + ' L');
conferir('e a ficha NAO chama os ' + matrix.volume_max_L + ' L da dose de "uma embalagem atende"',
  !/Uma embalagem atende, pela declaração do fabricante/.test(fichaMatrix));

console.log('\n5. a camada quimica so entra quando o leitor pede');
await calcular(100, { quimica: true });
const comQuimica = await page.evaluate(LER_TRILHO, '#aqm-c12-vitrine-trilho');
const alvoQ = esperada(MIDIAS, true);
conferir('com a quimica pedida, a vitrine ganha os cartoes quimicos no fim',
  comQuimica.length === alvoQ.length && comQuimica.every((c, i) => c.modelo === alvoQ[i].m.modelo),
  comQuimica.map((c) => c.modelo).join(' > '));
conferir('o cartao quimico diz que nao substitui a biologica',
  comQuimica.filter((c) => c.grupo === 'quimica').every((c) => /não substitui a biológica/.test(c.rende)),
  comQuimica.filter((c) => c.grupo === 'quimica').length + ' cartoes quimicos');

console.log('\n6. a vitrine pintada vem antes da lista tecnica, e o console fica limpo');
const ordemPintada = await page.evaluate(() => {
  const v = document.querySelector('#aqm-c12-vitrine');
  const l = document.querySelector('#aqm-c12-produtos-lista');
  return (v.compareDocumentPosition(l) & Node.DOCUMENT_POSITION_FOLLOWING) ? 'antes' : 'depois';
});
conferir('a vitrine pintada vem ANTES da lista tecnica e da procedencia', ordemPintada === 'antes', ordemPintada);
conferir('console sem mensagem', erros.length === 0, erros.join(' | '));

console.log('\n7. celular de 390 px sem rolagem horizontal');
const ctxCel = await navegador.newContext({ viewport: { width: 390, height: 780 } });
await semRedeExterna(ctxCel);
const cel = await ctxCel.newPage();
await cel.goto(URL);
await cel.fill('#aqm-c12-volume', '100');
await cel.click('#aqm-c12-form button[type=submit]');
await cel.waitForTimeout(150);
const rolagem = await cel.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
conferir('sem rolagem horizontal a 390 px', rolagem <= 0, rolagem + ' px');
await ctxCel.close();

await navegador.close();

console.log('\n' + (falhas === 0 ? 'TUDO OK' : falhas + ' FALHA(S)'));
process.exit(falhas === 0 ? 0 : 1);

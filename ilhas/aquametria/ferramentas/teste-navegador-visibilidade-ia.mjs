// Mede, num Chromium de verdade, o que a Sentinela Tecnica mediu a mao em
// 09/09/2026 e encontrou ZERO em 13 de 13 paginas: se a pagina serve algo
// citavel por um modelo de linguagem, ou so um formulario vazio.
//
// A regra de primeira classe do projeto diz que toda pagina de ferramenta
// precisa de (a) JSON-LD, (b) tabela de exemplos PRE-RENDERIZADA no HTML e
// (c) resposta antes da explicacao. Ate hoje isso era conferido por leitura.
// Leitura nao roda de novo na proxima sessao; este arquivo roda.
//
// O ponto que faz este teste valer: ele le a pagina com o JAVASCRIPT
// DESLIGADO. E o que um crawler de IA que nao executa script recebe, e e a
// unica forma honesta de provar que os numeros estao no HTML servido e nao
// foram desenhados pela calculadora depois.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-para-teste.php . aquametria_calculadora_vazao > /tmp/c3.html
//   php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor > /tmp/c5.html
//   node ferramentas/teste-navegador-visibilidade-ia.mjs /tmp

import { chromium } from 'playwright';

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

// Os seis volumes que a fila manda cobrir. Nao e uma escolha estetica: e a
// faixa de uso real do comercio brasileiro, do nano ao aquario de sala.
const VOLUMES = ['30', '60', '100', '150', '200', '300'];

const CASOS = [
  {
    codigo: 'C3', arquivo: 'c3.html', prefixo: 'aqm-c3',
    // O numero que a calculadora devolve para 100 L comunitario. Se a tabela
    // pre-renderizada nao disser a mesma coisa, uma das duas esta mentindo.
    ancora: '180 a 1.000',
    nomeApp: /vaz[aã]o/i,
  },
  {
    codigo: 'C5', arquivo: 'c5.html', prefixo: 'aqm-c5',
    ancora: '100 a 150',
    nomeApp: /aquecedor/i,
  },
];

let falhas = 0;
function ok(m, extra)  { console.log('  ok    ' + m + (extra ? ' — ' + extra : '')); }
function ruim(m, extra) { falhas++; console.log('  FALHA ' + m + (extra ? ' — ' + extra : '')); }
function conferir(cond, m, extra) { cond ? ok(m, extra) : ruim(m, extra); }

const navegador = await chromium.launch({ executablePath: CHROME });

for (const caso of CASOS) {
  console.log('\n' + caso.codigo + ' — ' + caso.arquivo + '  (JavaScript DESLIGADO)');

  // javaScriptEnabled:false e o coracao do teste. Com script ligado, qualquer
  // numero na tela pode ter sido desenhado pela calculadora.
  const ctx = await navegador.newContext({ javaScriptEnabled: false });
  const pagina = await ctx.newPage();
  await pagina.goto('file://' + DIR + '/' + caso.arquivo);

  // ---------------------------------------------------------------- JSON-LD
  const blocos = await pagina.$$eval('script[type="application/ld+json"]', ns => ns.map(n => n.textContent));
  conferir(blocos.length >= 1, 'a pagina serve JSON-LD', blocos.length + ' bloco(s)');

  let grafo = [];
  for (const b of blocos) {
    try { const d = JSON.parse(b); grafo = grafo.concat(d['@graph'] || [d]); }
    catch (e) { ruim('JSON-LD invalido', String(e).slice(0, 120)); }
  }
  conferir(grafo.length > 0, 'todo bloco de JSON-LD faz parse', grafo.length + ' no(s)');

  const app = grafo.find(n => n['@type'] === 'WebApplication');
  conferir(!!app, 'existe um no WebApplication');
  if (app) {
    conferir(caso.nomeApp.test(app.name || ''), 'o WebApplication tem nome desta calculadora', app.name);
    conferir(!!app.applicationCategory, 'WebApplication declara applicationCategory', app.applicationCategory);
    conferir(app.isAccessibleForFree === true, 'WebApplication declara isAccessibleForFree');
    conferir(Array.isArray(app.featureList) && app.featureList.length >= 4,
      'WebApplication tem featureList', (app.featureList || []).length + ' itens');
    conferir(!!app.publisher && !!app.publisher.name, 'WebApplication nomeia o publisher',
      app.publisher && app.publisher.name);
  }

  const faq = grafo.find(n => n['@type'] === 'FAQPage');
  conferir(!!faq, 'existe um no FAQPage');
  if (faq) {
    const qs = faq.mainEntity || [];
    conferir(qs.length >= 6, 'o FAQPage traz ao menos seis perguntas', qs.length + ' perguntas');
    const vazias = qs.filter(q => !q.acceptedAnswer || !(q.acceptedAnswer.text || '').trim());
    conferir(vazias.length === 0, 'toda pergunta do FAQPage tem resposta com texto');
    const curtas = qs.filter(q => (q.acceptedAnswer.text || '').length < 120);
    conferir(curtas.length === 0, 'nenhuma resposta do FAQPage e curta demais para ser citada',
      'menor resposta: ' + Math.min(...qs.map(q => q.acceptedAnswer.text.length)) + ' caracteres');
    // A regra que impede FAQPage-lixo: a resposta tem de existir na PAGINA.
    const semNumero = qs.filter(q => !/\d/.test(q.acceptedAnswer.text));
    conferir(semNumero.length === 0, 'toda resposta do FAQPage carrega numero');
  }

  // ------------------------------------------ tabela de exemplos no HTML
  const tabela = await pagina.$('.' + caso.prefixo + '-exemplos table');
  conferir(!!tabela, 'a tabela de exemplos existe no HTML servido');

  if (tabela) {
    const texto = await tabela.innerText();
    const faltando = VOLUMES.filter(v => !new RegExp('(^|[^\\d.])' + v + ' L').test(texto));
    conferir(faltando.length === 0, 'a tabela cobre 30, 60, 100, 150, 200 e 300 L',
      faltando.length ? 'faltam: ' + faltando.join(', ') : VOLUMES.length + ' volumes');

    const linhas = await tabela.$$eval('tr', ns => ns.length);
    conferir(linhas >= 7, 'a tabela tem cabecalho mais seis linhas', linhas + ' linhas');

    conferir(texto.includes(caso.ancora),
      'o numero da tabela bate com o que a calculadora devolve para 100 L', caso.ancora);

    // -------------------------------- a coluna de produto (bloco 4c, 09/09/2026)
    // Pedido do Raphael: a tabela pre-renderizada tem de dizer QUAL produto
    // atende cada faixa, senao ela responde ao leitor e nao responde ao
    // comprador. Com o script desligado, essa coluna e a UNICA recomendacao de
    // compra que a pagina serve — se ela sumir, ninguem percebe pela tela.
    const ultimaColuna = await tabela.$$eval('tr td:last-child',
      ns => ns.map(n => n.innerText.trim()));
    conferir(ultimaColuna.length === 6, 'a coluna de produto tem uma celula por volume',
      ultimaColuna.length + ' celulas');

    const mudas = ultimaColuna.filter(t => t.length < 20);
    conferir(mudas.length === 0,
      'nenhuma celula de produto sai muda: ou nomeia um modelo ou escreve por que esta vazia',
      mudas.length ? mudas.length + ' celula(s) mudas' : ultimaColuna.length + ' com texto');

    // Link de afiliado dentro da tabela obedece as mesmas regras do cartao.
    const links = await tabela.$$eval('a[href]', ns => ns.map(n => ({
      href: n.getAttribute('href'),
      rel: n.getAttribute('rel') || '',
      alvo: n.getAttribute('target') || '',
      texto: n.innerText.trim(),
    })));
    const errados = links.filter(l => !/\bsponsored\b/.test(l.rel)
      || !/\bnoopener\b/.test(l.rel) || l.alvo !== '_blank');
    conferir(errados.length === 0,
      'todo link da tabela e sponsored, noopener e abre em aba nova',
      errados.length ? errados.map(l => l.texto + ' [rel=' + l.rel + ']').join('; ')
        : links.length + ' link(s)');
    conferir(links.every(l => l.texto.length > 0),
      'nenhum link da tabela e um alvo sem texto (leitor de tela e teclado)');

    // O aviso de comissao tem de estar visivel JUNTO da tabela, nao so no
    // bloco de resultado que o script pinta depois.
    const aviso = await pagina.$('.' + caso.prefixo + '-exemplos .' + caso.prefixo + '-aviso-afiliado');
    conferir(!!aviso, 'a tabela carrega o aviso de publicidade dela');
    if (aviso) {
      const t = await aviso.innerText();
      conferir(/comiss/i.test(t), 'o aviso da tabela diz a palavra comissao');
      conferir(/pre[cç]o/i.test(t), 'o aviso da tabela explica por que nao publica preco');
    }
  }

  // ------------------------------------- resposta antes da explicacao
  const direta = await pagina.$('.' + caso.prefixo + '-direta');
  conferir(!!direta, 'existe o bloco de resposta direta no topo');

  if (direta) {
    const t = await direta.innerText();
    conferir(/\d/.test(t), 'a resposta direta carrega numero, nao so promessa');
    conferir(t.length >= 400, 'a resposta direta tem corpo suficiente para ser citada',
      t.length + ' caracteres');
    // Procedencia DENTRO da frase: fonte nomeada e data na mesma passagem.
    conferir(/\d{2}\/\d{2}\/\d{4}/.test(t), 'a resposta direta traz data de verificacao');

    // Vem ANTES do formulario? Um modelo le de cima para baixo.
    const ordem = await pagina.evaluate(p => {
      const d = document.querySelector('.' + p + '-direta');
      const f = document.querySelector('form');
      if (!d || !f) { return null; }
      return (d.compareDocumentPosition(f) & Node.DOCUMENT_POSITION_FOLLOWING) ? 'antes' : 'depois';
    }, caso.prefixo);
    conferir(ordem === 'antes', 'a resposta vem antes do formulario no HTML', ordem);
  }

  // ---------------------------------- e o que a pagina NAO pode ter feito
  // Com o script desligado, o container de resultado tem de continuar oculto:
  // se algum numero de resultado vazasse para o HTML servido, seria numero
  // sem entrada, e isso e pior que formulario vazio.
  const saida = await pagina.$('#' + caso.prefixo + '-saida');
  if (saida) {
    const oculto = await saida.evaluate(n => n.className.indexOf('-oculto') !== -1);
    conferir(oculto, 'o resultado da calculadora continua oculto sem JavaScript');
  }

  await ctx.close();
}

await navegador.close();

console.log('');
if (falhas) { console.log('=== ' + falhas + ' FALHA(S) ==='); process.exit(1); }
console.log('=== tudo passou ===');

// Mede, num Chromium de verdade e com o JAVASCRIPT DESLIGADO, se os tres
// artigos-ancora da ilha servem algo citavel por um modelo de linguagem.
//
// E o irmao do teste-navegador-visibilidade-ia.mjs, que mede as calculadoras.
// Precisou ser outro arquivo porque artigo nao e calculadora em tres pontos
// que importam:
//
//   - artigo nao tem formulario nem WebApplication: o no e Article;
//   - a tabela pre-renderizada do artigo e a tabela QUE ELE JA TINHA, escrita em
//     Markdown. Nao se inventa tabela para passar num portao — tabela decorativa
//     e pior que nenhuma;
//   - o eixo da tabela nao e comparavel entre os tres (linha comercial de
//     aquecedor, dosagem de midia, regua de lm/L), entao exigir os mesmos seis
//     degraus seria reprovar artigo por estar certo.
//
// O QUE ELE AFIRMA, e por que assim: a promessa, nunca o estado. Nao ha um
// numero esperado gravado aqui dentro. As duas asercoes que valem o arquivo sao
// de COERENCIA entre duas metades da mesma pagina:
//
//   (1) todo numero da resposta direta existe no corpo do artigo;
//   (2) toda resposta do FAQPage carrega ao menos um numero que existe no corpo.
//
// Mudar um numero do artigo com fonte melhor nao reprova nada — desde que o
// bloco do topo e o FAQ mudem junto, que e exatamente o defeito que este teste
// existe para pegar. Quatro asercoes venceram sozinhas nesta ilha por afirmarem
// estado; nenhuma aqui afirma.
//
//   npm i --no-save playwright@1.56.1
//   php ferramentas/render-artigo-para-teste.php . <slug> > /tmp/art-<codigo>.html
//   node ferramentas/teste-navegador-artigos.mjs /tmp

import { chromium } from 'playwright';

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const CASOS = [
  { codigo: 'C5',  arquivo: 'art-c5.html',  slug: 'quantos-watts-de-aquecedor-para-aquario' },
  { codigo: 'C12', arquivo: 'art-c12.html', slug: 'quanta-midia-biologica-o-aquario-precisa' },
  { codigo: 'C15', arquivo: 'art-c15.html', slug: 'quantos-lumens-por-litro-aquario-plantado' },
];

let falhas = 0;
const ok   = (m, e) => console.log('  ok    ' + m + (e ? ' — ' + e : ''));
const ruim = (m, e) => { falhas++; console.log('  FALHA ' + m + (e ? ' — ' + e : '')); };
const conferir = (c, m, e) => (c ? ok(m, e) : ruim(m, e));

// O corpus dos artigos escreve milhar com espaco fino ("6 630 lm", "1 000
// lumens") e o registro do snippet escreve com ponto. Sao o MESMO numero: sem
// normalizar, a comparacao reprovaria por tipografia, que e ruido.
function normalizar(t) {
  let s = String(t).replace(/[   ]/g, ' ');
  for (let i = 0; i < 3; i++) {
    s = s.replace(/(\d) (\d{3})(?!\d)/g, '$1.$2');
  }
  return s;
}

// Data nao e numero de conteudo: 04/09/2026 e procedencia, e nao precisa (nem
// deve) aparecer no corpo. Sai antes da extracao.
function numeros(t) {
  const s = normalizar(t).replace(/\b\d{1,2}\/\d{2}\/\d{4}\b/g, ' ');
  return new Set((s.match(/\d+(?:[.,]\d+)*/g) || []));
}

const navegador = await chromium.launch({ executablePath: CHROME });

for (const caso of CASOS) {
  console.log('\n' + caso.codigo + ' — ' + caso.arquivo + '  (JavaScript DESLIGADO)');

  const ctx = await navegador.newContext({ javaScriptEnabled: false });
  const pagina = await ctx.newPage();
  await pagina.goto('file://' + DIR + '/' + caso.arquivo);

  // -------------------------------------------------------------- JSON-LD
  const blocos = await pagina.$$eval('script[type="application/ld+json"]', ns => ns.map(n => n.textContent));
  conferir(blocos.length >= 1, 'a pagina serve JSON-LD', blocos.length + ' bloco(s)');

  let grafo = [];
  for (const b of blocos) {
    try { const d = JSON.parse(b); grafo = grafo.concat(d['@graph'] || [d]); }
    catch (e) { ruim('JSON-LD invalido', String(e).slice(0, 120)); }
  }
  conferir(grafo.length > 0, 'todo bloco de JSON-LD faz parse', grafo.length + ' no(s)');

  const art = grafo.find(n => n['@type'] === 'Article');
  conferir(!!art, 'existe um no Article');
  if (art) {
    conferir(!!art.headline, 'o Article tem headline', art.headline);
    // O limite de 110 caracteres e do proprio schema.org para headline. O titulo
    // longo do artigo continua declarado, em alternativeHeadline.
    conferir((art.headline || '').length <= 110, 'a headline cabe no limite do schema',
      (art.headline || '').length + ' caracteres');
    conferir(!!art.alternativeHeadline, 'o titulo completo fica em alternativeHeadline');
    conferir((art.description || '').length >= 80, 'o Article tem description com corpo',
      (art.description || '').length + ' caracteres');
    conferir(art.inLanguage === 'pt-BR', 'o Article declara o idioma', art.inLanguage);
    conferir(/^\d{4}-\d{2}-\d{2}$/.test(art.datePublished || ''), 'o Article declara datePublished', art.datePublished);
    conferir(/^\d{4}-\d{2}-\d{2}$/.test(art.dateModified || ''), 'o Article declara dateModified', art.dateModified);
    conferir(!!(art.author && art.author.name), 'o Article nomeia o autor', art.author && art.author.name);
    conferir(!!(art.publisher && art.publisher.name), 'o Article nomeia o publisher', art.publisher && art.publisher.name);
    conferir(!!art.keywords, 'o Article declara a consulta que mira', art.keywords);
    // Procedencia e a diferenca entre esta ilha e uma fazenda de conteudo: as
    // fontes que sustentam o texto sao declaradas, nao subentendidas.
    conferir(Array.isArray(art.citation) && art.citation.length >= 3,
      'o Article cita as fontes que sustentam o texto', (art.citation || []).length + ' fontes');
    const semData = (art.citation || []).filter(c => !/\d{2}\/\d{2}\/\d{4}/.test(String(c)));
    conferir(semData.length === 0, 'toda fonte citada leva data',
      semData.length ? semData.length + ' sem data' : 'todas datadas');
  }

  // -------------------------------------------------------------- FAQPage
  const faq = grafo.find(n => n['@type'] === 'FAQPage');
  conferir(!!faq, 'existe um no FAQPage');
  let respostas = [];
  if (faq) {
    const qs = faq.mainEntity || [];
    respostas = qs.map(q => (q.acceptedAnswer && q.acceptedAnswer.text) || '');
    conferir(qs.length >= 6, 'o FAQPage traz ao menos seis perguntas', qs.length + ' perguntas');
    conferir(respostas.every(t => t.trim()), 'toda pergunta do FAQPage tem resposta com texto');
    const curtas = respostas.filter(t => t.length < 120);
    conferir(curtas.length === 0, 'nenhuma resposta do FAQPage e curta demais para ser citada',
      'menor resposta: ' + Math.min(...respostas.map(t => t.length)) + ' caracteres');
    conferir(respostas.every(t => /\d/.test(t)), 'toda resposta do FAQPage carrega numero');
    const perguntas = qs.map(q => q.name || '');
    conferir(perguntas.every(p => /\?$/.test(p.trim())), 'toda pergunta do FAQPage e uma pergunta de verdade');
  }

  // ------------------------------------- resposta antes da explicacao
  const direta = await pagina.$('.aqm-art-direta');
  conferir(!!direta, 'existe o bloco de resposta direta no topo');

  let textoDireta = '';
  if (direta) {
    textoDireta = await direta.innerText();
    conferir(/\d/.test(textoDireta), 'a resposta direta carrega numero, nao so promessa');
    conferir(textoDireta.length >= 700, 'a resposta direta tem corpo suficiente para ser citada',
      textoDireta.length + ' caracteres');
    conferir(/\d{2}\/\d{2}\/\d{4}/.test(textoDireta), 'a resposta direta traz data de verificacao');
    // Fonte nomeada DENTRO da frase: sem isso a frase citada fora de contexto
    // vira afirmacao sem dono, que e o que este projeto recusa publicar.
    conferir(/(ReefFlow|Seachem|Chihiros|Eheim|JBL|Ocean Tech|peixeseaquarismo)/.test(textoDireta),
      'a resposta direta nomeia a fonte dentro da frase');

    // Vem ANTES da explicacao? Um modelo le de cima para baixo, e o primeiro
    // titulo de secao marca onde a explicacao comeca.
    const ordem = await pagina.evaluate(() => {
      const d = document.querySelector('.aqm-art-direta');
      const h = document.querySelector('h2');
      if (!d || !h) { return null; }
      return (d.compareDocumentPosition(h) & Node.DOCUMENT_POSITION_FOLLOWING) ? 'antes' : 'depois';
    });
    conferir(ordem === 'antes', 'a resposta direta vem antes do primeiro titulo de secao', ordem);

    // Links de verdade, nao span com aparencia de link.
    const links = await direta.$$eval('a[href]', ns => ns.map(n => ({ href: n.getAttribute('href'), texto: n.innerText.trim() })));
    conferir(links.length >= 2, 'a resposta direta linka a ferramenta e o metodo', links.length + ' link(s)');
    conferir(links.every(l => l.texto.length > 0), 'nenhum link da resposta direta e alvo sem texto');
    conferir(links.some(l => /metodologia/.test(l.href)), 'a resposta direta linka a metodologia');
  }

  // ------------------------------- a tabela que o artigo ja tinha, no HTML
  // Nao se exige tabela NOVA: exige-se que o artigo continue servindo, no HTML,
  // a tabela de numeros que e o motivo de ele existir.
  const tabelas = await pagina.$$eval('table', ns => ns.map(n => ({
    linhas: n.querySelectorAll('tr').length,
    dentroDaDireta: !!n.closest('.aqm-art-direta'),
    texto: n.innerText,
  })));
  const proprias = tabelas.filter(t => !t.dentroDaDireta);
  conferir(proprias.length >= 1, 'o artigo serve tabela de numeros no HTML', proprias.length + ' tabela(s)');
  conferir(proprias.some(t => t.linhas >= 4), 'ao menos uma tabela tem cabecalho e tres linhas',
    proprias.map(t => t.linhas).join(', ') + ' linhas');
  conferir(proprias.every(t => /\d/.test(t.texto)), 'nenhuma tabela servida sai sem numero');

  // ------------------------------------------- coerencia entre as metades
  const corpo = await pagina.evaluate(() => {
    const d = document.querySelector('.aqm-art-direta');
    if (d) { d.remove(); }
    return document.body.innerText;
  });
  const doCorpo = numeros(corpo);

  if (textoDireta) {
    const faltando = [...numeros(textoDireta)].filter(n => !doCorpo.has(n));
    conferir(faltando.length === 0,
      'todo numero da resposta direta existe no corpo do artigo',
      faltando.length ? 'sem lastro: ' + faltando.join(', ') : numeros(textoDireta).size + ' numeros com lastro');
  }

  if (respostas.length) {
    const orfas = respostas.filter(t => ![...numeros(t)].some(n => doCorpo.has(n)));
    conferir(orfas.length === 0,
      'toda resposta do FAQPage tem ao menos um numero que o corpo do artigo sustenta',
      orfas.length ? orfas.length + ' resposta(s) sem lastro' : respostas.length + ' respostas com lastro');
  }

  // ------------------------------------------------ o portao das entidades
  // A regra da secao 8 do contrato: contar &#038; SO dentro de <script>. Contar
  // na pagina inteira e teste ERRADO — a casca do tema tem dezenas de ocorrencias
  // legitimas.
  const escapadas = blocos.reduce((n, b) => n + (b.match(/&#\d+;/g) || []).length, 0);
  conferir(escapadas === 0, 'zero entidade numerica dentro dos blocos de script', escapadas + ' ocorrencia(s)');

  await ctx.close();
}

await navegador.close();
console.log('\n' + (falhas ? falhas + ' falha(s)' : 'tudo passou'));
process.exit(falhas ? 1 : 0);

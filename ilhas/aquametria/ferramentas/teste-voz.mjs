// O PORTÃO DA VOZ — mede o que as quatro páginas da casca SERVEM.
//
//   node ferramentas/teste-voz.mjs .
//
// Nasceu do despacho do Raphael de 11/09/2026 (seção 15 do ARQUIPELAGO.md):
// "abrir a home e nenhum termo da lista Proibidas do VOZ.md aparecer em título
// ou primeiro parágrafo". Isso é uma afirmação sobre o que a página DIZ, e as
// cicatrizes da seção 8 dizem exatamente como se mede uma dessas:
//
//   1. QUEM CONFERE ESCREVE A PRÓPRIA RÉGUA. A lista de termos está AQUI, neste
//      arquivo, escrita à mão a partir do VOZ.md. Ela não é importada do snippet
//      nem de um JSON que o snippet também leia — se as duas metades lessem a
//      mesma lista, apagar um termo dela faria as duas errarem juntas e o teste
//      continuaria verde.
//   2. AFIRMAÇÃO SOBRE O QUE A PÁGINA DIZ SE MEDE NO CORPO. Nada aqui olha o
//      HTML inteiro: o <head>, o JSON-LD e o rodapé ficam de fora, senão o termo
//      seria "encontrado" dentro do próprio schema, que foi como a Robometria
//      passou um teste com resposta inventada.
//   3. PERDOAR POR PRESENÇA DE PALAVRA É ADIVINHAR. "Procedência" é palavra
//      proibida na voz e obrigatória na prova, e as duas são a mesma palavra.
//      Então quem decide é a ESTRUTURA: a página marca a camada de prova com a
//      classe `aqm-prova`, o teste RETIRA esses blocos e proíbe o termo em todo
//      o resto. Para a declaração não virar porta dos fundos — bastaria embrulhar
//      a página toda e ficar verde —, os blocos marcados são CONTADOS (no máximo
//      dois por página), nenhum deles pode ser o primeiro do corpo e nenhum pode
//      conter o H1 ou o primeiro parágrafo.
//   4. O NÚMERO DE TELA NASCE CONTADO. A home diz quantas calculadoras estão no
//      ar; o teste conta os cartões com link e compara. Número digitado que era
//      verdade no dia em que foi escrito é o defeito que o Clube do Mosaico
//      achou no ar em 11/09/2026.
//
// Uma página por processo (`render-casca-pagina.php` explica por quê).

import { execFileSync } from 'node:child_process';

const RAIZ = process.argv[2] || '.';
const PAGINAS = ['inicio', 'calculadoras', 'metodologia', 'sobre'];

/* A régua, escrita aqui. Vem do VOZ.md, seções "Como a gente fala" e
   "Proibidas". Termo em minúsculas; a comparação é sem acento e sem caixa, para
   "procedência" e "PROCEDENCIA" caírem no mesmo lugar. */
const PROIBIDOS = [
  'consulta parametrica',
  'especificacao verificavel',
  'procedencia',
  'conforme a ficha tecnica',
  'ficha tecnica',
  'dimensionamento',       // nome interno do produto, não palavra de quem compra
  'delta termico',
  'turnover',
  'instrumento de medida',
];

/* A RÉGUA DA ATRIBUIÇÃO, e ela vale SÓ para três superfícies: <title>, H1 e
   primeiro parágrafo. Item 4 do despacho da Sentinela de 13/09/2026 — as onze
   fichas de peixe abriam por "Para os N <peixe> que A FONTE DECLARA como cardume
   mínimo ... e A FONTE DECLARA a BASE, não o litro", duas menções à fonte na
   primeira frase da página, contra a 15.2 e contra a régua que o bloco de 11/09
   fixou: procedência não abre página.

   A LISTA É DE DUAS METADES, E A SEGUNDA PRECISA DE ESTRUTURA. Os três primeiros
   termos são atribuição em qualquer frase. "Conforme" e "segundo", que o despacho
   também nomeia, NÃO são: escritos como estão no despacho e medidos no primeiro
   parágrafo das 27 páginas, eles reprovaram TRÊS PÁGINAS CERTAS de uma vez —
   "iluminação baixa pode querer dizer 1.000 lúmens ou 2.000, CONFORME a régua que
   você abrir", "vai de 125 mililitros a 1,25 litro, CONFORME a marca que você
   abrir". Ali "conforme" é "dependendo de", e é justamente a frase que publica a
   divergência entre fontes, que é a tese da ilha. Uma lista literal teria
   silenciado a tese para proibir a atribuição.

   A saída não é uma heurística de vizinhança — a seção 8 já pagou por isso duas
   vezes, e a segunda APROVOU a frase errada. A saída é que ATRIBUIÇÃO PRECISA DE
   UM ATRIBUÍDO: "conforme" e "segundo" só são atribuição quando o que vem depois
   NOMEIA alguém — uma marca da lista de fontes da ilha, ou "a fonte", "o
   fabricante", "o compêndio", "o manual". "Conforme a régua que você abrir" não
   nomeia ninguém, e por isso não é procedência. A estrutura decide, não a
   vizinhança.

   E A LISTA NÃO VALE PARA O CORPO INTEIRO: as nove fichas com base declarada
   dizem, no segundo parágrafo, "Essa base dá de 54 a 72 litros de lâmina,
   CONFORME a altura do aquário ser 30 ou 40 cm". A 15.2 nomeia as superfícies da
   voz uma por uma — título, primeiro parágrafo, rótulos e chamadas —, e é isso
   que este portão mede. */
const ATRIBUICAO_SEMPRE = [
  'a fonte declara',
  'as fontes declaram',
  'declarado por',
  'declarada por',
  'declarados por',
];

const ATRIBUICAO_SE_NOMEIA = ['conforme', 'segundo', 'de acordo com'];

/* Quem pode ser atribuído: as fontes com nome da ilha, mais os quatro jeitos de
   dizer "fonte" sem dizer qual. `marca` e `régua` de propósito NÃO estão aqui —
   "conforme a marca que você abrir" fala de uma marca qualquer, não daquela
   marca, e a diferença entre as duas coisas é o que esta régua existe para não
   confundir. */
const ATRIBUIDOS_GENERICOS = [
  'a fonte', 'as fontes', 'o fabricante', 'os fabricantes',
  'o compendio', 'o manual', 'a ficha do', 'o boletim',
];

/* Fabricantes e fontes citadas pela ilha. Escrita À MÃO aqui, como a lista de
   proibidos: se viesse de dados/produtos-*.json, apagar a marca do banco
   apagaria a régua junto e o teste continuaria verde.

   Fica no alto do arquivo desde 13/09/2026: as duas réguas que a usam — a da
   atribuição, que vale para as 27 páginas, e a de "o primeiro parágrafo não
   nomeia fabricante", que vale para as 23 de conteudo/ — rodam em momentos
   diferentes do arquivo, e `const` declarado no meio explodiria na primeira. */
const MARCAS = [
  'eheim', 'seachem', 'jbl', 'ocean tech', 'atman', 'chihiros', 'ista',
  'sunsun', 'sicce', 'hopar', 'roxin', 'soma', 'maxxi', 'wfish', 'aquaverso',
  'reefflow', 'casa da ada', 'ehow', 'peixeseaquarismo', 'aquarioturbinado',
  'aquariosplantados', 'my-best', 'aquarismo paulista', 'aquaonline',
  'fishbase', 'seriously fish', 'seriouslyfish',
];

/* Título que começa assim é proibido pelo VOZ.md quando o que vem depois é
   termo técnico. A régua aqui é mais dura de propósito: nenhum título de página
   nem de cartão da casca começa com isto. As páginas de conteudo/ têm as suas,
   e não são medidas por este portão. */
const COMECO_PROIBIDO = /^calculadora de\b/;

const CORPO_MINIMO = 1500;   // seção 8 do ARQUIPELAGO.md: página fina é reprovação
const MAX_PROVA    = 2;      // blocos `aqm-prova` por página

let falhas = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

const semAcento = (t) => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const texto = (html) => html.replace(/<[^>]+>/g, ' ').replace(/&[a-z]+;|&#\d+;/gi, ' ').replace(/\s+/g, ' ').trim();

function render(slug) {
  return execFileSync('php', [RAIZ + '/ferramentas/render-casca-pagina.php', RAIZ, slug], {
    encoding: 'utf8', maxBuffer: 32 * 1024 * 1024,
  });
}

/* O corpo: só o que está entre <main> e </main>. É o que o leitor lê e o que o
   crawler indexa como conteúdo da página. */
function corpoDe(html) {
  const m = html.match(/<main[^>]*>([\s\S]*?)<\/main>/);
  return m ? m[1] : '';
}

/* Retira do corpo os blocos marcados como prova, e devolve os dois lados. O
   casamento de <div> é por contagem de aninhamento, não por regex preguiçosa:
   um `[\s\S]*?</div>` pararia no primeiro fechamento interno e deixaria metade
   da prova de volta na voz — o teste ficaria MAIS severo do que deveria e a
   primeira falha seria falsa, que é o pior tipo. */
function separarProva(corpo) {
  const blocos = [];
  let voz = '';
  let i = 0;
  const abre = /<(div|p)\b[^>]*class="[^"]*\baqm-prova\b[^"]*"[^>]*>/g;

  while (i < corpo.length) {
    abre.lastIndex = i;
    const m = abre.exec(corpo);
    if (!m) { voz += corpo.slice(i); break; }

    voz += corpo.slice(i, m.index);

    const tag = m[1];
    let fim = m.index + m[0].length;
    let nivel = 1;
    const passo = new RegExp(`<${tag}\\b[^>]*>|</${tag}>`, 'g');
    passo.lastIndex = fim;
    let p;
    while ((p = passo.exec(corpo)) !== null) {
      nivel += p[0].startsWith('</') ? -1 : 1;
      if (nivel === 0) { fim = p.index + p[0].length; break; }
    }
    if (nivel !== 0) { fim = corpo.length; }

    blocos.push({ html: corpo.slice(m.index, fim), inicio: m.index });
    i = fim;
  }

  return { voz, blocos };
}

function primeiroParagrafo(corpo) {
  const m = corpo.match(/<p\b[^>]*>([\s\S]*?)<\/p>/);
  return m ? texto(m[1]) : '';
}

function h1De(corpo) {
  const m = corpo.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/);
  return m ? texto(m[1]) : '';
}

function acharProibidos(t) {
  const plano = semAcento(t);
  return PROIBIDOS.filter((termo) => plano.includes(termo));
}

/* Atribuição achada no texto. Os termos de sempre valem sozinhos; "conforme" e
   "segundo" só contam quando o que vem depois NOMEIA quem declarou — e o "depois"
   é uma janela curta, porque atribuição encosta no atribuído. */
const JANELA_ATRIBUIDO = 40;

function acharAtribuicao(t) {
  const plano = semAcento(t);
  const achados = ATRIBUICAO_SEMPRE.filter((termo) => plano.includes(termo));

  for (const termo of ATRIBUICAO_SE_NOMEIA) {
    let i = plano.indexOf(termo);
    while (i !== -1) {
      const depois = plano.slice(i + termo.length, i + termo.length + JANELA_ATRIBUIDO);
      const nomeado = [...MARCAS, ...ATRIBUIDOS_GENERICOS].find((n) => depois.includes(n));
      if (nomeado) { achados.push(`${termo} + ${nomeado}`); break; }
      i = plano.indexOf(termo, i + 1);
    }
  }
  return achados;
}

/* As três superfícies de abertura, medidas com a mesma régua e numa função só —
   senão a próxima superfície nasce sem a regra, que é como o <title> ficou de
   fora até 11/09/2026. */
function medirAbertura(rotulo, aba, h1, p1) {
  for (const [onde, t] of [['<title>', aba], ['H1', h1], ['primeiro parágrafo', p1]]) {
    const achados = acharAtribuicao(t);
    ok(`${rotulo}${onde} sem atribuição de fonte`, achados.length === 0,
      achados.join(', ') + (achados.length ? ` — em "${t.slice(0, 90)}"` : ''));
  }
}

/* ---------------------------------------------------------------------- */

/* ----------------------------------------------------------------------
 * A RÉGUA DA ATRIBUIÇÃO MEDIDA CONTRA SI MESMA, em duas frases produzidas.
 *
 * Não é zelo: a primeira versão desta régua, com "conforme" na lista literal,
 * reprovou três páginas certas da ilha. As duas frases abaixo travam a
 * distinção que custou aquela rodada — quem um dia achar mais simples pôr
 * "conforme" de volta na lista de sempre reprova AQUI, antes de reprovar dez
 * páginas. E a segunda frase existe para a régua não afrouxar até deixar de
 * pegar o defeito que ela nasceu para pegar.
 * ------------------------------------------------------------------- */
console.log('\nRÉGUA DA ATRIBUIÇÃO — duas frases produzidas');
{
  const dependencia = 'Iluminação baixa pode querer dizer 1.000 lúmens ou 2.000, conforme a régua que você abrir.';
  const atribuicao  = 'Iluminação baixa é 1.000 lúmens, conforme o compêndio, e 2.000 segundo a Chihiros.';
  ok('"conforme" de dependência NÃO é atribuição', acharAtribuicao(dependencia).length === 0,
    acharAtribuicao(dependencia).join(', '));
  ok('"conforme" com fonte nomeada É atribuição', acharAtribuicao(atribuicao).length >= 2,
    acharAtribuicao(atribuicao).join(', '));
  ok('"a fonte declara" é atribuição sozinha, sem precisar de nome',
    acharAtribuicao('Para os 5 tetra neon que a fonte declara como cardume mínimo.').length === 1);
}

console.log('\nPORTÃO DA VOZ — ' + PAGINAS.length + ' páginas da casca, um processo cada');

const renderizadas = {};

for (const slug of PAGINAS) {
  console.log(`\n/${slug === 'inicio' ? '' : slug + '/'}`);
  const html = render(slug);
  renderizadas[slug] = html;

  const corpo = corpoDe(html);
  ok('o corpo foi encontrado', corpo.length > 0);

  const { voz, blocos } = separarProva(corpo);
  const h1 = h1De(corpo);
  const p1 = primeiroParagrafo(corpo);
  const corpoTexto = texto(corpo);

  /* O <title> e o H1 sao duas superficies diferentes e as duas sao "titulo". O
     <title> da home vinha da tagline do WordPress, e ficou anos na voz antiga
     sem nenhum teste olhar — porque o teste olhava so o corpo. */
  const aba = texto((html.match(/<title>([\s\S]*?)<\/title>/) || [, ''])[1]);
  ok('tem <title>', aba.length > 0, aba);
  ok('<title> sem termo proibido', acharProibidos(aba).length === 0, acharProibidos(aba).join(', '));
  ok('<title> com no máximo 65 caracteres', aba.length <= 65, `${aba.length}`);

  ok('tem H1', h1.length > 0, h1);
  ok('H1 sem termo proibido', acharProibidos(h1).length === 0, acharProibidos(h1).join(', '));
  ok('H1 não começa com "Calculadora de"', !COMECO_PROIBIDO.test(semAcento(h1)));

  ok('tem primeiro parágrafo', p1.length > 0);
  ok('primeiro parágrafo sem termo proibido', acharProibidos(p1).length === 0, acharProibidos(p1).join(', '));

  medirAbertura('', aba, h1, p1);

  // O corpo inteiro, TIRANDO a camada de prova declarada.
  const achados = acharProibidos(texto(voz));
  ok('nenhum termo proibido fora da camada de prova', achados.length === 0, achados.join(', '));

  // A declaração não pode virar porta dos fundos.
  ok(`no máximo ${MAX_PROVA} blocos de prova declarados`, blocos.length <= MAX_PROVA, `achei ${blocos.length}`);
  ok('nenhum bloco de prova contém o H1', !blocos.some((b) => /<h1\b/.test(b.html)));
  ok('nenhum bloco de prova contém o primeiro parágrafo',
    p1.length === 0 || !blocos.some((b) => texto(b.html).startsWith(p1.slice(0, 40))));
  ok('a prova nunca abre a página',
    blocos.every((b) => texto(corpo.slice(0, b.inicio)).length > 200));

  // Página fina não entra no índice de domínio novo (seção 8).
  ok(`corpo com pelo menos ${CORPO_MINIMO} caracteres`, corpoTexto.length >= CORPO_MINIMO, `${corpoTexto.length}`);

  // Títulos de cartão: a pergunta da pessoa, nunca o nome interno.
  const cartoes = [...corpo.matchAll(/<li class="aqm-card">([\s\S]*?)<\/li>/g)].map((m) => m[1]);
  if (cartoes.length > 0) {
    const titulos = cartoes.map((c) => texto((c.match(/<h3\b[^>]*>([\s\S]*?)<\/h3>/) || [, ''])[1]));
    ok('nenhum título de cartão começa com "Calculadora de"',
      titulos.every((t) => !COMECO_PROIBIDO.test(semAcento(t))),
      titulos.filter((t) => COMECO_PROIBIDO.test(semAcento(t))).join(' | '));
    ok('nenhum título de cartão tem termo proibido',
      titulos.every((t) => acharProibidos(t).length === 0),
      titulos.filter((t) => acharProibidos(t).length).join(' | '));
    ok('todo cartão é uma pergunta ou uma frase de gente',
      titulos.every((t) => t.length > 0));
  }
}

/* ----------------------------------------------------------------------
 * A home tem exigências que só ela tem: o molde GUIA do VOZ.md.
 * ------------------------------------------------------------------- */
console.log('\nHOME — molde GUIA');
{
  const corpo = corpoDe(renderizadas['inicio']);
  const p1 = primeiroParagrafo(corpo);
  const h2s = [...corpo.matchAll(/<h2\b[^>]*>([\s\S]*?)<\/h2>/g)].map((m) => texto(m[1]));

  // A pergunta mais frequente em cima, com as três medidas.
  const abertura = (corpo.match(/<div class="aqm-abertura aqm-pergunta">([\s\S]*?)<\/div>/) || [, ''])[1];
  ok('a home abre por um bloco de pergunta', abertura.length > 0);
  const perguntaTexto = texto(abertura);
  ok('a abertura é uma pergunta de verdade', /\?/.test(texto((abertura.match(/<p[^>]*>([\s\S]*?)<\/p>/) || [, ''])[1])));
  const medidas = ['comprimento', 'largura', 'altura'];
  const faltando = medidas.filter((m) => !semAcento(perguntaTexto).includes(m));
  ok('a abertura nomeia as três medidas', faltando.length === 0, 'falta: ' + faltando.join(', '));
  ok('a abertura não é manifesto (não fala da própria marca)',
    !/\baquametria\b/.test(semAcento(perguntaTexto)));

  // Os guias embaixo, com link de verdade.
  const guias = [...corpo.matchAll(/<li class="aqm-guia">([\s\S]*?)<\/li>/g)].map((m) => m[1]);
  ok('a home tem a prateleira de guias', guias.length > 0, `${guias.length} guias`);
  ok('todo guia é um <a href> de verdade', guias.every((g) => /<h3><a href="https?:\/\/[^"]+">/.test(g)));

  // Ordem do molde: pergunta, contas, guias, prova.
  const iPergunta = corpo.indexOf('aqm-pergunta');
  const iCards    = corpo.indexOf('aqm-cards');
  const iGuias    = corpo.indexOf('aqm-guias');
  const iProva    = corpo.indexOf('aqm-prova');
  ok('a ordem é pergunta → contas → guias → prova',
    iPergunta >= 0 && iPergunta < iCards && iCards < iGuias && iGuias < iProva,
    `${iPergunta} ${iCards} ${iGuias} ${iProva}`);

  // O número da tela é CONTADO, não digitado.
  const cartoes = [...corpo.matchAll(/<li class="aqm-card">([\s\S]*?)<\/li>/g)].map((m) => m[1]);
  const comLink = cartoes.filter((c) => /<a href="https?:\/\/[^"]+">Abrir calculadora<\/a>/.test(c)).length;
  const frase = texto(corpo).match(/(\d+) de (\d+) j[áa] est[ãa]o no ar/);
  ok('a home declara quantas calculadoras estão no ar', !!frase);
  if (frase) {
    ok('o número declarado é o número de cartões com link',
      Number(frase[1]) === comLink, `diz ${frase[1]}, contei ${comLink}`);
    ok('o total declarado é o número de cartões',
      Number(frase[2]) === cartoes.length, `diz ${frase[2]}, contei ${cartoes.length}`);
  }

  ok('nenhum h2 da home tem termo proibido',
    h2s.every((t) => acharProibidos(t).length === 0),
    h2s.filter((t) => acharProibidos(t).length).join(' | '));
  ok('o primeiro parágrafo é a pergunta', /\?$/.test(p1), p1);
}

/* ----------------------------------------------------------------------
 * O header: o menu fala a língua do VOZ.md e continua no HTML servido.
 * ------------------------------------------------------------------- */
console.log('\nHEADER');
{
  const html = renderizadas['inicio'];
  const nav = (html.match(/<nav class="aqm-nav"[^>]*>[\s\S]*?<\/nav>/) || [''])[0];
  ok('o <nav> existe no HTML servido', nav.length > 0);
  const rotulos = [...nav.matchAll(/<a href="[^"]+">([^<]+)<\/a>/g)].map((m) => m[1]);
  ok('três links no menu', rotulos.length === 3, rotulos.join(' · '));
  ok('nenhum rótulo de menu tem termo proibido',
    rotulos.every((r) => acharProibidos(r).length === 0), rotulos.join(' · '));
  ok('o menu não diz "Metodologia"', !rotulos.includes('Metodologia'), rotulos.join(' · '));

  // Regra permanente do projeto.
  const scripts = html.match(/<script[\s\S]*?<\/script>/g) || [];
  const escapados = scripts.join('').match(/&#038;/g) || [];
  ok('zero &#038; dentro de <script>', escapados.length === 0, `achei ${escapados.length}`);

  const corpo = corpoDe(html);
  ok('nenhum <script> dentro do corpo', !/<script/.test(corpo));
  ok('nenhum <style> dentro do corpo', !/<style/.test(corpo));
  ok('o corpo não começa por metadado YAML', !texto(corpo).startsWith('---'));
}

/* ======================================================================
 * AS NOVE PÁGINAS DE conteudo/ — a metade da ilha que este portão não media
 *
 * Até 11/09/2026 este arquivo olhava só as quatro páginas da casca, e o
 * despacho da voz registrava "as de conteudo/ ainda não foram" como pendência
 * escrita à mão. Pendência escrita à mão não é portão: as cinco calculadoras
 * seguiram no ar com H1 começando por "Calculadora de", que é a única forma de
 * título que o VOZ.md proíbe pelo nome, e oito dos nove <title> passavam de 65
 * caracteres — nada disso precisava de olho humano para ser visto, precisava de
 * alguém medindo.
 *
 * DUAS COISAS QUE MUDAM EM RELAÇÃO À RÉGUA DA CASCA, e as duas de propósito:
 *
 *   1. O RENDERIZADOR É OUTRO. Página de conteudo/ só sai inteira pelo
 *      render-pagina-completa.php — os outros três montam metade. Medir a voz
 *      no renderizador errado seria medir um H1 que o site não serve.
 *   2. NÃO SE COBRA "termo proibido no corpo inteiro". A casca são quatro
 *      páginas curtas de interface; estas nove são, em boa parte, a própria
 *      camada de prova — explicação, tabela de fonte, "como sabemos". A 15.2
 *      nomeia o que fica na voz: TÍTULO, PRIMEIRO PARÁGRAFO, rótulos e
 *      chamadas. É isso que se mede aqui, mais os H2, que são chamadas.
 *
 * E UMA TERCEIRA, que é a régua que faltava: PROCEDÊNCIA NÃO ABRE PÁGINA. O
 * primeiro parágrafo não pode nomear fabricante nem carregar data de leitura —
 * era exatamente assim que os três artigos abriam ("Coletadas em 08/09/2026 e
 * atribuídas ao próprio fabricante: Seachem Matrix, ..."), sem nenhum termo da
 * lista de proibidas aparecer. Lista de palavra não pega isso; só pega quem
 * mede a NATUREZA do que está escrito ali.
 * ==================================================================== */

const CONTEUDO = [
  'calculadora-de-litragem',
  'calculadora-de-vazao-do-filtro',
  'calculadora-de-potencia-do-aquecedor',
  'calculadora-de-midia-filtrante',
  'calculadora-de-iluminacao',
  'divulgacao-de-afiliados',
  'quantos-watts-de-aquecedor-para-aquario',
  'quanta-midia-biologica-o-aquario-precisa',
  'quantos-lumens-por-litro-aquario-plantado',
  /* A leva 1 do eixo /peixes/ (T4, 12/09/2026). Estas cinco não vêm de
     conteudo/ — o corpo delas é shortcode —, mas saem inteiras pelo MESMO
     renderizador, e a voz vale para toda página da ilha. Ao entrarem aqui, três
     aberturas reprovaram de uma vez: nenhuma das três falava na segunda pessoa
     e a da categoria abria com "o banco desta ilha", que é vocabulário de dentro
     da fábrica. Nenhum olho tinha visto; a régua viu. */
  'peixes',
  'tetras',
  'quantos-litros-para-tetra-neon',
  'quantos-litros-para-tetra-cardinal',
  'quantos-litros-para-mato-grosso',
  /* A leva 2 (12/09/2026): as quatro que fecham a categoria. A do rodóstomo é a
     primeira ficha da ilha que declara uma AUSÊNCIA de dado no corpo, e por isso
     a que mais arriscava escorregar para o vocabulário de dentro da fábrica. */
  'quantos-litros-para-tetra-ember',
  'quantos-litros-para-tetra-brilhante',
  'quantos-litros-para-rodostomo',
  'quantos-litros-para-tetra-negro',
  /* A leva 3 (12/09/2026): a categoria /peixes/corydoras/ e as quatro fichas
     dela. A da categoria é a que mais importa aqui: a abertura de categoria
     deixou de ser texto fixo e passou a vir declarada por categoria, e texto
     declarado num array de configuração é exatamente onde a voz escapa sem
     ninguém ler — não passa por revisão de página, passa por revisão de dado. */
  'corydoras',
  'quantos-litros-para-coridora-bronze',
  'quantos-litros-para-coridora-pimenta',
  'quantos-litros-para-coridora-panda',
  'quantos-litros-para-coridora-sterbai',
];

/* As onze fichas de espécie, separadas do resto do CONTEUDO porque têm duas
   exigências que só elas têm (a abertura pelo número e a distinção
   BASE/COMPRIMENTO). O conjunto está escrito À MÃO, e não filtrado por prefixo
   do slug: a próxima leva vai acrescentar fichas com outro prefixo, e um filtro
   esperto deixaria as novas fora da régua sem uma falha para avisar. */
const FICHAS_PEIXE = new Set([
  'quantos-litros-para-tetra-neon',
  'quantos-litros-para-tetra-cardinal',
  'quantos-litros-para-mato-grosso',
  'quantos-litros-para-tetra-ember',
  'quantos-litros-para-tetra-brilhante',
  'quantos-litros-para-rodostomo',
  'quantos-litros-para-tetra-negro',
  'quantos-litros-para-coridora-bronze',
  'quantos-litros-para-coridora-pimenta',
  'quantos-litros-para-coridora-panda',
  'quantos-litros-para-coridora-sterbai',
]);

/* A lista de MARCAS subiu para o alto do arquivo em 13/09/2026 — ver o bloco
   da régua de atribuição, que passou a usá-la também. */
const DATA_DE_LEITURA = /\b\d{2}\/\d{2}\/\d{4}\b/;

const TITULO_MAXIMO = 65;   // o que o Google mostra antes de cortar

function renderCompleta(slug) {
  return execFileSync('php', [RAIZ + '/ferramentas/render-pagina-completa.php', RAIZ, slug], {
    encoding: 'utf8', maxBuffer: 64 * 1024 * 1024,
  });
}

/* O último degrau da trilha: o nome que a casca dá à página. */
function degrauAtual(corpo) {
  const m = corpo.match(/<span aria-current="page">([\s\S]*?)<\/span>/);
  return m ? texto(m[1]) : '';
}

console.log('\n\nPORTÃO DA VOZ — ' + CONTEUDO.length + ' páginas de conteudo/, um processo cada');

const h1Vistos = new Map();

for (const slug of CONTEUDO) {
  console.log(`\n/${slug}/`);
  const html  = renderCompleta(slug);
  const corpo = corpoDe(html);
  ok('o corpo foi encontrado', corpo.length > 0);

  const { voz, blocos } = separarProva(corpo);
  const h1  = h1De(corpo);
  const p1  = primeiroParagrafo(corpo);
  const aba = texto((html.match(/<title>([\s\S]*?)<\/title>/) || [, ''])[1]);
  const h2s = [...corpo.matchAll(/<h2\b[^>]*>([\s\S]*?)<\/h2>/g)].map((m) => texto(m[1]));

  /* --- o título, nas duas superfícies --- */
  ok('tem H1', h1.length > 0, h1);
  ok('H1 sem termo proibido', acharProibidos(h1).length === 0, acharProibidos(h1).join(', '));
  ok('H1 não começa com "Calculadora de"', !COMECO_PROIBIDO.test(semAcento(h1)), h1);
  ok('<title> sem termo proibido', acharProibidos(aba).length === 0, acharProibidos(aba).join(', '));
  ok(`<title> com no máximo ${TITULO_MAXIMO} caracteres`, aba.length <= TITULO_MAXIMO, `${aba.length} — ${aba}`);
  ok('o <title> começa pelo H1', aba.startsWith(h1), `${aba} vs ${h1}`);

  /* UM NOME POR PÁGINA. O degrau da trilha e o H1 ficam a uma linha um do
     outro na tela, e até 11/09/2026 diziam coisas diferentes em 8 das 9 — a
     trilha dizia "Quantos litros tem o seu aquário?" e o H1, logo abaixo,
     "Calculadora de litragem: quantos litros tem o seu aquário". Dois nomes
     para a mesma página é o defeito; a régua é a igualdade. */
  const degrau = degrauAtual(corpo);
  ok('a trilha nomeia a página', degrau.length > 0, degrau);
  ok('o degrau da trilha é igual ao H1', degrau === h1, `trilha "${degrau}" vs H1 "${h1}"`);

  /* Duas páginas com o mesmo H1 competem entre si na mesma busca. */
  const chave = semAcento(h1);
  ok('nenhuma outra página desta ilha tem este H1',
    !h1Vistos.has(chave), h1Vistos.has(chave) ? 'igual ao de /' + h1Vistos.get(chave) + '/' : '');
  h1Vistos.set(chave, slug);

  /* --- o primeiro parágrafo: a camada de voz --- */
  ok('tem primeiro parágrafo', p1.length > 0);
  ok('primeiro parágrafo sem termo proibido', acharProibidos(p1).length === 0, acharProibidos(p1).join(', '));

  const marcasNoP1 = MARCAS.filter((m) => semAcento(p1).includes(m));
  ok('o primeiro parágrafo não nomeia fabricante nem fonte',
    marcasNoP1.length === 0, marcasNoP1.join(', '));
  ok('o primeiro parágrafo não carrega data de leitura',
    !DATA_DE_LEITURA.test(p1), (p1.match(DATA_DE_LEITURA) || [''])[0]);

  /* O VOZ.md manda falar em SEGUNDA PESSOA ("o seu aquário"). Cinco das nove
     páginas abriam falando da internet em vez de falar com quem entrou
     ("Pergunte na internet brasileira quanta mídia biológica um aquário de 100
     litros precisa..."), e nenhuma régua de palavra proibida pega isso.
     O LIMITE DESTA RÉGUA ESTÁ DECLARADO: ela pega o abridor que fala do mundo
     em terceira pessoa, não pega um manifesto que diga "você" logo na primeira
     linha — o antigo abridor da página de iluminação dizia, e passaria. Quem
     julga manifesto é a ronda (15.4); esta linha é o piso mecânico. */
  ok('o primeiro parágrafo fala com a pessoa, na segunda pessoa',
    /\b(voce|seu|sua|seus|suas)\b/.test(semAcento(p1)), p1.slice(0, 70));

  medirAbertura('', aba, h1, p1);

  /* --- a ficha de peixe: a abertura responde COM O NÚMERO, e diz qual dos dois
         mundos ela é ---

     É a outra metade do item 4 do despacho, e a que protege a decisão 7 do
     snippet: 14 dos 36 registros do banco declaram só o COMPRIMENTO mínimo e
     nunca disseram uma palavra sobre o fundo. Enquanto a abertura citava a
     fonte, era a palavra "fonte" que carregava a diferença; agora ela viaja na
     ESTRUTURA da frase, e por isso precisa de régua: a ficha com fundo diz "por
     Y cm de fundo" e termina em BASE, a ficha sem fundo diz que ele FICA EM
     ABERTO e termina em COMPRIMENTO. EXATAMENTE UM dos dois — a reescrita que
     colapsasse os dois casos num só publicaria um fundo que ninguém declarou
     (ou esconderia o que foi declarado), e passaria por qualquer régua que só
     proibisse palavra. */
  if (FICHAS_PEIXE.has(slug)) {
    const plano = semAcento(p1);
    ok('a ficha abre pelo número, com a frente em centímetros',
      /\d+(,\d+)? cm de frente/.test(plano), p1.slice(0, 90));

    const comBase = / cm de fundo/.test(plano) && /\bbase\b/.test(plano);
    const semBase = /fica em aberto/.test(plano) && /\bcomprimento\b/.test(plano);
    ok('a ficha declara a BASE ou o COMPRIMENTO, e exatamente um dos dois',
      comBase !== semBase, `base=${comBase} comprimento=${semBase} — "${p1.slice(0, 110)}"`);
    ok('a ficha não fala de litro como se fosse a medida que manda',
      /nao o litro/.test(plano), p1.slice(-60));
  }

  /* --- as chamadas --- */
  ok('nenhum h2 tem termo proibido',
    h2s.every((t) => acharProibidos(t).length === 0),
    h2s.filter((t) => acharProibidos(t).length).join(' | '));
  ok('nenhum h2 começa com "Calculadora de"',
    h2s.every((t) => !COMECO_PROIBIDO.test(semAcento(t))),
    h2s.filter((t) => COMECO_PROIBIDO.test(semAcento(t))).join(' | '));

  /* --- a declaração de prova não vira porta dos fundos --- */
  ok(`no máximo ${MAX_PROVA} blocos de prova declarados`, blocos.length <= MAX_PROVA, `achei ${blocos.length}`);
  ok('nenhum bloco de prova contém o H1', !blocos.some((b) => /<h1\b/.test(b.html)));
  ok('nenhum bloco de prova contém o primeiro parágrafo',
    p1.length === 0 || !blocos.some((b) => texto(b.html).startsWith(p1.slice(0, 40))));

  /* --- o texto de âncora é a consulta da página de destino, não o nome
         interno do produto (16.4a) --- */
  const ancoras = [...voz.matchAll(/<a href="https?:\/\/aquametria\.com\.br\/[^"]*"[^>]*>([\s\S]*?)<\/a>/g)]
    .map((m) => texto(m[1])).filter((t) => t.length > 0);
  const ancorasRuins = ancoras.filter((t) => COMECO_PROIBIDO.test(semAcento(t)));
  ok('nenhum link interno tem âncora começando por "Calculadora de"',
    ancorasRuins.length === 0, ancorasRuins.join(' | '));

  ok(`corpo com pelo menos ${CORPO_MINIMO} caracteres`, texto(corpo).length >= CORPO_MINIMO, `${texto(corpo).length}`);

  /* Regras permanentes do projeto, nestas páginas também. */
  const scripts = html.match(/<script[\s\S]*?<\/script>/g) || [];
  ok('zero &#038; dentro de <script>', (scripts.join('').match(/&#038;/g) || []).length === 0);
  ok('o corpo não começa por metadado YAML', !texto(corpo).startsWith('---'));
}

console.log(falhas === 0 ? '\nTUDO OK' : `\n${falhas} FALHA(S)`);
process.exit(falhas === 0 ? 0 : 1);

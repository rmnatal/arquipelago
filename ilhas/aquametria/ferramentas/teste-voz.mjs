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

/* ---------------------------------------------------------------------- */

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

  ok('tem H1', h1.length > 0, h1);
  ok('H1 sem termo proibido', acharProibidos(h1).length === 0, acharProibidos(h1).join(', '));
  ok('H1 não começa com "Calculadora de"', !COMECO_PROIBIDO.test(semAcento(h1)));

  ok('tem primeiro parágrafo', p1.length > 0);
  ok('primeiro parágrafo sem termo proibido', acharProibidos(p1).length === 0, acharProibidos(p1).join(', '));

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

console.log(falhas === 0 ? '\nTUDO OK' : `\n${falhas} FALHA(S)`);
process.exit(falhas === 0 ? 0 : 1);

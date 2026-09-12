// O PORTÃO DA ÁRVORE — mede a trilha, o BreadcrumbList e o cluster que as TREZE
// páginas no ar SERVEM (seção 16 do ARQUIPELAGO.md).
//
//   node ferramentas/teste-arvore.mjs .
//
// AS CICATRIZES DA SEÇÃO 8 QUE ESTE ARQUIVO OBEDECE, uma a uma:
//
//   1. QUEM CONFERE ESCREVE A PRÓPRIA RÉGUA. Nada aqui é importado do snippet.
//      O mapa de código -> página, o de categoria -> rótulo e a lista das treze
//      páginas estão escritos ABAIXO, à mão. Se as duas metades lessem a mesma
//      lista, trocar a categoria da C5 faria as duas errarem juntas e o teste
//      continuaria verde.
//   2. AS DUAS METADES TÊM QUE SE FALAR. A árvore também está escrita em
//      ARVORE.md, em português, e documento e código mantidos à mão em dois
//      lugares divergem em silêncio — foi assim que a Robometria publicou meses
//      uma coluna "Temos hoje" que contradizia o próprio banco. Então este teste
//      LÊ o ARVORE.md, extrai as tabelas das seções 2 e 5, e exige que a
//      categoria que o documento dá a cada página seja a que a página serve.
//   3. AFIRMAÇÃO SOBRE O QUE A PÁGINA DIZ SE MEDE NO CORPO. Tudo o que se afirma
//      sobre a trilha e o cluster é medido entre <main> e </main>. O JSON-LD é
//      lido à parte, do <head>, e justamente por isso ele nunca pode servir de
//      prova de que o texto está na tela — foi assim que a Robometria passou um
//      teste com resposta inventada.
//   4. A GRADE PISA NA BORDA. O 16.4(c) manda de 2 a 4 irmãs. Grade que só
//      medisse "está entre 2 e 4" não separa `>` de `>=`: então o teste exige
//      que os DOIS extremos apareçam de verdade no site de hoje — alguma página
//      com exatamente 2 irmãs e alguma com exatamente 4 —, senão a faixa é
//      amostra com nome de grade.
//   5. NÚMERO DE TELA NASCE CONTADO. A frase do cluster diz quantas contas estão
//      no ar. O teste conta os cartões com link no hub e compara. Número
//      digitado que era verdade no dia em que foi escrito é o defeito que o
//      Clube do Mosaico achou no ar em 11/09/2026.
//
// Uma página por processo (`render-pagina-completa.php` explica por quê).

import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const RAIZ = process.argv[2] || '.';

/* ------------------------------------------------------------------ a régua */

/* As treze páginas no ar, e o que cada uma é. Escrito à mão a partir do
   manifest e do ARVORE.md — não lido de nenhum dos dois. */
const HOME = 'inicio';

const RAIZ_DA_ILHA = ['calculadoras', 'metodologia', 'sobre', 'divulgacao-de-afiliados'];

/* Código do hub -> slug da página. É a ponte entre o ARVORE.md (que fala em C5)
   e a URL (que fala em calculadora-de-potencia-do-aquecedor). */
const CODIGO_PARA_SLUG = {
  C1: 'calculadora-de-litragem',
  C3: 'calculadora-de-vazao-do-filtro',
  C5: 'calculadora-de-potencia-do-aquecedor',
  C12: 'calculadora-de-midia-filtrante',
  C15: 'calculadora-de-iluminacao',
};

const CALCULADORAS = Object.values(CODIGO_PARA_SLUG);

const GUIAS = [
  'quantos-watts-de-aquecedor-para-aquario',
  'quanta-midia-biologica-o-aquario-precisa',
  'quantos-lumens-por-litro-aquario-plantado',
];

/* Slug de categoria -> rótulo na tela. O rótulo é o nome que a pessoa usa
   (VOZ.md); o slug é o do ARVORE.md. */
const ROTULO_CATEGORIA = {
  aquario: 'Aquário',
  filtragem: 'Filtragem',
  'aquecimento-e-luz': 'Aquecimento e luz',
  lotacao: 'Lotação',
  aquecimento: 'Aquecimento',
  iluminacao: 'Iluminação',
};

const TODAS = [HOME, ...RAIZ_DA_ILHA, ...CALCULADORAS, ...GUIAS];

/* As páginas que EXISTEM publicadas. Trilha nunca pode linkar fora daqui. */
const PUBLICADAS = new Set(TODAS);

const MIN_IRMAS = 2;
const MAX_IRMAS = 4;

let falhas = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  if (!cond) falhas++;
}

/* ------------------------------------------------------------- ferramentas */

function render(slug) {
  return execFileSync('php', [RAIZ + '/ferramentas/render-pagina-completa.php', RAIZ, slug], {
    encoding: 'utf8',
    maxBuffer: 48 * 1024 * 1024,
  });
}

/* O corpo: só o que está entre <main> e </main>. É o que o leitor lê. */
function corpoDe(html) {
  const m = html.match(/<main[^>]*>([\s\S]*?)<\/main>/);
  return m ? m[1] : '';
}

const textoDe = (html) =>
  html.replace(/<[^>]+>/g, ' ').replace(/&[a-z]+;|&#\d+;/gi, ' ').replace(/\s+/g, ' ').trim();

/* O slug que um endereço da ilha aponta. '' para endereço de fora. */
function slugDaUrl(url) {
  const m = url.match(/^https:\/\/aquametria\.com\.br\/([^?#]*)$/);
  if (!m) return null;
  const caminho = m[1].replace(/\/$/, '');
  return caminho === '' ? HOME : caminho;
}

/* Os degraus da trilha, lidos do HTML servido: rótulo, e o destino quando é
   link. Sem regex preguiçosa — cada <li> é recortado inteiro. */
function trilhaDe(corpo) {
  const nav = corpo.match(/<nav class="aqm-trilha"[^>]*>([\s\S]*?)<\/nav>/);
  if (!nav) return null;
  const itens = [...nav[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map((m) => m[1]);
  return itens.map((li) => {
    const link = li.match(/<a href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/);
    const atual = /aria-current="page"/.test(li);
    const espera = /class="aqm-trilha-espera"/.test(li);
    return {
      rotulo: textoDe(li),
      url: link ? link[1] : '',
      atual,
      espera,
    };
  });
}

function clusterDe(corpo) {
  const nav = corpo.match(/<nav class="aqm-veja"[^>]*>([\s\S]*?)<\/nav>/);
  if (!nav) return null;
  const bruto = nav[1];
  const frase = bruto.match(/<p class="aqm-veja-mae">([\s\S]*?)<\/p>/);
  const itens = [...bruto.matchAll(/<li><a href="([^"]+)"[^>]*>([\s\S]*?)<\/a><\/li>/g)].map((m) => ({
    url: m[1],
    rotulo: textoDe(m[2]),
  }));
  return { frase: frase ? frase[1] : '', irmas: itens };
}

function jsonldTrilhaDe(html) {
  const m = html.match(/id="aquametria-trilha-jsonld">([\s\S]*?)<\/script>/);
  if (!m) return null;
  try {
    return JSON.parse(m[1]);
  } catch (e) {
    return 'INVALIDO';
  }
}

/* --------------------------------------- a árvore como o ARVORE.md a escreve */

/* Seção 2: as linhas da tabela de categorias das calculadoras.
   | `/calculadoras/aquecimento-e-luz/` | C5 aquecedor · C15 iluminação · C7 ... | */
function arvoreCalculadoras(doc) {
  const mapa = {};
  const re = /\|\s*`\/calculadoras\/([a-z0-9-]+)\/`\s*\|([^|]*)\|/g;
  let m;
  while ((m = re.exec(doc)) !== null) {
    const categoria = m[1];
    for (const cod of m[2].match(/\bC\d+\b/g) || []) mapa[cod] = categoria;
  }
  return mapa;
}

/* Seção 5: | `slug-do-artigo` | `/guias/aquecimento/` | C5 | */
function arvoreGuias(doc) {
  const mapa = {};
  const re = /\|\s*`([a-z0-9-]+)`\s*\|\s*`\/guias\/([a-z0-9-]+)\/`\s*\|/g;
  let m;
  while ((m = re.exec(doc)) !== null) mapa[m[1]] = m[2];
  return mapa;
}

/* ------------------------------------------------------------------ medição */

console.log('PORTÃO DA ÁRVORE — trilha, BreadcrumbList e cluster nas 13 páginas\n');

const doc = readFileSync(RAIZ + '/ARVORE.md', 'utf8');
const catCalc = arvoreCalculadoras(doc);
const catGuia = arvoreGuias(doc);

console.log('ARVORE.md — o documento e o código dizem a mesma coisa');
ok('ARVORE.md nomeia as 5 calculadoras no ar', CALCULADORAS.every((s) =>
  Object.entries(CODIGO_PARA_SLUG).some(([c, sl]) => sl === s && catCalc[c])),
  Object.keys(catCalc).join(','));
ok('ARVORE.md nomeia os 3 guias', GUIAS.every((g) => catGuia[g]), Object.values(catGuia).join(','));
for (const cat of [...new Set([...Object.values(catCalc), ...Object.values(catGuia)])]) {
  ok(`categoria "${cat}" tem rótulo declarado nesta régua`, !!ROTULO_CATEGORIA[cat]);
}

/* Uma página por processo, e o que cada uma serve fica guardado para as
   afirmações que só dá para fazer olhando o site inteiro (órfã, bordas). */
const servido = {};
for (const slug of TODAS) {
  const html = render(slug);
  const corpo = corpoDe(html);
  servido[slug] = { html, corpo, trilha: trilhaDe(corpo), cluster: clusterDe(corpo), jsonld: jsonldTrilhaDe(html) };
}

console.log('\nA HOME não tem trilha (16.3)');
ok('home sem <nav class="aqm-trilha">', servido[HOME].trilha === null);
ok('home sem BreadcrumbList', servido[HOME].jsonld === null);

console.log('\nTRILHA — as 12 páginas internas');
for (const slug of TODAS.filter((s) => s !== HOME)) {
  const { corpo, trilha } = servido[slug];
  const nome = slug.length > 34 ? slug.slice(0, 33) + '…' : slug;

  if (!trilha) {
    ok(`${nome}: tem trilha`, false);
    continue;
  }
  ok(`${nome}: uma trilha só`, (corpo.match(/<nav class="aqm-trilha"/g) || []).length === 1);
  ok(`${nome}: a trilha vem ANTES do H1`, corpo.indexOf('aqm-trilha') < corpo.indexOf('<h1'));
  ok(`${nome}: começa em Início, com link`, trilha[0].rotulo === 'Início' && trilha[0].url !== '');
  ok(`${nome}: o último degrau é a página, sem link`,
    trilha[trilha.length - 1].atual && trilha[trilha.length - 1].url === '');
  ok(`${nome}: nenhum degrau do meio é a página atual`,
    trilha.slice(0, -1).every((d) => !d.atual));

  /* Link morto é pior que degrau sem link: cada <a> da trilha tem que apontar
     para página que existe. */
  const mortos = trilha.filter((d) => d.url !== '' && !PUBLICADAS.has(slugDaUrl(d.url)));
  ok(`${nome}: nenhum degrau aponta para página inexistente`, mortos.length === 0,
    mortos.map((d) => d.url).join(' '));

  /* Degrau sem link é sempre declarado como espera — nunca texto solto por
     acidente. */
  ok(`${nome}: degrau sem link é marcado como categoria em espera`,
    trilha.slice(0, -1).every((d) => d.url !== '' || d.espera));

  if (RAIZ_DA_ILHA.includes(slug)) {
    ok(`${nome}: página de raiz tem 2 degraus`, trilha.length === 2, `tem ${trilha.length}`);
  } else {
    ok(`${nome}: página de árvore tem 4 degraus`, trilha.length === 4, `tem ${trilha.length}`);
  }
}

console.log('\nTRILHA — a categoria que a página mostra é a que o ARVORE.md dá');
for (const [cod, slug] of Object.entries(CODIGO_PARA_SLUG)) {
  const esperado = ROTULO_CATEGORIA[catCalc[cod]];
  const t = servido[slug].trilha;
  ok(`${cod}: nível 2 = "${esperado}"`, !!t && t[2] && t[2].rotulo === esperado,
    t && t[2] ? `serve "${t[2].rotulo}"` : 'sem degrau 2');
  ok(`${cod}: nível 1 é /calculadoras/`, !!t && t[1] && slugDaUrl(t[1].url) === 'calculadoras');
}
for (const g of GUIAS) {
  const esperado = ROTULO_CATEGORIA[catGuia[g]];
  const t = servido[g].trilha;
  ok(`${g.slice(0, 26)}…: nível 2 = "${esperado}"`, !!t && t[2] && t[2].rotulo === esperado,
    t && t[2] ? `serve "${t[2].rotulo}"` : 'sem degrau 2');
  ok(`${g.slice(0, 26)}…: /guias/ ainda em texto`, !!t && t[1] && t[1].url === '' && t[1].espera);
}

console.log('\nBREADCRUMBLIST — válido, e amarrado à trilha da tela');
for (const slug of TODAS.filter((s) => s !== HOME)) {
  const { trilha, jsonld } = servido[slug];
  const nome = slug.length > 30 ? slug.slice(0, 29) + '…' : slug;

  if (!jsonld || jsonld === 'INVALIDO') {
    ok(`${nome}: BreadcrumbList presente e válido`, false);
    continue;
  }
  const itens = jsonld.itemListElement || [];
  ok(`${nome}: @type BreadcrumbList`, jsonld['@type'] === 'BreadcrumbList');
  ok(`${nome}: 2 itens ou mais`, itens.length >= 2, `tem ${itens.length}`);
  ok(`${nome}: posições 1..n sem buraco`, itens.every((it, i) => it.position === i + 1));
  /* A regra que faz o schema valer: ListItem do meio SEM item invalida a lista
     inteira no Google, e lista inválida é lista ignorada. */
  ok(`${nome}: todo item do meio tem endereço`, itens.slice(0, -1).every((it) => !!it.item));
  ok(`${nome}: nenhum endereço do schema é de página inexistente`,
    itens.every((it) => !it.item || PUBLICADAS.has(slugDaUrl(it.item))));

  /* E a amarração com a tela: os itens do schema são exatamente os degraus
     LINKADOS da trilha, mais a página atual. Sem isso o schema poderia
     descrever uma navegação que a página não tem. */
  const daTela = trilha.filter((d) => d.url !== '').map((d) => d.rotulo);
  daTela.push(trilha[trilha.length - 1].rotulo);
  ok(`${nome}: nomes do schema = degraus linkados + página atual`,
    JSON.stringify(itens.map((it) => it.name)) === JSON.stringify(daTela),
    itens.map((it) => it.name).join(' > '));
}

console.log('\nCLUSTER "VEJA TAMBÉM" (16.4c)');
const tamanhos = [];
for (const slug of [...CALCULADORAS, ...GUIAS]) {
  const { cluster } = servido[slug];
  const nome = slug.length > 30 ? slug.slice(0, 29) + '…' : slug;
  if (!cluster) {
    ok(`${nome}: tem bloco Veja também`, false);
    continue;
  }
  const n = cluster.irmas.length;
  tamanhos.push(n);
  ok(`${nome}: de ${MIN_IRMAS} a ${MAX_IRMAS} irmãs`, n >= MIN_IRMAS && n <= MAX_IRMAS, `tem ${n}`);
  ok(`${nome}: nenhuma irmã é ela mesma`, cluster.irmas.every((i) => slugDaUrl(i.url) !== slug));
  ok(`${nome}: nenhuma irmã repetida`, new Set(cluster.irmas.map((i) => i.url)).size === n);
  ok(`${nome}: toda irmã existe publicada`,
    cluster.irmas.every((i) => PUBLICADAS.has(slugDaUrl(i.url))));

  /* Irmã é quem tem a MESMA MÃE. Calculadora nunca é irmã de guia. */
  const mesmaFamilia = CALCULADORAS.includes(slug) ? CALCULADORAS : GUIAS;
  ok(`${nome}: toda irmã tem a mesma mãe`,
    cluster.irmas.every((i) => mesmaFamilia.includes(slugDaUrl(i.url))),
    cluster.irmas.map((i) => slugDaUrl(i.url)).join(' '));

  /* Âncora é a consulta da irmã, nunca "clique aqui" nem "saiba mais". */
  ok(`${nome}: âncora não é genérica`,
    cluster.irmas.every((i) => !/^(clique aqui|saiba mais|veja mais|leia mais)$/i.test(i.rotulo)));
  ok(`${nome}: âncora tem palavra de gente`, cluster.irmas.every((i) => i.rotulo.length > 12));
}

/* A BORDA DE BAIXO, que o mundo de hoje produz sozinho: os guias são três, logo
   cada um tem exatamente duas irmãs. */
ok(`a grade pisa na borda de baixo (${MIN_IRMAS})`, tamanhos.includes(MIN_IRMAS), tamanhos.join(','));

/* A BORDA DE CIMA NÃO É PRODUZIDA PELO MUNDO DE HOJE, e foi a mutação que
   descobriu isso: com cinco calculadoras no ar, cada página tem no máximo
   QUATRO irmãs candidatas — então trocar o teto de 4 por 5 no snippet não muda
   nada do que o site serve, e o portão ficava verde nas duas versões. Ver "está
   entre 2 e 4" quando o mundo nunca passa de 4 é amostra com nome de grade, que
   é a cicatriz da seção 8 do contrato.
   A saída é a bancada FABRICAR a borda: o modo `todas` do renderizador põe as
   três calculadoras em construção no ar, a página passa a ter sete candidatas,
   e aí o teto tem o que cortar. É a única afirmação deste arquivo que mede um
   mundo que não é o de hoje, e é de propósito. */
console.log('\nA BORDA DE CIMA, fabricada — 7 irmãs candidatas, o teto corta em 4');
const naBorda = execFileSync(
  'php',
  [RAIZ + '/ferramentas/render-pagina-completa.php', RAIZ, CODIGO_PARA_SLUG.C5, 'todas'],
  { encoding: 'utf8', maxBuffer: 48 * 1024 * 1024 }
);
const clusterBorda = clusterDe(corpoDe(naBorda));
ok('com 8 calculadoras no ar a C5 ainda recebe 4 irmãs', !!clusterBorda && clusterBorda.irmas.length === MAX_IRMAS,
  clusterBorda ? `tem ${clusterBorda.irmas.length}` : 'sem cluster');
ok('e as 4 continuam sendo calculadoras, nunca guias', !!clusterBorda &&
  clusterBorda.irmas.every((i) => /^calculadora-de-/.test(slugDaUrl(i.url) || '')));
/* A mesma da mesma categoria continua vindo primeiro: afinidade, não sorteio.
   Com o mundo cheio, a C15 e a C7 são as duas de aquecimento-e-luz. */
ok('a afinidade manda: as de aquecimento-e-luz vêm primeiro', !!clusterBorda &&
  ['calculadora-de-iluminacao', 'calculadora-de-consumo-de-energia']
    .every((s) => clusterBorda.irmas.slice(0, 2).some((i) => slugDaUrl(i.url) === s)),
  clusterBorda ? clusterBorda.irmas.map((i) => slugDaUrl(i.url)).join(' ') : '');

console.log('\nA MÃE, LINKADA NO CORPO (16.4b) — e a contagem contada, nunca digitada');
/* Quantas calculadoras o hub de fato abre: cartão com link. É esta a régua, e
   ela é contada aqui, no HTML servido do hub — não perguntada ao snippet. */
const cartoesComLink = [
  ...corpoDe(servido.calculadoras.html).matchAll(/<a href="([^"]+)"[^>]*>Abrir calculadora<\/a>/g),
].length;
ok('o hub abre 5 calculadoras', cartoesComLink === CALCULADORAS.length, `conta ${cartoesComLink}`);

for (const slug of CALCULADORAS) {
  const { cluster } = servido[slug];
  const nome = slug.length > 30 ? slug.slice(0, 29) + '…' : slug;
  const frase = cluster ? cluster.frase : '';
  ok(`${nome}: o corpo linka a mãe`, /href="https:\/\/aquametria\.com\.br\/calculadoras\/"/.test(frase));
  const num = textoDe(frase).match(/\b(\d+)\b/);
  ok(`${nome}: o número da frase é o contado (${cartoesComLink})`,
    !!num && Number(num[1]) === cartoesComLink, num ? num[1] : 'sem número');
}
for (const g of GUIAS) {
  /* /guias/ não existe: frase de mãe apontaria para link morto. Ela só nasce
     quando a mãe nascer — e o teste cobra a ausência, para ninguém "consertar"
     isso com um href inventado. */
  ok(`${g.slice(0, 26)}…: sem frase de mãe enquanto /guias/ não existe`,
    servido[g].cluster.frase === '');
}

/* ---------------------------------------------------------------------------
 * ÓRFÃ — DUAS AFIRMAÇÕES DIFERENTES, E MISTURAR AS DUAS MEDE A ERRADA
 *
 * A primeira versão desta seção contou só os links do <main> e reprovou
 * `/sobre/` com zero. O defeito era da régua, não da página: `/sobre/` está no
 * menu e no rodapé de todas as treze, então o robô acha — que é exatamente o
 * que o 16.4(f) existe para garantir ("Página que ninguém linka, o robô não
 * acha"). Contar só o corpo era uma régua MAIS dura que a regra, e falha por
 * régua errada é a pior de todas.
 *
 * Só que contar a página inteira sozinho não mede nada: como o menu aponta
 * Calculadoras, Metodologia e Sobre em toda página, essas três passariam
 * sempre, inclusive no dia em que ninguém mais as citasse. Teste que não pode
 * ficar vermelho é teste que não mede — a cicatriz do teste que mede a si mesmo.
 *
 * Então são duas afirmações, com nomes diferentes:
 *   (a) 16.4(f), literal: pelo menos 2 páginas apontam para ela no HTML servido,
 *       contando navegação. Vale para as treze.
 *   (b) A promessa do cluster: as páginas DA ÁRVORE — calculadoras e guias —
 *       recebem link do CORPO de outra página, que é onde a autoridade escorre.
 *       Não vale para as páginas de raiz, que vivem da navegação por desenho.
 *
 * O que a medição (b) deixou registrado, e não é defeito desta entrega:
 * `/sobre/` é a única das treze que nenhum corpo cita. Fica para a pauta.
 * ------------------------------------------------------------------------- */

console.log('\nÓRFÃ (16.4f) — 2 páginas ou mais apontam para ela, no HTML servido');
const apontamNoHtml = {};
const apontamNoCorpo = {};
for (const slug of TODAS) {
  apontamNoHtml[slug] = new Set();
  apontamNoCorpo[slug] = new Set();
}
for (const origem of TODAS) {
  const varre = (texto, onde) => {
    for (const m of texto.matchAll(/href="(https:\/\/aquametria\.com\.br\/[^"]*)"/g)) {
      const destino = slugDaUrl(m[1]);
      if (destino && destino !== origem && onde[destino]) onde[destino].add(origem);
    }
  };
  varre(servido[origem].html, apontamNoHtml);
  varre(servido[origem].corpo, apontamNoCorpo);
}
for (const slug of TODAS) {
  const n = apontamNoHtml[slug].size;
  ok(`${slug.slice(0, 30)}: ${n} página(s) apontam`, n >= 2, n < 2 ? [...apontamNoHtml[slug]].join(',') : '');
}

console.log('\nO CLUSTER ESCORRE DE VERDADE — página da árvore citada no CORPO de outra');
for (const slug of [...CALCULADORAS, ...GUIAS, 'calculadoras']) {
  const n = apontamNoCorpo[slug].size;
  ok(`${slug.slice(0, 30)}: ${n} corpo(s) a citam`, n >= 1);
}

console.log(`\n${falhas === 0 ? 'PASSOU' : 'REPROVOU'} — ${falhas} falha(s)`);
process.exit(falhas === 0 ? 0 : 1);

// AS TREZE PÁGINAS NUM CHROMIUM DE VERDADE, depois que a árvore chegou nelas.
//
//   for p in <as treze>; do php ferramentas/render-pagina-completa.php . $p > /tmp/aqmp-$p.html; done
//   node ferramentas/teste-navegador-arvore.mjs /tmp
//
// POR QUE ELE EXISTE, ao lado do teste-navegador-casca-paginas.mjs: aquele mede
// as QUATRO páginas da casca, montadas pelo render-casca-pagina.php. A trilha e
// o cluster da casca 1.5.0 nascem nas TREZE, e as nove de conteudo/ nunca foram
// medidas inteiras em navegador nenhum — só o shortcode solto era.
//
// O QUE SE MEDE AQUI, e não dá para medir sem navegador:
//
//   1. ROLAGEM HORIZONTAL. A trilha é uma fileira que não quebra linha, e
//      fileira que não quebra é a maneira mais fácil de empurrar a largura da
//      página no celular. Ela rola DENTRO da própria caixa de propósito — este
//      teste é quem prova que a caixa segura e a página não rola.
//   2. A TRILHA CABE NA TELA. Rolagem zero pode significar "está tudo certo" ou
//      "a trilha vazou para fora do viewport e ninguém viu". Então mede-se
//      também que o retângulo dela começa dentro da tela.
//   3. CONSOLE LIMPO.
//
// O TAMANHO DA PÁGINA MEDIDA SAI IMPRESSO, sempre: bancada que serve menos que
// o site mede a metade errada sem erro nenhum aparecer, e foi assim que a
// Robometria mediu 915 KB do que no ar tem 960 KB (seção 8 do ARQUIPELAGO.md).
//
// 390 px é o iPhone da vida real; 360 px é o Android mais estreito que ainda
// aparece; 781, 782 e 783 cercam a quebra do menu sanfona — a borda é onde o
// defeito mora.

import { chromium } from 'playwright';

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const PAGINAS = [
  'inicio',
  'calculadoras',
  'metodologia',
  'sobre',
  'divulgacao-de-afiliados',
  'calculadora-de-litragem',
  'calculadora-de-vazao-do-filtro',
  'calculadora-de-potencia-do-aquecedor',
  'calculadora-de-midia-filtrante',
  'calculadora-de-iluminacao',
  'quantos-watts-de-aquecedor-para-aquario',
  'quanta-midia-biologica-o-aquario-precisa',
  'quantos-lumens-por-litro-aquario-plantado',
  /* O eixo /peixes/ inteiro — leva 1 (12/09/2026) e leva 2 (12/09/2026).
     Estas nove entraram aqui na leva 2, e entraram porque são as páginas com
     MAIS tabela larga da ilha: a ficha serve até quatro tabelas, uma delas com
     cinco colunas de número. Tabela é o caso que a seção 6 do contrato deixa
     estourar a largura, e só dentro do próprio `overflow-x: auto` — medir isso
     a 360 px é a diferença entre a regra e a esperança de que ela valha. */
  'peixes',
  'tetras',
  'quantos-litros-para-tetra-neon',
  'quantos-litros-para-tetra-cardinal',
  'quantos-litros-para-mato-grosso',
  'quantos-litros-para-tetra-ember',
  'quantos-litros-para-tetra-brilhante',
  'quantos-litros-para-rodostomo',
  'quantos-litros-para-tetra-negro',
];
const LARGURAS = [360, 390, 781, 782, 783, 1200];

/* Seção 8 do contrato: página fina é reprovação, e a mesma trava que mede o
   corpo é a que denuncia bancada servindo metade da página. */
const CORPO_MINIMO = 1500;

let falhas = 0;
let medicoes = 0;
function ok(nome, cond, extra = '') {
  console.log(`  ${cond ? 'ok   ' : 'FALHA'} ${nome}${extra ? ' — ' + extra : ''}`);
  medicoes++;
  if (!cond) falhas++;
}

const browser = await chromium.launch({ executablePath: CHROME });

for (const slug of PAGINAS) {
  console.log(`\n/${slug === 'inicio' ? '' : slug + '/'}`);
  const erros = [];
  const page = await browser.newPage();
  page.on('console', (m) => {
    if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|TUNNEL|PROXY)/.test(m.text())) {
      erros.push(m.text());
    }
  });
  page.on('pageerror', (e) => erros.push(String(e)));

  await page.goto('file://' + DIR + '/aqmp-' + slug + '.html');

  const corpo = await page.evaluate(
    () => (document.querySelector('main') || document.body).innerText.length
  );
  console.log(`       corpo medido: ${corpo} caracteres`);
  ok(`corpo acima do piso de ${CORPO_MINIMO}`, corpo >= CORPO_MINIMO, `${corpo}`);

  for (const w of LARGURAS) {
    await page.setViewportSize({ width: w, height: 900 });
    const m = await page.evaluate(() => {
      const doc = document.documentElement;
      const trilha = document.querySelector('.aqm-trilha');
      const veja = document.querySelector('.aqm-veja');
      const r = (el) => {
        if (!el) return null;
        const b = el.getBoundingClientRect();
        return { esq: Math.round(b.left), dir: Math.round(b.right), alt: Math.round(b.height) };
      };
      return {
        sobra: Math.max(0, doc.scrollWidth - doc.clientWidth),
        trilha: r(trilha),
        veja: r(veja),
        larguraTela: doc.clientWidth,
      };
    });
    ok(`sem rolagem horizontal a ${w} px`, m.sobra === 0, `${m.sobra} px`);

    /* A trilha existe em doze das treze; onde ela existe, tem que estar dentro
       da tela e ter altura de verdade (bloco com altura zero é bloco que não
       aparece, e isso passaria despercebido numa medida só de rolagem). */
    if (m.trilha) {
      ok(`trilha dentro da tela a ${w} px`,
        m.trilha.esq >= 0 && m.trilha.esq < m.larguraTela && m.trilha.alt > 0,
        `esq ${m.trilha.esq}, alt ${m.trilha.alt}`);
    }
    if (m.veja) {
      ok(`bloco "Veja também" dentro da tela a ${w} px`,
        m.veja.esq >= 0 && m.veja.dir <= m.larguraTela + 1 && m.veja.alt > 0,
        `esq ${m.veja.esq}, dir ${m.veja.dir}, alt ${m.veja.alt}`);
    }
  }

  ok('console sem mensagem', erros.length === 0, erros.slice(0, 2).join(' | '));
  await page.close();
}

await browser.close();
console.log(`\n${medicoes} medições · ${falhas} falha(s)`);
console.log(falhas === 0 ? 'TUDO OK' : 'REPROVOU');
process.exit(falhas === 0 ? 0 : 1);

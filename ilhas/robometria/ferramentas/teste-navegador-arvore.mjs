// AS NOVE PÁGINAS NUM CHROMIUM DE VERDADE, depois que a árvore chegou nelas.
//
//   for a in home ferramentas metodologia sobre afiliados r1 r2 a1 a2; do \
//     php ferramentas/render-para-teste.php . robometria_$a > /tmp/rbm-$a.html; done
//   node ferramentas/teste-navegador-arvore.mjs /tmp
//
// O QUE SE MEDE AQUI, e não dá para medir sem navegador:
//
//   1. ROLAGEM HORIZONTAL. A trilha é uma fileira que não quebra linha, e fileira
//      que não quebra é a maneira mais fácil de empurrar a largura da página no
//      celular. Ela rola DENTRO da própria caixa de propósito — este teste é quem
//      prova que a caixa segura e a página não rola.
//   2. A TRILHA CABE NA TELA. Rolagem zero pode significar "está tudo certo" ou
//      "a trilha vazou para fora do viewport e ninguém viu". Então mede-se também
//      que o retângulo dela começa dentro da tela, e que ela é visível.
//   3. A TRILHA ESTÁ ACIMA DO H1 na tela, não só na ordem do HTML: a 16.3 fala de
//      onde o leitor vê a trilha, e CSS pode reordenar o que o HTML ordenou.
//   4. CONSOLE LIMPO.
//
// O TAMANHO DA PÁGINA MEDIDA SAI IMPRESSO, sempre: bancada que serve menos que o
// site mede a metade errada sem erro nenhum aparecer, e foi assim que esta ilha
// mediu 915 KB do que no ar tem 960 KB (seção 8 do ARQUIPELAGO.md).
//
// 390 px é o iPhone da vida real; 360 px é o Android mais estreito que ainda
// aparece; 781, 782 e 783 cercam a quebra do menu sanfona — a borda é onde o
// defeito mora.

// O playwright desta máquina é global, e import de módulo ES não olha NODE_PATH.
// Resolvê-lo por createRequire mantém o arquivo rodável sem instalar nada dentro
// da ilha — e RBM_NODE_MODULES troca o caminho em outra máquina.
import { createRequire } from 'node:module';
const exigir = createRequire(process.env.RBM_NODE_MODULES || '/opt/node22/lib/node_modules/');
const { chromium } = exigir('playwright');

const DIR = process.argv[2] || '/tmp';
const CHROME = process.env.RBM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const PAGINAS = [
  ['home', false],
  ['ferramentas', true],
  ['metodologia', true],
  ['sobre', true],
  ['afiliados', true],
  ['r1', true],
  ['r2', true],
  ['a1', true],
  ['a2', true],
];

const LARGURAS = [360, 390, 781, 782, 783, 1200];

let falhas = 0;
let feitos = 0;

function ok(condicao, rotulo, medida = '') {
  feitos++;
  if (condicao) {
    console.log(`  ok   ${rotulo.padEnd(58)} ${medida}`);
    return true;
  }
  falhas++;
  console.log(`  FALHA ${rotulo.padEnd(58)} ${medida}`);
  return false;
}

const navegador = await chromium.launch({ executablePath: CHROME });

for (const [nome, temTrilha] of PAGINAS) {
  const arquivo = `file://${DIR}/rbm-${nome}.html`;
  const pagina = await navegador.newPage();
  const recados = [];
  /* A casca carrega as fontes do Google, e nesta maquina a saida passa por um
     proxy que recusa. O erro de rede que isso gera nao e defeito da pagina — e
     a unica mensagem de console que este teste perdoa, pelo nome do erro. */
  pagina.on('console', (m) => {
    if (m.type() === 'error' && !/ERR_(CONNECTION|NAME|INTERNET|TUNNEL|PROXY|ABORTED|FAILED)/.test(m.text())) {
      recados.push(`${m.type()}: ${m.text()}`);
    }
  });
  pagina.on('pageerror', (e) => recados.push(`pageerror: ${e.message}`));
  await pagina.goto(arquivo, { waitUntil: 'domcontentloaded' });

  for (const largura of LARGURAS) {
    await pagina.setViewportSize({ width: largura, height: 900 });

    const medida = await pagina.evaluate(() => {
      const trilha = document.querySelector('.rbm-trilha');
      const h1 = document.querySelector('h1');
      const r = trilha ? trilha.getBoundingClientRect() : null;
      const rh = h1 ? h1.getBoundingClientRect() : null;
      return {
        rolagem: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
        bytes: document.documentElement.outerHTML.length,
        temTrilha: !!trilha,
        trilhaEsq: r ? Math.round(r.left) : null,
        trilhaDir: r ? Math.round(r.right) : null,
        trilhaVisivel: r ? r.height > 0 : false,
        trilhaAcimaDoH1: r && rh ? r.top < rh.top : null,
        veja: document.querySelectorAll('.rbm-veja').length,
      };
    });

    ok(medida.rolagem === 0, `[${nome} @${largura}] rolagem horizontal zero`,
      `${medida.rolagem} px, ${medida.bytes} bytes`);
    ok(medida.temTrilha === temTrilha, `[${nome} @${largura}] trilha ${temTrilha ? 'presente' : 'ausente'}`);
    if (temTrilha) {
      ok(medida.trilhaVisivel && medida.trilhaEsq >= 0 && medida.trilhaEsq < largura,
        `[${nome} @${largura}] a trilha comeca dentro da tela`,
        `esq ${medida.trilhaEsq}, dir ${medida.trilhaDir}`);
      ok(medida.trilhaAcimaDoH1 === true, `[${nome} @${largura}] a trilha esta acima do H1 na tela`);
    }
    ok(recados.length === 0, `[${nome} @${largura}] console sem mensagem`, recados.slice(0, 1).join(' '));
  }

  await pagina.close();
}

await navegador.close();

console.log(`\n${falhas ? 'REPROVADO' : 'APROVADO'}: ${feitos} medicoes, ${falhas} falha(s).`);
process.exit(falhas ? 1 : 0);

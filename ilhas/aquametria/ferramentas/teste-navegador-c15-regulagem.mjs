// O portao da REGULAGEM da C15 (bloco T3a, 12/09/2026).
//
// O defeito que este arquivo existe para impedir de voltar, medido no ar em
// 12/09/2026: o mesmo banco escrevia o mesmo fato de duas maneiras. Seis
// registros da familia Chihiros WRGB II gravavam regulagem 'aplicativo'; a irma
// chihiros-wrgb-ii-pro-60, colhida na MESMA leva e da MESMA fonte, gravava
// 'app'. O vocabulario do esquema declara 'app'. O podeRegular() do JavaScript
// tinha uma TERCEIRA copia da lista, digitada dentro dele, e testava 'app'.
// Resultado: 5 das 8 luminarias do catalogo que declaram regulagem eram
// invisiveis para o ramo dos "reguláveis", e a pagina afirmava sobre elas que
// "não declara regulagem de intensidade" — contradizendo o proprio banco, que
// listava 'regulagem' entre os campos que a fonte sustenta.
//
// Nenhum portao via, e a razao vale mais que o defeito: o validador nunca lia a
// chave 'vocabulario' do esquema, e o teste de navegador media a lista de
// produtos "dentro da faixa", onde o defeito nao aparece. Um ramo inteiro da
// pagina — os reguláveis — estava inalcancavel para quase todo o catalogo, e um
// ramo que nunca executa nao reprova em teste nenhum.
//
// O que este teste mede, e por que cada um:
//
//   1. AS DUAS FONTES DIZEM A MESMA COISA. AQM_C15_REGULA (o que chegou ao
//      snippet) e igual a 'regulagem.regula_intensidade' do esquema (a fonte).
//      E a afirmacao que cobra que o gerador tenha rodado.
//   2. O RAMO E ALCANCAVEL. Varrida a entrada inteira, o ramo dos reguláveis
//      produz cartao em pelo menos um estado. Com o defeito no ar esta
//      afirmacao reprovava sozinha, e nenhuma outra reprovava.
//   3. A TELA BATE COM A REGUA PROPRIA, cartao por cartao, nos 69 estados.
//      A regua le dados/produtos-iluminacao.json e dados/esquema-produtos.json
//      DIRETO — nunca AQM_C15_CATALOGO, nunca aquametria_c15_catalogo(), nunca
//      AQM_C15_REGULA. Regua que chama quem produziu o dado erra junto com ele.
//   4. A FRASE COLAPSADA MORREU. "não declara regulagem de intensidade" nao
//      aparece em lugar nenhum do corpo, em nenhum dos 69 estados.
//   5. OS TRES ESTADOS TEM TRES FRASES. Campo vazio (a ilha nao colheu),
//      'nenhuma' (o fabricante declara que nao tem) e valor que regula sao
//      afirmacoes diferentes, e a pagina nunca atribui ao fabricante o silencio
//      que e nosso.
//
// Tudo e medido no CORPO da lista de produtos (secao 8 do ARQUIPELAGO.md),
// nunca no HTML completo: a frase proibida aparece legitimamente dentro da
// documentacao do proprio snippet, e procura-la na pagina inteira acharia o
// comentario em vez da tela.
//
//   npm i --no-save playwright
//   php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
//   node ferramentas/teste-navegador-c15-regulagem.mjs /tmp/c15.html

import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

const ARQUIVO = process.argv[2] || '/tmp/c15.html';
const CHROME = process.env.AQM_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

/* ------------------------------------------------------- a regua, escrita aqui */

// As faixas consolidadas por nivel, em lm/L, e a secao transversal usada para
// derivar o volume do comprimento. Repetidas de proposito: regua que importa a
// constante de quem produz o dado erra junto com ele. Se a pagina mudar a faixa,
// este teste passa a discordar dela — e discordar e o resultado util.
const NIVEIS = {
  baixa: { min: 10, max: 20, aberto: false },
  media: { min: 20, max: 40, aberto: false },
  alta:  { min: 40, max: 60, aberto: true  }
};
const LARGURA_CM = 40, ALTURA_CM = 40;

const banco = JSON.parse(readFileSync('dados/produtos-iluminacao.json', 'utf8'));
const esquema = JSON.parse(readFileSync('dados/esquema-produtos.json', 'utf8'));

const declIluminacao = esquema.entidades.iluminacao;
const declRegulagem = declIluminacao.campos.find((c) => c.campo === 'regulagem') || {};
const REGULA_ESQUEMA = declRegulagem.regula_intensidade || [];
const VOCABULARIO = declRegulagem.vocabulario || [];
const EXIGIDOS = declIluminacao.minimo_para_sugerir['c15-iluminacao'];

function preenchido(v) {
  if (v === null || v === undefined) return false;
  if (Array.isArray(v)) return v.length > 0;
  if (typeof v === 'object') return Object.values(v).some((x) => x !== null && x !== undefined);
  if (typeof v === 'string') return v.trim() !== '';
  return true;
}

function conservadorDe(p, campo) {
  for (const c of p.conflitos || []) {
    if (c.campo === campo && c.tratamento === 'intersecao-conservadora') return c.valor_conservador;
  }
  return null;
}

function valorDe(p, campo) {
  if (campo.startsWith('conflito:')) return conservadorDe(p, campo.slice('conflito:'.length));
  return p[campo];
}

// Quem o esquema deixa a C15 sugerir. Mesma leitura do minimo_para_sugerir, feita
// aqui e nao chamada de la.
const sugeriveis = banco.produtos.filter((p) => {
  if (p.status_registro === 'rascunho' || p.status_registro === 'revalidar') return false;
  return EXIGIDOS.every((req) => req.split(' OU ').some((alt) => preenchido(valorDe(p, alt.trim()))));
});

function cobre(p, cm) {
  const c = p.comprimento_aquario_cm || {};
  const mn = typeof c === 'number' ? c : c.min;
  const mx = typeof c === 'number' ? c : c.max;
  if (mn !== null && mn !== undefined && cm < mn) return false;
  if (mx !== null && mx !== undefined && cm > mx) return false;
  return true;
}

const regula = (p) => !!p.regulagem && REGULA_ESQUEMA.indexOf(p.regulagem) !== -1;

// A regua de um estado: quem a pagina DEVE desenhar, na ordem em que deve.
function esperado(cm, nivelId) {
  const n = NIVEIS[nivelId];
  const V = Math.round(cm * LARGURA_CM * ALTURA_CM / 1000);
  const min = V * n.min, max = V * n.max;

  const dentro = [], reguláveis = [];
  for (const p of sugeriveis) {
    if (!cobre(p, cm)) continue;
    if (p.fluxo_lm >= min && (n.aberto || p.fluxo_lm <= max)) { dentro.push(p); continue; }
    if (p.fluxo_lm > max && regula(p)) { reguláveis.push(p); }
  }
  const meio = (min + max) / 2;
  dentro.sort((a, b) => Math.abs(a.fluxo_lm - meio) - Math.abs(b.fluxo_lm - meio));
  reguláveis.sort((a, b) => a.fluxo_lm - b.fluxo_lm);
  return { V, min, max, dentro, reguláveis: reguláveis.slice(0, 2) };
}

/* ------------------------------------------------------------------ a medicao */

let ok = 0;
const falhas = [];
function conferir(nome, condicao, detalhe) {
  if (condicao) { ok++; return; }
  falhas.push(nome + (detalhe ? ' — ' + detalhe : ''));
}

const navegador = await chromium.launch({ executablePath: CHROME });
const pagina = await navegador.newPage();
// Erro de VERDADE e excecao de JavaScript (pageerror), que e a convencao dos
// outros testes desta ilha. Falha de CARREGAMENTO de recurso nao entra: a
// bancada roda num egresso que barra fonts.googleapis.com, entao toda pagina
// medida aqui acumula ERR_TUNNEL_CONNECTION_FAILED das fontes. Contar isso como
// defeito faria o portao reprovar sempre, e portao que reprova sempre e
// desligado na semana seguinte. O que interessa e que nenhuma linha da
// calculadora estourou.
const erros = [];
pagina.on('pageerror', (e) => erros.push(String(e)));
const consoleSujo = [];
pagina.on('console', (m) => {
  if (m.type() !== 'error') return;
  if (/ERR_|Failed to load resource/.test(m.text())) return;
  consoleSujo.push(m.text());
});
await pagina.goto('file://' + (ARQUIVO.startsWith('/') ? ARQUIVO : process.cwd() + '/' + ARQUIVO));

// 1. As duas fontes dizem a mesma coisa.
const regulaNaTela = await pagina.evaluate(() => (typeof AQM_C15_REGULA === 'undefined' ? null : AQM_C15_REGULA));
conferir('AQM_C15_REGULA chegou ao snippet', Array.isArray(regulaNaTela), 'valor: ' + JSON.stringify(regulaNaTela));
conferir('AQM_C15_REGULA e igual ao regula_intensidade do esquema',
  JSON.stringify(regulaNaTela) === JSON.stringify(REGULA_ESQUEMA),
  'tela=' + JSON.stringify(regulaNaTela) + ' esquema=' + JSON.stringify(REGULA_ESQUEMA));
conferir('regula_intensidade nao inventa valor fora do vocabulario',
  REGULA_ESQUEMA.every((v) => VOCABULARIO.includes(v)),
  'vocabulario=' + JSON.stringify(VOCABULARIO));
conferir('o esquema declara pelo menos um comando que regula', REGULA_ESQUEMA.length > 0);

// 1b. NÃO EXISTE SEGUNDA CÓPIA DA LISTA, e esta afirmação é estrutural de
// propósito. Devolver a lista para dentro do podeRegular() com os MESMOS valores
// não muda um byte na tela: as duas cópias concordam no dia em que nascem, e a
// divergência chega depois, quando alguém mexe numa e esquece a outra — que foi
// exatamente a história deste bloco. Uma mutação que só troca a fonte única por
// uma cópia idêntica é inerte para qualquer medição de resultado, e ficou
// inerte de verdade na primeira rodada de mutações. O que ela ameaça não é um
// valor, é a estrutura; então é a estrutura que se mede. Medido DENTRO do corpo
// da função, nunca na página inteira: os valores aparecem legitimamente no
// catálogo embutido e na documentação do snippet.
const corpoPodeRegular = await pagina.evaluate(() => {
  const fonte = Array.from(document.querySelectorAll('script'))
    .map((s) => s.textContent || '').join('\n');
  const i = fonte.indexOf('function podeRegular(');
  if (i === -1) return null;
  const abre = fonte.indexOf('{', i);
  let nivel = 0;
  for (let j = abre; j < fonte.length; j++) {
    if (fonte[j] === '{') nivel++;
    else if (fonte[j] === '}') { nivel--; if (nivel === 0) return fonte.slice(abre, j + 1); }
  }
  return null;
});
conferir('o corpo de podeRegular() foi encontrado no script servido', corpoPodeRegular !== null);
if (corpoPodeRegular !== null) {
  conferir('podeRegular() lê a fonte única (AQM_C15_REGULA)',
    corpoPodeRegular.indexOf('AQM_C15_REGULA') !== -1,
    corpoPodeRegular.replace(/\s+/g, ' ').slice(0, 160));
  const literais = VOCABULARIO.filter((v) => corpoPodeRegular.indexOf("'" + v + "'") !== -1
    || corpoPodeRegular.indexOf('"' + v + '"') !== -1);
  conferir('podeRegular() não guarda uma segunda cópia da lista',
    literais.length === 0,
    'valores digitados no corpo da função: ' + JSON.stringify(literais));
}

// A varredura: comprimento de 30 a 140 de 5 em 5, nos tres niveis. Vai ate 140
// de proposito — 125 a 140 cm e a borda superior da cobertura declarada da
// familia WRGB II, e borda e onde ceil se separa de floor+1.
const COMPRIMENTOS = [];
for (let cm = 30; cm <= 140; cm += 5) COMPRIMENTOS.push(cm);

const FRASE_MORTA = 'não declara regulagem de intensidade';
let estadosComRegulavel = 0, cartoesRegulaveis = 0, estados = 0;

for (const nivelId of Object.keys(NIVEIS)) {
  for (const cm of COMPRIMENTOS) {
    const e = esperado(cm, nivelId);
    estados++;

    await pagina.fill('#aqm-c15-volume', String(e.V));
    await pagina.fill('#aqm-c15-comprimento', String(cm));
    await pagina.fill('#aqm-c15-lamina', '40');
    await pagina.selectOption('#aqm-c15-nivel', nivelId);
    await pagina.click('#aqm-c15-form button[type="submit"]');

    // Medido no CORPO da lista, nunca no HTML da pagina.
    const cartoes = await pagina.$$eval('#aqm-c15-produtos-lista .aqm-c15-produto', (els) =>
      els.map((el) => ({
        titulo: (el.querySelector('h4') || {}).textContent || '',
        regulavel: el.classList.contains('aqm-c15-produto-regulavel'),
        texto: el.textContent || ''
      })));

    const rotulo = nivelId + ' / ' + cm + ' cm';
    const nomesEsperados = e.dentro.concat(e.reguláveis)
      .map((p) => [p.marca, p.modelo].filter(Boolean).join(' '));
    const nomesNaTela = cartoes.map((c) => c.titulo.trim());
    conferir('a lista da tela bate com a regua (' + rotulo + ')',
      JSON.stringify(nomesNaTela) === JSON.stringify(nomesEsperados),
      'tela=' + JSON.stringify(nomesNaTela) + ' regua=' + JSON.stringify(nomesEsperados));

    const regulaveisNaTela = cartoes.filter((c) => c.regulavel).map((c) => c.titulo.trim());
    const regulaveisEsperados = e.reguláveis.map((p) => [p.marca, p.modelo].filter(Boolean).join(' '));
    conferir('o grupo "regulável" bate com a regua (' + rotulo + ')',
      JSON.stringify(regulaveisNaTela) === JSON.stringify(regulaveisEsperados),
      'tela=' + JSON.stringify(regulaveisNaTela) + ' regua=' + JSON.stringify(regulaveisEsperados));

    if (regulaveisEsperados.length) { estadosComRegulavel++; cartoesRegulaveis += regulaveisEsperados.length; }

    // A faixa ALTA e aberta por cima: a fonte publica "acima de 40 lm/L" e para
    // ai. Logo nada nunca esta "acima do teto" nela, e um cartao regulável na
    // alta significaria que alguem fechou a faixa aberta sem dizer — defeito, e
    // nao melhora. Esta e a afirmacao que separa "o ramo voltou a funcionar" de
    // "o ramo passou a funcionar demais".
    if (NIVEIS[nivelId].aberto) {
      conferir('faixa aberta nao produz cartao regulável (' + rotulo + ')',
        regulaveisNaTela.length === 0,
        'tela=' + JSON.stringify(regulaveisNaTela));
    }

    // 4. A frase colapsada morreu, no corpo de todos os estados.
    const corpo = await pagina.$eval('#aqm-c15-saida', (el) => el.textContent || '').catch(() => '');
    conferir('a frase colapsada sumiu do corpo (' + rotulo + ')',
      corpo.indexOf(FRASE_MORTA) === -1,
      'achada em ' + rotulo);

    // 5c. A FICHA de quem nao tem regulagem colhida diz que o silencio e NOSSO.
    // Esta afirmacao nasceu de uma mutacao que PASSOU: a linha da ficha voltava a
    // dizer "não declarada" — que atribui ao fabricante o que a ilha nao foi
    // perguntar — e nada reprovava, porque o teste so media a frase da LISTA.
    for (const c of cartoes) {
      const reg = sugeriveis.find((p) => [p.marca, p.modelo].filter(Boolean).join(' ') === c.titulo.trim());
      if (!reg || preenchido(reg.regulagem)) continue;
      conferir('a ficha do campo vazio diz que nao colhemos (' + rotulo + ': ' + c.titulo.trim() + ')',
        c.texto.indexOf('não colhemos este campo') !== -1,
        'ficha sem a frase');
      conferir('a ficha do campo vazio nao diz "não declarada" (' + rotulo + ': ' + c.titulo.trim() + ')',
        c.texto.indexOf('não declarada') === -1);
    }

    // 5. Cada cartao regulavel diz QUAL comando regula, e nunca a frase de silencio.
    for (const c of cartoes.filter((x) => x.regulavel)) {
      conferir('cartao regulável nomeia a regulagem (' + rotulo + ': ' + c.titulo.trim() + ')',
        REGULA_ESQUEMA.some((v) => c.texto.indexOf(v) !== -1),
        'texto sem nenhum valor de regulagem');
      conferir('cartao regulável nao diz que nao colhemos (' + rotulo + ': ' + c.titulo.trim() + ')',
        c.texto.indexOf('não colheu') === -1 && c.texto.indexOf('não colhemos este campo') === -1);
    }
  }
}

// 2. O ramo e alcancavel. Com o defeito no ar, esta afirmacao reprovava sozinha.
conferir('o ramo dos reguláveis e alcancavel na varredura',
  estadosComRegulavel > 0,
  estadosComRegulavel + ' estado(s) com cartao regulável');

// 5b. Os tres estados sao distinguiveis: existe no catalogo pelo menos um
// registro sem regulagem colhida, e a pagina fala DELE sem culpar o fabricante.
const semColheita = sugeriveis.filter((p) => !preenchido(p.regulagem));
conferir('o catalogo ainda tem registro com regulagem nao colhida',
  semColheita.length > 0, semColheita.length + ' registro(s)');

if (semColheita.length) {
  // Um estado em que um deles apareca acima do teto: a Ista I-401 (810 lm, 45 cm)
  // com exigencia baixa num aquario de 45 cm pede 720 a 1.440 lm, entao ela cai
  // DENTRO; para achar um estado de silencio de verdade, varremos.
  let achou = null;
  for (const nivelId of Object.keys(NIVEIS)) {
    for (const cm of COMPRIMENTOS) {
      const e = esperado(cm, nivelId);
      const foraPorTeto = sugeriveis.filter((p) => cobre(p, cm) && p.fluxo_lm > e.max && !regula(p) && !preenchido(p.regulagem));
      if (foraPorTeto.length) { achou = { cm, nivelId, alvo: foraPorTeto[0] }; break; }
    }
    if (achou) break;
  }
  conferir('existe estado em que a pagina fala de peca sem regulagem colhida', !!achou);
  if (achou) {
    const e = esperado(achou.cm, achou.nivelId);
    await pagina.fill('#aqm-c15-volume', String(e.V));
    await pagina.fill('#aqm-c15-comprimento', String(achou.cm));
    await pagina.fill('#aqm-c15-lamina', '40');
    await pagina.selectOption('#aqm-c15-nivel', achou.nivelId);
    await pagina.click('#aqm-c15-form button[type="submit"]');
    const corpo = await pagina.$eval('#aqm-c15-saida', (el) => el.textContent || '');
    conferir('o silencio e NOSSO e a pagina diz isso',
      corpo.indexOf('não colheu') !== -1 || corpo.indexOf('não colhemos') !== -1,
      achou.nivelId + ' / ' + achou.cm + ' cm, alvo ' + achou.alvo.id);
    conferir('a pagina nao atribui esse silencio ao fabricante',
      corpo.indexOf(FRASE_MORTA) === -1);
  }
}

conferir('nenhuma excecao de JavaScript nos 69 estados', erros.length === 0, erros.join(' | '));
conferir('console sem erro que nao seja de rede', consoleSujo.length === 0, consoleSujo.join(' | '));

await navegador.close();

console.log('estados varridos: ' + estados
  + ' | estados com cartao regulável: ' + estadosComRegulavel
  + ' | cartoes reguláveis: ' + cartoesRegulaveis);
console.log('afirmacoes: ' + (ok + falhas.length) + ' | aprovadas: ' + ok + ' | falhas: ' + falhas.length);
for (const f of falhas.slice(0, 25)) console.log('  FALHA ' + f);
process.exit(falhas.length ? 1 : 0);

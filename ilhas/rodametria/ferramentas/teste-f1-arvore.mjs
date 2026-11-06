/**
 * PORTAO DA ARVORE DA F1 NO NAVEGADOR — sem rede e sem navegador.
 *
 * A arvore da F1 esta escrita DUAS vezes de proposito, e isso e a secao 8 do
 * ARQUIPELAGO.md e nao descuido: *"a regua da DECISAO se escreve duas vezes de
 * proposito, porque e ali que a divergencia ensina algo"*. Uma mora em
 * `regras/f1.py` (e o PHP a serve pre-renderizada); a outra mora no JS do
 * rodape de `snippets/rodametria-f1.php`, que e quem responde quando a pessoa
 * troca um campo.
 *
 * O PROBLEMA QUE ESTE ARQUIVO RESOLVE: `ferramentas/teste-f1.py` confere a
 * arvore do CEREBRO contra uma arvore escrita a mao em Python, e nao alcanca o
 * JS. Sem este portao, a metade da ferramenta que a PESSOA de fato usa — a que
 * recomputa no navegador — nao tinha regua nenhuma, e divergir dela e divergir
 * calado: a caixa pre-renderizada diria uma coisa e o primeiro clique diria
 * outra, as duas com cara de certas. E a cicatriz literal da secao 8 desta
 * ilha, *"as duas metades nunca se falavam"*, no unico lugar onde ela ainda
 * podia acontecer.
 *
 * COMO ELE MEDE, e por que nao e circular:
 *
 *   1. EXTRAI a funcao `categoria()` do JS servido, do proprio arquivo PHP, por
 *      recorte de texto. Nao reescreve, nao importa, nao adivinha: usa o
 *      MESMO codigo que vai ao ar.
 *   2. ESCREVE UMA TERCEIRA ARVORE, aqui, em JavaScript, a mao, a partir do
 *      texto da secao 1.3 da especificacao e dos artigos da resolucao — nunca
 *      copiando a do PHP nem a do Python.
 *   3. COMPARA as duas sobre a grade dos limiares FICTICIOS, a mesma do
 *      `teste-f1.py`: a grade passa pelos limiares EXATOS, porque mutacao de
 *      fronteira so se ve no veiculo que esta no limite — licao medida em
 *      06/11/2026, quando a bateria do portao em Python passava sobre uma grade
 *      que nunca tocava um limiar.
 *   4. E PROVA QUE MORDE: refaz a arvore de mentira de quatro jeitos e exige
 *      que a comparacao pegue os quatro. Portao que nunca viu vermelho nao
 *      prova que ficaria vermelho.
 *
 * LIMIARES FICTICIOS, DECLARADOS FICTICIOS, pela 1.6 da especificacao: nenhum
 * numero aqui e um numero da resolucao, e os valores sao reconheciveis a olho.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const AQUI = dirname(fileURLToPath(import.meta.url));
const ILHA = dirname(AQUI);
const SNIPPET = join(ILHA, 'snippets', 'rodametria-f1.php');

const FICTICIOS = {
  LIMIAR_BIKE_W: 555,
  LIMIAR_BIKE_KMH: 11,
  LIMIAR_AUTOPROP_W: 777,
  LIMIAR_AUTOPROP_KMH: 22,
  LIMIAR_AUTOPROP_LARGURA_MM: 333,
  LIMIAR_AUTOPROP_ENTRE_EIXOS_MM: 888,
  LIMIAR_CICLOMOTOR_W: 999,
  LIMIAR_CICLOMOTOR_KMH: 44,
};

const falhas = [];
let afirmacoes = 0;
function ok(cond, frase) {
  afirmacoes += 1;
  if (!cond) falhas.push(frase);
}

/* ------------------------------------------------------------------ (1) extrai */

function extrairFuncao(fonte, nome) {
  const abre = fonte.indexOf('function ' + nome + '(');
  if (abre === -1) return null;
  let i = fonte.indexOf('{', abre);
  if (i === -1) return null;
  let nivel = 0;
  for (let j = i; j < fonte.length; j++) {
    const c = fonte[j];
    if (c === '{') nivel += 1;
    else if (c === '}') {
      nivel -= 1;
      if (nivel === 0) return fonte.slice(abre, j + 1);
    }
  }
  return null;
}

const phpFonte = readFileSync(SNIPPET, 'utf8');
const textoDaFuncao = extrairFuncao(phpFonte, 'categoria');

ok(textoDaFuncao !== null,
  'nao achei a funcao `categoria()` dentro do JS de snippets/rodametria-f1.php. ' +
  'Se ela foi renomeada, este portao tem de ser reapontado — e nao pode passar ' +
  'em silencio, porque silencio aqui e a arvore do navegador deixando de ser medida');

/* A funcao do PHP chama `lim(nome)`, que no ar vai ao pacote de dados. Aqui ela
   vai aos limiares FICTICIOS: e assim que o portao afirma a ARVORE em vez dos
   numeros do mundo. */
let categoriaDoNavegador = null;
if (textoDaFuncao) {
  // eslint-disable-next-line no-new-func
  const fabrica = new Function('lim', textoDaFuncao + '; return categoria;');
  categoriaDoNavegador = fabrica((nome) => {
    if (!(nome in FICTICIOS)) {
      throw new Error('a arvore do navegador pediu o limiar ' + nome + ', que nao existe');
    }
    return FICTICIOS[nome];
  });
}

/* ------------------------------------------- (2) a TERCEIRA arvore, escrita aqui */

function arvoreAMao(w, kmh, acel) {
  // Escrita do texto da 1.3 e dos artigos lidos, nao copiada das outras duas.
  // A ordem das recusas e a da 1.1: o pivo decide, e `nao_declarado` nunca cai
  // no lado permissivo por omissao.
  const temNumeros = typeof w === 'number' && typeof kmh === 'number' && w > 0 && kmh > 0;
  const pivoValido = acel === 'manual' || acel === 'so_pedal_assistido';
  if (!temNumeros || !pivoValido) return null;

  const cabeBike = !(w > FICTICIOS.LIMIAR_BIKE_W) && !(kmh > FICTICIOS.LIMIAR_BIKE_KMH);
  if (acel === 'so_pedal_assistido' && cabeBike) return 'bicicleta_eletrica';

  const cabeAuto = !(w > FICTICIOS.LIMIAR_AUTOPROP_W) && !(kmh > FICTICIOS.LIMIAR_AUTOPROP_KMH);
  if (cabeAuto) return 'autopropelido';

  const cabeCiclo = !(w > FICTICIOS.LIMIAR_CICLOMOTOR_W) && !(kmh > FICTICIOS.LIMIAR_CICLOMOTOR_KMH);
  if (cabeCiclo) return 'ciclomotor';

  return 'acima_do_ciclomotor';
}

/* ---------------------------------------------------------------- (3) compara */

// A GRADE PASSA PELOS LIMIARES EXATOS, e os valores sao DERIVADOS dos ficticios
// e nunca digitados: o dia em que alguem trocar os ficticios, a grade acompanha.
const limsW = [...new Set(Object.keys(FICTICIOS).filter((k) => k.endsWith('_W')).map((k) => FICTICIOS[k]))];
const limsKmh = [...new Set(Object.keys(FICTICIOS).filter((k) => k.endsWith('_KMH')).map((k) => FICTICIOS[k]))];
const GRADE_W = [null, 0, ...new Set(limsW.flatMap((v) => [v - 1, v, v + 1])), 99999];
const GRADE_KMH = [null, 0, ...new Set(limsKmh.flatMap((v) => [v - 1, v, v + 1])), 999];
const ACELS = [null, undefined, 'manual', 'so_pedal_assistido', 'nao_declarado'];

function varrer(arvore) {
  let divergiu = 0;
  let total = 0;
  const exemplos = [];
  for (const w of GRADE_W) {
    for (const kmh of GRADE_KMH) {
      for (const acel of ACELS) {
        total += 1;
        const meu = arvoreAMao(w, kmh, acel);
        const dela = arvore(w, kmh, acel);
        if (meu !== dela) {
          divergiu += 1;
          if (exemplos.length < 5) exemplos.push({ w, kmh, acel, meu, dela });
        }
      }
    }
  }
  return { total, divergiu, exemplos };
}

if (categoriaDoNavegador) {
  const r = varrer(categoriaDoNavegador);
  ok(r.divergiu === 0,
    'a arvore do NAVEGADOR discorda da minha em ' + r.divergiu + ' de ' + r.total +
    ' mundos. Primeiros casos: ' + JSON.stringify(r.exemplos));
  console.log('  varredura: ' + r.total + ' mundos, ' + r.divergiu + ' divergencia(s) ' +
    'entre a arvore do navegador e a escrita neste portao');
}

/* ------------------------------------------------------------- (4) as mutacoes */

function semPivo(w, kmh, acel) {
  // MUTACAO 1: o acelerador deixa de decidir — o erro permissivo.
  if (!(w > 0) || !(kmh > 0)) return null;
  if (w <= FICTICIOS.LIMIAR_BIKE_W && kmh <= FICTICIOS.LIMIAR_BIKE_KMH) return 'bicicleta_eletrica';
  return 'autopropelido';
}

function fronteiraEstrita(w, kmh, acel) {
  // MUTACAO 2: `<` no lugar de `<=`, que so se ve no veiculo EXATAMENTE no limite.
  if (!(w > 0) || !(kmh > 0)) return null;
  if (acel !== 'manual' && acel !== 'so_pedal_assistido') return null;
  if (acel === 'so_pedal_assistido' && w < FICTICIOS.LIMIAR_BIKE_W && kmh < FICTICIOS.LIMIAR_BIKE_KMH) {
    return 'bicicleta_eletrica';
  }
  if (w < FICTICIOS.LIMIAR_AUTOPROP_W && kmh < FICTICIOS.LIMIAR_AUTOPROP_KMH) return 'autopropelido';
  if (w < FICTICIOS.LIMIAR_CICLOMOTOR_W && kmh < FICTICIOS.LIMIAR_CICLOMOTOR_KMH) return 'ciclomotor';
  return 'acima_do_ciclomotor';
}

function tresSaidas(w, kmh, acel) {
  // MUTACAO 3: a arvore VELHA da 1.3, que terminava em `senao -> ciclomotor`.
  if (!(w > 0) || !(kmh > 0)) return null;
  if (acel !== 'manual' && acel !== 'so_pedal_assistido') return null;
  if (acel === 'so_pedal_assistido' && w <= FICTICIOS.LIMIAR_BIKE_W && kmh <= FICTICIOS.LIMIAR_BIKE_KMH) {
    return 'bicicleta_eletrica';
  }
  if (w <= FICTICIOS.LIMIAR_AUTOPROP_W && kmh <= FICTICIOS.LIMIAR_AUTOPROP_KMH) return 'autopropelido';
  return 'ciclomotor';
}

function pivoInvertido(w, kmh, acel) {
  // MUTACAO 4: o pivo troca de lado — acelerador manual passa a ser bike.
  if (!(w > 0) || !(kmh > 0)) return null;
  if (acel !== 'manual' && acel !== 'so_pedal_assistido') return null;
  if (acel === 'manual' && w <= FICTICIOS.LIMIAR_BIKE_W && kmh <= FICTICIOS.LIMIAR_BIKE_KMH) {
    return 'bicicleta_eletrica';
  }
  if (w <= FICTICIOS.LIMIAR_AUTOPROP_W && kmh <= FICTICIOS.LIMIAR_AUTOPROP_KMH) return 'autopropelido';
  if (w <= FICTICIOS.LIMIAR_CICLOMOTOR_W && kmh <= FICTICIOS.LIMIAR_CICLOMOTOR_KMH) return 'ciclomotor';
  return 'acima_do_ciclomotor';
}

for (const [nome, m] of [
  ['o acelerador deixa de ser pivo', semPivo],
  ['`<` no lugar de `<=` na fronteira', fronteiraEstrita],
  ['a arvore VELHA, de tres saidas', tresSaidas],
  ['o pivo troca de lado', pivoInvertido],
]) {
  const r = varrer(m);
  ok(r.divergiu > 0, 'a mutacao ' + JSON.stringify(nome) + ' NAO foi pega pela varredura: ' +
    'o portao nao morde nela');
}
console.log('  mutacoes: 4, e a varredura pegou todas');

/* ------------------------------- (5) o JS nao escreve frase e nao digita limiar */

const jsAbre = phpFonte.indexOf('<script id="rodametria-f1-js">');
const jsFecha = phpFonte.indexOf('</script>', jsAbre);
const js = jsAbre === -1 ? '' : phpFonte.slice(jsAbre, jsFecha);
ok(js !== '', 'nao achei o bloco <script> do JS da F1 dentro do snippet');

// (a) NENHUM LIMIAR DIGITADO NO JS. Os valores proibidos saem da constante, nao
// desta lista: a regua continua certa no dia em que a resolucao trocar os numeros.
const constantes = JSON.parse(readFileSync(join(ILHA, 'dados', 'constantes.json'), 'utf8'));
const limiarReal = (constantes.constantes.find(
  (c) => c.id === 'limiares-categoria-contran-996-2023') || {}).valor || {};
// So o CODIGO entra na regua: comentario CITA numero de proposito, e o dia em que
// citar no comentario for proibido e o dia em que ninguem mais registra o que leu.
const jsCodigo = js
  .replace(/\/\*[\s\S]*?\*\//g, '')
  .split('\n').map((l) => l.replace(/\/\/.*$/, '')).join('\n');
for (const [nome, v] of Object.entries(limiarReal)) {
  const re = new RegExp('(?<![\\d.])' + Math.trunc(v) + '(?![\\d.])');
  ok(!re.test(jsCodigo),
    'o JS da F1 traz o literal ' + Math.trunc(v) + ' (valor de ' + nome + ') dentro do ' +
    'codigo. A 1.3 proibe literal numerico de limiar na logica: ele mora na constante e ' +
    'e referenciado por nome');
}

// (b) O JS PREENCHE MOLDE E NAO ESCREVE FRASE. A regua: todo texto longo que o JS
// poe na tela tem de vir de `D.moldes`. String literal longa dentro do JS e frase
// escrita duas vezes — a bateria de mutacoes da F2 reprovou justamente as duas
// versoes em que o JS dela escrevia frase propria.
// A regua procura string longa NUMA LINHA SO (`[^'\n]`), e a primeira versao
// dela usava `[^']`, que atravessa linha e casou 37 pedacos de codigo entre uma
// aspa e a seguinte. Regex que atravessa linha reprova a pagina certa, e a 20.5
// ja ensinou que isso e o caminho mais curto para alguem ignorar o portao.
//
// E ela deixa passar SELETOR e NOME DE CLASSE, que nao sao frase: CSS e atributo
// de dado nao viram texto na tela.
const ehSeletorOuClasse = (s) => /^['"][\w\s.#\-[\]=]+['"]$/.test(s);
const literais = (jsCodigo.match(/'[^'\n]{40,}'|"[^"\n]{40,}"/g) || [])
  .filter((s) => !ehSeletorOuClasse(s));
ok(literais.length === 0,
  'o JS da F1 tem ' + literais.length + ' string(s) longa(s) dentro do codigo, e elas ' +
  'seriam frase escrita duas vezes: ' + JSON.stringify(literais.slice(0, 3)));

// (c) E O JS LE OS MOLDES QUE EXISTEM. Molde pedido por nome que o arquivo de
// respostas nao tem sai como `undefined` na tela, calado.
const respostas = JSON.parse(readFileSync(join(ILHA, 'dados', 'f1-respostas.json'), 'utf8'));
const pedidos = [...new Set([...jsCodigo.matchAll(/D\.moldes\.(\w+)/g)].map((m) => m[1]))];
const pedidosPorChave = [...new Set(
  [...jsCodigo.matchAll(/'(veredito_\w+|placa_\w+|ressalva_\w+|municipal_\w+|recusa_\w+)'/g)]
    .map((m) => m[1]))];
for (const nome of [...pedidos, ...pedidosPorChave]) {
  ok(nome in respostas.frases_molde,
    'o JS pede o molde ' + JSON.stringify(nome) + ' e dados/f1-respostas.json nao o tem: ' +
    'na tela isso sai como `undefined`, calado');
}
console.log('  o JS pede ' + (pedidos.length + pedidosPorChave.length) +
  ' molde(s) e todos existem no arquivo de respostas');

console.log('');
console.log('teste-f1-arvore: ' + afirmacoes + ' afirmacoes, ' + falhas.length + ' falha(s)');
for (const f of falhas.slice(0, 20)) console.log('  FALHA ' + f);
console.log(falhas.length ? 'REPROVADO' : 'APROVADO');
process.exit(falhas.length ? 1 : 0);

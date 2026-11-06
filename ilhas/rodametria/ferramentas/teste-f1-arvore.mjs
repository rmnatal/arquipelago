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

/* -------------------- (6) O QUANTIFICADOR NO JSON-LD, que a prosa nao alcanca
 *
 * MEDIDO NO AR em 06/11/2026: a varredura de quantificador por extenso do portao
 * de ar le o TEXTO VISIVEL, e `corpo_da_pagina()` tira `<script>` antes de medir
 * — com razao, porque ali mora CSS e JSON. Entao o `FAQPage` desta pagina ESCAPA
 * dela, e foi por ali que `costuma` e `0 de 14 declaram` chegaram ao ar, as duas
 * frases que a camada visivel ja nao tinha. E o JSON-LD e justamente a camada que
 * a visao geral de IA ingere: defeito ali vale MAIS que na prosa, nao menos. E a
 * familia da 32.4-b (o comentario de CSS que nenhum portao via) um andar acima.
 *
 * A regua mede o FONTE do snippet e nao o ar, de proposito: ela pega a frase
 * ANTES do desembarque, que e onde ela custa menos. Ela varre as strings longas
 * do PHP que ficam FORA de comentario — a prosa que vai para a pagina e para o
 * JSON-LD — e nao sabe de camada nenhuma, que e o que a fez achar o defeito.
 * -------------------------------------------------------------------------- */
const QUANTIFICADORES = [
  'costuma', 'geralmente', 'normalmente', 'a maioria', 'quase sempre', 'quase nunca',
  'na maior parte', 'o mais comum', 'mais comum', 'em geral', 'tipicamente', 'raramente',
];

// Tira comentarios de bloco e de linha do PHP: comentario CITA o defeito de
// proposito (os desta ilha sao a memoria dela), e proibir a citacao seria proibir
// o registro. O que a regua mede e o que a pagina SERVE.
const phpCodigo = phpFonte
  .replace(/\/\*[\s\S]*?\*\//g, '')
  .split('\n').map((l) => l.replace(/^\s*\/\/.*$/, '')).join('\n');
const stringsLongas = (phpCodigo.match(/'[^'\n]{25,}'|"[^"\n]{25,}"/g) || []);
for (const t of QUANTIFICADORES) {
  const achadas = stringsLongas.filter((x) => x.toLowerCase().includes(t));
  ok(achadas.length === 0,
    'o snippet da F1 traz o quantificador por extenso ' + JSON.stringify(t) + ' em ' +
    achadas.length + ' string(s) que vao para a pagina ou para o JSON-LD: ' +
    JSON.stringify(achadas.slice(0, 2)));
}

// E A OUTRA METADE: a resposta do FAQ sobre o pico nao pode ser prosa escrita a
// mao. Ela TEM de chamar a funcao que monta a frase do molde — senao a frase
// volta a existir em dois lugares, e so um deles e consertado.
ok(/rodametria_f1_frase_do_pico\s*\(/.test(phpCodigo),
  'o snippet nao chama `rodametria_f1_frase_do_pico()`: a frase do pico voltou a ' +
  'ser escrita a mao, e foi assim que o quantificador chegou ao JSON-LD');
console.log('  o JSON-LD e a prosa do snippet: ' + QUANTIFICADORES.length +
  ' quantificador(es) proibido(s) conferido(s) em ' + stringsLongas.length +
  ' string(s) longa(s) do PHP');

/* ------- (7) O NOME DO CAMPO DO FORMULARIO, e esta regua nasceu de um 404 no ar
 *
 * MEDIDO EM 06/11/2026: o formulario desta ferramenta e `method="get"` para a
 * propria home, e o primeiro campo se chamava `w`. `w` E QUERY VAR RESERVADA DO
 * WORDPRESS (a SEMANA do arquivo de data), e `https://rodametria.com.br/?w=500`
 * devolve **404** — a pagina "Pagina nao encontrada" da propria ilha. Medido
 * campo por campo, com controle: `w=500` em 404, e `kmh`, `acel` e `mun` em 200
 * nas mesmas passadas, com a home sem query em 200.
 *
 * O CUSTO ERA DE VERDADE: o JS e quem chama `preventDefault()`, entao quem
 * estivesse sem JavaScript e apertasse o botao da ferramenta principal desta ilha
 * caia num 404. E ele e da familia mais paciente — a pagina responde 200, o
 * portao de ar fica verde, o portao de pixel fica verde, e o defeito so aparece
 * para quem APERTA O BOTAO sem JavaScript.
 *
 * A REGUA COBRA O PREFIXO E NAO A LISTA, de proposito. A lista de reservadas do
 * WordPress tem mais de vinte nomes curtos e muda com a versao; prefixo proprio
 * torna a classe inteira impossivel em vez de consertar o caso de hoje. A lista
 * entra tambem, como segunda afirmacao, para o caso de alguem prefixar errado.
 * ------------------------------------------------------------------------- */
const RESERVADAS_DO_WORDPRESS = [
  'm', 'p', 'w', 's', 'cat', 'name', 'title', 'order', 'orderby', 'author',
  'paged', 'page', 'page_id', 'feed', 'year', 'monthnum', 'day', 'hour',
  'minute', 'second', 'attachment', 'attachment_id', 'pagename', 'tag',
  'taxonomy', 'term', 'preview', 'robots', 'error', 'embed', 'cpage',
  'comments_popup', 'subpost', 'static', 'post_type', 'sentence', 'search',
];
const PREFIXO = 'rdm_';
const nomesDeCampo = [...new Set(
  [...phpFonte.matchAll(/name="([^"]+)"/g)].map((m) => m[1]))];
ok(nomesDeCampo.length > 0, 'nao achei nenhum `name=` de campo no snippet da F1');
for (const nome of nomesDeCampo) {
  ok(nome.startsWith(PREFIXO),
    'o campo ' + JSON.stringify(nome) + ' do formulario nao carrega o prefixo ' +
    JSON.stringify(PREFIXO) + '. O formulario e method=get para a propria pagina, e nome ' +
    'curto colide com query var do WordPress — `w` custou um 404 na ferramenta principal ' +
    'desta ilha em 06/11/2026');
  ok(!RESERVADAS_DO_WORDPRESS.includes(nome),
    'o campo ' + JSON.stringify(nome) + ' E QUERY VAR RESERVADA DO WORDPRESS: a URL que o ' +
    'botao monta devolve 404');
}
console.log('  nomes de campo: ' + nomesDeCampo.length + ', todos com o prefixo ' +
  JSON.stringify(PREFIXO) + ' e nenhum nas ' + RESERVADAS_DO_WORDPRESS.length +
  ' query vars reservadas do WordPress');

/* ------------------ (8) O <noscript>, porque o formulario SO responde com JS
 *
 * O formulario e method=get e o JS chama `preventDefault()`. Sem JavaScript o
 * botao recarrega a pagina e a caixa volta a servir o CASO DE EXEMPLO, com cara
 * de resposta ao que a pessoa escolheu — a pagina responderia outra pergunta
 * parecendo responder a dela. A 22.8 e a 32.5 cobram que a resposta
 * pre-renderizada ESTEJA no HTML servido, e ela esta; o que elas nao cobrem e
 * esta confusao, porque do lado de fora as duas paginas sao identicas.
 * Esta regua cobra que a pagina DIGA isso. Ela vale para toda ferramenta desta
 * ilha que tenha formulario.
 * ------------------------------------------------------------------------- */
ok(/<noscript>/.test(phpFonte),
  'o snippet nao serve <noscript> nenhum, e o formulario dele SO responde com ' +
  'JavaScript: sem ele o botao recarrega a pagina e a caixa volta a servir o caso de ' +
  'exemplo, parecendo resposta');
ok(/rodametria_f1_noscript_html\s*\(/.test(phpCodigo),
  'a pagina nao chama `rodametria_f1_noscript_html()`: o aviso existe e nao e impresso');
console.log('  o <noscript> que diz que a caixa serve o exemplo: presente e impresso');

console.log('');
console.log('teste-f1-arvore: ' + afirmacoes + ' afirmacoes, ' + falhas.length + ' falha(s)');
for (const f of falhas.slice(0, 20)) console.log('  FALHA ' + f);
console.log(falhas.length ? 'REPROVADO' : 'APROVADO');
process.exit(falhas.length ? 1 : 0);

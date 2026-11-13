/**
 * PORTAO DA PASSAGEM DE NUMERO ENTRE AS FERRAMENTAS — sem rede e sem navegador.
 *
 * O QUE ELE MEDE, e por que ele existe (13/11/2026):
 *
 * A F3 convida para a F2 com um link, e ate 13/11/2026 aquele link saia do
 * servidor como `?rdm_peso=<exemplo da F3>` enquanto a F2 NUNCA LIA `$_GET` —
 * o parametro nao fazia nada, e no dia em que fizesse entregaria a F2 um peso
 * que era o EXEMPLO DA ILHA, nao o do leitor. A decisao desta passada foi de
 * autoria: numero que a ilha escreveu nao viaja, numero que o leitor declarou
 * viaja, e quem o escreve no href e o JS da F3, no instante em que ele e
 * declarado. A F2 passou a ler o endereco, no navegador, validando cada
 * parametro contra o PROPRIO controle.
 *
 * As duas metades vivem em JS de rodape, que e exatamente a camada que nenhum
 * portao desta ilha alcancava: `conferir-no-ar.py` le o HTML servido e
 * `conferir-32-5-no-navegador.mjs` mede pixel — e entre os dois faltava quem
 * APERTASSE a logica. Este arquivo segue a receita do `teste-f1-arvore.mjs`:
 *
 *   1. EXTRAI as funcoes do JS servido, dos proprios arquivos PHP, por recorte
 *      de texto. Nao reescreve e nao adivinha: usa o MESMO codigo do ar.
 *   2. FABRICA os controles (os dois `select`, os dois campos numericos, o
 *      ancora do convite) como objetos simples, com as mesmas regras que o HTML
 *      do formulario declara — `min`/`max` e lista de `option`.
 *   3. AFIRMA os dois sentidos: o que o leitor declarou chega, e o que ele nao
 *      declarou NAO chega — inclusive o caso que deu origem a tudo, o exemplo
 *      da F3 viajando sozinho.
 *   4. PROVA QUE MORDE: refaz cada metade do jeito velho e exige que as
 *      afirmacoes fiquem vermelhas. Portao que nunca viu vermelho nao prova
 *      que ficaria vermelho.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const AQUI = dirname(fileURLToPath(import.meta.url));
const ILHA = dirname(AQUI);
const F2 = join(ILHA, 'snippets', 'rodametria-f2.php');
const F3 = join(ILHA, 'snippets', 'rodametria-f3.php');

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
  const i = fonte.indexOf('{', abre);
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

const fonteF2 = readFileSync(F2, 'utf8');
const fonteF3 = readFileSync(F3, 'utf8');

const txtValorDaUrl = extrairFuncao(fonteF2, 'valorDaUrl');
const txtAplicarNoCampo = extrairFuncao(fonteF2, 'aplicarNoCampo');
const txtAplicarUrl = extrairFuncao(fonteF2, 'aplicarUrl');
const txtSincronizar = extrairFuncao(fonteF3, 'sincronizarConvite');

ok(txtValorDaUrl !== null && txtAplicarNoCampo !== null && txtAplicarUrl !== null,
  'nao achei `valorDaUrl`, `aplicarNoCampo` ou `aplicarUrl` no JS de '
  + 'snippets/rodametria-f2.php. Renomear uma delas sem reapontar este portao '
  + 'deixa a leitura do endereco sem regua nenhuma, e em silencio');
ok(txtSincronizar !== null,
  'nao achei `sincronizarConvite` no JS de snippets/rodametria-f3.php — o href '
  + 'do convite voltaria a envelhecer sem ninguem medir');

/* ------------------------------------------------- (2) os controles fabricados */

/* AS LISTAS SAEM DO BANCO DA FERRAMENTA, nunca digitadas aqui: e de
   `dados/f2-respostas.json` que o PHP monta cada `<option>`, e lista copiada
   para dentro de um portao envelhece calada — passaria a aprovar o que o campo
   de verdade recusa. Os LIMITES, ao contrario, sao literais no PHP (o campo nao
   os le de dado nenhum), entao eles vem escritos abaixo e ha uma afirmacao
   propria cobrando que o PHP continue dizendo os mesmos. */
const BANCO = JSON.parse(readFileSync(join(ILHA, 'dados', 'f2-respostas.json'), 'utf8'));
const TENSOES = BANCO.campos.tensoes_v.map((v) => String(v));
const AMPERAGENS = BANCO.campos.amperagens_ah.map((v) => String(v));
const RELEVOS = BANCO.campos.relevos.map((v) => String(v));
const PESO_MIN = '30';
const PESO_MAX = '200';
const AUT_MIN = '1';
const AUT_MAX = '400';

ok(TENSOES.indexOf('72') !== -1 && AMPERAGENS.indexOf('26') !== -1
  && RELEVOS.indexOf('ladeira') !== -1,
  'o banco da F2 nao traz mais os valores que os casos deste portao usam '
  + '(72 V, 26 Ah, ladeira) — reaponte os casos em vez de os deixar medindo '
  + 'uma lista que o formulario nao serve');

function select(valores, inicial) {
  return {
    tagName: 'SELECT',
    value: inicial,
    options: valores.map((v) => ({ value: v })),
  };
}
function numero(min, max, inicial) {
  return { tagName: 'INPUT', min, max, value: inicial === undefined ? '' : inicial };
}

function campos() {
  return {
    elV: select(TENSOES, '48'),
    elAh: select(AMPERAGENS, '20'),
    elPeso: numero(PESO_MIN, PESO_MAX),
    elRelevo: select(RELEVOS, 'misto'),
    elAut: numero(AUT_MIN, AUT_MAX),
  };
}

function montarAplicarUrl(corpoValor, corpoCampo, corpoAplicar) {
  // eslint-disable-next-line no-new-func
  const fabrica = new Function('elV', 'elAh', 'elPeso', 'elRelevo', 'elAut',
    corpoValor + ';' + corpoCampo + ';' + corpoAplicar + '; return aplicarUrl;');
  return (c) => fabrica(c.elV, c.elAh, c.elPeso, c.elRelevo, c.elAut);
}

const fabricarAplicarUrl = (txtValorDaUrl && txtAplicarNoCampo && txtAplicarUrl)
  ? montarAplicarUrl(txtValorDaUrl, txtAplicarNoCampo, txtAplicarUrl)
  : null;

/* O ancora e o formulario da F3. `campoPeso` e `campoCarga` sao os dois campos
   que a pagina da F3 serve; `conviteCru` e o href que o SERVIDOR entrega. */
const CRU = 'https://rodametria.com.br/autonomia-patinete-eletrico/';

function montarSincronizar(corpo) {
  // eslint-disable-next-line no-new-func
  const fabrica = new Function('convite', 'conviteCru', 'campoPeso', 'campoCarga',
    corpo + '; return sincronizarConvite;');
  return (cenario) => fabrica(cenario.convite, cenario.conviteCru,
    cenario.campoPeso, cenario.campoCarga);
}

function cenarioF3(pesoTxt, cargaTxt, cru) {
  const href = { valor: cru === undefined ? CRU : cru };
  return {
    conviteCru: href.valor,
    convite: {
      getAttribute: () => href.valor,
      setAttribute: (_n, v) => { href.valor = v; },
      get href() { return href.valor; },
    },
    campoPeso: { value: pesoTxt },
    campoCarga: { value: cargaTxt },
  };
}

const fabricarSincronizar = txtSincronizar ? montarSincronizar(txtSincronizar) : null;

/* ---------------------------------------------------------------- (3) afirma */

/* 3.1 — O LADO DA F3: o href servido nao leva numero, e o numero que ele passa
   a levar e o TOTAL declarado pelo leitor. */

if (fabricarSincronizar) {
  const semNada = cenarioF3('', '');
  fabricarSincronizar(semNada)();
  ok(semNada.convite.href === CRU,
    'F3: com os dois campos vazios o convite tem de ficar o href CRU, sem '
    + 'parametro — veio ' + semNada.convite.href);

  const declarado = cenarioF3('100', '8');
  fabricarSincronizar(declarado)();
  ok(declarado.convite.href === CRU + '?rdm_peso=108',
    'F3: 100 kg de piloto e 8 kg de carga tem de virar `rdm_peso=108` (o TOTAL, '
    + 'porque o campo da F2 e o peso com mochila) — veio ' + declarado.convite.href);

  const semCarga = cenarioF3('82', '');
  fabricarSincronizar(semCarga)();
  ok(semCarga.convite.href === CRU + '?rdm_peso=82',
    'F3: carga vazia conta como zero, e o convite leva o peso do piloto — veio '
    + semCarga.convite.href);

  const cargaLixo = cenarioF3('82', 'abc');
  fabricarSincronizar(cargaLixo)();
  ok(cargaLixo.convite.href === CRU + '?rdm_peso=82',
    'F3: carga ilegivel conta como zero e nao derruba o peso declarado — veio '
    + cargaLixo.convite.href);

  /* O CASO QUE DEU ORIGEM A ESTE PORTAO: o exemplo da ilha (100 kg) nao pode
     viajar quando o leitor nao declarou nada. */
  const soExemplo = cenarioF3('', '8');
  fabricarSincronizar(soExemplo)();
  ok(soExemplo.convite.href.indexOf('rdm_peso') === -1,
    'F3: sem peso declarado pelo leitor NENHUM numero viaja — e este e o '
    + 'defeito que a passada de 13/11/2026 fechou: veio ' + soExemplo.convite.href);

  /* E O NUMERO NAO FICA PENDURADO: quem declara e depois apaga tem de ver o
     href voltar ao cru. */
  const apagou = cenarioF3('100', '8');
  const sinc = fabricarSincronizar(apagou);
  sinc();
  apagou.campoPeso.value = '';
  sinc();
  ok(apagou.convite.href === CRU,
    'F3: apagar o peso tem de DEVOLVER o href cru; link com numero que saiu da '
    + 'tela e a mesma mentira com um passo a mais — veio ' + apagou.convite.href);

  /* Arredondamento: o campo aceita decimal digitado em teclado de numero. */
  const meio = cenarioF3('100.4', '8.4');
  fabricarSincronizar(meio)();
  ok(meio.convite.href === CRU + '?rdm_peso=109',
    'F3: 100,4 + 8,4 = 108,8 arredonda para 109 e nunca sai com virgula no '
    + 'endereco — veio ' + meio.convite.href);

  /* Se um dia o href cru ganhar parametro proprio, o nosso entra com `&`. */
  const comParametro = cenarioF3('90', '0', CRU + '?x=1');
  fabricarSincronizar(comParametro)();
  ok(comParametro.convite.href === CRU + '?x=1&rdm_peso=90',
    'F3: href que ja tem parametro recebe o nosso com `&`, nunca com um segundo '
    + '`?` — veio ' + comParametro.convite.href);

  /* Sem o ancora na pagina (F2 desativada, o `function_exists` do PHP), a
     funcao tem de ser inofensiva em vez de estourar. */
  let estourou = false;
  try {
    const semAncora = cenarioF3('100', '8');
    semAncora.convite = null;
    semAncora.conviteCru = null;
    fabricarSincronizar(semAncora)();
  } catch (e) { estourou = true; }
  ok(!estourou,
    'F3: sem o ancora do convite (a F2 desativada, pela guarda do PHP) a funcao '
    + 'tem de nao fazer nada em vez de estourar e levar a recomputacao junto');
}

/* 3.2 — O LADO DA F2: o que chega pelo endereco entra; o resto nao. */

if (fabricarAplicarUrl) {
  const c1 = campos();
  const mexeu1 = fabricarAplicarUrl(c1)('?rdm_peso=108');
  ok(mexeu1 === true && c1.elPeso.value === '108',
    'F2: `?rdm_peso=108` tem de entrar no campo de peso — veio '
    + JSON.stringify(c1.elPeso.value));

  const c2 = campos();
  const mexeu2 = fabricarAplicarUrl(c2)('');
  ok(mexeu2 === false && c2.elPeso.value === '' && c2.elV.value === '48',
    'F2: endereco sem parametro nenhum NAO mexe um campo — e e isso que garante '
    + 'que a pagina servida fica como o servidor a entregou');

  const c3 = campos();
  const mexeu3 = fabricarAplicarUrl(c3)('?utm_source=x&v=12345');
  ok(mexeu3 === false,
    'F2: parametro de terceiro (quebra de cache, etiqueta de campanha) nao pode '
    + 'ser lido como numero de leitor');

  const c4 = campos();
  fabricarAplicarUrl(c4)('?rdm_peso=29');
  ok(c4.elPeso.value === '',
    'F2: peso abaixo do `min` do proprio campo (30) tem de ser RECUSADO — veio '
    + JSON.stringify(c4.elPeso.value));

  const c5 = campos();
  fabricarAplicarUrl(c5)('?rdm_peso=201');
  ok(c5.elPeso.value === '',
    'F2: peso acima do `max` do proprio campo (200) tem de ser RECUSADO — veio '
    + JSON.stringify(c5.elPeso.value));

  const c6 = campos();
  fabricarAplicarUrl(c6)('?rdm_peso=200&rdm_aut=400');
  ok(c6.elPeso.value === '200' && c6.elAut.value === '400',
    'F2: o valor EXATO do limite passa — recusar o limite e o erro classico de '
    + 'fronteira, e e o que a grade do `teste-f1-arvore.mjs` ensinou a cobrar');

  const c7 = campos();
  fabricarAplicarUrl(c7)('?rdm_peso=108kg');
  ok(c7.elPeso.value === '',
    'F2: "108kg" nao e numero — `parseFloat` sozinho aceitaria e a pagina '
    + 'nomearia um peso que ninguem escreveu assim');

  const c8 = campos();
  fabricarAplicarUrl(c8)('?rdm_peso=1e2');
  ok(c8.elPeso.value === '',
    'F2: notacao exponencial nao entra em campo de `step="1"`');

  const c9 = campos();
  fabricarAplicarUrl(c9)('?rdm_peso=-80');
  ok(c9.elPeso.value === '',
    'F2: peso negativo nao entra');

  const c10 = campos();
  fabricarAplicarUrl(c10)('?rdm_peso=');
  ok(c10.elPeso.value === '',
    'F2: parametro presente e VAZIO nao mexe no campo');

  const c11 = campos();
  fabricarAplicarUrl(c11)('?rdm_v=72&rdm_ah=26&rdm_relevo=ladeira');
  ok(c11.elV.value === '72' && c11.elAh.value === '26' && c11.elRelevo.value === 'ladeira',
    'F2: os tres `select` aceitam valor que existe na propria lista de `option`');

  const c12 = campos();
  fabricarAplicarUrl(c12)('?rdm_v=99&rdm_relevo=montanha');
  ok(c12.elV.value === '48' && c12.elRelevo.value === 'misto',
    'F2: valor que NAO existe na lista de `option` e recusado, e o `select` fica '
    + 'com o que o servidor escolheu — veio ' + c12.elV.value + ' / ' + c12.elRelevo.value);

  /* A ARMADILHA DA LISTA REAL: `amperagens_ah` tem valores com DECIMAL (7,8 e
     10,4 Ah). A regra de inteiro vale para os dois campos numericos de
     `step="1"` e nunca para um `select`, que casa pelo valor que ele serve. */
  const decimal = AMPERAGENS.filter((v) => v.indexOf('.') !== -1)[0];
  if (decimal) {
    const cd = campos();
    fabricarAplicarUrl(cd)('?rdm_ah=' + decimal);
    ok(cd.elAh.value === decimal,
      'F2: amperagem com decimal que EXISTE na lista (' + decimal + ' Ah) tem de '
      + 'entrar — a regra de inteiro e dos campos de `step="1"`, nao do `select`');
  }

  const c13 = campos();
  fabricarAplicarUrl(c13)('?rdm_peso=108&rdm_peso=200');
  ok(c13.elPeso.value === '108',
    'F2: com o parametro repetido vale o PRIMEIRO, sempre o mesmo — veio '
    + c13.elPeso.value);

  const c14 = campos();
  fabricarAplicarUrl(c14)('?rdm_relevo=%6Cadeira');
  ok(c14.elRelevo.value === 'ladeira',
    'F2: o valor chega decodificado (%6C e `l`)');

  const c15 = campos();
  fabricarAplicarUrl(c15)('?rdm_relevo=%E0%A4%A');
  ok(c15.elRelevo.value === 'misto',
    'F2: percent-encoding quebrado derruba `decodeURIComponent`, e a excecao tem '
    + 'de ser PRESA — solta ela leva a pagina inteira, que e tela sem JS nenhum');

  const c16 = campos();
  fabricarAplicarUrl(c16)('?xrdm_peso=108');
  ok(c16.elPeso.value === '',
    'F2: `xrdm_peso` nao e `rdm_peso` — casar por pedaco de nome le parametro de '
    + 'outra gente');

  const c17 = campos();
  fabricarAplicarUrl(c17)('?a=1&rdm_peso=108');
  ok(c17.elPeso.value === '108',
    'F2: o parametro e achado quando nao e o primeiro da lista');
}

/* 3.3 — A SEGUNDA FONTE: as listas e os limites deste portao tem de continuar
   batendo com o HTML que o PHP escreve. Sem isto, o portao envelhece sozinho e
   passa a aprovar o que o campo de verdade recusa. */

ok(fonteF2.indexOf('min="30" max="200"') !== -1,
  'F2: o campo de peso do PHP nao diz mais `min="30" max="200"` — este portao '
  + 'valida contra esses limites e os dois lados tem de concordar');
ok(fonteF2.indexOf('min="1" max="400"') !== -1,
  'F2: o campo de autonomia do PHP nao diz mais `min="1" max="400"`');

/* 3.4 — O QUE O SERVIDOR NAO PODE VOLTAR A FAZER. As duas pontas do defeito de
   13/11/2026, cobradas no proprio texto do PHP. */

const trechoConvite = fonteF3.slice(
  Math.max(0, fonteF3.indexOf('rdm-f3-convite') - 200),
  fonteF3.indexOf('rdm-f3-convite') + 600);
ok(fonteF3.indexOf('rdm-f3-convite') !== -1 && trechoConvite.indexOf('add_query_arg') === -1,
  'F3: o convite servido voltou a montar parametro no PHP (`add_query_arg`). O '
  + 'numero que a ILHA escreve nao viaja: quem acrescenta `rdm_peso` e o JS, com '
  + 'o numero do leitor');
ok(fonteF3.indexOf('data-rdm-f3-convite') !== -1,
  'F3: o ancora do convite perdeu o atributo `data-rdm-f3-convite` e o JS nao '
  + 'tem mais como acha-lo — o link voltaria a ser cru para sempre, em silencio');
ok(/name="rdm_peso"[^>]*min="30"/.test(fonteF2.replace(/\s+/g, ' ')) === false
  || fonteF2.indexOf("( null === $peso_do_exemplo ? '' : ' value=\"'") !== -1,
  'F2: o campo de peso voltou a receber `value` do servidor sem a guarda do '
  + 'exemplo — foi esse o defeito do item 2 de 13/11/2026');

/* --------------------------------------------------------- (4) prova que morde */

/* Cada mutacao e uma versao VELHA ou INGENUA de uma das duas metades, e o
   portao tem de ficar vermelho em todas. O que se mede e quantas das
   afirmacoes de cima a mutacao derruba. */

function conta(fn) {
  const antes = falhas.length;
  fn();
  const depois = falhas.length;
  falhas.length = antes;
  return depois - antes;
}

const mutacoes = [];

if (fabricarSincronizar) {
  /* A F3 do jeito VELHO: o exemplo da ilha pendurado no href, sempre. */
  const velho = 'function sincronizarConvite(){ convite.setAttribute("href", '
    + 'conviteCru + "?rdm_peso=100"); }';
  mutacoes.push(['F3 velha: o exemplo da ilha viaja sempre', conta(() => {
    const f = montarSincronizar(velho);
    const a = cenarioF3('', '');
    f(a)();
    ok(a.convite.href === CRU, 'x');
    const b = cenarioF3('', '8');
    f(b)();
    ok(b.convite.href.indexOf('rdm_peso') === -1, 'x');
  })]);

  /* So o piloto, sem a carga: a metade da quantidade. */
  const soPiloto = 'function sincronizarConvite(){ var p = parseFloat(campoPeso.value);'
    + ' if (!(p > 0)) { convite.setAttribute("href", conviteCru); return; }'
    + ' convite.setAttribute("href", conviteCru + "?rdm_peso=" + Math.round(p)); }';
  mutacoes.push(['F3 so com o piloto, sem a carga', conta(() => {
    const f = montarSincronizar(soPiloto);
    const a = cenarioF3('100', '8');
    f(a)();
    ok(a.convite.href === CRU + '?rdm_peso=108', 'x');
  })]);

  /* O numero pendurado: declara, apaga, e o href nao volta. */
  const pendurado = 'function sincronizarConvite(){ var p = parseFloat(campoPeso.value);'
    + ' var c = parseFloat(campoCarga.value); if (!(p > 0)) { return; }'
    + ' if (!(c >= 0)) { c = 0; }'
    + ' convite.setAttribute("href", conviteCru + "?rdm_peso=" + Math.round(p + c)); }';
  mutacoes.push(['F3 que deixa o numero pendurado depois de apagado', conta(() => {
    const f = montarSincronizar(pendurado);
    const a = cenarioF3('100', '8');
    const s = f(a);
    s();
    a.campoPeso.value = '';
    s();
    ok(a.convite.href === CRU, 'x');
  })]);
}

if (fabricarAplicarUrl) {
  /* A F2 INGENUA: `parseFloat` sem limite e sem forma. */
  const ingenua = 'function aplicarNoCampo(el, texto){ if (!el || texto === null) '
    + '{ return false; } var n = parseFloat(texto); if (isNaN(n)) { return false; } '
    + 'el.value = String(n); return true; }';
  mutacoes.push(['F2 ingenua: `parseFloat` sem limite e sem forma', conta(() => {
    const f = montarAplicarUrl(txtValorDaUrl, ingenua, txtAplicarUrl);
    const a = campos();
    f(a)('?rdm_peso=108kg');
    ok(a.elPeso.value === '', 'x');
    const b = campos();
    f(b)('?rdm_peso=201');
    ok(b.elPeso.value === '', 'x');
    const c = campos();
    f(c)('?rdm_v=99&rdm_relevo=montanha');
    ok(c.elV.value === '48' && c.elRelevo.value === 'misto', 'x');
  })]);

  /* Casar o nome do parametro por PEDACO, que le parametro de outra gente. */
  const porPedaco = 'function valorDaUrl(busca, nome){ var s = String(busca);'
    + ' var i = s.indexOf(nome + "="); if (i === -1) { return null; }'
    + ' var resto = s.slice(i + nome.length + 1); var j = resto.indexOf("&");'
    + ' return j === -1 ? resto : resto.slice(0, j); }';
  mutacoes.push(['F2 que casa o nome do parametro por pedaco', conta(() => {
    const f = montarAplicarUrl(porPedaco, txtAplicarNoCampo, txtAplicarUrl);
    const a = campos();
    f(a)('?xrdm_peso=108');
    ok(a.elPeso.value === '', 'x');
  })]);

  /* Sem try/catch no decode: a excecao sobe e leva o JS da pagina. */
  const semGuarda = 'function valorDaUrl(busca, nome){ var partes = String(busca)'
    + '.replace(/^[?]/, "").split("&"); for (var i = 0; i < partes.length; i++) {'
    + ' var corte = partes[i].indexOf("="); var chave = corte === -1 ? partes[i] :'
    + ' partes[i].slice(0, corte); if (chave !== nome) { continue; }'
    + ' return decodeURIComponent(partes[i].slice(corte + 1)); } return null; }';
  mutacoes.push(['F2 sem a guarda do decode', conta(() => {
    const f = montarAplicarUrl(semGuarda, txtAplicarNoCampo, txtAplicarUrl);
    let caiu = false;
    try {
      const a = campos();
      f(a)('?rdm_relevo=%E0%A4%A');
      ok(a.elRelevo.value === 'misto', 'x');
    } catch (e) { caiu = true; }
    ok(!caiu, 'x');
  })]);
}

for (const [nome, pegou] of mutacoes) {
  ok(pegou > 0, 'a mutacao "' + nome + '" passou pelo portao sem derrubar uma '
    + 'afirmacao — portao que nao morde no defeito nao prova nada');
}

/* ------------------------------------------------------------------- veredito */

const linhas = [];
linhas.push('PORTAO DA PASSAGEM DE NUMERO ENTRE AS FERRAMENTAS');
linhas.push('');
for (const [nome, pegou] of mutacoes) {
  linhas.push('  mutacao: ' + nome + ' -> ' + pegou + ' afirmacao(oes) vermelha(s)');
}
linhas.push('');
linhas.push(afirmacoes + ' afirmacao(oes), ' + falhas.length + ' falha(s).');
for (const f of falhas) linhas.push('  FALHA: ' + f);
linhas.push(falhas.length === 0 ? 'APROVADO' : 'REPROVADO');
console.log(linhas.join('\n'));
process.exit(falhas.length === 0 ? 0 : 1);

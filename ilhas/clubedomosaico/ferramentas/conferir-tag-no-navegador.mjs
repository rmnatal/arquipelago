/**
 * Abre a ilha num navegador de verdade e mede o DISPARO do GA4 saindo.
 *
 *   npm i --no-save playwright@1.56.1
 *   node ferramentas/conferir-tag-no-navegador.mjs
 *
 * POR QUE ELE EXISTE, e por que o conferir-no-ar.py nao basta. O
 * conferir-no-ar.py abre as onze URLs com `curl` e afirma sobre o HTML servido:
 * ele prova que a tag ESTA na pagina, com o ID certo, na posicao certa. E so
 * isso. `curl` nao executa uma linha de JavaScript, entao ele nao pode provar a
 * unica coisa que interessa de verdade — que a visita CHEGA na propriedade.
 *
 * Entre "a tag esta no HTML" e "a propriedade recebeu a sessao" cabe o mundo
 * inteiro: o script do Google bloqueado por politica de egresso, um ID que
 * existe mas aponta para propriedade apagada, um erro de JavaScript de outro
 * trecho da pagina derrubando o `gtag` antes do `config`, um Consent Mode
 * herhado de plugin segurando o disparo. Nenhuma dessas aparece no HTML, e
 * todas terminam do mesmo jeito: relatorio em zero, lido como "ninguem veio".
 * A secao 5 do ARQUIPELAGO.md diz isso com todas as letras — enquanto a tag nao
 * mede, o zero mede a AUSENCIA DA TAG, e o relatorio tem de dizer qual dos dois
 * e. Este arquivo e o que permite dizer.
 *
 * O QUE ELE MEDE: a requisicao de coleta que sai do navegador para o Google,
 * com o `tid` desta ilha e o codigo HTTP que o Google devolve. Nao le a
 * propriedade — ler exige a credencial da conta de servico, que nao mora no
 * repositorio e nao estava no ambiente em 12/09/2026. Ver o disparo sair e
 * receber 2xx e a metade que a nuvem alcanca sozinha; a outra metade e o Tempo
 * Real do GA4, e quem a fecha e quem tiver a credencial.
 *
 * ESTE ARQUIVO NUNCA FOI VISTO APROVANDO, e isso esta escrito aqui em cima de
 * proposito, porque ferramenta que ninguem viu rodar e promessa. Ele nasceu em
 * 12/09/2026 e a nuvem das rotinas nao consegue executa-lo, por DOIS motivos
 * independentes, os dois medidos e repetidos na mesma execucao:
 *
 *   1. `www.googletagmanager.com` esta FORA da lista de egresso das rotinas. O
 *      gateway responde 403 ao CONNECT, cinco vezes seguidas, enquanto
 *      clubedomosaico.com.br responde 200 na mesma passada. Nao e intermitencia
 *      de tunel (a secao 20.2), e politica — e a regra do proxio e nao insistir
 *      em 403, e sim nomear o host barrado. Mesmo que o navegador carregasse a
 *      pagina, ele nao baixaria o gtag.js: disparo nenhum sairia daqui.
 *   2. O Chromium nao atravessa este tunel nem para o dominio liberado:
 *      ERR_CONNECTION_RESET em tres tentativas, com o proxy registrando
 *      `ws_closed_mid_exchange` — e `curl` devolvendo 200 no mesmo minuto.
 *
 * O QUE FALTA PARA ELE RODAR NA NUVEM: `www.googletagmanager.com` e
 * `*.google-analytics.com` na rede Personalizada do ambiente das rotinas, do
 * mesmo jeito que os dominios das ilhas ja estao. E uma linha de configuracao
 * do Raphael, nao um conserto de codigo. Ate la, ele roda no Chrome dele.
 *
 * O QUE NAO SE FAZ ENQUANTO ISSO, e vale escrever para ninguem ter a ideia:
 * mandar um evento pelo Measurement Protocol para "confirmar" a medicao. Seria
 * inventar a visita que se queria comprovar, e ainda sujaria a serie com uma
 * sessao que nunca existiu. Zero medido e dado; zero fabricado e mentira.
 *
 * Bancada: nunca vai para o site.
 */

import { chromium } from 'playwright';

const BASE = 'https://clubedomosaico.com.br';
/* Copiado a mao do PROMPT.md da ilha, como nos outros portoes: conferir a casca
   com a constante da casca so provaria que ela concorda consigo mesma. */
const GA4 = 'G-0K5PY39HV7';
const PAGINAS = ['/', '/materiais/qual-cola-usar-no-mosaico/', '/privacidade/'];

let falhas = 0;
let feitos = 0;
function ok(cond, rotulo, medida = '') {
  feitos++;
  if (!cond) falhas++;
  console.log((cond ? '  ok   ' : '  FALHA ') + rotulo.padEnd(58) + ' ' + medida);
}

/* O NAVEGADOR NAO HERDA A REDE DO AMBIENTE, e descobrir isso custou uma leitura
   errada em 12/09/2026: a saida das rotinas e um proxy em HTTPS_PROXY, o `curl`
   e o `python` o respeitam sozinhos e o Chromium NAO — ele tenta a rede direto e
   devolve ERR_CONNECTION_RESET, que tem exatamente a cara de "o dominio esta
   fora da lista de egresso". A secao 20.2 do ARQUIPELAGO.md manda nao presumir
   bloqueio de rede sem repetir o teste, e este comentario e a outra metade da
   mesma licao: antes de acreditar num erro de rede do navegador, confira se o
   navegador esta usando a rede certa. Como o proxy e o do ambiente e o
   certificado dele e proprio, o argumento de ignorar erro de certificado fica
   restrito a ESTA bancada — nada aqui vai para o site. */
const proxy = process.env.HTTPS_PROXY || process.env.https_proxy || '';
const navegador = await chromium.launch({
  proxy: proxy ? { server: proxy } : undefined,
  args: ['--ignore-certificate-errors'],
});

for (const caminho of PAGINAS) {
  const ctx = await navegador.newContext();
  const pagina = await ctx.newPage();

  const coletas = [];
  const erros = [];
  const scripts = [];

  pagina.on('request', (r) => {
    const u = r.url();
    if (/google-analytics\.com|analytics\.google\.com/.test(u) && /\/(g\/)?collect/.test(u)) {
      coletas.push(u);
    }
    if (r.resourceType() === 'script') scripts.push(u);
  });
  pagina.on('response', async (r) => {
    const u = r.url();
    if (/google-analytics\.com|analytics\.google\.com/.test(u) && /\/(g\/)?collect/.test(u)) {
      coletas[coletas.indexOf(u)] = u + ' -> ' + r.status();
    }
  });
  /* Erro de JavaScript de QUALQUER trecho da pagina derruba a medicao junto, e
     por isso ele e medido aqui e nao so no teste de navegador da casca. */
  pagina.on('pageerror', (e) => erros.push(String(e)));

  await pagina.goto(BASE + caminho + '?v=' + Date.now(), { waitUntil: 'load', timeout: 60000 });
  /* O gtag dispara o page_view logo depois do carregamento; a espera e curta de
     proposito, porque "esperar ate achar" transformaria um disparo lento em
     aprovacao silenciosa. */
  await pagina.waitForTimeout(6000);

  console.log('\n' + caminho);

  const daIlha = coletas.filter((u) => u.includes('tid=' + GA4));
  ok(coletas.length > 0, '[' + caminho + '] o navegador DISPAROU coleta para o Google',
     coletas.length + ' requisicao(oes)');
  ok(daIlha.length > 0, '[' + caminho + '] o disparo carrega o tid desta ilha',
     daIlha.length ? daIlha[0].replace(/^.*?\?/, '').slice(0, 70) : 'nenhum');
  ok(daIlha.some((u) => / -> 2\d\d$/.test(u)), '[' + caminho + '] e o Google respondeu 2xx',
     daIlha.map((u) => (u.match(/ -> (\d+)$/) || [])[1]).join(', ') || 'sem resposta');
  /* A CONTAGEM DUPLA, medida onde ela realmente aparece. No HTML, duas tags sao
     dois <script>; no navegador, sao dois page_view — e e o segundo numero que
     o relatorio mostra. E o caso Site Kit desta ilha. */
  const pageViews = daIlha.filter((u) => /[?&]en=page_view/.test(u));
  ok(pageViews.length <= 1, '[' + caminho + '] UM page_view, e nao dois (contagem dupla)',
     pageViews.length + ' page_view');
  const externos = scripts.filter((u) => !u.includes('clubedomosaico.com.br'));
  ok(externos.length === 1 && externos[0].includes('googletagmanager.com'),
     '[' + caminho + '] o gtag e o unico script de terceiro carregado',
     externos.length ? externos.join(' ; ').slice(0, 70) : 'nenhum');
  ok(erros.length === 0, '[' + caminho + '] nenhum erro de JavaScript na pagina',
     erros.join(' | ').slice(0, 70) || 'console limpo');

  await ctx.close();
}

await navegador.close();

console.log('\n' + (falhas === 0 ? 'APROVADO' : 'REPROVADO') +
            ': ' + feitos + ' afirmacoes medidas num navegador de verdade, ' + falhas + ' falha(s).');
process.exit(falhas ? 1 : 0);

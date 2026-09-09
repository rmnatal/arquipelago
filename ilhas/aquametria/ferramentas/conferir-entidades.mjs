// Portão contra a corrupção por entidade HTML — o defeito que derrubou as cinco
// calculadoras em 08/09/2026 e que três execuções seguidas reportaram como
// resolvido enquanto ele seguia no ar.
//
//   node ferramentas/conferir-entidades.mjs [raiz-da-ilha]
//
// Duas famílias de defeito, e é importante não confundi-las, porque a segunda
// nasceu da tentativa de consertar a primeira:
//
//   (1) ESCAPE NA RENDERIZAÇÃO. JS ou CSS dentro do retorno do shortcode
//       atravessa os filtros de texto do conteúdo do WordPress, que trocam cada
//       "&" pela entidade numérica dele. Um "&&" escapado assim mata o script
//       INTEIRO com SyntaxError. Pego aqui rodando o render de teste (que imita
//       esse escape) e passando cada bloco <script> por node --check.
//
//   (2) CORRUPÇÃO DO FONTE. Alguém conserta o snippet partindo do HTML SERVIDO
//       pelo site — que já traz as entidades escapadas — em vez de partir do
//       código-fonte. As entidades entram no arquivo do repositório e ficam.
//       Pego aqui pela regra dura: entidade NUMÉRICA não tem uso legítimo
//       nenhum em snippets/ (texto acentuado vai em UTF-8 direto), então
//       qualquer ocorrência é corrupção.
//
// ARMADILHA, e ela é séria: as entidades NOMEADAS de esc() —
// .replace(/&/g, '&amp;') e as três irmãs — são CÓDIGO CORRETO. Uma troca cega
// de "&amp;" por "&" dentro do JavaScript quebraria o escape de HTML das cinco
// calculadoras. Por isso este portão proíbe só a família numérica e trata as
// nomeadas por lista de exceção explícita.

import { readFileSync, writeFileSync, mkdtempSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const RAIZ = process.argv[2] || '.';
const CALCULADORAS = [
  { codigo: 'C1',  shortcode: 'aquametria_calculadora_litragem'   },
  { codigo: 'C3',  shortcode: 'aquametria_calculadora_vazao'      },
  { codigo: 'C5',  shortcode: 'aquametria_calculadora_aquecedor'  },
  { codigo: 'C12', shortcode: 'aquametria_calculadora_midia'      },
  { codigo: 'C15', shortcode: 'aquametria_calculadora_iluminacao' },
];

// Entidades nomeadas que PODEM aparecer dentro de <script>: só a cadeia do esc().
const NOMEADAS_PERMITIDAS = /\.replace\(\/&\/g, '&amp;'\)\.replace\(\/<\/g, '&lt;'\)\.replace\(\/>\/g, '&gt;'\)\.replace\(\/"\/g, '&quot;'\)/g;

const NUMERICA = /&#\d+;/g;
const NOMEADA  = /&[a-zA-Z][a-zA-Z0-9]{1,9};/g;

const tmp = mkdtempSync(join(tmpdir(), 'aqm-ent-'));
let falhas = 0;
const falhar = (m) => { falhas++; console.log('  FALHA  ' + m); };

/* ---------- portão 1: o fonte ---------- */
console.log('fonte (snippets/):');
for (const arq of readdirSync(join(RAIZ, 'snippets')).filter(f => f.endsWith('.php')).sort()) {
  const src = readFileSync(join(RAIZ, 'snippets', arq), 'utf8');
  const numericas = src.match(NUMERICA) || [];
  if (numericas.length) {
    falhar(`${arq}: ${numericas.length} entidade(s) numérica(s) ${[...new Set(numericas)].join(' ')} — `
         + 'é corrupção; troque pelo caractere. NUNCA por busca-e-troca cega: confira antes se '
         + 'a linha não é a cadeia de esc().');
  } else {
    console.log(`  ok     ${arq}`);
  }
}

/* ---------- portão 2: o que chega ao navegador ---------- */
console.log('\nrenderizado (script e style, depois do escape do WordPress):');
for (const c of CALCULADORAS) {
  let html;
  try {
    html = execFileSync('php', [join(RAIZ, 'ferramentas/render-para-teste.php'), RAIZ, c.shortcode],
                        { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  } catch (e) {
    falhar(`${c.codigo}: o render de teste não rodou — ${String(e.message).split('\n')[0]}`);
    continue;
  }

  const numericasDoc = (html.match(NUMERICA) || []).length;
  const numericas038  = (html.match(/&#0*38;/g) || []).length;
  // Guardamos a ABERTURA da tag junto do corpo porque desde o bloco 4c (09/09/2026)
  // nem todo <script> da página é JavaScript: o JSON-LD sai num
  // <script type="application/ld+json">, e passar JSON por `node --check` reprova
  // SEMPRE — um objeto literal solto é sintaxe inválida em script. O teste ficou
  // vermelho em C3 e C5 desde que o JSON-LD nasceu, medindo a coisa errada. Regra
  // que fica: cada bloco é conferido pelo verificador da LINGUAGEM dele.
  const blocosScript = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)]
    .map(m => ({ atributos: m[1] || '', corpo: m[2] }))
    .filter(b => b.corpo.trim());
  const ehJsonLd = b => /type\s*=\s*["']application\/ld\+json["']/i.test(b.atributos);
  const scripts = blocosScript.map(b => b.corpo);
  const styles  = [...html.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/g)].map(m => m[1]).filter(s => s.trim());

  if (!scripts.length) { falhar(`${c.codigo}: nenhum bloco <script> no render`); continue; }

  // Entidade dentro de script OU style é sempre defeito; a exceção do esc() só
  // vale para as nomeadas.
  for (const [rotulo, blocos] of [['script', scripts], ['style', styles]]) {
    blocos.forEach((corpo, i) => {
      const numericas = corpo.match(NUMERICA) || [];
      if (numericas.length) {
        falhar(`${c.codigo} ${rotulo}[${i}]: ${numericas.length} entidade(s) numérica(s) DENTRO do bloco `
             + `(${[...new Set(numericas)].join(' ')})`);
      }
      const sobra = corpo.replace(NOMEADAS_PERMITIDAS, '').match(NOMEADA) || [];
      if (sobra.length) {
        falhar(`${c.codigo} ${rotulo}[${i}]: entidade(s) nomeada(s) fora da cadeia de esc(): `
             + [...new Set(sobra)].join(' '));
      }
    });
  }

  // Sem perdão nos dois casos: JavaScript quebrado é a calculadora morta no
  // navegador, e JSON-LD quebrado é a página invisível para o robô e para o
  // modelo de IA — que é a regra de primeira classe do Raphael. O que muda é só
  // QUAL verificador roda em cada bloco.
  let sintaxeOk = 0, jsonLdOk = 0;
  blocosScript.forEach((b, i) => {
    if (ehJsonLd(b)) {
      // JSON.parse é mais severo aqui do que node --check seria: ele reprova
      // exatamente o defeito de 08/09/2026 se ele reaparecer no JSON-LD, porque
      // um `&#038;` no meio de uma string escapada quebra a análise.
      try { JSON.parse(b.corpo); jsonLdOk++; }
      catch (e) {
        falhar(`${c.codigo} script[${i}] (JSON-LD): JSON.parse reprovou — ${e.message}`);
      }
      return;
    }
    const f = join(tmp, `${c.codigo}-${i}.js`);
    writeFileSync(f, b.corpo);
    try { execFileSync(process.execPath, ['--check', f], { stdio: 'pipe' }); sintaxeOk++; }
    catch (e) {
      falhar(`${c.codigo} script[${i}]: node --check reprovou — `
           + String(e.stderr || e.message).split('\n').filter(Boolean).slice(0, 3).join(' | '));
    }
  });

  // O script tem de vir DEPOIS do HTML que ele controla (wp_footer, não inline).
  const posScript = html.lastIndexOf('<script');
  const posForm   = html.lastIndexOf('</form>') >= 0 ? html.lastIndexOf('</form>') : html.lastIndexOf('aqm-resposta');
  const ordemOk   = posScript > posForm;
  if (!ordemOk) falhar(`${c.codigo}: o <script> vem ANTES do conteúdo — ele tem de sair no wp_footer`);

  console.log(`  ${c.codigo}: script=${scripts.length} style=${styles.length} `
            + `js_ok=${sintaxeOk} jsonld_ok=${jsonLdOk} entidade_038_no_documento=${numericas038} numéricas_no_documento=${numericasDoc} `
            + `script_depois_do_conteúdo=${ordemOk ? 'sim' : 'NÃO'}`);
}

console.log(`\nfalhas: ${falhas}`);
process.exit(falhas ? 1 : 0);

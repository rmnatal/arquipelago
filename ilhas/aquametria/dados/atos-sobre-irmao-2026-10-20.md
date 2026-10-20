# ATOS SOBRE IRMÃO EM `ferramentas/`, FORA DO PYTHON — a conta do item 7

**Medido em 20/10/2026, pela execução das 16h18Z.** Este arquivo responde a
pergunta que o fecho de 20/10 às 13h18Z deixou escrita, com a ordem embutida:

> *"o `.mjs` e o `.php` desta pasta carregam e invocam irmãos, e **ninguém os
> mediu**. Quem a tomar responde primeiro quantos atos existem lá, antes de
> propor régua nenhuma."*

A `regua-alvos-de-portao.py` lê a árvore sintática do **Python** e escreve, no
próprio cabeçalho, que os **40** arquivos `.mjs` e `.php` desta pasta estão fora
do alcance dela. A resposta, nas duas metades:

| metade | arquivos | atos sobre irmão | literal | indireto | construído | **invisíveis** | por resolver |
|---|---|---|---|---|---|---|---|
| `.php` | 21 | **12** | 12 | 0 | 0 | **0** | 1 (varre `snippets/`) |
| `.mjs` | 20 | **9** | 7 | 2 | 0 | **0** | 0 |
| **fora do Python** | **41** | **21** | 19 | 2 | 0 | **0** | 1 |
| (`.py`, pela régua irmã) | 103 | 196 | 48 | 142 | 6 | **0** | 10 |

**A leitura, e é ela que decide o que fazer:** **zero** ato invisível nas duas
metades novas, como já era no Python. A varredura por nome da
`regua-classes-da-bancada.py` **não está cega em nenhuma das três linguagens
desta pasta hoje** — e, nas duas metades novas, ela não está cega por acidente:
19 dos 21 atos nomeiam o alvo no próprio sítio. É o contrário do que se mediu no
Python, onde 148 dos 196 só são visíveis por acidente.

**Por quê a diferença, e não é cultura: é a falta de um idioma.** O Python desta
pasta carrega irmão por `spec_from_file_location(apelido, caminho)` com o
caminho montado por variável e função, e os `mutacoes-*` recebem o alvo por
parâmetro. O PHP carrega por `require __DIR__ . '/<nome>.php'`, que não tem para
onde esconder o nome, e o `.mjs` invoca `execFileSync('php', [RAIZ +
'/ferramentas/<nome>.php', ...])`, igual. **Linguagem sem indirecção de carga
produz alvo visível por construção.**

---

## A METADE DO PHP — 12 atos, e um único alvo

| quem age | linha | ato | alvo | posição |
|---|---|---|---|---|
| `listar-categorias-do-eixo.php` | 35 | carrega | `render-para-teste.php` | literal |
| `listar-constantes-do-snippet.php` | 59 | carrega | `render-para-teste.php` | literal |
| `listar-paginas-da-casca.php` | 30 | carrega | `render-para-teste.php` | literal |
| `listar-paginas-do-eixo.php` | 32 | carrega | `render-para-teste.php` | literal |
| `listar-promessas.php` | 40 | carrega | `render-para-teste.php` | literal |
| `listar-teto-do-titulo.php` | 51 | carrega | `render-para-teste.php` | literal |
| `render-artigo-para-teste.php` | 31 | carrega | `render-para-teste.php` | literal |
| `render-casca-pagina.php` | 30 | carrega | `render-para-teste.php` | literal |
| `render-casca-para-teste.php` | 18 | carrega | `render-para-teste.php` | literal |
| `render-pagina-completa.php` | 52 | carrega | `render-para-teste.php` | literal |
| `teste-escape-shortcode.php` | 19 | carrega | `render-para-teste.php` | literal |
| `teste-site-jsonld.php` | 33 | carrega | `render-para-teste.php` | literal |

**12 de 12 são `carrega`, e 12 de 12 têm o MESMO alvo.** Nenhum `invoca` e
nenhum `abre` sobre irmão. O `render-para-teste.php` é o eixo de toda a metade
do PHP desta pasta — e isso é informação de risco, não curiosidade: um renomeio
dele toca doze arquivos de uma vez, e os doze o nomeiam literalmente, então o
renomeio é visível para qualquer varredura por nome. **Esta metade está medida e
tem portão:** `teste-alvos-em-php.py` (53 afirmações) e
`mutacoes-alvos-em-php.py` (18, com o leitor em PHP mutilado também).

**Dois sítios ficaram de fora por MEDIÇÃO e não por limite**, e os dois estão
nomeados no portão:
- `teste-atualizador-sync.php:60` — `exec( ... escapeshellarg( __FILE__ ) ... )`
  é ato sobre **si mesmo**, e ato sobre si não é ato sobre irmão.
- `proteger-funcoes.php:3` — `file_get_contents( $argv[1] )` recebe o alvo da
  **linha de comando**, não da pasta.

**Um sítio ficou POR RESOLVER, e ele é o idioma de quem varre outra pasta:**
`render-para-teste.php:188` — `eval( file_get_contents( $arquivo ) )` dentro de
`foreach ( glob( $raiz . '/snippets/*.php' ) as $arquivo )`. O alvo vem do disco
em tempo de execução e não do texto, então não há nome a resolver. **Não é
cobrado pelo portão, e o motivo é por construção:** ele varre `snippets/`, não
`ferramentas/`, e carga que varre outra pasta não pode esconder irmão nenhum. O
que o portão cobra é a carga que **não resolve E fala desta pasta** — essa sim
poderia.

---

## A METADE DO `.mjs` — 9 atos, e ela NÃO tem portão

| quem age | linha | ato | alvo | posição |
|---|---|---|---|---|
| `conferir-entidades.mjs` | 97 | invoca | `render-para-teste.php` | literal |
| `teste-arvore.mjs` | 95 | invoca | `render-pagina-completa.php` | literal |
| `teste-arvore.mjs` | 337 | invoca | `render-pagina-completa.php` | literal |
| `teste-navegador-c15-vitrine.mjs` | 73 | invoca | `regua-constantes-de-snippet.py` | literal |
| `teste-voz.mjs` | 55 | invoca | `regua-teto-do-titulo.py` | literal |
| `teste-voz.mjs` | 106 | invoca | `listar-paginas-do-eixo.php` | **indireto** |
| `teste-voz.mjs` | 106 | invoca | `listar-paginas-da-casca.php` | **indireto** |
| `teste-voz.mjs` | 244 | invoca | `render-casca-pagina.php` | literal |
| `teste-voz.mjs` | 594 | invoca | `render-pagina-completa.php` | literal |

**9 de 9 são `invoca`** — nenhum `.mjs` desta pasta carrega nem abre irmão.
Quatro arquivos agem, e **cinco dos nove atos são do `teste-voz.mjs`**.

**OS DOIS ÚNICOS ATOS INDIRECTOS DESTA METADE são o mesmo sítio**, e vale
nomear o mecanismo porque é o único desta metade que a varredura por nome só
enxerga por acidente: o `listarPelo(arquivo)` do `teste-voz.mjs` invoca
`RAIZ + '/ferramentas/' + arquivo`, com o nome chegando por **parâmetro**. Os
dois literais estão nos sítios de chamada, nas linhas 127 e 128 — e estão ali
porque alguém os escreveu, não porque algo os sustente. Um renomeio que os
apague derruba a visibilidade em silêncio, que é exatamente a família de risco
que o item 7 nomeou no Python.

**Zero sítio por resolver**: a `conferir-entidades.mjs:156` invoca
`process.execPath` com `['--check', f]` sobre os arquivos que ela varre, e não
fala de `ferramentas/` por nenhum literal — é verificação de sintaxe do próprio
Node, não ato sobre irmão nomeado.

### POR QUE ESTA METADE NÃO GANHOU PORTÃO HOJE, dito com o bloqueio nomeado

A medição acima foi feita com a **API de compilação do TypeScript**
(`ts.createSourceFile`), que é um analisador sintático de verdade e lê `.mjs`
sem executar nada. Ela existe neste ambiente, e **só neste ambiente**:

- resolve em `/opt/node-tools/node_modules/typescript`, que é da **imagem do
  ambiente**, não do repositório;
- **não está declarada no `package.json`** desta ilha, cujo único dependente
  declarado é o `playwright`;
- e **não resolve por `import`**: `import ts from 'typescript'` devolve
  `ERR_MODULE_NOT_FOUND` de dentro desta pasta. Só carrega por
  `createRequire` com caminho absoluto para `/opt/node-tools`.

**Portão que fica vermelho onde a dependência não existe é pior que portão
nenhum** — ele ensina a ignorar o vermelho, que é o dano que a 20.5 escreveu
com todas as letras sobre o portão da 20.4 ("o perigo maior é o contrário, que é
concluir que o portão mente e passar a ignorá-lo"). Escrever um tokenizador de
JavaScript à mão também não serve: literal de expressão regular contra divisão é
a ambiguidade clássica da linguagem, e esta pasta tem `/^(\d{4})-(\d{2})-(\d{2})$/.exec(...)`
em quatro arquivos. **Leitor errado é pior que limite declarado.**

**O que existe no lugar, e tem dentes:** a metade 3 do `teste-alvos-em-php.py`
cobra **cobertura declarada** — todo arquivo de `ferramentas/` ou é lido por uma
das duas réguas, ou aparece **nomeado** num limite de uma delas. Isso não mede
JavaScript nenhum, e o portão diz isso. O que impede é que uma linguagem **nova**
entre nesta pasta e fique sem medição por um mês, que é exatamente o que
aconteceu com estes 41 arquivos entre 22/09 (quando a `bancada.py` passou a
varrer a pasta) e hoje. A régua irmã só nomeia `.py`, `.mjs` e `.php`; um `.sh`
ou um `.ts` não estaria em lista nenhuma, e há mutação provando os dois lados.

### PRONTO QUANDO — o critério do portão do `.mjs`, pré-registrado

Esta metade fecha quando **uma** destas três acontecer, e nenhuma delas é bloco
desta ilha hoje:

1. o `package.json` desta ilha declarar um analisador de JavaScript e ele
   instalar neste ambiente — e aí a régua nasce com o mesmo desenho da do PHP
   (leitor na linguagem, posição no Python, vocabulário **importado** da régua
   irmã, nunca copiado);
2. ou os 9 atos virarem **literais no sítio**, com os dois do
   `listarPelo()` trocados por chamada direta — e aí a varredura por nome deixa
   de depender de acidente nesta metade, e o portão do `.mjs` perde o objeto;
3. ou a conta subir. Enquanto forem **9 atos em 4 arquivos, todos `invoca`,
   todos visíveis**, o risco não paga uma dependência nova.

**O número é de uma DATA e envelhece com a pasta.** A conta do `.php` se refaz
com `python3 ferramentas/regua-alvos-em-php.py`; a do `.mjs` **não tem comando**
nesta ilha, e é por isso que ela está escrita aqui com a data no nome do
arquivo, em vez de prometida como se houvesse instrumento.

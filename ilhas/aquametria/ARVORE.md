# ÁRVORE DA AQUAMETRIA

Item (i) do 16.8 do `ARQUIPELAGO.md`, escrito em 11/09/2026 no bloco de reescrita da home e do header.

Este arquivo diz **onde cada página mora** e **quem é a mãe de quem**. Ele é o mapa que os blocos seguintes seguem: breadcrumb, cluster de interlinkagem e leva de malha saem daqui, não da cabeça de quem executa.

Os nomes dos níveis são os do `VOZ.md` — é a pessoa que decide como a seção se chama, não a fábrica. Por isso não existe `/ferramentas/` nem `/entidades/` nesta ilha: ninguém digita isso.

---

## 1. Os três níveis

**Nível 1 — seção.** Quatro, e só estas:

| slug | o que mora ali | existe hoje |
|---|---|---|
| `/calculadoras/` | as contas | **sim** (página da casca) |
| `/peixes/` | ficha de espécie: quanto espaço, que temperatura, com quem convive | **sim** (levas 1 e 2 do T4, 12/09/2026) |
| `/equipamentos/` | listagens do banco: filtro, aquecedor, luminária, mídia | não |
| `/guias/` | os textos que explicam o porquê do número | não |

**Nível 2 — categoria**, com o nome que a pessoa usa. **Categoria só nasce com 3 filhas de dado real** (16.5); até lá o cartão na mãe não é link e diz "em breve", sem contagem.

**Nível 3 — a pergunta ou a ficha**, com as palavras que a pessoa digita.

Sem quarto nível. Fora da árvore ficam só a home, `/sobre/`, `/metodologia/`, `/divulgacao-de-afiliados/` e a futura página de privacidade.

---

## 2. `/calculadoras/`

| nível 2 | filhas de hoje | filhas |
|---|---|---|
| `/calculadoras/aquario/` | C1 litragem · C2 peso e carga | 1 no ar, 1 na fila |
| `/calculadoras/filtragem/` | C3 vazão · C12 mídia | 2 no ar |
| `/calculadoras/aquecimento-e-luz/` | C5 aquecedor · C15 iluminação · C7 consumo | 2 no ar, 1 na fila |
| `/calculadoras/lotacao/` | C8 lotação | 0 no ar |

**A categoria do C8 se chamava `peixes` e virou `lotacao` em 12/09/2026**, junto com a leva 1 do eixo. O motivo é de endereço, não de gosto: `aquametria_casca_url_se_existir()` acha a página pelo `post_name`, que é o último pedaço da URL, e com `/peixes/` e `/calculadoras/peixes/` no ar ao mesmo tempo o hub linkaria uma das duas ao acaso. A página do C8 não existe, então a troca não moveu URL nenhuma. `ferramentas/teste-peixes.py` tem a afirmação que impede a colisão de voltar, e `mutacoes-peixes.py` a exercita.

**Nenhuma das quatro atinge as 3 filhas com dado real hoje**, então nenhuma nasce agora — é a regra 16.5, e ela é o que impede a ilha de publicar quatro páginas de categoria magras num domínio que ainda não indexou a primeira leva. A `/calculadoras/aquecimento-e-luz/` é a primeira a fechar, e fecha no dia em que a C7 entrar.

Enquanto isso, `/calculadoras/` continua sendo a mãe direta das cinco calculadoras no ar — dois níveis em vez de três, declarado aqui como estado de transição, não como desenho.

## 3. `/peixes/` — NO AR desde 12/09/2026 (levas 1 e 2 do T4)

A camada que a Bússola verificou ABERTA e a de maior volume de busca da ilha ("quantos litros para N neons"). O banco de espécies (`dados/especies-agua-doce.json`, 36 registros) é o que limita quantas filhas cabem, e desde 12/09/2026 são **duas** réguas com dois nomes, não uma:

- **`catalogo-de-especies`** — sete campos e duas fontes de corpos distintos. **27 dos 36 passam.** É quem entra na contagem da seção, na tabela da categoria e na lista de quem divide a mesma água.
- **`pagina-especie`** — o catálogo MAIS `cardume_minimo OU convivencia igual a solitario/casal/harem`. **26 dos 27 passam.** É quem pode ter página própria, porque a ficha deste eixo se chama "quantos litros para um cardume de X" e abre pela frase que nomeia o cardume mínimo.

As duas listas saem nomeadas, registro por registro, em `ferramentas/gerar-catalogo-especies.py`. **Quem está no catálogo e não pode ter página hoje: `corydoras-sterbai`** — declara convivência "grupo" e nenhuma fonte diz de quantos. Isso muda a próxima leva: `/peixes/corydoras/` tem **3** filhas elegíveis (panda, paleatus, aeneus), não 4, e 3 é exatamente o mínimo do 16.5.

A separação nasceu de um erro que vale registrar: a primeira versão pôs a regra do cardume no portão do CATÁLOGO, e a contagem da seção caiu de 27 para 26 — o sterbai sumiu de três lugares onde o dado dele é bom, para resolver um problema de outra página. Apertar o portão errado tira da tela informação verdadeira.

Categorias pelo nome que a pessoa usa, nunca pelo nome científico. Seis, e só estas:

| nível 2 | filhas no ar | estado |
|---|---|---|
| `/peixes/tetras/` | tetra neon · neon cardinal · mato-grosso · tetra ember · tetra-brilhante · rodóstomo · tetra-negro | **no ar e FECHADA** (7 de 7 espécies do banco) |
| `/peixes/corydoras/` | — | em breve, sem link e sem contagem (16.5) — 3 filhas elegíveis, o mínimo exato |
| `/peixes/bettas/` | — | em breve |
| `/peixes/ciclideos-anoes/` | — | em breve |
| `/peixes/plecos-e-limpa-vidros/` | — | em breve |
| `/peixes/vivaparos/` | — | em breve |

Filha de nível 3 = a ficha da espécie, com o número que ninguém mais dá. **E o número não é o litro: é a BASE.** As fontes de aquarismo declaram o tamanho do chão do aquário, e as sete primeiras respostas da SERP brasileira dão litro sem fonte e discordam entre si. Cada ficha serve a base declarada (com o nome do corpo de fonte e a data) ao lado das duas réguas brasileiras de lotação, que discordam em quatro vezes, com a atribuição de cada extremo.

**O que NÃO se faz nesta camada, e está escrito no snippet:** multiplicar o derivado per capita (frente mínima ÷ cardume mínimo) para estender o cardume. Para o neon daria 120 cm para dez peixes, que nenhuma fonte sustenta. Quem responde "e para dez?" são os três critérios de lotação. `ferramentas/teste-peixes.py` tem afirmação para isso e `ferramentas/mutacoes-peixes.py` tem a mutação que a exercita.

**E espécie que o banco declara agressiva não ganha lista de companheiro** — a ficha conta quantas espécies dividem a faixa de temperatura e diz por que não recomenda nenhuma. O esquema do banco recusa compatibilidade como campo justamente porque ela depende de volume, layout e ordem de introdução.

Portão da seção 9 conferido nas sete: cada ficha nomeia 10 ou mais registros reais do banco e traz tabelas calculadas na hora de imprimir.

**E "BASE" não é "FRENTE" — a leva 2 achou isso na tela.** A frase mestra da ficha terminava sempre em "e a fonte declara a BASE, não o litro". Era verdade nas três fichas da leva 1, e é falsa em **14 dos 36 registros** do banco, onde a fonte declara só o comprimento mínimo e nunca disse uma palavra sobre o fundo. O rodóstomo é o primeiro caso publicado: o Seriously Fish declara "no mínimo 90 cm de comprimento" e para aí; uma coleta limpa em 12/09, restrita ao domínio, devolveu a mesma frase e mais nada. Nesses registros a ficha diz COMPRIMENTO, as duas tabelas que dependem do fundo não saem — **e a página declara a ausência e a causa** em vez de encolher calada, que é a forma disfarçada do "silêncio parece defeito" da seção 7.

## 4. `/equipamentos/`

`/equipamentos/filtros/`, `/equipamentos/aquecedores/`, `/equipamentos/luminarias/`, `/equipamentos/midias/`. Os quatro bancos existem (`dados/produtos-*.json`).

**Listagem, não ficha de produto.** A seção 14.2 do contrato põe ficha de produto em último lugar e só quando existe dúvida paramétrica que o fabricante e a loja não respondem — então o nível 3 aqui nasce como cruzamento ("aquecedor para aquário de 100 litros"), não como uma página por modelo.

## 5. `/guias/`

`/guias/aquecimento/`, `/guias/filtragem/`, `/guias/iluminacao/`. Os três artigos-âncora de hoje são as três primeiras filhas, uma em cada categoria — ou seja, **nenhuma das três categorias tem as 3 filhas que a 16.5 exige**. É a `pauta.md` da seção 17 que enche isso, e é por isso que a Pauta entra na fila desta ilha antes de qualquer leva de malha nova.

| artigo de hoje | mãe | ferramenta que ele empurra |
|---|---|---|
| `quantos-watts-de-aquecedor-para-aquario` | `/guias/aquecimento/` | C5 |
| `quanta-midia-biologica-o-aquario-precisa` | `/guias/filtragem/` | C12 |
| `quantos-lumens-por-litro-aquario-plantado` | `/guias/iluminacao/` | C15 |

---

## 6. O QUE ESTÁ TRAVADO, E POR QUÊ — leia antes de mover qualquer URL

**ATUALIZADO EM 12/09/2026: das duas travas, uma caiu e a outra fica.** A distinção é a que decide o trabalho: **criar URL nova está liberado; MOVER URL publicada continua travado.**

1. ~~**Item 5 do despacho da Sentinela de 10/09:** nenhuma página nova até 16/09.~~ **SUSPENSO em 12/09/2026 pela seção 21 do `ARQUIPELAGO.md`**, que é posterior ao despacho e o alcança: com 13 URLs a ilha está ABAIXO do piso de 40, e abaixo do piso "zero impressão" não é informação e nunca trava, adia ou reduz leva nenhuma. O campo `congelamento` no cabeçalho do `ESTADO.md` é o que vale. **A leva 1 do eixo `/peixes/` nasceu por causa disso** — cinco URLs novas, dentro do teto de 10 por leva e 3 levas por semana (21.4).
2. **T2 do `PROMPT.md`: continua de pé.** A janela para trocar o endereço dos três artigos (hoje em `/2026/09/08/<slug>/`, endereço com data que envelhece sozinho) só abre depois que a leitura de 16/09 disser **por que** a leva de 08/09 não indexou. Trocar endereço antes disso soma uma variável a um diagnóstico que ainda não fechou. **Isto vale para as cinco calculadoras também:** elas não têm impressão registrada e a 12.1 permitiria mover o slug delas, mas a decisão fica para depois de 16/09.

**Consequência prática para a próxima leva:** `/calculadoras/aquecimento-e-luz/` (item 1 da ordem da seção 7) continua esperando, não pela trava de página nova, e sim por duas outras coisas — a C7 não existe (16.5 exige 3 filhas) e pôr C5 e C15 sob a categoria nova seria MOVER duas URLs publicadas. Foi por isso que a leva 1 saiu pelo item 3 da ordem, `/peixes/tetras/`: é o único cluster do mapa que nasce inteiro sem mover endereço nenhum.

As cinco calculadoras no ar **não têm impressão registrada**, então a seção 12.1 ainda permite mover o slug delas — mas as duas travas acima valem do mesmo jeito, e a decisão fica para depois de 16/09.

**O que dava para fazer antes de 16/09 está FEITO** (casca 1.5.0, 11/09/2026): breadcrumb com `BreadcrumbList` e os blocos "Veja também" do cluster (16.4) nas treze páginas no ar. Nenhum dos dois criou URL. O breadcrumb nasceu com o nível 2 **em texto, sem link**, porque a categoria ainda não existe — e vira link sozinho no dia em que a página existir, porque quem resolve o endereço é `aquametria_casca_url_se_existir()`. Estado de transição declarado, não desenho.

**Três coisas desse bloco que quem vier depois precisa saber:**

1. **O JSON-LD não carrega o degrau sem endereço.** A trilha na tela mostra quatro degraus numa calculadora (Início › Calculadoras › Aquecimento e luz › a página); o `BreadcrumbList` publica três, sem a categoria. Não é esquecimento: `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista inválida é lista ignorada — o schema publicaria menos com cara de publicar mais. Quando a categoria nascer, ela entra nos dois lados de uma vez, sem ninguém lembrar disto. `ferramentas/teste-arvore.mjs` cobra exatamente essa relação.
2. **As irmãs são derivadas, e a mãe de transição é `/calculadoras/`.** Enquanto o nível 2 não existe, irmã de uma calculadora é qualquer outra calculadora no ar, com as da mesma categoria vindo primeiro. Quando as categorias nascerem, a regra de irmã passa a ser "mesma mãe de nível 2" e as listas encolhem — é o desenho do 16.4(c), e a mudança é de uma linha.
3. **O guia ainda não tem frase de mãe no corpo.** O 16.4(b) pede breadcrumb E frase; `/guias/` não existe, e frase apontando para página inexistente seria link morto. Os três guias saem com a trilha e com as irmãs, sem a frase — e o portão cobra a AUSÊNCIA dela, para ninguém "consertar" isso com um endereço inventado. A frase nasce junto com `/guias/`.

**E um achado que ficou de fora de propósito:** `/sobre/` é a única das treze páginas que nenhum CORPO de outra página cita — ela vive do menu e do rodapé, que estão em todas, então não é órfã pelo 16.4(f). Mas é a única sem citação editorial, e isso é assunto de pauta (seção 17), não de casca.

---

## 7. Ordem das levas, quando destravar (16.6)

Primeiro a mãe e as **3 primeiras filhas de maior intenção de compra**, depois as irmãs, depois a próxima categoria. Nunca uma filha de cada categoria espalhada.

1. `/calculadoras/aquecimento-e-luz/` + C5, C15, C7 — é o cluster cuja resposta termina num produto do banco, e o C5 é a consulta de maior intenção de compra da ilha.
2. `/guias/aquecimento/` + os guias da pauta que apontam para a C5.
3. ~~`/peixes/tetras/` + as 3 espécies de maior busca com banco fechado.~~ **FEITO** — leva 1 (12/09, 5 URLs) e leva 2 (12/09, 4 URLs: ember, brilhante, rodóstomo, negro). A categoria está fechada: 7 de 7.
4. `/equipamentos/aquecedores/` — só depois que o cluster de aquecimento estiver indexado.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir em `dados/indexacao.md`, e só dobrar se indexou **e** apareceu.

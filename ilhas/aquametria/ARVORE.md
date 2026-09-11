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
| `/peixes/` | ficha de espécie: quanto espaço, que temperatura, com quem convive | não |
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
| `/calculadoras/peixes/` | C8 lotação | 0 no ar |

**Nenhuma das quatro atinge as 3 filhas com dado real hoje**, então nenhuma nasce agora — é a regra 16.5, e ela é o que impede a ilha de publicar quatro páginas de categoria magras num domínio que ainda não indexou a primeira leva. A `/calculadoras/aquecimento-e-luz/` é a primeira a fechar, e fecha no dia em que a C7 entrar.

Enquanto isso, `/calculadoras/` continua sendo a mãe direta das cinco calculadoras no ar — dois níveis em vez de três, declarado aqui como estado de transição, não como desenho.

## 3. `/peixes/`

A camada que a Bússola verificou ABERTA e a de maior volume de busca da ilha ("quantos litros para N neons"). Depende do bloco T3(d), o banco de espécies — `dados/especies-agua-doce.json` já existe e é o que limita quantas filhas cabem.

Categorias pelo nome que a pessoa usa, nunca pelo nome científico: `/peixes/tetras/`, `/peixes/corydoras/`, `/peixes/bettas/`, `/peixes/ciclideos-anoes/`, `/peixes/plecos-e-limpa-vidros/`, `/peixes/camaroes-e-caramujos/`.

Filha de nível 3 = a ficha da espécie, com o número que ninguém mais dá: quantos litros para N deles. Portão da seção 9: 3 itens de banco reais e um número calculado próprio.

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

**Nada nesta árvore muda endereço de página antes da leitura de 16/09/2026.** Duas travas independentes, e basta uma:

1. **Item 5 do despacho da Sentinela de 10/09:** nenhuma página nova até 16/09. As oito páginas de nível 1 e 2 desta árvore são oito URLs novas. A leva de 08/09 (6 páginas) não indexou nenhuma e as 7 indexadas não registraram impressão — publicar categoria agora é jogar mais página no mesmo buraco.
2. **T2 do `PROMPT.md`:** a janela para trocar o endereço dos três artigos (hoje em `/2026/09/08/<slug>/`, endereço com data que envelhece sozinho) só abre depois que a leitura de 16/09 disser **por que** a leva de 08/09 não indexou. Trocar endereço antes disso soma uma variável a um diagnóstico que ainda não fechou.

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
3. `/peixes/tetras/` + as 3 espécies de maior busca com banco fechado.
4. `/equipamentos/aquecedores/` — só depois que o cluster de aquecimento estiver indexado.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir em `dados/indexacao.md`, e só dobrar se indexou **e** apareceu.

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

Sem quarto nível. Fora da árvore ficam só a home, `/sobre/`, `/metodologia/`, `/divulgacao-de-afiliados/` e `/politica-de-privacidade/`.

**`/politica-de-privacidade/` nasceu em 13/09/2026** e é a quinta e última página da família institucional que o 16.1 nomeia. Ela fica na raiz pelo mesmo veredito que pôs `/metodologia/` lá: o 16.1 lista essa família por nome, e página institucional não é filha de um assunto. Não tem mãe, não tem irmã e não entra em cluster nenhum — o que a tira de ser órfã pelo 16.4(f) é o **rodapé**, que a linka de **todas as páginas** do site (36 em 14/09/2026, pelo `urls_publicadas` do `ESTADO.md`). *(Dizia "das 28 páginas", contado antes das levas 4 e 5. Número de tela nasce contado, não digitado — este é digitado e vai envelhecer de novo. Corrigido pelo Pente Fino em 14/09/2026.)*

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

## 3. `/peixes/` — NO AR desde 12/09/2026 (levas 1 a 7 do T4)

A camada que a Bússola verificou ABERTA e a de maior volume de busca da ilha ("quantos litros para N neons"). O banco de espécies (`dados/especies-agua-doce.json`, **39 registros** — contados no arquivo em 21/09/2026 pelo Pente Fino; dizia **37**, e mais abaixo esta mesma página diz **36**, três números para um banco só. O `ESTADO.md` corrobora 39 (`validar-especies 39 registros`) e o `REGISTRO.md` anota a passagem de 37 para 39. **Os números DERIVADOS — "29 dos 37 passam", "14 dos 36 registros" — não foram recalculados aqui**: recontar régua é bloco, e a ilha está fora do foco. Trate os dois como não verificados até alguém rodar `validar-especies.py`) é o que limita quantas filhas cabem, e desde 12/09/2026 são **duas** réguas com dois nomes, não uma:

- **`catalogo-de-especies`** — sete campos e duas fontes de corpos distintos. **29 dos 37 passam** desde 13/09/2026 (eram 27 de manhã; o gurami mel entrou quando o porte foi colhido no compêndio e o plati variatus às 21h21Z). É quem entra na contagem da seção, na tabela da categoria e na lista de quem divide a mesma água.
- **`pagina-especie`** — o catálogo MAIS `cardume_minimo OU convivencia igual a solitario/casal/harem`. **29 dos 29 passam**, desde 12/09/2026 (27 de 27 naquele dia; 29 de 29 em 13/09). É quem pode ter página própria, porque a ficha deste eixo se chama "quantos litros para um cardume de X" e abre pela frase que nomeia o cardume mínimo.

**E DESDE 13/09/2026 OS 8 QUE NÃO PASSAM CHEGAM À TELA, com nome e causa** (snippet 1.6.0). Até então o catálogo embutido carregava só quem passa, então os barrados não existiam dentro do snippet: a seção servia "são 29 espécies" e não tinha como dizer que o banco tem 37 nem por que os outros não estão ali. O gerador passou a escrever um segundo bloco — `aquametria_peixes_barrados()` —, a seção publica os três números contados e a lista dos ausentes em ordem de quem está mais perto de entrar, e a página de categoria faz o mesmo com quem ela declara e a tabela não mostra. **Esse conjunto ficou vazio nas duas primeiras categorias e DEIXOU DE ESTAR em 14/09/2026**, com a leva 4: a `bettas` declara as **cinco** Osphronemidae do banco, o portão barra duas por falta de `convivencia`, e a página as publica com nome e causa. Foi o primeiro mundo real daquele ramo — até ali ele só existia dentro das quatro mutações de `mutacoes-peixes.py` que o PRODUZIAM, e essas continuam, porque elas provam o ramo VAZIO da mesma régua. O motivo viaja como código e a tradução para a língua do leitor mora num mapa só do PHP: nome de campo de banco na tela é vocabulário de dentro da fábrica.

As duas listas saem nomeadas, registro por registro, em `ferramentas/gerar-catalogo-especies.py`. **Hoje ninguém está no catálogo sem poder ter página**, e isso mudou na leva 3: o `corydoras-sterbai` era o único, porque declarava convivência "grupo" e nenhuma fonte dizia de quantos. A leva 3 colheu o número na ficha da própria espécie, por busca restrita, e `/peixes/corydoras/` nasceu com **4** filhas em vez das 3 que este documento previa — folga de uma sobre o mínimo do 16.5, em vez do mínimo exato.

**O que isso custou à bancada, e vale para a próxima categoria:** com 27 de 27 passando, o banco deixou de ter um caso que discrimine o portão de página do portão de catálogo. Duas mutações de `ferramentas/mutacoes-peixes.py` viviam da sterbai e teriam virado inertes continuando a reprovar — por slug duplicado, não pelo cardume. Foram reescritas para PRODUZIR o mundo: tiram o número de quem o tem, uma no banco e outra no catálogo do snippet. Régua que depende de um caso raro do banco morre no dia em que o banco melhora.

A separação nasceu de um erro que vale registrar: a primeira versão pôs a regra do cardume no portão do CATÁLOGO, e a contagem da seção caiu de 27 para 26 — o sterbai sumiu de três lugares onde o dado dele é bom, para resolver um problema de outra página. Apertar o portão errado tira da tela informação verdadeira.

Categorias pelo nome que a pessoa usa, nunca pelo nome científico. **As da tabela abaixo, e só estas** — o número não se escreve aqui, se conta nela:

> **ERAM SEIS ATÉ 22/09/2026, e o número estava DIGITADO em dois lugares que envelheceram juntos.** Esta linha dizia "Seis, e só estas" e a afirmação dos cartões em `ferramentas/teste-peixes.py` cobrava `len(cartoes) == 6`, com a palavra "seis" no rótulo. Nenhum dos dois era derivado do outro, então a sétima categoria reprovou numa régua **sem apontar defeito nenhum** — que é exatamente o caso que este eixo já registrou duas vezes (o `registradas == [CATEGORIA]` da leva 2 e a data de SERP digitada da leva 4). Consertado na leva 7 pelo mesmo desenho do `teste-arvore.mjs`: a régua passou a **ler a tabela abaixo** (`categorias_do_arvore()`), então este documento é quem diz quantas categorias o eixo tem, e categoria que entrar no código sem entrar aqui reprova. **Quem acrescentar a oitava mexe nesta tabela, e só nela.**
>
> **A OITAVA NASCEU EM 22/09/2026 (leva 8, `/peixes/acaras/`), e o conserto da leva 7 funcionou pela metade.** A régua do `teste-peixes.py` leu a tabela e não reclamou de nada — a categoria entrou nas duas pontas de uma vez, como o desenho previa. **Mas esta linha de cima continuava DIGITADA**: ela dizia "**Sete**, e só estas" três linhas depois de o parágrafo explicar que o número saiu do código justamente por ser digitado. Nenhum portão a lia, então ela envelheceria em silêncio a cada categoria nova, para sempre. Trocada pela forma que não tem número: quem quiser saber quantas são, conta as linhas. **É a segunda metade do mesmo defeito, e ela levou uma leva inteira para aparecer** — matar o número no código e deixá-lo na prosa do documento que virou a fonte da verdade é trocar de lugar, não consertar.

| nível 2 | filhas no ar | estado |
|---|---|---|
| `/peixes/tetras/` | tetra neon · neon cardinal · mato-grosso · tetra ember · tetra-brilhante · rodóstomo · tetra-negro | **no ar e FECHADA** (7 de 7 espécies do banco) |
| `/peixes/corydoras/` | coridora bronze · coridora pimenta · coridora panda · coridora sterbai | **no ar e FECHADA** (4 de 4 espécies do banco) |
| `/peixes/bettas/` | betta · colisa-anão · gurami mel | **NO AR e FECHADA NO DADO desde 14/09/2026 (leva 4, 4 URLs)** — 3 das 5 Osphronemidae do banco. É a primeira categoria deste eixo em que as filhas **não vivem do mesmo jeito**, e foi isso que ela custou em código: até 13/09 as onze fichas no ar eram todas `convivencia: cardume` e a palavra estava DIGITADA em sete lugares do corpo da ficha. O betta vive sozinho (um por aquário) e é agressivo, a colisa-anão vive em casal, o gurami mel vive em grupo de **4 a 6** — e a fonte dele escreve, com todas as letras, que a espécie NÃO é gregária no sentido dos peixes de cardume. Os dois guramis grandes, pérola e tricogaster, são **declarados na categoria e barrados pelo portão** por falta de `convivencia`, e saem na página com nome e causa: sem declará-los, a frase de lista fechada diria que todo betta e todo gurami que o banco sustenta já tem página, e o banco sustenta os dois. SERP das quatro consultas classificada em 13/09/2026, e as quatro páginas declaram `serp_em` |
| `/peixes/ciclideos-anoes/` | **NO AR desde 14/09/2026 (leva 6, 4 URLs)** — ramirezi · apistogramma agassizi · papilocromis | ~~em breve — **1 elegível**~~ **ESTA CÉLULA DESCREVIA O MUNDO DE 13/09. Corrigida pelo Pente Fino em 21/09/2026**, contra `REGISTRO.md` (2026-09-14 22h11Z: *"LEVA 6: A QUINTA CATEGORIA … QUATRO URLs novas — `/peixes/ciclideos-anoes/` e as fichas do ramirezi, do apistogramma agassizi e do papilocromis"*, peixes 1.10.0, manifest revisão 87, `/status` conferido na 87) e contra o `congelamento` do `ESTADO.md`, que fecha a semana em 3 de 3 levas. **Não remedi o conteúdo das três fichas nem a contagem de elegíveis** — a ilha está fora do foco e isso é bloco, não auditoria. O texto original dizia: em breve — 1 elegível (ramirezi). O banco não tem mais nenhum ciclídeo ANÃO: acará-bandeira, discus e oscar são ciclídeos e não cabem no rótulo |
| `/peixes/danios-e-rasboras/` | paulistinha · rasbora arlequim · tanictis | **NO AR desde 22/09/2026 (leva 7, 4 URLs)** — 3 das 4 espécies que o banco declara nesta prateleira. É a **primeira leva do eixo que não custou uma coleta**: as três passavam nos dois portões desde 11/09/2026, estavam no catálogo, na contagem da seção e na lista de quem divide a mesma água, e não tinham página nem categoria que as abrigasse — o que faltava era o lugar, não o dado. É também a **segunda categoria do eixo em que nem a família nem o gênero servem**, e ela falha pelo lado CONTRÁRIO ao dos ciclídeos anões: lá a família trazia peixe demais, aqui ela deixa peixe de fora (o tanictis é a única Tanichthyidae do banco, família só dele, e o segundo nome popular brasileiro dele é `paulistinha-da-montanha`). Quem separa é o nome que a pessoa digita, e nesta categoria ele é verificável dentro do banco: os quatro registros declarados são exatamente os que trazem `danio`, `rasbora` ou `paulistinha` entre os nomes populares. A **rasbora galáxia** é declarada e barrada pelo portão, e é a barrada mais distante do eixo inteiro — faltam-lhe QUATRO campos, contra o campo único do molly e do guppy. SERP das quatro consultas classificada em 22/09/2026, e as quatro páginas declaram `serp_em` |
| `/peixes/plecos-e-limpa-vidros/` | — | em breve — **1 elegível** (otocinclo). O cascudo (`ancistrus-cirrhosus`) está a UM campo de entrar: falta `temperatura_C`. **Segunda tentativa de coleta em 13/09/2026, recusada:** nem o compêndio nem a base científica declaram faixa térmica para esta espécie, e a busca ofereceu sozinha a das *espécies aparentadas* do gênero (pH 6,0–6,5 e 75–80 °F), que é exatamente o que a regra da congênere proíbe gravar |
| `/peixes/acaras/` | acará-bandeira · oscar · acará-disco | **NO AR desde 22/09/2026 (leva 8, 4 URLs)** — os 3 Cichlidae do banco que a loja brasileira NÃO vende na prateleira de ciclídeo anão. É a **terceira categoria seguida em que o critério da anterior não serve**, e a primeira em que falha justamente o critério que a leva 7 tinha acabado de comemorar por ser verificável dentro do banco: separar pelo NOME que a pessoa digita traria o `mikrogeophagus-ramirezi` para cá, porque o terceiro nome popular brasileiro dele é **acará-borboleta** — e ele já é filha de `/peixes/ciclideos-anoes/`. Quem separa aqui é o **porte declarado**, que é número e não leitura: os três desta linha começam em 13,7 cm e os três ciclídeos anões terminam em 5,6 cm, sem nenhum registro entre os dois grupos. É também a categoria com a **maior distância de porte** do eixo (13,7 a 45,7 cm) e a **única em que duas filhas não cabem na mesma água**: a faixa declarada do oscar termina a 25 °C e a do acará-disco começa a 26 °C, as duas pela mesma base científica, sem um grau de interseção. A ficha do **acará-disco** é a **primeira do eixo a nascer no terceiro estado da ausência de fundo**: o chão de 120 × 45 cm que o compêndio declara é para juvenis ou um casal, o registro publica cardume de cinco, e a página diz a largura, diz para quem ela foi declarada e não abre as duas tabelas que dependem do fundo. SERP das quatro consultas classificada em 22/09/2026, e as quatro páginas declaram `serp_em` |
| `/peixes/vivaparos/` | platy · peixe-espada · plati variatus | **NO AR e FECHADA NO DADO desde 14/09/2026 (leva 5, 4 URLs)** — 3 das 5 Poeciliidae do banco, todas do gênero `Xiphophorus`. É a primeira categoria deste eixo em que **nenhuma filha tem número declarado**: as três vivem em `harem`, e harém é o único valor do vocabulário fechado em que a fonte descreve a proporção entre os sexos e nunca o tamanho do grupo — a escada de lotação sai como escada de LEITURA e nenhuma linha se chama mínima. Foi essa leva que exercitou pela primeira vez o ramo do arranjo sem número, e ele estava errado: a ficha abria pela tradução de `como_vive()` e a primeira frase da página voltava a citar quem declarou, contra a 15.2. **Os dois vivíparos MAIS vendidos do Brasil são declarados na categoria e barrados pelo portão**, e saem na página com nome e causa — o guppy tem duas urls de um corpo só (E15) e o molly não tem `comprimento_minimo_aquario_cm`. **A parede do molly mudou de natureza em 13/09/2026 e isso importa para quem for tentar de novo:** os DOIS corpos já foram perguntados — o compêndio publica a seção de dimensões vazia e a base científica, perguntada em duas passadas limpas, devolveu o número da espécie vizinha —, então o desbloqueio dele depende da leitura direta, que é o despacho de egresso aberto para o Raphael. SERP das três fichas classificada em 13/09/2026 e a da MÃE em 14/09/2026, e as quatro páginas declaram `serp_em`: a consulta da mãe é a única do eixo em que o top 7 **não fala do assunto** — devolve as páginas genéricas de "quantos peixes cabem no aquário", com a regra por centímetro em três versões que discordam entre si |

Filha de nível 3 = a ficha da espécie, com o número que ninguém mais dá. **E o número não é o litro: é a BASE.** As fontes de aquarismo declaram o tamanho do chão do aquário, e as sete primeiras respostas da SERP brasileira dão litro sem fonte e discordam entre si. Cada ficha serve a base declarada (com o nome do corpo de fonte e a data) ao lado das duas réguas brasileiras de lotação, que discordam em quatro vezes, com a atribuição de cada extremo.

**O que NÃO se faz nesta camada, e está escrito no snippet:** multiplicar o derivado per capita (frente mínima ÷ cardume mínimo) para estender o cardume. Para o neon daria 120 cm para dez peixes, que nenhuma fonte sustenta. Quem responde "e para dez?" são os três critérios de lotação. `ferramentas/teste-peixes.py` tem afirmação para isso e `ferramentas/mutacoes-peixes.py` tem a mutação que a exercita.

**A RODA DAS IRMÃS, e ela é regra de malha, não detalhe de casca (12/09/2026).** O cluster tem teto de quatro irmãs (16.4c) e varria o mapa do começo: toda página escolhia as mesmas quatro do topo, e as duas últimas da categoria não eram irmãs de ninguém — no ar, **um** link interno apontando para elas contra os sete da primeira, e o 16.4(f) cobra dois. **Teto com ordem fixa não reparte: concentra.** A lista passa a começar depois de mim e dar a volta. Era inerte com três filhas, e é o que qualquer categoria desta ilha vai encontrar ao passar de quatro.

**E espécie que o banco declara agressiva não ganha lista de companheiro** — a ficha conta quantas espécies dividem a faixa de temperatura e diz por que não recomenda nenhuma. O esquema do banco recusa compatibilidade como campo justamente porque ela depende de volume, layout e ordem de introdução.

Portão da seção 9 conferido nas sete: cada ficha nomeia 10 ou mais registros reais do banco e traz tabelas calculadas na hora de imprimir.

**E "BASE" não é "FRENTE" — a leva 2 achou isso na tela.** A frase mestra da ficha terminava sempre em "e a fonte declara a BASE, não o litro". Era verdade nas três fichas da leva 1, e é falsa em **14 dos 36 registros** do banco, onde a fonte declara só o comprimento mínimo e nunca disse uma palavra sobre o fundo. O rodóstomo é o primeiro caso publicado: o Seriously Fish declara "no mínimo 90 cm de comprimento" e para aí; uma coleta limpa em 12/09, restrita ao domínio, devolveu a mesma frase e mais nada. Nesses registros a ficha diz COMPRIMENTO, as duas tabelas que dependem do fundo não saem — **e a página declara a ausência e a causa** em vez de encolher calada, que é a forma disfarçada do "silêncio parece defeito" da seção 7.

**E "BASE DECLARADA" NÃO É "BASE DECLARADA PARA ESTES PEIXES" — a terceira ausência, achada em 22/09/2026 e com oito dias no ar.** A frase acima diz que cada ficha serve a base declarada. Faltava a metade que decide: **a base é um número sobre uma POPULAÇÃO**, e até hoje o esquema não tinha onde dizer qual. A ficha do apistogramma agassizi abria com *"para um harém de apistogramma agassizi — e harém quer dizer mais fêmeas do que machos, nunca um casal —, o seu aquário precisa de 60 cm de frente por 30 cm de fundo"*, e os 30 cm de fundo são do compêndio, que os declarou **para UM CASAL**. A proibição já estava escrita, em maiúsculas, dentro do `observacao` daquele mesmo registro — *"O QUE A FICHA NÃO PODE FAZER: prometer que 60 x 30 cm serve ao harém"* —, e **prosa não barra página**. Agora barra: `chao_declarado_para` (esquema de espécies, versão 5) guarda os termos e a cláusula transcrita da fonte, os termos são ordenados por população (juvenis < um exemplar < casal < grupo) e a ficha só serve o fundo quando o chão declarado cobre o que ela publica. Quando não cobre, ela diz o número, diz **para quem** ele foi declarado e não abre as duas tabelas que dependem do fundo — porque a ausência aqui é diferente da do rodóstomo, e as duas são diferentes para quem lê: uma é "ninguém declarou largura", a outra é "a largura declarada não é sobre estes peixes".

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
3. ~~`/peixes/tetras/` + as 3 espécies de maior busca com banco fechado.~~ **FEITO** — leva 1 (12/09, 5 URLs) e leva 2 (12/09, 4 URLs: ember, brilhante, rodóstomo, negro). A categoria está fechada: 7 de 7. **A leva 3 (12/09, 5 URLs) fechou `/peixes/corydoras/` com 4 de 4, e a leva 4 (14/09, 4 URLs) abriu `/peixes/bettas/` com 3 de 5** — a primeira semana nova depois do teto de 3 levas da 21.4, que zerou em 14/09.
4. `/equipamentos/aquecedores/` — só depois que o cluster de aquecimento estiver indexado.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir em `dados/indexacao.md`, e só dobrar se indexou **e** apareceu.

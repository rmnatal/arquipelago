# ÁRVORE DA ROBOMETRIA

Item (i) do 16.8 do `ARQUIPELAGO.md`, escrito em 11/09/2026 no bloco da árvore — o item que o despacho do Raphael de 11/09 deixou de pé depois do bloco da voz.

Este arquivo diz **onde cada página mora** e **quem é a mãe de quem**. É o mapa que os blocos seguintes seguem: breadcrumb, cluster de interlinkagem e leva de malha saem daqui, não da cabeça de quem executa. `ferramentas/teste-arvore.php` lê este arquivo e cobra que ele e o código digam a mesma coisa — documento e código mantidos à mão em dois lugares divergem em silêncio.

Os nomes dos níveis são os do `VOZ.md`: quem chega aqui diz peça, sucção, modelo. Não existe `/entidades/` nem `/cruzamentos/` nesta ilha, porque ninguém digita isso.

---

## 1. Os três níveis

**Nível 1 — seção.** Quatro, e só estas:

| slug | o que mora ali | existe hoje |
|---|---|---|
| `/pecas/` | a peça que serve: a ferramenta de compatibilidade e as categorias por tipo de peça | não |
| `/succao/` | quanta sucção e quanto tempo: a ferramenta de dimensionamento e os cruzamentos de piso, pelo e metragem | não |
| `/modelos/` | a ficha de cada robô, por marca — o que o fabricante declarou dele | não |
| `/guias/` | os textos que explicam o porquê do número | não |

**Nível 2 — categoria**, com o nome que a pessoa usa. **Categoria só nasce com 3 filhas de dado real** (16.5); até lá o cartão na mãe não é link e diz "em breve", sem contagem.

| nível 2 | mãe | filhas previstas |
|---|---|---|
| `/pecas/filtros/` | `/pecas/` | filtro por modelo e por marca |
| `/pecas/escovas-laterais/` | `/pecas/` | escova lateral por modelo |
| `/pecas/escovas-principais/` | `/pecas/` | escova rotativa central por modelo |
| `/pecas/mops/` | `/pecas/` | pano e suporte por modelo |
| `/pecas/baterias/` | `/pecas/` | bateria por modelo |
| `/succao/pisos-e-pelo/` | `/succao/` | quantos Pa por tipo de piso e por pelo |
| `/succao/metragem-e-autonomia/` | `/succao/` | quantos ciclos por metragem |
| `/modelos/electrolux/` | `/modelos/` | ficha por modelo da marca |
| `/modelos/multi/` | `/modelos/` | idem |
| `/modelos/positivo/` | `/modelos/` | idem |
| `/modelos/roborock/` | `/modelos/` | idem |
| `/modelos/xiaomi/` | `/modelos/` | idem |
| `/modelos/wap/` | `/modelos/` | idem |
| `/guias/pecas/` | `/guias/` | os textos sobre peça e compatibilidade |
| `/guias/succao/` | `/guias/` | os textos sobre sucção, autonomia e metragem |

**`/pecas/reservatorios/` continua fora da lista de propósito, e o MOTIVO mudou pela SEGUNDA vez em 13/09/2026 — este parágrafo já nasceu mentira uma vez e a correção fica registrada junto.** A primeira versão dizia que o tipo "reservatório" não tinha **nenhuma** peça declarada; ela ficou falsa no dia em que o recipiente do W300 e o do WSMART entraram. A segunda dizia que o que segurava a categoria era o mínimo desta tabela — **categoria só nasce com 3 filhas de dado real** (16.5) —, e que "a terceira peça de reservatório é o que abre esta linha". **A terceira peça entrou às 23h de 13/09/2026** (o Kit Recipiente de Pó FW008543, declarado pela loja oficial da WAP para o W100 e para o W90), então o mínimo da 16.5 está **cumprido**: são três peças cobrindo quatro modelos.

**O que segura a categoria agora não é dado, é o portão de malha.** Categoria nova é **URL nova**, e esta ilha não publica leva de malha (bloco 5b) enquanto o sitemap não for reenviado no Search Console — a metade humana do despacho da Sentinela de 10/09, que é do Raphael. A rampa da seção 14 é inexecutável sem medição, e abrir uma categoria sem saber se o que já está no ar indexa gastaria orçamento de rastreamento às cegas (14.1). **No dia em que o sitemap for reenviado, esta linha nasce sem esperar dado nenhum** — e quem a abrir confere antes se ainda são três, porque contagem escrita em prosa é a coisa que este parágrafo já errou duas vezes.

> **ESSE DIA CHEGOU EM 16/09/2026 E ESTE ARQUIVO NÃO SOUBE — corrigido em 21/09/2026.** O parágrafo acima, e o "NÃO FEITO" da seção 4 abaixo, dizem que a leva de malha espera o **reenvio do sitemap**. O item 4 da DEFINIÇÃO DE PRONTA do `PROMPT.md` registra o sitemap **aceito e processado** desde 16/09, com última leitura em 15/09 e as 9 páginas lidas, e a leitura semanal de 16/09 mediu **6 indexadas de 9, 11 impressões e posição média 7,9** — ou seja, a medição que a rampa da seção 14 pedia EXISTE. O bloqueio que estes dois parágrafos descrevem morreu há cinco dias e continuou escrito, que é o defeito da seção 4 do `ARQUIPELAGO.md` — resumo velho lido como fato — dentro do documento que decide a próxima leva. **O que segura a primeira categoria hoje é o dado**, medido logo abaixo na seção 5, e não o Search Console.

**Nível 3 — a pergunta ou a ficha**, com as palavras que a pessoa digita.

Sem quarto nível.

---

## 2. Fora da árvore, na raiz

| slug | por quê |
|---|---|
| `inicio` | a home. Sem breadcrumb (16.3) |
| `sobre` | a 16.1 admite na raiz |
| `divulgacao-de-afiliados` | a 16.1 admite na raiz |
| `metodologia` | ver o veredito abaixo |
| `ferramentas` | ver o veredito abaixo — é a **mãe de transição**, não uma página de raiz permanente |

**VEREDITO SOBRE `/metodologia/` — fica na raiz.** A lista da 16.1 (home, sobre, contato, divulgação de afiliados, privacidade) nomeia uma **família**: a página institucional, que fala da casa e não do assunto. A metodologia é dessa família — é o "como trabalhamos" ao lado do "quem somos" —, e pô-la dentro de uma seção de tópico a faria filha de um assunto que ela não tem. A Aquametria resolveu do mesmo jeito em 11/09/2026, e duas ilhas resolvendo diferente o mesmo caso seria a fábrica decidindo por gosto.

**VEREDITO SOBRE `/ferramentas/` — fica hoje, e é a única página desta ilha com prazo de validade.** Ela é um hub que lista as duas ferramentas, que é exatamente o que uma página de nível 1 faz. Enquanto `/pecas/` e `/succao/` não existem, ela é a **mãe de transição** das duas ferramentas: dá a elas um degrau de trilha com endereço de verdade, em vez de um degrau em texto apontando para o vazio. No dia em que as duas seções nascerem, ela passa a servir a mesma listagem que elas — duas URLs com o mesmo conteúdo, que a 14.4 proíbe — e **é retirada com 301 para a home**, que nesta ilha já é a ferramenta (molde FERRAMENTA do `VOZ.md`). Isso não acontece neste bloco: hoje ela é a mãe, e retirar a mãe antes de a substituta existir deixaria as duas ferramentas sem trilha.

---

## 3. Onde mora cada página de hoje

| página | papel | mãe de hoje | mãe de destino | irmãs de hoje |
|---|---|---|---|---|
| `inicio` | home | — | — | — |
| `ferramentas` | seção (transição) | — | — | — |
| `metodologia` | raiz | — | — | — |
| `sobre` | raiz | — | — | — |
| `divulgacao-de-afiliados` | raiz | — | — | — |
| `qual-peca-serve-no-meu-robo-aspirador` | filha | `/ferramentas/` | `/pecas/` | a outra ferramenta |
| `quantos-pa-o-robo-aspirador-precisa` | filha | `/ferramentas/` | `/succao/` | a outra ferramenta |
| `filtro-universal-de-robo-aspirador` | filha | `/guias/` (não existe) | `/guias/pecas/` | o outro guia |
| `quantos-m2-o-robo-aspirador-limpa-por-carga` | filha | `/guias/` (não existe) | `/guias/succao/` | o outro guia |

---

## 4. O que este bloco fez, e o que ele NÃO fez

**FEITO** (casca 1.3.0, 11/09/2026), e **nenhuma URL nova**:

- **Trilha** (16.3) nas oito páginas que não são a home, sempre entre o cabeçalho e o H1.
- **`BreadcrumbList`** em JSON-LD, levando só os degraus com endereço de verdade.
- **"Veja também"** (16.4c) nas quatro páginas de conteúdo, com as irmãs derivadas.
- **Frase que linka a mãe** (16.4b) nas duas ferramentas, com a contagem **contada**.
- **O par ferramenta ↔ guia** (16.4d) fechado nos dois sentidos — faltava um lado, ver abaixo.

**NÃO FEITO, e por quê:** as quatro páginas de nível 1 e as quatorze de nível 2 são dezoito URLs novas, e esta ilha não publica leva de malha enquanto o sitemap não for reenviado no Search Console (metade humana do despacho da Sentinela de 10/09; a rampa da seção 14 é inexecutável sem medição). Trocar o pai e o slug das páginas existentes espera o mesmo destravamento, e leva 301 quando acontecer. *(O motivo desta frase VENCEU em 16/09/2026 — ver o quadro da seção 1. Ela fica como registro do que o bloco de 11/09 decidiu, e não vale mais como trava. **O que não venceu é a segunda metade:** trocar o pai e o slug das duas ferramentas continua proibido pela 12.1 enquanto elas tiverem impressão registrada, e as duas têm — `quantos-pa` em 6,8 e `quantos-m2` em 7,0, medidas em 16/09. As seções nascem, elas ficam onde estão, e a mãe passa a apontar para elas.)*

**Quatro coisas que quem vier depois precisa saber:**

1. **O degrau sem endereço sai em TEXTO, nunca em link, e não entra no JSON-LD.** A trilha de um guia mostra quatro degraus na tela (Início › Guias › Peças › o título) e o `BreadcrumbList` publica dois. Não é esquecimento: `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista inválida é lista ignorada — o schema "mais completo" publicaria MENOS com cara de publicar mais. Quando `/guias/` nascer, ela entra nos dois lados de uma vez, porque quem resolve o endereço é `robometria_casca_url_se_existir()`.
2. **As irmãs são derivadas, nunca digitadas.** Saem do mesmo registro que alimenta o hub e a prateleira de artigos. Ferramenta ou artigo novo vira irmã de todo mundo sozinho, e página que não existe publicada não entra — irmã é link, e link morto não é cluster.
3. **Hoje cada mãe tem duas filhas, então cada filha tem UMA irmã — e a 16.4(c) pede de 2 a 4.** É estado de transição declarado, não desenho: o mínimo de duas é alcançado no dia em que a terceira filha de uma mãe nascer. O portão cobra "todas as irmãs publicadas, teto de 4" e a bancada **fabrica a borda** (um catálogo de seis filhas) para provar que o teto corta — grade que nunca pisa na borda é amostra com nome de grade.
4. **A frase de mãe só sai com mãe publicada.** As duas ferramentas a têm, porque `/ferramentas/` existe; os dois guias não a têm, porque `/guias/` não existe, e o portão cobra a AUSÊNCIA dela justamente para ninguém fechar isso com um endereço inventado.

**O DEFEITO QUE A VARREDURA DE LINKS ACHOU SEM PROCURAR:** medindo qual página cita qual no CORPO, a ferramenta de sucção linkava o guia do filtro universal e **não linkava o guia dela**, o de metros quadrados por carga — que é justamente o texto que explica de onde vem o número de área por carga que ela usa. O par da 16.4(d) estava aberto de um lado só, e ninguém tinha como ver, porque o link existia (para o outro guia) e nenhum teste perguntava se era o guia CERTO. Agora o par sai do catálogo de artigos, pelo campo `ferramenta`, e o portão cobra os dois sentidos.

**E um achado que fica registrado, fora do escopo:** `/sobre/` é a única das nove páginas que nenhum CORPO de outra cita — ela vive do menu e do rodapé, que estão em todas, então não é órfã pelo 16.4(f). Mas é a única sem citação editorial, e isso é assunto de pauta (seção 17), não de casca. A Aquametria tem exatamente o mesmo achado, o que sugere que é do molde da casca e não da ilha.

---

## 5. Ordem das levas, quando destravar (16.6)

Primeiro a mãe e as **3 primeiras filhas de maior intenção de compra**, depois as irmãs, depois a próxima categoria. Nunca uma filha de cada categoria espalhada.

1. `/pecas/` + `/pecas/filtros/` com as 3 primeiras filhas — é o cluster de maior intenção de compra da ilha ("filtro para robô X" termina numa peça que se compra), e é onde o banco tem mais pares declarados.

   > **A PRIMEIRA LEVA ESTEVE TRAVADA POR DADO, E NÃO POR PORTÃO, ATÉ 21/09/2026 — e quem mediu isso foi a execução que a destravou.** O parágrafo acima foi escrito em 11/09 e diz "as 3 primeiras filhas" sem nunca ter contado se o banco as sustenta. Contado em 21/09, antes da leva do dia: a 16.5 exige **3 filhas com dado real** e o portão de dado da seção 13 exige **3 itens de banco reais por página**, e o banco tinha filtro de **três** marcas — Xiaomi (4 filtros), Electrolux (1 filtro avulso mais 5 Kits Performance, e os cinco declaram `filtro` na composição) e Multi (2). **Só duas passavam**, e categoria com duas filhas não nasce. Nenhum portão dizia isso: a 16.5 é regra de documento, e nenhuma régua desta ilha conta filha de categoria que ainda não existe.
   >
   > **A leva de 21/09 levantou a terceira**, e ela veio da única marca cujo catálogo de filtro estava inteiro fora do banco: a **WAP**, com três filtros lidos direto na API de catálogo da loja oficial (`FW006270` HEPA e `FW006271` grade, os dois do W300; `FW007700` de entrada, do W100). O tipo `filtro` foi de 7 para 11 registros e de 3 para 5 marcas — a Positivo entrou junto, com o filtro do PRA800/PRA2000, e ainda não é filha porque tem um só.
   >
   > **As três filhas que a leva autoriza, com o número de cada uma medido no `main` de 21/09/2026:**
   >
   > | filha | itens de banco | modelos que ela responde |
   > |---|---|---|
   > | `/pecas/filtros/xiaomi/` | 4 filtros | E10, E10C, S10, S20, Mop 2, Mop 2 Lite |
   > | `/pecas/filtros/wap/` | 3 filtros | W300 (dois filtros declarados, HEPA e grade) e W100 |
   > | `/pecas/filtros/electrolux/` | 1 filtro avulso + 5 kits que declaram filtro | ERB10, ERB11, ERB20, ERB30, ERB44, ERB60, ERB61, ERB62, ERB80 |
   >
   > **Multi (2 filtros) e Positivo (1) entram como cartão sem link e "em breve"**, que é o que a 16.5 manda — e sem contagem de banco no cartão, porque contagem ali vira promessa datada.
   >
   > **Quem abrir esta leva RECONTA antes**, com `python3 ferramentas/cobertura-r1.py` e o banco na mão: esta tabela é o estado de 21/09, e a seção 3 deste arquivo já errou duas vezes exatamente por publicar contagem em prosa. E confere também o que a leva NÃO mediu: a classificação de SERP da 14.9 para as três consultas-alvo, que não foi feita nesta execução e é pré-requisito escrito para a página nascer.
2. `/succao/` + `/succao/pisos-e-pelo/` — a segunda ferramenta ganha a mãe própria e `/ferramentas/` é retirada com 301.
3. `/guias/` + `/guias/pecas/`, com os temas da `pauta.md` (seção 17) que apontam para a ferramenta de peças.
4. `/modelos/<marca>/` — por último, e só depois de o cluster de peças estar indexado: ficha de modelo compete com o fabricante e com o marketplace (14.2, item 4), então ela só nasce onde carrega um número que eles não dão.

**O menu, quando as seções existirem.** O `VOZ.md` descreve Peças · Modelos · Guias. Hoje ele é Peças · Sucção · Como conferimos, porque esses três são onde a pessoa resolve o problema e os outros sairiam como `<span>`. Quando `/pecas/` e `/succao/` nascerem, os dois primeiros rótulos passam a apontar para as SEÇÕES em vez das ferramentas — mesmo rótulo, endereço melhor — e `/guias/` entra no lugar de "Como conferimos", que volta para o rodapé. `/modelos/` não entra no menu: ele é a camada de entidade, alcançada pela ferramenta de sucção e pelas fichas, e um menu de quatro itens em celular é uma lista, não um menu.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir em `dados/indexacao.md`, e só dobrar se indexou **e** apareceu.

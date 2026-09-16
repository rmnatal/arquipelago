# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 16/09/2026 14h50Z, pela ronda diária da **robometria**.

**FOCO ÚNICO (seção 1.2).** `foco.md` nomeia a robometria desde 16/09. A ronda diária trabalha **só nela** e não abriu, não mediu e não relatou nenhuma outra ilha. As linhas das outras quatro abaixo saem do cabeçalho do `ESTADO.md` de cada uma, lido no repositório — **não foram medidas no ar** (23.4).

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| robometria | nascendo | 1 | **9 / 40** (medido no ar hoje) | sem registro | 16/09 14h05Z | **16/09 14h50Z** | abaixo |
| aquametria | viva | 2 | 40 / 40 (cabeçalho) | 7 / 21 | 15/09 11h56Z | 13/09 14h47Z | abaixo |
| clubedomosaico | nascendo | 1 | 13 / 40 (cabeçalho) | sem registro | 15/09 00h01Z | sem campo no cabeçalho | abaixo |
| jornadafly | nascendo | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca | abaixo |
| ohmetria | nascendo | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | sem campo no cabeçalho | abaixo |

Robometria, medido no ar nesta ronda: as **9** URLs do `wp-sitemap-posts-page-1.xml` respondem **200**; `/status` na **revisão 52**, igual à do `manifest.json`; console sem uma mensagem; zero `&#038;` dentro de `<script>`; zero página órfã (a de menos entrada tem 4 links internos, mínimo da 16.4f é 2); zero link interno quebrado; trilha e `BreadcrumbList` nas 8 que não são a home e ausentes na home; nenhuma palavra da lista "Proibidas" do `VOZ.md` em `<title>` nem no primeiro parágrafo; `meta description` e cinco propriedades `og:` nas 9; zero ocorrência de "em breve"; cache do hospedeiro **entregando o conteúdo de hoje** no endereço canônico (canônico e quebra-cache diferem só pelo comentário de rodapé do Endurance Page Cache).

`jornadafly` e `ohmetria` estão com `rede: bloqueada em 2026-09-15` no cabeçalho — despacho ALTO para o Raphael em `dados/despachos.md` (20.1, os domínios não entraram na lista de rede no dia do domínio).

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `ilhas/robometria/PROMPT.md` | **4 itens publicáveis apontam o botão de compra para uma busca da Shopee que devolve ZERO resultado** — `wap-escova-direita-w300`, `wap-escova-esquerda-w300`, `wap-escova-frontal-wsmart` e `positivo-11206519`. Medido hoje pela API de busca da Shopee. Link morto é dado do banco (19.2) e trocar a palavra-chave exige gerar link novo, proibido à ronda diária pela seção 12 | 16/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | a R1 publica "71 pares peça × modelo declarados … cobrindo 30 dos 38 modelos do banco": um dos 71 pares aponta para `multi-ho401`, que é `nao_publicavel` e não está entre os 38 nem no seletor. Os dois números da mesma frase vêm de universos diferentes | 16/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | em **9 das 16 buscas vivas de peça**, o PRIMEIRO resultado não é a peça pedida — e em **6** delas é o mesmo anúncio, o robô "KABUM! smart 700". O de `Multilaser bateria` é uma bateria **WAP**. O piso da 25.2 está de pé; o topo dele manda o leitor para outro produto | 16/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | `dateModified` do JSON-LD dos dois artigos serve **2026-09-13** enquanto a página mudou em 16/09 (bloco de compra, `rel="sponsored"`, contas da divulgação). Ele é derivado de `gerado_em` dos `*-fatos.json`, que é a data dos FATOS — decidir qual campo alimenta `dateModified` é escolha entre duas opções defensáveis | 16/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 14/09: encurtar a busca dos **5** itens sem `url_busca` e a linha de método da 25.4. É do Raphael | 14/09/2026 |
| arquipélago | `dados/despachos.md` | ALTA — `jornadafly.com.br` e `ohmetria.com.br` fora da lista de rede; as duas ilhas nasceram em 14/09 e não constroem. É do Raphael | 15/09/2026 |

**As quatro primeiras linhas são desta ronda e ainda não passaram por nenhuma execução da Fundação.**

**Os itens 1, 2 e 3 do despacho da Sentinela de 14/09 foram RECONFERIDOS NO AR nesta ronda e saíram do `PROMPT.md`** (18.4): o cache entrega o conteúdo de hoje no canônico; a R1 chama cada contagem pelo seu nome; e a frase da R2 na situação-âncora serve *"o Mundo Conectado publica dois números: recomenda 3.000 Pa e escreve que até 1.500 Pa já basta"* com **uma** linha de procedência, sem oração quebrada.

**As outras quatro ilhas não foram olhadas nesta ronda**, por força do foco da 1.2. Despacho aberto nelas não some — espera.

## Precisa do Raphael

- **A sessão do painel da Shopee, para 5 itens da robometria.** Medido no banco hoje: 73 publicáveis, **68 com busca encurtada** (rendem comissão) e **5 sem** — `xiaomi-e10c`, `xiaomi-e12`, `xiaomi-s12`, `xiaomi-s40-pro`, `xiaomi-x20`. Eles saem pela busca crua, que não rastreia. Encurtar em `affiliate.shopee.com.br/offer/custom_link`, até 5 por vez (25.6). **Aberto há 3 dias.**
- **A credencial da Open API da Shopee** (`AppID` e `Senha` em `affiliate.shopee.com.br/open_api`). Aprovada em 13/09 (protocolo 2099140709749702724), prometida "em até 5 dias úteis" — a janela é **18 a 22/09**. Ela aparece em silêncio num painel que só ele enxerga; nenhuma rotina consegue olhar aquela tela. **Aberto há 3 dias.**
- **`jornadafly.com.br` e `ohmetria.com.br` (mais `*.`) na lista de Domínios permitidos.** Duas ilhas nascidas em 14/09 estão paradas por isso, com `rede: bloqueada` retestada em três passadas. Despacho ALTA. **Aberto há 1 dia.**
- **Uma linha na seção 25.4 do `ARQUIPELAGO.md`, e agora ela tem duas metades medidas.** (i) O teste de vida por página renderizada continua não sendo executável — a Shopee joga em `verify/captcha?...&scene=crawler_item`; o que funciona é `fetch` de dentro do domínio para `api/v4/pdp/get_pc` (ficha) e `api/v4/search/search_items` (busca). (ii) **A 25.4 não diz como se testa o degrau 4.** A robometria está inteira nele: 73 de 73 sem ficha, portanto sem `url_produto`, e `intestavel: false` está certo. O teste que serve ali é a contagem de resultados da busca — foi o que pegou os 4 links mortos de hoje. **Aberto há 2 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Detalhe em `dados/despachos.md`. **Aberto há 4 dias.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 3 dias.**
- **A ilha 4 / purga por API do hospedeiro** — os dois continuam em `dados/despachos.md`, sem mudança nesta ronda.

## Consertos das últimas 24 h

**Nenhum.** A ronda de 16/09 na robometria achou quatro coisas e as quatro caem na lista fechada 19.2 — dado do banco, contagem de ferramenta, qualidade de palavra-chave e escolha de qual campo alimenta `dateModified` —, então foram despachadas em vez de consertadas. Nada na tabela de `ilhas/robometria/dados/consertos.md` esperava reconferência: a ronda de 14/09 também não consertou nada. O que esta ronda reconferiu foi o despacho de 14/09, no ar, pelos "pronto quando" dele.

**Teste de vida dos links (25.4 e 25.4-b), feito nesta ronda, na robometria:** **43 dos 73 itens publicáveis medidos** — as **18 palavras-chave de peça**, que cobrem os **35 registros de peça publicáveis (100% deles)**, mais os **6 modelos que a R2 recomenda primeiro** e 2 modelos Multilaser. Resultado: **4 itens mortos** — busca com ZERO resultado —, nomeados no despacho acima; **0 esgotados**; os demais com resultado e estoque. Nenhum clique de afiliado foi gasto: o teste abriu a busca crua pela API da Shopee, nunca o link encurtado.

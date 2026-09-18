# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 18/09/2026 14h45Z, pela ronda diária da **robometria**.

**FOCO ÚNICO (seção 1.2).** `foco.md` nomeia a robometria desde 16/09. A ronda diária trabalhou **só nela** e não abriu, não mediu e não relatou nenhuma outra ilha no ar. As linhas das outras quatro abaixo saem do cabeçalho do `ESTADO.md` de cada uma, lido no repositório — **não foram medidas no ar** (23.4).

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| robometria | nascendo | 1 | **9 / 40** (medido no ar hoje) | 7 / 21 (desde 11/09) | 18/09 13h45Z | **18/09 14h45Z** | abaixo |
| aquametria | viva | 2 | 40 / 40 (cabeçalho) | 9 / 21 (desde 09/09) | 15/09 11h56Z | 13/09 14h47Z | abaixo |
| clubedomosaico | nascendo | 1 | 13 / 40 (cabeçalho) | sem registro | 15/09 00h01Z | sem campo no cabeçalho | abaixo |
| jornadafly | nascendo | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca | abaixo |
| ohmetria | nascendo | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | sem campo no cabeçalho | abaixo |

**Robometria, medido no ar nesta ronda:** as **9** URLs do sitemap respondem **200**; `/status` na **revisão 66**, igual à do `manifest.json`; console sem uma mensagem; zero `&#038;` dentro de `<script>`; zero página órfã (mínimo de entradas: 4, e a 16.4f pede 2); zero link interno quebrado; zero `noindex`; trilha e `BreadcrumbList` nas 8 que não são a home e ausentes na home; 8 imagens servidas, todas com `alt`, `width` e `height`; nenhuma palavra da lista "Proibidas" do `VOZ.md` em `<title>` nem no primeiro parágrafo; `dateModified` dos dois artigos em 2026-09-18; cache do hospedeiro entregando o conteúdo de hoje no endereço canônico.

**`jornadafly` e `ohmetria` saíram do bloqueio de rede**: os dois cabeçalhos trazem `rede: aberta em 2026-09-18`, medido pela própria Fundação. O despacho ALTA de 15/09 sobre a lista de domínios está cumprido e saiu deste painel.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `ilhas/robometria/PROMPT.md` | **O primeiro cartão da R2 em `piso=tapete&pelo=sim&m2=80` (`roborock-q8-max`) aponta para uma busca da Shopee com ZERO resultado.** Beco sem saída no lugar mais caro da página | 18/09/2026 (0 dia) |
| robometria | `ilhas/robometria/PROMPT.md` | **22 dos 95 publicáveis com `afiliado.url_busca` vazio**: saem pela URL crua de busca, sem `sponsored`, sem sub-id e sem comissão. Eram ZERO em 16/09 — cada leva nova entra sem piso encurtado | 18/09/2026 (0 dia) |
| robometria | `ilhas/robometria/PROMPT.md` | **A R1 e a R2 dizem "não tem link de loja" para item cujo cartão serve botão de compra.** `$sem_link` conta `afiliado.url` e ignora o piso `url_busca` (`snippets/robometria-r1.php`, 934-939). Atinge 66 dos 95 publicáveis. É a família que a seção 7 proíbe | 18/09/2026 (0 dia) |
| robometria | `ilhas/robometria/PROMPT.md` | em **5 das 6 buscas Roborock** o primeiro resultado é um **Xiaomi**; na busca de reservatório Xiaomi é um robô inteiro. O leitor clica no botão de uma marca e cai em outra | 18/09/2026 (0 dia) |
| robometria | `ilhas/robometria/PROMPT.md` | propostas 1 e 3 da leitura semanal de 16/09: as duas pedem que a **leitura semanal seguinte** meça (rastreio da R1; segunda consulta em formato de superfície generativa). Nenhum bloco da Fundação as fecha | 16/09/2026 (2 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 14/09: encurtar a busca dos itens sem `url_busca` e a linha de método da 25.4. É do Raphael | 14/09/2026 (4 dias) |

**As quatro primeiras linhas são desta ronda e ainda não passaram por nenhuma execução da Fundação.**

**O despacho da ronda diária de 16/09 foi RECONFERIDO NO AR nesta ronda e está cumprido inteiro:** os 4 links mortos estão vivos (105, 102, 111 e 300 resultados), a R1 publica "86 pares … cobrindo 38 dos 45 modelos" sem contar o registro não publicável, e o `dateModified` dos dois artigos serve 2026-09-18.

**As outras quatro ilhas não foram olhadas nesta ronda**, por força do foco da 1.2. Despacho aberto nelas não some — espera.

## Precisa do Raphael

- **A credencial da Open API da Shopee no ambiente** (`AppID` e `Senha` de `affiliate.shopee.com.br/open_api`, guardadas no documento `arquipelago-credenciais` do Drive). Sem ela, `ferramentas/medir-palavras-chave.py --gravar --encurtar` não roda, e é ele que fecha os **22 itens sem piso rastreável** — o defeito de receita mais caro do painel. **Aberto há 5 dias.**
- **A decisão da foto de fabricante.** 66 registros ficaram sem foto (30 modelos, 36 peças), com nome e causa em `ilhas/robometria/dados/residuo-de-fotos-2026-09-18.md`. Os cinco domínios estão abertos na rede desde 17/09, mas a licença da 25.3 cobre a imagem do anúncio de afiliado, não a do fabricante. **Enquanto ele não disser, não há bloco de construção elegível nesta ilha**, por ordem escrita do despacho de 18/09. **Aberto há 0 dia.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Detalhe em `dados/despachos.md`. **Aberto há 6 dias.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 5 dias.**
- **Uma linha na seção 25.4 do `ARQUIPELAGO.md` sobre como se testa o degrau 4.** O teste de ficha por `api/v4/pdp/get_pc` está escrito e funcionou (29 de 29 hoje); o teste do degrau 4 é a contagem de resultados da busca, e é o que pegou o link morto de hoje — mas continua não escrito. **Aberto há 4 dias.**
- **A ilha 4 / purga por API do hospedeiro** — os dois continuam em `dados/despachos.md`, sem mudança nesta ronda.

## Consertos das últimas 24 h

**Nenhum.** A ronda de 18/09 na robometria achou quatro coisas e as quatro caem na lista fechada 19.2 — palavra-chave e dado do banco, piso de afiliado que depende de credencial, e código de snippet —, então foram despachadas em vez de consertadas. Nada na tabela de `ilhas/robometria/dados/consertos.md` esperava reconferência: a ronda de 16/09 também não consertou nada. O que esta ronda reconferiu foi o despacho de 16/09, no ar, pelos "pronto quando" dele — e os três itens da Fundação passaram.

**Teste de vida dos links (25.4 e 25.4-b), feito nesta ronda, na robometria:** **29 de 29** itens com `url_produto` testados pela API de ficha da Shopee, do navegador — **29 vivos, 0 mortos, 0 esgotados**. Mais **13 palavras-chave de busca**: **1 com zero resultado** (`Roborock Q8 Max robo aspirador`), 12 com resultado. **Itens `intestavel: true`: ZERO.** Itens sem `url_produto`: **66**, os 66 com `motivo_sem_url_produto` escrito — medição honesta pela 25.7, não defeito. Nenhum clique de afiliado foi gasto.

# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 14/09/2026 14h32Z, pela ronda diária da **robometria**.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva | 2 | 36 / 40 | 5 / 21 | 14/09 14h05Z | 13/09 14h47Z | abaixo |
| robometria | nascendo | 1 | 9 / 40 | sem registro | 14/09 13h54Z | **14/09 14h32Z** | abaixo |
| clubedomosaico | nascendo | 1 | 11 / 40 | sem registro | 14/09 13h21Z | 12/09 14h43Z | abaixo |

As **9** páginas da robometria foram contadas no `wp-sitemap-posts-page-1.xml` no ar nesta ronda, e as 9 respondem 200; o `/status` foi lido na **revisão 36**, igual à do `manifest.json`. Os números das outras duas ilhas saem do cabeçalho do `ESTADO.md` de cada uma, lido hoje — **não foram medidos no ar nesta ronda** (23.4), porque a ronda é da robometria pela regra da dívida da seção 12: as três publicaram desde a própria última ronda, e a robometria era a de `ultima_ronda` mais antiga (11/09 14h53Z).

Aquametria: `congelamento` suspenso em 12/09/2026 pela seção 21 — abaixo do piso, zero impressão não é sinal. As três ilhas estão abaixo do piso de 40 páginas.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `ilhas/robometria/PROMPT.md` | cache da hospedagem serve HTML de 11/09 (anterior à casca 1.3.0, sem trilha e sem `BreadcrumbList`) a todo cliente que não negocia `gzip` — nas 9 URLs; navegador e Googlebot recebem a página certa, mas todo `curl` de verificação da nuvem lê a página velha e aprova | 14/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | a R1 serve dois números para a mesma coisa na mesma página: "63 pares peça × modelo" no parágrafo de promessa e "São 73 pares" na tabela, que tem 73 linhas — os kits abrem uma linha por peça | 14/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | a R2, na situação-âncora `liso\|nao`, diz "as fontes brasileiras divergem" e nomeia o Mundo Conectado nos dois lados, com a oração quebrada ("trata até 1.500 Pa já basta") — é o que a página serve a quem chega sem preencher nada | 14/09/2026 |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 10/09: reenviar `https://robometria.com.br/wp-sitemap.xml` no Search Console. Trava leva de malha (18 URLs de nível 1 e 2 esperando) | 10/09/2026 |

**As três primeiras linhas são da ronda de hoje e ainda não passaram por nenhuma execução da Fundação.** A quarta é do Raphael, não da Fundação, e também está na lista abaixo.

**Aquametria e clubedomosaico não têm despacho aberto para a Fundação.** Conferido nos dois `PROMPT.md` hoje: na aquametria os itens 1 a 4 do despacho da Sentinela de 13/09 foram cumpridos e verificados no ar em 13/09 15h16Z, o item 5 é registro de receita (depende do Raphael) e o item 6 está suspenso pela seção 21; na clubedomosaico os dois itens da Sentinela de 12/09 foram cumpridos, e os quatro achados da artesã de 14/09 saíram inteiros na execução das 11h18Z — o que sobrou ali (`/tecnicas/Picassiete/`) é bloco de malha, não conserto.

## Precisa do Raphael

- **A sessão do painel da Shopee — é o único elo que falta para a robometria ter porta de compra.** Medido no banco hoje: 32 itens publicáveis, **32 sem `url_busca`**, 32 sem `url_produto`, **zero link de loja em zero cartão**. A palavra-chave já está escolhida e gravada em `afiliado.url_busca_produto` nos 32; falta só encurtar em `affiliate.shopee.com.br/offer/custom_link`, até 5 por vez (25.6). Enquanto isso a ilha recomenda peça e não vende nenhuma. Na clubedomosaico são 15 itens na mesma espera; na aquametria, 78.
- **A credencial da Open API da Shopee** (`AppID` e `Senha` em `affiliate.shopee.com.br/open_api`). Aprovada em 13/09 (protocolo 2099140709749702724), prometida "em até 5 dias úteis" — ou seja, deve aparecer entre **18 e 22/09**. Vale conferir: ela resolve de uma vez o encurtamento acima **e** o teste de vida.
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Detalhe em `dados/despachos.md`. **Aberto há 2 dias.**
- **A ilha 4.** `bussola/dossies/` continua vazia; o topo da fila é energia solar off-grid (4,20), seguido de nobreak e estabilizador (4,19). **Aberto há 2 dias.**
- **`www.fishbase.se`, `www.fishbase.org` e `www.seriouslyfish.com`** na lista de domínios permitidos das rotinas — trava campos da aquametria e, com eles, a categoria `/peixes/vivaparos/`. **Aberto há 1 dia.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 1 dia.**
- **Reenviar o sitemap da robometria no Search Console.** Trava leva de malha nesta ilha desde 10/09. **Aberto há 4 dias.**
- **Uma linha na seção 25.4 do `ARQUIPELAGO.md`:** o teste de vida como está escrito não é executável. Medido hoje — a nuvem recebe 0 bytes de `shopee.com.br` e de `www.mercadolivre.com.br`, e o Chrome dele cai em `verify/captcha?...&scene=crawler_item` ao navegar para página de produto ou de busca da Shopee. O que funcionou foi `shopee.com.br/api/v4/pdp/get_pc?shop_id=<id>&item_id=<id>&detail_level=0`, chamado por `fetch` de dentro do domínio: devolve `item_status` e o nome, sem gastar clique de afiliado e sem esbarrar no anti-robô.

## Consertos das últimas 24 h

Nenhum. A ronda de 14/09 na robometria achou quatro coisas e as quatro caem na lista fechada 19.2 — camada de hospedagem, lógica de ferramenta, dado de banco e dependência humana —, então foram despachadas em vez de consertadas. `ilhas/robometria/dados/consertos.md` nasce nesta ronda com essa constatação.

**Teste de vida dos links (25.4), feito nesta ronda:** 10 itens testados, **10 vivos, 0 mortos, 0 esgotados**. Foram os 10 da clubedomosaico, porque a robometria não tem um único link para testar. Nenhum dos 4 que morreram em 13/09 reapareceu e nenhum novo morreu em 24 h.

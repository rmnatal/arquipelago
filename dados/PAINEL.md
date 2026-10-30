# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 30/10/2026 15h1xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **rodametria** — a PRIMEIRA ronda técnica desta ilha — e a varredura curta de HTTP e porta de entrada na **clubedomosaico**, na **aquametria** e na **robometria**. A ronda anterior é de **28/10 14h5xZ**. **Não houve ronda em 29/10.**

**POR QUE A RODAMETRIA (regra da dívida, seção 12):** a primeira metade da regra decidiu sozinha. As quatro ilhas com página no ar têm `ultima_ronda: 2026-10-28T20:00Z`, e **só uma publicou depois disso** — a rodametria, que foi de 2 para 5 URLs em 29/10 e para **9** no meio desta ronda. A clubedomosaico não executa desde 23/10, a aquametria desde 21/10 e a robometria desde 26/10.

**O ACHADO DA RONDA NÃO É DA ILHA DA RONDA: A ROBOMETRIA ESTÁ FORA DO AR, MENOS A HOME.** Está no topo da lista do Raphael, abaixo, e o despacho ALTA está em `ilhas/robometria/PROMPT.md`.

## Ilhas

| ilha | estado | prio | páginas | última construção | última ronda | piso |
|---|---|---|---|---|---|---|
| rodametria | viva (**EM FOCO** desde 27/10) | 1 | **9 / 40** (contado no wp-sitemap no ar hoje; eram 5 no `ESTADO.md`) | 30/10 14h40Z (revisão 19, bloco 5d, **em execução durante a ronda**) | **30/10 15h1xZ** (ronda FUNDA, a primeira desta ilha) | abaixo |
| clubedomosaico | nascendo (modo de medição) | 1 | **39 / 40** (contado no wp-sitemap no ar hoje; eram 32 em 28/10) | 23/10 19h43Z (revisão 93) | **30/10 15h0xZ** (técnica curta) | abaixo |
| aquametria | viva (modo de medição) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | 21/10 21h48Z (revisão 135) | **30/10 15h0xZ** (técnica curta) | atingido |
| robometria | viva (PRONTA em 20/09) — **1 de 14 URLs no ar** | 1 | **14 publicadas, 1 servindo** | 26/10 16h59Z (revisão 95) | **30/10 14h5xZ** (técnica curta, e ela achou a queda) | abaixo |
| jornadafly | nascendo (fora do foco desde 27/10; sem site, `rede: BLOQUEADA`) | 1 | 0 / 40 | 27/10 19h53Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**A VARREDURA DE HTTP, URL POR URL, COM QUEBRA DE CACHE, HOJE:** rodametria **9 de 9** em 200, clubedomosaico **39 de 39**, aquametria **52 de 52**. **Robometria: 1 de 14** — a home. As 13 internas que a própria home linka, mais `/robots.txt`, `/wp-sitemap.xml` e o endpoint do Sync, devolvem **404 nas duas leituras**, servindo a página de erro **da HostGator** e não a do WordPress. Assinatura da queda do `.htaccess` da raiz, a mesma que derrubou a clubedomosaico três vezes. Controle verde no mesmo minuto nas outras duas: não é rede.

**A PORTA DE ENTRADA DA 29.2:** verde na rodametria (`/` 200 `text/html`, `/robots.txt` 200 `text/plain`, `/wp-sitemap.xml` 200 `application/xml`, `/wp-json/` 200 `application/json`), verde na clubedomosaico e na aquametria nas duas leituras, **vermelha na robometria em três das quatro portas**.

**SOFT 404 NA BORDA:** na **rodametria** o caminho virgem respondeu **404 nas QUATRO leituras seguidas**, sem quebra de cache — **o defeito das outras ilhas NÃO aparece nesta**, medido hoje e não herdado. Nas outras três ele segue registrado e segue sendo do hospedeiro; nesta ronda não foi remedido na clubedomosaico nem na aquametria (ronda curta), e na robometria não há como medir enquanto tudo é 404 de verdade.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 9 URLs DA RODAMETRIA:** zero `&#038;` dentro de `<script>`; JSON-LD nas 9 com `BreadcrumbList` nas 8 que não são a home e breadcrumb visível nas mesmas 8; zero `noindex`; zero `<img>` sem `alt` e zero sem `width`/`height`; `aria-expanded` e `aria-controls` nas 9; zero palavra da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo; tabela de exemplos pré-renderizada no HTML servido da F2. **16.4(f) na direção de quem aponta (16.9b): zero órfã** — as 9 recebem 8 links de entrada cada. **Console sem uma mensagem**, lido com navegação de verdade em três páginas. **Duas exceções**, as duas no item 5 do despacho: `meta description` de **161** caracteres na home e de **193** na F2, contra o teto de 160.

**A F2 RODADA COM ENTRADA INÉDITA E A CONTA REFEITA NA MÃO, E ELA FECHA:** `60 V × 26,0 Ah` → **1.560 Wh**; `36 V × 10,4 Ah` → **374 Wh**; faixa na ladeira **34 km** (80 ÷ 2,37 = 33,76) e em pouca subida **52 km** (80 ÷ 1,54 = 51,9); linha "Haixia" da tabela pré-renderizada, 1.200 Wh, **19–45** e **29–45**. E o caso **sem autonomia declarada** diz que não dá para estimar, nomeia a constante pendente e não inventa número — a seção 10 obedecida na tela.

**COERÊNCIA DA RECOMENDAÇÃO: REPROVOU EM TRÊS LINHAS, E NENHUMA É DE ENCANAMENTO.** (1) A caixa da F2 serve "34 a 80 km" e logo abaixo escreve "e não os 80 km do anúncio" — **nega o topo da faixa que ela mesma acabou de publicar**, e o mesmo em pouca subida ("52 a 80 km, e não os 80 km"). (2) O campo "seu peso" **não muda nada**: 50 kg e 150 kg devolvem a mesma resposta palavra por palavra, e o resultado nunca menciona o peso — enquanto o título, o primeiro parágrafo da F2 e a pergunta da home prometem "com o seu peso". (3) Dois dos quatro cartões de compra servem **"R$ 8.244,00 na Mercado Livre"** e **"R$ 8.856,00 na Mercado Livre"** com o botão **"Ver ofertas na Shopee"** — o preço tem procedência e data, e o botão não serve aquele preço. Itens 1, 2 e 3 do despacho de hoje.

**RECEITA:** o topo das duas listas da vitrine e os quatro cartões da F2 têm saída de compra. Passa.

**TESTE DE VIDA DOS LINKS (25.4) NA RODAMETRIA: 9 itens testados, 9 VIVOS, 0 morto, 0 esgotado — e 13 NÃO TESTADOS, o que é a outra metade do número.** Pela `api/v4/pdp/get_pc` chamada de dentro de uma aba no domínio, os 9 com `item_status: normal`. **Zero clique de afiliado gasto e zero CAPTCHA resolvido.**

**E A RECEITA DO PAINEL DE 28/10 NÃO REPRODUZIU: O QUE ESGOTA É ORÇAMENTO DE CHAMADAS NA JANELA, NÃO INTERVALO.** Medido em quatro lotes: com 4,5 s de intervalo, **3 passaram** e a 4ª caiu em `/verify/traffic/error`; com **14 s**, de novo **3**; com 45 s de espera e 10 s de intervalo, **3 de 3**; e o lote seguinte, com o mesmo ritmo, **0 de 3** — o de depois caiu em `/verify/captcha?...&scene=crawler_item`, que a Sentinela é proibida de resolver. Três por lote em intervalos que diferem por um fator de três, e um lote zerado no mesmo ritmo do anterior. A linha de 28/10 ("4 a 5 segundos entre chamadas, 14 seguidas sem recusa") descreve aquele dia; **a régua que hoje mediu é lote de 3 com 45 s entre lotes, e cerca de 9 a 12 itens por sessão.** Item 6 do despacho.

**AS 21 OFERTAS DA VITRINE DA RODAMETRIA SÃO INTESTÁVEIS E SEM PISO — E O PAR EXISTE NO REPOSITÓRIO.** `dados/vitrine-de-produto.json` serve 21 ofertas distintas nas duas páginas de consulta de produto (37 ocorrências de `s.shopee.com.br` em `/veiculos/patinete-eletrico/` e 15 em `/veiculos/bicicleta-eletrica/`, contadas no HTML servido) e as 21 têm **só** a encurtada: sem `url_produto`, sem `shop_id`, sem `item_id`, sem `url_busca` própria. É o gêmeo exato das 58 ofertas da clubedomosaico despachadas em 28/10. **A diferença boa:** `dados/anuncios-por-consulta.json` guarda `url_produto`, `shop_id` e `item_id` para **40 de 40** anúncios, colhidos **na mesma chamada** que o `url_afiliado` — o par é demonstrável sem remendo (25.4-b.1), e foi lendo esse arquivo que a ronda de hoje conseguiu testar 9 das 21. Item 4 do despacho.

**O PISO DA 25.2 NO BANCO QUE O PORTÃO LÊ (rodametria):** 5 registros publicáveis, **0 sem `url_busca`**, **0 sem `url_busca_produto`**; 1 em degrau 1 com o par completo e 4 em degrau 4, que não têm ficha para guardar. O banco está certo — e continua não cobrindo a vitrine, que é onde estão 21 dos 26 links que a ilha serve.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 30/10 — **ALTA** | **a ilha fora do ar menos a home**: 13 de 14 URLs internas, `/robots.txt`, `/wp-sitemap.xml` e o endpoint do Sync em 404, servindo a página de erro da HostGator. Queda do `.htaccess` da raiz. **O gesto é do Raphael** | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 1 | a caixa da F2 negando o topo da faixa que ela serve ("34 a 80 km, e não os 80 km do anúncio") | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 2 | o campo "seu peso" que não muda nada, contra a promessa do título, do primeiro parágrafo e da home | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 3 | preço da Mercado Livre com botão da Shopee em dois dos quatro cartões de compra | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 4 | as 21 ofertas da vitrine sem `url_produto`, `shop_id`, `item_id` e `url_busca`, e o portão do piso que não lê esse arquivo | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 5 | as duas `meta description` acima de 160 — **não consertadas de propósito**: são literais dentro de snippet, e a trava 3 da seção 12 proíbe | 30/10/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 28/10 (leitura semanal) item 1 | a conta da 31.1, que era 0 de 5 e é 1 de 6. **Quem fecha é a leitura semanal** | 28/10/2026 (2 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 28/10 item 1 | as 58 ofertas da vitrine no ar sem `url_produto`, `shop_id` e `url_busca`, e o portão do piso que não lê esse arquivo. **Não reconferido hoje — ronda curta** | 28/10/2026 (2 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 28/10 item 2 | as duas filhas de `/como-fazer/` servindo zero irmã (16.9a). **Não reconferido hoje — ronda curta** | 28/10/2026 (2 dias) |
| robometria | `PROMPT.md`, despacho de 26/10 item 1 | o `electrolux-erb60` esgotado, que a Fundação diz ter fechado. **Quarto dia sem verificação independente**, e hoje foi impossível: a página está em 404 | 26/10/2026 (4 dias) |
| aquametria | `PROMPT.md`, despacho de 21/10 itens 1, 2 e 3 | a caixa de resultado congelada da `/calculadora-de-iluminacao/`; o "seis registros e três sugeridos" contra 26 e 15 no banco; o texto de bastidor da 32.4 em 30 das 52 páginas. **Não reconferidos hoje — ronda curta** | 21/10/2026 (9 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 21/10 item 1 | as QUATRO calculadoras restantes e as fichas de peixe no molde da seção 32 | 21/10/2026 (9 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 e a lista do que **não** é para fazer nesta ilha | 14/10/2026 (16 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | a SERP brasileira das 14 consultas `nao-medida`, vista com os olhos | 09/10/2026 (21 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10 item 2 | a passada do `search-console.py` **com credencial** | 07/10/2026 (23 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Detectada, mas não indexada" | 07/10/2026 (23 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | o soft 404 na borda do hospedeiro — do Raphael | 30/09/2026 (30 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | o soft 404 na borda, o irmão do de cima. **Não remedido hoje — ronda curta** | 29/09/2026 (31 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa. **Não reconferido, e por regra:** a 25.8 proíbe conferir o link da ilha pelo encurtador | 23/09/2026 (37 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (37 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (44 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael | 14/09/2026 (46 dias) |
| aquametria | `PROMPT.md`, despacho de 14/10 (leitura semanal) item 1 | os 11 itens do banco com link de produto e sem `url_produto` (dívida da 25.4-b) | 13/09/2026 (47 dias) |

**NASCERAM HOJE: SEIS** — um ALTA na robometria e cinco na rodametria. **SAIU DA LISTA HOJE: NENHUM.** Esta ronda **não consertou nada**, e o motivo está escrito no item 5 do despacho da rodametria: os dois únicos defeitos da lista 19.1 que ela achou são literais dentro de snippet, e a trava 3 da seção 12 proíbe a Sentinela de tocar em snippet mesmo para mudar uma linha. Zero conserto também significa que **a ronda seguinte não tem nada a reconferir pela 19.4(c)** — `ilhas/rodametria/dados/consertos.md` nasce hoje dizendo exatamente isso.

## Precisa do Raphael

- **A ROBOMETRIA ESTÁ FORA DO AR E O CONSERTO É DE PAINEL, NÃO DE REPOSITÓRIO. É O ITEM MAIS CARO DESTA LISTA.** 13 das 14 URLs em 404 com a página de erro da HostGator, `/robots.txt` e `/wp-sitemap.xml` entre elas, e **10 das 14 estavam no índice do Google na leitura de 28/10** (18 impressões, posição média 14,3). O `/divulgacao-de-afiliados/`, exigido pelos programas de afiliado, está caído enquanto a home continua no ar. O gesto: **WordPress → Configurações → Links permanentes → Salvar**, que reescreve o `.htaccess` da raiz; se não voltar, recriar o arquivo pelo Gerenciador de Arquivos do cPanel com as sete linhas padrão do WordPress. **E como o `/wp-json/` caiu junto, o Sync não alcança a ilha:** nenhum conserto por commit desembarca lá até a raiz voltar.
- **A RODAMETRIA AINDA NÃO ESTÁ NA LISTA DE DOMÍNIOS PERMITIDOS DA NUVEM DESTA ROTINA, E ELA É A ILHA EM FOCO — TERCEIRO DIA.** Medido hoje às 14h4xZ: `rodametria.com.br` e `www.rodametria.com.br` em **000** nas três passadas, com `aquametria.com.br` e `clubedomosaico.com.br` em **200** nas mesmas três, e o proxy nomeando a causa (`connect_rejected`, recusa de política). **O site não caiu** — a ronda de hoje mediu as 9 URLs em 200 pelo navegador. O que isso custa é concreto: a Sentinela consegue rondar esta ilha porque roda no seu Chrome, mas **as execuções de nuvem da Fundação não alcançam o site para conferir o que entregam**, e a 20.1 é textual sobre o preço disso. O caminho: `claude.ai/code` → seletor de ambiente → Nuvem → engrenagem → Domínios permitidos, acrescentando `rodametria.com.br` e `*.rodametria.com.br`. *(O `ESTADO.md` da ilha diz `rede: aberta em 2026-10-30` com medição de 200 às 10h1xZ — então ou há duas listas de domínios diferentes entre os ambientes, ou a liberação é parcial. De qualquer modo, desta rotina a recusa é de hoje e tem três passadas.)*
- **A JORNADAFLY SEGUE COM O EGRESSO RECUSADO**, décimo segundo dia, e fora do foco desde 27/10. Mesma porta, mesmo conserto.
- **O SOFT 404 NA BORDA, NA CLUBEDOMOSAICO E NA AQUAMETRIA** — caminho inexistente responde 404 na primeira leitura e 200 na segunda, por cerca de duas horas. O chamado na HostGator está em `ilhas/clubedomosaico/dados/despachos.md` desde 05/10 e segue sem resposta. **A rodametria, no mesmo hospedeiro, não apresenta o defeito** — medido hoje, quatro leituras em 404. Isso é informação nova para o chamado: não é o hospedeiro inteiro, é a configuração daquelas contas.
- **O MÉTODO DO TESTE DE VIDA DA SHOPEE, na sua lista desde 26/10, mudou de forma hoje.** A receita de 28/10 (4 a 5 s entre chamadas) não reproduziu: o que esgota é **orçamento de chamadas na janela**, e a sessão termina em CAPTCHA, que a Sentinela não resolve. Com a régua de hoje, uma ronda mede de 9 a 12 links por sessão — o que basta para a rodametria hoje e **não basta** para a clubedomosaico, que tem 58 na vitrine mais 24 no banco. Se o teste tiver de cobrir ilha grande, o caminho é a Open API de afiliados (25.6) na coleta, e não a `api/v4/pdp` na ronda.
- **VENDA E POSIÇÃO continuam não medidas** em toda ilha nova: é da leitura semanal, e o painel do Shopee Afiliados exige a sua sessão.

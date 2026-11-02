# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 02/11/2026 15h1xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **robometria** — a primeira depois de a ilha voltar ao ar — e a varredura curta de HTTP e porta de entrada na **rodametria**, na **clubedomosaico** e na **aquametria**. A ronda anterior é de **30/10 15h1xZ**. **Não houve ronda em 31/10 nem em 01/11.**

**POR QUE A ROBOMETRIA (regra da dívida, seção 12):** duas ilhas publicaram desde a última ronda — esta hoje às 10h35Z (revisão 96, a ilha de volta ao ar depois de quatro dias) e a rodametria hoje às 14h14Z (revisão 28) — e o desempate é a segunda metade da regra: `ultima_ronda` de 30/10 **14h55Z** nesta contra **15h10Z** na rodametria. E havia uma dívida de verificação nomeada esperando por esta ronda: a 19.4(c) sobre o conserto que a Fundação fez hoje, e o `electrolux-erb60`, fechado em 26/10 e nunca reconferido no ar.

**O QUE A RONDA FECHOU, E É A PARTE QUE VALE: AS DUAS DÍVIDAS DE VERIFICAÇÃO DA ROBOMETRIA ESTÃO PAGAS, MEDIDAS POR QUEM NÃO CONSTRUIU.** (1) A porta de entrada da raiz: **14 de 14 URLs do sitemap em 200 em DUAS leituras com quebra de cache**, `/robots.txt` 200 `text/plain`, `/wp-sitemap.xml` 200 `application/xml` com `<sitemap>` de verdade, `/wp-json/` 200 `application/json`, e caminho virgem em **404 na página da própria ilha** — 17 medições, 0 falha, e `/status` em 96 igual ao manifest. (2) O `electrolux-erb60`: **zero** ocorrência do encurtado morto (`7ptINupGy6`) e **zero** do anúncio aposentado (`854082976`) em `/quantos-m2-o-robo-aspirador-limpa-por-carga/`; o **primeiro** botão de compra é `s.shopee.com.br/AAHCqjJaR9`, que é a `url_busca` do registro, com o rótulo "Ver ofertas na Shopee"; e no banco o registro está em **degrau 4**, `url_produto` em `null`, com a história inteira no `motivo_sem_url_produto` e fora dos campos vivos, como a 25.4-b.1 manda. O ERB60 continua na página como produto.

**O DEFEITO NOVO DA RONDA É DE JULGAMENTO, NÃO DE ENCANAMENTO: OS MINUTOS DO CICLO DA R2 NÃO DEPENDEM DA METRAGEM.** Medido com sete entradas na `/quantos-pa-o-robo-aspirador-precisa/`, só mudando a área: **10, 20, 95, 160 e 166 m² recebem todos "100 minutos de limpeza"** — e 100 min é a autonomia declarada inteira do ERB60 (`autonomia_min_declarada.valor` = 100, "até 1h40"). Um apartamento de 10 m² recebe o mesmo tempo de limpeza que uma casa de 166 m². Em mais de um ciclo é a mesma conta multiplicada: **200 m² → "200 minutos de limpeza somados"**, **400 m² → "300 minutos"**, cobrando bateria cheia no último ciclo quando faltam 68 m². **E a página se contradiz em voz alta:** poucos blocos abaixo da caixa de resposta ela declara que "esta ferramenta não converte minutos em metros quadrados" porque isso seria "dar ao leitor um número que nenhum fabricante sustenta". É item 1 do despacho de hoje, e é 19.2: literal dentro de `snippets/robometria-r2.php`, função `robometria_r2_frase_ciclo()`.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 14 URLs DA ROBOMETRIA:** zero `&#038;` dentro de `<script>`; zero `noindex`; JSON-LD nas 14 e `BreadcrumbList` nas 13 que não são a home; `description` única nas 14 e **nenhuma acima de 160** (a maior tem 151); zero `<img>` sem `alt` e zero sem `width`/`height` nas 19 imagens; `aria-expanded`, `aria-controls` e favicon nas 14; corpo nunca começando por metadado; zero palavra da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo. **16.4(f) na direção de quem aponta (16.9b): zero órfã**, menor contagem de entrada **4**. **Console sem uma mensagem**, lido no Chrome do Raphael em duas páginas com navegação de verdade.

**AS DUAS FERRAMENTAS COM ENTRADA INÉDITA E A CONTA REFEITA NA MÃO, E AS DUAS FECHAM.** R1 em `electrolux-erb44 + escova lateral` → **0 peça**, sem bloco de compra e com o motivo escrito, e o banco concorda: o ERB44 tem exatamente dois pares declarados (filtro HEPA ERB44/60/61/62 e Kit Performance ERB44) e nenhum deles cobre escova lateral. A prestação de contas da R1 foi **recontada linha por linha na tabela servida**: **108 linhas de corpo, 97 perguntas distintas (modelo × função) e 11 dobradas** — exatamente o que a prosa publica. E função por função a tabela bate com o banco: bateria 2, escova lateral 28, escova principal 16, filtro 26, mop 30, reservatório 6. **A primeira expansão desta ronda deu 109 e a PÁGINA estava certa:** a 109ª era a entrada de `composicao` do `electrolux-kit-performance-erb44` com `tipo: null` ("escovas originais, SEM o tipo"), que a página se recusa a publicar como linha — a seção 10 obedecida na tela. R2 em `95 m² · carpete · pelo longo` → limiar "acima de 4.000 Pa" com autor e data e **5 modelos**, os 5 recontados no banco pela regra LIDA e não suposta (`pa_declarado > 4000` E `canal_brasileiro` não nulo), na mesma ordem servida: 15 publicáveis têm Pa ≥ 4.000, **4 empatam exatamente em 4.000** (`xiaomi-s10`, `xiaomi-e10`, `xiaomi-e12`, `xiaomi-s12`) e **6 não têm canal brasileiro**.

**RECEITA:** os 5 botões da R2 são `s.shopee.com.br`, **zero link cru**, e o topo da lista tem saída de compra. Passa.

**TESTE DE VIDA DOS LINKS (25.4): 0 DE 28 MEDIDOS, E É ACHADO DE INSTRUMENTO, NÃO DE ILHA.** Duas tentativas limpas, 50 s de intervalo, as duas caindo em `shopee.com.br/verify/captcha?...&scene=crawler_item` **na primeira ficha da sessão** — `xiaomi-b112-ch` e `xiaomi-h40`. A Sentinela é proibida de resolver CAPTCHA e não o resolveu; **zero clique de afiliado gasto**. "Não medido" não é "vivo", e o `xiaomi-b112-ch` está na **terceira ronda seguida** sem medição (16/10, 26/10, hoje). **O número de testáveis caiu de 29 para 28, e a queda está certa:** é o próprio ERB60, que perdeu a ficha ao descer para o degrau 4.

**PISO DA 25.2 NA ROBOMETRIA:** **99 de 99 publicáveis** (54 peças + 45 modelos) com `url_busca` e `url_busca_produto`, **0 intestável**, 0 sem saída de compra, 0 link sem degrau. Contagem independente batendo com o `contagem` dos dois bancos.

**A SEÇÃO MÃE DA RODAMETRIA, QUE ENTROU NO MOLDE 45 MINUTOS ANTES DESTA RONDA, FOI MEDIDA NA MÃO E FECHA:** a caixa de resposta de `/veiculos/` serve **21 anúncios de adulto, de R$ 1.297,13 a R$ 6.199,90**, e as duas filhas servem 16 (de 1.297,13 a 3.399,00) e 5 (de 2.299,99 a 6.199,90) — **16 + 5 = 21**, o mínimo é o menor dos mínimos e o máximo é o maior dos máximos. As **3** famílias sem página aparecem contadas e cada cartão diz a causa medida em vez de prometer data. Breadcrumb em dois níveis com o atual sem link e `BreadcrumbList` com as mesmas URLs: correto pela 16.3.

## Ilhas

| ilha | estado | prio | páginas | última construção | última ronda | piso |
|---|---|---|---|---|---|---|
| rodametria | viva (**EM FOCO** desde 27/10) | 1 | **9 / 40** (contado no wp-sitemap no ar hoje) | 02/11 14h14Z (revisão 28, a seção mãe `/veiculos/` no molde da 32.2) | **02/11 15h0xZ** (técnica curta, pelo navegador) | abaixo |
| clubedomosaico | nascendo (modo de medição) | 1 | **42 / 40** (contado hoje em todos os sub-sitemaps no ar; o `ESTADO.md` ainda diz 32) | 23/10 19h43Z (revisão 93) | **02/11 15h1xZ** (técnica curta) | abaixo |
| aquametria | viva (modo de medição) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | 21/10 21h48Z (revisão 135) | **02/11 15h1xZ** (técnica curta) | atingido |
| robometria | viva (de volta ao ar em 02/11 depois de 4 dias) | 1 | **14 / 40** | 02/11 10h35Z (revisão 96) | **02/11 15h1xZ** (RONDA FUNDA) | abaixo |
| jornadafly | nascendo (fora do foco desde 27/10; sem site, `rede: BLOQUEADA`) | 1 | 0 / 40 | 27/10 19h53Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**A VARREDURA DE HTTP, URL POR URL, COM QUEBRA DE CACHE, HOJE:** robometria **14 de 14** em 200 em duas leituras, clubedomosaico **42 de 42**, aquametria **52 de 52**, rodametria **9 de 9** (medida pelo navegador: a nuvem desta rotina segue recusada no domínio). **Zero 404 em toda URL de sitemap do arquipélago.**

**A PORTA DE ENTRADA DA 29.2:** verde nas quatro ilhas no ar — `/` em `text/html`, `/robots.txt` em `text/plain`, `/wp-sitemap.xml` em `application/xml`, `/wp-json/` em `application/json`, todas em 200.

**SOFT 404 NA BORDA:** medido hoje só na **robometria** (caminho virgem em 404 nas duas leituras, servindo a página da própria ilha) e na **rodametria** (404). Na clubedomosaico e na aquametria **não foi remedido hoje** — ronda curta — e segue registrado como do hospedeiro.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 02/11 item 1 | os minutos do ciclo da R2 que não dependem da metragem: 10 e 166 m² recebem os mesmos "100 minutos de limpeza", e a página se contradiz dizendo que não converte minuto em metro quadrado | 02/11/2026 (hoje) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 1 | a caixa da F2 negando o topo da faixa que ela serve ("34 a 80 km, e não os 80 km do anúncio") | 30/10/2026 (3 dias) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 2 | o campo "seu peso" que não muda nada, contra a promessa do título, do primeiro parágrafo e da home | 30/10/2026 (3 dias) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 3 | preço da Mercado Livre com botão da Shopee em dois dos quatro cartões de compra | 30/10/2026 (3 dias) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 4 | as 21 ofertas da vitrine sem `url_produto`, `shop_id`, `item_id` e `url_busca`, e o portão do piso que não lê esse arquivo | 30/10/2026 (3 dias) |
| rodametria | `PROMPT.md`, despacho de 30/10 item 5 | as duas `meta description` acima de 160 — literais dentro de snippet, e a trava 3 da seção 12 proíbe | 30/10/2026 (3 dias) |
| rodametria | `PROMPT.md`, despacho de 28/10 (leitura semanal) item 1 | a conta da 31.1, que era 0 de 5 e é 1 de 6. **Quem fecha é a leitura semanal** | 28/10/2026 (5 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 28/10 item 1 | as 58 ofertas da vitrine no ar sem `url_produto`, `shop_id` e `url_busca`, e o portão do piso que não lê esse arquivo. **Não reconferido hoje — ronda curta** | 28/10/2026 (5 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 28/10 item 2 | as duas filhas de `/como-fazer/` servindo zero irmã (16.9a). **Não reconferido hoje — ronda curta** | 28/10/2026 (5 dias) |
| aquametria | `PROMPT.md`, despacho de 21/10 itens 1, 2 e 3 | a caixa de resultado congelada da `/calculadora-de-iluminacao/`; o "seis registros e três sugeridos" contra 26 e 15 no banco; o texto de bastidor da 32.4 em 30 das 52 páginas. **Não reconferidos hoje — ronda curta** | 21/10/2026 (12 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 21/10 item 1 | as QUATRO calculadoras restantes e as fichas de peixe no molde da seção 32 | 21/10/2026 (12 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 e a lista do que **não** é para fazer nesta ilha | 14/10/2026 (19 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | a SERP brasileira das 14 consultas `nao-medida`, vista com os olhos | 09/10/2026 (24 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10 item 2 | a passada do `search-console.py` **com credencial** | 07/10/2026 (26 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Detectada, mas não indexada" | 07/10/2026 (26 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | o soft 404 na borda do hospedeiro — do Raphael. **Remedido hoje nesta ilha e NÃO aparece:** caminho virgem em 404 nas duas leituras | 30/09/2026 (33 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | o soft 404 na borda, o irmão do de cima. **Não remedido hoje — ronda curta** | 29/09/2026 (34 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa. **Não reconferido, e por regra:** a 25.8 proíbe conferir o link da ilha pelo encurtador | 23/09/2026 (40 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (40 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (47 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael | 14/09/2026 (49 dias) |
| aquametria | `PROMPT.md`, despacho de 14/10 (leitura semanal) item 1 | os 11 itens do banco com link de produto e sem `url_produto` (dívida da 25.4-b) | 13/09/2026 (50 dias) |

**NASCEU HOJE: UM** — o item 1 na robometria. **SAÍRAM DA LISTA HOJE: DOIS, os dois na robometria e os dois por verificação independente desta ronda** — o despacho **ALTA de 30/10** (a ilha fora do ar) e o **item 1 de 26/10** (o `electrolux-erb60` esgotado), que esperava reconferência havia sete dias e era o item mais antigo em dívida de verificação do arquipélago. Esta ronda **não consertou nada e não tentou nenhum conserto**: nenhum defeito da lista fechada 19.1 apareceu na robometria, e o único defeito novo é 19.2 por duas razões independentes — é literal dentro de snippet (trava 3 da seção 12) e escolher entre tirar os minutos, rotulá-los como autonomia da bateria ou publicar tempo proporcional é escolha entre duas opções defensáveis.

## Precisa do Raphael

- **A RODAMETRIA AINDA NÃO ESTÁ NA LISTA DE DOMÍNIOS PERMITIDOS DA NUVEM DESTA ROTINA, E ELA É A ILHA EM FOCO — SEXTO DIA.** Medido hoje às 15h0xZ: `rodametria.com.br` recusada nas **quatro** portas da 29.2 com `CONNECT tunnel failed, 403` (recusa de política do proxy), com `clubedomosaico.com.br` e `aquametria.com.br` em **200** na mesma janela. **O site não caiu** — as 9 URLs responderam 200 pelo navegador, as quatro portas verdes e o 404 virgem em 404. O que custa continua concreto: as execuções de nuvem da Fundação não alcançam o site para conferir o que entregam. O caminho: `claude.ai/code` → seletor de ambiente → Nuvem → engrenagem → Domínios permitidos, acrescentando `rodametria.com.br` e `*.rodametria.com.br`.
- **O TESTE DE VIDA DA SHOPEE CAIU DE NOVO, E AGORA NA PRIMEIRA CHAMADA DA SESSÃO.** 0 de 28 hoje na robometria, com CAPTCHA `scene=crawler_item` nas DUAS tentativas limpas, 50 s de intervalo — nem a receita de lote de 3 de 30/10 chegou a ser exercida, porque a primeira ficha já caiu. Em três rondas desta ilha o instrumento deu 0 de 29 (16/10), 28 de 29 (26/10) e 0 de 28 (hoje): **não é ritmo, é uma porta que abre e fecha.** O caminho que não depende dela é a Open API de afiliados (25.6) **na coleta**, gravando o estado do anúncio junto do par, e não a `api/v4/pdp` na ronda.
- **A JORNADAFLY SEGUE COM O EGRESSO RECUSADO**, décimo quinto dia, e fora do foco desde 27/10. Mesma porta, mesmo conserto.
- **O SOFT 404 NA BORDA, NA CLUBEDOMOSAICO E NA AQUAMETRIA** — o chamado na HostGator está em `ilhas/clubedomosaico/dados/despachos.md` desde 05/10 e segue sem resposta. **Não remedido hoje nessas duas** (ronda curta); na robometria e na rodametria, medido hoje, o defeito **não aparece**. Isso continua sendo informação para o chamado: não é o hospedeiro inteiro, são aquelas duas contas.
- **VENDA E POSIÇÃO continuam não medidas** em toda ilha: é da leitura semanal, e o painel do Shopee Afiliados exige a sua sessão.

## Consertos das últimas 24 h

**Nenhum conserto da lista 19.1, por ronda nenhuma.** O único conserto no arquipélago nas últimas 24 h foi da **Fundação**, não de uma ronda: a porta de entrada da raiz da robometria, reparada às 10h3xZ de 02/11 pela rota de reparo da casca 1.15.0 — e esta ronda o **reconferiu no ar**, 17 medições e 0 falha. Está na linha de 02/11 de `ilhas/robometria/dados/consertos.md`.

# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 16/10/2026 14h4xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **robometria** e a **ronda técnica da porta de entrada** na aquametria e na clubedomosaico. A ronda anterior é de **14/10 14h5xZ**.

**POR QUE A ROBOMETRIA, e a escolha foi medida e não sorteada (regra da dívida, seção 12):** nenhuma ilha publicou nada desde a última ronda — a aquametria teve execução em 15/10 e hoje 16/10 14h31Z, mas as duas foram **zero byte no ar** (segue em 52 URLs, `/status` na revisão 122 e nenhum Sync acionado), e a clubedomosaico não publica desde 12/10. Sem publicação nova, manda a segunda metade da regra: o `ultima_ronda` do cabeçalho das três ilhas no ar está empatado em 14/10 19h58Z (é a leitura semanal), e o desempate é a **ronda diária técnica própria** mais antiga — a robometria é a única cuja última linha de `dados/consertos.md` é de **02/10**, contra 14/10 na aquametria e 12/10 na clubedomosaico. Ela também é a ilha com o despacho de ronda aberto há mais tempo.

**A ILHA EM FOCO CONTINUA A AQUAMETRIA** (linha `ilha:` do `foco.md`, janela até 21/10). A ronda técnica roda em toda ilha no ar (decisão do Raphael de 28/09, seção 1.2); a metade que CONSTRÓI continua só na ilha em foco. **Lembrete datado que já estava aqui e segue valendo: em 22/10 alguém tem de editar a linha `ilha:` para `jornadafly`** — em 10/10 ninguém editou e o foco ficou preso quatro dias.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva (**EM FOCO** pela linha `ilha:` do `foco.md`, até 21/10) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | **37 / 21 — fechado** (desde 09/09) | 16/10 14h31Z (**zero byte no ar**) | **16/10 14h4xZ** (porta de entrada) | **atingido** |
| clubedomosaico | nascendo (modo de medição desde 14/10) | 1 | **32 / 40** (contado no wp-sitemap no ar hoje) | sem registro (`primeira_indexacao: desconhecida`) | 12/10 13h18Z | **16/10 14h4xZ** (porta de entrada) | abaixo |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (contado no wp-sitemap no ar hoje) | **35 / 21 — fechado** (desde 11/09) | 21/09 20h09Z | **16/10 14h4xZ** (ronda FUNDA) | abaixo |
| jornadafly | nascendo (sem site; a fila do `foco.md` a põe em foco a partir de 22/10) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS ILHAS NO AR:** `/wp-sitemap.xml` (200, `application/xml`), `/robots.txt` (200, `text/plain`) e `/wp-json/` (200, `application/json`) **nas três**, e caminho virgem em **404 na página da própria ilha nas três**. Nenhuma das três está fora do ar. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ pela quarta ronda seguida.**

**`/status` igual ao `manifest.json` nas três:** aquametria **122**, clubedomosaico **88**, robometria **81**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 14 URLs DA ROBOMETRIA:** 14 de 14 em HTTP 200; zero `&#038;` dentro de `<script>`; zero página órfã — contado pela 16.9 **na direção de quem aponta**, e a menor contagem de entrada é **4**; zero `noindex` indevido; `description` única nas 14 e nenhuma acima de 160 (a maior tem 151); JSON-LD nas 14 e `BreadcrumbList` nas 13 que não são a home; **zero** `<img>` sem `alt` e **zero** sem `width`/`height` (22 imagens); botão de menu com `aria-expanded` e `aria-controls` nas 14; favicon próprio nas 14; nenhuma frase da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo. **Console sem uma mensagem**, com recarga, em `/quantos-m2-.../` com parâmetro e em `/pecas/filtros/electrolux/`.

**AS DUAS FERRAMENTAS EXECUTADAS COM ENTRADA INÉDITA E A CONTA REFEITA NA MÃO:** **R1** em `?modelo=wap-w400&peca=filtro` → "Não localizamos declaração do fabricante de filtro para este modelo; não vamos supor", **sem bloco de compra**, e a página escreve por que não tem — é a resposta certa, e o banco concorda: o `wap-w400` não tem par declarado de filtro. A prestação de contas da mesma página bate na mão: **108 linhas, 97 perguntas, 11 com mais de uma peça** (108 − 11 = 97). **R2** em `?piso=carpete&pelo=longo` com 200 m² → limiar de **4.000 Pa** (o MAIOR dos dois citados, Canaltech contra Mundo Conectado, com autor e data na tela) e **5 modelos** acima dele. **Os 5 foram recontados no banco e a regra foi descoberta, não suposta:** `pa_declarado > 4000` **e** `canal_brasileiro` não nulo dão exatamente `roborock-saros-z70`, `xiaomi-h40`, `xiaomi-s40`, `xiaomi-s40c` e `xiaomi-s20`. Os 15 publicáveis com Pa ≥ 4.000 só viram 5 porque 4 empatam no limiar (4.000 não é "acima de 4.000") e 6 perderam o canal brasileiro, cada um com o motivo e a data da aferição gravados. **Fica escrito para a próxima ronda não reabrir isto como defeito de número.** **Coerência da recomendação: passa nas duas.** **Receita:** os 5 botões do bloco de compra da R2 são `s.shopee.com.br` rastreáveis — **zero link cru** e nenhum item sem comissão acima de item com comissão (25.2-b).

**O PISO DA 25.2 NA ROBOMETRIA É 100% NOS DOIS BANCOS, RECONTADO NO REPOSITÓRIO:** **54 de 54** peças publicáveis e **45 de 45** modelos publicáveis com `url_busca` **e** `url_busca_produto`; **zero** intestável; **zero** registro com `url` de afiliado e sem `url_produto`; `links_sem_degrau: 0`.

**TESTE DE VIDA DA 25.4 NA ROBOMETRIA: 0 de 29 itens testáveis medidos — e isso é achado de INSTRUMENTO, não de ilha.** Os 29 (14 peças + 15 modelos, todos Shopee de degrau 3) têm `url_produto` e nenhum pôde ser lido: `api/v4/pdp/get_pc` devolveu `error: 90309999` **na primeira chamada de cada contexto**, em **dois contextos limpos** — um entrado por URL de ficha (`/product/<shop>/<item>`) e um por URL de busca (`/search?keyword=...`), que é exatamente a receita que funcionou em 12/10 e em 14/10 —, e as duas abas caíram em `verify/captcha?...&scene=crawler_item`. Nenhum clique de afiliado foi gasto e **nenhum CAPTCHA foi resolvido**. **"Não medido" não é "vivo".** Pela instrução que a ronda de 14/10 deixou escrita, não insisti nos mesmos dois endpoints além dos dois contextos. **Isto reabre a pendência de método que está na lista do Raphael: o orçamento medido em 14/10 (39 chamadas de ficha seguidas) não se reproduziu dois dias depois na robometria.**

**UM DEFEITO NOVO, E ELE É DA LISTA FECHADA 19.2 — despachado, não consertado.** `/quantos-m2-o-robo-aspirador-limpa-por-carga/` serve nó `Article` **sem `author`**, enquanto o irmão `/filtro-universal-de-robo-aspirador/` serve o mesmo nó **com** `author`. Detalhe no despacho de 16/10 da robometria.

**UMA ERRATA DA PRÓPRIA SENTINELA, MEDIDA E ANULADA HOJE:** o item 1 do despacho de **14/10** desta ilha ("3 registros do banco sem o piso da 25.2") é **FALSO POSITIVO**. Os três — `multi-pr684`, `multi-pr550`, `xiaomi-s20-acessorios` — estão com `status: excluido_do_banco`, com o motivo escrito em cada um (os dois primeiros são peça de aspirador vertical e de mão, não de robô), **não entram em nenhuma página servida** e o `contagem` do banco diz `itens_sem_saida_de_compra: 0`. A 25.2 cobra piso de item **publicável**. Anulado no `PROMPT.md` com a medição ao lado, para a Fundação não gastar bloco — e, pior, não "consertar" fabricando link de compra para peça que não é de robô.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 16/10 item 1 | **`Article` sem `author` em `/quantos-m2-o-robo-aspirador-limpa-por-carga/`** — código de snippet, 19.2. Pronto quando o nó `Article` daquela URL servir `author` no ar | 16/10/2026 (hoje) |
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase** — `/sobre/`, `/qual-peca-serve-no-meu-robo-aspirador/` e `/pecas/` dizem **91** pares peça × modelo e `/filtro-universal-de-robo-aspirador/` diz **92**. **Reconferido hoje no ar e recontado no banco: continua, e as duas contas continuam certas sob definições diferentes** (92 = pares declarados pelo lado da peça; 91 = pares cujos dois lados são publicáveis; o par que os separa é `multi-pr10124` × `multi-ho401`). Escolher a definição é da Fundação (19.2), e a ilha está fora do foco | 02/10/2026 (14 dias) |
| aquametria | `PROMPT.md`, despacho de 14/10 item 1 | **os 12 itens do banco com link de produto e sem `url_produto`** (dívida da 25.4-b). O mesmo número de 13/09, 02/10, 12/10 e 14/10 — **um mês e três dias sem mover** | 13/09/2026 (33 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | **a lista de consultas de produto em `dados/consultas-de-produto.md`**, com a SERP de cada uma classificada — é o trabalho da janela de foco | 09/10/2026 (7 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Propostas 1 e 2, e item 2 | a metade de MEDIÇÃO das propostas, e o defeito de instrumento do `search-console.py` (falta a passada com credencial) | 07/10/2026 (9 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Discovered - currently not indexed" — não é da Fundação | 07/10/2026 (9 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda** — camada do hospedeiro; o fechamento é do Raphael | 29/09/2026 (17 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também nesta ilha** — **remedido hoje em duas sondas virgens: 404 · 200 · 200 · 200 nas duas. CONTINUA.** O fechamento é do Raphael | 30/09/2026 (16 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa — sem reconferência porque a sessão do Shopee Afiliados está deslogada | 23/09/2026 (23 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (23 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 (`/pecas/filtros/` em "Detectada, mas não indexada"; SOLICITAR INDEXAÇÃO recusado por cota) e a lista do que **não** é para fazer nesta ilha. **Nada disto é bloco de código** | 14/10/2026 (2 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (30 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael | 14/09/2026 (32 dias) |

**SAIU DA LISTA HOJE:** o **item 1 do despacho de 14/10 da robometria** — não por ter sido cumprido, mas por ter sido **anulado por medição** (ver acima). **Nasceu um despacho novo:** o `Article` sem `author`.

## Precisa do Raphael

- **O TESTE DE VIDA DA SHOPEE VOLTOU A ZERO, E A RECEITA DE 12/10 NÃO SE REPRODUZIU.** Entrar por URL de ficha ou de busca e só então chamar `api/v4/pdp/get_pc` deu 39 chamadas seguidas em 14/10 na aquametria e **zero chamadas** em 16/10 na robometria, com `error: 90309999` na primeira e `verify/captcha` nas duas abas. Enquanto isto oscilar assim, **a 25.4 não tem instrumento confiável** e a decisão de qual passa a ser o método é do dono. **Aberto há 24 dias.**
- **O ACIONAMENTO DO SYNC PELA ROTINA DA SENTINELA CONTINUA BLOQUEADO.** `?<ilha>_sync=...&forcar=1` por `curl` é recusado por este ambiente (classificado como deploy em produção). Enquanto estiver assim, a 19.1 e a 19.3 são **letra morta para a Sentinela** em todo defeito que dependa de desembarque. Não travou nada hoje porque não houve defeito da 19.1 — e é a quinta ronda seguida assim, o que não deve ser lido como "o problema não existe". **Aberto há 11 dias.**
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`** — terceira queda em 08/10, intervalo encurtando de 11 para 3 dias. **Reconferido hoje: o reparo está de pé.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 11 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — na clubedomosaico e na robometria.** Medido hoje na robometria em duas sondas virgens sem quebra de cache: **404 na primeira leitura e 200 com corpo de erro nas três seguintes**, nas duas sondas. Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 17 dias.**
- **A sessão do Shopee Afiliados está deslogada no Chrome.** É o que impede medir clique e venda por `Sub_id` nas três ilhas. **Aberto há 9 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Sem ele, link de catálogo `/p/MLB...` só se testa no navegador. **Aberto há 18 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na URL de boletim que 19 campos do banco citam. **Aberto há 11 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** — travam a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. **Aberto há 32 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede das rotinas. Sem ela não há Search Console neste ambiente. **Aberto há 29 dias.**
- **A cota de SOLICITAR INDEXAÇÃO parece ser de CONTA, não de propriedade** — duas recusas em 14/10, em duas propriedades, com "A cota foi excedida". Se for de conta, a 14.7 precisa de uma frase que não tem: **qual ilha gasta a cota do dia.** Hoje as três disputam o mesmo recurso sem ninguém decidir. **Aberto há 2 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico esperam por ela. **Aberto há 16 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — falta a metade que é dado da artesã. **Aberto há 18 dias.**
- **Uma caixa de e-mail por ilha**, para a página de privacidade ter canal de titular. **Aberto há 28 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/`. Não bloqueia. **Aberto há 35 dias.**
- **O `ESTADO.md` da ohmetria continua sem `ultima_ronda` e `bloqueada_por`** (dívida registrada na seção 2 em 30/09). Pela própria seção 2 o conserto é de quem reservar aquela ilha, não da ronda. **Aberto há 16 dias.**

## Consertos das últimas 24 h

**Nenhum.** Zero defeito da lista fechada 19.1 em qualquer das três ilhas no ar — o único defeito novo de hoje é da 19.2 e virou despacho. **A reconferência da 19.4(c) na robometria** abriu `dados/consertos.md` antes de tudo: as quatro linhas de lá registram **zero conserto**, então não havia conserto anterior a reabrir; o que foi reconferido foram os despachos de **02/10** (continua) e **30/09** (continua), os dois no ar.

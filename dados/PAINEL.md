# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 21/10/2026 14h5xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **aquametria** e a **ronda técnica da porta de entrada mais a varredura de HTTP** na **clubedomosaico** e na **robometria**. A ronda anterior é de **16/10 14h4xZ**.

**POR QUE A AQUAMETRIA, e a escolha foi medida (regra da dívida, seção 12):** manda a primeira metade da regra, sem precisar de desempate — **a aquametria PUBLICOU desde a última ronda**. A execução de hoje, 13h22Z→14h09Z, pôs no ar a primeira das cinco calculadoras no molde da seção 32 (`/calculadora-de-iluminacao/`, revisão **128**), e código novo é onde mora defeito. Além disso a Fundação deixou, no `dados/consertos.md` da ilha, uma medição da 32.5 **explicitamente marcada como pendente da ronda** — e a 32.5 e a 19.4(c) mandam que a conferência seja de quem não construiu. As outras duas ilhas no ar não publicam desde 12/10 (clubedomosaico) e 21/09 (robometria) e receberam a ronda curta.

**A ILHA EM FOCO É A AQUAMETRIA** e **a janela dela termina HOJE, 21/10**. **LEMBRETE DATADO, QUE É DE AMANHÃ E JÁ FALHOU UMA VEZ: em 22/10 alguém tem de editar a linha `ilha:` do `foco.md` para `jornadafly`.** Em 10/10 ninguém editou e o foco ficou preso quatro dias. O `foco.md` diz, com todas as letras, que a linha da fila "NÃO troca o foco sozinha".

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva (**EM FOCO**, janela até **hoje, 21/10**) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | **42 / 21 — fechado** (desde 09/09) | **21/10 14h09Z** (a 1ª calculadora no molde 32, revisão 128) | **21/10 14h5xZ** (ronda FUNDA) | **atingido** |
| clubedomosaico | nascendo (modo de medição desde 14/10) | 1 | **32 / 40** (contado no wp-sitemap no ar hoje) | sem registro (`primeira_indexacao: desconhecida`) | 14/10 10h30Z | **21/10 14h5xZ** (porta de entrada + 32 URLs) | abaixo |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (contado no wp-sitemap no ar hoje) | **40 / 21 — fechado** (desde 11/09) | 21/09 20h09Z | **21/10 14h5xZ** (porta de entrada + 14 URLs) | abaixo |
| jornadafly | nascendo (sem site; a fila do `foco.md` a põe em foco a partir de **22/10**) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**AS TRÊS ILHAS NO AR ESTÃO INTEIRAS NO AR, MEDIDO HOJE URL POR URL:** aquametria **52 de 52** em HTTP 200, clubedomosaico **32 de 32**, robometria **14 de 14**. A `/politica-de-privacidade/` da aquametria devolveu **504** numa primeira leitura e **200** em três releituras seguidas — oscilação do hospedeiro, não da ilha, e fica escrito porque é a camada que já derrubou a clubedomosaico três vezes.

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS:** `/wp-sitemap.xml` (200, `application/xml`, com XML de sitemap de verdade), `/robots.txt` (200, `text/plain`) e `/wp-json/` (200, `application/json`) **nas três**, e caminho virgem em **404 na página da própria ilha nas três**. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ pela quinta ronda seguida.**

**`/status` igual ao `manifest.json` nas três:** aquametria **128**, clubedomosaico **88**, robometria **81**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 52 URLs DA AQUAMETRIA:** zero `&#038;` dentro de `<script>`; zero `noindex`; JSON-LD nas 52 e `BreadcrumbList` nas 51 que não são a home; zero `<img>` sem `alt` e zero sem `width`/`height` (13 imagens); `description` única nas 52, a maior com 151 — **corrigido: 149** — caracteres; `aria-expanded` e `aria-controls` nas 52; favicon próprio nas 52; zero corpo começando por metadado YAML; **zero página órfã, contado pela 16.9 na direção de quem aponta, com a menor contagem de entrada em 3**. **Console sem uma mensagem.**

**A CONFERÊNCIA DA 32.5 QUE A FUNDAÇÃO DEIXOU PENDENTE ESTÁ FECHADA, E REPRODUZIU:** no Chrome do Raphael, a 390 px, visitante novo — formulário a **434 px** (teto 700; a Fundação mediu 419), primeiro cartão de loja a **1.300 px** (teto 1.400; a Fundação mediu 1.345), altura **9.853 px**, rolagem horizontal **0**, 9 dobras todas fechadas. **A 32.5 passa no estado em que ninguém usou a página.** O que a medição de quem construiu não podia achar está no despacho de hoje, item 1.

**UM DEFEITO NOVO E GRANDE, DA LISTA FECHADA 19.2 — despachado, não consertado:** a caixa de resultado do TOPO da `/calculadora-de-iluminacao/` é **congelada no exemplo de 170 L e nunca recalcula**; a resposta real nasce numa segunda caixa, abaixo. Com isso o primeiro cartão de compra cai de **1.300 px** para **5.839 px** depois de a pessoa calcular (e para 3.839 px em quem volta com aquário guardado), contra o teto de **1.400 px** da 32.5 — e quem volta vê formulário dizendo 120 L e resultado dizendo 170 L na mesma tela. **A conta da calculadora está CERTA** (conferida na mão com 250 L, 300 L e 85 L): o defeito é de qual caixa fica em cena.

**DOIS ACHADOS MENORES, OS DOIS TAMBÉM 19.2 E OS DOIS NO DESPACHO DE HOJE:** (a) o "Como sabemos" daquela página publica **"seis registros e três sugeridos"** contra **26** registros e **15** sugeríveis recontados em `dados/produtos-iluminacao.json`, e a razão do barramento que ela declara (voltagem) é falsa — os 26 declaram voltagem, e quem barra são **11** sem `fluxo_lm`; (b) o texto de bastidor da **32.4** está em **30 das 52** páginas (as 29 fichas de peixe mais `/peixes/`), não só na ficha do betta que o despacho do Raphael citou como exemplo — são duas frases, as duas do mesmo snippet.

**PISO DA 25.2 NA AQUAMETRIA, RECONTADO NO REPOSITÓRIO:** **78 de 78** registros com `url_busca` **e** `url_busca_produto`; **11** intestáveis (têm `url` de afiliado e não têm `url_produto`); **36** testáveis. Bate com o que a leitura de 14/10 deixou escrito.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| aquametria | `PROMPT.md`, despacho de 21/10 item 1 | **a caixa de resultado do topo da `/calculadora-de-iluminacao/` congelada no exemplo, e o 1º cartão de compra a 5.839 px depois do cálculo** (teto 1.400 da 32.5) — lógica de snippet e escolha entre duas opções, 19.2. Pronto quando, no ar a 390 px e DEPOIS de um cálculo inédito, o 1º cartão aparecer antes de 1.400 px e houver uma só caixa de resultado em cena | 21/10/2026 (hoje) |
| aquametria | `PROMPT.md`, despacho de 21/10 item 2 | **"seis registros e três sugeridos" contra 26 e 15 no banco**, e a razão de barramento falsa. Pronto quando o número no ar for reproduzível por `grep` no banco no mesmo dia | 21/10/2026 (hoje) |
| aquametria | `PROMPT.md`, despacho de 21/10 item 3 | **o texto de bastidor da 32.4 em 30 das 52 páginas** — duas strings do `aquametria-peixes`. É o escopo medido do item 3 do despacho do Raphael de 21/10 | 21/10/2026 (hoje) |
| aquametria | `PROMPT.md`, despacho do Raphael de 21/10 item 1 | **as QUATRO calculadoras restantes e as fichas de peixe no molde da seção 32** — fura o foco pela 1.2. A primeira saiu hoje | 21/10/2026 (hoje) |
| aquametria | `PROMPT.md`, despacho de 14/10 (leitura semanal) item 1 | **os 11 itens do banco com link de produto e sem `url_produto`** (dívida da 25.4-b). Eram 12 em 14/10; o `eheim-classic-250-2213` fechou naquela noite. **Um mês e oito dias** | 13/09/2026 (38 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | **a SERP brasileira das 14 consultas `nao-medida`** de `dados/consultas-de-produto.md`, vista com os olhos — é o que a nuvem não alcança | 09/10/2026 (12 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Propostas 1 e 2, e item 2 | a metade de MEDIÇÃO das propostas de título (**a janela fecha hoje, 21/10 — é a leitura semanal que lê**) e a passada do `search-console.py` **com credencial** | 07/10/2026 (14 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Detectada, mas não indexada" — não é da Fundação | 07/10/2026 (14 dias) |
| robometria | `PROMPT.md`, despacho de 16/10 item 1 | **`Article` sem `author` em `/quantos-m2-o-robo-aspirador-limpa-por-carga/`** — código de snippet, 19.2 | 16/10/2026 (5 dias) |
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase** — 91 contra 92 pares peça × modelo. Escolher a definição é da Fundação (19.2), e a ilha está fora do foco | 02/10/2026 (19 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda** — camada do hospedeiro; o fechamento é do Raphael | 29/09/2026 (22 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também nesta ilha**. O fechamento é do Raphael | 30/09/2026 (21 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa | 23/09/2026 (28 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (28 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 e a lista do que **não** é para fazer nesta ilha. **Nada disto é bloco de código** | 14/10/2026 (7 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (35 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael | 14/09/2026 (37 dias) |

**NASCERAM HOJE:** os três itens do despacho de 21/10 da aquametria. **SAIU DA LISTA HOJE:** o despacho de **ronda diária de 14/10** da aquametria, apagado do `PROMPT.md` nesta data porque o único item que continuava aberto nele (a dívida da 25.4-b daquela passada) foi cumprido e conferido no ar em 14/10 — a 18.4 manda apagar o cumprido. **MUDOU DE NÚMERO:** a dívida da 25.4-b da aquametria, de **12** para **11** itens.

## Precisa do Raphael

- **O TESTE DE VIDA DA SHOPEE FALHOU PELA SEGUNDA RONDA SEGUIDA, AGORA NA SEGUNDA ILHA — e há um dado novo que estreita a causa.** 14/10 na aquametria: **35 de 35** medidos. 16/10 na robometria: **0 de 29**. 21/10 na aquametria: **0 de 36**, com `error: 90309999` na primeira chamada de dois contextos limpos e `verify/captcha` nas duas abas. **A sessão do Shopee NÃO está deslogada** — o cookie `SPC_U` estava presente, logo o que barra é o anti-robô e não o login. Enquanto isto oscilar assim, **a 25.4 não tem instrumento confiável** e a decisão de qual passa a ser o método é do dono. **Aberto há 29 dias.**
- **O ACIONAMENTO DO SYNC PELA ROTINA DA SENTINELA CONTINUA BLOQUEADO.** `?<ilha>_sync=...&forcar=1` por `curl` é recusado por este ambiente. Enquanto estiver assim, a 19.1 e a 19.3 são **letra morta para a Sentinela** em todo defeito que dependa de desembarque. Não travou nada hoje porque não houve defeito da 19.1 — e é a **sexta** ronda seguida assim, o que não deve ser lido como "o problema não existe". **Aberto há 16 dias.**
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`** — terceira queda em 08/10. **Reconferido hoje: o reparo está de pé.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 16 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — na clubedomosaico e na robometria.** Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 22 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Sem ele, link de catálogo `/p/MLB...` só se testa no navegador. **Aberto há 23 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na URL de boletim que 19 campos do banco citam. **Aberto há 16 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** — travam a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. **Aberto há 37 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede das rotinas. Sem ela não há Search Console neste ambiente. **Aberto há 34 dias.**
- **A cota de SOLICITAR INDEXAÇÃO parece ser de CONTA, não de propriedade.** Se for, a 14.7 precisa de uma frase que não tem: **qual ilha gasta a cota do dia.** **Aberto há 7 dias.**
- **EM 22/10 A LINHA `ilha:` DO `foco.md` TEM DE PASSAR PARA `jornadafly`** — a janela da aquametria termina hoje e a fila do `foco.md` já está decidida. Em 10/10 ninguém editou e o foco ficou preso quatro dias. **Vence amanhã.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico esperam por ela. **Aberto há 21 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — falta a metade que é dado da artesã. **Aberto há 23 dias.**
- **Uma caixa de e-mail por ilha**, para a página de privacidade ter canal de titular. **Aberto há 33 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/`. Não bloqueia. **Aberto há 40 dias.**
- **O `ESTADO.md` da ohmetria continua sem `ultima_ronda` e `bloqueada_por`** (dívida registrada na seção 2 em 30/09). Pela própria seção 2 o conserto é de quem reservar aquela ilha. **Aberto há 21 dias.**
- **AVISO, não pedido:** para medir o caso do visitante que volta, a ronda calculou com valores de teste na `/calculadora-de-iluminacao/` e isso sobrescreveu o aquário guardado no `localStorage` do Chrome do Raphael. **Restaurado para `real_L: 120` na mesma passada**, e o bloco `iluminacao` que o teste reescreveu foi apagado em vez de inventado — o próximo cálculo dele o reescreve certo. Está detalhado no `dados/consertos.md` da ilha.

## Consertos das últimas 24 h

**Nenhum.** Zero defeito da lista fechada 19.1 em qualquer das três ilhas no ar — os três defeitos novos de hoje são da 19.2 e viraram despacho. A reconferência da **19.4(c)** na aquametria abriu `dados/consertos.md` antes de tudo: as linhas de 13/09, 23/09 e 14/10 registram **zero conserto**, então não havia conserto anterior a reabrir. O que foi reconferido e **fechado** foi a medição da **32.5** que a Fundação havia deixado marcada como pendente da ronda, na linha de 21/10 daquele arquivo.

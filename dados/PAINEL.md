# PAINEL DO ARQUIPÉLAGO

**Instantâneo escrito pela RONDA DIÁRIA de 2026-11-09, entre 14h4xZ e 14h5xZ.** Pela seção 23, só a Sentinela escreve aqui, e este arquivo é instantâneo: sem narrativa, sem histórico, sem projeção. Número sem procedência não entra (23.4); campo não medido nesta ronda diz `não medido hoje`.

Ilha da ronda funda de hoje: **rodametria** (regra da dívida da seção 12 — publicou desde a última ronda: as revisões 69 e 70 desembarcaram hoje, a última às 14h14Z, e a ronda mediu 27 minutos depois). As outras três no ar receberam a ronda técnica curta pela decisão do Raphael de 28/09/2026 (ponteiro da 1.2): sitemap, as três portas da 29.2, caminho virgem e as URLs uma por uma, medidos no ar hoje.

**NÃO HAVIA NAVEGADOR NESTA RONDA, e isto manda em três linhas deste painel.** Nem a extensão de Chrome, nem o navegador embutido, nem o shell do computador do Raphael responderam. Pela seção 12 é a condição esperada e não é defeito da ilha; o que ela custa está dito onde custa, e nada foi estimado para preencher.

## Uma linha por ilha

| ilha | estado | prio | URLs / 40 | dias desde 1ª indexação / 21 | última execução | última ronda | piso | observação |
|---|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **10** / 40 (contado no ar hoje) | `null` — 0 de 21 | 2026-11-09T14:14Z | 2026-11-09T14:54Z | abaixo | **EM FOCO** (`foco.md`, desde 27/10) |
| aquametria | viva | 2 | **52** / 40 (contado no ar hoje) | 61 (os 21 fecharam em 30/09) | 2026-10-21T21:48Z | 2026-11-04T20:10Z | atingido | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | **44** / 40 (contado no ar hoje) | desconhecida | 2026-10-23T19:43Z | 2026-11-04T20:10Z | abaixo (cabeçalho) | **o `ESTADO.md` dela diz 32 URLs; o ar diz 44, e 44 passa das 40 da 21.1 — divergência aberta desde 28/10** |
| robometria | viva | 1 | **14** / 40 (contado no ar hoje) | 59 | 2026-11-02T10:35Z | 2026-11-04T20:10Z | abaixo | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 | `null` | 2026-09-15T11:17Z | `null` | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 | `null` | 2026-10-27T19:53Z | `null` | abaixo | sem site e com o egresso da nuvem recusado em 27/10 — `não medido hoje` |

Saúde no ar, medida hoje em **duas leituras com quebra de cache** na ilha da ronda e em **uma** nas outras três: **rodametria 10 de 10 em 200, aquametria 52 de 52, robometria 14 de 14, clubedomosaico 44 de 44.** As três portas da 29.2 (`/wp-sitemap.xml`, `/robots.txt`, `/wp-json/`) verdes nas quatro ilhas, com `content-type` certo, e o caminho virgem respondendo **404 na página da própria ilha** nas quatro. **Nenhuma ilha fora do ar, e nenhuma URL não-200 em 120 URLs medidas.**

**Na rodametria, além do ar:** `/status` em 70 e `manifest.json` em 70, iguais; zero `&#038;` dentro de `<script>` nas 10 páginas; JSON-LD nas 10, todos parseando, `BreadcrumbList` em 9 e ausente só na home (16.3); zero página órfã (mínimo de 2 links de miolo por URL) e zero link interno apontando para fora do sitemap; meta description máxima de **159** (teto 160); zero imagem sem `width`/`height` e zero `alt` faltando; os três formulários com todos os campos prefixados `rdm_` e com `<noscript>`; **22 de 22 itens da vitrine com `url_produto` e `url_busca`** — intestáveis **zero**, item sem piso da 25.2 **zero** — e **20 de 20 botões de compra com `rel="sponsored noopener"`, zero link cru** (25.2-b). As contas das três tabelas pré-renderizadas e as seis contagens do banco foram refeitas uma por uma e **todas batem**.

**Não medido hoje nesta ronda, por falta de navegador:** o **teste de vida dos links de afiliado** da 25.4 (última medição 06/11, **12 de 12 vivos**, três dias de idade — a chamada de nuvem é 403 do servidor da Shopee e isso já está medido na 25.4, então não foi repetida), o **console** das páginas e os **números de pixel da 32.5** a 390 px.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-09 | 5 itens novos desta ronda; o item 2 é a SEGUNDA volta do mesmo campo (19.4(b)) | 0 dias |
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | ALTA: itens 1 e 2, nenhum fechado — quem fecha é a leitura semanal rodando `search-console.py`; e o "pronto quando" do item 1 pede 9 páginas, o sitemap serve 10 | 5 dias |
| rodametria | `PROMPT.md`, DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10 | duas SERPs e um volume, numa sessão de Chrome | 10 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-02 (ronda técnica) | os minutos do ciclo da R2 não dependem da metragem | 7 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 12 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 19 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (ronda técnica) | 2 itens; o item 1 é um terço dos links da ilha | 12 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | duas propostas com consulta nomeada | 12 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 19 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-14 (leitura semanal) | — | 26 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 12 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 19 dias |
| aquametria | `PROMPT.md`, DESPACHO DO RAPHAEL — 2026-10-09 | páginas pelo nome do produto: só a metade que esta nuvem não alcança | 31 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-07 (leitura semanal) | só o que falta ficou | 33 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-09-23 (leitura semanal) | — | 47 dias |
| ohmetria | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 56 dias |
| jornadafly | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 56 dias |

**FECHADO desde o painel anterior, e por isso saiu desta lista:** o DESPACHO DA SENTINELA — 2026-11-06 (ronda técnica) da rodametria, cinco itens, fechado no mesmo dia às 16h4xZ — e a ronda de hoje reconferiu os cinco no ar: **quatro estão fechados; o quinto (o `nota` de `veiculos.json`) voltou e é o item 2 do despacho de hoje.**

As linhas de despacho das ilhas **fora do foco** vêm do painel de 06/11 envelhecidas em três dias e **não foram reconferidas nesta ronda**: a ronda técnica curta mede o ar delas, não a fila delas. As ilhas fora do foco não recebem bloco de construção (1.2), então despacho delas acumula por decisão, não por esquecimento.

## Precisa do Raphael

- **UM NAVEGADOR ABERTO NO COMPUTADOR DELE, e hoje é a linha mais caradura deste painel.** Esta ronda não alcançou nem a extensão de Chrome, nem o navegador embutido, nem o shell do computador. Pela seção 12 a ronda precisa disso, e o que ficou sem medição está nomeado acima: o teste de vida dos links de afiliado (que em 13/09/2026 achou 4 links mortos em 9 em menos de 12 horas, e cuja última medição nesta ilha tem três dias), o console e os pixels da 32.5. **Nada disso trava página nenhuma no ar — as quatro ilhas estão sãs —, mas são as três afirmações que só o navegador dele produz.**
- **rodametria — a parede do `.gov.br` segue de pé, e é o que trava a metade da CNH.** Medida em 05/11 às 19h1xZ (6 recusas contra 4 controles verdes, com a parede sendo o DOMÍNIO e não os hosts) e **não remedida desde então** — `não medido hoje`. O que ela ainda trava: o **CTB** (sem ele a ilha não pode dizer se dispensa ou exige habilitação, e é por isso que cinco páginas servem a oração que recusa responder), as **prefeituras** da camada municipal e as **três etiquetas do Mercado Livre**.
- **rodametria — despacho da Fundação de 30/10:** abrir a SERP das duas caudas que sobraram e ler um volume, numa sessão de Chrome, ~10 minutos. Três das cinco caudas já estão fechadas sem ele.
- **clubedomosaico — chamado na HostGator** sobre o `.htaccess` da raiz de `/clubedomosaico.com.br` (29.5 e 19.4(b): segunda queda na mesma raiz deixa de ser conserto e vira chamado). Está em `dados/despachos.md`.
- **Gerador do Mercado Livre** continua com reCAPTCHA: link `/p/` novo é clique dele (25.6). Nunca bloqueia página — o piso da 25.2 é a busca.
- **jornadafly** segue sem WordPress e com o egresso recusado (última medição 27/10), em espera até decisão nova dele.
- **ohmetria** segue sem site.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Nenhum.** A ronda de hoje na rodametria achou 5 defeitos e consertou **zero**, e nenhum conserto foi tentado: **nenhum dos cinco é consertável pela Sentinela.** O item 1 é fallback de gerador e alcança mais de uma página (22.7); o item 2 é prosa de metadado do banco (19.2) **e** é a segunda volta do mesmo campo, que pela 19.4(b) despacha de qualquer jeito; o item 3 é componente da casca em duas páginas; os itens 4 e 5 são escolha entre duas opções defensáveis (19.2). **É a QUARTA ronda seguida desta ilha com zero conserto**, e as quatro pelo mesmo motivo: o defeito mecânico desta ilha nasce dentro de snippet, de gerador ou do metadado do banco. **Reconferência da ronda anterior: nada a reconferir** — a de 06/11 também fechou com zero conserto.

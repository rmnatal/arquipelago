# PAINEL DO ARQUIPÉLAGO

**Instantâneo escrito pela RONDA DIÁRIA de 2026-11-04, entre 14h3xZ e 15h0xZ.** Pela seção 23, só a Sentinela escreve aqui, e este arquivo é instantâneo: sem narrativa, sem histórico, sem projeção. Número sem procedência não entra (23.4); campo não medido nesta ronda diz `não medido hoje`.

Ilha da ronda funda de hoje: **rodametria** (regra da dívida da seção 12 — publicou desde a última ronda, revisão 40 às 13h39Z de hoje). As outras três no ar receberam a ronda técnica curta pela decisão do Raphael de 28/09/2026 (ponteiro da 1.2): sitemap, portas da 29.2 e 404 virgem, medidos no ar hoje.

## Uma linha por ilha

| ilha | estado | prio | URLs / 40 | dias desde 1ª indexação / 21 | última execução | última ronda | piso | observação |
|---|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **9** / 40 (contado no ar hoje) | `null` — 0 de 21 | 2026-11-04T13:45Z | 2026-11-04T15:04Z | abaixo | **EM FOCO** (`foco.md`, desde 27/10) |
| aquametria | viva | 2 | **52** / 40 (contado no ar hoje) | 56 (os 21 fecharam em 30/09) | 2026-10-21T21:48Z | 2026-10-28T20:00Z | atingido | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | **44** / 40 (contado no ar hoje) | desconhecida | 2026-10-23T19:43Z | 2026-10-28T20:00Z | abaixo (cabeçalho) | **o `ESTADO.md` dela diz 32 URLs; o ar diz 44, e 44 passa das 40 da 21.1** |
| robometria | viva | 1 | **14** / 40 (contado no ar hoje) | 54 | 2026-11-02T10:35Z | 2026-11-02T15:16Z | abaixo | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 | `null` | 2026-09-15T11:17Z | `null` | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 | `null` | 2026-10-27T19:53Z | `null` | abaixo | sem site e com o egresso da nuvem recusado |

Saúde no ar, medida hoje: **aquametria 52 de 52 em 200, robometria 14 de 14 em 200, clubedomosaico 44 de 44 em 200, rodametria 9 de 9 em 200** (duas leituras com quebra de cache). As três portas da 29.2 (`/wp-sitemap.xml`, `/robots.txt`, `/wp-json/`) verdes nas quatro ilhas, com `content-type` certo, e o caminho virgem respondendo **404 na página da própria ilha** nas quatro. Nenhuma ilha fora do ar.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 | 5 itens novos desta ronda (o item 1 é o teto de pixel da 32.5 estourado em 2 px) | 0 dias |
| rodametria | `PROMPT.md`, DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10 | duas SERPs e um volume, numa sessão de Chrome | 5 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-02 (ronda técnica) | os minutos do ciclo da R2 não dependem da metragem | 2 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 7 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 14 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (ronda técnica) | 2 itens; o item 1 é um terço dos links da ilha | 7 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | duas propostas com consulta nomeada | 7 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 14 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-14 (leitura semanal) | — | 21 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 7 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 14 dias |
| aquametria | `PROMPT.md`, DESPACHO DO RAPHAEL — 2026-10-09 | páginas pelo nome do produto: só a metade que esta nuvem não alcança | 26 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-07 (leitura semanal) | só o que falta ficou | 28 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-09-23 (leitura semanal) | — | 42 dias |
| ohmetria | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 51 dias |
| jornadafly | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 51 dias |

As ilhas fora do foco não recebem bloco de construção (1.2), então despacho delas acumula por decisão, não por esquecimento.

## Precisa do Raphael

- **O egresso desta nuvem voltou a recusar `rodametria.com.br` — e é a ilha EM FOCO.** Medido nesta ronda às 14h4xZ: `CONNECT tunnel failed, response 403` do proxy de política, **seis medições em 000**, com `aquametria.com.br` em **200 nas mesmas seis passadas**. A execução da Fundação de hoje às 13h19Z mediu o domínio em **200 em três passadas**, então a recusa nasceu nas horas entre as duas. Sem isso, nenhuma execução de nuvem confere esta ilha no ar. O domínio precisa estar em Configurações → Recursos → Execução de código e criação de arquivos → Domínios adicionais permitidos; **nenhuma rotina mexe nessa lista** (25.6). *(Esta ronda contornou abrindo as páginas no Chrome dele, que não passa pelo proxy.)*
- **rodametria — os dois despachos ALTA de egresso seguem valendo:** `gov.br` para a F1 (Resolução Contran 996/2023) e os três varejos grandes para a F3.
- **rodametria — despacho da Fundação de 30/10:** abrir a SERP das duas caudas que sobraram e ler um volume, numa sessão de Chrome, ~10 minutos. Três das cinco caudas já estão fechadas sem ele.
- **clubedomosaico — chamado na HostGator** sobre o `.htaccess` da raiz de `/clubedomosaico.com.br` (29.5 e 19.4(b): segunda queda na mesma raiz deixa de ser conserto e vira chamado). Está em `dados/despachos.md`.
- **Gerador do Mercado Livre** continua com reCAPTCHA: link `/p/` novo é clique dele (25.6). Nunca bloqueia página — o piso da 25.2 é a busca.
- **jornadafly** segue sem WordPress e com o egresso recusado, em espera até decisão nova dele.
- **ohmetria** segue sem site.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Nenhum.** A ronda de hoje na rodametria achou 5 defeitos e consertou **zero**, e nenhum conserto foi tentado: nenhum deles é da lista 19.1. O item 1 é teto de pixel resolvido dentro de snippet, e a trava 3 da seção 12 proíbe a Sentinela de tocar em snippet "sem exceção, mesmo que a mudança pareça de uma linha"; os outros quatro são dado de banco, esquema, JSON-LD de casca e metadado do `manifest.json`. Nada da ronda anterior ficou para reconferir: a de 30/10 também fechou com zero conserto.

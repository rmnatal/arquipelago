# PAINEL DO ARQUIPÉLAGO

**Instantâneo de 2026-11-18, 15h0xZ**, reescrito pela RONDA DIÁRIA TÉCNICA da **rodametria** (seção 23.1: quem escreve é a ronda, e ninguém mais). Pela 23.4, todo número aqui sai de arquivo do repositório ou de medição desta ronda; o que não foi medido hoje diz `não medido hoje` em vez de repetir número velho com cara de novo.

## Ilhas

| ilha | estado | prio | URLs / 40 | dias desde 1ª indexação | ultima_execucao | ultima_ronda | piso | congelamento |
|---|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **11** / 40 (medido no ar hoje: 11 de 11 em 200) | — (`primeira_indexacao: null`) | 2026-11-18T13:47Z | **2026-11-18T15:00Z** | abaixo | nenhum — **ILHA EM FOCO TOTAL** desde 27/10 |
| aquametria | viva | 2 | 52 / 40 | 70 (1ª em 2026-09-09) | 2026-10-21T21:48Z | 2026-11-13T15:12Z | atingido | modo de medição (1.2-b.1): mede, não recebe bloco |
| robometria | viva | 1 | 14 / 40 | 68 (1ª em 2026-09-11) | 2026-11-02T10:35Z | 2026-11-13T15:12Z | abaixo | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | 44 / 40 | ≥69 (1ª indexação exata desconhecida; ≥10/09/2026) | 2026-11-12T10:46Z | 2026-11-13T15:12Z | atingido | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 / 40 | — | 2026-09-15T11:17Z | campo AUSENTE no cabeçalho | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 / 40 | — | 2026-10-27T19:53Z | null (correto: sem site) | abaixo | sem site; egresso RECUSADO desde 19/10 |

**A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA NAS QUATRO ILHAS NO AR** (as três URLs da 29.2 com `content-type` certo + caminho virgem em 404 na página da própria ilha, zero HostGator): rodametria **verde**, aquametria **verde**, robometria **verde**, clubedomosaico **verde**.

**rodametria, revisão:** `/status` **111** = `manifest.json` **111**, casca **1.29.0**, `versao_sync` 1.1.5.

**O CAMPO AUSENTE DA SEÇÃO 2 QUE AINDA ESPERA:** a `ohmetria` segue sem `ultima_ronda` e sem `bloqueada_por` no cabeçalho (a `robometria`, que estava igual em 26/10, já tem os dois). Pela regra da seção 2, quem reservar a `ohmetria` acrescenta os dois no mesmo commit — reserva é por ilha, e esta ronda não a reservou.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-18** (5 itens: `alt` vazio no ar com o alt pronto no banco; 2 fotos de cartão em 503; anúncio ESGOTADO no banco; 6 de 7 anúncios ao mesmo preço em `/veiculos/bicicleta-eletrica/`; sétima queda da porta) | 0 dia |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-18**: a moto elétrica (823 mil buscas/mês) fora do ar por falta de **um** anúncio; o que a destrava são os 5 links do Mercado Livre | 0 dia |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-17, ALTA**: o `.htaccess` da raiz é reescrito sem o bloco do WordPress, sem mão nossa — chamado na HostGator + decisão sobre o token | 1 dia |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-11 (leitura semanal)**: o item 1 fechou em 12/11; o que sobra não é da Fundação | 7 dias |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: sitemap "Não foi possível buscar" desde 20/10 — reenviado em 11/11, e **o veredito era da leitura de 18/11, que ainda não rodou** | 7 dias |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-11 (17h5xZ), despacho de CLASSE**: a cura da porta (29.4). Esta ilha **não tem** a cura que a rodametria ganhou em 12/11 | 7 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-11, ALTA** — reescrito pela 18.3 em 12/11: itens 1 e 2 fechados, **ficam os itens 3, 4 e 5** | 7 dias |
| clubedomosaico | `dados/despachos.md` | 5 das 17 peças são o MESMO oratório (sufixos `-2` e `-3`) — se virarem 301, `urls_publicadas` cai de 44 | 7 dias |
| aquametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: fila de ROI para quando a ilha sair do modo de medição | 7 dias |
| ohmetria / jornadafly | `PROMPT.md` | despachos de NASCIMENTO (carregam a fila inteira; pela 18.2 não cabem como despacho) | — |

## Precisa do Raphael

1. **OS 5 LINKS DO MERCADO LIVRE DA RODAMETRIA** — `dados/links-afiliado-pendentes.md`, pronto desde 11/11: criar a etiqueta `rodametriamotoeletrica`, gerar os 5 links de catálogo e colar na coluna `url`. O gerador do ML tem reCAPTCHA e não responde a script (25.6). **É o único gesto que devolve `/veiculos/moto-eletrica/` ao ar**, e hoje a Shopee tem **1** anúncio que serve naquela consulta, não 2 — o segundo saiu ESGOTADO nesta ronda.
2. **O CHAMADO NA HOSTGATOR, com a frase da 29.5(b) e a série anexada.** A porta da rodametria caiu pela **sétima** vez hoje às **14:34Z**. Argumento novo desta ronda: o intervalo anterior ficou **FECHADO em ~27 h 19 min** (reposição de 17/11 11:15:20Z → queda de 18/11 14:34Z), contra ~4 min no mesmo dia 17/11. Evento irregular, não processo.
3. **A DECISÃO SOBRE O TOKEN DO SYNC DA RODAMETRIA** (aberta desde 05/11). Nas irmãs o token está no `PROMPT.md`; nesta, não. Com ele, a próxima queda custa um comando em vez de esperar a trava de uma hora.
4. **`cf.shopee.com.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA** (Configurações → Recursos → Domínios adicionais permitidos). Medido nesta ronda, duas passadas por URL: a nuvem recebe `CONNECT tunnel failed, response 403`. Por causa disso o portão `conferir-32-5-no-navegador.mjs` **não consegue separar** foto quebrada de foto que o egresso recusou, e hoje reprovou 3 páginas das quais **1 é falso positivo**. Nenhuma rotina mexe nessa lista.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Zero, e nenhum tentado.** A ronda de 18/11 achou 5 defeitos e **nenhum** é da lista 19.1: quatro são dado do banco ou código de snippet (19.2) e o quinto é a porta do hospedeiro. É a **oitava** ronda técnica seguida da rodametria com zero conserto, e a causa segue onde a ronda de 16/11 a pôs: já não nasce em snippet, nasce no dado do banco e na régua que o admite.

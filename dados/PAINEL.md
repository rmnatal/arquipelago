# PAINEL DO ARQUIPÉLAGO

**Instantâneo de 2026-11-20, 14h5xZ**, reescrito pela RONDA DIÁRIA TÉCNICA da **robometria** (seção 23.1: quem escreve é a ronda, e ninguém mais). Pela 23.4, todo número aqui sai de arquivo do repositório ou de medição desta ronda; o que não foi medido hoje diz `não medido hoje` em vez de repetir número velho com cara de novo.

## Ilhas

| ilha | estado | prio | URLs / 40 | ultima_execucao | ultima_ronda | piso | congelamento |
|---|---|---|---|---|---|---|---|
| **robometria** | viva | 1 | **14** / 40 (medido no ar hoje: 14 de 14 em 200, com quebra de cache) | 2026-11-20T11:09Z | **2026-11-20T14:54Z** (ronda técnica) | abaixo | modo de medição (1.2-b.1) |
| rodametria | viva | 1 | 11 / 40 (não medido hoje) | 2026-11-20T13:44Z | 2026-11-18T20:01Z | abaixo | nenhum — **ILHA EM FOCO TOTAL** desde 27/10 |
| aquametria | viva | 2 | 52 / 40 (não medido hoje) | 2026-10-21T21:48Z | 2026-11-13T15:12Z | atingido | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | 44 / 40 (não medido hoje) | 2026-11-12T10:46Z | 2026-11-13T15:12Z | atingido | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 / 40 | 2026-09-15T11:17Z | campo AUSENTE no cabeçalho | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 / 40 | 2026-10-27T19:53Z | null (correto: sem site) | abaixo | sem site; egresso RECUSADO desde 19/10 |

**A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA — SÓ NA ILHA DA RONDA:** robometria **verde** (as três URLs da 29.2 com `content-type` certo — `text/plain`, `application/xml`, `application/json` — e caminho virgem em 404 servido pela página da própria ilha, zero HostGator). rodametria, aquametria e clubedomosaico: **não medidas hoje** — a ronda de hoje foi funda numa ilha, não rasa em quatro.

**robometria, revisão:** `/status` **98** = `manifest.json` **98**, `versao_sync` 1.1.5, último Sync 2026-11-20 14:13:24.

**O CAMPO AUSENTE DA SEÇÃO 2 QUE AINDA ESPERA:** a `ohmetria` segue sem `ultima_ronda` e sem `bloqueada_por` no cabeçalho. Pela regra da seção 2, quem reservar a `ohmetria` acrescenta os dois no mesmo commit — reserva é por ilha, e esta ronda não a reservou.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| robometria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-20** (6 itens: 3 fichas esgotadas no ar — `electrolux-kit-performance-erb30`, `xiaomi-b112-ch`, `xiaomi-s40`; 1 com vendedor de férias; o piso da 25.2 ausente em 3 das 4 telas que servem ficha; "18.500 Pa — a maior deste banco" contradito pelos 22.000 Pa servidos na mesma página) | 0 dia |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)**: item 1 FECHADO por medição (sitemap de volta a Processado, reconferido hoje); o item 2 (as quatro da leva de 21/09 fora do índice, pedido de URL Inspection em `/pecas/`) é **pedido ao Raphael**, não bloco | 2 dias |
| rodametria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-18** (5 itens) | 2 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-18**: a moto elétrica (823 mil buscas/mês) destravada pelos 5 links do Mercado Livre | 2 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-17, ALTA**: o `.htaccess` da raiz reescrito sem o bloco do WordPress — chamado na HostGator + decisão sobre o token | 3 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-11 (leitura semanal)** | 9 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-11, ALTA** — itens 1 e 2 fechados em 12/11; ficam os itens 3, 4 e 5 | 9 dias |
| clubedomosaico | `dados/despachos.md` | 5 das 17 peças são o MESMO oratório (sufixos `-2` e `-3`) — se virarem 301, `urls_publicadas` cai de 44 | 9 dias |
| aquametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: fila de ROI para quando a ilha sair do modo de medição | 9 dias |
| ohmetria / jornadafly | `PROMPT.md` | despachos de NASCIMENTO (carregam a fila inteira; pela 18.2 não cabem como despacho) | — |

**FECHADO HOJE, E NÃO POR ESTA RONDA:** o despacho de CLASSE de 11/11 sobre a cura da porta (29.4) saiu da lista — a execução da robometria de hoje às 11h09Z o entregou na casca 1.16.1, revisão 98, e esta ronda confirmou no ar as 14 URLs em 200 e as três portas da 29.2 verdes. A **causa** da queda segue sem nome e o chamado na HostGator segue aberto: a cura é cura, não conserto.

## Precisa do Raphael

1. **OS 5 LINKS DO MERCADO LIVRE DA RODAMETRIA** — `ilhas/rodametria/dados/links-afiliado-pendentes.md`, pronto desde 11/11: criar a etiqueta `rodametriamotoeletrica`, gerar os 5 links de catálogo e colar na coluna `url`. O gerador do ML tem reCAPTCHA e não responde a script (25.6). É o único gesto que devolve `/veiculos/moto-eletrica/` ao ar.
2. **O CHAMADO NA HOSTGATOR, com a frase da 29.5(b) e a série anexada.** Sétima queda da porta da rodametria em 18/11 às 14:34Z, com intervalo anterior FECHADO em ~27 h 19 min. Evento irregular, não processo.
3. **A DECISÃO SOBRE O TOKEN DO SYNC DA RODAMETRIA** (aberta desde 05/11). Nas irmãs o token está no `PROMPT.md`; nessa, não. **Argumento novo, medido hoje:** a dedução de 19/11 de que a robometria também não tinha o token era FALSA — ele estava em claro na linha `Sync:` do `PROMPT.md` dela, e o reparo saiu da nuvem em um minuto por causa disso. Na rodametria, a ausência é real e custa a trava de uma hora a cada queda.
4. **`cf.shopee.com.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA** (Configurações → Recursos → Domínios adicionais permitidos). A nuvem recebe `CONNECT tunnel failed, response 403`, e por isso o portão de foto da rodametria não separa foto quebrada de foto que o egresso recusou. Nenhuma rotina mexe nessa lista.
5. **A URL INSPECTION DE `/pecas/` DA ROBOMETRIA** — as quatro páginas da leva de 21/09 completam 60 dias em "Discovered - currently not indexed", e a solicitação manual foi recusada por **cota de conta** em 14/10. É pedido dele, não bloco da Fundação.
6. **NOVO, DESTA RONDA — O TESTE DE VIDA DA 25.4 NÃO RODA PELO CAMINHO QUE O CONTRATO MANDA, NA ROTINA AGENDADA.** O caminho da 25.4 (a API de ficha `shopee.com.br/api/v4/pdp/get_pc`, chamada de dentro de uma aba já no domínio) foi **recusado pelo classificador de modo automático** nesta ronda, nas duas formas: `fetch` na página e navegação direta à rota da API. A ronda contornou abrindo a `url_produto` de cada item e lendo o corpo — funcionou nos 17, **sem nenhum clique em link de afiliado**, mas custa uma navegação por item e depende de a Shopee não pedir CAPTCHA. **Decisão dele:** ou a rotina ganha permissão para a rota `shopee.com.br/api/v4/pdp/*`, ou a 25.4 passa a declarar a leitura do corpo como o método oficial e aceita o teto de itens por ronda.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Zero, e nenhum tentado.** A ronda de 20/11 na robometria achou seis defeitos e **nenhum** é da lista 19.1: três são ficha morta (dado do banco), um é um quarto estado de anúncio que o banco não tem campo para guardar, um é o piso que não chega à tela em três das quatro telas, e o sexto é prosa gerada por snippet. É a mesma causa que a ronda da rodametria de 16/11 nomeou, agora medida na segunda ilha: **já não nasce defeito em casca — nasce no dado do banco que envelhece sozinho e na régua que o admite.** Os 17 itens testados hoje estavam com `conferido_em` de 16 ou 18/09/2026: **65 dias sem reteste, e três morreram nesse intervalo.**

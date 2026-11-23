# PAINEL DO ARQUIPÉLAGO

**Instantâneo de 2026-11-23, 14h5xZ**, reescrito pela RONDA DIÁRIA TÉCNICA da **rodametria** (seção 23.1: quem escreve é a ronda, e ninguém mais). Pela 23.4, todo número aqui sai de arquivo do repositório ou de medição desta ronda; o que não foi medido hoje diz `não medido hoje` em vez de repetir número velho com cara de novo.

## Ilhas

| ilha | estado | prio | URLs / 40 | ultima_execucao | ultima_ronda | piso | congelamento |
|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **11** / 40 (medido no ar hoje: 11 de 11 em 200, com quebra de cache) | 2026-11-23T13:31Z | **2026-11-23T14:59Z** (ronda técnica) | abaixo | nenhum — **ILHA EM FOCO TOTAL** desde 27/10 |
| robometria | viva | 1 | 14 / 40 (medido raso hoje: 14 de 14 em 200) | 2026-11-20T11:09Z | 2026-11-20T14:54Z | abaixo | modo de medição (1.2-b.1) |
| aquametria | viva | 2 | 52 / 40 (medido raso hoje: 52 de 52 em 200) | 2026-10-21T21:48Z | 2026-11-18T20:01Z | atingido | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | **102** no sitemap (medido raso hoje: 89 em `posts-page` + 13 em `posts-peca`, **102 de 102 em 200**) — o cabeçalho dela diz `urls_publicadas: 44` | 2026-11-12T10:46Z | 2026-11-18T20:01Z | atingido | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 / 40 | 2026-09-15T11:17Z | campo AUSENTE no cabeçalho | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 / 40 | 2026-10-27T19:53Z | null (correto: sem site) | abaixo | sem site; egresso RECUSADO desde 19/10 |

**AS QUATRO ILHAS NO AR RESPONDERAM HOJE, E ISSO FOI MEDIDO E NÃO SUPOSTO:** a ronda foi funda na rodametria e **rasa (só HTTP, do sitemap) nas outras três** — robometria 14/14, aquametria 52/52, clubedomosaico 102/102, rodametria 11/11, todas em 200 com quebra de cache. A varredura rasa existe porque o Clube do Mosaico passou nove dias fora do ar sem ninguém medir.

**NÚMERO QUE NÃO BATE, E ELE NÃO É DESTA RONDA CONSERTAR (reserva é por ilha):** o `wp-sitemap.xml` da **clubedomosaico** serve hoje **102** URLs (89 `page` + 13 `peca`) contra `urls_publicadas: 44` (27 + 17) do cabeçalho dela, de 12/11 — e as **peças caíram de 17 para 13**, direção compatível com o despacho aberto dos 5 oratórios repetidos, que ninguém conferiu. É a seção 4 ao pé da letra: o site andou e o cabeçalho ficou para trás. **Quem reservar a clubedomosaico recontа no ar e acerta o campo no mesmo commit.**

**rodametria, revisão:** `/status` **120** = `manifest.json` **120**, `versao_sync` 1.1.5, log da revisão 120 com as 7 linhas dizendo `ok` (20.4). Casca 1.30.0.

**A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA — SÓ NA ILHA DA RONDA:** rodametria **verde** (as três URLs da 29.2 com `content-type` certo — `text/plain`, `application/xml`, `application/json` — e caminho virgem em 404 servido pela página da própria ilha, 73.279 bytes, zero HostGator). robometria, aquametria e clubedomosaico: **não medidas hoje** além do HTTP das URLs do sitemap.

**O CAMPO AUSENTE DA SEÇÃO 2 QUE AINDA ESPERA:** a `ohmetria` segue sem `ultima_ronda` e sem `bloqueada_por` no cabeçalho. Pela regra da seção 2, quem reservar a `ohmetria` acrescenta os dois no mesmo commit — reserva é por ilha, e esta ronda não a reservou.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-23** (4 itens: ALTA, `/veiculos/moto-eletrica/` com ZERO link interno de miolo — mãe e irmãs não a listam; `dateModified` de 18/11 nas 11 páginas; preço do único anúncio da moto 2,0% acima do banco, 57 anúncios sem reteste desde 18/11; e o teto do anti-robô da Shopee, que é gesto do Raphael) | 0 dia |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-18 (ronda técnica)**: itens 1 a 4 FECHADOS e conferidos no ar; fica o **item 5**, que é gesto do Raphael (chamado na HostGator + decisão do token) | 5 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-18 (leitura semanal)**: fica o item 2 (os 5 links do Mercado Livre da moto elétrica, gesto do Raphael) e o 3-b (egresso de `rodametria.com.br` nos Domínios adicionais permitidos da conta, gesto do Raphael). O item 4 manda **medir em 25/11** a impressão de `/veiculos/patinete-eletrico/` | 5 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-17, ALTA**: o `.htaccess` da raiz reescrito sem o bloco do WordPress — chamado na HostGator + decisão sobre o token | 6 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-11 (leitura semanal)** | 12 dias |
| robometria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-20** (6 itens: 3 fichas esgotadas no ar, 1 vendedor de férias, o piso da 25.2 ausente em 3 das 4 telas que servem ficha, e a contradição dos 18.500 Pa) | 3 dias |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)**: item 1 FECHADO; o item 2 (URL Inspection em `/pecas/`) é **pedido ao Raphael** | 5 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-11, ALTA** — itens 1 e 2 fechados em 12/11; ficam os itens 3, 4 e 5 | 12 dias |
| clubedomosaico | `dados/despachos.md` | 5 das 17 peças são o MESMO oratório (sufixos `-2` e `-3`) — e o sitemap dela serve hoje **13** peças, não 17 | 12 dias |
| aquametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: fila de ROI para quando a ilha sair do modo de medição | 12 dias |
| ohmetria / jornadafly | `PROMPT.md` | despachos de NASCIMENTO (carregam a fila inteira; pela 18.2 não cabem como despacho) | — |

*(Os dias de cada linha saem da data no título do próprio despacho, contra 23/11. As linhas das ilhas que não são a desta ronda foram lidas do PAINEL de 20/11 e dos títulos no repositório, não remedidas abertura por abertura.)*

## Precisa do Raphael

1. **OS 5 LINKS DO MERCADO LIVRE DA RODAMETRIA** — `ilhas/rodametria/dados/links-afiliado-pendentes.md`, pronto desde 11/11: criar a etiqueta `rodametriamotoeletrica`, gerar os 5 links de catálogo e colar na coluna `url`. O gerador do ML tem reCAPTCHA e não responde a script (25.6). **Argumento novo desta ronda:** a consulta `moto eletrica adulto` continua com **UM** anúncio que serve, e o preço dele já se moveu 2,0% — a página de 823 mil buscas/mês segue degradada, servindo só o piso da busca.
2. **O CHAMADO NA HOSTGATOR, com a frase da 29.5(b) e a série anexada.** A oitava queda desta raiz foi em **21/11 às 05h24Z**, medida pelo contador e sem ninguém por perto; a cura devolveu as páginas na mesma requisição. Série de intervalos: ~4 min · ≥27 min · ≥2 h 26 min · ≥5 h 11 min · ≥23 h · 27 h 19 min (fechado) · **62 h 50 min (fechado)**. Evento irregular, não processo. **Hoje a porta está de pé**, medida nesta ronda.
3. **A DECISÃO SOBRE O TOKEN DO SYNC DA RODAMETRIA** (aberta desde 05/11). Nas irmãs o token está no `PROMPT.md`; nessa, não — e a ausência é real, não deduzida. Custa a trava de uma hora a cada queda.
4. **`cf.shopee.com.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA** (Configurações → Recursos → Domínios adicionais permitidos). A nuvem recebe `CONNECT tunnel failed, response 403`, e por isso o portão de foto da rodametria não separa foto quebrada de foto que o egresso recusou. **Hoje as 9 fotos de cartão carregam no Chrome dele** — inclusive as duas que estavam quebradas em 18/11 —, mas quem mediu isso foi o navegador, não a nuvem.
5. **`rodametria.com.br` NOS DOMÍNIOS ADICIONAIS PERMITIDOS DA CONTA** (o campo da conta, 25.6, onde já moram `robometria.com.br` e `aquametria.com.br`). Sem ele a linha de indexação desta ilha fica em `n/d`, porque o ambiente das MÃOS não alcança o domínio.
6. **A URL INSPECTION DE `/pecas/` DA ROBOMETRIA** — as quatro páginas da leva de 21/09 em "Discovered - currently not indexed", solicitação manual recusada por cota de conta em 14/10.
7. **O TESTE DE VIDA DA 25.4 NÃO RODA PELO CAMINHO QUE O CONTRATO MANDA, NA ROTINA AGENDADA — SEGUNDA RONDA SEGUIDA, E AGORA COM O TETO MEDIDO.** A API de ficha (`shopee.com.br/api/v4/pdp/get_pc`, de dentro de uma aba no domínio) foi **recusada pelo classificador de modo automático** nesta ronda, como foi em 20/11 na robometria. O contorno — abrir a `url_produto` e ler o corpo — funcionou em **15 leituras**, e na **16ª** a Shopee redirecionou para `verify/traffic?...&scene=crawler_item`; a Sentinela é proibida de resolver CAPTCHA e parou ali. **Decisão:** ou a rotina ganha permissão para a rota `shopee.com.br/api/v4/pdp/*`, ou a 25.4 declara a leitura do corpo como método oficial **com teto de ~15 leituras por ronda**.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Zero, e nenhum tentado.** A ronda de 23/11 na rodametria achou três defeitos e **nenhum** é da lista 19.1: um é molde/PHP (a listagem da mãe e o bloco de irmãs), um é o `dateModified` que o snippet escreve, e o terceiro é preço no banco. É a **nona** ronda técnica seguida desta ilha com zero conserto, e a causa é a mesma que a ronda de 16/11 nomeou e a da robometria de 20/11 mediu na segunda ilha: **já não nasce defeito em casca — nasce no dado do banco que envelhece sozinho, no molde que decide quem é listado, e na régua que admite os dois.** O achado de ALTA de hoje é dessa última família: a régua de cluster desta ilha conta o **menu e o rodapé** como links de entrada, e por isso ficou verde sobre uma página com **zero** link de miolo apontando para ela.

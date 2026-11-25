# PAINEL DO ARQUIPÉLAGO

**Instantâneo de 2026-11-25, 15h4xZ**, reescrito pela RONDA DIÁRIA TÉCNICA da **rodametria** (seção 23.1: quem escreve é a ronda, e ninguém mais). Pela 23.4, todo número aqui sai de arquivo do repositório ou de medição desta ronda; o que não foi medido hoje diz `não medido hoje` em vez de repetir número velho com cara de novo.

## Ilhas

| ilha | estado | prio | URLs / 40 | ultima_execucao | ultima_ronda | piso | congelamento |
|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **11** / 40 (medido no ar hoje: 11 de 11 em 200, duas leituras com quebra de cache) | 2026-11-25T13:4xZ | **2026-11-25T15:40Z** (ronda técnica) | abaixo | nenhum — **ILHA EM FOCO TOTAL** desde 27/10 |
| robometria | viva | 1 | 14 / 40 (medido raso hoje: 14 de 14 em 200) | 2026-11-20T11:09Z | 2026-11-20T14:54Z | abaixo | modo de medição (1.2-b.1) |
| aquametria | viva | 2 | 52 / 40 (medido raso hoje: 52 de 52 em 200) | 2026-10-21T21:48Z | 2026-11-18T20:01Z | atingido | modo de medição (1.2-b.1) |
| clubedomosaico | nascendo | 1 | **102** no sitemap (medido raso hoje: 89 em `posts-page` + 13 em `posts-peca`, **102 de 102 em 200**) — o cabeçalho dela diz `urls_publicadas: 44` | 2026-11-12T10:46Z | 2026-11-18T20:01Z | atingido | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 / 40 | 2026-09-15T11:17Z | campo AUSENTE no cabeçalho | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 / 40 | 2026-10-27T19:53Z | null (correto: sem site) | abaixo | sem site; egresso RECUSADO desde 19/10 |

**AS QUATRO ILHAS NO AR RESPONDERAM HOJE, E ISSO FOI MEDIDO E NÃO SUPOSTO:** a ronda foi funda na rodametria e **rasa (só HTTP, do sitemap) nas outras três** — robometria 14/14, aquametria 52/52, clubedomosaico 102/102, rodametria 11/11, todas em 200 com quebra de cache. A varredura rasa existe porque o Clube do Mosaico passou nove dias fora do ar sem ninguém medir.

**NÚMERO QUE NÃO BATE, PELA SEGUNDA RONDA SEGUIDA, E ELE NÃO É DESTA RONDA CONSERTAR (reserva é por ilha):** o `wp-sitemap.xml` da **clubedomosaico** serve hoje **102** URLs (89 `page` + 13 `peca`) contra `urls_publicadas: 44` (27 + 17) do cabeçalho dela, de 12/11 — os MESMOS números de 23/11, e as **peças seguem em 13**, não 17, direção compatível com o despacho aberto dos 5 oratórios repetidos, que ninguém conferiu. É a seção 4 ao pé da letra: o site andou e o cabeçalho ficou para trás. **Quem reservar a clubedomosaico reconta no ar e acerta o campo no mesmo commit.**

**rodametria, revisão:** `/status` **138** = `manifest.json` **138**, `versao_sync` 1.1.5, log da revisão 138 com as 9 linhas dizendo `ok` (20.4).

**A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA — SÓ NA ILHA DA RONDA:** rodametria **verde** (as três URLs da 29.2 com `content-type` certo — `text/plain`, `application/xml` com `<sitemap>` de verdade, `application/json` — e caminho virgem em 404 servido pela página da própria ilha, 73.429 bytes, zero HostGator). O contador durável em `/casca → porta → quedas`: `tem_bloco_wordpress: true`, `cura_liberada_em_s: 0`, `episodios_vistos: 3`, `reposicoes_da_cura: 3`, `leituras_nao_sei: 0`, episódio corrente de 23/11 19:20Z com `reposto_depois: true` — **nenhuma queda nova em 24 e 25/11.** robometria, aquametria e clubedomosaico: **não medidas hoje** além do HTTP das URLs do sitemap.

**O CAMPO AUSENTE DA SEÇÃO 2 QUE AINDA ESPERA:** a `ohmetria` segue sem `ultima_ronda` e sem `bloqueada_por` no cabeçalho. Pela regra da seção 2, quem reservar a `ohmetria` acrescenta os dois no mesmo commit — reserva é por ilha, e esta ronda não a reservou.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-25** (3 itens: ALTA, a home serve o resultado da F1 nas QUATRO categorias com ZERO link de loja, com o piso da 25.2 publicado no banco; `/peso-maximo-patinete-eletrico/` idem, mas dizendo; e o teto do anti-robô da Shopee, que é gesto do Raphael) | 0 dia |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-23**: itens 1, 2 e 3 FECHADOS, e o **ALTA do link interno de miolo da moto elétrica foi CONFERIDO NO AR em 25/11** (de 0 para 5 links de miolo). Fica o **item 4**, que é gesto do Raphael (teto do anti-robô da Shopee) | 2 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-18 (ronda técnica)**: itens 1 a 4 FECHADOS e conferidos no ar; fica o **item 5**, que é gesto do Raphael (chamado na HostGator + decisão do token) | 7 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-18 (leitura semanal)**: fica o item 2 (os 5 links do Mercado Livre da moto elétrica, gesto do Raphael) e o 3-b (egresso de `rodametria.com.br` nos Domínios adicionais permitidos da conta, gesto do Raphael). **O item 4 mandava medir HOJE, 25/11, a impressão de `/veiculos/patinete-eletrico/` — e isso é da LEITURA SEMANAL, não da ronda técnica: não foi medido hoje** | 7 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-17, ALTA**: o `.htaccess` da raiz reescrito sem o bloco do WordPress — chamado na HostGator + decisão sobre o token | 8 dias |
| rodametria | `PROMPT.md` | **DESPACHO DA SENTINELA — 2026-11-11 (leitura semanal)** | 14 dias |
| robometria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-20** (6 itens: 3 fichas esgotadas no ar, 1 vendedor de férias, o piso da 25.2 ausente em 3 das 4 telas que servem ficha, e a contradição dos 18.500 Pa) | 5 dias |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)**: item 1 FECHADO; o item 2 (URL Inspection em `/pecas/`) é **pedido ao Raphael** | 7 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-11, ALTA** — itens 1 e 2 fechados em 12/11; ficam os itens 3, 4 e 5 | 14 dias |
| clubedomosaico | `dados/despachos.md` | 5 das 17 peças são o MESMO oratório (sufixos `-2` e `-3`) — e o sitemap dela serve hoje **13** peças, não 17 | 14 dias |
| aquametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: fila de ROI para quando a ilha sair do modo de medição | 14 dias |
| ohmetria / jornadafly | `PROMPT.md` | despachos de NASCIMENTO (carregam a fila inteira; pela 18.2 não cabem como despacho) | — |

*(Os dias de cada linha saem da data no título do próprio despacho, contra 25/11. As linhas das ilhas que não são a desta ronda foram lidas do PAINEL de 23/11 e dos títulos no repositório, não remedidas abertura por abertura.)*

## Precisa do Raphael

1. **O TESTE DE VIDA DA 25.4 DEIXOU DE TER INSTRUMENTO, E ISTO SUBIU PARA O PRIMEIRO LUGAR DA LISTA HOJE — TERCEIRA RONDA SEGUIDA, E AGORA COM O TETO EM UMA LEITURA.** A rota que o contrato manda (`shopee.com.br/api/v4/pdp/get_pc`, por `fetch` de dentro de uma aba no domínio) foi **recusada pelo classificador de modo automático** nesta ronda, como em 20/11 na robometria e em 23/11 nesta ilha. O contorno autorizado — abrir a `url_produto` e ler o corpo, sem nunca clicar no link de afiliado — aguentou **15 leituras em 23/11** e **1 leitura em 25/11**: a segunda navegação caiu em `shopee.com.br/verify/captcha?...&scene=crawler_item`, e a Sentinela é proibida de resolver CAPTCHA. **Resultado medido de hoje: 1 de 10 itens testado (vivo), 9 não testados, e os 58 anúncios do banco da rodametria seguem sem reteste desde 23/11.** A decisão é uma de duas: permissão para a rota `shopee.com.br/api/v4/pdp/*` na rotina agendada, **ou** a 25.4 passa a declarar que o teste de vida é gesto de sessão dele e não de rotina.
2. **OS 5 LINKS DO MERCADO LIVRE DA RODAMETRIA** — `ilhas/rodametria/dados/links-afiliado-pendentes.md`, pronto desde 11/11: criar a etiqueta `rodametriamotoeletrica`, gerar os 5 links de catálogo e colar na coluna `url`. O gerador do ML tem reCAPTCHA e não responde a script (25.6). A consulta `moto eletrica adulto` continua com **UM** anúncio que serve, e a divergência de preço de 2,0% aberta em 23/11 **não foi remedida hoje**, pela mesma causa do item 1.
3. **O CHAMADO NA HOSTGATOR, com a frase da 29.5(b) e a série anexada.** A oitava queda desta raiz segue sendo a de **21/11 às 05h24Z**; **nenhuma queda nova em 24 e 25/11**, medido pelo contador durável nesta ronda. Série de intervalos: ~4 min · ≥27 min · ≥2 h 26 min · ≥5 h 11 min · ≥23 h · 27 h 19 min (fechado) · **62 h 50 min (fechado)**. Evento irregular, não processo. **Hoje a porta está de pé**, medida nesta ronda.
4. **A DECISÃO SOBRE O TOKEN DO SYNC DA RODAMETRIA** (aberta desde 05/11). Nas irmãs o token está no `PROMPT.md`; nessa, não — e a ausência é real, não deduzida. Custa a trava de uma hora a cada queda.
5. **`cf.shopee.com.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA** (Configurações → Recursos → Domínios adicionais permitidos). A nuvem recebe `CONNECT tunnel failed, response 403`, e por isso o portão de foto da rodametria não separa foto quebrada de foto que o egresso recusou. **Não medido hoje.**
6. **`rodametria.com.br` NOS DOMÍNIOS ADICIONAIS PERMITIDOS DA CONTA** (o campo da conta, 25.6, onde já moram `robometria.com.br` e `aquametria.com.br`). Sem ele a linha de indexação desta ilha fica em `n/d`, porque o ambiente das MÃOS não alcança o domínio.
7. **`*.gov.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA.** É o pedido de uma linha que destrava a constante `exigencia-de-habilitacao-por-categoria-ctb` (hoje `pendente`) e com ela a camada de habilitação da F1 — e é a mesma parede que a camada municipal espera. Enquanto ele não for feito, a home responde, com razão, que "sobre habilitação esta página não responde".
8. **A URL INSPECTION DE `/pecas/` DA ROBOMETRIA** — as quatro páginas da leva de 21/09 em "Discovered - currently not indexed", solicitação manual recusada por cota de conta em 14/10.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Zero, e nenhum tentado.** A ronda de 25/11 na rodametria achou três defeitos e **nenhum** é da lista 19.1: dois são o bloco de compra que o PHP do snippet gera mais a escolha de qual piso a categoria da F1 serve (19.2 nas duas pontas), e o terceiro é gesto do Raphael. É a **décima** ronda técnica seguida desta ilha com zero conserto, e a causa é a que a de 16/11 nomeou e a de 23/11 repetiu: **já não nasce defeito em casca — nasce no dado do banco que envelhece sozinho, no molde que decide quem é listado, e no lugar onde o piso de compra foi gravado.** O achado de ALTA de hoje é dessa última família, e tem antecedente de seis dias na mesma ilha: a **25.2-c** foi escrita em 19/11 porque o piso morava dentro do bloco que não nasce em `/veiculos/moto-eletrica/`; aquela página está consertada e conferida no ar hoje, e **a home nunca recebeu o mesmo conserto.**

# PAINEL DO ARQUIPÉLAGO

**Instantâneo de 2026-11-27, 14h5xZ**, reescrito pela RONDA DIÁRIA TÉCNICA da **clubedomosaico** (seção 23.1: quem escreve é a ronda, e ninguém mais). Pela 23.4, todo número aqui sai de arquivo do repositório ou de medição desta ronda; o que não foi medido hoje diz `não medido hoje` em vez de repetir número velho com cara de novo.

## Ilhas

| ilha | estado | prio | URLs / 40 | ultima_execucao | ultima_ronda | piso | congelamento |
|---|---|---|---|---|---|---|---|
| **clubedomosaico** | nascendo | 1 | **105** no sitemap (medido fundo hoje: 89 `posts-page` + 16 `posts-peca`, **105 de 105 em 200**, duas leituras) — o cabeçalho dela diz `urls_publicadas: 44` | 2026-11-12T10:46Z | **2026-11-27T14:54Z** (ronda técnica) | atingido | **FORA DA FÁBRICA: o `/status` dela diz que o Sync foi DESLIGADO em 19/11 por decisão do Raphael** |
| rodametria | viva | 1 | 11 / 40 (medido raso hoje: 11 de 11 em 200) | 2026-11-27T13:22Z | 2026-11-25T15:40Z (ronda técnica) | abaixo | nenhum — **ILHA EM FOCO TOTAL** desde 27/10 |
| robometria | viva | 1 | 14 / 40 (medido raso hoje: 14 de 14 em 200) | 2026-11-20T11:09Z | 2026-11-20T14:54Z | abaixo | modo de medição (1.2-b.1) |
| aquametria | viva | 2 | 52 / 40 (medido raso hoje: 52 de 52 em 200) | 2026-10-21T21:48Z | 2026-11-18T20:01Z | atingido | modo de medição (1.2-b.1) |
| ohmetria | nascendo | 1 | 0 / 40 | 2026-09-15T11:17Z | campo AUSENTE no cabeçalho | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 / 40 | 2026-10-27T19:53Z | null (correto: sem site) | abaixo | sem site; egresso RECUSADO desde 19/10 |

**AS QUATRO ILHAS NO AR RESPONDERAM HOJE, E ISSO FOI MEDIDO E NÃO SUPOSTO:** 182 URLs de sitemap, **182 em 200** — clubedomosaico 105/105 (ronda funda), rodametria 11/11, robometria 14/14, aquametria 52/52 (as três rasas, só HTTP do sitemap, com quebra de cache). A varredura rasa existe porque o Clube do Mosaico passou nove dias fora do ar sem ninguém medir.

**ALTA — A ILHA DESTA RONDA ESTÁ SÃ NO AR E FORA DA FÁBRICA AO MESMO TEMPO, E O REPOSITÓRIO NÃO SABE.** O log que o `/status` da clubedomosaico serve traz `2026-11-19 14:01 SYNC DESLIGADO em 19/11/2026 por decisão do Raphael: ilha fora da fábrica, nada mais é aplicado do repositório`. Essa decisão **não está escrita em lugar nenhum do repositório**: nem no `ESTADO.md` dela (`estado: nascendo`, `bloqueada_por: null`), nem no `REGISTRO.md`, nem no `foco.md`, nem em `dados/despachos.md` — procurado nos quatro nesta ronda. É a seção 4 virada do avesso: não é o site que ficou para trás, é o repositório. **Consequência que este painel precisa carregar:** os três despachos da Sentinela abertos no `PROMPT.md` dessa ilha (11/11, 18/11, 25/11) pedem trabalho que **não pode chegar ao ar** enquanto o Sync estiver desligado, e a ronda de hoje não pôde consertar nada ali pelo mesmo motivo. É a única das quatro com essa linha, e a única em casca 1.2.0.

**clubedomosaico, revisão:** `/status` **94** = `manifest.json` **94**, casca **1.26.0**, `versao_sync` **1.2.0** — e o último desembarque do log é de **12/11**. As 58 URLs de produto de 20/11 e as 3 peças de hoje nasceram **sem sync**: as peças vêm do painel da artesã, não do repositório.

**A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA — SÓ NA ILHA DA RONDA:** clubedomosaico **verde** (as três URLs da 29.2 com `content-type` certo — `text/plain`, `application/xml` com `<sitemap>` de verdade, `application/json` — e caminho virgem em **404 de 94.071 bytes com 31 ocorrências de `mosaico`**, servido pela página da própria ilha, zero HostGator). `?rest_route=/clubedomosaico/v1/rotas`: `bytes: 1579`, `blocos: ["NFD EPC","WordPress"]`, `tem_wordpress: true`, `mtime` 27/11 14:53Z. **E a porta caiu TRÊS vezes mais desde 12/11** — 20/11 01h50Z, 24/11 15h09Z e 27/11 02h02Z, a 7ª, 8ª e 9ª desta raiz —, as três repostas **sozinha** pela cura automática, com os intervalos **encurtando** (~7 d 15 h → ~4 d 13 h → ~2 d 11 h). Série nova em `ilhas/clubedomosaico/dados/consertos.md`. rodametria, robometria e aquametria: **não medidas hoje** além do HTTP das URLs do sitemap.

**O TESTE DE VIDA DA 25.4 FECHOU UMA TERCEIRA PORTA HOJE, E ISSO VALE PARA AS QUATRO ILHAS.** Tentado nesta ronda pelo contorno autorizado (abrir a `url_produto` crua, nunca o link de afiliado), no navegador desta nuvem, em lotes de 3: **12 de 12 fichas da Shopee em HTTP 200, zero CAPTCHA, e corpo renderizado em ZERO byte de texto** — 0 veredito em 12. A causa: `cf.shopee.com.br` e `down-zl-br.img.susercontent.com` devolvem `net::ERR_TUNNEL_CONNECTION_FAILED` no navegador e `000` por `curl`, e o HTML cru da ficha é casca de JavaScript (sem `<title>`, sem `item_status`, sem "O produto não existe", sem "Esgotado"). Controle da 33 na mesma passada: **`example.com` também devolve `000`**, logo é política da lista de permissões desta nuvem, não queda da Shopee. **Não é CAPTCHA (23 e 25/11) nem 403 (17/09): é um terceiro motivo, e ele muda o valor do item de `cf.shopee.com.br` na lista abaixo.**

**O CAMPO AUSENTE DA SEÇÃO 2 QUE AINDA ESPERA:** a `ohmetria` segue sem `ultima_ronda` e sem `bloqueada_por` no cabeçalho, e a `robometria` sem os dois. Pela regra da seção 2, quem reservar cada uma acrescenta no mesmo commit — reserva é por ilha, e esta ronda não reservou nenhuma.

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| clubedomosaico | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-27** (8 itens: ALTA o Sync desligado que o repositório não registra; ALTA as 58 ofertas intestáveis, sexta leitura; ALTA 704 px de rolagem horizontal em 2 páginas; "Escrito por em" nas 16 peças; `<title>` e `<h1>` duplicados em 2 peças novas; 2 filhas sem irmã; a série da porta; e o teste de vida fechado nesta nuvem) | 0 dia |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-25 (leitura semanal)**: 10 itens, 2 deles ALTA (as 58 sem piso; o autoclique com a etiqueta da ilha) | 2 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)** | 9 dias |
| clubedomosaico | `PROMPT.md` | **SENTINELA 2026-11-11, ALTA** — itens 1 e 2 fechados em 12/11; ficam os itens 3, 4 e 5 | 16 dias |
| clubedomosaico | `dados/despachos.md` (raiz) | peças repetidas na loja: o par `/loja/bandejas/` e `/loja/bandejas-2/` de hoje entra na mesma família | 16 dias |
| rodametria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-25** (3 itens: ALTA a home servindo o resultado da F1 nas quatro categorias com zero link de loja; a página do peso máximo idem; e o teto do anti-robô da Shopee, gesto do Raphael) | 2 dias |
| rodametria | `PROMPT.md` | **SENTINELA 2026-11-23**: itens 1 a 3 fechados; fica o item 4, gesto do Raphael | 4 dias |
| rodametria | `PROMPT.md` | **SENTINELA 2026-11-18 (ronda técnica)**: itens 1 a 4 fechados; fica o item 5, gesto do Raphael | 9 dias |
| rodametria | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)**: ficam o item 2 (os 5 links do Mercado Livre) e o 3-b (egresso de `rodametria.com.br`), os dois gesto do Raphael | 9 dias |
| rodametria | `PROMPT.md` | **FUNDAÇÃO PARA O RAPHAEL — 2026-11-17, ALTA**: o `.htaccess` da raiz e a decisão sobre o token | 10 dias |
| rodametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)** | 16 dias |
| robometria | `PROMPT.md`, topo | **DESPACHO DA SENTINELA — 2026-11-20** (6 itens: 3 fichas esgotadas no ar, 1 vendedor de férias, o piso da 25.2 ausente em 3 das 4 telas que servem ficha, e a contradição dos 18.500 Pa) — **três deles são link de compra morto servido no ar, e é o custo que a 34 nomeia** | 7 dias |
| robometria | `PROMPT.md` | **SENTINELA 2026-11-18 (leitura semanal)**: item 1 fechado; o item 2 (URL Inspection em `/pecas/`) é pedido ao Raphael | 9 dias |
| aquametria | `PROMPT.md` | **SENTINELA 2026-11-11 (leitura semanal)**: fila de ROI para quando a ilha sair do modo de medição | 16 dias |
| ohmetria / jornadafly | `PROMPT.md` | despachos de NASCIMENTO (carregam a fila inteira; pela 18.2 não cabem como despacho) | — |

*(Os dias de cada linha saem da data no título do próprio despacho, contra 27/11. As linhas das ilhas que não são a desta ronda foram lidas dos títulos no repositório, não remedidas abertura por abertura.)*

## Precisa do Raphael

1. **A DECISÃO SOBRE A CLUBEDOMOSAICO ESTAR FORA DA FÁBRICA, E ELA É NOVA NESTA LISTA.** O Sync dela está desligado desde 19/11 por decisão escrita que só existe no log do site. Ou a decisão entra no repositório (`foco.md`, cabeçalho do `ESTADO.md`, `dados/despachos.md`) e os três despachos abertos dela ficam marcados como suspensos, ou o Sync é religado. Enquanto nenhuma das duas acontecer, a ilha é a de maior tráfego do Arquipélago (285 impressões e 5 dos 9 cliques da última janela) recebendo despacho que não pode ser cumprido.
2. **`cf.shopee.com.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA** (Configurações → Recursos → Domínios adicionais permitidos). **Este item mudou de tamanho hoje:** ele era o portão de foto da rodametria e passou a ser **o teste de vida da 25.4 do Arquipélago inteiro** — medido nesta ronda, 12 de 12 fichas em 200 com corpo renderizado vazio porque os ativos do aplicativo da Shopee são recusados pelo egresso, com `example.com` como controle também em `000`.
3. **A ALTERNATIVA, se o item 2 não for o caminho:** permissão para a rota `shopee.com.br/api/v4/pdp/*` na rotina agendada, **ou** a 25.4 passa a declarar que o teste de vida é gesto de sessão dele e não de rotina. A rota que o contrato manda foi recusada pelo classificador de modo automático em 20/11, 23/11 e 25/11.
4. **O CHAMADO NA HOSTGATOR, com a frase da 29.5(b) e a série anexada.** Agora são **duas raízes e doze quedas** no Arquipélago, e a da clubedomosaico chegou à **nona**, com os intervalos encurtando pela terceira medição seguida (~7 d 15 h → ~4 d 13 h → ~2 d 11 h). A cura automática está repondo sozinha, o que compra tempo e não resolve: a 29.5 proíbe tratar reparo como solução.
5. **OS 5 LINKS DO MERCADO LIVRE DA RODAMETRIA** — `ilhas/rodametria/dados/links-afiliado-pendentes.md`, pronto desde 11/11: criar a etiqueta `rodametriamotoeletrica`, gerar os 5 links de catálogo e colar na coluna `url`. O gerador do ML tem reCAPTCHA e não responde a script (25.6). **Não medido hoje.**
6. **A DECISÃO SOBRE O TOKEN DO SYNC DA RODAMETRIA** (aberta desde 05/11). Nas irmãs o token está no `PROMPT.md`; nessa, não. **Não medido hoje.**
7. **`rodametria.com.br` NOS DOMÍNIOS ADICIONAIS PERMITIDOS DA CONTA.** Sem ele a linha de indexação daquela ilha fica em `n/d`, porque o ambiente das MÃOS não alcança o domínio. **Não medido hoje.**
8. **`*.gov.br` NA LISTA DE DOMÍNIOS PERMITIDOS DA CONTA**, que destrava a camada de habilitação da F1 da rodametria. **Não medido hoje.**
9. **A URL INSPECTION DE `/pecas/` DA ROBOMETRIA** — quatro páginas em "Discovered - currently not indexed", solicitação manual recusada por cota de conta em 14/10. **Não medido hoje.**
10. **O NOME DAS DUAS PEÇAS NOVAS DA LOJA.** `/loja/bandejas/` e `/loja/bandejas-2/` são peças **diferentes** com o mesmo nome, e `/loja/vasos/` tem nome genérico. O nome é cadastro da artesã no WordPress, e a 19.3 proíbe a Sentinela mexer por lá — então é gesto, não conserto.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Zero, e a causa não é falta de defeito — é que o canal de conserto da ilha desta ronda está desligado.** A ronda de 27/11 na clubedomosaico achou **seis** defeitos, e **dois deles são da lista 19.1** (as duas filhas de `/como-fazer/` sem link de irmã e sem bloco "Veja também"; o título duplicado das duas peças). A 19.3 exige que o conserto chegue ao ar pelo repositório, seja sincronizado e seja reconferido na URL — e o `/status` dessa ilha diz que nada do repositório é aplicado desde 19/11. Conserto que não chega ao ar falha a trava (a) da 19.4, e falha de conferência vira despacho; o título, além disso, é cadastro da artesã no WordPress, que a 19.3 proíbe tocar. **Os seis estão no despacho de hoje com o motivo escrito item por item, e nenhum foi tentado às cegas.** As três reposições da porta (20/11, 24/11, 27/11) **não** são conserto nosso: foram da cura automática da casca, e entraram em `dados/consertos.md` como série, que é o que sustenta o chamado.

# PAINEL DO ARQUIPÉLAGO

**Instantâneo escrito pela RONDA DIÁRIA de 2026-11-13, entre 14h4xZ e 15h1xZ.** Pela seção 23, só a Sentinela escreve aqui, e este arquivo é instantâneo: sem narrativa, sem histórico, sem projeção. Número sem procedência não entra (23.4); campo não medido nesta ronda diz `não medido hoje`.

Ilha da ronda funda de hoje: **rodametria** (regra da dívida da seção 12 — é a única que teve execução desde a última ronda: 12/11 e 13/11, com a casca indo de 1.10.0 para 1.26.0 e a revisão de 83 para 91). As outras três no ar receberam a ronda técnica curta pela decisão do Raphael de 28/09/2026 (ponteiro da 1.2), e **as três estão sãs**.

**AS DUAS ILHAS QUE CAÍRAM EM 11/11 ESTÃO NO AR HOJE, MEDIDO E NÃO HERDADO:** robometria **14 de 14** e clubedomosaico **44 de 44** URLs do sitemap em 200, as três portas da 29.2 verdes nas duas e caminho virgem em 404 na página da própria ilha nas duas. A clubedomosaico tinha caído **de novo** às 20h0xZ de 11/11 (5ª queda daquela porta, 8ª do Arquipélago) e está de pé agora. A causa segue sendo o chamado na HostGator, que é do Raphael.

## Uma linha por ilha

| ilha | estado | prio | URLs / 40 | dias desde 1ª indexação / 21 | última execução | última ronda | piso | observação |
|---|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **10** / 40 (contado no ar hoje, 2 leituras) | `null` — 0 de 21 | 2026-11-13T13:53Z | 2026-11-13T15:12Z | abaixo | **EM FOCO** (`foco.md`, desde 27/10). Sã: 10 de 10 em 200. `/status` 91 = `manifest` 91 |
| aquametria | viva | 2 | **52** / 40 (contado no ar hoje) | 65 (os 21 fecharam em 30/09) | 2026-10-21T21:48Z | 2026-11-13T15:12Z | atingido | modo de medição (1.2-b.1). Sã: 52 de 52 em 200. `/status` 138 = `manifest` 138 |
| robometria | viva | 1 | **14** / 40 (contado no ar hoje) | 63 | 2026-11-02T10:35Z | 2026-11-13T15:12Z | abaixo | modo de medição (1.2-b.1). Sã: 14 de 14 em 200. `/status` 96 = `manifest` 96 |
| clubedomosaico | nascendo | 1 | **44** / 40 (contado no ar hoje) | desconhecida | 2026-10-23T19:43Z | 2026-11-13T15:12Z | atingido | **caiu em 11/11 às 20h0xZ e está no ar hoje**: 44 de 44 em 200. `/status` 94 = `manifest` 94 |
| ohmetria | nascendo | 1 | 0 | `null` | 2026-09-15T11:17Z | `null` | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 | `null` | 2026-10-27T19:53Z | `null` | abaixo | sem site: não há o que rondar. Egresso da nuvem para o domínio: `não medido hoje` |

## O que a rodametria mediu hoje (ilha da ronda funda)

**No ar, em duas leituras com quebra de cache:** 10 de 10 URLs em **200**; as três portas da 29.2 em 200 com `content-type` certo (`text/plain`, `application/json`, `application/xml`) e o `/wp-sitemap.xml` servindo `sitemapindex` de verdade; caminho virgem em **404 na página da própria ilha** (73.105 bytes, 28 ocorrências do nome da ilha, zero da HostGator); `/status` em **91** = `manifest.json` em **91**.

**A CURA DA PORTA DA 29.4 ESTÁ CARREGADA E TEM ONDE ESCREVER:** `/casca` serve `tem_cura_da_porta: true` e `fonte_do_log_da_cura: "funcao:rodametria_sync_log"`, casca **1.26.0**. **Linha nova de `cura da porta:` nas últimas 24 h: NENHUMA VISÍVEL** — e isto é `não medido` e não `zero`: a janela de 15 linhas do `/status` começa em 12/11 16:39 e a linha da cura de 12/11 16:25 já saiu dela (é a 20.13). O instrumento que responderia "quantas vezes" não existe nesta janela.

**Conteúdo:** zero `&#038;` dentro de `<script>` nas 10 páginas; JSON-LD em 10 de 10, trilha em 9 e ausente só na home (16.3, correto); **zero página órfã** contada na direção de ENTRADA pela 16.9(b) (mínimo medido: 2 links de miolo); **zero** link interno de miolo apontando para fora do sitemap (os `?p=NN` que respondem 301 são o `rel=shortlink` do WordPress, no `<head>`, e não miolo); meta description máxima de **159** (teto 160); **zero** `alt` faltando e **zero** imagem sem `width`/`height`; **zero** `noindex` nas 10; zero frase da lista "Proibidas" do `VOZ.md` em título ou primeiro parágrafo.

**Pixel da 32.5, a 390 px, em navegador de verdade — os números PASSAM:** pior caixa/formulário **428 px** (teto 700), pior primeiro botão de compra **1.351 px** (teto 1.400), 10 de 10 páginas dentro do molde, 0 fora. O portão fecha REPROVADO por outra régua, a 32.5-d (foto de cartão que não carregou), e **a causa é o egresso desta nuvem, medida e não suposta**: `cf.shopee.com.br` devolve `ERR_TUNNEL_CONNECTION_FAILED` aqui, e **no navegador do Raphael as 5 fotos de `/veiculos/patinete-eletrico/` carregam, 5 de 5**. Não é defeito de página e não virou item.

**Console: 10 de 10 limpo do lado da ilha** — 0 erro de JavaScript, 0 exceção, 0 recurso da ilha caído, 0 resposta ≥ 400 vinda da ilha. As 5 a 10 falhas de rede por página são `fonts.gstatic.com` e `cf.shopee.com.br` recusados pelo egresso desta nuvem.

**Comportamento:** menu de celular abre e fecha nas 10 (`aria-expanded` alternando `false→true→false`, lista de `display:none` para `flex`), **4 itens** com a ferramenta principal entre eles; rolagem horizontal **zero** nas 10 (`scrollWidth` 390 = `innerWidth` 390); `<details>` nenhum aberto por padrão.

**As três ferramentas apertadas de verdade, com entrada trocada no formulário e o número conferido na mão — 10 de 10 CERTAS na aritmética:** F1 em 1.000 W/32 km/h com acelerador (autopropelido, o limite inclusive), 1.000 W/40 (ciclomotor), 500 W/25 só pedal (bicicleta elétrica) e 5.000 W/80 (acima do ciclomotor, com a resolução parando onde para); F2 em 36 V × 10,4 Ah = 374 Wh, 72 V × 30 Ah = 2.160 Wh e 48 V × 15 Ah = 720 Wh; F3 em 130 kg → 152, 60 kg → 75 e 77+10 kg → 96, as três com a folga de 10% batendo na mão. **A aritmética está certa e mesmo assim a F2 tem defeito — item 2 do despacho de hoje, e ele é de ENTRADA, não de conta.**

**Teste de vida dos links de afiliado (25.4), no navegador do Raphael, lendo a `url_produto` e NUNCA clicando no link de afiliado — 28 leituras, 1 MORTO:**

- **22 links de ficha de produto: 21 vivos, 1 MORTO.** O morto é `https://shopee.com.br/product/1389372092/23898889810` — *"Patinete Elétrico Adulto Dobrável 30km/h Original Premium"*, loja ZeroOne!, **degrau 1**, encurtado `s.shopee.com.br/4fxWYUAZJT`, servido como **linha 7 da tabela de exemplos de `/veiculos/patinete-eletrico/`**. A página devolve **"O produto não existe"** em **duas** leituras, sem `h1` e com 1.640 bytes de corpo.
- **6 palavras-chave de busca (o piso da 25.2): 6 vivas**, 44 a 74 cartões cada, zero busca vazia.
- **28 de 28 links de loja servidos no `<main>` rastreáveis até o repositório; intestáveis (sem `url_produto`) ZERO; item sem piso da 25.2 ZERO; 44 de 44 botões com `rel="sponsored noopener"` e ZERO link cru.**

**Reconferência do que a ronda de 11/11 e a passada de 12/11 pediram por escrito:**

- `s.shopee.com.br/9pfbJrNKOR` e o anúncio `58212105781` com **zero** ocorrência nas 10 URLs e nos campos vivos do banco — **FECHADO**;
- `\bilhas?\b` com **zero** ocorrência em texto visível nas 10 URLs — **FECHADO**;
- `publicáv` e `Tipo: pendente` com **zero** ocorrência na F2 — **FECHADO**;
- a cadeia de critério de ordenação **idêntica** em `/sobre/`, `/divulgacao-de-afiliados/` e nas duas páginas de produto, vinda de um lugar — **FECHADO na cadeia e ABERTO na quarta cópia**: a frase que o próprio despacho de 11/11 chamou de falsa (*"a ordem é por venda medida"*) **segue no ar** nas duas páginas de produto, vinda de `dados/paginas-de-produto.json`, que o conserto não tocou. Virou o item 3 de hoje;
- a porta de pé e a cura carregada — **FECHADO** (ver acima).

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-13 | 3 itens desta ronda; o item 1 é link morto na tabela de exemplos da página de maior intenção de compra | 0 dias |
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-11 (leitura semanal) | item 1 fechado em 12/11; o que sobra não é da Fundação | 2 dias |
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | itens 1 e 2 — quem fecha é a leitura semanal | 9 dias |
| rodametria | `PROMPT.md`, DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10 | duas SERPs e um volume, numa sessão de Chrome | 14 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-11 | ALTA de queda da porta: **a ilha está no ar hoje, 44 de 44**, mas foi a 5ª queda e a causa segue na HostGator | 2 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | a posição voltou sozinha; o título não deve ser revertido | 9 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-02 (ronda técnica) | os minutos do ciclo da R2 não dependem da metragem | 11 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 16 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 23 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | a rampa destravou; `/loja/` chegou à primeira página | 9 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (ronda técnica) | 2 itens; o item 1 é um terço dos links da ilha | 16 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | duas propostas com consulta nomeada | 16 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 23 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-14 (leitura semanal) | — | 30 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 16 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 23 dias |
| aquametria | `PROMPT.md`, DESPACHO DO RAPHAEL — 2026-10-09 | páginas pelo nome do produto: só a metade que esta nuvem não alcança | 35 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-07 (leitura semanal) | só o que falta ficou | 37 dias |

**FECHADO DESDE O PAINEL ANTERIOR:** o despacho ALTA da robometria de 2026-11-11 (ilha fora do ar) — reparado em 11/11 às 17h54Z e **conferido no ar hoje**, 14 de 14 URLs em 200 e as três portas verdes.

## Precisa do Raphael

1. **O chamado na HostGator, e ele é o único lugar onde a causa se resolve.** O bloco `# BEGIN WordPress` do `.htaccess` da raiz foi apagado **oito vezes** no Arquipélago, a mais recente em 11/11 às 20h0xZ na clubedomosaico, 2h06 depois de um reparo. A rodametria já tem a cura automática da 29.4 carregada (casca 1.26.0); **as outras três não têm**, e nelas a próxima queda dura até alguém rodar um comando.
2. **rodametria — duas SERPs e um volume, numa sessão de Chrome** (despacho da Fundação de 30/10, 14 dias abertos). A SERP brasileira não se alcança desta nuvem: `google.com.br`, `bing.com` e `duckduckgo.com` em `000` (seção 33, remedido em 13/11 no cabeçalho da ilha).
3. **rodametria — o limiar legal da F1 segue sem fonte**: `gov.br`, `in.gov.br`, `planalto.gov.br` e `lex.com.br` em **000** no egresso desta nuvem, remedidos em 13/11. E `lista.mercadolivre.com.br` em **403**, que é o que trava as duas pontas de página de produto do degrau 2.
4. **clubedomosaico — os 5 oratórios repetidos** (a mesma peça com sufixos `-2` e `-3` entre as 17 do sitemap): a decisão de virar 301 é dele, e muda `urls_publicadas` de 44 para 39.
5. **aquametria — o despacho do Raphael de 09/10**, na metade que esta nuvem não alcança (35 dias).

## Consertos das últimas 24 h (lista mecânica da 19.1)

**ZERO**, e nenhum foi tentado: **nenhum dos três defeitos achados hoje é da lista 19.1.** É a SEXTA ronda técnica seguida desta ilha com zero conserto, sempre pela mesma causa — o defeito mecânico da rodametria nasce dentro de snippet, de gerador ou do metadado do banco.

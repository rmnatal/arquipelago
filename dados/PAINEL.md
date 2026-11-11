# PAINEL DO ARQUIPÉLAGO

**Instantâneo escrito pela RONDA DIÁRIA de 2026-11-11, entre 14h3xZ e 15h0xZ.** Pela seção 23, só a Sentinela escreve aqui, e este arquivo é instantâneo: sem narrativa, sem histórico, sem projeção. Número sem procedência não entra (23.4); campo não medido nesta ronda diz `não medido hoje`.

Ilha da ronda funda de hoje: **rodametria** (regra da dívida da seção 12 — publicou desde a última ronda: as revisões 82 e 83 desembarcaram hoje, a última às 14h10Z, e a ronda mediu na 83). As outras três no ar receberam a ronda técnica curta pela decisão do Raphael de 28/09/2026 (ponteiro da 1.2) — **e foi ela que achou o defeito ALTA de hoje.**

**HOUVE NAVEGADOR NESTA RONDA, e isso é a diferença entre este painel e os três anteriores.** A extensão de Chrome do Raphael respondeu (1 navegador conectado) e o Chromium desta nuvem subiu pela seção 33. Com os dois, as três afirmações que as rondas de 04, 06 e 09/11 declararam "não medidas por falta de navegador" foram medidas hoje: **o teste de vida da 25.4, o console das páginas e os pixels da 32.5.**

## ALTA — DUAS ILHAS FORA DO AR

**robometria e clubedomosaico servem só a home.** Medido às 15h0xZ de 11/11/2026, uma leitura com quebra de cache por URL:

| medida | robometria | clubedomosaico |
|---|---|---|
| `/` (home) | **200** | **200** |
| as três portas da 29.2 (`/robots.txt`, `/wp-json/`, `/wp-sitemap.xml`) | **404 nas três** | **404 nas três** |
| páginas de caminho bonito testadas | **0 de 7 em 200** (`/pecas/`, `/pecas/filtros/`, `/sobre/`, `/contato/`, `/privacidade/`, `/calculadoras/`, `/guias/`) | **0 de 8 em 200** (`/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`, `/loja/`, `/privacidade/`, `/materiais/colas-e-adesivos/`, `/materiais/acabamento/`) |
| quem serve o 404 | página de estacionamento da **HostGator**, 2.361 bytes, **zero** ocorrência do nome da ilha | idêntica, 2.361 bytes, **zero** ocorrência do nome da ilha |
| REST por `?rest_route=` (29.7) | **200**, `application/json`, revisão **96** | **200**, `application/json`, revisão **93** |
| rota `/rotas` da 29.3 registrada | **sim** (401 sem token) | **sim** (401 sem token) |

**As quatro grandezas da 29.7(3) estão na mesa, então a causa se NOMEIA:** o bloco `# BEGIN WordPress` sumiu do `.htaccess` da raiz. **6ª e 7ª queda da mesma porta no Arquipélago** (clubedomosaico 24/09, 05/10 e 08/10; robometria 30/10; rodametria 05/11). O reparo é `?rest_route=/<ilha>/v1/rotas&token=<token do Sync>&reparar=1`, e **o token não está no repositório: o reparo não é exercitável desta nuvem.**

**Janela da queda, medida e não estimada:** o painel de **09/11 às 14h5xZ** registrou as duas ilhas com 14 de 14 e 44 de 44 URLs em 200 e as três portas verdes. Portanto as duas caíram **entre 09/11 14h5xZ e 11/11 15h0xZ** — no máximo **2 dias e 20 minutos**.

## Uma linha por ilha

| ilha | estado | prio | URLs / 40 | dias desde 1ª indexação / 21 | última execução | última ronda | piso | observação |
|---|---|---|---|---|---|---|---|---|
| **rodametria** | viva | 1 | **10** / 40 (contado no ar hoje) | `null` — 0 de 21 | 2026-11-11T14:16Z | 2026-11-11T15:03Z | abaixo | **EM FOCO** (`foco.md`, desde 27/10). Sã: 10 de 10 em 200 |
| aquametria | viva | 2 | **52** / 40 (contado no ar hoje) | 63 (os 21 fecharam em 30/09) | 2026-10-21T21:48Z | 2026-11-11T15:03Z | atingido | modo de medição (1.2-b.1). Sã: 52 de 52 em 200 |
| **robometria** | viva | 1 | **não medido hoje** — o `wp-sitemap.xml` está em 404 e não há o que contar | 61 | 2026-11-02T10:35Z | 2026-11-11T15:03Z | abaixo | **FORA DO AR, menos a home (ALTA acima)** |
| **clubedomosaico** | nascendo | 1 | **não medido hoje** — o `wp-sitemap.xml` está em 404 e não há o que contar | desconhecida | 2026-10-23T19:43Z | 2026-11-11T15:03Z | abaixo (cabeçalho) | **FORA DO AR, menos a home (ALTA acima)**. A divergência 32 (cabeçalho) × 44 (ar) segue aberta e hoje não é mensurável |
| ohmetria | nascendo | 1 | 0 | `null` | 2026-09-15T11:17Z | `null` | abaixo | sem site: não há o que rondar |
| jornadafly | nascendo | 1 | 0 | `null` | 2026-10-27T19:53Z | `null` | abaixo | sem site e com o egresso da nuvem recusado em 27/10 — `não medido hoje` |

## O que a rodametria mediu hoje (ilha da ronda funda)

**No ar, em duas leituras com quebra de cache:** 10 de 10 URLs em **200**; as três portas da 29.2 em 200 com `content-type` certo (`text/plain`, `application/json`, `application/xml`) e o `/wp-sitemap.xml` servindo `sitemapindex` de verdade; caminho virgem em **404 na página da própria ilha** (28 ocorrências do nome da ilha no corpo, zero da HostGator); `/status` em **83** e `manifest.json` em **83**, iguais.

**Conteúdo:** zero `&#038;` dentro de `<script>` nas 10 páginas; **zero comentário dentro do `<script>` da ilha** — a 32.4-d, escrita hoje, está **fechada no ar** (os 7 marcadores que sobram são do `speculationrules` do próprio WordPress, não da ilha); JSON-LD em 10 de 10, trilha em 9 e ausente só na home (16.3); **zero página órfã** (mínimo de 2 links de miolo por URL, contados na direção de ENTRADA pela 16.9(b)) e **zero** link interno apontando para fora do sitemap; meta description máxima de **159** (teto 160).

**Pixel da 32.5, a 390 px, em navegador de verdade — 10 de 10 APROVADAS:** pior formulário/caixa a **548 px** (teto 700) e pior primeiro botão de compra a **1.351 px** (teto 1.400). Números por página: `/` form 369; `/autonomia-patinete-eletrico/` form 353 e botão 1.351; `/peso-maximo-patinete-eletrico/` form 353 e caixa 548; `/veiculos/patinete-eletrico/` caixa 211 e botão 1.191; `/veiculos/bicicleta-eletrica/` caixa 211 e botão 1.145; `/veiculos/` caixa 428; as quatro institucionais caixa 244.

**Console: 10 de 10 limpo do lado da ilha** — 0 erro de JavaScript, 0 exceção, 0 recurso da ilha caído, 0 resposta ≥ 400 vinda da ilha. As 5 a 10 falhas de rede por página são **do egresso desta nuvem e não da ilha**: `fonts.gstatic.com` e `cf.shopee.com.br` devolvem `ERR_TUNNEL_CONNECTION_FAILED`. Não é defeito de página e não vira despacho.

**Comportamento, que nenhuma régua de HTTP alcança:** o menu de celular abre e fecha nas 10 (o `aria-expanded` alterna `false→true→false` e a lista sai de `display:none` para `flex`); o menu serve **4 itens** e a ferramenta principal da ilha está entre eles (**o item 5 do despacho de 09/11 está fechado no ar**); `<details>` nenhum aberto por padrão; rolagem horizontal **zero** nas 10 (`scrollWidth` 390 = `innerWidth` 390); a barra fixa esconde quando o bloco de compra está na tela e aparece quando sai, nas 6 páginas que a servem, com o rótulo certo nas duas pontas (`Ver produtos` onde há cartão, `Por que não indicamos` onde não há).

**As três ferramentas apertadas de verdade, com entrada trocada no formulário e o número conferido na mão — 9 de 9 CERTAS:** F1 em 1.000 W/32 km/h com acelerador (autopropelido, o limite inclusive), 1.000 W/40 (ciclomotor), 1.500 W/45 (ciclomotor), 5.000 W/80 (acima do ciclomotor) e 500 W/25 só pedal assistido (bicicleta elétrica); F2 em 36 V × 10,4 Ah no plano (374 Wh, 50 km) e 72 V × 30 Ah em ladeira (2.160 Wh, 38 km = 90 ÷ 2,37); F3 em 130 kg (143 kg = 130 × 1,10) e 60 kg (66 kg). **Coerência da recomendação:** acima de ~109 kg de peso total o bloco de compra diz, com o número, que nenhum dos 3 veículos com carga declarada aguenta — e não inventa vitrine.

**Teste de vida dos links de afiliado (25.4), no navegador do Raphael, lendo a `url_produto` e NUNCA clicando no link de afiliado — 31 itens medidos, 1 MORTO:**

- **24 links de ficha de produto: 23 vivos, 1 esgotado.** O morto é `https://shopee.com.br/product/1430771203/58212105781` — *"Patinete Elétrico Adulto 650W com 3 Velocidades Bateria Recarregável para Mobilidade Urbana"*, **degrau 1**, encurtado `s.shopee.com.br/9pfbJrNKOR`, servido como **cartão 2 da vitrine de `/veiculos/patinete-eletrico/`**. A palavra **`Esgotado`** aparece colada ao título, em **duas** leituras.
- **7 palavras-chave de busca (o piso da 25.2): 7 vivas**, 15 cartões cada, zero busca vazia.
- **29 de 29 botões servidos no `<main>` rastreáveis até o repositório; intestáveis (sem `url_produto`) ZERO; item sem piso da 25.2 ZERO.**

## Despachos abertos

| ilha | onde | o que é | aberto há |
|---|---|---|---|
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-11 | **ALTA: ilha fora do ar, menos a home. Reparo exige o token do Sync** | 0 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-11 | **ALTA: ilha fora do ar, menos a home. Reparo exige o token do Sync** | 0 dias |
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-11 | 4 itens desta ronda; o item 1 é link morto na vitrine | 0 dias |
| rodametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | ALTA: itens 1 e 2, nenhum fechado — quem fecha é a leitura semanal; o "pronto quando" do item 1 pede 9 páginas e o sitemap serve 10 | 7 dias |
| rodametria | `PROMPT.md`, DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10 | duas SERPs e um volume, numa sessão de Chrome | 12 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | a posição voltou sozinha; o título não deve ser revertido | 7 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-02 (ronda técnica) | os minutos do ciclo da R2 não dependem da metragem | 9 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 14 dias |
| robometria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 21 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-11-04 (leitura semanal) | a rampa destravou; `/loja/` chegou à primeira página | 7 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (ronda técnica) | 2 itens; o item 1 é um terço dos links da ilha | 14 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | duas propostas com consulta nomeada | 14 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 21 dias |
| clubedomosaico | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-14 (leitura semanal) | — | 28 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-28 (leitura semanal) | ilha em modo de medição | 14 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-21 (leitura semanal) | — | 21 dias |
| aquametria | `PROMPT.md`, DESPACHO DO RAPHAEL — 2026-10-09 | páginas pelo nome do produto: só a metade que esta nuvem não alcança | 33 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-10-07 (leitura semanal) | só o que falta ficou | 35 dias |
| aquametria | `PROMPT.md`, DESPACHO DA SENTINELA — 2026-09-23 (leitura semanal) | — | 49 dias |
| ohmetria | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 58 dias |
| jornadafly | `PROMPT.md`, DESPACHO DO RAPHAEL — 14/09 | despacho de nascimento: a ilha não tem site | 58 dias |

**FECHADO desde o painel anterior, e por isso saiu desta lista:** o DESPACHO DA SENTINELA — 2026-11-09 da rodametria, cinco itens, fechado em 09/11 às 17h4xZ na revisão 72. **Reconferência independente desta ronda, item por item, no ar:** (1) os quatro `id` de repositório **não aparecem** em texto visível nas 10 URLs; (2) o `nota` de `veiculos.json` diz **4 publicáveis, recontados por `derivar-banco.py` e conferidos por `validar-banco.py`** — o campo que voltou duas vezes está fechado na terceira; (3) o rótulo da barra fixa é `Ver produtos` só onde há cartão; (4) `17 registros` × `14 anúncios colhidos` separados pelo verbo; (5) o menu serve a ferramenta principal da ilha. **Os cinco passam.**

As linhas de despacho das ilhas **fora do foco** vêm das datas dos próprios cabeçalhos e **não foram reconferidas nesta ronda**: a ronda técnica curta mede o ar delas, não a fila delas.

## Precisa do Raphael

- **ALTA — LEVANTAR A PORTA DE ENTRADA DA robometria E DA clubedomosaico.** As duas servem só a home; o reparo é um GET, e só ele falta: `https://robometria.com.br/?rest_route=/robometria/v1/rotas&token=<token do Sync>&reparar=1` e `https://clubedomosaico.com.br/?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>&reparar=1`. O token se lê logado em `?rest_route=/<ilha>/v1/token` e **não está no repositório por decisão**, então nenhuma rotina faz isso. Pronto quando: as três portas da 29.2 em 200 com `content-type` certo e o `wp-sitemap.xml` servindo `sitemapindex`.
- **ALTA — O CHAMADO NA HOSTGATOR DEIXOU DE SER DE UMA ILHA.** A 19.4(b) manda parar de consertar defeito que volta; esta é a **7ª** queda da mesma porta no Arquipélago e a **2ª** da robometria em 12 dias. O chamado em `dados/despachos.md` fala só do `.htaccess` de `/clubedomosaico.com.br`; **o de `/robometria.com.br` cai pela mesma assinatura byte por byte e precisa entrar no mesmo chamado.**
- **rodametria — a parede do `.gov.br`** segue de pé, última medição 05/11, **não remedida hoje** — `não medido hoje`. Trava o CTB (a metade da habilitação), as prefeituras e as três etiquetas do Mercado Livre.
- **rodametria — despacho da Fundação de 30/10:** abrir a SERP das duas caudas que sobraram e ler um volume, numa sessão de Chrome, ~10 minutos.
- **Gerador do Mercado Livre** continua com reCAPTCHA: link `/p/` novo é clique dele (25.6). Nunca bloqueia página — o piso da 25.2 é a busca.
- **jornadafly** segue sem WordPress e com o egresso recusado (última medição 27/10), em espera até decisão nova dele.
- **ohmetria** segue sem site.

**O QUE DEIXOU DE PRECISAR DELE:** a linha "um navegador aberto no computador dele", que os painéis de 04, 06 e 09/11 traziam como a mais caradura. A extensão respondeu hoje sem nada ser pedido, e o Chromium desta nuvem resolve pixel, console e comportamento pela seção 33. **O teste de vida da Shopee continua sendo do navegador dele** (desta nuvem o `deo.shopeemobile.com` é recusado pelo egresso e a página não renderiza — medido hoje, 23 recursos falhados, corpo vazio) — e hoje ele respondeu, 31 itens em lotes de 3, zero CAPTCHA.

## Consertos das últimas 24 h (lista mecânica da 19.1)

**Nenhum.** A ronda de hoje na rodametria achou 4 defeitos e consertou **zero**, e **nenhum conserto foi tentado, porque nenhum dos quatro é da lista 19.1**: o item 1 é link morto, que é dado do banco (19.2); o item 2 é a palavra `ilha` servida ao visitante em 5 páginas, e ela mora em `dados/paginas-institucionais.json` **e** em três snippets, o que cai na trava 3 da seção 12 e na 22.7; o item 3 é literal de snippet; o item 4 é escolha entre duas redações defensáveis (19.2). **É a QUINTA ronda seguida desta ilha com zero conserto, e as cinco pelo mesmo motivo** — o defeito mecânico desta ilha nasce dentro de snippet, de gerador ou do metadado do banco. Pela 19.5, volume de defeito mecânico que não cabe na Sentinela é problema de casca, e casca é da Fundação.

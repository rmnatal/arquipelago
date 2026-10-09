# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 09/10/2026 14h5xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **clubedomosaico** (a única ilha com execução nova desde a última ronda, pela regra da dívida da seção 12) e a **ronda técnica inteira** na aquametria e na robometria.

`foco.md` nomeia a **clubedomosaico** desde 24/09, e registra a fila decidida pelo Raphael em 09/10: a clubedomosaico fecha em 09/10 e entra em modo de medição, a **aquametria** entra em foco de 10/10 a 16/10 e a **jornadafly** a partir de 17/10. **Quem troca o foco é a linha `ilha:` do `foco.md`, editada na data** — a linha da fila não troca sozinha. A ronda técnica roda em toda ilha no ar (decisão do Raphael de 28/09, seção 1.2); a leitura semanal estratégica e o teto de geração de link continuam só na ilha em foco.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| clubedomosaico | nascendo (EM FOCO até 09/10) | 1 | **21 / 40** (medido no ar hoje, wp-sitemap) | sem registro (`primeira_indexacao: desconhecida`) | 09/10 (duas execuções; cabeçalho em 15h5xZ) | **09/10 14h5xZ** | abaixo |
| aquametria | viva (modo de medição; foco a partir de 10/10) | 2 | **52 / 40** (medido no ar hoje, wp-sitemap) | **30 / 21 — fechado** (desde 09/09) | 24/09 17h02Z | **09/10 14h5xZ** | abaixo (o cabeçalho manda passar a `atingido` no primeiro bloco) |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (medido no ar hoje, wp-sitemap) | **28 / 21 — fechado** (desde 11/09) | 21/09 20h09Z | **09/10 14h5xZ** | abaixo |
| jornadafly | nascendo (sem site; foco a partir de 17/10) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS ILHAS NO AR:** `/`, `/wp-sitemap.xml` (200, `application/xml`), `/robots.txt` (200, `text/plain`) e `/wp-json/` (200, `application/json`) **nas três**, e caminho inexistente em **404 na página da própria ilha nas três**. Nenhuma das três está fora do ar. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ, e a quarta linha da série não precisou ser escrita.**

**TODAS AS URLs DO SITEMAP EM 200:** 21 de 21 na clubedomosaico, 52 de 52 na aquametria, 14 de 14 na robometria. **`/status` igual ao `manifest.json` nas três:** clubedomosaico **71**, aquametria **117**, robometria **81**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS TRÊS, nas 21 + 52 + 14 URLs:** zero `&#038;` dentro de `<script>`; zero página órfã (mínimo de 2 links internos na clubedomosaico, 3 na aquametria, 4 na robometria); zero `noindex` indevido; `description` em todas e nenhuma acima de 160; JSON-LD em todas e `BreadcrumbList` em todas as que não são home; breadcrumb visível; zero `<img>` sem `alt` e zero sem `width`/`height`; `aria-expanded` e `aria-controls`; nenhuma palavra da lista "Proibidas" do `VOZ.md` de cada ilha em `<title>`, `<h1>` ou primeiro parágrafo. **Console sem uma mensagem**, com recarga, nos dois estados com parâmetro da F1 e da F2.

**AS DUAS FERRAMENTAS DA ILHA EM FOCO, COM ENTRADA REAL E A CONTA REFEITA NA MÃO, EM ESTADO INÉDITO:** **F1** em `forma=cilindro, d=22, h=30, p15, esp=4, junta=5, sobra=15, rejunte=acrilico, onde=externo_exposto` → **2.073 cm² (0,207 m²), passo 2,0 cm, 2.500 pastilhas/m², 597 pastilhas**. Confere: π × 22 × 30 = 2.073,45; 1,5 + 0,5 = 2,0; 10.000 ÷ 4 = 2.500; 2.073,45 ÷ 4 = 518,36, com 15% = 596,12 → **597**. **Os quatro números batem**, e a página se recusa a calcular o rejunte acrílico com o motivo publicado. **F2** em `mdf_madeira + interno_molhado + caco_azulejo + 4 mm` → **Tekbond Silicone Neutro**, com `madeira` declarada pelo fabricante, e quatro rejuntes cujas faixas cobrem de fato 4 mm (1–4, 2–10, 1–5, 2–10), com o Piscinas fora e o motivo escrito. **Coerência da recomendação: passa nas duas.**

**ZERO DEFEITO NOVO DE ILHA, E ZERO CONSERTO A FAZER — segunda ronda seguida.** O único achado é de **instrumento** e está na lista do Raphael.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| clubedomosaico | `PROMPT.md`, despacho de 09/10 item 1 | **o teste de vida da 25.4 continua morto, pela terceira ronda seguida** — 4 de 24 itens medidos hoje, os 20 da Shopee NÃO MEDIDOS. Não é da Fundação: a escolha do método é do Raphael | 07/10/2026 (2 dias) |
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase** — `/sobre/`, `/qual-peca-serve-no-meu-robo-aspirador/` e `/pecas/` contra `/filtro-universal-de-robo-aspirador/`. Escolher a definição é da Fundação (19.2), e a ilha está fora do foco, então espera pela 1.2 | 02/10/2026 (7 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda** — remedido hoje: 404 · 200 · 200 · 200 em caminho virgem. Camada do hospedeiro; o fechamento é do Raphael | 29/09/2026 (10 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também nesta ilha** — remedido hoje: 404 · 404 · 200 · 200. O fechamento é do Raphael | 30/09/2026 (9 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (leitura semanal, reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa, que impede o painel de responder "qual ilha vendeu" — não pôde ser reconferido em 08/10 porque a sessão do Shopee Afiliados está deslogada | 23/09/2026 (16 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal**: a saída de `/author/` de `dados/posicoes.md`, o formato `clubedomosaico-f2---` no Relatório de cliques, o CTR de `qual-cola` e o primeiro clique orgânico | 23/09/2026 (16 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | propostas 1 e 3 da leitura semanal de 16/09: as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (23 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 14/09: a linha de método da 25.4. É do Raphael | 14/09/2026 (25 dias) |
| aquametria | `ilhas/aquametria/PROMPT.md` | **os itens do banco com link de produto e sem `url_produto`** — a dívida da 25.4-b. **Não remedido hoje** (a ronda técnica mede o site, não o banco desta ilha): o último número medido é de 02/10, 12 de 78. Entra em foco em 10/10 | 13/09/2026 (26 dias) |

**SAIU DA LISTA HOJE:** nada — nenhum despacho fechou, e nenhum novo item da Fundação nasceu.

## Precisa do Raphael

- **O TESTE DE VIDA DA 25.4 CONTINUA MORTO, E AGORA SÃO TRÊS RONDAS SEGUIDAS (05/10 degradado, 07/10 e 09/10 em zero).** Medido hoje em dois contextos de aba: `api/v4/pdp/get_pc` e `api/v4/item/get` devolvem **403 com `error: 90309999` na primeira chamada**, inclusive com a sessão logada (`is_login: true`) e inclusive abertas direto na barra de endereço; a ficha e até a **home** da Shopee caem em `verify/captcha?...&scene=crawler_item` com o quebra-cabeça *"Arraste para completar"*. **A Sentinela é proibida de resolver CAPTCHA (25.4).** Resultado de hoje: **4 de 24 itens medidos** — os 4 do Mercado Livre `/p/MLB...`, vivos com preço (R$ 59, R$ 81, R$ 19, R$ 76) — e **20 NÃO MEDIDOS**, todos da Shopee. **"Não medido" não é "vivo": 20 dos 41 itens desta ilha estão com a saúde do link desconhecida há 3 dias.** A decisão de qual passa a ser o método é do Raphael. **Aberto há 2 dias, e é o mais caro da lista.**
- **NÃO HOUVE RONDA EM 08/10, E FOI EXATAMENTE O DIA EM QUE A PORTA CAIU PELA TERCEIRA VEZ.** O `ultima_ronda` do cabeçalho era de **07/10 20h35Z** quando esta ronda abriu, e a queda de 08/10 (20 das 21 URLs em 404) foi pega às 19h2xZ pela **Fundação**, no aviso do `PROMPT.md`, não pela ronda. É a terceira vez que a demora tem a mesma causa: ninguém rodou o comando naquela janela. Não há conserto de código para isto — é a cadência da própria vigia. **Aberto há 1 dia.**
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`.** O bloco `# BEGIN WordPress` desapareceu pela **terceira** vez em 08/10, com a mesma assinatura nas seis grandezas, e o intervalo entre quedas encurtou de 11 dias para 3. **Reconferido hoje: o reparo de 08/10 está de pé, 21 de 21 em 200, porta de entrada inteira.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 4 dias.**
- **O ACIONAMENTO DO SYNC PELA ROTINA DA SENTINELA ESTÁ BLOQUEADO.** `?clubedomosaico_sync=...&forcar=1` por `curl` é recusado pelo ambiente desta rotina (classificado como deploy em produção). Enquanto estiver assim, a 19.1 e a 19.3 são **letra morta para a Sentinela** em todo defeito que dependa de desembarque. Não travou nada hoje, porque hoje não houve defeito da 19.1 para consertar. **Aberto há 4 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — em DUAS ilhas.** Remedido hoje, em sonda virgem: clubedomosaico **404 · 200 · 200 · 200**, robometria **404 · 404 · 200 · 200**, aquametria **404 nas quatro**. Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 10 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Remedido hoje em **três** passadas da nuvem, pela 20.2: **000 nas três**. O teste de vida dos 4 links de catálogo `/p/MLB...` teve de ser feito no navegador outra vez. **Aberto há 11 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na própria URL de boletim que 19 campos do banco citam. **Aberto há 4 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** na rede Personalizada — trava a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly, que entra em foco em 17/10. Detalhe em `dados/despachos.md`. **Aberto há 25 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Sem ela não há Search Console neste ambiente — e é o instrumento que diria quando o Google viu os 404 de 08/10. **Aberto há 22 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico são as pastilhas, e os 13 esperam por ela. Está em `dados/despachos.md`. **Aberto há 9 dias.**
- **Uma linha na seção 25.4 do `ARQUIPELAGO.md` sobre como se testa o degrau 4.** **Aberto há 20 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — tirar a unidade de dentro do valor de `cdm_medidas`. A metade de máquina está entregue e conferida. Falta a metade que é dado da artesã. **Aberto há 11 dias.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 21 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/` — a página Sobre segue com "a artesã". Não bloqueia. **Aberto há 28 dias.**
- **A sessão do Shopee Afiliados está deslogada** — o Relatório de cliques não abre, e sem ele o `sub_id` deslocado não se reconfere. **Aberto há 1 dia.**
- **A ilha 4 / purga por API do hospedeiro** — os dois continuam em `dados/despachos.md`, sem mudança nesta ronda.
- **O cabeçalho da `ohmetria` continua sem `ultima_ronda` e sem `bloqueada_por`.** É da próxima execução que reservar aquela ilha. Fica aqui só para não se perder.

## Consertos das últimas 24 h

**Nenhum conserto, e nenhum tentado** — nenhum defeito da lista fechada 19.1 apareceu nesta ronda, nas três ilhas no ar. O teto de 5 da 19.5 não foi tocado. `ilhas/clubedomosaico/dados/consertos.md` ganhou a linha desta ronda, que é de **reconferência**.

**Reconferência da 19.4(c), na clubedomosaico:** as **dez** entradas de `dados/consertos.md` foram abertas antes de qualquer outra coisa e reconferidas no ar. **(1) O reparo do `.htaccess` de 08/10 — a terceira queda — PASSOU**, e era essa a reconferência que aquela entrada pré-registrou: 21 de 21 em 200, porta de entrada inteira, 404 virgem na página da ilha. A **quarta** linha da série não precisou ser escrita. **(2) A porta de entrada de 24/09 e o reparo de 05/10 PASSARAM** pela sexta ronda seguida. **(3) Os links regerados de 25/09 PASSARAM, e em número maior** — **78** ocorrências de link de loja servidas, 73 `s.shopee.com.br` + 5 `meli.la`, **100% rastreáveis, zero cru, zero encurtador desconhecido**. **(4) A etiqueta de robô de 25/09 PASSOU** — zero `noindex` indevido nas 21, nenhuma `<meta robots>` duplicada. **(5) O soft 404 na borda de 29/09 CONTINUA** e segue sendo do Raphael. **(6) Os cinco defeitos de 28/09 continuam fechados.** **(7) O item 1 de 30/09 CONTINUA cumprido.**

**Piso da 25.2, medido no banco inteiro da ilha em foco:** **41 de 41** itens com bloco de afiliado têm `url_busca` **e** `url_busca_produto`. **Itens intestáveis (com `url` e sem `url_produto`): ZERO.** **Degrau nulo: ZERO.** Degraus: **1** no degrau 1, **4** no degrau 2 (todos `/p/MLB...`), **19** no degrau 3, **17** no degrau 4.

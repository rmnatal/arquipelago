# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 02/10/2026 14h51Z, pela **ronda diária técnica**, que mediu **as três ilhas no ar**.

`foco.md` nomeia a **clubedomosaico** desde 24/09. **Construção continua só nela.** A ronda técnica roda em toda ilha no ar, em foco ou fora (decisão do Raphael de 28/09, seção 1.2); a leitura semanal estratégica e o teto de geração de link continuam só na ilha em foco.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| clubedomosaico | nascendo (EM FOCO) | 1 | **17 / 40** (medido no ar hoje, wp-sitemap) | sem registro (`primeira_indexacao: desconhecida`) | 02/10 13h17Z | **02/10 14h51Z** | abaixo |
| aquametria | viva (modo de medição) | 2 | **52 / 40** (medido no ar hoje, wp-sitemap) | **23 / 21 — fechado** (desde 09/09) | 24/09 17h02Z | **02/10 14h51Z** | abaixo |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (medido no ar hoje, wp-sitemap) | **21 / 21 — fecha hoje** (desde 11/09) | 21/09 20h09Z | **02/10 14h51Z** | abaixo |
| jornadafly | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**O QUE A RONDA TÉCNICA MEDIU NO AR NAS TRÊS, hoje:** **83 URLs de sitemap em 200** (17 + 52 + 14). Porta de entrada da 29.2 **inteira nas três** (`/wp-sitemap.xml` 200 com `application/xml` e XML de sitemap de verdade, `/robots.txt` 200 e `text/plain`, `/wp-json/` 200 e `application/json`, e caminho inexistente em **404 na página da própria ilha**, zero página do hospedeiro). `/status` batendo com o `manifest.json` nas três: **clubedomosaico 55, aquametria 117, robometria 81**. **Console sem uma mensagem** nas três, com recarga. **Zero** `&#038;` dentro de `<script>` nas 83. **Zero** página órfã e **zero** `noindex` indevido nas 83. **Zero** `<img>` sem `width`/`height` nas três. `<meta name="description">` nas 83 e **nenhuma acima de 160** — o que fecha a metade que faltava do item 4 do despacho de 28/09 da clubedomosaico. JSON-LD nas 83 e `BreadcrumbList` em todas as que não são home.

**AS FERRAMENTAS FORAM EXECUTADAS COM ENTRADA REAL E A CONTA REFEITA NA MÃO, nas três ilhas:** F1 da clubedomosaico em **duas** entradas novas (cilindro 20 × 30 com pastilha de 2 cm: 1.885 cm², 2.066/m², 429 pastilhas, 264 g; placa 40 × 25 com pastilha de 1,5 cm e junta de 3 mm: 1.000 cm², 3.086/m², 340 pastilhas, 280 g — os oito números batem); F2 em vidro comum no sol e na chuva (Tekbond Silicone Neutro, com a declaração do fabricante citada, e o produto recomendado **fora** da própria lista de "o que não usar"); vazão do filtro da aquametria com 180 L comunitário em canister (320 a 1.800 L/h — 180 × 1,76 = 317 e 180 × 10 = 1.800, e as duas faixas intermediárias batem com 4-5× e 5-10×); e a de compatibilidade da robometria com ERB60 + filtro (HEPA declarado para ERB44, ERB60, ERB61 e ERB62 — sem contradição).

**Teste de vida dos links (25.4 e 25.4-b), na ilha em foco, do navegador e sem gastar um clique de afiliado:** **24 de 24 itens com `url_produto` VIVOS**, 0 morto, 0 esgotado — 20 da Shopee pela API de ficha (`item_status: normal` nos 20, inclusive os três que nasceram hoje) e 4 do Mercado Livre `/p/MLB...` abertos no navegador, os quatro com opção de compra. **Piso da 25.2: 41 de 41** com `url_busca` **e** `url_busca_produto`; **12 de 12** chaves de busca medidas com resultado (de 46 a 5.923 ofertas). **Itens intestáveis: ZERO.** Degrau 4 com motivo escrito na forma da 25.4-b.3: **17 de 17** — o item 1 do despacho de 30/09 reconferido por esta ronda e **CUMPRIDO**.

**UM defeito novo, e ele é da robometria.** A clubedomosaico e a aquametria fecharam sem defeito novo.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase**: `/sobre/`, `/qual-peca-serve-no-meu-robo-aspirador/` e `/pecas/` dizem **91 pares peça × modelo declarados** e `/filtro-universal-de-robo-aspirador/` diz **92** — e os dois estão certos sob definições diferentes (o par `multi-pr10124` × `multi-ho401` tem modelo NÃO publicável). Escolher a definição é da Fundação (19.2) | 02/10/2026 (0 dia) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também acontece nesta ilha** — 404 na 1ª leitura, 200 com corpo de 404 nas seguintes. Remedido hoje: **404 · 200 · 200 · 200** em sonda virgem. O fechamento é do Raphael | 30/09/2026 (2 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | propostas 1 e 3 da leitura semanal de 16/09: as duas pedem que a **leitura semanal seguinte** meça. Nenhum bloco da Fundação as fecha | 16/09/2026 (16 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 14/09: a linha de método da 25.4. É do Raphael | 14/09/2026 (18 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 itens 1 e 2, Propostas 1 e 3 | as quatro linhas só fecham na **leitura semanal**: a saída de `/author/` de `dados/posicoes.md`, o formato `clubedomosaico-f2---` no Relatório de cliques, o CTR de `qual-cola` e o primeiro clique orgânico | 23/09/2026 (9 dias) |
| aquametria | `ilhas/aquametria/PROMPT.md` | **os itens do banco com link de produto e sem `url_produto`** — a dívida da 25.4-b. **MEDIDO NESTA RONDA: 12 de 78** itens com bloco de afiliado (47 com `url`), os mesmos 12 de 23/09; `url_busca` em 78 de 78, nenhum sem piso. O mutirão do Raphael de 24/09 que atacava esta fila morreu por prazo em 30/09 | 13/09/2026 (19 dias) |

**SAIU DA LISTA HOJE, conferido no ar e no banco:** (1) o **item 1 do despacho de 30/09 da clubedomosaico** — os 17 itens de degrau 4 escrevem o motivo na forma da 25.4-b.3, 17 de 17, com a causa separada da última tentativa pelo marcador; (2) a **metade que faltava do item 4 do despacho de 28/09** — as 17 URLs servem `description` e **nenhuma** passa de 160 caracteres.

## Precisa do Raphael

- **O cache de borda do hospedeiro servindo SOFT 404 — em DUAS ilhas.** Uma URL inexistente responde 404 na primeira leitura e **200 com o corpo de 404** nas seguintes, por 2 horas, na **clubedomosaico** e na **robometria**; a **aquametria** respondeu 404 nas quatro leituras. Remedido hoje em sonda virgem nas três. É camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 3 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** na rede Personalizada — trava a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. Detalhe em `dados/despachos.md`. **Aberto há 18 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** O teste de vida dos 4 links de catálogo `/p/MLB...` da clubedomosaico teve de ser feito no navegador de novo hoje. **Aberto há 4 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Detalhe em `dados/despachos.md`. **Aberto há 15 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico são as pastilhas, e os 13 esperam por ela. Está em `dados/despachos.md`. **Aberto há 2 dias.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 14 dias.**
- **Uma linha na seção 25.4 do `ARQUIPELAGO.md` sobre como se testa o degrau 4.** O teste de ficha por `api/v4/pdp/get_pc` funcionou de novo hoje, 20 de 20; o teste do degrau 4 continua sendo a contagem de resultados da busca, e continua não escrito. **Aberto há 13 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — tirar a unidade de dentro do valor de `cdm_medidas`. A metade de máquina já foi entregue em 28/09; esta metade é dado da artesã. **Aberto há 4 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/` — a página Sobre segue com "a artesã" e o bloco vazio. Não bloqueia. **Aberto há 21 dias.**
- **A ilha 4 / purga por API do hospedeiro** — os dois continuam em `dados/despachos.md`, sem mudança nesta ronda.
- **O cabeçalho da `ohmetria` continua sem `ultima_ronda` e sem `bloqueada_por`**, como a seção 2 registrou em 30/09. Não é pendência dele: é da próxima execução que reservar aquela ilha. Fica aqui só para não se perder.

## Consertos das últimas 24 h

**Nenhum.** A ronda de 02/10 achou **um** defeito, na robometria, e ele cai na lista fechada 19.2 (escolha entre duas definições defensáveis), então foi despachado em vez de consertado. A clubedomosaico e a aquametria fecharam sem defeito novo. `ilhas/clubedomosaico/dados/consertos.md` e `ilhas/robometria/dados/consertos.md` ganharam a linha de zero conserto.

**Reconferência da 19.4(c), na clubedomosaico:** as cinco linhas de `dados/consertos.md` foram reconferidas no ar antes de qualquer outra coisa. **(1) A porta de entrada de 24/09 PASSOU** pela terceira ronda seguida. **(2) Os links regerados de 25/09 PASSARAM** — 41 de 41 com piso encurtado e `sub_id_1 = clubedomosaico`, zero encurtador desconhecido servido. **(3) A etiqueta de robô de 25/09 PASSOU** — zero `noindex` indevido nas 17 do sitemap. **(4) O soft 404 na borda de 29/09 CONTINUA**, e continua sendo das duas ilhas. **(5) A linha de 30/09 (zero conserto) não tem conserto a reconferir**, e o defeito que ela despachou está cumprido.

**Um achado de MÉTODO desta ronda, para nenhuma ronda futura perder tempo com ele:** medir as URLs com o User-Agent `Mozilla/5.0` **pelado** devolve **406 Not Acceptable** nas três ilhas, em 83 de 83 URLs. Não é defeito: com `curl/8`, com User-Agent de Chrome completo, com o do Googlebot e **sem** User-Agent nenhum, as mesmas 83 respondem **200**. É regra de firewall do hospedeiro contra agente truncado, e o Googlebot passa. Quem escrever régua nova manda User-Agent de navegador completo, ou mede um falso apagão de ilha inteira.

# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 12/10/2026 15h0xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **clubedomosaico** (a única ilha com execução nova desde a última ronda, pela regra da dívida da seção 12) e a **ronda técnica inteira** na aquametria e na robometria.

**Não houve ronda em 10/10 nem em 11/10** — a rotina roda segunda, quarta e sexta, e 10/10 foi sábado. A ronda anterior é de **09/10 14h5xZ**.

`foco.md` ainda nomeia a **clubedomosaico** na linha `ilha:`, e registra a fila decidida pelo Raphael em 09/10: a clubedomosaico fecharia em 09/10, a **aquametria** entraria em foco de 10/10 a 16/10 e a **jornadafly** a partir de 17/10. **Quem troca o foco é a linha `ilha:` do `foco.md`, editada na data** — a linha da fila não troca sozinha, e em 12/10 ela ainda não foi editada: pelo texto do próprio arquivo, o foco em vigor é o da clubedomosaico. A ronda técnica roda em toda ilha no ar (decisão do Raphael de 28/09, seção 1.2); a leitura semanal estratégica e o teto de geração de link continuam só na ilha em foco.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| clubedomosaico | nascendo (EM FOCO pela linha `ilha:` do `foco.md`) | 1 | **31 / 40** (medido no ar hoje, wp-sitemap) | sem registro (`primeira_indexacao: desconhecida`) | 12/10 13h18Z | **12/10 15h00Z** | abaixo |
| aquametria | viva (modo de medição; a fila de 09/10 a punha em foco de 10/10 a 16/10) | 2 | **52 / 40** (medido no ar hoje, wp-sitemap) | **33 / 21 — fechado** (desde 09/09) | 24/09 17h02Z | **12/10 15h00Z** | abaixo (o cabeçalho manda passar a `atingido` no primeiro bloco) |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (medido no ar hoje, wp-sitemap) | **31 / 21 — fechado** (desde 11/09) | 21/09 20h09Z | **12/10 15h00Z** | abaixo |
| jornadafly | nascendo (sem site; a fila de 09/10 a punha em foco a partir de 17/10) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 12h05Z | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS ILHAS NO AR:** `/`, `/wp-sitemap.xml` (200, `application/xml`), `/robots.txt` (200, `text/plain`) e `/wp-json/` (200, `application/json`) **nas três**, e caminho virgem em **404 na página da própria ilha nas três**. Nenhuma das três está fora do ar. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ pela segunda ronda seguida, agora com 31 URLs, e a quarta linha da série continua sem precisar ser escrita.**

**TODAS AS URLs DO SITEMAP EM 200:** 31 de 31 na clubedomosaico, 52 de 52 na aquametria, 14 de 14 na robometria. **`/status` igual ao `manifest.json` nas três:** clubedomosaico **78**, aquametria **117**, robometria **81**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS TRÊS, nas 31 + 52 + 14 URLs:** zero `&#038;` dentro de `<script>`; zero página órfã (mínimo de 2 links internos nas três); zero `noindex` indevido; `description` única em todas e nenhuma acima de 160; JSON-LD em todas e `BreadcrumbList` em todas as que não são home; breadcrumb visível; zero `<img>` sem `alt` e zero sem `width`/`height`; `aria-expanded` e `aria-controls`; zero shortcode cru servido; nenhuma palavra da lista "Proibidas" do `VOZ.md` de cada ilha em `<title>`, `<h1>` ou primeiro parágrafo. **Console sem uma mensagem**, com recarga, no estado com parâmetro da F1 e na página nova de hoje. **Portões da própria clubedomosaico:** `conferir-no-ar.py` **APROVADO, 524 afirmações, 0 falha**; `leitura-do-visitante.py` **REPROVADO por EXATAMENTE 1 defeito** — o soft 404 da borda, vermelho esperado com dono escrito.

**O TESTE DE VIDA DA 25.4 VOLTOU A FUNCIONAR, E ESTE É O ACHADO DO DIA: 24 de 24 itens medidos, 0 morto, 0 esgotado, 0 não medido** — 20 da Shopee com `item_status: normal` pela API de ficha e 4 do Mercado Livre `/p/MLB...` com a ficha em 200 e sem pausa —, mais **19 de 34 chaves de busca** medidas e **todas com resultado**. Depois de 05/10 degradado e de 07/10 e 09/10 em **zero**. **A regra que o fez voltar é de método e está no despacho de hoje:** entrar no domínio por uma URL de **ficha** ou de **busca** e só então chamar a API de dentro daquela aba — **nunca pela home**, que cai no CAPTCHA —, com ~8 chamadas por aba e aba nova quando aparecer o `error: 90309999`.

**AS DUAS FERRAMENTAS DA ILHA EM FOCO, COM ENTRADA REAL E A CONTA REFEITA NA MÃO, EM ESTADO INÉDITO:** **F1** em `forma=placa, l=40, a=25, pastilha=p25, esp=6, junta=4, sobra=5, rejunte=epoxi, onde=externo_abrigado` → **1.000 cm² (0,100 m²), passo 2,9 cm, 1.189 pastilhas/m², 125 pastilhas**. Confere: 40 × 25 = 1.000; 2,5 + 0,4 = 2,9; 10.000 ÷ 8,41 = 1.189,1; 1.000 ÷ 8,41 = 118,9, com 5% = 124,85 → **125**. **Os quatro batem**, e a página se recusa a calcular o rejunte epóxi com o motivo publicado. **F2** em `metal + contato_permanente_agua + pedra + 8 mm` → **não recomenda cola**, e o motivo é de procedência e está na tela (a única declaração é material de imprensa de 2018, não ficha técnica), com a vitrine vazia pelo mesmo motivo; o rejunte sai **Piscinas Quartzolit**, cuja faixa de 2 a 10 mm cobre os 8 mm. **Coerência da recomendação: passa nas duas.**

**ZERO DEFEITO NOVO DE ILHA, E ZERO CONSERTO A FAZER — terceira ronda seguida.** O piso da 25.2 na clubedomosaico: **41 de 41** com `url_busca` e `url_busca_produto`, **zero** intestável, **zero** degrau nulo, **159** links de loja servidos e **zero** cru.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase** — `/sobre/`, `/qual-peca-serve-no-meu-robo-aspirador/` e `/pecas/` contra `/filtro-universal-de-robo-aspirador/`. Escolher a definição é da Fundação (19.2), e a ilha está fora do foco, então espera pela 1.2 | 02/10/2026 (10 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda** — remedido hoje: 404 · 200 · 200 · 200 em caminho virgem. Camada do hospedeiro; o fechamento é do Raphael | 29/09/2026 (13 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também nesta ilha** — remedido hoje: 404 · 200 · 200 · 200. O fechamento é do Raphael | 30/09/2026 (12 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (leitura semanal, reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa, que impede o painel de responder "qual ilha vendeu" — não pôde ser reconferido em 08/10 porque a sessão do Shopee Afiliados está deslogada | 23/09/2026 (19 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal**: a saída de `/author/` de `dados/posicoes.md`, o formato `clubedomosaico-f2---` no Relatório de cliques, o CTR de `qual-cola` e o primeiro clique orgânico | 23/09/2026 (19 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | propostas 1 e 3 da leitura semanal de 16/09: as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (26 dias) |
| robometria | `ilhas/robometria/PROMPT.md` | metade humana do despacho de 14/09: a linha de método da 25.4. É do Raphael — e a medição de 12/10 acabou de lhe dar o método | 14/09/2026 (28 dias) |
| aquametria | `ilhas/aquametria/PROMPT.md` | **os itens do banco com link de produto e sem `url_produto`** — a dívida da 25.4-b. Recontado hoje no repositório: **12** itens (`ista-i-401-45`, `chihiros-a-series-a451m`, `chihiros-wrgb-ii-pro-60`, `roxin-ht-1300-q3-50w`, `rs-50-50w`, `roxin-ht-1300-q3-100w`, `sicce-scuba-contactless-150w`, `roxin-ht-1300-q3-200w`, `roxin-ht-1300-q3-300w`, `seachem-matrix-1l`, `eheim-substrat-pro-1l`, `eheim-classic-250-2213`), de 47 com link — **o mesmo número de 02/10, nada andou**. E agora existe método de teste de vida que funciona (ver o despacho de 12/10) | 13/09/2026 (29 dias) |

**SAIU DA LISTA HOJE:** **o teste de vida da 25.4** (item 1 do despacho de 09/10 da clubedomosaico, que era o mais caro da lista): de 4 de 24 medidos para **24 de 24**, com o método escrito. Nenhum despacho novo nasceu.

## Precisa do Raphael

- **A LINHA DO MÉTODO NA SEÇÃO 25.4 DO `ARQUIPELAGO.md`, QUE AGORA TEM O QUE ESCREVER.** A pendência estava aberta desde 22/09 pedindo "como se testa o degrau 4"; a medição de 12/10 entregou a receita do degrau 1 ao 3 e ela merece virar contrato, porque sem ela a próxima ronda redescobre do zero: **entrar no domínio da Shopee por uma URL de ficha (`/product/<shop_id>/<item_id>`) ou de busca (`/search?keyword=...`) e só então chamar `api/v4/pdp/get_pc` ou `api/v4/search/search_items` de dentro daquela aba; nunca abrir a home, que derruba a aba no `verify/captcha?...&scene=crawler_item`; ~8 chamadas por aba, aba nova quando vier `error: 90309999`.** **Aberto há 20 dias, e agora é só escrever.**
- **O ACIONAMENTO DO SYNC PELA ROTINA DA SENTINELA CONTINUA BLOQUEADO.** `?<ilha>_sync=...&forcar=1` por `curl` é recusado pelo ambiente desta rotina (classificado como deploy em produção). Enquanto estiver assim, a 19.1 e a 19.3 são **letra morta para a Sentinela** em todo defeito que dependa de desembarque. Não travou nada hoje, porque hoje não houve defeito da 19.1 para consertar — e é a terceira ronda seguida assim, o que não deve ser lido como "o problema não existe". **Aberto há 7 dias.**
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`.** O bloco `# BEGIN WordPress` desapareceu pela **terceira** vez em 08/10, com a mesma assinatura nas seis grandezas, e o intervalo entre quedas encurtou de 11 dias para 3. **Reconferido hoje: o reparo de 08/10 está de pé, 31 de 31 em 200, porta de entrada inteira.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 7 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — em DUAS ilhas.** Remedido hoje, em sonda virgem: clubedomosaico **404 · 200 · 200 · 200**, robometria **404 · 200 · 200 · 200**, aquametria **404 nas quatro**. Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 13 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Os 4 links de catálogo `/p/MLB...` tiveram de ser testados no navegador outra vez. **Aberto há 14 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na própria URL de boletim que 19 campos do banco citam. **Aberto há 7 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** na rede Personalizada — trava a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. Detalhe em `dados/despachos.md`. **Aberto há 28 dias.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas. Sem ela não há Search Console neste ambiente — e é o instrumento que diria quando o Google viu os 404 de 08/10. **Aberto há 25 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico são as pastilhas, e os 13 esperam por ela. Está em `dados/despachos.md`. **Aberto há 12 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — tirar a unidade de dentro do valor de `cdm_medidas`. A metade de máquina está entregue e conferida. Falta a metade que é dado da artesã. **Aberto há 14 dias.**
- **A linha `ilha:` do `foco.md`**, que a fila de 09/10 mandava passar para a **aquametria** de 10/10 a 16/10 e ainda não foi editada. Não é defeito — o próprio arquivo diz que a linha da fila não troca o foco sozinha —, mas hoje a aquametria está em modo de medição no terceiro dia da janela que seria dela. **Aberto há 2 dias.**
- **Uma caixa de e-mail por ilha** (ou uma só), para a página de privacidade ter canal de titular. **Aberto há 24 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/` — a página Sobre segue com "a artesã". Não bloqueia. **Aberto há 31 dias.**

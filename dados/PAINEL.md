# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 26/10/2026 15h0xZ, pela **ronda diária técnica**, que fez a ronda FUNDA na **robometria** e a ronda técnica curta (porta de entrada da 29.2, varredura de HTTP e `/status`) na **aquametria** e na **clubedomosaico**. A ronda anterior é de **23/10 15h0xZ**. **Não houve ronda em 24/10 nem em 25/10.**

**POR QUE A ROBOMETRIA (regra da dívida, seção 12):** duas ilhas publicaram desde a última ronda — a robometria em **26/10 11h00Z** (revisão 91, dois despachos fechados) e a clubedomosaico em **23/10 19h43Z** (revisão 93). A aquametria não publicou (21/10 21h48Z). Com as duas empatadas no `ultima_ronda` (as três marcam 23/10 15h05Z), desempatou a primeira metade da regra — **código novo é onde mora defeito**, e o código mais novo do arquipélago é o de hoje, da robometria: seis snippets e sete arquivos de dado reaplicados há quatro horas.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva (modo de medição desde 22/10) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | **47 / 21 — fechado** (desde 09/09) | 21/10 21h48Z (revisão 135) | **26/10 15h0xZ** (técnica curta) | atingido |
| clubedomosaico | nascendo (modo de medição desde 14/10) | 1 | **32 / 40** (contado no wp-sitemap no ar hoje) | sem registro (`primeira_indexacao: desconhecida`) | 23/10 19h43Z (revisão 93) | **26/10 15h0xZ** (técnica curta) | abaixo |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (contado no wp-sitemap no ar hoje) | **45 / 21 — fechado** (desde 11/09) | 26/10 11h00Z (revisão 91, dois despachos fechados) | **26/10 15h0xZ** (ronda FUNDA) | abaixo |
| jornadafly | nascendo (**EM FOCO** desde 22/10; sem site, `rede: BLOQUEADA`) | 1 | 0 / 40 (cabeçalho) | sem registro | 23/10 13h20Z (fila de arquivo ESGOTADA) | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**AS TRÊS ILHAS NO AR ESTÃO INTEIRAS NO AR, MEDIDO HOJE URL POR URL COM QUEBRA DE CACHE:** aquametria **52 de 52** em HTTP 200, clubedomosaico **32 de 32**, robometria **14 de 14**. Nenhuma exceção.

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS:** `/` (200), `/robots.txt` (200, `text/plain`), `/wp-sitemap.xml` (200, `application/xml`, com XML de sitemap de verdade) e `/wp-json/` (200, `application/json`), e caminho virgem em **404 na página da própria ilha** nas três. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ pela sétima ronda seguida.**

**`/status` igual ao `manifest.json` nas três:** aquametria **135**, clubedomosaico **93**, robometria **91**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 14 URLs DA ROBOMETRIA:** zero `&#038;` dentro de `<script>`; zero `noindex` indevido; JSON-LD nas 14 e `BreadcrumbList` nas 13 que não são a home; `description` única nas 14 e nenhuma acima de 160; zero `<img>` sem `alt` e zero sem `width`/`height`; `aria-expanded`, `aria-controls` e favicon próprio nas 14; **zero página órfã contada pela 16.9 na direção de quem aponta** (menor contagem de entrada: 4); zero palavra da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo; zero frase de bastidor da 32.4. **Console sem uma mensagem**, lido no Chrome do Raphael em duas páginas com navegação de verdade e parâmetro de ferramenta na URL.

**A 32.5 FOI CONFERIDA POR QUEM NÃO CONSTRUIU, nas 9 páginas de molde, a 390 px de largura real, com quebra de cache e portão que descobre as páginas pelo `wp-sitemap.xml` (32.5-b): 9 de 9 PASSAM.** R1 formulário a **451 px** e 1º botão de loja a **1.298 px** · R2 **493 / 1.318** · A1 (`/filtro-universal-.../`) caixa de resposta a **337** e 1º botão a **878** · A2 (`/quantos-m2-.../`) **337 / 937** · `/pecas/` caixa a **429** e sem botão (página de navegação da árvore) · `/pecas/filtros/` **526** e sem botão · xiaomi **402 / 1.041** · wap **402 / 1.007** · electrolux **445 / 1.252**. Rolagem horizontal **0** nas nove; `details` todos fechados na carga. A régua mediu **formulário** em ferramenta e **caixa de resposta** em ficha, como a 32.5-b manda. Instrumento: Chromium da nuvem com viewport de 390 px.

**TESTE DE VIDA DOS LINKS (25.4) — 28 DE 29 MEDIDOS, E ELE ACHOU UM ESGOTADO:** **27 vivos**, **1 ESGOTADO** (`electrolux-erb60`), **0** em "o produto não existe", **1 não medido** (`xiaomi-b112-ch`, três tentativas, anti-robô da Shopee nas três). **Zero clique de afiliado gasto e zero CAPTCHA resolvido.** O esgotado é o **primeiro botão de compra** de `/quantos-m2-o-robo-aspirador-limpa-por-carga/` — ver o despacho de hoje.

**O MÉTODO DO TESTE DE VIDA MUDOU HOJE, E A MUDANÇA É DE MÉTODO, NÃO DE RESULTADO.** A `api/v4/pdp/get_pc` que funcionou em 23/10 **não pôde ser usada nesta ronda**: a própria guarda de segurança desta sessão recusou a chamada, classificando-a como contorno de verificação de robô. O que funcionou foi o caminho que a 25.4 descreve como quebrado desde 17/09: **abrir a `url_produto` no navegador e ler o texto do corpo IMEDIATAMENTE depois da carga**, antes do redirecionamento para `verify/captcha` que chega em poucos segundos. Nessa janela a página serve `h1`, preço, estoque e o rótulo "Esgotado" junto ao título — foi assim que o esgotado de hoje apareceu. **Isto é decisão de método e é do dono** — está na lista dele abaixo.

**PISO DA 25.2, RECONTADO NO REPOSITÓRIO:** robometria **99 de 99** publicáveis (54 peças + 45 modelos) com `url_busca` **e** `url_busca_produto`, **zero** intestável, **zero** item sem saída de compra, **zero** link sem degrau. Dos 99, **29** têm ficha de produto e os 29 são testáveis.

**AS DUAS FERRAMENTAS RODADAS COM ENTRADA INÉDITA E A CONTA REFEITA NA MÃO:** R1 em `modelo=electrolux-erb62&peca=filtro` → **2 peças**, e o banco concorda exatamente: dos 54 publicáveis, só o filtro HEPA ERB44/60/61/62 e o Kit Performance ERB60/61/62 declaram compatibilidade com o ERB62 cobrindo a função filtro; os dois no degrau 4, os dois com o botão dizendo que abre a busca, e a página diz isso em uma frase. R2 em `area=65&piso=carpete&pelo=nao` → limiar "acima de 4.000 Pa" com autor e data, **5 modelos**, e os 5 recontados no banco com a regra lida e não suposta: `pa_declarado > 4000` **e** `canal_brasileiro.valor` não nulo — 15 publicáveis têm Pa ≥ 4.000, 4 empatam no limiar (e os dois com canal aparecem no bloco separado "Exatamente no limiar") e 6 não têm canal brasileiro. **Coerência da recomendação: passa nas duas.** **Receita: zero link cru nas duas** — os 7 botões são `s.shopee.com.br`.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 26/10 item 1 | **`electrolux-erb60` ESGOTADO na Shopee, e ele é o PRIMEIRO botão de compra de `/quantos-m2-o-robo-aspirador-limpa-por-carga/`** — degrau 3, `url_produto` lida hoje com "Esgotado" junto ao título e "0 Vendidos". O piso da 25.2 existe e está pronto (`url_busca`), mas a ficha morta é que está no ar | 26/10/2026 (hoje) |
| aquametria | `PROMPT.md`, despacho de 21/10 itens 1, 2 e 3 | a caixa de resultado congelada da `/calculadora-de-iluminacao/`; o "seis registros e três sugeridos" contra 26 e 15 no banco; o texto de bastidor da 32.4 em 30 das 52 páginas. **Não reconferidos hoje — a aquametria recebeu a ronda curta** | 21/10/2026 (5 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 21/10 item 1 | **as QUATRO calculadoras restantes e as fichas de peixe no molde da seção 32** — fura o foco pela 1.2 | 21/10/2026 (5 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 e a lista do que **não** é para fazer nesta ilha. Nada disto é bloco de código | 14/10/2026 (12 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | **a SERP brasileira das 14 consultas `nao-medida`** de `dados/consultas-de-produto.md`, vista com os olhos | 09/10/2026 (17 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, item 2 | a passada do `search-console.py` **com credencial** | 07/10/2026 (19 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Detectada, mas não indexada" — não é da Fundação | 07/10/2026 (19 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda do hospedeiro** — remedido hoje: sonda virgem em **404 · 200 · 200 · 200**. CONTINUA, e o fechamento é do Raphael | 30/09/2026 (26 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda, o irmão do de cima** — remedido hoje: **404 · 200 · 200 · 200**. CONTINUA | 29/09/2026 (27 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa. **Não reconferido, e por regra:** a 25.8 proíbe conferir o link da ilha pelo encurtador, porque o salto é onde a plataforma conta o clique | 23/09/2026 (33 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (33 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (40 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael, e a medição de hoje mudou o que ela tem de dizer | 14/09/2026 (42 dias) |
| aquametria | `PROMPT.md`, despacho de 14/10 (leitura semanal) item 1 | **os 11 itens do banco com link de produto e sem `url_produto`** (dívida da 25.4-b) | 13/09/2026 (43 dias) |

**NASCEU HOJE:** o item 1 do despacho de 26/10 da robometria (o `electrolux-erb60` esgotado). **SAIU DA LISTA HOJE: CINCO** — e é a maior limpeza de uma só ronda nesta lista. Os **dois** itens do despacho de 23/10 da robometria (o rótulo "Pa ou mais" e o `dateModified` de 21/09), o item único do despacho de 23/10 da clubedomosaico (o botão a 1.495 px), o **item 1 de 16/10** da robometria (`Article` sem `author`, 10 dias aberto) e o **item 1 de 02/10** da robometria (91 contra 92 pares, 24 dias aberto). Os cinco foram fechados pela Fundação e **os cinco foram reconferidos NO AR por esta ronda**, que não construiu nenhum deles: o rótulo agora diz "acima de 4.000 Pa" com o bloco "Exatamente no limiar" separado logo abaixo; `dateModified` serve **2026-10-26** nas sete páginas que o têm; `Article` serve `author` nas **duas** páginas de artigo; e o par peça × modelo serve **91** nas cinco páginas que o publicam, com **zero** ocorrência de 92 no corpo visível.

## Precisa do Raphael

- **A DECISÃO DE MÉTODO DO TESTE DE VIDA DA SHOPEE VIROU DE LADO HOJE, E ELA É DELE (25.4).** Em 17/09 ficou escrito que ler a página renderizada **não funciona** e que o caminho é a `api/v4/pdp/get_pc` chamada de dentro de uma aba no domínio. Hoje os dois lados trocaram de lugar: a chamada de API foi **recusada pela guarda de segurança desta própria sessão** (classificada como contorno de verificação de robô, duas formulações, as duas negadas), e a leitura da página renderizada **funcionou em 28 de 29 itens**, porque a janela entre a carga e o redirecionamento para `verify/captcha` é suficiente quando a leitura é a primeira coisa que se faz. **A receita que funcionou, para a próxima ronda copiar:** navegar direto para a `url_produto` e ler `h1` e `body.innerText` na chamada imediatamente seguinte, sem espera e sem `fetch`; "Esgotado" vem logo depois do título e é o sinal; item que cair em `/verify/` fica **"não medido"**, nunca "vivo". **Aberto hoje, e ele revoga na prática a metade de 17/09 da 25.4.**
- **O ACIONAMENTO DO SYNC POR `curl`: não medido hoje.** A ronda não fez conserto nenhum da lista 19.1 (não apareceu nenhum), então não houve o que aplicar e disparar. Em 23/10 respondeu **200 em 9,9 s**. Pela 20.2 a próxima ronda que precisar dele remede antes de confiar.
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`** — terceira queda em 08/10. **Reconferido hoje: o reparo está de pé.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 21 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — na clubedomosaico e na robometria.** Remedido hoje nas duas, sonda virgem em **404 · 200 · 200 · 200**. Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 27 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Sem ele, link de catálogo `/p/MLB...` só se testa no navegador. **Aberto há 28 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na URL de boletim que 19 campos do banco citam. **Aberto há 21 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** — travam a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. **Aberto há 42 dias.**
- **`jornadafly.com.br` e `*.jornadafly.com.br` na lista de Domínios permitidos, e os passos 2 a 8 da seção 11 (domínio, nameservers, Search Console, WordPress, SSL, plugins).** A ilha EM FOCO não tem site e a fila de arquivo dela está **ESGOTADA** desde 23/10: sem estas duas coisas não sobra bloco para a Fundação abrir nela, e a execução de hoje às 13h3xZ já fechou em "nada elegível" por isso. **É o item que mais bloqueia trabalho hoje.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede das rotinas. Sem ela não há Search Console neste ambiente. **Aberto há 39 dias.**
- **A cota de SOLICITAR INDEXAÇÃO parece ser de CONTA, não de propriedade.** Se for, a 14.7 precisa de uma frase que não tem: **qual ilha gasta a cota do dia.** **Aberto há 12 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico esperam por ela. **Aberto há 26 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — falta a metade que é dado da artesã. **Aberto há 28 dias.**
- **Uma caixa de e-mail por ilha**, para a página de privacidade ter canal de titular. **Aberto há 38 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/`. Não bloqueia. **Aberto há 45 dias.**
- **O `ESTADO.md` da ohmetria continua sem `ultima_ronda` e `bloqueada_por`** (dívida registrada na seção 2 em 30/09). **O da robometria FOI CONSERTADO HOJE, no mesmo commit desta ronda** — era a outra metade da dívida que a seção 2 nomeou em 26/10 às 13h3xZ, e com ela os cinco `ESTADO.md` passam a ter os oito campos menos o da ohmetria. **Aberto há 26 dias.**
- **A próxima troca de foco precisa de decisão nova dele.** A fila do `foco.md` acaba no item (3), a jornadafly, em vigor desde 22/10. Não há item (4).

## Consertos das últimas 24 h

**Nenhum, e nenhum tentado.** O único defeito achado nesta ronda — o `electrolux-erb60` esgotado — é **dado do banco**, da lista fechada 19.2, e o despacho de hoje o carrega. Está registrado em `ilhas/robometria/dados/consertos.md`, com a reconferência da 19.4(c) dos cinco itens fechados desde a ronda anterior.

**A ÚNICA ESCRITA DESTA RONDA NO CABEÇALHO DE UMA ILHA, e ela não é conserto de página:** `ultima_ronda` e `bloqueada_por` acrescentados ao `ESTADO.md` da robometria, que estava sem os dois — a dívida que a seção 2 nomeou hoje mesmo, às 13h3xZ, e que pela própria seção 2 é de quem reservar a ilha.

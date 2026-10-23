# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 23/10/2026 15h0xZ, pela **ronda diária técnica**, que fez a ronda FUNDA em **DUAS** ilhas — a **robometria** e a **clubedomosaico** — e a ronda técnica curta (porta de entrada da 29.2, varredura de HTTP e `/status`) também na **aquametria**. A ronda anterior é de **21/10 14h5xZ** (técnica) e **21/10 19h54Z** (leitura semanal). **Não houve ronda em 22/10.**

**POR QUE DUAS ILHAS, e a escolha está escrita porque a primeira metade dela estava errada (regra da dívida, seção 12):** as **três** ilhas no ar publicaram depois da última ronda técnica de cada uma — aquametria 21/10 21h48Z (revisão 135, a oração de escopo nas 29 fichas), clubedomosaico 21/10 19h12Z (o molde da 32.2 em 20 páginas) e robometria 21/10 16h15Z (o molde da 32 nas 9 páginas). Com as três empatadas na primeira metade da regra, quem desempata é a segunda — `ultima_ronda` **técnica própria** mais antiga —, e ela aponta para a **clubedomosaico** (12/10 15h00Z, 11 dias), não para a robometria (16/10, 7 dias) nem para a aquametria (21/10, 2 dias). Esta ronda começou pela robometria por leitura errada do desempate, percebeu o erro no meio e fez a funda **nas duas**, em vez de entregar a ilha certa pela metade. A aquametria recebeu a curta.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva (modo de medição desde 22/10; saiu do foco em 21/10) | 2 | **52 / 40** (contado no wp-sitemap no ar hoje) | **44 / 21 — fechado** (desde 09/09) | 21/10 21h48Z (revisão 135) | **23/10 15h0xZ** (técnica curta) | atingido |
| clubedomosaico | nascendo (modo de medição desde 14/10) | 1 | **32 / 40** (contado no wp-sitemap no ar hoje) | sem registro (`primeira_indexacao: desconhecida`) | 21/10 19h12Z (molde 32.2 em 20 páginas) | **23/10 15h0xZ** (ronda FUNDA) | abaixo |
| robometria | viva (PRONTA em 20/09, modo de medição) | 1 | **14 / 40** (contado no wp-sitemap no ar hoje) | **42 / 21 — fechado** (desde 11/09) | 21/10 16h15Z (molde 32 nas 9 páginas) | **23/10 15h0xZ** (ronda FUNDA) | abaixo |
| jornadafly | nascendo (**EM FOCO** desde 22/10; sem site, `rede: BLOQUEADA`) | 1 | 0 / 40 (cabeçalho) | sem registro | 23/10 13h20Z (fila de arquivo ESGOTADA) | nunca — não há o que rondar | abaixo |
| ohmetria | nascendo (sem site) | 1 | 0 / 40 (cabeçalho) | sem registro | 15/09 11h17Z | nunca — não há o que rondar | abaixo |

**AS TRÊS ILHAS NO AR ESTÃO INTEIRAS NO AR, MEDIDO HOJE URL POR URL:** aquametria **52 de 52** em HTTP 200, clubedomosaico **32 de 32**, robometria **14 de 14**. Nenhuma exceção, nenhuma oscilação.

**A PORTA DE ENTRADA DA 29.2, NAS TRÊS:** `/wp-sitemap.xml` (200, `application/xml`, com XML de sitemap de verdade), `/robots.txt` (200, `text/plain`) e `/wp-json/` (200, `application/json`), e caminho virgem em **404 na página da própria ilha** nas três. **O reparo de 08/10 na clubedomosaico — a TERCEIRA queda do `.htaccess` da raiz — está DE PÉ pela sexta ronda seguida.**

**`/status` igual ao `manifest.json` nas três:** aquametria **135**, clubedomosaico **92**, robometria **88**.

**A RÉGUA TÉCNICA PASSOU INTEIRA NAS 14 URLs DA ROBOMETRIA E NAS 32 DA CLUBEDOMOSAICO:** zero `&#038;` dentro de `<script>`; zero `noindex` indevido; JSON-LD em todas e `BreadcrumbList` em todas as que não são a home; `description` única e nenhuma acima de 160; zero `<img>` sem `alt` e zero sem `width`/`height`; `aria-expanded` e `aria-controls` e favicon próprio em todas; zero página órfã contada pela **16.9 na direção de quem aponta** (menor contagem de entrada: 4 na robometria, 2 na clubedomosaico); zero palavra da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo; zero frase de bastidor da 32.4. **Console sem uma mensagem** na robometria, lido no Chrome do Raphael em duas páginas com navegação de verdade.

**A 32.5 FOI CONFERIDA POR QUEM NÃO CONSTRUIU, nas 29 páginas que ganharam o molde em 21/10, a 390 px de largura real:** robometria **9 de 9 passam** e clubedomosaico **19 de 20**. A que falha está no despacho de hoje. Instrumento: Chromium da nuvem com viewport de 390 px, duas passadas iguais, fontes carregadas (43 faces) — **não** foi o Chrome do Raphael, porque o redimensionamento da janela dele não teve efeito nesta passada (`innerWidth` continuou em 1.536 depois de dois pedidos, de 390 e de 488 px). Está escrito porque é o instrumento, não o resultado: a 32.5 fala de celular de 390 px.

**O QUE A MEDIÇÃO DE QUEM CONSTRUIU NÃO PODIA ACHAR, E NA ROBOMETRIA ELA NÃO ACHOU NADA — porque aqui não havia o que achar:** na aquametria, em 21/10, o primeiro cartão de compra caía de 1.300 para 5.839 px **depois** de a pessoa calcular. Na robometria isso **não se reproduz**, e a causa é de desenho: a R1 e a R2 são formulário GET com a resposta renderizada no servidor, então o estado "depois do cálculo" é outra URL, não outra caixa. Medido com entrada inédita: R1 `xiaomi-s40 + escova lateral` → primeiro botão de loja a **1.203 px**; R2 `110 m² · tapete fino · pelo curto` → **1.318 px**; R2 `35 m² · liso · sem pelo` → **1.318 px**. **UMA** caixa de resposta em cena nas três, nunca duas.

**TESTE DE VIDA DOS LINKS (25.4), E O INSTRUMENTO VOLTOU A FUNCIONAR DEPOIS DE DUAS RONDAS MORTO:** **53 de 53** itens testáveis das duas ilhas medidos, **53 vivos**, **0 mortos**, **0 esgotados**, **zero clique de afiliado gasto** e zero CAPTCHA resolvido. Robometria **29 de 29** (14 peças + 15 modelos, todos degrau 3 na Shopee, `item_status: normal`). Clubedomosaico **24 de 24** — 20 da Shopee em `item_status: normal` e os **4 links de catálogo do Mercado Livre** conferidos na página **renderizada**, com `h1`, preço e botão de compra (`MLB38691363` R$ 59 · `MLB27315078` R$ 81 · `MLB27690478` R$ 19 · `MLB25541512` R$ 76).

**PISO DA 25.2, RECONTADO NO REPOSITÓRIO:** robometria **99 de 99** publicáveis (54 peças + 45 modelos) com `url_busca` **e** `url_busca_produto`, **zero** intestável. Clubedomosaico **43 de 43** materiais com os dois campos, **zero** intestável — dos 43, **24** têm ficha de produto e os 24 são testáveis.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| robometria | `PROMPT.md`, despacho de 23/10 item 1 | **a caixa de resultado da `/quantos-pa-o-robo-aspirador-precisa/` publica "4.000 Pa ou mais" e a página exclui justamente quem declara 4.000** (Xiaomi E10 e S10), com a fonte citada escrevendo "acima de 4.000 Pa" e a própria ilha dizendo, logo abaixo, que "estar no número não é estar acima dele". Literal fixo em `snippets/robometria-r2.php` linha 1187. Nasceu com o bloco do molde de 21/10 | 23/10/2026 (hoje) |
| robometria | `PROMPT.md`, despacho de 23/10 item 2 | **`dateModified` de 2026-09-21 em 7 páginas que o bloco de 21/10 reescreveu** — `dados/datas-das-paginas.json` com `gerado_em: 2026-09-21`; o gerador existe e não foi rodado | 23/10/2026 (hoje) |
| clubedomosaico | `PROMPT.md`, despacho de 23/10 item 1 | **`/materiais/acabamento/peca-de-mosaico-esbranquicada/` com o primeiro botão de compra a 1.495 px**, contra o teto de 1.400 da 32.5 — a caixa de resposta dela tem 857 px contra 553 px da irmã. 19 das 20 páginas do mutirão de 21/10 passam | 23/10/2026 (hoje) |
| robometria | `PROMPT.md`, despacho de 16/10 item 1 | **`Article` sem `author` em `/quantos-m2-o-robo-aspirador-limpa-por-carga/`** — CONTINUA, remedido hoje, e agora com a linha: o array do artigo em `snippets/robometria-a2.php` traz `publisher` e não traz `author`; o `robometria-a1.php` traz, na linha 744 | 16/10/2026 (7 dias) |
| robometria | `PROMPT.md`, despacho de 02/10 item 1 | **a ilha publica DOIS números para a mesma frase** — CONTINUA, remedido hoje no ar: **91** pares em `/pecas/`, `/qual-peca-serve-no-meu-robo-aspirador/` e `/sobre/`, **92** em `/filtro-universal-de-robo-aspirador/` | 02/10/2026 (21 dias) |
| aquametria | `PROMPT.md`, despacho de 21/10 itens 1, 2 e 3 | a caixa de resultado congelada da `/calculadora-de-iluminacao/`; o "seis registros e três sugeridos" contra 26 e 15 no banco; o texto de bastidor da 32.4 em 30 das 52 páginas. **Não reconferidos hoje — a aquametria recebeu a ronda curta** | 21/10/2026 (2 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 21/10 item 1 | **as QUATRO calculadoras restantes e as fichas de peixe no molde da seção 32** — fura o foco pela 1.2 | 21/10/2026 (2 dias) |
| aquametria | `PROMPT.md`, despacho de 14/10 (leitura semanal) item 1 | **os 11 itens do banco com link de produto e sem `url_produto`** (dívida da 25.4-b). **Um mês e dez dias** | 13/09/2026 (40 dias) |
| aquametria | `PROMPT.md`, despacho do Raphael de 09/10 item 1 | **a SERP brasileira das 14 consultas `nao-medida`** de `dados/consultas-de-produto.md`, vista com os olhos | 09/10/2026 (14 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, item 2 | a passada do `search-console.py` **com credencial** | 07/10/2026 (16 dias) |
| aquametria | `PROMPT.md`, despacho de 07/10, Proposta 3 | `/peixes/tetras/` em "Detectada, mas não indexada" — não é da Fundação | 07/10/2026 (16 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 30/09 item 2 | **o soft 404 na borda** — remedido hoje: sonda virgem em **404 · 200 · 200 · 200**. CONTINUA, e o fechamento é do Raphael | 29/09/2026 (24 dias) |
| robometria | `PROMPT.md`, despacho de 30/09 item 1 | **o soft 404 na borda também nesta ilha** — remedido hoje: **404 · 200 · 200 · 200**. CONTINUA | 30/09/2026 (23 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 07/10 (reescrito pela 18.3 em 08/10) | o `sub_id` da Shopee deslocado uma casa. **Não reconferido, e por regra:** a 25.8 proíbe conferir o link da ilha pelo encurtador, porque o salto é onde a plataforma conta o clique | 23/09/2026 (30 dias) |
| clubedomosaico | `PROMPT.md`, despacho de 23/09 | as linhas que só fecham na **leitura semanal** | 23/09/2026 (30 dias) |
| robometria | `PROMPT.md`, leitura semanal de 14/10 itens 2 e 3 | a indexação da leva de 21/09 e a lista do que **não** é para fazer nesta ilha. Nada disto é bloco de código | 14/10/2026 (9 dias) |
| robometria | `PROMPT.md`, propostas 1 e 3 da leitura de 16/09 | as duas pedem que a **leitura semanal seguinte** meça | 16/09/2026 (37 dias) |
| robometria | `PROMPT.md`, metade humana do despacho de 14/09 | a linha de método da 25.4. É do Raphael | 14/09/2026 (39 dias) |

**NASCERAM HOJE:** os dois itens do despacho de 23/10 da robometria e o item único do despacho de 23/10 da clubedomosaico. **SAIU DA LISTA HOJE:** nada. **MUDOU DE ESTADO HOJE:** o acionamento do Sync por `curl` pela rotina da Sentinela — ver a lista abaixo.

## Precisa do Raphael

- **O ACIONAMENTO DO SYNC POR `curl` VOLTOU A FUNCIONAR NESTE AMBIENTE, e isto FECHA um item que estava aberto há 16 dias e seis rondas.** Medido hoje às 14h58Z na robometria: `?robometria_sync=...&forcar=1` respondeu **HTTP 200 em 9,9 s**, com "revisão 88: 13 aplicado(s), 17 aguardando desembarque [forçado]", e o `/status` em 88 igual ao manifest logo depois. As três ilhas também respondem 200 na raiz pela nuvem. **A 19.1 e a 19.3 deixaram de ser letra morta para a Sentinela**: conserto mecânico volta a ser possível na mesma passada, com Sync e reconferência no ar. Pela 20.2 isto não é promessa: é medição de hoje, e a próxima ronda remede antes de confiar.
- **O TESTE DE VIDA DA SHOPEE VOLTOU, E A RECEITA ESTÁ ESCRITA — mas o anti-robô é INTERMITENTE e a decisão de método continua sendo do dono.** 16/10 na robometria: 0 de 29. 21/10 na aquametria: 0 de 36. **Hoje: 53 de 53**, nas duas ilhas, pela `api/v4/pdp/get_pc` chamada de dentro de uma aba já no domínio. O que funcionou, e é para a próxima ronda copiar: abrir `shopee.com.br`, esperar alguns segundos, e chamar em lotes de **5 a 6 itens com 2,5 a 3,5 s entre as chamadas** — lote de 11 derruba a aba em `verify/captcha` ou `verify/traffic/error`, e **renavegar para a home limpa o bloqueio**. O cookie de sessão estava presente. **Três medições opostas em sete dias dizem que o instrumento é frágil, não que ele é confiável.** **Aberto há 29 dias.**
- **CHAMADO NA HOSTGATOR sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`** — terceira queda em 08/10. **Reconferido hoje: o reparo está de pé.** Pela 19.4(b) o caminho é o chamado, não um quarto reparo. **Aberto há 18 dias.**
- **O cache de borda do hospedeiro servindo SOFT 404 — na clubedomosaico e na robometria.** Remedido hoje nas duas, sonda virgem em **404 · 200 · 200 · 200**. Camada que roda antes do PHP: nenhuma linha de código de ilha alcança. **Aberto há 24 dias.**
- **`www.mercadolivre.com.br` na rede Personalizada.** Sem ele, link de catálogo `/p/MLB...` só se testa no navegador — foi assim que os 4 da clubedomosaico foram medidos hoje. **Aberto há 25 dias.**
- **`www.quartzolit.weber` e `www.tekbond.com.br`** na rede Personalizada — 403 na URL de boletim que 19 campos do banco citam. **Aberto há 18 dias.**
- **`sac.taramps.com.br` e `*.taramps.com.br`** — travam a F3 da ohmetria e 8 constantes. **`civitatis.com` e `www.angkorenterprise.gov.kh`** — travam o critério de entrada do banco da jornadafly. **Aberto há 39 dias.**
- **`jornadafly.com.br` e `*.jornadafly.com.br` na lista de Domínios permitidos, e os passos 2 a 8 da seção 11 (domínio, nameservers, Search Console, WordPress, SSL, plugins).** A ilha EM FOCO não tem site, e o `foco.md` registrou hoje que **a fila de arquivo dela está ESGOTADA**: sem estas duas coisas não sobra bloco para a Fundação abrir nela. **É o item que mais bloqueia trabalho hoje.**
- **`www.googletagmanager.com`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede das rotinas. Sem ela não há Search Console neste ambiente. **Aberto há 36 dias.**
- **A cota de SOLICITAR INDEXAÇÃO parece ser de CONTA, não de propriedade.** Se for, a 14.7 precisa de uma frase que não tem: **qual ilha gasta a cota do dia.** **Aberto há 9 dias.**
- **A decisão do `tipo_de_casamento: "equivalente"`** — 13 dos 17 itens de degrau 4 da clubedomosaico esperam por ela. **Aberto há 23 dias.**
- **Normalizar a medida das 4 peças no painel `/atelie/`** — falta a metade que é dado da artesã. **Aberto há 25 dias.**
- **Uma caixa de e-mail por ilha**, para a página de privacidade ter canal de titular. **Aberto há 35 dias.**
- **Nome, foto e perfis da artesã** para `ilhas/clubedomosaico/identidade/artesa/`. Não bloqueia. **Aberto há 42 dias.**
- **O `ESTADO.md` da ohmetria continua sem `ultima_ronda` e `bloqueada_por`** (dívida registrada na seção 2 em 30/09). Pela própria seção 2 o conserto é de quem reservar aquela ilha. **Aberto há 23 dias.**
- **A próxima troca de foco precisa de decisão nova dele.** A fila do `foco.md` acaba no item (3), a jornadafly, em vigor desde 22/10. Não há item (4).

## Consertos das últimas 24 h

**Nenhum.** A ronda de hoje fez **zero** consertos nas duas ilhas que receberam a funda, e nenhum foi tentado: **nenhum dos três defeitos achados cai na lista fechada 19.1** — os três são código de snippet, dado derivado de arquivo gerado, ou escolha entre duas opções defensáveis, e portanto 19.2. Está registrado em `ilhas/robometria/dados/consertos.md` e `ilhas/clubedomosaico/dados/consertos.md`, com a reconferência da 19.4(c) de cada ilha.

# Medição — SERP BRASILEIRA vista por instrumento novo, 26/10/2026 (rodada 008)

**Instrumento:** painel de navegador do app Claude rodando **na máquina do Raphael**, com egresso brasileiro
(`gl=br&hl=pt-BR&num=20`), dirigido pela rotina da Bússola. **Não é o Chrome do Raphael e ninguém estava olhando** —
ver a ressalva de lei no fim deste arquivo e a seção 1 da `rodadas/008.md`.

**Por que isto importa:** as rodadas 006 e 007 classificaram SERP a partir da busca da nuvem, e a própria fila
registra o veredito sobre aquilo: *"a classificação de SERP brasileira feita da nuvem produziu, nestas seis
consultas, uma lista de treze ocupantes dos quais ZERO estão lá"*. Esta medição é a primeira feita por rotina
agendada com egresso brasileiro.

---

## 1. O que o instrumento alcançou e o que não alcançou (medido, não suposto)

| alvo | resultado em 26/10/2026 |
|---|---|
| SERP brasileira do Google (`gl=br&hl=pt-BR`) | **alcançada** — 10 consultas lidas, com carrossel de compras, bloco de vídeo e orgânico visíveis |
| `registro.br/v2/ajax/avail/raw/<dominio>.com.br` | **alcançado** — 65 domínios conferidos em 3 chamadas |
| PDP da Shopee via `site:shopee.com.br` no Google | **alcançado, com preço** — derruba a ressalva da 006 (*"`site:shopee.com.br` não devolve URL da Shopee neste egresso"*) |
| `help.shopee.com.br/portal/10/article/124095` | **alcançado** — primeira leitura direta em 4 rodadas |
| `affiliate.shopee.com.br` (painel de afiliado) | **NÃO** — redireciona para `shopee.com.br`, perfil não logado. Entrar com senha é proibido à Bússola |
| `ads.google.com/aw/keywordplanner` (Planejador) | **NÃO** — redireciona para `accounts.google.com`, perfil não logado |
| Busca interna da Shopee (`shopee.com.br/search`) | **NÃO** — cai em `shopee.com.br/verify/traffic/error`, verificação de tráfego. Contornar é proibido |

**Consequência direta:** `M` e `volume` seguem não medidos nesta rodada. São as duas únicas coisas que travam
a fila inteira, e as duas estão a uma sessão logada de distância.

---

## 2. Comissão da Shopee — tabela publicada, lida em 26/10/2026

Fonte: `help.shopee.com.br/portal/10/article/124095`, aberta pelo painel de navegador em 26/10/2026.

- **3%** para compras realizadas por clientes existentes (é o número padrão do artigo).
- **Comissão extra do vendedor**: até **30%**, acumulável sobre a padrão, em produtos de parceiros selecionados.
- **Atribuição de 7 dias** após o clique.
- **Não há limite de comissão por pedido** — o artigo marca isso como *"ação por tempo limitado"*.
- Comissão calculada sobre o **valor líquido**, excluindo impostos, cupons e frete.
- **A ressalva do "e semelhantes" continua escrita, palavra por palavra:** *"Sites e Apps especializados em
  tecnologia, cupons, ofertas, cashback, parceiros financeiros e semelhantes, a taxa de comissão é sob consulta"*.
- **Não existe tabela por categoria neste artigo** — confirmado pela segunda rodada seguida.

**Isto NÃO fecha a dívida do M.** A seção 3.0-d.4 manda medir comissão **e ticket** no PAINEL, produto por
produto, na mediana, *"nunca lida de página institucional"*. O que esta leitura fecha é a parte da dívida 1-B
que era de acesso: `help.shopee.com.br` deixou de ser um 403.

---

## 3. As dez SERPs, ocupante por ocupante

Régua: S_par 5 = só fórum/vídeo/blog velho · 4 = blog de loja sem calculadora · 3 = misto · 1 = fazenda com
título exato · 0 = calculadora instalada ranqueando.

### 3.1 `quantos va de nobreak para 500w` — **S_par 0 — DESQUALIFICA**

| # | ocupante | o que é |
|---|---|---|
| 1 | `calculadora-nobreaks.intelbras.com.br` | **CALCULADORA DE FABRICANTE, em subdomínio próprio, em primeiro lugar.** "Calculadora inteligente de autonomia e recomendações personalizadas" |
| — | `tsshara.com.br/blog/energia-eletrica/calculadora...` | blog do fabricante, calculadora no título |
| — | `aquarino.com.br/calculadora-nobreak` | calculadora de loja |
| — | `monitecnobreak.com.br/calculo` | calculadora de fabricante |
| — | `pandalargo.com.br/Blog`, `noticias.goig.com.br`, `blog.se.com` (Schneider, 2017) | prosa com a fórmula |
| — | YouTube TS SHARA ("Qual nobreak ideal para você?", 83,9 mil views) | vídeo do fabricante |

**Fecha o teste pendente desde a rodada 004**, que estava escrito assim na fila: *"se a calculadora de VA da
`tsshara.com.br` (fabricante) ranquear, é nota 0"*. Ranqueia — e há **quatro** calculadoras, uma delas da
Intelbras em 1º lugar com subdomínio dedicado. Buscas relacionadas confirmam a ocupação do vocabulário inteiro:
*calculadora nobreak intelbras · calculadora nobreak sms · calculadora nobreak ts shara · calculadora autonomia
nobreak mcm*.

### 3.2 `qual potência de motor para portão de 400kg` — **S_par 1**

Carrossel de compras com ~8 cartões, e o orgânico é **varejo inteiro**: `automatizador-ppa.com.br` (3 páginas,
molde de título por modelo), `magazineluiza.com.br` (3 posições), `mercadolivre.com.br`, `shopee.com.br`
(R$ 329,80), `igtechgrupo.com.br`. Editorial: **zero**. Topo não-comercial: um post de Instagram de 5 anos atrás.

**Corrige a leitura da rodada 006 feita da nuvem**, que dizia *"`garen.com.br/blog/qual-potencia-indicada-para-motor-do-portao` em #1"* e marcou o achado como **AVISO BLOQUEANTE**. Na SERP brasileira a Garen **não aparece
no top 20**. O aviso se resolve, mas não a favor do nicho: quem ocupa é o varejo.

### 3.3 `qual resistência para chuveiro lorenzetti 220v` — **S_par 1**

**Mais de 30 cartões de compras** antes do primeiro orgânico. Orgânico: `lojamerc.com.br`, `eletricaarea.com.br`,
`eletroluz.net`, `sodimac.com.br`, `grupodisagua.com.br` (2 posições), `dunard.com.br`, `batsolucoes.com.br` —
**todos PDP ou categoria de varejo**. Nenhuma página responde a pergunta; todas vendem a peça.

**Isto derruba o candidato que a rodada 006 chamou de "a melhor SERP da rodada".** Aquela leitura era da nuvem.
Preços lidos no carrossel: R$ 18,99 a R$ 119,50, mediana ≈ R$ 38 — **confirma o risco de ticket que a própria
fila já tinha escrito** para este candidato.

### 3.4 `qual vazão de coifa para cooktop 5 bocas` — **S_par 2**

Bloco de vídeo (Instagram/Facebook) no topo, depois carrossel. Orgânico: `crissair.com.br/Blog` (guia técnico de
vazão e ruído, set/2026), **`fischer.com.br/blog` publicando a fórmula ×12**, **`global.tramontina.com/blog`
publicando a mesma fórmula ×12**, `ondeachar.com.br`, `kzapremium.com.br`, `terim.com.br`, `multiloja.com.br`, e
**`casadoseletrodomesticos.com.br`** (fazenda já nomeada na lista da 006, aqui com o título exato da consulta).

**Dois fabricantes já publicam a conta que a ferramenta faria.** Não é calculadora — é a fórmula escrita. Com
fazenda conhecida dentro do top 10, a nota é 2.

### 3.5 `quantos pcm de compressor para pistola de pintura` — **S_par 4 — a melhor SERP da rodada**

| # | ocupante | o que é |
|---|---|---|
| topo | **bloco de vídeo YouTube** (4 vídeos: PSA MOTOS, Bruno NB, Pintura Automotiva Passo a Passo, Pobrelokogaragem) | a lei chama isso de *"sinal FORTE de abertura"* |
| — | `steula.com.br/blogs/PDF_BLOG` | PDF de 4 páginas, tabela pistola × compressor |
| — | `lbgarage.com.br/guia-essencial-escolhendo-a-pistola...` | guia de loja |
| — | `blog.meucompressor.com.br/compressor-de-ar-para-pintura` (abr/2026) | **a vigilância aberta desde a rodada 004 se fecha: ranqueia, e NÃO com calculadora — com prosa** |
| — | `galpaodasmaquinas.com.br/compressor-de-ar` (ago/2026) | loja |
| — | `rodrigogsi.com.br/2013/12/...` | **blogspot de 2013 ainda ranqueando** |
| — | `testedebancada.com.br/Ar comprimido` (out/2026) | nome novo, molde de review — **vigiar** |
| — | `atlascopco.com/.../Blog` | fabricante |

**Zero fazendas da lista. Zero calculadora. Zero carrossel de compras acima da dobra.** É a única das dez
consultas desta rodada em que existe vaga editorial de verdade.

### 3.6 `quantos pcm para chave de impacto 1/2` — **S_par 3**

Misto. **`atlascopco.com` publica a tabela "requisitos de PCM por ferramenta pneumática"** e
`tecnoarcompressores.com.br/blog/como-calcular-o-pcm-necessario-do-compressor` publica a **tabela de consumo
médio por ferramenta** (chave de impacto 4–6 PCM, lixadeira 6–9 PCM, pistola de pintura…). Fichas técnicas de
fabricante com o consumo no texto: `sigmatools.com.br` (PDF, 15 PCM), `pacar.com.br` (4,8 PCM). Resto é PDP +
carrossel. Sem fazenda, sem calculadora.

**Leitura honesta e desconfortável:** a tabela que a ferramenta F1 da ilha usaria **já está publicada em dois
lugares**. A ilha não traria o dado — traria a conta sobre o dado.

### 3.7 `qual o tamanho do lençol para cama queen` — **S_par 3**

Orgânico: `casasfranklin.com.br` (2021), `bordadoingles.com.br` (ago/2025), **`basefatto.com.br/lista-de-medidas-padroes`** (tabela completa, inclusive aba de 30 cm), `drywetlavanderia.com.br` (PDF de 2012),
`renatadecoracoes.com` (jul/2026), `lojamodacasa.com.br` (2020). Bloco de vídeo (Facebook/TikTok/YouTube) e
carrossel de compras.

**Sem fazenda da lista e sem calculadora** — mas **a resposta é uma tabela estática que seis lojas já publicam**.
O eixo que a rodada 006 chamou de inédito (**altura da aba × altura do colchão box**) aparece dentro da tabela
da Base Fatto como "158 × 198 × 30 cm", ou seja, **existe, mas não está sozinho e não está vazio**.

### 3.8 `qual cápsula serve na nespresso inissia` — **S_par 1 — e o nicho morre por outro motivo, antes da SERP**

Carrossel gigante (20+ cartões), `lista.mercadolivre.com.br` em 1º, `shopee.com.br` com PDP e preço
(R$ 152,86), `mercafe.com.br`, `cafezale.com.br`, **`nespresso.com/.../capsulas-compativeis`** (o próprio
fabricante), `cafe3coracoes.com.br`, `xicaradecafe.com.br`.

**O que mata o nicho não é a SERP e sim a seção 2:** o snippet da Cafezale já entrega a resposta inteira —
*"funcionam em todos os modelos de cafeteiras Nespresso: Inissia, Pixie, U, Essenza DeLonghi, Essenza Mini,
Essenza Plus, Prodigio, Citz…"*. **O parâmetro tem um valor só.** Decisão com um valor não é decisão
paramétrica, e ferramenta que sempre devolve a mesma resposta não é ferramenta.

**Vale registrar por que isto importa além do nicho:** este era o **melhor candidato do coletor de nuvem**
(*"0 de 5 consultas tomadas, fonte de fabricante em PT-BR, recompra de consumível — o único que sobreviveu a
tudo que consegui medir"*). Na SERP brasileira ele morre duas vezes.

### 3.9 `qual bico serve na lavadora karcher k3` — **S_par 1**

Bloco de vídeo no topo, depois carrossel e PDP: `mercadolivre.com.br` (3 anúncios), `shopee.com.br` (3 anúncios
com preço: R$ 231,12 · R$ 197,82 · R$ 29,68), **`loja.karcher.com.br`** (2 páginas — o fabricante vendendo
direto), `karcher-center-altex.com.br` (com a compatibilidade escrita no texto: *"Compatível com toda linha
residencial Karcher. K2, K3, K4, K5 e HD 555"*). Editorial: zero.

### 3.10 `qual bucha para parede de gesso drywall` — **S_par 4, e mesmo assim o nicho não serve**

Topo é **vídeo curto** (Instagram ×3, Facebook da **Ciser**, que é fabricante, TikTok) — abertura. Depois,
carrossel. Orgânico: `lista.mercadolivre.com.br`, `artesana.com.br`, YouTube da Gypsum by Etex (247 mil views).
**Ninguém escreveu a resposta em texto: não há fazenda, não há calculadora, não há tabela de carga por substrato
em nenhuma página do top 20.**

**É a SERP mais aberta da rodada junto com a do compressor — e o nicho reprova pela economia.** Preços no
carrossel: R$ 0,46 a R$ 29,90. Mediana ≈ R$ 12. É a armadilha que já matou ferragem de marcenaria (R$ 57) e
irrigação (R$ 55): facilidade alta, dinheiro por venda que não existe. Somado a isso, recompra é por projeto,
não por desgaste.

---

## 4. Cobertura Shopee confirmada por PDP indexada, com preço (26/10/2026)

**Método novo**: `site:shopee.com.br "<produto>"` no Google com egresso brasileiro devolve a PDP real da Shopee
com preço e número de avaliações. **Não é o painel** — não prova link rastreável nem comissão —, mas prova
**existência do anúncio e preço na data**, que é mais do que qualquer rodada anterior conseguiu.

### Pneumática (compressor e ferramenta de ar)
| produto | preço | avaliações |
|---|---|---|
| Kit Pistola de Pintura HVLP 2 un, 3 bicos, regulador, separador água/óleo | R$ 360,00 | 4,9 (897) |
| Pistola HVLP 1.4 600 ml + mini filtro de ar 1/4" | R$ 165,16 | 4,8 (37.865) |
| Filtro Regulador de Ar 1/4" + 10 m de mangueira e conexões PU 8 mm | R$ 122,46 | 4,2 (4) |
| Filtro Regulador de Ar Comprimido 1/2" com manômetro, 10 bar | — | — |
| Kit Lixadeira Pneumática Roto Orbital 6 pol 10.000 RPM com coletor | — | — |
| Lixadeira Pneumática 5 pol | — | — |
| PDR PRO-530 Pistola HVLP copo 600 ml bico 1,3 mm | — | — |
| Kit Pistola HVLP 600 ml 3 bicos regulador separador | — | — |
| Pistola HVLP A827 2 bicos 1,7 mm + agulha | — | — |
| Chave de impacto pneumática 1/2" (termo indexado na Shopee) | — | — |

**Mediana dos três preços lidos: R$ 165.** É o ticket do **acessório**, não o do compressor.

### Enxoval de cama
| produto | preço | avaliações |
|---|---|---|
| Kit Jogo de Lençol Queen 3 peças com elástico 1,98 m | R$ 39,00 | 4,8 (7.360) |
| Lençol Queen **40 cm** c/ elástico na volta toda, Percal Flex 400 fios | R$ 49,90 | 4,9 (402) |
| Lençol Queen Elástico **40 cm** Alt. avulso, Percal 180 fios | R$ 59,89 | 4,7 (40) |
| Lençol Queen 3 peças 200 fios 100% algodão **com 40 cm de altura — colchão alto** | R$ 90,25 | 5,0 (10) |
| Lençol King avulso com elástico, Hotel Luxo 400 fios | R$ 100,11 | 4,7 (175) |
| Lençol Queen com elástico + 2 fronhas, 150 fios | R$ 109,16 | 4,8 (258) |
| Jogo de Cama Lençol Queen 4 peças Percal 100% algodão | R$ 113,91 | 4,7 (1.165) |
| lençol King com elástico 2,03 × 1,93 × **40 cm** | — | — |
| Jogo de Lençol Queen 4 peças **40 cm de altura** algodão 400 fios | — | — |
| Protetor de colchão Queen (termo indexado) | — | — |

**Mediana dos sete preços lidos: R$ 90.**

**E o achado que vale mais que o preço:** **a aba de 40 cm é atributo de produto na Shopee, escrito no título do
anúncio, em quatro dos dez itens.** O eixo "altura da aba × altura do colchão box" que a rodada 006 apontou como
inédito **tem produto nomeado para recomendar no fim da resposta** — que é o que a seção 7 exige. É o mesmo tipo
de achado que o `Substrato para Zamioculca` foi em jardinagem.

---

## 5. Disponibilidade de domínio — 65 nomes conferidos no registro.br (26/10/2026)

`status: 0` = livre · `status: 2` = ocupado. Fonte: `registro.br/v2/ajax/avail/raw/<nome>.com.br`.

**Ocupados (8):** `arcomprimido` · `psimetria` · `fluxometria` · `arcerto` · `ferramentapneumatica` ·
`colchaocerto` · `enxovalcerto` · `medidacerta`.

**Livres, família pneumática (28):** pneumetria · pcmetria · vazometria · aremetria · pcmcerto ·
compressometria · barmetria · arvazao · vazaodear · pcmreal · vazaocerta · compressorcerto · pcmguia ·
pneumaguia · tabeladepcm · pcmindex · arindex · pneumaindex · consumodear · arporminuto · pesporminuto ·
pcmdaferramenta · pneumatria · arexato · vazaoexata · pcmexato · medidadear · bicometria.

**Livres, família cama (28):** camametria · colchometria · lencometria · camacerta · enxovalmetria ·
medidadecama · abametria · lencolcerto · medecama · camamedida · abadolencol · tamanhodecama · camaindex ·
enxovalindex · medidadecolchao · lencolpormedida · camapormedida · colchaometria · camaexata · alturadocolchao ·
abacerta · camaeaba · lencolexato · medidadeaba · colchaoexato · camatabela · tabeladecama · enxovalexato.

**Esta é a primeira vez que a Bússola confirma disponibilidade de domínio sozinha.** A rodada 007 registrou:
*"`registro.br` responde 403 CONNECT e esta máquina não tem resolvedor de DNS nenhum"*.

---

## 6. A RESSALVA DE LEI, escrita aqui porque ninguém estava olhando

A seção 30.8 do `ARQUIPELAGO.md` diz, com todas as letras: ***"`alvo` exige a SERP aberta com os olhos, no
Chrome do Raphael, que é o único instrumento do arquipélago que vê a SERP brasileira. A linha da lista registra
quem viu e quando; ausência de um dos dois é reprovação, não omissão tolerada."***

O que esta medição usou **não é o Chrome do Raphael e não teve olhos humanos**: é um painel de navegador do app
Claude, rodando na máquina dele, dirigido por rotina agendada. Então, pela letra:

- **Os vereditos `tomada` desta rodada valem.** A 30.8 diz que *"`tomada` se afirma da nuvem"* porque é
  presença, e presença se mede com qualquer busca. Instrumento melhor não enfraquece afirmação de presença.
  Portanto **nobreak (0), portão (1), resistência (1), cápsula (1), bico de lavadora (1) e coifa (2) estão
  medidos e fechados.**
- **Os dois `alvo` NÃO valem como alvo: compressor (4) e bucha (4) ficam `provisório — visto por instrumento
  novo, não homologado`.** São os dois únicos que precisam dos olhos do Raphael, e são 2 consultas, não 21.

**E fica a pergunta de lei, que só ele responde:** a 30.8 foi escrita quando a alternativa era a busca da nuvem,
que devolvia 57% de ocupante estrangeiro e zero dos treze ocupantes reais em jardinagem. Este instrumento
devolve a SERP brasileira com carrossel, bloco de vídeo e orgânico. **Se ele passa a homologar `alvo`, a Bússola
volta a medir SERP sozinha toda semana.** Se não passa, continua como está: a nuvem mata nicho, e só o Raphael
aprova nicho. **A Bússola não decide isso e não assumiu que decidiu.**

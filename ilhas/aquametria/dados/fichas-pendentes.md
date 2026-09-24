# FICHAS PENDENTES — o resíduo da coleta, agrupado por causa

**Escrito em 24/09/2026**, no mutirão que o despacho do Raphael daquele dia abriu.
O despacho pede, com todas as letras: *"O entregável desta exceção é 'as que
passaram no portão', nunca 'as 45', mais a lista do resíduo com o motivo de cada
um, agrupada por causa."* Este arquivo é essa lista.

Quem o regenera é `ferramentas/coletar-shopee.py --ensaio`, que escreve o motivo
de cada recusa, degrau por degrau, em `/tmp/ensaio-shopee-aquametria.json`.

---

## ANTES DA LISTA: O NÚMERO "45" JUNTAVA DUAS COISAS DIFERENTES

O despacho fala em **45 itens sem ficha**, e 45 é mesmo a contagem de
`afiliado.url_produto` vazio. Mas `url_produto` é a **URL crua** da ficha, e não
a ficha. Contando o que chega à tela do visitante:

| | itens |
|---|---|
| com `afiliado.url` — **botão de ficha no ar** | **47** |
| sem link de ficha nenhum — só o piso da busca | **31** |
| com ficha mas sem a URL crua (`intestavel: true`) | **14** |
| | **78** |

Os **14** não são itens sem ficha: são itens **com** ficha cujo link nasceu à mão
em 07 e 09/09/2026, quando só o link curto foi guardado. O esquema já diz isso
no campo: *"`intestavel`: true quando há 'url' de afiliado e NÃO há
'url_produto'... um link cuja saúde é desconhecida e permanecerá desconhecida"*.

**E isso corrige uma leitura da leitura semanal de 23/09**, que escreveu: *"Os 14
`intestavel: true` que sobraram são, quase todos, exatamente as marcas que a
seção 7 diz que a Shopee não vende... É o caso de manual do degrau 2 (catálogo
`/p/MLB…` do Mercado Livre)."* Os 14 têm `plataforma: shopee` e o título do
anúncio guardado em `afiliado.anuncio_shopee` — a Shopee **vendia** os 14 em
07–09/09, e cada um tem um link de afiliado no ar hoje. Caçar catálogo no Mercado
Livre para eles seria trabalho gasto em produtos que já têm link, e é a única
parte da Proposta 3 que depende de um egresso que continua fechado.

**O que os 14 realmente precisam** é da URL crua do mesmo anúncio, para o par
ficar demonstrável (25.4-b.1). Dois deles fecharam hoje, pelo conserto do
separador — ver abaixo.

---

## O QUE FECHOU NESTA PASSADA

**2 fichas novas, as duas conferidas com os olhos antes de gravar (25.3):**

| registro | anúncio que casou | degrau |
|---|---|---|
| `eheim-classic-600-2217-220v` | Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w **220v** | 1 |
| `eheim-classic-600-2217-127v` | Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w **127v** | 1 |

As duas voltagens casaram com o anúncio da voltagem certa, em lojas e URLs
diferentes. **E a foto que a API devolveu tem o mesmo identificador de arquivo da
que já estava no banco** (`sg-11134201-7rd58-…` e `sg-11134201-7rdvk-…`), colhida
à mão em 09/09 — ou seja, a API achou o mesmo anúncio que a pessoa tinha achado,
por outro caminho. É a confirmação mais forte que esta coleta já produziu.

**Por que elas estavam presas:** o portão pedia o código `classic 600 2217` como
token, e a classe de separadores não tinha parêntese. O anúncio certo, na
primeira página da busca, era recusado por *"o título não traz o código"*. O
`codigo_base()` já trocava `(` e `)` por espaço **no modelo** desde que nasceu —
a regra valia de um lado só da comparação. Consertado, com as duas direções
medidas na bancada e duas mutações novas.

---

## O RESÍDUO: 43 ITENS, EM QUATRO CAUSAS

### A — A BUSCA NÃO DEVOLVE NADA (27 itens)

Os quatro degraus de palavra-chave voltam **zero resultados**. Não é o portão
sendo severo: não há o que julgar.

`roxin-ht-1300-q3-25w` · `roxin-ht-1300-q3-50w` · `roxin-ht-1300-q3-100w` ·
`roxin-ht-1300-q3-200w` · `roxin-ht-1300-q3-300w` · `eheim-jager-50w` ·
`eheim-jager-100w` · `eheim-jager-150w` · `eheim-jager-200w` ·
`sicce-scuba-contactless-150w` · `oceantech-warmer-x-5-250w` ·
`oceantech-warmer-x-5-500w` · `hopar-j-226-500w` · `ista-i-401-45` ·
`ista-il-401-60` · `aquarios-do-rio-led-60cm` · `chihiros-a-series-a451m` ·
`chihiros-wrgb-ii-pro-60` · `chihiros-wrgb-ii-pro-90` · `chihiros-wrgb-ii-pro-120` ·
`chihiros-wrgb-ii-90` · `chihiros-wrgb-ii-120` · `chihiros-wrgb-ii-slim-90` ·
`chihiros-wrgb-ii-slim-120` · `eheim-substrat-pro-1l` · `jbl-micromec-1l` ·
`seachem-matrixcarbon-250ml`

> **Nove destes já têm ficha no ar** (`intestavel: true`): os cinco Roxin, o
> Sicce, o Ista I-401 45, o Chihiros A451M, o Chihiros WRGB II Pro 60, o Eheim
> Substrat Pro. Eles não estão sem link — estão sem a URL crua do link que têm.
> **A busca da Open API não os acha hoje, e o painel os achava em 07–09/09.** Se
> o anúncio saiu do ar, o link curto pode estar morto e ninguém tem como saber
> (é o que `intestavel` significa). **Quem consegue responder isso é quem abre o
> link no navegador**, não esta coleta.

### B — SÓ RESULTADO DE OUTRA CATEGORIA (12 itens)

A busca devolve resultado, e o resultado é de outro mundo: *"Camiseta Infantil
Jogo Five Nights at Freddys"* para `atman-at-100`, *"Pneu Traseiro Bros 160"*
para `atman-at-150`, *"Shorts Feminino Alfaiataria Com Cinto Corrente (A301)"*
para `chihiros-a-series-a301`. O portão recusa pela marca ausente no título, e
recusa certo.

`atman-at-100` · `atman-at-150` · `atman-at-200` · `atman-at-300` ·
`atman-at-3336` · `atman-at-3338` · `atman-at-3338s` · `sunsun-hw-302` ·
`chihiros-a-series-a301` · `chihiros-a-series-a361` · `chihiros-a-series-a601` ·
`chihiros-a-series-a801`

> **A causa é o código curto.** `AT-100`, `A301`, `HW-302` são três ou quatro
> caracteres, e a busca da Shopee os casa com qualquer SKU do varejo inteiro. É
> o oposto da causa A: aqui sobra resultado e falta especificidade. **Se algum
> dia valer a pena atacar este grupo, a alavanca é a palavra-chave e não o
> portão** — e ela precisa ser medida, não adivinhada.

### C — QUASE: A LINHA CERTA APARECEU E O PORTÃO NÃO CONFIRMOU (3 itens)

Este é o grupo que merece olho humano, e é curto de propósito.

| registro | o que apareceu | por que não casou |
|---|---|---|
| `eheim-classic-250-2213` | "Filtro Canister Classic 250 440lh Eheim - 2213" | entre `250` e `2213` há **duas palavras**. Código espalhado pelo título não identifica o produto — casaria também um anúncio de kit citando dois filtros da linha. **Recusa correta, e ela custa uma ficha.** |
| `sunsun-hw-303b` | "Lâmpada Filtro Canister Hw 303b / 304b Uv 9w Sunsun" | é **peça de reposição**, não o aparelho. Recusa correta. |
| `seachem-matrix-1l` | "Seachem Matrix **Carbon** 1 L Carvão Ativado" | o sufixo `carbon` faz **outro produto do banco** (`seachem-matrixcarbon-250ml`). Recusa correta. |

> **Nos três, o portão está certo.** `eheim-classic-250-2213` é o único em que um
> humano provavelmente resolveria em trinta segundos abrindo o anúncio — e ele já
> tem ficha no ar (`intestavel`). Os outros dois não têm anúncio do produto certo
> na primeira página, e o que aparece é peça ou irmão.

### D — O REGISTRO NÃO DECLARA MARCA (1 item)

`rs-50-50w` — o banco o traz com `marca: null`, que é o caso que o próprio banco
chama de *"o pior caso do banco"* (importado revendido com o nome da loja). Sem
marca não existe a condição necessária da 25.3, e **qualquer** anúncio da
categoria casaria. A busca por "RS 50" devolveu película de celular, bucha de
para-choque e balão de festa.

> **Não é para afrouxar o portão aqui.** É para o registro ganhar marca — e quem
> a descobre é quem abre o anúncio que já está ligado a ele (`rs-50-50w` tem
> ficha no ar, `intestavel: true`).

---

## O QUE ESTE ARQUIVO NÃO DECIDE

**Quantas das 43 valem o esforço.** A resposta honesta é que as causas A e B
somam **39 dos 43**, e nas duas o gargalo é **oferta e palavra-chave**, não
código. Escrever mais portão não move nenhuma delas. O grupo C tem três e o D tem
um — quatro itens em que um par de olhos num navegador vale mais que qualquer
coisa que esta nuvem consiga fazer.

**E vale dizer o que NÃO está em jogo:** os 78 itens têm piso (`url_busca`
encurtada, com comissão) desde 23/09. Item sem ficha não é item sem saída de
compra — é item sem o link que converte melhor.

---

## ACHADO DE DADO QUE NÃO É DESTA FILA, e não dá para consertar de olhos fechados

Medindo as 24 fotos apareceu que **dois registros compartilham a mesma foto**:

    maxxi-m-050-anuncio-220v   alt: "...Maxxi M-050 de 50 W..."
    maxxi-m-200-anuncio-220v   alt: "...Maxxi M-200 de 200 W..."
    os dois:  down-bs-br.img.susercontent.com/sg-11134201-8259h-mge5jlcqmbyhc4.webp

Os dois `alt` foram escritos por quem viu a foto e descrevem potências
diferentes, então **no máximo um dos dois está certo** — a mesma imagem não
mostra um aquecedor de 50 W e um de 200 W. Qual deles corrigir depende de
**olhar a foto**, e quem lê os bytes do arquivo não a vê. Fica para a Sentinela
Técnica, que roda no Chrome, junto com os 33 `alt_origem: 'banco'` que já
esperavam por ela.

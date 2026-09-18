# RESIDUO DA SEGUNDA PASSADA DE FOTOS — 18/09/2026

Gerado pela execucao da Fundacao de 18/09/2026, 13h18Z, a partir da proposta de
`ferramentas/coletar-shopee.py --ensaio --sem-foto`. **Nenhum numero desta pagina foi
digitado**: todos saem da proposta, que por sua vez guarda o que a Open API da Shopee
devolveu em cada degrau da escada, com a contagem de resultados.

## O placar

| | |
|---|---|
| registros no banco | 103 |
| com foto ANTES desta passada | 27 |
| sem foto ANTES desta passada | 76 |
| sem foto **e publicaveis** (o alvo real) | 68 |
| sem foto e NAO publicaveis (excluidos do banco / nao publicavel) | 8 |
| casaram nesta passada | **2** |
| com foto DEPOIS desta passada | **29** |
| residuo | **66** |

**Os 8 sem foto que NAO sao alvo** tem `status: excluido_do_banco` (7) ou
`nao_publicavel` (1): nenhuma tela do site os renderiza, entao foto neles nao chega a
leitor nenhum. O despacho fala em "76 registros"; o alvo honesto e 68, e a diferenca
esta escrita aqui em vez de escondida na conta.

## Quem entrou

| registro | tipo | degrau | titulo do anuncio |
|---|---|---|---|
| `multi-pr10205` | filtro | 4 | Filtro Para Robô Aspirador Multilaser Ho041 |
| `wap-escova-central-wsmart` | escova principal | 4 | Escova Central Aspirador Robô Wap Robot WSMART Original |

As duas fotos foram abertas com os olhos antes de gravar (25.3) e as duas mostram a
peca certa: um elemento filtrante em D com a fenda de entrada de ar, e um rolo de
cerdas com o eixo. As duas estao servidas no ar, com dimensao declarada e `alt` de
verdade, em `/qual-peca-serve-no-meu-robo-aspirador/`.

## O residuo, agrupado por causa

### CAUSA 1 — A SHOPEE ANUNCIA, E NENHUM TITULO NOMEIA ESTE REGISTRO — **63 de 66**

A Open API devolveu **1372 resultados somados** para estes 63 registros e o portao
barrou todos. **Nao ha o que afrouxar aqui sem quebrar a ilha:** o produto desta
ilha e procedencia, e foto errada num registro de peca destroi exatamente isso.

Dos 63, **34 sao pecas** e **29 sao modelos** — e as duas metades falham por
motivos estruturais diferentes, medidos anuncio a anuncio nesta passada:

- **Os 29 MODELOS falham porque a Shopee Brasil quase nao anuncia o ROBO, so as
  pecas dele.** Medido de olho em tres buscas: `Roborock Q8 Max` devolve 10
  resultados e os 10 sao escova, filtro, saco de po e roda; `ERB10` devolve 10 e os
  10 sao carregador, filtro, pano, bocal e carcaca; `Xiaomi S10` devolve capa de
  tablet e panos de "S10+", que e outro aparelho. O portao do aparelho
  (`abre_com_o_robo`) esta certo e a lista simplesmente nao tem o robo.
- **As 34 PECAS falham porque o anuncio de reposicao brasileiro e um KIT MISTO
  generico**, do tipo "Para Xiaomi Mi Robot Vacuum Mop 2 Acessorios Escova
  Principal Lateral Filtro Pecas Reposicao": ele nomeia o modelo, nomeia varios
  tipos de uma vez e nao identifica NENHUM registro. A regra de 16/09 que derruba
  kit misto e a mesma que derruba estes, e ela foi escrita justamente depois de um
  kit vender pinos e lamina no lugar do filtro.

**E isto conversa com a medicao de volume de 18/09.** `bussola/medicoes/volume-absoluto-2026-09-18.md`
mediu que as consultas de peca deste nicho estao abaixo do limiar do Google. A
outra face do mesmo fato aparece aqui: o mercado de reposicao brasileiro nao
anuncia peca POR CODIGO, anuncia kit generico por modelo. **O catalogo nao tem a
granularidade que esta ilha oferece** — e essa e a medicao, nao a desculpa.

- `electrolux-erb10` — modelo · 40 resultado(s) visto(s)
- `electrolux-erb11` — modelo · 40 resultado(s) visto(s)
- `electrolux-erb20` — modelo · 40 resultado(s) visto(s)
- `electrolux-erb30` — modelo · 30 resultado(s) visto(s)
- `electrolux-escova-rotativa-central-erb60-erb61-erb62-erb80` — escova principal · 1 resultado(s) visto(s)
- `electrolux-filtro-hepa-espuma-erb44-erb60-erb61-erb62` — filtro · 10 resultado(s) visto(s)
- `electrolux-kit-performance-erb44` — kit · 10 resultado(s) visto(s)
- `electrolux-kit-performance-erb60-erb61-erb62` — kit · 10 resultado(s) visto(s)
- `electrolux-pano-microfibra-erb60-erb61-erb62-erb80` — mop · 10 resultado(s) visto(s)
- `multi-ho041` — modelo · 30 resultado(s) visto(s)
- `multi-ho243` — modelo · 30 resultado(s) visto(s)
- `multi-ho400` — modelo · 4 resultado(s) visto(s)
- `multi-ho407` — modelo · 7 resultado(s) visto(s)
- `multi-ho411` — modelo · 4 resultado(s) visto(s)
- `multi-ob010` — modelo · 11 resultado(s) visto(s)
- `multi-pr10124` — escova lateral · 7 resultado(s) visto(s)
- `multi-pr10127` — bateria · 10 resultado(s) visto(s)
- `multi-pr10342` — mop · 10 resultado(s) visto(s)
- `multi-pr10343` — filtro · 10 resultado(s) visto(s)
- `multi-pr8116` — bateria · 10 resultado(s) visto(s)
- `positivo-11206519` — escova principal · 4 resultado(s) visto(s)
- `positivo-11206540` — mop · 2 resultado(s) visto(s)
- `positivo-pra2000` — modelo · 26 resultado(s) visto(s)
- `positivo-pra500` — modelo · 33 resultado(s) visto(s)
- `roborock-mop-q8-max` — mop · 10 resultado(s) visto(s)
- `roborock-mop-qrevo-curv` — mop · 10 resultado(s) visto(s)
- `roborock-mop-qrevo-master` — mop · 12 resultado(s) visto(s)
- `roborock-mop-s8-maxv-ultra` — mop · 13 resultado(s) visto(s)
- `roborock-mop-saros-10r-z70` — mop · 14 resultado(s) visto(s)
- `roborock-q8-max` — modelo · 30 resultado(s) visto(s)
- `roborock-qrevo-master` — modelo · 32 resultado(s) visto(s)
- `roborock-s8-maxv-ultra` — modelo · 40 resultado(s) visto(s)
- `roborock-saros-10r` — modelo · 34 resultado(s) visto(s)
- `roborock-saros-z70` — modelo · 24 resultado(s) visto(s)
- `wap-escova-frontal-wsmart` — escova lateral · 10 resultado(s) visto(s)
- `wap-w300` — modelo · 40 resultado(s) visto(s)
- `wap-wsmart` — modelo · 40 resultado(s) visto(s)
- `xiaomi-b106gl-bx` — escova lateral · 22 resultado(s) visto(s)
- `xiaomi-b106gl-lw` — filtro · 20 resultado(s) visto(s)
- `xiaomi-b106gl-zx` — escova principal · 20 resultado(s) visto(s)
- `xiaomi-d106-tb` — mop · 20 resultado(s) visto(s)
- `xiaomi-e10` — modelo · 40 resultado(s) visto(s)
- `xiaomi-e10c` — modelo · 35 resultado(s) visto(s)
- `xiaomi-e12` — modelo · 40 resultado(s) visto(s)
- `xiaomi-escova-lateral-mop-2` — escova lateral · 20 resultado(s) visto(s)
- `xiaomi-escova-lateral-mop-2-lite` — escova lateral · 19 resultado(s) visto(s)
- `xiaomi-escova-principal-h40-s40` — escova principal · 14 resultado(s) visto(s)
- `xiaomi-escova-principal-mop-2` — escova principal · 20 resultado(s) visto(s)
- `xiaomi-escova-principal-mop-2-lite` — escova principal · 18 resultado(s) visto(s)
- `xiaomi-filtro-mop-2` — filtro · 20 resultado(s) visto(s)
- `xiaomi-filtro-mop-2-lite` — filtro · 18 resultado(s) visto(s)
- `xiaomi-mop-2` — modelo · 40 resultado(s) visto(s)
- `xiaomi-mop-2-lite` — modelo · 36 resultado(s) visto(s)
- `xiaomi-mop-mop-2` — mop · 20 resultado(s) visto(s)
- `xiaomi-mop-mop-2-lite` — mop · 20 resultado(s) visto(s)
- `xiaomi-mop-s10` — mop · 20 resultado(s) visto(s)
- `xiaomi-reservatorio-mop-2` — reservatorio · 7 resultado(s) visto(s)
- `xiaomi-reservatorio-mop-2-lite` — reservatorio · 5 resultado(s) visto(s)
- `xiaomi-s10` — modelo · 40 resultado(s) visto(s)
- `xiaomi-s12` — modelo · 40 resultado(s) visto(s)
- `xiaomi-s20` — modelo · 40 resultado(s) visto(s)
- `xiaomi-s40-pro` — modelo · 40 resultado(s) visto(s)
- `xiaomi-x20` — modelo · 40 resultado(s) visto(s)

### CAUSA 2 — CASAMENTO AMBIGUO: DOIS REGISTROS NO MESMO ANUNCIO — **2 de 66**

Os dois registros sao a escova lateral DIREITA e a ESQUERDA do mesmo modelo, e o
anuncio vende o par. Pela regra de 16/09, casamento que nao identifica UM registro
nao identifica nenhum, e os dois caem. **Este e o residuo que uma decisao humana
resolve e nenhuma regra resolve sozinha:** se o Raphael decidir que o par pode
ilustrar as duas metades, sao +2 com uma linha de excecao escrita.

- `wap-escova-direita-w300` — escova lateral
- `wap-escova-esquerda-w300` — escova lateral

### CAUSA 3 — SEM ANUNCIO NA SHOPEE: A ESCADA INTEIRA DEVOLVEU ZERO — **1 de 66**

A escada inteira devolveu ZERO em todos os degraus. **Nao ha o que colher, e coleta
nenhuma muda isso** — so uma fonte que nao seja a Shopee.

- `roborock-qrevo-curv` — modelo · 0 resultado(s) visto(s)

## O QUE ESTA LISTA PERMITE DECIDIR, e a decisao NAO e desta camada

O despacho de 18/09 escreveu, com todas as letras: *"NAO colete imagem de site de
fabricante nesta execucao. (...) Isso e decisao do Raphael, e ele decide depois de ver
o tamanho do residuo. Escreva o numero e pare."* **O numero e 66, e esta execucao
parou.** Os cinco dominios de fabricante estao abertos na rede desde 17/09 e as
paginas deles tem foto de produto — mas a licenca e outra: a 25.3 chama a imagem do
feed/API de fonte legitima porque **a imagem do anuncio ao lado do link do anuncio e
exatamente o que o programa de afiliado existe para permitir**, e isso nao se estende
ao site do fabricante.

**A conta que a decisao precisa, para nao precisar reabrir esta pagina:** dos 66 do
residuo, **30 sao modelos** (e pagina de fabricante tem foto do robo, entao a fonte
nova resolveria quase todos) e **36 sao pecas** (e pagina de acessorio de fabricante
e mais rara, entao a fonte nova resolveria uma parte).

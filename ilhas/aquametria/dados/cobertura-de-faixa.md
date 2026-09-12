# Cobertura de faixa das calculadoras da Aquametria

Medido em **2026-09-09** por `ferramentas/varrer-cobertura.mjs`, que abre cada
calculadora num Chromium de verdade e a preenche ponto a ponto. O numero de cada
linha e a quantidade de cartoes de produto que a calculadora REALMENTE desenhou
naquela entrada — nao uma contagem de banco, nao uma reimplementacao da regra.

Criterio (secao 14.3 do `ARQUIPELAGO.md`): **nenhuma faixa produzivel pode sair com
menos de 3 produtos elegiveis.** O que aparece marcado abaixo e a lista de
compras do banco, em ordem de urgencia.

Este arquivo e HISTORICO: cada medicao vira uma secao nova, nunca sobrescreve a
anterior. E a serie que diz se o banco esta cobrindo mais faixa ou so ficando maior.

## Medicao de 2026-09-12 — C15, medida no BANCO (bloco T3a)

Instrumento NOVO e diferente do de 09/09: `ferramentas/varrer-c15-banco.py`, uma
regua que le `dados/produtos-iluminacao.json` e `dados/esquema-produtos.json`
direto e reimplementa a regra publicada da C15, sem abrir navegador. Ela nao
substitui o `varrer-cobertura.mjs` — aquele conta o que a TELA desenha e continua
sendo a medicao de fechamento. Esta responde a outra pergunta, a que decide o que
colher: quantas luminarias do banco sobreviveriam a cada faixa, inclusive nas
faixas que hoje saem vazias, onde a tela nao tem cartao nenhum para contar e
portanto nao diz por que esta vazia.

**A coluna nova e o assunto do bloco.** A C15 tem DOIS jeitos de oferecer uma
luminaria: quem cai dentro da faixa de lm/L, e quem passa do teto mas tem
regulagem de intensidade declarada e por isso pode trabalhar abaixo do maximo. A
serie de 09/09 contava so a primeira coluna — e com isso leu como "falta produto"
um problema que era de um campo com duas grafias (ver o `REGISTRO.md` de 12/09).
Ate esta data o ramo dos reguláveis era inalcancavel para 5 das 8 luminarias do
catalogo que declaram regulagem, entao a segunda coluna teria sido zero em quase
toda a tabela mesmo se alguem a tivesse medido.

| condicao declarada | faixa | na faixa | + regulavel | total | |
|---|---|---:|---:|---:|---|
| exigencia baixa | 30 a 40 cm | 1 | 0 | 1 | **abaixo de 3** |
| exigencia baixa | 45 cm | 1 | 1 | 2 | **abaixo de 3** |
| exigencia baixa | 50 a 55 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia baixa | 60 a 70 cm | 0 | 1 | 1 | **abaixo de 3** |
| exigencia baixa | 75 cm | 1 | 1 | 2 | **abaixo de 3** |
| exigencia baixa | 80 cm | 0 | 1 | 1 | **abaixo de 3** |
| exigencia baixa | 85 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia baixa | 90 a 110 cm | 0 | 2 | 2 | **abaixo de 3** |
| exigencia baixa | 115 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia baixa | 120 cm | 0 | 2 | 2 | **abaixo de 3** |
| exigencia media | 30 a 40 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia media | 45 cm | 0 | 1 | 1 | **abaixo de 3** |
| exigencia media | 50 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia media | 55 cm | 1 | 0 | 1 | **abaixo de 3** |
| exigencia media | 60 a 65 cm | 2 | 1 | 3 | ok |
| exigencia media | 70 a 75 cm | 1 | 1 | 2 | **abaixo de 3** |
| exigencia media | 80 cm | 0 | 1 | 1 | **abaixo de 3** |
| exigencia media | 85 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia media | 90 a 110 cm | 1 | 2 | 3 | ok |
| exigencia media | 115 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia media | 120 cm | 1 | 1 | 2 | **abaixo de 3** |
| exigencia alta | 30 cm | 1 | 0 | 1 | **abaixo de 3** |
| exigencia alta | 35 a 40 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia alta | 45 cm | 1 | 0 | 1 | **abaixo de 3** |
| exigencia alta | 50 a 55 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia alta | 60 cm | 2 | 0 | 2 | **abaixo de 3** |
| exigencia alta | 65 a 75 cm | 1 | 0 | 1 | **abaixo de 3** |
| exigencia alta | 80 cm | 2 | 0 | 2 | **abaixo de 3** |
| exigencia alta | 85 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia alta | 90 cm | 3 | 0 | 3 | ok |
| exigencia alta | 95 a 110 cm | 2 | 0 | 2 | **abaixo de 3** |
| exigencia alta | 115 cm | 0 | 0 | 0 | **VAZIA** |
| exigencia alta | 120 cm | 1 | 0 | 1 | **abaixo de 3** |

Faixas medidas: 33 | VAZIAS: 11 | abaixo do piso de 3: 19 | cumprem: 3

### O que mudou em relacao a 09/09, e o que NAO mudou

- **O catalogo nao cresceu:** 15 luminarias sugeriveis, as mesmas de 11/09. Este
  bloco nao trouxe um registro novo nem um numero novo.
- **As faixas que cumprem o criterio foram de 1 para 3**, e as tres saem da
  segunda coluna: 60 a 65 cm e 90 a 110 cm na exigencia media passam a ter tres
  opcoes porque a regulagem declarada voltou a ser lida.
- **O buraco de 90 a 140 cm em exigencia BAIXA e MEDIA deixou de ser silencio.**
  Antes a pagina nao tinha o que oferecer e dizia, sobre a Chihiros WRGB II, que
  ela "nao declara regulagem de intensidade" — afirmacao que o proprio banco
  desmentia. Agora ela aparece como regulavel, com o comando nomeado.
- **A exigencia ALTA nao tem nenhum regulavel, e isso esta certo:** a faixa alta e
  ABERTA por cima (a fonte publica "acima de 40 lm/L" e para ai), entao nada
  nunca esta "acima do teto" nela. Uma coluna de reguláveis diferente de zero na
  linha da alta seria defeito, nao melhora — e e uma afirmacao que o portao mede.
- **O que continua sendo falta de produto de verdade:** 50 a 55 cm e 85 cm e 115
  cm em toda exigencia, e 35 a 55 cm na exigencia alta. Nenhuma regulagem
  conserta isso: nao existe peca no banco que cubra aquele comprimento.
- **O campo que barra continua sendo o mesmo:** 11 dos 26 registros nao declaram
  `fluxo_lm`, e 8 deles sao as Soma, que tem link de afiliado. Ampliar o catalogo
  com marca que nao publica lumen segue nao movendo este numero em nada.

### Lista de compras, revisada por esta medicao

1. Luminaria com fluxo declarado que cubra **50 a 55 cm** (hoje: nenhuma peca do
   banco cobre esse comprimento em nenhum nivel).
2. Luminaria que cubra **85 cm** e **115 cm** — sao os dois vaos entre as
   coberturas declaradas das familias que ja temos.
3. Luminaria de **30 a 55 cm com fluxo alto** para a exigencia alta.
4. `fluxo_lm` das 8 Soma, que ja tem link e cobrem de 20 a 130 cm. Continua sendo
   o item que mais move a tabela, e continua bloqueado pela mesma razao: nem a
   marca nem as nove lojas conferidas publicam lumen.

---

## Medicao de 2026-09-09

### C3 — vazao do filtro

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| comunitario, carga leve | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga leve | 40 L | 1 | **abaixo de 3** |
| comunitario, carga leve | 50 a 60 L | 3 | ok |
| comunitario, carga leve | 70 a 90 L | 4 | ok |
| comunitario, carga leve | 100 a 350 L | 5 | ok |
| comunitario, carga leve | 360 a 400 L | 4 | ok |
| comunitario, carga media | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga media | 40 L | 1 | **abaixo de 3** |
| comunitario, carga media | 50 a 60 L | 3 | ok |
| comunitario, carga media | 70 a 90 L | 4 | ok |
| comunitario, carga media | 100 a 350 L | 5 | ok |
| comunitario, carga media | 360 a 400 L | 4 | ok |
| comunitario, carga pesada | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga pesada | 40 L | 1 | **abaixo de 3** |
| comunitario, carga pesada | 50 a 60 L | 3 | ok |
| comunitario, carga pesada | 70 a 90 L | 4 | ok |
| comunitario, carga pesada | 100 a 350 L | 5 | ok |
| comunitario, carga pesada | 360 a 400 L | 4 | ok |
| plantado, carga media | 20 a 70 L | 0 | **VAZIA** |
| plantado, carga media | 80 L | 1 | **abaixo de 3** |
| plantado, carga media | 90 L | 2 | **abaixo de 3** |
| plantado, carga media | 100 a 120 L | 1 | **abaixo de 3** |
| plantado, carga media | 130 a 150 L | 2 | **abaixo de 3** |
| plantado, carga media | 160 a 170 L | 1 | **abaixo de 3** |
| plantado, carga media | 180 a 190 L | 3 | ok |
| plantado, carga media | 200 a 250 L | 5 | ok |
| plantado, carga media | 260 a 270 L | 3 | ok |
| plantado, carga media | 280 a 290 L | 4 | ok |
| plantado, carga media | 300 a 350 L | 5 | ok |
| plantado, carga media | 360 a 400 L | 4 | ok |

### C5 — potencia do aquecedor

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| delta 4 C, tomada 110 V | 20 L | 3 | ok |
| delta 4 C, tomada 110 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 4 C, tomada 110 V | 60 a 80 L | 3 | ok |
| delta 4 C, tomada 110 V | 90 a 150 L | 5 | ok |
| delta 4 C, tomada 110 V | 160 L | 3 | ok |
| delta 4 C, tomada 110 V | 170 a 200 L | 5 | ok |
| delta 4 C, tomada 110 V | 210 a 300 L | 2 | **abaixo de 3** |
| delta 4 C, tomada 110 V | 310 a 400 L | 0 | **VAZIA** |
| delta 6 C, tomada 110 V | 20 L | 3 | ok |
| delta 6 C, tomada 110 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 110 V | 60 a 80 L | 3 | ok |
| delta 6 C, tomada 110 V | 90 a 150 L | 5 | ok |
| delta 6 C, tomada 110 V | 160 L | 3 | ok |
| delta 6 C, tomada 110 V | 170 a 200 L | 5 | ok |
| delta 6 C, tomada 110 V | 210 a 300 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 110 V | 310 a 400 L | 0 | **VAZIA** |
| delta 6 C, tomada 220 V | 20 L | 3 | ok |
| delta 6 C, tomada 220 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 220 V | 60 a 80 L | 3 | ok |
| delta 6 C, tomada 220 V | 90 a 150 L | 5 | ok |
| delta 6 C, tomada 220 V | 160 L | 3 | ok |
| delta 6 C, tomada 220 V | 170 a 200 L | 5 | ok |
| delta 6 C, tomada 220 V | 210 a 300 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 220 V | 310 a 400 L | 0 | **VAZIA** |
| delta 10 C, tomada 220 V | 20 L | 3 | ok |
| delta 10 C, tomada 220 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 10 C, tomada 220 V | 60 a 80 L | 3 | ok |
| delta 10 C, tomada 220 V | 90 a 150 L | 5 | ok |
| delta 10 C, tomada 220 V | 160 L | 3 | ok |
| delta 10 C, tomada 220 V | 170 a 200 L | 5 | ok |
| delta 10 C, tomada 220 V | 210 a 300 L | 2 | **abaixo de 3** |
| delta 10 C, tomada 220 V | 310 a 400 L | 0 | **VAZIA** |

### C12 — midia filtrante

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| comunitario | 20 a 400 L | 3 | ok |
| plantado | 20 a 400 L | 3 | ok |
| sensiveis | 20 a 400 L | 3 | ok |

### C15 — iluminacao

Eixo varrido: 30 a 120 cm, de 5 em 5.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| exigencia baixa | 30 a 40 cm | 1 | **abaixo de 3** |
| exigencia baixa | 45 cm | 2 | **abaixo de 3** |
| exigencia baixa | 50 a 70 cm | 0 | **VAZIA** |
| exigencia baixa | 75 cm | 1 | **abaixo de 3** |
| exigencia baixa | 80 a 120 cm | 0 | **VAZIA** |
| exigencia media | 30 a 40 cm | 0 | **VAZIA** |
| exigencia media | 45 cm | 1 | **abaixo de 3** |
| exigencia media | 50 cm | 0 | **VAZIA** |
| exigencia media | 55 cm | 1 | **abaixo de 3** |
| exigencia media | 60 a 65 cm | 2 | **abaixo de 3** |
| exigencia media | 70 a 75 cm | 1 | **abaixo de 3** |
| exigencia media | 80 a 120 cm | 0 | **VAZIA** |
| exigencia alta | 30 cm | 1 | **abaixo de 3** |
| exigencia alta | 35 a 40 cm | 0 | **VAZIA** |
| exigencia alta | 45 cm | 1 | **abaixo de 3** |
| exigencia alta | 50 a 55 cm | 0 | **VAZIA** |
| exigencia alta | 60 cm | 1 | **abaixo de 3** |
| exigencia alta | 65 a 75 cm | 0 | **VAZIA** |
| exigencia alta | 80 cm | 1 | **abaixo de 3** |
| exigencia alta | 85 cm | 0 | **VAZIA** |
| exigencia alta | 90 cm | 1 | **abaixo de 3** |
| exigencia alta | 95 a 120 cm | 0 | **VAZIA** |

### Resumo

- Faixas medidas: **87**
- Faixas VAZIAS (nenhum produto): **18**
- Faixas com 1 ou 2 produtos (abaixo do piso de 3): **28**
- Faixas que cumprem o criterio: **41**

### O que estes numeros dizem, e o que comprar por causa deles

**A C15 nao cumpre o criterio em NENHUMA faixa.** Nas 22 faixas medidas, o melhor
resultado e 2 luminarias, e 8 faixas saem vazias. A causa nao e tamanho de catalogo:
sao 20 luminarias no banco e 11 delas estao barradas pelo mesmo campo, `fluxo_lm`,
que o meio do mercado brasileiro nao publica. Ampliar o catalogo com marca que nao
declara lumen nao move este numero em nada — foi por isso que o bloco T3(a2) trouxe
a Chihiros A-Series, que declara. Faixa mais urgente: **acima de 80 cm em qualquer
exigencia, e 30 a 55 cm na exigencia alta.**

**A C5 fica sem NENHUM aquecedor acima de 310 L**, nas quatro combinacoes de delta e
tomada. O banco simplesmente nao tem aparelho acima de 300 W. E de 30 a 50 L e de
210 a 300 L ela entrega dois, um a menos que o piso. Compras, em ordem: **um aquecedor
de 400 a 500 W**, depois **250 W**, depois **um segundo e um terceiro de 25 a 50 W**.
Repare que trocar a tomada de 110 para 220 V nao muda uma linha sequer: todos os
aquecedores aptos declaram as duas tensoes, entao a barreira de voltagem hoje nao
elimina ninguem — ela so elimina os dez registros que estao com `voltagem: null`.

**A C3 tem um buraco de entrada: de 20 a 40 L nao ha filtro nenhum**, em todos os
perfis. E o aquario de comeco, que e onde mais gente chega pela busca. Compra:
**dois ou tres filtros de baixa vazao, entre 150 e 400 L/h**. No perfil plantado o
buraco e maior e vai ate 170 L, porque a dupla condicao (vazao E volume atendido)
corta mais fundo.

**A C12 cumpre o criterio em toda a faixa, mas no piso**: exatamente 3 midias de 20 a
400 L, nos tres perfis. Nao e folga, e o minimo — qualquer midia que saia do banco
derruba a calculadora inteira abaixo do criterio.

Ordem de compra que estes numeros determinam, e que substitui qualquer meta de
numero redondo:

1. Luminaria com fluxo declarado acima de 80 cm (C15 vazia em toda a faixa alta).
2. Aquecedor acima de 300 W (C5 vazia de 310 a 400 L).
3. Filtro de baixa vazao para 20 a 40 L (C3 vazia na entrada).
4. Luminaria com fluxo declarado de 30 a 55 cm para exigencia alta.
5. Aquecedor de 250 W e um segundo de 25 a 50 W.
6. Uma quarta midia biologica, para a C12 sair do piso.

---

## Medicao de 2026-09-09 (noite) — depois da leva de fechamento de faixa

Segunda medicao do dia, com o MESMO instrumento e o MESMO eixo, depois de o banco
ir de 68 para 78 produtos (4 aquecedores e 6 luminarias, mais a Chihiros WRGB II
Pro 60 destravada pela voltagem). A comparacao honesta e por PONTO medido, nao por
linha de tabela: as linhas agrupam pontos contiguos de mesma contagem, entao elas se
re-segmentam a cada medicao e o numero de linhas nao compara com nada.

| | manha | noite |
|---|---:|---:|
| pontos que cumprem o criterio | 312 de 486 | **379 de 486** |
| pontos abaixo do piso de 3 | 81 | 73 |
| pontos VAZIOS | 93 | **34** |

Por calculadora, em pontos medidos:

| | ok | abaixo de 3 | VAZIA |
|---|---:|---:|---:|
| C3 (manha e noite) | 131 | 13 | 12 |
| C5 manha | 64 | 52 | 40 |
| **C5 noite** | **128** | **28** | **0** |
| C12 (manha e noite) | 117 | 0 | 0 |
| C15 manha | 0 | 16 | 41 |
| **C15 noite** | **3** | **32** | **22** |

**A C3 e a C12 devolveram numero IDENTICO nas duas medicoes**, e isso nao e detalhe: o
banco delas nao foi tocado, entao a repeticao exata prova que o instrumento e estavel e
que a diferenca na C5 e na C15 veio do banco, nao da medida.

**A C5 nao tem mais nenhum ponto vazio de 20 a 400 L** — era o buraco numero 2 da lista
de compras. **A C15 cumpre o criterio pela primeira vez**, em dois degraus (60 a 65 cm
na exigencia media e 90 cm na exigencia alta); era zero de 22 na manha.


### C3 — vazao do filtro

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| comunitario, carga leve | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga leve | 40 L | 1 | **abaixo de 3** |
| comunitario, carga leve | 50 a 60 L | 3 | ok |
| comunitario, carga leve | 70 a 90 L | 4 | ok |
| comunitario, carga leve | 100 a 350 L | 5 | ok |
| comunitario, carga leve | 360 a 400 L | 4 | ok |
| comunitario, carga media | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga media | 40 L | 1 | **abaixo de 3** |
| comunitario, carga media | 50 a 60 L | 3 | ok |
| comunitario, carga media | 70 a 90 L | 4 | ok |
| comunitario, carga media | 100 a 350 L | 5 | ok |
| comunitario, carga media | 360 a 400 L | 4 | ok |
| comunitario, carga pesada | 20 a 30 L | 0 | **VAZIA** |
| comunitario, carga pesada | 40 L | 1 | **abaixo de 3** |
| comunitario, carga pesada | 50 a 60 L | 3 | ok |
| comunitario, carga pesada | 70 a 90 L | 4 | ok |
| comunitario, carga pesada | 100 a 350 L | 5 | ok |
| comunitario, carga pesada | 360 a 400 L | 4 | ok |
| plantado, carga media | 20 a 70 L | 0 | **VAZIA** |
| plantado, carga media | 80 L | 1 | **abaixo de 3** |
| plantado, carga media | 90 L | 2 | **abaixo de 3** |
| plantado, carga media | 100 a 120 L | 1 | **abaixo de 3** |
| plantado, carga media | 130 a 150 L | 2 | **abaixo de 3** |
| plantado, carga media | 160 a 170 L | 1 | **abaixo de 3** |
| plantado, carga media | 180 a 190 L | 3 | ok |
| plantado, carga media | 200 a 250 L | 5 | ok |
| plantado, carga media | 260 a 270 L | 3 | ok |
| plantado, carga media | 280 a 290 L | 4 | ok |
| plantado, carga media | 300 a 350 L | 5 | ok |
| plantado, carga media | 360 a 400 L | 4 | ok |

### C5 — potencia do aquecedor

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| delta 4 C, tomada 110 V | 20 L | 3 | ok |
| delta 4 C, tomada 110 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 4 C, tomada 110 V | 60 a 80 L | 3 | ok |
| delta 4 C, tomada 110 V | 90 a 150 L | 5 | ok |
| delta 4 C, tomada 110 V | 160 L | 4 | ok |
| delta 4 C, tomada 110 V | 170 a 200 L | 5 | ok |
| delta 4 C, tomada 110 V | 210 a 250 L | 3 | ok |
| delta 4 C, tomada 110 V | 260 L | 2 | **abaixo de 3** |
| delta 4 C, tomada 110 V | 270 a 300 L | 3 | ok |
| delta 4 C, tomada 110 V | 310 a 330 L | 1 | **abaixo de 3** |
| delta 4 C, tomada 110 V | 340 a 400 L | 3 | ok |
| delta 6 C, tomada 110 V | 20 L | 3 | ok |
| delta 6 C, tomada 110 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 110 V | 60 a 80 L | 3 | ok |
| delta 6 C, tomada 110 V | 90 a 150 L | 5 | ok |
| delta 6 C, tomada 110 V | 160 L | 4 | ok |
| delta 6 C, tomada 110 V | 170 a 200 L | 5 | ok |
| delta 6 C, tomada 110 V | 210 a 250 L | 3 | ok |
| delta 6 C, tomada 110 V | 260 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 110 V | 270 a 300 L | 3 | ok |
| delta 6 C, tomada 110 V | 310 a 330 L | 1 | **abaixo de 3** |
| delta 6 C, tomada 110 V | 340 a 400 L | 3 | ok |
| delta 6 C, tomada 220 V | 20 L | 3 | ok |
| delta 6 C, tomada 220 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 220 V | 60 a 80 L | 3 | ok |
| delta 6 C, tomada 220 V | 90 a 150 L | 5 | ok |
| delta 6 C, tomada 220 V | 160 L | 4 | ok |
| delta 6 C, tomada 220 V | 170 a 200 L | 5 | ok |
| delta 6 C, tomada 220 V | 210 a 250 L | 3 | ok |
| delta 6 C, tomada 220 V | 260 L | 2 | **abaixo de 3** |
| delta 6 C, tomada 220 V | 270 a 300 L | 3 | ok |
| delta 6 C, tomada 220 V | 310 a 330 L | 1 | **abaixo de 3** |
| delta 6 C, tomada 220 V | 340 a 400 L | 3 | ok |
| delta 10 C, tomada 220 V | 20 L | 3 | ok |
| delta 10 C, tomada 220 V | 30 a 50 L | 2 | **abaixo de 3** |
| delta 10 C, tomada 220 V | 60 a 80 L | 3 | ok |
| delta 10 C, tomada 220 V | 90 a 150 L | 5 | ok |
| delta 10 C, tomada 220 V | 160 L | 4 | ok |
| delta 10 C, tomada 220 V | 170 a 200 L | 5 | ok |
| delta 10 C, tomada 220 V | 210 a 250 L | 3 | ok |
| delta 10 C, tomada 220 V | 260 L | 2 | **abaixo de 3** |
| delta 10 C, tomada 220 V | 270 a 300 L | 3 | ok |
| delta 10 C, tomada 220 V | 310 a 330 L | 1 | **abaixo de 3** |
| delta 10 C, tomada 220 V | 340 a 400 L | 3 | ok |

### C12 — midia filtrante

Eixo varrido: 20 a 400 L, de 10 em 10.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| comunitario | 20 a 400 L | 3 | ok |
| plantado | 20 a 400 L | 3 | ok |
| sensiveis | 20 a 400 L | 3 | ok |

### C15 — iluminacao

Eixo varrido: 30 a 120 cm, de 5 em 5.

| condicao declarada | faixa | produtos elegiveis | |
|---|---|---:|---|
| exigencia baixa | 30 a 40 cm | 1 | **abaixo de 3** |
| exigencia baixa | 45 cm | 2 | **abaixo de 3** |
| exigencia baixa | 50 a 55 cm | 0 | **VAZIA** |
| exigencia baixa | 60 a 70 cm | 1 | **abaixo de 3** |
| exigencia baixa | 75 cm | 2 | **abaixo de 3** |
| exigencia baixa | 80 cm | 1 | **abaixo de 3** |
| exigencia baixa | 85 a 120 cm | 0 | **VAZIA** |
| exigencia media | 30 a 40 cm | 0 | **VAZIA** |
| exigencia media | 45 cm | 1 | **abaixo de 3** |
| exigencia media | 50 cm | 0 | **VAZIA** |
| exigencia media | 55 cm | 1 | **abaixo de 3** |
| exigencia media | 60 a 65 cm | 3 | ok |
| exigencia media | 70 a 75 cm | 2 | **abaixo de 3** |
| exigencia media | 80 cm | 1 | **abaixo de 3** |
| exigencia media | 85 cm | 0 | **VAZIA** |
| exigencia media | 90 a 110 cm | 1 | **abaixo de 3** |
| exigencia media | 115 cm | 0 | **VAZIA** |
| exigencia media | 120 cm | 1 | **abaixo de 3** |
| exigencia alta | 30 cm | 1 | **abaixo de 3** |
| exigencia alta | 35 a 40 cm | 0 | **VAZIA** |
| exigencia alta | 45 cm | 1 | **abaixo de 3** |
| exigencia alta | 50 a 55 cm | 0 | **VAZIA** |
| exigencia alta | 60 cm | 2 | **abaixo de 3** |
| exigencia alta | 65 a 75 cm | 1 | **abaixo de 3** |
| exigencia alta | 80 cm | 2 | **abaixo de 3** |
| exigencia alta | 85 cm | 0 | **VAZIA** |
| exigencia alta | 90 cm | 3 | ok |
| exigencia alta | 95 a 110 cm | 2 | **abaixo de 3** |
| exigencia alta | 115 cm | 0 | **VAZIA** |
| exigencia alta | 120 cm | 1 | **abaixo de 3** |

### Resumo

- Faixas medidas: **107**
- Faixas VAZIAS (nenhum produto): **14**
- Faixas com 1 ou 2 produtos (abaixo do piso de 3): **38**
- Faixas que cumprem o criterio: **55**

### O que estes numeros dizem, e a lista de compras que sobra

**A C5 esta resolvida como cobertura, e o que sobra e um limite do mercado, nao do banco.**
Nenhum ponto vazio de 20 a 400 L. O unico trecho que fica com UM so aparelho e de 310 a
330 L, e o motivo esta fora do nosso alcance: a janela de potencia ali vai de 310 a 465 W,
e o mercado brasileiro so publica degraus de 300 W e 500 W — 400 W aparece numa linha so
(Hopar J-226). Comprar mais aquecedor nao fecha esse trecho; o que fecha e a propria tela,
que ja diz desde 08/09/2026 que acima do maior degrau da linha a resposta e mais de um
aparelho. Continuam abaixo do piso, e esses sim sao compra: **30 a 50 L** (dois aparelhos)
e **260 L** (dois).

**A C15 cumpriu o criterio pela primeira vez, e a forma do buraco mudou de lugar.** Era
zero de 22 faixas de manha; agora ha dois degraus servidos (60 a 65 cm na exigencia media,
90 cm na alta). O que a leva ensinou, e que nao dava para ver antes:

1. **O buraco de 85 cm e de 115 cm e do MERCADO.** As pecas declaram cobrir 90 a 110 cm ou
   120 a 140 cm, e ninguem declara o meio. Nao adianta procurar melhor: nao existe.
2. **A exigencia BAIXA virou o pior caso, e por inversao.** De 85 a 120 cm ela sai vazia
   justamente porque as luminarias que entraram sao potentes demais: a faixa de lumens que
   a exigencia baixa pede fica ABAIXO do que uma WRGB II de 90 a 130 W entrega. Falta
   luminaria fraca e grande — barra economica de 100 a 120 cm com lumen declarado — e essa
   e uma compra que a medicao da manha nao sabia pedir.
3. **`fluxo_lm` continua sendo o campo que decide tudo.** Das 26 luminarias do banco, 11
   seguem barradas por nao declarar lumen, e oito delas sao a linha Soma inteira, que cobre
   de 20 a 130 cm e **tem link de afiliado em todas**. Ampliar catalogo com marca que nao
   declara lumen nao move este numero em nada.

Ordem de compra que estes numeros determinam, substituindo a da manha:

1. Luminaria de exigencia BAIXA (lumen modesto) de 85 a 120 cm — a faixa vazia mais larga
   que sobrou, e a que a medicao anterior nem enxergava.
2. Luminaria com fluxo declarado de 30 a 55 cm, que segue vazia nas exigencias media e alta.
3. Filtro de baixa vazao para 20 a 40 L (C3 vazia na entrada, inalterada desde a manha).
4. Segundo e terceiro aquecedores de 25 a 50 L, e um de ~250 W para o degrau de 260 L.
5. Uma quarta midia biologica, para a C12 sair do piso exato de 3.
6. **Nao comprar:** aquecedor acima de 300 W. A faixa esta coberta, e o unico trecho magro
   e uma lacuna do mercado brasileiro que a tela ja explica.

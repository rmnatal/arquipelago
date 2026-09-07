---
titulo: Modelo do banco de produtos da Aquametria
bloco: 3
gerado_em: 2026-09-07
depende_de: dados/especificacao-calculadoras.md
define: dados/esquema-produtos.json
publicar: false
---

# Modelo do banco de produtos — Aquametria

Bloco 3 do playbook. O Bloco 2 especificou as 8 calculadoras e, calculadora
por calculadora, listou os campos que cada uma precisa receber de um produto.
Este bloco transforma essa lista em **modelo**: quais entidades existem, quais
campos cada uma tem, com que unidade, o que é obrigatório, **de onde vem cada
dado** e o que acontece quando as fontes discordam.

O modelo é executável em três arquivos:

| Arquivo | Papel |
|---|---|
| `dados/esquema-produtos.json` | o contrato: campos, tipos, unidades, vocabulários, origem esperada, regras V1 a V14 |
| `dados/produtos-filtro.json`, `-aquecedor`, `-iluminacao`, `-midia` | os dados, uma entidade por arquivo |
| `dados/produtos-cotacoes.json` | preços observados, por loja e por data (hoje vazio, e a seção 8 explica por quê) |
| `ferramentas/validar-produtos.py` | as regras rodando de verdade sobre os dados |

Junto com o modelo vão **15 registros de semente**, colhidos hoje. Eles não
existem para cobrir o mercado — existem para testar o modelo contra a realidade
do varejo brasileiro antes que ele seja usado em escala. E testaram: a seção 10
lista o que quebrou.

---

## 1. Os seis princípios

1. **Procedência por campo, não por registro.** Um produto quase sempre tem a
   vazão do fabricante e a disponibilidade do varejo. O registro guarda as duas
   origens separadas, cada uma dizendo quais campos sustenta.
2. **Declarado não é medido.** Todo número de fabricante é *declaração*. O banco
   nunca converte declaração em desempenho: `vazao_real_lh` existe no esquema e
   é `null` em todo registro, porque medição própria ainda não existe.
3. **Divergência é conteúdo.** Quando duas fontes do mesmo nível discordam, o
   campo vira conflito e a tela publica os dois valores com atribuição. Nunca a
   média, nunca a escolha silenciosa.
4. **O que falta fica explícito.** Campo sem fonte é `null` com motivo escrito,
   nunca um número plausível.
5. **Preço não é atributo de produto.** É série temporal, com loja e data, em
   arquivo próprio — e nunca entra em critério técnico de sugestão.
6. **Derivado não se escreve à mão.** Turnover implícito, W/L, lm/W e mL/L são
   calculados a partir dos campos com fonte. Gravar um derivado é defeito, e o
   validador reprova (V4).

---

## 2. Identidade do produto

O caso que definiu a regra apareceu no primeiro dia de coleta:

| | Atman AT-3338 | Atman AT-3338**S** |
|---|---|---|
| vazão nominal | 1200 L/h | 1500 L/h |
| potência | 35 W | 18 W |
| coluna máxima | 1,8 m | 1,5 m |
| volume declarado | até 450 L | 150 a 400 L |

Uma letra no fim do modelo muda os quatro campos que a C3 e a C7 usam. Daí as
três regras de identidade:

- **`id`**: kebab-case, `marca-modelo[-variante]`, estável para sempre
  (`atman-at-3338`, `atman-at-3338s`, `eheim-classic-250-2213`).
- **Variante é registro próprio.** Nunca duas especificações no mesmo registro.
- **`nomes_alternativos`** guarda as grafias do varejo brasileiro (`Sun Sun
  HW303B`, `SunSun HW-303 B`) para casar busca e cotação. Não tem valor técnico.

Um caso pior apareceu na iluminação: produto **sem marca declarada**, vendido
com o nome da loja. `marca` aceita `null`, mas sem ela não há como casar
cotações entre lojas — o registro fica `parcial` e a limitação está escrita nele.

---

## 3. Campos comuns a todas as entidades

| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| `id` | string kebab-case | sim | editorial |
| `entidade` | filtro/aquecedor/iluminacao/midia | sim | editorial |
| `marca`, `modelo` | string | sim | fabricante ou varejo |
| `linha`, `variante` | string \| null | não | fabricante |
| `nomes_alternativos` | lista | não | varejo |
| `gtin` | EAN-13 \| null | não | varejo |
| `disponibilidade_br` | vendido/importado/descontinuado/desconhecido | sim | varejo |
| `voltagem` | lista de 110/127/220/bivolt \| null | não na ficha, **sim para sugerir** | fabricante ou varejo |
| `volume_atendido_declarado_L` | `{min, max}` | sim (não para iluminação) | fabricante, senão varejo |
| `fontes[]` | lista | sim | editorial |
| `conflitos[]` | lista | não | editorial |
| `verificado_em` | data ISO | sim | editorial |
| `status_registro` | completo/parcial/conflito/revalidar/rascunho | sim | editorial |

`volume_atendido_declarado_L` é sempre **o que o fabricante declara**, nunca uma
recomendação da Aquametria; `min` pode ser `null` quando a ficha só publica o
teto ("até 250 L"). Não é obrigatório em iluminação porque fabricante de
luminária dimensiona por centímetro, não por litro — nenhum dos 4 registros de
semente declara volume.

**`voltagem` merece parágrafo próprio.** Não é obrigatória para a ficha existir,
mas é requisito para a calculadora **sugerir** o produto (C3, C5 e C15):
aquecedor, bomba e luminária queimam na voltagem errada, e o varejo brasileiro
omite o dado com frequência. Hoje é o campo que mais barra sugestão no banco
inteiro — ver seção 10.

### `status_registro`

| Status | Significado |
|---|---|
| `completo` | todos os obrigatórios da entidade preenchidos e com fonte |
| `parcial` | falta obrigatório; a ficha vale como conteúdo, mas a calculadora que depende do campo faltante não sugere |
| `conflito` | fontes do mesmo nível divergem; pode ser sugerido, mas a tela publica a divergência |
| `revalidar` | verificado há mais de 180 dias, ou marcado como implausível pelo validador; sai da sugestão |
| `rascunho` | sem fonte suficiente; nunca sai na tela |

---

## 4. Entidade `filtro`

Consumida por C3 (vazão), C7 (consumo) e C12 (mídia).

| Campo | Unidade | Obrigatório | Origem esperada |
|---|---|---|---|
| `tipo` | canister/hang-on/interno/esponja/sump/filtro-de-caixa/fluidizado | sim | fabricante ou varejo |
| `vazao_nominal_lh` | L/h | sim | fabricante |
| `vazao_real_lh` | L/h | não (sempre null) | **só medição própria** |
| `potencia_w` | W | sim | fabricante |
| `coluna_maxima_m` | m | sim | fabricante |
| `volume_cesto_L`, `volume_filtragem_L` | L | não | fabricante |
| `midia_inclusa` | lista | não | fabricante ou varejo |
| `uv_w` | W | não | fabricante |
| `mangueira_mm` | mm | não | fabricante |

**Derivados** (calculados, nunca gravados):

- `turnover_implicito_xh` = vazão ÷ volume declarado. É o turnover que o próprio
  fabricante considera suficiente, e o eixo editorial da C3.
- `eficiencia_lh_por_w` = vazão ÷ potência. Alimenta a comparação de economia
  mensal da C7.

`vazao_nominal_lh` é medida pelo fabricante a coluna zero e sem mídia: **não é**
a vazão no aquário do visitante. A C3 registra que não existe fator de perda com
fonte publicável e proíbe inventar um; `vazao_real_lh` só será preenchido por
bancada própria.

---

## 5. Entidade `aquecedor`

Consumida por C5 (potência por delta térmico) e C7.

| Campo | Unidade | Obrigatório | Origem esperada |
|---|---|---|---|
| `potencia_w` | W | sim | fabricante |
| `tipo` | resistencia-vidro/quartzo/titanio/cabo/externo-em-linha | sim | fabricante ou varejo |
| `termostato` | interno-analogico/interno-digital/externo/nenhum | sim | fabricante ou varejo |
| `faixa_ajuste_C` | °C `{min,max}` | sim | fabricante |
| `precisao_C` | °C | não | fabricante |
| `comprimento_cm` | cm | não | fabricante ou varejo |
| `submersivel` | booleano | não | fabricante |
| `protecao_funcionamento_a_seco` | booleano | não | fabricante |

**Derivados:** `w_por_L_declarado` (potência ÷ volume declarado) e
`largura_faixa_x` (volume máximo ÷ volume mínimo). Acima de 3x, a declaração do
fabricante não dimensiona nada e a tela é obrigada a dizer isso — o Eheim Jäger
de 200 W, declarado para 30 a 400 L, dá **13,3x**.

`protecao_funcionamento_a_seco` é item de segurança: nunca preencher por
inferência. Sem declaração, `null`.

---

## 6. Entidade `iluminacao`

Consumida por C15 (lm/L e fotoperíodo) e C7.

| Campo | Unidade | Obrigatório | Origem esperada |
|---|---|---|---|
| `tipo` | led-barra/led-calha/led-tampa/led-pendente/refletor/fluorescente | sim | fabricante ou varejo |
| `potencia_w` | W | sim | fabricante ou varejo |
| `fluxo_lm` | lm | sim | fabricante |
| `comprimento_luminaria_cm` | cm | sim | fabricante ou varejo |
| `comprimento_aquario_cm` | cm `{min,max}` | não | fabricante ou varejo |
| `temperatura_cor_k` | K | não | fabricante ou varejo |
| `espectro` | branco/branco-azul/rgb/wrgb/full-spectrum | não | fabricante |
| `ppfd_declarado` + `ppfd_distancia_cm` | µmol/m²/s + cm | não, **e só em par** | fabricante |
| `regulagem` | nenhuma/dimmer/temporizador/app/controlador | não | fabricante |

**PPFD sem distância de medição é número sem significado**: o validador rejeita
um sem o outro (V5).

**Comprimento da peça não é comprimento do aquário.** A Sunsun ADE-400c tem
41 cm de peça e é declarada para aquários de 48 a 65 cm (tem hastes). São dois
campos, e um não se deriva do outro. Como o varejo brasileiro nomeia a luminária
pelo próprio tamanho ("LED 60 cm") e quase nunca declara o aquário atendido, o
critério da C15 aceita qualquer um dos dois — mas com uma pendência aberta:

> **Pendência de critério (C15).** Converter `comprimento_luminaria_cm` em
> cobertura do aquário exige uma convenção editorial declarada (quanta sombra nas
> pontas é aceitável). Enquanto essa convenção não virar constante em
> `dados/constantes-calculadoras.json` com status `convencao-editorial`, a C15 só
> pode sugerir produto que declare `comprimento_aquario_cm`.

**Derivado:** `eficacia_lm_por_w`. Ele permitiria estimar o lúmen de um produto
que não o declara — e é justamente o que **não** se faz: estimativa não entra no
banco. Se sair, sai na tela, marcada como estimativa da Aquametria.

---

## 7. Entidade `midia`

Consumida por C12 (volume, ordem e troca de mídia) — o vácuo nº 1 do Bloco 1.

| Campo | Unidade | Obrigatório | Origem esperada |
|---|---|---|---|
| `tipo` | biologica/mecanica/quimica/mista | sim | fabricante |
| `material` | ceramica-porosa/vidro-sinterizado/silicato-poroso/argila-expandida/espuma/perlon/carvao-ativado/zeolita/resina/cascalho | sim | fabricante |
| `volume_embalagem_L` | L | sim | fabricante ou varejo |
| `dosagem_declarada` | `{volume_midia_mL, por_volume_agua_L}` | sim | fabricante |
| `area_superficial_m2_por_L` | m²/L | não | fabricante |
| `peso_g` | g | não | fabricante ou varejo |
| `granulometria_mm` | mm | não | fabricante |
| `regeneravel`, `vida_util_declarada_meses` | booleano, meses | não | fabricante |
| `posicao_no_fluxo` | pre-filtragem/mecanica-grossa/mecanica-fina/biologica/quimica/polimento | não | **editorial** |

Mídia se compra por volume: peso sem volume não dimensiona cesto nenhum.
`posicao_no_fluxo` é o único campo do banco de origem **editorial** — é
classificação da Aquametria a partir de `tipo` e `material`, serve para publicar
a ordem das mídias no canister, e por isso não exige fonte de terceiro (o
validador o exclui da regra V2).

**Área superficial declarada é número de marketing** na maior parte do setor:
entra com atribuição e **nunca** compara marcas na tela sem dizer que o método de
medição não é o mesmo. Seachem Matrix declara mais de 700 m²/L; Eheim SUBSTRAT
pro, cerca de 450 m²/L; nenhum dos dois publica como mediu.

**Derivados:** `dosagem_mL_por_L`, `densidade_aparente_g_por_L` e
`embalagens_necessarias` (calculado na hora, com o volume do visitante) — a
comparação de custo por litro tratado que nenhum varejo brasileiro publica.

---

## 8. De onde vem cada dado: a escada de fontes

Toda entrada de `fontes[]` declara uma origem, e a origem tem nível. **Em
conflito, o nível mais alto vence e o outro fica registrado. Dentro do mesmo
nível, ninguém vence: o campo vira conflito.**

| Nível | Origem | Pode sustentar | Existe hoje? |
|---|---|---|---|
| 1 | `medicao-propria` | vazão real, consumo real, PPFD. **A única que pode publicar desempenho** | não |
| 2 | `manual-fabricante` | qualquer campo técnico declarado (manual/ficha oficial **lida direto**) | não — egresso bloqueado |
| 3 | `fabricante-via-busca` | campo técnico atribuído ao fabricante, colhido por busca. Tela: "a confirmar no manual" | sim |
| 4 | `varejo-oficial` | campo técnico transcrito pela loja oficial da marca. Tela: "confira a embalagem" | sim |
| 5 | `varejo` | campo técnico transcrito por varejista especializado. Tela: "confira a embalagem" | sim |
| 6 | `marketplace-anuncio` | **apenas** existência do produto, nomenclatura e cotação. Nunca um número técnico | sim |

O nível 2 está bloqueado por infraestrutura, não por escolha: o egresso da nuvem
barra domínios de fabricante (`seachem.com` e `sicce.com` devolveram
`EGRESS_BLOCKED` em 07/09/2026). Por isso **todo** número de fabricante da
semente entrou como nível 3, com a reconferência anotada no próprio registro.

### Conflito não se resolve, se publica

O bloco `conflitos[]` guarda os valores divergentes com atribuição, a razão da
diferença e o tratamento:

- `publicar-os-dois` — a tela mostra as duas leituras e de quem são;
- `nivel-mais-alto-vence` — o valor do nível superior fica no campo, o outro no conflito;
- `campo-vira-null` — empate de nível: nenhum valor entra no campo.

Dois conflitos reais na semente:

1. **Seachem Matrix, o fabricante contra si mesmo.** "250 mL para 200 L"
   (1,25 mL/L) e "1 L para 100 galões" (2,6 mL/L) saem da mesma comunicação.
   2,1 vezes de diferença → `publicar-os-dois`.
2. **Roxin HT-1300/Q3, varejo contra varejo.** Faixa de ajuste de 22 a 34 °C numa
   ficha, 16 a 32 °C em outra, mesmo nível → `campo-vira-null` nos três registros
   da linha, até a embalagem ser conferida.

---

## 9. Preço é série temporal

Preço **não** é campo de produto. Vive em `dados/produtos-cotacoes.json`, uma
observação por loja e por data: `produto_id`, `loja`, `tipo_loja`, `url`,
`preco_brl`, `cotado_em`, `condicao`, `disponivel`, `frete_incluso`, `voltagem`
(a mesma peça custa diferente em 110 e 220 — sem isso a comparação mente) e
`link_afiliado`, que só é preenchido no desembarque e **nunca substitui a URL de
origem**: a procedência do preço tem de continuar auditável.

- `preco_referencia` é uma **view**: mediana das cotações novas e disponíveis dos
  últimos 30 dias, com `n` e data na tela. Sem cotação no período, é `null` e a
  tela diz "sem cotação recente".
- **Preço nunca entra em critério técnico de sugestão.** A ordenação é por
  adequação técnica; o preço é coluna, não filtro.

**O arquivo nasceu vazio, de propósito**, e recebeu a primeira leva em 07/09/2026:
10 cotações da Shopee, todas do painel de afiliados, lidas pelo operador no
momento em que os links curtos foram gerados. Cada uma tem loja, data, condição,
disponibilidade e o título do anúncio — o mínimo para uma cotação valer. O campo
`origem_leitura` diz, em cada registro, que não foi a Aquametria que leu a página
(o egresso da nuvem barra `shopee.com.br`).

Continuam de fora os valores sem data de leitura que apareceram em busca
(R$ 649,90 para o Atman AT-3338; R$ 91,00 para o Roxin 200 W): sem data, sem
voltagem e sem confirmação de disponibilidade, seriam número inventado com
aparência de dado. E a **atualização recorrente segue barrada**: enquanto não
houver coleta a partir do próprio site, a série só cresce à mão — motivo pelo
qual a tela nunca crava preço no HTML, e sim mostra o valor com a data ao lado e
a frase de que ele muda na loja.

---

## 10. O que a semente de 15 produtos revelou

`ferramentas/validar-produtos.py` roda as regras sobre os dados. Resultado de
07/09/2026: **15 produtos, 0 erros, 3 avisos** — depois de corrigir 12 erros que
o próprio validador apontou na primeira execução (campo sem fonte, status
incoerente, voltagem gravada sem origem).

### Achado 1 — os fabricantes discordam entre si sobre turnover, não só do Brasil

| Filtro | Vazão | Volume declarado | Turnover implícito |
|---|---|---|---|
| Eheim classic 250 (2213) | 440 L/h | até 250 L | **1,76 x/h** |
| Atman AT-3338 | 1200 L/h | até 450 L | 2,67 x/h |
| SunSun HW-303B | 1400 L/h | até 350 L | 4,00 x/h |
| Seachem Tidal 55 | 1000 L/h | até 200 L | 5,00 x/h |
| Atman AT-3338S | 1500 L/h | 150 a 400 L | 3,75 a **10,0 x/h** |

O Bloco 2 já tinha encontrado a divergência entre o Eheim (1,8 x/h) e as regras
de bolso brasileiras (5 a 10 x/h). A semente mostra que **os próprios fabricantes
divergem entre si por 5,7 vezes** no mesmo mercado. A C3 tem material para
publicar a tabela acima como está — é a pergunta mais replicada do aquarismo
brasileiro respondida com atribuição, e ninguém no país publica isso.

### Achado 2 — a diferença de consumo entre filtros que "servem" ao mesmo aquário

`eficiencia_lh_por_w` vai de **34,3** (Atman AT-3338) a **166,7** L/h por W
(Seachem Tidal 55): 4,9 vezes. O Tidal está marcado `revalidar` justamente por
isso — um HOB trabalha com coluna baixíssima e pode mesmo ser muito eficiente,
mas 1000 L/h com 6 W precisa sair do manual lido antes de virar comparação de
conta de luz na C7. **O aviso V10 existe para isso: número bom demais é motivo
de reconferência, não de publicação.**

### Achado 3 — a linha popular brasileira não segue uma regra própria

Roxin HT-1300/Q3: 100 W para 50–150 L (0,67 W/L no teto), 200 W para até 200 L
(1,0 W/L), 300 W para 250–350 L (0,86 W/L). As faixas nem sequer se encostam de
forma contínua — entre 200 e 250 L não há modelo declarado. A C5 pode publicar a
série inteira e mostrar que "1 W por litro" não é o que o próprio fabricante faz.

### Achado 4 — voltagem é o gargalo do banco

De 13 equipamentos elétricos na semente, **9 não têm voltagem declarada em
nenhuma fonte**. Como voltagem é requisito de sugestão, o retrato de hoje é:

| Calculadora | Aptos | Barrados | Campo que mais barra |
|---|---|---|---|
| C3 vazão | 2 | 3 | `voltagem`, `coluna_maxima_m` |
| C5 aquecedor | **0** | 4 | `voltagem`, `faixa_ajuste_C` |
| C15 iluminação | **0** | 4 | `voltagem`, `fluxo_lm` |
| C12 mídia | 3 | 4 | `volume_filtragem_L` |
| C7 consumo | 12 | 1 | — |

Isso não é fracasso do modelo: é o modelo funcionando. Um banco que aceitasse
esses 15 registros como "prontos" sugeriria aquecedor sem dizer a voltagem, que é
o erro que queima equipamento do leitor.

### Achado 5 — na iluminação, o lúmen aparece; a voltagem, não

Contra a expectativa do Bloco 1, **3 das 4 luminárias declaram lúmen**
(3717 lm/35 W, 2400 lm/24 W, 5000 lm/60 W — eficácias de 83 a 106 lm/W, todas
plausíveis). O que falta é outra coisa: nenhuma declara voltagem, uma não declara
comprimento nenhum e outra não tem nem marca. E o par Sunsun ADE-400c (peça de
41 cm para aquário de 48 a 65 cm) provou que os dois campos de comprimento são
mesmo independentes.

### Achado 6 — mídia: duas áreas superficiais, nenhum método

Seachem Matrix declara >700 m²/L e Eheim SUBSTRAT pro cerca de 450 m²/L. Nenhum
publica o método de medição, então a C12 pode citar os dois com atribuição, mas
**não pode ranqueá-los**. Some-se a isso o contraste que o Bloco 2 já registrou:
a dosagem do fabricante de mídia (1,25 mL/L) contra o cesto do fabricante de
filtro (Eheim 2213: 3,0 L de mídia para 250 L = 12 mL/L) — uma ordem de grandeza
de diferença que ninguém no Brasil discute.

---

## 11. As regras, e o que cada uma protege

| Regra | O que verifica | Severidade |
|---|---|---|
| V1 | `id` único no banco inteiro, kebab-case sem acento | erro |
| V2 | todo campo técnico preenchido tem fonte que o sustente (campo `editorial` fica de fora) | erro |
| V3 | sanidade numérica: min ≤ max, valores positivos | erro |
| V4 | nenhum derivado gravado no arquivo de produto | erro |
| V5 | `ppfd_declarado` e `ppfd_distancia_cm` vêm em par | erro |
| V6 | fonte de marketplace não sustenta campo técnico | erro |
| V7 | nenhum campo de preço dentro de `produtos-*.json`; cotação aponta para produto existente | erro |
| V8 | status `completo` exige todos os obrigatórios | erro |
| V9 | `verificado_em` não está no futuro; acima de 180 dias exige `revalidar` | aviso |
| V10 | filtro com mais de 120 L/h por W é implausível | aviso |
| V11 | aquecedor com faixa declarada acima de 3x não dimensiona | aviso |
| V12 | registro com `conflitos[]` tem status `conflito` | erro |
| V13 | iluminação com lúmen e sem comprimento não pode ser sugerida | aviso |
| V14 | status `parcial` sem obrigatório faltante: status errado ou motivo não escrito | aviso |

Rodar antes de cada commit que toque o banco:

```
cd ilhas/aquametria && python3 ferramentas/validar-produtos.py
```

Sai 0 sem erros, 1 com erro. Avisos não reprovam: existem para virar tarefa de
coleta, não para travar o trabalho.

---

## 12. Limitações conhecidas do esquema v1

Escritas aqui para não serem redescobertas como surpresa:

1. **Potência é um número por produto, mas depende da voltagem.** O manual do
   Tidal 55 declara 6 W em 120 V e 5 W em 230 V. Hoje grava-se o de 120 V com a
   observação; a v2 precisa de potência por voltagem.
2. **Não existe entidade `especie`.** As fichas que a C8 (lotação) e o banco de
   compatibilidade (C10) exigem — tamanho adulto, temperatura, pH, GH, cardume
   mínimo, agressividade, zona de nado — são modelagem do Bloco 4. O esquema de
   produto não serve para elas: espécie não tem marca, modelo nem cotação.
3. **Dimensão física do filtro não é modelada.** `coluna_maxima_m` diz se a bomba
   vence a altura, mas não se o canister cabe no móvel. Falta largura × profundidade
   × altura, e quase nenhuma ficha brasileira publica.
4. **Ruído não é modelado.** É a segunda reclamação mais comum sobre canister e
   nenhuma fonte publica dB. Entra se e quando houver medição própria.
5. **Não há histórico por campo.** `verificado_em` existe por registro e por
   fonte; se um fabricante mudar a especificação de um modelo, o histórico da
   mudança é o histórico do Git, não um campo.
6. **`disponibilidade_br` envelhece rápido** e não tem data própria — hoje anda
   junto do `verificado_em` do registro.

---

## 13. Coletas que este bloco abre

Em ordem do que mais desbloqueia, integradas às 8 coletas que o Bloco 2 deixou:

1. **Voltagem dos 9 equipamentos sem o campo.** É o gargalo: destrava a C5 e a
   C15 inteiras. Sai da embalagem ou da loja, é barata e não depende de ninguém.
2. **`coluna_maxima_m` do SunSun HW-303B e do Tidal 55**, e `volume_filtragem_L`
   de todo canister — o campo que liga filtro e mídia, e que hoje barra 4 de 5
   filtros na C12.
3. **`faixa_ajuste_C` da linha Roxin na embalagem**, para resolver o conflito
   varejo-contra-varejo dos três registros.
4. **Reconferir o Tidal 55 no manual** (aviso V10) e o **Seachem Matrix na
   embalagem** (conflito de 2,1x), assim que houver egresso para os domínios de
   fabricante.
5. **Convenção editorial de cobertura da luminária**, para virar constante e
   liberar o critério da C15 com `comprimento_luminaria_cm`.
6. **Primeiras cotações de preço com data**, quando houver como ler a página da
   loja no dia.
7. Segue valendo a fila do Bloco 2: `u-vidro-aquario` (libera a C5 física e a
   C6), porosidade do substrato, espessura de vidro, mínimas do INMET, tarifas
   ANEEL, PPFD e as fichas das 8 espécies iniciais.

---

## 14. Bloqueio de publicação

Tudo com `publicar: false`. Além disso, três travas próprias deste banco:

- **Nenhum produto com `rascunho` ou `revalidar` é sugerido por calculadora.**
- **Nenhum campo técnico sai na tela sem o selo da fonte**: `fabricante-via-busca`
  sai com "a confirmar no manual"; `transcrita-varejo`, com "confira a embalagem".
- **Nenhum link de afiliado substitui a URL de origem.** A procedência do preço
  tem de continuar auditável depois do desembarque — é o único ativo que a marca
  tem e o motivo de o banco existir.

---

## 15. O link de afiliado (esquema v2, 07/09/2026)

O link é **campo de produto**; o preço daquele anúncio é **cotação datada**. Um
não substitui o outro, e nenhum dos dois substitui a URL de origem do dado
técnico: a procedência da especificação continua sendo o fabricante ou o varejo
especializado, nunca a loja que paga comissão.

```json
"afiliado": {
  "plataforma": "shopee",
  "url": "https://s.shopee.com.br/…",
  "sub_id_1": "aquametria",
  "sub_id_2": "C5",
  "rel": "sponsored",
  "verificado_em": "2026-09-07",
  "anuncio_shopee": "Termostato Com Aquecedor Roxin HT-1300 - Q3 - 300w - 220v",
  "voltagem_anuncio": "220"
}
```

- `sub_id_2` é o código da calculadora (C3, C5, C12, C15). É o que permite ler no
  painel **qual calculadora vende** — sem ele, a receita chega anônima e não há
  como decidir o que construir a seguir.
- `anuncio_shopee` guarda o título exato. Link curto de marketplace pode ser
  reapontado para outro produto sem aviso; o título é como se confere depois.
- `voltagem_anuncio` é a voltagem **do anúncio**, não do produto. Anúncio de
  marketplace é fonte de nível 6 e não sustenta campo técnico: o campo `voltagem`
  do registro continua `null` até um fabricante ou varejista declarar. A tela
  usa `voltagem_anuncio` só para avisar qual versão o link abre.
- Sem anúncio, `plataforma` é `null` e `motivo` é obrigatório. Produto sem link
  **não aparece** no bloco de produto: resposta sem produto é melhor que produto
  errado.
- **Variante errada é defeito, não aproximação.** O anúncio da Ista na Shopee é
  da luminária de 45 cm (7,6 W, 810 lm); o registro que existia era o de 60 cm
  (35 W, 3717 lm). Colar aquele link neste registro faria a C15 prometer 3717 lm
  e entregar 810. Por isso entrou um registro novo (`ista-i-401-45`) e o de 60 cm
  ficou sem link.
- `dados/afiliados-sem-produto.json` guarda o link gerado que ainda **não** tem
  registro no banco (hoje, um LED genérico de 30–60 cm). Fica fora do banco de
  propósito: link sem ficha verificada não pode ser sugerido por calculadora.

A regra **V15** do validador executa isso: todo produto tem `afiliado`; com
plataforma preenchida exige URL https, os dois `sub_id`, o título do anúncio e
`rel: "sponsored"`, e proíbe qualquer campo de preço lá dentro; com plataforma
`null` exige o motivo. O relatório do validador passou a separar, por
calculadora, quem está **apto com link** de quem está **apto sem link** — este
segundo grupo é conteúdo de ficha, não sugestão.

Na renderização, sem exceção: `rel="sponsored"`, `target="_blank"`,
`rel="noopener"`, e aviso visível na página de que a Aquametria pode receber
comissão.

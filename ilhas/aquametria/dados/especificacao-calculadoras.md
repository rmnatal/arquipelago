---
titulo: Especificação das calculadoras da Aquametria
bloco: 2
gerado_em: 2026-09-07
depende_de: dados/constantes-calculadoras.json
publicar: false
---

# Especificação das calculadoras — Aquametria

Bloco 2 do playbook. Define **8 calculadoras** derivadas dos 15 clusters do
Bloco 1, cada uma com entradas, fórmula, faixas de saída, a fonte de cada
constante e os produtos que a resposta deve sugerir.

Nenhuma constante aparece aqui por conta própria: toda ela tem um `id` em
`dados/constantes-calculadoras.json`, com fonte, data e status. **Constante
com status `pendente` não entra em fórmula publicada** — a especificação diz,
em cada caso, o que fica de fora e qual coleta libera.

## Índice

| # | Calculadora | Cluster | Estado |
|---|---|---|---|
| C1 | Litragem e volume útil (núcleo) | C1 | especificada — libera as outras 7 |
| C2 | Peso do aquário cheio e carga no piso | C2 | especificada (sem espessura de vidro) |
| C3 | Vazão do filtro e turnover | C3 | especificada |
| C5 | Potência do aquecedor por delta térmico | C5 | especificada em duas vias (a física está bloqueada) |
| C7 | Consumo elétrico e custo mensal | C7 | especificada |
| C8 | Lotação e aquário mínimo | C8 | especificada para 8 espécies |
| C12 | Mídia filtrante: volume, ordem e troca | C12 | PUBLICADA 08/09/2026 |
| C15 | Iluminação e fotoperíodo | C15 | especificada (lm/L; PPFD pendente) |

Fora do lote inicial, com o critério de entrada: C4, C6, C9, C10, C11, C13,
C14 — ver a seção final.

---

## 1. Contrato de resposta (vale para as 8)

Toda calculadora devolve o mesmo objeto. **Nunca um número seco.** Cada
extremo da faixa carrega o critério que o define e a constante (logo, a
fonte) de onde saiu.

```json
{
  "calculadora": "c3-vazao-filtro",
  "versao": 1,
  "entradas": { "volume_real_L": 180, "tipo_aquario": "comunitario" },
  "resposta": {
    "grandeza": "vazão nominal do filtro",
    "unidade": "L/h",
    "faixa": { "min": 320, "max": 1800 },
    "extremos": [
      {
        "limite": "min",
        "valor": 320,
        "criterio": "dimensionamento do próprio fabricante (Eheim classic 250: 440 L/h para 250 L ⇒ 1,8 x/h)",
        "constante": "eheim-classic-250-2213"
      },
      {
        "limite": "max",
        "valor": 1800,
        "criterio": "teto da regra de bolso brasileira (10 renovações por hora)",
        "constante": "turnover-comunitario-br"
      }
    ],
    "leitura": "As fontes brasileiras pedem de 3 a 6 vezes mais vazão do que o próprio fabricante do filtro. Mostramos as duas.",
    "avisos": [ { "tipo": "metodologia", "texto": "..." } ],
    "constantes_usadas": ["turnover-comunitario-br", "eheim-classic-250-2213"],
    "produtos_sugeridos": {
      "entidade": "filtro",
      "criterio": { "vazao_nominal_lh": [320, 1800], "coluna_maxima_m": ">= altura informada" }
    }
  }
}
```

Regras do contrato:

1. **Faixa sempre.** Se as fontes convergirem num único valor, a faixa tem
   min = max e o critério diz que houve convergência.
2. **Atribuição sempre.** Cada extremo cita a constante; a tela mostra fonte
   e data de verificação ao lado.
3. **Divergência é conteúdo, não defeito.** Quando as fontes discordam, a
   resposta diz de quanto é a discordância. Foi isso que o Bloco 1 encontrou
   em quase todos os clusters, e é a metodologia da marca.
4. **Status na tela.** Constante `transcrita-varejo` sai com "confira a
   embalagem"; `fabricante-via-busca` sai com "a confirmar no manual";
   `convencao-editorial` sai com "valor inicial, ajuste para o seu caso".
5. **Nada de veredito onde há risco.** Carga estrutural e dosagem não
   recebem "pode" ou "não pode" — recebem o número e para quem perguntar.
6. **A resposta é linkável e citável.** Cada resposta tem um permalink com as
   entradas na query string; é isso que faz uma loja ou um fórum citar a
   Aquametria sem que o Raphael apareça.

---

## 2. Estado de aquário compartilhado

O Bloco 1 concluiu que C1 alimenta 8 dos 15 clusters. Portanto **não são 8
formulários isolados**: existe um objeto `aquario` único, preenchido uma vez,
lido por todas as calculadoras.

```json
{
  "apelido": "meu 120",
  "medidas": { "comprimento_cm": 80, "largura_cm": 40, "altura_cm": 40, "tipo_medida": "externa" },
  "vidro": { "espessura_mm": 8 },
  "agua": { "altura_lamina_cm": 37, "borda_livre_cm": 3 },
  "substrato": { "altura_cm": 5, "tipo": "cascalho-fino", "porosidade_medida": null },
  "decoracao": { "volume_rochas_L": null },
  "volumes": { "bruto_L": 128, "interno_L": 118.4, "lamina_L": 109.5, "real_L": 109.5, "real_incerteza": "substrato não descontado" },
  "perfil": { "tipo_aquario": "plantado-low-tech", "tampado": true },
  "termica": { "temp_alvo_C": [24, 28], "temp_min_ambiente_C": 14, "cidade": null },
  "lotacao": [ { "especie_id": "acara-bandeira", "quantidade": 4 } ],
  "equipamentos": { "filtro_id": null, "aquecedor_w": null, "luz_lm": null, "luz_w": null }
}
```

- Persistência: `localStorage` do visitante, chave **`aquametria.aquario`** (a
  especificação dizia `aquametria_aquario`; a chave publicada na C1, em
  07/09/2026, é a com ponto, e é ela que vale — as outras calculadoras leem
  desta), mais
  a query string do permalink. Nada de conta, nada de login, nada de coleta
  de dado pessoal.
- `volumes.real_L` é a **única** entrada de volume que as outras
  calculadoras leem. Quem muda uma medida em C1 vê C3, C5, C7, C8, C12 e C15
  se atualizarem.
- O objeto é o contrato entre os snippets. Um snippet por calculadora, todos
  lendo e escrevendo o mesmo estado. Nomes de snippet descritivos, nunca
  numerados (`Aquametria Calculadora de Litragem`, e assim por diante).

---

## 3. C1 — Litragem e volume útil  *(núcleo)*

**Cluster C1 (25 consultas).** Padrões: "aquário de {C}x{L}x{A} quantos
litros", o inverso litros → medidas, desconto de substrato, bruta x real.

### Entradas
| Campo | Unidade | Obrigatório | Observação |
|---|---|---|---|
| comprimento, largura, altura | cm | sim | com seletor **medida externa / interna** |
| espessura do vidro | mm | não | sem ela, não há volume interno |
| altura da lâmina de água | cm | não | valor inicial = altura − `borda-livre-padrao` (3 cm, **convenção da Aquametria, não é dado técnico**) |
| altura do substrato | cm | não | entra como aviso, não como desconto — ver abaixo |
| volume de rochas e decoração | L | não | desconto direto, se o usuário souber |
| **inverso:** volume desejado + duas medidas | L, cm | — | devolve a terceira medida |

### Fórmulas
```
V_bruto (L)     = C × L × A / 1000                    [cm]
C_int           = C − 2·e/10 ;  L_int = L − 2·e/10 ;  A_int = A − e/10
V_interno (L)   = C_int × L_int × A_int / 1000
V_lamina (L)    = C_int × L_int × altura_lamina / 1000
V_real (L)      = V_lamina − volume_rochas
```
(`e` em mm; a base desconta uma espessura, as laterais duas. Se o usuário
informou medidas internas, `C_int = C` e o volume interno é o bruto.)

### Saídas
1. **Volume bruto** — o número que o vendedor usa. É o que a busca pergunta.
2. **Volume interno** — descontado o vidro. Só aparece com a espessura.
3. **Volume real de referência** = `V_lamina − rochas`. É o que vai para o
   estado compartilhado e o que as outras calculadoras usam.
4. **Faixa de incerteza declarada**: "o substrato reduz este volume; a
   Aquametria ainda não publica de quanto — ver por quê".

### O desconto de substrato fica de fora da v1, e isso é deliberado

Descontar substrato exige a porosidade do leito (a água que fica *entre* os
grãos). O corpus do Bloco 1 tem, para densidade de substrato, `1 a 2 kg/L`
(guiadoaquarismo) contra `1 kg ≈ 1 L` (peixeseaquarismo) — **100 % de
diferença** — e nenhuma fonte publica porosidade. Constantes
`substrato-densidade` e `substrato-porosidade` estão `pendente`, logo estão
proibidas em fórmula.

Consequência assumida: `V_real` fica **superestimado**. A direção do erro
importa e a especificação a declara:

| Calculadora | Efeito de superestimar o volume | Direção |
|---|---|---|
| C3 filtro | pede vazão maior | segura |
| C5 aquecedor | pede potência maior | segura |
| C12 mídia | pede mais mídia | segura |
| C7 custo | custo estimado maior | conservadora |
| C8 lotação | permitiria mais peixe | **insegura** → C8 aplica o volume da lâmina *menos* a camada de substrato inteira (pior caso) |
| dosagem | **overdose** | **insegura** → é uma das razões de C13 não entrar no lote inicial |

**Coleta que libera o desconto** (protocolo próprio, inédito no BR): recipiente
graduado, substrato seco até uma marca conhecida, água até cobrir os grãos;
porosidade = água adicionada ÷ volume do recipiente. Medir para areia grossa,
cascalho fino e substrato fértil, três repetições, foto de cada medição. Isso
vira artigo do Bloco 4 e constante com fonte própria — procedência gerada em
casa, que é exatamente o ativo da marca.

### Produtos sugeridos
Nenhum. C1 é o núcleo: sua função é alimentar as outras e capturar a maior
consulta genérica do nicho.

### Constantes usadas
`borda-livre-padrao` (convenção). Recusadas: `substrato-densidade`,
`substrato-porosidade`.

---

## 4. C2 — Peso do aquário cheio e carga no piso

**Cluster C2 (11 consultas).** "quanto pesa aquário de {N} litros",
"laje/móvel aguenta", "espessura para {N} litros".

### Entradas
Vêm do estado: medidas, espessura do vidro, `V_real`. Mais:
peso do substrato (kg, se souber), peso das rochas (kg), peso do móvel (kg,
opcional), ambiente (dormitório/sala · área de serviço · corredor).

### Fórmulas
```
massa_agua (kg)   = V_real × 1,00            [agua-densidade-25c = 0,997; arredondado, declarado na tela]
area_vidro (m²)   = base + 2 frentes + 2 laterais            [pelas medidas externas]
massa_vidro (kg)  = area_vidro × espessura_mm × 2,5          [vidro-densidade: 2500 kg/m³ = 2,5 kg/m²·mm]
massa_total (kg)  = massa_agua + massa_vidro + substrato + rochas + movel
carga (kgf/m²)    = massa_total / (C × L em m²)
```

### Saídas
1. **Faixa de peso**: mínimo = só água + vidro; máximo = com substrato,
   rochas e móvel informados.
2. **Carga distribuída** em kgf/m², com a área de apoio usada no cálculo.
3. **Comparação de referência**, não veredito: NBR 6120:2019 prevê carga
   acidental de 1,5 kN/m² (≈ 153 kgf/m²) para dormitório e sala, 2,0 para
   área de serviço, 3,0 para corredor de acesso público
   (`carga-acidental-residencial`, `norma-via-secundaria`).
4. **Aviso obrigatório, em destaque**: carga de norma é *distribuída* e é
   valor de projeto; um aquário apoiado em quatro pés é carga *concentrada*.
   Um aquário de 200 L costuma passar de 300 kgf/m² na sua pegada e ainda
   assim ficar seguro sobre uma viga — ou não ficar sobre um vão de laje.
   **Quem decide é engenheiro, com o projeto do prédio na mão.** A Aquametria
   dá o número, não a autorização.

### Espessura de vidro NÃO sai na v1

É a segunda consulta do cluster e a resposta fica retida de propósito: a
fórmula de espessura depende de tensão admissível de flexão e coeficiente de
segurança, e **não temos essa fonte** — nem no corpus, nem em fabricante de
vidro para uso em aquário. Errar aqui não gera resposta ruim, gera vidro
estourado e casa alagada. Libera quando houver: (a) tensão admissível do
vidro float publicada por fabricante ou norma, e (b) o coeficiente de
segurança adotado, citável. Até então a página responde a pergunta com a
metodologia e diz por que não publica número — o que, em domínio novo, vale
mais que uma tabela copiada de blog.

### Produtos sugeridos
Nenhum na v1 (móvel e suporte não entram no banco do Bloco 3). A resposta
puxa C3 e C5 pelo estado compartilhado.

### Constantes usadas
`agua-densidade-25c`, `vidro-densidade`, `carga-acidental-residencial`.

---

## 5. C3 — Vazão do filtro e turnover

**Cluster C3 (65 consultas)** — "melhor filtro para aquário de {N} litros" é
o padrão mais replicado da web brasileira. Inclui o inverso ("filtro de {X}
L/h serve para quantos litros") e "{modelo} até quantos litros".

### Entradas
`V_real` e `tipo_aquario` do estado; carga de peixes (leve · média · pesada,
ou herdada de C8); altura da coluna de água até o filtro (m, para canister);
tipo de filtro pretendido (canister · hang-on · interno · sump).

### Fórmulas
```
Q (L/h) = V_real × turnover

turnover por perfil:
  comunitário        5 – 10 x/h    [turnover-comunitario-br]
  comunitário (cons.) 4 – 5 x/h    [turnover-comunitario-mybest]
  plantado            3 – 5 x/h    [turnover-plantado]
  marinho com sump    sump ≥ 20 % do volume  [sump-proporcao-minima]

contraponto do fabricante:
  Eheim classic 250 (2213): 440 L/h nominais para até 250 L ⇒ 1,76 x/h
  [eheim-classic-250-2213]
```

### O achado que a página existe para publicar

O fabricante dimensiona **1,8 renovações por hora**; a web brasileira pede
**5 a 10**. É uma divergência de 3 a 6 vezes, e **nenhuma fonte BR do corpus
confronta as duas**. A resposta da C3 mostra a faixa inteira, do
dimensionamento do fabricante ao teto da regra de bolso, e explica os dois
lados: o fabricante mede vazão livre e conta com a mídia certa; as regras de
bolso compensam sujeira, perda de carga e lotação alta com folga.

### Vazão real não é vazão nominal — e não inventamos o fator

Vazão nominal é medida sem mídia e com coluna zero; o 2213 declara coluna
máxima de 1,5 m. A perda percentual com mídia suja não tem fonte no corpus,
então **a v1 não aplica fator de derating nenhum**. Em vez disso:
- dimensiona pela vazão **nominal** e diz que a real é menor;
- barra modelos cuja coluna máxima seja menor que a altura informada;
- oferece o **protocolo do balde** (medir a vazão real: tempo para encher um
  volume conhecido na saída do filtro; L/h = volume ÷ tempo). Medição própria
  outra vez, em lugar de constante inventada.

### Saídas
Faixa L/h com critério em cada extremo · leitura inversa (dado Q, faixa de
litragem atendida por cada critério) · veredito para um modelo escolhido do
banco ("o fabricante declara até 250 L; pela regra de bolso brasileira
cobriria 44 a 88 L") · avisos de coluna e de mídia.

### Produtos sugeridos
Entidade `filtro`. Campos que o Bloco 3 precisa entregar: `marca`, `modelo`,
`tipo`, `vazao_nominal_lh`, `potencia_w`, `volume_atendido_declarado_L`,
`coluna_maxima_m`, `volume_de_filtragem_L`, `midia_inclusa`, `preco`,
`fonte`, `verificado_em`.
Critério de sugestão: `vazao_nominal_lh` dentro da faixa (ordenado por
proximidade do meio da faixa), `coluna_maxima_m ≥` altura informada, tipo
compatível. A resposta mostra, para cada modelo, o turnover que ele entrega
naquele aquário — não só se "serve".
Modelos que as buscas já citam e devem estar no banco: Sunsun HW-303B, Atman
AT-3338 e HF-800, Seachem Tidal 35 e 55, Roxin Q3 e Q5, Hopar J-226 e 3028,
Boyu FEF-230, Eheim Classic 2213.

### Constantes usadas
`turnover-comunitario-br`, `turnover-comunitario-mybest`, `turnover-plantado`,
`sump-proporcao-minima`, `eheim-classic-250-2213`.

---

## 6. C5 — Potência do aquecedor por delta térmico

**Cluster C5 (34 consultas).** É o **vácuo de conteúdo nº 2** do Bloco 1:
todas as fontes repetem "1 W/L" e nenhuma pergunta a mínima da cidade.
Calculadora que pede o delta térmico real é inédita no Brasil.

### Entradas
`V_real` e `tampado` do estado · temperatura-alvo (da ficha da espécie, ou
manual) · **temperatura mínima do ambiente onde o aquário fica** (entrada do
usuário) · região (para aplicar a leitura do Sul).

### Duas vias, publicadas lado a lado

**Via A — síntese atribuída das regras de bolso (é o que a v1 entrega).**
Não é uma média: é o conjunto das regras aplicáveis, cada uma com a condição
que o *próprio autor* declarou.

```
ΔT = temp_alvo − temp_min_ambiente

ΔT ≤ 10 °C   → 1,0 a 1,5 W/L   [wl-delta-ate-10, ReefFlow]
região Sul   → até 2,0 W/L     [wl-sul, Casa da Ada]
genérico     → 1,0 W/L         [wl-generico]  |  1,3 W/L  [wl-ehow]

P_min = V_real × menor W/L aplicável
P_max = V_real × maior W/L aplicável
```
Se `ΔT > 10 °C`, **nenhuma fonte do corpus cobre o caso**: a resposta diz
isso com essas palavras, entrega a faixa das regras genéricas como piso e
avisa que o piso pode ser insuficiente. Extrapolar a regra de bolso para
além do delta que a fonte declarou seria inventar constante.

**Via B — cálculo físico `P = U · A · ΔT`: bloqueada.**
Falta `u-vidro-aquario` (status `pendente`): o coeficiente global de troca do
vidro do aquário com convecção natural nas duas faces, mais a parcela de
evaporação na lâmina livre, que costuma dominar. Sem fonte, não sai. Libera
com: coeficiente U por espessura em catálogo técnico de vidro plano +
tratamento da perda por evaporação em superfície livre. **É a entrega que
torna a Aquametria a única referência do nicho no Brasil** — vale um bloco
próprio.

### Saídas
1. Faixa de potência em W, cada extremo com a regra e o autor.
2. **Potência comercial mais próxima** na linha 25/50/75/100/150/200/300 W
   (`eheim-jager-linha-comercial`).
3. **Confronto com o dimensionamento do fabricante**, que é o segundo achado
   do bloco: a Eheim declara o modelo de 200 W para **30 a 400 L** — uma faixa
   de 13 vezes. Serve para escolher a potência comercial; não serve para
   dimensionar. A resposta diz isso.
4. Avisos: dois aquecedores de metade da potência falham melhor que um
   grande (falha aberta não cozinha o aquário, falha fechada não o congela) —
   entra como **raciocínio editorial identificado como tal**, não como
   constante; termostato e verificação com termômetro independente; aquário
   destampado perde mais.

### Produtos sugeridos
Entidade `aquecedor`. Campos do Bloco 3: `marca`, `modelo`, `potencia_w`,
`volume_declarado_min_L`, `volume_declarado_max_L`, `tipo`
(resistência/titânio), `termostato`, `faixa_ajuste_C`, `preco`, `fonte`,
`verificado_em`. A sugestão mostra a potência calculada **e** o volume que o
fabricante declara, com a diferença explícita entre as duas.

### Constantes usadas
`wl-delta-ate-10`, `wl-sul`, `wl-generico`, `wl-ehow`,
`eheim-jager-linha-comercial`, `especies-parametros-iniciais`.
Recusadas: `u-vidro-aquario`, `temperatura-minima-por-cidade` (por isso a
mínima é entrada do usuário).

---

## 7. C7 — Consumo elétrico e custo mensal

**Cluster C7 (11 consultas).** {W} × {h/dia} × tarifa.

### Entradas
Do estado: potência do aquecedor, da luz e da bomba. Mais: fotoperíodo (de
C15), ciclo de trabalho do aquecedor (faixa 8–10 h/dia como valor inicial),
outros equipamentos (aerador, cooler), **tarifa em R$/kWh**.

### Fórmulas
```
kWh_mes = Σ ( W_i × h_i/dia × 30 ) / 1000

filtro/bomba : 24 h/dia
luz          : fotoperíodo (6 a 10 h/dia) [fotoperiodo]
aquecedor    : 8 a 10 h/dia [ciclo-de-trabalho-aquecedor] — NÃO 24 h
custo        = kWh_mes × tarifa
```

### O erro que todo mundo comete e que a página corrige

O corpus registra 8 h/dia (Seu Pet Saudável) e 10 h/dia (Grupo Sarlo) de
ciclo efetivo do aquecedor; **todas as outras fontes multiplicam a potência
por 24 h** e erram o custo por 2,4 a 3 vezes. A resposta mostra as duas
contas lado a lado — a certa e a que circula por aí.

### Tarifa é entrada, não constante
`tarifa-energia-kwh` está `pendente`. A tela pede o valor **da fatura do
usuário** (total pago ÷ kWh consumidos), que já embute ICMS, PIS/COFINS e
bandeira — mais exato que qualquer média que pudéssemos publicar. Coleta
futura: tarifas homologadas ANEEL por distribuidora, para virar valor inicial
por estado.

### Saídas
Faixa de kWh/mês e de R$/mês · ranking por equipamento (quem pesa mais na
conta — quase sempre o aquecedor, não a luz) · comparação verão/inverno (o
ciclo do aquecedor acompanha o ΔT de C5) · custo anual.

### Produtos sugeridos
Entidades `filtro`, `aquecedor` e `iluminacao`, ordenadas por `potencia_w`
para a mesma faixa de atendimento: a resposta mostra a economia mensal em
reais de escolher o modelo mais eficiente. É o gancho de afiliado mais
honesto do site — o número que o próprio visitante confere na conta de luz.

### Constantes usadas
`ciclo-de-trabalho-aquecedor`, `fotoperiodo`,
`eheim-jager-linha-comercial`. Recusada: `tarifa-energia-kwh`.

---

## 8. C8 — Lotação e aquário mínimo

**Cluster C8 (57 consultas)** — a maior cauda longa do nicho: "quantos
{espécie} em {N} litros".

### Entradas
`V_real` (aqui usado no **pior caso**: lâmina menos a camada inteira de
substrato — ver C1) · lista de espécies e quantidades, do banco de fichas ·
inverso: "quero N indivíduos de X" → litragem mínima.

### Fórmulas — três critérios, publicados juntos
```
soma_cm = Σ ( tamanho_adulto_cm × quantidade )

critério permissivo   : soma_cm ≤ V_real / 1        [lotacao-1cm-por-litro]
critério conservador  : soma_cm ≤ V_real / 4        [lotacao-litros-por-cm, extremo 4 L/cm]
critério intermediário: soma_cm ≤ V_real / 1,5      [lotacao-litros-por-cm, extremo 1,5 L/cm]

regra específica de espécie SEMPRE prevalece:
  kinguio : 100 L + 40 L por indivíduo adicional    [lotacao-kinguio]
  oscar   : 100 L + 100 L por indivíduo             [lotacao-oscar]
```

### Duas recusas explícitas
- **"Regra dos 10 %"**: `pendente`. A fonte não diz 10 % de quê
  (comprimento? massa? volume?). Regra cuja definição não conseguimos
  enunciar não entra em fórmula.
- **Espécie sem ficha com fonte não é aceita.** A v1 abre com as **8
  espécies** de `especies-parametros-iniciais` (betta, kinguio, guppy,
  acará-disco, tetra, acará-bandeira, barbo-sumatra, paulistinha). Cada
  espécie nova exige ficha com fonte e data. Em domínio novo, 8 páginas com
  dado real valem mais que 300 vazias — e cauda longa vazia causa
  desindexação em bloco.

### Saídas
Ocupação em % por critério (três barras, não uma) · veredito com o critério
de cada extremo ("folgado pela regra clássica, superlotado pelo critério
conservador — a diferença entre as duas é de 4 vezes, e é assim que as fontes
brasileiras estão") · litragem mínima recomendada · cardume mínimo e proporção
macho/fêmea (C9, quando a ficha trouxer) · alerta de temperatura incompatível
entre espécies (interseção das faixas de `especies-parametros-iniciais`) ·
encaminhamento para o banco de compatibilidade (C10).

### Produtos sugeridos
Nenhum diretamente. Quando o veredito é "superlotado", a resposta encaminha
para C3 (filtro maior) e C1 (aquário maior) pelo estado compartilhado —
nunca sugere comprar peixe.

### Constantes usadas
`lotacao-1cm-por-litro`, `lotacao-litros-por-cm`, `lotacao-kinguio`,
`lotacao-oscar`, `especies-parametros-iniciais`. Recusada:
`lotacao-regra-10-porcento`.

---

## 9. C12 — Mídia filtrante: volume, ordem e troca

**Cluster C12 (14 consultas).** É o **vácuo de conteúdo nº 1**: nenhuma fonte
brasileira publica quantidade de mídia biológica por litragem ou por vazão.

### Entradas
`V_real` · vazão do filtro (de C3) · modelo do filtro (traz o volume de
filtragem do banco) · carga de peixes (de C8) · tipo de aquário.

### Fórmulas — QUATRO âncoras de fabricante, que discordam por 10x
Atualizado em 08/09/2026: a coleta da construção da C12 levou de duas para
quatro as dosagens declaradas, e de uma para duas as âncoras de mídia total.
```
mídia biológica, dosagem declarada pelo fabricante DA MÍDIA:
   1,25 mL/L  [seachem-matrix-dosagem, leitura "250 mL para 200 L"]
   2,64 mL/L  [seachem-matrix-dosagem, leitura "1 L para 100 gal"]
   5,00 mL/L  [jbl-micromec-dosagem: 650 g = 1 L para 200 L]
  12,50 mL/L  [ocean-tech-bio-glass-dosagem: 1 L para cada 80 L]
  ⇒ as duas primeiras são da própria copy da Seachem e conflitam por 2,1x
  ⇒ do piso ao teto vão 10x, e a Ocean Tech é a única marca BRASILEIRA
    que publica o número

O PARADOXO DA ÁREA (é o eixo do artigo pareado):
  área declarada × dosagem declarada = área entregue por litro de ÁGUA
  Seachem Matrix    >700 m2/L × 1,25 mL/L =  0,88 m2 por litro de água
  JBL MicroMec      1500 m2/L × 5,00 mL/L =  7,5  m2 por litro de água
  Ocean Tech        1500 m2/L × 12,5 mL/L = 18,8  m2 por litro de água
  ⇒ 21x de diferença. Se a área fosse o critério, convergiriam — e a marca
    que declara MAIS área é a que pede DEZ VEZES mais mídia, ou seja, a
    relação é a inversa da esperada. Nenhuma publica método de medição.

volume total de cesto (mecânica + biológica + química), declarado pelo
fabricante DO FILTRO, como volume de filtragem ÷ volume atendido:
  12,0 mL/L   [eheim-classic-250-2213: 3,0 L para até 250 L]
   6,0 mL/L   [seachem-tidal-55: 1,2 L para até 200 L]
   3,6 a 10,7 [atman-at-3338: ficha de varejo ambígua, 1,6 L ou 4,8 L]
   8,8 a 26,3 [atman-at-3338s: ficha ambígua, 3,5 L ou 10,5 L]
  ⇒ a Seachem é fabricante de mídia E de filtro, e as duas declarações dela
    não se falam: 1,25 mL/L como marca de mídia, 6,0 mL/L de espaço como
    marca de filtro

carvão ativado : 1 a 2 g/L, trocar a cada 15 a 30 dias  [carvao-ativado]
perlon         : trocar semanal a quinzenal             [perlon-troca]
cerâmica       : substituir parcialmente a cada 6 a 12 meses [ceramica-regeneracao]
ordem no canister: cerâmica/argila → perlon → carvão → perlon → cerâmica → perlon
                                                          [ordem-midias-canister]
```

### Como a resposta trata o conflito
Não escolhe. Publica **as quatro dosagens atribuídas em uma tabela e as âncoras
de mídia total em outra**, separadas porque respondem perguntas diferentes: a
segunda família inclui mecânica e química e por isso é naturalmente maior. Todas
as dosagens ficam marcadas como *a conferir na embalagem* — as páginas dos
fabricantes não puderam ser lidas direto (egresso HTTP bloqueado para
`seachem.com`, `jbl.de` e as lojas brasileiras) e os números vieram por resultado
de busca, reconfirmados em varejo especializado que replica a mesma ficha.
**Esta é, pelo levantamento do Bloco 1, a primeira publicação brasileira de mL de
mídia biológica por litro de água com fonte de fabricante.** Faz da C12 a peça de
autoridade do site.

### O teto físico — a saída que nenhuma fonte publica (v1.0.0, 08/09/2026)
A dosagem só vale se a mídia couber. Escolhido o filtro (ou digitado o volume do
cesto), a C12 devolve, para cada dosagem, **quanto do volume útil de mídia a
camada biológica sozinha ocuparia** — e diz, quando estoura, que o problema não
é a mídia, é o filtro. É conta trivial e não a encontramos publicada em português.

### O que a C12 se RECUSA a publicar (declarado na tela)
- **Proporção entre as camadas** do cesto: nenhuma fonte do corpus reparte o
  volume em porcentagens (`proporcao-entre-camadas-do-cesto`, pendente). Publica
  a ORDEM, que tem fonte.
- **Conversão de grama em mililitro** no carvão: falta
  `densidade-aparente-carvao-ativado` (pendente). A regra BR (1 a 2 g/L, troca em
  15 a 30 dias) e a declaração do fabricante (MatrixCarbon, 0,625 mL/L, "vários
  meses") saem lado a lado, cada uma na sua unidade. A FREQUÊNCIA compara sem
  conversão: 4 a 10 vezes mais trocas na regra BR do que o fabricante manda.
- **Ranking por área de superfície**: nenhum fabricante publica o método.
- **Dimensionamento de mídia sem dosagem declarada** (Eheim Substrat pro): sai no
  cartão sem número de compra, dizendo por quê.
- **Prazo de validade da mídia biológica**: só a substituição PARCIAL de 6 a 12
  meses, que tem fonte.

### A crítica de fundo, que o artigo pareado desenvolve
As quatro dosagens são por litro de ÁGUA, mas o trabalho da mídia biológica
depende da amônia que entra — ou seja, da carga de peixes, que NENHUMA das
declarações pergunta. Fechar isso exigiria `taxa-de-nitrificacao-por-area`
(pendente): amônia processada por dia por área colonizada, em temperatura e pH
declarados. Existe na literatura de engenharia sanitária; não achamos tradução
para aquário com fonte citável em português.

### Saídas
Volume (mL/L e total) de cada camada, com o critério de cada âncora · gramas
de carvão · **cronograma de troca com datas calculadas** a partir da data de
montagem (perlon toda semana, carvão em 15–30 dias, cerâmica em 6–12 meses) ·
ordem de empilhamento, com o aviso de conferir o manual do próprio modelo,
porque cada fabricante especifica a sua · gatilhos de TPA por nitrato
(`nitrato-limites`: > 40 ppm troca urgente; ≤ 20 ppm para sensíveis; 5–10 ppm
em plantado) e percentual de TPA (`tpa-percentual`, 10–30 % / 25–30 % semanal
/ teto de 50 %) com a diferença térmica tolerada (`tpa-diferenca-termica`:
até 1 °C; acima de 2 °C, choque).

### Aviso obrigatório
Nunca lavar toda a mídia biológica de uma vez, nunca em água de torneira: o
cloro mata a colônia nitrificante e o aquário volta ao ciclo. Vai como
**mecanismo explicado**, não como número.

### Produtos sugeridos
Entidade `midia`. Campos do Bloco 3: `marca`, `modelo`, `tipo`
(biológica/mecânica/química), `volume_embalagem_L`, `peso_g`,
`area_superficial_m2_por_L`, `volume_atendido_declarado_L`, `preco`, `fonte`,
`verificado_em`. A sugestão calcula **quantas embalagens** o aquário precisa e
o custo por litro tratado — comparação que nenhum varejo brasileiro publica.

### Constantes usadas
`seachem-matrix-dosagem`, `jbl-micromec-dosagem`, `ocean-tech-bio-glass-dosagem`,
`seachem-matrixcarbon-dosagem`, `seachem-purigen-dosagem`,
`eheim-classic-250-2213`, `seachem-tidal-55-midia`, `carvao-ativado`,
`perlon-troca`, `ceramica-regeneracao`, `ordem-midias-canister`,
`nitrato-limites`, `tpa-percentual`, `tpa-diferenca-termica`.
Recusadas por falta de fonte: `proporcao-entre-camadas-do-cesto`,
`densidade-aparente-carvao-ativado`, `taxa-de-nitrificacao-por-area`.

### Estado
**PUBLICADA em 08/09/2026**, v1.0.0, em `/calculadora-de-midia-filtrante/`,
pareada com o artigo `/quanta-midia-biologica-o-aquario-precisa/`.

---

## 10. C15 — Iluminação e fotoperíodo

**Cluster C15 (83 consultas)**, empatado com C10 como maior cluster.

### Entradas
`V_real` · **altura da lâmina** (a profundidade importa e é o que lm/L
ignora) · exigência das plantas (baixa · média · alta) · com ou sem CO2 ·
tipo de luminária.

### Fórmulas — três fontes que discordam do mesmo rótulo
```
lm_total = V_real × (lm/L do nível escolhido)

                peixeseaquarismo   aquarioturbinado   aquariosplantados
baixa                20 lm/L          10 – 20 lm/L         15 lm/L
média              30 – 40 lm/L       20 – 40 lm/L         30 lm/L
alta                 60 lm/L            > 40 lm/L          60 lm/L
                                              [iluminacao-lumen-por-litro]

faixa consolidada com atribuição: baixa 10–20 · média 20–40 · alta 40–60+

fotoperíodo: low tech 6–8 h · high tech 8–10 h · contra alga 5–6 h ·
             ciclagem 4–6 h                              [fotoperiodo]
temperatura de cor: 6500 – 8000 K                        [temperatura-de-cor]
CO2: 15–35 mg/L útil, tóxico acima de 30–35 mg/L         [co2-concentracao]
```

### Duas honestidades na tela
1. As três fontes discordam **por 2x sobre o mesmo rótulo "baixa"**. A
   resposta mostra as três, não a média.
2. Os limites de CO2 se **sobrepõem** (35 mg/L é ao mesmo tempo "faixa útil"
   e "acima de 30–35 é tóxico"). A página mostra a sobreposição e manda ler o
   drop checker (azul baixo · verde na faixa · amarelo excesso), que é medição,
   não conta.

### PPFD fica pendente, e a página diz por quê
lm/L ignora profundidade e espectro; PAR/PPFD é a medida correta e **nenhuma
fonte brasileira publica PPFD por litragem** (`ppfd-por-litragem`,
`pendente`). Coleta prevista: PPFD declarado pelos fabricantes de luminária
vendidos no Brasil. Enquanto não houver, a resposta usa lm/L e declara a
limitação — dizer o que a própria conta não enxerga é o que separa a
Aquametria dos blogs que copiam a tabela.

### Saídas
Lúmens totais e lm/L por nível, atribuídos · fotoperíodo por regime · faixa
de Kelvin · aviso de CO2 obrigatório quando o nível é alto · aviso de que
profundidade acima de ~45 cm derruba a luz que chega ao substrato e lm/L não
capta isso.

### Produtos sugeridos
Entidade `iluminacao`. Campos do Bloco 3: `marca`, `modelo`, `potencia_w`,
`fluxo_lm`, `temperatura_cor_k`, `comprimento_cm`, `ppfd_declarado`,
`volume_atendido_declarado_L`, `preco`, `fonte`, `verificado_em`. Critério:
`fluxo_lm` dentro da faixa **e** `comprimento_cm` compatível com o aquário —
luminária que não cobre o comprimento cria sombra, e nenhum varejo avisa.
A resposta puxa C7 para mostrar o custo mensal do fotoperíodo escolhido.

### Constantes usadas
`iluminacao-lumen-por-litro`, `fotoperiodo`, `temperatura-de-cor`,
`co2-concentracao`. Recusada: `ppfd-por-litragem`.

---

## 11. Fora do lote inicial — e o que libera cada uma

| Cluster | Decisão | Critério de entrada |
|---|---|---|
| **C10** compatibilidade (83 consultas) | **Não é calculadora**: é banco de fichas de espécie + interseção de faixas. Melhor cauda longa do nicho e candidato natural ao widget de loja. | Bloco 3 (modelo do banco) e Bloco 4. |
| **C13** dosagem (32 consultas) | **Retida. Risco letal.** Só 2 dosagens verificadas no fabricante (Mbreda Micronutri, Veromar KH); 3 transcritas em varejo; 7 pendentes, incluindo sal grosso com 3 valores em 5 fontes. Somado ao volume superestimado da C1 (erra para **overdose**), a conta é insegura. | Só abre com: (a) ≥ 6 rótulos verificados na embalagem ou no fabricante, (b) **marca e concentração como entrada obrigatória** — nunca dose genérica, (c) o desconto de substrato resolvido na C1. |
| **C14** TPA (6 consultas) | Absorvida pela C12 como painel de manutenção. Sozinha é uma regra de três e não sustenta página. | — |
| **C4** circulação e sump (13) | Depois da C3, no mesmo motor de vazão. Nicho marinho, público pequeno e mais exigente. | C3 publicada + constantes de circulação marinha com fonte. |
| **C6** resfriamento (9) | Depende do modelo térmico bloqueado na C5 (`u-vidro-aquario`). | Via B da C5 desbloqueada. |
| **C9** cardume mínimo (7) | Campo da ficha de espécie, exibido dentro da C8. | Banco de fichas. |
| **C11** ciclagem (30) | Cronograma e diagnóstico, não cálculo: vira artigo-âncora com checklist datado. | Bloco 4. |

---

## 12. Coletas que este bloco abriu (entram nos blocos 3 a 5)

Ordenadas pelo que mais desbloqueia:

1. **`u-vidro-aquario`** — libera o cálculo físico do aquecedor (C5 via B) e a
   C6. É a entrega que não tem paralelo no Brasil.
2. **`substrato-porosidade`** (medição própria, protocolo na seção C1) — libera
   o volume real correto na C1 e é pré-requisito da C13.
3. **`seachem-matrix-dosagem`** — reconfirmar na embalagem/fabricante e
   resolver o conflito interno de 2x. A página do fabricante está bloqueada
   pelo egresso da nuvem; conferir por foto de rótulo do varejo brasileiro.
4. **Espessura de vidro** — tensão admissível + coeficiente de segurança
   citáveis, para liberar a segunda pergunta do cluster C2.
5. **`temperatura-minima-por-cidade`** — Normais Climatológicas do INMET
   (1991–2020), mínima média do mês mais frio. Vira página programática **com
   dado suficiente para ser útil sozinha**: cada cidade ganha ΔT, faixa de
   potência e custo mensal.
6. **`tarifa-energia-kwh`** — tarifas ANEEL por distribuidora, para valor
   inicial por estado na C7.
7. **`ppfd-por-litragem`** — PPFD declarado pelos fabricantes de luminária
   vendidos no Brasil.
8. **Fichas de espécie** — as 8 iniciais precisam de tamanho adulto, GH,
   cardume mínimo, agressividade e zona de nado; só então a C8 sai da faixa
   mínima.

## 13. Bloqueios de publicação (desembarque)

Nenhuma calculadora vai ao ar sem aprovação do Raphael; `publicar: false` em
todas. Além disso, cada uma tem uma travessa técnica própria:

- **C2** não publica espessura de vidro nem veredito de "a laje aguenta".
- **C5** não publica a via física até `u-vidro-aquario` ter fonte.
- **C8** não aceita espécie sem ficha com fonte e data.
- **C12** publica a âncora Seachem marcada como "a conferir na embalagem".
- **C13** não existe.
- Nenhuma calculadora publica número cuja constante esteja `pendente`.

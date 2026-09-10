---
titulo: Especificação das ferramentas — Robometria
bloco: 2
gerado_em: 2026-09-09
publicar: false
---

# Especificação das ferramentas — Robometria

Bloco 2 da fila. Define **o que cada ferramenta responde, com que entrada, com que
saída, com que fonte e o que ela se recusa a responder**. Nenhuma linha de PHP nasce
antes deste arquivo; nenhum número entra aqui sem fonte e data.

Duas ferramentas âncora, uma por eixo do corpus (`dados/corpus-buscas.md`), e elas
**não se fundem**: compatibilidade é catálogo, dimensionamento é cálculo.

| Código | Ferramenta | Eixo | Sub_id 2 |
|---|---|---|---|
| **R1** | Localizador de peça compatível por modelo | compatibilidade | `R1` |
| **R2** | Dimensionador de sucção e autonomia por área, piso e pelo | dimensionamento | `R2` |

Sub_id 1 é sempre `robometria` (seção 7 do `ARQUIPELAGO.md`).

---

## 0. Como esta coleta foi feita, e o que isso limita

O egresso HTTP direto está fechado nesta nuvem: `multilaser.com.br` e `manuals.plus`
devolveram **EGRESS_BLOCKED** em 09/09/2026, como já havia acontecido com as fontes da
Aquametria. Toda a coleta abaixo saiu de **busca web, restrita ao domínio da fonte**
quando a atribuição precisava ser exata.

Consequência que fica escrita, e não escondida: **a leitura direta das páginas de peça
e dos manuais em PDF continua sendo uma coleta em aberto.** A Aquametria já registrou
um caso de busca restrita devolver número errado com atribuição certa — por isso todo
dado deste bloco entra em `constantes.json` com o canal de coleta declarado, e a
reconfirmação na fonte primária é trabalho do Bloco 3, não um capricho.

---

## 1. FERRAMENTA R1 — Localizador de peça compatível por modelo

### 1.1 A pergunta e o alvo de busca

**Consulta principal:** `filtro compatível robô aspirador <marca> <modelo>` e as irmãs
`escova lateral <modelo>`, `mop <modelo>`, `bateria <modelo>` (clusters A1–A4 do corpus).

**Classificação da SERP, feita em 09/09/2026 na consulta real
"qual filtro serve no robô aspirador Positivo PRA500 compatível"** — exigência da
seção 14.9 do `ARQUIPELAGO.md`:

| Quem ocupa | O que entrega |
|---|---|
| Mercado Livre (anúncio) | título de anúncio: "kit 3 filtros HEPA, exclusivo PRA500". Sem fonte, sem data, e quem afirma a compatibilidade é o vendedor |
| Loja oficial Positivo / positivocasainteligente | página **do robô**, não da peça |
| TechTudo (lista de 5 modelos) | guia de compra, não responde a pergunta |
| aspiradortop, gamerpoint, pegmix, buscapé | review e comparação de preço |

**Veredito: é ALVO.** Ninguém na primeira página responde "qual peça serve neste
modelo" com fonte do fabricante e data — a resposta que está no ar é copy de anúncio.
Não há fazenda de conteúdo com domínio forte estacionada nesta consulta, porque a
consulta é chata de escrever e não vende display. É exatamente o buraco que a Bússola
aprovou na rodada 003.

**Por que a R1 chega às 10 primeiras:** a página serve, em HTML, a tabela peça × modelo
com o código do fabricante, o endereço da declaração e a data da verificação — três
coisas que nenhum dos concorrentes acima tem. Intenção de compra: alta e imediata
(quem busca peça já tem o robô e já quebrou algo).

### 1.2 Entradas

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| `marca` | seleção | sim | lista fechada, vinda do banco do Bloco 3 |
| `modelo` | seleção dependente | sim | códigos do fabricante (HO041, PRA500, S20…), nunca texto livre |
| `tipo_de_peca` | seleção | não | filtro · escova lateral · escova principal · mop · bateria. Vazio = mostra todas |

**O seletor de tipo só oferece o que o banco consegue responder** — decisão da terceira
leva do Bloco 3c, obrigada pela varredura da entrada (`dados/cobertura-r1.json`). Medido:
`reservatório` está no vocabulário do esquema e tem **zero** peças no banco inteiro, então
oferecê-lo é oferecer uma escolha que sempre devolve recusa. Isso contraria a promessa
antes do formulário (seção 6 do `ARQUIPELAGO.md`) e ensina o visitante que a ferramenta
não sabe responder. O tipo volta ao seletor no dia em que a primeira peça dele entrar no
banco — a regra é do banco, não da lista escrita aqui: **o seletor é gerado da varredura,
nunca digitado à mão.**

`bateria` fica, e com ressalva medida: ela responde em **1** modelo só (o HO041). Fica
porque é o único tipo em que a variante de hardware muda a peça — é lá que a R1 dá a
resposta que nenhum anúncio dá — e porque a recusa dela é informativa, não vazia.

**Texto livre é proibido na entrada de modelo.** O corpus (cluster A2) já mostrou o
sintoma: anúncio "escova lateral V3 V5 A4 A6" sem marca no título. Campo livre faria a
ferramenta adivinhar de qual fabricante é o "V3" — e adivinhar compatibilidade é
exatamente o defeito que esta ilha existe para não cometer.

### 1.3 Saída — e os três níveis de certeza

A R1 **nunca infere compatibilidade**. Cada par peça × modelo sai com um dos três
selos abaixo, e o selo aparece na frase, não numa legenda de rodapé:

1. **`declarada_fabricante`** — o fabricante declara, na própria página da peça ou no
   manual. Só este nível pode ser escrito como *"serve"*. Frase padrão:
   > "A Multilaser declara a escova lateral **PR10124** compatível com HO041, HO400,
   > HO401, HO407 e OB010 (página oficial de peça, verificada em 09/09/2026)."
2. **`declarada_terceiro`** — quem afirma é lojista ou marketplace. Aparece em seção
   **separada, abaixo, rotulada** — nunca misturada, nunca em primeiro lugar (seção 7 do
   `ARQUIPELAGO.md`). Frase padrão: *"o anunciante declara… — não localizamos declaração
   do fabricante"*.
3. **`nao_declarada`** — a ferramenta diz que não encontrou e **para ali**. Silêncio
   parece defeito (seção 7), então o texto é explícito: *"não localizamos declaração do
   fabricante para esta peça neste modelo; não vamos supor."*

### 1.4 REGRA DE DIVERGÊNCIA DA R1 — vale o conjunto MAIS ESTREITO

Achado desta coleta, e é o caso que fixa a regra:

- `multilaser.com.br` (varejo) intitula o filtro **PR10205** como *"Filtro para Aspirador
  Robô Mars, Moon e Duster"*, associado ao **HO041**.
- `multilaserempresas.com.br` intitula **o mesmo código PR10205** como
  *"Filtro para Aspirador Robô (HO041 e OB010)"*.
- E existe um **PR10343**, *"Filtro para Aspirador Robô OB010"*, código próprio para o
  OB010.

Dois canais do mesmo fabricante, um código de peça, conjuntos de compatibilidade
diferentes — e um terceiro código que sugere que o OB010 tem filtro próprio.

**Regra: em compatibilidade, divergência resolve pelo conjunto MAIS ESTREITO, e as duas
declarações são publicadas.** Isto é o **oposto** da regra do banco de espécies da
Aquametria, que resolve pelo maior, e a inversão é deliberada: lá o erro para o lado
largo dá ao peixe mais espaço do que precisa; aqui o erro para o lado largo faz alguém
comprar uma peça que não encaixa. **A assimetria de custo decide a direção do
arredondamento, não o gosto de quem grava.**

Aplicado ao caso: o PR10205 sai como compatível com **HO041**; a declaração
"HO041 e OB010" aparece como divergência registrada; para o OB010 a ferramenta aponta o
**PR10343**. E a página diz que os dois canais do fabricante discordam, com as duas
datas.

### 1.5 Armadilha registrada: peça de aspirador que não é robô

O filtro **PR550** é do *aspirador de pó 2 em 1 HO03/HO04* — **não é robô aspirador**.
O corpus do Bloco 1 trouxe "HO03/HO04" na lista de modelos, e eles não entram no banco
de modelos de robô. Idem para o PR684 (HO011/HO012), que precisa de verificação de
categoria antes de qualquer coisa. **Modelo entra no banco só depois de confirmado que
é robô**, e o campo `categoria` do Bloco 3 existe para isso.

### 1.6 Correção que este bloco faz no corpus do Bloco 1

O corpus registrou `PRA8000`. A coleta de hoje não encontra PRA8000 em canal nenhum: a
linha da Positivo Casa Inteligente que aparece é **PRA500, PRA800, PRA1000 e PRA2000**.
Trata-se, com alta probabilidade, de erro de transcrição de **PRA800**. O Bloco 3 grava
`PRA800` e **não** grava PRA8000; se a fonte primária mostrar que os dois existem, o
banco recebe os dois. Nenhum dado técnico foi herdado do nome errado.

### 1.7 Tabela de exemplos pré-renderizada (obrigatória, seção 5)

Servida em HTML, sem depender de JavaScript, cobrindo as marcas de maior recorrência no
corpus. Mínimo de 8 linhas na primeira publicação.

**A tabela é GERADA, não digitada** — decisão da terceira leva do Bloco 3c. O arquivo
`dados/tabela-exemplos-r1.md` sai de `ferramentas/cobertura-r1.py --gravar` e hoje tem
**45 linhas**, todas com o código, o selo e a data que o banco tem. Tabela digitada à mão
discorda do banco em silêncio no dia em que o banco muda, e é exatamente esse silêncio que
a seção 5 do `ARQUIPELAGO.md` existe para impedir. A ordem alterna marcas de propósito: em
ordem alfabética as nove primeiras linhas seriam todas Electrolux, e a promessa desta ilha
é comparação **cross-marca**. O Bloco 4 serve essas linhas em HTML; o formato é:

| Modelo | Peça | Código do fabricante | Selo | Fonte / data |
|---|---|---|---|---|
| Multilaser HO041 | escova lateral | PR10124 | declarada_fabricante | página oficial de peça · 09/09/2026 |
| Multilaser HO400 | escova lateral | PR10124 | declarada_fabricante | página oficial de peça · 09/09/2026 |
| Multilaser HO041 | filtro | PR10205 | declarada_fabricante (divergência registrada) | dois canais do fabricante · 09/09/2026 |
| Multilaser OB010 | filtro | PR10343 | declarada_fabricante | página oficial de peça · 09/09/2026 |

A tabela é o corpo da página para um modelo de linguagem: sem ela, a R1 é um formulário
vazio (seção 5 do `ARQUIPELAGO.md`).

### 1.8 Vitrine dentro do resultado (bloco 4e)

O cartão diz **a especificação que fez o produto entrar**: *"filtro HEPA — o fabricante
declara compatível com o seu HO041"*. Produto sem imagem **não some**: entra com espaço
reservado neutro. Item sem link de afiliado entra no banco com `afiliado.url` presente e
vazio, e a contagem de itens esperando link é reportada em todo bloco (seção 7).

### 1.9 JSON-LD

`WebApplication` na ferramenta · `FAQPage` nas perguntas de compatibilidade mais
recorrentes do corpus · `Organization` com `sameAs` na marca. Ficha de peça só ganha
`Product` quando existir ficha — e, pela seção 14.2, **ficha de produto nasce por
último**, só quando houver dúvida paramétrica que o fabricante e a loja não respondem.

---

## 2. FERRAMENTA R2 — Dimensionador de sucção e autonomia

### 2.1 A pergunta e o alvo de busca

**Consultas principais:** `quantos Pa preciso robô aspirador pelo de cachorro` (B1),
`robô aspirador para quantos m2` (B2), `robô aspirador para 80 m2` (B2/B3).

**Classificação da SERP, feita em 09/09/2026 na consulta
"quantos Pa robô aspirador carpete pelo de cachorro"** — seção 14.9:

| Quem ocupa | O que entrega |
|---|---|
| Canaltech, Mundo Conectado, O Povo, O Cafezinho | explicação do que é Pa + faixa genérica. Domínios fortes |
| TechTudo, Exame | lista de compra "melhores para pet" |
| melhoraspiradordepo, ladotech, Tecnoblog Comunidade | fazenda/comparativo e fórum |

**Veredito: alvo PARCIAL, e a página nasce mirando a cauda, não a cabeça.** A consulta
curta "o que é Pa" está tomada por veículo grande e a Robometria **não** disputa essa —
seria gastar rastreamento de domínio novo para estacionar na página 4. A consulta que
nasce agora é a **paramétrica com a casa da pessoa dentro**: "quantos Pa para 80 m² com
carpete e cachorro", "quanto tempo um robô de 162 m² por carga leva em 200 m²". Nenhum
dos veículos acima devolve número para a casa de quem pergunta — todos devolvem faixa
genérica. **É por aí que se ganha, e só por aí.**

### 2.2 O que a R2 calcula de próprio — e é a razão de ela existir

O Bloco 1 já tinha achado o vácuo: **nenhuma fonte publica a conta que liga bateria →
autonomia → área.** Todo m² que circula é número fechado do fabricante. Confirmado hoje,
com um caso limpo: a Xiaomi declara, na página oficial de especificações do S20,
**3.200 mAh, até 120 min e recarga de 220 min — e não declara cobertura em m² nenhuma.**

A R2 **não inventa** o coeficiente que falta. Ela publica o número que ninguém publica e
que sai de dado declarado:

> **CICLOS** = teto( área_informada ÷ cobertura_declarada_por_carga )
>
> **TEMPO REAL ATÉ TERMINAR** = ciclos × autonomia_declarada + (ciclos − 1) × recarga_declarada

Exemplo com dado de fabricante, ponta a ponta: um robô que a Electrolux declara cobrir
**até 162 m² com até 2 h de bateria** (ERB44, loja oficial), numa casa de 200 m², precisa
de **2 ciclos** — e, com uma recarga no meio, o serviço termina em muito mais tempo do
que as "2 horas" que o anúncio comunica. *Esse* é o número que a pessoa queria e que
ninguém dá: não a autonomia, mas **quando a casa fica limpa**.

**Três honestidades que ficam escritas na própria página:**

1. **`area_informada` é área livre de piso**, sem móveis. A ferramenta **não** aplica
   coeficiente de obstrução, porque coeficiente de obstrução seria dado inventado. Ela
   pede a área e diz qual suposição está fazendo.
2. **O cálculo de mais de um ciclo só vale se o modelo retomar de onde parou.** Modelo
   que não retoma após recarregar não termina a casa sozinho, e a conta perde sentido a
   partir do segundo ciclo. Por isso o Bloco 3 tem que gravar `retoma_apos_recarga` como
   campo de banco, declarado pelo fabricante — sem ele a R2 não publica resultado de
   múltiplos ciclos.
3. **Cobertura por carga só entra se o fabricante declarar.** Onde ele declara só
   minutos (Xiaomi S20, Positivo PRA800), a R2 escreve *"o fabricante não declara
   cobertura em m² para este modelo"* e mostra apenas a autonomia. **Não converte.**

### 2.3 A constante que NÃO existe ainda — e fica proibida

Seria cômodo derivar uma taxa de cobertura (m² por minuto) e aplicá-la a todo modelo.
Hoje o banco tem **um único par (minutos, m²) declarado por fabricante**: os 162 m² em
até 120 min da Electrolux, que dão 1,35 m²/min. **Um ponto não é um coeficiente.**

Por isso `taxa-cobertura-m2-por-min` entra em `constantes.json` com status **`pendente`**
e está **proibida dentro de qualquer fórmula publicada** (seção 10 do `ARQUIPELAGO.md`).
Ela só muda de status quando o banco tiver **pelo menos 5 pares (minutos, m²) declarados
pelo próprio fabricante**, e ainda assim publica **faixa com a dispersão à mostra**,
nunca a média — média esconde exatamente o desacordo que faz a página valer.

### 2.4 Entradas

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| `area_m2` | número, 10–400 | sim | área **livre de piso**, declarado no rótulo do campo |
| `tipo_de_piso` | liso · tapete fino · carpete | sim | vocabulário das próprias fontes |
| `pelo_de_pet` | não · curto · longo | sim | |
| `modelo_de_referencia` | seleção, opcional | não | quando preenchido, a saída inclui ciclos e tempo real daquele modelo |

### 2.5 Saída — faixa com critério e fonte, nunca número seco

O `PROMPT.md` desta ilha exige faixa com critério e fonte. A coleta de hoje mostra **por
que**: as fontes brasileiras não concordam entre si sobre o limiar de Pa.

| Situação | O que cada fonte recomenda | Fonte |
|---|---|---|
| piso liso, sujeira leve | até 1.500 Pa basta | Mundo Conectado |
| apartamento piso liso, pouca circulação | 2.000 Pa | Mundo Conectado |
| apartamento pequeno sem animais, dia a dia | 3.000 Pa | Mundo Conectado |
| casa com pet | **acima de 4.000 Pa** = alta sucção, ideal para pelo e carpete | Canaltech |
| casa com pet | consenso acima de 3.000 Pa; faixa confortável 4.000–6.000 Pa | Mundo Conectado |
| piso liso com tapete pontual | acima de 6.000 Pa entrega resultado próximo do limite prático percebido | Mundo Conectado |

**A R2 mostra o desacordo, exatamente como a Aquametria faz na C3 e na C5.** Ela não
escolhe um número e o apresenta como verdade: devolve o **maior limiar citado para a
situação da pessoa** como recomendação segura, e ao lado o **menor limiar citado**,
dizendo quem recomenda cada um. Quem tem cachorro e carpete não deveria descobrir
depois da compra que a "faixa recomendada" que leu tinha um autor e um critério.

**Aviso de tipo de fonte, na frase:** os limiares de Pa **não são especificação de
fabricante** — são recomendação editorial de veículo brasileiro. A página diz isso com
essas palavras. Fabricante declara o Pa do aparelho; **quanto Pa a sua casa precisa é
opinião publicada, e opinião publicada tem autor.** Confundir os dois seria vender
editorial como dado técnico, que é o que as fazendas fazem.

### 2.6 Elegibilidade do bloco de produto na R2 (seção 7)

Um modelo entra na lista de recomendados só se passar em **TODAS** as condições que a
ferramenta conhece:

1. `pa_declarado` ≥ maior limiar citado para a situação informada;
2. se `area_m2` > cobertura declarada por carga → `retoma_apos_recarga` = verdadeiro;
3. voltagem compatível com a informada, quando o campo existir no banco.

Quem passa na (1) e falha na (2) vai para seção **separada, abaixo, rotulada**:
*"atende à sucção, mas não retoma após recarregar — na sua metragem, não termina
sozinho"*. **Nunca misturado, nunca em primeiro lugar** — recomendar em primeiro lugar
um produto que a própria página diz não servir é defeito grave, e foi a cicatriz que a
Aquametria pagou em 09/09/2026.

Ordem da lista: (1) elegibilidade técnica completa; (2) adequação técnica entre os
elegíveis; (3) **só como desempate** entre equivalentes, quem tem link de loja aparece
antes. Sem item elegível, o bloco não lista — **e diz por quê**.

### 2.7 Tabela de exemplos pré-renderizada

Casos já resolvidos, servidos em HTML, cobrindo a faixa real de uso — pelo menos as
metragens de 40, 60, 80, 120 e 200 m², cruzadas com piso liso / carpete e com / sem pet.
Cada linha traz o limiar de Pa recomendado **com o nome de quem recomenda**, e, quando
houver modelo de referência com cobertura declarada, os ciclos e o tempo real.

### 2.8 Resposta antes da explicação

Primeira dobra, frase autossuficiente que sobrevive a ser citada fora de contexto:

> "Para 80 m² de piso liso com um cachorro que solta pelo, as fontes brasileiras
> divergem: a Canaltech recomenda acima de 4.000 Pa e o Mundo Conectado trata 3.000 Pa
> como o consenso mínimo, com faixa confortável entre 4.000 e 6.000 Pa (verificado em
> 09/09/2026). Um robô que o fabricante declara cobrir 162 m² por carga faz essa casa em
> um ciclo só."

### 2.9 JSON-LD

`WebApplication` na ferramenta · `FAQPage` nas perguntas de Pa e metragem · `Dataset`
quando o banco de modelos virar página · `Organization` com `sameAs`.

---

## 3. O que vale para as duas

- **JS e CSS nunca dentro do retorno do shortcode** — vão no `wp_footer`. Foi o defeito
  que derrubou cinco calculadoras da Aquametria em 08/09/2026 (seção 8).
- **Menu hambúrguer, favicon próprio e vitrine** entram na casca (Bloco 3b), não como
  acabamento.
- **Interlinkagem obrigatória:** a R1 aponta para a R2 e vice-versa. O corpus (cluster
  B4) mostrou que as duas intenções convivem na cabeça de quem compra — o conselho
  recorrente em fórum é *"cheque a peça de reposição antes de comprar"*. O link entre as
  duas ferramentas é a materialização desse conselho, e é o que impede que a ilha tenha
  página órfã já no nascimento.
- **Nenhuma página de malha antes do Search Console verificado** (seção 11, passo 9).
  Ferramenta e artigo podem sair; leva de malha, não.
- **Todo número na tela em IBM Plex Mono com `tabular-nums`**; texto corrido nunca em
  Mono; o vermelho `#CC3311` é cor de sinal, um uso por tela.

---

## 4. O que este bloco NÃO fecha — e vira lista de compras do Bloco 3

Campos que o modelo do banco tem que ter, e que saíram desta especificação:

**MODELO DE ROBÔ:** `categoria` (robô | aspirador comum — para barrar HO03/HO04),
`pa_declarado`, `autonomia_min_declarada`, `cobertura_m2_declarada` (nulo quando o
fabricante não declara — e nulo é resposta, não lacuna), `recarga_min_declarada`,
**`retoma_apos_recarga`**, `bateria_mah`, `voltagem`, `base_autoesvaziamento`,
`fonte`, `verificado_em`, `imagem{url,largura,altura,fonte,coletado_em,alt}`,
`afiliado{url,coletado_em}`.

**PEÇA:** `codigo_fabricante`, `tipo`, `modelos_compatíveis[]`, **`selo_de_compatibilidade`**
(declarada_fabricante | declarada_terceiro | nao_declarada), `divergencias[]` (canal,
conjunto declarado, data), `vida_util_declarada`, `fonte`, `verificado_em`, `imagem`,
`afiliado`.

Pendências honestas, que não se resolvem inventando:

1. **Nenhum par (minutos, m²) além do ERB44** foi confirmado. Faltam pelo menos quatro
   para a taxa de cobertura sair de `pendente`.
2. **A faixa "5.000–10.000 Pa para carpete"** apareceu na busca **sem atribuição
   exata a um veículo**. Está em `constantes.json` como `atribuicao_incerta` e
   `nao_publicavel` — precisa de busca restrita ao domínio antes de ir para a tela.
3. **Vida útil de peça diverge**: o manual da Electrolux declara **6 meses** para o
   filtro HEPA; veículos editoriais dizem 3 meses e 2–3 meses. Fabricante e editorial
   não são a mesma classe de fonte, e o banco grava a classe junto com o número.
4. **A leitura direta das páginas de peça e dos manuais em PDF continua bloqueada.**

**Próximo passo desbloqueado: Bloco 3 — modelo do banco** (`dados/esquema-banco.json` +
os primeiros registros de MODELO DE ROBÔ, PEÇA e MARCA), com os campos acima, o
`selo_de_compatibilidade` como campo de primeira classe e o campo `imagem` desde já —
a Aquametria descobriu tarde que o banco não tinha e travou a vitrine. Continua sem
depender de WordPress nem de domínio.

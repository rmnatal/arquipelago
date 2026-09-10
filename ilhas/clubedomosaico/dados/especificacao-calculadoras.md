# Especificação das duas ferramentas — Clube do Mosaico

Bloco 2 da fila. Escrito em 10/09/2026 a partir de `dados/constantes.json` (coletado nesta
mesma execução, direto do domínio de cada fabricante) e de `dados/corpus-buscas.md` (bloco 1).

Este arquivo é o contrato de construção das ferramentas: o bloco 4 escreve os snippets a
partir daqui e não precisa decidir nada de novo. **Nenhuma constante técnica é inventada
aqui** — toda regra abaixo aponta para um item de `constantes.json`, que por sua vez aponta
para a página ou ficha do fabricante, com data de coleta.

**Ordem de construção: F2 primeiro, F1 depois.** O bloco 1 mediu por quê: a pessoa que
busca cola está com o vaso na mão e a cola errada no carrinho (maior intenção de compra), a
SERP dessa consulta está aberta e poluída por blog traduzido, e a resposta certa é
declarada por fabricante — enquanto a de rejunte exige inventar menos, mas vende menos.

---

## 0. O que as duas ferramentas têm em comum (vale para as duas, não se repete depois)

- **Resposta antes da explicação** (seções 5 e 14.5 do contrato): o número e o critério nos
  dois primeiros parágrafos, em frase autossuficiente que sobrevive a ser citada fora de
  contexto, com fabricante e data dentro da própria frase.
- **Tabela de exemplos pré-renderizada no HTML servido**, cobrindo a faixa real de uso. É o
  que faz a página existir para modelo de linguagem, que nunca vê o resultado do JavaScript.
- **JSON-LD**: `WebApplication` na ferramenta, `FAQPage` no bloco de perguntas, `Dataset` na
  tabela de exemplos quando ela for a resposta principal (é o caso da F1).
- **JS e CSS no `wp_footer`, nunca dentro do retorno do shortcode** (seção 8 — foi o defeito
  que derrubou cinco calculadoras da Aquametria).
- **Toda função de nível superior dentro de `if ( ! function_exists( ... ) )`**, snippet
  começando com `/**`, sem `$_SERVER` literal (usar `add_query_arg( array() )`).
- **Bloco de compra com link de afiliado ANTES da prova de procedência** (seção 7, cicatriz
  da Robometria de 10/09/2026). Detalhe no item 3 abaixo — é obrigatório nas duas, e nenhuma
  das duas vai ao ar sem ele, mesmo com `afiliado.url` ainda vazio.
- **Interface**: promessa em uma linha antes do formulário; no celular, barra fixa no rodapé
  enquanto o resultado está fora da tela e rolagem automática até o resultado; miolo branco,
  coral `#FC483B` só no botão e no número-resposta; alerta técnico em âmbar `#B9791A`, nunca
  em vermelho. Sem gradiente, sem sombra colorida, separação por linha de 1px.
- **Unidade em JetBrains Mono com `tabular-nums`**; texto corrido nunca em Mono.
- **Rastreamento de afiliado**: Shopee `Sub_id 1 = clubedomosaico`, `Sub_id 2 = F1` ou `F2`;
  Mercado Livre etiqueta `clubedomosaico-F1` / `clubedomosaico-F2`.

---

## 1. F2 — Seletor de cola e rejunte  *(constrói primeiro)*

### 1.1 O que ela responde, e por que ela ganha
Consulta principal: **"qual cola usar para mosaico em <base>"**, e as variantes medidas no
bloco 1: `cola para mosaico` (10–100/mês), `cola para mosaico em MDF`, `cola para mosaico em
vidro`, `qual cola usar em vaso de cerâmica área externa`.

Por que ela chega às dez primeiras (exigência da seção 14.9): a SERP de hoje é Vila do
Artesão, FazFácil e dois domínios traduzidos do russo, e **nenhum deles cita fabricante,
código de produto, data ou separa interno de externo e de molhado**. A F2 responde a mesma
pergunta com a restrição declarada pelo próprio fabricante do adesivo, com URL e data — e
é a única página em português que diz **o que não usar, e por quê**.

URL: `/qual-cola-para-mosaico/` · Código de rastreamento: `F2`

### 1.2 Entradas
| campo | valores | obrigatório |
|---|---|---|
| Base da peça | cerâmica esmaltada ou porcelana · vidro · espelho · MDF ou madeira · cimento ou concreto · alvenaria ou tijolo · metal · plástico | sim |
| Material da tessela | pastilha de vidro · pastilha cerâmica · caco de azulejo · caco de louça · caco de espelho · pedra | sim |
| Ambiente | interno seco · interno molhado (banheiro, cozinha) · externo abrigado · externo exposto a sol e chuva · contato permanente com água | sim |
| Largura de junta pretendida | 1 a 10 mm | não (padrão 2 mm) |

### 1.3 A regra de decisão — elegibilidade mecânica, não opinião
A F2 aplica a **regra de elegibilidade da seção 7 do contrato** de forma literal: o produto
só entra na lista de recomendados se passar em **TODAS** as condições declaradas pelo
fabricante que a ferramenta conhece. Basta **uma** restrição declarada bater com a entrada
para o produto sair dos recomendados e ir para a seção rotulada **"o que não usar neste
caso, e por quê"**, com a frase do fabricante e a data.

Isso é possível porque a ficha do Silicone Acético Construção Tekbond (BRSA004, revisada em
10/2025) publica a lista de restrições — ver `tekbond-silicone-acetico-restricoes` em
`constantes.json`. **Espelho, concreto, cimento, tijolo, calcário, superfície alcalina,
superfície pintada ou porosa, acrílico, aquário, metal corrosível e imersão contínua
eliminam o silicone acético por declaração do próprio fabricante.**

Matriz publicada (cada linha vira uma linha da tabela pré-renderizada):

| base | ambiente | recomendado | por que, na frase | eliminado, e por quê |
|---|---|---|---|---|
| cerâmica / porcelana | interno seco ou molhado | silicone acético | o fabricante indica cerâmica e azulejo; cura ≥3 mm em 24 h a 23 °C | PVA: o fabricante não declara resistência a água |
| cerâmica / porcelana | externo abrigado | silicone acético | mesma indicação; faixa de trabalho −50 a 150 °C | — |
| cerâmica / porcelana | externo exposto | silicone **neutro** primeiro | é o que o fabricante declara resistente a chuva e a raios UV | acético fica em segundo: indicado para cerâmica, mas sem declaração de chuva/UV |
| vidro (não laminado) | interno, externo abrigado | silicone acético | indicado para vidro não laminado e alumínio | — |
| vidro laminado | qualquer | silicone neutro | acético **proibido** em vidro laminado pelo fabricante | acético (restrição declarada) |
| **espelho** | qualquer | silicone **neutro** | o mesmo fabricante lista espelhos entre o que o neutro veda | **acético: proibido em espelhos pela ficha BRSA004** |
| MDF / madeira | interno seco | PVA (Cascorez Extra) | o fabricante indica MDF, compensado e madeira de alta, média e baixa densidade | acético: superfície porosa é restrição declarada |
| MDF / madeira | molhado ou externo | **a ilha não recomenda** | o fabricante do PVA não declara uso externo nem resistência a água, e a ilha não transforma silêncio em recomendação | PVA (sem declaração) e acético (poroso) |
| cimento / concreto | qualquer | cimentcola AC-II (área grande) ou silicone neutro (colagem pontual) | AC-II é declarada para área interna e externa pela NBR 14.081; o neutro é declarado para concreto e alvenaria | **acético: concreto, cimento e superfície alcalina são restrição declarada** |
| alvenaria / tijolo | qualquer | cimentcola AC-II ou silicone neutro | mesma justificativa | **acético: tijolo e superfície alcalina, restrição declarada** |
| metal | interno | silicone neutro | declarado resistente a metais corrosíveis | **acético: metal corrosível, zinco e chapa galvanizada, restrição declarada** |
| plástico | qualquer | **faixa descoberta** — ver 1.6 | — | acético não recomendado em PE, PP e PC |
| qualquer | contato permanente com água | **faixa descoberta** — ver 1.6 | — | **acético: imersão contínua é restrição declarada**; em piscina, a cimentcola AC-II só recebe água 7 dias depois |

### 1.4 O que a F2 devolve
1. **A frase-resposta**, primeira coisa da página, com fabricante e data dentro dela.
   Modelo: *"Para pastilha de vidro sobre vaso de cimento em área externa, use silicone
   neutro ou cimentcola AC-II — e não silicone acético: a ficha técnica BRSA004 do Silicone
   Acético Construção Tekbond, revisada em 10/2025, lista concreto, cimento e superfícies
   alcalinas entre as superfícies em que o produto não deve ser usado (verificado em
   10/09/2026)."*
2. **O tempo de espera**, que a SERP nunca dá: silicone acético cura ≥3 mm em 24 h a 23 °C
   e 55% de umidade relativa — é quanto a peça descansa antes do rejunte.
3. **O rejunte compatível e o procedimento**: junta de 2 a 10 mm no rejunte cerâmicas
   Quartzolit; a mistura repousa 15 minutos antes de usar; **junta de até 3 mm é molhada
   com água limpa antes da aplicação** (e quase toda peça de mosaico artesanal cai nessa
   faixa); liberação para contato com área molhada em 24 h; em área externa, proteger de
   sol, vento e chuva por 24 h.
4. **O bloco de compra** (item 3 desta especificação), e só depois dele a procedência.
5. **A seção "o que não usar neste caso"**, com a restrição declarada e o link de fonte.

### 1.5 Tabela pré-renderizada
As 13 linhas da matriz de 1.3, servidas no HTML, cada uma com a frase de justificativa
completa. É essa tabela que um modelo de linguagem lê quando cita a página.

### 1.6 Faixas descobertas — declaradas, nunca preenchidas no chute
Dois casos ficam **sem recomendação publicada** nesta versão, e a página diz isso em vez de
inventar: **peça em contato permanente com água** (falta o boletim do rejunte epóxi
Quartzolit) e **base de plástico**. Silêncio parece defeito; texto honesto, não. As duas
faixas estão em `pendentes` no `constantes.json` com o documento exato que as fecha.

---

## 2. F1 — Calculadora de pastilhas e rejunte  *(constrói depois)*

### 2.1 O que ela responde, e por que ela ganha
Consulta principal: **"quantas pastilhas e quanto rejunte para <peça>"**, e as variantes
`rejunte para mosaico`, `quantos gramas de rejunte por peça`, `pastilhas para mosaico`.

Por que ela chega às dez primeiras: o bloco 1 mediu que **a SERP inteira de rejunte responde
a pergunta de obra** — 0,2 a 0,4 kg/m², "1 kg faz 3 m²", tudo calculado com azulejo grande.
Aplicando a fórmula do **próprio fabricante** ao tamanho real da pastilha de artesanato, o
consumo é **2,80 kg/m²** para pastilha de 1×1 cm com 4 mm de espessura e junta de 2 mm —
**sete a catorze vezes o número que a primeira página do Google publica**. A ferramenta não
disputa aquelas páginas: ela responde outra pergunta, e é a única que a responde.

URL: `/calculadora-pastilhas-rejunte/` · Código de rastreamento: `F1`

### 2.2 Entradas
| campo | valores |
|---|---|
| Forma da peça | cilindro/vaso reto · vaso cônico (cachepot) · placa retangular · disco/tampo redondo · esfera · moldura (com vão) |
| Medidas | conforme a forma, em cm |
| Tamanho da pastilha | 1×1 · 1,5×1,5 · 2×2 · 2,5×2,5 cm · tessela irregular (lado equivalente) |
| **Espessura da pastilha** | em mm, padrão sugerido 4 mm, **com o aviso "meça a sua"** |
| Junta | 1 a 10 mm, padrão 2 mm |
| Sobra para quebra e recorte | padrão 10%, ajustável |

**A espessura é entrada, não constante.** Nenhum fabricante de pastilha de artesanato
publica espessura padronizada, então a ilha não finge conhecê-la: o campo vem com um valor
sugerido e um aviso, e a tabela de exemplos declara em cada linha a espessura usada.

### 2.3 As contas
**Área**, por forma (geometria, cálculo próprio da ilha):

| forma | área da superfície a revestir |
|---|---|
| cilindro / vaso reto | `π × D × H` (lateral) |
| vaso cônico | `π × (D₁+D₂)/2 × √(((D₁−D₂)/2)² + H²)` |
| placa retangular | `L × A` |
| disco / tampo | `π × D² / 4` |
| esfera | `π × D²` |
| moldura | `L × A − l × a` |

**Pastilhas**: `pastilhas_por_m² = 1 / ((lado_mm + junta_mm)/1000)²`, multiplicado pela área
e pela sobra, **sempre arredondado para cima** (regra de divergência da ilha: faltar
material no meio da peça é pior que sobrar, porque lote novo muda de cor).

**Rejunte**, pela fórmula publicada pela própria Quartzolit:
`consumo_kg/m² = ((A + B) × E × L × CR) / (A × B)`, com A e B em mm (lados da pastilha), E a
espessura em mm, L a junta em mm e **CR = 1,75**, que é o coeficiente que o fabricante usa
no exemplo publicado dele — `(200+200) × 8 × 10 × 1,75 / (200×200) = 1,4 kg/m²`.

**Cola**: a coluna existe e vem **vazia com explicação** nesta versão. O fabricante do
silicone declara rendimento por cordão, não por área, e o consumo em kg/m² da cimentcola não
foi obtido — os dois estão em `pendentes` no `constantes.json`. Converter isso no palpite é
exatamente o que a seção 10 do contrato proíbe. A tela diz: *"gramas de cola: ainda não
publicamos este número porque o fabricante declara rendimento por cordão, não por área."*

**Conversão entre unidades de venda** (achado próprio do bloco 1, que não existe na SERP):
placa quadrada de lado L com N pastilhas tem passo `L/√N` — a placa 30×30 com 225 pastilhas
tem passo de 2,00 cm, ou seja, é pastilha nominal de 2 cm e **não** de 1×1 cm, que é o erro
que a artesã comete ao comparar preços. Com junta de 2 mm, 100 pastilhas de 1×1 cm cobrem
144 cm²; com junta de 3 mm, 100 pastilhas de 2×2 cm cobrem 529 cm². A conversão **grama ↔
peça** fica pendente por SKU: depende do peso unitário, que nenhum fabricante declara de
forma geral e que o banco MATERIAL do bloco 3 coleta item a item, com data.

### 2.4 Tabela pré-renderizada — 12 peças típicas
Calculada nesta execução com as fórmulas acima, sobra de 10%, CR 1,75. Vai no HTML servido.

| peça | área | pastilha · junta · espessura | pastilhas (com 10%) | rejunte |
|---|---|---|---|---|
| Vaso cilíndrico 15 cm Ø × 20 cm | 942 cm² | 1×1 cm · 2 mm · 4 mm | 720 | 264 g |
| Cachepot cônico 18/12 cm × 15 cm | 721 cm² | 1×1 cm · 2 mm · 4 mm | 551 | 202 g |
| Tampo redondo 60 cm Ø | 2.827 cm² | 2×2 cm · 3 mm · 4 mm | 588 | 594 g |
| Quadro / placa 30 × 40 cm | 1.200 cm² | 1×1 cm · 2 mm · 4 mm | 917 | 336 g |
| Moldura de espelho 40×60 (vão 30×50) | 900 cm² | 2×2 cm · 3 mm · 4 mm | 188 | 189 g |
| Esfera decorativa 20 cm Ø | 1.257 cm² | 1×1 cm · 2 mm · 4 mm | 960 | 352 g |
| Mandala disco 40 cm Ø | 1.257 cm² | 2,5×2,5 cm · 4 mm · 5 mm | 165 | 352 g |
| Filtro de barro 30 cm Ø × 40 cm | 3.770 cm² | 2×2 cm · 3 mm · 4 mm | 784 | 792 g |
| Placa de número de casa 20 × 30 cm | 600 cm² | 1×1 cm · 2 mm · 4 mm | 459 | 168 g |
| Bandeja 25 × 35 cm | 875 cm² | 1×1 cm · 2 mm · 4 mm | 669 | 245 g |
| Vaso grande 25 cm Ø × 35 cm | 2.749 cm² | 2,5×2,5 cm · 3 mm · 5 mm | 386 | 577 g |
| Pingente / colar 5 × 5 cm | 25 cm² | 1×1 cm · 1 mm · 4 mm | 23 | 3,5 g |

Referência de consumo, para a frase-resposta: **2,80 kg/m²** (1×1 cm, 4 mm, junta 2 mm) ·
**4,20** (1×1, junta 3 mm) · **1,40** (2×2, junta 2 mm) · **2,10** (2×2, junta 3 mm) ·
**2,10** (2,5×2,5, 5 mm, junta 3 mm). Contra **0,73 kg/m²** do azulejo de 10×10 cm e
**1,40 kg/m²** do piso de 20×20 cm com junta de 10 mm — que é o que a SERP publica.

### 2.5 A frase-resposta da F1
*"Um vaso cilíndrico de 15 cm de diâmetro por 20 cm de altura tem 942 cm² de superfície e
consome cerca de 720 pastilhas de 1×1 cm (já com 10% de sobra) e 264 g de rejunte, com junta
de 2 mm e pastilha de 4 mm de espessura. O consumo de 2,80 kg/m² sai da fórmula publicada
pela Quartzolit — `((A+B) × E × L × CR)/(A × B)` com CR 1,75 — aplicada ao tamanho real da
pastilha de artesanato, e não ao azulejo de obra (verificado em 10/09/2026)."*

---

## 3. O bloco de compra — obrigatório nas duas, e vem ANTES da procedência

Cicatriz da Robometria, 10/09/2026 (seção 7 do contrato): a ferramenta dela publicou 45
pares peça × modelo com a coluna de procedência apontando para a loja do fabricante e
**nenhum link de afiliado na página** — o único clique de compra levava para onde a ilha não
ganha nada. As duas ferramentas desta ilha nascem sem repetir isso:

1. **O bloco de compra vem antes da prova de procedência**, dentro da mesma resposta:
   carrossel `scroll-snap` em CSS puro, cartões que são `<a href>` de verdade, com foto,
   marca, **a especificação que fez o produto entrar** (é o "cerâmica e azulejo" da ficha,
   não adjetivo de marketing), faixa de preço com data da coleta e botão de loja.
   `rel="sponsored"` + `target="_blank" rel="noopener"`, aviso de comissão visível.
2. **O link de procedência é discreto**: texto "fonte", `rel="nofollow noopener"`, nunca um
   botão. Ele existe para ser conferido, não para ser clicado.
3. **Nenhuma das duas vai ao ar sem o bloco**, mesmo com `afiliado.url` vazio: a página
   reserva o lugar, mostra "link de loja em breve" e **a ilha reporta em todo bloco quantos
   itens estão esperando link**. Esse número é trabalho pendente de verdade.
4. **Ordem da lista**: (1) elegibilidade técnica completa pela matriz de 1.3; (2) adequação;
   (3) ter link de loja **só como desempate** entre equivalentes. Nunca comparar comissão.
5. Produto sem imagem **não some** do resultado: aparece com espaço reservado neutro.

Os itens do banco MATERIAL que essas vitrines consomem são o bloco 3. Nesta execução o
banco ainda não existe, então **a primeira ferramenta publicada não pode sair sem o bloco 3
ter enchido pelo menos as categorias cola, rejunte e pastilha** — é o portão de dado da
seção 9 (3 itens de banco reais por página) aplicado à ferramenta.

---

## 4. Verificação antes de marcar `publicar: true` (seção 8, aplicada a estas duas)
1. `php -l` de verdade em cada snippet; toda função dentro de `if ( ! function_exists() )`.
2. JS e CSS no `wp_footer`; **zero `&#038;` DENTRO dos blocos `<script>`** (extrair só os
   `<script>` e contar ali — contar na página inteira é teste errado).
3. Buscar a URL no ar: HTTP 200; corpo começa pelo texto e não por metadado YAML; a tabela
   pré-renderizada aparece no HTML servido; JSON-LD presente e válido.
4. **Conferir três linhas da tabela na mão**, com calculadora, contra as fórmulas de 2.3.
5. **Coerência da recomendação**: rodar a F2 em espelho, em cimento e em imersão e confirmar
   que o silicone acético aparece **na seção de eliminados**, com a frase do fabricante — e
   nunca em primeiro lugar. Recomendar em primeiro lugar o produto que a própria página diz
   não servir é defeito GRAVE.
6. Revisão aplicada no `/status` igual à do manifest, depois do Sync.

## 5. O que este bloco deixa desbloqueado
- **Bloco 3** (modelo do banco) pode ser escrito: as entradas de MATERIAL que as duas
  ferramentas exigem estão nomeadas aqui — categoria cola (com a lista de restrições por
  produto), rejunte (com faixa de junta), pastilha (com lado, espessura e unidade de venda).
- **Bloco 4** (as ferramentas) fica dependente de duas coisas, e só delas: o WordPress
  existir e o banco do bloco 3 ter os itens das três categorias.
- As seis pendências de `constantes.json` são trabalho de coleta, não bloqueio: duas delas
  (consumo da cimentcola e rendimento do silicone) seguram apenas a coluna de gramas de cola
  da F1, e a ferramenta publica sem ela dizendo por quê.

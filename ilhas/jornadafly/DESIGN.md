# DESIGN — JORNADA FLY

Dono dos tokens desta ilha (seção 22.6 do `ARQUIPELAGO.md`). A casca renderiza a partir daqui.
**Token novo não nasce em despacho:** cor, fonte ou medida que não estiver neste arquivo é defeito, não identidade.
Quando este arquivo e o `VOZ.md` discordarem, **manda o `VOZ.md`** (seção 22.2).

## Marca — trazida pelo Raphael em 14/09/2026

A identidade desta ilha **não foi desenhada pela fábrica**. O Raphael trouxe a marca pronta e ela é a versão oficial: monograma em "J" com traço ascendente azul, nas versões horizontal, vertical e ícone, em fundo claro e escuro.

**O que o dossiê propunha está descartado** — as duas barras horizontais com marcador vertical não são mais a marca desta ilha. Fica escrito para ninguém "restaurar" o desenho do dossiê achando que corrige um desvio.

**Assinatura:** `A CONTA ANTES DA VIAGEM.` — caixa alta, espaçada, com ponto final. É a promessa da ilha, e tem consequência operacional: ver a seção "O que esta assinatura obriga", abaixo.

**Linha secundária, só em peça institucional (rodapé, perfil):** `PLANEJAR HOJE, VIAJAR SEMPRE.` Nunca substitui a assinatura.

**Imperativo só em botão.** `Calcule sua viagem` é rótulo de botão da ferramenta. Nunca vira assinatura de marca — embaixo do logo a pessoa ainda está decidindo se fica.

### Arquivo do símbolo — RESOLVIDO

- `ilhas/jornadafly/logo.svg` — símbolo oficial, duas cores: rasgo `#378AD0`, haste `#0F2539`. viewBox `0 0 1570 1960`.
- `ilhas/jornadafly/logo-branco.svg` — mesma forma com a haste em `#FFFFFF`, para uso sobre `--tinta`. Usar SÓ em fundo escuro.
- Procedência: vetorização da arte do próprio Raphael (a placa de marca que ele enviou em 15/09/2026). Não é a curva original do autor da arte — é um traço fiel de um raster pequeno. Se algum dia aparecer o SVG/AI original, ele substitui estes dois arquivos e esta nota some.
- Ninguém redesenha este símbolo. Quem precisar de outro tamanho exporta a partir do SVG.
- Regra de uso: o símbolo nunca aparece dentro de um quadrado colorido de fundo. Fundo transparente ou sólido claro (`--papel` / `--superficie`); em fundo escuro, usar a versão branca.
- Favicon e avatar: exportar do SVG em 512 / 180 / 32 / 16 px, PNG com fundo transparente.

### Lockups — RESOLVIDO

- `lockup-horizontal.svg` — símbolo + JORNADA FLY em uma linha. É o logo do cabeçalho do site. viewBox `0 0 943.1 160`.
- `lockup-vertical.svg` — símbolo em cima, JORNADA FLY embaixo, assinatura `A CONTA ANTES DA VIAGEM.` no pé. Rodapé, redes sociais, qualquer peça quadrada. viewBox `0 0 695.7 454.6`.
- `lockup-horizontal-branco.svg` e `lockup-vertical-branco.svg` — mesmas formas com a tipografia e a haste do J em `#FFFFFF`, para uso sobre `--tinta`. O rasgo continua `#378AD0`.
- Tipografia já convertida em curvas (Montserrat SemiBold na marca, Light na assinatura). Nenhum lockup depende de webfont carregar — o cabeçalho nunca aparece com a fonte errada.
- A palavra JORNADA e a palavra FLY têm o MESMO peso e a MESMA cor. Ninguém pinta FLY de azul: o azul da marca é do rasgo do símbolo e de mais nada.
- Área de respiro mínima em volta de qualquer lockup: a altura do símbolo dividida por 4. Nada entra nessa faixa.
- Tamanho mínimo do lockup horizontal: 180 px de largura. Abaixo disso, usa-se só o símbolo (`logo.svg`).
- Ninguém redigita a marca com `<text>` e webfont, e ninguém remonta lockup novo. Precisou de outra proporção, exporta destes arquivos.

## Cor — amostrada da arte oficial, contraste calculado em 14/09/2026

| token | valor | onde | contraste |
|---|---|---|---|
| `--tinta` | `#0F2539` | texto corrido, H1–H3, fundo das faixas escuras | **15,36:1** sobre `--papel` |
| `--sinal` | `#378AD0` | a cor da marca: traço do monograma, "FLY", preenchimento, barra do resultado | **3,62:1** sobre `--papel` → **só preenchimento, ícone e texto ≥ 24 px. NUNCA texto corrido** · 4,25:1 sobre `--tinta` |
| `--sinal-texto` | `#1F6AAF` | o mesmo azul em versão de texto: link, rótulo, número em destaque | **5,52:1** sobre `--papel` |
| `--papel` | `#FDFDFD` | fundo da página | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do resultado | — |
| `--traco` | `#B0C0CD` | borda de 1 px e divisor (**1,83:1 sobre papel — decorativo, nunca carrega informação sozinho**); sobre `--tinta` vale como texto de apoio, com 8,38:1 | — |
| `--legenda` | `#5A6675` | operador, data da coleta do preço, moeda, nota de rodapé | ≥ 4,5:1 sobre `--papel` — **conferir antes do primeiro uso; se reprovar, escurecer até passar e corrigir aqui** |
| `--custo` | `#8A5A12` | **o número de dinheiro** e a etiqueta de preço coletado | **5,91:1** sobre branco |
| `--alerta` | `#9A2B1E` | ressalva de preço e temporada | **7,67:1** sobre branco |

**Portão:** `#378AD0` reprova em texto normal. Onde for texto, é `#1F6AAF`. Isso não é preferência, é o critério de contraste da seção 5, e a Sentinela confere na ronda.

**Sobre `--tinta`:** branco tem 15,62:1 e o cinza `--traco` tem 8,38:1 — os dois passam. O azul da marca tem 4,25:1: serve para título e elemento gráfico, não para texto pequeno.

## O que esta assinatura obriga

"A conta antes da viagem" é promessa medível. **Página de experiência sem preço com data de coleta e moeda original é defeito**, não falta de dado — vira item de despacho na ronda da Sentinela, porque a marca está dizendo uma coisa que a página não entrega.

## Tipografia

Três famílias, uma monoespaçada — o teto da seção **22.4** do `ARQUIPELAGO.md`. *(Dizia "seção 15", que é a da voz; o teto de fontes é da 22.4 — "no máximo duas famílias de texto + uma monoespaçada" —, e este mesmo arquivo já a cita certo no parágrafo de carregamento. Corrigido pelo Pente Fino em 21/09/2026.)*

- **Marca e títulos: Montserrat.** É a fonte da arte oficial, informada pelo Raphael em 14/09/2026 — não é escolha da fábrica, é o que está no logo.
  - `JORNADA` e `FLY`: **Montserrat 500/600** (Medium a SemiBold), caixa alta.
  - Assinatura `A CONTA ANTES DA VIAGEM.`: **Montserrat 300/400** (Light a Regular), caixa alta, com **entreletra generosa** (`letter-spacing` de 0,18 a 0,24 em), e o **ponto final faz parte da assinatura**.
  - H1–H3 das páginas: Montserrat 600.
- **Texto corrido: Source Sans 3 400/600.** Corpo 1,0625 rem, altura de linha 1,7, medida máxima 66 caracteres. Montserrat é geométrica e cansa em parágrafo longo — ela manda no topo da página, não no meio.
- **Dinheiro, dias, número de pessoas e data de coleta: JetBrains Mono 500 com `tabular-nums`.** Texto corrido nunca vai em mono.

**Carregamento (seção 22.4 — desempenho é parte do desenho):** carregue **apenas os pesos usados** — Montserrat 300, 500 e 600; Source Sans 3 400 e 600; JetBrains Mono 500. Todas com `font-display: swap`. Peso que não está nesta lista não é carregado; se uma página precisar de um peso novo, ele entra **aqui** antes de entrar na casca.

## Espaço, raio, sombra

Espaço na escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 6px` · `--r-md 12px`. Borda 1 px em `--traco`.
Sombra única: `0 1px 2px rgba(15,37,57,.06)`. **A caixa do resultado não usa sombra: usa borda esquerda de 3 px em `--sinal`.**

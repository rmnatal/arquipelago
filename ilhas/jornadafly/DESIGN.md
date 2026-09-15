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

**PENDENTE — arquivo vetorial.** A marca existe hoje como imagem de apresentação. O `logo.svg` desta pasta ainda **não** foi entregue pelo Raphael; enquanto não for, nenhuma casca publica header ou favicon definitivos. Não redesenhe um substituto.

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

- **Títulos e marca:** grotesca geométrica de caixa alta espaçada, no espírito da arte oficial. A família definitiva entra aqui quando o Raphael entregar o vetor e o nome da fonte usada. **Até lá, a casca não fixa fonte de título.**
- **Texto:** Source Sans 3 400/600. Corpo 1,0625 rem, altura de linha 1,7, medida máxima 66 caracteres.
- **Dinheiro, dias, número de pessoas e data de coleta:** JetBrains Mono 500 com `tabular-nums`. Texto corrido nunca vai em mono.

Escala (rem, base 16): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.3125` · `--t-xl 1.75` · `--t-2xl 2.375`.

## Espaço, raio, sombra

Espaço na escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 6px` · `--r-md 12px`. Borda 1 px em `--traco`.
Sombra única: `0 1px 2px rgba(15,37,57,.06)`. **A caixa do resultado não usa sombra: usa borda esquerda de 3 px em `--sinal`.**

# DESIGN — Clube do Mosaico

Dono dos tokens desta ilha. A casca renderiza a partir daqui; o `PROMPT.md` não é mais dono da paleta. Cor, fonte ou medida que não está neste arquivo é defeito, não identidade (seção 22.6 do `ARQUIPELAGO.md`) — foi essa regra que barrou, em 11/09, um segundo branco a quatro passos do branco aprovado. O `VOZ.md` manda na palavra, este arquivo manda na forma; quando discordarem, o `VOZ.md` decide.

**Molde de casca: LOJA.** Domingo à tarde, sem pressa. Foto grande, muito branco, produto primeiro.

## Cor
Paleta lida pixel a pixel do logo e aprovada pelo Raphael em 10/09/2026.

| token | valor | onde |
|---|---|---|
| `--papel` | `#FFFFFF` | fundo do miolo e do cabeçalho. **Miolo branco, cara de e-commerce** |
| `--tinta` | `#1F1715` | texto corrido e menu |
| `--coral` | `#FC483B` | marca e **cor de sinal**: botão, preço, passagem do menu. Um uso forte por tela |
| `--rubi` | `#8A0F18` | link e texto de destaque sobre branco (4,5:1 garantido) |
| `--vinho` | `#69030C` | wordmark dentro do logo. **Não se usa em texto** |
| `--salmao` | `#FA7665` | pétalas laterais; só ilustração e hover, nunca texto sobre branco |
| `--noite` | `#000000` | **só o rodapé** |
| `--traco` | `#E9DCD7` | borda de 1 px, divisor |
| `--legenda` | `#6E5F5B` | medida, prazo, fonte, data |
| `--alerta` | `#B9791A` | ressalva técnica. Âmbar, nunca vermelho — vermelho é a marca |

**O preto nunca vai no topo.** O wordmark do logo é `--vinho` e desaparece no escuro; foi isso que sumiu com o logo em 11/09.

## Tipografia
- Títulos e **preço**: **Outfit** 600/700.
- Texto: **Source Sans 3** 400/600.
- Medida, quantidade, unidade, código de produto: **JetBrains Mono** 500 com `tabular-nums`. Texto corrido nunca vai em Mono.

Escala (rem): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.3125` · `--t-xl 1.75` · `--t-2xl 2.375`. Corpo 1.0625 rem, altura de linha **1.7** (mais folgada que nas outras ilhas — o ritmo é calmo), medida máxima 66 caracteres.

## Espaço, raio, borda
Escala de 4, com mais ar: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96`. Raio `--r-sm 8px` · `--r-md 14px` — cantos mais macios que os das outras ilhas. Borda 1 px em `--traco`. Sombra única e leve: `0 2px 8px rgba(31,23,21,.06)`. Generoso com branco: bloco de seção respira 64 px no desktop, 40 px no celular.

## Cabeçalho
Papel `--papel`, borda inferior de 1 px em `--traco`, sem sombra, altura ~96 px. O **logo completo do Raphael** (`https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png`, que já é transparente) em `<img>` de **64 px** de altura, `alt="Clube do Mosaico"`, link para `/`, e **nenhum texto ao lado** — o wordmark está desenhado dentro do arquivo. A lótus solta (`identidade/logo/lotus-512.png`) é ícone pequeno, nunca substitui o logo no cabeçalho. Menu em `--tinta` peso 500, passagem em `--coral`.

## Componentes
- **Cartão de peça** — a foto manda: proporção 4:5, `width`/`height` no HTML, `--r-md`. Nome em Outfit `--t-lg`, preço em Outfit 700 `--coral`, medida e prazo em `--legenda` `--t-sm`. Disponibilidade em texto, nunca contagem regressiva, nunca "mais vendido" inventado.
- **Vitrine** — carrossel permitido **abaixo da dobra**, sem autoplay, com os itens todos no HTML (seção 22.3).
- **Caixa de resposta das ferramentas** — `--papel` com borda de 2 px em `--coral`, quantidade em Mono `--t-xl`, a frase em linguagem de ateliê logo abaixo.
- **Bloco de compra do material** — abaixo da resposta, botão em `--coral`, aviso de comissão dentro do bloco.
- **"Como sabemos"** — no fim da página, `--t-sm`, fabricante e data em `--legenda`, link "fonte" como texto com `rel="nofollow noopener"`. Nunca na home, nunca no primeiro parágrafo.
- **A artesã** — foto redonda de 72 px, nome em Outfit, uma linha. No rodapé da home e no "feita por" de cada peça.
- **Trilha (breadcrumb)** — `--t-sm` `--legenda`, abaixo do cabeçalho, degrau atual igual ao H1.

## Rodapé
Único lugar escuro: `--noite`, texto em `--papel`, com divulgação de afiliados, o mapa das seções e a artesã. O logo no rodapé é a **lótus sozinha**, nunca o arquivo completo.

## O que este arquivo não decide
URL, árvore, breadcrumb como estrutura, âncora de link interno, `<title>`, ordem resposta-antes-da-explicação e JSON-LD. Seções 9, 14, 16 e 22.2.

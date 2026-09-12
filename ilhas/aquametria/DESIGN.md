# DESIGN — Aquametria

Dono dos tokens desta ilha. A casca renderiza a partir daqui; o `PROMPT.md` não é mais dono da paleta. Cor, fonte ou medida que não está neste arquivo é defeito, não identidade (seção 22.6 do `ARQUIPELAGO.md`). O `VOZ.md` manda na palavra, este arquivo manda na forma; quando discordarem, o `VOZ.md` decide.

**Molde de casca: GUIA.** O que a ilha vende é acertar a conta de primeira.

## Cor
| token | valor | onde |
|---|---|---|
| `--tinta` | `#0D1B22` | texto corrido, H1–H3 |
| `--lamina` | `#0E7C8C` | marca e cor de sinal: link, botão de compra, barra do resultado. **Um uso forte por tela** |
| `--papel` | `#F4F7F7` | fundo da página |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa de resultado |
| `--traco` | `#DDE5E6` | borda de 1 px, divisor |
| `--legenda` | `#5C7075` | fonte, data, nota de rodapé, unidade |
| `--alerta` | `#B5762A` | ressalva técnica. Âmbar, nunca vermelho |

Sem gradiente. Sem sombra colorida. Fundo escuro só no rodapé.

## Tipografia
- Títulos: **Chivo** 700.
- Texto: **IBM Plex Sans** 400/600.
- Número, unidade, litro, watt, L/h: **IBM Plex Mono** 500 com `tabular-nums`. Texto corrido nunca vai em Mono.
- Três famílias é o teto (seção 22.4). Todas com `font-display: swap`.

Escala (rem, base 16 px): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.25` · `--t-xl 1.625` · `--t-2xl 2.125`. Corpo 1.0625 rem com altura de linha 1.65; medida de leitura no máximo **68 caracteres**. H1 `--t-2xl` no desktop, `--t-xl` no celular.

## Espaço, raio, borda
Escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio: `--r-sm 6px` (campo, botão) · `--r-md 10px` (cartão, caixa de resultado). Borda sempre 1 px em `--traco`. Sombra única e discreta: `0 1px 2px rgba(13,27,34,.06)`; a caixa de resultado não usa sombra, usa borda de 2 px em `--lamina`.

## Componentes
- **Caixa de resultado** — o elemento mais importante da ilha. Sempre acima da dobra, `--superficie`, borda de 2 px `--lamina`, número em Mono `--t-2xl`, unidade em `--t-lg`, a frase de leitura logo abaixo em `--t-base`. Nasce pré-renderizada com o caso padrão (seção 22.3).
- **Bloco de compra** — imediatamente abaixo da caixa de resultado, antes de qualquer explicação. Botão em `--lamina`, aviso de comissão dentro do bloco em `--t-sm` `--legenda`. Nasce mesmo sem link, dizendo "link de loja em breve".
- **Tabela de prova** — `--superficie`, cabeçalho em `--legenda` `--t-sm` maiúsculas com espaçamento, números em Mono alinhados à direita, linhas zebradas com `--papel`. No celular vira rolagem horizontal dentro do próprio contêiner, nunca some.
- **"Como sabemos"** — no fim da página, `--t-sm`, fonte e data em `--legenda`, o link da fonte como texto com `rel="nofollow noopener"`, nunca botão.
- **Cartão de calculadora** — a pergunta na linguagem da pessoa como título, uma linha de explicação, sem ícone decorativo.
- **Trilha (breadcrumb)** — `--t-sm` `--legenda`, logo abaixo do cabeçalho, separador `›`, o degrau atual sem link. O degrau é sempre igual ao H1 da página.

## Cabeçalho e rodapé
Cabeçalho claro (`--superficie`, borda inferior 1 px `--traco`, altura ~72 px), símbolo à esquerda, menu curto: Calculadoras · Produtos · Guias. Sem hero de texto. Rodapé escuro em `--tinta` com divulgação de afiliados, "como sabemos" geral e o mapa das seções.

## O que este arquivo não decide
URL, árvore, breadcrumb como estrutura, âncora de link interno, `<title>`, ordem resposta-antes-da-explicação e JSON-LD. Isso é das seções 9, 14, 16 e 22.2 — e o desenho não toca.

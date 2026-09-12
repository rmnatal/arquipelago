# DESIGN — Robometria

Dono dos tokens desta ilha. A casca renderiza a partir daqui; o `PROMPT.md` não é mais dono da paleta. Cor, fonte ou medida que não está neste arquivo é defeito, não identidade (seção 22.6 do `ARQUIPELAGO.md`). O `VOZ.md` manda na palavra, este arquivo manda na forma; quando discordarem, o `VOZ.md` decide.

**Molde de casca: FERRAMENTA.** A ferramenta é a home. A pessoa chega irritada e quer "serve" ou "não serve" em dois segundos.

## Cor
| token | valor | onde |
|---|---|---|
| `--tinta` | `#16191D` (grafite) | texto corrido, títulos |
| `--varredura` | `#CC3311` | marca e **cor de sinal: um uso por tela**. O veredito e o botão de compra. Ausente do corpo do texto |
| `--piso` | `#F2F1EF` | fundo da página |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do veredito |
| `--traco` | `#DFDCD6` | borda de 1 px, divisor |
| `--legenda` | `#6B6862` | código de peça, fonte, data |
| `--alerta` | `#A26A00` | ressalva técnica. Âmbar, nunca vermelho — vermelho é a marca |

Sem gradiente. O vermelho aparece uma vez por tela e nunca como fundo de bloco grande.

## Tipografia
- Títulos: **Archivo** 700.
- Texto: **IBM Plex Sans** 400/600.
- Todo número, unidade e **código de peça**: **IBM Plex Mono** 500 com `tabular-nums`. Texto corrido nunca vai em Mono.
- Assinatura da marca: `ROBO` em Archivo 700 + `METRIA` em Archivo 400, coladas, sem espaço. Nunca no mesmo peso, nunca separadas, nunca inclinada.

Escala (rem): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.25` · `--t-xl 1.625` · `--t-2xl 2.125`. Corpo 1.0625 rem, altura de linha 1.6, medida máxima 68 caracteres. Ritmo rápido: parágrafo curto, muito respiro entre blocos.

## Espaço, raio, borda
Escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 4px` · `--r-md 8px` — cantos mais secos que os das outras ilhas, porque a ilha é técnica. Borda 1 px em `--traco`. Sombra única: `0 1px 2px rgba(22,25,29,.07)`.

## Componentes
- **Veredito** — o elemento mais importante. Três estados, e o estado é visível antes de ler: **serve** (borda esquerda de 4 px em `--varredura`, palavra em Archivo 700 `--t-xl`), **não serve** (borda em `--legenda`, mesma forma), **serve se** (borda em `--alerta`, com a condição na linha seguinte). Acima da dobra, sempre.
- **Seletor "Qual é o seu robô?"** — marca e modelo, na home, acima de tudo. Os três atalhos (filtro · escova · bateria) logo abaixo, como links de verdade para as páginas, não como filtros de JS (seção 22.3).
- **Bloco de compra** — imediatamente abaixo do veredito, antes de qualquer explicação. Aviso de comissão dentro do bloco. Nasce mesmo sem link, reservando o lugar com "link de loja em breve".
- **Tabela de compatibilidade** — `--superficie`, código do fabricante em Mono, cabeçalho em `--legenda` `--t-sm` maiúsculas, rolagem horizontal no celular dentro do contêiner.
- **"Como sabemos"** — nota discreta no fim, `--t-sm`, link "fonte" como texto com `rel="nofollow noopener"`, nunca botão, sem fundo.
- **Trilha (breadcrumb)** — `--t-sm` `--legenda`, abaixo do cabeçalho, degrau atual igual ao H1.

## Cabeçalho e rodapé
Cabeçalho claro e enxuto (`--superficie`, borda inferior 1 px, ~64 px), símbolo do encaixe à esquerda com a assinatura, menu curto: Peças · Modelos · Guias. **Sem hero de texto.** Rodapé em `--tinta` com divulgação de afiliados e o mapa das seções.

## O que este arquivo não decide
URL, árvore, breadcrumb como estrutura, âncora de link interno, `<title>`, ordem veredito-antes-da-explicação e JSON-LD. Seções 9, 14, 16 e 22.2.

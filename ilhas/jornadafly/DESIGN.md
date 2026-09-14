# DESIGN — JornadaFly

Dono dos tokens desta ilha. A casca renderiza a partir daqui; o `PROMPT.md` não é dono da paleta. Cor, fonte ou medida que não está neste arquivo é defeito, não identidade (seção 22.6 do `ARQUIPELAGO.md`). O `VOZ.md` manda na palavra, este arquivo manda na forma; quando discordarem, o `VOZ.md` decide.

**Molde de casca: GUIA.** A pergunta mais frequente em cima, ferramentas como cartões na linguagem da pessoa, guias embaixo. (A Aquametria também é GUIA — por isso a paleta quente, a serifada editorial e a foto grande de cartão separam as duas à primeira vista.)

## Cor
| token | valor | onde | contraste medido |
|---|---|---|---|
| `--tinta` | `#1A1714` | texto corrido, H1–H3 | 17,85:1 sobre branco · 16,70:1 sobre `--papel` |
| `--sinal` | `#2F3E9E` (índigo de fim de tarde) | marca, link, botão, barra do resultado. **Um uso forte por tela** | 9,12:1 sobre branco · 8,53:1 sobre `--papel` |
| `--custo` | `#8A5A12` (ocre) | **o número de dinheiro** e a etiqueta de preço coletado. Só isso | 5,91:1 sobre branco · 5,53:1 sobre `--papel` |
| `--papel` | `#FAF7F2` (areia) | fundo da página. Quente, ao contrário do cinza frio da Ohmetria e do `#F4F7F7` da Aquametria | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do resultado | — |
| `--traco` | `#E3DCD1` | borda de 1 px, divisor | 1,27:1 — decorativo, **nunca carrega informação sozinho** |
| `--legenda` | `#6B625A` | operador, data da coleta, moeda, nota de rodapé | 5,97:1 sobre branco · 5,58:1 sobre `--papel` |
| `--alerta` | `#9A2B1E` | ressalva ("preço de 09/2026, alta temporada") | 7,67:1 sobre branco |
| `--ouro` | `#C79A3A` | **só sobre `--tinta`**, no rodapé escuro. Nunca sobre papel | 6,89:1 sobre `--tinta` |

Todos os pares de texto ficam acima de 4,5:1. Sem gradiente. Fundo escuro só no rodapé.
**REGRA DURA: nunca foto de fundo atrás de texto.** É o vício visual do nicho de viagem e quebra contraste em toda tela. Foto grande é bem-vinda **no cartão de experiência**, com o texto fora dela.

## Tipografia
- Títulos: **Fraunces** 600. Serifada de contraste alto, editorial — é o que separa esta ilha das três primeiras, todas em grotesca.
- Texto: **Source Sans 3** 400/600.
- Dinheiro, dias, número de pessoas, data de coleta: **JetBrains Mono** 500 com `tabular-nums`. Texto corrido nunca vai em Mono.
- Assinatura da marca: `JORNADA` em 700 caixa alta + `fly` em 400 caixa baixa, coladas, sem espaço. **`fly` nunca maior que `JORNADA`** — o olho lê "jornada" primeiro, e é isso que o produto promete.
- Três famílias é o teto. Todas com `font-display: swap`.

Escala (rem): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.3125` · `--t-xl 1.75` · `--t-2xl 2.375`. Corpo 1,0625 rem, altura de linha **1,7**, medida máxima **66 caracteres**.

## Espaço, raio, borda
Escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 6px` · `--r-md 12px` — mais macios que os da Ohmetria, porque a leitura aqui é de planejamento, não de emergência. Borda 1 px em `--traco`. Sombra única: `0 1px 2px rgba(26,23,20,.06)`.

## Símbolo
Gesto do nicho: **comparar o que se paga com o que se recebe**. Grade de 24, traço de 2 px, cantos retos.
Uma barra horizontal de `(3,9)` a `(21,9)` em `--tinta`; outra, menor, de `(3,16)` a `(14,16)` em `--sinal`; e um marcador vertical de `(14,12)` a `(14,20)` em `--custo`, na ponta da menor — é o ponto em que a decisão é tomada. Duas leituras postas lado a lado, com parentesco visual de régua vista de lado, e nada mais.
O vão entre as barras nunca fecha abaixo de 3 px, para o favicon de 16 px funcionar.
**PROIBIDO no símbolo: avião, asa, mala, globo, passaporte, carimbo, mapa dobrado, bússola, montanha e balão.** O domínio diz "Fly", o produto não voa — se o símbolo voar, a contradição vira a cara do site.
O desenho de referência está em `bussola/dossies/viagem-experiencia-icone/logo.svg`.

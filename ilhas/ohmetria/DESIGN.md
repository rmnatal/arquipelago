# DESIGN — Ohmetria

Dono dos tokens desta ilha. A casca renderiza a partir daqui; o `PROMPT.md` não é dono da paleta. Cor, fonte ou medida que não está neste arquivo é defeito, não identidade (seção 22.6 do `ARQUIPELAGO.md`). O `VOZ.md` manda na palavra, este arquivo manda na forma; quando discordarem, o `VOZ.md` decide.

**Molde de casca: FERRAMENTA.** A F1 é a home. A pessoa chega com o falante já comprado e quer "fecha" ou "não fecha" em dois segundos.

## Cor
| token | valor | onde | contraste medido |
|---|---|---|---|
| `--tinta` | `#101A24` | texto corrido, H1–H3 | 17,57:1 sobre `--superficie` · 15,80:1 sobre `--piso` |
| `--sinal` | `#B86E00` | marca, preenchimento, barra do veredito, botão. **Um uso forte por tela** | 3,99:1 sobre branco · 4,41:1 sobre `--tinta` |
| `--sinal-texto` | `#8A5200` | o mesmo âmbar em versão de texto: link, rótulo, número em destaque | 6,39:1 sobre branco · 5,75:1 sobre `--piso` |
| `--piso` | `#F1F3F6` | fundo da página. Cinza **frio** — a Robometria usa `#F2F1EF`, quente; é aqui que as duas se separam à primeira vista | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do resultado | — |
| `--traco` | `#D5DBE3` | borda de 1 px, divisor | 1,39:1 — decorativo, **nunca carrega informação sozinho** |
| `--legenda` | `#5E6B7A` | fonte, data de leitura, unidade, código de modelo | 5,44:1 sobre branco · 4,89:1 sobre `--piso` |
| `--alerta` | `#B3261E` | ressalva técnica ("este módulo não estabiliza em 1 ohm") | 6,54:1 sobre branco |

**TRAVA, e não é preferência:** `#B86E00` **reprova em texto normal** (3,99:1, e o mínimo é 4,5:1). Onde for texto, é `#8A5200`. O `#B86E00` só entra em preenchimento, ícone e texto grande de 24 px para cima.
Sem gradiente. Sem sombra colorida. O âmbar aparece **uma vez por tela** e nunca como fundo de bloco grande. Fundo escuro (`--tinta`) só no rodapé.

## Tipografia
- Títulos: **Saira Condensed** 700. Condensada, com a verticalidade de escala de painel.
- Texto: **Public Sans** 400/600.
- Todo número, unidade e código de modelo — ohm, W RMS, litro, mm², Hz: **Roboto Mono** 500 com `tabular-nums`. Texto corrido nunca vai em Mono.
- Assinatura da marca: `OHM` em Saira Condensed 700 + `ETRIA` em Saira Condensed 400, coladas, sem espaço, caixa alta. Nunca no mesmo peso, nunca separadas, nunca inclinada.
- Três famílias é o teto (seção 22.4). Todas com `font-display: swap`.
- **Nenhuma família coincide com a da Robometria** (Archivo + IBM Plex Sans + IBM Plex Mono). Duas ilhas no mesmo molde precisam parecer sites diferentes.

Escala (rem, base 16 px): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.25` · `--t-xl 1.75` · `--t-2xl 2.25`. Corpo 1,0625 rem com altura de linha 1,6; medida de leitura no máximo **68 caracteres**.

## Espaço, raio, borda
Escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 4px` (campo, botão) · `--r-md 8px` (cartão, caixa de resultado). Borda sempre 1 px em `--traco`. Sombra única: `0 1px 2px rgba(16,26,36,.07)`. **A caixa do veredito não usa sombra: usa borda de 2 px em `--sinal`.**

## Símbolo
Gesto técnico do nicho: **fechar o circuito na impedância certa**. Grade de 24, traço uniforme de 2 px, cantos retos, sem gradiente.
Dois arcos espelhados sobem de `(5,20)` e `(19,20)` até `(12,8)`, raio 7, formando uma ferradura fechada — dois caminhos que viram um. Um traço vertical de `(12,3)` a `(12,8)`, em `--sinal`, é o **ponto de medida**: é ele que muda de cor quando a ferramenta dá o veredito.
O vão entre os arcos nunca fecha abaixo de 3 px, para o favicon de 16 px funcionar. **Não é o glifo Ω** — seria notação emprestada, não desenho próprio. **Nada de carro, alto-falante, onda sonora, nota musical ou fone.**
O desenho de referência está em `bussola/dossies/som-automotivo/logo.svg`.

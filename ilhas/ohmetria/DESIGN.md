# DESIGN — OHMETRIA

Dono dos tokens desta ilha (seção 22.6 do `ARQUIPELAGO.md`). A casca renderiza a partir daqui.
**Token novo não nasce em despacho:** cor, fonte ou medida que não estiver neste arquivo é defeito, não identidade.
Quando este arquivo e o `VOZ.md` discordarem, **manda o `VOZ.md`** (seção 22.2) — ele é quem fala com a pessoa.

## Símbolo — aprovado pelo Raphael em 14/09/2026

**"O paralelo":** duas barras horizontais iguais (os dois caminhos) e o traço âmbar que as fecha no meio.
Gesto técnico do nicho: fechar o circuito na impedância certa. Arquivo: `logo.svg`, grade de 24, traço 2, cantos retos, sem gradiente e sem sombra.

**Registro da recusa:** a primeira proposta (dois arcos em ferradura, do dossiê) foi recusada por ele porque repetia a receita da Robometria — arco escuro mais peça colorida. Fica escrito para ninguém "restaurar" o desenho antigo achando que é o original.

**Regra de uso, obrigatória:** sozinho e pequeno, o símbolo pode ser lido como sinal de igual ou ícone de menu. No cabeçalho e em qualquer barra de navegação ele anda **sempre colado à palavra OHMETRIA**. Isolado só em favicon, avatar e onde o contexto já é a marca.

**Assinatura:** `OHM` em peso 700 + `ETRIA` em peso 400, coladas, sem espaço, caixa alta. Nunca separadas, nunca no mesmo peso, nunca inclinada.

## Cor — contraste medido, não estimado

| token | valor | onde | contraste |
|---|---|---|---|
| `--tinta` | `#101A24` | texto corrido, H1–H3 | 17,57:1 sobre `--superficie` · 15,80:1 sobre `--piso` |
| `--sinal` | `#B86E00` | marca, preenchimento, barra do veredito, botão. **Um uso forte por tela** | 3,99:1 sobre branco → só preenchimento, ícone e texto ≥ 24 px; **nunca texto corrido** |
| `--sinal-texto` | `#8A5200` | link, rótulo, número em destaque | 6,39:1 sobre branco · 5,75:1 sobre `--piso` |
| `--piso` | `#F1F3F6` | fundo da página (cinza frio — a Robometria usa quente) | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do resultado | — |
| `--traco` | `#D5DBE3` | borda de 1 px, divisor (decorativo, nunca carrega informação sozinho) | 1,39:1 |
| `--legenda` | `#5E6B7A` | fonte, data de leitura, unidade, código de modelo | 5,44:1 sobre branco · 4,89:1 sobre `--piso` |
| `--alerta` | `#B3261E` | ressalva técnica | 6,54:1 sobre branco |

**Portão:** `#B86E00` reprova em texto normal. Onde for texto, é `#8A5200`. Sem gradiente, sem sombra colorida, sem fundo âmbar em bloco grande. Fundo escuro (`--tinta`) só no rodapé.

## Tipografia

- **Títulos:** Saira Condensed 700.
- **Texto:** Public Sans 400/600. Corpo 1,0625 rem, altura de linha 1,6, medida máxima 68 caracteres.
- **Número, unidade e código de modelo (Ω, W RMS, litro, mm², Hz):** Roboto Mono 500 com `tabular-nums`.

Escala (rem, base 16): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.25` · `--t-xl 1.75` · `--t-2xl 2.25`.

## Espaço, raio, sombra

Espaço na escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 4px` · `--r-md 8px`. Borda 1 px em `--traco`.
Sombra única: `0 1px 2px rgba(16,26,36,.07)`. **A caixa do veredito não usa sombra: usa borda de 2 px em `--sinal`.**

## Canvas de identidade

Montado na conversa em 14/09/2026 (fecha a pendência P7 da rodada 004): marca, paleta com contraste medido, tipografia e a home no celular.

# DESIGN — RODAMETRIA

Dono dos tokens desta ilha (seção 22.6 do `ARQUIPELAGO.md`). Nasce no dossiê; a Fundação copia para `ilhas/rodametria/DESIGN.md` no dia do nascimento.
**Token novo não nasce em despacho.** Quando este arquivo e o `VOZ.md` discordarem, manda o `VOZ.md`.

## Marca — aprovada pelo Raphael em 27/10/2026

- **Símbolo: V9.** Patinete elétrico visto de frente (guidão com manoplas e manetes, painel com tela verde, coluna, farol com centro verde, para-lama, garfo e roda com três risquinhos), com **asas curvas em forma de pena**, três de cada lado, e **onze raios verdes** saindo do farol. Arquivo: `logo.svg` (viewBox 120).
- **Assinatura horizontal aprovada: H1.** Símbolo à esquerda; à direita, `RODAMETRIA` em Alfa Slab One e, embaixo, `MOBILIDADE ELÉTRICA` em Barlow 600, caixa alta, espaçamento 0,32 em, entre duas linhas de 2 px.
- **Vertical:** símbolo em cima, `RODAMETRIA` embaixo, a linha `MOBILIDADE ELÉTRICA` entre traços.
- **O símbolo nunca perde detalhe.** Em qualquer tamanho do cabeçalho vai o desenho completo (raios, manetes, garfo, risquinhos da roda) — pedido do Raphael ao ver uma versão enxuta. Só o favicon (≤ 32 px) pode simplificar.
- **No cabeçalho do celular** a linha `MOBILIDADE ELÉTRICA` sai (ficaria com 8 px); símbolo + nome ficam.
- **Negativo (rodapé e fundo escuro):** desenho em branco, verdes em `#3FC08E`, farol com miolo `#13212B`.
- **Exceção registrada:** a seção 5(e) do `BUSSOLA.md` diz que o símbolo não desenha o produto. Nesta ilha o Raphael escolheu o produto (o patinete) como símbolo, depois de recusar abstrações (três barras, roda-velocímetro, dez conceitos). Decisão dele, vale só para a Rodametria.
- **Registro das recusas, para ninguém restaurar:** "os três números" (três barras), "a roda-velocímetro" (parecia relógio), patinete de lado em linha fina, e os dez conceitos abstratos de 27/10/2026.
- O site vende **mobilidade elétrica**: patinete (núcleo, Shopee), peças e acessórios (Shopee), scooter, moto e bicicleta elétrica (bônus, Mercado Livre). Por isso a assinatura diz "mobilidade elétrica", nunca "patinete elétrico".

## Cor — contraste medido (WCAG 2.x)

| token | valor | onde | contraste |
|---|---|---|---|
| `--tinta` | `#13212B` | texto, títulos, símbolo | 15,38:1 sobre `--piso` · 16,40:1 sobre branco |
| `--verde` | `#0A6B4C` | raios e farol do símbolo, veredito "cabe", botão principal. **Um uso forte por tela fora da marca** | 6,11:1 sobre `--piso` · branco sobre ele 6,52:1 |
| `--verde-claro` | `#3FC08E` | só sobre `--tinta` (rodapé, negativo) | 7,14:1 sobre `--tinta` · **nunca sobre branco** (2,30:1) |
| `--alerta` | `#8F4A00` | "precisa de CNH", "não aguenta" | 6,26:1 sobre `--piso` |
| `--legenda` | `#4A5A66` | fonte, data, unidade | 6,68:1 sobre `--piso` |
| `--piso` | `#F6F8F7` | fundo da página | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, resultado | — |
| `--traco` | `#D3DAD7` | borda e divisor, decorativo | 1,42:1 |
| `--verde-fundo` | `#E8F3EE` | caixa do veredito "cabe" | verde 5,74:1 · tinta 14,44:1 |
| `--alerta-fundo` | `#FBF1E6` | caixa do veredito "não cabe" | âmbar 5,98:1 |

Sem gradiente, sem sombra colorida. Fundo escuro só no rodapé. Botão de loja em `--tinta`; o verde fica para o veredito.

## Tipografia

- **Nome da marca:** Alfa Slab One, só na assinatura (nunca em título de página).
- **Títulos:** Barlow Semi Condensed 700.
- **Texto:** Barlow 400/600. Corpo 1,0625 rem, linha 1,6, até 68 caracteres.
- **Número e unidade (W, km/h, V, Ah, Wh, km, kg, aro):** JetBrains Mono 500, `tabular-nums`.
Escala (rem): `.8125 · .9375 · 1 · 1.25 · 1.75 · 2.25`.

## Espaço, raio, sombra

Espaço na escala de 4 (`4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`). Raio 4 px (campo, botão) e 8 px (cartão). Borda 1 px `--traco`. A caixa do veredito usa borda de 2 px na cor do veredito, sem sombra.

## Canvas de identidade

Canvas "Rodametria — identidade visual" (Claude, 27/10/2026): pranchas da marca (V9 vertical, H1 horizontal), paleta, tipografia e a home no celular no molde de conversão (seção 32).

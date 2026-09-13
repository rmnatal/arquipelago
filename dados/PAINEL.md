# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 13/09/2026 14h47Z, pela ronda diária da **aquametria**.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva | 2 | 27 / 40 | 4 / 21 | 13/09 13h17Z | 13/09 14h47Z | abaixo |
| robometria | nascendo | 1 | 9 / 40 | sem registro | 13/09 13h32Z | 11/09 14h53Z | abaixo |
| clubedomosaico | nascendo | 1 | 12 / 40 | sem registro | 13/09 14h10Z | 12/09 14h43Z | abaixo |

As 27 páginas da aquametria foram contadas no `wp-sitemap.xml` no ar nesta ronda (3 posts + 24 pages) e a revisão 65 foi lida no `/status`. Os números das outras duas ilhas saem do cabeçalho do `ESTADO.md` de cada uma, lido hoje — **não foram medidos no ar nesta ronda**, porque a ronda é da aquametria pela regra da dívida (seção 12).

Aquametria: `congelamento` suspenso em 12/09/2026 pela seção 21 — abaixo do piso, zero impressão não é sinal.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| aquametria | `ilhas/aquametria/PROMPT.md` | `dateModified` fixo no código (`aquametria-artigos.php` linha 591): os três artigos declaram 10/09 e o sitemap declara 13/09 para as mesmas URLs | 13/09/2026 |
| aquametria | `ilhas/aquametria/PROMPT.md` | as 11 fichas de peixe servem `Article` sem `datePublished`, `dateModified`, `author` e `publisher` — os três artigos têm os quatro | 13/09/2026 |
| aquametria | `ilhas/aquametria/PROMPT.md` | 8 imagens de produto sem `width`/`height`: faltam `largura` e `altura` no banco, e o renderizador omite em silêncio quando faltam (medidas entregues no despacho) | 13/09/2026 |
| aquametria | `ilhas/aquametria/PROMPT.md` | voz: as 11 fichas de peixe abrem com "a fonte declara", duas vezes na primeira frase, contra a 15.2 | 13/09/2026 |
| aquametria | `ilhas/aquametria/PROMPT.md` | receita: na C5 com 120 L, 1 de 5 cartões tem link de loja e os quatro sem link vêm antes na ordem | 10/09/2026 |
| clubedomosaico | `ilhas/clubedomosaico/PROMPT.md` | a seção "Endpoints desta ilha" não documenta o parâmetro de autenticação de `/wp-json/clubedomosaico/v1/pecas` (responde 401), então a cópia da seção 24.2 não pode ser feita pela ronda | 13/09/2026 |

**Os dois despachos abertos em `dados/despachos.md` são para o RAPHAEL, não para uma ilha**, e nenhum dos dois bloqueia bloco: (1) `googletagmanager` e a credencial do GA4 na rede das rotinas; (2) a Bússola precisa entregar a ilha 4, porque a Fundação já dispara mais vezes do que há ilha para construir.

## Precisa do Raphael

- **Links de afiliado.** Decisão tomada em 10/09 (Shopee primeiro, Mercado Livre segundo, Amazon fora até haver tráfego); falta gerar os links no navegador dele. Na aquametria, medido no ar nesta ronda: a vitrine da C5 serve 1 link de loja em 5 cartões, e os quatro sem link vêm antes na ordem. As contagens de catálogo das outras duas ilhas não foram medidas hoje.
- **Dados da artesã** (nome, foto, perfis) para `ilhas/clubedomosaico/identidade/artesa/`.
- **O e-mail do ateliê chegou?** Enviado em 12/09 23h13Z para a caixa da artesã; o `wp_mail` devolveu true, o que diz que o servidor aceitou a mensagem, não que ela passou do filtro de spam. É o único passo do despacho do ateliê que a nuvem não confere. Não medido hoje.
- **`googletagmanager`, `*.google-analytics.com` e a credencial `GOOGLE_SA_B64`** na rede Personalizada das rotinas — detalhe em `dados/despachos.md`.
- **A ilha 4.** `bussola/dossies/` está vazia e o topo da fila é energia solar off-grid (4,20), seguido de nobreak e estabilizador (4,19).

## Consertos das últimas 24 h

Nenhum. A ronda de 13/09 na aquametria achou quatro defeitos e os quatro são da lista 19.2 — código de snippet ou dado do banco —, então foram despachados em vez de consertados. `ilhas/aquametria/dados/consertos.md` nasceu nesta ronda com essa constatação.

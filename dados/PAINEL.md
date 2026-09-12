# PAINEL DO ARQUIPÉLAGO

Instantâneo. Reescrito pela Sentinela ao fim de toda ronda (seção 23 do `ARQUIPELAGO.md`). Não escreva aqui se você não é a ronda.

**Escrito em:** 12/09/2026 23h20Z — as linhas da clubedomosaico e os despachos foram atualizados pela Fundação ao fechar o bloco 4d, porque deixá-los velhos é a armadilha que o despacho do GA4 registra (resumo velho lido como fato). O resto continua sendo o arquivo inicial. **A primeira ronda que rodar reescreve tudo abaixo** — a seção 23 diz que quem escreve o painel é a ronda diária, não a Fundação.

## Ilhas

| ilha | estado | prio | páginas | dias de indexação | última construção | última ronda | piso |
|---|---|---|---|---|---|---|---|
| aquametria | viva | 2 | 13 / 40 | 3 / 21 | 11/09 23h59Z | 10/09 14h55Z | abaixo |
| robometria | nascendo | 1 | 9 / 40 | sem registro | 11/09 23h37Z | 11/09 14h53Z | abaixo |
| clubedomosaico | nascendo | 1 | 12 / 40 | sem registro | 12/09 23h20Z | 12/09 14h43Z | abaixo |

Aquametria: `congelamento` suspenso em 12/09/2026 pela seção 21 — abaixo do piso, zero impressão não é sinal.

## Despachos abertos

| ilha | onde | o que é | aberto desde |
|---|---|---|---|
| _(nenhum em ilha)_ | — | nenhuma ilha tem defeito aberto: o despacho do ateliê foi fechado em 12/09 23h20Z e os dois de coerência da F1 e da F2 estão cumpridos desde 12/09 15h51Z | — |

**Os dois despachos abertos em `dados/despachos.md` são para o RAPHAEL, não para uma ilha** — e nenhum dos dois bloqueia bloco: (1) `googletagmanager` e a credencial do GA4 na rede das rotinas; (2) a Bússola precisa entregar a ilha 4, porque a Fundação já dispara mais vezes do que há ilha para construir e execução que acorda sem ilha elegível fecha vazia.

## Precisa do Raphael

- **Links de afiliado.** Decisão já tomada em 10/09 (Shopee primeiro, Mercado Livre segundo, Amazon fora até haver tráfego); falta gerar os links no navegador dele. Aquametria 39 de 78 produtos esperando; clubedomosaico 10 de 10; robometria no ar com zero link de loja.
- **Dados da artesã** (nome, foto, perfis) para `ilhas/clubedomosaico/identidade/artesa/`.
- **O e-mail do ateliê chegou?** Enviado em 12/09 23h13m23s Z para a caixa da artesã. O
  `wp_mail` devolveu true, o que diz que o servidor **aceitou** a mensagem — não que ela
  passou do filtro de spam da Hotmail. É o único passo do despacho do ateliê que a nuvem
  não consegue conferir, e a linha 178 do `PROMPT.md` da ilha manda tratar queda em spam
  como **bloqueio da ilha**, não como detalhe.
- **A option `cdm_whatsapp` da clubedomosaico está vazia.** Enquanto estiver, a ficha da
  peça serve a frase de que o contato não foi publicado, em vez de um número inventado.
  É de uma linha, e é o que transforma a ficha em venda.

## Consertos das últimas 24 h

Nenhum. A ronda de 12/09 na clubedomosaico foi a primeira da ilha e não achou defeito da lista 19.1.

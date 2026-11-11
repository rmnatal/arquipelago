# Série de posição por consulta — Rodametria

Uma linha por leitura semanal, por consulta ou por página. **Nunca sobrescrever linha antiga**: a série só vale porque cresce. Fonte: Search Console, propriedade `sc-domain:rodametria.com.br`. Regra e bandas na seção 12.1 do `ARQUIPELAGO.md`. **Posição é média, não é um lugar** — sempre com uma casa decimal.

## Leitura semanal de 2026-11-04 — janela 27/10→02/11 (7 dias)

**AINDA SEM DADO, e isto não é fracasso.** A propriedade existe e responde; a janela devolveu **0 impressão e 0 clique**, e a dimensão `page` não devolveu página nenhuma. A ilha subiu em 30/10 e o sitemap só foi enviado em 04/11 — **não há posição a medir porque a ilha ainda não entrou na disputa**. A série começa a valer na primeira leitura que trouxer impressão. Não escrever bloco de CTR, de título ou de malha em cima deste zero: ele é de indexação, nunca de ranqueamento (12.1).

---

## Leitura semanal de 2026-11-11 — janela 03→09/11 (7 dias), medida no navegador do Raphael

**A PRIMEIRA LINHA DE VERDADE DESTA SÉRIE.** Em 04/11 a resposta honesta era "ainda sem dado"; hoje existe dado, e ele é pouco e é claro.

| consulta | página | posição hoje | impressões | cliques | banda |
|---|---|---|---|---|---|
| mobilidade elétrica | (não atribuída na aba de consultas) | — | 4 | 0 | — |
| electric scooter vehicle price | (não atribuída) | — | 2 | 0 | — |
| mobilidade elatrica | (não atribuída) | — | 1 | 0 | — |

| página | posição 7d | impressões 7d | cliques 7d | banda |
|---|---|---|---|---|
| /veiculos/ | 59,0 | 8 | 0 | 21+ |

### O que esta leitura decide

- **AS TRÊS CONSULTAS NOMEADAS SÃO DE ASSINATURA, NÃO DE COMPRA.** `mobilidade elétrica` é literalmente o que a assinatura da marca diz (`MOBILIDADE ELÉTRICA`, `PROMPT.md`, Identidade), `mobilidade elatrica` é a mesma com erro de digitação, e `electric scooter vehicle price` é estrangeira. **Nenhuma das seis cabeças de compra do nicho gerou uma impressão sequer.** Isto não é problema de ranqueamento: pela 12.1, consulta sem impressão volta para a seção 14, e a 12.1 é literal — "não mexa no texto de uma página que o Google ainda não viu".
- **AS 8 IMPRESSÕES FORAM TODAS PARA `/veiculos/`, A MÃE DE CATEGORIA — E ZERO PARA AS DUAS PÁGINAS QUE TÊM BOTÃO DE COMPRA** (`/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`). Metade da explicação está medida: **`/veiculos/bicicleta-eletrica/` NÃO ESTÁ NO ÍNDICE** (ver o despacho). A outra metade, a do patinete, é idade: ela está no índice e ainda não recebeu impressão, e três semanas é cedo.
- **POSIÇÃO 59,0 É UM NÚMERO HONESTO E NÃO É SINAL.** A 12.1 manda anotar com uma casa decimal e nunca tratar média como lugar; a 21.1 manda não ler zero (ou quase zero) como informação abaixo do piso. A ilha tem 10 URLs de 40.
- **A BANDA 11-20 DESTA ILHA NÃO EXISTE AINDA**, e a série só começa a valer quando houver duas semanas comparáveis (12.1). A próxima leitura é a primeira que pode comparar.
- Não abri a SERP nesta leitura: **não verifiquei**. A 30.8 continua inteira.

---

### ERRATA E COMPLEMENTO DA LEITURA DE 2026-11-11 — e um DEFEITO do instrumento, que vale para duas ilhas

**ERRATA.** O bloco acima diz que a leitura pela nuvem falhou nos dois disparos. **É falso.** O commit `2169969db46983d48e6b669b59cd473a12c73fb5` gravou `dados/search-console-2026-11-11.md` às 19h51Z; o `raw.githubusercontent.com` serviu 404 em cache por mais de 20 minutos mesmo com `?v=`. **Lição de método, irmã da 20.5: cache de CDN também serve 404, e 404 em cache é indistinguível de arquivo que não existe — confira pelo `MAOS-LOG.md` antes de concluir que um disparo não gravou.**

**O QUE SÓ A NUVEM TEM: a consulta ATRIBUÍDA À PÁGINA, com a posição de cada uma.**

| consulta | página | posição hoje | impressões | cliques | banda |
|---|---|---|---|---|---|
| electric scooter vehicle price | /veiculos/ | 40,5 | 2 | 0 | 21+ |
| mobilidade elatrica | /veiculos/ | 50,0 | 1 | 0 | 21+ |
| mobilidade elétrica | /veiculos/ | 68,8 | 4 | 0 | 21+ |

**As três caem na MESMA página, `/veiculos/`, e as três estão na banda 21+.** A consulta de marca da ilha (`mobilidade elétrica`) é a de pior posição das três, em 68,8. Isso confirma, com a atribuição na mão, o que o bloco acima concluiu sem ela: **a ilha ainda não disputa nada de compra, e pela 12.1 o caminho é a seção 14, não o texto das páginas.**

**DEFEITO DO INSTRUMENTO, e ele é novo: `ferramentas/search-console.py` busca o sitemap em `https://<ilha>.com.br/sitemap.xml`, e as ilhas servem `wp-sitemap.xml`.** Nesta ilha a linha de indexação saiu `| 2026-11-11 | n/d | n/d | n/d | 8 | 0 |` com o erro gravado: `ProxyError … Tunnel connection failed: 403 Forbidden` em `https://rodametria.com.br/sitemap.xml`. **E há uma segunda metade nesse mesmo erro: o egresso do ambiente das MÃOS continua recusando `rodametria.com.br`, enquanto o egresso do ambiente da Sentinela JÁ o alcança** — as três portas da 29.2 desta ilha foram medidas em 200 da nuvem da Sentinela em 11/11 20h0xZ, na mesma hora em que as MÃOS tomavam 403. **São dois ambientes com listas de domínio diferentes, e isso nunca tinha sido separado por escrito.** O número bom desta linha (10 URLs, 9 indexadas, 90%) veio do navegador, não da nuvem.

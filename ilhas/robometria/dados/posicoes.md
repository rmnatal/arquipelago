# Série de posição por consulta — Robometria

Uma linha por leitura semanal, por consulta ou por página. **Nunca sobrescrever linha antiga**: a série só vale porque cresce. Fonte: Search Console, propriedade `sc-domain:robometria.com.br`, Desempenho → últimos 28 dias, país Brasil. Regra e bandas na seção 12.1 do `ARQUIPELAGO.md`. **Posição é média, não é um lugar** — sempre com uma casa decimal, nunca arredondada para "1º lugar".

| data | consulta | página | posição hoje | posição semana passada | variação | impressões | cliques | banda |
|---|---|---|---|---|---|---|---|---|
| 2026-09-16 | `context: location: brazil (not for language). do not include location references in your response. question: quero comprar peças de reposição e consumíveis para o meu robô (filtro, escovas, pano); como garantir compatibilidade com o modelo certo?` | a Search Console não atribui página a esta consulta | 10,0 | — (série nova) | — | 1 | 0 | 4 a 10 — CTR |
| 2026-09-16 | anonimizada pela Search Console (só 1 das 11 impressões tem consulta nomeada) | https://robometria.com.br/filtro-universal-de-robo-aspirador/ | 9,2 | — (série nova) | — | 5 | 0 | 4 a 10 — CTR |
| 2026-09-16 | anonimizada pela Search Console | https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/ | 6,8 | — (série nova) | — | 4 | 0 | 4 a 10 — CTR |
| 2026-09-16 | anonimizada pela Search Console | https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/ | 7,0 | — (série nova) | — | 2 | 0 | 4 a 10 — CTR |
| 2026-09-16 | — | https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/ | sem impressão | — | — | 0 | 0 | sem impressão nenhuma — é indexação, não ranqueamento (12.1). Não mexa no texto desta página. |
| 2026-09-23 | `context: location: brazil (not for language). do not include location references in your response. question: quero comprar peças de reposição e consumíveis para o meu robô (filtro, escovas, pano); como garantir compatibilidade com o modelo certo?` | https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/ | 9,0 | 10,0 (sem página atribuída) | **–1,0 e ganhou página** | 1 | 0 | 4 a 10 — CTR. **A consulta passou a ser atendida pela página construída para ela.** Em 16/09 a Search Console não atribuía página nenhuma; hoje atribui a R1. NÃO MEXER: a posição melhorou (12.1 proíbe mexer em página que está subindo). |
| 2026-09-23 | anonimizada pela Search Console | https://robometria.com.br/filtro-universal-de-robo-aspirador/ | sem impressão | 9,2 | **perdeu as 5 impressões** | 0 | 0 | sem impressão nenhuma — **o teste de CTR da proposta 2 de 16/09 é INMENSURÁVEL nesta janela.** O título novo está no ar desde 17/09 e não houve impressão para medir CTR. Rola para a leitura de 30/09. |
| 2026-09-23 | anonimizada pela Search Console | https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/ | sem impressão | 6,8 | **perdeu as 4 impressões** | 0 | 0 | idem — sem impressão, sem leitura de CTR. |
| 2026-09-23 | anonimizada pela Search Console | https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/ | sem impressão | 7,0 | **perdeu as 2 impressões** | 0 | 0 | idem — sem impressão, sem leitura de CTR. |

## Notas da primeira medição (2026-09-16)

- **A série começa a valer com duas semanas** (12.1). Esta é a linha 1: nenhuma variação existe ainda, e nenhuma decisão de banda deve ser tomada só com ela.
- **A ilha inteira soma 11 impressões e 0 clique**, posição média 7,9 no período 08/09 a 14/09. As três páginas com impressão estão TODAS na banda 4 a 10 — primeira página, sem clique. Com 11 impressões isso é amostra fina, não é diagnóstico de CTR fechado.
- **A única consulta nomeada tem forma de consulta de superfície de IA** (o prefixo `context: ... question: ...` é como as consultas de leque do modo IA do Google aparecem na Search Console). A Sentinela NÃO abriu a SERP para confirmar de que superfície ela veio — portanto: **não verifiquei**. O que é fato medido é o texto da consulta, a posição 10,0 e a impressão única.
- **O que essa consulta pede é exatamente o que a R1 responde** — "peças de reposição e consumíveis (filtro, escovas, pano), como garantir compatibilidade com o modelo certo". E a página construída para ela, `/qual-peca-serve-no-meu-robo-aspirador/`, **não está no índice**. Quem atendeu essa consulta foi outra página da ilha.

## O QUE MUDOU ENTRE A LEITURA DE 16/09 E A PRÓXIMA (17/09/2026, pela Fundação)

A Fundação executou a **proposta 2** da leitura de 16/09 e trocou `<title>` e
`<meta name="description">` das **três** páginas da banda 4 a 10. Está escrito
aqui, e não só no `REGISTRO.md`, porque a próxima leitura semanal precisa saber o
que mudou para poder ler a variação — série sem a lista do que foi mexido mede
tudo junto e não atribui nada.

**Nenhuma URL mudou** (proibido pela 12.1) e **nenhum nome de página mudou** nas
cinco superfícies (H1, og:title, trilha, cartão, primeira metade do `<title>`). O
que cedeu o lugar foi a **marca** no fim do `<title>`, e só nestas três.

| página | `<title>` até 16/09 | `<title>` desde 17/09 | posição a bater |
|---|---|---|---|
| `/filtro-universal-de-robo-aspirador/` | `Existe filtro universal de robô aspirador? – Robometria` | `Existe filtro universal de robô aspirador? – 0 das 35 peças` | 9,2 · CTR 0% · 5 impressões |
| `/quantos-pa-o-robo-aspirador-precisa/` | `Quantos Pa o seu robô aspirador precisa – Robometria` | `Quantos Pa o seu robô aspirador precisa – de 1.400 a 10.000 Pa` | 6,8 · CTR 0% · 4 impressões |
| `/quantos-m2-o-robo-aspirador-limpa-por-carga/` | `Quantos m² um robô aspirador limpa por carga – Robometria` | `Quantos m² um robô aspirador limpa por carga – 1 de 5 marcas` | 7,0 · CTR 0% · 2 impressões |

**O NÚMERO NÃO É DIGITADO**: os seis saem de `dados/casca-fatos.json`, derivado do
banco commitado. Quando o banco andar, o título anda junto — então a comparação da
próxima leitura é **entre títulos que podem não ser os mesmos textos**, e ela deve
copiar para cá o título servido no dia da medição, não confiar nesta tabela.

**A RESSALVA DA PRÓPRIA PROPOSTA, repetida aqui porque é ela que evita a
conclusão errada:** com 11 impressões no total, "CTR 0%" é amostra fina. Duas ou
três semanas de série ainda podem mostrar 0% sem que o título tenha nada a ver
com isso, e a 12.1 manda comparar com a média das outras na mesma posição — o que
esta ilha **continua sem ter com o que fazer**. Subida de CTR aqui é sinal; falta
de subida, sozinha, não é prova de que a troca não serviu.

**As outras seis páginas ficaram como estavam, de propósito.** Trocar tudo de uma
vez torna a próxima leitura ilegível: sem nada parado para comparar, qualquer
variação vira ruído.

## Notas da segunda medição (2026-09-23) — a comparação que esta série existia para fazer NÃO pôde ser feita

- **A ilha caiu de 11 impressões (08→14/09) para 1 (15→21/09), e as três páginas do teste de título ficaram com ZERO.** Sem impressão não há CTR, e sem CTR a proposta 2 de 16/09 continua sem veredito. **Isso não é prova de que a troca de título não serviu, e não é prova de que serviu** — é ausência de dado, e está escrito como ausência.
- **A ressalva da amostra fina, repetida pela terceira vez porque ela é o que impede a conclusão errada:** 11 e 1 são números pequenos demais para uma tendência. Uma queda de 11 para 1 numa ilha de 14 URLs é ruído compatível com o normal. **Não trate como regressão.**
- **O que É sinal, e é o único desta janela:** a R1 entrou no índice e a consulta de superfície generativa voltou pela segunda semana seguida, agora atribuída à página certa e na posição 9,0. **A proposta 1 de 16/09 fechou pelo critério que ela mesma escreveu** na metade da indexação; a metade "7 ou mais indexadas de 9" ficou para trás porque o sitemap passou a 14.
- **A proposta 3 pedia duas ou mais consultas no formato de superfície generativa para virar bloco. Apareceu UMA, a mesma.** Duas semanas, uma consulta por semana. Continua em registro e vigilância; **nenhum bloco nasce disto hoje.**
- **Não abri a SERP nesta leitura: não verifiquei.**

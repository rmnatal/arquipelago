# CONSERTOS DA SENTINELA — Clube do Mosaico

Trava 19.4(c) do `ARQUIPELAGO.md`: todo conserto que uma ronda faz entra aqui, e a ronda SEGUINTE abre esta lista antes de qualquer outra coisa e reconfere no ar o que está escrito. É essa releitura que substitui a validação pelo autor. Uma linha por conserto.

| data | URL | o que mudou | conferido pela ronda de |
|---|---|---|---|
| 2026-09-24 | as 17 URLs do sitemap, mais `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/` | o `.htaccess` da raiz tinha só o bloco `NFD EPC` e não tinha o `# BEGIN WordPress`: a ilha servia a página de estacionamento da HostGator em 16 das 17 URLs. Reparado por `flush_rewrite_rules( true )` pela rota `/rotas` da casca 1.12.0 | **a próxima ronda** |
| 2026-09-25 | os 31 links de Shopee do banco, servidos em `/materiais/qual-cola-usar-no-mosaico/` e `/materiais/quantas-pastilhas-para-mosaico/` | os `sub_id` estavam deslocados uma casa (`-clubedomosaico-F2--`, campo 1 vazio) nos 16 links de 13/09, e 15 itens não tinham piso encurtado. Todos regerados pela Open API (25.6, 25.8). As 13 chaves das pastilhas devolviam ZERO oferta e foram trocadas | **a próxima ronda** |

## 12/09/2026 — primeira ronda desta ilha, nenhum conserto

`ultima_ronda` era `null`: a ilha nunca tinha sido rondada. Foram abertas as 11 URLs no navegador do Raphael e nenhum defeito da lista fechada 19.1 apareceu — não há, portanto, nada para a próxima ronda reconferir nesta tabela.

Os dois defeitos encontrados são de **coerência da recomendação** (seção 12) e caem na lista 19.2 (lógica de ferramenta), então a Sentinela não os consertou: eles estão em `PROMPT.md`, na seção `## DESPACHO DA SENTINELA — 12/09/2026`. O que a próxima ronda tem de reconferir é aquele despacho, no ar, pelos critérios de "pronto quando" que ele declara.

## 24/09/2026 — CONSERTO DA FUNDAÇÃO, não da Sentinela, e está aqui de propósito

Esta tabela é da Sentinela pela 19.4(c). A linha acima foi escrita pela **Fundação**, e entra aqui por um motivo só: **a ronda seguinte abre esta lista antes de qualquer outra coisa**, e o que ela tem de reconferir é justamente a porta de entrada do site. O conserto está em `REGISTRO.md`, na entrada de 24/09 às 19h40Z, com o antes e o depois do arquivo.

**O que a próxima ronda reconfere, e é um comando:** `python3 ferramentas/conferir-no-ar.py .` — ele ganhou hoje a seção da porta de entrada e reprova se o sitemap, o `robots.txt` ou a raiz do REST saírem do ar, ou se um caminho inexistente passar a responder a página do hospedeiro em vez da desta ilha. Se reprovar, o diagnóstico por dentro do servidor está em `?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>`, e `&reparar=1` conserta.

**A causa de origem continua sem nome** (ver a seção 29.5 do `ARQUIPELAGO.md`). Se o defeito **voltar**, a 19.4(b) vale com força dobrada: defeito que volta não é defeito, é sintoma de causa que ninguém enxergou — e aí o caminho é chamado na HostGator sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`, não mais um reparo.

## 25/09/2026 — CONSERTO DA FUNDAÇÃO (bloco 0 do despacho do Raphael de 24/09)

Também não é conserto de Sentinela, e está aqui pelo mesmo motivo da linha de 24/09: **a ronda seguinte abre esta lista antes de qualquer outra coisa.**

**O que a próxima ronda reconfere, e são dois comandos:**

1. `python3 ferramentas/conferir-no-ar.py .` — ganhou hoje a seção *"O link de afiliado servido"*: ela varre as URLs do sitemap e **reprova se aparecer encurtador de Shopee que o banco não conhece**. É o portão que pega link velho continuando na tela depois de uma regeração, que é defeito mudo — o link antigo continua **vivo** na Shopee, nada dá 404, e a ilha só perde a atribuição.
2. `SHOPEE_APP_ID=… SHOPEE_SECRET=… python3 ../../ferramentas/conferir-sub-id.py` — gera um link de **bancada** e lê a casa do sub-id no `utm_content` do 301. **Não use link desta ilha nesse teste:** o salto do encurtador é onde a Shopee conta o clique, e a leitura semanal está justamente procurando o PRIMEIRO clique orgânico desta ilha (proposta 3 do despacho de 23/09). Um autoclique com a etiqueta `clubedomosaico` apaga esse sinal. É a seção **25.8** do contrato, escrita hoje.

**O que ela NÃO consegue reconferir, e é a metade que falta:** se o Relatório de cliques da Shopee passou a mostrar `clubedomosaico-f2---` com o campo 1 preenchido. Isso só aparece quando houver um clique **de gente**, e é o que o "pronto quando" do item 2 do despacho de 23/09 pede. Até lá o que está provado é a mecânica, na bancada, e que a tela serve os links de hoje.

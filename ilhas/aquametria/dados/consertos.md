# CONSERTOS DA SENTINELA — ilha Aquametria

Registro dos consertos que a ronda diária fez sozinha, pela lista fechada 19.1 do `ARQUIPELAGO.md`.
Regra 19.4(c): **a ronda seguinte abre este arquivo antes de qualquer outra coisa** e reconfere o que a anterior consertou. É essa releitura que substitui a validação por quem construiu.
Uma linha por conserto: data, URL, o que mudou, e quem conferiu depois.

| data | URL | o que mudou | conferido por |
|---|---|---|---|
| 2026-09-13 | — | **Nenhum conserto.** A ronda achou quatro defeitos e os quatro caem na lista fechada 19.2: `dateModified` fixo em `aquametria-artigos.php` linha 591; `Article` sem data/autor/publicador nas 11 fichas de peixe; `largura`/`altura` ausentes em 8 registros de imagem do banco; e a abertura das 11 fichas pela camada de prova, montada em `aquametria-peixes.php` linhas 2870-2884. Três são código de snippet e um é dado do banco — a regra 3 da seção 12 manda parar e despachar. Foram para o `DESPACHO DA SENTINELA — 2026-09-13` no `PROMPT.md`. | — |
| 2026-09-23 | — | **Nenhum conserto.** A ronda achou dois defeitos e os dois caem na lista fechada 19.2: (a) a home nao serve JSON-LD nenhum — o unico emissor de `ld+json` da casca e a trilha, e ela se pula na home, e nao existe `WebSite` nem `Organization` em lugar nenhum da ilha, entao e codigo de snippet; (b) 39 dos 78 itens do banco tem link de afiliado de produto e nao tem `afiliado.url_produto` (`intestavel: true`), e preencher exige ESCOLHER o anuncio, que e dado do banco. Foram para o `DESPACHO DA SENTINELA — 2026-09-23` no `PROMPT.md`. A linha de 13/09 acima registra zero conserto, entao nao havia conserto anterior a reconferir pela 19.4(c). | — |

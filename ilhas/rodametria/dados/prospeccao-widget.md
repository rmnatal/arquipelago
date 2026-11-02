# PROSPECCAO DO WIDGET — RODAMETRIA (bloco 6, secao 14.7 do contrato)

> **ARQUIVO GERADO por `ferramentas/gerar-prospeccao.py` a partir de**
> **`dados/prospeccao-widget.json`. Nao edite a mao:** o portao
> `validar-prospeccao.py` regera este texto e compara, e edicao a mao
> fica vermelha. Mude o JSON e rode o gerador.

Atualizado em **2026-11-02**. Instrumento desta passada: **busca**.

**NINGUEM ABRIU NENHUM SITE.** O egresso desta nuvem responde 403 no CONNECT para todo dominio fora da lista de permitidos. Medido NESTA ILHA em 29/10/2026, tres passadas cada, com `rodametria.com.br` e `aquametria.com.br` em 200 nas mesmas: `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br`, `evoo.com.br`, `www.casasbahia.com.br`, `www.extra.com.br` e `www.magazineluiza.com.br` todos em `connect_rejected`, classificacao lida no `__agentproxy/status` e nao suposta. O WebFetch devolve o mesmo. O unico instrumento que alcanca o mundo daqui e a BUSCA — o mesmo degrau por onde o banco desta ilha foi construido e por onde a jornadafly entrou em 27/10.

**NAO EXISTE `false` NESTE ARQUIVO.** Esta passada sabe afirmar PRESENCA, nunca ausencia — a mesma assimetria que a 30.8 ja escreveu para o veredito de SERP, aplicada a outro assunto. Um dominio nao aparecer na busca de calculadora nao prova que ele nao tem calculadora: prova que a busca nao o mostrou. Entao `vende_veiculo`, `publica_conteudo` e `ja_tem_calculadora` so aceitam `true` (com evidencia que os nomeia) ou `null` (= nao medido). O portao RECUSA `false`, de proposito, para o arquivo nao virar uma lista de negativas que ninguem mediu.

## PRIORIDADE 1 — vende o veiculo E publica no proprio dominio

| dominio | nome | tipo | vende veiculo | publica conteudo | ja tem calculadora |
|---|---|---|---|---|---|
| `bicieletric.com.br` | Bici Eletric | loja | sim | sim | nao medido |

### `bicieletric.com.br` — Bici Eletric

O UNICO candidato que fecha as duas condicoes com o que a busca alcanca: e loja, vende os DOIS veiculos que as ferramentas desta ilha classificam (bicicleta eletrica e patinete) e publica conteudo editorial NO PROPRIO DOMINIO, num guia com endereco proprio. Quem ja mantem pagina de guia tem onde encaixar uma ferramenta e ja tem o habito de publicar; quem nao tem precisa criar a pagina antes. E A OBSERVACAO HONESTA, escrita para quem abrir o site decidir: o guia dele se chama `Melhor Bicicleta Eletrica 2026`, que e o formato que o `VOZ.md` desta ilha proibe nominalmente e que o bloco 5c contou como assinatura de fazenda nas caudas. A diferenca medida aqui e que esta pagina esta no dominio de uma LOJA e fala dos proprios produtos, que e outra coisa de uma fazenda que vive de ocupar a consulta — mas quem abordar le a pagina antes.

- **dominio, tipo, vende_veiculo** (busca, 2026-11-02) — consulta `marcas brasileiras bicicleta elétrica patinete elétrico fabricante nacional loja própria site` → [Bici Eletric, Bicicletas Elétricas Sustentáveis](https://bicieletric.com.br/)
- **vende_veiculo** (busca, 2026-11-02) — consulta `blog dicas autonomia bateria patinete bicicleta elétrica CNH (restrita a bicieletric.com.br e outros cinco)` → [Patinete Elétrico Urban Scooter, Dobrável Bici Eletric](https://bicieletric.com.br/bike-patinete.html)
- **publica_conteudo** (busca, 2026-11-02) — consulta `blog dicas autonomia bateria patinete bicicleta elétrica CNH (restrita a bicieletric.com.br e outros cinco)` → [Melhor Bicicleta Elétrica 2026: Guia Completo e Comparativo Bici Eletric](https://bicieletric.com.br/guia-melhor-bike-eletrica.html)

## PRIORIDADE 2 — uma das duas condicoes, ou teto de tipo

| dominio | nome | tipo | vende veiculo | publica conteudo | ja tem calculadora |
|---|---|---|---|---|---|
| `brazilelectric.com.br` | Brazil Electric Bike | fabricante | sim | nao medido | nao medido |
| `caloi.com` | Caloi | fabricante | nao medido | sim | nao medido |
| `eletricz.com.br` | Eletricz | distribuidora | sim | nao medido | nao medido |
| `fatbikefloripa.com.br` | Fat Bike Floripa | loja | sim | nao medido | nao medido |
| `zeliastore.com.br` | Zélia Store | loja | sim | nao medido | nao medido |

### `brazilelectric.com.br` — Brazil Electric Bike

Fabricante de Goiania que se apresenta como produtor nacional de bicicleta eletrica, com linha propria. Fabricante vale menos que loja na prospecao de widget — vende pouco direto ao leitor e alcanca revenda em vez de leitor —, mas vale por outro motivo que e desta ilha em particular: o campo que falta ao banco inteiro e `potencia_nominal_w`, e `veiculos_com_nominal_declarado` esta em ZERO desde 28/10. Fabricante e o nivel 4 da escada de fontes, e o bloco 3e mediu que ele pode ser estruturalmente vazio neste nicho porque as duas marcas principais do banco sao marcas de marketplace. Este e um fabricante brasileiro com site proprio: e a contraprova do bloco 3e, e por isso a linha fica aqui mesmo sem conteudo medido.

- **dominio, tipo, vende_veiculo** (busca, 2026-11-02) — consulta `marcas brasileiras bicicleta elétrica patinete elétrico fabricante nacional loja própria site` → [Brazil Electric Bike - HOME](https://brazilelectric.com.br/)

### `caloi.com` — Caloi

Fabricante com blog proprio e secao dedicada a bicicleta eletrica, que publica exatamente o assunto da F2 (o que olhar na bateria e na potencia antes de comprar). E A RESSALVA ESTA MEDIDA E E DE QUALIDADE DE LINK, nao de produto: a propria busca registrou que a pagina de blog dele carrega comentarios de spam com links de apostas. A 14.7 proibe link pago e PBN porque a penalizacao custa mais que o ganho, e dominio que deixa a secao de comentarios aberta a spam e dominio cujo link vale menos do que o nome sugere. Quem abrir o site confere isso ANTES de qualquer abordagem — esta linha existe para que a conferencia aconteca, nao para desqualificar de longe.

- **dominio, tipo, publica_conteudo** (busca, 2026-11-02) — consulta `"bicicleta elétrica" loja oficial brasil blog autonomia bateria dicas comprar` → [Vai comprar uma bike elétrica? Tudo o que você precisa saber antes de decidir](https://caloi.com/blog/eletrica/vai-comprar-uma-bike-eletrica-tudo-o-que-voce-precisa-saber-antes-de-decidir/)

### `eletricz.com.br` — Eletricz

Distribuidora de Sao Paulo com catalogo proprio por MODELO — patinete, monociclo e bicicleta eletrica —, em dois enderecos do mesmo dominio (`www.` e `loja.`). E o candidato cujo catalogo mais se parece com a entrada das ferramentas desta ilha: as fichas dele declaram bateria em V e Ah ao lado da autonomia, que e exatamente o par que a F2 recebe, e uma delas usa a palavra AUTOPROPELIDO no titulo do produto, que e a saida da F1. Nao subiu para 1 por uma razao so, e ela e de medicao: a busca restrita ao dominio nao devolveu pagina editorial nenhuma, so ficha de produto e a pagina de SAC. Conteudo `null` e nao medido.

- **dominio, tipo, vende_veiculo** (busca, 2026-11-02) — consulta `patinete elétrico bicicleta elétrica comprar loja (restrita a eletricz.com.br e outros quatro)` → [Especialistas em Bicicletas Elétricas. Escolha a sua Bike elétrica Na Eletricz.](https://www.eletricz.com.br/veiculos/bicicleta-eletrica)
- **vende_veiculo** (busca, 2026-11-02) — consulta `blog dicas guia como escolher autonomia CNH patinete scooter elétrica (restrita a eletricz.com.br e outros quatro)` → [Patinete Elétrico autopropelido KingSong KS-N14 + → Patinete elétrico](https://www.eletricz.com.br/veiculos/patinete-eletrico/patinete-eletrico-autopropelido-kingsong-n14)

### `fatbikefloripa.com.br` — Fat Bike Floripa

Loja de Florianopolis com secao propria de eletricos, bicicleta e patinete no mesmo catalogo, novo e seminovo. A ficha que a busca devolveu anuncia um patinete de 2000 W — potencia que, pelo numero que o corpus desta ilha colheu para o limite nacional, cai FORA do autopropelido —, e vender acima do limiar e exatamente o lugar em que a pergunta da F1 aparece na cabeca de quem compra. Conteudo editorial nao foi medido.

- **dominio, tipo, vende_veiculo** (busca, 2026-11-02) — consulta `patinete elétrico bicicleta elétrica comprar loja (restrita a fatbikefloripa.com.br e outros quatro)` → [Bike Elétrica - Oferta de Bicicleta e Patinete Elétrico](https://www.fatbikefloripa.com.br/eletricas)
- **vende_veiculo** (busca, 2026-11-02) — consulta `blog dicas autonomia bateria patinete bicicleta elétrica CNH (restrita a fatbikefloripa.com.br e outros cinco)` → [Patinete Scooter Elétrico Off-Road TD-Monster 2000W Seminovo - Fat Bike Floripa](https://www.fatbikefloripa.com.br/patinete-scooter-eltrico-off-road-td-monster-2000w-seminovo)

### `zeliastore.com.br` — Zélia Store

A loja desta lista que vende exatamente o que as DUAS consultas de maior volume desta ilha pedem e que a Shopee nao entrega: moto eletrica e scooter eletrica de 1000 W, com preco publicado. `veiculos/moto-eletrica` (823 mil buscas/mes) e `veiculos/scooter-eletrica` (301 mil) tem SERP `alvo` vista no Chrome em 27/10 e endereco reservado desde o bloco 5b, e nao nascem por falta de PRODUTO — cinco registros percorreram a escada de chaves inteira e a loja devolveu zero em todos os degraus. E o argumento de prospecao esta no titulo das paginas dela: as duas vendem `sem CNH` e uma cita a Resolucao Contran 996/2023 no corpo. Quem anuncia `sem CNH` e quem mais precisa da pergunta respondida com numero, e e a venda dele que a duvida trava.

- **dominio, tipo, vende_veiculo** (busca, 2026-11-02) — consulta `patinete elétrico scooter elétrica loja brasil autopropelido sem CNH 1000W comprar site oficial marca` → [Moto Elétrica JET 1000W Preta sem CNH por R$ 3.889,00](https://zeliastore.com.br/jet-preta/)
- **vende_veiculo** (busca, 2026-11-02) — consulta `patinete elétrico scooter elétrica loja brasil autopropelido sem CNH 1000W comprar site oficial marca` → [Scooter Elétrica X12 1000W sem CNH por R$ 6.732,40](https://zeliastore.com.br/x12-1000w/)

## PRIORIDADE 3 — ja tem calculadora, tipo que nao atravessa, ou nada medido

| dominio | nome | tipo | vende veiculo | publica conteudo | ja tem calculadora |
|---|---|---|---|---|---|
| `diasbike.com.br` | Dias Bike | desconhecido | nao medido | sim | nao medido |
| `guiaebike.com.br` | Blog GuiaEbike | fazenda | nao medido | sim | nao medido |
| `melhoresparacomprar.com.br` | Melhores Para Comprar | fazenda | nao medido | sim | nao medido |
| `techinter.com.br` | Techinter — mobilidade elétrica | fazenda | nao medido | sim | nao medido |

### `diasbike.com.br` — Dias Bike

Mantem blog com endereco proprio (`blog.diasbike.com.br`, subdominio do dominio dele, que pela regra 2 conta como site proprio) e publica sobre bicicleta — o que o faz ter ONDE por uma ferramenta. O `tipo` fica `desconhecido` de proposito: o nome diz loja de bicicleta e a busca NAO devolveu uma pagina de catalogo dele, muito menos de eletrica. Chutar `loja` subiria a prioridade dele de 3 para 2 sobre uma leitura de nome, e leitura de nome erra — a 30.8 ja escreveu essa licao para leitura de slug. Nao saber e motivo para descer, nunca para chutar.

- **dominio, publica_conteudo** (busca, 2026-11-02) — consulta `marcas brasileiras bicicleta elétrica patinete elétrico fabricante nacional loja própria site` → [11 Marcas de Bicicletas Brasileiras para Você Conhecer](https://blog.diasbike.com.br/tipos-bicicleta/marcas-de-bicicletas-brasileiras-que-voce-precisa-conhecer/)

### `guiaebike.com.br` — Blog GuiaEbike

Blog dedicado a bicicleta eletrica, com volume de publicacao visivel e paginas de uso real (`Como Ligar uma Bicicleta Eletrica`, `Niveis de Assistencia da E-bike`). ENTRA COMO FAZENDA, E A CLASSIFICACAO E MEDIDA E NAO IMPRESSAO: o mesmo dominio publica `As 7 Melhores Marcas de Bicicleta Eletrica que Dominam o Brasil em 2026` e `Melhor Bicicleta Eletrica Nacional`, que e literalmente o formato `melhor X` e `Top 10` que o bloco 5c desta ilha contou como assinatura de fazenda em 26 paginas dedicadas entre os 102 ocupantes das cinco caudas, e que o `VOZ.md` desta ilha proibe nominalmente. Site que vive de ocupar a consulta de compra nao e prospect: e CONCORRENTE, e nao linka para fora de graca. A linha fica na lista para ser reconhecida como tal, e e por isso que o teto do tipo `fazenda` e 3.

- **dominio, tipo** (busca, 2026-11-02) — consulta `marcas brasileiras bicicleta elétrica patinete elétrico fabricante nacional loja própria site` → [As 7 Melhores Marcas de Bicicleta Elétrica que Dominam o Brasil em 2026 — Blog GuiaEbike](https://guiaebike.com.br/blog/as-7-melhores-marcas-de-bicicleta-eletrica-que-dominam-o-brasil-em-2026)
- **publica_conteudo** (busca, 2026-11-02) — consulta `blog dicas autonomia bateria patinete bicicleta elétrica CNH (restrita a guiaebike.com.br e outros cinco)` → [Níveis de Assistência da E-bike: Guia Completo Para Dominar Cada Modo — Blog GuiaEbike](https://guiaebike.com.br/blog/niveis-de-assistencia-da-e-bike-guia-completo-para-dominar-cada-modo)

### `melhoresparacomprar.com.br` — Melhores Para Comprar

Publica pagina dedicada a `scooter eletrica sem CNH`, que e a consulta de 301 mil buscas/mes cujo endereco esta reservado nesta ilha. O titulo e a classificacao: `Melhor Scooter Eletrica sem CNH: Top 8 Modelos`. Entra na lista como OCUPANTE a reconhecer e nao como prospect — e o unico destes tres que disputa diretamente uma consulta que esta ilha quer, e por isso vale estar escrito em algum lugar com URL e data.

- **dominio, tipo, publica_conteudo** (busca, 2026-11-02) — consulta `patinete elétrico scooter elétrica loja brasil autopropelido sem CNH 1000W comprar site oficial marca` → [Melhor Scooter Elétrica sem CNH: Top 8 Modelos](https://melhoresparacomprar.com.br/melhor-scooter-eletrica-sem-cnh)

### `techinter.com.br` — Techinter — mobilidade elétrica

Tem secao dedicada de mobilidade eletrica e publica sobre bicicleta eletrica. Mesma classificacao e mesma razao da GuiaEbike, com a assinatura no proprio titulo da pagina de secao: `As 10 melhores bicicletas eletricas de 2026`. Concorrente pela consulta, nao prospect do widget.

- **dominio, tipo, publica_conteudo** (busca, 2026-11-02) — consulta `marcas brasileiras bicicleta elétrica patinete elétrico fabricante nacional loja própria site` → [As 10 melhores bicicletas elétricas de 2026 - Techinter](https://techinter.com.br/mobilidade-eletrica/bicicletas-eletricas/)

---

## O que esta lista NAO diz

- NAO diz que algum destes dominios nao tem calculadora. Nenhum campo `ja_tem_calculadora` e `true` nesta passada, e isso quer dizer `nao medido`, nunca `nao tem`. A busca de `calculadora autonomia bicicleta eletrica patinete km bateria ferramenta online brasil` nao devolveu uma calculadora sequer — nem brasileira nem estrangeira —, o que e consistente com o `todos falam, ninguem calcula` que o corpus de 28/10 mediu no eixo da CNH, e NAO e prova de ausencia.
- NAO diz contato de ninguem. `contato` e `null` em todas as dez linhas, com motivo escrito: o egresso nao abre o site e e no site que mora o canal. Campo vazio sem motivo e onde a proxima passada inventa um e-mail, e a secao 28 do contrato ja pagou uma vez por e-mail de pessoa de verdade escrito em repositorio.
- NAO diz a plataforma de loja de ninguem (Nuvemshop, Tray, Shopify, WooCommerce). Isso se le no HTML, e ninguem abriu o HTML.
- NAO e ordem de abordagem. A prioridade e CALCULADA dos campos medidos e ordena por quem tem interesse e tem onde por a ferramenta — nao por quem responderia. Quem abordar decide.
- NAO esgota o mercado. Sao dez dominios achados em sete consultas, e o proprio instrumento vaza: o corpus de 28/10 mediu que o eixo da autonomia devolve ~40 de ~50 ocupantes fora do Brasil. Lista maior se faz com mais consultas, nao com mais suposicao.

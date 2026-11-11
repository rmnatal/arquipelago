# LINKS DE AFILIADO PENDENTES — RODAMETRIA

> **Este arquivo só existe onde o gerador exige clique humano (seção 7 do `ARQUIPELAGO.md`).** Na Shopee o link sai pela Open API na própria coleta e esta fila NÃO é criada. No **Mercado Livre** o Gerador de links carrega reCAPTCHA e não responde a clique de script (medido em 13/09/2026), então **montar a lista é trabalho de máquina e apertar "Gerar" é trabalho do Raphael**.

## Como usar (3 passos)

1. Em `mercadolivre.com.br/afiliados/adminlabel`, crie a etiqueta **`rodametriamotoeletrica`**. A etiqueta só aceita **letra minúscula e dígito**, sem hífen, sem maiúscula, sem espaço, no máximo 30 caracteres — esta tem 22 e é o formato `<ilha><ferramenta>` da seção 7.
2. Em `mercadolivre.com.br/afiliados/linkbuilder`, escolha essa etiqueta, cole as URLs da coluna `url_produto` abaixo e aperte **Gerar**.
3. Cole cada link encurtado na coluna `url` da linha correspondente, escreva a data em `gerado_em`, e **não apague a `url_produto`** — sem ela não existe teste de vida (25.4-b).

## Consulta: `moto elétrica` — 823 mil buscas/mês

**Por que esta consulta e não outra:** é a maior das seis cabeças do nicho, a SERP tem veredito `alvo` visto com os olhos do Raphael em 27/10/2026, e `dados/consultas-de-produto.json` já escreve que **o que falta é o PRODUTO e que o caminho é o Mercado Livre** — a Shopee devolveu só três anúncios de adulto, os três com zero venda.

**Colhido no Chrome do Raphael em 2026-11-11, por volta das 20h0xZ, em `lista.mercadolivre.com.br/moto-eletrica-adulto`, lendo só os `href` que contêm `/p/MLB` — que é o degrau 2 da 25.1 (página de CATÁLOGO, nunca `produto.mercadolivre.com.br/MLB-…-_JM`).**

| # | url_produto (degrau 2, catálogo) | título colhido | preço na coleta | vendas declaradas | url (encurtado, a colar) | gerado_em |
|---|---|---|---|---|---|---|
| 1 | https://www.mercadolivre.com.br/moto-eletrica-off-road-gt600-potencia-de-7500w-pico-80kmh-preto/p/MLB78820650 | Moto Elétrica Off-road Gt600 - Potência De 7500w Pico 80km/h Preto | R$ 17.999 | **+50 vendidos** | | |
| 2 | https://www.mercadolivre.com.br/moto-eletrica-autopropelido-sem-cnh-scooter-falcon-500w-48v-15ah-bateria-de-litio-brushless-display-led-chumbo-zelt/p/MLB81237535 | Moto Elétrica Autopropelido Sem Cnh Scooter Falcon 500w 48v 15ah | R$ 10.000 | nenhuma declarada | | |
| 3 | https://www.mercadolivre.com.br/scooter-eletrica-moto-bicicleta-cor-preta-800w-aro-14-bateria-de-litio-20ah-duravel-roda-45-km-por-carga/p/MLB67977032 | Scooter Elétrica Moto Bicicleta Preta 800w Aro 14 Lítio 20Ah 45 km | R$ 5.600 | nenhuma declarada | | |
| 4 | https://www.mercadolivre.com.br/honeywhale-s150-bicicleta-eletrica-adulto-720w-100km-35kmh-48v225ah-bateria-litio/p/MLB74406653 | Honeywhale S150 Bicicleta Elétrica Adulto 720w 100km 35km/h 48v/22.5Ah | R$ 12.665 | nenhuma declarada | | |
| 5 | https://www.mercadolivre.com.br/bicicleta-eletrica-inow-v20-mini-750w-preto/p/MLB76065564 | Bicicleta Elétrica Inow V20 Mini 750w Preto | R$ 7.326 | nenhuma declarada | | |

**O QUE FOI DEIXADO DE FORA, E POR QUÊ — porque contagem sem o descarte escrito é número sem procedência (23.4):** a busca devolveu **7** páginas de catálogo e esta lista tem **5**. As duas que saíram são **MLB81237529 e MLB81237531**, que são **o MESMO anúncio da linha 2** (Scooter Falcon 500W, R$ 10.000) em entradas de catálogo diferentes. Gerar link para as três seria publicar o mesmo produto três vezes na mesma vitrine.

**O QUE ESTA LISTA NÃO DECIDE:** quem entra na vitrine. A régua de família desta consulta (`exige_todas: [moto, eletric]`, `exige_alguma: [adulto, adultos]`) e o veredito por anúncio são de `ferramentas/teste-relevancia-do-anuncio.py`, que é da Fundação. **Quatro das cinco linhas acima provavelmente NÃO passam nessa régua pelo título** — as linhas 3, 4 e 5 dizem `scooter`/`bicicleta` e não `moto`, e nenhuma das cinco diz `adulto` no título. Isto está escrito aqui de propósito: **a lista é de candidatos colhidos, não de aprovados.**

**O AVISO HONESTO, e ele muda a decisão de publicar:** das 5 ofertas distintas, **só 1 declara venda**. O piso da 30.2 é três anúncios que servem; nascer no piso com quatro ofertas sem uma venda é o mesmo risco que `dados/consultas-de-produto.json` já nomeou para a Shopee. **Se a régua reprovar e sobrarem menos de três, a consulta NÃO recebe endereço** — e isso é a 30.2 funcionando, não um bloco perdido.

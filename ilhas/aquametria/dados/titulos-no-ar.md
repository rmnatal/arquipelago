# Serie do TITULO SERVIDO NO AR — Aquametria

O `<title>` e a `<meta name="description">` que cada URL do
`wp-sitemap.xml` desta ilha SERVE, com as entidades decodificadas — que e
como a tela conta. Escreve aqui o
`ferramentas/conferir-titulo-no-ar.py --gravar`; quem confere e o mesmo
arquivo sem a opcao, e ele compara PAGINA POR PAGINA, nao pelo total.

**Secao nova vai no TOPO** (a serie cresce por cima, como
`dados/posicoes.md`, `dados/cano-de-links.md` e
`dados/deriva-do-catalogo.md`) e secao antiga NUNCA e sobrescrita: a serie
so vale porque cresce. O bloco `json` de cada secao e a declaracao que o
portao le — o primeiro do arquivo e o que manda.

**POR QUE ELA NASCEU EM 19/10/2026, dois dias antes de ser cobrada.** A
linha de 14/10 do `dados/posicoes.md` diz: *"NAO COPIEI os `<title>`
servidos para esta serie (...) A leitura de 21/10 e a primeira em que
copiar o titulo servido significa alguma coisa — e ai e OBRIGATORIO."* O
critErio de pronto da Proposta 1 e da Proposta 2 da leitura de 07/10 pede
o titulo servido no dia da medicao. Esta serie e esse titulo, **medido e
nao copiado da aba** — a leitura de 21/10 cita a secao desta data em vez
de transcrever 52 frases a mao.

Titulo que muda **nao e defeito**: leva nova, promessa nova e pagina nova
movem estas frases por desenho. O que e defeito e titulo que mudou no ar e
ninguem declarou — que e a cicatriz de 11/09/2026 desta ilha, quando 293
afirmacoes de bancada ficaram verdes com os nove titulos do ar sendo os de
antes.


## 2026-10-21 12:23Z

**52 URL(s)** do `wp-sitemap.xml`, abertas uma a uma com quebra de cache. Revisao do `/status` na medicao: **125**.

| o que | quanto |
|---|---|
| URLs sem `<title>` | **0** |
| URLs sem `<meta name="description">` | **0** |
| `<title>` com algarismo (a promessa da banda 4 a 10) | **6** |
| o `<title>` mais longo, decodificado (teto 65) | **64** |

**AS PROMESSAS QUE CHEGARAM AO AR**, com o `<title>` servido inteiro — e esta tabela e a que a leitura semanal cita:

| URL | promessa que o snippet resolve | `<title>` servido | n |
|---|---|---|---|
| `https://aquametria.com.br/calculadora-de-iluminacao/` | de 10 a 60 lm por litro | Quanta luz o seu aquário precisa? – de 10 a 60 lm por litro | 59 |
| `https://aquametria.com.br/calculadora-de-midia-filtrante/` | de 1,25 a 12,5 mL/L | Quanta mídia biológica cabe no seu filtro? – de 1,25 a 12,5 mL/L | 64 |
| `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` | de 1 a 2 W por litro | Quantos watts de aquecedor você precisa? – de 1 a 2 W por litro | 63 |
| `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` | de 1,76 a 10 renovações/h | Qual filtro dá conta do seu aquário? – de 1,76 a 10 renovações/h | 64 |
| `https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/` | de 40,5 a 54 litros | Quantos litros para um betta? – de 40,5 a 54 litros | 51 |

```json
{
  "medido_em": "2026-10-21 12:23Z",
  "paginas": {
    "https://aquametria.com.br/": {
      "descricao": "Quantos litros tem o seu aquário? E quantos watts de aquecedor, qual filtro, quanta luz? As contas do seu aquário, com a fonte de cada número.",
      "descricao_n": 142,
      "digito": false,
      "n": 37,
      "titulo": "Aquametria – as contas do seu aquário"
    },
    "https://aquametria.com.br/2026/09/08/quanta-midia-biologica-o-aquario-precisa/": {
      "descricao": "Seachem pede 1,25 mL de mídia por litro; Ocean Tech pede 12,5. Dez vezes de diferença para o mesmo trabalho — fomos às declarações originais.",
      "descricao_n": 141,
      "digito": false,
      "n": 56,
      "titulo": "Cada marca pede uma dose diferente de mídia – Aquametria"
    },
    "https://aquametria.com.br/2026/09/08/quantos-lumens-por-litro-aquario-plantado/": {
      "descricao": "Três fontes brasileiras chamam a mesma faixa de lúmens por litro com o dobro do número. De onde vem a regra e por que o lúmen é a unidade errada.",
      "descricao_n": 145,
      "digito": false,
      "n": 64,
      "titulo": "Quantos lúmens por litro o aquário plantado precisa – Aquametria"
    },
    "https://aquametria.com.br/2026/09/08/quantos-watts-de-aquecedor-para-aquario/": {
      "descricao": "O 1 W por litro não veio de um cálculo, veio da prateleira. De onde a regra saiu, quando ela acerta por acidente e o que muda ao medir o cômodo.",
      "descricao_n": 144,
      "digito": true,
      "n": 59,
      "titulo": "Por que o 1 W por litro erra para o mesmo lado – Aquametria"
    },
    "https://aquametria.com.br/calculadora-de-iluminacao/": {
      "descricao": "Quantos lúmens o seu aquário plantado precisa? De 10 a 60 lm por litro pelas três leituras brasileiras, cada faixa com o nome de quem a declara.",
      "descricao_n": 144,
      "digito": true,
      "n": 59,
      "titulo": "Quanta luz o seu aquário precisa? – de 10 a 60 lm por litro"
    },
    "https://aquametria.com.br/calculadora-de-litragem/": {
      "descricao": "Quantos litros tem o seu aquário? Informe as medidas em centímetros e receba os três volumes: o bruto da etiqueta, o interno e a água real.",
      "descricao_n": 139,
      "digito": false,
      "n": 46,
      "titulo": "Quantos litros tem o seu aquário? – Aquametria"
    },
    "https://aquametria.com.br/calculadora-de-midia-filtrante/": {
      "descricao": "Quanta mídia filtrante o seu aquário pede, em mililitros? De 1,25 a 12,5 mL por litro: é o que quatro fabricantes declaram, cada um com o nome.",
      "descricao_n": 143,
      "digito": true,
      "n": 64,
      "titulo": "Quanta mídia biológica cabe no seu filtro? – de 1,25 a 12,5 mL/L"
    },
    "https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/": {
      "descricao": "Quantos watts de aquecedor o seu aquário pede? De 1 a 2 W por litro, conforme a fonte e a diferença de temperatura — e a conta sai pelo seu cômodo.",
      "descricao_n": 147,
      "digito": true,
      "n": 63,
      "titulo": "Quantos watts de aquecedor você precisa? – de 1 a 2 W por litro"
    },
    "https://aquametria.com.br/calculadora-de-vazao-do-filtro/": {
      "descricao": "Qual a vazão de filtro para o seu aquário, em L/h? De 1,76 renovação por hora, que a Eheim declara, a 10, da regra de bolso brasileira.",
      "descricao_n": 135,
      "digito": true,
      "n": 64,
      "titulo": "Qual filtro dá conta do seu aquário? – de 1,76 a 10 renovações/h"
    },
    "https://aquametria.com.br/calculadoras/": {
      "descricao": "As contas do seu aquário em um lugar só: litros, vazão do filtro, watts do aquecedor, mídia filtrante e luz — cada uma com a fonte do número.",
      "descricao_n": 141,
      "digito": false,
      "n": 25,
      "titulo": "Calculadoras – Aquametria"
    },
    "https://aquametria.com.br/divulgacao-de-afiliados/": {
      "descricao": "A Aquametria recebe comissão por alguns links de loja. O que isso muda na ordem dos produtos recomendados: nada. O critério inteiro, por escrito.",
      "descricao_n": 145,
      "digito": false,
      "n": 45,
      "titulo": "Como a Aquametria ganha dinheiro – Aquametria"
    },
    "https://aquametria.com.br/metodologia/": {
      "descricao": "De onde sai cada número da Aquametria: o manual do fabricante, a data em que foi conferido e a faixa inteira quando as fontes discordam.",
      "descricao_n": 136,
      "digito": false,
      "n": 33,
      "titulo": "Como a gente calcula – Aquametria"
    },
    "https://aquametria.com.br/peixes/": {
      "descricao": "Quanto espaço cada peixe pede, em centímetros de chão e não em litros: o mínimo declarado por fonte com nome e data, espécie por espécie.",
      "descricao_n": 137,
      "digito": false,
      "n": 42,
      "titulo": "Quanto espaço cada peixe pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/": {
      "descricao": "Acará-bandeira, oscar e acará-disco lado a lado: como cada um vive, a frente mínima declarada por fonte com nome e data, e a faixa térmica.",
      "descricao_n": 139,
      "digito": false,
      "n": 60,
      "titulo": "Acarás: quantos litros, do solitário ao cardume – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-bandeira/": {
      "descricao": "Quantos litros para um grupo de acará-bandeira? A base e a altura mínima que a fonte declara, a conta pelas duas réguas de lotação e as irmãs.",
      "descricao_n": 142,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um grupo de acará-bandeira? – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-disco/": {
      "descricao": "Quantos litros para um cardume de acará-disco? A frente que a fonte declara para o grupo, o que ela não cobre, e as duas réguas de lotação.",
      "descricao_n": 139,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de acará-disco? – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-oscar/": {
      "descricao": "Quantos litros para um oscar? A base que a fonte declara para um adulto, para quem ela foi declarada, e a conta pelas duas réguas de lotação.",
      "descricao_n": 141,
      "digito": false,
      "n": 42,
      "titulo": "Quantos litros para um oscar? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/": {
      "descricao": "Barbo sumatra, rosado e cereja lado a lado: a frente mínima declarada por fonte com nome e data, o cardume de cada um e a faixa térmica.",
      "descricao_n": 136,
      "digito": false,
      "n": 57,
      "titulo": "Barbos: quantos litros, e quem divide a água – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-cereja/": {
      "descricao": "Quantos litros para um cardume de barbo cereja? A base de 60 cm que a fonte declara, o grupo de 6 a 10 e a conta pelas duas réguas.",
      "descricao_n": 131,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um cardume de barbo cereja? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-rosado/": {
      "descricao": "Quantos litros para um cardume de barbo rosado? As duas frentes que as fontes declaram, a faixa subtropical dele e as réguas de lotação.",
      "descricao_n": 136,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um cardume de barbo rosado? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-sumatra/": {
      "descricao": "Quantos litros para um cardume de barbo sumatra? A base de 80 cm que a fonte declara, as duas réguas de lotação e a recusa que ela escreveu.",
      "descricao_n": 140,
      "digito": false,
      "n": 61,
      "titulo": "Quantos litros para um cardume de barbo sumatra? – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/": {
      "descricao": "Betta, colisa-anão e gurami mel não vivem do mesmo jeito: o arranjo que a fonte declara ao lado da frente mínima de cada um, com nome e data.",
      "descricao_n": 141,
      "digito": false,
      "n": 59,
      "titulo": "Bettas e gouramis: quantos litros cada um pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/": {
      "descricao": "Quantos litros para um betta? De 40,5 a 54 litros, que é o que a base de 45 × 30 cm declarada pelo Seriously Fish dá — e o pote de 2 L não é aquário.",
      "descricao_n": 149,
      "digito": true,
      "n": 51,
      "titulo": "Quantos litros para um betta? – de 40,5 a 54 litros"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-colisa-anao/": {
      "descricao": "Quantos litros para um casal de colisa-anão? A base que a ficha da espécie declara, com nome e data, e os quatro números que a busca publica.",
      "descricao_n": 141,
      "digito": false,
      "n": 57,
      "titulo": "Quantos litros para um casal de colisa-anão? – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-gurami-mel/": {
      "descricao": "Quantos litros para um grupo de gurami mel? A base e o grupo mínimo de 4 a 6 que a ficha da espécie declara, com nome da fonte e data.",
      "descricao_n": 134,
      "digito": false,
      "n": 56,
      "titulo": "Quantos litros para um grupo de gurami mel? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/": {
      "descricao": "Quantos litros para ciclídeo anão? Os ciclídeos anões pedem aquário pelo arranjo, não pelo tamanho: dois do mesmo porte pedem 60 cm, o terceiro 120.",
      "descricao_n": 148,
      "digito": false,
      "n": 63,
      "titulo": "Ciclídeos anões: quantos litros para ciclídeo anão – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-apistogramma-agassizi/": {
      "descricao": "Quantos litros para apistogramma agassizi? Os 60 cm que as duas fontes declaram, uma para casal e outra para harém, e quantos cabem no seu aquário.",
      "descricao_n": 147,
      "digito": false,
      "n": 55,
      "titulo": "Quantos litros para apistogramma agassizi? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-papilocromis/": {
      "descricao": "Quantos litros para um grupo de papilocromis? Os 120 cm que a fonte declara para o grupo de 6 a 8, e quantos cabem no aquário que você já tem.",
      "descricao_n": 142,
      "digito": false,
      "n": 58,
      "titulo": "Quantos litros para um grupo de papilocromis? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-ramirezi/": {
      "descricao": "Quantos litros para um casal de ramirezi? A frente mínima que a fonte declara, a conta pelas duas réguas de lotação e quantos cabem no seu aquário.",
      "descricao_n": 147,
      "digito": false,
      "n": 54,
      "titulo": "Quantos litros para um casal de ramirezi? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/": {
      "descricao": "Coridora se dimensiona pelo chão, não pelo litro: porte, cardume mínimo e base mínima das quatro espécies, com a fonte de cada linha.",
      "descricao_n": 133,
      "digito": false,
      "n": 48,
      "titulo": "Coridoras: quanto chão o grupo pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-bronze/": {
      "descricao": "Quantos litros para um cardume de coridora bronze? A base de 80 x 30 cm que a fonte declara, com nome e data, e a conta pelas duas réguas.",
      "descricao_n": 138,
      "digito": false,
      "n": 63,
      "titulo": "Quantos litros para um cardume de coridora bronze? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-panda/": {
      "descricao": "Quantos litros para um cardume de coridora panda? A base de 45 x 30 cm que a fonte declara — a menor do banco — e a conta em litros.",
      "descricao_n": 132,
      "digito": false,
      "n": 62,
      "titulo": "Quantos litros para um cardume de coridora panda? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-pimenta/": {
      "descricao": "Quantos litros para um cardume de coridora pimenta? A base mínima declarada por duas fontes que discordam, com os dois números na tela.",
      "descricao_n": 135,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de coridora pimenta? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-sterbai/": {
      "descricao": "Quantos litros para um cardume de coridora sterbai? A base e o cardume mínimo que a ficha da espécie declara, com nome da fonte e data.",
      "descricao_n": 135,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de coridora sterbai? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/": {
      "descricao": "Três peixes que não passam de 5 cm e frentes mínimas de 60 e 90 cm: a tabela de porte, cardume e base declarada, com a fonte de cada linha.",
      "descricao_n": 139,
      "digito": false,
      "n": 61,
      "titulo": "Danios e rasboras: quantos litros o cardume pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-paulistinha/": {
      "descricao": "Quantos litros para um cardume de paulistinha? Os 90 cm de base que a fonte declara, o outro número do conflito e quantos cabem no seu aquário.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de paulistinha? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-rasbora-arlequim/": {
      "descricao": "Quantos litros para um cardume de rasbora arlequim? A base de 60 cm que a fonte declara, o cardume mínimo dela e quantos cabem no seu aquário.",
      "descricao_n": 142,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de rasbora arlequim? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-tanictis/": {
      "descricao": "Quantos litros para um cardume de tanictis? As duas fontes declaram cardume de 5 e de 10 na mesma frente de 60 cm: a página publica as duas.",
      "descricao_n": 140,
      "digito": false,
      "n": 56,
      "titulo": "Quantos litros para um cardume de tanictis? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/": {
      "descricao": "Porte, cardume mínimo e frente mínima dos tetras lado a lado, com a fonte de cada linha — e a conta em litros pelas duas réguas brasileiras.",
      "descricao_n": 140,
      "digito": false,
      "n": 50,
      "titulo": "Tetras: quantos litros o cardume pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-mato-grosso/": {
      "descricao": "Quantos litros para um cardume de mato-grosso? As duas fontes discordam da frente mínima, e esta página publica as duas com o nome de cada uma.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de mato-grosso? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-rodostomo/": {
      "descricao": "Quantos litros para um cardume de rodóstomo? A fonte declara 90 cm de comprimento e nenhuma largura — e esta página diz isso em vez de inventar.",
      "descricao_n": 144,
      "digito": false,
      "n": 57,
      "titulo": "Quantos litros para um cardume de rodóstomo? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-brilhante/": {
      "descricao": "Quantos litros para um cardume de tetra-brilhante? A base declarada, a divergência de um exemplar no cardume e a conta pelas duas réguas.",
      "descricao_n": 137,
      "digito": false,
      "n": 63,
      "titulo": "Quantos litros para um cardume de tetra-brilhante? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-cardinal/": {
      "descricao": "Quantos litros para um cardume de neon cardinal? A base declarada pela fonte, o cardume mínimo de 8 e a conta em litros pelas duas réguas.",
      "descricao_n": 138,
      "digito": false,
      "n": 61,
      "titulo": "Quantos litros para um cardume de neon cardinal? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-ember/": {
      "descricao": "Quantos litros para um cardume de tetra ember? A base de 45 × 30 cm que a fonte declara, o cardume mínimo de 8 e a conta pelas duas réguas.",
      "descricao_n": 139,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de tetra ember? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-negro/": {
      "descricao": "Quantos litros para um cardume de tetra-negro? Cardume mínimo de 5, base declarada de 75 × 30 cm e a divergência de 15 cm entre as duas fontes.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de tetra-negro? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-neon/": {
      "descricao": "Quantos litros para um cardume de tetra neon? A base que a fonte declara, a conta pelas duas réguas de lotação e quantos cabem no seu aquário.",
      "descricao_n": 142,
      "digito": false,
      "n": 58,
      "titulo": "Quantos litros para um cardume de tetra neon? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/": {
      "descricao": "Platy, peixe-espada e plati variatus vivem em harém e pedem frentes que diferem em duas vezes: a base mínima de cada um, com nome da fonte e data.",
      "descricao_n": 146,
      "digito": false,
      "n": 51,
      "titulo": "Vivíparos: quantos litros o harém pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-peixe-espada/": {
      "descricao": "Quantos litros para um peixe-espada? Os 120 × 30 cm de base que a ficha da espécie declara, com nome da fonte e data: o dobro da frente do platy.",
      "descricao_n": 145,
      "digito": false,
      "n": 49,
      "titulo": "Quantos litros para um peixe-espada? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-plati-variatus/": {
      "descricao": "Quantos litros para plati variatus? Os 60 cm de frente que a ficha da espécie declara, com nome e data, e o que separa esta espécie do platy comum.",
      "descricao_n": 147,
      "digito": false,
      "n": 48,
      "titulo": "Quantos litros para plati variatus? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-platy/": {
      "descricao": "Quantos litros para platy? Os 60 cm de frente que a ficha da espécie declara, com nome da fonte e data — e por que o litro sozinho engana aqui.",
      "descricao_n": 143,
      "digito": false,
      "n": 39,
      "titulo": "Quantos litros para platy? – Aquametria"
    },
    "https://aquametria.com.br/politica-de-privacidade/": {
      "descricao": "Sem cadastro, sem formulário e sem cookie vindo do servidor. Os seis endereços que o seu navegador procura fora daqui, medidos página por página.",
      "descricao_n": 145,
      "digito": false,
      "n": 44,
      "titulo": "O que este site sabe sobre você – Aquametria"
    },
    "https://aquametria.com.br/sobre/": {
      "descricao": "Quem publica a Aquametria e por quê: um site de aquarismo que mostra a conta, cita o manual do fabricante e recusa número sem fonte declarada.",
      "descricao_n": 142,
      "digito": false,
      "n": 18,
      "titulo": "Sobre – Aquametria"
    }
  },
  "promessas": {
    "https://aquametria.com.br/calculadora-de-iluminacao/": "de 10 a 60 lm por litro",
    "https://aquametria.com.br/calculadora-de-midia-filtrante/": "de 1,25 a 12,5 mL/L",
    "https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/": "de 1 a 2 W por litro",
    "https://aquametria.com.br/calculadora-de-vazao-do-filtro/": "de 1,76 a 10 renovações/h",
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/": "de 40,5 a 54 litros"
  },
  "revisao_do_status": "125",
  "site": "https://aquametria.com.br",
  "teto": 65,
  "totais": {
    "com_digito": 6,
    "paginas": 52,
    "sem_descricao": 0,
    "sem_titulo": 0,
    "titulo_mais_longo": 64
  }
}
```

## 2026-10-19 13:46Z

**52 URL(s)** do `wp-sitemap.xml`, abertas uma a uma com quebra de cache. Revisao do `/status` na medicao: **122**.

| o que | quanto |
|---|---|
| URLs sem `<title>` | **0** |
| URLs sem `<meta name="description">` | **0** |
| `<title>` com algarismo (a promessa da banda 4 a 10) | **6** |
| o `<title>` mais longo, decodificado (teto 65) | **64** |

**AS PROMESSAS QUE CHEGARAM AO AR**, com o `<title>` servido inteiro — e esta tabela e a que a leitura semanal cita:

| URL | promessa que o snippet resolve | `<title>` servido | n |
|---|---|---|---|
| `https://aquametria.com.br/calculadora-de-iluminacao/` | de 10 a 60 lm por litro | Quanta luz o seu aquário precisa? – de 10 a 60 lm por litro | 59 |
| `https://aquametria.com.br/calculadora-de-midia-filtrante/` | de 1,25 a 12,5 mL/L | Quanta mídia biológica cabe no seu filtro? – de 1,25 a 12,5 mL/L | 64 |
| `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` | de 1 a 2 W por litro | Quantos watts de aquecedor você precisa? – de 1 a 2 W por litro | 63 |
| `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` | de 1,76 a 10 renovações/h | Qual filtro dá conta do seu aquário? – de 1,76 a 10 renovações/h | 64 |
| `https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/` | de 40,5 a 54 litros | Quantos litros para um betta? – de 40,5 a 54 litros | 51 |

```json
{
  "medido_em": "2026-10-19 13:46Z",
  "paginas": {
    "https://aquametria.com.br/": {
      "descricao": "Quantos litros tem o seu aquário? E quantos watts de aquecedor, qual filtro, quanta luz? As contas do seu aquário, com a fonte de cada número.",
      "descricao_n": 142,
      "digito": false,
      "n": 37,
      "titulo": "Aquametria – as contas do seu aquário"
    },
    "https://aquametria.com.br/2026/09/08/quanta-midia-biologica-o-aquario-precisa/": {
      "descricao": "Seachem pede 1,25 mL de mídia por litro; Ocean Tech pede 12,5. Dez vezes de diferença para o mesmo trabalho — fomos às declarações originais.",
      "descricao_n": 141,
      "digito": false,
      "n": 56,
      "titulo": "Cada marca pede uma dose diferente de mídia – Aquametria"
    },
    "https://aquametria.com.br/2026/09/08/quantos-lumens-por-litro-aquario-plantado/": {
      "descricao": "Três fontes brasileiras chamam a mesma faixa de lúmens por litro com o dobro do número. De onde vem a regra e por que o lúmen é a unidade errada.",
      "descricao_n": 145,
      "digito": false,
      "n": 64,
      "titulo": "Quantos lúmens por litro o aquário plantado precisa – Aquametria"
    },
    "https://aquametria.com.br/2026/09/08/quantos-watts-de-aquecedor-para-aquario/": {
      "descricao": "O 1 W por litro não veio de um cálculo, veio da prateleira. De onde a regra saiu, quando ela acerta por acidente e o que muda ao medir o cômodo.",
      "descricao_n": 144,
      "digito": true,
      "n": 59,
      "titulo": "Por que o 1 W por litro erra para o mesmo lado – Aquametria"
    },
    "https://aquametria.com.br/calculadora-de-iluminacao/": {
      "descricao": "Quantos lúmens o seu aquário plantado precisa? De 10 a 60 lm por litro pelas três leituras brasileiras, cada faixa com o nome de quem a declara.",
      "descricao_n": 144,
      "digito": true,
      "n": 59,
      "titulo": "Quanta luz o seu aquário precisa? – de 10 a 60 lm por litro"
    },
    "https://aquametria.com.br/calculadora-de-litragem/": {
      "descricao": "Quantos litros tem o seu aquário? Informe as medidas em centímetros e receba os três volumes: o bruto da etiqueta, o interno e a água real.",
      "descricao_n": 139,
      "digito": false,
      "n": 46,
      "titulo": "Quantos litros tem o seu aquário? – Aquametria"
    },
    "https://aquametria.com.br/calculadora-de-midia-filtrante/": {
      "descricao": "Quanta mídia filtrante o seu aquário pede, em mililitros? De 1,25 a 12,5 mL por litro: é o que quatro fabricantes declaram, cada um com o nome.",
      "descricao_n": 143,
      "digito": true,
      "n": 64,
      "titulo": "Quanta mídia biológica cabe no seu filtro? – de 1,25 a 12,5 mL/L"
    },
    "https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/": {
      "descricao": "Quantos watts de aquecedor o seu aquário pede? De 1 a 2 W por litro, conforme a fonte e a diferença de temperatura — e a conta sai pelo seu cômodo.",
      "descricao_n": 147,
      "digito": true,
      "n": 63,
      "titulo": "Quantos watts de aquecedor você precisa? – de 1 a 2 W por litro"
    },
    "https://aquametria.com.br/calculadora-de-vazao-do-filtro/": {
      "descricao": "Qual a vazão de filtro para o seu aquário, em L/h? De 1,76 renovação por hora, que a Eheim declara, a 10, da regra de bolso brasileira.",
      "descricao_n": 135,
      "digito": true,
      "n": 64,
      "titulo": "Qual filtro dá conta do seu aquário? – de 1,76 a 10 renovações/h"
    },
    "https://aquametria.com.br/calculadoras/": {
      "descricao": "As contas do seu aquário em um lugar só: litros, vazão do filtro, watts do aquecedor, mídia filtrante e luz — cada uma com a fonte do número.",
      "descricao_n": 141,
      "digito": false,
      "n": 25,
      "titulo": "Calculadoras – Aquametria"
    },
    "https://aquametria.com.br/divulgacao-de-afiliados/": {
      "descricao": "A Aquametria recebe comissão por alguns links de loja. O que isso muda na ordem dos produtos recomendados: nada. O critério inteiro, por escrito.",
      "descricao_n": 145,
      "digito": false,
      "n": 45,
      "titulo": "Como a Aquametria ganha dinheiro – Aquametria"
    },
    "https://aquametria.com.br/metodologia/": {
      "descricao": "De onde sai cada número da Aquametria: o manual do fabricante, a data em que foi conferido e a faixa inteira quando as fontes discordam.",
      "descricao_n": 136,
      "digito": false,
      "n": 33,
      "titulo": "Como a gente calcula – Aquametria"
    },
    "https://aquametria.com.br/peixes/": {
      "descricao": "Quanto espaço cada peixe pede, em centímetros de chão e não em litros: o mínimo declarado por fonte com nome e data, espécie por espécie.",
      "descricao_n": 137,
      "digito": false,
      "n": 42,
      "titulo": "Quanto espaço cada peixe pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/": {
      "descricao": "Acará-bandeira, oscar e acará-disco lado a lado: como cada um vive, a frente mínima declarada por fonte com nome e data, e a faixa térmica.",
      "descricao_n": 139,
      "digito": false,
      "n": 60,
      "titulo": "Acarás: quantos litros, do solitário ao cardume – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-bandeira/": {
      "descricao": "Quantos litros para um grupo de acará-bandeira? A base e a altura mínima que a fonte declara, a conta pelas duas réguas de lotação e as irmãs.",
      "descricao_n": 142,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um grupo de acará-bandeira? – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-disco/": {
      "descricao": "Quantos litros para um cardume de acará-disco? A frente que a fonte declara para o grupo, o que ela não cobre, e as duas réguas de lotação.",
      "descricao_n": 139,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de acará-disco? – Aquametria"
    },
    "https://aquametria.com.br/peixes/acaras/quantos-litros-para-oscar/": {
      "descricao": "Quantos litros para um oscar? A base que a fonte declara para um adulto, para quem ela foi declarada, e a conta pelas duas réguas de lotação.",
      "descricao_n": 141,
      "digito": false,
      "n": 42,
      "titulo": "Quantos litros para um oscar? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/": {
      "descricao": "Barbo sumatra, rosado e cereja lado a lado: a frente mínima declarada por fonte com nome e data, o cardume de cada um e a faixa térmica.",
      "descricao_n": 136,
      "digito": false,
      "n": 57,
      "titulo": "Barbos: quantos litros, e quem divide a água – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-cereja/": {
      "descricao": "Quantos litros para um cardume de barbo cereja? A base de 60 cm que a fonte declara, o grupo de 6 a 10 e a conta pelas duas réguas.",
      "descricao_n": 131,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um cardume de barbo cereja? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-rosado/": {
      "descricao": "Quantos litros para um cardume de barbo rosado? As duas frentes que as fontes declaram, a faixa subtropical dele e as réguas de lotação.",
      "descricao_n": 136,
      "digito": false,
      "n": 60,
      "titulo": "Quantos litros para um cardume de barbo rosado? – Aquametria"
    },
    "https://aquametria.com.br/peixes/barbos/quantos-litros-para-barbo-sumatra/": {
      "descricao": "Quantos litros para um cardume de barbo sumatra? A base de 80 cm que a fonte declara, as duas réguas de lotação e a recusa que ela escreveu.",
      "descricao_n": 140,
      "digito": false,
      "n": 61,
      "titulo": "Quantos litros para um cardume de barbo sumatra? – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/": {
      "descricao": "Betta, colisa-anão e gurami mel não vivem do mesmo jeito: o arranjo que a fonte declara ao lado da frente mínima de cada um, com nome e data.",
      "descricao_n": 141,
      "digito": false,
      "n": 59,
      "titulo": "Bettas e gouramis: quantos litros cada um pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/": {
      "descricao": "Quantos litros para um betta? De 40,5 a 54 litros, que é o que a base de 45 × 30 cm declarada pelo Seriously Fish dá — e o pote de 2 L não é aquário.",
      "descricao_n": 149,
      "digito": true,
      "n": 51,
      "titulo": "Quantos litros para um betta? – de 40,5 a 54 litros"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-colisa-anao/": {
      "descricao": "Quantos litros para um casal de colisa-anão? A base que a ficha da espécie declara, com nome e data, e os quatro números que a busca publica.",
      "descricao_n": 141,
      "digito": false,
      "n": 57,
      "titulo": "Quantos litros para um casal de colisa-anão? – Aquametria"
    },
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-gurami-mel/": {
      "descricao": "Quantos litros para um grupo de gurami mel? A base e o grupo mínimo de 4 a 6 que a ficha da espécie declara, com nome da fonte e data.",
      "descricao_n": 134,
      "digito": false,
      "n": 56,
      "titulo": "Quantos litros para um grupo de gurami mel? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/": {
      "descricao": "Quantos litros para ciclídeo anão? Os ciclídeos anões pedem aquário pelo arranjo, não pelo tamanho: dois do mesmo porte pedem 60 cm, o terceiro 120.",
      "descricao_n": 148,
      "digito": false,
      "n": 63,
      "titulo": "Ciclídeos anões: quantos litros para ciclídeo anão – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-apistogramma-agassizi/": {
      "descricao": "Quantos litros para apistogramma agassizi? Os 60 cm que as duas fontes declaram, uma para casal e outra para harém, e quantos cabem no seu aquário.",
      "descricao_n": 147,
      "digito": false,
      "n": 55,
      "titulo": "Quantos litros para apistogramma agassizi? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-papilocromis/": {
      "descricao": "Quantos litros para um grupo de papilocromis? Os 120 cm que a fonte declara para o grupo de 6 a 8, e quantos cabem no aquário que você já tem.",
      "descricao_n": 142,
      "digito": false,
      "n": 58,
      "titulo": "Quantos litros para um grupo de papilocromis? – Aquametria"
    },
    "https://aquametria.com.br/peixes/ciclideos-anoes/quantos-litros-para-ramirezi/": {
      "descricao": "Quantos litros para um casal de ramirezi? A frente mínima que a fonte declara, a conta pelas duas réguas de lotação e quantos cabem no seu aquário.",
      "descricao_n": 147,
      "digito": false,
      "n": 54,
      "titulo": "Quantos litros para um casal de ramirezi? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/": {
      "descricao": "Coridora se dimensiona pelo chão, não pelo litro: porte, cardume mínimo e base mínima das quatro espécies, com a fonte de cada linha.",
      "descricao_n": 133,
      "digito": false,
      "n": 48,
      "titulo": "Coridoras: quanto chão o grupo pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-bronze/": {
      "descricao": "Quantos litros para um cardume de coridora bronze? A base de 80 x 30 cm que a fonte declara, com nome e data, e a conta pelas duas réguas.",
      "descricao_n": 138,
      "digito": false,
      "n": 63,
      "titulo": "Quantos litros para um cardume de coridora bronze? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-panda/": {
      "descricao": "Quantos litros para um cardume de coridora panda? A base de 45 x 30 cm que a fonte declara — a menor do banco — e a conta em litros.",
      "descricao_n": 132,
      "digito": false,
      "n": 62,
      "titulo": "Quantos litros para um cardume de coridora panda? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-pimenta/": {
      "descricao": "Quantos litros para um cardume de coridora pimenta? A base mínima declarada por duas fontes que discordam, com os dois números na tela.",
      "descricao_n": 135,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de coridora pimenta? – Aquametria"
    },
    "https://aquametria.com.br/peixes/corydoras/quantos-litros-para-coridora-sterbai/": {
      "descricao": "Quantos litros para um cardume de coridora sterbai? A base e o cardume mínimo que a ficha da espécie declara, com nome da fonte e data.",
      "descricao_n": 135,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de coridora sterbai? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/": {
      "descricao": "Três peixes que não passam de 5 cm e frentes mínimas de 60 e 90 cm: a tabela de porte, cardume e base declarada, com a fonte de cada linha.",
      "descricao_n": 139,
      "digito": false,
      "n": 61,
      "titulo": "Danios e rasboras: quantos litros o cardume pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-paulistinha/": {
      "descricao": "Quantos litros para um cardume de paulistinha? Os 90 cm de base que a fonte declara, o outro número do conflito e quantos cabem no seu aquário.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de paulistinha? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-rasbora-arlequim/": {
      "descricao": "Quantos litros para um cardume de rasbora arlequim? A base de 60 cm que a fonte declara, o cardume mínimo dela e quantos cabem no seu aquário.",
      "descricao_n": 142,
      "digito": false,
      "n": 64,
      "titulo": "Quantos litros para um cardume de rasbora arlequim? – Aquametria"
    },
    "https://aquametria.com.br/peixes/danios-e-rasboras/quantos-litros-para-tanictis/": {
      "descricao": "Quantos litros para um cardume de tanictis? As duas fontes declaram cardume de 5 e de 10 na mesma frente de 60 cm: a página publica as duas.",
      "descricao_n": 140,
      "digito": false,
      "n": 56,
      "titulo": "Quantos litros para um cardume de tanictis? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/": {
      "descricao": "Porte, cardume mínimo e frente mínima dos tetras lado a lado, com a fonte de cada linha — e a conta em litros pelas duas réguas brasileiras.",
      "descricao_n": 140,
      "digito": false,
      "n": 50,
      "titulo": "Tetras: quantos litros o cardume pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-mato-grosso/": {
      "descricao": "Quantos litros para um cardume de mato-grosso? As duas fontes discordam da frente mínima, e esta página publica as duas com o nome de cada uma.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de mato-grosso? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-rodostomo/": {
      "descricao": "Quantos litros para um cardume de rodóstomo? A fonte declara 90 cm de comprimento e nenhuma largura — e esta página diz isso em vez de inventar.",
      "descricao_n": 144,
      "digito": false,
      "n": 57,
      "titulo": "Quantos litros para um cardume de rodóstomo? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-brilhante/": {
      "descricao": "Quantos litros para um cardume de tetra-brilhante? A base declarada, a divergência de um exemplar no cardume e a conta pelas duas réguas.",
      "descricao_n": 137,
      "digito": false,
      "n": 63,
      "titulo": "Quantos litros para um cardume de tetra-brilhante? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-cardinal/": {
      "descricao": "Quantos litros para um cardume de neon cardinal? A base declarada pela fonte, o cardume mínimo de 8 e a conta em litros pelas duas réguas.",
      "descricao_n": 138,
      "digito": false,
      "n": 61,
      "titulo": "Quantos litros para um cardume de neon cardinal? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-ember/": {
      "descricao": "Quantos litros para um cardume de tetra ember? A base de 45 × 30 cm que a fonte declara, o cardume mínimo de 8 e a conta pelas duas réguas.",
      "descricao_n": 139,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de tetra ember? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-negro/": {
      "descricao": "Quantos litros para um cardume de tetra-negro? Cardume mínimo de 5, base declarada de 75 × 30 cm e a divergência de 15 cm entre as duas fontes.",
      "descricao_n": 143,
      "digito": false,
      "n": 59,
      "titulo": "Quantos litros para um cardume de tetra-negro? – Aquametria"
    },
    "https://aquametria.com.br/peixes/tetras/quantos-litros-para-tetra-neon/": {
      "descricao": "Quantos litros para um cardume de tetra neon? A base que a fonte declara, a conta pelas duas réguas de lotação e quantos cabem no seu aquário.",
      "descricao_n": 142,
      "digito": false,
      "n": 58,
      "titulo": "Quantos litros para um cardume de tetra neon? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/": {
      "descricao": "Platy, peixe-espada e plati variatus vivem em harém e pedem frentes que diferem em duas vezes: a base mínima de cada um, com nome da fonte e data.",
      "descricao_n": 146,
      "digito": false,
      "n": 51,
      "titulo": "Vivíparos: quantos litros o harém pede – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-peixe-espada/": {
      "descricao": "Quantos litros para um peixe-espada? Os 120 × 30 cm de base que a ficha da espécie declara, com nome da fonte e data: o dobro da frente do platy.",
      "descricao_n": 145,
      "digito": false,
      "n": 49,
      "titulo": "Quantos litros para um peixe-espada? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-plati-variatus/": {
      "descricao": "Quantos litros para plati variatus? Os 60 cm de frente que a ficha da espécie declara, com nome e data, e o que separa esta espécie do platy comum.",
      "descricao_n": 147,
      "digito": false,
      "n": 48,
      "titulo": "Quantos litros para plati variatus? – Aquametria"
    },
    "https://aquametria.com.br/peixes/vivaparos/quantos-litros-para-platy/": {
      "descricao": "Quantos litros para platy? Os 60 cm de frente que a ficha da espécie declara, com nome da fonte e data — e por que o litro sozinho engana aqui.",
      "descricao_n": 143,
      "digito": false,
      "n": 39,
      "titulo": "Quantos litros para platy? – Aquametria"
    },
    "https://aquametria.com.br/politica-de-privacidade/": {
      "descricao": "Sem cadastro, sem formulário e sem cookie vindo do servidor. Os seis endereços que o seu navegador procura fora daqui, medidos página por página.",
      "descricao_n": 145,
      "digito": false,
      "n": 44,
      "titulo": "O que este site sabe sobre você – Aquametria"
    },
    "https://aquametria.com.br/sobre/": {
      "descricao": "Quem publica a Aquametria e por quê: um site de aquarismo que mostra a conta, cita o manual do fabricante e recusa número sem fonte declarada.",
      "descricao_n": 142,
      "digito": false,
      "n": 18,
      "titulo": "Sobre – Aquametria"
    }
  },
  "promessas": {
    "https://aquametria.com.br/calculadora-de-iluminacao/": "de 10 a 60 lm por litro",
    "https://aquametria.com.br/calculadora-de-midia-filtrante/": "de 1,25 a 12,5 mL/L",
    "https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/": "de 1 a 2 W por litro",
    "https://aquametria.com.br/calculadora-de-vazao-do-filtro/": "de 1,76 a 10 renovações/h",
    "https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/": "de 40,5 a 54 litros"
  },
  "revisao_do_status": "122",
  "site": "https://aquametria.com.br",
  "teto": 65,
  "totais": {
    "com_digito": 6,
    "paginas": 52,
    "sem_descricao": 0,
    "sem_titulo": 0,
    "titulo_mais_longo": 64
  }
}
```


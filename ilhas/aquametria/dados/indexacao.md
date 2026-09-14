# Série de indexação — Aquametria

Uma linha por leitura semanal. **Nunca sobrescrever linha antiga**: a série só vale porque cresce. Fonte: Search Console (propriedade de prefixo `https://aquametria.com.br/`) e `site:` quando o relatório de Páginas não abrir. Regra da rampa na seção 9 e na seção 14.6 do `ARQUIPELAGO.md`.

| data | URLs no sitemap | indexadas | % | impressões 28d | cliques 28d | posição média | decisão da rampa | observação |
|---|---|---|---|---|---|---|---|---|
| 2026-09-09 | 14 (12 vivas + 2 resíduos 404) | 7 | 54% | 0 | 0 | — | **SEGURA até 16/09** | Primeira medição. Série de Desempenho tem só 05 e 06/09 (propriedade nasceu 06/09). Relatório de Páginas em "dados em processamento"; indexação medida por `site:`. Das 7 indexadas, 5 não vendem (home, /calculadoras/, /metodologia/, /sobre/, /divulgacao-de-afiliados/); as 6 fora do índice são as que vendem (C5, C12, C15 e as 3 respostas paramétricas de 08/09). Sitemap processado, lido em 09/09 — descoberta não é o problema. Sub_id provado: 2 cliques Shopee com `aquametria-C5` e `aquametria-C3`. Vendas: 0. |

## Levas publicadas — o que cada uma mira, para a leitura ter o que medir

A seção 14.9 manda cada página nascer com duas promessas escritas: a consulta que ela mira e por que ela consegue chegar às dez primeiras. Elas moram no registro do snippet que serve a página; esta tabela é o índice delas, para a leitura semanal não precisar abrir código.

| leva | data | URLs | consulta-alvo de cada uma | classificação da SERP na véspera | posição medida |
|---|---|---|---|---|---|
| malha 1 — eixo `/peixes/` | 2026-09-12 | `/peixes/` · `/peixes/tetras/` · 3 fichas de tetra | "quantos litros por peixe aquário" · "quantos litros para tetras" · "quantos litros para tetra neon" · "quantos litros para neon cardinal" · "quantos litros para mato grosso peixe" | **ALVO nas três fichas** (12/09/2026): top 7 a 9 de blog de nicho, loja e portal; nenhum domínio forte, nenhum número atribuído a fonte nomeada, e eles se contradizem entre si (40 L para 8 a 10 neons contra 20 L para 6 a 8; cardume de 3 contra cardume de 6 no mato-grosso) | ainda não — nasceram hoje |
| malha 2 e 3 — `/peixes/tetras/` e `/peixes/corydoras/` | 2026-09-12 | 4 fichas de tetra · a categoria coridoras + 4 fichas | "quantos litros para tetra ember" · "...tetra brilhante" · "...rodostomo" · "...tetra negro" · "quantos litros para coridoras" · "...coridora bronze" · "...coridora pimenta" · "...coridora panda" · "...coridora sterbai" | **ALVO**, classificadas na MESMA data da leva 1 (12/09/2026) — a constante `AQUAMETRIA_PEIXES_SERP_EM` do snippet, e o `porque` de cada ficha traz a leitura dela. A do rodóstomo é a única do eixo em que alguém do top publica a base (80 × 30 × 40 cm), e publica sem dizer de onde tirou | ainda não |
| **malha 4 — `/peixes/bettas/`** | classificada em **2026-09-13**, **publicada em 2026-09-14** | `/peixes/bettas/` + 3 fichas: betta · colisa-anão · gurami mel | "quantos litros para gourami" (categoria) · "quantos litros para um betta" · "quantos litros para colisa anão" · "quantos litros para gurami mel" | **ALVO nas quatro.** Ver a leitura inteira embaixo desta tabela | a medir |

## A classificação de SERP da leva 4 — `/peixes/bettas/`, medida em 13/09/2026

> **A leva saiu em 14/09/2026**, com as quatro URLs e as quatro declarando
> `serp_em: 13/09/2026` no registro — quem não declarasse herdaria 12/09/2026,
> que seria mentira nestas quatro. Esta seção fica como foi escrita, um dia
> antes das páginas: é a prova de que a classificação veio antes, e não depois.

Escrita ANTES de a leva existir, que é o que a seção 14.9 manda e a 21.3 mantém
de pé abaixo do piso. **As quatro consultas são ALVO**, e nenhuma delas tem no
top uma fazenda de conteúdo com domínio forte fechando a página.

| consulta | quem ocupa o top | os números que eles publicam | veredito |
|---|---|---|---|
| "quantos litros para um betta" | 1 blog de loja grande (Cobasi) e 5 blogs de nicho/portais (peixeseaquarismo, aquariovivo, vigopeixe, manualdoagora, guiadoaquarismo) | **20 L**, **18 L**, **40 L** — e o mesmo texto que diz "mínimo 18" diz "recomendado 40" | **ALVO** |
| "quantos litros para colisa anão" | 3 fichas de aquarismo e 5 páginas de produto de loja (Pró-Aquarista, Fazenda Submersa, Solaqua) | **56 L**, **40 L**, **36 L**, e "40 a 44 L é o mínimo aceitável" | **ALVO** |
| "quantos litros para gurami mel" | 6 fichas de aquarismo e 3 páginas de produto de loja | **40 L**, **36 L** (sozinho), **56 L** (grupo de 3) — e um deles declara a BASE: 60 × 30 × 30 cm | **ALVO** |
| "quantos litros para gourami" (a da categoria) | quase só página de produto de loja, mais um agregador | 40, 54, 60 e **70 L**, cada um de uma espécie diferente, sem dizer de qual | **ALVO** |

**A medição que vale mais que as quatro linhas acima, e ela não é sobre uma
consulta: é sobre duas.** O *Trichogaster lalius* — a colisa-anão, uma espécie
só — aparece com **56 L** numa consulta e com **70 L** na outra, no mesmo dia,
além do 40 e do 36 que já discordavam entre si. **Quatro números para o mesmo
peixe, nenhum atribuído a fonte nomeada, dois deles na primeira página.** É a
tese desta ilha medida por fora dela, e é o parágrafo que a ficha da colisa tem
de ter.

**O que a ilha tem e eles não têm, e é o mesmo de sempre:** a base declarada por
compêndio com nome e data, ao lado das duas réguas brasileiras de lotação com a
atribuição de cada extremo. **O que ela tem A MAIS nesta categoria** — e é o que
justifica a categoria existir em vez de três fichas soltas — é o arranjo social:
sob o mesmo rótulo estão um peixe que vive **sozinho**, um que vive **em casal**
e um que vive **em grupo com hierarquia**, e nenhuma das quatro SERPs distingue
isso. Quem responde "quantos litros para gourami" com um número só está
respondendo a pergunta errada.

**O limite deste método, declarado e não escondido:** a classificação sai da
ferramenta de busca desta nuvem, que não é o Google brasileiro visto de um IP
brasileiro. Ela mede *quem publica* e *que número publica* — que é o que a 14.9
pede para decidir —, e não a ordem exata do top 10 para um usuário no Brasil. É
o mesmo método das levas 1 a 3, e fica dito aqui em vez de ficar subentendido.

**Consequência de código, já resolvida:** esta é a primeira classificação em
data diferente da das páginas no ar, e por isso a data deixou de ser só a
constante `AQUAMETRIA_PEIXES_SERP_EM` e virou o campo `serp_em` do registro
(snippet 1.3.0, 13/09/2026). A leva 4 nasce declarando `'serp_em' => '13/09/2026'`
em cada uma das quatro páginas; quem não declarar, herda 12/09/2026 — que seria
mentira nestas quatro.

## Leitura da série
- **Zero impressão em 2 dias de série NÃO prova palavra-chave errada** — é ausência de evidência. A leitura de 16/09 decide.
- A leva de 08/09 (6 páginas) não indexou nenhuma. **A trava que essa frase criava caiu em 12/09/2026**, pela seção 21 do `ARQUIPELAGO.md` (piso da rampa): com 18 URLs a ilha segue ABAIXO do piso de 40, e abaixo do piso zero impressão não é informação e não trava leva. O fato continua verdadeiro e continua sendo o que a leitura de 16/09 tem de explicar; ele só deixou de ser motivo de congelamento.
- **O que a leitura de 16/09 precisa responder sobre a leva de hoje**, e é diferente do que ela responde sobre a de 08/09: as cinco URLs novas são as primeiras desta ilha com **três níveis de URL, mãe publicada e `BreadcrumbList` com quatro degraus**. Se elas indexarem e a leva de 08/09 continuar fora, a hierarquia é uma hipótese a olhar — e se nenhuma das duas indexar, a causa é do domínio e não da página.

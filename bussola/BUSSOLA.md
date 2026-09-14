# BÚSSOLA — o cérebro que escolhe a próxima ilha

Este arquivo é a lei da Bússola, como `ARQUIPELAGO.md` é a lei da Fundação e da Sentinela.
A rotina da Bússola é curta de propósito: o que ela avalia mora aqui. Corrigir a Bússola = editar este arquivo.

Vive nesta pasta: `BUSSOLA.md` (regras), `fila.md` (ranking vivo, com as notas componentes de cada nicho),
`rodadas/<NNN>.md` (o que cada rodada mediu e por quê) e `dossies/<nicho>/` (o pacote de nascimento de um nicho aprovável).

## 1. Para que a Bússola existe

O Arquipélago ganha dinheiro com comissão de afiliado em páginas que respondem, com número e fonte, uma pergunta
que o visitante faz com o cartão na mão. A Bússola escolhe **onde** isso vale a pena. Errar aqui custa meses:
uma ilha em nicho fechado nunca chega à primeira página, e o relógio do Google não devolve o tempo.

Restrições permanentes do Raphael, válidas para todo nicho: ele não aparece (sem rosto, vídeo ou presença pessoal),
tráfego 100% orgânico sem anúncio, sem link building pago, nunca YMYL (saúde, dinheiro, jurídico).

## 2. O que um nicho precisa ter (critérios estruturais — eliminatórios)

**Ampliados em 13/09/2026, por decisão do Raphael.** O motivo está registrado porque importa: os três primeiros nichos eram todos de marketplace, e os critérios tinham sido escritos descrevendo **esses três** em vez de descrever a regra. Critério que descreve o passado desqualifica o futuro — foi o que quase aconteceu com o nicho de viagem, que reprovava nos quatro e mesmo assim tem a forma certa.

- **Objeto de compra verificável na fonte de quem vende, fabrica ou opera.** O caso comum é produto físico com ficha de fabricante. **Também vale serviço com preço e condição publicados por quem opera** — passeio, ingresso, seguro, plano. O que NÃO vale é objeto cujo preço e cujas condições só existam em opinião de terceiro: sem fonte primária não há dado, e sem dado a ilha é blog.
- **Decisão de compra paramétrica**: depende de um número que o usuário dá. Em produto físico é medida, litragem, potência, compatibilidade peça × modelo. **Em serviço é dias × pessoas × padrão** — "quanto custa 7 dias em X para 2 pessoas" é tão paramétrico quanto "qual cola para vaso de cerâmica".
- **Existe recompra.** Consumível, peça, ou **o mesmo usuário voltando para outra ocasião do mesmo tipo** (outro destino, outra temporada). Recorrência anual conta; recorrência nenhuma desqualifica.
- **Cobertura de afiliado (cicatriz da Aquametria, 09/09/2026 — ampliada em 13/09/2026):** o que a ferramenta recomendaria tem **programa de afiliado acessível, com link rastreável e comissão declarada**. Verifique pelo menos 10 itens que uma ferramenta do nicho indicaria; se menos de 7 tiverem programa, o nicho está **desqualificado** por enquanto. **Marketplace não é requisito — é o caso comum.** Na Aquametria, 20 de 29 produtos não existiam na Shopee, e foi isso que criou a regra: o que ela protege é a existência de **porta de compra rastreável**, não a marca do programa. Ilha que recomenda o que não tem link é trabalho sem receita, venha o link de onde vier. Cobertura não verificada não é cobertura aprovada: nicho com verificação incompleta fica `pendente`, fora do ranking, e não é pontuado.

## 3. Scorecard v3 (rodada 004 em diante)

Notas de 0 a 5. A mudança em relação à v2: **S se divide em duas**.

- **S_par — SERP da busca PARAMÉTRICA** ("qual X para Y", "quanto de X para Y", "X serve no Y"). É a nota que decide.
  5 = só fórum, vídeo, blog velho ou resposta genérica sem número · 4 = blog de loja sem calculadora · 3 = misto ·
  1 = fazenda programática com página no título exato da consulta · 0 = calculadora de grande varejista instalada (desqualifica).
- **S_com — SERP da busca COMERCIAL** ("melhor X 2026"). Só registro: está tomada por fazenda em praticamente todo nicho
  de eletro, e por isso NÃO discrimina. Entra com peso pequeno.
- **S = S_par × 0,85 + S_com × 0,15.**
- **P** paramétrico (quão natural é a pergunta com número) · **D** demanda (ordenação relativa por proxies gratuitos:
  autocomplete, buscas relacionadas, Trends, composição da SERP) · **M** = 2,2 × log10(R$ por venda) − 0,07, limitado a 5,
  calculado sobre o ticket TÍPICO que a recomendação converte (nunca o topo da categoria) × a comissão do **programa que a
  ilha realmente vai usar**. **A âncora é a tabela publicada do programa de destino — Shopee Afiliados e Mercado Livre no
  caso comum, ou o programa próprio do operador quando a ilha for de serviço. A Amazon NÃO é âncora de nada: a seção 7 do
  `ARQUIPELAGO.md` a mantém fora de todas as ilhas, e régua de dinheiro apontada para um programa que ninguém usa mede o
  nicho errado.** Registre na `fila.md` qual programa e qual data de leitura sustentam o percentual. **Percentual não
  alcançado na rodada = M não calculado**, e nicho sem M sai do ranking para "fora do ranking" com o motivo escrito —
  nunca herde percentual de rodada anterior sem reverificar, e nunca preencha com estimativa · **R** recorrência ·
  **A** acesso ao programa (existe porta de compra rastreável para o que a ferramenta recomenda? aplique a regra ampliada
  da seção 2 — marketplace é o caso comum, não o requisito) · **V** verificabilidade da especificação.

- Facilidade = S × 0,60 + P × 0,40
- Retorno = M × 0,40 + D × 0,30 + R × 0,15 + A × 0,15
- **Índice = média harmônica** = 2 × Facilidade × Retorno ÷ (Facilidade + Retorno). Desaba quando um lado é fraco — é a regra
  do Raphael: lucrativo mas impossível de ranquear não serve; fácil mas sem dinheiro também não.
- Desqualifica: V < 2, S_par ≤ 1, cobertura de afiliado < 7/10.

## 3.1 Nota que não foi medida não vira índice

Três regras que nasceram da autocrítica da própria rodada 004, e valem da 005 em diante.

- **Componente convertido não é componente medido.** Herdar a nota de um scorecard antigo por conversão mecânica (por exemplo `S_par = S_com = S` da v2) produz um número com cara de medição que ninguém mediu. Nicho nessa situação **sai do ranking** e vai para "fora do ranking" com estado `pendente`, até a rodada refazer a SERP. Nota de rodapé não resolve: quem lê a tabela lê a coluna, não o rodapé.
- **Valor neutro é invenção.** Preencher P, D, R, A ou V com um valor médio porque o componente não foi recuperado é fabricar índice. Se falta componente, **não calcule o índice** — `pendente`, fora do ranking, motivo escrito.
- **V é por ferramenta, não por nicho.** A verificabilidade tem que ser medida na fonte de CADA uma das três primeiras ferramentas do plano (seção 5, item f), não na fonte mais fácil do nicho. Fabricante que publica o dado da ferramenta 1 não prova nada sobre a ferramenta 2. No dossiê, escreva V ferramenta por ferramenta, com o fabricante e o documento que sustentam cada uma; **ferramenta cujo dado não foi encontrado não entra no plano**.

Fazendas programáticas conhecidas no Brasil (presença delas na paramétrica derruba S_par): guiaomelhor, qualeamelhor,
melhoresparacomprar, guiarecomenda, buscamelhores, recomenda360, br.my-best, analisamelhor, topavaliado, monitorcasa,
qualmelhorcomprar, ositensdecasa. SERP paramétrica dominada por YouTube/TikTok é sinal FORTE de abertura.

## 4. Toda rodada reavalia o topo (SERP aberta fecha)

Antes de pontuar candidato novo, refaça a busca paramétrica dos **5 primeiros** da fila sem ilha nascida. Se entrou
fazenda, rebaixe S_par, registre a data e mova na fila. Aquarismo caiu de 1º para 12º em quatro dias (03→07/09/2026) —
nicho aprovado que fechou tem que ser desmarcado antes de alguém pagar domínio.

## 5. Cadência e o que a rodada entrega

- A Bússola roda **uma vez por semana** (segunda de manhã). O Arquipélago nasce **duas ilhas por semana** enquanto a meta
  for ~10 ilhas (decisão do Raphael em 10/09/2026): o relógio do Google é o único recurso que não se compra depois, e cada
  ilha nova herda as cicatrizes das anteriores — por isso escalonado, não dez de uma vez.
- Toda rodada garante que existam **dois dossiês prontos** para os dois primeiros da fila que ainda não têm ilha
  (`dossies/<nicho>/`). Dossiê é o que o Raphael aprova com um "sim"; sem dossiê não há decisão.
- Um dossiê contém: (a) o porquê do nicho em 10 linhas, com as notas e as duas SERPs descritas; (b) as 5 consultas
  paramétricas-alvo, cada uma com quem ocupa o top 10 hoje; (c) a prova de cobertura de afiliado (os 10 produtos e onde
  estão); (d) naming — 30 a 40 candidatos, filtro DNS (negativo, nunca prova de disponibilidade) e confirmação em
  `https://registro.br/v2/ajax/avail/raw/<dominio>.com.br` (`status: 0` = livre), o nome escolhido em duas linhas, e o
  descartado com motivo; (e) identidade — paleta com hex e contraste WCAG calculado (≥ 4,5:1 em texto normal), tipografia
  (no máximo 3 famílias, uma monoespaçada para número e unidade) e o conceito do símbolo, que nasce do GESTO TÉCNICO do
  nicho (medir, encaixar, dimensionar), nunca de animal, produto ou mascote; se a skill `design` estiver disponível,
  o canvas com os quatro artboards (logo, paleta, tipografia, aplicações) e o link no dossiê; (f) o plano da ilha: as 3
  primeiras ferramentas, o que vai no banco, o que a casca precisa ter; (g) o `VOZ.md` da ilha, pronto, no formato dos três existentes (`ilhas/*/VOZ.md`): quem entra, momento, quem fala, como fala, frases com a nossa cara × proibidas, home e molde de casca (seção 15 do `ARQUIPELAGO.md`). A Fundação lê o dossiê no dia em que a ilha nasce.
- Quando o Raphael aprova, a ilha nasce pela seção 11 do `ARQUIPELAGO.md` (ele paga o domínio; o resto é da fábrica),
  com casca + 1 ferramenta + sitemap no ar em até 48h — é isso que liga o relógio do Google. O crescimento vem na rampa.

## 6. O que a Bússola nunca faz

Não compra domínio, não cria conta, não escreve na memória como canal de decisão (o canal é o repositório, pelas
Mãos — seção 12.2 do `ARQUIPELAGO.md`), não pontua com percentual inventado ("não verificado" é resposta válida),
e não promove nicho por ser bonito: o critério único é ROI dentro da facilidade de ranquear.

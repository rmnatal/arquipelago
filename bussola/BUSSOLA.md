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

- Produto físico comprável no Brasil, com **especificação verificável na fonte do fabricante**.
- **Decisão de compra paramétrica**: depende de um número do usuário (medida, litragem, potência, compatibilidade peça × modelo).
- Existe consumível ou peça de recompra (recorrência).
- **Cobertura de afiliado (cicatriz da Aquametria, 09/09/2026):** os produtos que a ferramenta recomendaria existem na
  Shopee **ou** no Mercado Livre. Verifique pelo menos 10 produtos que uma calculadora do nicho indicaria; se menos de 7
  tiverem anúncio num dos dois programas, o nicho está **desqualificado** por enquanto — ilha que recomenda o que não tem
  link é trabalho sem receita (na Aquametria, 20 de 29 produtos não existiam na Shopee).

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
  ancorado na tabela oficial da Amazon Associados BR e no ticket TÍPICO que a recomendação converte, nunca no topo da
  categoria · **R** recorrência · **A** acesso ao programa (Shopee/ML cobrem? com a regra da seção 2 já aplicada) ·
  **V** verificabilidade da especificação.

- Facilidade = S × 0,60 + P × 0,40
- Retorno = M × 0,40 + D × 0,30 + R × 0,15 + A × 0,15
- **Índice = média harmônica** = 2 × Facilidade × Retorno ÷ (Facilidade + Retorno). Desaba quando um lado é fraco — é a regra
  do Raphael: lucrativo mas impossível de ranquear não serve; fácil mas sem dinheiro também não.
- Desqualifica: V < 2, S_par ≤ 1, cobertura de afiliado < 7/10.

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

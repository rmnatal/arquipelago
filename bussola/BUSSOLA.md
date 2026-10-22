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

## 3.0-b PISO DE DEMANDA ABSOLUTA — a lacuna que custou uma ilha (18/09/2026)

Toda a régua acima é **relativa**. `S_par` e `S_com` medem quem ocupa a SERP; `P` mede se a pergunta é natural; `D` ordena nichos entre si por proxies gratuitos; `M` é ticket × comissão. **Nenhum componente diz quantas pessoas procuram.** Na frase do Raphael, em 18/09/2026: *"ranquear em primeiro para um termo que tem 10 buscas por mês não adianta nada"*.

**A REGRA NOVA, e o que ela mede não é o que parece.** O piso **não** é o volume do termo-cabeça do nicho. É este: **as consultas que as FERRAMENTAS da ilha respondem precisam ter volume próprio.** Um nicho pode ter milhares de buscas na cabeça comercial e zero na metade que a ilha vai construir — e é exatamente isso que aconteceu com a Robometria, medido em `bussola/medicoes/volume-absoluto-2026-09-18.md`: `filtro para aquario` tem 1 mil–10 mil buscas/mês e `filtro robô aspirador` está abaixo do limiar, no mesmo dia e na mesma ferramenta.

**Como medir, antes de a ilha nascer:** monte uma amostra de pelo menos 40 consultas do corpus paramétrico do nicho — **incluindo os termos mais genéricos possíveis da metade que a ilha vai atender** — e rode no Google Keyword Planner (Brasil, últimos 12 meses). Registre a medição em `bussola/medicoes/` com data, ferramenta, recorte e ressalvas. **Nicho em que a maioria das consultas paramétricas volta `—` não vira ilha**, por melhor que seja o índice: índice alto em corpus vazio é ilha perfeita num deserto.

**A escala ainda é magra e isto está dito de propósito:** hoje existem dois pontos de calibração — Aquametria 51% e Robometria 18% de consultas com volume mensurável. **Dois pontos não definem um corte numérico**, e por isso esta seção não fixa um percentual mínimo ainda. Fixa o PROCEDIMENTO e a obrigação de registrar. O corte se escreve quando houver a terceira ilha medida do mesmo jeito — e quem escrever o corte com dois pontos estará fazendo exatamente o que a 3.1 abaixo proíbe.

**SUPERADO EM PARTE em 21/10/2026:** o corte numérico que este parágrafo deixava para depois foi fixado pelo Raphael, e não em percentual de consultas com volume, e sim em TRÁFEGO: é a seção 3.0-c, logo abaixo. O procedimento de medir e registrar desta seção continua valendo e alimenta a conta da 3.0-c.

## 3.0-c PISO DE TRÁFEGO — 1.000 visitas orgânicas por dia, ou a ilha não nasce (decisão do Raphael, 21/10/2026)

**A frase dele:** "Como a gente vai se basear em tráfego 100% orgânico, a Bússola tem que encontrar nichos que sejam, ao mesmo tempo, fáceis de ranquear e que tragam pelo menos 1.000 pessoas por dia. Se for menos de 1.000 pessoas por dia, não compensa fazer essa ilha. A conversão em venda fica em torno de 1%; ranquear fácil numa palavra que traz 10 ou 20 pessoas por mês não adianta nada. E tem que ter produto para vender para essas pessoas, de preferência na Shopee."

**3.0-c.1 A trava, eliminatória:** nenhum nicho vira ilha se a conta abaixo der **menos de 1.000 visitas orgânicas por dia** com a ilha ranqueada no que ela consegue alcançar. Mais é melhor; menos desqualifica, por melhor que seja o índice da seção 3.

**3.0-c.2 A conta, obrigatória em todo dossiê:**
- Liste as consultas que a ilha vai atender **e que levam a um produto vendável** (a metade paramétrica e a de produto pelo nome, seção 30 do `ARQUIPELAGO.md`). Consulta sem produto no fim não entra na soma.
- **Volume MEDIDO, nunca estimado:** Google Keyword Planner, Brasil, últimos 12 meses, registrado em `bussola/medicoes/` com data. Se a conta devolver faixa (`1 mil – 10 mil`), use o **piso da faixa**. Termo com `—` conta zero.
- Para cada consulta, a **posição alcançável** pela classificação de SERP desta lei (S_par): SERP aberta → top 3; mista → 4 a 10; tomada → não entra na soma.
- **CTR por posição** de uma curva pública de CTR orgânico com fonte e data registradas no dossiê, descontada a presença de resposta de IA no topo quando a SERP mostrar uma. A curva escolhida fica escrita no dossiê, para a próxima rodada usar a mesma.
- **Visitas/dia = Σ (volume mensal × CTR da posição alcançável) ÷ 30.** Escreva o número, a soma por cluster e a lista das 20 consultas que mais pesam.
- Ao lado, sempre: **vendas/dia esperadas = visitas/dia × 1%** e **comissão/dia = vendas × ticket típico × comissão do programa** (seção 3, M). É ordem de grandeza para decidir, marcada como estimativa — nunca promessa.

**3.0-c.3 Tem que ter o que vender:** a busca precisa ter intenção clara num nicho específico, terminando em produto que a ilha consiga indicar como afiliado. **Shopee é o programa preferido do Raphael — centralizar nela sempre que possível.** A cobertura de afiliado da seção 2 passa a ser medida primeiro na Shopee: se 7 de 10 produtos que a ferramenta indicaria estão na Shopee com link rastreável, o nicho é Shopee-só; Mercado Livre e programa de operador entram apenas para o que a Shopee não vende, e o dossiê diz quantos itens dependem deles.

**3.0-c.4 O que esta seção não faz:** não muda a facilidade (S, P) nem o índice — um nicho com 1.000 visitas/dia possíveis mas SERP tomada continua desqualificado pela seção 3. A ilha precisa passar nas DUAS: fácil de ranquear E com 1.000 visitas/dia no que é ranqueável.

**3.0-c.5 Sem medição, sem ilha:** se o Planejador não abrir, ou a conta não fechar por falta de dado, o nicho vai para "fora do ranking" com o motivo escrito (seção 3.1). Nunca preencher a soma com palpite.

## 3.0-d O PISO PASSA A SER DA BUSCA QUE COMPRA — 1.000 visitas/dia de intenção de compra (decisão do Raphael, 22/10/2026)

**A frase dele:** *"O mais importante de tudo é ter venda. E para ter venda tem que ter audiência (…) se a gente
conseguir fazer o cruzamento de ilhas que tem potencial de fazer 1.000 visitas por dia com o público interessado
em comprar, isso que é o ideal."* E, fechando: **"1.000 visitas por dia de buscas de intenção + maximização da
comissão."**

**O que esta seção corrige na 3.0-c.** A 3.0-c mandava somar *"as consultas que a ilha vai atender e que levam a
um produto vendável"* — mas na prática as rodadas somaram o corpus informacional inteiro do nicho, porque a lei
não definia como separar as duas metades nem obrigava a separá-las antes de medir. **O resultado foi medir
audiência onde não há comprador.** Em jardinagem, medido em 21–22/10/2026: o nicho tem 405.830 buscas
informacionais ranqueáveis por mês e **apenas 20.930 delas — 5,2% — terminam em produto.** Os outros 94,8% são
*"como fazer muda de X"* e *"como plantar X"*, que é **a busca de quem quer justamente NÃO comprar**: a pessoa já
tem a planta e quer multiplicar de graça em vez de comprar outra. Pelo piso antigo jardinagem dava 1.441
visitas/dia e passava. Pelo piso desta seção dá **73** e reprova por treze vezes.

**3.0-d.1 A TRAVA, eliminatória, e ela substitui a leitura da 3.0-c.1 sobre o nicho inteiro:** nenhum nicho vira
ilha se as consultas **com intenção de compra** não somarem, sozinhas, **1.000 visitas orgânicas por dia** com a
ilha ranqueada no que ela alcança. O corpus informacional que não termina em produto **não entra na soma** — pode
ser escrito ao lado como volume de apoio, nunca somado ao piso. Como o piso novo é estritamente mais duro que o
antigo, um nicho que passa nele passa automaticamente na 3.0-c.1; a 3.0-c.2 continua valendo inteira para **como**
se faz a conta (volume medido no Planejador, posição alcançável pela SERP vista no Chrome, curva de CTR escrita
no dossiê, desconto de dupla contagem, visitas/dia = Σ volume × CTR ÷ 30).

**3.0-d.2 O QUE É "CONSULTA COM INTENÇÃO DE COMPRA" — o teste, porque a trava inteira depende dele.**
Uma consulta tem intenção de compra quando **a resposta correta dela nomeia um produto que a ilha pode indicar
como afiliado**. O teste em uma pergunta: *"para responder certo, eu preciso mandar a pessoa comprar alguma
coisa?"*
- **Sim** → entra na soma: `qual adubo para zamioculca` · `substrato para rosa do deserto` ·
  `qual corrediça para gaveta de 40 cm` · `qual resistência do chuveiro X` · `que bitola de cabo para 5500W`.
  A resposta é um objeto com especificação, e sem comprá-lo a pessoa não resolve o problema.
- **Não** → fica fora: `como fazer muda de rosa do deserto` · `como plantar morango` · `como cuidar de suculenta`.
  **A regra de corte é esta: se a consulta pode ser respondida por inteiro sem nomear nenhum produto, ela não é
  de intenção de compra** — mesmo que a pessoa, no fim, acabe comprando terra. Intenção que depende de o leitor
  mudar de ideia não é intenção medida, é esperança.
- **Caso de borda, e ele decide no lado conservador:** consulta que nomeia o produto mas busca o modo de usar
  (`como aplicar NPK 10-10-10`) fica **fora**, porque quem pergunta já comprou. Na dúvida entre as duas metades,
  a consulta vai para fora da soma — errar para menos custa um nicho que não nasceu; errar para mais custa uma
  ilha inteira num deserto de compradores, que é o erro que esta seção existe para impedir.

**3.0-d.3 A SEPARAÇÃO É FEITA ANTES DO PLANEJADOR, e a razão fica escrita.** A rodada monta **duas listas** —
a de intenção de compra e a de apoio — e **cola no Planejador só a primeira** para efeito do piso. O dossiê
registra as duas somas e **a razão entre elas** (em jardinagem: 5,2%), porque é esse número que diz se o nicho
é de comprador ou de hobby. Razão baixa com volume enorme é o retrato de jardinagem e **não vira ilha**.

**3.0-d.4 MAXIMIZAÇÃO DA COMISSÃO — e a fronteira que não pode ser cruzada.**
Entre nichos que passam na trava acima, **a Bússola escolhe o de maior comissão medida**, e isso é trabalho dela:
é para isso que o M existe. Três regras:
- **A comissão é medida no PAINEL de afiliado, produto por produto, na mediana** (`affiliate.shopee.com.br` →
  Oferta de produto), nunca herdada de rodada anterior e nunca lida de página institucional. A remedição de
  22/10/2026 mostrou por quê: a `fila.md` inteira estava ancorada em 3% e **o piso real é 8% em dez nichos de
  dez**, com ferragem de marcenaria em 13% e peça de robô aspirador em 12%.
- **O TICKET também é medido no painel, na mediana, nunca suposto.** A mesma remedição mostrou irrigação por
  gotejamento com ticket real de R$ 55 onde a fila supunha R$ 250 — a comissão subiu de 3% para 8% e **o M caiu
  mesmo assim**. Comissão remedida sobre ticket suposto conserta metade do erro e piora a outra.
- **A FRONTEIRA, e ela é absoluta: maximizar comissão vale na escolha do NICHO, nunca na escolha do PRODUTO.**
  A seção 7 do `ARQUIPELAGO.md` proíbe, com todas as letras, ordenar recomendação por taxa — *"nunca comparar
  taxa, nunca promover produto pior porque paga mais"* — e a ordem lá é elegibilidade técnica, adequação, e loja
  só como desempate entre equivalentes. Portanto **o M de um nicho se calcula sobre a comissão MEDIANA da
  categoria, nunca sobre a fatia de 18–28% que existe nela**: calcular sobre a fatia alta mede uma ilha que o
  Arquipélago não pode construir. Onde esta seção e a 7 parecerem divergir, **manda a 7**.

**3.0-d.5 O QUE ESTA TRAVA CUSTA, dito agora para ninguém se surpreender depois.** Pela curva de CTR em uso
(Backlinko, top-3 18,7%), 1.000 visitas/dia de intenção de compra exigem **≈ 214.000 buscas/mês de intenção de
compra ranqueadas em top-3** — e, se a SERP for mista (4–10, 4,2%), exigem quase um milhão, o que na prática
significa que **só SERP aberta passa nesta seção**. É um corte duro e deliberado: **é possível que nenhum nicho
da `fila.md` de hoje passe nele.** O Raphael aceitou esse custo ao fixá-lo, e a leitura correta disso é que a
Bússola prefere não parir ilha a parir ilha sem comprador. **Nicho que reprova aqui não vira ilha por melhor que
seja o índice da seção 3** — e nicho que passa aqui ainda tem de passar na seção 3 (fácil de ranquear) e na
cobertura de afiliado da seção 2. São três portões independentes, e a ilha ideal é o cruzamento dos três.

## 3.1 Nota que não foi medida não vira índice

Três regras que nasceram da autocrítica da própria rodada 004, e valem da 005 em diante.

- **Componente convertido não é componente medido.** Herdar a nota de um scorecard antigo por conversão mecânica (por exemplo `S_par = S_com = S` da v2) produz um número com cara de medição que ninguém mediu. Nicho nessa situação **sai do ranking** e vai para "fora do ranking" com estado `pendente`, até a rodada refazer a SERP. Nota de rodapé não resolve: quem lê a tabela lê a coluna, não o rodapé.
- **Valor neutro é invenção.** Preencher P, D, R, A ou V com um valor médio porque o componente não foi recuperado é fabricar índice. Se falta componente, **não calcule o índice** — `pendente`, fora do ranking, motivo escrito.
- **V é por ferramenta, não por nicho.** A verificabilidade tem que ser medida na fonte de CADA uma das três primeiras ferramentas do plano (seção 5, item f), não na fonte mais fácil do nicho. Fabricante que publica o dado da ferramenta 1 não prova nada sobre a ferramenta 2. No dossiê, escreva V ferramenta por ferramenta, com o fabricante e o documento que sustentam cada uma; **ferramenta cujo dado não foi encontrado não entra no plano**.

Fazendas programáticas conhecidas no Brasil (presença delas na paramétrica derruba S_par): guiaomelhor, qualeamelhor,
melhoresparacomprar, guiarecomenda, buscamelhores, recomenda360, br.my-best, analisamelhor, topavaliado, monitorcasa,
qualmelhorcomprar, ositensdecasa. SERP paramétrica dominada por YouTube/TikTok é sinal FORTE de abertura.

**A LISTA FOI AMPLIADA EM 14/09/2026 (rodada 005), porque estava desatualizada e isso superestimava S_com.** Em doze
consultas medidas, os doze nomes acima pegaram **quatro ocorrências** — enquanto fazendas do mesmo molde e **fora da
lista** dominaram duas SERPs comerciais inteiras, o que dava S_com alto para SERP que na verdade estava fechada. Entram
na lista: techminuto, casastech, focsfoto, guiadeferramenta, melhoresdotech, envidracamentoemsacadas, santonela,
techinter, amoprodutinhos, guiadosperifericos, avaliado.com.br, qualmelhorproduto, radardacasa, topdezmelhores, achehoje,
buscageral, buscasempre, osreviews, mecanie, gdm, cabemcasa, mastereview, prosanacozinha.
**E a régua passa a ser de FORMA, não de lista:** qualquer domínio cujo título siga o molde "As N Melhores X de 2026",
sem medição própria, conta como fazenda — esteja nomeado aqui ou não. **A lista é atalho de reconhecimento, nunca a
definição**, e toda rodada que encontrar um nome novo o acrescenta aqui.

**AMPLIADA NA RODADA 006 (21/10/2026) — trinta e um nomes novos, agrupados por MOLDE, porque é o molde que reconhece
o próximo.** Catorze candidatos foram medidos e dez morreram; quatro deles morreram por **calculadora já instalada e
ranqueando que não é de varejista nem de fabricante** — ver a proposta de régua no fim deste bloco.
- **Espelho de oferta de marketplace** (uma página por oferta, título igual ao do anúncio; são afiliados programáticos,
  isto é, concorrentes diretos das ilhas): `escorregaopreco.com.br`, `melhoraopreco.com.br`, `descontostop.com`.
- **Calculadora traduzida servindo uma página por valor do parâmetro** (`/plate-calculator/40-kg`, `/50-kg`, `/60-kg`…):
  `size.ly`, `omnicalculator.com/pt`, `miniwebtool.com/br`, `arvo.guru/pt-BR/tools/`, `hacecuentas.com/pt`,
  `calculadorabrasil.com.br`.
- **Loja ou fabricante publicando sobre paramétrica alheia**: `maxturbos.com.br` (loja de turbina respondendo sobre
  cama, pneu, óleo e relação — apareceu em TODAS as consultas automotivas da rodada, às vezes com 4 posições),
  `labra.com.br`, `casadoseletrodomesticos.com.br`, `engehall.com.br`, `webarcondicionado.com.br`, `larpontual.com.br`.
- **Parasita puro** (domínio sem relação nenhuma com o nicho): `auditorioibirapuera.com.br` (casa de espetáculos
  respondendo "qual o fio certo para 220V", em elétrica E em chuveiro), `quintoandar.com.br/guias/` (portal
  imobiliário, em ventilador E em caixa d'água), `projetoagathaedu.com.br` (questões do ENEM, em "dimensionar
  bitolas"), `faq.blackpilado.com.br`.
- **Banco de ficha ou de preço gerado por modelo**: `olhardigital.com.br/fichas-tecnicas/`,
  `oficinadanet.com.br/smartphones/comparacao-`, `mercadolivre.com.br/blog/` e `/blog/reviews/<sku>`,
  `shopee.com.br/blog/<modelo>-ficha-tecnica/`, `zoom.com.br`, `buscape.com.br`, `bondfaro.com.br` (os três do mesmo
  grupo, uma página por string digitada), `orcamentor.com` (base SINAPI programática).
- **Demais**: `clickpetroleoegas.com.br`, `digitei.com`, `mundodosreviews.com.br`, `motoragora.com.br`,
  `portalinsights.com.br`, `engenharia360.com`, `cidesp.com.br`, `vocepergunta.com`, `essemundoenosso.com.br`,
  `voltflow.net`, `uai.com.br`, `plataformaassaad.com.br`, `ecoautomacao.com.br`, `monitordomercado.com.br`,
  `oantagonista.com.br/economia/`, `tupi.fm`, `revistaoeste.com`, `accelerated-ideas.com`.
- **PORTAL GRANDE CONTADO COMO FAZENDA PELA RÉGUA DE FORMA, e isto é novo na prática**:
  `canaltech.com.br/eletro/<a consulta inteira>`, `olhardigital.com.br/curiosidades/?p=<id>` (seis posições numa só
  SERP), `opovo.com.br/trends/<a consulta>`, `tecmundo.com.br/produto/<id>-melhores-<x>-de-<ano>`. Autoridade de marca
  não muda o molde: página por consulta sem medição própria é fazenda, venha de onde vier.

**AMPLIADA NA RODADA 007 (21/10/2026) — o nicho de jardinagem, 21 consultas, e um molde que a lista não tinha:
a REDE DE CONTEÚDO SINDICALIZADO.** Agrupados por molde, porque é o molde que reconhece o próximo.
- **Rede de conteúdo sindicalizado** (marcador `-g4` no fim do slug; a MESMA pauta em muitos portais regionais —
  nove URLs em cinco consultas de jardinagem). É um ocupante, não dezessete, e é imbatível em quantidade:
  `litoralmania.com.br`, `acordacidade.com.br`, `leouve.com.br`, `jdv.com.br`, `obemdito.com.br`,
  `folhabv.com.br`, `bandab.com.br`, `gazetabrasilia.com.br`, `tnh1.com.br`, `ndmais.com.br`, `itatiaia.com.br`,
  `agazeta.com.br`, `crusoe.com.br`, `ellasmagazine.com.br`, `diariodonordeste.verdesmares.com.br`,
  `tribunadejundiai.com.br`, `folhavitoria.com.br`.
- **Conglomerado de imprensa rodando fazenda editorial** (várias páginas por consulta, títulos variados sobre o
  mesmo molde — **7 das 9 vagas de "como plantar quiabo" são do grupo Diários Associados**):
  `em.com.br/emfoco/`, `uai.com.br`, `correiobraziliense.com.br/cbradar/`, `tupi.fm`,
  `tudogostoso.com.br/noticias/`, `revistaoeste.com`, `catracalivre.com.br/noticias/`, `ecycle.com.br`.
- **Parasita puro** (domínio sem relação nenhuma com o nicho): `psicopedagogia.com.br` (adubo 10-10-10 **com o
  título exato da consulta**, e muda de rosa do deserto), `concursosnobrasil.com` (site de concursos públicos com
  **quatro** variações do mesmo título sobre suculenta), `lojadomecanico.com.br/blog` (**1º lugar** em "como fazer
  muda de orquídea"), `pacpme.com.br`, `cbzoo.com.br`, `hbatools2.com.br`, `blog.7mboots.com.br`,
  `capitalist.com.br`, `chavesnamao.com.br`.
- **Banco de FAQ ou de glossário gerado, uma página por pergunta ou por valor de parâmetro**:
  `mapaagro.com.br/glossario/`, e `faq.blackpilado.com.br` (já listado) aqui com **três URLs numa só SERP**, uma
  por fórmula de adubo.
- **Fazenda de jardinagem com título exato de consulta**: `casaeconstrucao.org`, `jardinagem.casaefesta.com`,
  `cultivarjardinagem.com.br`, `tudojardim.com`, `jardim.biz`, `decorfacil.com`, `enfeitedecora.com`,
  `terrabrasilnoticias.com`, `essaseoutras.com.br`, `passoapasso.com`, `casajardimsintonia.com.br`,
  `pepalantusambiental.com.br`, `antoniettasp.com.br`, `casa.umcomo.com.br`, `agron.com.br`,
  `hortasbiologicas.pt`.
- **Calculadora servindo o parâmetro central do nicho** — o molde da proposta de nota 0 por função, e aqui ele
  apareceu em três eixos de uma vez (dose de adubo, litros de terra por vaso, espaçamento de plantio):
  `textei.com.br`, `agrododia.com.br`, `plantaselar.com.br`, `ploys.com.br`, `calculadoradomundo.com.br`,
  `acalculadoras.com.br`, `casaejardim.portaltvcariri.com.br`, `calculover.com/pt-br`, `pt.jardineriaon.com`.
- **E uma loja que é o ocupante mais consistente do nicho, sem ser fazenda:** `petz.com.br/blog` apareceu em
  **4 das 5** consultas de "como fazer muda", com 5 das 10 vagas de "qual o tamanho do vaso" e 6 URLs numa só
  SERP de "como plantar uva em vaso" — sempre com o slug no título exato. Blog de loja no título exato é S_par 4
  pela régua, mas **blog de loja que ocupa metade da SERP não é 4**, e a régua não tem onde pôr isso. Registrado.

**TERCEIRO PADRÃO MEDIDO E NÃO APLICADO (rodada 007) — só o Raphael transforma em régua: VOLUME SEM POSIÇÃO NÃO É
TRÁFEGO.** A varredura de 21/10/2026 multiplicou volume do Planejador por CTR de **top-3** antes de medir quem
ocupa a SERP, e devolveu 2.530 visitas/dia para jardinagem. Medidas as 21 SERPs, a mesma conta no mesmo volume dá
**426** — erro de **fator 6**, vindo inteiro da premissa de posição. **Proposta:** a 3.0-c.2 passa a exigir, na
ordem, (1) classificar a SERP de pelo menos uma consulta por cluster, (2) só então aplicar o CTR da posição
classificada, e (3) proibir cenário de top-3 em cluster cuja SERP não foi vista com os olhos, por força da 30.8.
Varredura por volume continua valendo, mas o que ela devolve é **teto de volume**, e a rodada escreve isso ao lado,
nunca "visitas/dia". **Corolário de custo:** reprovar por posição custa uma rodada da nuvem; reprovar por volume
custa uma sessão do Raphael no Planejador — então a ordem natural é SERP primeiro, Planejador depois, ao contrário
do que a 006 e a varredura fizeram.

**DOIS PADRÕES QUE A RODADA 006 MEDIU E QUE SÓ O RAPHAEL PODE TRANSFORMAR EM RÉGUA — ficam registrados, não aplicados:**
1. **O molde `?p=<id>` sem slug apareceu em NOVE domínios distintos** numa só rodada (`olhardigital`, `maxturbos`,
   `digitei`, `uai`, `quintoandar/guias`, `calculadorabrasil`, `plataformaassaad`, `ecoautomacao`,
   `lojadomecanico/blog`). É WordPress publicando em massa sem nem gerar URL legível.
2. **A régua da nota 0 está velha.** Ela diz "calculadora de grande varejista instalada", e a seção 3 fala em
   fabricante. Mas quatro dos dez candidatos mortos na 006 foram mortos por calculadora que **não é nem de varejista
   nem de fabricante** — `size.ly` (numeração de calçado), `omnicalculator.com/pt` (tamanho de sutiã, 2º lugar),
   `miniwebtool.com/br` (tamanho de fralda e de ventilador de teto), `arvo.guru` (anilha, **nove de dez slots**). Pela
   letra, nada disso dispara nota 0, e os coletores tiveram de propor 1 para não extrapolar a lei. **Proposta: a nota 0
   passa a ser por FUNÇÃO — "a resposta paramétrica central do nicho já está em máquina, indexada e em português" —
   independentemente de quem seja o dono.**

## 4. Toda rodada reavalia o topo (SERP aberta fecha)

Antes de pontuar candidato novo, refaça a busca paramétrica dos **5 primeiros** da fila sem ilha nascida. Se entrou
fazenda, rebaixe S_par, registre a data e mova na fila. Aquarismo caiu de 1º para 12º em quatro dias (03→07/09/2026) —
nicho aprovado que fechou tem que ser desmarcado antes de alguém pagar domínio.

## 5. Cadência e o que a rodada entrega

> **BÚSSOLA PAUSADA EM 16/09/2026, por decisão do Raphael.** A rotina semanal está desligada e a meta de duas ilhas por semana **está suspensa**: são cinco ilhas na carteira e a Fundação tem ~20 execuções por semana, então achar nicho novo produz candidato para uma fila que não vaza. A cadência abaixo descreve o regime normal e volta a valer quando a Bússola for religada — o gatilho combinado é **uma ilha terminada e dando dinheiro**. Nada abaixo desta linha deve ser lido como ordem de nascer ilha enquanto esta pausa estiver escrita aqui.

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

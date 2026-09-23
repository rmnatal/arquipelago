/**
 * Aquametria Peixes — a malha do eixo /peixes/
 * Versão: 1.14.0 (23/09/2026) — PREPARAÇÃO DA LEVA 9: OS BARBOS GANHAM BANCO E A
 * NONA CATEGORIA PASSA A SER POSSÍVEL. NENHUMA URL NOVA — seguem 48 — e nenhuma
 * leva do teto da 21.4 gasta. O que muda nesta tela é só a contagem: o catálogo
 * embutido vai de 32 para 34 espécies, porque `Puntius titteya` (barbo cereja)
 * entrou no banco e `pethia-conchonius` (barbo rosado) saiu de `parcial` para
 * `conflito` ao ganhar o segundo corpo de fonte. São 3 barbos elegíveis, o
 * mínimo exato do 16.5 — os dois passos que a leva 8 nomeou na véspera.
 *
 *   A LISTA DE ESPÉCIES DA CATEGORIA CONTINUA SEM EXISTIR, e isso é preparo e
 *   não esquecimento: `barbos` NÃO foi declarada em aquametria_peixes_categorias()
 *   nem em aquametria_peixes_registro(). A preparação da leva 6 (v1.9.0) já tinha
 *   tentado preencher a lista de uma categoria antes da leva e foi REPROVADA na
 *   bancada; e a regra que a leva 5 deixou diz por quê — texto de categoria
 *   escrito antes da leva é afirmação contra uma tabela que ninguém viu. O
 *   `criterio` e a `linha_mestra` desta categoria nascem na execução que publicar
 *   as quatro URLs, contra a tabela que a página serve, como as levas 7 e 8
 *   fizeram.
 *
 *   O QUE A TABELA DELA JÁ DIZ, para quem escrever a leva: as três faixas
 *   térmicas são 18 a 22 °C (rosado), 20 a 26 °C (sumatra) e 23 a 27 °C (cereja)
 *   — a do rosado termina ANTES de a do cereja começar, e o sumatra é o único que
 *   encosta nas duas. É a segunda categoria seguida em que a coluna que decide é
 *   a temperatura, e aqui ela é uma escada de três degraus em vez do par que a
 *   `acaras` achou. E, ao contrário dos acarás, os três portes estão na MESMA
 *   régua (5,0 · 7,0 · 14,0 cm TL), então comparar porte aqui é legítimo.
 *
 *   E O CRITÉRIO NÃO PODE SER A FAMÍLIA, agora contado em vez de suposto:
 *   Cyprinidae tem QUATRO elegíveis sem categoria, e o quarto é o kinguio, que
 *   ninguém vende como barbo. Quem conta isso é
 *   `ferramentas/varrer-categorias-possiveis.py`, que nasceu nesta execução para
 *   matar a quarta lista escrita à mão desta família — a varredura que as levas 7
 *   e 8 fizeram de cabeça, cada uma com números diferentes.
 *
 * Versão: 1.13.0 (22/09/2026) — LEVA 8: A OITAVA CATEGORIA, E A PRIMEIRA EM QUE
 * O CRITÉRIO DA LEVA ANTERIOR FALHARIA. Quatro URLs novas: /peixes/acaras/ e as
 * fichas do acará-bandeira, do oscar e do acará-disco. A ilha vai de 44 para 48
 * URLs, e a família Cichlidae fica inteira publicada, repartida em duas
 * categorias.
 *
 *   O NOME NÃO SERVE DE CRITÉRIO AQUI, E ISSO SE MEDE. A leva 7 fechou
 *   comemorando um critério que era verificável DENTRO do banco: separar pelo
 *   nome que a pessoa digita, conferindo `nomes_populares_br`. Nesta categoria
 *   ele falha, e falha pelo lado caro — QUATRO registros do banco trazem
 *   "acará" entre os nomes populares, e o quarto é o `acará-borboleta`, que é o
 *   ramirezi e já é filha de `/peixes/ciclideos-anoes/` desde a leva 6. Um
 *   critério de nome tiraria uma filha da mãe dela. Critério bom não é o que
 *   funcionou na última vez: é o que sobrevive à varredura desta vez.
 *
 *   O QUE SERVE É O PORTE DECLARADO, e ele é número e não leitura: os três
 *   desta categoria começam em 13,7 cm de adulto e os três ciclídeos anões
 *   terminam em 5,6 cm. Entre 5,6 e 13,7 cm não existe um único Cichlidae neste
 *   banco — o corte atravessa um vão vazio de oito centímetros, então não é uma
 *   linha escolhida para caber no dado.
 *
 *   A LINHA MESTRA MUDOU DE COLUNA, e é a primeira vez no eixo. As sete
 *   categorias anteriores tinham faixas térmicas que se cruzavam, e a
 *   temperatura era dado de ficha sem nada a dizer na abertura. Aqui as faixas
 *   do oscar (22 a 25 °C) e do acará-disco (26 a 30 °C) NÃO SE TOCAM, as duas
 *   pela mesma base científica — então a comparação é legítima pela regra da
 *   leva 7, porque não há duas réguas, há uma só. Dois peixes que a loja põe na
 *   mesma prateleira e a SERP responde na mesma página não cabem no mesmo
 *   aquário, e nenhuma conta de litragem diz isso.
 *
 *   E O QUE A LINHA MESTRA NÃO DIZ É DELIBERADO: nada sobre porte comparado.
 *   Esta é a categoria com a MAIOR distância de porte do eixo (13,7 a 45,7 cm)
 *   e mesmo assim o número fica fora da frase, porque o acará-disco declara SL
 *   e os outros dois declaram TL. A regra da leva 7 vale contra a frase mais
 *   forte que esta página poderia publicar.
 *
 *   O TERCEIRO ESTADO DA AUSÊNCIA DE FUNDO GANHA O SEGUNDO CASO, e o primeiro
 *   que nasce sabendo. A 1.12.0 escreveu esse ramo consertando um defeito que
 *   esteve oito dias no ar (a ficha do apistogramma agassizi prometendo ao
 *   harém o chão do casal); a ficha do acará-disco nasce nele — o chão de
 *   120 × 45 cm foi declarado para juvenis ou um casal, o registro publica
 *   cardume de cinco, e a página diz a largura, diz para quem ela foi declarada
 *   e não abre as duas tabelas que dependem do fundo. É a diferença entre uma
 *   regra escrita por conserto e uma regra que já trabalha.
 *
 *   E OS TRÊS ESCOPOS DE CHÃO VIVEM NA MESMA CATEGORIA, o que nenhuma outra
 *   tem: `nao-declarado` no acará-bandeira, `um-exemplar` no oscar e
 *   `juvenis`+`casal` no acará-disco. O oscar é também a primeira ficha do eixo
 *   com `convivencia: solitario` cujo chão declarado COBRE o arranjo publicado
 *   — o betta também vive sozinho, e nele a fonte não diz para quem a base foi
 *   dada. Eram dois ramos da mesma função com um exemplar só.
 *
 *   UMA RÉGUA REPROVOU UMA PÁGINA CERTA, E O CONSERTO É DO CONTRATO. A
 *   afirmação "a palavra cardume não aparece no corpo" é da leva 4, escrita
 *   quando o betta era o único peixe de arranjo fixo da ilha, e procurava a
 *   palavra SOLTA no corpo inteiro. As três ocorrências no corpo do oscar eram,
 *   todas, o TÍTULO DE OUTRA PÁGINA dentro de um link — o degrau da trilha, a
 *   frase de mãe e o bloco "Veja também". Nenhuma delas diz uma palavra sobre o
 *   oscar, e apagar a palavra dos títulos seria mentir sobre a categoria e
 *   sobre o disco, que vive em cardume mesmo. A régua passou a medir o LUGAR e
 *   não a palavra solta, que é o que a 16.5 do ARQUIPELAGO.md manda com todas
 *   as letras — e a segunda metade dela impede o afrouxamento: toda ocorrência
 *   que sobra no corpo tem de ser, uma a uma, o título de outra página do eixo.
 *   Uma mutação nova prova a porta dos fundos.
 *
 * HISTÓRICO — versão 1.12.0 (22/09/2026) — O CHÃO DECLARADO GANHA DONO. Nenhuma
 * URL nova. `chao_declarado_para` (esquema de espécies versão 5) nasceu para a
 * base declarada viajar com o arranjo a que ela se refere, e com ele dois
 * defeitos saíram do ar: a ficha do apistogramma agassizi prometendo ao harém
 * os 30 cm de fundo que o compêndio declarou para um casal, e quatro fichas
 * atribuindo a base ao corpo de fonte errado.
 *
 * HISTÓRICO — versão 1.11.0 (22/09/2026) — LEVA 7: A SÉTIMA CATEGORIA, E A PRIMEIRA LEVA
 * DESTE EIXO QUE NÃO CUSTOU UMA COLETA. Quatro URLs novas:
 * /peixes/danios-e-rasboras/ e as fichas do paulistinha, da rasbora arlequim e
 * do tanictis. A ilha vai de 40 para 44 URLs.
 *
 *   O QUE FALTAVA ERA O LUGAR, NÃO O DADO. As três espécies passavam nos DOIS
 *   portões do esquema desde 11/09/2026 — estavam no catálogo, na contagem da
 *   seção e na lista de quem divide a mesma água — e não tinham página porque
 *   nenhuma das seis categorias do ARVORE.md as abrigava, e o documento fechava
 *   o eixo em "Seis, e só estas". Seis levas seguidas leram essa linha como o
 *   limite do eixo; ela era o limite do DOCUMENTO. Onze espécies elegíveis
 *   continuam sem categoria hoje pelo mesmo motivo, e isso está escrito no
 *   ESTADO.md como dívida nomeada, não como descoberta.
 *
 *   A CATEGORIA É A SEGUNDA DO EIXO EM QUE NEM A FAMÍLIA NEM O GÊNERO SERVEM,
 *   e ela falha pelo lado CONTRÁRIO ao dos ciclídeos anões: lá a família trazia
 *   peixe demais (Cichlidae carrega o oscar de 45,7 cm), aqui ela deixa peixe
 *   de FORA — o tanictis é a única Tanichthyidae do banco, família só dele, e
 *   o segundo nome popular brasileiro dele é `paulistinha-da-montanha`, que é o
 *   nome do peixe da linha de cima com um sobrenome. O que serve é o nome que a
 *   pessoa digita, e nesta categoria ele é verificável DENTRO do banco: os
 *   quatro registros declarados são exatamente os que trazem `danio`, `rasbora`
 *   ou `paulistinha` entre os nomes populares, e nenhum outro registro traz.
 *
 *   A LINHA MESTRA DESVIOU DE UMA ARMADILHA DE MEDIDA QUE AS SEIS ANTERIORES
 *   NÃO TINHAM, e é a lição desta leva. A primeira escrita dizia "o MENOR
 *   destes três é o que pede o MAIOR aquário" — a frase mais forte que esta
 *   página poderia publicar, e ela não se sustenta: o porte do paulistinha está
 *   declarado em SL (3,8 cm, o corpo sem a cauda) e o do tanictis em TL (4,0 cm,
 *   com ela). Na mesma régua a ordem entre os dois pode inverter, e a página
 *   estaria publicando como medição uma comparação que nenhuma das duas fontes
 *   fez. COMPARAR NÚMERO DE MEDIDAS DIFERENTES É A MESMA FAMÍLIA DA REGRA DA
 *   CONGÊNERE: parece medição e é vizinhança. A versão publicada diz o que a
 *   tabela paga com qualquer régua — os três portes cabem num intervalo de
 *   pouco mais de um centímetro, a frente varia em 30 cm e a frente POR
 *   INDIVÍDUO varia em três vezes — e a advertência de medida sai na página, na
 *   língua do leitor, ao lado da coluna de porte.
 *
 *   E UM DEFEITO QUE ESTAVA NO AR DESDE 14/09/2026 SAIU JUNTO, achado por esta
 *   leva ao conferir que as páginas novas eram medidas pelo portão da voz: a
 *   linha mestra de `/peixes/ciclideos-anoes/` dizia "o que dobra o AQUÁRIO",
 *   falando do mundo em terceira pessoa, e o VOZ.md manda falar com quem
 *   entrou. Ninguém viu porque a leva 6 acrescentou as quatro URLs ao
 *   `teste-peixes.py` e ESQUECEU do `teste-voz.mjs`, que tem lista escrita à
 *   mão e não avisa quem falta. Oito dias de página no ar com o portão verde.
 *   As duas listas do portão da voz ganharam as levas 6 e 7 nesta execução, e
 *   ele passou de 36 para 44 páginas — o site inteiro, pela primeira vez.
 *
 *   O NÚMERO DE CATEGORIAS DEIXOU DE SER DIGITADO. A afirmação dos cartões em
 *   `teste-peixes.py` cobrava `len(cartoes) == 6`, com a palavra "seis" no
 *   rótulo, e o ARVORE.md dizia "Seis, e só estas" na mesma linha. Nenhum dos
 *   dois era derivado do outro, então a sétima categoria reprovou numa régua
 *   SEM APONTAR DEFEITO NENHUM. A régua passa a LER a tabela do ARVORE.md, pelo
 *   mesmo desenho do `teste-arvore.mjs`: o documento manda, e categoria que
 *   entrar no código sem entrar nele reprova.
 *
 * HISTÓRICO — versão 1.10.0 (14/09/2026) — LEVA 6: A QUINTA CATEGORIA, E A PRIMEIRA EM QUE
 * AS TRÊS FILHAS VIVEM DE TRÊS JEITOS DIFERENTES. Quatro URLs novas:
 * /peixes/ciclideos-anoes/ e as fichas do ramirezi (casal), do apistogramma
 * agassizi (harém) e do papilocromis (grupo de 6 a 8). A ilha vai de 36 para
 * 40 URLs — que é o PISO DA RAMPA da seção 21.
 *
 *   AS QUATRO CATEGORIAS ANTERIORES TINHAM NO MÁXIMO DOIS ARRANJOS, e a
 *   `vivaparos` tinha um só. Esta tem os três que o vocabulário fechado
 *   permite numa categoria só, e por isso é a primeira em que a tabela de
 *   lotação percorre os três ramos da abertura lado a lado, na mesma tela.
 *
 *   E A FRENTE MÍNIMA DO PAPILOCROMIS É A PRIMEIRA DO EIXO QUE É CONDICIONAL:
 *   o compêndio não publica "aquário mínimo" solto, publica "grupo misto de 6
 *   a 8 ou mais DESDE QUE o aquário tenha 120 cm ou mais". Quebrar a frase em
 *   dois números seria publicar uma frente que a fonte nunca declarou sozinha
 *   — a mesma família do BASE contra FRENTE que a leva 2 consertou.
 *
 *   O BANCO, O CRITÉRIO, A LINHA MESTRA E A SERP desta categoria vieram da
 *   preparação de 1.9.0, na execução das 21h18Z do mesmo dia. Esta versão
 *   publica: preenche a lista `especies` da categoria e escreve as quatro
 *   entradas em `aquametria_peixes_registro()`. Nenhuma URL das levas 1 a 5
 *   muda, nenhum endereço se move.
 *
 * Versão: 1.9.0 (14/09/2026) — PREPARAÇÃO DA LEVA 6: A QUINTA CATEGORIA GANHA
 * BANCO, CRITÉRIO E LINHA MESTRA, E NENHUMA URL NASCE. Duas espécies novas no
 * banco (Apistogramma agassizii e Mikrogeophagus altispinosus) levam
 * `/peixes/ciclideos-anoes/` de UM elegível para TRÊS, que é o mínimo exato do
 * 16.5. A categoria continua FORA de `aquametria_peixes_registro()`, então
 * nenhuma URL foi criada e nenhuma leva do teto da 21.4 foi gasta: o que muda
 * na tela é a contagem do catálogo, de 29 para 31, que a seção e as categorias
 * imprimem na hora.
 *
 *   É A PRIMEIRA CATEGORIA DO EIXO EM QUE NEM A FAMÍLIA NEM O GÊNERO SERVEM
 *   de critério. Nos tetras a família não servia e o gênero resolvia; nas
 *   coridoras o gênero não servia e a subfamília resolvia; nas bettas e nos
 *   vivíparos a família serviu. Aqui Cichlidae carrega o oscar, o disco e a
 *   bandeira — deste mesmo banco — e o gênero Mikrogeophagus põe as duas
 *   PONTAS da tabela lado a lado. Quem separa é a prateleira brasileira, que
 *   tem endereço próprio em três lojas, e o porte declarado explica a
 *   prateleira: os três desta lista têm menos de 6 cm e o menor dos outros
 *   Cichlidae do banco tem 13,7 cm.
 *
 *   E A TABELA DESTA CATEGORIA PROVA A TESE DO EIXO COM DOIS PEIXES DE PORTE
 *   IDÊNTICO, coisa que nenhuma das outras quatro pode fazer: o ramirezi e o
 *   apistogramma agassizi têm os mesmos 4,2 cm SL na mesma base científica e
 *   pedem os mesmos 60 cm; o papilocromis tem 5,6 cm — 1,4 cm a mais — e pede
 *   120. O que dobra o aquário é o ARRANJO (casal, harém e grupo de 6 a 8),
 *   não o tamanho do peixe.
 *
 * Versão: 1.8.0 (14/09/2026) — LEVA 5: A QUARTA CATEGORIA, E A PRIMEIRA EM QUE
 * NENHUMA FILHA TEM NÚMERO DECLARADO. Quatro URLs novas: /peixes/vivaparos/ e as
 * fichas do platy, do peixe-espada e do plati variatus. A ilha vai de 32 para
 * 36 URLs.
 *
 *   O QUE A CATEGORIA CUSTOU, e de novo não foi preencher a lista. As três
 *   vivem em `harem`, e harém é o único valor do vocabulário fechado em que a
 *   fonte descreve a PROPORÇÃO entre os sexos — mais fêmeas do que machos, para
 *   dissipar o assédio — e nunca o tamanho do grupo. A leva 4 escreveu os três
 *   mundos da escada de lotação e publicou dois; o terceiro, o do arranjo sem
 *   número, ficou como ramo de RESGATE, e ramo de resgate é régua que não pode
 *   falhar.
 *
 *   ELE ESTAVA ERRADO, e do jeito exato que o contrato prevê: abria pela
 *   tradução do `como_vive()`, que carrega a oração do temperamento. A primeira
 *   frase da ficha do platy sairia como "Para o platy, que vive em harém, um
 *   macho para várias fêmeas, E A FONTE O DECLARA PACÍFICO, o seu aquário
 *   precisa de..." — procedência abrindo a página, que é o que o item 4 do
 *   despacho da Sentinela de 13/09/2026 tirou das onze fichas antigas (15.2).
 *   O ramo virou branch com nome, com abertura própria no mapa do arranjo, e o
 *   resgate deixou de existir: `aquametria_peixes_pode_virar_ficha()` passa a
 *   exigir que o termo esteja no vocabulário fechado, que é o que o cabeçalho
 *   da 1.7.0 já afirmava e o código não fazia — bastava `cardume_minimo`
 *   preenchido para uma `convivencia` qualquer virar página chamando o peixe de
 *   cardume.
 *
 *   E DOIS DEFEITOS QUE JÁ ESTAVAM NO AR SAÍRAM JUNTO, os dois de CONCORDÂNCIA,
 *   os dois medidos no HTML servido em 14/09/2026:
 *
 *   1. "1 ficaram fora porque o banco OS declara agressivoS" — a frase da
 *      prestação de contas nasceu plural e o banco tem UM peixe agressivo, o
 *      mato-grosso. Até esta leva ele ou aparecia junto com o betta (dois) ou
 *      não aparecia (zero, e a frase nem sai); a coridora sterbai já servia a
 *      versão errada desde 12/09. Nasceu `aquametria_peixes_concorda()`.
 *
 *   2. "cabem 1 coridora sterbai ... A diferença entre os dois é de 4 vezes" —
 *      duas coisas na mesma frase. O verbo, e o número: o "4 vezes" saía das
 *      CONSTANTES (4 L/cm contra 1 cm/L), e a razão entre as réguas só é a razão
 *      entre os NÚMEROS DA TELA enquanto o arredondamento para baixo não morde.
 *      Ele mordia em DEZ das quatorze fichas no ar — 4,2 no cardinal, 5 no
 *      tetra-negro, 5,5 no gurami mel, 6 na sterbai — e morde mais no
 *      peixe-espada, que com 16 cm é o maior peixe com ficha da ilha: a linha do
 *      meio dá 7 e 1, que é SETE vezes, com a frase anunciando quatro a uma
 *      linha de distância dos dois números que a desmentem. É o escopo de
 *      afirmação da seção 8: a frase fala do que ela imprimiu, e agora a razão é
 *      derivada dos dois números impressos.
 *
 *   A LINHA MESTRA DA CATEGORIA FOI REESCRITA NA LEVA QUE A PUBLICOU, pelo mesmo
 *   motivo que a da `bettas`: a de 13/09 prometia um número que a página não
 *   paga — "quantos vão existir daqui a três meses, e o macho é quem manda nessa
 *   conta" —, e nenhuma fonte deste banco declara taxa de reprodução. Pior: ela
 *   dizia que manda o MACHO e o critério logo abaixo dizia que manda a FÊMEA, as
 *   duas na mesma tela e nenhuma medida. O critério também perdeu a frase da
 *   fêmea: dos três registros, dois declaram o porte da fêmea e o do plati
 *   variatus não declara sexo nenhum. O que as duas dizem agora é o que a tabela
 *   paga linha a linha — o arranjo sem número, e a frente que varia em duas
 *   vezes DENTRO de um gênero só.
 *
 *   A CATEGORIA DECLARA AS CINCO POECILIIDAE, e aqui os dois barrados não são
 *   vizinhança: são o guppy e o molly, os dois vivíparos MAIS vendidos do
 *   Brasil, cada um a UM campo de entrar. Saem na página com nome e causa.
 *
 *   A SERP DA MÃE FOI CLASSIFICADA EM 14/09/2026 e é a única do eixo em que o
 *   top 7 não fala do assunto: devolve as páginas genéricas de "quantos peixes
 *   cabem no aquário", com a regra por centímetro em três versões que discordam
 *   entre si e o "10 litros vagos + 5 litros por peixe" — a conta per capita que
 *   esta ilha recusa desde a leva 1. As três fichas seguem com `serp_em`
 *   13/09/2026, que é quando elas foram medidas.
 *
 *   E UMA TROCA DE TELA NO BANCO, declarada, pelo precedente da colisa-anão: os
 *   nomes populares do `xiphophorus-hellerii` foram reordenados para pôr
 *   "peixe-espada" na frente. `aquametria_peixes_nome()` lê o PRIMEIRO do campo e
 *   é ele que vai para o título, para o corpo e para a tabela da categoria; a
 *   consulta classificada é "quantos litros para peixe espada", e "espada"
 *   sozinho é ambíguo fora do aquarismo.
 *
 * HISTÓRICO — versão 1.7.0 (14/09/2026) — LEVA 4: A TERCEIRA CATEGORIA DO EIXO, E O EIXO
 * APRENDE QUE PEIXE NEM SEMPRE VIVE EM CARDUME. Quatro URLs novas:
 * /peixes/bettas/ e as fichas do betta, da colisa-anão e do gurami mel.
 *
 *   O QUE A CATEGORIA CUSTOU EM CÓDIGO, e não era o que parecia. Preencher a
 *   lista de espécies da `bettas` é uma linha; o que esta leva pagou foi outra
 *   coisa. Até 13/09/2026 as ONZE fichas no ar eram `convivencia: cardume`, sem
 *   exceção — e por isso a palavra "cardume" estava DIGITADA em sete lugares do
 *   corpo da ficha: a abertura, a legenda da tabela de lotação, o contraexemplo
 *   do cubo, a chamada do filtro, o bloco da espécie agressiva, a linha da
 *   tabela de fontes e o rabicho do JSON-LD. Era verdade em toda página
 *   publicada e é FALSA em três das quatro desta leva: o betta vive sozinho, a
 *   colisa-anão vive em casal e o gurami mel vive em grupo — e a fonte dele
 *   escreve, com todas as letras, que a espécie NÃO é gregária no sentido dos
 *   peixes de cardume.
 *
 *   É a cicatriz da seção 8 do ARQUIPELAGO.md em estado puro, no lado que ela
 *   chama de "régua escrita para um mundo que nunca aconteceu": o esquema desta
 *   ilha permite `solitario`, `casal`, `harem` e `grupo` desde o primeiro dia —
 *   `aquametria_peixes_pode_virar_ficha()` cita os três primeiros PELO NOME — e
 *   o banco nunca tinha produzido um. Nenhum portão podia falhar, e nenhum
 *   falhou.
 *
 *   O VOCABULÁRIO É FECHADO e mora num mapa só, `aquametria_peixes_arranjo()`.
 *   Termo fora dele devolve null e a espécie não vira ficha: inventar coletivo
 *   para valor novo é pior que não publicar.
 *
 *   DUAS RECUSAS QUE A LEVA ESCREVEU:
 *
 *   1. A ESCADA DE LOTAÇÃO SÓ SOBE ONDE A FONTE DEIXA. No betta, a fonte
 *      declara um por aquário; a tabela pré-renderizada de "N exemplares"
 *      subiria até 20, oferecendo com cara de tabela exatamente o número que a
 *      fonte recusa — e a tabela é a metade que um modelo de linguagem lê. Onde
 *      o arranjo FIXA o número (solitário 1, casal 2) a escada tem um degrau e
 *      a página diz por quê; onde a fonte declara um número de grupo, começa
 *      nele; onde declara o arranjo e não o número (harém), a escada é a de
 *      leitura e NENHUMA linha se chama mínima.
 *
 *   2. O CONSELHO DO BLOCO DA ESPÉCIE AGRESSIVA SE INVERTE COM O ARRANJO. "Quanto
 *      maior o cardume, menos a agressão se concentra num alvo só" é certo para
 *      o mato-grosso e é o CONTRÁRIO do que a fonte diz do betta, que é
 *      agressivo E solitário: ali ela manda um por aquário. E a frase antiga
 *      ainda iria ao ar quebrada, porque `$card` é nulo nessa espécie —
 *      "cardume mínimo de  e não de dois".
 *
 *   O DEFEITO QUE JÁ ESTAVA NO AR, e saiu junto: `/peixes/corydoras/` servia
 *   "fechada quer dizer que todo TETRA que o banco desta ilha sustenta já tem a
 *   página dele". Medido no HTML servido em 14/09/2026. É a mesma cicatriz do
 *   "São 4 tetras" que a leva 3 pegou ANTES de publicar, escondida um nível mais
 *   fundo: ela mora num ramo que só é alcançado quando a categoria FECHA, e até
 *   12/09 só os tetras tinham fechado. Ramo novo herda o texto do mundo antigo.
 *   O sujeito agora vem declarado por categoria, como o `plural`; e o exemplo da
 *   pergunta do nível 2, que era "quantos litros para dez neons" digitado em
 *   toda categoria, passa a ser a consulta da própria página.
 *
 *   A FAIXA DO GRUPO, e ela custou um campo de esquema (versão 4). O compêndio
 *   recomenda, do gurami mel, "não menos que 4 a 6 exemplares". O piso morava em
 *   `cardume_minimo` desde 13/09 e o teto não tinha onde morar — a ficha
 *   publicaria metade da recomendação, e completá-la de cabeça seria inventar a
 *   metade que falta. Nasceu `cardume_recomendado_ate`, o número sai da MESMA
 *   sentença já transcrita em `fontes[]` (sem passada nova de coleta) e o
 *   validador ganhou a regra E18. O teto declarado é DEGRAU da tabela, sempre: a
 *   escada de leitura (6, 8, 10…) só por acaso carrega o segundo número de "4 a
 *   6", e numa faixa "5 a 7" o 7 não apareceria em linha nenhuma.
 *
 *   A CATEGORIA DECLARA AS CINCO OSPHRONEMIDAE, e não só as três que passam.
 *   Esse é o primeiro mundo REAL do ramo de barrados que a 1.6.0 escreveu em
 *   13/09 sem ter caso no banco para exercitá-lo: os dois guramis grandes têm
 *   duas fontes cada e o portão os barra por `convivencia`, então saem na página
 *   com nome e causa. Sem declará-los, a frase de lista fechada diria que todo
 *   betta e todo gurami que o banco sustenta já tem página — e o banco sustenta
 *   os dois. As quatro mutações que PRODUZIAM aquele mundo continuam, porque
 *   agora elas provam o ramo VAZIO da mesma régua.
 *
 *   AS QUATRO PÁGINAS DECLARAM `serp_em` => '13/09/2026', que é o primeiro uso
 *   real do campo nascido na 1.3.0: quem não declara herda 12/09/2026, e isso
 *   seria mentira nestas quatro.
 *
 *   E UMA TROCA DE TELA NO BANCO, declarada: os nomes populares da colisa foram
 *   reordenados para pôr "colisa-anão" na frente. `aquametria_peixes_nome()` é
 *   documentada como "o nome que a pessoa digita" e lê o PRIMEIRO do campo — e a
 *   classificação de SERP de 13/09 mediu que a consulta brasileira é "quantos
 *   litros para colisa anão". Com "colisa" na frente, o título da ficha e o corpo
 *   dela serviriam nomes diferentes a uma linha de distância.
 */


/**
 * Aquametria Peixes — a malha do eixo /peixes/
 * HISTÓRICO — versão 1.6.0 (13/09/2026): A PRESTAÇÃO DE CONTAS DA SEÇÃO 7 ALCANÇA QUEM
 * NÃO ESTÁ NA TABELA. Nenhuma URL nova, nenhuma página criada: o que muda é o
 * que a seção e as categorias conseguem dizer sobre o próprio banco.
 *
 *   O BURACO, E ELE ERA ESTRUTURAL. O catálogo embutido carregava só quem PASSA
 *   no portão, então os barrados não existiam dentro do snippet. A seção servia
 *   "são 29 espécies" e não tinha como dizer que o banco tem 37, nem por que os
 *   outros 8 não estão ali — não por descuido de texto, mas porque o dado não
 *   chegava à página. A regra da seção 7 do `ARQUIPELAGO.md` ("cada item da
 *   categoria consultada aparece exatamente uma vez na prosa da resposta — ou
 *   na frase que o recomenda, ou numa linha que diz por que ele não está")
 *   estava cumprida para quem está na tabela e para mais ninguém, e ausência
 *   sem nome, numa página que fala do próprio banco, é indistinguível de
 *   espécie que a ilha nunca procurou.
 *
 *   O QUE PASSOU A EXISTIR. `ferramentas/gerar-catalogo-especies.py` escreve um
 *   SEGUNDO bloco, `aquametria_peixes_barrados()`, com o registro barrado, a
 *   família e o motivo em CÓDIGO — e a tradução do código para a língua do
 *   leitor mora em `aquametria_peixes_motivo_na_tela()`, num mapa só. O
 *   vocabulário de códigos é fechado nos dois lados e o gerador RECUSA gravar
 *   código fora dele: regra nova de portão que chegasse à tela como
 *   `comprimento_minimo_aquario_cm` seria vocabulário de dentro da fábrica na
 *   cara de quem lê.
 *
 *   UM DEFEITO LATENTE SAIU JUNTO, e ele é filho da mesma mudança: o cartão de
 *   categoria da seção virava link quando a categoria DECLARAVA espécie.
 *   Enquanto o snippet só conhecia quem passa, declarar e entrar na tabela eram
 *   a mesma coisa; com os barrados aqui dentro deixaram de ser, e uma categoria
 *   que declarasse só barradas viraria link para uma página de tabela vazia —
 *   a página fina que o 16.5 existe para não deixar entrar no índice de domínio
 *   novo. Quem decide o link passou a ser a contagem de quem está no catálogo.
 *
 *   E A FRASE "ESTA LISTA ESTÁ FECHADA" GANHOU A FORMA QUE FALTAVA. Com uma
 *   barrada declarada na categoria ela ficaria falsa sem mudar uma letra, que é
 *   a forma mais silenciosa do número de tela que envelhece.
 *
 *   Medem isso `ferramentas/teste-peixes.py` (1246 → 1302 afirmações, com régua
 *   própria que recomputa o portão e os motivos do banco, sem importar nada do
 *   gerador), `ferramentas/mutacoes-peixes.py` (46 → 56, e QUATRO delas produzem
 *   o mundo, porque nenhuma categoria no ar declara barrada hoje) e
 *   `ferramentas/conferir-peixes-no-ar.py`, no HTML que o servidor devolve.
 *
 * Versão: 1.5.0 (13/09/2026) — A CATEGORIA DOS VIVÍPAROS ALCANÇA O MÍNIMO DO
 * 16.5 E GANHA CRITÉRIO ESCRITO, com a lista de espécies ainda vazia. Nenhuma
 * URL nova: é a mesma preparação que a `bettas` recebeu na 1.3.0, agora na
 * categoria seguinte da ordem, e o que a destravou foi um registro de banco.
 *
 *   O QUE MUDOU DE ESTADO. `/peixes/vivaparos/` tinha DOIS elegíveis (platy e
 *   espada) e o 16.5 pede três; com `xiphophorus-variatus` no banco passa a ter
 *   três, que é o mínimo exato, sem folga — a mesma posição em que a `bettas`
 *   está. As duas espécies que estavam a UM campo de entrar continuam fora, e
 *   as duas recusas de 13/09/2026 estão escritas nos registros delas: o molly
 *   (`poecilia-sphenops`) porque os DOIS corpos de fonte foram perguntados e
 *   nenhum entrega a frente mínima, e o guppy (`poecilia-reticulata`) porque
 *   suas duas urls são do mesmo corpo (aviso E15).
 *
 *   O CRITÉRIO DESTA CATEGORIA PRESTA CONTAS DE QUEM FICOU FORA, e é por isso
 *   que ele é mais longo que o rótulo: as três que podem ter página hoje são
 *   todas `Xiphophorus`, e as duas `Poecilia` do banco — os dois vivíparos que
 *   o Brasil vende MAIS — estão de fora. Categoria que se chama "Vivíparos" e
 *   serve só um gênero tem de dizer isso na primeira linha, do mesmo jeito que
 *   a `bettas` diz que junta um peixe solitário, um de casal e um de grupo.
 *
 *   A CLASSIFICAÇÃO DE SERP DA 14.9 FOI MEDIDA ANTES, em 13/09/2026, nas três
 *   consultas das fichas: as três são ALVO. A data está na régua de `serp_em`
 *   abaixo; o que cada SERP tem está no `REGISTRO.md` desta execução e no
 *   `ARVORE.md`, que é onde a categoria seguinte vai buscá-la.
 *
 * Versão: 1.4.0 (13/09/2026) — A FICHA PARA DE ABRIR PELA PROVA, E O `Article`
 * GANHA DATA, AUTOR E PUBLICADOR. Itens 2 e 4 do despacho da Sentinela de
 * 13/09/2026, e os dois eram o mesmo defeito visto de dois lados: a página que
 * mais depende de procedência com data era a que citava a fonte onde não devia e
 * a que não declarava data onde devia.
 *
 *   ITEM 4, a VOZ. As onze fichas começavam por "Para os N <peixe> que A FONTE
 *   DECLARA como cardume mínimo ... e A FONTE DECLARA a BASE, não o litro" — duas
 *   menções à fonte na primeira frase, contra a 15.2 e contra a régua que o bloco
 *   de 11/09 fixou, "procedência não abre página". A prova não foi apagada: ela
 *   já estava duas telas abaixo, na tabela "O que as fontes declaram", com o
 *   corpo e a data de cada linha. O que a reescrita tinha de preservar é a
 *   decisão 7 deste cabeçalho, e ela continua inteira sem a palavra "fonte" —
 *   ver a atualização escrita ali.
 *
 *   ITEM 2, o SCHEMA. O `Article` das onze trazia `headline`, `about`,
 *   `inLanguage`, `isAccessibleForFree` e `mainEntityOfPage`, e nada mais — sem
 *   `datePublished`, `dateModified`, `author` nem `publisher`, que o `Article`
 *   dos três artigos já declarava. As duas datas vêm de
 *   `aquametria_casca_data_da_pagina()` (casca 1.8.0), do post servido, e não de
 *   um campo novo do registro: nenhuma das onze declara data de publicação em
 *   lugar nenhum do repositório, então o post é a única coisa que sabe — e
 *   escrever a data da leva à mão seria a constante do item 1 renascendo na
 *   página vizinha.
 *
 * Medem isso `ferramentas/teste-datas-schema.py`, `ferramentas/mutacoes-datas.py`
 * (12 de 12), a régua de atribuição nova do `ferramentas/teste-voz.mjs` e as
 * duas afirmações de estrutura que ele passou a fazer sobre a abertura da ficha.
 *
 * Versão: 1.3.0 (13/09/2026)
 *
 * T4 do PROMPT.md, leva 1: cinco URLs novas no eixo que a Bússola verificou
 * ABERTO e que é o de maior volume de busca da ilha — "quantos litros para X
 * peixes". Nível 1 `/peixes/`, nível 2 `/peixes/tetras/` e três fichas de
 * nível 3, na ordem do 16.6 (a mãe e as três primeiras filhas de maior
 * intenção, nunca uma filha de cada categoria espalhada).
 *
 * A TESE DESTA LEVA, e é ela que justifica a página existir: AS FONTES
 * DECLARAM A BASE DO AQUÁRIO, NÃO O LITRO. As sete primeiras respostas da
 * SERP brasileira (medidas em 12/09/2026, ver `consulta` de cada ficha) dão
 * litro sem fonte — "8 a 10 neons em 40 litros", "3 a 5 litros por neon" — e
 * discordam entre si. O banco desta ilha tem, para cada espécie, a base mínima
 * declarada por compêndio com nome e data, e as duas réguas brasileiras de
 * lotação com a atribuição de cada extremo. A página serve as duas coisas lado
 * a lado, e é isso que nenhum dos sete serve.
 *
 * SEIS DECISÕES, e nenhuma é de estilo:
 *
 *   1. NENHUM NÚMERO DESTA PÁGINA É DIGITADO. Frente mínima, litro por altura,
 *      lotação pelos três critérios, quantas espécies têm ficha, quantas estão
 *      no banco: tudo sai do catálogo gerado do banco, contado na hora de
 *      imprimir. É a cicatriz de 11/09 (seção 8): número de tela que era
 *      verdade no dia em que foi escrito mente em silêncio no dia seguinte.
 *
 *   2. A FRENTE MÍNIMA NÃO SE EXTRAPOLA POR INDIVÍDUO. O esquema do banco
 *      declara o derivado `frente_por_individuo_cm` (frente mínima ÷ cardume
 *      mínimo) e ele sai na tela como leitura per capita do mínimo declarado —
 *      mas NUNCA multiplicado para "quantos cm para 10 peixes". Os 60 cm que a
 *      fonte declara para 5 neons são o piso de onde o cardume consegue nadar
 *      em cardume, não o preço de cinco peixes: multiplicar daria 120 cm para
 *      dez neons, que contradiz todas as fontes e seria regra de bolso nossa
 *      com cara de dado. Quem responde "e para dez?" são os três critérios de
 *      lotação, que é exatamente para isso que eles existem.
 *
 *   3. CONFLITO DECLARADO SAI COM OS DOIS EXTREMOS E O NOME DE CADA UM. O
 *      mato-grosso tem 60 cm na FishBase e 80 cm no Seriously Fish; o cardinal
 *      tem 2,5 e 3,0 cm de porte. A ilha nunca tira média (rodapé da casca), e
 *      onde o número entra em conta a página usa o extremo SEGURO — aquário
 *      maior, peixe maior — e diz que escolheu e por quê.
 *
 *   4. ESPÉCIE NÃO É PRODUTO, então aqui não tem bloco de compra — e a página
 *      DIZ isso, porque silêncio parece defeito (seção 7). Peixe vivo não se
 *      vende por link de afiliado, e o equipamento que o cardume pede sai nas
 *      calculadoras, onde a vitrine já existe. As fichas linkam C1, C5 e C3
 *      pelo corpo, que é o 16.4(d) e é também o caminho do dinheiro.
 *
 *   5. A LISTA DE QUEM DIVIDE A ÁGUA NÃO É VEREDITO DE CONVIVÊNCIA. O esquema
 *      do banco recusa compatibilidade como campo booleano, de propósito:
 *      convivência depende de volume, de layout e de ordem de introdução. O
 *      que a página publica é o que ela mede — interseção das faixas de
 *      temperatura declaradas, com o critério escrito na frente da lista — e
 *      quem o banco declara agressivo fica fora com o nome na tela.
 *
 *   7. A SEGUNDA CATEGORIA (leva 3, 12/09/2026) SEPAROU O DECLARADO DO
 *      DIGITADO. Enquanto /peixes/tetras/ foi a única mãe de nível 2, três
 *      coisas eram indistinguíveis de suas versões corretas: "a mãe" e "a mãe
 *      certa"; "as fichas do eixo" e "as fichas desta categoria"; e o
 *      substantivo da abertura, que era a palavra "tetras" escrita no meio do
 *      HTML ao lado de uma contagem derivada. A primeira renderização de
 *      /peixes/corydoras/ serviu "São 4 tetras" — contagem certa, substantivo
 *      mentindo —, e o portão pegou antes do ar porque a régua do teste passou
 *      a declarar o rótulo em vez de derivá-lo do slug. Agora `plural` e
 *      `linha_mestra` moram na declaração da categoria, junto do `criterio`.
 *
 *   6. O JSON-LD SAI NO wp_head, NUNCA no retorno do shortcode. O retorno
 *      atravessa os filtros do the_content, que trocam "&" pela entidade
 *      numérica e quebrariam o JSON do mesmo jeito que quebraram o JavaScript
 *      das cinco calculadoras em 08/09/2026.
 *
 *   7. A PÁGINA SÓ AFIRMA O QUE A FONTE DECLAROU, E "BASE" NÃO É "FRENTE"
 *      (leva 2, 12/09/2026). A linha mestra da ficha terminava sempre em "e a
 *      fonte declara a BASE, não o litro". Era verdade nas três fichas da leva
 *      1, porque as três têm `base_minima_cm` preenchida — e é falsa em 14 dos
 *      36 registros do banco, onde a fonte declara só o COMPRIMENTO mínimo e
 *      nunca disse uma palavra sobre o fundo. O rodóstomo, desta leva, é o
 *      primeiro caso: o Seriously Fish declara "no mínimo 90 cm de
 *      comprimento" e ponto. Nesses registros a frase passa a dizer
 *      COMPRIMENTO, as duas tabelas que dependem do fundo não saem — e a
 *      página DIZ que não saíram e por quê, em vez de simplesmente encolher.
 *      Sumiço silencioso de tabela é a forma disfarçada do "silêncio parece
 *      defeito" da seção 7: quem lê não tem como saber se a ilha não sabe ou
 *      se esqueceu.
 *      ATUALIZADO EM 13/09/2026 (item 4 do despacho da Sentinela): a distinção
 *      continua inteira e mudou de palavras. A frase não diz mais QUEM
 *      declarou — a 15.2 proíbe procedência no primeiro parágrafo, e a tabela
 *      "O que as fontes declaram" já traz cardume e base com o corpo e a data
 *      de cada um. O que distingue os dois casos na tela agora são duas coisas
 *      que não precisam da palavra "fonte": o trecho "por Y cm de fundo", que
 *      só existe quando há fundo declarado, e a palavra final, BASE ou
 *      COMPRIMENTO. Quem tem só o comprimento diz que o fundo FICA EM ABERTO.
 *
 *   8. ESPÉCIE DE CARDUME SEM O NÚMERO DO CARDUME NÃO VIRA FICHA. O título
 *      deste eixo é "quantos litros para um cardume de X" e a linha mestra
 *      abre por "para um cardume mínimo de N X" (até 13/09/2026, "para os N X
 *      que a fonte declara como cardume mínimo" — ver a nota 7). Sem N a
 *      página caía num ramo que escrevia a frase sem o número e abria a tabela
 *      pré-renderizada em UM exemplar — numa página que, duas telas abaixo,
 *      diz que a espécie só vive em grupo. O esquema já cobrava esse número no
 *      portão da C8 desde que o banco nasceu; o que faltava era a página
 *      cobrar o mesmo, com a mesma frase. `aquametria_peixes_pode_virar_ficha()`
 *      é a régua DESTE lado, escrita aqui e não importada do gerador — quem
 *      confere escreve a própria régua (seção 8 do contrato).
 *
 * O QUE ESTE SNIPPET NÃO FAZ: criar página. Quem cria é a casca, pelo filtro
 * `aquametria_paginas` (casca 1.7.0) — inclusive o pai de cada uma, que é o que
 * faz a URL mostrar os três níveis da seção 16.1.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'AQUAMETRIA_PEIXES_VERSAO' ) ) {
	define( 'AQUAMETRIA_PEIXES_VERSAO', '1.14.0' );
}

/* A data em que a SERP das consultas foi classificada (seção 14.9).
   ESTA CONSTANTE DEIXOU DE SER A ÚNICA FONTE DA DATA em 13/09/2026, e o
   próprio comentário anterior tinha previsto o dia: "se uma leva futura sair
   em outro dia, esta constante deixa de servir para todas e vira campo do
   registro". O dia chegou antes da leva — a classificação das quatro consultas
   de `/peixes/bettas/` foi medida em 13/09/2026, e as doze páginas no ar
   continuam classificadas em 12/09/2026. As TRÊS consultas de
   `/peixes/vivaparos/` também foram medidas em 13/09/2026, mais tarde no mesmo
   dia — e a coincidência de data entre as duas categorias é o argumento contra
   voltar a confiar na constante: duas medições do mesmo dia não são a mesma
   medição, e a página que herdar a data de outra não tem como mostrar isso.

   Ela continua existindo como PADRÃO, e não por compatibilidade: doze páginas
   repetirem a mesma data doze vezes é a mesma data escrita doze vezes, que é
   o defeito que ela nasceu para impedir. Quem tem data própria declara
   `serp_em` no registro; quem não declara herda esta. Lê os dois lados
   `aquametria_peixes_serp_em()`, e é ela — nunca a constante — que as páginas
   chamam. */
if ( ! defined( 'AQUAMETRIA_PEIXES_SERP_EM' ) ) {
	define( 'AQUAMETRIA_PEIXES_SERP_EM', '12/09/2026' );
}

/**
 * A data em que a SERP da consulta desta página foi classificada.
 *
 * O campo `serp_em` do registro quando ele existe; a constante quando não.
 * Nenhuma página imprime a constante direto: se imprimisse, a página com data
 * própria continuaria servindo a data das outras e o defeito seria invisível
 * justamente na página que ele afeta.
 */
if ( ! function_exists( 'aquametria_peixes_serp_em' ) ) {
function aquametria_peixes_serp_em( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( isset( $registro[ $slug ]['serp_em'] ) && '' !== $registro[ $slug ]['serp_em'] ) {
		return $registro[ $slug ]['serp_em'];
	}
	return AQUAMETRIA_PEIXES_SERP_EM;
}
}

/* As duas réguas brasileiras de lotação, com o extremo de cada uma. Vêm de
   `dados/constantes-calculadoras.json` (lotacao-1cm-por-litro e
   lotacao-litros-por-cm), colhidas em 04/09/2026 no levantamento do Bloco 1.
   Estão aqui em CONSTANTE e não no meio de uma função porque é o que muda de
   ilha para ilha, e porque a tela precisa nomear quem publicou cada extremo. */
if ( ! defined( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA' ) ) {
	define( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA', 1.0 );   // 1 cm de peixe por litro
	define( 'AQUAMETRIA_PEIXES_LOTACAO_MEIO', 1.5 );       // 1,5 L por cm de peixe
	define( 'AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA', 4.0 ); // 4 L por cm de peixe
}

/* ---------------------------------------------------------------------------
 * 1. O catálogo — gerado do banco, nunca editado à mão
 *
 * `ferramentas/gerar-catalogo-especies.py` reescreve o bloco abaixo. Só entra
 * quem passa no portão de página do esquema (sete campos e duas fontes de
 * corpos distintos), e nada derivado é gravado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_catalogo' ) ) {
function aquametria_peixes_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */
	static $catalogo = null;
	if ( null !== $catalogo ) {
		return $catalogo;
	}
	$catalogo = array(
		'hyphessobrycon-amandae' => array(
			'id' => 'hyphessobrycon-amandae',
			'cientifico' => 'Hyphessobrycon amandae',
			'sinonimos' => array(),
			'populares' => array(
				'tetra ember',
				'tetra fogo',
				'ember tetra',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => 'América do Sul: bacia do rio Araguaia',
			'porte_cm' => 2,
			'porte_medida' => 'SL',
			'cardume' => 8,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 20,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/12376',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
					),
					'referencia' => 'FishBase - ficha da especie: max length 2,0 cm SL macho/nao-sexado; tropical, 24 a 28 C; familia Acestrorhamphidae (tetras americanos); America do Sul, bacia do rio Araguaia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hyphessobrycon-amandae',
					'em' => '2026-09-11',
					'campos' => array(
						'temperatura_C',
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'convivencia',
						'comportamento',
					),
					'referencia' => 'Seriously Fish - ficha da especie: aquario com base de no minimo 45 x 30 cm (18 x 12 pol) ou equivalente; temperatura de 20 a 28 C, com a agua de pH levemente acido a neutro e a temperatura na ponta ALTA da faixa; gregaria e formando cardume por natureza, com a compra minima recomendada de 8 a 10 exemplares, porque em numero menor fica arisca; muito pacifica, nao compete com companheiros agitados ou bem maiores.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'temperatura_C',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 24,
								'max' => 28,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: tropical, 24 a 28 C',
						),
						array(
							'valor' => array(
								'min' => 20,
								'max' => 28,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: 20 a 28 C, com a recomendacao de manter na ponta alta da faixa',
						),
					),
					'razao' => 'Temperatura e campo de MANUTENCAO, e a tabela dominio_por_campo poe o compendio acima da base cientifica justamente nesses campos: a FishBase descreve a agua onde o peixe vive, o compendio descreve a agua em que ele e mantido. As duas faixas nao se contradizem - 24 a 28 cabe dentro de 20 a 28 -, e o piso mais baixo e uma permissao do compendio, nao uma recomendacao: a mesma frase manda ficar na ponta alta. Quem dimensiona aquecedor pelo piso de 20 C encomenda mais potencia, que e o lado seguro do erro.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'paracheirodon-innesi' => array(
			'id' => 'paracheirodon-innesi',
			'cientifico' => 'Paracheirodon innesi',
			'sinonimos' => array(),
			'populares' => array(
				'tetra neon',
				'neon',
				'neon comum',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 2.2,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Paracheirodon-innesi',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 2,2 cm SL; 20 a 26 C; pH 5,0 a 7,0; dH 1 a 2; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/paracheirodon-innesi/',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
						'chao_declarado_para',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 60 x 30 cm ou maior; agua tipicamente acida, de dureza de carbonatos desprezivel, tingida por substancias humicas.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.org/summary/10691',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Characiformes > Acestrorhamphidae (tetras americanos).',
				),
			),
			'conflitos' => array(),
		),
		'paracheirodon-axelrodi' => array(
			'id' => 'paracheirodon-axelrodi',
			'cientifico' => 'Paracheirodon axelrodi',
			'sinonimos' => array(
				'Cheirodon axelrodi',
				'Hyphessobrycon cardinalis',
			),
			'populares' => array(
				'neon cardinal',
				'tetra cardinal',
				'cardinal',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => 'Alto Orinoco e bacia do rio Negro, América do Sul',
			'porte_cm' => 3,
			'porte_medida' => 'SL',
			'cardume' => 8,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 23,
			'temp_max' => 27,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/paracheirodon-axelrodi.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'nivel_natacao',
						'origem_geografica',
					),
					'referencia' => 'FishBase — ficha da especie: 23 a 27 C, pH 4,0 a 6,0, dH 5 a 12; ocorre sobretudo em cardumes nas camadas medias da coluna; alto Orinoco e rio Negro. Max 2,5 cm SL na busca restrita de 09/09/2026 e 3,0 cm SL na busca aberta do mesmo dia (ver conflitos).',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/paracheirodon-axelrodi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 60 x 30 cm ou maior; manter em grupo misto de pelo menos 8 a 10 exemplares, e junto de outros cardumes para dar seguranca ao grupo.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/paracheirodon-axelrodi.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Characiformes > Acestrorhamphidae (tetras americanos). A familia mudou de nome na revisao recente dos caracideos: a ficha nao diz mais Characidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'porte_adulto_cm',
					'valores' => array(
						array(
							'valor' => 2.5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, leitura por busca restrita ao dominio em 09/09/2026: max 2,5 cm SL',
						),
						array(
							'valor' => 3,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, leitura por busca aberta em 09/09/2026, com a atribuicao explicita a FishBase no resumo: 3,0 cm SL',
						),
					),
					'razao' => 'Duas leituras da MESMA fonte, no mesmo dia, devolveram 2,5 e 3,0 cm SL. Nao e divergencia entre autores: e o limite de colher numero por resumo de busca sem poder abrir a pagina. Enquanto o egresso nao abrir, o banco publica os dois e usa o maior, porque em lotacao errar o porte para menos e o lado que lota demais.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'hemigrammus-erythrozonus' => array(
			'id' => 'hemigrammus-erythrozonus',
			'cientifico' => 'Hemigrammus erythrozonus',
			'sinonimos' => array(),
			'populares' => array(
				'tetra-brilhante',
				'glowlight',
				'tetra-luminoso',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 3.3,
			'porte_medida' => 'TL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 37.5,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 24,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10642',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Acestrorhamphidae (tetras americanos); max 3,3 cm TL; pH 6,0 a 8,0; dH 5 a 12; 24 a 28 C; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hemigrammus-erythrozonus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'ph',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 60 x 37,5 x 30 cm (70 litros) abriga confortavelmente um grupo pequeno; comprar sempre grupo de pelo menos 6, de preferencia 10 ou mais, porque e especie de cardume e vai muito melhor entre os seus; pH 5,5 a 7,5, mais colorida em agua acida; e um dos melhores tetras para o aquario comunitario geral: ativa, colorida e pacifica.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pelo menos 6, de preferencia 10 ou mais',
						),
					),
					'razao' => 'Campo de bem-estar com divergencia de um individuo: fica o maior, 6.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 6,
								'max' => 8,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 6,0 a 8,0',
						),
						array(
							'valor' => array(
								'min' => 5.5,
								'max' => 7.5,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pH 5,5 a 7,5, mais colorida em agua acida',
						),
					),
					'razao' => 'Faixas deslocadas em meio ponto de pH nas duas pontas. Campo de manutencao: manda o compendio.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'otocinclus-vittatus' => array(
			'id' => 'otocinclus-vittatus',
			'cientifico' => 'Otocinclus vittatus',
			'sinonimos' => array(),
			'populares' => array(
				'otocinclo',
				'oto',
				'limpa-vidro',
			),
			'familia' => 'Loricariidae',
			'origem' => '',
			'porte_cm' => 3.3,
			'porte_medida' => 'TL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 20,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Otocinclus-vittatus',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: max 3,3 cm TL; 20 a 25 C; pH 6,0 a 7,5; dH 2 a 18.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/otocinclus-macrospilus/',
					'em' => '2026-09-09',
					'campos' => array(
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
						'alimentacao',
						'exige_aquario_maduro',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish — ficha do genero Otocinclus (pagina de O. macrospilus): sao gregarios por natureza e o ideal e manter em grupo de 6 exemplares ou mais; o menor aquario a considerar seguro para o genero tem pelo menos 45 cm de comprimento, por causa das arrancadas de nado; a unica atividade diurna e raspar alga de folha, tronco, rocha e vidro, e sem planta e superficie em abundancia o peixe se sente exposto, o que traz doenca e morte precoce; muitos aquaristas relatam menos problema quando os peixes entram em aquario maduro e plantado, com qualidade de agua estavel e microrganismos e algas em quantidade.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Otocinclus-vittatus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Loricariidae (Armored catfishes) > subfamilia Hypoptopomatinae.',
				),
			),
			'conflitos' => array(),
		),
		'corydoras-panda' => array(
			'id' => 'corydoras-panda',
			'cientifico' => 'Corydoras panda',
			'sinonimos' => array(
				'Hoplisoma panda',
			),
			'populares' => array(
				'coridora-panda',
				'cory-panda',
			),
			'familia' => 'Callichthyidae',
			'origem' => '',
			'porte_cm' => 3.8,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 20,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/corydoras-panda.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie (hoje publicada como Hoplisoma panda): familia Callichthyidae (callichthyid armored catfishes); max 3,8 cm SL; pH 6,0 a 8,0; dH 2 a 25; 20 a 25 C; alto Amazonas.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-panda',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 45 x 30 x 30 cm ja atende um grupo pequeno; coridoras devem ser mantidas em grupo, e um grupo de pelo menos SEIS e o melhor; temperatura em torno de 24 C esta bem.',
				),
			),
			'conflitos' => array(),
		),
		'danio-rerio' => array(
			'id' => 'danio-rerio',
			'cientifico' => 'Danio rerio',
			'sinonimos' => array(
				'Brachydanio rerio',
				'Brachydanio frankei',
			),
			'populares' => array(
				'paulistinha',
				'zebrafish',
				'peixe-zebra',
			),
			'familia' => 'Danionidae',
			'origem' => '',
			'porte_cm' => 3.8,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 90,
			'base_comprimento' => 90,
			'base_largura' => 30,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 18,
			'temp_max' => 24,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/danio-rerio.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 3,8 cm SL; 18 a 24 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/danio-rerio/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'comportamento',
					),
					'referencia' => 'Seriously Fish — ficha da especie (publicada como Brachydanio rerio): especie ativa, entao mesmo um grupo pequeno precisa de aquario com base minima de 90 x 30 cm; tamanho usual de 40 a 50 mm; e pacifica, rustica e barata.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/danio-rerio.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Teleostei > Cypriniformes (Carps) > Danionidae (Danios) > Danioninae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 90,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: especie ativa, base minima de 90 x 30 cm mesmo para grupo pequeno',
						),
					),
					'razao' => 'Meia diferenca de frente para o mesmo peixe de 4 cm. O compendio manda em campo de manutencao e o campo e de bem-estar: fica o maior, 90 cm, e a ficha publica o outro numero atribuido.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'hyphessobrycon-eques' => array(
			'id' => 'hyphessobrycon-eques',
			'cientifico' => 'Hyphessobrycon eques',
			'sinonimos' => array(
				'Hyphessobrycon callistus',
				'Hyphessobrycon serpae',
				'Megalamphodus eques',
			),
			'populares' => array(
				'mato-grosso',
				'serpae',
				'tetra-serpae',
			),
			'familia' => 'Characidae',
			'origem' => '',
			'porte_cm' => 4,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'agressivo',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 22,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/Summary/SpeciesSummary.php?id=46294',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
						'cardume_minimo',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Characidae (subfamilia Stethaprioninae); max 4 cm SL macho/nao sexado; pH 5,0 a 7,8; dH 10 a 25; 22 a 26 C; secao de aquario: agressivo, em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hyphessobrycon-eques/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'ph',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 80 x 30 cm ou equivalente e o minimo absoluto a considerar (volume citado de 72 litros); os exemplares de criadouro sao adaptaveis quanto a quimica da agua e ficam bem na faixa de pH 5,0 a 7,5.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 80,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 80 x 30 cm e o minimo absoluto',
						),
					),
					'razao' => 'Um terco a mais de frente para o mesmo peixe de 4 cm. O compendio manda em campo de manutencao e o campo e de bem-estar: fica o maior, 80 cm.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7.8,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 5,0 a 7,8',
						),
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7.5,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: exemplares de criadouro ficam bem de 5,0 a 7,5',
						),
					),
					'razao' => 'Divergencia pequena (0,3 no teto) e no mesmo sentido. pH e campo de manutencao: fica o do compendio, que e tambem o mais estreito.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'tanichthys-albonubes' => array(
			'id' => 'tanichthys-albonubes',
			'cientifico' => 'Tanichthys albonubes',
			'sinonimos' => array(),
			'populares' => array(
				'tanictis',
				'peixe-neve',
				'paulistinha-da-montanha',
				'white cloud',
			),
			'familia' => 'Tanichthyidae',
			'origem' => 'Ásia: China e Vietnã',
			'porte_cm' => 4,
			'porte_medida' => 'TL',
			'cardume' => 10,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 14,
			'temp_max' => 22,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Tanichthys-albonubes',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 4,0 cm TL; 18 a 22 C, sobrevivendo a agua de ate 5 C; pH 6,0 a 8,0; dH 5 a 19; familia Tanichthyidae; Asia, China e Vietna; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/tanichthys-albonubes',
					'em' => '2026-09-11',
					'campos' => array(
						'temperatura_C',
						'cardume_minimo',
						'convivencia',
						'comportamento',
					),
					'referencia' => 'Seriously Fish - ficha da especie: manter a 14 a 22 C (57 a 72 F); peixe de cardume por natureza, o ideal e comprar um grupo de 10 ou mais exemplares, porque assim os individuos ficam menos nervosos, o conjunto fica mais natural e os machos mostram a melhor cor disputando as femeas; muito pacifico e residente ideal de aquario comunitario bem mantido, desde que a exigencia de temperatura seja respeitada; micropredador que come pequenos insetos, vermes, crustaceos e zooplancton.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'temperatura_C',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 18,
								'max' => 22,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: 18 a 22 C, sobrevivendo a agua de ate 5 C',
						),
						array(
							'valor' => array(
								'min' => 14,
								'max' => 22,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: manter a 14 a 22 C',
						),
					),
					'razao' => 'Campo de manutencao: o compendio manda, pela tabela dominio_por_campo. O teto e o mesmo nas duas fontes e so o piso desce, de 18 para 14 C. Nao muda o que esta especie ja significava para a ilha - ela e a segunda que dispensa aquecedor em boa parte do Brasil -, mas muda o lado oposto da conta: com teto de 22 C, o risco desta especie no verao brasileiro e de agua QUENTE demais, e nenhuma calculadora da ilha dimensiona resfriamento hoje.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, busca restrita ao dominio em 09/09/2026: secao de aquario, manter em grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 10,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish, busca restrita ao dominio em 11/09/2026: o ideal e um grupo de 10 ou mais exemplares',
						),
					),
					'razao' => 'As duas regras do esquema apontam para o mesmo lado aqui, o que e raro: o compendio manda em campo de manutencao, E o conservador de campo de bem-estar e o MAIOR. O banco publica 10. O numero importa porque ele multiplica a frente por individuo: com 60 cm declarados, 5 peixes dao 12 cm de frente por individuo e 10 peixes dao 6 cm - a mesma especie, o dobro de densidade, dependendo de qual fonte a pagina citar. Publicar as duas e o unico jeito honesto.',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'mikrogeophagus-ramirezi' => array(
			'id' => 'mikrogeophagus-ramirezi',
			'cientifico' => 'Mikrogeophagus ramirezi',
			'sinonimos' => array(
				'Apistogramma ramirezi',
				'Papiliochromis ramirezi',
				'Microgeophagus ramirezi',
			),
			'populares' => array(
				'ramirezi',
				'borboleta-boliviana',
				'acará-borboleta',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 4.2,
			'porte_medida' => 'SL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'casal',
			'comportamento' => 'territorial',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 27,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Mikrogeophagus-ramirezi',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae; max 4,2 cm SL; pH 5,0 a 6,0; dH 5 a 12; 27 a 30 C; secao de aquario: aquario minimo de 60 cm, aos pares.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/mikrogeophagus-ramirezi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: ao atingir a maturidade sexual os ramirezi formam casais, e cada casal passa a defender um territorio de cerca de meio metro de diametro.',
				),
			),
			'conflitos' => array(),
		),
		'hemigrammus-rhodostomus' => array(
			'id' => 'hemigrammus-rhodostomus',
			'cientifico' => 'Hemigrammus rhodostomus',
			'sinonimos' => array(
				'Petitella rhodostoma',
			),
			'populares' => array(
				'rodóstomo',
				'nariz-vermelho',
				'cabeça-de-fósforo',
			),
			'familia' => 'Characidae',
			'origem' => '',
			'porte_cm' => 5,
			'porte_medida' => 'TL',
			'cardume' => 10,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 90,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 26.5,
			'temp_max' => 29,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Hemigrammus-rhodostomus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (hoje publicada como Petitella rhodostoma): familia Characidae; max 5,0 cm TL; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 80 cm; especie tropical das bacias do baixo Amazonas e do Orinoco.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/hemigrammus-rhodostomus',
					'em' => '2026-09-09',
					'campos' => array(
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'Seriously Fish — ficha da especie: agua mole e acida, pH 5,5 a 6,5, gH 1 a 5, temperatura em torno de 26,5 a 29 C; manter em grupos de 10 ou de preferencia mais, porque e um dos pequenos tetras de cardume mais coeso e nao vai bem em numero insuficiente; a natacao ativa pede aquario de no minimo 90 cm de comprimento.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais',
						),
						array(
							'valor' => 10,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupos de 10 ou de preferencia mais',
						),
					),
					'razao' => 'O dobro de peixes para o mesmo cardume. Campo de bem-estar: fica o maior, 10, e o numero da base sai publicado do lado. Dobrar o cardume dobra a carga biologica, entao esta divergencia muda o filtro e o aquario que a pessoa compra.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 80,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 80 cm',
						),
						array(
							'valor' => 90,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: no minimo 90 cm de comprimento',
						),
					),
					'razao' => 'Campo de bem-estar com duas declaracoes proximas: fica o maior, 90 cm.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'trigonostigma-heteromorpha' => array(
			'id' => 'trigonostigma-heteromorpha',
			'cientifico' => 'Trigonostigma heteromorpha',
			'sinonimos' => array(
				'Rasbora heteromorpha',
			),
			'populares' => array(
				'rasbora arlequim',
				'arlequim',
				'rasbora',
			),
			'familia' => 'Danionidae',
			'origem' => 'Sudeste asiático: Malásia, Singapura e Indonésia',
			'porte_cm' => 5,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 22,
			'temp_max' => 25,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10881',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'origem_geografica',
						'nivel_natacao',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 5,0 cm TL; 22 a 25 C; pH 5,0 a 7,0; dH 5 a 12; bentopelagica; Malasia, Singapura e Indonesia; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trigonostigma-heteromorpha',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
						'chao_declarado_para',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 60 x 30 cm deve ser a menor a considerar, porque a especie tem de ser mantida em numero; pH 5,0 a 6,0 e dureza de 1 a 5 graus, com a temperatura na parte alta da faixa.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/trigonostigma-heteromorpha.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Danionidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'ph',
					'valores' => array(
						array(
							'valor' => array(
								'min' => 5,
								'max' => 7,
							),
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: pH 5,0 a 7,0',
						),
						array(
							'valor' => array(
								'min' => 5,
								'max' => 6,
							),
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: pH 5,0 a 6,0, dureza de 1 a 5 graus',
						),
					),
					'razao' => 'Intervalos encaixados, nao contraditorios: o compendio e mais estreito e mais acido. Campo de manutencao que NAO e de bem-estar direto, entao vale a intersecao conservadora da regra V17 do banco de produtos — a afirmacao que as duas fontes sustentam e 5,0 a 6,0.',
					'tratamento' => 'intersecao-conservadora',
				),
			),
		),
		'xiphophorus-maculatus' => array(
			'id' => 'xiphophorus-maculatus',
			'cientifico' => 'Xiphophorus maculatus',
			'sinonimos' => array(),
			'populares' => array(
				'platy',
				'plati',
				'moeda',
			),
			'familia' => 'Poeciliidae',
			'origem' => '',
			'porte_cm' => 6,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'harem',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 18,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-maculatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'FishBase — ficha da especie: max 4,0 cm TL macho e 6,0 cm TL femea; 18 a 25 C; pH 7,0 a 8,0; dH 9 a 19; secao de aquario: aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/xiphophorus-maculatus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comportamento',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: muito pacifico e convive com a maioria das especies comunitarias, sem a agressividade de alguns espadas e molinesias, com os machos se tolerando; quando machos e femeas dividem o aquario deve haver mais femeas que machos, para dissipar o assedio dos machos; macho cerca de 5 cm e femea cerca de 7,5 cm; a agua do habitat natural fica em media entre 23 e 24 C.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-maculatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: Cyprinodontiformes > Poeciliidae (Poeciliids).',
				),
			),
			'conflitos' => array(),
		),
		'betta-splendens' => array(
			'id' => 'betta-splendens',
			'cientifico' => 'Betta splendens',
			'sinonimos' => array(
				'Micracanthus marchei',
			),
			'populares' => array(
				'betta',
				'beta',
				'peixe-de-briga',
			),
			'familia' => 'Osphronemidae',
			'origem' => '',
			'porte_cm' => 6.5,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'solitario',
			'comportamento' => 'agressivo',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'chao_para' => array(
				'um-exemplar',
				'casal',
			),
			'temp_min' => 24,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/betta-splendens.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: max 6,5 cm TL para o macho; 24 a 30 C; pH 6,0 a 8,0; dH 5 a 19.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/betta-splendens/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
						'comportamento',
						'ph',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 45 x 30 cm ou equivalente ja e grande para um macho sozinho ou um casal; melhor manter sozinho, as linhagens ornamentais sao mais agressivas que qualquer outra especie de Betta e na maioria dos casos so um individuo por aquario; manter o aquario bem tampado e nao encher ate a borda, porque a especie precisa de acesso a camada de ar umido acima da agua e e excelente saltadora; exemplares selvagens preferem pH entre 5,0 e 7,0 e as linhagens ornamentais aceitam de 6,0 a 8,0.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/speciessummary.php?id=4768',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Osphronemidae (gouramis).',
				),
			),
			'conflitos' => array(),
		),
		'nannostomus-beckfordi' => array(
			'id' => 'nannostomus-beckfordi',
			'cientifico' => 'Nannostomus beckfordi',
			'sinonimos' => array(
				'Nannostomus anomalus',
				'Nannostomus aripirangensis',
			),
			'populares' => array(
				'peixe-lápis',
				'peixe lápis dourado',
				'nannostomus beckfordi',
			),
			'familia' => 'Lebiasinidae',
			'origem' => '',
			'porte_cm' => 6.5,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 24,
			'temp_max' => 26,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Nannostomus-beckfordi',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 6,5 cm SL; 24 a 26 C; pH 6,0 a 8,0; dH 5 a 19; familia Lebiasinidae; habita rios pequenos de pouca correnteza e brejos, formando grupos em que os machos dominam para defender territorio; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/nannostomus-beckfordi/',
					'em' => '2026-09-11',
					'campos' => array(
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: como os demais Nannostomus, o N. beckfordi deve ser mantido em grupo; e bastante comum no comercio aquarista e uma excelente escolha para quem esta comecando, por ser menos exigente que a maioria das congeneres.',
				),
			),
			'conflitos' => array(),
		),
		'corydoras-paleatus' => array(
			'id' => 'corydoras-paleatus',
			'cientifico' => 'Corydoras paleatus',
			'sinonimos' => array(
				'Hoplisoma paleatum',
			),
			'populares' => array(
				'coridora pimenta',
				'coridora paleatus',
				'cory paleatus',
			),
			'familia' => 'Callichthyidae',
			'origem' => '',
			'porte_cm' => 6.6,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 61,
			'base_comprimento' => 61,
			'base_largura' => 38,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 18,
			'temp_max' => 23,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Corydoras-paleatus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie (publicada tambem como Hoplisoma paleatum): max length 6,6 cm SL macho/nao-sexado e 7,1 cm SL femea; 18 a 23 C; pH 6,0 a 8,0; dH 5 a 19; familia Callichthyidae; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-paleatus',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish - ficha da especie: base recomendada de 61 x 38 cm (24 x 15 pol).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 61,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'corydoras-sterbai' => array(
			'id' => 'corydoras-sterbai',
			'cientifico' => 'Corydoras sterbai',
			'sinonimos' => array(
				'Hoplisoma sterbai',
			),
			'populares' => array(
				'coridora sterbai',
				'cory sterbai',
			),
			'familia' => 'Callichthyidae',
			'origem' => 'América do Sul: Brasil central e Bolívia',
			'porte_cm' => 6.8,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 45,
			'base_comprimento' => 45,
			'base_largura' => 30,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 21,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/corydoras-sterbai.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase - ficha da especie (publicada tambem como Hoplisoma sterbai): max length 6,8 cm SL macho/nao-sexado; 21 a 25 C; pH 6,0 a 8,0; dH 2 a 25; familia Callichthyidae; America do Sul, Brasil central e Bolivia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-sterbai/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
						'nivel_natacao',
					),
					'referencia' => 'Seriously Fish - ficha da especie: um aquario de 45 x 30 x 30 cm (42,5 litros) e grande o bastante para um grupo pequeno desta especie.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-sterbai/',
					'em' => '2026-09-12',
					'campos' => array(
						'cardume_minimo',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: a especie deve ser mantida SEMPRE em grupo, porque fica bem mais confiante e ativa na presenca dos seus, e um grupo de pelo menos SEIS e o melhor.',
				),
			),
			'conflitos' => array(),
		),
		'puntigrus-tetrazona' => array(
			'id' => 'puntigrus-tetrazona',
			'cientifico' => 'Puntigrus tetrazona',
			'sinonimos' => array(
				'Puntius tetrazona',
				'Systomus tetrazona',
				'Barbus tetrazona',
			),
			'populares' => array(
				'barbo sumatra',
				'sumatrano',
				'tigre',
			),
			'familia' => 'Cyprinidae',
			'origem' => '',
			'porte_cm' => 7,
			'porte_medida' => 'TL',
			'cardume' => 8,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'semi-agressivo',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Puntigrus-tetrazona',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (barbo-de-sumatra): max 7,0 cm TL; 20 a 26 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, NAO manter com peixes de nadadeiras longas, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/puntigrus-tetrazona/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'comportamento',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 80 x 30 cm ou equivalente deve ser a menor a considerar; grupo de pelo menos 8 a 10 exemplares deve ser a compra minima, porque assim os peixes se distraem entre si em vez de perturbar os companheiros de aquario, e o conjunto fica mais natural.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Puntigrus-tetrazona',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cyprinidae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 8,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupo de pelo menos 8 a 10 exemplares como compra minima',
						),
					),
					'razao' => 'Campo de manutencao e de bem-estar: manda o compendio e vence o maior. Aqui o numero maior nao e so conforto do peixe, e seguranca dos vizinhos: as duas fontes ligam grupo pequeno a agressao dirigida para fora do cardume.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'corydoras-aeneus' => array(
			'id' => 'corydoras-aeneus',
			'cientifico' => 'Corydoras aeneus',
			'sinonimos' => array(
				'Osteogaster aenea',
				'Corydoras schultzei',
				'Corydoras venezuelanus',
			),
			'populares' => array(
				'coridora bronze',
				'coridora',
				'cascudinho',
			),
			'familia' => 'Callichthyidae',
			'origem' => 'América do Sul, da Colômbia e Trinidad até a bacia do Prata, a leste dos Andes',
			'porte_cm' => 7.5,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 80,
			'base_comprimento' => 80,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 25,
			'temp_max' => 28,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/7777',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'nivel_natacao',
						'origem_geografica',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie (publicada tambem como Osteogaster aenea): max 7,5 cm SL; 25 a 28 C; pH 6,0 a 8,0; dH 5 a 19; demersal; da Colombia e Trinidad ate a bacia do Prata; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/corydoras-aeneus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base de 80 x 30 cm ou equivalente para manutencao de longo prazo; areia fina e o substrato ideal, cascalho arredondado serve desde que mantido escrupulosamente limpo; grupo de pelo menos seis da o comportamento e a confianca normais do genero.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Corydoras-aeneus',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie (publicada como Osteogaster aenea): Siluriformes (Catfishes) > Callichthyidae (Callichthyid armored catfishes) > subfamilia Corydoradinae.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 80,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 80 x 30 cm ou equivalente para manutencao de longo prazo',
						),
					),
					'razao' => 'Campo de manutencao: pela tabela dominio_por_campo quem manda e o compendio, e o compendio pede mais espaco. Como e campo de bem-estar, o conservador e o MAIOR, e as duas declaracoes saem atribuidas na ficha.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: grupo de pelo menos seis',
						),
					),
					'razao' => 'Mesma logica: campo de manutencao e de bem-estar, vence o maior, e os dois numeros ficam publicados.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'gymnocorymbus-ternetzi' => array(
			'id' => 'gymnocorymbus-ternetzi',
			'cientifico' => 'Gymnocorymbus ternetzi',
			'sinonimos' => array(),
			'populares' => array(
				'tetra-negro',
				'viúva-negra',
				'tetra-preto',
			),
			'familia' => 'Acestrorhamphidae',
			'origem' => '',
			'porte_cm' => 7.5,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 75,
			'base_comprimento' => 75,
			'base_largura' => 30,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 20,
			'temp_max' => 26,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4682',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comportamento',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Acestrorhamphidae (tetras americanos); max 7,5 cm SL; pH 6,0 a 8,0; dH 5 a 19; 20 a 26 C (subtropical); peixe de cardume pacifico.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/gymnocorymbus-ternetzi/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um grupo pode ser mantido em aquario padrao de 75 x 30 cm (70 litros); especie ativa, que quer bastante espaco aberto para nadar mais areas de plantio denso e vegetacao flutuante para amenizar a luz.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4682',
					'em' => '2026-09-12',
					'campos' => array(
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'FishBase - secao de aquario: manter em grupos de 5 ou mais individuos; aquario minimo de 60 cm.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 60,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 60 cm',
						),
						array(
							'valor' => 75,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: um grupo pode ser mantido em aquario padrao de 75 x 30 cm',
						),
					),
					'razao' => 'Quinze centimetros de frente entre as duas declaracoes, e as DUAS reguas do esquema apontam para o mesmo lado, o que e raro e vale registrar: comprimento_minimo_aquario_cm e campo de MANUTENCAO, e a tabela dominio_por_campo poe o compendio acima da base cientifica nesses campos; e a regra de assimetria de custo do banco de especies manda ficar com o MAIOR, porque errar espaco para cima so custa aquario mais largo. Fica 75. A divergencia nao e conflito de fato: a base cientifica declara o piso de onde a especie sobrevive e o compendio declara a base de onde o cardume nada em cardume - e e o segundo que a pergunta desta ilha faz.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'melanotaenia-boesemani' => array(
			'id' => 'melanotaenia-boesemani',
			'cientifico' => 'Melanotaenia boesemani',
			'sinonimos' => array(),
			'populares' => array(
				'peixe arco-íris boesemani',
				'rainbow boesemani',
				'arco-íris de boeseman',
			),
			'familia' => 'Melanotaeniidae',
			'origem' => 'Ásia/Oceania: lagos Ajamaru, península de Vogelkop, Irian Jaya, Indonésia',
			'porte_cm' => 9,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => 120,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 27,
			'temp_max' => 30,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/10489',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 9,0 cm SL macho/nao-sexado e 7,0 cm SL femea; 27 a 30 C; pH 7,0 a 8,0; dH 9 a 19; familia Melanotaeniidae; conhecida apenas dos lagos Ajamaru, Irian Jaya; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 80 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/melanotaenia-boesemani',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
					),
					'referencia' => 'Seriously Fish - ficha da especie: base de 120 x 30 cm (48 x 12 pol); a especie pede aquario de pelo menos 120 x 30 x 30 cm; deve ser mantida em cardume de ao menos 6 a 8 individuos, de preferencia mais.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 80,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 120,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => '',
						),
						array(
							'valor' => 6,
							'fonte' => 'Seriously Fish',
							'referencia' => '',
						),
					),
					'razao' => '',
					'tratamento' => 'nivel-mais-alto-vence',
				),
			),
		),
		'trichogaster-lalius' => array(
			'id' => 'trichogaster-lalius',
			'cientifico' => 'Trichogaster lalius',
			'sinonimos' => array(
				'Colisa lalia',
			),
			'populares' => array(
				'colisa-anão',
				'colisa',
				'gurami-anão',
			),
			'familia' => 'Osphronemidae',
			'origem' => 'Ásia: Paquistão, Índia e Bangladesh',
			'porte_cm' => 9.5,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'casal',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'casal',
			),
			'temp_min' => 25,
			'temp_max' => 28,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4774',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Osphronemidae; max 9,5 cm TL macho/nao sexado; pH 6,0 a 8,0; dH 5 a 19; 25 a 28 C; Asia: Paquistao, India e Bangladesh.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trichogaster-lalius/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario de 60 x 30 x 30 cm (56 litros) e apenas grande o bastante para UM CASAL, desde que montado corretamente; peixe timido, que pede aquario densamente plantado, substrato escuro e vegetacao flutuante; populacoes selvagens vivem em agua mole e acida.',
				),
			),
			'conflitos' => array(),
		),
		'symphysodon-aequifasciatus' => array(
			'id' => 'symphysodon-aequifasciatus',
			'cientifico' => 'Symphysodon aequifasciatus',
			'sinonimos' => array(),
			'populares' => array(
				'acará-disco',
				'disco',
				'disco azul',
			),
			'familia' => 'Cichlidae',
			'origem' => 'América do Sul: baixo Amazonas e afluentes a leste da confluência do Negro com o Solimões',
			'porte_cm' => 13.7,
			'porte_medida' => 'SL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => 120,
			'base_largura' => 45,
			'chao_para' => array(
				'juvenis',
				'casal',
			),
			'temp_min' => 26,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/11185',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 13,7 cm SL; 26 a 30 C; pH 5,0 a 8,0; dH 0 a 12; familia Cichlidae; America do Sul, baixo Amazonas; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 120 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/symphysodon-aequifasciatus/',
					'em' => '2026-09-22',
					'campos' => array(
						'base_minima_cm',
						'chao_declarado_para',
						'altura_minima_cm',
						'volume_minimo_declarado_L',
					),
					'referencia' => 'Seriously Fish - ficha da especie: um casal reprodutor precisa de espaco na horizontal e na vertical, entao um aquario de 48 x 18 x 18 polegadas (120 x 45 x 45 cm), 255 litros, e recomendado para alguns juvenis ou um casal de adultos reprodutores; porte maximo relatado do disco selvagem em torno de 14 cm; peixe timido e assustadico, que precisa de esconderijo; o selvagem come sobretudo zooplancton, insetos e outros invertebrados pequenos.',
				),
			),
			'conflitos' => array(),
		),
		'pethia-conchonius' => array(
			'id' => 'pethia-conchonius',
			'cientifico' => 'Pethia conchonius',
			'sinonimos' => array(
				'Puntius conchonius',
			),
			'populares' => array(
				'barbo rosado',
				'barbo rosa',
				'puntius rosado',
			),
			'familia' => 'Cyprinidae',
			'origem' => 'Ásia: Afeganistão, Paquistão, Índia, Nepal e Bangladesh',
			'porte_cm' => 14,
			'porte_medida' => 'TL',
			'cardume' => 8,
			'cardume_ate' => 10,
			'convivencia' => 'cardume',
			'comportamento' => 'pacifico',
			'frente_cm' => 100,
			'base_comprimento' => 100,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 18,
			'temp_max' => 22,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/4714',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: max length 14,0 cm TL macho/nao-sexado; subtropical, 18 a 22 C; pH 6,0 a 8,0; dH 5 a 19; familia Cyprinidae; Asia: Afeganistao, Paquistao, India, Nepal e Bangladesh, com introducao no mundo todo; secao de aquario: manter em grupos de 5 ou mais individuos, tamanho minimo de aquario 80 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/pethia-conchonius/',
					'em' => '2026-09-23',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'cardume_recomendado_ate',
						'convivencia',
						'comportamento',
					),
					'referencia' => 'Seriously Fish - ficha da especie: dimensoes de base de pelo menos 100 x 30 cm ou equivalente sao necessarias; algumas formas chegam a 90 a 100 mm, mas a maioria esta adulta com 65 a 75 mm; e uma especie de cardume por natureza e o ideal e mante-la em grupo de pelo menos 8 a 10 exemplares - em numero decente o peixe fica menos nervoso, o conjunto fica mais natural e os machos mostram a melhor cor competindo entre si pela atencao das femeas; especie geralmente pacifica e residente ideal do aquario comunitario bem pesquisado, que nao impoe exigencia especial de quimica da agua e pode ser combinada com muitos dos peixes mais populares do hobby - outros pequenos ciprinideos, tetras, viviparos, peixes arco-iris, anabantoideos, cascudos e botias; considerada um dos pequenos ciprinideos mais resistentes do hobby, e excelente escolha para quem esta comecando.',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 80,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: tamanho minimo de aquario 80 cm',
						),
						array(
							'valor' => 100,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: dimensoes de base de pelo menos 100 x 30 cm ou equivalente sao necessarias',
						),
					),
					'razao' => 'Campo de espaco, e as duas fontes medem coisas diferentes com o mesmo numero: a base cientifica declara so a frente e o compendio declara a base inteira, frente e fundo. Os 20 cm de diferenca nao sao divergencia de opiniao sobre o mesmo peixe, sao o que aparece quando alguem declara o fundo junto - e quem declara o fundo declara o maior.',
					'tratamento' => 'publicar-os-dois',
				),
				array(
					'campo' => 'cardume_minimo',
					'valores' => array(
						array(
							'valor' => 5,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: manter em grupos de 5 ou mais individuos',
						),
						array(
							'valor' => 8,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: o ideal e mante-la em grupo de pelo menos 8 a 10 exemplares',
						),
					),
					'razao' => 'Campo de manutencao e de bem-estar: manda o compendio e vence o maior. E o MESMO par de numeros do barbo sumatra (5 da base cientifica contra 8 do compendio), nas mesmas duas fontes - a terceira vez que este banco encontra a divergencia, e a primeira em que ela aparece duas vezes na mesma categoria.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'pterophyllum-scalare' => array(
			'id' => 'pterophyllum-scalare',
			'cientifico' => 'Pterophyllum scalare',
			'sinonimos' => array(),
			'populares' => array(
				'acará-bandeira',
				'bandeira',
				'anjo',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 15,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'grupo',
			'comportamento' => 'semi-agressivo',
			'frente_cm' => 100,
			'base_comprimento' => 100,
			'base_largura' => 40,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 24,
			'temp_max' => 30,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Pterophyllum-scalare.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 15 cm TL; 24 a 30 C; pH 6,0 a 8,0; dH 5 a 13; secao de aquario: manter em grupos de 5 ou mais individuos, casais em aquario pequeno so para reproducao, aquario minimo de 100 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/pterophyllum-scalare/',
					'em' => '2026-09-09',
					'campos' => array(
						'base_minima_cm',
						'chao_declarado_para',
						'altura_minima_cm',
						'comportamento',
						'alimentacao',
					),
					'referencia' => 'Seriously Fish — ficha da especie: base minima de 100 x 40 x 50 cm, com altura de pelo menos 50 cm para o adulto, e e despropositado sugerir que o adulto caiba em aquario bem menor; ciclideo geralmente pacifico que briga com os proprios, melhor em grupo pequeno; bom peixe comunitario, mas come peixe pequeno como tetras; onivoro, o selvagem come sobretudo pequenos crustaceos e invertebrados aquaticos e o de criadouro aceita racao.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://fishbase.se/summary/4717',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae.',
				),
			),
			'conflitos' => array(),
		),
		'xiphophorus-hellerii' => array(
			'id' => 'xiphophorus-hellerii',
			'cientifico' => 'Xiphophorus hellerii',
			'sinonimos' => array(
				'Xiphophorus helleri',
				'Xiphophorus guntheri',
			),
			'populares' => array(
				'peixe-espada',
				'espada',
				'espadinha',
			),
			'familia' => 'Poeciliidae',
			'origem' => '',
			'porte_cm' => 16,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'harem',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => 120,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 22,
			'temp_max' => 28,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Xiphophorus-hellerii.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Poeciliidae; macho ate 14,0 cm TL e femea ate 16,0 cm TL; 22 a 28 C; pH 7,0 a 8,0; dH 9 a 19.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/xiphophorus-hellerii/',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
					),
					'referencia' => 'Seriously Fish — ficha da especie: aquario com base de 120 x 30 cm ou equivalente e o menor a considerar (volume citado de 108 litros); machos ate 14 cm e femeas ate 16 cm TL; havendo machos e femeas juntos, manter varias femeas para cada macho, porque o assedio do macho e implacavel.',
				),
			),
			'conflitos' => array(),
		),
		'chromobotia-macracanthus' => array(
			'id' => 'chromobotia-macracanthus',
			'cientifico' => 'Chromobotia macracanthus',
			'sinonimos' => array(
				'Botia macracanthus',
				'Botia macracantha',
			),
			'populares' => array(
				'botia-palhaço',
				'botia',
			),
			'familia' => 'Botiidae',
			'origem' => '',
			'porte_cm' => 30.5,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 180,
			'base_comprimento' => 180,
			'base_largura' => 60,
			'chao_para' => array(
				'grupo',
			),
			'temp_min' => 25,
			'temp_max' => 30,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/10897',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Botiidae (pointface loaches); max 30,5 cm TL macho/nao sexado; pH 5,0 a 8,0; dH 5 a 12; 25 a 30 C; secao de aquario: em grupos de 5 ou mais individuos, aquario minimo de 150 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/chromobotia-macracanthus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario com base de 180 x 60 cm ou equivalente e o minimo absoluto para abrigar um grupo (volume citado de 648 litros).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'comprimento_minimo_aquario_cm',
					'valores' => array(
						array(
							'valor' => 150,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase, secao de aquario: aquario minimo de 150 cm',
						),
						array(
							'valor' => 180,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: base de 180 x 60 cm e o minimo absoluto',
						),
					),
					'razao' => 'Campo de bem-estar: fica o maior, 180 cm. A diferenca entre os dois numeros, na pratica, e de 648 para cerca de 450 litros — nenhum dos dois cabe na sala de quem comprou cinco filhotes de 4 cm.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'astronotus-ocellatus' => array(
			'id' => 'astronotus-ocellatus',
			'cientifico' => 'Astronotus ocellatus',
			'sinonimos' => array(
				'Lobotes ocellatus',
				'Astronotus orbiculatus',
			),
			'populares' => array(
				'oscar',
				'apaiari',
				'acará-açu',
			),
			'familia' => 'Cichlidae',
			'origem' => '',
			'porte_cm' => 45.7,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'solitario',
			'comportamento' => '',
			'frente_cm' => 150,
			'base_comprimento' => 150,
			'base_largura' => 60,
			'chao_para' => array(
				'um-exemplar',
			),
			'temp_min' => 22,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Astronotus-ocellatus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cichlidae; max 45,7 cm TL; pH 6,0 a 8,0; dH 5 a 19; 22 a 25 C; habita aguas rasas e paradas de fundo de lama ou areia.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/astronotus-ocellatus/',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
						'expectativa_vida_anos',
					),
					'referencia' => 'Seriously Fish — ficha da especie: um aquario com base de 150 x 60 cm e apenas grande o bastante para abrigar UM adulto, e um casal ou grupo exige mais espaco; e peixe de aquario popular, mas o tamanho adulto e a expectativa de vida tipica de 10 a 20 anos tem de ser considerados antes da compra.',
				),
			),
			'conflitos' => array(),
		),
		'carassius-auratus' => array(
			'id' => 'carassius-auratus',
			'cientifico' => 'Carassius auratus',
			'sinonimos' => array(),
			'populares' => array(
				'kinguio',
				'peixe dourado',
				'japonês',
			),
			'familia' => 'Cyprinidae',
			'origem' => '',
			'porte_cm' => 48,
			'porte_medida' => 'TL',
			'cardume' => 5,
			'cardume_ate' => null,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 100,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 0,
			'temp_max' => 41,
			'status' => 'conflito',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Carassius-auratus.html',
					'em' => '2026-09-09',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'cardume_minimo',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase — ficha da especie: max 48,0 cm TL; faixa termica de 0 a 41 C; pH 6,0 a 8,0; dH 5 a 19; secao de aquario: manter em grupos de 5 ou mais individuos, aquario minimo de 100 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/stunted-growth-means-stunted-lives/',
					'em' => '2026-09-09',
					'campos' => array(
						'expectativa_vida_anos',
					),
					'referencia' => 'Seriously Fish — artigo \'Stunted growth means stunted lives\': mantido de forma correta, C. auratus chega a 30 cm e vive 30 ou 40 anos; um kinguio mantido em aquario de 30 x 20 cm pode sobreviver alguns anos e continuar com poucos centimetros, e isso e nanismo severo, nao tamanho natural.',
				),
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/271',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
					),
					'referencia' => 'FishBase — ficha da especie: familia Cyprinidae (minnows, carps).',
				),
			),
			'conflitos' => array(
				array(
					'campo' => 'porte_adulto_cm',
					'valores' => array(
						array(
							'valor' => 48,
							'fonte' => 'FishBase',
							'referencia' => 'FishBase: max 48,0 cm TL',
						),
						array(
							'valor' => 30,
							'fonte' => 'Seriously Fish',
							'referencia' => 'Seriously Fish: mantido de forma correta chega a 30 cm',
						),
					),
					'razao' => 'Nao e a mesma grandeza: 48 cm e o maximo registrado da especie e 30 cm e o que se espera em aquario bem mantido. Porte e campo de BIOLOGIA, entao pela tabela dominio_por_campo fica o valor da base cientifica, e o numero do compendio sai publicado do lado porque e ele que descreve o que o leitor vai ter em casa.',
					'tratamento' => 'publicar-os-dois',
				),
			),
		),
		'trichogaster-chuna' => array(
			'id' => 'trichogaster-chuna',
			'cientifico' => 'Trichogaster chuna',
			'sinonimos' => array(
				'Colisa chuna',
			),
			'populares' => array(
				'gurami mel',
				'colisa mel',
				'gourami mel',
			),
			'familia' => 'Osphronemidae',
			'origem' => 'Ásia: Índia e Bangladesh',
			'porte_cm' => 5.5,
			'porte_medida' => 'SL',
			'cardume' => 4,
			'cardume_ate' => 6,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'casal',
				'grupo',
			),
			'temp_min' => 22,
			'temp_max' => 28,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/11201',
					'em' => '2026-09-09',
					'campos' => array(
						'familia',
						'origem_geografica',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase - ficha da especie: 22 a 28 C; pH 6,0 a 8,0; dH 5 a 19; familia Osphronemidae; Asia, India e Bangladesh; secao de aquario: tamanho minimo de aquario 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trichogaster-chuna',
					'em' => '2026-09-09',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: um aquario com base de 60 x 30 cm (24 x 12 pol) ou equivalente e suficiente para abrigar um casal ou grupo pequeno.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/trichogaster-chuna',
					'em' => '2026-09-13',
					'campos' => array(
						'porte_adulto_cm',
						'porte_medida',
						'cardume_minimo',
						'cardume_recomendado_ate',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: comprimento padrao maximo de 55 mm SL, ou 5,5 cm; a especie nao e gregaria no sentido dos peixes de cardume, mas parece precisar da interacao com os seus e mostra comportamento mais interessante quando mantida em numero, de modo que a compra de nao menos que 4 a 6 exemplares e recomendada; o grupo desenvolve hierarquia visivel, com os dominantes enxotando os rivais na hora da comida e no ponto preferido do aquario; as femeas adultas sao visivelmente maiores que os machos.',
				),
			),
			'conflitos' => array(),
		),
		'xiphophorus-variatus' => array(
			'id' => 'xiphophorus-variatus',
			'cientifico' => 'Xiphophorus variatus',
			'sinonimos' => array(),
			'populares' => array(
				'plati variatus',
				'platy variatus',
			),
			'familia' => 'Poeciliidae',
			'origem' => 'bacias que drenam para o Golfo do México, do sul de Tamaulipas ao norte de Veracruz (México)',
			'porte_cm' => 7,
			'porte_medida' => 'TL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'harem',
			'comportamento' => 'pacifico',
			'frente_cm' => 60,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 15,
			'temp_max' => 25,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/3233',
					'em' => '2026-09-13',
					'campos' => array(
						'familia',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'comprimento_minimo_aquario_cm',
					),
					'referencia' => 'FishBase — ficha da especie: Cyprinodontiformes > Poeciliidae (Poeciliids); max 7,0 cm TL macho/nao sexado, comprimento comum 3,9 cm TL; secao de aquario: aquario minimo de 60 cm e faixa de manutencao de 15 a 25 C.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/xiphophorus-variatus/',
					'em' => '2026-09-13',
					'campos' => array(
						'comportamento',
						'convivencia',
						'origem_geografica',
					),
					'referencia' => 'Seriously Fish — ficha da especie: bom peixe para aquario comunitario geral, pacifico e rustico; havendo machos e femeas juntos deve haver mais femeas que machos, para dissipar a atencao do macho, que e incessante, e varias femeas para cada macho; precisa de agua de dureza moderada ou maior e nao prospera em agua mole e acida; nativo das bacias que drenam para o Golfo do Mexico, do sul de Tamaulipas ao norte de Veracruz.',
				),
			),
			'conflitos' => array(),
		),
		'apistogramma-agassizii' => array(
			'id' => 'apistogramma-agassizii',
			'cientifico' => 'Apistogramma agassizii',
			'sinonimos' => array(),
			'populares' => array(
				'apistogramma agassizi',
				'apistograma agassizi',
			),
			'familia' => 'Cichlidae',
			'origem' => 'América do Sul: bacia do rio Amazonas, ao longo do Amazonas-Solimões, do Peru, passando pelo Brasil, até a bacia do rio Capim',
			'porte_cm' => 4.2,
			'porte_medida' => 'SL',
			'cardume' => null,
			'cardume_ate' => null,
			'convivencia' => 'harem',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'casal',
			),
			'temp_min' => 26,
			'temp_max' => 29,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/Apistogramma-agassizii',
					'em' => '2026-09-14',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
						'ph',
						'dureza_dgh',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'FishBase - ficha da especie: Teleostei > Cichliformes > Cichlidae (Cichlids) > Geophaginae; max 4,2 cm SL macho/nao sexado; America do Sul, bacia do rio Amazonas, ao longo do Amazonas-Solimoes, do Peru, passando pelo Brasil, ate a bacia do rio Capim; agua doce, bentopelagica; tropical, 26 a 29 C; pH 5,0 a 7,0; dH 0 a 12; secao de aquario: varias femeas para um macho, aquario minimo de 60 cm.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/apistogramma-agassizii/',
					'em' => '2026-09-14',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
					),
					'referencia' => 'Seriously Fish - ficha da especie: base de 60 x 30 cm ou mais e aceitavel para UM casal, com o grupo exigindo espaco maior; exemplares nascidos em cativeiro sao a escolha recomendada para o aquario comunitario geral, enquanto os selvagens ficam melhor sozinhos ou com pequenos peixes de companhia como os Nannostomus, e idealmente nao devem ser misturados com outros Apistogramma; desovador de substrato, que deposita os ovos em frestas e cavidades da decoracao; o macho e maior, mais colorido e desenvolve nadadeiras mais extensas que a femea.',
				),
			),
			'conflitos' => array(),
		),
		'mikrogeophagus-altispinosus' => array(
			'id' => 'mikrogeophagus-altispinosus',
			'cientifico' => 'Mikrogeophagus altispinosus',
			'sinonimos' => array(),
			'populares' => array(
				'papilocromis',
				'papilocromis boliviano',
				'altispinosa',
			),
			'familia' => 'Cichlidae',
			'origem' => 'América do Sul: bacia do rio Amazonas, na drenagem do rio Guaporé no Brasil e na Bolívia, e na drenagem do rio Mamoré na Bolívia',
			'porte_cm' => 5.6,
			'porte_medida' => 'SL',
			'cardume' => 6,
			'cardume_ate' => 8,
			'convivencia' => 'grupo',
			'comportamento' => '',
			'frente_cm' => 120,
			'base_comprimento' => null,
			'base_largura' => null,
			'chao_para' => array(),
			'temp_min' => 22,
			'temp_max' => 26,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/mikrogeophagus-altispinosus.html',
					'em' => '2026-09-14',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'porte_sexo',
						'temperatura_C',
					),
					'referencia' => 'FishBase - ficha da especie: Teleostei > Cichliformes > Cichlidae (Cichlids) > Cichlinae; max 5,6 cm SL macho/nao sexado; America do Sul, bacia do rio Amazonas, na drenagem do rio Guapore no Brasil e na Bolivia, e na drenagem do rio Mamore na Bolivia; agua doce, bentopelagica; tropical, 22 a 26 C.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/mikrogeophagus-altispinosus',
					'em' => '2026-09-14',
					'campos' => array(
						'cardume_minimo',
						'cardume_recomendado_ate',
						'comprimento_minimo_aquario_cm',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: ciclideo relativamente gregario, que idealmente se mantem em grupo misto de machos e femeas de 6 a 8 ou mais, desde que o aquario seja espacoso, de 120 cm de comprimento ou maior; em espaco confinado os machos ficam com frequencia mais agressivos na defesa do proprio territorio; apesar de ser normalmente vendido como tal, nao e recomendado para o aquario comunitario geral, porque exige agua de qualidade impecavel e e mau competidor, o que nao quer dizer que precise ser mantido sozinho; desovador de substrato biparental.',
				),
			),
			'conflitos' => array(),
		),
		'puntius-titteya' => array(
			'id' => 'puntius-titteya',
			'cientifico' => 'Puntius titteya',
			'sinonimos' => array(
				'Barbus titteya',
				'Rohanella titteya',
			),
			'populares' => array(
				'barbo cereja',
				'barbo-cereja',
				'cherry barb',
			),
			'familia' => 'Cyprinidae',
			'origem' => 'Ásia: Sri Lanka, das bacias do Kelani ao Nilwala',
			'porte_cm' => 5,
			'porte_medida' => 'TL',
			'cardume' => 6,
			'cardume_ate' => 10,
			'convivencia' => 'cardume',
			'comportamento' => '',
			'frente_cm' => 60,
			'base_comprimento' => 60,
			'base_largura' => 30,
			'chao_para' => array(
				'nao-declarado',
			),
			'temp_min' => 23,
			'temp_max' => 27,
			'status' => 'completo',
			'fontes' => array(
				array(
					'corpo' => 'FishBase',
					'url' => 'https://www.fishbase.se/summary/6147',
					'em' => '2026-09-23',
					'campos' => array(
						'familia',
						'origem_geografica',
						'porte_adulto_cm',
						'porte_medida',
						'temperatura_C',
						'ph',
						'dureza_dgh',
					),
					'referencia' => 'FishBase - ficha da especie (cherry barb): max 5,0 cm TL, comprimento comum 2,5 cm TL; 23 a 27 C; pH 6,0 a 8,0; dH 5 a 19; familia Cyprinidae; Asia: Sri Lanka, das bacias do Kelani ao Nilwala, em riachos muito sombreados de agua rasa e lenta, com substrato de silte e folhas. A secao de aquario NAO declara numero de grupo nem tamanho minimo de aquario.',
				),
				array(
					'corpo' => 'Seriously Fish',
					'url' => 'https://www.seriouslyfish.com/species/puntius-titteya/',
					'em' => '2026-09-23',
					'campos' => array(
						'comprimento_minimo_aquario_cm',
						'base_minima_cm',
						'chao_declarado_para',
						'cardume_minimo',
						'cardume_recomendado_ate',
						'convivencia',
					),
					'referencia' => 'Seriously Fish - ficha da especie: dimensoes de base de pelo menos 60 x 30 cm ou equivalente sao necessarias; e uma especie de cardume por natureza, e pelo menos 6 a 10 exemplares devem ser comprados - manter nesse numero deixa o peixe menos arisco, resulta num conjunto mais natural e faz os machos desenvolverem cor melhor na presenca de rivais da mesma especie; escolha sem ressalva para iniciante, e um dos pequenos ciprinideos mais onipresentes do hobby.',
				),
			),
			'conflitos' => array(),
		),
	);
	return $catalogo;
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 1b. Os barrados — o que o banco tem e o portão não deixa entrar
 *
 * Mesmo gerador, segundo bloco. Existe porque até 13/09/2026 o snippet só
 * conhecia quem PASSA: a seção podia dizer "são 29 espécies" e não tinha como
 * dizer que o banco tem 37 nem por que os outros 8 não estão na tabela. A
 * prestação de contas da seção 7 do `ARQUIPELAGO.md` estava cumprida para quem
 * está na tabela e para mais ninguém — e ausência sem nome, numa página que
 * fala do próprio banco, é indistinguível de espécie que nunca foi procurada.
 *
 * O motivo chega aqui como CÓDIGO, e quem traduz é
 * `aquametria_peixes_motivo_na_tela()`, logo abaixo. Código na tela do leitor
 * seria `comprimento_minimo_aquario_cm` no lugar de "a frente mínima de
 * aquário", que é vocabulário de dentro da fábrica — e é justamente o defeito
 * que a seção 15.1 e a seção 5 do contrato existem para impedir.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_barrados' ) ) {
function aquametria_peixes_barrados() {
	/* BARRADOS-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */
	static $barrados = null;
	if ( null !== $barrados ) {
		return $barrados;
	}
	$barrados = array(
		'ancistrus-cirrhosus' => array(
			'id' => 'ancistrus-cirrhosus',
			'cientifico' => 'Ancistrus cirrhosus',
			'populares' => array(
				'cascudo-ancistrus',
				'ancistrus',
				'cascudo-barbudo',
			),
			'familia' => 'Loricariidae',
			'faltando' => array(
				'temperatura_C',
			),
		),
		'poecilia-reticulata' => array(
			'id' => 'poecilia-reticulata',
			'cientifico' => 'Poecilia reticulata',
			'populares' => array(
				'guppy',
				'lebiste',
				'barrigudinho',
			),
			'familia' => 'Poeciliidae',
			'faltando' => array(
				'duas fontes distintas',
			),
		),
		'poecilia-sphenops' => array(
			'id' => 'poecilia-sphenops',
			'cientifico' => 'Poecilia sphenops',
			'populares' => array(
				'molinésia',
				'black molly',
				'molinésia preta',
			),
			'familia' => 'Poeciliidae',
			'faltando' => array(
				'comprimento_minimo_aquario_cm',
			),
		),
		'trichopodus-leerii' => array(
			'id' => 'trichopodus-leerii',
			'cientifico' => 'Trichopodus leerii',
			'populares' => array(
				'gurami pérola',
				'gourami pérola',
				'trichogaster pérola',
			),
			'familia' => 'Osphronemidae',
			'faltando' => array(
				'convivencia',
			),
		),
		'trichopodus-trichopterus' => array(
			'id' => 'trichopodus-trichopterus',
			'cientifico' => 'Trichopodus trichopterus',
			'populares' => array(
				'tricogaster',
				'gurami-azul',
				'tricogaster-três-pintas',
			),
			'familia' => 'Osphronemidae',
			'faltando' => array(
				'convivencia',
			),
		),
		'danio-margaritatus' => array(
			'id' => 'danio-margaritatus',
			'cientifico' => 'Danio margaritatus',
			'populares' => array(
				'rasbora galáxia',
				'danio galáxia',
				'microrasbora galáxia',
			),
			'familia' => 'Danionidae',
			'faltando' => array(
				'comprimento_minimo_aquario_cm',
				'convivencia',
				'temperatura_C',
				'duas fontes distintas',
			),
		),
	);
	return $barrados;
	/* BARRADOS-FIM */
}
}

/**
 * O motivo de um barrado, na língua de quem lê.
 *
 * Cada frase completa "falta ___". O mapa é FECHADO e casado com o vocabulário
 * do gerador: código sem tradução devolve string vazia, e quem chama NUNCA
 * imprime o código cru no lugar — a página prefere contar sem nomear a causa a
 * publicar nome de campo de banco. Quem não deixa isso acontecer em silêncio é
 * a bancada: `ferramentas/teste-peixes.py` reprova se algum barrado do banco de
 * hoje tiver motivo sem tradução, então o buraco aparece antes do desembarque e
 * não na tela.
 */
if ( ! function_exists( 'aquametria_peixes_motivo_na_tela' ) ) {
function aquametria_peixes_motivo_na_tela( $codigo ) {
	$mapa = array(
		'nome_cientifico'               => 'o nome científico',
		'nomes_populares_br'            => 'o nome pelo qual a loja brasileira vende',
		'porte_adulto_cm'               => 'o tamanho adulto',
		'porte_medida'                  => 'qual medida de comprimento a fonte usa',
		'comprimento_minimo_aquario_cm' => 'a frente mínima de aquário',
		'convivencia'                   => 'como a espécie vive (sozinha, em casal ou em grupo)',
		'temperatura_C'                 => 'a faixa de temperatura',
		'duas fontes distintas'         => 'um segundo corpo de fonte (as duas referências do banco são do mesmo)',
		'status_registro rascunho'      => 'fechar o registro, que ainda está em rascunho',
		'status_registro revalidar'     => 'refazer a conferência, que o próprio registro pede',
		'fonte sem nome de corpo'       => 'o nome de quem declarou o número, que a referência não deixa ler',
	);
	return isset( $mapa[ $codigo ] ) ? $mapa[ $codigo ] : '';
}
}

/**
 * A lista de barrados em HTML: um item por espécie, com todos os motivos dela.
 *
 * UM ITEM POR ESPÉCIE, E NÃO UM GRUPO POR MOTIVO, e a escolha é entre duas
 * regras da seção 7 que se cruzam aqui. Ela manda que "cada item da categoria
 * consultada apareça exatamente uma vez na prosa" e também que "causa que o
 * código separa, o texto separa". Espécie a que faltam duas coisas — e há uma
 * assim no banco de hoje — apareceria em dois grupos, quebrando a primeira; e
 * juntar as duas causas numa frase só quebraria a segunda. A saída é a espécie
 * aparecer uma vez e cada causa ser uma oração própria, nomeada, nunca fundida
 * numa razão genérica.
 */
if ( ! function_exists( 'aquametria_peixes_barrados_lista_html' ) ) {
function aquametria_peixes_barrados_lista_html( $lista ) {
	$html = '<ul class="aqm-px-barrados">';
	foreach ( $lista as $b ) {
		$html .= '<li><strong>' . esc_html( $b['cientifico'] ) . '</strong>';
		if ( ! empty( $b['populares'] ) ) {
			$html .= ' (' . esc_html( implode( ', ', $b['populares'] ) ) . ')';
		}
		$frases = array();
		foreach ( (array) $b['faltando'] as $codigo ) {
			$frase = aquametria_peixes_motivo_na_tela( $codigo );
			if ( '' !== $frase ) {
				$frases[] = $frase;
			}
		}
		if ( $frases ) {
			/* Enumeração com "e" antes do último: cada causa continua com nome
			   próprio (seção 7), e repetir "falta" quatro vezes na mesma linha
			   — o que a primeira versão fazia — só torna ilegível a espécie que
			   mais precisa ser lida, que é justamente a que está mais longe. */
			$ultima = array_pop( $frases );
			$texto  = $frases ? implode( ', ', $frases ) . ' e ' . $ultima : $ultima;
			$html  .= ' — falta ' . esc_html( $texto ) . '.';
		} else {
			/* Motivo sem tradução: a página conta e não nomeia, em vez de servir
			   o código do banco. A bancada reprova este estado antes do ar. */
			$html .= ' — o registro não passou no portão, e o motivo dele ainda não tem nome nesta tela.';
		}
		$html .= '</li>';
	}
	$html .= '</ul>';
	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 2. As páginas desta leva, e as duas promessas da seção 14.9
 *
 * `consulta` é a consulta-alvo, e `porque` é por que esta página consegue
 * chegar às dez primeiras. As duas são obrigatórias e o teste cobra as duas:
 * página que não sabe o que mira não deveria ter nascido.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_registro' ) ) {
function aquametria_peixes_registro() {
	return array(
		'peixes' => array(
			'nivel'    => 1,
			'pai'      => '',
			'titulo'   => 'Quanto espaço cada peixe pede',
			'conteudo' => '[aquametria_peixes_secao]',
			'consulta' => 'quantos litros por peixe aquário',
			'porque'   => 'É a mãe do eixo e existe para o cluster, não para ranquear sozinha: ela recebe a autoridade do menu e do rodapé e passa para as fichas, que são as páginas de consulta. O que ela tem de próprio é o critério — por que a ilha responde em centímetros de base antes de responder em litros.',
		),
		'tetras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Tetras: quantos litros o cardume pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para tetras',
			'porque'   => 'A SERP desta consulta é de blog de nicho sem fonte, e nenhum dos sete primeiros publica a base mínima declarada por espécie numa tabela comparável. Esta página é a tabela: porte, cardume mínimo e frente mínima das sete espécies do banco, lado a lado, com a fonte de cada linha.',
		),
		'quantos-litros-para-tetra-neon' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'paracheirodon-innesi',
			'titulo'   => 'Quantos litros para um cardume de tetra neon?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra neon',
			'porque'   => 'Medido em 12/09/2026: o top 7 é blog de nicho (aquariovivo, chaveinspiradora, aquarioepeixes, peixemania, aquariopedia), uma loja e um portal de artigo. Nenhum é domínio forte, nenhum atribui o número a fonte nomeada e eles discordam entre si (40 L para 8 a 10 neons contra 20 L para 6 a 8). É resposta genérica que não dá número com procedência — o caso que a 14.9 classifica como ALVO.',
		),
		'quantos-litros-para-tetra-cardinal' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'paracheirodon-axelrodi',
			'titulo'   => 'Quantos litros para um cardume de neon cardinal?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para neon cardinal',
			'porque'   => 'Medido em 12/09/2026: o top 9 tem blog de nicho, três lojas e um portal estrangeiro, e o único que declara base (60 × 30 × 30 cm) não diz de onde tirou. Nenhum publica o cardume mínimo de 8 ao lado da base, que é a conta que decide a compra.',
		),
		'quantos-litros-para-mato-grosso' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hyphessobrycon-eques',
			'titulo'   => 'Quantos litros para um cardume de mato-grosso?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para mato grosso peixe',
			'porque'   => 'Medido em 12/09/2026: o top 8 é blog antigo, duas lojas e dois portais de ração, com números que se contradizem na mesma página de resultados — 40 L de mínimo contra 60 L para 6 a 8, cardume de 3 contra cardume de 6, e porte de 3 cm contra 5 cm. É a SERP mais frouxa das três, e a única em que as duas fontes do nosso banco também discordam: a página publica as duas.',
		),

		/* --- LEVA 2, 12/09/2026: as quatro que faltavam para fechar a
		   categoria. Nenhuma URL da leva 1 muda, nenhum endereço se move. --- */

		'quantos-litros-para-tetra-ember' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hyphessobrycon-amandae',
			'titulo'   => 'Quantos litros para um cardume de tetra ember?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra ember',
			'porque'   => 'Medido em 12/09/2026: o top 8 não tem um domínio brasileiro forte — é revista de loja estrangeira (zooplus.pt), blog (blogdopescador), três lojas hispano-americanas, uma ficha de aquarismo e uma loja brasileira. Os números discordam na mesma página de resultados (30 L, 40 L para 10 exemplares, 50 L para 10) e nenhum atribui o número a fonte nomeada. O caso que a 14.9 classifica como ALVO.',
		),
		'quantos-litros-para-tetra-brilhante' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hemigrammus-erythrozonus',
			'titulo'   => 'Quantos litros para um cardume de tetra-brilhante?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra brilhante',
			'porque'   => 'Medido em 12/09/2026: o top 10 é seis lojas (rsdiscus, proaquarista, kauar, barretos, aquastuchi), duas fichas de aquarismo, um portal e um WordPress de 2011. Dão 40, 50 e 60 L sem fonte, e a própria página de resultados mistura outras espécies (tetra gold, neon verde) na resposta — sinal de SERP frouxa. É ALVO, e o registro do nosso banco é o mais bem sustentado da categoria: as duas fontes concordam na frente e divergem em um exemplar de cardume.',
		),
		'quantos-litros-para-rodostomo' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'hemigrammus-rhodostomus',
			'titulo'   => 'Quantos litros para um cardume de rodóstomo?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para rodostomo',
			'porque'   => 'Medido em 12/09/2026: o top 9 é três fichas de aquarismo (aquarismopaulista, peixeseaquarismo, blogdopescador) e seis lojas. É a única das sete consultas deste eixo em que alguém do top publica a base (80 × 30 × 40 cm) — e publica sem dizer de onde tirou, ao lado de outra resposta que diz 60 L para o mesmo cardume. Segue ALVO, e aqui a vantagem da ilha não é o ineditismo do número: é a atribuição, e é a página assumir que o fundo NÃO está declarado por ninguém em vez de completá-lo de cabeça.',
		),
		'quantos-litros-para-tetra-negro' => array(
			'nivel'    => 3,
			'pai'      => 'tetras',
			'especie'  => 'gymnocorymbus-ternetzi',
			'titulo'   => 'Quantos litros para um cardume de tetra-negro?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tetra negro',
			'porque'   => 'Medido em 12/09/2026: é a SERP mais disputada das sete deste eixo — tem a Petz, que é domínio forte, ao lado de zooplus.pt, PetMag, aquarismopaulista e três lojas. Segue ALVO porque um domínio forte não é "quase tudo" (14.9) e porque o que ele serve é blog de varejo sem número atribuído: a mesma página de resultados dá 60 L, 70 L e 112 L, e o conselho de "três a seis indivíduos de cada tipo", que é regra de aquário comunitário e não cardume mínimo da espécie. As duas fontes do nosso banco declaram 5 ou mais, e discordam da frente em 15 cm.',
		),

		/* --- LEVA 3, 12/09/2026: a segunda categoria do eixo. A mãe e as
		   QUATRO filhas saem juntas, que é o 16.6 (a categoria inteira, nunca
		   uma filha de cada). Nenhuma URL das levas 1 e 2 muda. --- */

		'corydoras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Coridoras: quanto chão o grupo pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para coridoras',
			'porque'   => 'Medido em 12/09/2026: o top 7 não tem um domínio forte e tem um POST DE GRUPO DO FACEBOOK — três fichas de aquarismo (myaquarium, peixeseaquarismo, peixepedia), um blog de loja estrangeira (tiendanimal.pt), um site que não é de aquarismo (caiaque.net) e a pergunta de um aquarista no Facebook. É a SERP mais frouxa das cinco desta leva. Os números se contradizem na mesma página de resultados — 54 L "para a maioria das espécies", 40 L para um grupo de 3, e "7 litros por cada coridora que você adicionar" — e o terceiro é justamente a conta per capita que esta ilha se recusa a fazer desde a leva 1, publicada ali como se fosse regra. Ela vale a categoria inteira: é a página que explica por que coridora se dimensiona por CHÃO e não por litro, e as quatro fichas pendem dela.',
		),
		'quantos-litros-para-coridora-bronze' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-aeneus',
			'titulo'   => 'Quantos litros para um cardume de coridora bronze?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora bronze',
			'porque'   => 'Medido em 12/09/2026: o top 8 é uma ficha de aquarismo forte no nicho (aquarismopaulista), o aquaonline, o blogdopescador e cinco lojas (proaquarista duas vezes, fazendasubmersa, myaquarium). Nenhum domínio forte de fora do nicho. A contradição está dentro da mesma página de resultados: "60 x 30 x 40 cm (72 litros)", "60 litros no mínimo" e "70 litros comportam com folga cinco coridoras" — e a última briga com o cardume de 6 que a mesma resposta declara duas linhas acima. Nenhum atribui o número. O nosso registro é o que pede MAIS espaço da categoria (80 x 30 cm, Seriously Fish), e a página ganha por assumir isso com o nome da fonte em vez de competir por baixo.',
		),
		'quantos-litros-para-coridora-pimenta' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-paleatus',
			'titulo'   => 'Quantos litros para um cardume de coridora pimenta?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora pimenta',
			'porque'   => 'Medido em 12/09/2026: o top 9 é seis lojas (rioaqua, aquaverso.pt, aquariumcrystal, aquastuchi, rsdiscus, proaquarista), duas fichas de aquarismo e um portal generalista de 2010 (culturamix). Duas lojas do top vendem a espécie com nomes populares diferentes — "pimenta" e "mármore" — o que reparte a própria SERP. Os números discordam (60 x 30 x 30 cm contra "mínimo 70 litros") e nenhum diz de onde saiu. É a única das quatro em que o nosso banco tem CONFLITO declarado de frente (60 cm na FishBase, 61 no compêndio), e a ficha publica os dois com a atribuição de cada um — que é exatamente o que o top 9 não faz.',
		),
		'quantos-litros-para-coridora-panda' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-panda',
			'titulo'   => 'Quantos litros para um cardume de coridora panda?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora panda',
			'porque'   => 'Medido em 12/09/2026: o top 8 é blog (blogdopescador), duas fichas de aquarismo (aquarismopaulista, myaquarium), um Blogspot de 2006 e quatro lojas (rsdiscus, fazendasubmersa, proaquarista, rolizoo). Nenhum domínio forte. Eles dão "60 litros para 5 a 6" e "60 x 30 x 30 cm (54 litros)" na mesma resposta, que são dois números diferentes para a mesma pergunta, e nenhum é atribuído. Aqui a vantagem da ilha é incomum e vale dizer: o nosso número é MENOR que o do top — 45 x 30 cm declarados pelo compêndio contra os 60 cm que a SERP repete —, e é o registro que sustenta o aquário de 30 a 40 litros sem mentir. Número menor com fonte nomeada é mais difícil de publicar que número maior, e é o que a página faz.',
		),
		'quantos-litros-para-coridora-sterbai' => array(
			'nivel'    => 3,
			'pai'      => 'corydoras',
			'especie'  => 'corydoras-sterbai',
			'titulo'   => 'Quantos litros para um cardume de coridora sterbai?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para coridora sterbai',
			'porque'   => 'Medido em 12/09/2026: o top 10 é o aquaonline, o blogdopescador, duas fichas de aquarismo e seis lojas (fazendasubmersa duas vezes, rsdiscus, proaquarista, myaquarium). Nenhum domínio forte, e é a SERP mais contraditória das cinco: a mesma página de resultados dá 54 L, 90 L "para um grupo de seis" e "70 litros comportam com folga cinco" — três respostas para uma pergunta só, nenhuma com fonte. É também a ficha que esta leva destravou: até 12/09 o cardume mínimo desta espécie era null no banco e ela não podia virar página, porque ficha que se chama "quantos litros para um cardume" e não sabe o cardume abre a tabela em um exemplar. O número veio da ficha da própria espécie no compêndio, por busca restrita, e o registro guarda a recusa da alternativa fácil ao lado dele.',
		),

		/* --- LEVA 4, 14/09/2026: a TERCEIRA categoria do eixo, e a primeira em
		   que as filhas não vivem todas do mesmo jeito. A mãe e as três filhas
		   saem juntas, que é o 16.6. Nenhuma URL das levas 1, 2 e 3 muda.

		   AS QUATRO DECLARAM `serp_em`, e é a primeira vez que o campo nascido
		   na 1.3.0 tem para quem servir: as quatro consultas foram classificadas
		   em 13/09/2026 e as doze páginas no ar continuam em 12/09/2026. Quem
		   não declarar herda o padrão, que seria mentira nestas quatro. --- */

		'bettas' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Bettas e gouramis: quantos litros cada um pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para gourami',
			'serp_em'  => '13/09/2026',
			'porque'   => 'Medido em 13/09/2026: o top é quase só página de produto de loja, mais um agregador, e os números que eles publicam são 40, 54, 60 e 70 L — cada um de uma espécie diferente, sem dizer de qual. É a SERP que mais pede a página de categoria em vez de três fichas soltas: "gourami" é um balcão inteiro, não um peixe, e responder com um número só é responder à pergunta errada. A vantagem desta página não é o número: é o arranjo social. Sob o mesmo rótulo estão um peixe que vive sozinho, um que vive em casal e um que vive em grupo com hierarquia, e nenhuma das quatro SERPs desta leva distingue isso.',
		),
		'quantos-litros-para-betta' => array(
			'nivel'    => 3,
			'pai'      => 'bettas',
			'especie'  => 'betta-splendens',
			'titulo'   => 'Quantos litros para um betta?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para um betta',
			'serp_em'  => '13/09/2026',
			'porque'   => 'Medido em 13/09/2026: o top é um blog de loja grande (Cobasi) e cinco blogs de nicho e portais (peixeseaquarismo, aquariovivo, vigopeixe, manualdoagora, guiadoaquarismo). Eles publicam 20 L, 18 L e 40 L — e o MESMO texto que diz "mínimo 18" diz "recomendado 40", que é a contradição dentro de uma página só. Nenhum atribui o número a fonte nomeada. É ALVO, e esta é a ficha em que a distância entre o que a fonte declara e o que o mercado pratica é a maior do banco: o compêndio declara base de 45 × 30 cm para UM macho, e o varejo brasileiro vende o peixe em pote de menos de 2 L.',
		),
		'quantos-litros-para-colisa-anao' => array(
			'nivel'    => 3,
			'pai'      => 'bettas',
			'especie'  => 'trichogaster-lalius',
			'titulo'   => 'Quantos litros para um casal de colisa-anão?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para colisa anão',
			'serp_em'  => '13/09/2026',
			'serp_nota' => 'Esta espécie é a medição mais forte desta leva, e ela não veio de uma consulta: veio de duas. O Trichogaster lalius aparece com 56 L numa das consultas classificadas em 13/09/2026 e com 70 L na outra, no mesmo dia, além dos 40 L e dos 36 L que já discordavam entre si. São quatro números para o mesmo peixe, nenhum atribuído a fonte nomeada, dois deles na primeira página. Nesta página o número é um só, e vem com o nome de quem o declarou e a data em que foi colhido.',
			'porque'   => 'Medido em 13/09/2026: o top é três fichas de aquarismo e cinco páginas de produto de loja (Pró-Aquarista, Fazenda Submersa, Solaqua), com 56 L, 40 L, 36 L e "40 a 44 L é o mínimo aceitável". É ALVO, e é a única das quatro consultas desta leva em que a tese da ilha foi medida POR FORA dela: a mesma espécie se contradiz em duas buscas do mesmo dia. Nas levas 1 a 3 a discordância era entre páginas diferentes sobre espécies diferentes; aqui é o mesmo peixe.',
		),
		'quantos-litros-para-gurami-mel' => array(
			'nivel'    => 3,
			'pai'      => 'bettas',
			'especie'  => 'trichogaster-chuna',
			'titulo'   => 'Quantos litros para um grupo de gurami mel?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para gurami mel',
			'serp_em'  => '13/09/2026',
			'porque'   => 'Medido em 13/09/2026: o top é seis fichas de aquarismo e três páginas de produto de loja, com 40 L, 36 L para um exemplar sozinho e 56 L para um grupo de três — e um deles chega a declarar a BASE, 60 × 30 × 30 cm, que é o número que esta ilha publica com o nome da fonte do lado. É ALVO, e a vantagem daqui é a outra metade: o compêndio declara que a espécie NÃO é de cardume no sentido dos lambaris, que a compra recomendada é de 4 a 6 exemplares e que o grupo forma hierarquia, com o dominante enxotando o rival na hora da comida. Nenhuma resposta do top publica o arranjo ao lado do espaço.',
		),

		/* --- LEVA 5, 14/09/2026: a QUARTA categoria do eixo, e a primeira em
		   que NENHUMA filha tem número declarado. A mãe e as três filhas saem
		   juntas, que é o 16.6. Nenhuma URL das levas 1 a 4 muda.

		   AS TRÊS FICHAS declaram `serp_em` => '13/09/2026', porque foi nesse
		   dia que as três consultas foram classificadas, na execução das 21h21Z
		   que preparou a categoria. A MÃE declara 14/09/2026, que é o dia da
		   própria leva: a consulta dela não existia classificada e foi medida
		   nesta execução. --- */

		'vivaparos' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Vivíparos: quantos litros o harém pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para peixes vivíparos',
			'serp_em'  => '14/09/2026',
			'porque'   => 'Medido em 14/09/2026, e o achado é a ausência: NENHUMA das sete primeiras respostas fala de vivíparo. A consulta devolve as páginas genéricas de "quantos peixes cabem no meu aquário" — dois blogs de pet shop, uma ficha de aquarismo, uma loja portuguesa, um fórum, um artigo de 2020 e um Blogspot de 2013 —, e o que elas publicam é a regra por centímetro de peixe, em três versões que discordam entre si na mesma página de resultados (1 L por cm até 2 cm, 1,5 L por cm de 2 a 5 cm, 2 L por cm de 5 a 10 cm), mais o "10 litros vagos + 5 litros por peixe" que apareceu na busca vizinha. É a conta per capita que esta ilha recusa desde a leva 1, publicada ali como se fosse regra. Nenhum domínio forte, nenhuma atribuição, e o próprio resumo da busca termina mandando o leitor pesquisar espécie por espécie — que é exatamente a tabela que esta página é. ALVO, e do tipo mais limpo do eixo: aqui a ilha não disputa um número com ninguém, ela ocupa um lugar vazio.',
		),
		'quantos-litros-para-platy' => array(
			'nivel'    => 3,
			'pai'      => 'vivaparos',
			'especie'  => 'xiphophorus-maculatus',
			'titulo'   => 'Quantos litros para platy?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para platy',
			'serp_em'  => '13/09/2026',
			'porque'   => 'Medido em 13/09/2026: top 8 com UM domínio forte de varejo (blog da Cobasi) e sete entre loja, blog e ficha estrangeira. A mesma página de resultados dá 40 L, 30 L para um trio, 50 L para comunitário, 80 L e 60 L para seis; nenhum atribui o número a fonte nomeada e nenhum publica a base. Um domínio forte não é "quase tudo" (14.9), e o que ele serve é blog de varejo sem procedência. É ALVO, e a vantagem daqui é o que o mercado não diz: a base de 60 cm é declarada, e o que decide a lotação depois não é quantos você comprou.',
		),
		'quantos-litros-para-peixe-espada' => array(
			'nivel'    => 3,
			'pai'      => 'vivaparos',
			'especie'  => 'xiphophorus-hellerii',
			'titulo'   => 'Quantos litros para um peixe-espada?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para peixe espada',
			'serp_em'  => '13/09/2026',
			'serp_nota' => 'Esta é a consulta mais valiosa da categoria, e virou medição em vez de leitura: a SERP brasileira recomenda 60 L para o peixe que o compêndio declara com 120 cm de frente. A observação do registro dele já dizia, desde 09/09/2026, que é "o peixe que mais aparece em aquário de 60 L no Brasil e o que menos cabe nele" — era leitura de quem escreveu o registro; em 13/09/2026 passou a ser o que o top 10 publica.',
			'porque'   => 'Medido em 13/09/2026: top 10 de blog, loja e um blogspot de 2013, dando 60 L para grupo e 100 L para casal, nenhum atribuído. É ALVO, e é a ficha em que a distância entre a fonte e o mercado é a maior desta categoria: o compêndio declara base de 120 × 30 cm, que é o dobro da frente do platy — o peixe vendido na prateleira do lado, no mesmo gênero.',
		),
		'quantos-litros-para-plati-variatus' => array(
			'nivel'    => 3,
			'pai'      => 'vivaparos',
			'especie'  => 'xiphophorus-variatus',
			'titulo'   => 'Quantos litros para plati variatus?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para plati variatus',
			'serp_em'  => '13/09/2026',
			'porque'   => 'Medido em 13/09/2026: a SERP responde com páginas do OUTRO peixe — o resultado editorial do topo é a ficha do Xiphophorus maculatus e o resumo mistura os números dos dois. A SERP trata as duas espécies como uma, e a mesma base que sustenta este banco as separa em DOIS campos ao mesmo tempo: 7,0 contra 6,0 cm TL de porte e 15 a 25 contra 18 a 25 °C de faixa. É o buraco mais limpo que esta categoria tem para ocupar, e a página ganha por publicar a diferença entre os dois em vez de repeti-los como um só.',
		),

		/* --- LEVA 6, 14/09/2026: a QUINTA categoria do eixo e as três fichas dela.
		   `/peixes/ciclideos-anoes/` sai do vazio com o mínimo exato do 16.5, e a
		   ilha vai de 36 para 40 URLs — que é o piso da rampa da seção 21. O banco,
		   o critério e a linha mestra desta categoria foram preparados na execução
		   das 21h18Z do mesmo dia, e a SERP das quatro consultas foi classificada
		   lá; esta leva publica. Nenhuma URL das levas 1 a 5 muda, nenhum endereço
		   se move. --- */

		'ciclideos-anoes' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Ciclídeos anões: quantos litros, do casal ao grupo',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para ciclídeo anão',
			'serp_em'  => '14/09/2026',
			'porque'   => 'Medido em 14/09/2026: o top 10 não tem um domínio forte e tem um portal europeu (zooplus.pt), um fórum português, dois blogs de pet shop, um Blogspot de 2012, uma loja, três blogs de aquarismo e uma ficha de OUTRA espécie do gênero. Os números se contradizem na mesma página de resultados — 54 L, 30 L para um casal e 50 L para comunitário, 75 L, 100 L —, nenhum é atribuído e nenhum publica a base em centímetros. E o próprio resumo da busca termina mandando o leitor pesquisar espécie por espécie, que é exatamente a tabela que esta página é. ALVO, e a categoria vale mais do que a soma das fichas: é aqui que se vê que o mesmo porte pede o mesmo aquário e que é o arranjo que dobra o número.',
		),
		'quantos-litros-para-ramirezi' => array(
			'nivel'    => 3,
			'pai'      => 'ciclideos-anoes',
			'especie'  => 'mikrogeophagus-ramirezi',
			'titulo'   => 'Quantos litros para um casal de ramirezi?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para ramirezi',
			'serp_em'  => '14/09/2026',
			'porque'   => 'Medido em 14/09/2026: o top 9 tem SEIS lojas, uma ficha de portal de aquarismo, um portal de conteúdo e um blog — nenhum domínio forte. Os números da mesma página de resultados vão de 30 L para um casal a 60 L, passando por 40 e 50, e nenhum é atribuído a fonte nomeada; junto vem a regra de bolso de "um ramirezi para cada 20 litros", que é a conta per capita que esta ilha recusa desde a leva 1. Nenhum publica a base em centímetros, que é o que a nossa fonte declara. ALVO. É a espécie mais vendida da categoria e a que mais aparece em aquário pequeno demais.',
		),
		'quantos-litros-para-apistogramma-agassizi' => array(
			'nivel'    => 3,
			'pai'      => 'ciclideos-anoes',
			'especie'  => 'apistogramma-agassizii',
			'titulo'   => 'Quantos litros para apistogramma agassizi?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para apistogramma agassizi',
			'serp_em'  => '14/09/2026',
			'porque'   => 'Medido em 14/09/2026, e é a SERP mais frouxa das quatro: OITO dos nove primeiros são páginas de PRODUTO — elas vendem o peixe e não respondem a pergunta —, mais uma ficha de portal. O que aparece de número está espalhado entre 30 L, 50 L, 60 × 30 × 30 cm e 60 L, sem atribuição. ALVO com uma vantagem que as outras três não têm: aqui os dois corpos de fonte declaram o MESMO 60 cm para arranjos diferentes (o compêndio para um casal, a base para várias fêmeas por macho), e a página ganha por publicar essa diferença em vez de escolher uma e calar a outra.',
		),
		'quantos-litros-para-papilocromis' => array(
			'nivel'    => 3,
			'pai'      => 'ciclideos-anoes',
			'especie'  => 'mikrogeophagus-altispinosus',
			'titulo'   => 'Quantos litros para um grupo de papilocromis?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para papilocromis',
			'serp_em'  => '14/09/2026',
			'porque'   => 'Medido em 14/09/2026: dos oito primeiros, só DOIS falam da espécie, e os dois são lojas. O resto é página genérica de "quantos peixes cabem" (duas), uma ficha de kinguio fora do assunto, um Blogspot de 2013, um de 2011 e um fórum. Os números são 60 L para um casal, 100 L para um harém e 70 L para um casal — e NINGUÉM publica os 120 cm de frente que o compêndio declara para o grupo de 6 a 8, que é o arranjo que a própria fonte recomenda. É a maior distância do eixo inteiro entre o que a SERP responde e o que a fonte declara, e por isso a página de maior valor desta leva.',
		),

		/* --- LEVA 7, 22/09/2026: a SÉTIMA categoria do eixo e as três fichas
		   dela. `/peixes/danios-e-rasboras/` nasce com o mínimo exato do 16.5 e a
		   ilha vai de 40 para 44 URLs. É a PRIMEIRA leva do eixo que não custou
		   uma coleta: as três espécies passavam nos dois portões desde
		   11/09/2026 e estavam no catálogo, na contagem da seção e na lista de
		   quem divide a mesma água — sem página própria e sem categoria que as
		   abrigasse, porque o `ARVORE.md` fechava o eixo em seis categorias
		   "e só estas". O que esta leva construiu foi o lugar, não o dado.

		   E É TAMBÉM A PRIMEIRA EM QUE A CATEGORIA E A LEVA SAEM NA MESMA
		   EXECUÇÃO. Nas levas 4, 5 e 6 o critério e a linha mestra foram escritos
		   numa execução e a página nasceu noutra, e a leva 5 deixou disso uma
		   regra: "texto de categoria escrito antes da leva é afirmação que
		   ninguém mediu". Aqui não há distância entre os dois — o critério foi
		   escrito contra a mesma tabela que a página serve, no mesmo commit.

		   AS QUATRO DECLARAM `serp_em` => '22/09/2026': as quatro consultas foram
		   classificadas nesta execução, pela 14.9, e as 40 páginas no ar
		   continuam em 12, 13 ou 14/09/2026. --- */

		'danios-e-rasboras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Danios e rasboras: quantos litros o cardume pede',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para danios e rasboras',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: a consulta da categoria devolve listicles de "peixes para aquário pequeno" e páginas de produto de loja — nenhum domínio forte, nenhum fabricante, nenhum marketplace. E ela se contradiz dentro da própria página de resultados, com a maior distância que este eixo já mediu numa SERP só: um resultado diz que danios "podem viver em aquários de apenas 10 litros" e outro publica 40 L de mínimo para o paulistinha, que é um danio. Quatro vezes, na mesma tela, sem que nenhum dos dois diga de onde tirou o número. ALVO, e a categoria vale mais que a soma das três fichas: é aqui que se vê que três peixes que cabem num intervalo de um centímetro de porte pedem frentes de 60 e 90 cm, e que a frente por indivíduo varia em três vezes entre eles.',
		),
		'quantos-litros-para-paulistinha' => array(
			'nivel'    => 3,
			'pai'      => 'danios-e-rasboras',
			'especie'  => 'danio-rerio',
			'titulo'   => 'Quantos litros para um cardume de paulistinha?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para paulistinha',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 10 é seis páginas de produto de loja (RSDiscus quatro vezes, Pró-Aquarista duas, Kauar, Aqua Stuchi), um blog de loja (Hiperzoo) e uma ficha de portal de aquarismo. Nenhum domínio forte. Os números da mesma página de resultados são 40 L, 50 L, 60 a 80 L e "pelo menos 80 cm de comprimento" — quatro respostas para uma pergunta só, nenhuma atribuída a fonte nomeada. É ALVO, e esta é a ficha em que o nosso registro pede MAIS espaço que o top inteiro: 90 × 30 cm de base declarados, contra os 40 L que a SERP repete. Número maior com fonte nomeada é o lado difícil de publicar, e é o que a página faz — com o outro número do conflito (60 cm) impresso do lado, com o nome de quem o declarou.',
		),
		'quantos-litros-para-rasbora-arlequim' => array(
			'nivel'    => 3,
			'pai'      => 'danios-e-rasboras',
			'especie'  => 'trigonostigma-heteromorpha',
			'titulo'   => 'Quantos litros para um cardume de rasbora arlequim?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para rasbora arlequim',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 9 é dois blogs de pesca (Pesca Gerais, Blog do Pescador), três lojas (RSDiscus duas vezes, Pró-Aquarista), duas fichas de portal (MyAquarium), uma página genérica de "quantos peixes cabem" e um site estrangeiro. Nenhum domínio forte. Os dois números que aparecem são 80 L e "40 L para um pequeno grupo de 10", que discordam em duas vezes para o mesmo peixe, e nenhum é atribuído. É ALVO, e aqui a vantagem é a que este eixo mais repete e que o top nunca faz: a base declarada de 60 × 30 cm com o nome de quem a declarou, ao lado do cardume mínimo que a mesma fonte publica.',
		),
		'quantos-litros-para-tanictis' => array(
			'nivel'    => 3,
			'pai'      => 'danios-e-rasboras',
			'especie'  => 'tanichthys-albonubes',
			'titulo'   => 'Quantos litros para um cardume de tanictis?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para tanictis',
			'serp_em'  => '22/09/2026',
			'serp_nota' => 'Esta espécie é vendida no Brasil com quatro nomes diferentes — tanictis, peixe-neve, neon chinês e falso neon —, e isso reparte a própria SERP: as duas consultas medidas em 22/09/2026 devolvem conjuntos de lojas quase sem interseção. A ilha publica a página no nome da prateleira, que é "tanictis", e o banco guarda os quatro.',
			'porque'   => 'Medido em 22/09/2026: o top 9 é sete páginas de produto de loja (Pró-Aquarista, Aquarium Crystal, Barretos, Fazenda Submersa, Kauar, AquaOrinoco, uma portuguesa), um Blogspot de 2010 e duas fichas de portal. Nenhum domínio forte. É a SERP mais contraditória das quatro desta leva: 20 L, 30 L, 50 L para um grupo de 6, 54 L e 100 L para um grupo de 20 — cinco números, nenhum atribuído —, e o cardume mínimo aparece como 3, 5 e 10 na mesma tela. ALVO. É também a ficha em que o nosso banco tem o conflito mais consequente do eixo: as duas fontes declaram 5 e 10 exemplares de cardume mínimo, e com a mesma frente de 60 cm isso é o dobro da densidade dependendo de quem a página citasse. A ficha publica as duas com a atribuição de cada uma.',
		),

		/* --- LEVA 8, 22/09/2026: a OITAVA categoria do eixo e as três fichas
		   dela. `/peixes/acaras/` nasce com o mínimo exato do 16.5 e a ilha vai
		   de 44 para 48 URLs. O banco fechou na execução das 17h25Z do MESMO
		   dia, quando `chao_declarado_para` deu ao acará-disco o segundo corpo
		   de fonte que ele esperava havia treze dias — sem uma busca nova.

		   É A TERCEIRA CATEGORIA SEGUIDA EM QUE O CRITÉRIO DA ANTERIOR NÃO
		   SERVE, e a primeira em que falha o critério que a leva 7 tinha
		   acabado de comemorar por ser verificável dentro do banco. Lá o que
		   separava era o NOME que a pessoa digita; aqui ele traria o
		   `mikrogeophagus-ramirezi` para esta página, porque o terceiro nome
		   popular brasileiro dele é `acará-borboleta` — e ele já é filha de
		   `/peixes/ciclideos-anoes/`. Quem separa aqui é o PORTE declarado,
		   que é número e não leitura.

		   AS QUATRO DECLARAM `serp_em` => '22/09/2026': as quatro consultas
		   foram classificadas nesta execução, pela 14.9, e as 44 páginas no ar
		   continuam em 12, 13, 14 ou 22/09/2026. --- */

		'acaras' => array(
			'nivel'    => 2,
			'pai'      => 'peixes',
			'titulo'   => 'Acarás: quantos litros, do solitário ao cardume',
			'conteudo' => '[aquametria_peixes_categoria]',
			'consulta' => 'quantos litros para acará',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 10 é três blogs de nicho (Aquarismo Paulista duas vezes, Aquaristz duas), uma revista de aquicultura, dois fabricantes de ração (Grupo Sarlo, Alcon), um site de criador, um blog e um agregador de perguntas. Nenhum marketplace, nenhum domínio forte. O defeito desta SERP não é o número errado, é o SUJEITO trocado: a mesma página de resultados responde por três espécies diferentes — acará-bandeira, acará comum (Geophagus) e acará-disco — e devolve 60 L, 200 L, 250 L e 300 L sem que dê para saber de qual peixe cada número fala. É ALVO do tipo que esta tabela resolve por desenho: uma linha por espécie, com o arranjo ao lado do espaço. E ela publica o que nenhum dos dez publica — que dois destes peixes não cabem na mesma água, porque a faixa declarada do oscar termina a 25 °C e a do acará-disco começa a 26 °C.',
		),
		'quantos-litros-para-acara-bandeira' => array(
			'nivel'    => 3,
			'pai'      => 'acaras',
			'especie'  => 'pterophyllum-scalare',
			'titulo'   => 'Quantos litros para um grupo de acará-bandeira?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para acará bandeira',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 9 é uma revista de aquicultura, dois fabricantes de ração (Grupo Sarlo, Alcon), três blogs de nicho (Aquarismo Paulista, Aquario Vivo, Tô Aquariando), um Blogspot de 2011, uma página de produto de loja e um fórum. Nenhum domínio forte. Os números se contradizem na mesma tela e a contradição é aritmética, não de opinião: 200 L para um grupo de SEIS e 200 L para DOZE exemplares, 150 L para um casal, e 60 L num cubo de 40 cm para o casal reprodutor. Ninguém publica os 100 cm de frente que o compêndio declara. É ALVO, e esta é a ÚNICA ficha do eixo inteiro em que a fonte declara ALTURA mínima — 50 cm —, que é justamente a medida que a SERP repete sem número: ela diz que o peixe cresce na vertical e que aquário baixo deforma a nadadeira, e nenhuma das nove diz quantos centímetros de coluna isso quer dizer.',
		),
		'quantos-litros-para-oscar' => array(
			'nivel'    => 3,
			'pai'      => 'acaras',
			'especie'  => 'astronotus-ocellatus',
			'titulo'   => 'Quantos litros para um oscar?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para oscar',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 9 é uma página genérica de "quantos peixes cabem", dois blogs de nicho do mesmo domínio, um vídeo, um fabricante de ração, um blog de varejo de pet, uma enciclopédia de aquarismo, uma página de produto de loja e um marketplace estrangeiro. Um domínio forte só, e ele é de varejo de pet, não de aquarismo. Os números vão de 100 a 300 L sem atribuição — e o que faz desta a ficha de maior valor da leva é uma coincidência que vira contradição quando se lê com atenção: a SERP publica "150 cm de comprimento e mais de 300 L" para VÁRIOS oscares, e o compêndio declara que uma base de 150 × 60 cm é apenas grande o bastante para UM adulto. O mesmo número, para populações opostas. É ALVO, e a página ganha por dizer de quem o número fala.',
		),
		'quantos-litros-para-acara-disco' => array(
			'nivel'    => 3,
			'pai'      => 'acaras',
			'especie'  => 'symphysodon-aequifasciatus',
			'titulo'   => 'Quantos litros para um cardume de acará-disco?',
			'conteudo' => '[aquametria_peixes_ficha]',
			'consulta' => 'quantos litros para acará disco',
			'serp_em'  => '22/09/2026',
			'porque'   => 'Medido em 22/09/2026: o top 9 é a revista de uma loja estrangeira (zooplus.pt), três páginas do mesmo blog de nicho, duas de uma enciclopédia de aquarismo, dois sites de criador de disco e um site de comunidade. Nenhum domínio forte brasileiro. A SERP é a mais numerosa do eixo e a que mais se contradiz por peixe: 50 L por adulto, 60 L por peixe, 200 L para três, 250 L para cinco ou seis e 300 L para quatro ou cinco — três dessas cinco não podem ser verdade juntas, porque 200 L para três é mais por peixe do que 300 L para cinco. Ninguém publica os 120 cm de frente que a base científica declara para o grupo de cinco ou mais. É ALVO, e é a primeira ficha deste eixo a nascer no TERCEIRO ESTADO da ausência de fundo: o chão de 120 × 45 cm existe, foi declarado para juvenis ou um casal, e a página diz isso em vez de o prometer ao cardume.',
		),
	);
}
}

/* Os nomes de nível 2 do eixo, na ordem do ARVORE.md seção 3. Categoria só
   nasce com 3 filhas de dado real (16.5); as outras cinco ficam sem link e sem
   contagem, que é o que a regra manda. A pertinência é por ESPÉCIE, escrita
   aqui: derivar "tetra" da família daria a lista errada nas duas direções — o
   banco tem tetra em Acestrorhamphidae e em Characidae ao mesmo tempo (nota de
   taxonomia do próprio banco), e Characidae também carrega quem o comércio
   brasileiro não vende como tetra. */
if ( ! function_exists( 'aquametria_peixes_categorias' ) ) {
function aquametria_peixes_categorias() {
	return array(
		'tetras' => array(
			'rotulo'  => 'Tetras',
			'plural'  => 'tetras',
			/* `singular` é o sujeito da frase de lista fechada, com o artigo
			   dentro porque o gênero muda com a categoria. Declarado e nunca
			   derivado do `plural`: foi exatamente a derivação de cabeça que pôs
			   "todo tetra" na página das coridoras. */
			'singular' => 'todo tetra',
			'linha_mestra' => 'Tetra pequeno não quer dizer aquário pequeno: o que decide o mínimo do seu aquário é o cardume, e não o tamanho do peixe.',
			'criterio' => 'As espécies que a loja brasileira vende como tetra: os Paracheirodon, os Hemigrammus, os Hyphessobrycon e o Gymnocorymbus. A família não serve de critério aqui — a revisão recente dos caracídeos deixou o banco com tetra em duas famílias diferentes, e Characidae carrega peixe que ninguém vende como tetra.',
			'especies' => array(
				'paracheirodon-innesi',
				'paracheirodon-axelrodi',
				'hyphessobrycon-amandae',
				'hyphessobrycon-eques',
				'hemigrammus-erythrozonus',
				'hemigrammus-rhodostomus',
				'gymnocorymbus-ternetzi',
			),
		),
		'corydoras' => array(
			'rotulo'   => 'Corydoras',
			'plural'   => 'coridoras',
			'singular' => 'toda coridora',
			'linha_mestra' => 'Coridora é peixe de fundo, e peixe de fundo se mede pelo chão: o que decide o mínimo do seu aquário é quantos centímetros de base o grupo tem para vasculhar, não quantos litros cabem em cima.',
			'criterio' => 'Os peixes de fundo que a loja brasileira vende como coridora, da subfamília Corydoradinae. O gênero Corydoras não serve de critério, e aqui pelo motivo oposto ao dos tetras: a revisão recente da subfamília tirou as quatro do gênero na própria fonte — a ficha já publica Hoplisoma panda, Hoplisoma paleatum, Hoplisoma sterbai e Osteogaster aenea —, então filtrar por Corydoras devolveria lista vazia para uma categoria que o aquarista brasileiro compra pelo nome todo dia. O banco guarda os dois nomes de cada uma e esta página serve os dois.',
			'especies' => array(
				'corydoras-aeneus',
				'corydoras-paleatus',
				'corydoras-panda',
				'corydoras-sterbai',
			),
		),
		'bettas' => array(
			'rotulo'   => 'Bettas e gouramis',
			'plural'   => 'bettas e gouramis',
			'singular' => 'todo betta e todo gurami',
			/* A LINHA MESTRA FOI REESCRITA EM 14/09/2026, na leva que a publicou.
			   A de 13/09 prometia um número que esta página não paga: "quanto da
			   superfície do aquário fica livre para eles subirem". A superfície
			   até sairia da aritmética (frente × fundo), mas a AFIRMAÇÃO de que
			   é ela que decide em vez do litro está declarada por fonte para UMA
			   das três — o compêndio diz do betta que a espécie precisa de acesso
			   à camada de ar úmido acima da água — e estendê-la às outras duas é
			   a regra da congênere que esta ilha recusa desde a leva 1. O que a
			   categoria tem para dizer, e paga na tabela linha a linha, é o
			   arranjo social: é o que o próprio critério dela já declarava. */
			'linha_mestra' => 'Betta, colisa-anão e gurami mel dividem a mesma prateleira da loja e não vivem do mesmo jeito: um vive sozinho, um vive em casal e um vive em grupo com hierarquia — e é esse arranjo, e não o litro, que decide o seu aquário.',
			'criterio' => 'Os anabantídeos da família Osphronemidae que a loja brasileira vende como betta, colisa e gurami. Aqui o posto taxonômico SERVE de critério, e é a primeira categoria deste eixo em que ele serve: nos tetras a família não servia (a revisão dos caracídeos deixou tetra em duas famílias e Characidae carrega peixe que ninguém vende como tetra) e nas coridoras o gênero não servia (a revisão da subfamília tirou as quatro do gênero Corydoras na própria fonte). Nesta, as cinco espécies do banco são Osphronemidae e todas as cinco são vendidas com um desses três nomes — não há uma sexta que a família traga de brinde nem uma que ela deixe de fora. O que a família NÃO decide é o arranjo social, e é ele que muda a resposta: dentro do mesmo rótulo estão um peixe que vive sozinho (o betta), um que vive em casal (a colisa-anão) e um que vive em grupo com hierarquia (o gurami mel). Categoria que junta os três tem de dizer isso na primeira linha, em vez de publicar um mínimo só.',
			/* A LEVA 4, 14/09/2026: a lista sai do vazio. As três são as que
			   passam no portão de página do esquema, e a categoria nasce no
			   mínimo exato do 16.5. Os dois guramis grandes do banco — pérola e
			   tricogaster — continuam fora por não terem `convivencia`
			   declarada, medida em quatro passadas e dois corpos. */
			'especies' => array(
				'betta-splendens',
				'trichogaster-lalius',
				'trichogaster-chuna',
				/* OS DOIS GURAMIS GRANDES SÃO DECLARADOS AQUI E O PORTÃO OS BARRA,
				   que é exatamente o ramo que a 1.6.0 escreveu em 13/09/2026 sem
				   ter um caso no banco para exercitá-lo. Sem declará-los, a frase
				   de lista fechada desta página diria que todo betta e todo gurami
				   que o banco sustenta já tem página — e o banco sustenta estes
				   dois, com duas fontes cada; o que falta neles é `convivencia`.
				   Declarados, eles saem da tabela e entram na lista de fora, com
				   nome e causa, e a frase de fechamento muda de forma sozinha. */
				'trichopodus-leerii',
				'trichopodus-trichopterus',
			),
		),
		'ciclideos-anoes' => array(
			'rotulo'   => 'Ciclídeos anões',
			'plural'   => 'ciclídeos anões',
			'singular' => 'todo ciclídeo anão',
			/* PREPARAÇÃO DA LEVA 6, 14/09/2026. O banco fechou em três elegíveis
			   e a categoria ganhou critério e linha mestra — a página ainda NÃO
			   está em `aquametria_peixes_registro()`, então nenhuma URL nasceu
			   aqui e nenhuma leva foi consumida. É o mesmo passo que a `bettas`
			   recebeu em 13/09 às 13h17Z e a `vivaparos` às 21h21Z: quem
			   publicar a leva lê a linha mestra e o critério ANTES de tudo, pela
			   regra que a leva 5 escreveu (texto de categoria escrito antes da
			   leva é afirmação que ninguém mediu).

			   A LINHA MESTRA SAI DA TABELA E DE MAIS NADA, e é o caso mais
			   limpo do eixo inteiro: o ramirezi e o apistogramma agassizi têm
			   EXATAMENTE o mesmo porte declarado (4,2 cm SL, os dois na mesma
			   base científica) e o papilocromis tem 5,6 cm — 1,4 cm a mais. E o
			   aquário dobra: 60 cm de frente para os dois primeiros, 120 para o
			   terceiro. Nenhuma outra categoria deste eixo tem dois peixes de
			   porte IDÊNTICO para provar que o porte não é o que decide. */
			/* SEGUNDA PESSOA ACRESCENTADA EM 22/09/2026, pela leva 7, e este é um
			   defeito que esteve NO AR desde 14/09. A frase dizia "o que dobra o
			   AQUÁRIO", falando do mundo em terceira pessoa, e o VOZ.md manda falar
			   com quem entrou. Ninguém viu porque esta página nunca esteve na lista
			   do `teste-voz.mjs`: a leva 6 acrescentou as quatro URLs ao
			   `teste-peixes.py` e esqueceu do portão da voz, que é escrito à mão e
			   não avisa quem falta. Oito dias verdes sem medir. A afirmação não
			   mudou — mudou uma palavra, e ela é a que a régua cobra. */
			'linha_mestra' => 'Dois destes três têm o mesmo tamanho de corpo e pedem o mesmo aquário; o terceiro tem pouco mais de um centímetro a mais e pede o dobro de frente. O que dobra o seu aquário não é o peixe: é com quantos ele vive.',
			/* O CRITÉRIO, e esta é a PRIMEIRA categoria do eixo em que nem a
			   família nem o gênero servem — nas outras quatro sempre um dos dois
			   serviu ou foi recusado por um motivo taxonômico. Aqui a família
			   Cichlidae carrega, NESTE MESMO BANCO, o oscar (45,7 cm), o
			   acará-disco e o acará-bandeira, que ninguém chama de anão; e os
			   três desta lista estão em dois gêneros diferentes, com dois deles
			   (ramirezi e papilocromis) no mesmo gênero e em pontas opostas da
			   tabela. O que serve é a PRATELEIRA brasileira, e ela é verificável
			   em vez de opinativa: "ciclídeos anões" é uma categoria de loja no
			   Brasil, com endereço próprio na Kauar, na RSDiscus e na Fazenda
			   Submersa, e as três põem os três desta lista lá dentro e nenhuma
			   põe o oscar, o disco ou a bandeira. O porte declarado explica por
			   quê sem precisar de régua nova: os três ficam abaixo de 6 cm e os
			   outros três Cichlidae do banco começam em 13,7 cm. */
			'criterio' => 'Os ciclídeos que a loja brasileira vende na prateleira de ciclídeo anão. A família NÃO serve de critério aqui, e é a primeira categoria deste eixo em que nem ela nem o gênero servem: Cichlidae é a família do oscar, do acará-disco e do acará-bandeira, que estão neste mesmo banco e que ninguém chama de anão; e o gênero também não, porque dois desta lista são Mikrogeophagus e ocupam as duas pontas da tabela, enquanto o terceiro é Apistogramma e cai em cima de um deles. Quem separa é a prateleira, e o porte declarado mostra por quê: os três desta página têm menos de 6 cm de adulto e o menor dos outros Cichlidae do banco tem 13,7 cm. O que esta tabela publica é o ciclídeo anão cujos campos os dois corpos de fonte sustentam, um por um; espécie a um campo de distância fica de fora, e o aquário mínimo dela NÃO é completado pelo da espécie vizinha — o que é regra desta ilha desde a leva 1 e aqui teria custado caro, porque foi exatamente o que uma das buscas ofereceu.',
			/* A LISTA CONTINUA VAZIA, E ISSO É REGRA COM PORTÃO, não esquecimento:
			   a lista de espécies é da LEVA e não da preparação (afirmação 3 do
			   `teste-peixes.py`), porque preenchê-la antes faria a mãe publicar
			   a contagem de uma categoria que o 16.5 ainda não deixou nascer.
			   Esta execução tentou preenchê-la e o portão reprovou — é o caso
			   de régua que PODE falhar, e falhou na bancada em vez de no ar.

			   OS TRÊS QUE JÁ PASSAM NO PORTÃO DE PÁGINA, medidos em 14/09/2026
			   pelo `validar-especies.py` (39 registros, 0 erro) e pelo
			   `gerar-catalogo-especies.py` (31 no catálogo), e que a leva 6
			   escreve aqui na hora de nascer: `mikrogeophagus-ramirezi` (no
			   banco desde 09/09), `apistogramma-agassizii` e
			   `mikrogeophagus-altispinosus` (colhidos nesta execução, para ESTA
			   categoria alcançar o mínimo de três).

			   LEVA 6, 14/09/2026: A LISTA SAI DO VAZIO, porque a página nasceu, e a
			   categoria entra no mínimo EXATO do 16.5, sem folga — a mesma posição
			   da `bettas` e da `vivaparos`. Nenhuma espécie declarada aqui é barrada
			   pelo portão, então a lista de fora desta categoria nasce VAZIA: não
			   existe um quarto ciclídeo anão no banco, nem passando nem barrado. A
			   candidata que faltaria é a `Apistogramma cacatuoides`, e ela não está
			   no banco por RECUSA DE COLETA e não por portão — a base não publica o
			   aquário dela e a busca ofereceu o da congênere. A causa está no
			   `REGISTRO.md` da execução das 21h18Z. */
			'especies' => array(
				'mikrogeophagus-ramirezi',
				'apistogramma-agassizii',
				'mikrogeophagus-altispinosus',
			),
		),
		'danios-e-rasboras' => array(
			'rotulo'   => 'Danios e rasboras',
			'plural'   => 'danios e rasboras',
			'singular' => 'todo danio e toda rasbora',
			/* A LINHA MESTRA SAI DA TABELA E DE MAIS NADA, e aqui ela teve de
			   desviar de uma armadilha de medida que as seis categorias anteriores
			   não tinham. A primeira escrita dizia "o MENOR destes três é o que
			   pede o MAIOR aquário", que é a frase mais forte que esta página
			   poderia publicar — e ela não se sustenta: o porte do paulistinha
			   está declarado em SL (3,8 cm, o corpo sem a cauda) e o do tanictis
			   em TL (4,0 cm, com ela). Na mesma régua a ordem entre os dois pode
			   inverter, e a página estaria apostando numa comparação que nenhuma
			   das duas fontes fez. A versão abaixo diz o que a tabela paga com
			   qualquer medida: os três portes cabem num intervalo de pouco mais de
			   um centímetro, a frente mínima varia em 30 cm, e a frente POR
			   INDIVÍDUO varia em três vezes. Comparar número de medidas diferentes
			   é a mesma família da regra da congênere: parece medição e é
			   vizinhança. */
			'linha_mestra' => 'Três peixes que não passam de 5 cm, vendidos na mesma prateleira, e a frente mínima de um deles é 30 cm maior que a dos outros dois. O espaço que sobra para cada indivíduo varia em três vezes de uma linha a outra desta tabela — e é isso, não o tamanho do peixe, que decide o seu aquário.',
			/* O CRITÉRIO, e esta é a SEGUNDA categoria do eixo em que nem a família
			   nem o gênero servem — a primeira foi a `ciclideos-anoes`. Aqui o
			   motivo é o oposto do dela: lá a família trazia peixe DEMAIS
			   (Cichlidae carrega o oscar de 45,7 cm), e aqui ela deixa peixe de
			   FORA. O tanictis é a única Tanichthyidae do banco, família só dele, e
			   filtrar por Danionidae o excluiria de uma página em que o próprio
			   banco já o coloca: o segundo nome popular brasileiro dele é
			   `paulistinha-da-montanha`, que é o nome do peixe da linha de cima com
			   um sobrenome. O gênero também não serve: são três gêneros para três
			   peixes.

			   O QUE SERVE É O NOME QUE A PESSOA DIGITA, e aqui ele é verificável
			   dentro do próprio banco em vez de depender da leitura de quem
			   escreve: os quatro registros declarados nesta categoria trazem
			   `danio`, `rasbora` ou `paulistinha` entre os nomes populares
			   brasileiros, e nenhum outro registro do banco traz. */
			'criterio' => 'Os peixes de cardume que a loja brasileira vende como danio, rasbora ou paulistinha. Nem a família nem o gênero servem de critério aqui, e a família falha pelo lado contrário ao dos ciclídeos anões: lá ela trazia peixe demais, aqui ela deixa peixe de fora. O tanictis é a única espécie deste banco na família Tanichthyidae — família só dele — e ficaria fora de uma página em que o segundo nome popular brasileiro dele, paulistinha-da-montanha, é o nome da espécie da linha de cima com um sobrenome. O gênero também não serve: são três gêneros para três peixes. Quem separa é o nome que a pessoa digita, e nesta categoria ele é verificável dentro do banco: os registros declarados aqui são exatamente os que trazem danio, rasbora ou paulistinha entre os nomes populares, e nenhum outro registro do banco traz. Uma advertência de medida fica junto da tabela e não aqui, porque ela muda o que dá para comparar: o porte destes registros não está todo na mesma régua — uns declaram o corpo sem a cauda e outros com ela —, então a coluna de porte serve para ler cada linha e não para ordenar as linhas entre si.',
			/* A LEVA 7, 22/09/2026: a lista nasce CHEIA, e é a primeira categoria do
			   eixo em que isso acontece. As seis anteriores foram preparadas numa
			   execução e publicadas noutra, então a lista nascia vazia e saía do
			   vazio na leva; aqui o banco já sustentava as três desde 11/09/2026 e
			   nenhuma coleta foi precisa. O que faltava era a categoria existir.

			   A RASBORA GALÁXIA É DECLARADA AQUI E O PORTÃO A BARRA, e ela é a
			   barrada mais distante do eixo inteiro: faltam-lhe QUATRO campos
			   (frente mínima, convivência, temperatura e a segunda fonte), contra o
			   campo único que faltava ao molly e ao guppy na leva 5. Sem declará-la,
			   a frase de lista fechada desta página diria que todo danio e toda
			   rasbora que o banco sustenta já tem página — e o banco tem o registro
			   dela, com o nome, a família e o porte colhidos em 09/09/2026.
			   Declarada, ela sai da tabela e entra na lista de fora, com nome e
			   causa. */
			'especies' => array(
				'danio-rerio',
				'trigonostigma-heteromorpha',
				'tanichthys-albonubes',
				'danio-margaritatus',
			),
		),
		'acaras' => array(
			'rotulo'   => 'Acarás',
			'plural'   => 'acarás',
			'singular' => 'todo acará grande',
			/* A LINHA MESTRA SAI DA TABELA E DE MAIS NADA, e nesta categoria a
			   coluna que decide não é a do espaço: é a da TEMPERATURA. As sete
			   categorias anteriores tinham, todas, faixas térmicas que se
			   cruzavam — a tabela servia a temperatura como dado de ficha, e
			   nenhuma linha mestra teve o que dizer sobre ela. Aqui as faixas do
			   oscar (22 a 25 °C) e do acará-disco (26 a 30 °C) NÃO SE TOCAM, e
			   as duas vêm da MESMA base científica, o que torna a comparação
			   legítima pela regra da leva 7: aqui não há duas réguas, há uma só.
			   Um grau de distância entre o teto de um e o piso do outro é o que
			   separa dois peixes que a loja põe na mesma prateleira e a SERP
			   responde na mesma página.

			   A FRASE NOMEIA OS DOIS PEIXES E NÃO IMPRIME OS DOIS NÚMEROS, e as
			   duas metades da escolha são deliberadas. Nomear: a linha mestra é
			   a resposta CITÁVEL desta página (seção 5), e afirmação citada fora
			   de contexto sem sujeito não afirma nada — "dois deles" só existe
			   para quem está com a tabela na tela. Não imprimir: o número vive na
			   tabela, que sai do banco, e número digitado em frase é o defeito
			   que esta ilha mais paga. A frase continua verdadeira enquanto a
			   tabela a pagar, e quem mudar a faixa térmica de um dos dois vê a
			   contradição na mesma tela em vez de ver dois números concordando
			   com nada.

			   E A PRIMEIRA TENTATIVA DE NOMEAR OS DOIS QUEBROU DUAS REGRAS DA
			   VOZ, as duas pegas pelo `teste-voz.mjs` antes do ar: ela dizia "a
			   faixa de temperatura QUE A FONTE DECLARA para o oscar" — e
			   procedência não abre página (15.2) —, e trocava "o SEU aquário"
			   por "o mesmo aquário", perdendo a segunda pessoa que o `VOZ.md`
			   manda. As duas cabem na mesma correção: o dono do número sai da
			   frase de abertura e continua ao lado do número, na tabela, que é
			   onde a camada de prova mora.

			   O QUE ELA NÃO DIZ, E É DELIBERADO: nada sobre o porte comparado.
			   O acará-bandeira declara 15,0 cm TL, o oscar 45,7 cm TL e o
			   acará-disco 13,7 cm SL — e comparar o disco com os outros dois
			   seria comparar o corpo sem a cauda com o corpo com ela, que é
			   exatamente o que a leva 7 proibiu. A distância de porte desta
			   categoria é a maior do eixo e mesmo assim ela fica fora da frase,
			   porque metade dela não está na mesma régua. */
			'linha_mestra' => 'Três peixes vendidos na mesma prateleira, e dois deles não cabem na mesma água: a faixa de temperatura do oscar termina antes de a do acará-disco começar. Antes de perguntar quantos litros, veja se esses dois podem dividir o seu aquário — porque essa resposta nenhuma conta de litragem dá.',
			/* O CRITÉRIO, e esta é a TERCEIRA categoria seguida em que o critério
			   da anterior não serve. Mais: é a primeira em que falha justamente o
			   critério que a leva 7 tinha acabado de comemorar por ser verificável
			   dentro do banco em vez de depender da leitura de quem escreve.

			   O NOME NÃO SERVE AQUI, E ISSO SE MEDE: varrendo `nomes_populares_br`
			   do banco inteiro, QUATRO registros trazem "acará" — o acará-bandeira,
			   o acará-disco, o acará-açu (que é o oscar) e o `acará-borboleta`, que
			   é o ramirezi e já é filha de `/peixes/ciclideos-anoes/` desde a leva
			   6. Um critério de nome puxaria uma filha para fora da mãe dela.

			   A FAMÍLIA TAMBÉM NÃO SERVE, pelo motivo que a própria `ciclideos-anoes`
			   já tinha escrito de lá para cá: Cichlidae é a família das seis, e as
			   três de lá têm menos de 6 cm. E o gênero não serve porque são três
			   gêneros para três peixes.

			   O QUE SERVE É O PORTE DECLARADO, e ele é número: os três desta lista
			   começam em 13,7 cm de adulto e os três ciclídeos anões terminam em
			   5,6 cm. Entre 5,6 e 13,7 cm não existe um único Cichlidae neste banco
			   — o corte não passa por cima de nenhum registro, e não é uma linha
			   escolhida para caber no dado: é um vão de oito centímetros vazio.
			   A prateleira brasileira concorda com ele, e é a mesma prova que a
			   `ciclideos-anoes` levantou ao contrário: as lojas que têm endereço de
			   ciclídeo anão põem os três de lá lá dentro e nenhuma põe estes três. */
			'criterio' => 'Os ciclídeos grandes que a loja brasileira vende como acará, e que ela NÃO põe na prateleira de ciclídeo anão. Nem a família, nem o gênero, nem o nome servem de critério aqui, e é a terceira categoria seguida deste eixo em que o critério da anterior falha. A família é a mesma dos ciclídeos anões, que já têm página própria. O gênero são três gêneros para três peixes. E o nome, que foi o que separou os danios e as rasboras, falha pelo lado mais caro: quatro registros deste banco trazem "acará" entre os nomes populares, e o quarto é o acará-borboleta, que é o ramirezi — um critério de nome o tiraria da categoria de que ele é filha. Quem separa é o porte declarado, que é número e não leitura: os três desta tabela começam em 13,7 cm de adulto e os três ciclídeos anões terminam em 5,6 cm, sem um único registro deste banco entre os dois. O que esta tabela publica é o acará cujos campos os dois corpos de fonte sustentam, um por um.',
			/* A LISTA NASCE CHEIA, como a da leva 7, e pelo mesmo desenho: a
			   categoria e as três fichas saem na MESMA execução, então o critério
			   e a linha mestra foram escritos contra a tabela que esta página
			   serve, e não contra uma tabela que ninguém tinha visto ainda. É a
			   regra que a leva 5 deixou — texto de categoria escrito antes da leva
			   é afirmação que ninguém mediu.

			   `barradas` NASCE VAZIA, e é afirmação e não descuido: os seis
			   Cichlidae do banco estão distribuídos entre esta categoria e a
			   `ciclideos-anoes`, os seis passam no portão, e não existe um sétimo
			   ciclídeo no banco — nem passando nem barrado. A frase de lista
			   fechada desta página é verdadeira sem ressalva.

			   O ACARÁ-DISCO ENTROU HÁ POUCAS HORAS, e isso é o que esta lista tem
			   de mais frágil e de mais bem documentado: ele passou treze dias em um
			   corpo de fonte só, e o que o destravou não foi coleta, foi o campo
			   `chao_declarado_para` da versão 5 do esquema, escrito na execução das
			   17h25Z de hoje. A recusa que nomeou o conserto continua gravada em
			   `coletas_recusadas` dentro do registro dele, com `superada_em` e
			   `superada_por` — é a primeira recusa superada desta ilha e a série é
			   o que ensina. */
			'especies' => array(
				'pterophyllum-scalare',
				'astronotus-ocellatus',
				'symphysodon-aequifasciatus',
			),
		),
		'plecos-e-limpa-vidros' => array(
			'rotulo'   => 'Plecos e limpa-vidros',
			'plural'   => 'plecos e limpa-vidros',
			'singular' => 'todo pleco e todo limpa-vidros',
			'criterio' => '',
			'especies' => array(),
		),
		'vivaparos' => array(
			'rotulo'   => 'Vivíparos',
			'plural'   => 'vivíparos',
			'singular' => 'todo vivíparo',
			/* A LINHA MESTRA FOI REESCRITA EM 14/09/2026, na leva que publicou a
			   página, e pelo mesmo motivo que a da `bettas` tinha sido: a de
			   13/09 prometia um número que esta página não paga. Ela dizia que o
			   que decide o aquário é "quantos vão existir daqui a três meses, e o
			   macho é quem manda nessa conta" — e nenhuma fonte deste banco
			   declara taxa de reprodução, ninhada nem prazo. Pior: ela dizia que
			   manda o MACHO e o critério logo abaixo dizia que manda a fêmea, as
			   duas afirmações na mesma tela, nenhuma das duas medida.

			   O que a tabela paga, linha a linha, são duas coisas, e a linha
			   mestra agora diz exatamente essas duas: as três declaram o ARRANJO
			   e nenhuma declara o NÚMERO (a coluna "Como vive" repete "número não
			   declarado" três vezes — é a única categoria do eixo assim), e a
			   frente mínima varia em duas vezes DENTRO de um gênero só. */
			/* E A PRIMEIRA ESCRITA DESTA LINHA REPROVOU NO PORTÃO DA VOZ, por
			   duas coisas ao mesmo tempo: ela abria por "as fontes destes três
			   declaram", que é procedência na primeira frase (15.2), e falava do
			   banco em vez de falar com quem lê. A versão abaixo diz os mesmos
			   dois fatos medidos, na segunda pessoa e sem citar quem declarou —
			   quem declarou está duas telas abaixo, na tabela. */
			'linha_mestra' => 'Vivíparo não tem um número: destes três está declarado com quem cada um vive — mais fêmeas do que machos — e nunca quantos. O que decide o seu aquário é a frente, e entre dois peixes do mesmo gênero, vendidos na mesma prateleira, ela varia em duas vezes.',
			'criterio' => 'Os vivíparos da família Poeciliidae que a loja brasileira vende como plati, espada, molinésia e lebiste. A família serve de critério e o gênero não, e por um motivo que o aquarista reconhece na prateleira: plati e espada são o mesmo gênero e pedem frentes de aquário que diferem em duas vezes, enquanto plati e molinésia são gêneros diferentes e pedem água da mesma dureza. Quem decide a resposta aqui é a frente mínima que a fonte declara para cada espécie, uma por uma, e ela não se deduz do parentesco: a maior distância desta tabela está dentro do gênero Xiphophorus, e não entre gêneros. O que esta tabela publica é o vivíparo cujos sete campos os dois corpos de fonte sustentam; espécie a um campo de distância fica de fora e a frente mínima dela NÃO é completada pela da espécie vizinha, que é o atalho que faria esta lista crescer hoje e mentir amanhã. Quantas estão dentro e quantas esperam está contado logo abaixo da tabela, nunca escrito aqui.',
			/* A LEVA 5, 14/09/2026: a lista sai do vazio. As três que passam no
			   portão de página são as três `Xiphophorus`, e a categoria nasce no
			   mínimo exato do 16.5, sem folga — a mesma posição da `bettas`.

			   AS DUAS `Poecilia` SÃO DECLARADAS AQUI E O PORTÃO AS BARRA, e aqui
			   isso não é refinamento: são os dois vivíparos MAIS vendidos do
			   Brasil. Sem declará-los, a frase de lista fechada desta página
			   diria que todo vivíparo que o banco sustenta já tem página — e o
			   banco sustenta os dois registros, cada um a um campo de distância.
			   Declarados, eles saem da tabela e entram na lista de fora, com nome
			   e causa: o guppy por ter duas urls de um corpo só e o molly por não
			   ter frente mínima declarada por ninguém. */
			'especies' => array(
				'xiphophorus-maculatus',
				'xiphophorus-hellerii',
				'xiphophorus-variatus',
				'poecilia-reticulata',
				'poecilia-sphenops',
			),
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 3. A aritmética — toda ela derivada, nenhuma gravada
 * ------------------------------------------------------------------------- */

/**
 * A faixa de porte de uma espécie: [min, max] em cm.
 *
 * Igual nos dois extremos quando não há divergência declarada; os dois valores
 * do conflito quando há. Quem escolhe o extremo é quem CONSOME: para lotação
 * vale o peixe maior, porque errar para cima de carga é o lado seguro.
 */
if ( ! function_exists( 'aquametria_peixes_porte_faixa' ) ) {
function aquametria_peixes_porte_faixa( $e ) {
	$valores = array( (float) $e['porte_cm'] );
	foreach ( (array) $e['conflitos'] as $c ) {
		if ( 'porte_adulto_cm' !== $c['campo'] ) {
			continue;
		}
		foreach ( (array) $c['valores'] as $v ) {
			if ( is_numeric( $v['valor'] ) ) {
				$valores[] = (float) $v['valor'];
			}
		}
	}
	return array( min( $valores ), max( $valores ) );
}
}

/**
 * O portão de PÁGINA, deste lado — decisão 8 do cabeçalho.
 *
 * Estar no catálogo não basta para ter página própria: a ficha deste eixo se
 * chama "quantos litros para um cardume de X" e abre pela frase que nomeia o
 * cardume mínimo. Espécie que o banco declara de cardume ou de grupo SEM o
 * número não passa. Quem declara convivência solitário, casal ou harém passa
 * sem o número — ali a ausência é a declaração, não o buraco.
 *
 * A régua está ESCRITA aqui e não importada do gerador de catálogo. É a mesma
 * frase que o esquema usa (`minimo_para_sugerir.pagina-especie`), e é o teste
 * que cobra que as duas digam o mesmo — se este arquivo chamasse a régua de
 * quem produziu o dado, as duas metades errariam juntas (seção 8 do contrato).
 */
if ( ! function_exists( 'aquametria_peixes_pode_virar_ficha' ) ) {
function aquametria_peixes_pode_virar_ficha( $e ) {
	/* O VOCABULÁRIO FECHADO É PARTE DO PORTÃO desde 14/09/2026 (leva 5), e essa
	   metade faltava. O cabeçalho da 1.7.0 já dizia que termo fora do mapa do
	   arranjo "devolve null e a espécie não vira ficha" — e não era verdade:
	   bastava `cardume_minimo` preenchido para a espécie passar por aqui com
	   `convivencia` qualquer, e a ficha então abriria chamando de "cardume
	   mínimo" um peixe que a fonte não declarou de cardume. É a mesma família do
	   defeito que a leva 4 consertou, um nível mais fundo. O esquema enumera os
	   cinco valores e o validador reprova o sexto; esta linha é o que garante
	   que, se um sexto nascer no esquema sem nascer no mapa, a página não sai em
	   vez de sair com o vocabulário errado. */
	if ( null === aquametria_peixes_arranjo( $e ) ) {
		return false;
	}
	if ( ! empty( $e['cardume'] ) ) {
		return true;
	}
	return in_array( $e['convivencia'], array( 'solitario', 'casal', 'harem' ), true );
}
}

/**
 * A faixa de frente mínima declarada: [min, max] em cm. Mesma regra do porte,
 * e aqui o extremo seguro é o MAIOR — aquário maior nunca fez mal a cardume.
 */
if ( ! function_exists( 'aquametria_peixes_frente_faixa' ) ) {
function aquametria_peixes_frente_faixa( $e ) {
	$valores = array( (float) $e['frente_cm'] );
	foreach ( (array) $e['conflitos'] as $c ) {
		if ( 'comprimento_minimo_aquario_cm' !== $c['campo'] ) {
			continue;
		}
		foreach ( (array) $c['valores'] as $v ) {
			if ( is_numeric( $v['valor'] ) ) {
				$valores[] = (float) $v['valor'];
			}
		}
	}
	return array( min( $valores ), max( $valores ) );
}
}

/**
 * A leitura per capita do mínimo declarado: frente mínima ÷ cardume mínimo.
 *
 * Derivado `frente_por_individuo_cm` do esquema. Sai na tela como leitura, e
 * NUNCA multiplicado para extrapolar cardume — ver decisão 2 do cabeçalho.
 * Devolve null quando a espécie não declara cardume (solitário, casal, harém).
 */
if ( ! function_exists( 'aquametria_peixes_frente_por_individuo' ) ) {
function aquametria_peixes_frente_por_individuo( $e ) {
	if ( empty( $e['cardume'] ) ) {
		return null;
	}
	$frente = aquametria_peixes_frente_faixa( $e );
	return $frente[1] / (float) $e['cardume'];
}
}

/**
 * O CHÃO DECLARADO É UMA AFIRMAÇÃO SOBRE UMA POPULAÇÃO (1.12.0, 22/09/2026).
 *
 * `base_minima_cm` sempre foi um número sobre um punhado de peixes — e até a
 * versão 5 do esquema não havia onde dizer QUAL punhado. O preço esteve oito
 * dias no ar: a ficha do apistogramma agassizi abria com "para um harém de
 * apistogramma agassizi ... o seu aquário precisa de 60 cm de frente por 30 cm
 * de fundo", e os 30 cm de fundo são do compêndio, que os declarou para UM
 * CASAL. A proibição existia, escrita em maiúsculas dentro do `observacao`
 * daquele registro — "O QUE A FICHA NÃO PODE FAZER: prometer que 60 x 30 cm
 * serve ao harém" —, e prosa não barra página.
 *
 * Os termos são ORDENADOS por população, e é essa ordem que decide: aquário
 * declarado para um grupo abriga um casal, e o contrário não vale.
 * `nao-declarado` fica FORA da ordem de propósito — não é um nível, é a
 * ausência de nível: a fonte publicou a base como o mínimo da espécie sem
 * nomear população nenhuma, e aí ela vale para o arranjo que o registro
 * publica. É o caso mais comum, e é como este eixo inteiro sempre a leu.
 */
if ( ! function_exists( 'aquametria_peixes_nivel_do_chao' ) ) {
function aquametria_peixes_nivel_do_chao( $termo ) {
	$niveis = array(
		'juvenis'     => 0,
		'um-exemplar' => 1,
		'casal'       => 2,
		'grupo'       => 3,
	);
	return isset( $niveis[ $termo ] ) ? $niveis[ $termo ] : null;
}
}

/**
 * A população que a FICHA publica. Harém e cardume caem os dois em `grupo`
 * porque os dois são vários peixes no mesmo aquário — e é exatamente por isso
 * que uma base declarada para um casal não serve nenhum dos dois.
 */
if ( ! function_exists( 'aquametria_peixes_populacao_publicada' ) ) {
function aquametria_peixes_populacao_publicada( $e ) {
	$mapa = array(
		'solitario' => 'um-exemplar',
		'casal'     => 'casal',
		'cardume'   => 'grupo',
		'grupo'     => 'grupo',
		'harem'     => 'grupo',
	);
	$conv = isset( $e['convivencia'] ) ? $e['convivencia'] : '';
	return isset( $mapa[ $conv ] ) ? $mapa[ $conv ] : null;
}
}

/** O chão declarado cobre a população que esta ficha publica? */
if ( ! function_exists( 'aquametria_peixes_chao_serve_o_arranjo' ) ) {
function aquametria_peixes_chao_serve_o_arranjo( $e ) {
	$arranjos = isset( $e['chao_para'] ) ? (array) $e['chao_para'] : array();
	if ( ! $arranjos || in_array( 'nao-declarado', $arranjos, true ) ) {
		return true;
	}
	$populacao = aquametria_peixes_populacao_publicada( $e );
	if ( null === $populacao ) {
		return true;
	}
	$teto = null;
	foreach ( $arranjos as $a ) {
		$n = aquametria_peixes_nivel_do_chao( $a );
		if ( null !== $n && ( null === $teto || $n > $teto ) ) {
			$teto = $n;
		}
	}
	if ( null === $teto ) {
		return true;
	}
	return aquametria_peixes_nivel_do_chao( $populacao ) <= $teto;
}
}

/**
 * O FUNDO QUE ESTA PÁGINA PODE PUBLICAR, e não o fundo que o banco tem.
 *
 * UMA régua, UM lugar: a ficha e o JSON-LD liam `base_largura` cada um por si,
 * e duas leituras do mesmo campo são duas respostas no dia em que uma delas
 * ganhar condição. Quem não passa aqui não tem fundo na tela, não tem tabela de
 * litros por altura, não tem a tabela de quantos cabem no aquário mínimo e não
 * tem litro no schema — porque as quatro coisas saem da multiplicação por um
 * número que foi declarado para outra gente.
 */
if ( ! function_exists( 'aquametria_peixes_fundo' ) ) {
function aquametria_peixes_fundo( $e ) {
	if ( empty( $e['base_largura'] ) ) {
		return null;
	}
	if ( ! aquametria_peixes_chao_serve_o_arranjo( $e ) ) {
		return null;
	}
	return (float) $e['base_largura'];
}
}

/**
 * O fundo existe no banco e foi declarado para OUTRA população.
 *
 * Serve para a página distinguir as duas ausências, que são diferentes para
 * quem lê: "ninguém declarou largura" e "a largura declarada não é sobre estes
 * peixes". A segunda é conteúdo — tem número, tem fonte e tem para quem —, e
 * calá-la seria repetir, do outro lado, o erro de publicá-la sem escopo.
 */
if ( ! function_exists( 'aquametria_peixes_fundo_de_outro_arranjo' ) ) {
function aquametria_peixes_fundo_de_outro_arranjo( $e ) {
	if ( empty( $e['base_largura'] ) || aquametria_peixes_chao_serve_o_arranjo( $e ) ) {
		return null;
	}
	$de = array(
		'juvenis'     => 'juvenis',
		'um-exemplar' => 'um exemplar adulto',
		'casal'       => 'um casal',
		'grupo'       => 'um grupo',
	);
	$nomes = array();
	foreach ( (array) $e['chao_para'] as $a ) {
		if ( isset( $de[ $a ] ) ) {
			$nomes[] = $de[ $a ];
		}
	}
	if ( ! $nomes ) {
		return null;
	}
	return array(
		'largura' => (float) $e['base_largura'],
		'para'    => aquametria_peixes_lista_em_ou( $nomes ),
	);
}
}

/** "a" · "a ou b" · "a, b ou c" — a mesma juntada que o resto da ficha usa. */
if ( ! function_exists( 'aquametria_peixes_lista_em_ou' ) ) {
function aquametria_peixes_lista_em_ou( $itens ) {
	$itens = array_values( array_filter( (array) $itens ) );
	if ( count( $itens ) < 2 ) {
		return isset( $itens[0] ) ? $itens[0] : '';
	}
	$ultimo = array_pop( $itens );
	return implode( ', ', $itens ) . ' ou ' . $ultimo;
}
}

/** Volume bruto da lâmina, em litros: a conta de C1, antes de vidro e substrato. */
if ( ! function_exists( 'aquametria_peixes_volume_bruto' ) ) {
function aquametria_peixes_volume_bruto( $comprimento_cm, $largura_cm, $altura_cm ) {
	if ( ! $comprimento_cm || ! $largura_cm || ! $altura_cm ) {
		return null;
	}
	return ( (float) $comprimento_cm * (float) $largura_cm * (float) $altura_cm ) / 1000.0;
}
}

/** As três alturas comuns de aquário que a tabela varre. A fonte declara base, nunca altura. */
if ( ! function_exists( 'aquametria_peixes_alturas' ) ) {
function aquametria_peixes_alturas() {
	return array( 30, 35, 40 );
}
}

/**
 * Litros que N exemplares pedem, pelos três critérios brasileiros.
 * Recebe a soma dos comprimentos adultos em cm e devolve os três números.
 */
if ( ! function_exists( 'aquametria_peixes_litros_por_criterio' ) ) {
function aquametria_peixes_litros_por_criterio( $soma_cm ) {
	$soma_cm = (float) $soma_cm;
	return array(
		'classica'     => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_CLASSICA,
		'meio'         => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_MEIO,
		'conservadora' => $soma_cm * AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA,
	);
}
}

/**
 * Quantos exemplares caberiam num volume, pelos três critérios. É a pergunta
 * inversa, e é a que a pessoa faz de verdade quando já tem o aquário.
 */
if ( ! function_exists( 'aquametria_peixes_quantos_cabem' ) ) {
function aquametria_peixes_quantos_cabem( $litros, $porte_cm ) {
	if ( ! $litros || ! $porte_cm ) {
		return array();
	}
	$litros  = (float) $litros;
	$porte   = (float) $porte_cm;
	return array(
		'classica'     => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA ) / $porte ),
		'meio'         => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_MEIO ) / $porte ),
		'conservadora' => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA ) / $porte ),
	);
}
}

/**
 * O ARRANJO SOCIAL DECLARADO, e ele decide a frase E a tabela (1.7.0, leva 4).
 *
 * Até a leva 3 as ONZE fichas no ar eram `convivencia: cardume`, sem exceção, e
 * por isso a palavra "cardume" estava DIGITADA em sete lugares do corpo da
 * ficha: na abertura, na legenda da tabela de lotação, no contraexemplo do
 * cubo, na chamada do filtro, no bloco da espécie agressiva e no JSON-LD. Era
 * verdade em todas as páginas publicadas e é FALSA em três das quatro que a
 * leva 4 traz: o betta vive sozinho, a colisa-anão vive em casal e o gurami mel
 * vive em grupo — e a fonte deste último escreve, com todas as letras, que a
 * espécie NÃO é gregária no sentido dos peixes de cardume.
 *
 * É a cicatriz da seção 8 do `ARQUIPELAGO.md` em estado puro: o esquema desta
 * ilha permite `solitario`, `casal`, `harem` e `grupo` desde o primeiro dia —
 * `aquametria_peixes_pode_virar_ficha()` cita os três primeiros pelo nome —, e
 * o banco nunca tinha produzido um. Régua escrita para um mundo que nunca
 * aconteceu nasce errada sem poder falhar.
 *
 * O VOCABULÁRIO É FECHADO e a tradução mora neste mapa, num lugar só. Termo que
 * não estiver aqui devolve `null`, e quem chama trata isso como espécie que não
 * vira ficha — inventar um coletivo para valor novo é pior que não publicar.
 *
 * `fixo` é a chave da tabela: quando a fonte declara um arranjo que FECHA o
 * número (um por aquário, um casal), a escada de lotação tem um degrau só e
 * nada acima dele, porque acima dele a fonte diz não. Onde a fonte declara um
 * número de grupo, a escada começa nele. Onde declara o arranjo e não o número
 * (harém), a escada é a de leitura e NENHUMA linha se chama mínimo.
 */
if ( ! function_exists( 'aquametria_peixes_arranjo' ) ) {
function aquametria_peixes_arranjo( $e ) {
	$mapa = array(
		'cardume' => array(
			'fixo'     => null,
			'coletivo' => 'cardume',
			'acao'     => 'nadar em cardume',
			'curto'    => 'em cardume',
			'vive'     => 'vive em cardume',
			'abertura' => '',
			'de'       => 'um cardume de',
			'este'     => 'este cardume',
			'minimo'   => 'cardume mínimo',
		),
		'grupo' => array(
			'fixo'     => null,
			'coletivo' => 'grupo',
			'acao'     => 'viver em grupo',
			'curto'    => 'em grupo',
			'vive'     => 'vive em grupo',
			'abertura' => '',
			'de'       => 'um grupo de',
			'este'     => 'este grupo',
			'minimo'   => 'grupo mínimo',
		),
		'harem' => array(
			'fixo'     => null,
			'coletivo' => 'harém',
			'acao'     => 'viver em harém',
			'curto'    => 'em harém',
			'vive'     => 'vive em harém',
			/* A ABERTURA DO HARÉM NASCEU NA LEVA 5 (14/09/2026), e antes dela
			   este campo era a string vazia porque nenhuma página o usava. Sem
			   ela a ficha caía no ramo de resgate, que abre pela tradução do
			   `como_vive()` — e essa tradução carrega a oração do temperamento,
			   "e a fonte o declara pacífico". A abertura da ficha citando quem
			   declarou é exatamente o que o item 4 do despacho da Sentinela de
			   13/09/2026 tirou das onze fichas antigas (15.2), e ele voltaria
			   pela porta de trás na primeira página de harém.

			   O que a frase diz é a tradução do próprio termo do esquema, do
			   mesmo jeito que "e é um por aquário, não dois" traduz `solitario`:
			   os três registros de harém do banco têm a mesma sentença de fonte
			   por trás — mais fêmeas do que machos, para dissipar o assédio do
			   macho — e nenhum deles declara QUANTAS. É por isso que a frase
			   não traz número, e é por isso que `minimo` fica vazio. */
			'abertura' => 'e harém quer dizer mais fêmeas do que machos, nunca um casal',
			'de'       => 'um harém de',
			'este'     => 'este harém',
			'minimo'   => '',
		),
		'solitario' => array(
			'fixo'     => 1,
			'coletivo' => 'peixe',
			'acao'     => 'viver sozinho',
			'curto'    => 'sozinho',
			'vive'     => 'vive sozinho',
			'abertura' => 'e é um por aquário, não dois',
			'de'       => 'um',
			'este'     => 'este peixe',
			'minimo'   => '',
		),
		'casal' => array(
			'fixo'     => 2,
			'coletivo' => 'casal',
			'acao'     => 'viver em casal',
			'curto'    => 'em casal',
			'vive'     => 'vive em casal',
			'abertura' => 'e são dois, não um macho sozinho',
			'de'       => 'um casal de',
			'este'     => 'este casal',
			'minimo'   => '',
		),
	);
	$chave = isset( $e['convivencia'] ) ? $e['convivencia'] : '';
	if ( ! isset( $mapa[ $chave ] ) ) {
		return null;
	}
	$a           = $mapa[ $chave ];
	$a['chave']  = $chave;
	$a['numero'] = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : null;
	/* O número que a fonte fixa vence o campo de contagem: espécie solitária com
	   `cardume` gravado seria contradição do banco, e a tela não é o lugar de
	   desempatar isso em silêncio — o validador do banco é. */
	if ( null !== $a['fixo'] ) {
		$a['numero'] = $a['fixo'];
	}
	return $a;
}
}

/**
 * O arranjo em uma célula de tabela: a forma de viver mais o número, quando há.
 *
 * É o que substitui a coluna "Cardume mínimo" na categoria que mistura
 * arranjos. Ali "não declarado" seria a resposta errada para dois dos três — a
 * fonte DECLARA quantos cabem no betta e na colisa, e o que ela não declara é
 * um cardume, que é outra coisa.
 */
if ( ! function_exists( 'aquametria_peixes_arranjo_curto' ) ) {
function aquametria_peixes_arranjo_curto( $e ) {
	$a = aquametria_peixes_arranjo( $e );
	if ( ! $a ) {
		return 'não declarado';
	}
	if ( null !== $a['fixo'] ) {
		return $a['curto'] . ', ' . $a['fixo'] . ' por aquário';
	}
	if ( ! empty( $e['cardume'] ) ) {
		return ! empty( $e['cardume_ate'] )
			? $a['curto'] . ', ' . (int) $e['cardume'] . ' a ' . (int) $e['cardume_ate']
			: $a['curto'] . ', ' . (int) $e['cardume'] . ' ou mais';
	}
	return $a['curto'] . ', número não declarado';
}
}

/**
 * A RÉGUA DE LOTAÇÃO CONTRA A BASE DECLARADA, comparada e nunca afirmada.
 *
 * Nasceu de um defeito medido em bancada em 14/09/2026, antes de a leva ir ao
 * ar, e ele é o retrato do que esta leva inteira persegue: a primeira escrita
 * do ramo do arranjo fixo dizia, de frase pronta, que "as duas réguas ficam bem
 * abaixo da base que a fonte declara". Era VERDADE no betta — 6,5 a 26 litros
 * contra 47,3 da base — e FALSA na página do lado: no casal de colisa-anão o
 * critério conservador pede 76 litros e a base dá 63. A afirmação nasceu certa
 * na primeira página em que foi escrita e foi ao HTML errada na segunda, que é
 * exatamente a forma do "número de tela digitado" desta fábrica, com uma
 * agravante: ela também ia dentro do JSON-LD, onde um modelo de linguagem a
 * cita sem ter como conferir.
 *
 * Devolve os três números e a comparação JÁ RESOLVIDA, para que as duas
 * superfícies que a publicam — o corpo e o FAQ — nunca possam discordar.
 */
if ( ! function_exists( 'aquametria_peixes_lotacao_contra_base' ) ) {
function aquametria_peixes_lotacao_contra_base( $e, $frente, $porte, $larg, $n ) {
	$l = aquametria_peixes_litros_por_criterio( $n * $porte[1] );
	$alturas = aquametria_peixes_alturas();
	$altura  = $alturas[1];
	$base    = aquametria_peixes_volume_bruto( $frente[1], $larg, $altura );
	if ( null === $base ) {
		/* Sem o fundo declarado não existe litro da base, e comparar com um
		   fundo inventado seria o atalho que a decisão 7 deste snippet recusa. */
		return array( 'base' => null, 'litros' => $l, 'altura' => $altura, 'frase' => '' );
	}
	if ( $l['conservadora'] < $base ) {
		$frase = 'as duas ficam abaixo dos ';
	} elseif ( $l['classica'] >= $base ) {
		$frase = 'as duas ficam acima dos ';
	} else {
		$frase = 'uma delas fica abaixo e a outra acima dos ';
	}
	$frase .= aquametria_peixes_num( $base ) . ' litros que essa base dá num aquário de '
		. aquametria_peixes_num( $altura ) . ' cm de altura';
	return array( 'base' => $base, 'litros' => $l, 'altura' => $altura, 'frase' => $frase );
}
}

/**
 * Os degraus que a tabela pré-renderizada varre.
 *
 * Três mundos, e o do meio é o único que existia até a leva 3:
 *   - arranjo FIXO pela fonte (solitário, casal): um degrau só, o da fonte;
 *   - número declarado (cardume, grupo): começa nele e sobe pela escada;
 *   - arranjo sem número (harém): a escada de leitura inteira, sem mínimo.
 */
if ( ! function_exists( 'aquametria_peixes_degraus_de_cardume' ) ) {
function aquametria_peixes_degraus_de_cardume( $e ) {
	$escada  = array( 6, 8, 10, 12, 15, 20 );
	$arranjo = aquametria_peixes_arranjo( $e );
	if ( $arranjo && null !== $arranjo['fixo'] ) {
		return array( $arranjo['fixo'] );
	}
	if ( empty( $e['cardume'] ) ) {
		return $escada;
	}
	$minimo  = (int) $e['cardume'];
	/* O TETO DECLARADO É DEGRAU, sempre: a fonte que recomenda "4 a 6" nomeou
	   os dois números, e a escada de leitura (6, 8, 10...) só por acaso teria o
	   segundo deles. Num peixe cuja faixa fosse "5 a 7" o 7 não apareceria em
	   linha nenhuma, e a página publicaria uma recomendação sem a conta dela. */
	$degraus = array( $minimo );
	if ( ! empty( $e['cardume_ate'] ) ) {
		$degraus[] = (int) $e['cardume_ate'];
	}
	foreach ( $escada as $n ) {
		if ( $n > $minimo ) {
			$degraus[] = $n;
		}
	}
	sort( $degraus );
	return array_values( array_unique( $degraus ) );
}
}

/**
 * Quem divide a MESMA ÁGUA: interseção das faixas de temperatura declaradas.
 *
 * NÃO é veredito de convivência — ver decisão 5 do cabeçalho. Três condições,
 * todas medidas em campo declarado:
 *   1. a faixa de temperatura encosta na da espécie da página em 2 °C ou mais;
 *   2. a frente mínima declarada do companheiro cabe na frente da página, ou
 *      seja: o aquário mínimo desta ficha também serve para ele;
 *   3. o banco não declara o companheiro agressivo.
 *
 * Devolve array( 'dentro' => ids, 'maior' => ids, 'agressivos' => ids ), porque
 * a página deve ao leitor o nome de quem ficou de fora e por qual das duas
 * causas (seção 7: causa que o código separa, o texto separa).
 */
if ( ! function_exists( 'aquametria_peixes_mesma_agua' ) ) {
function aquametria_peixes_mesma_agua( $id ) {
	$catalogo = aquametria_peixes_catalogo();
	if ( ! isset( $catalogo[ $id ] ) ) {
		return array( 'dentro' => array(), 'maior' => array(), 'agressivos' => array() );
	}
	$alvo   = $catalogo[ $id ];
	$frente = aquametria_peixes_frente_faixa( $alvo );

	$dentro     = array();
	$maior      = array();
	$agressivos = array();

	foreach ( $catalogo as $outro_id => $o ) {
		if ( $outro_id === $id ) {
			continue;
		}
		$sobreposicao = min( (float) $alvo['temp_max'], (float) $o['temp_max'] )
			- max( (float) $alvo['temp_min'], (float) $o['temp_min'] );
		if ( $sobreposicao < 2 ) {
			continue;
		}
		if ( 'agressivo' === $o['comportamento'] ) {
			$agressivos[] = $outro_id;
			continue;
		}
		$frente_outro = aquametria_peixes_frente_faixa( $o );
		if ( $frente_outro[1] > $frente[1] ) {
			$maior[] = $outro_id;
			continue;
		}
		$dentro[ $outro_id ] = $sobreposicao;
	}

	/* Ordem: maior sobreposição primeiro, e entre iguais o peixe menor antes —
	   afinidade declarada, nunca sorteio (16.4c). */
	uksort( $dentro, function ( $a, $b ) use ( $dentro, $catalogo ) {
		if ( $dentro[ $a ] !== $dentro[ $b ] ) {
			return ( $dentro[ $a ] < $dentro[ $b ] ) ? 1 : -1;
		}
		$pa = (float) $catalogo[ $a ]['porte_cm'];
		$pb = (float) $catalogo[ $b ]['porte_cm'];
		if ( $pa === $pb ) {
			return strcmp( $a, $b );
		}
		return ( $pa > $pb ) ? 1 : -1;
	} );

	return array(
		'dentro'     => array_keys( $dentro ),
		'maior'      => $maior,
		'agressivos' => $agressivos,
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. Texto: nome, número e unidade
 * ------------------------------------------------------------------------- */

/**
 * Como a espécie vive, na língua de quem compra.
 *
 * O banco guarda `cardume`, `grupo`, `solitario`, `casal`, `harem` — vocabulário
 * de campo do esquema, não de tela. A tradução é palavra por palavra e não
 * acrescenta juízo nenhum: o que a fonte declarou continua sendo o que a tela
 * diz. Termo que não estiver no mapa sai como veio, porque inventar tradução
 * para valor novo é pior que mostrar o valor cru.
 */
if ( ! function_exists( 'aquametria_peixes_como_vive' ) ) {
function aquametria_peixes_como_vive( $e ) {
	$convivencia = array(
		'cardume'   => 'em cardume',
		'grupo'     => 'em grupo',
		'solitario' => 'sozinho',
		'casal'     => 'em casal',
		'harem'     => 'em harém, um macho para várias fêmeas',
	);
	$comportamento = array(
		'pacifico'  => 'pacífico',
		'agressivo' => 'agressivo',
	);

	$texto = isset( $convivencia[ $e['convivencia'] ] ) ? $convivencia[ $e['convivencia'] ] : $e['convivencia'];
	if ( $e['comportamento'] ) {
		$c = isset( $comportamento[ $e['comportamento'] ] ) ? $comportamento[ $e['comportamento'] ] : $e['comportamento'];
		$texto .= ', e a fonte o declara ' . $c;
	}
	return $texto;
}
}

/**
 * Concordância de número: a forma singular quando a contagem é UM.
 *
 * Nasceu na leva 5 (14/09/2026), e as três frases que ela conserta estavam no ar
 * desde 12/09 sem poder errar. "N ficaram fora porque o banco os declara
 * agressivos" é verdade com dois e é agramatical com um — e até esta leva o
 * único peixe agressivo do banco, o mato-grosso, ou encostava na faixa de
 * temperatura da ficha junto com o betta (dois) ou não encostava (zero, e a
 * frase nem sai). O platy e o plati variatus são as primeiras fichas em que ele
 * aparece SOZINHO. Mesma coisa em "cabem N": só um peixe grande o bastante faz
 * o critério conservador arredondar para baixo até um, e o peixe-espada, com
 * 16 cm, é o maior peixe com ficha desta ilha.
 *
 * A régua é a contagem, nunca o texto: quem chama passa as duas formas e o
 * número que ele mesmo contou.
 */
if ( ! function_exists( 'aquametria_peixes_concorda' ) ) {
function aquametria_peixes_concorda( $n, $singular, $plural ) {
	return ( 1 === (int) $n ) ? $singular : $plural;
}
}

/** O nome que a pessoa digita: o primeiro popular do banco. */
if ( ! function_exists( 'aquametria_peixes_nome' ) ) {
function aquametria_peixes_nome( $e ) {
	return isset( $e['populares'][0] ) ? $e['populares'][0] : $e['cientifico'];
}
}

/** Número com vírgula decimal e sem zero à direita inútil. */
if ( ! function_exists( 'aquametria_peixes_num' ) ) {
function aquametria_peixes_num( $v, $casas = 1 ) {
	if ( null === $v ) {
		return '—';
	}
	$v = (float) $v;
	if ( abs( $v - round( $v ) ) < 0.05 ) {
		return number_format_i18n( round( $v ), 0 );
	}
	return number_format_i18n( $v, $casas );
}
}

/** "2,2 cm" ou "2,5 a 3,0 cm" quando a fonte discorda. */
if ( ! function_exists( 'aquametria_peixes_faixa_texto' ) ) {
function aquametria_peixes_faixa_texto( $faixa, $unidade = 'cm' ) {
	if ( abs( $faixa[0] - $faixa[1] ) < 0.01 ) {
		return aquametria_peixes_num( $faixa[0] ) . ' ' . $unidade;
	}
	return aquametria_peixes_num( $faixa[0] ) . ' a ' . aquametria_peixes_num( $faixa[1] ) . ' ' . $unidade;
}
}

/**
 * O nome de um campo do banco, na língua de quem lê — e a unidade dele.
 *
 * `comprimento_minimo_aquario_cm` é nome de campo de esquema, e ele chegou a
 * sair na tela do bloco de divergência antes desta função existir. Campo que
 * não estiver no mapa sai como veio, de propósito: nome cru é feio e avisa,
 * enquanto nome inventado engana.
 */
if ( ! function_exists( 'aquametria_peixes_campo_na_tela' ) ) {
function aquametria_peixes_campo_na_tela( $campo ) {
	$mapa = array(
		'porte_adulto_cm'               => array( 'o porte adulto', 'cm' ),
		'comprimento_minimo_aquario_cm' => array( 'a frente mínima do aquário', 'cm' ),
		'base_minima_cm'                => array( 'a base mínima do aquário', 'cm' ),
		'temperatura_C'                 => array( 'a temperatura', '°C' ),
		'cardume_minimo'                => array( 'o cardume mínimo', 'exemplares' ),
		'ph'                            => array( 'o pH', '' ),
		'dureza_dgh'                    => array( 'a dureza da água', 'dGH' ),
		'expectativa_vida_anos'         => array( 'a expectativa de vida', 'anos' ),
	);
	return isset( $mapa[ $campo ] ) ? $mapa[ $campo ] : array( $campo, '' );
}
}

/** dd/mm/aaaa a partir da data ISO do banco. */
if ( ! function_exists( 'aquametria_peixes_data_br' ) ) {
function aquametria_peixes_data_br( $iso ) {
	$partes = explode( '-', (string) $iso );
	if ( 3 !== count( $partes ) ) {
		return (string) $iso;
	}
	return $partes[2] . '/' . $partes[1] . '/' . $partes[0];
}
}

/** O corpo de fonte que sustenta um campo, com a data. '' quando nenhum sustenta. */
if ( ! function_exists( 'aquametria_peixes_fonte_do_campo' ) ) {
function aquametria_peixes_fonte_do_campo( $e, $campo ) {
	foreach ( (array) $e['fontes'] as $f ) {
		if ( in_array( $campo, (array) $f['campos'], true ) ) {
			return $f;
		}
	}

	/* Duas substituições declaradas, e as duas são do MESMO fato colhido:
	   - o nome científico é nomeado por quem classifica a espécie, e no banco
	     quem sustenta `familia` é o corpo taxonômico. Sem esta linha a ficha
	     dizia "sem fonte que sustente" para o nome científico que a própria
	     FishBase publicou, o que é falso na direção pior — a de parecer que a
	     ilha não sabe de onde veio o dado que ela tem;
	   - a frente mínima e a base mínima são o mesmo número lido de dois jeitos
	     (comprimento, ou comprimento × largura), e há registro em que a fonte
	     declara só um dos dois campos. */
	$substitutos = array(
		'nome_cientifico'               => 'familia',
		'comprimento_minimo_aquario_cm' => 'base_minima_cm',
		'base_minima_cm'                => 'comprimento_minimo_aquario_cm',
	);
	if ( isset( $substitutos[ $campo ] ) ) {
		foreach ( (array) $e['fontes'] as $f ) {
			if ( in_array( $substitutos[ $campo ], (array) $f['campos'], true ) ) {
				return $f;
			}
		}
	}

	return array();
}
}

/* ---------------------------------------------------------------------------
 * 5. A ficha de espécie (nível 3)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_ficha_html' ) ) {
function aquametria_peixes_ficha_html( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ]['especie'] ) ) {
		return '';
	}
	$catalogo = aquametria_peixes_catalogo();
	$id       = $registro[ $slug ]['especie'];
	if ( ! isset( $catalogo[ $id ] ) ) {
		/* Espécie que saiu do portão de página some da tela em vez de servir
		   ficha pela metade. Página sem corpo é página fina, e o teste reprova. */
		return '';
	}
	if ( ! aquametria_peixes_pode_virar_ficha( $catalogo[ $id ] ) ) {
		/* Decisão 8: espécie de cardume sem o número do cardume não vira ficha.
		   Devolver vazio aqui é o mesmo tratamento de quem sai do catálogo —
		   página sem corpo é página fina, e o portão do teste reprova antes de
		   a URL nascer. */
		return '';
	}
	$e      = $catalogo[ $id ];
	$nome   = aquametria_peixes_nome( $e );
	$porte  = aquametria_peixes_porte_faixa( $e );
	$frente = aquametria_peixes_frente_faixa( $e );
	$larg    = aquametria_peixes_fundo( $e );
	$card    = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : null;
	$arranjo = aquametria_peixes_arranjo( $e );

	$html = '<div class="aqm-px aqm-px-ficha">';

	/* --- 5.1 A resposta antes da explicação (seção 5, item 2). Frase
	   autossuficiente: sobrevive a ser citada fora de contexto. --- */
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">';
	/* A ABERTURA NÃO CITA QUEM DECLAROU — item 4 do despacho da Sentinela de
	   13/09/2026. Até aqui as 11 fichas começavam por "Para os N <peixe> que A
	   FONTE DECLARA como cardume mínimo ... e A FONTE DECLARA a BASE, não o
	   litro": duas menções à fonte na primeira frase da página, e a 15.2 manda a
	   procedência morar na tabela, no "como sabemos" e no JSON-LD. A prova não
	   foi apagada, foi só deixada onde ela já estava — duas telas abaixo, a
	   tabela "O que as fontes declaram sobre o <peixe>" traz cada linha com o
	   corpo que a sustenta e a data da coleta, cardume e base inclusive.

	   O QUE A REESCRITA TINHA DE PRESERVAR, e é a decisão 7 deste snippet: 14
	   dos 36 registros do banco declaram COMPRIMENTO e não BASE, e esta frase é
	   o lugar onde a diferença aparece na tela. Ela continua aparecendo em dois
	   lugares ao mesmo tempo, e nenhum deles precisa da palavra "fonte": o
	   trecho "por Y cm de fundo" só existe quando há fundo declarado, e a
	   palavra final é BASE ou COMPRIMENTO. Quem tem só o comprimento diz que o
	   fundo FICA EM ABERTO — que é o que um aquarista diria, e não um buraco
	   escondido. */
	/* DOIS RAMOS, e eram TRÊS até a leva 5 (14/09/2026). O ramo do arranjo que
	   FIXA o número (solitário, casal) e o do arranjo SEM número (harém) davam,
	   depois do conserto desta leva, a MESMA frase byte a byte — e foi a mutação
	   82 que mostrou isso, ao recusar operar sobre um alvo que aparecia DUAS
	   vezes. Duas cópias da mesma frase são duas frases que vão divergir, e o
	   motivo de elas serem iguais não é coincidência: o que a abertura precisa
	   dizer, nos dois casos, é O ARRANJO — porque em nenhum dos dois existe um
	   número de exemplares que a fonte declare para a página abrir. O que separa
	   solitário e casal do harém é a ESCADA, e ela é decidida em
	   `aquametria_peixes_degraus_de_cardume()`, que continua com os três mundos.

	   A GUARDA DO PRIMEIRO RAMO É O RÓTULO, e não a presença do número: espécie
	   com `cardume_minimo` preenchido e `convivencia` de casal abriria "Para um
	   de 5 <peixe>", com o rótulo vazio no meio da frase. O esquema permite (o
	   campo é anulável e a convivência é outro campo) e o banco nunca produziu.
	   Quem manda aqui é o mapa do arranjo: se ele declara um rótulo de mínimo, a
	   abertura é a do número; se não declara, é a do arranjo. */
	if ( $card && '' !== $arranjo['minimo'] ) {
		/* A FAIXA, quando a fonte declarou uma: o compêndio do gurami mel
		   recomenda "não menos que 4 a 6 exemplares", e abrir a página em 4 é
		   publicar metade da recomendação. O teto vem do banco (esquema versão
		   4) e nunca de aritmética sobre o piso. */
		$html .= 'Para um ' . esc_html( $arranjo['minimo'] ) . ' de '
			. esc_html( $card )
			. ( ! empty( $e['cardume_ate'] ) ? ' a ' . esc_html( (int) $e['cardume_ate'] ) : '' ) . ' '
			. esc_html( $nome ) . ', o seu aquário precisa de '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm de frente';
	} else {
		/* A ABERTURA PELO ARRANJO, e ela cobre os três valores em que a fonte não
		   entrega número para a frase: solitário e casal, em que o arranjo FIXA o
		   número e a escada tem um degrau; e o harém, em que a fonte descreve a
		   proporção entre os sexos — mais fêmeas do que machos — e nunca o tamanho
		   do grupo.

		   O HARÉM FOI PUBLICADO PELA PRIMEIRA VEZ NA LEVA 5, e até ali ele caía num
		   RAMO DE RESGATE que abria pela tradução do `como_vive()` — a que carrega a
		   oração do temperamento, "que vive em harém, um macho para várias fêmeas,
		   E A FONTE O DECLARA PACÍFICO". A primeira frase da página voltaria a citar
		   quem declarou, contra a 15.2 e contra o item 4 do despacho da Sentinela de
		   13/09/2026; como nenhuma das 14 fichas no ar caía ali, o defeito não tinha
		   como ser medido por página nenhuma — régua escrita para um mundo que nunca
		   aconteceu (seção 8 do ARQUIPELAGO.md).

		   E O RAMO DE RESGATE DEIXOU DE EXISTIR, em vez de ser consertado: o
		   vocabulário é fechado nos DOIS lados — o esquema enumera os cinco valores
		   de `convivencia` e o validador reprova qualquer outro, e
		   `aquametria_peixes_arranjo()` tem os mesmos cinco —, e quem não estiver no
		   mapa não passa mais no portão de página (ver
		   `aquametria_peixes_pode_virar_ficha()`). Aqui o arranjo é sempre conhecido
		   e sempre tem abertura declarada.

		   A PRIMEIRA ESCRITA DESTA FRASE, na leva 4, dizia "que é o que a fonte
		   declara por aquário", e o portão da voz reprovou antes de a página
		   existir: a distinção que importa é O NÚMERO, não quem o disse, e quem o
		   disse está um parágrafo abaixo, na camada de prova. */
		$html .= 'Para ' . esc_html( $arranjo['de'] ) . ' ' . esc_html( $nome )
			. ' — ' . esc_html( $arranjo['abertura'] ) . ' —, o seu aquário precisa de '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm de frente';
	}
	if ( $larg ) {
		$html .= ' por ' . esc_html( aquametria_peixes_num( $larg ) )
			. ' cm de fundo. O que manda é a BASE do aquário, não o litro.</p>';
	} elseif ( aquametria_peixes_fundo_de_outro_arranjo( $e ) ) {
		/* A TERCEIRA ABERTURA (1.12.0). Sem ela a página dizia "o fundo fica em
		   aberto" e, dois parágrafos abaixo, publicava a largura que a fonte
		   declarou — duas coisas diferentes a uma tela de distância, e a
		   primeira lida como "ninguém sabe". As duas ausências são diferentes
		   para quem lê e por isso têm frases diferentes desde a primeira linha.
		   A procedência continua fora do primeiro parágrafo (15.2): aqui não se
		   nomeia corpo nenhum, só se diz que a largura é de outra conta. */
		$html .= ', e o fundo fica de fora: a largura declarada é para outra '
			. 'quantidade de peixe. O que manda é o COMPRIMENTO do aquário, não o litro.</p>';
	} else {
		$html .= ', e o fundo fica em aberto. O que manda é o COMPRIMENTO do '
			. 'aquário, não o litro.</p>';
	}

	$alturas = aquametria_peixes_alturas();
	$litros_alturas = array();
	foreach ( $alturas as $a ) {
		$v = aquametria_peixes_volume_bruto( $frente[1], $larg, $a );
		if ( null !== $v ) {
			$litros_alturas[ $a ] = $v;
		}
	}
	if ( $litros_alturas ) {
		$primeira = min( array_keys( $litros_alturas ) );
		$ultima   = max( array_keys( $litros_alturas ) );
		/* O contraexemplo é CALCULADO, não escolhido: o cubo de mesmo volume é o
		   aquário com a menor frente possível para aquele litro, então ele é o
		   pior caso honesto — e a diferença em centímetros sai da subtração, não
		   de uma fração escrita à mão. */
		$cubo = pow( $litros_alturas[ $ultima ] * 1000, 1 / 3 );
		$html .= '<p>Essa base dá de ' . esc_html( aquametria_peixes_num( $litros_alturas[ $primeira ] ) )
			. ' litros a ' . esc_html( aquametria_peixes_num( $litros_alturas[ $ultima ] ) )
			. ' litros de lâmina, conforme a altura do aquário ser '
			. esc_html( aquametria_peixes_num( $primeira ) ) . ' ou '
			. esc_html( aquametria_peixes_num( $ultima ) ) . ' cm. '
			. 'E é por isso que responder só em litros engana: um aquário cúbico de '
			. esc_html( aquametria_peixes_num( $litros_alturas[ $ultima ] ) ) . ' litros tem '
			. esc_html( aquametria_peixes_num( $cubo ) ) . ' cm de lado — o litro certo e '
			. esc_html( aquametria_peixes_num( $frente[1] - $cubo ) )
			. ' cm de frente a menos do que ' . esc_html( $arranjo ? $arranjo['este'] : 'este cardume' )
			. ' pede.</p>';
	} else {
		/* Decisão 7, a outra metade: sem o fundo declarado, as duas tabelas que
		   dependem dele não saem — e a página DIZ que não saíram e por quê. A
		   versão anterior deste código simplesmente encolhia, e quem lesse não
		   tinha como distinguir "a ilha não sabe" de "a ilha esqueceu".

		   E DESDE A 1.12.0 SÃO DUAS AUSÊNCIAS, não uma. "Ninguém declarou
		   largura" e "a largura declarada não é sobre estes peixes" são
		   diferentes para quem lê, e a segunda tem número, tem fonte e tem para
		   quem — calá-la seria repetir, do outro lado, o erro de publicá-la sem
		   escopo. */
		$outro = aquametria_peixes_fundo_de_outro_arranjo( $e );
		if ( $outro ) {
			$html .= '<p class="aqm-px-fundo-de-outro-arranjo"><strong>O fundo deste aquário, esta página não promete a '
				. esc_html( $arranjo ? $arranjo['este'] : 'este cardume' ) . ' — e o motivo é a própria fonte.</strong> '
				. 'A largura de ' . esc_html( aquametria_peixes_num( $outro['largura'] ) ) . ' cm que a fonte publica para o '
				. esc_html( $nome ) . ' foi declarada para ' . esc_html( $outro['para'] ) . ', que é outra quantidade de peixe. '
				. 'Servir esse número aqui seria dizer, com cara de medida, que aquele chão atende '
				. esc_html( $arranjo ? $arranjo['este'] : 'este cardume' ) . ' — e a fonte não faz essa afirmação. '
				. 'Por isso não sai a tabela de litros por altura nem a de quantos cabem no aquário mínimo: as duas partem do fundo. '
				. 'O que fica de pé é a frente de ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm, essa sim declarada para '
				. esc_html( $arranjo ? $arranjo['este'] : 'este cardume' ) . ', e a outra metade da resposta logo abaixo: quantos litros '
				. esc_html( $arranjo ? $arranjo['este'] : 'o cardume' ) . ' pede pelas duas réguas brasileiras de lotação, que partem do comprimento dos peixes e não do chão do aquário.</p>';
		} else {
		$html .= '<p class="aqm-px-sem-fundo"><strong>O fundo do aquário, esta página não tem como dizer — e isso é o que a fonte declarou, não um buraco nosso.</strong> '
			. 'Para o ' . esc_html( $nome ) . ' a fonte publica o comprimento mínimo e para aí: não há largura declarada por ninguém. '
			. 'Sem os dois lados do chão não existe litro, então aqui não sai a tabela de litros por altura nem a de quantos cabem no aquário mínimo — elas sairiam de um fundo que a gente teria inventado. '
			. 'O que a página responde com o que está medido é a outra metade, e ela está logo abaixo: quantos litros o ' . esc_html( $arranjo ? $arranjo['coletivo'] : 'cardume' ) . ' pede pelas duas réguas brasileiras de lotação, que partem do comprimento dos peixes e não do chão do aquário.</p>';
		}
	}

	/* A camada de prova: fonte pelo nome e data, um parágrafo abaixo (15.2). */
	/* A FRASE PERGUNTA PELO CAMPO QUE ELA VAI NOMEAR (1.12.0, 22/09/2026).
	   Até aqui ela perguntava SEMPRE pelo comprimento e caía na base só quando
	   não havia comprimento declarado — e então dizia "quem declara essa BASE é
	   o <corpo que declarou só o comprimento>". Quatro fichas serviam isso no
	   ar: tetra neon, tetra-brilhante, rasbora arlequim e apistogramma agassizi
	   diziam "quem declara essa base é o FishBase", e nas quatro os dois lados
	   do chão são do Seriously Fish — a base científica declara a frente e não
	   fala de fundo. Atribuir número à fonte errada é o defeito mais caro desta
	   ilha, porque a procedência é o que ela vende. O `$substitutos` de
	   `aquametria_peixes_fonte_do_campo()` continua cobrindo o registro que
	   declara só um dos dois campos. */
	$fonte_frente = aquametria_peixes_fonte_do_campo( $e, $larg ? 'base_minima_cm' : 'comprimento_minimo_aquario_cm' );
	$html .= '<p class="aqm-prova">';
	if ( $fonte_frente ) {
		$html .= 'Quem declara ' . ( $larg ? 'essa base' : 'esse comprimento' ) . ' é o '
			. esc_html( $fonte_frente['corpo'] )
			. ', na ficha da espécie, colhido em ' . esc_html( aquametria_peixes_data_br( $fonte_frente['em'] ) ) . '. ';
	}
	if ( count( (array) $e['conflitos'] ) ) {
		$html .= 'Esta espécie tem divergência declarada entre fontes, e ela está publicada mais abaixo com o nome de quem disse cada número. ';
	}
	$html .= 'A página não foi lida direto: o egresso da nuvem barra os domínios das duas fontes, então cada número veio de busca restrita ao domínio — está na lista de reconferência da ilha.</p>';
	$html .= '</div>';

	/* --- 5.2 Quantos litros para N exemplares: a tabela pré-renderizada
	   (seção 5, item 1). É o que um modelo de linguagem lê sem preencher
	   formulário, e é a metade em que o erro é mais caro (seção 7). --- */
	/* O TÍTULO E A PERGUNTA DE ABERTURA SEGUEM O ARRANJO (1.7.0). "Quantos
	   litros para N betta" e "quem responde 'e para dez?'" são a pergunta
	   ERRADA para um peixe cuja fonte declara um por aquário: a página estaria
	   oferecendo, com cara de tabela, o número que a fonte recusa. Onde a fonte
	   fixa o arranjo, a escada tem um degrau e o texto diz por quê — e o que a
	   página ganha em troca é o achado desta categoria, que é a distância entre
	   a régua de lotação e a base declarada. */
	if ( $arranjo && null !== $arranjo['fixo'] ) {
		$html .= '<h2>Quantos litros para ' . esc_html( $arranjo['de'] ) . ' ' . esc_html( $nome ) . '</h2>';
		$contra = aquametria_peixes_lotacao_contra_base( $e, $frente, $porte, $larg, $arranjo['fixo'] );
		$html .= '<p>A base declarada é o piso do aquário, e aqui ela não vira escada: a fonte declara '
			. ( 1 === $arranjo['fixo'] ? 'um por aquário' : 'um casal' )
			. ', então não existe "e para dez?" a responder. O que a tabela abaixo mostra é o que as duas réguas de lotação que circulam no aquarismo brasileiro devolvem para esse número — elas discordam em quatro vezes entre si'
			. ( '' !== $contra['frase'] ? ', e ' . esc_html( $contra['frase'] ) : '' )
			. '. É por isso que régua de lotação não responde sozinha a esta pergunta.</p>';
	} else {
		$html .= '<h2>Quantos litros para N ' . esc_html( $nome ) . '</h2>';
		$html .= '<p>A base declarada é o piso do aquário; quem responde "e para dez?" são as duas réguas de lotação que circulam no aquarismo brasileiro. Elas discordam em quatro vezes, e a Aquametria publica as duas com o nome de quem disse cada uma em vez de tirar média.</p>';
	}
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
	$html .= '<caption>Litros para ' . esc_html( $arranjo ? $arranjo['de'] : 'um cardume de' ) . ' '
		. esc_html( $nome )
		. ', pelas duas réguas brasileiras. O porte adulto usado é '
		. esc_html( aquametria_peixes_faixa_texto( $porte ) )
		. ( abs( $porte[0] - $porte[1] ) > 0.01 ? ' — a coluna usa o extremo maior, porque errar carga para cima é o lado seguro' : '' )
		. '.</caption>';
	$html .= '<thead><tr><th scope="col">Exemplares</th><th scope="col">Soma dos comprimentos</th>'
		. '<th scope="col">Regra clássica (1 cm/L)</th><th scope="col">Critério intermediário (1,5 L/cm)</th>'
		. '<th scope="col">Critério conservador (4 L/cm)</th></tr></thead><tbody>';
	/* QUAL LINHA SE CHAMA MÍNIMA, e o rótulo sai do mapa do arranjo. Vazio em
	   solitário, casal e harém: nos dois primeiros o degrau único não é um piso
	   (é o teto que a fonte declara) e no terceiro a fonte declara o arranjo e
	   nunca o número — chamar qualquer linha de "mínimo" ali seria publicar um
	   número que ninguém declarou. */
	$rotulo_minimo = ( $arranjo && '' !== $arranjo['minimo'] && $card ) ? $arranjo['minimo'] : '';
	foreach ( aquametria_peixes_degraus_de_cardume( $e ) as $n ) {
		$soma = $n * $porte[1];
		$l    = aquametria_peixes_litros_por_criterio( $soma );
		$e_minima = ( '' !== $rotulo_minimo && $n === $card );
		$marca = $e_minima ? ' class="aqm-px-linha-minima"' : '';
		$html .= '<tr' . $marca . '><th scope="row">' . esc_html( $n )
			. ( $e_minima ? ' (' . esc_html( $rotulo_minimo ) . ')' : '' ) . '</th>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $soma ) ) . ' cm</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['classica'] ) ) . ' L</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['meio'] ) ) . ' L</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $l['conservadora'] ) ) . ' L</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="aqm-prova">A regra clássica de 1 cm de peixe por litro e o critério de 1,5 a 4 litros por cm de peixe saíram do levantamento de fontes brasileiras da ilha, em 04/09/2026, e as duas são publicadas com a ressalva das próprias fontes: elas contam comprimento e ignoram massa, formato e carga biológica. A "regra dos 10 %" ficou de fora porque nenhuma das fontes diz 10 % de quê.</p>';

	/* --- 5.3 O inverso: quantos cabem na base declarada. --- */
	if ( $litros_alturas ) {
		$html .= '<h2>E quantos ' . esc_html( $nome ) . ' cabem no aquário mínimo</h2>';
		$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
		$html .= '<caption>A base de ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' × '
			. esc_html( aquametria_peixes_num( $larg ) ) . ' cm em três alturas de aquário. '
			. 'O litro é o bruto da lâmina, antes de descontar vidro e substrato — a conta cheia está na calculadora de litragem.</caption>';
		$html .= '<thead><tr><th scope="col">Altura</th><th scope="col">Litros brutos</th>'
			. '<th scope="col">Pela regra clássica</th><th scope="col">Pelo intermediário</th>'
			. '<th scope="col">Pelo conservador</th></tr></thead><tbody>';
		foreach ( $litros_alturas as $a => $v ) {
			$q = aquametria_peixes_quantos_cabem( $v, $porte[1] );
			$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_num( $a ) ) . ' cm</th>';
			$html .= '<td>' . esc_html( aquametria_peixes_num( $v ) ) . ' L</td>';
			$html .= '<td>' . esc_html( $q['classica'] ) . '</td>';
			$html .= '<td>' . esc_html( $q['meio'] ) . '</td>';
			$html .= '<td>' . esc_html( $q['conservadora'] ) . '</td>';
			$html .= '</tr>';
		}
		$html .= '</tbody></table></div>';
		$meio_altura = $alturas[1];
		if ( isset( $litros_alturas[ $meio_altura ] ) && $arranjo && null !== $arranjo['fixo'] ) {
			/* NO ARRANJO FIXO ESTA TABELA RESPONDE À PERGUNTA ERRADA, e a página
			   tem de dizer isso na mesma tela. A frase antiga saía igual para
			   todo mundo — "cabem 1 pelo critério apertado e 6 pelo folgado" —,
			   e numa ficha que acabou de declarar um casal por aquário ela
			   oferece SEIS. A régua de lotação conta centímetro de peixe e não
			   sabe de comportamento; deixá-la falar sozinha aqui é publicar o
			   número que a fonte recusa, com a autoridade de uma tabela. */
			$q = aquametria_peixes_quantos_cabem( $litros_alturas[ $meio_altura ], $porte[1] );
			$html .= '<p>Traduzindo a linha do meio: pelas duas réguas de lotação caberiam de '
				. esc_html( $q['conservadora'] ) . ' a ' . esc_html( $q['classica'] ) . ' '
				. esc_html( $nome ) . ' no aquário mínimo com '
				. esc_html( aquametria_peixes_num( $meio_altura ) )
				. ' cm de altura — e é aqui que a régua responde à pergunta errada. '
				. 'Ela conta centímetros de peixe e não sabe de comportamento: a fonte declara '
				. ( 1 === $arranjo['fixo'] ? 'um por aquário' : 'um casal' )
				. ', e esse limite não sai de conta de litro nenhuma.</p>';
		} elseif ( isset( $litros_alturas[ $meio_altura ] ) ) {
			$q = aquametria_peixes_quantos_cabem( $litros_alturas[ $meio_altura ], $porte[1] );
			$html .= '<p>Traduzindo a linha do meio: no aquário mínimo com '
				. esc_html( aquametria_peixes_num( $meio_altura ) ) . ' cm de altura ';
			if ( (int) $q['conservadora'] < 1 ) {
				/* O CASO EM QUE O CRITÉRIO APERTADO NÃO PÕE NEM UM, e ele é a
				   borda deste bloco: com peixe grande o bastante, o conservador
				   arredonda para baixo até zero DENTRO do aquário que a própria
				   fonte declara como mínimo. Dizer "cabem 0" ali seria publicar
				   uma contradição sem nome; o que a página deve é a contradição
				   COM nome, porque ela é o assunto da ficha. Nenhum peixe do
				   banco com ficha chega a isso hoje — a mutação que produz o
				   mundo é quem mede este ramo (seção 8 do ARQUIPELAGO.md). */
				$html .= 'o critério apertado não põe nem um ' . esc_html( $nome )
					. ', e o folgado põe ' . esc_html( $q['classica'] )
					. '. Os dois números saem do mesmo litro, e é a base declarada — não a régua de lotação — que decide aqui.';
			} else {
				$html .= esc_html( aquametria_peixes_concorda( $q['conservadora'], 'cabe', 'cabem' ) ) . ' '
					. esc_html( $q['conservadora'] ) . ' ' . esc_html( $nome )
					. ' pelo critério apertado e ' . esc_html( $q['classica'] )
					. ' pelo critério folgado. ';
				/* A DIFERENÇA É ENTRE OS DOIS NÚMEROS DA TELA, e não entre as duas
				   constantes. Até 14/09/2026 esta frase imprimia 4 vezes, que é a
				   razão entre as réguas — e ela é a razão entre os NÚMEROS só
				   enquanto o arredondamento para baixo não morde. No peixe-espada
				   morde: a linha do meio dá 7 e 1, que é SETE vezes, e a frase
				   anunciava quatro a uma linha de distância dos dois números que
				   a desmentem. É o escopo de afirmação da seção 8, e ele só podia
				   aparecer numa ficha de peixe grande, que esta ilha não tinha. */
				$vezes = $q['classica'] / $q['conservadora'];
				$html .= 'A diferença entre os dois é de '
					. esc_html( aquametria_peixes_num( $vezes ) )
					. ' vezes, e é assim que as fontes brasileiras estão.';
			}
			$html .= ' Quem está montando o primeiro aquário faz melhor ficando perto do número apertado: o que sobra de espaço vira margem para o dia em que a filtragem falhar.</p>';
		}
	}

	/* --- 5.4 O que a fonte declara, campo por campo. --- */
	$html .= '<h2>O que as fontes declaram sobre o ' . esc_html( $nome ) . '</h2>';
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela aqm-px-declarado">';
	$html .= '<caption>Cada linha com o corpo que a sustenta e a data em que foi colhida.</caption>';
	$html .= '<thead><tr><th scope="col">O que</th><th scope="col">Declarado</th><th scope="col">Quem declara</th></tr></thead><tbody>';

	$linhas = array(
		array( 'Nome científico', esc_html( $e['cientifico'] ), 'nome_cientifico' ),
		array( 'Porte adulto', esc_html( aquametria_peixes_faixa_texto( $porte ) ) . ' (' . esc_html( $e['porte_medida'] ) . ')', 'porte_adulto_cm' ),
		array( 'Temperatura', esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' a ' . esc_html( aquametria_peixes_num( $e['temp_max'] ) ) . ' °C', 'temperatura_C' ),
		array( 'Frente mínima do aquário', esc_html( aquametria_peixes_faixa_texto( $frente ) ), 'comprimento_minimo_aquario_cm' ),
		array( 'Como vive', esc_html( aquametria_peixes_como_vive( $e ) ), 'convivencia' ),
	);
	if ( $card ) {
		/* O RÓTULO SAI DO ARRANJO, não digitado: "Cardume mínimo" numa espécie
		   cuja fonte escreve que ela NÃO é gregária no sentido dos peixes de
		   cardume é a fonte sendo contrariada na tabela que a cita. E o valor
		   serve a FAIXA quando a fonte declarou uma — o piso sozinho é menos do
		   que ela disse. */
		$rotulo_linha = ( $arranjo && '' !== $arranjo['minimo'] )
			? ucfirst( $arranjo['minimo'] )
			: 'Cardume mínimo';
		$valor_linha = ! empty( $e['cardume_ate'] )
			? esc_html( $card ) . ' a ' . esc_html( (int) $e['cardume_ate'] ) . ' exemplares'
			: esc_html( $card ) . ' exemplares';
		$linhas[] = array( $rotulo_linha, $valor_linha, 'cardume_minimo' );
	}
	if ( $e['origem'] ) {
		$linhas[] = array( 'De onde vem', esc_html( $e['origem'] ), 'origem_geografica' );
	}
	foreach ( $linhas as $linha ) {
		$f = aquametria_peixes_fonte_do_campo( $e, $linha[2] );
		$html .= '<tr><th scope="row">' . $linha[0] . '</th><td>' . $linha[1] . '</td><td>';
		if ( $f ) {
			$html .= esc_html( $f['corpo'] ) . ', ' . esc_html( aquametria_peixes_data_br( $f['em'] ) );
		} else {
			$html .= 'sem fonte que sustente — e por isso não entra em conta nenhuma';
		}
		$html .= '</td></tr>';
	}
	$html .= '</tbody></table></div>';

	$por_individuo = aquametria_peixes_frente_por_individuo( $e );
	if ( null !== $por_individuo ) {
		$html .= '<p>Dividindo o mínimo declarado pelo '
			. esc_html( $arranjo ? $arranjo['minimo'] : 'cardume mínimo' ) . ' dá '
			. esc_html( aquametria_peixes_num( $por_individuo ) )
			. ' cm de frente por exemplar — e esse número serve para comparar espécies, não para multiplicar. '
			. 'Os ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm que a fonte declara são o espaço de onde o '
			. esc_html( $arranjo ? $arranjo['coletivo'] : 'cardume' ) . ' consegue '
			. esc_html( $arranjo ? $arranjo['acao'] : 'nadar em cardume' ) . ', não o preço de '
			. esc_html( $card ) . ' peixes: multiplicar diria que dez ' . esc_html( $nome ) . ' precisam de '
			. esc_html( aquametria_peixes_num( $por_individuo * 10 ) ) . ' cm, o que nenhuma fonte sustenta.</p>';
	}

	/* --- 5.5 A divergência, publicada com os dois nomes. --- */
	if ( count( (array) $e['conflitos'] ) ) {
		$html .= '<h2>Onde as fontes discordam</h2>';
		$html .= '<p>A Aquametria nunca tira média de fontes que discordam: publica os dois extremos com o nome de quem disse cada um. '
			. 'E onde o número entra numa conta desta página, vale o extremo seguro — aquário maior, peixe maior —, porque errar espaço para cima não machuca ninguém.</p>';
		foreach ( (array) $e['conflitos'] as $c ) {
			list( $rotulo_campo, $unidade ) = aquametria_peixes_campo_na_tela( $c['campo'] );
			$html  .= '<p><strong>Sobre ' . esc_html( $rotulo_campo ) . ':</strong> ';
			$partes = array();
			foreach ( (array) $c['valores'] as $v ) {
				$valor = $v['valor'];
				if ( is_array( $valor ) ) {
					$valor = aquametria_peixes_num( isset( $valor['min'] ) ? $valor['min'] : null )
						. ' a ' . aquametria_peixes_num( isset( $valor['max'] ) ? $valor['max'] : null );
				} else {
					$valor = aquametria_peixes_num( $valor );
				}
				$partes[] = esc_html( trim( $valor . ' ' . $unidade ) ) . ' pelo ' . esc_html( $v['fonte'] );
			}
			$html .= implode( ', e ', $partes ) . '. ';

			/* Qual extremo esta página usou, e onde. A razão escrita no banco NÃO
			   vem para cá de propósito: ela é nota interna, escrita sem acento e
			   no vocabulário do esquema ("campo de manutenção"), e texto de tela
			   desta ilha sai acentuado e na língua de quem compra. O que o leitor
			   precisa saber é qual número a conta usou — e isso a página sabe
			   dizer sozinha, porque é ela que escolhe. */
			if ( 'comprimento_minimo_aquario_cm' === $c['campo'] || 'base_minima_cm' === $c['campo'] ) {
				$html .= '<span class="aqm-px-razao">As contas desta página usam '
					. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm, o maior dos dois.</span>';
			} elseif ( 'porte_adulto_cm' === $c['campo'] ) {
				$html .= '<span class="aqm-px-razao">As tabelas de lotação desta página usam '
					. esc_html( aquametria_peixes_num( $porte[1] ) ) . ' cm, o maior dos dois.</span>';
			} else {
				$html .= '<span class="aqm-px-razao">Este número não entra em nenhuma conta desta página; está aqui porque o banco registrou a divergência e esconder divergência é escolher um lado em silêncio.</span>';
			}
			$html .= '</p>';
		}
	}

	/* --- 5.6 Quem divide a mesma água. Critério na frente da lista (14.4). --- */
	$vizinhos = aquametria_peixes_mesma_agua( $id );

	/* ESPÉCIE QUE O BANCO DECLARA AGRESSIVA NÃO GANHA LISTA DE COMPANHEIRO, e
	   isto não é excesso de zelo: o filtro da função acima tira o companheiro
	   agressivo da lista, e não olhava o peixe da PRÓPRIA ficha. Na primeira
	   versão desta página o mato-grosso — que a FishBase declara agressivo —
	   servia tetra ember e tetra neon na tabela de quem divide a água, com uma
	   nota dizendo que não era veredito de convivência. Nota não desfaz tabela:
	   quem lê vê a lista, não a ressalva.
	   E a saída honesta não é uma lista menor, é NÃO publicar lista: o esquema
	   do banco recusa compatibilidade como campo justamente porque ela depende
	   de volume, layout e ordem de introdução, e para peixe agressivo é aí que
	   a resposta mora. Então a página conta o que mediu (quantas espécies do
	   banco dividem a faixa) e diz por que não recomenda nenhuma. */
	if ( 'agressivo' === $e['comportamento'] ) {
		$total_faixa = count( $vizinhos['dentro'] ) + count( $vizinhos['maior'] ) + count( $vizinhos['agressivos'] );
		$html .= '<h2>Com quem ' . esc_html( $arranjo ? $arranjo['este'] : 'esse cardume' ) . ' divide o aquário</h2>';
		$html .= '<p>Esta ficha <strong>não publica lista de companheiro</strong>, e a razão está duas tabelas acima: a fonte declara o '
			. esc_html( $nome ) . ' <strong>agressivo</strong>. '
			. esc_html( $total_faixa ) . ' das ' . esc_html( count( aquametria_peixes_catalogo() ) )
			. ' espécies do banco dividem faixa de temperatura com ele, e nenhuma delas vira recomendação por causa disso: '
			. 'temperatura é o que a gente mediu, e convivência com peixe agressivo depende do volume, do layout e da ordem em que os peixes entram no aquário — nada disso cabe numa tabela, e o banco desta ilha não guarda compatibilidade como campo justamente por isso.</p>';
		/* O CONSELHO SE INVERTE COM O ARRANJO, e este é o ramo que a leva 4
		   descobriu sem nenhum portão reprovar. A frase antiga — "quanto maior o
		   cardume, menos a agressão se concentra num alvo só ... por isso a fonte
		   declara cardume mínimo de N e não de dois" — era verdadeira para a
		   única espécie agressiva publicada até aqui (o mato-grosso, cardume 5) e
		   é o CONTRÁRIO do que a fonte diz do betta, que é agressivo E solitário:
		   ali a fonte manda um por aquário. Pior: `$card` é nulo nessa espécie, e
		   a frase iria ao ar com um buraco no meio ("cardume mínimo de  e não de
		   dois"). Diluir agressão em número é conselho de peixe de cardume, e
		   aplicá-lo a um peixe solitário seria mandar o leitor comprar o segundo
		   exemplar que a fonte proíbe. */
		if ( $arranjo && null !== $arranjo['fixo'] ) {
			$html .= '<p class="aqm-px-fora">O que dá para dizer com o que está medido: a fonte declara '
				. ( 1 === $arranjo['fixo'] ? 'um por aquário' : 'um casal' )
				. ' para o ' . esc_html( $nome ) . ', e esse número não é uma sugestão de companhia — é o limite. '
				. 'Espaço além dos ' . esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm mínimos ajuda, '
				. 'mas aqui ele não compra um segundo exemplar: num peixe que a fonte declara agressivo e manda '
				. esc_html( $arranjo['acao'] ) . ', mais espaço é folga para o mesmo habitante, não vaga para outro.</p>';
		} else {
			$html .= '<p class="aqm-px-fora">O que dá para dizer com o que está medido: quanto mais espaço além dos '
				. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm mínimos, e quanto maior o '
				. esc_html( $arranjo ? $arranjo['coletivo'] : 'cardume' ) . ', menos a agressão se concentra num alvo só — '
				. 'é a mesma razão por que a fonte declara ' . esc_html( $arranjo ? $arranjo['minimo'] : 'cardume mínimo' )
				. ' de ' . esc_html( $card ) . ' e não de dois.</p>';
		}
	} elseif ( $vizinhos['dentro'] ) {
		$html .= '<h2>Quem divide a mesma faixa de temperatura</h2>';
		$html .= '<p>Isto não é veredito de convivência, e a diferença importa: o que está medido aqui é a <strong>interseção das faixas de temperatura declaradas</strong>, com dois filtros a mais — o aquário mínimo do companheiro cabe nos '
			. esc_html( aquametria_peixes_num( $frente[1] ) ) . ' cm desta ficha, e o banco não o declara agressivo. '
			. 'Quem decide convivência de verdade é o volume, o layout e a ordem em que os peixes entram, e isso nenhuma tabela resolve.</p>';
		$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela"><caption>Espécies do banco cuja faixa declarada encosta na do '
			. esc_html( $nome ) . ' em 2 °C ou mais.</caption>';
		$html .= '<thead><tr><th scope="col">Espécie</th><th scope="col">Temperatura declarada</th>'
			. '<th scope="col">Onde as duas faixas se encontram</th>'
			. '<th scope="col">Porte adulto</th><th scope="col">Frente mínima</th></tr></thead><tbody>';
		$catalogo = aquametria_peixes_catalogo();
		foreach ( $vizinhos['dentro'] as $outro_id ) {
			$o  = $catalogo[ $outro_id ];
			$op = aquametria_peixes_porte_faixa( $o );
			$of = aquametria_peixes_frente_faixa( $o );
			$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_nome( $o ) )
				. ' <span class="aqm-px-cientifico">' . esc_html( $o['cientifico'] ) . '</span></th>';
			$html .= '<td>' . esc_html( aquametria_peixes_num( $o['temp_min'] ) ) . ' a '
				. esc_html( aquametria_peixes_num( $o['temp_max'] ) ) . ' °C</td>';
			/* A largura da interseção sai na tela de propósito: sem ela, a
			   espécie que só encosta em 2 °C fica com a mesma cara de quem
			   compartilha a faixa inteira, e o leitor não tem como ver a
			   diferença. Coluna que mostra o quanto a afirmação é folgada é o
			   contrário de colher cereja. */
			$html .= '<td>' . esc_html( aquametria_peixes_num( max( (float) $e['temp_min'], (float) $o['temp_min'] ) ) )
				. ' a ' . esc_html( aquametria_peixes_num( min( (float) $e['temp_max'], (float) $o['temp_max'] ) ) )
				. ' °C</td>';
			$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( $op ) ) . '</td>';
			$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( $of ) ) . '</td></tr>';
		}
		$html .= '</tbody></table></div>';

		/* Prestação de contas: quem ficou de fora, e por qual das duas causas
		   (seção 7 — causa que o código separa, o texto separa). */
		$html .= '<p class="aqm-px-fora">';
		$total_faixa = count( $vizinhos['dentro'] ) + count( $vizinhos['maior'] ) + count( $vizinhos['agressivos'] );
		$html .= 'Entre ' . esc_html( aquametria_peixes_concorda( $total_faixa, 'a', 'as' ) ) . ' '
			. esc_html( $total_faixa ) . ' '
			. esc_html( aquametria_peixes_concorda( $total_faixa, 'espécie', 'espécies' ) )
			. ' do banco com faixa de temperatura que encosta na do '
			. esc_html( $nome ) . ', ' . esc_html( count( $vizinhos['dentro'] ) ) . ' '
			. esc_html( aquametria_peixes_concorda( count( $vizinhos['dentro'] ), 'está', 'estão' ) )
			. ' na tabela acima. ';
		if ( $vizinhos['maior'] ) {
			$nomes = array();
			foreach ( $vizinhos['maior'] as $outro_id ) {
				$of = aquametria_peixes_frente_faixa( $catalogo[ $outro_id ] );
				$nomes[] = aquametria_peixes_nome( $catalogo[ $outro_id ] ) . ' (' . aquametria_peixes_num( $of[1] ) . ' cm)';
			}
			$html .= esc_html( count( $vizinhos['maior'] ) ) . ' '
				. esc_html( aquametria_peixes_concorda( count( $vizinhos['maior'] ), 'ficou', 'ficaram' ) )
				. ' fora por pedir aquário mais largo que esta ficha: '
				. esc_html( implode( ', ', $nomes ) ) . '. ';
		}
		if ( $vizinhos['agressivos'] ) {
			$nomes = array();
			foreach ( $vizinhos['agressivos'] as $outro_id ) {
				$nomes[] = aquametria_peixes_nome( $catalogo[ $outro_id ] );
			}
			$html .= esc_html( count( $vizinhos['agressivos'] ) ) . ' '
				. esc_html( aquametria_peixes_concorda( count( $vizinhos['agressivos'] ), 'ficou', 'ficaram' ) )
				. ' fora porque o banco '
				. esc_html( aquametria_peixes_concorda( count( $vizinhos['agressivos'] ), 'o', 'os' ) )
				. ' declara '
				. esc_html( aquametria_peixes_concorda( count( $vizinhos['agressivos'] ), 'agressivo', 'agressivos' ) )
				. ': ' . esc_html( implode( ', ', $nomes ) ) . '. ';
		}
		$html .= '</p>';
	}

	/* --- 5.7 O equipamento que este aquário pede — o 16.4(d), e o caminho do
	   dinheiro. A vitrine não mora aqui: mora na calculadora. --- */
	$html .= '<h2>O equipamento que esse aquário pede</h2>';
	$html .= '<p>';
	$url_c1 = aquametria_casca_url_se_existir( 'calculadora-de-litragem' );
	$url_c5 = aquametria_casca_url_se_existir( 'calculadora-de-potencia-do-aquecedor' );
	$url_c3 = aquametria_casca_url_se_existir( 'calculadora-de-vazao-do-filtro' );
	if ( '' !== $url_c1 ) {
		$html .= 'O litro bruto da tabela acima não é a água que você vai tratar: vidro e substrato comem uma parte, e a '
			. '<a href="' . esc_url( $url_c1 ) . '">conta dos litros</a> devolve os três números com as suas medidas. ';
	}
	if ( '' !== $url_c5 ) {
		$html .= 'O ' . esc_html( $nome ) . ' pede água entre '
			. esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' e '
			. esc_html( aquametria_peixes_num( $e['temp_max'] ) )
			. ' °C, e quanto de aquecedor isso custa depende do frio que faz no seu cômodo — é a '
			. '<a href="' . esc_url( $url_c5 ) . '">conta dos watts</a>. ';
	}
	if ( '' !== $url_c3 ) {
		$html .= 'Peixe come e peixe suja, então a vazão do filtro sai da '
			. '<a href="' . esc_url( $url_c3 ) . '">conta do filtro</a>, com a faixa que os fabricantes declaram.';
	}
	$html .= '</p>';
	$html .= '<p class="aqm-px-sem-loja"><strong>Nesta página não tem link de loja, e isso é decisão, não esquecimento.</strong> '
		. 'Peixe vivo não se compra por link de afiliado — quem vende é a loja da sua cidade, e a Aquametria não tem como conferir o lote nem a aclimatação de ninguém. '
		. 'O equipamento tem link, e ele está dentro das calculadoras acima, onde o produto entra como consequência do número que você calculou.</p>';

	/* --- 5.8 A mãe no corpo, e as irmãs. 16.4(b) e 16.4(c). --- */
	$html .= aquametria_peixes_frase_de_mae_html( $slug );

	/* --- 5.9 A consulta-alvo e a classificação da SERP, no corpo, porque quem
	   confere a 14.9 é quem lê a página. --- */
	$html .= '<p class="aqm-px-consulta">Esta página mira a consulta <strong>“'
		. esc_html( $registro[ $slug ]['consulta'] ) . '”</strong>. A SERP dessa consulta foi classificada em '
		. esc_html( aquametria_peixes_serp_em( $slug ) ) . ' antes de a página nascer, como manda o critério da ilha, e a classificação está escrita no snippet que serve esta página.</p>';

	/* O QUE A MEDIÇÃO DA SERP ACHOU E SÓ ESTA PÁGINA TEM PARA DIZER. Campo
	   opcional do registro, servido aqui e em nenhum outro lugar: é leitura do
	   mundo lá fora, com a data da medição, e não afirmação sobre o banco. Sem
	   ele a única saída seria escrever a frase dentro do gerador com um `if` por
	   slug, que é o número de tela digitado com outro nome. */
	if ( ! empty( $registro[ $slug ]['serp_nota'] ) ) {
		$html .= '<p class="aqm-px-serp-nota">' . esc_html( $registro[ $slug ]['serp_nota'] ) . '</p>';
	}

	$html .= '</div>';

	return $html;
}
}

/**
 * A frase do corpo que linka a mãe — o 16.4(b), a metade que não é breadcrumb.
 *
 * As IRMÃS não saem daqui: quem publica o bloco "Veja também" é a casca, para
 * toda página da ilha, e duas marcações para o mesmo cluster viram dois CSS e,
 * mais cedo do que se pensa, duas aparências. O que este snippet faz é dizer à
 * casca quem são as irmãs, pelo filtro `aquametria_peixes`.
 *
 * A frase só sai com mãe PUBLICADA. Frase apontando para página inexistente é
 * link morto, e o portão cobra a ausência dela justamente para ninguém fechar
 * isso com um endereço inventado.
 */
if ( ! function_exists( 'aquametria_peixes_frase_de_mae_html' ) ) {
function aquametria_peixes_frase_de_mae_html( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return '';
	}
	$pai = $registro[ $slug ]['pai'];
	if ( '' === $pai || ! isset( $registro[ $pai ] ) ) {
		return '';
	}
	$url_pai = aquametria_casca_url_se_existir( $pai );
	if ( '' === $url_pai ) {
		return '';
	}

	$irmas = aquametria_peixes_irmas( $slug );
	if ( 3 === $registro[ $slug ]['nivel'] ) {
		return '<p class="aqm-px-mae">Esta é uma das ' . esc_html( count( $irmas ) + 1 )
			. ' fichas de <a href="' . esc_url( $url_pai ) . '">'
			. esc_html( $registro[ $pai ]['titulo'] ) . '</a>, onde a mesma conta aparece para todas elas na mesma tabela.</p>';
	}

	return '<p class="aqm-px-mae">Esta lista é uma das categorias de <a href="'
		. esc_url( $url_pai ) . '">' . esc_html( $registro[ $pai ]['titulo'] )
		. '</a>, que é onde o critério inteiro da ilha para este assunto está escrito.</p>';
}
}

/** As irmãs de uma página do eixo: mesma mãe, no registro, nunca digitadas. */
if ( ! function_exists( 'aquametria_peixes_irmas' ) ) {
function aquametria_peixes_irmas( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return array();
	}
	$pai   = $registro[ $slug ]['pai'];
	$irmas = array();
	foreach ( $registro as $outro => $def ) {
		if ( $outro === $slug || $def['pai'] !== $pai || '' === $pai ) {
			continue;
		}
		$irmas[] = $outro;
	}
	return $irmas;
}
}

/* ---------------------------------------------------------------------------
 * 6. A categoria (nível 2) — listagem com critério próprio, nunca grade de links
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_categoria_html' ) ) {
function aquametria_peixes_categoria_html( $slug ) {
	$categorias = aquametria_peixes_categorias();
	if ( ! isset( $categorias[ $slug ] ) ) {
		return '';
	}
	$cat      = $categorias[ $slug ];
	$catalogo = aquametria_peixes_catalogo();
	$registro = aquametria_peixes_registro();

	$dentro = array();
	foreach ( $cat['especies'] as $id ) {
		if ( isset( $catalogo[ $id ] ) ) {
			$dentro[ $id ] = $catalogo[ $id ];
		}
	}

	/* A OUTRA METADE DA MESMA LISTA: quem esta categoria declara e o portão
	   barra. Até 13/09/2026 o `foreach` acima era a lista inteira, e o `if`
	   descartava em silêncio — a categoria podia declarar uma espécie e a
	   página não dizia uma palavra sobre ela. Hoje as duas categorias no ar
	   têm este conjunto vazio, e é por isso que a prova deste ramo é uma
	   mutação que PRODUZ O MUNDO (seção 8: caso que o esquema permite e o
	   banco ainda não tem é caso que a régua trata hoje). */
	$barrados = aquametria_peixes_barrados();
	$barradas_daqui = array();
	foreach ( $cat['especies'] as $id ) {
		if ( ! isset( $catalogo[ $id ] ) && isset( $barrados[ $id ] ) ) {
			$barradas_daqui[ $id ] = $barrados[ $id ];
		}
	}

	$com_ficha = array();
	foreach ( $registro as $s => $def ) {
		if ( isset( $def['especie'] ) && isset( $dentro[ $def['especie'] ] ) ) {
			$com_ficha[ $def['especie'] ] = $s;
		}
	}

	/* O SUBSTANTIVO DA CATEGORIA VEM DECLARADO, e isto é conserto de um defeito
	   que o portão pegou nesta leva antes de ir ao ar: a abertura dizia "São N
	   tetras" com o "tetras" digitado, e a página das coridoras serviu "São 4
	   tetras" na primeira renderização. A contagem estava certa e o substantivo
	   mentia — a forma mais silenciosa do número de tela que envelhece, porque
	   aqui nem número era. Enquanto houve uma categoria só, digitado e derivado
	   eram indistinguíveis; a segunda separou os dois. */
	$html  = '<div class="aqm-px aqm-px-categoria">';
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">' . esc_html( $cat['linha_mestra'] ) . '</p>';
	$html .= '<p>São ' . esc_html( count( $dentro ) ) . ' '
		. esc_html( $cat['plural'] )
		. ' com aquário mínimo declarado por fonte com nome e data, e o mínimo vai de '
		. esc_html( aquametria_peixes_num( aquametria_peixes_menor_frente( $dentro ) ) ) . ' a '
		. esc_html( aquametria_peixes_num( aquametria_peixes_maior_frente( $dentro ) ) )
		. ' cm de frente';

	/* A SEGUNDA METADE DA ABERTURA MUDA DE ASSUNTO QUANDO A CATEGORIA MISTURA
	   ARRANJOS (1.7.0). Até a leva 3 as duas categorias no ar eram inteiramente
	   de peixe de cardume, e a frase dizia "com o cardume mínimo indo de X a Y
	   exemplares" — derivada, mas derivada de um mundo de um tipo só. Numa
	   categoria em que só uma das espécies declara número, `menor_cardume()` e
	   `maior_cardume()` devolvem o MESMO valor e a frase sai dizendo "de 4 a 4",
	   com cara de faixa medida, escondendo que as outras duas não têm cardume
	   nenhum a declarar. O que essa categoria tem para dizer é outra coisa — e é
	   justamente o que o critério dela declara: o arranjo social. */
	$arranjos = array();
	foreach ( $dentro as $x ) {
		$a = aquametria_peixes_arranjo( $x );
		if ( $a ) {
			$arranjos[ $a['chave'] ] = $a;
		}
	}
	if ( 1 === count( $arranjos ) && null === aquametria_peixes_menor_cardume( $dentro ) ) {
		$html .= '. A tabela abaixo põe porte e espaço lado a lado, que é a comparação que nenhuma das respostas de busca desta consulta publica.</p>';
	} elseif ( 1 === count( $arranjos ) ) {
		$unico = reset( $arranjos );
		$html .= ' — com o ' . esc_html( $unico['minimo'] ? $unico['minimo'] : $unico['coletivo'] ) . ' indo de '
			. esc_html( aquametria_peixes_menor_cardume( $dentro ) ) . ' a '
			. esc_html( aquametria_peixes_maior_cardume( $dentro ) )
			. ' exemplares. A tabela abaixo põe os dois números lado a lado, que é a comparação que nenhuma das respostas de busca desta consulta publica.</p>';
	} else {
		$formas = array();
		foreach ( $arranjos as $a ) {
			$formas[] = 'peixe que ' . $a['vive'];
		}
		$ultima = array_pop( $formas );
		$html .= '. E a fonte não declara o mesmo arranjo para todos: aqui tem '
			. esc_html( $formas ? implode( ', ', $formas ) . ' e ' . $ultima : $ultima )
			. '. É essa diferença que decide a resposta, e é ela que nenhuma das respostas de busca desta consulta distingue — '
			. 'a tabela abaixo põe o arranjo ao lado do espaço, um a um.</p>';
	}
	$html .= '</div>';

	$html .= '<h2>' . esc_html( ucfirst( $cat['plural'] ) ) . ' do banco, com o mínimo declarado de cada um</h2>';
	$html .= '<p class="aqm-px-criterio"><strong>O critério desta lista:</strong> ' . esc_html( $cat['criterio'] ) . '</p>';
	/* A COLUNA MUDA DE NOME QUANDO A CATEGORIA MUDA DE MUNDO (1.7.0): onde todas
	   declaram o mesmo tipo de número, ela é o rótulo daquele arranjo; onde os
	   arranjos são diferentes, ela deixa de ser um número e passa a ser a forma
	   de viver, com o número dentro de quem tem um. */
	$coluna_arranjo = ( 1 === count( $arranjos ) && null !== aquametria_peixes_menor_cardume( $dentro ) )
		? ucfirst( reset( $arranjos )['minimo'] )
		: 'Como vive';
	$html .= '<div class="aqm-px-rolagem"><table class="aqm-px-tabela">';
	$html .= '<caption>Porte adulto, ' . esc_html( mb_strtolower( $coluna_arranjo, 'UTF-8' ) )
		. ' e frente mínima declarada. Onde as fontes discordam, a coluna traz os dois extremos.</caption>';
	$html .= '<thead><tr><th scope="col">Espécie</th><th scope="col">Porte adulto</th>'
		. '<th scope="col">' . esc_html( $coluna_arranjo ) . '</th><th scope="col">Frente mínima</th>'
		. '<th scope="col">Temperatura</th><th scope="col">A conta inteira</th></tr></thead><tbody>';

	/* Ordem: frente mínima crescente, e entre iguais o peixe menor antes. Quem
	   procura "tetra para aquário pequeno" lê de cima para baixo. */
	uasort( $dentro, function ( $a, $b ) {
		$fa = aquametria_peixes_frente_faixa( $a );
		$fb = aquametria_peixes_frente_faixa( $b );
		if ( $fa[1] !== $fb[1] ) {
			return ( $fa[1] > $fb[1] ) ? 1 : -1;
		}
		if ( (float) $a['porte_cm'] === (float) $b['porte_cm'] ) {
			return strcmp( $a['id'], $b['id'] );
		}
		return ( (float) $a['porte_cm'] > (float) $b['porte_cm'] ) ? 1 : -1;
	} );

	foreach ( $dentro as $id => $e ) {
		$html .= '<tr><th scope="row">' . esc_html( aquametria_peixes_nome( $e ) )
			. ' <span class="aqm-px-cientifico">' . esc_html( $e['cientifico'] ) . '</span></th>';
		$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( aquametria_peixes_porte_faixa( $e ) ) ) . '</td>';
		$html .= '<td>' . esc_html( 'Como vive' === $coluna_arranjo
			? aquametria_peixes_arranjo_curto( $e )
			: ( $e['cardume'] ? $e['cardume'] : 'não declarado' ) ) . '</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_faixa_texto( aquametria_peixes_frente_faixa( $e ) ) ) . '</td>';
		$html .= '<td>' . esc_html( aquametria_peixes_num( $e['temp_min'] ) ) . ' a '
			. esc_html( aquametria_peixes_num( $e['temp_max'] ) ) . ' °C</td>';
		$html .= '<td>';
		if ( isset( $com_ficha[ $id ] ) ) {
			$url = aquametria_casca_url_se_existir( $com_ficha[ $id ] );
			if ( '' !== $url ) {
				/* Âncora = o TÍTULO da filha, que nesta ilha é a pergunta que a
				   pessoa digita — é o que o 16.4(a) pede e é o mesmo nome que a
				   filha usa na trilha, no H1 e no <title>. */
				$html .= '<a href="' . esc_url( $url ) . '">'
					. esc_html( $registro[ $com_ficha[ $id ] ]['titulo'] ) . '</a>';
			} else {
				$html .= 'em breve';
			}
		} else {
			$html .= 'em breve';
		}
		$html .= '</td></tr>';
	}
	$html .= '</tbody></table></div>';

	/* Prestação de contas da listagem: quantas têm página, quantas esperam. A
	   frase muda de forma quando a fila zera, porque "0 estão na fila, e a
	   próxima leva sai depois" é uma promessa sobre uma leva que não existe. */
	$na_fila = count( $dentro ) - count( $com_ficha );
	$html .= '<p class="aqm-px-fora">';
	if ( $na_fila > 0 ) {
		$html .= 'Das ' . esc_html( count( $dentro ) ) . ' espécies da tabela, '
			. esc_html( count( $com_ficha ) ) . ' já têm a conta inteira numa página própria e '
			. esc_html( $na_fila )
			. ' estão na fila. A ordem não é alfabética nem por gosto: sai primeiro a que mais gente procura, e a próxima leva sai depois de medirmos se estas foram indexadas.';
	} elseif ( $barradas_daqui ) {
		/* FECHADA SÓ VALE QUANDO NÃO HÁ NINGUÉM ESPERANDO DO LADO DE FORA. A
		   frase de baixo diz "fechada quer dizer que todo X que o banco
		   sustenta já tem página" — com um barrado declarado nesta categoria
		   ela passa a ser falsa sem mudar uma letra, que é a forma silenciosa
		   do número de tela que envelhece. Aqui o texto muda de forma. */
		$html .= 'As ' . esc_html( count( $dentro ) )
			. ' espécies da tabela têm a conta inteira numa página própria, e a lista NÃO está fechada: o banco tem mais '
			. esc_html( count( $barradas_daqui ) )
			. ' desta mesma categoria que o portão ainda barra, e o que falta em cada uma está logo abaixo. '
			. 'A lista cresce quando o banco crescer, não quando der vontade de escrever.';
	} else {
		/* O SUBSTANTIVO DESTA FRASE ESTAVA DIGITADO, E ESTAVA NO AR ERRADO. É a
		   mesma cicatriz do "São 4 tetras" que a leva 3 pegou antes de publicar,
		   numa forma que escapou porque mora num RAMO: este `else` só é
		   alcançado quando a categoria fecha (zero na fila e zero barrados), e
		   até 12/09 só os tetras tinham fechado. No dia em que `/peixes/
		   corydoras/` fechou, a página passou a servir "fechada quer dizer que
		   todo TETRA que o banco desta ilha sustenta já tem a página dele" — na
		   página das coridoras, medido no HTML servido em 14/09/2026. Ramo novo
		   herda o texto do mundo antigo, e nenhuma contagem estava errada: só a
		   palavra. Agora ela vem declarada por categoria, como o `plural`. */
		$html .= 'As ' . esc_html( count( $dentro ) )
			. ' espécies da tabela têm a conta inteira numa página própria — esta lista está fechada, e fechada quer dizer que '
			. esc_html( $cat['singular'] ) . ' que o banco desta ilha sustenta com duas fontes já tem a página dele. '
			. 'A lista cresce quando o banco crescer, não quando der vontade de escrever: espécie sem duas fontes de corpos distintos não entra na tabela, e espécie que vive em cardume sem o número do cardume declarado não ganha página, porque a página começa justamente por esse número.';
	}
	$html .= '</p>';

	/* Quem esta categoria declara e a tabela não mostra, com nome e causa. */
	if ( $barradas_daqui ) {
		$html .= '<p class="aqm-px-fora">Fora da tabela, e declarados nesta categoria: '
			. esc_html( count( $barradas_daqui ) ) . ' de '
			. esc_html( count( $cat['especies'] ) )
			. '. Não é escolha editorial — é o portão de dado, e o que falta em cada um está nomeado aqui em vez de sumir da página.</p>';
		$html .= aquametria_peixes_barrados_lista_html( $barradas_daqui );
	}

	/* O EXEMPLO DA PERGUNTA SAI DA CONSULTA DESTA PÁGINA, e não de uma frase
	   digitada (1.7.0). "Quem pergunta 'quantos litros para dez neons'" é a
	   consulta da categoria dos tetras escrita na página das coridoras e, a
	   partir da leva 4, na dos bettas — a mesma família do substantivo herdado
	   logo acima, só que aqui nunca chegou a ser falso, só estranho. */
	$html .= '<h2>Por que a gente responde em centímetros antes de responder em litros</h2>';
	$html .= '<p>Quem pergunta "' . esc_html( $registro[ $slug ]['consulta'] ) . '" quer um número, e a resposta honesta tem duas partes. '
		. 'A primeira é a base: as fontes de aquarismo declaram o tamanho do <strong>chão</strong> do aquário, porque é ele que decide se o peixe nada à vontade ou fica encolhido num canto. '
		. 'A segunda é a lotação, e aí entram as duas réguas brasileiras que discordam em quatro vezes. '
		. 'Um aquário alto e estreito pode ter o litro certo e o chão errado — e é por isso que a tabela acima tem a coluna em centímetros.</p>';

	$html .= aquametria_peixes_frase_de_mae_html( $slug );
	$html .= '<p class="aqm-px-consulta">Esta página mira a consulta <strong>“'
		. esc_html( $registro[ $slug ]['consulta'] ) . '”</strong>, e a SERP dela foi classificada em '
		. esc_html( aquametria_peixes_serp_em( $slug ) ) . ' antes de a página nascer.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_peixes_menor_frente' ) ) {
function aquametria_peixes_menor_frente( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		$f = aquametria_peixes_frente_faixa( $e );
		$v = ( null === $v ) ? $f[1] : min( $v, $f[1] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_maior_frente' ) ) {
function aquametria_peixes_maior_frente( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		$f = aquametria_peixes_frente_faixa( $e );
		$v = ( null === $v ) ? $f[1] : max( $v, $f[1] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_menor_cardume' ) ) {
function aquametria_peixes_menor_cardume( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		if ( empty( $e['cardume'] ) ) {
			continue;
		}
		$v = ( null === $v ) ? (int) $e['cardume'] : min( $v, (int) $e['cardume'] );
	}
	return $v;
}
}

if ( ! function_exists( 'aquametria_peixes_maior_cardume' ) ) {
function aquametria_peixes_maior_cardume( $lista ) {
	$v = null;
	foreach ( $lista as $e ) {
		if ( empty( $e['cardume'] ) ) {
			continue;
		}
		$v = ( null === $v ) ? (int) $e['cardume'] : max( $v, (int) $e['cardume'] );
	}
	return $v;
}
}

/* ---------------------------------------------------------------------------
 * 7. A seção (nível 1)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_secao_html' ) ) {
function aquametria_peixes_secao_html() {
	$catalogo   = aquametria_peixes_catalogo();
	$categorias = aquametria_peixes_categorias();
	$registro   = aquametria_peixes_registro();

	$com_ficha = 0;
	foreach ( $registro as $def ) {
		if ( isset( $def['especie'] ) && isset( $catalogo[ $def['especie'] ] ) ) {
			$com_ficha++;
		}
	}

	$html  = '<div class="aqm-px aqm-px-secao">';
	$html .= '<div class="aqm-px-direta">';
	$html .= '<p class="aqm-px-linha-mestra">O número que decide se o peixe cabe no seu aquário é o tamanho do chão, em centímetros — não o litro. E é isso que quase nenhuma resposta de busca diz.</p>';
	$html .= '<p>São ' . esc_html( count( $catalogo ) ) . ' espécies de água doce com o mínimo declarado por fonte com nome e data. '
		. 'Para cada uma, a ilha publica o que a fonte declarou (a base do aquário e o cardume mínimo) e o que as duas réguas brasileiras de lotação calculam para o número de peixes que você quer — que discordam em quatro vezes entre si. '
		. 'As duas coisas na mesma tela, com o nome de quem disse cada número.</p>';
	$html .= '</div>';

	$html .= '<h2>Por onde começar</h2>';
	$html .= '<ul class="aqm-px-cats">';
	foreach ( $categorias as $slug => $cat ) {
		/* QUEM DECIDE O LINK É QUANTAS ESPÉCIES ENTRAM NA TABELA, e não quantas
		   a categoria declara. Eram a mesma coisa enquanto o snippet só
		   conhecia quem passa no portão; desde que os barrados existem aqui
		   dentro, uma categoria poderia declarar três espécies e as três serem
		   barradas — o cartão viraria link para uma página de tabela vazia, que
		   é exatamente a página fina que o 16.5 existe para não deixar entrar
		   no índice de domínio novo. */
		$quantas = 0;
		foreach ( $cat['especies'] as $id ) {
			if ( isset( $catalogo[ $id ] ) ) {
				$quantas++;
			}
		}
		$url = '';
		if ( $quantas ) {
			$url = aquametria_casca_url_se_existir( $slug );
		}
		$html .= '<li class="aqm-px-cat">';
		if ( '' !== $url ) {
			$html .= '<h3><a href="' . esc_url( $url ) . '">'
				. esc_html( isset( $registro[ $slug ]['titulo'] ) ? $registro[ $slug ]['titulo'] : $cat['rotulo'] )
				. '</a></h3>';
			$html .= '<p>' . esc_html( $quantas ) . ' espécies com o mínimo declarado, da menor frente para a maior.</p>';
		} else {
			/* Categoria sem as 3 filhas de dado real não é link e não mostra
			   contagem: é a regra 16.5, e ela existe para categoria vazia não
			   entrar no índice de domínio novo como página fina. */
			$html .= '<h3>' . esc_html( $cat['rotulo'] ) . '</h3>';
			$html .= '<p><span class="aqm-tag">Em breve</span></p>';
		}
		$html .= '</li>';
	}
	$html .= '</ul>';

	$html .= '<h2>O que esta parte do site responde</h2>';
	$html .= '<p>Uma pergunta só, e ela tem duas metades. A primeira: <strong>qual é o aquário mínimo desta espécie</strong> — e a resposta vem em centímetros de frente e de fundo, porque é assim que os compêndios de aquarismo declaram. '
		. 'A segunda: <strong>quantos exemplares cabem no aquário que você tem</strong> — e aí a resposta é uma faixa, porque as fontes brasileiras de lotação vão de 1 cm de peixe por litro até 4 litros por cm de peixe, e isso é quatro vezes de diferença para o mesmo peixe no mesmo aquário.</p>';
	$html .= '<p>A ilha não escolhe uma das duas réguas para você. Ela publica as duas com a atribuição de cada extremo e diz o que cada uma ignora — as duas contam comprimento e nenhuma conta massa, formato ou carga biológica. '
		. 'Onde o banco não tem fonte que preste, a ficha diz que não tem, em vez de chutar um número redondo.</p>';
	$html .= '<p class="aqm-prova">' . esc_html( $com_ficha ) . ' espécies têm ficha própria no ar hoje, e a contagem desta frase é feita na hora de imprimir a página, não digitada. '
		. 'Todo número do banco veio de busca restrita ao domínio da fonte, porque o egresso da nuvem barra a leitura direta das duas bases usadas — é reconferência em aberto, e está escrita na nota do banco.</p>';

	/* AS QUE FICARAM DE FORA. A frase de abertura diz quantas espécies a ilha
	   publica; sem este bloco ela era a única coisa que a página dizia sobre o
	   tamanho do banco, e quem lesse não tinha como saber que existem registros
	   colhidos que a tabela não mostra. Os três números são contados na hora,
	   nunca digitados, e o terceiro é a subtração dos dois primeiros feita pelo
	   PHP — número de tela nasce contado (seção 8). */
	$barrados = aquametria_peixes_barrados();
	if ( $barrados ) {
		$total = count( $catalogo ) + count( $barrados );
		$html .= '<h2>As espécies que o banco tem e esta seção não publica</h2>';
		$html .= '<p>O banco desta ilha guarda ' . esc_html( $total ) . ' registros de espécie, e '
			. esc_html( count( $catalogo ) ) . ' deles têm o mínimo declarado que as tabelas acima exigem. '
			. 'Os outros ' . esc_html( count( $barrados ) ) . ' estão aqui pelo nome, com o que falta em cada um — '
			. 'porque espécie que a ilha já procurou e não publica é uma ausência que ninguém consegue adivinhar do lado de fora. '
			. 'A ordem é de quem está mais perto de entrar para quem está mais longe, e nenhuma delas tem número chutado para completar o que a fonte não declarou.</p>';
		$html .= aquametria_peixes_barrados_lista_html( $barrados );
	}

	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. Shortcodes — a página se reconhece pelo SLUG
 *
 * Pelo slug e não pelo atributo do shortcode: os cinco corpos são
 * `[aquametria_peixes_ficha]` sem parâmetro nenhum, então não existe o caso de
 * alguém editar a página no wp-admin e passar o id de outra espécie.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_slug_atual' ) ) {
function aquametria_peixes_slug_atual() {
	$registro = aquametria_peixes_registro();

	/* Na bancada o slug chega pelo global, como nos outros renderizadores. */
	if ( ! empty( $GLOBALS['__slug_pagina'] ) && isset( $registro[ $GLOBALS['__slug_pagina'] ] ) ) {
		return $GLOBALS['__slug_pagina'];
	}
	if ( ! function_exists( 'is_singular' ) || ! is_singular() ) {
		return null;
	}
	$pagina = get_post();
	if ( ! $pagina || empty( $pagina->post_name ) ) {
		return null;
	}
	return isset( $registro[ $pagina->post_name ] ) ? $pagina->post_name : null;
}
}

add_shortcode( 'aquametria_peixes_ficha', function () {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return '';
	}
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_ficha_html( $slug );
} );

add_shortcode( 'aquametria_peixes_categoria', function () {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return '';
	}
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_categoria_html( $slug );
} );

add_shortcode( 'aquametria_peixes_secao', function () {
	add_action( 'wp_footer', 'aquametria_peixes_imprimir_estilo', 20 );
	return aquametria_peixes_secao_html();
} );

/* ---------------------------------------------------------------------------
 * 9. A casca: as páginas e a árvore
 *
 * Quem cria página é a casca (1.7.0), pelo filtro `aquametria_paginas`. Quem
 * diz onde cada uma mora na árvore é o filtro `aquametria_peixes`, no mesmo
 * molde do hub de calculadoras e da prateleira de guias: a casca não guarda
 * cópia de título nenhum, e página nova aparece na trilha sozinha.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_registrar_paginas' ) ) {
function aquametria_peixes_registrar_paginas( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		$paginas = array();
	}
	foreach ( aquametria_peixes_registro() as $slug => $def ) {
		$paginas[ $slug ] = array(
			'titulo'   => $def['titulo'],
			'conteudo' => $def['conteudo'],
			'pai'      => $def['pai'],
		);
	}
	return $paginas;
}
}
add_filter( 'aquametria_paginas', 'aquametria_peixes_registrar_paginas' );

if ( ! function_exists( 'aquametria_peixes_registrar_arvore' ) ) {
function aquametria_peixes_registrar_arvore( $lista ) {
	if ( ! is_array( $lista ) ) {
		$lista = array();
	}
	$categorias = aquametria_peixes_categorias();
	foreach ( aquametria_peixes_registro() as $slug => $def ) {
		$cat = ( 3 === $def['nivel'] && isset( $categorias[ $def['pai'] ] ) )
			? array( $def['pai'], $categorias[ $def['pai'] ]['rotulo'] )
			: array();
		$lista[ $slug ] = array(
			'nivel'  => $def['nivel'],
			'pai'    => $def['pai'],
			'rotulo' => $def['titulo'],
			'nivel2' => $cat,
		);
	}
	return $lista;
}
}
add_filter( 'aquametria_peixes', 'aquametria_peixes_registrar_arvore' );

/* ---------------------------------------------------------------------------
 * 10. Estilo e JSON-LD — os dois no wp_head, nunca no retorno do shortcode
 *
 * Classes NOVAS de propósito (aqm-px-*). A ilha já pagou duas rodadas de teste
 * por reaproveitar classe que um teste de navegador usa como localizador.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_peixes_css' ) ) {
function aquametria_peixes_css() {
	return <<<'CSS'
.aqm-px{--px-tinta:var(--aqm-tinta,#0D1B22);--px-lamina:var(--aqm-lamina,#0E7C8C);
--px-papel:var(--aqm-papel,#F4F7F7);--px-superficie:var(--aqm-superficie,#FFFFFF);
--px-traco:var(--aqm-traco,#DDE5E6);--px-legenda:var(--aqm-legenda,#5C7075);
--px-alerta:var(--aqm-alerta,#B5762A);
--px-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--px-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--px-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
font-family:var(--px-texto);color:var(--px-tinta);max-width:56rem;}
.aqm-px h2{font-family:var(--px-display);font-size:1.18rem;font-weight:600;
margin:2rem 0 .6rem;line-height:1.3;}
.aqm-px p{line-height:1.65;margin:0 0 .9rem;}
.aqm-px-direta{background:var(--px-papel);border:1px dashed var(--px-traco);
border-radius:3px;padding:1rem 1.1rem;margin:0 0 1.4rem;font-size:.96rem;}
.aqm-px-direta p:last-child{margin-bottom:0;}
.aqm-px-linha-mestra{font-family:var(--px-display);font-size:1.1rem;font-weight:600;
line-height:1.35;}
.aqm-px-rolagem{overflow-x:auto;margin:0 0 1rem;}
.aqm-px-tabela{border-collapse:collapse;width:100%;font-size:.88rem;
background:var(--px-superficie);}
.aqm-px-tabela caption{caption-side:top;text-align:left;font-size:.8rem;
color:var(--px-legenda);padding:0 0 .5rem;line-height:1.5;}
.aqm-px-tabela th,.aqm-px-tabela td{border:1px solid var(--px-traco);
padding:.42rem .55rem;text-align:left;vertical-align:top;}
.aqm-px-tabela thead th{font-family:var(--px-texto);font-weight:600;font-size:.8rem;
background:var(--px-papel);}
.aqm-px-tabela td{font-family:var(--px-mono);font-variant-numeric:tabular-nums;}
.aqm-px-tabela tbody th{font-weight:500;}
.aqm-px-linha-minima td,.aqm-px-linha-minima th{background:var(--px-papel);}
.aqm-px-cientifico{display:block;font-family:var(--px-mono);font-size:.72rem;
font-style:italic;color:var(--px-legenda);}
.aqm-px-criterio,.aqm-px-fora,.aqm-px-sem-loja,.aqm-px-serp-nota{font-size:.86rem;
color:var(--px-legenda);border-left:2px solid var(--px-traco);
padding:.1rem 0 .1rem .7rem;}
.aqm-px-sem-loja{border-left-color:var(--px-alerta);}
.aqm-px-serp-nota{border-left-color:var(--px-lamina);margin:.4rem 0 0;}
.aqm-px-razao{display:block;font-size:.84rem;color:var(--px-legenda);margin:.2rem 0 0;}
.aqm-px-consulta{font-family:var(--px-mono);font-size:.76rem;color:var(--px-legenda);
border-top:1px solid var(--px-traco);margin:1.4rem 0 0;padding:.6rem 0 0;}
.aqm-px-barrados{list-style:none;padding:0;margin:0 0 1.4rem;}
.aqm-px-barrados li{font-size:.88rem;color:var(--px-legenda);
border-bottom:1px solid var(--px-traco);padding:.5rem 0;}
.aqm-px-barrados strong{font-family:var(--px-mono);font-style:italic;
font-weight:500;color:var(--px-tinta);}
.aqm-px-irmas,.aqm-px-cats{list-style:none;padding:0;margin:0 0 1.2rem;}
.aqm-px-irmas li{border-bottom:1px solid var(--px-traco);padding:.5rem 0;}
.aqm-px-cats{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:.8rem;}
.aqm-px-cat{border:1px solid var(--px-traco);border-radius:3px;padding:.8rem .9rem;
background:var(--px-superficie);}
.aqm-px-cat h3{font-family:var(--px-display);font-size:.98rem;margin:0 0 .4rem;}
.aqm-px-cat p{font-size:.84rem;color:var(--px-legenda);margin:0;}
.aqm-px a{color:var(--px-lamina);}
@media (max-width:600px){.aqm-px-direta{font-size:.92rem;padding:.85rem .9rem;}
.aqm-px-tabela{font-size:.82rem;}}
CSS;
}
}

if ( ! function_exists( 'aquametria_peixes_estilo_impresso' ) ) {
function aquametria_peixes_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_peixes_imprimir_estilo' ) ) {
function aquametria_peixes_imprimir_estilo() {
	if ( aquametria_peixes_estilo_impresso() ) {
		return;
	}
	aquametria_peixes_estilo_impresso( true );
	echo '<style id="aquametria-peixes-estilo">' . "\n" . aquametria_peixes_css() . "\n" . '</style>' . "\n";
}
}

/**
 * O JSON-LD de cada página do eixo.
 *
 * Ficha: Article + FAQPage, porque o H1 É a pergunta e a resposta está servida
 * no HTML. NÃO é Product — espécie não é produto, e declarar Product sem preço
 * nem disponibilidade é schema inválido com cara de válido.
 * Seção e categoria: CollectionPage + ItemList com as filhas que EXISTEM
 * publicadas, pelo mesmo motivo de o breadcrumb não carregar degrau sem
 * endereço: item de lista sem URL é lista pior, não lista maior.
 */
if ( ! function_exists( 'aquametria_peixes_jsonld_dados' ) ) {
function aquametria_peixes_jsonld_dados( $slug ) {
	$registro = aquametria_peixes_registro();
	if ( ! isset( $registro[ $slug ] ) ) {
		return array();
	}
	$def  = $registro[ $slug ];
	$url  = aquametria_casca_url_se_existir( $slug );
	$nos  = array();

	if ( 3 === $def['nivel'] && isset( $def['especie'] ) ) {
		$catalogo = aquametria_peixes_catalogo();
		if ( ! isset( $catalogo[ $def['especie'] ] ) ) {
			return array();
		}
		$e      = $catalogo[ $def['especie'] ];
		$nome   = aquametria_peixes_nome( $e );
		$porte  = aquametria_peixes_porte_faixa( $e );
		$frente = aquametria_peixes_frente_faixa( $e );
		$card    = ! empty( $e['cardume'] ) ? (int) $e['cardume'] : null;
		$larg    = aquametria_peixes_fundo( $e );
		$arranjo = aquametria_peixes_arranjo( $e );

		/* O RABICHO DA RESPOSTA SEGUE O ARRANJO (1.7.0), pelo mesmo motivo do
		   corpo: "para o cardume mínimo de N exemplares" é a frase que o modelo
		   de linguagem cita, e citá-la sobre um peixe solitário publicaria a
		   negação do que a fonte declara — com a autoridade do schema. */
		$rabicho = '';
		if ( $arranjo && null !== $arranjo['fixo'] ) {
			$rabicho = ', para ' . $arranjo['de'] . ' ' . $nome
				. ', que é o que a fonte declara por aquário';
		} elseif ( $card && $arranjo && '' !== $arranjo['minimo'] ) {
			$rabicho = ', para o ' . $arranjo['minimo'] . ' de ' . $card
				. ( ! empty( $e['cardume_ate'] ) ? ' a ' . (int) $e['cardume_ate'] : '' )
				. ' exemplares';
		}
		$resposta = 'O aquário mínimo declarado para o ' . $nome . ' é de '
			. aquametria_peixes_num( $frente[1] ) . ' cm de frente'
			. ( $larg ? ' por ' . aquametria_peixes_num( $larg ) . ' cm de fundo' : '' )
			. $rabicho . '.';
		$v35 = aquametria_peixes_volume_bruto( $frente[1], $larg, 35 );
		if ( null !== $v35 ) {
			$resposta .= ' Com 35 cm de altura isso dá ' . aquametria_peixes_num( $v35 )
				. ' litros brutos de lâmina.';
		}
		$fonte = aquametria_peixes_fonte_do_campo( $e, 'comprimento_minimo_aquario_cm' );
		if ( ! $fonte ) {
			$fonte = aquametria_peixes_fonte_do_campo( $e, 'base_minima_cm' );
		}
		if ( $fonte ) {
			$resposta .= ' Declarado pelo ' . $fonte['corpo'] . ', colhido em '
				. aquametria_peixes_data_br( $fonte['em'] ) . '.';
		}

		$perguntas = array(
			array( $def['titulo'], $resposta ),
		);
		if ( $arranjo && null !== $arranjo['fixo'] ) {
			/* A SEGUNDA PERGUNTA EXISTE NOS DOIS MUNDOS, e no arranjo fixo ela é
			   a mais importante da página: é onde a régua de lotação e a base
			   declarada se contradizem, e é a contradição que a SERP desta
			   consulta publica sem perceber. Sem este ramo a ficha do betta
			   serviria UMA pergunta no FAQPage, e a única que ela tem de
			   responder — "quantos litros para um betta" — ficaria de fora. */
			/* A PERGUNTA NÃO PODE SER A DO TÍTULO. A primeira escrita deste ramo
			   repetia o `titulo` da página palavra por palavra, e o FAQPage ia
			   ao ar com duas Question de MESMO nome e respostas diferentes —
			   duplicata que o Google trata como o que é. A pergunta distinta é
			   a que esta página responde e as outras onze não: se a régua de
			   lotação serve para um peixe cujo número a fonte fixa. */
			$n = $arranjo['fixo'];
			$contra_faq = aquametria_peixes_lotacao_contra_base( $e, $frente, $porte, $larg, $n );
			$l = $contra_faq['litros'];
			$perguntas[] = array(
				'A regra de 1 cm de peixe por litro serve para o ' . $nome . '?',
				'Não sozinha. A fonte declara ' . $arranjo['de'] . ' ' . $nome
					. ' por aquário, e o que ela declara é a BASE: '
					. aquametria_peixes_num( $frente[1] ) . ' cm de frente'
					. ( $larg ? ' por ' . aquametria_peixes_num( $larg ) . ' cm de fundo' : '' ) . '. '
					. 'As duas réguas brasileiras de lotação, aplicadas a ' . $n . ' exemplar'
					. ( $n > 1 ? 'es' : '' ) . ' de ' . aquametria_peixes_num( $porte[1] )
					. ' cm, dariam de ' . aquametria_peixes_num( $l['classica'] ) . ' a '
					. aquametria_peixes_num( $l['conservadora'] ) . ' litros'
					. ( '' !== $contra_faq['frase'] ? ', e ' . $contra_faq['frase'] : '' )
					. '. Elas contam centímetros de peixe e não sabem de comportamento.',
			);
		} elseif ( $card ) {
			$l = aquametria_peixes_litros_por_criterio( $card * $porte[1] );
			$perguntas[] = array(
				'Quantos litros para ' . $card . ' ' . $nome . '?',
				$card . ' ' . $nome . ' somam ' . aquametria_peixes_num( $card * $porte[1] )
					. ' cm de peixe adulto. Pela regra clássica brasileira de 1 cm por litro isso pede '
					. aquametria_peixes_num( $l['classica'] ) . ' litros; pelo critério conservador de 4 litros por cm, '
					. aquametria_peixes_num( $l['conservadora'] )
					. ' litros. A Aquametria publica os dois extremos com a atribuição de cada um em vez de tirar média.',
			);
		}
		$perguntas[] = array(
			'Qual é a temperatura do ' . $nome . '?',
			'As fontes declaram de ' . aquametria_peixes_num( $e['temp_min'] ) . ' a '
				. aquametria_peixes_num( $e['temp_max'] ) . ' °C para o ' . $nome
				. ' (' . $e['cientifico'] . ').',
		);

		$faq = array();
		foreach ( $perguntas as $p ) {
			$faq[] = array(
				'@type'          => 'Question',
				'name'           => $p[0],
				'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
			);
		}

		/* A MESMA editora que os três artigos já declaram. Escrita aqui e não
		   importada do outro snippet porque o Sync desembarca um sem o outro, e
		   o nó de schema não pode depender de quem chegou primeiro. */
		$editora = array(
			'@type' => 'Organization',
			'name'  => 'Aquametria',
			'url'   => home_url( '/' ),
		);

		$artigo = array(
			'@type'         => 'Article',
			'headline'      => $def['titulo'],
			'about'         => array(
				'@type' => 'Thing',
				'name'  => $nome,
				'alternateName' => $e['cientifico'],
			),
			'inLanguage'    => 'pt-BR',
			'isAccessibleForFree' => true,
			'author'        => $editora,
			'publisher'     => $editora,
		);
		if ( '' !== $url ) {
			$artigo['mainEntityOfPage'] = $url;
		}

		/* AS DUAS DATAS, da mesma fonte que o sitemap: item 2 do despacho da
		   Sentinela de 13/09/2026. As 11 fichas serviam `Article` sem data, sem
		   autor e sem publicador, enquanto o `Article` dos três artigos trazia os
		   quatro campos — e a assimetria era a prova de que faltava, não de que
		   alguém escolheu. Numa ilha cuja tese é procedência COM DATA, a ficha de
		   espécie é a página que mais depende disso.

		   `datePublished` sai de `post_date_gmt` e não de um campo do registro
		   das páginas: nenhuma das 11 declara data de publicação em lugar nenhum
		   do repositório, então o post é a única coisa que sabe. Escrever à mão a
		   data da leva seria a constante do item 1 renascendo na página vizinha.

		   Sem casca ou sem data, os campos não saem — a regra está no cabeçalho
		   de `aquametria_casca_data_da_pagina()`. */
		$publicado = function_exists( 'aquametria_casca_data_da_pagina' )
			? aquametria_casca_data_da_pagina( 'publicado' )
			: '';
		if ( '' !== $publicado ) {
			$artigo['datePublished'] = $publicado;
		}
		$modificado = function_exists( 'aquametria_casca_data_da_pagina' )
			? aquametria_casca_data_da_pagina( 'modificado' )
			: '';
		if ( '' !== $modificado ) {
			$artigo['dateModified'] = $modificado;
		}
		$nos[] = $artigo;
		$nos[] = array( '@type' => 'FAQPage', 'mainEntity' => $faq );

		return $nos;
	}

	/* Seção e categoria: CollectionPage + ItemList das filhas publicadas. */
	$itens = array();
	$posicao = 0;
	foreach ( $registro as $outro => $outra ) {
		if ( $outra['pai'] !== $slug ) {
			continue;
		}
		$url_filha = aquametria_casca_url_se_existir( $outro );
		if ( '' === $url_filha ) {
			continue;
		}
		$posicao++;
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $posicao,
			'name'     => $outra['titulo'],
			'item'     => $url_filha,
		);
	}

	$colecao = array(
		'@type'      => 'CollectionPage',
		'name'       => $def['titulo'],
		'inLanguage' => 'pt-BR',
	);
	if ( '' !== $url ) {
		$colecao['mainEntityOfPage'] = $url;
	}
	$nos[] = $colecao;
	if ( $itens ) {
		$nos[] = array(
			'@type'           => 'ItemList',
			'name'            => $def['titulo'],
			'numberOfItems'   => count( $itens ),
			'itemListElement' => $itens,
		);
	}

	return $nos;
}
}

if ( ! function_exists( 'aquametria_peixes_imprimir_jsonld' ) ) {
function aquametria_peixes_imprimir_jsonld( $slug ) {
	foreach ( aquametria_peixes_jsonld_dados( $slug ) as $no ) {
		$no = array_merge( array( '@context' => 'https://schema.org' ), $no );
		echo '<script type="application/ld+json">'
			. wp_json_encode( $no, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
			. '</script>' . "\n";
	}
}
}

if ( ! function_exists( 'aquametria_peixes_cabeca' ) ) {
function aquametria_peixes_cabeca() {
	$slug = aquametria_peixes_slug_atual();
	if ( null === $slug ) {
		return;
	}
	aquametria_peixes_imprimir_estilo();
	aquametria_peixes_imprimir_jsonld( $slug );
}
}
add_action( 'wp_head', 'aquametria_peixes_cabeca', 21 );

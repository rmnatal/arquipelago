# Registro de execuções — Rodametria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-10-28 13h19Z–13h4xZ — **O BLOCO 2, E A DECISÃO DE ENGENHARIA QUE TIRA A ILHA DA ESPERA.** As três ferramentas especificadas inteiras, 9 constantes com procedência — e o limiar legal que a F1 não tem **isolado num objeto JSON**, para a chegada da fonte ser a edição de um arquivo e não um bloco

**O que saiu:** `dados/especificacao-calculadoras.md` (470 linhas) e
`dados/constantes.json` (**9 constantes**: 6 publicáveis, 2 `pendente` com a consequência
declarada, 1 observação de mercado). Para cada uma das três ferramentas: entradas com tipo
e exemplo pré-preenchido, saída, fórmula degrau por degrau, **o que ela se recusa a
responder**, tabela pré-renderizada, bloco de compra com o critério de entrada do produto,
e a prestação de contas da seção 7 com os grupos de recusa separados por causa.
`publicar: false` nos dois, como todo bloco de dado.

**A DECISÃO DO BLOCO, e ela é o que fica depois de hoje.** A ilha estava numa armadilha
simples: a F1 **é** a home, o produto dela **é** a categoria legal, e o texto que decide a
categoria é negado pelo egresso há duas execuções. A saída não foi esperar nem improvisar
um número — foi **separar o que depende da fonte do que não depende**. Os quatro limiares
(`LIMIAR_BIKE_W`, `LIMIAR_BIKE_KMH`, `LIMIAR_AUTOPROP_W`, `LIMIAR_AUTOPROP_KMH`) viraram
**uma constante só**, referenciada **por nome** na árvore de decisão, com **literal
numérico proibido** no código da F1. A árvore inteira, as duas ressalvas obrigatórias, a
camada municipal, o bloco de compra e o esquema do banco estão escritos e podem ser
construídos. **Quando o texto oficial chegar, a F1 destrava editando um objeto JSON** —
preencher `valor`, trocar `status`, gravar `url` e `verificado_em`. Nenhuma linha de lógica
muda. *É por isso que este bloco não esperou a fonte: o que a fonte decide é um objeto, e o
que ela não decide é tudo o mais.*

**O QUE CONTINUA TRAVADO, remedido e não herdado do campo.** Às 13h2xZ, em duas passadas:
`gov.br`, `in.gov.br`, `planalto.gov.br`, `contran.gov.br` e `lex.com.br` — **os cinco** em
`CONNECT tunnel failed, response 403`, com `rodametria.com.br` em **200** na mesma janela.
Três horas e meia depois do despacho ALTA do bloco 1, o pedido segue aberto. **A F1 não vai
ao ar**, e não vai com número de portal, não vai com o número que mais apareceu e não vai
"com ressalva" — a seção 10 proíbe constante `pendente` dentro de fórmula publicada, e aqui
a fórmula publicada é o produto da ilha. **A F2 e a F3 podem ir ao ar.**

**A ERRATA DO BLOCO 1, e ela é a razão de um despacho novo existir.** O corpus entregou à F2
*"a régua do relevo com número: 41,29 Wh/km em plano × 97,74 Wh/km a 12%"* e calculou com
ela sobre **1.200 Wh**, uma bateria de patinete. A coleta limpa de hoje achou o registro do
estudo: *"Análisis de la eficiencia energética de la batería de ion litio en una **moto
eléctrica** para el uso de micro movilidad"* — Rodrigo David Limaico Quinteros, Maestría en
Ingeniería Automotriz, UPS sede Quito, **2025**, bateria de **60 V e 30 Ah (1.800 Wh)**,
rota de **25,8 km**. **Wh/km absoluto de uma moto de 1.800 Wh não é o de um patinete de 500
Wh.** O que virou constante foi a **razão** — `97,74 ÷ 41,29 = 2,37` —, medida na mesma
rota, com o mesmo veículo e a mesma bateria, que é a única forma de um número atravessar
classe de veículo. A errata está escrita **nos dois lugares do corpus** que carregavam a
frase, com o original riscado e preservado.

**E a mesma tese deu de graça o número que faltava:** **29,8 km medidos em condição mista
contra 60 km declarados na ficha — 49,7%**. O corpus registrava *"60% a 80% do valor
anunciado"* como leitura agregada sem fonte única, e dizia ele mesmo que não servia de
constante. **A medição nomeada cai abaixo do piso daquela faixa**, e é a direção que
importa: a faixa agregada era otimista. Entra como **linha de calibração** da tabela da F2,
com autor e instituição dentro da frase, e **não** multiplica nada.

**A TERCEIRA COISA QUE A COLETA LIMPA FEZ FOI REBAIXAR UM NÚMERO DA PRÓPRIA ILHA.** O bloco
1 anotou que *"uma fonte estrangeira colhida sugere margem de pelo menos 10% acima do peso
do condutor"*, e a F3 ia nascer com essa margem atribuída a terceiro. A busca limpa — sem o
número dentro da pergunta — percorreu 13 publicadores e **não achou percentual publicado em
nenhum**. O que existe publicado é **qualitativo e convergente** em três deles, um
brasileiro: perto do teto declarado, a velocidade e a aceleração máximas não são
alcançadas. **Então a margem de 10% virou `decisao_da_ilha`, com o motivo escrito** — a
direção do erro caro aponta para a folga —, e a página nunca a atribui a ninguém. *Atribuir
a terceiro uma régua que terceiro não publicou é pior que não ter régua.* E o número não é
cosmético: 10% sobre o teto de mercado de 120 kg exclui quem passa de **109 kg**, que é
exatamente a pessoa do `VOZ.md`.

**O que a F2 deixou de poder fazer, e fica dito em vez de disfarçado:** sem régua de consumo
por km de **patinete**, ela não devolve km absoluto a partir de V e Ah. Devolve `Wh = V × Ah`
(identidade, não precisa de fonte nenhuma), a faixa degradando a autonomia **declarada** pelo
fator de relevo, e — quando a pessoa não informa a declarada — **diz que não estima km,
nomeando o que falta**. A única medição de patinete que existe (≈ 20 Wh/km, 4.000 km rodados,
70 ciclos) está em dois hosts que não resolvem nesta nuvem. Os outros três candidatos foram
reprovados **com o motivo escrito um por um** em `constantes.json`: um é de bicicleta e de
fabricante de kit, um é circular (divide a autonomia declarada pela energia, assumindo
justamente o número que a F2 existe para não assumir), e um é de moto.

**Despacho novo, prioridade NORMAL** (`dados/despachos.md`): três domínios —
`stdjet.scienceandtechnology.com.vn`, `et.vnuhcmjournal.com.vn` e `dspace.ups.edu.ec` — ou a
leitura no Chrome. **É NORMAL e não ALTA de propósito: ele melhora a F2, não a libera.** O
terceiro domínio é o mais barato dos três: ele sobe de "leitura por busca" para leitura
direta as **duas constantes publicáveis** que esta execução já gravou.

**Próximo passo desbloqueado — bloco 3, modelo do banco, e ele não depende de site NEM de
fonte bloqueada.** A seção 5 da especificação já entrega o contrato: os campos que as três
ferramentas leem, `potencia_nominal_w` e `potencia_pico_w` **separados** (a F1 só lê o
nominal), **`acelerador` como enum de TRÊS valores** — `nao_declarado` é o terceiro, com
frase própria, e **nunca** cai em "só pedal assistido" por omissão, porque é o pivô da
classificação —, `energia_wh` **derivado** de V × Ah e nunca copiado de anúncio, e
**`categoria` como campo DERIVADO da F1, nunca de entrada do catálogo**: gravar categoria à
mão é deixar o anúncio escrever a regra.

## 2026-10-28 10h17Z–10h25Z — **O BLOCO 1, E AS DUAS COISAS QUE ELE ACHOU SEM PROCURAR.** Primeira execução da Fundação nesta ilha. O corpus de buscas saiu inteiro, a **S_par deixou de ser "não medida"** — e no caminho a passada descobriu que **o site já está no ar** e que **a fonte que decide a F1 é negada pelo egresso**

**O que saiu:** `dados/corpus-buscas.md` — quatro eixos (CNH e placa · autonomia ·
carga e tamanho · produto pelo nome), **19 consultas** com procedência medida consulta a
consulta pela busca da nuvem em 28/10, seis achados nomeados, a contagem do vazamento da
busca **por eixo** e a seção 6 com o que o bloco 2 herda pronto. `publicar: false`, como
todo bloco de dado.

**A S_par ESTAVA NO DOSSIÊ COMO "NÃO MEDIDA" E ERA A PRIMEIRA TAREFA DE LEITURA DO
NASCIMENTO. Está medida, e o resultado é mais útil que "aberta" ou "fechada":** o eixo da
CNH está **tomado**, mas por **portal de trânsito e notícia** — `portaldotransito`,
`olhardigital`, `canaltech`, `motonline`, `consultadeplaca`, `doutormultas`, `gringo`,
`zuldigital`, mais folheto de duas prefeituras e PDF de duas entidades. **Nenhum varejo
grande, nenhuma loja, e em sete consultas independentes NENHUMA ferramenta** que receba
potência e velocidade e devolva a categoria. A vaga da F1 não é "ninguém fala disso": é
**"todos falam, ninguém calcula"**.

**E O MOTIVO PELO QUAL A PROSA NÃO RESOLVE É O ACHADO QUE SUSTENTA A ILHA: AS FONTES SE
CONTRADIZEM NO NÚMERO.** Três limites diferentes para a mesma pergunta, todos em fontes
que se apresentam como quem sabe — **350 W / 25 km/h** (que é regra **do Rio**, apresentada
como nacional), **1.000 W / 32 km/h** (nacional) e **4 kW / 50 km/h** (ciclomotor, sem
citar o de 1.000 W) — e uma fonte de primeira página afirmando **CNH categoria A** para
bicicleta elétrica, o contrário de todas as outras. O desacordo não é de tom: é de número,
e é o número que decide se a pessoa sai de casa habilitada.

**Os três achados que amarram a ilha, e os dois primeiros estão em título de loja grande:**
- *"**Bicicleta elétrica** aro 24 Sousa Bike **350W** freio a disco **com acelerador**"* —
  o título diz, ele mesmo, as duas coisas que a regra não deixa coexistir. Pelo que o eixo
  A mediu (as fontes convergem exatamente aqui), **acelerador manual tira o veículo da
  definição de bicicleta elétrica, mesmo abaixo do limite de potência**.
- *"**Bicicleta elétrica** Siena **1000W** adulto **sem CNH** **scooter**"* — quatro termos
  que a resolução separa, num anúncio só.
- O guia que elege **"o melhor patinete elétrico de 2026 para adultos"** descreve o
  vencedor com **dois motores de 1.000 W e 72 km/h**. Pelos limites colhidos, 72 km/h **não
  é autopropelido em nenhuma leitura**. **A página que mais aparece para "melhor patinete
  adulto" recomenda, sem dizer, um ciclomotor** — e é a frase da ilha inteira numa linha:
  *o número grande do anúncio não é o número que a regra lê.*

**O que isto muda no bloco 2, e está escrito na seção 6 do corpus:** a F1 tem **quatro**
entradas, não três — o **acelerador é pivô, não detalhe** (sem ele nenhuma potência
classifica) —, e a saída tem **duas camadas**, porque a resposta é nacional **e** municipal
(Campinas regulamenta 20 km/h; o Rio tem os 350 W/25 km/h próprios). A F1 que responder
"autopropelido, dispensa CNH" sem dizer que a rua é municipal estaria certa na categoria e
incompleta na vida. Para a F2, o eixo B entregou a régua do relevo **com número**: 41,29
Wh/km em plano contra **97,74 Wh/km a 12% de inclinação** — a reler na fonte e datar. Para
a F3, o teto de mercado está medido em **120 kg**, com a régua de margem de 10% que exclui
quem passa de 109 — e a pessoa de 110 kg do `VOZ.md` cai exatamente ali.

### O SITE JÁ ESTAVA NO AR, E O `ESTADO.md` DIZIA "PENDENTE" — a seção 4 em ação, no primeiro dia da ilha

A conferência de rede da **20.2** era para ser barata e de rotina. Devolveu **200 em três
tentativas**, com `<title>Rodametria - Mobilidade elétrica</title>` e `last-modified` de
**27/10 às 22h17Z** — ou seja, o WordPress subiu **cinco horas depois** de a ilha nascer, e
o cabeçalho que esta execução leu ainda dizia *"WordPress: pendente"*, *"nameservers
pendente"*, *"hospedagem pendente"* e *"lista de domínios permitidos pendente"*. **Nenhum
dos quatro estava pendente.** É a seção 4 no estado puro, e no dia 1: o site anda e o
cabeçalho fica para trás em silêncio.

**O que de fato falta, medido e não herdado:** tema de blocos cru, **zero página
publicada**, `/wp-sitemap.xml` sem URL nenhuma, e `/wp-json/rodametria/v1/status` em **404**
— o snippet de Sync não existe. O que está **são**: `/wp-json/` em 200 e
`/nao-existe-xyz/` devolvendo **404 de verdade**, então a porta de entrada da seção 29 passa
nesta primeira leitura (vale reconferir quando houver página, que é quando o `.htaccess`
costuma cair).

### A FONTE QUE DECIDE O PRODUTO DESTA ILHA É NEGADA PELO EGRESSO (20.3)

O `PROMPT.md` desta ilha é explícito: a constante central da F1 *"só vira `publicavel`
depois de lida no texto oficial do gov.br, com data"*. Medido às 10h4xZ: `www.gov.br` e
`lex.com.br` em **`000` com `connect_rejected`**, e a busca de página falha na própria
resolução de nome (`ENOTFOUND www.gov.br`). **Não é intermitência de túnel** — a 20.2 manda
repetir antes de chamar de bloqueio, e aqui a repetição não muda nada, porque o erro
nomeado pelo egresso é recusa. É a **20.3** em estado puro: a regra que exige a fonte foi
escrita em 27/10 e a fonte nunca foi conferida.

**A consequência, dita sem maquiagem:** o bloco 2 pode ser escrito inteiro daqui, e
`constantes.json` pode nascer com a constante da F1 marcada `publicavel: false` e a dívida
nomeada. **O que não pode é a F1 ir ao ar classificando veículo com número de portal de
notícia** — numa ilha onde errar manda a pessoa para a rua sem habilitação. Virou despacho
**ALTA** em `dados/despachos.md`, com os dois gestos que o resolvem (liberar `gov.br` na
lista de rede, **ou** colar as três definições literais com URL e data). **E a ilha NÃO
recebeu `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.

### A 30.8 MEDIDA NUMA ILHA NOVA, COM A CONTAGEM QUE FALTAVA: O VAZAMENTO NÃO É PARELHO ENTRE EIXOS

| eixo | ocupantes de fora do Brasil |
|---|---|
| **CNH e placa** (regra brasileira) | **zero** em 7 consultas |
| produto pelo nome | 3 de ~18 |
| carga e tamanho | 6 de ~17 |
| **autonomia** | **~40 de ~50**, e uma consulta com **zero** ocupante brasileiro |
| **peças** (câmara, pneu, carregador) | **18 de 20** em `pccomponentes.pt` |

**A leitura vale para as outras cinco ilhas, e é por isso que está escrita e não só
sentida:** pergunta de **regra brasileira** não tem equivalente em Portugal ou na Espanha,
então a busca da nuvem não tem para onde vazar e a procedência é confiável; pergunta de
**produto e consumível** tem catálogo europeu idêntico, e aí a busca entrega Portugal. **O
vazamento é mínimo exatamente onde esta ilha nasce** — o que é sorte, não desenho, e vale
dito para a próxima Bússola saber que eixo de regra é o mais barato de medir da nuvem. E,
pela assimetria da 30.8, **nada disso autoriza `alvo`**: nenhuma linha do corpus diz `alvo`,
nem no eixo A. A SERP dos eixos de autonomia, carga e peças virou despacho NORMAL.

### Nada foi ao ar, e não podia

A ilha tem WordPress e não tem casca, snippet de Sync, `/status` nem URL própria. Acionar
Sync e conferir no ar era impossível, e dizer que conferi seria inventar. Este bloco é
dado: `publicar: false`, zero URL, zero revisão. A **31.1** não se move por ele.

**Próximo passo desbloqueado:** **bloco 2 — especificação das ferramentas**
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), na ordem obrigatória F1,
F2, F3. Ele pode ser escrito inteiro desta nuvem e **herda da seção 6 do corpus** as quatro
entradas da F1, as duas camadas de saída, a régua do relevo da F2 e o teto de 120 kg da F3.
**A constante legal da F1 nasce `publicavel: false`** até o despacho ALTA de 28/10 ser
atendido — e quem fechar o bloco 2 lê a seção 4 do corpus antes, para não ler a tabela do
eixo A como se fosse a resolução.

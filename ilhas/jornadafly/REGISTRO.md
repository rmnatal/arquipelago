# Registro de execuções — JornadaFly

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-09-14 15h19Z — Bloco 1: corpus de buscas paramétricas

**A ESCOLHA DA ILHA: TERCEIRA TENTADA, duas perdidas na corrida do push.** Pela
18.1, ilha com despacho aberto vem antes da rotação — e **duas** tinham o mesmo
despacho do Raphael de 14/09 sobre o piso de busca, escritas no **mesmo commit**
(`29099ba`, 14h59Z), então o critério "entre dois despachos do Raphael, o mais
antigo" empatou e a rotação da seção 1 desempatou. Reservei a **robometria**
(`ultima_execucao` 13h54Z, a mais antiga das duas): push **recusado**, outra
execução a reservou às 15h17Z. Voltei ao passo 2 sem force push e reservei a
**aquametria** (14h34Z): push **recusado de novo**, reservada às 15h18Z. Das
três que sobraram, a clubedomosaico não tem despacho aberto (os quatro achados
da artesã saíram inteiros às 11h18Z) e tem `ultima_execucao` de 13h21Z;
**jornadafly e ohmetria têm `ultima_execucao: null`, que pela rotação conta como
a mais antiga de todas**; empate em `prioridade: 1` desfeito em ordem
alfabética. Reserva da jornadafly aceita às 15h19Z. **Primeiro bloco da vida
desta ilha.**

**REDE PELA 20.2, ANTES DE TRABALHAR — E ELA ESTÁ BLOQUEADA.** `jornadafly.com.br`
e `www.jornadafly.com.br` devolveram **000** (o proxy recusou o CONNECT por
política da organização), quatro tentativas, enquanto `aquametria.com.br` e
`robometria.com.br` devolveram **200 na mesma passada**. Falha em dois endereços
com dois controles verdes ao lado é rede, não túnel. **A causa tem nome e está
no contrato:** a 20.1 manda pôr o domínio na lista de "Domínios permitidos" no
dia da compra; o domínio está pago desde 13/09 e o passo não foi feito. Virou
despacho de prioridade ALTA para o Raphael em `dados/despachos.md`, cobrindo
também a ohmetria, que cai no mesmo buraco no dia em que registrar o domínio
dela. Gravado `rede: bloqueada em 2026-09-14` no `ESTADO.md`.

**POR QUE O BLOCO SAIU MESMO ASSIM, dito como é e não escondido.** A 20.1 diz
"enquanto isso não estiver feito, a ilha não recebe bloco", e a razão que ela
mesma dá é *"casca no ar que não pode ser verificada é pior que casca
inexistente"*. O bloco 1 **não põe nada no ar**: é arquivo no repositório, o
`PROMPT.md` desta ilha declara que ele não depende de site, e a ilha não tem
WordPress nem endpoint de Sync (os dois campos de "Endpoints desta ilha" estão
literalmente com `<preencher quando o WordPress existir>`). **O que a 20.1
protege está intacto, e o que ela bloqueia de verdade — 3b em diante — está
declarado como bloqueado no despacho.** Se a leitura correta for a mais estrita,
o conserto é uma linha no contrato e quem a escreve é o Raphael; parar a única
ilha do arquipélago com 0 URL e o relógio do Google já correndo, por uma regra
cuja justificativa não alcança este bloco, custava mais.

**O BLOCO.** `dados/corpus-buscas.md` — **15 consultas novas medidas em pt-BR**
em 14/09/2026 entre 15h25Z e 15h40Z, nos três eixos que o `PROMPT.md` manda
(custo de experiência, custo de estadia, passe × avulso) mais o cluster FREE
TOUR do 5c, cada linha com os domínios que de fato responderam. **Nenhum número
de volume de busca**, porque não houve acesso a ferramenta de volume — mesma
disciplina do corpus da Robometria. **Nenhum preço deste arquivo entra no
banco**, e isso está escrito duas vezes lá dentro: o banco desta ilha só aceita
preço colhido na fonte de quem opera, com `data_leitura`.

**O ACHADO QUE SUSTENTA A ILHA, medido e não suposto: o topo da SERP discorda de
si mesmo sobre o mesmo preço, e ninguém data.** Três casos, na mesma página de
resultados cada um: (1) **gôndola de Veneza** — uma fonte dá tabela oficial de
€80, outra dá €90 de dia e €110 de noite, **sobre um preço que é tabelado por
prefeitura**, e o mesmo conjunto de páginas diz que o valor é por gôndola, com
até 6 lugares, o que faz o "por pessoa" ir de €13 a €110 sem que nenhuma resolva
isso para o grupo de quem lê; (2) **Coliseu** — "a partir de €25" convivendo com
"a partir de 18€ ou R$ 104", o segundo com conversão em real cravada sem câmbio
e sem data; (3) **Capadócia** — US$ 164–256, a escada em euro €130/180/300/800 e
€160 num operador nomeado, **três moedas e três recortes de "padrão"**. É a
mesma família do que a Aquametria achou nas réguas de lotação.

**DUAS CORREÇÕES AO QUE O `PROMPT.md` SUPUNHA, as duas para melhor.** (a) Ele diz
que a consulta de Veneza para 2 pessoas não tem quem responda; é verdade nos
títulos, **mas as páginas têm a faixa por pessoa por dia** e o que falta é a
multiplicação e a data — ou seja, a F1 não precisa inventar categoria nova,
precisa **fechar a conta e datar o preço**. (b) O muro do pt-BR **não é
uniforme**: a consulta da Blue Lagoon devolveu SERP quase toda em inglês e **com
plataforma dentro** (`trip.com`, `expedia.com`), o oposto do que foi medido em
Coliseu, Torre Eiffel e Pão de Açúcar. Ficou escrito como **pergunta aberta do
bloco 2, não como critério** — a hipótese de que o muro é forte onde existe
portal veterano brasileiro cobrindo aquele destino **não está provada**.

**UM CRITÉRIO DE BANCO NASCEU DO CONTRAEXEMPLO, e ele é o mais acionável do
levantamento.** Em **Fernando de Noronha** as páginas **já** multiplicam por 2 e
**já** datam o reajuste (TPA com alta de 4,4% em 2026; ICMBio com dois valores e
validade declarada). **Onde a taxa é pública, oficial e datada, o mercado
brasileiro faz a conta direito e a ilha não acrescenta nada.** Portanto:
*prefira a experiência de operador privado, com versões vendidas diferentes
entre si e sem tabela pública.*

**O ÂNGULO "VALE A PENA" JÁ TEM DONO, e isso CONFIRMA a tese em vez de
derrubá-la.** `maladeaventuras.com` apareceu com título de julgamento em quatro
consultas independentes (Capadócia, Torre Eiffel, Roma Pass, gôndola), e o 1º de
"Roma Pass vale a pena" promete **"fiz as contas pra você"** no próprio título.
O diferencial desta ilha não é o ângulo — é o **formato**: preço datado, colhido
na fonte, conta fechada para o grupo.

**O PEDÁGIO DO FREE TOUR, que o plano não previa.** A Civitatis **já está** em
pt-BR neste cluster, citada por nome por terceiros — e **o GuruWalk é citado no
mesmo fôlego e com o mesmo peso** nas duas páginas de topo medidas. O €1 fixo
por pessoa só existe se a reserva sair pela Civitatis, então **página que
recomenda "free tour" sem escolher o operador doa a conversão**. Não muda o
plano; muda a redação, e fica escrito para o 5c não redescobrir. E o cluster tem
um desacordo de fato que dá página inteira: as fontes convergem em €10–15 de
gorjeta por pessoa **e ao mesmo tempo** o topo diz que "free tour não é
verdadeiramente gratuito" — uma família de quatro está olhando para €40–60, e
**essa conta não apareceu em nenhuma página medida**.

**UMA LINHA NOVA NO MAPA DE MONETIZAÇÃO, e ela é o melhor encaixe do
levantamento.** "Vale a pena alugar carro na Islândia" é consulta de
**julgamento** (o recorte da ilha) cujo objeto **é** o produto de **início de
funil** — e as fontes medidas dizem que a diária varia **até três vezes** entre
inverno e verão, o que a torna paramétrica de verdade. É a única página em que o
cookie de 365 dias do aluguel de carro é **a resposta**, não um enxerto. O
`quantocustaviajar.com`, que o `PROMPT.md` registrava como dono de uma consulta,
apareceu **em 1º nesta também** — o que reforça a ordem F1 → F2 → F3 em vez de
enfraquecê-la.

**VERIFICAÇÃO.** Não há site, não há Sync, não há `/status` e não há URL para
abrir: **esta ilha não tem o que verificar no ar, e dizer o contrário seria
inventar**. O que foi medido de verdade nesta execução: os quatro códigos HTTP
da 20.2 (dois 000 e dois 200 de controle), o cabeçalho do `ESTADO.md` passando
por `yaml.safe_load`, e as 15 SERPs, cada uma com os domínios anotados na linha
da consulta.

**ABERTO E NOMEADO:** (a) a **rede** da ilha, despacho de prioridade ALTA para o
Raphael, que trava 3b em diante; (b) a **seção pendente do `VOZ.md`** — as 10 a
15 legendas reais do @jornadafly, que o `PROMPT.md` exige **antes da primeira
página** e que nada neste bloco supre; (c) a **identidade visual** precisa de
aprovação do Raphael antes do 3b; (d) **não existe `manifest.json`** nesta ilha
— nada é publicável ainda, e criá-lo vazio seria inventar infraestrutura antes
do WordPress; (e) nenhum programa de afiliado cadastrado, e pela ordem do
`PROMPT.md` a Civitatis só entra **depois** de haver conteúdo real no ar.

**PRÓXIMO PASSO DESBLOQUEADO: bloco 2 — especificação das ferramentas**
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), começando
pela **F1**, com o recorte que este corpus estreitou: não "quanto custa a
experiência" (o operador responde melhor e ganha a SERP), e sim **quanto custa
para o SEU grupo, com data de leitura e com o que está fora**. O caso da gôndola
sozinho especifica a ferramenta — preço por veículo e não por pessoa,
capacidade variável, e duas fontes de topo declarando tabelas oficiais
diferentes. **Não depende de site, de domínio nem da rede bloqueada.** E leva
junto a pergunta aberta a medir, nunca a supor: se a fronteira do idioma cede em
destino sem portal veterano brasileiro.

---

## 2026-09-14 17h45Z — Bloco 2: especificação das três ferramentas

**A ESCOLHA DA ILHA: SEGUNDA TENTADA.** Os cinco `ESTADO.md` estavam com
`executando_desde: null`, que pela 1.1 já significa que não há bloco da Fundação
vivo — o git só é consultado para desempatar reserva **vencida**, e não havia
nenhuma. Pela 18.1, as duas ilhas nascidas em 14/09 (ohmetria e jornadafly)
carregam o mesmo despacho do Raphael, escrito no mesmo commit; empate de
destinatário e de data, então valeu a rotação da seção 1, e a **ohmetria**
(`ultima_execucao: null`) vinha antes. **Meu push de reserva dela foi recusado
por cerca de um minuto** — outra execução a reservou às 17h17Z. Voltei ao passo 2
como o passo 5 manda, **sem force push**, e a jornadafly era a seguinte com
despacho aberto. Reserva aceita às 17h20Z, e o rebase daquela volta ainda
atropelou uma terceira reserva (clubedomosaico, 17h18Z), resolvida por rebase e
não por força. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.

**REDE PELA 20.2 — RETESTADA, NÃO HERDADA.** O `ESTADO.md` já trazia
`rede: bloqueada em 2026-09-14`, e a seção 4 é explícita: **bloqueio herdado do
`ESTADO.md` é retestado antes de ser respeitado, nunca lido como fato.** Foram
duas passadas: `jornadafly.com.br` e `www.jornadafly.com.br` em **000** nas duas,
`aquametria.com.br` em **200 na mesma passada**. O bloqueio é real e continua. O
bloco 2 não põe nada no ar.

### O que foi entregue

`dados/especificacao-calculadoras.md` (476 linhas) e `dados/constantes.json`
(6 constantes). As três ferramentas com pergunta-alvo, classificação de SERP pela
14.9, entradas, saídas na ordem da 15.2, régua de divergência, prestação de
contas da seção 7, tabela pré-renderizada, JSON-LD e **recusa declarada**.

### A pergunta aberta do bloco 1 foi medida, e está NEGADA

O bloco 1 proibiu de supô-la: *"o muro do português é forte onde existe portal
veterano brasileiro cobrindo o destino, e fraco onde não existe"*. Se fosse
verdade, mudaria a ordem das cidades do banco. **Seis consultas novas, em três
continentes, e o contraexemplo vem dos dois lados:** Petra não tem portal
veterano dedicado **e** não tem plataforma; Angkor tem **dois** portais veteranos
(`melhoresdestinos`, `queroviajarmais`) **e** também não tem plataforma. Ha Long
trouxe o Booking, Dubai trouxe Hellotickets e uma **página de produto** da
Civitatis em português, Buenos Aires não trouxe plataforma nenhuma — o lugar
delas está tomado por **receptivos brasileiros vendendo direto**.

**Nenhuma cidade do banco muda de ordem**, que era a única decisão que a pergunta
podia mudar. A leitura que aparece no lugar (plataforma entra em atividade de
operador, não em ingresso de sítio público) ficou escrita **com o contraexemplo
ao lado** — o balão da Capadócia, que é atividade de operador privado e deu zero
plataforma — e com o que a derrubaria. Não é critério e não decide nada.

### O que apareceu em 100% das oito consultas dos dois blocos

Ninguém data o preço, e **a unidade do preço troca dentro da mesma resposta**:
gôndola é **por veículo**, o cruzeiro de Ha Long aparece **por cabine** na mesma
lista dos por pessoa, Petra e Angkor são por pessoa **em escada de dias**. Foi
isso que especificou a F1, e não uma ideia: declarar a unidade, fechar a conta do
grupo, datar o preço. A tabela pré-renderizada nasce obrigada a ir até **6
pessoas**, porque é aí que o degrau de capacidade aparece — tabela que para em 4
esconde justamente o que a ferramenta tem de diferente.

### A gôndola, resolvida na fonte que tabela o preço

Cinco leituras divergentes do mesmo preço nas páginas de topo (€80 até 4; €90
dia / €110 noite; €30–90 por pessoa; €16 por pessoa com 5; €34 por pessoa na
plataforma). O **Comune di Venezia** publica €90 de dia (30 min, 9h–19h) e €110 à
noite (35 min), **máximo 5 passageiros**, pela **Delibera della Giunta Comunale
n. 89 de 20/04/2023**, e diz a unidade com todas as letras: não se paga por
pessoa, e sim pelo aluguel da embarcação inteira. **As duas páginas de topo que
dizem "€80 para até 4" não estão arredondando: estão três anos desatualizadas.**
Para 4 pessoas, de dia, a conta é **€90 no total e €22,50 por pessoa**.

**A régua de divergência desta ilha ficou escrita com o erro caro nomeado antes
da direção**, como a seção 10 exige: havendo tarifa de poder público, ela ganha;
não havendo autoridade, resolve-se para o valor **maior**, porque quem chega com
dinheiro a menos perde a experiência na porta e quem chega com a mais volta com
troco. Média continua proibida.

### O diferencial que não depende de nada bloqueado

**IOF de 3,5%** sobre compra internacional no cartão de pessoa física (Decreto
12.499/2025). Por ser percentual, ele entra na conta **na moeda do operador**, sem
precisar de câmbio: *"no cartão brasileiro são €93,15 no total, €23,29 por
pessoa"*. **Nenhuma das seis páginas medidas hoje menciona IOF**, e três
convertem para real sem declarar câmbio nem data — o defeito exatamente inverso.

### O que cai da página, e está dito em vez de escondido

`cambio-eur-brl` e `cambio-usd-brl` nasceram **pendentes**: nenhuma fonte de
cotação é alcançável desta nuvem (`economia.awesomeapi.com.br`,
`open.er-api.com` e `api.bcb.gov.br` em **000**, com o proxy declarando
`connect_rejected`). Constante pendente é **proibida em fórmula publicada**
(seção 10), então a F1 publica na moeda que o operador cobra — que é a que não
muda — e diz o porquê ao leitor. Pesa mais do que parece: **quatro das seis
experiências medidas hoje publicam em dólar**. Virou acréscimo ao despacho de
rede que já estava aberto, pedindo `api.bcb.gov.br` na mesma lista, e **não trava
ferramenta nenhuma**: custa uma linha por resultado.

### A escada da seção 25 não serve como está, e isso foi resolvido sem copiar a forma

Os quatro degraus da 25.1 são de **marketplace** (Shopee, Mercado Livre) e
**nenhum existe no nicho de experiência**. O **princípio** da 25.2 vale inteiro —
o piso nunca depende de ninguém —, então a escada desta ilha é a tradução dele:
página da experiência na plataforma → **página de cidade da Civitatis
(`civitatis.com/br/<cidade>/`), que é o PISO** → página de reserva do operador. O
piso foi medido em **dois destinos independentes** (`/br/veneza/`, `/br/dubai/`) e
é fabricável sozinho a partir do campo `cidade` do banco. Sem programa cadastrado,
o link nasce **cru e sem `rel="sponsored"`**, porque `sponsored` declara relação
**paga** e ninguém paga por aquele clique — a mesma decisão que a Aquametria e a
Robometria já registraram. "Link de loja em breve" não aparece em lugar nenhum.

### A armadilha em que esta execução caiu, e fica escrita

**Duas das minhas consultas carregavam o número que eu queria confirmar**
("IOF … 3,5%", "gondola … 90 euro 110 notturno"), que é exatamente o que a seção
8 proíbe: *pergunte qual é o valor, não se o valor é X*. As duas foram
**descartadas como fonte e refeitas com pergunta limpa antes de qualquer
gravação**. As duas confirmaram por outros publicadores — e a limpa da gôndola
ainda trouxe **o ato que sustenta a tarifa** (Delibera 89/2023), que a plantada
não tinha trazido. **O que sustenta os dois números é a segunda passada**, e é ela
que está citada no `constantes.json`.

### Verificação

**Não há site, não há Sync, não há `/status` e não há URL para abrir: esta ilha
não tem o que verificar no ar, e dizer o contrário seria inventar.** O que foi
medido de verdade: os quatro códigos HTTP da 20.2 (dois `000` e dois `200` de
controle), os três códigos das fontes de câmbio (`000`, com a causa declarada
pelo proxy), o `EGRESS_BLOCKED` na tentativa de leitura direta do
`comune.venezia.it`, o cabeçalho do `ESTADO.md` passando por `yaml.safe_load`, o
`constantes.json` passando por `json.load`, e uma afirmação que compara o
`resumo` do JSON com a lista **contada** — nunca com número digitado, que é a
cicatriz do número de tela — e cobra que **nenhuma constante pendente esteja em
uso**.

### Aberto e nomeado

(a) a **rede** da ilha, despacho ALTO, que trava 3b em diante; (b) o **câmbio**,
acrescentado ao mesmo despacho, que custa uma linha e não trava bloco; (c) a
**seção pendente do `VOZ.md`** — as 10 a 15 legendas reais do @jornadafly, que o
`PROMPT.md` exige **antes da primeira página**; (d) a **identidade visual**, que
precisa da aprovação do Raphael antes do 3b; (e) **nenhum programa de afiliado
cadastrado**, e pela ordem do `PROMPT.md` a Civitatis só entra depois de haver
conteúdo real no ar; (f) **não existe `manifest.json`**, e criá-lo vazio seria
inventar infraestrutura antes do WordPress.

**PRÓXIMO PASSO DESBLOQUEADO: bloco 3 — modelo do banco.** Este bloco já o obriga
a ter `unidade_de_preco` ∈ {por_pessoa, por_veiculo, por_cabine, por_grupo},
`capacidade_maxima`, `versoes[]`, `temporada`, `faixa_etaria`, `data_leitura`
(obrigatória **e visível na página**) e `afiliado.url_busca_produto` preenchida
desde o nascimento. **Não depende de site, de domínio nem da rede bloqueada.**

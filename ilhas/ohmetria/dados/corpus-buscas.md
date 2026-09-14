---
titulo: Levantamento de buscas paramétricas — Ohmetria
bloco: 1
gerado_em: 2026-09-14
publicar: false
---

# Corpus de buscas — Ohmetria

Bloco 1 da fila. Consultas reais em pt-BR do recorte **casar impedância, RMS,
litragem e bitola**, separadas nos três eixos que o `PROMPT.md` manda não
misturar, com procedência marcada consulta a consulta. Coletado por busca web em
**14/09/2026**, entre 17h20Z e 17h45Z.

## Método, e o que este arquivo NÃO tem

- **Não houve acesso a ferramenta de volume de busca** (Keyword Planner,
  Ubersuggest, Semrush). Portanto **nenhum número de volume mensal aparece
  aqui** — mesma disciplina do corpus da Robometria e do da JornadaFly. O que
  existe de métrica é **variedade de formulação**, **recorrência de domínio
  entre consultas independentes** e, nesta ilha, uma terceira que as outras duas
  não tinham: **o desacordo numérico entre as páginas que hoje ocupam a SERP**.
- **Procedência de cada linha** = os domínios que de fato responderam àquela
  consulta na medição de 14/09. Quando a linha cita um número, ele é **o número
  que aquele domínio publicou**, nunca um número desta ilha.
- **NENHUM número deste arquivo entra no banco nem em constante de calculadora.**
  O banco da Ohmetria só aceita valor lido em documento do fabricante, com
  `fonte_url`, `fonte_tipo` e `data_leitura` (blocos 2 e 3). Os números citados
  aqui servem a um propósito só: **medir o desacordo da SERP**, que é a vaga
  desta ilha. Tratar qualquer valor daqui como constante de engenharia seria o
  defeito mais grave que o `VOZ.md` nomeia — litragem absurda com cara de número
  exato.
- **A coleta foi por busca, não por leitura de página.** O egresso da nuvem
  recusa `curl` e WebFetch para todo domínio de terceiro (`EGRESS_BLOCKED` em
  `www.lojadesomautomotivo.com.br`, medido nesta execução) — a rede Personalizada
  libera os domínios das ilhas, `*.googleapis.com` e `github.com`, e nada mais.
  Portanto **toda URL citada aqui é URL que apareceu em resultado de busca**, com
  o título que a busca devolveu; nenhuma foi aberta. Isso é o que a seção 20.3 do
  contrato manda declarar: quem escreve a regra que exige a fonte confere se a
  fonte está liberada. **Consequência para o bloco 3:** a carga do banco vai
  precisar de leitura de PDF de fabricante, e hoje ela está fora do alcance da
  nuvem. Está registrado como o que falta, não como resolvido.

---

## EIXO A — CASAMENTO DE CARGA

O eixo âncora. É onde a **F1** mora. O dossiê já mediu
`qual modulo para 2 subwoofer de 2 ohms` (rodada 004) e **este arquivo não
repete aquela medição** — mede o que ela deixou em aberto.

### Cluster A1 — a família "qual módulo usar para X de N RMS"

O dossiê tinha **um** exemplo de URL por faixa de RMS
(`/qual-modulo-usar/subwoofer/400-rms.html`) e disse que ninguém constrói isso
sem busca própria em cada variação. **A família foi mapeada e ela tem DOIS
eixos, não um.**

| Consulta | Procedência medida em 14/09/2026 |
|---|---|
| `quantos rms de modulo para alto falante de 200w rms` (**a que o dossiê marcou como não medida**) | `lojadesomautomotivo.com.br` → `/comprar/qual-modulo-usar/woofer/200-rms.html`, título *"QUAL MÓDULO USAR PARA WOOFER 200 RMS? Veja exemplos."* · `blog.mundomax.com.br` · `somautomotivobr.com.br` (dois artigos distintos) · `magnumfalantes.com.br` · `clubedohardware.com.br` (**fórum**) |
| `qual modulo usar para woofer 400 rms` | `lojadesomautomotivo.com.br` → `/woofer/400-rms.html` **e** `/subwoofer/400-rms.html` na mesma página de resultados · `somautomotivobr.com.br` · `blog.mundomax.com.br` · `tiktok.com/@aprenda.somautomotivo` |
| `qual módulo usar para subwoofer 600w rms 2 ohms` | `lojadesomautomotivo.com.br` → `/woofer/600-rms.html` · `blog.mundomax.com.br` · `s2magazine.com.br` (ficha de produto) · `abellcar.com.br` (ficha) · **`kwai.com/discover/qual-módulo-usar-para-subwoofer-600w-rms`** |
| `qual módulo usar para subwoofer 1200 rms 2 ohms` | `lojadesomautomotivo.com.br` → `/woofer/1200-rms.html`, `/subwoofer/1000-rms.html`, `/subwoofer/2000-rms.html` · `somautomotivobr.com.br` · `blog.mundomax.com.br` |

**Achado A1-a — a família é `{woofer, subwoofer} × faixa de RMS`, e sete URLs
dela foram vistas.** `woofer/200`, `woofer/400`, `woofer/600`, `woofer/1200`,
`subwoofer/400`, `subwoofer/1000`, `subwoofer/2000`, mais as duas páginas-mãe
`/qual-modulo-usar/woofer.html` e `/qual-modulo-usar/subwoofer.html`. O
`somautomotivobr` mantém uma página que cobre **cinco tipos** no mesmo endereço
(*"Qual módulo usar Alto Falante | Subwoofer Woofer Driver Tweeter Escolher
rms"*). **A hipótese do dossiê está confirmada e ampliada:** a variação por
faixa tem busca própria, e o tipo de alto-falante é um segundo eixo com busca
própria também. Isto é planta de malha para o bloco **5b**, medida e não
suposta.

**Achado A1-b — E ISTO É A VAGA DA F1: as páginas que ocupam a consulta
DISCORDAM da regra central, e nenhuma declara o critério.** Na mesma medição de
14/09, para a mesma pergunta:

| Regra publicada | Quem publicou | O que ela dá para um falante de 200 W RMS |
|---|---|---|
| "até **100%** do valor em RMS no módulo — maior desempenho e melhor custo-benefício" | `lojadesomautomotivo.com.br` | 200 W |
| "pode-se usar o **dobro** da potência do alto-falante" (título literal: *"Dobro de rms Módulo"*) | `somautomotivobr.com.br` | 400 W |
| "**150 a 250 W RMS** a 4 Ω, para um sub de 200 W RMS" | `blog.mundomax.com.br` | 150–250 W |

O intervalo entre o menor e o maior número publicado para a **mesma** pergunta é
de **150 a 400 W — 2,7 vezes**. E o mesmo `mundomax` publica, para um sub de
**500** W RMS a 2 Ω, a faixa **300–600 W**: o multiplicador dele muda de
`0,75–1,25×` para `0,6–1,2×` entre dois exemplos da mesma página, sem que a
página diga por quê. **Nenhuma das três diz de onde a regra sai** — não há
folga térmica declarada, não há critério de clipping, não há fonte de
fabricante. É a mesma família do que a Aquametria achou nas réguas de lotação e
do que a JornadaFly achou nos preços de Veneza: **o topo da SERP discorda de si
mesmo sobre o número, e ninguém resolve para o caso de quem lê.**

### Cluster A2 — a associação em si, e o buraco que nenhuma prosa nomeia

| Consulta | Procedência medida em 14/09/2026 |
|---|---|
| `como ligar 2 subwoofer 2+2 ohms em 1 ohm associação paralelo` | `corsaclube.com.br` (**fórum**, mesmo tópico que o dossiê já tinha achado) · `somautomotivobr.com.br` (dois artigos) · `poweraltofalantes.webnode.page` · `youtube.com` · **`sac.taramps.com.br`, DOIS artigos**: *"Como fazer ligações em PARALELO — alto-falantes"* e *"Possíveis ligações de alto-falantes de bobina dupla (BD) em amplificadores Taramps de 1, 2 e 4 ohms"* |
| `qual módulo estabiliza em 1 ohm lista módulos 1 ohm taramps stetsom soundigital` | `lojadosomeacessorios.com.br` (**categoria de loja, filtrada por CANAL — "1 Canal Mono" — e não por impedância estável**) · `tiktok.com` · `youtube.com` · `facebook.com` · **`qualmelhorcomprar.com.br`** (uma das quatro fazendas nomeadas no dossiê) · `magazineluiza.com.br` |

**Achado A2-a — a Taramps publica a tabela de decisão de ligação, e ela é a
fonte da F1.** O artigo *"Possíveis ligações de alto-falantes de bobina dupla
(BD) em amplificadores Taramps de 1, 2 e 4 ohms"* é exatamente o que o
`PROMPT.md` diz ser o diferencial desta marca: **tabela de decisão pronta, não
só ficha**. Ela entra no bloco 2 como fonte do eixo A, do mesmo jeito que a
tabela de bitola do SAC entra como fonte do eixo C. **Não foi lida** — o egresso
está fechado para o domínio; foi vista em resultado de busca, com o título
acima.

**Achado A2-b — a consulta-âncora tem um caso em que a resposta certa é "não
fecha", e NENHUMA página da SERP o nomeia.** Dois subwoofers de bobina dupla
2+2 Ω chegam, em ligação simétrica, a **0,5 Ω** (as quatro bobinas em paralelo),
**2 Ω** (bobinas de cada sub em série, os dois subs em paralelo) e **8 Ω** (tudo
em série). **1 Ω não está no conjunto.** A pessoa que digita a consulta-âncora
com esse par de subs e um módulo de 1 Ω está pedindo uma coisa que não existe — e
as páginas medidas respondem com prosa de "calcule a impedância" ou com a
fórmula `impedância ÷ número de alto-falantes`, que sozinha produz 0,5 Ω e não
avisa nada. **O veredito "não fecha, e o mais perto que dá é 2 Ω" é
exatamente o que o `VOZ.md` manda pôr na primeira linha, e é o que ninguém
publica.**

**Achado A2-c — não existe, em pt-BR, lista de módulos filtrável por impedância
estável.** A busca por isso devolve categoria de loja organizada por **número de
canais**, vídeo de comparação de marca e uma fazenda. Módulo mono não é sinônimo
de módulo que estabiliza em 1 Ω, e a loja não oferece esse filtro. **É a metade
da F1 que nenhum concorrente tem**, e ela depende do banco de MÓDULOS do bloco 3
(`impedancias_estaveis[]`, `rms_por_impedancia{}`).

### Achado que CORRIGE o dossiê — a calculadora de impedância JÁ EXISTE no Brasil

O dossiê da rodada 004 escreveu *"uma única calculadora em toda a varredura:
`infinitysom.com.br`"*. **Isso é verdadeiro para as consultas que ele mediu e
falso para o nicho.** Medido em 14/09 na consulta
`calculadora impedância associação alto falantes som automotivo ohms`:

- `nexxobox.com.br/calculadora-impedancia` e `nexxobox.com.br/calculadora-lei-de-ohm`
- `amantesdeamplificadores.com.br/calculadora-impedancia-alto-falante-online`
- `sombox.com.br/calculos/CalcuAltoPara.html` e `sombox.com.br/calcular-impedancia-de-alto-falantes-em-serie-e-paralelo/`
- `somaovivo.org` (artigo, não ferramenta — e é um dos dois domínios da
  interseção com áudio residencial que o dossiê já tinha nomeado)

**Por que isto CONFIRMA a tese em vez de derrubá-la, e a distinção é a linha que
a ilha inteira defende:** essas ferramentas fazem a **aritmética** — dadas as
impedâncias, devolvem o equivalente em série ou paralelo. Nenhuma faz a
**decisão**, que é cruzar o resultado contra um banco de módulos que estabilizam
naquela impedância com RMS compatível. E, o que decide a estratégia: **nenhuma
delas apareceu no top 10 da consulta-âncora medida pelo dossiê**
(`qual modulo para 2 subwoofer de 2 ohms`, três fóruns e prosa de loja). A
ferramenta existe e **não ocupa a pergunta que a pessoa digita**. É a mesma
forma do achado da JornadaFly sobre o ângulo "vale a pena": o diferencial não é
a existência da calculadora, é o **formato** — veredito, e o produto que fecha.

---

## EIXO B — DIMENSIONAMENTO DE CAIXA

Onde a **F2** mora. O dossiê já mediu
`qual litragem de caixa selada para subwoofer 12 polegadas` e achou dois
blogspots de 2009 e 2010 no top 10; **não repetido aqui.**

| Consulta | Procedência medida em 14/09/2026 |
|---|---|
| `quantos litros caixa dutada subwoofer 12 polegadas sintonia duto` | `blog.lojadesomautomotivo.com.br` · `somautomotivobr.com.br` (duas páginas, as duas com a faixa de RMS no título) · `carrostech.com.br` · **`sacpb.blogspot.com`, post de 2012** · **`zettaaudio.com.br` — PDF de projeto de caixa** · **`audioclassico.com/calculo_duto.php` — calculadora de duto brasileira** |
| `calculadora litragem caixa selada subwoofer online Vas Qts brasil` | `speakerboxlite.com/subwoofer-box-calculator` · `omnicalculator.com/pt` · `caixasdesom.com.br` · `autosom.net/artigos/box_design.htm` · `acusticateoria.com.br` (**duas URLs, e o domínio se apresenta como "Melhores Caixas De Som Bluetooth"**) · `youtube.com` (dois vídeos) |
| `volume bruto ou volume livre litragem caixa som automotivo desconto do alto falante` | **`hinor.com.br/blog` — *"Dica Hinor: o que é volume bruto e volume líquido?"*, do próprio fabricante** · `amantesdeamplificadores.com.br` · **`tudosobresom.blogspot.com` (2009), `soundportal.blogspot.com` (2012), `g85tempo.blogspot.com` (2012)** · `acusticateoria.com.br` |

**Achado B1 — o vácuo de manual do dossiê está confirmado e é mais fundo do que
ele mediu.** Somando as três consultas deste eixo, **cinco blogspots** de 2009,
2012 e 2012 aparecem em top 10, em consultas diferentes. Não é uma página velha
sobrevivendo: é a camada inteira de explicação do eixo B parada há mais de uma
década.

**Achado B2 — e ISTO é a trava que pode quebrar a F2: "litros" é três grandezas
diferentes, e as fontes não usam o mesmo nome.** Medido:

- `zettaaudio.com.br` publica um projeto com *"volume bruto 49 L, volume livre
  42 L, sintonia 41 Hz"*.
- `hinor.com.br` — **fabricante da lista de carga do bloco 3** — publica que
  *"40 litros brutos, com o duto e o subwoofer dentro, dão aproximadamente 32 a
  35 litros"*.
- As páginas de litragem recomendada em geral dizem só "litros".

A razão entre líquido e bruto nas duas fontes fica entre **0,80 e 0,88**. **A
trava 3 do `PROMPT.md` está em risco por causa disso:** ela manda validar a
fórmula da F2 contra a litragem que o fabricante recomenda, e **se a fórmula
devolver volume líquido e a recomendação for bruta, a validação acusa erro de
12 a 20% que não é erro de fórmula, é erro de unidade.** É a mesma família do
`Vas 672,3 cm³` que o `PROMPT.md` já tinha nomeado, só que mais perigosa, porque
os dois números são plausíveis e nenhum parece absurdo. **Consequência
obrigatória para o bloco 2:** o modelo do banco precisa de
`litragem_tipo: bruto | liquido | nao_declarado` ao lado de `litragem_l`, e a
F2 precisa dizer na tela qual dos dois ela está devolvendo. Sem isso a ilha
entrega número exato e errado — o pior defeito possível aqui.

**Achado B3 — nasce uma fonte de projeto que o `PROMPT.md` não listava:**
`zettaaudio.com.br` publica PDF de projeto de caixa por modelo, com volume,
duto e **frequência de sintonia**. Entra na fila de carga depois dos quatro
primeiros (Bomber, JBL/Selenium, Eros, Pioneer), na mesma prateleira de Triton,
Ultravox e Hinor. Como toda fonte deste eixo: **não foi lida**, foi vista em
resultado de busca.

**Achado B4 — aqui também existe calculadora, e o recorte se estreita do mesmo
jeito do eixo A.** `speakerboxlite.com`, `omnicalculator.com/pt` e
`audioclassico.com` calculam caixa e duto a partir de Thiele-Small. Só que
**nenhuma delas apareceu na consulta que o dossiê mediu em linguagem de pessoa**
(`qual litragem de caixa selada para subwoofer 12 polegadas`, onde o top 10 tem
blogspot de 2009 e anúncio de caixa pronta). As ferramentas ocupam a consulta de
quem **já sabe** que precisa de Vas e Qts; a SERP da pergunta de quem **não
sabe** continua com prosa velha. **E nenhuma delas resolve a entrada que a F2
declara:** o `PROMPT.md` manda aceitar **o modelo do sub** como entrada, e é aí
que o banco de Thiele-Small do bloco 3 vira a barreira que a fórmula sozinha não
é.

---

## EIXO C — INSTALAÇÃO ELÉTRICA

Onde a **F3** mora, a última da ordem obrigatória — a única que entra contra um
concorrente com ferramenta pronta (`infinitysom.com.br`). O dossiê já mediu
`que bitola de cabo para modulo 1000w som automotivo`; **não repetido aqui.**

| Consulta | Procedência medida em 14/09/2026 |
|---|---|
| `qual fusível usar módulo 2000w rms som automotivo amperagem` | `corsaclube.com.br` (**fórum**) · `somautomotivobr.com.br` (*"Qual Fusível Disjuntor usar? Calcular Amperes"*) · `webcarr.com` · `carangoautoparts.blogspot.com` (**2015**) · `amantesdeamplificadores.com.br` · `maxturbos.com.br` |
| `bitola de cabo 4 metros bateria porta-malas módulo 1000w rms mm2 queda de tensão` | `corsaclube.com.br` (**dois tópicos de fórum**) · `somautomotivobr.com.br` · `mdmax.com.br` · `preparados.com.br` (**fórum**) · `opaleirosdoparana.forumeiros.com` (**fórum**) · `neosolar.com.br/forum` (**fórum, e é de energia solar**) · **`guiaomelhor.com.br`** (fazenda nomeada) |
| `quantos farad de capacitor para 1000w rms som automotivo` | `somautomotivobr.com.br` · **`lojadesomautomotivo.com.br` — ficha do produto *"Mega Capacitor Taramps 0,3 Farad 1000w rms"*** · `brainly.com.br` · `eliteautogear.com` (em inglês) · `pt.accio.com` (duas URLs) |

**Achado C1 — TRÊS divisores diferentes para a mesma corrente, e é o desacordo
mais caro do arquipélago até aqui, porque dele saem o fusível E o cabo.** Para
um módulo de **2000 W RMS**, na mesma medição:

| Conta publicada | Quem publicou | Corrente |
|---|---|---|
| `W ÷ 12 V` | `webcarr.com` e outros | **167 A** |
| `W ÷ 12,6 V` | `mdmax.com.br` (exemplo com 300 W → 23,81 A) | **159 A** |
| `W ÷ 20` ("consumo musical") | `somautomotivobr.com.br` | **100 A** |

**A diferença entre a maior e a menor é de 67%**, e ela cai inteira no
dimensionamento: o fusível recomendado ("125% a 150% da corrente calculada") vai
de **125 A a 250 A** dependendo de qual página a pessoa abriu primeiro.
**Nenhuma das três declara o rendimento do módulo** — e é ele que faz a conta
ser outra: um classe D real puxa mais da bateria do que entrega no falante, então
`W ÷ V` subestima e `W ÷ 20` é regra de bolso sem premissa escrita. **A F3 tem
de dizer a premissa na tela**, e é isso que a separa da calculadora da
InfinitySom, que o dossiê manda superar em vez de imitar.

**Achado C2 — a distância, que é a variável da F3, NÃO está nas respostas.** A
consulta foi escrita com os três parâmetros que decidem (1000 W RMS, 4 metros,
queda de tensão) e o top 10 devolveu **cinco fóruns** — um deles de energia
solar —, um guia de loja e uma fazenda. As páginas falam que *"comprimento
influencia a queda"* e **nenhuma fecha a conta para um comprimento dado**. A
calculadora da InfinitySom, que o dossiê achou na consulta sem distância,
**não apareceu nesta**. É a vaga da F3 medida com precisão: não é "calcular
bitola", é **calcular bitola para a distância de ida e volta, com o fusível
junto**, que é exatamente onde o `PROMPT.md` diz que a do concorrente para.

**Achado C3 — o capacitor tem desacordo de 3,3×, e um dos dois números é do
próprio fabricante.** Para 1000 W RMS: a regra de bolso publicada é **1 farad
por 1000 W**, e a **ficha de produto da Taramps vendida na
`lojadesomautomotivo` se chama literalmente "Mega Capacitor 0,3 Farad 1000w
rms"**. O rótulo do fabricante e o guia que ensina a escolher discordam por
3,3 vezes na mesma página de resultados. **Não vira ferramenta agora** — o
capacitor é entidade do banco (bloco 3) e não tem ferramenta própria na fila —,
mas é matéria de artigo-âncora do bloco 5, e é o tipo de pergunta em que a ilha
pode dizer o que ninguém diz: **que a conta certa não é por potência, é por
quanto tempo o pico dura**, e que o número do rótulo e o da regra de bolso
respondem perguntas diferentes.

---

## O que este levantamento decide para os próximos blocos

1. **Bloco 2 (especificação) nasce com três obrigações que saíram daqui:**
   (a) a F1 declara o critério de casamento de RMS **com fonte**, porque o
   mercado publica de 100% a 200% sem dizer de onde tira; (b) a F1 tem de saber
   dizer **"não fecha"** e qual é a impedância mais próxima que fecha — o caso
   dos dois subs 2+2 com módulo de 1 Ω; (c) a F3 declara **o rendimento suposto
   e a distância de ida e volta** na tela, não no rodapé.
2. **Bloco 3 (modelo do banco) ganha dois campos que não estavam no
   `PROMPT.md`:** `litragem_tipo` (`bruto | liquido | nao_declarado`) ao lado de
   `litragem_l`, pelo achado B2; e, na entidade MÓDULO, a garantia de que
   `impedancias_estaveis[]` é o campo que responde a consulta A2-c, que hoje não
   tem resposta em lugar nenhum do pt-BR.
3. **Bloco 5b (malha) já tem planta medida:** `{woofer, subwoofer, driver,
   tweeter} × faixa de RMS`, com sete URLs do concorrente vistas como prova de
   que cada variação tem busca própria.
4. **O que ficou por medir, e está dito como o que falta:** o autocomplete e as
   "buscas relacionadas" do Google não foram lidos (o egresso não alcança), então
   a variedade de formulação aqui vem de resultado de busca, não de sugestão de
   digitação. E **nenhuma fonte de fabricante foi aberta** — a leitura dos PDFs
   de Thiele-Small que o bloco 3 exige está hoje fora do alcance da nuvem, e isso
   é problema do bloco 3, não deste.

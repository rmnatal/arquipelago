# DOSSIÊ — SOM AUTOMOTIVO — 1º da fila, rodadas 004 e 005 (14/09/2026)

Nome proposto: **OHMETRIA** · domínio: **ohmetria.com.br** · molde de casca: **FERRAMENTA** · índice **4,00**

---

## ATUALIZAÇÃO DA RODADA 005 — 14/09/2026 — quatro portões fecharam

**1. O DOMÍNIO ESTÁ LIVRE, confirmado na fonte.** `registro.br/v2/ajax/avail/raw/ohmetria.com.br` devolveu
`{"status":0,"fqdn":"ohmetria.com.br","fqdnace":"","exempt":false}`. **`status: 0` = livre.** A pendência P5 da rodada 004
está fechada — o filtro de DNS deixou de ser a única evidência. **O nome está pronto para ser pago.**

**2. V MEDIDO POR FERRAMENTA, como a seção 3.1 do `BUSSOLA.md` passou a exigir.** O dossiê da 004 dava V=5 ao nicho
inteiro apoiado nos manuais da **Taramps**, que são de **módulo** — não provavam nada sobre a ferramenta de caixa. Medido
agora, uma por uma:

| ferramenta | o número que ela precisa | quem publica | V |
|---|---|---|---|
| **F1** — casa o módulo com o falante | RMS por impedância estável | **Taramps**, manual PDF por modelo no domínio oficial (`MN_012477_R03_HD-3000_V2_SITE.pdf`: "3000W RMS — 1 OHM 2 OHMS 4 OHMS"); Soundigital e JBL Selenium publicam impedância de bobina e RMS na ficha | **5** |
| **F2** — litragem da caixa | Vas, Qts, Fs por alto-falante | **6 de 7 fabricantes publicam** — detalhe abaixo | **4** |
| **F3** — bitola do cabo | mm² por corrente e distância | **Taramps**, tabela oficial no SAC ("Technical Table: Power Cable Gauge for 12V Taramps Amplifiers") | **5** |

**Nenhuma das três entra no plano sem fonte — e as três têm.** A F2 leva 4 e não 5 porque a Oversound ficou em aberto e
porque o dado mora em PDF, não em ficha web.

**3. A F2 É CONSTRUÍVEL — 6 dos 7 fabricantes publicam Thiele-Small**, com valor lido em documento oficial:
- **Bomber** (o melhor material): Bicho Papão 12" 800W 4Ω → `Vas 31,50 L · Qts 0,50 · Fs 37 Hz · Xmax 13 mm · Sd 453 cm²`, **e ainda projetos de caixa de 37 a 66 L** em selada, duto circular, retangular e triangular
- **JBL/Selenium**: seção "PARÂMETROS DE THIELE-SMALL" por modelo — Bass 10SW17A → `Fs 35,8 · Qts 0,80 · Vas 41 L`; Matador 15SW21A com "CAIXAS ACÚSTICAS SUGERIDAS" (selada 55 L, dutada 65 mm × 19,5 cm)
- **Eros**: E-12 MB 2.2K → `Fs 57,36 · Qts 0,323 · Vas 29,61 L`. **Cuidado: os PDFs "Projeto-" NÃO trazem T-S — use os de especificação**
- **Ultravox**: Ultra 700+ 12" → `Fs 80 · Vas 22,34 L · Qts 0,77`, com nota de rastreabilidade (equipamento CLIO)
- **Hinor**: 12 EVO 550 4Ω → `Fs 82,96 · Vas 19,37 L · Qts 0,661`
- **Triton**: AK 6.1 → `Fs 80 · Qts 0,422 · Vas 10,31 L`
- **Pioneer BR**: **o único em HTML raspável** — TS-W3090BR → `Fs 37 · Qts 0,78 · Vas 46,5 L · Xmax 9,5 mm`, e já publica selada 35 L / dutada 35 ou 50 L com a medida do duto
- **Oversound**: **não verificado** — publica datasheet oficial por produto, mas em PDF sem camada de texto. Não é "não publica"; é "não foi lido". Abrir manualmente.

**Três regras que isso impõe à F2, e não são opcionais:**
- O formato dominante é **PDF**, não HTML. Montar o banco é extração por modelo, não scraping. Só a Pioneer entrega em página.
- **A extração automática erra, e erra feio.** Nos testes apareceram `Fs 4 Hz` num manual Hinor (fisicamente impossível) e `Vas 672,3 cm³` num JBL (unidade trocada). **O banco nasce com validação de faixa obrigatória — Fs 20 a 90 Hz, Vas 10 a 250 L, Qts 0,2 a 0,9 — e conferência manual por modelo.** Sem isso a ferramenta cospe litragem absurda com cara de número exato, que é o pior defeito possível nesta ilha.
- **Bomber e Pioneer já publicam a litragem recomendada.** É conjunto de validação de graça: a fórmula da F2 tem de bater com o que o fabricante recomenda, e onde não bater o erro é nosso. Serve também de conteúdo de reserva para modelo sem T-S encontrado.
- **Ordem de carga do banco: Bomber, JBL/Selenium, Eros e Pioneer primeiro.** Triton, Ultravox e Hinor na segunda leva. Oversound quando alguém abrir os PDFs.

**4. O ÍNDICE CAIU DE 4,23 PARA 4,00 — e não foi por nada que o nicho fez.** A rodada 005 descobriu que o M de toda a fila
estava ancorado na tabela da **Amazon Associados BR**, um programa que a seção 7 do `ARQUIPELAGO.md` **proíbe em todas as
ilhas** (o `BUSSOLA.md` já foi corrigido). A âncora passou a ser o piso publicado da **Shopee: 3%**, cookie de 7 dias por
último clique, lido em 14/09/2026. Para esta ilha: **ticket típico R$ 202 × 3% = R$ 6,06 por venda → M 1,65** (era 2,59
sobre os 8% da Amazon). **Som automotivo continua em 1º lugar nas duas réguas** — mudou o nível de todo mundo, não a
posição dele. **Mas o aviso do dossiê original fica mais duro, não menos: o ticket é a fraqueza desta ilha, e agora com
número pior.** A comissão extra de vendedor parceiro da Shopee (até 30%, acumulável) é o que pode reverter isso, **e ela
não é publicada por categoria** — medir isso no painel vale mais para esta ilha do que para qualquer outra da fila.

**5. "Áudio residencial" foi fundido neste nicho, e não pode virar ilha separada.** A rodada 005 mediu a interseção de
SERP: apenas 2 domínios em comum (`discabos.com.br`, `somaovivo.org`), **e os dois só na pergunta de cabo e bitola**. O
artigo da discabos que ranqueia no lado automotivo é, lido de perto, **residencial** — fala de "amplificador, home theater
ou multiroom" e não menciona carro em lugar nenhum. Ele vaza para cá porque **bitola por potência e casamento de
impedância são a mesma física** dos dois lados. Consequência prática: **a F3 e a F1 são a fronteira compartilhada**, e uma
ilha de áudio residencial canibalizaria exatamente as duas páginas mais fortes desta. Se um dia áudio residencial for
construído, é **como cluster dentro da Ohmetria**, nunca como domínio próprio.

---

## (a) Por que este nicho — dez linhas

1. **A SERP paramétrica está vazia e é medida, não suposta.** Três consultas, três fóruns brasileiros vivos no top 10, e dois blogspots de 2009 e 2010 ainda ranqueando em "litragem de caixa selada para subwoofer 12".
2. **As quatro fazendas conhecidas estão do outro lado da porta.** `buscamelhores`, `topavaliado`, `qualmelhorcomprar` e `guiaomelhor` ocupam o top 8 de "melhor módulo amplificador 2026" e **não tocaram em nenhuma das três paramétricas**. É exatamente o padrão que a Bússola procura: comercial tomada, paramétrica aberta.
3. **O usuário não consegue nem formular a dúvida sem número.** Ohm, RMS, litro e milímetro de bitola são a língua nativa do nicho. P = 5.
4. **O fabricante publica tabela de decisão pronta, não só ficha.** A Taramps mantém manual em PDF por modelo com RMS por impedância (`MN_012477_R03_HD-3000_V2_SITE.pdf`: "3000W RMS — 1 OHM 2 OHMS 4 OHMS") e uma **tabela oficial de bitola de cabo por amplificador** no SAC. V = 5. Nenhum dos outros nove candidatos da rodada tinha isso.
5. **Cobertura de afiliado 10 de 10**, com o Mercado Livre mantendo subcategoria própria (`/acessorios-veiculos/som-automotivo/`) e a Shopee cobrindo a faixa barata (cabo, alto-falante, módulo de entrada). A = 5.
6. **A demanda é alta e pulverizada.** Uma loja de nicho construiu **uma URL por parâmetro** (`/qual-modulo-usar/subwoofer/400-rms.html`, `/woofer.html`) — ninguém faz isso sem busca própria em cada variação. D = 5.
7. **Erro caro e irreversível.** Módulo de 2 ohms em sub de 4+4 queima; caixa com litragem errada estraga o grave. A pessoa procura antes de comprar, e procura com o número na mão.
8. **A recompra é por etapas, não por consumo.** Falante → módulo → cabo de bitola certa → capacitor porque o farol pisca → bobina queimada. R = 4.
9. **A fraqueza é o ticket, e ela está declarada:** R$ 202 no módulo típico (Soundigital SD400.4, dois espelhos de ML). **M = 2,59** — o mais baixo entre os quatro primeiros da fila. O índice 4,23 já é líquido disso.
10. **É a Robometria de novo, num nicho maior.** Mesma forma (compatibilidade peça × parâmetro), mesma prova (ficha de fabricante), e desta vez com fórum e blogspot de 2009 no lugar de fazenda.

**Notas:** S_par 5 · S_com 1 · S 4,40 · P 5 · D 5 · M 2,59 (R$ 16/venda, ticket R$ 202) · R 4 · A 5 · V 5
→ Facilidade 4,64 · Retorno 3,89 · **Índice 4,23**

**As duas SERPs, descritas:**
- **PARAMÉTRICA (a que decide, S_par 5).** Fórum em primeiro lugar em "qual módulo para 2 subwoofer de 2 ohms" (`corsaclube.com.br`), com `autoforum.com.br` e `forum.monzeiros.com` no mesmo top 10. Loja de nicho (`lojadesomautomotivo.com.br`) ocupando três posições com páginas que respondem em prosa, sem ferramenta. Blogspot de 2009 e de 2010 ainda posicionados em litragem de caixa. Uma única calculadora encontrada em toda a varredura: `infinitysom.com.br` (bitola de cabo) — **loja de nicho pequena, não grande varejista, e pela régua da seção 3 não zera o nicho**.
- **COMERCIAL (S_com 1).** `osmelhoresdosom`, `blog-vinisound`, `tecnocurioso`, `experimentebrasilia`, e então **`buscamelhores`, `topavaliado`, `qualmelhorcomprar` e `guiaomelhor`** — quatro fazendas da lista nomeada no top 8. Fechada, e não é onde a ilha vai jogar.

---

## (b) As 5 consultas paramétricas-alvo, com quem ocupa o top 10 hoje (14/09/2026)

**1. `qual modulo para 2 subwoofer de 2 ohms`** — *a consulta-âncora da ilha*
1. corsaclube.com.br — "Ligar um sub 2 + 2 Ohms em uma potencia 2 ohms" (**fórum**)
2. blog.mundomax.com.br — "Qual o Módulo de Potência certo para o meu Subwoofer"
3. lojadesomautomotivo.com.br — "QUAL MÓDULO USAR PARA SUBWOOFER? Veja exemplos"
4. autoforum.com.br — "Qual O Melhor Para Um Subwoofer? 2+2 Ohms Ou 4+4?" (**fórum**)
5. lojadesomautomotivo.com.br — "QUAL MÓDULO USAR PARA WOOFER?"
6. lojadesomautomotivo.com.br — "QUAL MÓDULO USAR PARA SUBWOOFER 400 RMS?"
7. somautomotivobr.com.br — "Como ligar Alto Falante no Módulo? 1 ohm 2 ohms 4 ohms 8 ohms"
8. forum.monzeiros.com — "sub 4ohms em modulo de 2 ohms pode?" (**fórum**)
9. poweraltofalantes.webnode.page — "Como ligar o Alto Falante no módulo Amplificador?"
→ **Nenhuma calcula. Todas explicam em prosa.** É a vaga da ferramenta.

**2. `qual litragem de caixa selada para subwoofer 12 polegadas`**
1. blog.lojadesomautomotivo.com.br — "Litragem Caixa Alto Falante Subwoofer Quake"
2. nandinsound.com.br (espelho ML) — anúncio de caixa com duto, R$ 169,99
3. carrostech.com.br — "Caixa de subwoofer para carro: selada, dutada e litros"
4. autoforum.com.br — "[PROJETO] Caixa selada sub 12 | 37 litros horizontal" (**fórum**)
5. **tudosobresom.blogspot.com — "Litragem de caixas de som", post de 2009**
6. wellbagagitos.com.br — "Caixa Box 12 47 Litros Som Extremo"
7. somautomotivobr.com.br — "Caixa para Alto Falante Woofer 12"
8. **extremepreparacoes.blogspot.com — "Litragem ideal da Caixa", post de 2010**
→ Dois blogspots com 16 e 17 anos no top 10. Vácuo de manual.

**3. `que bitola de cabo para modulo 1000w som automotivo`**
1. discabos.com.br — "Cabo ideal para caixa de som ou alto-falante"
2. corsaclube.com.br — "Qual a Bitola dos fios utilizados para Som automotivo" (**fórum**)
3. **sac.taramps.com.br — "Technical Table: Power Cable Gauge for 12V Taramps Amplifiers"** (tabela oficial do fabricante — é a nossa fonte, não o nosso concorrente)
4. somautomotivobr.com.br — "MÓDULO AMPLIFICADOR TARAMPS TA 1000"
5. somautomotivobr.com.br — "Qual bitola Fio/Cabo usar no Módulo Amplificador e Bateria?"
6. somautomotivobr.com.br — "Qual bitola de cabos/fios utilizar em alto falantes?"
7. autoforum.com.br — "Bitola De Cabos - Estão Super-dimensionando?" (**fórum**)
8. **infinitysom.com.br — "Calculadora de Bitola de Cabos de Alimentação"** ← o único concorrente com ferramenta; loja de nicho, não grande varejista
9. mdmax.com.br — "Guia de cabos para som automotivo"
→ **Entrar por aqui exige ser melhor que a InfinitySom, não apenas existir.** Ver o plano em (f).

**4. `quantos rms de modulo para alto falante de 200w rms`** — *variação da âncora, mesma família de páginas*
Não medida isoladamente na rodada 004; a família é a mesma da consulta 1 e da terceira URL da `lojadesomautomotivo`
(`/qual-modulo-usar/subwoofer/400-rms.html`), que existe justamente porque cada faixa de RMS tem busca própria.
**Marcado para medir antes do nascimento** — não vai ao dossiê como medida o que não foi medido.

**5. `melhor módulo amplificador som automotivo 2026`** — *a comercial, registrada só para saber onde NÃO jogar*
osmelhoresdosom.com.br · blog-vinisound.com.br · tecnocurioso.com.br · experimentebrasilia.com.br ·
**buscamelhores.com.br** · **topavaliado.com.br** · **qualmelhorcomprar.com.br** · **guiaomelhor.com.br**
→ Quatro fazendas nomeadas. **A ilha não disputa esta consulta na largada.**

---

## (c) Prova de cobertura de afiliado — 10 produtos que a ferramenta recomendaria e onde estão

Regra da seção 2: pelo menos 7 de 10 com porta de compra rastreável. **Resultado: 10 de 10.**
Verificação por busca em 14/09/2026 (o `curl` para ML e Shopee foi negado pelo proxy do ambiente — ver seção 0 da rodada 004).

| # | Produto que a ferramenta indicaria | Onde está | Preço visto em 14/09 |
|---|---|---|---|
| 1 | Módulo Taramps MD 1200.1 (1 ohm) | ML `/p/MLB23110053` | **R$ 710,43** |
| 2 | Módulo Taramps MD 1200.1 (4 ohms) | ML `/p/MLB26036585` | não visto |
| 3 | Módulo Taramps TS 400x4 | ML `/up/MLBU3007566863` · **Shopee `i.411060907.8732540788`** | não visto |
| 4 | Módulo Soundigital SD400.4 EVO | ML `/p/MLB21621303` | **R$ 202 / R$ 209** |
| 5 | Subwoofer JBL Selenium 12SW10A Matador 600W 4+4Ω | ML (lista dedicada) | não visto |
| 6 | Subwoofer JBL Selenium Flex 12SW26A 300W RMS | ML `/som-automotivo/...` | não visto |
| 7 | Subwoofer Bomber Bicho Papão 12" 600W 4+4Ω | ML (espelho `MLB-2199356455`) | **R$ 555,45** |
| 8 | Alto-falante Pioneer TS-A1676S 6" | ML (lista) · **Shopee (linha TS-A1688S/1687S)** | não visto |
| 9 | Caixa selada MDF 12" 30–35 L | ML `/p/MLB27482549` | não visto |
| 10 | Cabo de energia 8 mm para som automotivo | ML (lista) · **Shopee `i.338537944...`, `i.786522725...`** | não visto |
| + | Mega Capacitor 2.0 Farad | ML (categoria própria) | não visto |

**Ordem de programa (seção 7 do `ARQUIPELAGO.md`):** quando o produto existe nos dois, **o link é o da Shopee**; o Mercado
Livre entra onde a Shopee não tem — nunca pela comissão maior. Etiqueta do ML no formato sem hífen: `ohmetriaf1`, `ohmetriaf2`,
`ohmetriaf3` (uma por par ilha × ferramenta; as etiquetas ainda **não existem** na conta RMNATAL e precisam ser criadas).
`Sub_id 1` da Shopee = `ohmetria`; `Sub_id 2` = o código da ferramenta.

**Leitura honesta da cobertura:** é a melhor da rodada em largura, e a pior em ticket. O produto que a ferramenta
mais recomenda (módulo de 400 RMS) custa R$ 202. A regra da cesta de 7 dias da Shopee ajuda — quem compra módulo compra
cabo, fusível e capacitor na mesma sessão — **mas isso não foi medido e não entrou no M.** O M de 2,59 é o número sem favor.

---

## (d) Naming

**Restrição de ambiente, registrada:** `registro.br` **não foi alcançado** nesta rodada (403 CONNECT no proxy de saída).
O filtro abaixo é **DNS puro, que é negativo por natureza — ausência de DNS nunca prova que o domínio está livre**.
**A confirmação em `https://registro.br/v2/ajax/avail/raw/ohmetria.com.br` (`status: 0` = livre) é pré-requisito
obrigatório antes de qualquer pagamento** (pendência P5 da rodada 004).

### Os 40 candidatos e o filtro de DNS (14/09/2026)

**Família "unidade + metria" (a família do Arquipélago):** ohmetria · sommetria · rmsmetria · gravemetria · bassmetria · ohmetrica · sonometria
**Família "o número certo":** ohmcerto · somexato · ohmexato · somcalculado · modulocerto · rmscerto · bitolacerta · litragemcerta · graveexato · caixacerta
**Família "medir/dimensionar":** medidasom · sompormedida · somsobmedida · dimensionasom · somdimensionado · numerodosom · calculasom · ohmagem
**Família "encaixe/impedância":** ohmpar · parimpedancia · impedanciacerta · casadeohm · acertoohm · ohmdoseu · ohmfecha
**Outros testados:** ohmbase · sombase · ohmlab · ohmguia · somfechado · ohmzero · somzero · ohmfino · somdecerto

**Sem DNS (38 de 40):** todos acima **exceto** os dois abaixo.
**Com DNS, portanto OCUPADOS e descartados de saída:** `ohmlab.com.br` (200.160.2.95) · `caixacerta.com.br` (69.6.213.219)

### O nome escolhido, em duas linhas

**OHMETRIA** — porque o ohm é a unidade que a pessoa já digita ("sub 2 ohms", "módulo 1 ohm") e "metria" é a assinatura do
Arquipélago (Aquametria, Robometria): o nome diz, sem explicar, que aqui a impedância é **medida**, não adivinhada.
E porque cobre a ilha inteira sem prometer só uma peça — a mesma marca serve para ohm, RMS, litragem e bitola, que são
quatro contas do mesmo ofício.

### Os descartados que chegaram perto, com o motivo

- **`sonometria.com.br`** — som + metria, som bonito e disponível no DNS. **Descartado**: "sonometria" já significa medição de
  nível de ruído em higiene ocupacional e audiologia. A ilha entraria brigando por uma SERP de saúde ocupacional que não é a
  dela, **e encostaria em YMYL**, que é restrição permanente do Raphael (seção 1 do `BUSSOLA.md`).
- **`modulocerto.com.br`** — a mais legível de todas para o público. **Descartado por escopo**: nomeia o módulo e só o módulo.
  A ilha também responde litragem de caixa e bitola de cabo; o nome viraria uma promessa menor que o site já no primeiro mês.
- **`gravemetria.com.br`** — a mais evocativa. **Descartada**: colide de ouvido com "gravimetria" (medição de gravidade),
  que é palavra estabelecida em geofísica e em química analítica — ruído de marca de graça.
- **`somsobmedida.com.br`** — boa e humana. **Descartada**: diz "sob medida" (personalização, instalador, serviço), e a ilha
  não presta serviço nem instala nada. O nome prometeria o que ela não faz.

---

## (e) Identidade

**Regra obedecida (seção 5 do `BUSSOLA.md`):** o símbolo nasce do **gesto técnico** — aqui, *fechar o circuito na impedância
certa* —, nunca de animal, produto ou mascote. **Não há carro, alto-falante, onda sonora, nota musical nem fone.**

### Conceito do símbolo
**Dois arcos espelhados que se aproximam e travam num traço vertical curto.** É o gesto de casar duas bobinas numa carga só:
dois caminhos que viram um. Lido de longe, o conjunto tem a silhueta de uma ferradura fechada — parentesco visual com o ohm
sem ser o glifo Ω, que seria notação emprestada e não desenho próprio. O traço vertical no encontro é o **ponto de medida**:
é ele que muda de cor quando a ferramenta dá o veredito. Traço uniforme de 2 px na grade de 24, cantos retos, sem gradiente,
sem sombra. Funciona em 16 px (favicon) porque o vão entre os arcos nunca fecha abaixo de 3 px.

**Assinatura da marca:** `OHM` em peso 700 + `ETRIA` em peso 400, coladas, sem espaço, tudo em caixa alta. Nunca no mesmo peso,
nunca separadas, nunca inclinada. (Mesma gramática da Robometria, deliberadamente — é a assinatura da casa —, em outra
família tipográfica, porque duas ilhas com o mesmo molde precisam parecer sites diferentes.)

### Cor — com contraste WCAG calculado, não estimado

| token | valor | onde | contraste medido |
|---|---|---|---|
| `--tinta` | `#101A24` | texto corrido, H1–H3 | **17,57:1** sobre `--superficie` · **15,80:1** sobre `--piso` |
| `--sinal` | `#B86E00` | marca, preenchimento, barra do veredito, botão. **Um uso forte por tela** | **3,99:1** sobre branco → **só preenchimento, ícone e texto grande (≥ 24 px); nunca texto corrido** · **4,41:1** sobre `--tinta` |
| `--sinal-texto` | `#8A5200` | o mesmo âmbar em versão de texto: link, rótulo, número em destaque | **6,39:1** sobre branco · **5,75:1** sobre `--piso` |
| `--piso` | `#F1F3F6` | fundo da página (cinza **frio** — a Robometria usa `#F2F1EF`, quente; é aqui que as duas se separam à primeira vista) | — |
| `--superficie` | `#FFFFFF` | cartão, tabela, caixa do resultado | — |
| `--traco` | `#D5DBE3` | borda de 1 px, divisor (1,39:1 — decorativo, **nunca carrega informação sozinho**) | — |
| `--legenda` | `#5E6B7A` | fonte, data de leitura, unidade, código de modelo | **5,44:1** sobre branco · **4,89:1** sobre `--piso` |
| `--alerta` | `#B3261E` | ressalva técnica ("este módulo não estabiliza em 1 ohm") | **6,54:1** sobre branco |

Todos os pares de texto ficam **acima de 4,5:1**, como a seção 5 exige. Sem gradiente. Sem sombra colorida. O âmbar aparece
**uma vez por tela** e nunca como fundo de bloco grande. Fundo escuro (`--tinta`) só no rodapé.
**Nota de uso obrigatória:** `#B86E00` reprova em texto normal (3,99:1). Onde for texto, é `#8A5200`. Isso não é preferência,
é o portão.

### Tipografia — três famílias, uma monoespaçada
- **Títulos: Saira Condensed 700.** Condensada, com a verticalidade de escala de painel. Nada a ver com a Archivo da Robometria.
- **Texto: Public Sans 400/600.**
- **Número, unidade e código de modelo — ohm, W RMS, litro, mm², Hz: Roboto Mono 500 com `tabular-nums`.** Texto corrido nunca vai em Mono.
- Todas com `font-display: swap`. Três famílias é o teto (seção 22.4 do `ARQUIPELAGO.md`).

Escala (rem, base 16): `--t-xs .8125` · `--t-sm .9375` · `--t-base 1` · `--t-lg 1.25` · `--t-xl 1.75` · `--t-2xl 2.25`.
Corpo 1,0625 rem, altura de linha 1,6, medida máxima **68 caracteres**.
Espaço na escala de 4: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64`. Raio `--r-sm 4px` · `--r-md 8px`. Borda 1 px em `--traco`.
Sombra única: `0 1px 2px rgba(16,26,36,.07)`. A caixa do veredito não usa sombra: usa borda de 2 px em `--sinal`.

**Canvas de identidade:** não gerado nesta rodada (pendência P7 da rodada 004). A especificação em texto acima está completa
— paleta com hex e contraste calculado, tipografia e conceito do símbolo —, e o `logo.svg` está nesta pasta.

---

## (f) O plano da ilha

**Molde de casca: FERRAMENTA** (seção 15.3). A ferramenta principal é a home. A pessoa chega com o falante já comprado e
quer "fecha" ou "não fecha" em dois segundos.

### As 3 primeiras ferramentas, na ordem

**F1 — Casa o módulo com o seu alto-falante.** *(a de nascimento, com casca + sitemap em 48 h)*
Entrada: quantidade de falantes, impedância de cada um (2+2, 4+4, 1, 2, 4 Ω) e RMS de cada um. Saída: **impedância final da
associação** (série, paralelo, série-paralelo) e a lista de módulos do banco que **estabilizam naquela impedância com RMS
compatível**. Ataca a consulta-âncora, onde hoje há três fóruns e nenhuma ferramenta.
*Portão da seção 7 que esta ferramenta precisa respeitar desde o primeiro dia:* **todo módulo do banco é nomeado uma vez em
cada resposta** — ou na frase que o recomenda, ou numa linha que diz por que ficou fora ("o MD 1200.1 4 Ω não estabiliza em
1 Ω") — e **nenhum módulo entra no bloco de compra sem que a frase o nomeie**. A soma dos nomeados fecha o banco, e isso se
mede varrendo a entrada inteira contra o tamanho contado do banco, nunca contra um número digitado. Vale igual para a
**tabela pré-renderizada**, que é a metade que um modelo de linguagem lê sem preencher formulário.

**F2 — Litragem da caixa para o seu subwoofer.** Entrada: modelo do sub (ou Vas, Qts, Fs) e tipo de caixa (selada ou dutada).
Saída: litro interno recomendado, com faixa, e — na dutada — comprimento e diâmetro do duto para a frequência de sintonia.
Ataca a consulta onde dois blogspots de 2009 e 2010 ainda ranqueiam.

**F3 — Bitola do cabo de alimentação.** Entrada: RMS total do sistema, tensão e distância bateria → módulo.
Saída: mm² mínimo, fusível e queda de tensão. **É a única das três que entra contra um concorrente que já tem ferramenta**
(`infinitysom.com.br`). Entra depois, e só entra **melhor**: com a tabela oficial da Taramps citada como fonte datada, com
a distância de verdade (ida e volta) e com o fusível junto — que é onde a calculadora do concorrente para.

### O que vai no banco
Um registro por produto, com: `marca`, `modelo`, `tipo` (módulo / subwoofer / alto-falante / caixa / cabo / capacitor),
**`impedancias_estaveis[]`** e **`rms_por_impedancia{}`** (para módulo), **`impedancia_bobinas`**, `rms`, `vas_l`, `qts`, `fs_hz`
(para falante), `litragem_l` e `tipo_caixa` (para caixa), `secao_mm2` (para cabo), `fonte_url`, `fonte_tipo` (manual PDF do
fabricante / página oficial), **`data_leitura`**, e `afiliado.url` + `afiliado.programa` (`shopee | mercadolivre`).
**`afiliado.url` nasce presente e vazio** e a ilha reporta em todo bloco quantos itens esperam link (seção 7 — cicatriz da
Robometria). A primeira carga vem dos manuais PDF da Taramps e das fichas de JBL Selenium, Bomber, Soundigital e Pioneer.

### O que a casca precisa ter
Header claro, logo à esquerda, menu curto (**Ferramentas · Produtos · Guias**); resultado sempre acima da dobra; **bloco de
compra com link de afiliado ANTES da prova de procedência** (cicatriz da Robometria, seção 7), com o link de "fonte" discreto,
`rel="nofollow noopener"`, nunca botão; `rel="sponsored"` + `target="_blank" rel="noopener"` nos links de afiliado; aviso de
comissão visível; preço nunca cravado como atual (ou sem preço, ou com data de coleta); `<title>`, meta, canonical, JSON-LD e
sitemap são da casca — **nenhum plugin de SEO**; GA4 por snippet, medindo as referências de IA; favicon próprio e menu
hambúrguer dentro da casca, não como acabamento.

### O encaixe com a fila do nascimento
Domínio → domínio adicional no cPanel com raiz própria → nameservers → **Search Console por propriedade de domínio, antes do
WordPress** → WordPress limpo → os três plugins da lista fechada → snippet **"Ohmetria Sync"** com token novo → sitemap e a
primeira medição em `dados/indexacao.md` (um zero honesto). Tudo pela seção 11 do `ARQUIPELAGO.md`, sem atalho.

---

## (g) VOZ.md

Entregue como arquivo próprio nesta pasta: `bussola/dossies/som-automotivo/VOZ.md`. A Fundação copia para
`ilhas/ohmetria/VOZ.md` no dia do nascimento.

---

## O que o Raphael precisa saber antes de dizer sim

1. **O domínio não foi confirmado no registro.br** — só o filtro de DNS, que é negativo. Confirmar `status: 0` antes de pagar.
2. **O ticket é a fraqueza declarada** (R$ 202 típico, M 2,59). Este nicho ganha por volume de consulta e por cesta, não por venda cara.
3. **A F3 entra contra alguém que já tem ferramenta.** Está na ordem certa por isso: terceira, e só se for melhor.
4. **As etiquetas do Mercado Livre `ohmetriaf1/f2/f3` ainda não existem** na conta RMNATAL. Criar etiqueta funciona por script; **gerar o link, não** — o gerador tem reCAPTCHA e é trabalho dele (seção 7).

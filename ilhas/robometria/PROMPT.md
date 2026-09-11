# ILHA: ROBOMETRIA — robô aspirador

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: robô aspirador — **compatibilidade de peças e consumíveis** (qual filtro HEPA, escova lateral e mop servem em qual modelo) e **dimensionamento** (Pa de sucção por tipo de piso e pelo, autonomia por m²).
- Domínio: robometria.com.br, registrado em 09/09/2026. Segunda ilha do Arquipélago.
- Paleta: grafite `#16191D` (tinta) · varredura `#CC3311` (marca, **cor de sinal**: um uso por tela) · piso `#F2F1EF` (fundo) · superfície `#FFFFFF` · traço `#DFDCD6` · legenda `#6B6862` · alerta `#A26A00` (ressalva técnica — âmbar, nunca vermelho, porque vermelho é a marca).
- Tipografia: **Archivo** (títulos) · **IBM Plex Sans** (texto) · **IBM Plex Mono** (todo número, unidade e código de peça, com `tabular-nums`). Texto corrido nunca vai em Mono.
- Símbolo: **anel aberto + peça com lingueta que encaixa nele** — o assunto da ilha é o encaixe, então o símbolo é o encaixe. **Nunca um robô desenhado.** Anel: círculo de raio 15 em viewBox 48, traço 3, com corte de 50° à direita (`M37.59 17.66 A15 15 0 1 0 37.59 30.34`). Peça: `M41 16 h6 v16 h-6 v-4 h-3 v-8 h3 z`, preenchida na cor varredura — é o único vermelho da marca.
- Assinatura: `ROBO` em Archivo 700 + `METRIA` em Archivo 400, coladas, sem espaço. Nunca no mesmo peso, nunca separadas, nunca inclinada.
- Identidade aprovada pelo Raphael em 09/09/2026.

## O buraco que esta ilha existe para ocupar
A Bússola verificou em 07/09/2026: a busca **comercial** ("melhor robô aspirador") está tomada por fazendas (analisamelhor, melhores.com, melhorroboaspirador). A busca de **compatibilidade** está fragmentada entre páginas de peça de fabricante (Multilaser, iRobot, Positivo, Oster, Xiaomi) e **não existe nenhum comparador cross-marca**. É esse o eixo.

**Nunca ataque de frente a família "melhor robô aspirador 2026."** Ataque "qual filtro serve no meu robô X", "escova lateral compatível com Y", "quantos Pa preciso para pelo de cachorro", "qual robô para 80 m²".

## Endpoints desta ilha
- Sync: `https://robometria.com.br/?robometria_sync=lho9XAzCjAjHdXGHUEOQUMq1faJBN0vx&forcar=1`
- Status: `https://robometria.com.br/wp-json/robometria/v1/status`
- O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador (a copiar da Aquametria quando for preciso).
- Search Console: propriedade de domínio `sc-domain:robometria.com.br`, verificada. Sitemap `https://robometria.com.br/wp-sitemap.xml` enviado em 10/09/2026.
- **Quem aciona o Sync é a própria Fundação, por `curl`, ao fim de cada bloco publicável** (seção 4 do contrato; a nuvem alcança o site desde 10/09/2026). Commit sem Sync não está no ar.

## Memória a carregar
`/areas/projeto-robometria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada 003, que aprovou este nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz (prioridade máxima, antes de qualquer bloco novo)

Seção 15 nova no `ARQUIPELAGO.md` e `VOZ.md` novo nesta pasta. Primeiro bloco a partir de agora: **reescrever a home e o header de Robometria pelo molde FERRAMENTA e pela voz do `VOZ.md`** — título e primeiro parágrafo de cada página da home na linguagem da pessoa; número, fonte e data para a camada de prova (tabela, "como sabemos", JSON-LD). Não trocar URL, não mexer em estrutura de ferramenta que já funciona, não tocar em página posicionada além do texto (seção 12.1). Depois disso, cada página existente é reescrita na voz ao passar pela ronda. Critério de pronto: abrir a home e nenhum termo da lista "Proibidas" do `VOZ.md` aparecer em título ou primeiro parágrafo; registrar a revisão no ESTADO.md e acionar o Sync.

ATUALIZAÇÃO 11/09: junto com a reescrita da home e do header, aplicar a seção 16 do contrato (árvore de três níveis, breadcrumb com BreadcrumbList, cluster de interlinkagem mãe↔filhas↔irmãs, categoria só com ≥3 filhas): escrever `ARVORE.md` desta ilha, dar pai a toda página existente, publicar breadcrumb e "Veja também" — sem trocar URL de página que já tem impressão (seção 12.1); 301 para toda URL que mudar e sitemap reenviado.

ATUALIZAÇÃO 11/09 (Pauta): quando existir `pauta.md` nesta pasta (seção 17 do contrato), os guias entram na fila depois desta reescrita e da árvore, em levas por cluster; registrar no fecho de cada bloco quantos temas estão escritos / na fila / recusados.

## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 11/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O despacho de 10/09, logo abaixo, NÃO deve ser apagado:** o que resta nele é a metade humana (reenviar o sitemap no Search Console), que é do Raphael e não da Fundação.

**Nenhuma correção foi feita pela Sentinela nesta ronda.** Os dois defeitos achados moram em código de snippet PHP, e a regra 3 da seção 12 manda parar e despachar.

1. **NENHUMA das 9 páginas publicadas tem `<meta name="description">`.** Medido em 11/09/2026 às 14h40Z, no navegador, nas 9 URLs do `wp-sitemap.xml` (`/`, `/ferramentas/`, `/metodologia/`, `/sobre/`, `/divulgacao-de-afiliados/`, `/qual-peca-serve-no-meu-robo-aspirador/`, `/filtro-universal-de-robo-aspirador/`, `/quantos-pa-o-robo-aspirador-precisa/`, `/quantos-m2-o-robo-aspirador-limpa-por-carga/`): `document.querySelector('meta[name=description]')` devolve `null` nas nove, e as ÚNICAS metas servidas são `charset`, `viewport`, `robots`, `theme-color` e os dois `generator`. Também não há `og:title`, `og:description` nem `og:url` em nenhuma delas. **Diagnóstico, feito no código commitado:** `snippets/robometria-casca.php` imprime `<meta name="theme-color">` (perto da linha 478) e monta o JSON-LD `Organization + WebSite` com um campo `description` (perto da linha 496) — mas essa string vai só para o JSON-LD, nunca para uma tag `<meta>`; e `grep -l 'meta name="description"' snippets/*.php` não devolve arquivo nenhum. Como esta ilha não tem plugin de SEO por decisão de projeto, ninguém mais imprime essa tag. **Consequência de negócio:** a seção 12.1 chama a faixa de posição 4 a 10 de "trabalho de CTR (título, meta, schema)" — sem description, não existe o que ajustar, e o Google inventa o trecho do resultado. **Conserto:** na casca, na mesma função que já imprime `theme-color`, imprimir também `<meta name="description">` por página, com o texto vindo de um mapa slug → descrição, e junto `og:title`, `og:description`, `og:url` e `og:type`. O texto de cada ferramenta deve dizer o que ela responde, não o que ela é. **Pronto quando:** nas 9 URLs do sitemap, `<meta name="description">` existir, com 110 a 160 caracteres, texto DIFERENTE em cada uma das nove, e `og:title`/`og:description`/`og:url` presentes; conferido com o site no ar, não em bancada.

2. **O `<h1>` da raiz é a palavra "Início".** Medido na mesma ronda: em `https://robometria.com.br/`, `[...document.querySelectorAll('h1')].map(h=>h.textContent)` devolve `["Início"]`. É o H1 da página que disputa a marca, e ele não nomeia o que a ilha faz. **Não abra bloco novo para isto:** o DESPACHO DO RAPHAEL de 11/09 já manda reescrever a home e o header pelo molde FERRAMENTA e pela voz do `VOZ.md` — leve o H1 junto nessa reescrita. **Pronto quando:** o H1 da raiz nomear o assunto da ilha (compatibilidade de peça e dimensionamento de robô aspirador) em vez de "Início", e nenhum termo da lista "Proibidas" do `VOZ.md` aparecer nele.

**O QUE A RONDA MEDIU E APROVOU em 11/09/2026 — não refaça, e use como linha de base:**
- `/wp-json/robometria/v1/status` devolve **revisão 14**, igual à do `manifest.json`. As 9 URLs do sitemap devolvem 200 e abrem; nenhuma página órfã; todo link interno vivo.
- **Zero `&#038;` dentro de `<script>`** nas nove páginas (contado só dentro dos blocos de script, 15 a 17 por página).
- Corpo não começa por YAML; JSON-LD presente em todas (`Organization+WebSite`, mais `WebApplication+FAQPage` nas duas ferramentas e `Article+FAQPage` nos dois artigos); favicon próprio; botão de menu com `aria-expanded="false"` e `aria-controls="rbm-nav-lista"`; nenhuma imagem sem `alt`; nenhum `noindex` indevido; canonical em todas; **console sem mensagem**.
- **R2 executada com entrada real e o número conferido na mão:** 200 m², piso liso, sem animal, referência Electrolux ERB60 (166 m² por carga) → limiar 3.000 Pa (Mundo Conectado), menor limiar "até 1.500 Pa", **6 modelos**, e "200 m² exigem 2 ciclos: 200 minutos, mais 1 recarga" — bate com `dados/tabela-exemplos-r2.md` e com `ceil(200/166)=2`. Borda do `ceil` conferida nos dois lados: **166 m² → 1 ciclo** ("faz 166 m² em um ciclo só — 100 minutos"), **167 m² → 2 ciclos**, **332 m² → 2 ciclos**. Caso sem retomada conferido: 333 m² com ERB44 recusa publicar a conta e diz por quê.
- **R1 executada com entrada real:** `electrolux-erb44` com "todas as peças" e com "bateria" devolve, palavra por palavra e com os acentos no lugar, o que está em `dados/r1-referencia.json` — inclusive o kit sem composição transcrita e a recusa "não vamos supor", sem bloco de compra.
- **Os números da `/metodologia/` foram conferidos contra o banco, e batem:** a escada serve 47 de nível 3, 18 de nível 4 e 7 de nível 7, idêntico ao que `ferramentas/gerar-casca-fatos.py` recalcula hoje; e a seção de cobertura serve 15 modelos que respondem, 12 vazios e 116 de 168 combinações, idêntico a `dados/cobertura-r1.json`. O defeito latente nomeado no `ESTADO.md` (`robometria_casca_numeros()` lendo option de `publicar=false`) **continua latente e ainda não disparou** — os números no ar estão certos hoje.
- **Registro de receita (não é defeito, não conserte por conta disso):** a ilha está no ar com quatro páginas de conteúdo e **nenhum link de loja em nenhum cartão** — todo cartão diz "Link de loja em breve", nas duas ferramentas. Nenhum equivalente tem link, então não há caso de "topo sem link com equivalente que tem". Ilha viva sem porta de compra.
- **Achado de processo:** existia um `DESPACHO DA SENTINELA — 10/09/2026` neste arquivo, mas o cabeçalho do `ESTADO.md` estava com `ultima_ronda: null` — a ronda de 10/09 não gravou a data. A edição 2 deste despacho fecha isso.

## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 10/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O item 0 saiu daqui em 10/09/2026, cumprido** (a procedência era a única porta de compra da R1; virou a quinta decisão de desenho do bloco 4, abaixo). **Restou só a metade humana do item 1**, e ela não é da Fundação.

1. ~~**Os sitemaps respondem HTTP 404 com XML válido no corpo.**~~ **METADE DE CÓDIGO CUMPRIDA em 10/09/2026, 15h49Z** (casca 1.0.1, manifest revisão 9). A causa era a própria casca mandar "Hello world!" para a lixeira: sem nenhum post publicado, a consulta principal das rotas `index.php?sitemap=…` volta vazia e o `handle_404()` do núcleo carimba 404 antes de o XML sair. Consertado pelo filtro `pre_handle_404`, que só age em requisição de sitemap. **Medido no ar:** `wp-sitemap.xml` e `wp-sitemap-posts-page-1.xml` devolvem **200**, `/pagina-que-nao-existe-mesmo/` continua **404** (o conserto não vazou), e `wp-sitemap-posts-post-1.xml` segue 404 porque esta ilha não tem post nenhum — de propósito, e ele não está no índice.
   **FALTA A METADE HUMANA, e ela não é da Fundação:** reenviar o sitemap no Search Console (Sitemaps → enviar `https://robometria.com.br/wp-sitemap.xml`) para ele sair de "Não foi possível buscar". Exige o navegador do Raphael ou credencial de conta de serviço que este ambiente ainda não tem. **Enquanto isso não acontecer, nenhuma leva de malha (bloco 5b) nasce** — a rampa da seção 14 é inexecutável sem medição.

## FILA DE BLOCOS

**1. LEVANTAMENTO DE BUSCAS PARAMÉTRICAS.** Consultas reais do nicho no Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta a consulta (autocomplete, buscas relacionadas, fórum, YouTube). Grave em `dados/corpus-buscas.md`. Separe explicitamente o eixo de **compatibilidade** (peça × modelo) do de **dimensionamento** (Pa, m², autonomia). Não depende de site nem de domínio.

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. As duas ferramentas âncora prováveis: (a) localizador de peça compatível por modelo; (b) dimensionador de sucção e autonomia por área, tipo de piso e pelo. Saída é sempre **faixa com critério e fonte**, nunca número seco.

**3. MODELO DO BANCO.** Entidades: **MODELO DE ROBÔ** (marca, linha, Pa, autonomia em minutos, tipo de navegação, voltagem, base de autoesvaziamento sim/não) · **PEÇA** (tipo, código do fabricante, modelos compatíveis, vida útil declarada) · **MARCA**. O campo `imagem` entra desde já (seção 6 do `ARQUIPELAGO.md`) — a Aquametria descobriu tarde que o banco não tinha e travou a vitrine.

**3b. CASCA DO SITE — ENTREGUE em 10/09/2026** (`snippets/robometria-casca.php` v1.0.0,
manifest na revisão 7). Identidade sobre o tema ativo, logo SVG do encaixe, menu hambúrguer
acessível, favicon próprio, JSON-LD Organization + WebSite, e **cinco** páginas — início,
ferramentas, metodologia, sobre e divulgação de afiliados (esta última nasceu junto porque
o aviso de comissão precisa estar publicado antes do primeiro link, não depois).

**3b ENTREGUE E NO AR em 10/09/2026, 14h11 UTC.** Sync acionado pela nuvem: `/status` responde
**revisão 7**, snippet `robometria-casca` aplicado (#6), a home serve o título da ilha, o sitemap
de páginas lista início, ferramentas, metodologia, sobre e divulgação-de-afiliados, e o sitemap
de posts está vazio ("Hello world" saiu). Próximo bloco da fila é o 3c.

**Antes de mexer na casca, rode `php ferramentas/teste-casca.php .`** — 59 medições, sem
site e sem rede, e é a única verificação da seção 8 que esta ilha consegue executar sozinha
(a nuvem não alcança robometria.com.br). Ele confere o que a seção 8 pede e mais a
identidade: paleta fechada, nenhum gradiente, a varredura ausente do corpo porque é cor de
sinal, e **cada número da tela conferido contra o banco commitado** — quem expandir o banco
e não atualizar o instantâneo da casca vê o teste reprovar em vez de o site publicar número
que o repositório não sustenta. Na primeira rodada ele já pegou o nome da superglobal de
servidor escrito dentro de um *comentário*, que o ModSecurity casa do mesmo jeito e faria a
gravação falhar em silêncio no wp-admin.

**3c. EXPANDIR O BANCO — não depende de site.** O modelo já existe e o
`ferramentas/validar-banco.py` já reprova o que estiver fora do contrato; o que falta é
cobertura. **A urgência não é número de itens** (a seção 14.3 do `ARQUIPELAGO.md`
descartou meta redonda): é faixa descoberta. Produto novo entra com `afiliado.url`
presente e vazio, e a execução reporta quantos itens esperam link.

A primeira leva do 3c (09/09/2026) fechou as lacunas (c) e (d) da ordem original. A
**segunda leva (09/09/2026, 23h16Z) fechou a lacuna do `pa_declarado`**: de 2 para **11
modelos publicáveis**, em 3 marcas, de 1.400 a 10.000 Pa — a R2 deixou de sair vazia.

A **terceira leva (10/09/2026, 11h17Z) varreu a entrada da R1**, que nunca tinha sido
varrida, e o resultado **reordenou esta lista**. A medição está em
`dados/cobertura-r1.json` e se refaz sozinha com
`python3 ferramentas/cobertura-r1.py --gravar`. **A ordem que vale agora, da maior para a
menor:**

(a) **PEÇAS COM CÓDIGO DA XIAOMI E DA WAP — a urgência número 1, e ela só apareceu no
cruzamento das duas varreduras.** Esta linha estava em ÚLTIMO lugar até 10/09/2026.
Medido: das 28 entradas publicáveis, só **3** são atendidas pelas DUAS ferramentas da
ilha. A R2 atende 8 modelos (Xiaomi, WAP, PRA500) em que a R1 sai **vazia**; a R1 atende
12 (Electrolux, Multi) em que a R2 sai vazia. **O funil está partido na emenda:** a ilha
ganha a visita pela R2 ("quantos Pa para pelo de cachorro"), a pessoa compra, volta meses
depois procurando o filtro daquele robô — que é a consulta de maior intenção de compra do
nicho e a razão de a R1 existir — e recebe "não localizamos declaração do fabricante".
Este é também o único lado **coletável** da emenda: o lado simétrico (Pa da Electrolux e
da Multi) já foi medido como inexistente no mercado brasileiro.
(b) **FAIXA DESCOBERTA E CONCENTRAÇÃO DE MARCA na R2.** Medição em
`cobertura_de_faixa_r2`, dentro de `dados/modelos-robo.json`: acima de **6.000 Pa** só
existem 2 elegíveis (o portão da seção 9 pede 3), e **toda faixa acima de 3.000 Pa é 100%
Xiaomi** — inclusive a de pet, que é a que vende. Não se conserta afrouxando
elegibilidade: conserta-se achando Pa de **outra marca** nessa faixa. Continua sendo
trabalho de verdade; caiu para segundo porque (a) rende nas duas ferramentas de uma vez e
(b) só rende numa.
(c) **MANUAIS EM PDF DA WAP — a melhor porta de entrada para o NÍVEL 2 da escada de
fontes.** A WAP publica um manual por modelo em `mais.conteudo.wap.ind.br`, com revisão e
data no nome do arquivo. Hoje o domínio devolve `EGRESS_BLOCKED`; no dia em que abrir,
esses PDFs sobem o banco inteiro da marca de nível 3 para nível 2 de uma vez, trazem o Pa
dos modelos que a loja declara só como "três modos de sucção" **e**, pela varredura da
R1, são a chance de tirar W400, W1000 e W310 do vazio duplo. Toda a ilha está em nível 3
ou 4 — nenhuma fonte de nível 2 ainda.
(d) **pares (minutos, m²): a lacuna mudou de natureza e NÃO é mais coleta.** Ficou medido
que Xiaomi, WAP, Multi e Positivo **não declaram m² em canal nenhum** — só a Electrolux
declara. Não adianta procurar mais: o número não está publicado. A
`taxa-cobertura-m2-por-min` continua `pendente` e **proibida em fórmula**, e a recusa
virou conteúdo: a R2 mostra os minutos, diz que o fabricante não declara área e explica
por que não chuta.

(e) **A RECARGA DOS MODELOS QUE JÁ DECLARAM COBERTURA — o item de MENOR custo e
MAIOR retorno que a varredura da R2 encontrou, e ele não existia nesta lista até
11/09/2026.** Medido: a fórmula do tempo real da especificação precisa de TRÊS
números declarados — cobertura por carga, autonomia e recarga — e **nenhum dos 28
modelos publicáveis tem os três**. Os 5 da Electrolux declaram cobertura e
autonomia e calam a recarga; o Xiaomi S20 e o Positivo PRA2000 declaram recarga e
calam a cobertura. **Um campo, em cinco modelos de uma marca só, destrava a frase
que é a razão de a R2 existir** — "a sua casa fica pronta em X minutos" — e ela
hoje sai pela metade, dizendo que o total depende de um número que ninguém
publica. Não é lacuna de mercado como a dos m²: a recarga é dado de manual, e a
Electrolux publica manual.

**TODA a coleta acima depende de rede que hoje NÃO existe.** Medido em
11/09/2026: `mi.com.br`, `xiaomi.com.br`, `wap.ind.br` e
`mais.conteudo.wap.ind.br` devolvem `000` — só os domínios das ilhas respondem.
**Antes de escolher um alvo do 3c, teste a rede com `curl`.** Se ela continuar
fechada, o 3c inteiro está bloqueado e a fila cai para o trabalho de repositório
listado em "Específico desta ilha", que não depende de rede nenhuma.

**ANTES de colher qualquer coisa para o 3c, rode `python3 ferramentas/cobertura-r1.py` e
`ferramentas/validar-banco.py`.** As duas varreduras são o que separa "acrescentei um
item" de "tirei uma entrada do vazio" — e foi contando itens, em vez de varrer, que a
lacuna da R1 ficou escondida atrás de "33 pares declarados".

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase. **Não deixe retrofit para depois** — foi o que custou dias na Aquametria.

**4 e 4e — AS DUAS FERRAMENTAS ESTÃO NO AR.** A R1 desde 10/09/2026
(`snippets/robometria-r1.php`, v1.1.1) e a **R2 desde 11/09/2026**
(`snippets/robometria-r2.php` v1.0.0, manifest revisão 12, `/status` conferido),
em `https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/`. As cinco
decisões abaixo deixaram de ser opinião e viraram o jeito desta ilha — **ferramenta
nova nasce com elas, nunca com retrofit depois:**

1. **A resposta é servida pelo SERVIDOR.** Formulário GET para a própria página, resposta
   montada em PHP. Sem JavaScript a ferramenta funciona por completo, e cada consulta tem
   a resposta inteira no HTML servido. Não repita o desenho de calculadora que só calcula
   no navegador: para um modelo de linguagem, aquilo é um formulário vazio.
2. **A regra mora na implementação de referência, e o PHP não a reescreve.**
   `ferramentas/gerar-r1.py` importa `cobertura-r1.py`, deriva os fatos para
   `dados/r1-respostas.json` (que o Sync leva para uma option) e o snippet só escreve a
   frase, acentuada. `ferramentas/teste-r1.php` compara **as 188 frases** das duas
   implementações ignorando acento: elas batem por construção, não por sorte. **A R2 tem
   que ganhar a mesma dupla**, e a referência dela ainda não existe.
3. **O caso-âncora é escolhido por regra, nunca a dedo**, e sai no HTML sem clique nenhum
   — é ele que um modelo de linguagem lê como resposta.
4. **Consulta não vira URL indexável:** `?modelo=…` sai com `noindex,follow` e canônica
   para a página limpa (seção 14.1). Domínio novo não tem orçamento de rastreamento para
   centenas de combinações.
5. **A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA, e existe antes do link**
   (v1.1.0, 10/09/2026 — item 0 do despacho, hoje cumprido). A R1 estreou com um único
   link clicável por peça, e ele ia para a loja do fabricante: a página ficou impecável
   de procedência e perfeita para a Electrolux. Agora o bloco "Onde comprar estas peças"
   vem antes, com o aviso de comissão dentro dele; a procedência é link de texto "fonte"
   com `rel="nofollow noopener"`, nunca um botão e sem fundo no CSS; e o bloco **nasce
   mesmo sem link**, reservando o lugar com "Link de loja em breve" — esconder o bloco
   enquanto o cano de links enche devolveria a procedência ao papel de única porta
   clicável, que é exatamente o defeito. Quando não há o que recomendar, o bloco não
   lista **e a página diz por quê**. `teste-r1.php` mede os cinco pontos (seção 13 dele),
   e a R2 nasce com isso, não com retrofit.

**O QUE A R2 ACRESCENTOU À DECISÃO 2, e vale para toda ferramenta de entrada
contínua.** A entrada da R1 é uma lista fechada, então o gerador pré-calcula toda
resposta possível e o snippet vira um escritor de frases. A da R2 tem metragem
contínua de 10 a 400 m², e por isso o PHP **precisa** fazer aritmética. A regra
continua na referência e viaja como fato; a aritmética declarada o PHP faz, e a
prova de que faz igual é uma **GRADE** que o teste percorre inteira — 9 situações,
114 cartões, 200 casos de metragem. E a grade tem que incluir as **bordas**: a de
10 em 10 m² não pegava trocar `ceil` por `floor + 1`, porque 162 e 166 m² não têm
múltiplo terminado em zero. Grade que não cobre a borda é amostra com nome de grade.

**A RÉGUA DE UMA REGRA NÃO PODE MORAR NO SNIPPET SE QUEM A CONFERE É O TESTE.** A
R2 nasceu com uma função `atende( $pa, $limiar )` que respeitava o operador da
fonte, nunca era chamada na montagem da página, e só o teste chamava — para
conferir a lista que o snippet publica. Trocar o `>` por `>=` fazia as duas metades
errarem juntas e o teste passar, com um modelo que a fonte citada não cobre em
primeiro lugar numa lista de recomendação. A função saiu do snippet e a comparação
passou a ser escrita no teste, lida do operador que a fonte declara. **Função morta
num snippet publicado não é neutra: ela parece a regra, e um dia alguém a usa.**

**E o achado que só apareceu LENDO a resposta como um leitor lê:** a página se
contradizia na mesma tela, dizendo "a Electrolux declara o filtro X compatível com o
ERB60" e, na frase seguinte, "a Electrolux não vende o filtro avulso para este modelo".
"Não vende avulso" é afirmação sobre o catálogo inteiro do modelo — frase que só o
resultado inteiro sustenta não pode ser escrita olhando uma peça de cada vez. **A R2 tem
frases da mesma família** ("nenhum modelo atende a sua metragem"): escreva-as depois de
montar o resultado inteiro, não durante.

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**OS DOIS ESTÃO NO AR.** O da R2 desde 11/09/2026
(`snippets/robometria-a2.php` v1.0.0, manifest revisão 13):
`https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/`. Ele não
repete a ferramenta — a R2 calcula a casa da pessoa, o artigo conta o catálogo e
responde a pergunta anterior, de onde vem o número de m² que os sites publicam.

**A PROVA DE QUE A TESE É DERIVADA PASSOU A RODAR DENTRO DO TESTE, toda vez.** No
A1 as mutações foram feitas uma vez, à mão, por quem escreveu. No A2
(`teste-a2.php`) elas são parte do arquivo: seis bancos adulterados num
subprocesso, um por molde, exigindo que o texto troque de forma **e** que os
números de hoje sumam da tela. Ler a página de hoje só prova que ela está certa
hoje — e a decisão 1 abaixo é sobre amanhã. **Artigo novo nasce assim.**

**E o A1 publicava o FAQPage em ASCII.** "Nao. Nas 16 pecas de reposicao..." dentro
do JSON-LD, que é justamente o canal que a seção 5 do `ARQUIPELAGO.md` diz valer
tanto quanto ranquear. Corrigido em 11/09/2026 no `gerar-a1.py`, sem tocar no
snippet. **O banco é ASCII porque ele CITA fontes; o que a ilha ESCREVE sai
acentuado — e isso vale também para o que ela escreve dentro de marcação.**

**O DA R1 ESTÁ NO AR desde 10/09/2026** (`snippets/robometria-a1.php` v1.0.0, manifest
revisão 11): `https://robometria.com.br/filtro-universal-de-robo-aspirador/`. Ele fechou a
malha da R1 nos dois sentidos — duas listagens (home e hub), três irmãs, e a R1 v1.1.1
apontando de volta. **O artigo da R2 nasce junto com a R2, na mesma execução**, e herda as
três decisões que este bloco fixou:

1. **A tese do artigo é derivada, nunca digitada.** `ferramentas/gerar-a1.py` deriva os
   números do banco para `dados/a1-fatos.json`, e a frase de abertura tem DUAS formas,
   escolhidas pela contagem. Um artigo cuja tese é um número e que traz esse número dentro
   do HTML passa a mentir em silêncio no dia em que o banco cresce — e "em silêncio" é o
   ponto: ninguém relê artigo publicado.
2. **A DESCRIÇÃO DO JSON-LD E A RESPOSTA DO FAQPage SÃO PARTE DA TESE, não embrulho.** O
   defeito só apareceu ao plantar uma peça multimarca numa cópia do banco: a página visível
   se corrigia e o JSON-LD continuava afirmando o que deixara de valer. Numa ilha cuja seção
   5 diz que ser recomendado pela IA vale tanto quanto ranquear, **contradizer-se no canal
   que a IA lê é pior do que na tela**. Todo artigo novo deriva os três lugares juntos.
3. **O artigo não repete a ferramenta.** Sem formulário: a consulta é da ferramenta, e duas
   páginas respondendo a mesma coisa competem entre si no índice (seção 14.4).

**A PROVA DE QUE UMA TRAVA REPROVA É PARTE DO BLOCO.** As travas novas do `teste-a1.php`
foram medidas quebrando o banco de propósito numa cópia — números adulterados nos fatos e
uma peça multimarca plantada. Trava que nunca foi vista reprovando é trava não medida.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **WordPress, casca, AS DUAS ferramentas e OS DOIS artigos estão no ar desde 11/09/2026** (manifest revisão 13, 9 páginas no sitemap). Os blocos 1, 2, 3, 3b, 4, 4e e 5 estão feitos para os dois eixos da ilha.
- **ACHADO DE 11/09/2026, e ele é a MESMA família do defeito da escada — ainda não corrigido.** `robometria_casca_numeros()` lê `get_option('robometria_dados_cobertura-r1')` para atualizar os números da seção 4 da metodologia, mas **`cobertura-r1` tem `publicar: false` no manifest**. Ou seja: no site no ar aquele `get_option` nunca devolve nada e a página serve os números DIGITADOS no snippet, com a data digitada junto. Hoje eles por acaso batem com a medição (28 / 15 / 12 / 168 / 116, conferido nesta execução) — o defeito está latente, não disparado, e é exatamente assim que a escada ficou meses errada. **Conserto:** ou publicar `cobertura-r1`, ou derivar esses cinco números para `casca-fatos.json`, que já existe e já viaja. A segunda é mais barata e usa o cano que esta execução abriu.
- **O PRÓXIMO PASSO, e ele NÃO depende de rede:** as duas dívidas de dados acima foram fechadas em 11/09/2026. O próximo trabalho de repositório é o achado logo acima — derivar os cinco números da seção 4 da metodologia para `casca-fatos.json`, pelo mesmo cano que a escada passou a usar.
  **Só depois disso, e só se a rede abrir**, vem o 3c: teste com `curl` antes de escolher o alvo, e leia a ordem atualizada na fila (o item (e), a recarga dos modelos que já declaram cobertura, entrou em 11/09/2026 como o de menor custo e maior retorno).
  **A leva de malha (5b) continua travada** pela metade humana do despacho: o sitemap precisa ser reenviado no Search Console, e isso exige o navegador do Raphael.
- **Antes de mexer em qualquer snippet, rode os SEIS testes de bancada:** `php ferramentas/teste-casca.php .` (64 medições), `php ferramentas/teste-r1.php .` (90), `php ferramentas/teste-a1.php .` (53), `php ferramentas/teste-r2.php .` (86), `php ferramentas/teste-a2.php .` (62) e `php ferramentas/teste-acentuacao.php .` (16). Eles são a única verificação da seção 8 que roda sem depender do site. **O sexto é o único que varre a ENTRADA INTEIRA** — 72 estados, um processo por estado, via `ferramentas/varrer-corpo.php`: os outros medem o caso-âncora, e foi por isso que "Aspirador Robo" e "Versao A" ficaram invisíveis para cinco testes verdes. O segundo compara as 188 frases publicadas contra a implementação de referência; o terceiro **recalcula a tese do artigo em PHP, direto do banco, sem olhar para o que o gerador em Python escreveu** — duas contas independentes que batem são medição, uma conta sozinha é o que o autor achou.
- **A PORTA DE COMPRA TEM UM DONO SÓ, e ele é a casca.** `robometria_casca_porta_de_compra`, `robometria_casca_rotulo_da_loja`, `robometria_casca_fonte_link` e `robometria_casca_css_vitrine` valem para toda página desta ilha que recomenda item; a R1 delega para elas. Página nova que recomenda produto **chama estas funções**, nunca escreve as suas. Os pesos visuais do botão de compra e do link de procedência são regra do Arquipélago (seção 7), não estilo local: com uma cópia por página, bastaria alguém ajustar uma delas para a ilha voltar — numa página só, e sem ninguém notar — ao defeito de 10/09/2026.
- **Página nova entra no catálogo da casca pelo FILTRO dela**, `robometria_ferramentas` para ferramenta e `robometria_artigos` para artigo. A casca nunca ganha uma cópia da página dentro; é assim que a home e o hub listam qualquer coisa nova sem serem editados de novo, e é o que garante as duas listagens que a seção 9 exige.
- ~~**O BANCO ESTÁ EM ASCII, E AGORA ISSO APARECE NA TELA.**~~ **CUMPRIDO em 11/09/2026.** 121 strings restauradas nos nove campos que a varredura mediu chegando ao corpo servido, e a operação é **provada diacrítico-only**: reduzido a sem-diacrítico, o banco de hoje é byte a byte o de ontem (`dados/acentuacao-restaurada.json`, conferido linha a linha por `teste-acentuacao.php` com régua própria). **A restauração não é releitura:** o acento foi reposto pela ilha, não lido no fabricante — e é por isso que o livro-razão existe, como lista de conferência de quem reler os manuais quando a rede abrir.
  **Quem segura daqui para a frente é `ferramentas/teste-acentuacao.php`**, que lê o CORPO dos 72 estados e reprova qualquer palavra da régua. Palavra ambígua (o "e" que pode ser "é") ficou de fora do mapa de propósito: acertar por adivinhação não é acertar. **O que ficou de fora do escopo, e é trabalho de verdade:** `declarado_como`, `motivo_do_null` e `descricao_na_fonte` seguem em ASCII. Elas NÃO estão na tela hoje (medido), mas são prosa longa e chegam à tela no dia em que alguém as publicar — e aí o portão reprova, que é exatamente o desenho.
- **O KIT DECLARADO NÃO TEM PORTA DE COMPRA, E ISSO SE DESTRAVA POR DADO.** Na
  consulta ERB30 + filtro, a Electrolux declara um Kit Performance compatível com
  o modelo e a página não oferece compra dele: a composição do kit não foi
  transcrita, então a página não sabe se ele contém filtro, e vender kit debaixo
  de "qual filtro serve no meu robô" seria recomendar em primeiro lugar um
  produto que a própria página diz não saber se serve (seção 7). **Não afrouxe a
  regra: transcreva a composição dos kits na próxima leva do 3c** — o dado abre
  a porta de compra sozinho, e hoje são os kits que concentram o que a Electrolux
  declara para os modelos mais novos.
- ~~**UMA FONTE ESTÁ NO NÍVEL 2 E A ESCADA DIZ QUE O NÍVEL 2 NÃO EXISTE.**~~ **DECIDIDO em 11/09/2026: NÃO é nível 2. É nível 3.**
  **A regra, e ela vale para toda fonte de toda ilha desta pasta:** uma origem tem TRÊS elos — quem escreveu o documento, quem o guarda e como nós o lemos — e **o nível é o do elo MAIS FRACO**, nunca o do mais forte. O manual do ERB10/ERB11/ERB20 é escrito pela Electrolux (elo forte), mas está guardado por `manuals.plus` e chegou aqui por busca, sem leitura direta. Dois dos três elos são fracos.
  **A direção saiu da assimetria de custo (seção 10 do contrato), não do gosto:** errar para BAIXO custa uma frase mais fraca na tela ("a confirmar no manual"); errar para CIMA faz a página de metodologia declarar um rigor que a ilha não tem — e metodologia é a página cujo único produto é o rigor.
  **A medição decidiu sozinha:** as QUATRO únicas fontes de nível 2 do banco inteiro eram a mesma entrada de `manuals.plus`. Nível 2, neste banco, era inteiro custódia de terceiro — não um registro solto.
  **O que ficou mecânico, para a contradição não voltar:** (a) `validar-banco.py` passou a exigir que `origem` bata com a `origem` que a escada dá àquele `nivel` — era por aí que o defeito entrava, porque só o `nivel` era conferido; (b) nível 1 ou 2 agora exige o campo `leitura: "direta-na-fonte-primaria"` **declarado**, e silêncio nunca promove (adivinhar pelo texto do `canal_de_coleta` seria a heurística por vizinhança que a seção 8 proíbe); (c) a coluna "Temos hoje" da página **deixou de ser digitada e passou a ser contada** (`dados/casca-fatos.json`). As três foram testadas quebrando o banco de propósito e reprovam.
  **O caminho de volta ao nível 2 está escrito no registro:** reler o mesmo manual no endereço da Electrolux sobe o campo de 3 para 2 sem mudar mais nada.

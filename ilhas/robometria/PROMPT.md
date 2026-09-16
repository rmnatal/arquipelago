# ILHA: ROBOMETRIA — robô aspirador

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: robô aspirador — **compatibilidade de peças e consumíveis** (qual filtro HEPA, escova lateral e mop servem em qual modelo) e **dimensionamento** (Pa de sucção por tipo de piso e pelo, autonomia por m²).
- Domínio: robometria.com.br, registrado em 09/09/2026. Segunda ilha do Arquipélago.
- **Os tokens desta ilha moram em `DESIGN.md`, nesta mesma pasta** — é de lá que a casca renderiza. As linhas de paleta e tipografia abaixo continuam aqui como registro do que foi aprovado; se as duas discordarem, vale o `DESIGN.md` (seção 22.6).
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
- GA4: propriedade `553889920` na conta `Arquipélago` (`407777291`) · ID de medição **G-RM7KS75QP2** · fluxo "Robometria — site" (`15766206182`)

## Memória a carregar
`/areas/projeto-robometria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada 003, que aprovou este nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz

~~**Reescrever a home e o header pelo molde FERRAMENTA e pela voz do `VOZ.md`.**~~
**CUMPRIDO em 11/09/2026** — casca 1.2.0, manifest na revisão 15. A home virou a
ferramenta (promessa numa linha, o seletor da R1 chamado e servido no HTML,
atalhos por tipo de peça derivados do banco), a confissão numérica foi para a
metodologia (seção 15.2: número mora na camada de prova), o H1 da raiz deixou de
ser "Início" e o menu virou Peças · Sucção · Como conferimos. Nenhuma URL mudou.
Critério de pronto conferido na bancada, não de olho: `teste-casca.php` mede o
título da raiz e o primeiro parágrafo da home contra a lista de proibidas do
`VOZ.md`, por estrutura e nunca na página inteira.

**A árvore da seção 16 está CUMPRIDA em 11/09/2026** — casca 1.3.0, manifest na
revisão 16, `/status` conferido e as nove URLs abertas no ar às 19h47Z. Nasceu o
`ARVORE.md` desta ilha (quatro seções de nível 1, quatorze categorias de nível 2,
o lugar de cada página de hoje); trilha nas oito páginas que não são a home (16.3),
`BreadcrumbList` levando só os degraus com endereço de verdade, e blocos "Veja
também" com as irmãs derivadas mais a frase que linka a mãe com a contagem
contada. **Nenhuma URL nova**, que era a condição para caber agora. Critério de
pronto medido, não de olho: `ferramentas/teste-arvore.php` (213 afirmações, régua
própria, um processo `php` por página, e ele LÊ o `ARVORE.md` para cobrar que
documento e código digam a mesma coisa), 18 mutações deliberadas em
`ferramentas/mutacoes-arvore.py` — 18 reprovadas — e 258 medições em Chromium.

**As duas decisões que este despacho mandou tomar, tomadas** (o porquê está na
seção 2 do `ARVORE.md`): `/metodologia/` **fica na raiz**, porque a lista da 16.1
nomeia a família da página institucional e ela é dessa família; `/ferramentas/`
**fica hoje como mãe de transição** das duas ferramentas e sai com 301 para a home
no dia em que `/pecas/` e `/succao/` nascerem, porque aí ela passaria a servir a
mesma listagem que elas. O menu continua Peças · Sucção · Como conferimos: os três
rótulos do `VOZ.md` só entram quando as seções existirem como página.

**O que continua de pé desta seção, e trava até o Search Console:**
- **as quatro páginas de nível 1 e as quatorze de nível 2**, e a troca de pai e
  slug das existentes (com 301 para toda URL que mudar). São dezoito URLs novas, e
  esta ilha não publica leva de malha enquanto o sitemap não for reenviado — é a
  metade humana do despacho da Sentinela de 10/09, logo abaixo, e é do Raphael.
  Quando destravar, o nível 1 e o nível 2 da trilha e do `BreadcrumbList` viram
  link sozinhos: quem resolve o endereço é `robometria_casca_url_se_existir()`.
- **a frase de mãe dos dois guias** (16.4b), que só nasce junto com `/guias/`: hoje
  ela apontaria para página inexistente, e o portão cobra a ausência dela
  justamente para ninguém fechar isso com um endereço inventado.

**A VOZ CHEGOU ÀS NOVE PÁGINAS — CUMPRIDO em 11/09/2026**, casca 1.4.0, manifest
na revisão 17, `/status` conferido e as nove URLs medidas no ar às 21h48Z (65
afirmações, 0 falha). Fecha a 15.5 nesta ilha: as oito páginas que não são a home
ganharam abertura na voz do `VOZ.md` — nenhuma começa mais nomeando a própria
página ("Esta ferramenta responde…", "A Robometria é um banco de…") — e a
procedência desceu um parágrafo, para a camada de prova (`rbm-prova`), como manda
a 15.2. **Nenhuma URL mudou.**

E o achado que não estava no despacho: **seis das nove páginas tinham DOIS
NOMES**, porque o mapa das cabeças (1.2.0) trazia um título digitado ao lado do
da definição da página. O `og:title` dizia "Quem publica a Robometria" e o H1, na
mesma página, "Sobre". Agora o nome tem uma fonte só e as cinco superfícies
derivam dela, com portão próprio (`ferramentas/teste-voz.php`, 155 afirmações, um
processo por página). O `<title>` passou a ser escrito por este repositório: na
home ele vinha do campo de descrição curta do wp-admin, com 73 caracteres em
vocabulário de dentro da fábrica.

ATUALIZAÇÃO 11/09 (Pauta): quando existir `pauta.md` nesta pasta (seção 17 do contrato), os guias entram na fila depois da árvore, em levas por cluster; registrar no fecho de cada bloco quantos temas estão escritos / na fila / recusados.

## DESPACHO DA SENTINELA — 14/09/2026 (ronda diária, 14h32Z, no Chrome do Raphael)

**Isto tem prioridade sobre a fila (seções 18.1 e 18.5).** Aplique antes de qualquer bloco, verifique pela seção 8, registre no `REGISTRO.md` como "despacho da Sentinela de 14/09 — item N cumprido", e apague daqui o item cumprido **só depois de abrir a URL no ar e conferir o "pronto quando"** (18.4).

**RECONFERÊNCIA DO QUE A RONDA ANTERIOR DEIXOU (regra 19.4c).** Não existia `dados/consertos.md` nesta ilha — a ronda de 11/09 não consertou nada —, então não havia conserto a reconferir. O arquivo nasce nesta ronda, com zero conserto. **O que a ronda de 11/09 mediu e aprovou continua valendo e foi reconferido hoje sem defeito novo:** 9 de 9 URLs do sitemap em HTTP 200; zero `&#038;` dentro de `<script>`; JSON-LD em todas; favicon próprio; `aria-expanded`/`aria-controls` no botão de menu; nenhuma imagem sem `alt` (a ilha não serve imagem nenhuma hoje); canonical em todas; nenhum `noindex` indevido; corpo nunca começa por metadado YAML; **console sem uma mensagem sequer**; `/status` na **revisão 36**, igual à do `manifest.json`.

**O QUE MAIS PASSOU NESTA RONDA, para a Fundação não refazer** (medido por `fetch` + `DOMParser` no navegador, portanto no HTML servido e sem depender de render): trilha da 16.3 presente nas 8 páginas que não são a home e **ausente na home**, que é o certo; `BreadcrumbList` nas mesmas 8; bloco "Veja também" nas 4 páginas de conteúdo; **zero página órfã** — a URL com menos links internos de entrada tem 4, e o mínimo da 16.4f é 2; **nenhum alvo interno fora do sitemap** (zero link interno quebrado); **nenhuma palavra da lista "Proibidas" do `VOZ.md`** em `<title>` nem no primeiro parágrafo de nenhuma das 9. **R1 executada com entrada real:** `electrolux-erb44` + `bateria` devolve "não localizamos declaração do fabricante de bateria para este modelo; não vamos supor", sem bloco de compra — igual à linha de base de 11/09. **R2 executada com entrada real:** 200 m², piso liso, sem animal, referência `electrolux-erb60` devolve limiar de 3.000 Pa e **6 modelos** — igual à linha de base de 11/09.

**CORREÇÕES APLICADAS PELA SENTINELA NESTA RONDA: NENHUMA.** Os quatro achados abaixo caem todos na lista fechada 19.2 — camada de hospedagem, lógica de ferramenta e dado de banco —, e a 19.2 manda parar e despachar. Nenhum deles é da 19.1.

---

### 1. O CACHE DO HOSPEDEIRO — **CUMPRIDO, e a medição que faltava foi feita às 19h33Z de 14/09: a purga entrega em 166 s, e a régua que decidia isso era cega para texto**

**O que esta ronda achou está certo e era o topo de um defeito maior.** A causa não é "sem `gzip`": é **sem cabeçalho `Accept-Encoding` nenhum**. Medido nas mesmas URLs, em `/metodologia/`, às 15h20Z: `gzip` → página de hoje; `identity` → página de hoje; `br` → página de hoje; **nenhum cabeçalho → cópia de 11/09**. `curl -s` cru não manda o cabeçalho; navegador e Googlebot mandam. **As três ferramentas `conferir-*-no-ar.py` passaram a mandar `Accept-Encoding: identity`** — e a régua que mede a variante quebrada continua existindo, na seção 9 do `conferir-no-ar.py`, exatamente como esta ronda exigiu.

**E O QUE ESTAVA POR BAIXO É PIOR, E FOI CONSERTADO.** O cache tem assinatura no HTML servido: `<!--Generated by Endurance Page Cache-->`, o cache em arquivo do próprio hospedeiro. Ele purga quando um POST é salvo no wp-admin — e o Sync desta ilha **grava options e atualiza snippets, nunca passa por lá**. Medido nesta execução: a revisão 37 aplicou ("10 aplicado(s)"), o `/status` respondeu 37, as nove URLs deram 200 e os títulos bateram — **e o endereço canônico da página de compatibilidade continuou servindo a cópia das 14h40, sem um botão de compra e com a frase proibida em quatro cartões.** Com quebra de cache na URL, a página nova aparecia inteira. É a seção 4 do contrato uma camada abaixo: lá o Sync não era acionado; aqui ele é, o log diz aplicado, o `/status` confirma, e o leitor continua na página de antes.

A casca 1.6.1 passou a purgar o cache na gravação das options da ilha, e **nasceram duas réguas que não existiam**: a seção 10 do `conferir-no-ar.py` põe o endereço canônico contra o mesmo endereço com quebra de cache, e a seção 11 conta o piso da 25.2 no HTML servido. A falta delas é o que deixou esta mesma ferramenta aprovar a revisão 37 sobre uma página velha.

**A PURGA PEGOU, E O CAMINHO ATÉ ESSA CONCLUSÃO É A PARTE ÚTIL.** Duas estratégias foram ao ar: as ações de purga do plugin (revisão 39) e o esvaziamento da pasta `endurance-page-cache` (revisão 40). Medindo logo depois, o canônico continuava velho — e eu **retirei** a purga por arquivo na revisão 41, por achar que a camada estava à frente do Apache.

**A medição que me convenceu disso estava errada, e o erro tem nome:** os cabeçalhos vinham de um `curl -I` (HEAD) e o corpo de um GET feito segundos depois — **duas requisições, dois estados do cache** —, e o `no-store` sem `last-modified` que parecia provar "isto não é arquivo local" era o retrato de um arquivo sendo apagado naquele instante. Medidos juntos (`curl -D - -o /dev/null`), HEAD e GET concordam. **Fica a regra de método, e ela vale para toda ilha: cabeçalho e corpo da mesma URL se medem na MESMA requisição.**

**E o relógio desfaz a outra metade:** a entrada de cache presa era de **14h40:01** com `max-age` de 7200 s, portanto só venceria sozinha às **16h40** — e foi **recriada às 16h05:59**, durante o Sync da revisão 41, com a purga por arquivo sendo o código que rodava. Não é prova de causa; é a única causa identificada, com o vencimento por tempo descartado pelo relógio. A purga foi **restaurada na revisão 42** (casca 1.6.4), com a atribuição dita como inferência.

**ESTADO REAL, medido às 16h07Z no endereço canônico:** quatro saídas de compra pela busca, **zero** ocorrências da frase proibida, "73 linhas" na tabela, a `/divulgacao-de-afiliados/` limpa. `conferir-no-ar.py`: **220 afirmações, 0 falha**, seções 9, 10 e 11 incluídas. **Este item está CUMPRIDO.**

**OS ITENS (b) E (c) FORAM EXECUTADOS NA EXECUÇÃO DAS 19h17Z DE 14/09, e o (b) devolveu DUAS coisas — uma esperada e uma que ninguém procurava.**

- **(c) A reconferência "duas horas depois": PASSOU.** `conferir-no-ar.py` às 19h20Z, antes de qualquer trabalho: **220 afirmações, 0 falha**, seções 9, 10 e 11 incluídas. A purga continuava entregando três horas depois de restaurada.
- **(b) A inferência virou medição, e a purga PEGA — só que não na hora.** A revisão 43 (a leva do Xiaomi S10) mudou texto servido de verdade: o artigo-âncora passou a nomear `S20, S10, E10, S12, E12, X20` no lugar de `HO041, HO400, HO401, HO407, OB010`. Sync às **19h30:50Z**; canônico ainda VELHO às **19h33:30Z** (com a quebra de cache já servindo o novo, medido a um segundo de distância); canônico NOVO às **19h33:36Z**, com a entrada de cache nova criada às 19h33:35Z (`expires` 21h33:35, `max-age` 7200 s). **166 segundos**, e não os 7200 do vencimento por tempo: a atribuição de 14/09 está certa, e ganha um número.
- **E O ACHADO QUE O TESTE NÃO PROCURAVA: a seção 10 era CEGA para mudança de texto.** Ela comparava três contagens de marcador — saídas de compra, degraus de trilha e blocos de compra — enquanto o docstring prometia comparar "a revisão servida", que **não existe no HTML e nunca foi implementada**. Nenhuma das três se move quando o desembarque troca uma palavra, que é o desembarque mais comum desta ilha. Às 19h33:30Z ela teria aprovado, item por item, a página velha que o leitor estava recebendo. Consertado na mesma passada: a afirmação passa a ser sobre **a impressão do leitor** (o texto servido, sem marcação e sem a chave de quebra de cache), e ela repete dentro de um orçamento **declarado** de 360 s, imprimindo o atraso que mediu — janela conhecida vira número em vez de alarme falso, que é o erro que custou quatro revisões de diagnóstico às 15h17Z. A prova de que a trava morde está em `ferramentas/mutacoes-canonico-velho.py`, que reconstrói o par velho/novo de hoje e mostra as contagens empatando enquanto a impressão separa. `conferir-no-ar.py` foi de 220 para **229 afirmações**.

**O QUE FICA, e não bloqueia nada:** (a) o despacho para o Raphael segue **NORMAL** — a medição de hoje confirma que a purga entrega, então a purga por API do painel continua sendo oportunidade e não conserto. **A primeira coisa de toda execução desta ilha continua sendo rodar `conferir-no-ar.py` e olhar as seções 9, 10 e 11**; o que mudou é que agora a 10 vê texto, e um atraso impresso em segundos é informação, não defeito.

### 2. OS DOIS NÚMEROS DA R1 — **CUMPRIDO E CONFERIDO NO AR** (R1 1.8.0, 14/09/2026)

E a medição achou que **a diferença não era a que esta ronda supôs**, o que torna o achado mais útil. Não são os kits abrindo uma linha por peça. Contado: a tabela tem **73 linhas** (uma por `modelo, tipo, peça`), responde **63 células** (`modelo, tipo`), mostra **56 pares** peça × modelo — e o banco declara **63 pares**. Ou seja **os dois 63 são grandezas diferentes que hoje dão o mesmo número por acidente do banco**. Igualar os números, que era o conserto tentador, teria colado duas contas que não são a mesma e publicado a igualdade como fato.

Nada foi igualado: cada número ganhou nome. O alto fala do BANCO; a tabela fala de si mesma ("73 linhas … respondem 63 perguntas do tipo qual peça desta função serve neste modelo"); e as 10 linhas a mais saem com a causa escrita. A régua é a seção 19 do `teste-r1.php`, que recomputa as quatro contas a partir das linhas e do `pecas.json`, por um caminho que não é o do gerador — e que **exige que a página continue chamando cada uma pelo seu nome enquanto forem iguais**, porque é enquanto são iguais que ninguém percebe que foram confundidas.

### 3. A FRASE DA R2 — **CUMPRIDO E CONFERIDO NO AR** (R2 1.6.0, 14/09/2026)

Os dois defeitos que esta ronda nomeou, mais dois da mesma família que a leitura das nove frases achou.

**(a) Divergência é entre FONTES, não entre NÚMEROS.** `ha_divergencia` comparava os dois limiares e nunca perguntava quem os publicava. Consertado na raiz. **(b) A oração quebrada** vinha de um molde de um tamanho só recebendo a saída de `escrever_limiar()`; nasceu `escrever_piso()`, que escolhe o verbo pela comparação. **(c) NASCEU UM QUARTO MOLDE** — dois números, um publicador só —, porque tirar `liso|nao` do molde da divergência o jogaria no da "ÚNICA recomendação", onde há duas: trocar uma afirmação falsa por outra não é conserto. **(d) A CONTRAÇÃO**, que esta ronda não viu: `carpete|nao` servia *"a única recomendação brasileira deste banco é a de a Canaltech"*. A regra de contração nasceu nesta ilha na manhã do mesmo dia e este molde não a usava.

**E a linha de procedência** passou a ter uma entrada por DOCUMENTO e não por limiar. A chave é o endereço com a data, nunca o nome do veículo — o mesmo veículo pode publicar dois artigos, e aí são duas fontes de verdade.

Lido no ar, na situação-âncora: *"Para piso liso sem animal que solta pelo, o Mundo Conectado publica dois números: recomenda 3.000 Pa e escreve que até 1.500 Pa já basta (verificado em 09/09/2026)"*, com **uma** linha de procedência. A régua é a seção 12 do `teste-r2.php`, que lê a FRASE SERVIDA e nunca a bandeira que a produziu — era na bandeira que estava o defeito —, e `ferramentas/mutacoes-divergencia-r2.py` produz o mundo de ontem e vê as quatro travas reprovarem.

### 4. O PISO DA 25.2 — **a conta mudou em 14/09/2026, e a dívida agora tem outro nome**

Esta ronda contou 32 itens (só o `pecas.json`); com os 33 modelos de `modelos-robo.json` são **65**. A execução das 15h17Z fechou o despacho do Raphael e a leitura correta passou a ser esta:

- **65 de 65 têm saída de compra na página** — a busca crua, que a máquina fabrica sozinha. **Zero sem saída**, que é o que a 25.2 chama de defeito da 19.1.
- **65 de 65 saem por link que NÃO rastreia e NÃO paga comissão.** Isso não é defeito de página: é dívida de receita, e o que falta continua sendo só o ENCURTAMENTO, que exige a sessão logada do painel da Shopee (25.6).
- **65 de 65 seguem sem `url_produto`**, porque não há ficha de produto nenhuma para conferir. `intestavel` é `false` nos 65 — não há link encurtado cuja saúde fique desconhecida.

**Continua sendo linha de "Precisa do Raphael"**, e o texto original desta ronda segue valendo para essa metade: a escolha da palavra-chave está feita, item a item. O que mudou é que **a página parou de esperar por ela**.



**A metade que já estava feita, e que muda de quem é a dívida:** os 65 têm `afiliado.url_busca_produto` preenchido com a URL crua da busca e `motivo_sem_url_busca` escrito. Exemplo: `multi-pr10124` → `https://shopee.com.br/search?keyword=Multilaser%20escova%20lateral%20robo%20aspirador`. **A escolha da palavra-chave já foi feita; falta só o encurtamento**, que pela 25.6 exige a sessão logada do painel de afiliado da Shopee. A seção 12 proíbe a ronda diária de gerar link de afiliado novo.

*(Os parágrafos que ficavam aqui diziam "a ilha continua no ar sem UMA porta de compra" e "32 itens intestáveis". As duas frases eram verdade quando esta ronda as escreveu, às 14h32Z, e deixaram de ser às 15h47Z. Foram REESCRITAS e não acrescentadas: duas frases em desacordo no mesmo arquivo não são história, são armadilha — a próxima execução acredita na que ler primeiro.)*

### 5. ACHADO DE MÉTODO: o teste de vida da 25.4, do jeito que está escrito, NÃO É EXECUTÁVEL hoje — e existe um caminho que funciona

Isto não é defeito desta ilha. Está aqui porque a 25.4 manda a ronda diária abrir a página do produto, e **isso falhou nas duas vias, medido hoje**:

- **Da nuvem:** `shopee.com.br` e `www.mercadolivre.com.br` devolvem **0 bytes** (egresso). Não é intermitência: repetido.
- **Do Chrome do Raphael, navegando:** a Shopee redireciona para `shopee.com.br/verify/captcha?...&scene=crawler_item` depois de poucos segundos, tanto em `/search?keyword=` quanto em `/product/<shop>/<item>`. **A Sentinela não resolve CAPTCHA, por regra**, e parou ali.

**O caminho que funcionou, medido hoje no navegador dele, e que a 25.4 deveria passar a mandar usar:** a API de ficha da própria Shopee, chamada por `fetch` de dentro de uma aba já no domínio —

```
https://shopee.com.br/api/v4/pdp/get_pc?shop_id=<shop_id>&item_id=<item_id>&detail_level=0
```

devolve `data.item.title` e `data.item.item_status`. Os dois ids saem tanto de `.../product/<shop_id>/<item_id>` quanto do sufixo `i.<shop_id>.<item_id>` das URLs de slug. **Não gasta clique de afiliado, não depende de ler texto de página renderizada e não esbarra no anti-robô.** Isto pede uma linha na 25.4 do `ARQUIPELAGO.md` — e essa linha é do Raphael, não da Fundação.

**Medição de hoje com esse método, feita na clubedomosaico porque a robometria não tem link nenhum para testar** (a ronda é desta ilha; o teste foi onde havia o que testar): **10 de 10 itens vivos**, 0 mortos, 0 esgotados — 6 da Shopee (`tekbond-silicone-acetico-construcao`, `cascola-cascorez-extra`, `quartzolit-rejunte-acrilico`, `quartzolit-rejunte-ceramicas`, `quartzolit-rejunte-porcelanatos-e-ceramicas`, `quartzolit-rejunte-piscinas`), todos com `item_status: normal` e o nome batendo com o do banco; e 4 catálogos `/p/MLB...` do Mercado Livre (`tekbond-silicone-neutro`, `quartzolit-cimentcola-externo-acii`, `loctite-durepoxi`, `quartzolit-rejunte-epoxi`), todos HTTP 200 com o `<h1>` do produto certo. **Nenhum dos 4 links que morreram em 13/09 reapareceu, e nenhum novo morreu em 24 h.**

## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 11/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O despacho de 10/09, logo abaixo, NÃO deve ser apagado:** o que resta nele é a metade humana (reenviar o sitemap no Search Console), que é do Raphael e não da Fundação.

**Nenhuma correção foi feita pela Sentinela nesta ronda.** Os dois defeitos achados moram em código de snippet PHP, e a regra 3 da seção 12 manda parar e despachar.

**OS ITENS 1 E 2 FORAM CUMPRIDOS em 11/09/2026** (casca 1.2.0, manifest revisão 15
— ver `REGISTRO.md`). O texto deles saiu daqui; o que a ronda MEDIU E APROVOU
continua abaixo, como linha de base para a próxima. Um achado dos dois vale ser
lembrado: a trava de página fina que entrou junto reprovou
`/divulgacao-de-afiliados/` com 1.325 caracteres de corpo — defeito que já estava
no ar e que nenhuma ronda tinha procurado.

<!-- item 1 (meta description e Open Graph nas 9 páginas) cumprido em 11/09/2026 -->
<!-- item 2 (H1 da raiz era "Início") cumprido em 11/09/2026 -->

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
   **CUMPRIDO E CONFERIDO EM 16/09/2026.** Medido no Search Console, propriedade `sc-domain:robometria.com.br`, aba Sitemaps: `https://robometria.com.br/wp-sitemap.xml` é Índice de Sitemaps, enviado em 10/09/2026, **última leitura em 15/09/2026, status PROCESSADO, 9 páginas encontradas, 0 vídeos**. O "Não foi possível buscar" de 10/09 era o estado normal de domínio recém-certificado e se resolveu sozinho em cinco dias — ninguém precisou reenviar nada. **A lição, e ela vale para toda ilha nova:** "não foi possível buscar" em sitemap de domínio novo NÃO é defeito, é espera; o erro foi carregar isso como pendência humana durante seis dias sem voltar para medir. Antes de abrir despacho de metade humana, meça de novo.

   **O que isso destrava:** a rampa da seção 14 dependia desta medição. A leva de malha (bloco 5b) deixa de estar bloqueada por falta de sitemap lido.

   **O que ainda NÃO existe, e é diferente de sitemap:** na mesma visita, a aba Indexação das páginas respondeu "Dados em processamento: volte em mais ou menos um dia" — a propriedade é de 09/09 e ainda não tem série de indexação. Sitemap lido não é página indexada. Só depois que essa aba trouxer número é que a rampa da 14 tem dado para decidir tamanho de leva.

## DESPACHO DO RAPHAEL — 14/09/2026 — O PISO DE BUSCA — **CUMPRIDO E CONFERIDO NO AR EM 14/09/2026, 15h**

Fechado pela execução das 15h17Z, item por item, e o que ele achou pelo caminho está registrado abaixo porque muda o que a próxima execução precisa saber.

**Item 1 — a URL de busca crua.** JÁ EXISTIA, em 65 de 65 publicáveis, e não foi duplicada. O despacho pediu o campo com o nome `afiliado.url_busca_bruta`; o contrato já tinha batizado o mesmo fato de `afiliado.url_busca_produto` na 25.4-b, e esta ilha o preencheu em 13/09. Criar um segundo nome para a mesma coisa é exatamente a cicatriz que a R2 pagou de manhã — duas metades que nunca se falam, cada uma certa no seu lugar. **Fica valendo o nome do contrato.**

**Item 2 — `degrau: 4` e `conferido_em`.** Gravados nos **65** publicáveis (32 peças + 33 modelos; a ronda contou só as 32 do `pecas.json`). O degrau sai derivado do próprio campo em `ferramentas/gerar-busca-de-produto.py`, nunca digitado, e `conferido_em` só é reescrito quando o degrau muda — carimbar a data de hoje a cada passada faria o campo dizer "conferido hoje" sem que nada tivesse sido conferido. **A régua do validador estava INVERTIDA e foi reescrita:** ela dizia "degrau sem ficha não parou em lugar nenhum", o que contradiz a própria 25.1, cujo degrau 4 é a busca e por definição não tem ficha.

**Item 3 — `intestavel`.** Nasceu como campo DERIVADO (há `url` e não há `url_produto`), e hoje é `false` em 65 de 65, porque nenhum item tem link encurtado. Como o mundo não existe no banco, a mutação o PRODUZ.

**Item 4 — o piso na tela. Era aqui que estava o trabalho.** A frase proibida saiu de **cinco** lugares (a casca, a R1, a R2, o A1 e o A2) e de uma seção inteira da `/divulgacao-de-afiliados/` que existia para explicá-la ao leitor. A porta de compra passou a descer a escada da 25.1 e parar no primeiro degrau que servir. **A busca crua sai SEM `rel="sponsored"`**: ninguém paga por aquele clique, e a página de divulgação passou a dizer ao leitor qual link rende comissão e qual não rende.

**Item 5 — os números, contados e nomeados:** 65 publicáveis, 65 com piso, **0 sem saída de compra**, 65 com saída que não rastreia (esperando só o encurtamento da 25.6), 0 com ficha de produto, 0 intestáveis, 0 com `url_produto`.

**O QUE ESTE DESPACHO ACHOU E NÃO PEDIA, e é a parte que importa para as outras ilhas:** o desembarque desta ilha parava no **cache do hospedeiro**. Ver o item 1 do despacho da Sentinela, reescrito acima.

## DEFINIÇÃO DE PRONTA — PRAZO 23/09/2026 (dado pelo Raphael em 16/09/2026)

[stated] Ele disse: "robometria deve estar pronta em no maximo 7 dias". Esta ilha é a única em foco (`foco.md`), então recebe todas as execuções da Fundação e o teto semanal inteiro de geração de link.

**Esta seção manda sobre a FILA DE BLOCOS.** A fila abaixo é aberta por natureza — "expandir o banco" não tem fim. A partir de agora, bloco que não fecha um dos cinco itens desta lista NÃO é executado antes dos que fecham. Quando os cinco estiverem fechados, a ilha é declarada PRONTA no `ESTADO.md` (`estado: viva`) e a fila volta a valer normalmente.

1. **PORTA DE COMPRA EM TODO ITEM PUBLICÁVEL.** Nenhum cartão com "Link de loja em breve". Todo item publicável com saída de compra pela escada da 25.1, parando no primeiro degrau que servir, e o aviso de comissão visível na página. `rel="sponsored"` **só** no link que rende comissão (ficha ou busca encurtada); a busca crua sai sem ele, e o cartão diz qual é qual. **Pronto quando:** uma varredura das páginas no ar não encontra a frase "em breve", não encontra item publicável sem saída, e a página de divulgação declara as duas contas — quantos itens têm saída e quantos rendem comissão. *(A meta de receita — os 68 com `url_busca` encurtada — continua existindo, mas como **dívida do elo da Shopee**, não como critério de PRONTA, porque ela não depende da Fundação.)*
   *(Corrigido em 16/09/2026 pelo achado G2 do Pente Fino: a versão anterior deste item, escrita nesta mesma manhã, exigia carimbar de patrocinado 68 links que ninguém paga — afirmação falsa ao Google e ao leitor.)*
   **— FECHADO em 16/09/2026, medido no ar (revisão 52).** `conferir-no-ar.py`: zero ocorrência de "em breve" nas 9 URLs, zero item sem saída, 229 afirmações e 0 falha. A página de divulgação passou a declarar **as duas contas**: 73 itens publicáveis, **68 rendem comissão** e 5 não. *(A segunda conta ESTAVA FALSA no ar até esta execução, e é o achado: ela vinha de `com_link`, que conta FICHA de produto, e a página a apresentava como "quantos rendem comissão". Os dois foram o mesmo número enquanto a única alternativa à ficha era a busca crua, que não rende nada; com os links encurtados de 16/09 a página passou a dizer ao leitor que NADA rendia comissão enquanto 68 links rendiam e saíam com `rel="sponsored"`. **Subdeclarar relação paga é tão errado quanto superdeclarar** — as duas descrevem a relação errado, e a página de divulgação é o pior lugar possível para isso. A conta passou a ser a da ESCADA: rende quem tem ficha OU busca encurtada.)* Os **5 que não rendem** são os modelos Xiaomi sem canal brasileiro que entraram hoje, e o encurtamento deles depende da sessão do painel da Shopee (25.6) — **dívida do elo, não critério de PRONTA**, como o próprio item já dizia.
2. **A EMENDA DO FUNIL FECHADA.** A pessoa chega pela R2 e volta pela R1 sem encontrar. É o defeito estrutural que esta ilha já mediu sozinha. Pronto quando: `cobertura-r1.py --gravar` mostrar pelo menos **15** modelos publicáveis atendidos pelas duas ferramentas, e a medição estiver commitada. **A RÉGUA DESTE ITEM MUDOU EM 16/09/2026, e o número não andou: 38 modelos publicáveis, dos quais 8 atendidos pelas duas.** Até hoje o cruzamento contava como "a R2 responde" todo modelo com `pa_declarado`. A R2 passou a exigir também **canal brasileiro** (ver o bloco do portão, abaixo), e a régua mudou junto — porque **régua que mede a meta não pode ser mais frouxa que a ferramenta que a meta descreve, senão a meta se fecha sozinha**. Concretamente: os cinco modelos Xiaomi que entraram hoje têm Pa declarado e peça declarada, e contariam +5 na interseção pela régua antiga, sem que UMA pessoa a mais fosse atendida — a Xiaomi Brasil não os vende. A forma mais barata de chegar a 15 seria despejar modelos globais no banco, e essa porta está fechada. *(Linha de base anterior, medida pelo Pente Fino na mesma manhã: 33 publicáveis, 8 pelas duas — `positivo-pra2000`, `positivo-pra800`, `xiaomi-e10`, `xiaomi-h40`, `xiaomi-s10`, `xiaomi-s20`, `xiaomi-s40`, `xiaomi-s40c`, os mesmos oito de hoje.)* *(Este item dizia "das 28 entradas publicáveis, só 3" — os dois números são a varredura de 13/09/2026 e envelheceram com a leva do Xiaomi S10 de 14/09. A meta de 15 não foi tocada: ela é absoluta e continua de pé.)*
3. **[RAPHAEL] ZERO DEFEITO ABERTO DE RONDA.** Nenhum item pendente nos despachos da Sentinela dentro deste arquivo. Pronto quando: as seções de despacho não tiverem item sem "CUMPRIDO E CONFERIDO NO AR".
4. **SITEMAP ACEITO NO SEARCH CONSOLE.** Hoje está em "Não foi possível buscar". É metade humana e está no despacho de 10/09. Pronto quando: a propriedade `sc-domain:robometria.com.br` mostrar o sitemap lido, com contagem de URLs. **— FECHADO em 16/09/2026: processado, última leitura 15/09, 9 páginas encontradas.**
5. **TODA PÁGINA COM `<meta name="description">` E TAGS `og:`.** Defeito levantado na ronda de 11/09. Pronto quando: varredura das páginas no ar não achar nenhuma sem os dois. — **JÁ ATENDIDO. Medido no ar pelo Pente Fino em 16/09/2026: 9 de 9 URLs do sitemap em HTTP 200, todas com `<meta name="description">` e com cinco propriedades `og:` (`og:title`, `og:type`, `og:url`, `og:description`, `og:locale`).** *(O defeito de 11/09 é o item 1 daquela ronda, e o próprio arquivo o registra cumprido em 11/09/2026, poucas linhas acima — este item nasceu descrevendo o mundo anterior. Quem fechar o placar reconfere e marca feito; nenhum bloco precisa ser gasto nele.)*

**QUEM É DONO DE CADA ITEM.** Item marcado **[RAPHAEL]** não é da Fundação e nenhuma execução dela consegue fechá-lo — o placar obrigatório deve dizer "esperando o Raphael", nunca "faltando". Hoje o item 3 está nessa condição: as três pendências que sobram nas seções de despacho deste arquivo se declaram dele (o encurtamento na Shopee e as duas linhas do despacho da Sentinela de 14/09). O prazo de 23/09 continua de pé; o que esta marcação muda é de quem é cada item, para a Fundação não gastar execução olhando para um vermelho que não é dela.

**O QUE "PRONTA" NÃO SIGNIFICA, escrito para ninguém se iludir com o prazo:** pronta é a ilha completa e capaz de faturar — não é a ilha faturando. Indexação e posição são relógio do Google, não nosso: dias para indexar, semanas para posicionar. Cumprir os cinco itens até 23/09 é a nossa parte, e é a única parte que depende de nós.

**Em toda execução, o relatório final abre com o placar dos cinco itens**, cada um com feito ou faltando e o número medido ao lado. Sem placar, a execução não fechou.

## O PORTÃO DO CANAL BRASILEIRO — nasceu em 16/09/2026, e ele decide o que a R2 recomenda

**A regra, e ela cabe numa frase:** a R1 responde a quem JÁ TEM o aparelho, então a compatibilidade declarada pelo fabricante vale onde o aparelho estiver; a R2 recomenda uma **compra** a um leitor brasileiro, então modelo sem canal brasileiro não é recomendação — é um beco. São duas perguntas diferentes e o banco passou a responder as duas separadamente, pelo campo `canal_brasileiro` (esquema versão 8).

**Canal brasileiro é endereço do FABRICANTE, e marketplace não serve.** Todo código tem busca em marketplace, então aceitar marketplace faria o portão aprovar tudo — e voltar a ser o que era antes de existir. O validador reprova.

**Por que ele nasceu, e é a parte que vale para as outras ilhas:** até 16/09 a elegibilidade da R2 pedia `status: publicavel` e `pa_declarado`, e mais nada. A lista saía certa mesmo assim, porque as cinco marcas coletadas eram todas de canal brasileiro — **verdade por coincidência da coleta**. E o contraexemplo já estava DENTRO do banco desde 13/09: cinco códigos Xiaomi (E10C, E12, S12, S40 Pro, X20) que as páginas de acessório do próprio fabricante declaram e que a Xiaomi Brasil não lista. Um deles declara **15.000 Pa**, a maior sucção do banco inteiro: sem o portão, o primeiro nome da lista em toda situação de pelo — a consulta que mais vende no nicho — seria um aparelho que o leitor não compra aqui.

**O portão não mudou UMA linha da tela**, e é por isso que a bateria `ferramentas/mutacoes-canal-brasileiro.py` existe: trava que nasce sem mudar nada é trava que ninguém sabe se existe. As 5 mutações reprovam, inclusive a que produz o mundo em que as duas metades da R2 erram juntas.

**O que ele custa, dito com o número na mesa:** 6 dos 38 modelos publicáveis ficam fora da recomendação — `electrolux-erb20` (que entrou no banco só por agregador de manual, sem página da Electrolux Brasil) e os cinco Xiaomi. A página **diz isso ao leitor**, com os nomes e com os 15.000 Pa, porque portão que só anuncia o que protege e nunca o que custa é portão que ninguém consegue discutir.

## A ESCADA DE COMPRA SE MEDE INTEIRA, NUNCA POR UM DEGRAU (16/09/2026)

**QUATRO réguas desta ilha reprovaram no mesmo dia por medir um degrau da 25.1 em vez da escada**, e as quatro reprovaram uma página que tinha **melhorado**: `teste-r1.php`, `teste-a1.php`, `teste-r2.php`, `teste-a2.php` e a seção 11 do `conferir-no-ar.py` exigiam `rbm-comprar-cru > 0` — isto é, exigiam que a vitrine saísse pelo degrau 4, a busca CRUA. Quando os links de busca encurtada entraram, as páginas subiram para o degrau 3 e as réguas acharam zero onde esperavam quatro.

**Quando quatro réguas erram igual no mesmo dia, o erro não é de nenhuma delas:** é de terem sido escritas quando só existia um degrau alcançável, cada uma sem saber das outras. A afirmação que interessa nunca foi "quantas buscas cruas" — é **"o bloco de compra nunca fica vazio"**. Todas passaram a medir isso e a IMPRIMIR o degrau ao lado, que é como se vê o encurtamento avançando sem precisar de outra medição.

**Régua nova desta ilha nasce medindo a escada.** Se ela precisar do degrau, ela o imprime; se ela o exigir, ela reprova a subida.

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
site e sem rede, e é a verificação da seção 8 que esta ilha consegue executar **sem** tocar o
site. *(Esta linha dizia "a nuvem não alcança robometria.com.br" — falso desde 10/09/2026, e
contradito pela própria seção "Endpoints desta ilha" acima e pelo bloco 3b logo abaixo, que
registra o Sync acionado pela nuvem. Corrigido pelo Pente Fino em 14/09/2026.)* Ele confere o que a seção 8 pede e mais a
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
**ATUALIZAÇÃO 13/09/2026, segunda leva do dia — o lado WAP foi aberto e a linha MUDOU DE
NATUREZA.** A R1 saiu de 20 para **22** modelos que respondem e o vazio caiu de 13 para
**11**: W300 e WSMART entraram com 4 escovas. O que falta **não é mais achar a página** e
**não é rede** — a busca alcança a loja e o blog da WAP. Falta (i) o **código** da ficha,
que a busca não devolve (só o título e a URL), e (ii) a **função** da escova nos modelos de
escova única, que a seção 26 do `ARQUIPELAGO.md` proíbe ler do nome. Os dois se resolvem
pelo mesmo lugar: os manuais em PDF do item (c). Detalhe por alvo em
`dados/pecas.json` → `lista_de_compras`. **Sobram W400, W1000, W310 e W90 no vazio da
marca**, e o W90 é recusa medida, não lacuna de procura.
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

(e) ~~**A RECARGA DOS MODELOS QUE JÁ DECLARAM COBERTURA.**~~ **FECHADO em
12/09/2026, e NÃO por coleta: a lacuna mudou de natureza, como a dos m² no item
(d).** Nenhuma página de modelo declara tempo de carga (conferido no ERB60 e no
ERB80). O único número que a Electrolux publica no canal alcançável está num
artigo de **família** — 24 h na primeira carga, 5 h nas seguintes — e esse mesmo
artigo declara, **na mesma frase**, autonomia de 90 minutos, que não é a de
nenhum dos cinco (100, 100, 100, 100 e 120). O artigo fala de outro aparelho.
Os cinco `motivo_do_null` agora carregam essa causa, com o nome do documento. O
caminho de volta é a leitura direta do manual de cada modelo, que segue atrás do
egresso fechado. **O texto original fica abaixo, porque a medição que o derrubou
só faz sentido ao lado da expectativa que ele criou:**

(e-original) **A RECARGA DOS MODELOS QUE JÁ DECLARAM COBERTURA — o item de MENOR custo e
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

**O EGRESSO DIRETO A ESSES DOMÍNIOS SEGUE FECHADO, E ISSO NÃO BLOQUEIA O 3c.** Medido em
11/09/2026: `mi.com.br`, `xiaomi.com.br`, `wap.ind.br` e
`mais.conteudo.wap.ind.br` devolvem `000` — só os domínios das ilhas respondem.
*(O texto que ficava aqui mandava testar esses endereços com `curl` e dar o 3c inteiro por
bloqueado se eles falhassem. Foi exatamente isso que parou a coleta desta ilha por três dias:
o banco sempre citou `www.mi.com/br`, e a busca alcança. A seção 4 do `ARQUIPELAGO.md` virou
regra a partir deste caso — **o endereço que se testa sai do BANCO, do campo `url` da fonte
que se quer reler, nunca da prosa que descreve o bloqueio** —, e o registro de 13/09 mais
abaixo neste mesmo arquivo já dizia o contrário desta linha. Corrigido pelo Pente Fino em
14/09/2026.)*
**Antes de escolher um alvo do 3c:** abra o registro que você quer melhorar, copie o endereço
do campo `url` dele, e teste **esse**. Teste também os **dois canais**, que são redes
diferentes — egresso direto (`curl`/`WebFetch`) e canal de busca —, como manda o item
"O EGRESSO DIRETO E O CANAL DE BUSCA SÃO DUAS REDES DIFERENTES" em "Específico desta ilha".
Uma falha só vira bloqueio depois de repetir na mesma execução (seções 4 e 20.2), e bloqueio
herdado do `ESTADO.md` é retestado antes de ser respeitado. Alvo cujo canal estiver
comprovadamente fechado nos dois cai para o trabalho de repositório listado em "Específico
desta ilha", que não depende de rede nenhuma — o 3c inteiro, não.

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
   com a porta de compra já aberta**, descendo a escada da 25.1 e parando no primeiro
   degrau que servir — ficha (`url`), busca encurtada (`url_busca`) ou, enquanto o
   encurtamento não existir, a busca crua de `url_busca_produto`, que sai **sem**
   `rel="sponsored"` porque ninguém paga por aquele clique. Quando não há o que
   recomendar, o bloco não lista **e a página diz por quê**. `teste-r1.php` mede os
   cinco pontos (seção 13 dele), e a R2 nasce com isso, não com retrofit.
   *(Esta decisão mandava o bloco nascer "reservando o lugar com 'Link de loja em breve'",
   com o argumento — correto na época — de que esconder o bloco devolveria à procedência o
   papel de única porta clicável. A frase foi **PROIBIDA pela seção 7 do `ARQUIPELAGO.md`
   em 14/09/2026** e retirada de cinco lugares desta ilha no mesmo dia (casca 1.6.0, R1
   1.7.0, R2 1.5.0); medido no ar em 16/09/2026 pelo Pente Fino: **zero ocorrências de
   "em breve" nas 9 URLs do sitemap**. A ordem velha ficou de pé e faria a próxima
   ferramenta nascer com o defeito. Corrigido pelo Pente Fino em 16/09/2026.)*

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

**A SEXTA DECISÃO, fixada em 12/09/2026 no A2 e valendo para toda página desta ilha: A
ATRIBUIÇÃO DE UM NÚMERO É LIDA DO DEGRAU, NUNCA DIGITADA — e a régua que a deriva serve
a QUALQUER campo.** A R2 fechou isso em 11/09 para o Pa, e escreveu no próprio registro o
que aconteceria no dia em que um número entrasse por loja oficial da marca: "a página
emprestaria calada a autoridade do fabricante a quem apenas transcreveu". No A2 esse dia
já era o dia — a área por carga dos cinco Electrolux vem do degrau 4, e os cinco cartões
publicavam "O fabricante declara". Duas coisas seguem disso, e valem antes de escrever
qualquer página nova:

1. **Regra derivável por um campo só é regra que a segunda página reescreve.** A versão
   de 11/09 só sabia derivar a procedência do Pa; o A2 decide pela ÁREA e ficou sem de
   onde ler. Hoje quem deriva é `procedencia_do_campo(m, campo)` em `cobertura-r2.py` —
   página nova chama essa, não escreve a sua.
2. **Frase que publica DOIS números precisa de DUAS procedências.** Hoje os dois do
   cartão do A2 saem da mesma fonte, e é justamente por isso que a frase não pode
   presumir: verdade por coincidência do banco é a família de defeito que esta ilha já
   pagou duas vezes. Trava latente assim só conta como medida quando a mutação PRODUZ o
   mundo em que ela morde — ver `ferramentas/mutacoes-a2-procedencia.py`.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **WordPress, casca, AS DUAS ferramentas e OS DOIS artigos estão no ar desde 11/09/2026** (manifest revisão 13, 9 páginas no sitemap). Os blocos 1, 2, 3, 3b, 4, 4e e 5 estão feitos para os dois eixos da ilha.
- ~~**ACHADO DE 11/09/2026: `robometria_casca_numeros()` lia uma option que nunca existiu no site.**~~ **CUMPRIDO em 11/09/2026** (casca 1.3.0, revisão 16): os onze números que a ilha publica sobre si mesma viajam em `dados/casca-fatos.json`, publicável, com as réguas da medição dentro do arquivo, e o gerador recusa gravar se o banco de hoje não bater. Um dos números já mentia: dizia 33 pares e o site serve 32.
- **UM NOME POR PÁGINA, e ele tem uma fonte só — 11/09/2026, casca 1.4.0, revisão 17, conferida no ar.** `robometria_casca_nome_da_pagina()` resolve as nove páginas; o H1 (post_title), o `<title>`, o `og:title`, o degrau da trilha e o rótulo do cartão **derivam** dela. Seis das nove tinham dois nomes ao mesmo tempo, porque o mapa das cabeças trazia um `titulo` digitado ao lado do da definição da página. **Página nova não precisa lembrar de nada**: nomeia-se num lugar só, e o portão `ferramentas/teste-voz.php` cobra as cinco superfícies.
  **O `<title>` agora é escrito por este repositório** (`document_title_parts` na casca). Antes a home servia o nome do site mais a descrição curta do wp-admin — 73 caracteres, vocabulário de dentro da fábrica, num campo que nenhum arquivo daqui escreve. **O teto é 65 caracteres, cobrado no NOME (52), na bancada, antes de publicar.**
- **TODA PÁGINA DESTA ILHA TEM UM SEGUNDO ESTADO VÁLIDO, e ele é invisível para quem mede o corpo.** Quando o banco não chega, as duas ferramentas, os dois artigos e o trecho de números da metodologia servem "estamos sem o banco" — página inteira, com cabeçalho, rodapé e prosa honesta. `ferramentas/varrer-corpo.php` passou dois dias medindo TRÊS desses estados como se fossem a página (a1 com 1.118 caracteres, a2 com 1.107, a metodologia sem os números), porque não carregava as options que o Sync grava. Agora: dono único do aviso (`robometria_casca_sem_banco_html`), marca `rbm-sem-banco` no markup, `!!! sem-banco` na linha do estado varrido, e **dois portões reprovando** (`teste-voz.php` e `teste-acentuacao.php`). **Bancada nova copia o boot inteiro — options E snippets —, ou mede a metade que não dá erro.**
- ~~**O PRÓXIMO PASSO é a vitrine de produto dentro do resultado da R2.**~~ **ERA
  FALSO, e o registro fica: a vitrine existia desde 11/09**, nasceu junto com a R2 e
  `robometria_r2_vitrine()` já era chamada na resposta. O passo tinha sido escrito de
  memória e nunca medido, e quem o leu como fato quase construiu de novo o que já
  estava no ar. **Antes de começar um bloco, abra a URL** — custa dois minutos e é a
  mesma regra que a seção 20.2 do contrato aplica a bloqueio de rede: estado herdado
  de execução anterior se reconfere, nunca se lê como fato.
  **O que o cartão realmente não tinha era PROCEDÊNCIA, e isso foi fechado em
  11/09/2026** (R2 1.2.0, revisão 18): o Pa é o único número que decide a
  recomendação e saía sem endereço, sem data e sem o degrau da escada. Ver o
  `REGISTRO.md`.
- ~~**O PRÓXIMO PASSO, medido no ar em 23h37Z de 11/09/2026 e não lembrado:** o **A2**
  (`/quantos-m2-o-robo-aspirador-limpa-por-carga/`) serve **5 cartões de vitrine com
  ZERO procedência** — "O fabricante declara 166 m² por carga", sem endereço, sem
  data, sem degrau e sem link. É o mesmo defeito que a R2 acabou de fechar, na página
  irmã dela, e a casca já tem todas as peças (`na_tela` na escada de fontes,
  `robometria_casca_fonte_link`, e o padrão de teste da seção 16 do `teste-r2.php`
  para copiar). Depois dele, a seção **"Exatamente no limiar"** da própria R2, que
  nomeia modelos e Pa e também não cita origem.~~ **OS DOIS ESTÃO CUMPRIDOS:** o A2
  em 12/09/2026 (A2 1.2.0, revisão 20) e a seção da R2 em 12/09/2026 (R2 **1.3.0**,
  revisão **22**, `/status` conferido às 19h30Z em um disparo). Com isso **não resta
  nenhum lugar nas duas ferramentas nem nos dois artigos em que um número decide e a
  origem não aparece** — mede isso a seção 17 do `teste-r2.php` e a do
  `conferir-no-ar.py`, no HTML servido.
  **A DECISÃO QUE FICOU, e vale para toda seção desta ilha que NÃO recomenda:** a
  regra da seção 7 (porta de compra antes da procedência) existe para o link de fonte
  nunca ser a única coisa clicável de um bloco. Onde a página recusa o item, a porta
  não pode existir — e o que a regra proíbe é o **silêncio** sobre a ausência, não a
  ausência. Então a seção declara que não vende e diz por quê. Trocar um silêncio por
  outro não é conserto.
  **E o `afiliado.sub_id_2` saiu do banco na mesma passada:** ele nomeia a PÁGINA que
  levou o clique, e o banco só sabe dizer um valor por registro. Cada gerador carimba
  o próprio código (R1, R2, A1, A2); `validar-banco.py` reprova o campo de volta no
  banco, e a seção 17 do `teste-casca.php` cobra que cada arquivo de dados carimbe só
  o seu — **página nova que copiar um gerador antigo reprova antes de existir URL**.
  ~~**O PRÓXIMO PASSO** é a transcrição da composição dos kits e o item **(e)** do 3c.~~
  **OS DOIS FORAM FECHADOS EM 12/09/2026**, e cada um de um jeito: a transcrição
  **entregue** (ERB30 e ERB44, ver os itens logo abaixo) e a recarga **recusada com
  causa medida** — ela deixou de ser coleta, como os m² do item (d). O que destravou
  não foi a rede abrir: foi separar o egresso direto do canal de busca.
  ~~**O PRÓXIMO PASSO AGORA** é o kit do ERB80.~~ **CUMPRIDO em 12/09/2026** (ver
  os itens abaixo), junto com o pano de microfibra que a mesma varredura achou.
  ~~**O PRÓXIMO PASSO AGORA** são as **peças da Xiaomi e da WAP com código.**~~
  **O LADO XIAOMI FOI CUMPRIDO em 13/09/2026** (manifest revisão 25, `/status`
  conferido em UM disparo): oito peças com código entraram, a R1 foi de 16 para
  **20 dos 28** modelos e o cruzamento com a R2 de **3 para 7**. E a causa dos três
  dias parados **não era a rede**: o `PROMPT.md` e o `ESTADO.md` mandavam testar
  `mi.com.br` e `xiaomi.com.br`, e o banco desta ilha sempre citou
  **`www.mi.com/br`** — o endereço está escrito em sete registros desde 09/09. O
  egresso direto segue fechado por política nos três; a **busca alcança `mi.com`**,
  e nunca tinha sido testada nele. **Quando o canal falhar, confira o endereço
  contra o BANCO**, que é quem guarda a fonte, e não contra a prosa que descreve o
  bloqueio.
  ~~**O PRÓXIMO PASSO AGORA é a WAP, e o alvo TROCOU: lá o gargalo é MODELO, não
  peça.**~~ **O LADO DO MODELO FOI CUMPRIDO em 13/09/2026** (manifest revisão 26,
  `/status` conferido em UM disparo): **W90, W100, W100C, W300 e WSMART** entraram,
  e a WAP passou de 3 para **8** modelos. Nenhum dos cinco declara Pa — a marca
  publica Pa no W400 e nível de sucção no resto —, então a leva **não move a R2**:
  ela existe para abrir o lado do modelo, que era o que travava a peça. O preço
  está medido e é honesto: a R1 continua respondendo em 20 modelos e passa a sair
  **vazia em 13** (era 8), e a página de metodologia publica os dois números
  contados. Ordem "modelo antes de peça" cumprida.
  ~~**O PRÓXIMO PASSO AGORA é a PEÇA da WAP.**~~ **REMEDIDO EM 14/09/2026, 19h25Z,
  e o resultado foi NEGATIVO — o que muda a ordem da fila, não o diagnóstico.** A
  peça da WAP foi o primeiro alvo desta execução, e as duas medições pedidas abaixo
  foram feitas: (i) o egresso direto a `loja.wap.ind.br`, `blog.wap.ind.br` e
  `www.wap.ind.br` devolveu `000` nos três, com `connect_rejected` do proxy, e o
  `WebFetch` devolveu `EGRESS_BLOCKED`; (ii) **a passada limpa não devolve o
  código**. Buscando com `FW006267` na consulta, ele volta — o que é circular e não
  vale; buscando pelo título do produto, restrito a `loja.wap.ind.br`, a página
  aparece e **o campo da ficha não**, com a própria busca dizendo que o número não
  estava no conteúdo recuperado. É a terceira passada limpa a falhar no mesmo
  ponto, em execuções diferentes: **não é teimosia da busca, é o canal.** E os
  quatro modelos WAP que continuam no vazio da R1 (W400, W1000, W310, W100C) não
  têm página de peça de reposição na loja — duas passadas devolveram só a página do
  próprio robô e categorias genéricas. Fica valendo: quem destrava é o egresso
  abrindo, ou alguém lendo a ficha no navegador. **Por isso o alvo desta execução
  passou a ser o Xiaomi, que é o canal que funciona** — e a leva B106GL tirou o S10
  do vazio. A varredura de 13/09 já abriu as páginas de acessório
  por modelo (W300 com 9 acessórios em 7 categorias — filtro, escova, carregador,
  recipiente, mop, controle remoto e pincel; WSMART com 9; W90 com escova rotativa
  e carregador) e `marcas.json` já tem o `canal_de_pecas` da marca. **O que
  impediu a gravação hoje foram duas coisas, e as duas são de método:**
  1. **O código voltou em UMA passada e não voltou na segunda.** `FW006267` na
     escova direita do W300, `FW008028` na escova central do WSMART e `FW009132`
     na escova rotativa do W90 — nas três, a segunda passada limpa não devolveu o
     código. Um código de peça é o que a pessoa digita na busca da loja: entrar com
     ele meio confirmado é pior que não entrar.
  2. **A página de acessório NÃO declara a função da escova.** "Direita",
     "Esquerda", "Central", "Frontal" e "Rotativa" são **nomes**, e ler
     `tipo_de_peca` de um nome é a heurística por vizinhança que a seção 8 do
     contrato proíbe — a mesma que fez a Xiaomi publicar um catálogo de variantes
     como kit. Quem for pegar isto decide primeiro **onde** a função está
     declarada (a ficha do próprio robô lista o que vem na caixa, e é candidata),
     e só então grava.
  **E existe um terceiro alvo barato que apareceu junto:** o W300 e o WSMART
  publicam acessório na categoria **Recipiente**, e `reservatorio` é justamente o
  único tipo do vocabulário sem NENHUMA peça no banco inteiro — é o tipo que saiu
  do seletor da R1 por isso. Uma peça de reservatório com função declarada devolve
  o tipo ao seletor.
  **Os manuais em PDF continuam sendo a porta do nível 2** e agora são oito, um por
  modelo WAP do banco, com revisão e data no nome do arquivo (W400 "FW009293
  REV00MAI23", W1000 "FW010143 REV03ABR25", W90 "FW010263 REV00JAN24", W100
  "FW007467 REV01OUT21", W100C "FW008617 REV00SET21", WSMART "FW007881 REV. 00
  ABRIL/2020"). Só o `WebFetch` do PDF segue bloqueado; **o WSMART é a exceção de
  endereço** — a WAP guarda o manual dele no próprio blog, e não em
  `mais.conteudo.wap.ind.br`.
  **E há alvos de CATEGORIA DESCOBERTA que o vocabulário não comporta — dois
  agora, porque a leva da Xiaomi acrescentou a tampa de escova `D106-BZSZ` do S20
  ao lado do saco descartável do ERB80. Os dois ficam fora pela mesma régua:**
  `loja.electrolux.com.br/kit-3-sacos-descartaveis-electrolux-para-robo-aspirador-erb80/p`.
  Saco descartável é consumível de base autolimpante, e o ERB80 tem base
  autolimpante — mas `tipo_de_peca` no `esquema-banco.json` não tem esse tipo, e
  **acrescentar tipo mexe no seletor da R1, na cobertura e nos portões**. Fica
  registrado como categoria descoberta, não como coleta pendente: quem for pegá-lo
  decide primeiro se o tipo nasce, e a régua dessa decisão é a 14.3 (faixa
  descoberta, não número redondo). Na mesma varredura apareceu também um **ERB40**
  com Kit Performance próprio, e ele não está em `modelos-robo.json`.
  **A leva de malha (5b) continua travada** pela metade humana do despacho: o sitemap precisa ser reenviado no Search Console, e isso exige o navegador do Raphael.
- **Antes de mexer em qualquer snippet, rode os OITO testes de bancada:** `teste-casca.php`, `teste-r1.php`, `teste-a1.php`, `teste-r2.php`, `teste-a2.php`, `teste-acentuacao.php`, `teste-arvore.php` e `teste-voz.php`, todos com a raiz da ilha como argumento (`php ferramentas/teste-casca.php .`). **A contagem de afirmações de cada um NÃO está escrita aqui de propósito** — em 13/09/2026 eram 902 no total, e a lista que ficava nesta linha já tinha cinco números vencidos ao mesmo tempo. Quem quiser o número de hoje roda e lê a última linha; quem escreve número derivado em prosa assina um cheque contra o banco de amanhã, e esta ilha já pagou esse cheque dentro da própria bancada (ver `mutacoes-varredura-por-modelo.py`). Depois do desembarque, `python3 ferramentas/conferir-no-ar.py` mede as nove URLs no ar com régua própria — **e `python3 ferramentas/conferir-kits-no-ar.py` (71) mede a ENTRADA da R1 no ar, 14 estados de modelo × tipo, porque o primeiro mede o caso-âncora e bloco que muda resposta de consulta não aparece lá** — os endereços e os nomes estão escritos literalmente dentro dele, e não lidos do código, para as duas metades não errarem juntas. Eles são a única verificação da seção 8 que roda sem depender do site. **O sexto é o único que varre a ENTRADA INTEIRA** — um estado por página fixa, um por modelo publicável do banco, um por tipo de peça e as bordas da R2, um processo por estado (eram 72 quando isto nasceu; hoje são quantos o banco pedir, e o próprio portão cobra um estado para CADA modelo, por id), via `ferramentas/varrer-corpo.php`: os outros medem o caso-âncora, e foi por isso que "Aspirador Robo" e "Versao A" ficaram invisíveis para cinco testes verdes. O segundo compara as 188 frases publicadas contra a implementação de referência; o terceiro **recalcula a tese do artigo em PHP, direto do banco, sem olhar para o que o gerador em Python escreveu** — duas contas independentes que batem são medição, uma conta sozinha é o que o autor achou.
- **A PORTA DE COMPRA TEM UM DONO SÓ, e ele é a casca.** `robometria_casca_porta_de_compra`, `robometria_casca_rotulo_da_loja`, `robometria_casca_fonte_link` e `robometria_casca_css_vitrine` valem para toda página desta ilha que recomenda item; a R1 delega para elas. Página nova que recomenda produto **chama estas funções**, nunca escreve as suas. Os pesos visuais do botão de compra e do link de procedência são regra do Arquipélago (seção 7), não estilo local: com uma cópia por página, bastaria alguém ajustar uma delas para a ilha voltar — numa página só, e sem ninguém notar — ao defeito de 10/09/2026.
- **Página nova entra no catálogo da casca pelo FILTRO dela**, `robometria_ferramentas` para ferramenta e `robometria_artigos` para artigo. A casca nunca ganha uma cópia da página dentro; é assim que a home e o hub listam qualquer coisa nova sem serem editados de novo, e é o que garante as duas listagens que a seção 9 exige.
- ~~**O BANCO ESTÁ EM ASCII, E AGORA ISSO APARECE NA TELA.**~~ **CUMPRIDO em 11/09/2026.** 121 strings restauradas nos nove campos que a varredura mediu chegando ao corpo servido, e a operação é **provada diacrítico-only**: reduzido a sem-diacrítico, o banco de hoje é byte a byte o de ontem (`dados/acentuacao-restaurada.json`, conferido linha a linha por `teste-acentuacao.php` com régua própria). **A restauração não é releitura:** o acento foi reposto pela ilha, não lido no fabricante — e é por isso que o livro-razão existe, como lista de conferência de quem reler os manuais quando a rede abrir.
  **Quem segura daqui para a frente é `ferramentas/teste-acentuacao.php`**, que lê o CORPO dos 72 estados e reprova qualquer palavra da régua. Palavra ambígua (o "e" que pode ser "é") ficou de fora do mapa de propósito: acertar por adivinhação não é acertar. **O que ficou de fora do escopo, e é trabalho de verdade:** `declarado_como`, `motivo_do_null` e `descricao_na_fonte` seguem em ASCII. Elas NÃO estão na tela hoje (medido), mas são prosa longa e chegam à tela no dia em que alguém as publicar — e aí o portão reprova, que é exatamente o desenho.
- ~~**O KIT DECLARADO NÃO TEM PORTA DE COMPRA, E ISSO SE DESTRAVA POR DADO.**~~
  **CUMPRIDO em 12/09/2026** (manifest revisão 23, `/status` conferido em um
  disparo). A previsão estava certa e foi medida, não suposta: **o dado abriu a
  porta de compra sozinho**, sem uma linha de snippet. Na consulta ERB30 +
  filtro a página agora diz que a Electrolux não vende o filtro avulso, nomeia o
  Kit Performance que o contém, e serve o bloco "Onde comprar" antes da
  procedência. O ERB30 era o único modelo da ilha que não respondia consulta
  nenhuma; a Electrolux passou a 9/9 e a R1 a 16 dos 28 modelos.
  **O QUE FICOU VALENDO PARA A PRÓXIMA TRANSCRIÇÃO, e é o mais importante:** o
  ERB30 veio com quantidades e o **ERB44 veio pela metade** — a página dele
  declara os tipos e não as quantidades, e diz "escovas" sem dizer qual, num
  modelo que tem escova rotativa central vendida à parte. A busca **ofereceu a
  composição do ERB30 como preenchimento** e ela foi recusada: modelo vizinho não
  declara pelo vizinho. Item sem tipo entra com `tipo: null`, que é como o esquema
  diz "o kit serve e nós não sabemos dizer este item" — e a R1 então recusa aquele
  tipo, que é o acerto e não a falta.
- ~~**O KIT DO ERB80 EXISTE NA LOJA E NÃO ESTÁ NO BANCO.**~~ **CUMPRIDO em
  12/09/2026** (manifest revisão 24, `/status` conferido em UM disparo) — **e a
  previsão escrita aqui estava errada, o que vale mais que o registro em si.**
  O texto anterior dizia que o kit entraria "no nível do ERB44, não no do
  ERB30", porque as leituras de então tinham devolvido só o trio genérico. A
  coleta desta execução, com perguntas limpas, achou o contrário: a página do
  kit no domínio do **fabricante**
  (`content.electrolux.com.br/…/kit_performance_erb80/`) descreve os três itens
  **um a um** e nomeia a escova pelo **tipo** — "escovas laterais, direita e
  esquerda". Ele entra ACIMA do ERB44.
  **A CONFERÊNCIA QUE SUSTENTA ISSO CUSTOU UMA LEITURA A MAIS, e é a régua para
  a próxima transcrição desta ilha:** um bloco por item numa página de catálogo
  pode ser molde do gerador de páginas, e aí não declara nada sobre aquele
  produto. O jeito de saber é ler a **página irmã** com a MESMA pergunta — a do
  ERB44, mesmo domínio, mesmo formato, traz só a cópia genérica. Logo o bloco
  por item existe na página do ERB80 porque a Electrolux o escreveu lá; e, de
  quebra, isso confirma que o `tipo: null` do ERB44 foi acerto e não preguiça.
  É a mesma família do "documento de família com dois números", só que a
  declaração vizinha aqui serve para **confirmar**, não para desmascarar.
  **A QUANTIDADE FICOU null NOS TRÊS**, de propósito: "direita e esquerda" está
  numa frase de benefício, descrevendo o que escova lateral faz, não numa lista
  de conteúdo da embalagem. Ler dali um "2" é transformar prosa de venda em
  quantidade declarada. E a busca ofereceu "1 filtro HEPA, 1 pano e 2 escovas"
  dizendo **textualmente** que era "baseado em kits similares de outros
  modelos" — recusado, pela mesma regra que barrou o preenchimento do ERB44.
- **O PANO DE MICROFIBRA ERB60/61/62/80 ENTROU JUNTO, e não estava previsto em
  lugar nenhum** — apareceu na mesma varredura do kit. É a primeira peça avulsa
  desta ilha a servir o ERB80 e cobre quatro modelos de uma vez. **A lição de
  fila:** varredura feita para colher UM alvo devolve vizinhos, e o vizinho aqui
  era mais barato que o alvo. Vale olhar a lista de resultados inteira antes de
  fechar a coleta.
- **FRASE QUE DEPENDE DA VIZINHA É FRASE QUE UM DIA MENTE — e esta estava NO AR
  em três páginas** (12/09/2026, R1 **1.3.0**). A frase do kit quando existe a
  peça avulsa era *"Ele também vem dentro do kit …"*. O pronome só apontava para
  alguma coisa por **sorte de ordem**: as frases saem na ordem do banco, e no
  único caso que existia (o filtro do ERB60/61/62) o registro da peça avulsa
  vinha antes do registro do kit. Quando o pano de microfibra deu ao **mop** um
  avulso, a frase do kit saiu na posição do KIT — depois da escova lateral e
  **antes de o mop ser nomeado**. Oito portões verdes, porque todos mediam a
  frase sozinha, e sozinha ela estava certa.
  **A saída não foi reordenar a lista** — seria consertar o sintoma e deixar a
  dependência de pé. A frase passa a **nomear o tipo**, nas duas implementações,
  e fica autossuficiente: é a 5.2 do contrato ("frase que sobrevive a ser citada
  fora de contexto") e a 8 ("quem decide é a estrutura, nunca a vizinhança").
  **Quem segura daqui para a frente:** a seção 14 do `teste-r1.php` (régua
  escrita à mão no próprio teste, medindo só a **primeira oração** das frases
  das DUAS implementações), `ferramentas/mutacoes-frase-nomeia-o-tipo.py` (4 de
  4 reprovadas — e a terceira **produz o mundo**, quebrando os dois lados juntos,
  então a comparação PHP × referência continua verde e só a trava nova pega), e
  a metade no ar em `conferir-kits-no-ar.py`, que passou a varrer os 5 estados
  do ERB80.
- **MUTAÇÃO TAMBÉM TEM NÚMERO DE TELA, e duas morreram caladas aqui**
  (12/09/2026). Duas mutações do `mutacoes-arvore.py` traziam o número
  **digitado** nos dois lados (`"pares_declarados": 32` → `33`). Bastou o banco
  crescer para o alvo sumir do arquivo e elas deixarem de editar coisa alguma —
  a "mutação inerte" que aquele arquivo existe para impedir, agora dentro dele.
  Agora leem o valor de hoje e somam 1. **A cicatriz do "número de tela nasce
  contado" vale para a bancada, não só para a página:** quem digita um número
  derivado assina um cheque contra o banco de amanhã.
- **O EGRESSO DIRETO E O CANAL DE BUSCA SÃO DUAS REDES DIFERENTES, e a distinção
  vale por um bloco inteiro** (12/09/2026). `curl` e `WebFetch` devolvem `000` e
  `EGRESS_BLOCKED` em `electrolux.com.br`, `loja.electrolux.com.br`,
  `cuida.electrolux.com.br`, `mi.com.br` e `wap.ind.br` — política de egresso,
  remedida em duas passadas com a ilha em 200 nas duas. **A busca alcança os
  mesmos fabricantes.** Os dois kits ficaram três dias esperando porque o
  `ESTADO.md` dizia "a rede está fechada" e ninguém tinha separado os dois canais.
  Antes de declarar coleta bloqueada nesta ilha, teste **os dois**.
- **QUANDO UM DOCUMENTO DE FAMÍLIA TRAZ DOIS NÚMEROS, O QUE VOCÊ JÁ CONHECE DIZ SE
  O OUTRO É DO SEU MODELO** (12/09/2026, e é a régua que fechou o item (e) do 3c).
  A recarga dos cinco Electrolux que declaram cobertura não é mais coleta: nenhuma
  página de modelo declara tempo de carga, e o único número publicado está num
  artigo de família ("Como faço para utilizar o meu Robô Aspirador Home-e
  Experience com Autonomous Technology") que, **na mesma frase**, declara autonomia
  de 90 minutos — número que não é o de nenhum dos cinco (100, 100, 100, 100 e
  120). A declaração vizinha desmascarou a atribuição. Sem essa conferência, o 5 h
  entraria com cara de dado de fabricante.
- ~~**UMA FONTE ESTÁ NO NÍVEL 2 E A ESCADA DIZ QUE O NÍVEL 2 NÃO EXISTE.**~~ **DECIDIDO em 11/09/2026: NÃO é nível 2. É nível 3.**
  **A regra, e ela vale para toda fonte de toda ilha desta pasta:** uma origem tem TRÊS elos — quem escreveu o documento, quem o guarda e como nós o lemos — e **o nível é o do elo MAIS FRACO**, nunca o do mais forte. O manual do ERB10/ERB11/ERB20 é escrito pela Electrolux (elo forte), mas está guardado por `manuals.plus` e chegou aqui por busca, sem leitura direta. Dois dos três elos são fracos.
  **A direção saiu da assimetria de custo (seção 10 do contrato), não do gosto:** errar para BAIXO custa uma frase mais fraca na tela ("a confirmar no manual"); errar para CIMA faz a página de metodologia declarar um rigor que a ilha não tem — e metodologia é a página cujo único produto é o rigor.
  **A medição decidiu sozinha:** as QUATRO únicas fontes de nível 2 do banco inteiro eram a mesma entrada de `manuals.plus`. Nível 2, neste banco, era inteiro custódia de terceiro — não um registro solto.
  **O que ficou mecânico, para a contradição não voltar:** (a) `validar-banco.py` passou a exigir que `origem` bata com a `origem` que a escada dá àquele `nivel` — era por aí que o defeito entrava, porque só o `nivel` era conferido; (b) nível 1 ou 2 agora exige o campo `leitura: "direta-na-fonte-primaria"` **declarado**, e silêncio nunca promove (adivinhar pelo texto do `canal_de_coleta` seria a heurística por vizinhança que a seção 8 proíbe); (c) a coluna "Temos hoje" da página **deixou de ser digitada e passou a ser contada** (`dados/casca-fatos.json`). As três foram testadas quebrando o banco de propósito e reprovam.
  **O caminho de volta ao nível 2 está escrito no registro:** reler o mesmo manual no endereço da Electrolux sobe o campo de 3 para 2 sem mudar mais nada.

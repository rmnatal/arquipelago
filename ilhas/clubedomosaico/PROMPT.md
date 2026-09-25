# ILHA: CLUBE DO MOSAICO — mosaico artesanal (loja + guia + escola)

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá.**

> **ESTA ILHA ESTÁ EM FOCO desde 24/09/2026.** `foco.md` na raiz nomeia a **clubedomosaico**, e pela seção **1.2**
> do `ARQUIPELAGO.md` a Fundação trabalha **só nela**. Este arquivo vale inteiro. *(O aviso anterior era de 16/09,
> dizia que a ilha estava fora do foco por causa da robometria, e continuou aqui depois de a aquametria entrar e
> sair — três mundos atrás. Corrigido em 24/09/2026 pela execução que achou a ilha fora do ar.)*

> **ANTES DE QUALQUER BLOCO, A PORTA DE ENTRADA — seção 29 do `ARQUIPELAGO.md` (24/09/2026).** Esta ilha passou
> pelo menos um dia com 16 das 17 URLs servindo a página de estacionamento da HostGator, com o `/status` verde e a
> bancada verde, porque todo portão daqui entra por query na raiz ou rota REST. Rodar `python3
> ferramentas/conferir-no-ar.py .` é um comando e mede a porta; se ela estiver caída, o diagnóstico e o reparo estão
> em `?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>` (com `&reparar=1` para consertar).

## O que esta ilha tem de diferente (leia antes de tudo)
Esta é a **terceira ilha** e a primeira que **não veio da Bússola**: é um projeto pessoal do Raphael. A mãe dele faz mosaico artesanal (vasos, colares, quadros). O site tem **três motores num domínio só**, e a malha fecha um ciclo comercial completo:
1. **LOJA** — venda direta das peças da mãe (margem cheia, produto próprio, sem afiliado).
2. **GUIA DE MATERIAIS** — fichas de pastilhas, alicates, colas, rejuntes, bases e acabamento, com vitrine de afiliado (Shopee e Mercado Livre).
3. **ESCOLA** — tutoriais "como fazer mosaico em X" e páginas de técnica, com lista de materiais linkada ao Guia e "prefere pronto?" linkado à Loja.

Consequências para a Fundação:
- **Existe uma artesã real.** É a única ilha com uma pessoa por trás. **Confirmado pelo Raphael em 11/09/2026: a artesã aparece com nome e foto no Sobre e na assinatura das peças, com links para as redes sociais dela.** Nome, foto e perfis ainda não foram entregues — enquanto não chegarem à pasta `identidade/artesa/`, a página Sobre usa 'a artesã' e deixa o bloco de foto/redes pronto e vazio, registrado no `ESTADO.md` como pendência dele (não bloqueia).
- **Produto próprio não é afiliado.** Página de peça leva `Product` + `Offer` com preço real, disponibilidade ("pronta entrega" ou "sob encomenda, N dias") e botão **Comprar** que abre WhatsApp com mensagem pronta ou link de pagamento. Nunca `rel="sponsored"` em link de peça própria. Nunca inventar peça, preço, medida ou foto: **o catálogo é cadastrado pela própria artesã no painel `/atelie/`** (ver DESPACHO abaixo). Sem peça cadastrada, a Loja fica com as páginas de coleção prontas e com estado vazio honesto, e o `ESTADO.md` diz isso.
- **O logo é fornecido pelo Raphael** e vai para `identidade/logo/` desta pasta. **Não reconstruir, não redesenhar, não vetorizar por conta própria.** O cabeçalho é CLARO e serve **o arquivo completo dele** (`logo-clube-do-mosaico.png`, lótus + wordmark), em `<img>` de 52 px de altura, **sem nenhum texto ao lado** — o nome já está dentro do logo. **O arquivo é TRANSPARENTE** (conferido pelo Raphael na biblioteca de mídia em 11/09/2026); a afirmação anterior de que ele tinha fundo preto era ERRADA e foi retirada daqui. O que não funciona é o logo sobre fundo ESCURO: o wordmark é vinho `#69030C` e some no preto. `identidade/logo/lotus-512.png` está truncado no repositório e serve só para ícone pequeno quando for corrigido — nunca substitui o logo no cabeçalho.

## Identidade
- Nicho: mosaico artesanal no Brasil — o eixo paramétrico é **"o que comprar para fazer a peça X"** (qual cola/rejunte para qual base e ambiente; quantas pastilhas/rejunte para qual área) e **"qual peça pronta para qual uso"** (centro de mesa, presente, jardim).
- Domínio: clubedomosaico.com.br, registrado em 10/09/2026. Ilha nº 3 do Arquipélago.
- **Os tokens desta ilha moram em `DESIGN.md`, nesta mesma pasta** — é de lá que a casca renderiza. As linhas de paleta e tipografia abaixo continuam aqui como registro do que foi aprovado; se as duas discordarem, vale o `DESIGN.md` (seção 22.6).
- Paleta (lida pixel a pixel do logo, aprovada pelo Raphael em 10/09/2026): noite `#000000` (fundo de rodapé; **o cabeçalho é claro — o logo NUNCA vai sobre preto, porque o wordmark vinho some**) · coral `#FC483B` (marca, **cor de sinal**: botões, preço, um uso por tela) · salmão `#FA7665` (pétalas laterais; só em ilustração e hover, nunca em texto sobre branco) · vinho `#69030C` (wordmark do logo) · rubi `#8A0F18` (links e texto de destaque sobre branco, 4,5:1 garantido) · papel `#FFFFFF` (fundo do miolo) · tinta `#1F1715` (texto) · traço `#E9DCD7` · legenda `#6E5F5B`. **Miolo branco e limpo, cara de e-commerce; o preto fica só no rodapé.** Alerta técnica em âmbar `#B9791A`, nunca em vermelho (vermelho é a marca).
- Tipografia: **Outfit** (títulos e preço) · **Source Sans 3** (texto) · **JetBrains Mono** (medida, quantidade, unidade, código de produto, com `tabular-nums`). Texto corrido nunca vai em Mono.
- Símbolo: **o logo fornecido** (flor de lótus geométrica de sete pétalas em coral/salmão, fundo transparente, wordmark "clube do mosaico" em minúsculas arredondadas logo abaixo). Ver "O que esta ilha tem de diferente".
- Interface: padrão da seção 6 do contrato (hambúrguer no celular, vitrine em carrossel, promessa antes do formulário, favicon próprio). Sem contagem regressiva, sem "mais vendido" inventado.

## O buraco que esta ilha existe para ocupar
Medido em 10/09/2026 (Planejador de palavras-chave, conta do Raphael, faixas; SERP aberta no Chrome dele):
- **Não existe fazenda de conteúdo nem autoridade editorial** no mosaico artesanal BR. Top 10 de "material para mosaico", "alicate para mosaico", "vaso de mosaico": lojinhas WooCommerce pequenas (mosaicoemcasa, universodomosaico, onomosaicos, bsmosaicos, mosaikaescoladearte), listas do Mercado Livre, Pinterest, YouTube, Wikipedia, blog de 2012. **Ninguém responde as perguntas técnicas** (qual cola para qual base, quantas pastilhas por peça).
- Cauda exata do artesanato, 100–1.000/mês: material para mosaico · pastilhas para mosaico · pastilhas de vidro para mosaico · azulejo para mosaico · alicate para mosaico (+35 variantes de 10–100) · kit mosaico · curso de mosaico · espelho mosaico · loja de materiais para artesanato · presente artesanal · vaso decorado. 10–100: vaso de mosaico · colar de mosaico · cola para mosaico · rejunte para mosaico · base para mosaico · mandala de mosaico · mosaico para iniciantes · ~80 "como fazer mosaico em/de X".
- Cabeças que se alcançam por tabela, 1k–100k/mês: como fazer mosaico · mosaico bizantino · tesselas · material para artesanato · cachepots · vaso decoracao · vaso para mesa de jantar.
- **Três armadilhas, não construir em cima:** "quadro mosaico" (é quadro impresso em 5 painéis, outra intenção); "pastilha de vidro" sozinho e tudo com piso/piscina/cozinha/banheiro/pedra ferro/são tomé (revestimento de obra: Leroy, Portobello); "mosaico no instagram/canva/de fotos" (grade de feed).
- Corpus completo, com faixa, concorrência e CPC: gravar em `dados/corpus-buscas.md` no bloco 1 a partir do que está em `/areas/projeto-clube-do-mosaico.md`.

## Endpoints desta ilha
- Sync: `https://clubedomosaico.com.br/?clubedomosaico_sync=jDJMsXmxxUFjfLahxgKArxP3VhtZPwHK&forcar=1`
- Status: `https://clubedomosaico.com.br/wp-json/clubedomosaico/v1/status`
- **Cópia das peças (seção 24 do contrato), URL COMPLETA e literal:** `https://clubedomosaico.com.br/wp-json/clubedomosaico/v1/pecas?token=jDJMsXmxxUFjfLahxgKArxP3VhtZPwHK` — o parâmetro chama-se `token` e o valor é **o mesmo token do Sync** da linha acima (`cdm_loja_token_esperado()` lê `clubedomosaico_sync_token()`). Sem ele a rota devolve 401, que foi exatamente o que a ronda da Aquametria mediu em 13/09/2026: o endpoint existia, o nome do parâmetro não estava escrito em lugar nenhum, e a cópia da 24 não aconteceu por falta de uma linha de documentação. Conferido desta nuvem em 13/09/2026 às 15h21Z: HTTP 200, `{"total":0,"pecas":[]}` — a artesã ainda não cadastrou peça, e **zero peça é resposta, não falha**; o arquivo `dados/pecas.json` nasce no dia em que houver a primeira.
- Estado da loja em número, rota **pública** e sem token: `https://clubedomosaico.com.br/wp-json/clubedomosaico/v1/loja` — não há segredo em dizer quantas peças a loja tem; o que é dado da artesã fica atrás do token, na rota de cópia acima.
- Snippet "Clube do Mosaico Sync" v1.1.5 = snippet #5 do Code Snippets, ATIVO desde 11/09/2026 01h03 UTC. Primeiro sync: revisão 3 lida, 0 aplicados, 5 aguardando desembarque. O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador (copiar da Aquametria quando for preciso).
- **Quem aciona o Sync é a própria Fundação, por `curl`, ao fim de cada bloco publicável** (seção 4 do contrato). Commit sem Sync não está no ar.
- Search Console: propriedade de domínio `sc-domain:clubedomosaico.com.br`, VERIFICADA em 10/09/2026. Sitemap `https://clubedomosaico.com.br/wp-sitemap.xml` enviado em 11/09/2026 (primeira leitura "não foi possível buscar" é o placeholder até o Google ler). ATENÇÃO: o domínio teve vida anterior — há um `sitemap.xml` de 2019 na propriedade; conferir no Search Console e no Wayback se existem backlinks antigos ou URLs órfãs para redirecionar (oportunidade e risco).
- Plugins ativos (11/09/2026): Code Snippets, Site Kit by Google (não conectado — exige OAuth do Raphael; não é bloqueio), Converter for Media, Limit Login Attempts Reloaded. Akismet e Hello Dolly inativos.
- WordPress: admin `mosaico_gestor` (credencial nunca vai para o repositório).
- GA4: propriedade `553922792` na conta `Arquipélago` (`407777291`) · ID de medição **G-0K5PY39HV7** · fluxo "Clube do Mosaico — site" (`15766180417`)
- **LOGO OFICIAL (arquivos que o Raphael subiu na biblioteca de mídia em 11/09/2026 — usar EXATAMENTE estes, sem redesenhar):**
  - Logo principal (lótus + wordmark "clube do mosaico", **fundo transparente**, 1536×1024): `https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png` — **é o logo do cabeçalho, sempre, inteiro e sem texto ao lado**, e também o `logo` do `Organization` no JSON-LD. Só não pode ser servido sobre fundo escuro.
  - Favicon (lótus sobre quadrado branco): `https://clubedomosaico.com.br/wp-content/uploads/2026/09/clube-do-mosaico-favicon.png` — fonte para os ícones; a casca pode servir os PNGs de `identidade/logo/` (favicon-512/180/32, gerados dessa mesma lótus) como data URI, ou apontar `<link rel="icon">` para esta URL. `identidade/logo/lotus-512.png` (lótus transparente) serve para os lugares pequenos onde o logo completo não cabe.

## Memória a carregar
`/areas/projeto-clube-do-mosaico.md`, `/areas/fabrica-de-sites.md`, `/areas/arquipelago-operacao.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/shopee-affiliate.md` (método de uma passada só e Mercado Livre), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DA SENTINELA — 2026-09-23 (LEITURA SEMANAL, 20h12Z) — a ilha esquecida é a que tem tráfego

**A ilha está FORA DO FOCO** (`foco.md` nomeia a aquametria desde 21/09), então pela 1.2 nada aqui fura a fila: **despacho NORMAL de ilha fora do foco espera.** Este despacho existe porque a 1.2-b.1 manda a medição continuar em todas as ilhas, e porque o que a medição achou muda a conversa sobre a ordem do foco.

**O NÚMERO QUE MANDA NESTE DESPACHO:** em 15→21/09 esta ilha teve **30 impressões**, contra **4** da aquametria (que tem 48 URLs e está em foco) e **1** da robometria. **Três páginas na primeira página do Google** — 7,8 · 9,1 · 7,0 — e **zero clique**. A ilha não recebe execução desde **15/09** e não tem ronda técnica registrada em nenhuma data.

**A DECISÃO DA RAMPA: MANTÉM.** `piso: abaixo` — 17 URLs de 40. Pela 21.8 a série não autoriza nem proíbe.

### 1. `/author/mosaico_gestor/` ESTÁ INDEXADA E TOMOU IMPRESSÃO NA POSIÇÃO 1,0 — E NÃO É PÁGINA DESTA ILHA

Medido hoje: responde **HTTP 200**, **não tem `<meta name="robots">`**, **não tem `rel="canonical"`**, **não está no sitemap** e **nenhuma página da ilha aponta para ela** (conferido na home e em `/materiais/qual-cola-usar-no-mosaico/`: zero ocorrências de `/author/`). Mesmo assim o Google a indexou e a serviu **uma vez, na posição 1,0**, nesta janela.

É página fina, órfã, sem dado e sem porta de compra, competindo por orçamento de rastreamento com **15 páginas não indexadas** desta mesma propriedade. **É o oposto do que a seção 14 manda.**

**A mesma família existe nas irmãs e está medida:** na aquametria `/author/aquametria_gestor/` responde **200 sem `noindex`** (ainda não indexada); na robometria o slug equivalente dá 404. E `/?s=<termo>` responde **200 sem `noindex`** nas **três** ilhas — sem sintoma hoje, porque nenhuma serve caixa de busca, mas é o mesmo buraco.

**Isto é código de snippet (`clubedomosaico-casca.php`) e por isso NÃO foi consertado pela Sentinela** (seção 12, lista fechada: snippet é sempre da Fundação).

**Pronto quando:** `/author/mosaico_gestor/` servir `<meta name="robots" content="noindex, follow">` no HTML servido, as 17 URLs do sitemap continuarem **sem** `noindex` (as duas direções medidas por portão, não por olho), e a leitura semanal seguinte registrar que a linha de `/author/` **saiu** de `dados/posicoes.md`.

> **DUAS DAS TRÊS CONDIÇÕES ESTÃO CUMPRIDAS E CONFERIDAS NO AR EM 25/09/2026 às 13h29Z** (casca 1.13.0, BLOCO B
> do despacho do Raphael de 24/09). `/author/mosaico_gestor/` serve `noindex, follow` e as 17 URLs do sitemap
> continuam sem `noindex`, as duas direções por portão em `conferir-no-ar.py`. **A terceira é da leitura de
> 30/09** — só ela pode dizer se a linha de `/author/` saiu de `dados/posicoes.md`, e por isso este item fica
> aberto até lá, pela 18.4.
>
> **A ETIQUETA SAI COM ASPAS SIMPLES**, `<meta name='robots' content='noindex, follow' />`, e isso não é
> divergência: quem imprime agora é o `wp_robots()` do núcleo, como o BLOCO B manda. Três réguas desta ilha
> mediam a ASPA em vez da diretiva e tiveram de ser consertadas no mesmo movimento — uma delas passava a vazio
> justamente onde teria pegado as duas etiquetas.
>
> **E `/?s=<termo>` fechou junto**, que este mesmo item nomeia como "o mesmo buraco": a busca interna sai do
> índice com `noindex, follow` na mesma linha de código. **Nas irmãs continua aberto** — a aquametria e a
> robometria não foram tocadas, por força do foco.

### 2. O `sub_id` DA SHOPEE DESTA ILHA ESTÁ DESLOCADO UMA CASA — A ÚNICA VENDA QUE ESTA ILHA GERAR NÃO SABERÁ DE ONDE VEIO

Medido no Relatório de cliques do painel Shopee Afiliados, janela 16→22/09. O único clique desta ilha no período (20/09, 13h23) veio com o `sub_id` gravado assim:

```
-clubedomosaico-F2--
```

A Shopee junta os cinco `sub_id` com hífen. Os cinco campos deste clique são, portanto: **`sub_id_1` VAZIO**, `sub_id_2` = `clubedomosaico`, `sub_id_3` = `F2`, 4 e 5 vazios. (Que os campos são cinco e que o hífen é o separador está provado pelos outros cliques da mesma janela: `robometria-r1---` dá `robometria` + `r1`, que é a forma certa, e `robometria----` dá só `robometria`. E a 25.7 mediu que **hífen não é aceito DENTRO de um sub_id** — logo `clubedomosaico-F2` não pode ser um campo só.)

**A seção 7 manda: `Sub_id 1` = nome da ilha, `Sub_id 2` = código da ferramenta.** Aqui está tudo uma casa à direita, com o campo 1 vazio. **Consequência medida: o painel não consegue responder "qual ilha vendeu".** Hoje custa pouco porque o número é 1 clique e 0 pedido; custa tudo no dia em que houver pedido, que é exatamente o dia em que ninguém vai querer descobrir isto.

**Pronto quando:** todo link de afiliado desta ilha for gerado com `sub_id_1 = clubedomosaico` e `sub_id_2 = <código da ferramenta>`, **o banco da ilha for recontado** e o número de registros com `sub_id_1` preenchido for igual ao número de registros com link, e a leitura semanal seguinte encontrar no Relatório de cliques o formato `clubedomosaico-f2---` (campo 1 preenchido) em vez de `-clubedomosaico-F2--`.

> **A METADE DA MÁQUINA FECHOU EM 25/09/2026 às 10h40Z** (BLOCO 0), com os 31 links regerados pela Open API.
> **A METADE QUE FALTA NÃO É DE CÓDIGO:** só um clique DE GENTE faz o Relatório mostrar `clubedomosaico-f2---`,
> e conferir com clique nosso apagaria o primeiro clique orgânico que a leitura semanal procura. **Quem lê essa
> linha é a leitura de 30/09.**

### 3. CORREÇÃO DE CABEÇALHO — `urls_publicadas: 13` ESTÁ DEFASADO; O SITEMAP SERVE 17

Contado no ar hoje: `wp-sitemap-posts-page-1.xml` tem **12** URLs e `wp-sitemap-posts-peca-1.xml` tem **5** — total **17**. É a seção 4 em ação: resumo velho lido como fato.

**Pronto quando:** o cabeçalho do `ESTADO.md` trouxer `urls_publicadas: 17`, com a contagem refeita no sitemap no ar e registrada no `REGISTRO.md`.

### AS TRÊS PROPOSTAS DE ACELERAÇÃO (12.1) — na ordem de ROI

**PROPOSTA 1 — `/materiais/qual-cola-usar-no-mosaico/` ESTÁ EM 7,8 COM 17 IMPRESSÕES E CTR ZERO. É A MELHOR LINHA DO ARQUIPÉLAGO INTEIRO.**
- Consulta nomeada: **`cola para mosaico`**, posição **10,0**. A página inteira está em 7,8 com 17 impressões — mais impressões do que a aquametria e a robometria somadas, quatro vezes.
- Página: `https://clubedomosaico.com.br/materiais/qual-cola-usar-no-mosaico/`.
- Banda 4 a 10 pela 12.1: o trabalho é de **CTR, não de conteúdo**. A alavanca que a 12.1 nomeia: **título que promete o número, meta que promete a faixa e a fonte**. O precedente que já rodou está na robometria, proposta 2 de 16/09: o número sai de um arquivo derivado do banco, nunca digitado, e a marca é o que cede lugar no `<title>`.
- **O que esta proposta NÃO autoriza:** trocar a URL (proibido pela 12.1), reescrever a página, ou mexer em `/como-fazer/o-que-e-mosaico-picassiete/` — deixe uma página parada para a próxima leitura ter com o que comparar.
- **Pronto quando:** o `<title>` e a `<meta name="description">` servidos citarem um número que a própria página calcula, com a fonte, e a leitura de 30/09 registrar impressões e CTR desta linha para comparar com **7,8 · 17 impressões · CTR 0%**.

**PROPOSTA 2 — A ORDEM DO FOCO MERECE SER REVISTA, E QUEM DECIDE É O RAPHAEL.**
- A 1.2-b.3 diz, com todas as letras, que **a fila de foco é reordenada por número, não por quem esperou mais**, e que a aquametria entrou em foco por ser a única com demanda medida. **Isso era verdade em 18/09 e hoje há número novo:** a aquametria tem 46 de 48 URLs indexadas e **4 impressões**; a clubedomosaico tem 17 URLs, três páginas na primeira página e **30 impressões**. **Demanda medida por corpus e demanda medida por impressão não são a mesma coisa, e a segunda é mais barata de acreditar.**
- **Esta proposta NÃO é um pedido para trocar o foco**, e a Sentinela não tem essa autoridade. É o registro de que o critério da própria 1.2-b.3 aponta para cá agora, para o Raphael decidir com o número na mão.
- **Pronto quando:** o Raphael responder — ou mantendo a aquametria em foco com o motivo escrito em `foco.md`, ou trocando. **Qualquer das duas fecha esta proposta;** o que não pode é ficar sem resposta escrita.
- > **FECHADA em 24/09/2026, e ele escolheu a segunda.** `foco.md` na raiz passou a nomear a **clubedomosaico**, com o motivo escrito: *"a escolha da Clube do Mosaico não é rotação: é a 1.2-b.3 aplicada ao dado de 23/09 — ela é a ilha com MAIS TRÁFEGO do Arquipélago"*. O critério de pronto pedia resposta escrita e ela existe; esta proposta não tem mais item aberto. *(Reconhecido em 25/09/2026 pela execução das 19h16Z, que veio fechar a fila e achou uma proposta marcada como aberta cuja condição de fechamento já estava cumprida havia um dia — a seção 4 do contrato de novo: resumo velho lido como fato.)*

**PROPOSTA 3 — A CAMADA DE VENDA: AINDA SEM DADO, E COM UM BURACO DE ATRIBUIÇÃO.**
- Shopee, 16→22/09: **1 clique, 0 pedido** — e o clique veio com o `sub_id` deslocado do item 2. Mercado Livre, mesma janela, conta inteira: **1 clique, 0 pedido, R$ 0** (as etiquetas `clubedomosaicof1` e `clubedomosaicof2` existem desde 13/09; o painel só atribui etiqueta quando há venda, então **não dá para dizer que este clique foi desta ilha — não verifiquei**).
- **Lacuna de produto, link morto, comissão melhor, produto novo vendendo, backlink, marca: ainda sem dado.** Com 30 impressões e 0 clique orgânico, não havia outro número possível, e isso não é fracasso.
- **Pronto quando:** houver o primeiro clique orgânico saindo de uma das três páginas de primeira página para um link de afiliado — é esse o número que abre a camada de venda desta ilha, e nenhum outro.

## O LOGO DELE NO CABEÇALHO — CUMPRIDO E CONFERIDO NO AR EM 11/09/2026, 20h35Z

Era o despacho do Raphael de 11/09 (2), de prioridade máxima. **Casca 1.4.0,
manifest na revisão 8, `/status` com revisão 8.** Os cinco itens saíram inteiros:
o cabeçalho serve `logo-clube-do-mosaico.png` em `<img>` de 52 px com link para a
home e **nenhuma letra ao lado**, a barra subiu para 84 px, a lótus solta ficou só
para lugar pequeno, e o `VOZ.md` foi corrigido no molde de casca LOJA.

**O critério de pronto que ele escreveu, conferido abrindo a home:** a lótus com o
nome "clube do mosaico" embaixo, sobre fundo branco, sem texto duplicado ao lado.
E medido nas nove URLs por `ferramentas/conferir-no-ar.py` — 102 afirmações no
HTML servido, nenhuma falha.

**Duas decisões que ficam registradas para ele poder discordar:**
- **Os hexadecimais do despacho não entraram, como em 11/09:** `#FBF7F4` e
  `#EEE8E4` são vizinhos de um a quatro passos de `papel #FFFFFF` e `traço
  #E9DCD7`, que são os tokens aprovados por ele em 10/09 e os que o portão de
  paleta cobra. Um segundo branco a quatro unidades do primeiro é defeito, não
  identidade. Se ele quiser exatamente aqueles valores, é uma linha.
- **A 52 px o wordmark dentro do logo fica com ~8 px por linha.** É legível como
  logotipo e foi conferido ampliado pixel a pixel, mas é pequeno para ler. O
  arquivo é um lockup empilhado (lótus em cima, nome embaixo em duas linhas), e
  52 px de altura total é o número do próprio despacho. Se ele quiser mais
  presença há dois caminhos, e nenhum é da Fundação decidir sozinha: subir para
  ~64 px, ou mandar uma versão horizontal do lockup.

---

## DESPACHO DO RAPHAEL — 11/09/2026 — cabeçalho da casca: CUMPRIDO, menos a lótus

**Cumprido e conferido no ar em 11/09/2026 17h55Z** — casca 1.2.0, manifest na
revisão 6, `/status` com revisão 6. Os itens 1, 3 e 4 saíram inteiros e o item 2
saiu pela metade, pelo motivo abaixo. Ver `REGISTRO.md` para o que foi medido.

- **1. Header claro e limpo — feito.** Papel `#FFFFFF`, linha de 1 px em
  `#E9DCD7`, sem sombra, menu em `#1F1715` peso 500 com passagem em coral.
  Medido no navegador: `rgb(255, 255, 255)` de fundo nas nove páginas. A paleta
  não ganhou cor nova: os hexadecimais sugeridos no despacho (`#FBF7F4`,
  `#EEE8E4`, `#111`, `#E8483A`) são vizinhos de um a quatro passos dos tokens
  aprovados em 10/09, e um segundo coral a quatro unidades do primeiro é
  defeito, não identidade. **Se o Raphael quiser exatamente aqueles valores, é
  uma linha** — está registrado para ele poder discordar.
- **3. A home não exibe "Início" — feito.** O H1 da home é "Mosaico feito à mão,
  uma peça por vez", que é também o título da página, a tagline do site e a
  segunda metade do `<title>` no resultado de busca. O defeito por trás era o
  título nunca sincronizar; agora sincroniza, sem tocar em `post_name`.
- **4. Aparência clean, cara de e-commerce — feito** na medida em que este bloco
  alcança: miolo branco com respiro, título em peso 600 e abertura em 500 em vez
  de 700 em tudo, rodapé segue escuro. O que ainda não é e-commerce de verdade é
  a **vitrine**, que depende do CPT `peca` do bloco 4d — sem peça cadastrada, a
  home mostra estado vazio honesto.

### O ITEM 2 DESTE DESPACHO FOI FECHADO POR CIMA, e não cumprido como estava escrito

- **2. A lótus no cabeçalho.** Este item pedia a lótus SOLTA ao lado do wordmark
  em texto, e não é mais o que o cabeçalho tem que servir: o despacho de 11/09 (2)
  mandou o **logo completo, sem texto ao lado**, e o logo já contém a lótus e o
  nome. Cumprido em 20h35Z na casca 1.4.0. **A lótus solta continua truncada** no
  repositório (o `IDAT` declara 11.638 bytes num arquivo com 8.770), e isso deixou
  de bloquear qualquer coisa: o lugar dela é ícone pequeno, não o cabeçalho. Quando
  chegar um arquivo válido, `php ferramentas/gerar-marca.php .` embute — a
  ferramenta **recusa** arquivo que não abre, sem canal alfa ou com canto opaco.

**A reescrita da home e da `/materiais/` pela seção 15 (as duas ATUALIZAÇÕES de
11/09) saiu junto e está cumprida.** A home deixou de ser manifesto; o bastidor
do Guia mudou para `/materiais/como-sabemos/` (nível 2, `noindex`, fora do
sitemap); o bug "10 dos 5 itens esperam link" saiu do ar.

**A ÁRVORE DA SEÇÃO 16 TAMBÉM ESTÁ CUMPRIDA — 11/09/2026, 19h40Z**, casca 1.3.0,
manifest na revisão 7, `/status` conferido e as nove URLs abertas no ar.
`ARVORE.md` escrito, trilha em oito das nove páginas (a home não tem, 16.3),
`BreadcrumbList` nas mesmas oito e o cluster "Veja também" ligando os três
motores. **Nenhuma URL mudou e nenhuma precisou mudar** — esta ilha já nascera
com a árvore certa na estrutura; o que faltava era ela ficar visível. Por isso
não há 301 nenhum e o sitemap continua com as mesmas oito URLs. Critério de
pronto medido, não de olho: `teste-casca.php` com 327 afirmações (ele LÊ o
`ARVORE.md` para cobrar que documento e código digam a mesma coisa),
`ferramentas/mutacoes-arvore.py` com 19 de 19 mutações reprovadas, e 117
afirmações medidas no HTML servido.

ATUALIZAÇÃO 11/09 (Pauta): quando existir `pauta.md` nesta pasta (seção 17 do contrato), os guias entram na fila depois desta reescrita e da árvore, em levas por cluster; registrar no fecho de cada bloco quantos temas estão escritos / na fila / recusados.

## DESPACHO DA SESSÃO DE CONVERSA — 10/09/2026 — PAINEL DA ARTESÃ (requisito do Raphael, "não pode esquecer disso"; v2 substitui a v1)
A mãe do Raphael cadastra as peças **ela mesma**, com login e senha próprios, **numa área do site fora do wp-admin**. Palavras dele: "eu não quero que ela entre numa área wp-admin… um ambiente de cadastro de produto muito mais amigável… ela não é administradora, tem acesso somente a cadastro de produto". Portanto:
- O catálogo da Loja **NÃO vive no repositório**: `dados/pecas.json` é descartado. Vive no WordPress como CPT `peca`.
- **Ela nunca vê o wp-admin.** O painel é uma página pública do site, `/atelie/`, renderizada por snippet — o mesmo padrão do painel de corretores da Real 21 (front-end próprio, WordPress só por baixo).

**4d. LOJA — dois snippets, publicados nesta ordem, depois da casca 3b:**

**(a) "Clube do Mosaico Loja — peças e vitrine"** (o modelo e o lado público):
- CPT `peca` (`has_archive` em `/loja/`, `rewrite` `/loja/<slug>/`, `show_in_rest` true, **`show_ui` false** — não aparece no wp-admin para ninguém), taxonomias `colecao` (uso: centro de mesa, presente, jardim, parede, joia…) e `tecnica` (bizantino, direto, indireto, opus…), termos iniciais criados pelo snippet.
- Metas: `_cdm_preco` (decimal), `_cdm_disponibilidade` (`pronta_entrega`|`sob_encomenda`), `_cdm_prazo_dias`, `_cdm_medidas` (A×L×P cm), `_cdm_peso_g`, `_cdm_base`, `_cdm_cores`, `_cdm_quantidade`, `_cdm_galeria` (IDs de anexo em ordem). Imagem destacada = primeira da galeria.
- **Página pública da peça**: carrossel das fotos com `scroll-snap`, miniaturas, zoom no toque; título, preço em destaque (cor de sinal), disponibilidade e prazo, ficha técnica em tabela, descrição, botão **Verificar disponibilidade** (ver adendo LEADS DA LOJA; a option `cdm_whatsapp` continua existindo, mas passa a alimentar o link do e-mail de notificação, não o botão público), "como esta peça é feita" (tutorial da técnica, Escola) e "materiais usados" (Guia). **JSON-LD `Product` + `Offer`** (preço real, `availability` InStock/PreOrder, `image` = galeria, `brand` Clube do Mosaico). Sem `rel="sponsored"`: produto próprio. Seção 6 do contrato (sem contagem regressiva, sem selo inventado); miolo branco, coral só no preço e no botão. Cara de e-commerce.
- Arquivo `/loja/` e coleções `/loja/colecao/<termo>/`: grade de cartões (foto, título, preço, etiqueta de disponibilidade), filtro por coleção e técnica. Estado vazio honesto ("em breve") quando não há peça — nunca peça inventada.
- Página inicial ganha a faixa "Peças do ateliê" com as últimas 4–8 publicadas, quando houver. Sitemap e feed do Merchant Center (bloco 6) leem do CPT.

**(b) "Clube do Mosaico Ateliê — painel da artesã"** (a área dela, em `/atelie/`):
- **Login na própria página** (formulário do site com a identidade da ilha, `wp_signon` por baixo; "esqueci a senha" usa o fluxo nativo por e-mail). Papel `artesa`: só `edit/publish/delete` de `peca` próprias e `upload_files`. **Bloqueio duplo**: `admin_init` redireciona `artesa` para `/atelie/` se tentar o wp-admin, e `show_admin_bar` false para ela.
- **Tela inicial do painel**: "Olá, <nome>", botão grande **Nova peça**, e a lista das peças dela em cartões (foto, título, preço, status Publicada/Rascunho/Pausada) com Editar · Pausar/Publicar · Excluir (confirmação). Nada de menus do WordPress.
- **Formulário de peça**, em uma tela só, em português simples, com ajuda curta em cada campo: título · descrição (textarea simples, sem editor de blocos) · **fotos: área de arrastar-e-soltar com várias imagens de uma vez, miniaturas, arrastar para reordenar, a primeira é a capa, remover com um clique** (upload via `media_handle_upload`/REST `wp/v2/media` com nonce; redimensionar no cliente para máx. 2000 px antes de enviar) · preço · pronta entrega ou sob encomenda + prazo · medidas · peso · base · técnica · coleção · cores · quantidade. Botões **Salvar rascunho** e **Publicar**, com **pré-visualização** da página pública antes de publicar. Validação amigável (preço obrigatório, pelo menos 1 foto). Funciona no celular — ela vai fotografar e cadastrar do telefone.
- **Usuário da artesã criado pelo snippet** na primeira execução, se não existir: login `artesa`, e-mail **mina196@hotmail.com** (e-mail da própria artesã, dado pelo Raphael em 11/09/2026), papel `artesa`. **A senha NUNCA é escrita no repositório nem em log**: o snippet gera senha aleatória descartada e dispara `retrieve_password` para esse e-mail, então o link para criar a senha chega direto a ela. O e-mail de criação de senha do WordPress é **substituído** (filtros `retrieve_password_message` + `retrieve_password_title`) por um e-mail HTML em português, amigável, com o logo, o texto "Seu ateliê está pronto" e **um único botão grande "Criar minha senha e entrar"** (o link de redefinição), seguido de uma linha com o endereço do painel `https://clubedomosaico.com.br/atelie/`. Depois de definir a senha, o `login_redirect` do papel `artesa` leva a `/atelie/`, nunca ao wp-admin. O Raphael (raphaeh9@gmail.com) recebe cópia só de um aviso curto, "o acesso da artesã foi enviado", sem link de senha. Registrar no `ESTADO.md` que o e-mail foi enviado. Ela troca a senha em "Meus dados" dentro do painel.
- **MALHA AUTOMÁTICA POR PEÇA (requisito do Raphael, 10/09: "cada cadastro de produto já tem que estar pensado na arquitetura completa, vínculo de categorias + SEO + malha completa").** A artesã só preenche o formulário; **tudo abaixo o site faz sozinho no ato de publicar**, sem ela saber que existe:
  - **Categorias obrigatórias no formulário**: coleção (uso) e técnica são campos de escolha, não texto livre; base também. É isso que liga a peça ao resto do site. Sem coleção e técnica o botão Publicar não habilita.
  - **SEO da página da peça gerado dos campos**: `<title>` = "<título> — <coleção> em mosaico | Clube do Mosaico"; meta description a partir da descrição + técnica + medidas; canonical; slug limpo; `alt` de cada foto = "<título>, mosaico em <base>, foto N"; breadcrumb Início › Loja › <coleção> › <peça> (visível e em JSON-LD `BreadcrumbList`); `Product`+`Offer`; OpenGraph com a capa. Se ela editar, tudo se regenera.
  - **Links de saída (a peça aponta para 3 irmãs, regra da seção 9)**: (1) a coleção dela em `/loja/colecao/<uso>/`; (2) a página de técnica em `/tecnicas/<tecnica>/` e o tutorial "como fazer mosaico em <base>" em `/como-fazer/`; (3) as fichas do Guia dos materiais que a técnica e a base implicam (mapa fixo no snippet: base cerâmica → cola PU/silicone + rejunte; base vidro → silicone; base MDF → PVA + verniz; pastilha de vidro → ficha de pastilhas; etc.); (4) "peças parecidas": 4 peças da mesma coleção ou técnica.
  - **Links de entrada (mão dupla, nenhuma página órfã)**: a coleção lista a peça; a página da técnica e o tutorial ganham a faixa "peças do ateliê feitas assim"; a ficha de material ganha "peças feitas com este material"; a home mostra as últimas. Tudo por query do CPT — nada é escrito à mão.
  - **Sitemap e feed**: a peça entra em `wp-sitemap.xml` na hora (CPT público) e no feed `/feed-produtos.xml` do Merchant Center; ao pausar/excluir, sai dos dois e a página responde 410/redireciona para a coleção.
  - **Taxonomias com página própria e SEO**: `/loja/colecao/<uso>/` e `/tecnicas/<tecnica>/` têm título, descrição editorial (escrita pela Fundação, uma vez), grade das peças e links para os tutoriais e fichas correspondentes — são as páginas que miram "vaso centro de mesa", "presente artesanal", "mosaico bizantino".
  - **Regra de qualidade**: peça sem foto ou sem preço não publica; peça publicada nunca fica órfã (o teste da seção 8 verifica, para uma peça de teste, que ela aparece na coleção, na técnica, no tutorial da base e na ficha de material, e que a página dela linka de volta para os quatro).
- **Verificação obrigatória antes de `publicar: true`**: `php -l` nos dois; entrar em `/atelie/` como `artesa`, cadastrar uma peça de TESTE ("TESTE — apagar", 3 fotos) pelo formulário, publicar, abrir a página pública (carrossel, JSON-LD válido, botão do WhatsApp), pausar, excluir; confirmar que `artesa` em `/wp-admin/` é redirecionada para `/atelie/`; testar a 360 px de largura.

### ADENDO 3 — 11/09/2026 — LEADS DA LOJA ("Verificar disponibilidade")

> **CUMPRIDO em 13/09/2026 11h56Z** — snippet `clubedomosaico-leads.php` 1.0.0
> (snippet #11), `loja` 1.1.0, `atelie` 1.1.0, manifest na revisão 18, `/status`
> conferido em UM disparo. Saiu inteiro: o botão "Verificar disponibilidade", o
> formulário de dois campos, o CPT `lead_peca`, o e-mail imediato com o botão que
> abre a conversa **com o cliente**, a aba Interessados e o CSV. O texto abaixo
> fica como escrito, que é o que permite conferir o que foi entregue contra o que
> foi pedido; o que **mudou de forma e não de conteúdo** está declarado aqui:
>
> - **A mensagem pronta sai em português de conversa**, não com os rótulos do
>   adendo dentro da frase ("Ela está pronta, já feita." em vez de "Ela está
>   pronta entrega"). Os dados são os mesmos e nenhum é inventado — sem
>   disponibilidade gravada, a frase simplesmente não sai.
> - **O nome da artesã vem da option `cdm_artesa_nome`, que nasce vazia**, e não
>   do `first_name` da usuária. O Ateliê grava ali o texto de espera `Artesã`, e
>   ler dali faria a mensagem dizer "Aqui é Artesã" para uma cliente — o portão
>   pegou isso antes do ar. Enquanto a option estiver vazia a mensagem assina "do
>   Clube do Mosaico", que é o mesmo estado que a página Sobre já respeita.
> - **"Meus dados" continua fora**, como já estava: a option `cdm_email_leads`
>   existe e funciona, mas ainda não é editável por ela na tela. É o primeiro
>   item do próximo bloco.
>
> **A option `cdm_whatsapp` deixou de decidir se a peça tem como ser pedida.** O
> caminho de venda passou a ser o formulário, que não depende de número nenhum.

Decisão do Raphael em 11/09/2026. Faz parte do bloco 4d (Loja + painel) e vai no mesmo snippet "Clube do Mosaico Loja — peças e vitrine" ou num terceiro snippet "Clube do Mosaico Leads — verificar disponibilidade" (preferir o terceiro, para o Sync desembarcar separado).

**Na página da peça**, o botão principal (coral, único por tela) é **"Verificar disponibilidade"**. Ele abre um formulário curto, na própria página (modal ou bloco que desliza, sem sair da peça):
- Campos: **Nome** e **WhatsApp** (máscara BR, DDD obrigatório, guardar normalizado com DDI 55 — mesma regra de canonização usada na Real 21: `r21_wa_canonico`, para não duplicar lead por formato). Nada mais. Sem e-mail, sem CEP.
- Texto de consentimento obrigatório, abaixo do botão, no padrão de praxe: "Ao enviar, você autoriza o Clube do Mosaico a entrar em contato pelo WhatsApp sobre esta peça. Seus dados são usados só para esse atendimento e não são repassados a terceiros. Política de privacidade." Checkbox marcável, obrigatório; link para `/privacidade/` (página que a casca já cria).
- Botão do formulário: "Quero esta peça". Depois de enviar: mensagem "Pronto, {nome}! A artesã vai te chamar no WhatsApp para confirmar disponibilidade e prazo." e o nome da peça. Sem redirecionar.
- Honeypot + nonce + limite de 5 envios por IP/hora. Nunca gravar IP em texto puro além do necessário para o limite (hash).

**Gravação:** CPT interno `lead_peca` (show_ui false, sem página pública), metas: `_cdm_nome`, `_cdm_whatsapp` (canônico), `_cdm_peca_id`, `_cdm_origem` (URL da peça + UTM se houver), `_cdm_status` (`novo` → `contatado` → `vendido`/`perdido`), `_cdm_consentimento` (timestamp + texto exibido, para LGPD).

**Notificação por e-mail, a cada lead, imediata**, para **mina196@hotmail.com** (a artesã) — option `cdm_email_leads`, editável em "Meus dados" do painel `/atelie/`:
- Assunto: "Novo interessado: {nome da peça} — {nome do cliente}".
- Corpo HTML curto com o logo, a foto principal da peça, o nome da peça, preço e disponibilidade atuais, nome e WhatsApp do cliente, e **um botão grande "Responder no WhatsApp"** que abre `https://wa.me/55{whatsapp do cliente}?text={mensagem pronta}`. A mensagem pronta, em português e no tom da artesã, cita a peça específica: "Olá, {primeiro nome}! Aqui é {nome da artesã, ou 'do Clube do Mosaico' enquanto não houver nome} — vi que você se interessou pela peça *{nome da peça}*. Ela está {pronta entrega / sob encomenda, prazo de N dias}. Posso te passar os detalhes de pagamento e envio?". Use `rawurlencode`, quebra de linha `%0A`, sem emoji.
- Um segundo botão menor: "Ver a peça no site".
- Rodapé: "Este e-mail foi enviado pelo Clube do Mosaico porque um cliente pediu para verificar disponibilidade."
- Enviar por `wp_mail` com `From: Clube do Mosaico <contato@clubedomosaico.com.br>` e `Reply-To` vazio. Hotmail é rigoroso: a casca (bloco 3b) precisa criar a conta `contato@` no cPanel OU garantir SPF/DKIM do servidor para o domínio — registrar em `ESTADO.md` o que foi feito e testar o recebimento na Hotmail com um lead de teste marcado `_cdm_teste=1` (apagar depois). Se cair em spam, tratar como bloqueio da ilha, não como detalhe.

**No painel `/atelie/`:** aba "Interessados" com a lista dos leads (peça, nome, WhatsApp clicável em `wa.me` com a mesma mensagem pronta, data, status editável). É a segunda aba do painel, depois de "Minhas peças". Nada disso aparece no wp-admin para ela.

**Malha e SEO:** o formulário não muda o JSON-LD `Product` + `Offer` da peça (`availability` continua real). Não criar página por lead. `noindex` no que for endpoint.

**Quem recebe:** só a artesã (mina196@hotmail.com). O Raphael NÃO recebe cópia de lead, a não ser que a option `cdm_email_leads_copia` seja preenchida.

**CÓPIA DO DADO DA ARTESÃ — parte deste bloco, seção 24 do `ARQUIPELAGO.md`.** As peças que ela cadastra são o único dado do Arquipélago inteiro que não existe fora do banco do WordPress. Este bloco não fecha sem: (a) um endpoint de leitura protegido pelo mesmo token do Sync devolvendo JSON com todas as peças, seus metadados e as URLs das fotos; (b) a linha no `ESTADO.md` dizendo que a ronda diária passa a commitar `ilhas/clubedomosaico/dados/pecas.json`. O mesmo vale para `lead_peca`, com uma ressalva: o JSON dos leads **não vai para o repositório** — nome e WhatsApp de pessoa não entram em arquivo versionado. Para os leads, a cópia é a exportação CSV dentro do próprio painel, para a artesã baixar.

## DESPACHO DA SENTINELA — 12/09/2026

Ronda diária de 12/09/2026, 14h43Z, no navegador do Raphael. Primeira ronda desta ilha (`ultima_ronda` era `null`). Foram abertas as 11 URLs, conferidos os 50 links internos, executadas as duas ferramentas com entradas reais e recalculados à mão os 12 exemplos pré-renderizados da F1.

**Nenhum defeito da lista fechada 19.1 apareceu, então esta ronda não fez conserto nenhum** (`dados/consertos.md` criado com essa constatação). O que passou limpo, para a Fundação não refazer: as 11 URLs e os 50 links internos em 200; nenhuma página órfã (toda URL do sitemap com 2 ou mais links internos apontando para ela); zero `&#038;` dentro de `<script>` nas 11 páginas; JSON-LD em todas e `BreadcrumbList` em todas menos a home, que é o certo pela 16.3; favicon próprio servido; `aria-expanded` e `aria-controls` no botão de menu; nenhuma imagem sem `alt`; corpo sem metadado no começo; tabelas de exemplo presentes no HTML servido; estado com parâmetro em `noindex, follow` com canonical para o endereço limpo; console sem uma mensagem sequer; `/status` na revisão 11, igual à do manifest; e nenhuma palavra da lista "Proibidas" do `VOZ.md` em título, `h1` ou primeiro parágrafo de nenhuma das 11 páginas. A aritmética foi conferida à mão e está toda certa: os 12 exemplos da F1 (área, contagem e gramas), as duas contas rodadas ao vivo (disco de 50 cm com pastilha de 2 cm, folga de 4 mm, 6 mm de espessura e 15% de sobra → 1.963 cm², 393 pastilhas, 825 g a 4,20 kg/m²; e o caso-âncora do vaso de 15 × 20 → 942 cm², 720 pastilhas, 264 g a 2,80 kg/m²), a tabela de comparação com a obra (0,74 e 1,40 kg/m² nas duas linhas de obra, e os múltiplos 3,8× e 2,0×), a tabela da placa (o passo é o lado dividido pela raiz do número de pastilhas, e as quatro linhas batem) e a recusa de calcular gramas para acrílico e epóxi.

**OS DOIS ITENS FORAM CUMPRIDOS em 12/09/2026** (F1 1.1.0, F2 1.1.0, manifest na revisão 12, `/status` com revisão 12 às 15h51Z, em UM disparo). O texto deles saiu daqui; o que a ronda MEDIU E APROVOU fica acima, como linha de base para a próxima. **A ronda seguinte confere, que quem constrói não aprova o próprio conserto** — e o que ela precisa saber está abaixo.

Os dois eram de **coerência da recomendação** (seção 12), e tinham a mesma raiz: a página falava de menos produtos do que listava, ou nomeava a causa errada por quem ficou de fora. Por isso o conserto não foram dois remendos, e sim **uma regra**, que subiu para o `ARQUIPELAGO.md` seção 7 e vale para toda ilha: **todo item do banco é nomeado exatamente uma vez em cada resposta** — na frase que o recomenda, e aí ele está na vitrine, ou numa linha que diz por que ele não está — e **o bloco de compra serve exatamente o que a frase nomeia**.

O que mede isso agora, e onde olhar se voltar: `ferramentas/teste-prestacao-rejunte.php`, com régua própria recomputada dos `perfis_esperados_do_rejunte` escritos à mão (nunca chamando `cdm_f2_celula_rejunte()`), varrendo 540 estados da F2, 180 da F1 e as 9 linhas da tabela pré-renderizada, um processo por estado; e `ferramentas/mutacoes-prestacao.py`, cujas duas primeiras mutações são os dois defeitos deste despacho escritos de volta. No ar: 231 afirmações medidas por `conferir-no-ar.py`, incluindo as 6 combinações que o item 1 nomeia e os 5 nomes do banco contados um a um nas respostas do item 2.

**Três coisas que o conserto descobriu e que valem para a próxima ronda:**
- **A F1 afirmava sobre o banco inteiro o que valia só para um tipo.** `strtok( $rotulo, ' —' )` cortava no primeiro espaço e devolvia só "Rejunte", então a frase saía "Nenhum rejunte do nosso banco…" onde cabia "Nenhum rejunte cimentício…". Metade do defeito era essa, e nenhuma leitura do código a mostrava — só a tela.
- **"Faixa não obtida" não é "a folga não cabe", e as duas ferramentas confundiam as duas.** O rejunte piscinas não tem faixa publicada; dizer que ele não cobre 4 mm é afirmar sobre uma declaração que ninguém leu. Agora ele tem linha própria nas duas telas e na tabela.
- **Havia um grupo que a F2 nunca imprimia**: o de produto sustentado só por fonte fraca. Vazio hoje, invisível para sempre no dia em que enchesse. A mutação que o mede precisa **produzir o mundo** (rebaixar a fonte no banco E no perfil escrito à mão), senão passa sem medir nada.

Nada mais nesta ronda.

### DESPACHO DO RAPHAEL — 24/09/2026 — ENTRADA NO FOCO: MEDIR ANTES DE CONSTRUIR

> **ESTADO DESTE DESPACHO EM 25/09/2026, 14h0xZ, pela 18.3 — FALTA SÓ O BLOCO A. OS BLOCOS 0, B, C e D SAÍRAM.**
>
> **BLOCO B — CUMPRIDO E CONFERIDO NO AR** (18.4). `/author/mosaico_gestor/` serve `noindex, follow`, numa
> etiqueta só, e continua fora do sitemap; as 17 URLs do sitemap continuam **sem** `noindex`, medido nas duas
> direções por portão. O caminho foi o filtro `wp_robots`, como o bloco manda, nunca uma tag em paralelo.
>
> **E ELE ACHOU UM DEFEITO MAIOR, QUE JÁ ESTAVA NO AR:** quatro lugares desta ilha imprimiam a própria
> `<meta name="robots">` num `wp_head` paralelo — a casca, a F1, a F2 e o Leads —, e o WordPress imprime a
> dele. O resultado servido eram **DUAS etiquetas**, medido em `/materiais/como-sabemos/` e no estado com
> parâmetro de `/materiais/qual-cola-usar-no-mosaico/`, que é a **melhor página desta ilha**. Nenhum portão
> daqui via: todos mediam SE a frase `noindex` aparecia, nenhum media QUANTAS etiquetas apareciam. A casca
> 1.13.0 abriu `cdm_fora_do_indice` e agora quem imprime é ela, uma vez. **Detalhe que vale mais que o
> conserto:** a F2 explicava, três linhas acima do próprio `echo`, por que NÃO imprime o canonical — *"serviria
> DOIS canonicals (...) sujo numa página cujo propósito inteiro é ter UM endereço no índice"* — e fazia
> exatamente isso com a etiqueta de robô.
>
> **BLOCO C — CUMPRIDO.** A varredura está em `dados/indexacao.md` e a ferramenta é
> `ferramentas/varrer-canonicas.py` (com `--autoteste`, 11 casos fabricados, porque passada limpa em portão que
> nunca acusou nada não prova nada). **71 URLs lidas, 71 em "esperado, nenhuma ação", 0 defeito.** Nenhuma
> correção aplicada, como o bloco manda.
>
> **O ACHADO DO BLOCO C, e ele muda como esta ilha se mede:** o rastreador **nunca recebe redirecionamento**.
> O WordPress redireciona `www`, barra final e a home em `http` — e **o cache de página responde 200 antes**,
> porque o Googlebot não manda quebra de cache. Em 36 das 71 URLs as duas leituras discordam. Isso explica o
> primeiro motivo do e-mail ("Página alternativa com tag canônica adequada", e é comportamento esperado) e
> **não** explica o segundo: a fonte provável de "Página com redirecionamento" é a vida anterior do domínio,
> e a lista só existe dentro do Search Console. **O pedido de acesso à conta `sentinela@` continua de pé e é o
> que destrava de verdade.**
>
> **O QUE ISSO CUSTA A QUEM MEDIR ESTA ILHA:** `conferir-no-ar.py` gruda `?v=<agora>` em toda URL — e está
> certo, porque nasceu para provar que o Sync aplicou a revisão nova. O preço é que **ele nunca vê o que o
> visitante vê**. Cache servindo página velha para gente de verdade passa por baixo das 488 afirmações dele
> sem encostar em nenhuma.
>
> **DE PASSAGEM, UMA BANCADA VERMELHA QUE NÃO ERA DESTE DESPACHO:** `teste-f1` (2 falhas) e `teste-f2` (1)
> estavam vermelhos no `main` desde as 10h40Z, e com eles **duas baterias de mutação se recusavam a rodar**
> ("a F1 de verdade já está reprovada — conserte antes de mutar"). A causa era a própria melhora daquela
> execução: os treze itens de pastilha subiram do degrau 4 para o 3, e as réguas cobravam, com número fixo,
> que estivessem no 4. Consertado derivando o degrau do banco em vez de cravá-lo, e produzindo o degrau 4 num
> mundo novo (`so_crua=1`) em vez de esperá-lo do banco. **Os dois voltaram a verde e as duas baterias
> voltaram a rodar: `mutacoes-f1` 46/46 e `mutacoes-f2` 50/50, nenhuma passando.**
>
> **O QUE FALTA, E É SÓ ISTO:** o **BLOCO A**, que **espera 30/09** por ordem do próprio despacho — o veredito
> é de 08/10 e trocar título antes do número de 30/09 misturaria duas causas na mesma janela.

Esta ilha entrou em FOCO em 24/09/2026 por decisão do Raphael. A ordem das coisas aqui é o contrário do de sempre: **a primeira passada com foco não cria página nenhuma.** Esta ilha já tem tráfego e já tem três páginas na primeira página — o próximo ganho não vem de URL nova, vem de consertar o cano e de fazer o clique acontecer. Só a passada SEGUINTE abre malha, e sob o teto da 21.4 (máximo 10 URLs por leva, máximo 3 levas por semana) e com `piso: abaixo` (17 de 40 URLs).

#### ~~BLOCO 0 — O `sub_id` DESLOCADO. Antes de tudo.~~ — **CUMPRIDO em 25/09/2026 às 10h40Z**

Estava gravado como `-clubedomosaico-F2--`: deslocado uma casa, `sub_id_1` vazio. Eram 16 links nascidos
no painel `offer/custom_link` com os cinco campos preenchidos a mão — e mão humana em cinco caixas de
texto não tem portão. Agora são 31 links gerados por API, com a casa provada em bancada. O detalhe do
conserto está na abertura deste despacho, no `REGISTRO.md` de 25/09 e em `dados/consertos.md`.

#### BLOCO A — CTR das três páginas que já estão na primeira página

`/materiais/qual-cola-usar-no-mosaico/` (posição 7,8, 17 impressões), `/materiais/quantas-pastilhas-para-mosaico/` (9,1, 9 impressões), `/como-fazer/o-que-e-mosaico-picassiete/` (7,0, 3 impressões). **Zero clique nas três.** Consultas nomeadas: `cola para mosaico` (posição 10,0) e `picassiete` (6,0); 28 das 30 impressões vêm anonimizadas pela Search Console.

- Pela 12.1, banda de 4 a 10 é **trabalho de CTR, não de conteúdo**: título que promete o número, meta que promete a faixa e a fonte.
- **NÃO REESCREVER O CONTEÚDO dessas três páginas.** Posição conquistada não se mexe: reescrever corpo de página que já rankeia é risco sem retorno.
- Gravar em `dados/posicoes.md` o título e a meta ANTES da troca, na mesma linha da série, para haver com o que comparar depois.
- A 12.1 manda comparar o CTR com a média das outras na mesma posição. Com 30 impressões **não há com o que comparar** — isso fica ESCRITO, não estimado.
- O veredito é de **08/10** (duas semanas de série), não de 30/09. Não declarar vitória nem derrota na leitura de 30/09.

#### ~~BLOCO B — `/author/mosaico_gestor/` indexada~~ — **CUMPRIDO em 25/09/2026 às 13h29Z, casca 1.13.0**

Já há despacho da Sentinela de 23/09 sobre isso. O que este parágrafo acrescenta é uma **lição trazida da Aquametria**, e ela muda o caminho técnico:

- **NÃO adicionar uma segunda meta robots.** O WordPress já imprime a meta pelo `wp_robots` (com aspas simples), e uma tag injetada em paralelo gera **meta duplicada** — o problema fica pior que o original e mais difícil de achar.
- O caminho é o **filtro** (`wp_robots`, ou o filtro do plugin de SEO), nunca uma tag em paralelo.
- Sair do sitemap também, não só `noindex`.
- Conferir no ar depois: a página tem de servir UMA meta robots, com `noindex`, e o `conferir-no-ar` tem de reprovar se aparecerem duas.

#### ~~BLOCO C — os dois motivos do Search Console~~ — **CUMPRIDO em 25/09/2026 às 13h4xZ**, em `dados/indexacao.md`. O pedido de acesso do `sentinela@` ao Search Console CONTINUA ABERTO e é o único item deste bloco que depende do Raphael

E-mail do Search Console de qua., 23/09/2026, 14h26 BRT, propriedade **clubedomosaico.com.br**, dois motivos novos:

1. "Página alternativa com tag canônica adequada"
2. "Página com redirecionamento"

**PRIMEIRO, O AVISO QUE EVITA TRABALHO INVENTADO: os dois motivos são, na esmagadora maioria dos casos, COMPORTAMENTO ESPERADO — não defeito.** Canônica apontando para a versão boa e redirecionamento que redireciona para o lugar certo são o Google fazendo o trabalho dele. A tarefa é **verificar e relatar**, não "consertar".

**SEGUNDO, O QUE ESTA NUVEM NÃO ALCANÇA:** a conta de serviço `sentinela@` **não tem acesso** a `sc-domain:clubedomosaico.com.br` — só a aquametria e a robometria (está em `dados/search-console-2026-09-23.md`). Então **não invente a lista de URLs do relatório** e não escreva "verificado" sobre URL que você não abriu. O que é possível fazer sem a Search Console, e é o que deve ser feito nesta passada:

- Varrer as **17 URLs do sitemap** mais `/author/mosaico_gestor/` e, para cada uma: ler o `<link rel="canonical">` servido e seguir a cadeia de redirecionamento (código HTTP, destino, número de saltos).
- Classificar cada URL em DUAS listas, em `dados/indexacao.md`:
  - **"esperado, nenhuma ação"** — canônica aponta para a própria URL ou para a página certa; redirect de URL antiga para a nova, ou de variação para a canônica.
  - **"defeito, com a correção proposta"** — canônica de página de conteúdo apontando para a home; paginação ou variação de filtro canonicalizada para o lugar errado; **URL que está no sitemap e redireciona** (o sitemap não deve listar URL que redireciona); redirect para a home em vez da página equivalente; cadeia com mais de um salto.
- **NÃO APLICAR CORREÇÃO NESTA PASSADA.** O que for defeito volta como PROPOSTA, URL por URL, com o valor atual e o valor proposto, para o Raphael autorizar item por item.
- **PEDIDO AO RAPHAEL, que é o que destrava de verdade:** dar acesso à conta de serviço `sentinela@` na propriedade `sc-domain:clubedomosaico.com.br` no Search Console (Configurações, Usuários e permissões, adicionar; leitura basta). Enquanto isso não existir, indexação e posição desta ilha só podem ser lidas no navegador dele, e a série de 30/09 vai ter a mesma nota de rodapé da de 23/09.

#### ~~BLOCO D — correção de cabeçalho, de passagem~~ — **CUMPRIDO em 24/09/2026 às 19h33Z**

`urls_publicadas` passou de 13 para **17**, contado no `wp-sitemap.xml` no ar: 12 em `wp-sitemap-posts-page-1.xml` e 5 em `wp-sitemap-posts-peca-1.xml`, listadas uma a uma no `REGISTRO.md`. `primeira_indexacao` continua `desconhecida`, como o bloco manda.

*(A contagem só foi possível porque o sitemap voltou a existir: às 19h20Z ele servia 404. Ver a abertura deste despacho.)*

#### O QUE NÃO FAZER NESTA ENTRADA

- Não criar bloco de malha antes do retrato de medição estar escrito.
- Não mexer em conteúdo de página que já rankeia.
- Não aplicar correção de canônica ou de redirect sem autorização item por item.
- Não escrever número de Search Console que esta nuvem não conseguiu ler.
- A 21.4 continua valendo, e o piso da rampa (40 URLs + 21 dias desde a primeira indexação) continua `abaixo`.

## FILA DE BLOCOS

**Leia a seção 14 do `ARQUIPELAGO.md` antes de montar a fila: tudo existe para indexar e chegar à primeira página.** A ordem abaixo já aplica a regra de intenção de compra (seção 9): fichas de material e peças antes de tutorial genérico.

### O QUE ESTÁ DESBLOQUEADO AGORA, em 14/09/2026 às 23h19Z — leia antes de escolher bloco

1. ~~**A SEGUNDA PÁGINA DE TÉCNICA: o trencadís.**~~ **ENTREGUE em 14/09/2026 às 23h19Z**, em `/como-fazer/o-que-e-trencadis/` (técnicas **1.1.0**, manifest na revisão 35). A pergunta que este item deixava em aberto — "duas grades ou uma?" — **não foi escolhida, foi medida**: o snippet calcula uma grade por caquinho e agrupa as idênticas, as duas do trencadís saem iguais nas 45 células, e a página serve uma tabela **dizendo na tela que comparou as 90 e por quê**. A causa está na régua da F2 e vale para as próximas: **o caquinho entra na decisão num lugar só**, a condição de superfície porosa, e os dois cacos são porosos. Está tudo na seção 4b do `ARVORE.md`, com a comparação dos seis caquinhos do vocabulário. **Com isso o eixo das técnicas está SEM PRÓXIMA PÁGINA** — as duas que o portão autoriza já nasceram, e a terceira depende do item 2 abaixo. **A semana da 21.4 está em 2 de 3 levas** (uma URL cada).
2. **AS TRÊS TÉCNICAS QUE SEGUEM EM ZERO** (direto, indireto, bizantino) **não são trabalho de texto, e sim de FONTE.** Cada uma tem o `motivo_sem_materiais` escrito dizendo por que não declara material. O bizantino é o de maior valor de indexação da ilha e o mais distante; o indireto tem uma faixa de banco descoberta com nome próprio: **a cola hidrossolúvel que o método exige não existe nos 7 itens do banco de colas.**
3. **A COLETA DAS CATEGORIAS VAZIAS** — eram quatro (`alicate`, `base`, `acabamento`, `apoio`) e **restam DUAS**: a `alicate` saiu de zero em 25/09/2026 às 16h43Z (6 itens) e a `acabamento` às 19h16Z do mesmo dia (7 itens). Continua sendo o que destrava o bloco **4c**, e nenhuma coleta de cola ou de rejunte a fecha. Está medido em `dados/cobertura.json` e explicado na seção 7b do `ARVORE.md`. O canal de busca alcança; o egresso direto aos domínios de fabricante, não. **`base` e `apoio` são as duas que sobram, e nenhuma das duas tem a linha do esquema que autoriza enchê-la sem decisão nova** — a `acabamento` também não tinha, e a decisão dela está em `regras_da_categoria_acabamento` do `dados/esquema-banco.json` (versão 4), que serve de molde para as outras duas.
4. **A LINHA DA PEÇA NA TABELA DO `ARVORE.md`** — seção 5 daquele arquivo diz exatamente o que falta, e é conserto de TESTE, não de documento.

**1. CORPUS DE BUSCAS.** `dados/corpus-buscas.md` com os três clusters (materiais/ferramentas · peças prontas · aprender), faixa, concorrência, CPC e a classificação de SERP por consulta (aberta / tomada / armadilha). A base já está na memória; complete com autocomplete e buscas relacionadas. Não depende de infraestrutura.

**2. ESPECIFICAÇÃO DAS DUAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`:
- **F1 Calculadora de pastilhas e rejunte** — entrada: forma da peça (cilindro/vaso, placa, esfera, tampo redondo), medidas, tamanho da pastilha (1×1, 2×2, 2,5×2,5 cm, tessela irregular), junta; saída: área, quantidade com sobra, gramas de rejunte e de cola, tabela pré-renderizada com 12 peças típicas.
- **F2 Seletor de cola e rejunte** — entrada: base (cerâmica, vidro, MDF, cimento, plástico, parede), material da pastilha, ambiente (interno/externo/molhado); saída: tipo de adesivo (PVA, silicone, PU, argamassa ACII/ACIII, epóxi), rejunte compatível, cura. Constante só com fonte de fabricante (Quartzolit, Tekbond, Loctite, Cascola) e data. Sem fonte, `pendente` e fora de fórmula publicada.

**3. MODELO DO BANCO.** Três entidades, todas com `imagem` desde já: **MATERIAL** (categoria, tipo, medida, material, embalagem, `afiliado.programa`/`afiliado.url` vazios até a Sentinela preencher) · **PEÇA** (CPT `peca` no WordPress, cadastrada pela artesã no painel `/atelie/`: nome, técnica, base, medidas, peso, cores, preço, disponibilidade, prazo, fotos — nunca inventada) · **TÉCNICA** (bizantino, direto, indireto, opus).

**3b. CASCA DO SITE** — só depois que o WordPress existir. Seção 6 do contrato com a paleta acima. Páginas: início, loja, materiais, como-fazer, sobre, contato, divulgação de afiliados. Logo: ver regra no topo. **Cabeçalho CLARO (papel `#FFFFFF`) e rodapé escuro, miolo branco** — *esta linha dizia "cabeçalho e rodapé pretos", que é o mundo anterior a 11/09/2026 e contradizia a regra do topo deste arquivo, o `DESIGN.md` e o `VOZ.md`: o wordmark dentro do logo é vinho `#69030C` e some no preto, e foi isso que sumiu com o logo em 11/09. Corrigido pelo Pente Fino em 14/09/2026.*

**4. FERRAMENTAS**, cada uma com JSON-LD, tabela pré-renderizada, resposta antes da explicação, procedência na frase e vitrine (4e) desde a primeira. **A ordem é F2 e depois F1** — quem mandou foi o bloco 1, e a razão está no `dados/especificacao-calculadoras.md`: quem busca cola está com o vaso na mão e a cola errada no carrinho.

- **F2 — ENTREGUE e no ar em 11/09/2026**, em `/materiais/qual-cola-usar-no-mosaico/` (snippet `clubedomosaico-f2.php` **v1.1.0**, casca 1.5.0, manifest na revisão 12). Primeira ferramenta e primeira página de nível 3 da ilha. A resposta é servida pelo SERVIDOR — o formulário é um GET para a própria página e não existe uma linha de decisão em JavaScript —, a elegibilidade é recomputada das declarações dos fabricantes pelas regras do `dados/esquema-banco.json`, e o estado com parâmetro sai com `noindex, follow` e canonical para o endereço limpo. O que mede isso é `ferramentas/teste-f2.php` (69 afirmações, varrendo os 45 estados de cola e os 60 de rejunte, um processo cada) e `ferramentas/mutacoes-f2.py`.
- **F1 — ENTREGUE e no ar em 12/09/2026**, em `/materiais/quantas-pastilhas-para-mosaico/` (snippet `clubedomosaico-f1.php` **v1.1.0**, casca **1.6.0**, manifest na revisão 12). Segunda ferramenta e segunda URL de nível 3. A geometria (área por forma, com o cone pela **geratriz**) e a contagem pelo passo são aritmética da ilha e não dependem de banco; os gramas saem da fórmula publicada pela Quartzolit com o coeficiente **lido do banco**, e a ferramenta **recusa** calcular para acrílico e epóxi — a correção do bloco 3c, na tela. A régua do rejunte é a da F2, chamada daqui em vez de reescrita. Mede isso `ferramentas/teste-f1.php` (67 afirmações, régua aritmética própria, um processo por estado, varrendo forma × caquinho, folga × tipo, sobras, espessuras, lugares e as bordas) e `ferramentas/mutacoes-f1.py` (27 de 27). Desde 12/09 a prestação de contas do rejunte tem portão próprio nas duas ferramentas: `ferramentas/teste-prestacao-rejunte.php` e `ferramentas/mutacoes-prestacao.py` (despacho da Sentinela de 12/09).
  **O que ela custou e vale ser lido antes do próximo bloco:** a página nasceu **404** com o Sync dizendo revisão 10 e seis itens aplicados. A casca só remontava a estrutura quando a **versão dela** mudava, e o filtro `cdm_paginas` — criado na 1.5.0 justamente para a ferramenta se registrar sozinha — ficava inerte. A F2 escapou porque nasceu junto com a 1.5.0. Casca **1.6.0**: a chave de remontagem virou a versão **mais** um resumo do mapa de páginas. **Toda ferramenta ou página nova daqui em diante nasce sozinha depois do Sync** — e o portão 21b do `teste-casca.php` mede o mecanismo, nunca a versão.

**4c. FICHAS DE CATEGORIA DE MATERIAL** — /materiais/pastilhas, /alicates, /colas, /rejuntes, /bases, /acabamento: comparativo, "qual escolher para quê", vitrine. É a primeira leva que vai ao índice junto com F1 e F2.

**4d. LOJA** — ver DESPACHO de 10/09 acima: cadastro de peças é área da artesã no WordPress (snippet de CPT `peca`), não `dados/pecas.json`. Coleções por uso (/loja/centro-de-mesa, /loja/presentes, /loja/jardim) e por técnica listam as peças publicadas. Antes de existir peça cadastrada, as coleções ficam com estado vazio honesto ("em breve"), nunca com peça inventada.

**5. TUTORIAIS-ÂNCORA**, 12: vaso, cachepot, tampo de mesa, quadro, espelho, mandala, filtro de barro, parede, número de casa, colar, bizantino, iniciante. Cada um com lista de materiais (Guia) e "prefere pronto?" (Loja). Marcar `revisao_tecnica: pendente` até a mãe do Raphael revisar.

**5b. MALHA**, em levas de 5 a 10 guiadas por indexação. Página só nasce com 3 itens de banco reais e um número calculado (seção 9).

**6. FEED DE PRODUTO** para Google Merchant Center (listagens gratuitas) a partir do CPT `peca` — snippet que serve `/feed-produtos.xml`. Só quando houver peça publicada.

**7. LISTA DE PROSPECÇÃO DO WIDGET** (F1 incorporável): escolas e ateliês de mosaico, blogs de artesanato, lojas de material sem conteúdo. `publicar: false`.

## Específico desta ilha
- O dado que é o produto da ilha: a **compatibilidade cola × base × ambiente** e a **quantidade por peça**. Errar aí faz a peça descolar ou faltar material — é a confiança que separa a ilha da lojinha.
- Programas de afiliado: **Shopee** (conta única do Arquipélago; Sub_id 1 = `clubedomosaico`, Sub_id 2 = código da página: `F1`, `F2`, `G-PASTILHAS`, `G-ALICATES`, `G-COLAS`, `T-VASO`…) e **Mercado Livre** (etiqueta `clubedomosaico<codigo>`, tudo junto e em minúsculas: `clubedomosaicof1`, `clubedomosaicof2` — *a forma com hífen que ficava aqui é recusada pelo painel do ML, medido em 13/09/2026; ver seção 7 do `ARQUIPELAGO.md`. Corrigido pelo Pente Fino em 14/09/2026*). Amazon só com tráfego.
- Enquanto falta infraestrutura: blocos 1, 2 e 3 não dependem de site. Não invente peça para preencher a Loja.

## DESPACHO DO RAPHAEL — 12/09/2026, 18h20 BRT — O ATELIÊ TEM DE ESTAR DE PÉ AMANHÃ

> **CUMPRIDO em 12/09/2026 23h20Z, e VERIFICADO no ar** — os cinco itens do corte
> saíram, o e-mail de acesso foi enviado às **23h13m23s Z**, e o fechamento inteiro
> está em `dados/despachos.md`. O texto original fica abaixo porque a 18.4 manda:
> despacho fechado nunca é apagado.
>
> **A metade do portão que a Fundação NÃO pode cumprir, e por quê:** a senha da
> artesã não existe em lugar nenhum a que a nuvem tenha acesso — o snippet a gera
> aleatória e a descarta sem imprimir, e o que chega a ela é um link na caixa dela.
> Não há como entrar como `artesa`, e fabricar um jeito seria quebrar a única coisa
> que protege a conta de uma pessoa de verdade. A metade da **janela de 360 px** foi
> cumprida num Chromium (91 medições, `teste-navegador-atelie.mjs`), e foi ela que
> achou os botões de foto com 38 px. O que resta é humano: confirmar a chegada do
> e-mail na Hotmail e o dedo dela na tela.
>
> **Para a próxima execução:** não há mais despacho aberto nesta ilha. A option
> `cdm_whatsapp` está vazia e é o primeiro item da fila, de uma linha; depois o
> adendo 3 inteiro (`lead_peca`), que era o corte de hoje.

Ele vai à casa dos pais **no domingo, 13/09**, e quer ensinar a própria mãe a entrar no site e cadastrar as peças dela. É a primeira vez que alguém de fora da máquina vai usar o que a gente construiu, e é a mãe dele. **Isto fura tudo** (seção 18.1: despacho aberto do Raphael vence qualquer rotação).

### O CORTE — o que entra hoje e o que NÃO entra
O bloco 4d inteiro não cabe numa noite, e tentar tudo é a forma mais segura de não entregar nada. **Entregue este mínimo, inteiro e funcionando; o resto do 4d continua na fila para depois de domingo.**

**ENTRA (nesta ordem, e cada peça só depois da anterior estar de pé):**
1. **CPT `peca`** e o papel `artesa`, com as capacidades da especificação (só as próprias peças, `upload_files`), e o bloqueio duplo do wp-admin.
2. **O usuário da artesã e o e-mail de acesso** — login `artesa`, e-mail `mina196@hotmail.com`, senha aleatória descartada e `retrieve_password` disparado, com o e-mail HTML em português, o logo e o botão único "Criar minha senha e entrar". **Este item é o que precisa estar feito mais cedo**, porque o e-mail tem de chegar hoje e ele quer poder conferir antes de sair de casa. Escreva no `ESTADO.md` a hora exata do envio.
3. **`/atelie/` — login e tela inicial**: formulário de login com a cara da ilha, "Olá, <nome>", botão grande **Nova peça**, e a lista das peças em cartões com Editar e Publicar/Pausar.
4. **Formulário de peça, uma tela só**, em português simples: título · descrição · **fotos (várias de uma vez, miniaturas, a primeira é a capa)** · preço · pronta entrega ou sob encomenda + prazo · medidas · base · técnica · coleção. Salvar rascunho e Publicar. **Tem de funcionar no CELULAR** — ela vai fotografar e cadastrar do telefone, e é assim que ele vai ensinar amanhã.
5. **A página pública da peça**: fotos, título, preço, medidas, disponibilidade, botão de WhatsApp, `Product`+`Offer`, breadcrumb. E `/loja/` listando o que estiver publicado.

**NÃO ENTRA HOJE — e não é esquecimento, é escolha:** o formulário "Verificar disponibilidade" e o CPT `lead_peca` (adendo 3), o feed do Merchant Center, as páginas de técnica, os textos editoriais das coleções, "peças parecidas" e a malha completa da peça. Tudo isso volta à fila depois de domingo. **Se faltar tempo, corte de baixo para cima nesta lista de 1 a 5, nunca pelo meio.**

### O PORTÃO, que aqui vale mais que o de sempre
Antes de dar por pronto: entre em `/atelie/` como `artesa`, **numa janela de 360 px de largura**, cadastre uma peça de teste com 3 fotos, publique, abra a página pública, volte, pause e apague. Se qualquer passo exigir saber o que é WordPress, **não está pronto** — ela nunca viu um painel de CMS, e o objetivo é que ela não precise ver.

### O que escrever no `ESTADO.md` ao fechar
A hora do envio do e-mail para `mina196@hotmail.com`, o que dos cinco itens saiu, o que ficou de fora, e **uma frase que o Raphael possa ler no domingo de manhã dizendo se ele pode ou não ensinar a mãe hoje**. Se não deu, diga que não deu — ele prefere saber antes de chegar lá do que descobrir na frente dela.

## DESPACHO DO RAPHAEL — 14/09/2026 — A ARTESÃ USOU O ATELIÊ, E ACHOU QUATRO COISAS
### FECHADO ÀS 21h17Z DE 14/09/2026 — os quatro itens saíram às 11h18Z e a página do Picassiete, que era o que sobrava, foi ao ar e foi conferida

**A mãe do Raphael recebeu o e-mail, criou a senha, entrou e cadastrou a primeira
peça do Arquipélago** — "Quadro flores do campo", quatro fotos, R$ 500, pronta
entrega. O ateliê funcionou de ponta a ponta com uma pessoa de verdade. Os quatro
itens que ela encontrou usando foram cumpridos e verificados no ar em 14/09/2026
(ateliê 1.3.0, loja 1.2.0, casca 1.9.2, manifest na revisão 30, `/status` com revisão 30); o que
cada um era, o que estava errado e como foi medido está no `REGISTRO.md` desta
execução. **Um resumo de uma linha por item, e só para não voltarem a eles:**

1. **O 404 ao publicar — CUMPRIDO, e a causa NÃO era a hipótese do despacho.** A
   regra de reescrita estava de pé (`/loja/quadro-flores-do-campo/` respondia 200
   antes de qualquer conserto). Era **colisão de nome**: o painel carregava o id em
   `?peca=`, e `peca` é o tipo de conteúdo, registrado com `query_var` — para o
   núcleo `/atelie/?peca=24` é "a peça de slug 24", que não existe. O parâmetro
   virou `cdm_peca`. **Atingia SETE voltas do painel, não só publicar.** A faixa de
   "Peça publicada!" com "Ver no site" e "Cadastrar outra peça" está no lugar do
   404. Medido no ar: `/atelie/?cdm_peca=999999` responde 200.
2. **"Escolha" — CUMPRIDO.** Toda lista do painel abre com
   `<option value="" disabled hidden selected>Selecione…</option>`. Coleção e
   técnica ganharam `required`, com frase do painel e não do navegador; o botão de
   rascunho ganhou `formnovalidate`, senão guardar o que ela digitou passaria a
   depender de ela ter decidido a coleção. No servidor a régua já existia.
3. **Picassiete — CUMPRIDO na lista.** A rota pública `/v1/loja` dizia `tecnica: 4` e
   agora diz **5**. O que faltava não era a linha: era a **versão da Loja**, que é
   quem manda criar os termos. Trincadís fica. A distinção entre os dois está na
   ajuda do campo. **A página `/tecnicas/Picassiete/` NÃO nasceu — veja abaixo.**
4. **O carrossel — CUMPRIDO, com código nosso.** Miniaturas quadradas por
   `aspect-ratio`, foto grande em 4:5, setas de 44 px com `aria-label`, ampliar em
   `<dialog>` nativo com X, `Esc` e clique fora, e zoom por `transform`. Zero
   biblioteca, zero busca em JavaScript, tudo sobre o HTML já servido. Os tokens
   nasceram no `DESIGN.md` antes do código, como a 22.6 manda.

**O QUINTO ITEM — a página do Picassiete — SAIU ÀS 21h17Z DE 14/09/2026, e o
despacho está FECHADO.** Conferido pela 18.4, abrindo a URL no ar e não o
repositório: `https://clubedomosaico.com.br/como-fazer/o-que-e-mosaico-picassiete/`
responde 200, manifest na revisão 34, `/status` na 34 em UM disparo com 12
aplicados, e `ferramentas/conferir-tecnica-no-ar.py` aprova com 23 afirmações
sobre o HTML servido — inclusive a comparação do endereço canônico com o mesmo
endereço sem cache, que é a trava do cache do hospedeiro.

**O ENDEREÇO NÃO É O QUE O DESPACHO PEDIU, e a diferença tem regra por trás.**
Você escreveu `/tecnicas/Picassiete/`; a página nasceu em
`/como-fazer/o-que-e-mosaico-picassiete/`. Dois motivos, nenhum de gosto: a
seção 16.1 do contrato proíbe página solta na raiz desde 11/09 (só home, sobre,
contato, divulgação de afiliados e privacidade moram lá), e o slug é a **consulta
que a pessoa digita** — é assim que as duas ferramentas desta ilha já vivem. A
categoria `/como-fazer/tecnicas/` só nasce com três filhas (16.5) e mover a URL
depois de a página posicionar é proibido pela 12.1, então o endereço de hoje
pendura na mãe que já existe. Está tudo na `ARVORE.md`, seção 4b.

**E O QUE DUAS EXECUÇÕES TINHAM DADO COMO IMPOSSÍVEL ERA ERRO DE LEITURA, NÃO
FALTA DE DADO.** As execuções de 11h18Z e 18h45Z de 14/09 responderam que a
página não podia nascer, cada uma com número na mão, e os **três** portões que
elas mediram decidiam errado: um contava caco de prato (que não tem fabricante)
quando o que a página recomenda é a **cola** do caco — são cinco, com link e
declaração datada; outro cobrava a 16.5 de uma página que nasce filha direta; e
o terceiro dizia que "nenhum número autoriza leva nova", que é o **oposto** do
que a seção 21.1 manda para ilha abaixo do piso. Esse terceiro virou regra nova
do Arquipélago (21.8), porque é a segunda ilha a lê-lo ao contrário.

**O que a página entrega, e é o que faltava na fila da Escola:** a resposta de
"com o que colar caquinho de louça" nas 45 combinações de superfície e lugar,
servida no HTML e recalculada da declaração dos fabricantes a cada
carregamento — 11 delas dizendo, com todas as letras, que não há resposta. E ela
se **recusa** a responder o rejunte, dizendo a causa que mediu.

**A taxonomia `tecnica` continua `public => false`**, e agora por uma razão que
não é mais o portão de dado: é o orçamento de rastreamento (decisão 4 do snippet
da Loja, 12/09). A página da técnica não é o arquivo da taxonomia — é página de
conteúdo, escrita e medida uma a uma.

**E O QUE SÓ UMA PESSOA PODE MEDIR, que fica escrito como o que falta e nunca como
conferido:** o **dedo dela na galeria nova**, num telefone. A Fundação mediu o HTML
servido, as marcas do `wpautop`, os `aria-label`, a proporção das fotos e as
âncoras das miniaturas; **ninguém tocou a tela**. Mesma metade humana do bloco do
ateliê, e pela mesma razão.

**A consequência boa que o despacho previu ACONTECEU:** `dados/pecas.json` nasceu
com a peça de verdade dentro (seção 24). O campo `gerado_em` da rota fica de fora da
cópia de propósito — com ele dentro, toda passada da ronda viraria um commit, e a
24.2 manda commitar só quando o JSON mudou.
## ESCLARECIMENTO DO RAPHAEL — 14/09/2026 — TRINCADÍS FICA; PICASSIETE É ADIÇÃO
O trincadís é o mosaico tradicional de caquinho, quebrado com torquês. Nunca foi para sair da lista.
O Picassiete usa louça quebrada (pratos, xícaras) misturada ao caquinho. É técnica própria, entrou como `picassiette`.
Observação registrada para decisão futura: o campo "técnica" hoje mistura MÉTODO (direto, indireto) com ESTILO (bizantino, trincadís, Picassiete). São dois eixos diferentes, e a artesã pode marcar um e achar que marcou o outro. Não mexer agora; anotar como dívida de modelagem.
Grafia definida pelo Raphael em 14/09/2026: **Picassiete**, palavra única, sem hífen. A chave interna continua `picassiette`; só o rótulo visível mudou.

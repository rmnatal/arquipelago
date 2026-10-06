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
>
> **E DESDE 29/09/2026 SÃO DOIS COMANDOS, porque o primeiro nunca viu a borda.** `conferir-no-ar.py`
> gruda `?v=<agora>` em toda URL: todas as 508 afirmações dele medem a **origem**. Quem lê como o
> Google lê — sem quebra de cache — é `python3 ferramentas/leitura-do-visitante.py .`, e ele fecha
> **REPROVADO** hoje, por **1 defeito que é do hospedeiro e não desta ilha**: toda URL inexistente
> responde 404 na 1ª leitura e **200 na 2ª**, por 2 horas, com o corpo do 404 (soft 404). **Vermelho
> esperado, com dono escrito no `ESTADO.md`** — não é regressão sua, e não se conserta daqui. O que
> **não** pode acontecer é ele ficar vermelho por **outro** motivo: aí é defeito novo.

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

## DESPACHO DA SENTINELA — 2026-10-05 (RONDA DIÁRIA TÉCNICA, 14h55Z) — TRÊS ITENS; OS DOIS DA FUNDAÇÃO ESTÃO FECHADOS, SÓ O 3 FICOU

> **ESTA RONDA ESCOLHEU A clubedomosaico PELA REGRA DA DÍVIDA (seção 12):** ela é a única ilha com publicação
> nova desde a última ronda — o `ultima_execucao` do cabeçalho é de **hoje, 14h05Z**, e o sitemap foi de 17 para
> **21 URLs** com a mãe `/materiais/acabamento/` e as três filhas. Código novo é onde mora defeito. A aquametria
> e a robometria receberam **sonda de vida** (porta de entrada e contagem de sitemap), e as duas estão de pé:
> `/`, `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/` em 200 com o tipo certo, caminho inexistente em 404, e
> sitemap com 52 URLs na aquametria e 14 na robometria.

**RECONFERÊNCIA DA 19.4(c), ANTES DE QUALQUER OUTRA COISA.** As **oito** entradas de `dados/consertos.md` foram
abertas primeiro e reconferidas no ar, com quebra de cache e `Accept-Encoding: identity`:

- **24/09 — a porta de entrada (29.2): PASSOU pela quarta ronda seguida.** 21 de 21 URLs do `wp-sitemap.xml` em
  **200**; `/wp-sitemap.xml` em 200 com `application/xml` e XML de sitemap de verdade; `/robots.txt` em 200 e
  `text/plain`; `/wp-json/` em 200 e `application/json`; caminho inexistente em **404 na página desta ilha**.
- **05/10 — o reparo do `.htaccess` das 10h17Z: PASSOU.** É a mesma medição acima, e ela é a reconferência que a
  entrada de hoje pediu. **Pela 19.4(b), se cair uma terceira vez o caminho é o chamado na HostGator, não um
  terceiro reparo** — e o chamado já está na lista de ABERTOS de `dados/despachos.md`.
- **25/09 — os links regerados: PASSARAM.** **35** links de loja servidos nas 21 URLs, **todos** presentes no
  banco (`url` ou `url_busca`), **zero** encurtador desconhecido e **zero** link cru de Shopee ou Mercado Livre.
- **25/09 — a etiqueta de robô: PASSOU, e hoje em CINCO alvos, um deles novo.** `/author/artesa/` — que nasceu
  com as páginas de peça e é linkado das **cinco** pelo bloco "Escrito por" — serve **uma**
  `<meta name='robots' content='noindex, follow' />`, igual a `/author/mosaico_gestor/`,
  `/materiais/como-sabemos/` e `/?s=cola`. E **zero** `noindex` indevido nas 21 do sitemap.
- **29/09 — o soft 404 na borda: CONTINUA**, e segue sendo do Raphael (item 2 do despacho de 30/09).
- **28/09 — OS CINCO ITENS ESTÃO FECHADOS, e dois deles foram medidos hoje pela primeira vez desde que fecharam:**
  a **unidade dobrada** (`46x36cm cm`) tem **zero** ocorrência nas 21 URLs, na vitrine, na página da peça e no
  `description` do `Product` no JSON-LD; os **estados com parâmetro da F1** servem `noindex`; as 21 servem
  `<meta name="description">` e **nenhuma** passa de 160 caracteres; **zero** `afiliado.degrau` em `null` em 41
  de 41 itens com bloco de afiliado; e o **`alt` das imagens de `/loja/`** está certo — a foto de destaque e as
  cinco do carrossel de cada peça têm `alt` descritivo ("Bandeja em madeira — trencadís (caquinho), foto 3"), e
  as únicas que restam com `alt=""` são as **miniaturas de 150×150 da tira**, duplicata decorativa da imagem já
  rotulada ao lado. **Miniatura decorativa com `alt` vazio é correto e não é defeito** — a contagem de 22 não
  deve voltar a ser relatada como pendência.
- **30/09 — o item 1 CONTINUA cumprido:** **17 de 17** itens de degrau 4 com `motivo_sem_ficha` na forma da
  25.4-b.3, com a causa separada da última tentativa pelo marcador.

**O QUE ESTA RONDA MEDIU E PASSOU, para a Fundação não remedir:** 21 de 21 URLs em **200**; **zero** `&#038;`
dentro de `<script>` nas 21 (contado só nos blocos `<script>`, como a seção 12 manda); **zero** página órfã —
toda URL com 2 ou mais links internos apontando para ela, a mais pobre com 2; JSON-LD nas 21 e `BreadcrumbList`
nas 20 que não são home, com os **quatro** níveis certos nas três filhas novas; breadcrumb **visível**
(`nav.cdm-trilha`, com `aria-current="page"` no nível atual) nas 20; **zero** `<img>` sem `width`/`height`;
`aria-expanded` e `aria-controls` nas 21; nenhuma palavra da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>`
ou primeiro parágrafo das 21; **console sem uma mensagem**, com recarga, em `/materiais/acabamento/` e em
`/materiais/acabamento/impermeabilizar-peca-de-mosaico/`; `/status` na **revisão 56**, igual à do
`manifest.json`. **Malha da 16.4 fechada na categoria nova:** a mãe lista as três filhas com âncora na consulta
de cada uma ("selar a base antes de fazer mosaico: precisa de selador?"), e cada filha linka a mãe **e as duas
irmãs** em bloco "Veja também", mais o seletor de cola no corpo.

**AS DUAS FERRAMENTAS FORAM EXECUTADAS COM ENTRADA REAL E A CONTA REFEITA NA MÃO:**

- **F1 (quantas pastilhas)**, entrada nova — `forma=disco&d=30&pastilha=p25&esp=4&junta=4&sobra=15&rejunte=epoxi&onde=externo_exposto`
  → **707 cm² (0,071 m²)**, **passo 2,9 cm**, **1.189 pastilhas/m²**, **97 pastilhas para comprar**. Confere:
  π × 15² = 706,86 cm²; 2,5 + 0,4 = 2,9 cm; 10.000 ÷ 2,9² = 1.189,1; 706,86 ÷ 8,41 = 84,05 pastilhas, com 15%
  de sobra = 96,66, arredondado para cima = **97**. **Os cinco números batem.** O rejunte epóxi sai como "a
  gente não calcula para esse", com o motivo publicado — e isso é a regra funcionando, não defeito.
- **F2 (qual cola)**, `base=espelho&onde=externo_exposto&caco=caco_espelho&junta=3` → **Tekbond Silicone
  Neutro**. Conferido no banco na mão: `espelhos` está em `declaracoes.indicado_para` e `chuva` e `raios UV` em
  `resistencias_declaradas`. **Nenhuma contradição:** o produto recomendado **não** aparece na própria lista de
  "o que não usar", que nomeia o Acético Construção pelo motivo publicado. Coerência da recomendação conferida
  lendo como leitor leria, não por régua.

**TESTE DE VIDA DOS LINKS (25.4 e 25.4-b), do navegador do Raphael, sem gastar um clique de afiliado:**
**10 de 24 itens com `url_produto` medidos — 10 VIVOS, 0 morto, 0 esgotado — e 14 NÃO MEDIDOS.** Os **4** do
Mercado Livre `/p/MLB...` foram abertos no navegador e os quatro estão vivos com preço (R$ 59, R$ 81, R$ 19,
R$ 76), nenhum pausado. Dos **20** da Shopee, **6** responderam `item_status: "normal"` pela API de ficha, com
o título batendo com o registro; os outros 14 não foram medidos pelo motivo do **item 3** abaixo. **"Não medido"
não é "vivo", e esta ronda não vai escrever que é.** **Piso da 25.2: 41 de 41** itens com bloco de afiliado têm
`url_busca` **e** `url_busca_produto`. **Itens intestáveis (com `url` e sem `url_produto`): ZERO.**

---


> **ESTADO DESTE DESPACHO EM 05/10/2026 às 16h4xZ, pela 18.3 — OS ITENS 1 E 2 SAÍRAM E SÓ O 3 FICOU, QUE NÃO É DA FUNDAÇÃO.**
> Os dois itens acionáveis estão **CUMPRIDOS e conferidos contra o critério de pronto que eles mesmos declararam**
> (18.4). O texto deles foi substituído pelo fecho, logo abaixo, e não apagado: o que a próxima execução precisa
> ler não é o defeito, é a escolha que o item 2 exigia e **a metade dele que NÃO virou régua, com o número que
> mostra por quê**. O **item 3** fica inteiro, porque ele mesmo se declara método endereçado ao Raphael — e com
> ele fica a consequência: **nenhuma ronda deve escrever "N de N vivos" sobre um banco que não conseguiu varrer.**
>
> **E UM ACHADO DE CARONA QUE VALE MAIS QUE O ITEM 1, para a próxima execução não repetir:** o atraso de
> desembarque não era do rejunte. **13 sha estavam vencidos no manifest, dez deles de commits de HOJE** — a manhã
> inteira parada, com o `bloco_atual` de 13h18Z dizendo "nenhum Sync acionado" e deixando o conserto para quem
> viesse depois. **Quem fecha bloco publicável aciona o Sync na mesma execução**, mesmo quando o bloco "só mexeu
> em dado": dado desta ilha É página, porque as ferramentas leem o banco.

---

### ~~1. O BANCO SABE E O SITE NÃO: SETE DAS NOVE CÉLULAS DE REJUNTE DA F2 ESTÃO ERRADAS NO AR~~ — **CUMPRIDO em 05/10/2026 às 16h36Z, manifest e `/status` na revisão 57**

**Os quatro critérios de pronto que o item declarou foram medidos um por um no ar, com quebra de cache:** (a)
`/status` em **revisão 57**, `ultimo` **2026-10-05 16:36:21**; (b) a entrada de `junta=6` em
`contato_permanente_agua` deixou de dizer "Não temos rejunte para indicar" e agora serve *"o rejunte é **Rejunte
Piscinas Quartzolit**"*, com *"Cobre junta de 2 a 10 mm"* e a declaração de uso submerso citada — **a célula que
estava VAZIA passou a ter recomendado**; (c) a frase "a gente não conseguiu a faixa de junta" tem **zero**
ocorrência em `junta=3`, `junta=5` e `junta=6`; (d) `junta=3` lista *"Rejunte Epóxi Quartzolit **e** Rejunte
Piscinas Quartzolit — o fabricante nomeia este lugar nos dois"*.

**O DIAGNÓSTICO DO ITEM ESTAVA CERTO E A CAUSA ERA UMA SÓ:** commit sem Sync não é entrega. Nada no banco
precisou mudar — a faixa de 2 a 10 mm já estava no `main` desde a manhã, do boletim de agosto de 2017.

**A NOTA DE PAPEL QUE O ITEM DEIXOU CONTINUA VALENDO, e ela não se fecha daqui:** a ronda **tentou** acionar o
Sync e foi **recusada pelo ambiente dela** como *deploy em produção*; daqui, no papel de Fundação, o mesmo
acionamento passou. **Enquanto for assim, a 19.1 e a 19.3 são letra morta para a Sentinela em todo defeito que
dependa de desembarque** — ela vai despachar em vez de consertar, e isso não é falha dela. Segue em "Precisa do
Raphael" no `dados/PAINEL.md`.

---

### ~~2. `quartzolit-rejunte-acrilico` ESTÁ NO `degrau: 2` COM UMA URL DE ANÚNCIO DE VENDEDOR NA SHOPEE~~ — **CUMPRIDO em 05/10/2026, com portão novo; e UMA METADE DELE NÃO VIROU RÉGUA, com o número**

**A ESCOLHA, que pela 19.2 era da Fundação:** o `degrau` desceu para **3** com o
`por_que_este_degrau_da_25_1` escrito, em vez de trocar o `url_produto` por uma `/p/MLB...` do Mercado Livre. O
motivo é medido: a **25.4-b.1** manda reescolher o par **inteiro** — `url` e `url_produto` da mesma oferta, na
mesma chamada — e o **item 3 deste mesmo despacho** acabou de medir que o anti-robô fecha a sessão em 4 a 6
fichas. **Rotular o que o link É está sempre disponível; casar um catálogo que ninguém conferiu, não.**

**O critério de pronto do item, cumprido:** `validar-banco.py` reprova registro cujo `degrau` seja 2 sem
`url_produto` de catálogo do Mercado Livre e, rodado no banco desta ilha, imprime **zero** reprovação. **O degrau
2 saiu de 5 para 4**, e a escada fecha **1:1 2:4 3:19 4:17** em 41.

**O PORTÃO NOVO É A TERCEIRA CAMADA DA MESMA FAMÍLIA** (28/09: o degrau tem de estar escrito; 30/09: o degrau 4
diz por que parou ali; **05/10: o degrau escrito tem de DESCREVER a URL ao lado dele**). A régua é a **forma da
URL**, nunca a prosa ao lado dela: degrau 2 exige a `/p/MLB...` (nas **duas** formas legítimas, com rótulo no
caminho e na curta sem rótulo), reprova o `produto.mercadolivre.com.br/MLB-..._JM` que a 25.1 nomeia, e degrau 3
exige `url_busca`. **Mais a metade silenciosa do achado:** a mesma `shop_id` da Shopee não pode carregar dois
degraus, porque ser loja oficial do fabricante é propriedade da **loja** e não do produto. Hoje: **15 lojas da
Shopee lidas, 0 com mais de um degrau**. Bateria `ferramentas/mutacoes-forma-do-degrau.py`: **5 de 5 reprovadas,
4 só pelo portão novo, 0 falso positivo** — e ela é a primeira entre as irmãs a medir falso positivo, porque a
primeira régua escrita exigia o rótulo no caminho da URL e **reprovaria catálogo de verdade** na forma curta.

**O QUE ESTE CONSERTO NÃO MUDOU, dito porque a tentação é dizer que mudou:** **nenhum snippet lê
`afiliado.degrau`** (conferido nos oito), e a vitrine da F2 desempata por presença de `url`. O item corrigiu a
**verdade do banco** e a contagem que mede durabilidade — **não um pixel do que o site serve**.

#### A METADE QUE NÃO VIROU RÉGUA, E O NÚMERO QUE MOSTRA POR QUÊ — leia antes de pedir de novo

O item pedia também que o validador **reprovasse `etiqueta_ml` não nulo com `programa` diferente de
`mercadolivre`**. **Essa régua não entrou, e não é esquecimento.**

**Contado antes de escrever régua: 21 dos 41 registros** do banco estão assim — 4 colas, **13 pastilhas** e 4
rejuntes. A régua reprovaria **21**, e o próprio critério de pronto do item (*"rodado no banco desta ilha,
imprimir zero reprovação"*) seria **inalcançável**.

**E o campo não é defeito: é rótulo pré-atribuído.** A **seção 7** diz *"uma etiqueta por par ilha × ferramenta"*
— `clubedomosaicof1` e `clubedomosaicof2` são as etiquetas das **duas ferramentas desta ilha**, não de um
programa. E o `REGISTRO.md` de **13/09/2026** guarda a decisão: o validador cobrava a forma
`clubedomosaico-<codigo>`, **impossível de criar**, e **23 registros foram corrigidos de propósito** para a forma
sem hífen, **nos dois programas**. **Zerar o campo num registro só o tornaria o único incoerente dos 21.**

Isto é a **19.2** funcionando como ela promete — *"sintoma não é causa; quem vê o sintoma costuma errar a
causa"*. O despacho **acertou o degrau**, que era defeito de verdade e caro, e leu a etiqueta ao lado dele como
parte do mesmo defeito. Era outra coisa. Registrado aqui pela **19.6**, para a decisão não ficar no silêncio.

---

### 3. O TESTE DE VIDA DA 25.4 PAROU DE COBRIR UMA RONDA INTEIRA, E ISTO É MÉTODO, NÃO DEFEITO DESTA ILHA

**Não é trabalho da Fundação e não é defeito do site.** Está aqui para a próxima ronda não gastar a execução
redescobrindo, como a 25.4 avisa que acontece.

**O QUE FOI MEDIDO HOJE, no navegador do Raphael, entre 14h2xZ e 14h4xZ:**

- Abrir `https://shopee.com.br/` direto **cai no anti-robô na hora**: a aba é levada para
  `shopee.com.br/verify/captcha?...&scene=crawler_item`.
- Chamar `https://shopee.com.br/api/v4/pdp/get_pc?...` **como URL de aba** devolve
  `{"is_login":true,"error":90309999,"redirect_to_error_page":true}` — a sessão existe e o anti-robô recusa.
- De dentro de uma aba **já numa ficha de produto** (`/product/<shop_id>/<item_id>`), o `fetch` para
  `/api/v4/pdp/get_pc?shop_id=…&item_id=…&detail_level=0` com `X-API-SOURCE: pc`,
  `X-Shopee-Language: pt-BR` e `X-Requested-With: XMLHttpRequest` **funciona** — 200, `error: null`,
  `item_status` e `title` de verdade. **Mas só nos primeiros 4 a 6 chamados daquele contexto.** Do quinto ou
  sexto em diante vem `error: 90309999`, e a aba é redirecionada para
  `shopee.com.br/verify/traffic?...&scene=crawler_item`, o que mata qualquer laço em andamento.
- Abrir uma ficha nova para zerar o contador **deixou de funcionar na terceira tentativa**: a quarta aba já
  respondeu `90309999` no primeiro chamado. O limite escalou para a sessão, não para a página.
- **Dois erros de método, medidos e escritos para ninguém repetir:** (a) `fetch` com um header `af-ac-enc-dat`
  vazio devolve **403** mesmo dentro da ficha — não invente header; (b) chamar `/api/v4/item/get` ou
  `/api/v4/pdp/get_rw` **aciona o anti-robô na hora** e queima o contexto. **Só `pdp/get_pc`.**
- E uma observação que **não** vira régua: na ficha de produto o `document.title` chega por um instante com o
  nome real do produto antes de voltar para o genérico "Shopee Brasil | Ofertas incríveis…". **A 25.4 proíbe usar
  o `<title>` como teste e continua certa** — isto é frágil e some em milissegundos.

**A Sentinela é proibida de resolver CAPTCHA (25.4), então não há o que tentar daqui.** O resultado honesto desta
ronda é **6 de 20 itens da Shopee medidos** (todos `normal`: `acrilex-verniz-acrilico-brilhante`,
`acrilex-verniz-acrilico-fosco`, `acrilex-verniz-acrilfix-brilhante`, `quartzolit-verniz-protetor-para-pisos`,
`quartzolit-borracha-liquida-elastica`, `suvinil-seladora-para-madeira`) e **14 não medidos**:
`coral-selador-acrilico`, `coral-resina-acrilica`, `cortag-torques-mosaico-roldanas`,
`cortag-torques-azulejista-corte-reto`, `vonder-vdec-51`, `vonder-vdec-75`, `vonder-vdec-90`,
`tekbond-silicone-acetico-construcao`, `cascola-cascorez-extra`, `tekbond-silicone-acetico-maxx`,
`quartzolit-rejunte-ceramicas`, `quartzolit-rejunte-porcelanatos-e-ceramicas`, `quartzolit-rejunte-acrilico`,
`quartzolit-rejunte-piscinas`.

**O QUE ISSO CUSTA, dito sem maquiar:** com 4 a 6 itens por sessão, um banco de 20 fichas na Shopee precisa de
**três a quatro rondas** para ser varrido uma vez, e a cicatriz de 13/09 foi **quatro links mortos em menos de
doze horas**. A escolha de quais itens testar primeiro deixa de ser detalhe: a 25.4 manda começar pelos que a
ferramenta mais recomenda e pelos que nunca foram testados, e com teto de 6 isso passa a ser a regra inteira.

**O que seria preciso, e é decisão do Raphael, não da Fundação:** ou a Open API de Afiliados (25.6) passa a
responder o estado do anúncio — ela já é chamada para encurtar, e aí o teste sai do navegador e vira rotina de
nuvem —, ou a 25.4 ganha a linha que diz quantos itens por ronda são possíveis e em que ordem. **Enquanto não
houver uma das duas, nenhuma ronda deve escrever "N de N vivos" sobre um banco que ela não conseguiu varrer.**

**REGISTRO, NÃO DEFEITO (seção 12, RECEITA):** em `/materiais/acabamento/` e em
`/materiais/acabamento/selar-a-base-antes-de-fazer-mosaico/`, o `quartzolit-fundo-selador` — que está no degrau 4
e serve só a busca — aparece em **segundo** lugar, acima do `suvinil-seladora-para-madeira`, que tem ficha. **Não
viola a 25.2-b**, porque o link de busca é rastreável e rende; e o **primeiro** item das duas listas tem ficha,
então a régua da RECEITA não dispara. Fica escrito porque o topo é o espaço mais caro da página e a ordenação é
escolha da Fundação (19.2).

## DESPACHO DA SENTINELA — 2026-09-30 (RONDA DIÁRIA TÉCNICA, 14h53Z) — UM ITEM NOVO; OS QUATRO DE 28/09 RECONFERIDOS NO AR E CONFIRMADOS

> **ESTADO DESTE DESPACHO EM 30/09/2026 às 16h3xZ, pela 18.3 — O ITEM 1 SAIU E NÃO SOBROU NADA PARA A FUNDAÇÃO.**
> O **item 1** está CUMPRIDO e conferido contra o critério de pronto que ele mesmo declarou (18.4): o validador
> imprime `degrau 4 com motivo escrito: 17 de 17`, reprova a forma errada, e a bateria nova fecha 10 de 10 só pelo
> portão novo. O detalhe ficou escrito no lugar do item, e não apagado, porque o erro que a execução cometeu no
> caminho — um classificador que media a ordem das travas e devolveu 17 de 17 na mesma classe — é a parte que a
> próxima execução precisa ler.
>
> **ATUALIZADO EM 02/10/2026 às 11h5xZ:** o item 1 continua cumprido e nada nele foi tocado. O que mudou neste
> arquivo hoje é de despacho mais antigo e de prioridade maior — o **BLOCO A** do despacho do Raphael de 24/09 e o
> **item 4 (metade)** do despacho de 28/09, os dois fechados com a janela de medição de 30/09. **O item 2 abaixo
> segue aberto e segue não sendo da Fundação.**
>
> O **item 2** (soft 404 na borda) continua aberto e **não é trabalho da Fundação**: é camada de cache do
> hospedeiro, está com o Raphael desde 29/09 e hoje foi medido também na robometria. `leitura-do-visitante.py`
> segue fechando **REPROVADO por esse único defeito**, que é vermelho esperado com dono escrito.
>
> **E um pedido NOVO ao Raphael saiu deste item, medido e não inventado:** 13 dos 17 registros do degrau 4 são as
> pastilhas e os 13 esperam a decisão do `tipo_de_casamento: "equivalente"`. Está em `dados/despachos.md`, na
> lista de ABERTOS.

**RECONFERÊNCIA DA 19.4(c), antes de qualquer outra coisa.** As quatro linhas de `dados/consertos.md` foram abertas primeiro e reconferidas no ar, com quebra de cache:

- **24/09 — a porta de entrada (29.2): PASSOU pela segunda ronda seguida.** As 17 URLs do `wp-sitemap.xml` em **200**; `/wp-sitemap.xml` em 200 com `application/xml` e XML de sitemap de verdade; `/robots.txt` em 200 e `text/plain`; `/wp-json/` em 200 e `application/json`; e um caminho inexistente respondendo **404 na página desta ilha**, não na do hospedeiro.
- **25/09 — os links regerados: PASSOU.** Os 38 itens do banco seguem com `url_busca` encurtada e `sub_id_1 = clubedomosaico`; nenhum encurtador desconhecido servido nas páginas medidas.
- **25/09 — a etiqueta de robô: AGORA PASSA NOS 5 ALVOS.** A metade que falhou em 28/09 (os estados com parâmetro da F1) foi conferida hoje com os nomes de campo reais: `?base=ceramica_esmaltada_porcelana`, `?base=ceramica_esmaltada_porcelana&caco=caco_louca`, `?base=xxx` (valor inválido), `?caco=caco_vidro&junta=3` e os quatro campos juntos servem `<meta name='robots' content='noindex, follow' />`, **uma** etiqueta cada. O mesmo na F2 (`?forma=cilindro&d=20`, `?forma=conico&d=20&h=30`, `?l=30&a=20`). **O item 2 do despacho de 28/09 está fechado.**
- **29/09 — o soft 404 na borda: CONTINUA, e deixou de ser problema de uma ilha só.** Ver o item 2 abaixo.

**O QUE ESTA RONDA MEDIU E PASSOU, para a Fundação não remedir:** **17 de 17** URLs do sitemap em HTTP 200; `/status` na **revisão 52**, igual à do `manifest.json`; **console sem uma mensagem** (com recarga) em `/materiais/qual-cola-usar-no-mosaico/`; **zero** `&#038;` dentro de `<script>` nas 17; **zero** página órfã (toda URL com 2 ou mais links internos apontando para ela); **zero** `noindex` indevido; JSON-LD presente nas 17; `BreadcrumbList` nas 16 que não são a home; **zero** `<img>` sem `width`/`height` e **zero** `<img>` sem `alt`; as 17 servindo `<meta name="description">`; nenhuma frase da lista "Proibidas" do `VOZ.md` em `<title>`, `<h1>` ou primeiro parágrafo. As 22 imagens com `alt=""` são as miniaturas da tira das 5 páginas de `/loja/`, cujo `alt` vazio é deliberado e correto — a contagem já tinha sido corrigida em 28/09 e **continua certa**.

**AS DUAS FERRAMENTAS FORAM EXECUTADAS COM ENTRADA REAL E A CONTA FOI REFEITA NA MÃO:**
- **F2 (qual cola)**, `base=mdf_madeira&onde=externo_exposto&caco=caco_louca&junta=3` → recomenda **Tekbond Silicone Neutro**, com a declaração do fabricante citada ("a Tekbond escreve madeira entre as superfícies deste produto; declara também chuva e raios UV"). **Nenhuma contradição**: o bloco "o que não usar em MDF ou madeira" nomeia a Tekbond Silicone Acético Construção pelo motivo publicado (superfícies porosas), e o rejunte sai como "não temos rejunte para indicar com 3 mm de junta no sol e na chuva", um a um, com o motivo de cada exclusão. Coerência da recomendação conferida lendo como leitor leria, não por régua.
- **F1 (quantas pastilhas)**, `forma=cilindro&d=20&h=30&pastilha=p20&esp=4&junta=2&sobra=10&rejunte=cimenticio&onde=interno_seco` → **1.885 cm², 429 pastilhas, 264 g de rejunte, 2.066 pastilhas/m², passo 2,2 cm**. Confere na mão: π × 20 × 30 = 1.885,0 cm²; passo 2,0 + 0,2 cm → 4,84 cm² por pastilha → 389,5 pastilhas, com 10% de sobra e arredondamento para cima = **429**; 10.000 ÷ 4,84 = **2.066**/m²; 1,40 kg/m² × 0,1885 m² = **263,9 g ≈ 264 g**. **Os cinco números batem.**

**TESTE DE VIDA DOS LINKS (25.4 e 25.4-b), do navegador, sem gastar um clique de afiliado:** **21 de 21 itens com `url_produto` VIVOS**, 0 morto, 0 esgotado. **17 da Shopee** pela API de ficha (`api/v4/pdp/get_pc`, `item_status: normal` nos 17, título batendo com o registro) e **4 do Mercado Livre** (`/p/MLB...`) abertos no navegador, os quatro com botão "Comprar agora" e preço; a expressão "Sem estoque" que aparece no HTML dos dois rejuntes/durepoxi é o **texto de erro do seletor de quantidade**, não o estado do anúncio — medido e descartado. **Piso da 25.2: 38 de 38** com `url_busca`; **10 de 10** chaves de busca medidas com resultado (de 42 a 5.913 ofertas), inclusive a `cascola adesivo de montagem pl500`, que em 28/09 tinha caído no desvio para CAPTCHA. **Itens intestáveis: ZERO** — nenhum item do banco tem `url` sem `url_produto`.

#### ~~1. DOZE DOS DEZESSETE ITENS DE DEGRAU 4 NÃO DIZEM POR QUE PARARAM NO DEGRAU 4~~ — **CUMPRIDO em 30/09/2026 às 16h3xZ, manifest e `/status` na revisão 53**

**Conferido contra o critério de pronto que o próprio item declarou (18.4), e ele era medível por portão:** o
`validar-banco.py` imprime **`degrau 4 com motivo escrito: 17 de 17`**, e reprova registro no degrau 4 sem ficha
cujo `motivo_sem_ficha` não esteja na forma da 25.4-b.3 — `CAUSA (<classe>): ... || ULTIMA TENTATIVA
<AAAA-MM-DD>: ...`, a causa que não muda separada por marcador da tentativa que se reescreve a cada passada.
Bateria `ferramentas/mutacoes-motivo-degrau-4.py`: **10 mutações, 10 reprovadas, as 10 só pelo portão novo.**
Esquema do banco na **v9**.

**O motivo foi MEDIDO, não escrito de cabeça.** `ferramentas/medir-degrau-4.py` desceu a escada inteira pela Open
API para os dezessete, com a regra de `casar-anuncio.py` importada. Ela não grava `url` em nenhuma hipótese, e é
por isso que pôde medir as treze pastilhas que o `coletar-shopee.py` exclui por decisão pendente do Raphael:
**medir não é agir**, e foi por confundir os dois que elas passaram dezessete dias carregando a frase "elas nem
foram tentadas".

**A REPARTIÇÃO, que era o que o item pedia — e a 25.4-b.4 previa duas causas, a medição achou três:**

| causa medida | quantos | de quem é |
|---|---|---|
| `marca-nao-anunciada` | **13** | **do Raphael.** Nenhuma oferta da escada traz a marca; os degraus por código e por nome comercial devolvem zero. Pede a decisão do `tipo_de_casamento: "equivalente"`, não trava melhor |
| `candidato-barrado-nome` | **2** | nossa — `quartzolit-protetor-para-fachadas`, `cortag-torques-azulejista-corte-curvo` |
| `candidato-barrado-variante` | **2** | nossa — `quartzolit-fundo-selador`, `cascola-pl500-adesivo-de-montagem` |

**E O ERRO DA PRÓPRIA EXECUÇÃO, que vale mais que o item:** a primeira versão do classificador decidia a causa
pela trava que barrou o candidato e devolveu **17 de 17 na mesma classe** — exatamente o número que não diz nada
de que este item reclamava. As cinco travas de `casar.compativel` correm **em ordem** e a 5b quase sempre falha
antes de qualquer trava de irmão ser avaliada: **"nenhuma trava de irmão foi acionada" media a ordem do código,
não o mundo.** O que separa as causas é a trava 1 — algum anúncio traz a marca? O relato inteiro está no
`REGISTRO.md` de 30/09 e a repartição em `dados/links-afiliado-pendentes.md`.

### 2. O SOFT 404 NA BORDA CONTINUA, E HOJE ELE FOI MEDIDO TAMBÉM NA ROBOMETRIA — a pendência deixou de ser desta ilha

**Não é item novo desta ilha e não é da Fundação.** Está registrado desde 29/09 em `dados/consertos.md` e depende do Raphael, porque a camada de cache do hospedeiro responde antes do PHP. **O que mudou hoje é o alcance**, e isso muda o diagnóstico: a mesma sonda, rodada em duas URLs virgens por ilha, quatro leituras cada, deu **404 · 200 · 200 · 200** na clubedomosaico **e na robometria** (`x-server-cache: true`, `cache-control: max-age=7200`, corpo de 404 da própria ilha), e **404 · 404 · 404 · 404** nas duas sondas da **aquametria**. **Não é defeito de uma ilha: é a camada de borda, e a aquametria é a exceção que prova.** O pedido ao Raphael passa a valer para as duas ilhas, e está no `dados/PAINEL.md`. Esta linha existe aqui só para a próxima ronda não a redescobrir.

## ~~DESPACHO DA SENTINELA — 2026-09-28 (RONDA DIÁRIA TÉCNICA, 15h10Z)~~ — **FECHADO INTEIRO EM 02/10/2026 às 11h5xZ**: os cinco itens cumpridos e conferidos no ar, o meio item que faltava incluído

> **REESCRITO PELA 18.3 em 28/09/2026 às 17h0xZ, pela execução das 16h17Z que o resolveu.** O despacho tinha
> CINCO itens. Os itens **1, 2, 3 e 5 estão CUMPRIDOS e conferidos no ar** pela 18.4 — cada um contra o critério
> de pronto que ele mesmo declarou — e saíram daqui. O item **4 está cumprido pela metade**, e a metade que falta
> está escrita abaixo com o motivo. Nada foi apagado sem verificação; o relato inteiro, com o que mudou em cada
> camada, está no `REGISTRO.md` de 28/09 e o resumo das versões no `manifest.json` (revisão **45**).
>
> **O QUE SAIU, em uma linha cada, com a medição no ar:**
>
> - **Item 1 — a medida com a unidade dobrada.** `/loja/` serve `40×28 cm`, `35cm de diâmetro`, `46×36 cm`,
>   `46cm de diâmetro`, `46×37 cm`: **uma** unidade em cada, e o `description` do `Product` da peça saiu
>   *"…técnica pica-sete (louça quebrada), 46×36 cm. Pronta entrega"*. Consertado nos **dois** lados como o
>   despacho manda — valor normalizado na gravação (e nas quatro peças que já existiam, por migração idempotente)
>   **e** molde tolerante. Régua nova em `conferir-no-ar.py` medindo o **texto servido**.
> - **Item 2 — os estados com parâmetro da página da cola.** As três URLs do despacho servem
>   `<meta name='robots' content='noindex, follow' />`, **uma** etiqueta, e a âncora continua com
>   `max-image-preview:large`, sem `noindex`. A régua passou a medir com **valor inválido**, que é o estado que
>   falhava, e alcança o `d2` do cone — que a lista escrita à mão esquecia desde que a forma cônica existe.
> - **Item 3 — o `alt` das fotos.** A foto de destaque das cinco peças serve
>   `Vaso com flores em cerâmica — pica-sete (louça quebrada), foto 1`. **E a contagem do despacho foi corrigida
>   pela medição:** eram 27 imagens com `alt=""` e o defeito eram **5** — as 22 restantes são as miniaturas da
>   tira, cujo `alt=""` é deliberado e correto (repetem a foto que já tem descrição e o nome do controle está no
>   `<a>`). O detalhe está no item 3 do `REGISTRO.md`.
> - **Item 5 — os 13 itens sem degrau.** Os 38 itens do banco têm `degrau` escrito. A escada agora é contada no
>   relatório do validador: **1:1 · 2:5 · 3:4 · 4:28, soma 38**. Portão novo e bateria nova
>   (`ferramentas/mutacoes-degrau.py`, 8 de 8 reprovadas nos cinco bancos, 4 só pelo portão novo).
>
> **E A SEGUNDA OBSERVAÇÃO DO DESPACHO foi decidida e escrita**, como ela pedia: a 25.2-b nomeia um **conceito**,
> não um campo, e nesta ilha o conceito tem **dois** campos — `url_busca_gerada_em` declara o sucesso e
> `motivo_sem_url_busca` declara o fracasso. A decisão está em `dados/esquema-banco.json`, no campo
> `e_o_campo_de_tentativa_da_25_2_b`. *(A primeira observação — quatro `<title>` de peça acima de 64 caracteres —
> continua como recomendação, não como defeito, pelo que ela mesma diz: a régua de 64 é da aquametria e não do
> contrato.)*

### ~~4. (METADE) AS QUATRO PÁGINAS QUE JÁ TINHAM `description` CONTINUAM ACIMA DE 160~~ — **CUMPRIDO em 02/10/2026 às 11h5xZ, revisão 54. COM ISTO O DESPACHO DE 28/09 ESTÁ FECHADO INTEIRO.**

**Conferido no ar contra o critério de pronto que o próprio item declarou (18.4), palavra por palavra:**

- *"as quatro servirem `description` entre 120 e 160 caracteres contados decodificados"* — **143, 139, 150 e 139**,
  medidas no HTML servido pelo `conferir-no-ar.py`, que imprime as quatro.
- *"sem duplicata"* — as 17 descrições do sitemap são distintas, inclusive nos 60 primeiros caracteres.
- *"e a de `/materiais/qual-cola-usar-no-mosaico/` citar um número que a própria página calcula, com a fonte"* —
  ela cita **três**: `7 colas em 270 casos de base, lugar e caquinho, e os 68 que a gente ainda não responde`,
  todos de `cdm_f2_cobertura()`, a mesma varredura que escreve a seção "o que a gente ainda não responde" na tela.
  **Com isso a Proposta 1 de 23/09 fecha do lado da máquina**, como este item pedia.
- *"Fechar isto é tirar as quatro da lista `TRAVADAS_ATE_30_09`"* — a lista **não foi esvaziada, foi apagada**: a
  faixa passa a ser cobrada nas 17 sem exceção escrita em lista nenhuma, que é o único jeito de uma exceção não
  sobreviver ao motivo dela.

**A ESPERA ERA LEGÍTIMA E ACABOU.** O motivo escrito aqui em 28/09 era o BLOCO A do despacho do Raphael de 24/09,
que pela 18.1 vem antes deste e mandava não mexer na promessa da SERP antes da janela de 30/09. A janela fechou, o
BLOCO A saiu no mesmo movimento — a `description` é a outra metade da mesma promessa, e separá-las é que teria
feito o que aquele bloco existia para impedir.

**E A PEÇA DA LOJA FICOU DE FORA, de propósito e com a decisão citada:** o portão novo de `<title>` mediu as 17 e
achou **quatro títulos de peça entre 71 e 79 caracteres** (`/loja/quadro-nossa-senhora-aparecida/` é o maior). A
primeira observação deste mesmo despacho de 28/09 já tinha decidido isso — *"continua como recomendação, não como
defeito, pelo que ela mesma diz: a régua de 64 é da aquametria e não do contrato"* —, e o formato é o que o
despacho do Raphael de 10/09 escreveu. Então o número é **medido e impresso, nunca reprovado**, no mesmo desenho
do soft 404 de borda. A régua nasceu reprovando página certa e foi consertada antes de o despacho fechar.

*(O texto original do item, para a próxima execução saber contra o que ele foi conferido, está preservado abaixo.)*

### ~~4-original. (METADE) AS QUATRO PÁGINAS QUE JÁ TINHAM `description` CONTINUAM ACIMA DE 160~~ — e a espera era por ordem de despacho mais antigo

**O que já saiu:** as **oito** URLs que não serviam `<meta name="description">` nenhuma — `/`, `/loja/`,
`/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/`, `/privacidade/` — servem uma
cada, entre **121 e 143 caracteres**, nenhuma repetida, medido no ar em 28/09/2026 às 17h0xZ. E a causa que o
próprio despacho nomeou — *"não é o texto de uma página: é qual camada emite a etiqueta e para quais tipos de
página"* — está resolvida: **quem tem `description` DECLARA pelo filtro `cdm_descricao`; quem imprime é a casca,
uma vez.** F1, F2, tecnicas e Loja pararam de dar `echo` na própria. A bancada da casca conta os `echo` no código
dos snippets e reprova o segundo emissor que nascer.

**O que falta:** a **faixa de 120 a 160** nas quatro que já tinham etiqueta —
`/materiais/qual-cola-usar-no-mosaico/` (183), `/materiais/quantas-pastilhas-para-mosaico/` (165),
`/como-fazer/o-que-e-mosaico-picassiete/` (192), `/como-fazer/o-que-e-trencadis/` (189).

**Por que não saiu, e o motivo não é fôlego:** **três delas estão na primeira página do Google** e o **BLOCO A do
despacho do Raphael de 24/09** — que pela 18.1 vem antes deste — diz, com todas as letras, que ele **espera
30/09**, porque *"trocar título antes do número de 30/09 misturaria duas causas na mesma janela"*. A `description`
é a outra metade da mesma promessa de SERP: trocá-la agora faria exatamente o que aquele bloco existe para
impedir. A quarta (Trencadís) fica parada pelo mesmo despacho, que manda *"deixe uma página parada para a próxima
leitura ter com o que comparar"*.

**E é por isso que o pedido do item 4 de escrever a `description` de `/materiais/qual-cola-usar-no-mosaico/`
cumprindo a Proposta 1 no mesmo movimento não foi obedecido:** a Proposta 1 pede um número que a própria página
calcula no `<title>` **e** na `description`, e é exatamente o trabalho do BLOCO A, que espera 30/09 por ordem do
Raphael. Fazer só a `description` agora seria a pior das três opções — mexeria na janela de medição sem entregar a
alavanca inteira.

**Pronto quando:** depois da leitura de 30/09, as quatro servirem `description` entre 120 e 160 caracteres
contados decodificados, sem duplicata, e a de `/materiais/qual-cola-usar-no-mosaico/` citar um número que a
própria página calcula, com a fonte — fechando a Proposta 1 no mesmo movimento em que fecha esta faixa. A régua no
ar **já existe e já mede as quatro**: `conferir-no-ar.py` cobra presença nas 17 e faixa em todas menos essas
quatro, e **imprime o número delas** para ele não ser esquecido. Fechar isto é tirar as quatro da lista
`TRAVADAS_ATE_30_09`.

## DESPACHO DA SENTINELA — 2026-09-23 (LEITURA SEMANAL, 20h12Z) — a ilha esquecida é a que tem tráfego

**A ilha está FORA DO FOCO** (`foco.md` nomeia a aquametria desde 21/09), então pela 1.2 nada aqui fura a fila: **despacho NORMAL de ilha fora do foco espera.** Este despacho existe porque a 1.2-b.1 manda a medição continuar em todas as ilhas, e porque o que a medição achou muda a conversa sobre a ordem do foco.

> **PONTEIRO DO PENTE FINO — 28/09/2026: O PARÁGRAFO ACIMA É DE 23/09 E DEIXOU DE DESCREVER O MUNDO EM 24/09.**
> Esta ilha **está em foco desde 24/09/2026** (`foco.md`, e o aviso no topo deste mesmo arquivo), justamente por
> causa do número que este despacho mediu — a Proposta 2 abaixo está fechada com essa decisão. Lida ao pé da
> letra, a frase "despacho NORMAL de ilha fora do foco espera" manda **adiar** os itens abertos da ilha que hoje
> recebe todas as execuções. **Não espera: esta é a ilha em foco, e o que sobra deste despacho entra na fila
> normalmente, atrás do despacho do Raphael de 24/09 (18.1).**

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
> **A TERCEIRA CONDIÇÃO SEGUE ABERTA EM 02/10/2026, E O MOTIVO MUDOU DE DONO.** Ela dizia "a leitura semanal
> seguinte registrar que a linha de `/author/` **saiu** de `dados/posicoes.md`". **A leitura semanal de 30/09 não
> aconteceu** — a ronda diária técnica daquele dia rodou às 14h53Z, a estratégica não foi disparada, e em 01/10
> não houve execução nenhuma. A Fundação **não pode** fazê-la: a conta `sentinela@` não tem acesso a
> `sc-domain:clubedomosaico.com.br`. Então este item não espera mais trabalho de máquina: espera a próxima
> leitura semanal, e o que a destrava está em `dados/despachos.md`, na lista de ABERTOS.
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
> e conferir com clique nosso apagaria o primeiro clique orgânico que a leitura semanal procura. ~~**Quem lê essa
> linha é a leitura de 30/09.**~~ **A leitura de 30/09 não aconteceu** (02/10/2026), então quem lê é a próxima —
> e o clique continua não existindo: a ilha tinha zero clique orgânico em 23/09 e nada desde então o produziu.
> **A troca de título e de meta de 02/10 é justamente a aposta que existe para esse clique aparecer.**

### 3. CORREÇÃO DE CABEÇALHO — `urls_publicadas: 13` ESTÁ DEFASADO; O SITEMAP SERVE 17

Contado no ar hoje: `wp-sitemap-posts-page-1.xml` tem **12** URLs e `wp-sitemap-posts-peca-1.xml` tem **5** — total **17**. É a seção 4 em ação: resumo velho lido como fato.

**Pronto quando:** o cabeçalho do `ESTADO.md` trouxer `urls_publicadas: 17`, com a contagem refeita no sitemap no ar e registrada no `REGISTRO.md`.

> **CUMPRIDO EM 24/09/2026 às 19h33Z, E O ITEM CONTINUAVA SEM A LINHA QUE OS DOIS IRMÃOS GANHARAM.** *(Fechado
> pelo Pente Fino em 28/09/2026, pela 18.4, contra as duas evidências que já estavam no repositório: o cabeçalho
> do `ESTADO.md` desta ilha traz `urls_publicadas: 17`, e o **BLOCO D** do despacho do Raphael de 24/09, neste
> mesmo arquivo, registra a contagem refeita no `wp-sitemap.xml` no ar — 12 em `wp-sitemap-posts-page-1.xml` mais
> 5 em `wp-sitemap-posts-peca-1.xml` — listada uma a uma no `REGISTRO.md`. Os itens 1 e 2 receberam nota de
> estado e este não; item cumprido apresentado como aberto faz a execução seguinte refazer contagem.)*

### AS TRÊS PROPOSTAS DE ACELERAÇÃO (12.1) — na ordem de ROI

**PROPOSTA 1 — `/materiais/qual-cola-usar-no-mosaico/` ESTÁ EM 7,8 COM 17 IMPRESSÕES E CTR ZERO. É A MELHOR LINHA DO ARQUIPÉLAGO INTEIRO.**
- Consulta nomeada: **`cola para mosaico`**, posição **10,0**. A página inteira está em 7,8 com 17 impressões — mais impressões do que a aquametria e a robometria somadas, quatro vezes.
- Página: `https://clubedomosaico.com.br/materiais/qual-cola-usar-no-mosaico/`.
- Banda 4 a 10 pela 12.1: o trabalho é de **CTR, não de conteúdo**. A alavanca que a 12.1 nomeia: **título que promete o número, meta que promete a faixa e a fonte**. O precedente que já rodou está na robometria, proposta 2 de 16/09: o número sai de um arquivo derivado do banco, nunca digitado, e a marca é o que cede lugar no `<title>`.
- **O que esta proposta NÃO autoriza:** trocar a URL (proibido pela 12.1), reescrever a página, ou mexer em `/como-fazer/o-que-e-mosaico-picassiete/` — deixe uma página parada para a próxima leitura ter com o que comparar.
- **Pronto quando:** o `<title>` e a `<meta name="description">` servidos citarem um número que a própria página calcula, com a fonte, e a leitura de 30/09 registrar impressões e CTR desta linha para comparar com **7,8 · 17 impressões · CTR 0%**.
- > **A PRIMEIRA METADE ESTÁ CUMPRIDA E CONFERIDA NO AR EM 02/10/2026 às 11h5xZ** (BLOCO A, revisão 54). O
  > `<title>` serve `Qual cola usar no mosaico, e qual rejunte – 7 colas para 9 bases` e a `description` serve
  > `7 colas em 270 casos de base, lugar e caquinho, e os 68 que a gente ainda não responde` — **três** números,
  > todos de `cdm_f2_cobertura()`, com a fonte na frase. O precedente que esta proposta citava foi seguido à
  > risca: o número sai de uma varredura derivada, nunca digitado, e a marca é o que cede lugar no `<title>`.
  > **A SEGUNDA METADE NÃO É DA FUNDAÇÃO e segue aberta:** a leitura de 30/09 não aconteceu, e a janela
  > 23→30/09 — a última semana inteira com o título antigo, e por isso a única base de comparação limpa que vai
  > existir — está pedida em `dados/despachos.md`. **O veredito continua de 08/10**, como o BLOCO A manda.

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

## DESPACHO DO RAPHAEL — 24/09/2026 — ENTRADA NO FOCO: MEDIR ANTES DE CONSTRUIR

*(Promovido de `###` para `##` pelo Pente Fino em 28/09/2026: este despacho nasceu como subseção do DESPACHO DA
SENTINELA de 12/09, que está CUMPRIDO e termina com "Nada mais nesta ronda". Pela 18.1 o despacho do Raphael vem
antes do da Sentinela, e o único despacho ABERTO do Raphael nesta ilha estava aninhado dentro de um fechado. Só o
nível do título mudou — nenhuma linha de conteúdo foi movida nem reordenada.)*

> **ESTADO DESTE DESPACHO EM 02/10/2026, 11h5xZ — FECHADO. O BLOCO A SAIU, E COM ELE O ÚLTIMO ITEM.**
> Os cinco blocos (0, A, B, C, D) estão CUMPRIDOS e conferidos no ar pela 18.4. O **BLOCO A** foi o único que
> esperou, e esperou por ordem escrita deste despacho: a janela de medição de 30/09 tinha de fechar primeiro.
> Fechou. O que mudou no ar está medido em `dados/posicoes.md`, no retrato "DEPOIS" de 02/10, ao lado do retrato
> "ANTES" de 29/09 — e o veredito continua sendo de **08/10**, como este despacho manda.
> **A ÚNICA COISA QUE SOBREVIVE A ELE é o pedido do BLOCO C ao Raphael** (acesso da conta `sentinela@` ao Search
> Console desta propriedade), que não é trabalho da Fundação e passou a morar em `dados/despachos.md`, na lista de
> ABERTOS, junto com o pedido novo de ler a janela 23→30/09 — a última semana inteira com o título antigo.
>
> *(O bloco de estado anterior, de 25/09 às 14h0xZ, dizia "FALTA SÓ O BLOCO A" e está preservado abaixo, porque o
> que ele conta sobre os blocos B e C é o que a próxima execução precisa ler.)*

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

#### ~~BLOCO A — CTR das três páginas que já estão na primeira página~~ — **CUMPRIDO em 02/10/2026 às 11h5xZ, manifest e `/status` na revisão 54**

**Conferido no ar pela 18.4, contra as cinco ordens que o próprio bloco escreveu:**

| o que o bloco mandou | o que está no ar |
|---|---|
| título que promete o número | `– 7 colas para 9 bases` (64) · `– 12 peças calculadas` (64) · `– 7 colas em 45 casos` (62) |
| meta que promete a faixa e a fonte | as quatro em **120 a 160**: 143 · 139 · 150 · 139, cada uma dizendo a procedência |
| NÃO reescrever o conteúdo das três | nenhuma linha de corpo mudou. O `<h1>` servido continua `Qual cola usar no mosaico, e qual rejunte`, e a promessa aparece **uma vez** no HTML inteiro: dentro do `<title>` |
| gravar título e meta ANTES da troca | `dados/posicoes.md`, retrato "ANTES" de 29/09 (medido pela borda) e retrato "DEPOIS" de 02/10 |
| CTR sem com o que comparar fica ESCRITO | está escrito nos dois retratos, com as 30 impressões nomeadas |
| não declarar vitória nem derrota | nada declarado; o veredito segue de **08/10** |

**O QUE CEDEU O LUGAR FOI A MARCA, NÃO O NOME DA PÁGINA.** `Clube do Mosaico` são 16 caracteres de carimbo no fim
de um título que está na primeira página e não é clicado, numa ilha com **zero clique orgânico medido** — ninguém
a procura pelo nome. O nome continua um só nas cinco superfícies em que aparece (H1, cartão, degrau da trilha,
`og:title` e a primeira metade do `<title>`), que é a regra que a Aquametria pagou para esta ilha herdar em
11/09/2026. O caminho é o precedente da Robometria de 17/09, portado: a casca 1.19.0 monta o título **uma vez**, e
quem tem promessa a **declara** pelo filtro `cdm_promessa` — o mesmo contrato de camadas que a `description` tem
desde 28/09 e a etiqueta de robô desde 25/09.

**NENHUM NÚMERO É DIGITADO, e é isso que faz a promessa não envelhecer calada.** Os três da `qual-cola` saem de
`cdm_f2_cobertura()`, a **mesma** varredura de base × lugar × caquinho que escreve "o que a gente ainda não
responde" na tela — então a promessa da SERP e a confissão do fim da página não têm como discordar. Os da
`quantas-pastilhas` saem da mesma conta que monta a tabela das doze peças; os do `picassiete`, de
`cdm_tecnicas_contas()`.

**TRÊS TRAVAS, E DUAS SÃO SILENCIOSAS POR DESENHO:** promessa que estoura o teto de 65 devolve a marca; número que
não chegou — ou zero — recusa o molde **inteiro**; e a bancada reprova quem DECLARA promessa e serve título sem
dígito. As duas primeiras não falham, elas devolvem a marca e a página continua válida: por isso a bancada ganhou
o mundo `sem_banco=1`, em que a trava 2 dispara **na página** e não só na função pura. Bateria nova
`ferramentas/mutacoes-promessa-do-titulo.py`: **19 mutações, 19 reprovadas, 0 passaram.**

**E A BANCADA SERVIA UM TÍTULO QUE NENHUMA AFIRMAÇÃO MEDIA.** Até 02/10 o `render-para-teste.php` punha
`<title>Clube do Mosaico — teste</title>` em toda página — um rótulo fixo. O bloco que troca a marca por um número
mexe exatamente nessa etiqueta, e régua que não alcança o que o bloco muda é régua que nasce cega. Agora a bancada
monta o título pelo caminho do WordPress: partes, filtro `document_title_parts`, separador.

**O QUE NÃO FOI TOCADO, E A AUSÊNCIA É A DECISÃO:** o `<title>` do **Trencadís**. Este mesmo despacho, no de 23/09,
manda *"deixe uma página parada para a próxima leitura ter com o que comparar"*. Ele não declara promessa, e o
portão mede isso nas duas direções — promessa onde tem de haver, marca onde tem de ficar. Só a `description` dele
mudou, de 189 para 139, que era o que o item 4 do despacho de 28/09 cobrava.

**O QUE ESTE BLOCO NÃO PODE FECHAR, e não é por falta de fôlego:** a segunda metade da **Proposta 1** de 23/09 pede
que *"a leitura de 30/09 registre impressões e CTR desta linha"*. **A leitura semanal de 30/09 não aconteceu** — a
ronda técnica daquele dia rodou, a estratégica não —, e a Fundação não pode fazê-la: a conta `sentinela@` não tem
acesso a esta propriedade. Está em `dados/posicoes.md` com todas as letras e virou pedido em `dados/despachos.md`.

*(O texto original do bloco, para a próxima execução saber contra o que ele foi conferido: as três páginas eram
`/materiais/qual-cola-usar-no-mosaico/` (posição 7,8, 17 impressões), `/materiais/quantas-pastilhas-para-mosaico/`
(9,1, 9 impressões) e `/como-fazer/o-que-e-mosaico-picassiete/` (7,0, 3 impressões), com **zero clique nas três**;
consultas nomeadas `cola para mosaico` (10,0) e `picassiete` (6,0), e 28 das 30 impressões anonimizadas pela
Search Console.)*

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
3. > **ENTREGUE EM 02/10/2026 às 19h51Z — O 4c DE `acabamento` ESTÁ NO AR, COM A MÃE E AS TRÊS FILHAS.**
   > Quatro URLs novas (a ilha vai de **17 para 21**), snippet `Clube do Mosaico Guia` **1.0.0**, manifest e
   > `/status` na **revisão 56**. Endereços: `/materiais/acabamento/` e, debaixo dela,
   > `selar-a-base-antes-de-fazer-mosaico`, `verniz-para-peca-de-mosaico` e
   > `impermeabilizar-peca-de-mosaico` — **a primeira árvore de três segmentos desta ilha**, porque é o
   > primeiro bloco em que a categoria nasce ANTES da filha. O número da seção 9 é a **cobertura
   > declarada** (das 15 superfícies do vocabulário, quantas a frase do fabricante alcança: 13 de 150 na
   > mãe) e o segundo é o **relógio**, que fecha em 2 dos 10 produtos e só neles. Bancadas novas:
   > `teste-guia.php` (106 afirmações) e `mutacoes-guia.py` (14 de 14). O detalhe inteiro está no
   > `REGISTRO.md` de 02/10 às 19h51Z.
   >
   > **A `alicate/cortador_de_azulejo` TAMBÉM está em `pode_nascer` e FICOU DE FORA de propósito:** a mãe
   > dela está em `espera_serp`, e filha sozinha pendurada em `/materiais/` é o cluster ralo que a 16.6
   > proíbe. **O que a destrava é medir a SERP de `alicate`** — busca, não coleta —, e com ela a segunda
   > categoria do Guia sai com a mesma leva de quatro. O mesmo vale para `pastilha` e `rejunte`.
   >
   > **MEDIDO EM 05/10/2026 ÀS 19h3xZ — AS DUAS FILHAS QUE FALTAM NO `rejunte` NÃO ESTÃO A UMA COLETA DE
   > SKU, E O BLOQUEIO TEM NOME NOVO: É ÍNDICE DE BUSCA, NÃO EGRESSO. NÃO REPITA A COLETA.**
   >
   > A frase de seis horas antes mandava a próxima execução coletar **2 itens de banco** para
   > `rejunte/acrilico` e **2** para `rejunte/epoxi`, dizendo *"não é mais procura de número — é coleta de
   > SKU"*. A metade sobre o número está certa. A outra metade supôs que coletar SKU de rejunte fosse como
   > coletar de `acabamento`, e **não é**: `acabamento` saiu de zero por busca porque Acrilex, Coral e
   > Suvinil publicam a declaração em página de produto, e nenhuma delas entra em fórmula de junta. O
   > rejunte entra, e a declaração de faixa de junta mora em **boletim técnico**.
   >
   > **O que foi medido nesta execução, e é a razão:**
   >
   > | porta | medida (três passadas) |
   > |---|---|
   > | `*.vteximg.com.br` e `*.vtexassets.com` (o espelho) | **ABERTAS** — 9 de 9 hosts conversaram |
   > | `www.quartzolit.weber` | **403**, e isto MUDOU: o registro de 30/09 dizia `connect_rejected` |
   > | `www.portokoll.com.br`, `rejuntamix.com.br`, `bautech`, `kerakoll`, `mapei`, `votomassa`, `eucatex` | `000` — falha de **DNS**, inclusive por WebFetch (`ENOTFOUND`) |
   > | `web.archive.org`, `r.jina.ai`, `docs.google.com` | `000` — as três escapatórias estão fechadas |
   > | `www.telhanorte.com.br`, `*.vtexcommercestable.com.br`, `*.myvtex.com` | `000` — **não há como NAVEGAR o espelho** |
   >
   > **A consequência prática, e ela é a regra que fica:** o espelho é **arquivo por nome conhecido**, nunca
   > catálogo. O inventário inteiro dele são **14 documentos**, listados em `dados/canal-de-espelho.md`
   > com a identidade lida na página 1 de cada um — e **nenhum é rejunte acrílico nem epóxi**. Quatro
   > consultas diferentes desta execução procuraram os dois nas duas famílias de CDN e deram zero. Então
   > *"o egresso não abre PDF de fabricante"* e *"eu não sei o nome do arquivo"* são **bloqueios
   > diferentes**, e quatro blocos desta ilha escreveram os dois com a mesma frase. O que destrava
   > `rejunte/acrilico` e `rejunte/epoxi` é uma das duas, e nenhuma é coleta: **(a)** o curinga
   > `*.quartzolit.weber` na lista de rede — com a ressalva nova de que o `www.` já responde **403**, então
   > o curinga pode entrar e o 403 ficar, porque 403 é decisão do fabricante e não da rede do Raphael; ou
   > **(b)** o nome do arquivo aparecer num host do espelho, que é sorte de índice e não trabalho.
   >
   > **O QUE ESTE BLOCO ENTREGOU NO LUGAR, e ele é o mesmo veio:** o espelho pagou a **primeira dívida de
   > `conferir_no_pdf` desta ilha**. Eram **46** fontes marcadas *"confira no PDF"*; o boletim do
   > `cimentcola externo quartzolit` (revisado em **maio de 2016**) foi aberto e lido página a página, e com
   > ele: a pendência `cimentcola-consumo-e-tempo-em-aberto` saiu de "falta número" para **número escrito**
   > (3,5 / 4,5 / 8 kg/m² por faixa de área, e tempo em aberto ≥20 min — mais os do **AC-III**, do boletim
   > do `cimentcola flexível`, que ficaram em `dados/constantes.json` porque **não existe registro de
   > AC-III no banco**); a embalagem ganhou o **saco plástico de 5 kg**, que o banco não tinha e que é o
   > único formato deste produto que não é formato de obra; e o `nao_indicado_para`, que estava **vazio**,
   > ganhou as três proibições da seção 3 do boletim.
   >
   > **E A DECISÃO QUE ESTE BLOCO TOMOU E NÃO ESCONDEU, porque ela é o achado:** a pendência
   > `cimentcola-substrato-declarado` **mudou de natureza e continua aberta**. O documento responde
   > inteira, na seção 4.1 — emboço, alvenaria, contrapiso, paredes de concreto, alvenarias de blocos e
   > gesso acartonado —, e **nada disso foi gravado**, de propósito. Gravar só essa metade faria a F2
   > recomendar esta argamassa em `cimento_concreto` e `alvenaria_tijolo` para quem respondeu **pastilha de
   > vidro** — e o MESMO boletim proíbe *"revestimentos especiais"*, que é o que pastilha de vidro é. As
   > cinco regras de elegibilidade decidem sobre BASE e AMBIENTE; a sexta lê a tessela por **um** campo
   > (`exige_superficie_porosa`). **Não existe campo para proibição que fala da PEÇA que se cola.**
   >
   > ~~**ENTÃO O PRÓXIMO BLOCO ESTÁ ESCOLHIDO E É A REGRA 7**, e ela não é linha, é bloco: proibição
   > declarada sobre a peça elimina o produto para as tesselas que a ilha classifica naquele grupo — lista
   > no esquema (molde de `superficies_porosas`), classificação **nossa** e a tela proibida de dizer que o
   > fabricante classificou (26.3), nas **duas** implementações (`validar-banco.py` e o snippet da F2 em
   > PHP), com matriz esperada e bateria.~~ **ENTREGUE EM 06/10/2026** — esquema na **v11**, F2 **1.8.0**,
   > Técnicas **1.4.0**, `grupos_de_tessela_proibidos` com 3 grupos, `matriz_esperada_da_proibicao_sobre_a_peca`
   > com 18 pares e 5 âncoras, e 20 mutações novas em `mutacoes-f2.py`.
   >
   > **MAS A SEGUNDA METADE DA FRASE ESTAVA ERRADA, E O ERRO ERA LEGÍVEL NO PRÓPRIO REPOSITÓRIO.** Ela
   > dizia *"fechada ela, o substrato entra e a cimentcola AC-II passa a ser recomendação primária em duas
   > bases"*. **O substrato NÃO entrou.** As três frases da seção 4.1 do boletim já estavam gravadas aqui
   > desde 05/10, e lê-las mostrou que a proibição de peça era **um de três** bloqueios:
   >
   > | bloqueio | estado | o que falta |
   > |---|---|---|
   > | proibição sobre a PEÇA | **fechado** | nada — é a regra 7 |
   > | o qualificador de **ambiente** vem colado no substrato (`em áreas internas`, `em paredes internas`) e o banco decide ambiente por PRODUTO | aberto | campo de par substrato×ambiente, ou uma regra 8 lida como a 7 lê o grupo |
   > | o substrato sem qualificador de ambiente tem qualificador de **CURA** (`paredes de concreto curado há 180 dias`; abaixo disso o boletim manda usar outro produto, nomeado) | aberto | a F2 servir `preparo` na resposta |
   >
   > Os dois abertos são caros **nesta** ilha: `alvenaria_tijolo` + `externo_abrigado` é muro de mosaico ao
   > ar livre, e `cimento_concreto` aqui não é parede de obra — é vaso e tampo que a artesã acabou de
   > fazer, muito abaixo dos 180 dias. A razão inteira está em `materiais-colas.json`, no campo
   > `substratos_que_o_documento_declara_e_que_NAO_foram_gravados.os_outros_dois_bloqueios_medidos_em_06_10_2026`.
   >
   > **E A REGRA 7 ACHOU UM DEFEITO QUE NÃO TINHA NADA A VER COM A ARGAMASSA.** O Tekbond Silicone
   > Acético Construção proíbe `espelhos` desde 10/09 e a F2 o servia **no topo** para quem respondeu
   > **caco de espelho** sobre cerâmica: a frase era lida como base e só como base. Pior — a **âncora
   > escrita à mão da regra 6**, de 13/09, declarava esse produto no topo de `vidro` + `caco de espelho`,
   > ou seja, a régua independente tinha o defeito escrito como **resultado esperado**. Portão
   > independente mede divergência entre as metades; nunca a lacuna que as duas têm.
   >
   > ~~**O PRÓXIMO BLOCO ESTÁ ESCOLHIDO E É O BARATO DOS DOIS QUE FICARAM: a F2 (e o Guia) passarem a
   > servir `preparo` na resposta.**~~ **ENTREGUE EM 06/10/2026 às 14h10Z** — esquema na **v12**
   > (`regras_do_campo_preparo`, três estados), F2 **1.9.0**, Guia **1.1.0**, casca **1.20.0**,
   > `mutacoes-preparo.py` (16 de 16, 12 só pelo portão novo, 0 falso positivo). **CINCO registros
   > ganharam `literal_do_fabricante` lido no dia** — Cascorez, PL500, AF1500 e os boletins do rejunte
   > piscinas e da cimentcola externo — e **oito** ficaram sem, com a causa classificada em
   > `host-recusa` (4, Tekbond e Quartzolit em 403 nas três passadas) e `nao-coletado` (4).
   >
   > **A FRASE ABAIXO ACERTOU O BLOCO E ERROU O TAMANHO DELE, e o que faltava não era trabalho: era
   > CONFERIR.** Ela dizia que eram "nove declarações de fabricante lidas, gravadas e descartadas em
   > silêncio" e que o bloco era a tela passar a ler o campo. A primeira metade estava certa. A
   > segunda supunha que as nove frases fossem do fabricante — e **quatro** delas puderam ser
   > conferidas contra o documento em 06/10, **as quatro perdendo informação dele**: uma fechou uma
   > lista que ele deixou aberta, uma apagou o motivo de uma instrução e uma linha com número, uma
   > apagou a condição que ele escreve dentro do preparo, e uma apagou **sete das oito** frases da
   > seção — entre elas uma que o registro IRMÃO carrega inteira. **Paráfrase servida entre aspas é a
   > instrução dele menos a parte que a gente deixou cair, com o nome dele embaixo.** Por isso o campo
   > tem três estados e a tela serve só o primeiro, e por isso o bloco custou o que custou.
   >
   > **E A DÍVIDA QUE ESTE BLOCO EXISTIA PARA PAGAR NÃO FOI PAGA — LEIA ISTO ANTES DE PROMETÊ-LA DE
   > NOVO.** A cura de 180 dias da cimentcola AC-II está **gravada** e **não está na tela**. Varredura
   > dos 45 estados de cola em 06/10, um render por estado: **zero** servem a frase. O produto é
   > **eliminado por silêncio** nas 45 células, porque `indicado_para` não nomeia nenhuma base do
   > vocabulário — e não nomeia porque **o substrato não foi gravado**. O bloco de preparo só alcança
   > quem a página **recomenda**. **Servir `preparo` era necessário e não suficiente: o terceiro
   > bloqueio é JUSANTE do segundo, não irmão dele.**
   >
   > A frase de 05/10 — *"ou a F2 passa a servir `preparo` na resposta, e a cura vira texto na tela"* —
   > acertou o mecanismo e errou a ordem, e a execução de 06/10 **a repetiu**: escreveu que a cura
   > estava na tela antes de varrer os 45 estados, e corrigiu depois de medir. `teste-f2.php` passou a
   > fixar o estado nos **dois** sentidos: hoje ele cobra **zero**, e no dia em que o substrato entrar
   > a afirmação cai — a queda é a **entrega**, não o defeito, e o comentário dela diz isso.
   >
   > **A ordem certa está medida:** primeiro o campo de par substrato × ambiente (ou a regra 8 lida
   > como a 7 lê o grupo), e a cura entra na tela **junto** com a recomendação, no mesmo bloco,
   > dizendo ao leitor que o vaso novo não serve.
   >
   > **O PRÓXIMO BLOCO TEM DOIS CANDIDATOS MEDIDOS, e o barato é o (a):**
   >
   > **(a) `propriedades.sobra_declarada_pct` na F1, a partir dos 10% da AF1500.** A linha *"Compre 10%
   > a mais para cortes e ajustes na aplicação"* é a **única** sobra declarada por fabricante que esta
   > ilha tem lida — e a paráfrase a tinha apagado por inteiro. A F1 pergunta a sobra ao visitante
   > **sugerindo 15%**, um número que não é de ninguém. Hoje a declaração dele está na tela como frase
   > e **não entra na conta**. Quem fizer: o campo é `propriedades`, então exige fonte por valor; a F1
   > tem de dizer **de quem** é o número quando usar o declarado; e a bateria tem de medir o estado em
   > que o produto escolhido **não** declara sobra, que é o de 40 dos 41 registros.
   >
   > **(b) O campo de par substrato × ambiente**, medido em `materiais-colas.json /
   > quartzolit-cimentcola-externo-acii / fontes / bt-cimentcola-externo-2016-05 /
   > substratos_que_o_documento_declara_e_que_NAO_foram_gravados`. Decisão de esquema — bloco, não linha.
   >
   > **E uma coisa que NÃO é bloco e destrava quatro registros de uma vez:** `*.quartzolit.weber` na
   > lista de rede (`dados/despachos.md`, ABERTOS). Quatro das oito paráfrases sem literal são da
   > Quartzolit e **duas já têm o documento nomeado** por derivação da constante. A ressalva nova: o
   > `www.` já responde **403**, então o curinga pode entrar e o 403 ficar — 403 é decisão do
   > fabricante, não da rede do Raphael.
   >
   > *(O texto abaixo é o da execução de 12h34Z e fica sem uma palavra alterada: foi ele que escolheu o
   > bloco, e o que ele mediu — a varredura dos nove snippets, os 9 de 41 registros, o
   > `quartzolit-rejunte-porcelanatos-e-ceramicas` com motivo no lugar do texto — está todo certo.)*
   >
   > **O PRÓXIMO BLOCO ESTÁ ESCOLHIDO E É O BARATO DOS DOIS QUE FICARAM: a F2 (e o Guia) passarem a
   > servir `preparo` na resposta.** Varredura de 06/10/2026 nos nove snippets: a palavra `preparo` não
   > aparece em **nenhum** deles, e **9 dos 41 registros** do banco têm o campo preenchido com frase de
   > fabricante — o acético, o Cascorez, o PL500, a AF1500 e cinco rejuntes da Quartzolit ("deixar em
   > repouso por 15 minutos antes de usar", "juntas de até 3 mm devem ser molhadas antes"). **São nove
   > declarações de fabricante lidas, gravadas e descartadas em silêncio**, que é o defeito que esta ilha
   > já mediu quatro vezes com outros nomes. Não é só a cura da cimentcola: vale para o banco inteiro, e é
   > o que destrava um terço do substrato da AC-II. Um dos nove (`quartzolit-rejunte-porcelanatos-e-ceramicas`)
   > tem `preparo: "Nao coletado nesta execucao."` — isso é motivo, não texto de fabricante, e a tela não
   > pode servi-lo; separar os dois estados é parte do bloco. Depois dele, o campo de par
   > substrato×ambiente, que é decisão de esquema.
   >
   > **TRÊS PORTAS MEDIDAS DE CARONA, e as três valem mais que uma coleta:**
   > **(1)** `www.pastilhart.com.br` responde **200 nas três passadas**, e o registro de 28/09 dizia que
   > *"não entrou nem no apex"*. A página do `pastilhart-af1500` foi **aberta e lida** (167 KB): as cinco
   > declarações de ambiente e os três números de geometria **conferiram, zero divergência** — a coleta por
   > busca de 12/09 estava certa, e isso também é resultado. O nível **não** subiu e não devia: nível é
   > natureza da fonte, nunca alcance dela.
   > **(2)** O **primeiro preço** que esta ilha vê numa fonte alcançável está medido (R$ 49,00 à vista, de
   > R$ 71,89, estoque 30, lido em 05/10). `dados/cotacoes.json` segue não existindo, e criá-lo é decidir
   > formato, validade do preço e como a tela mostra preço datado — bloco, não linha.
   > **(3)** A **pista da FISPQ** que o bloco de 13h2xZ deixou está **FECHADA, e a resposta é NÃO**: os
   > dois arquivos são a FISPQ do **Osmocolor ST** e a do **Pentox Cupim**, as duas da Montana Química, e
   > uma terceira achada hoje é a do **Piso Sobre Piso Interno Quartzolit**. Nenhuma é a FISPQ do epóxi, e
   > `regras_da_categoria_apoio` continua travada exatamente onde estava. **Ninguém precisa gastar bloco
   > nesta pista outra vez.**
   >
   > *(O texto abaixo é de seis horas antes e fica sem uma palavra alterada: foi ele que abriu o canal, e
   > foi a explicação dele — não o achado — que caiu.)*
   >
   > **MEDIDO EM 05/10/2026 ÀS 13h2xZ — O NÚMERO QUE FALTAVA FOI ENCONTRADO, E `rejunte/cimenticio`
   > PASSOU OS DOIS PORTÕES. O QUE SEGURA A SEGUNDA CATEGORIA DO GUIA AGORA SÃO AS OUTRAS DUAS FILHAS.**
   >
   > A frase de três horas antes dizia que a filha estava **a um número** — `liberacao_area_molhada_h` nos
   > 3 itens do recorte. Era exatamente isso, e o número estava num lugar que esta ilha dava por fechado há
   > três blocos: **dentro do boletim técnico do fabricante, em PDF.**
   >
   > | recorte | antes | agora |
   > |---|---|---|
   > | `rejunte/cimenticio` | `espera_dado` | **`pode_nascer`** — os dois portões abriram |
   > | `rejunte` (mãe) | `pode_nascer` | `pode_nascer`, inalterada |
   > | `rejunte/acrilico` | `sem_nenhum_dos_dois` | igual: **2 itens de banco** e SERP nunca olhada |
   > | `rejunte/epoxi` | `sem_nenhum_dos_dois` | igual: **2 itens de banco** e SERP nunca olhada |
   >
   > **O QUE ISTO DEIXA PARA A PRÓXIMA EXECUÇÃO, e agora são DUAS coisas, não uma.** A 16.5 cobra **3
   > filhas** na categoria e o `rejunte` tem **1**. Para a segunda categoria do Guia nascer faltam
   > `rejunte/acrilico` e `rejunte/epoxi`, e as duas pedem a MESMA coisa: **2 itens de banco cada uma**, e
   > depois a SERP de cada recorte. Não é mais procura de número — é coleta de SKU, que é o que a
   > `acabamento` fez em 25/09 e em 02/10. **Não repita a procura de propriedade: ela acabou.**
   >
   > **E O ACHADO QUE VALE MAIS QUE O BLOCO, porque ele não é sobre rejunte: O EGRESSO NUNCA BARROU PDF.
   > ELE BARRA HOST.** Três blocos seguidos (`base` em 28/09, `apoio` em 28/09, a escada inteira desde
   > 10/09) pararam escrevendo alguma forma de *"o egresso não abre PDF de fabricante"*, e o pedido de rede
   > ao Raphael sempre foi escrito como *"liberem o domínio do fabricante"*. **Ninguém tinha medido um host
   > de TERCEIRO.** Medido hoje:
   >
   > | host | o que ele faz |
   > |---|---|
   > | `telhanorte.vteximg.com.br` | **ABRE.** Dois boletins Quartzolit baixados e lidos inteiros |
   > | `cdn.obramax.com.br` | `EGRESS_BLOCKED` |
   > | `bd-sp.canaldapeca.com.br` | `EGRESS_BLOCKED` |
   > | `www.quartzolit.weber` | 403, como em 29/09 e 30/09 |
   >
   > O CDN da Telha Norte — varejista do próprio grupo Saint-Gobain — serve o boletim técnico do fabricante
   > com cabeçalho, rodapé e data de revisão dele. Está escrito no esquema, em
   > `escada_de_fontes.canal_de_espelho`, com o que ele **não** autoriza: espelho **não** vira nível 1 (do
   > espelho sai o documento, não a garantia de que a revisão é a vigente) e espelho **não batiza** (o nome
   > do arquivo lá é `1200003.pdf`, código do varejista — a trava da 26.2 reprovava `Rejunte Piscinas
   > Quartzolit` dizendo que o fabricante não escreve esse nome, e o fabricante escreve, no título da
   > página 1). **O pedido do curinga `*.quartzolit.weber` continua de pé e continua sendo o caminho do
   > nível 1 — ele só deixou de ser a única porta.**
   >
   > **A PISTA QUE FICA, medida e não aberta:** o mesmo host serve **FISPQ** (`arquivos/101494.pdf`,
   > `arquivos/90387.pdf`). A FISPQ do epóxi é nomeada em `regras_da_categoria_apoio` como a **única** coisa
   > que segura o primeiro SKU de `apoio`, e a `base` para na mesma porta. **Não foram abertas e não se sabe
   > de que produto são** — é pista, não resultado.
   >
   > *(O texto abaixo é de três horas antes e fica sem uma palavra alterada: foi ele que nomeou a
   > propriedade que faltava, e acertou.)*
   >
   > **MEDIDO EM 05/10/2026 ÀS 10h3xZ — A SERP DAS TRÊS MÃES FOI OLHADA, E A FRASE ACIMA ESTAVA ERRADA NA
   > SEGUNDA METADE.** Medir a SERP de `alicate` **não** fez a segunda categoria do Guia sair, e o motivo é
   > que a frase acima confundiu dois portões: a mãe estava em `espera_serp`, mas o que a **16.5** cobra são
   > **3 filhas no cruzamento**, e as filhas não param na SERP — param no **dado**. As cinco medições novas
   > estão em `dados/serp-das-filhas.json` (de 10 para 15) e o veredito regerado em
   > `dados/cruzamento-14-9.md`:
   >
   > | recorte | antes | agora | o que falta AGORA |
   > |---|---|---|---|
   > | `alicate` (mãe) | `espera_serp` | **`pode_nascer`** | nada nela: os dois portões abriram |
   > | `rejunte` (mãe) | `espera_serp` | **`pode_nascer`** | nada nela: os dois portões abriram |
   > | `pastilha` (mãe) | `espera_serp` | `espera_autoridade` | autoridade — 7 de 9 da SERP são loja, fabricante ou marketplace |
   > | `rejunte/cimenticio` | `sem_nenhum_dos_dois` | **`espera_dado`** | **UMA coisa: um número que a página calcule sobre os 3 itens — `liberacao_area_molhada_h`** |
   > | `alicate/torques` | `sem_nenhum_dos_dois` | `sem_nenhum_dos_dois` | SERP saiu **TOMADA** (7 de 10 lojas): este recorte **não é** o caminho, e agora está medido |
   >
   > **O QUE ISTO DEIXA PARA A PRÓXIMA EXECUÇÃO, e é uma coisa só:** `espera_serp` **ZEROU** — não há mais
   > nenhum recorte com "dado verde e SERP nunca olhada", que este arquivo chamava de *"o caso que mais
   > custou nesta ilha, porque parece passe livre"*. **Daqui para frente o que falta no Guia é DADO, não
   > busca** — e o caminho mais curto para a segunda categoria é o **`rejunte`**, não o `alicate`: a mãe já
   > passa os dois portões e a filha `rejunte/cimenticio` está a **um número** de passar (os 3 itens já
   > existem; falta `liberacao_area_molhada_h` neles, que é declaração de fabricante, o mesmo tipo de lastro
   > que a `acabamento` juntou por busca em 25/09). As outras duas filhas de `rejunte` (`acrilico`, `epoxi`)
   > têm 1 item cada e precisam de 2 mais cada uma.
   >
   > **E UMA ARMADILHA DE CONSULTA FICOU MEDIDA, porque ela muda o que se vai escrever:** a consulta crua
   > `rejunte para mosaico` cai na SERP de **obra** (o corpus de 10/09 mediu isso: Omni, Viva Decora, cálculo
   > de piso), e a consulta em forma de pergunta sobre **peça artesanal** cai numa SERP com **ZERO
   > marketplace, ZERO loja e ZERO fabricante em 10 de 10** — a mais aberta que esta ilha já mediu. São
   > **duas SERPs vizinhas**, e a frase da página decide em qual ela aterrissa. Quem escrever a página de
   > `rejunte` mira a pergunta da peça, nunca o termo cru. A margem, porém, é de **UM** resultado, e isso
   > está escrito no `motivo` da medição: 8 dos 10 respondem obra e o décimo é a biografia de uma pessoa na
   > Wikipedia — SERP rala, não SERP conquistada.
   >
   > *(O texto abaixo é de três e seis horas antes e fica sem uma palavra alterada: foi ele que mandou
   > medir, e é ele que explica por que a categoria escolhida não foi escolhida.)*
   >
   > **ESTADO EM 02/10/2026 às 13h17Z — A METADE DESTE ITEM QUE TRAVAVA O 4c SAIU, E `acabamento` É A
   > PRIMEIRA CATEGORIA DO GUIA A PASSAR A 16.5.** O ponteiro de 30/09 abaixo mediu que o 4c esperava
   > **3 filhas de nível 3 numa categoria que já tem tipos**, e nomeou o caminho mais barato:
   > `acabamento`, **a 3 itens** — 1 impermeabilizante e 2 seladores, por busca. **Coletados hoje, os
   > três**: `suvinil-seladora-para-madeira`, `coral-selador-acrilico` e `coral-resina-acrilica`.
   > `acabamento/selador` foi de 1 para 3 e `acabamento/impermeabilizante` de 2 para 3, com lastro e
   > com número calculável (`tempo_de_secagem_h` nos três seladores, `base_quimica` nos três
   > impermeabilizantes); com o verniz, **3 de 3**. `dados/filhas-do-guia.json` registra `acabamento`
   > como a única categoria que alcança as 3, e a tabela da seção 2 do `ARVORE.md` foi para
   > `10 itens | 3 de 3` — corrigida pelo portão `--conferir`, não pela mão.
   >
   > **ATUALIZADO EM 02/10/2026 às 16h2xZ — O PORTÃO DE SERP TAMBÉM ABRIU, E AGORA OS DOIS SÃO UM
   > COMANDO.** O parágrafo abaixo é de três horas antes e dizia que o de SERP era outro. Ele foi
   > **medido**: `acabamento/selador` e `acabamento/impermeabilizante` nunca tinham tido SERP olhada, e
   > as duas saíram **ABERTAS**, como a `acabamento/verniz` de 30/09 e como a mãe `acabamento`, medida
   > hoje — fórum, blog de 2010 e resposta genérica sem número, **zero marketplace**. Com isso
   > `acabamento` passa os dois portões na mãe **e** nas três filhas da 16.5: **o 4c está liberado
   > nela**, e é a primeira categoria do Guia onde isso vale.
   >
   > **E a leitura dos dois portões deixou de ser trabalho de cabeça.** A metade de SERP era prosa num
   > arquivo que o gerador preservava sem ler; agora é dado em `dados/serp-das-filhas.json`, e
   > `ferramentas/cruzamento-14-9.py` devolve **um** veredito por recorte em `dados/cruzamento-14-9.md`
   > (32 casos de autoteste, `--conferir` de pé). Quem pegar o 4c **lê o veredito, não cruza na mão.**
   >
   > **O que o cruzamento achou e nenhum dos dois arquivos mostrava:** a 16.5 conta filhas, e filha não
   > é filha no dado — é no cruzamento. A `pastilha` tem **1 filha no dado e 0 no cruzamento**, porque
   > `pastilha/vidro`, a de mais banco da ilha, tem SERP de marketplace (`espera_autoridade`). E
   > `alicate`, `pastilha` e `rejunte` — as três mães — ficaram em `espera_serp`: **dado verde e SERP
   > nunca olhada**, que é o estado que parece passe livre.
   >
   > **O QUE SOBRA ANTES DE PUBLICAR, e é UMA coisa só:** a **faixa de volume** das seis consultas
   > abertas não existe — o Planejador é do Raphael, o campo está `null` em vez de estimado, e o pedido
   > está em `dados/despachos.md` com a lista derivada. **Ela não decide se a página nasce; decide a
   > ordem da leva** (1.2-b.3). Quem publicar o 4c de `acabamento` pode publicar sem ela, e **não pode
   > estimá-la**.
   >
   > *(O parágrafo seguinte fica como estava, sem uma palavra alterada, porque foi ele que mandou medir.)*
   >
   > **O QUE ISTO ABRE, E O QUE NÃO ABRE.** Abre o portão de **DADO** do 4c. **Não** abre o de SERP: a
   > medição da 14.9 em `dados/filhas-do-guia.md` diz que as filhas publicáveis desta ilha hoje têm
   > forma de **pergunta** e não de tipo (`verniz para peça de mosaico` ABERTA, `pastilhas de vidro
   > para mosaico` TOMADA), e **`verniz` não existe em `dados/corpus-buscas.md`** — sem faixa de volume
   > medida. Quem for publicar o 4c cruza os dois, que é o que a 14.9 manda com essas palavras. Os dois
   > vereditos saem juntos ou nenhum dos dois serve.
   >
   > **E A PARTE DESTE ITEM QUE CONTINUA INTEIRA:** `base` e `apoio` seguem em ZERO SKU e seguem
   > travadas pelo **curinga** de egresso, não por decisão — as duas têm regra escrita, portão de pé e
   > bateria verde (e as duas baterias estavam **vermelhas** no `main` desde 30/09, consertadas nesta
   > execução). A lista derivada do que falta liberar está em `dados/egresso-de-fontes.md`, e segue com
   > o Raphael.

3. **A COLETA DAS CATEGORIAS VAZIAS** — *(**PONTEIRO DE 30/09/2026: A PRIMEIRA FRASE DESTE ITEM ESTÁ INCOMPLETA E ELA É A QUE TRAVAVA A FILA.** Ele diz, três linhas abaixo, que a coleta das categorias vazias "continua sendo o que destrava o bloco **4c**" — e isso foi lido por quatro execuções como "o 4c espera `base` e `apoio`", que estão presas no egresso. **Medido agora:** o 4c espera a **16.5**, que são 3 filhas de nível 3 por categoria, e ela se fecha coletando **DENTRO de uma categoria que já tem tipos**, não nas vazias. A `apoio` nem tem nível 2 nesta árvore. O caminho mais barato é **`acabamento`, a 3 itens** — 1 impermeabilizante e 2 seladores —, alcançável por **busca**, que é como a própria `acabamento` saiu de zero em 25/09. O número inteiro, recorte por recorte, com a lista de compras das sete categorias e a classificação de SERP da 14.9, está em `dados/filhas-do-guia.md`, e o portão é `ferramentas/filhas-do-guia.py`. **`base` e `apoio` continuam presas no curinga do egresso e continuam NÃO sendo o caminho do 4c.**)* — eram quatro (`alicate`, `base`, `acabamento`, `apoio`) e **restam DUAS**: a `alicate` saiu de zero em 25/09/2026 às 16h43Z (6 itens) e a `acabamento` às 19h16Z do mesmo dia (7 itens). Continua sendo o que destrava o bloco **4c**, e nenhuma coleta de cola ou de rejunte a fecha. Está medido em `dados/cobertura.json` e explicado na seção 7b do `ARVORE.md`. O canal de busca alcança; o egresso direto aos domínios de fabricante, não. **`base` e `apoio` são as duas que sobram, e nenhuma das duas tem a linha do esquema que autoriza enchê-la sem decisão nova** — a `acabamento` também não tinha, e a decisão dela está em `regras_da_categoria_acabamento` do `dados/esquema-banco.json` (versão 4), que serve de molde para as outras duas.
   > **ESTADO EM 28/09/2026 às 10h16Z — A `base` JÁ TEM A DECISÃO DE CAMPO; O QUE FALTA NELA NÃO É DECISÃO, É FRASE DE FABRICANTE.** `regras_da_categoria_base` e `ponte_do_tipo_para_o_vocabulario_base` estão escritas no esquema (**versão 5**), com portão no `validar-banco.py` e `ferramentas/mutacoes-base.py` (20 de 20, 19 só os portões novos viram). **Nenhum SKU foi coletado**, e o motivo é o CANAL e não a rede: o egresso de fabricante continua em 000, e nesta execução a busca devolveu **resumo e tradução** das páginas de painel de MDF em vez da frase do fabricante — e `literal_do_fabricante` é a viga do esquema. Está escrito em `regras_da_categoria_base.o_que_falta_para_coletar_o_primeiro_SKU`.
   >
   > **A DECISÃO ACHOU UM BURACO QUE NÃO ERA DA CATEGORIA, E SIM DO VOCABULÁRIO:** dos cinco tipos de `tipo_por_categoria.base`, só `mdf_cru` e `cimento` pousam em `vocabularios.base`; `ceramica_crua` e `isopor_estrutural` **não têm valor** e `moldura` **não é material** (é forma, e forma aqui é a F1). Dois vernizes do banco carregam `isopor` e `gesso` na frase literal do fabricante, e as duas palavras não existem no vocabulário — declaração lida e descartada em silêncio. **Acrescentar os dois valores novos é decisão do Raphael e só pode sair DEPOIS da leitura de 30/09**, porque muda o que `/materiais/qual-cola-usar-no-mosaico/` (posição 7,8) serve: a lista suspensa ganha duas opções e a contagem da página sai de 270 para 330 combinações. **Pela ordem da fila, a próxima categoria a coletar é a `apoio`** — é a única ainda sem decisão de campo nenhuma e a de menor risco de egresso, porque espátula, óculos e luva são do mesmo terreno da `alicate`, que saiu de zero por busca.

   > **ESTADO EM 28/09/2026 às 14h55Z — A `apoio` TAMBÉM JÁ TEM A DECISÃO DE CAMPO, E AGORA NENHUMA DAS
   > SETE CATEGORIAS ESTÁ SEM A SUA.** `regras_da_categoria_apoio` (o objeto `servico`),
   > `ponte_do_tipo_de_apoio_para_o_ramo` (os seis tipos divididos em ferramenta × EPI) e
   > `exigencias_de_apoio_ja_declaradas_no_banco` estão no esquema (**versão 6**), com portão no
   > `validar-banco.py` e `ferramentas/mutacoes-apoio.py` (24 de 24, as 24 só o portão novo viu).
   > **Nenhum SKU foi coletado**, e o motivo é o de sempre: `dureza_shore_a` e `norma_declarada` moram em
   > PDF de fabricante, e o egresso não abre PDF. Está escrito em
   > `regras_da_categoria_apoio.o_que_falta_para_coletar_o_primeiro_SKU`.
   >
   > **O QUE A DECISÃO ACHOU, e é o achado que vale mais que a categoria:** cinco frases de fabricante, em
   > quatro registros de três categorias, **já nomeavam um apoio** e nenhuma tinha campo para onde ir — a
   > Pastilhart escreve *"desempenadeira de borracha para não riscar"* e as 13 pastilhas do banco são de
   > vidro. E o vocabulário aponta para o lado oposto do banco: dos **seis** tipos que
   > `tipo_por_categoria.apoio` declara, **um** aparece no banco; dos **dois** termos que mais aparecem
   > (`pincel`, `rolo`), **zero** estão no vocabulário. Os dois ficam como `sem_valor_no_vocabulario` com
   > `valor_proposto` escrito, e **isto NÃO espera 30/09** (nenhuma página lê `tipo_por_categoria`): é a
   > regra de crescimento — o valor nasce com o primeiro SKU que o use.
   >
   > **E o silêncio virou número:** o ramo do EPI tem **zero** declarações em 38 registros, e a F2
   > recomenda os dois epóxis do banco. O bloco não inventou recomendação de proteção; tornou
   > `risco_declarado` obrigatório mesmo null. **O que destrava é a FISPQ do epóxi — mesmo egresso de PDF
   > que segura o primeiro SKU da `base`. Terceiro bloco seguido parando na mesma porta.**
   >
   > **Pela ordem da fila, o que sobra das categorias vazias não é mais decisão de campo: é CANAL.** As
   > duas (`base` e `apoio`) têm a regra escrita, o portão de pé e a bateria verde, e as duas esperam a
   > mesma coisa — uma frase de fabricante que esta nuvem consiga citar literalmente.
   >
   > ~~**REMEDIDO EM 29/09/2026 às 10h20Z, E O CANAL CONTINUA FECHADO**~~ — o parágrafo de 29/09 dizia que
   > `quartzolit.weber`, `tekbond.com.br`, `loctite.com.br`, `cascola.com.br` e `pastilhart.com.br`
   > *"devolvem **403 ao CONNECT**"*. **Essa frase é FALSA desde algum momento entre 29/09 e 30/09, e
   > quem a derrubou foi a 20.2.** Ela fica riscada e não apagada porque foi ela que motivou o pedido
   > que o Raphael atendeu — pela metade.
   >
   > **REMEDIDO EM 30/09/2026 às 10h22Z, E A PORTA ESTÁ PELA METADE — FALTA O CURINGA, NÃO O DOMÍNIO.**
   > Os **apex** `quartzolit.weber`, `tekbond.com.br`, `cascola.com.br` e `loctite.com.br` **estabelecem o
   > CONNECT**: o túnel devolve `HTTP/1.1 200 Connection Established` e o **servidor de verdade** responde
   > **301**, com cabeçalho de Apache e de CloudFront, data e `content-length`. Os quatro domínios
   > **entraram na lista de rede**. E o ganho é **zero**, porque os quatro redirecionam tudo para o host
   > `www.` (a Loctite para `next.henkel-adhesives.com`), que continua em `connect_rejected` por política
   > de egresso — e as **36 URLs de boletim técnico** que os bancos desta ilha citam nesses domínios estão
   > **todas** em `www.`. `pastilhart.com.br` não entrou nem no apex.
   >
   > **A 20.1 sempre mandou os dois**, `<ilha>.com.br` **e** `*.<ilha>.com.br`; o que falta é exatamente a
   > metade que serve para algo. O pedido novo é **derivado da medição**, domínio por domínio, com quem
   > exige cada um, em `dados/egresso-de-fontes.md`, e a ferramenta que o produz é
   > `ferramentas/medir-egresso.py` (`--autoteste`, 29 casos fabricados). **Enquanto o curinga não entrar,
   > nenhuma execução da Fundação tira `base` ou `apoio` do zero** — e insistir é gastar bloco para
   > reescrever o mesmo motivo, que foi o que aconteceu quatro vezes entre 26/09 e 29/09.
   >
   > **A `base` continua bloqueada por outro motivo, e ele é inteiro:** os **dez** fabricantes de painel
   > que `regras_da_categoria_base` nomeia — `dexco`, `duratex`, `guararapes`, `arauco`, `berneck`,
   > `eternit`, `brasilit`, `termotecnica`, `isoeste`, `leroymerlin` — estão em **000 no apex E no `www.`**,
   > medido nas três passadas. Nenhum deles entrou na lista. A correção acima não os alcança.
   >
   > **E A LIÇÃO, que não é sobre estes domínios:** quatro execuções escreveram "403 ao CONNECT" e a
   > quinta mediu. Medir CONNECT **não é** medir entrega: um portão que olhasse só o CONNECT diria hoje
   > "liberado" e mandaria coletar o que não há como ler; um que olhasse só o código final diria
   > "bloqueado" e esconderia que falta **uma linha**, não uma decisão. Os dois vereditos saem juntos ou
   > nenhum dos dois serve — e é por isso que a ferramenta tem o veredito
   > `liberado_mas_sem_entrega`, que nenhuma das quatro passadas anteriores tinha como escrever.
4. ~~**A LINHA DA PEÇA NA TABELA DO `ARVORE.md`**~~ — **CUMPRIDO em 28/09/2026 às 19h3xZ** (casca **1.17.0**,
   Loja **1.4.0**, manifest na revisão **47**). E o item estava **mal descrito**: dizia "é conserto de TESTE, não
   de documento", e não era — a própria seção 5 já registrava em 28/09 às 11h0xZ que o conserto não era só no
   teste, e sim uma **decisão de chave** deixada para a Fundação pela 19.2. **Escolhida a chave por caminho
   inteiro** (`loja/<slug>`), e quem decidiu foi um segundo defeito que só existe com o slug nu e que a outra
   opção não consertaria: **peça com slug de página da raiz servia a trilha daquela página** — `sobre` saía como
   `Início › Sobre`, sem o nome da peça, com o `BreadcrumbList` apontando para `/sobre/`. Com o caminho inteiro a
   colisão deixa de existir por construção. O conserto tem duas pontas e **uma** função
   (`cdm_loja_caminho_da_peca()`), e o portão da tabela tem **três pernas** — documento × código, documento ×
   `dados/pecas.json` (a cópia da seção 24) e **todas** as 5 peças da cópia × código —, porque o número de peças
   não se digita no documento: quem publica peça é a artesã. `mutacoes-arvore.py` foi de 21 para **29, 29
   reprovadas**. Detalhe inteiro no `REGISTRO.md` de 28/09 e na seção 5 do `ARVORE.md`.
   > **E UMA MUTAÇÃO PRÉ-EXISTENTE ESTAVA INERTE, achada de passagem e consertada no mesmo commit:**
   > `dois slugs com o mesmo ultimo nivel` casava com a entrada `'sobre'` escrita em uma linha, e a casca 1.16.0
   > — de algumas horas antes nesta mesma quarta — quebrou a entrada em várias. A mutação passou a se declarar
   > INVÁLIDA, que a bancada conta como "passou", e a trava dos slugs repetidos ficou sem ninguém a vendo.
   > Conferido que já estava inerte **antes** deste bloco.

5. **A ESCADA DA 25.1 SUBIU DE VERDADE, E O QUE SOBRA NELA E DE TRES DONOS DIFERENTES.**
   **ENTREGUE em 29/09/2026 as 16h17Z** (manifest e `/status` na **revisao 49**): a escada saiu de
   `1:1 · 2:5 · 3:4 · 4:28` para `1:1 · 2:5 · 3:14 · 4:18` — dez materiais de acabamento, alicate e cola
   sairam do piso da 25.2 e ganharam **ficha de produto**, com foto medida, pela Open API (25.6) e pela
   regra de casamento de `ferramentas/casar-anuncio.py`. O que impedia isto nao era falta de trabalho e
   sim falta de portao: o cabecalho dos bancos dizia, desde 25/09 e com razao, que *"ficha exige casamento
   de item, que a 25.7 proibe sem prova de que o anuncio e daquele SKU"*. **A prova passou a existir**, com
   bancada (`teste-casamento.py`, 42 afirmacoes sobre titulos reais) e bateria (`mutacoes-casamento.py`,
   17 de 17 reprovadas), e `validar-banco.py` reconfere o titulo gravado passando-o pela regra **viva**.
   Detalhe inteiro no `REGISTRO.md` de 29/09.
   > **OS 18 QUE CONTINUAM NO DEGRAU 4 SE DIVIDEM EM TRES, E SO UM TERCO E DA FUNDACAO:**
   >
   > - **TREZE sao as pastilhas, e sao do RAPHAEL.** Nao foram nem tentadas: a Shopee nao anuncia a
   >   codificacao da Glass Mosaic, e o caminho continua sendo o campo
   >   `afiliado.tipo_de_casamento: "equivalente"` descrito em `dados/links-afiliado-pendentes.md`, com a
   >   frase na tela dizendo ao leitor que o produto e equivalente e nao o exato. **E decisao, nao coleta**
   >   — e sao a maior fatia do que resta, incluindo a vitrine inteira da F1.
   > - ~~**TRES sao da Quartzolit** (...) **Consertar e COLETA** (...) **esbarra no mesmo egresso**~~ —
   >   **MEDIDO E DERRUBADO NA MESMA QUARTA, as 19h16Z, e a correcao vale mais que o item.** O batismo
   >   do fabricante **ja estava no repositorio**, dentro do proprio registro, desde 25/09: `fontes[].url`
   >   guarda o boletim tecnico, e o **NOME DO ARQUIVO** e o fabricante escrevendo o nome do produto
   >   (`BT_Borracha Liquida Elastica Quartzolit_REV110624.pdf`). **Nao dependia do egresso.** O defeito
   >   era um so — `borracha-liquida-elastica` trazia `impermeabilizante`, palavra que veio do **CAMINHO**
   >   da pagina de produto, que e a **prateleira** do fabricante e nao o nome. Corrigido com a divergencia
   >   gravada, e o registro **subiu para o degrau 3** (escada `1:1 2:5 3:15 4:17`). A regra ja era do
   >   banco: `escada_de_fontes` manda o nivel mais alto vencer, e ninguem tinha aplicado isso a
   >   `nome_comercial`. Virou portao: `ferramentas/batismo-do-fabricante.py` + `teste-batismo.py` (59
   >   afirmacoes) + `mutacoes-batismo.py` (14 de 14), esquema **versao 8**.
   >   **O QUE SOBRA DA QUARTZOLIT SAO DOIS, e nao e coleta de nome:** `protetor-para-fachadas` e
   >   `fundo-selador` tem o nome **certo**, so em minusculas, e a caixa nao foi conferida de proposito —
   >   a unica fonte deles e a pagina de produto e o batismo chega pelo **SLUG**, que soletra as palavras
   >   e perde a tipografia. Capitalizar dali e palpite com cara de declaracao do fabricante. O que os
   >   segura no degrau 4 e a **Shopee**, nao o nome: nenhuma das chaves identificou um anuncio so.
   >   **Nao invente o nome comercial** — inventa-lo e a mesma familia do numero de tela digitado.
   >   **E a licao maior, que nao e sobre a Quartzolit:** quatro execucoes anotaram "esbarra no egresso"
   >   sem abrir a fonte que estava em casa. A **20.2** manda retestar bloqueio herdado antes de
   >   respeita-lo, e isso vale para bloqueio herdado de **documento** tanto quanto do `ESTADO.md`.
   > - **DOIS sao retentativa barata, e sao da FUNDACAO.** `cortag-torques-azulejista-corte-curvo` (as
   >   chaves devolvem o anuncio de corte RETO, e so duas ofertas voltam da chave larga — vale tentar uma
   >   chave nova, escrita para o anuncio e nao para a busca do site — **TENTADO em 29/09 as 19h2xZ com
   >   quatro chaves novas, e a resposta e que a Shopee NAO anuncia este produto: "cortag corte curvo" e
   >   "torques corte curvo" devolvem a torques de MOSAICO, que ja e outro registro deste banco, e casar
   >   as duas seria a armadilha 5 da 25.7. Nao e chave ruim; e catalogo que nao tem o item**) e
   >   `cascola-pl500-adesivo-de-montagem`
   >   (o anuncio diz `Cola **Adesiva** Montagem`, o registro diz `**Adesivo** de Montagem`, e a trava do
   >   nome comercial nao conhece genero — **REMEDIDO em 29/09 as 19h2xZ e o diagnostico do genero esta
   >   INCOMPLETO**: existe anuncio com o genero certo, `Adesivo de Montagem Monta e Fixa 360g PL500 -
   >   CASCOLA`, e ele cai pela palavra **`Interior`** e pela marca repetida dentro do `nome_comercial`,
   >   nao pelo genero. E o `nome_comercial` **nao e defeito**: ele e identico ao slug da propria pagina
   >   do fabricante (`cascola-adesivo-de-montagem---pl500-interior`), que e a unica fonte deste registro.
   >   Entao aqui nao ha nome a consertar; ha uma chave a escrever ou nada a fazer). **O que NAO vale e afrouxar a trava para o Cascola passar:**
   >   isso e criterio dobrado para caber no dado que veio (1.2-b.4), e a trava existe porque sem ela um
   >   `Selador PU30` entrou como `fundo selador` no ensaio deste mesmo bloco. Se for mexer, mexa na
   >   CHAVE ou no `nome_comercial`, com fonte — nunca na regua.
   >
   > **E o que este item deixa desbloqueado para quem vier:** a mesma ferramenta
   > (`ferramentas/coletar-shopee.py`) sobe o degrau de **qualquer** registro novo que nascer no degrau 4,
   > sem codigo novo — `--ensaio` mostra o que ela faria sem tocar no banco. Ela e o caminho normal de todo
   > item daqui em diante, nao um mutirao de uma vez.

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
- Programas de afiliado: **Shopee** (conta única do Arquipélago; Sub_id 1 = `clubedomosaico`, Sub_id 2 = código da página: `F1`, `F2`, `GUIA`, `GPASTILHAS`, `GALICATES`, `GCOLAS`, `TVASO`… — *a forma com hífen que ficava aqui (`G-PASTILHAS`, `G-ALICATES`, `G-COLAS`, `T-VASO`) é **recusada pela própria Shopee**: a seção 25.7 do `ARQUIPELAGO.md` mediu em 16/09/2026 que hífen e sublinhado dentro de um `sub_id` devolvem `[11001] Params Error : invalid sub id`, e esta mesma linha já tinha sido corrigida em 14/09 só na metade do Mercado Livre. O `GUIA` está aqui porque é o código que o banco desta ilha já usa em 13 registros de alicate. Corrigido pelo Pente Fino em 28/09/2026*) e **Mercado Livre** (etiqueta `clubedomosaico<codigo>`, tudo junto e em minúsculas: `clubedomosaicof1`, `clubedomosaicof2` — *a forma com hífen que ficava aqui é recusada pelo painel do ML, medido em 13/09/2026; ver seção 7 do `ARQUIPELAGO.md`. Corrigido pelo Pente Fino em 14/09/2026*). Amazon só com tráfego.
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

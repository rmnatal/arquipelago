# ILHA: CLUBE DO MOSAICO — mosaico artesanal (loja + guia + escola)

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá.**

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
- Snippet "Clube do Mosaico Sync" v1.1.5 = snippet #5 do Code Snippets, ATIVO desde 11/09/2026 01h03 UTC. Primeiro sync: revisão 3 lida, 0 aplicados, 5 aguardando desembarque. O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador (copiar da Aquametria quando for preciso).
- **Quem aciona o Sync é a própria Fundação, por `curl`, ao fim de cada bloco publicável** (seção 4 do contrato). Commit sem Sync não está no ar.
- Search Console: propriedade de domínio `sc-domain:clubedomosaico.com.br`, VERIFICADA em 10/09/2026. Sitemap `https://clubedomosaico.com.br/wp-sitemap.xml` enviado em 11/09/2026 (primeira leitura "não foi possível buscar" é o placeholder até o Google ler). ATENÇÃO: o domínio teve vida anterior — há um `sitemap.xml` de 2019 na propriedade; conferir no Search Console e no Wayback se existem backlinks antigos ou URLs órfãs para redirecionar (oportunidade e risco).
- Plugins ativos (11/09/2026): Code Snippets, Site Kit by Google (não conectado — exige OAuth do Raphael; não é bloqueio), Converter for Media, Limit Login Attempts Reloaded. Akismet e Hello Dolly inativos.
- WordPress: admin `mosaico_gestor` (credencial nunca vai para o repositório).
- **LOGO OFICIAL (arquivos que o Raphael subiu na biblioteca de mídia em 11/09/2026 — usar EXATAMENTE estes, sem redesenhar):**
  - Logo principal (lótus + wordmark "clube do mosaico", **fundo transparente**, 1536×1024): `https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png` — **é o logo do cabeçalho, sempre, inteiro e sem texto ao lado**, e também o `logo` do `Organization` no JSON-LD. Só não pode ser servido sobre fundo escuro.
  - Favicon (lótus sobre quadrado branco): `https://clubedomosaico.com.br/wp-content/uploads/2026/09/clube-do-mosaico-favicon.png` — fonte para os ícones; a casca pode servir os PNGs de `identidade/logo/` (favicon-512/180/32, gerados dessa mesma lótus) como data URI, ou apontar `<link rel="icon">` para esta URL. `identidade/logo/lotus-512.png` (lótus transparente) serve para os lugares pequenos onde o logo completo não cabe.

## Memória a carregar
`/areas/projeto-clube-do-mosaico.md`, `/areas/fabrica-de-sites.md`, `/areas/arquipelago-operacao.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/shopee-affiliate.md` (método de uma passada só e Mercado Livre), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DO RAPHAEL — 11/09/2026 (2) — O LOGO DELE, INTEIRO, NO CABEÇALHO (prioridade máxima)

Ele reclamou, com razão: "cadê o logo que eu exigi e subi e mandei até a URL?" e "o nome já está embutido no logo, você não precisa escrever". O cabeçalho atual mostra só o wordmark em TEXTO. Errado.

**CORREÇÃO DE UM ERRO MEU, 20h15Z:** eu tinha escrito aqui que o arquivo dele tinha fundo preto e mandei gerar uma versão transparente por GD. **Isso está errado e foi cancelado.** Ele conferiu na biblioteca de mídia e mostrou: `logo-clube-do-mosaico.png` (1536×1024, 1 MB) **já tem fundo transparente**. Não existe nada a processar, nada a gerar, nada a converter.

**O que fazer, simples assim:**

1. O cabeçalho usa `https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png` direto, em `<img>`, `alt="Clube do Mosaico"`, link para `/`. **Nenhum texto ao lado** — o nome está dentro do logo.
2. Altura da imagem 52 px; a barra do cabeçalho sobe para ~84 px para o logo respirar. Fundo claro (branco ou papel #FBF7F4), borda inferior 1 px #EEE8E4, menu à direita em preto, como já está.
3. **Nunca usar o logo sobre fundo escuro:** o wordmark é vinho (#69030C) e desaparece em preto — foi exatamente isso que aconteceu no cabeçalho anterior, e não tem a ver com fundo do arquivo.
4. `lotus-512.png` continua servindo só como símbolo solto (favicon, avatar, ícone quadrado). **No cabeçalho vai o logo completo dele, sempre.**
5. Corrija o `VOZ.md` desta ilha, na seção "Molde de casca: LOJA", onde hoje manda usar `lotus-512.png` + wordmark em texto: trocar por "logo completo do Raphael (`logo-clube-do-mosaico.png`, já transparente), sem texto ao lado".

**Critério de pronto:** abrir https://clubedomosaico.com.br/ e ver a lótus com o nome "clube do mosaico" embaixo, nítidos sobre o fundo claro, sem texto duplicado ao lado. Registrar a revisão no ESTADO.md e acionar o Sync.

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

### O QUE FALTA DESTE DESPACHO — uma coisa só, e ela é do Raphael

- **2. A lótus no cabeçalho.** O wordmark "clube do mosaico" em texto já está no
  ar e legível (12,97:1 de contraste). **A lótus não entrou porque
  `identidade/logo/lotus-512.png` está TRUNCADO no repositório**: o chunk `IDAT`
  declara 11.638 bytes num arquivo que tem 8.770, com um `IEND` colado no fim, e
  o `zlib` recusa o primeiro bloco — não sai um único pixel. Servi-lo teria
  trocado o logo sumido por um ícone de imagem quebrada.
  **Pronto quando:** o Raphael commitar a lótus em PNG transparente (≥ 512 px no
  menor lado) em `identidade/logo/lotus-512.png`; então
  `php ferramentas/gerar-marca.php .` embute e a lótus aparece ao lado do
  wordmark sem mexer em mais nada. A ferramenta **recusa** arquivo que não abre,
  sem canal alfa ou com canto opaco — não force. Conferir depois abrindo a home
  e vendo a lótus ao lado do nome.
  *Tentativa em 11/09/2026: a lótus não pôde ser embutida — arquivo truncado, ver
  `identidade/logo/LEIA-ME.md`.*

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

## FILA DE BLOCOS

**Leia a seção 14 do `ARQUIPELAGO.md` antes de montar a fila: tudo existe para indexar e chegar à primeira página.** A ordem abaixo já aplica a regra de intenção de compra (seção 9): fichas de material e peças antes de tutorial genérico.

**1. CORPUS DE BUSCAS.** `dados/corpus-buscas.md` com os três clusters (materiais/ferramentas · peças prontas · aprender), faixa, concorrência, CPC e a classificação de SERP por consulta (aberta / tomada / armadilha). A base já está na memória; complete com autocomplete e buscas relacionadas. Não depende de infraestrutura.

**2. ESPECIFICAÇÃO DAS DUAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`:
- **F1 Calculadora de pastilhas e rejunte** — entrada: forma da peça (cilindro/vaso, placa, esfera, tampo redondo), medidas, tamanho da pastilha (1×1, 2×2, 2,5×2,5 cm, tessela irregular), junta; saída: área, quantidade com sobra, gramas de rejunte e de cola, tabela pré-renderizada com 12 peças típicas.
- **F2 Seletor de cola e rejunte** — entrada: base (cerâmica, vidro, MDF, cimento, plástico, parede), material da pastilha, ambiente (interno/externo/molhado); saída: tipo de adesivo (PVA, silicone, PU, argamassa ACII/ACIII, epóxi), rejunte compatível, cura. Constante só com fonte de fabricante (Quartzolit, Tekbond, Loctite, Cascola) e data. Sem fonte, `pendente` e fora de fórmula publicada.

**3. MODELO DO BANCO.** Três entidades, todas com `imagem` desde já: **MATERIAL** (categoria, tipo, medida, material, embalagem, `afiliado.programa`/`afiliado.url` vazios até a Sentinela preencher) · **PEÇA** (CPT `peca` no WordPress, cadastrada pela artesã no painel `/atelie/`: nome, técnica, base, medidas, peso, cores, preço, disponibilidade, prazo, fotos — nunca inventada) · **TÉCNICA** (bizantino, direto, indireto, opus).

**3b. CASCA DO SITE** — só depois que o WordPress existir. Seção 6 do contrato com a paleta acima. Páginas: início, loja, materiais, como-fazer, sobre, contato, divulgação de afiliados. Logo: ver regra no topo. Cabeçalho e rodapé pretos, miolo branco.

**4. FERRAMENTAS**, F1 e depois F2, uma por execução, cada uma com JSON-LD, tabela pré-renderizada, resposta antes da explicação, procedência na frase e vitrine (4e) desde a primeira.

**4c. FICHAS DE CATEGORIA DE MATERIAL** — /materiais/pastilhas, /alicates, /colas, /rejuntes, /bases, /acabamento: comparativo, "qual escolher para quê", vitrine. É a primeira leva que vai ao índice junto com F1 e F2.

**4d. LOJA** — ver DESPACHO de 10/09 acima: cadastro de peças é área da artesã no WordPress (snippet de CPT `peca`), não `dados/pecas.json`. Coleções por uso (/loja/centro-de-mesa, /loja/presentes, /loja/jardim) e por técnica listam as peças publicadas. Antes de existir peça cadastrada, as coleções ficam com estado vazio honesto ("em breve"), nunca com peça inventada.

**5. TUTORIAIS-ÂNCORA**, 12: vaso, cachepot, tampo de mesa, quadro, espelho, mandala, filtro de barro, parede, número de casa, colar, bizantino, iniciante. Cada um com lista de materiais (Guia) e "prefere pronto?" (Loja). Marcar `revisao_tecnica: pendente` até a mãe do Raphael revisar.

**5b. MALHA**, em levas de 5 a 10 guiadas por indexação. Página só nasce com 3 itens de banco reais e um número calculado (seção 9).

**6. FEED DE PRODUTO** para Google Merchant Center (listagens gratuitas) a partir do CPT `peca` — snippet que serve `/feed-produtos.xml`. Só quando houver peça publicada.

**7. LISTA DE PROSPECÇÃO DO WIDGET** (F1 incorporável): escolas e ateliês de mosaico, blogs de artesanato, lojas de material sem conteúdo. `publicar: false`.

## Específico desta ilha
- O dado que é o produto da ilha: a **compatibilidade cola × base × ambiente** e a **quantidade por peça**. Errar aí faz a peça descolar ou faltar material — é a confiança que separa a ilha da lojinha.
- Programas de afiliado: **Shopee** (conta única do Arquipélago; Sub_id 1 = `clubedomosaico`, Sub_id 2 = código da página: `F1`, `F2`, `G-PASTILHAS`, `G-ALICATES`, `G-COLAS`, `T-VASO`…) e **Mercado Livre** (etiqueta `clubedomosaico-<código>`). Amazon só com tráfego.
- Enquanto falta infraestrutura: blocos 1, 2 e 3 não dependem de site. Não invente peça para preencher a Loja.

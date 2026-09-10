# ILHA: CLUBE DO MOSAICO — mosaico artesanal (loja + guia + escola)

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá.**

## O que esta ilha tem de diferente (leia antes de tudo)
Esta é a **terceira ilha** e a primeira que **não veio da Bússola**: é um projeto pessoal do Raphael. A mãe dele faz mosaico artesanal (vasos, colares, quadros). O site tem **três motores num domínio só**, e a malha fecha um ciclo comercial completo:
1. **LOJA** — venda direta das peças da mãe (margem cheia, produto próprio, sem afiliado).
2. **GUIA DE MATERIAIS** — fichas de pastilhas, alicates, colas, rejuntes, bases e acabamento, com vitrine de afiliado (Shopee e Mercado Livre).
3. **ESCOLA** — tutoriais "como fazer mosaico em X" e páginas de técnica, com lista de materiais linkada ao Guia e "prefere pronto?" linkado à Loja.

Consequências para a Fundação:
- **Existe uma artesã real.** É a única ilha com uma pessoa por trás. A página Sobre pode ter nome, ateliê e assinatura nas peças **só depois que o Raphael confirmar** (pendente em 10/09/2026). Até lá, "o ateliê".
- **Produto próprio não é afiliado.** Página de peça leva `Product` + `Offer` com preço real, disponibilidade ("pronta entrega" ou "sob encomenda, N dias") e botão **Comprar** que abre WhatsApp com mensagem pronta ou link de pagamento. Nunca `rel="sponsored"` em link de peça própria. Nunca inventar peça, preço, medida ou foto: **o catálogo vem de `dados/pecas.json`, preenchido a partir do material que o Raphael entregar** (fotos, medidas, peso, técnica, preço, prazo). Sem esse material, a Loja fica com as páginas de coleção prontas e vazias de peça, e o `ESTADO.md` diz isso.
- **O logo é fornecido pelo Raphael** e vai para `identidade/logo/` desta pasta. **Não reconstruir, não redesenhar, não vetorizar por conta própria.** Enquanto o arquivo não existir na pasta, a casca usa só o wordmark tipográfico ("clube do mosaico" em minúsculas) e o favicon fica pendente — registrar no `ESTADO.md` como `bloqueada_por: logo`. Quando o arquivo chegar, a casca passa a usar o arquivo exato, sem alteração.

## Identidade
- Nicho: mosaico artesanal no Brasil — o eixo paramétrico é **"o que comprar para fazer a peça X"** (qual cola/rejunte para qual base e ambiente; quantas pastilhas/rejunte para qual área) e **"qual peça pronta para qual uso"** (centro de mesa, presente, jardim).
- Domínio: clubedomosaico.com.br, registrado em 10/09/2026. Ilha nº 3 do Arquipélago.
- Paleta (lida pixel a pixel do logo, aprovada pelo Raphael em 10/09/2026): noite `#000000` (fundo de cabeçalho e rodapé; o logo vive sobre preto puro) · coral `#FC483B` (marca, **cor de sinal**: botões, preço, um uso por tela) · salmão `#FA7665` (pétalas laterais; só em ilustração e hover, nunca em texto sobre branco) · vinho `#69030C` (wordmark do logo) · rubi `#8A0F18` (links e texto de destaque sobre branco, 4,5:1 garantido) · papel `#FFFFFF` (fundo do miolo) · tinta `#1F1715` (texto) · traço `#E9DCD7` · legenda `#6E5F5B`. **Miolo branco e limpo, cara de e-commerce; o preto fica só em cabeçalho e rodapé.** Alerta técnica em âmbar `#B9791A`, nunca em vermelho (vermelho é a marca).
- Tipografia: **Outfit** (títulos e preço) · **Source Sans 3** (texto) · **JetBrains Mono** (medida, quantidade, unidade, código de produto, com `tabular-nums`). Texto corrido nunca vai em Mono.
- Símbolo: **o logo fornecido** (flor de lótus geométrica de sete pétalas em coral/salmão sobre preto, wordmark "clube do mosaico" em minúsculas arredondadas). Ver "O que esta ilha tem de diferente".
- Interface: padrão da seção 6 do contrato (hambúrguer no celular, vitrine em carrossel, promessa antes do formulário, favicon próprio). Sem contagem regressiva, sem "mais vendido" inventado.

## O buraco que esta ilha existe para ocupar
Medido em 10/09/2026 (Planejador de palavras-chave, conta do Raphael, faixas; SERP aberta no Chrome dele):
- **Não existe fazenda de conteúdo nem autoridade editorial** no mosaico artesanal BR. Top 10 de "material para mosaico", "alicate para mosaico", "vaso de mosaico": lojinhas WooCommerce pequenas (mosaicoemcasa, universodomosaico, onomosaicos, bsmosaicos, mosaikaescoladearte), listas do Mercado Livre, Pinterest, YouTube, Wikipedia, blog de 2012. **Ninguém responde as perguntas técnicas** (qual cola para qual base, quantas pastilhas por peça).
- Cauda exata do artesanato, 100–1.000/mês: material para mosaico · pastilhas para mosaico · pastilhas de vidro para mosaico · azulejo para mosaico · alicate para mosaico (+35 variantes de 10–100) · kit mosaico · curso de mosaico · espelho mosaico · loja de materiais para artesanato · presente artesanal · vaso decorado. 10–100: vaso de mosaico · colar de mosaico · cola para mosaico · rejunte para mosaico · base para mosaico · mandala de mosaico · mosaico para iniciantes · ~80 "como fazer mosaico em/de X".
- Cabeças que se alcançam por tabela, 1k–100k/mês: como fazer mosaico · mosaico bizantino · tesselas · material para artesanato · cachepots · vaso decoracao · vaso para mesa de jantar.
- **Três armadilhas, não construir em cima:** "quadro mosaico" (é quadro impresso em 5 painéis, outra intenção); "pastilha de vidro" sozinho e tudo com piso/piscina/cozinha/banheiro/pedra ferro/são tomé (revestimento de obra: Leroy, Portobello); "mosaico no instagram/canva/de fotos" (grade de feed).
- Corpus completo, com faixa, concorrência e CPC: gravar em `dados/corpus-buscas.md` no bloco 1 a partir do que está em `/areas/projeto-clube-do-mosaico.md`.

## Endpoints desta ilha
- Sync: `<preencher quando o WordPress existir>`
- Status: `<preencher quando o WordPress existir>`
- Search Console: propriedade de domínio `sc-domain:clubedomosaico.com.br` criada em 10/09/2026 (TXT já no DNS; verificação pendente de propagação).

## Memória a carregar
`/areas/projeto-clube-do-mosaico.md`, `/areas/fabrica-de-sites.md`, `/areas/arquipelago-operacao.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/shopee-affiliate.md` (método de uma passada só e Mercado Livre), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DA SESSÃO DE CONVERSA — 10/09/2026 — ÁREA DE CADASTRO DE PEÇAS (requisito do Raphael, "não pode esquecer disso")
A mãe do Raphael vai cadastrar as peças **ela mesma**, com login e senha próprios. Portanto o catálogo da Loja **NÃO vive no repositório**: `dados/pecas.json` é descartado. Ele vive no WordPress, e o bloco 4d passa a ser:

**4d. LOJA — snippet "Clube do Mosaico Loja — cadastro de peças"** (Code Snippets, um snippet, `publicar: true` quando o WordPress existir, depois da casca 3b):
- **Custom post type `peca`** (rótulo "Peças", ícone de loja, `has_archive` em `/loja/`, `rewrite` `/loja/<slug>/`, com título, editor para a descrição, imagem destacada e **galeria** (meta `_cdm_galeria`, lista de IDs de anexo, escolhida pela biblioteca de mídia com o seletor nativo `wp.media`, arrastar para ordenar). Suporte a `excerpt` para a frase curta do cartão.
- **Meta box "Ficha da peça"**, campos: preço (R$, decimal), disponibilidade (`pronta_entrega` | `sob_encomenda`) e prazo em dias, medidas (altura × largura × profundidade, cm), peso (g), base (cerâmica, vidro, MDF, cimento, outro), técnica (taxonomia), cores (texto curto), quantidade disponível. Tudo salvo com nonce e sanitização.
- **Taxonomias**: `colecao` (uso: centro de mesa, presente, jardim, parede, joia…) e `tecnica` (bizantino, direto, indireto, opus…). Termos iniciais criados pelo snippet, editáveis por ela.
- **Papel `artesa`** (rótulo "Artesã"): capabilities só de `peca` (criar, editar, publicar, excluir as próprias), `upload_files`, e nada mais — sem plugins, temas, usuários ou snippets. Ao entrar, o wp-admin dela mostra só Peças e Mídia (remover os outros menus por `admin_menu` para esse papel; barra de admin no front desligada). Tela de edição simples, com os campos em português claro e um texto de ajuda de 3 linhas no topo ("Título → foto principal → galeria → preço → publicar").
- **Usuário da artesã criado pelo snippet** na primeira execução, se não existir: login `artesa` (ou o nome que o Raphael passar), e-mail do Raphael (raphaeh9@gmail.com) até ela ter um, papel `artesa`. **A senha NUNCA é escrita no repositório nem em log**: o snippet gera uma senha aleatória descartada e dispara o fluxo nativo de redefinição (`retrieve_password`), então o link para criar a senha chega ao e-mail cadastrado. Registrar no `ESTADO.md` que o e-mail foi enviado. O Raphael repassa o acesso; ela troca a senha em Perfil.
- **Página pública da peça** (`single-peca`, renderizada pelo snippet com `template_include` ou filtro de conteúdo, sem tema custom): carrossel das fotos com `scroll-snap`, miniaturas clicáveis, zoom no toque; coluna com título, preço em destaque (cor de sinal), disponibilidade e prazo, ficha técnica em tabela (medidas, peso, base, técnica, cores), descrição, botão **Comprar** (abre WhatsApp com "Olá, quero a peça <título> (<url>)"; número do WhatsApp em uma option `cdm_whatsapp` que o Raphael preenche em Configurações → Loja), bloco "como esta peça é feita" linkando o tutorial da técnica (Escola) e "materiais usados" linkando o Guia. **JSON-LD `Product` + `Offer`** com preço real, `availability` (InStock/PreOrder), `image` = galeria, `brand` = Clube do Mosaico. Sem `rel="sponsored"`: é produto próprio. Padrão de interface da seção 6 (sem contagem regressiva, sem selo inventado); cara de e-commerce, miolo branco, coral só no preço e no botão.
- **Arquivo e coleções** (`/loja/`, `/loja/colecao/<termo>/`): grade de cartões (foto principal, título, preço, etiqueta de disponibilidade), filtro por coleção e técnica, ordenação por recente. Estado vazio honesto quando não há peça.
- **Página inicial** passa a ter uma faixa "Peças do ateliê" com as 4–8 últimas peças publicadas (query do CPT), quando houver.
- **Feed do Merchant Center (bloco 6)** e o **sitemap** passam a ler do CPT `peca`, não de JSON.
- Verificação obrigatória antes de `publicar: true`: `php -l`; cadastrar uma peça de TESTE pelo formulário (título "TESTE — apagar", com 3 imagens), abrir a página pública, conferir carrossel, JSON-LD válido, botão do WhatsApp, e **apagar a peça de teste**; conferir que o usuário `artesa` NÃO vê Plugins, Snippets, Usuários nem Configurações.

## FILA DE BLOCOS

**Leia a seção 14 do `ARQUIPELAGO.md` antes de montar a fila: tudo existe para indexar e chegar à primeira página.** A ordem abaixo já aplica a regra de intenção de compra (seção 9): fichas de material e peças antes de tutorial genérico.

**1. CORPUS DE BUSCAS.** `dados/corpus-buscas.md` com os três clusters (materiais/ferramentas · peças prontas · aprender), faixa, concorrência, CPC e a classificação de SERP por consulta (aberta / tomada / armadilha). A base já está na memória; complete com autocomplete e buscas relacionadas. Não depende de infraestrutura.

**2. ESPECIFICAÇÃO DAS DUAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`:
- **F1 Calculadora de pastilhas e rejunte** — entrada: forma da peça (cilindro/vaso, placa, esfera, tampo redondo), medidas, tamanho da pastilha (1×1, 2×2, 2,5×2,5 cm, tessela irregular), junta; saída: área, quantidade com sobra, gramas de rejunte e de cola, tabela pré-renderizada com 12 peças típicas.
- **F2 Seletor de cola e rejunte** — entrada: base (cerâmica, vidro, MDF, cimento, plástico, parede), material da pastilha, ambiente (interno/externo/molhado); saída: tipo de adesivo (PVA, silicone, PU, argamassa ACII/ACIII, epóxi), rejunte compatível, cura. Constante só com fonte de fabricante (Quartzolit, Tekbond, Loctite, Cascola) e data. Sem fonte, `pendente` e fora de fórmula publicada.

**3. MODELO DO BANCO.** Três entidades, todas com `imagem` desde já: **MATERIAL** (categoria, tipo, medida, material, embalagem, `afiliado.programa`/`afiliado.url` vazios até a Sentinela preencher) · **PEÇA** (`dados/pecas.json`: nome, técnica, base, medidas, peso, cores, preço, disponibilidade, prazo, fotos — só do que o Raphael entregar) · **TÉCNICA** (bizantino, direto, indireto, opus).

**3b. CASCA DO SITE** — só depois que o WordPress existir. Seção 6 do contrato com a paleta acima. Páginas: início, loja, materiais, como-fazer, sobre, contato, divulgação de afiliados. Logo: ver regra no topo. Cabeçalho e rodapé pretos, miolo branco.

**4. FERRAMENTAS**, F1 e depois F2, uma por execução, cada uma com JSON-LD, tabela pré-renderizada, resposta antes da explicação, procedência na frase e vitrine (4e) desde a primeira.

**4c. FICHAS DE CATEGORIA DE MATERIAL** — /materiais/pastilhas, /alicates, /colas, /rejuntes, /bases, /acabamento: comparativo, "qual escolher para quê", vitrine. É a primeira leva que vai ao índice junto com F1 e F2.

**4d. LOJA** — ver DESPACHO de 10/09 acima: cadastro de peças é área da artesã no WordPress (snippet de CPT `peca`), não `dados/pecas.json`. Coleções por uso (/loja/centro-de-mesa, /loja/presentes, /loja/jardim) e por técnica listam as peças publicadas. Antes de existir peça cadastrada, as coleções ficam com estado vazio honesto ("em breve"), nunca com peça inventada.

**5. TUTORIAIS-ÂNCORA**, 12: vaso, cachepot, tampo de mesa, quadro, espelho, mandala, filtro de barro, parede, número de casa, colar, bizantino, iniciante. Cada um com lista de materiais (Guia) e "prefere pronto?" (Loja). Marcar `revisao_tecnica: pendente` até a mãe do Raphael revisar.

**5b. MALHA**, em levas de 5 a 10 guiadas por indexação. Página só nasce com 3 itens de banco reais e um número calculado (seção 9).

**6. FEED DE PRODUTO** para Google Merchant Center (listagens gratuitas) a partir de `dados/pecas.json` — snippet que serve `/feed-produtos.xml`. Só quando houver peça real.

**7. LISTA DE PROSPECÇÃO DO WIDGET** (F1 incorporável): escolas e ateliês de mosaico, blogs de artesanato, lojas de material sem conteúdo. `publicar: false`.

## Específico desta ilha
- O dado que é o produto da ilha: a **compatibilidade cola × base × ambiente** e a **quantidade por peça**. Errar aí faz a peça descolar ou faltar material — é a confiança que separa a ilha da lojinha.
- Programas de afiliado: **Shopee** (conta única do Arquipélago; Sub_id 1 = `clubedomosaico`, Sub_id 2 = código da página: `F1`, `F2`, `G-PASTILHAS`, `G-ALICATES`, `G-COLAS`, `T-VASO`…) e **Mercado Livre** (etiqueta `clubedomosaico-<código>`). Amazon só com tráfego.
- Enquanto falta infraestrutura: blocos 1, 2 e 3 não dependem de site. Não invente peça para preencher a Loja.

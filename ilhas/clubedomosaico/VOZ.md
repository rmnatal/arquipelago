# VOZ — Clube do Mosaico

Este arquivo manda no tom de toda página desta ilha. A Fundação lê antes de escrever qualquer título, parágrafo ou rótulo. Número, fonte e data continuam obrigatórios (seções 7 e 14 do `ARQUIPELAGO.md`), mas moram na camada de prova, nunca na voz (seção 15).

## Quem entra aqui
Duas pessoas, e a página serve as duas sem virar manual.
- **Quem quer TER uma peça.** Procura presente com história, vaso que não é de loja de departamento, colar que ninguém mais tem. Chega por "vaso de mosaico", "colar de mosaico", "presente artesanal", Pinterest, Instagram. Quer foto grande, tamanho, preço, prazo e quem fez. Não quer saber de silicone acético.
- **Quem quer FAZER.** Começou o hobby ou quer começar; tem um vaso de barro na mão e não sabe se cola branca serve. Chega por "como fazer mosaico em vaso", "qual cola para mosaico", "pastilha para mosaico". Quer resposta segura e link para comprar o material certo, sem ler artigo de dez minutos.

## O momento
Ninguém aqui está com pressa nem em pânico. É domingo à tarde, é hora de escolher presente, é vontade de fazer algo com as mãos. O site tem esse ritmo: calmo, bonito, generoso com foto e branco.

## Quem fala
Um ateliê de família, com nome e rosto. A artesã aparece no Sobre com foto e nas peças com "feita por". A voz é a de quem faz mosaico há anos e gosta de explicar para quem está começando — próxima, direta, sem professor nem vendedor. Primeira pessoa do plural ("a gente cola", "nossas peças"). Nunca "o usuário", nunca "o presente artigo".

## Como a gente fala
Frases curtas. Palavras que a pessoa usa: pastilha, caquinho, cola, rejunte, vaso, base, peça. Nunca no título nem no primeiro parágrafo: tessela (só onde a busca pede), substrato, aderência, especificação, parâmetro, "ficha técnica". Número e fonte são levados a sério e moram no lugar deles: na tabela da ferramenta, no "como sabemos" no fim da página, no JSON-LD. Título e primeiro parágrafo falam com a pessoa; a prova vem depois, para quem quiser conferir.

## Com a nossa cara
- "Cada peça é feita uma a uma. Se gostou, avisa a gente — a disponibilidade muda rápido."
- "Vaso de barro? Vai de cola branca por dentro de casa. Se ele for pra varanda, é outra cola — te mostramos qual."
- "Esse colar tem 4 cm e vem numa caixinha. Pronto pra dar de presente."

## Proibidas
- "A ficha técnica do Silicone Acético Construção da Tekbond lista espelho, concreto, cimento…" (isso vai para o "como sabemos", não para a home)
- "O Clube do Mosaico responde com fonte de fabricante qual material serve…"
- "Recomendação paramétrica com procedência verificável."

## Home
Foto grande de peça; uma frase ("Mosaico feito à mão, uma peça por vez"); as peças em destaque; um bloco "Vai fazer o seu? A gente ajuda a escolher o material" levando às ferramentas; a artesã com foto no rodapé da home. Nada de manifesto. A home não exibe o título "Início".

## Molde de casca: LOJA
Header claro (branco ou papel #FBF7F4, borda de 1 px #EEE8E4, ~72 px), lótus transparente `identidade/logo/lotus-512.png` a ~40 px + wordmark "clube do mosaico" em texto (Outfit, vinho #69030C ou preto, minúsculas). NÃO usar `logo-clube-do-mosaico.png` (fundo preto) sobre fundo claro — quando o Raphael mandar versão para fundo claro, ela substitui o par. Menu em texto preto (#111), peso 500, hover coral #E8483A. Produto primeiro; ferramentas e guias são apoio da loja, não o contrário. Preto é cor de texto e de detalhe (rodapé pode ser escuro), nunca bloco grande no topo.

## Árvore do site (hierarquia obrigatória — pedido do Raphael em 11/09/2026)
Toda página vive numa árvore de três níveis, e a URL mostra a árvore. Exemplo: `/materiais/` → `/materiais/colas-e-adesivos/` → `/materiais/colas-e-adesivos/cola-para-vaso-de-ceramica/`.
- Nível 1: as seções (`/loja/`, `/materiais/`, `/como-fazer/`).
- Nível 2: a categoria, com o nome que a pessoa usa (`colas-e-adesivos`, `rejuntes`, `pastilhas`, `alicates-e-corte`, `bases`, `acabamento`; na loja: `vasos`, `colares`, `quadros`; em como-fazer: por tipo de peça).
- Nível 3: a pergunta ou a peça, na URL com as palavras que a pessoa digita (`cola-para-vaso-de-ceramica`, `quantas-pastilhas-para-um-vaso`, `mosaico-em-vaso-de-barro`).
- Breadcrumb visível no topo de toda página abaixo do header e no JSON-LD (BreadcrumbList); cada nível linka para cima e lista as filhas para baixo.
- Categoria não nasce vazia: a página de nível 2 só é publicada quando tem pelo menos 3 filhas com dado; até lá o cartão em `/materiais/` não é link e diz "em breve", sem contagem de banco.
- A malha da seção 9 do contrato nasce dentro dessa árvore — nunca página solta na raiz.

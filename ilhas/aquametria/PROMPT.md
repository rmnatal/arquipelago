# ILHA: AQUAMETRIA — aquarismo

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: aquarismo — calculadoras de dimensionamento e banco técnico.
- Domínio: https://aquametria.com.br (no ar desde 06/09/2026). Primeira ilha do Arquipélago.
- Paleta: tinta `#0D1B22` · lâmina `#0E7C8C` · papel `#F4F7F7` · superfície `#FFFFFF` · traço `#DDE5E6` · legenda `#5C7075` · alerta `#B5762A`.
- Tipografia: **Chivo** (títulos) · **IBM Plex Sans** (texto) · **IBM Plex Mono** (números, com `tabular-nums`).
- Símbolo: instrumento de precisão — recipiente graduado com linha de enchimento. **Sem peixe, sem bolha, sem mascote.**

## Endpoints desta ilha
- Sync: `https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
- Status: `https://aquametria.com.br/wp-json/aquametria/v1/status`
- O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador.

## Quem verifica esta ilha
- **Sentinela técnica**, todo dia 11h30 BRT, **no Chrome do Raphael**: abre cada página, executa cada calculadora e lê o console. Disparo dela com defeito descrito **tem prioridade sobre a fila**.
- **Sentinela estratégica**, quartas: funil, indexação, vendas, Shopee, backlink.

## Memória a carregar
`/areas/projeto-aquametria.md`, `/areas/aquametria-corpus-buscas.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/topics/dev-conventions.md`, `/areas/fabrica-de-sites.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## META DESTA ILHA — decidida pelo Raphael em 09/09/2026

A Aquametria só conta como completa quando estiver **entrando tráfego orgânico**: páginas indexadas no Google, aparecendo em busca e recebendo visita. Não é quantidade de calculadora publicada, e não é a primeira venda. Toda escolha de bloco se justifica por **indexação e visita** — o que não move essas duas coisas espera a vez.

Isso não afrouxa nenhuma regra do `ARQUIPELAGO.md`. Publicar rápido e errado é a maneira mais eficiente de não ser indexado.

## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz

**A reescrita da home e do header está CUMPRIDA** na execução das 15h16Z de 11/09/2026 (casca 1.4.0, revisão 40). O critério de pronto que o despacho pediu virou portão medido: `ferramentas/teste-voz.mjs` mede as quatro páginas da casca, uma por processo, e reprova termo proibido em título ou primeiro parágrafo. Dez mutações deliberadas em `ferramentas/mutacoes-voz.py`, dez reprovadas — inclusive a porta dos fundos, que é embrulhar a página inteira na classe que declara camada de prova.

**A árvore chegou às treze páginas — CUMPRIDO em 11/09/2026**, casca 1.5.0, manifest na revisão 43, `/status` conferido e as treze URLs abertas no ar. Breadcrumb com `BreadcrumbList` em doze delas (a home não tem, 16.3) e blocos "Veja também" nas oito páginas da árvore, com 2 a 4 irmãs derivadas e a frase que linka a mãe com a contagem contada. **Nenhuma URL nova**, que era a condição para isto caber antes de 16/09. Critério de pronto medido, não de olho: `ferramentas/teste-arvore.mjs` (288 afirmações, régua própria, e ele LÊ o `ARVORE.md` para cobrar que documento e código digam a mesma coisa), 14 mutações deliberadas em `ferramentas/mutacoes-arvore.py` — 14 reprovadas —, e 224 medições em Chromium nas treze páginas.

**O que continua de pé desta seção**, e trava até 16/09:
- **as oito páginas de nível 1 e 2** e a troca de pai/slug das existentes: travadas até a leitura de 16/09 por duas regras independentes (item 5 do despacho da Sentinela, e o T2 deste arquivo). O `ARVORE.md` seção 6 explica as duas. Quando destravar, o nível 2 da trilha e o do `BreadcrumbList` viram link sozinhos — quem resolve o endereço é `aquametria_casca_url_se_existir()`, então não há nada a lembrar.
- **a frase de mãe dos três guias** (16.4b), que só nasce junto com `/guias/`: hoje ela apontaria para página inexistente, e o portão cobra a ausência dela justamente para ninguém fechar isso com um endereço inventado.

**As nove páginas de `conteudo/` foram — CUMPRIDO em 11/09/2026**, casca 1.5.1, artigos 1.2.0, manifest na revisão 46. Nenhuma URL mudou. Os nove títulos passaram a ser o mesmo nome que a casca já publicava na trilha e nos cartões — **um nome por página, em toda superfície** —, os nove `<title>` entraram no teto de 65 caracteres (oito passavam), e os nove primeiros parágrafos viraram camada de voz: sem fabricante, sem data de leitura, em segunda pessoa. A procedência dos três artigos desceu um parágrafo dentro da própria caixa da resposta direta, marcada com `aqm-prova`, então a seção 5 continua inteira — quem cita a caixa leva a fonte junto.

O que mede isso agora é o mesmo `ferramentas/teste-voz.mjs`, que passou de 4 para **13 páginas** e de 86 para 293 afirmações, com as nove de `conteudo/` montadas pelo `render-pagina-completa.php` (os outros renderizadores montam metade da página). `ferramentas/mutacoes-voz.py` foi de 11 para **20 mutações, 20 reprovadas**. A régua que faltava e que nenhuma lista de palavra proibida pegaria: **procedência não abre página**, e **o degrau da trilha é igual ao H1** — em 8 das 9 páginas os dois diziam nomes diferentes a uma linha de distância.

ATUALIZAÇÃO 11/09 (Pauta): quando existir `pauta.md` nesta pasta (seção 17 do contrato), os guias entram na fila depois desta reescrita e da árvore, em levas por cluster; registrar no fecho de cada bloco quantos temas estão escritos / na fila / recusados.

## DESPACHO DA SENTINELA — 2026-09-10 (ronda diária, medida no Chrome do Raphael)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8, registre no `REGISTRO.md` como "despacho da Sentinela de 10/09 — item N cumprido", e apague daqui o item cumprido no mesmo commit.

O item 1 do despacho de 09/09 (a categoria "sem categoria" no sitemap) foi CONFERIDO E FECHADO nesta ronda: o `wp-sitemap.xml` lista só os dois provedores de post e de page, `/category/metodos/` serve `noindex, follow` e está fora do sitemap. Não volte a ele.

O item 1 (nenhuma das 13 URLs servia `<meta name="description">`) foi CUMPRIDO na execução das 17h15Z de 10/09/2026, revisão 34 conferida no `/status`. As 13 URLs servem uma description cada, entre 120 e 160 caracteres, texto diferente em cada uma, mais 6 tags `og:` e `twitter:card`. **A ronda seguinte confere, que quem constrói não aprova o próprio conserto.** O que ela precisa saber: o texto NÃO se edita dentro do snippet — ele mora no front matter de cada página de `conteudo/` e, para as quatro páginas da casca, em `dados/metas-seo.json`; quem escreve o mapa no snippet é `ferramentas/gerar-metas-descricao.py`, que recusa gerar fora da faixa de caracteres, com texto repetido ou com slug faltando. Sem `og:image` de propósito: a ilha não tem imagem própria hospedada, e declarar uma que não existe quebra o cartão.

O item 3 (três links internos caindo em 301) também foi CUMPRIDO na mesma execução. A causa de raiz não estava no HTML das calculadoras: `aquametria_casca_url_se_existir()` só procurava em `post_type` `page`, e os três artigos-âncora são `post` — as duas vias falhavam e quem chamava caía no último recurso, que monta `/<slug>/`. A casca 1.3.1 ganhou uma terceira via, por `post_name` em `post_type` `post`, então **o próximo artigo nasce com link canônico sem ninguém lembrar disto**. Medido no ar: os 16 endereços internos servidos pelas 13 páginas respondem 200, nenhum 301. O `conferir-slugs.py` agora reprova nos dois sentidos (artigo linkado sem data, página linkada com data), com teste negativo feito.

2. ~~A C5 se contradiz no bloco de produto.~~ **CUMPRIDO em 10/09/2026, C5 v1.4.0, revisão 35.** A Fundação escolheu o segundo caminho dos dois que o despacho ofereceu: **a elegibilidade estava certa e não mudou.** Aquecedor não se vende em 160 W; o teto da lista é de propósito o degrau comercial que cobre o topo da faixa, e a própria página anuncia isso duas telas acima ("na prateleira, isso vira um aquecedor de 200 W"). O que mentia era o rótulo. Agora a lista tem dois grupos com cabeçalho e frase próprios — "Dentro da faixa calculada — 110 a 160 W" e "O degrau comercial acima — 200 W" —, o cartão do degrau acima parou de dizer "aparece aqui porque atende ao seu número", o `h3` do bloco não afirma mais "atendem essa potência", e a tabela pré-renderizada (o lado que a IA lê sem JavaScript) avisa na célula quando o modelo escolhido passa do topo, o que acontece em 2 das 6 linhas. **A ordem não mudou:** distância até o topo da faixa dentro de cada grupo, e quem cabe na faixa vem antes. Com as entradas do despacho a lista serve 150, 150, 150 no primeiro grupo e 200, 200 no segundo. **Para a ronda seguinte:** o caso 15b do `teste-navegador-c5.mjs` reproduz a entrada exata e lê a ordem do DOM — é o portão que impede a contradição de voltar. Leia o cartão como um leitor leria; é isso que a verificação por regra não pega.

3. ~~Três links internos apontam para URL que redireciona (301).~~ **CUMPRIDO em 10/09/2026, revisão 34** — ver a nota acima. Aguardando a conferência da ronda seguinte.

4. **RECEITA — o topo da lista de produto está sem link de loja.** Isto é registro, não pedido de mudança de ordem: a ordem NÃO muda, e a regra de reportar continua valendo. Medido em 10/09: na C3 com 200 L, o 1º da lista (Atman AT-3338) não tem link de loja e os 4 seguintes têm; na C5 com 108 L, o 1º e o 2º (Atman AT-150 e Eheim Jäger 150 W) não têm e o 3º (Ocean Tech Warmer X-5 150 W) tem. Medido em 11/09 na C15: com 60 cm em alta exigência os TRÊS primeiros não têm link e só o 4º tem; na vitrine servida de 90 cm o 1º não tem e o 2º tem. O topo é o espaço mais caro da página. O desbloqueio é banco melhor ou segundo programa de afiliado, e isso é decisão do Raphael. Reporte em todo bloco quantos itens esperam link E quantos desses não têm loja possível hoje.

5. **NENHUMA PÁGINA NOVA ATÉ 16/09** (era o item 2 do despacho de 09/09; continua de pé, não foi cumprido nem vencido). Decisão da rampa: a leva de 08/09 (6 páginas) não indexou nenhuma, e as 7 indexadas não registraram impressão. Isso inclui a leva 2 da malha. Trabalhe vitrine (T8), banco, schema e links de afiliado — nada que crie URL nova. Pronto quando: a leitura de 16/09 reavaliar.
   → A categoria "Métodos" foi criada fora do sitemap e com `noindex` justamente para respeitar este item. Depois de 16/09, e só com texto próprio explicando o critério (seção 14.4 do `ARQUIPELAGO.md`), basta acrescentar `metodos` em `aquametria_seo_categorias_no_sitemap()` para ela entrar no sitemap e sair do `noindex` na mesma linha.

**O que esta ronda mediu e PASSOU, para a Fundação não refazer:** 13 de 13 URLs do sitemap em HTTP 200; zero link interno quebrado; zero página órfã; zero `&#038;` dentro de `<script>` nas 13 páginas; corpo nunca começa por metadado YAML; o script da calculadora está sempre no rodapé; tabela de exemplos servida no HTML das 5 calculadoras; JSON-LD válido em 8 de 8 páginas (WebApplication+FAQPage nas calculadoras, Article+FAQPage nos artigos); favicon próprio servido; `aria-expanded` e `aria-controls` no menu, com os links no HTML servido; revisão 33 no `/status` igual à do manifest; console sem mensagem nenhuma. Contas conferidas na mão, todas certas: C3 (200 L, comunitário, carga média → 350 a 2.000 L/h, com piso 1,76 x/h e teto 10 x/h); C5 (108 L, Δ 10 °C → 110 a 160 W); C12 (150 L, plantado → 190 mL a 1,88 L); C15 (100 L, exigência média → 2.000 a 4.000 lm); C1 (100 × 40 × 50 cm, vidro 8 mm → bruto 200 L, interno 186 L, real 175 L).

**Correções aplicadas pela Sentinela nesta ronda: nenhuma.** Os quatro defeitos acima moram em snippet ou em regra de elegibilidade, e a regra 3 da seção 12 manda parar e despachar.

## FILA DE BLOCOS — reordenada em 09/09/2026 pela meta de tráfego

**MODO MUTIRÃO, ligado em 09/09/2026 a pedido do Raphael:** ele quer a ilha fechada o quanto antes e tirou a regra de um bloco por execução PARA ESTA ILHA. Entregue quantos blocos couberem na sessão, em sequência, na ordem da fila — **verificando cada um pela seção 8 do `ARQUIPELAGO.md` antes de começar o próximo**, e respeitando integralmente a seção 13. O que **não** entra no mutirão: publicar a malha em massa. A malha continua saindo em leva de 5 a 10 páginas com medição no meio, porque é justamente o que protege a indexação — e indexação é a meta desta ilha.

Blocos 1 a 3b (buscas, especificação, banco inicial, casca) estão CONCLUÍDOS. Calculadoras publicadas e verificadas rodando: C1, C3, C5, C12, C15. C2, C7 e C8 saem da fila por ora — ferramenta nova não traz tráfego enquanto as que existem não estiverem indexadas.

**T1. MEDIR A INDEXAÇÃO — é o primeiro bloco, antes de qualquer construção.**
Não dá para otimizar tráfego às cegas, e a rampa da malha (seção 9 do `ARQUIPELAGO.md`) depende deste número para existir.
- Confirme se o Search Console está verificado para aquametria.com.br. Se não estiver, verificar É o bloco (Site Kit no wp-admin, no Chrome do Raphael) — reporte e pare aí.
- Se estiver: quantas URLs **indexadas**, quantas em **"descoberta — não indexada"**, quantas em **"rastreada — não indexada"**, quantas excluídas e por qual motivo. Impressões e cliques dos últimos 28 dias, por página.
- Confirme que o sitemap está submetido, que ele lista o que deve listar e que não lista o que não deve.
- Grave em `dados/indexacao.md` com a data. Este arquivo é histórico: cada medição vira uma seção nova, nunca sobrescreve a anterior — a série temporal é o que diz se a rampa pode dobrar.

**T2. LIMPAR O QUE ATRAPALHA A INDEXAÇÃO** (era o bloco 4d) — **CONCLUÍDO: no ar e verificado em 10/09/2026 (revisão 33).**
- ~~Os 3 artigos vivem em `/2026/09/08/<slug>/` e caem em `/category/uncategorized/`, que está no sitemap. Crie categoria de verdade e tire a "sem categoria" do sitemap.~~ Feito pelo snippet `aquametria-seo-tecnico` v1.0.0.
- ~~Confira canonical, paginação, e que nenhuma página fina de arquivo esteja no sitemap.~~ Conferido: o `rel_canonical` do núcleo continua ligado e não foi tocado; arquivo por data, autor, tag, anexo e busca saíram do índice; o provedor de autores e o de taxonomias saíram do `wp-sitemap.xml`; a página de anexo foi desligada pelo interruptor do núcleo. O provedor de posts nunca sai — é o sitemap da ilha.
- `robots.txt` já foi medido em 09/09 e está limpo — não mexa.
- **O que sobra deste bloco não é código:** a medição no ar, que depende do Chrome do Raphael (ver o item 1 do despacho). Enquanto ela não for feita, T2 não conta como entregue.
- **Fica anotado, e NÃO é para fazer agora:** os artigos vivem em `/2026/09/08/<slug>/`, um endereço com data que envelhece sozinho. Trocar a estrutura de permalink move URL, e a seção 12.1 proíbe mover URL de página posicionada. Como nenhum dos três tem impressão ainda, existe uma janela para trocar — mas ela só se abre depois que a leitura de 16/09 disser por que a leva de 08/09 não indexou. Trocar endereço antes de entender isso é somar uma variável a um diagnóstico que ainda não fechou.

**T3. BANCO DE DADOS** (era o bloco 4b) — **agora é bloco de tráfego, não de venda.**
O portão da malha exige 3 itens de banco reais e um número calculado próprio por página. Sem banco, não existe página nova legítima: o banco é o que limita quantas páginas a ilha PODE ter.
- (d) **Banco de espécies — faça este primeiro.** Ficha, não calculadora: temperatura, pH, porte adulto, espaço mínimo, comportamento, com fonte. Destrava "quantos litros para X peixes", que é o eixo que a Bússola verificou ABERTO e o de maior volume de busca da ilha.
- (a) Catálogo de iluminação de 30 a 120 cm cobrindo baixa/média/alta exigência, com lúmen e voltagem de fonte do fabricante. Hoje são 3 luminárias e a única com link (Ista I-401, 45 cm, 810 lm) não cai em faixa nenhuma.
- (c) Catálogo geral com ficha completa, referência de pelo menos 60 itens. A Sentinela mediu que a C5 a 108 L pede 110–150 W e os três aquecedores com link são 100/200/300 W — nenhum na janela.
- (b) Voltagem dos elétricos que faltam, com fonte e data. Não fechou: `voltagem: null` com o motivo. **Nunca chute 110 ou 220.**
- (e) Produto novo entra sem `afiliado.url`; quem gera o link é a Sentinela estratégica. Deixe o campo pronto e reporte quantos esperam link.

**T4. MALHA DE PÁGINAS** (era o bloco 5b) — **o motor de tráfego da ilha.**
Camadas: ficha de produto · ficha de espécie · página de volume · cruzamentos.
**Eixo:** as fazendas já tomaram "melhor filtro para aquário de X litros" — priorize "quantos litros para X peixes" e "quantos watts de aquecedor".
Portão, rampa e regra da malha estão na seção 9 do `ARQUIPELAGO.md` e **não são negociáveis**: primeira leva de 5 a 10 páginas, medir a indexação delas em `dados/indexacao.md`, e só dobrar se indexaram. Se ficaram em "descoberta — não indexada", NÃO aumente — investigue por quê.

**T5. ARTIGOS-ÂNCORA** (era o bloco 5). Pareados com cada calculadora, na mesma execução. Toda tabela técnica cita o manual do fabricante e leva data de verificação.

**T6. PROSPECÇÃO DO WIDGET** (era o bloco 6) — **subiu de prioridade.**
Em domínio novo sem link nenhum apontando para ele, backlink não é luxo: é o que faz o Google voltar a rastrear. É a única alavanca de link do projeto, já que não há link pago nem presença pessoal. Lojas de aquarismo brasileiras com site próprio, `publicar: false`.

**T7. SCHEMA E VISIBILIDADE EM IA** (era o bloco 4c) — segue **obrigatório em toda página nova**, conforme a seção 5 do `ARQUIPELAGO.md`. O retrofit das páginas antigas (JSON-LD zero em 13 de 13, medido pela Sentinela) encaixa entre blocos, duas calculadoras por vez, na ordem C3 e C5, depois C12 e C15, depois C1 e os artigos.
- **T7 FECHADO: 8 de 8 páginas.** As cinco calculadoras (C3, C5, C15, C12 e a C1 em 10/09/2026) e os três artigos-âncora (leva 4, 10/09/2026, snippet `aquametria-artigos.php` v1.0.0, revisão 33). O `conferir-entidades.mjs` não mostra nenhuma página com `jsonld_ok=0`; o `teste-navegador-visibilidade-ia.mjs` mede as cinco calculadoras (**155 afirmações**) e o `teste-navegador-artigos.mjs` mede os três artigos (**108 afirmações**), os dois com o JavaScript DESLIGADO e zero falha.
- **O que a leva dos artigos ensinou, e vale para toda ilha:** (a) **página de conteúdo se identifica pelo SLUG, página de ferramenta pelo shortcode** — artigo não tem formulário, e amarrar o JSON-LD à presença de um shortcode faria a página perder o schema no dia em que alguém tirasse o bloco do topo; (b) **tabela pré-renderizada NÃO se inventa** — os três artigos já serviam tabela própria em Markdown, e o portão da seção 5 é servir resposta citável, não servir uma tabela; (c) **a resposta direta de artigo entrega a TESE com número**, não um caso de exemplo, porque é ela que vai ser citada fora de contexto.
- **Fica pendente, de propósito e não por esquecimento: a `Organization` com `sameAs` na home**, que mora na casca. A Aquametria não tem perfil externo nenhum (o Raphael não aparece em ilha nenhuma), então `sameAs` sairia vazio ou inventado. Ela nasce quando o T6 der o primeiro perfil externo real.
- **O que a C1 ensinou, e vale para o próximo que montar tabela pré-renderizada:** o eixo pertence à PERGUNTA, não ao formato. C3, C5 e C12 indexam por litro; a C15 por centímetro de luminária; a C1 por centímetro de aquário, porque nela o litro é a SAÍDA — quem abre a página tem a fita métrica na mão e não sabe o volume. Uma tabela indexada por litro ali responderia à pergunta que a pessoa ainda não consegue fazer.
- **E o precedente do bloco sem produto:** a tabela da C1 não tem link de loja porque litragem é geometria e geometria não escolhe produto — o bloco de produto nasce nas calculadoras que leem o volume. A tabela **diz isso** em vez de ficar em silêncio, e o aviso dela cumpre a seção 7 do contrato explicando a ausência. Silêncio parece defeito.
- **Nasceu um teste novo, `ferramentas/teste-navegador-c1-tabela.mjs`** (28 afirmações, JavaScript LIGADO): põe a tabela servida contra a própria calculadora, linha por linha. Ele **não guarda número esperado nenhum** — lê as entradas da coluna do aquário, digita no formulário e compara — justamente para não virar mais uma asserção de ESTADO que vence sozinha. Copie o desenho ao medir tabela de outra ilha.
- **Cuidado que custou duas rodadas de teste na C15 e uma na C12:** não reaproveite classe CSS que o teste de navegador usa como localizador (`.aqm-c1-fontes`, `.aqm-c1-aviso-afiliado` e irmãs). Tabela nova e nota nova pedem classe nova, com o estilo herdado pela lista de seletores. Use as convenções que já existem: `-direta` para a resposta do topo, `-bloco-exemplos` para o painel, `-exemplos` para a tabela e `-aviso-tabela` para a nota dela.
- **Rode UM teste de navegador de cada vez.** Cada `page.goto()` espera as fontes do Google, que o egresso barra até o timeout de 30 s por navegação; três testes em paralelo disputam a máquina e todos rastejam. Medido em 09/09/2026.

**T8. VITRINE DE PRODUTO** (era o bloco 4e) — **FEITA NA C3 (v1.5.0, revisões 36 e 37), NA C5 (v1.5.0, revisão 38) e NA C15 (v1.3.0, revisão 39, em 11/09/2026). Falta só na C12.** Regras gerais na seção 6 do `ARQUIPELAGO.md`; o específico desta ilha:
- **Ordem do que falta: C12.** Na C1 provavelmente não nasce: litragem é geometria, e geometria não escolhe produto — o mesmo precedente que já vale para a tabela dela.
- **O QUE A C15 ENSINOU, e é o que a C12 tem que procurar antes de escrever uma linha: LEIA O CARTÃO COMO UM LEITOR LERIA, PORQUE FAIXA ABERTA MENTE EM SILÊNCIO.** A C15 tem um nível cuja faixa não tem teto declarado (alta exigência: a fonte publica "acima de 40 lm/L" e para aí). O filtro estava certo — aceitar qualquer fluxo acima do piso é o que a fonte sustenta —, mas a frase do cartão dizia "fica dentro da faixa de 40 a 60 lm/L" para TODO mundo, inclusive para uma luminária que entrega 115,1 lm/L num aquário de 60 cm. Nenhuma verificação por regra pegava isso, porque a regra de elegibilidade não estava errada. Conserto: dois grupos com frases próprias, o de baixo mostrando o número que ele realmente entrega, e o grupo indo para o DOM (`aqm-c15-produto-acima`) para o portão poder conferir que o cartão da vitrine diz o mesmo grupo que a lista técnica. **Antes de montar a vitrine da C12, procure na C12 a faixa que não tem um dos dois lados.**
- **E A C15 ENSINOU A ESCOLHER O AQUÁRIO DE REFERÊNCIA DA VITRINE SERVIDA SEM COLHER CEREJA:** varra todos os casos da tabela em todos os níveis, conte quantos produtos cada célula produz, escolha a célula que tem de três a cinco — e **publique o motivo na própria página**. Na C15 são 18 células, 9 com algum produto e 1 só com três ou mais dentro do intervalo publicado. Escolher o caso e calar o motivo é colher cereja; escolher e dizer por quê é medição, e vira conteúdo da entidade do mesmo jeito que a lista de barrados.
- **O QUE A C5 ENSINOU, E QUE MUDA COMO SE ESCOLHE A PRÓXIMA:** este arquivo dizia que a C5 vinha primeiro porque "11 dos 14 aquecedores com link têm foto". O número estava certo e a conclusão estava errada, porque ele foi medido no BANCO e a vitrine desenha o CATÁLOGO. Dos 27 aquecedores do banco, só 18 passam no `minimo_para_sugerir` — e 9 dos 11 que têm foto são justamente os que ficam de fora, por não declararem volume, faixa de ajuste ou voltagem. Resultado medido: a vitrine da C5 tem foto em 2 dos 18. **Ao escolher a próxima, conte foto e link DEPOIS do portão de elegibilidade, nunca antes.** Rode `python3 ferramentas/gerar-catalogo-*.py` e leia a linha "vitrine: N de M com link, K com foto" — ela é a medida certa.
- **A C5 também mostrou que o cartão precisa saber de qual GRUPO ele é.** A lista dela é partida em dois desde a 1.4.0 (dentro da faixa calculada / o degrau comercial acima), e cartão de vitrine não comporta cabeçalho de grupo sem quebrar o `scroll-snap`. A distinção viaja na frase da especificação, e a sequência é calculada UMA vez em `pintarProdutos()` e passada para `pintarVitrine()`. Calculador de ordem duplicado é combinar de divergir depois. Quem for montar vitrine em calculadora com lista agrupada copia isto, não a C3 crua.
- **Copie o desenho da C3, não reinvente.** Uma função de cartão em PHP e o espelho dela em JavaScript, com a MESMA marcação: duas marcações para o mesmo cartão viram dois CSS e, mais cedo do que se pensa, duas aparências. Duas vitrines por página — a pintada, dentro do resultado, e a **servida** no HTML para um caso de referência, porque crawler de IA não executa JavaScript.
- **A vitrine vem ANTES da ficha e da procedência** (contrato 7). E ela **nunca reordena nada**: desenha a mesma sequência que a lista técnica, e é isso que o teste da C3 mede como afirmação central.
- **Preço sai, e sai datado.** As frases de "não publicamos preço" daquela calculadora se reescrevem na MESMA versão em que a vitrine entra — página que mostra preço e diz que não publica preço se contradiz. Confira também as páginas de `conteudo/`: na C3 a contradição estava lá, e só apareceu ao ler a página no ar.
- **Acentue o `alt` das imagens daquele banco antes de gerar o catálogo.** `alt` é texto de tela: leitor de tela lê, crawler lê. Os geradores de filtros, de aquecedores e de iluminação já recusam gravar imagem sem `alt` — copie esse portão para o de mídia. Feito nos bancos de filtro (10/09), de aquecedor (10/09, 11 `alt`) e de iluminação (11/09, 10 `alt`); **falta só o de mídia.**
- Preencher `imagem` para os itens que já têm `afiliado.url`, usando a foto do próprio anúncio da Shopee. Se a nuvem não alcançar o CDN da Shopee, **guarde a URL com `verificado_em: null`** e deixe a Sentinela confirmar no navegador — não anule o campo. **Pendência nomeada da C5:** os três Roxin HT-1300/Q3 (100, 200 e 300 W) têm link e não têm foto, e a URL da foto só sai do painel da Shopee, no navegador do Raphael. São os avisos V20 do validador.
- O cartão diz a especificação que fez o produto entrar: "440 L/h — atende os 190 L do seu aquário".
- Linha de promessa no topo, curta, sem exclamação, sem tom de anúncio.
- A tabela de exemplos do T7 já resolve metade disso: inclua nela a coluna do produto que atende cada faixa.
- **Largura e altura não se inventam:** o banco não mediu as imagens e a ilha não grava dimensão que não mediu. `aspect-ratio: 1/1` com `object-fit: contain` cumpre o que a regra existe para garantir, que é o layout não saltar. Quando o banco trouxer medida, o código já imprime os atributos.

## Link interno obrigatório
Toda calculadora linka as outras que consomem o mesmo estado, a metodologia, o artigo pareado e as páginas de entidade. Nenhuma página órfã — página órfã não é rastreada.

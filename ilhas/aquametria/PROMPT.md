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

## DESPACHO DA SENTINELA — 2026-09-09 (1ª leitura semanal)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8, registre no `REGISTRO.md` como "despacho da Sentinela de 09/09 — item N cumprido", e apague daqui o item cumprido no mesmo commit.

1. **`/category/uncategorized/` responde 200 e está no sitemap.** Tirar do sitemap e pôr `noindex`. Mover os 3 artigos para uma categoria de verdade (já era o T2 — o dado de hoje confirma que é urgente). Pronto quando: `wp-sitemap.xml` não lista mais a URL e ela serve `<meta name="robots" content="noindex">`.
   → **CÓDIGO ESCRITO E VERIFICADO NO REPOSITÓRIO em 09/09/2026 às 21h (revisão 28), MAS NÃO NO AR.** O snippet `aquametria-seo-tecnico` (v1.0.0) cria a categoria "Métodos", esvazia a "sem categoria", troca a categoria padrão, tira o provedor de autores e o de taxonomias do `wp-sitemap.xml` e manda `noindex, follow` por `wp_robots`. **A nuvem não alcança o site (EGRESS_BLOCKED), então o Sync não foi acionado e a medição do despacho não foi feita.** Este item continua ABERTO até alguém no Chrome do Raphael: (a) abrir a URL do Sync, (b) conferir em `/wp-json/aquametria/v1/status` que a revisão aplicada é **28**, (c) conferir que `wp-sitemap.xml` não lista mais `/category/uncategorized/`, e (d) conferir que essa URL serve `noindex`. Só então apague este item.
2. **NENHUMA PÁGINA NOVA ATÉ 16/09.** Decisão da rampa: a leva de 08/09 (6 páginas) não indexou nenhuma e as 7 indexadas não registraram impressão. Isso inclui a leva 2 da malha. Trabalhe vitrine (4e), banco, schema, links de afiliado — nada que crie URL nova. Pronto quando: a leitura de 16/09 reavaliar.
   → A categoria "Métodos" foi criada **fora do sitemap e com `noindex`** justamente para respeitar este item: ela tira os artigos da "sem categoria" sem pedir ao Google que indexe URL nova. Depois de 16/09, e só com texto próprio explicando o critério (seção 14.4 do `ARQUIPELAGO.md`), basta acrescentar `metodos` em `aquametria_seo_categorias_no_sitemap()` para ela entrar no sitemap e sair do `noindex` na mesma linha.
3. **20 dos 29 produtos sem link não existem na Shopee** (Eheim, Atman canister, Chihiros, JBL). Como a ordem é por adequação técnica, melhorar o banco reduz links na tela. **Não mude a ordem.** O desbloqueio é segundo programa de afiliado, e isso é decisão do Raphael. Reporte em todo bloco quantos itens esperam link E quantos desses não têm loja possível hoje.

## FILA DE BLOCOS — reordenada em 09/09/2026 pela meta de tráfego

**MODO MUTIRÃO, ligado em 09/09/2026 a pedido do Raphael:** ele quer a ilha fechada o quanto antes e tirou a regra de um bloco por execução PARA ESTA ILHA. Entregue quantos blocos couberem na sessão, em sequência, na ordem da fila — **verificando cada um pela seção 8 do `ARQUIPELAGO.md` antes de começar o próximo**, e respeitando integralmente a seção 13. O que **não** entra no mutirão: publicar a malha em massa. A malha continua saindo em leva de 5 a 10 páginas com medição no meio, porque é justamente o que protege a indexação — e indexação é a meta desta ilha.

Blocos 1 a 3b (buscas, especificação, banco inicial, casca) estão CONCLUÍDOS. Calculadoras publicadas e verificadas rodando: C1, C3, C5, C12, C15. C2, C7 e C8 saem da fila por ora — ferramenta nova não traz tráfego enquanto as que existem não estiverem indexadas.

**T1. MEDIR A INDEXAÇÃO — é o primeiro bloco, antes de qualquer construção.**
Não dá para otimizar tráfego às cegas, e a rampa da malha (seção 9 do `ARQUIPELAGO.md`) depende deste número para existir.
- Confirme se o Search Console está verificado para aquametria.com.br. Se não estiver, verificar É o bloco (Site Kit no wp-admin, no Chrome do Raphael) — reporte e pare aí.
- Se estiver: quantas URLs **indexadas**, quantas em **"descoberta — não indexada"**, quantas em **"rastreada — não indexada"**, quantas excluídas e por qual motivo. Impressões e cliques dos últimos 28 dias, por página.
- Confirme que o sitemap está submetido, que ele lista o que deve listar e que não lista o que não deve.
- Grave em `dados/indexacao.md` com a data. Este arquivo é histórico: cada medição vira uma seção nova, nunca sobrescreve a anterior — a série temporal é o que diz se a rampa pode dobrar.

**T2. LIMPAR O QUE ATRAPALHA A INDEXAÇÃO** (era o bloco 4d) — **feito no repositório em 09/09/2026, revisão 28; falta o Sync.**
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
- **AS CINCO CALCULADORAS ESTÃO FEITAS: C3, C5, C15, C12 e — em 10/09/2026 às 11h37Z — a C1** (snippet v1.2.0, revisão 32). O `conferir-entidades.mjs` já não mostra nenhuma com `jsonld_ok=0`, e o `teste-navegador-visibilidade-ia.mjs` mede as cinco: **155 afirmações, JavaScript DESLIGADO, zero falha**.
- **Falta: os 3 artigos.** O molde das calculadoras não serve inteiro aqui — artigo não tem formulário, então "resposta antes da explicação" e JSON-LD valem, mas a tabela pré-renderizada só entra se o artigo tiver número próprio para pôr nela. Onde não tiver, **não invente tabela**: o portão da seção 5 é servir resposta citável, e tabela decorativa é pior que nenhuma.
- **O que a C1 ensinou, e vale para o próximo que montar tabela pré-renderizada:** o eixo pertence à PERGUNTA, não ao formato. C3, C5 e C12 indexam por litro; a C15 por centímetro de luminária; a C1 por centímetro de aquário, porque nela o litro é a SAÍDA — quem abre a página tem a fita métrica na mão e não sabe o volume. Uma tabela indexada por litro ali responderia à pergunta que a pessoa ainda não consegue fazer.
- **E o precedente do bloco sem produto:** a tabela da C1 não tem link de loja porque litragem é geometria e geometria não escolhe produto — o bloco de produto nasce nas calculadoras que leem o volume. A tabela **diz isso** em vez de ficar em silêncio, e o aviso dela cumpre a seção 7 do contrato explicando a ausência. Silêncio parece defeito.
- **Nasceu um teste novo, `ferramentas/teste-navegador-c1-tabela.mjs`** (28 afirmações, JavaScript LIGADO): põe a tabela servida contra a própria calculadora, linha por linha. Ele **não guarda número esperado nenhum** — lê as entradas da coluna do aquário, digita no formulário e compara — justamente para não virar mais uma asserção de ESTADO que vence sozinha. Copie o desenho ao medir tabela de outra ilha.
- **Cuidado que custou duas rodadas de teste na C15 e uma na C12:** não reaproveite classe CSS que o teste de navegador usa como localizador (`.aqm-c1-fontes`, `.aqm-c1-aviso-afiliado` e irmãs). Tabela nova e nota nova pedem classe nova, com o estilo herdado pela lista de seletores. Use as convenções que já existem: `-direta` para a resposta do topo, `-bloco-exemplos` para o painel, `-exemplos` para a tabela e `-aviso-tabela` para a nota dela.
- **Rode UM teste de navegador de cada vez.** Cada `page.goto()` espera as fontes do Google, que o egresso barra até o timeout de 30 s por navegação; três testes em paralelo disputam a máquina e todos rastejam. Medido em 09/09/2026.

**T8. VITRINE DE PRODUTO** (era o bloco 4e) — layout aprovado pelo Raphael em 09/09, continua na fila, mas é bloco de **conversão**, não de tráfego: entra depois do T4. Regras gerais na seção 6 do `ARQUIPELAGO.md`; o específico desta ilha:
- Preencher `imagem` para os itens que já têm `afiliado.url`, usando a foto do próprio anúncio da Shopee. Se a nuvem não alcançar o CDN da Shopee, **guarde a URL com `verificado_em: null`** e deixe a Sentinela confirmar no navegador — não anule o campo.
- O cartão diz a especificação que fez o produto entrar: "440 L/h — atende os 190 L do seu aquário".
- Linha de promessa no topo: "calcule a vazão do seu aquário e veja quais filtros atendem, com a faixa e a fonte de cada um". Curto, sem exclamação, sem tom de anúncio.
- A tabela de exemplos do T7 já resolve metade disso: inclua nela a coluna do produto que atende cada faixa.

## Link interno obrigatório
Toda calculadora linka as outras que consomem o mesmo estado, a metodologia, o artigo pareado e as páginas de entidade. Nenhuma página órfã — página órfã não é rastreada.

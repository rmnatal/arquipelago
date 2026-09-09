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

## FILA DE BLOCOS — reordenada em 09/09/2026 pela meta de tráfego

**MODO MUTIRÃO, ligado em 09/09/2026 a pedido do Raphael:** ele quer a ilha fechada o quanto antes e tirou a regra de um bloco por execução PARA ESTA ILHA. Entregue quantos blocos couberem na sessão, em sequência, na ordem da fila — **verificando cada um pela seção 8 do `ARQUIPELAGO.md` antes de começar o próximo**, e respeitando integralmente a seção 13. O que **não** entra no mutirão: publicar a malha em massa. A malha continua saindo em leva de 5 a 10 páginas com medição no meio, porque é justamente o que protege a indexação — e indexação é a meta desta ilha.

Blocos 1 a 3b (buscas, especificação, banco inicial, casca) estão CONCLUÍDOS. Calculadoras publicadas e verificadas rodando: C1, C3, C5, C12, C15. C2, C7 e C8 saem da fila por ora — ferramenta nova não traz tráfego enquanto as que existem não estiverem indexadas.

**T1. MEDIR A INDEXAÇÃO — é o primeiro bloco, antes de qualquer construção.**
Não dá para otimizar tráfego às cegas, e a rampa da malha (seção 9 do `ARQUIPELAGO.md`) depende deste número para existir.
- Confirme se o Search Console está verificado para aquametria.com.br. Se não estiver, verificar É o bloco (Site Kit no wp-admin, no Chrome do Raphael) — reporte e pare aí.
- Se estiver: quantas URLs **indexadas**, quantas em **"descoberta — não indexada"**, quantas em **"rastreada — não indexada"**, quantas excluídas e por qual motivo. Impressões e cliques dos últimos 28 dias, por página.
- Confirme que o sitemap está submetido, que ele lista o que deve listar e que não lista o que não deve.
- Grave em `dados/indexacao.md` com a data. Este arquivo é histórico: cada medição vira uma seção nova, nunca sobrescreve a anterior — a série temporal é o que diz se a rampa pode dobrar.

**T2. LIMPAR O QUE ATRAPALHA A INDEXAÇÃO** (era o bloco 4d)
- Os 3 artigos vivem em `/2026/09/08/<slug>/` e caem em `/category/uncategorized/`, que está no sitemap. Crie categoria de verdade e tire a "sem categoria" do sitemap.
- Confira canonical, paginação, e que nenhuma página fina de arquivo esteja no sitemap.
- `robots.txt` já foi medido em 09/09 e está limpo — não mexa.

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

**T8. VITRINE DE PRODUTO** (era o bloco 4e) — layout aprovado pelo Raphael em 09/09, continua na fila, mas é bloco de **conversão**, não de tráfego: entra depois do T4. Regras gerais na seção 6 do `ARQUIPELAGO.md`; o específico desta ilha:
- Preencher `imagem` para os itens que já têm `afiliado.url`, usando a foto do próprio anúncio da Shopee. Se a nuvem não alcançar o CDN da Shopee, **guarde a URL com `verificado_em: null`** e deixe a Sentinela confirmar no navegador — não anule o campo.
- O cartão diz a especificação que fez o produto entrar: "440 L/h — atende os 190 L do seu aquário".
- Linha de promessa no topo: "calcule a vazão do seu aquário e veja quais filtros atendem, com a faixa e a fonte de cada um". Curto, sem exclamação, sem tom de anúncio.
- A tabela de exemplos do T7 já resolve metade disso: inclua nela a coluna do produto que atende cada faixa.

## Link interno obrigatório
Toda calculadora linka as outras que consomem o mesmo estado, a metodologia, o artigo pareado e as páginas de entidade. Nenhuma página órfã — página órfã não é rastreada.

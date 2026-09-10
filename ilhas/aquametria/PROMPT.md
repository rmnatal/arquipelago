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

## DESPACHO DA SENTINELA — 2026-09-10 (ronda diária, medida no Chrome do Raphael)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8, registre no `REGISTRO.md` como "despacho da Sentinela de 10/09 — item N cumprido", e apague daqui o item cumprido no mesmo commit.

O item 1 do despacho de 09/09 (a categoria "sem categoria" no sitemap) foi CONFERIDO E FECHADO nesta ronda: o `wp-sitemap.xml` lista só os dois provedores de post e de page, `/category/metodos/` serve `noindex, follow` e está fora do sitemap. Não volte a ele.

1. **NENHUMA PÁGINA TEM `<meta name="description">`. Nem uma, nas 13 URLs do sitemap.** Também não existe nenhuma tag `og:` em página nenhuma. Medido em 10/09/2026 no navegador: o `<head>` traz 6 elementos `<meta>` em toda página, e nenhum deles é `description`. Isto é código de snippet, então a Sentinela não toca (regra 3 da seção 12). É o defeito mais caro da ilha hoje: a meta description é metade da alavanca de CTR da seção 12.1, e a meta desta ilha é tráfego. Escreva uma meta description por página, com a consulta da página nas palavras da consulta e a promessa do número. Pronto quando: as 13 URLs do sitemap servirem `<meta name="description" content="...">` com 120 a 160 caracteres, texto diferente em cada uma, e a ronda seguinte medir zero página sem description.

2. **A C5 se contradiz no bloco de produto.** Entradas reais usadas na medição: volume 108 L, mínima do cômodo 16 °C, alvo 26 °C, 220 V, tampado. A resposta publicada foi **110 a 160 W** (1,00 a 1,50 W/L). No grupo cujo título é "Aquecedores que atendem essa potência" aparecem o **Atman AT-200** e o **Eheim Jäger 200 W**, e o texto do próprio cartão diz "entrega 1,85 W por litro, **contra** os 1,00 a 1,50 W/L que a sua diferença de 10,0 °C pede" — e mesmo assim o rodapé do cartão do AT-200 afirma "Ele aparece aqui porque atende ao seu número, e é só isso que decide a lista". Ou 200 W é elegível de propósito, por ser a medida comercial acima que a própria saída exibe como "potência comercial 200 W", e então o título do grupo e a frase do cartão estão errados; ou 200 W não é elegível, e então a regra de elegibilidade está errada. Isso é elegibilidade, é da Fundação, e a Sentinela não escolhe qual das duas. Pronto quando: com essas mesmas entradas, nenhum produto do grupo "atendem" tiver W/L fora da faixa publicada, OU o grupo tiver título e frase próprios que digam por que a medida comercial acima entra — e a ronda seguinte, lendo o cartão como um leitor leria, não encontrar contradição.

3. **Três links internos apontam para URL que redireciona (301).** Cada calculadora linka o artigo pareado sem o prefixo de data:
   - `/calculadora-de-potencia-do-aquecedor/` linka `/quantos-watts-de-aquecedor-para-aquario/` → 301 para `/2026/09/08/quantos-watts-de-aquecedor-para-aquario/`
   - `/calculadora-de-midia-filtrante/` linka `/quanta-midia-biologica-o-aquario-precisa/` → 301 para `/2026/09/08/quanta-midia-biologica-o-aquario-precisa/`
   - `/calculadora-de-iluminacao/` linka `/quantos-lumens-por-litro-aquario-plantado/` → 301 para `/2026/09/08/quantos-lumens-por-litro-aquario-plantado/`
   O link está dentro do snippet das calculadoras, então a Sentinela não toca. Troque o href pela URL canônica, com a data. Salto de redirecionamento é orçamento de rastreamento gasto à toa, e orçamento de rastreamento é o recurso escasso da seção 14.1. Pronto quando: nenhuma página servida contiver link interno que devolva 301, medido com `redirect: 'manual'`.

4. **RECEITA — o topo da lista de produto está sem link de loja.** Isto é registro, não pedido de mudança de ordem: a ordem NÃO muda, e a regra de reportar continua valendo. Medido hoje: na C3 com 200 L, o 1º da lista (Atman AT-3338) não tem link de loja e os 4 seguintes têm; na C5 com 108 L, o 1º e o 2º (Atman AT-150 e Eheim Jäger 150 W) não têm e o 3º (Ocean Tech Warmer X-5 150 W) tem. O topo é o espaço mais caro da página. O desbloqueio é banco melhor ou segundo programa de afiliado, e isso é decisão do Raphael. Reporte em todo bloco quantos itens esperam link E quantos desses não têm loja possível hoje.

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

**T8. VITRINE DE PRODUTO** (era o bloco 4e) — layout aprovado pelo Raphael em 09/09, continua na fila, mas é bloco de **conversão**, não de tráfego: entra depois do T4. Regras gerais na seção 6 do `ARQUIPELAGO.md`; o específico desta ilha:
- Preencher `imagem` para os itens que já têm `afiliado.url`, usando a foto do próprio anúncio da Shopee. Se a nuvem não alcançar o CDN da Shopee, **guarde a URL com `verificado_em: null`** e deixe a Sentinela confirmar no navegador — não anule o campo.
- O cartão diz a especificação que fez o produto entrar: "440 L/h — atende os 190 L do seu aquário".
- Linha de promessa no topo: "calcule a vazão do seu aquário e veja quais filtros atendem, com a faixa e a fonte de cada um". Curto, sem exclamação, sem tom de anúncio.
- A tabela de exemplos do T7 já resolve metade disso: inclua nela a coluna do produto que atende cada faixa.

## Link interno obrigatório
Toda calculadora linka as outras que consomem o mesmo estado, a metodologia, o artigo pareado e as páginas de entidade. Nenhuma página órfã — página órfã não é rastreada.

---
ilha: robometria
estado: nascendo
prioridade: 1
ultima_execucao: 2026-09-10T21:15Z
executando_desde: null
bloco_atual: "bloco 5 ENTREGUE: o ARTIGO-ANCORA da R1 esta no ar (/filtro-universal-de-robo-aspirador/, snippet robometria-a1 v1.0.0, manifest revisao 11). A tese e medida, nao escrita: das 16 pecas com compatibilidade declarada NENHUMA atravessa marca, a maior lista do banco nomeia 5 codigos de modelo, e na Electrolux as 6 pecas formam 6 conjuntos de modelos DIFERENTES. O numero nao esta digitado no HTML — a frase de abertura, a description do JSON-LD e a resposta do FAQPage tem duas formas escolhidas pela contagem, e foi provando isso numa copia do banco que apareceu o defeito de a pagina se corrigir na tela e o JSON-LD nao. A malha da secao 9 fechou: duas listagens (home e hub), tres irmas, e a R1 (v1.1.1) apontando de volta. A folha e as funcoes da porta de compra sairam da R1 para a casca (v1.0.2), que agora tambem tem catalogo de artigos. Verificacao: teste-a1 53, teste-casca 64, teste-r1 90, validar-banco, e Chromium com 0 px de rolagem horizontal em 360/390/782/1200. 16 pecas esperando link de afiliado. Proximo: 3c alvo (a), pecas com codigo da Xiaomi e da WAP, se a rede alcancar o fabricante; se nao, a R2"
ultima_ronda: null
bloqueada_por: null
---

# Estado da ilha Robometria

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura

- **Domínio:** robometria.com.br, registrado em 09/09/2026.
- **Hospedagem:** domínio adicional já criado no cPanel da HostGator, com raiz
  própria — mesmo plano da Aquametria, custo extra zero.
- **DNS:** nameservers `ns604.hostgator.com.br` e `ns605.hostgator.com.br`
  apontados no registro.br.
- **DNS propagado em 09/09/2026** — o domínio resolve para 108.179.253.218
  (br604-ip04.hostgator.com.br), o mesmo servidor da Aquametria.
- **WordPress: INSTALADO em 09/09/2026, 16h17 BRT**, via Softaculous, em
  https://robometria.com.br, na raiz do domínio. Versão 7.1, idioma pt_BR,
  instalação limpa (nenhum plugin de brinde do Softaculous). Usuário
  administrador não é `admin`. Credenciais foram por e-mail ao Raphael e não
  entram neste arquivo. **Medido no navegador do Raphael pela sessão de
  conversa** — a Fundação estava certa em não escrever isto sem medir.
- **SSL: EMITIDO** durante a madrugada de 10/09/2026 (Let's Encrypt via AutoSSL, ~14 h depois da instalação — dentro das 24 h oficiais). O site abre em https com o título certo.
- **ARMADILHA:** testar TLS pela nuvem não vale — o proxy de saída intercepta e apresenta certificado próprio. Certificado só se confere no navegador.
- **Plugins (10/09/2026):** Code Snippets, Site Kit by Google, Converter for Media e Limit Login Attempts Reloaded instalados e ATIVOS. Akismet e Hello Dolly estão desativados (a exclusão foi barrada pelo classificador de segurança; fica para o Raphael, é cosmético). Site Kit ainda **não conectado** à conta Google — exige autorização OAuth do Raphael; não é bloqueio, porque a propriedade de domínio no Search Console já existe.
- **Snippet de Sync: "Robometria Sync" v1.1.5, snippet #5 do Code Snippets, ATIVO desde 10/09/2026** — fonte em `snippets/robometria-sync.php` (sha256 `b4fa6b84…`), token gerado pelo próprio WordPress. **Primeiro sync executado às 13:09 UTC: revisão 6 lida, 0 aplicados, 9 aguardando desembarque** — correto, porque os 9 itens do manifest são pesquisa com `publicar: false`. Endpoints no `PROMPT.md`.
- **Search Console: propriedade de domínio `sc-domain:robometria.com.br` criada e VERIFICADA em 09/09/2026** (TXT `google-site-verification=xvI914rD2M69UhAao_MF2csPC3XAKKSUmol9JU-xxwg` gravado no Editor de Zona DNS; passo 4b da seção 11). Sitemap `wp-sitemap.xml` submetido em 10/09/2026. **O "não foi possível buscar" do Google NÃO era normalidade de domínio novo, como se supôs aqui: era defeito.** Os sitemaps serviam XML válido com status HTTP **404**, e sitemap com 404 é sitemap inexistente. Consertado em 10/09 às 15h49Z (casca 1.0.1) — hoje `wp-sitemap.xml` devolve **200**. **Falta reenviar o sitemap no Search Console**, e isso exige o navegador do Raphael. `dados/indexacao.md` aberto com a linha zero.
- **Identidade visual:** aprovada pelo Raphael em 09/09/2026. Paleta, tipografia
  e a geometria do símbolo estão no `PROMPT.md` desta pasta.

Sem credenciais neste arquivo.

## O que já foi entregue

- 10/09/2026 — **Bloco 5: o ARTIGO-ÂNCORA da R1 existe, e a malha da ilha fechou
  nos dois sentidos.** `snippets/robometria-a1.php` v1.0.0 publica
  `/filtro-universal-de-robo-aspirador/`, a primeira página desta ilha que não é
  ferramenta nem casca, com `ferramentas/gerar-a1.py`, `dados/a1-fatos.json` (o
  combustível, `publicar: true`) e `ferramentas/teste-a1.php`. **A tese é uma
  medição:** das 16 peças com compatibilidade declarada, nenhuma é declarada para
  modelos de mais de uma marca; a lista mais longa do banco inteiro nomeia 5
  códigos de modelo; e as 6 peças da Electrolux formam 6 conjuntos de modelos
  DIFERENTES, ou seja, compatibilidade não se herda nem dentro da própria marca.
  **O número não está digitado no HTML** — a frase de abertura, a `description`
  do JSON-LD e a resposta do FAQPage têm duas formas escolhidas pela contagem, e
  foi ao provar isso numa cópia do banco com uma peça multimarca plantada que
  apareceu o defeito de a página se corrigir na tela e **o JSON-LD continuar
  afirmando o que deixou de valer**, corrigido antes do desembarque. A casca
  subiu para 1.0.2 (catálogo de artigos, as duas listagens e a folha
  compartilhada da porta de compra) e a R1 para 1.1.1 (aponta de volta, e delega
  as funções de compra à casca). Manifest na **revisão 11**. **Verificação:**
  `teste-a1.php` APROVADO em 53 medições — entre elas a recontagem da tese em
  PHP, direto do banco, sem olhar para o gerador em Python —, mais
  `teste-casca.php` (64), `teste-r1.php` (90), `validar-banco.py` e um Chromium
  de verdade com 0 px de rolagem horizontal a 360, 390, 782 e 1200. **16 peças
  esperando link de afiliado.**

- 10/09/2026 — **Despacho da Sentinela, item 0: a procedência deixou de ser a
  única porta de compra.** A R1 tinha nascido com um único link clicável por
  peça, e ele ia para a loja do FABRICANTE: 12 links externos na consulta que a
  Sentinela mediu, nenhum de afiliado. Pela seção 7 do contrato, a R1 v1.1.0
  (manifest revisão 10) serve o bloco "Onde comprar estas peças" ANTES da prova
  de procedência, com o aviso de comissão dentro dele; a procedência virou link
  de texto "fonte" com `rel="nofollow noopener"`, sem fundo e sem preenchimento
  no CSS; o bloco existe mesmo com `afiliado.url` vazio, reservando o lugar com
  "Link de loja em breve"; e modelo sem declaração de fabricante não ganha bloco
  de compra — a página diz por quê. **Verificação: `teste-r1.php` APROVADO em 90
  medições** (eram 70; a seção 13 é nova e só sobre este item), mais
  `teste-casca.php` (64) e `validar-banco.py`. **NO AR:** Sync acionado às
  17h25Z, `/status` em **revisão 10**, página em 200, **48 links externos e zero
  sem `nofollow`**, bloco de compra antes da primeira fonte, zero `&#038;` dentro
  dos `<script>`. **14 peças recomendadas na tela, 14 esperando link de
  afiliado** — trabalho da Sentinela estratégica, não da Fundação.

- 10/09/2026 — **Blocos 4 e 4e: A FERRAMENTA R1 EXISTE, e é a primeira ferramenta
  desta ilha.** `snippets/robometria-r1.php` v1.0.0, mais `ferramentas/gerar-r1.py`,
  `ferramentas/teste-r1.php`, `dados/r1-respostas.json` (o combustível, o primeiro
  item de **dados** desta ilha com `publicar: true`) e `dados/r1-referencia.json`
  (o gabarito, `publicar: false`). Manifest na **revisão 8**, e **NO AR**: o Sync
  foi acionado por esta execução e o `/status` respondeu a revisão aplicada. A
  página é `https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/`.
  **Verificação: `teste-r1.php` APROVADO em 70 medições**, entre elas a comparação
  das **188 frases** publicadas contra a implementação de referência; mais `php -l`,
  `teste-casca.php` (64) e `validar-banco.py`, e a medição num Chromium de verdade
  (rolagem horizontal 0 px a 360, 390, 782 e 1200; botão do menu aparece até 782 e
  some a 1200; `aria-expanded` false → true → false no clique e no Escape; barra
  fixa do celular só enquanto o resultado está fora da tela; console limpo).
  **No ar:** a página devolve 200, serve as 45 linhas da tabela, a resposta-âncora,
  o formulário GET, JSON-LD WebApplication + FAQPage e **zero `&#038;` dentro dos
  blocos `<script>`**; uma consulta real sai com `noindex,follow` e canônica.

- 10/09/2026 — **Despacho da Sentinela, item 1: os sitemaps voltaram a 200.**
  Serviam XML válido com status 404, porque esta ilha não tem post nenhum e o
  `handle_404()` do WordPress carimbava a resposta antes de o XML sair. Consertado
  na casca (v1.0.1, manifest revisão 9) pelo filtro `pre_handle_404`, que só age em
  requisição de sitemap. Medido no ar: `wp-sitemap.xml` e
  `wp-sitemap-posts-page-1.xml` em **200**, endereço inexistente ainda em **404**.
  **Falta a metade humana:** reenviar o sitemap no Search Console.

- 10/09/2026 — **Bloco 3b: a CASCA DO SITE existe.** `snippets/robometria-casca.php`
  v1.0.0 (`publicar: true`, `ativo: true`), o primeiro item desta ilha que vai ao ar.
  Identidade aplicada sobre o tema: paleta grafite/varredura/piso, Archivo + IBM Plex
  Sans + IBM Plex Mono com `tabular-nums` em todo número, logotipo em SVG do **encaixe**
  (anel aberto + peça de lingueta), wordmark ROBO 700 colado a METRIA 400, menu sanfona
  com `aria-expanded`/`aria-controls` e os três links sempre no HTML servido, favicon
  próprio no lugar do ícone do WordPress, JSON-LD Organization + WebSite em toda página,
  e as cinco páginas (início, ferramentas, metodologia, sobre e divulgação de afiliados)
  com o conteúdo em shortcode do próprio snippet. Vieram junto três ferramentas de
  bancada: `gerar-favicon.php`, `render-para-teste.php` e `teste-casca.php`. Manifest na
  revisão 7. **Verificação: `teste-casca.php` APROVADO em 59 medições**, mais `php -l` e
  a conferência do menu num Chromium de verdade (botão aparece a 390 px, abre, o
  `aria-expanded` vira `true`, Escape fecha, zero rolagem horizontal a 360 px).
  **NO AR desde 10/09/2026, 14h11Z** — revisão 7 confirmada no `/status`.

- 10/09/2026 — **Bloco 3c, terceira leva: a entrada da R1 foi varrida pela primeira
  vez, e a varredura reordenou a fila.** `ferramentas/cobertura-r1.py` (implementação
  de referência da R1 + varredura), `dados/cobertura-r1.json` (a medição) e
  `dados/tabela-exemplos-r1.md` (45 linhas, geradas). Manifest na revisão 6. **Não
  houve coleta nesta execução**: a busca web devolveu "unavailable" e o egresso HTTP
  devolveu `EGRESS_BLOCKED` em `wap.ind.br`, `positivocasainteligente.com.br` e
  `roborock.com`. Nenhum dado técnico novo entrou no banco, e nenhum número desta leva
  vem de fora do repositório.

- 09/09/2026 — pasta da ilha criada dentro da reorganização do Arquipélago em
  uma única Fundação que escolhe a ilha de cada execução (seção 1 do contrato).
- 09/09/2026 — **Bloco 1**: `dados/corpus-buscas.md`, levantamento de buscas
  paramétricas separado nos eixos compatibilidade (filtro, escova lateral, mop,
  bateria) e dimensionamento (Pa, m², autonomia, pelo de pet), com procedência
  marcada consulta a consulta. Sem ferramenta de volume de busca nessa coleta —
  o arquivo diz isso em vez de inventar número.
- 09/09/2026 — **Bloco 2**: `dados/especificacao-calculadoras.md` e
  `dados/constantes.json`. As duas ferramentas âncora especificadas ponta a
  ponta — **R1**, localizador de peça compatível por modelo, e **R2**,
  dimensionador de sucção e autonomia — com entrada, saída, elegibilidade,
  tabela de exemplos pré-renderizada, JSON-LD e classificação de SERP da
  consulta-alvo. 21 constantes, cada uma com classe de fonte, URL, canal de
  coleta e data.
- 09/09/2026 — **Bloco 3c, segunda leva: a R2 deixou de sair vazia.**
  `pa_declarado` passou de **2 para 11 modelos publicáveis**, em 3 marcas, cobrindo de
  **1.400 a 10.000 Pa** numa escala contínua. 33 modelos (eram 24) e 5 marcas (eram 4),
  com a WAP entrando no banco. Esquema na versão 3, manifest na revisão 5,
  `validar-banco.py` APROVADO com três invariantes novas mais a conferência das contagens
  do cabeçalho — e todas foram testadas quebrando o banco de propósito numa cópia.

- 09/09/2026 — **Bloco 3c entregue: o banco saiu do modelo e virou cobertura.**
  24 modelos (eram 17), 18 peças (eram 8) e **33 pares peça × modelo declarados**
  (eram 10). Esquema na versão 2, manifest na revisão 4, `validar-banco.py`
  APROVADO com cinco invariantes novas — e as cinco foram testadas quebrando o
  banco de propósito numa cópia, para provar que reprovam.
- 09/09/2026 — **Bloco 3 entregue: o modelo do banco existe e é verificável.**
  `dados/esquema-banco.json` (contrato das entidades MARCA, MODELO_ROBO, PEÇA e
  COTAÇÃO), `dados/marcas.json` (4), `dados/modelos-robo.json` (17) e
  `dados/pecas.json` (8 peças, **10 pares peça × modelo, todos declarados pelo
  fabricante e nenhum inferido**), mais `ferramentas/validar-banco.py`, que roda
  sem rede e reprova o banco quando alguma invariante do esquema é violada.
  Manifest na revisão 3.

### O que a TERCEIRA LEVA do 3c descobriu — e é o achado mais caro da ilha até aqui

1. **A R1, que é o produto desta ilha, sai VAZIA em 12 dos 28 modelos publicáveis.**
   Ninguém sabia porque ninguém tinha varrido: o cabeçalho anunciava "33 pares
   declarados", e par novo num modelo que já respondia não tira modelo nenhum do vazio.
   Das 168 células (modelo × tipo consultável), **116 não têm o que responder**.
   Contar item e varrer faixa são coisas diferentes, e a seção 14.3 do contrato pede a
   segunda.
2. **AS DUAS FERRAMENTAS DA ILHA TÊM COBERTURA QUASE DISJUNTA — só 3 dos 28 modelos
   são atendidos pelas duas.** A R2 atende 8 modelos em que a R1 é vazia (Xiaomi, WAP,
   e o PRA500); a R1 atende 12 em que a R2 é vazia (Electrolux e Multi). A causa é a
   mesma nos dois sentidos, e é de mercado: **Electrolux e Multi publicam peça com
   compatibilidade declarada e não publicam Pa; Xiaomi e WAP publicam Pa e não publicam
   peça com código.**
3. **Consequência que custa dinheiro: o funil está partido na emenda.** A ilha ganha a
   visita pela R2 ("quantos Pa para pelo de cachorro"), que na faixa alta só consegue
   recomendar Xiaomi. Quem compra volta meses depois procurando o filtro daquele robô —
   a consulta de maior intenção de compra do nicho, e a razão de a R1 existir — e recebe
   "não localizamos declaração do fabricante". As duas ferramentas não se entregam a
   visita uma para a outra, e nenhuma das duas medições isoladas mostrava isso.
4. **Por isso "peças da Xiaomi e da WAP com código" saiu do ÚLTIMO para o PRIMEIRO
   lugar** entre os alvos de coleta. Dois motivos medidos: é o único lado da emenda que
   dá para colher (o lado simétrico, Pa da Electrolux e da Multi, já foi medido como
   inexistente no mercado brasileiro), e são exatamente os modelos que a R2 já
   recomenda — o retorno chega na visita que a ilha já sabe atrair.
5. **A implementação de referência pegou dois defeitos de frase antes de eles irem para
   a tela.** Rodar as regras da especificação contra o banco de verdade produziu "ele
   vem dentro do **sem codigo publicado**" (quando o fabricante não publica código de
   peça) e "não vende **escova lateral avulso**" (sem concordância de gênero). As duas
   teriam nascido dentro do PHP do Bloco 4, num snippet que só dá para testar com o site
   no ar. **Escrever a regra onde ela pode ser conferida é mais barato do que escrevê-la
   onde ela não pode.**
6. **Decisão de interface obrigada pela medição:** o tipo `reservatório` tem **zero**
   peças no banco inteiro e sai do seletor da R1. Oferecer uma escolha que sempre
   devolve recusa contraria a promessa antes do formulário (seção 6 do contrato). O
   seletor passa a ser gerado da varredura, não digitado — e o tipo volta no dia em que
   a primeira peça dele entrar.
7. **A consulta-alvo escrita na especificação responde com recusa.** O PRA500 é
   literalmente o exemplo da seção 1.1, e a R1 sai vazia nele: as três peças da Positivo
   no banco declaram PRA800 e PRA2000 e não o citam. Pelo conjunto mais estreito, a
   recusa é a resposta **certa** — mas isso significa que **a página-âncora da R1 não
   pode ser a do PRA500** enquanto não houver peça declarada, sob pena de a ilha estrear
   a ferramenta com um "não sabemos".

### O que a SEGUNDA LEVA do 3c descobriu, e muda a estratégia inteira

1. **A lacuna de Pa está fechada, e a que sobrou é de OUTRO tipo.** A varredura da faixa
   de entrada da R2 de ponta a ponta (seção 14.3), gravada em `cobertura_de_faixa_r2`,
   mostrou que 5 das 6 faixas passam no portão de 3 itens. Sobraram duas coisas: acima de
   **6.000 Pa** só há 2 elegíveis, e — o achado que só aparece olhando a varredura inteira
   — **toda faixa acima de 3.000 Pa é 100% Xiaomi**, faixa de pet inclusive. Contar
   elegíveis diz que está resolvido; olhar a composição diz que não. Numa ilha que se
   vende como comparador **cross-marca**, a faixa que mais vende não pode ser catálogo de
   uma marca só.
2. **Quem declara sucção alta no Brasil é essencialmente a Xiaomi.** Electrolux e Multi
   não publicam Pa em canal nenhum (as duas declaram *níveis*), e a WAP só publica na
   parte barata da linha: 1.400 Pa no W400, e nada no topo W1000, que declara "três modos
   de sucção". Isso é fato de mercado medido, não impressão — e é conteúdo publicável na
   página de metodologia, porque nenhum comparador diz isso.
3. **A lacuna de m² não é de esforço, é de mercado — e isso vira conteúdo.** Xiaomi, WAP,
   Multi e Positivo foram varridas modelo a modelo e **nenhuma** declara área coberta em
   m². Só a Electrolux declara. Não adianta coletar mais: o número não está publicado. A
   `taxa-cobertura-m2-por-min` segue proibida em fórmula, e a recusa da R2 deixa de ser
   uma pendência envergonhada e passa a ser a resposta: quando um site promete "atende até
   120 m²" para um robô cujo fabricante só declarou minutos, esse número foi inventado
   por alguém.
4. **Divergência de especificação não é só de peça — e o PRA500 provou.** O mesmo canal do
   fabricante declara **1600 Pa na ficha e 2000 Pa no texto de venda da MESMA página**.
   Não há nível mais alto para desempatar, e a média (1800) é a única saída proibida.
   Valeu 1600, porque o erro caro é o do lado alto: publicar 2000 faz alguém comprar um
   robô fraco demais por recomendação nossa. Isso forçou `divergencias[]` e `resolucao` a
   existirem também em `MODELO_ROBO`, na versão 3 do esquema.
5. **Faixa e tolerância declaradas resolvem para o lado caro, nunca para o meio.** O
   fabricante quase nunca dá número: dá "de 5 a 6 horas" ou "130 minutos ±10%". A versão 3
   escreveu a regra por campo — Pa e autonomia para **baixo**, tempo de recarga para
   **cima** — e `declarado_como` guarda a faixa inteira, para a página citar a faixa e não
   o número escolhido.
6. **A WAP é a melhor chance de NÍVEL 2 que a ilha já teve.** É a única marca que publica
   um manual em PDF por modelo, em endereço próprio e estável, com revisão e data no nome
   do arquivo. Hoje `EGRESS_BLOCKED`; no dia em que abrir, sobe o banco inteiro da marca
   de uma vez. A ilha ainda não tem **nenhuma** fonte de nível 2.

### O que o Bloco 3c descobriu, e muda a estratégia de coleta

1. **A Electrolux não publica sucção em Pa. Em canal nenhum.** Loja oficial,
   página de conteúdo, portal de cuidados e canal de parceiros: todos declaram
   **níveis** de sucção (mínimo, médio, máximo), nunca pascal. Veículos
   editoriais citam "4.000 Pa" para a linha, mas pela escada de fontes editorial
   **nunca** sustenta especificação de aparelho — então o número ficou de fora,
   de propósito. **Consequência prática:** `pa_declarado` continua em 2 de 19
   modelos publicáveis, e insistir na Electrolux não vai resolver. O campo tem
   que vir de Xiaomi, Multi, WAP e Positivo. Isso corrige a suposição do bloco
   anterior, que tratava a Electrolux como fonte de maior rendimento.
2. **A Electrolux não vende filtro de robô avulso — vende o Kit Performance.**
   Quem procura "filtro do ERB10" compra o **KPCEL01**. Foi isso que obrigou o
   esquema a ganhar o tipo de peça `kit` com `composicao[]`: sem ele a R1 não
   responderia a própria consulta-alvo. E é o KPCEL01 que finalmente dá dono à
   vida útil de 6 meses do manual, que desde o Bloco 3 era um número sem peça.
3. **A dispersão da cobertura virou conteúdo.** O banco tem agora dois pares
   (minutos, m²) declarados: 162 m² em até 2h no ERB44 (1,35 m²/min) e 166 m² em
   até 1h40 na família ERB60/61/62/80 (1,66 m²/min). São **23% de diferença
   dentro da mesma marca** — e é o melhor argumento de que taxa geral não existe.
   A constante `taxa-cobertura-m2-por-min` **continua proibida em fórmula
   publicada**, agora com dois números do próprio fabricante sustentando o
   porquê. Faltam pares de **marcas diferentes**: são 2 declarações de 1 marca, e
   o critério pede 5 de marcas diferentes.
4. **"Compatibilidade não se herda" apareceu no catálogo do próprio fabricante.**
   O ERB80 está na lista da escova rotativa central e **não** está na do filtro
   HEPA com espuma nem na do Kit Performance do ERB60/61/62. A R1 não pode
   completar lista por analogia, e agora a ilha tem o exemplo para mostrar.
5. **Armadilha da R1, escrita antes de custar caro:** o **PRA500** é literalmente
   a consulta-alvo da especificação, e as três peças novas da Positivo declaram
   **PRA800 e PRA2000**, sem citá-lo. Pelo conjunto mais estreito, a resposta
   certa para o PRA500 é "não encontramos peça declarada". Dizer que serve seria
   exatamente o erro caro desta ilha.

### As três decisões que este bloco fixa

1. **`variante_de_hardware` é campo de primeira classe.** O fabricante vende
   duas baterias diferentes para o **mesmo** código de modelo: a PR10127
   ("Versão A") e a PR8116 ("Mars HO041 versão B"). Saber que o robô é um HO041
   **não basta** para acertar a peça. Consequência escrita na especificação da
   R1: quando o modelo tem mais de uma variante conhecida, a ferramenta mostra
   as duas e explica como a pessoa descobre qual é a dela — devolver uma só
   seria adivinhar, que é o defeito que esta ilha existe para não cometer.
2. **Todo número é `{valor, fonte, declarado_como}`.** Número solto não entra:
   sem a transcrição do texto do fabricante, a página parafraseia em vez de
   citar, e a frase citável com procedência é justamente o que a seção 5 do
   contrato exige. Onde o fabricante não declara, o valor é `null` **com
   motivo** — e o motivo vai para a tela com essas palavras.
3. **Categoria é portão, e o verificador o aplica.** Registro com
   `categoria != robo` não pode ser `publicavel`, e o `validar-banco.py` falha
   se alguém tentar.

## O que este bloco descobriu, e vale dinheiro

- **Pendência do Bloco 2 resolvida:** HO011 e HO012 são aspirador de pó
  **vertical e de mão 2 em 1** (127 V/1000 W e 220 V/700 W, pelos títulos das
  páginas do próprio fabricante), **não** robôs. Logo o filtro PR684 não é peça
  de robô e ficou excluído, com a fonte, para nenhuma execução futura recolhê-lo
  de novo.
- **Quatro modelos novos com categoria confirmada pelo fabricante**: HO407
  (Duster), OB010 (ObaDuster), HO243 (Hydra / Acqua Solution, 90 min declarados)
  e HO411 (Midnight, com lâmina oficial em PDF esperando o egresso abrir).
- **Duas peças novas**: o pano PR10342, que fecha o cluster A3 do corpus (mop),
  que até agora não tinha nenhum item; e a bateria PR8116.
- **Duas divergências resolvidas pelo conjunto mais estreito**, com as duas
  declarações publicadas: o filtro PR10205 (dois canais do fabricante discordam
  sobre o OB010) e a bateria PR8116, cuja divergência está **dentro de uma única
  página** — o título promete "Mars, Moon e Duster" e o endereço da mesma página
  diz "Mars HO041 versão B".
- **O PRA800 tem 2.800 Pa** e portanto fica **abaixo** dos dois limiares que as
  fontes editoriais recomendam para casa com pet (3.000 Pa no Mundo Conectado,
  4.000 Pa no Canaltech). É um caso limpo da regra de elegibilidade da seção 7:
  ele não pode encabeçar a lista de uma consulta com pet.

## O que este bloco deliberadamente NÃO fez

- **Não converteu W em Pa.** O HO041 declara 30 W de potência e nenhum Pa.
  Potência não é sucção e não existe conversão: `pa_declarado` ficou null com
  esse motivo escrito.
- **Não emprestou vida útil de um fabricante para a peça de outro.** O único
  número de fabricante que a ilha tem é o do manual da Electrolux (6 meses para
  o filtro HEPA do ERB10/ERB11/ERB20) e ele vale para **aqueles** modelos. As
  peças da Multi ficaram com `vida_util_declarada` null e motivo.
- **Não coletou nenhuma imagem.** O campo `imagem{}` existe em todo registro,
  com a forma completa e `url` null — o egresso barra os domínios de fabricante
  e de varejo, então não há como baixar nem medir o arquivo. Pela seção 6 do
  contrato, isso **não** elimina o registro da vitrine: ele aparece com espaço
  reservado neutro e o nome em destaque.
- **Não tirou a taxa de cobertura m²/min de `pendente`** — e o Bloco 3c também
  não tirou, de propósito. Os pares declarados passaram de 1 para 2, mas os dois
  são da **mesma marca** e discordam em 23% entre si. O critério pede 5 pares de
  marcas **diferentes**, e continua valendo: publicar a média seria a única saída
  proibida pela seção 10 do contrato.

## O que está travando

Nada que pare a fila. **`bloqueada_por` continua `null`**, e continua sendo erro
marcar bloqueio por causa de infraestrutura.

Os blocos 1, 2, 3, 3b, 4 e 4e estão entregues **e no ar**: o `/status` responde a
revisão do manifest, a casca serve as cinco páginas e a ferramenta R1 responde em
`https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/`.

**Uma metade humana em aberto, e ela não é bloqueio da fila:** o item 1 do
despacho da Sentinela de 10/09 pede, além do conserto do status 404 (feito nesta
execução), **reenviar o sitemap no Search Console** para ele sair de "Não foi
possível buscar". Isso é propriedade da conta do Raphael e exige o navegador dele
ou uma credencial de conta de serviço que este ambiente ainda não tem. Todo o
resto do item foi cumprido e medido.

**O trabalho desbloqueado, em ordem:**

1. **Bloco 5 — o artigo-âncora pareado com a R1.** A fila manda o artigo nascer
   junto da ferramenta, e ele é o que dá à R1 uma segunda listagem e as irmãs
   que a regra da malha exige. Não depende de rede nem de coleta.
2. **Bloco 3c, alvo (a): peça com código da Xiaomi e da WAP** — os 8 modelos que
   a R2 já recomenda e em que a R1 sai vazia, e o único lado coletável da emenda
   entre as duas ferramentas. **Depende de a rede alcançar o fabricante**, e
   nesta execução ela não alcançou: `www.wap.ind.br`,
   `mais.conteudo.wap.ind.br`, `www.mi.com` e `www.xiaomi.com.br` não
   responderam. Isso não é `bloqueada_por` — é uma execução em que a coleta não
   estava disponível.
3. **Bloco 3c, alvo (b):** faixa descoberta acima de 6.000 Pa e a concentração
   100% Xiaomi acima de 3.000 Pa, medidas em `cobertura_de_faixa_r2`. Rende numa
   ferramenta só, por isso vem depois.

**Nenhuma leva de malha (bloco 5b) antes de o Search Console voltar a buscar o
sitemap.** A rampa da seção 14 é inexecutável sem medição, e publicar página no
escuro é exatamente o que desindexa domínio novo.

### Dois achados desta execução que valem para a próxima

1. **O BANCO ESTÁ EM ASCII, E AGORA ELE APARECE NA TELA.** Enquanto o banco só
   alimentava medição, os acentos faltando em `nome_na_fonte`, `publicador` e
   `o_que_muda` não custavam nada. Com a R1 no ar, esse texto é citado dentro da
   resposta publicada: a tela mostra "Aspirador Robo" e "identificada como
   'Versao A'". O que a ilha escreve sai acentuado; o que ela cita sai como o
   banco tem — e o banco tem errado, porque a transcrição perdeu os acentos da
   fonte. É trabalho de dados, não de snippet, e vale a pena fazer junto da
   próxima leva de coleta, quando esses registros já forem ser tocados.
2. **UMA FONTE DO BANCO ESTÁ NO NÍVEL 2 E A ESCADA DIZ QUE O NÍVEL 2 NÃO
   EXISTE.** `pecas.json/electrolux-kpcel01/f-manual` declara `nivel: 2`, mas a
   escada da página de metodologia define o nível 2 como "manual, lâmina ou
   página oficial **LIDA direto**" e publica "temos hoje: —". Aquele manual foi
   colhido por busca restrita a `manuals.plus`, um terceiro, sem leitura direta.
   Uma das duas afirmações está errada, e **a R1 não publica número de nível de
   fonte** justamente para não levar a contradição para a tela antes de alguém
   decidir. A decisão é de regra, não de digitação: *manual do fabricante
   hospedado por terceiro, colhido por busca, é nível 2 ou não?* Escrever a
   resposta na escada e acertar o banco é bloco de dados para a Fundação.

**NA EXECUÇÃO DAS 11h17Z NÃO DEU PARA COLHER NADA, e isso foi medido, não
suposto.** Em 10/09/2026, 11h17Z, a busca web devolveu `unavailable` em três consultas
seguidas, e o `WebFetch` devolveu `EGRESS_BLOCKED` em `www.wap.ind.br`,
`www.positivocasainteligente.com.br` e `global.roborock.com`. Isso **não** é
`bloqueada_por`: é uma execução em que a coleta não estava disponível, e a
resposta certa foi trabalhar o que não depende de rede — medir o que o banco já
tem — em vez de deixar a execução passar em branco ou, pior, escrever número de
memória. A coleta segue sendo o primeiro item da fila na próxima execução em que
a rede responder.

O manifest tem **dez** itens: os nove de dados e medição continuam com
`publicar: false` porque são pesquisa, e o décimo — a casca — é o **primeiro
`publicar: true` desta ilha**. Enquanto o Sync não rodar, nada disso está no ar, e
a distância entre o repositório (revisão 7) e o site (revisão 6) é exatamente o
buraco que a seção 4 do contrato descreve. Itens esperando link de afiliado:
**44** (28 modelos e 16 peças) — o campo `afiliado.url` já nasce presente e vazio
em todos. **Continua em 44:** nem a leva de medição nem a casca acrescentaram item
ao banco. É trabalho pendente de verdade, não
estatística: pela seção 7 do contrato, quem gera link é a Sentinela estratégica,
no navegador do Raphael, com teto de calendário — o cano enche em paralelo e não
compete com a fila da Fundação.

Uma coleta segue em aberto, e não é bloqueio: o egresso HTTP direto está fechado
(`multilaser.com.br`, `suporte.multilaser.com.br`, `lamina.multilaser.com.br`,
`arquivos.multilaser.com.br`, `mi.com`, `manuals.plus`, `loja.electrolux.com.br`,
`content.electrolux.com.br` e, medido nesta execução, também
`www.mi.com`, `loja.wap.ind.br`, `mais.conteudo.wap.ind.br` e
`static.positivocasainteligente.com.br` devolveram EGRESS_BLOCKED em
09/09/2026), então tudo foi colhido por busca restrita ao domínio, com o canal
declarado campo a campo. A leitura direta das páginas de peça, das lâminas e dos
manuais em PDF é trabalho a fazer, não dependência humana — e os manuais da WAP
são o alvo de maior retorno, porque são a única chance de NÍVEL 2 que a ilha tem
hoje. A ilha inteira está em nível 3 e 4: **nenhuma fonte de nível 2 ainda.**

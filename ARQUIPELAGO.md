# CONTRATO DO ARQUIPÉLAGO

Regras que valem para TODA ilha. Quem executa um bloco lê este arquivo primeiro e depois o `PROMPT.md` da ilha sorteada. Regra nova do Arquipélago se escreve AQUI, uma vez — nunca copiada para dentro dos prompts das ilhas.

Vocabulário: cada site de nicho é uma **ilha**, o conjunto é o **arquipélago**, o portão de publicação é o **desembarque**. Camadas: **BÚSSOLA** (decide o nicho) → **FUNDAÇÃO** (constrói) → **SENTINELA** (cuida da ilha viva).

---

## 1. COMO A FUNDAÇÃO ESCOLHE A ILHA DE CADA EXECUÇÃO

Existe **uma** Fundação para o arquipélago inteiro, não uma por ilha. A cada execução:

1. `git fetch origin main` e trabalhe do estado real do `main`. Confira se existe branch `claude/*` ou PR aberto de execução anterior; se houver, mergeie antes de qualquer coisa.
2. Liste `ilhas/*/ESTADO.md` e leia o cabeçalho YAML de cada um (formato na seção 2).
3. Descarte as ilhas com `estado: pausada`, com `bloqueada_por` preenchido, e as que têm `executando_desde` de menos de 40 minutos atrás (outra execução está com ela).
4. Entre as que sobraram, escolha a de `ultima_execucao` mais antiga (`null` conta como a mais antiga de todas). Empate: menor `prioridade` primeiro (1 é a mais alta). Empate ainda: ordem alfabética.
5. **Reserve a ilha**: escreva `executando_desde` com o horário UTC de agora, commite só esse arquivo e empurre para o `main`. Se o push for recusado, `git fetch` + `rebase` e volte ao passo 2 — outra execução chegou primeiro e você escolhe outra ilha. Nunca force push.
6. Leia `ilhas/<ilha>/PROMPT.md`, `REGISTRO.md` e `ESTADO.md`. Execute **um** bloco.
7. Ao terminar, limpe `executando_desde` (volta a `null`), atualize `ultima_execucao` e `bloco_atual`, escreva a entrada no `REGISTRO.md` e empurre tudo para o `main`.

Se **nenhuma** ilha estiver elegível, não invente trabalho: registre "nada elegível" no relatório e pare. É informação útil, não fracasso.

**Por que assim:** com uma rotina por ilha, 50 ilhas seriam 50 rotinas e 50 prompts para manter. Aqui, ilha nova é uma pasta nova — nenhuma rotina muda. E como a reserva é feita por commit, várias execuções podem rodar ao mesmo tempo sem se atropelar: quem perde a corrida do push simplesmente pega outra ilha.

---

## 2. Cabeçalho de estado — obrigatório no topo de todo `ilhas/<ilha>/ESTADO.md`

```yaml
---
ilha: aquametria
estado: viva              # nascendo | viva | pausada
prioridade: 2             # 1 alta, 2 normal, 3 baixa
ultima_execucao: 2026-09-09T18:00Z
executando_desde: null
bloco_atual: "4c"
ultima_ronda: 2026-09-09T14:36Z   # última vez que a Sentinela olhou esta ilha; null se nunca
bloqueada_por: null       # texto curto quando depende de algo humano; null quando não
---
```

Regras do cabeçalho:
- `bloqueada_por` só existe para dependência **humana ou externa** (domínio não propagou, senha que só o Raphael tem). Falta de dado que você mesmo pode colher NÃO é bloqueio — é trabalho.
- Ao desbloquear, apague o texto e volte para `null` na mesma execução.
- `ultima_execucao` é gravada mesmo quando o bloco falha; senão a mesma ilha é escolhida para sempre.
- Abaixo do cabeçalho, o `ESTADO.md` continua sendo prosa livre: credenciais **não**, estado do projeto **sim**.
- `ultima_ronda` é escrita pela Sentinela, não pela Fundação. É o que faz a verificação ser distribuída por dívida em vez de varrer tudo todo dia (seção 12).

---

## 3. O repositório é o lugar do trabalho

**Tudo que for código ou conteúdo de site nasce como arquivo commitado, nunca direto no WordPress.**

- Cada ilha vive em `ilhas/<ilha>/`: `snippets/`, `conteudo/`, `dados/`, `ferramentas/`, `manifest.json`, `PROMPT.md`, `README.md`, `ESTADO.md`, `REGISTRO.md`.
- Todo arquivo publicável entra no `manifest.json` da ilha: incremente `revisao`, atualize `atualizado_em`, grave o `sha256` do arquivo final commitado.
- **Toque apenas na pasta da ilha que você reservou.** Nunca edite arquivos de outra ilha.
- **O bloco só conta como entregue quando está no `main`.** Depois do push na branch: `git fetch origin main && git rebase origin/main` e `git push origin HEAD:main`. Se recusar: `gh pr create --base main --fill` e `gh pr merge --merge --delete-branch`. Só se nada funcionar, deixe o PR aberto e diga no relatório com o link.
- Push recusado = rebase e tentar de novo, até 3 vezes. **NUNCA force push.**
- `REGISTRO.md` é append-only: o que foi entregue e qual é o próximo passo.

---

## 4. O SITE FICA PARA TRÁS EM SILÊNCIO

Descoberto na Aquametria em 09/09/2026: o repositório estava na revisão 17 e o site na 11. Três blocos estavam commitados e **não estavam no ar**. Ninguém percebeu porque a verificação olhava o repositório, não o site.

Causa: o desenho é **PULL** — o site busca o `manifest.json` no raw.githubusercontent e aplica. Só que o WP-Cron do WordPress dispara quando alguém **visita** o site, e site novo sem tráfego não tem visita.

Portanto, ao terminar todo bloco que mexeu em conteúdo publicável: acione o Sync da ilha, espere o cache, e **confirme no endpoint `/status` da ilha que a revisão aplicada é igual à do manifest**. Se não bater, diga isso no relatório em vez de dar o bloco por entregue.

**A NUVEM ALCANÇA O SITE desde 10/09/2026 — a Fundação aciona o Sync ela mesma.** Os ambientes das rotinas ("Arquipélago — Fundação" e "Arquipélago — Mãos no repositório", em claude.ai/code → seletor de ambiente → engrenagem) têm rede Personalizado com os domínios das ilhas, `*.googleapis.com` e `github.com` liberados, mantendo a lista padrão de pacotes. Medido pelas próprias rotinas em `ferramentas/teste-rede-rotinas.txt`: sites 200, Search Console API 401 (chega; só falta credencial). Portanto o Sync deixou de ser tarefa da Sentinela no navegador: **ao terminar bloco publicável, a Fundação roda `curl -s "<URL do Sync da ilha>"` (a URL com `&forcar=1` está no `PROMPT.md` da ilha), lê o JSON de resposta, e confirma com `curl -s <endpoint /status>` que `revisao` é igual à do manifest.** Se a rede falhar (403 CONNECT), escreva isso no relatório e deixe o item aberto — mas não presuma bloqueio sem testar. Primeira execução real: Aquametria revisão 33 (18 itens) e Robometria revisão 7 (casca), ambas por curl, em 10/09/2026.

**CACHE DUPLO:** o `raw.githubusercontent` guarda ~5 min e o WebFetch guarda 15 min por URL. Sempre acrescente `?v=<hora e minuto>` na URL ao verificar, ou você conclui erradamente que nada mudou.

---

## 5. Visibilidade em IA — regra de primeira classe

Decisão do Raphael, 08/09/2026: ser recomendado pelas IAs vale tanto quanto ranquear no Google.

**O defeito que a Aquametria descobriu tarde:** calculadora que calcula em JavaScript mostra a um modelo de linguagem um **formulário vazio**, nunca um número. Toda ferramenta nasce resolvendo isso:

1. **Tabela de exemplos pré-renderizada no HTML** — casos já resolvidos, servidos no HTML, cobrindo a faixa real de uso.
2. **Resposta antes da explicação** — o número e o critério nos primeiros parágrafos, em frase autossuficiente que sobrevive a ser citada fora de contexto.
3. **JSON-LD** em toda página: `WebApplication` na ferramenta, `Product` nas fichas, `Dataset` no banco, `FAQPage` onde couber, `Organization` com `sameAs` na marca.
4. **Procedência na própria frase** — "segundo o manual do fabricante X, o modelo Y atende Z (verificado em DD/MM/AAAA)".
5. **`robots.txt` não bloqueia crawler de IA** (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).
6. **Entidade clara**: página Sobre com quem publica e qual o método.

---

## 6. Padrão de interface da ilha

- **Menu hambúrguer no celular** é padrão fixo do Arquipélago. Sem custo de SEO se for feito certo: os links existem no HTML servido, são `<a href>` de verdade dentro de `<nav>`, o botão é `<button>` com `aria-expanded` e `aria-controls`, e o teclado funciona. Link escondido por CSS continua sendo rastreado; a preocupação com conteúdo oculto vale para conteúdo, não para navegação.
- **Favicon próprio desde o dia 1.** `remove_action('wp_head','wp_site_icon')` e imprimir no `wp_head` um `<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,...">` com o símbolo da ilha embutido, mais `apple-touch-icon`. **Ícone padrão do WordPress na aba = bloco reprovado.**
- **Vitrine de produto dentro do resultado**, desde a primeira ferramenta: carrossel de cartões com foto, marca, modelo, **a especificação que fez o produto entrar**, faixa de preço com data da coleta e botão de loja. `scroll-snap` em CSS puro, sem biblioteca; cartões são links de verdade, não `div` com `onclick`; `loading="lazy"`, `width`/`height` declarados, `alt` descritivo.
- **Promessa antes do formulário**: uma linha no topo dizendo o que a pessoa recebe. No celular, barra fixa no rodapé enquanto o resultado está fora da tela, e rolagem automática até o resultado ao calcular.
- **Campo de imagem no modelo de produto**: `imagem: {url, largura, altura, fonte, coletado_em, alt}`. Produto **sem** imagem não some do resultado — aparece com espaço reservado neutro. Perder a recomendação técnica certa por falta de foto é trocar o certo pelo bonito.
- Sem gradiente e sem sombra colorida. As ilhas separam com linha de 1px.

---

## 7. Monetização — e o que ela nunca pode fazer

- O bloco de produto nasce **dentro** da resposta, como consequência do cálculo, com a especificação que fez o produto entrar e o link. Três a cinco produtos.
- **REGRA DE ELEGIBILIDADE** (cicatriz da Aquametria, 09/09/2026): produto entra na lista de recomendados só se passar em **TODAS** as condições declaradas pelo fabricante que a ferramenta conhece, não apenas na principal. Quem passa na principal e falha em outra vai para seção separada, abaixo, rotulada — nunca misturado, nunca em primeiro lugar. **Recomendar em primeiro lugar um produto que a própria página diz não servir é defeito GRAVE.**
- **ORDEM DA LISTA:** (1) elegibilidade técnica completa; (2) adequação técnica entre os elegíveis; (3) só como **desempate** entre itens equivalentes, quem tem link de loja aparece antes. Isso não é ordenar por comissão: nunca comparar taxa, nunca promover produto pior porque paga mais.
- Sem item que atenda, o bloco não lista — mas **diga por quê** ao visitante. Silêncio parece defeito.
- Links de afiliado: `rel="sponsored"` + `target="_blank" rel="noopener"`; aviso visível de comissão na página; preço nunca cravado como atual (ou sem preço, ou com data da coleta). O link de afiliado nunca substitui a URL de origem do dado técnico.
- **PROCEDÊNCIA NUNCA É A ÚNICA PORTA DE COMPRA (cicatriz da Robometria, 10/09/2026).** A ferramenta de compatibilidade publicou 45 pares peça × modelo com a coluna "Como sabemos" apontando para a loja oficial do fabricante — e sem nenhum link de afiliado na página. Resultado: o único clique de compra levava para a Electrolux, onde a ilha não ganha nada. A procedência fica (é o que dá credibilidade ao Google e às IAs), mas com três regras: (1) **o bloco de compra com link de afiliado vem ANTES da prova de procedência**, na mesma resposta; (2) o link de procedência é discreto — texto "fonte", `rel="nofollow noopener"`, nunca um botão — porque ele existe para ser conferido, não para ser clicado; (3) **ferramenta que recomenda peça ou produto não vai ao ar sem o bloco de afiliado junto**, mesmo com `afiliado.url` ainda vazio: a página reserva o lugar, mostra "link de loja em breve" e a ilha reporta quantos itens esperam link. A Robometria corrige isto no próximo bloco publicável (ver despacho no PROMPT.md dela).
- **PROIBIDO em toda ilha:** contagem regressiva, escassez inventada, selo de "mais vendido", avaliação que a ilha não mediu. A confiança é o único ativo que separa o Arquipélago das fazendas de conteúdo.
- **DOIS PROGRAMAS DE AFILIADO, uma regra só de ordem.** Desde 09/09/2026 o Arquipélago tem **Shopee Afiliados** e **Mercado Livre Afiliados** (perfil RMNATAL, aberto pelo Raphael; painel em `mercadolivre.com.br/afiliados/hub`). O Mercado Livre existe porque a Shopee não vende as marcas de loja especializada (na Aquametria: Eheim, JBL, Chihiros, Atman canister) — um marketplace só cobre só a faixa de marcas que ele vende, e isso vale para toda ilha. **A ordem da lista continua sendo a da regra acima — elegibilidade, adequação, e loja só como desempate.** Programa nunca é critério de ordem; se dois programas têm o mesmo produto, escolha o de link mais estável, nunca o de comissão maior.
- **Rastreamento por programa.** Shopee: `Sub_id 1` = nome da ilha, `Sub_id 2` = código da ferramenta de origem. Mercado Livre: **etiqueta** (o painel chama de "etiqueta"; cria-se em "Administrar etiquetas" e escolhe-se no "Gerador de links") no formato `<ilha>-<ferramenta>`, por exemplo `aquametria-C3`. Uma etiqueta por par ilha × ferramenta; nunca reaproveite etiqueta entre ilhas. O campo do banco é o mesmo `afiliado.url`, com `afiliado.programa: shopee | mercadolivre` ao lado.
- **Autocompra é a única regra de punição conhecida** nos dois programas: ninguém da casa compra pelo próprio link, nunca. A Amazon Associados fica **fora** até haver tráfego, porque o relógio das 3 vendas em 180 dias começa no cadastro.
- **O CANO DE LINKS DE AFILIADO ENCHE EM PARALELO, SEMPRE — não espere o tráfego chegar.** A geração de link é feita pela Sentinela estratégica, no navegador do Raphael, e tem teto de calendário (algumas dezenas por semana, no máximo). Isso NÃO consome execução da Fundação: são recursos diferentes, então nunca competem por fila. Um produto que entra no banco hoje sem link só vira receita semanas depois, quando alguém finalmente gerar o link — e quando o tráfego chegar, o catálogo precisa estar pronto, não sendo montado às pressas. Portanto: produto novo entra no banco com o campo `afiliado.url` presente e vazio, a ilha reporta em todo bloco **quantos itens estão esperando link**, e esse número é trabalho pendente de verdade, não estatística.
- **NUNCA crie conta** em plataforma nenhuma, nunca compre nada, nunca toque em meio de pagamento, nunca altere configuração de conta do Raphael.

---

## 8. Verificação antes de marcar `publicar: true`

- `php -l` de verdade. Toda função de nível superior dentro de `if ( ! function_exists( 'nome' ) ) { ... }`.
- **JS e CSS NUNCA vão dentro do que o shortcode retorna** — vão no `wp_footer`. O WordPress roda os filtros do `the_content` sobre o retorno e converte o E-comercial duplo em entidade HTML, matando o script inteiro. Foi o defeito que derrubou 5 calculadoras da Aquametria em 08/09/2026.
- **Ao corrigir um snippet, parta SEMPRE do código-fonte do repositório, nunca do HTML servido.**
- Depois de publicar, **busque a URL no ar** e confira com número medido: (1) HTTP 200; (2) **zero entidades `&#038;` DENTRO de `<script>`** — extraia só os blocos `<script>` e conte ali; **contar na página inteira é teste ERRADO**, a casca do tema tem dezenas de ocorrências legítimas, e `&amp;` `&lt;` `&gt;` `&quot;` aparecem uma vez cada dentro do script por causa da função `esc()` da própria calculadora; (3) o corpo começa pelo texto e não por metadado YAML; (4) o script vem do rodapé e a tabela de exemplos aparece no HTML servido; (5) a revisão aplicada bate com a do manifest.
- Se algo falhar, diga **"não concluí"** em vez de marcar sucesso. **"Aplicado com sucesso" no log do Sync não é evidência de nada.**
- **Antes de escrever qualquer snippet PHP, releia a fase 4b do playbook** (`/areas/playbook-nascimento-projeto.md`): nunca confie na ausência de erro; evite `$_SERVER` literal (use `add_query_arg( array() )`, porque o ModSecurity mata a gravação em silêncio); snippet começa com `/**`; texto na tela sai acentuado; nome de snippet descritivo, nunca numerado.

---

## 9. Malha de páginas — limitada por dado, não por calendário

- **ORDEM DAS LEVAS — por intenção de compra, não por facilidade de gerar página.** Tráfego e tráfego não são a mesma coisa. "Quantos litros para 10 neons" traz um curioso; "qual aquecedor para 100 L em 220 V" traz alguém com o cartão na mão. Os dois indexam, os dois contam como tráfego orgânico, mas um está a um clique do dinheiro e o outro está a meses. Como a malha sai em levas pequenas por causa da rampa, **a ordem das levas decide qual tráfego chega primeiro** — então a primeira leva de cada camada é sempre a dos clusters cuja resposta termina num produto do banco. Isso não afrouxa o portão nem a rampa: só escolhe, entre as páginas que já passariam, quais nascem antes.
- **Portão inegociável:** pelo menos 3 itens de banco reais **e** um número calculado próprio por página. Cauda longa vazia em domínio novo causa desindexação em bloco.
- **Rampa guiada por indexação:** primeira leva de 5 a 10 páginas; se indexou, dobre; se ficou em "descoberta e não indexada", **não** aumente.
- **Regra da malha:** toda página entra em pelo menos 2 listagens e aponta para 3 irmãs; link de mão dupla; nenhuma página órfã.

---

## 10. Regras que valem sempre

- **O repositório é a fonte da verdade.** A nuvem não alcança os sites por HTTP direto; o desenho é PULL. Para checar, WebFetch (GET), nunca curl.
- **Desembarque automático**: ferramentas, páginas-âncora, artigos, páginas de entidade e snippets vão ao ar sem consulta. O portão humano fica só para publicação programática em escala.
- **Nunca invente dado técnico.** Toda constante e toda especificação citam a fonte do fabricante e levam data. Constante com status `pendente` é proibida dentro de fórmula publicada.
- **QUANDO AS FONTES DIVERGEM, QUEM DECIDE A DIREÇÃO É A ASSIMETRIA DE CUSTO — nunca a média, nunca o gosto de quem grava.** Duas fontes boas discordando é normal e acontece toda semana; a média é a única saída proibida, porque esconde exatamente o desacordo que faz a página valer. A ilha publica as duas declarações com as duas datas e resolve para o lado em que **errar dói menos**. É por isso que as duas ilhas resolvem para lados opostos, e as duas estão certas: no banco de espécies da Aquametria vale o **MAIOR** (errar para cima dá ao peixe mais espaço do que precisa); na compatibilidade de peça da Robometria vale o conjunto **MAIS ESTREITO** (errar para o lado largo faz alguém comprar peça que não encaixa). Antes de resolver qualquer divergência, escreva qual é o erro caro — a direção sai sozinha depois disso.
- **Um bloco por execução.** Você roda de novo em poucas horas. Bloco bem-feito e registrado vale mais que três pela metade.
- **A identidade visual da ilha é parte do nascimento, não do acabamento** — paleta, tipografia e símbolo entram no `PROMPT.md` da ilha antes do primeiro bloco de casca. O símbolo vem do **gesto técnico** do nicho, nunca do objeto desenhado.
- **ILHA NÃO LINKA ILHA.** Despacho da Sentinela de 09/09/2026, agora regra do arquipélago: não existe link de rodapé, de menu, de "nossos outros sites" nem de artigo entre duas ilhas de nichos diferentes. Aquametria e Robometria são o primeiro par, e a razão vale para todos os pares futuros: **o público não se sobrepõe**. Quem calcula a vazão do filtro do aquário não está comprando peça de robô aspirador, então um link entre as duas não ajuda leitor nenhum — e link que não ajuda leitor é exatamente o que o Google aprendeu a descontar, quando não a tratar como rede de sites. O arquipélago é uma economia de fábrica (mesmo repositório, mesma hospedagem, mesma Fundação), **não uma rede de links**, e essa distinção é o que mantém cada ilha valendo pelo próprio mérito. A única alavanca de link do projeto continua sendo o widget instalado em lojas (seção 14.7). Se um dia duas ilhas tiverem público de verdade sobreposto, o link se justifica pelo leitor primeiro — e aí se escreve a exceção aqui, com o nome das duas.
- O Raphael **não aparece** em ilha nenhuma: sem rosto, sem vídeo, sem fórum, sem tráfego pago, sem link pago. A autoridade vem de metodologia, procedência e do widget instalado em lojas.
- Não faça perguntas: você roda sozinho, sem ninguém acompanhando. Só sinalize ao Raphael se estiver bloqueado ou se concluiu um bloco grande.

---

## 11. NASCIMENTO DA ILHA — checklist de infraestrutura, de fábrica

Ordem obrigatória. Ilha nova segue isto inteiro antes de existir site.

1. **[RAPHAEL]** Registrar e pagar o domínio no registro.br. É o único gasto e o único passo que exige CPF e cartão. Nenhuma camada faz isso.
2. **Domínio adicional na hospedagem ANTES do DNS.** cPanel da HostGator → Domínios → Create A New Domain, com **raiz própria** (`/home3/<usuário>/<dominio>`), NUNCA compartilhando raiz com outra ilha. Isso cria a zona no servidor.
3. **Só então** apontar os nameservers no registro.br (`ns604` e `ns605.hostgator.com.br`). **Invertendo a ordem o registro.br recusa** ("Pesquisa recusada"), porque valida se os nameservers já respondem pelo domínio. A Aquametria pagou esse erro em 06/09/2026 e a Robometria acertou em 09/09 seguindo esta ordem.
4. Esperar a propagação — na Aquametria demorou ~2h; na Robometria (09/09/2026) foi questão de minutos. Confira pelo servidor autoritativo (`108.179.253.218`), não por resolvedor público. Enquanto isso, trabalhe os blocos de pesquisa da ilha, que não dependem de site. Não marque `bloqueada_por` por causa de propagação.
4b. **SEARCH CONSOLE POR PROPRIEDADE DE DOMÍNIO — logo que o DNS responder, ANTES do WordPress.** No navegador do Raphael: Search Console → seletor de propriedade → "Adicionar propriedade" → cartão **Domínio** (não "Prefixo do URL") → o Google devolve um TXT `google-site-verification=...` → cPanel → **Editor de Zona DNS** → zona da ilha → Adicionar registro → tipo TXT, nome `<dominio>.` (com o ponto final), TTL 14400, texto = o TXT → Salvar → voltar ao Search Console e clicar em Verificar. A verificação é automática em segundos, porque o servidor da HostGator já responde o registro. **Não precisa de site, de SSL nem de senha** — é só DNS. Cobre http, https e www num relatório só, e é a propriedade que a Sentinela lê (`resource_id=sc-domain:<dominio>`). **Nunca remova o TXT depois**: a verificação vive dele. Feito assim na Aquametria e na Robometria em 09/09/2026.
5. WordPress pelo Softaculous, em **português do Brasil**, instalação limpa — **desmarque todos os plugins sugeridos**.
6. **Certificado: o AutoSSL da HostGator roda sozinho e não dá para forçar.** O cPanel desta conta **não expõe** a aba de status do AutoSSL (a rota `#/status` do SSL/TLS Wizard redireciona para `#/create`). É Let's Encrypt, gratuito, em todo plano, e o prazo oficial da HostGator é de **até 24 horas depois da propagação do DNS** (renova sozinho a cada 90 dias enquanto o DNS apontar para eles). Menos de 24 h sem certificado é normal e não justifica chamado no suporte; a checagem automática confere a cada 90 min sem incomodar ninguém. Como o WordPress nasce com URL `https`, **o wp-admin não abre até o certificado sair** — e isso trava só os passos 7 e 8. **Confira o certificado NO NAVEGADOR do Raphael**, nunca pela nuvem: o proxy de saída intercepta TLS e devolve "SSL OK" com certificado próprio enquanto o Chrome mostra "Erro de privacidade". Agende uma checagem automática a cada 40 min que retome do passo 7 quando o certificado sair.
7. No wp-admin: instalar e ativar o **Code Snippets**; remover Akismet e Hello Dolly; instalar **Converter for Media** e **Limit Login Attempts Reloaded**. **Site Kit by Google é OPCIONAL** desde 10/09/2026: a medição passou a ser pela Search Console API, na nuvem, com conta de serviço (`ferramentas/search-console.py`); o Site Kit só entra se o Raphael quiser o painel dentro do wp-admin, e a conexão OAuth dele é sempre um "sim" explícito do Raphael. **Sem plugin de cache** (a HostGator já tem mu-plugin) e **sem plugin de SEO**.
8. Snippet **"<Ilha> Sync"**, copiado do Sync da ilha anterior com as constantes trocadas: nome da ilha, caminho `ilhas/<ilha>/` e **token novo**, gerado na hora. Anote o endpoint do Sync e o do `/status` no `PROMPT.md` da ilha — sem eles a seção 4 não é executável.
9. **MEDIÇÃO — o passo que ninguém pode pular.** A propriedade de domínio já existe desde o passo 4b e é a única necessária. **Dê à conta de serviço do Arquipélago acesso Total nela** (Search Console → Configurações → Usuários e permissões → e-mail da conta de serviço); a partir daí a leitura é `python3 ferramentas/search-console.py <ilha>` na nuvem, sem navegador, e devolve as linhas prontas para `dados/indexacao.md` e `dados/posicoes.md`. Enquanto a credencial não existir no ambiente, a leitura continua pelo navegador do Raphael, como antes. **Submeter o sitemap** e gravar a primeira medição em `dados/indexacao.md`: URLs indexadas, em "descoberta — não indexada", em "rastreada — não indexada", excluídas e por quê. Esse arquivo é **série histórica** — cada medição vira uma linha nova, nunca sobrescreve a anterior. A primeira medição de ilha nova é um zero honesto.
   **A rampa da seção 9 é inexecutável sem isto.** Enquanto o Search Console não estiver verificado, a ilha **não publica leva de malha** — estaria soltando página no escuro, que é exatamente o que desindexa domínio novo. Pode publicar ferramenta, artigo e banco normalmente.
10. Favicon próprio e menu hambúrguer entram na **casca** (seção 6), não como acabamento depois.

O que a ilha nova REAPROVEITA, para o custo ficar honesto: o mesmo repositório (é pasta nova, não repo novo), a mesma hospedagem (o Plano M aceita domínios ilimitados — custo extra zero), a mesma conta da Shopee, o snippet de Sync já depurado e a Fundação única, que **não precisa de rotina nova**. Custo real de uma ilha: o domínio, e alguns minutos dele.

---

## 12. A SENTINELA — o que ela verifica em toda ilha

A Sentinela cuida da ilha viva. Ela **nunca conserta código**: emite veredito e despacha o defeito para a Fundação. Quem constrói não pode ser quem aprova — foi por confundir isso que cinco calculadoras da Aquametria ficaram horas quebradas no ar em 08/09/2026 enquanto a Fundação relatava sucesso.

São duas, separadas por **ritmo**, não por assunto. Não as junte: quando o tempo aperta numa execução que faz as duas coisas, é sempre a metade estratégica que cai, porque a técnica é concreta e termina.

**RONDA DIÁRIA — saúde técnica.** Para cada página publicada da ilha:
- HTTP 200 em tudo que está no sitemap; links internos vivos; nenhuma página órfã
- Executar cada ferramenta com entradas reais e conferir o número na mão
- **Zero `&#038;` DENTRO de `<script>`** — extraia só os blocos `<script>`. Contar na página inteira é teste ERRADO: a casca do tema tem dezenas de ocorrências legítimas. `&amp;` `&lt;` `&gt;` `&quot;` uma vez cada dentro do script são a função `esc()` da própria calculadora, e são legítimos
- Corpo não começa por metadado YAML; script vem do rodapé; tabela de exemplos aparece no HTML servido
- JSON-LD presente; favicon próprio servido; botão de menu com `aria-expanded`/`aria-controls` e links no HTML servido
- Revisão aplicada no `/status` **igual** à do manifest
- Console sem mensagem
- **COERÊNCIA DA RECOMENDAÇÃO:** reprova se algum produto recomendado for contradito pelo próprio texto da página ("o fabricante declara até X" com X menor que a entrada). Verificação por regra objetiva pega defeito de encanamento; defeito de julgamento só aparece lendo o resultado como um leitor leria
- **RECEITA:** registra se os primeiros itens da lista não têm link de loja e existem equivalentes que têm — o topo é o espaço mais caro da página
- Bloco de produto vazio é PORTÃO, não defeito — confirmar lendo o catálogo da página antes de acusar

**LEITURA SEMANAL — o negócio.** Indexação em primeiro lugar (`dados/indexacao.md`, série nova); visitas; vendas por Sub_id; Shopee (link morto, comissão melhor, produto novo vendendo); lacuna de produto e de conteúdo; backlink; **interlinkagem entre ilhas**, que só dá para julgar olhando o arquipélago inteiro; marca. Critério único: ROI. Camada sem dado ainda escreve "ainda sem dado" em vez de inventar análise.

**VERIFICAR POR DÍVIDA, NÃO VARRENDO TUDO.** Primeiro o que foi publicado desde a última ronda (código novo é onde mora defeito), depois a ilha de `ultima_ronda` mais antiga. Mesma reserva por commit da seção 1. Com muitas ilhas, varrer tudo todo dia não cabe numa execução — e tentar é como a verificação morre.

**As duas precisam do computador do Raphael ligado.** A nuvem agendada não alcança os sites: o proxy bloqueia e o WebFetch exige aprovação humana por URL, que não existe em rotina. Por isso a ronda tem que ser econômica.

**Não incomode com "está tudo bem".** Só sinalize defeito, bloqueio ou achado que mude decisão.

**O QUE A RONDA DIÁRIA PODE CORRIGIR SOZINHA** — decisão do Raphael em 09/09/2026.

PODE corrigir, registrando sempre o que corrigiu e por quê:
- Título e meta description de página
- Link interno quebrado ou faltando; página órfã (colocando-a nas listagens que a regra da malha exige)
- Categoria ou taxonomia errada, e item que não devia estar no sitemap
- `noindex` indevido
- Preço vencido no banco, com nova data de coleta; e link de afiliado morto — trocando pelo link vivo do MESMO produto, ou removendo o link e mantendo o produto
- Texto de bloco vazio fora do padrão
- `alt` de imagem faltando

**NÃO pode, nunca, por melhor que seja a intenção:**
- Código de snippet — PHP, JS ou CSS. Vai para a Fundação, sempre
- Fórmula, constante, faixa ou regra de elegibilidade. Dado técnico é da Fundação
- Publicar página nova ou apagar página existente
- Mudar identidade visual da ilha
- Acrescentar ou remover produto do catálogo — isso muda a recomendação, e quem verifica não decide o que é verificado
- Gerar link de afiliado novo na ronda diária. Isso é da leitura semanal, que tem teto de calendário

**As quatro regras que preservam a independência da verificação:**
1. **Correção da Sentinela também passa pelo repositório.** Commit na pasta da ilha e Sync, como qualquer coisa. Nunca direto no WordPress.
2. **Ela NUNCA aprova a própria correção na mesma execução.** Corrigiu, registra no `REGISTRO.md` como "corrigido pela Sentinela — aguardando verificação", e quem confere é a ronda SEGUINTE. Validar o próprio conserto na hora é exatamente o que fez a Fundação relatar sucesso com cinco calculadoras quebradas no ar em 08/09/2026.
3. **Se a correção exigir tocar em snippet, ela para e despacha.** Sem exceção, mesmo que a mudança pareça de uma linha.
4. **Teto de 5 correções por execução.** Mais que isso não é "o pequeno" — é bloco de trabalho, e vai para a Fundação. O teto existe para a ronda não virar construção disfarçada.

### 12.1 ACOMPANHAMENTO DE POSIÇÃO — a leitura semanal é dona disto

Indexar é o meio; **a posição é o alvo** (seção 14.9). A leitura semanal mantém, em `dados/posicoes.md` de cada ilha, uma tabela que cresce semana a semana e nunca é sobrescrita:

| consulta | página | posição hoje | posição semana passada | variação | impressões | cliques | banda |

A fonte é o Search Console (Desempenho → Consultas, últimos 28 dias, país Brasil). **Posição é média, não é um lugar** — anote sempre com uma casa decimal e nunca arredonde para "1º lugar".

**AS BANDAS, E O QUE FAZER EM CADA UMA.** A banda decide a ação; a posição sozinha não decide nada.

- **Sem impressão nenhuma.** A página não entrou na disputa. Não é problema de ranqueamento, é de indexação — volta para a seção 14 e para o `dados/indexacao.md`. Não mexa no texto de uma página que o Google ainda não viu.
- **Posição 21+.** Distância grande demais para conserto de detalhe. O que costuma faltar aqui é **cobertura de intenção**: a página responde a outra pergunta, não à consulta. Despache para a Fundação como lacuna de conteúdo, com a consulta real na mão.
- **Posição 11 a 20 — É AQUI QUE MORA O DINHEIRO.** É a única banda em que trabalho pequeno vira página um. Priorize sempre esta banda antes de qualquer outra, e trate cada linha dela como uma tarefa nomeada, nunca como "melhorar o SEO da página". O que move: título e meta description que digam a consulta com as palavras da consulta; a resposta direta subindo para o primeiro parágrafo; a tabela de exemplos pré-renderizada cobrindo o caso exato que a pessoa buscou; três links internos de páginas irmãs que já rankeiam, com âncora igual à consulta.
- **Posição 4 a 10.** Está na primeira página e ainda não é clicada. O trabalho aqui é de **CTR**, não de conteúdo: título que promete o número, meta que promete a faixa e a fonte, e schema que ganhe destaque na SERP. Compare o CTR desta linha com a média das outras na mesma posição — CTR baixo com posição boa é título ruim, e isso é conserto de minutos.
- **Posição 1 a 3.** Não toque. Sério. Registre e passe adiante.

**O QUE ELA NÃO PODE FAZER, POR MAIS TENTADOR QUE SEJA:**
- **Não mexer em página que está subindo.** Se a posição melhorou em relação à semana passada, a página fica como está por mais uma semana. Mexer no meio da subida troca um sinal que está funcionando por um palpite.
- **Não trocar a URL de página posicionada.** Nunca. Nem para "melhorar o slug".
- **Nada de link pago, troca de link, PBN ou diretório.** A única alavanca de link do Arquipélago é o widget nas lojas (seção 7).
- **Não inventar concorrente nem diagnóstico de SERP sem ter aberto a SERP.** Se não abriu, escreve "não verifiquei".
- Toda correção desta seção obedece ao teto e às quatro regras de independência da seção 12 — inclusive a de que **quem corrige não aprova a própria correção na mesma execução**.

**COMO ELA PROPÕE ACELERAR.** No fim da leitura semanal, no máximo **três** propostas, cada uma com: a consulta, a página, a posição de hoje, o que falta, e a estimativa do que muda. Proposta sem consulta nomeada não vale — é opinião. E o que sai daqui vira bloco na fila da Fundação, com o número da posição na descrição, para a execução seguinte saber por que aquilo entrou na fila.

**A PRIMEIRA MEDIÇÃO DE UMA ILHA NOVA É UM ZERO HONESTO.** Ilha recém-nascida não tem posição, e escrever "sem dado ainda" é a resposta certa. A série só começa a valer quando houver duas semanas.

### 12.2 COMO O DESPACHO CHEGA À FUNDAÇÃO — o canal é o repositório, nunca a memória

A Sentinela não tem repositório (limite de plataforma: rotina com navegador não commita). Mas despacho que fica só na memória é esperança, não despacho — a Fundação não tem garantia de abrir o arquivo certo.

Por isso, **ao terminar cada execução**, a Sentinela dispara a rotina **MÃOS NO REPOSITÓRIO** (`trig_01Jg2qeDDsWDJdU9khHVswqd`) por `fire_trigger`, mandando no `text` uma instrução completa e literal: qual arquivo, qual trecho, qual texto. O que ela manda gravar:

1. Em `ilhas/<ilha>/PROMPT.md`, uma seção `## DESPACHO DA SENTINELA — <data>` **no topo da fila de blocos**, com as correções que a Fundação deve aplicar, uma por linha, cada uma dizendo o que medir depois para saber que ficou pronta. Despacho anterior já cumprido é apagado no mesmo commit; despacho não cumprido continua.
2. Em `ilhas/<ilha>/dados/indexacao.md` (ronda semanal), a linha nova da série. Em `dados/posicoes.md`, idem.
3. No cabeçalho de `ilhas/<ilha>/ESTADO.md`, o campo `ultima_ronda` com a hora desta execução.

A instrução para as mãos tem que ser **autossuficiente e literal** — texto pronto para colar, não "atualize o arquivo". As mãos não decidem nada; se a instrução vier incompleta, elas param e respondem "sem instrução", e o despacho se perde. Prefira uma instrução longa e chata a uma curta e ambígua.

A Fundação, na execução seguinte, lê o `DESPACHO DA SENTINELA` **antes** de qualquer bloco da fila — despacho tem prioridade sobre fila, porque defeito no ar custa mais que bloco atrasado.

---

## 13. ACELERAR NUNCA AFROUXA PORTÃO

Decisão do Raphael, 09/09/2026, para todo o Arquipélago: *"vamos seguir o plano de acelerar, mas de forma segura, porque o mais importante é a nossa indexação no Google e nas ferramentas de IA — não podemos comprometer estes passos de forma alguma."*

**O que a pressa PODE mudar:**
- Quantos blocos uma execução entrega — deixa de ser um por execução quando a fila está cheia e o material já está pronto
- Quantas execuções por dia
- Quantos trabalhadores em paralelo
- A ordem da fila

**O que a pressa NUNCA muda, por mais urgente que pareça:**
1. **O portão de dado** (seção 9): pelo menos 3 itens de banco reais e um número calculado próprio por página. Página sem isso não nasce, nem que a fila fique parada.
2. **A rampa de indexação** (seções 9 e 11): leva de 5 a 10 páginas, medir, e só dobrar se indexou. Soltar dezenas de uma vez em domínio novo desindexa em bloco — isso é acelerar para trás.
3. **A verificação antes de publicar** (seção 8): buscar a URL no ar e conferir com número medido. "Aplicado com sucesso" no log não é evidência de nada.
4. **A visibilidade em IA** (seção 5): tabela de exemplos pré-renderizada, resposta antes da explicação, JSON-LD e procedência na frase. Página publicada sem isso nasce invisível para modelo de linguagem, e teria que ser refeita inteira.
5. **Nunca inventar dado técnico.** Constante sem fonte e voltagem chutada não aceleram nada — criam retrabalho e destroem a confiança, que é o único ativo que separa o Arquipélago das fazendas de conteúdo.

**O teste, quando bater a dúvida:** se a pressa fizer você publicar algo que depois vai precisar ser refeito, corrigido ou desindexado, aquilo não é aceleração, é dívida com juros. Prefira entregar menos no dia e não ter que voltar.

**MUTIRÃO.** Quando a fila estiver cheia e o material pronto, uma execução PODE entregar vários blocos em sequência — desde que **cada um passe pela verificação da seção 8 inteira, individualmente, antes de começar o próximo**. Mutirão é fazer mais coisa certa, nunca conferir menos.

---

## 14. INDEXAÇÃO É A PRIORIDADE MÁXIMA DE TODA ILHA NOVA

Decisão do Raphael, 09/09/2026: *"nosso foco é indexação rápida no Google e nas ferramentas de IA. A estratégia de arquitetura completa, produtos, layout, tudo, deve ser em prol disso."*

**O princípio, e o teste:** toda decisão de arquitetura, de banco e de layout precisa ser explicável como "isso faz uma página ser rastreada, indexada e citada mais cedo". O que não passa nesse teste espera a vez, por melhor que pareça.

### 14.1 O recurso escasso é o orçamento de rastreamento
Domínio novo tem orçamento de rastreamento minúsculo. Cada URL fraca gasta orçamento que uma página boa precisaria, e ainda ensina ao Google que este site produz coisa que não vale voltar para buscar. Daí a regra que inverte a intuição: **menos páginas, melhores, indexam mais rápido do que muitas.** Volume é consequência da indexação, nunca causa.
O sitemap é **curadoria, não inventário**. Página que não merece ser indexada não entra nele — e, quase sempre, não deveria existir.

### 14.2 Ordem de nascimento das páginas, por valor de indexação
Esta ordem vale para toda ilha. Não pule etapa para "ganhar tempo".

1. **PÁGINAS DE PARÂMETRO** — a busca é literalmente a pergunta e a resposta é um número calculado pela própria ilha ("quantos watts de aquecedor para 60 litros", "quantos Pa para pelo de cachorro em 80 m²"). Maior retorno de indexação que existe aqui: a intenção é exata, a concorrência é fraca, e a resposta é nossa. **Nascem primeiro, sempre.**
2. **PÁGINAS DE ENTIDADE do nicho** — espécie, modelo de equipamento, tipo de peça. Busca perene e de volume, e a ilha acrescenta um número que ninguém dá ("quantos litros para N deste peixe").
3. **CRUZAMENTOS** entidade × parâmetro — cauda longa de verdade, só com dado real nas duas pontas.
4. **FICHA DE PRODUTO — por último, e seletiva.** Ficha de produto de site afiliado compete com o fabricante, com o marketplace e com dez lojas, todos com mais autoridade e com a página que a pessoa realmente quer, que é onde dá para comprar. Sem preço e sem estoque, ela é fina e duplicada — o perfil de afiliado que o update de março de 2026 pune. **Só crie ficha de produto quando existir dúvida paramétrica que o fabricante e a loja NÃO respondem** ("este filtro serve mesmo no meu aquário de 120 L?"), e a página tem que carregar o número, o critério, a fonte e a data. Sem isso, o produto vive dentro do resultado da ferramenta e da vitrine, não numa página própria.

### 14.3 O tamanho do banco é COBERTURA, não número redondo
Nunca persiga uma meta do tipo "60 produtos" — número redondo não é critério.
**O critério é: nenhuma faixa que as ferramentas da ilha conseguem produzir pode sair sem pelo menos 3 produtos elegíveis.** Mede-se varrendo a faixa de entrada de cada ferramenta de ponta a ponta e contando quantos itens do banco passam em TODAS as condições declaradas (seção 7). O que falta nessa varredura é a lista de compras do banco — e o número final aparece sozinho: pode dar 40, pode dar 90.
Produto que não fecha nenhuma faixa descoberta não é prioridade, por melhor que seja a comissão. Faixa descoberta é a única urgência de catálogo.
**O Raphael descartou explicitamente a meta de "60 produtos" em 09/09/2026** — foi número redondo, não critério. Vale a cobertura de faixa.

### 14.4 Categorias e listagens: poucas, e cada uma é uma página de verdade
- Listagem só existe com **3 itens ou mais** e um critério que alguém realmente busca.
- Toda listagem tem texto próprio explicando o critério — listagem que é só uma grade de links é página fina.
- Categoria automática do CMS (a "sem categoria", arquivos por data, tags geradas) fica **fora do sitemap**, e de preferência com `noindex`.
- Paginação com `canonical` correto; nunca duas URLs servindo o mesmo conteúdo.

### 14.5 O layout também serve à indexação
- **O que responde tem que estar no HTML SERVIDO.** Ferramenta que só calcula em JavaScript é página vazia para robô e para modelo de IA: por isso a tabela de exemplos pré-renderizada é obrigatória (seção 5).
- **Resposta antes da explicação**, na primeira dobra, em frase autossuficiente com fonte e data. É essa frase que é citada.
- **Título e H1 são a pergunta que a pessoa digita**, não o nome interno da ferramenta.
- **Nenhuma página órfã:** toda página entra em pelo menos 2 listagens e aponta para 3 irmãs (seção 9). Página que ninguém linka, o robô não acha.
- **Navegação em HTML servido**, com `<a href>` de verdade — é por isso que o menu hambúrguer é feito do jeito descrito na seção 6.
- **Peso e estabilidade:** sem biblioteca desnecessária, imagem com `width`/`height` e `loading="lazy"`. Página lenta é página rastreada com menos frequência.
- **JSON-LD** em toda página (seção 5).

### 14.6 A rampa, e o gatilho de parada
Primeira leva de 5 a 10 páginas. Medir. Só dobra se a leva anterior **indexou E apareceu** — com impressão registrada e posição medida. Indexar sem impressão significa que a palavra-chave estava errada; nesse caso corrija a escolha de consulta antes de aumentar o volume. Se a leva anterior ficou em "descoberta — não indexada", **não publique mais nenhuma página de malha** até descobrir por quê: mais páginas nesse estado pioram o problema em vez de compensá-lo.
Cauda longa só nasce **depois** de a página-âncora do mesmo assunto estar indexada. Âncora primeiro, ramificação depois.

### 14.7 Sinais externos, porque domínio sem link é raramente visitado
- **Submeter o sitemap** e pedir indexação manual das primeiras páginas de cada leva.
- A **prospecção do widget em lojas** é a única alavanca de link do projeto e por isso vale mais no começo do que no fim: backlink é o que faz o robô voltar.
- Nada de link pago, PBN ou troca em escala — a penalização custa mais do que o ganho.

### 14.8 A decisão é tomada com número, nunca com sensação
Toda ilha mantém `dados/indexacao.md` como **série histórica** (seção 11, passo 9): cada medição é uma seção nova, nunca sobrescreve. É essa série — e não impressão de ninguém — que autoriza dobrar a leva, manter ou parar.

### 14.9 O alvo não é indexar — é a PRIMEIRA PÁGINA, com palavra-chave que vende
Raphael, 09/09/2026: *"indexação, ranqueamento, primeira página do Google — é isso que importa, com foco em palavra-chave que vai gerar venda e dinheiro no nosso bolso."*
Indexar é o começo, não o fim: página indexada na posição 40 vale zero. Por isso toda página nasce com DOIS compromissos escritos no próprio arquivo: **a consulta principal que ela mira** e **por que ela consegue chegar às 10 primeiras**.
**ANTES de criar a página, olhe a SERP daquela consulta e classifique quem ocupa o top 10:**
- Fazenda de conteúdo, marketplace e fabricante com domínio forte ocupando quase tudo → **a página NÃO nasce agora.** Anote numa lista de "quando houver autoridade" e siga para a próxima consulta. Publicar ali é gastar rastreamento de domínio novo para estacionar na página 4.
- Fórum, vídeo, blog de loja velho, ou resposta genérica que não dá número → **é alvo.** É onde a resposta paramétrica com fonte e data ganha, e é exatamente o buraco que a Bússola procura ao aprovar um nicho.
**A prioridade é o cruzamento de duas coisas, nunca de uma só:** intenção de compra × chance real de primeira página. Volume alto sem chance é página desperdiçada; chance alta sem intenção é visita que não vira dinheiro. Consulta sem nenhuma das duas não entra na fila, por mais fácil que seja de escrever.
**Meça posição, não só indexação.** Em `dados/indexacao.md`, cada página registra a consulta-alvo e a posição média dela.

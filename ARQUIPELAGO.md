# CONTRATO DO ARQUIPÉLAGO

## 0. MAPA DE LEITURA — leia só a sua parte (12/09/2026)

Este contrato tem mais de 500 linhas e continua crescendo. **Ninguém lê tudo.** Cada papel abre as seções da sua linha e para. Ler seção de outro papel não é zelo: é gastar orçamento de contexto que faria falta no trabalho da ilha.

| Papel | Seções |
|---|---|
| **Fundação** | 1 a 11, 13 a 18, 20, 21, 22 |
| **Sentinela — ronda diária** | 2, 3, 4, 10, 12, 15, 16, 18, 19, 21, 22 |
| **Sentinela — leitura semanal** | 2, 3, 4, 10, 12, 12.1, 14, 18, 21 |
| **Bússola** | 10, 11, 14, 20, 21 — e `bussola/BUSSOLA.md`, que é a lei dela |
| **Pauta das ilhas** | 10, 14, 15, 16, 17, 21 |
| **Mãos no repositório** | nenhuma. A decisão já vem no disparo; ler o contrato é sinal de que virou Fundação |

**Sempre, para todo papel:** seções **2** (cabeçalho de estado), **3** (o repositório é o lugar do trabalho), **4** (o site fica para trás em silêncio), **10** (regras que valem sempre) e **18** (correção fura a fila).

**Como extrair só o que é seu**, sem carregar o arquivo inteiro:

```
awk '/^## 12\./{p=1} /^## 13\./{p=0} p' ARQUIPELAGO.md
```

Troque os dois números pelo começo da sua seção e pelo começo da seguinte. Para várias seções, rode uma vez por seção. **Quem tiver dúvida se uma seção é sua, lê — errar por ler a mais é barato; errar por não saber a regra custa uma leva inteira.**

Regras que valem para TODA ilha. Quem executa um bloco lê este arquivo primeiro e depois o `PROMPT.md` da ilha sorteada. Regra nova do Arquipélago se escreve AQUI, uma vez — nunca copiada para dentro dos prompts das ilhas.

Vocabulário: cada site de nicho é uma **ilha**, o conjunto é o **arquipélago**, o portão de publicação é o **desembarque**. Camadas: **BÚSSOLA** (decide o nicho) → **FUNDAÇÃO** (constrói) → **SENTINELA** (cuida da ilha viva).

---

## 1. COMO A FUNDAÇÃO ESCOLHE A ILHA DE CADA EXECUÇÃO

> ANTES de aplicar a rotação desta seção, leia a seção 18: ilha com despacho aberto tem prioridade sobre a ilha mais atrasada.

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

**BLOQUEIO DE REDE SE RECONFERE A CADA EXECUÇÃO, ou ele vira permanente sozinho (Clube do Mosaico, 11/09/2026).** A regra acima manda testar antes de presumir bloqueio, e falta a outra metade: **testar de novo antes de continuar presumindo.** Duas execuções seguidas leram um `curl` devolvendo `000` no domínio da ilha 3, escreveram "403 ao CONNECT, o domínio nunca entrou na lista Personalizada" no `ESTADO.md`, deixaram o item aberto como o contrato manda — e a execução seguinte leu aquilo como fato. Na terceira, o mesmo `000` apareceu; o **mesmo comando, repetido minutos depois, devolveu 200**, e o Sync, o `/status`, as nove páginas e o sitemap também. Era intermitência do túnel. Custou duas revisões presas e dois dias de uma ilha fora do ar por um diagnóstico que ninguém reconferiu porque estava escrito com número. Portanto: **uma falha de rede só vira bloqueio depois de repetir na mesma execução**, e todo bloqueio de rede herdado do `ESTADO.md` é retestado antes de ser respeitado — são dois comandos e resolvem o que a prosa não resolve.

**CACHE DUPLO:** o `raw.githubusercontent` guarda ~5 min e o WebFetch guarda 15 min por URL. Sempre acrescente `?v=<hora e minuto>` na URL ao verificar, ou você conclui erradamente que nada mudou.

**O CACHE É POR CAMINHO, NÃO POR COMMIT — e o primeiro "0 aplicado(s)" não é resposta (Clube do Mosaico, 11/09/2026).** O Sync baixa o `manifest.json` e cada arquivo que ele indexa em requisições separadas, e elas saem do cache em momentos diferentes: nos dois primeiros disparos deste bloco o Sync leu um manifest ainda na revisão anterior **enquanto já baixava o snippet novo**, e recusou aplicar com "sha256 divergente". A trava funcionou — o desembarque parcial é exatamente o que ela existe para impedir —, mas o log fica com cara de defeito e não é. Três coisas seguem disso, e valem para toda ilha: (1) **o `?v=` que o Sync já acrescenta não garante nada**, porque quem serve a borda pode ignorá-lo, e o servidor da hospedagem sai por um nó diferente do da nuvem — conferir o `raw` daqui e ver o arquivo novo **não prova** que o site vai ver; (2) **"sha256 divergente" logo depois de um push é cache, não corrupção**: espere alguns minutos e dispare de novo, em vez de mexer no manifest; (3) **só o `/status` com a revisão do manifest é entrega** — ler o primeiro "0 aplicado(s)" como pronto é a forma disfarçada do "commit sem Sync" que a seção 20 existe para impedir. Repita o disparo até a revisão bater, e escreva no relatório quantos disparos foram precisos.

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

> Cor, fonte, escala e componentes desta ilha não moram mais aqui: moram em `ilhas/<ilha>/DESIGN.md`, e quem manda neles é a **seção 22**. Esta seção 6 continua valendo para o que é comportamento de interface, não para token.

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
- **DOIS PROGRAMAS DE AFILIADO, uma regra só de ordem.** Desde 09/09/2026 o Arquipélago tem **Shopee Afiliados** e **Mercado Livre Afiliados** (perfil RMNATAL, aberto pelo Raphael; painel em `mercadolivre.com.br/afiliados/hub`). O Mercado Livre existe porque a Shopee não vende as marcas de loja especializada (na Aquametria: Eheim, JBL, Chihiros, Atman canister) — um marketplace só cobre só a faixa de marcas que ele vende, e isso vale para toda ilha. **A ordem da lista continua sendo a da regra acima — elegibilidade, adequação, e loja só como desempate.** Programa nunca é critério de ordem; quando o mesmo produto existe nos dois, **o link é o da Shopee** (decisão do Raphael em 10/09/2026: a atribuição de 7 dias da Shopee é verificada nos termos oficiais e vale para **qualquer compra na plataforma** dentro da janela — venda direta (o produto linkado) paga a comissão padrão MAIS a comissão extra do vendedor; venda indireta (outro produto comprado após o clique) paga só a comissão padrão — a extra é exclusiva da venda direta, e a atribuição é por último clique (fonte: help.shopee.com.br/portal/10/article/163055, lido em 10/09/2026). Um link da Shopee vale pela cesta, e a recomendação certeira é o que faz a venda ser direta. A janela e a regra de cesta do Mercado Livre nunca foram confirmadas), e o Mercado Livre entra onde a Shopee não tem o produto — nunca pela comissão maior. **Amazon Associados fica FORA de todas as ilhas** enquanto não houver tráfego: sem 3 vendas em 180 dias a conta é encerrada, e o relógio começa no cadastro. Regras de conta que a Sentinela semanal vigia: Shopee e Mercado Livre não têm prazo de inatividade conhecido (o do ML segue **não verificado** — ler na central de ajuda logado); a única punição conhecida nos dois é autocompra.
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
- **TESTE QUE MEDE A SI MESMO É UM TESTE VERDE QUE NÃO MEDE NADA.** Aprendido na Robometria em 10 e 11/09/2026, quebrando o código de propósito para ver seis travas novas reprovarem: **três delas passaram**, e as três tinham a mesma forma. (1) A régua da regra morava no snippet e o teste a chamava para conferir o que o snippet publica — trocar um `>` por `>=` fazia as duas metades errarem juntas. (2) A grade de casos nunca pisava na borda — varrida de 10 em 10, ela não conseguia separar `ceil` de `floor + 1`, porque nenhum múltiplo das constantes terminava em zero. (3) A conferência procurava o texto na página INTEIRA e o achava dentro do próprio JSON-LD, passando até com resposta inventada. Daí as três regras: **quem confere escreve a própria régua**, nunca chama a de quem produziu o dado; **grade tem que incluir a borda**, senão é amostra com nome de grade; e **afirmação sobre o que a página diz se mede no CORPO**, nunca no HTML completo — é o mesmo erro de contar `&#038;` na página inteira em vez de dentro do `<script>`.
- **O RENDER DE BANCADA TEM QUE SERVIR O QUE O SITE SERVE, e a metade que falta some em silêncio.** Mesma execução, mesmo dia: o renderizador da Robometria montava a página sem `is_page()`, então todo snippet respondia "não estou na minha página" e o HTML saía sem folha, sem JSON-LD e sem rodapé; e não carregava nas options o que o Sync carrega, então cada página caía no aviso de "estamos sem o banco" — **que é uma página válida**, com cabeçalho e rodapé. Nos dois casos o shortcode aparecia e a página PARECIA inteira: a medição de rolagem horizontal deu 0 px duas vezes medindo 26 KB do que no ar tem 62 KB. **Antes de confiar num número medido em bancada, confira que a página medida tem o tamanho da página real.**
- **PERDOAR POR PRESENÇA DE PALAVRA É ADIVINHAR — quem afirma sobre texto declara no markup o que é exceção.** Quarta trava da mesma família, aprendida no Clube do Mosaico em 11/09/2026. O teste que proíbe escassez inventada (seção 7) precisa deixar passar a frase legítima que diz *"não publicamos selo de mais vendido"*, e a tentação é procurar uma negação perto do termo. Duas versões caíram: a primeira reprovou a página Sobre, que é justamente onde a recusa deve estar escrita; a segunda, que perdoava a frase com qualquer negação, **aprovou** a mutação *"a ficha técnica do silicone acético mais vendido do Brasil lista … entre as superfícies em que o produto NÃO deve ser usado"* — o "não" da frase negava outra coisa. A saída não é uma heurística melhor, é parar de heurística: **a página marca o bloco de recusa no próprio markup** (uma classe), o teste retira esses blocos e proíbe o termo em todo o resto. E para a declaração não virar porta dos fundos — bastaria marcar uma promessa como recusa —, exija que **todo bloco marcado ABRA negando**, e que eles sejam poucos e contados; a mutação que enfiou *"Peça mais vendido, últimas unidades!"* dentro do bloco de recusa passou enquanto a regra só pedia negação em algum lugar dele. A regra vale para toda afirmação sobre o que a página diz, não só para escassez: quando o texto legítimo e o proibido são a mesma palavra, quem decide é a estrutura, nunca a vizinhança. **E vale a pena escrever a trava mesmo assim: foi a segunda versão dela, antes de ser reprovada, que achou um defeito real escrito pela própria Fundação** — a home da ilha chamava o produto de "o silicone acético mais vendido", número de venda que nenhuma ilha mediu.
- **PÁGINA FINA NÃO ENTRA NO ÍNDICE DE DOMÍNIO NOVO — e a bancada sabe medir isso antes de publicar.** Mesma execução: a trava que confere se a página medida tem tamanho de página (regra acima) reprovou duas páginas da casca que ninguém tinha percebido serem finas — `/como-fazer/` com 971 caracteres de corpo e `/contato/` com 1.194. Não era defeito de render: as páginas eram magras mesmo, e iam para o sitemap de um domínio recém-nascido gastar orçamento de rastreamento (seção 14.1). **Meça o corpo de toda página da casca e trate menos de ~1.500 caracteres como reprovação**, com duas saídas honestas: dar à página conteúdo real — tirado do banco da ilha, nunca enchimento — ou não publicá-la. As duas do Clube do Mosaico ganharam conteúdo do próprio banco e passaram a 2.716 e 1.813.
- **PERGUNTA QUE CARREGA A RESPOSTA NÃO É COLETA — é a mesma armadilha do teste que mede a si mesmo, agora na hora de colher o dado.** Aprendido no Clube do Mosaico em 11/09/2026, procurando o coeficiente de consumo do rejunte epóxi. A busca foi feita com o número candidato **escrito dentro da consulta** ("...coeficiente CR 1,55 boletim técnico"), e a resposta voltou confirmando 1,55 — com a cara de declaração do fabricante. Era eco: o número tinha sido plantado pela própria pergunta. A segunda tentativa, com pergunta limpa, generalizou para o epóxi um coeficiente que só estava publicado para o cimentício, **e ainda inventou uma justificativa técnica para ele**. As duas foram descartadas e a pendência ficou aberta. Daí a regra, que vale para toda coleta de toda ilha: **nunca ponha na consulta o valor que você quer confirmar** — pergunte qual é o valor, não se o valor é X; e quando a resposta vier sem citar o documento que a sustenta (código, arquivo, revisão, data), ela não é fonte, é paráfrase. Constante que chega assim entra como `pendente`, nunca dentro de fórmula publicada. É a versão de coleta da cicatriz anterior: lá, quem confere chamava a régua de quem produziu o dado; aqui, quem pergunta escreve metade da resposta.
- **CATEGORIA NOVA HERDA A RÉGUA DA ANTIGA EM SILÊNCIO, e o teste verde é o sintoma.** Mesma execução, mesma ilha. A matriz de compatibilidade da ilha era de **cola** — base × ambiente — mas o código que a recomputava varria **todos** os materiais do banco, sem olhar categoria. Passava há três blocos, e passava só porque o banco tinha uma categoria só. O primeiro rejunte gravado fez as 18 células falharem de uma vez, cada uma acusando os cinco rejuntes de "eliminados por silêncio" — frase sem sentido para um produto que nunca foi candidato a colar nada, porque rejunte não toca a base. **O conserto tentador é o perigoso:** colar os ids novos nas células esperadas devolve o verde e o significado nunca volta. Duas regras: **toda régua declara sobre qual categoria ela decide, e isso se confere em código**, não na cabeça de quem escreveu; e **categoria nova ganha régua própria quando as declarações do fabricante nomeiam coisas diferentes** — na cola a lista é de substrato, no rejunte é da peça que será rejuntada, e traduzir uma no vocabulário da outra produz uma afirmação sem sentido que entra calada no cálculo.
- **NÚMERO CRAVADO NA TELA ERA VERDADE QUANDO FOI ESCRITO — e o teste só mede a metade que existia naquele dia.** Terceira da mesma execução, e a única que já estava **no ar**. A casca da ilha mostra, em cada cartão de categoria, quantos itens reais o banco tem — o número que separa promessa de trabalho feito. Cinco dos seis cartões traziam `0` digitado à mão, o que era exato enquanto só uma categoria tinha dados. No dia em que a categoria rejunte ganhou cinco produtos, o cartão dela continuou dizendo zero, e **o teste aprovou**, porque conferia contra o banco apenas a categoria que existia quando ele foi escrito. A regra: **número de tela nasce contado, nunca digitado**; e a conferência varre a pasta de dados inteira, cobrando as duas direções — categoria mostrada sem arquivo de banco é promessa, e arquivo de banco sem categoria mostrada é dado colhido que a tela nunca usa. Vale para qualquer contagem publicada: itens no banco, páginas na malha, produtos esperando link.
- **AFIRMAÇÃO DA PÁGINA SOBRE O PRÓPRIO BANCO SE CONTA, NUNCA SE DIGITA — e isso não vale só para a tese de artigo.** A Robometria já sabia disso para o artigo-âncora (número que é a tese não pode estar escrito no HTML, porque passa a mentir em silêncio quando o banco cresce) e mesmo assim publicou meses, na página de **metodologia**, uma coluna "Temos hoje" digitada dentro do snippet, dizendo que a ilha não tinha nenhuma fonte de nível 2 enquanto quatro fontes do banco se declaravam nível 2. As duas metades nunca se falavam, então nenhuma podia corrigir a outra. Ao trocar a coluna por uma contagem, caiu **um segundo número que ninguém procurava**: o degrau de anúncio de marketplace dizia "sim" e a ilha não tinha uma única fonte daquele tipo. A regra é a mesma para qualquer frase em que a página fala de si: quantas fontes, quantos produtos, quantas páginas, desde quando. **E a derivação tem que ler TODAS as origens, ou é pior que o número digitado que substituiu:** a primeira versão daquele contador lia dois dos três arquivos e declarava, com ar de medição, que a ilha não tinha fonte editorial — quando tinha sete, citadas em toda resposta de uma das ferramentas. Número medido errado é pior que número digitado errado, porque este parece conferido.
- **BANCADA QUE MONTA MUITAS PÁGINAS NO MESMO PROCESSO MEDE A SEGUNDA PELA METADE.** Terceira vez que a Robometria paga por render que serve menos que o site, e a causa nova é a mais discreta das três: um `static` legítimo dentro do snippet da marca, que existe para o logotipo não sair duas vezes na MESMA página. No site um processo é uma requisição e ele está certo; num varredor que monta 72 estados em sequência, ele faz o cabeçalho aparecer no primeiro e sumir nos 71 seguintes — e o varredor mede 915 KB do que no ar tem 960 KB, sem erro nenhum. **Varredura de muitos estados roda um processo por estado**, e isso mata junto qualquer outro resíduo (filtro registrado duas vezes, cache de função, option carregada pela metade). Custa segundos; medir a metade errada custa um bloco.
- **VARRER A ENTRADA INTEIRA, NÃO O CASO-ÂNCORA — "o corpo" de uma ferramenta é o corpo de TODAS as respostas dela.** A seção 8 já mandava medir no corpo, e a Robometria media: renderizava as nove páginas e conferia. Só que ferramenta de entrada variável serve uma página por consulta, e a página sem consulta é o caso-âncora. Português sem acento vindo do banco ficou invisível para **cinco testes verdes** porque as palavras só apareciam quando alguém escolhia um modelo de uma marca específica. Quem afirma sobre o que a ilha serve monta cada modelo, cada situação e as bordas da faixa — 72 estados, no caso — e afirma sobre a soma. Amostra com nome de varredura é o mesmo defeito da grade que não pisa na borda.
- **A BANCADA E O SITE TÊM QUE LER A MESMA FONTE PARA O MESMO CAMPO — senão o portão fica verde sobre um dado que nunca vai ao ar.** Aquametria, 11/09/2026, e é primo do "render de bancada tem que servir o que o site serve", mas pior de achar: lá a página medida era menor que a real; aqui ela era **igual em tudo menos num campo**, e o campo era o título. Quem grava `post_title` é o Sync, e o Sync lê `titulo` do `manifest.json`; o front matter do `.md` ele nem abre. A bancada inteira — 293 afirmações de voz, 288 de árvore, 224 medições em Chromium — renderizava do `.md`. E a ferramenta que atualiza o manifest só recalculava `sha256`: o `titulo` **nunca** era reespelhado. Resultado do desembarque: o corpo das nove páginas trocou no ar, os nove títulos não, o log do Sync disse "18 aplicado(s)" e **nenhum portão podia ver**, porque todos liam a metade que estava certa. Três regras: (1) **para cada campo publicado, aponte quem é a fonte e faça a bancada ler DELA** — se o Sync lê o manifest, a bancada lê o manifest; (2) **a ferramenta que espelha um campo de uma fonte para outra imprime cada troca que fez**, senão o espelho envelhece calado; (3) **uma afirmação cobra que as duas fontes digam a mesma coisa**, e ela nomeia a ferramenta a rodar. Corolário para as mutações: quando a bancada muda de fonte, **toda mutação que editava a fonte antiga vira inerte** — 18 de 20 reprovaram sem medir nada até as três serem reapontadas. Mutação que não morde é teste verde com outro nome.
- **Antes de escrever qualquer snippet PHP, releia a fase 4b do playbook** (`/areas/playbook-nascimento-projeto.md`): nunca confie na ausência de erro; evite `$_SERVER` literal (use `add_query_arg( array() )`, porque o ModSecurity mata a gravação em silêncio); snippet começa com `/**`; texto na tela sai acentuado; nome de snippet descritivo, nunca numerado.

---

## 9. Malha de páginas — limitada por dado, não por calendário
> A rampa desta seção só passa a ler o sinal de impressão depois do PISO da seção 21. Antes do piso, zero impressão não trava leva nenhuma.

- **ORDEM DAS LEVAS — por intenção de compra, não por facilidade de gerar página.** Tráfego e tráfego não são a mesma coisa. "Quantos litros para 10 neons" traz um curioso; "qual aquecedor para 100 L em 220 V" traz alguém com o cartão na mão. Os dois indexam, os dois contam como tráfego orgânico, mas um está a um clique do dinheiro e o outro está a meses. Como a malha sai em levas pequenas por causa da rampa, **a ordem das levas decide qual tráfego chega primeiro** — então a primeira leva de cada camada é sempre a dos clusters cuja resposta termina num produto do banco. Isso não afrouxa o portão nem a rampa: só escolhe, entre as páginas que já passariam, quais nascem antes.
- **Portão inegociável:** pelo menos 3 itens de banco reais **e** um número calculado próprio por página. Cauda longa vazia em domínio novo causa desindexação em bloco.
- **Rampa guiada por indexação:** primeira leva de 5 a 10 páginas; se indexou, dobre; se ficou em "descoberta e não indexada", **não** aumente.
- **Regra da malha:** toda página entra em pelo menos 2 listagens e aponta para 3 irmãs; link de mão dupla; nenhuma página órfã.

---

## 10. Regras que valem sempre

- **O repositório é a fonte da verdade.** A nuvem não alcança os sites por HTTP direto; o desenho é PULL. Para checar, WebFetch (GET), nunca curl.
- **Desembarque automático**: ferramentas, páginas-âncora, artigos, páginas de entidade e snippets vão ao ar sem consulta. O portão humano fica só para publicação programática em escala.
- **Nunca invente dado técnico.** Toda constante e toda especificação citam a fonte do fabricante e levam data. Constante com status `pendente` é proibida dentro de fórmula publicada.
- **O NÍVEL DE UMA FONTE É O DO ELO MAIS FRACO — autoria, custódia e leitura são três coisas, e a escada guarda uma só.** Aprendido na Robometria em 11/09/2026. O banco declarava quatro fontes no nível 2 ("manual do fabricante"), e as quatro eram o mesmo manual da Electrolux hospedado em `manuals.plus`, colhido por busca, sem leitura direta. O documento era mesmo do fabricante — o elo da autoria era forte —, e foi por isso que alguém escreveu 2: a escada tem um número só e o instinto é preenchê-lo pelo elo mais forte. **Toda origem tem três: quem escreveu o documento, quem o guarda, e como nós o lemos. O nível é o do mais fraco, sempre.** A direção sai da assimetria de custo, como toda decisão de fonte: errar para baixo custa uma frase mais fraca na tela ("a confirmar no manual"); errar para cima faz a página de metodologia declarar um rigor que a ilha não tem — e metodologia é a página cujo único produto é o rigor. Numa fábrica que existe para substituir copy de anúncio por procedência, inflar o próprio nível de fonte é o defeito mais caro que existe. **E a regra só vale se for mecânica:** o validador de banco confere que a `origem` bate com a `origem` que a escada dá àquele `nivel` (era exatamente por aí que o defeito entrava — só o número era conferido), e os degraus de cima exigem um campo `leitura` **declarado**, porque silêncio nunca promove. Deduzir "foi lido direto" do texto do canal de coleta seria a heurística por vizinhança que a seção 8 proíbe.
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

> A regra "a Sentinela nunca conserta" foi revogada em 11/09/2026: leia a seção 19 antes de decidir entre consertar e despachar.


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

## 15. CADA ILHA TEM UMA VOZ — rigor no dado, nunca no tom (11/09/2026)

Decisão do Raphael em 11/09/2026: as ilhas estavam todas com a mesma cara e a mesma linguagem técnica, "explicando as calculadoras em parte científica". O rigor de número, fonte e data (seções 7 e 14) é a tese de SEO e de visibilidade em IA e FICA. Mas ele vira **camada de prova**, nunca a voz da página.

15.1 **`ilhas/<ilha>/VOZ.md` é obrigatório** e a Fundação o lê antes de escrever qualquer título, parágrafo, rótulo de botão ou texto de menu. Ele diz quem entra, em que momento, quem fala, como fala, frases com a cara da ilha e frases proibidas, o que vai na home e qual molde de casca a ilha usa. A Bússola entrega o `VOZ.md` no dossiê (item g). Ilha sem `VOZ.md` não recebe bloco novo até ele existir.

15.2 **Regra de camadas.** Título, primeiro parágrafo, rótulos e chamadas falam com a pessoa na voz do `VOZ.md`, com as palavras que ela digitaria. Número, código de peça, nome de fabricante, data de leitura e link "fonte" moram na camada de prova: tabela da ferramenta, bloco "como sabemos" no fim da página, JSON-LD. Nunca no título, nunca no primeiro parágrafo, nunca como manifesto na home. O que a seção 14 exige para ranquear (resposta antes da explicação, número na primeira linha do resultado) continua — a diferença é a linguagem em que o número aparece.

15.3 **Três moldes de casca**, escolhidos pelo `VOZ.md`:
- **LOJA** (ex.: Clube do Mosaico): produto primeiro, foto grande, ferramentas e guias como apoio.
- **FERRAMENTA** (ex.: Robometria): a ferramenta principal é a home; resultado e bloco de compra acima de tudo.
- **GUIA** (ex.: Aquametria): a pergunta mais frequente em cima, calculadoras como cartões na linguagem da pessoa, guias embaixo.
Os três compartilham a infraestrutura (seções 4, 7, 8, 9, 14), não a aparência: header claro por padrão, paleta e tipografia da identidade da ilha, e o layout do molde. Duas ilhas com o mesmo molde ainda precisam parecer sites diferentes.

15.4 **A ronda da Sentinela (seção 12) verifica tom**: em cada página visitada, "isso fala como o público do `VOZ.md` ou como um manual?". Título ou primeiro parágrafo com termo da lista de proibidas, ou home em forma de manifesto, é defeito e vira despacho como qualquer outro.

15.5 **Transição das ilhas vivas.** Aquametria, Robometria e Clube do Mosaico ganham `VOZ.md` em 11/09/2026. Para cada uma, o primeiro bloco após esta data é a **reescrita da home e do header pelo molde e pela voz**, antes de qualquer bloco novo de fila; em seguida, cada página existente é reescrita na voz ao passar pela ronda, sem trocar URL, sem mexer no que já está posicionado (seção 12.1) além do texto.

## 16. ÁRVORE, BREADCRUMB E CLUSTER — a malha é um silo de tópico, em toda ilha (11/09/2026)

Decisão do Raphael em 11/09/2026: toda ilha nasce com hierarquia visível na URL, breadcrumb e interlinkagem em cluster, porque isso fortalece o SEO (a autoridade de uma página forte escorre para as novas do mesmo assunto) — não é estética. A malha da seção 9 passa a ser construída DENTRO desta árvore. Vale para as três ilhas vivas e para toda ilha futura; o `VOZ.md` de cada ilha só escolhe os nomes dos níveis.

16.1 **Três níveis, e a URL mostra os três.** Nível 1 = seção (`/materiais/`, `/pecas/`, `/calculadoras/`, `/guias/` — o que a ilha tiver). Nível 2 = categoria, com o nome que a pessoa usa (`/materiais/colas-e-adesivos/`). Nível 3 = a pergunta ou o produto, com as palavras que a pessoa digita (`/materiais/colas-e-adesivos/cola-para-vaso-de-ceramica/`). Sem quarto nível; sem página solta na raiz além de home, sobre, contato, divulgação de afiliados e privacidade.

16.2 **Como isso vive no WordPress.** Páginas de nível 1 e 2 são páginas-mãe (page parent) OU termo de taxonomia hierárquica própria da ilha (ex.: `material_categoria`), a critério do molde — nunca a categoria padrão de post nem tag. Ferramentas e artigos de nível 3 têm o pai definido no cadastro; o slug é gerado da consulta-alvo. Toda página nova nasce com pai; página sem pai é defeito e não publica (trava na seção 8).

16.3 **Breadcrumb em toda página** abaixo do header: `Início › Materiais › Colas e adesivos › Cola para vaso de cerâmica`, cada nível linkado exceto o atual; e `BreadcrumbList` no JSON-LD com as mesmas URLs. Na home não há breadcrumb.

16.4 **Cluster de interlinkagem, obrigatório e bidirecional.** (a) A página-mãe (nível 1 ou 2) lista TODAS as filhas com o texto-âncora igual à consulta-alvo da filha, nunca "clique aqui" nem "saiba mais". (b) Toda filha linka a mãe no breadcrumb E numa frase do corpo. (c) Toda filha linka de 2 a 4 irmãs (mesma mãe) em bloco "Veja também" com âncora na consulta delas — escolhidas por afinidade, não aleatórias. (d) Ferramenta linka o guia que a explica e o guia linka a ferramenta, no corpo. (e) Produto do banco linka a ferramenta que o recomenda e a ferramenta linka o produto pelo bloco de compra (seção 7). (f) Nenhuma página órfã: toda URL do sitemap tem pelo menos 2 links internos apontando para ela, um deles da mãe. A Sentinela conta isso na ronda.

16.5 **Categoria só nasce com filhas.** Página de nível 2 é publicada quando tem pelo menos 3 filhas com dado real (portão da seção 13); até lá o cartão na mãe não é link e diz "em breve", sem contagem de banco. Categoria vazia indexada é página fina que derruba o resto.

16.6 **Ordem das levas (seção 9) dentro da árvore:** primeiro a mãe e suas 3 primeiras filhas de maior intenção de compra, depois as irmãs, depois a próxima categoria. Nunca uma filha de cada categoria espalhada — cluster ralo não passa autoridade.

16.7 **Entre ilhas não há link** (decisão de 09/09/2026): cada ilha é um silo próprio; a autoridade cresce dentro do domínio.

16.8 **Transição das ilhas vivas.** Aquametria, Robometria e Clube do Mosaico: no bloco de reescrita da home e do header (seção 15.5), a Fundação também (i) define a árvore da ilha em `ilhas/<ilha>/ARVORE.md` (níveis 1 e 2 com slugs, e a lista das páginas existentes com o pai de cada uma); (ii) muda o pai e o slug das páginas existentes SOMENTE se ainda não estiverem posicionadas (seção 12.1: página com impressão registrada não troca URL — recebe breadcrumb e links no lugar onde está, e o pai passa a apontar para ela); (iii) publica breadcrumb e blocos "Veja também" em tudo; (iv) toda URL que mudar recebe 301 da antiga e o sitemap é reenviado.

## 17. PAUTA DAS ILHAS — os guias são o terceiro nível da malha, não um blog (11/09/2026)

Decisão do Raphael em 11/09/2026: as ilhas passam a ter artigos escritos pela fábrica, com descoberta automática de tema, para ranquear e fortalecer os clusters (seção 16). Não é um blog em feed: é o nível `/guias/` (ou `/como-fazer/`, conforme o `VOZ.md`) da árvore, e cada artigo nasce com mãe, consulta-alvo e destino comercial dentro do site.

17.1 **Quem faz o quê.** A rotina **Pauta das ilhas** (terças, no computador do Raphael, como as Sentinelas) descobre e ranqueia temas e grava `ilhas/<ilha>/pauta.md` pelas mãos. A **Fundação** escreve os artigos na nuvem, dentro da rampa (seção 9: leva de 5 a 10, medir, só dobrar se indexou E apareceu). A **Sentinela** verifica tom (15.4), cluster (16.4) e posição (12.1) como em qualquer página.

17.2 **Portão de tema — os quatro têm que passar:** (a) consulta paramétrica ou de "como fazer" que uma pessoa digita, com as palavras dela; (b) SERP aberta pela régua da seção 14 (fórum, vídeo, blog velho, resposta sem número = entra; fazenda + marketplace + fabricante forte no top 10 = "quando houver autoridade"); (c) destino comercial: o artigo empurra uma ferramenta ou um produto do banco da mesma categoria — tema sem destino não entra, por mais volume que tenha; (d) mãe definida na árvore da ilha. Tema que passa nos quatro ganha nota = intenção de compra × abertura da SERP; a pauta é ordenada por essa nota.

17.3 **Formato de `ilhas/<ilha>/pauta.md`** (a rotina substitui o arquivo inteiro a cada semana; temas já escritos saem; temas recusados pela Fundação ficam em "recusados" com o motivo):
- cabeçalho: `data`, `ilha`, `fontes consultadas` (autocomplete, "as pessoas também perguntam", buscas relacionadas, Trends, corpus da ilha)
- tabela de até 10 temas: `#` · `consulta-alvo` · `variações` (2–4) · `mãe` (URL de nível 2) · `destino` (ferramenta ou produto) · `top 10 hoje` (quem ocupa, em 1 linha) · `nota` · `ângulo` (a resposta em uma frase, na voz da ilha)
- `recusados`: consulta e motivo (SERP fechada / sem destino / já coberto por página X)
Na Aquametria a descoberta parte do corpus do bloco 1 (`aquametria-corpus-buscas`, 480 consultas em 15 clusters): a rotina confirma SERP e destino, não redescobre.

17.4 **O artigo.** Na voz do `VOZ.md`; título = a consulta ou a resposta dela; a resposta com número na primeira dobra; a prova (fonte, data) na camada de prova (15.2); link para o destino comercial no corpo com o bloco de compra da seção 7 quando for produto; breadcrumb, link para a mãe e "Veja também" com 2–4 irmãs (16.4); JSON-LD `Article` + `BreadcrumbList` (+ `FAQPage` só se houver perguntas reais respondidas). Tamanho: o que a resposta pede — 400 palavras que respondem valem mais que 1.500 que enrolam. Sem data no slug; `dateModified` atualizado quando o dado mudar.

17.5 **Ritmo.** Entra na fila da ilha DEPOIS da reescrita de home/header (15.5) e da árvore (16.8), e a leva de guias respeita a rampa e a ordem por cluster (16.6): os guias de uma categoria saem juntos, apontando para a mesma mãe e a mesma ferramenta. A ilha reporta em todo bloco quantos temas da pauta estão escritos, na fila e recusados.

17.6 **O que a Pauta nunca faz:** não escreve o artigo (é da Fundação), não inventa volume ("faixa" ou "não medido" é resposta válida), não pauta tema YMYL, não pauta notícia ou tendência sem destino comercial, não repete consulta que já tem página na ilha (nesse caso registra "já coberto" e, se a página estiver mal posicionada, despacha para a Sentinela).

## 18. CORREÇÃO FURA A FILA E SAI INTEIRA (11/09/2026)

Decisão do Raphael em 11/09/2026, depois de uma correção de cabeçalho esperar três execuções: "está demorando muito essas passadas pras correções do site". A fábrica constrói rápido e conserta devagar — e é o contrário que ele precisa, porque defeito no ar custa mais caro que bloco não construído.

18.1 **Prioridade de ilha (substitui a rotação da seção 1 quando houver conflito).** Ao escolher a ilha da execução, a ordem é: (1ª) ilha com **DESPACHO aberto** no topo do `PROMPT.md` — despacho do Raphael antes de despacho da Sentinela; entre dois despachos do Raphael, o mais antigo; (2ª) ilha com defeito aberto registrado pela ronda; (3ª) a rotação normal da seção 1 (a de `ultima_execucao` mais antiga). A reserva por commit continua igual: quem perde a corrida escolhe a próxima da ordem.

18.2 **Despacho sai INTEIRO, não um item por execução.** Um despacho pode ter vários itens; a execução resolve **todos os itens do despacho** e só então fecha — não vale pegar um item e deixar o resto para a próxima passada. Correção não é bloco de construção e não consome a vez de um: se sobrar fôlego na execução depois de fechar o despacho, ela segue para o próximo bloco da fila normalmente.

18.3 **Teto de honestidade.** Se um item do despacho for grande demais para caber na execução, a execução resolve os que couber, **reescreve o despacho deixando SÓ os itens que faltam** (com o motivo em uma linha) e fecha. Despacho pela metade sem essa reescrita é proibido: o próximo trabalhador não tem como saber o que já foi feito.

18.4 **O despacho morre quando é verificado, não quando é escrito.** Só apague o despacho do `PROMPT.md` depois de abrir a URL no ar e conferir o critério de pronto que ele mesmo declara. Se a verificação falhar, o despacho fica, com a linha "tentativa em <data>: <o que falhou>".

18.5 **Verificação antes de construção, sempre.** Na dúvida entre fechar um despacho e começar um bloco novo, fecha o despacho. Ilha com defeito no ar não recebe página nova.

## 19. A SENTINELA CONSERTA O MECÂNICO NA MESMA PASSADA (11/09/2026)

Pergunta do Raphael em 11/09/2026: "por que que ela pega o erro e ela mesma não conserta? Tem que ficar esperando a burocracia de mandar pro despachante?". Ele está certo para uma parte dos defeitos e a regra muda aqui. O que NÃO muda é o motivo pelo qual a Sentinela existe: a Fundação reportou sucesso três vezes seguidas com as calculadoras quebradas porque conferia o próprio encanamento. **Quem constrói não aprova o que construiu.** A separação passa a ser pela NATUREZA DO DEFEITO, não pelo cargo.

19.1 **A Sentinela CONSERTA na mesma passada, sem despacho** (lista fechada — na dúvida, é despacho): texto de título, meta description, primeiro parágrafo ou rótulo, inclusive palavra da lista "Proibidas" do `VOZ.md`; acento, erro de digitação, número que não bate com a fonte já citada na própria página; link interno quebrado ou faltando; breadcrumb ausente; item de "Veja também" faltando; `noindex` indevido; `alt` de imagem; sitemap não enviado ou não acionado; Sync não disparado; `dateModified` desatualizado. São defeitos cujo critério de pronto é objetivo e foi definido ANTES do conserto, por quem achou o defeito.

19.2 **A Sentinela NÃO conserta, despacha** (também lista fechada, e ela vale mais que a de cima): qualquer código de snippet ou lógica de ferramenta; fórmula, faixa ou dado técnico do banco; estrutura de URL, pai ou molde de casca; qualquer coisa que exija ESCOLHER entre duas opções defensáveis; qualquer página que já tenha impressão registrada e cuja correção mude URL (seção 12.1); e tudo o que ela não souber consertar em uma tentativa. Sintoma não é causa: quem vê o sintoma costuma errar a causa, e é por isso que conserto de projeto continua sendo da Fundação.

19.3 **Como ela conserta.** O site é gerado do repositório: conserto que não passa pelo repositório é desfeito no Sync seguinte. Então ela escreve o arquivo corrigido **pelas mãos** (`trig_01Jg2qeDDsWDJdU9khHVswqd`, o mesmo canal do despacho), aciona o Sync da ilha por curl, **reabre a URL e confere** o critério de pronto. Só então registra. Nunca conserta pelo wp-admin.

19.4 **As três travas que substituem a espera pela Fundação.**
(a) **Conferir depois de consertar, sempre** — reabrir a URL, no ar, e checar o critério objetivo. Falhou, vira despacho com a linha "tentei consertar em <data>, falhou: <o quê>".
(b) **Segunda vez vira despacho** — se o MESMO defeito voltar na mesma página, a Sentinela para de consertar e despacha. Defeito que volta não é defeito, é sintoma de causa que ela não enxerga.
(c) **A ronda seguinte reconfere o que a anterior consertou** — a verificação independente continua existindo; ela passou a ser separada no TEMPO, não em pessoa. Todo conserto entra em `dados/consertos.md` da ilha (data, URL, o que mudou, quem conferiu) e a ronda seguinte abre essa lista antes de qualquer outra coisa.

19.5 **Teto por passada:** no máximo 5 consertos por ronda e por ilha. Passou de 5, os demais viram um despacho único — volume alto de defeito mecânico é problema da casca, não de página, e isso é da Fundação.

19.6 **A Fundação não reverte conserto de Sentinela** sem registrar o motivo no `REGISTRO.md` da ilha. Se ela achar que o conserto está errado, escreve por quê — duas camadas discordando no silêncio é como defeito volta a ficar horas no ar.

## 20. ILHA NOVA ENTRA NA LISTA DE REDE NO DIA DO DOMÍNIO (11/09/2026)

> **CORREÇÃO MEDIDA, 11/09/2026 17h50Z, pela execução seguinte à que escreveu esta seção.** A causa nomeada abaixo estava ERRADA: `clubedomosaico.com.br` **está** na lista de rede. O primeiro `curl` daquela execução também devolveu `000` — e o **mesmo comando, repetido minutos depois, devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o sitemap; as três revisões presas desembarcaram na hora. Era intermitência do túnel lida como bloqueio, e o diagnóstico se propagou porque cada execução leu o `ESTADO.md` da anterior como fato. O passo 20.1 continua valendo (é prevenção barata e certa); o 20.2 foi corrigido, porque do jeito que estava escrito ele teria parado a ilha por uma falha que não existia. Ver a regra de reconferência na seção 4.

Escrito em 11/09/2026 depois de três execuções seguidas travadas em silêncio: a Fundação escrevia no repositório normalmente, mas recebia `000`/403 ao tentar acionar o Sync e ao tentar abrir a URL para verificar. O trabalho ia para o `main` e não chegava ao site; três revisões ficaram presas sem ninguém perceber, porque o commit dava a impressão de que estava tudo entregue. **Essa metade — commit sem Sync não é entrega — segue verdadeira e é o que esta seção existe para impedir.**

20.1 **Passo obrigatório no nascimento da ilha (seção 11), no MESMO dia em que o domínio é comprado:** acrescentar `<ilha>.com.br` e `*.<ilha>.com.br` à lista "Domínios permitidos" dos ambientes de nuvem (`claude.ai/code` → seletor de ambiente → Nuvem → engrenagem). Enquanto isso não estiver feito, a ilha não recebe bloco: casca no ar que não pode ser verificada é pior que casca inexistente.

20.2 **Conferência barata que a Fundação faz antes de trabalhar numa ilha:** um `curl -s -o /dev/null -w '%{http_code}' https://<ilha>.com.br/` no começo da execução. **Se der 000 ou 403 de proxy, repita — e repita o Sync e o `/status` também — antes de chamar de bloqueio** (seção 4: falha de rede só vira bloqueio depois de repetir). Uma falha isolada é o túnel; três seguidas, em endereços diferentes, é rede. Confirmado o bloqueio, registre no `ESTADO.md` o campo `rede: bloqueada em <data>`, escreva no relatório e não construa às cegas — mas **bloqueio herdado do `ESTADO.md` é retestado antes de ser respeitado**, nunca lido como fato. Commit sem Sync e sem verificação no ar não é entrega (seções 8 e 18.4).

20.3 **A mesma armadilha vale para toda fonte nova** que uma ilha precise alcançar (domínio de fabricante, API, marketplace): quem escreve a regra que exige a fonte é quem confere se a fonte está liberada.

## 21. O PISO DA RAMPA — antes de 40 páginas e 21 dias, zero impressão não é sinal (11/09/2026)

Decisão do Raphael em 11/09/2026, depois de eu apontar o risco: a Aquametria tinha 8 dias de vida, 13 URLs, 7 indexadas e **zero impressões**. A regra da rampa (seção 9) diz para só dobrar a leva se a anterior **indexou E apareceu**. Lida ao pé da letra num site de uma semana, essa regra congela a ilha em 13 páginas esperando um sinal que só existiria com mais páginas e mais tempo. É uma regra boa para site maduro e ruim para site recém-nascido.

21.1 **O piso.** Uma ilha está ABAIXO DO PISO enquanto não tiver, ao mesmo tempo, **40 URLs publicadas** e **21 dias desde a primeira URL indexada**. Abaixo do piso, "zero impressão" **não é informação** e **nunca** trava, adia ou reduz leva nenhuma: a Fundação publica levas seguidas de 5 a 10 URLs, no ritmo normal da fila, sem esperar medição.

21.2 **Acima do piso, a seção 9 volta inteira**: mede, e só dobra a leva se a anterior indexou e apareceu. Aí sim "indexou e não apareceu" significa palavra-chave errada, e publicar mais do mesmo piora.

21.3 **O piso afrouxa a LEITURA DO SINAL, nunca a qualidade.** Continuam valendo, abaixo e acima do piso, sem exceção: o portão de dado da seção 13 (3 itens reais + 1 número por página), a classificação da SERP antes de criar a página (seção 14), a verificação da URL no ar com número medido (seção 8), a voz (15), a árvore e o cluster (16). Página ruim não entra mais rápido por causa do piso — o piso só decide QUANDO parar de publicar para medir.

21.4 **Teto para não virar fazenda:** no máximo 10 URLs por leva e **no máximo 3 levas por semana por ilha**. Domínio novo que despeja centenas de páginas numa semana é padrão de fazenda e o Google trata como tal. O piso é para sair de 13 páginas, não para chegar a 400.

21.5 **O que acontece AO ATINGIR o piso.** Se, com 40 URLs e 21 dias, a ilha continuar com **zero impressões**, isso passa a ser sinal forte e a resposta NÃO é publicar mais. A leitura semanal (seção 12) abre um diagnóstico com três hipóteses, nesta ordem, e escreve qual delas o dado sustenta: (a) **indexação** — as URLs estão no índice? (URL Inspection); (b) **consulta** — as páginas miram consultas que alguém digita, ou só variações que ninguém busca? (c) **SERP** — a classificação da seção 14 estava errada e o top 10 é mais fechado do que se mediu. Enquanto o diagnóstico não sair, a ilha não recebe leva nova de malha; ferramenta e guia continuam.

21.6 **Registrar o piso.** O cabeçalho do `ESTADO.md` de cada ilha ganha `piso: abaixo|atingido` e `primeira_indexacao: <data ou null>`, preenchidos pela leitura semanal. A Fundação lê esse campo antes de decidir o tamanho da leva — não recalcula de cabeça.

## 22. O DESENHO SERVE À MALHA — beleza e ranqueamento no mesmo lado da mesa (12/09/2026)

Escrita a pedido do Raphael em 12/09/2026, com a frase dele: *"o objetivo principal é ranqueamento no Google, toda a estratégia de malha de links e arquitetura voltadas ao SEO do projeto; design sempre será secundário, mas o plano perfeito é casar os dois em harmonia."* Esta seção existe para que o casamento seja possível **sem** que a ilha tenha de escolher — e para que, no dia em que houver escolha, ela já esteja feita.

### 22.1 A ordem nunca inverte
Ranqueamento primeiro, conversão depois, beleza por último. As três quase sempre andam juntas: página rápida, legível e organizada ranqueia melhor, vende melhor e é mais bonita. **Quando não andarem** — quando um desenho bonito custar uma posição, um link ou um dado — **o desenho cede, e o motivo vai para o `REGISTRO.md`.** Nunca o contrário, e nunca em silêncio.

### 22.2 O que o desenho NUNCA toca
Estes são estruturais e pertencem às seções 9, 14, 15 e 16. Nenhum despacho de desenho mexe neles:
- URL, árvore, nível e breadcrumb (seção 16) — nem por estética, nem por "ficou mais limpo".
- Links internos da malha e o **texto âncora** deles: âncora é consulta, não é rótulo de botão bonito.
- `<title>`, meta descrição, H1 e a ordem **resposta antes da explicação**.
- JSON-LD e o bloco de prova ("como sabemos", tabela, fonte, data).
- A camada de voz (seção 15): o `DESIGN.md` manda na forma, o `VOZ.md` manda na palavra. Quando os dois discordarem, é o `VOZ.md` que decide, porque é ele que fala com a pessoa.

### 22.3 HTML servido — a regra que mais protege o ranqueamento
**Tudo que precisa ranquear sai pronto do servidor, no primeiro HTML.** Nada de conteúdo injetado por JavaScript depois que a página abre.
- Link é sempre `<a href="…">` de verdade. Nunca `div` com `onclick`, nunca botão que navega por script, nunca `href="#"` com JS por trás. Um link que só existe depois do JS **não é link da malha** — e a malha é o motor da ilha inteira.
- "Ver mais", paginação, abas e acordeões: o conteúdo já está no HTML; o script só mostra e esconde. Acordeão fechado com o texto presente está certo; acordeão que busca o texto ao abrir está errado.
- Vitrine, tabela de produto, resultado de ferramenta com valores padrão, breadcrumb e rodapé: todos pré-renderizados.
- O JavaScript da ilha serve só interação: calcular quando a pessoa digita, abrir menu, trocar aba. **Zero framework na página pública.**

### 22.4 Orçamento de desempenho (é parte do desenho, não detalhe de programador)
- No máximo **duas famílias de texto + uma monoespaçada**, as que o `DESIGN.md` da ilha nomeia, sempre com `font-display: swap`. Fonte nova exige mudar o `DESIGN.md`.
- **Toda imagem com `width` e `height` no HTML** — é o que impede o salto de layout. Imagem abaixo da dobra com `loading="lazy"`; a imagem do LCP **nunca** é lazy e leva `fetchpriority="high"`.
- **Nada de carrossel automático acima da dobra.** Carrossel de vitrine é permitido abaixo do resultado, sem autoplay.
- CSS crítico embutido, o resto pode esperar. Sem biblioteca de ícone: ícone é SVG embutido.
- O LCP da página é **texto ou a foto principal** — nunca um bloco que só aparece depois de um script.

### 22.5 Onde o desenho tem liberdade inteira
Cor, tipografia, escala, espaçamento, foto, ilustração, moldura, microcópia dos botões, o molde de casca (LOJA / FERRAMENTA / GUIA, seção 15.3) e o desenho de cada componente. É bastante: é aí que mora a diferença entre três ilhas com a mesma cara e três ilhas com três personalidades.

### 22.6 `ilhas/<ilha>/DESIGN.md` passa a ser o dono dos tokens
Cada ilha tem um `DESIGN.md` com paleta, escala tipográfica, espaçamento, raio, sombra e a especificação dos componentes. A casca renderiza a partir dele.
- O `PROMPT.md` **deixa de ser dono da paleta**: onde ele hoje lista cor e fonte, passa a apontar para o `DESIGN.md`.
- **Token novo não nasce em despacho.** Cor, fonte ou medida que não está no `DESIGN.md` é defeito, não identidade — foi essa regra que barrou, no Clube do Mosaico em 11/09, um segundo branco a quatro passos do branco aprovado.
- Mudar token é mudar o `DESIGN.md` primeiro, num commit só, com o motivo.

### 22.7 A Sentinela confere o desenho na mesma ronda
Entram na lista mecânica da seção 19.1, que ela conserta na hora:
- imagem sem `width`/`height`;
- link interno que não é `<a href>`;
- texto que só aparece com JS ligado;
- cor ou fonte fora do `DESIGN.md` da ilha;
- imagem acima da dobra marcada como `lazy`.
O que ela **despacha** em vez de consertar (19.2): trocar molde de casca, mudar escala tipográfica, qualquer coisa que mexa em mais de uma página de uma vez.

### 22.8 O portão: a página tem de funcionar com o JavaScript desligado
Cada ilha ganha `ferramentas/teste-desenho.mjs`. Ele abre as páginas **com JavaScript desligado** e reprova se faltar qualquer um: `<title>`, H1, primeiro parágrafo, breadcrumb, os links internos da malha, o bloco de prova e o bloco de compra. Uma ferramenta pode perder o resultado calculado sem JS — e só ele. Página que fica em branco sem JS não publica.

## 23. O PAINEL — um instantâneo só, reescrito por quem já olhou (12/09/2026)

O Raphael não deve ter de caçar o estado do Arquipélago dentro de conversa, de boletim ou de `ESTADO.md` de três ilhas. Existe **um** arquivo com o instantâneo: `dados/PAINEL.md`.

### 23.1 Quem escreve
A **Sentinela**, ao fim de toda ronda diária, como último passo, pelo mesmo canal das mãos (seção 19.3). Ela já abriu as ilhas e já leu os estados — reescrever o painel custa quase nada e é a única forma de ele nunca estar velho. **Ninguém mais escreve nesse arquivo.** A Fundação não escreve, o boletim não escreve.

### 23.2 O que tem dentro, nesta ordem e só isto
1. A data e a hora da ronda que o escreveu.
2. Uma linha por ilha: `estado`, `prioridade`, `urls_publicadas / 40`, dias desde `primeira_indexacao` de 21, `ultima_execucao`, `ultima_ronda`, `piso`, e `congelamento` quando houver.
3. **Despachos abertos**, um por linha: ilha, onde, o que é, há quantos dias está aberto.
4. **Precisa do Raphael**: só o que depende mesmo dele — link de afiliado a gerar, dado que só ele tem, decisão que não é de máquina. Nada que a máquina possa fazer sozinha entra nesta lista.
5. **Consertos das últimas 24 h**, da lista mecânica da 19.1.

### 23.3 O que NÃO tem dentro
Narrativa, histórico, opinião, projeção e elogio. O painel é instantâneo; a leitura é do boletim de sexta, e o histórico é do `REGISTRO.md`. Se uma linha do painel só faz sentido com um parágrafo de explicação, ela não é do painel.

### 23.4 Número sem procedência não entra
Vale aqui a regra de sempre: todo número do painel sai de arquivo do repositório ou de medição da própria ronda. Quando um campo não foi medido nesta ronda, o painel escreve `não medido hoje` — nunca repete o número velho com cara de novo.

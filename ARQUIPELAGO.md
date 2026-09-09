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
- **PROIBIDO em toda ilha:** contagem regressiva, escassez inventada, selo de "mais vendido", avaliação que a ilha não mediu. A confiança é o único ativo que separa o Arquipélago das fazendas de conteúdo.
- **Sub_id** para rastrear venda: Sub_id 1 = nome da ilha, Sub_id 2 = código da ferramenta de origem.
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
- **Um bloco por execução.** Você roda de novo em poucas horas. Bloco bem-feito e registrado vale mais que três pela metade.
- **A identidade visual da ilha é parte do nascimento, não do acabamento** — paleta, tipografia e símbolo entram no `PROMPT.md` da ilha antes do primeiro bloco de casca. O símbolo vem do **gesto técnico** do nicho, nunca do objeto desenhado.
- O Raphael **não aparece** em ilha nenhuma: sem rosto, sem vídeo, sem fórum, sem tráfego pago, sem link pago. A autoridade vem de metodologia, procedência e do widget instalado em lojas.
- Não faça perguntas: você roda sozinho, sem ninguém acompanhando. Só sinalize ao Raphael se estiver bloqueado ou se concluiu um bloco grande.

---

## 11. NASCIMENTO DA ILHA — checklist de infraestrutura, de fábrica

Ordem obrigatória. Ilha nova segue isto inteiro antes de existir site.

1. **[RAPHAEL]** Registrar e pagar o domínio no registro.br. É o único gasto e o único passo que exige CPF e cartão. Nenhuma camada faz isso.
2. **Domínio adicional na hospedagem ANTES do DNS.** cPanel da HostGator → Domínios → Create A New Domain, com **raiz própria** (`/home3/<usuário>/<dominio>`), NUNCA compartilhando raiz com outra ilha. Isso cria a zona no servidor.
3. **Só então** apontar os nameservers no registro.br (`ns604` e `ns605.hostgator.com.br`). **Invertendo a ordem o registro.br recusa** ("Pesquisa recusada"), porque valida se os nameservers já respondem pelo domínio. A Aquametria pagou esse erro em 06/09/2026 e a Robometria acertou em 09/09 seguindo esta ordem.
4. Esperar a propagação — na Aquametria demorou ~2h. Enquanto isso, trabalhe os blocos de pesquisa da ilha, que não dependem de site. Não marque `bloqueada_por` por causa de propagação.
5. WordPress pelo Softaculous, em **português do Brasil**, instalação limpa — **desmarque todos os plugins sugeridos**.
6. cPanel → SSL/TLS Status → **Executar AutoSSL** no domínio novo.
7. No wp-admin: instalar e ativar o **Code Snippets**; remover Akismet e Hello Dolly; instalar **Site Kit by Google**, **Converter for Media** e **Limit Login Attempts Reloaded**. **Sem plugin de cache** (a HostGator já tem mu-plugin) e **sem plugin de SEO**.
8. Snippet **"<Ilha> Sync"**, copiado do Sync da ilha anterior com as constantes trocadas: nome da ilha, caminho `ilhas/<ilha>/` e **token novo**, gerado na hora. Anote o endpoint do Sync e o do `/status` no `PROMPT.md` da ilha — sem eles a seção 4 não é executável.
9. **MEDIÇÃO — o passo que ninguém pode pular.** Verificar o domínio no **Search Console** (pelo Site Kit, no navegador do Raphael), **submeter o sitemap**, e gravar a primeira medição em `dados/indexacao.md`: URLs indexadas, em "descoberta — não indexada", em "rastreada — não indexada", excluídas e por quê. Esse arquivo é **série histórica** — cada medição vira uma seção nova, nunca sobrescreve a anterior.
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

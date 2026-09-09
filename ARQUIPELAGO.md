# CONTRATO DO ARQUIPÉLAGO

Regras que valem para TODA ilha. Quem executa um bloco lê este arquivo primeiro e depois o `PROMPT.md` da ilha sorteada. Regra nova do Arquipélago se escreve AQUI, uma vez — nunca copiada para dentro dos prompts das ilhas.

Vocabulário: cada site de nicho é uma **ilha**, o conjunto é o **arquipélago**, o portão de publicação é o **desembarque**. Camadas: **BÚSSOLA** (decide o nicho) → **FUNDAÇÃO** (constrói) → **SENTINELA** (cuida da ilha viva).

---

## 1. O DESPACHANTE — como a ilha do dia é escolhida

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
bloqueada_por: null       # texto curto quando depende de algo humano; null quando não
---
```

Regras do cabeçalho:
- `bloqueada_por` só existe para dependência **humana ou externa** (domínio não propagou, senha que só o Raphael tem). Falta de dado que você mesmo pode colher NÃO é bloqueio — é trabalho.
- Ao desbloquear, apague o texto e volte para `null` na mesma execução.
- `ultima_execucao` é gravada mesmo quando o bloco falha; senão a mesma ilha é escolhida para sempre.
- Abaixo do cabeçalho, o `ESTADO.md` continua sendo prosa livre: credenciais **não**, estado do projeto **sim**.

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

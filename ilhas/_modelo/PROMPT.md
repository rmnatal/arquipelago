# ILHA: <NOME> — <nicho em três palavras>

Modelo de ilha nova. Copie esta pasta para `ilhas/<nome>/`, preencha tudo entre `< >` e apague esta linha. Enquanto houver um `< >` sem preencher, a ilha nasce com `estado: nascendo` e `prioridade: 3` no `ESTADO.md`.

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá** — regra comum se corrige em um lugar só.

## Identidade
- Nicho: `<o eixo paramétrico, não a categoria comercial>`
- Domínio: `<dominio.com.br>`, registrado em `<data>`. Ilha nº `<n>` do Arquipélago.
- Paleta, 7 valores e nada além: tinta `<#>` · marca `<#>` (**cor de sinal**: um uso por tela) · papel `<#>` · superfície `<#>` · traço `<#>` · legenda `<#>` · alerta `<#>`.
- Tipografia: `<display>` (títulos) · `<texto>` (corpo) · uma monoespaçada para todo número, unidade e código, com `tabular-nums`.
- Símbolo: **vem do gesto técnico do nicho, nunca do objeto desenhado.** A Aquametria mede, então o símbolo é um recipiente graduado; a Robometria encaixa, então o símbolo é um encaixe. Descreva-o aqui em geometria, para que qualquer execução redesenhe igual.
- A identidade é entregue ao Raphael como artefato e **aprovada por ele antes do bloco 3b**.

## O buraco que esta ilha existe para ocupar
`<o que a Bússola verificou: onde a SERP está tomada por fazendas, e qual busca paramétrica está órfã. É o eixo, e ele decide o que NÃO atacar de frente.>`

## Memória a carregar
`/areas/projeto-<nome>.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada que aprovou o nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

## Endpoints desta ilha
- Sync: `<preencher quando o WordPress existir>`
- Status: `<preencher quando o WordPress existir>`

---

## FILA DE BLOCOS

A fila padrão de nascimento. Corte, funda ou reordene conforme o nicho, mas **não pule a ordem**: dado antes de ferramenta, ferramenta antes de artigo, artigo antes de malha.

**1. LEVANTAMENTO DE BUSCAS PARAMÉTRICAS.** Consultas reais do nicho no Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta a consulta. Grave em `dados/corpus-buscas.md`. Não depende de site nem de domínio — **é sempre o primeiro bloco, mesmo sem infraestrutura.**

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json` (cada constante com fonte, data e status). Saída é sempre faixa com critério e fonte.

**3. MODELO DO BANCO.** Entidades do nicho, com o campo `imagem` desde já.

**3b. CASCA DO SITE** — só depois que o WordPress existir. Seção 6 do `ARQUIPELAGO.md`, com a paleta e o símbolo desta ilha.

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase.

**4e. VITRINE DE PRODUTO** dentro do resultado, desde a primeira ferramenta.

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**5b. MALHA DE PÁGINAS**, em levas pequenas guiadas por indexação.

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras do nicho com site próprio, `publicar: false`.

## Específico desta ilha
`<o que só vale aqui: qual dado é o produto da ilha e por que errar nele é fatal; qual programa de afiliado serve; o que fazer enquanto falta infraestrutura.>`

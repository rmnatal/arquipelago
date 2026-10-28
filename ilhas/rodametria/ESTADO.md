---
ilha: rodametria
estado: nascendo
prioridade: 1
piso: abaixo
primeira_indexacao: null
ultima_execucao: 2026-10-28T10:25Z   # BLOCO 1 ENTREGUE: `dados/corpus-buscas.md`, o corpus de buscas com procedencia consulta a consulta, e a S_par que o dossie deixou sem medir. No caminho, DUAS medicoes que nao eram do bloco: o WordPress JA esta no ar (a secao 4 em acao) e a fonte oficial da F1 e NEGADA pelo egresso. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-10-28T13:19Z   # reserva desta execucao (passo 5 da secao 1), ilha em foco pela 1.2. Rede reconferida pela 20.2 antes de reservar: raiz e wp-sitemap.xml em 200 nas TRES tentativas. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
bloco_atual: "2"   # o 1 fechou em 28/10. O 2 (especificacao F1/F2/F3 + constantes.json) pode ser ESCRITO inteiro daqui, mas a constante central da F1 nasce `publicavel: false`: ver a secao 4 do corpus e o despacho ALTA de 28/10 em dados/despachos.md
ultima_ronda: null
bloqueada_por: null
rede: ok em 2026-10-28   # `https://rodametria.com.br/` devolveu 200 em TRES tentativas as 10h17Z. O passo 20.1 esta cumprido de fato: o dominio passa pelo egresso desta nuvem. O que NAO passa e o gov.br (despacho ALTA de 28/10)
---

# Estado da ilha RODAMETRIA

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: **`rodametria.com.br` — REGISTRADO E PAGO pelo Raphael em 27/10/2026** (RDAP oficial lido no Chrome dele às 16h41 de Brasília: `status: active`, registro 27/10/2026 19:31Z, expira em 27/10/2028, nameservers ainda `a.auto.dns.br` / `b.auto.dns.br`). Passo 1 da seção 11 cumprido.
- Hospedagem: domínio adicional no mesmo plano da HostGator, raiz própria. **FEITO** — o domínio serve HTML próprio.
- Nameservers `ns604` / `ns605.hostgator.com.br`: **FEITO** — o DNS delegou e o domínio resolve.
- Search Console (propriedade de Domínio): **não medido daqui** (é navegador do Raphael).
- WordPress: **NO AR desde 27/10/2026 às 22h17Z**, medido em 28/10 às 10h17Z pela execução do bloco 1 —
  `https://rodametria.com.br/` devolve 200, `<title>Rodametria - Mobilidade elétrica</title>`, tema de blocos cru,
  **nenhuma página publicada**, `/wp-sitemap.xml` sem URL nenhuma. `/nao-existe-xyz/` devolve 404 de verdade, então
  a porta de entrada da seção 29 está sã nesta primeira leitura.
- Snippet de Sync: `Rodametria Sync`, token novo na hora. **Pendente** — `/wp-json/rodametria/v1/status` devolve 404.
- Lista de Domínios permitidos (seção 20): **FEITO para o domínio da ilha** — o egresso desta nuvem alcança
  `rodametria.com.br`. **Falta `gov.br`**, que é a fonte da F1: despacho ALTA de 28/10 em `dados/despachos.md`.

## O que já foi entregue
- Dossiê, ficha, identidade aprovada (símbolo V9, assinatura H1), `DESIGN.md`, `VOZ.md` e `logo.svg` — 27/10/2026, pela Bússola. Nenhuma URL publicada.
- **BLOCO 1 — `dados/corpus-buscas.md`**, 28/10/2026: quatro eixos, 19 consultas com procedência medida consulta a
  consulta, a **S_par medida** (era a primeira tarefa de leitura que o dossiê deixou) e a contagem do vazamento da
  busca da nuvem **por eixo** (zero fora do Brasil no eixo da regra; quase total no de autonomia e no de peças).
  Nenhuma URL publicada — bloco de dado, `publicar: false`.

## O que está travando
- **A fonte oficial da F1.** O texto da Resolução Contran nº 996/2023 no `gov.br` é **negado pelo egresso desta
  nuvem** (`connect_rejected`, e `ENOTFOUND www.gov.br` na busca de página), medido em 28/10 às 10h4xZ. O bloco 2
  pode ser escrito inteiro, mas a constante central nasce `publicavel: false`. Despacho **ALTA** de 28/10 em
  `dados/despachos.md`. **Isto NÃO é `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.
- **A SERP dos eixos de autonomia, carga e peças**, que a busca da nuvem não vê (30.8) — despacho NORMAL de 28/10.
- Os passos 4b a 9 da seção 11 que faltam (Search Console, snippet de Sync, plugins, conta de serviço) são trabalho
  de navegador do Raphael. **O WordPress e o DNS já saíram dessa lista** — ver a Infraestrutura acima.
- Os blocos 2 e 3 não dependem de site, e o 2 é o próximo.

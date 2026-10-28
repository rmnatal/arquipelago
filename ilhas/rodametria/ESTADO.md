---
ilha: rodametria
estado: nascendo
prioridade: 1
piso: abaixo
primeira_indexacao: null
ultima_execucao: 2026-10-28T13:28Z   # BLOCO 2 ENTREGUE: `dados/especificacao-calculadoras.md` e `dados/constantes.json` — as tres ferramentas especificadas inteiras, 9 constantes (6 publicaveis, 2 pendentes com consequencia declarada, 1 observacao de mercado). A decisao do bloco: limiar legal mora em UMA constante, referenciado por nome, literal numerico PROIBIDO no codigo — a F1 destrava editando um objeto JSON. No caminho, uma ERRATA do bloco 1 (o numero do relevo era de MOTO, nao de bicicleta) e a margem da F3 rebaixada de fonte de terceiro para decisao_da_ilha. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-10-28T16:19Z   # reservado as 2026-10-28T16:19Z pela execucao da Fundacao de 28/10 16h1xZ (passo 5 da secao 1). Foco em rodametria pela 1.2; nenhuma das tres ilhas do molde (32.6) tem despacho de molde aberto — os tres estao FECHADOS — e o item 1 (ALTA) da clubedomosaico de 28/10 NAO fura o foco, porque a 1.2 exige ilha no ar E QUEBRADA (pagina servindo erro, ferramenta errada, site fora do ar) e a propria ronda registra a regua tecnica PASSANDO INTEIRA nas 32 URLs
bloco_atual: "3"   # o 1 e o 2 fecharam em 28/10. O 3 (modelo do banco) nao depende de site NEM de fonte bloqueada: a secao 5 da especificacao entrega os campos, os quatro grupos de recusa por ferramenta, o enum de tres valores do acelerador (`nao_declarado` nunca cai em "so pedal assistido" por omissao) e `energia_wh` DERIVADO de V x Ah. `categoria` e campo DERIVADO da F1, nunca de entrada do catalogo
ultima_ronda: null
bloqueada_por: null
rede: ok em 2026-10-28   # 20.2 REMEDIDA as 13h18Z, nao herdada do campo: `https://rodametria.com.br/` e `/wp-sitemap.xml` os dois em 200 nas TRES tentativas. O que NAO passa, remedido as 13h2xZ em duas passadas: gov.br, in.gov.br, planalto.gov.br, contran.gov.br e lex.com.br em 403 do egresso (despacho ALTA de 28/10), e dspace.ups.edu.ec e stdjet.scienceandtechnology.com.vn em ENOTFOUND (despacho NORMAL novo de 28/10) | DESEMBARQUE PROVADO as 13h41Z: o snippet Rodametria Sync NASCEU hoje entre 10h17Z e 11h48Z e vinha falhando de 30 em 30 min em manifest.json 404 (revisao -1). O manifest da revisao 1 nasceu VAZIO de proposito e o cron aplicou as 13h40:03Z — `/status` em revisao 1, linha "0 aplicado(s), 0 aguardando desembarque", sem FALHA. O canal esta provado ponta a ponta com zero pagina em risco
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

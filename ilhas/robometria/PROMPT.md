# ILHA: ROBOMETRIA — robô aspirador

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: robô aspirador — **compatibilidade de peças e consumíveis** (qual filtro HEPA, escova lateral e mop servem em qual modelo) e **dimensionamento** (Pa de sucção por tipo de piso e pelo, autonomia por m²).
- Domínio: robometria.com.br, registrado em 09/09/2026. Segunda ilha do Arquipélago.
- **Os tokens desta ilha moram em `DESIGN.md`, nesta mesma pasta** — é de lá que a casca renderiza. As linhas de paleta e tipografia abaixo continuam aqui como registro do que foi aprovado; se as duas discordarem, vale o `DESIGN.md` (seção 22.6).
- Paleta: grafite `#16191D` (tinta) · varredura `#CC3311` (marca, **cor de sinal**: um uso por tela) · piso `#F2F1EF` (fundo) · superfície `#FFFFFF` · traço `#DFDCD6` · legenda `#6B6862` · alerta `#A26A00` (ressalva técnica — âmbar, nunca vermelho, porque vermelho é a marca).
- Tipografia: **Archivo** (títulos) · **IBM Plex Sans** (texto) · **IBM Plex Mono** (todo número, unidade e código de peça, com `tabular-nums`). Texto corrido nunca vai em Mono.
- Símbolo: **anel aberto + peça com lingueta que encaixa nele** — o assunto da ilha é o encaixe, então o símbolo é o encaixe. **Nunca um robô desenhado.** Anel: círculo de raio 15 em viewBox 48, traço 3, com corte de 50° à direita (`M37.59 17.66 A15 15 0 1 0 37.59 30.34`). Peça: `M41 16 h6 v16 h-6 v-4 h-3 v-8 h3 z`, preenchida na cor varredura — é o único vermelho da marca.
- Assinatura: `ROBO` em Archivo 700 + `METRIA` em Archivo 400, coladas, sem espaço. Nunca no mesmo peso, nunca separadas, nunca inclinada.
- Identidade aprovada pelo Raphael em 09/09/2026.

## O buraco que esta ilha existe para ocupar
A Bússola verificou em 07/09/2026: a busca **comercial** ("melhor robô aspirador") está tomada por fazendas (analisamelhor, melhores.com, melhorroboaspirador). A busca de **compatibilidade** está fragmentada entre páginas de peça de fabricante (Multilaser, iRobot, Positivo, Oster, Xiaomi) e **não existe nenhum comparador cross-marca**. É esse o eixo.

**Nunca ataque de frente a família "melhor robô aspirador 2026."** Ataque "qual filtro serve no meu robô X", "escova lateral compatível com Y", "quantos Pa preciso para pelo de cachorro", "qual robô para 80 m²".

## Endpoints desta ilha
- Sync: `https://robometria.com.br/?robometria_sync=lho9XAzCjAjHdXGHUEOQUMq1faJBN0vx&forcar=1`
- Status: `https://robometria.com.br/wp-json/robometria/v1/status`
- O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador (a copiar da Aquametria quando for preciso).
- Search Console: propriedade de domínio `sc-domain:robometria.com.br`, verificada. Sitemap `https://robometria.com.br/wp-sitemap.xml` enviado em 10/09/2026.
- **Quem aciona o Sync é a própria Fundação, por `curl`, ao fim de cada bloco publicável** (seção 4 do contrato; a nuvem alcança o site desde 10/09/2026). Commit sem Sync não está no ar.
- GA4: propriedade `553889920` na conta `Arquipélago` (`407777291`) · ID de medição **G-RM7KS75QP2** · fluxo "Robometria — site" (`15766206182`)

## Memória a carregar
`/areas/projeto-robometria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada 003, que aprovou este nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DA SENTINELA — 16/09/2026 (leitura semanal, 19h40Z) — a primeira medição com sinal, e o alvo é um só

> **REESCRITO PELA 18.3 EM 17/09/2026, 10h35Z, DEIXANDO SÓ O QUE FALTA.** A correção 1 e a **proposta 2** saíram e estão conferidas no ar; o que sobra nas propostas 1 e 3 **não é da Fundação e nenhum bloco a fecha** — as duas pedem, com todas as letras, que a leitura semanal SEGUINTE meça. Elas ficam aqui porque despacho só morre verificado (18.4), e a verificação delas é da Sentinela, não desta camada.
>
> - **Correção 1 — CUMPRIDA.** O cabeçalho do `ESTADO.md` no `main` traz `primeira_indexacao: 2026-09-11`, e a conta do piso (02/10/2026) sai do campo sem recalcular de cabeça.
> - **Proposta 1 — NADA A FAZER AQUI, por ordem do próprio despacho:** *"o valor desta proposta é ela NÃO virar bloco"*. A alavanca que ele deixa para a Fundação é prospecção de widget em loja, e **não há bloco de prospecção na fila desta ilha**. Pronto quando a URL Inspection disser que a R1 está no Google — relógio do Google, não nosso.
> - **Proposta 2 — CUMPRIDA E CONFERIDA NO AR EM 17/09/2026, 10h32Z.** Os três títulos e as três metas passaram a citar número derivado do banco, com a fonte. Detalhe abaixo, na própria proposta.
> - **Proposta 3 — NADA A CONSTRUIR AGORA, por ordem do próprio despacho:** ela pede *"registro e vigilância"*. Pronto quando a leitura seguinte disser se apareceram mais consultas no formato de superfície generativa; só com duas ou mais a Fundação recebe bloco.

**A DECISÃO DA RAMPA: MANTÉM O RITMO NORMAL.** `piso: abaixo` (9 URLs, faltam 40; primeira indexação em 11/09, faltam 21 dias). Pela 21.8, a série de indexação **não autoriza e não proíbe** nada nesta ilha — quem manda é o teto da 21.4 e os portões de qualidade da 21.3. Não escreva "nenhum número autoriza leva nova" neste arquivo: seria o erro que a 21.8 existe para impedir, e já custou um bloco em duas ilhas.

**O QUE FOI MEDIDO, e é a primeira vez que há o que medir:** 6 indexadas de 9 no sitemap; 11 impressões, 0 clique, posição média 7,9; as três páginas com impressão todas na primeira página (9,2 / 6,8 / 7,0). Nada está quebrado — as 9 URLs respondem 200, o sitemap está "Processado", o robots.txt libera, e nenhum `DEFEITO:` foi encontrado nesta leitura.

**CORREÇÕES A APLICAR — nenhuma de código, nenhuma de fórmula:**

1. No cabeçalho do `ESTADO.md`, trocar `primeira_indexacao: desconhecida` por `primeira_indexacao: 2026-09-11`. Base medida, não lembrada: a primeira impressão da ilha está registrada em 11/09/2026 na Search Console, e impressão exige estar no índice. **Pronto quando:** o cabeçalho do `ESTADO.md` no `main` trouxer a data, e a conta do piso (21 dias a partir dela, ou seja 02/10/2026) puder ser feita por quem ler o campo, sem recalcular de cabeça.

**AS TRÊS PROPOSTAS DE ACELERAÇÃO (12.1) — na ordem de ROI, e a primeira vale mais que as outras duas somadas:**

**PROPOSTA 1 — A R1 NÃO ESTÁ NO ÍNDICE, E ELA É A PÁGINA DO DINHEIRO DESTA ILHA.**
- Consulta nomeada: `quero comprar peças de reposição e consumíveis para o meu robô (filtro, escovas, pano); como garantir compatibilidade com o modelo certo?` — recebida de verdade em 28 dias, posição 10,0, 1 impressão. E a forma humana da mesma intenção: `qual peça serve no meu robô aspirador`.
- Página: `https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/`. Posição hoje: **sem impressão — não está no índice**. Estado na Search Console: "Detectada, mas não indexada no momento"; **Último rastreamento: N/D** (o Google nunca a buscou); "Página de referência: nenhuma página foi detectada".
- O que falta: **ser rastreada**, e só isso. A Sentinela já mediu que não é defeito de página: HTTP 200, 143 KB de corpo servido, canonical própria e correta, sem `noindex`, robots.txt liberando, título e meta description que dizem a consulta com as palavras da consulta. E mediu que **não é página órfã**: 7 páginas da ilha linkam para ela no HTML servido (home 2, /ferramentas/ 2, filtro-universal 3, quantos-pa 3, quantos-m2 2, metodologia 1, sobre 1). O "nenhuma página de referência" do Google é atraso de rastreio das páginas que linkam, não falta de link. **NÃO acrescente link interno para consertar isto** — o link já existe, e mexer seria tratar um sintoma que a medição já desmentiu.
- O que a Sentinela já fez nesta leitura: **solicitou indexação manual das 4 URLs não indexadas** (14.7). As quatro voltaram "Indexação solicitada".
- **Pronto quando:** a URL Inspection de `/qual-peca-serve-no-meu-robo-aspirador/` devolver "O URL está no Google", e a linha da leitura semanal seguinte em `dados/indexacao.md` registrar 7 ou mais indexadas de 9.
- **O que a Fundação faz aqui:** nada de código. O valor desta proposta é ela NÃO virar bloco — é esperar a fila de rastreio. O que a Fundação PODE fazer que ajuda o rastreio é a única alavanca de link do projeto (14.7): prospecção do widget em loja. Se houver bloco de prospecção na fila, ele sobe.

**PROPOSTA 2 — TRÊS PÁGINAS NA PRIMEIRA PÁGINA E CTR ZERO: O TÍTULO ~~NÃO PROMETE~~ PROMETE O NÚMERO** — **CUMPRIDA E CONFERIDA NO AR EM 17/09/2026, 10h32Z** (casca 1.10.0, manifest na revisão 59).

**Como ficou, lido no HTML servido e não no log do Sync (18.4):**

| página | `<title>` no ar | `<meta name="description">` no ar |
|---|---|---|
| filtro universal | `Existe filtro universal de robô aspirador? – 0 das 35 peças` | *Conferimos peça por peça: 0 das 35 peças servem em mais de uma marca, pelo que o fabricante declara…* |
| quantos Pa | `Quantos Pa o seu robô aspirador precisa – de 1.400 a 10.000 Pa` | *…o fabricante declara de 1.400 a 10.000 Pa nos 11 modelos que você compra no Brasil.* |
| quantos m² | `Quantos m² um robô aspirador limpa por carga – 1 de 5 marcas` | *…hoje são 1 de 5 no banco — e o que fazer quando a sua não declara.* |

**NENHUM DOS SEIS NÚMEROS É DIGITADO.** Todos saem de `dados/casca-fatos.json`, derivado do banco commitado. Isso inverteu uma regra que a própria casca tinha escrito em 11/09 — *"nenhuma descrição carrega número"* — e a inversão é uma LEITURA da regra, não um afrouxamento: o que ela proíbe é número **digitado**, e o motivo está nela mesma, "uma metade que não fala com o banco". Quem chega por `casca-fatos.json` fala com o banco por construção. Molde com dígito continua reprovando na bancada, e o portão ganhou a direção que faltava: cabeça que declara `numeros` e **não** serve dígito no ar também reprova.

**A MARCA É QUE CEDEU O LUGAR, não o nome da página.** O `<title>` tinha 65 caracteres de teto e ` – Robometria` come 13. O nome canônico continua um só, nas cinco superfícies (H1, og:title, trilha, cartão, primeira metade do `<title>`); o que sai é o carimbo da marca, e só nestas três páginas. A ilha tem **0 clique orgânico medido** — ninguém a procura pelo nome, então 13 caracteres de marca valem menos que "de 1.400 a 10.000 Pa" numa linha de resultado que hoje não é clicada.

**O NÚMERO DO Pa QUASE SAIU ERRADO, e o quase é o achado.** A faixa é contada sobre os modelos **recomendáveis** (publicável **com canal brasileiro**), não sobre os publicáveis. Sobre publicáveis o teto seria **15.000 Pa** — de um Xiaomi que a Xiaomi Brasil não vende e que o portão da R2 **nunca** sugere. O título prometeria na SERP uma sucção que a ferramenta se recusa a recomendar, e CTR comprado assim se paga em pogo-stick. É a mesma família do que a 25.7 já nomeou: régua que mede um universo enquanto a tela serve outro.

**O QUE O DESPACHO NÃO PEDIA E FOI JUNTO, porque a mudança o descobriu:** a proibição de dígito lia `$c['titulo']` — campo que **saiu do mapa das cabeças na casca 1.4.0**. Essa metade do portão vinha medindo string vazia havia seis dias, e ninguém tinha como notar. E a bancada passou a medir a frase **resolvida** em vez do molde: com molde, "de %1$s a %2$s Pa" tem 17 caracteres e o que o Google corta tem 20.

**AS TRAVAS SILENCIOSAS, contadas em vez de confiadas:** três coisas fazem a promessa sumir sem sintoma — banco fora do ar, chave ausente da medição, título estourando 65. Nos três casos a página volta a ser válida com a marca, e é por isso que `ferramentas/mutacoes-promessa-do-titulo.py` nasceu junto: **6 de 6**, nenhuma inerte, e o mundo sadio passa. A quinta mutação é a que importa e nenhuma régua da casca pegaria sozinha: o Pa voltando a ser contado sobre publicável.

**O QUE FALTA, E NÃO É DA FUNDAÇÃO:** a segunda metade do "pronto quando" pede que a **leitura semanal seguinte** registre impressões e CTR das três linhas em `dados/posicoes.md` para comparar com 9,2 / 6,8 / 7,0 e 0%. O de-para dos títulos velhos e novos já está escrito lá, para a comparação ser legível. A ressalva da amostra fina continua valendo inteira, e está repetida no `posicoes.md`.

**O texto original da proposta, para a leitura seguinte poder conferir o que foi pedido:**
- Consultas: anonimizadas pela Search Console (10 das 11 impressões). Páginas e posições medidas: `/filtro-universal-de-robo-aspirador/` em **9,2** (5 impressões), `/quantos-pa-o-robo-aspirador-precisa/` em **6,8** (4), `/quantos-m2-o-robo-aspirador-limpa-por-carga/` em **7,0** (2).
- Banda 4 a 10 pela 12.1: o trabalho é de **CTR, não de conteúdo**. E a 12.1 nomeia a alavanca: "título que promete o número, meta que promete a faixa e a fonte".
- O que falta, medido título por título: **nenhum dos três promete um número na SERP.** Hoje eles são "Existe filtro universal de robô aspirador? – Robometria", "Quantos Pa o seu robô aspirador precisa – Robometria" e "Quantos m² um robô aspirador limpa por carga – Robometria". Os três fazem a pergunta e nenhum entrega a prova de que a resposta é numérica e é nossa. A meta description tem o mesmo buraco: descreve o assunto, não a faixa nem a fonte.
- **RESSALVA QUE VALE MAIS QUE A PROPOSTA, e está aqui de propósito:** com 11 impressões no total, "CTR 0%" é amostra fina. Isto é **título e meta, e mais nada** — não é reescrever página, não é mexer em URL (proibido pela 12.1), não é tocar em página que esteja subindo. E a 12.1 manda comparar o CTR com a média das outras na mesma posição; com esta amostra **não há com o que comparar, e isso está escrito em vez de estimado**.
- **Pronto quando:** os três títulos e as três metas citarem um número ou uma faixa que a própria página calcula, com a fonte, e a leitura semanal seguinte registrar impressões e CTR das três linhas em `dados/posicoes.md` para comparar com 9,2 / 6,8 / 7,0 e 0%.

**PROPOSTA 3 — A CONSULTA QUE CHEGOU TEM FORMA DE CONSULTA DE IA, E A SEÇÃO 5 É REGRA DE PRIMEIRA CLASSE.**
- Consulta nomeada: a mesma da Proposta 1, com o prefixo `context: location: brazil (not for language). do not include location references in your response. question: ...`. Posição 10,0.
- O que falta: nada a construir agora. O que esta proposta pede é **registro e vigilância**, porque é a primeira evidência de que a ilha é lida por superfície generativa, e é o tipo de sinal que some se ninguém anotar. A Sentinela **não abriu a SERP** e portanto **não verificou** de que superfície veio.
- **Pronto quando:** a leitura semanal seguinte disser se apareceram mais consultas com esse formato — e, se aparecerem duas ou mais, a Fundação recebe um bloco para conferir se a tabela pré-renderizada da 14.5 cobre a pergunta exata que elas fazem.

**A CAMADA DE VENDA, SEM MAQUIAR:** Shopee Afiliados, período 15/09/2026, **0 cliques e 0 pedidos** — medido no painel do Raphael, não estimado. Com 0 clique orgânico na Search Console, não havia outro número possível. Mercado Livre: **ainda sem dado** — nenhum link do programa existe nesta ilha (as 73 linhas publicáveis do banco são todas `plataforma: shopee`). Backlink, marca e interlinkagem entre ilhas: **ainda sem dado**, e interlinkagem entre ilhas continua proibida pela seção 10.

**O CANO DE LINKS, CONTADO NO `main` E NÃO ESTIMADO (seção 27.3):** 73 registros publicáveis (35 peças + 38 modelos). **Itens sem piso `url_busca`: ZERO.** É a primeira vez que a ilha fecha a 25.2 inteira. **Itens sem `url_produto`: 46** — os 46 estão em `degrau: 4` (a busca É a porta de compra deles) e os 46 têm `motivo_sem_url_produto` escrito: "sem ficha: a escada de palavra-chave da API não casou nenhum resultado com o código deste registro (2026-09-16)". Nenhum item `intestavel: true`. Isso NÃO é defeito da 19.1: item sem ficha porque não há ficha, com a causa escrita, é medição honesta pela 25.7. Os 27 com ficha (12 peças + 15 modelos) têm os quatro campos que a 25.4-b pede e os 27 têm foto medida.

**O QUE A SENTINELA NÃO PÔDE FAZER NESTA EXECUÇÃO, dito para ninguém descobrir depois:** o teto semanal de geração de link de afiliado **não foi gasto**. O canal das MÃOS foi recusado pelo classificador de aprovação do ambiente no começo da execução, e pela 27.2 o banco só muda pelas MÃOS — gerar link que não pode ser gravado seria fabricar dado órfão. O alvo do teto da semana que vem, já escolhido e nomeado: os 46 registros em degrau 4, pelo **degrau 2 da 25.1** (catálogo `/p/MLB…` do Mercado Livre), que é o cavalo de batalha desta cauda longa pela 25.3 — e que precisa do clique do Raphael, pelo reCAPTCHA da 25.6.

## DESPACHO DO RAPHAEL — 18/09/2026 (segunda ordem do dia) — ~~TERMINAR AS FOTOS, E DEIXAR A DECISAO DE OUTUBRO PRE-REGISTRADA~~ — **CUMPRIDO E CONFERIDO NO AR EM 18/09/2026, 13h45Z**

**AS DUAS PARTES SAIRAM NA MESMA EXECUCAO, pela 18.2.** Casca sem mudanca, manifest na **revisao 66**, `/status` em 66.

**PARTE 1 — A COBERTURA MAXIMA QUE O CRITERIO PERMITE E 29 DE 103, E O RESIDUO TEM NOME, NUMERO E CAUSA.** A escada da Open API rodou sobre os **68 publicaveis sem `imagem.url`** — os outros 8 dos "76" do despacho tem `status: excluido_do_banco` ou `nao_publicavel` e nenhuma tela os renderiza, o que esta escrito em vez de escondido na conta. **Casaram 2**, os dois no degrau 4: `multi-pr10205` (filtro, "Filtro Para Robô Aspirador Multilaser Ho041") e `wap-escova-central-wsmart` ("Escova Central Aspirador Robô Wap Robot WSMART Original"). **O banco foi de 27 para 29 fotos.** As duas imagens foram abertas com os olhos antes de gravar (25.3) e as duas estao **servidas no ar**, com dimensao declarada e `alt` de verdade, em `/qual-peca-serve-no-meu-robo-aspirador/?modelo=multi-ho041&peca=filtro` e `...?modelo=wap-wsmart&peca=escova%20principal`. **A lista completa do residuo, por causa, esta em `dados/residuo-de-fotos-2026-09-18.md`** — 63 "a Shopee anuncia e nenhum titulo nomeia este registro", 2 "casamento ambiguo", 1 "sem anuncio na Shopee".

**O PORTAO NAO FOI AFROUXADO — FOI APERTADO, E POR MEDICAO.** O despacho mandou nao baixar o criterio para bater 100%, e o que aconteceu foi o contrario do temido: **um casamento errado passou pela regua e foi pego pelo olho.** `positivo-11206519` e a escova **PRINCIPAL** (o rolo) e casou com *"Escova E Filtro Hepa Para Robo Aspirador Positivo Pra800"* — o codigo PRA800 no titulo e `escova` na cabeca dele. **A foto do anuncio traz um filtro e uma escova LATERAL de tres bracos, e nenhum rolo.** A causa e uma frase escrita como verdade dois dias antes, em `palavras_estritas_do_tipo`: o substantivo pelado basta *"para a coleta, porque la o codigo do registro ou do modelo ja amarrou o anuncio"*. A primeira metade e verdadeira e a segunda e falsa — **quando quem amarra e o codigo do MODELO, o anuncio esta preso ao APARELHO, e o aparelho tem escova lateral E escova principal, as duas no banco.** A regra desceu para `coletar-shopee.py` e passou a valer nesse caminho; `ferramentas/mutacoes-qual-escova.py` nasceu com **7 de 7**, e com a trava desligada a bateria cai para 4 de 7, o que e a prova de que tres mutacoes estao vivas. **Os 27 registros que ja tinham foto foram reconferidos contra a regua nova: 0 reprovado**, entao o aperto nao custou nenhuma foto ja conferida.

**A PORTA NOVA CONTINUA FECHADA, COMO O DESPACHO MANDOU.** Nenhuma imagem foi colhida de site de fabricante. O numero que a decisao pede esta escrito: **66 de residuo, 30 modelos e 36 pecas.**

**PARTE 2 — CUMPRIDA: o criterio saiu de dentro deste despacho e virou secao permanente**, logo abaixo ("CRITERIO PRE-REGISTRADO DA DECISAO DE OUTUBRO"). O motivo e a 18.4: despacho morre quando e verificado, e criterio que mora dentro de um despacho morre junto com ele. Pela 1.2-b.4 o criterio tem de morar no `PROMPT.md` da ilha, e agora mora.


**ISTO NAO E EXPANSAO E NAO ESBARRA NO DESPACHO DE CONGELAMENTO ABAIXO.** E o despacho da API da Shopee de 16/09 terminando de sair: a coleta rodou uma vez, sobre o banco daquele dia, e o banco cresceu 30 registros depois dela. Terminar coleta comecada nao e investimento novo.

### PARTE 1 — SEGUNDA PASSADA DE COLETA DE IMAGEM

Estado medido no `main` em 18/09/2026, 12h10Z: **103 registros, 27 com foto (26%), 76 sem.** O Raphael pediu, com estas palavras, "preciso de todos com imagens".

**O QUE FAZER:** rode `ferramentas/shopee-api.py` sobre **todos os 76 registros sem `imagem.url`**, nos dois bancos, usando a escada de palavra-chave que o adendo de 16/09 fixou — codigo sozinho, marca + codigo, marca + modelo + tipo de peca, e por ultimo a chave de `url_busca_produto`. Grave `imagem`, `afiliado.url_produto` e o link com sub-id quando vierem. Registre em qual degrau cada item casou.

**O PORTAO QUE NAO SE AFROUXA, e ele vale mais que a meta de cobertura:** se o titulo que voltou nao contiver o codigo da peca ou o nome do modelo, **o registro fica sem foto**, com o motivo escrito. **Foto errada num registro de peca e pior que nenhuma foto** — a ilha inteira se vende por procedencia, e um filtro ilustrado com a foto do filtro errado destroi exatamente isso. Nao baixe o criterio para bater 100%.

**E POR ISSO O ALVO AQUI E HONESTO, NAO REDONDO.** Pode ser que 100% seja inalcancavel pela API: peca de reposicao de marca pequena simplesmente nao esta anunciada na Shopee. **O entregavel desta passada e a cobertura maxima que o criterio permite, MAIS a lista do residuo com o motivo de cada um**, agrupada por causa (sem anuncio na Shopee, titulo nao nomeia o modelo, casamento ambiguo). Essa lista e o que permite decidir o passo seguinte.

**UMA PORTA NOVA QUE EXISTE AGORA E QUE VOCE NAO DEVE ABRIR SOZINHA:** desde 17/09 os cinco dominios de fabricante estao liberados na rede, e paginas de fabricante tem foto de produto. **NAO colete imagem de site de fabricante nesta execucao.** A licenca e diferente: a secao 25.3 chama a imagem do feed/API de "fonte legitima" porque **a imagem do anuncio ao lado do link do anuncio e exatamente o que o programa de afiliado existe para permitir** — e isso nao se estende ao site do fabricante. Isso e decisao do Raphael, e ele decide depois de ver o tamanho do residuo. Escreva o numero e pare.

### PARTE 2 — A DECISAO DE OUTUBRO, ESCRITA ANTES DO DADO

O destino desta ilha depende da serie de impressoes, e a serie so ganha corpo em outubro. **O criterio tem de ser escrito AGORA, antes dos numeros chegarem** — criterio escrito depois do dado e criterio dobrado para caber no dado que veio. Esta parte nao pede medicao nenhuma hoje: pede que a regra exista.

**A ESTRUTURA DA DECISAO, fixa desde ja:**

- **Quem mede:** a leitura semanal da Sentinela, as quartas. As leituras que contam sao **23/09, 30/09, 07/10 e 14/10** — quatro pontos.
- **O que se mede:** impressoes em 28 dias e cliques, da Search Console, na serie de `dados/indexacao.md`; e a tabela de posicoes em `dados/posicoes.md`.
- **A leitura de 30/09 fixa o numero de corte**, e o fixa com DUAS referencias na mesa: a propria serie da Robometria e a serie da Aquametria no mesmo periodo de vida da ilha. Fixar corte hoje, com 11 impressoes, seria inventar.
- **Os tres desfechos possiveis, e nenhum outro:** (a) **a ilha volta a receber investimento** — malha cresce, leva nova de modelos, bloco de conteudo; (b) **a ilha fica em manutencao** — Sentinela continua, Fundacao nao investe, e o assunto so volta se a serie mudar; (c) **a ilha e arquivada** — o site fica no ar, a ronda para, e o aprendizado vai inteiro para a `BUSSOLA.md`.
- **O QUE NAO PODE ACONTECER, e esta linha existe para impedir:** a decisao ser adiada por falta de dado. Se em 14/10 a serie ainda estiver fina, isso **e** o resultado — nicho que em cinco semanas de indexacao nao produziu impressao mensuravel ja respondeu. Adiar por mais um mes e o jeito educado de nunca decidir.
- **O contexto que a decisao nao pode ignorar:** `bussola/medicoes/volume-absoluto-2026-09-18.md` mediu que as consultas de peca desta ilha estao abaixo do limiar do Google, e que o volume do nicho esta na metade de dimensionamento (R2). Uma serie fraca em outubro **confirma** essa medicao; uma serie forte a contradiz e vale um registro proprio, porque significaria que o Planejador nao enxerga a cauda que a ilha atende — e isso mudaria a regua da Bussola inteira.

**A LEITURA SEMANAL DE 23/09 JA DEVE ABRIR A SERIE COM ESTE ENQUADRAMENTO**, dizendo em qual dos quatro pontos ela esta e o que falta para o corte de 30/09.

## CRITERIO PRE-REGISTRADO DA DECISAO DE OUTUBRO — escrito em 18/09/2026, ANTES do dado

**ESTA SECAO NAO MORRE COM DESPACHO NENHUM.** Ela nasceu dentro do despacho de 18/09 e foi levantada para fora dele na mesma execucao que o cumpriu, porque a 18.4 manda apagar despacho verificado e a 1.2-b.4 manda o criterio morar no `PROMPT.md` da ilha. Criterio que mora dentro de um despacho morre junto com ele — e ai a decisao de outubro chegaria sem regra, que e exatamente o que este texto existe para impedir.

**POR QUE ELE ESTA ESCRITO HOJE, com 11 impressoes na mesa:** *criterio escrito depois do dado e criterio dobrado para caber no dado que veio.* Esta secao nao pede medicao nenhuma hoje. Ela pede que a regra exista antes de haver o que ela julgue.

**QUEM MEDE:** a leitura semanal da Sentinela, as quartas. As leituras que contam sao **23/09, 30/09, 07/10 e 14/10** — quatro pontos, e nenhum a mais.

**O QUE SE MEDE:** impressoes em 28 dias e cliques, da Search Console, na serie de `dados/indexacao.md`; e a tabela de posicoes em `dados/posicoes.md`.

**A LEITURA DE 30/09 FIXA O NUMERO DE CORTE**, e o fixa com DUAS referencias na mesa: a propria serie da Robometria e a serie da Aquametria no mesmo periodo de vida da ilha. Fixar corte hoje, com 11 impressoes, seria inventar.

**OS TRES DESFECHOS POSSIVEIS, e nenhum outro:**

| desfecho | o que acontece |
|---|---|
| **(a) volta ao investimento** | malha cresce, leva nova de modelos, bloco de conteudo |
| **(b) manutencao** | Sentinela continua, Fundacao nao investe, e o assunto so volta se a serie mudar |
| **(c) arquivada** | o site fica no ar, a ronda para, e o aprendizado vai inteiro para a `BUSSOLA.md` |

**O QUE NAO PODE ACONTECER, e esta linha existe para impedir:** a decisao ser adiada por falta de dado. Se em 14/10 a serie ainda estiver fina, isso **e** o resultado — nicho que em cinco semanas de indexacao nao produziu impressao mensuravel ja respondeu. **Adiar por mais um mes e o jeito educado de nunca decidir.**

**O CONTEXTO QUE A DECISAO NAO PODE IGNORAR:** `bussola/medicoes/volume-absoluto-2026-09-18.md` mediu que as consultas de peca desta ilha estao abaixo do limiar do Google, e que o volume do nicho esta na metade de dimensionamento (R2). Uma serie fraca em outubro **confirma** essa medicao; uma serie forte a contradiz e vale um registro proprio, porque significaria que o Planejador nao enxerga a cauda que a ilha atende — e isso mudaria a regua da Bussola inteira.

**UM SEGUNDO SINAL, MEDIDO EM 18/09 E QUE NAO EXISTIA QUANDO O CRITERIO FOI ENCOMENDADO:** a segunda passada de fotos mediu que **o catalogo da Shopee Brasil nao tem a granularidade que esta ilha oferece** — anuncio de reposicao aqui e kit misto generico por modelo, nao peca por codigo, e o robo em si quase nao e anunciado (`dados/residuo-de-fotos-2026-09-18.md`). **Isso e a mesma medicao do volume, vista do lado da oferta em vez do lado da demanda**, e as duas apontam para o mesmo lugar. Quem for decidir em outubro le as duas juntas; se a serie de impressoes vier forte APESAR das duas, o achado e maior que a ilha e vale registro proprio na `BUSSOLA.md`.

**A LEITURA SEMANAL DE 23/09 JA DEVE ABRIR A SERIE COM ESTE ENQUADRAMENTO**, dizendo em qual dos quatro pontos ela esta e o que falta para o corte de 30/09.

## DESPACHO DO RAPHAEL — 18/09/2026 — A ILHA TERMINA, MAS MUDA DE ESTADO: DE APOSTA PARA EXPERIMENTO MEDIDO

Em 18/09/2026 o volume de busca do corpus desta ilha foi medido pela primeira vez, no Google Keyword Planner. O levantamento inteiro, com metodo e ressalvas, esta em `bussola/medicoes/volume-absoluto-2026-09-18.md`. O resultado, em uma linha: **de 49 consultas, 9 tem volume — e NENHUMA delas e de peca ou compatibilidade.** As consultas mais amplas possiveis do assunto desta ilha (`filtro robô aspirador`, `escova lateral robô aspirador`, `peças robô aspirador`) estao **abaixo do limiar de relatorio do Google**. Na mesma ferramenta e no mesmo dia, `filtro para aquario` deu 1 mil–10 mil.

**ISTO EXPLICA A SEARCH CONSOLE, e nao contradiz nada.** 11 impressoes em 28 dias com tres paginas na primeira pagina do Google nao era um mistério: e primeira pagina de um assunto que quase ninguem procura. A ilha nao errou a execucao — o nicho nao tem gente na metade que ela construiu.

**DECISAO DO RAPHAEL, TOMADA COM O NUMERO NA MESA:**

1. **A ilha TERMINA.** Faltam quatro dias e um item; parar agora desperdicaria o que ja esta pago. A DEFINICAO DE PRONTA continua valendo inteira e o prazo de 23/09 continua de pe.
2. **Depois de pronta, ela NAO recebe investimento novo.** Deixa de ser candidata a bloco de crescimento e vira **experimento medido**: a serie de indexacao e posicao continua rodando, e **outubro decide**. Nenhuma execucao da Fundacao deve propor expansao de malha, leva nova de modelos ou bloco de conteudo nesta ilha sem que a serie mostre impressao em dois digitos.
3. **A metade que interessa e a R2, nao a R1.** O trafego que existe esta em dimensionamento — `robô aspirador que passa pano` (1 mil–10 mil), `qual robô aspirador comprar` (100–1 mil), `robô aspirador com mop` (100–1 mil) — e sao as paginas da R2 que ja ranqueiam. **A peca nao precisa ranquear; precisa estar ALCANCAVEL de dentro da R2.** Isso nao diminui o item 2 da DEFINICAO DE PRONTA — aumenta: a emenda do funil deixa de ser "juntar duas metades" e passa a ser o unico jeito de monetizar o unico trafego que a ilha tem.
4. **Nada disto se resolve com mais esforco na R1.** Se alguma execucao futura propuser "mais paginas de peca para crescer", esta linha e a resposta: foi medido, e nao tem quem procure.

## DESPACHO DO RAPHAEL — 17/09/2026 — A REDE ABRIU PARA OS FABRICANTES, E DOIS DOS CINCO ENDERECOS NUNCA EXISTIRAM

A execucao das 10h16Z de 17/09 registrou o item 2 da DEFINICAO DE PRONTA como **bloqueado por rede**, listando cinco dominios de fabricante que devolveram 403 do proxy de egresso. O Raphael acrescentou os cinco a lista de dominios permitidos da conta. **Medido da nuvem as 12h35Z de 17/09, um por um:**

```
www.electrolux.com.br            301  aberto
www.multilaser.com.br            200  aberto
mais.conteudo.wap.ind.br         200  aberto
www.mi.com                       301  aberto
www.positivotecnologia.com.br    200  aberto
```

**OS CINCO CAMINHOS ESTAO ABERTOS. O ITEM 2 DEIXA DE SER "BLOQUEADO POR REDE" E VOLTA A SER TRABALHO DA FUNDACAO.**

**DOIS DOS CINCO NOMES ESTAVAM ERRADOS, E O ERRO NAO ERA DE REDE.** A lista registrada trazia `www.mi.com.br` e `loja.positivotecnologia.com.br`. **Esses dois hostnames nao existem** — nao resolvem em DNS, nunca resolveram, e nenhuma lista de permissao faria diferenca. Os enderecos certos, conferidos no DNS antes de serem liberados, sao **`www.mi.com`** (a Xiaomi Brasil mora em `mi.com/br/`, nao em `mi.com.br`) e **`www.positivotecnologia.com.br`** (sem o `loja.`). Use esses dois daqui em diante e nao volte aos antigos.

**A LICAO DE PROCESSO, E ELA VALE PARA TODA ILHA (secao 20.2).** Um `403` do proxy e um host que nao existe produzem o mesmo sintoma para quem so olha `curl`: falha. Mas sao coisas opostas — o primeiro e um pedido de liberacao ao Raphael, o segundo e um endereco errado que so quem escreveu pode consertar. **Antes de declarar "bloqueado por rede", confira se o host resolve** (`getent hosts <host>`, ou qualquer consulta de DNS). Host que nao resolve nunca entra numa lista de "bloqueado": entra como **endereco errado**, e o conserto e trocar o nome, nao pedir permissao. Declarar bloqueio em endereco inexistente faz o placar mentir na direcao mais cara de todas — sugere que o trabalho esta parado esperando outra pessoa, quando esta parado esperando uma correcao de digitacao.

**O QUE FAZER AGORA, e e o caminho unico ate os 15 da emenda do funil:** colete `pa_declarado` e `canal_brasileiro` nos cinco fabricantes, fora da Xiaomi, que ja foi. A API da Shopee **nao serve para isto** e isso ja foi medido: ela traz foto, ficha e link, e nao traz nenhum dos dois campos. Vale a regra de sempre — dado com procedencia por campo, escada de fontes respeitada, e o que nao for encontrado fica `null` com o motivo escrito, nunca chutado por vizinhanca.

## DESPACHO DO RAPHAEL — 16/09/2026 — a API da Shopee ~~fecha quatro buracos desta ilha~~ — **CUMPRIDO E CONFERIDO NO AR EM 16/09/2026, 17h05Z**

Os quatro itens saíram inteiros, pela seção 18. Esquema na versão 9, casca 1.8.0, R1 1.10.0, R2 1.8.0, A1 1.4.0, A2 1.4.0, manifest na revisão 54.

**Como foi conferido, e não pelo log do Sync (18.4):** `conferir-no-ar.py` fechou com **251 afirmações e 0 falha**, incluindo a seção 12 nova — toda foto servida tem dimensão declarada, `alt` de verdade, `loading="lazy"` e endereço que **existe no banco**. O HTML servido de `/quantos-m2-o-robo-aspirador-limpa-por-carga/` traz `<img class="rbm-vitrine-img" ... width="1000" height="1000" alt="Aspirador Robô Electrolux 4 em 1 ... ERB60">`. A ilha tem foto no ar pela primeira vez.

**Os quatro critérios de pronto do despacho, um a um:** `ferramentas/shopee-api.py` roda e devolve JSON de consulta real; o banco tem **27** registros com `imagem.url` e `afiliado.url_produto`, todos conferidos à mão; o HTML servido mostra a foto; `validar-banco.py` passa; e **nenhum arquivo, log ou mensagem de commit contém o AppID ou a Senha** — conferido com `grep` na árvore inteira antes de cada push.

**A coleta, em números:** 27 de 73 publicáveis casaram (12 peças, 15 modelos), nos degraus 1→12, 2→3, 3→8 e 4→4. **Os 46 que não casaram ficaram sem foto e sem ficha, com o motivo escrito.** As cinco armadilhas de casamento que a conferência de olho da 25.3 pegou — e que a regra do despacho aprovaria — subiram para o contrato como seção **25.7**, junto com o achado de que a Shopee **valida o sub-id e recusa hífen e sublinhado**.

**O que o despacho não pedia e foi junto, porque o dado novo o cobrou:** o portão da imagem no `validar-banco.py` (url não-nula exige largura, altura, fonte, data e alt; url nula exige motivo); `largura` e `altura` **medidas do arquivo** e nunca digitadas; `itens_com_ficha` do cabeçalho do banco, que contava o **link de afiliado** e se chamava ficha, virou duas chaves; e o painel da foto passou a ser **uma** função na casca, chamada pelas quatro ferramentas.

**A dívida que continua aberta, e ela não é desta ilha:** o **item 2 da DEFINIÇÃO DE PRONTA** não andou. A API trouxe foto, ficha e link — não trouxe `pa_declarado` nem `canal_brasileiro`, que são o que a interseção das duas ferramentas conta. A interseção segue **8 de 38**. Os três caminhos medidos continuam valendo como estão escritos no `ESTADO.md`.

## DESPACHO DO RAPHAEL — 16/09/2026 — o espaço reservado da foto ~~está desenhado como uma roda de carregamento~~ — **CUMPRIDO E CONFERIDO NO AR EM 16/09/2026, 16h26Z**

As duas edições saíram (casca 1.7.1, R1 1.9.1, R2 1.7.1, A1 1.3.1, A2 1.3.1, manifest na revisão 53). **Conferido no ar pela regra 18.4, e não pelo log do Sync:** nas quatro páginas de ferramenta a folha servida traz `.rbm-vitrine-vazia::after{content:"sem foto";}`, a regra do painel não tem `border-radius` nem lado transparente, e os **17 painéis** servidos trazem cada um OU a foto OU o aviso — nunca os dois, nunca nenhum. `conferir-no-ar.py` ganhou a seção 12 e fechou com **250 afirmações, 0 falha**.

**O que o despacho não pedia e entrou junto, porque a trava não muda uma linha do banco de hoje:** `ferramentas/mutacoes-lugar-vazio-da-foto.py`, 6 de 6 no resultado esperado, **quatro delas plantando a foto que o banco ainda não tem** (seção 8: o caso que o esquema permite, a régua trata hoje) e a sexta sendo o MUNDO SADIO, que tem de passar. E a régua da R1 parou de cobrar "um painel por peça" — que é a mesma coisa que exigir que nenhuma peça tenha foto, e teria reprovado a primeira imagem que a API trouxesse.

## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz

~~**Reescrever a home e o header pelo molde FERRAMENTA e pela voz do `VOZ.md`.**~~
**CUMPRIDO em 11/09/2026** — casca 1.2.0, manifest na revisão 15. A home virou a
ferramenta (promessa numa linha, o seletor da R1 chamado e servido no HTML,
atalhos por tipo de peça derivados do banco), a confissão numérica foi para a
metodologia (seção 15.2: número mora na camada de prova), o H1 da raiz deixou de
ser "Início" e o menu virou Peças · Sucção · Como conferimos. Nenhuma URL mudou.
Critério de pronto conferido na bancada, não de olho: `teste-casca.php` mede o
título da raiz e o primeiro parágrafo da home contra a lista de proibidas do
`VOZ.md`, por estrutura e nunca na página inteira.

**A árvore da seção 16 está CUMPRIDA em 11/09/2026** — casca 1.3.0, manifest na
revisão 16, `/status` conferido e as nove URLs abertas no ar às 19h47Z. Nasceu o
`ARVORE.md` desta ilha (quatro seções de nível 1, quatorze categorias de nível 2,
o lugar de cada página de hoje); trilha nas oito páginas que não são a home (16.3),
`BreadcrumbList` levando só os degraus com endereço de verdade, e blocos "Veja
também" com as irmãs derivadas mais a frase que linka a mãe com a contagem
contada. **Nenhuma URL nova**, que era a condição para caber agora. Critério de
pronto medido, não de olho: `ferramentas/teste-arvore.php` (213 afirmações, régua
própria, um processo `php` por página, e ele LÊ o `ARVORE.md` para cobrar que
documento e código digam a mesma coisa), 18 mutações deliberadas em
`ferramentas/mutacoes-arvore.py` — 18 reprovadas — e 258 medições em Chromium.

**As duas decisões que este despacho mandou tomar, tomadas** (o porquê está na
seção 2 do `ARVORE.md`): `/metodologia/` **fica na raiz**, porque a lista da 16.1
nomeia a família da página institucional e ela é dessa família; `/ferramentas/`
**fica hoje como mãe de transição** das duas ferramentas e sai com 301 para a home
no dia em que `/pecas/` e `/succao/` nascerem, porque aí ela passaria a servir a
mesma listagem que elas. O menu continua Peças · Sucção · Como conferimos: os três
rótulos do `VOZ.md` só entram quando as seções existirem como página.

**O que continua de pé desta seção, e trava até o Search Console:**
- **as quatro páginas de nível 1 e as quatorze de nível 2**, e a troca de pai e
  slug das existentes (com 301 para toda URL que mudar). São dezoito URLs novas, e
  esta ilha não publica leva de malha enquanto o sitemap não for reenviado — é a
  metade humana do despacho da Sentinela de 10/09, logo abaixo, e é do Raphael.
  Quando destravar, o nível 1 e o nível 2 da trilha e do `BreadcrumbList` viram
  link sozinhos: quem resolve o endereço é `robometria_casca_url_se_existir()`.
- **a frase de mãe dos dois guias** (16.4b), que só nasce junto com `/guias/`: hoje
  ela apontaria para página inexistente, e o portão cobra a ausência dela
  justamente para ninguém fechar isso com um endereço inventado.

**A VOZ CHEGOU ÀS NOVE PÁGINAS — CUMPRIDO em 11/09/2026**, casca 1.4.0, manifest
na revisão 17, `/status` conferido e as nove URLs medidas no ar às 21h48Z (65
afirmações, 0 falha). Fecha a 15.5 nesta ilha: as oito páginas que não são a home
ganharam abertura na voz do `VOZ.md` — nenhuma começa mais nomeando a própria
página ("Esta ferramenta responde…", "A Robometria é um banco de…") — e a
procedência desceu um parágrafo, para a camada de prova (`rbm-prova`), como manda
a 15.2. **Nenhuma URL mudou.**

E o achado que não estava no despacho: **seis das nove páginas tinham DOIS
NOMES**, porque o mapa das cabeças (1.2.0) trazia um título digitado ao lado do
da definição da página. O `og:title` dizia "Quem publica a Robometria" e o H1, na
mesma página, "Sobre". Agora o nome tem uma fonte só e as cinco superfícies
derivam dela, com portão próprio (`ferramentas/teste-voz.php`, 155 afirmações, um
processo por página). O `<title>` passou a ser escrito por este repositório: na
home ele vinha do campo de descrição curta do wp-admin, com 73 caracteres em
vocabulário de dentro da fábrica.

ATUALIZAÇÃO 11/09 (Pauta): quando existir `pauta.md` nesta pasta (seção 17 do contrato), os guias entram na fila depois da árvore, em levas por cluster; registrar no fecho de cada bloco quantos temas estão escritos / na fila / recusados.

## DESPACHO DA SENTINELA — 16/09/2026 (ronda diária, 14h50Z) — ~~quatro itens~~ — **CUMPRIDO E CONFERIDO NO AR EM 16/09/2026, 20h**

Os quatro itens saíram inteiros na mesma execução, pela 18.2. Casca **1.9.0**, A1 **1.5.0**, A2 **1.5.0**, R1 **1.10.0**, manifest na **revisão 58**.

**Como foi conferido, e não pelo log do Sync (18.4):** `conferir-no-ar.py` ganhou as seções **13** (as duas datas do JSON-LD servido) e **14** (a busca do botão tem resultado) e fechou com **264 afirmações**. O HTML servido de `/filtro-universal-de-robo-aspirador/` traz `datePublished 2026-09-10` e `dateModified 2026-09-16`; o de `/quantos-m2-o-robo-aspirador-limpa-por-carga/` traz `2026-09-11` e `2026-09-16` — e até hoje essa página não servia `datePublished` nenhum.

### item 1 e item 3 — A PALAVRA-CHAVE PASSOU A SER MEDIDA, E A CAUSA ERA A MESMA NOS DOIS

Os dois achados tinham uma causa só, e ela já estava escrita no contrato antes de ser medida: a **seção 26** diz que *o vocabulário da ilha classifica pela FUNÇÃO e o fabricante batiza pela POSIÇÃO*. A chave de busca era composta do `tipo` — `escova principal`, `escova lateral` —, que é vocabulário da ILHA, e **vendedor nenhum digita isso**.

Nasceu `ferramentas/medir-palavras-chave.py`: ela chama a Open API da Shopee e desce uma **escada de cinco degraus** até achar a chave que serve o leitor — tipo, **batismo do fabricante** (a cabeça de `nome_na_fonte`), código da peça, código do modelo compatível, marca. Para no PRIMEIRO degrau que serve, e grava o que a API devolveu em `dados/palavras-chave-medidas.json`, com a data.

**O esquema prometia isto por escrito desde 13/09**, em `por_que_a_peca_nao_leva_o_codigo`: *"o estreitamento já tem data e dono: a Open API da 25.6 (...) No dia em que ela responder, quem estreita a chave consegue provar que ela traz resultado antes de gravar."* Este foi o dia. E a mesma frase supunha que o **código de peça** não aparece em título de anúncio — medido, é **falso**: loja de reposição digita `FW008024` e `PR10205`.

**Os números, medidos e não estimados:** das 18 chaves de ontem, a Open API devolve **zero em três** — e as três são `escova principal`, da Electrolux, da Positivo e da WAP. Depois da escada: **20 de 20 chaves com resultado** (zero beco sem saída) e **16 de 20** no critério do item 3, contra as **14 de 18** que o despacho pediu. Pela régua mais dura da 25.7 (o tipo é a CABEÇA do título), são 7 de 20 — o número está impresso ao lado do outro de propósito, porque esconder a folga entre as duas réguas seria escolher qual citar depois de ver o resultado.

**A bateria da Multilaser é a única sem conserto de chave**, e isso é medição honesta: o catálogo de ofertas não tem bateria de robô Multilaser, e o topo é sempre o carregador — por qualquer caminho da escada.

**O que o despacho não pedia e foi junto, porque o dado novo o cobrou:** o **encurtamento** deixou de esperar alguém. `generateShortLink` com sub-id fechou o segundo elo do piso da 25.2 — *"saída crua, sem rastreio"* foi de **5 para 0** em 73 publicáveis, e os cinco modelos Xiaomi que estavam sem link curto ganharam o deles.

**E a régua achou um beco sem saída que despacho nenhum tinha apontado:** o modelo `multi-ob010`. `Multilaser OB010 robo aspirador` devolve **zero** — a Multi vende aquele aparelho como **ObaDuster**, da Obabox, e ninguém anuncia o OB010. O modelo ganhou um segundo degrau com a mesma regra da peça, e `Multilaser ObaDuster robo aspirador` responde.

### item 2 — OS DOIS UNIVERSOS DO PAR GANHARAM NOME, E NENHUM FOI IGUALADO

A promessa da R1 passou a servir **70**, que é o par com as DUAS pontas publicáveis — o mesmo universo dos 38 modelos que a frase cita. Os outros dois números existem e têm nome próprio: `pares_declarados_no_banco` (71) e `pares_para_modelo_nao_publicavel` (1). É o mesmo conserto dos dois 63 do despacho de 14/09.

`teste-r1.php` reconta os **dois** universos por conta própria, e `ferramentas/mutacoes-universo-do-par.py` prova o que o *pronto quando* exigia — *"a régua tem de reprovar o mundo de hoje antes de aprovar o de amanhã"*: **3 de 3**, uma delas quebrando o gerador.

### item 4 — `dateModified` PASSOU A SAIR DE UM CAMPO NOVO, e a decisão está escrita

O despacho deixou a escolha aberta entre três. É um **campo novo**, e as outras duas foram descartadas com motivo: `gerado_em` dos fatos mede *a geração dos FATOS* e ficou cego para a revisão 52, que mexeu na **casca** sem regerar fato nenhum; a revisão do manifest é da **ilha inteira** e faria a data de um artigo andar porque outro mudou — ruído num campo que o Google usa para decidir se vale reindexar.

`ferramentas/gerar-datas-das-paginas.py` mede do **git** o commit mais recente entre os arquivos que compõem cada página, **a casca inclusa** — é ela que escreve a cabeça, a trilha e o bloco de compra DENTRO do artigo, e foi uma mudança de casca que atrasou o campo. `datePublished` continua **declarado**, com a entrada do `REGISTRO.md` ao lado, porque o histórico do `main` foi reescrito e o git jura que todo arquivo desta ilha nasceu em 15/09.

`robometria_casca_datas_da_pagina()` é **uma função só**, chamada pelas duas páginas. Sem a option, nenhuma data é publicada: ausente o Google infere, errada ele acredita.

**E a bancada passou a carregar TODAS as options do manifest**, não só as que cada teste escreve à mão. Ela mediu uma página sem o dado novo enquanto o site sairia com ele — **bancada que vê menos que o ar aprova o que o ar reprova**.

### O QUE FICA ABERTO, e não é desta ilha

**A busca do site não é mensurável desta nuvem, e as duas medições discordam.** `shopee.com.br/api/v4/search/search_items` devolve `error 90309999, redirect_to_error_page`, e a página de busca serve casca de JavaScript **idêntica byte a byte** para palavras diferentes — remedido em 16/09/2026. Então o que a régua nova prova é que a chave existe no catálogo que **paga comissão**, que não é o mesmo universo da busca que o leitor vê: `WAP escova lateral robo aspirador` devolve **zero** na busca do site (medido pela Sentinela no Chrome do Raphael) e **dez** na API. As duas chaves mortas que a ronda mediu no site e as três que a API mediu **não são o mesmo conjunto**. A única via para medir o universo do leitor continua sendo o navegador dele.

---

## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU, E É TUDO DO RAPHAEL

**Os itens 1, 2 e 3 deste despacho foram cumpridos em 14/09 e 16/09, reconferidos no ar pela ronda de 16/09/2026 às 14h50Z, e apagados daqui pela regra 18.4.** O que segue são os itens 4 e 5, que nunca foram da Fundação: os dois dependem de uma sessão logada ou de uma decisão do Raphael, e por isso atravessaram as rondas. A numeração original foi mantida de propósito, para o `REGISTRO.md` e o `dados/PAINEL.md` continuarem batendo com ela.

### 4. O PISO DA 25.2 — **a conta mudou em 14/09/2026, e a dívida agora tem outro nome**

Esta ronda contou 32 itens (só o `pecas.json`); com os 33 modelos de `modelos-robo.json` são **65**. A execução das 15h17Z fechou o despacho do Raphael e a leitura correta passou a ser esta:

- **65 de 65 têm saída de compra na página** — a busca crua, que a máquina fabrica sozinha. **Zero sem saída**, que é o que a 25.2 chama de defeito da 19.1.
- ~~**65 de 65 saem por link que NÃO rastreia e NÃO paga comissão.** Isso não é defeito de página: é dívida de receita, e o que falta continua sendo só o ENCURTAMENTO, que exige a sessão logada do painel da Shopee (25.6).~~ **ESTA DÍVIDA MORREU EM 16/09/2026, E DEIXOU DE SER DO RAPHAEL.** A Open API de Afiliados devolve o link já encurtado na mesma chamada que traz foto e ficha, então o encurtamento não exige mais sessão logada de ninguém (25.6, reescrita). **O que sobra é trabalho de coleta da Fundação, não pendência humana:** em 17/09 o banco tinha 12 de 49 peças e 15 de 45 modelos com link gerado pela API, e os demais continuam saindo pela busca crua, que é o piso da 25.2 e não é defeito. Este item sai da conta do item 3 da DEFINIÇÃO DE PRONTA e entra na fila normal da Fundação.
- **65 de 65 seguem sem `url_produto`**, porque não há ficha de produto nenhuma para conferir. `intestavel` é `false` nos 65 — não há link encurtado cuja saúde fique desconhecida.

**Continua sendo linha de "Precisa do Raphael"**, e o texto original desta ronda segue valendo para essa metade: a escolha da palavra-chave está feita, item a item. O que mudou é que **a página parou de esperar por ela**.



**A metade que já estava feita, e que muda de quem é a dívida:** os 65 têm `afiliado.url_busca_produto` preenchido com a URL crua da busca e `motivo_sem_url_busca` escrito. Exemplo: `multi-pr10124` → `https://shopee.com.br/search?keyword=Multilaser%20escova%20lateral%20robo%20aspirador`. **A escolha da palavra-chave já foi feita; falta só o encurtamento**, que pela 25.6 exige a sessão logada do painel de afiliado da Shopee. A seção 12 proíbe a ronda diária de gerar link de afiliado novo.

*(Os parágrafos que ficavam aqui diziam "a ilha continua no ar sem UMA porta de compra" e "32 itens intestáveis". As duas frases eram verdade quando esta ronda as escreveu, às 14h32Z, e deixaram de ser às 15h47Z. Foram REESCRITAS e não acrescentadas: duas frases em desacordo no mesmo arquivo não são história, são armadilha — a próxima execução acredita na que ler primeiro.)*

### 5. ACHADO DE MÉTODO: o teste de vida da 25.4, do jeito que está escrito, NÃO É EXECUTÁVEL hoje — e existe um caminho que funciona

Isto não é defeito desta ilha. Está aqui porque a 25.4 manda a ronda diária abrir a página do produto, e **isso falhou nas duas vias, medido hoje**:

- **Da nuvem:** `shopee.com.br` e `www.mercadolivre.com.br` devolvem **0 bytes** (egresso). Não é intermitência: repetido.
- **Do Chrome do Raphael, navegando:** a Shopee redireciona para `shopee.com.br/verify/captcha?...&scene=crawler_item` depois de poucos segundos, tanto em `/search?keyword=` quanto em `/product/<shop>/<item>`. **A Sentinela não resolve CAPTCHA, por regra**, e parou ali.

**O caminho que funcionou, medido hoje no navegador dele, e que a 25.4 deveria passar a mandar usar:** a API de ficha da própria Shopee, chamada por `fetch` de dentro de uma aba já no domínio —

```
https://shopee.com.br/api/v4/pdp/get_pc?shop_id=<shop_id>&item_id=<item_id>&detail_level=0
```

devolve `data.item.title` e `data.item.item_status`. Os dois ids saem tanto de `.../product/<shop_id>/<item_id>` quanto do sufixo `i.<shop_id>.<item_id>` das URLs de slug. **Não gasta clique de afiliado, não depende de ler texto de página renderizada e não esbarra no anti-robô.** Isto pede uma linha na 25.4 do `ARQUIPELAGO.md` — e essa linha é do Raphael, não da Fundação.

**Medição de hoje com esse método, feita na clubedomosaico porque a robometria não tem link nenhum para testar** (a ronda é desta ilha; o teste foi onde havia o que testar): **10 de 10 itens vivos**, 0 mortos, 0 esgotados — 6 da Shopee (`tekbond-silicone-acetico-construcao`, `cascola-cascorez-extra`, `quartzolit-rejunte-acrilico`, `quartzolit-rejunte-ceramicas`, `quartzolit-rejunte-porcelanatos-e-ceramicas`, `quartzolit-rejunte-piscinas`), todos com `item_status: normal` e o nome batendo com o do banco; e 4 catálogos `/p/MLB...` do Mercado Livre (`tekbond-silicone-neutro`, `quartzolit-cimentcola-externo-acii`, `loctite-durepoxi`, `quartzolit-rejunte-epoxi`), todos HTTP 200 com o `<h1>` do produto certo. **Nenhum dos 4 links que morreram em 13/09 reapareceu, e nenhum novo morreu em 24 h.**

## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 11/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O despacho de 10/09, logo abaixo, NÃO deve ser apagado:** o que resta nele é a metade humana (reenviar o sitemap no Search Console), que é do Raphael e não da Fundação.

**Nenhuma correção foi feita pela Sentinela nesta ronda.** Os dois defeitos achados moram em código de snippet PHP, e a regra 3 da seção 12 manda parar e despachar.

**OS ITENS 1 E 2 FORAM CUMPRIDOS em 11/09/2026** (casca 1.2.0, manifest revisão 15
— ver `REGISTRO.md`). O texto deles saiu daqui; o que a ronda MEDIU E APROVOU
continua abaixo, como linha de base para a próxima. Um achado dos dois vale ser
lembrado: a trava de página fina que entrou junto reprovou
`/divulgacao-de-afiliados/` com 1.325 caracteres de corpo — defeito que já estava
no ar e que nenhuma ronda tinha procurado.

<!-- item 1 (meta description e Open Graph nas 9 páginas) cumprido em 11/09/2026 -->
<!-- item 2 (H1 da raiz era "Início") cumprido em 11/09/2026 -->

**O QUE A RONDA MEDIU E APROVOU em 11/09/2026 — não refaça, e use como linha de base:**
- `/wp-json/robometria/v1/status` devolve **revisão 14**, igual à do `manifest.json`. As 9 URLs do sitemap devolvem 200 e abrem; nenhuma página órfã; todo link interno vivo.
- **Zero `&#038;` dentro de `<script>`** nas nove páginas (contado só dentro dos blocos de script, 15 a 17 por página).
- Corpo não começa por YAML; JSON-LD presente em todas (`Organization+WebSite`, mais `WebApplication+FAQPage` nas duas ferramentas e `Article+FAQPage` nos dois artigos); favicon próprio; botão de menu com `aria-expanded="false"` e `aria-controls="rbm-nav-lista"`; nenhuma imagem sem `alt`; nenhum `noindex` indevido; canonical em todas; **console sem mensagem**.
- **R2 executada com entrada real e o número conferido na mão:** 200 m², piso liso, sem animal, referência Electrolux ERB60 (166 m² por carga) → limiar 3.000 Pa (Mundo Conectado), menor limiar "até 1.500 Pa", **6 modelos**, e "200 m² exigem 2 ciclos: 200 minutos, mais 1 recarga" — bate com `dados/tabela-exemplos-r2.md` e com `ceil(200/166)=2`. Borda do `ceil` conferida nos dois lados: **166 m² → 1 ciclo** ("faz 166 m² em um ciclo só — 100 minutos"), **167 m² → 2 ciclos**, **332 m² → 2 ciclos**. Caso sem retomada conferido: 333 m² com ERB44 recusa publicar a conta e diz por quê.
- **R1 executada com entrada real:** `electrolux-erb44` com "todas as peças" e com "bateria" devolve, palavra por palavra e com os acentos no lugar, o que está em `dados/r1-referencia.json` — inclusive o kit sem composição transcrita e a recusa "não vamos supor", sem bloco de compra.
- **Os números da `/metodologia/` foram conferidos contra o banco, e batem:** a escada serve 47 de nível 3, 18 de nível 4 e 7 de nível 7, idêntico ao que `ferramentas/gerar-casca-fatos.py` recalcula hoje; e a seção de cobertura serve 15 modelos que respondem, 12 vazios e 116 de 168 combinações, idêntico a `dados/cobertura-r1.json`. O defeito latente nomeado no `ESTADO.md` (`robometria_casca_numeros()` lendo option de `publicar=false`) **continua latente e ainda não disparou** — os números no ar estão certos hoje.
- **Registro de receita (não é defeito, não conserte por conta disso):** a ilha está no ar com quatro páginas de conteúdo e **nenhum link de loja em nenhum cartão** — todo cartão diz "Link de loja em breve", nas duas ferramentas. Nenhum equivalente tem link, então não há caso de "topo sem link com equivalente que tem". Ilha viva sem porta de compra.
- **Achado de processo:** existia um `DESPACHO DA SENTINELA — 10/09/2026` neste arquivo, mas o cabeçalho do `ESTADO.md` estava com `ultima_ronda: null` — a ronda de 10/09 não gravou a data. A edição 2 deste despacho fecha isso.

## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 10/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O item 0 saiu daqui em 10/09/2026, cumprido** (a procedência era a única porta de compra da R1; virou a quinta decisão de desenho do bloco 4, abaixo). **Restou só a metade humana do item 1**, e ela não é da Fundação.

1. ~~**Os sitemaps respondem HTTP 404 com XML válido no corpo.**~~ **METADE DE CÓDIGO CUMPRIDA em 10/09/2026, 15h49Z** (casca 1.0.1, manifest revisão 9). A causa era a própria casca mandar "Hello world!" para a lixeira: sem nenhum post publicado, a consulta principal das rotas `index.php?sitemap=…` volta vazia e o `handle_404()` do núcleo carimba 404 antes de o XML sair. Consertado pelo filtro `pre_handle_404`, que só age em requisição de sitemap. **Medido no ar:** `wp-sitemap.xml` e `wp-sitemap-posts-page-1.xml` devolvem **200**, `/pagina-que-nao-existe-mesmo/` continua **404** (o conserto não vazou), e `wp-sitemap-posts-post-1.xml` segue 404 porque esta ilha não tem post nenhum — de propósito, e ele não está no índice.
   **CUMPRIDO E CONFERIDO EM 16/09/2026.** Medido no Search Console, propriedade `sc-domain:robometria.com.br`, aba Sitemaps: `https://robometria.com.br/wp-sitemap.xml` é Índice de Sitemaps, enviado em 10/09/2026, **última leitura em 15/09/2026, status PROCESSADO, 9 páginas encontradas, 0 vídeos**. O "Não foi possível buscar" de 10/09 era o estado normal de domínio recém-certificado e se resolveu sozinho em cinco dias — ninguém precisou reenviar nada. **A lição, e ela vale para toda ilha nova:** "não foi possível buscar" em sitemap de domínio novo NÃO é defeito, é espera; o erro foi carregar isso como pendência humana durante seis dias sem voltar para medir. Antes de abrir despacho de metade humana, meça de novo.

   **O que isso destrava:** a rampa da seção 14 dependia desta medição. A leva de malha (bloco 5b) deixa de estar bloqueada por falta de sitemap lido.

   **O que ainda NÃO existe, e é diferente de sitemap:** na mesma visita, a aba Indexação das páginas respondeu "Dados em processamento: volte em mais ou menos um dia" — a propriedade é de 09/09 e ainda não tem série de indexação. Sitemap lido não é página indexada. Só depois que essa aba trouxer número é que a rampa da 14 tem dado para decidir tamanho de leva.

## DESPACHO DO RAPHAEL — 14/09/2026 — O PISO DE BUSCA — **CUMPRIDO E CONFERIDO NO AR EM 14/09/2026, 15h**

Fechado pela execução das 15h17Z, item por item, e o que ele achou pelo caminho está registrado abaixo porque muda o que a próxima execução precisa saber.

**Item 1 — a URL de busca crua.** JÁ EXISTIA, em 65 de 65 publicáveis, e não foi duplicada. O despacho pediu o campo com o nome `afiliado.url_busca_bruta`; o contrato já tinha batizado o mesmo fato de `afiliado.url_busca_produto` na 25.4-b, e esta ilha o preencheu em 13/09. Criar um segundo nome para a mesma coisa é exatamente a cicatriz que a R2 pagou de manhã — duas metades que nunca se falam, cada uma certa no seu lugar. **Fica valendo o nome do contrato.**

**Item 2 — `degrau: 4` e `conferido_em`.** Gravados nos **65** publicáveis (32 peças + 33 modelos; a ronda contou só as 32 do `pecas.json`). O degrau sai derivado do próprio campo em `ferramentas/gerar-busca-de-produto.py`, nunca digitado, e `conferido_em` só é reescrito quando o degrau muda — carimbar a data de hoje a cada passada faria o campo dizer "conferido hoje" sem que nada tivesse sido conferido. **A régua do validador estava INVERTIDA e foi reescrita:** ela dizia "degrau sem ficha não parou em lugar nenhum", o que contradiz a própria 25.1, cujo degrau 4 é a busca e por definição não tem ficha.

**Item 3 — `intestavel`.** Nasceu como campo DERIVADO (há `url` e não há `url_produto`), e hoje é `false` em 65 de 65, porque nenhum item tem link encurtado. Como o mundo não existe no banco, a mutação o PRODUZ.

**Item 4 — o piso na tela. Era aqui que estava o trabalho.** A frase proibida saiu de **cinco** lugares (a casca, a R1, a R2, o A1 e o A2) e de uma seção inteira da `/divulgacao-de-afiliados/` que existia para explicá-la ao leitor. A porta de compra passou a descer a escada da 25.1 e parar no primeiro degrau que servir. **A busca crua sai SEM `rel="sponsored"`**: ninguém paga por aquele clique, e a página de divulgação passou a dizer ao leitor qual link rende comissão e qual não rende.

**Item 5 — os números, contados e nomeados:** 65 publicáveis, 65 com piso, **0 sem saída de compra**, 65 com saída que não rastreia (esperando só o encurtamento da 25.6), 0 com ficha de produto, 0 intestáveis, 0 com `url_produto`.

**O QUE ESTE DESPACHO ACHOU E NÃO PEDIA, e é a parte que importa para as outras ilhas:** o desembarque desta ilha parava no **cache do hospedeiro**. Ver o item 1 do despacho da Sentinela, reescrito acima.

## DEFINIÇÃO DE PRONTA — PRAZO 23/09/2026 (dado pelo Raphael em 16/09/2026)

[stated] Ele disse: "robometria deve estar pronta em no maximo 7 dias". Esta ilha é a única em foco (`foco.md`), então recebe todas as execuções da Fundação e o teto semanal inteiro de geração de link.

**Esta seção manda sobre a FILA DE BLOCOS.** A fila abaixo é aberta por natureza — "expandir o banco" não tem fim. A partir de agora, bloco que não fecha um dos cinco itens desta lista NÃO é executado antes dos que fecham. Quando os cinco estiverem fechados, a ilha é declarada PRONTA no `ESTADO.md` (`estado: viva`) e a fila volta a valer normalmente.

1. **PORTA DE COMPRA EM TODO ITEM PUBLICÁVEL.** Nenhum cartão com "Link de loja em breve". Todo item publicável com saída de compra pela escada da 25.1, parando no primeiro degrau que servir, e o aviso de comissão visível na página. `rel="sponsored"` **só** no link que rende comissão (ficha ou busca encurtada); a busca crua sai sem ele, e o cartão diz qual é qual. **Pronto quando:** uma varredura das páginas no ar não encontra a frase "em breve", não encontra item publicável sem saída, e a página de divulgação declara as duas contas — quantos itens têm saída e quantos rendem comissão. *(A meta de receita — os 68 com `url_busca` encurtada — continua existindo, mas como **dívida do elo da Shopee**, não como critério de PRONTA, porque ela não depende da Fundação.)*
   *(Corrigido em 16/09/2026 pelo achado G2 do Pente Fino: a versão anterior deste item, escrita nesta mesma manhã, exigia carimbar de patrocinado 68 links que ninguém paga — afirmação falsa ao Google e ao leitor.)*
   **— FECHADO em 16/09/2026, medido no ar (revisão 52).** `conferir-no-ar.py`: zero ocorrência de "em breve" nas 9 URLs, zero item sem saída, 229 afirmações e 0 falha. A página de divulgação passou a declarar **as duas contas**: 73 itens publicáveis, **68 rendem comissão** e 5 não. *(A segunda conta ESTAVA FALSA no ar até esta execução, e é o achado: ela vinha de `com_link`, que conta FICHA de produto, e a página a apresentava como "quantos rendem comissão". Os dois foram o mesmo número enquanto a única alternativa à ficha era a busca crua, que não rende nada; com os links encurtados de 16/09 a página passou a dizer ao leitor que NADA rendia comissão enquanto 68 links rendiam e saíam com `rel="sponsored"`. **Subdeclarar relação paga é tão errado quanto superdeclarar** — as duas descrevem a relação errado, e a página de divulgação é o pior lugar possível para isso. A conta passou a ser a da ESCADA: rende quem tem ficha OU busca encurtada.)* Os **5 que não rendem** são os modelos Xiaomi sem canal brasileiro que entraram hoje, e o encurtamento deles depende da sessão do painel da Shopee (25.6) — **dívida do elo, não critério de PRONTA**, como o próprio item já dizia.
2. **A EMENDA DO FUNIL FECHADA — FECHADO EM 18/09/2026, 10h32Z, COM A INTERSECAO EM 15.** `cobertura-r1.py --gravar` mede **15 modelos publicaveis atendidos pelas DUAS ferramentas**, em 45 publicaveis, e a medicao esta commitada em `dados/cobertura-r1.json`: `positivo-pra2000`, `positivo-pra800`, `roborock-q8-max`, `roborock-qrevo-curv`, `roborock-qrevo-master`, `roborock-s8-maxv-ultra`, `roborock-saros-z70` e os oito Xiaomi. **A meta era 15 e nao foi arredondada para chegar la** — os quatro que entraram hoje tem os TRES campos, um por um, com procedencia e data. O TETO, que era 13 e limitava a propria meta, foi para **17**.
   **A PORTA FOI A MESMA QUE O REGISTRO DE 17/09 DEIXOU ESCRITA, e ela nao pedia marca nova:** mais modelos da Roborock no canal brasileiro. **Esse canal esta agora VARRIDO INTEIRO e nao precisa ser reprocurado:** ele publica **seis** robos — Q8 Max, Qrevo Master, Qrevo Curv Series, S8 MaxV Ultra, Saros 10R e Saros Z70 —, e os seis estao no banco. **O `Q7 Max`, que o registro anterior apontava como alvo, NAO EXISTE no canal brasileiro**; o `F25 Combo Series` existe e e aspirador umido-seco, nao robo.
   **O QUE ENTROU SEM CONTAR, e esta dito para ninguem reprocurar:** o **Saros 10R** entrou com `pa_declarado: null` — TRES passadas, uma delas pedindo o valor em Pa com todas as letras, devolveram sempre "potencia de succao lider do setor" sem numero. E **recusa editorial do fabricante neste modelo**, nao lacuna de coleta, ja que as outras cinco paginas da mesma marca declaram o numero. Sem Pa ele nao e recomendavel pela R2 e portanto nao conta na intersecao nem no teto.
   *(O texto anterior deste item, com a regua, o teto de 13 e as cinco remedicoes de 17/09 que o levaram de 8 a 11, fica abaixo como historia do que foi medido. A regua NAO foi afrouxada para fechar: continua exigindo `pa_declarado` E `canal_brasileiro` na R2.)*

   **O TEXTO ORIGINAL, para quem quiser conferir o que foi pedido:** 2. **A EMENDA DO FUNIL FECHADA.** A pessoa chega pela R2 e volta pela R1 sem encontrar. É o defeito estrutural que esta ilha já mediu sozinha. Pronto quando: `cobertura-r1.py --gravar` mostrar pelo menos **15** modelos publicáveis atendidos pelas duas ferramentas, e a medição estiver commitada. **A RÉGUA DESTE ITEM MUDOU EM 16/09/2026, e o número não andou: 38 modelos publicáveis, dos quais 8 atendidos pelas duas.** Até hoje o cruzamento contava como "a R2 responde" todo modelo com `pa_declarado`. A R2 passou a exigir também **canal brasileiro** (ver o bloco do portão, abaixo), e a régua mudou junto — porque **régua que mede a meta não pode ser mais frouxa que a ferramenta que a meta descreve, senão a meta se fecha sozinha**. Concretamente: os cinco modelos Xiaomi que entraram hoje têm Pa declarado e peça declarada, e contariam +5 na interseção pela régua antiga, sem que UMA pessoa a mais fosse atendida — a Xiaomi Brasil não os vende. A forma mais barata de chegar a 15 seria despejar modelos globais no banco, e essa porta está fechada. *(Linha de base anterior, medida pelo Pente Fino na mesma manhã: 33 publicáveis, 8 pelas duas — `positivo-pra2000`, `positivo-pra800`, `xiaomi-e10`, `xiaomi-h40`, `xiaomi-s10`, `xiaomi-s20`, `xiaomi-s40`, `xiaomi-s40c`, os mesmos oito de hoje.)* *(Este item dizia "das 28 entradas publicáveis, só 3" — os dois números são a varredura de 13/09/2026 e envelheceram com a leva do Xiaomi S10 de 14/09. A meta de 15 não foi tocada: ela é absoluta e continua de pé.)*
   **— MEDIDO EM 17/09/2026, 10h32Z: ESTE ITEM ESTÁ BLOQUEADO POR REDE, E O BLOQUEIO NÃO É DA FUNDAÇÃO.** As duas únicas portas que o próprio `PROMPT.md` nomeia para mexer neste número exigem sair para o fabricante, e **as cinco saíram 403 do proxy de egresso** nesta execução, uma por marca: `mais.conteudo.wap.ind.br` (os manuais em PDF do item (c), que tirariam W400, W1000 e W310 do vazio duplo), `www.electrolux.com.br`, `www.mi.com.br`, `loja.positivotecnologia.com.br` e `www.multilaser.com.br`. Não é intermitência: `connect_rejected`, *gateway answered 403 to CONNECT (policy denial)*, nas cinco, na mesma passada — a lista de "Domínios permitidos" do ambiente de nuvem tem os domínios das **ilhas** e mais nada (seção 20.1 do contrato). A API da Shopee, que é a fonte que esta nuvem alcança, **já foi medida e não serve**: ela traz foto, ficha e link, e não traz `pa_declarado` nem `canal_brasileiro`, que são exatamente os dois campos que a interseção conta. **O que destrava, e é uma linha de configuração do Raphael, não um bloco:** acrescentar os cinco domínios à lista de permitidos do ambiente, pela 20.3 — quem exige a fonte confere se a fonte está liberada. Enquanto isso não acontecer, nenhuma execução da Fundação move este número de 8, e o placar deve dizer **bloqueado por rede**, nunca "faltando" — porque "faltando" sugere trabalho que existe.*

   **— REMEDIDO EM 17/09/2026, 13h20Z, E AS DUAS METADES DO PARAGRAFO ACIMA PRECISAM SER LIDAS SEPARADAS. A METADE DA REDE ESTA CERTA; A CONCLUSAO 'NENHUMA EXECUCAO MOVE ESTE NUMERO DE 8' ESTAVA ERRADA, E ELE FOI PARA 9 NESTA EXECUCAO.** O egresso direto continua fechado e foi remedido: `000` com `connect_rejected` em `www.mi.com`, `mi.com`, `loja.positivotecnologia.com.br`, `www.positivotecnologia.com.br`, `loja.wap.ind.br` e `www.wap.ind.br`, DUAS passadas em cada um, com `robometria.com.br` em 200 na mesma janela, e `WebFetch` de `www.mi.com` devolvendo `EGRESS_BLOCKED`. **O que faltou medir foi o SEGUNDO canal:** a busca restrita ao dominio do fabricante alcanca os mesmos enderecos, que e a descoberta de 12/09 escrita em "Especifico desta ilha" e que fez entrarem as levas Xiaomi de 13 e de 14/09. Foi por ela que os cinco consumiveis do Mi Robot Vacuum-Mop 2 entraram hoje, do artigo de suporte KA-11406 da propria Xiaomi. **Egresso fechado nao e coleta bloqueada** — antes de escrever "bloqueado por rede" nesta ilha, meça OS DOIS canais, que e o que o proprio `PROMPT.md` ja manda tres paragrafos acima.

      **— REMEDIDO EM 17/09/2026, 16h16Z: A INTERSECAO FOI PARA 10 E O TETO PARA 12, E O CAMINHO ESCRITO AS 13h16Z FUNCIONOU NA PRIMEIRA TENTATIVA.** Entrou o **Mi Robot Vacuum-Mop 2 Lite** com os TRES campos que a intersecao conta — Pa declarado (2.200), canal brasileiro (`mi.com/br`) e cinco pecas declaradas pelo fabricante (KA-11405). Modelo novo com os tres campos sobe a intersecao **e** o teto no mesmo movimento, que e o que peca nova nunca faz. **O que a mesma varredura mediu e NAO entrou, dito para ninguem reprocurar:** (i) o **Mi Robot Vacuum-Mop** (original) tem pagina em `mi.com/br` e artigo de suporte proprio (KA-07584), mas o Pa voltou em UMA passada so e **qualificado por variante** ("2500 Pa suction (for the Visual Navigation Version)") — a segunda passada nao o devolveu, e numero de variante lido como numero do modelo e a familia do erro do S20; ele volta quando uma segunda passada limpa disser o numero sem a qualificacao. (ii) **X10, X20 e E5 nao foram confirmados em `mi.com/br`** em duas passadas — a lista de robo aspirador do canal brasileiro devolve E10, S10, S20, S40, S40C, H40, Mop 2, Mop 2 Lite e Mop, e mais nada. **O caminho para 15 continua sendo modelo novo com os tres campos, e o canal brasileiro da Xiaomi acabou de ser varrido inteiro** — o proximo modelo com os tres campos tera de vir de OUTRA marca, ou da Xiaomi por um canal que esta varredura nao alcancou.

         **— REMEDIDO EM 17/09/2026, 19h16Z: A INTERSECAO FOI PARA 11 E O TETO PARA 13, E A PORTA NOVA E UMA MARCA, NAO UM MODELO.** Entrou o **Roborock Q8 Max** com os TRES campos — Pa declarado (5.500), canal brasileiro (`br.roborock.com/pages/q8-max-plus`) e peca declarada pelo fabricante (o pano, cujo titulo na loja oficial nomeia a 'Q8 Max Series'). **E o PRIMEIRO modelo nao-Xiaomi do banco acima de 3.000 Pa**, que era a urgencia numero 1 escrita na `lista_de_compras` desde 13/09: entre os RECOMENDAVEIS, a faixa acima de 3.000 Pa passou de 5 modelos de UMA marca para 6 de DUAS, e o cartao do Roborock e o primeiro da vitrine servida na situacao de pelo. **O caminho para 15 mudou de forma, nao de natureza:** continua sendo modelo novo com os tres campos, mas a porta que acabou de se abrir nao e marca nova e sim MAIS UM MODELO DESTA — a varredura devolveu Q5, Q7, Qrevo, S8, Saros e F25 no mesmo canal brasileiro, nenhum deles no banco. **O que a mesma varredura mediu e NAO entrou, dito para ninguem reprocurar:** (i) o 'Washable Filter*2', cujo titulo nomeia o Q8 Max, so veio na PROSA do resumidor — a passada cuja consulta nao dizia 'Q8' devolveu um titulo so com modelos Q7, e eco da pergunta lido como declaracao do fabricante e a armadilha desta ilha quando o canal e busca; (ii) o 'Side Brush*2' nomeou 'Q8 Max' numa passada e so 'Q8 Max+' na outra, e variante lida como modelo e a familia do erro do S20. Os dois voltam com uma segunda passada limpa. **E a Positivo, que o registro das 16h16Z apontava como alvo mais provavel, esta FECHADA: o canal dela publica tres robos — PRA2000, PRA800 e o Wi-Fi+ —, e os tres ja estao no banco.**

**E O TETO DESTA META E 13, NAO 15 — MEDIDO, NAO ESTIMADO, E ELE SUBIU DUAS VEZES EM 17/09.** A intersecao conta modelo atendido pelas DUAS ferramentas, e a R2 so responde com `pa_declarado` **E** `canal_brasileiro`: sao **13** modelos com os dois campos, em 40 publicaveis. **Logo a intersecao nao passa de 13 por mais peca que entre no banco.** Dos 13, **11 ja estao atendidos**; os 2 que faltam sao `positivo-pra500` e `wap-w400`, e os dois foram medidos hoje como **recusa de fabricante** e nao como coleta pendente — a Positivo publica acessorio de duas familias e nenhuma nomeia o "Wi-Fi+" (duas passadas), e a loja da WAP nao tem pagina de peca para o W400 (medido em 14/09 e nao remedido hoje). **O caminho para 15 e MODELO novo com os tres campos — Pa declarado, canal brasileiro e peca declarada —, nunca peca nova.** Enquanto este item falar so de peca, ele pede uma coisa que o banco nao pode dar; enquanto o placar disser "bloqueado por rede", ele esconde um trabalho que existe e que a busca alcanca. *(Os numeros deste paragrafo diziam 11, 9 e 38 quando foram medidos as 16h16Z e foram remedidos as 19h16Z, com a entrada do Roborock Q8 Max: 13, 11 e 40. Os dois modelos que faltam para o teto sao os MESMOS, e continuam sendo recusa de fabricante. A meta de 15 nunca foi tocada — o que mudou e que o teto deixou de estar abaixo dela por dois, e passou a estar por um.)*
3. **[RAPHAEL] ZERO DEFEITO ABERTO DE RONDA.** Nenhum **defeito** pendente nos despachos da Sentinela dentro deste arquivo. Pronto quando: as seções de despacho não tiverem DEFEITO sem "CUMPRIDO E CONFERIDO NO AR".
   **O QUE CONTA E O QUE NÃO CONTA, corrigido em 17/09/2026 porque a régua anterior não podia fechar nunca.** Conta **defeito**: coisa que está errada no ar, ou dívida que alguém precisa pagar. **Não conta** item que o próprio despacho classifica como *nada a fazer agora* — proposta de aceleração que pede "registro e vigilância", ou que espera medição da leitura semanal seguinte, ou que depende do relógio de indexação do Google. Esses itens estão funcionando exatamente como foram desenhados; contá-los como pendência deixa o placar permanentemente vermelho por causa de anotações saudáveis, e placar que nunca fecha é placar que ninguém olha. Na prática, em 17/09/2026 isso tira da conta as **propostas 1 e 3** da leitura semanal de 16/09, que dizem com todas as letras que a leitura SEGUINTE é quem mede.
4. **SITEMAP ACEITO NO SEARCH CONSOLE.** Hoje está em "Não foi possível buscar". É metade humana e está no despacho de 10/09. Pronto quando: a propriedade `sc-domain:robometria.com.br` mostrar o sitemap lido, com contagem de URLs. **— FECHADO em 16/09/2026: processado, última leitura 15/09, 9 páginas encontradas.**
5. **TODA PÁGINA COM `<meta name="description">` E TAGS `og:`.** Defeito levantado na ronda de 11/09. Pronto quando: varredura das páginas no ar não achar nenhuma sem os dois. — **JÁ ATENDIDO. Medido no ar pelo Pente Fino em 16/09/2026: 9 de 9 URLs do sitemap em HTTP 200, todas com `<meta name="description">` e com cinco propriedades `og:` (`og:title`, `og:type`, `og:url`, `og:description`, `og:locale`).** *(O defeito de 11/09 é o item 1 daquela ronda, e o próprio arquivo o registra cumprido em 11/09/2026, poucas linhas acima — este item nasceu descrevendo o mundo anterior. Quem fechar o placar reconfere e marca feito; nenhum bloco precisa ser gasto nele.)*

**QUEM É DONO DE CADA ITEM.** Item marcado **[RAPHAEL]** não é da Fundação e nenhuma execução dela consegue fechá-lo — o placar obrigatório deve dizer "esperando o Raphael", nunca "faltando". Hoje o item 3 está nessa condição: as três pendências que sobram nas seções de despacho deste arquivo se declaram dele (o encurtamento na Shopee e as duas linhas do despacho da Sentinela de 14/09). O prazo de 23/09 continua de pé; o que esta marcação muda é de quem é cada item, para a Fundação não gastar execução olhando para um vermelho que não é dela.

**O QUE "PRONTA" NÃO SIGNIFICA, escrito para ninguém se iludir com o prazo:** pronta é a ilha completa e capaz de faturar — não é a ilha faturando. Indexação e posição são relógio do Google, não nosso: dias para indexar, semanas para posicionar. Cumprir os cinco itens até 23/09 é a nossa parte, e é a única parte que depende de nós.

**Em toda execução, o relatório final abre com o placar dos cinco itens**, cada um com feito ou faltando e o número medido ao lado. Sem placar, a execução não fechou.

## O PORTÃO DO CANAL BRASILEIRO — nasceu em 16/09/2026, e ele decide o que a R2 recomenda

**A regra, e ela cabe numa frase:** a R1 responde a quem JÁ TEM o aparelho, então a compatibilidade declarada pelo fabricante vale onde o aparelho estiver; a R2 recomenda uma **compra** a um leitor brasileiro, então modelo sem canal brasileiro não é recomendação — é um beco. São duas perguntas diferentes e o banco passou a responder as duas separadamente, pelo campo `canal_brasileiro` (esquema versão 8).

**Canal brasileiro é endereço do FABRICANTE, e marketplace não serve.** Todo código tem busca em marketplace, então aceitar marketplace faria o portão aprovar tudo — e voltar a ser o que era antes de existir. O validador reprova.

**Por que ele nasceu, e é a parte que vale para as outras ilhas:** até 16/09 a elegibilidade da R2 pedia `status: publicavel` e `pa_declarado`, e mais nada. A lista saía certa mesmo assim, porque as cinco marcas coletadas eram todas de canal brasileiro — **verdade por coincidência da coleta**. E o contraexemplo já estava DENTRO do banco desde 13/09: cinco códigos Xiaomi (E10C, E12, S12, S40 Pro, X20) que as páginas de acessório do próprio fabricante declaram e que a Xiaomi Brasil não lista. Um deles declara **15.000 Pa**, a maior sucção do banco inteiro: sem o portão, o primeiro nome da lista em toda situação de pelo — a consulta que mais vende no nicho — seria um aparelho que o leitor não compra aqui.

**O portão não mudou UMA linha da tela**, e é por isso que a bateria `ferramentas/mutacoes-canal-brasileiro.py` existe: trava que nasce sem mudar nada é trava que ninguém sabe se existe. As 5 mutações reprovam, inclusive a que produz o mundo em que as duas metades da R2 erram juntas.

**O que ele custa, dito com o número na mesa:** 6 dos 38 modelos publicáveis ficam fora da recomendação — `electrolux-erb20` (que entrou no banco só por agregador de manual, sem página da Electrolux Brasil) e os cinco Xiaomi. A página **diz isso ao leitor**, com os nomes e com os 15.000 Pa, porque portão que só anuncia o que protege e nunca o que custa é portão que ninguém consegue discutir.

## A ESCADA DE COMPRA SE MEDE INTEIRA, NUNCA POR UM DEGRAU (16/09/2026)

**QUATRO réguas desta ilha reprovaram no mesmo dia por medir um degrau da 25.1 em vez da escada**, e as quatro reprovaram uma página que tinha **melhorado**: `teste-r1.php`, `teste-a1.php`, `teste-r2.php`, `teste-a2.php` e a seção 11 do `conferir-no-ar.py` exigiam `rbm-comprar-cru > 0` — isto é, exigiam que a vitrine saísse pelo degrau 4, a busca CRUA. Quando os links de busca encurtada entraram, as páginas subiram para o degrau 3 e as réguas acharam zero onde esperavam quatro.

**Quando quatro réguas erram igual no mesmo dia, o erro não é de nenhuma delas:** é de terem sido escritas quando só existia um degrau alcançável, cada uma sem saber das outras. A afirmação que interessa nunca foi "quantas buscas cruas" — é **"o bloco de compra nunca fica vazio"**. Todas passaram a medir isso e a IMPRIMIR o degrau ao lado, que é como se vê o encurtamento avançando sem precisar de outra medição.

**Régua nova desta ilha nasce medindo a escada.** Se ela precisar do degrau, ela o imprime; se ela o exigir, ela reprova a subida.

## FILA DE BLOCOS

**1. LEVANTAMENTO DE BUSCAS PARAMÉTRICAS.** Consultas reais do nicho no Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta a consulta (autocomplete, buscas relacionadas, fórum, YouTube). Grave em `dados/corpus-buscas.md`. Separe explicitamente o eixo de **compatibilidade** (peça × modelo) do de **dimensionamento** (Pa, m², autonomia). Não depende de site nem de domínio.

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. As duas ferramentas âncora prováveis: (a) localizador de peça compatível por modelo; (b) dimensionador de sucção e autonomia por área, tipo de piso e pelo. Saída é sempre **faixa com critério e fonte**, nunca número seco.

**3. MODELO DO BANCO.** Entidades: **MODELO DE ROBÔ** (marca, linha, Pa, autonomia em minutos, tipo de navegação, voltagem, base de autoesvaziamento sim/não) · **PEÇA** (tipo, código do fabricante, modelos compatíveis, vida útil declarada) · **MARCA**. O campo `imagem` entra desde já (seção 6 do `ARQUIPELAGO.md`) — a Aquametria descobriu tarde que o banco não tinha e travou a vitrine.

**3b. CASCA DO SITE — ENTREGUE em 10/09/2026** (`snippets/robometria-casca.php` v1.0.0,
manifest na revisão 7). Identidade sobre o tema ativo, logo SVG do encaixe, menu hambúrguer
acessível, favicon próprio, JSON-LD Organization + WebSite, e **cinco** páginas — início,
ferramentas, metodologia, sobre e divulgação de afiliados (esta última nasceu junto porque
o aviso de comissão precisa estar publicado antes do primeiro link, não depois).

**3b ENTREGUE E NO AR em 10/09/2026, 14h11 UTC.** Sync acionado pela nuvem: `/status` responde
**revisão 7**, snippet `robometria-casca` aplicado (#6), a home serve o título da ilha, o sitemap
de páginas lista início, ferramentas, metodologia, sobre e divulgação-de-afiliados, e o sitemap
de posts está vazio ("Hello world" saiu). Próximo bloco da fila é o 3c.

**Antes de mexer na casca, rode `php ferramentas/teste-casca.php .`** — 59 medições, sem
site e sem rede, e é a verificação da seção 8 que esta ilha consegue executar **sem** tocar o
site. *(Esta linha dizia "a nuvem não alcança robometria.com.br" — falso desde 10/09/2026, e
contradito pela própria seção "Endpoints desta ilha" acima e pelo bloco 3b logo abaixo, que
registra o Sync acionado pela nuvem. Corrigido pelo Pente Fino em 14/09/2026.)* Ele confere o que a seção 8 pede e mais a
identidade: paleta fechada, nenhum gradiente, a varredura ausente do corpo porque é cor de
sinal, e **cada número da tela conferido contra o banco commitado** — quem expandir o banco
e não atualizar o instantâneo da casca vê o teste reprovar em vez de o site publicar número
que o repositório não sustenta. Na primeira rodada ele já pegou o nome da superglobal de
servidor escrito dentro de um *comentário*, que o ModSecurity casa do mesmo jeito e faria a
gravação falhar em silêncio no wp-admin.

**3c. EXPANDIR O BANCO — não depende de site.** O modelo já existe e o
`ferramentas/validar-banco.py` já reprova o que estiver fora do contrato; o que falta é
cobertura. **A urgência não é número de itens** (a seção 14.3 do `ARQUIPELAGO.md`
descartou meta redonda): é faixa descoberta. Produto novo entra com `afiliado.url`
presente e vazio, e a execução reporta quantos itens esperam link.

A primeira leva do 3c (09/09/2026) fechou as lacunas (c) e (d) da ordem original. A
**segunda leva (09/09/2026, 23h16Z) fechou a lacuna do `pa_declarado`**: de 2 para **11
modelos publicáveis**, em 3 marcas, de 1.400 a 10.000 Pa — a R2 deixou de sair vazia.

A **terceira leva (10/09/2026, 11h17Z) varreu a entrada da R1**, que nunca tinha sido
varrida, e o resultado **reordenou esta lista**. A medição está em
`dados/cobertura-r1.json` e se refaz sozinha com
`python3 ferramentas/cobertura-r1.py --gravar`. **A ordem que vale agora, da maior para a
menor:**

(a) **PEÇAS COM CÓDIGO DA XIAOMI E DA WAP — a urgência número 1, e ela só apareceu no
cruzamento das duas varreduras.** Esta linha estava em ÚLTIMO lugar até 10/09/2026.
**ATUALIZAÇÃO 13/09/2026, segunda leva do dia — o lado WAP foi aberto e a linha MUDOU DE
NATUREZA.** A R1 saiu de 20 para **22** modelos que respondem e o vazio caiu de 13 para
**11**: W300 e WSMART entraram com 4 escovas. O que falta **não é mais achar a página** e
**não é rede** — a busca alcança a loja e o blog da WAP. Falta (i) o **código** da ficha,
que a busca não devolve (só o título e a URL), e (ii) a **função** da escova nos modelos de
escova única, que a seção 26 do `ARQUIPELAGO.md` proíbe ler do nome. Os dois se resolvem
pelo mesmo lugar: os manuais em PDF do item (c). Detalhe por alvo em
`dados/pecas.json` → `lista_de_compras`. **Sobram W400, W1000, W310 e W90 no vazio da
marca**, e o W90 é recusa medida, não lacuna de procura.
Medido: das 28 entradas publicáveis, só **3** são atendidas pelas DUAS ferramentas da
ilha. A R2 atende 8 modelos (Xiaomi, WAP, PRA500) em que a R1 sai **vazia**; a R1 atende
12 (Electrolux, Multi) em que a R2 sai vazia. **O funil está partido na emenda:** a ilha
ganha a visita pela R2 ("quantos Pa para pelo de cachorro"), a pessoa compra, volta meses
depois procurando o filtro daquele robô — que é a consulta de maior intenção de compra do
nicho e a razão de a R1 existir — e recebe "não localizamos declaração do fabricante".
Este é também o único lado **coletável** da emenda: o lado simétrico (Pa da Electrolux e
da Multi) já foi medido como inexistente no mercado brasileiro.
(b) **FAIXA DESCOBERTA E CONCENTRAÇÃO DE MARCA na R2.** Medição em
`cobertura_de_faixa_r2`, dentro de `dados/modelos-robo.json`: acima de **6.000 Pa** só
existem 2 elegíveis (o portão da seção 9 pede 3), e **toda faixa acima de 3.000 Pa é 100%
Xiaomi** — inclusive a de pet, que é a que vende. Não se conserta afrouxando
elegibilidade: conserta-se achando Pa de **outra marca** nessa faixa. Continua sendo
trabalho de verdade; caiu para segundo porque (a) rende nas duas ferramentas de uma vez e
(b) só rende numa.
(c) **MANUAIS EM PDF DA WAP — a melhor porta de entrada para o NÍVEL 2 da escada de
fontes.** A WAP publica um manual por modelo em `mais.conteudo.wap.ind.br`, com revisão e
data no nome do arquivo. Hoje o domínio devolve `EGRESS_BLOCKED`; no dia em que abrir,
esses PDFs sobem o banco inteiro da marca de nível 3 para nível 2 de uma vez, trazem o Pa
dos modelos que a loja declara só como "três modos de sucção" **e**, pela varredura da
R1, são a chance de tirar W400, W1000 e W310 do vazio duplo. Toda a ilha está em nível 3
ou 4 — nenhuma fonte de nível 2 ainda.
(d) **pares (minutos, m²): a lacuna mudou de natureza e NÃO é mais coleta.** Ficou medido
que Xiaomi, WAP, Multi e Positivo **não declaram m² em canal nenhum** — só a Electrolux
declara. Não adianta procurar mais: o número não está publicado. A
`taxa-cobertura-m2-por-min` continua `pendente` e **proibida em fórmula**, e a recusa
virou conteúdo: a R2 mostra os minutos, diz que o fabricante não declara área e explica
por que não chuta.

(e) ~~**A RECARGA DOS MODELOS QUE JÁ DECLARAM COBERTURA.**~~ **FECHADO em
12/09/2026, e NÃO por coleta: a lacuna mudou de natureza, como a dos m² no item
(d).** Nenhuma página de modelo declara tempo de carga (conferido no ERB60 e no
ERB80). O único número que a Electrolux publica no canal alcançável está num
artigo de **família** — 24 h na primeira carga, 5 h nas seguintes — e esse mesmo
artigo declara, **na mesma frase**, autonomia de 90 minutos, que não é a de
nenhum dos cinco (100, 100, 100, 100 e 120). O artigo fala de outro aparelho.
Os cinco `motivo_do_null` agora carregam essa causa, com o nome do documento. O
caminho de volta é a leitura direta do manual de cada modelo, que segue atrás do
egresso fechado. **O texto original fica abaixo, porque a medição que o derrubou
só faz sentido ao lado da expectativa que ele criou:**

(e-original) **A RECARGA DOS MODELOS QUE JÁ DECLARAM COBERTURA — o item de MENOR custo e
MAIOR retorno que a varredura da R2 encontrou, e ele não existia nesta lista até
11/09/2026.** Medido: a fórmula do tempo real da especificação precisa de TRÊS
números declarados — cobertura por carga, autonomia e recarga — e **nenhum dos 28
modelos publicáveis tem os três**. Os 5 da Electrolux declaram cobertura e
autonomia e calam a recarga; o Xiaomi S20 e o Positivo PRA2000 declaram recarga e
calam a cobertura. **Um campo, em cinco modelos de uma marca só, destrava a frase
que é a razão de a R2 existir** — "a sua casa fica pronta em X minutos" — e ela
hoje sai pela metade, dizendo que o total depende de um número que ninguém
publica. Não é lacuna de mercado como a dos m²: a recarga é dado de manual, e a
Electrolux publica manual.

**O EGRESSO DIRETO A ESSES DOMÍNIOS SEGUE FECHADO, E ISSO NÃO BLOQUEIA O 3c.** Medido em
11/09/2026: `mi.com.br`, `xiaomi.com.br`, `wap.ind.br` e
`mais.conteudo.wap.ind.br` devolvem `000` — só os domínios das ilhas respondem.
*(O texto que ficava aqui mandava testar esses endereços com `curl` e dar o 3c inteiro por
bloqueado se eles falhassem. Foi exatamente isso que parou a coleta desta ilha por três dias:
o banco sempre citou `www.mi.com/br`, e a busca alcança. A seção 4 do `ARQUIPELAGO.md` virou
regra a partir deste caso — **o endereço que se testa sai do BANCO, do campo `url` da fonte
que se quer reler, nunca da prosa que descreve o bloqueio** —, e o registro de 13/09 mais
abaixo neste mesmo arquivo já dizia o contrário desta linha. Corrigido pelo Pente Fino em
14/09/2026.)*
**Antes de escolher um alvo do 3c:** abra o registro que você quer melhorar, copie o endereço
do campo `url` dele, e teste **esse**. Teste também os **dois canais**, que são redes
diferentes — egresso direto (`curl`/`WebFetch`) e canal de busca —, como manda o item
"O EGRESSO DIRETO E O CANAL DE BUSCA SÃO DUAS REDES DIFERENTES" em "Específico desta ilha".
Uma falha só vira bloqueio depois de repetir na mesma execução (seções 4 e 20.2), e bloqueio
herdado do `ESTADO.md` é retestado antes de ser respeitado. Alvo cujo canal estiver
comprovadamente fechado nos dois cai para o trabalho de repositório listado em "Específico
desta ilha", que não depende de rede nenhuma — o 3c inteiro, não.

**ANTES de colher qualquer coisa para o 3c, rode `python3 ferramentas/cobertura-r1.py` e
`ferramentas/validar-banco.py`.** As duas varreduras são o que separa "acrescentei um
item" de "tirei uma entrada do vazio" — e foi contando itens, em vez de varrer, que a
lacuna da R1 ficou escondida atrás de "33 pares declarados".

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase. **Não deixe retrofit para depois** — foi o que custou dias na Aquametria.

**4 e 4e — AS DUAS FERRAMENTAS ESTÃO NO AR.** A R1 desde 10/09/2026
(`snippets/robometria-r1.php`, v1.1.1) e a **R2 desde 11/09/2026**
(`snippets/robometria-r2.php` v1.0.0, manifest revisão 12, `/status` conferido),
em `https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/`. As cinco
decisões abaixo deixaram de ser opinião e viraram o jeito desta ilha — **ferramenta
nova nasce com elas, nunca com retrofit depois:**

1. **A resposta é servida pelo SERVIDOR.** Formulário GET para a própria página, resposta
   montada em PHP. Sem JavaScript a ferramenta funciona por completo, e cada consulta tem
   a resposta inteira no HTML servido. Não repita o desenho de calculadora que só calcula
   no navegador: para um modelo de linguagem, aquilo é um formulário vazio.
2. **A regra mora na implementação de referência, e o PHP não a reescreve.**
   `ferramentas/gerar-r1.py` importa `cobertura-r1.py`, deriva os fatos para
   `dados/r1-respostas.json` (que o Sync leva para uma option) e o snippet só escreve a
   frase, acentuada. `ferramentas/teste-r1.php` compara **as 188 frases** das duas
   implementações ignorando acento: elas batem por construção, não por sorte. **A R2 tem
   que ganhar a mesma dupla**, e a referência dela ainda não existe.
3. **O caso-âncora é escolhido por regra, nunca a dedo**, e sai no HTML sem clique nenhum
   — é ele que um modelo de linguagem lê como resposta.
4. **Consulta não vira URL indexável:** `?modelo=…` sai com `noindex,follow` e canônica
   para a página limpa (seção 14.1). Domínio novo não tem orçamento de rastreamento para
   centenas de combinações.
5. **A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA, e existe antes do link**
   (v1.1.0, 10/09/2026 — item 0 do despacho, hoje cumprido). A R1 estreou com um único
   link clicável por peça, e ele ia para a loja do fabricante: a página ficou impecável
   de procedência e perfeita para a Electrolux. Agora o bloco "Onde comprar estas peças"
   vem antes, com o aviso de comissão dentro dele; a procedência é link de texto "fonte"
   com `rel="nofollow noopener"`, nunca um botão e sem fundo no CSS; e o bloco **nasce
   com a porta de compra já aberta**, descendo a escada da 25.1 e parando no primeiro
   degrau que servir — ficha (`url`), busca encurtada (`url_busca`) ou, enquanto o
   encurtamento não existir, a busca crua de `url_busca_produto`, que sai **sem**
   `rel="sponsored"` porque ninguém paga por aquele clique. Quando não há o que
   recomendar, o bloco não lista **e a página diz por quê**. `teste-r1.php` mede os
   cinco pontos (seção 13 dele), e a R2 nasce com isso, não com retrofit.
   *(Esta decisão mandava o bloco nascer "reservando o lugar com 'Link de loja em breve'",
   com o argumento — correto na época — de que esconder o bloco devolveria à procedência o
   papel de única porta clicável. A frase foi **PROIBIDA pela seção 7 do `ARQUIPELAGO.md`
   em 14/09/2026** e retirada de cinco lugares desta ilha no mesmo dia (casca 1.6.0, R1
   1.7.0, R2 1.5.0); medido no ar em 16/09/2026 pelo Pente Fino: **zero ocorrências de
   "em breve" nas 9 URLs do sitemap**. A ordem velha ficou de pé e faria a próxima
   ferramenta nascer com o defeito. Corrigido pelo Pente Fino em 16/09/2026.)*

**O QUE A R2 ACRESCENTOU À DECISÃO 2, e vale para toda ferramenta de entrada
contínua.** A entrada da R1 é uma lista fechada, então o gerador pré-calcula toda
resposta possível e o snippet vira um escritor de frases. A da R2 tem metragem
contínua de 10 a 400 m², e por isso o PHP **precisa** fazer aritmética. A regra
continua na referência e viaja como fato; a aritmética declarada o PHP faz, e a
prova de que faz igual é uma **GRADE** que o teste percorre inteira — 9 situações,
114 cartões, 200 casos de metragem. E a grade tem que incluir as **bordas**: a de
10 em 10 m² não pegava trocar `ceil` por `floor + 1`, porque 162 e 166 m² não têm
múltiplo terminado em zero. Grade que não cobre a borda é amostra com nome de grade.

**A RÉGUA DE UMA REGRA NÃO PODE MORAR NO SNIPPET SE QUEM A CONFERE É O TESTE.** A
R2 nasceu com uma função `atende( $pa, $limiar )` que respeitava o operador da
fonte, nunca era chamada na montagem da página, e só o teste chamava — para
conferir a lista que o snippet publica. Trocar o `>` por `>=` fazia as duas metades
errarem juntas e o teste passar, com um modelo que a fonte citada não cobre em
primeiro lugar numa lista de recomendação. A função saiu do snippet e a comparação
passou a ser escrita no teste, lida do operador que a fonte declara. **Função morta
num snippet publicado não é neutra: ela parece a regra, e um dia alguém a usa.**

**E o achado que só apareceu LENDO a resposta como um leitor lê:** a página se
contradizia na mesma tela, dizendo "a Electrolux declara o filtro X compatível com o
ERB60" e, na frase seguinte, "a Electrolux não vende o filtro avulso para este modelo".
"Não vende avulso" é afirmação sobre o catálogo inteiro do modelo — frase que só o
resultado inteiro sustenta não pode ser escrita olhando uma peça de cada vez. **A R2 tem
frases da mesma família** ("nenhum modelo atende a sua metragem"): escreva-as depois de
montar o resultado inteiro, não durante.

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**OS DOIS ESTÃO NO AR.** O da R2 desde 11/09/2026
(`snippets/robometria-a2.php` v1.0.0, manifest revisão 13):
`https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/`. Ele não
repete a ferramenta — a R2 calcula a casa da pessoa, o artigo conta o catálogo e
responde a pergunta anterior, de onde vem o número de m² que os sites publicam.

**A PROVA DE QUE A TESE É DERIVADA PASSOU A RODAR DENTRO DO TESTE, toda vez.** No
A1 as mutações foram feitas uma vez, à mão, por quem escreveu. No A2
(`teste-a2.php`) elas são parte do arquivo: seis bancos adulterados num
subprocesso, um por molde, exigindo que o texto troque de forma **e** que os
números de hoje sumam da tela. Ler a página de hoje só prova que ela está certa
hoje — e a decisão 1 abaixo é sobre amanhã. **Artigo novo nasce assim.**

**E o A1 publicava o FAQPage em ASCII.** "Nao. Nas 16 pecas de reposicao..." dentro
do JSON-LD, que é justamente o canal que a seção 5 do `ARQUIPELAGO.md` diz valer
tanto quanto ranquear. Corrigido em 11/09/2026 no `gerar-a1.py`, sem tocar no
snippet. **O banco é ASCII porque ele CITA fontes; o que a ilha ESCREVE sai
acentuado — e isso vale também para o que ela escreve dentro de marcação.**

**O DA R1 ESTÁ NO AR desde 10/09/2026** (`snippets/robometria-a1.php` v1.0.0, manifest
revisão 11): `https://robometria.com.br/filtro-universal-de-robo-aspirador/`. Ele fechou a
malha da R1 nos dois sentidos — duas listagens (home e hub), três irmãs, e a R1 v1.1.1
apontando de volta. **O artigo da R2 nasce junto com a R2, na mesma execução**, e herda as
três decisões que este bloco fixou:

1. **A tese do artigo é derivada, nunca digitada.** `ferramentas/gerar-a1.py` deriva os
   números do banco para `dados/a1-fatos.json`, e a frase de abertura tem DUAS formas,
   escolhidas pela contagem. Um artigo cuja tese é um número e que traz esse número dentro
   do HTML passa a mentir em silêncio no dia em que o banco cresce — e "em silêncio" é o
   ponto: ninguém relê artigo publicado.
2. **A DESCRIÇÃO DO JSON-LD E A RESPOSTA DO FAQPage SÃO PARTE DA TESE, não embrulho.** O
   defeito só apareceu ao plantar uma peça multimarca numa cópia do banco: a página visível
   se corrigia e o JSON-LD continuava afirmando o que deixara de valer. Numa ilha cuja seção
   5 diz que ser recomendado pela IA vale tanto quanto ranquear, **contradizer-se no canal
   que a IA lê é pior do que na tela**. Todo artigo novo deriva os três lugares juntos.
3. **O artigo não repete a ferramenta.** Sem formulário: a consulta é da ferramenta, e duas
   páginas respondendo a mesma coisa competem entre si no índice (seção 14.4).

**A PROVA DE QUE UMA TRAVA REPROVA É PARTE DO BLOCO.** As travas novas do `teste-a1.php`
foram medidas quebrando o banco de propósito numa cópia — números adulterados nos fatos e
uma peça multimarca plantada. Trava que nunca foi vista reprovando é trava não medida.

**A SEXTA DECISÃO, fixada em 12/09/2026 no A2 e valendo para toda página desta ilha: A
ATRIBUIÇÃO DE UM NÚMERO É LIDA DO DEGRAU, NUNCA DIGITADA — e a régua que a deriva serve
a QUALQUER campo.** A R2 fechou isso em 11/09 para o Pa, e escreveu no próprio registro o
que aconteceria no dia em que um número entrasse por loja oficial da marca: "a página
emprestaria calada a autoridade do fabricante a quem apenas transcreveu". No A2 esse dia
já era o dia — a área por carga dos cinco Electrolux vem do degrau 4, e os cinco cartões
publicavam "O fabricante declara". Duas coisas seguem disso, e valem antes de escrever
qualquer página nova:

1. **Regra derivável por um campo só é regra que a segunda página reescreve.** A versão
   de 11/09 só sabia derivar a procedência do Pa; o A2 decide pela ÁREA e ficou sem de
   onde ler. Hoje quem deriva é `procedencia_do_campo(m, campo)` em `cobertura-r2.py` —
   página nova chama essa, não escreve a sua.
2. **Frase que publica DOIS números precisa de DUAS procedências.** Hoje os dois do
   cartão do A2 saem da mesma fonte, e é justamente por isso que a frase não pode
   presumir: verdade por coincidência do banco é a família de defeito que esta ilha já
   pagou duas vezes. Trava latente assim só conta como medida quando a mutação PRODUZ o
   mundo em que ela morde — ver `ferramentas/mutacoes-a2-procedencia.py`.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **WordPress, casca, AS DUAS ferramentas e OS DOIS artigos estão no ar desde 11/09/2026** (manifest revisão 13, 9 páginas no sitemap). Os blocos 1, 2, 3, 3b, 4, 4e e 5 estão feitos para os dois eixos da ilha.
- ~~**ACHADO DE 11/09/2026: `robometria_casca_numeros()` lia uma option que nunca existiu no site.**~~ **CUMPRIDO em 11/09/2026** (casca 1.3.0, revisão 16): os onze números que a ilha publica sobre si mesma viajam em `dados/casca-fatos.json`, publicável, com as réguas da medição dentro do arquivo, e o gerador recusa gravar se o banco de hoje não bater. Um dos números já mentia: dizia 33 pares e o site serve 32.
- **UM NOME POR PÁGINA, e ele tem uma fonte só — 11/09/2026, casca 1.4.0, revisão 17, conferida no ar.** `robometria_casca_nome_da_pagina()` resolve as nove páginas; o H1 (post_title), o `<title>`, o `og:title`, o degrau da trilha e o rótulo do cartão **derivam** dela. Seis das nove tinham dois nomes ao mesmo tempo, porque o mapa das cabeças trazia um `titulo` digitado ao lado do da definição da página. **Página nova não precisa lembrar de nada**: nomeia-se num lugar só, e o portão `ferramentas/teste-voz.php` cobra as cinco superfícies.
  **O `<title>` agora é escrito por este repositório** (`document_title_parts` na casca). Antes a home servia o nome do site mais a descrição curta do wp-admin — 73 caracteres, vocabulário de dentro da fábrica, num campo que nenhum arquivo daqui escreve. **O teto é 65 caracteres, cobrado no NOME (52), na bancada, antes de publicar.**
- **TODA PÁGINA DESTA ILHA TEM UM SEGUNDO ESTADO VÁLIDO, e ele é invisível para quem mede o corpo.** Quando o banco não chega, as duas ferramentas, os dois artigos e o trecho de números da metodologia servem "estamos sem o banco" — página inteira, com cabeçalho, rodapé e prosa honesta. `ferramentas/varrer-corpo.php` passou dois dias medindo TRÊS desses estados como se fossem a página (a1 com 1.118 caracteres, a2 com 1.107, a metodologia sem os números), porque não carregava as options que o Sync grava. Agora: dono único do aviso (`robometria_casca_sem_banco_html`), marca `rbm-sem-banco` no markup, `!!! sem-banco` na linha do estado varrido, e **dois portões reprovando** (`teste-voz.php` e `teste-acentuacao.php`). **Bancada nova copia o boot inteiro — options E snippets —, ou mede a metade que não dá erro.**
- ~~**O PRÓXIMO PASSO é a vitrine de produto dentro do resultado da R2.**~~ **ERA
  FALSO, e o registro fica: a vitrine existia desde 11/09**, nasceu junto com a R2 e
  `robometria_r2_vitrine()` já era chamada na resposta. O passo tinha sido escrito de
  memória e nunca medido, e quem o leu como fato quase construiu de novo o que já
  estava no ar. **Antes de começar um bloco, abra a URL** — custa dois minutos e é a
  mesma regra que a seção 20.2 do contrato aplica a bloqueio de rede: estado herdado
  de execução anterior se reconfere, nunca se lê como fato.
  **O que o cartão realmente não tinha era PROCEDÊNCIA, e isso foi fechado em
  11/09/2026** (R2 1.2.0, revisão 18): o Pa é o único número que decide a
  recomendação e saía sem endereço, sem data e sem o degrau da escada. Ver o
  `REGISTRO.md`.
- ~~**O PRÓXIMO PASSO, medido no ar em 23h37Z de 11/09/2026 e não lembrado:** o **A2**
  (`/quantos-m2-o-robo-aspirador-limpa-por-carga/`) serve **5 cartões de vitrine com
  ZERO procedência** — "O fabricante declara 166 m² por carga", sem endereço, sem
  data, sem degrau e sem link. É o mesmo defeito que a R2 acabou de fechar, na página
  irmã dela, e a casca já tem todas as peças (`na_tela` na escada de fontes,
  `robometria_casca_fonte_link`, e o padrão de teste da seção 16 do `teste-r2.php`
  para copiar). Depois dele, a seção **"Exatamente no limiar"** da própria R2, que
  nomeia modelos e Pa e também não cita origem.~~ **OS DOIS ESTÃO CUMPRIDOS:** o A2
  em 12/09/2026 (A2 1.2.0, revisão 20) e a seção da R2 em 12/09/2026 (R2 **1.3.0**,
  revisão **22**, `/status` conferido às 19h30Z em um disparo). Com isso **não resta
  nenhum lugar nas duas ferramentas nem nos dois artigos em que um número decide e a
  origem não aparece** — mede isso a seção 17 do `teste-r2.php` e a do
  `conferir-no-ar.py`, no HTML servido.
  **A DECISÃO QUE FICOU, e vale para toda seção desta ilha que NÃO recomenda:** a
  regra da seção 7 (porta de compra antes da procedência) existe para o link de fonte
  nunca ser a única coisa clicável de um bloco. Onde a página recusa o item, a porta
  não pode existir — e o que a regra proíbe é o **silêncio** sobre a ausência, não a
  ausência. Então a seção declara que não vende e diz por quê. Trocar um silêncio por
  outro não é conserto.
  **E o `afiliado.sub_id_2` saiu do banco na mesma passada:** ele nomeia a PÁGINA que
  levou o clique, e o banco só sabe dizer um valor por registro. Cada gerador carimba
  o próprio código (R1, R2, A1, A2); `validar-banco.py` reprova o campo de volta no
  banco, e a seção 17 do `teste-casca.php` cobra que cada arquivo de dados carimbe só
  o seu — **página nova que copiar um gerador antigo reprova antes de existir URL**.
  ~~**O PRÓXIMO PASSO** é a transcrição da composição dos kits e o item **(e)** do 3c.~~
  **OS DOIS FORAM FECHADOS EM 12/09/2026**, e cada um de um jeito: a transcrição
  **entregue** (ERB30 e ERB44, ver os itens logo abaixo) e a recarga **recusada com
  causa medida** — ela deixou de ser coleta, como os m² do item (d). O que destravou
  não foi a rede abrir: foi separar o egresso direto do canal de busca.
  ~~**O PRÓXIMO PASSO AGORA** é o kit do ERB80.~~ **CUMPRIDO em 12/09/2026** (ver
  os itens abaixo), junto com o pano de microfibra que a mesma varredura achou.
  ~~**O PRÓXIMO PASSO AGORA** são as **peças da Xiaomi e da WAP com código.**~~
  **O LADO XIAOMI FOI CUMPRIDO em 13/09/2026** (manifest revisão 25, `/status`
  conferido em UM disparo): oito peças com código entraram, a R1 foi de 16 para
  **20 dos 28** modelos e o cruzamento com a R2 de **3 para 7**. E a causa dos três
  dias parados **não era a rede**: o `PROMPT.md` e o `ESTADO.md` mandavam testar
  `mi.com.br` e `xiaomi.com.br`, e o banco desta ilha sempre citou
  **`www.mi.com/br`** — o endereço está escrito em sete registros desde 09/09. O
  egresso direto segue fechado por política nos três; a **busca alcança `mi.com`**,
  e nunca tinha sido testada nele. **Quando o canal falhar, confira o endereço
  contra o BANCO**, que é quem guarda a fonte, e não contra a prosa que descreve o
  bloqueio.
  ~~**O PRÓXIMO PASSO AGORA é a WAP, e o alvo TROCOU: lá o gargalo é MODELO, não
  peça.**~~ **O LADO DO MODELO FOI CUMPRIDO em 13/09/2026** (manifest revisão 26,
  `/status` conferido em UM disparo): **W90, W100, W100C, W300 e WSMART** entraram,
  e a WAP passou de 3 para **8** modelos. Nenhum dos cinco declara Pa — a marca
  publica Pa no W400 e nível de sucção no resto —, então a leva **não move a R2**:
  ela existe para abrir o lado do modelo, que era o que travava a peça. O preço
  está medido e é honesto: a R1 continua respondendo em 20 modelos e passa a sair
  **vazia em 13** (era 8), e a página de metodologia publica os dois números
  contados. Ordem "modelo antes de peça" cumprida.
  ~~**O PRÓXIMO PASSO AGORA é a PEÇA da WAP.**~~ **REMEDIDO EM 14/09/2026, 19h25Z,
  e o resultado foi NEGATIVO — o que muda a ordem da fila, não o diagnóstico.** A
  peça da WAP foi o primeiro alvo desta execução, e as duas medições pedidas abaixo
  foram feitas: (i) o egresso direto a `loja.wap.ind.br`, `blog.wap.ind.br` e
  `www.wap.ind.br` devolveu `000` nos três, com `connect_rejected` do proxy, e o
  `WebFetch` devolveu `EGRESS_BLOCKED`; (ii) **a passada limpa não devolve o
  código**. Buscando com `FW006267` na consulta, ele volta — o que é circular e não
  vale; buscando pelo título do produto, restrito a `loja.wap.ind.br`, a página
  aparece e **o campo da ficha não**, com a própria busca dizendo que o número não
  estava no conteúdo recuperado. É a terceira passada limpa a falhar no mesmo
  ponto, em execuções diferentes: **não é teimosia da busca, é o canal.** E os
  quatro modelos WAP que continuam no vazio da R1 (W400, W1000, W310, W100C) não
  têm página de peça de reposição na loja — duas passadas devolveram só a página do
  próprio robô e categorias genéricas. Fica valendo: quem destrava é o egresso
  abrindo, ou alguém lendo a ficha no navegador. **Por isso o alvo desta execução
  passou a ser o Xiaomi, que é o canal que funciona** — e a leva B106GL tirou o S10
  do vazio. A varredura de 13/09 já abriu as páginas de acessório
  por modelo (W300 com 9 acessórios em 7 categorias — filtro, escova, carregador,
  recipiente, mop, controle remoto e pincel; WSMART com 9; W90 com escova rotativa
  e carregador) e `marcas.json` já tem o `canal_de_pecas` da marca. **O que
  impediu a gravação hoje foram duas coisas, e as duas são de método:**
  1. **O código voltou em UMA passada e não voltou na segunda.** `FW006267` na
     escova direita do W300, `FW008028` na escova central do WSMART e `FW009132`
     na escova rotativa do W90 — nas três, a segunda passada limpa não devolveu o
     código. Um código de peça é o que a pessoa digita na busca da loja: entrar com
     ele meio confirmado é pior que não entrar.
  2. **A página de acessório NÃO declara a função da escova.** "Direita",
     "Esquerda", "Central", "Frontal" e "Rotativa" são **nomes**, e ler
     `tipo_de_peca` de um nome é a heurística por vizinhança que a seção 8 do
     contrato proíbe — a mesma que fez a Xiaomi publicar um catálogo de variantes
     como kit. Quem for pegar isto decide primeiro **onde** a função está
     declarada (a ficha do próprio robô lista o que vem na caixa, e é candidata),
     e só então grava.
  **E existe um terceiro alvo barato que apareceu junto:** o W300 e o WSMART
  publicam acessório na categoria **Recipiente**, e `reservatorio` é justamente o
  único tipo do vocabulário sem NENHUMA peça no banco inteiro — é o tipo que saiu
  do seletor da R1 por isso. Uma peça de reservatório com função declarada devolve
  o tipo ao seletor.
  **Os manuais em PDF continuam sendo a porta do nível 2** e agora são oito, um por
  modelo WAP do banco, com revisão e data no nome do arquivo (W400 "FW009293
  REV00MAI23", W1000 "FW010143 REV03ABR25", W90 "FW010263 REV00JAN24", W100
  "FW007467 REV01OUT21", W100C "FW008617 REV00SET21", WSMART "FW007881 REV. 00
  ABRIL/2020"). Só o `WebFetch` do PDF segue bloqueado; **o WSMART é a exceção de
  endereço** — a WAP guarda o manual dele no próprio blog, e não em
  `mais.conteudo.wap.ind.br`.
  **E há alvos de CATEGORIA DESCOBERTA que o vocabulário não comporta — dois
  agora, porque a leva da Xiaomi acrescentou a tampa de escova `D106-BZSZ` do S20
  ao lado do saco descartável do ERB80. Os dois ficam fora pela mesma régua:**
  `loja.electrolux.com.br/kit-3-sacos-descartaveis-electrolux-para-robo-aspirador-erb80/p`.
  Saco descartável é consumível de base autolimpante, e o ERB80 tem base
  autolimpante — mas `tipo_de_peca` no `esquema-banco.json` não tem esse tipo, e
  **acrescentar tipo mexe no seletor da R1, na cobertura e nos portões**. Fica
  registrado como categoria descoberta, não como coleta pendente: quem for pegá-lo
  decide primeiro se o tipo nasce, e a régua dessa decisão é a 14.3 (faixa
  descoberta, não número redondo). Na mesma varredura apareceu também um **ERB40**
  com Kit Performance próprio, e ele não está em `modelos-robo.json`.
  **A leva de malha (5b) continua travada** pela metade humana do despacho: o sitemap precisa ser reenviado no Search Console, e isso exige o navegador do Raphael.
- **Antes de mexer em qualquer snippet, rode os OITO testes de bancada:** `teste-casca.php`, `teste-r1.php`, `teste-a1.php`, `teste-r2.php`, `teste-a2.php`, `teste-acentuacao.php`, `teste-arvore.php` e `teste-voz.php`, todos com a raiz da ilha como argumento (`php ferramentas/teste-casca.php .`). **A contagem de afirmações de cada um NÃO está escrita aqui de propósito** — em 13/09/2026 eram 902 no total, e a lista que ficava nesta linha já tinha cinco números vencidos ao mesmo tempo. Quem quiser o número de hoje roda e lê a última linha; quem escreve número derivado em prosa assina um cheque contra o banco de amanhã, e esta ilha já pagou esse cheque dentro da própria bancada (ver `mutacoes-varredura-por-modelo.py`). Depois do desembarque, `python3 ferramentas/conferir-no-ar.py` mede as nove URLs no ar com régua própria — **e `python3 ferramentas/conferir-kits-no-ar.py` (71) mede a ENTRADA da R1 no ar, 14 estados de modelo × tipo, porque o primeiro mede o caso-âncora e bloco que muda resposta de consulta não aparece lá** — os endereços e os nomes estão escritos literalmente dentro dele, e não lidos do código, para as duas metades não errarem juntas. Eles são a única verificação da seção 8 que roda sem depender do site. **O sexto é o único que varre a ENTRADA INTEIRA** — um estado por página fixa, um por modelo publicável do banco, um por tipo de peça e as bordas da R2, um processo por estado (eram 72 quando isto nasceu; hoje são quantos o banco pedir, e o próprio portão cobra um estado para CADA modelo, por id), via `ferramentas/varrer-corpo.php`: os outros medem o caso-âncora, e foi por isso que "Aspirador Robo" e "Versao A" ficaram invisíveis para cinco testes verdes. O segundo compara as 188 frases publicadas contra a implementação de referência; o terceiro **recalcula a tese do artigo em PHP, direto do banco, sem olhar para o que o gerador em Python escreveu** — duas contas independentes que batem são medição, uma conta sozinha é o que o autor achou.
- **A PORTA DE COMPRA TEM UM DONO SÓ, e ele é a casca.** `robometria_casca_porta_de_compra`, `robometria_casca_rotulo_da_loja`, `robometria_casca_fonte_link` e `robometria_casca_css_vitrine` valem para toda página desta ilha que recomenda item; a R1 delega para elas. Página nova que recomenda produto **chama estas funções**, nunca escreve as suas. Os pesos visuais do botão de compra e do link de procedência são regra do Arquipélago (seção 7), não estilo local: com uma cópia por página, bastaria alguém ajustar uma delas para a ilha voltar — numa página só, e sem ninguém notar — ao defeito de 10/09/2026.
- **Página nova entra no catálogo da casca pelo FILTRO dela**, `robometria_ferramentas` para ferramenta e `robometria_artigos` para artigo. A casca nunca ganha uma cópia da página dentro; é assim que a home e o hub listam qualquer coisa nova sem serem editados de novo, e é o que garante as duas listagens que a seção 9 exige.
- ~~**O BANCO ESTÁ EM ASCII, E AGORA ISSO APARECE NA TELA.**~~ **CUMPRIDO em 11/09/2026.** 121 strings restauradas nos nove campos que a varredura mediu chegando ao corpo servido, e a operação é **provada diacrítico-only**: reduzido a sem-diacrítico, o banco de hoje é byte a byte o de ontem (`dados/acentuacao-restaurada.json`, conferido linha a linha por `teste-acentuacao.php` com régua própria). **A restauração não é releitura:** o acento foi reposto pela ilha, não lido no fabricante — e é por isso que o livro-razão existe, como lista de conferência de quem reler os manuais quando a rede abrir.
  **Quem segura daqui para a frente é `ferramentas/teste-acentuacao.php`**, que lê o CORPO dos 72 estados e reprova qualquer palavra da régua. Palavra ambígua (o "e" que pode ser "é") ficou de fora do mapa de propósito: acertar por adivinhação não é acertar. **O que ficou de fora do escopo, e é trabalho de verdade:** `declarado_como`, `motivo_do_null` e `descricao_na_fonte` seguem em ASCII. Elas NÃO estão na tela hoje (medido), mas são prosa longa e chegam à tela no dia em que alguém as publicar — e aí o portão reprova, que é exatamente o desenho.
- ~~**O KIT DECLARADO NÃO TEM PORTA DE COMPRA, E ISSO SE DESTRAVA POR DADO.**~~
  **CUMPRIDO em 12/09/2026** (manifest revisão 23, `/status` conferido em um
  disparo). A previsão estava certa e foi medida, não suposta: **o dado abriu a
  porta de compra sozinho**, sem uma linha de snippet. Na consulta ERB30 +
  filtro a página agora diz que a Electrolux não vende o filtro avulso, nomeia o
  Kit Performance que o contém, e serve o bloco "Onde comprar" antes da
  procedência. O ERB30 era o único modelo da ilha que não respondia consulta
  nenhuma; a Electrolux passou a 9/9 e a R1 a 16 dos 28 modelos.
  **O QUE FICOU VALENDO PARA A PRÓXIMA TRANSCRIÇÃO, e é o mais importante:** o
  ERB30 veio com quantidades e o **ERB44 veio pela metade** — a página dele
  declara os tipos e não as quantidades, e diz "escovas" sem dizer qual, num
  modelo que tem escova rotativa central vendida à parte. A busca **ofereceu a
  composição do ERB30 como preenchimento** e ela foi recusada: modelo vizinho não
  declara pelo vizinho. Item sem tipo entra com `tipo: null`, que é como o esquema
  diz "o kit serve e nós não sabemos dizer este item" — e a R1 então recusa aquele
  tipo, que é o acerto e não a falta.
- ~~**O KIT DO ERB80 EXISTE NA LOJA E NÃO ESTÁ NO BANCO.**~~ **CUMPRIDO em
  12/09/2026** (manifest revisão 24, `/status` conferido em UM disparo) — **e a
  previsão escrita aqui estava errada, o que vale mais que o registro em si.**
  O texto anterior dizia que o kit entraria "no nível do ERB44, não no do
  ERB30", porque as leituras de então tinham devolvido só o trio genérico. A
  coleta desta execução, com perguntas limpas, achou o contrário: a página do
  kit no domínio do **fabricante**
  (`content.electrolux.com.br/…/kit_performance_erb80/`) descreve os três itens
  **um a um** e nomeia a escova pelo **tipo** — "escovas laterais, direita e
  esquerda". Ele entra ACIMA do ERB44.
  **A CONFERÊNCIA QUE SUSTENTA ISSO CUSTOU UMA LEITURA A MAIS, e é a régua para
  a próxima transcrição desta ilha:** um bloco por item numa página de catálogo
  pode ser molde do gerador de páginas, e aí não declara nada sobre aquele
  produto. O jeito de saber é ler a **página irmã** com a MESMA pergunta — a do
  ERB44, mesmo domínio, mesmo formato, traz só a cópia genérica. Logo o bloco
  por item existe na página do ERB80 porque a Electrolux o escreveu lá; e, de
  quebra, isso confirma que o `tipo: null` do ERB44 foi acerto e não preguiça.
  É a mesma família do "documento de família com dois números", só que a
  declaração vizinha aqui serve para **confirmar**, não para desmascarar.
  **A QUANTIDADE FICOU null NOS TRÊS**, de propósito: "direita e esquerda" está
  numa frase de benefício, descrevendo o que escova lateral faz, não numa lista
  de conteúdo da embalagem. Ler dali um "2" é transformar prosa de venda em
  quantidade declarada. E a busca ofereceu "1 filtro HEPA, 1 pano e 2 escovas"
  dizendo **textualmente** que era "baseado em kits similares de outros
  modelos" — recusado, pela mesma regra que barrou o preenchimento do ERB44.
- **O PANO DE MICROFIBRA ERB60/61/62/80 ENTROU JUNTO, e não estava previsto em
  lugar nenhum** — apareceu na mesma varredura do kit. É a primeira peça avulsa
  desta ilha a servir o ERB80 e cobre quatro modelos de uma vez. **A lição de
  fila:** varredura feita para colher UM alvo devolve vizinhos, e o vizinho aqui
  era mais barato que o alvo. Vale olhar a lista de resultados inteira antes de
  fechar a coleta.
- **FRASE QUE DEPENDE DA VIZINHA É FRASE QUE UM DIA MENTE — e esta estava NO AR
  em três páginas** (12/09/2026, R1 **1.3.0**). A frase do kit quando existe a
  peça avulsa era *"Ele também vem dentro do kit …"*. O pronome só apontava para
  alguma coisa por **sorte de ordem**: as frases saem na ordem do banco, e no
  único caso que existia (o filtro do ERB60/61/62) o registro da peça avulsa
  vinha antes do registro do kit. Quando o pano de microfibra deu ao **mop** um
  avulso, a frase do kit saiu na posição do KIT — depois da escova lateral e
  **antes de o mop ser nomeado**. Oito portões verdes, porque todos mediam a
  frase sozinha, e sozinha ela estava certa.
  **A saída não foi reordenar a lista** — seria consertar o sintoma e deixar a
  dependência de pé. A frase passa a **nomear o tipo**, nas duas implementações,
  e fica autossuficiente: é a 5.2 do contrato ("frase que sobrevive a ser citada
  fora de contexto") e a 8 ("quem decide é a estrutura, nunca a vizinhança").
  **Quem segura daqui para a frente:** a seção 14 do `teste-r1.php` (régua
  escrita à mão no próprio teste, medindo só a **primeira oração** das frases
  das DUAS implementações), `ferramentas/mutacoes-frase-nomeia-o-tipo.py` (4 de
  4 reprovadas — e a terceira **produz o mundo**, quebrando os dois lados juntos,
  então a comparação PHP × referência continua verde e só a trava nova pega), e
  a metade no ar em `conferir-kits-no-ar.py`, que passou a varrer os 5 estados
  do ERB80.
- **MUTAÇÃO TAMBÉM TEM NÚMERO DE TELA, e duas morreram caladas aqui**
  (12/09/2026). Duas mutações do `mutacoes-arvore.py` traziam o número
  **digitado** nos dois lados (`"pares_declarados": 32` → `33`). Bastou o banco
  crescer para o alvo sumir do arquivo e elas deixarem de editar coisa alguma —
  a "mutação inerte" que aquele arquivo existe para impedir, agora dentro dele.
  Agora leem o valor de hoje e somam 1. **A cicatriz do "número de tela nasce
  contado" vale para a bancada, não só para a página:** quem digita um número
  derivado assina um cheque contra o banco de amanhã.
- **O EGRESSO DIRETO E O CANAL DE BUSCA SÃO DUAS REDES DIFERENTES, e a distinção
  vale por um bloco inteiro** (12/09/2026). `curl` e `WebFetch` devolvem `000` e
  `EGRESS_BLOCKED` em `electrolux.com.br`, `loja.electrolux.com.br`,
  `cuida.electrolux.com.br`, `mi.com.br` e `wap.ind.br` — política de egresso,
  remedida em duas passadas com a ilha em 200 nas duas. **A busca alcança os
  mesmos fabricantes.** Os dois kits ficaram três dias esperando porque o
  `ESTADO.md` dizia "a rede está fechada" e ninguém tinha separado os dois canais.
  Antes de declarar coleta bloqueada nesta ilha, teste **os dois**.
- **QUANDO UM DOCUMENTO DE FAMÍLIA TRAZ DOIS NÚMEROS, O QUE VOCÊ JÁ CONHECE DIZ SE
  O OUTRO É DO SEU MODELO** (12/09/2026, e é a régua que fechou o item (e) do 3c).
  A recarga dos cinco Electrolux que declaram cobertura não é mais coleta: nenhuma
  página de modelo declara tempo de carga, e o único número publicado está num
  artigo de família ("Como faço para utilizar o meu Robô Aspirador Home-e
  Experience com Autonomous Technology") que, **na mesma frase**, declara autonomia
  de 90 minutos — número que não é o de nenhum dos cinco (100, 100, 100, 100 e
  120). A declaração vizinha desmascarou a atribuição. Sem essa conferência, o 5 h
  entraria com cara de dado de fabricante.
- ~~**UMA FONTE ESTÁ NO NÍVEL 2 E A ESCADA DIZ QUE O NÍVEL 2 NÃO EXISTE.**~~ **DECIDIDO em 11/09/2026: NÃO é nível 2. É nível 3.**
  **A regra, e ela vale para toda fonte de toda ilha desta pasta:** uma origem tem TRÊS elos — quem escreveu o documento, quem o guarda e como nós o lemos — e **o nível é o do elo MAIS FRACO**, nunca o do mais forte. O manual do ERB10/ERB11/ERB20 é escrito pela Electrolux (elo forte), mas está guardado por `manuals.plus` e chegou aqui por busca, sem leitura direta. Dois dos três elos são fracos.
  **A direção saiu da assimetria de custo (seção 10 do contrato), não do gosto:** errar para BAIXO custa uma frase mais fraca na tela ("a confirmar no manual"); errar para CIMA faz a página de metodologia declarar um rigor que a ilha não tem — e metodologia é a página cujo único produto é o rigor.
  **A medição decidiu sozinha:** as QUATRO únicas fontes de nível 2 do banco inteiro eram a mesma entrada de `manuals.plus`. Nível 2, neste banco, era inteiro custódia de terceiro — não um registro solto.
  **O que ficou mecânico, para a contradição não voltar:** (a) `validar-banco.py` passou a exigir que `origem` bata com a `origem` que a escada dá àquele `nivel` — era por aí que o defeito entrava, porque só o `nivel` era conferido; (b) nível 1 ou 2 agora exige o campo `leitura: "direta-na-fonte-primaria"` **declarado**, e silêncio nunca promove (adivinhar pelo texto do `canal_de_coleta` seria a heurística por vizinhança que a seção 8 proíbe); (c) a coluna "Temos hoje" da página **deixou de ser digitada e passou a ser contada** (`dados/casca-fatos.json`). As três foram testadas quebrando o banco de propósito e reprovam.
  **O caminho de volta ao nível 2 está escrito no registro:** reler o mesmo manual no endereço da Electrolux sobe o campo de 3 para 2 sem mudar mais nada.

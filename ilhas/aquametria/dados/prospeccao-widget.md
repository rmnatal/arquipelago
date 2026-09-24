# PROSPECCAO DO WIDGET — bloco T6, secao 14.7 do contrato

> **ARQUIVO GERADO por `ferramentas/gerar-prospeccao.py` a partir de**
> **`dados/prospeccao-widget.json`. Nao edite a mao:** o portao
> `validar-prospeccao.py` regera este texto e compara, e edicao a mao
> fica vermelha. Mude o JSON e rode o gerador.

Atualizado em **2026-09-24**. Nada aqui vai para o ar (`publicar: false`).

## O QUE MEDIU ISTO, E O QUE ELE NAO ALCANCA

O egresso desta nuvem responde 403 no CONNECT para todo dominio fora da lista de permitidos — medido em tres passadas em 24/09/2026, com aquametria.com.br em 200 nas mesmas tres. WebFetch tambem devolve EGRESS_BLOCKED. O unico instrumento que alcanca o mundo aqui e a BUSCA, que e o nivel 3 da escada de coleta desta ilha e foi como este banco inteiro foi construido.

**Ninguem abriu nenhum site.** Entao `contato` e `plataforma` estao
`null` em todas as linhas, com o motivo escrito em cada uma. O proximo passo
desta lista NAO e da Fundacao: e abrir cada dominio num navegador, confirmar
canal de contato e plataforma, e so entao escrever a abordagem.

Esta passada sabe afirmar PRESENCA, nunca ausencia. Um dominio nao aparecer na busca de calculadora nao prova que ele nao tem calculadora — prova que a busca nao o mostrou. Entao os tres campos de fato so aceitam `true` (com evidencia que os nomeia) ou `null` (= nao medido). O portao recusa `false`, de proposito, para o arquivo nao virar uma lista de negativas que ninguem mediu.

## O ACHADO QUE REORDENOU A LISTA

A consulta de calculadora de aquario em portugues do Brasil ja tem **13 dominios**
publicando ferramenta. Deles, **1** e loja de aquarismo (`aquariosplantados.com.br`); os outros 12 sao
site de conteudo, fazenda de calculadora e um dominio de outro nicho inteiro.
Isso vale nas duas direcoes, e as duas estao medidas:

- **Para a prospeccao:** loja que ja construiu a propria calculadora nao
  instala a de ninguem, e cai para prioridade 3 por regra, nao por opiniao.
- **Para a oferta:** das **13 lojas** desta lista, so **1** tem calculadora
  medida. A ferramenta que falta na loja brasileira de aquarismo e justamente
  esta, e o espaco existe porque quase ninguem do lado do comercio a tem.

## PRIORIDADE 1 — as tres condicoes medidas

| dominio | tipo | vende equipamento | publica conteudo | ja tem calculadora |
|---|---|---|---|---|
| `aquariosdorio.com.br` | loja | sim | sim | nao medido |

**Aquarios do Rio** (`aquariosdorio.com.br`) — O UNICO candidato que fecha as tres condicoes com o que a busca alcanca: e loja, vende o equipamento que as calculadoras dimensionam (filtro canister, aquecedor com termostato) e publica conteudo editorial NO PROPRIO DOMINIO, em /blog/. Quem ja mantem blog tem onde encaixar uma ferramenta e ja tem o habito de publicar; quem nao tem precisa criar a pagina primeiro.

## PRIORIDADE 2 — uma condicao medida, ou teto de tipo

| dominio | tipo | vende equipamento | publica conteudo | ja tem calculadora |
|---|---|---|---|---|
| `aquaricamp.com.br` | loja | sim | nao medido | nao medido |
| `aquariovivo.com.br` | conteudo | nao medido | sim | nao medido |
| `aquatank.com.br` | fabricante | sim | nao medido | nao medido |
| `aquaticabrazil.com.br` | distribuidora | nao medido | sim | nao medido |
| `atlantidaaquarios.com.br` | loja | sim | nao medido | nao medido |
| `doled.net.br` | fabricante | sim | nao medido | nao medido |
| `escoladeaquario.com.br` | conteudo | nao medido | sim | nao medido |
| `fazendasubmersa.com.br` | loja | sim | nao medido | nao medido |
| `forfish.com.br` | loja | sim | nao medido | nao medido |
| `francoaquarismo.com.br` | loja | sim | nao medido | nao medido |
| `gruposarlo.com.br` | fabricante | nao medido | sim | nao medido |
| `lojaaquaverso.com.br` | loja | nao medido | sim | nao medido |
| `petpataoshop.com.br` | loja | sim | nao medido | nao medido |
| `reefjoinville.com.br` | loja | sim | nao medido | nao medido |
| `reefpoint.com.br` | distribuidora | sim | nao medido | nao medido |
| `reefshock.com.br` | loja | sim | nao medido | nao medido |
| `reidosaquarios.com.br` | loja | sim | nao medido | nao medido |

**Aquaricamp** (`aquaricamp.com.br`) — Loja com catalogo de equipamento medido (arvore /equipamentos/filtros/filtros-canister). A busca restrita ao dominio devolveu vitrine de projetos e livro a venda, NAO artigo proprio — vitrine de projeto nao e conteudo editorial, e livro de terceiro menos ainda. Sobe para 1 no dia em que alguem abrir o site e achar area de conteudo.

**Aquario Vivo** (`aquariovivo.com.br`) — Site de conteudo de aquarismo, e o artigo medido chega a RECOMENDAR FAIXA DE LITRAGEM para iniciante (60 a 80 L) — exatamente a pergunta que a C1 responde com conta. Site de conteudo nao vende, entao o widget nao lhe traz receita; o que ele traz e ferramenta que a pagina dele nao tem.

**Aquatank** (`aquatank.com.br`) — Fabricante brasileiro com linha propria de filtro, bomba, aquecedor e luminaria, e com faixa de volume declarada por modelo (10 L a 200 L+). Fabricante que declara faixa e interlocutor natural de calculadora — e, de quebra, e fonte de dado para o banco desta ilha.

**Aquatica Brazil** (`aquaticabrazil.com.br`) — Distribuidora com BLOG proprio, e o artigo medido e dirigido a quem MONTA loja de aquarismo — ou seja, o publico dela e a lista de lojas. Um widget citado ali chega a varias lojas de uma vez; e a unica linha desta lista com esse efeito de alavanca.

**Atlantida Aquarios** (`atlantidaaquarios.com.br`) — Loja com as tres familias que as calculadoras desta ilha dimensionam na mesma arvore: filtro canister, aquecedor com termostato e bomba submersa. A busca restrita ao dominio devolveu SO pagina de produto — nenhum artigo.

**Doled** (`doled.net.br`) — Monta luminaria de aquario no Brasil e vende direto, com garantia e peca de reposicao. Fabricante que vende direto junta os dois lados: e alvo de widget e e fonte de especificacao para a C15.

**Escola de Aquario** (`escoladeaquario.com.br`) — Site de conteudo, e o artigo medido e dirigido a quem abre loja de aquarismo — publico de alavanca, como a Aquatica Brazil.

**Fazenda Submersa** (`fazendasubmersa.com.br`) — Loja de aquapaisagismo que tambem vende equipamento (canister e termostato no mesmo catalogo). A busca restrita ao dominio devolveu pagina de CATEGORIA com texto e LIVRO a venda — categoria com paragrafo nao e artigo, e livro de terceiro nao e conteudo proprio.

**ForFish** (`forfish.com.br`) — Marca com loja propria em subdominio (loja.forfish.com.br) e luminaria de marinho no catalogo. Subdominio proprio conta como site proprio; o que nao contaria e vitrine dentro de marketplace.

**Franco Aquarismo** (`francoaquarismo.com.br`) — Loja grande, com luminaria de aquario em pagina de produto propria — a familia que a C15 dimensiona. O conteudo que a busca associou a ela tambem e CANAL de video, fora do dominio.

**Grupo Sarlo** (`gruposarlo.com.br`) — Fabricante com blog datado e ativo (dois artigos medidos, um deles sobre CONSUMO DE ENERGIA no aquario — vizinho direto da conta que a C5 faz). Fabricante grande costuma ter equipe de conteudo, o que ajuda e atrapalha: ha onde publicar, e ha processo.

**AQUAVERSO** (`lojaaquaverso.com.br`) — Loja que publica GUIA proprio, no proprio dominio, e o guia fala de litragem inicial e de filtro e termostato como equipamento basico — o assunto exato das calculadoras desta ilha. Falta so medir o catalogo: se ela vende o equipamento que o guia dela recomenda, vira prioridade 1 na mesma hora.

**Pet Patao Shop** (`petpataoshop.com.br`) — Pet shop com secao de aquarismo e arvore de filtro canister propria. Nao e loja especializada, o que costuma significar menos apetite editorial — mas o catalogo cobre o que a C3 dimensiona.

**Reef Joinville** (`reefjoinville.com.br`) — Loja de marinho com iluminacao LED, skimmer, bomba de circulacao e filtragem no catalogo. ATENCAO DE ESCOPO: o banco desta ilha e de AGUA DOCE, e as cinco calculadoras assumem doce — uma delas instalada em loja de marinho serviria numero fora do escopo declarado. Prospeccao valida, oferta a combinar.

**Reef Point** (`reefpoint.com.br`) — Distribuidora com marcas exclusivas, entre elas iluminacao. Distribuidora nao vende ao leitor, entao o widget nao ajuda a venda dela diretamente — mas ela alcanca as lojas que vendem, e por isso o teto dela e 2 e nao 1.

**Reefshock** (`reefshock.com.br`) — Loja de marinho com arvore propria de luminaria. Mesma ressalva de escopo da Reef Joinville: o banco desta ilha e de agua doce.

**Rei dos Aquarios** (`reidosaquarios.com.br`) — Loja especializada (Maringa) com filtro canister, externo, interno e aquecedor no catalogo. O conteudo que a busca associou a ela e CANAL de video, que fica fora do dominio e nao serve de casa para widget.

## PRIORIDADE 3 — ja tem calculadora, tipo que nao atravessa, ou nada medido

| dominio | tipo | vende equipamento | publica conteudo | ja tem calculadora |
|---|---|---|---|---|
| `agrosete.com.br` | desconhecido | nao medido | sim | nao medido |
| `aquaplantados.com.br` | loja | nao medido | nao medido | nao medido |
| `aquariosplantados.com.br` | loja | nao medido | nao medido | sim |
| `cobasi.com.br` | rede-pet | nao medido | sim | nao medido |
| `kauar.com.br` | desconhecido | nao medido | sim | nao medido |
| `petz.com.br` | rede-pet | nao medido | sim | nao medido |

**Agrosete** (`agrosete.com.br`) — Blog proprio com artigo de aquario grande. Nao mediu se aquarismo e linha de verdade dela ou assunto de passagem — e loja agro com uma prateleira de aquario nao e interlocutor de calculadora.

**AquaPlantados** (`aquaplantados.com.br`) — Loja de aquapaisagismo e lago ornamental. NADA de fato foi medido nela nesta passada — nem catalogo de equipamento, nem conteudo proprio — e prioridade 3 aqui significa exatamente isso: falta medida, nao falta merito.

**Aquarios Plantados** (`aquariosplantados.com.br`) — E A LOJA QUE JA CONSTRUIU A PROPRIA CALCULADORA — duas paginas de litragem no proprio dominio. Quem ja tem a ferramenta nao instala a de outro, e insistir aqui e gastar a abordagem no lugar de menor chance. Ela vale mais como MEDIDA do que como alvo: e a prova de que loja de aquarismo brasileira ja enxerga calculadora como conteudo.

**Cobasi** (`cobasi.com.br`) — Blog grande, com artigo assinado por biologo da equipe. O teto 3 de `rede-pet` e JUIZO, nao medida, e o juizo esta escrito para poder ser contestado: rede nacional tem equipe editorial propria, fornecedor homologado e juridico — widget de dominio desconhecido nao atravessa isso, e a abordagem custa mais do que rende no comeco.

**Kauar** (`kauar.com.br`) — Tem blog proprio em subdominio, com guia de montagem. O TIPO nao foi medido — nao sei por busca se e loja, fabricante ou so conteudo — e `desconhecido` derruba o teto para 3 de proposito: prospeccao que nao sabe com quem fala escreve texto errado.

**Petz** (`petz.com.br`) — Mesmo caso da Cobasi, mesmo juizo escrito: blog proprio, porta institucional fechada para dominio novo.

## QUEM JA OCUPA A SERP DE CALCULADORA

Medido pelas tres consultas de calculadora desta passada. Nao e lista de
alvo: e o mapa de quem ja esta la, e serve tanto para a oferta do widget
quanto para quem for ler SERP depois.

| dominio | o que publica |
|---|---|
| `aquaa3.com.br` | calculadora de litragem de aquarios |
| `aquaninjas.com.br` | calculadora com 12 calculos (volume, TPA e parametros) |
| `aquariosplantados.com.br` | duas paginas de calculadora de litragem, no dominio de uma LOJA de aquarismo |
| `aquarismobrasil.com.br` | calculadora de aquario |
| `baixarfavicon.com.br` | calculadora de aquario que tambem estima filtro, aquecedor e quantidade de peixes — a mesma tese da Aquametria, num dominio de fazenda de ferramentas |
| `calculadora.lol` | calculadora de aquario em fazenda de calculadoras |
| `calculadorauniversal.com.br` | calculadora de aquario em fazenda de calculadoras |
| `found-tools.com` | calculadora de potencia e custo de aquecedor, em portugues, em dominio .com |
| `msfish.com.br` | calculadora para montagem de aquarios; o proprio resultado diz que ela e baseada na calculadora de OUTRO site (Aquaflux), o que mostra que neste nicho a ferramenta ja circula de site em site |
| `ranger3d.com.br` | calculadora de volume e custo de vidro — e de OUTRO nicho (impressao 3D), o que mostra que a consulta atrai site sem autoridade tematica |
| `reefflow.com.br` | calculadora de aquecedor. ESTA LINHA MERECE ATENCAO: a ReefFlow e a FONTE que a C5 desta ilha cita para a faixa de delta de 10 C — ou seja, a ilha cita como fonte um dominio que publica a calculadora concorrente da C5. Nao e defeito e nao muda o numero; e para ninguem descobrir isso depois. |
| `shrimp4you.pt` | calculadora de aquario; dominio de PORTUGAL aparecendo na consulta em portugues do Brasil |
| `shrimpnexus.com` | calculadora de litros, TPA e aquecedor; dominio .com, nao .br |

## O QUE ESTA LISTA NAO E

- **Nao e lista de link para publicar.** Nenhuma linha daqui vira link no
  site. A secao 10 do contrato proibe troca de link, PBN e diretorio, e a
  unica alavanca permitida e o widget INSTALADO por quem quis instalar.
- **Nao e diagnostico da 21.5.** O item 2 do despacho da Sentinela pede um
  diagnostico de consulta e SERP escrito DEPOIS da leitura semanal de
  30/09/2026, e sobre as consultas `quantos litros para <especie>`. As tres
  consultas desta passada sao de CALCULADORA, para a prospeccao. Escrever o
  diagnostico agora seria escrever o criterio antes do dado.
- **Nao e contato.** Ninguem foi abordado, e a Fundacao nao abre conta, nao
  escreve e-mail e nao fala com loja nenhuma.

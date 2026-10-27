---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-27T17:09Z   # BLOCO ENTREGUE: a carga do Parque Bondinho Pao de Acucar (5a experiencia, 1a brasileira) e a entidade ELEGIBILIDADE, esquema e banco na versao 8. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-27T17:09Z pela propria execucao que reservou as 16h25Z e renovou DUAS vezes pela 1.1 (16h30Z e 16h52Z): o bloco mexeu em esquema, banco, validador, mutacoes, F1, portao da F1, prospeccao e especificacao, e a bancada desta ilha passa de 40 minutos sozinha.
rede: BLOQUEADA em 2026-10-27   # 20.2, REMEDIDA as 16h2xZ e NAO herdada do campo: NONO dia de recusa. jornadafly.com.br e www.jornadafly.com.br em 000 nas TRES passadas, com aquametria.com.br, robometria.com.br e clubedomosaico.com.br em 200 nas MESMAS tres — nove controles verdes contra seis bloqueios, zero intermitencia. O `__agentproxy/status` nomeia a causa: "gateway answered 403 to CONNECT (policy denial or upstream failure)". SEGUE SENDO REGRESSAO. bloqueada_por SEGUE null de proposito (a secao 2 reserva o campo para o que trava a ILHA; isto trava a FABRICA, e vai no despacho pela 12.2). NOVO HOJE, E E O ACHADO: o egresso NAO trava a coleta inteira. O degrau 4 da escada — operador lido por BUSCA — nunca esteve travado, e foi por ele que o Bondinho entrou. O que o egresso trava e o degrau 2, a leitura direta, que e o PREFERIDO pelo criterio de entrada. As DUAS portas medidas hoje: curl em 000 com 403 de politica, WebFetch em `getaddrinfo ENOTFOUND`.
ultima_ronda: null       # escrito pela Sentinela, nunca pela Fundacao (secao 2). `null` e a resposta certa e nao uma lacuna: pela decisao do Raphael de 28/09/2026, a ronda tecnica so alcanca ilha com URL servida, e esta ilha nao tem site. ACRESCENTADO EM 27/10/2026 pela carga do Bondinho: este cabecalho NUNCA teve este campo nem o `bloqueada_por` abaixo, e a regua de PRESENCA da secao 2 (a de 30/09/2026) os acusou nos dois. O despacho de 26/10 em `dados/despachos.md` afirma que a jornadafly estava COMPLETA — esta errado, e a errata esta no REGISTRO.md desta data.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: a secao reserva o campo para dependencia humana que trava a ILHA, e o que falta aqui (egresso e passos 2 a 8) trava a FABRICA — isso se escreve no despacho, que e o canal da 12.2. Preenche-lo tiraria a ilha da rotacao da secao 1 e congelaria tambem os blocos que nao precisam de rede, que foram justamente os desta execucao.
bloco_atual: |
  A COLETA ANDOU COM A REDE FECHADA, e isso e o achado. Entrou o PARQUE BONDINHO PAO
  DE ACUCAR — quinta experiencia, quinta cidade e a PRIMEIRA BRASILEIRA do banco —, e
  com ela nasceu a entidade ELEGIBILIDADE: o preco de quem prova o que NAO e idade.
  Esquema e banco na versao 8. 5 experiencias, 5 cidades, 16 versoes, 11 fontes, 13
  faixas etarias, 2 elegibilidades, 11 declaracoes.
  POR QUE A ELEGIBILIDADE NASCEU, e nasceu de DADO e nao de previsao: o operador vende
  o MESMO Bilhete Bondinho por R$ 205, R$ 160 e R$ 89. O que muda nao e quantidade,
  nem escopo, nem momento — os tres eixos que este esquema tinha. E QUEM COMPRA: R$ 160
  de quem nasceu E mora no Brasil, R$ 89 de quem nasceu OU reside no estado do Rio.
  `faixa_etaria` tambem nao servia, porque o esquema diz que o `se_nao_cumprir` dela e
  "o que o operador cobra de quem nao prova a IDADE". Sem a entidade havia duas saidas
  e as duas erradas: inventar um eixo que o operador nao vende, ou publicar os R$ 205
  numa ilha em portugues do Brasil quando o operador cobra 28% MENOS do proprio leitor.
  E ELA FECHA UMA DIVIDA DE 15/09/2026: o `motivo_sem_faixa_etaria` do Coliseu diz por
  extenso que a divergencia sobre a gratuidade "nao entra em faixa_etaria porque
  faixa_etaria guarda PRECO, e aqui o que existe e uma divergencia sobre quem tem
  direito". QUEM TEM DIREITO e o que a ELEGIBILIDADE guarda. Segue null, porque as duas
  fontes dela sao nivel 6 e o nivel 6 nao sustenta nada sozinho — mas a divida saiu de
  prosa dentro de um motivo e passou a ter campo, nome e endereco de releitura.
  A SOMA NAO SE PRESUME, E TEM NUMERO: `acumula_com_faixa_etaria` nasceu obrigatorio
  porque metade de R$ 89 e R$ 44,50 e o operador cobra R$ 44 por crianca moradora do
  Rio. Somar publicaria cinquenta centavos inventados numa conta que pareceria certa.
  TRES DEFEITOS DA MESMA FAMILIA, em tres ferramentas, nenhum deles da elegibilidade:
  (1) o contador `experiencias_com_preco_em_brl` do validar-banco.py vivia DENTRO do
  ramo de ERRO da conferencia de moeda e publicava 0, que era a verdade por ACIDENTE;
  (2) o teste-f1.py afirmava que "R$ nunca aparece": 288 frases de tela carregam R$
  legitimamente hoje (contadas depois do conserto, varrendo a F1 de 1 a 12 pessoas) e ele
  reprovava todas; (3) a f1-referencia.py somava IOF de 3,5% em TODA versao e publicou
  R$ 144,90 num bilhete de R$ 140 — imposto de compra internacional numa compra que nao
  sai do pais. O TERCEIRO E O PIOR: os dois primeiros erram alto, e esse cobrava do
  leitor um imposto que ele nao paga, com a aritmetica certa. Os tres sao reguas
  escritas num mundo sem real, as tres certas enquanto o mundo nao mudou.
  O OPERADOR DISCORDA DE SI MESMO em QUATRO numeros (205/185, 89/80, 160/150, 285/295),
  no mesmo dominio e no mesmo dia. A escada desta ilha resolve conflito ENTRE niveis e
  nao previu a fonte que discorda DE SI: foi preciso quebra-la em duas fontes para a
  divergencia poder ser gravada. O Acesso Rapido ficou com `preco: null` de proposito —
  a `resolucao` e de UMA versao por experiencia, e preco errado por R$ 10 na pagina do
  dinheiro custa mais que preco ausente com a causa escrita.
  O ITEM 6 DA FILA DESTRAVOU: `bondinho.com.br` e o PRIMEIRO dos 25 candidatos com
  ferramenta ofertavel (a F1). Era pre-registrado, com o dominio escrito pelo nome. O
  criterio errou o ROTULO — ele pede "operador privado" e o Bondinho e
  `concessionaria_de_bem_publico`, o mesmo tipo da SETE da Torre Eiffel, entao
  `operador_privado` SEGUE SEM LASTRO. As tres condicoes que ele cobra de fato estao
  cumpridas. E o que NAO destravou foi a rede: o degrau 4 da escada (operador lido por
  BUSCA) nunca esteve travado, e tres execucoes fecharam em "nada elegivel" antes disto.
  DUAS PRIMEIRAS a mais: primeiro preco em `BRL_do_operador` (vocabulario sem lastro
  desde 14/09) — logo o primeiro total que chega ao leitor sem cambio, que esta pendente
  — e primeiro `afiliado.url_produto` que e o MESMO produto do registro, em 43 dias de
  tentativas.
  NENHUM PORTAO NOVO NASCEU (31.2) e a bancada segue com TREZE comandos: a regua da
  elegibilidade mora dentro do validar-banco.py, as quebras dentro do mutacoes-banco.py
  e a da F1 dentro do teste-f1.py. BANCADA 0 FALHA em DOZE dos treze: mutacoes-banco de
  154 para 178 casos, teste-f1 229.768 afirmacoes, mutacoes-f1 28, mutacoes-f2 51,
  teste-prospeccao 287, mutacoes-prospeccao 40. O DECIMO TERCEIRO, `mutacoes-f3`, ainda
  rodava quando o commit saiu e esta dito assim na tabela do REGISTRO em vez de
  arredondado — ele roda o teste-f3 45 vezes, e a quinta cidade levou a grade da F2 de
  3.077 para 3.846 estados, o que tornou as duas baterias longas bem mais lentas. A
  proxima execucao que o vir fechar reescreve aquela linha.
  E a regua do `sem_extrator`, que nasceu em 22/10, REPROVOU na hora o vocabulario novo
  sem extrator — primeira vez cobrada por um caso que nao era dela.
  NADA FOI AO AR, E NAO PODIA: sem WordPress nao ha casca, Sync, /status nem URL.
  A 31.1 vai de 4 em 14 para 4 em 15, dito sem maquiagem.
  PROXIMO PASSO, E AGORA EXISTE UM DA FUNDACAO: a coleta por busca no degrau 4 funciona
  com a rede fechada. O 5b pede 3 experiencias na mesma cidade e o Rio tem 1; o 5c pede
  3 free tours com operador nomeado, e `free_tour` segue sem lastro. Do Raphael nao
  mudou nada — e saiu da lista dele "o egresso destrava a coleta": ele destrava o
  degrau 2, que e o preferido, mas o degrau 4 nunca esteve travado.
---

# Estado da ilha JORNADAFLY

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: **`jornadafly.com.br` — JÁ REGISTRADO E PAGO em 13/09/2026** (registro.br, titular RAPHAEL NATAL, expira 13/09/2028). Em 14/09 ainda não respondia DNS, o que é o esperado para domínio registrado sem nameserver apontado.
- Hospedagem: domínio adicional no mesmo plano da HostGator, **com raiz própria** `/home3/<usuário>/jornadafly`. Pendente.
- Nameservers: `ns604` e `ns605.hostgator.com.br`, **só DEPOIS do domínio adicional existir no cPanel**. Pendente.
- Search Console: propriedade de **Domínio**, **antes do WordPress**. Pendente.
- WordPress: pendente.
- Snippet de Sync: `JornadaFly Sync`, token novo. Pendente.
- Programas de afiliado: **nenhum cadastrado ainda**, e há uma ordem obrigatória — ver o `PROMPT.md`, seção "Específico desta ilha".

## O que já foi entregue
- **Bloco 1 — corpus de buscas paramétricas**, em `dados/corpus-buscas.md`
  (14/09/2026, 15h19Z). 15 consultas medidas em pt-BR, três eixos mais o cluster
  free tour, procedência domínio a domínio. Sem número de volume de busca (não
  há ferramenta) e sem preço que sirva ao banco (o banco só aceita preço colhido
  na fonte de quem opera, com `data_leitura`).
- **Bloco 2 — especificação das ferramentas**, em
  `dados/especificacao-calculadoras.md` e `dados/constantes.json` (14/09/2026,
  17h45Z). As três ferramentas com entrada, saída, régua de divergência e
  **recusa declarada**; a pergunta aberta do bloco 1 medida em seis consultas
  novas e **negada**; a tarifa da gôndola resolvida na fonte que a tabela
  (Comune di Venezia, Delibera 89 de 20/04/2023). Seis constantes: três
  publicáveis, duas pendentes por falta de canal, uma que **não tem valor único
  no mundo** e por isso é entrada do leitor.

- **Blocos 3 e 4 — o banco e as três ferramentas como REGRA** (22/10/2026).
  `dados/esquema-banco.json` e `dados/experiencias.json` na **versão 7**, com as
  entidades `EXPERIÊNCIA`, `FAIXA_DIÁRIA` e `COBERTURA_DO_PASSE`; e as três
  âncoras em `ferramentas/f1-referencia.py`, `f2-referencia.py` e
  `f3-referencia.py`, com os arquivos de resposta gerados e `publicar: false`.
- **Bloco 5 — artigos-âncora**, em `ferramentas/artigos-referencia.py` e
  `dados/artigos-ancora.json` (23/10/2026, 10h17Z). **Quatro escritos** — gôndola
  de Veneza, Torre Eiffel, Coliseu de Roma e Angkor Pass —, todos na mãe
  `/guias/quanto-custa/`, com 44 linhas de tabela, 74 parágrafos de dobra e 14
  perguntas de FAQ. **O artigo é montado do banco, nunca redigido:** toda frase de
  preço sai da `f1-referencia.py`. E **dois pré-registrados** (o da F2 e o da F3),
  que esperam dado de coleta e não trabalho de escrita.

## O que está travando

> **A PRIMEIRA LINHA DESTA SEÇÃO JÁ NÃO VALE — ponteiro do Pente Fino em 21/09/2026.** O cabeçalho deste mesmo arquivo registra `rede: aberta em 2026-09-18`, medido às 12h35Z com **HTTP 200 e sem redirecionamento para www**, e o `dados/PAINEL.md` da ronda de 18/09 confirma. A rede **não trava mais o 3b**; o que trava o 3b hoje é o site não existir. O texto de 14/09 fica abaixo, inteiro, porque é o que foi medido naquele dia — mas não é o estado de hoje.

- **A REDE DA ILHA, medida em 14/09/2026 às 15h22Z.** `jornadafly.com.br` e
  `www.jornadafly.com.br` devolvem **000** (o proxy recusa o CONNECT por
  política da organização) enquanto `aquametria.com.br` e `robometria.com.br`
  devolvem **200 na mesma passada**. Não é o túnel. A causa é a **seção 20.1**:
  o domínio nunca entrou na lista "Domínios permitidos" dos ambientes de nuvem.
  **Despacho de prioridade ALTA para o Raphael** em `dados/despachos.md`.
  - **O que isso NÃO trava:** blocos 2 e 3 (especificação e modelo do banco) são
    arquivo no repositório e não tocam o site.
  - **O que trava:** o **3b em diante**. Casca no ar que a Fundação não consegue
    abrir é exatamente o que a 20.1 existe para impedir — e a ilha tem 0 URL com
    o relógio do Google correndo desde 13/09.
  - Por isso `bloqueada_por` segue `null`: preenchê-lo tiraria a ilha da rotação
    da seção 1 e congelaria também os blocos que não precisam de rede.
- **A seção pendente do `VOZ.md`**: as 10 a 15 legendas reais do @jornadafly. É
  do Raphael e o `PROMPT.md` a exige **antes da primeira página**.
- **A identidade visual** precisa da aprovação dele antes do bloco 3b.
- Não existe `manifest.json` nesta ilha, e isso é correto por ora: nada é
  publicável, e criá-lo vazio seria inventar infraestrutura antes do WordPress.

---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-27T17:09Z   # BLOCO ENTREGUE: a carga do Parque Bondinho Pao de Acucar (5a experiencia, 1a brasileira) e a entidade ELEGIBILIDADE, esquema e banco na versao 8. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-10-27T19:49Z   # reserva RENOVADA pela 1.1 (terceira renovacao): a bancada desta ilha passa de quarenta minutos sozinha, e a bateria de mutacoes da F3 roda o teste-f3 45 vezes. Reserva original as 19h18Z. A hora saiu do `date -u` na mesma linha de comando que a grava.
rede: BLOQUEADA em 2026-10-27   # 20.2, REMEDIDA as 16h2xZ e NAO herdada do campo: NONO dia de recusa. jornadafly.com.br e www.jornadafly.com.br em 000 nas TRES passadas, com aquametria.com.br, robometria.com.br e clubedomosaico.com.br em 200 nas MESMAS tres — nove controles verdes contra seis bloqueios, zero intermitencia. O `__agentproxy/status` nomeia a causa: "gateway answered 403 to CONNECT (policy denial or upstream failure)". SEGUE SENDO REGRESSAO. bloqueada_por SEGUE null de proposito (a secao 2 reserva o campo para o que trava a ILHA; isto trava a FABRICA, e vai no despacho pela 12.2). NOVO HOJE, E E O ACHADO: o egresso NAO trava a coleta inteira. O degrau 4 da escada — operador lido por BUSCA — nunca esteve travado, e foi por ele que o Bondinho entrou. O que o egresso trava e o degrau 2, a leitura direta, que e o PREFERIDO pelo criterio de entrada. As DUAS portas medidas hoje: curl em 000 com 403 de politica, WebFetch em `getaddrinfo ENOTFOUND`.
ultima_ronda: null       # escrito pela Sentinela, nunca pela Fundacao (secao 2). `null` e a resposta certa e nao uma lacuna: pela decisao do Raphael de 28/09/2026, a ronda tecnica so alcanca ilha com URL servida, e esta ilha nao tem site. ACRESCENTADO EM 27/10/2026 pela carga do Bondinho: este cabecalho NUNCA teve este campo nem o `bloqueada_por` abaixo, e a regua de PRESENCA da secao 2 (a de 30/09/2026) os acusou nos dois. O despacho de 26/10 em `dados/despachos.md` afirma que a jornadafly estava COMPLETA — esta errado, e a errata esta no REGISTRO.md desta data.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: a secao reserva o campo para dependencia humana que trava a ILHA, e o que falta aqui (egresso e passos 2 a 8) trava a FABRICA — isso se escreve no despacho, que e o canal da 12.2. Preenche-lo tiraria a ilha da rotacao da secao 1 e congelaria tambem os blocos que nao precisam de rede, que foram justamente os desta execucao.
bloco_atual: |
  O DIA SEGUINTE DA ELEGIBILIDADE, em algumas horas. Entrou o TREM DO CORCOVADO —
  sexta experiencia, SEGUNDA do Rio de Janeiro — e nasceu `provas_adicionais`: a
  tarifa que exige MAIS DE UMA PROVA na porta. Esquema e banco na versao 9.
  6 experiencias, 5 cidades, 17 versoes, 14 fontes, 16 faixas etarias, 5
  elegibilidades, 14 declaracoes e 3 tarifas com prova adicional.
  O DADO QUE NAO CABIA: o operador cobra R$ 70 de "idosos acima de 60 anos, APENAS
  BRASILEIROS" e R$ 107 de estudante e de ID Jovem "apenas para brasileiros". A
  versao 8 aprendeu O QUE se prova e supunha que se prova UMA coisa. As duas saidas
  disponiveis mentiam: enfiar a nacionalidade na prosa de `condicao` da FAIXA_ETARIA
  briga com o que o esquema diz dela desde 14/09 (o `se_nao_cumprir` dela e "o que o
  operador cobra de quem nao prova a IDADE") e prometeria R$ 70 ao estrangeiro de 65
  anos que paga R$ 134; chamar a tarifa inteira de ELEGIBILIDADE perderia a idade,
  que e metade do preco.
  CADA PROVA DIZ O QUE SE PAGA SEM ELA, e isso nasceu de um defeito desta passada: a
  primeira versao da frase da F1 emprestava o `se_nao_cumprir` DA TARIFA e imprimiu
  "sem isso, quem nao prova a IDADE paga R$ 134" para quem nao provou a
  NACIONALIDADE. Aritmetica certa, pessoa errada — a familia do IOF somado a compra
  que nao sai do pais, consertado nesta ilha poucas horas antes.
  `condicao_de_deficiencia` e o quarto valor de `o_que_se_prova`, nascido no commit do
  primeiro registro que o usa. NAO e `vinculo_declarado`: vinculo e relacao com
  instituicao que pode acabar; deficiencia e condicao da pessoa, provada por laudo ou
  cartao proprio — e chamar as duas pelo mesmo nome faria a tela PEDIR CARTEIRINHA DE
  QUEM PRECISA DE LAUDO. Ela fecha a metade que o Bondinho recusou gravar na mesma
  manha: aquela fonte empacotava idade, vinculo e deficiencia em "meia-entrada" sem
  preco por categoria; ESTE operador desempacota. O que era ingravavel la e gravavel
  aqui, e o que mudou foi a FONTE, nao a regra.
  O DEFEITO DE VESPERA, E E O MAIS CARO DESTA PASSADA: `elegibilidade_da_versao`
  nasceu hoje de manha, calcula as frases e as grava na resposta, e `imprimir()`
  NUNCA AS IMPRIMIU. O leitor do Bondinho via "a promocional de brasileiro nao se
  soma ao desconto por idade" — a recusa chegava a tela — SEM NUNCA VER QUE A
  PROMOCIONAL EXISTE E CUSTA R$ 160 CONTRA R$ 205. Causa: `imprimir()` nao era
  conferido por NENHUM portao. A afirmacao que nasceu e geral de proposito — toda
  frase que a resposta manda para a tela tem de estar na tela.
  A MESMA ASSINATURA UM ANDAR ABAIXO: a regua do `sem_extrator` (22/10) guarda
  VOCABULARIO novo sem extrator e nao alcanca CAMPO novo que carrega vocabulario
  velho. `provas_adicionais` nasceu usando `nacionalidade` em tres tarifas e o aviso
  de lastro continuou dizendo que `nacionalidade` nao tinha registro que o usasse.
  Consertado na mesma passada.
  TRES VEZES O PORTAO DECIDIU, DUAS CONTRA MIM: (1) `acumula_com_faixa_etaria: null`
  reprovado numa versao que TEM faixa etaria — virou `false`, e aqui a pergunta nao
  custa dinheiro, porque estudante e R$ 107 e a faixa de 7 a 11 anos tambem; (2) a
  `condicao` do ID Jovem dizia "de 15 a 29 anos" e foi reprovada pela regua de 27/10
  — ela esta CERTA, porque aquela faixa e a regra com que o GOVERNO emite a carteira,
  nao tarifa que o operador cobra por idade; o conserto foi no LUGAR DO DADO; (3) a
  regua que EU escrevi varria `declarado_como` e reprovou duas tarifas certas —
  `declarado_como` e CITACAO, e censurar a citacao para agradar ao portao e pior que
  o defeito que ele procura.
  PRIMEIRO REGISTRO SEM EIXO DE VERSAO: o operador vende UM produto e as seis linhas
  que o site chama de "tipos de bilhete" dao o MESMO trem com o MESMO acesso. Por
  isso ele, e nao o Bondinho, mostrou a lacuna — aqui o preco muda SO por quem compra.
  A PERGUNTA DA LINGUA, que ninguem previu: as paginas do operador que a busca
  devolveu nomeadas sao as de /en e /es. A pagina em PORTUGUES deste operador
  brasileiro nao voltou em nenhuma das tres passadas. O numero vale (mesmo operador,
  mesmo dominio, nivel 4) e a releitura tem de conferir primeiro a tabela em
  portugues. Esta em `nota_da_lingua` da fonte.
  A DIVERGENCIA QUE ESTE REGISTRO NAO DESEMPATA: travel.com.br diz R$ 122,50 de
  adulto em "alta temporada" sem data de tabela, e R$ 67 de infantil "de 5 a 11
  anos" (divergencia DUPLA: preco e recorte de faixa). A `regra_de_divergencia` da
  autoridade so aos niveis 1 e 3 e a escada diz que "o nivel mais alto vence" — duas
  leituras para nivel 4 contra nivel 6. Aqui as duas dao R$ 134, entao a pergunta
  fica escrita na nota da versao 9 PARA O DIA EM QUE O NIVEL 6 PUBLICAR O MAIOR.
  `url_produto` VOLTOU A SER null, e nao e regra nova: a plataforma devolveu
  /br/rio-de-janeiro/tour-cristo-redentor-trem/ e o slug diz TOUR — a mesma decisao
  do Angkor e do Coliseu. No Bondinho a pagina se chamava "Ingresso para o Pao de
  Acucar" e por isso o campo deixou de ser null la. Mesma regra, outro produto.
  A ARVORE FOI RECONTADA e o criterio do 5b NAO foi mexido: o Rio e a primeira cidade
  deste banco com DUAS experiencias, e o criterio pre-registrado pede TRES. Fica
  escrita uma pergunta que ele nao previu: a terceira mais facil de colher pelo mesmo
  degrau 4 (as vans da Paineiras) e a terceira porta do MESMO monumento que o trem, e
  a 7.4 proibe duas paginas na mesma consulta_alvo. Criterio escrito depois do dado e
  criterio dobrado — a decisao provavel, escrita no ARVORE.md, e que trem e van sejam
  UMA experiencia com duas versoes por ponto de embarque.
  NADA FOI AO AR E NAO PODIA: sem WordPress nao ha casca, Sync, /status nem URL. A
  31.1 vai de 4 em 15 para 4 em 16, dito sem maquiagem.
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
  *(Esquema e banco na **versão 9** desde 27/10/2026, por duas cargas no mesmo dia: a
  do **Parque Bondinho Pão de Açúcar** às 16h25Z, que fez nascer a entidade
  `ELEGIBILIDADE` — o preço de quem prova o que não é idade —, e a do **Trem do
  Corcovado** às 19h18Z, que fez nascer `provas_adicionais` — a tarifa que exige mais
  de uma prova — e o valor `condicao_de_deficiencia`. São **6 experiências em 5
  cidades**, e o Rio é a primeira cidade com duas. Ver as seções **9** e **10** da
  `especificacao-calculadoras.md`.)*
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

---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-22T16:59Z
executando_desde: 2026-10-22T19:16Z   # reserva da execucao de 22/10 19:16Z (passo 5 da secao 1, via 1.2 passo 2). A hora sai do `date -u` na mesma linha de comando que a grava.
rede: BLOQUEADA em 2026-10-22   # 20.2, REMEDIDA as 16h2xZ e NAO herdada do campo: TRES passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas tres (6 medicoes), com aquametria.com.br e robometria.com.br em 200 nas tres (6 de controle, nenhuma intermitencia). O curl verbose nomeia a causa e ela nao e tunel: `CONNECT tunnel failed, response 403` do proxy de egresso, ou seja o dominio NAO esta na lista de Dominios permitidos deste ambiente. SEGUE SENDO REGRESSAO (o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia), e o despacho ALTA de 15/09 em dados/despachos.md continua valendo. E DUAS FONTES NOVAS ENTRARAM NO BLOQUEIO, medidas hoje pela 20.3 porque a entidade FAIXA_DIARIA as exige: numbeo.com e www.booking.com em 000, com www.civitatis.com.br (ja listado) tambem em 000 e raw.githubusercontent.com em 301 ao lado. O que a rede trava e o 3b em diante e a COLETA das faixas, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas seis execucoes anteriores.
bloco_atual: |
  A F2 EXISTE COMO REGRA, e a pergunta aberta que ela trazia virou uma ENTIDADE. O
  registro anterior deixou escrito "a F2 soma hospedagem, alimentacao e transporte
  local, e nenhuma das tres esta no banco". A resposta nao era campo novo na
  EXPERIENCIA: e que as tres NAO SAO DA MESMA NATUREZA que uma experiencia.
  Experiencia tem preco colhido no site de quem opera, com data de leitura; diaria de
  hotel e FAIXA QUE UM TERCEIRO PUBLICOU. Dai a entidade propria FAIXA_DIARIA, e nao
  um campo da CIDADE: campo na CIDADE forcaria escolher UM publicador por cidade na
  carga, que e decisao editorial disfarcada de modelagem.
  NADA FOI AO AR, e nao podia ter ido: esta ilha nao tem site, nao tem WordPress, nao
  tem Sync e nao tem /status. Dizer que verifiquei no ar seria inventar.
  REDE REMEDIDA E NAO HERDADA (20.2): 6 medicoes de bloqueio contra 6 de controle
  verde, com `CONNECT tunnel failed, response 403` nomeado no verbose. Segue regressao.
  O QUE SAIU: ferramentas/f2-referencia.py (o cerebro), ferramentas/gerar-f2.py,
  dados/f2-respostas.json (3.077 estados servidos, 197 gravados, publicar false),
  ferramentas/teste-f2.py e ferramentas/mutacoes-f2.py. Esquema versao 6, banco 6.
  A TROCA E A MESMA DA VERSAO 5 UM ANDAR ACIMA: la a quantidade de uso de cada bilhete
  saiu da prosa do `rotulo` para `dias_de_uso`; aqui o que sai da prosa e O QUE O
  NUMERO SIGNIFICA. O bloco 1 mediu duas frases na MESMA pagina de resultados — "media
  de R$ 203,87 nos ultimos 30 dias" e "a diaria mais baixa encontrada foi R$ 396,84" —
  e a distincao entre elas morou em ressalva de leitura humana por 38 dias. Agora e
  `o_que_o_numero_e`, que e enum, e a regra "faixa de natureza diferente nao se soma"
  passou a ser COMPUTAVEL: somar uma media com um minimo da um intervalo que NINGUEM
  publicou.
  E A BASE E DECLARADA, NUNCA DEDUZIDA. `base` diz se o numero e por pessoa, por QUARTO
  ou pelo grupo; base de quarto exige `pessoas_por_quarto` e o numero tem de APARECER na
  frase da fonte. Quarto e unidade de capacidade como gondola: 6 pessoas numa diaria de
  quarto duplo sao TRES quartos, e a F2 CHAMA `unidades_necessarias` da F1 em vez de
  reescrever a conta. Faixa de quarto sem ocupacao NAO escala e a linha e recusada.
  A F2 PUBLICA UMA LINHA DE QUATRO HOJE, por falta de DADO e nao de regra: zero faixas
  no banco, e as duas unicas frases de diaria que esta ilha mediu foram guardadas SEM o
  nome de quem as publicou, sem URL e sem data. Carregar hoje exigiria inventar o dono
  do numero. A coleta nao e desta nuvem: numbeo.com, booking.com e civitatis.com.br em
  000, com raw.githubusercontent.com em 301 na mesma passada.
  OS PORTOES ACHARAM SETE DEFEITOS NA MINHA PROPRIA FERRAMENTA, todos antes do commit:
  (1) faixa de LARGURA ZERO — duas versoes de preco igual davam pontas de versoes
  DIFERENTES, e a tela publicava "de A a B" para um intervalo que nao e intervalo;
  (2) A FRASE QUE MENTIA SOBRE SIEM REAP, a pior das cinco — a F2 descartava quem nao
  fosse `publicavel` e a pagina dizia "esta ilha ainda nao leu o preco de nenhuma
  experiencia em Siem Reap", sendo que o passe de Angkor esta lido e gravado, so nao
  reconferido; e o mesmo item aparece na F1 COM RESSALVA e DESAPARECIA aqui, de modo que
  quem viesse de uma pagina para a outra veria a experiencia sumir. Quem achou foi o
  GERADOR, pela contagem: 2.268 estados com a linha nossa onde a grade pedia 3.024;
  (3) a concordancia — "as 1 experiencias que esta ilha leu custam";
  (4) O TETO DE DIAS QUE O PORTAO NAO TINHA COMO VER: a mutacao que trocou 21 por 60
  PASSOU, porque grade, bordas e a conta do que esta "fora" saiam todas de
  `f2.DIAS_MAXIMO`. Regua que toma o limite da coisa que ela mede nao mede o limite;
  (5) A MOEDA QUE A F1 CONFERE E A F2 NAO CONFERIA: tirar EUR do vocabulario PASSOU,
  porque `dinheiro()` olha o proprio dicionario de simbolos e nunca o vocabulario.
  (6) A CONTAGEM QUE SO UM MUNDO DE BANCADA PODIA MOSTRAR: o gerador contava os
  estados com total sobre o DOMINIO e o portao comparava com o arquivo RECORTADO. Com
  zero faixas os dois valem 0 e era invisivel — o mundo com as tres faixas carregadas
  mostrou, 252 contra 12. Sao dois numeros agora;
  (7) UMA FUNCAO MINHA SOBRESCREVEU UMA FUNCAO DA BATERIA DO BANCO, em silencio:
  `q_faixa_sem_data_de_leitura` ja existia para a faixa ETARIA, e a mutacao antiga passou
  a rodar a minha funcao. "Faixa" nesta pasta significava faixa etaria antes de hoje; a
  entidade nova e faixa DIARIA e os nomes dizem isso. Quem pegou foi a exigencia da
  FRASE: a mutacao antiga continuava `reprova`, e um relatorio que se contentasse com
  "reprovou" teria dito ok.
  AS REGRAS NOVAS DO VALIDADOR NAO FICARAM SEM BATERIA, e isso quase aconteceu: ~80
  linhas de regua para uma entidade com ZERO registros no banco nao seriam executadas por
  ninguem — o mesmo defeito que eu consertei um andar abaixo neste bloco. mutacoes-banco
  passou de 93 para 117 (16 mundos, 101 quebras, 57 cobradas pela frase), com as 24 novas
  carregando faixa EM MEMORIA e quebrando cada regra, inclusive a ocupacao achada DENTRO
  de outro numero (o 2 de 2400, a armadilha que o dias_de_uso pagou). Nenhuma faixa foi
  gravada no banco.
  E UM DEFEITO QUE NAO E DESTE BLOCO E JA ESTAVA NA PASTA: validar-banco.py conferia o
  crescimento de vocabulario contra SETE nomes digitados e o esquema tinha NOVE —
  `declarada_por` e `canal_de_leitura` nunca foram conferidos por ninguem, em silencio,
  desde 15/09/2026. Mesma familia da lista de portoes que a aquametria matou com o
  descobridor. So acrescentar os quatro novos a lista teria RENOVADO o defeito: a regua
  agora varre `vocabularios` do esquema e vocabulario sem extrator vira ERRO. Na
  primeira passada ela achou o que a lista escondia: `leitura_direta` sem lastro. E saiu
  `versao_esquema`, que dizia 4 enquanto `versao` dizia 5.
  O ARQUIVO GRAVADO NAO TRAZ OS 3.077 ESTADOS: gravalos deu 13 MB contra 858 KB do
  arquivo da F1. Ele leva o que a pagina le — a tabela e TODAS as bordas, 679 KB — e a
  prova da grade mora no portao, que a varre em cada passada.
  BANCADA, 0 falha: validar-banco verde; mutacoes-banco 117 de 117; teste-f1 139.658
  afirmacoes; mutacoes-f1 28 de 28; teste-f2 213.586 afirmacoes sobre os
  3.077 estados; mutacoes-f2 44 de 44 — 9 mundos, 25 quebras e 10 mortes, com 28 cobradas pela frase.
  PROXIMO PASSO: a F3 como REGRA (o passe da cidade vale a pena), e ela comeca pelo
  BANCO e nao pela ferramenta — nenhuma das quatro experiencias e `passe_de_cidade`, o
  vocabulario tem o valor e nenhum registro o usa, e o Roma Pass e o Lisboa Card que o
  corpus mediu nao estao carregados. O item mais caro desta ilha continua sendo a casca
  (3b): passos 2 a 8 da secao 11 e a liberacao do dominio no egresso, as duas do Raphael.
ultima_ronda: null   # escrito pela Sentinela; esta ilha nunca teve ronda
bloqueada_por: null
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

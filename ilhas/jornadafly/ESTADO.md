---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-09-15T12:05Z
executando_desde: null
rede: aberta em 2026-09-18   # 20.1: jornadafly.com.br entrou na lista de Dominios permitidos da conta. MEDIDO em 18/09 as 12h35Z: HTTP 200, sem redirecionamento para www. O bloqueio de 15/09 acabou.
bloco_atual: |
  CARGA DO BANCO, SEGUNDA PASSADA — entram o COLISEU DE ROMA e a TORRE EIFFEL, e o banco vai de 2 para 4 experiencias, de 5 para 11 versoes, de 2 para 4 cidades e de 5 para 7 fontes (esquema versao 3, banco versao 3). Os dois sao ingresso_de_sitio_publico, que e o tipo que a carga de 14/09 mediu como o unico reproduzivel enquanto o egresso estiver fechado — e era exatamente a lista curta que aquele registro deixou nomeada. NADA foi ao ar: esta ilha nao tem site, nao tem Sync e nao tem /status, e dizer que verificou no ar seria inventar.
  A ESCOLHA DA ILHA: SEGUNDA TENTADA, UMA PERDIDA NA CORRIDA DO PUSH. Os cinco ESTADO.md do main real parseiam em yaml.safe_load e os cinco estavam com executando_desde null, que pela 1.1 ja significa que nenhum bloco da Fundacao esta vivo — nao houve reserva vencida para o git desempatar. Pela 18.1 li o topo dos cinco PROMPT.md antes da rotacao e NENHUMA ilha tem despacho com item acionavel pela Fundacao: o da robometria, da Sentinela de 14/09, tem os itens 1, 2 e 3 CUMPRIDOS, o 4 dependendo da sessao logada da Shopee e o 5 sendo achado de metodo endereçado ao Raphael; os da ohmetria e da jornadafly sao de NASCIMENTO, que carregam a fila inteira e nao cabem na 18.2; os da aquametria e da clubedomosaico estao fechados. Sobrou a rotacao da secao 1. Pedi a OHMETRIA, que era a mais antiga (21h20Z), e o push foi RECUSADO: outras duas execucoes tinham reservado a aquametria as 11h16Z e a ohmetria as 11h17Z. Voltei ao passo 2 sem force push; sobraram tres, com jornadafly e robometria empatadas em 23h35Z e prioridade 1, e o desempate alfabetico da a jornadafly. Reserva aceita as 11h25Z. Nenhum PR aberto; as branches claude/* do repositorio estao todas mescladas ou sao anteriores a uma reescrita de historia do main.
  REDE PELA 20.2, RETESTADA E NAO HERDADA: TRES passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas tres, com aquametria.com.br e robometria.com.br em 200 nas mesmas tres. Seis medicoes de bloqueio contra seis de controle verde, igual as tres execucoes anteriores. Segue bloqueada, e bloqueada_por segue null de proposito: o que a rede trava e o 3b em diante, nao o bloco de arquivo.
  A PERGUNTA DA MOEDA FOI RESPONDIDA, E A RESPOSTA NAO ERA NENHUMA DAS DUAS QUE ESTAVAM POSTAS. A carga de 14/09 deixou escrito que quem gravasse a proxima cidade decidiria se o vocabulario de moeda cresce ou se o banco fica restrito a tres. Nasceu no esquema a regra_de_crescimento_de_vocabulario: valor de vocabulario controlado nasce JUNTO com o primeiro registro que o usa, nunca antes. Entao JOD, AED, ARS e VND NAO entram hoje, e o motivo esta escrito — nenhum registro cobra nelas. Vocabulario que cresce por previsao vira promessa vazia, que e a cicatriz que a ohmetria pagou.
  E A REGRA FOI EXERCIDA NO MESMO COMMIT, por outro vocabulario: tipo_de_operador ganhou concessionaria_de_bem_publico porque a Torre Eiffel precisa dele. A SETE opera o monumento sob concessao da cidade de Paris; nao e o poder publico declarando tarifa nem uma empresa privada qualquer, e chamar de um dos dois seria por o numero na boca de quem nao o publicou.
  O COLISEU E O PRIMEIRO REGISTRO QUE FICA PUBLICAVEL POR NOMEAR PAGINA DE TARIFA, e nao um ato. A regra_do_documento_nomeado dizia desde que nasceu que o ato, a tabela OU a pagina de tarifa servem; ate hoje so o ato tinha sido exercido, pela gondola. A busca devolveu a pagina de horarios e bilhetes do proprio orgao e a pagina de categorias do sistema oficial de venda — que e a diferenca exata para o Angkor, cuja autoridade so devolveu perguntas frequentes e por isso segue pendente_de_releitura.
  A TORRE EIFFEL E O PRIMEIRO REGISTRO DE NIVEL 4 DESTE BANCO. O degrau do operador lido por busca estava marcado no esquema como existe_hoje false. A busca nao devolveu alguem falando da tarifa: devolveu as paginas de tarifa do proprio operador, UMA POR BILHETE, com o preco no titulo de cada uma — 14,80, 23,50, 28,00 e 36,70 euros, confirmados por uma segunda passada em outra lingua que trouxe a grade inteira por faixa etaria.
  O ACHADO DE MODELO, E OS DOIS REGISTROS SAO A PROVA: faixa_etaria e da VERSAO e o esquema a poe na EXPERIENCIA. Na Torre Eiffel a crianca de 4 a 11 anos paga 3,80 por escada e 9,20 por elevador ate o topo — a mesma faixa, quatro precos. So a gratuidade dos menores de 4 anos, que vale igual nos quatro bilhetes, cabe no campo como ele e hoje. Nao apareceu antes porque o mundo nao se movia: a gondola nao tem faixa etaria e a do Angkor vale igual nas tres versoes. Campo que so erra quando o mundo se move parece certo ate o mundo se mover.
  A DIVERGENCIA MAIS CARA QUE ESTA ILHA JA MEDIU PARA O LEITOR BRASILEIRO, e ela ficou FORA de declaracoes de proposito. As duas passadas do Coliseu discordam sobre a gratuidade para menores de 18 anos: a portuguesa diz que e so para cidadao da Uniao Europeia, a inglesa diz com todas as letras que vale para UE e nao-UE, e as duas ainda divergem entre 4 e cerca de 2 euros na reduzida de 18 a 25. Nenhuma e autoridade, entao a regra sem autoridade resolve pelo MAIOR e o adolescente brasileiro paga os 18 euros do adulto. Nao entrou em declaracoes porque declaracao, neste esquema, discorda de uma VERSAO — e faixa etaria nao e versao. Mesma raiz do achado acima, nomeada no esquema.
  EXISTE_HOJE VIROU CAMPO DERIVADO, E ERA A PROSA MAIS SILENCIOSA DO ESQUEMA. O validador passou a recomputar existe_hoje de cada degrau a partir das fontes do banco e a reprovar o gravado que discordar, nas DUAS direcoes. A direcao perigosa e o false velho: ele faz a ilha negar um degrau que ja alcancou, e nada no banco contradiz a frase. E a regua nova achou uma interacao no mesmo dia em que nasceu — reprovou um MUNDO que passava havia uma carga, o mundo sem divergencia, que apaga as fontes editoriais e por isso tem de apagar o degrau 6 junto. Regua que so mede o banco real e regua com metade do mundo desligada.
  A BANCADA PASSOU A COBRAR A FRASE, e nao so o veredito. Mutacao ganhou quinto elemento opcional: a frase que a quebra tem de ouvir de volta. Reprovar nao e a mesma coisa que reprovar PELO MOTIVO CERTO, e sem isso uma mutacao pode disparar outra trava, voltar verde e nunca ter medido a sua. Provado que morde: trocando a frase esperada de uma quebra por outra trava real, a bancada acusa e sai com codigo 1.
  BANCADA, 0 falha: validar-banco verde sobre o banco real, com as duas reguas novas. MUTACOES 53 (eram 49): 6 mundos que tem de PASSAR e 47 quebras que tem de REPROVAR, todas decidindo certo nos dois lados da fronteira, 3 delas cobradas pela frase. Cada mutacao nova foi provada nao inerte uma a uma: o mundo do degrau novo REPROVA se o esquema nao acompanhar o banco, e a cobranca por frase acusa quando a frase e trocada. As cinco contagens do resumo ficaram para tras quando os registros entraram e o validador reprovou as cinco antes do commit — numero que a ilha publica sobre si mesma nasce contado. Os tres JSON passam por json.load e o cabecalho por yaml.safe_load.
  O VALIDADOR PUBLICA VOCABULARIO_SEM_LASTRO A CADA PASSADA, que e a outra metade da regra de crescimento: hoje 4 de 6 em categoria, 3 de 5 em tipo_de_operador, 2 de 4 em unidade_de_preco, 1 de 3 em moeda e 1 de 3 em status_do_registro. Momento_do_dia e o unico com lastro inteiro. E AVISO e nao erro de proposito — os valores que o bloco 3 ja trazia sao anteriores a regra e nao viram defeito retroativo; o que fica proibido enquanto a lista nao for vazia e a ilha publicar frase de inexistencia.
  ACHADO DE HIGIENE QUE NAO E DESTA CARGA: os commits de 00h20Z, 00h32Z e 00h45Z de 15/09 fizeram o simbolo, a fonte e os quatro lockups desta ilha e NAO fecharam a execucao — nao ha entrada no REGISTRO.md, o cabecalho nunca foi tocado e nenhuma reserva foi escrita. Os arquivos estao no main e o DESIGN.md os documenta; o que falta e o rastro. Fica dito aqui para a proxima execucao nao procurar o registro que nao existe.
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

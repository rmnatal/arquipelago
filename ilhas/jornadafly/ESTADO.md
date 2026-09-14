---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-09-14T17:45Z
executando_desde: null
rede: bloqueada em 2026-09-14   # 20.1: o dominio nao esta na lista de Dominios permitidos. Despacho ALTO para o Raphael em dados/despachos.md
bloco_atual: |
  BLOCO 2 ENTREGUE — a especificacao das tres ferramentas. dados/especificacao-calculadoras.md (476 linhas) e dados/constantes.json (6 constantes: 3 publicaveis, 2 pendentes, 1 sem valor unico por natureza). NADA foi ao ar: esta ilha nao tem site, nao tem Sync e nao tem /status, e dizer que verificou no ar seria inventar.
  A ESCOLHA DA ILHA: SEGUNDA TENTADA. Os cinco ESTADO.md com executando_desde null, que pela 1.1 ja significa que nao ha bloco da Fundacao vivo. Pela 18.1 as duas ilhas nascidas em 14/09 tem o mesmo despacho do Raphael aberto, escrito no mesmo commit; empate desfeito pela rotacao da secao 1, e a ohmetria (ultima_execucao null) vinha antes. Meu push de reserva da ohmetria foi RECUSADO por cerca de um minuto — outra execucao a reservou as 17h17Z. Voltei ao passo 2 sem force push, e a jornadafly era a seguinte com despacho aberto. Reserva aceita as 17h20Z.
  REDE PELA 20.2, RETESTADA E NAO HERDADA: o ESTADO.md ja trazia 'rede: bloqueada em 2026-09-14', e a secao 4 manda retestar bloqueio herdado antes de respeita-lo. Retestado em duas passadas: jornadafly.com.br e www.jornadafly.com.br em 000 nas duas, aquametria.com.br em 200 na mesma passada. Segue bloqueada, e o bloco 2 nao toca o site.
  A PERGUNTA ABERTA DO BLOCO 1 FOI MEDIDA E ESTA NEGADA. A hipotese era que o muro do pt-BR cede onde nao existe portal veterano brasileiro cobrindo o destino. Seis consultas novas em tres continentes, e o contraexemplo vem dos DOIS lados: Petra nao tem portal veterano dedicado E nao tem plataforma; Angkor tem DOIS portais veteranos E tambem nao tem plataforma. Nenhuma cidade do banco muda de ordem, que era a unica decisao que a pergunta poderia mudar. O que aparece no lugar ficou escrito como leitura com o contraexemplo ao lado (o balao da Capadocia), nunca como criterio.
  O QUE APARECEU EM 100% DAS OITO CONSULTAS DOS DOIS BLOCOS, e e o que sustenta a ilha: ninguem data o preco, e A UNIDADE DO PRECO TROCA DENTRO DA MESMA RESPOSTA. Gondola (por veiculo), cruzeiro de Ha Long (por cabine, na mesma lista dos por pessoa), Petra e Angkor (por pessoa em escada de dias). Foi isso que especificou a F1: declarar a unidade, fechar a conta do grupo, datar o preco.
  A GONDOLA RESOLVIDA NA FONTE QUE TABELA: cinco leituras divergentes do mesmo preco nas paginas de topo, e o Comune di Venezia publicando 90 euros de dia (30 min) e 110 a noite (35 min), maximo 5 passageiros, pela Delibera della Giunta Comunale n. 89 de 20/04/2023. As duas paginas de topo que dizem '80 euros ate 4 pessoas' nao estao arredondando: estao TRES ANOS desatualizadas. Para 4 pessoas de dia a conta e 90 no total e 22,50 por pessoa — nao 80, nao 34 por pessoa.
  A REGRA DE DIVERGENCIA DESTA ILHA, com o erro caro nomeado antes da direcao (secao 10): havendo tarifa de poder publico, ela ganha; nao havendo autoridade, resolve para o valor MAIOR, porque quem chega com dinheiro a menos perde a experiencia na porta e quem chega com a mais volta com troco. Media proibida.
  O DIFERENCIAL QUE NAO DEPENDE DE NADA BLOQUEADO: o IOF de 3,5 por cento sobre compra internacional no cartao de pessoa fisica e PERCENTUAL, entao entra na conta na moeda do operador, sem taxa de cambio. Nenhuma das seis paginas medidas hoje menciona IOF e tres convertem para real sem declarar cambio nem data.
  CAI UMA LINHA DA PAGINA, E ESTA DITO: cambio-eur-brl e cambio-usd-brl nasceram PENDENTES porque nenhuma fonte de cotacao e alcancavel (awesomeapi, open.er-api e api.bcb.gov.br em 000, connect_rejected). Constante pendente e proibida em formula publicada (secao 10), entao a F1 publica na moeda do operador e diz ao leitor por que. Virou acrescimo ao despacho de rede que ja estava aberto, pedindo api.bcb.gov.br na mesma lista.
  A ESCADA DA SECAO 25 NAO SERVE COMO ESTA, E ISSO ESTA RESOLVIDO SEM COPIAR A FORMA: os quatro degraus da 25.1 sao de marketplace e nenhum existe neste nicho. O PRINCIPIO da 25.2 vale inteiro, e o piso desta ilha e a pagina de cidade da Civitatis (civitatis.com/br/<cidade>/), medida em dois destinos independentes, fabricavel sozinha a partir do campo cidade do banco. Sem programa cadastrado, o link nasce CRU e sem rel sponsored, porque sponsored declara relacao paga e ninguem paga por aquele clique.
  A ARMADILHA EM QUE EU MESMA CAI, E FICA ESCRITA: duas consultas desta execucao carregavam o numero que eu queria confirmar, o que a secao 8 proibe. As duas foram refeitas com pergunta limpa antes de qualquer gravacao, e as duas confirmaram por outros publicadores — a limpa da gondola ainda trouxe o ato (Delibera 89/2023) que a plantada nao tinha trazido. O que sustenta os dois numeros e a SEGUNDA passada, e e ela que esta citada.
  VERIFICACAO: nao ha site, Sync, /status nem URL para abrir. O que foi medido: quatro codigos HTTP da 20.2 (dois 000 e dois 200 de controle), tres codigos das fontes de cambio (000), o cabecalho passando por yaml.safe_load, o constantes.json passando por json.load, e uma afirmacao que compara o resumo do JSON com a lista CONTADA (nunca com numero digitado) e cobra que nenhuma constante pendente esteja em uso.
  PROXIMO, com ordem e motivo: (1) BLOCO 3, o modelo do banco, que esta bloco ja obriga a ter unidade_de_preco, capacidade_maxima, versoes, temporada, faixa_etaria, data_leitura e afiliado.url_busca_produto — nao depende de site nem da rede; (2) 3b em diante, TRAVADO pela rede e pela aprovacao da identidade; (3) a secao pendente do VOZ.md, que e do Raphael e vem ANTES da primeira pagina.
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

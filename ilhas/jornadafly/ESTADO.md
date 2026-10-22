---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-22T13:55Z
executando_desde: 2026-10-22T16:44Z   # reserva RENOVADA pela 1.1 as 16:44Z: o bloco passou de 40 minutos (a bancada sem rede desta ilha ja passa de 40 minutos sozinha, e a bateria de mutacoes da F2 roda o portao 45 vezes). Reservada as 16:20Z (passo 5 da secao 1), escrita antes de qualquer trabalho. A anterior: a execucao de 22/10 13h29Z fechou as 13:55Z. Reserva NAO renovada no meio do caminho e a 1.1 manda dizer por que: o bloco passou de 40 minutos, e o proximo commit que esta execucao fez FOI o de fechamento — renovar e grava-la null na mesma linha seriam a mesma escrita. Nenhuma outra execucao consultou o git nesta janela porque nenhuma outra tocou esta ilha.
rede: BLOQUEADA em 2026-10-22   # 20.2, REMEDIDA as 13h3xZ e NAO herdada do campo: TRES passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas tres (6 medicoes), com aquametria.com.br e robometria.com.br em 200 nas tres (6 de controle, nenhuma intermitencia nesta rodada). O curl verbose nomeia a causa e ela nao e tunel: `CONNECT tunnel failed, response 403` do proxy de egresso, ou seja o dominio NAO esta na lista de Dominios permitidos deste ambiente. SEGUE SENDO REGRESSAO: o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia, e o despacho ALTA de 15/09 em dados/despachos.md, dado como cumprido em 18/09, continua valendo. O que a rede trava e o 3b em diante, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas cinco execucoes anteriores desta ilha.
bloco_atual: |
  A F1 EXISTE COMO REGRA — o bloco 4 entregue, no desenho que a ohmetria usou: a
  referencia em Python (estado -> resposta inteira, em frase acentuada), o dominio de
  resposta gravado, a tabela pre-renderizada, o portao e as mutacoes. SEM PHP, e isso e
  decisao registrada: sem casca, um snippet so poderia ser medido por um render de
  bancada que serve MENOS do que o site serve, que e a cicatriz que a secao 8 mais cobra.
  O PHP, quando nascer, e TRADUTOR da referencia, frase a frase.
  NADA FOI AO AR, e nao podia ter ido: esta ilha nao tem site, nao tem WordPress, nao
  tem Sync e nao tem /status. Dizer que verifiquei no ar seria inventar.
  REDE REMEDIDA E NAO HERDADA (20.2): 6 medicoes de bloqueio contra 6 de controle verde,
  com `CONNECT tunnel failed, response 403` nomeado no verbose. Segue regressao.
  O QUE SAIU: ferramentas/f1-referencia.py (o cerebro), ferramentas/gerar-f1.py,
  dados/f1-respostas.json (154 respostas e 44 linhas de tabela, publicar false),
  ferramentas/teste-f1.py e ferramentas/mutacoes-f1.py. Esquema versao 5, banco versao 5.
  A CONTA 3 DA ESPECIFICACAO NAO ERA CALCULAVEL, e descobrir isso foi o bloco: ela manda
  mostrar "a partir de quantos dias a versao mais cara passa a valer", e a quantidade de
  uso de cada bilhete existia SO NA PROSA do rotulo ("3 dias, usaveis dentro de uma
  semana"). Nasceram `eixo_das_versoes` na EXPERIENCIA (por_quantidade | por_escopo |
  por_momento) e `dias_de_uso` na VERSAO, transcrito da frase da fonte — e a regua cobra
  que o numero APARECA no `declarado_como`, em digito ou por extenso. Mesma troca da
  versao 4 um andar acima: lá a faixa etaria saiu da prosa, aqui a quantidade.
  E O EIXO E DECLARADO, NUNCA DEDUZIDO DO ROTULO: ler o rotulo acertaria no Angkor e
  ERRARIA no Coliseu, cujos bilhetes diferem em ESCOPO e nao em quantidade. Dois
  ingressos de 24 horas NAO dao a area restrita da Experiencia Completa — ponto de
  equilibrio ali seria aritmetica certa sobre pergunta sem sentido. Das 4 experiencias:
  1 por_quantidade (Angkor, 1/3/7 dias), 2 por_escopo (Coliseu, Torre Eiffel) e 1
  por_momento (gondola).
  O PORTAO ACHOU DOIS DEFEITOS NA MINHA PROPRIA FERRAMENTA, os dois antes do commit:
  (1) a F1 publicava portugues SEM ACENTO na frase-resposta ("O preco e por veiculo"),
  que e a cicatriz da Robometria cometida dentro do arquivo escrito para nao a cometer;
  (2) e, atras do acento, um defeito maior — a F1 repassava os `motivo_*` do BANCO para a
  tela, e esses motivos sao escritos para a proxima execucao: citam nome de campo entre
  acentos graves, data de migracao e numero de secao. A pagina dizia ao visitante que "o
  esquema PROIBE faixa etaria onde a unidade nao e `por_pessoa`" — texto de bastidor da
  fabrica, que a 32.4 proibe. Mesma cicatriz que a ohmetria pagou com dados/modulos.json
  na tela. A F1 passou a ESCREVER a propria frase de tela; o motivo fica no banco.
  O `momento_do_dia` NAO E A QUARTA ENTRADA que a especificacao listava: ele e campo da
  VERSAO, e um seletor separado deixaria pedir "noturno" sobre a versao diurna — estado
  que o operador nao vende. O estado da F1 e (experiencia, versao, pessoas).
  BANCADA, 0 falha: validar-banco verde (os 5 avisos de vocabulario_sem_lastro onde
  estavam); mutacoes-banco 93 de 93 (eram 73), 39 cobradas pela frase; teste-f1 139.658
  afirmacoes sobre os 154 estados, com a aritmetica reescrita a mao em Fraction e a grade
  pisando na borda do GRUPO e na da CAPACIDADE; mutacoes-f1 28 de 28 — 5 mundos, 15
  quebras e 8 mortes.
  O NUMERO QUE JUSTIFICA VARRER A ENTRADA INTEIRA: existe EXATAMENTE UM estado neste
  banco em que arredondar meio-para-cima difere de meio-para-par (gondola noturna, 2
  pessoas, 56,925 EUR por pessoa com IOF). Uma grade por amostragem teria 1 chance em 154
  de o achar, e a mutacao do arredondamento voltaria verde.
  PROXIMO PASSO: a F2 como REGRA (quanto custa N dias em <cidade>), que nasce com a
  mesma pergunta aberta do eixo — a F2 soma hospedagem, alimentacao e transporte local, e
  nenhuma das tres esta no banco. O que ela pode fazer hoje e o que a F1 fez.
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

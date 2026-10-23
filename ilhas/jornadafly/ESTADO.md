---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-22T20:01Z
executando_desde: 2026-10-23T10:31Z   # reserva RENOVADA pela 1.1 (a primeira foi as 10:17Z): o bloco 5 montou quatro artigos do banco, e a bateria de mutacoes do artigo roda o portao 41 vezes, sobre as quatro paginas e sobre o conjunto. Renovar e uma linha, e e o que faz a proxima execucao nao precisar do git para saber.
rede: BLOQUEADA em 2026-10-22   # 20.2, REMEDIDA as 19h1xZ e NAO herdada do campo: TRES passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas tres (6 medicoes), com aquametria.com.br e robometria.com.br em 200 nas tres (6 de controle, nenhuma intermitencia). O curl verbose nomeia a causa e ela nao e tunel: `CONNECT tunnel failed, response 403` do proxy de egresso. SEGUE SENDO REGRESSAO (o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia), e o despacho ALTA de 15/09 em dados/despachos.md continua valendo. E PELA 20.3, CINCO FONTES DE PASSE entraram no bloqueio, medidas hoje ANTES de escrever a regra que as exige: romapass.it, www.romapass.it, www.turismoroma.it, www.lisboacard.org e www.visitlisboa.com em 000, com www.civitatis.com.br (ja listado) tambem em 000 e raw.githubusercontent.com em 301 ao lado. Somadas as tres fontes de diaria de 16h2xZ (numbeo, booking, civitatis), o que a rede trava e a COLETA da F2 e da F3, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas sete execucoes anteriores.
bloco_atual: |
  A F3 EXISTE COMO REGRA, e com ela as TRES ancoras desta ilha existem. Escreve-la
  mostrou que a conta nao era a parte dificil: o 1o colocado da consulta ja publica
  «soma dos avulsos x preco do passe com ponto de equilibrio» e promete «fiz as contas
  pra voce» no titulo. O que ninguem publica e DE QUANTAS atracoes aquele numero saiu.
  A previsao do registro anterior estava MEIO CERTA: a F3 nao e atravessada pela
  procedencia de terceiro (avulso e passe sao os dois nossos), e o que a atravessa nao
  e «declarar o que o numero e» — e SOBRE O QUE a conta e feita.
  NADA FOI AO AR, e nao podia: esta ilha nao tem site, nao tem WordPress, nao tem Sync
  e nao tem /status. Dizer que verifiquei no ar seria inventar.
  REDE REMEDIDA E NAO HERDADA (20.2): 6 medicoes de bloqueio contra 6 de controle
  verde, com `CONNECT tunnel failed, response 403` nomeado no verbose. Segue regressao.
  E PELA 20.3, as CINCO fontes de passe que a F3 precisaria estao recusadas, medidas
  ANTES de escrever a regra que as exige: romapass.it, turismoroma.it, lisboacard.org,
  visitlisboa.com e civitatis.com.br em 000, com raw.githubusercontent.com em 301.
  O QUE SAIU: ferramentas/f3-referencia.py (o cerebro), ferramentas/gerar-f3.py,
  dados/f3-respostas.json (1.038 estados contados, 78 gravados, 48 linhas de tabela,
  publicar false), ferramentas/teste-f3.py e ferramentas/mutacoes-f3.py. Esquema
  versao 7, banco 7, com a entidade COBERTURA_DO_PASSE e o vocabulario
  forma_de_cobertura. A lista de portoes do PROMPT.md foi de SEIS para OITO e os dois
  novos foram escritos la na mesma passada — primeira vez que aquele aviso foi cobrado.
  A ENTIDADE NAO E CAMPO DE NENHUM DOS DOIS LADOS: o passe E uma experiencia
  (`passe_de_cidade`, no vocabulario desde 14/09 e sem um registro que o use), e o que
  nao tinha onde morar e a RELACAO entre o passe e cada atracao. Ela tem fonte e data
  PROPRIAS porque e ela que envelhece — o preco do passe pode estar certo e a cobertura
  errada no mesmo dia, e o bloco 1 mediu isso em 14/09 na fonte de topo do Roma Pass.
  AS TRES REGRAS, no esquema e cobradas por codigo: (1) NAO LIDA NAO E NAO COBERTA —
  atracao sem cobertura fica fora do valor E e nomeada; (2) o equilibrio e sobre o que
  a ilha LEU, com `atracoes_declaradas_pelo_passe` e a contagem das lidas na tela lado
  a lado; (3) «ate 50%» nao e 50% — `desconto_e_no_maximo` faz o valor ir de ZERO ao
  teto, e a regua do banco le a HEDGE da frase da fonte e reprova a hedge virada numero
  cheio.
  O VEREDITO TEM TRES DESFECHOS: paga (se paga ate na ponta de baixo), nao_paga (nem na
  de cima) e DEPENDE_DA_VERSAO, quando a faixa ATRAVESSA o preco do passe — ali existe
  bilhete em que ele paga e bilhete em que nao, e as duas sao verdade. E o equilibrio
  sai das mais caras para as mais baratas, com a ordem DECLARADA e as atracoes
  NOMEADAS, nas duas pontas da faixa.
  O DEFEITO QUE O PASSE CRIOU NA F2, e ele pagava a mesma visita DUAS VEZES: com um
  passe no banco, a linha de experiencias de Roma publicava «EUR 100 a 148» para 2
  pessoas — o ingresso (36 a 44) mais o passe que inclui o ingresso (64 a 104). A F2
  passou a descartar `passe_de_cidade` e a NOMEAR a recusa, mandando quem pergunta para
  a F3. A metade mais traicoeira era a segunda: a FONTE do passe continuava no «como
  sabemos», prestando contas de um numero que a pagina nao publica. Os arquivos gerados
  nao mudaram UM BYTE — a correcao e no-op no banco de hoje, e o defeito estava
  esperando a primeira carga.
  TRES DEFEITOS MEUS, antes do commit: (a) as recusas duras ECOAVAM id de registro na
  tela (bastidor da 32.4), e a causa de ninguem ver era ESTRUTURAL — a varredura do
  portao dava `continue` na borda e as frases de borda nunca passavam pela regua de
  acento, frase proibida e bastidor; agora passam. (b) O PORTAO MORRIA EM VEZ DE
  RELATAR, em CINCO pontos: a bateria mediu cinco quebras classificadas `morre` em vez
  de `reprova`, porque o portao PEGAVA o defeito e depois estourava IndexError na lista
  que a afirmacao acabara de dizer vazia. Regra: afirmar primeiro, e so entao ler o que
  a afirmacao garantiu. (c) A CONCORDANCIA, terceira vez nesta pasta: «1 atracao em
  Veneza CUSTAM» e «dentro DAS 1 atracao».
  E DOIS QUE JA ESTAVAM NA PASTA: o EIXO NULL nao conferia `dias_de_uso` (as duas
  direcoes cobravam `por_quantidade` e proibiam os outros eixos, e o null — a
  experiencia de UMA versao, que e o que um passe de validade unica e — nao caia em
  nenhuma); e o RELATORIO do validador escondia o que ele contava, porque a lista de
  chaves do main() era literal e `faixas_diarias` nao estava nela. Mais um que ia
  estourar na PRIMEIRA cobertura gravada: a secao nova do validador usava um indice de
  experiencias que nao existia.
  A REGUA DO VENCIMENTO saiu do validador e virou `f1.dias_de_validade` e
  `f1.preco_vencido`, com `hoje` sempre RECEBIDO. A F3 e a primeira ferramenta que leva
  o vencimento para a TELA, e o portao dela COMPARA os dois vereditos versao por versao
  do banco: discordarem quer dizer que uma das duas esta errada e nenhuma sabe.
  O QUE A F3 PUBLICA HOJE E METADE DA PERGUNTA: nos 1.008 estados validos ela publica a
  soma dos avulsos e fecha com `sem_passe_lido`. A recusa NUNCA diz que a cidade nao TEM
  passe — o vocabulario nasceu sem lastro e a regra de crescimento de vocabulario proibe
  frase de inexistencia; o portao cobra essa distincao em CADA estado, e e a primeira vez
  nesta ilha que aquela regra do esquema e conferida por codigo. O ANGKOR PASS NAO FOI
  RECATEGORIZADO: ele cobre UM sitio e nao uma cidade, e trocar a categoria dele para dar
  lastro ao vocabulario seria mover o dado para caber na ferramenta.
  BANCADA, 0 falha: validar-banco verde; mutacoes-banco 154 de 154 (37 novas);
  teste-f1 139.658 afirmacoes; mutacoes-f1 28 de 28; teste-f2 216.614; mutacoes-f2
  51 de 51; teste-f3 616.462 afirmacoes sobre os 1.038 estados; mutacoes-f3 45 de 45 —
  13 mundos, 25 quebras e 7 mortes, com 25 cobradas pela frase.
  PROXIMO PASSO: NAO HA MAIS FERRAMENTA A ESCREVER, e isso e informacao e nao fim de
  linha. Sobram dois itens de arquivo pequenos — bloco 5 (artigos-ancora pareados com
  cada ferramenta) e bloco 6 (lista de prospeccao do widget, publicar false). O 5b
  (malha) e o 5c (free tour) dependem da casca. Depois deles esta ilha nao tem bloco que
  nao precise do Raphael: a casca (3b), os passos 2 a 8 da secao 11, a liberacao do
  dominio no egresso e as fontes de diaria e de passe — todas de navegador, todas dele.
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

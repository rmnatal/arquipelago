---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-23T10:40Z
executando_desde: 2026-10-23T13:44Z   # reserva RENOVADA pela 1.1 (reservada as 13:20Z): o bloco 6 passou de 40 minutos porque a bancada desta ilha sem rede roda doze portoes e as cinco baterias de mutacao sozinhas passam disso. A hora sai do `date -u` na mesma linha de comando que a grava, nunca digitada.
rede: BLOQUEADA em 2026-10-23   # 20.2, REMEDIDA as 10h16Z e NAO herdada do campo: DUAS passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas duas (4 medicoes), com aquametria.com.br e robometria.com.br em 200 nas duas (4 de controle, nenhuma intermitencia) e raw.githubusercontent.com em 301 ao lado. SEGUE SENDO REGRESSAO (o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia), e o despacho ALTA de 15/09 em dados/despachos.md continua valendo. As fontes de diaria (numbeo, booking, civitatis) e as CINCO de passe (romapass.it, turismoroma.it, lisboacard.org, visitlisboa.com, civitatis.com.br) seguem recusadas pela 20.3, medidas em 22/10: o que a rede trava e a COLETA da F2 e da F3, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas oito execucoes anteriores.
bloco_atual: |
  O BLOCO 5 SAIU: os ARTIGOS-ANCORA existem como REGRA, e a decisao que mais
  importa neles e de FORMA. O caminho obvio era escrever quatro textos em
  Markdown, e ele teria destruido o produto desta ilha em silencio: artigo
  escrito a mao carrega numero digitado, e numero digitado envelhece calado — no
  dia da proxima carga do banco a calculadora publica o preco novo e o artigo
  continua publicando o velho, com a mesma cara de verdade. O VOZ.md chama preco
  cravado sem a data da coleta de «o defeito mais grave possivel nesta ilha».
  NADA FOI AO AR, e nao podia: esta ilha nao tem site, nao tem WordPress, nao tem
  Sync e nao tem /status. Dizer que verifiquei no ar seria inventar.
  REDE REMEDIDA E NAO HERDADA (20.2): 4 medicoes de bloqueio contra 4 de controle
  verde as 10h16Z. Segue regressao.
  O QUE SAIU: ferramentas/artigos-referencia.py (o cerebro: o mapa das consultas,
  a arvore, a rotacao das irmas, a montagem e o portao que confere),
  ferramentas/gerar-artigos.py, dados/artigos-ancora.json (4 artigos escritos, 44
  linhas de tabela, 74 paragrafos de dobra, 14 perguntas de FAQ, publicar false),
  ferramentas/mutacoes-artigos.py, e a secao 7 da especificacao. O banco e o
  esquema NAO foram tocados: o bloco 5 le, nao escreve.
  TODA FRASE DE PRECO SAI DA f1-referencia.py, a mesma regra que a bancada mede. O
  que a referencia do artigo guarda e o que NENHUMA ferramenta sabe: qual consulta
  ele ataca, quem ocupava a SERP dela no dia da medicao, qual e a mae na arvore,
  quais sao as irmas e para onde vai o link de compra.
  A MAE NAO E A CIDADE, e esse foi o erro barato que quase saiu: cada uma das
  quatro cidades do banco tem UMA experiencia, e quatro categorias com uma filha
  cada e cluster ralo que nao passa autoridade. Os quatro nasceram em
  /guias/quanto-custa/ — que e um dos tres itens do menu do VOZ.md — e assim cada
  pagina recebe TRES irmas apontando para ela. A janela de irmas ROTACIONA, e a
  afirmacao que mede isso e do CONJUNTO, na direcao de quem aponta.
  DOIS CAMPOS PARA A MESMA PERGUNTA: consulta_alvo e a consulta como a pessoa
  digita (e gente digita sem acento) e nunca vai para a tela; titulo_na_tela e a
  mesma pergunta em portugues correto. O portao cobra que o titulo nao perca
  palavra da consulta e so ganhe palavra de ligacao.
  E A FRONTEIRA COM A CALCULADORA FICOU ESCRITA: a consulta parametrica («para N
  pessoas») e da FERRAMENTA, a crua e do GUIA. O portao reprova titulo de guia que
  traga a parametrica, e reprova duas paginas na mesma consulta-alvo.
  QUATRO DEFEITOS, e o primeiro foi contra mim: (a) a regra «todo valor da tela
  esta no conjunto que o banco autoriza» REPROVAVA a prestacao de contas da
  gondola, que e o diferencial da ilha — os EUR 80 da Eurodicas e os EUR 34 da
  GetYourGuide sao os numeros com que ela DISCORDA; agora o valor de terceiro
  passa so dentro da frase que nomeia o publicador e traz a data. (b) Registro
  pendente_de_releitura publica na tela com a ressalva e NAO na description, que e
  lida sozinha no resultado de busca. (c) A REGUA DE ACENTUACAO FOI TENTADA TRES
  VEZES E NAO EXISTE: as tres reprovaram texto impecavel, e portao que reprova
  texto certo e pior que portao nenhum porque ensina a ignorar o vermelho — as
  tres estao escritas na afirmacao (8) do arquivo, com o que cada uma reprovou.
  (d) O FAQ RESPONDIA A OUTRA PERGUNTA em tres dos quatro artigos, e ia para o
  FAQPage do JSON-LD; cada pergunta passou a declarar DE ONDE sai a resposta dela,
  e o portao reprova duas perguntas respondidas pela mesma frase.
  DOIS ARTIGOS NAO FORAM ESCRITOS, e a causa e DADO e nao tempo: a F2 e a F3 nao
  tem resposta para publicar (zero faixas de diaria, zero passes, zero coberturas,
  e Roma com uma atracao so). Artigo cujo titulo promete um numero que a pagina nao
  entrega e EXATAMENTE o defeito que o bloco 1 mediu nos oito ocupantes. Os dois
  ficam PRE-REGISTRADOS no arquivo, com o criterio de destravamento escrito ANTES
  de o dado chegar.
  A LISTA DE PORTOES FOI DE OITO PARA DEZ, e a 31.3 foi lida ANTES: ela proibe
  testar portao que JA EXISTE, e o portao conferido pela bateria nasceu na mesma
  passada que o conteudo que ele guarda — o desenho que a F1, a F2 e a F3 tiveram
  em 22/10. Dez linhas ainda cabem numa tela e a margem agora e de duas ou tres.
  BANCADA, 0 falha: validar-banco verde; mutacoes-banco 154 de 154; teste-f1
  139.658 afirmacoes; mutacoes-f1 28 de 28; teste-f2 216.614; mutacoes-f2 51 de 51;
  teste-f3 616.462; mutacoes-f3 45 de 45; artigos-referencia 4 artigos conferidos;
  mutacoes-artigos 43 de 43 — 39 por artigo e 4 pelo conjunto, zero morte e zero
  inerte.
  PROXIMO PASSO: o BLOCO 6 — lista de prospeccao do widget (operadores e receptivos
  brasileiros com site proprio, publicar false). E o ULTIMO item de arquivo desta
  ilha. Depois dele nao sobra bloco que nao precise do Raphael: a casca (3b), os
  passos 2 a 8 da secao 11, a liberacao do dominio no egresso e as fontes de diaria
  e de passe — todas de navegador, todas dele. O 5b (malha) e o 5c (free tour)
  dependem da casca; os dois artigos pre-registrados dependem de coleta.
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

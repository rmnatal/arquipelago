---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-23T13:20Z
executando_desde: 2026-10-27T10:17Z   # reserva da execucao da Fundacao de 2026-10-27T10:17Z (ilha em FOCO pela 1.2; os despachos do molde da 32 estao os tres fechados, entao nada fura o foco)
rede: BLOQUEADA em 2026-10-23   # 20.2, REMEDIDA as 13h20Z e NAO herdada do campo: DUAS passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas duas (4 medicoes), com aquametria.com.br e robometria.com.br em 200 nas duas (4 de controle, nenhuma intermitencia) e raw.githubusercontent.com em 301 ao lado. SEGUE SENDO REGRESSAO (o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia), e o despacho ALTA de 15/09 em dados/despachos.md continua valendo. E A 20.3 FOI EXERCIDA NO BLOCO 6, as 13h28:28Z: os CANDIDATOS da lista de prospeccao tambem estao fora do egresso — bondinho.com.br, www.toureiffel.paris, viagemitalia.com, www.panrotas.com.br e www.civitatis.com em 000, com aquametria.com.br em 200 na mesma passada. As fontes de diaria (numbeo, booking, civitatis) e as CINCO de passe (romapass.it, turismoroma.it, lisboacard.org, visitlisboa.com, civitatis.com.br) seguem recusadas pela 20.3, medidas em 22/10: o que a rede trava e a COLETA e agora tambem a VERIFICACAO DE CANDIDATO, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas nove execucoes anteriores.
bloco_atual: |
  O BLOCO 6 SAIU — a LISTA DE PROSPECCAO DO WIDGET existe, com 25 candidatos e
  publicar false. E o ULTIMO item de arquivo da fila desta ilha: 1, 2, 3, 4 (F1,
  F2, F3), 5 (quatro artigos) e 6 estao cumpridos ate onde a Fundacao alcanca.
  NADA FOI AO AR, e nao podia: esta ilha nao tem site, nao tem WordPress, nao tem
  Sync e nao tem /status. Dizer que verifiquei no ar seria inventar.
  O ACHADO, e ele nao precisou de busca nova: A LISTA JA ESTAVA MEDIDA DESDE
  14/09. O corpus do bloco 1 mediu 69 dominios e rotulou operador,
  concessionaria e plataforma entre eles — como PROCEDENCIA, isto e, como
  concorrencia. bondinho.com.br entrou nesta lista porque o corpus ja o escrevia
  como «operador, e tres URLs dele». Duas metades contando a mesma coisa sem
  nunca se falarem, e agora o portao as faz conversar por regra.
  O QUE SAIU: dados/prospeccao-widget.json (o banco), dados/prospeccao-widget.md
  GERADO, ferramentas/prospeccao-referencia.py (a regua), gerar-prospeccao.py,
  validar-prospeccao.py (--autoteste, 15 casos), teste-prospeccao.py (285
  afirmacoes) e mutacoes-prospeccao.py (39 casos), mais a secao 8 da
  especificacao. A bancada da ilha foi de dez para treze portoes.
  A PRIORIDADE NAO E CAMPO DO BANCO: e DERIVADA, e o portao reprova se alguem a
  gravar. O barramento vem primeiro e sai de decisao que a ilha ja tinha tomado:
  dos seis clusters do bloco 1 a ilha declarou que NAO disputa um, o A2 —
  «disputar 'quanto custa o ingresso X' contra o operador e perder, e nao e
  preciso». Quem ocupa consulta de cluster disputado nao hospeda a ferramenta
  que a disputa. 7 dos 25 estao BARRADOS, e o caso que prova a regra e o
  northbound.is: operador com site proprio que ocupa a consulta que o proprio
  bloco 1 chama de «o melhor encaixe entre recorte e monetizacao».
  A DECISAO DO BLOCO: NESTA ILHA A FERRAMENTA PODE MINAR QUEM A HOSPEDA. Nas
  outras tres o widget ajuda o anfitriao a vender; aqui ela responde «vale a
  pena?». Entao a F1 so vai a quem vende A MESMA versao que o banco preca — o
  viagemitalia.com vende o tour do Coliseu a EUR 75 por pessoa COM o ingresso
  dentro, e o banco preca o avulso. A F2 exige FAIXA_DIARIA e a F3 exige passe e
  cobertura, CONTADOS DO BANCO em toda passada; a F3 nunca vai a vendedor de
  passe.
  NENHUM DOS 25 TEM FERRAMENTA OFERTAVEL HOJE, e a causa e UMA: a rede fechada
  decidiu a composicao do banco (quatro experiencias de tarifa publica, TRES dos
  quatro operadores sao PODER PUBLICO), e poder publico nao instala widget de
  afiliado. E a QUARTA consequencia do mesmo bloqueio, e a primeira vez que ela
  chega na secao 14.7 — a UNICA alavanca de link do projeto, parada nesta ilha.
  O QUE DESTRAVA ESTA NOMEADO E MEDIDO: uma experiencia de operador privado
  brasileiro no banco. O Parque Bondinho Pao de Acucar vende direto, pelo
  proprio site, mais de uma versao da mesma experiencia.
  AS TRES COISAS QUE OS PORTOES ACHARAM, as tres no meu proprio trabalho: (1) 68
  fatos afirmados sem evidencia que os nomeasse — o conserto foi AFIRMAR MENOS,
  oito campos viraram null, entre eles o tipo do ingressomachupicchu.com, que o
  NOME DO DOMINIO parecia provar; (2) a regua de acento reprovou texto legitimo
  (dados/experiencias.json, prospeccao-referencia.py) e a saida foi ESTRUTURA,
  nao heuristica: ela retira o que esta entre craseadas antes de olhar; (3) A
  CONTA QUE EU IA PUBLICAR ESTAVA ERRADA — o texto dizia 64 dominios no corpus e
  sao 69, porque a contagem de cabeca deixou .is, .fr, .pt, .paris, .kh e .cz de
  fora. O conserto nao foi trocar o numero: a bancada passou a LER a prosa do
  achado e conferi-la contra o banco e o corpus em toda passada.
  UMA REGRA DESTE BANCO NAO TEM NENHUM CASO HOJE, dito como e: a F3 nunca ir a
  vendedor de passe nao se aplica a ninguem, porque a venda de passe nao foi
  medida em nenhum candidato. Quem prova que ela morde e a bateria de mutacoes.
  ACHADO DE METODO: as TRES buscas dirigidas a «receptivo brasileiro com site
  proprio» devolveram portal de conteudo e plataforma — a concorrencia, nao os
  candidatos. Os unicos receptivos que apareceram POR NOME vieram da imprensa de
  trade. Operador e receptivo nao disputam a SERP de «quanto custa», logo nao
  sao achados por ela: quem continuar esta lista busca em trade.
  BANCADA, 0 falha: validar-prospeccao aprovado com o .md identico ao que a
  referencia gera, --autoteste 15 de 15, teste-prospeccao 285 afirmacoes,
  mutacoes-prospeccao 39 de 39 (4 mundos que tem de passar, inclusive o banco de
  experiencias CARREGADO, 21 quebras, 10 sobre a regua da oferta e 4 mortes).
  PROXIMO PASSO: NAO SOBROU BLOCO DE ARQUIVO NESTA ILHA. O que falta e todo do
  Raphael e todo de navegador — os passos 2 a 8 da secao 11, a liberacao de
  jornadafly.com.br no egresso, e a coleta das fontes de diaria e de passe. O 3b
  (casca), o 5b (malha) e o 5c (free tour) dependem da casca; os dois artigos
  pre-registrados e os dois destravamentos de ferramenta dependem de coleta. A
  execucao seguinte que encontrar esta ilha em foco e sem nenhuma dessas duas
  coisas NAO TEM BLOCO PARA ABRIR, e isso esta escrito para que ela nao invente
  um.
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

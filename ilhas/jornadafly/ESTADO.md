---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-27T13:56Z   # BLOCO ENTREGUE: `ARVORE.md`, o item (i) do 16.8 — esta ilha era a unica do arquipelago sem ele. A HORA SAIU DO datetime.now(utc) NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-10-27T16:30Z   # reserva RENOVADA pela 1.1 (a primeira foi as 16h25Z): o bloco passa de 40 minutos — coleta por busca em tres passadas e carga de registro novo no banco. A hora saiu do `date -u` na MESMA linha de comando que a grava.
rede: BLOQUEADA em 2026-10-27   # 20.2, REMEDIDA as 13h4xZ e NAO herdada do campo: OITAVO dia de recusa. jornadafly.com.br e www.jornadafly.com.br em 000, com aquametria.com.br, robometria.com.br e clubedomosaico.com.br em 200 na MESMA linha de comando — zero intermitencia no controle. SEGUE SENDO REGRESSAO (o campo dizia `aberta em 2026-09-18`, com HTTP 200 medido naquele dia). bloqueada_por SEGUE null de proposito: a secao 2 reserva o campo para dependencia humana que trava a ILHA, e o que falta aqui trava a FABRICA — isso se escreve no despacho, que e o canal da 12.2. NOVO HOJE: o egresso passou a travar tambem o 5c, porque `civitatis.com.br` esta entre os nove recusados e o cluster free tour espera COLETA, nao casca.
bloco_atual: |
  BLOCO ENTREGUE: `ARVORE.md` — o item (i) do 16.8 do ARQUIPELAGO.md. Esta ilha era a
  UNICA do arquipelago sem este arquivo: a aquametria, a robometria e a clubedomosaico
  tem o seu desde 11/09/2026, e era justamente a ilha EM FOCO, cuja malha (5b) e o bloco
  aberto, que estava sem o mapa que a malha segue.
  E HAVIA BLOCO — tres execucoes seguidas fecharam em "nada elegivel" apoiadas numa frase
  do registro de 23/10 que esta MEDIDA E FALSA em duas das tres pendencias: "o 3b (casca),
  o 5b (malha) e o 5c (free tour) dependem da casca". Para o 3b esta certo. O 5b e o 5c
  dependem de DADO, e ninguem havia aberto o banco para conferir. Eu abri.
  A CONTRADICAO QUE ISSO ESCONDIA: o 5b do PROMPT.md manda agrupar experiencia -> cidade
  -> pais, e a especificacao 7.2, escrita quatro dias depois, diz com todas as letras que
  "agrupar por cidade teria sido o erro barato: cada cidade do banco tem UMA experiencia".
  Os dois textos conviviam mandando coisas opostas, e o custo tinha endereco: a execucao
  que encontrasse a casca pronta publicaria o cluster ralo que a ilha ja havia recusado.
  MEDIDO em dados/experiencias.json: 4 experiencias, 4 cidades, 1 experiencia POR cidade
  nas quatro, 3 paises (Italia 2, Camboja 1, Franca 1), faixas_diarias 0, coberturas 0.
  Contra a 16.5 (3 filhas) e a 14.4 (3 itens), nenhuma pagina de cidade e nenhuma de pais
  nasce hoje. E as camadas (1) e (4) do 5b JA ESTAVAM ENTREGUES pelo bloco 5, sem o 5b
  saber: os quatro artigos sao um por experiencia, e ficha para as mesmas quatro seria a
  segunda pagina na mesma consulta_alvo, que a 7.4 proibe. A camada (3), pais, nao tem
  nivel onde morar — a experiencia gasta os tres da 16.1, que nao admite quarto.
  CRITERIO PRE-REGISTRADO (1.2-b.4), escrito ANTES do dado: /experiencias/<cidade>/ nasce
  com 3 experiencias naquela cidade; /experiencias/ nasce com a primeira que passar; a
  ficha so nasce para experiencia SEM artigo proprio; o pais nao nasce; e o free tour
  nasce com 3 free tours de dado real, com operador nomeado.
  O 5c E COLETA, NAO CASCA: `free_tour` esta no vocabulario do esquema (linha 135) com
  ZERO registros que o usem — a assinatura de `passe_de_cidade` —, e o validar-banco.py
  avisa os dois como vocabulario_sem_lastro. Falta `civitatis.com.br`, no egresso.
  TRES ACHADOS DE CASCA, de graca, os tres escritos ANTES de a casca existir: (1) a home
  e a F1 servem o mesmo formulario, que a 14.4 proibe — a home serve o formulario VAZIO e
  nunca le parametro, e a resposta com parametro mora so na calculadora, com canonical;
  (2) o rotulo do menu colide com o nome de uma categoria e a CALCULADORA, que e a pagina
  do dinheiro, fica fora do menu — conserto no rotulo, nunca no slug, que esta entregue e
  com portao; (3) os slugs da F2 e da F3 nao existiam em arquivo nenhum e nasceram aqui
  como PROPOSTA, para quem escrever a casca conferir.
  A REGRA DE OURO, copiada da robometria: documento e codigo mantidos a mao em dois
  lugares divergem em silencio. A arvore JA EXISTIA em codigo (artigos-referencia.py,
  linhas 41 e 42) e este documento nao a inventou — ele a leu. Onde discordarem, o codigo
  e o que esta entregue.
  NADA FOI AO AR, E NAO PODIA: sem WordPress nao ha casca, Sync, /status nem URL. E
  NENHUM PORTAO NASCEU — a 31.2 so deixa nascer portao com defeito medido no ar, e o que
  esta passada achou e contradicao de documento. O portao desta arvore nasce com a casca,
  LENDO este arquivo, como o teste-arvore.php da robometria.
  BANCADA 0 FALHA depois das mudancas: validar-banco, teste-f1, teste-f2, teste-f3,
  teste-prospeccao (285 afirmacoes), gerar-artigos e validar-prospeccao. Mudei DOIS
  arquivos .md e nenhuma linha de codigo e nenhum JSON.
  A 31.1 VAI DE 4 EM 13 PARA 4 EM 14, e esta dito sem maquiagem: ela se mede por entrega
  no ar, e esta ilha nao pode ter uma ate os passos 2 a 8. O que mudou nao e o numero — e
  que o proximo destravamento deixou de carregar um erro.
  PROXIMO PASSO: nao e da Fundacao, e o que o GESTO (2) do Raphael compra MUDOU. (1) O
  egresso destrava coleta, e agora tambem o 5c. (2) Os passos 2 a 8 destravam o ar, o 3b,
  o tradutor PHP e A PRIMEIRA LEVA DE MALHA — 8 URLs, ja desenhada e autorizada pelo dado
  de hoje na secao 6 do ARVORE.md. O que o gesto (2) NAO compra mais: o 5b e o 5c. (3)
  Uma linha no foco.md destrava a rotacao e os quatro despachos NORMAIS parados.
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

---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-10-22T10:33Z
executando_desde: 2026-10-22T13:29Z   # reservada pela execucao de 22/10 que comecou as 13:29Z (passo 5 da secao 1). A ilha estava com executando_desde null, que pela 1.1 ja significa que nao havia bloco da Fundacao vivo.
rede: BLOQUEADA em 2026-10-22   # 20.2, TRES passadas remedidas hoje e NAO herdadas: jornadafly.com.br e www.jornadafly.com.br em 000 nas tres, com aquametria.com.br e robometria.com.br em 200 nas mesmas passadas (a robometria caiu uma vez na 3a — intermitencia de tunel, que e justamente o que a 20.2 manda nao confundir com bloqueio). O curl verbose nomeia a causa e ela nao e intermitencia: `CONNECT tunnel failed, response 403` do proxy de egresso, ou seja o dominio NAO esta na lista de Dominios permitidos deste ambiente. ISTO E REGRESSAO: o campo dizia `aberta em 2026-09-18` com HTTP 200 medido as 12h35Z daquele dia. O despacho ALTA de 15/09 em dados/despachos.md, dado como cumprido em 18/09, voltou a valer. O que a rede trava e o 3b em diante, nao o bloco de arquivo — e bloqueada_por segue null de proposito, como nas quatro execucoes anteriores desta ilha.
bloco_atual: |
  FAIXA ETARIA DESCEU DE EXPERIENCIA PARA VERSAO, nas 11 versoes das 4 experiencias,
  e com isso o PROXIMO PASSO que o REGISTRO.md de 15/09/2026 deixou escrito esta
  CUMPRIDO ao pe da letra — "com a regua e as mutacoes junto, e migrar os registros da
  gondola e do Angkor na mesma passada". Esquema versao 4, banco versao 4.
  NADA FOI AO AR, e nao podia ter ido: esta ilha nao tem site, nao tem WordPress, nao
  tem Sync e nao tem /status. Dizer que verificou no ar seria inventar.
  O QUE A DESCIDA PRODUZIU, e nenhuma das tres coisas era possivel com o campo na
  EXPERIENCIA:
  (1) A TORRE EIFFEL PUBLICA 4 FAIXAS GRAVADAS em vez de 1. A carga de 15/09 so podia
  gravar a gratuidade dos menores de 4 anos, porque as outras tres mudam de bilhete
  para bilhete; os numeros ficaram em PROSA dentro da nota do registro. Agora sao
  campo: 3,80 e 7,40 EUR na escada ate o segundo piso, 9,20 e 18,40 no elevador ate o
  topo, cada um com `transcrito_de` dizendo que saiu daquela prosa e NAO de leitura
  nova. Mesma troca que a Aquametria fez em 21/10 com o porte_adulto_cm.
  (2) A PROIBICAO DE FAIXA EM TARIFA POR VEICULO VIROU REGRA. Era prosa no motivo da
  gondola desde 14/09 — "a tarifa e pela embarcacao inteira" — e so podia virar regra
  depois de a faixa descer, porque `unidade_de_preco` e campo da VERSAO. Seis pessoas
  na gondola sao DUAS gondolas: a crianca nao tem preco, tem assento.
  (3) O ACHADO QUE A MIGRACAO PAGOU: o `se_nao_cumprir` do Angkor cita US$ 37, que e o
  passe de UM DIA, e estava guardado num campo que valia para os TRES passes. Nomeado
  em `numero_da_frase_e_de_outra_versao` nas versoes de 3 e de 7 dias, e a regua cobra
  o campo em vez de confiar na nota. A ilha NAO troca 37 por 62 nem por 72: ela sabe o
  que a fonte escreveu, nao o que a bilheteria cobra.
  AS 4 CELULAS DO MEIO DA GRADE CONTINUAM NAO LIDAS — crianca e jovem nas duas versoes
  intermediarias da Torre Eiffel — e agora estao CONTADAS, 4 entradas em
  `faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu`, com o resumo publicando
  `faixas_declaradas_nao_transcritas: 4`. Tentei rele-las: `www.toureiffel.paris`
  responde 403 no CONNECT deste ambiente e a busca devolveu a grade por RESUMO —
  numero de resumo e pista, nao dado, entao a lacuna fica contada em vez de gravada.
  BANCADA, 0 falha: validar-banco verde sobre o banco real (11 faixas contadas, 4
  lacunas contadas) e MUTACOES 73 (eram 53) — 7 mundos que tem de PASSAR e 66 quebras
  que tem de REPROVAR, 22 delas cobradas pela FRASE que esperam ouvir de volta (eram
  3). Os tres JSON passam por json.load e o cabecalho por yaml.safe_load.
  E AS MUTACOES ME CORRIGIRAM DUAS VEZES, as duas antes do commit. A primeira versao da
  regra proibia faixa etaria em TODA unidade que nao fosse `por_pessoa`, e o MUNDO
  `por_cabine` a reprovou na hora: o argumento da gondola e sobre VEICULO alugado
  inteiro, e um cruzeiro vendido por cabine PODE declarar tarifa de crianca na cabine.
  A proibicao ficou no caso medido e `por_cabine` e `por_grupo` ficaram de fora dela, de
  proposito. A segunda: o mundo novo escreveu "crianca de 4 a 11 anos" sem cedilha e a
  regua das irmas reprovou TRES versoes de uma vez, porque e o rotulo que liga a mesma
  faixa entre bilhetes. Regua que diz nao para um mundo legitimo custa mais caro que
  regua que falta — e foi a bateria que achou o excesso, nao uma releitura minha.
  A ESCOLHA DA ILHA: NAO HOUVE ROTACAO. Hoje e 22/10/2026 e a linha
  `fila_decidida_pelo_raphael` do foco.md mandava, desde 09/10 e ajustada por ele em
  14/10, que a jornadafly entrasse em foco HOJE como foco principal — e avisava com
  todas as letras que a linha `ilha:` nao se troca sozinha e que "se ninguem editar, o
  foco fica preso, como ficou de 10/10 a 14/10". A janela da aquametria vencia em 21/10.
  Troquei a linha e reservei esta ilha no MESMO push, as 10h20Z, aceito de primeira.
  Os tres despachos do MOLDE da secao 32 estao FECHADOS nas tres ilhas (aquametria as
  18h2xZ, clubedomosaico as 19h1xZ e robometria, as nove paginas), entao a excecao que
  furava o foco pela 32 nao se aplica mais — o foco volta a mandar sozinho.
  REDE PELA 20.2, REMEDIDA E NAO HERDADA, E E REGRESSAO: tres passadas, jornadafly e
  www.jornadafly em 000 nas tres, com aquametria e robometria em 200 nas mesmas (a
  robometria caiu uma vez na terceira, que e a intermitencia de tunel que a 20.2 manda
  nao confundir com bloqueio). O curl verbose nomeia a causa: `CONNECT tunnel failed,
  response 403` do proxy de egresso, dominio fora da lista de Dominios permitidos. O
  campo dizia `aberta em 2026-09-18`, com HTTP 200 medido as 12h35Z daquele dia — entao
  isto JA ESTEVE RESOLVIDO e voltou, e o despacho ALTA de 15/09 volta a valer.
  A 31.1 E INALCANCAVEL NESTA ILHA, e esta escrito no PROMPT.md dela para nao ser lido
  como desobediencia: 7 de cada 10 execucoes entregam algo no ar, e aqui nao existe "no
  ar". Falta WordPress (passos 2 a 8 da secao 11, navegador do Raphael) e falta o
  dominio na lista de rede. As duas sao dele.
  PROXIMO PASSO: a F1 como REGRA (bloco 4), no desenho da F1 da ohmetria — referencia em
  Python, entrada -> resposta inteira em frase acentuada, tabela pre-renderizada e
  portoes, SEM PHP enquanto nao houver casca. A especificacao desta ilha ja foi
  atualizada hoje para o modelo novo: a F1 le a faixa da VERSAO que a pessoa escolheu,
  nunca da experiencia, e distingue TRES recusas que antes eram uma — faixa que o
  operador nao declara, faixa que ele declara e ninguem leu, e numero da frase que e de
  outro bilhete.
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

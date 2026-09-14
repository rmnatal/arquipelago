---
ilha: jornadafly
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: 2026-09-14T19:31Z
executando_desde: null
rede: bloqueada em 2026-09-14   # 20.1: o dominio nao esta na lista de Dominios permitidos. Despacho ALTO para o Raphael em dados/despachos.md
bloco_atual: |
  BLOCO 3 ENTREGUE — o MODELO DO BANCO. dados/esquema-banco.json (o contrato: entidades CIDADE, EXPERIENCIA, VERSAO, DECLARACAO, FONTE e AFILIADO, com escada de fontes, regra de divergencia e vocabularios), dados/experiencias.json (o banco, com UM registro) e a bancada que mede os dois: ferramentas/validar-banco.py e ferramentas/mutacoes-banco.py. NADA foi ao ar: esta ilha nao tem site, nao tem Sync e nao tem /status, e dizer que verificou no ar seria inventar.
  A ESCOLHA DA ILHA: SEGUNDA TENTADA, uma perdida na corrida do push. Os cinco ESTADO.md lidos do main real: a ohmetria ja estava reservada as 19h16Z por outra execucao e saiu pelo passo 3. Pela 18.1 sobrava UMA ilha com despacho aberto do Raphael — a jornadafly, com o 'ESTA ILHA NASCE AGORA' de 14/09. Meu primeiro push de reserva foi RECUSADO, mas NAO porque alguem pegou a jornadafly: outra execucao tinha acabado de reservar a robometria e o main andou. Voltei ao passo 2 sem force push, confirmei que a jornadafly seguia com executando_desde null e a reserva foi aceita as 19h19Z. Nenhum branch claude e nenhum PR aberto para mesclar.
  REDE PELA 20.2, RETESTADA E NAO HERDADA: TRES passadas, jornadafly.com.br e www.jornadafly.com.br em 000 nas tres, aquametria.com.br em 200 nas mesmas tres. Seis medicoes de bloqueio contra tres de controle verde. Segue bloqueada e o despacho ALTO do Raphael segue aberto — o bloco 3 e arquivo no repositorio e nao toca o site.
  O BANCO NASCE COM UM REGISTRO, E ISSO E DECISAO. Duas frases do repositorio pareciam brigar: o corpus do bloco 1 fecha com 'o banco comeca vazio no bloco 3', e a secao 5 da especificacao do bloco 2 manda 'quem for escrever o bloco 3 le a 2.2 e grava o numero no banco, uma vez'. Elas falam de coisas diferentes e as duas valem: nenhum preco do CORPUS entra, e a tarifa da gondola de Veneza — colhida no bloco 2 com o ato que a sustenta (Delibera della Giunta Comunale n. 89 de 20/04/2023) — entra uma vez. NENHUMA COLETA NOVA foi feita: gravar Petra, Angkor, Ha Long, Dubai ou Buenos Aires exige ler a fonte de quem opera, e isso e bloco de coleta, nao de modelo.
  O ACHADO DA BANCADA, e ele e de REGUA e so podia aparecer num mundo que o banco nao tem: A DIVERGENCIA E SOBRE A VERSAO, NUNCA SOBRE A EXPERIENCIA. A regra 'sem autoridade resolve para o MAIOR' foi escrita varrendo todas as versoes de mesma unidade — e no mundo de Petra (1, 2 e 3 dias por 70, 75 e 80) ela comparou o preco de UM dia com o de TRES, reprovando uma resolucao correta. Enquanto a experiencia tem versao unica as duas contas dao o mesmo numero e ninguem ve; e a mesma forma do defeito dos dois 63 da R1 da Robometria. Conserto na raiz: DECLARACAO ganhou o campo versao, declaracao sem versao atribuida NAO participa da resolucao (e conteudo na tela, nao voto na conta), e a conta passou a varrer so a versao resolvida.
  E ISSO ACENDEU UMA DIVIDA REAL DO PROPRIO BANCO: as QUATRO declaracoes divergentes da gondola estao com versao null, porque nenhuma das fontes diz se fala do passeio diurno ou do noturno. A ilha tem quatro divergencias e ZERO votos na conta — quem resolve hoje e a autoridade, sozinha. Esta contado no resumo como declaracoes_sem_versao e nao escondido.
  A SEGUNDA DIVIDA E DE COLETA E JA ESTAVA NO BLOCO 2: duas das quatro declaracoes NAO TEM PUBLICADOR NOMEADO — o bloco 2 anotou o que o CONJUNTO de paginas de topo publica, sem separar quem disse qual numero. Pela regra desta ilha, declaracao sem nome nao vai para a tela: 'algumas paginas dizem 30 a 90 euros' e exatamente a frase sem dono que a ilha existe para nao escrever. As duas ficam no banco como evidencia de coleta, com publicavel_na_tela=false DERIVADO e conferido pelo validador.
  A SECAO 26 APLICADA AO CAMPO QUE DOI NESTA ILHA: la o fabricante batiza a peca pela posicao e o banco classifica pela funcao; aqui o publicador escreve um NUMERO e ninguem declara a UNIDADE. unidade_de_preco e capacidade_maxima nascem com declarada_por (no_ato_oficial, no_texto_da_fonte ou no_contraste_da_propria_fonte) e sem uma das tres o registro nao nasce. A lista dos campos mora no ESQUEMA, nunca dentro da regua (26.2), e a mutacao que APAGA a chave do esquema reprova.
  O PISO DA 25.2 E DERIVADO, NAO DIGITADO: url_busca_produto e fabricada pelo validador a partir do molde do esquema com o slug_plataforma da cidade e comparada com o que esta gravado. Itens sem saida de compra: 0 (erro duro). Piso nao rastreavel: 1 — divida de comissao, nao defeito de pagina, e nenhum programa de afiliado esta cadastrado, entao o link sai cru, com rel nofollow noopener e NUNCA sponsored.
  VERIFICACAO, 0 falha: validar-banco.py verde sobre o banco real; mutacoes-banco.py com 45 mutacoes — 4 MUNDOS que tem de PASSAR (preco por pessoa com escada de dias, preco de crianca e temporada; preco por cabine; item com link rastreado e intestavel; experiencia sem divergencia nenhuma) e 41 QUEBRAS que tem de REPROVAR —, todas decidindo certo nos DOIS lados da fronteira. Tres mutacoes atacam o ESQUEMA e nao o dado: apagar a lista de campos que exigem origem, apagar a escada de fontes e apagar o molde do piso.
  ABERTO E NOMEADO: (a) a frase de tela da 26.3, que le declarada_por e escolhe a atribuicao ('o operador declarou' vs 'a ilha classificou'), NAO existe — nao ha pagina; divida nomeada ate o bloco 4; (b) as quatro declaracoes sem versao e as duas sem publicador, acima; (c) o endereco exato da pagina do Servizio Gondola nao foi registrado e a leitura direta segue barrada pelo egresso, o que trava a fonte no nivel 3; (d) o host do molde do piso esta na forma em que foi VISTO no bloco 2, sem www, e nao foi possivel abrir a URL para conferir a canonica; (e) cambio-eur-brl e cambio-usd-brl seguem pendentes, entao nenhum preco em real; (f) a secao pendente do VOZ.md e do Raphael e vem ANTES da primeira pagina; (g) a rede da ilha e o 3b em diante seguem travados.
  PROXIMO PASSO DESBLOQUEADO: a CARGA do banco — ler na fonte de quem opera as experiencias que o bloco 2 mediu (Petra, Angkor, Ha Long, Dubai, Buenos Aires, balao da Capadocia), com data_leitura e unidade declarada, ate haver banco suficiente para o portao de dado da secao 9 (3 itens reais por pagina). Nao depende de site nem da rede da ilha; depende de busca web, que esta aberta. A F1 (bloco 4) depende dela, e nao o contrario.
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

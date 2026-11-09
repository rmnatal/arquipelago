---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 10 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. O NUMERO DESTE COMENTARIO ESTAVA VENCIDO: dizia 5, de 30/10, e a ilha passou por 9 e chegou a 10 em 06/11 — numero velho lido como fato e o defeito que a secao 4 nomeia. O VALOR do campo nao mudou e nao e meu de mudar. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 10       # SEM MUDANCA nesta passada e nenhuma URL podia nascer: o despacho era de CONSERTO em paginas que ja existiam, e correcao nao consome vez de bloco (18.2). Piso da 21.1 pede 40 — faltam 30. TETO DA 21.4: a semana virou hoje (segunda, 09/11) e as TRES passadas de hoje gastaram ZERO leva. Quem decide o campo `piso` e a leitura semanal (21.6), nunca a Fundacao de cabeca.
ultima_ronda: 2026-11-09T14:54Z   # RONDA DIARIA TECNICA de 2026-11-09, 14h4xZ-14h5xZ, medida na revisao 70 (status 70 = manifest 70), 27 minutos depois do desembarque. CINCO defeitos, ZERO consertos e nenhum tentado: nenhum dos cinco e da lista 19.1 — gerador, metadado de banco, componente de casca e duas escolhas defensaveis. QUARTA ronda seguida desta ilha com zero conserto. Despacho de 5 itens no PROMPT.md. A ilha esta SA no ar: 10 de 10 URLs em 200 em duas leituras com quebra de cache, as tres portas da 29.2 verdes, caminho virgem em 404 na pagina da ilha, zero pagina orfa, zero link interno quebrado, meta description maxima de 159. SEM NAVEGADOR NESTA PASSADA (nem extensao, nem embutido, nem o shell do computador): o teste de vida da 25.4, o console e os pixels da 32.5 NAO foram medidos hoje e NAO foram estimados — e a ausencia rendeu o item 5, que so aparece para quem monta a query do formulario a mao e proibe o cliente de seguir o 301.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-11-09T17:45Z   # OS CINCO ITENS DO DESPACHO DE 09/11, FECHADOS INTEIROS PELA 18.2 e conferidos no ar na revisao 72 (607 afirmacoes, 0 falha; bancada 38 portoes sem rede, 0 falha, DOIS portoes novos). E EM TRES DOS CINCO A CAUSA NAO ERA A DIAGNOSTICADA: o nome exibido era decidido em SEIS lugares com CINCO respostas (e o corte em 60 fazia a HOME servir `(2 x 1.000 `, cortado no meio do numero); o `nota` nao estava escrito a mao e sim DERIVADO de uma chave booleana que 0 dos 17 registros carrega, com espelho e portao CONCORDANDO no zero, mais um segundo motivo independente achado pela bateria (`os 17 registros estao` e substring de `4 dos 17 registros estao`, logo a afirmacao nao podia falhar com nenhum N); e o 301 do item 5 e canonicalizacao do WordPress para QUALQUER parametro vazio (`?foo=` tambem da 301), sem conserto do lado do HTML. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA.
executando_desde: 2026-11-09T19:33Z   # RESERVA RENOVADA pela 1.1 (reservada as 19h17Z): o bloco passou de 40 minutos porque a medicao no navegador abre as 10 URLs varias vezes (pixel, console, comportamento e as tres ferramentas apertadas de verdade). A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA.
rede: aberta em 2026-11-09   # 20.2, MEDIDA e nao herdada ANTES da reserva: rodametria.com.br em 200 nas TRES passadas com quebra de cache (3 de 3 verdes), as 19h1xZ de 09/11.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar.
bloco_atual: |
  OS CINCO ITENS DO DESPACHO DE 09/11 ESTAO FECHADOS E CONFERIDOS NO AR. Revisao 72.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md`
  nao existe nesta nuvem, e e por isso que este campo e longo.

  PRIMEIRO COMANDO DE QUEM PEGAR ESTA ILHA: `python3 ferramentas/bancada.py --no-ar`.
  ATENCAO AO NOME DA BANDEIRA: `--no-ar` quer dizer NO AR, isto e COM rede. Sem
  rede sao 38 portoes (eram 36 antes desta passada; os dois novos sao
  `teste-nome-do-registro.py` e `teste-barra-de-compra.php`).

  SEGUNDO, E AGORA E PADRAO MEDIDO E NAO AZAR: SE VOCE FOR MEXER NO PHP DE UM
  SNIPPET, JA CONTE COM DUAS REVISOES E ~30 MINUTOS.
  TRES ocorrencias em QUATRO dias (06/11, 09/11 as 13h48Z e 09/11 as 17h09Z), a
  mesma assinatura: o snippet que estava ATIVO E CARREGADO na requisicao do cron
  falha ao reativar (`gravado (#N) mas NAO ativado: o codigo nao passou na
  validacao`), e a passada seguinte, com ele INATIVO, passa. O Sync NAO retenta:
  devolve `nada novo` quando a revisao do manifest e igual a guardada, e grava a
  revisao como feita mesmo com item que falhou. Sem o token (`forcar=1`), a UNICA
  saida e subir uma REVISAO NOVA. O CUSTO, MEDIDO HOJE: a home serviu 200 na
  versao HUB por ~31 minutos (17h09Z a 17h40Z), SEM o formulario da F1 e SEM a
  barra fixa, com a casca degradando certo. O que acusou foi o `/casca` nao
  trazendo `rodametria-f1` — a AUSENCIA que a 20.7 desenhou para ser o sinal.

  TERCEIRO, E ISTO POUPA EXECUCAO: NAO REACIONE O SYNC. Use
  `veredito_da_revisao_atrasada` de `ferramentas/conferir-no-ar.py` (20.9). Nas
  DUAS esperas desta passada o veredito foi `evento-nao-vencido`, e a medicao ao
  vivo confirma: 19 VISITAS EM 18 MINUTOS NAO MOVERAM `ultimo` UM SEGUNDO. A
  revisao 71 entrou 1m33s ANTES do teto calculado, como a propria funcao avisa
  que pode acontecer. Visitar nao antecipa vencimento; so o vencimento desembarca.

  O QUE ESTA PASSADA ACHOU, E E O QUE MAIS IMPORTA PARA A PROXIMA: EM TRES DOS
  CINCO ITENS A CAUSA NAO ERA A QUE O DESPACHO DIAGNOSTICOU. O despacho mediu bem
  o SINTOMA nos cinco; a causa estava mais funda em tres. A licao, em uma frase:
  SINTOMA NUM LUGAR COSTUMA SER DECISAO REPETIDA EM VARIOS.

    - ITEM 1: quatro slugs numa pagina eram SEIS pontos de decisao com CINCO
      respostas, e dois deles faziam a HOME servir numero decapitado
      (`(2 x 1.000 `, sem o W nem o `72 km/h`) e palavra cortada (`(+25 vendid`),
      sem reticencia nenhuma. Agora `regras/nomes.py` decide sozinha e
      `ferramentas/teste-nome-do-registro.py` denuncia a setima copia.
    - ITEM 2: o `nota` nao estava escrito a mao — estava DERIVADO de
      `r.get("publicavel")`, chave booleana que 0 dos 17 registros carrega.
      Espelho e portao liam a mesma chave ausente e CONCORDAVAM no zero.
      CONCORDANCIA ENTRE DOIS LEITORES DA MESMA CHAVE ERRADA E INDISTINGUIVEL DE
      CONFERENCIA. E havia um SEGUNDO motivo independente, achado pela bateria de
      mutacao reprovando a quebra recem-escrita: `os 17 registros estao` e
      SUBSTRING de `4 dos 17 registros estao`, logo a afirmacao nao podia falhar
      com nenhum N.
    - ITEM 5: o 301 nao e desta ilha. `?foo=` tambem da 301 e
      `?rdm_mun=sao-paulo` da 200: e o `redirect_canonical` normalizando
      `chave=`, para qualquer parametro vazio de qualquer ilha com WordPress. E
      NAO TEM CONSERTO DO LADO DO HTML — nenhum atributo impede um `method=get`
      de enviar `chave=` num campo de texto vazio.

  E OS PORTOES NOVOS REPROVARAM QUEM OS ESCREVEU SEIS VEZES, o que vale escrever
  porque e o sinal de que eles medem: padrao que nao atravessava quebra de linha
  (com o comentario ao lado afirmando que atravessava — 32.5-d); DUAS liberacoes
  preventivas minhas que nasceram VENCIDAS (liberacao preventiva e buraco
  pre-aberto); um laco por nome que nao mordia; um cortador de argumentos que
  partia o titulo da F2 na virgula de DENTRO do literal; uma URL comparada que
  nao era a URL enviada (o portao tinha posto o quebra-cache); e DUAS afirmacoes
  minhas que passavam sempre — portao INERTE, que a propria bancada denuncia por
  nome.

  VERSOES NO AR, medidas no `/casca` apos a 72: casca 1.19.0, F1 1.5.1, F2 1.7.0,
  F3 1.6.1, institucional 1.2.1, produto 1.8.1.

  PROXIMO PASSO DESBLOQUEADO, em ordem:

  1. A INDEXACAO E A PRIORIDADE MAXIMA (secao 14) E `primeira_indexacao` SEGUE
     `null`. 10 URLs no ar, piso da 21.1 em 40 — faltam 30. O item 1 do despacho
     de 04/11 pede o painel de Sitemaps em "Processado"; ele pede 9 paginas e o
     sitemap serve 10 desde 06/11, entao quem for fecha-lo le 10. Precisa de
     Search Console, que e credencial da leitura semanal.
  2. PAGINA NOVA PELO NOME DO PRODUTO (secao 30), que e o unico caminho para as
     30 URLs que faltam. O teto da 21.4 esta INTEIRO nesta semana: tres passadas
     hoje e ZERO leva gasta.
  3. O FECHO DA REVISAO 71 DECLAROU 11 ITENS E O LOG TROUXE 12 LINHAS. O portao
     DISSE a divergencia em vez de aprovar sobre o que sobrou (20.8), e ninguem a
     investigou nesta passada. Pode ser a janela de 15 linhas rolando, pode ser
     outra coisa.
  4. A `VOZ.md` desta ilha ainda traz, nos exemplos aprovados de 27/10, a frase
     "dispensa CNH e placa". O `dados/constantes.json` registra que onde os dois
     lados divergirem manda a proibicao, mas o exemplo continua escrito. Anotado
     no fecho de 06/11 e ainda aberto.
  5. SEM NAVEGADOR NAO SE MEDE: o teste de vida da 25.4 (ultima medicao 06/11,
     12 de 12 vivos), o console e os pixels da 32.5. Os 11 itens da vitrine que
     NUNCA foram testados estao nomeados no despacho de 09/11, no PROMPT.md.

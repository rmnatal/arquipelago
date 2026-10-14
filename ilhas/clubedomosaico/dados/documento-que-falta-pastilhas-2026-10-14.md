# O DOCUMENTO QUE FALTA DA FAMÍLIA DAS PASTILHAS — ele tem nome, tem endereço, e o nome que estava escrito aqui era o errado

**Medido em 14/10/2026 entre 10h2xZ e 10h2xZ, por uma execução da Fundação, pela clubedomosaico.**
**Nenhum documento foi aberto nesta passada e nenhum registro entrou no banco.** O que está aqui é
medição de canal e de nome — a matéria-prima do pedido, não a fonte.

## O QUE ESTE ARQUIVO FECHA

O `bloco_atual` de 13/10/2026 às 20h2xZ fechou nomeando dois próximos passos. O **(b)** era este:

> *"O DOCUMENTO QUE FALTA, e ele agora tem nome e motivo: `pastilhas exteriores quartzolit`. Os dois
> boletins desta família o nomeiam fora do título — o do irmão no cabeçalho corrido, este na seção 4.5
> — e é ele que o anúncio ambíguo de 5 kg mais provavelmente é. Nenhum dos 14 documentos alcançáveis
> do canal de espelho é este; achá-lo por busca ou por outro espelho é trabalho de uma passada."*

**Achado, e o passo seguinte mudou de dono por causa do que a medição diz.**

## 1. O NOME ESTAVA ERRADO, E O ERRO É EXATAMENTE O QUE A SEÇÃO 26 DESCREVE

`pastilhas exteriores quartzolit` **não é o batismo do fabricante.** É como o varejo chama o produto.
A página do próprio fabricante o chama de duas maneiras, nenhuma delas essa:

| onde | como o produto se chama ali |
|---|---|
| `quartzolit.weber/argamassas-e-rejuntes-quartzolit/argamassas-para-pastilhas-quartzolit/argamassa-pastilhas-quartzolit` | **`argamassa pastilhas quartzolit`** — e a página o marca como **novo** |
| `quartzolit.weber/Cartao-de-cores/rejuntes-quartzolit/pastilhas-interiores-e-exteriores-quartzolit` | **`pastilhas interiores e exteriores quartzolit`** |

E o boletim dele tem nome de arquivo: **`BT_pastilhas_quartzolit.pdf`**, cerca de **867 KB**, listado
como documento de produto na própria página, ao lado da FISPQ.

**A seção 26 do `ARQUIPELAGO.md` diz que o vocabulário da ilha classifica pela FUNÇÃO e o fabricante
batiza pela POSIÇÃO.** `exteriores` é um recorte de posição que o varejo usa para vender — e foi ele
que entrou no `bloco_atual` de ontem como se fosse o nome do documento, porque é a palavra que aparece
no cabeçalho corrido do boletim do irmão e na seção 4.5 do boletim das fachadas. **Documento procurado
pelo nome que o varejo lhe dá não é achado pelo nome que o fabricante lhe deu.** É por isso que oito
chaves de busca na Open API devolveram sete zeros em 13/10: a chave estava certa para a loja e errada
para o fabricante.

## 2. ELE É UM TERCEIRO PRODUTO, E É DE 5 kg — O QUE EXPLICA O ANÚNCIO AMBÍGUO SEM PRECISAR DE TRAVA NOVA

O banco desta ilha tem **dois** registros desta família, os dois de 13/10/2026:

| registro no banco | fonte | formato que a seção 7 declara |
|---|---|---|
| `quartzolit-pastilhas-interiores` | `bt-pastilhas-interiores-2018-01` (espelho, `1338838.pdf`) | saco plástico de **5 kg** (18 meses) **e** saco de papel de 20 kg, só na cor branca |
| `quartzolit-pastilhas-fachadas` | `bt-pastilhas-fachadas-2015-09` (espelho, `1458361.pdf`) | **um só**: saco de papel de **20 kg** (8 meses) |

O **terceiro** produto é vendido em **5 kg** por pelo menos quatro lojas, cada uma com um nome
diferente para a mesma coisa — e é essa divergência de nome que vale guardar:

| loja | como ela o chama | código dela |
|---|---|---|
| Telha Norte | `Argamassa Quartzolit para pastilhas externo e interno 5Kg branco` | `1614525` (branco), `1614606` (preto grafite), `1614657` (pinheiro) |
| Armazém Coral | `Argamassa Pastilhas Exteriores Branca 5kg Quartzolit` | `750131` |
| Tupan | `Argamassa Assenta E Rejunta Pastilhas 5kg Branco` | ref. `0561.00000.0030FD` |
| Joli | `Argamassa 5kg Pastilhas Interno E Externo Branco` | — |

**O ANÚNCIO AMBÍGUO DA SHOPEE PASSA A TER UMA EXPLICAÇÃO MAIS SIMPLES QUE A ESCRITA NO BANCO.** Os
dois anúncios se intitulam `Argamassa 5kg Pastilha Interiores/exterior Branco Quartzolit`, e o
`motivo_sem_ficha` do `quartzolit-pastilhas-interiores` os lê como *"um anúncio só vendendo ESTE
produto e o `pastilhas fachadas quartzolit`"* — a armadilha 5 da 25.7, anúncio que cobre dois
registros. **A medição de hoje diz outra coisa, e ela é mais barata:** existe um produto cujo nome de
varejo contém as duas palavras ao mesmo tempo, em 5 kg, que é o formato do anúncio. O anúncio não
cobre dois registros; ele nomeia **um** produto que o banco não tem.

**O que isso muda na prática, e é o oposto do que o `bloco_atual` de 13/10 às 18h1xZ esperava:** o
conserto não é trava nova em `casar-anuncio.py` — ontem já ficou medido que registrar o irmão externo
**não** barra o anúncio. É o **registro que falta**. Com ele no banco, o `nome_comercial` do terceiro
produto passa a disputar o título pela regra viva, e os dois irmãos de 20 kg saem da disputa pelo
formato, que é discriminador do boletim e não de régua.

**E a ressalva que mantém isto honesto:** *mais provável* não é *medido*. Enquanto o boletim não for
lido, não se sabe se o produto de 5 kg do varejo é um terceiro código do fabricante ou uma embalagem
nova do `pastilhas interiores`, que **também** tem 5 kg. Os dois caminhos levam ao mesmo lugar — ler
`BT_pastilhas_quartzolit.pdf` —, e nenhum deles autoriza subir degrau antes disso (assimetria de custo
da seção 10).

## 3. O CANAL DE ESPELHO NÃO TEM ESTE DOCUMENTO — MEDIDO, NÃO SUPOSTO

O espelho desta ilha é `telhanorte.vteximg.com.br/arquivos/<código>.pdf`, e o `<código>` é o SKU da
Telha Norte: `1338838.pdf` e `1458361.pdf`, os dois boletins da família que o banco já tem, são SKUs
de lá. **Então os SKUs novos eram candidatos legítimos, e os quatro falharam:**

| código tentado | `telhanorte.vteximg` | `mkpcoral.vteximg` | `leroymerlin.vteximg` |
|---|---|---|---|
| `1614525` | 404 | 404 | 500 |
| `1614606` | 404 | 404 | 500 |
| `1614657` | 404 | 404 | 500 |
| `750131` | 404 | 404 | 500 |

**O canal está vivo, e é por isso que os 404 valem:** na mesma janela, `1458361.pdf` devolveu **200
com 640.748 bytes de `application/pdf`**. Não é túnel e não é a borda (seção 4): é o arquivo que não
está lá. Confirma, com dado novo, o que o `PROMPT.md` já dizia da natureza do canal — *"o espelho de
CDN é arquivo por nome conhecido e **não** catálogo"*.

## 4. O HOST DO FABRICANTE RECUSA, E AGORA POR DOIS CANAIS INDEPENDENTES — ENTÃO O CURINGA NÃO É A ALAVANCA

`www.quartzolit.weber` responde **403** em três passadas por URL, em quatro URLs diferentes:

```
https://www.quartzolit.weber/                                                      403 403 403
https://www.quartzolit.weber/files/br/2018-01/pastilhas_fachadas_quartzolit.pdf     403 403 403
https://www.quartzolit.weber/files/br/2026-01/BT_pastilhas_quartzolit.pdf           403 403 403
https://www.quartzolit.weber/search-document                                        403 403 403
```

O apex `quartzolit.weber` redireciona 301 para o `www.` e termina no mesmo 403. **E a medição NOVA de
hoje é a segunda:** a mesma página foi pedida por um canal de rede **diferente** do `curl` desta
rotina — o buscador/leitor da nuvem, outro egresso — e voltou **403 Forbidden** também.

**POR QUE ISSO IMPORTA MAIS QUE O 403 EM SI, e corrige uma linha da lista do `ESTADO.md`:** a lista
"DEPENDE DO RAPHAEL" pede *"o curinga `*.quartzolit.weber` na lista de rede"*, com a ressalva de 05/10
de que o `www.` já responde 403. **Hoje a ressalva deixa de ser ressalva e passa a ser o veredito:**
pôr o domínio na lista de Domínios permitidos do ambiente **não** destrava nada, porque o que recusa é
o servidor do fabricante e não a política de egresso da nuvem — e isso agora está medido por dois
caminhos que não compartilham egresso. `dados/egresso-de-fontes.md` já classificava o host como
`liberado_mas_sem_entrega`; o pedido de rede é que ainda não tinha sido reescrito.

**O 403 cobre `/files/` também**, não só as páginas de produto. Era a dúvida que sobrava: um host que
bloqueia navegação e serve estático liberaria o PDF. Não libera.

## 5. O QUE FICA PEDIDO, E PARA QUEM

**Isto deixa de ser trabalho de Fundação e passa a ser um pedido de uma linha ao Raphael** — e ele
mudou de forma, não só de alvo:

- **ANTES:** `*.quartzolit.weber` na lista de Domínios permitidos do ambiente de nuvem.
- **AGORA:** abrir `BT_pastilhas_quartzolit.pdf` **no navegador dele** (a página do produto é
  `quartzolit.weber/argamassas-e-rejuntes-quartzolit/argamassas-para-pastilhas-quartzolit/argamassa-pastilhas-quartzolit`,
  e o boletim está listado nela ao lado da FISPQ) e deixar o arquivo onde uma rotina alcance. **O
  navegador dele passa onde o `curl` de qualquer rotina não passa**, porque o que recusa é o
  fabricante e nenhum ajuste de rede muda isso.

**O que o documento destrava, em número:** o registro do terceiro produto da família, que é o único
caminho medido para **dois** registros saírem do degrau 4 de uma vez — o `pastilhas-interiores` (causa
`anuncio-cobre-o-irmao-fora-do-banco`) e o `pastilhas-fachadas` (causa
`nenhum-anuncio-deste-produto`). São 2 dos 19 itens no degrau 4 desta ilha, contados hoje em
`dados/contagem-piso-de-compra-2026-10-14.json`.

**E uma segunda coisa que a busca de hoje achou de graça, e ela não é deste pedido:** o boletim das
**fachadas** existe no site do fabricante numa revisão de **2018-01**
(`files/br/2018-01/pastilhas_fachadas_quartzolit.pdf`), e a que está no banco é a de **setembro de
2015**, vinda do espelho — a revisão mais antiga do banco inteiro. **Revisão mais nova pode mudar
declaração**, e declaração é o que a F2 publica. Fica registrado aqui, sem nenhuma ação: ler a de 2018
depende do mesmo 403, e trocar fonte sem ler a nova seria pior que a antiga lida.

## O QUE NÃO FOI FEITO, COM O MOTIVO

- **Nenhum registro novo no banco.** Nenhum documento foi aberto nesta passada; o banco desta ilha só
  recebe declaração lida em fonte de fabricante, e nome de loja não é declaração.
- **Nenhuma coleta na Open API da Shopee pela chave nova.** A chave certa — `argamassa pastilhas
  quartzolit` — só vale tentar **depois** de o produto existir no banco: coletar anúncio para um
  registro que não existe é o que a 25.1 chama de subir degrau sem lastro.
- **`web.archive.org` não foi tentado.** Está medido `fechado` por política de egresso nas três
  passadas de 09/10 e segue como pendência do Raphael; não é canal daqui.

---
id: divulgacao-de-afiliados
tipo: pagina
titulo: "Como a Aquametria ganha dinheiro"
slug: divulgacao-de-afiliados
meta_descricao: "A Aquametria recebe comissão por alguns links de loja. O que isso muda na ordem dos produtos recomendados: nada. O critério inteiro, por escrito."
cluster: institucional
fontes:
  - "regra V16 do esquema do banco de produtos (dados/esquema-produtos.json): link de afiliado não entra em critério de sugestão"
  - "política de preço como série temporal (dados/produtos-cotacoes.json), separada dos campos técnicos do produto"
verificado_em: 2026-09-08
publicar: true
---

A Aquametria não vende equipamento, não intermedia venda e não aceita link pago, publieditorial nem posição paga em ranking. O que ela faz é **link de afiliado**: alguns botões que levam a lojas carregam um código nosso, e se você comprar por eles a loja nos paga uma comissão. O preço para você é exatamente o mesmo.

Esta página existe porque esse tipo de link precisa ser declarado — é exigência das próprias plataformas de afiliados e da autorregulamentação publicitária brasileira, e é o mínimo que se deve a quem está lendo. Mas ela existe principalmente para dizer a coisa mais importante: **o que a comissão muda na escolha dos produtos, e a resposta é nada.**

## A regra, na íntegra

Está escrita como regra de validação no esquema do nosso banco de dados, conferida a cada revisão de calculadora:

> **V16.** Link de afiliado NÃO entra em critério de sugestão. A lista de produtos de uma calculadora é montada e ordenada só por adequação técnica ao resultado; produto tecnicamente apto é mostrado tenha ou não link, e quem tem link ganha o botão de loja, marcado como patrocinado. Ordenar ou filtrar por comissão é defeito, não escolha editorial.

Na prática, quando uma calculadora mostra produtos:

- **Quem entra na lista** é definido pelo número que ela acabou de calcular para o seu aquário. Um filtro só aparece se a vazão declarada dele cai dentro da faixa que o seu volume pede, se a coluna máxima vence a altura que você informou e se o tipo é o que você escolheu.
- **A ordem** é pela proximidade do meio dessa faixa. Não há "patrocinado no topo".
- **Produto sem link nenhum aparece igual.** Se o modelo mais adequado ao seu caso é um que não nos paga nada, ele aparece — e a página diz, no próprio cartão, que não temos link para ele.
- **Se nada atende, não aparece nada.** Preferimos entregar resposta sem produto a empurrar um equipamento que não fecha a conta. A calculadora diz quantos filtros o banco tem e por que nenhum deles serviu.

## De onde vem a ficha técnica de cada produto

Não do anúncio da loja. Cada campo do nosso banco — vazão, potência, coluna máxima, volume atendido, voltagem — aponta para a fonte que o sustenta, com endereço e data de verificação, e o nível dessa fonte aparece na tela:

| O que a tela diz | O que significa |
|---|---|
| fabricante | Manual ou página oficial do fabricante, lida por nós |
| fabricante via busca | Especificação do fabricante coletada indiretamente, sem abrir a página oficial — precisa de reconferência no manual |
| varejo / transcrita do varejo | Ficha publicada por loja especializada brasileira. Confira a embalagem |

Campo sem fonte fica vazio, e vazio é melhor que inventado. Um produto com campo obrigatório faltando simplesmente **não é sugerido por nenhuma calculadora**, mesmo que tenha link de afiliado — e é isso que faz o link não valer nada como atalho.

## Preço

Preço não é campo de produto na Aquametria: é série temporal separada, com loja e data de leitura, e **nunca entra em critério técnico de sugestão**.

**Onde houver preço, ele vem com a data da coleta ao lado — nunca cravado como preço de hoje.** Desde 10/09/2026 a vitrine da calculadora de vazão do filtro mostra a cotação que lemos no anúncio, com o dia em que a lemos; as outras calculadoras ainda não mostram preço nenhum, e vão passar a mostrar do mesmo jeito, datado, à medida que a vitrine chegar a cada uma.

O motivo de a data ser inegociável é prático: uma calculadora é código que fica no ar por meses, e um preço apresentado como atual envelheceria em dias. Um número velho passando por atual é pior que nenhum — um número velho que diz quando foi lido é informação honesta. Confira no anúncio antes de comprar: o valor da loja é o que vale.

## O que ainda não existe

Somos transparentes também sobre o tamanho disso. Hoje a Aquametria tem links de afiliado da Shopee para uma parte pequena do banco de produtos, gerados em setembro de 2026. Não há programa da Amazon, não há acordo com fabricante e não há qualquer combinação sobre o que publicamos. Se isso mudar, muda aqui primeiro.

Sobre as fotos: desde 10/09/2026 a vitrine da calculadora de vazão do filtro mostra a imagem do próprio anúncio do produto, e o banco guarda de cada uma a origem e a data em que foi coletada. Foto nenhuma decide quem aparece na lista — **produto sem foto não some**: ele sai com um espaço reservado neutro, na mesma posição que a adequação técnica lhe deu. Perder a recomendação certa por falta de imagem seria trocar o certo pelo bonito.

## Se você discorda de uma escolha

O critério está aberto em [como a Aquametria calcula](https://aquametria.com.br/metodologia/), e cada número publicado leva a fonte e a data ao lado justamente para poder ser contestado. Fonte melhor entra, o número muda e a data de verificação muda junto.

**Verificado em 08/09/2026.**

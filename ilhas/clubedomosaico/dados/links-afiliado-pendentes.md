# Links de afiliado — Clube do Mosaico

**Estado em 13/09/2026:** 10 dos 20 itens do banco com link de afiliado vivo — 9 pela Shopee e 1 pelo Mercado Livre. **Nenhum material espera link.** As 10 pastilhas estão fora por decisão registrada abaixo.

## A DESCOBERTA QUE VALE PARA TODAS AS ILHAS

**O gerador da Shopee funciona por máquina. O do Mercado Livre não.**

- **Shopee** (`affiliate.shopee.com.br/offer/custom_link`): aceita até 5 URLs por vez, campos Sub_id 1 a 5, e responde a clique programático. Os links saem **na mesma ordem** em que as URLs entraram, num `textarea` de resultado. Medido de ponta a ponta em 13/09/2026 — nove links gerados numa sessão. **Sub_id aceita maiúscula** (`F1`, `F2` entram como estão), ao contrário da etiqueta do Mercado Livre.
- **Mercado Livre** (`mercadolivre.com.br/afiliados/linkbuilder`): tem reCAPTCHA. Clicar "Gerar" por script não dispara requisição nenhuma. Depende do Raphael.

**Consequência para a fábrica: a Shopee passa a ser o caminho padrão de link, e não só por cobertura de catálogo — é o único dos dois que a máquina consegue percorrer sozinha.** O Mercado Livre continua valendo para o que a Shopee não vende (foi por isso que ele entrou, em 09/09), mas cada item que só existe lá vira uma pendência com nome e sobrenome na lista do Raphael.

## Os 9 links vivos

Todos com Sub_id 1 = `clubedomosaico`. Gerados em 13/09/2026.

| item do banco | arquivo | Sub_id 2 | link |
|---|---|---|---|
| tekbond-silicone-acetico-construcao | colas | F2 | https://s.shopee.com.br/9fKqoq8pmC |
| tekbond-silicone-neutro | colas | F2 | https://s.shopee.com.br/9peH198CRF |
| cascola-cascorez-extra | colas | F2 | https://s.shopee.com.br/W6btt21Hf |
| loctite-durepoxi | colas | F2 | https://s.shopee.com.br/9Ki0QEA6SA |
| quartzolit-rejunte-acrilico | rejuntes | F2 | https://s.shopee.com.br/9V1QcX9T7D |
| quartzolit-rejunte-epoxi | rejuntes | F2 | https://s.shopee.com.br/AKaXc46IQO |
| quartzolit-rejunte-piscinas | rejuntes | F2 | https://s.shopee.com.br/1qbzUUOFBe |
| quartzolit-rejunte-ceramicas | rejuntes | F1 | https://s.shopee.com.br/AKaXc8DTnU |
| quartzolit-rejunte-porcelanatos-e-ceramicas | rejuntes | F1 | https://s.shopee.com.br/AUtxoRCqSX |

**Ressalvas honestas, para quem for auditar:**
- **Nenhum dos nove foi clicado para conferir o destino.** Clicar o próprio link de afiliado suja a métrica de cliques do Raphael e, em alguns programas, é infração. A conferência foi feita pelo título do anúncio contra o `nome_comercial` do banco, não pelo destino final. Se algum link levar a produto errado, é aqui que o erro estará — a ronda da Sentinela deve tratar link morto ou trocado como defeito da seção 19.
- **Silicone acético:** o anúncio é acético transparente Tekbond 280 g, apresentação que bate com o banco, mas **não foi possível confirmar que é o SKU BRSA004 da linha "Construção"**. A F2 recomenda por TIPO, não por SKU, então serve; trocar se aparecer a linha Construção nomeada.
- **Rejuntes:** o anúncio da Shopee é por linha com escolha de cor no próprio anúncio, o que casa melhor com o banco do que o catálogo do Mercado Livre, que separa por cor.

## O item que veio pelo Mercado Livre

**`quartzolit-cimentcola-externo-acii`** → `https://meli.la/13fPigD` — etiqueta `clubedomosaicof2`, gerado pelo Raphael no painel em 13/09/2026, porque o gerador do Mercado Livre tem reCAPTCHA e não aceita clique de máquina. A máquina preencheu a etiqueta e a URL na tela; ele apertou "Gerar" e devolveu o link.

Por que este item não pôde vir da Shopee: ela não vende a cimentcola **externo AC-II** da Quartzolit — tem AC-I interna, AC-III flexível e uma AC-2 *interna* para porcelanato, todas produto diferente, e a diferença é exatamente a que a F2 usa para decidir. Ligar a qualquer uma delas seria recomendar a argamassa errada para área externa, que é o erro que faz a peça descolar.

Divergência a registrar: o banco declara **saco de 15 kg** e o anúncio é de **20 kg**. A Quartzolit vende as duas — é divergência de embalagem, não de produto, e não invalida o link.

**O padrão que isto estabelece, e vale para toda ilha:** quando um produto só existe no Mercado Livre, a máquina deixa a etiqueta escolhida e a URL colada na tela do Raphael e escreve o pedido em `dados/despachos.md`. O trabalho dele é um clique e um copiar-colar, não uma pesquisa.

## As 10 pastilhas ficaram de fora, e por quê

`materiais-pastilhas.json` tem 10 itens: nove da Glass Mosaic (K2501, K2502, MIX2510, K117, K77, K66, A11, A61, ST5102) e o AF1500 da Pastilhart. **Nenhum link foi gerado, de propósito.**

A Shopee **tem** produto Glass Mosaic — mas anunciado com outra codificação (CG10, CG21, CG33) e com nomes genéricos de cor e medida. Nenhum anúncio cita os códigos do banco. Casar K2501 com "Pastilha de Vidro Cristal 2,3x2,3 BRANCO CG10" seria um palpite, e a ilha inteira se sustenta em dizer com precisão qual produto tem qual declaração do fabricante.

**O caminho certo, para o próximo bloco de banco:** ou achar loja oficial/revendedor Glass Mosaic que cite o código no anúncio e casar por código; ou aceitar que pastilha entra como **equivalente por atributo** (medida, acabamento, cor) — e nesse caso o esquema do banco ganha um campo `afiliado.tipo_de_casamento: "equivalente"` e **a página tem de dizer isso ao leitor, na cara**, do tipo "não achamos esta referência exata à venda; este é um produto com a mesma medida e acabamento". Vender equivalente é legítimo; vender equivalente fingindo ser o exato, não.

## Imagens

Os 20 itens seguem sem imagem: a nuvem das rotinas não alcança o domínio dos fabricantes. Pendência separada desta.

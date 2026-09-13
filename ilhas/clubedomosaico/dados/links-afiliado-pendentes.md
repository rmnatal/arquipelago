# Links de afiliado pendentes — Clube do Mosaico

**Levantado em 13/09/2026 por busca na web (a nuvem não abre o Mercado Livre: a busca interna do site não renderiza em aba de segundo plano).** As URLs de produto abaixo já estão conferidas uma a uma contra o `nome_comercial` do banco. O que falta é o passo humano: abrir `mercadolivre.com.br/afiliados/linkbuilder`, escolher a etiqueta indicada, colar o bloco de URLs, apertar **Gerar** e copiar os links curtos.

**Por que o Raphael tem de apertar o botão:** o gerador do Mercado Livre carrega reCAPTCHA e ignora clique programático. As etiquetas `clubedomosaicof1` e `clubedomosaicof2` já foram criadas (13/09/2026) e aparecem no seletor.

## Bloco 1 — etiqueta `clubedomosaicof2` (8 URLs, colar de uma vez)

```
https://produto.mercadolivre.com.br/MLB-1915431798-silicone-acetico-cartucho-280g-blister-transparente-tekbond-_JM
https://www.mercadolivre.com.br/cola-adesivo-silicone-transparente-neutro-280g-tekbond/p/MLB38691363
https://www.mercadolivre.com.br/cola-branca-de-1kg-cascorez-extra-adesivo-pva-extraforte/p/MLB26891495
https://www.mercadolivre.com.br/argamassa-externa-quartzolit-ac-ii-saco-20kg-cinza-weber/p/MLB27315078
https://produto.mercadolivre.com.br/MLB-2109686664-massa-adesiva-epoxi-durepoxi-50g-loctite-henkel-01-un-_JM
https://www.mercadolivre.com.br/rejunte-acrilico-weber-quartzolit-1kg-cores-cor-ype/p/MLB24454967
https://www.mercadolivre.com.br/rejunte-epoxi-quartzolit-1kg-cinza-platina/p/MLB25541512
https://www.mercadolivre.com.br/rejunte-piscinas-quartzolit-5kg-cinza-platina/p/MLB23483782
```

Os links saem **na mesma ordem** em que as URLs entraram. Cole o resultado em `afiliado.url` dos itens, nesta ordem:

| ordem | item do banco | arquivo | observação sobre o casamento |
|---|---|---|---|
| 1 | `tekbond-silicone-acetico-construcao` | materiais-colas.json | **casamento parcial.** O anúncio é silicone acético Tekbond em cartucho de 280 g, que é a apresentação declarada no banco; não foi possível confirmar que é o SKU BRSA004 da linha "Construção". A recomendação técnica da F2 é por TIPO (silicone acético), não por SKU, então o link serve — mas se aparecer um anúncio da linha Construção, troque. |
| 2 | `tekbond-silicone-neutro` | materiais-colas.json | catálogo, silicone neutro transparente Tekbond 280 g |
| 3 | `cascola-cascorez-extra` | materiais-colas.json | catálogo, Cascorez Extra PVA extraforte 1 kg — casamento exato |
| 4 | `quartzolit-cimentcola-externo-acii` | materiais-colas.json | catálogo, argamassa externa AC-II Quartzolit/Weber. **O banco diz saco de 15 kg e o anúncio é de 20 kg** — o Quartzolit vende as duas; anotar como divergência de embalagem, não de produto. |
| 5 | `loctite-durepoxi` | materiais-colas.json | Durepoxi 50 g, 1 unidade — casamento exato |
| 6 | `quartzolit-rejunte-acrilico` | materiais-rejuntes.json | catálogo, rejunte acrílico Weber/Quartzolit 1 kg (cor Ypê). **O catálogo do ML é por cor**; o link leva a uma cor específica. Aceitável como porta de compra. |
| 7 | `quartzolit-rejunte-epoxi` | materiais-rejuntes.json | catálogo, rejunte epóxi Quartzolit 1 kg (cinza platina) — mesma ressalva de cor |
| 8 | `quartzolit-rejunte-piscinas` | materiais-rejuntes.json | catálogo, rejunte piscinas Quartzolit 5 kg (cinza platina) — mesma ressalva de cor |

## Bloco 2 — etiqueta `clubedomosaicof1` (2 URLs)

```
https://produto.mercadolivre.com.br/MLB-3855986795-rejunte-cimenticio-1kg-quartzolit-diversas-cores-_JM
https://www.mercadolivre.com.br/rejunte-quartzolit-porcelanato-e-ceramica-marfim-1kg/p/MLB32462343
```

| ordem | item do banco | arquivo | observação |
|---|---|---|---|
| 1 | `quartzolit-rejunte-ceramicas` | materiais-rejuntes.json | **o mais fraco dos dez.** O anúncio é "rejunte cimentício 1 kg Quartzolit diversas cores"; o ML não tem página de catálogo limpa da linha "Cerâmicas". Trocar quando aparecer melhor. |
| 2 | `quartzolit-rejunte-porcelanatos-e-ceramicas` | materiais-rejuntes.json | catálogo, linha Porcelanatos e Cerâmicas 1 kg (marfim) — ressalva de cor |

## As dez pastilhas ficaram de fora, e por quê

`materiais-pastilhas.json` tem 10 itens (nove Glass Mosaic — K2501, K2502, MIX2510, K117, K77, K66, A11, A61, ST5102 — e o AF1500 da Pastilhart). **Nenhum link foi levantado, de propósito.** Esses são códigos de linha de fabricante, não nomes que apareçam em anúncio de marketplace; qualquer link seria uma pastilha *parecida* de outro vendedor, e a ilha inteira se sustenta em dizer com precisão qual produto tem qual declaração. Ligar o K2501 do banco a uma placa genérica de outro fornecedor seria mentir na página que mais promete exatidão.

O caminho certo para pastilha é outro e fica escrito aqui para o próximo bloco: procurar no Mercado Livre e na Shopee por **loja oficial ou revendedor da Glass Mosaic** e casar por código na descrição do anúncio; se não existir, pastilha entra pela Shopee com busca por atributo (tamanho da pastilha, acabamento, cor) e o banco ganha um campo dizendo que o link é de *equivalente*, não do SKU — e a página tem de dizer isso na cara do leitor.

## Estado

- 10 de 20 itens do banco com URL de produto escolhida, 0 com link de afiliado gerado.
- 10 itens (pastilhas) sem URL, por decisão registrada acima.
- Todos os 20 seguem sem imagem (a nuvem não alcança o domínio dos fabricantes).

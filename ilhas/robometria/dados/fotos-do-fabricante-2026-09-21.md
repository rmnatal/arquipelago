# A FOTO DO FABRICANTE — colheita de 2026-09-21

Gerada por `ferramentas/coletar-foto-do-fabricante.py --relatorio`, para o
**despacho do Raphael de 19/09/2026**. **Nenhum numero foi digitado:** os
registros saem dos dois arquivos de banco, as portas saem de `fontes{}.url` e
`canal_brasileiro.valor`, os candidatos saem do catalogo publico de cada loja
e o estado de cada host de imagem sai de uma consulta de DNS mais um `curl`.

## O placar

| | |
|---|---|
| publicaveis sem foto (o alvo do despacho) | **66** |
| com candidato E com o nome medido na pagina | **37** |
| ... cujo ARQUIVO da foto abre daqui (pode gravar hoje) | **36** |
| ... cujo arquivo esta em host de imagem fechado | **0** |
| ... reprovado pelo OLHO, com o motivo escrito | **1** |
| sem candidato (causa registro a registro, abaixo) | **29** |

## Os hosts de IMAGEM, um a um

Nenhum deles e o host da pagina. Esta e a metade que o pedido de 20/09 nao
cobria, porque ninguem tinha tentado baixar o arquivo.

| host da imagem | DNS | HTTP | registros |
|---|---|---|---|
| `i02.appmifile.com` | resolve | 200 | 9 |
| `electrolux.vteximg.com.br` | resolve | 200 | 8 |
| `lojawap.vteximg.com.br` | resolve | 200 | 4 |
| `i01.appmifile.com` | resolve | 200 | 4 |
| `positivocasainteligente.vteximg.com.br` | resolve | 200 | 3 |
| `cdn.shopify.com` | resolve | 200 | 3 |
| `us.roborock.com` | resolve | 200 | 2 |
| `i05.appmifile.com` | resolve | 200 | 2 |
| `lojamultilaser.vteximg.com.br` | resolve | 200 | 1 |
| `blog.wap.ind.br` | resolve | 200 | 1 |

## Pode gravar hoje

| registro | prova do nome | foto |
|---|---|---|
| `electrolux-erb10` | referencia | https://electrolux.vteximg.com.br/arquivos/ids/218331/Robot-Vacuum-ERB10-Perspective-Electrolux-1000x1000-principal.jpg?v=638703122955570000 |
| `electrolux-erb11` | referencia | https://electrolux.vteximg.com.br/arquivos/ids/223967/Robot-Vacuum-ERB11-Perspective-Electrolux-600x600-1.jpg?v=638703124416570000 |
| `electrolux-erb30` | referencia | https://electrolux.vteximg.com.br/arquivos/ids/218166/Robot-Vacuum-ERB30-Perspective-Electrolux-1000x1000-principal.jpg?v=638703122771470000 |
| `electrolux-escova-rotativa-central-erb60-erb61-erb62-erb80` | tokens | https://electrolux.vteximg.com.br/arquivos/ids/286240/Cybertron_Roller_Brush_FrontView_ERB60-61-62-80_Electrolux-1000x1000.jpg?v=638990794088630000 |
| `electrolux-filtro-hepa-espuma-erb44-erb60-erb61-erb62` | tokens | https://electrolux.vteximg.com.br/arquivos/ids/286951/Cybertron_HepaSponge_Filters_FrontView_ERB44-60-61-62_Electrolux-1000x1000.jpg?v=638993366926770000 |
| `electrolux-kit-performance-erb44` | tokens | https://electrolux.vteximg.com.br/arquivos/ids/287006/Cybertron_Kit_Performance_FrontView_ERB44_Electrolux-1000x1000.jpg?v=638996098971830000 |
| `electrolux-kit-performance-erb60-erb61-erb62` | tokens | https://electrolux.vteximg.com.br/arquivos/ids/286991/Cybertron_Kit_Performance_FrontView_ERB60-61-62_Electrolux-1000x1000.jpg?v=638995955285100000 |
| `electrolux-pano-microfibra-erb60-erb61-erb62-erb80` | tokens | https://electrolux.vteximg.com.br/arquivos/ids/286236/Cybertron_Mop_Pad_FrontView_ERB60-61-62-80_Electrolux-1000x1000.jpg?v=638990709370700000 |
| `multi-pr10124` | referencia | https://lojamultilaser.vteximg.com.br/arquivos/ids/1200172/10858_00.jpg?v=638533810079900000 |
| `positivo-11206519` | referencia | https://positivocasainteligente.vteximg.com.br/arquivos/ids/158004/ESCOVA-CENTRAL-ROBO-ASPIRADOR-PRA800-E-2000---01.jpg?v=638599427963500000 |
| `positivo-pra2000` | texto | https://positivocasainteligente.vteximg.com.br/arquivos/ids/159087/01_ASPIRADOR_PRA2000.jpg?v=639101416642970000 |
| `positivo-pra500` | texto | https://positivocasainteligente.vteximg.com.br/arquivos/ids/156577/Smart-Robo-Plus-Ang.jpg?v=637940196761330000 |
| `roborock-mop-q8-max` | tokens | https://cdn.shopify.com/s/files/1/0082/3666/2902/files/062ec9c82657b2be82b68364b1fc1900_3d93e94d-6075-44a9-8ce6-fc074f589202.jpg?v=1725035616 |
| `roborock-mop-qrevo-curv` | tokens | https://us.roborock.com/cdn/shop/files/1_3183c8ba-4be6-4a98-988c-ea1f947939e3_1200x1200.jpg?v=1735031940 |
| `roborock-mop-qrevo-master` | tokens | https://us.roborock.com/cdn/shop/files/4_q_-revo_2_1200x1200.jpg?v=1757929885 |
| `roborock-mop-s8-maxv-ultra` | tokens | https://cdn.shopify.com/s/files/1/0082/3666/2902/files/Roborock_2_S8_MaxV_Ultra_S8_Max_Ultra.jpg?v=1757930347 |
| `roborock-mop-saros-10r-z70` | tokens | https://cdn.shopify.com/s/files/1/0082/3666/2902/files/2_Saros-10R-1.jpg?v=1757937015 |
| `wap-escova-direita-w300` | tokens | https://lojawap.vteximg.com.br/arquivos/ids/158329/escova-direita-para-robo-aspirador-de-po-wap-robot-w300.png?v=637425033056500000 |
| `wap-escova-esquerda-w300` | tokens | https://lojawap.vteximg.com.br/arquivos/ids/158330/escova-esquerda-para-robo-aspirador-de-po-wap-robot-w300.png?v=637425034313300000 |
| `wap-escova-frontal-wsmart` | tokens | https://lojawap.vteximg.com.br/arquivos/ids/158342/escova-frontal-para-robo-aspirador-de-po-wap-robot-wsmart.png?v=637425466210430000 |
| `wap-w300` | texto | https://lojawap.vteximg.com.br/arquivos/ids/176674/robo-aspirador-de-po-wap-robot-w300.png?v=638794554372870000 |
| `xiaomi-b106gl-bx` | texto | https://i02.appmifile.com/884_operatorx_operatorx_opx/08/07/2025/541377074c7009cc069a3376562aedef.png |
| `xiaomi-b106gl-lw` | texto | //i02.appmifile.com/940_item_sg/01/04/2025/2b65c41b58396061c9f4630ff0c6d85c.png |
| `xiaomi-b106gl-zx` | texto | //i02.appmifile.com/940_item_sg/01/04/2025/2b65c41b58396061c9f4630ff0c6d85c.png |
| `xiaomi-d106-tb` | texto | https://i02.appmifile.com/884_operatorx_operatorx_opx/08/07/2025/541377074c7009cc069a3376562aedef.png |
| `xiaomi-e10` | texto | //i01.appmifile.com/v1/MI_18455B3E4DA706226CF7535A58E875F0267/pms_1677576726.00766138.png |
| `xiaomi-e10c` | texto | //i02.appmifile.com/271_operatorx_operatorx_opx/04/09/2023/59f973327a3440b9f939a414c88c3c64.png |
| `xiaomi-e12` | texto | //i05.appmifile.com/783_item_es/11/05/2023/5c6ee8ece6e0056ed25dfa1b886dd20e.png |
| `xiaomi-mop-2` | texto | //i01.appmifile.com/v1/MI_18455B3E4DA706226CF7535A58E875F0267/pms_1666842634.01573696.png |
| `xiaomi-mop-2-lite` | texto | //i01.appmifile.com/v1/MI_18455B3E4DA706226CF7535A58E875F0267/pms_1666876968.82583141.png |
| `xiaomi-mop-s10` | tokens | //i02.appmifile.com/940_item_sg/01/04/2025/2b65c41b58396061c9f4630ff0c6d85c.png |
| `xiaomi-s10` | texto | //i01.appmifile.com/v1/MI_18455B3E4DA706226CF7535A58E875F0267/pms_1677487225.40455674.png |
| `xiaomi-s12` | texto | //i05.appmifile.com/173_item_es/11/05/2023/385ba85dd65f7d80df868ecc051cf7e6.png |
| `xiaomi-s20` | texto | //i02.appmifile.com/584_operatorx_operatorx_opx/14/06/2024/dd1fda3e2e1750fcf21bc7fa9809c1df.png |
| `xiaomi-s40-pro` | texto | //i02.appmifile.com/369_operatorx_operatorx_opx/14/08/2025/f755059f82fc027af89f4911b3ed6b08.png |
| `xiaomi-x20` | texto | //i02.appmifile.com/558_operatorx_operatorx_opx/09/01/2024/8831075b8ffaff3a137e640258d36f39.jpg |

## Reprovado pelo olho (25.3), com o motivo

| registro | foto que foi aberta | por que nao entra |
|---|---|---|
| `wap-wsmart` | https://blog.wap.ind.br/wp-content/uploads/2020/08/Wsmart-1.png | 2026-09-20: a unica imagem que ABRE desta nuvem em toda a colheita, e ela nao serve. E o banner de lancamento do blog da WAP (1516x907), com "LANCAMENTO" num selo azul e o nome do produto em letra de cartaz ocupando metade do quadro. Procedencia passa — e do fabricante e nomeia o WSMART —, mas nao e foto de produto: no espaco quadrado do cartao ela entra como peca de campanha de 2020, com texto promocional que a ilha nao escreveu e nao pode datar. Foto e ganho e nunca requisito (25.3); espaco reservado neutro e melhor que cartaz velho. |

## Tem candidato e o arquivo nao abre daqui

Estes **nao** sao duvida de procedencia: o nome do registro foi medido na
pagina do fabricante, e a URL exata da foto esta escrita aqui. Falta so o
host da imagem na lista de dominios permitidos.

| registro | marca | tipo | prova do nome | foto |
|---|---|---|---|---|

## Sem candidato, por causa

| registro | porta | causa medida |
|---|---|---|
| `electrolux-erb20` |  | sem porta de fabricante aberta |
| `multi-ho041` | https://suporte.multilaser.com.br/produtos/aspirador-robo-mars-bivolt-ho041/duvidas-frequentes | pagina devolveu 000 |
| `multi-ho243` | https://suporte.multilaser.com.br/produtos/aspirador-robo-acqua-solution-ho243/duvidas-frequentes | pagina devolveu 000 |
| `multi-ho400` |  | sem porta de fabricante aberta |
| `multi-ho407` | https://www.multilaser.com.br/aspirador-robo-3-em-1-varre-aspira-e-passa-pano-duster-multi-ho407out/p | pagina devolveu 404 |
| `multi-ho411` |  | sem porta de fabricante aberta |
| `multi-ob010` |  | sem porta de fabricante aberta |
| `multi-pr10127` | https://www.multilaser.com.br/bateria-p-aspirador-robo-ho041-versao-a-pr10127/p | a pagina abre e nao serve foto de produto no HTML (html) |
| `multi-pr10342` | https://www.multilaser.com.br/pano-para-aspirador-robo-ob010/p | a pagina abre e nao serve foto de produto no HTML (html) |
| `multi-pr10343` | https://www.multilaser.com.br/filtro-para-aspirador-robo-ob010-pr10343/p | a pagina abre e nao serve foto de produto no HTML (html) |
| `multi-pr8116` |  | sem porta de fabricante aberta |
| `positivo-11206540` |  | sem porta de fabricante aberta |
| `roborock-q8-max` | https://br.roborock.com/pages/q8-max-plus | pagina devolveu 404 |
| `roborock-qrevo-curv` | https://br.roborock.com/pages/roborock-qrevo-curv-series | pagina devolveu 404 |
| `roborock-qrevo-master` | https://br.roborock.com/pages/roborock-qrevo-master | pagina devolveu 404 |
| `roborock-s8-maxv-ultra` | https://br.roborock.com/pages/s8-maxv-ultra | pagina devolveu 404 |
| `roborock-saros-10r` | https://br.roborock.com/pages/roborock-saros-10r | pagina devolveu 404 |
| `roborock-saros-z70` | https://br.roborock.com/pages/roborock-saros-z70 | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-escova-lateral-mop-2` | https://www.mi.com/global/support/faq/details/KA-11406/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-escova-lateral-mop-2-lite` | https://www.mi.com/global/support/faq/details/KA-11405/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-escova-principal-h40-s40` | https://www.mi.com/global/product/xiaomi-robot-vacuum-h40-and-s40-brush/ | a pagina nao nomeia este registro: faltou a palavra "escova" |
| `xiaomi-escova-principal-mop-2` | https://www.mi.com/global/support/faq/details/KA-11406/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-escova-principal-mop-2-lite` | https://www.mi.com/global/support/faq/details/KA-11405/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-filtro-mop-2` | https://www.mi.com/global/support/faq/details/KA-11406/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-filtro-mop-2-lite` | https://www.mi.com/global/support/faq/details/KA-11405/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-mop-mop-2` | https://www.mi.com/global/support/faq/details/KA-11406/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-mop-mop-2-lite` | https://www.mi.com/global/support/faq/details/KA-11405/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-reservatorio-mop-2` | https://www.mi.com/global/support/faq/details/KA-11406/ | a pagina abre e nao serve foto de produto no HTML (html) |
| `xiaomi-reservatorio-mop-2-lite` | https://www.mi.com/global/support/faq/details/KA-11405/ | a pagina abre e nao serve foto de produto no HTML (html) |


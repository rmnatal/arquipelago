# SÉRIE DA PORTA DE ENTRADA — RODAMETRIA, 2026-11-17

**O que este arquivo é, e por que ele está no repositório:** o retrato da queda da porta de entrada
(seção 29) medido **segundo por segundo** pela execução da Fundação de 17/11/2026, pelo campo `porta`
que o `/casca` passou a servir **sem token** nesta mesma passada (casca 1.28.0, seção 14-b do snippet,
regra **29.4-b** do `ARQUIPELAGO.md`).

**Ele existe porque o chamado na HostGator nunca teve esta prova.** A 29.5 diz, desde 05/10/2026, que
o que falta ao chamado é *"um horário em que o arquivo foi reescrito sem que ninguém do nosso lado o
tocasse, e o nome do bloco que sobrou"*. Aqui estão **as duas pontas do ciclo com hora**, e nenhuma
mão nossa no meio: esta execução **não tem o token do Sync** desta ilha, não abriu o cPanel, e o que
havia no ar era um `git push` e requisições GET.

**AS TRÊS LINHAS DE CURA DO DIA, lidas no log do `/status`:**

```
2026-11-16 23:02 cura da porta: bloco WordPress reposto — 1057 bytes [NFD EPC] -> 1580 bytes [NFD EPC, WordPress]
2026-11-17 10:15 cura da porta: bloco WordPress reposto — 1057 bytes [NFD EPC] -> 1580 bytes [NFD EPC, WordPress]
2026-11-17 11:15 cura da porta: bloco WordPress reposto — 1057 bytes [NFD EPC] -> 1580 bytes [NFD EPC, WordPress]
```

Como a **trava 1** da 29.4 só dispara com o bloco **ausente**, cada linha dessas prova um apagamento
**anterior** a ela. Somando a de **12/11 16:25** (aquela com o arquivo em **0 bytes e nenhum bloco**),
são **quatro apagamentos em cinco dias**, e o intervalo caiu de dias para **minutos**.

**O NÚMERO QUE O CHAMADO PRECISA:** a reposição das **10:15:18Z** foi desfeita em **~4 minutos** — às
10h19:51Z as três portas da 29.2 já estavam em 404, e o campo `cura_liberada_em_s` lido às 10h41:01Z
trazia **2057**, que põe a trava exatamente em 10:15:18. **Não é "o arquivo é reescrito de vez em
quando": é "é reescrito poucos minutos depois de cada reposição".**

**E QUEM DECIDIU A DURAÇÃO DA QUEDA FOI A TRAVA, NÃO O DEFEITO.** A trava 2 da 29.4 admite **uma
tentativa por hora** e é queimada **antes** de agir, de propósito — ela existe para impedir o laço de
reescrita da raiz que a 29.4 recusou. Consequência medida: a ilha serviu 404 em tudo menos a home por
**pelo menos 55 min 29 s**, com o conserto disponível desde o primeiro segundo. **A trava não está
errada; afrouxá-la é decisão do Raphael, não de uma execução.**

**COMO LER A TABELA.** Uma linha por leitura. `tem_bloco` é o bloco `# BEGIN WordPress` no `.htaccess`
da raiz (`False` = ausente, `True` = presente, `None`/`erro` = não sei). `espera` são os segundos que
faltam para a trava 2 liberar a cura. `sitemap` e `veiculos` são os códigos HTTP de
`/wp-sitemap.xml` e `/veiculos/`, as duas com quebra de cache. `sync_ultimo` é a última rodada do Sync
— note as duas que rodaram **dentro** da queda (10:40:07 e 11:09:54) com a cura calada, que é a trava 2
funcionando como desenhada.

## SÉRIE 1 — A QUEDA E A VOLTA (92 leituras, 10h42:14Z → 11h15:20Z)

```
hora_utc	tem_bloco	cura_liberada_em_s	sitemap	veiculos	sync_ultimo
10:42:14Z	False	1983	404	404	2026-11-17 10:40:07
10:42:36Z	False	1961	404	404	2026-11-17 10:40:07
10:42:58Z	False	1939	404	404	2026-11-17 10:40:07
10:43:20Z	False	1917	404	404	2026-11-17 10:40:07
10:43:42Z	False	1894	404	404	2026-11-17 10:40:07
10:44:05Z	False	1872	404	404	2026-11-17 10:40:07
10:44:27Z	False	1850	404	404	2026-11-17 10:40:07
10:44:49Z	False	1828	404	404	2026-11-17 10:40:07
10:45:11Z	False	1806	404	404	2026-11-17 10:40:07
10:45:33Z	False	1784	404	404	2026-11-17 10:40:07
10:45:55Z	False	1763	404	404	2026-11-17 10:40:07
10:46:16Z	False	1741	404	404	2026-11-17 10:40:07
10:46:38Z	False	1719	404	404	2026-11-17 10:40:07
10:47:00Z	False	1697	404	404	2026-11-17 10:40:07
10:47:22Z	False	1675	404	404	2026-11-17 10:40:07
10:47:44Z	False	1653	404	404	2026-11-17 10:40:07
10:48:05Z	False	1632	404	404	2026-11-17 10:40:07
10:48:27Z	False	1610	404	404	2026-11-17 10:40:07
10:48:49Z	False	1588	404	404	2026-11-17 10:40:07
10:49:11Z	False	1566	404	404	2026-11-17 10:40:07
10:49:33Z	False	1544	404	404	2026-11-17 10:40:07
10:49:55Z	False	1522	404	404	2026-11-17 10:40:07
10:50:16Z	False	1501	404	404	2026-11-17 10:40:07
10:50:38Z	False	1479	404	404	2026-11-17 10:40:07
10:51:00Z	False	1457	404	404	2026-11-17 10:40:07
10:51:22Z	False	1436	404	404	2026-11-17 10:40:07
10:51:43Z	False	1414	404	404	2026-11-17 10:40:07
10:52:05Z	False	1392	404	404	2026-11-17 10:40:07
10:52:27Z	False	1370	404	404	2026-11-17 10:40:07
10:52:49Z	False	1348	404	404	2026-11-17 10:40:07
10:53:11Z	False	1327	404	404	2026-11-17 10:40:07
10:53:33Z	False	1304	404	404	2026-11-17 10:40:07
10:53:55Z	False	1282	404	404	2026-11-17 10:40:07
10:54:17Z	False	1261	404	404	2026-11-17 10:40:07
10:54:38Z	False	1239	404	404	2026-11-17 10:40:07
10:55:00Z	False	1217	404	404	2026-11-17 10:40:07
10:55:22Z	False	1195	404	404	2026-11-17 10:40:07
10:55:44Z	False	1174	404	404	2026-11-17 10:40:07
10:56:06Z	False	1151	404	404	2026-11-17 10:40:07
10:56:28Z	False	1130	404	404	2026-11-17 10:40:07
10:56:49Z	False	1108	404	404	2026-11-17 10:40:07
10:57:11Z	False	1086	404	404	2026-11-17 10:40:07
10:57:33Z	False	1064	404	404	2026-11-17 10:40:07
10:57:54Z	False	1042	404	404	2026-11-17 10:40:07
10:58:17Z	False	1021	404	404	2026-11-17 10:40:07
10:58:38Z	False	999	404	404	2026-11-17 10:40:07
10:59:00Z	False	977	404	404	2026-11-17 10:40:07
10:59:22Z	False	955	404	404	2026-11-17 10:40:07
10:59:44Z	False	933	404	404	2026-11-17 10:40:07
11:00:06Z	False	911	404	404	2026-11-17 10:40:07
11:00:28Z	False	890	404	404	2026-11-17 10:40:07
11:00:49Z	False	868	404	404	2026-11-17 10:40:07
11:01:11Z	False	846	404	404	2026-11-17 10:40:07
11:01:33Z	False	824	404	404	2026-11-17 10:40:07
11:01:55Z	False	803	404	404	2026-11-17 10:40:07
11:02:16Z	False	781	404	404	2026-11-17 10:40:07
11:02:38Z	False	759	404	404	2026-11-17 10:40:07
11:03:00Z	False	737	404	404	2026-11-17 10:40:07
11:03:22Z	False	715	404	404	2026-11-17 10:40:07
11:03:43Z	False	694	404	404	2026-11-17 10:40:07
11:04:05Z	False	672	404	404	2026-11-17 10:40:07
11:04:26Z	False	651	404	404	2026-11-17 10:40:07
11:04:48Z	False	629	404	404	2026-11-17 10:40:07
11:05:10Z	False	607	404	404	2026-11-17 10:40:07
11:05:32Z	False	585	404	404	2026-11-17 10:40:07
11:05:53Z	False	564	404	404	2026-11-17 10:40:07
11:06:15Z	False	542	404	404	2026-11-17 10:40:07
11:06:37Z	False	520	404	404	2026-11-17 10:40:07
11:06:58Z	False	499	404	404	2026-11-17 10:40:07
11:07:20Z	False	477	404	404	2026-11-17 10:40:07
11:07:42Z	False	455	404	404	2026-11-17 10:40:07
11:08:04Z	False	434	404	404	2026-11-17 10:40:07
11:08:25Z	False	412	404	404	2026-11-17 10:40:07
11:08:47Z	False	390	404	404	2026-11-17 10:40:07
11:09:09Z	False	368	404	404	2026-11-17 10:40:07
11:09:31Z	False	346	404	404	2026-11-17 10:40:07
11:09:53Z	False	324	404	404	2026-11-17 11:09:54
11:10:15Z	False	303	404	404	2026-11-17 11:09:54
11:10:36Z	False	281	404	404	2026-11-17 11:09:54
11:10:58Z	False	259	404	404	2026-11-17 11:09:54
11:11:20Z	False	237	404	404	2026-11-17 11:09:54
11:11:42Z	False	215	404	404	2026-11-17 11:09:54
11:12:04Z	False	193	404	404	2026-11-17 11:09:54
11:12:26Z	False	171	404	404	2026-11-17 11:09:54
11:12:48Z	False	150	404	404	2026-11-17 11:09:54
11:13:09Z	False	128	404	404	2026-11-17 11:09:54
11:13:31Z	False	106	404	404	2026-11-17 11:09:54
11:13:53Z	False	84	404	404	2026-11-17 11:09:54
11:14:15Z	False	62	404	404	2026-11-17 11:09:54
11:14:36Z	False	41	404	404	2026-11-17 11:09:54
11:14:58Z	False	19	404	404	2026-11-17 11:09:54
11:15:20Z	True	3600	200	200	2026-11-17 11:09:54
11:15:42Z	True	3578	200	200	2026-11-17 11:09:54
11:16:04Z	True	3556	200	200	2026-11-17 11:09:54
11:16:26Z	True	3535	200	200	2026-11-17 11:09:54
11:16:47Z	True	3513	200	200	2026-11-17 11:09:54
11:17:09Z	True	3492	200	200	2026-11-17 11:09:54
11:17:31Z	True	3470	200	200	2026-11-17 11:09:54
11:17:52Z	True	3448	200	200	2026-11-17 11:09:54
11:18:14Z	True	3426	200	200	2026-11-17 11:09:54
11:18:36Z	True	3405	200	200	2026-11-17 11:09:54
11:18:57Z	True	3383	200	200	2026-11-17 11:09:54
```

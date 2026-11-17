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
trazia **2057**, que põe a trava exatamente em 10:15:18. **ESTA FRASE FOI CORRIGIDA PELA SÉRIE 2, ABAIXO, NA MESMA EXECUÇÃO — ela generalizava UM intervalo
como se fosse uma TAXA.** O que está medido é um apagamento ~4 minutos depois de uma reposição, e um
outro que sobreviveu 27min20s. É **evento irregular**, não período.

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

## SÉRIE 2 — A JANELA NO AR, E ELA CORRIGE A FRASE ACIMA (95 leituras, 11h15:55Z → 11h42:40Z)

**A FRASE *"é reescrito poucos minutos depois de cada reposição"*, escrita na seção acima às 11h19Z
desta mesma execução, ESTÁ ERRADA, e a errata é da passada que a escreveu.** Ela generalizava **um**
intervalo — os ~4 minutos entre a reposição das 10:15:18Z e o 404 das 10h19:51Z — para uma **taxa**. A
medição seguinte a desmentiu: **95 leituras entre 11h15:55Z e 11h42:40Z, as 95 com o bloco PRESENTE e
as 95 com `/wp-sitemap.xml` e `/veiculos/` em 200.** A reposição das **11:15:20Z** sobreviveu **27
minutos e 20 segundos** de medição contínua, sete vezes mais que a anterior.

**E UM SYNC RODOU DENTRO DESTA JANELA SEM APAGAR NADA: `11:39:49`, com o bloco presente antes e
depois.** Isso **descarta** a hipótese que esta execução chegou a considerar — a de que o próprio Sync,
ou a purga de cache dele, reescreveria o `.htaccess` da raiz na mesma requisição em que a cura o repõe,
já que em 17/11 a cura das 10:15 e a rodada do Sync das 10:15:14 caíram **no mesmo minuto**. Não é
isso. É a 29.5 confirmada por medição nova: *"o EPC preserva o que encontra"*.

**A LEITURA CERTA, E É A DA 29.5(b):** o que se procura **é um evento, com hora, não um processo**.
Quatro apagamentos em cinco dias, com intervalos de **dias** e um de **~4 minutos** — isso é evento
irregular, não desgaste e não período. **A frase do chamado é "o arquivo é reescrito sem mão nossa, em
horários irregulares, e em 17/11 um deles veio ~4 minutos depois de uma reposição", e não "é reescrito
a cada poucos minutos".** Número de uma amostra lido como taxa é a família do número de tela digitado
da seção 8: parece medição e não mede o que diz.

**E O QUE A SÉRIE 2 NÃO RESPONDE, dito para ninguém procurar aqui:** ela não diz quanto a reposição das
11:15 durou **de fato** — a medição parou às 11h42:40Z com o bloco ainda de pé, e a execução fechou. O
limite inferior é 27min20s e não há limite superior medido.

```
hora_utc	tem_bloco	espera	sitemap	veiculos	sync_ultimo
11:15:55Z	True	3565	200	200	2026-11-17 11:09:54
11:16:13Z	True	3548	200	200	2026-11-17 11:09:54
11:16:29Z	True	3531	200	200	2026-11-17 11:09:54
11:16:46Z	True	3514	200	200	2026-11-17 11:09:54
11:17:04Z	True	3497	200	200	2026-11-17 11:09:54
11:17:21Z	True	3480	200	200	2026-11-17 11:09:54
11:17:37Z	True	3463	200	200	2026-11-17 11:09:54
11:17:54Z	True	3446	200	200	2026-11-17 11:09:54
11:18:11Z	True	3429	200	200	2026-11-17 11:09:54
11:18:28Z	True	3412	200	200	2026-11-17 11:09:54
11:18:45Z	True	3395	200	200	2026-11-17 11:09:54
11:19:02Z	True	3379	200	200	2026-11-17 11:09:54
11:19:18Z	True	3362	200	200	2026-11-17 11:09:54
11:19:36Z	True	3345	200	200	2026-11-17 11:09:54
11:19:53Z	True	3328	200	200	2026-11-17 11:09:54
11:20:10Z	True	3311	200	200	2026-11-17 11:09:54
11:20:26Z	True	3294	200	200	2026-11-17 11:09:54
11:20:43Z	True	3277	200	200	2026-11-17 11:09:54
11:21:00Z	True	3260	200	200	2026-11-17 11:09:54
11:21:17Z	True	3244	200	200	2026-11-17 11:09:54
11:21:33Z	True	3227	200	200	2026-11-17 11:09:54
11:21:50Z	True	3210	200	200	2026-11-17 11:09:54
11:22:08Z	True	3193	200	200	2026-11-17 11:09:54
11:22:25Z	True	3176	200	200	2026-11-17 11:09:54
11:22:41Z	True	3159	200	200	2026-11-17 11:09:54
11:22:58Z	True	3143	200	200	2026-11-17 11:09:54
11:23:15Z	True	3125	200	200	2026-11-17 11:09:54
11:23:32Z	True	3108	200	200	2026-11-17 11:09:54
11:23:49Z	True	3092	200	200	2026-11-17 11:09:54
11:24:05Z	True	3075	200	200	2026-11-17 11:09:54
11:24:22Z	True	3058	200	200	2026-11-17 11:09:54
11:24:39Z	True	3041	200	200	2026-11-17 11:09:54
11:24:56Z	True	3024	200	200	2026-11-17 11:09:54
11:25:13Z	True	3007	200	200	2026-11-17 11:09:54
11:25:30Z	True	2991	200	200	2026-11-17 11:09:54
11:25:47Z	True	2974	200	200	2026-11-17 11:09:54
11:26:04Z	True	2956	200	200	2026-11-17 11:09:54
11:26:21Z	True	2940	200	200	2026-11-17 11:09:54
11:26:37Z	True	2923	200	200	2026-11-17 11:09:54
11:26:54Z	True	2906	200	200	2026-11-17 11:09:54
11:27:11Z	True	2889	200	200	2026-11-17 11:09:54
11:27:28Z	True	2872	200	200	2026-11-17 11:09:54
11:27:45Z	True	2855	200	200	2026-11-17 11:09:54
11:28:02Z	True	2839	200	200	2026-11-17 11:09:54
11:28:19Z	True	2822	200	200	2026-11-17 11:09:54
11:28:36Z	True	2804	200	200	2026-11-17 11:09:54
11:28:53Z	True	2788	200	200	2026-11-17 11:09:54
11:29:09Z	True	2771	200	200	2026-11-17 11:09:54
11:29:26Z	True	2754	200	200	2026-11-17 11:09:54
11:29:43Z	True	2737	200	200	2026-11-17 11:09:54
11:30:01Z	True	2720	200	200	2026-11-17 11:09:54
11:30:17Z	True	2703	200	200	2026-11-17 11:09:54
11:30:34Z	True	2686	200	200	2026-11-17 11:09:54
11:30:51Z	True	2669	200	200	2026-11-17 11:09:54
11:31:08Z	True	2652	200	200	2026-11-17 11:09:54
11:31:32Z	True	2628	200	200	2026-11-17 11:09:54
11:31:49Z	True	2612	200	200	2026-11-17 11:09:54
11:32:06Z	True	2594	200	200	2026-11-17 11:09:54
11:32:23Z	True	2577	200	200	2026-11-17 11:09:54
11:32:40Z	True	2560	200	200	2026-11-17 11:09:54
11:32:57Z	True	2543	200	200	2026-11-17 11:09:54
11:33:14Z	True	2526	200	200	2026-11-17 11:09:54
11:33:31Z	True	2509	200	200	2026-11-17 11:09:54
11:33:48Z	True	2492	200	200	2026-11-17 11:09:54
11:34:05Z	True	2475	200	200	2026-11-17 11:09:54
11:34:22Z	True	2458	200	200	2026-11-17 11:09:54
11:34:40Z	True	2441	200	200	2026-11-17 11:09:54
11:34:57Z	True	2423	200	200	2026-11-17 11:09:54
11:35:14Z	True	2406	200	200	2026-11-17 11:09:54
11:35:31Z	True	2389	200	200	2026-11-17 11:09:54
11:35:48Z	True	2372	200	200	2026-11-17 11:09:54
11:36:05Z	True	2355	200	200	2026-11-17 11:09:54
11:36:23Z	True	2338	200	200	2026-11-17 11:09:54
11:36:40Z	True	2321	200	200	2026-11-17 11:09:54
11:36:57Z	True	2303	200	200	2026-11-17 11:09:54
11:37:14Z	True	2286	200	200	2026-11-17 11:09:54
11:37:31Z	True	2269	200	200	2026-11-17 11:09:54
11:37:48Z	True	2252	200	200	2026-11-17 11:09:54
11:38:05Z	True	2235	200	200	2026-11-17 11:09:54
11:38:23Z	True	2218	200	200	2026-11-17 11:09:54
11:38:40Z	True	2201	200	200	2026-11-17 11:09:54
11:38:57Z	True	2183	200	200	2026-11-17 11:09:54
11:39:14Z	True	2166	200	200	2026-11-17 11:09:54
11:39:31Z	True	2149	200	200	2026-11-17 11:09:54
11:39:48Z	True	2132	200	200	2026-11-17 11:39:49
11:40:05Z	True	2115	200	200	2026-11-17 11:39:49
11:40:22Z	True	2098	200	200	2026-11-17 11:39:49
11:40:39Z	True	2081	200	200	2026-11-17 11:39:49
11:40:56Z	True	2064	200	200	2026-11-17 11:39:49
11:41:13Z	True	2047	200	200	2026-11-17 11:39:49
11:41:30Z	True	2030	200	200	2026-11-17 11:39:49
11:41:48Z	True	2012	200	200	2026-11-17 11:39:49
11:42:05Z	True	1995	200	200	2026-11-17 11:39:49
11:42:23Z	True	1977	200	200	2026-11-17 11:39:49
11:42:40Z	True	1960	200	200	2026-11-17 11:39:49
11:42:57Z	True	1943	200	200	2026-11-17 11:39:49
11:43:14Z	True	1926	200	200	2026-11-17 11:39:49
11:43:31Z	True	1909	200	200	2026-11-17 11:39:49
```

---

## SÉRIE 3 — 13h18:33Z a 13h41:41Z, PELA EXECUÇÃO DAS 13h17Z, E ELA FECHA O LIMITE SUPERIOR QUE FALTAVA

A série 2 terminou às **11h43:31Z** com o bloco de pé e esta nota escrita ao lado: *"quanto a reposição
das 11:15 durou **de fato** — o limite inferior é 27min20s e **não há limite superior medido**"*.
Agora há, e ele é **muito maior**.

**50 leituras entre 13h18:33Z e 13h41:41Z, as 50 com o bloco PRESENTE e as 50 com `/wp-sitemap.xml` e
`/veiculos/` em 200.** `cura_liberada_em_s` em **0** nas 50 — a trava 2 vencida e livre, o que significa
que qualquer apagamento nesta janela teria sido curado na requisição seguinte, e nenhuma cura aconteceu.

**E O INTERVALO ENTRE AS DUAS SÉRIES (11h43:31Z a 13h18:33Z, 1h35m) ESTÁ COBERTO POR DEDUÇÃO, NÃO POR
LEITURA — e a dedução é fechada:**

1. A linha mais nova do log do `/status` seguia sendo a de **11:15**, lida às 13h19Z e de novo às
   13h40Z. O log vem do mais novo para o mais velho, então **nenhuma linha de cura nova rolou para fora**.
2. A trava 2 venceu às **12h15:20Z**. De lá até agora, **qualquer** apagamento seria curado na primeira
   requisição que chegasse ao PHP, e a cura **escreveria linha**.
3. E uma requisição chegou: o **Sync rodou às 13:16:20Z** (`ultimo` do `/status`). Logo o bloco estava
   presente naquele instante, e as 50 leituras a partir de 13h18:33Z o mediram presente desde então.
4. A única janela em que um apagamento ficaria escondido é **11h43:31Z–12h15:20Z**, com a trava queimada
   — mas um apagamento ali deixaria a porta no chão até a primeira requisição depois de 12h15:20Z, que
   então escreveria a linha. Ela não existe.

**A CONTA, E ELA É O NÚMERO NOVO DO CHAMADO: a reposição das 11:15:20Z sobreviveu pelo menos
2 h 26 min** — de 11h15:20Z a 13h41:41Z —, contra os **~4 minutos** do ciclo anterior (10:15→~10:19) e
os 27min20s que a série 2 conseguiu medir. **Três intervalos medidos na mesma raiz no mesmo dia:
~4 min, ≥27 min, ≥2 h 26 min.** Isso não é um processo com taxa: é um **evento irregular**, que é
exatamente o que a **29.5(b)** manda procurar e o que a errata das 11h43Z já havia corrigido. A série 3
é a terceira medição independente a dizer a mesma coisa.

**O QUE A SÉRIE 3 NÃO RESOLVE, e é por isso que a execução das 13h17Z escreveu a 14-c:** cada uma
destas três medições custou uma execução da Fundação sentada em cima da ilha, lendo de 25 em 25
segundos, e **só mede o intervalo em que alguém estava olhando**. O apagamento que cai dentro da hora
queimada da trava 2 não deixa rastro no log (a cura recusa calada, de propósito), e o log é uma janela
de 40 linhas que **rola**. Daí o contador da **seção 14-c** da casca (1.29.0, revisão 105, regra
**29.4-c** do `ARQUIPELAGO.md`): ele conta as quedas **sem** ninguém olhando, **sem** encher o log, e
**não rola**. Ele nasceu em **zero** às 13h40Z — e zero ali quer dizer "nenhuma queda desde que entrou
no ar", não "esta porta nunca caiu". As quedas anteriores a ele continuam em `dados/consertos.md`.

**A SÉRIE 3 LINHA POR LINHA** (hora UTC · bloco presente · segundos até a cura liberar ·  ·  ·  do Sync):

```
hora	tem_bloco	cura_s	sitemap	veiculos	sync_ultimo
13:18:33Z	True	0	200	200	2026-11-17 13:16:20
13:19:01Z	True	0	200	200	2026-11-17 13:16:20
13:19:29Z	True	0	200	200	2026-11-17 13:16:20
13:19:58Z	True	0	200	200	2026-11-17 13:16:20
13:20:27Z	True	0	200	200	2026-11-17 13:16:20
13:20:55Z	True	0	200	200	2026-11-17 13:16:20
13:21:24Z	True	0	200	200	2026-11-17 13:16:20
13:21:53Z	True	0	200	200	2026-11-17 13:16:20
13:22:21Z	True	0	200	200	2026-11-17 13:16:20
13:22:49Z	True	0	200	200	2026-11-17 13:16:20
13:23:17Z	True	0	200	200	2026-11-17 13:16:20
13:23:46Z	True	0	200	200	2026-11-17 13:16:20
13:24:14Z	True	0	200	200	2026-11-17 13:16:20
13:24:42Z	True	0	200	200	2026-11-17 13:16:20
13:25:11Z	True	0	200	200	2026-11-17 13:16:20
13:25:39Z	True	0	200	200	2026-11-17 13:16:20
13:26:07Z	True	0	200	200	2026-11-17 13:16:20
13:26:35Z	True	0	200	200	2026-11-17 13:16:20
13:27:04Z	True	0	200	200	2026-11-17 13:16:20
13:27:32Z	True	0	200	200	2026-11-17 13:16:20
13:28:01Z	True	0	200	200	2026-11-17 13:16:20
13:28:29Z	True	0	200	200	2026-11-17 13:16:20
13:28:58Z	True	0	200	200	2026-11-17 13:16:20
13:29:25Z	True	0	200	200	2026-11-17 13:16:20
13:29:54Z	True	0	200	200	2026-11-17 13:16:20
13:30:22Z	True	0	200	200	2026-11-17 13:16:20
13:30:50Z	True	0	200	200	2026-11-17 13:16:20
13:31:19Z	True	0	200	200	2026-11-17 13:16:20
13:31:47Z	True	0	200	200	2026-11-17 13:16:20
13:32:15Z	True	0	200	200	2026-11-17 13:16:20
13:32:43Z	True	0	200	200	2026-11-17 13:16:20
13:33:11Z	True	0	200	200	2026-11-17 13:16:20
13:33:39Z	True	0	200	200	2026-11-17 13:16:20
13:34:08Z	True	0	200	200	2026-11-17 13:16:20
13:34:35Z	True	0	200	200	2026-11-17 13:16:20
13:35:03Z	True	0	200	200	2026-11-17 13:16:20
13:35:32Z	True	0	200	200	2026-11-17 13:16:20
13:36:00Z	True	0	200	200	2026-11-17 13:16:20
13:36:28Z	True	0	200	200	2026-11-17 13:16:20
13:36:56Z	True	0	200	200	2026-11-17 13:16:20
13:37:25Z	True	0	200	200	2026-11-17 13:16:20
13:37:53Z	True	0	200	200	2026-11-17 13:16:20
13:38:21Z	True	0	200	200	2026-11-17 13:16:20
13:38:49Z	True	0	200	200	2026-11-17 13:16:20
13:39:18Z	True	0	200	200	2026-11-17 13:16:20
13:39:45Z	True	0	200	200	2026-11-17 13:39:48
13:40:14Z	True	0	200	200	2026-11-17 13:39:48
13:40:42Z	True	0	200	200	2026-11-17 13:39:48
13:41:13Z	True	0	200	200	2026-11-17 13:39:48
13:41:41Z	True	0	200	200	2026-11-17 13:39:48
13:42:09Z	True	0	200	200	2026-11-17 13:39:48
13:42:37Z	True	0	200	200	2026-11-17 13:39:48
13:43:05Z	True	0	200	200	2026-11-17 13:39:48
13:43:34Z	True	0	200	200	2026-11-17 13:39:48
13:44:02Z	True	0	200	200	2026-11-17 13:39:48
13:44:30Z	True	0	200	200	2026-11-17 13:39:48
13:44:58Z	True	0	200	200	2026-11-17 13:39:48
13:45:27Z	True	0	200	200	2026-11-17 13:39:48
```

**A SERIE 3 LINHA POR LINHA** (hora UTC, bloco presente, segundos ate a cura liberar, codigo de `/wp-sitemap.xml`, codigo de `/veiculos/`, `ultimo` do Sync):

```
hora	tem_bloco	cura_s	sitemap	veiculos	sync_ultimo
13:18:33Z	True	0	200	200	2026-11-17 13:16:20
13:19:01Z	True	0	200	200	2026-11-17 13:16:20
13:19:29Z	True	0	200	200	2026-11-17 13:16:20
13:19:58Z	True	0	200	200	2026-11-17 13:16:20
13:20:27Z	True	0	200	200	2026-11-17 13:16:20
13:20:55Z	True	0	200	200	2026-11-17 13:16:20
13:21:24Z	True	0	200	200	2026-11-17 13:16:20
13:21:53Z	True	0	200	200	2026-11-17 13:16:20
13:22:21Z	True	0	200	200	2026-11-17 13:16:20
13:22:49Z	True	0	200	200	2026-11-17 13:16:20
13:23:17Z	True	0	200	200	2026-11-17 13:16:20
13:23:46Z	True	0	200	200	2026-11-17 13:16:20
13:24:14Z	True	0	200	200	2026-11-17 13:16:20
13:24:42Z	True	0	200	200	2026-11-17 13:16:20
13:25:11Z	True	0	200	200	2026-11-17 13:16:20
13:25:39Z	True	0	200	200	2026-11-17 13:16:20
13:26:07Z	True	0	200	200	2026-11-17 13:16:20
13:26:35Z	True	0	200	200	2026-11-17 13:16:20
13:27:04Z	True	0	200	200	2026-11-17 13:16:20
13:27:32Z	True	0	200	200	2026-11-17 13:16:20
13:28:01Z	True	0	200	200	2026-11-17 13:16:20
13:28:29Z	True	0	200	200	2026-11-17 13:16:20
13:28:58Z	True	0	200	200	2026-11-17 13:16:20
13:29:25Z	True	0	200	200	2026-11-17 13:16:20
13:29:54Z	True	0	200	200	2026-11-17 13:16:20
13:30:22Z	True	0	200	200	2026-11-17 13:16:20
13:30:50Z	True	0	200	200	2026-11-17 13:16:20
13:31:19Z	True	0	200	200	2026-11-17 13:16:20
13:31:47Z	True	0	200	200	2026-11-17 13:16:20
13:32:15Z	True	0	200	200	2026-11-17 13:16:20
13:32:43Z	True	0	200	200	2026-11-17 13:16:20
13:33:11Z	True	0	200	200	2026-11-17 13:16:20
13:33:39Z	True	0	200	200	2026-11-17 13:16:20
13:34:08Z	True	0	200	200	2026-11-17 13:16:20
13:34:35Z	True	0	200	200	2026-11-17 13:16:20
13:35:03Z	True	0	200	200	2026-11-17 13:16:20
13:35:32Z	True	0	200	200	2026-11-17 13:16:20
13:36:00Z	True	0	200	200	2026-11-17 13:16:20
13:36:28Z	True	0	200	200	2026-11-17 13:16:20
13:36:56Z	True	0	200	200	2026-11-17 13:16:20
13:37:25Z	True	0	200	200	2026-11-17 13:16:20
13:37:53Z	True	0	200	200	2026-11-17 13:16:20
13:38:21Z	True	0	200	200	2026-11-17 13:16:20
13:38:49Z	True	0	200	200	2026-11-17 13:16:20
13:39:18Z	True	0	200	200	2026-11-17 13:16:20
13:39:45Z	True	0	200	200	2026-11-17 13:39:48
13:40:14Z	True	0	200	200	2026-11-17 13:39:48
13:40:42Z	True	0	200	200	2026-11-17 13:39:48
13:41:13Z	True	0	200	200	2026-11-17 13:39:48
13:41:41Z	True	0	200	200	2026-11-17 13:39:48
13:42:09Z	True	0	200	200	2026-11-17 13:39:48
13:42:37Z	True	0	200	200	2026-11-17 13:39:48
13:43:05Z	True	0	200	200	2026-11-17 13:39:48
13:43:34Z	True	0	200	200	2026-11-17 13:39:48
13:44:02Z	True	0	200	200	2026-11-17 13:39:48
13:44:30Z	True	0	200	200	2026-11-17 13:39:48
13:44:58Z	True	0	200	200	2026-11-17 13:39:48
13:45:27Z	True	0	200	200	2026-11-17 13:39:48
13:45:55Z	True	0	200	200	2026-11-17 13:39:48
```

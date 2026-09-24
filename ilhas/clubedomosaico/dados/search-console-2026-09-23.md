A conta de serviço não tem acesso a sc-domain:clubedomosaico.com.br. Propriedades visíveis: ['sc-domain:aquametria.com.br', 'sc-domain:robometria.com.br']

RESOLVIDO EM 24/09/2026, 15h BRT: o Raphael adicionou a conta de serviço `sentinela@arquipelago-508214.iam.gserviceaccount.com` na propriedade `sc-domain:clubedomosaico.com.br`, com permissão **Total** — o mesmo nível que ela já tem na aquametria e na robometria. Conferido na tela de Usuários e permissões da propriedade: 2 usuários, o Raphael como Proprietário e a sentinela como Total.

A permissão é Total e não Restrito de propósito: Restrito bastaria para o relatório de Desempenho, mas a API de Inspeção de URL exige usuário total, e a diferença só apareceria semanas depois, como erro estranho numa ronda.

O QUE ISSO MUDA, para quem for rodar a próxima leitura desta ilha: a leitura pela nuvem passa a ser possível. A linha de 23/09 em `dados/indexacao.md` e as de `dados/posicoes.md` foram medidas NO NAVEGADOR DO RAPHAEL e continuam válidas como estão — não reescreva nem "recalcule" nenhuma delas. A partir da leitura de 30/09, a fonte volta a ser a API, e a nota de rodapé sobre leitura manual deixa de valer para as linhas NOVAS.

AINDA NÃO FOI TESTADO NO AR: ninguém chamou a API para esta propriedade depois da mudança. A primeira leitura que rodar é quem prova. Se ela falhar com falta de permissão, o problema não é este cadastro — é propagação, e basta esperar e repetir.

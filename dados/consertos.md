# CONSERTOS DO ARQUIPÉLAGO

Um registro por conserto de defeito, em ordem cronológica. **Nunca sobrescrever
entrada antiga**: o valor deste arquivo é a série. Quem conserta escreve aqui a
data, o defeito (não o sintoma) e o que foi feito.

---

## 12/09/2026 — robometria: `robometria_casca_numeros()` servia número de fonte não publicada

**O DEFEITO, e ele era latente.** `robometria_casca_numeros()`, em
`ilhas/robometria/snippets/robometria-casca.php`, lia
`get_option('robometria_dados_casca-fatos')` direto, sem perguntar se o item que
gerou aquela option ainda tem `publicar: true` no manifest. O Sync **pula** o item
despublicado (`$pulados++` em `robometria-sync.php`) e **nunca apaga a option que
já gravou** — então bastava alguém virar `casca-fatos` para `publicar: false` para
a página seguir servindo aqueles números para sempre, com cara de medição e sem
página de origem viva.

É a mesma família do defeito que a própria ilha já pagou: até 11/09/2026 a seção 4
da metodologia servia números **digitados**, porque o caminho "derivado" lia a
option de `cobertura-r1`, que é `publicar: false` e nunca existiu no site. Aquele
estava registrado como "achado na fila, não corrigido" no `ESTADO.md` da ilha.

**O QUE FOI FEITO** (casca **1.4.1**):

1. Nasceu `robometria_casca_fonte_publicada( $id )`. Ela pergunta ao **próprio
   Sync**: existe `robometria_sync_estado['itens']['dados:<id>']['option']`? O Sync
   só escreve esse registro quando **aplica** o item, e ele só aplica
   `publicar: true` — logo o registro é a única prova, dentro do site, de que a
   fonte foi publicada.
2. `robometria_casca_numeros()` passou a exigir esse atestado antes de ler a
   option. Sem atestado devolve `array()` vazio, e os cinco lugares que a chamam já
   sabem dizer que a medição está fora do ar (`robometria_casca_sem_medicao_html()`,
   marcada com `rbm-sem-banco`). **Nenhum número de reserva foi criado** — valor de
   reserva seria mentira com cara de medição.
3. A bancada aprendeu o mesmo: `ferramentas/render-para-teste.php` agora grava o
   registro do Sync junto com cada option que carrega. Sem isso a bancada mediria um
   estado degradado que o site não tem — a cicatriz de "a bancada tem de servir o
   que o site serve".
4. Controle negativo em `ferramentas/teste-casca.php`: tirado o registro do Sync, a
   função tem de recusar mesmo com a option na mesa; devolvido o registro, os
   números voltam. Se essa afirmação passar a aprovar com a option sozinha, a trava
   caiu.

**Verificação:** `teste-casca` 152 verificações, `teste-r1` 90, `teste-r2` 90,
`teste-a1` 55, `teste-a2` 63, `teste-acentuacao` 17, `teste-arvore` 213,
`teste-voz` 155, `validar-banco` aprovado, `php -l` limpo nos cinco snippets.
Zero falha, **com uma exceção deliberada**: `teste-casca` reprova a seção 15
(`manifest 1.4.0 / snippet 1.4.1`), porque este conserto **não subiu o manifest**.
Subir a revisão arma o Sync, e publicar não é desta execução.

**LIMITE CONHECIDO, para ninguém confiar demais.** Depois que o Sync já aplicou o
item, o registro fica. Se `publicar` virar `false` mais tarde, o site não consegue
distinguir "não mudou" de "foi despublicado". Fechar esse resto exige o Sync gravar
o `publicar` de cada item — e o snippet do Sync **não viaja pelo manifest**, é
colado à mão no Code Snippets.

**FICA NA FILA, mesma família, não corrigido:**
`robometria_casca_niveis_no_banco()` lê a MESMA option `casca-fatos` e não passou
pelo portão — o despacho nomeou só `robometria_casca_numeros()`. Enquanto ela ficar
de fora, a coluna "temos hoje" da escada de fontes ainda pode sair de fonte
despublicada.

**PENDENTE DE DESEMBARQUE:** o conserto está no repositório e **não está no ar**.
Falta subir versão e sha no manifest (`ferramentas/atualizar-manifest.py`), acionar
o Sync e conferir a página de metodologia no navegador.

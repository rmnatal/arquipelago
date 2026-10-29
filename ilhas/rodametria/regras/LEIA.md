# `regras/` — o cérebro das ferramentas desta ilha

Aqui mora a **regra** de cada ferramenta: entrada → resposta inteira, já em frase
acentuada. O snippet PHP que vai ao ar é **tradutor** dela, frase a frase, como a
Robometria faz entre `cobertura-r1.py` e `robometria-r1.php`.

**Por que não em `ferramentas/`, e isto não é arrumação:** a `bancada.py` varre
`ferramentas/` e classifica tudo pela convenção de nome, denunciando o que não
casa com nenhuma — *"ou ele é portão e precisa do prefixo, ou não é e precisa
estar fora de `ferramentas/`"*. A referência **não é portão**: ela produz a
resposta, e portão que confere a própria produção é o teste que mede a si mesmo
da seção 8 do `ARQUIPELAGO.md`. Em 29/10/2026 a bancada denunciou
`ferramentas/f2-referencia.py` no dia em que ele nasceu, e esta pasta é a
segunda saída que ela mesma oferece.

**O que garante que o código daqui roda:** `ferramentas/gerar-f2.py` o importa e
a bancada roda o gerador com `--conferir` em toda passada — então regra que
quebrar reprova a bancada, mesmo morando fora de `ferramentas/`.

**Quem confere não importa daqui.** `ferramentas/teste-f2.py` reescreve a
aritmética à mão em `Fraction` e lê as constantes de `dados/constantes.json`:
é a regra da seção 8, *"quem confere escreve a própria régua, nunca chama a de
quem produziu o dado"*.

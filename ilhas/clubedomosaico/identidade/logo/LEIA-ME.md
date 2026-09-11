# Logo do Clube do Mosaico

## O estado de hoje (11/09/2026), em uma linha
O cabeçalho do site serve o **wordmark "clube do mosaico" em texto**, na tipografia da identidade (Outfit, vinho `#69030C`, minúsculas). A lótus **não** está no cabeçalho porque o arquivo dela está quebrado no repositório — leia abaixo.

## PENDÊNCIA COM O RAPHAEL: `lotus-512.png` está truncado
O arquivo tem 9.095 bytes, mas o chunk `IDAT` dele declara **11.638** — faltam **2.868 bytes**, e há um `IEND` colado no fim. Não é imagem cortada pela metade: o fluxo comprimido está corrompido desde o primeiro bloco e **não sai um único pixel** dele (`zlib` devolve "invalid code lengths set" na primeira tentativa, e o GD recusa o arquivo).

Medido em 11/09/2026 pela Fundação, ao ir cumprir o despacho que mandava usar exatamente este arquivo no cabeçalho claro.

**O que é preciso:** o Raphael reenviar a lótus em PNG com fundo transparente, pelo menos 512 px no menor lado, e commitar em `identidade/logo/lotus-512.png`. Depois disso:

```
php ferramentas/gerar-marca.php .
```

A ferramenta gera `lotus-80.png`, embute o base64 no snippet da casca entre os marcadores `MARCA-INICIO`/`MARCA-FIM`, e a lótus aparece sozinha ao lado do wordmark — **sem tocar em mais nada**. Ela **recusa** arquivo que não abre, que não tenha canal alfa ou cujos cantos não sejam transparentes: fundo sólido vira um retângulo colorido sobre o cabeçalho branco, e ícone quebrado no lugar do logo sumido seria trocar um defeito visível por outro.

## Os arquivos
- `favicon-32.png` — a lótus centralizada sobre branco, quadrada, **válida**. É ela que a casca embute como data URI no `<link rel="icon">`, gerada por `ferramentas/gerar-favicon.php`. Não redesenhar, não vetorizar, não trocar cores.
- `lotus-512.png` — o símbolo transparente. **QUEBRADO, ver acima.** Não apagar: ele é a evidência da pendência, e o teste da casca confere que a régua de PNG continua reconhecendo-o como quebrado.
- `lotus-80.png` — gerado por `gerar-marca.php` a partir do anterior. **Ainda não existe**, pelo mesmo motivo.

## O logo completo, e por que ele saiu do cabeçalho
`https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png` (lótus + wordmark, vinho sobre **preto**) está na biblioteca de mídia do site. Ele foi o logo do cabeçalho até a casca 1.1.0, e por causa dele o cabeçalho inteiro era preto — era a única cor em que ele aparecia.

Em 11/09/2026 o Raphael reprovou os dois de uma vez: *"muito ruim o fundo preto no header, o logo sumiu, queria algo mais clean"*. Sobre fundo claro esse arquivo vira um retângulo escuro, então ele **não volta ao cabeçalho**. Continua sendo o `logo` do `Organization` no JSON-LD, onde quem lê é o Google e não o olho de quem entra no site.

Quando chegar uma versão do logo completo **para fundo claro**, ela substitui o par lótus + wordmark do cabeçalho, e esta linha é reescrita.

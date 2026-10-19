#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DAS CONSTANTES DE SNIPPET.

    python3 ferramentas/mutacoes-constantes-de-snippet.py

Sem rede. Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

Copia o desenho do `mutacoes-teto-do-titulo.py`: cada mutacao quebra UMA
afirmacao de proposito, numa ILHA DE SOMBRA (o repositorio de verdade nunca e
tocado), e exige tres coisas — que o arquivo mude (alvo sumido e INERTE e
aparece nomeado), que o portao saia 1, e que ele reprove PELA FRASE esperada,
porque reprovar nao e a mesma coisa que reprovar pelo motivo certo.

A MUTACAO QUE MAIS IMPORTA E A DO MARCADOR: a exencao `REGUA PROPRIA` e a unica
porta pela qual um redigito pode passar de proposito, e porta que nao se testa e
porta escancarada. Se o marcador parar de ser conferido na LINHA e passar a
valer para o ARQUIVO, uma declaracao honesta no topo de um portao calaria todo
redigito dele para sempre — e ninguem seria avisado.

A SEGUNDA QUE MAIS IMPORTA E A DO `entre()` ESCAPADO, e ela guarda um conserto
desta mesma passada: a `onde()` do `regua-teto-do-titulo.py` contava aspa
ESCAPADA como se abrisse string, e por isso denunciava encenacao. A mutacao 13
desfaz esse conserto e tem de ser pega — sem ela, o conserto vale para hoje e
nao para a semana que vem.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-constantes-de-snippet.py")
REGUA_DO_TETO = os.path.join("ferramentas", "regua-teto-do-titulo.py")
PERGUNTADOR = os.path.join("ferramentas", "listar-constantes-do-snippet.php")
TESTE = os.path.join("ferramentas", "teste-constantes-de-snippet.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-const-")
    shutil.copytree(os.path.join(RAIZ, "ferramentas"), os.path.join(tmp, "ferramentas"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    # Os snippets entram porque a regua PERGUNTA a eles pelo PHP, e o `dados/`
    # entra porque os snippets o leem ao carregar. Sombra sem um dos dois
    # reprovaria por ausencia de arquivo, e ausencia lida como mutacao pega e
    # mutacao que nunca foi medida.
    shutil.copytree(os.path.join(RAIZ, "snippets"), os.path.join(tmp, "snippets"))
    shutil.copytree(os.path.join(RAIZ, "dados"), os.path.join(tmp, "dados"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE."""
    caminho = os.path.join(ilha, arquivo)
    texto = io.open(caminho, encoding="utf-8").read()
    if velho not in texto:
        return False
    with io.open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(velho, novo, 1))
    return True


def rodar_teste(ilha):
    p = subprocess.Popen([sys.executable, os.path.join(ilha, TESTE)],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def mutacao(rotulo, aplicar, frase):
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo == 0:
            print("  SOBREVIVEU  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        if frase not in saida:
            print("  SEM A FRASE  %s — esperava ouvir %r" % (rotulo, frase))
            sem_frase.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def mundo_que_passa(rotulo, aplicar):
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if aplicar is not None and not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo != 0:
            print("  REPROVOU MUNDO BOM  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def main():
    print("MUTACOES DO PORTAO DAS CONSTANTES DE SNIPPET — ilha de sombra, sem rede\n")

    # ---- 1 a 3: NENHUM CAMINHO DEVOLVE PADRAO ----
    mutacao(
        "1. a regua devolve uma lista de consolo em vez de levantar na resposta vazia",
        lambda i: troca_em(i, REGUA,
                           'if not (texto or "").strip():\n        raise RespostaInvalida("resposta vazia")',
                           'if not (texto or "").strip():\n        return {"constantes": {"AQUAMETRIA_X": {"valor": 1, "tipo": "numero"}}, "snippets_pulados": [], "snippets_lidos": []}'),
        "resposta vazia e invalida",
    )
    mutacao(
        "2. a regua aceita constante sem o campo tipo",
        lambda i: troca_em(i, REGUA,
                           'if not isinstance(campo, dict) or "valor" not in campo or "tipo" not in campo:',
                           'if False:'),
        "constante sem o campo tipo e invalida",
    )
    mutacao(
        "3. a regua aceita constante de fora do prefixo da ilha",
        lambda i: troca_em(i, REGUA,
                           "if not nome.startswith(PREFIXO):",
                           "if False:"),
        "constante fora do prefixo da ilha e invalida",
    )

    # ---- 4 a 6: A COMPARACAO DE VALOR ----
    mutacao(
        "4. numero passa a comparar como TEXTO, e 40.0 deixa de ser 40",
        lambda i: troca_em(i, REGUA,
                           "            return float(literal) == float(valor)",
                           '            return literal == ("%s" % valor)'),
        "40.0 e 40 e o mesmo valor",
    )
    mutacao(
        "5. o texto passa a comparar aparado, e ' – ' vira '–'",
        lambda i: troca_em(i, REGUA,
                           '    return literal == ("%s" % valor)\n\n\n# A atribuicao',
                           '    return literal.strip() == ("%s" % valor).strip()\n\n\n# A atribuicao'),
        "o separador SEM os espacos nao casa",
    )
    mutacao(
        "6. literal None passa a casar com qualquer coisa",
        lambda i: troca_em(i, REGUA,
                           "    if literal is None:\n        return False",
                           "    if literal is None:\n        return True"),
        "None nunca casa",
    )

    # ---- 7 a 9: OS TRES VEREDITOS ----
    mutacao(
        "7. prova FRACA com valor diferente passa a virar aviso",
        lambda i: troca_em(i, REGUA,
                           '                    elif forca == "forte":\n                        veredito = "HOMONIMO"',
                           '                    elif True:\n                        veredito = "HOMONIMO"'),
        "nome FRACO e valor diferente: nao e achado nenhum",
    )
    mutacao(
        "8. prova FRACA com valor IGUAL deixa de denunciar, e o teto escapa",
        lambda i: troca_em(i, REGUA,
                           "                    if igual:\n                        veredito = \"REDIGITADO\"",
                           "                    if igual and forca == \"forte\":\n                        veredito = \"REDIGITADO\""),
        "cauda FRACA com valor igual: DENUNCIA",
    )
    mutacao(
        "9. redigito em PROSA passa a reprovar",
        lambda i: troca_em(i, REGUA,
                           '                    if veredito == "REDIGITADO" and posicao == "codigo":',
                           '                    if veredito == "REDIGITADO":'),
        "redigito em PROSA nao denuncia",
    )

    # ---- 10 e 11: A EXENCAO, QUE E A UNICA PORTA ----
    mutacao(
        "10. o marcador REGUA PROPRIA deixa de ser conferido",
        lambda i: troca_em(i, REGUA,
                           "                if MARCADOR_DE_EXENCAO in linha:",
                           "                if False:"),
        "o marcador cala a denuncia",
    )
    mutacao(
        "11. o marcador passa a valer para o ARQUIVO e nao para a linha",
        lambda i: troca_em(i, REGUA,
                           "                if MARCADOR_DE_EXENCAO in linha:",
                           "                if MARCADOR_DE_EXENCAO in (arquivos[arquivo] or \"\"):"),
        "o marcador NAO cala a linha seguinte",
    )

    # ---- 12: O MUNDO ENCENADO ----
    mutacao(
        "12. mundo encenado dentro de aspas passa a ser lido como codigo",
        lambda i: troca_em(i, REGUA,
                           '                if posicao == "dado":\n                    continue',
                           '                if False:\n                    continue'),
        "mundo ENCENADO dentro de aspas e silencioso",
    )

    # ---- 13: O CONSERTO DA ASPA ESCAPADA, DESTA MESMA PASSADA ----
    mutacao(
        "13. o entre() volta a contar aspa ESCAPADA como se abrisse string",
        lambda i: troca_em(i, REGUA_DO_TETO,
                           '    limpa = RE_ESCAPADO.sub("\\x00\\x00", nua)',
                           "    limpa = nua"),
        "a sombra intocada passa",
    )

    # ---- 14 e 15: O NOME NAO CASA NO MEIO DE OUTRO ----
    mutacao(
        "14. o nome passa a casar dentro de outro nome",
        lambda i: troca_em(i, REGUA,
                           r'r"(?:^|[^0-9A-Za-z_$])(?P<nome>[A-Z][A-Z0-9_]{2,})\s*=\s*"',
                           r'r"(?P<nome>[A-Z][A-Z0-9_]{2,})\s*=\s*"'),
        "o nome nao casa no MEIO de outro nome",
    )
    mutacao(
        "15. cauda de um segmento passa a ser prova forte",
        lambda i: troca_em(i, REGUA,
                           '        forca = "forte" if len(partes) - i >= 2 else "fraca"',
                           '        forca = "forte"'),
        "SITE e cauda de um segmento e portanto prova FRACA",
    )

    # ---- 16: AS NAO PERGUNTADAS ----
    mutacao(
        "16. as constantes dos snippets pulados saem como ZERO em vez de NAO MEDIDAS",
        lambda i: troca_em(i, REGUA,
                           '    for nome in resposta.get("snippets_pulados") or []:',
                           "    for nome in []:"),
        "a saida diz NAO MEDIDAS, e nao zero",
    )

    # ---- 17: O --constante NAO INVENTA ----
    mutacao(
        "17. o --constante devolve vazio e sai 0 para constante que nao da para perguntar",
        lambda i: troca_em(i, REGUA,
                           "            raise SystemExit(1)\n        print(cs[qual][\"valor\"])",
                           "            print(\"\")\n            raise SystemExit(0)\n        print(cs[qual][\"valor\"])"),
        "constante de snippet PULADO sai 1 em vez de inventar",
    )

    # ---- 18: A VARREDURA NAO SE ISENTA DE GRACA ----
    mutacao(
        "18. a lista do que fica fora da varredura passa a ser vazia",
        lambda i: troca_em(i, REGUA,
                           'FORA_DA_VARREDURA = (PERGUNTADOR, "regua-constantes-de-snippet.py", "regua-teto-do-titulo.py")',
                           "FORA_DA_VARREDURA = ()"),
        "a propria regua esta fora da varredura",
    )

    # ---- 19: O PERGUNTADOR NAO INVENTA CONSTANTE ----
    # A 19 PRECISA DE DUAS TROCAS, e a primeira versao dela SOBREVIVEU por nao
    # ter a segunda: tirar a guarda do perguntador nao prova nada enquanto
    # houver constante para devolver, porque o ramo nunca roda. Entao ela
    # tambem cega o filtro de prefixo — e ai o perguntador devolve objeto vazio
    # de verdade, e quem tem de reprovar e a regua, do outro lado do processo.
    def sem_constante(i):
        return (troca_em(i, PERGUNTADOR, "if ( ! $constantes ) {", "if ( false ) {")
                and troca_em(i, PERGUNTADOR,
                             "if ( strpos( $nome, 'AQUAMETRIA_' ) !== 0 ) {",
                             "if ( strpos( $nome, 'NAO_EXISTE_ESTE_PREFIXO_' ) !== 0 ) {"))

    mutacao(
        "19. o perguntador devolve objeto vazio em vez de sair 1 sem constante nenhuma",
        sem_constante,
        "resposta sem constante nenhuma",
    )

    # ---- OS MUNDOS QUE TEM DE PASSAR ----
    print("")
    mundo_que_passa("o mundo de hoje passa, sem mutacao nenhuma", None)
    mundo_que_passa(
        "trocar o define de uma constante NAO reprova — ela e lida",
        lambda i: troca_em(i, os.path.join("snippets", "aquametria-calculadora-iluminacao.php"),
                           "define( 'AQUAMETRIA_C15_VITRINE_NIVEL', 'alta' )",
                           "define( 'AQUAMETRIA_C15_VITRINE_NIVEL', 'media' )"),
    )
    mundo_que_passa(
        "mexer num comentario da regua nao reprova nada",
        lambda i: troca_em(i, REGUA, "# A MARCA DA EXENCAO.", "# A marca da exencao (comentario mexido)."),
    )

    print("")
    print("%d mutacao(oes): %d sobrevivente(s), %d inerte(s), %d sem a frase"
          % (feitas, len(sobreviventes), len(inertes), len(sem_frase)))
    for rotulo in sobreviventes:
        print("  SOBREVIVEU/REPROVOU MUNDO BOM: %s" % rotulo)
    for rotulo in inertes:
        print("  INERTE: %s" % rotulo)
    for rotulo in sem_frase:
        print("  SEM A FRASE: %s" % rotulo)
    return 1 if (sobreviventes or inertes or sem_frase) else 0


if __name__ == "__main__":
    raise SystemExit(main())

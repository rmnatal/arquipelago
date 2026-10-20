#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DO CANO DE LINKS.

    python3 ferramentas/mutacoes-cano-de-links.py

Sem rede. Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

O QUE ELAS PROVAM, e por que o `teste-cano-de-links.py` nao basta sozinho: um
portao verde prova que o mundo de hoje passa, nunca que o portao MORDE. Cada
mutacao daqui quebra uma afirmacao de proposito, numa ILHA DE SOMBRA (copia de
`dados/` e `ferramentas/` num diretorio temporario — o repositorio de verdade
nunca e tocado), e exige TRES coisas:

  1. que o arquivo mude de verdade (mutacao que nao encontra o alvo e INERTE, e
     aparece nomeada em vez de contar como sucesso);
  2. que o teste saia com codigo 1;
  3. que ele reprove PELA FRASE que a mutacao espera ouvir de volta.

A (3) e a licao de 15/10/2026 desta ilha: reprovar nao e a mesma coisa que
reprovar PELO MOTIVO CERTO — sem a frase, uma mutacao pode disparar outra trava,
voltar verde e nunca ter medido a sua.

E DOIS MUNDOS TEM DE PASSAR, porque bateria que so sabe reprovar nao distingue
"o portao morde" de "o portao morde tudo".

A MUTACAO QUE MAIS IMPORTA AQUI E A 6: a declaracao por TOTAL em vez de item
por item. Ela e a volta ao desenho que esta ilha ja viu falhar um andar abaixo,
na serie da deriva — "74 linhas podem virar 74 OUTRAS linhas sem o total mudar"
— e ela tem de reprovar pelo caso da troca, nao pelo mundo de hoje.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-cano-de-links.py")
PORTAO = os.path.join("ferramentas", "conferir-cano-de-links.py")
CONTADOR = os.path.join("ferramentas", "contar-cano-de-links.py")
TESTE = os.path.join("ferramentas", "teste-cano-de-links.py")
BANCADA = os.path.join("ferramentas", "bancada.py")
# A GUARDA QUE A MUTACAO 15 MUTILA MUDOU DE ARQUIVO EM 20/10/2026, e esta linha
# e o conserto de uma mutacao que ficou INERTE por isso. A `bancada.py` deixou de
# ter as tres perguntas da classificacao (a classe passou a sair da POSICAO da
# marca, nao da presenca dela, pela `regua-classes-da-bancada.py`), e o filtro
# "quem carrega tem de ser PORTAO" foi com elas. A mutacao continua medindo a
# MESMA regra, no lugar onde ela mora agora — e quem a acusou foi a trava de
# alvo exato do `troca_em`, que recusa operar quando o texto a mutar nao esta
# mais la. E o corolario de higiene da secao 8 do contrato, cobrado na primeira
# vez em que teve chance.
REGUA_CLASSES = os.path.join("ferramentas", "regua-classes-da-bancada.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-cano-")
    for pasta in ("dados", "ferramentas"):
        shutil.copytree(os.path.join(RAIZ, pasta), os.path.join(tmp, pasta),
                        ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE.

    `str.replace` cru de alvo sumido NAO falha: ele devolve o mesmo texto e a
    mutacao vira verde sobre nada. Foi assim que quatro mutacoes de
    `mutacoes-escada.py` morreram caladas em 23/09/2026.
    """
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


print("MUNDOS QUE TEM DE PASSAR")
mundo_que_passa("1. a ilha como ela esta", None)
mundo_que_passa(
    "2. comentario trocado na regua (a bateria nao pode estar presa ao texto)",
    lambda ilha: troca_em(ilha, REGUA, "# -*- coding: utf-8 -*-",
                          "# -*- coding: utf-8 -*-\n# comentario novo, inofensivo"))

print("")
print("QUEBRAS QUE TEM DE REPROVAR")

# 3. O PISO DA 25.2 DEIXA DE SER CONTADO. Se `estado()` mentir que todo registro
# tem piso, o item sem `url_busca` desaparece da contagem e da serie.
mutacao("3. estado() diz que todo registro tem piso",
        lambda ilha: troca_em(ilha, REGUA,
                              '1 if af.get("url_busca") else 0,',
                              '1,'),
        "conta o registro sem piso")

# 4. A FICHA DEIXA DE SER CONTADA — o degrau que paga comissao.
mutacao("4. estado() diz que todo registro tem ficha",
        lambda ilha: troca_em(ilha, REGUA,
                              '1 if af.get("url_produto") else 0,',
                              '1,'),
        "conta os registros sem ficha")

# 5. O DEGRAU SAI DA FRASE DE ESTADO. Registro que desce de degrau (link que
# morreu) passaria a mudar em silencio.
mutacao("5. o degrau sai da frase de estado",
        lambda ilha: troca_em(ilha, REGUA,
                              '"-" if degrau is None else degrau,',
                              '"-",'),
        "agrupa por degrau")

# 6. A DECLARACAO VOLTA A SER POR TOTAL. A mutacao que esta ilha ja viu falhar
# um andar abaixo: com o total no lugar dos itens, a troca de estado entre dois
# registros fica VERDE.
mutacao("6. a comparacao passa a ser pelo total, nao item por item",
        lambda ilha: troca_em(
            ilha, REGUA,
            '    novos = sorted(set(itens) - set(esperado))',
            '    if len(itens) == len(esperado):\n'
            '        return ([], [], [])\n'
            '    novos = sorted(set(itens) - set(esperado))'),
        "a comparacao item por item acusa as duas mudancas")

# 7. O VERDE VAZIO RESSUSCITA: a regua passa a nao achar banco nenhum, e "0 sem
# piso" vira a leitura de um cano inteiro. E a afirmacao que o portao faz
# PRIMEIRO de proposito.
mutacao("7. bancos() deixa de achar os bancos (o verde vazio)",
        lambda ilha: troca_em(ilha, REGUA,
                              'os.path.join(raiz, "dados", "produtos-*.json")',
                              'os.path.join(raiz, "dados", "produtos-nenhum-*.json")'),
        "conta os registros dos dois bancos")

# 8. O CONTADOR VOLTA A CONTAR SOZINHO. A afirmacao estrutural da metade (B): a
# segunda copia da aritmetica ressuscitando, que e o passo que esta passada
# existiu para tirar. Ela nao se pega por comportamento — hoje as duas copias
# dariam o mesmo numero.
mutacao("8. o contador volta a ter contagem propria (json.load dentro dele)",
        lambda ilha: troca_em(ilha, CONTADOR,
                              "import datetime",
                              "import datetime\nimport json  # json.load"),
        "o contador nao abre banco nenhum por conta propria")

# 9. O PORTAO DEIXA DE PERGUNTAR QUAIS BANCOS FORAM LIDOS.
mutacao("9. o portao para de perguntar quais bancos foram lidos",
        lambda ilha: troca_em(ilha, PORTAO,
                              "existentes = [os.path.basename(c) for c in regua.bancos(RAIZ)]",
                              "existentes = list(contagem['bancos'])"),
        "o portao pergunta a regua QUAIS bancos foram lidos")

# 10. O PORTAO PARA DE COMPARAR COM A DECLARACAO.
mutacao("10. o portao para de comparar com a declaracao",
        lambda ilha: troca_em(
            ilha, PORTAO,
            "    novos, sumidos, mudados = regua.comparar_com_declaracao(contagem[\"itens\"], declarado)",
            "    novos, sumidos, mudados = ([], [], [])"),
        "REPROVA o portao")

# 11. O TOTAL DIGITADO VOLTA A MANDAR: o portao para de conferir se a declaracao
# fecha com os proprios itens.
mutacao("11. o portao aceita total declarado que nao fecha com os itens",
        lambda ilha: troca_em(
            ilha, PORTAO,
            '           declarado.get("totais") == regua.totais(declarados)\n'
            '           and declarado.get("degraus") == regua.degraus(declarados),',
            '           True,'),
        "total declarado que nao fecha com os itens declarados REPROVA")

# 12. A DECLARACAO AUSENTE PASSA A SER LIDA COMO CANO VAZIO. E a mesma familia
# do "nao medido lido como zero" que esta fabrica paga caro — aqui, serie que
# nunca foi escrita passando por cano declarado.
mutacao("12. declaracao ausente passa a ser lida como cano vazio",
        lambda ilha: troca_em(ilha, REGUA,
                              '    if declarado is None:\n'
                              '        return (["a serie nao tem declaracao nenhuma"], [], [])',
                              '    if declarado is None:\n'
                              '        return ([], [], [])'),
        "declaracao ausente nao se le como cano vazio")

# 13. A IDENTIDADE DO ITEM PERDE O BANCO. Dois registros de mesmo id em bancos
# diferentes passariam a ser um so na serie — e um deles sumiria da contagem sem
# nada acusar.
mutacao("13. a identidade do item perde o nome do banco",
        lambda ilha: troca_em(ilha, REGUA,
                              'return "%s/%s" % (curto, item.get("id"))',
                              'return "%s" % item.get("id")'),
        "a identidade do item traz o banco e o id")

# 14. A SERIE PASSA A SER SOBRESCRITA em vez de crescer por cima. A serie so
# vale porque cresce: sobrescrita, ela deixa de dizer como o cano andou.
mutacao("14. a serie passa a ser sobrescrita em vez de crescer por cima",
        lambda ilha: troca_em(
            ilha, PORTAO,
            "    if os.path.exists(SERIE):\n        antigo = regua.ler(SERIE)",
            "    if False:\n        antigo = regua.ler(SERIE)"),
        "a serie cresceu por cima")

# 15. A BANCADA VOLTA A ACEITAR QUALQUER ARQUIVO COMO EXERCICIO DA REGUA. A
# regra que apagou a denuncia deste cano em 19/10/2026 e "contar- e producao SE
# um PORTAO carregar a conta dele". Sem o filtro, o proprio contador citando a
# propria regua basta — e a denuncia passa a calar sempre, que e pior que nao
# existir.
mutacao("15. a bancada volta a aceitar qualquer arquivo como exercicio da regua",
        lambda ilha: troca_em(ilha, REGUA_CLASSES,
                              "        if not E_PORTAO.match(outro):\n"
                              "            continue\n"
                              "        if e_ato_de_codigo(arquivos[outro], nome):\n",
                              "        if e_ato_de_codigo(arquivos[outro], nome):\n"),
        "CONTINUA denunciado")

print("")
print("=" * 68)
ruins = len(sobreviventes) + len(sem_frase) + len(inertes)
if ruins:
    print("REPROVADO: %d de %d mutacoes nao foram pegas como deviam" % (ruins, feitas))
    for r in sobreviventes:
        print("  SOBREVIVEU: %s" % r)
    for r in sem_frase:
        print("  SEM A FRASE: %s" % r)
    for r in inertes:
        print("  INERTE: %s" % r)
    sys.exit(1)
print("%d de %d mutacoes reprovadas pelo portao, zero inerte" % (feitas - 2, feitas))
sys.exit(0)

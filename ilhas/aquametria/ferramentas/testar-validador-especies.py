#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testes NEGATIVOS do validador do banco de especies.

Uso (a partir de ilhas/aquametria/):  python3 ferramentas/testar-validador-especies.py

Por que existe: validar-especies.py so prova que o banco de hoje passa. Isso nao prova
que uma regra pega o defeito que ela promete pegar — uma regra escrita errada aprova
tudo em silencio, e o banco parece so. Cada teste aqui corrompe uma copia do banco de
proposito, roda o validador contra a copia e exige que a regra certa reprove. O banco
real nunca e tocado: as copias vao para um diretorio temporario.

Codigo de saida: 0 se todas as regras reprovarem o que deviam, 1 se alguma passar batido.
"""

import copy
import json
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
VALIDADOR = os.path.join(RAIZ, "ferramentas", "validar-especies.py")


def pega(banco, rid):
    for r in banco["especies"]:
        if r["id"] == rid:
            return r
    raise KeyError(rid)


# ------------------------------------------------------------------ as corrupcoes
def c_e1(b):
    pega(b, "danio-rerio")["id"] = "peixe-zebra"


def c_e2(b):
    r = pega(b, "danio-rerio")
    r["convivencia"] = None
    r["status_registro"] = "conflito"


def c_e3(b):
    r = pega(b, "corydoras-panda")
    for f in r["fontes"]:
        if "temperatura_C" in f["campos"]:
            f["campos"].remove("temperatura_C")


def c_e4(b):
    pega(b, "betta-splendens")["fontes"][0]["status"] = "verificada-fabricante"


def c_e5(b):
    r = pega(b, "xiphophorus-hellerii")
    for f in r["fontes"]:
        f["origem"] = "varejo"
        f["status"] = "transcrita-varejo"


def c_e6(b):
    pega(b, "astronotus-ocellatus")["porte_medida"] = None


def c_e7(b):
    r = pega(b, "corydoras-panda")
    # base 45 x 30 cm x 30 cm de altura = 40,5 L: litro derivado, gravado a mao
    r["volume_minimo_declarado_L"] = 40.5
    r["fontes"][1]["campos"].append("volume_minimo_declarado_L")


def c_e8(b):
    pega(b, "hemigrammus-erythrozonus")["temperatura_C"] = {"min": 28, "max": 24}


def c_e9(b):
    # conflito de bem-estar cujo conservador nao e o maior
    pega(b, "chromobotia-macracanthus")["conflitos"][0]["valor_conservador"] = 150


def c_e10(b):
    pega(b, "hemigrammus-rhodostomus")["status_registro"] = "completo"


def c_e11(b):
    pega(b, "betta-splendens")["verificado_em"] = "2020-01-01"


def c_e12(b):
    r = pega(b, "astronotus-ocellatus")
    r["cardume_minimo"] = 4  # solitario com cardume preenchido


def c_e18_sem_piso(b):
    r = pega(b, "astronotus-ocellatus")   # solitario, cardume_minimo null
    r["cardume_recomendado_ate"] = 6


def c_e18_invertida(b):
    r = pega(b, "trichogaster-chuna")
    r["cardume_recomendado_ate"] = r["cardume_minimo"]


def c_e13(b):
    r = pega(b, "trichopodus-trichopterus")
    r["temperatura_C"] = {"min": 5, "max": 35}
    r["temperatura_e_tolerancia"] = False


def c_e14(b):
    r = pega(b, "mikrogeophagus-ramirezi")
    r["fontes"] = [r["fontes"][0]]


def c_e15(b):
    # troca o compendio por um espelho do MESMO corpo: duas urls, uma fonte so
    r = pega(b, "corydoras-panda")
    r["fontes"][1]["origem"] = "base-cientifica-via-busca"
    r["fontes"][1]["status"] = "base-cientifica-via-busca"
    r["fontes"][1]["url"] = "https://fishbase.org/summary/12188"


def c_e16_numero(b):
    # o campo passa a dizer um numero que a fonte citada nao diz
    pega(b, "tanichthys-albonubes")["cardume_minimo"] = 12


def c_e16_intervalo(b):
    # um lado do intervalo mexido: a regra tem de olhar min e max separados
    pega(b, "hyphessobrycon-amandae")["temperatura_C"]["max"] = 29


def c_e16_base(b):
    # e dentro do objeto de base tambem, que e onde mora a largura
    pega(b, "hyphessobrycon-amandae")["base_minima_cm"]["largura"] = 35


def c_e17_acento(b):
    # nome de tela sem acento. E o defeito que ficou tres levas no ar porque as
    # tres primeiras fichas eram nomes que o portugues nao acentua.
    pega(b, "hemigrammus-rhodostomus")["nomes_populares_br"][0] = "rodostomo"


def c_e17_acento_no_meio(b):
    # e nao so na primeira palavra, nem so no nome que a ficha usa como titulo:
    # a tabela de companheiros imprime o [0] de TODAS as especies do catalogo, e
    # o token errado pode estar depois de um hifen ou de um espaco.
    pega(b, "astronotus-ocellatus")["nomes_populares_br"][2] = "acara-acu"


def c_e17_acento_token_solto(b):
    # token separado por ESPACO, para provar que a regra nao olha so o hifen
    pega(b, "trichopodus-leerii")["nomes_populares_br"][0] = "gurami perola"


def c_e16_extenso(b):
    # a fonte da coridora-panda escreve "pelo menos SEIS", por extenso. Trocar o campo
    # para 7 tem de reprovar — e o 6 continuar passando e o que prova que a leitura
    # por extenso e real, e nao um buraco que aprova qualquer numero.
    pega(b, "corydoras-panda")["cardume_minimo"] = 7


# --- E19: a coleta recusada (22/09/2026) -----------------------------------
# O disco e o unico registro do banco com `coletas_recusadas` hoje, e e nele que
# estas quatro corrupcoes pegam. A quarta e a que importa: a recusa e o dado
# dizendo coisas contrarias sobre o mesmo campo, que e o estado em que a proxima
# execucao grava o numero e ninguem descobre que ele foi recusado antes.
def c_e19_sem_motivo(b):
    pega(b, "symphysodon-aequifasciatus")["coletas_recusadas"][0]["motivo"] = ""


def c_e19_campo_inventado(b):
    pega(b, "symphysodon-aequifasciatus")["coletas_recusadas"][0]["campos_pretendidos"] = ["tamanho_do_peixe"]


def c_e19_data_no_futuro(b):
    pega(b, "symphysodon-aequifasciatus")["coletas_recusadas"][0]["em"] = "2099-01-01"


def c_e19_campo_recusado_preenchido(b):
    """A base do disco entrou em 22/09/2026, e com ela superada_em/superada_por.

    Ate aquela data a corrupcao era PREENCHER o campo recusado; hoje ele esta
    preenchido de direito, e o que a regra tem de pegar e a metade que sobrou:
    recusa e dado dizendo coisas contrarias porque alguem apagou a superacao.
    """
    c = pega(b, "symphysodon-aequifasciatus")["coletas_recusadas"][0]
    c.pop("superada_em", None)
    c.pop("superada_por", None)


# ---- o chao declarado e a populacao para quem ele foi declarado (esquema versao 5)
def c_e20_sem_chao(b):
    del pega(b, "apistogramma-agassizii")["chao_declarado_para"]


def c_e20_chao_sem_base(b):
    r = pega(b, "poecilia-reticulata")
    r["chao_declarado_para"] = {"arranjos": ["grupo"], "frase": "grupo"}


def c_e20_mistura_nao_declarado(b):
    pega(b, "paracheirodon-innesi")["chao_declarado_para"]["arranjos"] = ["nao-declarado", "casal"]


def c_e20_arranjo_fora_do_vocabulario(b):
    pega(b, "corydoras-panda")["chao_declarado_para"]["arranjos"] = ["cardume-grande"]


def c_e22_frase_inventada(b):
    pega(b, "apistogramma-agassizii")["chao_declarado_para"]["frase"] = (
        "base de 60 x 30 cm aceitavel para o harem")


def c_e22_termo_sem_palavra(b):
    """A clausula do compendio diz UM CASAL; o termo diz grupo."""
    pega(b, "apistogramma-agassizii")["chao_declarado_para"]["arranjos"] = ["grupo"]


def c_e22_nao_declarado_que_nomeia(b):
    """'nao-declarado' e o termo PERMISSIVO: e o que devolve o fundo a ficha.

    Por isso ele e conferido pelo avesso — a clausula do panda nomeia um grupo
    pequeno, e dizer que ela nao nomeia ninguem e o palpite mais caro do campo.
    """
    pega(b, "corydoras-panda")["chao_declarado_para"]["arranjos"] = ["nao-declarado"]


def c_e21_arranjo_acima_do_chao(b):
    """O chao do gurami-anao foi declarado para UM CASAL; o registro passa a
    publicar harem, que e varios peixes. E o defeito do apistogramma agassizi,
    que esteve oito dias no ar."""
    pega(b, "trichogaster-lalius")["convivencia"] = "harem"


def c_e23_frase_inventada(b):
    """A clausula da recusa reescrita: a fonte do barbo sumatra escreveu outra coisa."""
    pega(b, "puntigrus-tetrazona")["restricoes_de_companhia"][0]["frase"] = (
        "nao manter junto de peixe de nadadeira comprida")


def c_e23_tipo_fora_do_vocabulario(b):
    pega(b, "puntigrus-tetrazona")["restricoes_de_companhia"][0]["tipo"] = "peixe-lento"


def c_e23_tipo_sem_palavra(b):
    """A clausula do papilocromis fala de aquario comunitario; o tipo diz nadadeira.

    E a metade que separa esta regra de "existe uma frase la": sem ela, qualquer
    clausula literal sustentaria qualquer tipo, e a traducao na tela falaria de uma
    coisa que a fonte nunca disse.
    """
    pega(b, "mikrogeophagus-altispinosus")["restricoes_de_companhia"][0]["tipo"] = "nadadeiras-longas"


def c_e23_lista_vazia(b):
    """Lista vazia afirma "a fonte foi lida e nao recusou ninguem", e isso se
    escreve deixando o campo fora."""
    pega(b, "puntius-titteya")["restricoes_de_companhia"] = []


def c_e23_sem_fonte_que_declare(b):
    """A clausula continua literal, e nenhuma fonte declara o campo em `campos`.

    E o caso em que a frase existe e a atribuicao nao: a pagina publicaria a recusa
    sem dono, que e opiniao de forum com cara de dado.
    """
    r = pega(b, "puntigrus-tetrazona")
    for f in r["fontes"]:
        if "restricoes_de_companhia" in f.get("campos", []):
            f["campos"].remove("restricoes_de_companhia")


def c_e24_frase_inventada(b):
    """A clausula do maximo reescrita: a fonte do barbo rosado escreveu outra coisa."""
    pega(b, "pethia-conchonius")["porte_e_maximo_registrado"]["frase"] = (
        "FishBase - ficha da especie: comprimento maximo de 14,0 cm TL")


def c_e24_clausula_sem_palavra_de_maximo(b):
    """A clausula e literal e NAO diz que o numero e maximo.

    E a metade que separa esta regra de "existe uma frase la". A clausula abaixo
    esta na transcricao do peixe-espada palavra por palavra e e exatamente o tipo
    de frase dos TRES registros que ficam sem o campo de proposito: ela traz o
    numero e nao o qualifica. Sem esta metade, o campo afirmaria "maximo
    registrado" sobre uma fonte que nunca usou a palavra.
    """
    r = pega(b, "xiphophorus-hellerii")
    r["porte_e_maximo_registrado"] = {"frase": "macho ate 14,0 cm TL e femea ate 16,0 cm TL"}
    for f in r["fontes"]:
        if "porte_adulto_cm" in f.get("campos", []):
            f["campos"].append("porte_e_maximo_registrado")


def c_e24_clausula_de_maximo_de_outra_coisa(b):
    """A clausula diz "maximo" e fala de OUTRA coisa — a profundidade da lagoa.

    Este e o caso que fez a regra pedir DUAS coisas em vez de uma, e ele nao foi
    inventado para o teste: a transcricao do danio-margaritatus traz, literalmente,
    "habita lagoas rasas de no maximo 30 cm de profundidade". Com a palavra
    sozinha bastando, o campo passaria a dizer que o porte do peixe e um maximo
    citando uma frase sobre a agua em que ele vive.
    """
    pega(b, "danio-margaritatus")["porte_e_maximo_registrado"]["frase"] = (
        "habita lagoas rasas de no maximo 30 cm de profundidade")


def c_e24_sem_fonte_que_declare(b):
    """A clausula continua literal, e nenhuma fonte declara o campo em `campos`.

    O caso em que a frase existe e a atribuicao nao: a pagina publicaria o escopo
    do numero sem dono. O mesmo defeito do E23, e o mesmo conserto.
    """
    r = pega(b, "pethia-conchonius")
    for f in r["fontes"]:
        if "porte_e_maximo_registrado" in f.get("campos", []):
            f["campos"].remove("porte_e_maximo_registrado")


def c_e24_comum_que_alcanca_o_maximo(b):
    """O tamanho comum igual ao maximo: a aritmetica do E18 um andar acima.

    75 mm sao 7,5 cm, e o maximo do barbo cereja e 5,0 cm. Tamanho comum que passa
    do maximo nao e tamanho comum — e numero trocado de lugar, e a pagina
    publicaria que a maioria dos adultos e maior que o maior ja registrado.
    """
    pega(b, "puntius-titteya")["porte_e_maximo_registrado"]["comum"]["de"] = 7.5


def c_e24_comum_com_unidade_que_a_clausula_nao_usa(b):
    """A unidade convertida na digitacao: a clausula diz cm e o campo diz mm.

    Converter ao digitar tira o numero do campo do texto da fonte — e e o E16 que
    deixaria de conferir, em silencio, o unico par de numeros que ninguem conferia
    antes da versao 7.

    O ALVO E O xiphophorus-variatus E A ESCOLHA E A METADE QUE FAZ O TESTE VALER.
    A primeira escrita deste caso corrompia o barbo rosado (mm -> cm) e PASSAVA
    POR OUTRA REGRA: 65 "cm" alcancam o maximo de 14,0 cm, entao a linha de erro
    saia pela conta do comum e nao pela unidade — e a mutacao que desligava a
    unidade SOBREVIVEU, em 15/10/2026, dizendo isso. Aqui 3,9 mm sao 0,39 cm,
    bem abaixo do maximo de 7,0, e a unica regra que pode reprovar e a que o
    teste existe para medir. Corrupcao que dispara duas regras nao mede nenhuma.
    """
    pega(b, "xiphophorus-variatus")["porte_e_maximo_registrado"]["comum"]["unidade"] = "mm"


def c_e24_comum_faixa_invertida(b):
    """Teto que nao passa do piso nao e faixa (a mesma frase do E18)."""
    pega(b, "pethia-conchonius")["porte_e_maximo_registrado"]["comum"]["ate"] = 65


def c_e24_comum_frase_inventada(b):
    """O numero do tamanho comum com clausula que a fonte nao escreveu."""
    pega(b, "pethia-conchonius")["porte_e_maximo_registrado"]["comum"]["frase"] = (
        "a maioria dos adultos esta entre 65 e 75 mm")


def c_e16_comum_numero(b):
    """O numero do comum fora do texto da fonte — e um nivel ABAIXO do que o E16 via.

    Enquanto valores_numericos olhava um nivel so, este defeito passava batido: o
    `comum` e objeto dentro de objeto. Portao que nao chega aprova por falta de
    evidencia, e este teste e o que prova que ele passou a chegar.
    """
    pega(b, "puntius-titteya")["porte_e_maximo_registrado"]["comum"]["de"] = 2.7


def c_e25_duas_reguas(b):
    """O comum numa regua DECLARADA e diferente da do maximo.

    O barbo cereja e o registro em que o aviso hoje CALA, e com razao: a fonte
    declara os dois lados em TL, entao os dois numeros se comparam. Trocar o comum
    para SL poe as duas medidas em reguas diferentes sem nenhum campo ficar vazio —
    e e o caso que prova que o E25 mede a DIVERGENCIA de regua, e nao apenas a
    ausencia dela. Sem esta metade, o aviso pegaria o `null` do barbo rosado e
    deixaria passar o par SL/TL, que e o erro de leitura que a leva 7 mediu em 20 %
    para peixe de cauda longa.
    """
    pega(b, "puntius-titteya")["porte_e_maximo_registrado"]["comum"]["medida"] = "SL"


TESTES = [
    ("E1", "id que nao corresponde ao nome cientifico", c_e1, "erro"),
    ("E24", "clausula do maximo que a fonte nao escreveu", c_e24_frase_inventada, "erro",
     "pethia-conchonius"),
    ("E24", "clausula literal que nao diz que o numero e maximo",
     c_e24_clausula_sem_palavra_de_maximo, "erro", "xiphophorus-hellerii"),
    ("E24", "clausula de maximo que fala de outra coisa (a lagoa, nao o peixe)",
     c_e24_clausula_de_maximo_de_outra_coisa, "erro", "danio-margaritatus"),
    ("E24", "escopo sem fonte que o declare em campos", c_e24_sem_fonte_que_declare, "erro",
     "pethia-conchonius"),
    ("E24", "tamanho comum que alcanca o porte maximo", c_e24_comum_que_alcanca_o_maximo, "erro",
     "puntius-titteya"),
    ("E24", "unidade do comum convertida na digitacao",
     c_e24_comum_com_unidade_que_a_clausula_nao_usa, "erro", "xiphophorus-variatus"),
    ("E24", "faixa do comum invertida: teto igual ao piso", c_e24_comum_faixa_invertida, "erro",
     "pethia-conchonius"),
    ("E24", "clausula do tamanho comum que a fonte nao escreveu", c_e24_comum_frase_inventada, "erro",
     "pethia-conchonius"),
    ("E16", "numero do comum (objeto dentro de objeto) fora do texto da fonte",
     c_e16_comum_numero, "erro", "puntius-titteya"),
    ("E25", "maximo e comum em reguas declaradas diferentes", c_e25_duas_reguas, "aviso",
     "puntius-titteya"),
    ("E20", "base dos dois lados sem chao_declarado_para", c_e20_sem_chao, "erro"),
    ("E20", "chao_declarado_para sem base dos dois lados", c_e20_chao_sem_base, "erro"),
    ("E20", "'nao-declarado' misturado com outro termo", c_e20_mistura_nao_declarado, "erro"),
    ("E20", "arranjo fora do vocabulario fechado", c_e20_arranjo_fora_do_vocabulario, "erro"),
    ("E22", "frase do chao que a fonte nao escreveu", c_e22_frase_inventada, "erro"),
    ("E22", "termo que a clausula da fonte nao sustenta", c_e22_termo_sem_palavra, "erro"),
    ("E22", "'nao-declarado' com clausula que nomeia populacao", c_e22_nao_declarado_que_nomeia, "erro"),
    ("E21", "arranjo publicado acima do chao declarado", c_e21_arranjo_acima_do_chao, "aviso"),
    ("E23", "clausula da recusa que a fonte nao escreveu", c_e23_frase_inventada, "erro"),
    ("E23", "tipo de restricao fora do vocabulario fechado", c_e23_tipo_fora_do_vocabulario, "erro"),
    ("E23", "tipo que a clausula da fonte nao sustenta", c_e23_tipo_sem_palavra, "erro"),
    ("E23", "lista de restricoes presente e vazia", c_e23_lista_vazia, "erro"),
    ("E23", "recusa sem fonte que a declare em campos", c_e23_sem_fonte_que_declare, "erro"),
    ("E2", "campo obrigatorio faltando sem status parcial", c_e2, "erro"),
    ("E3", "campo tecnico preenchido sem fonte", c_e3, "erro"),
    ("E4", "fonte com status incoerente com a origem", c_e4, "erro"),
    ("E5", "campo de manutencao sustentado so por varejo", c_e5, "erro"),
    ("E6", "porte sem SL ou TL do lado", c_e6, "erro"),
    ("E7", "litro derivado da base gravado a mao", c_e7, "erro"),
    ("E8", "intervalo com min maior que max", c_e8, "erro"),
    ("E9", "conflito de bem-estar com conservador que nao e o maior", c_e9, "erro"),
    ("E10", "conflito declarado com status completo", c_e10, "erro"),
    ("E11", "registro verificado ha mais de 365 dias", c_e11, "aviso"),
    ("E12", "convivencia solitario com cardume_minimo preenchido", c_e12, "erro"),
    ("E13", "tolerancia termica disfarcada de recomendacao", c_e13, "erro"),
    ("E14", "status completo com um corpo de fonte so", c_e14, "erro"),
    ("E15", "duas urls do mesmo corpo passando por duas fontes", c_e15, "aviso"),
    ("E16", "campo com numero que a fonte citada nao diz", c_e16_numero, "erro"),
    ("E16", "um lado do intervalo fora do texto da fonte", c_e16_intervalo, "erro"),
    ("E16", "largura da base fora do texto da fonte", c_e16_base, "erro"),
    ("E16", "numero por extenso na fonte, campo trocado", c_e16_extenso, "erro"),
    ("E18", "teto de faixa sem piso: cardume_recomendado_ate sem cardume_minimo", c_e18_sem_piso, "erro"),
    ("E18", "faixa invertida: teto igual ao piso", c_e18_invertida, "erro"),
    ("E19", "coleta recusada sem motivo escrito", c_e19_sem_motivo, "erro"),
    ("E19", "coleta recusada que nomeia campo fora do esquema", c_e19_campo_inventado, "erro"),
    ("E19", "coleta recusada com data no futuro", c_e19_data_no_futuro, "erro"),
    ("E19", "campo recusado agora preenchido, sem dizer quem superou", c_e19_campo_recusado_preenchido, "erro"),
    ("E17", "nome de tela sem acento (o nome que vira titulo)", c_e17_acento, "erro"),
    ("E17", "nome de tela sem acento depois do hifen", c_e17_acento_no_meio, "erro"),
    ("E17", "nome de tela sem acento em token separado por espaco", c_e17_acento_token_solto, "erro"),
]


def main():
    original = json.load(open(BANCO, encoding="utf-8"))
    tmp = tempfile.mkdtemp(prefix="aqm-especies-")
    falhas = []

    print("== testes negativos do validador de especies ==")
    for caso in TESTES:
        # O ALVO E OPCIONAL E DEVERIA SER OBRIGATORIO (15/10/2026). Sem ele este
        # portao pergunta so "a marca da regra apareceu na saida?", e isso APROVA
        # POR ACIDENTE quando a mesma regra ja reprova OUTRO registro do banco: a
        # corrupcao pode nao ter sido vista e o teste passa com a linha de um
        # vizinho. Nao e hipotese — foi medido por duas mutacoes do
        # mutacoes-porte-maximo.py que SOBREVIVERAM em 15/10/2026, uma delas a do
        # E25, cujo aviso continua saindo no barbo rosado quando o do barbo
        # cereja deixa de sair. E a mesma familia do "bloco ausente satisfazia o
        # `not in` por acidente" que o portao do search-console.py achou na
        # vespera: aprovar por falta de evidencia.
        regra, descricao, corromper, esperado = caso[:4]
        alvo = caso[4] if len(caso) > 4 else None
        banco = copy.deepcopy(original)
        corromper(banco)
        caminho = os.path.join(tmp, "banco-%s.json" % regra.lower())
        with open(caminho, "w", encoding="utf-8") as fp:
            json.dump(banco, fp, ensure_ascii=False, indent=2)

        saida = subprocess.run([sys.executable, VALIDADOR, caminho],
                               capture_output=True, text=True)
        marca = "ERRO  [%s]" % regra if esperado == "erro" else "aviso [%s]" % regra
        # Com alvo, a linha tem de ser a DAQUELE registro: a regra certa reprovando
        # o registro que foi corrompido, e nao a mesma regra reprovando um vizinho.
        procurado = "%s %s:" % (marca, alvo) if alvo else marca
        pegou = procurado in saida.stdout
        codigo_certo = (saida.returncode == 1) if esperado == "erro" else True
        ok = pegou and codigo_certo
        print("  %-4s %-56s %s" % (regra, descricao, "pegou" if ok else "PASSOU BATIDO"))
        if not ok:
            falhas.append(regra)

    # o banco real nao pode ter sido tocado por nada disto
    depois = json.load(open(BANCO, encoding="utf-8"))
    if depois != original:
        print("  !! o banco real mudou durante os testes")
        falhas.append("banco-intacto")

    print("\n== resultado ==")
    print("  %d teste(s), %d falha(s)" % (len(TESTES), len(falhas)))
    if falhas:
        print("  regras que nao reprovaram o defeito: %s" % ", ".join(falhas))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())

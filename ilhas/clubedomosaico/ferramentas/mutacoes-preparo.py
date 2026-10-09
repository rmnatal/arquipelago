#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO CAMPO `preparo` — 06/10/2026, esquema v12.

O portao que esta bateria mede nasceu do bloco que fez a F2 e o Guia servirem o
`preparo`, e o buraco que ele fecha nao era um campo errado: era um campo SEM
PORTAO NENHUM. De 10/09 a 06/10/2026 nove registros carregaram `preparo` como
STRING solta, sem fonte, sem forma e sem uma linha de snippet lendo a palavra.
Nove declaracoes de fabricante lidas, gravadas e descartadas em silencio — o
defeito que esta ilha ja mediu com quatro outros nomes (o `isopor` e o `gesso`
dos dois vernizes, a desempenadeira da Pastilhart, o drywall do boletim da
cimentcola).

E O PRECO TINHA ENDERECO ESCRITO NO PROPRIO BANCO. Em
`materiais-colas.json / quartzolit-cimentcola-externo-acii / fontes /
bt-cimentcola-externo-2016-05` estava registrado, com estas palavras, que a cura
de 180 dias nao podia ser gravada porque "o campo `preparo` nao resolve: ele
existe neste esquema e a F2 NAO o serve em lugar nenhum". Um terco do substrato
daquela argamassa estava parado atras de uma frase que nenhuma tela servia.

AS TRES REGRAS HERDADAS das baterias irmas desta ilha, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao roda o `validar-banco.py` duas vezes e separa o que SO o portao
      novo viu, desligando-o com CDM_SEM_PORTAO_PREPARO=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem.
      A m08 e essa: ela fabrica o registro de cola que nasce SEM o campo, que e
      exatamente como os 32 registros de hoje nasceram e e o estado que o portao
      precisa pegar amanha, quando entrar uma cola nova.

  (c) ESTA BATERIA MEDE O FALSO POSITIVO, e aqui ele tem nome e caminho: a
      varredura de `exigencias_de_apoio_ja_declaradas_no_banco` desce dentro do
      `preparo`, e dentro do `preparo` moram subcampos que sao NOSSOS. Uma
      varredura que os lesse acusaria a nossa parafrase como declaracao do
      fabricante; uma que ignorasse o campo inteiro ficaria cega para a frase
      dele, que e o defeito oposto e o pior dos dois. As duas direcoes estao
      medidas aqui.

E HA UMA QUARTA, que esta bateria herda da 26.2 e que as irmas tambem cobram: a
lista de categorias que exigem o campo mora no ESQUEMA, e a bateria apaga a
chave para provar que o portao morre com ela em vez de aprovar tudo em silencio.

Uso:  python3 ferramentas/mutacoes-preparo.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")

ARQUIVOS = {
    "colas":     os.path.join(ILHA, "dados", "materiais-colas.json"),
    "pastilhas": os.path.join(ILHA, "dados", "materiais-pastilhas.json"),
    "rejuntes":  os.path.join(ILHA, "dados", "materiais-rejuntes.json"),
    "esquema":   os.path.join(ILHA, "dados", "esquema-banco.json"),
}


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


def prep(banco, ident):
    return item(banco, ident)["preparo"]


# --------------------------------------------------------------- as mutacoes

def m01(b):
    """O ESTADO REAL DE ONTEM, escrito de volta: `preparo` volta a ser STRING.
    E a mutacao mais importante do arquivo porque ela nao fabrica nada — ela
    restaura o banco como ele esteve por 26 dias. String nao carrega fonte, e
    frase sem fonte nao pode ir a tela (15.2)."""
    item(b, "cascola-cascorez-extra")["preparo"] = \
        "Superficies limpas, firmes, niveladas e secas; lixar quando necessario."


def m02(b):
    """Literal sem `fonte_id`. A frase vai a tela entre aspas, com o nome do
    fabricante embaixo — sem o documento, e afirmacao sem prova."""
    prep(b, "cascola-pl500-adesivo-de-montagem")["fonte_id"] = None


def m03(b):
    """`fonte_id` apontando para uma chave que nao existe nas `fontes` do
    registro. Procedencia que nao volta ao documento e decoracao — e esta e a
    forma que passa pela leitura humana, porque o campo esta preenchido."""
    prep(b, "quartzolit-rejunte-piscinas")["fonte_id"] = "bt-que-nao-existe"


def m04(b):
    """`lido_em` fora da forma ISO. Documento de 2016 relido hoje e outra coisa
    de documento lido em 2016, e a data e o que separa os dois."""
    prep(b, "quartzolit-cimentcola-externo-acii")["lido_em"] = "outubro de 2026"


def m05(b):
    """Literal sem `recorte_do_documento`. Citacao parcial de documento longo e
    legitima; citacao parcial SILENCIOSA e o defeito que esta migracao mediu
    quatro vezes em quatro parafrases."""
    prep(b, "pastilhart-af1500")["recorte_do_documento"] = ""


def m06(b):
    """Literal E `motivo_sem_literal` no mesmo registro. Os dois juntos nao sao
    estado nenhum: ou a frase dele existe, ou existe a causa de ela faltar. E o
    estado em que um registro fica quando alguem colhe o literal e esquece de
    apagar o motivo da passada anterior."""
    prep(b, "cascola-cascorez-extra")["motivo_sem_literal"] = \
        "CAUSA (nao-coletado): sobrou da passada anterior."


def m07(b):
    """Sem literal e com motivo FORA da forma `CAUSA (<classe>): ...`. A classe
    separa o que o proximo trabalhador pode resolver (`nao-coletado`) do que nao
    depende dele (`host-recusa`) — e foi por nao separar as duas que esta ilha
    releu quatro vezes a mesma porta fechada."""
    prep(b, "quartzolit-rejunte-acrilico")["motivo_sem_literal"] = \
        "nao deu para ler o documento"


def m08(b):
    """PRODUZ O MUNDO: uma cola do banco perde o campo `preparo` inteiro, que e
    exatamente como os 32 registros de hoje nasceram e como a proxima cola vai
    nascer se ninguem cobrar. Sem esta mutacao o portao estaria medindo so o
    banco migrado, que e medir o acaso e nao a regra."""
    del item(b, "tekbond-silicone-neutro")["preparo"]


def m09(b):
    """A TRAVA DA 26.2, primeira metade: o esquema perde
    `regras_do_campo_preparo` e o portao fica sem regra. Regua que le a propria
    lista de um arquivo de dados aprova tudo, em silencio, no dia em que o
    arquivo perder a chave."""
    del b["regras_do_campo_preparo"]


def m10(b):
    """A TRAVA DA 26.2, segunda metade: a chave do esquema continua e a LISTA de
    categorias fica vazia. E a forma silenciosa do mesmo defeito — o portao
    continua existindo e nao cobra ninguem."""
    b["regras_do_campo_preparo"]["categorias_que_exigem_o_campo"] = []


def m11(b):
    """Literal sem `como_a_tela_chama_o_documento`. Sem ele a tela cai no campo
    `tipo` da fonte, que e prosa de arquivo: o do rejunte piscinas chega sem um
    acento e o da cimentcola traz `escada_de_fontes` e o nome de um arquivo do
    repositorio dentro da frase."""
    prep(b, "quartzolit-rejunte-piscinas")["como_a_tela_chama_o_documento"] = ""


def m12(b):
    """O VOCABULARIO DE QUEM ESCREVEU A ILHA NA BOCA DE QUEM A LE: o rotulo passa
    a citar um arquivo do repositorio. E a cicatriz que a Ohmetria pagou em
    15/09/2026, quando a regua de acento pegou um defeito que nao era de acento —
    `dados/modulos.json` servido ao visitante."""
    prep(b, "cascola-cascorez-extra")["como_a_tela_chama_o_documento"] = \
        "na fonte `pagina-produto-cascorez` de dados/materiais-colas.json"


def m13(b):
    """O rotulo sem a preposicao contraida. A tela escreve `Esta escrito ` e cola
    o campo depois: sem ela sai `Esta escrito em a pagina de produto dele`, que
    foi literalmente o que o primeiro render deste bloco serviu."""
    prep(b, "pastilhart-af1500")["como_a_tela_chama_o_documento"] = \
        "a pagina de produto dele"


def m14(b):
    """A VARREDURA DE APOIO FICA CEGA: o esquema perde a lista de subcaminhos
    nossos e a varredura volta a descer no objeto inteiro, lendo a NOSSA
    parafrase como declaracao do fabricante. Reprova em duas direcoes de uma
    vez, e e esse o ponto."""
    del b["exigencias_de_apoio_ja_declaradas_no_banco"]["subcampos_que_NAO_sao_frase_do_fabricante"]


def m15(b):
    """A lista de subcaminhos troca um caminho por um PREFIXO generico
    (`preparo`), que apagaria o campo inteiro da varredura — inclusive a frase do
    fabricante. E o defeito oposto ao da m14 e o pior dos dois: ele nao acusa
    nada, ele silencia."""
    cam = b["exigencias_de_apoio_ja_declaradas_no_banco"][
        "subcampos_que_NAO_sao_frase_do_fabricante"]["caminhos"]
    cam.append("preparo")


def m16(b):
    """CORTAR A FRASE DO FABRICANTE: a obs. da desempenadeira sai do literal da
    cimentcola. Foi o estado em que este bloco esteve por alguns minutos — o
    termo ficava so em `recorte_do_documento`, que e prosa nossa —, e cegar a
    varredura no mesmo gesto em que se corta a declaracao e a definicao de
    declaracao lida e descartada em silencio."""
    p = prep(b, "quartzolit-cimentcola-externo-acii")
    p["literal_do_fabricante"] = p["literal_do_fabricante"].split(" Obs.:")[0]


MUTACOES = [
    ("m01 `preparo` volta a ser STRING (o banco de ontem)",   "colas",     m01),
    ("m02 literal sem fonte_id",                              "colas",     m02),
    ("m03 fonte_id apontando para chave inexistente",         "rejuntes",  m03),
    ("m04 lido_em fora da forma ISO",                         "colas",     m04),
    ("m05 literal sem recorte_do_documento",                  "pastilhas", m05),
    ("m06 literal E motivo_sem_literal juntos",               "colas",     m06),
    ("m07 sem literal e sem CAUSA (<classe>) na forma",       "rejuntes",  m07),
    ("m08 PRODUZ: cola nascendo SEM o campo",                 "colas",     m08),
    ("m09 26.2: o esquema perde regras_do_campo_preparo",     "esquema",   m09),
    ("m10 26.2: a lista de categorias fica vazia",            "esquema",   m10),
    ("m11 literal sem como_a_tela_chama_o_documento",         "rejuntes",  m11),
    ("m12 rotulo de tela citando arquivo do repositorio",     "colas",     m12),
    ("m13 rotulo de tela sem a preposicao contraida",         "pastilhas", m13),
    ("m14 a varredura de apoio perde a lista e fica lendo o nosso", "esquema", m14),
    ("m15 a lista ganha PREFIXO generico e silencia o campo", "esquema",   m15),
    ("m16 o literal perde a frase que nomeia a desempenadeira", "colas",   m16),
]


# ----------------------------------------- a trava do falso positivo (regra c)
#
# Nao sao mutacoes: as tres tem de PASSAR. Portao que reprova o banco certo e
# desligado pela primeira pessoa com pressa, e aí ele deixa de medir qualquer
# coisa.

def fp1(b):
    """Categoria que NAO exige o campo e que o tem completo: a AF1500 e pastilha,
    e `categorias_que_exigem_o_campo` lista so cola e rejunte. Campo presente e
    campo cobrado pela FORMA em qualquer categoria — e forma certa passa."""
    prep(b, "pastilhart-af1500")["nossa_leitura"] = None


def fp2(b):
    """Um subcampo NOSSO do preparo nomeia uma ferramenta vigiada (`pincel`). A
    varredura de apoio NAO pode acusar: aquilo e o nosso julgamento, nao a
    declaracao do fabricante. Se esta passar vermelha, a lista de subcaminhos
    deixou de funcionar."""
    prep(b, "quartzolit-rejunte-epoxi")["motivo_sem_literal"] = (
        "CAUSA (host-recusa): o documento nao abre daqui, e sem ele nao da para "
        "dizer se ele manda usar pincel, rolo ou desempenadeira.")


def fp3(b):
    """Categoria que nao exige o campo e nao o tem: um verniz de `acabamento`
    perde... nada. Esta e a afirmacao de que os 28 registros de pastilha,
    acabamento e alicate que NAO tem o campo continuam passando — o portao nao
    pode cobrar 28 motivos `nao coletado` que ninguem ia ler."""
    prep(b, "quartzolit-rejunte-ceramicas")["nossa_leitura"] = \
        prep(b, "quartzolit-rejunte-ceramicas")["nossa_leitura"] + " "


FALSOS_POSITIVOS = [
    ("categoria que nao exige, com o campo completo",      "pastilhas", fp1),
    ("subcampo NOSSO nomeando ferramenta vigiada",         "rejuntes",  fp2),
    ("parafrase preservada com a causa escrita",           "rejuntes",  fp3),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_PREPARO"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def escreve_e_roda(arquivo, mutado, sem_portao_novo=False):
    backup = arquivo + ".original"
    shutil.copy2(arquivo, backup)
    try:
        with open(arquivo, "w", encoding="utf-8") as fh:
            json.dump(mutado, fh, ensure_ascii=False, indent=2)
        return roda(sem_portao_novo=sem_portao_novo)
    finally:
        shutil.move(backup, arquivo)


# A REDE DE SINAL — `ferramentas/rede-de-sinal.py`, uma copia para as catorze
# baterias que trabalham EM CIMA da arvore do git. O `finally` desta bateria nao
# roda quando ela morre por sinal, e foi assim que a `mutacoes-par.py` deixou um
# snippet mutado no repositorio em 09/10/2026. Nome com hifen nao se importa
# direto; renomear a ferramenta por conveniencia de sintaxe seria romper a
# convencao de nome desta pasta.
def _rede_de_sinal():
    import importlib.util
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "rede-de-sinal.py")
    spec = importlib.util.spec_from_file_location("cdm_rede_de_sinal", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    # A rede de sinal ANTES da primeira mutacao: a janela entre o retrato e o
    # handler e a unica que fica descoberta, e aqui ela tem zero linha.
    _rede_de_sinal().arma(list(ARQUIVOS.values()))
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in ARQUIVOS.items()}

    if roda():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao do preparo desligado")
        return 1

    print("Mutacoes do campo `preparo` (esquema v12) — %d escritas" % len(MUTACOES))
    print("")
    reprovadas = 0
    so_o_portao_novo = 0
    for nome, qual, funcao in MUTACOES:
        arquivo = ARQUIVOS[qual]
        mutado = copy.deepcopy(originais[qual])
        funcao(mutado)
        if mutado == originais[qual]:
            print("  INERTE  %s — a mutacao nao mudou nada" % nome)
            continue
        pegou = escreve_e_roda(arquivo, mutado)
        pegou_sem = escreve_e_roda(arquivo, mutado, sem_portao_novo=True)

        if pegou:
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
                print("  REPROVOU  %-62s (so o portao novo viu)" % nome)
            else:
                print("  REPROVOU  %-62s (outro portao tambem pega)" % nome)
        else:
            print("  PASSOU    %-62s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  A TRAVA DO FALSO POSITIVO — o banco certo tem de PASSAR:")
    falsos = 0
    for rotulo, qual, funcao in FALSOS_POSITIVOS:
        mutado = copy.deepcopy(originais[qual])
        funcao(mutado)
        if escreve_e_roda(ARQUIVOS[qual], mutado):
            falsos += 1
            print("    FALSO POSITIVO  %-50s  <-- o portao reprovou banco legitimo" % rotulo)
        else:
            print("    passou          %s" % rotulo)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    print("  falso positivo ................. %d  (tem de ser 0)" % falsos)
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se os portoes antigos pegam tudo, o novo nao se justifica.")
        return 1
    if falsos:
        print("\nREPROVADO: portao que reprova o banco certo e desligado pela primeira "
              "pessoa com pressa.")
        return 1
    print("\nOK: as %d mutacoes reprovaram, %d delas so pelo portao novo, e os %d estados "
          "legitimos passaram." % (len(MUTACOES), so_o_portao_novo, len(FALSOS_POSITIVOS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a CONTA que liga tecnica a material, uma mutacao por vez, e exige que
`tecnica-x-material.py` chegue ao numero certo em cada uma.

    python3 ferramentas/mutacoes-tecnica-x-material.py

POR QUE ESTA BATERIA E DIFERENTE DA `mutacoes-tecnicas.py`. Aquela mede o BANCO de
tecnica: campo faltando, fonte fraca, id fora do vocabulario. Esta mede a CONTA — a
funcao `itens_de_banco_da_tecnica` do `validar-banco.py`, que decide se o portao da
secao 9 abre para uma tecnica. Sao coisas diferentes e quem confundiu as duas foi a
propria ilha: a bateria de 14/09 tinha um caso "com o lado do material resolvido" que
passava porque a tecnica citava `pastilha_vidro` e o banco tem 13 pastilhas de vidro.
Nenhuma das 14 mutacoes tocava no caminho que as DUAS tecnicas reais desta ilha usam,
que e o caco chegando ao banco pela COLA. Aquele caminho nasceu hoje e nasceu sem regua.

O QUE CADA MUTACAO AFIRMA. Nao e "aprova" ou "reprova": e o NUMERO. Cada linha declara
quantos itens de banco cada tecnica tem de ter depois da mutacao, e quantos estados
chegam ao minimo. Afirmar so o veredito deixaria passar a mutacao mais perigosa desta
familia — a que INFLA a conta, faz o portao abrir mais cedo e continua verde porque
"abriu", que e exatamente o que aconteceria se `mencionados_com_ressalva` entrasse na
soma.

AS DUAS METADES DA FRONTEIRA ESTAO AQUI, e de proposito: mutacoes que FECHAM o portao,
mutacoes que o mantem aberto com numero diferente, e uma que o abre para uma terceira
tecnica. Regua que so sabe fechar nunca deixaria a familia nascer — foi o defeito que
esta ilha corrigiu hoje.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o banco de verdade.
Ferramenta de bancada: nunca vai para o site.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# O estado de hoje, medido pelo proprio gerador antes de qualquer mutacao. Nao e um
# numero digitado: o `main` confere que o banco intacto bate com isto antes de comecar,
# e a bateria inteira para se nao bater. Assim a expectativa de cada mutacao e uma
# DIFERENCA em relacao a um ponto de partida que foi conferido, e nao uma lembranca.
INTACTO = {
    "direto": (0, 0),
    "indireto": (0, 0),
    "bizantino": (0, 0),
    "trencadis": (5, 10),
    "picassiette": (5, 5),
}


def carregar(raiz, nome):
    with open(os.path.join(raiz, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


def gravar(raiz, nome, dado):
    with open(os.path.join(raiz, "dados", nome), "w", encoding="utf-8") as fh:
        json.dump(dado, fh, ensure_ascii=False, indent=2)


def tecnica(banco, ident):
    for t in banco["tecnicas"]:
        if t["id"] == ident:
            return t
    raise KeyError(ident)


def cola(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise KeyError(ident)


def trocar_no_validador(raiz, velho, novo):
    """Mutacao de CODIGO: mexe na regua, nao no dado."""
    caminho = os.path.join(raiz, "ferramentas", "validar-banco.py")
    texto = open(caminho, encoding="utf-8").read()
    if velho not in texto:
        raise AssertionError("a mutacao de codigo nao achou o trecho: %r" % velho[:60])
    open(caminho, "w", encoding="utf-8").write(texto.replace(velho, novo, 1))


# NENHUMA MUTACAO DESTE ARQUIVO APAGA PRODUTO DO BANCO, e a razao vale ser escrita
# porque a primeira versao tentou e nao pode. O esquema desta ilha pina a matriz da F2
# CELULA POR CELULA, com os ids dos produtos escritos a mao — e ela e uma regua
# independente, do bloco 3. Tirar uma cola do banco deixa o banco INVALIDO contra
# aquela matriz, e o gerador entao morre por banco invalido em vez de responder a
# pergunta que a mutacao fazia. Reescrever a matriz junto seria produzir o mundo novo
# nos dois lados e comparar a regua com ela mesma. Entao as mutacoes de dado mexem no
# que NAO esta pinado — o que a tecnica declara — e as de codigo atacam a conta
# diretamente, que e onde este arquivo nasceu para morder.


# ------------------------------------------------------------------ mutacoes

def m_tecnica_perde_a_tessela(raiz):
    """A unica ligacao do Picassiete com o banco e a louca quebrada. Sem ela, a
    tecnica volta a ser texto sem material e o portao FECHA — e e assim que uma pagina
    fina nasce: alguem limpa um campo que parecia editorial."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "picassiette")
    t["materiais_tipicos"] = None
    t.pop("materiais_tipicos_fonte_id", None)
    t["motivo_sem_materiais"] = "mutacao de bancada"
    gravar(raiz, "tecnicas.json", b)


def m_bizantino_ganha_pastilha_de_vidro(raiz):
    """O OUTRO LADO DA FRONTEIRA. No dia em que uma fonte sustentar que o bizantino
    usa pastilha de vidro, as 13 pastilhas do banco passam a contar E as 5 colas
    elegiveis para essa tessela tambem. Se esta mutacao nao abrir o portao para uma
    TERCEIRA tecnica, a conta esta presa nas duas de caco."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "bizantino")
    t["materiais_tipicos"] = ["pastilha_vidro"]
    t["materiais_tipicos_fonte_id"] = "fasbam-mosaicos-bizantinos"
    t.pop("motivo_sem_materiais", None)
    gravar(raiz, "tecnicas.json", b)


def m_ressalva_entra_na_conta(raiz):
    """A MUTACAO MAIS PERIGOSA DA FAMILIA, e ela INFLA em vez de quebrar. Contar
    `mencionados_com_ressalva` faz o portao abrir mais cedo e deixa tudo verde para
    quem so olha o veredito — a ilha estaria declarando um rigor que nao tem,
    sustentada por fonte que o proprio esquema classifica como fraca demais."""
    trocar_no_validador(
        raiz,
        'eleg = sorted(c["recomendados_topo"] + c["elegiveis_abaixo_do_topo"])',
        'eleg = sorted(c["recomendados_topo"] + c["elegiveis_abaixo_do_topo"]\n                              + c["mencionados_com_ressalva"])')


def m_conta_ignora_a_tessela_declarada(raiz):
    """A INFLACAO MAIS CARA DE TODAS: a varredura passa a andar todas as tesselas do
    vocabulario, em vez das que a tecnica declara. O portao abriria para as TRES
    tecnicas que nao declaram material nenhum — e cada uma delas tem escrito, no
    proprio registro, por que nao declara. Seria a ilha publicando pagina de tecnica
    sustentada por material que nenhuma fonte liga aquela tecnica."""
    trocar_no_validador(raiz,
                        "    for tessela in tesselas:\n        for base in VOC",
                        '    for tessela in (tesselas or VOC["material_tessela"]):\n        for base in VOC')


def m_varredura_so_da_primeira_base(raiz):
    """A varredura encolhe para uma base so. E a forma mais silenciosa de errar aqui:
    o arquivo continua saindo, com cara de completo, medindo um nono do vocabulario.

    O NUMERO ESPERADO DESTA LINHA FOI ESCRITO ERRADO NA PRIMEIRA VEZ, e o registro
    fica porque e o proprio argumento a favor de afirmar numero em vez de veredito:
    eu previ que a uniao de colas ficaria em 5 e que os estados com o minimo cairiam
    para 2 e 1. A bancada devolveu 4 e 6 e 3, e ela estava certa — a base que sobra
    (`ceramica_esmaltada_porcelana`) tem tres dos cinco ambientes com o minimo, para
    cada tessela, e nunca chega a cinco colas porque a quinta so aparece em MDF. Uma
    bateria que so perguntasse "abriu ou fechou" teria passado nas duas contas, a
    minha e a certa, sem distinguir uma da outra.
    """
    trocar_no_validador(raiz,
                        'for base in VOC["base"]:',
                        'for base in VOC["base"][:1]:')


def m_pastilha_deixa_de_contar(raiz):
    """As duas metades da soma medidas separadamente. Com o bizantino declarando
    pastilha de vidro, o total tem de ser 13 pastilhas mais 5 colas; se o lado da
    pastilha cair da conta, sobram as 5 colas e o numero denuncia."""
    m_bizantino_ganha_pastilha_de_vidro(raiz)
    trocar_no_validador(raiz,
                        '"total": len(pastilhas) + len(colas),',
                        '"total": len(colas),')


def m_a_conta_some_do_validador(raiz):
    """A conta e arrastada para dentro do gerador — a segunda copia da mesma decisao,
    que e a cicatriz que esta ilha ja pagou duas vezes no mesmo dia. O gerador TEM de
    morrer em vez de improvisar uma conta propria."""
    trocar_no_validador(raiz, "def itens_de_banco_da_tecnica(", "def _aposentada_itens_de_banco_da_tecnica(")


def m_derivado_nao_regerado(raiz):
    """O banco de tecnica muda e ninguem roda o gerador. O derivado passa a descrever
    um mundo que nao existe mais — e `--conferir` e o unico portao que enxerga isso."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "trencadis")
    t["materiais_tipicos"] = ["caco_louca"]
    gravar(raiz, "tecnicas.json", b)


# nome, funcao, o que tem de sair
#   dict  -> {tecnica: (itens_de_banco, estados_com_o_minimo)} depois de REGERAR
#   "inflou" -> alguma tecnica tem de passar a contar MAIS do que conta hoje
#   "morre" -> o gerador tem de falhar
#   "conferir-falha" -> o gerador regerado nao roda; `--conferir` tem de acusar velho
MUTACOES = [
    ("Picassiete perde a louca quebrada: o portao FECHA", m_tecnica_perde_a_tessela,
     dict(INTACTO, picassiette=(0, 0))),
    ("bizantino ganha pastilha de vidro com fonte", m_bizantino_ganha_pastilha_de_vidro,
     dict(INTACTO, bizantino=(18, 4))),
    ("mencao com ressalva entra na conta", m_ressalva_entra_na_conta, "inflou"),
    ("a conta ignora a tessela que a tecnica declara", m_conta_ignora_a_tessela_declarada, "inflou"),
    ("a varredura encolhe para uma base so", m_varredura_so_da_primeira_base,
     dict(INTACTO, trencadis=(4, 6), picassiette=(4, 3))),
    ("a pastilha cai da soma", m_pastilha_deixa_de_contar, dict(INTACTO, bizantino=(5, 4))),
    ("a conta some do validador (segunda copia)", m_a_conta_some_do_validador, "morre"),
    ("a tecnica muda e ninguem regera o derivado", m_derivado_nao_regerado, "conferir-falha"),
]


def rodar(raiz, *args):
    r = subprocess.run([sys.executable, os.path.join(raiz, "ferramentas", "tecnica-x-material.py")]
                       + list(args), capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def ler_derivado(raiz):
    with open(os.path.join(raiz, "dados", "tecnica-x-material.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    return {l["tecnica"]: (l["itens_de_banco"], l["estados_com_o_minimo"]) for l in d["tecnicas"]}


def main():
    rc, saida = rodar(ILHA, "--conferir")
    if rc != 0:
        print("O derivado de verdade ja esta velho — rode o gerador antes de mutar.")
        print(saida)
        return 1
    intacto = ler_derivado(ILHA)
    if intacto != INTACTO:
        print("O PONTO DE PARTIDA MUDOU. O banco de hoje nao bate com o que esta bateria")
        print("afirma como intacto — e sem ponto de partida conferido, nenhuma expectativa")
        print("de mutacao quer dizer coisa alguma.")
        print("  esperado: %s" % INTACTO)
        print("  medido:   %s" % intacto)
        return 1
    print("derivado intacto: bate com o ponto de partida desta bateria\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-txm-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)

            if esperado == "conferir-falha":
                rc, saida = rodar(copia, "--conferir")
                if rc != 0:
                    print("  acusou como devia:   %-44s | %s" % (nome, saida.strip().splitlines()[0][:86]))
                else:
                    erradas.append(nome + " (--conferir PASSOU sobre derivado velho)")
                    print("  PASSOU (a trava NAO viu): %s" % nome)
                continue

            rc, saida = rodar(copia)
            if esperado == "morre":
                if rc != 0:
                    print("  morreu como devia:   %-44s | %s" % (nome, saida.strip().splitlines()[0][:86]))
                else:
                    erradas.append(nome + " (o gerador RODOU sem a conta do validador)")
                    print("  RODOU (a trava NAO viu): %s" % nome)
                continue

            if rc != 0:
                erradas.append(nome + " (o gerador morreu e nao devia)")
                print("  MORREU e nao devia:  %-44s | %s" % (nome, saida.strip().splitlines()[0][:86]))
                continue

            medido = ler_derivado(copia)
            if esperado == "inflou":
                subiu = [k for k in medido if medido[k][0] > INTACTO[k][0]]
                if subiu:
                    print("  o numero INFLOU como a mutacao previa: %-22s | %s"
                          % (nome, ", ".join("%s %d>%d" % (k, INTACTO[k][0], medido[k][0]) for k in subiu)))
                else:
                    erradas.append(nome + " (a conta NAO se moveu — a mutacao foi inerte)")
                    print("  INERTE (nao mediu nada): %s" % nome)
                continue

            if esperado == "encolheu":
                caiu = [k for k in medido if medido[k][1] < INTACTO[k][1]]
                if caiu:
                    print("  a varredura ENCOLHEU como a mutacao previa: %-17s | %s"
                          % (nome, ", ".join("%s %d>%d estados" % (k, INTACTO[k][1], medido[k][1]) for k in caiu)))
                else:
                    erradas.append(nome + " (a varredura NAO encolheu — a mutacao foi inerte)")
                    print("  INERTE (nao mediu nada): %s" % nome)
                continue

            if medido == esperado:
                mudou = [k for k in medido if medido[k] != INTACTO[k]]
                print("  chegou ao numero:    %-44s | %s" % (
                    nome, ", ".join("%s %d itens" % (k, medido[k][0]) for k in mudou) or "nada mudou"))
            else:
                erradas.append(nome + " (numero errado)")
                print("  NUMERO ERRADO:       %-44s" % nome)
                for k in sorted(esperado):
                    if medido.get(k) != esperado[k]:
                        print("      %-12s esperado %s, medido %s" % (k, esperado[k], medido.get(k)))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d decididas certo, %d erradas" %
          (len(MUTACOES), len(MUTACOES) - len(erradas), len(erradas)))
    if erradas:
        print("\nAS ERRADAS SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in erradas:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

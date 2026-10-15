#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conta quais categorias NOVAS do eixo /peixes/ o banco de hoje sustenta.

    python3 ferramentas/varrer-categorias-possiveis.py .
    python3 ferramentas/varrer-categorias-possiveis.py . --gravar

POR QUE ELE EXISTE, e a resposta e uma conta que duas levas seguidas fizeram A
MAO no fecho delas.

A leva 7 (22/09/2026) escreveu no `PROMPT.md`: "Varridos o catalogo embutido e as
listas declaradas das sete categorias: 31 especies elegiveis, 23 com ficha
propria, 8 sem categoria nenhuma - nenhuma familia entre as oito chega a tres".
A leva 8, horas depois, escreveu a MESMA conta com outros numeros: "32 elegiveis,
26 com ficha propria, 6 sem categoria nenhuma". As duas contas decidem a mesma
coisa - se existe proxima leva de malha neste eixo -, as duas foram feitas de
cabeca, e nenhuma das duas deixou como medir de novo.

E a QUARTA lista escrita a mao desta familia, e as tres anteriores morreram
todas na mesma semana: a lista de portoes que cada execucao enumerava no
`REGISTRO.md` (morreu na bancada de 22/09), a lista de paginas do portao da voz,
e a tabela de levas de `dados/indexacao.md` (que ganhou o
`conferir-indice-de-levas.py` no mesmo dia). O defeito de todas e o mesmo: a
lista nao avisa quando alguem esquece de alimenta-la, e aqui ela decide se a
ilha PODE crescer.

O QUE ELE NAO DECIDE, e isto e o limite dele: **qual e o critério da categoria.**
O eixo /peixes/ tem oito categorias e nenhuma delas usa o mesmo critério que a
anterior - os tetras saem por genero comercial, os danios e rasboras por nome, os
acarás por porte declarado, e a propria `acaras` registrou que "nem a familia,
nem o genero, nem o nome servem de critério aqui". Uma ferramenta que escolhesse
o critério estaria inventando a afirmacao central da pagina. Entao ele CONTA por
familia (que e a conta que as duas levas fizeram a mao) e CONTA por nome popular
compartilhado (que e o critério que a `danios-e-rasboras` usou), e chama as duas
de PISTA, nunca de veredito. Quem decide e quem escreve a leva, contra a tabela
que a pagina serve.

A REGUA DE ELEGIBILIDADE ESTA ESCRITA AQUI, de proposito, e o esquema e lido
apenas para conferir que as duas listas dizem a mesma coisa - a mesma decisao do
`gerar-catalogo-especies.py` e pelo mesmo motivo (secao 8 do ARQUIPELAGO.md): se
este arquivo importasse a lista do esquema, apagar um campo la faria as duas
metades errarem juntas.
"""
import collections
import datetime
import io
import json
import os
import subprocess
import sys

RAIZ = None

# A regua do portao de PAGINA, escrita aqui. Espelha minimo_para_sugerir
# .pagina-especie do esquema, e a conferencia de que as duas concordam e feita
# em conferir_regua_com_esquema().
CAMPOS_DE_PAGINA = [
    "nome_cientifico", "nomes_populares_br", "porte_adulto_cm", "porte_medida",
    "comprimento_minimo_aquario_cm", "convivencia", "temperatura_C",
]
STATUS_QUE_NUNCA_SUGERE = ("rascunho", "revalidar")
CONVIVENCIA_SEM_CARDUME = ("solitario", "casal", "harem")
MINIMO_DO_16_5 = 3

# OS CORPOS DE FONTE SAO LIDOS DO ESQUEMA, E ESTA E A UNICA COISA DESTE ARQUIVO QUE NAO
# E ESCRITA DUAS VEZES — de proposito, e a diferenca importa. A CAMPOS_DE_PAGINA e uma
# DECISAO (que campos uma ficha precisa ter), e decisao se escreve duas vezes e se confere,
# senao apagar um campo no esquema faz as duas metades errarem juntas. O registro de corpos
# e um FATO EXTERNO (quais hosts sao a FishBase, de onde vem o numero de cada corpo), e
# ninguem redescobre isso de forma independente: a segunda escrita dele nao confere nada e
# so cria duas verdades. Medido em 15/10/2026 — a tabela estava copiada a mao aqui e no
# validar-especies.py, as duas ja com FORMAS diferentes (aqui as variantes "www." eram
# listadas a mao, la o "www." era removido do host), nada acusava a divergencia, e nenhuma
# das duas sabia o que e um REPRODUTOR. Agora a regua mora em `corpos_de_fonte` do esquema,
# com a procedencia declarada corpo por corpo, e a regra E26 a cobra.
CORPOS = {}      # host sem www -> (nome, procedencia, reproduz); preenchido no main()


def carregar_corpos():
    caminho = os.path.join(RAIZ, "dados", "esquema-especies.json")
    esquema = json.load(io.open(caminho, encoding="utf-8"))
    CORPOS.clear()
    for corpo in esquema["corpos_de_fonte"]["corpos"]:
        for host in corpo["hosts"]:
            CORPOS[host.lower()] = (corpo["nome"], corpo["procedencia"], corpo.get("reproduz"))


def preenchido(v):
    if v is None:
        return False
    if isinstance(v, str):
        return v.strip() != ""
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


def host_da_fonte(url):
    dominio = (url or "").split("/")[2] if "//" in (url or "") else (url or "")
    dominio = dominio.lower()
    return dominio[4:] if dominio.startswith("www.") else dominio


def corpo_contavel(url):
    """O nome com que a url CONTA, ou None se ela nao conta como corpo nenhum.

    Quem decide e a PROCEDENCIA declarada no esquema, nunca o host: `propria` conta
    como si, `reproduz` colapsa no corpo que ela reproduz — duas urls de hosts
    diferentes continuam sendo um corpo so —, e `indeterminada` nao conta, porque
    fonte que nao diz de onde veio o numero dela nao e o proprio corpo nem o de outro.
    Corpo nao declarado tambem nao conta, e o validador reprova o banco pelo E26.
    """
    declarado = CORPOS.get(host_da_fonte(url))
    if declarado is None:
        return None
    nome, procedencia, reproduz = declarado
    if procedencia == "reproduz":
        return reproduz
    if procedencia == "indeterminada":
        return None
    return nome


def corpos_de(registro):
    nomes = {corpo_contavel(f.get("url")) for f in (registro.get("fontes") or [])}
    nomes.discard(None)
    return nomes


def falta_para_pagina(registro):
    """O que impede este registro de virar ficha. Lista vazia = elegivel."""
    falta = []
    for campo in CAMPOS_DE_PAGINA:
        if not preenchido(registro.get(campo)):
            falta.append(campo)
    if len(corpos_de(registro)) < 2:
        falta.append("duas fontes de corpos distintos")
    if registro.get("status_registro") in STATUS_QUE_NUNCA_SUGERE:
        falta.append("status %s" % registro.get("status_registro"))
    conv = registro.get("convivencia")
    if not preenchido(registro.get("cardume_minimo")) and conv not in CONVIVENCIA_SEM_CARDUME:
        falta.append("cardume_minimo ou convivencia solitario/casal/harem")
    return falta


def conferir_regua_com_esquema():
    """As duas listas tem de dizer a mesma coisa, e a divergencia e ERRO."""
    caminho = os.path.join(RAIZ, "dados", "esquema-especies.json")
    esquema = json.load(io.open(caminho, encoding="utf-8"))
    do_esquema = list(esquema["minimo_para_sugerir"]["pagina-especie"])
    daqui = list(CAMPOS_DE_PAGINA) + ["duas fontes distintas",
                                      "cardume_minimo OU convivencia igual a solitario/casal/harem"]
    if sorted(do_esquema) != sorted(daqui):
        print("FALHA: a regua deste arquivo e a do esquema discordam.")
        print("  esquema: %s" % sorted(do_esquema))
        print("  daqui  : %s" % sorted(daqui))
        return False
    return True


def php(script, *args):
    saida = subprocess.run(["php", os.path.join(RAIZ, "ferramentas", script), RAIZ] + list(args),
                           capture_output=True, text=True, check=True).stdout
    return json.loads(saida)


def tokens_de_nome(registro):
    """Os nomes populares reduzidos a palavra que a loja usa como prateleira.

    'barbo sumatra', 'barbo-cereja' e 'barbo rosado' compartilham `barbo`. E o
    critério que a `danios-e-rasboras` usou, e por isso ele e contado - como
    PISTA, e nao como veredito.
    """
    palavras = set()
    for nome in registro.get("nomes_populares_br") or []:
        for pedaco in nome.replace("-", " ").lower().split():
            if len(pedaco) >= 4:
                palavras.add(pedaco)
    return palavras


def main():
    global RAIZ
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    gravar = "--gravar" in sys.argv
    alvo = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAIZ = os.path.abspath(alvo)

    carregar_corpos()
    if not conferir_regua_com_esquema():
        return 1

    banco = json.load(io.open(os.path.join(RAIZ, "dados", "especies-agua-doce.json"),
                              encoding="utf-8"))
    registros = banco["especies"]
    categorias = php("listar-categorias-do-eixo.php")
    paginas = php("listar-paginas-do-eixo.php")

    com_ficha = {d["especie"] for d in paginas.values() if d.get("especie")}
    em_categoria = {}
    for slug, dados in categorias.items():
        for eid in dados.get("especies") or []:
            em_categoria[eid] = slug

    elegiveis, barrados = [], []
    for r in registros:
        (elegiveis if not falta_para_pagina(r) else barrados).append(r)

    sem_categoria = [r for r in elegiveis if r["id"] not in em_categoria]
    sem_ficha = [r for r in elegiveis if r["id"] not in com_ficha]

    linhas = []
    linhas.append("== banco ==")
    linhas.append("  %d registros, %d elegiveis para ficha, %d barrados"
                  % (len(registros), len(elegiveis), len(barrados)))
    linhas.append("  %d elegiveis com ficha propria, %d elegiveis sem ficha, "
                  "%d elegiveis sem categoria nenhuma"
                  % (len(elegiveis) - len(sem_ficha), len(sem_ficha), len(sem_categoria)))

    linhas.append("")
    linhas.append("== categoria declarada, e o que ela ja sustenta ==")
    for slug in sorted(categorias):
        declaradas = categorias[slug].get("especies") or []
        vivas = [e for e in declaradas if e in {r["id"] for r in elegiveis}]
        publicada = slug in paginas
        linhas.append("  %-24s %d declarada(s), %d elegivel(is) — %s"
                      % (slug, len(declaradas), len(vivas),
                         "pagina no ar" if publicada else "declarada, sem pagina"))

    def agrupar(chave_de):
        grupos = collections.defaultdict(list)
        for r in sem_categoria:
            for chave in chave_de(r):
                grupos[chave].append(r["id"])
        return grupos

    for titulo, chave_de, nota in (
        ("por FAMILIA (a conta que as levas 7 e 8 fizeram a mao)",
         lambda r: [r.get("familia") or "<sem familia>"],
         "familia nao e critério de categoria neste eixo, e a `acaras` escreveu por que"),
        ("por NOME POPULAR compartilhado (o critério da danios-e-rasboras)",
         tokens_de_nome,
         "uma especie aparece em mais de um grupo, e grupo de nome nao prova prateleira"),
    ):
        linhas.append("")
        linhas.append("== elegiveis SEM categoria, agrupados %s ==" % titulo)
        linhas.append("  PISTA e nao veredito: %s" % nota)
        grupos = agrupar(chave_de)
        alcancam = [(k, v) for k, v in grupos.items() if len(v) >= MINIMO_DO_16_5]
        for chave, ids in sorted(grupos.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            marca = "ALCANCA O MINIMO DO 16.5" if len(ids) >= MINIMO_DO_16_5 else \
                    "falta %d" % (MINIMO_DO_16_5 - len(ids))
            linhas.append("  %-22s %d — %-24s %s" % (chave, len(ids), marca, ", ".join(sorted(ids))))
        if not grupos:
            linhas.append("  (nenhum)")
        linhas.append("  grupos que alcancam o minimo de %d: %d"
                      % (MINIMO_DO_16_5, len(alcancam)))

    linhas.append("")
    linhas.append("== barrados, e o que falta em cada um ==")
    for r in sorted(barrados, key=lambda x: len(falta_para_pagina(x))):
        linhas.append("  %-30s %s" % (r["id"], ", ".join(falta_para_pagina(r))))

    texto = "\n".join(linhas)
    print(texto)

    if gravar:
        serie = os.path.join(RAIZ, "dados", "cobertura-de-categorias.md")
        cabecalho = ("# Serie de cobertura de categoria — eixo /peixes/ da Aquametria\n\n"
                     "Uma secao por varredura, **nunca sobrescrever secao antiga**: a serie so "
                     "vale porque cresce. Quem escreve e `ferramentas/varrer-categorias-possiveis.py "
                     ". --gravar`. O que ela conta, e o que ela deliberadamente NAO decide, esta "
                     "no cabecalho daquele arquivo.\n")
        anterior = ""
        if os.path.exists(serie):
            anterior = io.open(serie, encoding="utf-8").read()
        else:
            anterior = cabecalho
        hoje = datetime.date.today().isoformat()
        with io.open(serie, "w", encoding="utf-8") as f:
            f.write(anterior.rstrip("\n"))
            f.write("\n\n## %s\n\n```\n%s\n```\n" % (hoje, texto))
        print("\ngravado em dados/cobertura-de-categorias.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

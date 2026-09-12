#!/usr/bin/env python3
"""Gera o catalogo de especies que o snippet das paginas de peixes embute.

    python3 ferramentas/gerar-catalogo-especies.py .

O site nao le JSON em tempo de requisicao — nenhum snippet desta ilha le. Entao
o banco precisa viajar DENTRO do snippet, e este script e o unico lugar onde a
traducao acontece. Ele reescreve o trecho entre CATALOGO-INICIO e CATALOGO-FIM
em snippets/aquametria-peixes.php. Nada mais do arquivo e tocado.

QUATRO DECISOES, e nenhuma e de estilo:

  1. SO ENTRA QUEM PASSA NO PORTAO DE PAGINA do esquema
     (`minimo_para_sugerir.pagina-especie`): nome cientifico, nomes populares,
     porte com a medida, frente minima declarada, convivencia, faixa de
     temperatura e DUAS fontes de corpos distintos. A regra do esquema exclui
     ainda `status_registro` rascunho e revalidar. A regua esta ESCRITA aqui,
     lida do esquema apenas para conferir que as duas listas dizem a mesma
     coisa — se este script importasse a lista do esquema, apagar um campo la
     faria as duas metades errarem juntas (secao 8 do ARQUIPELAGO.md).

  2. A FONTE VIAJA COM O NOME DO CORPO, nunca com o codigo de origem. A tela
     precisa dizer "FishBase" e "Seriously Fish", porque procedencia na propria
     frase e a regra da secao 5 — e `base-cientifica-via-busca` nao e nome de
     ninguem. O nome sai do prefixo da referencia, antes do travessao, e o
     script RECUSA gravar fonte cujo nome nao consegue ler: fonte sem nome na
     tela e fonte que o leitor nao pode conferir.

  3. NENHUM CAMPO DERIVADO E GRAVADO (regra E7 do esquema). Frente por
     individuo, volume e lotacao sao calculados pelo PHP na hora de imprimir.
     Gravar derivado aqui criaria duas verdades para o mesmo numero, e a que
     envelhece e sempre a gravada.

  4. O CONFLITO VIAJA INTEIRO. Registro com divergencia declarada publica os
     dois extremos com a atribuicao de cada um (secao 15.2 e o rodape da
     ilha: a Aquametria nunca tira media). Conflito que ficasse fora do
     catalogo faria a pagina publicar um numero unico com cara de consenso.
"""

import json
import os
import re
import sys

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-especies.json")
ALVO = os.path.join(RAIZ, "snippets", "aquametria-peixes.php")

INICIO = "\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */"
FIM = "\t/* CATALOGO-FIM */"

# A regua do portao de pagina, escrita aqui. Ver decisao 1 do cabecalho.
CAMPOS_DO_PORTAO = [
    "nome_cientifico",
    "nomes_populares_br",
    "porte_adulto_cm",
    "porte_medida",
    "comprimento_minimo_aquario_cm",
    "convivencia",
    "temperatura_C",
]
STATUS_BARRADOS = ("rascunho", "revalidar")


def php_valor(v, ident=2):
    """Serializa em array() do PHP 5 — o mesmo estilo dos outros catalogos."""
    tab = "\t" * ident
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        texto = repr(float(v))
        if texto.endswith(".0"):
            texto = texto[:-2]
        return texto
    if isinstance(v, str):
        return "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'"
    if isinstance(v, list):
        if not v:
            return "array()"
        itens = [tab + "\t" + php_valor(x, ident + 1) + "," for x in v]
        return "array(\n" + "\n".join(itens) + "\n" + tab + ")"
    if isinstance(v, dict):
        if not v:
            return "array()"
        itens = []
        for k, x in v.items():
            itens.append(tab + "\t" + php_valor(str(k), ident + 1) + " => " + php_valor(x, ident + 1) + ",")
        return "array(\n" + "\n".join(itens) + "\n" + tab + ")"
    raise SystemExit("ERRO: tipo que nao sei serializar: %r" % (v,))


def nome_do_corpo(referencia):
    """'FishBase — ficha da especie: ...' -> 'FishBase'.

    Sem nome legivel a fonte nao entra: ver decisao 2 do cabecalho.

    O corte e no PRIMEIRO separador de qualquer um dos quatro tipos, e nao so no
    travessao: o banco escreve a referencia de fonte com travessao
    ("FishBase - ficha da especie: ...") e a referencia de CONFLITO com virgula
    ou dois pontos ("FishBase, secao de aquario: ...", "FishBase: pH 5,0 a 7,8").
    Cortar so no travessao devolvia a frase inteira como se fosse nome de corpo,
    e ela ia para a tela assim — "5 a 7,8 pelo FishBase: pH 5,0 a 7,8".

    A recusa tambem e por DIGITO: nome de corpo de fonte nao tem numero dentro.
    E a unica regra que separa "FishBase" de "FishBase: pH 5,0" sem precisar de
    uma lista de fontes conhecidas — e lista de fontes conhecidas calaria a fonte
    nova em vez de acusar.
    """
    if not referencia:
        return ""
    corte = re.split(r"(?:\s+[—–-]\s+|:\s|,\s)", referencia, maxsplit=1)[0].strip()
    corte = corte.strip(" .:,")
    if not corte or len(corte) > 40 or re.search(r"\d", corte):
        return ""
    return corte


def host(url):
    """O dominio de uma url, sem www."""
    m = re.match(r"https?://([^/]+)", str(url or ""))
    if not m:
        return ""
    return m.group(1).lower().replace("www.", "")


def mapa_de_hosts(banco):
    """host -> nome do corpo, APRENDIDO das fontes do proprio banco.

    Por que aprendido e nao escrito: valor de conflito nem sempre traz
    `referencia` — dois registros do banco trazem so `valor`, `origem` e `url` —,
    e `origem` e codigo de esquema ("base-cientifica-via-busca"), nao nome de
    ninguem. O que identifica o corpo ali e a URL, e a mesma URL aparece nas
    `fontes`, onde a referencia diz o nome. Entao o mapa sai do banco.

    Lista de hosts escrita a mao faria a fonte NOVA sair na tela com o codigo de
    origem em vez de acusar a falta — e e a cicatriz da secao 8: quando o texto
    legitimo e o que se quer medir se parecem, quem decide e o identificador,
    nunca a vizinhanca.
    """
    mapa = {}
    for e in banco["especies"]:
        for f in e.get("fontes", []):
            nome = nome_do_corpo(f.get("referencia", ""))
            h = host(f.get("url"))
            if nome and h and h not in mapa:
                mapa[h] = nome
    return mapa


def nome_do_valor(v, mapa_host):
    """O nome do corpo de um valor de conflito: pela referencia, ou pelo host."""
    nome = nome_do_corpo(v.get("referencia", ""))
    if nome:
        return nome
    return mapa_host.get(host(v.get("url")), "")


def corpos_distintos(especie):
    """Dois corpos, nao duas urls (regra E15 do esquema)."""
    return {nome_do_corpo(f.get("referencia", "")) or f.get("origem", "") for f in especie.get("fontes", [])}


def passa_no_portao(e):
    faltando = []
    for campo in CAMPOS_DO_PORTAO:
        valor = e.get(campo)
        if campo == "temperatura_C":
            if not isinstance(valor, dict) or valor.get("min") is None or valor.get("max") is None:
                faltando.append(campo)
            continue
        if valor in (None, "", [], {}):
            faltando.append(campo)
    if len(corpos_distintos(e)) < 2:
        faltando.append("duas fontes distintas")
    if e.get("status_registro") in STATUS_BARRADOS:
        faltando.append("status_registro " + str(e.get("status_registro")))
    return faltando


def conferir_esquema():
    """As duas listas do portao tem de dizer a mesma coisa.

    O esquema e o documento; este script e o codigo. Documento e codigo mantidos
    a mao em dois lugares divergem em silencio, e por isso a conferencia nomeia
    a diferenca em vez de confiar.
    """
    with open(ESQUEMA, encoding="utf-8") as f:
        esquema = json.load(f)
    do_esquema = list(esquema["minimo_para_sugerir"]["pagina-especie"])
    daqui = CAMPOS_DO_PORTAO + ["duas fontes distintas"]
    if [x for x in do_esquema if x not in daqui] or [x for x in daqui if x not in do_esquema]:
        raise SystemExit(
            "ERRO: o portao de pagina do esquema e o deste script divergem.\n"
            "  esquema: %s\n  script : %s" % (do_esquema, daqui)
        )
    return esquema


def escrever_bloco(php, inicio, fim, corpo):
    if inicio not in php or fim not in php:
        raise SystemExit("ERRO: marcadores %s/%s nao encontrados em %s" % (inicio, fim, ALVO))
    antes = php.split(inicio)[0]
    depois = php.split(fim, 1)[1]
    return antes + inicio + "\n" + corpo + "\n" + fim + depois


def main():
    conferir_esquema()
    with open(BANCO, encoding="utf-8") as f:
        banco = json.load(f)
    mapa_host = mapa_de_hosts(banco)

    dentro = {}
    fora = []
    for e in banco["especies"]:
        faltando = passa_no_portao(e)
        if faltando:
            fora.append((e["id"], faltando))
            continue

        fontes = []
        sem_nome = []
        for f in e.get("fontes", []):
            corpo = nome_do_corpo(f.get("referencia", "")) or mapa_host.get(host(f.get("url")), "")
            if not corpo:
                sem_nome.append("fonte sem nome de corpo: " + str(f.get("url")))
                continue
            fontes.append({
                "corpo": corpo,
                "url": f.get("url") or "",
                "em": f.get("verificado_em") or "",
                "campos": list(f.get("campos") or []),
                "referencia": f.get("referencia") or "",
            })

        conflitos = []
        for c in e.get("conflitos", []):
            valores = []
            for v in c.get("valores", []):
                fonte = nome_do_valor(v, mapa_host)
                if not fonte:
                    sem_nome.append("conflito em %s sem nome de corpo: %s" % (c.get("campo"), v.get("url")))
                    continue
                valores.append({
                    "valor": v.get("valor") if not isinstance(v.get("valor"), dict) else v["valor"],
                    "fonte": fonte,
                    "referencia": v.get("referencia") or "",
                })
            conflitos.append({
                "campo": c.get("campo") or "",
                "valores": valores,
                "razao": c.get("razao") or "",
                "tratamento": c.get("tratamento") or "",
            })

        if sem_nome:
            """Registro que nao sabe nomear quem declarou o numero NAO vira pagina.

            A secao 5 do contrato manda a procedencia estar na propria frase, e
            a divergencia se publica com a atribuicao de cada extremo. Sem o
            nome do corpo a pagina serviria "5 a 7,8 pelo compendio-via-busca",
            que e codigo de esquema na tela do leitor. Barrar aqui e barrar cedo:
            a especie continua no banco e fica nomeada nesta saida.
            """
            fora.append((e["id"], sem_nome))
            continue

        base = e.get("base_minima_cm") or {}
        dentro[e["id"]] = {
            "id": e["id"],
            "cientifico": e["nome_cientifico"],
            "sinonimos": list(e.get("sinonimos_cientificos") or []),
            "populares": list(e["nomes_populares_br"]),
            "familia": e.get("familia") or "",
            "origem": e.get("origem_geografica") or "",
            "porte_cm": e["porte_adulto_cm"],
            "porte_medida": e["porte_medida"],
            "cardume": e.get("cardume_minimo"),
            "convivencia": e["convivencia"],
            "comportamento": e.get("comportamento") or "",
            "frente_cm": e["comprimento_minimo_aquario_cm"],
            "base_comprimento": base.get("comprimento"),
            "base_largura": base.get("largura"),
            "temp_min": e["temperatura_C"]["min"],
            "temp_max": e["temperatura_C"]["max"],
            "status": e.get("status_registro") or "",
            "fontes": fontes,
            "conflitos": conflitos,
        }

    corpo = "\tstatic $catalogo = null;\n"
    corpo += "\tif ( null !== $catalogo ) {\n\t\treturn $catalogo;\n\t}\n"
    corpo += "\t$catalogo = " + php_valor(dentro, 1) + ";\n"
    corpo += "\treturn $catalogo;"

    with open(ALVO, encoding="utf-8") as f:
        php = f.read()
    php = escrever_bloco(php, INICIO, FIM, corpo)
    with open(ALVO, "w", encoding="utf-8") as f:
        f.write(php)

    print("catalogo de especies: %d dentro, %d fora do portao de pagina" % (len(dentro), len(fora)))
    print("banco: %d registros" % len(banco["especies"]))
    for ident, faltando in fora:
        print("  fora: %-32s %s" % (ident, ", ".join(faltando)))


if __name__ == "__main__":
    main()

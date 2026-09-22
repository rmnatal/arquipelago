#!/usr/bin/env python3
"""Gera o catalogo de especies que o snippet das paginas de peixes embute.

    python3 ferramentas/gerar-catalogo-especies.py .

O site nao le JSON em tempo de requisicao — nenhum snippet desta ilha le. Entao
o banco precisa viajar DENTRO do snippet, e este script e o unico lugar onde a
traducao acontece. Ele reescreve o trecho entre CATALOGO-INICIO e CATALOGO-FIM
em snippets/aquametria-peixes.php. Nada mais do arquivo e tocado.

CINCO DECISOES, e nenhuma e de estilo:

  1. SO ENTRA QUEM PASSA NO PORTAO DE PAGINA do esquema
     (`minimo_para_sugerir.pagina-especie`): nome cientifico, nomes populares,
     porte com a medida, frente minima declarada, convivencia, faixa de
     temperatura e DUAS fontes de corpos distintos. A regra do esquema exclui
     ainda `status_registro` rascunho e revalidar. A regua esta ESCRITA aqui,
     lida do esquema apenas para conferir que as duas listas dizem a mesma
     coisa — se este script importasse a lista do esquema, apagar um campo la
     faria as duas metades errarem juntas (secao 8 do ARQUIPELAGO.md).

  5. ESTAR NO CATALOGO E VIRAR FICHA SAO DUAS REGUAS, e ate 12/09/2026 elas
     eram uma so — com o nome da segunda. O catalogo alimenta TRES coisas alem
     da ficha: a contagem da secao ("N especies com o minimo declarado"), a
     tabela da categoria e a lista de quem divide a mesma agua. Uma especie
     pode ser dado bom para as tres e mesmo assim nao poder ter pagina propria.

     O caso que mostrou isso: o titulo de toda ficha deste eixo e "quantos
     litros para um cardume de X", e a linha mestra abre por "para os N X que a
     fonte declara como cardume minimo". Sem N, o codigo cai num ramo que
     escreve a frase sem o numero e a tabela pre-renderizada abre a primeira
     linha em UM exemplar — numa pagina que, duas telas abaixo, diz que a
     especie so vive em grupo. O esquema ja cobrava esse numero no portao da
     C8, com a frase `cardume_minimo OU convivencia igual a
     solitario/casal/harem`, desde que o banco nasceu; o que faltava era a
     pagina cobrar o mesmo.

     A primeira versao desta mudanca poe a regra no portao do CATALOGO, e a
     conta da secao caiu de 27 para 26 especies: corydoras sterbai, que declara
     convivencia "grupo" sem numero, sumiu da contagem, da tabela da categoria
     e da lista de companheiros — tres lugares onde o dado dela e bom e a
     afirmacao da pagina ("com o minimo declarado por fonte com nome e data")
     continua verdadeira. Apertar o portao errado tirou informacao verdadeira
     da tela para resolver um problema de outra pagina. Por isso sao duas
     listas com dois nomes no esquema, `catalogo-de-especies` e
     `pagina-especie`, e a segunda e a primeira MAIS a regra do cardume.

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

  6. QUEM NAO PASSA TAMBEM VIAJA — e ate 13/09/2026 nao viajava (bloco das
     23h19Z). O catalogo carregava so quem PASSA no portao, entao os barrados
     simplesmente NAO EXISTIAM no snippet: a pagina podia dizer "sao 29
     especies" e nao tinha como dizer que o banco tem 37 nem por que os outros
     8 nao estao ali. A prestacao de contas da secao 7 do ARQUIPELAGO.md ("cada
     item da categoria consultada aparece exatamente uma vez na prosa da
     resposta — ou na frase que o recomenda, ou numa linha que diz por que ele
     nao esta") estava cumprida para quem esta na tabela e para mais ninguem.
     Este script passou a escrever um SEGUNDO bloco, entre BARRADOS-INICIO e
     BARRADOS-FIM, com o registro barrado e o que falta nele.

     E O MOTIVO VIAJA COMO CODIGO, NUNCA COMO FRASE. A traducao para a lingua
     do leitor mora no PHP, num mapa so, e nao aqui: se este script escrevesse
     a frase pronta, o dia em que alguem mudasse a redacao de um motivo
     reescreveria o catalogo inteiro e o `sha256` do manifest mudaria por causa
     de uma virgula. O vocabulario de codigos e FECHADO (`MOTIVOS`) e este
     script RECUSA gravar codigo que nao esteja nele — regra nova de portao que
     chegasse a tela como `comprimento_minimo_aquario_cm` seria vocabulario de
     dentro da fabrica na cara do leitor, que e o defeito que a secao 5 do
     contrato existe para impedir.

     E RECUSA TAMBEM registro barrado sem `nome_cientifico`: linha que nao sabe
     nomear a especie e linha que o leitor nao consegue conferir. O esquema
     declara esse campo obrigatorio, entao o caso nao existe hoje — a recusa
     esta aqui para o dia em que alguem afrouxar o esquema, e nao como ramo de
     tela, que seria regua escrita para um mundo que nao pode acontecer.
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

BARRADOS_INICIO = "\t/* BARRADOS-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */"
BARRADOS_FIM = "\t/* BARRADOS-FIM */"

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

# A regra 5 do cabecalho, escrita com a MESMA frase que o esquema usa no portao
# da C8 — e de proposito: duas frases diferentes para a mesma regra viram duas
# regras no dia em que alguem editar uma delas.
REGRA_DO_CARDUME = "cardume_minimo OU convivencia igual a solitario/casal/harem"
CONVIVENCIA_SEM_CARDUME = ("solitario", "casal", "harem")

# O VOCABULARIO FECHADO DOS MOTIVOS (decisao 6 do cabecalho). Um codigo por
# causa, e a causa e o que o leitor precisa entender — nao o texto de depuracao
# que o terminal imprime. Por isso `fonte sem nome de corpo: https://...` vira
# `fonte sem nome de corpo` sem a url: url dentro de um motivo na tela nao
# explica nada a quem le e ainda publica endereco de fonte que a ilha nao
# conseguiu ler.
MOTIVOS = tuple(CAMPOS_DO_PORTAO) + (
    "duas fontes distintas",
    "status_registro rascunho",
    "status_registro revalidar",
    "fonte sem nome de corpo",
)


def codigo_de_motivo(bruto):
    """O codigo fechado de um motivo que o portao produziu.

    O portao escreve motivo de DUAS formas: o nome do campo que faltou, seco, e
    uma frase de diagnostico com url dentro ("conflito em pH sem nome de corpo:
    https://..."). A segunda nunca pode chegar a tela, e cortar a url por
    heuristica seria adivinhar por vizinhanca — entao o corte e por prefixo
    declarado, e o que nao casar com nenhum prefixo conhecido PARA o script.
    """
    if bruto in MOTIVOS:
        return bruto
    for prefixo in ("fonte sem nome de corpo", "conflito em "):
        if bruto.startswith(prefixo):
            return "fonte sem nome de corpo"
    raise SystemExit(
        "ERRO: motivo sem codigo no vocabulario fechado: %r\n"
        "  Regra nova de portao precisa de um codigo em MOTIVOS aqui E de uma\n"
        "  traducao em aquametria_peixes_motivo_na_tela() no snippet, senao ela\n"
        "  chega a tela do leitor como nome de campo de banco." % (bruto,)
    )


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


def falta_para_virar_ficha(e):
    """O portao de PAGINA: o do catalogo MAIS a regra do cardume (decisao 5).

    Devolve a lista do que falta. Lista vazia = pode ter pagina propria.
    """
    faltando = list(passa_no_portao(e))
    if not e.get("cardume_minimo") and e.get("convivencia") not in CONVIVENCIA_SEM_CARDUME:
        faltando.append(REGRA_DO_CARDUME)
    return faltando


def conferir_esquema():
    """As duas listas do portao tem de dizer a mesma coisa.

    O esquema e o documento; este script e o codigo. Documento e codigo mantidos
    a mao em dois lugares divergem em silencio, e por isso a conferencia nomeia
    a diferenca em vez de confiar.
    """
    with open(ESQUEMA, encoding="utf-8") as f:
        esquema = json.load(f)
    for nome, daqui in (
        ("catalogo-de-especies", CAMPOS_DO_PORTAO + ["duas fontes distintas"]),
        ("pagina-especie", CAMPOS_DO_PORTAO + ["duas fontes distintas", REGRA_DO_CARDUME]),
    ):
        if nome not in esquema["minimo_para_sugerir"]:
            raise SystemExit("ERRO: o esquema nao declara minimo_para_sugerir.%s" % nome)
        do_esquema = list(esquema["minimo_para_sugerir"][nome])
        if [x for x in do_esquema if x not in daqui] or [x for x in daqui if x not in do_esquema]:
            raise SystemExit(
                "ERRO: o portao '%s' do esquema e o deste script divergem.\n"
                "  esquema: %s\n  script : %s" % (nome, do_esquema, daqui)
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
            # O TETO DA FAIXA (esquema versao 4, 14/09/2026). Viaja junto do
            # piso porque a ficha publica os DOIS: o compendio do gurami mel
            # recomenda "nao menos que 4 a 6 exemplares", e servir so o 4 e
            # publicar menos do que a fonte declarou.
            "cardume_ate": e.get("cardume_recomendado_ate"),
            "convivencia": e["convivencia"],
            "comportamento": e.get("comportamento") or "",
            "frente_cm": e["comprimento_minimo_aquario_cm"],
            "base_comprimento": base.get("comprimento"),
            "base_largura": base.get("largura"),
            # PARA QUEM A FONTE DECLAROU A BASE (esquema versao 5, 22/09/2026).
            # Viaja com os dois lados do chao porque e ele que decide se a ficha
            # pode servir o FUNDO ao arranjo que ela publica: o compendio declarou
            # os 60 x 30 cm do apistogramma agassizi para UM CASAL, e a ficha os
            # prometeu ao harem por oito dias. So os termos vem para o PHP — a
            # clausula transcrita e prova de banco, conferida pelo E22, e nao tem
            # o que fazer dentro do snippet.
            "chao_para": list((e.get("chao_declarado_para") or {}).get("arranjos") or []),
            "temp_min": e["temperatura_C"]["min"],
            "temp_max": e["temperatura_C"]["max"],
            "status": e.get("status_registro") or "",
            "fontes": fontes,
            "conflitos": conflitos,
        }

    """OS BARRADOS, na ordem de quem esta mais perto de entrar (decisao 6).

    A ordem e DERIVADA — quantos motivos faltam, e entre iguais o nome
    cientifico — e nunca a do arquivo do banco: quem le a lista quer saber
    quem esta a um campo de distancia, e ordem de arquivo e ordem de digitacao.
    """
    por_id = {e["id"]: e for e in banco["especies"]}
    barrados = {}
    for ident, faltando in fora:
        e = por_id[ident]
        if not e.get("nome_cientifico"):
            raise SystemExit(
                "ERRO: %s foi barrado e nao tem nome_cientifico — linha que nao\n"
                "  sabe nomear a especie e linha que o leitor nao pode conferir." % ident
            )
        codigos = []
        for bruto in faltando:
            codigo = codigo_de_motivo(bruto)
            if codigo not in codigos:
                codigos.append(codigo)
        barrados[ident] = {
            "id": ident,
            "cientifico": e["nome_cientifico"],
            "populares": list(e.get("nomes_populares_br") or []),
            "familia": e.get("familia") or "",
            "faltando": codigos,
        }
    barrados = dict(sorted(
        barrados.items(),
        key=lambda par: (len(par[1]["faltando"]), par[1]["cientifico"]),
    ))

    # A prova de que as duas listas sao disjuntas, feita aqui e nao confiada ao
    # `continue` do laco de cima: especie nos dois blocos apareceria na tabela E
    # na lista de ausentes da mesma pagina, que e a contradicao que a secao 7
    # nomeia ("negar e afirmar o mesmo fato em duas frases seguidas").
    nos_dois = sorted(set(dentro) & set(barrados))
    if nos_dois:
        raise SystemExit("ERRO: no catalogo E barrados ao mesmo tempo: %s" % ", ".join(nos_dois))
    if len(dentro) + len(barrados) != len(banco["especies"]):
        raise SystemExit(
            "ERRO: %d no catalogo + %d barrados nao fecham os %d registros do banco"
            % (len(dentro), len(barrados), len(banco["especies"]))
        )

    corpo = "\tstatic $catalogo = null;\n"
    corpo += "\tif ( null !== $catalogo ) {\n\t\treturn $catalogo;\n\t}\n"
    corpo += "\t$catalogo = " + php_valor(dentro, 1) + ";\n"
    corpo += "\treturn $catalogo;"

    corpo_barrados = "\tstatic $barrados = null;\n"
    corpo_barrados += "\tif ( null !== $barrados ) {\n\t\treturn $barrados;\n\t}\n"
    corpo_barrados += "\t$barrados = " + php_valor(barrados, 1) + ";\n"
    corpo_barrados += "\treturn $barrados;"

    with open(ALVO, encoding="utf-8") as f:
        php = f.read()
    php = escrever_bloco(php, INICIO, FIM, corpo)
    php = escrever_bloco(php, BARRADOS_INICIO, BARRADOS_FIM, corpo_barrados)
    with open(ALVO, "w", encoding="utf-8") as f:
        f.write(php)

    print("catalogo de especies: %d dentro, %d fora do portao de catalogo" % (len(dentro), len(fora)))
    print("banco: %d registros" % len(banco["especies"]))
    for ident, faltando in fora:
        print("  fora: %-32s %s" % (ident, ", ".join(faltando)))
    print("barrados no snippet: %d, com os motivos em codigo fechado" % len(barrados))
    for ident, b in barrados.items():
        print("  barrado: %-30s %s" % (ident, ", ".join(b["faltando"])))

    """Quem esta no catalogo e ainda assim NAO pode ter pagina propria.

    Isto e impresso porque e a lista de onde sai a proxima leva de malha. Sem
    ela a regra do cardume seria invisivel ate alguem escrever um registro no
    `aquametria_peixes_registro()` e o teste reprovar sem dizer por que.
    """
    sem_ficha = []
    for ident in dentro:
        falta = falta_para_virar_ficha(por_id[ident])
        if falta:
            sem_ficha.append((ident, falta))
    print("podem virar ficha: %d de %d no catalogo" % (len(dentro) - len(sem_ficha), len(dentro)))
    for ident, falta in sem_ficha:
        print("  sem pagina: %-30s %s" % (ident, ", ".join(falta)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
GERA dados/f1-respostas.json — tudo o que a F1 serve na tela.

NENHUM numero e NENHUMA frase de resposta da F1 e digitado dentro do snippet
PHP: tudo sai deste arquivo, que sai de regras/f1.py e de dados/constantes.json.
E o mesmo desenho da F2 desta ilha, pelo mesmo motivo da secao 8 do
ARQUIPELAGO.md.

AS DUAS GUARDAS DE TEXTO DE TELA SAO IMPORTADAS DA IRMA, nao reescritas.
`ferramentas/gerar-f2.py` tem `conferir_acento_na_tela()` e as duas listas
(PALAVRAS_DE_BASTIDOR e SEM_ACENTO_NA_TELA), e as duas cicatrizes que as
produziram sao de ARQUIVO indo para a TELA — exatamente o canal desta
ferramenta. Copia-las seria a 32.5-c acontecendo de novo: *"a regra deixou de
morar em dois lugares onde podia divergir"*. Importar da irma tem o custo de
acoplar dois geradores; duplicar tem o custo de uma delas envelhecer sozinha, e
esse e o custo que esta ilha ja pagou tres vezes.

E A GUARDA PEGOU ALGO NO DIA EM QUE ESTE ARQUIVO NASCEU: o campo `artigo` da
constante `consequencias-por-categoria-contran-996-2023` e TEXTO DE TELA, e a
primeira versao dele trazia a prosa inteira do registro — sem acento, porque os
arquivos de dado desta ilha sao ASCII de proposito. O smoke test de regras/f1.py
servia "a resolucao NAO diz qual" dentro de uma frase acentuada. O conserto foi
no DADO (o `artigo` ficou curto e acentuado, e o longo virou `artigo_detalhe`,
que nunca vai a tela), e esta guarda agora cobra isso em toda passada.

DOIS NUMEROS QUE ESTE GERADOR MEDE E QUE SAO A TESE DA ILHA:
  - `vitrine` nasce com ZERO cartoes, e a causa esta contada: NENHUM dos 17
    registros do banco declara `potencia_nominal_w`. A F1 nao tem o que vender
    porque o varejo nao declara o watt que a regra le — e a pagina diz isso com
    os nomes contados, em vez de nao ter bloco de compra e nao explicar.
  - a tabela de veiculos colhidos nasce com a coluna `categoria` cheia de
    recusa, e isso NAO e a tabela falhando: e a tabela sendo a prova da tese.
"""

import importlib.util
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(ILHA, "regras"))

import f1 as f1ref  # noqa: E402

SAIDA = os.path.join(ILHA, "dados", "f1-respostas.json")


def _irma():
    """Importa gerar-f2.py pelo caminho (o nome tem hifen e nao e identificador).

    So as guardas de texto de tela sao usadas daqui. O modulo nao executa nada
    ao ser importado: o `main()` dele esta sob `if __name__ == "__main__"`.
    """
    caminho = os.path.join(AQUI, "gerar-f2.py")
    spec = importlib.util.spec_from_file_location("gerar_f2", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


IRMA = _irma()
conferir_acento_na_tela = IRMA.conferir_acento_na_tela
PALAVRAS_DE_BASTIDOR = IRMA.PALAVRAS_DE_BASTIDOR


# O caso que a casca ja deixa preenchido no formulario (1.1 da especificacao).
# Os valores sao os do exemplo da propria especificacao, e o municipio nasce
# vazio de proposito: o terceiro estado da camada 2 (municipio conhecido com ato
# LIDO) nao existe no banco de hoje, e pre-preencher uma cidade faria a resposta
# de exemplo prometer um numero municipal que a ilha nao tem.
EXEMPLO = {
    "potencia_nominal_w": 500,
    "velocidade_max_kmh": 32,
    "acelerador": "manual",
    "municipio": "",
}

# A FAIXA DOS CAMPOS, para o formulario e para a bancada. Nao e grade sintetica
# de resposta (a 1.6 proibe): e o limite do que o campo aceita.
POTENCIAS_W = [250, 350, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000]
VELOCIDADES_KMH = [6, 20, 25, 32, 40, 45, 50, 60, 80]

ROTULOS = {
    "potencia_nominal_w": "Potência nominal (W)",
    "velocidade_max_kmh": "Velocidade máxima de fábrica (km/h)",
    "acelerador": "Tem acelerador?",
    "municipio": "Sua cidade (opcional)",
    "acelerador_manual": "Tem acelerador",
    "acelerador_so_pedal_assistido": "Só funciona pedalando",
    "titulo_categoria": "O que a resolução diz",
    "titulo_municipal": "E a rua, que é municipal",
    "titulo_ressalva": "Antes de usar esta resposta",
    "titulo_tabela_regra": "Os limites da resolução, do jeito que ela escreve",
    "titulo_tabela_banco": "O que os anúncios que a gente colheu declaram",
}


def fonte_na_tela_legal(cid, registro):
    """A frase de procedencia da regua legal, conferida contra bastidor.

    A irma tem um dicionario de frases de leitor por constante; estas duas
    constantes nasceram em 06/11/2026 e o `fonte` delas JA e frase de leitor,
    porque foi escrito sabendo que iria para a tela. O que esta funcao faz e
    cobrar isso, em vez de supor.
    """
    texto = registro.get("fonte") or ""
    for palavra in PALAVRAS_DE_BASTIDOR:
        assert palavra.lower() not in texto.lower(), (
            "32.4: a frase de procedencia de %r carrega a palavra de bastidor %r e "
            "ela iria para a tela: %r" % (cid, palavra, texto[:140]))
    return texto


def _valor(campo):
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def tabela_da_regra(constantes):
    """A tabela PRE-RENDERIZADA da regra: o que a resolucao poe em cada categoria.

    POR QUE ESTA TABELA EXISTE E A 1.6 NAO A PREVIA. A 1.6 pede uma tabela de
    "combinacoes reais colhidas no bloco 1" e proibe grade sintetica — e esta
    nao e nem uma nem outra: ela e a FONTE pre-renderizada, linha por categoria,
    com o artigo ao lado. E a metade que a visao geral de IA le sem preencher
    formulario, e e a unica coisa desta pagina que nao depende de o visitante
    saber os numeros do proprio veiculo. Nenhum numero aqui e digitado: todos
    saem da constante.
    """
    lim = f1ref.limiares_publicaveis(constantes)
    if lim is None:
        return None
    cons = f1ref.consequencias_publicaveis(constantes)

    def cm(mm):
        return f1ref._n(mm / 100)

    linhas = [
        {
            "categoria": "bicicleta_eletrica",
            "nome": f1ref.NOME_DA_CATEGORIA["bicicleta_eletrica"],
            "potencia_w": f1ref._n(lim["LIMIAR_BIKE_W"]),
            "velocidade_kmh": f1ref._n(lim["LIMIAR_BIKE_KMH"]),
            "acelerador": "não pode ter",
            "dimensao": "a resolução não limita",
            "placa": "não é sujeita a registro, licenciamento nem placa",
            "artigo": cons["bicicleta_eletrica"]["artigo"],
        },
        {
            "categoria": "autopropelido",
            "nome": f1ref.NOME_DA_CATEGORIA["autopropelido"],
            "potencia_w": f1ref._n(lim["LIMIAR_AUTOPROP_W"]),
            "velocidade_kmh": f1ref._n(lim["LIMIAR_AUTOPROP_KMH"]),
            "acelerador": "pode ter",
            "dimensao": "até %s cm de largura e %s cm entre eixos"
                        % (cm(lim["LIMIAR_AUTOPROP_LARGURA_MM"]),
                           cm(lim["LIMIAR_AUTOPROP_ENTRE_EIXOS_MM"])),
            "placa": "não é sujeito a registro, licenciamento nem placa",
            "artigo": cons["autopropelido"]["artigo"],
        },
        {
            "categoria": "ciclomotor",
            "nome": f1ref.NOME_DA_CATEGORIA["ciclomotor"],
            "potencia_w": f1ref._n(lim["LIMIAR_CICLOMOTOR_W"]),
            "velocidade_kmh": f1ref._n(lim["LIMIAR_CICLOMOTOR_KMH"]),
            "acelerador": "pode ter",
            "dimensao": "a resolução não limita",
            "placa": "registrado e licenciado, e com capacete",
            "artigo": cons["ciclomotor"]["artigo"],
        },
        {
            "categoria": "acima_do_ciclomotor",
            "nome": "acima disso",
            "potencia_w": "mais de %s" % f1ref._n(lim["LIMIAR_CICLOMOTOR_W"]),
            "velocidade_kmh": "mais de %s" % f1ref._n(lim["LIMIAR_CICLOMOTOR_KMH"]),
            "acelerador": "—",
            "dimensao": "—",
            "placa": "motocicleta, motoneta ou triciclo, conforme o caso — e a "
                     "resolução não diz qual",
            "artigo": cons["acima_do_ciclomotor"]["artigo"],
        },
    ]
    return linhas


def tabela_do_banco(veiculos, constantes):
    """A tabela da 1.6: os veiculos COLHIDOS, com o que a ficha declara.

    A 1.6 dizia *"a coluna categoria desta tabela esta VAZIA neste bloco, e isso
    e proposital. Ela so pode ser preenchida pelos limiares da 1.3"*. Os
    limiares chegaram, e a coluna nasce — com o que a arvore devolve PARA CADA
    REGISTRO, que em 06/11/2026 e recusa em todos, porque nenhum declara o watt
    nominal. A coluna nao e deixada vazia e nao e preenchida com o watt sem
    rotulo: ela diz o nome da causa, e e por isso que esta tabela e a prova da
    tese da ilha e nao um buraco nela.
    """
    lim = f1ref.limiares_publicaveis(constantes)
    linhas = []
    for r in veiculos["registros"]:
        if r.get("status") == "excluido_do_banco":
            continue
        w_nom = _valor(r.get("potencia_nominal_w"))
        w_sem = _valor(r.get("potencia_declarada_sem_rotulo_w"))
        w_pico = _valor(r.get("potencia_pico_w"))
        kmh = _valor(r.get("velocidade_max_kmh"))
        acel = _valor(r.get("acelerador"))
        v = f1ref.classificar(w_nom, kmh, acel, lim)

        fontes = r.get("fontes") or {}
        primeira = None
        for k in fontes:
            primeira = fontes[k]
            break

        linhas.append({
            "id": r.get("id"),
            "rotulo": (" ".join(x for x in (r.get("marca"), r.get("modelo")) if x)
                       or (r.get("titulo_colhido") or "")[:60]),
            "titulo_colhido": r.get("titulo_colhido"),
            "watt_nominal": None if w_nom is None else f1ref._n(
                f1ref.Fraction(str(w_nom))),
            "watt_sem_rotulo": None if w_sem is None else f1ref._n(
                f1ref.Fraction(str(w_sem))),
            "watt_pico": None if w_pico is None else f1ref._n(
                f1ref.Fraction(str(w_pico))),
            "velocidade_kmh": None if kmh is None else f1ref._n(
                f1ref.Fraction(str(kmh))),
            "acelerador": acel,
            "categoria": v["categoria"],
            "categoria_nome": (f1ref.NOME_DA_CATEGORIA[v["categoria"]]
                               if v["categoria"] else None),
            "causa_da_recusa": v["causa"],
            "fonte_tipo": (primeira or {}).get("tipo"),
            "data_leitura": (primeira or {}).get("data_leitura"),
        })
    return linhas


def frase_do_bloco_de_compra(grupos, categoria_pedida):
    """A frase de abertura do bloco de compra, DERIVADA da contagem.

    A irma desta funcao nasceu em 29/10/2026 na F2 por um defeito medido: a
    frase era string digitada no PHP, e portanto uma afirmacao sobre o estado do
    banco que nenhum portao conferia. Aqui ela nasce derivada desde o primeiro
    dia, com as quatro saidas escolhidas pela CONTAGEM e nunca pela intencao.
    """
    cabem = len(grupos["cabem_na_categoria"])
    sem_ficha = len(grupos["nao_declaram_nominal"])
    outra = len(grupos["de_outra_categoria"])
    nome = f1ref.NOME_DA_CATEGORIA.get(categoria_pedida, "") if categoria_pedida else ""

    if cabem:
        return ("Dos anúncios que a gente colheu, %d declara%s os números que a "
                "regra lê e cai%s nesta categoria."
                % (cabem, "m" if cabem > 1 else "", "em" if cabem > 1 else ""))
    if sem_ficha and not outra:
        return ("Não temos o que recomendar aqui, e a causa é de ficha e não "
                "de estoque: nenhum dos %d anúncios que a gente colheu declara a "
                "potência NOMINAL. Todos declaram um watt sem dizer se é nominal "
                "ou de pico — e esse número a regra não lê."
                % sem_ficha)
    if outra and not cabem:
        return ("Nenhum dos anúncios colhidos cai em %s: %d dele%s classifica%s "
                "noutra categoria e %d não declara%s a potência nominal."
                % (nome, outra, "s" if outra > 1 else "", "m" if outra > 1 else "",
                   sem_ficha, "m" if sem_ficha != 1 else ""))
    return ("Ainda não temos anúncio colhido para esta categoria, e a página "
            "diz isso em vez de oferecer outra coisa.")


def montar(constantes, veiculos, municipios):
    lim = f1ref.limiares_publicaveis(constantes)
    exemplo = f1ref.responder(
        EXEMPLO["potencia_nominal_w"], EXEMPLO["velocidade_max_kmh"],
        EXEMPLO["acelerador"], EXEMPLO["municipio"],
        constantes=constantes, municipios=municipios)

    grupos = f1ref.grupos_de_compra(
        veiculos["registros"], exemplo["categoria"], lim)

    linhas_regra = tabela_da_regra(constantes)
    linhas_banco = tabela_do_banco(veiculos, constantes)

    # ---- TODO texto que a tela serve passa pelas duas guardas, aqui, ANTES de
    # ser gravado. Portao no ponto em que o dado vira texto, nunca no ponto em
    # que o texto e impresso.
    textos = [("molde %s" % k, v) for k, v in f1ref.MOLDES.items()]
    textos += [("rotulo %s" % k, v) for k, v in ROTULOS.items()]
    textos += [("frase de exemplo", f) for f in
               exemplo["frases_categoria"] + exemplo["frases_municipal"]
               + exemplo["frases_ressalva"]]
    textos += [("frase de abertura da compra",
                frase_do_bloco_de_compra(grupos, exemplo["categoria"]))]
    for linha in (linhas_regra or []):
        for k, v in linha.items():
            if isinstance(v, str) and k != "categoria":
                textos.append(("tabela da regra, %s de %s" % (k, linha["categoria"]), v))
    conferir_acento_na_tela(textos)
    for onde, texto in textos:
        for palavra in PALAVRAS_DE_BASTIDOR:
            assert palavra.lower() not in texto.lower(), (
                "32.4: %s carrega a palavra de bastidor %r e ela iria para a tela: %r"
                % (onde, palavra, texto[:140]))

    constantes_na_tela = {}
    for cid in (f1ref.ID_LIMIARES, f1ref.ID_CONSEQUENCIAS, f1ref.ID_HABILITACAO,
                f1ref.ID_ASSISTENCIA_A_PE, f1ref.ID_ALTERACAO, f1ref.ID_WATT_SEM_ROTULO):
        reg = constantes[cid]
        constantes_na_tela[cid] = {
            "valor": reg.get("valor"),
            "status": reg.get("status"),
            "tipo": reg.get("tipo"),
            "fonte": fonte_na_tela_legal(cid, reg),
            "url": reg.get("url"),
            "verificado_em": reg.get("verificado_em"),
        }

    return {
        "id": "f1-respostas",
        "ilha": "rodametria",
        "ferramenta": "F1",
        "bloco": "4",
        "gerado_em": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%d"),
        "gerado_por": "ferramentas/gerar-f1.py",
        "referencia": "regras/f1.py",
        "especificacao": "dados/especificacao-calculadoras.md, secao 1",
        "publicar": True,
        "nota": "Tudo que a F1 serve na tela sai daqui: nenhum numero e nenhuma "
                "frase da F1 e digitado dentro do snippet PHP. Os limiares legais "
                "saem da constante `limiares-categoria-contran-996-2023`, lida no "
                "PDF oficial da Resolucao Contran 996/2023 em 05/11/2026; as "
                "consequencias por categoria saem de "
                "`consequencias-por-categoria-contran-996-2023`; e a exigencia de "
                "HABILITACAO nao sai de nenhuma, porque a resolucao nao a declara — "
                "a F1 cala sobre CNH e nomeia a causa.",
        "campos": {
            "potencias_w": POTENCIAS_W,
            "velocidades_kmh": VELOCIDADES_KMH,
            "aceleradores": list(f1ref.ACELERADORES),
            "exemplo": EXEMPLO,
        },
        "rotulos": ROTULOS,
        "categorias": list(f1ref.CATEGORIAS),
        "nome_da_categoria": dict(f1ref.NOME_DA_CATEGORIA),
        "constantes_usadas": constantes_na_tela,
        "limiares": (None if lim is None
                     else {k: str(v) for k, v in lim.items()}),
        "limiares_tela": (None if lim is None
                          else {k: f1ref._n(v) for k, v in lim.items()}),
        "habilitacao_respondida": f1ref.habilitacao_publicavel(constantes) is not None,
        # Os moldes viajam INTEIROS, de um lugar so: e deles que o navegador
        # monta a resposta quando a pessoa troca um campo, e e deles que o PHP
        # monta a resposta pre-renderizada. Duas metades lendo o mesmo molde nao
        # podem dizer coisas diferentes para a mesma entrada.
        "frases_molde": dict(f1ref.MOLDES),
        # OS FATOS DAS RESSALVAS SAO CONSTANTES, e por isso aparecem junto das
        # outras em `constantes_usadas` em vez de num campo proprio. O campo
        # proprio existiu por meia hora em 06/11/2026, quando eles moravam
        # dentro de regras/f1.py, e o portao da ferramenta os mandou para o
        # arquivo de dado — o que os poe automaticamente neste laco.
        "resposta_exemplo": {
            "entrada": exemplo["entrada"],
            "classifica": exemplo["classifica"],
            "categoria": exemplo["categoria"],
            "categoria_nome": exemplo["categoria_nome"],
            "causa_da_recusa": exemplo["causa_da_recusa"],
            "tom": exemplo["tom"],
            "frases_categoria": exemplo["frases_categoria"],
            "frases_municipal": exemplo["frases_municipal"],
            "frases_ressalva": exemplo["frases_ressalva"],
        },
        "tabela_regra": linhas_regra,
        "tabela_banco": {
            "linhas": linhas_banco,
            "total": len(linhas_banco),
            "com_nominal": sum(1 for l in linhas_banco if l["watt_nominal"]),
            "classificaveis": sum(1 for l in linhas_banco if l["categoria"]),
        },
        "compra": {
            "vitrine": [
                {
                    "id": r.get("id"),
                    "nome": " ".join(x for x in (r.get("marca"), r.get("modelo")) if x),
                }
                for r in grupos["cabem_na_categoria"]
            ],
            "frase_de_abertura": frase_do_bloco_de_compra(grupos, exemplo["categoria"]),
            "grupos": {k: [r.get("id") for r in v] for k, v in grupos.items()},
            "contagem": {k: len(v) for k, v in grupos.items()},
            "nomes_por_grupo": {
                k: [" ".join(x for x in (r.get("marca"), r.get("modelo")) if x)
                    or (r.get("titulo_colhido") or "")[:60] for r in v]
                for k, v in grupos.items()
            },
            "total_registros_veiculos": len(veiculos["registros"]),
        },
    }


def main():
    conferir = "--conferir" in sys.argv
    constantes = f1ref.carregar_constantes()
    with open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
        veiculos = json.load(f)
    with open(os.path.join(ILHA, "dados", "municipios.json"), encoding="utf-8") as f:
        municipios = json.load(f)["registros"]

    novo = montar(constantes, veiculos, municipios)
    texto = json.dumps(novo, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            print("REPROVADO: %s nao existe. Rode sem --conferir." % SAIDA)
            return 1
        atual = open(SAIDA, encoding="utf-8").read()

        # O SELO `gerado_em` SAI DA COMPARACAO, pela MESMA medicao que tirou o da
        # irma em 30/10/2026: ele e o relogio da execucao e nao entra em nada que
        # a F1 calcula, entao compara-lo reprovaria a pagina CERTA todo dia
        # seguinte ao que ela foi gerada. A lição nao foi inferida aqui: ela esta
        # medida no comentario de `ferramentas/gerar-f2.py`.
        def sem_selo(bruto, rotulo):
            try:
                d = json.loads(bruto)
            except ValueError as e:
                print("REPROVADO: %s nao e JSON legivel (%s): %s" % (rotulo, SAIDA, e))
                return None
            d["gerado_em"] = "<selo-fora-da-comparacao>"
            return json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True)

        a, b = sem_selo(atual, "o arquivo gravado"), sem_selo(texto, "a referencia")
        if a is None:
            return 1
        if a != b:
            print("REPROVADO: dados/f1-respostas.json esta diferente do que a "
                  "referencia produz agora, FORA do selo `gerado_em`. Rode "
                  "`python3 ferramentas/gerar-f1.py`.")
            return 1
        print("APROVADO: dados/f1-respostas.json bate com a referencia "
              "(o selo `gerado_em` fica fora da comparacao, de proposito).")
        return 0

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    c = novo["compra"]["contagem"]
    t = novo["tabela_banco"]
    print("gravado %s" % SAIDA)
    print("  limiares: %s" % ("LIDOS, a F1 pode ir ao ar" if novo["limiares"]
                              else "PENDENTES, a F1 nao vai ao ar"))
    print("  habilitacao (CNH): %s" % ("respondida" if novo["habilitacao_respondida"]
                                       else "NAO respondida, e a pagina diz isso"))
    print("  tabela da regra: %d linha(s)" % len(novo["tabela_regra"] or []))
    print("  tabela do banco: %d linha(s), %d com watt NOMINAL, %d classificavel(eis)"
          % (t["total"], t["com_nominal"], t["classificaveis"]))
    print("  vitrine: %d cartao(oes)" % len(novo["compra"]["vitrine"]))
    print("  prestacao de contas (soma fecha %d registros): %s"
          % (novo["compra"]["total_registros_veiculos"], c))
    return 0


if __name__ == "__main__":
    sys.exit(main())

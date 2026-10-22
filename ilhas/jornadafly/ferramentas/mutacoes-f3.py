#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F3 de proposito e verifica que ferramentas/teste-f3.py reprova.

    python3 ferramentas/mutacoes-f3.py

Sai com codigo 1 se qualquer mutacao decidir errado.

Quatro tipos, os mesmos das baterias da F1 e da F2:

  MUNDOS (esperam PASSAR) -- carregam passe e cobertura EM MEMORIA e exigem que o
  portao os aprove. Aqui eles valem mais do que em qualquer bateria desta pasta,
  porque o banco tem ZERO passes e ZERO coberturas: sem os mundos, a ferramenta
  INTEIRA -- valor entregue, ponto de equilibrio, os tres desfechos do veredito, a
  leitura da hedge do desconto -- nunca seria executada por ninguem, e o dia da
  primeira carga seria o dia de descobrir que estava errada. Nenhuma linha e gravada
  no banco de verdade.

  QUEBRAS DE REFERENCIA (esperam REPROVAR) -- editam o CODIGO da f3-referencia.py.
  Cada uma declara a FRASE que espera ouvir de volta, porque reprovar nao e a mesma
  coisa que reprovar PELO MOTIVO CERTO.

  QUEBRAS DE ESQUEMA (esperam REPROVAR) -- mexem no esquema, nao no codigo.

  MORTES (esperam MORRER) -- tiram do esquema uma chave de que a F3 depende e exigem
  que ela LEVANTE em vez de cair num literal.

TRAVA DE ALVO EXATO: toda quebra de referencia declara o TEXTO que vai editar, e
`_referencia_mutada` RECUSA OPERAR se o texto nao estiver mais la. Quando a regra
muda de linha, a mutacao que editava a linha antiga vira INERTE, e sem a trava ela
passa medindo nada enquanto o relatorio diz "0 sobrevivente".
"""

import copy
import importlib.util
import io
import json
import os
import sys
import types
from datetime import date

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

REFERENCIA = os.path.join(AQUI, "f3-referencia.py")

# A DATA E FIXA NESTA BATERIA, e isso e decisao: o vencimento do preco e uma das
# regras medidas aqui, e bateria que toma a data do sistema muda de resultado sozinha
# na virada de um dia qualquer. Fixada no dia em que esta bateria nasceu.
HOJE = date(2026, 10, 22)


def _ler(nome):
    with io.open(os.path.join(DADOS, nome), encoding="utf-8") as f:
        return json.load(f)


def _modulo(arquivo, nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arquivo))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _portao():
    return _modulo("teste-f3.py", "teste_f3")


def _gerador():
    return _modulo("gerar-f3.py", "gerar_f3")


FONTE_DA_REFERENCIA = io.open(REFERENCIA, encoding="utf-8").read()


def _referencia_mutada(trocas=()):
    """Carrega a f3-referencia.py com o codigo editado, de um texto em memoria."""
    fonte = FONTE_DA_REFERENCIA
    for antes, depois in trocas:
        quantas = fonte.count(antes)
        if quantas != 1:
            raise SystemExit(
                "MUTACAO INERTE: o alvo %r aparece %d vezes na f3-referencia.py (tem de "
                "aparecer 1). A regra mudou de linha e esta mutacao parou de medir o que "
                "diz medir." % (antes[:70], quantas))
        fonte = fonte.replace(antes, depois)
    modulo = types.ModuleType("f3_referencia_mutada")
    modulo.__file__ = REFERENCIA
    exec(compile(fonte, REFERENCIA, "exec"), modulo.__dict__)
    return modulo


# ---------------------------------------------------------------------------
# AS PECAS DOS MUNDOS
#
# Nenhuma delas e dado real e NENHUMA e gravada: sao mundos de bancada. O passe mora
# em ROMA porque e a cidade do banco que tem uma atracao cuja cobertura faz sentido
# (o ingresso do Coliseu), e cobertura precisa dos DOIS lados para existir.
# ---------------------------------------------------------------------------

def _fonte_de_bancada():
    return {
        "id": "passe-de-bancada-fonte",
        "nivel": 4,
        "origem": "operador-via-busca",
        "leitura": "busca_web",
        "autor": "operador de passe de bancada",
        "documento": "pagina de tarifas de bancada",
        "url": None,
        "motivo_sem_url": "mundo de bancada",
        "data_leitura": "2026-10-20",
    }


def _versao_do_passe(vid, rotulo, preco, dias):
    return {
        "id": vid, "rotulo": rotulo, "preco": preco, "moeda": "EUR",
        "unidade_de_preco": "por_pessoa", "unidade_de_preco_declarada_por":
            "no_texto_da_fonte",
        "capacidade_maxima": None, "capacidade_maxima_declarada_por": None,
        "duracao_minutos": None,
        "motivo_sem_duracao": "passe tem validade, nao duracao de passeio",
        "momento_do_dia": "qualquer", "acrescimos": [],
        "inclui": ["entrada nas atracoes cobertas"], "nao_inclui": [],
        "nao_inclui_motivo_lista_vazia": "mundo de bancada",
        "fonte": "passe-de-bancada-fonte", "data_leitura": "2026-10-20",
        "declarado_como": "%d euros por pessoa, validade de %d dias" % (preco, dias),
        "dias_de_uso": dias,
        "dias_de_uso_transcrito_de": "a frase declarada deste mundo de bancada",
        "faixa_etaria": None,
        "motivo_sem_faixa_etaria": "mundo de bancada",
        "faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu": [],
    }


def _passe_em_roma(banco, versoes=None, declaradas=2, status="publicavel"):
    banco["fontes"].append(_fonte_de_bancada())
    banco["experiencias"].append({
        "id": "roma-passe-de-bancada",
        "nome": "Passe de Roma (mundo de bancada)",
        "cidade": "roma",
        "categoria": "passe_de_cidade",
        "eixo_das_versoes": "por_quantidade",
        "nota_do_eixo_das_versoes": "validades do mesmo passe: mais da mesma coisa.",
        "operador": {"nome": "operador de passe de bancada",
                     "tipo": "concessionaria_de_bem_publico",
                     "url": None, "motivo_sem_url": "mundo de bancada"},
        "versoes": versoes if versoes is not None else [
            _versao_do_passe("48h", "2 dias", 16, 2),
            _versao_do_passe("72h", "3 dias", 20, 3),
            _versao_do_passe("96h", "4 dias", 40, 4)],
        "temporada": None, "motivo_sem_temporada": "mundo de bancada",
        "imagem": None, "motivo_sem_imagem": "mundo de bancada",
        "declaracoes": [], "motivo_sem_declaracoes": "mundo de bancada",
        "resolucao": None, "motivo_sem_resolucao": "mundo de bancada",
        "afiliado": {"programa": None, "url": "", "url_produto": None,
                     "motivo_sem_url_produto": "mundo de bancada",
                     "url_busca_produto": "https://civitatis.com/br/roma/",
                     "rel": "nofollow noopener", "intestavel": False},
        "status": status,
        "entra_por": "mundo de bancada",
        "atracoes_declaradas_pelo_passe": declaradas,
        "atracoes_declaradas_transcrito_de": "o passe da entrada em %d atracoes" % declaradas,
    })
    return banco


def _cobertura(**campos):
    base = {
        "id": "bancada-cob-coliseu",
        "passe": "roma-passe-de-bancada",
        "experiencia": "roma-coliseu-ingresso",
        "versao_coberta": "padrao-24h",
        "motivo_sem_versao_coberta": None,
        "como": "entrada_incluida",
        "reserva_obrigatoria": False,
        "reserva_transcrita_de": None,
        "desconto_percentual": None,
        "desconto_e_no_maximo": None,
        "desconto_transcrito_de": None,
        "declarada_por": "no_texto_da_fonte",
        "fonte": "passe-de-bancada-fonte",
        "data_leitura": "2026-10-20",
        "status": "publicavel",
    }
    base.update(campos)
    return base


# ---------------------------------------------------------------------------
# OS MUNDOS
# ---------------------------------------------------------------------------

def mundo_passe_sem_cobertura(banco, esquema, constantes):
    """Passe lido e cobertura nao lida: preco publicado, veredito NEGADO."""
    _passe_em_roma(banco)
    return banco, esquema, constantes


def mundo_passe_com_cobertura(banco, esquema, constantes):
    """O mundo inteiro: passe de tres validades e a cobertura do Coliseu.

    Com o ingresso comum coberto (18 por pessoa) e o passe em 16, 20 e 40, os TRES
    desfechos do veredito aparecem na mesma passada para 1 pessoa.
    """
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura()]
    return banco, esquema, constantes


def mundo_cobertura_sem_versao(banco, esquema, constantes):
    """A fonte do passe nao diz qual bilhete: o valor entregue e FAIXA."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(
        versao_coberta=None,
        motivo_sem_versao_coberta="a fonte escreve «entrada no Coliseu» e ele tem dois "
                                  "bilhetes")]
    return banco, esquema, constantes


def mundo_desconto_que_e_teto(banco, esquema, constantes):
    """«Ate 50%»: o valor entregue vai de ZERO ao teto. A terceira regra."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=True,
        desconto_transcrito_de="até 50% de desconto na entrada")]
    return banco, esquema, constantes


def mundo_desconto_cheio(banco, esquema, constantes):
    """Desconto percentual cheio: as duas pontas abatidas."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=False,
        desconto_transcrito_de="50% de desconto na entrada")]
    return banco, esquema, constantes


def mundo_cobertura_sem_efeito_no_preco(banco, esquema, constantes):
    """Fila preferencial: entrega ZERO, e zero declarado nao e ausencia."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(como="sem_efeito_no_preco")]
    return banco, esquema, constantes


def mundo_cobertura_com_reserva_obrigatoria(banco, esquema, constantes):
    """A regra que envelhece primeiro vai para a tela com a frase da fonte."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(
        reserva_obrigatoria=True,
        reserva_transcrita_de="a reserva de horário é obrigatória e feita à parte")]
    return banco, esquema, constantes


def mundo_passe_de_uma_validade_so(banco, esquema, constantes):
    """Passe de UMA versao: eixo null com `dias_de_uso` preenchido."""
    _passe_em_roma(banco, versoes=[_versao_do_passe("72h", "3 dias", 20, 3)])
    passe = banco["experiencias"][-1]
    passe["eixo_das_versoes"] = None
    del passe["nota_do_eixo_das_versoes"]
    passe["motivo_sem_eixo_das_versoes"] = "uma validade so"
    banco["coberturas_de_passe"] = [_cobertura()]
    return banco, esquema, constantes


def mundo_passe_sem_validade_lida(banco, esquema, constantes):
    """A validade do passe nao foi lida: a F3 nao diz se ele cobre a estadia."""
    versao = _versao_do_passe("unica", "o passe", 20, 3)
    versao["dias_de_uso"] = None
    versao["motivo_sem_dias_de_uso"] = "a fonte nao declara validade"
    del versao["dias_de_uso_transcrito_de"]
    _passe_em_roma(banco, versoes=[versao])
    passe = banco["experiencias"][-1]
    passe["eixo_das_versoes"] = None
    del passe["nota_do_eixo_das_versoes"]
    passe["motivo_sem_eixo_das_versoes"] = "uma validade so"
    banco["coberturas_de_passe"] = [_cobertura()]
    return banco, esquema, constantes


def mundo_passe_excluido_do_banco(banco, esquema, constantes):
    """Passe descartado: ele nao aparece, e a F3 diz que nao leu passe nenhum."""
    _passe_em_roma(banco, status="excluido_do_banco")
    banco["coberturas_de_passe"] = [_cobertura()]
    return banco, esquema, constantes


def mundo_cobertura_excluida_do_banco(banco, esquema, constantes):
    """Cobertura descartada conta como NAO LIDA, nunca como nao coberta."""
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [_cobertura(status="excluido_do_banco")]
    return banco, esquema, constantes


def mundo_duas_atracoes_em_roma(banco, esquema, constantes):
    """Roma com DUAS atracoes: o dominio deixa de ter um subconjunto so.

    O banco de hoje tem UMA atracao por cidade, entao a combinacao de atracoes --
    que e a entrada propria desta ferramenta -- nunca e exercitada pela grade real.
    """
    coliseu = copy.deepcopy(
        next(e for e in banco["experiencias"] if e["id"] == "roma-coliseu-ingresso"))
    coliseu["id"] = "roma-coliseu-de-bancada"
    coliseu["nome"] = "Segunda atração de Roma (mundo de bancada)"
    for v in coliseu["versoes"]:
        v["preco"] = 12
    banco["experiencias"].append(coliseu)
    _passe_em_roma(banco)
    banco["coberturas_de_passe"] = [
        _cobertura(),
        _cobertura(id="bancada-cob-segunda", experiencia="roma-coliseu-de-bancada",
                   versao_coberta="padrao-24h"),
    ]
    return banco, esquema, constantes


def mundo_preco_do_passe_vencido(banco, esquema, constantes):
    """Preco do passe lido ha mais de 60 dias: a F3 diz que a conta e do dia da leitura."""
    versoes = [_versao_do_passe("72h", "3 dias", 20, 3)]
    versoes[0]["data_leitura"] = "2026-01-01"
    _passe_em_roma(banco, versoes=versoes)
    passe = banco["experiencias"][-1]
    passe["eixo_das_versoes"] = None
    del passe["nota_do_eixo_das_versoes"]
    passe["motivo_sem_eixo_das_versoes"] = "uma validade so"
    banco["coberturas_de_passe"] = [_cobertura()]
    return banco, esquema, constantes


MUNDOS = [
    ("passe lido e cobertura NAO lida", mundo_passe_sem_cobertura),
    ("passe com cobertura: os tres desfechos", mundo_passe_com_cobertura),
    ("cobertura que nao diz qual bilhete", mundo_cobertura_sem_versao),
    ("desconto que e TETO («ate 50%»)", mundo_desconto_que_e_teto),
    ("desconto percentual cheio", mundo_desconto_cheio),
    ("cobertura sem efeito no preco (fila)", mundo_cobertura_sem_efeito_no_preco),
    ("cobertura com reserva obrigatoria", mundo_cobertura_com_reserva_obrigatoria),
    ("passe de UMA validade (eixo null)", mundo_passe_de_uma_validade_so),
    ("passe sem validade lida", mundo_passe_sem_validade_lida),
    ("passe excluido do banco", mundo_passe_excluido_do_banco),
    ("cobertura excluida do banco", mundo_cobertura_excluida_do_banco),
    ("Roma com DUAS atracoes", mundo_duas_atracoes_em_roma),
    ("preco do passe VENCIDO", mundo_preco_do_passe_vencido),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS DE REFERENCIA — (nome, trocas, frase esperada, mundo)
# ---------------------------------------------------------------------------

QUEBRAS_DE_REFERENCIA = [
    ("a HEDGE do desconto virada numero cheio: «ate 50%» entrega 50%",
     [("            return Decimal(0), teto * fator",
       "            return piso * fator, teto * fator")],
     "desconto que e TETO tem de comecar em ZERO", None),

    ("beneficio de fila contado como DINHEIRO",
     [("        return Decimal(0), Decimal(0)", "        return piso, teto")],
     "sem efeito no preco tem de entregar ZERO", None),

    ("a entrada incluida entrega METADE do avulso",
     [("    if como == \"entrada_incluida\":\n        return piso, teto",
       "    if como == \"entrada_incluida\":\n        return piso / 2, teto / 2")],
     "a conta a mao da", None),

    ("o equilibrio ordena das mais BARATAS para as mais caras",
     [("                   key=lambda i: (-Decimal(str(valores[i])), i))",
       "                   key=lambda i: (Decimal(str(valores[i])), i))")],
     "a conta a mao da", None),

    ("o equilibrio exige passar do preco em vez de alcanca-lo",
     [("        if acumulado >= preco:", "        if acumulado > preco:")],
     "a conta a mao da", None),

    ("o equilibrio de lista vazia devolve ZERO atracoes",
     [("    if not valores:\n        return None",
       "    if not valores:\n        return {\"quantas\": 0, \"acumulado\": Decimal(0), "
       "\"ordem\": []}")],
     "lista vazia tem de dar None", None),

    ("a ordem devolvida pelo equilibrio nao e a que ele usou",
     [("            return {\"quantas\": posicao, \"acumulado\": acumulado,\n"
       "                    \"ordem\": [ordem[i] for i in range(posicao)]}",
       "            return {\"quantas\": posicao, \"acumulado\": acumulado,\n"
       "                    \"ordem\": list(range(len(valores)))}")],
     "a ordem tem", None),

    ("o veredito perde o terceiro desfecho e vira sim-ou-nao",
     [("    if teto >= preco:\n        return \"depende_da_versao\", None",
       "    if False:\n        return \"depende_da_versao\", None")],
     "depende_da_versao", None),

    ("o veredito diz PAGA quando a ponta de CIMA alcanca",
     [("    if piso >= preco:\n        return \"paga\", piso - preco",
       "    if teto >= preco:\n        return \"paga\", teto - preco")],
     "veredito", None),

    ("cobertura DESCARTADA do banco volta a valer",
     [("        if cob.get(\"status\") == \"excluido_do_banco\":\n            continue\n"
       "        return cob",
       "        return cob")],
     "NAO LIDA", None),

    ("a atracao sem cobertura lida entra como COBERTA",
     [("            nao_lidas.append(atracao_id)\n            continue",
       "            lidas.append((atracao_id, {\"como\": \"entrada_incluida\", "
       "\"versao_coberta\": None, \"motivo_sem_versao_coberta\": \"suposto\", "
       "\"reserva_obrigatoria\": False, \"data_leitura\": \"2026-10-20\"}))\n"
       "            continue")],
     "entrou no valor entregue", mundo_passe_sem_cobertura),

    ("a cobertura nao lida fica SEM NOME na tela",
     [("    if nao_lidas:", "    if False:")],
     "nao NOMEOU isso", None),

    ("a base do equilibrio nao e declarada: a conta parece ser do passe inteiro",
     [("    elif isinstance(declaradas, int) and declaradas > todas_as_lidas:",
       "    elif False:")],
     "nao disse sobre quantas", None),

    ("passe sem cobertura nenhuma ganha VEREDITO",
     [("        if not entregas:", "        if False:")],
     "publicou veredito sobre um passe cuja cobertura ninguem leu", None),

    ("a ausencia de passe lido fica calada",
     [("    if not lista_de_passes:", "    if False:")],
     "NAO disse isso", None),

    ("a ausencia de passe lido vira frase de INEXISTENCIA",
     [("               \"Esta ilha ainda não leu nenhum passe de %s. Isso não quer dizer "
       "que %s \"\n               \"não tenha passe: quer dizer que esta ilha não leu o "
       "preço de nenhum na \"",
       "               \"Esta ilha ainda não leu nenhum passe de %s. %s \"\n"
       "               \"não tem passe: esta ilha não leu o preço de nenhum na \"")],
     "afirma INEXISTENCIA", None),

    ("o passe escolhido como atracao passa a ser aceito",
     [("        if existe is not None and existe.get(\"categoria\") == f2.CATEGORIA_DE_PASSE:",
       "        if False:")],
     "recusou por", mundo_passe_com_cobertura),

    ("atracao REPETIDA deixa de ser recusada e a conta soma duas vezes",
     [("    if len(escolhidas) != len(set(escolhidas)):", "    if False:")],
     "estado fora da faixa e a F3 NAO recusou", None),

    ("escolha VAZIA deixa de ser recusada",
     [("    if not escolhidas:", "    if False:")],
     "estado fora da faixa e a F3 NAO recusou", None),

    ("os subconjuntos passam a incluir a escolha VAZIA",
     [("    for mascara in range(1, 1 << total):", "    for mascara in range(0, 1 << total):")],
     "devolveu a escolha VAZIA", None),

    ("a versao NOMEADA pela cobertura e ignorada e o valor volta a ser faixa",
     [("        if versao_coberta is not None:", "        if False:")],
     "a conta a mao da 68 a 82", None),



    ("o teto de atracoes da tela sobe sem passar pela especificacao",
     [("ATRACOES_MAXIMO = 8", "ATRACOES_MAXIMO = 12")],
     "a especificacao diz 8", None),

    ("a faixa de dias da F3 deixa de ser a da F2",
     [("DIAS_MAXIMO = f2.DIAS_MAXIMO", "DIAS_MAXIMO = 60")],
     "a especificacao diz de 1 a 21", None),
]


# As DUAS metades da regra de validade do preco, quebradas uma por vez. A frase
# esperada e sempre a da secao 6 do portao, que compara o veredito da F3 com o do
# validador: elas discordarem quer dizer que uma das duas esta errada e nenhuma sabe.
QUEBRAS_DA_VALIDADE = [
    ("o preco vence no dia EXATO em vez de depois dele",
     [("    return passados > dias, passados, dias",
       "    return passados >= dias, passados, dias")],
     "preco_vencido com"),

    ("as duas janelas de validade trocadas de lugar",
     [("    if \"poder-publico\" in origem:\n        dias = validade.get"
       "(\"tarifa_de_poder_publico_dias\")\n    else:\n        dias = validade.get"
       "(\"operador_privado_dias\")",
       "    if \"poder-publico\" in origem:\n        dias = validade.get"
       "(\"operador_privado_dias\")\n    else:\n        dias = validade.get"
       "(\"tarifa_de_poder_publico_dias\")")],
     "tem de valer"),
]

F1 = os.path.join(AQUI, "f1-referencia.py")
FONTE_DA_F1 = io.open(F1, encoding="utf-8").read()


# ---------------------------------------------------------------------------
# AS MORTES — a chave sai do esquema e a referencia tem de LEVANTAR
# ---------------------------------------------------------------------------

def morte_sem_vocabulario_de_cobertura(banco, esquema, constantes):
    del esquema["vocabularios"]["forma_de_cobertura"]
    return banco, esquema, constantes


def morte_com_forma_nova_sem_escrita(banco, esquema, constantes):
    """Forma nova no esquema e sem rotulo na F3: a tela publicaria o codigo cru."""
    esquema["vocabularios"]["forma_de_cobertura"].append("meia_entrada")
    return banco, esquema, constantes


def morte_sem_as_tres_regras(banco, esquema, constantes):
    del esquema["regra_da_cobertura_do_passe"]["as_tres_regras"]
    return banco, esquema, constantes


def morte_sem_validade_do_preco(banco, esquema, constantes):
    del esquema["validade_do_preco"]
    return banco, esquema, constantes


def morte_sem_passe_no_vocabulario_de_categoria(banco, esquema, constantes):
    esquema["vocabularios"]["categoria"] = [
        c for c in esquema["vocabularios"]["categoria"] if c != "passe_de_cidade"]
    return banco, esquema, constantes


def morte_sem_molde_do_piso(banco, esquema, constantes):
    """Sem o molde, o bloco de compra do passe nao e fabricavel."""
    del esquema["piso_de_compra"]["molde"]
    return banco, esquema, constantes


def morte_sem_moeda_no_vocabulario(banco, esquema, constantes):
    esquema["vocabularios"]["moeda"] = ["USD"]
    return banco, esquema, constantes


MORTES = [
    ("sem vocabulario `forma_de_cobertura`", morte_sem_vocabulario_de_cobertura),
    ("forma de cobertura nova sem forma de escrita na F3", morte_com_forma_nova_sem_escrita),
    ("sem as tres regras da cobertura no esquema", morte_sem_as_tres_regras),
    ("sem `validade_do_preco` no esquema", morte_sem_validade_do_preco),
    ("`passe_de_cidade` fora do vocabulario `categoria`",
     morte_sem_passe_no_vocabulario_de_categoria),
    ("sem o molde do piso de compra", morte_sem_molde_do_piso),
    ("moeda do banco fora do vocabulario", morte_sem_moeda_no_vocabulario),
]


def _rodar(portao, gerador, f3, banco, esquema, constantes):
    """Roda o portao sobre um mundo, com o arquivo de respostas GERADO daquele mundo.

    Gerar o arquivo junto e o que impede a mutacao de reprovar pelo motivo errado:
    sem isto, toda quebra reprovaria tambem na secao 8 do portao (o arquivo gravado
    discordando do mundo mutado), e nenhuma provaria reprovar pela sua propria
    afirmacao.
    """
    try:
        doc = gerador.montar(f3, banco, esquema, constantes, HOJE)
    except Exception as erro:
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    try:
        falhas, _ = portao.conferir(f3, banco, esquema, constantes, doc, HOJE)
    except Exception as erro:
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    return ("reprova" if falhas else "passa"), falhas


def main():
    portao = _portao()
    gerador = _gerador()
    banco = _ler("experiencias.json")
    esquema = _ler("esquema-banco.json")
    constantes = _ler("constantes.json")

    f3 = _referencia_mutada()
    decidiu, falhas = _rodar(portao, gerador, f3, copy.deepcopy(banco),
                             copy.deepcopy(esquema), copy.deepcopy(constantes))
    if decidiu != "passa":
        print("O MUNDO REAL JA ESTA REPROVADO — nenhuma mutacao mede nada assim (%s):"
              % decidiu)
        for f in falhas[:10]:
            print("  - %s" % f)
        return 1

    resultados = []
    com_frase = 0

    for nome, funcao in MUNDOS:
        f3 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f3, b, e, c)
        resultados.append((nome, "passa", decidiu, falhas, None))

    for nome, trocas, frase, mundo in QUEBRAS_DE_REFERENCIA:
        f3 = _referencia_mutada(trocas)
        b, e, c = (copy.deepcopy(banco), copy.deepcopy(esquema), copy.deepcopy(constantes))
        if mundo is not None:
            b, e, c = mundo(b, e, c)
        decidiu, falhas = _rodar(portao, gerador, f3, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase or None))
        if frase:
            com_frase += 1

    # AS QUEBRAS DA VALIDADE mexem na F1, nao na F3: a regra mora la desde 22/10/2026,
    # e quebra-la de dentro da F3 seria quebrar uma copia que nao existe.
    for nome, trocas, frase in QUEBRAS_DA_VALIDADE:
        fonte = FONTE_DA_F1
        for antes, depois in trocas:
            quantas = fonte.count(antes)
            if quantas != 1:
                raise SystemExit(
                    "MUTACAO INERTE: o alvo %r aparece %d vezes na f1-referencia.py."
                    % (antes[:70], quantas))
            fonte = fonte.replace(antes, depois)
        modulo = types.ModuleType("f1_referencia_mutada")
        modulo.__file__ = F1
        exec(compile(fonte, F1, "exec"), modulo.__dict__)
        f3 = _referencia_mutada()
        f3.f1.dias_de_validade = modulo.dias_de_validade
        f3.f1.preco_vencido = modulo.preco_vencido
        b, e, c = (copy.deepcopy(banco), copy.deepcopy(esquema), copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f3, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase or None))
        if frase:
            com_frase += 1

    for nome, funcao in MORTES:
        f3 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f3, b, e, c)
        resultados.append((nome, "morre", decidiu, falhas, None))

    erradas = []
    for nome, espera, decidiu, falhas, frase in resultados:
        marca = "ok " if decidiu == espera else "NAO"
        if decidiu != espera:
            erradas.append((nome, espera, decidiu, falhas))
        elif frase is not None and not any(frase in f for f in falhas):
            marca = "NAO"
            erradas.append((nome + " (reprovou, mas nao pela frase %r)" % frase,
                            espera, decidiu, falhas))
        print("  %s  %-64s espera %-8s deu %s" % (marca, nome[:64], espera, decidiu))

    print("\n%d mutacoes: %d mundos que tem de PASSAR, %d quebras que tem de REPROVAR "
          "e %d mortes que tem de MATAR a referencia."
          % (len(resultados), len(MUNDOS),
             len(QUEBRAS_DE_REFERENCIA) + len(QUEBRAS_DA_VALIDADE), len(MORTES)))
    print("%d delas declaram a FRASE que esperam ouvir de volta, e foram cobradas por ela."
          % com_frase)

    if erradas:
        print("")
        for nome, espera, decidiu, falhas in erradas:
            print("  ERRADA: %s — esperava %s, deu %s" % (nome, espera, decidiu))
            for f in falhas[:3]:
                print("      %s" % f[:220])
        print("\n%d mutacao(oes) decidiram errado." % len(erradas))
        return 1
    print("Todas decidiram certo, nos TRES lados da fronteira.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

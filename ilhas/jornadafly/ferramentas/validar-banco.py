#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se o banco da JornadaFly cumpre o contrato de dados/esquema-banco.json.

Roda sem dependencia e sem rede:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Ferramenta de bancada: nunca
e publicada no site.

POR QUE ELE EXISTE, e por que nesta ilha ele mede outra coisa que nas irmas.
O produto desta ilha e o preco DATADO, com a unidade declarada e a conta fechada
para o grupo. Os dois defeitos que os blocos 1 e 2 mediram em oito consultas e tres
continentes sao: ninguem data o preco, e a unidade do preco troca dentro da mesma
resposta sem aviso. Um banco que deixe entrar preco sem data, ou unidade sem dizer
de onde ela foi lida, publica a ilha inteira cometendo o defeito que ela existe
para corrigir.

AS QUATRO COISAS QUE ELE FAZ E QUE NAO SAO "CONFERIR CAMPO OBRIGATORIO":

  1. RECOMPUTA A RESOLUCAO DE DIVERGENCIA a partir das declaracoes e da escada de
     fontes, e reprova o valor resolvido que nao seja o da autoridade (quando ha) ou
     o MAXIMO das declaracoes (quando nao ha). E a proibicao de media virada em
     codigo: media nao se reconhece pelo nome, se reconhece por cair entre o minimo
     e o maximo sem ser nenhum dos dois.
  2. DERIVA O PISO DE COMPRA do molde do esquema com o slug da cidade e compara com
     o que esta gravado. URL de piso digitada a mao envelhece calada no dia em que o
     molde mudar (secao 8: numero de tela nasce contado, nunca digitado).
  3. LE A LISTA DE CAMPOS QUE EXIGEM declarada_por DO ESQUEMA, nunca de dentro de si
     (secao 26.2) — e REPROVA SE A CHAVE SUMIR. Regua que le a propria lista de um
     arquivo de dados aprova tudo, em silencio, no dia em que o arquivo perder a
     chave.
  4. COBRA A REGRA DO DOCUMENTO NOMEADO (nascida na carga de 14/09/2026, e tambem
     lida do esquema): fonte de nivel de autoridade que nao nomeia o documento que
     a sustenta nao deixa o registro `publicavel` — ele entra como
     `pendente_de_releitura`. A escada ja cobrava o elo mais fraco entre autoria,
     custodia e leitura, e faltava o quarto elo. A tarifa da gondola e nivel 3 e
     cita a Delibera 89/2023; a do Angkor e nivel 3 e voltou em duas passadas sem
     nenhum ato, tabela ou pagina de tarifa junto. Sao coisas diferentes, e ate
     esta regra o esquema nao tinha como dizer isso.

E ele e importavel: `validar(esquema, banco, constantes, hoje)` devolve
(erros, avisos, resumo_calculado) sobre dicionarios em memoria. E assim que
ferramentas/mutacoes-banco.py produz os mundos que o banco ainda nao tem.
"""

import copy
import datetime
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

HEDGES = ("cerca de", "aproximadamente", "em torno de", "a partir de", "por volta de")
FRASE_PROIBIDA = "link de loja em breve"

# Os dois padroes da `regra_da_elegibilidade` (27/10/2026). Eles existem porque a troca
# entre faixa etaria e elegibilidade e SILENCIOSA: os dois campos guardam um preco menor
# com uma condicao escrita ao lado, e lidos de longe parecem a mesma coisa. O que os
# separa e O QUE SE PROVA na porta, e e isso que estes padroes procuram na frase.
PADRAO_IDADE = re.compile(
    r"(\d+\s*ano)|(menor(es)?\s+de\s+\d+)|(maior(es)?\s+de\s+\d+)"
    r"|(acima\s+de\s+\d+\s*ano)|(de\s+\d+\s+a\s+\d+\s*ano)", re.I)
PADRAO_RESIDENCIA = re.compile(
    r"(morador)|(residente)|(residencia)|(residência)|(nascid[oa])|(brasileir)"
    r"|(estrangeir)|(nacionalidade)", re.I)


def _carregar(nome):
    caminho = os.path.join(DADOS, nome)
    with open(caminho, encoding="utf-8") as fh:
        return json.load(fh)


def _e_data(valor):
    if not isinstance(valor, str):
        return False
    try:
        datetime.date.fromisoformat(valor)
        return True
    except ValueError:
        return False


def _textos(no):
    """Todo texto dentro de uma estrutura, para varredura de frase proibida."""
    if isinstance(no, str):
        yield no
    elif isinstance(no, dict):
        for k, v in no.items():
            yield k
            for t in _textos(v):
                yield t
    elif isinstance(no, list):
        for v in no:
            for t in _textos(v):
                yield t


# POR EXTENSO DE 1 A 12, que e a faixa de grupo que a F1 aceita. Esta lista e uma
# DECISAO desta regua (o que conta como "a fonte declarou o numero") e nao um fato
# externo, por isso ela mora aqui e nao no esquema — a fronteira da secao 8. A fonte
# do Angkor escreve "para a visitacao de um dia" por extenso e "para 3 dias" em
# digito na mesma leitura: quem escolhe a forma e ela, nao a ilha.
NUMERO_POR_EXTENSO = {
    1: ("um", "uma"),
    2: ("dois", "duas"),
    3: ("tres", "três"),
    4: ("quatro",),
    5: ("cinco",),
    6: ("seis",),
    7: ("sete",),
    8: ("oito",),
    9: ("nove",),
    10: ("dez",),
    11: ("onze",),
    12: ("doze",),
}


def _declara_o_numero(frase, n):
    """A frase da fonte diz o numero `n`, em digito ou por extenso?

    Confere em PALAVRA INTEIRA: sem isso, "7" acharia o 7 de "US$ 72" e "um"
    acharia o "um" de "algum", que e exatamente a vizinhanca que a secao 8 manda
    nao usar como criterio.
    """
    if not isinstance(frase, str) or not isinstance(n, int):
        return False
    baixo = frase.lower()
    if re.search(r"(?<![\d,.])%d(?![\d,.])" % n, baixo):
        return True
    for palavra in NUMERO_POR_EXTENSO.get(n, ()):
        if re.search(r"(?<![0-9a-zà-ÿ])%s(?![0-9a-zà-ÿ])" % re.escape(palavra), baixo):
            return True
    return False


def _maximo(valor):
    """Valor comparavel de uma declaracao: numero, ou o topo da faixa."""
    if isinstance(valor, (int, float)):
        return float(valor)
    if isinstance(valor, dict) and isinstance(valor.get("maximo"), (int, float)):
        return float(valor["maximo"])
    return None


def _minimo(valor):
    if isinstance(valor, (int, float)):
        return float(valor)
    if isinstance(valor, dict) and isinstance(valor.get("minimo"), (int, float)):
        return float(valor["minimo"])
    return None


def validar(esquema, banco, constantes=None, hoje=None):
    erros = []
    avisos = []
    hoje = hoje or datetime.date.today()
    n_eixo = {}
    n_dias_de_uso = 0

    def erro(msg):
        erros.append(msg)

    def aviso(msg):
        if msg not in avisos:
            avisos.append(msg)

    def conferir_dias_transcrito(ondev, versao, dias):
        """`dias_de_uso` preenchido: inteiro, com a frase, e o numero DENTRO da frase.

        Virou funcao em 22/10/2026, no bloco da F3, porque a conferencia valia para DOIS
        eixos e estava escrita dentro de um: `por_quantidade` a fazia e `eixo null` — a
        experiencia de UMA versao, que e exatamente o que um passe de validade unica e —
        nao caia em nenhuma das duas direcoes e passava calado. Duas copias da mesma
        conferencia seriam a familia de defeito que esta pasta mais paga; uma funcao
        chamada de dois lugares nao.
        """
        nonlocal n_dias_de_uso
        if not isinstance(dias, int) or isinstance(dias, bool) or dias < 1:
            erro("%s: `dias_de_uso` %r nao e inteiro maior que zero." % (ondev, dias))
            return
        if not versao.get("dias_de_uso_transcrito_de"):
            erro("%s: `dias_de_uso` %r sem `dias_de_uso_transcrito_de`. Numero que vira "
                 "campo diz de qual frase saiu — a mesma disciplina do `transcrito_de` "
                 "das faixas etarias." % (ondev, dias))
        n_dias_de_uso += 1
        declarado = versao.get("declarado_como") or ""
        if not _declara_o_numero(declarado, dias):
            erro("%s: `dias_de_uso` %r nao aparece em `declarado_como` (%r), nem em "
                 "digito nem por extenso. O numero tem de estar na FRASE DA FONTE: "
                 "aceita-lo so porque esta no campo e confiar na transcricao em vez de "
                 "conferi-la, e e a conta que a secao 8 chama de terceira."
                 % (ondev, dias, declarado[:90]))

    # ------------------------------------------------------------------
    # 1. O ESQUEMA ESTA INTEIRO?
    # A regua le a lista DELE (26.2). Se a chave sumir, tudo passa em silencio —
    # entao a ausencia da chave e erro duro, e e a primeira coisa conferida.
    # ------------------------------------------------------------------
    vocab = esquema.get("vocabularios")
    if not isinstance(vocab, dict) or not vocab:
        erro("esquema: `vocabularios` ausente ou vazio. Sem ele nenhum valor de "
             "vocabulario controlado pode ser conferido, e a regua aprovaria "
             "qualquer coisa em silencio.")
        vocab = {}

    for chave in ("unidade_de_preco", "declarada_por", "categoria", "tipo_de_operador",
                  "momento_do_dia", "canal_de_leitura", "moeda", "status_do_registro",
                  "eixo_das_versoes", "categoria_de_custo", "padrao_de_viagem",
                  "base_da_faixa", "o_que_o_numero_e", "forma_de_cobertura"):
        if not isinstance(vocab.get(chave), list) or not vocab.get(chave):
            erro("esquema: vocabularios.%s ausente ou vazio." % chave)

    if not isinstance((esquema.get("entidades") or {}).get("FAIXA_DIARIA"), dict):
        erro("esquema: entidade `FAIXA_DIARIA` ausente. Ela e onde moram hospedagem, "
             "alimentacao e transporte local — as tres linhas da F2 que NAO sao nossas. "
             "Sem ela a regua nao tem o que cobrar e a F2 some uma linha sem dono.")

    if not isinstance((esquema.get("entidades") or {}).get("COBERTURA_DO_PASSE"), dict):
        erro("esquema: entidade `COBERTURA_DO_PASSE` ausente. Ela e a relacao entre um "
             "passe e UMA atracao que ele cobre, e e sobre ela que a F3 calcula o ponto "
             "de equilibrio. Sem ela a regua nao tem o que cobrar e a F3 somaria o que o "
             "passe DIZ cobrir em vez do que esta ilha LEU que ele cobre.")

    regra_cobertura = esquema.get("regra_da_cobertura_do_passe")
    if not isinstance(regra_cobertura, dict) or \
            not isinstance(regra_cobertura.get("as_tres_regras"), list) or \
            len(regra_cobertura.get("as_tres_regras") or []) != 3:
        erro("esquema: `regra_da_cobertura_do_passe.as_tres_regras` ausente ou sem as "
             "tres. A regua le a lista DELE (26.2), e as tres sao o que a F3 publica: "
             "nao lida nao e nao coberta, o equilibrio e sobre o que a ilha leu, e "
             "desconto com teto e faixa.")

    exige = esquema.get("campos_que_exigem_declaracao_de_origem")
    campos_declarada_por = None
    if not isinstance(exige, dict) or not isinstance(exige.get("campos"), list) or not exige.get("campos"):
        erro("esquema: `campos_que_exigem_declaracao_de_origem.campos` ausente ou vazia. "
             "Esta e a lista da secao 26.2: sem ela a trava de origem do dado aprova "
             "todo registro, inclusive o proximo, e fica verde.")
    else:
        campos_declarada_por = exige["campos"]

    escada = esquema.get("escada_de_fontes", {}).get("niveis")
    niveis = {}
    if not isinstance(escada, list) or not escada:
        erro("esquema: `escada_de_fontes.niveis` ausente ou vazia. Sem escada, o nivel "
             "de uma fonte vira um numero que nao responde a ninguem — que e exatamente "
             "por onde o defeito do elo mais fraco entrou na Robometria.")
    else:
        for degrau in escada:
            niveis[degrau.get("nivel")] = degrau

    molde_piso = esquema.get("piso_de_compra", {}).get("molde")
    if not isinstance(molde_piso, str) or "{slug_plataforma}" not in molde_piso:
        erro("esquema: `piso_de_compra.molde` ausente ou sem {slug_plataforma}. O piso "
             "da 25.2 tem de ser DERIVADO da cidade; sem molde ele vira URL digitada.")
        molde_piso = None

    regra_div = esquema.get("regra_de_divergencia")
    if not isinstance(regra_div, dict) or not regra_div.get("media"):
        erro("esquema: `regra_de_divergencia` ausente ou sem a linha da media. A "
             "proibicao de media (secao 10) mora no esquema e e daqui que ela e cobrada.")

    # A regra do documento nomeado (nascida na carga de 14/09/2026). Ela tambem
    # mora no ESQUEMA e nao aqui dentro (26.2): se a chave sumir, autoridade de
    # ouvir falar volta a valer o mesmo que autoridade com ato nomeado, e a regua
    # fica verde sem medir nada.
    regra_doc = esquema.get("regra_do_documento_nomeado")
    niveis_de_autoridade = []
    status_sem_documento = None
    if not isinstance(regra_doc, dict) \
            or not isinstance(regra_doc.get("niveis_de_autoridade"), list) \
            or not regra_doc.get("niveis_de_autoridade") \
            or not regra_doc.get("status_quando_falta_documento"):
        erro("esquema: `regra_do_documento_nomeado` ausente ou incompleta. Sem ela, "
             "fonte de autoridade que nao nomeia o documento que a sustenta volta a "
             "sustentar registro `publicavel` — que e a distancia entre a tarifa da "
             "gondola, com ato citado, e a do Angkor, que duas passadas atribuiram ao "
             "vendedor oficial sem nenhuma delas trazer o ato.")
    else:
        niveis_de_autoridade = regra_doc["niveis_de_autoridade"]
        status_sem_documento = regra_doc["status_quando_falta_documento"]

    # A faixa etaria desceu da EXPERIENCIA para a VERSAO em 22/10/2026, e a regra que
    # a proibe fora de `por_pessoa` mora no ESQUEMA e nao aqui (26.2). Se a chave sumir,
    # a gondola volta a poder ter preco de crianca — numa tarifa cobrada pela
    # embarcacao inteira — e a regua fica verde sem medir nada. Mesma familia da
    # `regra_do_documento_nomeado` acima.
    campos_versao = esquema.get("entidades", {}).get("VERSAO", {}).get("campos", {})
    campos_exp = esquema.get("entidades", {}).get("EXPERIENCIA", {}).get("campos", {})
    faixa_esquema = campos_versao.get("faixa_etaria") if isinstance(campos_versao, dict) else None
    faixa_proibida_quando = None
    if not isinstance(faixa_esquema, dict) or not faixa_esquema.get("null_exige") \
            or not faixa_esquema.get("proibido_quando"):
        erro("esquema: `entidades.VERSAO.campos.faixa_etaria` ausente ou sem "
             "`null_exige`/`proibido_quando`. A faixa etaria desceu para a VERSAO em "
             "22/10/2026 justamente porque o preco dela depende da versao; sem esta "
             "chave a regua nao sabe que a lacuna exige motivo nem que faixa fora de "
             "`por_pessoa` e proibida.")
    else:
        faixa_proibida_quando = faixa_esquema["proibido_quando"]
    if isinstance(campos_exp, dict) and "faixa_etaria" in campos_exp:
        erro("esquema: `faixa_etaria` voltou para `entidades.EXPERIENCIA.campos`. Ela "
             "saiu de la em 22/10/2026 e o motivo esta medido: na Torre Eiffel a crianca "
             "de 4 a 11 anos paga 3,80 EUR pela escada e 9,20 EUR pelo elevador ate o "
             "topo, e um campo por experiencia publica o numero errado para tres das "
             "quatro versoes. Campo que volta para a entidade errada e regressao, nao "
             "escolha.")
    # O EIXO DAS VERSOES e os DIAS DE USO nasceram em 22/10/2026, no bloco 4, porque a
    # Conta 3 da F1 nao era calculavel sobre o banco versao 4: a quantidade de uso de
    # cada bilhete existia so na PROSA do rotulo. As duas regras moram no ESQUEMA e nao
    # aqui (26.2) — e se a chave sumir, a F1 volta a poder comparar bilhetes que nao se
    # substituem (dois ingressos de 24h do Coliseu nao dao a area restrita) e a regua
    # fica verde sem medir nada. Mesma familia da `faixa_etaria` acima.
    eixo_esquema = campos_exp.get("eixo_das_versoes") if isinstance(campos_exp, dict) else None
    if not isinstance(eixo_esquema, dict) or not eixo_esquema.get("null_exige"):
        erro("esquema: `entidades.EXPERIENCIA.campos.eixo_das_versoes` ausente ou sem "
             "`null_exige`. O eixo e a DECISAO sobre o conjunto de versoes — se as "
             "versoes sao mais da mesma coisa, coisas diferentes, ou a mesma coisa em "
             "outro horario — e e dele que a Conta 3 da F1 depende. Sem esta chave a "
             "regua nao sabe que a lacuna exige motivo.")
    dias_esquema = campos_versao.get("dias_de_uso") if isinstance(campos_versao, dict) else None
    dias_exigido_quando = None
    if not isinstance(dias_esquema, dict) or not dias_esquema.get("null_exige") \
            or not dias_esquema.get("exigido_quando") or not dias_esquema.get("proibido_quando"):
        erro("esquema: `entidades.VERSAO.campos.dias_de_uso` ausente ou sem "
             "`null_exige`/`exigido_quando`/`proibido_quando`. Sem as tres, versao de "
             "eixo de quantidade pode nascer sem a quantidade (e a Conta 3 cai calada) "
             "e versao de escopo pode nascer COM quantidade (e a F1 publica um ponto de "
             "equilibrio entre bilhetes que nao se substituem).")
    else:
        dias_exigido_quando = dias_esquema["exigido_quando"]
    if not isinstance(esquema.get("conta_3_da_F1_exige_EIXO_DECLARADO_e_nao_sai_do_rotulo"), dict):
        erro("esquema: falta o registro "
             "`conta_3_da_F1_exige_EIXO_DECLARADO_e_nao_sai_do_rotulo`. Ele guarda POR QUE "
             "os dois campos existem; sem ele a proxima execucao le dois campos sem causa "
             "e o primeiro que os achar incomodos os remove.")

    # ---- ELEGIBILIDADE (nasceu em 27/10/2026, na carga do Bondinho)
    if not isinstance((esquema.get("entidades") or {}).get("ELEGIBILIDADE"), dict):
        erro("esquema: falta a entidade `ELEGIBILIDADE`. Ela e onde mora o preco de quem "
             "prova uma condicao que NAO E IDADE — residencia, nacionalidade, vinculo. "
             "Sem a forma declarada, cada carga inventa a sua e o preco de brasileiro vai "
             "para `faixa_etaria`, que e o campo da idade.")
    eleg_esquema = campos_versao.get("elegibilidade") if isinstance(campos_versao, dict) else None
    if not isinstance(eleg_esquema, dict) or not eleg_esquema.get("null_exige"):
        erro("esquema: `entidades.VERSAO.campos.elegibilidade` ausente ou sem "
             "`null_exige`. Campo que pode ser null sem motivo exigido deixa a lacuna "
             "muda, e aqui a lacuna muda custa o preco do leitor brasileiro.")
    if isinstance(campos_exp, dict) and "elegibilidade" in campos_exp:
        erro("esquema: `elegibilidade` gravada em `entidades.EXPERIENCIA.campos`. Ela e "
             "da VERSAO pelo mesmo motivo da faixa etaria: no Bondinho a promocional de "
             "brasileiro existe no Bilhete Bondinho e NAO existe nas tarifas que ja sao "
             "promocionais.")
    regra_eleg = esquema.get("regra_da_elegibilidade")
    if not isinstance(regra_eleg, dict):
        erro("esquema: falta `regra_da_elegibilidade`. E dela que esta regua le a "
             "proibicao dos dois sentidos (idade nunca em elegibilidade, residencia "
             "nunca em faixa etaria) — a regua le a regra do esquema e nunca de dentro "
             "de si (secao 26.2).")
    else:
        for chave in ("idade_nunca_entra_em_elegibilidade",
                      "residencia_nunca_entra_em_faixa_etaria",
                      "elegibilidade_nunca_e_mais_cara_que_a_versao",
                      "a_soma_nao_se_presume"):
            if not regra_eleg.get(chave):
                erro("esquema: `regra_da_elegibilidade.%s` ausente. Regra que a regua "
                     "aplica e o esquema nao declara e regua decidindo sozinha." % chave)

    if not isinstance(esquema.get("entidades", {}).get("FAIXA_ETARIA"), dict):
        erro("esquema: falta a entidade `FAIXA_ETARIA`. Sem a forma declarada, cada "
             "faixa do banco e um dicionario de forma livre e a regua nao tem o que "
             "cobrar.")

    validade = esquema.get("validade_do_preco", {})

    if erros and campos_declarada_por is None:
        # Sem a lista, nao da para afirmar nada sobre os registros; o relatorio ja
        # nomeou a causa e insistir produziria cem erros derivados de um so.
        return erros, avisos, {}

    def em_vocab(chave, valor):
        return valor in vocab.get(chave, [])

    # ------------------------------------------------------------------
    # A TARIFA QUE EXIGE MAIS DE UMA PROVA (`provas_adicionais`, versao 9 do
    # esquema, 27/10/2026)
    #
    # Nasceu com a carga do Trem do Corcovado. O esquema versao 8 aprendeu O QUE
    # se prova na porta — residencia, nacionalidade, vinculo — e continuou supondo
    # que se prova UMA coisa. Este operador cobra R$ 70 de «idosos acima de 60
    # anos, APENAS BRASILEIROS» e R$ 107 de estudante e de ID Jovem «apenas para
    # brasileiros»: tres tarifas, duas provas cada.
    #
    # Sem o campo havia duas saidas e as duas mentiam. Enfiar a nacionalidade na
    # prosa de `condicao` de uma FAIXA_ETARIA briga com o que o esquema diz dela
    # desde 14/09 — `se_nao_cumprir` e «o que o operador cobra de quem nao prova a
    # IDADE» — e faria a tela prometer R$ 70 ao estrangeiro de 65 anos que paga
    # R$ 134; e a regua PADRAO_RESIDENCIA, que nasceu ontem, reprovaria a frase com
    # razao. Chamar a tarifa de ELEGIBILIDADE perderia a idade, que e metade do
    # preco. O campo e o terceiro lugar, e esta funcao e o que impede que ele vire
    # um deposito de prosa.
    # ------------------------------------------------------------------
    def conferir_provas_adicionais(onde, item, prova_do_dono=None):
        """Confere `provas_adicionais` de uma FAIXA_ETARIA ou de uma ELEGIBILIDADE.

        `prova_do_dono` e o `o_que_se_prova` da elegibilidade que a hospeda, ou None
        numa faixa etaria (onde a prova do dono e a idade, que nao esta no
        vocabulario de proposito).
        """
        if "provas_adicionais" not in item:
            erro("%s: falta o campo `provas_adicionais` (esquema versao 9). Ausencia "
                 "de chave e esquecimento; null com motivo e resposta — e aqui a "
                 "diferenca custa dinheiro na porta: o esquema nao sabe se o operador "
                 "nao exige nada a mais ou se ninguem leu." % onde)
            return 0
        provas = item.get("provas_adicionais")
        if provas is None:
            if not item.get("motivo_sem_provas_adicionais"):
                erro("%s: `provas_adicionais` null sem `motivo_sem_provas_adicionais`. "
                     "O motivo e o que separa «a frase da fonte nao exige mais nada» de "
                     "«esta leitura nao procurou», e as duas dao telas diferentes."
                     % onde)
            return 0
        if not isinstance(provas, list) or not provas:
            erro("%s: `provas_adicionais` tem de ser lista NAO vazia ou null com "
                 "motivo. Lista vazia nao diz qual das duas coisas aconteceu." % onde)
            return 0
        if not item.get("se_nao_cumprir") and not item.get("motivo_sem_se_nao_cumprir"):
            erro("%s: tarifa com `provas_adicionais` e sem `se_nao_cumprir`. A prova a "
                 "mais e exatamente o que barra o comprador no balcao: quem le precisa "
                 "saber o que paga sem ela." % onde)
        vistas = set()
        for i, prova in enumerate(provas):
            ondep = "%s/provas_adicionais/%d" % (onde, i)
            if not isinstance(prova, dict):
                erro("%s: entrada de `provas_adicionais` nao e objeto." % ondep)
                continue
            qual = prova.get("o_que_se_prova")
            if not em_vocab("o_que_se_prova", qual):
                erro("%s: `o_que_se_prova` %r fora do vocabulario. IDADE nao esta nele "
                     "de proposito: idade e FAIXA_ETARIA." % (ondep, qual))
            if qual in vistas:
                erro("%s: `o_que_se_prova` %r repetido na mesma tarifa. Duas entradas "
                     "para a mesma prova sao a mesma exigencia escrita duas vezes, e a "
                     "tela a pediria duas vezes ao leitor." % (ondep, qual))
            vistas.add(qual)
            if prova_do_dono is not None and qual == prova_do_dono:
                erro("%s: `o_que_se_prova` %r igual ao da propria elegibilidade que a "
                     "hospeda. Isso nao e prova adicional: e a mesma prova escrita duas "
                     "vezes." % (ondep, qual))
            if not prova.get("condicao"):
                erro("%s: entrada de `provas_adicionais` sem `condicao`. Prova a mais "
                     "sem dizer o que se prova e exigencia muda." % ondep)
            if not prova.get("declarado_como"):
                erro("%s: entrada de `provas_adicionais` sem `declarado_como`. A tela "
                     "cita a frase que exige a prova a mais, nunca a parafraseia — e e "
                     "essa frase que o leitor confere no balcao." % ondep)
            # SO `condicao` E VARRIDA, e `declarado_como` NAO — medido na propria
            # passada que escreveu esta funcao, em 27/10/2026. A primeira versao varria
            # as duas e reprovou DUAS tarifas certas: a frase da fonte diz «idosos
            # acima de 60 anos, apenas brasileiros» e «jovens brasileiros de 15 a 29
            # anos», porque e a fonte falando. `declarado_como` e CITACAO, e censurar a
            # citacao para agradar ao portao e pior que o defeito que o portao procura —
            # a tela cita, nunca parafraseia. Mesma escolha das reguas irmas de
            # PADRAO_IDADE e PADRAO_RESIDENCIA, que varrem rotulo e condicao e nunca a
            # frase da fonte. O que esta regua guarda e o que A ILHA declara ter de ser
            # provado.
            alvo = prova.get("condicao") or ""
            if PADRAO_IDADE.search(alvo):
                erro("%s: a prova adicional declara uma faixa de idade (%r). Idade "
                     "NUNCA entra aqui, pela mesma razao que nao esta em "
                     "`o_que_se_prova`: idade se prova em FAIXA_ETARIA, e dois campos "
                     "para o mesmo fato sao duas metades que nunca se falam."
                     % (ondep, alvo.strip()))
        return len(provas)

    # ------------------------------------------------------------------
    # 2. CIDADES
    # ------------------------------------------------------------------
    cidades = {}
    for cidade in banco.get("cidades", []):
        cid = cidade.get("id")
        onde = "cidades/%s" % (cid or "?")
        if not cid:
            erro("%s: sem `id`." % onde)
            continue
        if cid in cidades:
            erro("%s: `id` repetido." % onde)
        cidades[cid] = cidade
        for campo in ("nome", "pais", "moeda_local", "slug_plataforma"):
            if not cidade.get(campo):
                erro("%s: sem `%s`." % (onde, campo))
        if not em_vocab("moeda", cidade.get("moeda_local")):
            erro("%s: `moeda_local` %r fora do vocabulario." % (onde, cidade.get("moeda_local")))
        if not _e_data(cidade.get("slug_plataforma_conferido_em")):
            erro("%s: `slug_plataforma_conferido_em` ausente ou nao e data. Sem a data, "
                 "o piso de compra e uma URL SUPOSTA, e piso suposto e pior que piso "
                 "ausente: ele parece conferido." % onde)

    # ------------------------------------------------------------------
    # 3. FONTES — o elo mais fraco (secao 10)
    # ------------------------------------------------------------------
    fontes = {}
    for fonte in banco.get("fontes", []):
        fid = fonte.get("id")
        onde = "fontes/%s" % (fid or "?")
        if not fid:
            erro("%s: sem `id`." % onde)
            continue
        if fid in fontes:
            erro("%s: `id` repetido." % onde)
        fontes[fid] = fonte

        nivel = fonte.get("nivel")
        degrau = niveis.get(nivel)
        if degrau is None:
            erro("%s: nivel %r nao existe na escada do esquema." % (onde, nivel))
            continue
        if fonte.get("origem") != degrau.get("origem"):
            erro("%s: `origem` %r nao bate com a origem que a escada da ao nivel %s (%r). "
                 "Conferir so o numero e por onde o defeito do elo mais fraco entra."
                 % (onde, fonte.get("origem"), nivel, degrau.get("origem")))
        if not em_vocab("canal_de_leitura", fonte.get("leitura")):
            erro("%s: `leitura` %r fora do vocabulario. Silencio nunca promove."
                 % (onde, fonte.get("leitura")))
        if degrau.get("exige_leitura_direta") and fonte.get("leitura") != "leitura_direta":
            erro("%s: o nivel %s exige leitura direta e a fonte declara `leitura` %r. "
                 "Autoria forte nao promove custodia nem leitura fracas."
                 % (onde, nivel, fonte.get("leitura")))
        if not fonte.get("autor"):
            erro("%s: sem `autor`." % onde)
        if fonte.get("documento") is None and not fonte.get("motivo_sem_documento"):
            erro("%s: `documento` null sem `motivo_sem_documento`. Resposta que nao cita "
                 "o documento que a sustenta nao e fonte, e parafrase (secao 8)." % onde)
        if fonte.get("url") is None and not fonte.get("motivo_sem_url"):
            erro("%s: `url` null sem `motivo_sem_url`." % onde)
        if not _e_data(fonte.get("data_leitura")):
            erro("%s: `data_leitura` ausente ou nao e data." % onde)

    # `existe_hoje` de cada degrau e DERIVADO: verdadeiro quando alguma fonte do
    # banco declara aquele nivel. Ate 15/09/2026 este campo era prosa que ninguem
    # recomputava, e e a familia mais silenciosa do numero digitado — um
    # `existe_hoje: false` velho faz a ilha dizer que nao alcanca um degrau que ela
    # ja alcancou, e nada no banco contradiz a frase.
    niveis_no_banco = set(f.get("nivel") for f in banco.get("fontes", []))
    for nivel, degrau in sorted(niveis.items()):
        if "existe_hoje" not in degrau:
            erro("esquema: escada_de_fontes nivel %s sem `existe_hoje`. O campo e "
                 "derivado do banco e a regua precisa dele para ter o que comparar."
                 % nivel)
            continue
        derivado = nivel in niveis_no_banco
        if bool(degrau.get("existe_hoje")) != derivado:
            erro("esquema: escada_de_fontes nivel %s grava `existe_hoje` %r e o banco "
                 "da %r (%s fonte(s) neste degrau). O campo e DERIVADO das fontes do "
                 "banco; gravado a mao ele envelhece calado, e um `false` velho faz a "
                 "ilha negar um degrau que ja alcancou."
                 % (nivel, degrau.get("existe_hoje"), derivado,
                    sum(1 for f in banco.get("fontes", []) if f.get("nivel") == nivel)))

    fontes_usadas = set()

    # ------------------------------------------------------------------
    # 4. EXPERIENCIAS
    # ------------------------------------------------------------------
    ids = set()
    n_versoes = 0
    n_faixas_de_idade = 0
    n_lacunas_de_faixa = 0
    n_declaracoes = 0
    n_publicaveis = 0
    sem_saida = 0
    piso_nao_rastreavel = 0
    intestaveis = 0
    versoes_em_brl = set()
    n_elegibilidades = [0]
    n_tarifas_com_prova_adicional = [0]
    n_provas_adicionais = [0]
    sem_versao = 0
    n_passes = 0
    vencidos = []

    for exp in banco.get("experiencias", []):
        eid = exp.get("id")
        onde = "experiencias/%s" % (eid or "?")
        if not eid:
            erro("%s: sem `id`." % onde)
            continue
        if eid in ids:
            erro("%s: `id` repetido." % onde)
        ids.add(eid)

        if not exp.get("nome"):
            erro("%s: sem `nome`." % onde)
        if not exp.get("entra_por"):
            erro("%s: sem `entra_por`. Todo registro diz por que esta no banco — o "
                 "criterio de entrada prefere operador privado sem tabela publica, e "
                 "quem entra por outro motivo nomeia o motivo." % onde)
        if not em_vocab("categoria", exp.get("categoria")):
            erro("%s: `categoria` %r fora do vocabulario." % (onde, exp.get("categoria")))
        if not em_vocab("status_do_registro", exp.get("status")):
            erro("%s: `status` %r fora do vocabulario." % (onde, exp.get("status")))

        cidade = cidades.get(exp.get("cidade"))
        if cidade is None:
            erro("%s: `cidade` %r nao existe em cidades[]. Sem cidade nao ha piso de "
                 "compra, porque o piso e DERIVADO dela." % (onde, exp.get("cidade")))

        operador = exp.get("operador") or {}
        if not operador.get("nome"):
            erro("%s: operador sem `nome`." % onde)
        if not em_vocab("tipo_de_operador", operador.get("tipo")):
            erro("%s: operador com `tipo` %r fora do vocabulario." % (onde, operador.get("tipo")))
        if operador.get("url") is None and not operador.get("motivo_sem_url"):
            erro("%s: operador com `url` null sem `motivo_sem_url`." % onde)

        eixo = exp.get("eixo_das_versoes")
        if "eixo_das_versoes" not in exp:
            erro("%s: falta o campo `eixo_das_versoes`. Sem ele a F1 nao sabe se as "
                 "versoes desta experiencia se comparam em quantidade, e a Conta 3 "
                 "escolheria por conta propria — adivinhando pelo rotulo, que e prosa."
                 % onde)
        elif eixo is None:
            if len(exp.get("versoes") or []) != 1:
                erro("%s: `eixo_das_versoes` null com %d versoes. O null so vale para a "
                     "experiencia de UMA versao: com duas ha eixo a declarar, e nao "
                     "declarar e deixar a F1 escolher."
                     % (onde, len(exp.get("versoes") or [])))
            if not exp.get("motivo_sem_eixo_das_versoes"):
                erro("%s: `eixo_das_versoes` null sem `motivo_sem_eixo_das_versoes`." % onde)
        elif not em_vocab("eixo_das_versoes", eixo):
            erro("%s: `eixo_das_versoes` %r fora do vocabulario." % (onde, eixo))
        elif not exp.get("nota_do_eixo_das_versoes"):
            erro("%s: `eixo_das_versoes` %r sem `nota_do_eixo_das_versoes`. O eixo e "
                 "uma decisao sobre o conjunto; decisao sem motivo escrito e a primeira "
                 "coisa que a proxima execucao troca sem saber o que esta trocando."
                 % (onde, eixo))
        if eixo is not None:
            n_eixo[eixo] = n_eixo.get(eixo, 0) + 1

        if "faixa_etaria" in exp:
            erro("%s: `faixa_etaria` gravada na EXPERIENCIA. Desde 22/10/2026 ela e "
                 "campo da VERSAO, porque o preco de uma faixa depende do bilhete: "
                 "gravada aqui, ela publica um numero so para versoes que cobram "
                 "diferente." % onde)

        # ---------------- PASSE DE CIDADE: os dois campos que so existem aqui
        #
        # Nasceram em 22/10/2026 com a entidade COBERTURA_DO_PASSE. `atracoes_declaradas_
        # pelo_passe` NAO e a contagem das coberturas lidas: e o numero que a fonte do
        # passe publica, e a distancia entre os dois e o que a F3 leva para a tela. Os dois
        # sao PROIBIDOS fora de `passe_de_cidade` pela mesma razao que `pessoas_por_quarto`
        # e proibido fora da base de quarto: dar o campo a quem nao tem o fato convida a
        # conta que nao existe.
        e_passe = exp.get("categoria") == "passe_de_cidade"
        if e_passe:
            n_passes += 1
            if "atracoes_declaradas_pelo_passe" not in exp:
                erro("%s: passe de cidade sem o campo `atracoes_declaradas_pelo_passe`. "
                     "Ausencia de chave e esquecimento; null com motivo e resposta — e "
                     "sem este numero a F3 nao tem com que comparar as coberturas que a "
                     "ilha leu." % onde)
            else:
                quantas = exp.get("atracoes_declaradas_pelo_passe")
                transcrito = exp.get("atracoes_declaradas_transcrito_de")
                if quantas is None:
                    if not exp.get("motivo_sem_atracoes_declaradas"):
                        erro("%s: `atracoes_declaradas_pelo_passe` null sem "
                             "`motivo_sem_atracoes_declaradas`. Passe que nao diz quantas "
                             "atracoes cobre existe; passe que nao diz nem isso nem por "
                             "que nao diz e lacuna muda." % onde)
                elif not isinstance(quantas, int) or isinstance(quantas, bool) or quantas < 1:
                    erro("%s: `atracoes_declaradas_pelo_passe` %r nao e inteiro maior que "
                         "zero." % (onde, quantas))
                elif not transcrito:
                    erro("%s: `atracoes_declaradas_pelo_passe` %r sem "
                         "`atracoes_declaradas_transcrito_de`. Numero que vira campo diz "
                         "de qual frase saiu." % (onde, quantas))
                elif not _declara_o_numero(transcrito, quantas):
                    erro("%s: `atracoes_declaradas_pelo_passe` %r nao aparece em "
                         "`atracoes_declaradas_transcrito_de` (%r), nem em digito nem por "
                         "extenso. O numero do passe e TRANSCRITO da frase de quem o "
                         "vende: e justamente o numero que os artigos do nicho publicam "
                         "sem dizer de onde saiu." % (onde, quantas, transcrito[:90]))
        else:
            for campo in ("atracoes_declaradas_pelo_passe",
                          "atracoes_declaradas_transcrito_de",
                          "motivo_sem_atracoes_declaradas"):
                if campo in exp:
                    erro("%s: `%s` gravado numa experiencia de categoria %r. O esquema "
                         "PROIBE: so passe de cidade declara quantas atracoes cobre, e "
                         "dar o campo a um ingresso avulso faria a F3 procurar cobertura "
                         "onde nao ha passe." % (onde, campo, exp.get("categoria")))

        for campo, motivo in (("temporada", "motivo_sem_temporada"),
                              ("imagem", "motivo_sem_imagem")):
            if campo not in exp:
                erro("%s: falta o campo `%s`. Ausencia de chave e esquecimento; null "
                     "com motivo e resposta." % (onde, campo))
            elif exp.get(campo) is None and not exp.get(motivo):
                erro("%s: `%s` null sem `%s`. Lacuna com causa nomeada e dado; lacuna "
                     "muda e defeito que ninguem ve." % (onde, campo, motivo))

        # ---------------- versoes
        versoes = exp.get("versoes") or []
        if not versoes:
            erro("%s: sem `versoes`. A F1 so oferece o que o banco conhece; "
                 "experiencia sem versao nao tem o que oferecer." % onde)
        vistos = set()
        precos_por_id = {}
        faixas_por_versao = {}
        lacunas_por_versao = {}
        for versao in versoes:
            n_versoes += 1
            vid = versao.get("id")
            ondev = "%s/versoes/%s" % (onde, vid or "?")
            if not vid:
                erro("%s: sem `id`." % ondev)
            elif vid in vistos:
                erro("%s: `id` de versao repetido dentro da experiencia." % ondev)
            vistos.add(vid)

            if not versao.get("rotulo"):
                erro("%s: sem `rotulo`." % ondev)

            preco = versao.get("preco")
            if preco is None:
                if not versao.get("motivo_sem_preco"):
                    erro("%s: `preco` null sem `motivo_sem_preco`." % ondev)
            elif not isinstance(preco, (int, float)) or preco <= 0:
                erro("%s: `preco` %r nao e numero positivo." % (ondev, preco))
            precos_por_id[vid] = preco

            if not em_vocab("moeda", versao.get("moeda")):
                erro("%s: `moeda` %r fora do vocabulario." % (ondev, versao.get("moeda")))
            elif cidade is not None and versao.get("moeda") != cidade.get("moeda_local"):
                erro("%s: `moeda` %r nao e a moeda em que o operador desta cidade cobra "
                     "(%r). O banco guarda a moeda do operador, nunca uma convertida por "
                     "esta ilha — as constantes de cambio estao PENDENTES e constante "
                     "pendente e proibida em formula publicada (secao 10)."
                     % (ondev, versao.get("moeda"), cidade.get("moeda_local")))
            # O CONTADOR DE BRL CONTAVA A COISA ERRADA, e so dava para ver com um
            # registro em real dentro (27/10/2026, carga do Bondinho). Este `+= 1`
            # morava DENTRO do `elif` acima, que e um ramo de ERRO: ele contava versao
            # cuja moeda DISCORDA da moeda do operador daquela cidade, e publicava o
            # numero sob a chave `experiencias_com_preco_em_brl`. Com o banco inteiro
            # em EUR e USD o ramo nunca rodava, a chave saia 0 e 0 era a verdade por
            # ACIDENTE: nenhuma experiencia cobrava em real. Hoje uma cobra, e a chave
            # continuaria dizendo 0 — numero certo que vira errado calado quando o
            # mundo muda, a mesma familia do `/status` verde da 20.4 e do titulo que
            # diz «oito» sobre uma lista de dez. Agora conta o que o nome diz.
            if versao.get("moeda") == "BRL_do_operador":
                versoes_em_brl.add(eid)

            unidade = versao.get("unidade_de_preco")
            if not em_vocab("unidade_de_preco", unidade):
                erro("%s: `unidade_de_preco` %r fora do vocabulario." % (ondev, unidade))

            # A trava da secao 26 aplicada ao campo que doi nesta ilha.
            for campo in campos_declarada_por:
                if campo not in versao:
                    erro("%s: falta o campo `%s`, que o esquema declara obrigatorio."
                         % (ondev, campo))
                    continue
                chave = "%s_declarada_por" % campo
                if versao.get(campo) is None:
                    if versao.get(chave) is not None:
                        erro("%s: `%s` e null e mesmo assim declara `%s`. Origem de um "
                             "valor que nao existe e afirmacao sobre nada."
                             % (ondev, campo, chave))
                    continue
                if not em_vocab("declarada_por", versao.get(chave)):
                    erro("%s: `%s` ausente ou fora do vocabulario (%r). O esquema exige "
                         "declaracao de origem para `%s`: sem uma das tres origens "
                         "legitimas o registro NAO nasce (secao 26.1)."
                         % (ondev, chave, versao.get(chave), campo))

            cap = versao.get("capacidade_maxima")
            if cap is None:
                if unidade != "por_pessoa":
                    erro("%s: `capacidade_maxima` null com unidade %r. Quando a unidade "
                         "nao e por pessoa, e a capacidade que produz o degrau: 6 pessoas "
                         "na gondola sao DUAS gondolas, e sem ela a conta do grupo nao "
                         "fecha." % (ondev, unidade))
            elif not isinstance(cap, int) or cap < 1:
                erro("%s: `capacidade_maxima` %r nao e inteiro maior que zero." % (ondev, cap))

            # ---- DIAS DE USO (nasceu em 22/10/2026, com o eixo das versoes)
            # A terceira conta que a secao 8 pede: o numero nao e aceito porque esta
            # gravado, e aceito porque a FRASE DA FONTE o diz. Sem isto `dias_de_uso`
            # seria um inteiro digitado por quem migrou, com cara de transcrito.
            if "dias_de_uso" not in versao:
                erro("%s: falta o campo `dias_de_uso`. Ausencia de chave e "
                     "esquecimento; null com motivo e resposta." % ondev)
            else:
                dias = versao.get("dias_de_uso")
                if eixo == "por_quantidade":
                    if dias is None:
                        erro("%s: `dias_de_uso` null numa experiencia de eixo "
                             "`por_quantidade`. A experiencia declarou que suas versoes "
                             "sao mais da mesma coisa e esta versao nao diz QUANTO — a "
                             "Conta 3 da F1 nao tem a grandeza do eixo que a propria "
                             "experiencia declarou ter." % ondev)
                    else:
                        conferir_dias_transcrito(ondev, versao, dias)
                elif eixo is not None:
                    if dias is not None:
                        erro("%s: `dias_de_uso` %r numa experiencia de eixo %r. O "
                             "esquema proibe: dar quantidade a uma versao que difere em "
                             "escopo ou em horario convida a conta que nao existe — "
                             "comprar dois ingressos de 24 horas do Coliseu NAO da a "
                             "area restrita da Experiencia Completa."
                             % (ondev, dias, eixo))
                    elif not versao.get("motivo_sem_dias_de_uso"):
                        erro("%s: `dias_de_uso` null sem `motivo_sem_dias_de_uso`."
                             % ondev)
                else:
                    # EIXO NULL — a experiencia de UMA versao. Aqui `dias_de_uso` E
                    # PERMITIDO e ate hoje nao era conferido por ninguem: um passe de
                    # cidade de validade unica (72 horas e so) cai exatamente aqui, e e
                    # a validade dele que a F3 compara com os dias da estadia. Achado em
                    # 22/10/2026 pelo bloco da F3, que precisou do campo neste mundo.
                    if dias is None:
                        if not versao.get("motivo_sem_dias_de_uso"):
                            erro("%s: `dias_de_uso` null sem `motivo_sem_dias_de_uso` "
                                 "numa experiencia de eixo null. A F3 compara a validade "
                                 "do passe com os dias da estadia: sem o campo e sem o "
                                 "motivo ela nao sabe se nao ha validade ou se ninguem a "
                                 "leu, e as duas dao telas diferentes." % ondev)
                    else:
                        conferir_dias_transcrito(ondev, versao, dias)

            # ---- FAIXA ETARIA (desceu para a VERSAO em 22/10/2026)
            if "faixa_etaria" not in versao:
                erro("%s: falta o campo `faixa_etaria`. Ausencia de chave e "
                     "esquecimento; null com motivo e resposta." % ondev)
            else:
                faixas = versao.get("faixa_etaria")
                if faixas is None:
                    if not versao.get("motivo_sem_faixa_etaria"):
                        erro("%s: `faixa_etaria` null sem `motivo_sem_faixa_etaria`."
                             % ondev)
                elif not isinstance(faixas, list) or not faixas:
                    erro("%s: `faixa_etaria` tem de ser lista NAO vazia ou null com "
                         "motivo. Lista vazia nao diz se o operador nao declara faixa "
                         "ou se ninguem leu." % ondev)
                else:
                    if faixa_proibida_quando and unidade == "por_veiculo":
                        erro("%s: faixa etaria gravada com unidade %r. O esquema proibe "
                             "(%s), e o motivo e o da gondola: onde o VEICULO e alugado "
                             "inteiro, 6 pessoas sao DUAS gondolas e a crianca nao tem "
                             "preco, tem assento. `por_cabine` e `por_grupo` ficam de "
                             "FORA desta proibicao de proposito — ver o esquema."
                             % (ondev, unidade, faixa_proibida_quando))
                    if versao.get("faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu") is None:
                        erro("%s: faixa etaria gravada e falta "
                             "`faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu`. "
                             "Versao que declara ALGUMA faixa tem de responder pelas que "
                             "nao declara — lista vazia e a resposta 'nenhuma falta'."
                             % ondev)
                    rotulos_vistos = set()
                    for faixa in faixas:
                        ondef = "%s/faixa_etaria/%s" % (ondev, faixa.get("rotulo") or "?")
                        if not faixa.get("rotulo"):
                            erro("%s: faixa sem `rotulo`. O rotulo e o que permite "
                                 "contar a mesma faixa entre versoes irmas." % ondev)
                            continue
                        if faixa["rotulo"] in rotulos_vistos:
                            erro("%s: `rotulo` de faixa repetido dentro da versao."
                                 % ondef)
                        rotulos_vistos.add(faixa["rotulo"])
                        faixas_por_versao.setdefault(vid, {})[faixa["rotulo"]] = faixa

                        fpreco = faixa.get("preco")
                        if "preco" not in faixa:
                            erro("%s: faixa sem o campo `preco`." % ondef)
                        elif fpreco is None:
                            if not faixa.get("motivo_sem_preco"):
                                erro("%s: faixa com `preco` null sem `motivo_sem_preco`. "
                                     "Faixa que a fonte NOMEIA sem dizer o preco e dado "
                                     "sobre a fonte; faixa sem numero e sem motivo e "
                                     "lacuna muda." % ondef)
                        elif not isinstance(fpreco, (int, float)) or fpreco < 0:
                            erro("%s: faixa com `preco` %r, que nao e numero maior ou "
                                 "igual a zero. Zero e preco — e a gratuidade declarada."
                                 % (ondef, fpreco))
                        elif isinstance(preco, (int, float)) and fpreco > preco:
                            erro("%s: faixa custando %r onde o bilhete inteiro custa %r. "
                                 "Faixa etaria e o que o operador cobra de QUEM TEM "
                                 "AQUELA IDADE: mais caro que a tarifa cheia nao e faixa, "
                                 "e numero no campo errado." % (ondef, fpreco, preco))

                        if faixa.get("moeda") != versao.get("moeda"):
                            erro("%s: faixa em %r e a versao cobra em %r. Faixa em outra "
                                 "moeda seria conversao feita por esta ilha, e as "
                                 "constantes de cambio estao PENDENTES (secao 10)."
                                 % (ondef, faixa.get("moeda"), versao.get("moeda")))

                        for campo_f, motivo_f in (("condicao", "motivo_sem_condicao"),
                                                  ("se_nao_cumprir", "motivo_sem_se_nao_cumprir")):
                            if campo_f not in faixa:
                                erro("%s: faixa sem o campo `%s`." % (ondef, campo_f))
                            elif faixa.get(campo_f) is None and not faixa.get(motivo_f):
                                erro("%s: faixa com `%s` null sem `%s`."
                                     % (ondef, campo_f, motivo_f))

                        if not faixa.get("declarado_como"):
                            erro("%s: faixa sem `declarado_como`. Sem a frase da fonte a "
                                 "tela parafraseia a regra de idade — que e a frase que "
                                 "custa dinheiro na bilheteria." % ondef)
                        ffonte = faixa.get("fonte")
                        if ffonte not in fontes:
                            erro("%s: faixa com `fonte` %r que nao existe em fontes[]."
                                 % (ondef, ffonte))
                        else:
                            fontes_usadas.add(ffonte)
                        if not _e_data(faixa.get("data_leitura")):
                            erro("%s: faixa sem `data_leitura` valida. Preco sem data de "
                                 "leitura nao existe nesta ilha, e preco de crianca "
                                 "tambem e preco." % ondef)

                        quantas_p = conferir_provas_adicionais(ondef, faixa)
                        if quantas_p:
                            n_tarifas_com_prova_adicional[0] += 1
                            n_provas_adicionais[0] += quantas_p

                    # ---- residencia NUNCA entra em faixa etaria (regra de 27/10/2026)
                    # E este e o sentido que a ilha ia errar: na carga do Bondinho os
                    # CINCO precos do mesmo bilhete vieram na mesma leitura, e a saida
                    # barata era chamar os cinco de faixa.
                    for faixa in faixas:
                        alvo = "%s %s" % (faixa.get("rotulo") or "", faixa.get("condicao") or "")
                        if PADRAO_RESIDENCIA.search(alvo):
                            erro("%s/faixa_etaria/%s: a condicao desta faixa declara "
                                 "residencia ou nacionalidade (%r). Faixa etaria prova "
                                 "IDADE; este preco e de ELEGIBILIDADE. Os dois guardam "
                                 "um preco menor com uma condicao ao lado, e e por isso "
                                 "que a troca passa calada."
                                 % (ondev, faixa.get("rotulo") or "?", alvo.strip()))

                for lacuna in versao.get("faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu") or []:
                    if not lacuna.get("rotulo") or not lacuna.get("por_que"):
                        erro("%s: entrada de "
                             "`faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu` "
                             "sem `rotulo` ou sem `por_que`. Lacuna contada sem causa "
                             "nomeada e a lacuna muda com outro nome." % ondev)
                    else:
                        lacunas_por_versao.setdefault(vid, set()).add(lacuna["rotulo"])
                        n_lacunas_de_faixa += 1

            # ---- ELEGIBILIDADE: o preco de quem prova o que NAO e idade (27/10/2026)
            if "elegibilidade" not in versao:
                erro("%s: falta o campo `elegibilidade`. Ausencia de chave e "
                     "esquecimento; null com motivo e resposta." % ondev)
            else:
                elegs = versao.get("elegibilidade")
                if elegs is None:
                    if not versao.get("motivo_sem_elegibilidade"):
                        erro("%s: `elegibilidade` null sem `motivo_sem_elegibilidade`. "
                             "Sem o motivo a tela nao sabe se o operador nao cobra por "
                             "residencia ou se ninguem leu, e as duas dao telas "
                             "diferentes." % ondev)
                elif not isinstance(elegs, list) or not elegs:
                    erro("%s: `elegibilidade` tem de ser lista NAO vazia ou null com "
                         "motivo. Lista vazia nao diz qual das duas coisas aconteceu."
                         % ondev)
                else:
                    rotulos_eleg = set()
                    tem_faixa = isinstance(versao.get("faixa_etaria"), list) \
                        and bool(versao.get("faixa_etaria"))
                    for eleg in elegs:
                        onde_e = "%s/elegibilidade/%s" % (ondev, eleg.get("rotulo") or "?")
                        if not eleg.get("rotulo"):
                            erro("%s: elegibilidade sem `rotulo`." % ondev)
                            continue
                        if eleg["rotulo"] in rotulos_eleg:
                            erro("%s: `rotulo` de elegibilidade repetido dentro da versao."
                                 % onde_e)
                        rotulos_eleg.add(eleg["rotulo"])
                        n_elegibilidades[0] += 1

                        prova = eleg.get("o_que_se_prova")
                        if not em_vocab("o_que_se_prova", prova):
                            erro("%s: `o_que_se_prova` %r fora do vocabulario. IDADE nao "
                                 "esta nele de proposito: idade e FAIXA_ETARIA."
                                 % (onde_e, prova))

                        # ---- idade NUNCA entra em elegibilidade (o outro sentido)
                        alvo = "%s %s" % (eleg.get("rotulo") or "", eleg.get("condicao") or "")
                        if PADRAO_IDADE.search(alvo):
                            erro("%s: a condicao desta elegibilidade declara uma faixa de "
                                 "idade (%r). Elegibilidade prova residencia, "
                                 "nacionalidade ou vinculo; este preco e de FAIXA_ETARIA."
                                 % (onde_e, alvo.strip()))

                        epreco = eleg.get("preco")
                        if "preco" not in eleg:
                            erro("%s: elegibilidade sem o campo `preco`." % onde_e)
                        elif epreco is None:
                            if not eleg.get("motivo_sem_preco"):
                                erro("%s: `preco` null sem `motivo_sem_preco`." % onde_e)
                        elif not isinstance(epreco, (int, float)) or epreco < 0:
                            erro("%s: `preco` %r nao e numero maior ou igual a zero. Zero "
                                 "e preco — e a gratuidade declarada." % (onde_e, epreco))
                        elif isinstance(preco, (int, float)) and epreco > preco:
                            erro("%s: elegibilidade custando %r onde o bilhete inteiro "
                                 "custa %r. Elegibilidade e o que o operador cobra de "
                                 "quem PROVA a condicao: mais caro que a tarifa cheia nao "
                                 "e desconto de ninguem, e numero no campo errado."
                                 % (onde_e, epreco, preco))

                        if eleg.get("moeda") != versao.get("moeda"):
                            erro("%s: elegibilidade em %r e a versao cobra em %r. Moeda "
                                 "diferente seria conversao feita por esta ilha, e as "
                                 "constantes de cambio estao PENDENTES."
                                 % (onde_e, eleg.get("moeda"), versao.get("moeda")))

                        for campo_e, motivo_e in (("condicao", "motivo_sem_condicao"),
                                                  ("se_nao_cumprir", "motivo_sem_se_nao_cumprir")):
                            if campo_e not in eleg:
                                erro("%s: elegibilidade sem o campo `%s`."
                                     % (onde_e, campo_e))
                            elif eleg.get(campo_e) is None and not eleg.get(motivo_e):
                                erro("%s: `%s` null sem `%s`." % (onde_e, campo_e, motivo_e))

                        quantas_p = conferir_provas_adicionais(
                            onde_e, eleg, eleg.get("o_que_se_prova"))
                        if quantas_p:
                            n_tarifas_com_prova_adicional[0] += 1
                            n_provas_adicionais[0] += quantas_p

                        # ---- a soma nao se presume
                        if "acumula_com_faixa_etaria" not in eleg:
                            erro("%s: falta `acumula_com_faixa_etaria`. E o campo que "
                                 "impede a F1 de multiplicar elegibilidade por faixa "
                                 "etaria — ver `regra_da_elegibilidade.a_soma_nao_se_presume`."
                                 % onde_e)
                        else:
                            acumula = eleg.get("acumula_com_faixa_etaria")
                            if acumula is None:
                                if tem_faixa:
                                    erro("%s: `acumula_com_faixa_etaria` null numa versao "
                                         "que TEM faixa etaria. E exatamente o caso em que "
                                         "a regua precisa saber se pode somar, e com null "
                                         "ela nao sabe." % onde_e)
                                elif not eleg.get("motivo_sem_acumula_com_faixa_etaria"):
                                    erro("%s: `acumula_com_faixa_etaria` null sem "
                                         "`motivo_sem_acumula_com_faixa_etaria`." % onde_e)
                            elif not isinstance(acumula, bool):
                                erro("%s: `acumula_com_faixa_etaria` %r nao e booleano."
                                     % (onde_e, acumula))
                            elif acumula is True:
                                frase = "%s %s" % (eleg.get("declarado_como") or "",
                                                   eleg.get("condicao") or "")
                                if not re.search(r"(acumul)|(soma)|(junto com)|(cumulat)",
                                                 frase, re.I):
                                    erro("%s: `acumula_com_faixa_etaria` true e nem "
                                         "`declarado_como` nem `condicao` trazem a frase "
                                         "da fonte que AUTORIZA somar. Silencio nunca "
                                         "autoriza soma: no Bondinho, metade de R$ 160 "
                                         "seria R$ 80, e R$ 80 nao e preco de nada."
                                         % onde_e)

                        if not eleg.get("declarado_como"):
                            erro("%s: elegibilidade sem `declarado_como`. Sem a frase da "
                                 "fonte a tela parafraseia a regra de quem tem direito — "
                                 "que e a frase que custa dinheiro na bilheteria."
                                 % onde_e)
                        efonte = eleg.get("fonte")
                        if efonte not in fontes:
                            erro("%s: `fonte` %r nao existe em fontes[]."
                                 % (onde_e, efonte))
                        else:
                            fontes_usadas.add(efonte)
                        if not _e_data(eleg.get("data_leitura")):
                            erro("%s: sem `data_leitura` valida. Preco sem data de leitura "
                                 "nao existe nesta ilha, e preco de brasileiro tambem e "
                                 "preco." % onde_e)

            if "duracao_minutos" not in versao:
                erro("%s: falta `duracao_minutos`." % ondev)
            elif versao.get("duracao_minutos") is None and not versao.get("motivo_sem_duracao"):
                erro("%s: `duracao_minutos` null sem `motivo_sem_duracao`." % ondev)

            if not em_vocab("momento_do_dia", versao.get("momento_do_dia")):
                erro("%s: `momento_do_dia` %r fora do vocabulario."
                     % (ondev, versao.get("momento_do_dia")))

            for lista, motivo in (("inclui", "inclui_motivo_lista_vazia"),
                                  ("nao_inclui", "nao_inclui_motivo_lista_vazia")):
                if not isinstance(versao.get(lista), list):
                    erro("%s: `%s` ausente ou nao e lista." % (ondev, lista))
                elif not versao.get(lista) and not versao.get(motivo):
                    erro("%s: `%s` vazia sem `%s`. Lista vazia nao some da tela: ela diz "
                         "que o operador nao declara o que esta incluso, e isso e "
                         "informacao sobre o operador." % (ondev, lista, motivo))

            for acrescimo in versao.get("acrescimos") or []:
                ondea = "%s/acrescimos" % ondev
                if not acrescimo.get("o_que_e") or not acrescimo.get("declarado_como"):
                    erro("%s: acrescimo sem `o_que_e` ou sem `declarado_como`." % ondea)
                    continue
                frase = acrescimo["declarado_como"].lower()
                hedge = next((h for h in HEDGES if h in frase), None)
                if hedge and acrescimo.get("aproximado") is not True:
                    erro("%s: `declarado_como` diz %r e `aproximado` nao e true. O 'mais "
                         "ou menos' e da fonte e nao pode virar numero seco na tela."
                         % (ondea, hedge))
                if not hedge and acrescimo.get("aproximado") is True:
                    erro("%s: `aproximado` true mas a frase da fonte nao tem ressalva "
                         "nenhuma. Ressalva inventada tambem e invencao." % ondea)

            fid = versao.get("fonte")
            if fid not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (ondev, fid))
            else:
                fontes_usadas.add(fid)
                if not _e_data(versao.get("data_leitura")):
                    erro("%s: `data_leitura` ausente ou nao e data. Preco sem data de "
                         "leitura nao existe nesta ilha — e o defeito mais grave que o "
                         "VOZ.md nomeia." % ondev)
                else:
                    origem = fontes[fid].get("origem") or ""
                    dias = int(validade.get("tarifa_de_poder_publico_dias", 180)) \
                        if "poder-publico" in origem \
                        else int(validade.get("operador_privado_dias", 60))
                    lido = datetime.date.fromisoformat(versao["data_leitura"])
                    if (hoje - lido).days > dias:
                        vencidos.append("%s (lido em %s, validade de %d dias)"
                                        % (ondev, versao["data_leitura"], dias))

            if not versao.get("declarado_como"):
                erro("%s: sem `declarado_como`. Sem a frase da fonte, a tela parafraseia "
                     "em vez de citar." % ondev)

        # ---------------- FAIXA ETARIA ENTRE VERSOES IRMAS
        # Esta e a regua que so pode existir depois de 22/10/2026, e e a razao inteira
        # de a faixa ter descido para a VERSAO: com o campo na EXPERIENCIA nao havia
        # irmas para comparar. Tres coisas se medem aqui, e as tres sao sobre a mesma
        # fonte lida uma vez e transcrita N vezes.
        todos_os_rotulos = set()
        for mapa in faixas_por_versao.values():
            todos_os_rotulos.update(mapa)
        for vid_f, mapa in sorted(faixas_por_versao.items()):
            ondev = "%s/versoes/%s" % (onde, vid_f)
            n_faixas_de_idade += len(mapa)
            faltando = todos_os_rotulos - set(mapa) - lacunas_por_versao.get(vid_f, set())
            for rotulo in sorted(faltando):
                erro("%s: a faixa %r existe em outra versao desta experiencia e aqui ela "
                     "nao e declarada NEM contada em "
                     "`faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu`. Ausencia "
                     "silenciosa de faixa e indistinguivel de 'o operador nao cobra faixa "
                     "neste bilhete', e as duas coisas custam dinheiro diferente na porta."
                     % (ondev, rotulo))

        # A mesma faixa, no mesmo preco e na mesma moeda, transcrita com DUAS frases
        # diferentes: a fonte foi lida uma vez, entao uma das duas frases foi escrita
        # pela ilha e nao pelo operador.
        for rotulo in sorted(todos_os_rotulos):
            frases = {}
            for vid_f, mapa in faixas_por_versao.items():
                faixa = mapa.get(rotulo)
                if not faixa:
                    continue
                chave = (faixa.get("preco"), faixa.get("moeda"))
                frases.setdefault(chave, {})[vid_f] = faixa.get("declarado_como")
            for chave, por_versao_ in sorted(frases.items(), key=lambda kv: repr(kv[0])):
                if len(por_versao_) > 1 and len(set(por_versao_.values())) > 1:
                    erro("%s: a faixa %r custa %r %s em %s e cada uma transcreve a fonte "
                         "com uma frase diferente. Mesmo numero, mesma moeda e mesma "
                         "leitura: uma das frases nao e da fonte."
                         % (onde, rotulo, chave[0], chave[1],
                            ", ".join(sorted(por_versao_))))

        # O NUMERO DA FRASE E DE OUTRA VERSAO — achado da migracao, no Angkor: a fonte
        # escreve que a crianca sem passaporte paga US$ 37, e 37 e o passe de UM DIA. A
        # mesma frase guardada num campo de EXPERIENCIA valia para os tres passes.
        for vid_f, mapa in sorted(faixas_por_versao.items()):
            ondev = "%s/versoes/%s" % (onde, vid_f)
            meu_preco = precos_por_id.get(vid_f)
            outros = {p for v2, p in precos_por_id.items()
                      if v2 != vid_f and isinstance(p, (int, float))}
            for rotulo, faixa in sorted(mapa.items()):
                frase = " ".join(str(faixa.get(k) or "")
                                 for k in ("declarado_como", "se_nao_cumprir"))
                numeros = set()
                for bruto in re.findall(r"\d+(?:[.,]\d+)?", frase):
                    try:
                        numeros.add(float(bruto.replace(",", ".")))
                    except ValueError:
                        pass
                de_outra = {p for p in outros if p in numeros and p != meu_preco}
                if de_outra and not faixa.get("numero_da_frase_e_de_outra_versao"):
                    erro("%s: a frase da faixa %r cita %s, que e o preco de OUTRA versao "
                         "desta experiencia e nao desta (%r), e a faixa nao traz "
                         "`numero_da_frase_e_de_outra_versao`. Frase da fonte colada numa "
                         "versao que ela nao descreve poe na boca do operador um numero "
                         "que ele nao disse daquele bilhete."
                         % (ondev, rotulo,
                            ", ".join(repr(p) for p in sorted(de_outra)), meu_preco))

        # ---------------- a regra do documento nomeado (esquema, 26.2)
        # O que sustenta o PRECO de um registro sao as fontes das versoes dele. Se
        # alguma delas e de nivel de autoridade e nao nomeia documento, o registro
        # entra como pendente_de_releitura e nunca como publicavel.
        if status_sem_documento:
            mudas = [v.get("fonte") for v in versoes
                     if fontes.get(v.get("fonte"), {}).get("nivel") in niveis_de_autoridade
                     and fontes.get(v.get("fonte"), {}).get("documento") is None]
            if mudas and exp.get("status") != status_sem_documento:
                erro("%s: `status` %r com preco sustentado por fonte de autoridade que "
                     "NAO nomeia documento (%s). O esquema manda %r nesse caso: o "
                     "registro entra, e entra a reconferir. Autoridade de que so se "
                     "ouviu falar nao vale o mesmo que autoridade com ato citado, e "
                     "antes desta regra as duas tinham o mesmo nivel."
                     % (onde, exp.get("status"), ", ".join(sorted(set(mudas))),
                        status_sem_documento))

        # ---------------- declaracoes divergentes
        declaracoes = exp.get("declaracoes")
        if not isinstance(declaracoes, list):
            erro("%s: `declaracoes` ausente ou nao e lista. Lista vazia e afirmacao "
                 "(ninguem mais publicou numero); chave ausente e esquecimento." % onde)
            declaracoes = []
        for i, dec in enumerate(declaracoes):
            n_declaracoes += 1
            onded = "%s/declaracoes[%d]" % (onde, i)
            if "versao" not in dec:
                erro("%s: falta o campo `versao`. Divergencia e sobre a VERSAO, nunca "
                     "sobre a experiencia: numa escada de dias, comparar o preco de 1 dia "
                     "com o de 3 e comparar dois produtos." % onded)
            elif dec.get("versao") is None:
                if not dec.get("motivo_sem_versao"):
                    erro("%s: `versao` null sem `motivo_sem_versao`." % onded)
                sem_versao += 1
            elif dec.get("versao") not in precos_por_id:
                erro("%s: `versao` %r nao e uma versao desta experiencia."
                     % (onded, dec.get("versao")))
            if dec.get("publicador") is None and not dec.get("motivo_sem_publicador"):
                erro("%s: `publicador` null sem `motivo_sem_publicador`." % onded)
            esperado = dec.get("publicador") is not None
            if dec.get("publicavel_na_tela") is not esperado:
                erro("%s: `publicavel_na_tela` gravado como %r e a derivacao da %r. "
                     "Declaracao so vai para a tela com nome: 'algumas paginas dizem X' "
                     "e a frase sem dono que esta ilha existe para nao escrever."
                     % (onded, dec.get("publicavel_na_tela"), esperado))
            if esperado:
                n_publicaveis += 1
            if dec.get("url") is None and not dec.get("motivo_sem_url"):
                erro("%s: `url` null sem `motivo_sem_url`." % onded)
            if not dec.get("diz"):
                erro("%s: sem `diz`." % onded)
            if not em_vocab("unidade_de_preco", dec.get("unidade_de_preco")):
                erro("%s: `unidade_de_preco` %r fora do vocabulario."
                     % (onded, dec.get("unidade_de_preco")))
            if not em_vocab("moeda", dec.get("moeda")):
                erro("%s: `moeda` %r fora do vocabulario." % (onded, dec.get("moeda")))
            if not _e_data(dec.get("data_leitura")):
                erro("%s: `data_leitura` ausente ou nao e data." % onded)
            if _maximo(dec.get("valor")) is None:
                erro("%s: `valor` %r nao e numero nem faixa {minimo, maximo}."
                     % (onded, dec.get("valor")))
            if dec.get("fonte") not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (onded, dec.get("fonte")))
            else:
                fontes_usadas.add(dec["fonte"])

        # ---------------- resolucao: a proibicao de media, em codigo
        resolucao = exp.get("resolucao")
        if declaracoes and not resolucao:
            erro("%s: ha declaracoes divergentes e nao ha `resolucao`. Divergencia sem "
                 "resolucao escrita e a ilha empurrando a duvida para quem le." % onde)
        if not declaracoes and resolucao:
            erro("%s: ha `resolucao` e nenhuma declaracao divergente para resolver." % onde)
        if declaracoes and resolucao:
            onder = "%s/resolucao" % onde
            if not resolucao.get("erro_caro"):
                erro("%s: sem `erro_caro`. Antes de resolver qualquer divergencia se "
                     "escreve qual e o erro caro — a direcao sai sozinha depois disso "
                     "(secao 10)." % onder)
            if not resolucao.get("texto"):
                erro("%s: sem `texto`." % onder)

            vid = resolucao.get("versao_resolvida")
            if vid not in precos_por_id:
                erro("%s: `versao_resolvida` %r nao e uma versao desta experiencia."
                     % (onder, vid))
            else:
                versao = next(v for v in versoes if v.get("id") == vid)
                if resolucao.get("valor") != versao.get("preco"):
                    erro("%s: `valor` %r nao e o preco da versao resolvida (%r). O valor "
                         "resolvido E o que vai para a tela; dois numeros para a mesma "
                         "coisa no mesmo registro e armadilha, nao historia."
                         % (onder, resolucao.get("valor"), versao.get("preco")))
                if resolucao.get("unidade_de_preco") != versao.get("unidade_de_preco"):
                    erro("%s: `unidade_de_preco` %r difere da versao resolvida (%r)."
                         % (onder, resolucao.get("unidade_de_preco"),
                            versao.get("unidade_de_preco")))
                if resolucao.get("moeda") != versao.get("moeda"):
                    erro("%s: `moeda` %r difere da versao resolvida (%r)."
                         % (onder, resolucao.get("moeda"), versao.get("moeda")))

            fid = resolucao.get("fonte")
            if fid not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (onder, fid))
            else:
                fontes_usadas.add(fid)
                origem = fontes[fid].get("origem") or ""
                tem_autoridade = "poder-publico" in origem
                if resolucao.get("por_autoridade") is not tem_autoridade:
                    erro("%s: `por_autoridade` gravado como %r e a escada diz %r para a "
                         "origem %r. Autoridade nao se declara, se le da escada."
                         % (onder, resolucao.get("por_autoridade"), tem_autoridade, origem))

                if not tem_autoridade:
                    # Sem autoridade resolve para o MAIOR. Media nao se reconhece pelo
                    # nome: ela se reconhece por cair entre o minimo e o maximo sem ser
                    # nenhum dos dois.
                    #
                    # E os candidatos sao os da VERSAO RESOLVIDA, nunca os da
                    # experiencia inteira: numa escada de dias, o preco de 3 dias e
                    # outro produto. Declaracao sem versao atribuida e conteudo na
                    # tela e nao e voto na conta.
                    unidade = resolucao.get("unidade_de_preco")
                    candidatos = []
                    comparaveis = []
                    versao_alvo = next((v for v in versoes if v.get("id") == vid), None)
                    if versao_alvo and isinstance(versao_alvo.get("preco"), (int, float)):
                        candidatos.append(float(versao_alvo["preco"]))
                    for dec in declaracoes:
                        if dec.get("versao") == vid and dec.get("unidade_de_preco") == unidade:
                            topo = _maximo(dec.get("valor"))
                            if topo is not None:
                                candidatos.append(topo)
                                comparaveis.append(dec)
                    if candidatos:
                        alvo = max(candidatos)
                        valor = resolucao.get("valor")
                        if isinstance(valor, (int, float)) and float(valor) != alvo:
                            piso = min(candidatos + [_minimo(d.get("valor")) or alvo
                                                     for d in comparaveis])
                            if piso < float(valor) < alvo:
                                erro("%s: sem autoridade, o valor resolvido %r cai ENTRE "
                                     "%r e %r sem ser nenhum dos dois. Isso e media com "
                                     "outro nome, e media e a unica saida proibida: ela "
                                     "esconde exatamente o desacordo que faz a pagina "
                                     "valer." % (onder, valor, piso, alvo))
                            else:
                                erro("%s: sem autoridade a regra resolve para o MAIOR "
                                     "(%r) e o gravado e %r. O erro caro desta ilha e "
                                     "subestimar." % (onder, alvo, valor))

        # ---------------- afiliado: o piso da 25.2
        afiliado = exp.get("afiliado")
        if not isinstance(afiliado, dict):
            erro("%s: sem `afiliado`. O piso de compra nasce com o item." % onde)
            sem_saida += 1
        else:
            ondea = "%s/afiliado" % onde
            if "url" not in afiliado or not isinstance(afiliado.get("url"), str):
                erro("%s: `url` ausente. Ela nasce PRESENTE E VAZIA — string vazia "
                     "declara que o campo existe e nao tem link rastreado; chave ausente "
                     "e esquecimento." % ondea)
            if afiliado.get("url_produto") is None and not afiliado.get("motivo_sem_url_produto"):
                erro("%s: `url_produto` null sem `motivo_sem_url_produto` (25.4-b: sem "
                     "URL crua o teste de vida e impossivel)." % ondea)

            piso = afiliado.get("url_busca_produto")
            if not piso:
                erro("%s: SEM PISO DE COMPRA. Item sem saida de compra e defeito da 19.1, "
                     "sempre — e 'link de loja em breve' esta proibido (secao 7)." % ondea)
                sem_saida += 1
            elif molde_piso and cidade is not None:
                derivado = molde_piso.replace("{slug_plataforma}", cidade.get("slug_plataforma") or "")
                if piso != derivado:
                    erro("%s: `url_busca_produto` gravada como %r e a derivacao do molde "
                         "com o slug da cidade da %r. O piso e fabricado a partir da "
                         "cidade, nunca digitado: URL digitada envelhece calada no dia em "
                         "que o molde mudar." % (ondea, piso, derivado))

            if not afiliado.get("url"):
                piso_nao_rastreavel += 1

            rel = afiliado.get("rel") or ""
            if afiliado.get("programa") is None:
                esperado_rel = esquema.get("piso_de_compra", {}).get("rel_enquanto_nao_ha_programa")
                if esperado_rel and rel != esperado_rel:
                    erro("%s: sem programa cadastrado, `rel` tem de ser %r e esta %r."
                         % (ondea, esperado_rel, rel))
                if "sponsored" in rel:
                    erro("%s: `rel` tem `sponsored` e nao ha programa de afiliado. "
                         "sponsored declara relacao PAGA, e ninguem esta pagando por este "
                         "clique." % ondea)

            esperado_int = bool(afiliado.get("url")) and afiliado.get("url_produto") is None
            if afiliado.get("intestavel") is not esperado_int:
                erro("%s: `intestavel` gravado como %r e a derivacao da %r."
                     % (ondea, afiliado.get("intestavel"), esperado_int))
            if esperado_int:
                intestaveis += 1

    # ------------------------------------------------------------------
    # 4b. FAIXAS DIARIAS — hospedagem, alimentacao e transporte local
    #
    # Estas NAO sao nossas: sao faixa que um terceiro publicou, e e por isso que
    # elas tem campos que a EXPERIENCIA nao tem (`publicado_por`, `metodo_declarado`,
    # `o_que_o_numero_e`). A regua existe ANTES do primeiro registro de proposito: o
    # banco tem zero faixas hoje, e regua escrita no dia da carga e regua que nasce
    # moldada ao dado que veio.
    # ------------------------------------------------------------------
    faixas = {}
    n_faixas_publicaveis = 0
    for faixa in banco.get("faixas_diarias", []):
        fxid = faixa.get("id")
        onde = "faixas_diarias/%s" % (fxid or "?")
        if not fxid:
            erro("%s: sem `id`." % onde)
            continue
        if fxid in faixas:
            erro("%s: `id` repetido." % onde)
        faixas[fxid] = faixa

        if faixa.get("cidade") not in cidades:
            erro("%s: `cidade` %r nao esta no banco. Faixa de cidade que a ilha nao "
                 "conhece nao tem pagina onde ser publicada." % (onde, faixa.get("cidade")))
        for chave, campo in (("categoria_de_custo", "categoria_de_custo"),
                             ("padrao_de_viagem", "padrao"),
                             ("base_da_faixa", "base"),
                             ("o_que_o_numero_e", "o_que_o_numero_e"),
                             ("moeda", "moeda"),
                             ("status_do_registro", "status")):
            if not em_vocab(chave, faixa.get(campo)):
                erro("%s: `%s` %r fora do vocabulario `%s`."
                     % (onde, campo, faixa.get(campo), chave))

        vmin, vmax = faixa.get("valor_min"), faixa.get("valor_max")
        for nome, valor in (("valor_min", vmin), ("valor_max", vmax)):
            if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor <= 0:
                erro("%s: `%s` %r nao e numero maior que zero. Faixa sem numero nao e "
                     "faixa." % (onde, nome, valor))
        if isinstance(vmin, (int, float)) and isinstance(vmax, (int, float)) \
                and not isinstance(vmin, bool) and not isinstance(vmax, bool) and vmax < vmin:
            erro("%s: `valor_max` %r menor que `valor_min` %r. Faixa invertida publica um "
                 "intervalo vazio com cara de intervalo." % (onde, vmax, vmin))

        # A BASE e a licao da `unidade_de_preco` um andar acima, e ela exige a frase
        # de onde saiu: multiplicar diaria de QUARTO pelo numero de pessoas continua
        # parecendo dinheiro, e e por isso que ninguem ve o erro.
        if not (faixa.get("base_transcrita_de") or "").strip():
            erro("%s: `base` declarada sem `base_transcrita_de`. A base e a grandeza a "
                 "que o numero se refere, e ela existe SO na prosa de quem publicou: sem "
                 "a frase copiada, a regua esta confiando que alguem leu certo." % onde)

        # A OCUPACAO DO QUARTO, quando a base e por quarto: sem ela a faixa nao
        # escala para o grupo, e a F2 recusa a linha. Mesma cobranca de `dias_de_uso`
        # um andar acima — o numero tem de APARECER na frase da fonte.
        ppq = faixa.get("pessoas_por_quarto")
        base = faixa.get("base")
        transcrita = faixa.get("base_transcrita_de") or ""
        if base == "por_quarto_por_dia":
            if ppq is None:
                if not (faixa.get("motivo_sem_pessoas_por_quarto") or "").strip():
                    erro("%s: base `por_quarto_por_dia` sem `pessoas_por_quarto` e sem "
                         "`motivo_sem_pessoas_por_quarto`. Sem a ocupacao a diaria nao "
                         "escala para o grupo: 6 pessoas numa diaria de quarto duplo sao "
                         "TRES quartos, e nao a diaria dividida por 6." % onde)
            elif not isinstance(ppq, int) or isinstance(ppq, bool) or ppq < 1:
                erro("%s: `pessoas_por_quarto` %r nao e inteiro maior ou igual a 1."
                     % (onde, ppq))
            elif not _declara_o_numero(transcrita, ppq):
                erro("%s: `pessoas_por_quarto` %d nao aparece em `base_transcrita_de` "
                     "(%r). O numero e TRANSCRITO da frase de quem publicou, nunca "
                     "suposto pela ilha — quem publica diaria de hotel quase nunca diz a "
                     "ocupacao no mesmo lugar em que diz o preco." % (onde, ppq, transcrita))
        elif ppq is not None:
            erro("%s: `pessoas_por_quarto` gravado com base %r. O esquema PROIBE ocupacao "
                 "fora da base de quarto: ali nao ha quarto a contar, e dar ocupacao a uma "
                 "faixa que nao e de quarto convida a conta que nao existe." % (onde, base))

        # O QUE O NUMERO E exige a frase exata. E a troca que esta migracao fez: a
        # distincao entre uma media e um minimo morava na prosa desde 14/09/2026.
        metodo = (faixa.get("metodo_declarado") or "").strip()
        if not metodo:
            erro("%s: `o_que_o_numero_e` declarado sem `metodo_declarado`. As duas frases "
                 "que esta ilha mediu na mesma SERP («media de R$ 203,87 nos ultimos 30 "
                 "dias» e «a diaria mais baixa encontrada foi R$ 396,84») diferem SO na "
                 "prosa: sem ela o enum e um palpite com cara de campo." % onde)

        if not (faixa.get("publicado_por") or "").strip():
            erro("%s: sem `publicado_por`. Republicar numero anonimo e exatamente o "
                 "defeito do concorrente que o bloco 1 mediu em 14/09/2026." % onde)
        if not faixa.get("url") and not (faixa.get("motivo_sem_url") or "").strip():
            erro("%s: sem `url` e sem `motivo_sem_url`. Faixa de terceiro sem endereco e "
                 "sem motivo nao pode ser reconferida por ninguem." % onde)
        if not _e_data(faixa.get("data_leitura")):
            erro("%s: `data_leitura` ausente ou nao e data. Preco sem data de leitura nao "
                 "existe nesta ilha, e faixa de terceiro nao e excecao." % onde)
        if faixa.get("status") == "publicavel":
            n_faixas_publicaveis += 1

    # A REGRA QUE A F2 CARREGA, conferida aqui e nao so escrita na descricao: duas
    # faixas publicaveis da MESMA cidade, categoria e padrao com `o_que_o_numero_e`
    # diferente nao podem virar um intervalo unico. Isso NAO e erro de banco — as duas
    # podem ser verdadeiras —, e aviso para a F2 publicar as duas lado a lado.
    naturezas = {}
    for faixa in banco.get("faixas_diarias", []):
        if faixa.get("status") != "publicavel":
            continue
        chave = (faixa.get("cidade"), faixa.get("categoria_de_custo"), faixa.get("padrao"))
        naturezas.setdefault(chave, set()).add(faixa.get("o_que_o_numero_e"))
    for chave, nats in sorted(naturezas.items()):
        if len(nats) > 1:
            aviso("faixas_diarias %s: %d naturezas diferentes de numero (%s) para a mesma "
                  "cidade, categoria e padrao. A F2 publica as duas com o nome de quem "
                  "publicou e NAO as soma num intervalo unico — somar media com minimo da "
                  "um intervalo que ninguem publicou."
                  % ("/".join(str(c) for c in chave), len(nats), ", ".join(sorted(nats))))

    # ------------------------------------------------------------------
    # 4c. COBERTURAS DE PASSE — a relacao entre um passe e UMA atracao
    #
    # A regua existe ANTES do primeiro registro, como a da FAIXA_DIARIA: o banco tem
    # ZERO coberturas hoje porque carregar exige ler a fonte do passe, e os cinco
    # dominios de passe que o corpus mediu estao recusados no egresso desta nuvem. O
    # que a torna executavel sao os mundos de ferramentas/mutacoes-banco.py, que
    # carregam passe e cobertura EM MEMORIA — a licao da FAIXA_DIARIA, cujas ~80 linhas
    # de regua quase nasceram sem ninguem para roda-las.
    # ------------------------------------------------------------------
    coberturas = {}
    n_coberturas_publicaveis = 0
    por_par = {}
    # O indice das experiencias POR ID, montado aqui e nao reaproveitado do laco acima:
    # la existe `ids`, que e um CONJUNTO e nao da acesso ao registro. Esta linha nasceu de
    # um defeito que ia estourar na primeira cobertura gravada e nunca antes dela — a
    # secao usava um `por_id` que nao existia, e com zero coberturas o laco nao roda e o
    # NameError nao acontece. E a familia exata da regra da secao 8 que esta pasta mais
    # repete: codigo que o banco de hoje nao alcanca so e medido por mundo de bancada.
    por_id = {e.get("id"): e for e in banco.get("experiencias", [])}
    for cob in banco.get("coberturas_de_passe", []):
        cid_cob = cob.get("id")
        onde = "coberturas_de_passe/%s" % (cid_cob or "?")
        if not cid_cob:
            erro("%s: sem `id`." % onde)
            continue
        if cid_cob in coberturas:
            erro("%s: `id` repetido." % onde)
        coberturas[cid_cob] = cob

        passe = por_id.get(cob.get("passe"))
        atracao = por_id.get(cob.get("experiencia"))
        if passe is None:
            erro("%s: `passe` %r nao esta no banco." % (onde, cob.get("passe")))
        elif passe.get("categoria") != "passe_de_cidade":
            erro("%s: `passe` %r tem categoria %r. Cobertura cujo passe nao e "
                 "`passe_de_cidade` e uma relacao entre dois ingressos, e essa relacao "
                 "nao existe." % (onde, cob.get("passe"), passe.get("categoria")))
        if atracao is None:
            erro("%s: `experiencia` %r nao esta no banco. Cobertura de atracao que a ilha "
                 "nao conhece nao tem avulso com que ser comparada — e e o avulso que faz "
                 "a conta da F3." % (onde, cob.get("experiencia")))
        elif atracao.get("categoria") == "passe_de_cidade":
            erro("%s: `experiencia` %r tambem e passe de cidade. Passe que cobre passe "
                 "faria a F3 somar a mesma conta duas vezes."
                 % (onde, cob.get("experiencia")))
        if passe is not None and atracao is not None \
                and passe.get("cidade") != atracao.get("cidade"):
            erro("%s: o passe e de %r e a atracao e de %r. Passe de cidade cobre atracao "
                 "DAQUELA cidade: cobertura cruzando cidade publicaria, na pagina de uma, "
                 "o valor entregue na outra." % (onde, passe.get("cidade"),
                                                 atracao.get("cidade")))

        par = (cob.get("passe"), cob.get("experiencia"))
        if par in por_par:
            erro("%s: segunda cobertura do par passe %r x atracao %r (a outra e %s). Duas "
                 "leituras do mesmo par fariam a F3 contar o valor entregue duas vezes; "
                 "leitura nova SUBSTITUI a antiga, com a data nova."
                 % (onde, par[0], par[1], por_par[par]))
        else:
            por_par[par] = cid_cob

        for chave, campo in (("forma_de_cobertura", "como"),
                             ("declarada_por", "declarada_por"),
                             ("status_do_registro", "status")):
            if not em_vocab(chave, cob.get(campo)):
                erro("%s: `%s` %r fora do vocabulario `%s`."
                     % (onde, campo, cob.get(campo), chave))

        # ---- A VERSAO COBERTA: null e resposta, ausencia e esquecimento.
        if "versao_coberta" not in cob:
            erro("%s: falta o campo `versao_coberta`. Ausencia de chave e esquecimento; "
                 "null com motivo e resposta — e a diferenca decide se a F3 publica UM "
                 "numero ou uma FAIXA." % onde)
        else:
            vc = cob.get("versao_coberta")
            if vc is None:
                if not cob.get("motivo_sem_versao_coberta"):
                    erro("%s: `versao_coberta` null sem `motivo_sem_versao_coberta`. Fonte "
                         "de passe quase nunca diz QUAL bilhete ela cobre, e esse e o caso "
                         "comum: ele vai para a tela como faixa, com o motivo." % onde)
            elif atracao is not None:
                nomes = [v.get("id") for v in (atracao.get("versoes") or [])]
                if vc not in nomes:
                    erro("%s: `versao_coberta` %r nao e uma versao de %r (as versoes sao "
                         "%s)." % (onde, vc, cob.get("experiencia"),
                                   ", ".join(repr(n) for n in nomes) or "nenhuma"))

        # ---- A RESERVA OBRIGATORIA: campo separado do `como` de proposito.
        if not isinstance(cob.get("reserva_obrigatoria"), bool):
            erro("%s: `reserva_obrigatoria` %r nao e booleano. O bloco 1 mediu, em "
                 "14/09/2026, que a fonte de topo do Roma Pass avisa que as regras de "
                 "reserva mudaram em 2026: e o dado que envelhece primeiro nesta "
                 "ferramenta, e ele nao pode ser null." % (onde, cob.get("reserva_obrigatoria")))
        elif cob.get("reserva_obrigatoria") and not (cob.get("reserva_transcrita_de") or "").strip():
            erro("%s: `reserva_obrigatoria` true sem `reserva_transcrita_de`. A regra de "
                 "reserva vai para a tela com a frase de quem a publicou, ao lado do "
                 "preco — sem a frase, ela e uma afirmacao desta ilha sobre o passe de "
                 "outro." % onde)

        # ---- O DESCONTO: o campo existe so na forma que o usa, e a HEDGE e lida.
        como = cob.get("como")
        pct = cob.get("desconto_percentual")
        teto = cob.get("desconto_e_no_maximo")
        transcrito = cob.get("desconto_transcrito_de") or ""
        if como == "desconto_declarado":
            if not isinstance(pct, (int, float)) or isinstance(pct, bool) \
                    or pct <= 0 or pct >= 100:
                erro("%s: `desconto_percentual` %r nao e numero entre 0 e 100 (exclusive). "
                     "Desconto de 100%% e entrada incluida e tem forma propria; desconto de "
                     "zero e `sem_efeito_no_preco`." % (onde, pct))
            elif not transcrito.strip():
                erro("%s: `desconto_percentual` %r sem `desconto_transcrito_de`." % (onde, pct))
            elif isinstance(pct, int) and not _declara_o_numero(transcrito, pct):
                erro("%s: `desconto_percentual` %r nao aparece em "
                     "`desconto_transcrito_de` (%r). O numero e transcrito da frase de "
                     "quem vende o passe." % (onde, pct, transcrito[:90]))
            if not isinstance(teto, bool):
                erro("%s: `desconto_e_no_maximo` %r nao e booleano. E ele que diz se «50%%» "
                     "e 50%% ou «ate 50%%» — e sem ele a hedge da fonte entra na conta como "
                     "numero cheio, com o resultado continuando a parecer dinheiro."
                     % (onde, teto))
            else:
                hedge = next((h for h in HEDGES + ("ate ", "até ", "no maximo",
                                                   "no máximo") if h in transcrito.lower()),
                             None)
                if hedge and not teto:
                    erro("%s: `desconto_transcrito_de` traz a hedge %r e "
                         "`desconto_e_no_maximo` e false. A frase diz que o desconto e um "
                         "TETO e o campo diz que e o valor: e a hedge virando numero "
                         "cheio, que e o defeito que este par de campos existe para "
                         "impedir." % (onde, hedge))
        else:
            for campo in ("desconto_percentual", "desconto_e_no_maximo",
                          "desconto_transcrito_de"):
                if cob.get(campo) is not None:
                    erro("%s: `%s` gravado com `como` %r. O esquema PROIBE desconto fora "
                         "de `desconto_declarado`: ali nao ha percentual a abater, e dar "
                         "o campo convida a conta que nao existe." % (onde, campo, como))

        if cob.get("fonte") not in fontes:
            erro("%s: `fonte` %r nao esta em fontes[]." % (onde, cob.get("fonte")))
        else:
            fontes_usadas.add(cob.get("fonte"))
        if not _e_data(cob.get("data_leitura")):
            erro("%s: `data_leitura` ausente ou nao e data. A data da COBERTURA nao e "
                 "herdada da data do preco do passe: sao duas leituras e elas envelhecem "
                 "em velocidades diferentes." % onde)
        if cob.get("status") == "publicavel":
            n_coberturas_publicaveis += 1

    # A OUTRA DIRECAO (secao 8): passe publicavel sem NENHUMA cobertura lida nao e erro
    # de banco — e o estado em que todo passe nasce —, e e AVISO porque a F3 publica o
    # passe assim mesmo, dizendo que a cobertura nao foi lida. O que seria defeito e a
    # F3 calar sobre isso, e quem cobra essa metade e o portao dela.
    for exp in banco.get("experiencias", []):
        if exp.get("categoria") != "passe_de_cidade" or exp.get("status") == "excluido_do_banco":
            continue
        quantas = sum(1 for c in banco.get("coberturas_de_passe", [])
                      if c.get("passe") == exp.get("id") and c.get("status") == "publicavel")
        declaradas = exp.get("atracoes_declaradas_pelo_passe")
        if quantas == 0:
            aviso("experiencias/%s: passe de cidade com ZERO coberturas publicaveis "
                  "lidas. A F3 publica o preco dele e NAO publica ponto de equilibrio: "
                  "nao ha valor entregue a somar, e supor cobertura seria inventar o "
                  "produto do passe." % exp.get("id"))
        elif isinstance(declaradas, int) and quantas < declaradas:
            aviso("experiencias/%s: o passe declara cobrir %d atracoes e esta ilha leu "
                  "%d. O ponto de equilibrio da F3 e sobre as %d lidas e a tela diz isso "
                  "— equilibrio sobre parte da cobertura apresentado como equilibrio do "
                  "passe e o defeito que o 1o colocado da consulta comete."
                  % (exp.get("id"), declaradas, quantas, quantas))

    # ------------------------------------------------------------------
    # 5. AS DUAS DIRECOES (secao 8): dado colhido que a tela nunca usa tambem conta
    # ------------------------------------------------------------------
    for fid in fontes:
        if fid not in fontes_usadas:
            erro("fontes/%s: nenhuma versao e nenhuma declaracao aponta para esta fonte. "
                 "Fonte colhida que o banco nunca usa e a outra direcao do numero "
                 "digitado: ela envelhece sem ninguem notar." % fid)
    usadas_por_exp = {e.get("cidade") for e in banco.get("experiencias", [])}
    for cid in cidades:
        if cid not in usadas_por_exp:
            aviso("cidades/%s: nenhuma experiencia nesta cidade ainda. Cidade pode "
                  "preceder experiencia; se persistir, e malha prometida e nao construida."
                  % cid)

    # ------------------------------------------------------------------
    # 6. FRASE PROIBIDA E CONSTANTE PENDENTE
    # ------------------------------------------------------------------
    for texto in _textos(banco):
        if FRASE_PROIBIDA in texto.lower():
            erro("banco: a frase %r aparece no banco. Proibida pela secao 7 desde "
                 "14/09/2026." % FRASE_PROIBIDA)
            break

    if constantes:
        pendentes = [c.get("id") for c in constantes.get("constantes", [])
                     if c.get("status") == "pendente"]
        textos = list(_textos(banco))
        for cid in pendentes:
            if any(cid and cid in t for t in textos):
                erro("banco: usa a constante %r, que esta com status `pendente`. "
                     "Constante pendente e proibida dentro de formula publicada "
                     "(secao 10)." % cid)

    # ------------------------------------------------------------------
    # 7. O RESUMO NASCE CONTADO, NUNCA DIGITADO (secao 8)
    # ------------------------------------------------------------------
    calculado = {
        "cidades": len(banco.get("cidades", [])),
        "experiencias": len(banco.get("experiencias", [])),
        "versoes": n_versoes,
        "fontes": len(banco.get("fontes", [])),
        "declaracoes": n_declaracoes,
        "declaracoes_publicaveis": n_publicaveis,
        "declaracoes_sem_versao": sem_versao,
        "itens_sem_saida_de_compra": sem_saida,
        "itens_com_piso_nao_rastreavel": piso_nao_rastreavel,
        "itens_intestaveis": intestaveis,
        "experiencias_com_preco_em_brl": len(versoes_em_brl),
        "fontes_de_leitura_direta": sum(1 for f in banco.get("fontes", [])
                                        if f.get("leitura") == "leitura_direta"),
        "faixas_etarias": n_faixas_de_idade,
        "elegibilidades": n_elegibilidades[0],
        "tarifas_com_prova_adicional": n_tarifas_com_prova_adicional[0],
        "provas_adicionais": n_provas_adicionais[0],
        "faixas_declaradas_nao_transcritas": n_lacunas_de_faixa,
        "experiencias_com_eixo_por_quantidade": n_eixo.get("por_quantidade", 0),
        "experiencias_com_eixo_por_escopo": n_eixo.get("por_escopo", 0),
        "experiencias_com_eixo_por_momento": n_eixo.get("por_momento", 0),
        "versoes_com_dias_de_uso": n_dias_de_uso,
        "faixas_diarias": len(banco.get("faixas_diarias", [])),
        "faixas_diarias_publicaveis": n_faixas_publicaveis,
        "coberturas_de_passe": len(banco.get("coberturas_de_passe", [])),
        "coberturas_de_passe_publicaveis": n_coberturas_publicaveis,
        "experiencias_que_sao_passe_de_cidade": n_passes,
    }
    gravado = banco.get("resumo") or {}
    for chave, valor in calculado.items():
        if chave not in gravado:
            erro("resumo: falta a chave `%s` (contada: %r)." % (chave, valor))
        elif gravado[chave] != valor:
            erro("resumo: `%s` gravado como %r e a contagem da %r. Numero que a ilha "
                 "publica sobre si mesma nasce contado, nunca digitado (secao 8)."
                 % (chave, gravado[chave], valor))
    for chave in gravado:
        if chave not in calculado:
            erro("resumo: `%s` nao e uma contagem que esta regua saiba refazer. Numero "
                 "no resumo que ninguem recomputa e digitado com cara de medido." % chave)

    if sem_saida:
        erro("banco: %d item(ns) SEM saida de compra. Pela 25.2 isso e erro duro, nunca "
             "divida." % sem_saida)

    for v in vencidos:
        aviso("preco vencido: %s. Item vencido e defeito de ronda, nunca item escondido — "
              "a data de leitura vai para a tela vencida ou nao." % v)

    # VOCABULARIO SEM LASTRO — a outra metade da regra de crescimento de vocabulario
    # do esquema, e ela e AVISO e nao erro de proposito. A regra nasceu em 15/09/2026
    # dizendo que valor novo nasce junto com o registro que o usa; os valores que o
    # esquema do bloco 3 ja trazia sao anteriores a ela e nao viram defeito
    # retroativo. O que a regra proibe enquanto esta lista nao for vazia e a ilha
    # publicar FRASE DE INEXISTENCIA — "nenhuma experiencia cobra em real", "nao ha
    # free tour no banco" —, porque essa frase so tem lastro quando o vocabulario e
    # a cobertura dizem a mesma coisa. Publicada a cada passada para ser contada, que
    # e a diferenca entre uma divida conhecida e uma frase que ninguem confere.
    # A LISTA DO QUE SE CONFERE SAI DO ESQUEMA, NUNCA DAQUI — e vocabulario sem
    # extrator e DENUNCIADO (22/10/2026). Ate hoje esta conferencia carregava sete
    # nomes escritos a mao, e o esquema tinha NOVE: `declarada_por` e
    # `canal_de_leitura` nunca foram conferidos por ninguem, em silencio, desde
    # 15/09/2026. E a mesma familia da lista de portoes que a aquametria matou com o
    # descobridor em 22/09/2026 e da lista de quem vigia que a leva 7 achou um andar
    # acima: lista escrita a mao nao erra alto, ela erra calada, e o que falta nela e
    # sempre o que acabou de nascer. Agora a regua varre `vocabularios` do esquema, e
    # o vocabulario que ela nao souber extrair vira ERRO em vez de ausencia.
    if vocab:
        usados = {chave: set() for chave in vocab}

        def usar(chave, valor):
            if chave in usados and valor is not None:
                usados[chave].add(valor)

        for cidade in banco.get("cidades", []):
            usar("moeda", cidade.get("moeda_local"))
        for fonte in banco.get("fontes", []):
            usar("canal_de_leitura", fonte.get("leitura"))
        for exp in banco.get("experiencias", []):
            usar("categoria", exp.get("categoria"))
            usar("eixo_das_versoes", exp.get("eixo_das_versoes"))
            usar("status_do_registro", exp.get("status"))
            usar("tipo_de_operador", (exp.get("operador") or {}).get("tipo"))
            for dec in (exp.get("declaracoes") or []):
                usar("moeda", dec.get("moeda"))
                usar("unidade_de_preco", dec.get("unidade_de_preco"))
            for versao in exp.get("versoes", []):
                usar("moeda", versao.get("moeda"))
                usar("unidade_de_preco", versao.get("unidade_de_preco"))
                usar("momento_do_dia", versao.get("momento_do_dia"))
                usar("declarada_por", versao.get("unidade_de_preco_declarada_por"))
                usar("declarada_por", versao.get("capacidade_maxima_declarada_por"))
                for acrescimo in (versao.get("acrescimos") or []):
                    usar("moeda", acrescimo.get("moeda"))
                # E O CAMPO NOVO ENTRA AQUI NA MESMA PASSADA (27/10/2026). A regua
                # do `sem_extrator` guarda vocabulario NOVO sem extrator; ela nao
                # alcanca CAMPO novo que carrega vocabulario velho — e foi
                # exatamente o que aconteceu: `provas_adicionais` nasceu usando
                # `nacionalidade` em tres tarifas e o aviso de lastro continuou
                # dizendo que `nacionalidade` nao tinha registro que o usasse. Um
                # andar abaixo da divida que a regua de 22/10 fechou, e com a mesma
                # assinatura: a conferencia nao erra alto, ela erra calada.
                for faixa_v in (versao.get("faixa_etaria") or []):
                    for prova in (faixa_v.get("provas_adicionais") or []):
                        usar("o_que_se_prova", prova.get("o_que_se_prova"))
                for eleg in (versao.get("elegibilidade") or []):
                    usar("o_que_se_prova", eleg.get("o_que_se_prova"))
                    usar("moeda", eleg.get("moeda"))
                    for prova in (eleg.get("provas_adicionais") or []):
                        usar("o_que_se_prova", prova.get("o_que_se_prova"))
        for cob in banco.get("coberturas_de_passe", []):
            usar("forma_de_cobertura", cob.get("como"))
            usar("declarada_por", cob.get("declarada_por"))
            usar("status_do_registro", cob.get("status"))
        for faixa in banco.get("faixas_diarias", []):
            usar("moeda", faixa.get("moeda"))
            usar("status_do_registro", faixa.get("status"))
            usar("categoria_de_custo", faixa.get("categoria_de_custo"))
            usar("padrao_de_viagem", faixa.get("padrao"))
            usar("base_da_faixa", faixa.get("base"))
            usar("o_que_o_numero_e", faixa.get("o_que_o_numero_e"))

        # Os vocabularios que ESTA regua sabe extrair. Lista explicita de proposito:
        # ela e o contrato entre o esquema e a conferencia, e o `assert` dela mora
        # logo abaixo. Vocabulario novo no esquema SEM extrator aqui reprova a regua.
        com_extrator = {
            "moeda", "unidade_de_preco", "categoria", "tipo_de_operador",
            "momento_do_dia", "canal_de_leitura", "status_do_registro",
            "eixo_das_versoes", "declarada_por", "categoria_de_custo",
            "padrao_de_viagem", "base_da_faixa", "o_que_o_numero_e",
            "forma_de_cobertura", "o_que_se_prova",
        }
        sem_extrator = sorted(c for c in vocab if c not in com_extrator)
        if sem_extrator:
            erro("esquema: %d vocabulario(s) sem extrator nesta regua (%s). A regra de "
                 "crescimento de vocabulario NAO PODE SER CONFERIDA para eles, e uma "
                 "conferencia que nao acontece fica verde: ate 22/10/2026 esta lista era "
                 "escrita a mao e `declarada_por` e `canal_de_leitura` passaram 37 dias "
                 "fora dela sem ninguem notar. Vocabulario novo entra no esquema e no "
                 "extrator na mesma passada."
                 % (len(sem_extrator), ", ".join(sem_extrator)))

        for chave in sorted(usados):
            sem_lastro = [v for v in vocab.get(chave, []) if v not in usados[chave]]
            if sem_lastro:
                aviso("vocabulario_sem_lastro em `%s`: %d de %d sem um registro que os "
                      "use (%s). Enquanto isto nao for vazio, frase de inexistencia "
                      "sobre este vocabulario esta proibida na tela."
                      % (chave, len(sem_lastro), len(vocab.get(chave, [])),
                         ", ".join(sem_lastro)))

    return erros, avisos, calculado


def main():
    esquema = _carregar("esquema-banco.json")
    banco = _carregar("experiencias.json")
    try:
        constantes = _carregar("constantes.json")
    except FileNotFoundError:
        constantes = None

    erros, avisos, calculado = validar(esquema, banco, constantes)

    print("Banco da JornadaFly — verificacao do esquema do bloco 3")
    # A LISTA DE CHAVES SAI DO `calculado`, nunca escrita a mao. Ate 22/10/2026 ela era
    # uma tupla literal aqui, e `faixas_diarias` e `faixas_diarias_publicaveis` — nascidas
    # na migracao do dia anterior — NAO ESTAVAM NELA: a regua contava os dois e o
    # relatorio nao os mostrava, de modo que a unica entidade com zero registros era
    # tambem a unica invisivel na tela de quem roda o portao. E a mesma familia da lista
    # de sete nomes de vocabulario que esta regua acabou de matar um andar acima, e do
    # descobridor de portoes da aquametria: lista escrita a mao nao erra alto, erra calada.
    for chave, valor in calculado.items():
        print("  %-38s %s" % (chave.replace("_", " ") + " ", valor))
    for a in avisos:
        print("  AVISO: %s" % a)
    if erros:
        print("\n%d ERRO(S):" % len(erros))
        for e in erros:
            print("  - %s" % e)
        sys.exit(1)
    print("\nOK: o banco cumpre o esquema, o piso de compra bate com a derivacao da "
          "cidade e a resolucao de divergencia bate com a escada de fontes.")


if __name__ == "__main__":
    main()

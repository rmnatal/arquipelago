#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se marcas.json, modelos-robo.json e pecas.json cumprem o contrato de
dados/esquema-banco.json.

Roda sem dependencia e sem rede:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Este arquivo NUNCA e publicado
no site: e ferramenta de bancada, como manda o esquema do manifest.

Por que ele existe: nesta ilha o produto e a afirmacao de compatibilidade. Uma
afirmacao errada aqui destroi a confianca inteira, e defeito de banco nao aparece
lendo o arquivo — aparece quando alguem compra a peca errada. O verificador e o que
transforma as regras escritas do esquema em algo que falha alto.
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

erros = []
avisos = []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    avisos.append(msg)


def carregar(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return json.load(fh)


esquema = carregar("esquema-banco.json")
marcas = carregar("marcas.json")
modelos = carregar("modelos-robo.json")
pecas = carregar("pecas.json")

VOC = esquema["vocabularios"]
NIVEIS = {n["nivel"] for n in esquema["escada_de_fontes"]["niveis"]}

CAMPOS_MODELO_OBRIGATORIOS = [
    "pa_declarado", "potencia_w_declarada", "autonomia_min_declarada",
    "cobertura_m2_declarada", "recarga_min_declarada", "retoma_apos_recarga",
    "bateria_mah", "voltagem", "base_autoesvaziamento",
]

CHAVES_IMAGEM = {"url", "largura", "altura", "fonte", "coletado_em", "alt"}
CHAVES_AFILIADO = {"url", "plataforma", "coletado_em", "sub_id_1", "sub_id_2"}


ORIGEM_DO_NIVEL = {n["nivel"]: n["origem"] for n in esquema["escada_de_fontes"]["niveis"]}

# Degraus que exigem ter LIDO o documento na fonte primaria. Ver
# escada_de_fontes.o_nivel_e_o_elo_mais_fraco no esquema.
NIVEIS_QUE_EXIGEM_LEITURA_DIRETA = {1, 2}
LEITURA_DIRETA = "direta-na-fonte-primaria"


def checar_fontes(reg, arquivo):
    """Toda fonte declarada tem nivel valido, origem coerente e data."""
    for fid, f in reg.get("fontes", {}).items():
        onde = "%s/%s/fontes/%s" % (arquivo, reg["id"], fid)
        if f.get("nivel") not in NIVEIS:
            erro("%s: nivel %r fora da escada_de_fontes" % (onde, f.get("nivel")))
        # O buraco por onde a contradicao de 11/09/2026 entrou: o nivel era
        # conferido e a ORIGEM nao, entao um manual de fabricante guardado por
        # terceiro podia se declarar nivel 2 com origem 'manual-fabricante' e
        # nada reprovava — enquanto a pagina de metodologia publicava "nivel 2:
        # temos hoje —". As duas metades nunca se encontravam.
        elif f.get("origem") != ORIGEM_DO_NIVEL[f["nivel"]]:
            erro("%s: nivel %d declara origem %r, e a escada diz %r. Nivel e origem sao "
                 "o mesmo degrau escrito duas vezes; divergir e contradizer a pagina de "
                 "metodologia, que le a escada"
                 % (onde, f["nivel"], f.get("origem"), ORIGEM_DO_NIVEL[f["nivel"]]))
        # A REGRA DO ELO MAIS FRACO, mecanica. Uma origem tem tres elos — quem
        # escreveu, quem guarda e como nos lemos — e o nivel e o do mais fraco.
        # Os dois degraus de cima exigem leitura na fonte primaria, e a unica
        # forma de provar isso e DECLARAR: silencio nunca promove. Adivinhar
        # pelo texto do canal_de_coleta seria a mesma heuristica por vizinhanca
        # que a secao 8 do ARQUIPELAGO.md proibe.
        if f.get("nivel") in NIVEIS_QUE_EXIGEM_LEITURA_DIRETA and f.get("leitura") != LEITURA_DIRETA:
            erro("%s: nivel %d sem declarar leitura=%r. Documento colhido por busca, ou "
                 "guardado por terceiro, e nivel 3 — errar para cima faz a ilha publicar "
                 "um rigor que ela nao tem, e a metodologia e a pagina cujo unico produto "
                 "e o rigor" % (onde, f["nivel"], LEITURA_DIRETA))
        if not f.get("verificado_em"):
            erro("%s: sem verificado_em" % onde)
        if not f.get("titulo_na_fonte"):
            erro("%s: sem titulo_na_fonte — a frase publicada nao tem o que citar" % onde)
        if not f.get("canal_de_coleta"):
            erro("%s: sem canal_de_coleta" % onde)


def checar_campo_de_valor(reg, campo, arquivo):
    """Valor nao nulo precisa de fonte existente; valor nulo precisa de motivo."""
    onde = "%s/%s/%s" % (arquivo, reg["id"], campo)
    v = reg.get(campo)
    if v is None:
        erro("%s: campo obrigatorio ausente" % onde)
        return
    if not isinstance(v, dict) or "valor" not in v:
        erro("%s: nao tem a forma campo_de_valor {valor, fonte, declarado_como}" % onde)
        return
    if v["valor"] is None:
        if not v.get("motivo_do_null"):
            erro("%s: valor null sem motivo_do_null. 'nao sei' e resposta legitima, "
                 "mas precisa estar escrita" % onde)
    else:
        fid = v.get("fonte")
        if not fid:
            erro("%s: valor %r sem fonte. Numero sem procedencia nao vai para a tela"
                 % (onde, v["valor"]))
        elif fid not in reg.get("fontes", {}):
            erro("%s: aponta para a fonte %r, que nao existe neste registro" % (onde, fid))
        if not v.get("declarado_como"):
            erro("%s: sem declarado_como — sem a transcricao a pagina parafraseia o "
                 "fabricante em vez de cita-lo" % onde)


# ---------------------------------------------------------------- MARCAS
ids_marca = set()
for m in marcas["registros"]:
    if m["id"] in ids_marca:
        erro("marcas.json: id duplicado %r" % m["id"])
    ids_marca.add(m["id"])
    for c in ("nome", "site_oficial", "sameAs", "verificado_em"):
        if not m.get(c):
            erro("marcas.json/%s: campo obrigatorio %s vazio" % (m["id"], c))

# ---------------------------------------------------------- MODELOS DE ROBO
ids_modelo = {}
for r in modelos["registros"]:
    onde = "modelos-robo.json/%s" % r["id"]
    if r["id"] in ids_modelo:
        erro("%s: id duplicado" % onde)
    ids_modelo[r["id"]] = r

    if r["marca"] not in ids_marca:
        erro("%s: marca %r nao existe em marcas.json" % (onde, r["marca"]))
    if r["categoria"] not in VOC["categoria"]:
        erro("%s: categoria %r fora do vocabulario" % (onde, r["categoria"]))
    if r["status"] not in VOC["status_do_registro"]:
        erro("%s: status %r fora do vocabulario" % (onde, r["status"]))

    # O PORTAO: so robo confirmado pode ser publicavel.
    if r["status"] == "publicavel" and r["categoria"] != "robo":
        erro("%s: PORTAO VIOLADO — status publicavel com categoria %r. So entra no site "
             "modelo que o proprio fabricante chama de aspirador robo" % (onde, r["categoria"]))
    if r["status"] != "publicavel" and not r.get("motivo_do_status"):
        erro("%s: status %r sem motivo_do_status" % (onde, r["status"]))

    checar_fontes(r, "modelos-robo.json")
    for campo in CAMPOS_MODELO_OBRIGATORIOS:
        checar_campo_de_valor(r, campo, "modelos-robo.json")

    if set(r.get("imagem", {})) < CHAVES_IMAGEM:
        erro("%s: imagem{} incompleta — falta %s"
             % (onde, sorted(CHAVES_IMAGEM - set(r.get("imagem", {})))))
    if set(r.get("afiliado", {})) != CHAVES_AFILIADO:
        erro("%s: afiliado{} fora da forma do esquema" % onde)
    elif r["afiliado"]["sub_id_1"] != "robometria":
        erro("%s: sub_id_1 tem que ser 'robometria'" % onde)

    for var in r.get("variantes_de_hardware", []):
        if var.get("fonte") not in r.get("fontes", {}):
            erro("%s: variante %r aponta para fonte inexistente" % (onde, var.get("rotulo")))

    v = r.get("voltagem", {})
    if v.get("valor") is not None and str(v["valor"]) not in [x for x in VOC["voltagem"] if x]:
        erro("%s: voltagem %r fora do vocabulario. Nunca chutar 127 ou 220" % (onde, v["valor"]))

    # Divergencia de ESPECIFICACAO DE APARELHO, nova na versao 3 do esquema. Ate a versao 2
    # so PECA divergia, porque a divergencia conhecida era de compatibilidade. O PRA500
    # declara 1600 Pa na ficha e 2000 Pa no texto de venda da MESMA pagina — e um numero
    # de succao errado manda alguem comprar um robo fraco demais para a casa dele.
    if "divergencias" not in r:
        erro("%s: divergencias ausente. Lista vazia e afirmacao ('nao encontramos "
             "declaracao divergente'); ausencia e omissao" % onde)
    if r.get("divergencias") and not r.get("resolucao"):
        erro("%s: tem divergencias e nao diz qual valor valeu nem qual e o erro caro que "
             "decidiu a direcao. Divergencia sem resolucao escrita e a ilha empurrando a "
             "duvida para o visitante — e escolher pela media e proibido" % onde)
    for dv in r.get("divergencias", []):
        campo = dv.get("campo")
        if not campo:
            erro("%s: item de divergencias sem 'campo' — nao da para saber o que diverge"
                 % onde)
        elif campo not in r:
            erro("%s: divergencia sobre o campo %r, que nao existe neste registro"
                 % (onde, campo))
        if not dv.get("transcricao"):
            erro("%s: divergencia sem transcricao. Sem o texto do fabricante a pagina "
                 "parafraseia os DOIS lados em vez de citar" % onde)

# ------------------------------------------------------------------ PECAS
ids_peca = set()
pares = 0
for p in pecas["registros"]:
    onde = "pecas.json/%s" % p["id"]
    if p["id"] in ids_peca:
        erro("%s: id duplicado" % onde)
    ids_peca.add(p["id"])

    if p["marca"] not in ids_marca:
        erro("%s: marca %r nao existe em marcas.json" % (onde, p["marca"]))
    if p["tipo"] not in VOC["tipo_de_peca"]:
        erro("%s: tipo %r fora do vocabulario" % (onde, p["tipo"]))

    # Kit e caixa fechada ate declarar o que tem dentro. Sem isto a R1 sabe QUE o kit
    # serve e nao consegue dizer que o filtro do ERB10 vem dentro dele — que e a resposta
    # que a pessoa procurou.
    if p["tipo"] == "kit":
        if not p.get("composicao"):
            erro("%s: tipo kit sem composicao. Kit sem composicao e caixa fechada: a R1 nao "
                 "consegue responder 'qual filtro serve no meu modelo'" % onde)
        for item in p.get("composicao", []):
            t = item.get("tipo")
            if t == "kit":
                erro("%s: composicao com item do tipo kit — kit dentro de kit nao existe "
                     "neste banco" % onde)
            elif t is not None and t not in VOC["tipo_de_peca"]:
                erro("%s: composicao com tipo %r fora do vocabulario" % (onde, t))
            elif t is None and not item.get("descricao_na_fonte"):
                erro("%s: item de composicao sem tipo E sem descricao_na_fonte — nao sobra "
                     "nada para a tela" % onde)
    elif p.get("composicao"):
        erro("%s: composicao so existe em peca do tipo kit" % onde)

    # Nem todo fabricante publica codigo. Isso e resposta, e como toda resposta null
    # nesta ilha, ela tem que estar escrita.
    if p.get("codigo_fabricante") is None and not p.get("motivo_sem_codigo"):
        erro("%s: codigo_fabricante null sem motivo_sem_codigo. 'o fabricante nao publica "
             "codigo' e resposta legitima, mas precisa estar escrita" % onde)
    if p["status"] not in VOC["status_do_registro"]:
        erro("%s: status %r fora do vocabulario" % (onde, p["status"]))
    if p["status"] != "publicavel" and not p.get("motivo_do_status"):
        erro("%s: status %r sem motivo_do_status" % (onde, p["status"]))
    if not p.get("nome_na_fonte"):
        erro("%s: sem nome_na_fonte" % onde)

    checar_fontes(p, "pecas.json")
    checar_campo_de_valor(p, "vida_util_declarada", "pecas.json")

    if "divergencias" not in p:
        erro("%s: divergencias ausente. Lista vazia e afirmacao ('nao encontramos "
             "declaracao divergente'); ausencia e omissao" % onde)
    if p.get("divergencias") and not p.get("resolucao"):
        erro("%s: tem divergencias e nao diz qual conjunto valeu. Divergencia sem "
             "resolucao escrita e a ilha empurrando a duvida para o visitante" % onde)

    if set(p.get("imagem", {})) < CHAVES_IMAGEM:
        erro("%s: imagem{} incompleta" % onde)
    if set(p.get("afiliado", {})) != CHAVES_AFILIADO:
        erro("%s: afiliado{} fora da forma do esquema" % onde)

    if not p.get("compatibilidade"):
        erro("%s: peca sem nenhum par de compatibilidade" % onde)
    for c in p.get("compatibilidade", []):
        if c["selo"] not in VOC["selo_de_compatibilidade"]:
            erro("%s: selo %r fora do vocabulario" % (onde, c["selo"]))
        if c["selo"] == "nao_declarada":
            erro("%s: par com selo nao_declarada listado como compatibilidade "
                 "afirmativa. nao_declarada e o caso em que a R1 diz que nao achou "
                 "e para ali" % onde)
        if c.get("fonte") not in p.get("fontes", {}):
            erro("%s: par %r aponta para fonte inexistente" % (onde, c.get("codigo_declarado")))
        if not c.get("codigo_declarado"):
            erro("%s: par sem codigo_declarado" % onde)
        if c.get("modelo") is None:
            aviso("%s: par %r sem modelo no banco (permitido, mas e lista de compras)"
                  % (onde, c.get("codigo_declarado")))
        elif c["modelo"] not in ids_modelo:
            erro("%s: par aponta para o modelo %r, que nao existe em modelos-robo.json"
                 % (onde, c["modelo"]))
        else:
            alvo = ids_modelo[c["modelo"]]
            if p["status"] == "publicavel" and alvo["status"] == "excluido_do_banco":
                erro("%s: peca publicavel declarada compativel com %r, que esta "
                     "excluido do banco por nao ser robo" % (onde, c["modelo"]))
            rotulos = [x.get("rotulo") for x in alvo.get("variantes_de_hardware", [])]
            if rotulos and c.get("variante_de_hardware") is None:
                aviso("%s: o modelo %r tem variantes %s e este par esta com "
                      "variante null, o que pelo esquema significa 'serve em todas as "
                      "conhecidas'. Confirmar na fonte que vale para %s antes de a R1 "
                      "afirmar isso na tela"
                      % (onde, c["modelo"], rotulos, " e ".join(map(str, rotulos))))
            if c.get("variante_de_hardware") and c["variante_de_hardware"] not in rotulos:
                erro("%s: variante %r nao existe no modelo %r"
                     % (onde, c["variante_de_hardware"], c["modelo"]))
        if p["status"] == "publicavel":
            pares += 1

# --------------------------------------------------- CONTAGENS DO CABECALHO
def conferir_contagem(doc, arquivo, chave, esperado):
    declarado = doc.get("contagem", {}).get(chave)
    if declarado != esperado:
        erro("%s: contagem.%s diz %r e o arquivo tem %r"
             % (arquivo, chave, declarado, esperado))

conferir_contagem(modelos, "modelos-robo.json", "total", len(modelos["registros"]))

# O cabecalho de modelos-robo.json anuncia a cobertura do campo que decide se a R2 sai com
# lista ou vazia. Contagem que nao bate com o arquivo e pior que contagem nenhuma: e um
# numero que a proxima execucao vai acreditar sem conferir.
_pub = [r for r in modelos["registros"] if r["status"] == "publicavel"]
conferir_contagem(modelos, "modelos-robo.json", "publicavel", len(_pub))
conferir_contagem(modelos, "modelos-robo.json", "com_pa_declarado",
                  sum(1 for r in _pub if r["pa_declarado"]["valor"] is not None))
conferir_contagem(modelos, "modelos-robo.json", "com_par_minutos_m2_declarado",
                  sum(1 for r in _pub if r["autonomia_min_declarada"]["valor"] is not None
                      and r["cobertura_m2_declarada"]["valor"] is not None))
conferir_contagem(modelos, "modelos-robo.json", "marcas_que_declaram_pa",
                  sorted({r["marca"] for r in _pub
                          if r["pa_declarado"]["valor"] is not None}))
conferir_contagem(modelos, "modelos-robo.json", "esperando_link_de_afiliado",
                  sum(1 for r in _pub if not r["afiliado"]["url"]))
conferir_contagem(pecas, "pecas.json", "total", len(pecas["registros"]))
conferir_contagem(pecas, "pecas.json", "pares_peca_x_modelo_declarados", pares)

esperando = ([r["id"] for r in modelos["registros"]
              if r["status"] == "publicavel" and not r["afiliado"]["url"]] +
             [p["id"] for p in pecas["registros"]
              if p["status"] == "publicavel" and not p["afiliado"]["url"]])

# ------------------------------------------------------------------ SAIDA
print("Robometria — verificacao do banco (esquema versao %s)" % esquema["versao_esquema"])
print("  marcas ............... %d" % len(marcas["registros"]))
print("  modelos de robo ...... %d (%d publicaveis, %d excluidos por nao serem robo)"
      % (len(modelos["registros"]),
         sum(1 for r in modelos["registros"] if r["status"] == "publicavel"),
         sum(1 for r in modelos["registros"] if r["status"] == "excluido_do_banco")))
print("  pecas ................ %d (%d publicaveis)"
      % (len(pecas["registros"]),
         sum(1 for p in pecas["registros"] if p["status"] == "publicavel")))
print("  pares peca x modelo .. %d, todos DECLARADOS pelo fabricante" % pares)
print("  esperando link de afiliado ... %d" % len(esperando))

if avisos:
    print("\nAvisos (%d) — nao reprovam, sao lista de trabalho:" % len(avisos))
    for a in avisos:
        print("  . " + a)

if erros:
    print("\nREPROVADO — %d invariante(s) violada(s):" % len(erros))
    for e in erros:
        print("  x " + e)
    sys.exit(1)

print("\nAPROVADO: nenhuma invariante do esquema violada.")

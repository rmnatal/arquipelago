#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA E O PORTAO DA LISTA DE PROSPECCAO DO WIDGET — o que a lista pode afirmar.

    python3 ferramentas/validar-prospeccao.py              # o portao, sobre o arquivo de verdade
    python3 ferramentas/validar-prospeccao.py --autoteste   # a regua, sobre mundos FABRICADOS

POR QUE A REGUA MORA DENTRO DO PORTAO, E NAO NUM `regua-prospeccao.py`
----------------------------------------------------------------------
A Aquametria separou os dois em 24/09/2026 e fez certo PARA AQUELA ILHA: la a
regua e carregada por quatro arquivos. Aqui ela e carregada por DOIS — este
portao e o `gerar-prospeccao.py`, que a importa —, e `bancada.py` desta ilha
classifica portao POR PREFIXO DE NOME (`validar-`, `mutacoes-`, `teste-`,
`conferir-`, `gerar-`, ...) e DENUNCIA o arquivo que nao casa com nenhum.
`regua-prospeccao.py` nasceria denunciado, e o conserto seria escrever o nome
dele numa lista de excecao a mao — exatamente a doenca que esta bancada matou
quando deixou de enumerar portao. Entao a regua mora aqui, numa fonte so, e o
gerador a importa. Quem precisar de um terceiro leitor um dia separa.

POR QUE ESTE PORTAO EXISTE, com a 31 na mao e nao contra ela
------------------------------------------------------------
A **31.2** proibe portao NOVO sem defeito medido no ar que ele teria pegado, e
este portao nunca vai pegar defeito no ar nenhum: o arquivo que ele julga tem
`publicar: false` e nao serve um byte a visitante nenhum. O que o autoriza e a
**31.5**, que preserva *"portao de dado"* com todas as letras, e a secao 10 do
contrato, que proibe inventar dado. **Portao de AR e portao de DADO nao sao a
mesma coisa**: o primeiro protege a pagina, o segundo protege a afirmacao. E e
por isso que esta execucao escreveu DOIS arquivos de ferramenta e nao cinco —
a Aquametria tem `regua-`, `validar-`, `teste-`, `mutacoes-` e `gerar-`, e a
bateria de mutacao e o teste sintetico dela seriam, aqui, bancada sobre bancada,
que e o que a 31.3 fecha enquanto houver item de conteudo aberto na fila. O
`--autoteste` abaixo faz a metade que importa: prova que a regua MORDE.

O INSTRUMENTO DESTA PASSADA E UM SO, e ele decide tudo o que esta escrito aqui
------------------------------------------------------------------------------
O egresso desta nuvem responde 403 no CONNECT para todo dominio fora da lista
de permitidos — medido nesta ilha em 29/10/2026 com tres passadas em cinco
dominios de fabricante e tres de varejo grande, todas `connect_rejected`, com
`rodametria.com.br` e `aquametria.com.br` em 200 nas mesmas. **Ninguem abre o
site de ninguem daqui.** O que existe e a BUSCA — o mesmo degrau 4 pelo qual a
jornadafly entrou em 27/10 e pelo qual o banco desta ilha foi construido.

AS QUATRO REGRAS QUE ISSO IMPOE, e todas sao sobre NAO AFIRMAR DEMAIS
---------------------------------------------------------------------
  1. NAO EXISTE `false` NOS CAMPOS DE FATO. Busca sabe afirmar PRESENCA, nunca
     ausencia — e a mesma assimetria que a **30.8** escreveu para o veredito de
     SERP desta ilha, aplicada a outro assunto. Um dominio nao aparecer na busca
     de calculadora nao prova que ele nao tem calculadora: prova que a busca nao
     o mostrou. Entao `vende_veiculo`, `publica_conteudo` e `ja_tem_calculadora`
     sao `true` (com evidencia) ou `null` (= nao medido). `false` e RECUSADO.
  2. EVIDENCIA TEM DE SER DO DOMINIO QUE ELA SUSTENTA. O host do
     `resultado_url` tem de ser o dominio do candidato ou subdominio dele. E a
     trava anti-invencao: nesta mesma coleta, a Eletricz foi achada primeiro por
     uma materia de `mecanicaonline.com.br` que fala DELA — e materia de terceiro
     nao prova nada sobre o site do candidato, que e o que vai instalar o widget.
     A linha so entrou quando a busca devolveu `eletricz.com.br/...`.
  3. A PRIORIDADE NAO SE ESCREVE, SE CALCULA. A lista diz o numero e o portao
     RECALCULA dos campos medidos; se discordarem, vermelho. Quem mudar um campo
     medido nao precisa lembrar de mexer na prioridade — ela vem do campo. E a
     mesma doenca do `versao` do manifest desta ilha em 02/11: constante que
     alguem sobe a mao e ninguem confere e rastro, nao mecanismo.
  4. O QUE NAO FOI MEDIDO TEM DE DIZER QUE NAO FOI. `contato` e `plataforma`
     sao `null` nesta passada, e `null` exige MOTIVO escrito. Campo vazio sem
     motivo e onde a proxima passada inventa um e-mail.

E A PORTA DOS FUNDOS QUE FICA FECHADA JUNTO: `abriu_no_navegador` ausente NAO
vale como `false`. Se o campo pudesse faltar, a lista ganharia um estado em que
ninguem sabe se alguem abriu o site — e "ninguem abriu" e justamente a limitacao
que este arquivo existe para deixar visivel. Ausencia e reprovacao, nao omissao
tolerada (a letra da 30.8 sobre `visto_por`/`visto_em`).
"""

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
ARQUIVO_JSON = RAIZ / "dados" / "prospeccao-widget.json"
ARQUIVO_MD = RAIZ / "dados" / "prospeccao-widget.md"

# ---------------------------------------------------------------------------
# O TETO POR TIPO. O que esta medido e o TIPO; o teto e JUIZO, e esta escrito
# aqui para poder ser contestado em vez de ficar na cabeca de quem ordenou.
#
#   loja            -> 1. A oferta do widget e "uma ferramenta que diz se o
#                      veiculo precisa de CNH e quantos km ele faz, ao lado do
#                      veiculo que voce vende". Loja especializada e quem mais
#                      perde venda com a duvida que a ilha resolve.
#   distribuidora   -> 1. Mesma coisa: vende direto ao leitor e tem catalogo
#                      proprio por modelo.
#   fabricante      -> 2. Vende pouco direto, declara ficha e alcanca revenda em
#                      vez de leitor.
#   conteudo        -> 2. Tem onde publicar e nao tem o que vender: a ferramenta
#                      ajuda a pagina, nao o caixa.
#   varejo-grande   -> 3. Rede nacional tem equipe editorial propria, fornecedor
#                      homologado e juridico. Dominio de seis dias nao atravessa.
#   fazenda         -> 3. Publica "Top 10" e vive de ocupar a consulta: nao linka
#                      para fora de graca, e o `VOZ.md` desta ilha proibe o
#                      formato nominalmente. Medida nesta ilha em 30/10: 26
#                      paginas dedicadas de fazenda entre os 102 ocupantes das
#                      cinco caudas.
#   desconhecido    -> 3. Prospeccao que nao sabe com quem fala escreve texto
#                      errado. Nao saber e motivo para descer, nunca para chutar.
TETO_POR_TIPO = {
    "loja": 1,
    "distribuidora": 1,
    "fabricante": 2,
    "conteudo": 2,
    "varejo-grande": 3,
    "fazenda": 3,
    "desconhecido": 3,
}

CAMPOS_DE_FATO = ("vende_veiculo", "publica_conteudo", "ja_tem_calculadora")
CAMPOS_COM_EVIDENCIA = ("dominio", "tipo") + CAMPOS_DE_FATO
INSTRUMENTOS = ("busca", "navegador", "curl")

# Dominio que NAO e site proprio. Vitrine dentro de marketplace ou de rede
# social nao serve de alvo de prospeccao por dois motivos independentes: o link
# de la nao passa autoridade (e `nofollow` por politica da plataforma) e a
# pagina nao e da loja, e sim da plataforma — ela nao pode instalar nada.
# A `loja_oficial` da Honeywhale, medida nesta ilha em 29/10/2026, e exatamente
# isso: uma vitrine do Mercado Livre chamada de site da marca.
NAO_E_SITE_PROPRIO = (
    "mercadolivre.com.br", "mercadolibre.com", "mercadolivre.com",
    "shopee.com.br", "amazon.com.br", "magazineluiza.com.br",
    "casasbahia.com.br", "extra.com.br", "americanas.com.br",
    "olx.com.br", "kabum.com.br", "netshoes.com.br",
    "instagram.com", "facebook.com", "youtube.com", "tiktok.com",
    "wa.me", "linktr.ee",
)


def prioridade(candidato):
    """A prioridade CALCULADA. Nunca a escrita no arquivo.

    A base sai do cruzamento que a **14.9** manda usar — intencao de compra x
    chance real —, traduzido para o que a busca consegue medir: quem vende o
    veiculo que as ferramentas desta ilha classificam TEM interesse; quem
    publica conteudo no proprio dominio TEM onde por a ferramenta. As duas
    juntas sao a unica combinacao que chega a 1.

    E quem JA TEM calculadora cai para 3 seja quem for: ninguem instala a
    ferramenta de outro tendo a propria. Por isso e a PRIMEIRA linha da funcao.
    """
    if candidato.get("ja_tem_calculadora") is True:
        base = 3
    elif candidato.get("vende_veiculo") is True and candidato.get("publica_conteudo") is True:
        base = 1
    elif candidato.get("vende_veiculo") is True or candidato.get("publica_conteudo") is True:
        base = 2
    else:
        base = 3
    return max(base, TETO_POR_TIPO.get(candidato.get("tipo"), 3))


def host_de(url):
    """O host de uma URL, sem esquema, sem porta, sem caminho, minusculo."""
    resto = str(url).split("://", 1)[-1]
    return resto.split("/", 1)[0].split("?", 1)[0].split("@")[-1].split(":", 1)[0].lower()


def do_dominio(url, dominio):
    """O host da URL e o dominio, ou subdominio dele?

    `loja.eletricz.com.br` conta para `eletricz.com.br` — subdominio proprio e
    site proprio, e aquela loja tem os dois endereços de verdade. Ja
    `eletricz.com.br.exemplo.com` NAO conta, e e por isso que a comparacao e por
    ROTULO (o ponto antes) e nunca por `endswith` de texto cru.
    """
    host = host_de(url)
    dominio = str(dominio).lower()
    return host == dominio or host.endswith("." + dominio)


def campos_afirmados(candidato):
    """Os campos que a linha AFIRMA, e que por isso precisam de evidencia."""
    return [c for c in CAMPOS_COM_EVIDENCIA
            if candidato.get(c) is not None
            and not (c == "tipo" and candidato.get(c) == "desconhecido")]


def erros_de_evidencia(candidato):
    """As afirmacoes sobre a lista de evidencia de UM candidato."""
    erros = []
    rotulo = candidato.get("id", "<sem id>")
    dominio = candidato.get("dominio", "")
    evidencias = candidato.get("evidencia")
    if not isinstance(evidencias, list) or not evidencias:
        return ["%s: sem lista de evidencia" % rotulo]

    sustentados = set()
    for i, ev in enumerate(evidencias):
        onde = "%s evidencia[%d]" % (rotulo, i)
        campos = ev.get("campos")
        if not isinstance(campos, list) or not campos:
            erros.append("%s: nao diz que campos sustenta" % onde)
        else:
            sustentados.update(campos)
        instrumento = ev.get("medido_como")
        if instrumento not in INSTRUMENTOS:
            erros.append("%s: instrumento desconhecido (%r)" % (onde, instrumento))
        elif instrumento != "busca" and not ev.get("medido_por"):
            # Esta nuvem nao tem navegador e nao atravessa o egresso. Evidencia
            # que diz ter vindo de um dos dois tem de nomear QUEM mediu, senao e
            # afirmacao sem instrumento.
            erros.append("%s: %r sem `medido_por`; esta nuvem nao tem esse instrumento"
                         % (onde, instrumento))
        for campo, queixa in (("consulta", "sem a consulta que a produziu"),
                              ("resultado_titulo", "sem o titulo do resultado"),
                              ("medido_em", "sem data")):
            if not ev.get(campo):
                erros.append("%s: %s" % (onde, queixa))
        url = ev.get("resultado_url")
        if not url:
            erros.append("%s: sem a URL do resultado" % onde)
        elif not do_dominio(url, dominio):
            # REGRA 2, a trava anti-invencao.
            erros.append("%s: a URL %s nao e do dominio %s" % (onde, url, dominio))

    for campo in campos_afirmados(candidato):
        if campo not in sustentados:
            erros.append("%s: afirma %r e nenhuma evidencia o sustenta" % (rotulo, campo))
    return erros


def erros_do_candidato(candidato):
    """Tudo o que uma linha pode ter de errado, menos o `.md`."""
    erros = []
    rotulo = candidato.get("id", "<sem id>")

    for campo in ("id", "nome", "dominio", "tipo", "porque"):
        if not candidato.get(campo):
            erros.append("%s: sem `%s`" % (rotulo, campo))

    dominio = str(candidato.get("dominio", "")).lower()
    if dominio in NAO_E_SITE_PROPRIO or any(dominio.endswith("." + d) for d in NAO_E_SITE_PROPRIO):
        erros.append("%s: %s nao e site proprio — vitrine de plataforma nao instala nada "
                     "e o link de la nao passa autoridade" % (rotulo, dominio))
    if "/" in dominio or dominio.startswith("http"):
        erros.append("%s: `dominio` tem de ser so o dominio, sem esquema e sem caminho (%r)"
                     % (rotulo, candidato.get("dominio")))

    if candidato.get("tipo") not in TETO_POR_TIPO:
        erros.append("%s: tipo %r nao esta na tabela de teto" % (rotulo, candidato.get("tipo")))

    # REGRA 1: `false` e recusado nos campos de fato.
    for campo in CAMPOS_DE_FATO:
        valor = candidato.get(campo)
        if valor is False:
            erros.append("%s: `%s` e `false`, e esta passada nao sabe afirmar ausencia. "
                         "Use `null` (= nao medido)" % (rotulo, campo))
        elif valor not in (True, None):
            erros.append("%s: `%s` so aceita `true` ou `null` (veio %r)" % (rotulo, campo, valor))

    # REGRA 4: `null` exige motivo escrito.
    for campo in ("contato", "plataforma"):
        if candidato.get(campo) is None and not candidato.get(campo + "_motivo"):
            erros.append("%s: `%s` e `null` e nao diz por que nao foi medido" % (rotulo, campo))

    # A porta dos fundos: ausencia nao vale como `false`.
    if "abriu_no_navegador" not in candidato:
        erros.append("%s: falta `abriu_no_navegador`; ausencia nao vale como `false`" % rotulo)
    elif candidato["abriu_no_navegador"] is True and not candidato.get("abriu_no_navegador_por"):
        erros.append("%s: diz que abriram no navegador e nao diz quem" % rotulo)

    if candidato.get("publicar") is not False:
        erros.append("%s: `publicar` tem de ser `false` — esta lista nao vai ao ar" % rotulo)

    # REGRA 3: a prioridade e recalculada.
    esperada = prioridade(candidato)
    if candidato.get("prioridade") != esperada:
        erros.append("%s: prioridade escrita %r, calculada %d dos campos medidos"
                     % (rotulo, candidato.get("prioridade"), esperada))

    erros += erros_de_evidencia(candidato)
    return erros


# ---------------------------------------------------------------------------
# O `.md` E GERADO, NUNCA ESCRITO
# ---------------------------------------------------------------------------
# Duas fontes para o mesmo fato divergem. Esta ilha pagou isso em 02/11/2026 no
# `descricao` do manifest, que DECLARAVA a versao corrente dos quatro snippets e
# estava velha nos quatro. Entao a lista tem UMA fonte (o JSON) e o `.md` sai
# dela por esta funcao. O portao regera em memoria e compara: `.md` editado a
# mao fica vermelho.
ROTULO_PRIORIDADE = {
    1: "PRIORIDADE 1 — vende o veiculo E publica no proprio dominio",
    2: "PRIORIDADE 2 — uma das duas condicoes, ou teto de tipo",
    3: "PRIORIDADE 3 — ja tem calculadora, tipo que nao atravessa, ou nada medido",
}


def _sim(valor):
    return "sim" if valor is True else "nao medido"


def render_md(dados):
    """O `.md` inteiro, a partir do JSON. Mesma fonte, uma so."""
    L = []
    L.append("# PROSPECCAO DO WIDGET — RODAMETRIA (bloco 6, secao 14.7 do contrato)")
    L.append("")
    L.append("> **ARQUIVO GERADO por `ferramentas/gerar-prospeccao.py` a partir de**")
    L.append("> **`dados/prospeccao-widget.json`. Nao edite a mao:** o portao")
    L.append("> `validar-prospeccao.py` regera este texto e compara, e edicao a mao")
    L.append("> fica vermelha. Mude o JSON e rode o gerador.")
    L.append("")
    L.append("Atualizado em **%s**. Instrumento desta passada: **%s**."
             % (dados.get("atualizado_em"), ", ".join(dados.get("instrumentos_desta_passada", []))))
    L.append("")
    L.append("**NINGUEM ABRIU NENHUM SITE.** %s" % dados.get("por_que_ninguem_abriu", ""))
    L.append("")
    L.append("**NAO EXISTE `false` NESTE ARQUIVO.** %s" % dados.get("por_que_nao_existe_false", ""))
    L.append("")

    candidatos = dados.get("candidatos", [])
    for nivel in (1, 2, 3):
        doNivel = [c for c in candidatos if prioridade(c) == nivel]
        if not doNivel:
            continue
        L.append("## %s" % ROTULO_PRIORIDADE[nivel])
        L.append("")
        L.append("| dominio | nome | tipo | vende veiculo | publica conteudo | ja tem calculadora |")
        L.append("|---|---|---|---|---|---|")
        for c in sorted(doNivel, key=lambda x: x["dominio"]):
            L.append("| `%s` | %s | %s | %s | %s | %s |"
                     % (c["dominio"], c["nome"], c["tipo"],
                        _sim(c.get("vende_veiculo")), _sim(c.get("publica_conteudo")),
                        _sim(c.get("ja_tem_calculadora"))))
        L.append("")
        for c in sorted(doNivel, key=lambda x: x["dominio"]):
            L.append("### `%s` — %s" % (c["dominio"], c["nome"]))
            L.append("")
            L.append(c["porque"])
            L.append("")
            for ev in c.get("evidencia", []):
                L.append("- **%s** (%s, %s) — consulta `%s` → [%s](%s)"
                         % (", ".join(ev.get("campos", [])), ev.get("medido_como"),
                            ev.get("medido_em"), ev.get("consulta"),
                            ev.get("resultado_titulo"), ev.get("resultado_url")))
            L.append("")
    L.append("---")
    L.append("")
    L.append("## O que esta lista NAO diz")
    L.append("")
    for linha in dados.get("o_que_esta_lista_nao_diz", []):
        L.append("- %s" % linha)
    L.append("")
    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------------------
# O AUTOTESTE — mundos FABRICADOS, e a regua tem de MORDER cada um
# ---------------------------------------------------------------------------
# A 32.5-d desta ilha e literal: "a regra do molde que nunca rodou contra o dado
# de verdade esta quebrada e parece sa". O inverso tambem vale — regua que so
# roda contra o dado de verdade so pega o mundo de hoje. Entao o primeiro mundo
# aqui e um candidato REAL desta lista, e os outros sao quebras dele.
def _candidato_bom():
    return {
        "id": "exemplo", "nome": "Exemplo", "dominio": "exemplo.com.br",
        "tipo": "loja", "vende_veiculo": True, "publica_conteudo": True,
        "ja_tem_calculadora": None, "prioridade": 1,
        "porque": "razao escrita", "abriu_no_navegador": False,
        "contato": None, "contato_motivo": "nao medido — o egresso nao abre o site",
        "plataforma": None, "plataforma_motivo": "nao medido — depende de abrir o HTML",
        "publicar": False,
        "evidencia": [{
            "campos": ["dominio", "tipo", "vende_veiculo", "publica_conteudo"],
            "medido_como": "busca", "medido_em": "2026-11-02",
            "consulta": "uma consulta",
            "resultado_titulo": "Um titulo",
            "resultado_url": "https://loja.exemplo.com.br/patinete-eletrico",
        }],
    }


def _autoteste():
    casos = []

    def caso(nome, muda, tem_de_reprovar_com):
        c = _candidato_bom()
        muda(c)
        erros = erros_do_candidato(c)
        bateu = any(tem_de_reprovar_com in e for e in erros)
        casos.append((nome, bateu, erros))

    def caso_passa(nome, muda=None):
        c = _candidato_bom()
        if muda:
            muda(c)
        erros = erros_do_candidato(c)
        casos.append((nome, not erros, erros))

    # 1. O mundo que TEM de passar. Sem ele, uma regua que reprova tudo passaria
    #    nos outros nove e ninguem veria.
    caso_passa("o candidato sao passa")
    # 2. Subdominio proprio e site proprio — a URL da evidencia e `loja.`.
    caso_passa("subdominio proprio conta como dominio proprio")

    # 3. REGRA 1 — `false` em campo de fato.
    caso("`false` em campo de fato e recusado",
         lambda c: c.update(ja_tem_calculadora=False),
         "nao sabe afirmar ausencia")
    # 4. REGRA 2 — evidencia de outro dominio. A armadilha medida nesta coleta:
    #    a materia de terceiro que fala do candidato.
    caso("evidencia de OUTRO dominio e recusada",
         lambda c: c["evidencia"][0].update(resultado_url="https://mecanicaonline.com.br/exemplo"),
         "nao e do dominio")
    # 5. A armadilha do `endswith` cru: dominio do candidato como PREFIXO de outro.
    caso("`exemplo.com.br.golpe.com` nao conta como `exemplo.com.br`",
         lambda c: c["evidencia"][0].update(resultado_url="https://exemplo.com.br.golpe.com/x"),
         "nao e do dominio")
    # 6. REGRA 3 — prioridade escrita a mao, divergindo do calculo.
    caso("prioridade escrita divergente do calculo e recusada",
         lambda c: c.update(prioridade=2),
         "prioridade escrita")
    # 7. REGRA 3, a outra ponta: quem ja tem calculadora cai para 3 mesmo sendo loja.
    caso("`ja_tem_calculadora` derruba para 3 e a prioridade 1 vira erro",
         lambda c: c.update(ja_tem_calculadora=True),
         "calculada 3")
    # 8. REGRA 4 — `null` sem motivo.
    caso("`contato: null` sem motivo e recusado",
         lambda c: c.pop("contato_motivo"),
         "nao diz por que nao foi medido")
    # 9. A porta dos fundos — ausencia do campo nao vale como `false`.
    caso("`abriu_no_navegador` ausente e reprovacao, nao omissao",
         lambda c: c.pop("abriu_no_navegador"),
         "ausencia nao vale como `false`")
    # 10. Campo afirmado que nenhuma evidencia sustenta.
    caso("afirmar um campo sem evidencia que o nomeie e recusado",
         lambda c: c["evidencia"][0].update(campos=["dominio"]),
         "nenhuma evidencia o sustenta")
    # 11. Vitrine de plataforma nao e site proprio.
    caso("vitrine de marketplace nao e candidato",
         lambda c: c.update(dominio="mercadolivre.com.br",
                            evidencia=[dict(c["evidencia"][0],
                                            resultado_url="https://mercadolivre.com.br/x")]),
         "nao e site proprio")
    # 12. Instrumento que esta nuvem NAO tem, sem dizer quem mediu.
    caso("`navegador` sem `medido_por` e recusado",
         lambda c: c["evidencia"][0].update(medido_como="navegador"),
         "esta nuvem nao tem esse instrumento")
    # 13. A lista nao vai ao ar.
    caso("`publicar: true` e recusado",
         lambda c: c.update(publicar=True),
         "nao vai ao ar")

    falhas = [(n, e) for n, ok, e in casos if not ok]
    for nome, ok, erros in casos:
        print("  %s  %s" % ("ok  " if ok else "FALHA", nome))
        if not ok:
            for e in erros[:4]:
                print("        %s" % e)
    print("\n%d de %d mundos fabricados." % (len(casos) - len(falhas), len(casos)))
    return 1 if falhas else 0


def main(argv):
    # O AUTOTESTE RODA SEMPRE, ANTES DO ARQUIVO DE VERDADE, e isso nao e zelo:
    # a `bancada.py` desta ilha so descobre `--autoteste` nos portoes de REDE
    # (os `conferir-*`), porque foi para eles que o mecanismo nasceu em 02/11.
    # Este portao e dos sem rede, entao o autoteste dele nunca entraria na fila
    # sozinho — e portao que depende de alguem lembrar nao roda. Entao a regua
    # se prova contra os mundos fabricados toda vez que alguem a usa, e a ordem
    # importa: regua quebrada reprovando o arquivo de verdade parece arquivo
    # errado. `--autoteste` sozinho roda so esta metade.
    print("AUTOTESTE DA REGUA DE PROSPECCAO — mundos fabricados\n")
    falhou_autoteste = _autoteste()
    if "--autoteste" in argv:
        print("APROVADO" if not falhou_autoteste else "REPROVADO")
        return falhou_autoteste
    if falhou_autoteste:
        print("\nREPROVADO — a regua nao passou nos proprios mundos; o arquivo de "
              "verdade nao foi julgado, porque regua quebrada reprova arquivo certo.")
        return 1
    print("\nO ARQUIVO DE VERDADE\n")

    if not ARQUIVO_JSON.exists():
        print("FALHA: %s nao existe" % ARQUIVO_JSON)
        return 1
    dados = json.loads(ARQUIVO_JSON.read_text(encoding="utf-8"))

    problemas = []
    if dados.get("publicar") is not False:
        problemas.append("topo: `publicar` tem de ser `false`")
    if dados.get("ninguem_abriu_nenhum_site") is not True:
        problemas.append("topo: `ninguem_abriu_nenhum_site` tem de ser `true` nesta nuvem, "
                         "ou a lista tem de nomear quem abriu")
    for campo in ("o_que_este_arquivo_e", "por_que_ninguem_abriu",
                  "por_que_nao_existe_false", "o_que_esta_lista_nao_diz"):
        if not dados.get(campo):
            problemas.append("topo: sem `%s`" % campo)

    candidatos = dados.get("candidatos", [])
    if not candidatos:
        problemas.append("topo: nenhum candidato")

    vistos = set()
    for c in candidatos:
        if c.get("id") in vistos:
            problemas.append("%s: id repetido" % c.get("id"))
        vistos.add(c.get("id"))
        problemas += erros_do_candidato(c)

    # O placar e CONTADO deste arquivo, nunca digitado (a 23.4 dentro do dado).
    placar = dados.get("placar") or {}
    contado = {
        "candidatos": len(candidatos),
        "prioridade_1": sum(1 for c in candidatos if prioridade(c) == 1),
        "prioridade_2": sum(1 for c in candidatos if prioridade(c) == 2),
        "prioridade_3": sum(1 for c in candidatos if prioridade(c) == 3),
        "abertos_no_navegador": sum(1 for c in candidatos if c.get("abriu_no_navegador") is True),
    }
    for chave, valor in contado.items():
        if placar.get(chave) != valor:
            problemas.append("placar: `%s` diz %r e a contagem deste arquivo da %d"
                             % (chave, placar.get(chave), valor))

    # O `.md` e regerado em memoria e comparado.
    if not ARQUIVO_MD.exists():
        problemas.append("%s nao existe — rode `gerar-prospeccao.py`" % ARQUIVO_MD.name)
    elif ARQUIVO_MD.read_text(encoding="utf-8") != render_md(dados):
        problemas.append("%s nao bate com o que o JSON gera — rode `gerar-prospeccao.py`"
                         % ARQUIVO_MD.name)

    for p in problemas:
        print("FALHA %s" % p)
    print("\n%d candidato(s), %d prioridade 1, %d prioridade 2, %d prioridade 3."
          % (contado["candidatos"], contado["prioridade_1"],
             contado["prioridade_2"], contado["prioridade_3"]))
    print("%d problema(s)." % len(problemas))
    print("APROVADO" if not problemas else "REPROVADO")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""A REGUA DE UMA COISA SO: esta pagina manda o robo NAO indexar?

Nao e portao, e a regua que dois portoes usam — `teste-robots.py` (bancada) e
`conferir-robots-no-ar.py` (no ar). Mora num arquivo proprio pelo motivo que
esta ilha ja pagou tres vezes: regua escrita duas vezes erra em um dos lados, e
o lado errado fica verde.

POR QUE ELA NASCEU EM 24/09/2026, e a causa e o proprio instrumento
-------------------------------------------------------------------
A leitura semanal de 23/09/2026 abriu um item de despacho dizendo que
`/author/aquametria_gestor/` estava no ar SEM `noindex`, com o criterio de
pronto escrito assim:

    curl -s .../author/aquametria_gestor/ | grep -c 'name="robots"[^>]*noindex'

O DEFEITO NAO EXISTIA. A pagina serve, e servia desde 10/09/2026:

    <meta name='robots' content='noindex, follow' />

ASPAS SIMPLES. Quem imprime a meta nesta ilha e o nucleo do WordPress, pelo
filtro `wp_robots` — e o nucleo usa aspas simples. A regua do despacho pedia
aspas DUPLAS, entao contou zero numa pagina certa. A regua nao veio do nada: nas
ilhas irmas (robometria, clubedomosaico) quem imprime a meta e o SNIPPET, com
aspas duplas, e la o mesmo `grep` esta certo. Foi uma regua correta atravessando
a fronteira de uma ilha onde a tag tem outro autor.

O CUSTO DE UM FALSO POSITIVO NAO E ZERO, e e por isso que isto virou arquivo: o
item mandava ACRESCENTAR `noindex`. Cumprido ao pe da letra por quem confiasse na
medicao, ele acrescentaria uma segunda meta `robots` na pagina — e o Google
resolve meta duplicada pelo lado mais restritivo. O conserto de um defeito
inexistente e que criaria o defeito.

AS TRES COISAS QUE ESTA REGUA FAZ, E QUE O `grep` NAO FAZIA
-----------------------------------------------------------
  1. NAO OLHA ASPA. Aceita `'`, `"` e sem aspa nenhuma, nos dois atributos.
  2. NAO ACEITA A PALAVRA SOLTA. `noindex` tem de estar no `content` de uma meta
     cujo `name` e `robots` — nao num `<script>`, num comentario, num texto de
     pagina, nem numa meta de outro nome. O `grep` de linha aceitava qualquer
     `noindex` que caisse na mesma linha da palavra `robots`.
  3. CONTA. Devolve quantas metas `robots` a pagina serve, porque DUAS e defeito
     tanto quanto zero, e a medicao que so pergunta "tem?" nunca ve a segunda.
  4. LE SO O QUE O NAVEGADOR LE. Comentario HTML e corpo de `<script>` e
     `<style>` saem antes da varredura: tag CITADA nao e tag SERVIDA. Isto nao
     foi previsto e sim medido — os casos 15 e o da contagem em
     `teste-robots.py` ficaram vermelhos na PRIMEIRA passada desta regua, em
     24/09/2026, e a regua e que estava errada. Uma tag comentada contando como
     diretiva e o falso positivo de 23/09 de novo, do outro lado.
"""
import re

# `name` e `content` em qualquer ordem, com aspa simples, dupla ou nenhuma.
META = re.compile(r"<meta\b[^>]*>", re.I)
ATRIBUTO = re.compile(r"""(\w[\w:-]*)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+))""")
# O que o nucleo do WordPress imprime quando o filtro esvazia o mapa: nada. Um
# `content` vazio nao e noindex, e um `content` de "noindexar" tambem nao — a
# diretiva e um item separado por virgula, nunca um pedaco de palavra.
DIRETIVA = re.compile(r"(?:^|,)\s*noindex\s*(?:$|,)", re.I)


# O que a pagina CITA nao e o que ela SERVE. Comentario e corpo de script/style
# saem antes de qualquer varredura de tag.
FORA_DE_LEITURA = re.compile(
    r"<!--.*?-->|<script\b[^>]*>.*?</script\s*>|<style\b[^>]*>.*?</style\s*>",
    re.I | re.S)


def servido(html):
    return FORA_DE_LEITURA.sub(" ", html or "")


def atributos(tag):
    fora = {}
    for m in ATRIBUTO.finditer(tag):
        valor = m.group(2) if m.group(2) is not None else (
            m.group(3) if m.group(3) is not None else (m.group(4) or ""))
        fora[m.group(1).lower()] = valor
    return fora


def metas_de_robots(html):
    """Toda tag <meta name=robots> da pagina, na ordem, so o `content` de cada."""
    fora = []
    for tag in META.findall(servido(html)):
        a = atributos(tag)
        if a.get("name", "").strip().lower() == "robots":
            fora.append(a.get("content", ""))
    return fora


def tem_noindex(html):
    """True se ALGUMA meta robots da pagina traz a diretiva `noindex`."""
    return any(DIRETIVA.search(c) for c in metas_de_robots(html))


def quantas_metas_de_robots(html):
    return len(metas_de_robots(html))

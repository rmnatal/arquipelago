#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o banco de TECNICA de proposito, uma mutacao por vez, e exige que
`validar-banco.py` decida certo em cada uma.

    python3 ferramentas/mutacoes-tecnicas.py

Por que este arquivo existe: `dados/tecnicas.json` nasceu em 14/09/2026 e a regua
que o mede estava escrita desde 12/09 — escrita e NUNCA EXECUTADA, porque o
arquivo nao existia. Regua nessa situacao e verde por ausencia, e verde por
ausencia nao e prova de nada (secao 8 do ARQUIPELAGO.md). Cada mutacao abaixo e
uma forma plausivel de este banco ficar errado em silencio.

A BATERIA TEM OS DOIS LADOS DA FRONTEIRA, e isso e de proposito. Quase toda
mutacao aqui tem de REPROVAR; uma tem de PASSAR. Uma regua que reprova tudo e
tao inutil quanto uma que aprova tudo, e o portao da familia das tecnicas
(3 itens de banco, secao 9) so esta medido quando as duas metades foram vistas:
com zero item, pagina declarada reprova; com o lado do material resolvido, a
MESMA pagina passa. Sem a segunda, ninguem sabe se o portao mede a contagem ou
se ele so odeia o campo.

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


# ------------------------------------------------------------------ mutacoes

def m_id_fora_do_vocabulario(raiz):
    """Alguem acrescenta 'mosaico veneziano' como tecnica nova sem passar pelo
    vocabulario do esquema. E o jeito mais comum de um banco crescer torto."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "indireto")["id"] = "veneziano"
    gravar(raiz, "tecnicas.json", b)


def m_id_repetido(raiz):
    """Duas tecnicas com o mesmo id — duas paginas disputando a mesma URL."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "trencadis")["id"] = "picassiette"
    gravar(raiz, "tecnicas.json", b)


def m_definicao_sem_fonte(raiz):
    """O esquema marca `definicao` com fonte_obrigatoria. Sumir com o ponteiro da
    fonte deixa o texto de pe e a procedencia no chao — que e exatamente o
    defeito que ninguem ve lendo a pagina."""
    b = carregar(raiz, "tecnicas.json")
    del tecnica(b, "bizantino")["definicao_fonte_id"]
    gravar(raiz, "tecnicas.json", b)


def m_definicao_aponta_para_fonte_que_nao_existe(raiz):
    """Pior que nao ter fonte: ter o ponteiro para uma que nao esta na lista. Na
    tela isso vira uma nota de rodape que leva a lugar nenhum."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "bizantino")["definicao_fonte_id"] = "britannica-mosaic"
    gravar(raiz, "tecnicas.json", b)


def m_fonte_de_blog_sustentando_definicao(raiz):
    """A tentacao desta entidade: os blogs de artesanato SAO os que mais escrevem
    sobre tecnica em portugues. O esquema lista tres origens aceitas e blog nao e
    nenhuma delas."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "picassiette")
    t["fontes"]["wikipedia-maison-picassiette"]["origem"] = "blog-de-artesanato"
    gravar(raiz, "tecnicas.json", b)


def m_fonte_perde_a_leitura(raiz):
    """O campo `leitura` e o que declara o elo mais fraco (secao 10 do contrato):
    colhido por busca nao e o mesmo que documento aberto. Sem ele, uma fonte de
    museu parece lida e nao foi."""
    b = carregar(raiz, "tecnicas.json")
    del tecnica(b, "trencadis")["fontes"]["mnceramica-gaudi-trencadis"]["leitura"]
    gravar(raiz, "tecnicas.json", b)


def m_campo_vazio_sem_motivo(raiz):
    """Some o motivo de `junta_tipica_mm` estar vazia. O valor continua null e
    ninguem mais sabe se ele foi medido e nao existe, ou se foi esquecido."""
    b = carregar(raiz, "tecnicas.json")
    del tecnica(b, "direto")["motivo_sem_junta"]
    gravar(raiz, "tecnicas.json", b)


def m_junta_inventada_sem_fonte(raiz):
    """A MUTACAO MAIS PERIGOSA DESTE ARQUIVO, e ela e plausivel demais: alguem
    escreve 3 mm de folga no bizantino porque 'e o que se usa'. Esse numero e
    valor sugerido do campo de entrada da F1 — ou seja, ele chega a uma
    ferramenta que calcula quantas pastilhas e quantos gramas comprar."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "bizantino")
    t["junta_tipica_mm"] = 3
    t.pop("motivo_sem_junta", None)
    gravar(raiz, "tecnicas.json", b)


def m_material_fora_do_vocabulario(raiz):
    """As fontes do trencadis citam vidro entre os cacos e o vocabulario nao tem
    valor para caco de vidro. Inventar `caco_vidro` aqui resolve a frase e quebra
    a unica coisa que liga esta entidade ao banco de material."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "trencadis")["materiais_tipicos"] = ["caco_azulejo", "caco_louca", "caco_vidro"]
    gravar(raiz, "tecnicas.json", b)


def m_material_preenchido_sem_fonte(raiz):
    """Lista de material sem dizer de onde saiu."""
    b = carregar(raiz, "tecnicas.json")
    del tecnica(b, "picassiette")["materiais_tipicos_fonte_id"]
    gravar(raiz, "tecnicas.json", b)


def m_sem_campo_imagem(raiz):
    """O esquema marca `imagem` obrigatoria com tipo objeto|null: null e resposta,
    ausencia nao e. Sumir com a chave e como o campo nunca ter sido pensado."""
    b = carregar(raiz, "tecnicas.json")
    del tecnica(b, "direto")["imagem"]
    gravar(raiz, "tecnicas.json", b)


def m_revisao_inventada(raiz):
    """A revisao da artesa vira um estado que ninguem definiu."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "indireto")["revisao_tecnica"] = "aprovada"
    gravar(raiz, "tecnicas.json", b)


def m_pagina_publicada_com_zero_material(raiz):
    """O PORTAO DA FAMILIA, produzido. E o caminho real pelo qual esta ilha
    publicaria pagina fina: o texto da tecnica esta pronto, a artesa tem peca, e
    alguem decide que ja da para publicar — com ZERO item de banco por tras."""
    b = carregar(raiz, "tecnicas.json")
    tecnica(b, "bizantino")["pagina_publicada"] = True
    gravar(raiz, "tecnicas.json", b)


def m_pagina_publicada_com_o_lado_do_material_resolvido(raiz):
    """O OUTRO LADO DA FRONTEIRA, E ESTA TEM DE PASSAR.

    O dia em que uma fonte sustentar que a tecnica usa pastilha de vidro, os 13
    itens do banco de pastilhas passam a contar e a pagina deixa de ser fina. Se
    esta mutacao reprovar, o portao nao esta medindo a contagem de itens — esta
    apenas proibindo o campo, e ai ele nunca deixaria a familia nascer."""
    b = carregar(raiz, "tecnicas.json")
    t = tecnica(b, "bizantino")
    t["materiais_tipicos"] = ["pastilha_vidro"]
    t["materiais_tipicos_fonte_id"] = "fasbam-mosaicos-bizantinos"
    t.pop("motivo_sem_materiais", None)
    t["pagina_publicada"] = True
    gravar(raiz, "tecnicas.json", b)


MUTACOES = [
    ("id fora do vocabulario de tecnica", m_id_fora_do_vocabulario, "reprova"),
    ("duas tecnicas com o mesmo id", m_id_repetido, "reprova"),
    ("definicao sem dizer de que fonte veio", m_definicao_sem_fonte, "reprova"),
    ("definicao apontando para fonte inexistente", m_definicao_aponta_para_fonte_que_nao_existe, "reprova"),
    ("blog de artesanato sustentando a definicao", m_fonte_de_blog_sustentando_definicao, "reprova"),
    ("fonte perde o campo que declara como foi lida", m_fonte_perde_a_leitura, "reprova"),
    ("campo vazio perde o motivo de estar vazio", m_campo_vazio_sem_motivo, "reprova"),
    ("folga em milimetro inventada, sem fonte", m_junta_inventada_sem_fonte, "reprova"),
    ("material fora do vocabulario (caco de vidro)", m_material_fora_do_vocabulario, "reprova"),
    ("lista de material sem dizer de onde saiu", m_material_preenchido_sem_fonte, "reprova"),
    ("some o campo imagem (null e resposta, ausencia nao)", m_sem_campo_imagem, "reprova"),
    ("estado de revisao que ninguem definiu", m_revisao_inventada, "reprova"),
    ("pagina de tecnica declarada com ZERO item de banco", m_pagina_publicada_com_zero_material, "reprova"),
    ("a MESMA pagina com o lado do material resolvido", m_pagina_publicada_com_o_lado_do_material_resolvido, "aprova"),
]


def rodar_validador(raiz):
    r = subprocess.run([sys.executable, os.path.join(raiz, "ferramentas", "validar-banco.py")],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_validador(ILHA)
    if base_rc != 0:
        print("O banco de verdade ja esta reprovado — conserte antes de mutar.")
        print(base_saida)
        return 1
    print("banco intacto: APROVADO (como tem que estar antes de comecar)\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-tec-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            rc, saida = rodar_validador(copia)
            aprovou = (rc == 0)
            certo = aprovou if esperado == "aprova" else not aprovou
            primeira = ""
            for linha in saida.splitlines():
                if linha.strip().startswith("- "):
                    primeira = linha.strip()[2:]
                    break
            if certo and esperado == "reprova":
                print("  reprovou como devia: %-52s | %s" % (nome, primeira[:92]))
            elif certo:
                print("  passou como devia:   %-52s | a contagem de itens abriu o portao" % nome)
            elif esperado == "reprova":
                erradas.append(nome + " (PASSOU e devia reprovar)")
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                erradas.append(nome + " (REPROVOU e devia passar)")
                print("  REPROVOU e devia passar: %-46s | %s" % (nome, primeira[:92]))
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
